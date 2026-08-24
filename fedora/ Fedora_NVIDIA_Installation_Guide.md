## Description

The recommended, most stable way to install NVIDIA drivers on Fedora Workstation is through the **RPM Fusion** repositories. Using the official `.run` installer directly from NVIDIA is strongly discouraged on Fedora because kernel updates will frequently break the display driver.

Below is the complete installation process.
---

## Step 1: Update System & Enable Repositories

First, ensure your system is completely up-to-date and enable the **RPM Fusion Non-Free** repository.

```bash
# Update existing system packages
sudo dnf \
  update \
  -y
```

```bash
# Enable RPM Fusion Free and Non-Free repositories
sudo dnf \
  install \
  -y \
  [https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm](https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm) -E %fedora).noarch.rpm \
  [https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm](https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm) -E %fedora).noarch.rpm
```

```bash
# Enable RPM Fusion AppStream metadata
sudo dnf \
  group \
  update \
  core \
  -y
```

*(If you updated your kernel in this step, reboot your system before proceeding: `sudo reboot`)*

---

## Step 2: Handle Secure Boot (Skip if Disabled)

If **Secure Boot** is enabled in your system's UEFI/BIOS settings, Linux will block unsigned driver modules from loading. You must generate and enroll a Machine Owner Key (MOK) **before** installing the drivers.

### 1. Generate the signing key:

```bash
sudo dnf \
  install \
  -y \
  kmodtool \
  akmods \
  mokutil \
  openssl
```

```bash
sudo kmodgenca \
  -a
```

### 2. Import the key into MOK:

```bash
sudo mokutil \
  --import \
  /etc/pki/akmods/certs/public_key.der
```

*You will be prompted to create a password. Remember this password.*

### 3. Reboot to complete MOK enrollment:

```bash
sudo reboot
```

*During boot, a blue screen (Shim UEFI Key Management / MOK Manager) will appear. Select **Enroll MOK** -> **Continue** -> **Yes**, enter the password you just set, and let the system reboot.*

---

## Step 3: Install NVIDIA Driver & CUDA Support

Once back in Fedora, install the main driver package along with CUDA and video acceleration support:

```bash
# Install the core driver package
sudo dnf \
  install \
  -y \
  akmod-nvidia
```

```bash
# Install CUDA / NVENC / NVDEC libraries (Recommended for gaming & compute)
sudo dnf \
  install \
  -y \
  xorg-x11-drv-nvidia-cuda
```

---

## Step 4: Wait for Kernel Module Compilation & Reboot

Fedora uses `akmods` to automatically build the NVIDIA kernel module in the background for your current kernel.

1. **Do not reboot immediately.** Wait a few minutes for the module compilation to complete.
2. Check if the module build has finished by running:

```bash
modinfo \
  -F \
  version \
  nvidia
```

If it returns a version number (e.g., `555.58.02` or similar), the compilation is complete. If it says `module nvidia not found`, wait another 1–2 minutes and run the command again.

3. Once verified, reboot your machine:

```bash
sudo reboot
```

---

## Step 5: Verification

After rebooting, verify that the driver is loaded properly using the NVIDIA System Management Interface:

```bash
nvidia-smi
```

If successful, this will output a table showing your GPU model, driver version, CUDA version, and active GPU processes.

---

## Sources & Verification

- **Source:** Verified against the official [RPM Fusion NVIDIA HowTo Guide](https://rpmfusion.org/Howto/NVIDIA). The commands provided correctly map to the standard deployment procedure for NVIDIA drivers on Fedora using `akmods`.
