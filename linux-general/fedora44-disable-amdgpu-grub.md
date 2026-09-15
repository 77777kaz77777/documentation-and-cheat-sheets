# Fedora 44: Blacklisting AMDGPU via GRUB (ASUS ROG Zephyrus G15)

## Objective

Disable the integrated AMD GPU at the OS level by adding the `amdgpu` module to the GRUB bootloader blacklist. This ensures the system relies exclusively on the dedicated NVIDIA GPU.

## Prerequisites

* Root/sudo privileges.
* Terminal access.

## Procedure

### 1. Edit the GRUB Configuration

Open the GRUB default configuration file in a text editor:

```bash
sudo nano /etc/default/grub
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
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

### 5. Reboot and Verify

Restart the system to apply the boot parameter changes.

Once logged in, open the terminal and run the following command to verify the module is disabled:

```bash
lsmod | grep amdgpu
```

If the command returns no output (a blank line), the AMD GPU driver has been successfully disabled.
