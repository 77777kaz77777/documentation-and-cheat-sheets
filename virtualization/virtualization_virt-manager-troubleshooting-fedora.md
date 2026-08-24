## Virt-Manager troubleshooting guide tailored for Fedora with notes for other distributions.


# Virt-Manager Troubleshooting: "No active connection" (Fedora Focus)

This guide outlines the steps to resolve the common "No active connection to install on" error in Virtual Machine Manager (Virt-Manager) specifically tailored for Fedora.

> **Disclaimer for Other Distributions:** While the core concepts of starting the virtualization daemon and assigning group permissions remain the same across Linux distributions, specific package managers, group names, or command syntax (such as `usermod` versus `adduser`) can vary. Adjust the commands accordingly if you are using Debian, Ubuntu, or other non-Fedora distributions.

## 1. Start and Enable the Libvirt Service

The background service required to run virtual machines might not be running. Run the following commands to start it and ensure it launches on boot:

```bash
sudo systemctl start libvirtd
sudo systemctl enable libvirtd
```

## 2. Check Your User Permissions

If you are logged in as a standard user, you might not have permission to access the socket without root privileges.

Add your user to the `libvirt` group using the Fedora-compatible command:

```bash
sudo usermod -aG libvirt $USER
```

*Note: You will need to log out and log back in (or reboot) for this group change to take effect.*

## 3. Manually Connect in Virt-Manager

If the service is running but disconnected in the application:

1. Open Virt-Manager and look at the main window behind this error popup.
2. Check if **QEMU/KVM** is listed and shows as "Not Connected".
3. Right-click on **QEMU/KVM** and select **Connect**.
4. If it isn't listed at all, go to **File > Add Connection**, select **QEMU/KVM** as the hypervisor, and click **Connect**.
