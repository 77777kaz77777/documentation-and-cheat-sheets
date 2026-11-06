# Commands to create filesystem snapshots and roll back changes using Snapper

## Configuration Setup & Management

Before taking snapshots, a configuration must exist for the target Btrfs subvolume.

**Create a new configuration for a subvolume (e.g., `sudo snapper -c home create-config /home`):**

```bash
sudo snapper -c <config> create-config <path>
```

**List all active Snapper configurations and their target subvolumes:**

```bash
sudo snapper list-configs
```

**View the retention policies, timers, and quota settings for a specific configuration:**

```bash
sudo snapper -c <config> get-config
```

**Modify a parameter (e.g., `TIMELINE_LIMIT_HOURLY=5`):**

```bash
sudo snapper -c <config> set-config <KEY>=<VALUE>
```

## Snapshot Operations

**List all snapshots for the default configuration (`root`):**

```bash
sudo snapper ls
```

**List snapshots for a specific configuration (e.g., `home`):**

```bash
sudo snapper -c <config> ls
```

**Create a standard, single manual snapshot with a description:**

```bash
sudo snapper -c <config> create -d "<description>"
```

**Create a snapshot manually but tag it for the automatic timeline cleanup algorithm:**

```bash
sudo snapper -c <config> create -c timeline
```

**Delete a specific snapshot by its ID number:**

```bash
sudo snapper -c <config> delete <number>
```

**Delete a sequential range of snapshots:**

```bash
sudo snapper -c <config> delete <start_num>-<end_num>
```

## Pre/Post Snapshots (System Changes)

Used to bracket system changes (like manual software installations or script executions) to track exactly what was modified.

```bash
# 1. Create the 'pre' snapshot and print its number
sudo snapper -c <config> create -t pre -p -d "Before system update"
# (Output will give you a number, e.g., 42)

# 2. Perform your system changes, then create the linked 'post' snapshot
sudo snapper -c <config> create -t post --pre-number 42 -d "After system update"
```

## Comparison & Diagnostics

**Show a high-level summary of files added (`+`), deleted (`-`), or modified (`c`):**

```bash
sudo snapper -c <config> status <num1>..<num2>
```

**Show the exact line-by-line file differences (similar to `git diff`) between two snapshots:**

```bash
sudo snapper -c <config> diff <num1>..<num2>
```

**Diff only a specific file or directory between two snapshots:**

```bash
sudo snapper -c <config> diff <num1>..<num2> <path>
```

## Rollback & Recovery

> **Note on Fedora Rollbacks:** The native `snapper rollback` command requires a specific Btrfs subvolume layout (SUSE-style). If using standard Fedora layouts, file-level recovery via `undochange` or mounting the snapshot manually is often preferred.

**Create a read-write snapshot of the specified read-only snapshot and set it as the default subvolume to boot into:**

```bash
sudo snapper rollback <number>
```

**Revert a specific file or directory to its state in `<num1>`, undoing changes made up to `<num2>`:**

```bash
sudo snapper -c <config> undochange <num1>..<num2> <path>
```

**Quickly revert a specific file to its exact state in the specified snapshot `<number>`:**

```bash
sudo snapper -c <config> undochange <number> <path>
```

## Manual File Restoration via Mount

If you need to manually copy files out of a snapshot without using `undochange`:

```bash
# Snapshots are natively accessible in the hidden .snapshots directory at the root of the subvolume:
sudo ls -l /.snapshots/<number>/snapshot/
sudo ls -l /home/.snapshots/<number>/snapshot/

# You can manually copy a file back to its live location:
sudo cp /.snapshots/<number>/snapshot/etc/fstab /etc/fstab
```

---

**Sources & Verification:**

- _Snapper Official Documentation:_ <http://snapper.io/documentation.html>
- _Snapper Man Pages:_ `man snapper`
- _Arch Wiki - Snapper (Highly applicable to Fedora Btrfs configs):_ <https://wiki.archlinux.org/title/Snapper>
