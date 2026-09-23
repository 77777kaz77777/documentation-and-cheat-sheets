## quick-reference guide for managing Btrfs filesystems

**Btrfs** (B-tree Filesystem / Better FS) is a modern Copy-on-Write (CoW) filesystem for Linux designed for fault tolerance, online repair, flexible multi-device management, and instant snapshotting.

---

## 1. Installation & Utility Setup

### Install Userspace Tools

```bash
# RHEL / Fedora
sudo dnf install btrfs-progs

# Debian / Ubuntu
sudo apt install btrfs-progs

# Arch Linux
sudo pacman -S btrfs-progs

# Alpine Linux
sudo apk add btrfs-progs
```

### Verify Kernel Module & Drivers

```bash
# Check if btrfs kernel module is loaded
lsmod | grep btrfs

# Load the module manually if required
sudo modprobe btrfs
```

---

## 2. Filesystem Creation & Mount Options

### Create a Btrfs Volume

```bash
# Single drive with filesystem label
sudo mkfs.btrfs -L "DataDrive" /dev/sdb

# Force overwrite existing partition tables/signatures
sudo mkfs.btrfs -f -L "DataDrive" /dev/sdb

# Specify node size (default: 16KiB) and sector size (default: 4KiB)
sudo mkfs.btrfs -n 32k -s 4k -L "HighPerformance" /dev/sdb

# Multi-device initial setup (RAID1 data and metadata across 2 drives)
sudo mkfs.btrfs -d raid1 -m raid1 -L "MyRaid" /dev/sdb /dev/sdc
```

### Recommended Mount Options

| Option | Description |
| :--- | :--- |
| `compress=zstd:N` | Enables ZSTD transparent compression at level `N` (1 to 15, default is 3). |
| `compress-force=zstd:N` | Forces compression on all files, bypassing initial compressibility heuristics. |
| `noatime` | Disables access-time updates on files, reducing unnecessary CoW write cycles. |
| `discard=async` | Enables asynchronous TRIM for SSDs/NVMe drives without blocking I/O. |
| `autodefrag` | Automatically detects random small writes and queues them for defragmentation. |
| `space_cache=v2` | Uses free space tree (v2 cache) for fast free space tracking on large drives. |
| `commit=N` | Sets data flush interval to disk in seconds (default is `30`). |
| `nodatacow` | Disables Copy-on-Write for all new files on the mounted subvolume/filesystem. |

### Mount Commands

```bash
# Mount with ZSTD compression and asynchronous TRIM for SSDs
sudo mount -o compress=zstd:3,noatime,discard=async,space_cache=v2 /dev/sdb /mnt/btrfs

# Mount specific subvolume by path name
sudo mount -o subvol=@home,compress=zstd /dev/sdb /home

# Mount specific subvolume by internal subvolume ID (subvolid)
sudo mount -o subvolid=256,noatime /dev/sdb /mnt/subvol
```

---

## 3. Subvolumes, Snapshots & Rollbacks

Subvolumes are independently mountable POSIX file trees within a single Btrfs storage pool.

### Subvolume Management

```bash
# Create subvolumes (Standard flat layout pattern)
sudo btrfs subvolume create /mnt/btrfs/@
sudo btrfs subvolume create /mnt/btrfs/@home
sudo btrfs subvolume create /mnt/btrfs/@snapshots

# List all subvolumes with path details and parent IDs
sudo btrfs subvolume list -p -t /mnt/btrfs

# Show currently designated default subvolume
sudo btrfs subvolume get-default /mnt/btrfs

# Change default mounted subvolume by ID (ID 5 is top-level root)
sudo btrfs subvolume set-default 256 /mnt/btrfs

# Delete a subvolume (must be empty of child subvolumes)
sudo btrfs subvolume delete /mnt/btrfs/@snapshots/snap_old
```

### Snapshots & Atomic Rollbacks

Snapshots are zero-copy, point-in-time references to subvolumes.

