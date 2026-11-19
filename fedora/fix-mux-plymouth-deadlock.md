# How to fix boot deadlocks caused by MUX switches and Plymouth

**Symptoms:** after switching the GPU MUX (e.g. to dedicated/dGPU-only mode), the laptop hangs at the boot splash or a black screen and never shows the LUKS passphrase prompt. The graphical splash (Plymouth) can't drive the display in that mode, so boot waits forever.

To force text mode and bypass the MUX/Plymouth deadlock, edit the GRUB parameters directly from the boot selection screen. This edit only applies to **this one boot**; nothing is saved.

## Step 1: Modify Kernel Parameters

1. **Locate the line:** Use the keyboard arrow keys to move the cursor down to the line starting with `linux`.
2. **Remove graphical flags:** Move the cursor across the line to find `rhgb quiet`. Use **Backspace** or **Delete** to remove both `rhgb` and `quiet`.
3. **Set text mode:** Move the cursor to the very end of that same `linux` line (after `modprobe.blacklist=nouveau,nova_core`). Add a space, then type `3`. This forces plain text mode so the LUKS passphrase prompt displays correctly.

## Step 2: Boot the System

- Press **Ctrl + X** (or **F10**) to boot using these temporary parameters.
- Enter your LUKS passphrase when prompted and log in to the text terminal.

## Step 3: Reconfigure GPU MUX & Reboot

Run **one** of the following commands based on your installed utilities:

- **Using `supergfxctl`:**

  ```bash
  supergfxctl -m Hybrid
  ```

- **Using `cardwire`** (see the [ASUS ROG setup guide](asus-rog-fedora-setup.md)):

  ```bash
  cardwire set hybrid
  ```

Then reboot. With the MUX back in hybrid mode, the normal graphical boot and passphrase prompt return:

```bash
sudo reboot
```

## Optional: always boot in text mode

If you switch to dedicated mode often, you can drop the splash permanently so this can't happen again:

```bash
sudo grubby --update-kernel=ALL --remove-args="rhgb quiet"
```

To bring the splash back later:

```bash
sudo grubby --update-kernel=ALL --args="rhgb quiet"
```

## Related guides

- [Install NVIDIA Drivers on Fedora (RPM Fusion)](fedora-nvidia-installation-guide.md)
- [Troubleshooting: dracut-install Failed to find module 'nvidia'](troubleshooting-dracut-nvidia-module-error.md)
- [Disable the Integrated AMD GPU on Fedora (GRUB Blacklist)](../linux-general/hardware-and-firmware/disable-amdgpu-grub.md)
- [ASUS ROG Zephyrus G15 Setup Guide for Fedora KDE](asus-rog-fedora-setup.md)
- [NVIDIA GPU and CUDA Monitoring Cheat Sheet](../linux-general/nvidia-cuda-monitoring-cheat-sheet.md)
