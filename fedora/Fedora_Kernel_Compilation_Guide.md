# Document Name: Fedora_Kernel_Compilation_Guide.md

## Overview
This document provides instructions on how to manually compile the Linux kernel on Fedora (including Fedora 44 KDE). It begins with the simplest method (building a vanilla upstream kernel) and moves to more advanced configuration methods.

## 1. The Simplest Method: Building a Vanilla Upstream Kernel

### Step 1: Install Build Dependencies
To compile the kernel manually, you need standard development tools and libraries. Open your terminal and run:
```bash
sudo dnf install \
    gcc \
    make \
    git \
    ncurses-devel \
    bison \
    flex \
    elfutils-libelf-devel \
    openssl-devel \
    bc
```

### Step 2: Download the Kernel Source
Clone the mainline kernel tree directly from kernel.org. To get Linus Torvalds's tree, run:
```bash
git clone \
    git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
cd linux
```

Alternatively, if you want the stable release tree, you can add it with:
```bash
git remote add \
    -f \
    stable \
    git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git
```

### Step 3: Configure the Kernel
The simplest and most efficient way to configure a new kernel is to base it on your currently running Fedora system, disabling modules you do not currently have loaded. This will drastically reduce compilation time:
```bash
make localmodconfig
```

*(Note: Press `Enter` to accept the default answers for any new kernel features introduced since your current kernel version).*

Alternatively, if you prefer to build the kernel exactly as your current one without stripping out unused modules, you can copy the existing configuration and use oldconfig:
```bash
cp /boot/config-$(uname -r) .config
make oldconfig
```

### Step 4: Build the Kernel
Compile the kernel and its modules. By adding `-j$(nproc)`, you instruct the `make` command to use all available CPU cores, which speeds up the compilation process significantly.
```bash
make \
    -j$(nproc) \
    bzImage \
    modules
```

### Step 5: Install the Kernel
Once compilation is complete, install the modules and the kernel itself. On Fedora, the `make install` command handles copying the kernel to `/boot`, creating the initial ramdisk (`initramfs`), and updating your GRUB bootloader menu automatically.
```bash
sudo make modules_install
sudo make install
```

### Step 6: Reboot
```bash
sudo reboot
```
Upon rebooting, your newly compiled kernel will be available as the default option in your GRUB menu.

---

## 2. Advanced Method: Customizing Kernel Options
If your goal is to reconfigure the existing kernel, enable experimental features, or strip out features to learn about kernel development, you can manually customize the kernel.

### Step 1: Open the Menu Configuration
After downloading the source (Step 2 above), open the terminal-based menu configuration tool:
```bash
make menuconfig
```

### Step 2: Customize and Save
* Navigate using your keyboard's arrow keys.
* Press the `Spacebar` to toggle features on `[*]`, off `[ ]`, or as a loadable module `[M]`.
* Once finished, navigate to `<Save>`, keep the filename as `.config`, and exit.

### Step 3: Build and Install
Proceed with compiling and installing exactly as you did in the simplest method:
```bash
make \
    -j$(nproc) \
    bzImage \
    modules
sudo make modules_install
sudo make install
```

### Optional Cleanup
If you need to manually remove your custom kernel later, you must delete its files from `/boot` (e.g., `config-<version>`, `initramfs-<version>`, `vmlinuz-<version>`, `System.map-<version>`) and its module directory from `/lib/modules/<version>`. Finally, remove the bootloader specification entries from `/boot/loader/entries/` and rebuild the GRUB config by running:
```bash
sudo grub2-mkconfig \
    -o \
    /boot/grub2/grub.cfg
```

---

## Sources
* **Fedora Quick Docs**: Building a Custom Kernel - https://docs.fedoraproject.org/en-US/quick-docs/kernel-build-custom/
* **Fedora Project Wiki**: Building a custom kernel - https://fedoraproject.org/wiki/Building_a_custom_kernel
