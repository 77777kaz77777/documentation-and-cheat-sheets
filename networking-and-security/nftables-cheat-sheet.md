## How to properly configure network filtering, manage firewall rulesets, and set up NAT using the nftables command-line utility

## 1. General Ruleset Management

**`nft list ruleset` — Display the entire active ruleset:**
```bash
nft list ruleset
```

**`nft flush ruleset` — Delete all tables, chains, and rules completely:**
```bash
nft flush ruleset
```

**`nft -f <file>` — Load and apply a ruleset from a configuration file:**
```bash
nft -f /etc/nftables.conf
```

**`nft list ruleset > <file>` — Save the current active ruleset to a file:**
```bash
nft list ruleset > /etc/nftables.conf
```

**`nft monitor` — Monitor netlink events (rule additions/deletions) in real-time:**
```bash
nft monitor
```

## 2. Table Management

_Tables act as containers for chains, sets, and stateful objects._

**`nft add table <family> <table>` — Create a new table (families: `ip`, `ip6`, `inet`, `arp`, `bridge`, `netdev`):**
```bash
nft add table inet my_table
```

**`nft list table <family> <table>` — List all chains and rules within a specific table:**
```bash
nft list table inet my_table
```

**`nft delete table <family> <table>` — Delete a table and all its contents:**
```bash
nft delete table inet my_table
```

**`nft flush table <family> <table>` — Remove all rules from all chains within a table (keeps the table and chains):**
```bash
nft flush table inet my_table
```

## 3. Chain Management

_Chains are containers for rules and can be base (hooked into kernel) or regular._

**`nft add chain <family> <table> <chain>` — Create a regular (non-base) chain:**
```bash
nft add chain inet my_table my_regular_chain
```

**`nft add chain <family> <table> <chain> { type <type> hook <hook> priority <prio> ; }` — Create a base chain attached to a specific networking hook:**
```bash
nft add chain inet my_table my_filter { type filter hook input priority 0 ; }
```

**`nft list chain <family> <table> <chain>` — List all rules within a specific chain:**
```bash
nft list chain inet my_table my_filter
```

**`nft delete chain <family> <table> <chain>` — Delete an empty chain:**
```bash
nft delete chain inet my_table my_regular_chain
```

**`nft flush chain <family> <table> <chain>` — Delete all rules within a specific chain:**
```bash
nft flush chain inet my_table my_filter
```

## 4. Rule Management

_Rules define the match criteria and the action to take._

**`nft add rule <family> <table> <chain> <matches> <statement>` — Append a rule to the end of a chain:**
```bash
nft add rule inet my_table my_filter tcp dport 22 accept
```

**`nft insert rule <family> <table> <chain> <matches> <statement>` — Insert a rule at the beginning of a chain:**
```bash
nft insert rule inet my_table my_filter ip saddr 192.168.1.50 drop
```

**`nft list chain -a <family> <table> <chain>` — List rules in a chain with their numerical handles:**
```bash
nft list chain -a inet my_table my_filter
```

**`nft delete rule <family> <table> <chain> handle <handle>` — Delete a specific rule by its handle number:**
```bash
nft delete rule inet my_table my_filter handle 5
```

**`nft replace rule <family> <table> <chain> handle <handle> <new_rule>` — Replace an existing rule in-place by its handle:**
```bash
nft replace rule inet my_table my_filter handle 5 tcp dport 80 accept
```

## 5. Sets and Maps

_Sets allow matching multiple values efficiently; Maps map a matched value to a specific verdict or data._

**`nft add set <family> <table> <set> { type <type>; }` — Create a named set (types: `ipv4_addr`, `ipv6_addr`, `inet_service`, etc.):**
```bash
nft add set inet my_table blackhole { type ipv4_addr; }
```

**`nft list set <family> <table> <set>` — Display the contents of a set:**
```bash
nft list set inet my_table blackhole
```

**`nft add element <family> <table> <set> { <elements> }` — Add elements to an existing set:**
```bash
nft add element inet my_table blackhole { 10.0.0.5, 192.168.1.100 }
```

**`nft delete element <family> <table> <set> { <elements> }` — Remove specific elements from a set:**
```bash
nft delete element inet my_table blackhole { 10.0.0.5 }
```

**`nft delete set <family> <table> <set>` — Delete a set entirely:**
```bash
nft delete set inet my_table blackhole
```

## 6. Common Rule Examples

### Port Filtering

**Allow incoming SSH (port 22):**
```bash
nft add rule inet filter input tcp dport 22 accept
```

**Allow incoming HTTP & HTTPS:**
```bash
nft add rule inet filter input tcp dport { 80, 443 } accept
```

**Drop incoming Telnet (port 23):**
```bash
nft add rule inet filter input tcp dport 23 drop
```

### IP/Network Filtering

**Drop specific source IP:**
```bash
nft add rule inet filter input ip saddr 192.168.1.100 drop
```

**Accept entire subnet:**
```bash
nft add rule inet filter input ip saddr 10.0.0.0/24 accept
```

**Match multiple IPs using anonymous set:**
```bash
nft add rule inet filter input ip saddr { 1.2.3.4, 5.6.7.8 } drop
```

### Stateful Tracking

**Allow established/related traffic:**
```bash
nft add rule inet filter input ct state established,related accept
```

**Drop invalid packets:**
```bash
nft add rule inet filter input ct state invalid drop
```

### Network Address Translation (NAT)

**Setup SNAT (Masquerade for outbound):**
```bash
nft add rule ip nat postrouting oifname "eth0" masquerade
```

**Setup DNAT (Port forwarding):**
```bash
nft add rule ip nat prerouting iifname "eth0" tcp dport 80 dnat to 192.168.1.50:8080
```
