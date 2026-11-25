# macOS launchd, Processes and Logs Cheat Sheet

Quick-reference guide for launchd services and LaunchAgents, processes, the unified log, and crash reports on macOS.

---

## 1. launchd Services

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

**Where Service Definitions Live:**

| Folder | Runs as | Starts |
| --- | --- | --- |
| `~/Library/LaunchAgents/` | You | When you log in |
| `/Library/LaunchAgents/` | Each logged-in user | When any user logs in |
| `/Library/LaunchDaemons/` | root | At boot, before login |
| `/System/Library/Launch*` | Apple's own services | Don't edit (protected by SIP) |

### Write Your Own LaunchAgent

`~/Library/LaunchAgents/com.kaz.backup.plist` runs a script every day at 02:30:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.kaz.backup</string>
    <key>ProgramArguments</key>
    <array>
        <string>/Users/kaz/bin/backup.sh</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>2</integer>
        <key>Minute</key>
        <integer>30</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>/tmp/com.kaz.backup.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/com.kaz.backup.log</string>
</dict>
</plist>
```

```bash
plutil -lint ~/Library/LaunchAgents/com.kaz.backup.plist
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.kaz.backup.plist
launchctl kickstart gui/$(id -u)/com.kaz.backup
```

Use `StartInterval` (seconds) instead of `StartCalendarInterval` to run every N seconds, or `RunAtLoad` with `KeepAlive` to keep a program running. A job missed while the Mac was asleep runs when it wakes.

---

## 2. Homebrew Services

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

---

## 3. Processes

**List All Processes with CPU and Memory Use:**

```bash
ps aux
```

**Find a Process by Name:**

```bash
pgrep -lf [name]
```

**Show the Process Tree:**

```bash
ps -axo pid,ppid,user,%cpu,%mem,command | head -n 30
```

**Which Process Has a File or Folder Open (Fixes "Disk Can't Be Ejected"):**

```bash
sudo lsof +D /Volumes/[name]
```

**Files and Network Connections a Process Has Open:**

```bash
sudo lsof -p [PID]
```

**Sample What a Hung App Is Doing (Writes a Report):**

```bash
sample [AppName] 5 -file ~/Desktop/[app]-sample.txt
```

**Watch File System Activity of One Process Live:**

```bash
sudo fs_usage -w -f filesys [AppName]
```

**Quit an App Gracefully:**

```bash
osascript -e 'quit app "[AppName]"'
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

**Restart Finder, the Dock, or the Menu Bar:**

```bash
killall Finder
killall Dock
killall SystemUIServer
```

---

## 4. Unified Log

**Stream Live Unified System Logs Filtered by Process:**

```bash
log stream --predicate 'process == "sshd"' --info
```

**Query Historical Unified System Logs (Last 1 Hour):**

```bash
log show --predicate 'subsystem == "com.apple.network"' --last 1h --info --style compact
```

**Only Errors and Faults from the Last 30 Minutes:**

```bash
log show --last 30m --predicate 'messageType == error OR messageType == fault' --style compact
```

**Messages Containing a Word:**

```bash
log show --last 1h --predicate 'eventMessage CONTAINS[c] "[word]"' --style compact
```

**Logs from One Subsystem (for Example Wi-Fi):**

```bash
log show --last 1h --predicate 'subsystem == "com.apple.wifi"' --style compact
```

**Shutdown and Restart Reasons from Recent Boots:**

```bash
log show --last 3d --predicate 'eventMessage CONTAINS "Previous shutdown cause"' --style compact
```

**Save Logs to an Archive to Look at Later or Share:**

```bash
sudo log collect --last 1h --output ~/Desktop/logs.logarchive
```

---

## 5. Crash Reports & Diagnostics

**App Crash and Hang Reports:**

```bash
ls -lt ~/Library/Logs/DiagnosticReports | head
```

**System Crash and Kernel Panic Reports:**

```bash
ls -lt /Library/Logs/DiagnosticReports | head
```

**Collect a Full Diagnostic Bundle for Apple Support (Takes a Few Minutes):**

```bash
sudo sysdiagnose -f ~/Desktop
```

---

## 6. Quick Reference

```bash
launchctl list | grep -v com.apple            # your loaded services
launchctl print gui/$(id -u)/[label]          # service details
launchctl kickstart -k gui/$(id -u)/[label]   # restart a service
brew services list                            # Homebrew services
pgrep -lf name                                # find a process
sudo lsof +D /Volumes/X                       # who's using a disk
log stream --process [name]                   # live logs
log show --last 30m --predicate 'messageType == error' --style compact
sudo sysdiagnose -f ~/Desktop                 # diagnostic bundle
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
