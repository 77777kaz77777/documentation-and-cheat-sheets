# macOS Command-Line Reference Guide (Apple Silicon)

A comprehensive reference guide for modern macOS command-line administration on Apple Silicon (`arm64`), covering Homebrew environment management, OS updates, hardware telemetry, networking diagnostics, launchd services, security controls, and system defaults.

---

## Architecture & Environment Specifics

* **Apple Silicon Architecture:** Modern macOS runs natively on Apple Silicon (`arm64`).
* **Homebrew Prefix:** Native Apple Silicon packages install strictly to `/opt/homebrew`.
* **Signed System Volume (SSV):** The root volume (`/`) is cryptographically sealed and mounted read-only. Dynamic user and system data lives on `/System/Volumes/Data` (firmlinked to `/Users`, `/Library`, and `/Applications`).
* **File System Behavior:** APFS is **Case-Insensitive but Case-Preserving** by default (`File.txt` and `file.txt` resolve to the same file). External drives mount under `/Volumes/`, and GUI applications in `/Applications/` are `.app` directory bundles with binaries located inside `Contents/MacOS/`.

---

## Package Management (Homebrew)

**Install Homebrew:**
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Configure Shell Environment (`~/.zprofile`):**
```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```

**Update Homebrew & Formulae Metadata:**
```bash
brew update
```

**Upgrade All Installed Formulae & Casks:**
```bash
brew upgrade
```

**Upgrade Including Auto-Updating GUI Casks:**
```bash
brew upgrade --greedy
```

**Install CLI Package (Formula):**
```bash
brew install [formula]
```

**Install GUI Application (Cask):**
```bash
brew install --cask [app_name]
```

**Search Formulae and Casks:**
```bash
brew search [query]
```

**Inspect Package Dependencies & Analytics:**
```bash
brew info [formula_or_cask]
```

**List Installed Formulae:**
```bash
brew list --formula
```

**List Installed Casks:**
```bash
brew list --cask
```

**Show Dependency Tree for Installed Packages:**
```bash
brew deps --tree --installed
```

**Uninstall Package Only:**
```bash
brew uninstall [formula]
```

**Completely Purge Cask (Removes App, Caches, and `.plist` Preferences):**
```bash
brew uninstall --cask --zap [app_name]
```

**Remove Orphaned Dependencies:**
```bash
brew autoremove
```

**Purge Old Versions & Clear Download Cache:**
```bash
brew cleanup --prune=all -s
```

**Export Installed Packages to a Brewfile (For Reproducible Setup):**
```bash
brew bundle dump --file=~/Brewfile --describe --force
```

**Install All Packages from a Brewfile:**
```bash
brew bundle --file=~/Brewfile
```

**Audit Homebrew Installation Health:**
```bash
brew doctor
```

---

## System, Hardware Telemetry & Power Management

**Check Detailed macOS Build & Version:**
```bash
sw_vers
```

**List Available macOS Software Updates:**
```bash
softwareupdate -l
```

**Install All Available Updates & Reboot Automatically:**
```bash
sudo softwareupdate -iaR
```

**Download the Latest Full macOS Installer to `/Applications`:**
```bash
softwareupdate --fetch-full-installer
```

**Download a Specific Full macOS Installer Version:**
```bash
softwareupdate --fetch-full-installer --full-installer-version [version]
```

**Install Xcode Command Line Tools (CLT):**
```bash
xcode-select --install
```

**Query Hardware, Software & NVMe Storage Profiles:**
```bash
system_profiler SPSoftwareDataType SPHardwareDataType SPNVMeDataType
```

**Monitor Apple Silicon CPU/GPU/ANE Power & Thermal Pressure (Live CLI):**
```bash
sudo powermetrics --samplers cpu_power,gpu_power,ane_power,thermal -i 1000 -n 1
```

**List All Disks, Partitions, and APFS Containers:**
```bash
diskutil list
```

**List APFS Volumes & Storage Pool Usage:**
```bash
diskutil apfs list
```

**Verify APFS Volume Integrity:**
```bash
diskutil verifyVolume /
```

**List Local Time Machine APFS Snapshots:**
```bash
tmutil listlocalsnapshots /
```

**Delete a Specific Local APFS Snapshot:**
```bash
sudo tmutil deletelocalsnapshots [snapshot_date]
```

**Eject an External Drive Safely:**
```bash
diskutil eject /dev/disk[n]
```

**Check Battery Status & Current Charge:**
```bash
pmset -g batt
```

**Check Battery Cycle Count & Maximum Capacity:**
```bash
system_profiler SPPowerDataType | grep -E "Cycle Count|Condition|Maximum Capacity"
```

**Check Active Power Assertions (Find What Is Preventing Sleep):**
```bash
pmset -g assertions
```

**Prevent System & Display Sleep Indefinitely (Press `Ctrl+C` to Stop):**
```bash
caffeinate -di
```

**Prevent Sleep Until a Specific Command Finishes:**
```bash
caffeinate -i [command]
```

**Prevent Sleep Until a Specific Process (PID) Completes:**
```bash
caffeinate -w [PID]
```

---

## Networking, Wi-Fi & Firewall Diagnostics

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

## Process, Service (`launchd`) & Log Management

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

## Security, Gatekeeper, XProtect & Disk Encryption

**Check FileVault Full-Disk Encryption Status:**
```bash
fdesetup status
```

