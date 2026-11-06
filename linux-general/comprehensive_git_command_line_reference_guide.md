# Git Command-Line Reference Guide

A structured, detailed, cross-platform command-line reference for Git operations.

## 0. Command-Line Syntax Conventions

When reading command-line documentation, observe the following standard notation:

| Notation | Meaning | Example | Usage | 
| ----- | ----- | ----- | ----- | 
| `<placeholder>` | **Required** argument. Replace the brackets and text with your actual value. | `git switch <branch>` | `git switch main` | 
| `[optional]` | **Optional** argument or flag. You may omit this if not needed. | `git status [-s]` | `git status` or `git status -s` | 
| `a \| b` | **Mutually exclusive** options. Choose either `a` or `b`, not both. | `git branch <-d \| -D> <branch>` | `git branch -d feat-1` | 
| `...` | **Repeatable** argument. You can pass multiple items separated by spaces. | `git add <file>...` | `git add index.html style.css` | 

### Core Architecture & Terminology

```
[Working Directory] --(git add)--> [Staging Area / Index] --(git commit)--> [Local Repo (HEAD)] --(git push)--> [Remote Repo (origin)]
[Working Directory] <--(git restore)-- [Staging Area]                        [Local Repo (HEAD)] <--(git fetch)-- [Remote Repo (origin)]
```

* **`Working Directory`**: The active filesystem directory on your machine where you edit files.
* **`Staging Area (Index)`**: The intermediate buffer holding changes queued for the next commit snapshot.
* **`HEAD`**: Pointer referencing the currently checked-out branch and its latest commit snapshot.
* **`HEAD~n`**: Relative reference pointing $n$ commits before `HEAD` (e.g., `HEAD~1` is the previous commit).
* **`origin`**: Default alias pointing to the hosted remote repository (e.g., GitHub, GitLab, Bitbucket).

## 1. Configuration & Authentication (`git config`)

### Synopsis

```
git config [--global | --local | --system] <key> [<value>]
```

### Configuration Reference Table

| Command / Option | Scope / Flag | Description | 
| ----- | ----- | ----- | 
| `git --version` | *None* | Verify the installed Git version. | 
| `git config user.name "<name>"` | `--global` | Set the author name attached to all commits across the system. | 
| `git config user.email "<email>"` | `--global` | Set the author email address attached to all commits. | 
| `git config init.defaultBranch main` | `--global` | Set default initial branch name to `main` instead of `master`. | 
| `git config core.editor "<editor>"` | `--global` | Set default text editor (`"nano"`, `"vim"`, or `"code --wait"` for VS Code). | 
| `git config core.excludesfile <path>` | `--global` | Set the path to a global `.gitignore` file applied across all local repositories. | 
| `git config --list` | `[--show-origin]` | List all active configuration settings and the file paths where they are defined. | 

### Remote Authentication

| Method | Command Sequence | Description | 
| ----- | ----- | ----- | 
| **GitHub CLI** *(Recommended)* | `gh auth login` | Interactive browser-based authentication (automatically configures Git credentials). | 
| **SSH Keygen** | `ssh-keygen -t ed25519 -C "<email>"` | Generate a modern Ed25519 SSH key pair in `~/.ssh/`. | 
| **SSH Agent** | `ssh-add ~/.ssh/id_ed25519` | Register your private SSH key with the local SSH authentication agent. | 

## 2. Repository Initialization (`init`, `clone`)

### Synopsis

```
git init [<directory>]
git clone <repo-url> [<local-dir>]
```

### Command Reference

| Command | Flags / Arguments | Description | 
| ----- | ----- | ----- | 
| `git init` | *None* | Initialize an empty `.git` repository inside the current directory. | 
| `git clone <url>` | `https://...` or `git@...` | Download a full copy of a remote repository into a newly created folder. | 
| `git clone <url> <dir>` | `<dir>` | Clone the remote repository into a custom folder named `<dir>`. | 
| `git clone --depth 1 <url>` | `--depth <n>` | Perform a shallow clone containing only the latest $n$ commits (faster for huge repos). | 

## 3. Tracking, Staging & Committing (`status`, `add`, `commit`)

### Synopsis

```
git status [-s] [-b]
git add [<options>] [<pathspec>...]
git commit [<options>] [-m "<message>"]
```

### `git status` & `git add` Reference

