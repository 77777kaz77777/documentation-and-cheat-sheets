# macOS 27 (Golden Gate) Command-Line Reference Guide

A comprehensive reference guide for macOS 27 (Golden Gate) command-line administration on Apple Silicon (`arm64`), covering Homebrew environment management, OS updates, Apple Silicon telemetry, networking diagnostics, launchd services, security controls, and system defaults.

---

## 1. Architecture & macOS 27 Environment Specifics

* **Apple Silicon Exclusivity:** macOS 27 (Golden Gate) drops all Intel (`x86_64`) Mac support. Every macOS 27 host runs natively on Apple Silicon (`arm64`).
* **Homebrew Prefix:** Native Apple Silicon packages install strictly to `/opt/homebrew` (unlike the legacy `/usr/local` Intel prefix).
* **Signed System Volume (SSV):** The root volume (`/`) is cryptographically sealed and mounted read-only. Dynamic user and system data lives on `/System/Volumes/Data` (firmlinked to `/Users`, `/Library`, and `/Applications`).

---

## 2. Package Management (Homebrew)

* **Install Homebrew:**
  `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` * **Configure Shell Environment (`~/.zprofile`):** `eval "$(/opt/homebrew/bin/brew shellenv)"`
* **Update Homebrew & Formulae Metadata:**
  `brew update`
* **Upgrade All Installed Formulae & Casks:**
  `brew upgrade`
* **Upgrade Including Auto-Updating GUI Casks:**
  `brew upgrade --greedy`
* **Install CLI Package (Formula):**
  `brew install [formula]`
* **Install GUI Application (Cask):**
  `brew install --cask [app_name]`
* **Search Formulae and Casks:**
  `brew search [query]`
* **Inspect Package Dependencies & Analytics:**
  `brew info [formula_or_cask]`
* **List Installed Formulae & Casks:**
  `brew list --formula`
  `brew list --cask`
* **Show Dependency Tree for Installed Packages:**
  `brew deps --tree --installed`
* **Uninstall Package Only:**
  `brew uninstall [formula]`
* **Completely Purge Cask (Removes App, Caches, and `.plist` Preferences):**
  `brew uninstall --cask --zap [app_name]`
* **Remove Orphaned Dependencies:**
  `brew autoremove`
* **Purge Old Versions & Clear Download Cache:**
  `brew cleanup --prune=all -s`
* **Export Installed Packages to a Brewfile (For Reproducible Setup):**
  `brew bundle dump --file=~/Brewfile --describe --force`
* **Install All Packages from a Brewfile:**
  `brew bundle --file=~/Brewfile`
* **Audit Homebrew Installation Health:**
  `brew doctor`

---

## 3. System, Hardware Telemetry & Power Management

* **Check Detailed macOS Build & Version:**
  `sw_vers`
* **List Available macOS Software Updates:**
  `softwareupdate -l`
* **Install All Available Updates & Reboot Automatically:**
  `sudo softwareupdate -iaR`
* **Download a Full macOS 27 Installer to `/Applications`:**
  `softwareupdate --fetch-full-installer --full-installer-version 27.0.1`
* **Install Xcode Command Line Tools (CLT):**
  `xcode-select --install`
* **Query Hardware, Software & NVMe Storage Profiles:**
  `system_profiler SPSoftwareDataType SPHardwareDataType SPNVMeDataType`
* **Monitor Apple Silicon CPU/GPU/ANE Power & Thermal Pressure (Live CLI):**
  `sudo powermetrics --samplers cpu_power,gpu_power,ane_power,thermal -i 1000 -n 1`
* **List All Disks, Partitions, and APFS Containers:**
  `diskutil list`
* **List APFS Volumes & Storage Pool Usage:**
  `diskutil apfs list`
* **Verify APFS Volume Integrity:**
  `diskutil verifyVolume /`
* **List Local Time Machine APFS Snapshots:**
  `tmutil listlocalsnapshots /`
* **Delete a Specific Local APFS Snapshot:**
  `sudo tmutil deletelocalsnapshots [snapshot_date]`
* **Eject an External Drive Safely:**
  `diskutil eject /dev/disk[n]`
* **Check Battery Health, Cycle Count & AC Status:**
  `pmset -g batt`
  `system_profiler SPPowerDataType | grep -E "Cycle Count|Condition|Maximum Capacity"`
* **Check Active Power Assertions (Find What Is Preventing Sleep):**
  `pmset -g assertions`
* **Prevent System & Display Sleep Indefinitely:**
  `caffeinate -di` (Runs until `Ctrl+C` is pressed)
* **Prevent Sleep Until a Specific Process (PID) Completes:**
  `caffeinate -w [PID]`

---

## 4. Networking, Wi-Fi & Firewall Diagnostics

