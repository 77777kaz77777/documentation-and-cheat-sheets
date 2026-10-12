# How to fix boot deadlocks caused by MUX switches and Plymouth

To force text mode and bypass the MUX/Plymouth deadlock, edit the GRUB parameters directly from the boot selection screen:

## Step 1: Modify Kernel Parameters

1. **Locate the line:** Use the keyboard arrow keys to move the cursor down to the line starting with `linux`.
2. **Remove graphical flags:** Move the cursor across the line to find `rhgb quiet`. Use **Backspace** or **Delete** to remove both `rhgb` and `quiet`.
3. **Set text mode:** Move the cursor to the very end of that same `linux` line (after `modprobe.blacklist=nouveau,nova_core`). Add a space, then type `3`. This forces plain text mode so the LUKS passphrase prompt displays correctly.

## Step 2: Boot the System

* Press **Ctrl + X** (or **F10**) to boot using these temporary parameters.
* Enter your LUKS passphrase when prompted and log in to the text terminal.

## Step 3: Reconfigure GPU MUX & Reboot

Run **one** of the following commands based on your installed utilities:

* **Using `supergfxctl`:**

  ```bash
  supergfxctl -m Hybrid
