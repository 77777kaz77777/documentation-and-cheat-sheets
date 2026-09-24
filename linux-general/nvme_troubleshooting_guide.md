# NVMe Unsafe Shutdown Troubleshooting Guide

## Overview
SMART data from both the Kingston (SNV2S500G) and Western Digital (WD PC SN735) NVMe drives shows excellent overall physical health (low wear, zero media errors). However, both drives have recorded an abnormally high number of **Unsafe Shutdowns** (e.g., 5,878 on the Kingston and 9,879 on the WD). 

## Root Cause: S2Idle Suspend State
An "Unsafe Shutdown" is recorded when power to the NVMe controller drops before the kernel sends a flush/shutdown command. 

Running `cat /sys/power/mem_sleep` returned `[s2idle]`, which indicates the system uses Modern Standby (Suspend-to-Idle) and the platform firmware does not expose standard ACPI S3 (`deep`) sleep to the operating system. 

During `s2idle`, the kernel suspends PCIe links while the NVMe drives are in lower Autonomous Power State Transitions (APST). Because the controller does not receive a complete power-down flush command before link teardown, it registers every sleep/wake cycle as an unsafe shutdown.

---

## Solutions

### Solution 1: Disable NVMe APST Latency Transitions (Recommended)
Disabling ultra-low power APST transitions prevents the NVMe controller from entering sleep states that fail to flush properly during `s2idle`. 

**Step 1: Apply Parameter via `grubby`**
Run the following command in the terminal to apply `nvme_core.default_ps_max_latency_us=0` across all installed kernels on Fedora:
```bash
sudo grubby --update-kernel=ALL --args="nvme_core.default_ps_max_latency_us=0"
```

**Step 2: Update `/etc/default/grub`**
To ensure future kernel updates retain this setting, update your GRUB configuration file. Ensure the `GRUB_CMDLINE_LINUX` line includes the new parameter.

*Example `/etc/default/grub`:*
```text
GRUB_TIMEOUT=5
GRUB_DISTRIBUTOR="$(sed 's, release .*$,,g' /etc/system-release)"
GRUB_DEFAULT=saved
GRUB_DISABLE_SUBMENU=true
GRUB_TERMINAL_OUTPUT="console"
GRUB_CMDLINE_LINUX="rhgb quiet nvme_core.default_ps_max_latency_us=0"
GRUB_DISABLE_RECOVERY="true"
GRUB_ENABLE_BLSCFG=true
```

**Step 3: Regenerate GRUB Configuration**
Apply the changes by regenerating the GRUB config:
```bash
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

**Step 4: Reboot**
Restart your system for the changes to take effect:
```bash
sudo reboot
```

### Solution 2: Enable ACPI S3 (`deep`) in BIOS/UEFI
If you prefer traditional S3 sleep over `s2idle`, you can check if your system's motherboard firmware allows enabling it:

1. Reboot into your UEFI/BIOS setup.
2. Navigate to **Advanced** or **Power Management**.
3. Look for options labeled **"Sleep State"**, **"OS Sleep Mode"**, or **"Block Sleep State"**.
4. Change the setting from **"Windows 10 / Modern Standby"** to **"Linux / S3"** (or similar).
5. Save changes and boot back into the OS.

To verify if `deep` sleep is now available, run:
```bash
cat /sys/power/mem_sleep
```
*Expected output if successful:* `s2idle [deep]`

---

## Verification
To verify that the kernel parameter was successfully applied after rebooting, run:
```bash
cat /sys/module/nvme_core/parameters/default_ps_max_latency_us
```
*Expected output:* `0`