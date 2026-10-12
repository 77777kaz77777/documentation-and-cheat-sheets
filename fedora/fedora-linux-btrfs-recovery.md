# CLI methods for rescuing a corrupted Btrfs filesystem on Fedora

## Scenario 1: You can reach a TTY / Command Line Terminal

If your system boots to a black screen, terminal prompt, or you can press **Ctrl + Alt + F3** to reach a login prompt:

### Method A: Quick Snapper Rollback (If Snapper is functional)

1. Log in with your username and password.
2. List available snapshots:

```bash
sudo snapper -c root list
```

1. Roll back to a snapshot number created *before* the issue occurred (e.g., #2):

```bash
sudo snapper -c root rollback 2
```

1. Reboot your system:

```bash
sudo reboot
```

## Scenario 2: System Won't Boot at All (Using a Fedora Live USB)

If an update completely broke the bootloader or kernel, boot into a **Fedora Live USB** and restore the root snapshot directly from your 1TB secondary drive (`/mnt/storage/btrfs-backups/`).

### 1. Boot Fedora Live USB & Open Terminal

Identify primary and secondary NVMe partitions.

1. Insert your Fedora Live USB drive and boot into it.
2. Open the terminal.
3. Identify your drive partitions using `lsblk`:
   * **Primary 500GB SSD:** `/dev/nvme0n1p3` (or similar main Btrfs partition).
   * **Secondary 1TB SSD:** `/dev/nvme1n1p1` (contains your `btrfs-backups` folder).

### 2. Mount Primary and Secondary Drives

Mount `subvolid=5` to access top-level Btrfs structure. Create temporary mount points and mount both drives:

```bash
# Mount top-level root of your primary 500GB drive
sudo mkdir -p /mnt/primary
sudo mount -o subvolid=5 /dev/nvme0n1p3 /mnt/primary

# Mount your 1TB backup drive
sudo mkdir -p /mnt/backup
sudo mount /dev/nvme1n1p1 /mnt/backup
```

### 3. Move Broken Root Subvolume

Preserve the broken subvolume just in case. In Fedora Btrfs, your active operating system lives in a subvolume named `root`. Rename it out of the way:

```bash
sudo mv /mnt/primary/root /mnt/primary/root_broken
```

### 4. Send Backup from 1TB SSD to Primary SSD

Stream the backup from the 1TB drive back to the 500GB primary drive.

1. List the backups stored on your 1TB drive to find the timestamp you want to restore:

```bash
ls -la /mnt/backup/btrfs-backups/
```

1. Send and receive the snapshot (replace `ROOT.20260813T1431` with your actual backup folder name):

```bash
sudo btrfs send /mnt/backup/btrfs-backups/ROOT.20260813T1431 | sudo btrfs receive /mnt/primary/
```

### 5. Rename Subvolume & Enable Write Access

Make the restored snapshot active and writable.

1. Rename the transferred snapshot back to `root`:

```bash
sudo mv /mnt/primary/ROOT.20260813T1431 /mnt/primary/root
```

1. Backups transferred via `btrfs send/receive` are marked **read-only**. Remove the read-only flag so Fedora can boot and write to it normally:

```bash
sudo btrfs property set -ts /mnt/primary/root ro false
```

### 6. Clean Up & Reboot

Unmount clean and restart. Unmount the partitions and reboot back into your restored OS:

```bash
sudo umount /mnt/primary
sudo umount /mnt/backup
sudo reboot
```

## Post-Recovery Cleanup

Once you successfully log back into Fedora:

1. You can safely delete the broken root directory leftover from the recovery step:

```bash
sudo btrfs subvolume delete /root_broken
```

1. Run `sudo btrbk run` to create a fresh baseline snapshot on your 1TB drive.
