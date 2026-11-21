# macOS launchd, Processes and Logs Cheat Sheet

Quick-reference guide for managing launchd services, processes, and the unified log on macOS.

---

**List All Loaded Services in Current Session:**

```bash
launchctl list
```

**Inspect Detailed State of a User Service (PID, Exit Code, Paths, Endpoints):**

```bash
launchctl print gui/$(id -u)/[service_label]
```

**Inspect Detailed State of a System Service:**

```bash
sudo launchctl print system/[service_label]
```

**Load & Start a User LaunchAgent (`~/Library/LaunchAgents/`):**

```bash
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/[label].plist
```

**Stop & Unload a User LaunchAgent:**

```bash
launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/[label].plist
```

**Force-Restart (`kickstart`) a Running Service Without Unloading:**

```bash
launchctl kickstart -k gui/$(id -u)/[service_label]
```

**Enable a Service Persistently Across Reboots:**

```bash
launchctl enable gui/$(id -u)/[service_label]
```

**Disable a Service Persistently Across Reboots:**

```bash
launchctl disable gui/$(id -u)/[service_label]
```

**List Homebrew Background Services:**

```bash
brew services list
```

**Start, Stop, or Restart a Homebrew Service:**

```bash
brew services start [formula]
brew services stop [formula]
brew services restart [formula]
```

**Kill a Process by Exact Name:**

```bash
killall [ProcessName]
```

**Kill Processes Matching a Pattern:**

```bash
pkill -f [pattern]
```

**Kill a Process Immediately by PID:**

```bash
kill -9 [PID]
```

**Stream Live Unified System Logs Filtered by Process:**

```bash
log stream --predicate 'process == "sshd"' --info
```

**Query Historical Unified System Logs (Last 1 Hour):**

```bash
log show --predicate 'subsystem == "com.apple.network"' --last 1h --info --style compact
```

---

## Sources & Verification

* **Built-in manual pages:** run `man <command>` (for example `man launchctl`)

## Related guides

* [macOS Command-Line Reference (Apple Silicon)](macos-command-line-reference.md)
* [macOS Homebrew Cheat Sheet](macos-homebrew-cheat-sheet.md)
* [macOS System, Updates and Hardware Cheat Sheet](macos-system-updates-and-hardware-cheat-sheet.md)
* [macOS Networking Cheat Sheet](macos-networking-cheat-sheet.md)
* [macOS Security Cheat Sheet](macos-security-cheat-sheet.md)
* [macOS defaults, Finder and CLI Tips Cheat Sheet](macos-defaults-and-cli-tips-cheat-sheet.md)
