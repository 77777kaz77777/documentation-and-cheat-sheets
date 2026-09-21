## Fedora SELinux Management & Context Resolution Cheat Sheet

Security-Enhanced Linux (SELinux) is a mandatory access control (MAC) security mechanism provided in the kernel. In Fedora and RHEL-based systems, it is enabled by default and operates primarily by labeling files, processes, and ports with a "context" and enforcing rules on how they interact.

## 1. State & Mode Management

| Action | Command |
| :--- | :--- |
| **Check Full SELinux Status** | `sestatus` |
| **Check Current Mode** | `getenforce` |
| **Set Mode Temporarily (Enforcing)** | `sudo setenforce 1` (Blocks policy violations) |
| **Set Mode Temporarily (Permissive)** | `sudo setenforce 0` (Logs violations but does not block them) |

> **Permanent Mode Configuration:**
> To permanently change the SELinux mode across reboots, you must edit `/etc/selinux/config` and change the `SELINUX=` directive to `enforcing`, `permissive`, or `disabled`. (Note: Disabling SELinux entirely is highly discouraged).

## 2. Viewing Security Contexts (Labels)

SELinux contexts are typically displayed in the format: `user:role:type:level`. The **type** (e.g., `httpd_sys_content_t`) is the most important part for standard administration.

| Target | Command |
| :--- | :--- |
| **View File/Directory Contexts** | `ls -lZ /path/to/dir` |
| **View Process Contexts** | `ps -Z` or `ps -eZ` |
| **View Current User Context** | `id -Z` |
| **View Port Contexts** | `sudo semanage port -l` |

## 3. Modifying File Contexts

### Temporary Changes (`chcon`)

Changes made with `chcon` will be lost the next time the filesystem is relabeled or `restorecon` is run.

```bash
# Temporarily change the type context of a file
sudo chcon -t httpd_sys_content_t /var/www/html/index.html
```

### Permanent Changes (`semanage fcontext` & `restorecon`)

To permanently define the default context for a directory and ensure the labels survive reboots and relabeling operations.

```bash
# 1. Add a rule to the SELinux policy (Regex specifies the directory and all contents)
sudo semanage fcontext -a -t virt_image_t "/mnt/storage/vms(/.*)?"

# 2. Traverse the directory recursively (-R) and apply the newly defined policy (-v for verbose)
sudo restorecon -Rv /mnt/storage/vms
```

## 4. SELinux Booleans

Booleans are on/off switches that allow you to modify SELinux policy behavior on the fly without having to write custom policy modules.

| Action | Command |
| :--- | :--- |
| **List All Booleans & Current State** | `getsebool -a` |
| **List Booleans with Descriptions** | `sudo semanage boolean -l` |
| **Change a Boolean Temporarily** | `sudo setsebool httpd_can_network_connect on` |
| **Change a Boolean Permanently (-P)** | `sudo setsebool -P httpd_can_network_connect on` |

## 5. Troubleshooting & Audit Logs

When a daemon or process is denied access, SELinux logs an AVC (Access Vector Cache) denial.

### Finding the Denials

```bash
# View recent SELinux denials in the audit log
sudo ausearch -m avc -ts recent

# If auditd is not running, denials may be in the system journal
sudo journalctl -t setroubleshoot
```

### Analyzing Denials with `sealert`

`sealert` translates cryptic audit logs into human-readable explanations and suggests fixes.

```bash
# Analyze the entire audit log and generate suggestions
sudo sealert -a /var/log/audit/audit.log
```

### Generating Custom Policy Modules (`audit2allow`)

If you are running a custom application and need to allow it to bypass a restriction, you can compile a custom policy module based on the denial logs.

```bash
# 1. Pipe the denial log into audit2allow to create a custom policy module named 'mypol'
grep my_custom_app /var/log/audit/audit.log | audit2allow -M mypol

# 2. Install the newly generated policy package (.pp file)
sudo semodule -i mypol.pp
```

## 6. Common Context Types Reference

* `httpd_sys_content_t`: Standard read-only web server content.
* `httpd_sys_rw_content_t`: Web server content that the web daemon needs to write to (e.g., upload directories).
* `public_content_t`: Read-only files shared via FTP, Samba, or Apache.
* `public_content_rw_t`: Read/write files shared via FTP, Samba, or Apache.
* `virt_image_t`: Disk image files used by KVM/libvirt.
* `container_file_t`: Files and directories mapped into Podman/Docker containers.
