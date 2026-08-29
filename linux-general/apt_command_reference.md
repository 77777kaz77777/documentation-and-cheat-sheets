#  Everyday package management commands for Debian and Ubuntu using APT.

## Core Package Management

**Install software.**
```bash
apt \
  install
```

**Remove (uninstall) software.**
```bash
apt \
  remove
```

**Upgrade software.**
```bash
apt \
  upgrade
```

**Downgrade software.**
```bash
apt \
  install \
  <package>=<version>
```

**Reinstall software.**
```bash
apt \
  reinstall
```

**Remove software and install another in one transaction (using chaining).**
```bash
apt \
  install \
  <package1> && \
apt \
  remove \
  <package2>
```

**Remove all unneeded packages originally installed as dependencies.**
```bash
apt \
  autoremove
```

**Install build dependencies for a package or spec file.**
```bash
apt \
  build-dep
```

**Install debuginfo packages.**
```bash
apt \
  install \
  <package>-dbgsym
```

**Change the reason for an installed package (mark as auto or manual).**
```bash
apt-mark \
  auto \
  <package>

apt-mark \
  manual \
  <package>
```

## Search and Information

**Search for software matching all specified strings.**
```bash
apt \
  search
```

**List packages depending on their relation to the system with additional details.**
```bash
apt \
  show
```

**List packages depending on their relation to the system.**
```bash
apt \
  list
```

**Find what package provides the given value.**
```bash
apt-file \
  search
```

**Search for packages matching various criteria (cache information).**
```bash
apt-cache \
  showpkg
```

**List groups of installed packages not required by other installed packages.**
```bash
apt-mark \
  showauto
```

**Show package changelogs.**
```bash
apt \
  changelog
```

**Print a list of unresolved dependencies for repositories.**
```bash
apt-get \
  check
```

## System Updates and Upgrades

**Check for available package upgrades.**
```bash
apt \
  list \
  --upgradable
```

**Upgrade or downgrade installed software to the latest available versions (handles changing dependencies).**
```bash
apt \
  full-upgrade
```

**Prepare the system for an upgrade to a new release.**
```bash
do-release-upgrade
```

**Determine whether the system or systemd services need restarting.**
```bash
needrestart
```

## Repository and Configuration Management

**Manage repositories (add).**
```bash
add-apt-repository
```

**Manage Copr-equivalent repositories (Personal Package Archives).**
```bash
add-apt-repository \
  ppa:<name>
```

**Generate the metadata cache.**
```bash
apt \
  update
```

**Remove or expire cached data.**
```bash
apt \
  clean
```

## Transactions and History

**Manage transaction history (viewing log).**
```bash
cat \
  /var/log/apt/history.log
```
