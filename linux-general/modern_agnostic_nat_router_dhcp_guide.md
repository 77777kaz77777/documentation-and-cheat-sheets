# Modern Distro-Agnostic NAT Router & DHCP Server

This guide and automation script turns any Linux system (Virtual Machine, LXC/LXD Container, or Bare-Metal Server) into a lightweight, high-performance **NAT Router, DHCP Server, and Caching DNS Forwarder**.

🔗 **Script Repository:** [setup-router.sh on GitHub](https://github.com/77777kaz77777/sysadmin-automation-scripts/blob/main/networking/setup-router.sh)

---

## 🚀 Why This Script Was Modernized

Legacy Linux routing scripts typically rely on outdated tools (`iptables`, `isc-dhcp-server`, and `apt-get`) that are either deprecated or locked to Debian-based distributions. Here is how this script upgrades the stack:

1. **Distro-Agnostic Package Management:** Automatically detects and supports `apt` (Debian/Ubuntu), `dnf` (RHEL/Fedora/Alma/Rocky), `pacman` (Arch), and `zypper` (openSUSE).
2. **`nftables` instead of `iptables`:** Replaces legacy `iptables` and `iptables-persistent` with a clean, atomic `nftables` ruleset (`/etc/nftables.conf`) for faster packet filtering and NAT masquerading.
3. **`dnsmasq` instead of `isc-dhcp-server`:** Uses `dnsmasq` to provide both DHCP and local caching DNS. Note that ISC has officially ended maintenance for `isc-dhcp-server`.
4. **Systemd-Resolved Deconfliction:** Automatically detects if `systemd-resolved` is occupying port 53 (common on modern Ubuntu/Fedora systems) and safely disables the stub listener so `dnsmasq` can bind cleanly.
5. **Strict Error Handling:** Uses `set -euo pipefail` and avoids dangerous variable exports in favor of scoped evaluation.

---

## 🗺️ Network Architecture

```text
                        +---------------------------------------+
                        |          LINUX NAT ROUTER             |
                        |         (VM or LXC Container)         |
+--------------+        |                                       |        +-------------------+
|              |  WAN   |  +---------------------------------+  |  LAN   |   LAN Switch /    |
| The Internet |=======>|  | IPv4 Forwarding + nftables NAT  |  |=======>|  Internal Bridge  |
|              | (eth0) |  +---------------------------------+  | (eth1) |  (192.168.1.0/24) |
+--------------+        |  |     dnsmasq (DHCP + DNS)        |  |        +-------------------+
                        |  +---------------------------------+  |          |       |       |
                        +---------------------------------------+          v       v       v
                                                                         [Client VMs / Devices]
                                                                       DHCP: 192.168.1.10 - .100
                                                                       Gateway/DNS: 192.168.1.1
```

* **WAN Interface (e.g., `eth0`):** Connects to your upstream network or the Internet. Outbound traffic from the LAN is masqueraded behind this interface's IP address.
* **LAN Interface (e.g., `eth1`):** Configured with a static gateway IP (`192.168.1.1/24` by default). `dnsmasq` listens exclusively on this interface to hand out IP leases and resolve DNS queries for downstream clients.

---

## 🛠️ Environment Setup Guide

### Option 1: Virtual Machine Setup (Proxmox / KVM / VirtualBox / VMware)

A Virtual Machine provides complete kernel isolation and is the most straightforward way to deploy a dedicated router.

1. **Create the VM:**
   * **CPU:** 1–2 vCPUs
   * **RAM:** 512 MB – 1 GB
   * **Storage:** 8–10 GB
   * **OS:** Any modern Linux distro (Debian 12, Ubuntu 24.04, Rocky Linux 9, Arch, etc.)
2. **Configure Network Interfaces:**
   * **Network Adapter 1 (WAN / `eth0`):** Attach to your hypervisor's main **Bridged** or **NAT** network that has Internet access.
   * **Network Adapter 2 (LAN / `eth1`):** Attach to an **Isolated Internal Network** or a dedicated **Linux Bridge / VLAN** (e.g., `vmbr1` in Proxmox) with **no hypervisor DHCP enabled**.
3. **Attach Client VMs:**
   * Connect your downstream test VMs to that same isolated LAN bridge (`vmbr1` / Internal Network) so they request DHCP leases from your new router VM.

---

### Option 2: Container Setup (LXD / Incus / Proxmox LXC)

> **⚠️ Note on Docker:** Running a full NAT router and DHCP server inside a standard Docker container is an anti-pattern because Docker manages its own `iptables`/`nftables` chains and network namespaces. **LXC/LXD system containers** are strongly recommended instead.

1. **Create an Isolated LAN Bridge on the Host:**

   ```bash
   lxc network create lan0 ipv4.address=none ipv6.address=none
   ```

2. **Launch the Router Container:**

   ```bash
   lxc launch images:debian/12 router-ct
   ```

3. **Attach WAN and LAN Interfaces:**

   ```bash
   # Attach WAN interface (connected to default internet-facing lxdbr0)
   lxc config device add router-ct eth0 nic nictype=bridged parent=lxdbr0 name=eth0

   # Attach LAN interface (connected to isolated lan0 bridge)
   lxc config device add router-ct eth1 nic nictype=bridged parent=lan0 name=eth1
   ```

4. **Grant Networking Capabilities:**
   To manipulate `nftables` and bind raw sockets for DHCP, ensure the container has sufficient permissions:

   ```bash
   lxc config set router-ct security.privileged true
   lxc restart router-ct
   ```

---

## ⚡ Quick Start & Installation

You can download and run the script directly from the [GitHub Repository](https://github.com/77777kaz77777/sysadmin-automation-scripts/blob/main/networking/setup-router.sh):

```bash
# Download the script from GitHub
curl -fsSL https://raw.githubusercontent.com/77777kaz77777/sysadmin-automation-scripts/main/networking/setup-router.sh -o setup-router.sh

# Make it executable
chmod +x setup-router.sh

# Run as root
sudo ./setup-router.sh
```

---

## 📜 Full Script (`setup-router.sh`)

Below is the complete source code for reference:

```bash
#!/usr/bin/env bash
# Configure NAT Router + DHCP/DNS Server (Distro-Agnostic & Modern)
# Source: https://github.com/77777kaz77777/sysadmin-automation-scripts/blob/main/networking/setup-router.sh
# Must be run as root

set -euo pipefail

#--- Help and Guard Rails
if [ "$EUID" -ne 0 ]; then
  echo "Error: This script must be run as root. Exiting." >&2
  exit 1
fi

#--- Utility: Distro & Package Manager Detection
detect_pkg_manager() {
  if command -v apt-get >/dev/null; then
    PACKAGER="apt"
  elif command -v dnf >/dev/null; then
    PACKAGER="dnf"
  elif command -v pacman >/dev/null; then
    PACKAGER="pacman"
  elif command -v zypper >/dev/null; then
    PACKAGER="zypper"
  else
    echo "Error: Supported package manager (apt, dnf, zypper, pacman) not found." >&2
    exit 1
  fi
}

#--- Utility: Install Packages Agnostically
install_packages() {
  local pkgs=("$@")
  echo "Installing packages (${pkgs[*]}) using $PACKAGER..."
  case "$PACKAGER" in
    apt)
      DEBIAN_FRONTEND=noninteractive apt-get update -y
      DEBIAN_FRONTEND=noninteractive apt-get install -y "${pkgs[@]}"
      ;;
    dnf)
      dnf install -y "${pkgs[@]}"
      ;;
    pacman)
      pacman -Sy --noconfirm "${pkgs[@]}"
      ;;
    zypper)
      zypper --non-interactive install "${pkgs[@]}"
      ;;
  esac
}

#--- Helper to prompt with a default value
prompt() {
  local var_name="$1" prompt_text="$2" default="$3"
  local input
  read -r -p "$prompt_text [$default]: " input
  eval "$var_name=\"\${input:-\$default}\""
}

echo "============================================="
echo "   MODERN AGNOSTIC NAT + DHCP ROUTER SETUP   "
echo "============================================="

# Detect Package Manager
detect_pkg_manager

# Gathering Network Parameters
prompt WAN_IF "Enter your WAN (Internet) interface" "eth0"
prompt LAN_IF "Enter your LAN (Private) interface" "eth1"
prompt LAN_IP "Enter LAN Gateway IP address" "192.168.1.1"
prompt LAN_NET "Enter LAN Network subnet (CIDR format)" "192.168.1.0/24"
prompt DHCP_START "Enter DHCP range start IP" "192.168.1.10"
prompt DHCP_END "Enter DHCP range end IP" "192.168.1.100"
prompt DNS_SERVERS "Enter Upstream DNS servers (comma-separated)" "1.1.1.1,8.8.8.8"

echo
echo "1) Enabling IPv4 Forwarding..."
mkdir -p /etc/sysctl.d
echo "net.ipv4.ip_forward = 1" > /etc/sysctl.d/99-router-forward.conf
sysctl -p /etc/sysctl.d/99-router-forward.conf || sysctl --system

echo
echo "2) Assigning IP Address to LAN Interface ($LAN_IF)..."
# Set LAN gateway interface IP
ip addr replace "$LAN_IP/24" dev "$LAN_IF" || true
ip link set "$LAN_IF" up

echo
echo "3) Setting up Firewall & NAT using nftables..."
# Ensure nftables is installed
if ! command -v nft >/dev/null; then
  install_packages nftables
fi

# Create and apply modern nftables rulesets (supports fast masquerade & routing)
cat <<EOF > /etc/nftables.conf
#!/usr/sbin/nft -f

flush ruleset

table inet filter {
    chain input {
        type filter hook input priority filter; policy accept;
        # Allow internal traffic & established connections
        iifname "lo" accept
        ct state established,related accept
    }

    chain forward {
        type filter hook forward priority filter; policy drop;
        # Forward LAN to WAN
        iifname "$LAN_IF" oifname "$WAN_IF" accept
        # Allow established back in
        iifname "$WAN_IF" oifname "$LAN_IF" ct state established,related accept
    }
}

table ip nat {
    chain postrouting {
        type nat hook postrouting priority srcnat; policy accept;
        # Modern Masquerade for outbound LAN traffic
        oifname "$WAN_IF" ip saddr $LAN_NET masquerade
    }
}
EOF

nft -f /etc/nftables.conf
systemctl enable nftables || true
systemctl restart nftables || true

echo
echo "4) Configuring DHCP and DNS using dnsmasq..."
# Install dnsmasq (highly efficient combined DNS & DHCP)
if ! command -v dnsmasq >/dev/null; then
  install_packages dnsmasq
fi

# Deconflict with Systemd-Resolved if present (Standard on modern Ubuntu/Systemd OS)
if systemctl is-active --quiet systemd-resolved 2>/dev/null; then
  echo "De-conflicting Systemd-Resolved on port 53..."
  mkdir -p /etc/systemd/resolved.conf.d || true
  cat <<EOF > /etc/systemd/resolved.conf.d/dnsmasq.conf
[Resolve]
DNSStubListener=no
EOF
  systemctl restart systemd-resolved || true
fi

# Make a backup of any current dnsmasq config
[ -f /etc/dnsmasq.conf ] && mv /etc/dnsmasq.conf /etc/dnsmasq.conf.bak

# Setup brand new optimized Dnsmasq Config
cat <<EOF > /etc/dnsmasq.conf
# Interfaces to listen on
interface=$LAN_IF
bind-interfaces

# DHCP range and lease time
dhcp-range=$DHCP_START,$DHCP_END,255.255.255.0,12h

# Gateway (Router)
dhcp-option=3,$LAN_IP

# Upstream DNS
$(for dns in ${DNS_SERVERS//,/ }; do echo "server=$dns"; done)
# DNS servers to hand out to DHCP clients
dhcp-option=6,$LAN_IP

# Set DHCP Lease store
dhcp-leasefile=/var/lib/misc/dnsmasq.leases

# Logging
log-facility=/var/log/dnsmasq.log
log-queries
log-dhcp
EOF

# Ensure lease directory exists across distros
mkdir -p /var/lib/misc

# Restart/Activate Service
systemctl enable dnsmasq
systemctl restart dnsmasq

echo
echo "=== SETUP COMPLETE! ==="
echo "WAN Link:       $WAN_IF"
echo "LAN Link:       $LAN_IF ($LAN_IP)"
echo "LAN Subnet:     $LAN_NET"
echo "DHCP Pool:      $DHCP_START → $DHCP_END"
echo "Upstream DNS:   $DNS_SERVERS"
echo "============================================="
```

---

## 🔍 Verification & Troubleshooting

Once you have run the script, you can verify everything is working using these commands:

* **Check Active `nftables` Rules:**

  ```bash
  sudo nft list ruleset
  ```

* **Check `dnsmasq` Service & Logs:**

  ```bash
  sudo systemctl status dnsmasq
  sudo tail -f /var/log/dnsmasq.log
  ```

* **View Active DHCP Leases:**

  ```bash
  cat /var/lib/misc/dnsmasq.leases
  ```

* **Persist LAN IP Across Reboots:**
   note that `ip addr replace` configures the interface immediately in memory. To ensure the static IP on `$LAN_IF` persists across full system reboots, add `192.168.1.1/24` to your distribution's network manager (`/etc/network/interfaces`, Netplan, or `nmcli`).
