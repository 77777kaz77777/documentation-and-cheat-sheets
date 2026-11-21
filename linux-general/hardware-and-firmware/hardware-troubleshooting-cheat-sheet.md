# Linux Hardware Troubleshooting Cheat Sheet

Quick-reference guide for identifying hardware, reading error logs, and testing components on Linux.

Work from the outside in: **identify** the device, **check the kernel log** for errors, **confirm the driver and firmware** are loaded, then **stress-test** the component you suspect. Most commands below need `sudo` to show complete information.

---

## 1. Install the Diagnostic Tools

```bash
# RHEL / Fedora / Rocky
sudo dnf install pciutils usbutils lshw dmidecode lm_sensors smartmontools nvme-cli stress-ng memtester inxi

# Debian / Ubuntu
sudo apt install pciutils usbutils lshw dmidecode lm-sensors smartmontools nvme-cli stress-ng memtester inxi

# Arch Linux
sudo pacman -S pciutils usbutils lshw dmidecode lm_sensors smartmontools nvme-cli stress-ng memtester inxi
```

`inxi` is in EPEL on RHEL and Rocky Linux. Enable EPEL first, or skip it.

---

## 2. Identify the Hardware

### Full System Summary

```bash
# Readable overview of CPU, GPU, drives, network, sensors
inxi -Fxz

# Detailed hardware tree; -short gives a compact table
sudo lshw -short

# Save a full HTML report to share or compare later
sudo lshw -html > hardware-report.html
```

`inxi -z` hides serial numbers and MAC addresses, so the output is safe to paste into forum posts.

### Motherboard, BIOS & Memory Modules (DMI/SMBIOS)

```bash
# Vendor, model, BIOS version
sudo dmidecode -t system -t bios

# Installed RAM sticks, sizes, speeds and slots
sudo dmidecode -t memory | grep -E "Size|Speed|Locator|Part Number" | grep -v "No Module"

# BIOS version without dmidecode
cat /sys/class/dmi/id/bios_version
```

### CPU

```bash
lscpu
grep -c ^processor /proc/cpuinfo
grep -m1 "model name" /proc/cpuinfo
```

### PCI Devices (GPU, Network, NVMe, Wi-Fi)

```bash
# List all PCI devices with the kernel driver in use
lspci -k

# Show vendor:device IDs (useful for searching driver support)
lspci -nn

# One device in full detail, including link speed (replace the address)
sudo lspci -vvv -s 01:00.0
```

Check `LnkSta` in the `-vvv` output. A GPU or NVMe drive running at a lower PCIe speed or width than `LnkCap` usually means a bad slot, riser, or BIOS setting.

### USB Devices

```bash
# Devices with vendor:product IDs
lsusb

# Tree view with speeds and drivers
lsusb -t

# Watch devices connect and disconnect live
sudo udevadm monitor --udev
```

### Block Devices

```bash
lsblk -o NAME,MODEL,SERIAL,SIZE,TYPE,TRAN,MOUNTPOINTS
```

---

## 3. Read the Kernel Log

Hardware faults almost always leave a trace in the kernel log.

```bash
# Errors and worse from the current boot
sudo journalctl -k -p err -b

# Same, from the previous boot (after a crash or freeze)
sudo journalctl -k -p err -b -1

# Follow live while you reproduce the problem
sudo journalctl -kf

# dmesg with readable timestamps, warnings and errors only
sudo dmesg -T --level=err,warn
```

Reading logs from a previous boot needs a persistent journal. Create it if `journalctl --list-boots` shows only one boot:

```bash
sudo mkdir -p /var/log/journal && sudo systemctl restart systemd-journald
```

### What to Search For

```bash
sudo journalctl -k -b | grep -iE "error|fail|timeout|reset|mce|hardware error|i/o error|firmware"
```

