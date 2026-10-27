# documentation-and-cheat-sheets

A structured personal repository dedicated to administrative cheat sheets, virtualization runbooks, container references, and cross-platform command-line documentation.

---

## 🌳 Repository Structure

<!-- START_SECTION:tree -->
### 📁 ansible (Ansible Automation Guides)

| File | Description |
|---|---|
| <a href="ansible/ansible-automation-cheat-sheet.md"><code>ansible-automation-cheat-sheet.md</code></a> | Quick-reference CLI and syntax cheat sheet for Ansible |


### 📁 containers (Docker, Podman, and LXC Guides)

| File | Description |
|---|---|
| <a href="containers/docker-cli-compose-cheat-sheet.md"><code>docker-cli-compose-cheat-sheet.md</code></a> | Reference guide for essential Docker and Docker Compose commands |
| <a href="containers/lxc-cheatsheet.md"><code>lxc-cheatsheet.md</code></a> | quick-reference CLI guide for managing LXC/LXD system containers |
| <a href="containers/podman-cheatsheet.md"><code>podman-cheatsheet.md</code></a> | Essential commands for running daemonless containers with Podman |
| <a href="containers/podman-desktop-guide.md"><code>podman-desktop-guide.md</code></a> | How to install and set up the Podman Desktop GUI |


### 📁 fedora (Fedora Linux Specific Documentation)

| File | Description |
|---|---|
| <a href="fedora/airpods-pro-microphone-guide.md"><code>airpods-pro-microphone-guide.md</code></a> | AirPods Pro 3 Microphone Configuration on Fedora 44 KDE |
| <a href="fedora/asus-rog-fedora-setup.md"><code>asus-rog-fedora-setup.md</code></a> | ASUS ROG Zephyrus G15 Setup Guide for Fedora 44 KDE |
| <a href="fedora/asusctl-cheat-sheet-guide.md"><code>asusctl-cheat-sheet-guide.md</code></a> | Commands to control fans, lighting, and performance profiles on ASUS ROG laptops (GA503RW) with asusctl |
| <a href="fedora/btrbk-snapshot-automation-cheat-sheet.md"><code>btrbk-snapshot-automation-cheat-sheet.md</code></a> | Steps to automate Btrfs snapshots and backups using Btrbk |
| <a href="fedora/clamav-selinux-implementation-guide.md"><code>clamav-selinux-implementation-guide.md</code></a> | Fedora ClamAV & SELinux Implementation Guide |
| <a href="fedora/dnf-command-reference.md"><code>dnf-command-reference.md</code></a> | useful commands for Fedora’s DNF package manager |
| <a href="fedora/dnf-optimization-and-configuration-guide.md"><code>dnf-optimization-and-configuration-guide.md</code></a> | DNF Package Manager Speed Optimization & Configuration Guide |
| <a href="fedora/fedora-alacritty-setup-and-verification.md"><code>fedora-alacritty-setup-and-verification.md</code></a> | Setting up the Alacritty terminal on Fedora, complete with custom fonts and themes |
| <a href="fedora/fedora-dnf5-tailscale-repository-fix.md"><code>fedora-dnf5-tailscale-repository-fix.md</code></a> | Fixes and syntax for setting up Tailscale repositories with DNF5 on Fedora |
| <a href="fedora/fedora-firewall-cheat-sheet.md"><code>fedora-firewall-cheat-sheet.md</code></a> | Firewalld Cheat Sheet (Fedora / RHEL / CentOS) |
| <a href="fedora/fedora-kde-grub-btrfs-advanced.md"><code>fedora-kde-grub-btrfs-advanced.md</code></a> | Advanced fixes and config steps for GRUB and Btrfs integration on Fedora KDE |
| <a href="fedora/fedora-kde-grub-btrfs-integration.md"><code>fedora-kde-grub-btrfs-integration.md</code></a> | How to get Btrfs snapshots showing up directly in the GRUB boot menu on Fedora KDE |
| <a href="fedora/fedora-kde-ssd-formatting-btrbk.md"><code>fedora-kde-ssd-formatting-btrbk.md</code></a> | Steps to format a secondary SSD and set up automated Btrbk snapshots on Fedora KDE |
| <a href="fedora/fedora-kernel-compilation-guide.md"><code>fedora-kernel-compilation-guide.md</code></a> | This guide provides step-by-step instructions for manually configuring, compiling, and installing a custom or vanilla Linux kernel on Fedora systems |
| <a href="fedora/fedora-linux-btrfs-recovery.md"><code>fedora-linux-btrfs-recovery.md</code></a> | CLI methods for rescuing a corrupted Btrfs filesystem on Fedora |
| <a href="fedora/fedora-nvidia-installation-guide.md"><code>fedora-nvidia-installation-guide.md</code></a> | A guide to safely installing NVIDIA drivers on Fedora Workstation utilizing RPM Fusion repositories |
| <a href="fedora/fedora-quick-reference.md"><code>fedora-quick-reference.md</code></a> | CLI reference for Fedora Linux system administration. Provides direct syntax for DNF package management, systemd service control, journalctl diagnostics, firewalld rules, SELinux enforcement, and network operations |
| <a href="fedora/fedora-rog-setup.md"><code>fedora-rog-setup.md</code></a> | This document outlines the configurations applied by `fedora_rog_setup.sh` for optimizing the ASUS ROG Zephyrus G15 on Fedora 44 KDE. It manages graphics switching, daemon integration, and power profile adjustments required for stable desktop performance and battery management |
| <a href="fedora/fedora-selinux-management-cheat-sheet.md"><code>fedora-selinux-management-cheat-sheet.md</code></a> | Fedora SELinux Management & Context Resolution Cheat Sheet |
| <a href="fedora/fedora-tpm2-luks-autounlock-guide.md"><code>fedora-tpm2-luks-autounlock-guide.md</code></a> | Step-by-step guide for configuring automatic LUKS2 root volume decryption using hardware TPM 2.0 and systemd-cryptenroll |
| <a href="fedora/fix-mux-plymouth-deadlock.md"><code>fix-mux-plymouth-deadlock.md</code></a> | How to fix boot deadlocks caused by MUX switches and Plymouth |
| <a href="fedora/kde-plasma-6-multi-monitor-troubleshooting.md"><code>kde-plasma-6-multi-monitor-troubleshooting.md</code></a> | Fixes for multi-monitor display glitches in KDE Plasma 6 |
| <a href="fedora/kdeconnect-fedora44-ios-troubleshooting.md"><code>kdeconnect-fedora44-ios-troubleshooting.md</code></a> | KDE Connect fails to pair or discover devices (specifically iPhones) on Fedora 44 KDE Plasma, even after adding firewall rules to the `home` zone |
| <a href="fedora/snapper-snapshot-management-cheat-sheet.md"><code>snapper-snapshot-management-cheat-sheet.md</code></a> | Commands to create filesystem snapshots and roll back changes using Snapper |
| <a href="fedora/troubleshooting_dracut_nvidia_module_error.md"><code>troubleshooting_dracut_nvidia_module_error.md</code></a> | Troubleshooting: dracut-install Failed to find module 'nvidia' |


