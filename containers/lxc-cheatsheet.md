## quick-reference CLI guide for managing LXC/LXD system containers

# LXC_LXD_CLI_Cheat_Sheet.md

## 🚀 Container Lifecycle

Most modern implementations use the `lxc` command-line tool (part of the LXD project).

**List Containers:**

```bash
lxc list
```

**Launch New Container:**

```bash
lxc launch images:[distro]/[version] [name]
```

**Example (Ubuntu):**

```bash
lxc launch images:ubuntu/24.04 my-ubuntu
```

**Start Container:**

```bash
lxc start [name]
```

**Stop Container:**

```bash
lxc stop [name]
```

**Restart Container:**

```bash
lxc restart [name]
```

**Delete Container:**

```bash
lxc delete [name] --force
```

**Show Container Info:**

```bash
lxc info [name]
```

## 🛠️ Access & Configuration

Interacting with the "inside" of an LXC container is very similar to interacting with a virtual machine.

**Open Shell (Root):**

```bash
lxc exec [name] -- /bin/bash
```

**Run Single Command:**

```bash
lxc exec [name] -- apt update
```

**Copy File TO Container:**

```bash
lxc file push [local_path] [name]/[remote_path]
```

**Pull File FROM Container:**

```bash
lxc file pull [name]/[remote_path] [local_path]
```

**Edit Config:**

```bash
lxc config edit [name]
```

**Set Resource Limit:**

```bash
lxc config set [name] limits.cpu 2
```

## 📸 Snapshots & Images

One of the best features of LXC is the ability to "freeze" a state before making risky changes.

**Create Snapshot:**

```bash
lxc snapshot [name] [snap_name]
```

**Restore Snapshot:**

```bash
lxc restore [name] [snap_name]
```

**List Snapshots:**

```bash
`lxc info [name]` _(Look under the Snapshots section)_
```

**Delete Snapshot:**

```bash
lxc delete [name]/[snap_name]
```

**Publish as Image:**

```bash
lxc publish [name]/[snap_name] --alias [my-custom-image]
```

## 🌐 Network & Storage

**List Networks:**

```bash
lxc network list
```

**Show Network Details:**

```bash
lxc network show [bridge_name]
```

**List Storage Pools:**

```bash
lxc storage list
```

**Create Managed Volume:**

```bash
lxc storage volume create [pool] [volume_name]
```
