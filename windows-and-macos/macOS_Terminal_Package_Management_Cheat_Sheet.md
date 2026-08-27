# macOS Terminal and Package Management Cheat Sheet

##  macOS Package Management (Homebrew)
| Action | Command |
| :--- | :--- |
| **Install Homebrew** | `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent...)"` |
| **Update Recipes** | `brew update` |
| **Upgrade All Packages** | `brew upgrade` |
| **Install App** | `brew install [formula]` |
| **Install GUI App (Cask)** | `brew install --cask [app_name]` (e.g., `google-chrome`) |
| **Search for App** | `brew search [query]` |
| **Cleanup Old Versions** | `brew cleanup` |

##  System & Software Management
| Action | Command |
| :--- | :--- |
| **List OS Updates** | `softwareupdate -l` |
| **Install All Updates** | `sudo softwareupdate -ia` |
| **List Disks/Volumes** | `diskutil list` |
| **Eject a Drive** | `diskutil eject /dev/disk[n]` |
| **Repair Permissions** | `diskutil repairPermissions /` |
| **Check Battery Info** | `pmset -g batt` |
| **Prevent Sleep** | `caffeinate -i` (Stays awake until you Ctrl+C) |

##  Networking & Finder Integration
| Action | Command |
| :--- | :--- |
| **Check IP Address** | `ipconfig getifaddr en0` |
| **List Wi-Fi Networks** | `/System/Library/PrivateFrameworks/Apple80211.framework/.../airport -s` |
| **Open Folder in Finder** | `open .` |
| **Open App from CLI** | `open -a "Visual Studio Code"` |
| **Show Hidden Files** | `defaults write com.apple.finder AppleShowAllFiles YES; killall Finder` |
| **Change Screenshots Dir** | `defaults write com.apple.screencapture location ~/Pictures/Screenshots` |

##  Process & Service Management
* **List Services:** `launchctl list`
* **Start a Service:** `launchctl load ~/Library/LaunchAgents/[plist]`
* **Kill a Process:** `killall [ProcessName]` (e.g., `killall Dock`)
* **Clear DNS Cache:** `sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder`

##  File System Differences
* **Case Sensitivity:** By default, macOS file systems (APFS) are **Case-Insensitive**. `File.txt` and `file.txt` are the same file.
* **Metadata Files:** You will often see `.DS_Store` files in directories; these store folder view settings.
* **App Locations:** Most apps are stored in `/Applications/` and are actually "Bundles" (folders ending in `.app`).
