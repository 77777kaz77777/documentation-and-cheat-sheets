# Comprehensive Post-Wi-Fi Hardware Replacement Diagnostic Guide

## 1. Hardware Detection & Bus Audit

Audit the hardware bus to confirm physical seating, PCIe/USB bus enumeration, and vendor device IDs.

### 1.1 PCI Express Bus Audit

```bash
# Query PCI wireless controllers and display active kernel drivers
lspci \
  -nnk \
  | grep \
  -A 3 \
  -i network
```

* **Expected Output:** Shows the card's vendor ID, product name (e.g., MediaTek MT7922 / Intel AX210), and the `Kernel driver in use:` line.
* **Verification:** If no output appears, the card is not physically seated in the M.2 slot or lacks PCIe power.

### 1.2 USB Bus Audit (For USB-based Wi-Fi Modules)

```bash
# Query USB bus hierarchy for wireless dongles or M.2 USB-interface cards
lsusb \
  -t \
  | grep \
  -i \
  -A 2 \
  -B 2 \
  wireless
```

* **Verification:** Device must be enumerated with an assigned driver (`btusb`, `rtw88`, etc.).

---

## 2. Kernel Module & Firmware Verification

Verify kernel driver module initialization and ensure the hardware vendor's firmware binaries load without errors.

### 2.1 Driver Module Loading

```bash
# List active wireless driver modules in kernel memory
lsmod \
  | grep \
  -E 'mt79|iwl|ath|rtw|b43'
```

* **Verification:** Confirm the relevant driver module (e.g., `mt7921e` for MediaTek MT7921/MT7922, `iwlwifi` for Intel, `rtw89` for Realtek) is listed as loaded.

### 2.2 Kernel Ring Buffer Audit

```bash
# Inspect boot logs for hardware initialization and firmware load traps
sudo dmesg \
  | grep \
  -iE 'wlan|firmware|wifi|mt79|iwl|ath|rtw'
```

* **Verification:** Look for lines indicating firmware load success (e.g., `firmware: direct-loading firmware...`).
* **Troubleshooting:** If `dmesg` reports `failed to load firmware (-2)`, install missing binary blobs:

```bash
# On Fedora / RHEL
sudo dnf \
  reinstall \
  linux-firmware
```

```bash
# On Debian / Ubuntu
sudo apt \
  install \
  --reinstall \
  firmware-linux-free \
  firmware-linux-nonfree
```

---

## 3. Radio Frequency & Interface Management

Ensure the system creates the logical interface and that software or hardware kill switches are cleared.

### 3.1 Interface Identification

```bash
# List all wireless network interfaces
ip link \
  show \
  type wifi

# Alternatively:
iw dev
```

* **Verification:** Identify your active wireless interface name (e.g., `wlan0`, `wlp2s0`, `wlp3s0`).

### 3.2 RF Kill State Audit & Clearing

```bash
# Check physical and software wireless block states
rfkill \
  list \
  all

# Clear all software blocks across Wi-Fi and Bluetooth
sudo rfkill \
  unblock \
  all
```

* **Verification:** Confirm that both `Soft blocked` and `Hard blocked` report `no` for `Wireless LAN` and `Bluetooth`.

### 3.3 Set Regulatory Domain

```bash
# Display active wireless regulatory domain
sudo iw \
  reg \
  get

# Manually set region code (e.g., CA for Canada, US for United States)
sudo iw \
  reg \
  set \
  CA
```

* **Verification:** Running `sudo iw reg get` reflects your specified country code to unlock region-specific 5 GHz and 6 GHz channels.

---

## 4. Network Scanning & NetworkManager Profile Purging

Perform active scanning and clean up legacy profiles tied to old MAC addresses or interface names.

### 4.1 Rescan & AP Identification

```bash
# Bring interface online manually if state is DOWN
sudo ip \
  link \
  set \
  <interface> \
  up

# Force NetworkManager to rescan available access points
nmcli \
  device \
  wifi \
  rescan

# Display detailed scan results
nmcli \
  device \
  wifi \
  list
```

* **Verification:** Confirm target SSID appears with appropriate signal strength (`SIGNAL`), channel (`CHAN`), and security protocols.

### 4.2 Legacy Profile Cleanup

