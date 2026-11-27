# Fix Wrong Time on Debian, Rocky Linux and Proxmox VE

Fix a wrong clock or time zone and get NTP synchronization working again.

## Before you start

- You need root or `sudo`. On Proxmox you are usually root already, so drop `sudo`.
- NTP needs outbound UDP port 123 and working DNS.
- A large clock jump can upset databases, clusters and Ceph. On production nodes, plan a maintenance window.

| System | Default NTP client | Service | Config file |
| --- | --- | --- | --- |
| Debian | systemd-timesyncd | `systemd-timesyncd` | `/etc/systemd/timesyncd.conf` |
| Rocky Linux | chrony | `chronyd` | `/etc/chrony.conf` |
| Proxmox VE 7+ | chrony | `chrony` | `/etc/chrony/chrony.conf` |

Some installs differ from these defaults. Run only one NTP client at a time.

## 1. Check the current state

```bash
timedatectl
date
date -u
```

If `date -u` is right but `date` is wrong, only the time zone needs fixing. If `date -u` is wrong, fix synchronization.

## 2. Set the time zone (all three)

```bash
timedatectl list-timezones | grep America
sudo timedatectl set-timezone America/Toronto
```

## 3. Fix synchronization

### Debian (systemd-timesyncd)

```bash
sudo apt update
sudo apt install systemd-timesyncd   # removes chrony or ntpsec if installed
sudo systemctl enable --now systemd-timesyncd
sudo timedatectl set-ntp true
```

To choose servers, edit `/etc/systemd/timesyncd.conf`:

```ini
[Time]
NTP=0.pool.ntp.org 1.pool.ntp.org 2.pool.ntp.org
```

```bash
sudo systemctl restart systemd-timesyncd
timedatectl timesync-status
```

If this machine already uses chrony and you want to keep it, follow the Proxmox steps instead.

### Rocky Linux (chrony)

```bash
sudo dnf install chrony
sudo systemctl enable --now chronyd
```

To choose servers, add this to `/etc/chrony.conf`:

```text
pool pool.ntp.org iburst
```

```bash
sudo systemctl restart chronyd
sudo chronyc makestep   # correct the clock immediately
```

### Proxmox VE (chrony)

Run on every node in a cluster.

```bash
apt update
apt install chrony
systemctl enable --now chrony
```

To choose servers, add this to `/etc/chrony/chrony.conf`:

```text
pool pool.ntp.org iburst
```

```bash
systemctl restart chrony
chronyc makestep
```

## 4. Hardware clock (RTC)

Keep the RTC in UTC, then write the corrected system time to it. Do this after synchronization works.

```bash
sudo timedatectl set-local-rtc 0
sudo hwclock --systohc
```

If `hwclock` is missing on Debian or Proxmox, install `util-linux-extra`. On a Windows dual boot, Windows expects local time by default and may show the wrong time after this change.

## 5. Proxmox guests

- **LXC containers** use the host's clock, so fix the host. To match the host's time zone, run `pct set <CTID> --timezone host`, then restart the container.
- **Linux VMs** keep their own time. Follow the steps above inside the VM.
- **Windows VMs** expect a local-time RTC: `qm set <VMID> --localtime 1`, then shut down and start the VM.

## Check it worked

```bash
timedatectl                    # System clock synchronized: yes
timedatectl timesync-status    # timesyncd only
chronyc tracking               # chrony only: Leap status should be Normal
chronyc sources -v             # chrony only: ^* marks the selected server
```

## If it still does not sync

```bash
journalctl -u systemd-timesyncd -b   # Debian
journalctl -u chronyd -b             # Rocky
journalctl -u chrony -b              # Proxmox
getent hosts pool.ntp.org            # does DNS work?
chronyc activity                     # are sources online?
```

- **All chrony sources show `?` or Reach is 0:** check that the firewall or router allows UDP 123, or use your local NTP server (often the router).
- **Time is wrong again after reboot:** check the BIOS/UEFI clock and the CMOS battery.
- **Debian or Rocky VM drifts after suspend or snapshot restore:** restart the NTP service. With chrony, also run `sudo chronyc makestep`.

## Undo

- Time zone: `sudo timedatectl set-timezone <previous zone>`
- Servers: remove the lines you added and restart the service.
- Windows VM setting: `qm set <VMID> --delete localtime`

## Related guides

- [systemd and journalctl Cheat Sheet](systemd-journalctl-cheat-sheet.md)
- [Proxmox Cheat Sheet](../../virtualization/proxmox-cheat-sheet.md)
