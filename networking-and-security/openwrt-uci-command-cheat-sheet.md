## How to configure OpenWrt router settings straight from the terminal using UCI

# OpenWrt UCI (Unified Configuration Interface) Cheat Sheet

## Core Configuration Commands

**Display the entire router configuration:**
```bash
uci show
```

**Display settings for a specific subsystem (e.g., `uci show network`):**
```bash
uci show <config>
```

**Retrieve the value of a specific configuration option:**
```bash
uci get <config>.<section>.<option>
```

**Modify or create a specific configuration option:**
```bash
uci set <config>.<section>.<option>=<value>
```

**Add a value to a configuration list (e.g., adding a DNS server):**
```bash
uci add_list <config>.<section>.<list>=<value>
```

**Remove a value from a configuration list:**
```bash
uci del_list <config>.<section>.<list>=<value>
```

**Delete an entire section or option:**
```bash
uci delete <config>.<section>
```

## Applying Changes

**View uncommitted changes staged in memory:**
```bash
uci changes
```

**Discard uncommitted changes for a specific configuration:**
```bash
uci revert <config>
```

**Write all staged changes to the `/etc/config/` filesystem:**
```bash
uci commit
```

**Restart the associated service to apply committed changes (e.g., `/etc/init.d/network restart`):**
```bash
/etc/init.d/<service> restart
```

## Common Use Case: Setting Custom DNS

```bash
uci set network.wan.peerdns='0'
uci del_list network.wan.dns='1.1.1.1'
uci add_list network.wan.dns='9.9.9.9'
uci commit network
/etc/init.d/network restart
```
