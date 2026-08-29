# useful commands for Fedora’s DNF package manager.

## Core Package Management

**Install software.**
```bash
dnf install
```

**Remove (uninstall) software.**
```bash
dnf remove
```

**Upgrade software.**
```bash
dnf upgrade
```

**Downgrade software.**
```bash
dnf downgrade
```

**Reinstall software.**
```bash
dnf reinstall
```

**Remove software and install another in one transaction.**
```bash
dnf swap
```

**Remove all unneeded packages originally installed as dependencies.**
```bash
dnf autoremove
```

**Install build dependencies for a package or spec file.**
```bash
dnf builddep
```

**Install debuginfo packages.**
```bash
dnf debuginfo-install
```

**Change the reason for an installed package.**
```bash
dnf mark
```

## Search and Information

**Search for software matching all specified strings.**
```bash
dnf search
```

**List packages depending on their relation to the system with additional details.**
```bash
dnf info
```

**List packages depending on their relation to the system.**
```bash
dnf list
```

**Find what package provides the given value.**
```bash
dnf provides
```

**Search for packages matching various criteria.**
```bash
dnf repoquery
```

**List groups of installed packages not required by other installed packages.**
```bash
dnf leaves
```

**Show package changelogs.**
```bash
dnf changelog
```

**Print a list of unresolved dependencies for repositories.**
```bash
dnf repoclosure
```

## System Updates and Upgrades

**Check for available package upgrades.**
```bash
dnf check-upgrade
```

**Upgrade or downgrade installed software to the latest available versions.**
```bash
dnf distro-sync
```

**Prepare the system for an upgrade to a new release.**
```bash
dnf system-upgrade
```

**Determine whether the system or systemd services need restarting.**
```bash
dnf needs-restarting
```

## Offline Operations

**Manage offline transactions.**
```bash
dnf offline
```

**Store an upgrade transaction to be performed offline.**
```bash
dnf offline-upgrade
```

**Store a distro-sync transaction to be performed offline.**
```bash
dnf offline-distrosync
```

## Repository and Configuration Management

**Manage repositories.**
```bash
dnf repo
```

**Manage configuration.**
```bash
dnf config-manager
```

**Manage Copr repositories (add-ons provided by users/community/third-party).**
```bash
dnf copr
```

**Synchronize a remote DNF repository to a local directory.**
```bash
dnf reposync
```

**Manage a directory with repodata or with rpm packages.**
```bash
dnf repomanage
```

**Generate the metadata cache.**
```bash
dnf makecache
```

**Remove or expire cached data.**
```bash
dnf clean
```

## Transactions and History

**Do transaction.**
```bash
dnf do
```

**Manage transaction history.**
```bash
dnf history
```

**Replay a transaction that was previously stored in a directory.**
```bash
dnf replay
```

## Group and Module Management

**Manage comps groups.**
```bash
dnf group
```

**Manage comps environments.**
```bash
dnf environment
```

**Manage modules.**
```bash
dnf module
```

## Advanced Management

**Manage advisories.**
```bash
dnf advisory
```

**Check for problems in the packagedb.**
```bash
dnf check
```

**Download software to the current directory.**
```bash
dnf download
```

**Manage versionlock configuration.**
```bash
dnf versionlock
```

## Common Aliases

**Alias for `check-upgrade`.**
```bash
dnf check-update
```

**Alias for `group`.**
```bash
dnf grp
```

**Alias for `repo info`.**
```bash
dnf repoinfo
```

**Alias for `repo list`.**
```bash
dnf repolist
```

**Alias for `advisory`.**
```bash
dnf updateinfo
```

**Alias for `upgrade --minimal`.**
```bash
dnf upgrade-minimal
```
