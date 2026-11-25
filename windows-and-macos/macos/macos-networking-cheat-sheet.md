# macOS Networking Cheat Sheet

Quick-reference guide for interfaces, Wi-Fi, DNS, routing, VPNs, ports, the firewall, and sharing on macOS.

---

## 1. Interfaces & IP Addresses

**Map Hardware Ports to BSD Device Interfaces (`en0`, `en1`, `bridge0`):**

```bash
networksetup -listallhardwareports
```

**Check Local IPv4 Address (Wi-Fi is `en0` on MacBooks):**

```bash
ipconfig getifaddr en0
```

**View Complete Interface Summary (SSID, BSSID, DHCP, IPv4/IPv6, DNS):**

```bash
ipconfig getsummary en0
```

**Check Public IP Address (IPv4/IPv6):**

```bash
curl -s https://ifconfig.me
```

**Show All Interfaces with Addresses:**

```bash
ifconfig | grep -E "^[a-z]|inet "
```

**Renew the DHCP Lease on Wi-Fi:**

```bash
sudo ipconfig set en0 DHCP
```

**Turn a Network Service Off and On:**

```bash
networksetup -setnetworkserviceenabled "Wi-Fi" off
networksetup -setnetworkserviceenabled "Wi-Fi" on
```

**List Network Services in Priority Order:**

```bash
networksetup -listnetworkserviceorder
```

---

## 2. Wi-Fi

**Run Comprehensive Apple Wireless Diagnostics (Channel, RSSI, Noise, MCS, Tx Rate):**

```bash
sudo wdutil info
```

**Scan for Nearby Networks (Signal, Channel, Security):**

```bash
system_profiler SPAirPortDataType
```

The old `airport` command was removed in macOS 14.4; use `wdutil` and `system_profiler` instead.

**Turn Wi-Fi Off and On:**

```bash
networksetup -setairportpower en0 off
networksetup -setairportpower en0 on
```

**Join a Wi-Fi Network:**

```bash
networksetup -setairportnetwork en0 "[SSID]" "[password]"
```

**List Saved (Preferred) Wi-Fi Networks:**

```bash
networksetup -listpreferredwirelessnetworks en0
```

**Forget a Saved Wi-Fi Network:**

```bash
sudo networksetup -removepreferredwirelessnetwork en0 "[SSID]"
```

**Show the Saved Password for a Wi-Fi Network (Prompts for Approval):**

```bash
security find-generic-password -wa "[SSID]"
```

---

## 3. DNS

**Get Active DNS Servers for Wi-Fi:**

```bash
networksetup -getdnsservers Wi-Fi
```

**Set Custom DNS Servers for Wi-Fi (e.g., Quad9):**

```bash
sudo networksetup -setdnsservers Wi-Fi 9.9.9.9 149.112.112.112
```

**Revert Wi-Fi DNS to DHCP Default:**

```bash
sudo networksetup -setdnsservers Wi-Fi "Empty"
```

**Flush System DNS Cache:**

```bash
sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
```

**Query DNS Resolution Using macOS Native Resolver (Respects mDNS & VPN Split-DNS):**

```bash
dscacheutil -q host -a name [example.com]
```

**Inspect Full System DNS Routing & Scoped Resolvers:**

```bash
scutil --dns
```

**Send Lookups for One Domain to a Specific DNS Server (Split DNS):**

```bash
sudo mkdir -p /etc/resolver && echo "nameserver [100.101.102.103]" | sudo tee /etc/resolver/[home.lan]
```

Every name ending in that domain now goes to that server. Check it with `scutil --dns`.

**Browse Services Advertised on the Local Network (Bonjour/mDNS):**

```bash
dns-sd -B _ssh._tcp
```

---

## 4. Routing & Troubleshooting

**Show the Routing Table:**

```bash
netstat -rn
```

**Show Which Gateway and Interface Reach an Address:**

```bash
route -n get default
route -n get [1.1.1.1]
```

**Ping and Trace a Route:**

