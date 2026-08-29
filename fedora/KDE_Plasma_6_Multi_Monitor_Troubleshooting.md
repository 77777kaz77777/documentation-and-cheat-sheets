# Fixes for multi-monitor display glitches in KDE Plasma 6.

**Issue:** An external monitor connected via USB-C/Dock or DisplayPort is not detected in KDE System Settings (`kscreen`), even though the monitor is powered on and connected.

---

## Step 1: Diagnose Hardware Detection vs. Software Bug

Before tweaking display settings, verify if the Linux kernel hardware layer sees the physical electrical connection.

Open a terminal (`Konsole`) and run:

```bash
for d in /sys/class/drm/card*-*; do echo "$d: $(cat $d/status)"; done
```

### Interpreting the Results
- **Scenario A: Kernel sees fewer connected displays than physically plugged in**
  - *Example:* Only 2 displays show connected.
  - *Cause:* Physical cable, missing dock power, or hardware bandwidth limitations. Try swapping cables or testing monitors individually.
- **Scenario B: Kernel sees all physical displays as connected**
  - *Example:* 3 displays show connected (`eDP-1`, `DP-3`, `DP-4`), but KDE Settings only shows 2.
  - *Cause:* KWin / KScreen display server allocation error, bandwidth lockout (e.g., high refresh rate), or stale cached display profiles. Proceed to **Step 2**.

---

## Step 2: Reduce Refresh Rate (DisplayPort / USB-C Bandwidth Fix)

Running an external monitor at high refresh rates (e.g., 100Hz or 144Hz) over a shared USB-C / DisplayPort Multi-Stream Transport (MST) dock can consume all available bus bandwidth. This causes KWin to silently fail to allocate a display output for the second external screen.

1. Open **System Settings** → **Display & Monitor**.
2. Select the currently working external display.
3. Lower the **Refresh Rate** from 100 Hz (or higher) down to **60 Hz** or **59.94 Hz**.
4. Click **Apply**.

---

## Step 3: Clear Stale KScreen Cache and Restart Services

KDE Plasma caches display configurations. If a previous layout failed or corrupted, KScreen may refuse to initialize newly connected ports.

1. Wipe the cached display configuration files:
   ```bash
   rm -rf ~/.local/share/kscreen/
   ```
2. Restart the KDE display daemon:
   ```bash
   systemctl --user restart plasma-kscreen.service
   ```
3. Unplug the USB-C dock or monitor cable from your laptop, wait 5 seconds, and plug it back in.

---

## Step 4: Verify Recognized Outputs

Check if KDE Plasma now recognizes all connected displays:

```bash
kscreen-doctor --outputs
```

You should now see all outputs listed (e.g., `eDP-1`, `DP-3`, `DP-4`).

---

## Step 5: Force Enable Display (If Recognized but Disabled)

If `kscreen-doctor` lists the display port (e.g., `DP-4`) but it remains dark, manually trigger it to turn on:

```bash
kscreen-doctor output.DP-4.enable
```

*(Replace `DP-4` with the specific port name identified in Step 1.)*

---

## Step 6: Fallback Options

If the display still fails to register under Wayland:

- **Test under X11:** Log out of your desktop session. On the SDDM login screen, change the session type from **Plasma (Wayland)** to **Plasma (X11)** and log in.
- **Direct Port Connection:** If both monitors are plugged into a single USB-C dock, try plugging one monitor into the dock and the other directly into an HDMI/DisplayPort on the laptop to bypass USB-C MST bandwidth limits.
