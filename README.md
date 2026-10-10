# documentation-and-cheat-sheets

A structured personal repository dedicated to administrative cheat sheets, virtualization runbooks, container references, and cross-platform command-line documentation.

---

## 🌳 Repository Structure
<!-- START_SECTION:tree -->
### 📁 ansible/ (Ansible Automation Guides)

| File | Description |
|---|---|
| <a href="ansible/Ansible_Automation_Cheat_Sheet.md"><code>Ansible_Automation_Cheat_Sheet.md</code></a> | Quick-reference CLI and syntax cheat sheet for Ansible |

### 📁 containers/ (Docker, Podman, and LXC Guides)

| File | Description |
| --- | --- |
| <a href="containers/Docker_CLI_Compose_Cheat_Sheet.md"><code>Docker_CLI_Compose_Cheat_Sheet.md</code></a> | reference guide for essential Docker and Docker Compose commands |
| <a href="containers/lxc-cheatsheet.md"><code>lxc-cheatsheet.md</code></a> | quick-reference CLI guide for managing LXC/LXD system containers |
| <a href="containers/podman-cheatsheet.md"><code>podman-cheatsheet.md</code></a> | Essential commands for running daemonless containers with Podman |
| <a href="containers/podman-desktop-guide.md"><code>podman-desktop-guide.md</code></a> | How to install and set up the Podman Desktop GUI |

### 📁 fedora/ (Fedora Linux Specific Documentation)

| File | Description |
| --- | --- |
| <a href="fedora/ Fedora_NVIDIA_Installation_Guide.md"><code> Fedora_NVIDIA_Installation_Guide.md</code></a> | A guide to safely installing NVIDIA drivers on Fedora Workstation utilizing RPM Fusion repositories |
| <a href="fedora/Btrbk_Snapshot_Automation_Cheat_Sheet.md"><code>Btrbk_Snapshot_Automation_Cheat_Sheet.md</code></a> | Steps to automate Btrfs snapshots and backups using Btrbk |
| <a href="fedora/ClamAV_SELinux_Implementation_Guide.md"><code>ClamAV_SELinux_Implementation_Guide.md</code></a> | Fedora ClamAV & SELinux Implementation Guide |
| <a href="fedora/DNF_Optimization_and_Configuration_Guide.md"><code>DNF_Optimization_and_Configuration_Guide.md</code></a> | DNF Package Manager Speed Optimization & Configuration Guide |
| <a href="fedora/Fedora_DNF5_Tailscale_Repository_Fix.md"><code>Fedora_DNF5_Tailscale_Repository_Fix.md</code></a> | Fixes and syntax for setting up Tailscale repositories with DNF5 on Fedora |
| <a href="fedora/Fedora_Firewall_Cheat_Sheet.md"><code>Fedora_Firewall_Cheat_Sheet.md</code></a> | Firewalld Cheat Sheet (Fedora / RHEL / CentOS) |
| <a href="fedora/Fedora_KDE_GRUB_Btrfs_Advanced.md"><code>Fedora_KDE_GRUB_Btrfs_Advanced.md</code></a> | Advanced fixes and config steps for GRUB and Btrfs integration on Fedora KDE |
| <a href="fedora/Fedora_KDE_GRUB_Btrfs_Integration.md"><code>Fedora_KDE_GRUB_Btrfs_Integration.md</code></a> | How to get Btrfs snapshots showing up directly in the GRUB boot menu on Fedora KDE |
| <a href="fedora/Fedora_KDE_SSD_Formatting_Btrbk.md"><code>Fedora_KDE_SSD_Formatting_Btrbk.md</code></a> | Steps to format a secondary SSD and set up automated Btrbk snapshots on Fedora KDE |
| <a href="fedora/Fedora_Kernel_Compilation_Guide.md"><code>Fedora_Kernel_Compilation_Guide.md</code></a> | This guide provides step-by-step instructions for manually configuring, compiling, and installing a custom or vanilla Linux kernel on Fedora systems |
| <a href="fedora/Fedora_Linux_Btrfs_Recovery.md"><code>Fedora_Linux_Btrfs_Recovery.md</code></a> | CLI methods for rescuing a corrupted Btrfs filesystem on Fedora |
| <a href="fedora/Fedora_SELinux_Management_Cheat_Sheet.md"><code>Fedora_SELinux_Management_Cheat_Sheet.md</code></a> | Fedora SELinux Management & Context Resolution Cheat Sheet |
| <a href="fedora/Fedora_TPM2_LUKS_AutoUnlock_Guide.md"><code>Fedora_TPM2_LUKS_AutoUnlock_Guide.md</code></a> | Step-by-step guide for configuring automatic LUKS2 root volume decryption using hardware TPM 2.0 and systemd-cryptenroll |
| <a href="fedora/KDE_Plasma_6_Multi_Monitor_Troubleshooting.md"><code>KDE_Plasma_6_Multi_Monitor_Troubleshooting.md</code></a> | Fixes for multi-monitor display glitches in KDE Plasma 6 |
| <a href="fedora/Snapper_Snapshot_Management_Cheat_Sheet.md"><code>Snapper_Snapshot_Management_Cheat_Sheet.md</code></a> | Commands to create filesystem snapshots and roll back changes using Snapper |
| <a href="fedora/asus-rog-fedora-setup.md"><code>asus-rog-fedora-setup.md</code></a> | ASUS ROG Zephyrus G15 Setup Guide for Fedora 44 KDE |
| <a href="fedora/asusctl_cheat_sheet_guide.md"><code>asusctl_cheat_sheet_guide.md</code></a> | Commands to control fans, lighting, and performance profiles on ASUS ROG laptops (GA503RW) with asusctl |
| <a href="fedora/dnf_command_reference.md"><code>dnf_command_reference.md</code></a> | useful commands for Fedora’s DNF package manager |
| <a href="fedora/fedora-alacritty-setup-and-verification.md"><code>fedora-alacritty-setup-and-verification.md</code></a> | Setting up the Alacritty terminal on Fedora, complete with custom fonts and themes |
| <a href="fedora/fedora-quick-reference.md"><code>fedora-quick-reference.md</code></a> | CLI reference for Fedora Linux system administration. Provides direct syntax for DNF package management, systemd service control, journalctl diagnostics, firewalld rules, SELinux enforcement, and network operations |
| <a href="fedora/fedora_rog_setup.md"><code>fedora_rog_setup.md</code></a> | This document outlines the configurations applied by `fedora_rog_setup.sh` for optimizing the ASUS ROG Zephyrus G15 on Fedora 44 KDE. It manages graphics switching, daemon integration, and power profile adjustments required for stable desktop performance and battery management |
| <a href="fedora/fix-mux-plymouth-deadlock.md"><code>fix-mux-plymouth-deadlock.md</code></a> | How to fix boot deadlocks caused by MUX switches and Plymouth |
| <a href="fedora/kdeconnect-fedora44-ios-troubleshooting.md"><code>kdeconnect-fedora44-ios-troubleshooting.md</code></a> | KDE Connect fails to pair or discover devices (specifically iPhones) on Fedora 44 KDE Plasma, even after adding firewall rules to the `home` zone |

