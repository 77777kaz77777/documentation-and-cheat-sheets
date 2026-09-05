# Networking Concepts and Explanations Cheatsheet

| Category | Concept | Explanation / Details |
| :--- | :--- | :--- |
| **OSI Model** | **Layer 1: Physical** | Handles the physical transmission of raw bit streams over a physical medium (e.g., Ethernet cables, fiber optics, radio waves). Hardware includes hubs, repeaters, and cables. |
| **OSI Model** | **Layer 2: Data Link** | Node-to-node data transfer. Detects and possibly corrects errors that may occur in the Physical layer. Defines MAC addresses. Hardware includes switches and bridges. |
| **OSI Model** | **Layer 3: Network** | Handles routing of data paths between different networks. Uses logical addressing (IP addresses) to route packets. Hardware includes routers. |
| **OSI Model** | **Layer 4: Transport** | Provides reliable or unreliable delivery of data between hosts (e.g., TCP for reliable, UDP for unreliable). Manages ports, segmentation, and error checking. |
| **OSI Model** | **Layer 5: Session** | Establishes, manages, and terminates connections (sessions) between local and remote applications. |
| **OSI Model** | **Layer 6: Presentation** | Translates, encrypts, and compresses data. Ensures that data transferred from the application layer of one system can be read by the application layer of another. |
| **OSI Model** | **Layer 7: Application** | Network applications and their protocols. Provides network services directly to the user's application (e.g., HTTP, FTP, SMTP). |
| **Protocols** | **TCP (Transmission Control Protocol)** | Connection-oriented protocol that ensures guaranteed, ordered, and error-checked delivery of a stream of packets. |
| **Protocols** | **UDP (User Datagram Protocol)** | Connectionless protocol that sends packets without guaranteeing delivery, order, or error checking. Faster but less reliable than TCP (used in streaming, gaming). |
| **Protocols** | **IP (Internet Protocol)** | The principal communications protocol for relaying datagrams across network boundaries. Responsible for routing packets based on IP addresses. |
| **Protocols** | **HTTP / HTTPS** | Hypertext Transfer Protocol (Secure). Foundation of data communication for the World Wide Web. HTTPS encrypts the data using TLS/SSL. |
| **Protocols** | **DNS (Domain Name System)** | Translates human-readable domain names (e.g., <www.example.com>) into machine-readable IP addresses (e.g., 192.0.2.1). |
| **Protocols** | **DHCP (Dynamic Host Configuration Protocol)** | Automatically assigns IP addresses and other network configuration parameters to devices on a network so they can communicate. |
| **Protocols** | **FTP / SFTP** | File Transfer Protocol (Secure). Used for the transfer of computer files between a client and server. SFTP adds a secure shell (SSH) encryption layer. |
| **Protocols** | **SSH (Secure Shell)** | Cryptographic network protocol for operating network services securely over an unsecured network. Typically used for remote command-line login. |
| **Addressing** | **IPv4** | 32-bit numeric address (e.g., 192.168.1.1) used to identify devices on a network. Limited to approximately 4.3 billion addresses. |
| **Addressing** | **IPv6** | 128-bit alphanumeric address (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334) designed to replace IPv4 due to address exhaustion. |
| **Addressing** | **MAC Address** | Media Access Control address. A unique identifier assigned to a network interface controller (NIC) for communications at the data link layer (Layer 2). |
| **Addressing** | **Subnetting** | The practice of dividing a network into two or more smaller networks (subnets) to improve routing efficiency and security. |
| **Addressing** | **NAT (Network Address Translation)** | Modifies network address information in packet headers while in transit across a traffic routing device, allowing multiple devices on a local network to share a single public IP. |
| **Hardware** | **Router** | Forwards data packets between different computer networks. Operates at Layer 3 of the OSI model. |
| **Hardware** | **Switch** | Connects devices within a single local area network (LAN) and uses MAC addresses to forward data to the correct destination. Operates at Layer 2. |
| **Hardware** | **Hub** | A basic network device that connects multiple computers but broadcasts data to all connected devices rather than routing it to a specific destination. Mostly obsolete. |
| **Hardware** | **Firewall** | A network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. |
| **Security** | **VPN (Virtual Private Network)** | Extends a private network across a public network, enabling users to send and receive data across shared networks as if their computing devices were directly connected to the private network. |
| **Security** | **DMZ (Demilitarized Zone)** | A physical or logical subnetwork that contains and exposes an organization's external-facing services to an untrusted, usually larger, network such as the Internet. |
| **Security** | **TLS / SSL** | Transport Layer Security / Secure Sockets Layer. Cryptographic protocols designed to provide communications security over a computer network (e.g., securing HTTPS). |
