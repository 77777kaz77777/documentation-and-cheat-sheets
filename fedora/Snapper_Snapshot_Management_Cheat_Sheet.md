# Commands to create filesystem snapshots and roll back changes using Snapper

## Snapshot Operations

| Command | Description |
| :--- | :--- |
| `sudo snapper ls` | List all snapshots for the default configuration (root). |
| `sudo snapper -c <config> ls` | List snapshots for a specific configuration (e.g., `home`). |
| `sudo snapper create -c <config> -d "<description>"` | Create a manual snapshot with a description. |
| `sudo snapper delete <number>` | Delete a specific snapshot by its number. |
| `sudo snapper delete <start_num>-<end_num>` | Delete a range of snapshots. |

## Rollback and Recovery

| Command | Description |
| :--- | :--- |
| `sudo snapper rollback <number>` | Roll back the system to the specified snapshot number. |
| `sudo snapper undochange <num1>..<num2>` | Undo changes made between two specific snapshots. |
| `sudo snapper diff <num1>..<num2>` | Show file differences between two snapshots. |
| `sudo snapper status <num1>..<num2>` | Show added (+), deleted (-), or modified (c) files between snapshots. |

## Configuration Management

| Command | Description |
| :--- | :--- |
| `sudo snapper list-configs` | List all active Snapper configurations. |
| `sudo snapper -c <config> get-config` | View the settings (retention, timers) for a specific configuration. |
| `sudo snapper -c <config> set-config <KEY>=<VALUE>` | Modify a configuration parameter (e.g., `TIMELINE_LIMIT_HOURLY=5`). |
