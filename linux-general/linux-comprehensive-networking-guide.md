# Linux Comprehensive Networking Tools Guide

This document covers the configuration, management, and troubleshooting of networking interfaces across all major Linux distributions, utilizing both modern standard and legacy tools.

## 1. NetworkManager (`nmcli` and `nmtui`)
**Standard on:** Fedora, RHEL, AlmaLinux, Rocky Linux, CentOS, openSUSE, and most Desktop Environments (KDE, GNOME).

### Viewing Network Status
```bash
nmcli general status
nmcli connection show
nmcli device status
```

### Configuring a Static IP (IPv4)
```bash
sudo nmcli connection modify "System eth0" ipv4.addresses 192.168.1.50/24
sudo nmcli connection modify "System eth0" ipv4.gateway 192.168.1.1
sudo nmcli connection modify "System eth0" ipv4.dns "1.1.1.1,8.8.8.8"
sudo nmcli connection modify "System eth0" ipv4.method "manual"
```

### Configuring DHCP (IPv4)
```bash
sudo nmcli connection modify "System eth0" ipv4.method "auto"
sudo nmcli connection modify "System eth0" ipv4.addresses ""
sudo nmcli connection modify "System eth0" ipv4.gateway ""
sudo nmcli connection modify "System eth0" ipv4.dns ""
```

### Applying Changes
```bash
sudo nmcli connection down "System eth0"
sudo nmcli connection up "System eth0"
```

---

## 2. Netplan
**Standard on:** Ubuntu (Server and Desktop, 18.04 LTS and newer).

### Configuration File Layout
Configuration files are located in `/etc/netplan/` (e.g., `01-netcfg.yaml`). 

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:
      dhcp4: no
      addresses:
        - 192.168.1.50/24
      routes:
        - to: default
          via: 192.168.1.1
      nameservers:
        addresses:
          - 1.1.1.1
          - 8.8.8.8
```

### Testing and Applying Configurations
```bash
sudo netplan generate
sudo netplan try
sudo netplan apply
```

---

## 3. systemd-networkd
**Standard on:** Arch Linux, Flatcar Container Linux, generic lightweight/containerized distributions.

### Configuration File Layout
Configuration files are located in `/etc/systemd/network/` (e.g., `20-wired.network`).

```ini
[Match]
Name=eth0

[Network]
DHCP=no
Address=192.168.1.50/24
Gateway=192.168.1.1
DNS=1.1.1.1
DNS=8.8.8.8
```

### Applying Changes
```bash
sudo systemctl daemon-reload
sudo systemctl restart systemd-networkd
sudo networkctl reload
```

### Viewing Status
```bash
networkctl status
networkctl status eth0
```

---

## 4. ifupdown (Debian Interfaces)
**Standard on:** Legacy Debian, Devuan, Alpine Linux (similar syntax).

### Configuration File Layout
The primary configuration file is `/etc/network/interfaces`.

```text
auto eth0
iface eth0 inet static
    address 192.168.1.50
    netmask 255.255.255.0
    gateway 192.168.1.1
    dns-nameservers 1.1.1.1 8.8.8.8
```

### Applying Changes
```bash
sudo ifdown eth0
sudo ifup eth0
sudo systemctl restart networking
```

---

## 5. sysconfig / network-scripts (Legacy Red Hat)
**Standard on:** RHEL 7, CentOS 7, and older variants (Deprecated in favor of NetworkManager).

### Configuration File Layout
Configuration files are located in `/etc/sysconfig/network-scripts/` (e.g., `ifcfg-eth0`).

```ini
TYPE=Ethernet
BOOTPROTO=none
NAME=eth0
DEVICE=eth0
ONBOOT=yes
IPADDR=192.168.1.50
PREFIX=24
GATEWAY=192.168.1.1
DNS1=1.1.1.1
DNS2=8.8.8.8
```

### Applying Changes
```bash
sudo systemctl restart network
```

---

## 6. iproute2 (Universal Temporary Networking)
**Standard on:** All modern Linux distributions (Replaces legacy `net-tools`).
**Warning:** All configurations applied via `iproute2` commands are temporary and will be wiped upon system reboot.

### Viewing Information
```bash
ip link show
ip addr show
ip route show
ip -s link show eth0
```

### Interface State Management
```bash
sudo ip link set dev eth0 down
sudo ip link set dev eth0 up
```

### IP Address Management
```bash
sudo ip addr flush dev eth0
sudo ip addr add 192.168.1.50/24 dev eth0
sudo ip addr del 192.168.1.50/24 dev eth0
```

### Routing Management
```bash
sudo ip route add default via 192.168.1.1
sudo ip route del default via 192.168.1.1
sudo ip route add 10.0.0.0/8 via 192.168.1.254 dev eth0
```

---

## 7. net-tools (Legacy / Deprecated)
**Standard on:** Older UNIX and legacy Linux environments. Replaced by `iproute2`.

### Viewing Information
```bash
ifconfig -a
route -n
netstat -tulpn
arp -a
```

### Interface and IP Management
```bash
sudo ifconfig eth0 down
sudo ifconfig eth0 up
sudo ifconfig eth0 192.168.1.50 netmask 255.255.255.0
sudo route add default gw 192.168.1.1 eth0
```

---

### Verification and DNS Testing
These tools are universally applicable across all distributions for verifying network connectivity and name resolution.

**Ping (ICMP Test):**
```bash
ping -c 4 1.1.1.1
ping -c 4 google.com
```

**DNS Resolution:**
```bash
dig google.com
nslookup google.com
resolvectl query google.com
```

**Trace Route:**
```bash
traceroute 1.1.1.1
mtr 1.1.1.1
```

### Sources
* **NetworkManager:** Red Hat Official Documentation, GNOME NetworkManager Reference.
* **Netplan:** Canonical Netplan Official Documentation.
* **systemd-networkd:** FreeDesktop systemd.network manual.
* **iproute2:** Linux Foundation iproute2 suite documentation.
* **Debian Interfaces:** Debian Administrator's Handbook.