```bash
# Create a writable snapshot
sudo btrfs subvolume snapshot /mnt/btrfs/@home /mnt/btrfs/@home_rw_snap

# Create a read-only snapshot (Required for replication and backups)
sudo btrfs subvolume snapshot -r /mnt/btrfs/@ /mnt/btrfs/@snapshots/root_$(date +%Y%m%d_%H%M)

# Atomic System Rollback Strategy (Boot from Live USB or rescue target)
# 1. Mount top-level Btrfs root (Subvolume ID 5)
sudo mount -o subvolid=5 /dev/sdb1 /mnt/root

# 2. Rename corrupted subvolume
sudo mv /mnt/root/@ /mnt/root/@_corrupted

# 3. Snapshot known good read-only snapshot to new writable subvolume @
sudo btrfs subvolume snapshot /mnt/root/@snapshots/root_good /mnt/root/@

# 4. Unmount and reboot into restored root
sudo umount /mnt/root
```

---

## 4. Send & Receive (Stream Backups & Replication)

Transfer snapshots locally or over network connections without file-by-file scanning.

```bash
# Send read-only snapshot to a raw stream archive file
sudo btrfs send /mnt/btrfs/@snapshots/root_snap | gzip > /backups/root_snap.img.gz

# Restore read-only snapshot from file archive
zcat /backups/root_snap.img.gz | sudo btrfs receive /mnt/backups/

# Direct local stream replication between Btrfs drives
sudo btrfs send /mnt/btrfs/@snapshots/root_snap | sudo btrfs receive /mnt/backup_drive/

# Stream over SSH with progress bar (pv) and ZSTD network compression
sudo btrfs send /mnt/btrfs/@snapshots/root_snap | zstd -1 | ssh user@remote "zstd -d | sudo btrfs receive /backups/"

# Incremental Send (Transfers ONLY blocks changed between snap_v1 and snap_v2)
sudo btrfs send -p /mnt/btrfs/@snapshots/snap_v1 /mnt/btrfs/@snapshots/snap_v2 | sudo btrfs receive /mnt/backup_drive/

# Cloned Incremental Send (Specifies parent -p and clone source -c)
sudo btrfs send -p /mnt/btrfs/@snapshots/snap_v1 -c /mnt/btrfs/@snapshots/snap_ref /mnt/btrfs/@snapshots/snap_v2 | sudo btrfs receive /mnt/backup_drive/
```

---

## 5. File Properties & NoCoW Attributes

### Btrfs Native Properties

```bash
# View properties on a file, directory, or subvolume
btrfs property get /mnt/btrfs/@data

# Set compression level directly on a directory
btrfs property set /mnt/btrfs/data_dir compression zstd

# Disable compression on an inode
btrfs property set /mnt/btrfs/data_dir compression ""

# Toggle read-only flag on a subvolume
btrfs property set /mnt/btrfs/@snapshot ro true
```

### Disabling Copy-on-Write (`nodatacow`)

CoW causes heavy fragmentation on active databases, virtual machine disks (QEMU/KVM, VirtualBox), and large log files.

```bash
# Apply NoCoW flag (+C) to a newly created EMPTY directory before adding files
mkdir /var/lib/libvirt/images
sudo chattr +C /var/lib/libvirt/images

# Verify +C attribute flag
lsattr -d /var/lib/libvirt/images
# Output includes 'C': ---------------C------ /var/lib/libvirt/images
```

*Note: Setting `chattr +C` on an existing file with data will not disable CoW retroactively. You must set it on an empty file or directory first.*

---

## 6. Swapfile Management

Creating swapfiles on Btrfs requires specific allocation flags to avoid CoW corruption.

### Automated Method (`btrfs-progs` >= 6.1)

```bash
# Automatically creates a non-fragmented, NoCoW swap file
sudo btrfs filesystem mkswapfile --size 4G /swap/swapfile
sudo swapon /swap/swapfile
```

### Manual Method (Legacy / Broad Compatibility)

```bash
# 1. Create a 0-byte file
sudo truncate -s 0 /swap/swapfile

# 2. Disable Copy-on-Write on the empty file
sudo chattr +C /swap/swapfile

# 3. Disable compression on file
sudo btrfs property set /swap/swapfile compression none

# 4. Allocate contiguous blocks (do NOT use sparse files)
sudo fallocate -l 4G /swap/swapfile

# 5. Restrict permissions, format, and activate
sudo chmod 0600 /swap/swapfile
sudo mkswap /swap/swapfile
sudo swapon /swap/swapfile
```