### 📁 linux-general (General Linux Reference)

| File | Description |
|---|---|
| <a href="linux-general/arkenfox-configuration-guide.md"><code>arkenfox-configuration-guide.md</code></a> | Arkenfox Configuration and Updater Guide |
| <a href="linux-general/bash-configuration-guide.md"><code>bash-configuration-guide.md</code></a> | Bash Configuration and Environment Automation Guide |
| <a href="linux-general/cardwire-cheat-sheet.md"><code>cardwire-cheat-sheet.md</code></a> | Cardwire Cheat Sheet |
| <a href="linux-general/enterprise-linux-ecosystem-and-commands-2026.md"><code>enterprise-linux-ecosystem-and-commands-2026.md</code></a> | A breakdown of the 2026 Enterprise Linux landscape plus core admin commands |
| <a href="linux-general/git-dotfiles-maintenance-cheat-sheet.md"><code>git-dotfiles-maintenance-cheat-sheet.md</code></a> | Commands and scripts for backing up system configurations and dotfiles with Git |
| <a href="linux-general/grubby-command-reference.md"><code>grubby-command-reference.md</code></a> | provides a quick-reference guide for using the grubby utility to view, switch, and modify Linux kernel boot parameters and default entries directly from the command line |
| <a href="linux-general/guide-to-using-alien.md"><code>guide-to-using-alien.md</code></a> | The Comprehensive Guide to Using `alien` |
| <a href="linux-general/iproute2-reference-guide.md"><code>iproute2-reference-guide.md</code></a> | This document provides a concise quick-reference guide for essential `iproute2` commands used in Linux network administration. It covers practical syntax for managing interfaces, IP addresses, routing tables, and socket statistics, serving as a modern replacement for legacy `net-tools` |
| <a href="linux-general/librepods-setup-guide.md"><code>librepods-setup-guide.md</code></a> | LibrePods Setup Guide |
| <a href="linux-general/linux-commands-cheat-sheet-tables.md"><code>linux-commands-cheat-sheet-tables.md</code></a> | Essential Linux commands, administration tools, and text editor shortcuts organized into tables |
| <a href="linux-general/linux-comprehensive-networking-guide.md"><code>linux-comprehensive-networking-guide.md</code></a> | Linux Comprehensive Networking Tools Guide |
| <a href="linux-general/linux-export-command-guide.md"><code>linux-export-command-guide.md</code></a> | How to properly set and manage environment variables using the export command |
| <a href="linux-general/linux-permissions-reference-expanded.md"><code>linux-permissions-reference-expanded.md</code></a> | A deep dive into managing Linux file permissions, ownership, and ACLs |
| <a href="linux-general/linux-source-installation-guide.md"><code>linux-source-installation-guide.md</code></a> | Steps to compile and install Linux software directly from source code |
| <a href="linux-general/linux-static-ip-configuration.md"><code>linux-static-ip-configuration.md</code></a> | Linux Static IP Configuration Guide |
| <a href="linux-general/linux-upstream-midstream-downstream-explained.md"><code>linux-upstream-midstream-downstream-explained.md</code></a> | A plain-English explanation of how upstream, midstream, and downstream open-source flows work |
| <a href="linux-general/linux-ventoy-usb-creation-guide.md"><code>linux-ventoy-usb-creation-guide.md</code></a> | How to format and create a multi-boot Ventoy USB drive on Linux |
| <a href="linux-general/make-bash-script-executable.md"><code>make-bash-script-executable.md</code></a> | How to make a Bash script executable and run it from anywhere on the system |
| <a href="linux-general/ncdu-command-reference.md"><code>ncdu-command-reference.md</code></a> | How to hunt down large files and analyze disk usage using NCDU |
| <a href="linux-general/nmcli-cheat-sheet.md"><code>nmcli-cheat-sheet.md</code></a> | Commands for managing network interfaces and Wi-Fi connections via nmcli |
| <a href="linux-general/nvidia-cuda-monitoring-cheat-sheet.md"><code>nvidia-cuda-monitoring-cheat-sheet.md</code></a> | Commands to monitor NVIDIA GPU performance and CUDA workloads |
| <a href="linux-general/samba-mount-guide.md"><code>samba-mount-guide.md</code></a> | Commands and configurations for connecting, temporarily mounting, and permanently automounting local SMB/CIFS network shares |
| <a href="linux-general/setup-script-documentation.md"><code>setup-script-documentation.md</code></a> | `setup.sh` - Workstation Setup Script Documentation |
| <a href="linux-general/ss-command-options-cheat-sheet.md"><code>ss-command-options-cheat-sheet.md</code></a> | How to inspect network sockets and connections using the ss command |
| <a href="linux-general/systemd-journalctl-cheat-sheet.md"><code>systemd-journalctl-cheat-sheet.md</code></a> | reference sheet for managing systemd services and inspecting system logs with journalctl |
| <a href="linux-general/vim-vi-editor-cheat-sheet.md"><code>vim-vi-editor-cheat-sheet.md</code></a> | Core commands for opening, editing, saving, and exiting Vi/Vim |


