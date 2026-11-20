# `setup.sh` - Workstation Setup Script Documentation

The `setup.sh` script in [linux-environment-automation](https://github.com/77777kaz77777/linux-environment-automation/blob/main/provisioning/setup.sh) bootstraps a Linux workstation: it installs a toolstack, adds software repositories, removes unused apps, installs helper scripts, and sets up the shell and terminal. An interactive menu lets you choose exactly which steps run, and the script is safe to run more than once.

## Target Systems & Requirements

- **Supported Distributions:** Red Hat-based systems (Fedora, RHEL, CentOS, AlmaLinux, Rocky Linux) with `dnf` or `dnf5`, and Arch Linux with `pacman`.
- **Privileges:** Run it with `sudo` from your normal user account. It refuses to run as root directly, because shell and desktop settings go to your own home folder.
- **Supported Desktop Environments (DEs):** KDE Plasma, GNOME, COSMIC.

## How It Works

### 1. Initialization and Detection

- **Root Check:** Exits unless it is run with `sudo` from a regular user.
- **Logging:** Writes a timestamped log to `/var/log/workstation-setup-<date>-<time>.log`.
- **System Profiling:** Reads `/etc/os-release` and checks running processes to identify the distribution, version, package manager (`dnf5`, `dnf`, or `pacman`) and the active desktop environment.
- **Menu Setup:** Installs `whiptail` (`newt` or `libnewt`) if it is missing.

### 2. Interactive Selection

A `whiptail` checklist lets you toggle these modules on or off. The KDE wallpaper step is pre-selected only on KDE.

#### PREREQS: Prerequisites & Repositories

- Installs base utilities (`curl`, `flatpak`, Go, `git`, `wget`, `unzip`, `fontconfig`).
- On DNF systems, tunes `/etc/dnf/dnf.conf` by setting only the keys it needs (`installonly_limit`, `max_parallel_downloads`, and others). Your other settings are kept, and a dated backup is saved next to the file.
- Adds the Brave Browser, Sublime Text and Tailscale repositories, each skipped if already configured.
- On Arch, Brave and Sublime Text are skipped because they are AUR-only.

#### CORE: Core Toolstack

- Installs Brave, Firefox, Sublime Text, Podman, btop, VLC, Nmap, Fastfetch, Tailscale, Alacritty and Dolphin (plus Spectacle on KDE).
- Installs everything in one batch, then retries one at a time if the batch fails. Packages not available in your repositories are reported instead of attempted.
- Enables the `tailscaled` service; run `sudo tailscale up` afterwards to log in.

#### DEBLOAT: Desktop Environment Debloat

- Removes common unused apps (such as Thunderbird and LibreOffice) plus a list tailored to the detected desktop (for example KMail on KDE, GNOME Tour on GNOME).
- Only removes packages that are actually installed, then cleans up orphaned dependencies.

#### FLATPAKS: Flatpak Installations

- Adds Flathub and installs LM Studio, Podman Desktop, Zenmap and Trayscale.
- If the Trayscale Flatpak fails, builds it with Go instead.

#### GITHUB: Scripts from linux-environment-automation

- Downloads the [linux-environment-automation](https://github.com/77777kaz77777/linux-environment-automation) repository.
- **The `update` command:** asks which update script to install as `/usr/local/bin/update`, with the one for your distribution pre-selected. It warns you if an older `/usr/local/sbin/update` exists that could run instead.
- **Tool scripts:** a checklist of the scripts in `utils/` and `security/` (none pre-selected). Each one is installed into `/usr/local/bin` without its `.sh` or `.py` extension.

#### TERM: Shell Aliases & Terminal Themes

- Writes aliases (`ll`, `c`, `u` for `sudo update`, and others) and a plain prompt to `~/.bashrc.d/workstation-aliases.sh`. Your existing `~/.bashrc` is kept. If it doesn't already load `~/.bashrc.d`, a loader is added once, with a dated backup.
- Applies a "Pure White on Black" color scheme to every Konsole profile, creating a default profile if there is none.
- Installs the JetBrainsMono Nerd Font and writes an `alacritty.toml` with padding, opacity and colors. Any existing config is backed up first.

#### DESKTOP: KDE Plasma Wallpaper Setup

- Only runs when KDE Plasma is detected.
- Downloads the wallpapers repository, lets you pick an image, copies it to `~/Pictures/Wallpapers`, and applies it.

### 3. Summary

When it finishes, the script lists anything that failed and where the full log is. It exits with an error code if any step failed.

## Usage

1. Download the script and read it before running it:

   ```bash
   curl -fsSLO https://raw.githubusercontent.com/77777kaz77777/linux-environment-automation/main/provisioning/setup.sh
   less setup.sh
   ```

2. Run it with `sudo` from your normal user account:

   ```bash
   sudo bash setup.sh
   ```

3. Follow the on-screen menus.
4. Open a new terminal, or run `source ~/.bashrc`, to use the new aliases.
