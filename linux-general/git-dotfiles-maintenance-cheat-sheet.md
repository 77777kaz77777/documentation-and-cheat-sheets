# Commands and scripts for backing up system configurations and dotfiles with Git

## Repository Syncing

| Command | Description |
| :--- | :--- |
| `git clone git@github.com:77777kaz77777/linux-maintenance-and-dotfiles.git` | Clone the maintenance repository via SSH. |
| `git pull origin main` | Fetch and merge the latest dotfile changes from the remote repository. |
| `git fetch --all && git reset --hard origin/main` | Force overwrite local files with the remote main branch (useful for fresh installs). |

## Staging & Committing

| Command | Description |
| :--- | :--- |
| `git add .` | Stage all modified maintenance scripts and dotfiles. |
| `git add -u` | Stage only modified and deleted files (ignore new untracked files). |
| `git commit -m "Update firewall rules and dnf configs"` | Commit staged changes with a descriptive message. |
| `git push origin main` | Push committed changes to GitHub. |

## Status & History

| Command | Description |
| :--- | :--- |
| `git status` | Show working tree status (modified dotfiles, untracked scripts). |
| `git diff` | Show unstaged changes within the scripts. |
| `git log --oneline -5` | View the last 5 commits to track recent system changes. |
| `git restore <file>` | Discard uncommitted local changes to a specific script. |
