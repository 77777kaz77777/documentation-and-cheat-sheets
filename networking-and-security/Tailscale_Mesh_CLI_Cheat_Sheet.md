## Terminal commands for setting up and managing Tailscale mesh networks

# Tailscale Mesh Networking Cheat Sheet

## Connectivity & State Management

| Command | Description |
| :--- | :--- |
| `tailscale up` | Connect device to the Tailnet using default or saved parameters. |
| `tailscale up --auth-key=<key>` | Authenticate non-interactively using a pre-authenticated key. |
| `tailscale up --reset` | Reset all flags back to default before applying new parameters. |
| `tailscale set <flags>` | Update configuration flags (e.g., `--accept-routes`) without re-authenticating. |
| `tailscale down` | Disconnect from the Tailnet while preserving authentication state. |
| `tailscale logout` | Disconnect and revoke the local device's node authentication key. |
| `tailscale status` | List active Tailnet peers, IP addresses, OS, and connection modes (direct vs. DERP). |
| `tailscale status --json` | Output full peer and netmap data in JSON format for scripting. |
| `tailscale ip -4` | Display the device’s IPv4 address on the Tailnet (`100.x.y.z`). |
| `tailscale ip -6` | Display the device’s IPv6 address on the Tailnet (`fd7a:115c:a1e0::/48`). |

## Exit Node Configuration

| Command | Description |
| :--- | :--- |
| `tailscale up --advertise-exit-node` | Offer this device as an exit node for internet traffic routing across the Tailnet. |
| `tailscale set --exit-node=<ip_or_name>` | Route all outbound internet traffic through a specified exit node. |
| `tailscale set --exit-node-allow-lan-access` | Maintain local LAN access (e.g., local printers/subnets) while using an exit node. |
| `tailscale set --exit-node=` | Clear the active exit node and revert to default local internet routing. |

> **Linux IP Forwarding Requirement:** Exit nodes and subnet routers require IP forwarding enabled on the host:  
> `echo 'net.ipv4.ip_forward = 1' | sudo tee -a /etc/sysctl.d/99-tailscale.conf`  
> `echo 'net.ipv6.conf.all.forwarding = 1' | sudo tee -a /etc/sysctl.d/99-tailscale.conf`  
> `sudo sysctl -p /etc/sysctl.d/99-tailscale.conf`

## Subnet Routing

| Command | Description |
| :--- | :--- |
| `tailscale up --advertise-routes=<subnets>` | Expose physical LAN subnets (e.g., `192.168.1.0/24,10.0.0.0/16`) to the Tailnet. |
| `tailscale set --accept-routes=true` | Accept and route traffic to subnets advertised by other Tailnet peers (default `true` on iOS/macOS/Windows, `false` on Linux). |
| `tailscale set --accept-routes=false` | Ignore subnets advertised by other peers and use local routing tables. |
| `tailscale up --snat-subnet-routes=false` | Disable Source NAT (SNAT) for subnet routing (requires custom LAN routing setup). |

## Tailscale SSH

| Command | Description |
| :--- | :--- |
| `tailscale up --ssh` | Enable the embedded Tailscale SSH server on the device, managed via ACLs. |
| `tailscale ssh <user>@<peer_ip_or_name>` | Authenticate and connect to a peer via Tailscale SSH without managing SSH keys. |

## Web Exposure & Proxying (Serve & Funnel)

| Command | Description |
| :--- | :--- |
| `tailscale serve http://127.0.0.1:<port>` | Proxy local service to the private Tailnet over HTTPS using automatically provisioned SSL certs. |
| `tailscale serve status` | Display active Tailscale Serve proxy configurations and endpoints. |
| `tailscale serve reset` | Clear all active local Tailscale Serve proxy configurations. |
| `tailscale funnel <port>` | Expose a local Web server/port publicly to the open internet via Tailscale relay infrastructure. |
| `tailscale funnel status` | View the status and active URLs of publicly funneled services. |

## File Transfer (Taildrop)

| Command | Description |
| :--- | :--- |
| `tailscale file cp <file> <peer_ip_or_name>:` | Send a file directly to a peer on the Tailnet via Taildrop. |
| `tailscale file get <target_directory>` | Receive and unpack pending incoming files sent via Taildrop into a specific folder. |

## Diagnostics & Troubleshooting

| Command | Description |
| :--- | :--- |
| `tailscale netcheck` | Perform diagnostics for STUN, UDP blocking, NAT mapping, and locate the nearest DERP server. |
| `tailscale ping <peer_ip_or_name>` | Diagnose latency and verify whether the connection to a peer is direct (`magicsock`) or relayed (`DERP`). |
| `tailscale cert <node_name.tailnet.ts.net>` | Fetch an official Let's Encrypt TLS certificate and private key for the local node. |
| `tailscale bugreport` | Generate a unique diagnostic log ID to attach to support tickets or GitHub issues. |
| `sudo systemctl status tailscaled` | Check the status of the underlying Tailscale daemon service on systemd-based Linux systems. |
