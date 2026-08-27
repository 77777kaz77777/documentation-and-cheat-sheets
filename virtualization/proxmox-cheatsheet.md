this Proxmox VE (Virtual Environment) cheatsheet is divided into the two main command sets: qm for Virtual Machines (QEMU/KVM) and pct for Containers (LXC).
## ** Proxmox Virtual Machine Commands (qm)**
These commands manage full virtual machines. Replace [vmid] with the numerical ID of your VM (e.g., 100).
|  |  |
| :- | :- |
| Action | Command |
| **List All VMs** | qm list |
| **Start VM** | qm start [vmid] |
| **Stop VM (Graceful)** | qm shutdown [vmid] |
| **Stop VM (Immediate)** | qm stop [vmid] |
| **Reset VM** | qm reset [vmid] |
| **Clone VM** | qm clone [vmid] [newid] --name [name] |
| **Remove VM** | qm destroy [vmid] |
| **Unlock VM** | qm unlock [vmid] (Used if a task hangs) |
| **Show Config** | qm config [vmid] |
| **Terminal Proxy** | qm terminal [vmid] |

## ** Proxmox Container Commands (pct)**
These are specific to the LXC containers running on your Proxmox host.
|  |  |
| :- | :- |
| Action | Command |
| **List All Containers** | pct list |
| **Start Container** | pct start [vmid] |
| **Stop Container** | pct stop [vmid] |
| **Enter Shell** | pct enter [vmid] |
| **Execute Command** | pct exec [vmid] -- [command] |
| **Show Config** | pct config [vmid] |
| **Clone Container** | pct clone [vmid] [newid] --hostname [name] |
| **Mount CT Disk** | pct mount [vmid] |
| **Unmount CT Disk** | pct unmount [vmid] |

## ** Storage & Backup (vzdump/pvesm)**
Proxmox uses vzdump for backups and pvesm for storage management.
|  |  |
| :- | :- |
| Action | Command |
| **Backup VM/CT** | vzdump [vmid] --storage [storage_name] --compress lzo |
| **Restore VM** | qmrestore [backup_file] [vmid] |
| **Restore Container** | pct restore [vmid] [backup_file] |
| **List Storage Pools** | pvesm status |
| **List Content in Pool** | pvesm list [storage_name] |
| **Free Up Space** | pvesm free [storage_name]:[volume] |

## ** Cluster & System Management**
Use these for node-level operations and health checks.
|  |  |
| :- | :- |
| Action | Command |
| **Cluster Status** | pvecm status |
| **Check Services** | systemctl status pve-cluster |
| **Update Node Repos** | apt update |
| **Update Proxmox** | apt dist-upgrade |
| **View Task Logs** | cat /var/log/pve/tasks/index |
| **Restart Web GUI** | systemctl restart pveproxy |

## ** Common Troubleshooting**
  - **Fix "No Subscription" Error:** If you are using the free version, you often need to disable the enterprise repo in /etc/apt/sources.list.d/pve-enterprise.list.
  - **Zombie Locks:** If a VM is stuck in a "locked" state after a failed backup, use qm unlock [vmid].
  - **High CPU/Load:** Use htop (you may need to install it with apt install htop) to see which process is eating resources on the host.
Would you like me to include the **Port Reference** I mentioned earlier (listing the default ports for Proxmox, SSH, Web GUIs, etc.)?
