#  documentation-and-cheat-sheets

A structured personal repository dedicated to administrative cheat sheets, virtualization runbooks, container references, and cross-platform command-line documentation.

---

## 🌳 Repository Structure
<!-- START_SECTION:tree -->
### 📁 ansible/ (Ansible Automation Guides)

| File | Description |
|---|---|
| `Ansible_Automation_Cheat_Sheet.md` | Ansible Automation Cheat Sheet |


### 📁 containers/ (Docker, Podman, and LXC Guides)

| File | Description |
|---|---|
| `Docker_CLI_Compose_Cheat_Sheet.md` | Core commands for spinning up Docker containers, managing images, and using Compose. |
| `lxc-cheatsheet.md` | LXC/LXD Essentials Cheat Sheet |
| `podman-cheatsheet.md` | Essential commands for running daemonless containers with Podman. |
| `podman-desktop-guide.md` | How to install and set up the Podman Desktop GUI |


### 📁 fedora/ (Fedora Linux Specific Documentation)

| File | Description |
|---|---|
| ` Fedora_NVIDIA_Installation_Guide.md` | A guide to safely installing NVIDIA drivers on Fedora Workstation utilizing RPM Fusion repositories. |
| `Btrbk_Snapshot_Automation_Cheat_Sheet.md` | Steps to automate Btrfs snapshots and backups using Btrbk. |
| `ClamAV_SELinux_Implementation_Guide.md` | Getting ClamAV antivirus working smoothly with SELinux on Fedora 44. |
| `DNF_Configuration_Guide.md` | Tweaks and settings to speed up the DNF package manager. |
| `Fedora_DNF5_Tailscale_Repository_Fix.md` | Fixes and syntax for setting up Tailscale repositories with DNF5 on Fedora. |
| `Fedora_Firewall_Cheat_Sheet.md` | Quick commands for managing network rules using Firewalld on Fedora. |
| `Fedora_KDE_GRUB_Btrfs_Advanced.md` | Advanced fixes and config steps for GRUB and Btrfs integration on Fedora KDE. |
| `Fedora_KDE_GRUB_Btrfs_Integration.md` | How to get Btrfs snapshots showing up directly in the GRUB boot menu on Fedora KDE. |
| `Fedora_KDE_SSD_Formatting_Btrbk.md` | Steps to format a secondary SSD and set up automated Btrbk snapshots on Fedora KDE. |
| `Fedora_Linux_Btrfs_Recovery.md` | CLI methods for rescuing a corrupted Btrfs filesystem on Fedora. |
| `Fedora_SELinux_Cheat_Sheet.md` | Everyday commands for fixing and managing SELinux policies on Fedora. |
| `Fedora_TPM2_LUKS_AutoUnlock_Guide.md` | Step-by-step guide for configuring automatic LUKS2 root volume decryption using hardware TPM 2.0 and systemd-cryptenroll. |
| `KDE_Plasma_6_Multi_Monitor_Troubleshooting.md` | Fixes for multi-monitor display glitches in KDE Plasma 6. |
| `Snapper_Snapshot_Management_Cheat_Sheet.md` | Commands to create filesystem snapshots and roll back changes using Snapper |
| `asusctl_cheat_sheet_guide.md` | Commands to control fans, lighting, and performance profiles on ASUS ROG laptops (GA503RW) with asusctl. |
| `dnf-speed-optimization-guide.md` | DNF Package Manager Speed Optimization & Configuration Guide |
| `dnf_command_reference.md` | useful commands for Fedora’s DNF package manager. |
| `fedora-alacritty-setup-and-verification.md` | Setting up the Alacritty terminal on Fedora, complete with custom fonts and themes. |
| `fedora-clamav-setup-guide.md` | How to deploy and automate ClamAV scans on Fedora. |
| `fix-mux-plymouth-deadlock.md` | How to fix boot deadlocks caused by MUX switches and Plymouth. |
| `selinux-context-resolution.md` | How to track down and fix SELinux context denials and permission errors. |


### 📁 linux-general/ (General Linux Reference)

