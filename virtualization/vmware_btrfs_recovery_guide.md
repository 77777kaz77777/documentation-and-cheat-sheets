# VMware VM Recovery Guide (Btrfs Snapshots)

## The Problem
A VMware virtual machine fails to boot due to a corrupted snapshot disk (`.vmdk`), and the built-in repair tool (`vmware-vdiskmanager -R`) reports that the disk is corrupted and cannot be repaired. 

Since the files reside on a Btrfs filesystem, the virtual machine can be rolled back to a previous working state using automated snapshots (via Snapper or btrbk).

## Restoration Steps

### 1. Identify a Working Snapshot
First, locate a snapshot taken before the corruption occurred. You can list the Btrfs subvolumes to find your snapshots:

```bash
sudo btrfs subvolume list /mnt/storage
```
*Note the path to the desired snapshot, for example: `.snapshots/43/snapshot`*

### 2. Verify Snapshot Contents
Check the contents of the target snapshot to ensure your VM files (`.vmdk`, `.vmx`, etc.) are intact.

```bash
sudo ls -la /mnt/storage/.snapshots/43/snapshot/vms/WorkVM/
```

### 3. Restore the VM Directory
Copy the contents of the working snapshot over to your live VM directory. 

**Important:** Do not use the wildcard (`*`) when copying with `sudo`, as the shell will attempt to expand it using your normal user permissions before elevating, resulting in a "No such file or directory" error on restricted snapshot folders. Use a period (`.`) instead to tell `cp` to copy the directory contents directly.

```bash
sudo cp -a /mnt/storage/.snapshots/43/snapshot/vms/WorkVM/. /mnt/storage/vms/WorkVM/
```

### 4. Remove the Stale Lock File
If the snapshot was taken while the virtual machine was running or suspended, it will have captured a lock file (`.lck`). If left in the live directory, VMware will believe the machine is already in use and refuse to boot.

Remove the restored lock directory:

```bash
sudo rm -rf /mnt/storage/vms/WorkVM/WorkVM.vmx.lck
```

### 5. Boot the Virtual Machine
Open VMware and power on the virtual machine. It should boot normally from the exact state it was in when the chosen Btrfs snapshot was created.