*Note: The legacy `airport` binary was removed in macOS 14.4, and `networksetup -getairportnetwork` redacts SSIDs without GUI Location Services permissions. Use `wdutil` or `ipconfig` on macOS 27 for accurate CLI wireless diagnostics.*

* **View Complete Interface Summary (Unhidden SSID, BSSID, DHCP, IPv4/IPv6, DNS):**
  `ipconfig getsummary en0`
* **Run Comprehensive Apple Wireless Diagnostics (Channel, RSSI, Noise, MCS, Tx Rate):**
  `sudo wdutil info`
* **Check Local IPv4 Address (Wi-Fi is `en0` on MacBook Air/Pro):**
  `ipconfig getifaddr en0`
* **Check Public IP Address (IPv4/IPv6):**
  `curl -s https://ifconfig.me`
* **Map Hardware Ports to BSD Device Interfaces (`en0`, `en1`, `bridge0`):**
  `networksetup -listallhardwareports`
* **Get Active DNS Servers for Wi-Fi:**
  `networksetup -getdnsservers Wi-Fi`
* **Set Custom DNS Servers for Wi-Fi (e.g., Local Resolver or Quad9):**
  `sudo networksetup -setdnsservers Wi-Fi 9.9.9.9 149.112.112.112`
* **Revert Wi-Fi DNS to DHCP Default:**
  `sudo networksetup -setdnsservers Wi-Fi "Empty"`
* **Flush System DNS Cache:**
  `sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder`
* **Query DNS Resolution Using macOS Native Resolver (Replaces `dig` for mDNS/VPNs):**
  `dscacheutil -q host -a name [example.com]`
* **Inspect Full System DNS Routing & Scoped Resolvers (Tailscale/VPN Split-DNS):**
  `scutil --dns`
* **Run Built-in Network Throughput, Responsiveness (RPM) & Latency Test:**
  `networkQuality -v`
* **View Listening TCP Ports & Owning Processes:**
  `sudo lsof -iTCP -sTCP:LISTEN -n -P`
* **View Active Network Connections & Socket Statistics:**
  `netstat -anv | grep ESTABLISHED`
* **Check macOS Application Layer Firewall (ALF) Status:**
  `/usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate`
* **Enable Application Firewall & Stealth Mode (Drop Unsolicited ICMP/Probes):**
  `sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on`
  `sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setstealthmode on`
* **Check Packet Filter (`pf`) Firewall Status & Rules:**
  `sudo pfctl -s info`
  `sudo pfctl -sr`

---

## 5. Process, Service (`launchd`) & Log Management

*Note: `launchctl load` and `unload` are deprecated. On macOS 27, always use `bootstrap`, `bootout`, `enable`, `disable`, and `kickstart` with explicit target domains (`gui/$(id -u)` for user agents, `system` for root daemons).*

* **List All Loaded Services in Current Session:**
  `launchctl list`
* **Inspect Detailed State of a Specific Service (PID, Exit Code, Paths, Endpoints):**
  `launchctl print gui/$(id -u)/[service_label]`
  `sudo launchctl print system/[service_label]`
* **Load & Start a User LaunchAgent (`~/Library/LaunchAgents/`):**
  `launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/[label].plist`
* **Stop & Unload a User LaunchAgent:**
  `launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/[label].plist`
* **Force-Restart (`kickstart`) a Running Service Without Unloading:**
  `launchctl kickstart -k gui/$(id -u)/[service_label]`
* **Enable or Disable a Service Persistently Across Reboots:**
  `launchctl enable gui/$(id -u)/[service_label]`
  `launchctl disable gui/$(id -u)/[service_label]`
* **Manage Homebrew Background Services (Wrapper for `launchctl`):**
  `brew services list`
  `brew services start [formula]`
  `brew services stop [formula]`
  `brew services restart [formula]`
* **Kill a Process by Exact Name:**
  `killall [ProcessName]`
* **Kill Processes Matching a Pattern:**
  `pkill -f [pattern]`
* **Stream Live Unified System Logs Filtered by Process or Subsystem:**
  `log stream --predicate 'process == "sshd"' --info`
* **Query Historical Unified System Logs (Last 1 Hour):**
  `log show --predicate 'subsystem == "com.apple.network"' --last 1h --info --style compact`

---

## 6. Security, Gatekeeper, XProtect & Disk Encryption

* **Check FileVault Full-Disk Encryption Status:**
  `fdesetup status`
* **Check System Integrity Protection (SIP) Status:**
  `csrutil status`
* **Check Gatekeeper Assessment Status:**
  `spctl --status`
* **Verify Code Signature & Notarization of an Application Bundle:**
  `codesign -dv --verbose=4 /Applications/[AppName].app`
  `spctl -a -vvv -t exec /Applications/[AppName].app`
* **Inspect Extended Attributes (`xattr`) on a File or Application:**
  `xattr -l /Applications/[AppName].app`
