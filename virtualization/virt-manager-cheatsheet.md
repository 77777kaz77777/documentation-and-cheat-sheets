## Virt-Manager & Virsh Command Line Cheat Sheet

Virt-Manager is a graphical desktop user interface for managing virtual machines through libvirt. Below are the common GUI actions and their underlying `virsh` and `virt-*` command-line equivalents for headless management and automation.

### **Virtual Machine Management (`virsh`)**

| Action | GUI Equivalent | CLI Command (`virsh`) |
| :--- | :--- | :--- |
| **List Running VMs** | Main Window | `virsh list` |
| **List All VMs (Running & Stopped)** | Main Window | `virsh list --all` |
| **Start a VM** | Right-click -> Run | `virsh start [vm_name]` |
| **Shutdown a VM (Graceful)** | Right-click -> Shut Down | `virsh shutdown [vm_name]` |
| **Force Stop a VM (Power Off)** | Right-click -> Force Off | `virsh destroy [vm_name]` |
| **Restart a VM** | Right-click -> Reboot | `virsh reboot [vm_name]` |
| **Save VM State to Disk** | Right-click -> Save | `virsh save [vm_name] [path_to_file]` |
| **Restore Saved VM State** | File -> Restore Saved State | `virsh restore [path_to_file]` |
| **Delete/Undefine a VM** | Right-click -> Delete | `virsh undefine [vm_name]` |

### **Inspection & Configuration**

| Action | CLI Command |
| :--- | :--- |
| **View VM Details / XML Config** | `virsh dumpxml [vm_name]` |
| **Edit VM XML Configuration** | `virsh edit [vm_name]` |
| **Check VM Info & Resource Allocation** | `virsh dominfo [vm_name]` |
| **Display Active Network Interfaces** | `virsh domiflist [vm_name]` |
| **Display Disk Storage Mappings** | `virsh domblklist [vm_name]` |

### **Snapshots (`virsh snapshot`)**

*Virt-Manager provides a graphical Snapshot GUI under the lightbulb icon in the VM details window.*

| Action | CLI Command |
| :--- | :--- |
| **Create a Snapshot** | `virsh snapshot-create-as [vm_name] [snap_name] --description "[desc]"` |
| **List All Snapshots for a VM** | `virsh snapshot-list [vm_name]` |
| **Revert to a Snapshot** | `virsh snapshot-revert [vm_name] [snap_name]` |
| **Delete a Snapshot** | `virsh snapshot-delete [vm_name] [snap_name]` |

### **Storage & Networks (`virsh pool-` / `net-`)**

| Action | CLI Command |
| :--- | :--- |
| **List Storage Pools** | `virsh pool-list --all` |
| **Start/Activate a Storage Pool** | `virsh pool-start [pool_name]` |
| **List Virtual Networks** | `virsh net-list --all` |
| **Start a Virtual Network (e.g., default)** | `virsh net-start default` |
| **Auto-start Network on Boot** | `virsh net-autostart default` |

### **Creating VMs (`virt-install`)**

*While Virt-Manager uses an interactive wizard to create VMs, you can achieve the exact same backend setup via the terminal.*

* **Quick Install Example:**

  ```bash
  virt-install \
    --name [vm_name] \
    --memory 4096 \
    --vcpus 2 \
    --disk size=20,pool=default \
    --os-variant ubuntu24.04 \
    --cdrom /path/to/install.iso \
    --network network=default
