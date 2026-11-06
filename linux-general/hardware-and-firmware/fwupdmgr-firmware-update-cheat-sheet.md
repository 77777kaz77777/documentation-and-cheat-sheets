## How to check for and apply hardware firmware updates with fwupdmgr

# fwupdmgr Firmware Update Cheat Sheet

## Discovery and Refresh

**List all detected hardware devices capable of firmware updates:**

```bash
fwupdmgr get-devices
```

**Download the latest firmware metadata from the Linux Vendor Firmware Service (LVFS):**

```bash
fwupdmgr refresh
```

**Check if any updates are available for your specific hardware:**

```bash
fwupdmgr get-updates
```

## Installation and Management

**Apply all available firmware updates. (May require a reboot):**

```bash
fwupdmgr update
```

**Downgrade a specific device to an earlier firmware version (if supported):**

```bash
fwupdmgr downgrade
```

**Reinstall the current firmware version (useful for troubleshooting corruption):**

```bash
fwupdmgr reinstall
```

**View the history of all firmware updates applied to the system:**

```bash
fwupdmgr get-history
```

## Security and Diagnostics

**Run an analysis of system security attributes (e.g., Secure Boot, TPM state, Intel BootGuard):**

```bash
fwupdmgr security
```

**Cryptographically verify that installed firmware matches the signatures on LVFS:**

```bash
fwupdmgr verify
```
