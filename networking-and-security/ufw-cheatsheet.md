## UFW (Uncomplicated Firewall) Command Reference for Ubuntu/Debian.
Service Control & Status
|  |  |
| :- | :- |
| **Command** | **Action** |
| sudo ufw status | View firewall status (enabled/disabled) |
| sudo ufw status verbose | View detailed status, default policies, and active rules |
| sudo ufw status numbered | Display active rules with line numbers (useful for deletion) |
| sudo ufw enable | Enable UFW (starts automatically on boot) |
| sudo ufw disable | Disable UFW |
| sudo ufw reload | Reload UFW rules without resetting connections |
| sudo ufw reset | Reset UFW to default factory state (deletes all custom rules) |

Default Policies
Set default traffic handling before adding specific rules:
# Deny all incoming traffic and allow all outgoing traffic (standard baseline)  
sudo ufw default deny incoming  
sudo ufw default allow outgoing  
Allowing Traffic
By Port or Service
# Allow SSH by service name or port number  
sudo ufw allow ssh  
sudo ufw allow 22  
  
# Allow HTTP and HTTPS  
sudo ufw allow http  
sudo ufw allow https  
sudo ufw allow 80/tcp  
sudo ufw allow 443/tcp  
By Port Range & Protocol
# Allow TCP port range 6000 to 6007  
sudo ufw allow 6000:6007/tcp  
  
# Allow UDP port range 6000 to 6007  
sudo ufw allow 6000:6007/udp  
By IP Address or Subnet
# Allow all incoming connections from a specific IP address  
sudo ufw allow from 192.168.1.50  
  
# Allow a specific IP address on a specific port (e.g., SSH)  
sudo ufw allow from 192.168.1.50 to any port 22  
  
# Allow an entire subnet (e.g., 192.168.1.0/24)  
sudo ufw allow from 192.168.1.0/24  
  
# Allow an entire subnet to access a specific port (e.g., MySQL 3306)  
sudo ufw allow from 192.168.1.0/24 to any port 3306  
Denying & Rate Limiting
# Deny incoming traffic on port 80  
sudo ufw deny 80/tcp  
  
# Deny connections from a specific IP  
sudo ufw deny from 203.0.113.100  
  
# Rate limit SSH (denies connections from IPs with 6+ attempts in 30 seconds)  
sudo ufw limit ssh  
Deleting Rules
Method 1: By Rule Line Number
# 1. List rules with numbers  
sudo ufw status numbered  
  
# 2. Delete rule by number (e.g., rule #3)  
sudo ufw delete 3  
Method 2: By Original Syntax
sudo ufw delete allow 80/tcp  
sudo ufw delete allow ssh  
Network Interface Rules
Apply rules to specific network interfaces (e.g., eth0 or wg0):
# Allow incoming traffic on port 80 on eth0 only  
sudo ufw allow in on eth0 to any port 80  
  
# Allow traffic on a specific VPN interface  
sudo ufw allow in on wg0  
Logging
# Enable logging (logs stored in /var/log/ufw.log)  
sudo ufw logging on  
  
# Set logging level (low, medium, high, full)  
sudo ufw logging medium  
  
# Disable logging  
sudo ufw logging off
