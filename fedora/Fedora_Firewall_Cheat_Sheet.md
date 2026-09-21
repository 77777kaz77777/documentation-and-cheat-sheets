# Firewalld Cheat Sheet (Fedora / RHEL / CentOS)

Fedora and other RHEL-based distributions use **firewalld** as the default dynamic firewall manager. It uses the concept of "Zones" to define trust levels for network connections and interfaces.

> **Crucial Concept: Runtime vs. Permanent**
> *   Commands run *without* `--permanent` apply immediately but are lost on reboot or reload.
> *   Commands run *with* `--permanent` are saved to disk but do not apply immediately. You must run `sudo firewall-cmd --reload` to activate them.

## 1. Service Control & Status

Manage the underlying `firewalld` system service and check overall status.

| Command | Description |
| :--- | :--- |
| `sudo systemctl status firewalld` | Check if the firewalld systemd service is running. |
| `sudo systemctl enable --now firewalld`| Start firewalld and enable it to launch on boot. |
| `sudo firewall-cmd --state` | Quick check to see if the firewall is actively running. |
| `sudo firewall-cmd --reload` | Reload permanent rules into runtime (does not drop connections). |
| `sudo firewall-cmd --complete-reload` | Reload rules and *drop* all active connections (use if state matching breaks). |

## 2. Managing Zones

Zones dictate the default behavior for incoming traffic on the interfaces or sources assigned to them. 

| Command | Description |
| :--- | :--- |
| `sudo firewall-cmd --get-default-zone` | View the current default zone. |
| `sudo firewall-cmd --set-default-zone=public` | Set the default zone for all unassigned interfaces. |
| `sudo firewall-cmd --get-active-zones` | List currently active zones and their bound interfaces/sources. |
| `sudo firewall-cmd --get-zones` | List all available zones on the system. |
| `sudo firewall-cmd --list-all` | List all settings for the default zone. |
| `sudo firewall-cmd --zone=home --list-all` | List all settings for a specific zone (e.g., `home`). |

### Interface Management
```bash
# Temporarily assign an interface to a specific zone
sudo firewall-cmd --zone=internal --change-interface=eth0

# Permanently assign an interface to a zone
sudo firewall-cmd --permanent --zone=internal --change-interface=eth0
```

## 3. Services and Ports

Instead of remembering ports, Firewalld allows you to allow/block predefined services (like HTTP, SSH, FTP).

### Managing Services
```bash
# List all predefined services firewalld knows about
sudo firewall-cmd --get-services

# Allow a service temporarily (until next reload/reboot)
sudo firewall-cmd --add-service=http

# Allow a service permanently
sudo firewall-cmd --permanent --add-service=https

# Remove a service permanently
sudo firewall-cmd --permanent --remove-service=ftp
```

### Managing Ports directly
```bash
# Open a specific port permanently (TCP or UDP)
sudo firewall-cmd --permanent --add-port=8080/tcp

# Open a range of ports
sudo firewall-cmd --permanent --add-port=5000-5050/udp

# Remove a port
sudo firewall-cmd --permanent --remove-port=8080/tcp
```

## 4. IP Addressing and Subnets (Sources)

You can trust or untrust specific IP addresses by binding them to specific zones (like `trusted` or `drop`).

```bash
# Allow all traffic from a specific IP (bind it to the 'trusted' zone)
sudo firewall-cmd --permanent --zone=trusted --add-source=192.168.1.50

# Block all traffic from an IP (bind it to the 'drop' zone)
sudo firewall-cmd --permanent --zone=drop --add-source=203.0.113.10

# Allow traffic from an entire subnet to a specific zone
sudo firewall-cmd --permanent --zone=internal --add-source=10.0.0.0/24

# Remove an IP from a zone
sudo firewall-cmd --permanent --zone=drop --remove-source=203.0.113.10
```

## 5. Rich Rules (Advanced Filtering)

Rich rules provide more granular control, allowing you to combine IPs, ports, and actions (allow, drop, reject, rate-limit).

```bash
# Block a specific IP address completely
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.1.100" drop'

# Allow a specific IP to access only a specific port (e.g., SSH)
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.1.50" port port="22" protocol="tcp" accept'

# Rate limit SSH connections (e.g., max 3 connections per minute)
sudo firewall-cmd --permanent --add-rich-rule='rule service name="ssh" limit value="3/m" accept'
```

## 6. Port Forwarding and Masquerading (NAT)

Useful if your Fedora machine is acting as a router or hosting containers/VMs.

```bash
# Enable masquerading (NAT) on a zone (required for port forwarding to work)
sudo firewall-cmd --permanent --zone=public --add-masquerade

# Forward incoming traffic on port 80 to port 8080 on the same machine
sudo firewall-cmd --permanent --zone=public --add-forward-port=port=80:proto=tcp:toport=8080

# Forward incoming traffic on port 80 to a different internal IP (192.168.1.10)
sudo firewall-cmd --permanent --zone=public --add-forward-port=port=80:proto=tcp:toport=80:toaddr=192.168.1.10
```

## 7. Panic Mode (Emergency)

If you are under attack or need to immediately sever all network communications, use Panic Mode. *Warning: This will drop SSH connections!*

| Command | Description |
| :--- | :--- |
| `sudo firewall-cmd --panic-on` | Drop all incoming and outgoing packets immediately. |
| `sudo firewall-cmd --panic-off` | Disable panic mode and restore normal routing. |
| `sudo firewall-cmd --query-panic` | Check if panic mode is currently active. |
