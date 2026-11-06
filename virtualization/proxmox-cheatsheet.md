## Proxmox Virtual Machine Commands (qm) Cheat Sheet

this Proxmox VE (Virtual Environment) cheatsheet is divided into the two main command sets: qm for Virtual Machines (QEMU/KVM) and pct for Containers (LXC).
These commands manage full virtual machines. Replace [vmid] with the numerical ID of your VM (e.g., 100).

**List All VMs:**

```bash
qm list
```

**Start VM:**

```bash
qm start [vmid]
```

**Stop VM (Graceful):**

```bash
qm shutdown [vmid]
```

**Stop VM (Immediate):**

```bash
qm stop [vmid]
```

**Reset VM:**

```bash
qm reset [vmid]
```

**Clone VM:**

```bash
qm clone [vmid] [newid] --name [name]
```

**Remove VM:**

```bash
qm destroy [vmid]
```

**Unlock VM:**

```bash
qm unlock [vmid] (Used if a task hangs)
```

**Show Config:**

```bash
qm config [vmid]
```

**Terminal Proxy:**

```bash
qm terminal [vmid]
```

## **Proxmox Container Commands (pct)**

These are specific to the LXC containers running on your Proxmox host.

**List All Containers:**

```bash
pct list
```

**Start Container:**

```bash
pct start [vmid]
```

**Stop Container:**

```bash
pct stop [vmid]
```

**Enter Shell:**

```bash
pct enter [vmid]
```

**Execute Command:**

```bash
pct exec [vmid] -- [command]
```

**Show Config:**

```bash
pct config [vmid]
```

**Clone Container:**

```bash
pct clone [vmid] [newid] --hostname [name]
```

**Mount CT Disk:**

```bash
pct mount [vmid]
```

**Unmount CT Disk:**

```bash
pct unmount [vmid]
```

## **Storage & Backup (vzdump/pvesm)**

Proxmox uses vzdump for backups and pvesm for storage management.

**Backup VM/CT:**

```bash
vzdump [vmid] --storage [storage_name] --compress lzo
```

**Restore VM:**

```bash
qmrestore [backup_file] [vmid]
```

**Restore Container:**

```bash
pct restore [vmid] [backup_file]
```

**List Storage Pools:**

```bash
pvesm status
```

**List Content in Pool:**

```bash
pvesm list [storage_name]
```

**Free Up Space:**

```bash
pvesm free [storage_name]:[volume]
```

## **Cluster & System Management**

Use these for node-level operations and health checks.

**Cluster Status:**

```bash
pvecm status
```

**Check Services:**

```bash
systemctl status pve-cluster
```

**Update Node Repos:**

```bash
apt update
```

**Update Proxmox:**

```bash
apt dist-upgrade
```

**View Task Logs:**

```bash
cat /var/log/pve/tasks/index
```

**Restart Web GUI:**

```bash
systemctl restart pveproxy
```

## **Common Troubleshooting**

- **Fix "No Subscription" Error:** If you are using the free version, you often need to disable the enterprise repo in /etc/apt/sources.list.d/pve-enterprise.list.
- **Zombie Locks:** If a VM is stuck in a "locked" state after a failed backup, use qm unlock [vmid].
- **High CPU/Load:** Use htop (you may need to install it with apt install htop) to see which process is eating resources on the host.
  Would you like me to include the **Port Reference** I mentioned earlier (listing the default ports for Proxmox, SSH, Web GUIs, etc.)?
