# macOS System, Updates and Hardware Cheat Sheet

Quick-reference guide for macOS updates, hardware information, battery health, power and sleep, disks and APFS, disk images, and Time Machine on Apple Silicon.

---

## 1. macOS Version & Updates

**Check Detailed macOS Build & Version:**

```bash
sw_vers
```

**Show Just the Version Number (Useful in Scripts):**

```bash
sw_vers -productVersion
```

**Confirm the Mac Is Apple Silicon (`arm64`) or Intel (`x86_64`):**

```bash
uname -m
```

**List Available macOS Software Updates:**

```bash
softwareupdate -l
```

**Install One Specific Update by Its Label (From `softwareupdate -l`):**

```bash
sudo softwareupdate -i "[label]"
```

**Install All Available Updates & Reboot Automatically:**

```bash
sudo softwareupdate -iaR
```

**Show Previously Installed Updates:**

```bash
softwareupdate --history
```

**List Full macOS Installers Available to Download:**

```bash
softwareupdate --list-full-installers
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

**Install Rosetta 2 (Run Intel Apps on Apple Silicon):**

```bash
softwareupdate --install-rosetta --agree-to-license
```

---

## 2. Hardware Information

**Model, Chip, Memory, Serial Number & Activation Lock Status:**

```bash
system_profiler SPHardwareDataType
```

**Query Hardware, Software & NVMe Storage Profiles Together:**

```bash
system_profiler SPSoftwareDataType SPHardwareDataType SPNVMeDataType
```

**Chip Name:**

```bash
sysctl -n machdep.cpu.brand_string
```

**Performance and Efficiency Core Counts (Apple Silicon):**

```bash
sysctl hw.perflevel0.physicalcpu hw.perflevel1.physicalcpu
```

`perflevel0` is the performance cores; `perflevel1` is the efficiency cores.

**Installed Memory in GB:**

```bash
echo "$(( $(sysctl -n hw.memsize) / 1024 / 1024 / 1024 )) GB"
```

**Displays, Resolutions & GPU Cores:**

```bash
system_profiler SPDisplaysDataType
```

**Connected USB Devices (`SPUSBHostDataType` on macOS 15 and Later):**

```bash
system_profiler SPUSBHostDataType 2>/dev/null || system_profiler SPUSBDataType
```

**Thunderbolt / USB4 Devices & Link Speeds:**

```bash
system_profiler SPThunderboltDataType
```

**Bluetooth Controller & Paired Devices (Including Their Battery Levels):**

```bash
system_profiler SPBluetoothDataType
```

**List Every `system_profiler` Report Type:**

```bash
system_profiler -listDataTypes
```

**Save a Full Hardware Report for Support:**

```bash
system_profiler -detailLevel basic > ~/Desktop/mac-report.txt
```

---

## 3. Memory & CPU Usage

**Memory Pressure (The Number Activity Monitor's Graph Is Based On):**

```bash
memory_pressure
```

**Page-Level Memory Statistics:**

```bash
vm_stat
```

**Swap Usage:**

```bash
sysctl vm.swapusage
```

**One-Shot Summary of CPU Load and Memory Use:**

```bash
top -l 1 -s 0 | head -n 12
```

**Top Processes by CPU (Live, Press `q` to Quit):**

```bash
top -o cpu
```

**Top Processes by Memory:**

```bash
top -o mem
```

**Monitor Apple Silicon CPU/GPU/ANE Power & Thermal Pressure (Live CLI):**

```bash
sudo powermetrics --samplers cpu_power,gpu_power,ane_power,thermal -i 1000 -n 1
```

---

## 4. Battery

**Current Charge, Charging State & Time Remaining:**

```bash
pmset -g batt
```

**Watch the Battery Percentage Update Every 30 Seconds:**

```bash
while true; do pmset -g batt | grep -o "[0-9]*%.*"; sleep 30; done
```

**Cycle Count, Condition & Maximum Capacity (Battery Health):**

```bash
system_profiler SPPowerDataType | grep -E "Cycle Count|Condition|Maximum Capacity"
```

**Full Battery Report (Charger Wattage, Serial Number, Firmware):**

```bash
system_profiler SPPowerDataType
```

**Raw Battery Data from the Battery Controller:**

```bash
ioreg -rn AppleSmartBattery | grep -E '"(CycleCount|DesignCapacity|AppleRawMaxCapacity|AppleRawCurrentCapacity|NominalChargeCapacity|Temperature|IsCharging|ExternalConnected|FullyCharged)" ='
```

**Calculate Battery Health as a Percentage of Design Capacity:**

```bash
ioreg -rn AppleSmartBattery | awk -F' = ' '/^ *"AppleRawMaxCapacity" = /{m=$2} /^ *"DesignCapacity" = /{d=$2} END{printf "Battery health: %.1f%% (%d of %d mAh)\n", m/d*100, m, d}'
```

**Battery Temperature in °C:**

```bash
ioreg -rn AppleSmartBattery | awk -F' = ' '/^ *"Temperature" = /{printf "%.1f °C\n", $2/100}'
```

**Connected Charger Details (Wattage, Family, Serial):**

```bash
pmset -g ac
```

**Battery & Charging History (Charge Level at Each Sleep and Wake):**

```bash
pmset -g log | grep -E "Using (AC|Batt)" | tail -n 20
```

**Turn Low Power Mode On or Off (All Power Sources):**

```bash
sudo pmset -a lowpowermode 1
sudo pmset -a lowpowermode 0
```

**Turn Low Power Mode On Only When on Battery:**

```bash
sudo pmset -b lowpowermode 1
```

### Reading the Battery Numbers

| Value | Meaning |
| --- | --- |
| `Cycle Count` | One cycle = 100% of capacity used, spread over any number of charges. Recent MacBooks are rated for 1,000 cycles, and the battery is designed to keep up to 80% of its capacity at that count |
| `Maximum Capacity` | Battery health: how much charge it holds compared with when it was new |
| `Condition` | `Normal`, or `Service Recommended` when macOS thinks the battery needs replacing |
| `Temperature` | Reported in hundredths of °C (`3050` = 30.5 °C) |
| `ExternalConnected` | `Yes` when a charger is plugged in, even if it isn't charging |

Charging to a fixed limit (for example 80%) isn't available as a built-in command. Use **System Settings → Battery → Battery Health → Optimized Battery Charging**, or a third-party app such as AlDente.

---

## 5. Power & Sleep Settings

`pmset` flags choose which power source a setting applies to: `-b` battery, `-c` charger, `-a` all.

**Show Current Power Settings:**

```bash
pmset -g
```

**Show Settings for Battery and Charger Separately:**

```bash
pmset -g custom
```

**Set Display Sleep (Minutes) on Battery and on Charger:**

```bash
sudo pmset -b displaysleep 5
sudo pmset -c displaysleep 15
```

**Set System Sleep (Minutes; `0` = Never) on Charger:**

```bash
sudo pmset -c sleep 0
```

**Disable Power Nap on Battery:**

```bash
sudo pmset -b powernap 0
```

**Stop Network Activity While Asleep on Battery (Saves Battery; Breaks Find My While Asleep):**

```bash
sudo pmset -b tcpkeepalive 0
```

**Sleep the Mac Immediately:**

```bash
pmset sleepnow
```

**Turn Off the Display Immediately (Locks the Screen if a Password Is Required):**

```bash
pmset displaysleepnow
```

**Check Active Power Assertions (Find What Is Preventing Sleep):**

```bash
pmset -g assertions
```

**See Why the Mac Last Woke Up or Went to Sleep:**

```bash
pmset -g log | grep -E "Wake from|Entering Sleep|DarkWake" | tail -n 20
```

**Schedule a Daily Wake or Power-On on Weekdays at 08:00:**

```bash
sudo pmset repeat wakeorpoweron MTWRF 08:00:00
```

**Show and Cancel Scheduled Power Events:**

```bash
pmset -g sched
sudo pmset repeat cancel
```

**Restore Default Power Settings:**

```bash
sudo pmset restoredefaults
```

**Prevent System & Display Sleep Indefinitely (Press `Ctrl+C` to Stop):**

```bash
caffeinate -di
```

**Prevent Sleep for One Hour:**

```bash
caffeinate -i -t 3600
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

