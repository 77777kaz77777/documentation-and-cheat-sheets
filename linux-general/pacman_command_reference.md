## Essential commands for managing Arch Linux packages with Pacman.

# Pacman Command Reference Guide

## Core Package Management

**Install software.**
```bash
pacman \
  -S
```

**Remove (uninstall) software.**
```bash
pacman \
  -R
```

**Upgrade software (synchronize and update).**
```bash
pacman \
  -Syu
```

**Downgrade software (from local cache or package file).**
```bash
pacman \
  -U \
  /var/cache/pacman/pkg/<package_name>.pkg.tar.zst
```

**Reinstall software.**
```bash
pacman \
  -S
```

**Remove software and install another in one transaction (using chaining).**
```bash
pacman \
  -S \
  <package1> && \
pacman \
  -Rs \
  <package2>
```

**Remove all unneeded packages originally installed as dependencies.**
```bash
pacman \
  -Rs \
  $(pacman -Qdtq)
```

**Install build dependencies for a package or PKGBUILD file.**
```bash
makepkg \
  -so
```

**Install debuginfo packages.**
```bash
pacman \
  -S \
  <package>-debug
```

**Change the reason for an installed package (mark as dependency or explicit).**
```bash
pacman \
  -D \
  --asdeps \
  <package>

pacman \
  -D \
  --asexplicit \
  <package>
```

## Search and Information

**Search for software matching all specified strings.**
```bash
pacman \
  -Ss
```

**List packages depending on their relation to the system with additional details.**
```bash
pacman \
  -Si
```

**List packages depending on their relation to the system (locally installed).**
```bash
pacman \
  -Q
```

**Find what package provides the given value (requires pacman -Fy first).**
```bash
pacman \
  -F
```

**Search for packages matching various criteria (list all packages in a repo).**
```bash
pacman \
  -Sl
```

**List groups of installed packages not required by other installed packages (orphans).**
```bash
pacman \
  -Qdt
```

**Show package changelogs.**
```bash
pacman \
  -Qc
```

**Print a list of unresolved dependencies for repositories.**
```bash
pacman \
  -Dk
```

## System Updates and Upgrades

**Check for available package upgrades.**
```bash
pacman \
  -Qu
```

**Upgrade or downgrade installed software to the latest available versions.**
```bash
pacman \
  -Syu
```

**Prepare the system for an upgrade to a new release (rolling release updates all packages).**
```bash
pacman \
  -Syu
```

## Repository and Configuration Management

**Generate the metadata cache (synchronize package databases).**
```bash
pacman \
  -Sy
```

**Remove or expire cached data.**
```bash
pacman \
  -Sc
```

## Transactions and History

**Manage transaction history (viewing log).**
```bash
cat \
  /var/log/pacman.log
```
