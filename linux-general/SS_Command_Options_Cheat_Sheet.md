# How to inspect network sockets and connections using the ss command

The `ss` command is a utility used to investigate socket connections on Linux systems.

---

## ⚙️ General Options

| Option | Long Option | Description |
| :--- | :--- | :--- |
| `-h` | `--help` | Displays the help message. |
| `-V` | `--version` | Outputs version information of the `ss` command. |

---

## 📊 Socket Display Options

| Option | Long Option | Description |
| :--- | :--- | :--- |
| `-n` | `--numeric` | Do not resolve service names; display numerical addresses. |
| `-r` | `--resolve` | Resolve host names to their corresponding IP addresses. |
| `-a` | `--all` | Display all sockets, including listening and non-listening. |
| `-l` | `--listening` | Display only listening sockets. |
| `-o` | `--options` | Show timer information for sockets. |
| `-e` | `--extended` | Show detailed socket information. |
| `-m` | `--memory` | Display socket memory usage statistics. |
| `-p` | `--processes` | Show the processes using the sockets. |
| `-T` | `--threads` | Display threads using the sockets. |
| `-i` | `--info` | Show internal TCP information. |
| | `--tipcinfo` | Show internal TIPC socket information. |
| `-s` | `--summary` | Display a summary of socket usage. |
| | `--tos` | Show Type of Service (ToS) and priority information. |
| | `--cgroup` | Display cgroup information related to sockets. |
| `-b` | `--bpf` | Show BPF filter socket information. |
| `-E` | `--events` | Continually display sockets as they are destroyed. |
| `-Z` | `--context` | Display task SELinux security contexts. |
| `-z` | `--contexts` | Display task and socket SELinux security contexts. |
| `-N` | `--net` | Switch to the specified network namespace name. |

---

## 🌐 Protocol-Specific Options

| Option | Long Option | Description |
| :--- | :--- | :--- |
| `-4` | `--ipv4` | Display only IPv4 sockets. |
| `-6` | `--ipv6` | Display only IPv6 sockets. |
| `-0` | `--packet` | Display PACKET sockets. |
| `-t` | `--tcp` | Display only TCP sockets. |
| `-M` | `--mptcp` | Display only MPTCP (Multipath TCP) sockets. |
| `-S` | `--sctp` | Display only SCTP (Stream Control Transmission Protocol) sockets. |
| `-u` | `--udp` | Display only UDP sockets. |
| `-d` | `--dccp` | Display only DCCP (Datagram Congestion Control Protocol) sockets. |
| `-w` | `--raw` | Display only RAW sockets. |
| `-x` | `--unix` | Display only Unix domain sockets. |
| | `--tipc` | Display only TIPC (Transparent Inter-Process Communication) sockets. |
| | `--vsock` | Display only vSockets. |
| | `--xdp` | Display only XDP (eXpress Data Path) sockets. |

---

## 🔍 Family and Filtering Options

| Option | Long Option | Description |
| :--- | :--- | :--- |
| `-f FAMILY` | `--family=FAMILY` | Display sockets of specified type (`inet`, `inet6`, `link`, `unix`, `netlink`, `vsock`, `tipc`, `xdp`, `help`). |
| `-K` | `--kill` | Forcibly close sockets and display what was closed. |
| `-H` | `--no-header` | Suppress the header line in the output. |
| `-O` | `--oneline` | Print socket data on a single line. |
| | `--inet-sockopt` | Show various inet socket options. |
| `-A QUERY` | `--query=QUERY`, `--socket=QUERY` | Query specific socket types (`all`, `inet`, `tcp`, `mptcp`, `udp`, `raw`, `unix`, `unix_dgram`, `unix_stream`, `unix_seqpacket`, `packet`, `packet_raw`, `packet_dgram`, `netlink`, `dccp`, `sctp`, `vsock_stream`, `vsock_dgram`, `tipc`, `xdp`). |
| `-D FILE` | `--diag=FILE` | Dump raw information about TCP sockets to the specified `FILE`. |
| `-F FILE` | `--filter=FILE` | Read filter information from the specified `FILE` (state filters & expressions). |

---

## 🏷️ State Filters & TCP States

### State Filters

- **`all`**
- **`connected`** (`established`, `syn-sent`, `syn-recv`, `fin-wait-1`, `fin-wait-2`, `time-wait`, `close-wait`, `last-ack`, `closing`)
- **`synchronized`** (`established`, `syn-recv`, `fin-wait-1`, `fin-wait-2`, `time-wait`, `close-wait`, `last-ack`, `closing`)
- **`bucket`** (`syn-recv`, `time-wait`)
- **`big`** (`established`, `syn-sent`, `fin-wait-1`, `fin-wait-2`, `closed`, `close-wait`, `last-ack`, `listening`, `closing`)

### Individual TCP States

`established`, `syn-sent`, `syn-recv`, `fin-wait-1`, `fin-wait-2`, `time-wait`, `closed`, `close-wait`, `last-ack`, `listening`, `closing`
