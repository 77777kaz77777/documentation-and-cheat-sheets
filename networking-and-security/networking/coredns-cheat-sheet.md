# CoreDNS Cheat Sheet

Quick-reference guide for running CoreDNS as a small internal DNS server for a homelab or private network.

**CoreDNS** is a DNS server built from plugins. Its configuration file, the `Corefile`, lists one or more **server blocks** (a zone and a port), each with a chain of plugins such as `hosts`, `forward`, and `cache`. It is a good fit for giving self-hosted apps their own internal hostnames.

---

## 1. Install

```bash
# Any distro: official container image (recommended)
podman pull docker.io/coredns/coredns:latest

# Any distro: single static binary from github.com/coredns/coredns/releases
sudo install -m 755 coredns /usr/local/bin/coredns && coredns -version

# Some distros also package it; check first
dnf search coredns    # or: apt search coredns / pacman -Ss coredns
```

The container image has no shell, so debug it with `podman logs` and query it from the host.

---

## 2. Corefile Structure

```text
ZONE[:PORT] {
    plugin [arguments]
    plugin {
        option value
    }
}
```

- `.` means "every name" (the root zone). It is the catch-all block.
- The default port is 53. CoreDNS picks the **most specific** matching zone for each query.
- Plugins run in a fixed order built into CoreDNS, not the order you write them.

### Minimal Caching Forwarder

```corefile
. {
    forward . 1.1.1.1 9.9.9.9
    cache 300
    errors
    log
}
```

---

## 3. Internal Hostnames with `hosts`

```corefile
home.lan {
    hosts {
        100.101.102.103 homepage.home.lan
        100.101.102.103 nextcloud.home.lan
        100.101.102.103 paperless.home.lan
        fallthrough
    }
    errors
    log
}

. {
    forward . 1.1.1.1 9.9.9.9
    cache 300
    errors
}
```

Point every app name at the server running your reverse proxy (here a Tailscale IP); the proxy then routes by hostname. `fallthrough` passes unknown names on to the next plugin instead of answering "not found".

### Keep Records in a Separate File

```corefile
home.lan {
    hosts /etc/coredns/home.hosts {
        reload 10s
        fallthrough
    }
}
```

`/etc/coredns/home.hosts` uses the same format as `/etc/hosts`. CoreDNS re-reads it automatically, so adding an app is just one new line.

### Wildcard Records with `template`

Answer **every** name under `home.lan` with the same IP:

```corefile
home.lan {
    template IN A home.lan {
        answer "{{ .Name }} 60 IN A 100.101.102.103"
    }
}
```

---

## 4. Zone Files with `file`

For a full zone with SOA, NS, MX, and CNAME records:

```corefile
home.lan {
    file /etc/coredns/db.home.lan
    reload 30s
}
```

`/etc/coredns/db.home.lan`:

```text
$ORIGIN home.lan.
@       3600 IN SOA ns.home.lan. admin.home.lan. 2026112001 7200 3600 1209600 3600
@       3600 IN NS  ns.home.lan.
ns      3600 IN A   100.101.102.103
server  3600 IN A   100.101.102.103
*       3600 IN CNAME server.home.lan.
```

Increase the serial number (`2026112001`) every time you edit the file.

---

## 5. Useful Plugins

| Plugin | Purpose |
| --- | --- |
| `forward` | Send queries to upstream resolvers |
| `cache` | Cache answers (seconds) |
| `hosts` | Answer from a hosts-format list or file |
| `file` | Serve a zone from an RFC 1035 zone file |
| `template` | Generate answers from a pattern (wildcards) |
| `rewrite` | Rewrite query names, for example `.lan` to `.home.lan` |
| `errors` | Log errors |
| `log` | Log every query |
| `health` | HTTP health endpoint on `:8080/health` |
| `ready` | Readiness endpoint on `:8181/ready` |
| `prometheus` | Metrics on `:9153/metrics` |
| `reload` | Reload the Corefile automatically when it changes |
| `loop` | Detect forwarding loops and stop |
| `bind` | Listen only on specific IPs |

### Forward over DNS-over-TLS

```corefile
. {
    forward . tls://1.1.1.1 tls://1.0.0.1 {
        tls_servername cloudflare-dns.com
        health_check 5s
    }
    cache 300
}
```

### Listen Only on the VPN Interface

```corefile
home.lan {
    bind 100.101.102.103
    hosts /etc/coredns/home.hosts
}
```

---

## 6. Split DNS over Tailscale

Use CoreDNS for your internal names on every Tailscale device, at home or away:

1. Run CoreDNS on a Tailscale node and `bind` it to that node's Tailscale IP.
2. In the Tailscale admin console, go to **DNS → Nameservers → Add nameserver → Custom**.
3. Enter the CoreDNS node's Tailscale IP and enable **Restrict to domain** with `home.lan`.

Only `*.home.lan` lookups go to CoreDNS; everything else uses normal DNS. Check from a client:

```bash
tailscale status
resolvectl query nextcloud.home.lan
```

---

## 7. Run CoreDNS in Podman (Quadlet)

`/etc/containers/systemd/coredns.container` (rootful, because port 53 is privileged):

```ini
[Unit]
Description=CoreDNS

[Container]
Image=docker.io/coredns/coredns:latest
ContainerName=coredns
Exec=-conf /etc/coredns/Corefile
Volume=/etc/coredns:/etc/coredns:ro,Z
PublishPort=100.101.102.103:53:53/udp
PublishPort=100.101.102.103:53:53/tcp
AutoUpdate=registry

[Service]
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload && sudo systemctl start coredns.service
```

If `systemd-resolved` is listening on port 53, publish only on a specific IP (as above) so they don't clash.

---

## 8. Testing & Troubleshooting

```bash
# Query CoreDNS directly
dig @100.101.102.103 nextcloud.home.lan +short
dig @100.101.102.103 example.com +short

# Without dig (bind-utils / dnsutils)
nslookup nextcloud.home.lan 100.101.102.103

# What resolver is this machine actually using?
resolvectl status

# Is something already on port 53?
sudo ss -lunp 'sport = :53'

# Logs
journalctl -u coredns -f
sudo podman logs -f coredns
```

| Problem | Likely cause |
| --- | --- |
| `bind: address already in use` | `systemd-resolved` or another DNS server on port 53 |
| `NXDOMAIN` for an internal name | Name missing, no `fallthrough`, or the query went to another zone block |
| Works with `dig @ip`, not in the browser | Client isn't using CoreDNS (check `resolvectl status` or Tailscale DNS settings) |
| `Loop ... detected` and CoreDNS exits | `forward . /etc/resolv.conf` points back at CoreDNS; forward to real upstream IPs |
| Changes not picked up | Add the `reload` plugin or restart the service |

Open the firewall if clients are on another host:

```bash
sudo firewall-cmd --permanent --add-service=dns && sudo firewall-cmd --reload
```

---

## Sources & Verification

- **Corefile syntax and plugins:** [CoreDNS manual](https://coredns.io/manual/toc/) and [plugin list](https://coredns.io/plugins/)
- **Split DNS with a custom nameserver:** [Tailscale DNS documentation](https://tailscale.com/kb/1054/dns)

## Related guides

- [Caddy Reverse Proxy Cheat Sheet](caddy-reverse-proxy-cheat-sheet.md)
- [Tailscale Mesh Networking Cheat Sheet](tailscale-mesh-cli-cheat-sheet.md)
- [AdGuard Home Management Cheat Sheet](adguard-home-management-cheat-sheet.md)
- [Podman Quadlets Cheat Sheet](../../containers/podman-quadlets-cheat-sheet.md)
