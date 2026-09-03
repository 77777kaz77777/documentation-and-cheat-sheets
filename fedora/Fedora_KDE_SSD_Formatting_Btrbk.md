# Steps to format a secondary SSD and set up automated Btrbk snapshots on Fedora KDE

## Prerequisites

* Fedora KDE running on Btrfs (primary drive).
* A secondary internal SSD (e.g., 1TB NVMe drive).
* Administrator (`sudo`) access.

## Phase 1: Wipe & Format Secondary SSD

1. Open **KDE Partition Manager** (`partitionmanager`).
2. Identify the secondary SSD (e.g., `/dev/nvme1n1`, ~953 GiB) by verifying drive size and partition scheme.
3. Select the drive and click **New Partition Table** -> Choose **GPT** -> Click **Apply**.
4. Right-click the unallocated space -> Click **New**:
   * **File system:** `btrfs`
   * **Label:** `Storage`
5. Click **Apply** to write the filesystem. The new partition will be at `/dev/nvme1n1p1`.

## Phase 2: Configure Auto-Mounting (`/etc/fstab`)

### 1. Create the Mount Directory

```bash
sudo mkdir -p /mnt/storage
```

### 2. Retrieve Partition UUID

```bash
sudo blkid /dev/nvme1n1p1
```

*Locate and copy the UUID="..." value from the output.*

### 3. Edit `/etc/fstab`

```bash
sudo nano /etc/fstab
```

Add the following line at the bottom of the file (replace with your actual UUID):

```text
UUID=YOUR-COPIED-UUID-HERE /mnt/storage btrfs defaults,noatime 0 2
```

**Mount Option Breakdown:**

* `defaults`: Enables standard read/write, boot auto-mount, and execution flags.
* `noatime`: Disables access timestamp updates to reduce SSD write wear and improve read speeds.
* `0`: Ignores drive for legacy dump backups.
* `2`: Sets secondary priority for boot filesystem checks (`fsck`).

### 4. Mount & Set User Permissions

```bash
# Test mount configuration without rebooting
sudo mount -a

# Transfer directory ownership to your active user
sudo chown -R $USER:$USER /mnt/storage
```

## Phase 3: Automated Btrfs Snapshots with btrbk

### 1. Install btrbk

```bash
sudo dnf install btrbk
```

### 2. Create the Backup Destination Directory

```bash
sudo mkdir -p /mnt/storage/btrfs-backups
```

### 3. Configure `/etc/btrbk/btrbk.conf`

```bash
sudo nano /etc/btrbk/btrbk.conf
```

Replace the file contents with the following syntax (compatible with btrbk v0.32+):

```text
# Local retention on primary boot SSD (keeps drive clean)
snapshot_preserve_min   latest
snapshot_preserve       2d

# Retention on secondary 1TB backup SSD
target_preserve_min     latest
target_preserve         14d 8w 6m

snapshot_dir            .snapshots

volume /
  subvolume .
    target /mnt/storage/btrfs-backups
```

### 4. Execute Initial Backup & Verification

```bash
sudo btrbk run
```

### 5. Enable Systemd Timer for Background Automation

```bash
sudo systemctl enable --now btrbk.timer
```

## Maintenance & Recovery Quick Reference

### Manual Backup Run

To force an immediate snapshot and sync before major system changes:

```bash
sudo btrbk run
```

### Check Automated Timer Status

```bash
systemctl status btrbk.timer
```

### Restoring from a Snapshot

If a system update causes instability, use **Btrfs Assistant** (GUI):

1. Open **Btrfs Assistant** from the KDE Launcher.
2. Navigate to the **Snapper / Btrbk** tab.
3. Select the desired pre-update snapshot timestamp.
4. Click **Restore Snapshot** and reboot.
