# Advanced fixes and config steps for GRUB and Btrfs integration on Fedora KDE.

## 📋 Prerequisites
Ensure your system meets the following requirements before proceeding:
* **OS:** Fedora KDE installed on a Btrfs filesystem.
* **Snapshot Utility:** Active snapshot tool configured (e.g., `snapper` or `btrbk`).
* **Required Packages:** Install build tools, filesystem utilities, and file-monitoring daemons:
```bash
sudo dnf install git make btrfs-progs inotify-tools
```

## 🛠️ Phase 1: Fedora Compatibility & Environment Setup
Fedora uses distinct directory structures and binary naming conventions compared to upstream Linux distributions. Perform these setup steps first to prevent syntax and daemon execution errors.

### 1. Fix GRUB Directory Path Link
Fedora stores GRUB configuration files inside `/boot/grub2/`, whereas grub-btrfs defaults to `/boot/grub/`. Create a symbolic link:
```bash
sudo ln -s /boot/grub2 /boot/grub
```

### 2. Fix Binary Tool Name Link
grub-btrfs validates syntax using `grub-script-check`, but Fedora prefixes GRUB binaries with `grub2-` (`/usr/bin/grub2-script-check`). Create a symbolic link to prevent script validation failures:
```bash
sudo ln -s /usr/bin/grub2-script-check /usr/bin/grub-script-check
```

### 3. Disable GRUB Auto-Hide & Set Boot Timeout
Fedora auto-hides the GRUB menu on single-boot systems (`menu_auto_hide=1`). Force GRUB to always display at startup with a 5-second timeout:
```bash
sudo grub2-editenv - unset menu_auto_hide
sudo grub2-editenv - set timeout=5
```

## 📦 Phase 2: Install grub-btrfs
Clone the official repository, compile, and install the utility:
```bash
cd ~
git clone https://github.com/Antynea/grub-btrfs.git
cd grub-btrfs
sudo make install
```
**Apply SELinux Contexts**
Because Fedora runs SELinux in Enforcing mode, restore security contexts for the installed binary and systemd service file:
```bash
sudo restorecon -Rv /usr/bin/grub-btrfs* /usr/lib/systemd/system/grub-btrfsd.service
```

## 🚀 Phase 3: Generate GRUB Menu & Enable Monitoring Daemon

### 1. Build the Initial Snapshot Submenu
Run `grub2-mkconfig` to scan for existing snapshots and build the **Fedora Snapshots** submenu:
```bash
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

### 2. Enable the Background Daemon
Enable `grub-btrfsd` so it automatically regenerates the GRUB boot menu whenever Snapper or btrbk creates or deletes a snapshot:
```bash
sudo systemctl enable --now grub-btrfsd
```

### 3. Verify Daemon Health
```bash
sudo systemctl status grub-btrfsd
```

## 🚨 Emergency Recovery Procedure (Booting a Snapshot)
If a kernel update, display driver failure, or system change prevents Fedora from loading normally:
1. **Access the GRUB Menu:** Turn on or restart your laptop. Repeatedly tap **Esc** or **F8** during the splash screen until the GRUB menu appears.
2. **Select and Boot Snapshot:** Navigate down to **Fedora Snapshots** (or **Btrfs Snapshots**) and press **Enter**. Select the timestamped snapshot created immediately before the issue occurred and press **Enter** to boot into the read-only snapshot environment.
3. **Make the Rollback Permanent:** Once booted into your desktop or TTY terminal session, execute a Snapper rollback to lock in the clean snapshot state:
```bash
sudo snapper rollback
sudo reboot
```

## 🔧 Troubleshooting & Common Issues

### Issue 1: `grub-script-check: No such file or directory`
* **Symptom:** `grub2-mkconfig` output reports `grub-btrfs: Error: Syntax errors were detected in generated /boot/grub/grub-btrfs.new file.`
* **Cause:** grub-btrfs cannot locate Fedora's renamed binary `/usr/bin/grub2-script-check`.
* **Resolution:**
```bash
sudo ln -s /usr/bin/grub2-script-check /usr/bin/grub-script-check
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

### Issue 2: `grub-btrfsd.service Fails with status=1/FAILURE`
* **Symptom:** `systemctl status grub-btrfsd` shows `Active: failed (Result: exit-code)`.
* **Cause:** `inotify-tools` is missing or the service was started before creating the binary symlinks.
* **Resolution:**
```bash
sudo dnf install inotify-tools
sudo systemctl restart grub-btrfsd
```

### Issue 3: GRUB Menu Is Skipped During Reboot
* **Symptom:** System boots straight into Fedora without displaying GRUB or snapshot options.
* **Cause:** Fedora's default `menu_auto_hide` feature bypasses the GRUB menu.
* **Resolution:**
```bash
sudo grub2-editenv - unset menu_auto_hide
sudo grub2-editenv - set timeout=5
```

### Issue 4: Snapshots Saved on Secondary Drives Do Not Appear in GRUB
* **Symptom:** Snapshots stored on a secondary NVMe/SSD drive fail to appear as GRUB boot options.
* **Cause:** Btrfs snapshots **cannot cross physical drive or filesystem boundaries**. GRUB can only boot snapshots residing on the primary boot volume (`/.snapshots`).
* **Resolution:** Keep bootable rollback snapshots on the main OS drive. Use secondary drives strictly for secondary backups via `btrfs send/receive` or `btrbk`.

## 🧹 Maintenance & Updates

**To Update grub-btrfs:**
```bash
cd ~/grub-btrfs
git pull
sudo make install
sudo restorecon -Rv /usr/bin/grub-btrfs* /usr/lib/systemd/system/grub-btrfsd.service
sudo systemctl restart grub-btrfsd
```

**To Uninstall grub-btrfs:**
```bash
cd ~/grub-btrfs
sudo systemctl disable --now grub-btrfsd
sudo make uninstall
sudo rm /usr/bin/grub-script-check
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```
