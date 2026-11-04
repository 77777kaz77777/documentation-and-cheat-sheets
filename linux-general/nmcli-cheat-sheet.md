## Commands for managing network interfaces and Wi-Fi connections via nmcli

# nmcli Cheat Sheet

`nmcli` (NetworkManager Command Line Interface) is a command-line tool for controlling NetworkManager and reporting network status.

## General Information

**Show help for nmcli:**
```bash
nmcli help
```

**Show overall network status:**
```bash
nmcli general status
```

**Get/Set logging level:**
```bash
nmcli general logging
```

## Device Management

**List all network devices:**
```bash
nmcli device
```

**Show status of all devices:**
```bash
nmcli device status
```

**Show detailed information for a device:**
```bash
nmcli device show [device]
```

**Connect a device:**
```bash
nmcli device connect [device]
```

**Disconnect a device:**
```bash
nmcli device disconnect [device]
```

## Connection Management

**List all connections:**
```bash
nmcli connection show
```

**List only active connections:**
```bash
nmcli connection show --active
```

**Show details of a connection:**
```bash
nmcli connection show [name]
```

**Activate a connection:**
```bash
nmcli connection up [name]
```

**Deactivate a connection:**
```bash
nmcli connection down [name]
```

**Delete a connection profile:**
```bash
nmcli connection delete [name]
```

**Modify a connection setting:**
```bash
nmcli connection modify [name] [param] [value]
```

## Practical Examples

### Wi-Fi

- **Scan for Wi-Fi networks:**
  `nmcli device wifi list`

- **Connect to a Wi-Fi network:**
  `nmcli device wifi connect "SSID_NAME" password "YOUR_PASSWORD"`

### Ethernet/IP Configuration

- **Set static IP address:**

  ```text
  nmcli connection modify "Wired connection 1" ipv4.addresses 192.168.1.100/24
  nmcli connection modify "Wired connection 1" ipv4.gateway 192.168.1.1
  nmcli connection modify "Wired connection 1" ipv4.dns 8.8.8.8
  nmcli connection modify "Wired connection 1" ipv4.method manual
  nmcli connection up "Wired connection 1"
  ```