| Command | Flag / Option | Description | 
| ----- | ----- | ----- | 
| `git status` | *None* | Show verbose state of working directory and staging area (untracked, modified, staged). | 
| `git status -sb` | `-s` (short), `-b` (branch) | Display compact two-column status output (`M` = modified, `A` = added, `??` = untracked). | 
| `git add <file>` | `<pathspec>` | Stage specific file(s) or directory for the next commit. | 
| `git add .` | `.` | Stage all new, modified, and deleted files in the current directory and subdirectories. | 
| `git add -A` | `-A` or `--all` | Stage all new, modified, and deleted files across the entire repository tree. | 
| `git add -u` | `-u` or `--update` | Stage modified and deleted files only (ignores brand-new untracked files). | 
| `git add -p` | `-p` or `--patch` | Interactively review each change hunk (`y` to stage, `n` to skip, `q` to quit). | 

### `git commit` Reference

| Command | Flag / Option | Description | 
| ----- | ----- | ----- | 
| `git commit -m "<msg>"` | `-m <msg>` | Record staged snapshot to repository history with an inline commit message. | 
| `git commit -am "<msg>"` | `-a` + `-m <msg>` | Automatically stage all **tracked, modified** files and commit immediately (skips `git add`). | 
| `git commit --amend` | `[-m "<new-msg>"]` | Replace the tip of the current branch by combining staged changes with the previous commit. | 
| `git commit --amend --no-edit` | `--no-edit` | Add staged files into the previous commit without changing its commit message. | 

## 4. Inspection, Diffs & History (`diff`, `log`, `show`, `blame`)

*(Terminal Pager Note: When viewing long outputs, use `Up`/`Down` arrows to scroll and press **`q`** to exit back to the command prompt).*

### Synopsis

```
git diff [--staged] [<commit>] [--] [<path>...]
git log [<options>] [<revision-range>]
```

### Inspection Reference Table

| Command | Flags / Arguments | Description | 
| ----- | ----- | ----- | 
| `git diff` | *None* | Show unstaged line-by-line differences between Working Directory and Staging Area. | 
| `git diff --staged` | `--staged` or `--cached` | Show staged differences between the Staging Area and the last commit (`HEAD`). | 
| `git diff HEAD` | `HEAD` | Show all uncommitted changes (both staged and unstaged) since the last commit. | 
| `git diff <branchA> <branchB>` | `<branchA> <branchB>` | Compare differences between the tips of two branches. | 
| `git diff --stat` | `--stat` | Show a summary histogram of changed files (insertions/deletions) instead of full code lines. | 
| `git log` | *None* | List commits in reverse chronological order with full metadata. | 
| `git log --oneline` | `--oneline` | Condense each commit to a single line (`<7-char-hash> <commit-subject>`). | 
| `git log --graph --oneline --all` | `--graph`, `--all` | Draw a text-based ASCII topology graph of all branches and merges. | 
| `git log -n <number>` | `-n <count>` | Limit log output to the most recent `<number>` of commits (e.g., `git log -n 5`). | 
| `git log -p` | `-p` or `--patch` | Display the full code diff introduced by each commit in the log. | 
| `git show <commit-hash>` | `<commit-hash>` | Display metadata and code diff for a single specified commit. | 
| `git blame <file>` | `[-L <start>,<end>]` | Show which commit and author last modified each line of a file. | 

## 5. Branching & Merging (`branch`, `switch`, `merge`)

### Synopsis

```
git branch [-a | -r] [-d | -D] [-m] [<branch-name>]
git switch [-c] <branch-name>
git merge [--no-ff | --abort | --continue] <branch-name>
```

### Branch Operations Reference

| Command | Flags / Arguments | Legacy Equivalent | Description | 
| ----- | ----- | ----- | ----- | 
| `git branch` | *None* | — | List all local branches (`*` denotes the currently active branch). | 
| `git branch -a` | `-a` or `--all` | — | List both local branches and remote-tracking branches. | 
| `git branch <name>` | `<name>` | — | Create a new branch pointer at `HEAD` without switching to it. | 
| `git switch <name>` | `<name>` | `git checkout <name>` | Switch working directory to an existing branch `<name>`. | 
| `git switch -c <name>` | `-c` (create) | `git checkout -b <name>` | Create a new branch `<name>` and switch to it immediately. | 
| `git switch -` | `-` | `git checkout -` | Toggle back to the previously checked-out branch. | 
| `git branch -m <new-name>` | `-m` (move/rename) | — | Rename the currently active branch to `<new-name>`. | 
| `git branch -d <name>` | `-d` (safe delete) | — | Delete a branch only if its commits have already been merged upstream. | 
| `git branch -D <name>` | `-D` (force delete) | — | Force delete a branch even if it contains unmerged commits. | 

