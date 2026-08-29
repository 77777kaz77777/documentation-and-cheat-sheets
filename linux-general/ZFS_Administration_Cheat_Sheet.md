## A technical reference detailing essential commands for managing ZFS physical storage pools and logical datasets, including pool creation, dataset properties, snapshot replication, and disk replacement workflows
## 1. Zpool Management (Physical Disks)


**Check Pool Status and Health:**

```bash
zpool status \
  -v
```

```bash
zpool iostat \
  -v \
  2
```

**Create a New Pool:**

```bash
zpool create \
  mypool \
  mirror \
  /dev/sda \
  /dev/sdb
```

```bash
zpool create \
  mypool \
  raidz1 \
  /dev/sda \
  /dev/sdb \
  /dev/sdc
```

**Import and Export Pools:**

```bash
zpool export \
  mypool
```

```bash
zpool import
```

```bash
zpool import \
  mypool
```

## 2. Dataset Management (Logical Storage)

**Create and Destroy Datasets:**

```bash
zfs create \
  mypool/data
```

```bash
zfs destroy \
  mypool/data
```

**Manage Properties:**

```bash
zfs set \
  compression=lz4 \
  mypool/data
```

```bash
zfs set \
  quota=500G \
  mypool/data
```

```bash
zfs get \
  all \
  mypool/data
```

## 3. Snapshots and Replication

**Take and View Snapshots:**

```bash
zfs snapshot \
  mypool/data@backup1
```

```bash
zfs list \
  -t \
  snapshot
```

**Rollback and Clone:**

```bash
zfs rollback \
  mypool/data@backup1
```

```bash
zfs clone \
  mypool/data@backup1 \
  mypool/data-clone
```

**Send and Receive (Replication):**

```bash
zfs send \
  mypool/data@backup1 | \
zfs receive \
  backuppool/data-backup
```

## 4. Maintenance and Disk Replacement

**Scrubbing (Data Integrity Check):**

```bash
zpool scrub \
  mypool
```

```bash
zpool status \
  mypool
```

**Replacing a Failed Disk:**

```bash
zpool offline \
  mypool \
  /dev/sda
```

```bash
zpool replace \
  mypool \
  /dev/sda \
  /dev/sde
```

```bash
zpool online \
  mypool \
  /dev/sde
```

---
## Sources & Verification
* **ZFS Commands:** Verified against the official OpenZFS Documentation (https://openzfs.github.io/openzfs-docs/). Syntax, dataset properties, and pool management parameters have been validated for correct structure and safe execution.
