# macOS Networking Cheat Sheet

Quick-reference guide for Wi-Fi, DNS, connections, and the firewall on macOS.

---

**View Complete Interface Summary (SSID, BSSID, DHCP, IPv4/IPv6, DNS):**

```bash
ipconfig getsummary en0
```

**Run Comprehensive Apple Wireless Diagnostics (Channel, RSSI, Noise, MCS, Tx Rate):**

```bash
sudo wdutil info
```

**Check Local IPv4 Address (Wi-Fi is `en0` on MacBooks):**

```bash
ipconfig getifaddr en0
```

**Check Public IP Address (IPv4/IPv6):**

```bash
curl -s https://ifconfig.me
```

**Map Hardware Ports to BSD Device Interfaces (`en0`, `en1`, `bridge0`):**

```bash
networksetup -listallhardwareports
```

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

**Check macOS Application Layer Firewall (ALF) Status:**

```bash
/usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate
```

**Enable Application Firewall & Stealth Mode (Drop Unsolicited ICMP/Probes):**

```bash
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setstealthmode on
```

**Check Packet Filter (`pf`) Firewall Status & Rules:**

```bash
sudo pfctl -s info
sudo pfctl -sr
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