| Log message | Usually points to |
| --- | --- |
| `Machine check events logged` / `mce:` | CPU, RAM, or motherboard fault |
| `EDAC ... CE` / `UE` | Corrected / uncorrected memory errors (ECC RAM) |
| `I/O error, dev sdX` / `blk_update_request` | Failing drive, cable, or controller |
| `ata1: hard resetting link` / `SATA link down` | Loose or bad SATA cable, port, or power |
| `nvme nvme0: I/O ... timeout` / `controller is down` | NVMe drive, power state, or firmware issue |
| `PCIe Bus Error` / `AER: Corrected error` | PCIe link problem (slot, riser, ASPM) |
| `usb X-Y: device descriptor read/64, error -71` | USB cable, hub, or under-powered port |
| `Direct firmware load for ... failed` | Missing firmware package |
| `thermal ... critical temperature reached` | Overheating and emergency shutdown |
| `watchdog: BUG: soft lockup` / `hard LOCKUP` | Driver hang, overheating, or unstable CPU/RAM |
| `Out of memory: Killed process` | Not hardware: RAM exhausted by software |

---

## 4. Drivers & Firmware

```bash
# Which driver each PCI device uses
lspci -k | grep -A3 -iE "vga|3d|network|ethernet|nvme"

# Is a module loaded?
lsmod | grep -i <module>

# Module details: version, firmware files, parameters
modinfo <module>

# Reload a driver (device must not be in use)
sudo modprobe -r <module> && sudo modprobe <module>

# Missing firmware messages
sudo journalctl -k -b | grep -i firmware

# Kernel version (driver support depends on it)
uname -r
```

Missing firmware is fixed by installing the distro's firmware package: `linux-firmware` on Fedora, RHEL, Rocky and Arch; on Debian enable the `non-free-firmware` component and install `firmware-linux`. BIOS and device firmware updates are covered in the [fwupdmgr Firmware Update Cheat Sheet](fwupdmgr-firmware-update-cheat-sheet.md).

---

## 5. Temperatures, Fans & Throttling

```bash
# Detect sensor chips once (answer the prompts; defaults are safe)
sudo sensors-detect

# Read temperatures, fan speeds and voltages
sensors

# Refresh every 2 seconds
watch -n 2 sensors

# Raw thermal zones if lm_sensors finds nothing
paste <(cat /sys/class/thermal/thermal_zone*/type) <(cat /sys/class/thermal/thermal_zone*/temp)

# Current CPU frequencies (drops under load mean throttling)
watch -n 1 "grep MHz /proc/cpuinfo"
```

Thermal zone values are in millidegrees: `65000` means 65 °C. Laptops that throttle often need cleaned fans and fresh thermal paste, not software fixes.

---

## 6. Memory (RAM)

### Quick Checks

```bash
free -h
sudo dmidecode -t memory | grep -E "Size|Speed" | grep -v "No Module"
```

### Memory Errors (ECC Systems)

`rasdaemon` collects machine check and EDAC memory errors:

```bash
sudo dnf install rasdaemon    # or: sudo apt install rasdaemon
sudo systemctl enable --now rasdaemon
sudo ras-mc-ctl --summary
sudo ras-mc-ctl --errors
```

### Test RAM

```bash
# Test 2 GB of RAM for 3 passes while the system is running
sudo memtester 2G 3
```

`memtester` can only test memory that isn't in use. For a full test, boot **Memtest86+** from the GRUB menu (installed with the `memtest86+` package on many distros) or from a USB stick, and let it run at least one complete pass. Any error at all means bad RAM, a wrong XMP/EXPO setting, or a bad slot: test one stick at a time to find it.

---

## 7. Storage Drives

```bash
# Overall SMART health (PASSED / FAILED)
sudo smartctl -H /dev/sda

# All SMART data and the error log
sudo smartctl -a /dev/sda

# Start a short self-test (about 2 minutes), then read the result
sudo smartctl -t short /dev/sda
sudo smartctl -l selftest /dev/sda

# NVMe health: media errors, spare capacity, temperature
sudo nvme smart-log /dev/nvme0n1
sudo nvme error-log /dev/nvme0n1
```

