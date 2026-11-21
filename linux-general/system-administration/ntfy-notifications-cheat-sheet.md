# ntfy Notifications Cheat Sheet

Quick-reference guide for sending push notifications from servers and scripts to your phone with ntfy.

**ntfy** is a publish/subscribe notification service. You **publish** a message to a **topic** with a simple HTTP request (`curl` is enough), and every device **subscribed** to that topic gets a push notification. You can use the public server `ntfy.sh` or self-host your own.

---

## 1. Send Your First Notification

Install the ntfy app on your phone (Android or iOS), subscribe to a topic, then publish to it:

```bash
curl -d "Backup finished" https://ntfy.sh/my-secret-topic-8f3k2
```

On the public server, **anyone who knows the topic name can read and post to it**. Use a long random topic name, or self-host with access control (Section 5).

---

## 2. Message Options (Headers)

Options are HTTP headers. Most have short aliases and an `X-` form (`Title`, `X-Title`, `t`).

```bash
curl -H "Title: Disk space low on $(hostname)" -H "Priority: high" -H "Tags: warning,floppy_disk" -d "Only 5 GB left on /" https://ntfy.example.com/alerts
```

| Header | Example | Effect |
| --- | --- | --- |
| `Title` | `Backup failed` | Notification title |
| `Priority` | `1`–`5` or `min`, `low`, `default`, `high`, `urgent` | Sound, vibration, and pop-up behaviour |
| `Tags` | `warning,skull` | Emoji (if the tag matches one) and labels |
| `Click` | `https://grafana.home.lan` | URL opened when tapping the notification |
| `Markdown` | `yes` | Render the message body as Markdown |
| `Delay` | `30m`, `tomorrow 9am` | Schedule delivery |
| `Actions` | `view, Open, https://host/` | Up to three buttons |
| `Icon` | `https://host/icon.png` | Notification icon |
| `Filename` | `backup.log` | Name for an attached file (with `-T`) |
| `Authorization` | `Bearer tk_...` | Access token (self-hosted with auth) |

Priority `5` / `urgent` makes a long vibration and pop-up on Android; `1` / `min` shows silently.

### Common Tags

`white_check_mark` ✅, `x` ❌, `warning` ⚠️, `rotating_light` 🚨, `floppy_disk` 💾, `lock` 🔒, `arrows_counterclockwise` 🔄.

### Send a File

```bash
curl -T /var/log/backup.log -H "Filename: backup.log" https://ntfy.example.com/backups
```

---

## 3. Use in Scripts

### Reusable Function

```bash
notify() {
    curl -fsS -m 10 -H "Authorization: Bearer ${NTFY_TOKEN}" -H "Title: $1" -H "Priority: ${3:-default}" -d "$2" "${NTFY_URL}" >/dev/null || true
}

notify "Backup OK" "Nightly backup finished on $(hostname)"
notify "Backup FAILED" "restic exited with an error" urgent
```

`-m 10` stops a slow notification server from hanging the script, and `|| true` stops a failed notification from failing the job.

### Alert on Failure Only

```bash
restic backup /srv || notify "Backup FAILED" "restic backup on $(hostname) failed" high
```

### Low Disk Space Check

```bash
used=$(df --output=pcent / | tail -1 | tr -dc '0-9'); [ "$used" -ge 90 ] && notify "Disk ${used}% full" "Root filesystem on $(hostname) is ${used}% full" high
```

### Notify on SSH Login

Add to `/etc/profile.d/ntfy-login.sh` (or a PAM `pam_exec` script):

```bash
[ -n "$SSH_CONNECTION" ] && curl -fsS -m 5 -H "Title: SSH login on $(hostname)" -H "Tags: lock" -d "$USER from ${SSH_CONNECTION%% *}" https://ntfy.example.com/logins >/dev/null 2>&1 &
```

---

## 4. Alert When a systemd Service Fails

Create a template service `/etc/systemd/system/ntfy-failure@.service`:

```ini
[Unit]
Description=Send ntfy alert for %i

[Service]
Type=oneshot
EnvironmentFile=/etc/ntfy-alert.env
ExecStart=/usr/bin/sh -c 'curl -fsS -m 10 -H "Authorization: Bearer $NTFY_TOKEN" -H "Title: %i failed on %H" -H "Priority: high" -H "Tags: rotating_light" -d "$(journalctl -u %i -n 20 --no-pager)" "$NTFY_URL"'
```

