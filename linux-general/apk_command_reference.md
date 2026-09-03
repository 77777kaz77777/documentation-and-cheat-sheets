# Commands for installing and updating packages in Alpine Linux and containers using APK

## Core Package Management

**Install software.**

```bash
apk \
  add \
  <package_name>
```

**Remove (uninstall) software.**

```bash
apk \
  del \
  <package_name>
```

**Upgrade software.**

```bash
apk \
  upgrade
```

**Install software temporarily (removed on next reboot or cache clean).**

```bash
apk \
  add \
  --virtual \
  <virtual_package_name> \
  <package_name>
```

## Search and Information

**Search for software matching specified strings.**

```bash
apk \
  search \
  <search_term>
```

**List packages depending on their relation to the system with additional details.**

```bash
apk \
  info \
  <package_name>
```

**Find what package provides the given value.**

```bash
apk \
  info \
  --who-owns \
  <file_path>
```

## Repository and Configuration Management

**Generate the metadata cache (update package lists).**

```bash
apk \
  update
```

**Clean cache.**

```bash
apk \
  cache \
  clean
```

---