* **Remove Quarantine Flag from a Downloaded Binary or Unsigned App:**
  `sudo xattr -dr com.apple.quarantine /Applications/[AppName].app`
* **Check XProtect Antivirus Version & Perform Manual Scan (macOS 15–27):**
  `xprotect version`
  `sudo xprotect check`
  `sudo xprotect update`
* **List Installed Configuration / MDM Profiles:**
  `profiles list`

---

## 7. macOS `defaults`, Finder & UI Tweaks

*Apply changes immediately by restarting the affected daemon (`killall Finder`, `killall Dock`, or `killall SystemUIServer`).*

* **Show Hidden Dotfiles in Finder:**
  `defaults write com.apple.finder AppleShowAllFiles -bool true && killall Finder`
* **Show All File Extensions System-Wide:**
  `defaults write NSGlobalDomain AppleShowAllExtensions -bool true && killall Finder`
* **Show Status Bar and Path Bar in Finder:**
  `defaults write com.apple.finder ShowStatusBar -bool true`
  `defaults write com.apple.finder ShowPathbar -bool true && killall Finder`
* **Display Full POSIX Path in Finder Window Title:**
  `defaults write com.apple.finder _FXShowPosixPathInTitle -bool true && killall Finder`
* **Default Finder Search Scope to Current Folder (Instead of "This Mac"):**
  `defaults write com.apple.finder FXDefaultSearchScope -string "SCcf" && killall Finder`
* **Keep Folders on Top When Sorting by Name in Finder:**
  `defaults write com.apple.finder _FXSortFoldersFirst -bool true && killall Finder`
* **Disable Warning When Changing a File Extension:**
  `defaults write com.apple.finder FXEnableExtensionChangeWarning -bool false && killall Finder`
* **Prevent Creation of `.DS_Store` Files on Network (SMB/NFS) & USB Volumes:**
  `defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true`
  `defaults write com.apple.desktopservices DSDontWriteUSBStores -bool true`
* **Disable `.DS_Store` Verification Dialog When Opening Network Folders:**
  `defaults write com.apple.LaunchServices LSQuarantine -bool false` (Optional—use with caution)
* **Set Custom Screenshot Save Directory:**
  `mkdir -p ~/Pictures/Screenshots`
  `defaults write com.apple.screencapture location ~/Pictures/Screenshots && killall SystemUIServer`
* **Disable Drop Shadows on Window Screenshots:**
  `defaults write com.apple.screencapture disable-shadow -bool true && killall SystemUIServer`
* **Change Screenshot Format (`png`, `jpg`, `pdf`, `heic`):**
  `defaults write com.apple.screencapture type -string "png" && killall SystemUIServer`
* **Speed Up Dock Auto-Hide & Remove Reveal Delay:**
  `defaults write com.apple.dock autohide-delay -float 0`
  `defaults write com.apple.dock autohide-time-modifier -float 0.15 && killall Dock`
* **Disable macOS "Press and Hold" Accents in Favor of Fast Key Repeat (Essential for Vim/Terminal):**
  `defaults write NSGlobalDomain ApplePressAndHoldEnabled -bool false`
  `defaults write NSGlobalDomain KeyRepeat -int 2`
  `defaults write NSGlobalDomain InitialKeyRepeat -int 15`

---

## 8. Daily CLI Productivity & Bridge Utilities

* **Copy Command Output Directly to macOS Clipboard (Pasteboard):**
  `cat ~/.ssh/id_ed25519.pub | pbcopy`
* **Paste Clipboard Contents into a File or Pipe:**
  `pbpaste > output.txt`
* **Open Current Working Directory in Finder:**
  `open .`
* **Launch an Application or Pass a File to a Specific GUI Application:**
  `open -a "Firefox" index.html`
* **Search Files Instantly via Spotlight Metadata Index (`mdfind`):**
  `mdfind "kMDItemDisplayName == '*config*'c"`
  `mdfind -onlyin ~/Documents "cybersecurity"`
* **Inspect Spotlight Metadata Attributes of a File:**
  `mdls [file_path]`
* **Convert Property List (`.plist`) Files Between Binary and XML for Editing:**
  `plutil -convert xml1 [file.plist]`
  `plutil -convert binary1 [file.plist]`
* **Validate `.plist` Syntax:**
  `plutil -lint [file.plist]`

---

## 9. Sources & Official Documentation

* **Apple macOS 27 (Golden Gate) Release Notes:** https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes
* **Apple Support — What's New in macOS 27 Golden Gate:** https://support.apple.com/en-us/127257
* **Homebrew Official Documentation (macOS 15–27 Support & Manpage):** https://docs.brew.sh/Installation and https://docs.brew.sh/Manpage
* **Apple Developer Man Pages (`launchctl`, `wdutil`, `softwareupdate`, `powermetrics`):** Accessible locally via `man [command]` or at https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/
* **macOS `defaults` Community Reference:** https://macos-defaults.com/
