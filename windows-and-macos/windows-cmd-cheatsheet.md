## A quick-reference cheat sheet for Windows Command Prompt (CMD) and PowerShell, covering file navigation, system management, and package provisioning

## File and System Navigation

**`List Files` — dir:**

```powershell
`ls` or `dir`
```

**`Change Directory` — cd [folder]:**

```powershell
cd [folder]
```

**`Make Directory` — mkdir [name]:**

```powershell
`mkdir` or `md`
```

**`Move/Rename` — move [src] [dest]:**

```powershell
`mv` or `Move-Item`
```

**`Copy File` — copy [src] [dest]:**

```powershell
`cp` or `Copy-Item`
```

**`Delete File` — del [file]:**

```powershell
`rm` or `Remove-Item`
```

**`Clear Screen` — cls:**

```powershell
`clear` or `cls`
```

**`Show File Content` — type [file]:**

```powershell
`cat` or `Get-Content`
```

**`Check IP Address` — ipconfig:**

```powershell
Get-NetIPAddress
```

## System & Networking

**`List Services` — sc query:**

```powershell
Get-Service
```

**`Stop Service` — net stop [name]:**

```powershell
Stop-Service [name]
```

**`List Running Apps` — tasklist:**

```powershell
Get-Process
```

**`Kill a Process` — taskkill /F /IM [app].exe:**

```powershell
Stop-Process -Name [app]
```

**`Check Network Path` — tracert [url]:**

```powershell
Test-NetConnection [url]
```

**`Environment Vars` — set:**

```powershell
Get-ChildItem Env:
```

## Package Management (Winget)

- **Search for an app:** `winget search [app_name]`
- **Install an app:** `winget install [app_name]`
- **Update all apps:** `winget upgrade --all`
- **Uninstall an app:** `winget uninstall [app_name]`

## Command Line Tips

- **Administrator Access:** Many system commands require running the terminal as an Administrator. Right-click the Start button and select **Terminal (Admin)**.
- **PowerShell Aliases:** PowerShell includes built-in aliases (like `ls` and `rm`) for faster navigation.
- **The Pipeline:** Unlike CMD which passes raw text, PowerShell passes structured objects between commands, allowing for advanced data filtering and manipulation.
