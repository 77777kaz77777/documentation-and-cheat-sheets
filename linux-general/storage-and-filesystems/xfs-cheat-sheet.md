# XFS Cheat Sheet

Quick-reference guide for creating, growing, checking, and maintaining XFS filesystems.

**XFS** is a high-performance 64-bit journaling filesystem. It is the default filesystem on RHEL, Rocky Linux, AlmaLinux, and CentOS Stream, and it handles large files, large volumes, and parallel I/O very well. Modern XFS also supports metadata checksums, reflink (copy-on-write file clones), and timestamps past 2038.

> **Key limitation:** An XFS filesystem can be **grown but not shrunk**. If you may need to reclaim space later, put XFS on LVM and leave free space in the volume group instead of allocating everything up front.

---

## 1. Installation & Utility Setup

### Install Userspace Tools

```bash
# RHEL / Fedora
sudo dnf install xfsprogs

# Debian / Ubuntu
sudo apt install xfsprogs

# Arch Linux
sudo pacman -S xfsprogs

# Alpine Linux
sudo apk add xfsprogs
```

On Fedora and RHEL, the online checker ships separately:

```bash
sudo dnf install xfsprogs-xfs_scrub
```

### Tool Overview

| Tool | Purpose |
| --- | --- |
| `mkfs.xfs` | Create a filesystem |
| `xfs_info` | Show filesystem geometry and enabled features |
| `xfs_admin` | Change label, UUID, and some features (unmounted) |
| `xfs_growfs` | Grow a mounted filesystem |
| `xfs_repair` | Offline check and repair |
| `xfs_scrub` | Online metadata check (and repair on newer kernels) |
| `xfs_quota` | User, group, and project quotas |
| `xfs_fsr` | Online defragmentation |
| `xfsdump` / `xfsrestore` | Filesystem-aware backup and restore |
| `xfs_db` | Low-level debugger (read-only use recommended) |
| `xfs_io` | Low-level file I/O and inspection |

---

## 2. Creating an XFS Filesystem

### Basic Format

```bash
# Format a partition with a label
sudo mkfs.xfs -L data /dev/sdb1

# Overwrite an existing filesystem signature (destructive)
sudo mkfs.xfs -f -L data /dev/sdb1
```

### Common `mkfs.xfs` Options

| Option | Meaning |
| --- | --- |
| `-L label` | Filesystem label (max 12 characters) |
| `-f` | Force: overwrite an existing filesystem |
| `-b size=4096` | Block size (4 KiB is the default and the right choice almost always) |
| `-m reflink=1` | Enable reflink / CoW clones (default on current xfsprogs) |
| `-m crc=1` | Metadata checksums (default; required for reflink, bigtime, rmapbt) |
| `-m bigtime=1` | Timestamps beyond 2038 (default on newer xfsprogs) |
| `-d su=64k,sw=4` | Stripe unit and width, for hardware RAID that doesn't report geometry |
| `-l logdev=/dev/sdc1` | External journal device |
| `-K` | Skip discard (TRIM) at format time, faster on large SSDs |

Recent `xfsprogs` releases already enable checksums, free-inode btrees, reflink, bigtime, inode btree counters, and reverse mapping btrees by default, so a plain `mkfs.xfs` is usually all you need.

### Format for Compatibility with an Older Kernel

`mkfs.xfs` can read a config file that matches the defaults of an older LTS kernel, so the filesystem stays mountable there:

```bash
ls /usr/share/xfsprogs/mkfs/
sudo mkfs.xfs -c options=/usr/share/xfsprogs/mkfs/lts_5.15.conf /dev/sdb1
```

### Format Software RAID

`mkfs.xfs` detects stripe geometry from `mdadm` and LVM automatically. Check it after formatting:

```bash
sudo mkfs.xfs -L raid /dev/md0
xfs_info /dev/md0 | grep -E 'sunit|swidth'
```

---

## 3. Mounting & `/etc/fstab`

### Mount Manually

```bash
sudo mkdir -p /mnt/data
sudo mount /dev/sdb1 /mnt/data
sudo mount -o noatime /dev/sdb1 /mnt/data
```

### Persistent Mount

Find the UUID first:

```bash
sudo blkid /dev/sdb1
```

Then add a line to `/etc/fstab`:

```text
UUID=xxxx-xxxx-xxxx  /mnt/data  xfs  defaults,noatime  0 0
```

