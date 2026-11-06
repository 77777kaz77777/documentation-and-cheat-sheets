# CLI reference for Fedora Linux system administration. Provides direct syntax for DNF package management, systemd service control, journalctl diagnostics, firewalld rules, SELinux enforcement, and network operations

## Package Management (DNF / DNF5)

### System Updates & Maintenance

**Refresh metadata & update all packages:**

```bash
sudo dnf upgrade
```

**Refresh package database only:**

```bash
sudo dnf check-update
```

**Remove unused/orphaned dependencies:**

```bash
sudo dnf autoremove
```

**Clean all cached package data & metadata:**

```bash
sudo dnf clean all
```

### Package Operations

**Search for a package:**

```bash
dnf search <package>
```

**Display package information:**

```bash
dnf info <package>
```

**Install package(s):**

```bash
sudo dnf install <package>
```

**Reinstall package:**

```bash
sudo dnf reinstall <package>
```

**Remove package(s):**

```bash
sudo dnf remove <package>
```

**Find package providing a specific file or binary:**

```bash
dnf provides <file_or_path>
```

**List installed packages:**

```bash
dnf list --installed
```

### Groups & Transaction History

**List available package groups:**

```bash
dnf group list
```

**Install a package group:**

```bash
sudo dnf group install "<group_name>"
```

**View DNF transaction history:**

```bash
dnf history
```

**Undo a specific transaction:**

```bash
sudo dnf history undo <transaction_id>
```

---

## Flatpak Application Management

**Add Flathub repository:**

```bash
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
```

**Search for flatpak applications:**

```bash
flatpak search <app_name>
```

**Install an application:**

```bash
flatpak install flathub <app_id>
```

**Update all installed flatpaks:**

```bash
flatpak update
```

**List installed flatpaks:**

```bash
flatpak list
```

**Remove an application:**

```bash
flatpak uninstall <app_id>
```

**Clean up unused runtimes & dependencies:**

```bash
flatpak uninstall --unused
```

**Grant/revoke filesystem access permissions:**

```bash
sudo flatpak override <app_id> --filesystem=<path>
```

---

## Service & Systemd Management (`systemctl`)

| Action                                | Command                                               |                   |                    |
| ------------------------------------- | ----------------------------------------------------- | ----------------- | ------------------ |
| Check status of a service             | `systemctl status <service>`                          |                   |                    |
| Start / Stop / Restart a service      | `sudo systemctl start                                 | stop              | restart <service>` |
| Enable service on boot                | `sudo systemctl enable <service>`                     |                   |                    |
| Enable and start service immediately  | `sudo systemctl enable --now <service>`               |                   |                    |
| Disable service from starting on boot | `sudo systemctl disable <service>`                    |                   |                    |
| Mask / Unmask a service               | `sudo systemctl mask                                  | unmask <service>` |                    |
| List all active services              | `systemctl list-units --type=service --state=running` |                   |                    |
| List failed services                  | `systemctl --failed`                                  |                   |                    |

---

## System Logging (`journalctl`)

**Tail live system logs:**

```bash
journalctl -f
```

**View logs for a specific service:**

```bash
journalctl -u <service> -f
```

**View logs for the current boot:**

```bash
journalctl -b
```

**View logs for the previous boot:**

```bash
journalctl -b -1
```

**Filter logs by priority (errors/critical):**

```bash
journalctl -p err..emerg
```

**Limit log size by age:**

```bash
sudo journalctl --vacuum-time=7d
```

---

## Security & Firewall (`firewalld` & SELinux)

**`Check firewall status` — sudo firewall-cmd --state:**

```bash

```

**`Get active zones and assigned interfaces` — sudo firewall-cmd --get-active-zones:**

```bash

```

**`Allow service permanently` — sudo firewall-cmd --add-service=<service> --permanent:**

```bash

```

**`Allow TCP/UDP port permanently` — `sudo firewall-cmd --add-port=<port>/<tcp:**

```bash
udp> --permanent`
```

**`Reload firewall configuration` — sudo firewall-cmd --reload:**

```bash

```

**`List allowed services/ports in active zone` — sudo firewall-cmd --list-all:**

```bash

```

**`Check SELinux status` — sestatus:**

```bash

```

**`Change SELinux mode temporarily` — `sudo setenforce 0` _(Permissive)_ \:**

```bash
`sudo setenforce 1` _(Enforcing)_
```

---

## Network Management (`nmcli` & `ip`)

**List active connections:**

```bash
nmcli connection show
```

**List network interfaces:**

```bash
nmcli device status
```

**Connect to a Wi-Fi network:**

```bash
nmcli dev wifi connect "<SSID>" password "<password>"
```

**Bring a connection up or down:**

```bash
`nmcli connection up
```

**Display IP addresses:**

```bash
ip -brief address
```

**Display routing table:**

```bash
ip route
```

---

## System Diagnostics & Maintenance

**Show Fedora release info:**

```bash
cat /etc/os-release
```

**Show active kernel version:**

```bash
uname -r
```

**Rebuild initramfs image:**

```bash
sudo dracut -f
```

**Update GRUB configuration:**

```bash
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

**Check disk usage:**

```bash
df -h
```

**Check directory space utilization:**

```bash
du -sh <path>
```

**Hardware summary:**

```bash
`lscpu` / `lspci` / `lsusb`
```

---

## Verified Sources & Documentation

- **Fedora Project Documentation**: [https://docs.fedoraproject.org](https://docs.fedoraproject.org)
- **Fedora Quick Docs (DNF)**: [https://docs.fedoraproject.org/en-US/quick-docs/dnf/](https://docs.fedoraproject.org/en-US/quick-docs/dnf/)
- **DNF5 Documentation**: [https://dnf5.readthedocs.io](https://dnf5.readthedocs.io)
- **Firewalld User Documentation**: [https://firewalld.org/documentation/](https://firewalld.org/documentation/)
- **Flatpak Documentation**: [https://docs.flatpak.org](https://docs.flatpak.org)
