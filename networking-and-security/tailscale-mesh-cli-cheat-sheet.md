## Terminal commands for setting up and managing Tailscale mesh networks

# Tailscale Mesh Networking Cheat Sheet

## Connectivity & State Management

**Connect device to the Tailnet using default or saved parameters:**

```bash
tailscale up
```

**Authenticate non-interactively using a pre-authenticated key:**

```bash
tailscale up --auth-key=<key>
```

**Reset all flags back to default before applying new parameters:**

```bash
tailscale up --reset
```

**Update configuration flags (e.g., `--accept-routes`) without re-authenticating:**

```bash
tailscale set <flags>
```

**Disconnect from the Tailnet while preserving authentication state:**

```bash
tailscale down
```

**Disconnect and revoke the local device's node authentication key:**

```bash
tailscale logout
```

**List active Tailnet peers, IP addresses, OS, and connection modes (direct vs. DERP):**

```bash
tailscale status
```

**Output full peer and netmap data in JSON format for scripting:**

```bash
tailscale status --json
```

**Display the device’s IPv4 address on the Tailnet (`100.x.y.z`):**

```bash
tailscale ip -4
```

**Display the device’s IPv6 address on the Tailnet (`fd7a:115c:a1e0::/48`):**

```bash
tailscale ip -6
```

## Exit Node Configuration

**Offer this device as an exit node for internet traffic routing across the Tailnet:**

```bash
tailscale up --advertise-exit-node
```

**Route all outbound internet traffic through a specified exit node:**

```bash
tailscale set --exit-node=<ip_or_name>
```

**Maintain local LAN access (e.g., local printers/subnets) while using an exit node:**

```bash
tailscale set --exit-node-allow-lan-access
```

**Clear the active exit node and revert to default local internet routing:**

```bash
tailscale set --exit-node=
```

> **Linux IP Forwarding Requirement:** Exit nodes and subnet routers require IP forwarding enabled on the host:  
> `echo 'net.ipv4.ip_forward = 1' | sudo tee -a /etc/sysctl.d/99-tailscale.conf`  
> `echo 'net.ipv6.conf.all.forwarding = 1' | sudo tee -a /etc/sysctl.d/99-tailscale.conf`  
> `sudo sysctl -p /etc/sysctl.d/99-tailscale.conf`

## Subnet Routing

**Expose physical LAN subnets (e.g., `192.168.1.0/24,10.0.0.0/16`) to the Tailnet:**

```bash
tailscale up --advertise-routes=<subnets>
```

**Accept and route traffic to subnets advertised by other Tailnet peers (default `true` on iOS/macOS/Windows, `false` on Linux):**

```bash
tailscale set --accept-routes=true
```

**Ignore subnets advertised by other peers and use local routing tables:**

```bash
tailscale set --accept-routes=false
```

**Disable Source NAT (SNAT) for subnet routing (requires custom LAN routing setup):**

```bash
tailscale up --snat-subnet-routes=false
```

## Tailscale SSH

**Enable the embedded Tailscale SSH server on the device, managed via ACLs:**

```bash
tailscale up --ssh
```

**Authenticate and connect to a peer via Tailscale SSH without managing SSH keys:**

```bash
tailscale ssh <user>@<peer_ip_or_name>
```

## Web Exposure & Proxying (Serve & Funnel)

**Proxy local service to the private Tailnet over HTTPS using automatically provisioned SSL certs:**

```bash
tailscale serve http://127.0.0.1:<port>
```

**Display active Tailscale Serve proxy configurations and endpoints:**

```bash
tailscale serve status
```

**Clear all active local Tailscale Serve proxy configurations:**

```bash
tailscale serve reset
```

**Expose a local Web server/port publicly to the open internet via Tailscale relay infrastructure:**

```bash
tailscale funnel <port>
```

**View the status and active URLs of publicly funneled services:**

```bash
tailscale funnel status
```

## File Transfer (Taildrop)

**Send a file directly to a peer on the Tailnet via Taildrop:**

```bash
tailscale file cp <file> <peer_ip_or_name>:
```

**Receive and unpack pending incoming files sent via Taildrop into a specific folder:**

```bash
tailscale file get <target_directory>
```

## Diagnostics & Troubleshooting

**Perform diagnostics for STUN, UDP blocking, NAT mapping, and locate the nearest DERP server:**

```bash
tailscale netcheck
```

**Diagnose latency and verify whether the connection to a peer is direct (`magicsock`) or relayed (`DERP`):**

```bash
tailscale ping <peer_ip_or_name>
```

**Fetch an official Let's Encrypt TLS certificate and private key for the local node:**

```bash
tailscale cert <node_name.tailnet.ts.net>
```

**Generate a unique diagnostic log ID to attach to support tickets or GitHub issues:**

```bash
tailscale bugreport
```

**Check the status of the underlying Tailscale daemon service on systemd-based Linux systems:**

```bash
sudo systemctl status tailscaled
```
