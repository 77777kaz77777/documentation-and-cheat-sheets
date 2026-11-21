# Cockpit Cheat Sheet

Quick-reference guide for installing, securing, and using Cockpit to administer Linux servers from a browser.

**Cockpit** is a web console for Linux servers. It shows logs, services, storage, networking, SELinux, updates, and Podman containers, and includes a terminal, all using the server's normal tools underneath. Changes made in Cockpit and on the command line are the same changes. It is installed by default on many RHEL, Rocky, and Fedora Server systems.

---

## 1. Install & Enable

```bash
# RHEL / Fedora / Rocky
sudo dnf install cockpit

# Debian / Ubuntu
sudo apt install cockpit

# Arch Linux
sudo pacman -S cockpit
```

```bash
# Cockpit starts on demand when someone connects to port 9090
sudo systemctl enable --now cockpit.socket

# Open the firewall (firewalld)
sudo firewall-cmd --permanent --add-service=cockpit && sudo firewall-cmd --reload
```

Browse to `https://<server>:9090` and log in with a normal Linux account. Tick **Reuse my password for privileged tasks** (or use **Turn on administrative access**) to get `sudo` rights in the UI.

---

## 2. Add-On Modules

```bash
# Podman containers, images, and pods
sudo dnf install cockpit-podman

# Disks, LVM, RAID, NFS, Stratis
sudo dnf install cockpit-storaged

# SELinux troubleshooting
sudo dnf install cockpit-selinux

# Software updates
sudo dnf install cockpit-packagekit

# Virtual machines (libvirt)
sudo dnf install cockpit-machines

# Diagnostic reports and kdump
sudo dnf install cockpit-sosreport cockpit-kdump

# File browser
sudo dnf install cockpit-files
```

Package names are the same on Debian and Ubuntu (`apt install`), though not every module is packaged on every distro. Refresh the browser after installing a module.

**Podman:** `cockpit-podman` shows both rootful containers and your user's rootless containers. Quadlet-managed containers appear there too; manage their lifecycle with `systemctl --user` so systemd stays in charge.

---

## 3. Restrict Access

Cockpit is a full root-capable shell in a browser. Don't expose it to the internet.

### Allow Only the VPN (firewalld)

```bash
# Remove from the default (public) zone
sudo firewall-cmd --permanent --remove-service=cockpit

# Allow on the Tailscale interface only
sudo firewall-cmd --permanent --zone=trusted --add-interface=tailscale0
sudo firewall-cmd --reload
```

### Listen on a Specific Address or Port

`sudo systemctl edit cockpit.socket`:

```ini
[Socket]
ListenStream=
ListenStream=100.101.102.103:9090
FreeBind=yes
```

The empty `ListenStream=` clears the default. `FreeBind=yes` lets the socket start before the Tailscale address exists.

```bash
sudo systemctl daemon-reload && sudo systemctl restart cockpit.socket
sudo ss -ltnp | grep 9090
```

If you change the port on an SELinux system, label it:

```bash
sudo semanage port -a -t websm_port_t -p tcp 9091
```

### Block Specific Users

Users listed in `/etc/cockpit/disallowed-users` can't log in (root is listed by default on many distros):

```bash
echo "root" | sudo tee -a /etc/cockpit/disallowed-users
```

---

## 4. Configuration (`/etc/cockpit/cockpit.conf`)

```ini
[WebService]
# Required when Cockpit is behind a reverse proxy
Origins = https://cockpit.home.lan wss://cockpit.home.lan
ProtocolHeader = X-Forwarded-Proto
AllowUnencrypted = false

# Login page title
LoginTitle = homelab

[Session]
# Log out after 15 idle minutes
IdleTimeout = 15
```

```bash
sudo systemctl restart cockpit
```

---

## 5. Behind a Reverse Proxy (Caddy)

```caddyfile
cockpit.home.lan {
    tls internal
    reverse_proxy https://127.0.0.1:9090 {
        transport http {
            tls_insecure_skip_verify
        }
    }
}
```

Add the matching `Origins` line from Section 4, or logins will fail with a WebSocket or origin error.

---

## 6. Certificates

Cockpit makes a self-signed certificate on first start. To use your own, put the certificate and key in `/etc/cockpit/ws-certs.d/`:

```bash
sudo cp server.crt /etc/cockpit/ws-certs.d/50-server.crt
sudo cp server.key /etc/cockpit/ws-certs.d/50-server.key
sudo chmod 640 /etc/cockpit/ws-certs.d/50-server.key
sudo systemctl restart cockpit

# See which certificate Cockpit is using
sudo /usr/libexec/cockpit-certificate-ensure --check
```

Cockpit uses the last file alphabetically. The `cockpit-certificate-ensure` path is `/usr/lib/cockpit/` on Debian and Ubuntu.

---

## 7. Managing Several Servers

From one Cockpit, use the host menu (top left) → **Add new host** to connect to others over SSH. The remote host needs the `cockpit-bridge` package but doesn't need `cockpit.socket` running or port 9090 open.

---

## 8. What to Use Cockpit For

| Page | Good for |
| --- | --- |
| **Overview** | CPU, memory, disk I/O, uptime, and health at a glance |
| **Logs** | Filtering the journal by priority, unit, and time |
| **Storage** | Creating partitions, LVM, RAID, and mounting; viewing SMART status |
| **Networking** | Bonds, bridges, VLANs, and the firewall |
| **Podman containers** | Starting, stopping, logs, and exec for containers |
| **Services** | Starting, stopping, enabling units, and timers |
| **SELinux** | Reading denials with suggested fixes |
| **Software updates** | Applying updates and enabling automatic updates |
| **Terminal** | A shell in the browser |

---

## 9. Troubleshooting

```bash
# Is the socket listening?
systemctl status cockpit.socket
sudo ss -ltnp | grep 9090

# Web service logs
journalctl -u cockpit -u cockpit.socket -b

# Check firewall rules
sudo firewall-cmd --list-all --zone=public
sudo firewall-cmd --list-all --zone=trusted
```

| Problem | Likely cause |
| --- | --- |
| Page doesn't load | Socket not enabled, or firewall blocks 9090 |
| Login works but pages are read-only | Administrative access not turned on |
| `root` can't log in | Listed in `/etc/cockpit/disallowed-users` |
| Blank page or WebSocket error behind a proxy | Missing `Origins` in `cockpit.conf` |
| A module is missing | Its `cockpit-*` package isn't installed |

---

## Sources & Verification

- **Installation and modules:** [Cockpit project documentation](https://cockpit-project.org/documentation.html)
- **`cockpit.conf` options:** [cockpit.conf(5)](https://cockpit-project.org/guide/latest/cockpit.conf.5.html)

## Related guides

- [Podman Quadlets Cheat Sheet](../../containers/podman-quadlets-cheat-sheet.md)
- [Caddy Reverse Proxy Cheat Sheet](../../networking-and-security/networking/caddy-reverse-proxy-cheat-sheet.md)
- [Firewalld Cheat Sheet](../../networking-and-security/security/fedora-firewall-cheat-sheet.md)
- [SSH and sshd Hardening Cheat Sheet](../../networking-and-security/security/ssh-hardening-cheat-sheet.md)
