## A quick-reference guide for Windows PowerShell administration, covering Registry manipulation, Active Directory user and group management, remote networking, and object-oriented data filtering.

## **Windows PowerShell & Active Directory Essentials**
### ** Windows Registry Management**
In PowerShell, the Registry is treated like a file drive (HKLM: for HKEY_LOCAL_MACHINE and HKCU: for HKEY_CURRENT_USER).
|  |  |
| :- | :- |
| Action | PowerShell Command |
| **Go to Registry Key** | cd HKLM:\Software\Microsoft |
| **List Values in Key** | Get-ItemProperty -Path . |
| **Create New Key** | New-Item -Path .\MyNewKey |
| **Set/Change Value** | Set-ItemProperty -Path . -Name "Version" -Value "1.1" |
| **Get Specific Value** | Get-ItemProperty -Path . -Name "Version" |
| **Remove Key/Value** | Remove-ItemProperty or Remove-Item |

### ** Active Directory (AD) Management**
*Note: These require the RSAT (Remote Server Administration Tools) to be installed on your machine.*
|  |  |
| :- | :- |
| Action | PowerShell Command |
| **Get User Info** | Get-ADUser -Identity [username] -Properties * |
| **Create New User** | New-ADUser -Name "John Doe" -SamAccountName jdoe |
| **Unlock Account** | Unlock-ADAccount -Identity [username] |
| **Reset Password** | Set-ADAccountPassword -Identity [username] |
| **Add to Group** | Add-ADGroupMember -Identity [Group] -Members [User] |
| **List Group Members** | Get-ADGroupMember -Identity [GroupName] |
| **Find Computers** | Get-ADComputer -Filter 'Name -like "*Desktop*"' |

### ** Windows Networking & Remote Management**
PowerShell excels at managing remote Windows machines using **WinRM**.
  - **Enter a Remote Session:** Enter-PSSession -ComputerName [RemotePC] (Like SSH for Windows).
  - **Run Command Remotely:** Invoke-Command -ComputerName [RemotePC] -ScriptBlock { Get-Service }
  - **Test Network Port:** Test-NetConnection -ComputerName [IP] -Port 80 (A modern telnet replacement).
### ** Comparing CMD vs. PowerShell Objects**
The biggest hurdle is realizing that PowerShell doesn't just return text; it returns **Data Objects**.
  - **Linux/CMD style (Text):** You grep or find a string of text.
  - **PowerShell style (Objects):** You filter by properties.
  - *Example:* Get-Service | Where-Object {$_.Status -eq "Running"} only shows services that are actually started.
Would you like me to create a dedicated section for **Azure CLI** or **Microsoft 365** PowerShell commands to round out your cloud administration toolkit?
