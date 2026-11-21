# Podman Quadlets Cheat Sheet

Quick-reference guide for running containers as systemd services with Podman Quadlets.

A **Quadlet** is a small unit-style file (`.container`, `.network`, `.volume`, `.pod`, `.image`, `.build`, `.kube`) that Podman turns into a normal systemd service at boot or on `daemon-reload`. You get declarative containers that start on boot, restart on failure, log to the journal, and auto-update, with no daemon and no Compose.

---

## 1. Where Quadlet Files Live

| Scope | Directory | Manage with |
| --- | --- | --- |
| Rootless (your user) | `~/.config/containers/systemd/` | `systemctl --user` |
| Rootful (system) | `/etc/containers/systemd/` | `sudo systemctl` |

Subdirectories are allowed, so you can keep one folder per app:

```text
~/.config/containers/systemd/
├── apps.network
├── nextcloud/
│   ├── nextcloud.container
│   ├── nextcloud-db.container
│   └── nextcloud-db.volume
└── caddy/
    └── caddy.container
```

### Let Rootless Services Run Without a Login

Rootless user services stop when you log out unless lingering is enabled:

```bash
sudo loginctl enable-linger $USER
loginctl show-user $USER --property=Linger
```

---

## 2. Your First Container

`~/.config/containers/systemd/whoami.container`:

```ini
[Unit]
Description=whoami test container

[Container]
Image=docker.io/traefik/whoami:latest
ContainerName=whoami
PublishPort=127.0.0.1:8080:80

[Service]
Restart=always

[Install]
WantedBy=default.target
```

Load and start it:

```bash
systemctl --user daemon-reload
systemctl --user start whoami.service
systemctl --user status whoami.service
curl http://127.0.0.1:8080
```

The service name is the file name with `.service` instead of `.container`. `systemctl enable` does **not** work on Quadlet units: the `[Install]` section is what makes them start on boot. Use `default.target` for rootless and `multi-user.target` for rootful.

---

## 3. Common `[Container]` Keys

| Key | Example | Equivalent `podman run` flag |
| --- | --- | --- |
| `Image=` | `docker.io/library/postgres:16` | image |
| `ContainerName=` | `nextcloud-db` | `--name` |
| `PublishPort=` | `127.0.0.1:8080:80` | `-p` |
| `Volume=` | `nextcloud-db.volume:/var/lib/postgresql/data:Z` | `-v` |
| `Network=` | `apps.network` | `--network` |
| `Environment=` | `TZ=America/Toronto` | `-e` |
| `EnvironmentFile=` | `%h/.config/nextcloud/env` | `--env-file` |
| `Secret=` | `db-password,type=env,target=POSTGRES_PASSWORD` | `--secret` |
| `Exec=` | `--config /etc/app.yml` | command arguments |
| `UserNS=` | `keep-id` | `--userns` |
| `AutoUpdate=` | `registry` | `io.containers.autoupdate` label |
| `HealthCmd=` | `pg_isready -U postgres` | `--health-cmd` |
| `Pod=` | `nextcloud.pod` | `--pod` |
| `Label=` | `app=nextcloud` | `--label` |
| `PodmanArgs=` | `--memory=2g` | any other flag |

`%h` expands to your home directory in rootless units. Add `:Z` to bind mounts on SELinux systems so the container can read them.

---

## 4. Networks, Volumes & Pods

### Network — `apps.network`

```ini
[Network]
NetworkName=apps
```

Containers on the same user-defined network reach each other by container name (for example `nextcloud-db:5432`).

### Volume — `nextcloud-db.volume`

```ini
[Volume]
VolumeName=nextcloud-db
```

### Pod — `nextcloud.pod`

```ini
[Pod]
PodName=nextcloud
PublishPort=127.0.0.1:8081:80
```

Containers join with `Pod=nextcloud.pod` and share the pod's network namespace, so they talk over `localhost`. Ports are published on the pod, not the containers.

Referencing `apps.network`, `x.volume`, or `x.pod` in a `.container` file creates the systemd dependency automatically: the network or volume is created before the container starts.

---

## 5. Multi-Container Example (App + Database)

`nextcloud-db.container`:

```ini
[Unit]
Description=Nextcloud PostgreSQL

[Container]
Image=docker.io/library/postgres:16
ContainerName=nextcloud-db
Network=apps.network
Volume=nextcloud-db.volume:/var/lib/postgresql/data:Z
Environment=POSTGRES_USER=nextcloud POSTGRES_DB=nextcloud
Secret=nextcloud-db-pass,type=env,target=POSTGRES_PASSWORD
HealthCmd=pg_isready -U nextcloud
AutoUpdate=registry

[Service]
Restart=always

[Install]
WantedBy=default.target
```

`nextcloud.container`:

