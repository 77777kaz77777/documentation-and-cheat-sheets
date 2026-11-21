# macOS Security Cheat Sheet

Quick-reference guide for Gatekeeper, XProtect, code signing, and FileVault disk encryption on macOS.

---

**Check FileVault Full-Disk Encryption Status:**

```bash
fdesetup status
```

**Check System Integrity Protection (SIP) Status:**

```bash
csrutil status
```

**Verify Code Signature & Deep Strict Validation of an App Bundle:**

```bash
codesign -dvv --deep --strict /Applications/[AppName].app
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

**Check XProtect Antivirus Version:**

```bash
xprotect version
```

**Perform Manual XProtect Scan & Signature Update:**

```bash
sudo xprotect check
sudo xprotect update
```

**List Installed Configuration / MDM Profiles:**

```bash
profiles status
sudo profiles list
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