### Merging & Conflict Resolution Reference

| Command | Flags / Options | Description | 
| ----- | ----- | ----- | 
| `git merge <branch>` | `<branch>` | Join histories by merging `<branch>` into the **currently active** branch. | 
| `git merge --no-ff <branch>` | `--no-ff` | Force creation of a merge commit even if a fast-forward merge is possible. | 
| `git merge --abort` | `--abort` | Abort an active conflict resolution process and restore pre-merge state. | 
| `git merge --continue` | `--continue` | Conclude a merge after all conflicts have been manually resolved and staged (`git add`). | 

#### Conflict Marker Syntax (Inside Conflicted Files)

```
<<<<<<< HEAD
Current branch code (what you had locally before merging)
=======
Incoming branch code (what the branch being merged is trying to introduce)
>>>>>>> <incoming-branch-name>
```

*Resolution Workflow:* Edit file to remove `<<<<<<<`, `=======`, and `>>>>>>>` lines $\rightarrow$ Save file $\rightarrow$ `git add <file>` $\rightarrow$ `git commit`.

## 6. Remote Synchronization (`remote`, `fetch`, `pull`, `push`)

### Synopsis

```
git remote [-v] [add <name> <url>] [set-url <name> <new-url>]
git fetch [<remote>] [--prune]
git pull [--rebase] [<remote>] [<branch>]
git push [-u] [--force-with-lease] [<remote>] [<branch>]
```

### Remote Command Reference

