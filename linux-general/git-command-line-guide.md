# Git Command-Line Reference Guide

A structured, detailed, cross-platform command-line reference for Git operations. Every command below is in its own isolated block so you can copy it with a single click.

---

## 0. Command-Line Syntax Conventions

When reading command-line documentation, replace any `<placeholder>` (including the angle brackets) with your actual file name, branch name, or URL:

* `<placeholder>` — **Required** argument (e.g., replace `<branch>` with `main`).
* `[optional]` — **Optional** argument or flag.
* `HEAD` — Points to the currently checked-out branch and its latest commit.
* `HEAD~1` — Points to $1$ commit before `HEAD` (`HEAD~2` is $2$ commits back, etc.).
* `origin` — The default name for your remote repository (e.g., on GitHub or GitLab).

---

## 1. Configuration & Authentication (`git config`)

### Check Installed Git Version
```bash
git --version
```

### Set Your Global Username
*(Attached to every commit you make)*
```bash
git config --global user.name "Your Name"
```

### Set Your Global Email Address
*(Must match the email on your GitHub/GitLab account)*
```bash
git config --global user.email "your.email@example.com"
```

### Set Default Branch Name to `main`
```bash
git config --global init.defaultBranch main
```

### Set Default Text Editor to VS Code
*(Prevents getting trapped in Vim during commits or merges)*
```bash
git config --global core.editor "code --wait"
```

### Set Default Text Editor to Nano (Simple Terminal Editor)
```bash
git config --global core.editor "nano"
```

### View All Active Configuration Settings
```bash
git config --list --show-origin
```

### Authenticate via GitHub CLI (Recommended)
```bash
gh auth login
```

### Generate a New SSH Key Pair
```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```

---

## 2. Repository Initialization (`init`, `clone`)

### Initialize a New Local Repository in the Current Folder
```bash
git init
```

### Clone a Remote Repository via HTTPS
```bash
git clone https://github.com/username/repository-name.git
```

### Clone a Remote Repository via SSH
```bash
git clone git@github.com:username/repository-name.git
```

### Clone a Remote Repository into a Custom Folder Name
```bash
git clone https://github.com/username/repository-name.git my-custom-folder
```

### Shallow Clone (Download Only the Latest Commit for Large Repos)
```bash
git clone --depth 1 https://github.com/username/repository-name.git
```

---

## 3. Tracking, Staging & Committing (`status`, `add`, `commit`)

### Check Full Repository Status
*(Shows untracked, modified, and staged files)*
```bash
git status
```

### Check Compact Repository Status
*(`M` = modified, `A` = added, `??` = untracked)*
```bash
git status -sb
```

### Stage a Specific File
```bash
git add path/to/file.ext
```

### Stage All Files (New, Modified, and Deleted) Across the Entire Repo
```bash
git add -A
```

### Stage All Files in the Current Directory and Subdirectories
```bash
git add .
```

### Stage Only Modified and Deleted Files (Ignores New Untracked Files)
```bash
git add -u
```

### Interactively Stage Specific Chunks/Lines Inside a File
*(Press `y` to stage chunk, `n` to skip chunk, `q` to quit)*
```bash
git add -p
```

### Commit Staged Changes with an Inline Message
```bash
git commit -m "Describe what you changed and why"
```

### Stage All Tracked, Modified Files and Commit in One Step
*(Note: Does not include brand-new untracked files)*
```bash
git commit -am "Describe what you changed and why"
```

### Edit the Previous Commit Message
*(Only do this before pushing to a shared remote branch)*
```bash
git commit --amend -m "New corrected commit message"
```

### Add Newly Staged Files into the Previous Commit Without Changing Its Message
```bash
git commit --amend --no-edit
```

---

## 4. Inspection, Diffs & History (`diff`, `log`, `show`, `blame`)

*(Note: If the terminal shows `:` or `(END)` at the bottom, press **`q`** to exit back to the command prompt).*

### View Unstaged Changes (Working Directory vs. Staging Area)
```bash
git diff
```

### View Staged Changes About to Be Committed (Staging Area vs. Last Commit)
```bash
git diff --staged
```

### View All Uncommitted Changes (Both Staged and Unstaged)
```bash
git diff HEAD
```

### Compare Differences Between Two Branches
```bash
git diff main feature-branch
```

### View Summary of Changed Files (Insertions/Deletions Count Only)
```bash
git diff --stat
```

### View Standard Commit History
```bash
git log
```

### View Compact One-Line Commit History
```bash
git log --oneline
```

### View Visual Branch Graph of All Commits Across All Branches
```bash
git log --graph --oneline --decorate --all
```

### View Only the Last 5 Commits
```bash
git log -n 5 --oneline
```

### View Commit History Along with Full Code Diffs
```bash
git log -p -n 3
```

### Inspect a Specific Commit's Metadata and Code Changes
```bash
git show <commit-hash>
```

### See Who Last Modified Each Line of a File
```bash
git blame path/to/file.ext
```

---

## 5. Branching & Merging (`branch`, `switch`, `merge`)

### List All Local Branches
*(`*` indicates the branch you are currently on)*
```bash
git branch
```

### List Both Local and Remote Branches
```bash
git branch -a
```

### Create a New Branch and Switch to It Immediately
```bash
git switch -c new-branch-name
```

### Switch to an Existing Branch
```bash
git switch existing-branch-name
```

