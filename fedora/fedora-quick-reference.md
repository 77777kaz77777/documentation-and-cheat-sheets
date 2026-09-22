# CLI reference for Fedora Linux system administration. Provides direct syntax for DNF package management, systemd service control, journalctl diagnostics, firewalld rules, SELinux enforcement, and network operations

## Package Management (DNF / DNF5)

### System Updates & Maintenance

| Action | Command |
| --- | --- |
| Refresh metadata & update all packages | `sudo dnf upgrade` |
| Refresh package database only | `sudo dnf check-update` |
| Remove unused/orphaned dependencies | `sudo dnf autoremove` |
| Clean all cached package data & metadata | `sudo dnf clean all` |

### Package Operations

| Action | Command |
| --- | --- |
| Search for a package | `dnf search <package>` |
| Display package information | `dnf info <package>` |
| Install package(s) | `sudo dnf install <package>` |
| Reinstall package | `sudo dnf reinstall <package>` |
| Remove package(s) | `sudo dnf remove <package>` |
| Find package providing a specific file or binary | `dnf provides <file_or_path>` |
| List installed packages | `dnf list --installed` |

### Groups & Transaction History

| Action | Command |
| --- | --- |
| List available package groups | `dnf group list` |
| Install a package group | `sudo dnf group install "<group_name>"` |
| View DNF transaction history | `dnf history` |
| Undo a specific transaction | `sudo dnf history undo <transaction_id>` |

---

## Flatpak Application Management

| Action | Command |
| --- | --- |
| Add Flathub repository | `flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo` |
| Search for flatpak applications | `flatpak search <app_name>` |
| Install an application | `flatpak install flathub <app_id>` |
| Update all installed flatpaks | `flatpak update` |
| List installed flatpaks | `flatpak list` |
| Remove an application | `flatpak uninstall <app_id>` |
| Clean up unused runtimes & dependencies | `flatpak uninstall --unused` |
| Grant/revoke filesystem access permissions | `sudo flatpak override <app_id> --filesystem=<path>` |

---

## Service & Systemd Management (`systemctl`)

| Action | Command |
| --- | --- |
| Check status of a service | `systemctl status <service>` |
| Start / Stop / Restart a service | `sudo systemctl start | stop | restart <service>` |
| Enable service on boot | `sudo systemctl enable <service>` |
| Enable and start service immediately | `sudo systemctl enable --now <service>` |
| Disable service from starting on boot | `sudo systemctl disable <service>` |
| Mask / Unmask a service | `sudo systemctl mask | unmask <service>` |
| List all active services | `systemctl list-units --type=service --state=running` |
| List failed services | `systemctl --failed` |

---

## System Logging (`journalctl`)

| Action | Command |
| --- | --- |
| Tail live system logs | `journalctl -f` |
| View logs for a specific service | `journalctl -u <service> -f` |
| View logs for the current boot | `journalctl -b` |
| View logs for the previous boot | `journalctl -b -1` |
| Filter logs by priority (errors/critical) | `journalctl -p err..emerg` |
| Limit log size by age | `sudo journalctl --vacuum-time=7d` |

---

## Security & Firewall (`firewalld` & SELinux)

| Action | Command |
| --- | --- |
| Check firewall status | `sudo firewall-cmd --state` |
| Get active zones and assigned interfaces | `sudo firewall-cmd --get-active-zones` |
| Allow service permanently | `sudo firewall-cmd --add-service=<service> --permanent` |
| Allow TCP/UDP port permanently | `sudo firewall-cmd --add-port=<port>/<tcp | udp> --permanent` |
| Reload firewall configuration | `sudo firewall-cmd --reload` |
| List allowed services/ports in active zone | `sudo firewall-cmd --list-all` |
| Check SELinux status | `sestatus` |
| Change SELinux mode temporarily | `sudo setenforce 0` *(Permissive)* \| `sudo setenforce 1` *(Enforcing)* |

---

## Network Management (`nmcli` & `ip`)

| Action | Command |
| --- | --- |
| List active connections | `nmcli connection show` |
| List network interfaces | `nmcli device status` |
| Connect to a Wi-Fi network | `nmcli dev wifi connect "<SSID>" password "<password>"` |
| Bring a connection up or down | `nmcli connection up | down <connection_name>` |
| Display IP addresses | `ip -brief address` |
| Display routing table | `ip route` |

---

## System Diagnostics & Maintenance

| Action | Command |
| --- | --- |
| Show Fedora release info | `cat /etc/os-release` |
| Show active kernel version | `uname -r` |
| Rebuild initramfs image | `sudo dracut -f` |
| Update GRUB configuration | `sudo grub2-mkconfig -o /boot/grub2/grub.cfg` |
| Check disk usage | `df -h` |
| Check directory space utilization | `du -sh <path>` |
| Hardware summary | `lscpu` / `lspci` / `lsusb` |

---

## Verified Sources & Documentation

- **Fedora Project Documentation**: [https://docs.fedoraproject.org](https://docs.fedoraproject.org)
- **Fedora Quick Docs (DNF)**: [https://docs.fedoraproject.org/en-US/quick-docs/dnf/](https://docs.fedoraproject.org/en-US/quick-docs/dnf/)
- **DNF5 Documentation**: [https://dnf5.readthedocs.io](https://dnf5.readthedocs.io)
- **Firewalld User Documentation**: [https://firewalld.org/documentation/](https://firewalld.org/documentation/)
- **Flatpak Documentation**: [https://docs.flatpak.org](https://docs.flatpak.org)
