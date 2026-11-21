# GitHub Terminal Setup Guide

Step-by-step guide to setting up Git and the GitHub CLI in a terminal, connecting your GitHub account, and creating new repositories or adding existing ones.

Follow the steps in order on a new computer. Steps 1–3 are done once per computer; steps 4–7 are what you do for each repository.

---

## 1. Install Git and the GitHub CLI

You need two tools: **`git`** (version control) and **`gh`** (the GitHub CLI, which logs you in and creates repositories from the terminal).

```bash
# Fedora
sudo dnf install git gh

# RHEL / Rocky / AlmaLinux: add the official GitHub CLI repository
sudo dnf install 'dnf-command(config-manager)' && sudo dnf config-manager --add-repo https://cli.github.com/packages/rpm/gh-cli.repo && sudo dnf install git gh

# Debian / Ubuntu (distro package; the official repository on cli.github.com is newer)
sudo apt install git gh

# Arch Linux
sudo pacman -S git github-cli

# macOS (Homebrew)
brew install git gh

# Windows (PowerShell)
winget install --id Git.Git -e && winget install --id GitHub.cli -e
```

Check both are installed:

```bash
git --version
gh --version
```

---

## 2. Set Your Git Identity

Every commit records a name and email address. Set them once:

```bash
git config --global user.name "Your Name"
git config --global user.email "ID+username@users.noreply.github.com"
```

### Keep Your Real Email Private

GitHub gives every account a private **noreply** address. Find yours at **GitHub → Settings → Emails** (it looks like `12345678+username@users.noreply.github.com`) and use it as `user.email` above. Also tick **Keep my email addresses private** and **Block command line pushes that expose my email** on the same page.

### Recommended Defaults

```bash
# New repositories start on "main"
git config --global init.defaultBranch main

# Editor for commit messages (pick one)
git config --global core.editor "nano"
git config --global core.editor "code --wait"

# "git pull" rebases your local commits instead of creating merge commits
git config --global pull.rebase true

# Check the result
git config --global --list
```

---

## 3. Connect Your GitHub Account

Pick **one** method. Option A is the easiest and works on every system.

### Option A: GitHub CLI Login (Recommended)

```bash
gh auth login
```

Answer the prompts:

1. **Where do you use GitHub?** → `GitHub.com`
2. **Preferred protocol for Git operations?** → `HTTPS` (simplest) or `SSH`
3. **Authenticate Git with your GitHub credentials?** (HTTPS only) → `Yes`
4. **How would you like to authenticate?** → `Login with a web browser`
5. Copy the one-time code, press Enter, paste the code in the browser, and approve.

Choosing **SSH** in step 2 makes `gh` find your existing SSH key, or offer to create one, and upload it to your account for you.

Check that it worked:

```bash
gh auth status
```

With HTTPS, `gh` is now Git's credential helper, so `git push` and `git pull` won't ask for a password. If you logged in another way (for example with `--with-token`), set that up manually:

```bash
gh auth setup-git
```

### Option B: SSH Key Only (Without the GitHub CLI)

```bash
# 1. Create a key (press Enter for the default path; set a passphrase)
ssh-keygen -t ed25519 -C "your-laptop-name"

# 2. Start the agent and add the key
eval "$(ssh-agent -s)" && ssh-add ~/.ssh/id_ed25519

# 3. Print the public key and copy it
cat ~/.ssh/id_ed25519.pub
```

Add it to your account: on GitHub, go to **Settings → SSH and GPG keys → New SSH key**, paste the key, and save. Then test the connection:

```bash
ssh -T git@github.com
```

You should see `Hi username! You've successfully authenticated, but GitHub does not provide shell access.`

If you already use `gh`, you can add the key from the terminal instead of the website:

```bash
gh ssh-key add ~/.ssh/id_ed25519.pub --title "your-laptop-name"
```

If that fails with a permissions error, grant the extra scope first: `gh auth refresh -h github.com -s admin:public_key`.

> **Passwords don't work for Git.** GitHub no longer accepts your account password for `git push` over HTTPS. Use `gh auth login`, an SSH key, or a personal access token.

---

## 4. Create a New Repository

### A. Brand-New Project (Nothing Exists Yet)

Create the repository on GitHub and clone it in one step:

```bash
cd ~/projects
gh repo create my-new-project --public --clone --add-readme --description "What this project is"
cd my-new-project
```

Use `--private` instead of `--public` for a private repository. Add `--license mit` or `--gitignore Python` to start with those files.

### B. Turn an Existing Local Folder into a GitHub Repository

For a project folder already on your computer that isn't on GitHub yet:

```bash
cd ~/projects/existing-folder

# 1. Start tracking it with Git (skip if it already has a .git folder)
git init

# 2. Make the first commit
git add .
git commit -m "Initial commit"

# 3. Create the GitHub repository from this folder and push it
gh repo create existing-folder --private --source=. --remote=origin --push
```

Check what you're about to commit before step 2 with `git status`. Add a `.gitignore` first so build files, `.env` files, and secrets stay out of the repository.