**Check System Integrity Protection (SIP) Status:**
```bash
csrutil status
```

**Verify Code Signature & Deep Strict Validation of an App Bundle:**
```bash
codesign -dvv --deep --strict /Applications/[AppName].app
```

**Verify Notarization Ticket Stapled to an App Bundle:**
```bash
stapler validate /Applications/[AppName].app
```

**Inspect Extended Attributes (`xattr`) on a File or Application:**
```bash
xattr -l /Applications/[AppName].app
```

**Remove Quarantine Flag from a Downloaded Binary or Unsigned App:**
```bash
sudo xattr -dr com.apple.quarantine /Applications/[AppName].app
```

**Check XProtect Antivirus Version:**
```bash
xprotect version
```

**Perform Manual XProtect Scan & Signature Update:**
```bash
sudo xprotect check
sudo xprotect update
```

**List Installed Configuration / MDM Profiles:**
```bash
profiles status
sudo profiles list
```

---

## macOS `defaults`, Finder & UI Tweaks

**Show Hidden Dotfiles in Finder:**
```bash
defaults write com.apple.finder AppleShowAllFiles -bool true && killall Finder
```

**Show All File Extensions System-Wide:**
```bash
defaults write NSGlobalDomain AppleShowAllExtensions -bool true && killall Finder
```

**Show Status Bar and Path Bar in Finder:**
```bash
defaults write com.apple.finder ShowStatusBar -bool true && defaults write com.apple.finder ShowPathbar -bool true && killall Finder
```

**Display Full POSIX Path in Finder Window Title:**
```bash
defaults write com.apple.finder _FXShowPosixPathInTitle -bool true && killall Finder
```

**Default Finder Search Scope to Current Folder (Instead of "This Mac"):**
```bash
defaults write com.apple.finder FXDefaultSearchScope -string "SCcf" && killall Finder
```

**Keep Folders on Top When Sorting by Name in Finder:**
```bash
defaults write com.apple.finder _FXSortFoldersFirst -bool true && killall Finder
```

**Disable Warning When Changing a File Extension:**
```bash
defaults write com.apple.finder FXEnableExtensionChangeWarning -bool false && killall Finder
```

**Prevent Creation of `.DS_Store` Files on Network (SMB/NFS) & USB Volumes:**
```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true
defaults write com.apple.desktopservices DSDontWriteUSBStores -bool true
```

**Set Custom Screenshot Save Directory:**
```bash
mkdir -p ~/Pictures/Screenshots && defaults write com.apple.screencapture location ~/Pictures/Screenshots && killall SystemUIServer
```

**Disable Drop Shadows on Window Screenshots:**
```bash
defaults write com.apple.screencapture disable-shadow -bool true && killall SystemUIServer
```

**Change Screenshot Format (`png`, `jpg`, `pdf`, `heic`):**
```bash
defaults write com.apple.screencapture type -string "png" && killall SystemUIServer
```

**Speed Up Dock Auto-Hide & Remove Reveal Delay:**
```bash
defaults write com.apple.dock autohide-delay -float 0 && defaults write com.apple.dock autohide-time-modifier -float 0.15 && killall Dock
```

**Disable "Press and Hold" Accents in Favor of Fast Key Repeat (Essential for Vim/Terminal):**
```bash
defaults write NSGlobalDomain ApplePressAndHoldEnabled -bool false
defaults write NSGlobalDomain KeyRepeat -int 2
defaults write NSGlobalDomain InitialKeyRepeat -int 15
```

---

## Daily CLI Productivity & Bridge Utilities

**Copy Command Output Directly to macOS Clipboard (Pasteboard):**
```bash
cat ~/.ssh/id_ed25519.pub | pbcopy
```

**Paste Clipboard Contents into a File:**
```bash
pbpaste > output.txt
```

**Open Current Working Directory in Finder:**
```bash
open .
```

**Launch an Application or Pass a File to a Specific GUI Application:**
```bash
open -a "Firefox" index.html
```

**Search Files Instantly via Spotlight Metadata Index (`mdfind`):**
```bash
mdfind "kMDItemDisplayName == '*config*'c"
```

**Search Spotlight Content Within a Specific Directory:**
```bash
mdfind -onlyin ~/Documents "security"
```

**Inspect Spotlight Metadata Attributes of a File:**
```bash
mdls [file_path]
```

**Convert Property List (`.plist`) Files Between Binary and XML for Editing:**
```bash
plutil -convert xml1 [file.plist]
plutil -convert binary1 [file.plist]
```

**Validate `.plist` Syntax:**
```bash
plutil -lint [file.plist]
```

---

## Sources & Official Documentation

* **Apple Developer macOS Release Notes:** [https://developer.apple.com/documentation/macos-release-notes](https://developer.apple.com/documentation/macos-release-notes)
* **Apple Terminal User Guide:** [https://support.apple.com/guide/terminal/welcome/mac](https://support.apple.com/guide/terminal/welcome/mac)
* **Homebrew Official Documentation & Manpage:** [https://docs.brew.sh/Manpage](https://docs.brew.sh/Manpage)
* **Apple Built-in Manual Pages (`launchctl`, `wdutil`, `softwareupdate`, `powermetrics`, `codesign`, `stapler`):** Accessible locally via `man [command]`
* **macOS `defaults` Reference:** [https://macos-defaults.com/](https://macos-defaults.com/)
