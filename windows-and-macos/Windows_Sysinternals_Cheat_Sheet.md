## A practical guide to core Microsoft Sysinternals tools (Process Explorer, Process Monitor, Autoruns, PsExec, and TCPView), highlighting specific filters, shortcuts, and commands for advanced troubleshooting, malware isolation, and remote system administration.

## 1. Process Explorer (procexp.exe)

* **Find locked files:** Press `Ctrl + F` and type a filename or folder name to see exactly which process is locking it (preventing deletion).
* **Verify image signatures:** Go to **Options > Verify Image Signatures** to highlight executables that lack valid digital signatures (useful for malware hunting).
* **Check VirusTotal:** Go to **Options > VirusTotal.com > Check VirusTotal.com** to automatically hash and scan running processes against 70+ antivirus engines.
* **Suspend processes:** Right-click a process and select **Suspend** to freeze it without killing it (useful for isolating suspected malware while preserving memory).

## 2. Process Monitor (procmon.exe)

* **The "Target" Tool:** Click the "bullseye" icon in the toolbar and drag it over an application window. Procmon will automatically filter traffic to show only activity from that application's process.
* **Boot Logging:** Go to **Options > Enable Boot Logging**. Restart the PC to capture all activity happening during the Windows boot sequence (essential for diagnosing slow boot times or startup crashes).
* **Essential Filters to apply (`Ctrl + L`):**
  * `Result` is `NAME NOT FOUND` (Useful for finding missing DLLs).
  * `Result` is `ACCESS DENIED` (Useful for troubleshooting permission issues).
  * `Path` contains `[Your App Name]`.

## 3. Autoruns (autoruns.exe)

* **Hide Microsoft Entries:** Go to **Options > Hide Microsoft Entries** to filter out standard Windows processes and see only third-party software starting up.
* **Analyze Offline Systems:** Go to **File > Analyze Offline System**. You can point Autoruns to the `C:\Windows` directory of an unbootable drive to view and disable malicious startup items preventing boot.
* **Disable vs Delete:** Unchecking a box disables the startup item (safe, easily reversible). Right-clicking and deleting removes the registry key permanently.

## 4. PsExec (psexec.exe)

**Run a remote Command Prompt:**

```powershell
psexec `
  \\RemotePCName `
  -s `
  cmd.exe
```

**Run a command as the local SYSTEM account:**

```powershell
psexec `
  -i `
  -s `
  regedit.exe
```

**Execute a script across multiple machines:**

```powershell
psexec `
  @C:\computers.txt `
  -c `
  install.bat
```

*(Note: PsExec requires File and Printer Sharing, Admin$ share access, and RPC on the target machine).*

## 5. TCPView (tcpview.exe)

* **Identify rogue connections:** Shows exactly which process owns which network connection, its local/remote port, and the remote IP address.
* **Kill connections instantly:** Right-click any established connection and select **Close Connection** to sever the network link without killing the underlying process.
* **Whois integration:** Right-click a remote address and select **Whois** to immediately query the IP ownership.

---
## Sources & Verification
* **Windows Sysinternals:** Tool features and parameters verified against Microsoft Learn official Sysinternals documentation (https://learn.microsoft.com/en-us/sysinternals/). PsExec remote execution syntax confirmed valid.
