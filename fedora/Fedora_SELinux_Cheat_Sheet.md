# Everyday commands for fixing and managing SELinux policies on Fedora.


Fedora runs Security-Enhanced Linux (SELinux) in **Enforcing** mode by default for mandatory access control.

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
