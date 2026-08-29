## A breakdown of the 2026 Enterprise Linux landscape plus core admin commands.

## 1. Enterprise Linux Ecosystem Overview (Current as of August 2026)

The current Enterprise Linux ecosystem relies on a specific upstream and downstream relationship structure:

* **CentOS Stream:** Serves as the continuously delivered upstream public development branch for RHEL. The current active major branches are CentOS Stream 10 (tracking ahead of RHEL 10) and CentOS Stream 9.
* **Red Hat Enterprise Linux (RHEL):** The primary commercial enterprise release. The current latest flagship version is RHEL 10.2, released in May 2026, with full support extending to May 2030 and maintenance to May 2035. 
* **Rocky Linux:** A downstream, 100% bug-for-bug compatible community rebuild of RHEL. The current latest version is Rocky Linux 10.2, released in May 2026. 

## 2. The Difference Between Fedora and Enterprise Linux

Understanding where Fedora sits in the Red Hat ecosystem clarifies its use case compared to RHEL, CentOS Stream, and Rocky Linux:

* **Fedora Linux:** The extreme upstream source. Fedora is a community-driven, fast-paced distribution sponsored by Red Hat. It acts as the testing ground for new technologies before they reach the enterprise. It features aggressive update cycles with a new major release every 6 months and a short lifecycle of roughly 13 months per release. It prioritizes cutting-edge software, innovation, and daily desktop usage.
* **CentOS Stream:** The mid-stream development branch. Red Hat takes a snapshot of a specific Fedora release (e.g., Fedora 40 was branched to create CentOS Stream 10) and begins stabilizing it. CentOS Stream receives continuous updates but moves slower than Fedora, providing a direct preview of what will be in the next minor release of RHEL.
* **RHEL & Rocky Linux:** The downstream enterprise releases. RHEL takes the stabilized CentOS Stream code and freezes it, providing up to 10-year lifecycles prioritizing extreme reliability, security compliance, and backwards compatibility over new features. Rocky Linux takes the published RHEL source code, removes the Red Hat branding, and rebuilds it to provide the exact same enterprise stability for free.

## 3. Package Management (DNF5)

With the release of EL10 (RHEL 10, CentOS Stream 10, Rocky Linux 10), the system utilizes DNF5 for faster dependency resolution and package management.

### Update the System

```bash
sudo dnf \
upgrade
```

### Install a Package

```bash
sudo dnf \
install \
<package_name>
```

### Search for a Package

```bash
dnf \
search \
<search_term>
```

### List Installed Packages

```bash
dnf \
list \
--installed
```

### Clean DNF Cache

```bash
sudo dnf \
clean \
all
```

## 4. Service Management (systemd)

Enterprise Linux distributions rely entirely on `systemd` for service initialization and management.

### Start and Enable a Service on Boot

```bash
sudo systemctl \
enable \
--now \
<service_name>
```

### Stop and Disable a Service

```bash
sudo systemctl \
disable \
--now \
<service_name>
```

### Check Service Status

```bash
systemctl \
status \
<service_name>
```

### Reload Systemd Daemon (After editing unit files)

```bash
sudo systemctl \
daemon-reload
```

## 5. Network Management (NetworkManager)

Networking is handled by NetworkManager (`nmcli`), utilizing keyfiles located in `/etc/NetworkManager/system-connections/`.

### Show All Network Connections

```bash
nmcli \
connection \
show
```

### Bring Up a Network Interface

```bash
sudo nmcli \
connection \
up \
<connection_name>
```

### Set a Static IP Address

```bash
sudo nmcli \
connection \
modify \
<connection_name> \
ipv4.addresses \
<ip_address/CIDR> \
ipv4.gateway \
<gateway_ip> \
ipv4.dns \
<dns_ip> \
ipv4.method \
manual
```

### Reload Network Connections

```bash
sudo nmcli \
connection \
reload
```

## 6. Firewall Management (firewalld)

Host-based firewall rules are managed dynamically via `firewalld` using zones and services.

### List Active Zones and Rules

```bash
sudo firewall-cmd \
--list-all
```

### Open a Specific Port Permanently

```bash
sudo firewall-cmd \
--permanent \
--add-port=<port_number>/<tcp|udp>
```

### Allow a Specific Service Permanently

```bash
sudo firewall-cmd \
--permanent \
--add-service=<service_name>
```

### Reload Firewall to Apply Changes

```bash
sudo firewall-cmd \
--reload
```

## 7. SELinux Management

Security-Enhanced Linux (SELinux) enforces mandatory access control policies. It should remain in enforcing mode on all EL systems.

### Check SELinux Status

```bash
sestatus
```

### Temporarily Change to Permissive Mode (for troubleshooting)

```bash
sudo setenforce \
0
```

### Restore Default SELinux Contexts on a Directory

```bash
sudo restorecon \
-R \
-v \
/path/to/directory
```

### Allow a Service Specific Access via Booleans

```bash
sudo setsebool \
-P \
<boolean_name> \
1
```

*(Use `getsebool -a` to view all available booleans).*