---

## 7. Storage Space, Usage & Quotas

Standard utilities like `df -h` can produce misleading results on Btrfs due to chunk allocation mechanics. Use native `btrfs` tools for accurate capacity planning.

```bash
# Detailed overall breakdown of allocated vs unallocated space
sudo btrfs filesystem usage /mnt/btrfs

# Device-level physical allocation overview
sudo btrfs device usage /mnt/btrfs

# Calculate actual disk space consumed by files considering shared CoW extents
sudo btrfs filesystem du -s /mnt/btrfs/@data/*
```

### Subvolume Quotas (qgroups)

```bash
# Enable quota engine
sudo btrfs quota enable /mnt/btrfs

# View quota group usage (Referenced vs Exclusive space)
sudo btrfs qgroup show -p -r /mnt/btrfs

# Assign limit (e.g., limit subvolume ID 256 to maximum 50GB)
sudo btrfs qgroup limit 50G 0/256 /mnt/btrfs

# Disable quota engine (Reduces performance overhead on high-write systems)
sudo btrfs quota disable /mnt/btrfs
```

---

## 8. Multi-Device Management, Dynamic RAID & Resizing

Btrfs handles multi-device pools natively without requiring hardware RAID or LVM layers.

### RAID Profiles Summary

| Profile | Min Devices | Data Redundancy | Space Efficiency | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Single** | 1 | None | 100% | Striped across devices if multiple. |
| **DUP** | 1 | 2 Copies | 50% | Duplicates data on same physical drive. |
| **RAID0** | 2 | None | 100% | Pure striping for maximum performance. |
| **RAID1** | 2 | 2 Copies | 50% | Mirroring across 2 separate devices. |
| **RAID1c3** | 3 | 3 Copies | 33.3% | Mirroring across 3 separate devices. |
| **RAID1c4** | 4 | 4 Copies | 25% | Mirroring across 4 separate devices. |
| **RAID10** | 4 | 1 Parity Set | 50% | Striping across mirrored pairs. |
| **RAID5/6** | 3 (R5) / 4 (R6) | Parity | 66–75% | **Unstable**: Parity write-hole bug present. Avoid for critical data. |

### Adding, Removing & Live Drive Replacement

```bash
# Online expansion: Add a new physical drive to mounted filesystem
sudo btrfs device add /dev/sdd /mnt/btrfs

# Online reduction: Shrink and safely evacuate data off a drive before removal
sudo btrfs device remove /dev/sdb /mnt/btrfs

# Online Drive Replacement (Faster than add + remove; streams directly)
sudo btrfs replace start /dev/sdb /dev/sde /mnt/btrfs

# Monitor live status of ongoing replace operation
sudo btrfs replace status /mnt/btrfs
```

### Live Resizing

```bash
# Expand mounted filesystem on devid 1 to occupy maximum available partition size
sudo btrfs filesystem resize 1:max /mnt/btrfs

# Shrink mounted filesystem by 20 Gigabytes
sudo btrfs filesystem resize -20G /mnt/btrfs
```

### Balancing Operations

Re-balances allocated chunks to reclaim unused block groups or convert online RAID profiles.

```bash
# Reclaim unused allocated block chunks (Quick filter balance)
sudo btrfs balance start -dusage=10 -musage=10 /mnt/btrfs

# Convert filesystem online to RAID1 data and RAID1 metadata
sudo btrfs balance start -dconvert=raid1 -mconvert=raid1 /mnt/btrfs

# Monitor running balance job
sudo btrfs balance status /mnt/btrfs

# Pause or cancel an active balance operation
sudo btrfs balance pause /mnt/btrfs
sudo btrfs balance cancel /mnt/btrfs
```

---

## 9. Maintenance, Integrity & Defragmentation

### Scrubbing (Checksum Integrity Check)

