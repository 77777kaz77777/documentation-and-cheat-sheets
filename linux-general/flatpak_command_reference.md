## Commands to install, update, and manage sandboxed Flatpak apps

# Flatpak Command Reference Guide (Linux Desktop)

## Core Package Management

**Install software.**

```bash
flatpak \
  install \
  <remote_name> \
  <application_id>
```

**Remove (uninstall) software.**

```bash
flatpak \
  uninstall \
  <application_id>
```

**Upgrade software.**

```bash
flatpak \
  update
```

**Remove unused runtimes and extensions.**

```bash
flatpak \
  uninstall \
  --unused
```

## Search and Information

**Search for software matching specified strings.**

```bash
flatpak \
  search \
  <search_term>
```

**List packages depending on their relation to the system with additional details.**

```bash
flatpak \
  info \
  <application_id>
```

**List installed packages (applications only).**

```bash
flatpak \
  list \
  --app
```

**List installed packages (runtimes only).**

```bash
flatpak \
  list \
  --runtime
```

## Repository and Configuration Management

**Add a new repository (remote).**

```bash
flatpak \
  remote-add \
  --if-not-exists \
  <remote_name> \
  <url>
```

**List configured repositories.**

```bash
flatpak \
  remotes
```

**Manage application permissions.**

```bash
flatpak \
  override \
  <application_id>
```
