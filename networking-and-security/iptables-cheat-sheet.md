# How to properly configure network filtering, manage firewall rulesets, and set up NAT using the iptables command-line utility

`iptables` is a command-line firewall utility for Linux systems. It uses policy chains to allow or block traffic.

## Core Concepts

- **Tables:** `filter` (default), `nat`, `mangle`, `raw`, `security`.
- **Chains:** `INPUT` (incoming), `FORWARD` (routing through), `OUTPUT` (outgoing).
- **Targets:** `ACCEPT` (allow), `DROP` (silently block), `REJECT` (block and send error).

---

## 1. Basic Commands

These commands are used to view, manage, and delete your current firewall rules.

| Action                     | Explanation                                                                                                                | Command Syntax                                | Example                           |
| :------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------- | :-------------------------------- |
| **List rules**             | Shows active rules. `-v` adds verbosity (packet counts), `-n` shows numerical IP addresses instead of resolving hostnames. | `sudo iptables -L [options]`                  | `sudo iptables -L -v -n`          |
| **List specific table**    | Views rules applied to a specific table (like `nat` or `mangle`) instead of the default `filter` table.                    | `sudo iptables -t [table_name] -L`            | `sudo iptables -t nat -L -v -n`   |
| **List with line numbers** | Displays a number next to each rule, which is essential for deleting or inserting rules at specific positions.             | `sudo iptables -L --line-numbers`             | `sudo iptables -L --line-numbers` |
| **Flush all rules**        | Deletes ALL rules in the selected table (or the default filter table if none is specified). **Use with caution.**          | `sudo iptables -F`                            | `sudo iptables -F`                |
| **Flush specific chain**   | Deletes all rules only within a specific chain (like INPUT, OUTPUT, or FORWARD).                                           | `sudo iptables -F [chain_name]`               | `sudo iptables -F INPUT`          |
| **Delete rule by number**  | Removes a specific rule based on its line number in a given chain.                                                         | `sudo iptables -D [chain_name] [line_number]` | `sudo iptables -D INPUT 1`        |

---

## 2. Default Policies

Setting default policies is crucial for a baseline security posture. A common secure setup drops all incoming traffic and allows all outgoing.

| Action                 | Explanation                                                                                            | Command Syntax                      | Example                          |
| :--------------------- | :----------------------------------------------------------------------------------------------------- | :---------------------------------- | :------------------------------- |
| **Drop all incoming**  | Sets the default behavior for inbound traffic to be blocked unless explicitly allowed by another rule. | `sudo iptables -P INPUT [TARGET]`   | `sudo iptables -P INPUT DROP`    |
| **Drop all forwarded** | Blocks traffic attempting to route through your machine to another destination.                        | `sudo iptables -P FORWARD [TARGET]` | `sudo iptables -P FORWARD DROP`  |
| **Allow all outgoing** | Permits your machine to send outbound traffic anywhere.                                                | `sudo iptables -P OUTPUT [TARGET]`  | `sudo iptables -P OUTPUT ACCEPT` |

---

## 3. Managing Connections (Stateful Rules)

Modern firewalls track the state of connections. You need these rules to ensure that if you request data (like loading a webpage), the response isn't blocked.

| Action                        | Explanation                                                                                                   | Command Syntax                                                     | Example                                                                       |
| :---------------------------- | :------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| **Allow established/related** | Permits incoming return traffic for connections your machine initiated. Essential if default INPUT is DROP.   | `sudo iptables -A INPUT -m conntrack --ctstate [states] -j ACCEPT` | `sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT` |
| **Allow loopback**            | Allows the system's internal services to communicate with each other securely over `localhost` (`127.0.0.1`). | `sudo iptables -A INPUT -i [interface] -j ACCEPT`                  | `sudo iptables -A INPUT -i lo -j ACCEPT`                                      |

---

## 4. Allowing and Blocking Ports

Use these rules to open or close specific services like web servers or SSH.

| Action                      | Explanation                                                                                               | Command Syntax                                                                       | Example                                                                     |
| :-------------------------- | :-------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------- | :-------------------------------------------------------------------------- |
| **Allow single port (SSH)** | Opens a specific TCP/UDP port for incoming traffic. `-p` defines protocol, `--dport` is destination port. | `sudo iptables -A INPUT -p [protocol] --dport [port] -j ACCEPT`                      | `sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT`                        |
| **Allow multiple ports**    | Uses the `multiport` module to open several ports in a single command, saving space.                      | `sudo iptables -A INPUT -p [protocol] -m multiport --dports [port1,port2] -j ACCEPT` | `sudo iptables -A INPUT -p tcp -m multiport --dports 80,443,8080 -j ACCEPT` |
| **Block specific port**     | Explicitly denies incoming traffic to a specific port.                                                    | `sudo iptables -A INPUT -p [protocol] --dport [port] -j DROP`                        | `sudo iptables -A INPUT -p tcp --dport 23 -j DROP`                          |

