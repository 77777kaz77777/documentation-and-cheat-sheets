## PowerShell commands to spin up and manage Hyper-V virtual machines

# Hyper-V PowerShell Management Cheat Sheet

_Note: Ensure you run these in a PowerShell window with **Administrator** privileges._

## Hyper-V VM Management

**List All VMs:**
```powershell
Get-VM
```

**Start a VM:**
```powershell
Start-VM -Name "[VMName]"
```

**Stop a VM (Shut down):**
```powershell
Stop-VM -Name "[VMName]"
```

**Turn Off (Hard Reset):**
```powershell
Stop-VM -Name "[VMName]" -TurnOff
```

**Restart a VM:**
```powershell
Restart-VM -Name "[VMName]"
```

**Suspend (Pause) VM:**
```powershell
Suspend-VM -Name "[VMName]"
```

**Resume VM:**
```powershell
Resume-VM -Name "[VMName]"
```

**Rename a VM:**
```powershell
Rename-VM -Name "[Old]" -NewName "[New]"
```

**Remove/Delete VM:**
```powershell
Remove-VM -Name "[VMName]"
```

## Configuration & Hardware

**Show VM Settings:**
```powershell
Get-VM -Name "[VMName]"
```

**Set Memory (Static):**
```powershell
Set-VMMemory -VMName "[VMName]" -StartupBytes 4GB
```

**Set CPU Count:**
```powershell
Set-VMProcessor "[VMName]" -Count 4
```

**Enable Dynamic Mem:**
```powershell
Set-VMMemory "[VMName]" -DynamicMemoryEnabled $true
```

**List Network Adapters:**
```powershell
Get-VMNetworkAdapter -VMName "[VMName]"
```

**Connect ISO/DVD:**
```powershell
Set-VMDvdDrive -VMName "[VMName]" -Path "C:\image.iso"
```

## Snapshots (Checkpoints)

**Create Checkpoint:**
```powershell
Checkpoint-VM -Name "[VMName]" -SnapshotName "[Label]"
```

**List Checkpoints:**
```powershell
Get-VMSnapshot -VMName "[VMName]"
```

**Apply Checkpoint:**
```powershell
Restore-VMSnapshot -Name "[Label]" -VMName "[VMName]"
```

**Delete Checkpoint:**
```powershell
Remove-VMSnapshot -Name "[Label]" -VMName "[VMName]"
```

## Virtual Networking (V-Switches)

**List All Switches:**
```powershell
Get-VMSwitch
```

**Create External Switch:**
```powershell
New-VMSwitch -Name "ExtSwitch" -NetAdapterName "Ethernet" -AllowManagementOS $true
```

**Create Private Switch:**
```powershell
New-VMSwitch -Name "PrivateNet" -SwitchType Private
```

**Connect VM to Switch:**
```powershell
Connect-VMNetworkAdapter -VMName "[VMName]" -SwitchName "[SwitchName]"
```

## Virtual Disks (VHD/VHDX)

**Create New Disk:**
```powershell
New-VHD -Path "C:\VMs\disk.vhdx" -SizeBytes 50GB -Dynamic
```

**Mount VHD to Host:**
```powershell
Mount-VHD -Path "C:\VMs\disk.vhdx"
```

**Expand Disk Size:**
```powershell
Resize-VHD -Path "C:\VMs\disk.vhdx" -SizeBytes 100GB
```

**Get Disk Info:**
```powershell
Get-VHD -Path "C:\VMs\disk.vhdx"
```

## Quick Diagnostics

- **Is Hyper-V enabled?** `Get-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V`
- **Check VM Uptime:** `Get-VM | Select Name, State, Uptime`
- **Expose Virtualization (Nested VT):** If you want to run Proxmox or Docker _inside_ a Hyper-V VM, run: `Set-VMProcessor -VMName "[VMName]" -ExposeVirtualizationExtensions $true`
