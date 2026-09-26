# Networking Concepts and Explanations Cheatsheet

# Comprehensive Networking Concepts & Explanations

## 1. The OSI Model & Protocol Data Units (PDUs)

The Open Systems Interconnection (OSI) model conceptualizes how networks operate. The PDU is the form data takes at that specific layer.

| Layer | Name | PDU | Hardware / Protocols | Description |
| :--- | :--- | :--- | :--- | :--- |
| **7** | **Application** | Data | HTTP/S, DNS, SSH, FTP, DHCP, SMTP | Network services directly interfacing with user applications. |
| **6** | **Presentation** | Data | TLS, SSL, JPEG, ASCII, MPEG | Translates, encrypts, and compresses data into a readable format for the application layer. |
| **5** | **Session** | Data | NetBIOS, RPC, SOCKS | Establishes, maintains, and terminates connections (sessions) between local and remote applications. |
| **4** | **Transport** | Segment (TCP) / Datagram (UDP) | TCP, UDP, Ports (1-65535) | Ensures reliable (TCP) or unreliable (UDP) delivery of data. Handles segmentation and port assignments. |
| **3** | **Network** | Packet | IP (IPv4/IPv6), ICMP, IPsec, Routers, L3 Switches | Handles logical addressing (IPs) and routing data paths between different networks. |
| **2** | **Data Link** | Frame | MAC Addresses, ARP, Switches, VLANs (802.1Q) | Node-to-node transfer within the same network. Uses physical MAC addresses. Detects L1 errors. |
| **1** | **Physical** | Bit | Ethernet (802.3), Wi-Fi (802.11), Cables, Hubs | Physical transmission of raw binary streams over a medium (copper, fiber, radio). |

## 2. Core Network Protocols

| Protocol | Layer | Port(s) | Description |
| :--- | :--- | :--- | :--- |
| **TCP** | 4 | N/A | Transmission Control Protocol. Connection-oriented. Uses a 3-way handshake (`SYN` -> `SYN-ACK` -> `ACK`) to guarantee ordered, error-checked delivery. |
| **UDP** | 4 | N/A | User Datagram Protocol. Connectionless. "Fire and forget." Faster but no delivery guarantee (used for DNS, VoIP, streaming). |
| **IP** | 3 | N/A | Internet Protocol. The core routing protocol of the internet. |
| **ICMP** | 3 | N/A | Internet Control Message Protocol. Used for diagnostics and error reporting (e.g., `ping`, `traceroute`). Does not use ports. |
| **ARP** | 2/3 | N/A | Address Resolution Protocol. Broadcasts on a local network to map a known logical Layer 3 IP address to an unknown physical Layer 2 MAC address. |
| **DNS** | 7 | 53 (UDP/TCP) | Domain Name System. Resolves human-readable hostnames to IP addresses. UDP for standard queries, TCP for zone transfers. |
| **DHCP** | 7 | 67, 68 (UDP) | Dynamic Host Configuration Protocol. Leases IP addresses, subnet masks, gateways, and DNS servers to clients dynamically. |
| **HTTP(S)** | 7 | 80, 443 (TCP) | Hypertext Transfer Protocol (Secure). HTTPS uses TLS encryption for secure web communication. |
| **SSH** | 7 | 22 (TCP) | Secure Shell. Encrypted remote command-line login and secure data tunneling. |
| **BGP/OSPF** | 7/3 | 179 / N/A | Routing protocols used by core internet routers to determine the shortest and most efficient paths for packets. |

## 3. Addressing & Subnetting

| Concept | Explanation |
| :--- | :--- |
| **MAC Address** | 48-bit hardware address burned into the Network Interface Card (NIC) by the manufacturer (e.g., `00:1A:2B:3C:4D:5E`). First 24 bits are the vendor OUI. |
| **IPv4** | 32-bit logical address. Exhausted globally. Consists of 4 octets (e.g., `192.168.1.100`). |
| **IPv6** | 128-bit logical address (e.g., `2001:db8::ff00:42:8329`). Features built-in IPsec, no need for NAT, and massive address space. |
| **RFC 1918 (Private IPs)** | Non-routable internet IPs reserved for local networks: <br>• `10.0.0.0/8` (Large enterprises)<br>• `172.16.0.0/12` (Medium networks)<br>• `192.168.0.0/16` (Home networks) |
| **Subnet Mask / CIDR** | Defines which part of the IP is the network vs. the host. <br>• `/24` = `255.255.255.0` (254 usable hosts)<br>• `/16` = `255.255.0.0` (65,534 usable hosts) |
| **NAT / PAT** | Network / Port Address Translation. Translates multiple private IP addresses on a LAN to a single public IP address at the router to access the internet. |

## 4. Hardware & Infrastructure

| Device/Concept | Description |
| :--- | :--- |
| **Switch (L2)** | Connects devices within a single LAN. Forwards traffic intelligently based on MAC address tables. |
| **Router (L3)** | Connects multiple disparate networks (e.g., your LAN to your ISP's network). Forwards traffic based on IP routing tables. |
| **Load Balancer (L4/L7)** | Distributes incoming network traffic across multiple backend servers to ensure reliability and performance (e.g., HAProxy, Nginx). |
| **Stateful Firewall** | Tracks the state of active connections. If traffic is allowed out, the return traffic is automatically allowed back in. |
| **VLAN (Virtual LAN)** | A logical grouping of network devices on the same physical switch into separate broadcast domains for security and traffic reduction (IEEE 802.1Q). |
| **DMZ** | Demilitarized Zone. An isolated subnet exposing externally facing services (web servers, mail servers) to the internet, separated from the internal secure LAN. |

---
**Sources & Verification:**

* *RFC 1918 Address Allocation for Private Internets:* <https://datatracker.ietf.org/doc/html/rfc1918>
* *RFC 793 Transmission Control Protocol:* <https://datatracker.ietf.org/doc/html/rfc793>
* *CompTIA Network+ / Cisco CCNA Official Study Guides*
* *Red Hat Enterprise Linux (RHEL) Networking Guide:* <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_networking/>
