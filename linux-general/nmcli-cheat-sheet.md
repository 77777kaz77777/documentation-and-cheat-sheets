## Commands for managing network interfaces and Wi-Fi connections via nmcli

# nmcli Cheat Sheet

`nmcli` (NetworkManager Command Line Interface) is a command-line tool for controlling NetworkManager and reporting network status.

## General Information

| Command | Description |
| :--- | :--- |
| `nmcli help` | Show help for nmcli |
| `nmcli general status` | Show overall network status |
| `nmcli general logging` | Get/Set logging level |

## Device Management

| Command | Description |
| :--- | :--- |
| `nmcli device` | List all network devices |
| `nmcli device status` | Show status of all devices |
| `nmcli device show [device]` | Show detailed information for a device |
| `nmcli device connect [device]` | Connect a device |
| `nmcli device disconnect [device]` | Disconnect a device |

## Connection Management

| Command | Description |
| :--- | :--- |
| `nmcli connection show` | List all connections |
| `nmcli connection show --active` | List only active connections |
| `nmcli connection show [name]` | Show details of a connection |
| `nmcli connection up [name]` | Activate a connection |
| `nmcli connection down [name]` | Deactivate a connection |
| `nmcli connection delete [name]` | Delete a connection profile |
| `nmcli connection modify [name] [param] [value]` | Modify a connection setting |

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
