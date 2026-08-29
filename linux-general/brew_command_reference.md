# Essential Homebrew commands for installing software on macOS and Linux.

## Core Package Management

**Install software.**
```bash
brew \
  install \
  <formula>
```

**Install GUI software (Cask).**
```bash
brew \
  install \
  --cask \
  <cask_name>
```

**Remove (uninstall) software.**
```bash
brew \
  uninstall \
  <formula>
```

**Upgrade software.**
```bash
brew \
  upgrade
```

**Remove unneeded dependencies and clear old cache.**
```bash
brew \
  cleanup
```

## Search and Information

**Search for software matching specified strings.**
```bash
brew \
  search \
  <search_term>
```

**List packages depending on their relation to the system with additional details.**
```bash
brew \
  info \
  <formula>
```

**List installed packages.**
```bash
brew \
  list
```

**Show package dependencies.**
```bash
brew \
  deps \
  <formula>
```

## Repository and Configuration Management

**Generate the metadata cache (update Homebrew and formulae).**
```bash
brew \
  update
```

**Add a new repository (tap).**
```bash
brew \
  tap \
  <user/repo>
```

**Check system for potential problems.**
```bash
brew \
  doctor
```

---
