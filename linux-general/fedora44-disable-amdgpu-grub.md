## instructions for disabling the integrated AMD GPU on Fedora 44 by blacklisting the amdgpu module in the GRUB bootloader, ensuring the system relies exclusively on the dedicated NVIDIA GPU. It also includes troubleshooting steps using grubby and dracut to resolve issues where Boot Loader Specification (BLS) files retain outdated kernel parameters

Disable the integrated AMD GPU at the OS level by adding the `amdgpu` module to the GRUB bootloader blacklist. This ensures the system relies exclusively on the dedicated NVIDIA GPU.

## Prerequisites

* Root/sudo privileges.
* Terminal access.

## Procedure

### 1. Edit the GRUB Configuration

Open the GRUB default configuration file in a text editor:

```bash
sudo nano \
  /etc/default/grub
```

### 2. Append to the Blacklist

Locate the line starting with `GRUB_CMDLINE_LINUX=`.
Append `amdgpu` to the existing comma-separated lists for both `rd.driver.blacklist` and `modprobe.blacklist`.

**Example line modification:**
Ensure the end of the line looks like this before the closing quote:

```text
GRUB_CMDLINE_LINUX="... rd.driver.blacklist=nouveau,nova_core,amdgpu modprobe.blacklist=nouveau,nova_core,amdgpu"
```

### 3. Save and Exit (Nano)

1. Press `Ctrl + O` to save.
2. Press `Enter` to confirm the file name.
3. Press `Ctrl + X` to exit the editor.

### 4. Rebuild the GRUB Configuration

Apply the changes to the bootloader by generating a new GRUB configuration file:

```bash
sudo grub2-mkconfig \
  -o \
  /boot/grub2/grub.cfg
```

### 5. Reboot and Verify

Restart the system to apply the boot parameter changes.

Once logged in, open the terminal and run the following command to verify the module is disabled:

```bash
lsmod \
  | grep amdgpu
```

If the command returns no output (a blank line), the AMD GPU driver has been successfully disabled.

---

## Troubleshooting: Kernel Still Booting with AMDGPU Blacklisted Post Fix Release

If your `/etc/default/grub` file is clean and does not contain `amdgpu` in the blacklist string, the reason kernel 7.2.5 still boots with `amdgpu` blacklisted is that Fedora uses BLS (Boot Loader Specification). Individual boot entries in `/boot/loader/entries/` store their own kernel command line arguments. If `amdgpu` was blacklisted when kernel 7.2.5 was installed, editing `/etc/default/grub` afterwards does not automatically update that specific kernel's BLS file.

To fix this across all kernel boot entries on Fedora, use `grubby`:

### 1. Remove the Blacklist Argument Across All Kernels

Run `grubby` to strip the `amdgpu` blacklist argument from all existing BLS boot entries at once:

```bash
sudo grubby \
  --update-kernel=ALL \
  --remove-args="modprobe.blacklist=nouveau,nova_core,amdgpu" \
  --args="modprobe.blacklist=nouveau,nova_core"
```

**Verification:** Run the following command and verify `amdgpu` is no longer present in any kernel command line:

```bash
sudo grubby \
  --info=ALL \
  | grep args
```

### 2. Regenerate GRUB and Update Initramfs

Regenerate your GRUB configuration and rebuild the initramfs images to ensure the updated firmware and modprobe rules are embedded into the early boot environment:

```bash
sudo grub2-mkconfig \
  -o \
  /boot/grub2/grub.cfg

sudo dracut \
  --regenerate-all \
  --force
```

**Verification:** Both commands complete with success status messages and no dracut build errors.

### 3. Reboot into Kernel 7.2.5

Reboot the system so the new kernel parameters and firmware load from stage 1 boot:

```bash
systemctl \
  reboot
```

**Verification:** The system boots cleanly to the KDE Plasma login screen. Once logged in, the following command will show active initialization logs for your integrated GPU:

```bash
sudo dmesg \
  | grep -i "amdgpu"
```
