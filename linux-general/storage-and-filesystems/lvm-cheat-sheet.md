# LVM Cheat Sheet

Quick-reference guide for managing disks with the Logical Volume Manager (LVM).

**LVM** adds a flexible layer between disks and filesystems. **Physical volumes (PVs)** are disks or partitions; they are pooled into a **volume group (VG)**; and you carve **logical volumes (LVs)** out of the VG to hold filesystems. LVs can be grown, moved between disks, and snapshotted without repartitioning.

```text
/dev/sdb1  /dev/sdc1        ← physical volumes (PV)
     \        /
     vg_data                ← volume group (VG)
     /     \
lv_media  lv_backup         ← logical volumes (LV) → mkfs → mount
```

---

## 1. Install & Inspect

```bash
# RHEL / Fedora / Rocky
sudo dnf install lvm2

# Debian / Ubuntu
sudo apt install lvm2

# Arch Linux
sudo pacman -S lvm2
```

```bash
# Short summaries
sudo pvs
sudo vgs
sudo lvs

# Full details
sudo pvdisplay
sudo vgdisplay vg_data
sudo lvdisplay /dev/vg_data/lv_media

# Everything together with the disk layout
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS
```

LVs appear as `/dev/<vg>/<lv>` and `/dev/mapper/<vg>-<lv>`; both names point to the same device.

---

## 2. Create PV → VG → LV

```bash
# 1. Mark disks or partitions as physical volumes (erases their signatures)
sudo pvcreate /dev/sdb1 /dev/sdc1

# 2. Pool them into a volume group
sudo vgcreate vg_data /dev/sdb1 /dev/sdc1

# 3a. Create a logical volume of a fixed size
sudo lvcreate -n lv_media -L 500G vg_data

# 3b. ...or use a percentage of the free space
sudo lvcreate -n lv_backup -l 100%FREE vg_data

# 4. Put a filesystem on it and mount it
sudo mkfs.xfs -L media /dev/vg_data/lv_media
sudo mkdir -p /srv/media && sudo mount /dev/vg_data/lv_media /srv/media
```

`-L` takes a size (`500G`, `2T`); `-l` takes extents or a percentage (`50%VG`, `100%FREE`).

Leave some free space in the VG when you can: it's needed for snapshots and lets you grow whichever LV fills first.

### fstab Entry

```text
/dev/vg_data/lv_media  /srv/media  xfs  defaults,noatime  0 0
```

---

## 3. Grow

### Grow an LV and Its Filesystem Together

```bash
# Add 100 GB
sudo lvextend -r -L +100G /dev/vg_data/lv_media

# Use all remaining free space in the VG
sudo lvextend -r -l +100%FREE /dev/vg_data/lv_media
```

`-r` (`--resizefs`) grows the filesystem too (XFS, ext4, and others). Both work while mounted.

### Add a New Disk to a VG

```bash
sudo pvcreate /dev/sdd
sudo vgextend vg_data /dev/sdd
sudo vgs vg_data
```

### After Enlarging a Virtual Disk or Partition

```bash
sudo growpart /dev/sdb 1
sudo pvresize /dev/sdb1
sudo lvextend -r -l +100%FREE /dev/vg_data/lv_media
```

---

## 4. Shrink

> **XFS cannot be shrunk.** Only ext4 (and a few others) can, and ext4 must be **unmounted** first. Back up before shrinking anything.

```bash
sudo umount /srv/backup
sudo lvreduce -r -L 200G /dev/vg_data/lv_backup
sudo mount /srv/backup
```

`lvreduce -r` runs the filesystem check and shrink in the right order. Without `-r`, shrinking the LV before the filesystem destroys data.

---

## 5. Remove a Disk from a VG

```bash
# 1. Move all data off the disk (online; can take hours)
sudo pvmove /dev/sdb1

# 2. Remove it from the VG
sudo vgreduce vg_data /dev/sdb1

# 3. Clear the LVM label
sudo pvremove /dev/sdb1
```

The other PVs in the VG need enough free space to receive the moved data. `pvmove` can resume after a reboot with plain `sudo pvmove`.

---

## 6. Snapshots

A snapshot records the state of an LV at a moment in time; it only stores blocks that change afterwards.

```bash
# Create a 20 GB snapshot (space for changes, not a full copy)
sudo lvcreate -s -n lv_media_snap -L 20G /dev/vg_data/lv_media

# Mount it read-only (XFS needs nouuid because the UUID matches the original)
sudo mkdir -p /mnt/snap && sudo mount -o ro,nouuid /dev/vg_data/lv_media_snap /mnt/snap

# Watch how full the snapshot is (Data%)
sudo lvs vg_data

# Roll the original back to the snapshot (applied at next activation if in use)
sudo umount /srv/media && sudo lvconvert --merge /dev/vg_data/lv_media_snap

# Or just delete the snapshot
sudo umount /mnt/snap && sudo lvremove /dev/vg_data/lv_media_snap
```