The last field (`fsck` pass) should be `0` for XFS; `fsck.xfs` does nothing, and checking is done with `xfs_repair` instead.

Test without rebooting:

```bash
sudo systemctl daemon-reload && sudo mount -a && findmnt /mnt/data
```

### Useful Mount Options

| Option | Effect |
| --- | --- |
| `noatime` | Don't update access times (less write overhead) |
| `discard` | Continuous TRIM; usually prefer `fstrim.timer` instead |
| `uquota` / `gquota` / `pquota` | Enable user / group / project quotas |
| `logbsize=256k` | Larger in-memory log buffers for metadata-heavy workloads |
| `nouuid` | Mount a cloned filesystem whose UUID duplicates a mounted one |
| `norecovery` | Mount without replaying the log (must be read-only, `ro`) |

### Periodic TRIM

```bash
sudo systemctl enable --now fstrim.timer
sudo fstrim -v /mnt/data
```

---

## 4. Inspecting a Filesystem

```bash
# Geometry and enabled features (mounted or unmounted)
xfs_info /mnt/data

# Space usage
df -hT /mnt/data

# Inode usage
df -i /mnt/data

# Label and UUID
sudo xfs_admin -l -u /dev/sdb1

# Free-space fragmentation summary
sudo xfs_db -r -c "freesp -s" /dev/sdb1

# File fragmentation factor (read-only)
sudo xfs_db -r -c frag /dev/sdb1

# Extent map of a single file
xfs_bmap -v /mnt/data/bigfile.img
```

`xfs_db -r` opens the device read-only. Results on a mounted filesystem can be slightly out of date, but the command is safe.

---

## 5. Labels, UUIDs & Feature Changes

`xfs_admin` changes must be made on an **unmounted** filesystem.

```bash
sudo umount /mnt/data

# Set a new label
sudo xfs_admin -L backups /dev/sdb1

# Generate a new random UUID (needed after cloning a disk)
sudo xfs_admin -U generate /dev/sdb1

# Upgrade an older filesystem to bigtime and inode btree counters
sudo xfs_admin -O bigtime=1,inobtcount=1 /dev/sdb1
```

If you only need to mount a cloned disk alongside the original once, use `mount -o nouuid` instead of changing the UUID.

---

## 6. Growing XFS

XFS grows **online** — the filesystem must be **mounted**. `xfs_growfs` takes the mount point, not the device.

### Grow After Enlarging a Partition

```bash
# 1. Grow the partition (here: partition 1 on /dev/sdb)
sudo growpart /dev/sdb 1

# 2. Grow the filesystem to fill it
sudo xfs_growfs /mnt/data
```

`growpart` comes from `cloud-utils-growpart` (Fedora/RHEL) or `cloud-guest-utils` (Debian/Ubuntu). `parted /dev/sdb resizepart 1 100%` works too.

### Grow on LVM

```bash
# Extend the LV and the filesystem in one step
sudo lvextend -r -L +50G /dev/vg_data/lv_data

# Or use all remaining free space in the VG
sudo lvextend -r -l +100%FREE /dev/vg_data/lv_data
```

`-r` (`--resizefs`) calls `xfs_growfs` for you. Without it, run `sudo xfs_growfs /mnt/data` afterward.

### Grow to a Specific Size

```bash
# Size is in filesystem blocks (check bsize in xfs_info)
sudo xfs_growfs -D 26214400 /mnt/data
```

### Why XFS Cannot Shrink

There is no supported way to shrink XFS. Upstream work exists for removing empty space at the end of a filesystem, but it is experimental and not something to rely on. To make XFS smaller:

1. Back up the data (`xfsdump`, `rsync -aHAX`, or another tool).
2. Shrink or recreate the underlying partition or LV.
3. Run `mkfs.xfs` on the smaller device.
4. Restore the data.

Tip: avoid growing a very small filesystem into a very large one. Each grow adds allocation groups, and too many small AGs can hurt performance. Create the filesystem near its expected final size when you can.

---

## 7. Checking & Repairing

### Offline Check and Repair with `xfs_repair`

`xfs_repair` must run on an **unmounted** filesystem. For the root filesystem, boot from live media or a rescue target.

```bash
sudo umount /mnt/data

# Dry run: report problems without changing anything
sudo xfs_repair -n /dev/sdb1

# Repair
sudo xfs_repair /dev/sdb1

# Verbose output
sudo xfs_repair -v /dev/sdb1
```

### "Dirty Log" Errors

