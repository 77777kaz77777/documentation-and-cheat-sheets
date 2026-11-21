# systemd Timers Cheat Sheet

Quick-reference guide for scheduling jobs with systemd timers instead of cron.

A **timer** (`name.timer`) starts a matching **service** (`name.service`) on a schedule. Compared with cron you get logging in the journal, catch-up runs after downtime (`Persistent=true`), randomised start times, dependencies, resource limits, and `OnFailure=` alerts.

---

## 1. Minimal Example

`/etc/systemd/system/cleanup.service` — **what** to run:

```ini
[Unit]
Description=Clean old files from /srv/tmp

[Service]
Type=oneshot
ExecStart=/usr/bin/find /srv/tmp -type f -mtime +7 -delete
```

`/etc/systemd/system/cleanup.timer` — **when** to run it:

```ini
[Unit]
Description=Daily cleanup of /srv/tmp

[Timer]
OnCalendar=daily
Persistent=true

[Install]
WantedBy=timers.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now cleanup.timer
systemctl list-timers cleanup.timer
```

Enable and start the **timer**, not the service. Use `Unit=other.service` in `[Timer]` if the names differ.

---

## 2. `OnCalendar` Syntax

Format: `DayOfWeek Year-Month-Day Hour:Minute:Second`. `*` means any value, `..` a range, `,` a list, and `/` a repeat step.

| Expression | Runs |
| --- | --- |
| `minutely` / `hourly` / `daily` / `weekly` / `monthly` | Start of each period (daily = midnight) |
| `*-*-* 02:30:00` | Every day at 02:30 |
| `Mon..Fri 08:00` | Weekdays at 08:00 |
| `Sat,Sun 10:00` | Weekends at 10:00 |
| `*:0/15` | Every 15 minutes |
| `*-*-* 00/6:00:00` | Every 6 hours (00, 06, 12, 18) |
| `*-*-01 03:00` | First day of each month at 03:00 |
| `Sun *-*-1..7 04:00` | First Sunday of each month at 04:00 |
| `*-*-* 09:00 America/Toronto` | 09:00 in a specific time zone |

Several `OnCalendar=` lines in one timer are combined.

### Test an Expression Before Using It

```bash
systemd-analyze calendar "Mon..Fri 08:00"
systemd-analyze calendar --iterations=5 "*:0/15"
```

---

## 3. Relative (Monotonic) Timers

Run relative to an event instead of the clock:

```ini
[Timer]
OnBootSec=5min
OnUnitActiveSec=1h
```

| Setting | Counts from |
| --- | --- |
| `OnBootSec=` | System boot |
| `OnStartupSec=` | systemd start (user manager start for user timers) |
| `OnActiveSec=` | The timer being started |
| `OnUnitActiveSec=` | The service last starting |
| `OnUnitInactiveSec=` | The service last finishing |

The pair above means "5 minutes after boot, then every hour after the last run".

---

## 4. Useful `[Timer]` Options

| Option | Effect |
| --- | --- |
| `Persistent=true` | Run at boot if a scheduled run was missed while off (calendar timers only) |
| `RandomizedDelaySec=15m` | Add a random delay up to 15 minutes (spreads load) |
| `AccuracySec=1s` | Fire precisely; default is up to 1 minute late to save power |
| `WakeSystem=true` | Wake the machine from suspend to run |
| `Unit=name.service` | Start a differently named service |

---

## 5. Useful `[Service]` Options for Jobs

```ini
[Unit]
Description=Nightly backup
Wants=network-online.target
After=network-online.target
OnFailure=ntfy-failure@%n.service

[Service]
Type=oneshot
User=backup
EnvironmentFile=/etc/backup/env
ExecStartPre=/usr/local/bin/dump-databases.sh
ExecStart=/usr/local/bin/backup.sh
TimeoutStartSec=4h
Nice=10
IOSchedulingClass=idle
```

- `Type=oneshot` is right for jobs that run and exit.
- `OnFailure=` starts another unit (for example a notification) if the job fails.
- `Nice=` and `IOSchedulingClass=idle` keep the job from slowing the system.
- Several `ExecStart=` lines run in order with `Type=oneshot`.

---

## 6. User Timers (No Root)

Put both files in `~/.config/systemd/user/` and use `--user`:

```bash
systemctl --user daemon-reload
systemctl --user enable --now cleanup.timer
systemctl --user list-timers
journalctl --user -u cleanup.service
```

User timers only run while you're logged in, unless lingering is enabled:

```bash
sudo loginctl enable-linger $USER
```

---

## 7. Manage & Debug

```bash
# All timers: next run, time left, last run
systemctl list-timers --all

# Run the job now, without waiting for the timer
sudo systemctl start cleanup.service

# Did the last run succeed?
systemctl status cleanup.service

# Output from the job
journalctl -u cleanup.service -n 50
journalctl -u cleanup.service --since today

# Stop scheduling it
sudo systemctl disable --now cleanup.timer

# Check unit files for mistakes
systemd-analyze verify /etc/systemd/system/cleanup.*
```

### One-Off Jobs Without Writing Files

```bash
# Run a command once in 30 minutes
sudo systemd-run --on-active=30m /usr/bin/touch /tmp/done

# Run a command every day at 03:00 until reboot
sudo systemd-run --on-calendar="*-*-* 03:00" --unit=tmp-job /usr/local/bin/job.sh
```

---

## 8. Cron to systemd Translation

| cron | `OnCalendar=` |
| --- | --- |
| `*/15 * * * *` | `*:0/15` |
| `0 * * * *` | `hourly` |
| `30 2 * * *` | `*-*-* 02:30:00` |
| `0 8 * * 1-5` | `Mon..Fri 08:00` |
| `0 4 1 * *` | `*-*-01 04:00` |
| `@reboot` | `OnBootSec=1min` (monotonic) |

| cron habit | systemd equivalent |
| --- | --- |
| `MAILTO=` | `OnFailure=` with a notification service |
| `>> /var/log/job.log 2>&1` | Not needed: output goes to the journal |
| `anacron` catch-up | `Persistent=true` |
| `flock` to prevent overlap | Automatic: a running service isn't started twice |

---

## Quick Reference

```bash
systemctl list-timers --all                     # all timers
systemd-analyze calendar "Mon..Fri 08:00"       # test a schedule
sudo systemctl enable --now job.timer           # activate
sudo systemctl start job.service                # run now
journalctl -u job.service -n 50                 # job output
systemctl --user list-timers                    # user timers
sudo systemd-run --on-active=10m cmd            # one-off delayed job
```

---

## Sources & Verification

- **Timer options:** [systemd.timer(5)](https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html)
- **Calendar syntax:** [systemd.time(7)](https://www.freedesktop.org/software/systemd/man/latest/systemd.time.html)

## Related guides

- [systemd and journalctl Cheat Sheet](systemd-journalctl-cheat-sheet.md)
- [ntfy Notifications Cheat Sheet](ntfy-notifications-cheat-sheet.md)
- [restic and Backrest Backup Cheat Sheet](../storage-and-filesystems/restic-backrest-backup-cheat-sheet.md)
- [Podman Quadlets Cheat Sheet](../../containers/podman-quadlets-cheat-sheet.md)
