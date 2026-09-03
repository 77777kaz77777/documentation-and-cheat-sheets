# How to make a Bash script executable and run it from anywhere on the system

Follow these steps to make a Bash script executable and runnable from anywhere using a simple custom command like `update`.

---

## 1. Create Your Script

Write your Bash script and save it with a `.sh` extension (e.g., `update.sh`):

```bash
#!/bin/bash
echo "Updating the system..."
sudo dnf update && sudo dnf upgrade -y
```

## 2. Make the Script Executable

Grant execution permissions to the script:

```bash
chmod +x update.sh
```

## 3. Move the Script to a Directory in `PATH`

Place the script in a directory included in your system's `PATH` (such as `/usr/local/bin` or `/usr/bin`) to make it globally accessible:

```bash
sudo mv update.sh /usr/local/bin/update
```

Now you can run the script from any terminal directory simply by typing `update`.

## 4. Verify Your `PATH` (Optional)

If `/usr/local/bin` is not already in your `PATH`, add it by editing your shell configuration file (`~/.bashrc`, `~/.zshrc`, etc.):

```bash
export PATH=$PATH:/usr/local/bin
```

Reload the configuration file to apply changes:

```bash
source ~/.bashrc
```

## 5. Test the Command

Run your new custom command:

```bash
update
```