If `xfs_repair` refuses to run because the log has unwritten changes:

1. **Mount and unmount once first.** Mounting replays the journal cleanly:

   ```bash
   sudo mount /dev/sdb1 /mnt/data && sudo umount /mnt/data
   ```

2. Run `xfs_repair` again.
3. **Only if mounting fails**, zero the log as a last resort. This discards recent metadata changes and can leave files in `lost+found`:

   ```bash
   sudo xfs_repair -L /dev/sdb1
   ```

### Online Check with `xfs_scrub`

`xfs_scrub` checks metadata while the filesystem stays mounted. Upstream still marks it **experimental**, and it needs a kernel built with online scrub support.

```bash
# Check only, no changes
sudo xfs_scrub -n /mnt/data

# Check and repair what the kernel can fix online (newer kernels)
sudo xfs_scrub /mnt/data

# Run the bundled systemd units for all XFS mounts
sudo systemctl enable --now xfs_scrub_all.timer
```

### Health Status

On recent kernels, after a scrub has run, you can read the stored health report:

```bash
sudo xfs_spaceman -c "health -c" /mnt/data
```

### Kernel Messages

```bash
sudo dmesg | grep -i xfs
sudo journalctl -k | grep -i xfs
```

Messages such as `Corruption detected` or `metadata I/O error` mean you should unmount and run `xfs_repair -n`, and also check the disk itself with `smartctl`.

---

## 8. Quotas

Quotas are enabled with **mount options**, not a separate command. On XFS, quota accounting is part of the filesystem's journaled metadata, so no `quotacheck` is needed.

### Enable Quotas

```text
UUID=xxxx-xxxx-xxxx  /srv  xfs  defaults,uquota,pquota  0 0
```

```bash
sudo umount /srv && sudo mount /srv
sudo xfs_quota -x -c state /srv
```

For the root filesystem, quota options must be passed on the kernel command line (`rootflags=uquota,pquota`), because `/` is mounted before `/etc/fstab` is read.

### User Quotas

```bash
# Soft 9 GiB / hard 10 GiB block limit for user alice
sudo xfs_quota -x -c "limit bsoft=9g bhard=10g alice" /srv

# Report usage for all users, human-readable
sudo xfs_quota -x -c "report -h" /srv

# Show one user's usage
sudo xfs_quota -c "quota -h alice" /srv
```

### Project (Directory) Quotas

Project quotas limit a directory tree regardless of who owns the files:

```bash
# 1. Map a project ID to a directory, and a name to the ID
echo "42:/srv/www" | sudo tee -a /etc/projects
echo "www:42" | sudo tee -a /etc/projid

# 2. Initialise the project
sudo xfs_quota -x -c "project -s www" /srv

# 3. Set a 50 GiB hard limit
sudo xfs_quota -x -c "limit -p bhard=50g www" /srv

# 4. Check usage
sudo xfs_quota -x -c "report -p -h" /srv
```

---

## 9. Reflink Copies & Deduplication

On a filesystem with `reflink=1` (check `xfs_info`), copies can share data blocks until one side is modified.

```bash
# Instant copy that shares blocks (fails if reflink is unsupported)
cp --reflink=always disk.img disk-clone.img

# Use reflink when possible, fall back to a normal copy otherwise
cp --reflink=auto disk.img disk-copy.img
```

For deduplication of existing files, use `duperemove` (from your distro repos):

```bash
sudo duperemove -dhr /srv/images
```

Note: `df` reports space shared by reflinked files only once, but `du` counts each file in full.

---

## 10. Defragmentation

XFS fragments very little in normal use. Check before defragmenting:

```bash
sudo xfs_db -r -c frag /dev/sdb1
```

```bash
# Defragment one file
sudo xfs_fsr -v /mnt/data/vm.img

# Defragment a whole mounted filesystem (runs for up to 2 hours by default)
sudo xfs_fsr -v /mnt/data
```

A high "fragmentation factor" is often misleading on large files. Look at actual extent counts with `xfs_bmap -v` before deciding it's a problem.

---

## 11. Backup & Restore with `xfsdump`

`xfsdump` backs up an XFS filesystem with all its attributes and supports incremental levels. Install `xfsdump` first (separate package).