## 6. Thermals

**Thermal Warning Level and CPU Speed Limit:**

```bash
pmset -g therm
```

**Live Thermal Pressure (Nominal, Fair, Serious, Critical):**

```bash
sudo powermetrics --samplers thermal -i 2000
```

**Log of Thermal Throttling Events:**

```bash
pmset -g thermlog
```

---

## 7. Disks & APFS

**List All Disks, Partitions, and APFS Containers:**

```bash
diskutil list
```

**Details for One Disk or Volume (Format, Size, Free Space, SMART Status):**

```bash
diskutil info /
```

**Free Space on All Mounted Volumes:**

```bash
df -h
```

**Largest Folders in Your Home Directory:**

```bash
du -sh ~/* 2>/dev/null | sort -rh | head -n 15
```

**List APFS Volumes & Storage Pool Usage:**

```bash
diskutil apfs list
```

**List APFS Snapshots on a Volume:**

```bash
diskutil apfs listSnapshots /
```

**Verify APFS Volume Integrity:**

```bash
diskutil verifyVolume /
```

**Repair an External Volume (Run First Aid):**

```bash
diskutil repairVolume /Volumes/[name]
```

**Unmount and Mount a Whole Disk:**

```bash
diskutil unmountDisk /dev/disk[n]
diskutil mountDisk /dev/disk[n]
```

