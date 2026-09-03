
# How to properly set and manage environment variables using the export command

The `export` command is a built-in shell utility in Bash, Zsh, and POSIX-compliant shells. It converts local shell variables into environment variables, making them accessible to child processes spawned by that shell.

---

## 🧠 Core Architecture: Shell Variables vs. Environment Variables

- **Local Shell Variables:** Stored inside the shell's internal symbol table. They exist only within the current shell session and are **not** passed down to scripts or sub-processes.
- **Environment Variables:** Stored in the process environment array (`environ`). When a process spawns a child process via `fork()` or `exec()`, the kernel copies this environment array to the child.

### Example 1: Local vs. Exported Variable Inheritance

```bash
# Define a local shell variable (not exported)
MY_LOCAL="Hidden from child"

# Define and export an environment variable
export MY_EXPORT="Visible to child"

# Spawn a child subshell and attempt to print both variables
bash -c 'echo "Local: $MY_LOCAL \vert{} Export:$MY_EXPORT"'
# Output: Local:  | Export: Visible to child
