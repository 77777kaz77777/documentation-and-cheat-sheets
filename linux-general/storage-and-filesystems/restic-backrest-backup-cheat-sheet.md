# restic and Backrest Backup Cheat Sheet

Quick-reference guide for encrypted, deduplicated backups with restic, and for managing them through the Backrest web UI.

**restic** backs up files into a **repository** (a local folder, SFTP server, S3 bucket, or other backend). Every backup is a **snapshot**; data is split into chunks, deduplicated, compressed, and encrypted with your repository password. **Backrest** is a web UI and scheduler that runs restic for you.

> **Lose the repository password and the backups are unrecoverable.** Store it in a password manager and somewhere offline.

---

## 1. Install

```bash
# RHEL / Fedora / Rocky (EPEL on RHEL and Rocky)
sudo dnf install restic

# Debian / Ubuntu
sudo apt install restic

# Arch Linux
sudo pacman -S restic

# Update a distro package to the latest release
sudo restic self-update
```

---

## 2. Set Up a Repository

Set the repository and password once per shell (or in a root-only env file) so you don't repeat them:

```bash
export RESTIC_REPOSITORY=/mnt/backup/restic
export RESTIC_PASSWORD_FILE=/root/.config/restic/password
```

```bash
# Create the password file (root-only)
sudo install -d -m 700 /root/.config/restic && sudo sh -c 'openssl rand -base64 32 > /root/.config/restic/password' && sudo chmod 600 /root/.config/restic/password

# Initialise the repository
restic init
```

### Repository Locations

| Backend | `RESTIC_REPOSITORY` example |
| --- | --- |
| Local folder or drive | `/mnt/backup/restic` |
| SFTP | `sftp:user@backup-host:/srv/restic` |
| REST server | `rest:https://user:pass@host:8000/repo` |
| S3-compatible | `s3:https://s3.example.com/bucket-name` |
| Backblaze B2 | `b2:bucket-name:path` |
| Any rclone remote | `rclone:remote:path` |

Cloud backends read credentials from environment variables such as `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` (S3) or `B2_ACCOUNT_ID` and `B2_ACCOUNT_KEY` (B2).

---

## 3. Back Up

```bash
# Back up directories
restic backup /home /etc /srv

# Tag a backup and exclude caches
restic backup /home --tag nightly --exclude-caches --exclude="*.tmp" --exclude="/home/*/.cache"

# Read excludes from a file
restic backup /home --exclude-file=/etc/restic/excludes.txt

# Back up a database dump straight from stdin
pg_dump -U nextcloud nextcloud | restic backup --stdin --stdin-filename nextcloud.sql

# Show what would be backed up without doing it
restic backup /home --dry-run -v
```

### Back Up Databases from Containers

Dump databases first, then back up the dump files, so the backup is consistent:

```bash
podman exec nextcloud-db pg_dump -U nextcloud nextcloud > /srv/dumps/nextcloud.sql
podman exec paperless-db pg_dumpall -U paperless > /srv/dumps/paperless.sql
sqlite3 /srv/appdata/app/app.db ".backup '/srv/dumps/app.db'"
```

---

## 4. Browse Snapshots

```bash
# List snapshots
restic snapshots

# Only one host or tag
restic snapshots --host server1 --tag nightly

# List files in the latest snapshot
restic ls latest /etc

# Find a file across all snapshots
restic find "*.conf"

# Compare two snapshots
restic diff 4bba301e 0eb9a3a2

# Repository size and dedup statistics
restic stats --mode raw-data
```

---

## 5. Restore

```bash
# Restore the latest snapshot into a new folder
restic restore latest --target /tmp/restore

# Restore only some paths
restic restore latest --target /tmp/restore --include /etc/caddy

# Restore one specific snapshot
restic restore 4bba301e --target /tmp/restore

# Print one file to stdout
restic dump latest /etc/fstab

# Mount all snapshots as a browsable filesystem (needs FUSE)
mkdir -p /mnt/restic && restic mount /mnt/restic
```

Restore into an empty folder first and copy what you need back, rather than restoring over live data.

---

## 6. Retention & Pruning

```bash
# Keep 7 daily, 4 weekly, 12 monthly snapshots; delete the rest and free space
restic forget --keep-daily 7 --keep-weekly 4 --keep-monthly 12 --prune

# Preview what would be removed
restic forget --keep-daily 7 --keep-weekly 4 --keep-monthly 12 --dry-run

# Apply retention per host and path group
restic forget --group-by host,paths --keep-daily 7 --keep-weekly 4 --prune
```

`forget` only removes snapshot records; `--prune` (or a separate `restic prune`) actually deletes the unused data.

