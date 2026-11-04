# nvme-cli Cheat Sheet

## Installation

**Ubuntu / Debian:**
```bash
sudo apt install nvme-cli
```

**Fedora / RHEL / CentOS:**
```bash
sudo dnf install nvme-cli
```

**Arch Linux:**
```bash
sudo pacman -S nvme-cli
```

**Alpine Linux:**
```bash
sudo apk add nvme-cli
```

## Device Discovery & Identification

**List all NVMe devices:**
```bash
sudo nvme list
```

**Show NVMe controller info:**
```bash
sudo nvme id-ctrl /dev/nvme0
```

**Show NVMe namespace info:**
```bash
sudo nvme id-ns /dev/nvme0n1
```

**List NVMe topologies:**
```bash
sudo nvme list-subsys
```

**Show supported LBA formats:**
```bash
sudo nvme id-ns /dev/nvme0n1
```

## Health & SMART Monitoring

**View SMART/Health log:**
```bash
sudo nvme smart-log /dev/nvme0
```

**View error log entries:**
```bash
sudo nvme error-log /dev/nvme0
```

**Run device self-test (Short):**
```bash
sudo nvme device-self-test /dev/nvme0 -s 1
```

**Run device self-test (Extended):**
```bash
sudo nvme device-self-test /dev/nvme0 -s 2
```

**Check self-test results:**
```bash
sudo nvme self-test-log /dev/nvme0
```

## Formatting & Secure Erase

> **Warning:** These commands will destroy data. Double-check device paths. Operations targeting namespaces use `/dev/nvme0n1`, while full drive operations often use the controller `/dev/nvme0`.

**Format namespace (default):**
```bash
sudo nvme format /dev/nvme0n1
```

**Format with specific LBA size:**
```bash
sudo nvme format /dev/nvme0n1 --lbaf=1
```

**Secure Erase (User Data):**
```bash
sudo nvme format /dev/nvme0n1 --ses=1
```

**Cryptographic Erase:**
```bash
sudo nvme format /dev/nvme0n1 --ses=2
```

**Sanitize (Block Erase):**
```bash
sudo nvme sanitize /dev/nvme0 --sanact=2
```

**Sanitize (Crypto Erase):**
```bash
sudo nvme sanitize /dev/nvme0 --sanact=4
```

**Check Sanitize Status:**
```bash
sudo nvme sanitize-log /dev/nvme0
```

## Firmware Management

**Check current firmware version:**
```bash
sudo nvme fw-log /dev/nvme0
```

**Download firmware to device:**
```bash
sudo nvme fw-download /dev/nvme0 --fw=fw_update.bin
```

**Commit firmware (Activate next boot):**
```bash
sudo nvme fw-commit /dev/nvme0 --slot=1 --action=2
```

**Commit & Activate immediately:**
```bash
sudo nvme fw-commit /dev/nvme0 --slot=1 --action=3
```

## Power Management

**Show supported power states:**
```bash
sudo nvme get-feature /dev/nvme0 -f 2
```

**Set active power state:**
```bash
sudo nvme set-feature /dev/nvme0 -f 2 -v <state_id>
```

**Show Autonomous Power Transitions:**
```bash
sudo nvme get-feature /dev/nvme0 -f 11
```

## Namespace Management (Advanced)

**Detach namespace:**
```bash
sudo nvme detach-ns /dev/nvme0 -n 1 -c 0
```

**Delete namespace:**
```bash
sudo nvme delete-ns /dev/nvme0 -n 1
```

**Create namespace (size in blocks):**
```bash
sudo nvme create-ns /dev/nvme0 -s <size> -c <cap> -f <lba_format>
```

**Attach namespace:**
```bash
sudo nvme attach-ns /dev/nvme0 -n 1 -c 0
```

**Reset NVMe controller:**
```bash
sudo nvme reset /dev/nvme0
```
