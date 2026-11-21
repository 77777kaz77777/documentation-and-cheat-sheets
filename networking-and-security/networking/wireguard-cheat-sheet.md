# WireGuard Cheat Sheet

Quick-reference guide for setting up and troubleshooting WireGuard VPN tunnels on Linux.

**WireGuard** is a fast, modern VPN built into the Linux kernel. Each machine (a **peer**) has a key pair; peers list each other's public keys and the IP ranges they're allowed to send (`AllowedIPs`). There is no server software in the usual sense: a "server" is just a peer with a fixed address that others connect to.

---

## 1. Install

```bash
# RHEL / Fedora / Rocky (kernel module is built in; this adds the tools)
sudo dnf install wireguard-tools

# Debian / Ubuntu
sudo apt install wireguard-tools

# Arch Linux
sudo pacman -S wireguard-tools
```

---

## 2. Generate Keys

```bash
# Private and public key pair (run on each peer)
umask 077 && wg genkey | tee privatekey | wg pubkey > publickey

# Optional pre-shared key for an extra layer of symmetric encryption
wg genpsk > presharedkey

cat publickey
```

Never share or commit the **private** key. Only the public key goes to the other side.

---

## 3. Server Config (`/etc/wireguard/wg0.conf`)

```ini
[Interface]
Address = 10.8.0.1/24
ListenPort = 51820
PrivateKey = SERVER_PRIVATE_KEY

# Laptop
[Peer]
PublicKey = LAPTOP_PUBLIC_KEY
AllowedIPs = 10.8.0.2/32

# Phone
[Peer]
PublicKey = PHONE_PUBLIC_KEY
AllowedIPs = 10.8.0.3/32
```

```bash
sudo chmod 600 /etc/wireguard/wg0.conf
```

On the server, each peer's `AllowedIPs` is **that peer's tunnel address** (`/32`).

---

## 4. Client Config

```ini
[Interface]
Address = 10.8.0.2/24
PrivateKey = LAPTOP_PRIVATE_KEY
DNS = 10.8.0.1

[Peer]
PublicKey = SERVER_PUBLIC_KEY
Endpoint = vpn.example.com:51820
AllowedIPs = 10.8.0.0/24, 192.168.1.0/24
PersistentKeepalive = 25
```

| `AllowedIPs` on the client | Result |
| --- | --- |
| `10.8.0.0/24` | Only VPN peers go through the tunnel (split tunnel) |
| `10.8.0.0/24, 192.168.1.0/24` | VPN peers plus the server's home LAN |
| `0.0.0.0/0, ::/0` | All traffic through the VPN (full tunnel) |

`PersistentKeepalive = 25` keeps the connection alive through NAT; use it on peers behind a home router or mobile network.

---

## 5. Bring Tunnels Up & Down

```bash
# Start and stop
sudo wg-quick up wg0
sudo wg-quick down wg0

# Start on boot
sudo systemctl enable --now wg-quick@wg0

# Status: peers, last handshake, data transferred
sudo wg show
sudo wg show wg0 latest-handshakes
```

A recent **latest handshake** (under 2 minutes) means the tunnel works. No handshake means the peers can't reach each other or the keys don't match.

### Reload Peers Without Dropping the Tunnel

```bash
sudo bash -c 'wg syncconf wg0 <(wg-quick strip wg0)'
```

### Add a Peer on the Fly

```bash
sudo wg set wg0 peer NEW_PUBLIC_KEY allowed-ips 10.8.0.4/32
```

Changes made with `wg set` are lost on restart unless you also add them to `wg0.conf`.

---

## 6. Server Networking (Routing to the LAN or Internet)

### Enable IP Forwarding

```bash
echo -e "net.ipv4.ip_forward = 1\nnet.ipv6.conf.all.forwarding = 1" | sudo tee /etc/sysctl.d/99-wireguard.conf && sudo sysctl --system
```

### firewalld

```bash
sudo firewall-cmd --permanent --add-port=51820/udp
sudo firewall-cmd --permanent --zone=trusted --add-interface=wg0
sudo firewall-cmd --permanent --add-masquerade
sudo firewall-cmd --reload
```

### nftables / iptables (Debian, Arch)

Add to the `[Interface]` section, replacing `eth0` with the internet-facing interface:

```ini
PostUp = iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE
```

Forward UDP port `51820` on your router to the server.

---

## 7. NetworkManager

```bash
# Import a wg-quick config as a NetworkManager connection
sudo nmcli connection import type wireguard file /etc/wireguard/wg0.conf

# Connect and disconnect
nmcli connection up wg0
nmcli connection down wg0

# Don't start automatically
nmcli connection modify wg0 connection.autoconnect no
```

---

## 8. Phone Setup (QR Code)

```bash
sudo dnf install qrencode    # or apt / pacman
qrencode -t ansiutf8 < phone.conf
```

Scan it in the official WireGuard app. Delete `phone.conf` afterwards; it contains the phone's private key.

---

## 9. Troubleshooting

```bash
# Is the interface up with the right address?
ip addr show wg0

# Which route does traffic to a peer use?
ip route get 10.8.0.1

# Is the server listening?
sudo ss -lunp | grep 51820

# Kernel debug messages (temporary)
echo "module wireguard +p" | sudo tee /sys/kernel/debug/dynamic_debug/control
sudo dmesg -wT | grep wireguard
```

| Problem | Likely cause |
| --- | --- |
| No handshake at all | Wrong endpoint, UDP port blocked or not forwarded, or mismatched keys |
| Handshake OK, can't ping the server | Client `Address` / server `AllowedIPs` mismatch |
| Can reach the server, not the LAN | IP forwarding off, missing masquerade, or LAN not in client `AllowedIPs` |
| Full tunnel has no internet | Missing masquerade/NAT on the server, or no `DNS =` on the client |
| Connection drops after idle | Add `PersistentKeepalive = 25` |
| `RTNETLINK answers: File exists` | An address or route already exists; `wg-quick down wg0` first |

---

## 10. WireGuard vs. Tailscale

Tailscale uses WireGuard underneath but handles keys, NAT traversal, and DNS for you. Use plain WireGuard for a simple fixed tunnel you fully control; use Tailscale when devices move between networks or sit behind NAT you can't configure.

---

## Quick Reference

```bash
wg genkey | tee privatekey | wg pubkey > publickey   # key pair
sudo wg-quick up wg0                                 # start tunnel
sudo wg-quick down wg0                               # stop tunnel
sudo systemctl enable --now wg-quick@wg0             # start on boot
sudo wg show                                         # status and handshakes
sudo bash -c 'wg syncconf wg0 <(wg-quick strip wg0)' # reload peers
qrencode -t ansiutf8 < phone.conf                    # QR for mobile
```

---

## Sources & Verification

- **Commands and config format:** [wg(8)](https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8) and [wg-quick(8)](https://git.zx2c4.com/wireguard-tools/about/src/man/wg-quick.8)
- **Protocol overview:** [WireGuard quick start](https://www.wireguard.com/quickstart/)

## Related guides

- [Tailscale Mesh Networking Cheat Sheet](tailscale-mesh-cli-cheat-sheet.md)
- [nmcli Cheat Sheet](nmcli-cheat-sheet.md)
- [Firewalld Cheat Sheet](../security/fedora-firewall-cheat-sheet.md)
- [SSH and sshd Hardening Cheat Sheet](../security/ssh-hardening-cheat-sheet.md)