```bash
# Full (level 0) dump of /srv to a file
sudo xfsdump -l 0 -L srv-full -M backup -f /backup/srv.l0.dump /srv

# Incremental (level 1) dump of changes since level 0
sudo xfsdump -l 1 -L srv-inc -M backup -f /backup/srv.l1.dump /srv

# List what a dump contains
sudo xfsrestore -t -f /backup/srv.l0.dump | less

# Restore a full dump into a directory
sudo xfsrestore -f /backup/srv.l0.dump /mnt/restore

# Interactive restore (browse and pick files)
sudo xfsrestore -i -f /backup/srv.l0.dump /mnt/restore
```

`xfsdump` only works on XFS. For backups you may restore to a different filesystem, use `rsync -aHAX` or a backup tool such as Borg or restic.

### Freeze for a Consistent Block-Level Snapshot

XFS has no built-in snapshots. When taking an LVM or SAN snapshot, freeze the filesystem briefly so it is consistent:

```bash
sudo xfs_freeze -f /srv
sudo lvcreate -s -L 10G -n srv_snap /dev/vg_data/lv_srv
sudo xfs_freeze -u /srv
```

Modern LVM freezes automatically during `lvcreate -s`, but the manual form works with any snapshot tool. Mount the snapshot with `-o nouuid,ro`, because it has the same UUID as the original.

---

## 12. Troubleshooting

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `No space left on device` but `df -h` shows free space | Out of inodes, or free space too fragmented for new inode chunks | `df -i`; check `xfs_db -r -c "freesp -s"`; free space or grow the filesystem |
| `mount: wrong fs type ... duplicate UUID` | Mounting a clone next to the original | `mount -o nouuid` or `xfs_admin -U generate` |
| `xfs_repair` says the log contains metadata changes | Unclean shutdown | Mount and unmount once, then repair; `-L` only as a last resort |
| Filesystem won't mount on an older kernel | Created with features the old kernel lacks (bigtime, rmapbt, nrext64) | Reformat with an `lts_*.conf` config file from `/usr/share/xfsprogs/mkfs/` |
| `xfs_growfs` reports no change | Partition or LV wasn't enlarged first | `lsblk` to confirm the device size, then `growpart` / `lvextend` |
| `Filesystem has duplicate UUID` after `dd` clone | Same as above | `xfs_admin -U generate /dev/sdX1` |
| Kernel logs `Corruption of in-memory data detected. Shutting down filesystem` | Metadata corruption or failing disk | Unmount, `xfs_repair -n`, check `smartctl -a`, then repair |

---

## 13. Quick Reference

```bash
sudo mkfs.xfs -L data /dev/sdb1                   # create
xfs_info /mnt/data                                # geometry and features
sudo xfs_admin -L newlabel /dev/sdb1              # relabel (unmounted)
sudo xfs_growfs /mnt/data                         # grow to fill device (mounted)
sudo lvextend -r -l +100%FREE /dev/vg/lv          # grow LV and filesystem
sudo xfs_repair -n /dev/sdb1                      # dry-run check (unmounted)
sudo xfs_repair /dev/sdb1                         # repair (unmounted)
sudo xfs_scrub -n /mnt/data                       # online check (experimental)
sudo xfs_quota -x -c "report -h" /mnt/data        # quota report
sudo xfs_fsr -v /mnt/data                         # defragment
cp --reflink=always a.img b.img                   # instant CoW copy
sudo xfsdump -l 0 -f /backup/data.dump /mnt/data  # full backup
```

---

## Sources & Verification

- **mkfs.xfs defaults and options:** [mkfs.xfs(8) manual page](https://man7.org/linux/man-pages/man8/mkfs.xfs.8.html)
- **Growing and the lack of shrink support:** [xfs_growfs(8) manual page](https://man7.org/linux/man-pages/man8/xfs_growfs.8.html)
- **Online scrub and repair status:** [Kernel documentation — XFS Online Fsck Design](https://docs.kernel.org/filesystems/xfs/xfs-online-fsck-design.html)
- **General XFS administration:** [ArchWiki — XFS](https://wiki.archlinux.org/title/XFS)

## Related guides

- [Btrfs Cheat Sheet](btrfs-cheat-sheet.md)
- [ZFS Administration Cheat Sheet](zfs-administration-cheat-sheet.md)
- [RAID Cheatsheet for Beginners](raid-cheat-sheet.md)
- [Storage Management Command Reference Guide](storage-management-reference.md)
- [smartctl Comprehensive Cheat Sheet](smartctl-cheat-sheet.md)
- [LVM Cheat Sheet](lvm-cheat-sheet.md)
