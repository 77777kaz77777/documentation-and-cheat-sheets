## A quick comparison of commands across the most common Linux package managers.

This table covers the essential commands for managing software. Whether you're using **Debian/Ubuntu** (APT), **RHEL/Fedora/Rocky** (DNF), or **Arch** (Pacman), these are your bread-and-butter commands.
|  |  |  |  |
| :- | :- | :- | :- |
| Action | Debian / Ubuntu | RHEL / CentOS / Fedora | Arch Linux |
| **Update Repos** | sudo apt update | sudo dnf check-update | sudo pacman -Sy |
| **Upgrade System** | sudo apt upgrade | sudo dnf upgrade | sudo pacman -Syu |
| **Install Package** | sudo apt install [pkg] | sudo dnf install [pkg] | sudo pacman -S [pkg] |
| **Remove Package** | sudo apt remove [pkg] | sudo dnf remove [pkg] | sudo pacman -R [pkg] |
| **Search for Pkg** | apt search [query] | dnf search [query] | pacman -Ss [query] |
| **Clean Cache** | sudo apt autoremove | sudo dnf clean all | sudo pacman -Sc |
| **Show Info** | apt show [pkg] | dnf info [pkg] | pacman -Si [pkg] |

## **System Maintenance & Info**
While many core commands (like ls, cd, grep) are universal, the way these systems handle services and identification can vary slightly.
### **Service Management (Systemd)**
*Most modern versions of all these distros use systemctl, so these are largely universal now:*
  - **Start a service:** sudo systemctl start [service]
  - **Enable on boot:** sudo systemctl enable [service]
  - **Check status:** systemctl status [service]
### **System Identification**
If you forget which box you're logged into, use these:
  - **Universal:** cat /etc/os-release
  - **Debian/Ubuntu specific:** lsb_release -a
  - **Red Hat specific:** cat /etc/redhat-release
## **Key Differences at a Glance**
  - **Debian/Ubuntu:** Uses .deb packages. Known for stability (Debian) and user-friendliness (Ubuntu).
  - **RHEL/Fedora:** Uses .rpm packages. Fedora is the "bleeding edge" upstream for the rock-solid Red Hat Enterprise Linux.
  - **Arch Linux:** Uses a "rolling release" model. You install it once and update forever; there are no "major versions" like Ubuntu 24.04.
  - **The AUR:** Arch users have access to the **Arch User Repository**, a massive community-driven library usually accessed via a "helper" like yay (e.g., yay -S [package]).
