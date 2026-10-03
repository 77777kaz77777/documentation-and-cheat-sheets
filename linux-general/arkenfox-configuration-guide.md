# Arkenfox Configuration and Updater Guide

## 1. Script Download and Initialization

Navigate to your Firefox profile directory (standard location on Linux/Fedora):
```bash
cd ~/.mozilla/firefox/*.default-release
```

Download the official Arkenfox maintenance scripts securely via HTTPS:
```bash
curl -O [https://raw.githubusercontent.com/arkenfox/user.js/master/updater.sh](https://raw.githubusercontent.com/arkenfox/user.js/master/updater.sh)
curl -O [https://raw.githubusercontent.com/arkenfox/user.js/master/prefsCleaner.sh](https://raw.githubusercontent.com/arkenfox/user.js/master/prefsCleaner.sh)
```

Make the scripts executable:
```bash
chmod +x updater.sh prefsCleaner.sh
```

## 2. Defining Configuration Overrides

Create or edit `user-overrides.js` in the same directory to restore broken site functionality without modifying the core `user.js` file.

```javascript
// File: user-overrides.js

/* --- 0800: WEBRTC (VIDEO CALLS) --- */
user_pref("media.peerconnection.enabled", true);

/* --- 2000: MEDIA & DRM --- */
user_pref("media.eme.enabled", true);

/* --- 4500: WEBGL (3D GRAPHICS) --- */
user_pref("webgl.disabled", false);

/* --- 5000: BROWSER FEATURES --- */
user_pref("browser.search.suggest.enabled", true);
user_pref("browser.urlbar.suggest.searches", true);
user_pref("browser.formfill.enable", true);

/* --- 7000: UI & BEHAVIOR --- */
user_pref("browser.startup.page", 3);
```

## 3. Update and Merge Workflow

Execute the following commands whenever applying new overrides or updating Arkenfox to match a new Firefox release.

1. **Run the Updater:**
   ```bash
   ./updater.sh
   ```
   *Downloads the latest upstream `user.js` and appends `user-overrides.js` to the bottom.*

2. **Run the Preferences Cleaner:**
   ```bash
   ./prefsCleaner.sh
   ```
   *Forces Firefox to forget any old, orphaned configurations no longer present in the updated `user.js`.*

3. **Restart Firefox** to apply the merged configuration.

## 4. `updater.sh` Security and Safety Audit

The official `updater.sh` script includes strict system safeguards:

* **Root Privilege Prevention:** The script actively checks for elevated privileges (`sudo`/`doas`) and aborts execution to prevent unintended system-wide modifications.
* **Permissions Safeguards:** It scans the current directory for files owned by root (`user 0`) and halts if any are found, protecting profile permissions.
* **Secure File Retrieval:** Downloads are strictly fetched over HTTPS directly from the official Arkenfox GitHub repository (`raw.githubusercontent.com`).
* **Safe Staging:** Incoming updates are downloaded into temporary files (`mktemp`) to ensure complete retrieval before altering active configurations.
* **Non-Destructive Backups:** The script automatically copies the active `user.js` into a `userjs_backups` directory before overwriting it, allowing immediate rollbacks.