### 📁 linux-general/ (General Linux Reference)

| File | Description |
| --- | --- |
| <a href="linux-general/Enterprise_Linux_Ecosystem_and_Commands_2026.md"><code>Enterprise_Linux_Ecosystem_and_Commands_2026.md</code></a> | A breakdown of the 2026 Enterprise Linux landscape plus core admin commands |
| <a href="linux-general/Fastfetch_Configuration_Guide.md"><code>Fastfetch_Configuration_Guide.md</code></a> | How to tweak and customize system info outputs using Fastfetch |
| <a href="linux-general/Git_Dotfiles_Maintenance_Cheat_Sheet.md"><code>Git_Dotfiles_Maintenance_Cheat_Sheet.md</code></a> | Commands and scripts for backing up system configurations and dotfiles with Git |
| <a href="linux-general/KDE_Plasma_Wayland_Shortcuts_Cheat_Sheet.md"><code>KDE_Plasma_Wayland_Shortcuts_Cheat_Sheet.md</code></a> | Essential keyboard shortcuts for getting around KDE Plasma on Wayland |
| <a href="linux-general/Linux_Commands_Cheat_Sheet_Tables.md"><code>Linux_Commands_Cheat_Sheet_Tables.md</code></a> | Essential Linux commands, administration tools, and text editor shortcuts organized into tables |
| <a href="linux-general/Linux_Export_Command_Guide.md"><code>Linux_Export_Command_Guide.md</code></a> | How to properly set and manage environment variables using the export command |
| <a href="linux-general/Linux_Upstream_Midstream_Downstream_Explained.md"><code>Linux_Upstream_Midstream_Downstream_Explained.md</code></a> | A plain-English explanation of how upstream, midstream, and downstream open-source flows work |
| <a href="linux-general/Linux_Ventoy_USB_Creation_Guide.md"><code>Linux_Ventoy_USB_Creation_Guide.md</code></a> | How to format and create a multi-boot Ventoy USB drive on Linux |
| <a href="linux-general/NVIDIA_CUDA_Monitoring_Cheat_Sheet.md"><code>NVIDIA_CUDA_Monitoring_Cheat_Sheet.md</code></a> | Commands to monitor NVIDIA GPU performance and CUDA workloads |
| <a href="linux-general/SS_Command_Options_Cheat_Sheet.md"><code>SS_Command_Options_Cheat_Sheet.md</code></a> | How to inspect network sockets and connections using the ss command |
| <a href="linux-general/Sublime_Text_Linux_Shortcuts.md"><code>Sublime_Text_Linux_Shortcuts.md</code></a> | Must-know keyboard shortcuts for Sublime Text on Linux |
| <a href="linux-general/Vim_Vi_Editor_Cheat_Sheet.md"><code>Vim_Vi_Editor_Cheat_Sheet.md</code></a> | Core commands for opening, editing, saving, and exiting Vi/Vim |
| <a href="linux-general/ZFS_Administration_Cheat_Sheet.md"><code>ZFS_Administration_Cheat_Sheet.md</code></a> | A technical reference detailing essential commands for managing ZFS physical storage pools and logical datasets, including pool creation, dataset properties, snapshot replication, and disk replacement workflows |
| <a href="linux-general/alacritty-font-rendering-fix.md"><code>alacritty-font-rendering-fix.md</code></a> | Alacritty Rendering Troubleshooting Guide (Fedora KDE) |
| <a href="linux-general/alacritty_keybindings_cheatsheet.md"><code>alacritty_keybindings_cheatsheet.md</code></a> | This document is a comprehensive Alacritty keybinding cheatsheet that outlines standard terminal shortcuts |
| <a href="linux-general/apk_command_reference.md"><code>apk_command_reference.md</code></a> | Commands for installing and updating packages in Alpine Linux and containers using APK |
| <a href="linux-general/appimage_installation_guide.md"><code>appimage_installation_guide.md</code></a> | How to Install and Run AppImages on Linux |
| <a href="linux-general/apt_command_reference.md"><code>apt_command_reference.md</code></a> | Everyday package management commands for Debian and Ubuntu using APT |
| <a href="linux-general/arkenfox-configuration-guide.md"><code>arkenfox-configuration-guide.md</code></a> | Arkenfox Configuration and Updater Guide |
| <a href="linux-general/bash_configuration_guide.md"><code>bash_configuration_guide.md</code></a> | Bash Configuration and Environment Automation Guide |
| <a href="linux-general/brew_command_reference.md"><code>brew_command_reference.md</code></a> | Essential Homebrew commands for installing software on macOS and Linux |
| <a href="linux-general/btrfs_cheat_sheet.md"><code>btrfs_cheat_sheet.md</code></a> | quick-reference guide for managing Btrfs filesystems |
| <a href="linux-general/cardwire-cheat-sheet.md"><code>cardwire-cheat-sheet.md</code></a> | Cardwire Cheat Sheet |
| <a href="linux-general/disable-amdgpu-grub.md"><code>disable-amdgpu-grub.md</code></a> | instructions for disabling the integrated AMD GPU on Fedora 44 by blacklisting the amdgpu module in the GRUB bootloader, ensuring the system relies exclusively on the dedicated NVIDIA GPU. It also includes troubleshooting steps using grubby and dracut to resolve issues where Boot Loader Specification (BLS) files retain outdated kernel parameters |
| <a href="linux-general/flatpak_command_reference.md"><code>flatpak_command_reference.md</code></a> | Commands to install, update, and manage sandboxed Flatpak apps |
| <a href="linux-general/fwupdmgr_Firmware_Update_Cheat_Sheet.md"><code>fwupdmgr_Firmware_Update_Cheat_Sheet.md</code></a> | How to check for and apply hardware firmware updates with fwupdmgr |
| <a href="linux-general/grubby-command-reference.md"><code>grubby-command-reference.md</code></a> | provides a quick-reference guide for using the grubby utility to view, switch, and modify Linux kernel boot parameters and default entries directly from the command line |
| <a href="linux-general/guide_to_using_alien.md"><code>guide_to_using_alien.md</code></a> | The Comprehensive Guide to Using `alien` |
| <a href="linux-general/iproute2_reference_guide.md"><code>iproute2_reference_guide.md</code></a> | This document provides a concise quick-reference guide for essential `iproute2` commands used in Linux network administration. It covers practical syntax for managing interfaces, IP addresses, routing tables, and socket statistics, serving as a modern replacement for legacy `net-tools` |
| <a href="linux-general/librepods_setup_guide.md"><code>librepods_setup_guide.md</code></a> | LibrePods Setup Guide |
| <a href="linux-general/linux-comprehensive-networking-guide.md"><code>linux-comprehensive-networking-guide.md</code></a> | Linux Comprehensive Networking Tools Guide |
| <a href="linux-general/linux-static-ip-configuration.md"><code>linux-static-ip-configuration.md</code></a> | Linux Static IP Configuration Guide |
| <a href="linux-general/linux_permissions_reference_expanded.md"><code>linux_permissions_reference_expanded.md</code></a> | A deep dive into managing Linux file permissions, ownership, and ACLs |
| <a href="linux-general/linux_source_installation_guide.md"><code>linux_source_installation_guide.md</code></a> | Steps to compile and install Linux software directly from source code |
| <a href="linux-general/make_bash_script_executable.md"><code>make_bash_script_executable.md</code></a> | How to make a Bash script executable and run it from anywhere on the system |
| <a href="linux-general/ncdu_command_reference.md"><code>ncdu_command_reference.md</code></a> | How to hunt down large files and analyze disk usage using NCDU |
| <a href="linux-general/nmcli-cheat-sheet.md"><code>nmcli-cheat-sheet.md</code></a> | Commands for managing network interfaces and Wi-Fi connections via nmcli |
| <a href="linux-general/nvme_cli_cheat_sheet.md"><code>nvme_cli_cheat_sheet.md</code></a> | nvme-cli Cheat Sheet |
| <a href="linux-general/nvme_troubleshooting_guide.md"><code>nvme_troubleshooting_guide.md</code></a> | NVMe Unsafe Shutdown Troubleshooting Guide |
| <a href="linux-general/pacman_command_reference.md"><code>pacman_command_reference.md</code></a> | Essential commands for managing Arch Linux packages with Pacman |
| <a href="linux-general/raid_cheatsheet.md"><code>raid_cheatsheet.md</code></a> | RAID Cheatsheet for Beginners |
| <a href="linux-general/samba-mount-guide.md"><code>samba-mount-guide.md</code></a> | Commands and configurations for connecting, temporarily mounting, and permanently automounting local SMB/CIFS network shares |
| <a href="linux-general/setup_script_documentation.md"><code>setup_script_documentation.md</code></a> | `setup.sh` - Workstation Setup Script Documentation |
| <a href="linux-general/smartctl_cheat_sheet.md"><code>smartctl_cheat_sheet.md</code></a> | `smartctl` Comprehensive Cheat Sheet |
| <a href="linux-general/storage_management_reference.md"><code>storage_management_reference.md</code></a> | Commands to manage block devices, format partitions, and handle filesystems |
| <a href="linux-general/systemd_journalctl_cheat_sheet.md"><code>systemd_journalctl_cheat_sheet.md</code></a> | reference sheet for managing systemd services and inspecting system logs with journalctl |
| <a href="linux-general/wifi-hardware-replacement-guide.md"><code>wifi-hardware-replacement-guide.md</code></a> | Comprehensive Post-Wi-Fi Hardware Replacement Diagnostic Guide |
| <a href="linux-general/zypper_command_reference.md"><code>zypper_command_reference.md</code></a> | Everyday commands for managing packages on openSUSE and SLES using Zypper |