```ini
[Unit]
Description=Nextcloud
Requires=nextcloud-db.service
After=nextcloud-db.service

[Container]
Image=docker.io/library/nextcloud:stable
ContainerName=nextcloud
Network=apps.network
Volume=%h/appdata/nextcloud:/var/www/html:Z
Environment=POSTGRES_HOST=nextcloud-db POSTGRES_USER=nextcloud POSTGRES_DB=nextcloud
Secret=nextcloud-db-pass,type=env,target=POSTGRES_PASSWORD
AutoUpdate=registry

[Service]
Restart=always

[Install]
WantedBy=default.target
```

---

## 6. Secrets

Keep passwords out of Quadlet files with Podman secrets:

```bash
# Create from a prompt (no shell history)
read -rs PASS && printf '%s' "$PASS" | podman secret create nextcloud-db-pass - && unset PASS

# Create from a random value
openssl rand -base64 32 | podman secret create app-key -

# List and inspect (values are not shown)
podman secret ls
podman secret inspect nextcloud-db-pass

# Remove
podman secret rm nextcloud-db-pass
```

Use in a Quadlet as an environment variable (`type=env,target=VAR`) or as a file mounted at `/run/secrets/<name>` (`Secret=name` alone).

---

## 7. Managing Quadlets

```bash
# Reload after adding or editing any Quadlet file
systemctl --user daemon-reload

# Start, stop, restart, status
systemctl --user restart nextcloud.service
systemctl --user status nextcloud.service

# Logs (follow)
journalctl --user -u nextcloud.service -f

# List all generated services
systemctl --user list-units --type=service | grep -iE "container|pod"
```

### `podman quadlet` Commands (Podman 5.6+)

```bash
# List installed Quadlets and their status
podman quadlet list

# Print the contents of an installed Quadlet
podman quadlet print nextcloud.container

# Install a Quadlet file (or a directory of them) for the current user
podman quadlet install ./nextcloud/

# Remove an installed Quadlet
podman quadlet rm nextcloud.container
```

On older Podman versions, copy files into the Quadlet directory by hand and run `daemon-reload`.

---

## 8. Debugging

```bash
# Show the generated systemd unit, or the syntax error
/usr/libexec/podman/quadlet -dryrun -user

# Rootful version
sudo /usr/libexec/podman/quadlet -dryrun

# Check the generator's messages in the journal
journalctl --user -b | grep -i quadlet

# Inspect the generated unit for one service
systemctl --user cat nextcloud.service
```

| Problem | Likely cause |
| --- | --- |
| `Unit nextcloud.service not found` | Typo or unknown key in the file; run the `-dryrun` command |
| Service stops when you log out | Lingering not enabled |
| `Permission denied` on a bind mount | Missing `:Z` (SELinux) or wrong owner; try `UserNS=keep-id` |
| Containers can't resolve each other | Not on the same user-defined `.network` |
| Can't bind port 80 or 443 rootless | Ports under 1024 are privileged; see Section 10 |

---

## 9. Auto-Updates

Set `AutoUpdate=registry` on each container, then enable the timer:

```bash
systemctl --user enable --now podman-auto-update.timer

# Preview which containers would update
podman auto-update --dry-run

# Update now
podman auto-update
```

If an updated container fails to start, Podman rolls back to the previous image. Use a fully qualified image name (`docker.io/...`) so the update check works.

---

## 10. Rootless Tips

```bash
# Allow rootless containers to bind ports from 80 upward (persistent)
echo "net.ipv4.ip_unprivileged_port_start=80" | sudo tee /etc/sysctl.d/90-unprivileged-ports.conf && sudo sysctl --system

# Run a command inside a container
podman exec -it nextcloud bash

# Fix file ownership inside the rootless user namespace
podman unshare chown -R 33:33 ~/appdata/nextcloud
```

Alternatively, publish high ports (8080, 8443) and redirect 80/443 to them with firewalld.

---

## 11. Quick Reference

```bash
loginctl enable-linger $USER                          # keep services running after logout
systemctl --user daemon-reload                        # regenerate units after edits
systemctl --user start app.service                    # start a Quadlet
journalctl --user -u app.service -f                   # follow logs
podman quadlet list                                   # list Quadlets (Podman 5.6+)
/usr/libexec/podman/quadlet -dryrun -user             # validate files
podman secret create name -                           # create a secret from stdin
systemctl --user enable --now podman-auto-update.timer  # nightly image updates
```

---

## Sources & Verification

- **Quadlet file syntax:** [podman-systemd.unit(5)](https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html)
- **`podman quadlet` commands:** [podman-quadlet(1)](https://docs.podman.io/en/latest/markdown/podman-quadlet.1.html)

## Related guides

- [Podman Cheat Sheet](podman-cheat-sheet.md)
- [Caddy Reverse Proxy Cheat Sheet](../networking-and-security/networking/caddy-reverse-proxy-cheat-sheet.md)
- [systemd Timers Cheat Sheet](../linux-general/system-administration/systemd-timers-cheat-sheet.md)
- [systemd and journalctl Cheat Sheet](../linux-general/system-administration/systemd-journalctl-cheat-sheet.md)
