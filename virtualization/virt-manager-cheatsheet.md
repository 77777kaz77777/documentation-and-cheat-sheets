## Virt-Manager & Virsh Command Line Cheat Sheet

Virt-Manager is a graphical desktop user interface for managing virtual machines through libvirt. Below are the common GUI actions and their underlying `virsh` and `virt-*` command-line equivalents for headless management and automation.

### **Virtual Machine Management (`virsh`)**

**`List Running VMs` — Main Window:**

```bash
virsh list
```

**`List All VMs (Running & Stopped)` — Main Window:**

```bash
virsh list --all
```

**`Start a VM` — Right-click -> Run:**

```bash
virsh start [vm_name]
```

**`Shutdown a VM (Graceful)` — Right-click -> Shut Down:**

```bash
virsh shutdown [vm_name]
```

**`Force Stop a VM (Power Off)` — Right-click -> Force Off:**

```bash
virsh destroy [vm_name]
```

**`Restart a VM` — Right-click -> Reboot:**

```bash
virsh reboot [vm_name]
```

**`Save VM State to Disk` — Right-click -> Save:**

```bash
virsh save [vm_name] [path_to_file]
```

**`Restore Saved VM State` — File -> Restore Saved State:**

```bash
virsh restore [path_to_file]
```

**`Delete/Undefine a VM` — Right-click -> Delete:**

```bash
virsh undefine [vm_name]
```

### **Inspection & Configuration**

**View VM Details / XML Config:**

```bash
virsh dumpxml [vm_name]
```

**Edit VM XML Configuration:**

```bash
virsh edit [vm_name]
```

**Check VM Info & Resource Allocation:**

```bash
virsh dominfo [vm_name]
```

**Display Active Network Interfaces:**

```bash
virsh domiflist [vm_name]
```

**Display Disk Storage Mappings:**

```bash
virsh domblklist [vm_name]
```

### **Snapshots (`virsh snapshot`)**

_Virt-Manager provides a graphical Snapshot GUI under the lightbulb icon in the VM details window._

**Create a Snapshot:**

```bash
virsh snapshot-create-as [vm_name] [snap_name] --description "[desc]"
```

**List All Snapshots for a VM:**

```bash
virsh snapshot-list [vm_name]
```

**Revert to a Snapshot:**

```bash
virsh snapshot-revert [vm_name] [snap_name]
```

**Delete a Snapshot:**

```bash
virsh snapshot-delete [vm_name] [snap_name]
```

### **Storage & Networks (`virsh pool-` / `net-`)**

**List Storage Pools:**

```bash
virsh pool-list --all
```

**Start/Activate a Storage Pool:**

```bash
virsh pool-start [pool_name]
```

**List Virtual Networks:**

```bash
virsh net-list --all
```

**Start a Virtual Network (e.g., default):**

```bash
virsh net-start default
```

**Auto-start Network on Boot:**

```bash
virsh net-autostart default
```

### **Creating VMs (`virt-install`)**

_While Virt-Manager uses an interactive wizard to create VMs, you can achieve the exact same backend setup via the terminal._

- **Quick Install Example:**

  ```bash
  virt-install \
    --name [vm_name] \
    --memory 4096 \
    --vcpus 2 \
    --disk size=20,pool=default \
    --os-variant ubuntu24.04 \
    --cdrom /path/to/install.iso \
    --network network=default
  ```
