# macOS defaults, Finder and CLI Tips Cheat Sheet

Quick-reference guide for changing hidden settings with `defaults`, tweaking Finder and the Dock, and everyday Terminal tools for the clipboard, screenshots, audio, images, and Spotlight on macOS.

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

## Reading & Resetting Settings

**Read Every Setting an App Has Stored:**

```bash
defaults read com.apple.finder
```

**Find the Setting Name Behind a Toggle (Run Before and After Changing It):**

```bash
defaults read > /tmp/before.txt
defaults read > /tmp/after.txt && diff /tmp/before.txt /tmp/after.txt
```

**Undo a `defaults write` Tweak:**

```bash
defaults delete com.apple.finder AppleShowAllFiles && killall Finder
```

**Reset the Dock to Its Default Apps and Layout:**

```bash
defaults delete com.apple.dock && killall Dock
```

**Toggle Dark Mode:**

```bash
osascript -e 'tell application "System Events" to tell appearance preferences to set dark mode to not dark mode'
```

---

## Screenshots, Audio & Notifications

**Screenshot of a Selected Area to the Desktop:**

```bash
screencapture -i ~/Desktop/shot.png
```

**Screenshot of the Whole Screen After a 5-Second Delay:**

```bash
screencapture -T 5 ~/Desktop/shot.png
```

**Screenshot Straight to the Clipboard:**

```bash
screencapture -ic
```

**Set, Mute, and Unmute the Volume:**

```bash
osascript -e 'set volume output volume 40'
osascript -e 'set volume output muted true'
osascript -e 'set volume output muted false'
```

**Show a Notification When a Long Command Finishes:**

```bash
[long-command]; osascript -e 'display notification "Finished" with title "Terminal"'
```

**Speak Text Aloud:**

```bash
say "Backup complete"
```

**Run a Shortcut from the Shortcuts App:**

```bash
shortcuts list
shortcuts run "[Shortcut Name]"
```

---

## Files, Images & Documents

**Preview Any File with Quick Look:**

```bash
qlmanage -p [file]
```

**Resize an Image So Its Longest Side Is 1200 px:**

```bash
sips -Z 1200 [photo].jpg --out [photo]-small.jpg
```

**Convert HEIC Photos to JPEG:**

```bash
sips -s format jpeg [photo].heic --out [photo].jpg
```

**Convert a Document Between Formats (for Example Word to Plain Text):**

```bash
textutil -convert txt [document].docx
```

**Compress and Extract Zip Files (Keeps macOS Metadata):**

```bash
ditto -c -k --sequesterRsrc --keepParent [folder] [folder].zip
ditto -x -k [archive].zip [destination]
```

**Show the File Type of a File:**

```bash
file [file]
```

---

## Spotlight Index

**Check Whether Spotlight Indexing Is On for a Volume:**

```bash
mdutil -s /
```

**Rebuild the Spotlight Index (Fixes Missing Search Results):**

```bash
sudo mdutil -E /
```

**Turn Off Indexing for an External Drive:**

```bash
sudo mdutil -i off /Volumes/[name]
```

---

## Sources & Verification

* **`defaults` reference:** [macos-defaults.com](https://macos-defaults.com/)
* **Terminal User Guide:** [Apple Support](https://support.apple.com/guide/terminal/welcome/mac)

## Related guides

* [macOS Command-Line Reference (Apple Silicon)](macos-command-line-reference.md)
* [macOS Homebrew Cheat Sheet](macos-homebrew-cheat-sheet.md)
* [macOS System, Updates and Hardware Cheat Sheet](macos-system-updates-and-hardware-cheat-sheet.md)
* [macOS Networking Cheat Sheet](macos-networking-cheat-sheet.md)
* [macOS launchd, Processes and Logs Cheat Sheet](macos-launchd-and-logs-cheat-sheet.md)
* [macOS Security Cheat Sheet](macos-security-cheat-sheet.md)