**Eject an External Drive Safely:**

```bash
diskutil eject /dev/disk[n]
```

**Erase an External Disk as APFS (Destroys All Data on It):**

```bash
diskutil eraseDisk APFS [NewName] GPT /dev/disk[n]
```

**Erase an External Disk as exFAT (Readable on Windows and Linux):**

```bash
diskutil eraseDisk ExFAT [NEWNAME] GPT /dev/disk[n]
```

Run `diskutil list` first and double-check the disk number. `disk0` is the internal drive.

**Internal SSD Health (Install `smartmontools` with Homebrew First):**

```bash
smartctl -a disk0
```

---

## 8. Disk Images (`hdiutil`)

**Create an Empty 1 GB APFS Disk Image:**

```bash
hdiutil create -size 1g -fs APFS -volname [Name] ~/Desktop/[name].dmg
```

**Create a Disk Image from a Folder:**

```bash
hdiutil create -srcfolder ~/[folder] ~/Desktop/[folder].dmg
```

**Create an Encrypted Disk Image (Prompts for a Password):**

```bash
hdiutil create -size 1g -fs APFS -encryption AES-256 -volname [Name] ~/Desktop/[name].dmg
```

**Mount and Unmount a Disk Image:**

```bash
hdiutil attach ~/Desktop/[name].dmg
hdiutil detach /Volumes/[Name]
```

**Verify a Downloaded Disk Image:**

```bash
hdiutil verify ~/Downloads/[file].dmg
```

---

## 9. Time Machine

**Current Backup Status and Progress:**

```bash
tmutil status
```

**Start and Stop a Backup:**

```bash
tmutil startbackup
tmutil stopbackup
```

**Show Backup Destinations:**

```bash
tmutil destinationinfo
```

**Show the Most Recent Backup and List All Backups:**

```bash
tmutil latestbackup
tmutil listbackups
```

**Exclude a Folder from Backups:**

```bash
tmutil addexclusion ~/[folder]
```

**Check Whether a Path Is Excluded:**

```bash
tmutil isexcluded ~/[folder]
```

**Create a Local APFS Snapshot Now:**

```bash
tmutil localsnapshot
```

**List Local Time Machine APFS Snapshots:**

```bash
tmutil listlocalsnapshots /
```

**Delete a Specific Local APFS Snapshot:**

```bash
sudo tmutil deletelocalsnapshots [snapshot_date]
```

**Free Up Space Held by Local Snapshots (Request 20 GB, Highest Urgency):**

```bash
sudo tmutil thinlocalsnapshots / 20000000000 4
```

---

## 10. Quick Reference

```bash
sw_vers                                         # macOS version
softwareupdate -l                               # available updates
system_profiler SPHardwareDataType              # model, chip, memory, serial
memory_pressure                                 # memory pressure
pmset -g batt                                   # battery charge
system_profiler SPPowerDataType | grep -E "Cycle|Condition|Maximum"   # battery health
pmset -g ac                                     # charger details
pmset -g assertions                             # what prevents sleep
caffeinate -di                                  # keep awake
pmset -g therm                                  # thermal throttling
diskutil list                                   # disks
tmutil status                                   # Time Machine status
```

---

## Sources & Verification

* **macOS release notes:** [Apple Developer](https://developer.apple.com/documentation/macos-release-notes)
* **Battery cycle counts and health:** [Apple Support — Determine battery cycle count](https://support.apple.com/en-us/102888)
* **Built-in manual pages:** run `man <command>` (for example `man pmset`, `man tmutil`, `man hdiutil`)

## Related guides

* [macOS Command-Line Reference (Apple Silicon)](macos-command-line-reference.md)
* [macOS Homebrew Cheat Sheet](macos-homebrew-cheat-sheet.md)
* [macOS Networking Cheat Sheet](macos-networking-cheat-sheet.md)
* [macOS launchd, Processes and Logs Cheat Sheet](macos-launchd-and-logs-cheat-sheet.md)
* [macOS Security Cheat Sheet](macos-security-cheat-sheet.md)
* [macOS defaults, Finder and CLI Tips Cheat Sheet](macos-defaults-and-cli-tips-cheat-sheet.md)
