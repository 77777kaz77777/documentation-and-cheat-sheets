## How to configure OpenWrt router settings straight from the terminal using UCI

# OpenWrt UCI (Unified Configuration Interface) Cheat Sheet

## Core Configuration Commands

| Command | Description |
| :--- | :--- |
| `uci show` | Display the entire router configuration. |
| `uci show <config>` | Display settings for a specific subsystem (e.g., `uci show network`). |
| `uci get <config>.<section>.<option>` | Retrieve the value of a specific configuration option. |
| `uci set <config>.<section>.<option>=<value>` | Modify or create a specific configuration option. |
| `uci add_list <config>.<section>.<list>=<value>` | Add a value to a configuration list (e.g., adding a DNS server). |
| `uci del_list <config>.<section>.<list>=<value>` | Remove a value from a configuration list. |
| `uci delete <config>.<section>` | Delete an entire section or option. |

## Applying Changes

| Command | Description |
| :--- | :--- |
| `uci changes` | View uncommitted changes staged in memory. |
| `uci revert <config>` | Discard uncommitted changes for a specific configuration. |
| `uci commit` | Write all staged changes to the `/etc/config/` filesystem. |
| `/etc/init.d/<service> restart` | Restart the associated service to apply committed changes (e.g., `/etc/init.d/network restart`). |

## Common Use Case: Setting Custom DNS

```bash
uci set network.wan.peerdns='0'
uci del_list network.wan.dns='1.1.1.1'
uci add_list network.wan.dns='9.9.9.9'
uci commit network
/etc/init.d/network restart
