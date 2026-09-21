# Everyday commands for handling services and logs with Systemd and journalctl

Systemd is the system and service manager responsible for controlling system units, background services, boots, and logs.

---

## 1. Service Management (`systemctl`)

| Action | Command |
| :--- | :--- |
| **Check Service Status** | `systemctl status <unit>` |
| **Start Service** | `sudo systemctl start <unit>` |
| **Stop Service** | `sudo systemctl stop <unit>` |
| **Restart Service** | `sudo systemctl restart <unit>` |
| **Reload Config without Restart** | `sudo systemctl reload <unit>` |
| **Reload or Restart (Fallback)** | `sudo systemctl reload-or-restart <unit>` |
| **Enable on Boot & Start Immediately** | `sudo systemctl enable --now <unit>` |
| **Disable on Boot & Stop Immediately** | `sudo systemctl disable --now <unit>` |
| **Mask Unit (Prevent manual/auto start)** | `sudo systemctl mask <unit>` |
| **Unmask Unit** | `sudo systemctl unmask <unit>` |

---

## 2. State & Unit Inspection

| Action | Command |
| :--- | :--- |
| **Check if Active** | `systemctl is-active <unit>` |
| **Check if Enabled on Boot** | `systemctl is-enabled <unit>` |
| **Check if Unit Failed** | `systemctl is-failed <unit>` |
| **List All Active Services** | `systemctl list-units --type=service --state=running` |
| **List All Installed Unit Files** | `systemctl list-unit-files --type=service` |
| **List All Failed Units** | `systemctl --failed` |
| **View Unit File Contents** | `systemctl cat <unit>` |
| **Show Low-Level Unit Properties** | `systemctl show <unit>` |

---

## 3. Unit File Editing & Lifecycle

| Action | Command |
| :--- | :--- |
| **Reload Manager (After file changes)** | `sudo systemctl daemon-reload` |
| **Create Override/Drop-in Config** | `sudo systemctl edit <unit>` |
| **Edit Complete Unit File Copy** | `sudo systemctl edit --full <unit>` |
| **Remove Override/Drop-in Config** | `sudo systemctl revert <unit>` |

---

## 4. Log Filtering & Diagnostics (`journalctl`)

### Basic & Real-Time Logs

| Action | Command |
| :--- | :--- |
| **Follow Unit Logs Real-Time** | `sudo journalctl -u <unit> -f` |
| **View Last N Lines for Unit** | `sudo journalctl -u <unit> -n 100` |
| **View Current Boot Logs** | `sudo journalctl -b` |
| **View Previous Boot Logs** | `sudo journalctl -b -1` |
| **List All Available Boots** | `sudo journalctl --list-boots` |
| **View Kernel Logs (`dmesg` equivalent)** | `sudo journalctl -k` |

### Time & Priority Filtering

| Action | Command |
| :--- | :--- |
| **Filter by Relative Time** | `sudo journalctl --since "1 hour ago"` |
| **Filter by Absolute Time Range** | `sudo journalctl --since "2026-09-20 00:00:00" --until "2026-09-20 12:00:00"` |
| **Filter by Priority Level** | `sudo journalctl -p err..emerg` |
| **Filter by Process ID** | `sudo journalctl _PID=<pid>` |
| **Filter by Executable Path** | `sudo journalctl /usr/bin/<binary>` |

### Formatting & Disk Space Maintenance

| Action | Command |
| :--- | :--- |
| **Raw Message Output (No metadata)** | `sudo journalctl -u <unit> -o cat` |
| **Pretty JSON Output** | `sudo journalctl -u <unit> -o json-pretty` |
| **Check Total Journal Disk Usage** | `sudo journalctl --disk-usage` |
| **Trim Storage by Size Limit** | `sudo journalctl --vacuum-size=500M` |
| **Trim Storage by Retention Period** | `sudo journalctl --vacuum-time=2weeks` |

---

## 5. Boot Analysis & Performance (`systemd-analyze`)

| Action | Command |
| :--- | :--- |
| **Check Startup Duration Breakdown** | `systemd-analyze` |
| **List Slowest Initializing Services** | `systemd-analyze blame` |
| **Print Boot Time Dependency Tree** | `systemd-analyze critical-chain` |
| **Analyze Unit Security Hardening** | `systemd-analyze security <unit>` |

---

## 6. User-Level Services (`--user`)

User services operate without `sudo` under `~/.config/systemd/user/`.

| Action | Command |
| :--- | :--- |
| **Check User Service Status** | `systemctl --user status <unit>` |
| **Start User Service** | `systemctl --user start <unit>` |
| **Enable User Service** | `systemctl --user enable --now <unit>` |
| **View User Service Logs** | `journalctl --user -u <unit> -f` |
| **Persist User Services After Logout** | `loginctl enable-linger $USER` |

---

## 7. System State & Targets

| Action | Command |
| :--- | :--- |
| **View Current Default Target** | `systemctl get-default` |
| **Set Default to Multi-User (CLI)** | `sudo systemctl set-default multi-user.target` |
| **Set Default to Graphical (GUI)** | `sudo systemctl set-default graphical.target` |
| **Switch Target without Rebooting** | `sudo systemctl isolate multi-user.target` |
| **Reboot System** | `systemctl reboot` |
| **Power Off System** | `systemctl poweroff` |

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
