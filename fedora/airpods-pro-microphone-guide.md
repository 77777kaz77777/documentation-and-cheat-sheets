# AirPods Pro 3 Microphone Configuration on Fedora 44 KDE

When connecting AirPods to Fedora Linux, the system defaults to a high-fidelity playback profile (A2DP) which disables the microphone. To use the microphone, you must switch to a Headset profile (HSP/HFP).

Additionally, WirePlumber's autoswitch feature often reverts the headset back to the playback-only profile. Below are the steps to prevent this and force the microphone profile to remain active.

## 1. Make the Microphone Profile Permanent

To prevent WirePlumber from automatically switching away from your chosen headset profile, you need to create a custom configuration rule.

**Step 1: Create the configuration directory and file**
Open your terminal and run the following commands:

```bash
mkdir -p ~/.config/wireplumber/wireplumber.conf.d
nano ~/.config/wireplumber/wireplumber.conf.d/51-bluetooth-persistent-profile.conf
```

**Step 2: Add the configuration settings**
Paste the following block into the file to disable autoswitching and enable persistent storage:

```json
wireplumber.settings = {
  bluetooth.use-persistent-storage = true
  bluetooth.autoswitch-to-headset-profile = false
}
```

Save and exit the file (in nano, press `Ctrl+O`, `Enter`, then `Ctrl+X`).

**Step 3: Apply the changes**
Restart the WirePlumber service to apply the new rules:

```bash
systemctl --user restart wireplumber
```

## 2. Choosing the Right Audio Profile

After applying the fix above, open your KDE Audio Volume widget, click the three vertical dots (`⋮`) next to **Karim's AirPods Pro** under *Output Devices*, and select the appropriate profile based on the laptop you are using:

### Laptop 1 (Zephyrus / LC3 Supported)

* **Best Profile:** `Headset Head Unit (HSP/HFP, codec LC3-24kHz)`
* **Why:** The LC3 codec offers the highest sample rate (24kHz) and the best overall voice and audio quality for two-way communication.

### Laptop 2 (ThinkPad / No LC3 Support)

* **Best Profile:** `Headset Head Unit (HSP/HFP, codec mSBC)`
* **Why:** Because the Bluetooth adapter on this laptop does not expose the LC3 codec, mSBC is the next best option. It provides wideband speech (16kHz), which is significantly clearer than the older, default CVSD codec.

**Verification:**
Once the correct profile is selected, " AirPods Pro" will immediately appear under the **Input Devices** section in your audio widget, confirming the microphone is active and ready to use.