| File | Description |
|---|---|
| `Enterprise_Linux_Ecosystem_and_Commands_2026.md` | A breakdown of the 2026 Enterprise Linux landscape plus core admin commands. |
| `Fastfetch_Configuration_Guide.md` | How to tweak and customize system info outputs using Fastfetch. |
| `Git_Dotfiles_Maintenance_Cheat_Sheet.md` | Commands and scripts for backing up system configurations and dotfiles with Git |
| `KDE_Plasma_Wayland_Shortcuts_Cheat_Sheet.md` | Essential keyboard shortcuts for getting around KDE Plasma on Wayland. |
| `Linux_Export_Command_Guide.md` | How to properly set and manage environment variables using the export command. |
| `Linux_Systemd_Cheat_Sheet.md` | Everyday commands for handling services and logs with Systemd and journalctl. |
| `Linux_Upstream_Midstream_Downstream_Explained.md` | A plain-English explanation of how upstream, midstream, and downstream open-source flows work. |
| `Linux_Ventoy_USB_Creation_Guide.md` | How to format and create a multi-boot Ventoy USB drive on Linux. |
| `NVIDIA_CUDA_Monitoring_Cheat_Sheet.md` | Commands to monitor NVIDIA GPU performance and CUDA workloads. |
| `SS_Command_Options_Cheat_Sheet.md` | How to inspect network sockets and connections using the ss command. |
| `Sublime_Text_Linux_Shortcuts.md` | Must-know keyboard shortcuts for Sublime Text on Linux. |
| `Vim_Vi_Editor_Cheat_Sheet.md` | Core commands for opening, editing, saving, and exiting Vi/Vim. |
| `ZFS_Administration_Cheat_Sheet.md` | A technical reference detailing essential commands for managing ZFS physical storage pools and logical datasets, including pool creation, dataset properties, snapshot replication, and disk replacement workflows |
| `apk_command_reference.md` | Commands for installing and updating packages in Alpine Linux and containers using APK. |
| `apt_command_reference.md` | Everyday package management commands for Debian and Ubuntu using APT. |
| `brew_command_reference.md` | Essential Homebrew commands for installing software on macOS and Linux. |
| `cheatsheet-for-linux.md` | A quick comparison of commands across the most common Linux package managers. |
| `flatpak_command_reference.md` | Commands to install, update, and manage sandboxed Flatpak apps. |
| `fwupdmgr_Firmware_Update_Cheat_Sheet.md` | How to check for and apply hardware firmware updates with fwupdmgr. |
| `linux_permissions_reference_expanded.md` | A deep dive into managing Linux file permissions, ownership, and ACLs. |
| `linux_source_installation_guide.md` | Steps to compile and install Linux software directly from source code. |
| `make_bash_script_executable.md` | How to make a Bash script executable and run it from anywhere on the system. |
| `ncdu_command_reference.md` | NCDU (NCurses Disk Usage) Command Reference Guide |
| `nmcli-cheat-sheet.md` | nmcli Cheat Sheet |
| `pacman_command_reference.md` | Pacman Command Reference Guide |
| `storage_management_reference.md` | Storage Management Command Reference Guide |
| `workstation_bootstrap_documentation.md` | Workstation Bootstrap & Toolstack Installer Documentation |
| `zypper_command_reference.md` | Zypper Command Reference Guide (openSUSE / SUSE Linux Enterprise) |


### 📁 networking-and-security/ (Networking & Security Configurations)

| File | Description |
|---|---|
| `AdGuard_Home_Management_Cheat_Sheet.md` | AdGuard Home Management & DNS Filtering Cheat Sheet |
| `OpenWrt_UCI_Command_Cheat_Sheet.md` | OpenWrt UCI (Unified Configuration Interface) Cheat Sheet |
| `Pentesting_Toolkit_Cheat_Sheet.md` | Penetration Testing Toolkit Cheat Sheet |
| `Tailscale_Mesh_CLI_Cheat_Sheet.md` | Tailscale Mesh Networking Cheat Sheet |
| `ufw-cheatsheet.md` | UFW (Uncomplicated Firewall) Command Reference for Ubuntu/Debian. |


### 📁 virtualization/ (Hypervisor & VM Runbooks)

| File | Description |
|---|---|
| `Hyper-V_PowerShell_Cheat_Sheet.md` | Hyper-V PowerShell Management Cheat Sheet |
| `proxmox-cheatsheet.md` | Proxmox Virtual Machine Commands (qm) Cheat Sheet |
| `virt-manager-cheatsheet.md` | Virt-Manager & Virsh Command Line Cheat Sheet |
| `virt-manager-docker-conflict.md` | Virt-Manager and Docker: Networking Conflicts Explained |
| `virtualization_virt-manager-troubleshooting-fedora.md` | Virt-Manager troubleshooting guide tailored for Fedora with notes for other distributions. |


### 📁 windows-and-macos/ (Windows & macOS References)

| File | Description |
|---|---|
| `Windows_Sysinternals_Cheat_Sheet.md` | A practical guide to core Microsoft Sysinternals tools (Process Explorer, Process Monitor, Autoruns, PsExec, and TCPView), highlighting specific filters, shortcuts, and commands for advanced troubleshooting, malware isolation, and remote system administration. |
| `Winget_Cheat_Sheet.md` | A quick-reference guide for managing Windows software packages using the Winget command-line tool, covering package discovery, silent installations, bulk upgrades, and system provisioning. |
| `macOS_Terminal_Package_Management_Cheat_Sheet.md` | A quick-reference guide for macOS command-line operations, covering Homebrew package management, system software updates, networking tools, process management, and essential Finder modifications. |
| `windows-cmd-cheatsheet.md` | A quick-reference cheat sheet for Windows Command Prompt (CMD) and PowerShell, covering file navigation, system management, and package provisioning. |
| `windows-powershell-active-directory.md` | A quick-reference guide for Windows PowerShell administration, covering Registry manipulation, Active Directory user and group management, remote networking, and object-oriented data filtering. |
<!-- END_SECTION:tree -->
