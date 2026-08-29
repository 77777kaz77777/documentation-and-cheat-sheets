## Terminal commands for setting up and managing Tailscale mesh networks. 

# Tailscale Mesh Networking Cheat Sheet

## Connectivity & Status

| Command | Description |
| :--- | :--- |
| `tailscale up` | Connect the device to the Tailscale network. |
| `tailscale down` | Disconnect the device from the Tailscale network. |
| `tailscale status` | List all peers in your Tailnet, showing IP addresses and connection status. |
| `tailscale netcheck` | Run diagnostics on NAT traversal, UDP mapping, and display the nearest DERP relay. |
| `tailscale ping <peer_ip_or_name>` | Ping a peer directly over the Tailnet to test latency and direct connection success. |

## Exit Node Configuration

| Command | Description |
| :--- | :--- |
| `tailscale up --advertise-exit-node` | Configure the current device to act as an exit node for the Tailnet. |
| `tailscale up --exit-node=<ip_or_name>` | Route all local internet traffic through a specific exit node on your Tailnet. |
| `tailscale up --exit-node=<ip> --exit-node-allow-lan-access` | Route traffic through an exit node while retaining access to the local LAN. |
| `tailscale up --exit-node=` | Disable the active exit node and revert to normal internet routing. |

## Subnet Routing

| Command | Description |
| :--- | :--- |
| `tailscale up --advertise-routes=<subnet>` | Expose a local physical subnet (e.g., `192.168.8.0/24`) to the Tailnet. |
| `tailscale up --accept-routes` | Allow the local device to accept and route traffic to subnets advertised by other peers. |
