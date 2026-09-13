
## A comprehensive setup for deploying LibrePods on Linux to enable native Apple AirPods capabilities, including advanced configuration for Bluetooth and media controls. It also includes an automated Bash script and instructions for managing the application via Gearlever

LibrePods unlocks native AirPods capabilities on Linux, including noise control modes, adaptive transparency, ear detection, and battery status reporting.

## 1. System-Level Bluetooth Configuration

The BlueZ Linux stack disables the experimental D-Bus interfaces required to monitor BLE signals by default. LibrePods requires the `--experimental` (`-E`) flag enabled in the Bluetooth systemd service.

Additionally, to ensure the connection remains stable, the BlueZ controller must operate in dual mode (`ControllerMode = dual`), allowing simultaneous standard audio streams and BLE data streams.

## 2. Managing AppImages with Gearlever

Instead of manually moving the AppImage and creating desktop entries, Gearlever provides a graphical interface to organize AppImages, automatically generate desktop entries, and seamlessly handle executable permission issues. Since the current primary environment utilizes Fedora Linux, Gearlever can be installed directly via Flatpak.

```bash
flatpak install flathub it.mijorus.gearlever
```

Once installed, open Gearlever and drag the LibrePods AppImage into the window to integrate it into the application launcher.

## 3. Enabling Media Controls (PipeWire/WirePlumber)

If tap gestures (Play/Pause/Skip) are not functioning, AVRCP support must be enabled. For systems utilizing PipeWire/WirePlumber:

1. Create a WirePlumber configuration directory and file:

```bash
mkdir -p ~/.config/wireplumber/wireplumber.conf.d/
nano ~/.config/wireplumber/wireplumber.conf.d/51-bluez-avrcp.conf
```

1. Add the following block to enable the dummy AVRCP player:

```ini
monitor.bluez.properties = {
  bluez5.dummy-avrcp-player = true
}
```

1. Restart WirePlumber:

```bash
systemctl --user restart wireplumber
```

## 4. Command-Line Controls

LibrePods includes `librepods-ctl` to control the AirPods directly from the terminal or in scripts while the main application is running.

| Command | Description |
| --- | --- |
| `librepods-ctl noise:off` | Disable noise control |
| `librepods-ctl noise:anc` | Enable Active Noise Cancellation |
| `librepods-ctl noise:transparency` | Enable Transparency mode |
| `librepods-ctl noise:adaptive` | Enable Adaptive mode |

## 5. Hearing Aid Features

To adjust amplification, balance, tone, ambient noise reduction, own voice amplification, and conversation boost, LibrePods uses a separate script (`hearing_aid.py`).

Because AirPods check for the DeviceID characteristic to verify an Apple device before allowing hearing aid features, the DeviceID must be explicitly set in the BlueZ configuration.

1. Open `/etc/bluetooth/main.conf` as root.
2. Add this line under the `[General]` section:

```ini
DeviceID = bluetooth:004C:0000:0000
```

1. Restart Bluetooth and re-pair the AirPods:

```bash
sudo systemctl restart bluetooth
```

1. Run the Python script to apply audiogram settings:

```bash
python3 hearing_aid.py
```

*Note: This setting may cause AirPods to occasionally disconnect if they expect more Apple-specific information; once hearing aid features are configured, the DeviceID can be reverted to its previous state to ensure stable connectivity.*

## 6. Automated Setup Script

The following Bash script automates the BlueZ systemd override, WirePlumber AVRCP configuration, and Gearlever installation.

### setup_librepods.sh

```bash
#!/bin/bash
# setup_librepods.sh
# Automates LibrePods system requirements, media controls, and installs Gearlever.

if [ "$EUID" -eq 0 ]; then
  echo "Error: Please run this script as your standard user."
  echo "It will prompt for sudo automatically when modifying system directories."
  exit 1
fi

echo "Configuring BlueZ experimental features..."
sudo mkdir -p /etc/systemd/system/bluetooth.service.d

# Write the override configuration to append the experimental flag (-E)
echo -e "[Service]\nExecStart=\nExecStart=/usr/libexec/bluetooth/bluetoothd -E" | sudo tee /etc/systemd/system/bluetooth.service.d/override.conf > /dev/null

echo "Applying systemd configuration and restarting the Bluetooth daemon..."
sudo systemctl daemon-reload
sudo systemctl restart bluetooth

echo "Configuring PipeWire/WirePlumber for AirPods media controls (AVRCP)..."
mkdir -p ~/.config/wireplumber/wireplumber.conf.d/
cat << 'EOF' > ~/.config/wireplumber/wireplumber.conf.d/51-bluez-avrcp.conf
monitor.bluez.properties = {
  bluez5.dummy-avrcp-player = true
}
EOF

echo "Restarting WirePlumber..."
systemctl --user restart wireplumber

echo "Installing Gearlever via Flatpak to manage the AppImage..."
# Ensures Flatpak is up to date and installs Gearlever from Flathub
flatpak remote-add --if-not-exists flathub [https://dl.flathub.org/repo/flathub.flatpakrepo](https://dl.flathub.org/repo/flathub.flatpakrepo)
flatpak install -y flathub it.mijorus.gearlever

echo "Setup complete!"
echo "Open Gearlever from your application menu and drag the LibrePods AppImage into it."
```
