## A quick-reference guide for managing Windows software packages using the Winget command-line tool, covering package discovery, silent installations, bulk upgrades, and system provisioning

## Search & Discovery

**Searches repositories for a package matching the name:**
```powershell
winget search <name>
```

**Searches for a specific, exact package ID:**
```powershell
winget search --id <id>
```

**Lists all installed applications on the system:**
```powershell
winget list
```

**Checks if a specific application is currently installed:**
```powershell
winget list <name>
```

**Displays detailed metadata (version, publisher, URLs) for a package:**
```powershell
winget show <package>
```

## Installation & Removal

**Installs the best match for the given name:**
```powershell
winget install <name>
```

****Best Practice:** Installs an exact match by its unique ID:**
```powershell
winget install --id <id> -e
```

**Uninstalls the specified package:**
```powershell
winget uninstall <name>
```

**Uninstalls a package using its exact ID:**
```powershell
winget uninstall --id <id>
```

## Updates & Upgrades

**Lists all installed packages that have an available update:**
```powershell
winget upgrade
```

**Upgrades a specific package:**
```powershell
winget upgrade <name>
```

**Upgrades all eligible packages to their latest versions:**
```powershell
winget upgrade --all
```

## Automation & Provisioning

**Exports a list of all currently installed winget packages to a JSON file:**
```powershell
winget export -o <file.json>
```

**Installs all packages listed in a previously exported JSON file:**
```powershell
winget import -i <file.json>
```

## Essential Modifiers & Flags

| Flag                          | Effect                                                                         |
| :---------------------------- | :----------------------------------------------------------------------------- |
| `-h` or `--silent`            | Runs the installer in the background without launching a visible UI.           |
| `--accept-package-agreements` | Automatically accepts license agreements.                                      |
| `--accept-source-agreements`  | Automatically accepts repository agreements.                                   |
| `--override "<args>"`         | Passes custom arguments directly to the underlying `.exe` or `.msi` installer. |
| `-v <version>`                | Installs a specific version of a package rather than the latest.               |

**Example of a fully automated, silent install:**

```powershell
winget install --id Mozilla.Firefox -e --silent --accept-package-agreements --accept-source-agreements
```
