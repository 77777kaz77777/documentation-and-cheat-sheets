# RAID Cheatsheet for Beginners

RAID (Redundant Array of Independent Disks) is a way of combining multiple physical hard drives or SSDs into a single logical storage drive. To your operating system, three or four separate drives appear as one large volume.

The two main goals of RAID are **speed** (reading/writing across multiple drives at once) and **fault tolerance** (protecting your data if a drive dies).

---

## Core RAID Concepts Explained Simply

Before picking a RAID level, you need to understand the three fundamental building blocks:

1. **Striping:** Data is sliced into chunks and spread sequentially across multiple drives (e.g., Block 1 goes to Drive A, Block 2 to Drive B). This makes reading and writing extremely fast because all drives work simultaneously.
2. **Mirroring:** An exact duplicate of your data is written to two or more drives at the same time. If Drive A dies, Drive B has a 100% complete copy.
3. **Parity:** Mathematical calculations performed on striped data. Parity acts as a "checksum." If one drive in the array dies, the system uses the remaining data and parity values to dynamically reconstruct the missing files.

---

## The Common RAID Levels Explained

| RAID Level | Primary Purpose | How It Works | Usable Capacity | Drive Failure Tolerance | When to Use It |
| --- | --- | --- | --- | --- | --- |
| **RAID 0** | Maximum Speed | Pure Striping. Data splits evenly across all drives. | 100% of total drive space | **0 Drives** (1 dead drive destroys all data) | Temporary scratch disks, video editing caches |
| **RAID 1** | Simple Safety | Pure Mirroring. Every file is cloned across drives. | 50% (assuming 2 equal drives) | **1 Drive** (per pair) | Operating system drives, boot volumes |
| **RAID 5** | Speed + Safety | Striping + Single Parity distributed across all drives. | Total space minus 1 drive | **1 Drive** | Media servers, general NAS storage |
| **RAID 6** | Double Safety | Striping + Dual Parity distributed across all drives. | Total space minus 2 drives | **2 Drives** simultaneously | Large capacity HDD arrays where rebuilds take days |
| **RAID 10** | Speed + Heavy Safety | Nested RAID (1+0). Mirrors drives in pairs, then stripes across them. | 50% of total drive space | **1 Drive per mirror pair** (up to half total drives) | High-performance databases, virtual machine storage |

---

## Step-by-Step Linux Software RAID (`mdadm`) Guide

Linux manages software RAID using a tool called `mdadm`. Here is how to build, mount, and manage a RAID array from scratch.

### Step 1: Identify Your Drives

Before running creation commands, list all connected drives to make sure you target the correct disks:

```bash
lsblk -p
```

*Look for unformatted drives, such as `/dev/sdb` and `/dev/sdc`.*

---

### Step 2: Create a RAID 1 Array (Mirroring)

To create a mirrored array named `/dev/md0` using two drives (`/dev/sdb` and `/dev/sdc`):

```bash
sudo mdadm --create --verbose /dev/md0 --level=1 --raid-devices=2 /dev/sdb /dev/sdc
```

**What each flag means:**

* `sudo mdadm`: Runs the Linux RAID management utility with administrative privileges.
* `--create`: Instructs `mdadm` to initialize a brand-new array.
* `--verbose`: Outputs step-by-step diagnostic details to your screen.
* `/dev/md0`: The virtual drive name assigned to this new array.
* `--level=1`: Sets the RAID mode (1 for Mirroring).
* `--raid-devices=2`: Specifies the number of active physical drives in the array.
* `/dev/sdb /dev/sdc`: The exact paths of the physical target drives.

**Verification:** Check if the array was successfully created and initialized:

```bash
cat /proc/mdstat
```

*You should see `/dev/md0` listed as `active` along with a sync progress bar.*

---

### Step 3: Format and Mount the RAID Volume

Once the array is created, format it with a filesystem and attach it to a directory.

```bash
# Format the array with the XFS filesystem
sudo mkfs.xfs /dev/md0

# Create a mount point directory
sudo mkdir -p /mnt/raidstorage

# Mount the array to the directory
sudo mount /dev/md0 /mnt/raidstorage
```

**Verification:** Confirm that the storage is mounted and accessible:

```bash
df -h /mnt/raidstorage
```

---

### Step 4: Make the RAID Array Persistent Across Reboots

If you do not save your configuration, Linux will forget the array mapping when you restart.

1. **Save array configuration to `mdadm.conf`:**

   ```bash
   sudo mdadm --detail --scan | sudo tee -a /etc/mdadm.conf
   ```

2. **Update the initial ramdisk (initramfs) image:**

   ```bash
   # Use dracut for RHEL/Fedora/CentOS
   sudo dracut --force
   
   # Use update-initramfs for Ubuntu/Debian
   sudo update-initramfs -u
   ```

3. **Add the volume to `/etc/fstab` for auto-mounting on boot:**

   ```bash
   echo "/dev/md0  /mnt/raidstorage  xfs  defaults  0 0" | sudo tee -a /etc/fstab
   ```

---

### Step 5: How to Replace a Failed Drive

When a physical drive breaks, the array enters a **degraded** state. Here is the process to swap the drive without losing data.

1. **Locate the bad drive and mark it as failed:**

   ```bash
   sudo mdadm --manage /dev/md0 --fail /dev/sdb
   ```

2. **Remove the failed drive from the active array:**

   ```bash
   sudo mdadm --manage /dev/md0 --remove /dev/sdb
   ```

3. **Insert the new drive, then add it to the array:**

   ```bash
   sudo mdadm --manage /dev/md0 --add /dev/sdb
   ```

4. **Monitor the automatic rebuild progress:**

   ```bash
   watch -n 1 cat /proc/mdstat
   ```

   *Press `Ctrl + C` to exit the monitoring screen once recovery hits 100%.*
