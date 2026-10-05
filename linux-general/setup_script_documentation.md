# `setup.sh` - Workstation Setup Script Documentation

## Overview

The `setup.sh` script is an automated Bash utility designed to bootstrap a Linux workstation. It handles installing essential toolstacks, adding software repositories, debloating the desktop environment, and configuring terminal interfaces. It features an interactive Terminal User Interface (TUI) that allows the user to select exactly which configuration steps they want to run.

## Target Systems & Requirements

* **Supported Distributions:** Arch Linux and Red Hat-based systems (Fedora, RHEL, CentOS, AlmaLinux, Rocky Linux).

* **Privileges:** The script must be executed with `root` privileges (e.g., using `sudo`).

* **Supported Desktop Environments (DEs):** KDE Plasma, GNOME, Cosmic.

## How It Works

### 1. Initialization and Detection

When executed, the script performs several preliminary checks and setups:

* **Root Check:** Verifies the user is running the script as root; otherwise, it exits.

* **Logging:** Initializes a log file named `workstation_install.log` in the directory where the script is run.

* **System Profiling:** Reads `/etc/os-release` and checks running processes to identify the Linux distribution, version, Package Manager (`dnf5`, `dnf4`, or `pacman`), and the active Desktop Environment.

* **TUI Setup:** Ensures `whiptail` (or `newt`) is installed to provide the interactive graphical menu.

### 2. Interactive Selection (TUI)

The script presents a checklist menu using `whiptail`. Users can toggle the following installation modules on or off:

#### PREREQS: Prerequisites & Repositories

* Installs base utilities (`curl`, `flatpak`, `go`, `git`, `wget`, `unzip`).

* For RPM-based systems (DNF), it optimizes the package manager configuration (`dnf.conf`).

* Adds third-party repositories for Brave Browser, Sublime Text, and Tailscale.

#### CORE: Core Toolstack

* Installs a predefined list of essential applications using the native package manager.

* Packages include: Brave, Firefox, Sublime Text, Podman, Virt-Manager, Btop, VLC, Nmap, Fastfetch, Tailscale, Alacritty, and Dolphin (plus Spectacle for KDE users).

#### DEBLOAT: Desktop Environment Debloat

* Removes common bloatware (like Thunderbird and LibreOffice).

* Applies a tailored removal list based on the detected Desktop Environment to clean up unnecessary default apps (e.g., removing KMail in KDE, or GNOME Tour in GNOME).

* Runs package manager clean-up commands (e.g., `dnf autoremove` or `pacman -Sc`).

#### FLATPAKS: Flatpak Installations

* Adds the Flathub repository.

* Installs specific Flatpak applications: LM Studio, Podman Desktop, and Zenmap.

* Attempts to install Trayscale via Flatpak, falling back to building it from source using Go if the Flatpak installation fails.

#### GITHUB: Maintenance Scripts

* Clones a designated GitHub repository containing system automation scripts (`77777kaz77777/linux-environment-automation`).

* Presents interactive menus allowing the user to copy specific update or tool scripts into `/usr/local/bin/` for system-wide use.

#### TERM: Terminal & Aliases Configuration

* Backs up the current user's `.bashrc` and generates a new one populated with helpful aliases (e.g., `ll`, `c`, `u` for updates) and a customized prompt.

* Configures a "Pure White on Black" color scheme for KDE's **Konsole**.

* Downloads the "JetBrainsMono Nerd Font" and configures **Alacritty** by generating an `alacritty.toml` file with specific window padding, opacity, and color settings.

#### DESKTOP: KDE Plasma Wallpaper Setup

* *(Only executes if the detected DE is KDE Plasma)*

* Clones a wallpaper repository from GitHub.

* Presents a menu of discovered image files, allowing the user to select one.

* Copies the selected image to `~/Pictures/Wallpapers` and applies it automatically via D-Bus commands.

## Usage

1. Make the script executable:

   ```
   chmod +x setup.sh
   
   ```

2. Run the script with sudo:

   ```
   sudo ./setup.sh
   
   ```

3. Follow the on-screen interactive prompts.

4. Once completed, restart your terminal or run `source ~/.bashrc` to apply the shell changes.
