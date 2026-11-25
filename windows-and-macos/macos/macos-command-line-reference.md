# macOS Command-Line Reference (Apple Silicon)

Start page for the macOS command-line cheat sheets. They cover modern macOS administration on Apple Silicon (`arm64`): Homebrew, updates and hardware, networking, launchd services, security, and system defaults.

---

## Architecture & Environment Specifics

* **Apple Silicon Architecture:** Modern macOS runs natively on Apple Silicon (`arm64`).
* **Homebrew Prefix:** Native Apple Silicon packages install strictly to `/opt/homebrew`.
* **Signed System Volume (SSV):** The root volume (`/`) is cryptographically sealed and mounted read-only. Dynamic user and system data lives on `/System/Volumes/Data` (firmlinked to `/Users`, `/Library`, and `/Applications`).
* **File System Behavior:** APFS is **Case-Insensitive but Case-Preserving** by default (`File.txt` and `file.txt` resolve to the same file). External drives mount under `/Volumes/`, and GUI applications in `/Applications/` are `.app` directory bundles with binaries located inside `Contents/MacOS/`.

---

## Cheat Sheets in This Set

| Cheat sheet | Covers |
| --- | --- |
| [macOS Homebrew Cheat Sheet](macos-homebrew-cheat-sheet.md) | Installing, upgrading, and removing formulae and casks; Brewfiles; cleanup |
| [macOS System, Updates and Hardware Cheat Sheet](macos-system-updates-and-hardware-cheat-sheet.md) | Updates and Rosetta, hardware info, memory and CPU, **battery health and charging**, power and sleep settings, thermals, disks and APFS, disk images, Time Machine |
| [macOS Networking Cheat Sheet](macos-networking-cheat-sheet.md) | Interfaces, Wi-Fi (scan, join, forget, saved passwords), DNS and split DNS, routing and troubleshooting, VPNs and proxies, ports, firewall, computer name and Remote Login |
| [macOS launchd, Processes and Logs Cheat Sheet](macos-launchd-and-logs-cheat-sheet.md) | `launchctl` services, writing your own LaunchAgent, Homebrew services, processes and open files, unified log searches, crash reports, `sysdiagnose` |
| [macOS Security Cheat Sheet](macos-security-cheat-sheet.md) | Security status, FileVault, Gatekeeper and code signing, quarantine, XProtect, privacy permissions, Keychain and certificates, Touch ID for `sudo`, MDM profiles |
| [macOS defaults, Finder and CLI Tips Cheat Sheet](macos-defaults-and-cli-tips-cheat-sheet.md) | `defaults` tweaks for Finder and the Dock, clipboard, `open`, screenshots, volume, notifications, Shortcuts, image conversion, Spotlight, and plist tools |

For Homebrew commands that work on both macOS and Linux, see the [Homebrew Command Reference](../../linux-general/package-management/brew-command-reference.md).

---

## Sources & Official Documentation

* **Apple Developer macOS Release Notes:** [https://developer.apple.com/documentation/macos-release-notes](https://developer.apple.com/documentation/macos-release-notes)
* **Apple Terminal User Guide:** [https://support.apple.com/guide/terminal/welcome/mac](https://support.apple.com/guide/terminal/welcome/mac)
* **Homebrew Official Documentation & Manpage:** [https://docs.brew.sh/Manpage](https://docs.brew.sh/Manpage)
* **Apple Built-in Manual Pages (`launchctl`, `wdutil`, `softwareupdate`, `powermetrics`, `codesign`, `stapler`):** Accessible locally via `man [command]`
* **macOS `defaults` Reference:** [https://macos-defaults.com/](https://macos-defaults.com/)
