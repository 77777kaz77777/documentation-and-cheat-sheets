# macOS System, Updates and Hardware Cheat Sheet

Quick-reference guide for macOS updates, hardware information, disks and APFS, battery, and sleep on Apple Silicon.

---

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

## Sources & Verification

* **macOS release notes:** [Apple Developer](https://developer.apple.com/documentation/macos-release-notes)
* **Built-in manual pages:** run `man <command>` (for example `man softwareupdate`)

## Related guides

* [macOS Command-Line Reference (Apple Silicon)](macos-command-line-reference.md)
* [macOS Homebrew Cheat Sheet](macos-homebrew-cheat-sheet.md)
* [macOS Networking Cheat Sheet](macos-networking-cheat-sheet.md)
* [macOS launchd, Processes and Logs Cheat Sheet](macos-launchd-and-logs-cheat-sheet.md)
* [macOS Security Cheat Sheet](macos-security-cheat-sheet.md)
* [macOS defaults, Finder and CLI Tips Cheat Sheet](macos-defaults-and-cli-tips-cheat-sheet.md)