### 📁 networking-and-security/ (Networking & Security Configurations)

| File | Description |
| --- | --- |
| <a href="networking-and-security/AdGuard_Home_Management_Cheat_Sheet.md"><code>AdGuard_Home_Management_Cheat_Sheet.md</code></a> | Commands and config paths for managing AdGuard Home DNS rules and filters |
| <a href="networking-and-security/OpenWrt_UCI_Command_Cheat_Sheet.md"><code>OpenWrt_UCI_Command_Cheat_Sheet.md</code></a> | How to configure OpenWrt router settings straight from the terminal using UCI |
| <a href="networking-and-security/Pentesting_Toolkit_Cheat_Sheet.md"><code>Pentesting_Toolkit_Cheat_Sheet.md</code></a> | A quick reference for everyday penetration testing tools and frameworks |
| <a href="networking-and-security/Tailscale_Mesh_CLI_Cheat_Sheet.md"><code>Tailscale_Mesh_CLI_Cheat_Sheet.md</code></a> | Terminal commands for setting up and managing Tailscale mesh networks |
| <a href="networking-and-security/networking_cheatsheet.md"><code>networking_cheatsheet.md</code></a> | Networking Concepts and Explanations Cheatsheet |
| <a href="networking-and-security/nftables_Cheat_Sheet.md"><code>nftables_Cheat_Sheet.md</code></a> | How to properly configure network filtering, manage firewall rulesets, and set up NAT using the nftables command-line utility |
| <a href="networking-and-security/opkg_cheatsheet.md"><code>opkg_cheatsheet.md</code></a> | quick reference for the ⁠opkg⁠ package manager, commonly used on OpenWrt and embedded Linux systems. It covers the essential commands needed to install, upgrade, query, and manage software packages and their dependencies |
| <a href="networking-and-security/ufw-cheatsheet.md"><code>ufw-cheatsheet.md</code></a> | UFW (Uncomplicated Firewall) Command Reference for Ubuntu/Debian |