### 📁 linux-general/desktop-environments (KDE Plasma, Terminals & Desktop Tools)

| File | Description |
|---|---|
| <a href="linux-general/desktop-environments/alacritty-font-rendering-fix.md"><code>alacritty-font-rendering-fix.md</code></a> | Alacritty Rendering Troubleshooting Guide (Fedora KDE) |
| <a href="linux-general/desktop-environments/alacritty-keybindings-cheatsheet.md"><code>alacritty-keybindings-cheatsheet.md</code></a> | This document is a comprehensive Alacritty keybinding cheatsheet that outlines standard terminal shortcuts |
| <a href="linux-general/desktop-environments/fastfetch-configuration-guide.md"><code>fastfetch-configuration-guide.md</code></a> | How to tweak and customize system info outputs using Fastfetch |
| <a href="linux-general/desktop-environments/kde-plasma-wayland-shortcuts-cheat-sheet.md"><code>kde-plasma-wayland-shortcuts-cheat-sheet.md</code></a> | Essential keyboard shortcuts for getting around KDE Plasma on Wayland |
| <a href="linux-general/desktop-environments/sublime-text-linux-shortcuts.md"><code>sublime-text-linux-shortcuts.md</code></a> | Must-know keyboard shortcuts for Sublime Text on Linux |


