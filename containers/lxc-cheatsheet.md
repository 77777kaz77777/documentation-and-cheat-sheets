## LXC/LXD Essentials Cheat Sheet 

Most modern implementations use the lxc command-line tool (part of the LXD project).
|  |  |
| :- | :- |
| Action | Command |
| **List Containers** | lxc list |
| **Launch New Container** | lxc launch images:[distro]/[version] [name] |
| **Example (Ubuntu)** | lxc launch images:ubuntu/24.04 my-ubuntu |
| **Start Container** | lxc start [name] |
| **Stop Container** | lxc stop [name] |
| **Restart Container** | lxc restart [name] |
| **Delete Container** | lxc delete [name] --force |
| **Show Container Info** | lxc info [name] |

## **🛠️ Access & Configuration**
Interacting with the "inside" of an LXC container is very similar to interacting with a virtual machine.
|  |  |
| :- | :- |
| Action | Command |
| **Open Shell (Root)** | lxc exec [name] -- /bin/bash |
| **Run Single Command** | lxc exec [name] -- apt update |
| **Copy File TO Container** | lxc file push [local_path] [name]/[remote_path] |
| **Pull File FROM Container** | lxc file pull [name]/[remote_path] [local_path] |
| **Edit Config** | lxc config edit [name] |
| **Set Resource Limit** | lxc config set [name] limits.cpu 2 |

## **📸 Snapshots & Images**
One of the best features of LXC is the ability to "freeze" a state before making risky changes.
  - **Create Snapshot:** lxc snapshot [name] [snap_name]
  - **Restore Snapshot:** lxc restore [name] [snap_name]
  - **List Snapshots:** lxc info [name] (Look under the Snapshots section)
  - **Delete Snapshot:** lxc delete [name]/[snap_name]
  - **Publish as Image:** lxc publish [name]/[snap_name] --alias [my-custom-image]
## **🌐 Network & Storage**
|  |  |
| :- | :- |
| Action | Command |
| **List Networks** | lxc network list |
| **Show Network Details** | lxc network show [bridge_name] |
| **List Storage Pools** | lxc storage list |
| **Create Managed Volume** | lxc storage volume create [pool] [volume_name] |

### **Comparison Note**
  - **Docker:** Temporary, ephemeral, application-centric.
  - **LXC/LXD:** Persistent, stateful, machine-centric (it has its own init, ssh, cron, etc.).
Should we add a section for **Proxmox-specific LXC** commands (since many people use LXC through the Proxmox pct tool)?
