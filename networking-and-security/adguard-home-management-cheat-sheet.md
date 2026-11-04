## Commands and config paths for managing AdGuard Home DNS rules and filters

# AdGuard Home Management & DNS Filtering Cheat Sheet

## Service Management (Linux / OpenWrt)

**Restart the AdGuard Home service (Standard Linux):**
```bash
sudo systemctl restart AdGuardHome
```

**Restart the AdGuard Home service (OpenWrt):**
```bash
/etc/init.d/AdGuardHome restart
```

**Verify the service status and uptime:**
```bash
sudo systemctl status AdGuardHome
```

**Stop the service using the built-in binary flag:**
```bash
sudo AdGuardHome -s stop
```

## DNS Testing & Verification

**Test DNS resolution locally against the AdGuard Home instance:**
```bash
dig @127.0.0.1 <domain>
```

**Verify that a known ad domain is returning `0.0.0.0` (blocked):**
```bash
dig @<router_ip> doubleclick.net
```

**Alternative DNS lookup to test custom filtering rules:**
```bash
nslookup <domain> <router_ip>
```

## Configuration & Logs

**Edit the main configuration file (path varies by installation):**
```bash
nano /opt/AdGuardHome/AdGuardHome.yaml
```

**Follow the live DNS query log in JSON format:**
```bash
tail -f /opt/AdGuardHome/data/querylog.json
```

**Validate the syntax of `AdGuardHome.yaml` before restarting:**
```bash
sudo AdGuardHome --check-config
```
