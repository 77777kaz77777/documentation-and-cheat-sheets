# Security Auditing Cheat Sheet

Quick-reference guide for auditing and monitoring a Linux server with Lynis, rkhunter, auditd, and automatic security updates.

Together these tools answer four questions: **How hardened is the system?** (Lynis), **Has anything been tampered with?** (rkhunter), **Who did what, and when?** (auditd), and **Are security fixes applied?** (dnf-automatic or unattended-upgrades).

---

## 1. Install

```bash
# RHEL / Rocky (Lynis and rkhunter come from EPEL)
sudo dnf install epel-release
sudo dnf install lynis rkhunter audit dnf-automatic

# Fedora
sudo dnf install lynis rkhunter audit dnf-automatic

# Debian / Ubuntu
sudo apt install lynis rkhunter auditd unattended-upgrades
```

---

## 2. Lynis — Hardening Audit

Lynis checks hundreds of settings (SSH, kernel, file permissions, services, logging, and more) and prints warnings, suggestions, and a **hardening index** from 0 to 100.

```bash
# Full system audit
sudo lynis audit system

# Run without pausing between sections
sudo lynis audit system --quick

# Show details for one finding
sudo lynis show details SSH-7408

# Lynis version and whether it's current
lynis show version
sudo lynis update info
```

### Read the Results

```bash
# Warnings and suggestions from the last run
sudo grep -E "^warning|^suggestion" /var/log/lynis-report.dat

# Hardening index
sudo grep hardening_index /var/log/lynis-report.dat
```

Full output is in `/var/log/lynis.log`; machine-readable results are in `/var/log/lynis-report.dat`.

### Skip Tests That Don't Apply

`/etc/lynis/custom.prf`:

```text
# Example: no separate /tmp partition on purpose
skip-test=FILE-6310
```

Track the hardening index over time rather than aiming for 100; some suggestions don't suit every server.

### Weekly Lynis with a systemd Timer

`/etc/systemd/system/lynis-audit.service`:

```ini
[Unit]
Description=Lynis security audit

[Service]
Type=oneshot
ExecStart=/usr/bin/lynis audit system --cronjob
```

`/etc/systemd/system/lynis-audit.timer`:

```ini
[Unit]
Description=Weekly Lynis audit

[Timer]
OnCalendar=Sun 04:00
Persistent=true

[Install]
WantedBy=timers.target
```

```bash
sudo systemctl daemon-reload && sudo systemctl enable --now lynis-audit.timer
```

`--cronjob` runs without colours or pauses, for unattended use.

---

## 3. rkhunter — Rootkit & Tamper Checks

rkhunter compares system binaries against a stored baseline and looks for known rootkits, suspicious files, and risky settings.

```bash
# Update the rootkit signatures
sudo rkhunter --update

# Record the current state as the trusted baseline (run on a known-clean system)
sudo rkhunter --propupd

# Run a check, showing only warnings
sudo rkhunter --check --sk --rwo

# Full output
sudo less /var/log/rkhunter/rkhunter.log
```

`--sk` skips the "press Enter" pauses; `--rwo` reports warnings only.

> **After every system update, run `sudo rkhunter --propupd`.** Updated packages change binaries, and rkhunter will otherwise warn about every one of them.

### Reduce False Positives

`/etc/rkhunter.conf.local` (overrides the main file):

```text
# Use the package manager to verify file changes
PKGMGR=RPM

# Known-good items that trigger warnings
ALLOWHIDDENDIR=/etc/.java
SCRIPTWHITELIST=/usr/bin/egrep
SCRIPTWHITELIST=/usr/bin/fgrep
ALLOW_SSH_ROOT_USER=no
```

Use `PKGMGR=DPKG` on Debian and Ubuntu. Check the config after editing:

```bash
sudo rkhunter -C
```

Fedora and RHEL packages include a daily cron job; on other systems, schedule `rkhunter --cronjob --report-warnings-only` with a timer.

---

## 4. auditd — Record Security Events

`auditd` writes kernel audit events (logins, `sudo`, file access, system calls, SELinux denials) to `/var/log/audit/audit.log`.

```bash
sudo systemctl enable --now auditd
sudo auditctl -s      # status
sudo auditctl -l      # loaded rules
```

### Add Rules

Rules go in `/etc/audit/rules.d/*.rules`. `/etc/audit/rules.d/50-homelab.rules`:

