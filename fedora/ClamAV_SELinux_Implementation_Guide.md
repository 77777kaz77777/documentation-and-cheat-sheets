# Document Name: ClamAV_SELinux_Implementation_Guide.md

# Comprehensive ClamAV & SELinux Implementation Guide (Fedora 44)

This technical reference provides an in-depth breakdown of the interactions between the ClamAV daemon, systemd, and SELinux on Fedora. It explains the underlying mechanics of file descriptor passing, socket communication, and mandatory access control constraints.

## 1. System Architecture & SELinux Mechanics

Fedora’s implementation of ClamAV differs significantly from Debian-based systems, specifically in how it handles services and security boundaries.

* **Instantiated Systemd Services (`clamd@.service`):** Fedora uses systemd template units. Instead of a single monolithic daemon, you can run multiple ClamAV instances with different configurations. `clamd@scan.service` explicitly instructs systemd to look for `/etc/clamd.d/scan.conf` and use it as the operational blueprint for that specific daemon instance.
* **Mandatory Access Control (MAC):** SELinux operates on a "default deny" principle. Even if the `clamd` process runs as the `root` user, SELinux confines it to the `antivirus_t` security domain. By default, `antivirus_t` is forbidden from reading user home directories (`user_home_t`) or core system binaries (`bin_t`).
* **The File Descriptor (`--fdpass`) Conflict:** When `clamdscan` runs, it normally opens a file and passes the open OS-level file handle (descriptor) across the UNIX socket to `clamd`. SELinux views passing an open file descriptor across security boundaries as a severe security risk and terminates the transfer. This is why the daemon logs `Control message truncated`.
* **The Streaming (`--stream`) Solution:** Using `--stream` forces the `clamdscan` client to read the file into memory itself and stream the raw bytes over the socket to the daemon. The daemon never requests a file handle, entirely bypassing the SELinux descriptor restriction.

---

## 2. Daemon Provisioning & Policy Configuration

The following sequence details the exact technical changes required to bring the daemon online, configure its runtime environment, and map it correctly to Fedora's SELinux policies.

1. **Provision the Configuration Blueprint:** Required for systemd template binding.
The daemon requires a specific configuration file to bind to `clamd@scan.service`. We copy the upstream sample, and immediately strip the `Example` directive. ClamAV hardcodes an exit function if it detects the string `Example` in a config file to prevent unconfigured daemons from starting.

```bash
if [ ! -f /etc/clamd.d/scan.conf ]; then
    sudo cp /etc/clamd.d/scan.conf.sample /etc/clamd.d/scan.conf
fi
sudo sed -i '/^Example/d' /etc/clamd.d/scan.conf
```

2. **Configure Inter-Process Communication:** Establishing the IPC UNIX socket.
The daemon must establish a local UNIX socket to receive scan instructions from clients. We configure it to build this socket in `/run/clamd.scan/`.

```bash
sudo sed -i 's|^#LocalSocket /run/clamd.scan/clamd.sock|LocalSocket /run/clamd.scan/clamd.sock|' /etc/clamd.d/scan.conf
```

3. **Elevate Daemon Execution to Root:** Bypassing standard POSIX permissions.
By default, the daemon drops privileges to the `clamupdate` user. To read files across the entire filesystem (like `/home` or `/root`), we must force the daemon to retain `root` execution privileges at the POSIX level.

```bash
sudo sed -i 's|^User .*|User root|' /etc/clamd.d/scan.conf
```

4. **Construct the Runtime Environment:** Handling volatile tmpfs storage.
Fedora mounts `/run` as `tmpfs` (RAM). On reboot, this directory is destroyed. If the directory for the socket does not exist when the service starts, `clamd` crashes. We create it and assign ownership so the daemon can initialize the socket file.

```bash
sudo mkdir -p /run/clamd.scan
sudo chown clamupdate:clamupdate /run/clamd.scan
```

