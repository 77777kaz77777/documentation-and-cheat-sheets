## DNF Package Manager Speed Optimization & Configuration Guide

### 1. Open the DNF configuration file
Open the file using a terminal text editor with elevated privileges:
```bash
sudo nano /etc/dnf/dnf.conf
```

### 2. Update Configuration Parameters
Add or update the parameters under the `[main]` section. If the parameters already exist, change their values; otherwise, append them to the file.

```ini
[main]
gpgcheck=1
installonly_limit=3
clean_requirements_on_remove=true
best=False
skip_if_unavailable=True
max_parallel_downloads=10
fastestmirror=True
```

### 3. Apply Changes
Clear and refresh the metadata cache to apply the changes:
```bash
sudo dnf clean all
sudo dnf makecache
```

### Configuration Parameters Explained
* **`gpgcheck=1`**: Enforces cryptographic signature verification for downloaded packages against trusted local keys before installation.
* **`installonly_limit=3`**: Limits the maximum number of simultaneous versions of "install-only" packages (such as the Linux kernel) that can be kept on the system.
* **`clean_requirements_on_remove=true`**: Automatically purges orphaned dependencies when the parent package is uninstalled.
* **`best=False`**: Instructs DNF to tolerate slightly older or non-ideal package versions during transactions if the absolute latest version cannot be installed due to dependency conflicts.
* **`skip_if_unavailable=True`**: Tells DNF to bypass specific repositories if they are unreachable, offline, or experiencing timeout errors.
* **`max_parallel_downloads=10`**: Increases the maximum number of simultaneous package downloads from 3 up to 10.
* **`fastestmirror=True`**: Measures response times across available mirror servers and automatically selects the fastest responding mirrors.