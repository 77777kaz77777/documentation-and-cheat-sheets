## Commands and config paths for managing AdGuard Home DNS rules and filters

# AdGuard Home Management & DNS Filtering Cheat Sheet

## Service Management (Linux / OpenWrt)

| Command | Description |
| :--- | :--- |
| `sudo systemctl restart AdGuardHome` | Restart the AdGuard Home service (Standard Linux). |
| `/etc/init.d/AdGuardHome restart` | Restart the AdGuard Home service (OpenWrt). |
| `sudo systemctl status AdGuardHome` | Verify the service status and uptime. |
| `sudo AdGuardHome -s stop` | Stop the service using the built-in binary flag. |

## DNS Testing & Verification

| Command | Description |
| :--- | :--- |
| `dig @127.0.0.1 <domain>` | Test DNS resolution locally against the AdGuard Home instance. |
| `dig @<router_ip> doubleclick.net` | Verify that a known ad domain is returning `0.0.0.0` (blocked). |
| `nslookup <domain> <router_ip>` | Alternative DNS lookup to test custom filtering rules. |

## Configuration & Logs

| Command | Description |
| :--- | :--- |
| `nano /opt/AdGuardHome/AdGuardHome.yaml` | Edit the main configuration file (path varies by installation). |
| `tail -f /opt/AdGuardHome/data/querylog.json` | Follow the live DNS query log in JSON format. |
| `sudo AdGuardHome --check-config` | Validate the syntax of `AdGuardHome.yaml` before restarting. |
