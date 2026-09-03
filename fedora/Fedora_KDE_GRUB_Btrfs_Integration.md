# How to get Btrfs snapshots showing up directly in the GRUB boot menu on Fedora KDE

## Prerequisites

* Fedora KDE installed on a Btrfs filesystem.
* Active snapshot utility configured (snapper or btrbk).
* `git` and `make` installed (`sudo dnf install git make`).

## Phase 1: Fedora Path Compatibility Fix

Fedora stores GRUB configuration files inside `/boot/grub2/`, whereas grub-btrfs defaults to the standard upstream path `/boot/grub/`. Create a symbolic link so grub-btrfs can write its configuration files without errors:

```bash
sudo ln -s /boot/grub2 /boot/grub
```

## Phase 2: Install grub-btrfs

1. Clone the official repository and enter the directory:

```bash
git clone https://github.com/Antynea/grub-btrfs.git
cd grub-btrfs
```
1. Execute the installer:

```bash
sudo make install
```

## Phase 3: Generate GRUB Menu & Enable Daemon

1. Generate the updated GRUB menu containing the Fedora Snapshots entry:

```bash
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```
1. Enable and start the background monitoring service (`grub-btrfsd`). This daemon automatically updates the GRUB boot menu whenever btrbk or snapper creates or deletes a snapshot:

```bash
sudo systemctl enable --now grub-btrfsd
```
1. Verify service status:

```bash
sudo systemctl status grub-btrfsd
```

## Emergency Recovery Procedure (Booting a Snapshot)

If a kernel update, driver issue, or system change prevents Fedora from loading normally:

### 1. Access the GRUB Menu

Turn on your laptop. While the ROG logo is on screen, repeatedly tap Esc (or hold Shift) to bring up the GRUB boot menu.

### 2. Select a Snapshot

1. Navigate down to Fedora Snapshots (or Btrfs Snapshots) and press Enter.
2. Choose the timestamped snapshot created immediately before the issue occurred.
3. Press Enter to boot into the read-only snapshot environment.

### 3. Make the Rollback Permanent

Once booted into your desktop or TTY terminal session, lock in the snapshot so it becomes your active system again:

```bash
sudo snapper rollback
sudo reboot
```

Upon restarting, your system will be permanently restored to that clean state.

## Maintenance & Updates

Because grub-btrfs was installed from source, updates are managed via Git:

* To Update grub-btrfs:

```bash
cd ~/grub-btrfs
git pull
sudo make install
```

* To Uninstall grub-btrfs:

```bash
cd ~/grub-btrfs
sudo make uninstall
sudo systemctl disable --now grub-btrfsd
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```
