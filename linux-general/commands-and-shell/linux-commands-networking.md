# Linux Commands: Networking

Interfaces, connections, transfers and diagnostics, plus mail and user messaging.

Part of the [Linux commands cheat sheet](linux-commands-cheat-sheet-tables.md).

## Networking Commands

**`arp` — Manipulate the system ARP cache:**

```bash
arp -a
```

**`curl` — Transfer a URL:**

```bash
curl -O http://example.com/file.zip
```

**`host` — DNS lookup utility:**

```bash
host example.com
```

**`hostid` — Print the numeric identifier for the current host:**

```bash
hostid
```

**`hostname` — Show or set the system's host name:**

```bash
hostname
```

**`hostnamectl` — Control the system hostname:**

```bash
hostnamectl set-hostname server1
```

**`ifconfig` — Configure a network interface (legacy; use `ip`):**

```bash
ip addr show eth0      # modern replacement
ifconfig eth0          # legacy net-tools, often not installed
```

**`iftop` — Display bandwidth usage on an interface:**

```bash
iftop -i eth0
```

**`ifup` — Bring a network interface up:**

```bash
ifup eth0
```

**`ip` — Show / manipulate routing, network devices, interfaces and tunnels:**

```bash
ip addr show
```

**`ipcrm` — Remove a message queue, semaphore set, or shared memory id:**

```bash
ipcrm -m 1234
```

**`ipcs` — Provide information on ipc facilities:**

```bash
ipcs -m
```

**`iptables` — Administration tool for IPv4 packet filtering and NAT:**

```bash
iptables -L
```

**`iptables-save` — Dump iptables rules to stdout:**

```bash
iptables-save > /etc/iptables/rules.v4
```

**`iwconfig` — Configure a wireless network interface:**

```bash
iwconfig wlan0
```

**``nc`(`netcat`)` — Arbitrary TCP and UDP connections and listens:**

```bash
nc -lvp 8080
```

**`netstat` — Print network connections, routing tables, interface statistics, etc (legacy; use `ss`):**

```bash
ss -tuln               # modern replacement
netstat -tuln          # legacy net-tools, often not installed
```

**`nmcli` — Command-line tool for controlling NetworkManager:**

```bash
nmcli connection show
```

**`nslookup` — Query Internet name servers interactively:**

```bash
nslookup example.com
```

**`ping` — Send ICMP ECHO_REQUEST to network hosts:**

```bash
ping 8.8.8.8
```

**`rcp` — Remote file copy:**

```bash
rcp file.txt host:/tmp/
```

**`route` — Show / manipulate the IP routing table:**

```bash
route -n
```

**`rsync` — Fast, versatile, remote (and local) file-copying tool:**

```bash
rsync -avz /local/dir/ user@remote:/remote/dir/
```

**`scp` — Secure copy:**

```bash
scp file.txt user@remote:/tmp/
```

**`ssh` — OpenSSH SSH client:**

```bash
ssh user@remote
```

**`tracepath` — Traces path to a network host discovering MTU:**

```bash
tracepath 8.8.8.8
```

**`traceroute` — Print the route packets trace to network host:**

```bash
traceroute example.com
```

**`vnstat` — Console-based network traffic monitor:**

```bash
vnstat -i eth0
```

**`wget` — The non-interactive network downloader:**

```bash
wget http://example.com/file.iso
```

## Mail and User Communication Commands

**`biff` — Be notified if mail arrives and who it is from:**

```bash
biff y
```

**`mailq` — Print the mail queue:**

```bash
mailq
```

**`write` — Send a message to another user:**

```bash
write username
```

**`wall` — Send a message to everybody's terminal:**

```bash
wall "System will go down in 10 minutes"
```
