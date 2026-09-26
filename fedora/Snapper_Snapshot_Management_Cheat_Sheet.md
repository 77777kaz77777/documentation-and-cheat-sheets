# Commands to create filesystem snapshots and roll back changes using Snapper
## Configuration Setup & Management

Before taking snapshots, a configuration must exist for the target Btrfs subvolume.

| Command | Description |
| :--- | :--- |
| `sudo snapper -c <config> create-config <path>` | Create a new configuration for a subvolume (e.g., `sudo snapper -c home create-config /home`). |
| `sudo snapper list-configs` | List all active Snapper configurations and their target subvolumes. |
| `sudo snapper -c <config> get-config` | View the retention policies, timers, and quota settings for a specific configuration. |
| `sudo snapper -c <config> set-config <KEY>=<VALUE>` | Modify a parameter (e.g., `TIMELINE_LIMIT_HOURLY=5`). |

## Snapshot Operations

| Command | Description |
| :--- | :--- |
| `sudo snapper ls` | List all snapshots for the default configuration (`root`). |
| `sudo snapper -c <config> ls` | List snapshots for a specific configuration (e.g., `home`). |
| `sudo snapper -c <config> create -d "<description>"` | Create a standard, single manual snapshot with a description. |
| `sudo snapper -c <config> create -c timeline` | Create a snapshot manually but tag it for the automatic timeline cleanup algorithm. |
| `sudo snapper -c <config> delete <number>` | Delete a specific snapshot by its ID number. |
| `sudo snapper -c <config> delete <start_num>-<end_num>` | Delete a sequential range of snapshots. |

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

| Command | Description |
| :--- | :--- |
| `sudo snapper -c <config> status <num1>..<num2>` | Show a high-level summary of files added (`+`), deleted (`-`), or modified (`c`). |
| `sudo snapper -c <config> diff <num1>..<num2>` | Show the exact line-by-line file differences (similar to `git diff`) between two snapshots. |
| `sudo snapper -c <config> diff <num1>..<num2> <path>` | Diff only a specific file or directory between two snapshots. |

## Rollback & Recovery

> **Note on Fedora Rollbacks:** The native `snapper rollback` command requires a specific Btrfs subvolume layout (SUSE-style). If using standard Fedora layouts, file-level recovery via `undochange` or mounting the snapshot manually is often preferred.

| Command | Description |
| :--- | :--- |
| `sudo snapper rollback <number>` | Create a read-write snapshot of the specified read-only snapshot and set it as the default subvolume to boot into. |
| `sudo snapper -c <config> undochange <num1>..<num2> <path>` | Revert a specific file or directory to its state in `<num1>`, undoing changes made up to `<num2>`. |
| `sudo snapper -c <config> undochange <number> <path>` | Quickly revert a specific file to its exact state in the specified snapshot `<number>`. |

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
* *Snapper Official Documentation:* http://snapper.io/documentation.html
* *Snapper Man Pages:* `man snapper`
* *Arch Wiki - Snapper (Highly applicable to Fedora Btrfs configs):* https://wiki.archlinux.org/title/Snapper