`/etc/ntfy-alert.env` (mode `600`):

```text
NTFY_URL=https://ntfy.example.com/alerts
NTFY_TOKEN=tk_REPLACE_ME
```

Then add one line to any service you want watched (with `sudo systemctl edit restic-backup.service`):

```ini
[Unit]
OnFailure=ntfy-failure@%n.service
```

For rootless Quadlet services, put the same template in `~/.config/systemd/user/` and use `journalctl --user`.

---

## 5. Self-Host ntfy

### Quadlet

```ini
[Unit]
Description=ntfy

[Container]
Image=docker.io/binwiederhier/ntfy:latest
ContainerName=ntfy
Exec=serve
Network=apps.network
Volume=%h/appdata/ntfy/etc:/etc/ntfy:Z
Volume=%h/appdata/ntfy/cache:/var/cache/ntfy:Z
Volume=%h/appdata/ntfy/lib:/var/lib/ntfy:Z
Environment=TZ=America/Toronto
AutoUpdate=registry

[Service]
Restart=always

[Install]
WantedBy=default.target
```

### `/etc/ntfy/server.yml`

```yaml
base-url: "https://ntfy.example.com"
behind-proxy: true
cache-file: "/var/cache/ntfy/cache.db"
attachment-cache-dir: "/var/cache/ntfy/attachments"
auth-file: "/var/lib/ntfy/user.db"
auth-default-access: "deny-all"
```

`base-url` must be the exact URL your phone uses. `behind-proxy: true` makes ntfy read the client IP from the proxy's headers (Caddy sets them automatically).

### Users, Access & Tokens

```bash
# Create an admin and a publishing user
podman exec -it ntfy ntfy user add --role=admin admin
podman exec -it ntfy ntfy user add alerts-bot
podman exec -it ntfy ntfy user add phone-user

# Grant access: rw = read-write, ro = subscribe only, wo = publish only
podman exec ntfy ntfy access alerts-bot alerts wo
podman exec ntfy ntfy access phone-user alerts ro

# Create a token for scripts
podman exec ntfy ntfy token add alerts-bot

# Review
podman exec ntfy ntfy user list
podman exec ntfy ntfy access
```

Log in on the phone app as `phone-user`, and use the token in scripts.

### iOS Push with a Self-Hosted Server

iOS delivers instant notifications through Apple's push service, which self-hosted servers reach via `ntfy.sh`. Add this to `server.yml` so iOS gets notified promptly:

```yaml
upstream-base-url: "https://ntfy.sh"
```

The message content isn't sent to `ntfy.sh`; it only gets a poll request that tells the phone to fetch the message from your server.

---

## 6. The `ntfy` CLI

```bash
# Publish
ntfy publish --title "Hello" --priority high --tags tada mytopic "Test message"

# Publish to a self-hosted server with a token
ntfy publish --token tk_REPLACE_ME https://ntfy.example.com/alerts "Test"

# Subscribe and print messages
ntfy subscribe mytopic

# Run a command for every message received
ntfy subscribe mytopic 'notify-send "$m"'
```

---

## 7. Troubleshooting

| Problem | Likely cause |
| --- | --- |
| `403 forbidden` | User lacks write access to the topic, or the token is wrong |
| `401 unauthorized` | Missing `Authorization` header with `auth-default-access: deny-all` |
| Phone gets nothing | Phone subscribed to a different server URL than `base-url` |
| iOS notifications are delayed | `upstream-base-url` not set |
| Works when run by hand, not from cron or a timer | `NTFY_URL` / `NTFY_TOKEN` not set in cron's environment |

Test from the command line with verbose output:

```bash
curl -v -H "Authorization: Bearer $NTFY_TOKEN" -d "test" "$NTFY_URL"
```

---

## Sources & Verification

- **Publishing options and headers:** [ntfy publishing docs](https://docs.ntfy.sh/publish/)
- **Self-hosting, users, and access control:** [ntfy server configuration](https://docs.ntfy.sh/config/)

## Related guides

- [systemd Timers Cheat Sheet](systemd-timers-cheat-sheet.md)
- [systemd and journalctl Cheat Sheet](systemd-journalctl-cheat-sheet.md)
- [restic and Backrest Backup Cheat Sheet](../storage-and-filesystems/restic-backrest-backup-cheat-sheet.md)
- [Podman Quadlets Cheat Sheet](../../containers/podman-quadlets-cheat-sheet.md)
