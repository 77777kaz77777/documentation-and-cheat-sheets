# Workstation Bootstrap & Toolstack Installer Documentation

## Overview

The **Automated Python Workstation Bootstrap & Toolstack Installer** is a cross-distribution Linux deployment utility featuring a graphical user interface (GUI). It automates the setup of core development toolstacks, third-party repositories, system debloat routines, repository-managed maintenance scripts, and terminal/shell customizations.

## System Requirements & Prerequisites

* **Operating System:** Linux (Tested/Optimized for Fedora, RHEL, Rocky Linux, Ubuntu, Debian, and Arch-based distributions).
* **Python Version:** Python 3.x
* **Privileges:** Root (Sudo) access is required to execute system-level package installations and write to global directories.

### Required System Packages

Before executing the script, ensure your system has the standard GUI library and package management prerequisites installed:

* **Fedora / RHEL / Rocky Linux:**
  ~~~bash
  sudo \
  dnf \
  install \
  python3-tkinter
  ~~~
* **Ubuntu / Debian:**
  ~~~bash
  sudo \
  apt-get \
  install \
  python3-tk
  ~~~
* **Arch Linux:**
  ~~~bash
  sudo \
  pacman \
  -S \
  python-tkinter
  ~~~

---

## Installation & Execution Guide

1. Save the installer script to your local machine (e.g., `setup.py`).
2. Grant execution permissions or run directly with administrative privileges using Python:
   ~~~bash
   sudo \
   python3 \
   -E \
   setup.py
   ~~~

*(Note: The `-E` flag is recommended to preserve necessary environment variables during `sudo` execution).*

---

## Installer Features & GUI Options

When the GUI launches, you can toggle the following modular installation stages via checkboxes:

* **Install Prerequisites & Repositories:** Installs core utilities (`curl`, `flatpak`, `golang`, `git`, `wget`) and configures third-party repositories for **Brave Browser**, **Sublime Text**, and **Tailscale** (with dynamic version resolution for RHEL/Rocky and Debian/Ubuntu). It also applies parallel download optimizations to `dnf.conf` on Red Hat-based systems.
* **Install Core Toolstack:** Deploys developer tools and daily-driver applications:
  * Brave Browser (`brave-origin` or `brave-browser`)
  * Firefox
  * Sublime Text
  * Podman
  * Virt-Manager / QEMU
  * `btop`, `vlc`, `nmap`, `fastfetch`, and `tailscale`
  * KDE Spectacle (automatically added if KDE Desktop is detected)
* **Execute Distro/DE Debloat Routine:** Automatically purges pre-installed system bloat, unused office suites, and mail clients tailored to your active Desktop Environment (KDE, Cosmic, Cinnamon, or generic) and package manager, followed by orphan package cleanup.
* **Install Flatpaks & Trayscale:** Adds the Flathub remote and installs **LM Studio**, **Podman Desktop**, **Zenmap**, and **Trayscale** (with a fallback to build via Go if the Flatpak fails).
* **Clone & Install GitHub Maintenance Scripts:** Clones the remote repository (`77777kaz77777/linux-maintenance-and-dotfiles`), prompting interactive GUI dialogs for you to choose preferred update scripts (installed to `/usr/local/bin/update`) and additional root utility scripts.
* **Configure Shell Aliases & Terminal Theme:** Appends standard color-supported `ls` and `grep` aliases to `.bashrc` and executes a terminal setup script configuring a pure white text on black background theme for KDE Konsole.

---

## Post-Installation Notes

* **Execution Logs:** Every run exports a detailed step-by-step execution audit log to `workstation_install.log` in the local directory.
* **Global Command Path (`/usr/local/bin`):** Installed scripts placed in `/usr/local/bin` require proper `sudo` path configurations on enterprise distributions like Rocky Linux. If a command says "not found" when run with `sudo`, ensure `:/usr/local/bin` is included in your `secure_path` via `sudo visudo`, or execute them using their absolute path (e.g., `sudo /usr/local/bin/update`).
