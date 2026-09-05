# nftables Cheat Sheet

## 1. General Ruleset Management
| Command | Description | Example |
| :--- | :--- | :--- |
| `nft list ruleset` | Display the entire active ruleset | `nft list ruleset` |
| `nft flush ruleset` | Delete all tables, chains, and rules completely | `nft flush ruleset` |
| `nft -f <file>` | Load and apply a ruleset from a configuration file | `nft -f /etc/nftables.conf` |
| `nft list ruleset > <file>` | Save the current active ruleset to a file | `nft list ruleset > /etc/nftables.conf` |
| `nft monitor` | Monitor netlink events (rule additions/deletions) in real-time | `nft monitor` |

## 2. Table Management
*Tables act as containers for chains, sets, and stateful objects.*

| Command | Description | Example |
| :--- | :--- | :--- |
| `nft add table <family> <table>` | Create a new table (families: `ip`, `ip6`, `inet`, `arp`, `bridge`, `netdev`) | `nft add table inet my_table` |
| `nft list table <family> <table>` | List all chains and rules within a specific table | `nft list table inet my_table` |
| `nft delete table <family> <table>` | Delete a table and all its contents | `nft delete table inet my_table` |
| `nft flush table <family> <table>` | Remove all rules from all chains within a table (keeps the table and chains) | `nft flush table inet my_table` |

## 3. Chain Management
*Chains are containers for rules and can be base (hooked into kernel) or regular.*

| Command | Description | Example |
| :--- | :--- | :--- |
| `nft add chain <family> <table> <chain>` | Create a regular (non-base) chain | `nft add chain inet my_table my_regular_chain` |
| `nft add chain <family> <table> <chain> { type <type> hook <hook> priority <prio> ; }` | Create a base chain attached to a specific networking hook | `nft add chain inet my_table my_filter { type filter hook input priority 0 ; }` |
| `nft list chain <family> <table> <chain>` | List all rules within a specific chain | `nft list chain inet my_table my_filter` |
| `nft delete chain <family> <table> <chain>` | Delete an empty chain | `nft delete chain inet my_table my_regular_chain` |
| `nft flush chain <family> <table> <chain>` | Delete all rules within a specific chain | `nft flush chain inet my_table my_filter` |

## 4. Rule Management
*Rules define the match criteria and the action to take.*

| Command | Description | Example |
| :--- | :--- | :--- |
| `nft add rule <family> <table> <chain> <matches> <statement>` | Append a rule to the end of a chain | `nft add rule inet my_table my_filter tcp dport 22 accept` |
| `nft insert rule <family> <table> <chain> <matches> <statement>` | Insert a rule at the beginning of a chain | `nft insert rule inet my_table my_filter ip saddr 192.168.1.50 drop` |
| `nft list chain -a <family> <table> <chain>` | List rules in a chain with their numerical handles | `nft list chain -a inet my_table my_filter` |
| `nft delete rule <family> <table> <chain> handle <handle>` | Delete a specific rule by its handle number | `nft delete rule inet my_table my_filter handle 5` |
| `nft replace rule <family> <table> <chain> handle <handle> <new_rule>` | Replace an existing rule in-place by its handle | `nft replace rule inet my_table my_filter handle 5 tcp dport 80 accept` |

## 5. Sets and Maps
*Sets allow matching multiple values efficiently; Maps map a matched value to a specific verdict or data.*

| Command | Description | Example |
| :--- | :--- | :--- |
| `nft add set <family> <table> <set> { type <type>; }` | Create a named set (types: `ipv4_addr`, `ipv6_addr`, `inet_service`, etc.) | `nft add set inet my_table blackhole { type ipv4_addr; }` |
| `nft list set <family> <table> <set>` | Display the contents of a set | `nft list set inet my_table blackhole` |
| `nft add element <family> <table> <set> { <elements> }` | Add elements to an existing set | `nft add element inet my_table blackhole { 10.0.0.5, 192.168.1.100 }` |
| `nft delete element <family> <table> <set> { <elements> }` | Remove specific elements from a set | `nft delete element inet my_table blackhole { 10.0.0.5 }` |
| `nft delete set <family> <table> <set>` | Delete a set entirely | `nft delete set inet my_table blackhole` |

## 6. Common Rule Examples

### Port Filtering
| Purpose | Command Example |
| :--- | :--- |
| Allow incoming SSH (port 22) | `nft add rule inet filter input tcp dport 22 accept` |
| Allow incoming HTTP & HTTPS | `nft add rule inet filter input tcp dport { 80, 443 } accept` |
| Drop incoming Telnet (port 23) | `nft add rule inet filter input tcp dport 23 drop` |

### IP/Network Filtering
| Purpose | Command Example |
| :--- | :--- |
| Drop specific source IP | `nft add rule inet filter input ip saddr 192.168.1.100 drop` |
| Accept entire subnet | `nft add rule inet filter input ip saddr 10.0.0.0/24 accept` |
| Match multiple IPs using anonymous set | `nft add rule inet filter input ip saddr { 1.2.3.4, 5.6.7.8 } drop` |

### Stateful Tracking
| Purpose | Command Example |
| :--- | :--- |
| Allow established/related traffic | `nft add rule inet filter input ct state established,related accept` |
| Drop invalid packets | `nft add rule inet filter input ct state invalid drop` |

### Network Address Translation (NAT)
| Purpose | Command Example |
| :--- | :--- |
| Setup SNAT (Masquerade for outbound) | `nft add rule ip nat postrouting oifname "eth0" masquerade` |
| Setup DNAT (Port forwarding) | `nft add rule ip nat prerouting iifname "eth0" tcp dport 80 dnat to 192.168.1.50:8080` |
