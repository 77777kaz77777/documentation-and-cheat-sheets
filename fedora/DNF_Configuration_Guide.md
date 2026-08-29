## Tweaks and settings to speed up the DNF package manager.

# For the complete configuration file, please visit the linux-maintenance-and-dotfiles repository.
This guide explains the key parameters found in `/etc/dnf/dnf.conf` to optimize Fedora's package manager for performance and reliability.

## Overview
The `/etc/dnf/dnf.conf` file is the primary configuration file for DNF. Modifying the `[main]` section allows you to tailor DNF's behavior to your hardware, network, and preferences.

## Configuration Parameters

### `[main]`
The primary section header for global DNF configurations. Settings placed underneath this header apply universally to all DNF package management operations across the system.

### `gpgcheck=1`
Enforces cryptographic signature verification for downloaded packages. When enabled, DNF verifies the GPG key of the package against trusted local keys before installation, preventing the installation of tampered or malicious software.

### `installonly_limit=3`
Limits the maximum number of simultaneous versions of "install-only" packages (such as the Linux kernel) that can be kept on the system at any given time. When a fourth kernel is installed, the oldest one is automatically removed to conserve disk space.

### `clean_requirements_on_remove=true`
Automatically purges orphaned dependencies (packages that were installed solely to satisfy dependencies for another package) when the parent package is uninstalled, preventing unnecessary clutter in the system libraries.

### `best=False`
Instructs DNF to tolerate slightly older or non-ideal package versions during transactions if the absolute latest version cannot be installed due to dependency conflicts, making updates more resilient against temporary repository inconsistencies.

### `skip_if_unavailable=True`
Tells DNF to bypass specific repositories if they are unreachable, offline, or experiencing timeout errors, allowing package operations to proceed successfully using the remaining active repositories rather than failing entirely.

### `max_parallel_downloads=10`
Increases the maximum number of simultaneous package downloads from 3 (the default) up to 10, significantly reducing overall download times on fast internet connections by fully utilizing available bandwidth.

### `fastestmirror=True`
Measures response times across available mirror servers for each repository and automatically selects and prioritizes the fastest responding mirrors for package downloads and metadata updates.
