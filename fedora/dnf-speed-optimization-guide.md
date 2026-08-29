## DNF Package Manager Speed Optimization & Configuration Guide

To speed up `dnf` by applying the recommended configurations (`max_parallel_downloads=10` and `fastestmirror=True`), follow the steps below to update your DNF configuration file.

## Step-by-Step Instructions

### 1. Open the DNF configuration file
Open the file using a terminal text editor with elevated privileges:

```bash
sudo nano /etc/dnf/dnf.conf
```

### 2. Update Configuration Parameters
Add or update the parameters under the `[main]` section. If the parameters already exist, change their values; otherwise, append them to the file. 

*(Ensure each parameter is on its own line exactly as shown below)*:

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

### 3. Save and Exit
In nano, press `Ctrl + O`, then `Enter` to save, and `Ctrl + X` to exit.

### 4. Apply Changes
Clear and refresh the metadata cache to apply the changes:

```bash
sudo dnf clean all
sudo dnf makecache
```