### 📁 virtualization/ (Hypervisor & VM Runbooks)

| File | Description |
| --- | --- |
| <a href="virtualization/Hyper-V_PowerShell_Cheat_Sheet.md"><code>Hyper-V_PowerShell_Cheat_Sheet.md</code></a> | PowerShell commands to spin up and manage Hyper-V virtual machines |
| <a href="virtualization/proxmox-cheatsheet.md"><code>proxmox-cheatsheet.md</code></a> | Proxmox Virtual Machine Commands (qm) Cheat Sheet |
| <a href="virtualization/virt-manager-cheatsheet.md"><code>virt-manager-cheatsheet.md</code></a> | Virt-Manager & Virsh Command Line Cheat Sheet |
| <a href="virtualization/virt-manager-docker-conflict.md"><code>virt-manager-docker-conflict.md</code></a> | How to fix network bridge conflicts when running Virt-Manager and Docker on the same machine |
| <a href="virtualization/virtualization_virt-manager-troubleshooting-fedora.md"><code>virtualization_virt-manager-troubleshooting-fedora.md</code></a> | Fixes and tweaks for running Virt-Manager smoothly on Fedora |

### 📁 windows-and-macos/ (Windows & macOS References)

| File | Description |
| --- | --- |
| <a href="windows-and-macos/Windows_Sysinternals_Cheat_Sheet.md"><code>Windows_Sysinternals_Cheat_Sheet.md</code></a> | A practical guide to core Microsoft Sysinternals tools (Process Explorer, Process Monitor, Autoruns, PsExec, and TCPView), highlighting specific filters, shortcuts, and commands for advanced troubleshooting, malware isolation, and remote system administration |
| <a href="windows-and-macos/Winget_Cheat_Sheet.md"><code>Winget_Cheat_Sheet.md</code></a> | A quick-reference guide for managing Windows software packages using the Winget command-line tool, covering package discovery, silent installations, bulk upgrades, and system provisioning |
| <a href="windows-and-macos/macOS_Terminal_Package_Management_Cheat_Sheet.md"><code>macOS_Terminal_Package_Management_Cheat_Sheet.md</code></a> | A quick-reference guide for macOS command-line operations, covering Homebrew package management, system software updates, networking tools, process management, and essential Finder modifications |
| <a href="windows-and-macos/windows-cmd-cheatsheet.md"><code>windows-cmd-cheatsheet.md</code></a> | A quick-reference cheat sheet for Windows Command Prompt (CMD) and PowerShell, covering file navigation, system management, and package provisioning |
| <a href="windows-and-macos/windows-powershell-active-directory.md"><code>windows-powershell-active-directory.md</code></a> | A quick-reference guide for Windows PowerShell administration, covering Registry manipulation, Active Directory user and group management, remote networking, and object-oriented data filtering |
<!-- END_SECTION:tree -->