```text
# Watch for changes to accounts and sudo rules (w = write, a = attribute change)
-w /etc/passwd -p wa -k identity
-w /etc/shadow -p wa -k identity
-w /etc/group -p wa -k identity
-w /etc/sudoers -p wa -k sudoers
-w /etc/sudoers.d/ -p wa -k sudoers

# Watch SSH server config
-w /etc/ssh/sshd_config -p wa -k sshd
-w /etc/ssh/sshd_config.d/ -p wa -k sshd

# Watch container Quadlet definitions
-w /etc/containers/systemd/ -p wa -k quadlets

# Log every command run as root by a logged-in user
-a always,exit -F arch=b64 -S execve -F euid=0 -F auid>=1000 -F auid!=unset -k root-cmd
```

```bash
# Load rules from rules.d
sudo augenrules --load
sudo auditctl -l
```

`-k` sets a **key** so you can search for the events later. The `execve` rule is noisy; add it only if you want a full command history.

### Search Events

```bash
# Events for one key, human-readable
sudo ausearch -k identity -i

# Today's events for a key
sudo ausearch -k sshd --start today -i

# Failed logins
sudo ausearch -m USER_LOGIN --success no -i

# SELinux denials (AVC) from the last 10 minutes
sudo ausearch -m AVC -ts recent

# Events by one user
sudo ausearch -ua 1000 -i
```

### Summary Reports

```bash
sudo aureport --summary
sudo aureport --login --failed
sudo aureport --auth
sudo aureport -k
```

`auditd` keeps rotating logs itself; tune size and count in `/etc/audit/auditd.conf` (`max_log_file`, `num_logs`). Restart it with `sudo service auditd restart`, not `systemctl`.

---

## 5. Automatic Security Updates

### RHEL / Fedora / Rocky — dnf-automatic

`/etc/dnf/automatic.conf`:

```ini
[commands]
upgrade_type = security
apply_updates = yes
reboot = never

[emitters]
emit_via = stdio
```

```bash
sudo systemctl enable --now dnf-automatic.timer
systemctl list-timers dnf-automatic.timer
journalctl -u dnf-automatic.service -n 50
```

On Fedora 41 and later (DNF5), the timer is `dnf5-automatic.timer` (`dnf-automatic.timer` is an alias) and its log is under `journalctl -u dnf5-automatic.service`. It still reads `/etc/dnf/automatic.conf`, on top of defaults in `/usr/share/dnf5/dnf5-plugins/automatic.conf`.

`upgrade_type = security` only applies packages with security advisories. Fedora marks fewer updates this way than RHEL, so on Fedora `default` is often the better choice.

### Debian / Ubuntu — unattended-upgrades

```bash
sudo dpkg-reconfigure -plow unattended-upgrades
sudo unattended-upgrade --dry-run -d
```

### Know When a Reboot Is Needed

```bash
# RHEL / Fedora / Rocky
sudo dnf needs-restarting -r

# Debian / Ubuntu
[ -f /var/run/reboot-required ] && cat /var/run/reboot-required.pkgs
```

---

## 6. Suggested Schedule

| Task | How often |
| --- | --- |
| Security updates | Daily (timer) |
| `rkhunter --check` | Daily (cron job or timer) |
| `rkhunter --propupd` | After each update |
| `lynis audit system` | Weekly |
| Review `aureport --summary` and failed logins | Weekly |
| Review Lynis suggestions and hardening index | Monthly |

Send failures and new warnings to your phone with an `OnFailure=` ntfy alert on each timer's service.

---

## 7. Quick Reference

```bash
sudo lynis audit system                        # hardening audit
sudo grep hardening_index /var/log/lynis-report.dat
sudo rkhunter --update && sudo rkhunter --check --sk --rwo
sudo rkhunter --propupd                        # refresh baseline after updates
sudo augenrules --load && sudo auditctl -l     # load audit rules
sudo ausearch -k identity -i                   # search audit events
sudo aureport --login --failed                 # failed logins
sudo systemctl enable --now dnf-automatic.timer
sudo dnf needs-restarting -r                   # reboot needed?
```

---

## Sources & Verification

- **Lynis:** [CISOfy Lynis documentation](https://cisofy.com/documentation/lynis/)
- **auditd rules and searches:** [auditctl(8)](https://man7.org/linux/man-pages/man8/auditctl.8.html) and [ausearch(8)](https://man7.org/linux/man-pages/man8/ausearch.8.html)

## Related guides

- [SSH and sshd Hardening Cheat Sheet](ssh-hardening-cheat-sheet.md)
- [Fedora SELinux Management Cheat Sheet](fedora-selinux-management-cheat-sheet.md)
- [Firewalld Cheat Sheet](fedora-firewall-cheat-sheet.md)
- [ntfy Notifications Cheat Sheet](../../linux-general/system-administration/ntfy-notifications-cheat-sheet.md)