SATA attributes to watch: `Reallocated_Sector_Ct`, `Current_Pending_Sector`, `Offline_Uncorrectable`, and `UDMA_CRC_Error_Count` (cable problems). Any non-zero value that keeps rising is a warning sign. On NVMe, watch `media_errors`, `percentage_used`, and `critical_warning`.

Read-only surface scan (safe, but slow on large drives):

```bash
sudo badblocks -sv /dev/sda
```

Never run `badblocks -w` on a drive with data: write mode erases it. For more, see the [smartctl Comprehensive Cheat Sheet](../storage-and-filesystems/smartctl-cheat-sheet.md) and the [nvme-cli Cheat Sheet](../storage-and-filesystems/nvme-cli-cheat-sheet.md).

---

## 8. CPU & Stability Testing

Run stress tests in one terminal and watch `sensors` and `journalctl -kf` in another.

```bash
# Load every CPU thread for 10 minutes and print a summary
stress-ng --cpu 0 --timeout 10m --metrics-brief

# Stress RAM: 2 workers using 75% of memory, with data verification
stress-ng --vm 2 --vm-bytes 75% --verify --timeout 10m

# Combined CPU, memory and disk I/O load
stress-ng --cpu 0 --vm 2 --vm-bytes 50% --io 2 --timeout 15m
```

A freeze, reboot, or `mce`/`EDAC` messages under load point to overheating, an unstable overclock or undervolt, bad RAM, or a weak power supply.

---

## 9. GPU

```bash
# Which GPU and driver are in use
lspci -k | grep -A3 -iE "vga|3d|display"

# Renderer in use (needs mesa-utils / mesa-demos)
glxinfo -B

# Vulkan devices (needs vulkan-tools)
vulkaninfo --summary

# GPU errors in the kernel log
sudo journalctl -k -b | grep -iE "amdgpu|nouveau|nvidia|i915|xe|drm"
```

For NVIDIA, `nvidia-smi` shows temperature, power, and errors; see the [NVIDIA GPU and CUDA Monitoring Cheat Sheet](nvidia-cuda-monitoring-cheat-sheet.md). On AMD, `amdgpu_top` and `radeontop` show live load.

---

## 10. Network Hardware

```bash
# Interfaces, link state and driver
ip -br link
sudo ethtool eth0
sudo ethtool -i eth0

# NIC error and drop counters
ip -s link show eth0
sudo ethtool -S eth0 | grep -iE "err|drop|crc"

# Wi-Fi radio blocks (hardware switch or airplane mode)
rfkill list

# Wi-Fi link quality
iw dev wlan0 link
```

Rising CRC or error counters on a wired link usually mean a bad cable or port. Rising `rx_missed` or drops point to driver or ring-buffer limits rather than hardware. For Wi-Fi card problems, see the [Wi-Fi hardware replacement guide](wifi-hardware-replacement-guide.md).

---

## 11. USB & Peripherals

```bash
# Watch kernel messages while plugging the device in
sudo dmesg -Tw

# Check power management state for USB devices
grep . /sys/bus/usb/devices/*/power/control

# Disable USB autosuspend for testing (until reboot)
echo -1 | sudo tee /sys/module/usbcore/parameters/autosuspend
```

`error -71` or repeated disconnects usually mean a bad cable, hub, or a port that can't supply enough power. Try a different port (preferably directly on the motherboard) before blaming the device.

---

## 12. Power, Battery & Laptops

```bash
# Battery health: compare energy-full to energy-full-design
upower -i "$(upower -e | grep -i bat)"

# Same from sysfs
cat /sys/class/power_supply/BAT0/{energy_full,energy_full_design} 2>/dev/null

# Suspend and resume problems from the previous boot
sudo journalctl -b -1 | grep -iE "suspend|resume|PM:"

# Supported sleep states
cat /sys/power/mem_sleep
```

Battery health is `energy_full ÷ energy_full_design`. Below about 80% means the battery has noticeably worn. Some batteries report `charge_full` instead of `energy_full`.