```bash
# Display saved NetworkManager connection profiles
nmcli \
  connection \
  show

# Remove orphaned network profiles tied to replaced hardware MAC addresses
sudo nmcli \
  connection \
  delete \
  "OLD_PROFILE_NAME"
```

* **Verification:** Running `nmcli connection show` confirms legacy connections are removed.

### 4.3 Connect to Target Access Point

```bash
# Connect to access point via nmcli
nmcli \
  device \
  wifi \
  connect \
  "SSID_NAME" \
  password \
  "WIFI_PASSWORD"
```

* **Verification:** `nmcli device` reports the interface state as `connected`.

---

## 5. Network Layer & DNS Routing Diagnostics

Verify IP assignment, default gateway routing, and systemd DNS resolution.

### 5.1 IP & Gateway Route Inspection

```bash
# Verify IPv4 and IPv6 address allocation
ip addr \
  show \
  dev \
  <interface>

# Inspect default routing table
ip route \
  show
```

* **Verification:** Confirm an IP address (DHCP or static) is bound to the interface and a `default via <GATEWAY_IP>` route exists.

### 5.2 DNS Resolution & Connectivity Test

```bash
# Check systemd-resolved DNS status
resolvectl \
  status \
  <interface>

# Test end-to-end ICMP connectivity and DNS lookup
ping \
  -c 4 \
  1.1.1.1

ping \
  -c 4 \
  fedoraproject.org
```

* **Verification:** Packet loss must be 0%, and domain name queries must resolve to valid IP addresses.

---

## 6. Power Management & Latency Optimization

Disable aggressive wireless power saving to prevent intermittent latency spikes, packet drops, or unexpected disconnections.

### 6.1 Inspect Power Save Status

```bash
# Read interface power management status
iw \
  dev \
  <interface> \
  get \
  power_save
```

* **Verification:** Displays whether wireless power saving is currently `on` or `off`.

### 6.2 Disable Power Save in NetworkManager (Persistent)

```bash
# Disable power save for a specific connection profile (2 = disabled, 3 = enabled)
sudo nmcli \
  connection \
  modify \
  "SSID_NAME" \
  802-11-wireless.powersave \
  2
```

```ini
# Global configuration override (Fedora / RHEL / Arch)
# /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf
[connection]
wifi.powersave = 2
```

```bash
# Restart NetworkManager to apply
sudo systemctl \
  restart \
  NetworkManager
```

* **Verification:** Running `iw dev <interface> get power_save` outputs `Power save: off`.

---

## 7. Bluetooth Coexistence & Controller Setup

Modern Wi-Fi cards are combo modules housing Bluetooth on an internal USB protocol bus. Verify Bluetooth stack integration.

### 7.1 Bluetooth Controller Status

```bash
# Inspect Bluetooth service state
systemctl \
  status \
  bluetooth.service

# Verify Bluetooth adapter hardware recognition
bluetoothctl \
  show
```

* **Verification:** `bluetoothctl show` displays controller details including MAC address and `Powered: yes`.

### 7.2 Unblock & Restart Bluetooth Stack

```bash
# Unblock Bluetooth radio
sudo rfkill \
  unblock \
  bluetooth

# Restart Bluetooth service
sudo systemctl \
  restart \
  bluetooth
```

* **Verification:** Run `bluetoothctl devices` to verify active scanning and discovery of nearby Bluetooth devices.

---

## 8. Diagnostic Command Reference Matrix

| Diagnostic Stage | Command | Success Indicator |
| --- | --- | --- |
| **PCI Hardware** | `lspci -nnk \| grep -A 3 -i network` | Driver module listed under `Kernel driver in use` |
| **Kernel Log** | `sudo dmesg \| grep -iE 'mt79\|iwl\|ath\|rtw'` | `firmware: direct-loading...` with no failure code |
| **RF Block State** | `rfkill list all` | `Soft blocked: no`, `Hard blocked: no` |
| **Scanning** | `nmcli device wifi list` | Target SSIDs listed with signal percentages |
| **Connection** | `nmcli device wifi connect "SSID" password "PASS"` | `Device 'wlan0' successfully activated` |
| **Routing** | `ip route show` | `default via <gateway_ip> dev <interface>` present |
| **DNS Resolution** | `resolvectl status` | Valid DNS servers listed under interface |
| **Power Management** | `iw dev <interface> get power_save` | `Power save: off` |
