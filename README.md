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
| `Docker_CLI_Compose_Cheat_Sheet.md` | Docker CLI & Compose Cheat Sheet |
| `lxc-cheatsheet.md` | LXC/LXD Essentials Cheat Sheet |
| `podman-cheatsheet.md` | Essential commands for running daemonless containers with Podman. |
| `podman-desktop-guide.md` | How to install and set up the Podman Desktop GUI |


### 📁 fedora/ (Fedora Linux Specific Documentation)

| File | Description |
|---|---|
| ` Fedora_NVIDIA_Installation_Guide.md` | A guide to safely installing NVIDIA drivers on Fedora Workstation utilizing RPM Fusion repositories. |
| `Btrbk_Snapshot_Automation_Cheat_Sheet.md` | Btrbk Snapshot & Backup Automation Cheat Sheet |
| `ClamAV_SELinux_Implementation_Guide.md` | Comprehensive ClamAV & SELinux Implementation Guide (Fedora 44) |
| `DNF_Configuration_Guide.md` | DNF Configuration Guide |
| `Fedora_DNF5_Tailscale_Repository_Fix.md` | Fedora 41+ (DNF5) Tailscale Repository Setup & Syntax Guide |
| `Fedora_Firewall_Cheat_Sheet.md` | Fedora Linux Firewall (Firewalld) Cheat Sheet |
| `Fedora_KDE_GRUB_Btrfs_Advanced.md` | Fedora KDE - Advanced GRUB Btrfs Configuration & Troubleshooting |
| `Fedora_KDE_GRUB_Btrfs_Integration.md` | Fedora KDE - GRUB Btrfs Snapshot Integration Guide |
| `Fedora_KDE_SSD_Formatting_Btrbk.md` | Fedora KDE - Secondary SSD Formatting & Automated Btrbk Runbook |
| `Fedora_Linux_Btrfs_Recovery.md` | Fedora Linux - Command-Line Btrfs Recovery Methods |
| `Fedora_SELinux_Cheat_Sheet.md` | Fedora Linux SELinux Cheat Sheet |
| `Fedora_TPM2_LUKS_AutoUnlock_Guide.md` | Step-by-step guide for configuring automatic LUKS2 root volume decryption using hardware TPM 2.0 and systemd-cryptenroll. |
| `KDE_Plasma_6_Multi_Monitor_Troubleshooting.md` | KDE Plasma 6 Multi-Monitor Troubleshooting Guide |
| `Snapper_Snapshot_Management_Cheat_Sheet.md` | Snapper Snapshot Management Cheat Sheet |
| `asusctl_cheat_sheet_guide.md` | asusctl v6.3.8 Cheat Sheet (GA503RW) |
| `dnf-speed-optimization-guide.md` | DNF Package Manager Speed Optimization & Configuration Guide |
| `dnf_command_reference.md` | DNF Command Reference Guide |
| `fedora-alacritty-setup-and-verification.md` | Complete guide for installing and configuring the Alacritty terminal emulator on Fedora 44 KDE, featuring a matte black color scheme, JetBrains Mono Nerd Font integration, and custom workflow keybindings. |
| `fedora-clamav-setup-guide.md` | ClamAV Setup and Automation Guide for Fedora Linux |
| `fix-mux-plymouth-deadlock.md` | Fixing MUX / Plymouth Boot Deadlock |
| `selinux-context-resolution.md` | SELinux Context Resolution |


### 📁 linux-general/ (General Linux Reference)

| File | Description |
|---|---|
| `Enterprise_Linux_Ecosystem_and_Commands_2026.md` | An overview of the 2026 Enterprise Linux ecosystem—detailing the relationship between Fedora, CentOS Stream, RHEL, and Rocky Linux—paired with an essential command reference guide for package (DNF5), service (systemd), network (NetworkManager), firewall (firewalld), and SELinux administration. |
| `Fastfetch_Configuration_Guide.md` | Fastfetch Configuration & Customization Guide |
| `Git_Dotfiles_Maintenance_Cheat_Sheet.md` | Git Dotfiles & Maintenance Scripts Cheat Sheet |
| `KDE_Plasma_Wayland_Shortcuts_Cheat_Sheet.md` | KDE Plasma (Wayland) Shortcuts & Control Cheat Sheet |
| `Linux_Export_Command_Guide.md` | Deep Dive: Linux `export` Command & Environment Variables |
| `Linux_Systemd_Cheat_Sheet.md` | Linux Systemd Service & Management Cheat Sheet |
| `Linux_Upstream_Midstream_Downstream_Explained.md` | Open Source Software Flow: Upstream, Midstream, and Downstream |
| `Linux_Ventoy_USB_Creation_Guide.md` | How to Create a Ventoy USB on Fedora Linux |
| `NVIDIA_CUDA_Monitoring_Cheat_Sheet.md` | NVIDIA & CUDA Monitoring Cheat Sheet |
| `SS_Command_Options_Cheat_Sheet.md` | ss Command Options Cheat Sheet |
| `Sublime_Text_Linux_Shortcuts.md` | Sublime Text Shortcuts (Linux) |
| `Vim_Vi_Editor_Cheat_Sheet.md` | Vi / Vim Text Editor Cheat Sheet |
| `ZFS_Administration_Cheat_Sheet.md` | A technical reference detailing essential commands for managing ZFS physical storage pools and logical datasets, including pool creation, dataset properties, snapshot replication, and disk replacement workflows |
| `apk_command_reference.md` | APK Command Reference Guide (Alpine Linux / Containers) |
| `apt_command_reference.md` | APT Command Reference Guide |
| `brew_command_reference.md` | Homebrew Command Reference Guide (macOS / Linux Desktop) |
| `cheatsheet-for-linux.md` | **Package Management Cheat Sheet** |
| `flatpak_command_reference.md` | Flatpak Command Reference Guide (Linux Desktop) |
| `fwupdmgr_Firmware_Update_Cheat_Sheet.md` | fwupdmgr Firmware Update Cheat Sheet |
| `linux_permissions_reference_expanded.md` | Advanced Linux Permissions, Ownership, and Access Control Reference Guide |
| `linux_source_installation_guide.md` | Comprehensive guide for building and installing software from source code on Linux. |
| `make_bash_script_executable.md` | How to Make a Bash Script Executable and Callable Globally |
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
