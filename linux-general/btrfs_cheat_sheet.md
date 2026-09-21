# Btrfs Comprehensive Cheat Sheet

**Btrfs** (B-tree FS / Better FS) is a modern Copy-on-Write (CoW) filesystem for Linux focused on fault tolerance, repair, and easy administration.

---

## 1. Installation & Basic Utilities

### Install Userspace Tools

| Distribution | Command |
| :--- | :--- |
| **Debian / Ubuntu** | `sudo apt install btrfs-progs` |
| **RHEL / Fedora** | `sudo dnf install btrfs-progs` |
| **Arch Linux** | `sudo pacman -S btrfs-progs` |
| **Alpine Linux** | `sudo apk add btrfs-progs` |

---

## 2. Creating & Mounting Filesystems

### Create a Btrfs Filesystem

```bash
# Single drive with default label
sudo mkfs.btrfs -L "DataDrive" /dev/sdb

# Force overwrite existing signatures
sudo mkfs.btrfs -f -L "DataDrive" /dev/sdb

# Multi-device setup (RAID1 for data and metadata across 2 drives)
sudo mkfs.btrfs -d raid1 -m raid1 -L "MyRaid" /dev/sdb /dev/sdc
```

### Mount Options

```bash
# Standard mount
sudo mount /dev/sdb /mnt/btrfs

# Mount with transparent compression (zstd)
sudo mount -o compress=zstd /dev/sdb /mnt/btrfs

# Mount with compression level (zstd:1 to zstd:15)
sudo mount -o compress=zstd:3 /dev/sdb /mnt/btrfs

# Mount specific subvolume by name or ID
sudo mount -o subvol=@home /dev/sdb /home
sudo mount -o subvolid=256 /dev/sdb /mnt/subvol
```

---

## 3. Subvolumes & Snapshots

Btrfs subvolumes act like independent filesystems within a single Btrfs volume.

### Managing Subvolumes

```bash
# Create a subvolume
sudo btrfs subvolume create /mnt/btrfs/@data

# List all subvolumes in a filesystem
sudo btrfs subvolume list /mnt/btrfs

# List subvolumes with detailed paths and layout
sudo btrfs subvolume list -p -t /mnt/btrfs

# Show default subvolume (mounted when no subvol flag is specified)
sudo btrfs subvolume get-default /mnt/btrfs

# Change default subvolume by ID
sudo btrfs subvolume set-default 256 /mnt/btrfs

# Delete a subvolume
sudo btrfs subvolume delete /mnt/btrfs/@data
```

### Creating & Managing Snapshots

Snapshots are instant, copy-on-write subvolumes.

```bash
# Create a read-write snapshot
sudo btrfs subvolume snapshot /mnt/btrfs/@data /mnt/btrfs/@data_snapshot

# Create a read-only snapshot (Recommended for backups)
sudo btrfs subvolume snapshot -r /mnt/btrfs/@data /mnt/btrfs/@data_ro_snap

# Delete a snapshot (treated same as deleting a subvolume)
sudo btrfs subvolume delete /mnt/btrfs/@data_ro_snap
```

---

## 4. Send & Receive (Backups & Replication)

Transfer snapshots efficiently across locations or drives.

```bash
# Send a read-only snapshot to a file (for archive)
sudo btrfs send /mnt/btrfs/@data_ro_snap > /backups/data_snap.img

# Receive a snapshot from a file
sudo btrfs receive /mnt/backups < /backups/data_snap.img

# Send/Stream snapshot directly to another Btrfs mount (Local or Remote over SSH)
# Local transfer:
sudo btrfs send /mnt/btrfs/@data_ro_snap | sudo btrfs receive /mnt/backup_drive/

# Remote transfer over SSH:
sudo btrfs send /mnt/btrfs/@data_ro_snap | ssh user@remote "sudo btrfs receive /backups/"

# Incremental Send (Only sends differences between snap1 and snap2)
sudo btrfs send -p /mnt/btrfs/@snap_v1 /mnt/btrfs/@snap_v2 | sudo btrfs receive /mnt/backup_drive/
```

---

## 5. Storage Space & Usage Analysis

Standard `df -h` often displays inaccurate available space on Btrfs. Use native commands:

```bash
# Overview of overall filesystem usage
sudo btrfs filesystem usage /mnt/btrfs

# Detailed breakdown of data/metadata allocation
sudo btrfs device usage /mnt/btrfs

# Show filesystem summary and UUIDs
sudo btrfs filesystem show
```

### Quotas (Optional Usage Limits)

```bash
# Enable quota handling
sudo btrfs quota enable /mnt/btrfs

# Show quota group (qgroup) usage
sudo btrfs qgroup show /mnt/btrfs

# Limit a subvolume size (e.g., limit subvolume ID 256 to 50GB)
sudo btrfs qgroup limit 50G 0/256 /mnt/btrfs
```

---

## 6. Device Management & Dynamic RAID

Btrfs allows adding, removing, and rebalancing drives live while mounted.

### Adding & Removing Devices

```bash
# Add a new drive to an existing filesystem
sudo btrfs device add /dev/sdd /mnt/btrfs

# Remove a device (data automatically migrates off the drive first)
sudo btrfs device remove /dev/sdb /mnt/btrfs

# Replace a failing drive online (/dev/sdb replaced with /dev/sde)
sudo btrfs replace start /dev/sdb /dev/sde /mnt/btrfs

# Check status of ongoing replace operation
sudo btrfs replace status /mnt/btrfs
```

### Converting / Balancing RAID Profiles

A balance operation re-allocates chunk trees to re-balance space or change RAID levels on the fly.

```bash
# Run a basic balance across all drives
sudo btrfs balance start /mnt/btrfs

# Convert Data to RAID1 and Metadata to RAID1
sudo btrfs balance start -dconvert=raid1 -mconvert=raid1 /mnt/btrfs

# Convert Data to Single and Metadata to DUP
sudo btrfs balance start -dconvert=single -mconvert=dup /mnt/btrfs

# Monitor balance progress
sudo btrfs balance status /mnt/btrfs

# Cancel or Pause a running balance
sudo btrfs balance cancel /mnt/btrfs
sudo btrfs balance pause /mnt/btrfs
```

> **Warning:** Btrfs RAID5/6 modes are considered unstable for production workloads. Stick to RAID0, RAID1, RAID10, or DUP.

---

## 7. Maintenance, Scrubbing & Repair

### Scrubbing (Checksum Verification)

Scrub reads all data and metadata, verifies checksums, and automatically repairs corrupt blocks using redundant copies (RAID1/DUP).

```bash
# Start background scrub
sudo btrfs scrub start /mnt/btrfs

# Check status/progress of scrub
sudo btrfs scrub status /mnt/btrfs

# Cancel running scrub
sudo btrfs scrub cancel /mnt/btrfs
```

### Defragmentation & Compression

```bash
# Defragment a single file or entire folder/subvolume
sudo btrfs filesystem defragment -r /mnt/btrfs/@data

# Defragment and apply compression at the same time
sudo btrfs filesystem defragment -r -czstd /mnt/btrfs/@data
```

### Checking Hardware Error Counters

```bash
# View read/write/checksum errors per physical device
sudo btrfs device stats /mnt/btrfs

# Reset stats counters back to 0
sudo btrfs device stats -z /mnt/btrfs
```

---

## 8. Handy One-Liners & Systemd Automation

```bash
# Find top subvolumes by space consumed (requires quota enabled)
sudo btrfs qgroup show --sort=excl /mnt/btrfs

# Monthly Scrub Cron Job / Systemd Timer Command
sudo btrfs scrub start -B /mnt/btrfs
```