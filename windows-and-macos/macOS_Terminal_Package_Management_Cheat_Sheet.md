## A quick-reference guide for macOS command-line operations, covering Homebrew package management, system software updates, networking tools, process management, and essential Finder modifications

## Package Management (Homebrew)

| Action | Command |
| :--- | :--- |
| **Install Homebrew** | `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` |
| **Update Recipes** | `brew update` |
| **Upgrade All Packages** | `brew upgrade` |
| **Install CLI Package** | `brew install [formula]` |
| **Install GUI App (Cask)** | `brew install --cask [app_name]` (e.g., `google-chrome`) |
| **Search for Package/App** | `brew search [query]` |
| **List Installed Packages** | `brew list` |
| **Uninstall Package** | `brew uninstall [formula]` |
| **Check System Health** | `brew doctor` |
| **Cleanup Old Versions/Cache**| `brew cleanup` |

## System & Power Management

> **Note:** `diskutil repairPermissions` was deprecated and removed in OS X El Capitan (10.11). Use `verifyVolume` or `repairVolume` instead.

| Action | Command |
| :--- | :--- |
| **List OS Updates** | `softwareupdate -l` |
| **Install All Updates** | `sudo softwareupdate -ia` |
| **System Info Overview** | `system_profiler SPSoftwareDataType SPHardwareDataType` |
| **List Disks/Volumes** | `diskutil list` |
| **Verify Disk Volume** | `diskutil verifyVolume /` |
| **Eject a Drive** | `diskutil eject /dev/disk[n]` |
| **Check Battery/Power Info** | `pmset -g batt` |
| **Prevent System Sleep** | `caffeinate -i` (Stays awake until `Ctrl+C` is pressed) |
| **Prevent Sleep for Command**| `caffeinate -i [command]` (Prevents sleep until command finishes) |

## Networking & Connectivity

> **Note:** The legacy `airport` CLI tool is deprecated in macOS Sonoma (14.0+). Use `networksetup` for modern Wi-Fi management.

| Action | Command |
| :--- | :--- |
| **Check Local IP Address** | `ipconfig getifaddr en0` (Wi-Fi is typically `en0`) |
| **Check Public IP Address** | `curl ifconfig.me` |
| **List Network Interfaces** | `networksetup -listallhardwareports` |
| **View Current Wi-Fi Network**| `networksetup -getairportnetwork en0` |
| **Clear DNS Cache** | `sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder` |
| **View Listening Ports** | `lsof -iTCP -sTCP:LISTEN -n -P` |

## Process & Service Management

| Action | Command |
| :--- | :--- |
| **List Active Services** | `launchctl list` |
| **Start a Daemon/Service** | `launchctl load ~/Library/LaunchAgents/[plist_file]` |
| **Stop a Daemon/Service** | `launchctl unload ~/Library/LaunchAgents/[plist_file]` |
| **Kill a Process by Name** | `killall [ProcessName]` (e.g., `killall Dock`) |
| **Kill a Process by PID** | `kill -9 [PID]` |
| **Manage Brew Services** | `brew services start/stop/restart [formula]` (Requires Homebrew) |

## macOS defaults & Finder Tweaks

`defaults` commands modify system preferences that are often hidden from the GUI. **Restart Finder** (`killall Finder`) or the relevant app after applying these.

| Action | Command |
| :--- | :--- |
| **Show Hidden Files** | `defaults write com.apple.finder AppleShowAllFiles -bool true; killall Finder` |
| **Show File Extensions** | `defaults write NSGlobalDomain AppleShowAllExtensions -bool true; killall Finder` |
| **Show Finder Path Bar** | `defaults write com.apple.finder ShowPathbar -bool true; killall Finder` |
| **Change Screenshot Dir** | `defaults write com.apple.screencapture location ~/Pictures/Screenshots; killall SystemUIServer` |
| **Disable Screenshot Shadow** | `defaults write com.apple.screencapture disable-shadow -bool true; killall SystemUIServer` |
| **Open Current Dir in Finder**| `open .` |
| **Open App from CLI** | `open -a "Visual Studio Code"` |

## macOS File System Specifics

* **Case Sensitivity:** By default, macOS file systems (APFS and HFS+) are **Case-Insensitive but Case-Preserving**. `File.txt` and `file.txt` are treated as the same file.
* **Metadata Files (`.DS_Store`):** The system generates these in directories to store custom attributes, folder view settings, and icon placements.
* **App Bundles:** Applications in `/Applications/` are actually directories styled as packages (ending in `.app`). Their executable binaries live inside at `Contents/MacOS/`.
* **External Drives:** Automatically mounted under the `/Volumes/` directory.

---
**Sources & Verification:**
* *Apple Developer Documentation (softwareupdate, pmset, launchctl):* https://developer.apple.com/library/archive/documentation/Darwin/Reference/ManPages/
* *Homebrew Official Documentation:* https://docs.brew.sh/
* *macOS Defaults Reference:* https://macos-defaults.com/
