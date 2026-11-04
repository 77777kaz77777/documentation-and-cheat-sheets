## Steps to automate Btrfs snapshots and backups using Btrbk

## Execution & Dry Runs

**Simulate the btrbk configuration without making any changes:**
```bash
sudo btrbk dryrun
```

**Execute backups and snapshots according to `/etc/btrbk/btrbk.conf`:**
```bash
sudo btrbk run
```

**Run btrbk using a specific configuration file:**
```bash
sudo btrbk -c /path/to/custom.conf run
```

**Only create snapshots (skip sending them to backup targets):**
```bash
sudo btrbk snapshot
```

**Manually send a specific subvolume to an archive target:**
```bash
sudo btrbk archive <source> <target>
```

## Monitoring & Status

**Display statistics of all snapshots and backups managed by btrbk:**
```bash
sudo btrbk stats
```

**List all snapshots and backups defined in the configuration:**
```bash
sudo btrbk list
```

**Filter the list to only show local snapshots:**
```bash
sudo btrbk list snapshots
```

**List all snapshots for a specific subvolume directory:**
```bash
sudo btrbk ls /path/to/subvolume
```

## Configuration Testing (`btrbk.conf`)

**Parse and print the current configuration, expanding all wildcards:**
```bash
btrbk config print
```

**View logs for automated btrbk systemd timer executions:**
```bash
sudo journalctl -u btrbk.service
```

**Check the status of the automated btrbk schedule:**
```bash
sudo systemctl status btrbk.timer
```
