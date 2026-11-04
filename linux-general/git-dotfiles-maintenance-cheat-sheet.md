# Commands and scripts for backing up system configurations and dotfiles with Git

## Repository Syncing

**Clone the maintenance repository via SSH:**
```bash
git clone git@github.com:77777kaz77777/linux-maintenance-and-dotfiles.git
```

**Fetch and merge the latest dotfile changes from the remote repository:**
```bash
git pull origin main
```

**Force overwrite local files with the remote main branch (useful for fresh installs):**
```bash
git fetch --all && git reset --hard origin/main
```

## Staging & Committing

**Stage all modified maintenance scripts and dotfiles:**
```bash
git add .
```

**Stage only modified and deleted files (ignore new untracked files):**
```bash
git add -u
```

**Commit staged changes with a descriptive message:**
```bash
git commit -m "Update firewall rules and dnf configs"
```

**Push committed changes to GitHub:**
```bash
git push origin main
```

## Status & History

**Show working tree status (modified dotfiles, untracked scripts):**
```bash
git status
```

**Show unstaged changes within the scripts:**
```bash
git diff
```

**View the last 5 commits to track recent system changes:**
```bash
git log --oneline -5
```

**Discard uncommitted local changes to a specific script:**
```bash
git restore <file>
```
