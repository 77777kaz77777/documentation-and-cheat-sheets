# How to format and create a multi-boot Ventoy USB drive on Linux.

This guide provides step-by-step instructions to create a Ventoy USB drive on Fedora Linux using either the graphical WebGUI or the command-line interface.

> ⚠️ **Warning:** Installing Ventoy will completely format the USB drive and wipe all existing data on it. Back up any important files before proceeding.

---

## Step-by-Step Instructions

### Step 1: Identify your USB drive path
Plug in your USB flash drive and open a terminal. Run `lsblk` to identify its device name:

```bash
lsblk
```

Look for your USB drive in the list (e.g., `sdb` or `sdc`). Note the device path without partition numbers (use `/dev/sdb`, not `/dev/sdb1`).

---

### Step 2: Download and extract Ventoy
Download the latest Linux `.tar.gz` package from Ventoy's GitHub release page or run the following commands in your terminal:

```bash
wget [https://github.com/ventoy/Ventoy/releases/download/v1.0.99/ventoy-1.0.99-linux.tar.gz](https://github.com/ventoy/Ventoy/releases/download/v1.0.99/ventoy-1.0.99-linux.tar.gz)
tar -xvf ventoy-1.0.99-linux.tar.gz
cd ventoy-1.0.99/
```

---

### Step 3: Choose an installation method

#### Option A: Install via WebGUI (Recommended)
Launch the WebGUI installer with administrator privileges:

```bash
sudo ./VentoyWeb.sh
```

1. Open the URL printed in the terminal (typically `http://127.0.0.1:24684`) in your web browser.
2. Select your USB drive from the device dropdown list.
3. Click **Install**.
4. Once finished, return to the terminal and press `Ctrl+C` to stop the web server.

#### Option B: Install via CLI
Run `Ventoy2Disk.sh` with the `-i` flag targeting your USB drive:

```bash
sudo ./Ventoy2Disk.sh -i /dev/sdX
```

*(Replace `/dev/sdX` with your actual drive path, e.g., `/dev/sdb`)*

---

### Step 4: Copy ISO files to the USB
1. Unplug and re-plug your USB drive (or remount it).
2. Open the volume labeled **Ventoy**.
3. Drag and drop any ISO image files (Fedora, Ubuntu, Windows, etc.) directly onto the drive.