---

## 13. Crashes & Freezes

| Symptom | Where to look |
| --- | --- |
| Random reboots, no log entries | Power supply, overheating, or RAM. If `journalctl -b -1` just stops with no error, suspect power or heat; run Memtest86+ and `stress-ng` |
| Freeze under load | Temperatures with `sensors`; `journalctl -k -b -1` for lockups or GPU resets |
| Freeze at idle or on resume | Power states: try kernel parameters such as `pcie_aspm=off` or `nvme_core.default_ps_max_latency_us=0` one at a time |
| Kernel panic | `journalctl -k -b -1`; set up `kdump` to capture a crash dump |
| Device works on Windows, not Linux | Missing driver or firmware (Section 4); newer kernel may be needed |

### Useful Kernel Parameters for Testing

Add one at a time to the kernel command line and remove it if it doesn't help:

```bash
# Fedora / RHEL / Rocky
sudo grubby --update-kernel=ALL --args="pcie_aspm=off"
sudo grubby --update-kernel=ALL --remove-args="pcie_aspm=off"
```

On Debian, Ubuntu and Arch, edit `GRUB_CMDLINE_LINUX_DEFAULT` in `/etc/default/grub`, then run `sudo update-grub` (Debian/Ubuntu) or `sudo grub-mkconfig -o /boot/grub/grub.cfg` (Arch).

| Parameter | Use when |
| --- | --- |
| `pcie_aspm=off` | PCIe AER errors, NVMe or Wi-Fi dropping out |
| `nvme_core.default_ps_max_latency_us=0` | NVMe drive disappears or times out |
| `nomodeset` | Black screen at boot with a new GPU (temporary only) |
| `acpi_osi=Linux` / `acpi_osi=!` | Some laptop ACPI quirks (brightness, battery, sleep) |

---

## 14. Collect a Report for Support

```bash
# Anonymised summary for forum posts
inxi -Fxz > inxi.txt

# Kernel log from this boot
sudo journalctl -k -b > kernel.log

# PCI and USB device lists with drivers
lspci -nnk > lspci.txt && lsusb > lsusb.txt
```

Before sharing, check the files for serial numbers, MAC addresses, and hostnames you don't want public.

---

## 15. Quick Reference

```bash
inxi -Fxz                          # system summary
lspci -k                           # PCI devices and drivers
lsusb -t                           # USB tree
sudo dmidecode -t memory           # RAM sticks
sudo journalctl -k -p err -b       # kernel errors, this boot
sudo journalctl -k -p err -b -1    # kernel errors, last boot
sensors                            # temperatures and fans
sudo smartctl -H /dev/sda          # SATA drive health
sudo nvme smart-log /dev/nvme0n1   # NVMe health
sudo memtester 2G 1                # quick RAM test
stress-ng --cpu 0 --timeout 10m    # CPU stress test
sudo ras-mc-ctl --summary          # logged hardware errors
rfkill list                        # radio blocks
upower -i "$(upower -e | grep -i bat)"  # battery health
```

---

## Related guides

- [smartctl Comprehensive Cheat Sheet](../storage-and-filesystems/smartctl-cheat-sheet.md)
- [nvme-cli Cheat Sheet](../storage-and-filesystems/nvme-cli-cheat-sheet.md)
- [NVMe Unsafe Shutdown Troubleshooting Guide](../storage-and-filesystems/nvme-troubleshooting-guide.md)
- [systemd and journalctl Cheat Sheet](../system-administration/systemd-journalctl-cheat-sheet.md)
- [fwupdmgr Firmware Update Cheat Sheet](fwupdmgr-firmware-update-cheat-sheet.md)
- [NVIDIA GPU and CUDA Monitoring Cheat Sheet](nvidia-cuda-monitoring-cheat-sheet.md)
- [Comprehensive Post-Wi-Fi Hardware Replacement Diagnostic Guide](wifi-hardware-replacement-guide.md)
