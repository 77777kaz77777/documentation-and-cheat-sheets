# macOS Security Cheat Sheet

Quick-reference guide for FileVault, Gatekeeper, code signing, XProtect, privacy permissions, the Keychain, and Touch ID for `sudo` on macOS.

---

## 1. Security Status at a Glance

**Check FileVault Full-Disk Encryption Status:**

```bash
fdesetup status
```

**Check System Integrity Protection (SIP) Status:**

```bash
csrutil status
```

**Check Gatekeeper Status (`assessments enabled` Means It's On):**

```bash
spctl --status
```

**Check the Application Firewall Status:**

```bash
/usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate
```

**Check Whether Automatic Security Updates Are Enabled:**

```bash
defaults read /Library/Preferences/com.apple.SoftwareUpdate
```

Look for `AutomaticallyInstallMacOSUpdates`, `ConfigDataInstall`, and `CriticalUpdateInstall` set to `1`.

**Check Activation Lock (Find My) Status:**

```bash
system_profiler SPHardwareDataType | grep "Activation Lock"
```

---

## 2. FileVault Disk Encryption

**Show Whether FileVault Is On:**

```bash
fdesetup isactive
```

**List Users Who Can Unlock the Disk at Startup:**

```bash
sudo fdesetup list
```

**Turn On FileVault (Prints a Recovery Key; Store It Safely):**

```bash
sudo fdesetup enable
```

**Check Whether a Personal Recovery Key Exists:**

```bash
sudo fdesetup haspersonalrecoverykey
```

**Create a New Personal Recovery Key:**

```bash
sudo fdesetup changerecovery -personal
```

---

## 3. Gatekeeper, Code Signing & Quarantine

**Check Whether Gatekeeper Would Allow an App to Run:**

```bash
spctl --assess -vv /Applications/[AppName].app
```

**Verify Code Signature & Deep Strict Validation of an App Bundle:**

```bash
codesign -dvv --deep --strict /Applications/[AppName].app
```

**Show Who Signed an App (Developer ID and Team):**

```bash
codesign -dv --verbose=4 /Applications/[AppName].app 2>&1 | grep -E "Authority|TeamIdentifier"
```

**Show an App's Entitlements (What It's Allowed to Access):**

```bash
codesign -d --entitlements - /Applications/[AppName].app
```

**Verify Notarization Ticket Stapled to an App Bundle:**

```bash
stapler validate /Applications/[AppName].app
```

**Inspect Extended Attributes (`xattr`) on a File or Application:**

```bash
xattr -l /Applications/[AppName].app
```

**Remove Quarantine Flag from a Downloaded Binary or Unsigned App:**

```bash
sudo xattr -dr com.apple.quarantine /Applications/[AppName].app
```

Only remove quarantine from software you trust: it bypasses the Gatekeeper check for that app.

---

## 4. XProtect & Malware Protection

**Check XProtect Antivirus Version:**

```bash
xprotect version
```

**Perform Manual XProtect Scan & Signature Update:**

```bash
sudo xprotect check
sudo xprotect update
```

**List Login Items and Background Apps (Common Place for Unwanted Software):**

```bash
sudo sfltool dumpbtm
```

**List Third-Party LaunchAgents and LaunchDaemons:**

```bash
ls ~/Library/LaunchAgents /Library/LaunchAgents /Library/LaunchDaemons
```

---

## 5. Privacy Permissions (TCC)

macOS asks before apps can use the camera, microphone, files, screen recording, and more. These commands reset those decisions so the app asks again.

**Reset One App's Camera Permission:**

```bash
tccutil reset Camera [com.example.bundle-id]
```

**Reset Screen Recording Permission for All Apps:**

```bash
tccutil reset ScreenCapture
```

**Find an App's Bundle ID (Needed Above):**

```bash
osascript -e 'id of app "[AppName]"'
```

Other service names include `Microphone`, `Accessibility`, `SystemPolicyAllFiles` (Full Disk Access), and `All`.

---

## 6. Keychain & Certificates (`security`)

**List Keychains:**

```bash
security list-keychains
```

**Read a Saved Password from the Keychain (Prompts for Approval):**

```bash
security find-generic-password -s "[service name]" -w
```

**Store a Password in the Keychain for Use in Scripts:**

```bash
security add-generic-password -a "$USER" -s "[service name]" -w
```

**Trust a Root Certificate System-Wide (For Example, Caddy's Internal CA):**

```bash
sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain ~/Downloads/[root].crt
```

**Find a Certificate by Name:**

```bash
security find-certificate -a -c "[name]" -p
```

**Remove a Trusted Certificate:**

```bash
sudo security remove-trusted-cert -d ~/Downloads/[root].crt
```

**Store SSH Key Passphrases in the Keychain:**

```bash
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

Add `UseKeychain yes` and `AddKeysToAgent yes` under `Host *` in `~/.ssh/config` so keys load automatically after a restart.

---

## 7. Use Touch ID for `sudo`

macOS 14 Sonoma and later keep this setting through system updates:

```bash
sed "s/^#auth/auth/" /etc/pam.d/sudo_local.template | sudo tee /etc/pam.d/sudo_local
```

Open a new terminal and run `sudo -v`: a Touch ID prompt should appear. Delete `/etc/pam.d/sudo_local` to turn it off again.

---

## 8. Configuration & MDM Profiles

**List Installed Configuration / MDM Profiles:**

```bash
profiles status
sudo profiles list
```

**Check Whether the Mac Is Enrolled in Device Management (MDM):**

```bash
profiles status -type enrollment
```

---

## 9. Quick Reference

```bash
fdesetup status                       # FileVault
csrutil status                        # System Integrity Protection
spctl --status                        # Gatekeeper
spctl --assess -vv /Applications/X.app   # would Gatekeeper allow it?
codesign -dvv /Applications/X.app     # who signed it
xattr -l file                         # quarantine and other attributes
sudo sfltool dumpbtm                  # login items and background apps
tccutil reset Camera bundle.id        # reset a privacy permission
security find-generic-password -s name -w   # read a Keychain password
```

---

## Sources & Verification

* **Built-in manual pages:** run `man <command>` (for example `man codesign`)

## Related guides

* [macOS Command-Line Reference (Apple Silicon)](macos-command-line-reference.md)
* [macOS Homebrew Cheat Sheet](macos-homebrew-cheat-sheet.md)
* [macOS System, Updates and Hardware Cheat Sheet](macos-system-updates-and-hardware-cheat-sheet.md)
* [macOS Networking Cheat Sheet](macos-networking-cheat-sheet.md)
* [macOS launchd, Processes and Logs Cheat Sheet](macos-launchd-and-logs-cheat-sheet.md)
* [macOS defaults, Finder and CLI Tips Cheat Sheet](macos-defaults-and-cli-tips-cheat-sheet.md)
