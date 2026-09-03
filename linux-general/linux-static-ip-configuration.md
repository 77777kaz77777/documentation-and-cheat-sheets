# Linux Static IP Configuration Guide

## Step 0: Identify Network Details

Before making changes, determine your active interface and current routing information.

**Find interface name (e.g., `eth0`, `enp3s0`):**

```bash
ip addr
```

**Find default gateway:**

```bash
ip route
```

*(Look for the line starting with `default via`)*

---

## 1. NetworkManager (`nmcli`)

**Best for:** Fedora, RHEL, CentOS, AlmaLinux, and desktop environments like KDE. This is the simplest and most recommended method for standard workstation and laptop setups.

**Identify Connection Name:**

```bash
nmcli connection show
```

*(Locate the "NAME" column for your active device, e.g., "System eth0" or "Wired connection 1")*.

**Apply Static Configuration:**

```bash
sudo nmcli connection modify "System eth0" ipv4.addresses 192.168.1.100/24
sudo nmcli connection modify "System eth0" ipv4.gateway 192.168.1.1
sudo nmcli connection modify "System eth0" ipv4.dns "1.1.1.1,8.8.8.8"
sudo nmcli connection modify "System eth0" ipv4.method "manual"
```

**Restart the Connection:**

```bash
sudo nmcli connection down "System eth0"
sudo nmcli connection up "System eth0"
```

---

## 2. Netplan

**Best for:** Modern Ubuntu systems.

**Locate Configuration File:**
Find your YAML configuration file inside `/etc/netplan/` (e.g., `01-netcfg.yaml` or `50-cloud-init.yaml`).

**Configuration File (`/etc/netplan/01-netcfg.yaml`):**
Replace the contents of the file completely with the updated configuration block below.

```yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: no
      addresses:
        - 192.168.1.100/24
      routes:
        - to: default
          via: 192.168.1.1
      nameservers:
        addresses:
          - 1.1.1.1
          - 8.8.8.8
```

**Test and Apply:**
Always test before applying so Netplan can roll back if you lose connection.

```bash
sudo netplan try
sudo netplan apply
```

---

## 3. systemd-networkd

**Best for:** Arch Linux, lightweight server deployments, and containerized setups.

**Configuration File (`/etc/systemd/network/10-static-eth0.network`):**
Create or overwrite this file entirely with the block below.

```ini
[Match]
Name=eth0

[Network]
Address=192.168.1.100/24
Gateway=192.168.1.1
DNS=1.1.1.1
DNS=8.8.8.8
```

**Apply and Enable:**

```bash
sudo systemctl restart systemd-networkd
sudo systemctl enable systemd-networkd
```

---

## 4. iproute2 (Temporary / Session-Only)

**Best for:** Rescue environments or testing. **Warning:** Changes made with `ip` will be lost upon reboot.

**Flush DHCP IP and Apply Static:**

```bash
sudo ip addr flush dev eth0
sudo ip addr add 192.168.1.100/24 dev eth0
sudo ip route add default via 192.168.1.1
```

**Set Temporary DNS:**

```bash
echo "nameserver 1.1.1.1" | sudo tee /etc/resolv.conf
```

---

### Verification and Sources

* **Verify changes:** Run `ip addr` to check the IP, and ping an external address (e.g., `ping 1.1.1.1`) to verify the gateway.
* **Sources verified via:** ElderNode Linux Static IP Guide, `nmcli` Documentation, Canonical Netplan Reference, systemd.network manual.