5. **Toggle SELinux Kernel Booleans:** Modifying the active kernel security policy.
Standard POSIX root permissions are insufficient under SELinux. We must persistently (`-P`) toggle two kernel booleans. `antivirus_can_scan_system` explicitly permits the `antivirus_t` domain to traverse user and system file labels. `antivirus_use_jit` permits the daemon to allocate writable/executable memory pages required by the PCRE (Perl Compatible Regular Expressions) engine for signature matching.

```bash
sudo setsebool -P antivirus_can_scan_system 1
sudo setsebool -P antivirus_use_jit 1
```

6. **Restore Extended Security Attributes:** Aligning security attributes.
Manual directory creation assigns incorrect default SELinux context labels (e.g., `unconfined_t`). `restorecon` queries the system policy database and recursively reapplies the correct labels (e.g., `antivirus_var_run_t`), preventing access denials based on context mismatches.

```bash
sudo restorecon -Rv /run/clamd.scan /etc/clamd.d/
```

7. **Initialize Database and Daemon:** Satisfying daemon startup requirements.
The daemon requires valid bytecode signatures (`.cvd` or `.cld` files) in `/var/lib/clamav/` to compile its scanning engine. `freshclam` pulls these directly from the mirror network.

```bash
sudo freshclam
sudo systemctl enable --now clamd@scan
```

---

## 3. Production Scanning Script (`/usr/local/bin/sys-scan`)

This script acts as the primary scanning utility. It relies on bash strict mode (`set -euo pipefail`) to fail safely on pipeline errors. It leverages `--multiscan` to instruct the daemon to use multi-threading, drastically reducing scan times across large directories.

Edit the script with `sudo nano /usr/local/bin/sys-scan`:

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "========================================="
echo "    Starting Manual ClamAV System Scan   "
echo "========================================="
echo "Scanning: /home, /usr/bin, /usr/local/bin"
echo "Please wait..."

SOCKET_PATH="/run/clamd.scan/clamd.sock"
CONFIG_PATH="/etc/clamd.d/scan.conf"

# Verify if the ClamAV daemon is currently listening on the UNIX socket
if [ -S "$SOCKET_PATH" ]; then
    # --config-file: Forces clamdscan to locate the correct socket path
    # --multiscan: Enables multi-threaded scanning by the daemon
    # --stream: Passes raw bytes to avoid SELinux descriptor blocks
    clamdscan --config-file="$CONFIG_PATH" --multiscan --stream /home /usr/bin /usr/local/bin
else
    echo "Warning: ClamAV daemon socket not found at $SOCKET_PATH."
    echo "Falling back to standalone engine (clamscan)..."
    # Fallback to the slow, single-threaded standalone engine if the daemon is dead
    clamscan -r --infected /home /usr/bin /usr/local/bin
fi

echo "========================================="
echo "             Scan Complete               "
echo "========================================="
```

Apply executable permissions:

```bash
sudo chmod +x /usr/local/bin/sys-scan
```

---

## 4. Operational & Troubleshooting Reference

When diagnosing failures, rely on `journalctl` for systemd/daemon errors and `ausearch` for kernel-level security denials.

| Symptom / Error | Technical Root Cause | Resolution |
| --- | --- | --- |
| `Unit clamav-daemon.service not found` | Attempting to manage a Debian-specific unit name in a Fedora systemd environment. | Issue commands to `clamd@scan.service`. |
| `Can't send to clamd: Broken pipe` | The client script attempted to connect to `/run/clamd.scan/clamd.sock`, but no daemon process was listening. | Restart the daemon via `sudo systemctl restart clamd@scan`. |
| `Control message truncated` | `clamdscan` used `--fdpass`. SELinux intercepted and killed the file descriptor transfer at the kernel level. | Ensure the scanning script explicitly uses the `--stream` flag. |
| Scan executes in `< 0.5 sec` but logs `Total errors` | The daemon rejected the scan request immediately, usually due to a POSIX `Permission denied` on the target directory. | Verify `User root` is set in `/etc/clamd.d/scan.conf`. |

**SELinux Audit Logging:**
If files are still not scanning correctly, you can query the system audit logs for raw SELinux Access Vector Cache (AVC) denials to see exactly which file ClamAV was blocked from reading:

```bash
sudo ausearch -m avc -ts recent -c clamd
```