### C. Without the GitHub CLI (Using the Website)

1. On GitHub, click **+ → New repository**, enter a name, and **leave "Add a README" unticked** so the repository is empty.
2. Connect your local folder and push:

```bash
cd ~/projects/existing-folder
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin git@github.com:username/existing-folder.git
git push -u origin main
```

Use `https://github.com/username/existing-folder.git` as the remote URL if you connected with HTTPS instead of SSH.

---

## 5. Add an Existing GitHub Repository to Your Computer

### Clone One of Your Repositories

```bash
# List your repositories
gh repo list

# Clone by name (uses the protocol you chose at login)
gh repo clone username/repository-name

# Or with plain git
git clone git@github.com:username/repository-name.git
git clone https://github.com/username/repository-name.git
```

### Clone Into a Specific Folder

```bash
gh repo clone username/repository-name ~/projects/my-folder
```

### Fork and Clone Someone Else's Repository

```bash
gh repo fork owner/repository-name --clone
```

This creates a copy under your account, clones it, and adds the original as the `upstream` remote so you can pull their updates.

### Clone All Your Repositories at Once

```bash
gh repo list username --limit 200 --json name --jq '.[].name' | xargs -I{} gh repo clone username/{}
```

---

## 6. Connect a Local Repository to an Existing GitHub Repository

For a local repository that should push to a GitHub repository that already exists:

```bash
# See current remotes
git remote -v

# Add GitHub as "origin"
git remote add origin git@github.com:username/repository-name.git

# First push: set origin/main as the upstream branch
git push -u origin main
```

If the GitHub repository already has commits (for example a README created on the website), pull them first:

```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

### Switch Between HTTPS and SSH

```bash
# To SSH
git remote set-url origin git@github.com:username/repository-name.git

# To HTTPS
git remote set-url origin https://github.com/username/repository-name.git
```

---

## 7. Everyday Workflow

```bash
# Get the latest changes
git pull

# See what changed
git status
git diff

# Save and upload your work
git add .
git commit -m "Describe the change"
git push

# Work on a separate branch and open a pull request
git switch -c fix-typo
git add . && git commit -m "Fix typo in README"
git push -u origin fix-typo
gh pr create --fill

# Open the repository in your browser
gh repo view --web
```

For the full set of Git commands, see the [Git Command-Line Reference Guide](git-command-line-guide.md).

---

## 8. Optional: Sign Your Commits with SSH

Signed commits show a **Verified** badge on GitHub.

```bash
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true

# Upload the same key as a signing key
gh ssh-key add ~/.ssh/id_ed25519.pub --type signing --title "your-laptop-name signing"
```

---

## 9. Managing Accounts

```bash
# Which account and protocol are in use?
gh auth status

# Add a second account (for example work and personal)
gh auth login

# Switch the active account
gh auth switch

# Log out
gh auth logout
```

To use a different name or email in one repository only, run the `git config` commands from step 2 **without** `--global` inside that repository.

---

## 10. Troubleshooting

| Error | Fix |
| --- | --- |
| `Permission denied (publickey)` | SSH key not loaded or not on GitHub: run `ssh-add -l`, then `ssh -T git@github.com`; re-add the key in Settings |
| `Support for password authentication was removed` | Use `gh auth login` (HTTPS) or switch the remote to SSH |
| `remote: Repository not found` | Wrong URL or no access: check `git remote -v` and `gh auth status` for the right account |
| `! [rejected] main -> main (fetch first)` | GitHub has commits you don't: run `git pull` then `git push` |
| `refusing to merge unrelated histories` | Local and GitHub repositories both have a first commit: `git pull origin main --allow-unrelated-histories` |
| `GH007: Your push would publish a private email address` | Set `user.email` to your noreply address, then `git commit --amend --reset-author` |
| `fatal: not a git repository` | You're not inside the repository folder, or you haven't run `git init` |
| `src refspec main does not match any` | No commits yet, or the branch is `master`: commit first, or run `git branch -M main` |
| `gh: command not found` | GitHub CLI isn't installed (step 1) |

---

## Quick Reference

```bash
gh auth login                                        # connect account
gh auth status                                       # check login
git config --global user.name "Name"                 # set identity
gh repo create name --public --clone                 # new repo, cloned
gh repo create name --private --source=. --push      # existing folder → new GitHub repo
gh repo clone username/repo                          # existing GitHub repo → computer
git remote add origin git@github.com:user/repo.git   # link local repo to GitHub
git push -u origin main                              # first push
ssh -T git@github.com                                # test SSH
```

---

## Sources & Verification

- **GitHub CLI commands:** [GitHub CLI manual](https://cli.github.com/manual/)
- **Git configuration:** [git-config documentation](https://git-scm.com/docs/git-config)

## Related guides

- [Git Command-Line Reference Guide](git-command-line-guide.md)
- [Back Up Dotfiles with Git](git-dotfiles-maintenance-cheat-sheet.md)
- [SSH and sshd Hardening Cheat Sheet](../networking-and-security/security/ssh-hardening-cheat-sheet.md)
