# Troubleshooting: dracut-install Failed to find module 'nvidia'

This error occurs during a kernel update or initramfs rebuild because `dracut` is explicitly instructed to include the `nvidia` kernel module in the initramfs, but that module isn't compiled or installed for the target kernel (e.g., `7.2.10-200.fc44.x86_64`).

This typically happens on Fedora when using RPM Fusion Nvidia drivers if the `akmods` background service hasn't finished compiling the kernel module for the newly installed kernel yet, or if a custom dracut configuration is forcing the module load.

Here is how to resolve this, starting from the simplest and most common fix.

## Method 1: Wait for or Force the `akmods` Kernel Module Build

If you recently updated your kernel via `dnf`, the Nvidia driver module builds in the background via `akmods`. If you rebuild initramfs before `akmods` finishes, `dracut` will throw this exact error.

1. Trigger the module compilation manually to check if it completes or fails:

   ```bash
   sudo akmods --force
   ```

2. Once `akmods` finishes without errors, rebuild your initramfs for the new kernel:

   ```bash
   sudo dracut --regenerate-all --force
   ```

_Verification:_ Running the `dracut` command should complete cleanly without returning any `Failed to find module 'nvidia'` output.

---

## Method 2: Check Dracut Configuration Files

If you are intentionally running an open-source/integrated GPU setup (or AMD/Intel only) and do not use Nvidia drivers, an old or leftover dracut config file might be forcing `dracut` to search for `nvidia` modules that no longer exist.

1. Inspect your dracut configuration files for forced Nvidia inclusions:

   ```bash
   grep -rnw '/etc/dracut.conf.d/' -e 'nvidia'
   ```

2. If a file (such as `/etc/dracut.conf.d/nvidia.conf` or similar) contains lines like `add_drivers+=" nvidia ... "`, edit or remove that file:

   ```bash
   sudo rm /etc/dracut.conf.d/nvidia.conf
   ```

3. Rebuild the initramfs:

   ```bash
   sudo dracut --regenerate-all --force
   ```

_Verification:_ Rebuilding initramfs succeeds without attempting to pull in `nvidia` modules.

---

## Method 3: Reinstall the Akmod/Nvidia Driver Packages

If `akmods` fails during Step 1, the kmod headers or driver packages for the current kernel may be mismatched.

1. Ensure kernel headers and development packages match your current kernel:

   ```bash
   sudo dnf reinstall kernel-devel kernel-headers
   ```

2. Reinstall the RPM Fusion Nvidia driver package:

   ```bash
   sudo dnf reinstall akmod-nvidia
   ```

3. Force the build and regenerate:

   ```bash
   sudo akmods --force
   sudo dracut --regenerate-all --force
   ```
