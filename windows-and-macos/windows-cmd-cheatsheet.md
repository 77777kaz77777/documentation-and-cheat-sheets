## A quick-reference cheat sheet for Windows Command Prompt (CMD) and PowerShell, covering file navigation, system management, and package provisioning.

## File and System Navigation
| Action | CMD (Command Prompt) | PowerShell |
| :--- | :--- | :--- |
| **List Files** | `dir` | `ls` or `dir` |
| **Change Directory** | `cd [folder]` | `cd [folder]` |
| **Make Directory** | `mkdir [name]` | `mkdir` or `md` |
| **Move/Rename** | `move [src] [dest]` | `mv` or `Move-Item` |
| **Copy File** | `copy [src] [dest]` | `cp` or `Copy-Item` |
| **Delete File** | `del [file]` | `rm` or `Remove-Item` |
| **Clear Screen** | `cls` | `clear` or `cls` |
| **Show File Content** | `type [file]` | `cat` or `Get-Content` |
| **Check IP Address** | `ipconfig` | `Get-NetIPAddress` |

## System & Networking
| Action | CMD | PowerShell |
| :--- | :--- | :--- |
| **List Services** | `sc query` | `Get-Service` |
| **Stop Service** | `net stop [name]` | `Stop-Service [name]` |
| **List Running Apps** | `tasklist` | `Get-Process` |
| **Kill a Process** | `taskkill /F /IM [app].exe` | `Stop-Process -Name [app]` |
| **Check Network Path** | `tracert [url]` | `Test-NetConnection [url]` |
| **Environment Vars** | `set` | `Get-ChildItem Env:` |

## Package Management (Winget)
* **Search for an app:** `winget search [app_name]`
* **Install an app:** `winget install [app_name]`
* **Update all apps:** `winget upgrade --all`
* **Uninstall an app:** `winget uninstall [app_name]`

## Command Line Tips
* **Administrator Access:** Many system commands require running the terminal as an Administrator. Right-click the Start button and select **Terminal (Admin)**.
* **PowerShell Aliases:** PowerShell includes built-in aliases (like `ls` and `rm`) for faster navigation.
* **The Pipeline:** Unlike CMD which passes raw text, PowerShell passes structured objects between commands, allowing for advanced data filtering and manipulation.