---

## 7. Verify Backups

```bash
# Check repository structure
restic check

# Also read back 10% of the stored data
restic check --read-data-subset=10%

# Read every byte (slow; do this occasionally)
restic check --read-data
```

A backup you have never restored from is not a tested backup. Restore a few files to a scratch folder every month.

### Other Maintenance

```bash
# Remove a stale lock left by a killed backup
restic unlock

# Add another password (key) to the repository
restic key add

# Upgrade an old repository to format v2 (compression)
restic migrate upgrade_repo_v2
```

---

## 8. Automate with a systemd Timer

`/etc/systemd/system/restic-backup.service`:

```ini
[Unit]
Description=restic backup
Wants=network-online.target
After=network-online.target

[Service]
Type=oneshot
EnvironmentFile=/etc/restic/env
ExecStart=/usr/bin/restic backup /home /etc /srv --exclude-caches --tag nightly
ExecStartPost=/usr/bin/restic forget --keep-daily 7 --keep-weekly 4 --keep-monthly 12 --prune
```

`/etc/systemd/system/restic-backup.timer`:

```ini
[Unit]
Description=Nightly restic backup

[Timer]
OnCalendar=*-*-* 02:30:00
Persistent=true
RandomizedDelaySec=15m

[Install]
WantedBy=timers.target
```

`/etc/restic/env` (mode `600`) contains `RESTIC_REPOSITORY=...` and `RESTIC_PASSWORD_FILE=...`.

```bash
sudo systemctl daemon-reload && sudo systemctl enable --now restic-backup.timer
systemctl list-timers restic-backup.timer
```

---

## 9. Backrest (Web UI)

Backrest schedules backups, applies retention, runs checks, and lets you browse and restore snapshots from a browser. It uses an installed restic if one is compatible, or downloads its own.

### Install

```bash
# Container (recommended alongside Podman Quadlets)
podman pull docker.io/garethgeorge/backrest:latest

# Native install: download a release from github.com/garethgeorge/backrest/releases, then:
mkdir backrest && tar -xzf backrest_Linux_x86_64.tar.gz -C backrest && cd backrest && ./install.sh
```

The native installer sets up a service listening on `127.0.0.1:9898` by default. Open `http://localhost:9898`; the first visit asks you to create a username and password.

### Quadlet

```ini
[Container]
Image=docker.io/garethgeorge/backrest:latest
ContainerName=backrest
Network=apps.network
Environment=BACKREST_DATA=/data BACKREST_CONFIG=/config/config.json XDG_CACHE_HOME=/cache TZ=America/Toronto
Volume=%h/appdata/backrest/data:/data:Z
Volume=%h/appdata/backrest/config:/config:Z
Volume=%h/appdata/backrest/cache:/cache:Z
Volume=/srv:/userdata:ro
Volume=/mnt/backup:/repos:Z
```

Mount what you back up read-only, and mount the repository location read-write.

### Typical Setup in the UI

1. **Add Repository:** URI (for example `/repos/restic`), password, and any backend environment variables.
2. **Add Plan:** paths, excludes, schedule (cron or interval), and retention (for example 7 daily, 4 weekly, 12 monthly).
3. **Hooks:** send a notification on `CONDITION_SNAPSHOT_ERROR` or `CONDITION_ANY_ERROR`, for example a command hook that runs `curl` against ntfy.
4. **Check schedule:** set a periodic `check` on the repository.
5. Back up Backrest's own `config.json`; it holds the repository passwords.

---

## 10. Quick Reference

```bash
restic init                                             # create repository
restic backup /path --tag nightly                       # back up
restic snapshots                                        # list snapshots
restic ls latest                                        # browse latest
restic restore latest --target /tmp/restore             # restore
restic forget --keep-daily 7 --keep-weekly 4 --prune    # apply retention
restic check --read-data-subset=10%                     # verify
restic unlock                                           # clear stale lock
restic mount /mnt/restic                                # browse with FUSE
```

---

## Sources & Verification

- **restic commands:** [restic documentation](https://restic.readthedocs.io/en/stable/)
- **Backrest install and defaults:** [Backrest on GitHub](https://github.com/garethgeorge/backrest)

## Related guides

- [Btrbk Snapshot Automation Guide](btrbk-snapshot-automation-cheat-sheet.md)
- [systemd Timers Cheat Sheet](../system-administration/systemd-timers-cheat-sheet.md)
- [ntfy Notifications Cheat Sheet](../system-administration/ntfy-notifications-cheat-sheet.md)
- [Podman Quadlets Cheat Sheet](../../containers/podman-quadlets-cheat-sheet.md)