### 📁 linux-general/hardware-and-firmware (Firmware Updates & Hardware Quirks)

| File | Description |
|---|---|
| <a href="linux-general/hardware-and-firmware/disable-amdgpu-grub.md"><code>disable-amdgpu-grub.md</code></a> | instructions for disabling the integrated AMD GPU on Fedora 44 by blacklisting the amdgpu module in the GRUB bootloader, ensuring the system relies exclusively on the dedicated NVIDIA GPU. It also includes troubleshooting steps using grubby and dracut to resolve issues where Boot Loader Specification (BLS) files retain outdated kernel parameters |
| <a href="linux-general/hardware-and-firmware/fwupdmgr-firmware-update-cheat-sheet.md"><code>fwupdmgr-firmware-update-cheat-sheet.md</code></a> | How to check for and apply hardware firmware updates with fwupdmgr |
| <a href="linux-general/hardware-and-firmware/wifi-hardware-replacement-guide.md"><code>wifi-hardware-replacement-guide.md</code></a> | Comprehensive Post-Wi-Fi Hardware Replacement Diagnostic Guide |


### 📁 linux-general/package-management (Package Managers & App Formats)

| File | Description |
|---|---|
| <a href="linux-general/package-management/apk-command-reference.md"><code>apk-command-reference.md</code></a> | Commands for installing and updating packages in Alpine Linux and containers using APK |
| <a href="linux-general/package-management/appimage-installation-guide.md"><code>appimage-installation-guide.md</code></a> | How to Install and Run AppImages on Linux |
| <a href="linux-general/package-management/apt-command-reference.md"><code>apt-command-reference.md</code></a> | Everyday package management commands for Debian and Ubuntu using APT |
| <a href="linux-general/package-management/brew-command-reference.md"><code>brew-command-reference.md</code></a> | Essential Homebrew commands for installing software on macOS and Linux |
| <a href="linux-general/package-management/flatpak-command-reference.md"><code>flatpak-command-reference.md</code></a> | Commands to install, update, and manage sandboxed Flatpak apps |
| <a href="linux-general/package-management/pacman-command-reference.md"><code>pacman-command-reference.md</code></a> | Essential commands for managing Arch Linux packages with Pacman |
| <a href="linux-general/package-management/zypper-command-reference.md"><code>zypper-command-reference.md</code></a> | Everyday commands for managing packages on openSUSE and SLES using Zypper |


### 📁 linux-general/storage-and-filesystems (BTRFS, ZFS, RAID & Storage Utilities)

| File | Description |
|---|---|
| <a href="linux-general/storage-and-filesystems/btrfs-cheat-sheet.md"><code>btrfs-cheat-sheet.md</code></a> | quick-reference guide for managing Btrfs filesystems |
| <a href="linux-general/storage-and-filesystems/nvme-cli-cheat-sheet.md"><code>nvme-cli-cheat-sheet.md</code></a> | nvme-cli Cheat Sheet |
| <a href="linux-general/storage-and-filesystems/nvme-troubleshooting-guide.md"><code>nvme-troubleshooting-guide.md</code></a> | NVMe Unsafe Shutdown Troubleshooting Guide |
| <a href="linux-general/storage-and-filesystems/raid-cheatsheet.md"><code>raid-cheatsheet.md</code></a> | RAID Cheatsheet for Beginners |
| <a href="linux-general/storage-and-filesystems/smartctl-cheat-sheet.md"><code>smartctl-cheat-sheet.md</code></a> | `smartctl` Comprehensive Cheat Sheet |
| <a href="linux-general/storage-and-filesystems/storage-management-reference.md"><code>storage-management-reference.md</code></a> | Commands to manage block devices, format partitions, and handle filesystems |
| <a href="linux-general/storage-and-filesystems/zfs-administration-cheat-sheet.md"><code>zfs-administration-cheat-sheet.md</code></a> | A technical reference detailing essential commands for managing ZFS physical storage pools and logical datasets, including pool creation, dataset properties, snapshot replication, and disk replacement workflows |


### 📁 networking-and-security (Networking & Security Configurations)

