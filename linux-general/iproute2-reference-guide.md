## This document provides a concise quick-reference guide for essential `iproute2` commands used in Linux network administration. It covers practical syntax for managing interfaces, IP addresses, routing tables, and socket statistics, serving as a modern replacement for legacy `net-tools`

## 1. Network Interfaces (`ip link`)

_Replaces legacy `ifconfig` for interface management._

**List all network interfaces and their MAC addresses:**

```bash
`ip link show` / `ip l`
```

**Show status and details of a specific interface (`eth0`):**

```bash
ip link show dev eth0
```

**Bring the `eth0` interface up:**

```bash
ip link set eth0 up
```

**Bring the `eth0` interface down:**

```bash
ip link set eth0 down
```

**Change the MAC address of `eth0` (interface must be down first):**

```bash
ip link set eth0 address 00:11:22:33:44:55
```

## 2. IP Addresses (`ip addr`)

_Replaces legacy `ifconfig` for IP assignment._

**List all IP addresses across all interfaces:**

```bash
`ip addr show` / `ip a`
```

**Show a brief, one-line-per-interface status including IP and state:**

```bash
ip -br a
```

**Show IP addresses assigned specifically to `eth0`:**

```bash
ip addr show dev eth0
```

**Assign a static IPv4 address to `eth0`:**

```bash
ip addr add 192.168.1.10/24 dev eth0
```

**Assign a static IPv6 address to `eth0`:**

```bash
ip -6 addr add 2001:db8::1/64 dev eth0
```

**Remove a specific IP address from `eth0`:**

```bash
ip addr del 192.168.1.10/24 dev eth0
```

**Remove all IP addresses dynamically assigned or static on `eth0`:**

```bash
ip addr flush dev eth0
```

## 3. Routing Table (`ip route`)

_Replaces legacy `route` command._

**Display the kernel's IPv4 routing table:**

```bash
`ip route show` / `ip r`
```

**Display the kernel's IPv6 routing table:**

```bash
ip -6 route show
```

**Add a default gateway route:**

```bash
ip route add default via 192.168.1.1
```

**Add a static route to a specific subnet via a gateway:**

```bash
ip route add 10.0.0.0/24 via 192.168.1.1
```

**Delete a specific route from the table:**

```bash
ip route del 10.0.0.0/24
```

**Test and display the route the kernel will use to reach a specific IP:**

```bash
ip route get 8.8.8.8
```

## 4. Neighbor / ARP Table (`ip neigh`)

_Replaces legacy `arp` command._

**Display the neighbor/ARP cache table:**

```bash
`ip neigh show` / `ip n`
```

**Clear the entire ARP cache for a specific interface:**

```bash
ip neigh flush dev eth0
```

**Add a static, permanent ARP entry:**

```bash
ip neigh add 192.168.1.100 lladdr 00:11:22:33:44:55 dev eth0
```

**Delete a specific ARP entry:**

```bash
ip neigh del 192.168.1.100 dev eth0
```

## 5. Socket Statistics (`ss`)

_Replaces legacy `netstat` for connection monitoring._

**Show all listening TCP and UDP ports (in numeric format):**

```bash
ss -tuln
```

**List all listening processes, extended statistics, and associated PIDs:**

```bash
ss -anpe
```

**Display a summary of statistics for all network sockets:**

```bash
ss -s
```

---

**Sources & Verification:**

- Official `iproute2` utility suite documentation (maintained by Stephen Hemminger and the Linux Foundation).
- Command syntax and flag definitions verified against Daniil Baturin's task-centered `iproute2` guide.
- Legacy `net-tools` mappings and practical CLI examples verified via community network administration reference sheets.
