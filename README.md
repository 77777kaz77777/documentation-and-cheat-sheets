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
| `lxc-cheatsheet.md` | **📦 LXC/LXD Essentials** |
| `podman-cheatsheet.md` | **🐳 Podman Command Line Cheat Sheet** |
| `podman-desktop-guide.md` | Podman Desktop: Installation and Usage Guide |


### 📁 fedora/ (Fedora Linux Specific Documentation)

| File | Description |
|---|---|
| ` Fedora_NVIDIA_Installation_Guide.md` | The recommended, most stable way to install NVIDIA drivers on Fedora Workstation is through the **RPM Fusion** repositories. Using the official `.run` installer directly from NVIDIA is strongly discouraged on Fedora because kernel updates will frequently break the display driver. |
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
| `Fedora_TPM2_LUKS_AutoUnlock_Guide.md` | 1. Install Dependencies |
| `KDE_Plasma_6_Multi_Monitor_Troubleshooting.md` | KDE Plasma 6 Multi-Monitor Troubleshooting Guide |
| `Snapper_Snapshot_Management_Cheat_Sheet.md` | Snapper Snapshot Management Cheat Sheet |
| `asusctl_cheat_sheet_guide.md` | asusctl v6.3.8 Cheat Sheet (GA503RW) |
| `dnf-speed-optimization-guide.md` | Document Name: dnf-speed-optimization-guide.md |
| `dnf_command_reference.md` | DNF Command Reference Guide |
| `fedora-clamav-setup-guide.md` | ClamAV Setup and Automation Guide for Fedora Linux |
| `fix-mux-plymouth-deadlock.md` | Fixing MUX / Plymouth Boot Deadlock |


### 📁 linux-general/ (General Linux Reference)

| File | Description |
|---|---|
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
| `apk_command_reference.md` | APK Command Reference Guide (Alpine Linux / Containers) |
| `apt_command_reference.md` | APT Command Reference Guide |
| `brew_command_reference.md` | Homebrew Command Reference Guide (macOS / Linux Desktop) |
| `cheatsheet-for-linux.md` | **Package Management Cheat Sheet** |
| `flatpak_command_reference.md` | Flatpak Command Reference Guide (Linux Desktop) |
| `fwupdmgr_Firmware_Update_Cheat_Sheet.md` | fwupdmgr Firmware Update Cheat Sheet |
| `linux_permissions_reference_expanded.md` | Advanced Linux Permissions, Ownership, and Access Control Reference Guide |
| `make_bash_script_executable.md` | How to Make a Bash Script Executable and Callable Globally |
| `ncdu_command_reference.md` | NCDU (NCurses Disk Usage) Command Reference Guide |
| `nmcli-cheat-sheet.md` | nmcli Cheat Sheet |
| `pacman_command_reference.md` | Pacman Command Reference Guide |
| `storage_management_reference.md` | Storage Management Command Reference Guide |
| `zypper_command_reference.md` | Zypper Command Reference Guide (openSUSE / SUSE Linux Enterprise) |


### 📁 networking-and-security/ (Networking & Security Configurations)

| File | Description |
|---|---|
| `AdGuard_Home_Management_Cheat_Sheet.md` | AdGuard Home Management & DNS Filtering Cheat Sheet |
| `OpenWrt_UCI_Command_Cheat_Sheet.md` | OpenWrt UCI (Unified Configuration Interface) Cheat Sheet |
| `Pentesting_Toolkit_Cheat_Sheet.md` | Penetration Testing Toolkit Cheat Sheet |
| `Tailscale_Mesh_CLI_Cheat_Sheet.md` | Tailscale Mesh Networking Cheat Sheet |
| `ufw-cheatsheet.md` |  |


### 📁 virtualization/ (Hypervisor & VM Runbooks)

| File | Description |
|---|---|
| `Hyper-V_PowerShell_Cheat_Sheet.md` | Hyper-V PowerShell Management Cheat Sheet |
| `proxmox-cheatsheet.md` | **🖥️ Proxmox Virtual Machine Commands (qm)** |
| `virt-manager-cheatsheet.md` | **🖥️ Virt-Manager & Virsh Command Line Cheat Sheet** |
| `virt-manager-docker-conflict.md` | Virt-Manager and Docker: Networking Conflicts Explained |
| `virtualization_virt-manager-troubleshooting-fedora.md` |  |


### 📁 windows-and-macos/ (Windows & macOS References)

| File | Description |
|---|---|
| `Winget_Cheat_Sheet.md` | Winget Command Cheat Sheet |
| `macOS_Terminal_Package_Management_Cheat_Sheet.md` | macOS Terminal and Package Management Cheat Sheet |
| `windows-cmd-cheatsheet.md` | **💻 Windows Command Line Comparison** |
| `windows-powershell-active-directory.md` | **Windows PowerShell & Active Directory Essentials** |
<!-- END_SECTION:tree -->
