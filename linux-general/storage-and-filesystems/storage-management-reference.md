# Storage Management Command Reference Guide

Commands to manage block devices, format partitions, and handle filesystems.

## Block Devices and Partitions

**List all block devices (disks and partitions).**

```bash
lsblk
```

**List all block devices with file system information (UUIDs and labels).**

```bash
lsblk -f
```

**List block devices with specific columns (name, size, type, mountpoint).**

```bash
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT
```

**List disk partition tables and sizes (requires root).**

```bash
fdisk -l
```

**Open the interactive partition manager for a specific drive.**

```bash
fdisk /dev/nvme0n1
```

## Disk Space and Usage

**Show file system disk space usage in human-readable format.**

```bash
df -h
```

**Show file system disk space usage including the file system type.**

```bash
df -h -T
```

**Estimate file space usage for a specific directory in human-readable format.**

```bash
du -s -h /path/to/directory
```

**List the sizes of all files and directories in the current location.**

```bash
du -s -h *
```

## Mounting and Unmounting

**Mount a storage device to a directory.**

```bash
mount /dev/sda1 /mnt/storage
```

**Unmount a storage device from its directory.**

```bash
umount /mnt/storage
```

**Reload all mount points defined in `/etc/fstab`.**

```bash
mount -a
```

## BTRFS File System Management

**Show information about all BTRFS file systems.**

```bash
btrfs filesystem show
```

**Show disk space usage specific to a BTRFS file system.**

```bash
btrfs filesystem df /mnt/btrfs_storage
```

**List all BTRFS subvolumes under a specific path.**

```bash
btrfs subvolume list /mnt/btrfs_storage
```

**Create a new BTRFS subvolume.**

```bash
btrfs subvolume create /mnt/btrfs_storage/@new_subvol
```

**Start a balance operation on a BTRFS file system to reclaim space.**

```bash
btrfs balance start /mnt/btrfs_storage
```

## XFS File System Management

For the full guide, see the [XFS Cheat Sheet](xfs-cheat-sheet.md).

**Create an XFS file system with a label.**

```bash
mkfs.xfs -L data /dev/sdb1
```

**Show the geometry and enabled features of a mounted XFS file system.**

```bash
xfs_info /mnt/xfs_storage
```

**Grow a mounted XFS file system to fill its partition or logical volume (XFS cannot be shrunk).**

```bash
xfs_growfs /mnt/xfs_storage
```

**Check an unmounted XFS file system without making changes.**

```bash
xfs_repair -n /dev/sdb1
```

**Show a human-readable quota report for an XFS file system.**

```bash
xfs_quota -x -c "report -h" /mnt/xfs_storage
```

## Snapper and Snapshot Management

**List all existing snapshots for the default configuration (usually root).**

```bash
snapper list
```

**List snapshots for a specific configuration.**

```bash
snapper -c home list
```

**Create a manual snapshot with a description.**

```bash
snapper create -d "Before system update" -c timeline
```

**Delete a specific snapshot by its number.**

```bash
snapper delete 42
```
