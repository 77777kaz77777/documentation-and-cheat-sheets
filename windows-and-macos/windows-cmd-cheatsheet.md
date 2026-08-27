Moving from Linux to Windows can feel like learning a new dialect. While **CMD** is the "old guard" (legacy), **PowerShell** is the modern, object-oriented powerhouse that actually shares many aliases with Linux.
## ** Windows Command Line Comparison**
This table covers the most common file and system navigation tasks.
|  |  |  |  |
| :- | :- | :- | :- |
| Action | CMD (Command Prompt) | PowerShell | Linux (Reference) |
| **List Files** | dir | ls or dir | ls |
| **Change Directory** | cd [folder] | cd [folder] | cd |
| **Make Directory** | mkdir [name] | mkdir or md | mkdir |
| **Move/Rename** | move [src] [dest] | mv or Move-Item | mv |
| **Copy File** | copy [src] [dest] | cp or Copy-Item | cp |
| **Delete File** | del [file] | rm or Remove-Item | rm |
| **Clear Screen** | cls | clear or cls | clear |
| **Show File Content** | type [file] | cat or Get-Content | cat |
| **Check IP Address** | ipconfig | Get-NetIPAddress | ip addr |

## ** System & Networking**
In PowerShell, most commands follow a **Verb-Noun** structure (e.g., Get-Service), which makes them very predictable once you learn the pattern.
|  |  |  |
| :- | :- | :- |
| Action | CMD | PowerShell |
| **List Services** | sc query | Get-Service |
| **Stop Service** | net stop [name] | Stop-Service [name] |
| **List Running Apps** | tasklist | Get-Process |
| **Kill a Process** | taskkill /F /IM [app].exe | Stop-Process -Name [app] |
| **Check Network Path** | tracert [url] | Test-NetConnection [url] |
| **Environment Vars** | set | Get-ChildItem Env: |

## ** Package Management (Winget)**
Windows now has a built-in package manager called **Winget**. It works similarly to apt or dnf and is available in both CMD and PowerShell.
  - **Search for an app:** winget search [app_name]
  - **Install an app:** winget install [app_name]
  - **Update all apps:** winget upgrade --all
  - **Uninstall an app:** winget uninstall [app_name]
## ** Pro Tips for your Google Doc**
  - **Administrator Access:** Many commands (like net stop or winget install) require you to run the terminal as an Administrator. Right-click the Start button and select **Terminal (Admin)**.
  - **PowerShell Aliases:** PowerShell is designed to be friendly to Linux users. It has "aliases" built-in, so ls, rm, and pwd work exactly as you’d expect without you needing to learn the long-form Windows commands immediately.
  - **The Pipeline:** In PowerShell, you aren't just passing text between commands like in Linux; you are passing **objects**. This allows for much more powerful data filtering.
**Ready to paste?** When you bring this into your Google Doc, the tables will remain editable so you can add your own notes or frequently used server paths.
Would you like me to add a section on **Windows Registry** commands or **Active Directory** management for PowerShell?
