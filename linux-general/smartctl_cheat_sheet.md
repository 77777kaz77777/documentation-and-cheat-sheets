# `smartctl` Comprehensive Cheat Sheet

`smartctl` is a command-line tool for controlling and monitoring storage systems using the Self-Monitoring, Analysis, and Reporting Technology (S.M.A.R.T.) system built into most modern ATA, Serial ATA, SCSI, and NVMe hard drives.

---

## 1. Installation

| Distribution / OS | Command |
| :--- | :--- |
| **Debian / Ubuntu** | `sudo apt install smartmontools` |
| **RHEL / CentOS / Fedora** | `sudo dnf install smartmontools` |
| **Arch Linux** | `sudo pacman -S smartmontools` |
| **Alpine Linux** | `sudo apk add smartmontools` |
| **macOS** (Homebrew) | `brew install smartmontools` |

---

## 2. Basic Syntax & Drive Scanning

### Scan for Available Devices

```bash
# Scan for all smartctl-compatible devices
sudo smartctl --scan

# Scan including OPENED devices (useful for RAID controllers)
sudo smartctl --scan-open
```

### General Syntax

```bash
sudo smartctl [options] /dev/<device_name>
```

> **Note:** Replace `/dev/sdX` with your drive target (e.g., `/dev/sda`, `/dev/nvme0n1`).

---

## 3. Quick Checks & Information

### Basic Info & S.M.A.R.T. Status

```bash
# Display drive hardware info (Model, Serial, Firmware, Family)
sudo smartctl -i /dev/sda

# Quick S.M.A.R.T. health check (PASSED or FAILED)
sudo smartctl -H /dev/sda

# Check if S.M.A.R.T. is supported and enabled
sudo smartctl -i /dev/sda | grep -i "smart"
```

### Enabling & Disabling S.M.A.R.T

```bash
# Enable S.M.A.R.T. on a drive
sudo smartctl -s on /dev/sda

# Disable S.M.A.R.T. on a drive
sudo smartctl -s off /dev/sda

# Enable automatic attribute autosave
sudo smartctl -S on /dev/sda
```

---

## 4. Reading S.M.A.R.T. Data & Attributes

```bash
# Print ALL available S.M.A.R.T. information for a drive
sudo smartctl -a /dev/sda

# Print ALL information, including non-SMART vendor information
sudo smartctl -x /dev/sda

# Print S.M.A.R.T. attributes table only (HDDs & SATA SSDs)
sudo smartctl -A /dev/sda

# Print error log
sudo smartctl -l error /dev/sda

# Print self-test log history
sudo smartctl -l selftest /dev/sda
```

---

## 5. Critical S.M.A.R.T. Attributes to Watch (HDDs)

When reviewing `smartctl -A /dev/sda`, pay special attention to the `RAW_VALUE` of these attributes:

| ID | Attribute Name | Description & Risk |
| :--- | :--- | :--- |
| **5** | `Reallocated_Sector_Ct` | **Critical.** Count of damaged sectors moved to spare area. Non-zero = drive degrading. |
| **187** | `Reported_Uncorrect` | Uncorrectable read errors reported to OS. Non-zero = imminent failure risk. |
| **188** | `Command_Timeout` | Aborted operations due to HDD timeout. Often power/cable issue or failing drive. |
| **197** | `Current_Pending_Sector` | **Critical.** "Unstable" sectors waiting to be remapped on next write. |
| **198** | `Offline_Uncorrectable` | Uncorrectable errors during background scan. Drive is failing. |
| **199** | `UDMA_CRC_Error_Count` | Interface errors. Usually bad SATA cable/connection, not drive failure. |

---

## 6. S.M.A.R.T. Testing (Self-Tests)

### Types of Self-Tests

1. **Short Test (`short`)**: Checks electrical/mechanical properties and a small portion of the disk surface (~2 mins).
2. **Long / Extended Test (`long`)**: Complete surface scan (~hours depending on drive size).
3. **Conveyance Test (`conveyance`)**: Checks for damage incurred during transportation (not supported by all drives).

### Running and Managing Tests

```bash
# Start a short background self-test
sudo smartctl -t short /dev/sda

# Start an extended / long background self-test
sudo smartctl -t long /dev/sda

# Start a conveyance test (if supported)
sudo smartctl -t conveyance /dev/sda

# Check test progress (view self-test log / remaining percentage)
sudo smartctl -l selftest /dev/sda

# Abort an ongoing test
sudo smartctl -X /dev/sda
```

---

## 7. Working with NVMe Drives

NVMe drives use a different S.M.A.R.T. format compared to ATA/SATA drives.

```bash
# Basic info for an NVMe drive
sudo smartctl -i /dev/nvme0n1

# Health and S.M.A.R.T. log for NVMe (Temperature, Wear Level, Critical Warnings)
sudo smartctl -A /dev/nvme0n1

# Full NVMe details
sudo smartctl -a /dev/nvme0n1
```

### Important NVMe Health Indicators

- **Critical Warning:** Should be `0x00`. Non-zero indicates overheating, wear, or memory errors.
- **Percentage Used:** Estimated wear level percentage (100% = end of rated lifetime).
- **Data Units Read / Written:** Total volume of data moved (helps calculate total bytes written / TBW).
- **Media and Data Integrity Errors:** Should be `0`. Non-zero indicates unrecoverable data errors.

---

## 8. Working with Hardware RAID Controllers

To query drives attached behind a hardware RAID controller, specify the controller/device type using the `-d` flag.

### MegaRAID / LSI

```bash
# Query physical drive 0 behind MegaRAID controller
sudo smartctl -a -d megaraid,0 /dev/sda

# Query physical drive 1
sudo smartctl -a -d megaraid,1 /dev/sda
```

### HP Smart Array (cciss)

```bash
# Query physical drive 0
sudo smartctl -a -d cciss,0 /dev/sg0
```

### ARECA RAID

```bash
# Query enclosure 1, disk 2
sudo smartctl -a -d areca,2/1 /dev/sg1
```

### SAT / USB Enclosures

```bash
# Force ATA/SATA mode on USB enclosures or bridges that obscure drive pass-through
sudo smartctl -a -d sat /dev/sdb
```

---

## 9. Background Monitoring with `smartd` Service

`smartd` is the daemon included with `smartmontools` to continuously monitor drives and send alerts on failures.

### Configuration File

`/etc/smartd.conf`

### Common Configuration Examples

```text
# Monitor all drives, send email on warning/failure
DEVICESCAN -m admin@example.com -M exec /usr/share/smartmontools/smartd-runner

# Custom configuration for a specific drive (/dev/sda)
# -a: monitor all SMART properties
# -o on: enable automatic offline testing
# -S on: enable attribute saving
# -s (S/../.././02|L/../../6/03): Short test daily at 2am, Long test Saturdays at 3am
/dev/sda -a -o on -S on -s (S/../.././02|L/../../6/03) -m admin@example.com
```

### Managing the Daemon

```bash
# Enable and start smartd daemon
sudo systemctl enable --now smartd

# Check service status
sudo systemctl status smartd
```

---

## 10. Handy One-Liners & Summary Scripts

```bash
# Get health status of ALL drives at once
for dev in $(sudo smartctl --scan | awk '{print $1}'); do
    echo -n "$dev: "
    sudo smartctl -H "$dev" | grep "SMART overall-health" || echo "UNKNOWN"
done

# Check current temperature of all drives
for dev in $(sudo smartctl --scan | awk '{print $1}'); do
    echo -n "$dev: "
    sudo smartctl -A "$dev" | grep -iE "temperature|Temperature_Celsius" | awk '{print $10 "°C"}'
done
```