| Command | Flags / Arguments | Description | 
| ----- | ----- | ----- | 
| `git remote -v` | `-v` (verbose) | List configured remote aliases (`origin`) along with their `fetch` and `push` URLs. | 
| `git remote add origin <url>` | `add <name> <url>` | Link a local repository to a remote host under the alias `origin`. | 
| `git remote set-url origin <url>` | `set-url <name> <url>` | Update the remote URL (e.g., when switching a repo from HTTPS to SSH). | 
| `git remote remove <name>` | `remove <name>` | Disconnect and remove a remote alias from local configuration. | 
| `git fetch origin` | `[--prune]` (`-p`) | Download objects and refs from `origin` without modifying local working files (`-p` removes dead remote branch references). | 
| `git pull origin <branch>` | `<remote> <branch>` | Fetch changes from remote branch and immediately `git merge` them into current branch. | 
| `git pull --rebase origin <branch>` | `--rebase` | Fetch changes from remote and replay local unpushed commits on top of them (keeps history linear). | 
| `git push -u origin <branch>` | `-u` (`--set-upstream`) | Upload `<branch>` to `origin` and link them so future `git push`/`git pull` commands need no arguments. | 
| `git push` | *None* | Upload local commits on the current branch to its tracked upstream remote branch. | 
| `git push --force-with-lease` | `--force-with-lease` | Safely overwrite remote history (aborts if a teammate pushed new commits you haven't fetched yet). | 
| `git push origin --delete <branch>` | `--delete` (`-d`) | Delete a branch on the remote server (`origin`). | 

## 7. Stashing Work (`git stash`)

Temporarily shelve uncommitted modifications so you can switch branches with a clean working directory.

### Synopsis

```
git stash [push [-u] [-m "<message>"]] [list | pop | apply | drop | clear]
```

### Stash Reference Table

| Command | Flags / Arguments | Description | 
| ----- | ----- | ----- | 
| `git stash` | *None* | Shelve tracked modifications from working directory and staging area onto the stash stack. | 
| `git stash push -u -m "<msg>"` | `-u` (untracked), `-m` | Shelve both tracked and **untracked** files with a descriptive label `<msg>`. | 
| `git stash list` | *None* | List all saved stash entries (`stash@{0}` is the newest). | 
| `git stash pop` | `[stash@{n}]` | Re-apply the latest stash entry to the working directory and delete it from the stash stack. | 
| `git stash apply` | `[stash@{n}]` | Re-apply a stash entry to the working directory while keeping a copy in the stash stack. | 
| `git stash drop` | `[stash@{n}]` | Delete a specific stash entry (defaults to `stash@{0}`). | 
| `git stash clear` | *None* | Permanently delete **all** stored stash entries. | 

## 8. Undoing, Restoring & Resetting (`restore`, `reset`, `revert`, `clean`, `reflog`)

### Synopsis

```
git restore [--staged] [--source=<commit>] <file>...
git reset [--soft | --mixed | --hard] [<commit>]
git revert <commit>
git clean [-f] [-d] [-n]
```

### File-Level Undo (`git restore` & `git rm` & `git mv`)

| Command | Flags / Arguments | Legacy Equivalent | Description | 
| ----- | ----- | ----- | ----- | 
| `git restore <file>` | `<file>` | `git checkout -- <file>` | **Destructive:** Discard unstaged local edits in `<file>`, restoring it to match `HEAD`. | 
| `git restore --staged <file>` | `--staged` (`-S`) | `git reset HEAD <file>` | **Safe:** Unstage `<file>` (moves from Staging Area back to Working Directory without losing edits). | 
| `git restore -s <commit> <file>` | `-s` (`--source`) | `git checkout <commit> -- <file>` | Overwrite working copy of `<file>` with the version from a specific historical `<commit>`. | 
| `git rm --cached <file>` | `--cached` (`-r` for dir) | — | Stop tracking `<file>` in Git (e.g., `.env`) while keeping the physical file on your disk. | 
| `git mv <old> <new>` | `<old-name> <new-name>` | — | Rename or move a tracked file and automatically stage the change. | 
| `git clean -nd` | `-n` (dry-run), `-d` (dirs) | — | Preview which untracked files and directories would be deleted. | 
| `git clean -fd` | `-f` (force), `-d` (dirs) | — | **Destructive:** Permanently delete all untracked files and folders from the Working Directory. | 

### Commit-Level Undo (`git reset`, `git revert`, `git reflog`)

| Command | Mode / Flag | Working Directory | Staging Area | Effect on Commit History | 
| ----- | ----- | ----- | ----- | ----- | 
| `git reset --soft HEAD~1` | `--soft` | **Preserved** | **Preserved (Staged)** | Moves `HEAD` back 1 commit; leaves changes staged ready to recommit. | 
| `git reset HEAD~1` | `--mixed` *(Default)* | **Preserved** | **Unstaged** | Moves `HEAD` back 1 commit; keeps edits in files but unstages them. | 
| `git reset --hard HEAD~1` | `--hard` | **DESTROYED** | **DESTROYED** | **Destructive:** Moves `HEAD` back 1 commit and permanently wipes all uncommitted edits. | 
| `git revert <commit-hash>` | `<commit-hash>` | Clean | Clean | **Safe for shared branches:** Creates a *new* commit that inverses the changes of `<commit-hash>`. | 
| `git reflog` | *None* | No change | No change | Displays chronological ledger of all local `HEAD` movements (use `git reset --hard <reflog-hash>` to recover lost commits). | 

## 9. Quick Troubleshooting & Emergency Reference

| Problem / Symptom | Command / Action | Explanation | 
| ----- | ----- | ----- | 
| **Trapped in Vim editor** (Terminal won't let you type commands after `git commit` or `git merge`) | Press `Esc` $\rightarrow$ type `:wq` $\rightarrow$ press `Enter` | Saves the default commit message and exits Vim (`:q!` exits without saving). | 
| **Stuck in `git log` or `git diff` output** (Bottom line shows `:` or `(END)`) | Press `q` | Exits the `less` terminal pager and returns to the shell prompt. | 
| **Committed to the wrong branch** (Haven't pushed yet) | `git branch <correct-branch>` $\rightarrow$ `git reset --hard HEAD~1` $\rightarrow$ `git switch <correct-branch>` | Copies the current state to a new branch, rewinds the current branch by 1 commit, and switches over. | 
| **Renamed `file.js` to `File.js`**, and Git ignores the change | `git mv file.js File.js` | Case-insensitive filesystems ignore capitalization changes; `git mv` forces the Git index to record the change. | 
| **Need quick CLI shortcuts** (Aliases) | `git config --global alias.<short> "<full-cmd>"` | E.g., `git config --global alias.st "status -sb"` lets you run `git st`. | 