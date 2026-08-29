## Fedora ClamAV & SELinux Implementation Guide

### 1. Installation
Remove any incomplete upstream standalone RPMs to prevent conflicts, then install the official Fedora packages.
```bash
sudo dnf remove clamav
sudo dnf install clamav clamav-update clamd
```

### 2. Daemon Provisioning & Configuration
Fedora's default `clamd` configuration includes a deliberate safety lock (`Example`). Overwrite `/etc/clamd.d/scan.conf` to configure local socket connections and force the daemon to retain `root` execution privileges at the POSIX level so it can read files across the entire filesystem.

```bash
cat << 'EOF' | sudo tee /etc/clamd.d/scan.conf > /dev/null
LogSyslog yes
LogFacility LOG_LOCAL6
LogClean no
LocalSocket /run/clamd.scan/clamd.sock
LocalSocketGroup clamscan
LocalSocketMode 660
User root
MaxDirectoryRecursion 15
FollowDirectorySymlinks yes
FollowFileSymlinks yes
ReadTimeout 180
MaxThreads 12
MaxConnectionQueueLength 15
EOF
```

### 3. Runtime Environment & SELinux Setup
Fedora mounts `/run` as `tmpfs` (RAM). You must create the socket directory and set SELinux booleans to permit scanning and JIT memory allocation. Manual directory creation requires restoring context labels.

```bash
sudo mkdir -p /run/clamd.scan
sudo chown clamupdate:clamupdate /run/clamd.scan

sudo setsebool -P antivirus_can_scan_system 1
sudo setsebool -P antivirus_use_jit 1

sudo restorecon -Rv /run/clamd.scan /etc/clamd.d/
```

### 4. Signature Updates & Service Activation
```bash
sudo freshclam
sudo systemctl enable --now clamd@scan.service
sudo systemctl enable --now clamav-freshclam.service
```

### 5. Production Scanning Script (`/usr/local/bin/sys-scan`)
Using `--stream` forces the `clamdscan` client to read the file into memory itself and stream the raw bytes over the socket to the daemon, bypassing the SELinux descriptor restriction.

```bash
sudo nano /usr/local/bin/sys-scan
```
```bash
#!/usr/bin/env bash
set -euo pipefail

echo "========================================="
echo "    Starting Manual ClamAV System Scan   "
echo "========================================="

SOCKET_PATH="/run/clamd.scan/clamd.sock"
CONFIG_PATH="/etc/clamd.d/scan.conf"

if [ -S "$SOCKET_PATH" ]; then
    clamdscan --config-file="$CONFIG_PATH" --multiscan --stream /home /usr/bin /usr/local/bin
else
    echo "Warning: ClamAV daemon socket not found. Falling back to clamscan..."
    clamscan -r --infected /home /usr/bin /usr/local/bin
fi
```
```bash
sudo chmod +x /usr/local/bin/sys-scan
```

### Operational Troubleshooting
* **`Can't send to clamd: Broken pipe`**: Daemon not listening. Restart via `sudo systemctl restart clamd@scan`.
* **`Control message truncated`**: SELinux intercepted file descriptor transfer. Ensure script uses `--stream`.
* **SELinux Audit Logging**: Query raw AVC denials with `sudo ausearch -m avc -ts recent -c clamd`.