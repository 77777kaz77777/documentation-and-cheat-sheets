# How to deploy and automate ClamAV scans on Fedora.

This document outlines the complete process for installing, configuring, and automating ClamAV Antivirus on Fedora Linux. It includes steps for removing incomplete upstream installations, configuring the ClamAV daemon (`clamd`), managing SELinux policies, and deploying custom automation scripts using systemd timers.

---

## 1. Installation

If an incomplete upstream standalone RPM was previously installed, it must be removed first to prevent conflicts with the native Fedora packages.

### Clean Previous Installations

```bash
sudo dnf remove clamav
```

### Install Fedora Official Packages

Install the complete ClamAV suite, including the daemon, updater, and core utilities from the official Fedora repositories.

```bash
sudo dnf install clamav clamav-update clamd
```

---

## 2. Daemon Configuration

Fedora's default `clamd` configuration includes a deliberate safety lock (`Example`) and lacks an active socket configuration. You must overwrite the default `/etc/clamd.d/scan.conf` file to enable local socket connections for the `clamscan` user group.

### Apply Configuration via `tee`

```bash
cat << 'EOF' | sudo tee /etc/clamd.d/scan.conf > /dev/null
# /etc/clamd.d/scan.conf
# Complete configuration for Fedora clamd@scan.service

LogSyslog yes
LogFacility LOG_LOCAL6
LogClean no

LocalSocket /run/clamd.scan/clamd.sock
LocalSocketGroup clamscan
LocalSocketMode 660

User clamscan

MaxDirectoryRecursion 15
FollowDirectorySymlinks yes
FollowFileSymlinks yes
ReadTimeout 180
MaxThreads 12
MaxConnectionQueueLength 15
EOF
```

---

## 3. Signature Updates & Service Activation

Before starting the daemon, you must download the initial malware definitions.

### Download Initial Signatures

```bash
sudo freshclam
```

### Enable Background Services

Enable and start the ClamAV scanning daemon and the automatic background signature updater.

```bash
sudo systemctl enable --now clamd@scan.service
sudo systemctl enable --now clamav-freshclam.service
```

Verify the daemon is running successfully:

```bash
sudo systemctl status clamd@scan.service
