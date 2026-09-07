
## This document provides a concise quick-reference guide for essential `iproute2` commands used in Linux network administration. It covers practical syntax for managing interfaces, IP addresses, routing tables, and socket statistics, serving as a modern replacement for legacy `net-tools`

## 1. Network Interfaces (`ip link`)

*Replaces legacy `ifconfig` for interface management.*

| Command | Description |
| --------- | ------------- |
| `ip link show` / `ip l` | List all network interfaces and their MAC addresses. |
| `ip link show dev eth0` | Show status and details of a specific interface (`eth0`). |
| `ip link set eth0 up` | Bring the `eth0` interface up. |
| `ip link set eth0 down` | Bring the `eth0` interface down. |
| `ip link set eth0 address 00:11:22:33:44:55` | Change the MAC address of `eth0` (interface must be down first). |

## 2. IP Addresses (`ip addr`)

*Replaces legacy `ifconfig` for IP assignment.*

| Command | Description |
| --------- | ------------- |
| `ip addr show` / `ip a` | List all IP addresses across all interfaces. |
| `ip -br a` | Show a brief, one-line-per-interface status including IP and state. |
| `ip addr show dev eth0` | Show IP addresses assigned specifically to `eth0`. |
| `ip addr add 192.168.1.10/24 dev eth0` | Assign a static IPv4 address to `eth0`. |
| `ip -6 addr add 2001:db8::1/64 dev eth0` | Assign a static IPv6 address to `eth0`. |
| `ip addr del 192.168.1.10/24 dev eth0` | Remove a specific IP address from `eth0`. |
| `ip addr flush dev eth0` | Remove all IP addresses dynamically assigned or static on `eth0`. |

## 3. Routing Table (`ip route`)

*Replaces legacy `route` command.*

| Command | Description |
| --------- | ------------- |
| `ip route show` / `ip r` | Display the kernel's IPv4 routing table. |
| `ip -6 route show` | Display the kernel's IPv6 routing table. |
| `ip route add default via 192.168.1.1` | Add a default gateway route. |
| `ip route add 10.0.0.0/24 via 192.168.1.1` | Add a static route to a specific subnet via a gateway. |
| `ip route del 10.0.0.0/24` | Delete a specific route from the table. |
| `ip route get 8.8.8.8` | Test and display the route the kernel will use to reach a specific IP. |

## 4. Neighbor / ARP Table (`ip neigh`)

*Replaces legacy `arp` command.*

| Command | Description |
| --------- | ------------- |
| `ip neigh show` / `ip n` | Display the neighbor/ARP cache table. |
| `ip neigh flush dev eth0` | Clear the entire ARP cache for a specific interface. |
| `ip neigh add 192.168.1.100 lladdr 00:11:22:33:44:55 dev eth0` | Add a static, permanent ARP entry. |
| `ip neigh del 192.168.1.100 dev eth0` | Delete a specific ARP entry. |

## 5. Socket Statistics (`ss`)

*Replaces legacy `netstat` for connection monitoring.*

| Command | Description |
| --------- | ------------- |
| `ss -tuln` | Show all listening TCP and UDP ports (in numeric format). |
| `ss -anpe` | List all listening processes, extended statistics, and associated PIDs. |
| `ss -s` | Display a summary of statistics for all network sockets. |

---

**Sources & Verification:**

- Official `iproute2` utility suite documentation (maintained by Stephen Hemminger and the Linux Foundation).
- Command syntax and flag definitions verified against Daniil Baturin's task-centered `iproute2` guide.
- Legacy `net-tools` mappings and practical CLI examples verified via community network administration reference sheets.
