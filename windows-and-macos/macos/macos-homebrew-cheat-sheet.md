# macOS Homebrew Cheat Sheet

Quick-reference guide for installing, updating, and cleaning up software on macOS with Homebrew.

---

**Install Homebrew:**

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Configure Shell Environment (`~/.zprofile`):**

```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```

**Update Homebrew & Formulae Metadata:**

```bash
brew update
```

**Upgrade All Installed Formulae & Casks:**

```bash
brew upgrade
```

**Upgrade Including Auto-Updating GUI Casks:**

```bash
brew upgrade --greedy
```

**Install CLI Package (Formula):**

```bash
brew install [formula]
```

**Install GUI Application (Cask):**

```bash
brew install --cask [app_name]
```

**Search Formulae and Casks:**

```bash
brew search [query]
```

**Inspect Package Dependencies & Analytics:**

```bash
brew info [formula_or_cask]
```

**List Installed Formulae:**

```bash
brew list --formula
```

**List Installed Casks:**

```bash
brew list --cask
```

**Show Dependency Tree for Installed Packages:**

```bash
brew deps --tree --installed
```

**Uninstall Package Only:**

```bash
brew uninstall [formula]
```

**Completely Purge Cask (Removes App, Caches, and `.plist` Preferences):**

```bash
brew uninstall --cask --zap [app_name]
```

**Remove Orphaned Dependencies:**

```bash
brew autoremove
```

**Purge Old Versions & Clear Download Cache:**

```bash
brew cleanup --prune=all -s
```

**Export Installed Packages to a Brewfile (For Reproducible Setup):**

```bash
brew bundle dump --file=~/Brewfile --describe --force
```

**Install All Packages from a Brewfile:**

```bash
brew bundle --file=~/Brewfile
```

**Audit Homebrew Installation Health:**

```bash
brew doctor
```

---

## Sources & Verification

* **Homebrew documentation:** [docs.brew.sh/Manpage](https://docs.brew.sh/Manpage)

## Related guides

* [macOS Command-Line Reference (Apple Silicon)](macos-command-line-reference.md)
* [macOS System, Updates and Hardware Cheat Sheet](macos-system-updates-and-hardware-cheat-sheet.md)
* [macOS Networking Cheat Sheet](macos-networking-cheat-sheet.md)
* [macOS launchd, Processes and Logs Cheat Sheet](macos-launchd-and-logs-cheat-sheet.md)
* [macOS Security Cheat Sheet](macos-security-cheat-sheet.md)
* [macOS defaults, Finder and CLI Tips Cheat Sheet](macos-defaults-and-cli-tips-cheat-sheet.md)
* [Homebrew Command Reference (macOS and Linux)](../../linux-general/package-management/brew-command-reference.md)