---

## 5. Allowing and Blocking IP Addresses

Control access based on the source IP or subnet of the incoming traffic.

| Action                        | Explanation                                                                                | Command Syntax                                                                  | Example                                                              |
| :---------------------------- | :----------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------ | :------------------------------------------------------------------- |
| **Allow specific IP**         | Grants full access to all ports from a trusted single IP address using `-s` (source).      | `sudo iptables -A INPUT -s [ip_address] -j ACCEPT`                              | `sudo iptables -A INPUT -s 192.168.1.100 -j ACCEPT`                  |
| **Block specific IP**         | Silently drops all packets coming from a specific IP address.                              | `sudo iptables -A INPUT -s [ip_address] -j DROP`                                | `sudo iptables -A INPUT -s 203.0.113.50 -j DROP`                     |
| **Reject specific IP**        | Blocks traffic from an IP but sends an ICMP "connection refused" error back to the sender. | `sudo iptables -A INPUT -s [ip_address] -j REJECT`                              | `sudo iptables -A INPUT -s 203.0.113.50 -j REJECT`                   |
| **Allow subnet**              | Permits traffic from an entire range of IPs using CIDR notation.                           | `sudo iptables -A INPUT -s [subnet/CIDR] -j ACCEPT`                             | `sudo iptables -A INPUT -s 192.168.1.0/24 -j ACCEPT`                 |
| **Allow IP to specific port** | Combines source IP and destination port flags to create a highly specific access rule.     | `sudo iptables -A INPUT -p [protocol] -s [ip_address] --dport [port] -j ACCEPT` | `sudo iptables -A INPUT -p tcp -s 192.168.1.50 --dport 22 -j ACCEPT` |

---

## 6. NAT and Port Forwarding (Requires `-t nat`)

_Note: You must enable IP forwarding on your system first (`sysctl net.ipv4.ip_forward=1`)._

| Action                          | Explanation                                                                                                          | Command Syntax                                                                                         | Example                                                                                          |
| :------------------------------ | :------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| **Local Port Forwarding**       | Redirects traffic arriving on one port to a different port on the _same_ machine using `REDIRECT`.                   | `sudo iptables -t nat -A PREROUTING -p tcp --dport [original_port] -j REDIRECT --to-port [new_port]`   | `sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080`                |
| **Forward port to internal IP** | Acts as a router, sending traffic on a specific port to a completely different machine on your local network (DNAT). | `sudo iptables -t nat -A PREROUTING -p tcp --dport [port] -j DNAT --to-destination [internal_ip:port]` | `sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 192.168.1.100:80` |
| **Masquerade (Outbound NAT)**   | Allows internal network devices to share the host's public IP address for outbound internet access.                  | `sudo iptables -t nat -A POSTROUTING -o [outbound_interface] -j MASQUERADE`                            | `sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE`                                      |

---

## 7. Saving and Restoring Rules

By default, `iptables` rules are wiped out when the server reboots. You must save them using OS-specific tools.

| OS / Action       | Explanation                                                                             | Command                                        | Example                                           |
| :---------------- | :-------------------------------------------------------------------------------------- | :--------------------------------------------- | :------------------------------------------------ |
| **Debian/Ubuntu** | Uses the `iptables-persistent` package to automatically save and load rules on boot.    | `sudo netfilter-persistent save`               | `sudo netfilter-persistent save`                  |
| **RHEL/CentOS**   | Saves the current rules directly into the system's default iptables configuration file. | `sudo iptables-save > /etc/sysconfig/iptables` | `sudo iptables-save > /etc/sysconfig/iptables`    |
| **Manual Export** | Dumps the current active ruleset into a custom text file for backups or migrations.     | `sudo iptables-save > [file_path]`             | `sudo iptables-save > ~/iptables_backup.rules`    |
| **Manual Import** | Restores rules from a previously saved text file into the active firewall.              | `sudo iptables-restore < [file_path]`          | `sudo iptables-restore < ~/iptables_backup.rules` |
