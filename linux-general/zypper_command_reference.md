## Everyday commands for managing packages on openSUSE and SLES using Zypper.

# Zypper Command Reference Guide (openSUSE / SUSE Linux Enterprise)

## Core Package Management

**Install software.**
```bash
zypper \
  install \
  <package_name>
```

**Remove (uninstall) software.**
```bash
zypper \
  remove \
  <package_name>
```

**Upgrade software (standard update).**
```bash
zypper \
  update
```

**Upgrade software (distribution upgrade / rolling release).**
```bash
zypper \
  dup
```

**Remove unneeded dependencies.**
```bash
zypper \
  remove \
  --clean-deps \
  <package_name>
```

**Install build dependencies for a package.**
```bash
zypper \
  source-install \
  --build-deps-only \
  <package_name>
```

## Search and Information

**Search for software matching specified strings.**
```bash
zypper \
  search \
  <search_term>
```

**List packages depending on their relation to the system with additional details.**
```bash
zypper \
  info \
  <package_name>
```

**Find what package provides the given value.**
```bash
zypper \
  search \
  --provides \
  <file_or_value>
```

## Repository and Configuration Management

**Generate the metadata cache (refresh).**
```bash
zypper \
  refresh
```

**List configured repositories.**
```bash
zypper \
  repos
```

**Add a new repository.**
```bash
zypper \
  addrepo \
  <url> \
  <alias>
```

**Remove or expire cached data.**
```bash
zypper \
  clean
```

---