### Switch Back to the Previously Checked-Out Branch
```bash
git switch -
```

### Legacy Command: Create and Switch to a New Branch
```bash
git checkout -b new-branch-name
```

### Legacy Command: Switch to an Existing Branch
```bash
git checkout existing-branch-name
```

### Rename the Currently Checked-Out Branch
```bash
git branch -m new-branch-name
```

### Safely Delete a Local Branch (Only Works if Already Merged)
```bash
git branch -d branch-to-delete
```

### Force Delete a Local Branch (Deletes Even if Unmerged)
```bash
git branch -D branch-to-delete
```

### Merge Another Branch into Your Currently Active Branch
*(First run `git switch main`, then merge your feature branch into it)*
```bash
git merge feature-branch
```

### Abort an Active Merge (Return Everything to Pre-Merge State)
```bash
git merge --abort
```

### Complete a Merge After Manually Fixing Conflict Markers and Running `git add`
```bash
git merge --continue
```

---

## 6. Remote Synchronization (`remote`, `fetch`, `pull`, `push`)

### View Configured Remote URLs
```bash
git remote -v
```

### Link a Local Repository to a Remote Repository (`origin`)
```bash
git remote add origin https://github.com/username/repository-name.git
```

### Change an Existing Remote URL
```bash
git remote set-url origin https://github.com/username/new-repository.git
```

### Download Remote History Without Modifying Your Local Working Files
*(Also cleans up deleted remote branches)*
```bash
git fetch origin --prune
```

### Download Remote Changes and Merge Them into Your Current Branch
```bash
git pull origin main
```

### Download Remote Changes and Rebase Your Local Commits on Top of Them
*(Keeps commit history straight and clean without extra merge commits)*
```bash
git pull --rebase origin main
```

### Push a New Local Branch to Remote for the First Time (`-u` Links Them)
```bash
git push -u origin new-branch-name
```

### Push Commits on an Already-Linked Branch
```bash
git push
```

### Safely Force Push After Amending or Rebasing
*(Refuses to overwrite if a teammate pushed new code you haven't fetched yet)*
```bash
git push --force-with-lease
```

### Delete a Branch on the Remote Server
```bash
git push origin --delete branch-to-delete
```

---

## 7. Stashing Work (`git stash`)

Use stash when you need to switch branches immediately without committing half-finished work.

### Stash All Modified Tracked Files
```bash
git stash
```

### Stash Modified AND Untracked Files with a Descriptive Note
```bash
git stash push -u -m "WIP: working on login form"
```

### List All Saved Stashes
```bash
git stash list
```

### Restore the Most Recent Stash and Remove It from the Stash List
```bash
git stash pop
```

### Restore a Specific Stash Without Removing It from the Stash List
```bash
git stash apply stash@{0}
```

### Delete the Most Recent Stash
```bash
git stash drop
```

### Delete All Stashes Permanently
```bash
git stash clear
```

---

## 8. Undoing, Restoring & Resetting (`restore`, `reset`, `revert`, `clean`, `reflog`)

### Unstage a File (Keep Your File Edits, Just Remove from `git add`)
```bash
git restore --staged path/to/file.ext
```

### Discard Local Unstaged Edits in a File (Destructive: Reverts File to Last Commit)
```bash
git restore path/to/file.ext
```

### Restore a File to Match a Specific Older Commit
```bash
git restore --source=<commit-hash> path/to/file.ext
```

### Stop Tracking a File in Git Without Deleting It from Your Computer
*(Useful when you accidentally committed a `.env` file)*
```bash
git rm --cached path/to/file.ext
```

### Undo Last Commit, Keep All Changes Staged
*(Moves `HEAD` back 1 commit; files stay green/staged)*
```bash
git reset --soft HEAD~1
```

### Undo Last Commit, Keep All Changes Unstaged
*(Moves `HEAD` back 1 commit; files stay modified in your working folder)*
```bash
git reset HEAD~1
```

### Destroy Last Commit AND Permanently Wipe All Uncommitted Changes
*(Warning: Completely deletes uncommitted work)*
```bash
git reset --hard HEAD~1
```

### Safely Undo a Older Commit on a Shared Branch
*(Creates a brand-new commit that reverses the target commit without rewriting history)*
```bash
git revert <commit-hash>
```

### Preview Which Untracked Files Would Be Deleted by `git clean`
```bash
git clean -nd
```

### Permanently Delete All Untracked Files and Folders
```bash
git clean -fd
```

### View the Recovery Ledger of Every Action You Have Taken Locally
*(Use this to find the `<commit-hash>` of accidentally deleted commits or branches)*
```bash
git reflog
```

### Recover a Lost Commit or Branch Found in `git reflog`
```bash
git reset --hard <reflog-commit-hash>
```

---

## 9. Quick Troubleshooting & Emergency Commands

### Committed to the Wrong Branch by Mistake (Before Pushing)
Run these three commands in order to move the commit to a new branch and rewind the current branch:
```bash
git branch correct-branch-name
```
```bash
git reset --hard HEAD~1
```
```bash
git switch correct-branch-name
```

### Force Git to Recognize a File Capitalization Rename (`file.js` to `File.js`)
```bash
git mv file.js File.js
```

### Escape the Vim Terminal Editor
If your terminal opens a screen full of `~` lines after `git commit` or `git merge`, press the `Escape` key, type the following characters, and press `Enter`:
```text
:wq
```