A classic snapshot that fills to 100% becomes **invalid** and is lost. Size it for the changes you expect, or use thin snapshots.

---

## 7. Thin Provisioning

Thin pools allocate space only when data is written and make cheap snapshots.

```bash
# Create a 500 GB thin pool
sudo lvcreate --type thin-pool -n pool0 -L 500G vg_data

# Create thin volumes larger in total than the pool
sudo lvcreate --type thin -n vm1 -V 200G --thinpool pool0 vg_data
sudo lvcreate --type thin -n vm2 -V 200G --thinpool pool0 vg_data

# Thin snapshot (no size needed)
sudo lvcreate -s -n vm1_snap vg_data/vm1

# Thin snapshots are skipped at boot; activate one to use it
sudo lvchange -ay -K vg_data/vm1_snap

# Monitor pool usage: Data% and Meta%
sudo lvs -a vg_data
```

**Never let a thin pool fill up.** Writes then fail across every volume in the pool. Watch `Data%` and `Meta%`, or set auto-extend in `/etc/lvm/lvm.conf`:

```text
thin_pool_autoextend_threshold = 80
thin_pool_autoextend_percent = 20
```

---

## 8. Rename, Activate & Remove

```bash
# Rename
sudo lvrename vg_data lv_media lv_movies
sudo vgrename vg_data vg_storage

# Activate / deactivate
sudo lvchange -an /dev/vg_data/lv_media
sudo vgchange -ay vg_data

# Remove an LV (unmount first; data is gone)
sudo lvremove /dev/vg_data/lv_media

# Remove a whole VG
sudo vgremove vg_data
```

Update `/etc/fstab` (and the kernel command line, for the root VG) after renaming.

---

## 9. Mirroring & RAID with LVM

```bash
# Two-way mirror (RAID 1) across two PVs
sudo lvcreate --type raid1 -m 1 -n lv_safe -L 100G vg_data

# Check sync progress and health
sudo lvs -a -o name,copy_percent,health_status,devices vg_data

# Replace a failed device
sudo lvconvert --repair vg_data/lv_safe
```

---

## 10. Troubleshooting

```bash
# Rescan for PVs, VGs, and LVs (after attaching disks)
sudo pvscan && sudo vgscan && sudo lvscan

# Activate everything found
sudo vgchange -ay

# Import a VG moved from another machine
sudo vgimportdevices -a

# Restore VG metadata from automatic backups
sudo vgcfgrestore --list vg_data
```

| Problem | Likely cause |
| --- | --- |
| `Insufficient free space` | VG full: `vgs` shows `VFree`; add a PV or shrink another LV |
| LV missing after boot | VG not activated; `vgchange -ay`, check `/etc/lvm/devices/system.devices` |
| VG not found on a moved disk (Fedora/RHEL 9+) | Device not in the LVM devices file; run `vgimportdevices -a` |
| `WARNING: Device mismatch detected` | Cloned disk with duplicate PV UUIDs: disconnect one, or `vgimportclone` |
| Snapshot shows `Invalid` | Classic snapshot ran out of space |

---

## 11. Quick Reference

```bash
sudo pvs; sudo vgs; sudo lvs                          # overview
sudo pvcreate /dev/sdX1                               # new PV
sudo vgcreate vg_data /dev/sdX1                       # new VG
sudo lvcreate -n lv_name -L 100G vg_data              # new LV
sudo lvextend -r -L +50G /dev/vg_data/lv_name         # grow LV + filesystem
sudo vgextend vg_data /dev/sdY1                       # add disk to VG
sudo pvmove /dev/sdX1 && sudo vgreduce vg_data /dev/sdX1  # remove disk
sudo lvcreate -s -n snap -L 10G /dev/vg_data/lv_name  # snapshot
sudo lvremove /dev/vg_data/snap                       # delete LV/snapshot
```

---

## Sources & Verification

- **LVM commands:** [lvm(8) and related man pages](https://man7.org/linux/man-pages/man8/lvm.8.html)
- **Thin provisioning:** [lvmthin(7)](https://man7.org/linux/man-pages/man7/lvmthin.7.html)

## Related guides

- [XFS Cheat Sheet](xfs-cheat-sheet.md)
- [RAID Cheatsheet for Beginners](raid-cheat-sheet.md)
- [Storage Management Command Reference Guide](storage-management-reference.md)
- [Btrfs Cheat Sheet](btrfs-cheat-sheet.md)
