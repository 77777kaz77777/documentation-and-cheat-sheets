## quick reference for the ⁠opkg⁠ package manager, commonly used on OpenWrt and embedded Linux systems. It covers the essential commands needed to install, upgrade, query, and manage software packages and their dependencies

## Updating & Upgrading

* `opkg update` : Fetches the latest list of packages from the configured package repositories. You must run this after each reboot before finding or installing any packages.
* `opkg upgrade` : Upgrades all currently installed packages. *(Caution: Upgrading kernel modules on OpenWrt snapshot/trunk builds can sometimes break dependencies).*
* `opkg upgrade <package>` : Upgrades one or more specific packages.
* `opkg list-upgradable` : Displays a list of all packages that currently have upgrades available.

## Installing & Removing

* `opkg install <package>` : Downloads and installs a specific package along with its dependencies.
* `opkg remove <package>` : Removes a currently installed package.

## Searching & Listing

* `opkg list` : Displays a complete list of all available packages in the configured repositories.
* `opkg list '*keyword*'` : Searches for available packages using wildcards (e.g., `opkg list '*usb*'` finds any package containing "usb" in its name or description).
* `opkg list-installed` : Outputs a list of all currently installed packages on the system.
* `opkg list-installed '*keyword*'` : Narrows down the list of installed packages using a wildcard search.
* `opkg info <package>` : Displays detailed metadata for a specific package, including its version, size, dependencies, and description.

## Dependencies & Advanced Commands

* `opkg whatdepends [-A] <package>` : Shows which installed packages depend on the specified package.
* `opkg whatprovides <package>` : Determines which package provides a specific file or dependency.
* `opkg print-architecture` : Lists the package architectures that are installable on the current system.
* `--force-depends` : A flag used alongside installation commands to ignore dependency errors and force an installation (useful when missing dependencies are handled externally).
* `-d <dest_name>` / `--dest <dest_name>` : Specifies a different root directory for package installation, removal, or upgrading (requires the destination name to be defined in the opkg configuration file).
