## How to check for and apply hardware firmware updates with fwupdmgr

# fwupdmgr Firmware Update Cheat Sheet

## Discovery and Refresh

| Command | Description |
| :--- | :--- |
| `fwupdmgr get-devices` | List all detected hardware devices capable of firmware updates. |
| `fwupdmgr refresh` | Download the latest firmware metadata from the Linux Vendor Firmware Service (LVFS). |
| `fwupdmgr get-updates` | Check if any updates are available for your specific hardware. |

## Installation and Management

| Command | Description |
| :--- | :--- |
| `fwupdmgr update` | Apply all available firmware updates. (May require a reboot). |
| `fwupdmgr downgrade` | Downgrade a specific device to an earlier firmware version (if supported). |
| `fwupdmgr reinstall` | Reinstall the current firmware version (useful for troubleshooting corruption). |
| `fwupdmgr get-history` | View the history of all firmware updates applied to the system. |

## Security and Diagnostics

| Command | Description |
| :--- | :--- |
| `fwupdmgr security` | Run an analysis of system security attributes (e.g., Secure Boot, TPM state, Intel BootGuard). |
| `fwupdmgr verify` | Cryptographically verify that installed firmware matches the signatures on LVFS. |