Background process reading all block extents, verifying against stored cryptographic checksums (CRC32c / XXHASH / SHA256), and repairing damaged sectors using redundant RAID/DUP mirrors.

```bash
# Start background scrub task
sudo btrfs scrub start /mnt/btrfs

# Check status, repair statistics, and error count
sudo btrfs scrub status /mnt/btrfs

# Run scrub in foreground blocking mode (ideal for scripts/cron)
sudo btrfs scrub start -B /mnt/btrfs
```

### Defragmentation

```bash
# Recursively defragment a directory or subvolume
sudo btrfs filesystem defragment -r /mnt/btrfs/@data

# Defragment and re-compress extents with ZSTD
sudo btrfs filesystem defragment -r -czstd /mnt/btrfs/@data
```

*Warning: Defragmenting files involved in active snapshot chains will clone shared extents, increasing overall disk space usage.*

### Device Hardware Statistics

```bash
# Display physical disk I/O, checksum, and uncorrectable read/write errors
sudo btrfs device stats /mnt/btrfs

# Reset hardware error counters to 0
sudo btrfs device stats -z /mnt/btrfs
```

---

## 10. Emergency Recovery, Repair & Forensics

### Emergency Read-Only Recovery Mounts

When a Btrfs filesystem fails standard mounting due to tree corruption, force read-only recovery mode:

```bash
# Attempt mount using backup superblock trees
sudo mount -o ro,rescue=usebackuproot /dev/sdb1 /mnt/recovery

# Attempt mount bypassing corrupted log trees
sudo mount -o ro,rescue=nologreplay /dev/sdb1 /mnt/recovery

# Ignore free space cache errors during emergency boot
sudo mount -o ro,rescue=clear_cache /dev/sdb1 /mnt/recovery
```

### Offline File Extraction (`btrfs restore`)

Extract files from an unmountable corrupted filesystem without writing to the damaged device.

```bash
# Extract files matching standard paths to an external backup target
sudo btrfs restore -v /dev/sdb1 /mnt/external_backup/
```

### Structural Repair Utilities

```bash
# Clear corrupted transaction log tree (Fixes panic on boot following sudden power loss)
sudo btrfs rescue zero-log /dev/sdb1

# Recover primary superblock using backup mirrors
sudo btrfs rescue super-recover /dev/sdb1

# Non-destructive filesystem consistency check (Safe dry-run inspection)
sudo btrfs check --readonly /dev/sdb1

# Inspect internal superblock metadata
sudo btrfs inspect-internal dump-super /dev/sdb1
```

*CRITICAL WARNING: Never run `btrfs check --repair` unless explicitly instructed as an absolute last resort by developers or after creating a complete block-level disk image (`dd`). Running `--repair` on a partially damaged filesystem can cause irreversible data loss.*

---

## 11. Production `/etc/fstab` Example & System Architecture

### Standard Recommended Layout (`/etc/fstab`)

```fstab
# <file system>                           <mount point>  <type>  <options>                                             <dump> <pass>
UUID=a1b2c3d4-e5f6-7890-abcd-1234567890ab /              btrfs   subvol=@,compress=zstd:3,noatime,discard=async        0      0
UUID=a1b2c3d4-e5f6-7890-abcd-1234567890ab /home          btrfs   subvol=@home,compress=zstd:3,noatime,discard=async    0      0
UUID=a1b2c3d4-e5f6-7890-abcd-1234567890ab /.snapshots    btrfs   subvol=@snapshots,compress=zstd:3,noatime             0      0
```

### Best Practices Checklist

1. **Avoid LVM/MDADM Layers**: Place Btrfs directly on raw block partitions (`/dev/nvme0n1p2` or `/dev/sda1`) to allow native checksum verification and device repair functions to operate directly on disk hardware.
2. **Automate Scrubbing**: Schedule monthly scrub jobs using systemd timers (`btrfs-scrub.timer`) or cron to identify bit rot early on cold data storage.
3. **Set Up Automated Snapper / Btrbk**: Use snapshot management automation (like `snapper` or `btrbk`) for automated boot snapshots and incremental off-site replication.