```bash
ping -c 4 [1.1.1.1]
traceroute [example.com]
```

**Test Whether a TCP Port Is Open:**

```bash
nc -vz [host] [port]
```

**Show the ARP Table (Devices Seen on the Local Network):**

```bash
arp -a
```

**Capture Packets on Wi-Fi (Press `Ctrl+C` to Stop):**

```bash
sudo tcpdump -i en0 -n port 53
```

---

## 5. VPN & Proxies

**List Built-In VPN Connections and Their Status:**

```bash
scutil --nc list
```

**Connect and Disconnect a Built-In VPN:**

```bash
scutil --nc start "[VPN name]"
scutil --nc stop "[VPN name]"
```

**Show Web Proxy Settings for Wi-Fi:**

```bash
networksetup -getwebproxy "Wi-Fi"
networksetup -getsecurewebproxy "Wi-Fi"
```

**Show All Proxy Settings in Effect:**

```bash
scutil --proxy
```

---

## 6. Speed, Ports & Connections

**Run Built-in Network Throughput, Responsiveness (RPM) & Latency Test:**

```bash
networkQuality -v
```

**View Listening TCP Ports & Owning Processes:**

```bash
sudo lsof -iTCP -sTCP:LISTEN -n -P
```

**View Active Network Connections & Socket Statistics:**

```bash
netstat -anv | grep ESTABLISHED
```

**Live Per-App Network Usage:**

```bash
nettop -m tcp
```

---

## 7. Firewall

**Check macOS Application Layer Firewall (ALF) Status:**

```bash
/usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate
```

**Enable Application Firewall & Stealth Mode (Drop Unsolicited ICMP/Probes):**

```bash
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setstealthmode on
```

**List Apps Allowed or Blocked by the Firewall:**

```bash
/usr/libexec/ApplicationFirewall/socketfilterfw --listapps
```

**Check Packet Filter (`pf`) Firewall Status & Rules:**

```bash
sudo pfctl -s info
sudo pfctl -sr
```

---

## 8. Computer Name & Sharing

**Show the Three Names macOS Uses:**

```bash
scutil --get ComputerName; scutil --get LocalHostName; scutil --get HostName
```

**Set the Computer Name (Shown in Finder and AirDrop) and Local Hostname (`.local`):**

```bash
sudo scutil --set ComputerName "[Kaz MacBook]"
sudo scutil --set LocalHostName "[kaz-macbook]"
```

**Turn On Remote Login (SSH Server):**

```bash
sudo systemsetup -setremotelogin on
```

**Check Whether Remote Login Is On:**

```bash
sudo systemsetup -getremotelogin
```

---

## 9. Quick Reference

```bash
ipconfig getifaddr en0                     # local IP
sudo wdutil info                           # Wi-Fi diagnostics
networksetup -setairportpower en0 off      # Wi-Fi off (on to re-enable)
networksetup -getdnsservers Wi-Fi          # DNS servers
sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder   # flush DNS
scutil --dns                               # DNS routing
networkQuality                             # speed test
sudo lsof -nP -iTCP -sTCP:LISTEN           # listening ports
netstat -rn                                # routes
scutil --nc list                           # VPNs
```

---

## Sources & Verification

* **Terminal User Guide:** [Apple Support](https://support.apple.com/guide/terminal/welcome/mac)
* **Built-in manual pages:** run `man <command>` (for example `man networksetup`)

## Related guides

* [macOS Command-Line Reference (Apple Silicon)](macos-command-line-reference.md)
* [macOS Homebrew Cheat Sheet](macos-homebrew-cheat-sheet.md)
* [macOS System, Updates and Hardware Cheat Sheet](macos-system-updates-and-hardware-cheat-sheet.md)
* [macOS launchd, Processes and Logs Cheat Sheet](macos-launchd-and-logs-cheat-sheet.md)
* [macOS Security Cheat Sheet](macos-security-cheat-sheet.md)
* [macOS defaults, Finder and CLI Tips Cheat Sheet](macos-defaults-and-cli-tips-cheat-sheet.md)
