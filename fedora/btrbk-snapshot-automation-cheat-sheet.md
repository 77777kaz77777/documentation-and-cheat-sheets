## Steps to automate Btrfs snapshots and backups using Btrbk

## Execution & Dry Runs

| Command | Description |
| :--- | :--- |
| `sudo btrbk dryrun` | Simulate the btrbk configuration without making any changes. |
| `sudo btrbk run` | Execute backups and snapshots according to `/etc/btrbk/btrbk.conf`. |
| `sudo btrbk -c /path/to/custom.conf run` | Run btrbk using a specific configuration file. |
| `sudo btrbk snapshot` | Only create snapshots (skip sending them to backup targets). |
| `sudo btrbk archive <source> <target>` | Manually send a specific subvolume to an archive target. |

## Monitoring & Status

| Command | Description |
| :--- | :--- |
| `sudo btrbk stats` | Display statistics of all snapshots and backups managed by btrbk. |
| `sudo btrbk list` | List all snapshots and backups defined in the configuration. |
| `sudo btrbk list snapshots` | Filter the list to only show local snapshots. |
| `sudo btrbk ls /path/to/subvolume` | List all snapshots for a specific subvolume directory. |

## Configuration Testing (`btrbk.conf`)

| Command | Description |
| :--- | :--- |
| `btrbk config print` | Parse and print the current configuration, expanding all wildcards. |
| `sudo journalctl -u btrbk.service` | View logs for automated btrbk systemd timer executions. |
| `sudo systemctl status btrbk.timer` | Check the status of the automated btrbk schedule. |
