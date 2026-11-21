# Caddy Reverse Proxy Cheat Sheet

Quick-reference guide for running Caddy as an HTTPS reverse proxy for self-hosted services.

**Caddy** is a web server that turns on HTTPS automatically. For public domains it gets certificates from Let's Encrypt or ZeroSSL; for internal names it can act as its own private certificate authority (CA). Configuration lives in a short, readable `Caddyfile`.

---

## 1. Install

```bash
# Fedora
sudo dnf install caddy

# RHEL / Rocky (official Caddy COPR)
sudo dnf install 'dnf-command(copr)' && sudo dnf copr enable @caddy/caddy && sudo dnf install caddy

# Debian / Ubuntu: add the official Caddy repo first (see caddyserver.com/docs/install)
sudo apt install caddy

# Arch Linux
sudo pacman -S caddy

# Container image
podman pull docker.io/library/caddy:latest
```

Package installs read `/etc/caddy/Caddyfile` and run as the `caddy` user via `caddy.service`.

---

## 2. Caddyfile Basics

```caddyfile
# Global options block (optional, must be first)
{
    email you@example.com
}

# One site block per hostname
app.example.com {
    reverse_proxy 127.0.0.1:8080
}
```

- Indentation is for readability only; `caddy fmt` (which uses tabs) tidies it.
- A site address with a real domain gets a public certificate automatically (ports 80 and 443 must be reachable).
- `http://` in front of an address disables HTTPS for that site.

---

## 3. Reverse Proxy Patterns

```caddyfile
# Basic proxy
nextcloud.home.lan {
    reverse_proxy nextcloud:80
}

# Several backends with load balancing and health checks
api.home.lan {
    reverse_proxy 10.0.0.11:3000 10.0.0.12:3000 {
        lb_policy round_robin
        health_uri /health
    }
}

# Path-based routing
tools.home.lan {
    handle_path /logs/* {
        reverse_proxy dozzle:8080
    }
    handle {
        reverse_proxy it-tools:80
    }
}

# Backend that already serves HTTPS with a self-signed certificate
cockpit.home.lan {
    reverse_proxy https://127.0.0.1:9090 {
        transport http {
            tls_insecure_skip_verify
        }
    }
}
```

`handle_path` strips the matched prefix before proxying; `handle` keeps it. Caddy passes `X-Forwarded-For`, `X-Forwarded-Proto`, and `X-Forwarded-Host` to backends automatically.

### Reusable Snippets

```caddyfile
(internal) {
    tls internal
    encode zstd gzip
}

paperless.home.lan {
    import internal
    reverse_proxy paperless:8000
}
```

---

## 4. Internal HTTPS with Caddy's Private CA

For names that only exist on your network or VPN (such as `*.home.lan`), use `tls internal`:

```caddyfile
{
    local_certs
}

homepage.home.lan {
    reverse_proxy homepage:3000
}
```

`local_certs` in the global block makes every site use the internal CA; `tls internal` inside one site does it for just that site.

### Trust the Root Certificate

Each device that visits these sites must trust Caddy's root CA once. Find it at `<caddy data dir>/pki/authorities/local/root.crt`:

| How Caddy runs | Path to `root.crt` |
| --- | --- |
| Package (`caddy.service`) | `/var/lib/caddy/.local/share/caddy/pki/authorities/local/root.crt` |
| Official container | `/data/caddy/pki/authorities/local/root.crt` (inside the container) |

```bash
# Copy it out of a container
podman cp caddy:/data/caddy/pki/authorities/local/root.crt ./caddy-root.crt

# Trust it on Fedora / RHEL / Rocky
sudo cp caddy-root.crt /etc/pki/ca-trust/source/anchors/ && sudo update-ca-trust

# Trust it on Debian / Ubuntu
sudo cp caddy-root.crt /usr/local/share/ca-certificates/caddy-root.crt && sudo update-ca-certificates

# Trust it on Arch
sudo trust anchor caddy-root.crt
```

