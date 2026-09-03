# Quick commands for managing network rules using Firewalld on Fedora

Fedora uses **firewalld** by default for packet filtering, managed via the `firewall-cmd` utility.

| Action | Command |
| :--- | :--- |
| **Check Firewall Status** | `sudo firewall-cmd --state` |
| **List All Active Settings** | `sudo firewall-cmd --list-all` |
| **Reload Rules (Without Dropping Connections)** | `sudo firewall-cmd --reload` |
| **Allow a Service Temporarily** | `sudo firewall-cmd --service=http` |
| **Allow a Service Permanently** | `sudo firewall-cmd --permanent --add-service=http` |
| **Open a Port (TCP/UDP) Permanently** | `sudo firewall-cmd --permanent --add-port=80/tcp` |
| **Remove a Port Permanently** | `sudo firewall-cmd --permanent --remove-port=80/tcp` |
| **List Open Ports/Services** | `sudo firewall-cmd --list-ports` / `sudo firewall-cmd --list-services` |
| **Change Default Zone** | `sudo firewall-cmd --set-default-zone=public` |
