# Hyper-V PowerShell Management Cheat Sheet

*Note: Ensure you run these in a PowerShell window with **Administrator** privileges.*

##  Hyper-V VM Management
| Action | PowerShell Command |
| :--- | :--- |
| **List All VMs** | `Get-VM` |
| **Start a VM** | `Start-VM -Name "[VMName]"` |
| **Stop a VM (Shut down)** | `Stop-VM -Name "[VMName]"` |
| **Turn Off (Hard Reset)** | `Stop-VM -Name "[VMName]" -TurnOff` |
| **Restart a VM** | `Restart-VM -Name "[VMName]"` |
| **Suspend (Pause) VM** | `Suspend-VM -Name "[VMName]"` |
| **Resume VM** | `Resume-VM -Name "[VMName]"` |
| **Rename a VM** | `Rename-VM -Name "[Old]" -NewName "[New]"` |
| **Remove/Delete VM** | `Remove-VM -Name "[VMName]"` |

## 🛠️ Configuration & Hardware
| Action | PowerShell Command |
| :--- | :--- |
| **Show VM Settings** | `Get-VM -Name "[VMName]"` |
| **Set Memory (Static)** | `Set-VMMemory -VMName "[VMName]" -StartupBytes 4GB` |
| **Set CPU Count** | `Set-VMProcessor "[VMName]" -Count 4` |
| **Enable Dynamic Mem** | `Set-VMMemory "[VMName]" -DynamicMemoryEnabled $true` |
| **List Network Adapters** | `Get-VMNetworkAdapter -VMName "[VMName]"` |
| **Connect ISO/DVD** | `Set-VMDvdDrive -VMName "[VMName]" -Path "C:\image.iso"` |

## 📸 Snapshots (Checkpoints)
| Action | PowerShell Command |
| :--- | :--- |
| **Create Checkpoint** | `Checkpoint-VM -Name "[VMName]" -SnapshotName "[Label]"` |
| **List Checkpoints** | `Get-VMSnapshot -VMName "[VMName]"` |
| **Apply Checkpoint** | `Restore-VMSnapshot -Name "[Label]" -VMName "[VMName]"` |
| **Delete Checkpoint** | `Remove-VMSnapshot -Name "[Label]" -VMName "[VMName]"` |

##  Virtual Networking (V-Switches)
| Action | PowerShell Command |
| :--- | :--- |
| **List All Switches** | `Get-VMSwitch` |
| **Create External Switch** | `New-VMSwitch -Name "ExtSwitch" -NetAdapterName "Ethernet" -AllowManagementOS $true` |
| **Create Private Switch** | `New-VMSwitch -Name "PrivateNet" -SwitchType Private` |
| **Connect VM to Switch** | `Connect-VMNetworkAdapter -VMName "[VMName]" -SwitchName "[SwitchName]"` |

## Virtual Disks (VHD/VHDX)
| Action | PowerShell Command |
| :--- | :--- |
| **Create New Disk** | `New-VHD -Path "C:\VMs\disk.vhdx" -SizeBytes 50GB -Dynamic` |
| **Mount VHD to Host** | `Mount-VHD -Path "C:\VMs\disk.vhdx"` |
| **Expand Disk Size** | `Resize-VHD -Path "C:\VMs\disk.vhdx" -SizeBytes 100GB` |
| **Get Disk Info** | `Get-VHD -Path "C:\VMs\disk.vhdx"` |

## 🔍 Quick Diagnostics
* **Is Hyper-V enabled?** `Get-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V`
* **Check VM Uptime:** `Get-VM | Select Name, State, Uptime`
* **Expose Virtualization (Nested VT):** If you want to run Proxmox or Docker *inside* a Hyper-V VM, run: `Set-VMProcessor -VMName "[VMName]" -ExposeVirtualizationExtensions $true`
