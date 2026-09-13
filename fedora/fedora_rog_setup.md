## This document outlines the configurations applied by `fedora_rog_setup.sh` for optimizing the ASUS ROG Zephyrus G15 on Fedora 44 KDE. It manages graphics switching, daemon integration, and power profile adjustments required for stable desktop performance and battery management

## System Prerequisites & Core Dependencies

* A minimum Linux kernel version of `>= 6.19` is recommended to ensure all patches that drastically improve the Linux experience on an ASUS/ROG laptop are available .
* The script relies on `asusctl` and `supergfxctl`, which are officially supported and packaged for Fedora Workstation .
* To ensure proper functionality, any distro-provided methods of graphics switching (like `envycontrol`) must be removed prior to configuration .

## Graphics Driver & GPU Management (`supergfxctl`)

The script sets up `supergfxctl` to manage the NVIDIA dGPU and AMD iGPU power states.

* Install NVIDIA proprietary drivers using `sudo dnf install akmod-nvidia xorg-x11-drv-nvidia-cuda` .
* You must wait after the RPM transaction ends to allow the kmod to be built; this can take up to 5 minutes on older systems and about 2 minutes on newer systems .
* `supergfxctl` allows switching between `Hybrid` (dGPU offload), `Integrated` (forces dGPU off), and `Vfio` (binds dGPU for VM pass-through) modes .
* **Xorg Support:** Xorg is no longer officially supported by `supergfxctl`, though `supergfxd` may still function with it . Wayland is strongly recommended for variable refresh rate (VRR) support .
* **Reversibility/Troubleshooting:** If the rebootless GPU switch fails, you may need to force user processes to quit by editing `/etc/systemd/logind.conf` and setting `KillUserProcesses=yes` .
* **External Display Lag:** If an external display is laggy, and the USB-C port takes the signal from the iGPU, use a USB-C to HDMI/DP cable to avoid rendering two screens on separate GPUs .

## Power Profiles & Fan Curves (`asusctl`)

Power distribution and thermal management are strictly handled by `asusctl`.

* `asusctl` maps directly to power-profiles-daemon, meaning custom CPU turbo or frequency adjustments via `asusctl` are disabled in favor of standardized desktop profiles .
* You can manually apply the maximum performance profile using the command `asusctl profile -P Performance` .
* Custom fan curves can be applied directly to the CPU and GPU via the command line .
* For example, a CPU fan curve can be set using `asusctl fan-curve -m "balanced" -f cpu -D "20c:0%,40c:0%,50c:0%,60c:5%,70c:15%,80c:40%,90c:70%,100c:80%"` .
* **Reversibility/Troubleshooting:** Custom fan profiles can be immediately disabled using `asusctl fan-curve -m -e false` .
* To restore factory default fan curves for your active power profile, the underlying kernel `pwm_enable` flag can be set to option `3` .

## Hardware Quirks & ACPI Fixes (Zephyrus G15)

Specific fixes are applied based on the hardware generation of the Zephyrus G15.

* **2022 Models:** Ensure the system BIOS is updated past version `313` . ASUS fixed ACPI support for Linux in this release, resolving power distribution issues that caused stuttering in performance mode .
* **2021 Models (Suspend Issues):** Using a secondary NVMe drive on 2021 models can break `s0ix` (s2idle) suspend . This requires a DSDT table patch on older kernels, but is fixed natively in kernel versions `6.1.x` and up .
* **S3 Sleep Fallback:** If `s0ix` fails completely, you must patch your DSDT tables to force the legacy S3 suspend method . This is a manual process and cannot be integrated directly into the kernel . If you update your BIOS after applying an S3 patch, you must disable the old DSDT table and create a new one .
