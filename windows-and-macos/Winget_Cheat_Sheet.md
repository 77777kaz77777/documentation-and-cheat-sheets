## A quick-reference guide for managing Windows software packages using the Winget command-line tool, covering package discovery, silent installations, bulk upgrades, and system provisioning.

## Search & Discovery
| Command | Action |
| :--- | :--- |
| `winget search <name>` | Searches repositories for a package matching the name. |
| `winget search --id <id>` | Searches for a specific, exact package ID. |
| `winget list` | Lists all installed applications on the system. |
| `winget list <name>` | Checks if a specific application is currently installed. |
| `winget show <package>` | Displays detailed metadata (version, publisher, URLs) for a package. |

## Installation & Removal
| Command | Action |
| :--- | :--- |
| `winget install <name>` | Installs the best match for the given name. |
| `winget install --id <id> -e` | **Best Practice:** Installs an exact match by its unique ID. |
| `winget uninstall <name>` | Uninstalls the specified package. |
| `winget uninstall --id <id>` | Uninstalls a package using its exact ID. |

## Updates & Upgrades
| Command | Action |
| :--- | :--- |
| `winget upgrade` | Lists all installed packages that have an available update. |
| `winget upgrade <name>` | Upgrades a specific package. |
| `winget upgrade --all` | Upgrades all eligible packages to their latest versions. |

## Automation & Provisioning
| Command | Action |
| :--- | :--- |
| `winget export -o <file.json>` | Exports a list of all currently installed winget packages to a JSON file. |
| `winget import -i <file.json>` | Installs all packages listed in a previously exported JSON file. |

## Essential Modifiers & Flags
| Flag | Effect |
| :--- | :--- |
| `-h` or `--silent` | Runs the installer in the background without launching a visible UI. |
| `--accept-package-agreements` | Automatically accepts license agreements. |
| `--accept-source-agreements` | Automatically accepts repository agreements. |
| `--override "<args>"` | Passes custom arguments directly to the underlying `.exe` or `.msi` installer. |
| `-v <version>` | Installs a specific version of a package rather than the latest. |

**Example of a fully automated, silent install:**
```powershell
winget install --id Mozilla.Firefox -e --silent --accept-package-agreements --accept-source-agreements
```
