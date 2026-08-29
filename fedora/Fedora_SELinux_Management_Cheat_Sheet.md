## Fedora SELinux Management & Context Resolution Cheat Sheet

| Action | Command |
| :--- | :--- |
| **Check SELinux Status** | `sestatus` |
| **Check Current Mode** | `getenforce` |
| **Set Mode Temporarily (Enforcing)** | `sudo setenforce 1` |
| **Set Mode Temporarily (Permissive)** | `sudo setenforce 0` |
| **List SELinux Booleans** | `getsebool -a` |
| **Change a Boolean Permanently** | `sudo setsebool -P [boolean_name] on` |
| **View SELinux Audit Logs** | `sudo ausearch -m avc -ts recent` |
| **Restore Default File Security Contexts** | `sudo restorecon -Rv /path/to/directory` |
| **Generate Policy Fix from Logs** | `sudo sealert -a /var/log/audit/audit.log` |

### Tracking Down and Fixing Context Denials
If a daemon (like `rpc-virtqemud`) denies access to a file because it requires a specific SELinux context (e.g., `virt_image_t`), you must permanently define the default context for the directory and restore the labels.

```bash
sudo semanage fcontext -a -t virt_image_t "/mnt/storage/vms(/.*)?"
sudo restorecon -R -v /mnt/storage/vms
```

**Command Breakdown:**
* `semanage fcontext`: Permanently adds a rule to the SELinux policy, ensuring any file created in the target directory automatically receives the defined label.
* `restorecon`: Traverses the directory recursively (`-R`) and applies the newly defined policy to any existing files, outputting the changes (`-v`).