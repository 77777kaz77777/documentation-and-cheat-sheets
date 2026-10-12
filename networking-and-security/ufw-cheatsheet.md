## UFW (Uncomplicated Firewall) Command Reference for Ubuntu/Debian

UFW is a user-friendly frontend for managing iptables (or nftables) firewall rules on Linux. It aims to make basic firewall management simple while still allowing for advanced configurations.

## 1. Service Control & Status

| Command | Description |
| :--- | :--- |
| `sudo ufw status` | Display active firewall status and configured rules. |
| `sudo ufw status verbose` | Show detailed status including default policies, logging level, and active profiles. |
| `sudo ufw status numbered` | Display active rules with index numbers (required for precise deletion or insertion). |
| `sudo ufw enable` | Enable UFW and configure systemd to start the firewall service on boot. **Warning:** Ensure SSH is allowed before enabling! |
| `sudo ufw disable` | Stop UFW and disable automatic launch at system boot. |
| `sudo ufw reload` | Reload configuration files and re-apply rules without dropping active connections. |
| `sudo ufw reset` | Disable UFW and delete all custom rules, returning it to factory defaults. |

## 2. Default Policies

It is best practice to define default behaviors for traffic that does not match any specific rule.

```bash
# Deny all incoming connections (Standard secure baseline)
sudo ufw default deny incoming

# Allow all outgoing connections (Allows your server to reach the internet)
sudo ufw default allow outgoing

# Reject incoming traffic (Sends an ICMP "unreachable" response instead of silently dropping)
sudo ufw default reject incoming

# Allow/Deny routed traffic (Forwarding between interfaces, useful for VPNs/routers)
sudo ufw default allow routed
```

## 3. Application Profiles

UFW can read application profiles (usually located in `/etc/ufw/applications.d`) which bundle port configurations for specific software.

```bash
# List all available application profiles installed on the system
sudo ufw app list

# View details and ports associated with a specific profile
sudo ufw app info "Nginx Full"

# Allow traffic using an application profile
sudo ufw allow "Nginx Full"
sudo ufw allow OpenSSH
```

## 4. Allowing & Denying Traffic

### By Port or Service

```bash
# Allow/Deny by service name (reads from /etc/services)
sudo ufw allow ssh
sudo ufw deny telnet

# Allow/Deny by specific port number
sudo ufw allow 22
sudo ufw deny 23

# Specify TCP or UDP protocol
sudo ufw allow 80/tcp
sudo ufw allow 1194/udp
```

### By Port Ranges

```bash
# Allow TCP port range 6000 to 6007
sudo ufw allow 6000:6007/tcp

# Allow UDP port range 6000 to 6007
sudo ufw allow 6000:6007/udp
```

### Advanced IP and Subnet Rules

```bash
# Allow all incoming connections from a specific IP address
sudo ufw allow from 192.168.1.50

# Deny all incoming connections from a specific IP
sudo ufw deny from 203.0.113.100

# Allow an entire CIDR subnet (e.g., 192.168.1.0 to 192.168.1.255)
sudo ufw allow from 192.168.1.0/24

# Allow a specific IP address to access a specific port (e.g., SSH)
sudo ufw allow from 192.168.1.50 to any port 22

# Allow a specific subnet to access a specific port and protocol (MySQL)
sudo ufw allow from 192.168.1.0/24 to any port 3306 proto tcp

# Specify the destination IP (useful if your server has multiple IP addresses)
sudo ufw allow from 192.168.1.50 to 10.0.0.5 port 22
```

### Outgoing Traffic Rules

If you change the default outgoing policy to `deny`, you must explicitly allow outbound traffic:

```bash
# Allow outbound traffic to a specific port (e.g., HTTP/HTTPS)
sudo ufw allow out 80/tcp
sudo ufw allow out 443/tcp

# Allow outbound traffic to a specific IP address
sudo ufw allow out to 8.8.8.8 port 53 proto udp
```

## 5. Rate Limiting (Brute-Force Protection)

UFW can rate-limit connections to prevent brute-force attacks. By default, it denies connections from an IP address that has attempted to initiate 6 or more connections in the last 30 seconds.

```bash
# Rate limit SSH (Highly recommended if exposed to the internet)
sudo ufw limit ssh

# Rate limit a specific custom port
sudo ufw limit 2222/tcp
```

## 6. Network Interface Specific Rules

You can restrict rules to specific network interfaces (e.g., `eth0`, `wlan0`, `wg0`, `tun0`).

```bash
# Allow incoming traffic on port 80 only on the 'eth0' interface
sudo ufw allow in on eth0 to any port 80

# Deny incoming traffic from a specific IP on a specific interface
sudo ufw deny in on eth0 from 192.168.1.100

# Allow all traffic on a trusted VPN interface (e.g., WireGuard)
sudo ufw allow in on wg0
sudo ufw allow out on wg0
```

## 7. Managing & Editing Rules

### Inserting Rules at a Specific Position

Rules are evaluated top-down. The first matching rule applies.

```bash
# Insert a rule at line number 1 (highest priority)
sudo ufw insert 1 allow from 192.168.1.100 to any port 22

# Insert a rule at line number 3
sudo ufw insert 3 deny from 203.0.113.50
```

### Deleting Rules

```bash
# Method 1: By Line Number (Safest)
sudo ufw status numbered
sudo ufw delete 3   # Deletes the rule at index 3

# Method 2: By Original Syntax
sudo ufw delete allow 80/tcp
sudo ufw delete allow ssh
```

## 8. Logging

Logs are typically stored in `/var/log/ufw.log`, `/var/log/syslog`, or `/var/log/kern.log` depending on your Linux distribution.

```bash
# Enable firewall logging
sudo ufw logging on

# Set logging level (options: low, medium, high, full)
# 'low' logs blocked packets not matching defined policy (default)
# 'medium' adds logs for allowed packets not matching defined policy
sudo ufw logging medium

# Disable logging
sudo ufw logging off
```
