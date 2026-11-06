# reference sheet for managing systemd services and inspecting system logs with journalctl

Systemd is the system and service manager responsible for controlling system units, background services, boots, and logs.

---

## 1. Service Management (`systemctl`)

**Check Service Status:**

```bash
systemctl status <unit>
```

**Start Service:**

```bash
sudo systemctl start <unit>
```

**Stop Service:**

```bash
sudo systemctl stop <unit>
```

**Restart Service:**

```bash
sudo systemctl restart <unit>
```

**Reload Config without Restart:**

```bash
sudo systemctl reload <unit>
```

**Reload or Restart (Fallback):**

```bash
sudo systemctl reload-or-restart <unit>
```

**Enable on Boot & Start Immediately:**

```bash
sudo systemctl enable --now <unit>
```

**Disable on Boot & Stop Immediately:**

```bash
sudo systemctl disable --now <unit>
```

**Mask Unit (Prevent manual/auto start):**

```bash
sudo systemctl mask <unit>
```

**Unmask Unit:**

```bash
sudo systemctl unmask <unit>
```

---

## 2. State & Unit Inspection

**Check if Active:**

```bash
systemctl is-active <unit>
```

**Check if Enabled on Boot:**

```bash
systemctl is-enabled <unit>
```

**Check if Unit Failed:**

```bash
systemctl is-failed <unit>
```

**List All Active Services:**

```bash
systemctl list-units --type=service --state=running
```

**List All Installed Unit Files:**

```bash
systemctl list-unit-files --type=service
```

**List All Failed Units:**

```bash
systemctl --failed
```

**View Unit File Contents:**

```bash
systemctl cat <unit>
```

**Show Low-Level Unit Properties:**

```bash
systemctl show <unit>
```

---

## 3. Unit File Editing & Lifecycle

**Reload Manager (After file changes):**

```bash
sudo systemctl daemon-reload
```

**Create Override/Drop-in Config:**

```bash
sudo systemctl edit <unit>
```

**Edit Complete Unit File Copy:**

```bash
sudo systemctl edit --full <unit>
```

**Remove Override/Drop-in Config:**

```bash
sudo systemctl revert <unit>
```

---

## 4. Log Filtering & Diagnostics (`journalctl`)

### Basic & Real-Time Logs

**Follow Unit Logs Real-Time:**

```bash
sudo journalctl -u <unit> -f
```

**View Last N Lines for Unit:**

```bash
sudo journalctl -u <unit> -n 100
```

**View Current Boot Logs:**

```bash
sudo journalctl -b
```

**View Previous Boot Logs:**

```bash
sudo journalctl -b -1
```

**List All Available Boots:**

```bash
sudo journalctl --list-boots
```

**View Kernel Logs (`dmesg` equivalent):**

```bash
sudo journalctl -k
```

### Time & Priority Filtering

**Filter by Relative Time:**

```bash
sudo journalctl --since "1 hour ago"
```

**Filter by Absolute Time Range:**

```bash
sudo journalctl --since "2026-09-20 00:00:00" --until "2026-09-20 12:00:00"
```

**Filter by Priority Level:**

```bash
sudo journalctl -p err..emerg
```

**Filter by Process ID:**

```bash
sudo journalctl _PID=<pid>
```

**Filter by Executable Path:**

```bash
sudo journalctl /usr/bin/<binary>
```

### Formatting & Disk Space Maintenance

**Raw Message Output (No metadata):**

```bash
sudo journalctl -u <unit> -o cat
```

**Pretty JSON Output:**

```bash
sudo journalctl -u <unit> -o json-pretty
```

**Check Total Journal Disk Usage:**

```bash
sudo journalctl --disk-usage
```

**Trim Storage by Size Limit:**

```bash
sudo journalctl --vacuum-size=500M
```

**Trim Storage by Retention Period:**

```bash
sudo journalctl --vacuum-time=2weeks
```

---

## 5. Boot Analysis & Performance (`systemd-analyze`)

**Check Startup Duration Breakdown:**

```bash
systemd-analyze
```

**List Slowest Initializing Services:**

```bash
systemd-analyze blame
```

**Print Boot Time Dependency Tree:**

```bash
systemd-analyze critical-chain
```

**Analyze Unit Security Hardening:**

```bash
systemd-analyze security <unit>
```

---

## 6. User-Level Services (`--user`)

User services operate without `sudo` under `~/.config/systemd/user/`.

**Check User Service Status:**

```bash
systemctl --user status <unit>
```

**Start User Service:**

```bash
systemctl --user start <unit>
```

**Enable User Service:**

```bash
systemctl --user enable --now <unit>
```

**View User Service Logs:**

```bash
journalctl --user -u <unit> -f
```

**Persist User Services After Logout:**

```bash
loginctl enable-linger $USER
```

---

## 7. System State & Targets

**View Current Default Target:**

```bash
systemctl get-default
```

**Set Default to Multi-User (CLI):**

```bash
sudo systemctl set-default multi-user.target
```

**Set Default to Graphical (GUI):**

```bash
sudo systemctl set-default graphical.target
```

**Switch Target without Rebooting:**

```bash
sudo systemctl isolate multi-user.target
```

**Reboot System:**

```bash
systemctl reboot
```

**Power Off System:**

```bash
systemctl poweroff
```

---

## 8. Reference Unit File Template

```ini
# /etc/systemd/system/example.service

[Unit]
Description=Example Custom Background Service
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=nobody
Group=nobody
ExecStart=/usr/local/bin/example-daemon --config /etc/example.conf
Restart=on-failure
RestartSec=5s

# Basic Security Sandboxing
ProtectSystem=full
ProtectHome=true
NoNewPrivileges=true

[Install]
WantedBy=multi-user.target
```
