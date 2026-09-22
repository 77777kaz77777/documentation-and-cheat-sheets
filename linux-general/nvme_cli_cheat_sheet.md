# nvme-cli Cheat Sheet

## Installation

| Distribution | Command |
| :--- | :--- |
| **Ubuntu / Debian** | `sudo apt install nvme-cli` |
| **Fedora / RHEL / CentOS** | `sudo dnf install nvme-cli` |
| **Arch Linux** | `sudo pacman -S nvme-cli` |
| **Alpine Linux** | `sudo apk add nvme-cli` |

## Device Discovery & Identification

| Action | Command |
| :--- | :--- |
| **List all NVMe devices** | `sudo nvme list` |
| **Show NVMe controller info** | `sudo nvme id-ctrl /dev/nvme0` |
| **Show NVMe namespace info** | `sudo nvme id-ns /dev/nvme0n1` |
| **List NVMe topologies** | `sudo nvme list-subsys` |
| **Show supported LBA formats** | `sudo nvme id-ns /dev/nvme0n1 | grep -i lbaf` |

## Health & SMART Monitoring

| Action | Command |
| :--- | :--- |
| **View SMART/Health log** | `sudo nvme smart-log /dev/nvme0` |
| **View error log entries** | `sudo nvme error-log /dev/nvme0` |
| **Run device self-test (Short)** | `sudo nvme device-self-test /dev/nvme0 -s 1` |
| **Run device self-test (Extended)**| `sudo nvme device-self-test /dev/nvme0 -s 2` |
| **Check self-test results** | `sudo nvme self-test-log /dev/nvme0` |

## Formatting & Secure Erase

> **Warning:** These commands will destroy data. Double-check device paths. Operations targeting namespaces use `/dev/nvme0n1`, while full drive operations often use the controller `/dev/nvme0`.

| Action | Command |
| :--- | :--- |
| **Format namespace (default)** | `sudo nvme format /dev/nvme0n1` |
| **Format with specific LBA size**| `sudo nvme format /dev/nvme0n1 --lbaf=1` |
| **Secure Erase (User Data)** | `sudo nvme format /dev/nvme0n1 --ses=1` |
| **Cryptographic Erase** | `sudo nvme format /dev/nvme0n1 --ses=2` |
| **Sanitize (Block Erase)** | `sudo nvme sanitize /dev/nvme0 --sanact=2` |
| **Sanitize (Crypto Erase)** | `sudo nvme sanitize /dev/nvme0 --sanact=4` |
| **Check Sanitize Status** | `sudo nvme sanitize-log /dev/nvme0` |

## Firmware Management

| Action | Command |
| :--- | :--- |
| **Check current firmware version**| `sudo nvme fw-log /dev/nvme0` |
| **Download firmware to device** | `sudo nvme fw-download /dev/nvme0 --fw=fw_update.bin` |
| **Commit firmware (Activate next boot)**| `sudo nvme fw-commit /dev/nvme0 --slot=1 --action=2` |
| **Commit & Activate immediately** | `sudo nvme fw-commit /dev/nvme0 --slot=1 --action=3` |

## Power Management

| Action | Command |
| :--- | :--- |
| **Show supported power states** | `sudo nvme get-feature /dev/nvme0 -f 2` |
| **Set active power state** | `sudo nvme set-feature /dev/nvme0 -f 2 -v <state_id>` |
| **Show Autonomous Power Transitions**| `sudo nvme get-feature /dev/nvme0 -f 11` |

## Namespace Management (Advanced)

| Action | Command |
| :--- | :--- |
| **Detach namespace** | `sudo nvme detach-ns /dev/nvme0 -n 1 -c 0` |
| **Delete namespace** | `sudo nvme delete-ns /dev/nvme0 -n 1` |
| **Create namespace (size in blocks)**| `sudo nvme create-ns /dev/nvme0 -s <size> -c <cap> -f <lba_format>`|
| **Attach namespace** | `sudo nvme attach-ns /dev/nvme0 -n 1 -c 0` |
| **Reset NVMe controller** | `sudo nvme reset /dev/nvme0` |