On phones, install `root.crt` as a CA certificate (iOS also needs it enabled under Settings → General → About → Certificate Trust Settings). Firefox uses its own store unless `security.enterprise_roots.enabled` is set.

Caddy can't install its root into the host trust store from inside a container, so this step is manual.

---

## 5. Useful Directives

```caddyfile
site.home.lan {
    # Compression
    encode zstd gzip

    # Security headers
    header {
        Strict-Transport-Security "max-age=31536000"
        X-Content-Type-Options nosniff
        -Server
    }

    # Basic auth (hash with: caddy hash-password)
    basic_auth /admin/* {
        admin $2a$14$REPLACE_WITH_HASH
    }

    # Only allow the Tailscale range
    @notvpn not remote_ip 100.64.0.0/10
    respond @notvpn "Forbidden" 403

    # Redirects
    redir /old /new permanent

    # Access log
    log {
        output file /var/log/caddy/site.log
    }

    reverse_proxy backend:8080
}
```

```bash
caddy hash-password
```

---

## 6. Run Caddy in Podman (Quadlet)

`~/.config/containers/systemd/caddy.container`:

```ini
[Unit]
Description=Caddy reverse proxy

[Container]
Image=docker.io/library/caddy:latest
ContainerName=caddy
Network=apps.network
PublishPort=80:80
PublishPort=443:443
PublishPort=443:443/udp
Volume=%h/appdata/caddy/Caddyfile:/etc/caddy/Caddyfile:Z
Volume=caddy-data:/data
Volume=caddy-config:/config
AutoUpdate=registry

[Service]
Restart=always

[Install]
WantedBy=default.target
```

- Keep `/data` on a persistent volume; it holds the certificates and the private CA. Losing it means re-trusting a new root on every device.
- Put Caddy on the same Podman network as the apps and proxy to them by container name.
- Rootless containers need `net.ipv4.ip_unprivileged_port_start=80` to publish ports 80 and 443.

---

## 7. Validate, Reload & Debug

```bash
# Format the Caddyfile in place
caddy fmt --overwrite /etc/caddy/Caddyfile

# Check the config without applying it
caddy validate --config /etc/caddy/Caddyfile

# Reload without downtime (package install)
sudo systemctl reload caddy

# Reload inside a container
podman exec -w /etc/caddy caddy caddy reload

# Logs
journalctl -u caddy -f
podman logs -f caddy

# Test a site, showing the certificate chain
curl -vI https://app.home.lan
```

| Problem | Likely cause |
| --- | --- |
| Browser: certificate not trusted | Root CA not installed on that device |
| `502 Bad Gateway` | Backend down, wrong port, or not on the same network |
| `dial tcp: lookup app: no such host` | Caddy and the app are on different Podman networks |
| Certificate errors for a public domain | Ports 80/443 not reachable, or DNS doesn't point to the server |
| Redirect loop | Backend also forces HTTPS; set its "trusted proxy" setting |

---

## 8. Quick Reference

```bash
caddy fmt --overwrite Caddyfile       # tidy formatting
caddy validate --config Caddyfile     # check config
sudo systemctl reload caddy           # apply changes
caddy hash-password                   # make a basic_auth hash
caddy trust                           # install the root CA (non-container installs)
caddy version                         # show version
```

---

## Sources & Verification

- **Caddyfile and directives:** [Caddy documentation](https://caddyserver.com/docs/caddyfile)
- **Internal CA and trust:** [Caddy `tls` directive](https://caddyserver.com/docs/caddyfile/directives/tls) and [Automatic HTTPS](https://caddyserver.com/docs/automatic-https)

## Related guides

- [CoreDNS Cheat Sheet](coredns-cheat-sheet.md)
- [Podman Quadlets Cheat Sheet](../../containers/podman-quadlets-cheat-sheet.md)
- [Tailscale Mesh Networking Cheat Sheet](tailscale-mesh-cli-cheat-sheet.md)
- [Cockpit Cheat Sheet](../../linux-general/system-administration/cockpit-cheat-sheet.md)