| File | Description |
|---|---|
| <a href="networking-and-security/adguard-home-management-cheat-sheet.md"><code>adguard-home-management-cheat-sheet.md</code></a> | Commands and config paths for managing AdGuard Home DNS rules and filters |
| <a href="networking-and-security/iptables-cheat-sheet.md"><code>iptables-cheat-sheet.md</code></a> | How to properly configure network filtering, manage firewall rulesets, and set up NAT using the iptables command-line utility |
| <a href="networking-and-security/networking-cheatsheet.md"><code>networking-cheatsheet.md</code></a> | Networking Concepts and Explanations Cheatsheet |
| <a href="networking-and-security/nftables-cheat-sheet.md"><code>nftables-cheat-sheet.md</code></a> | How to properly configure network filtering, manage firewall rulesets, and set up NAT using the nftables command-line utility |
| <a href="networking-and-security/openwrt-uci-command-cheat-sheet.md"><code>openwrt-uci-command-cheat-sheet.md</code></a> | How to configure OpenWrt router settings straight from the terminal using UCI |
| <a href="networking-and-security/opkg-cheatsheet.md"><code>opkg-cheatsheet.md</code></a> | quick reference for the ⁠opkg⁠ package manager, commonly used on OpenWrt and embedded Linux systems. It covers the essential commands needed to install, upgrade, query, and manage software packages and their dependencies |
| <a href="networking-and-security/pentesting-toolkit-cheat-sheet.md"><code>pentesting-toolkit-cheat-sheet.md</code></a> | A quick reference for everyday penetration testing tools and frameworks |
| <a href="networking-and-security/tailscale-mesh-cli-cheat-sheet.md"><code>tailscale-mesh-cli-cheat-sheet.md</code></a> | Terminal commands for setting up and managing Tailscale mesh networks |
| <a href="networking-and-security/ufw-cheatsheet.md"><code>ufw-cheatsheet.md</code></a> | UFW (Uncomplicated Firewall) Command Reference for Ubuntu/Debian |


### 📁 virtualization (Hypervisor & VM Runbooks)

| File | Description |
|---|---|
| <a href="virtualization/hyper-v-powershell-cheat-sheet.md"><code>hyper-v-powershell-cheat-sheet.md</code></a> | PowerShell commands to spin up and manage Hyper-V virtual machines |
| <a href="virtualization/proxmox-cheatsheet.md"><code>proxmox-cheatsheet.md</code></a> | Proxmox Virtual Machine Commands (qm) Cheat Sheet |
| <a href="virtualization/virt-manager-cheatsheet.md"><code>virt-manager-cheatsheet.md</code></a> | Virt-Manager & Virsh Command Line Cheat Sheet |
| <a href="virtualization/virt-manager-docker-conflict.md"><code>virt-manager-docker-conflict.md</code></a> | How to fix network bridge conflicts when running Virt-Manager and Docker on the same machine |
| <a href="virtualization/virtualization-virt-manager-troubleshooting-fedora.md"><code>virtualization-virt-manager-troubleshooting-fedora.md</code></a> | Fixes and tweaks for running Virt-Manager smoothly on Fedora |
| <a href="virtualization/vmware_btrfs_recovery_guide.md"><code>vmware_btrfs_recovery_guide.md</code></a> | VMware VM Recovery Guide (Btrfs Snapshots) |


### 📁 windows-and-macos (Windows & macOS References)

| File | Description |
|---|---|
| <a href="windows-and-macos/macos-terminal-package-management-cheat-sheet.md"><code>macos-terminal-package-management-cheat-sheet.md</code></a> | A quick-reference guide for macOS command-line operations, covering Homebrew package management, system software updates, networking tools, process management, and essential Finder modifications |
| <a href="windows-and-macos/windows-cmd-cheatsheet.md"><code>windows-cmd-cheatsheet.md</code></a> | A quick-reference cheat sheet for Windows Command Prompt (CMD) and PowerShell, covering file navigation, system management, and package provisioning |
| <a href="windows-and-macos/windows-powershell-active-directory.md"><code>windows-powershell-active-directory.md</code></a> | A quick-reference guide for Windows PowerShell administration, covering Registry manipulation, Active Directory user and group management, remote networking, and object-oriented data filtering |
| <a href="windows-and-macos/windows-sysinternals-cheat-sheet.md"><code>windows-sysinternals-cheat-sheet.md</code></a> | A practical guide to core Microsoft Sysinternals tools (Process Explorer, Process Monitor, Autoruns, PsExec, and TCPView), highlighting specific filters, shortcuts, and commands for advanced troubleshooting, malware isolation, and remote system administration |
| <a href="windows-and-macos/winget-cheat-sheet.md"><code>winget-cheat-sheet.md</code></a> | A quick-reference guide for managing Windows software packages using the Winget command-line tool, covering package discovery, silent installations, bulk upgrades, and system provisioning |
<!-- END_SECTION:tree -->
