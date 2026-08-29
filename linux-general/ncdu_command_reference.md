# How to hunt down large files and analyze disk usage using NCDU.

## Basic Usage

**Launch the disk usage analyzer in the current directory.**
```bash
ncdu
```

**Launch the disk usage analyzer for a specific directory.**
```bash
ncdu \
  /path/to/directory
```

**Scan the entire root file system (excluding other mounted file systems to prevent scanning external drives or network shares).**
```bash
ncdu \
  -x \
  /
```

## Advanced Scanning and Exporting

**Scan a directory quietly (reduces UI updates for faster scanning of large file systems).**
```bash
ncdu \
  -q \
  /path/to/directory
```

**Scan a directory and export the results to a file for later viewing.**
```bash
ncdu \
  -o \
  ncdu_export.file \
  /path/to/directory
```

**Load and view previously exported disk usage results.**
```bash
ncdu \
  -f \
  ncdu_export.file
```

**Scan a directory with extended information (enables extended mode).**
```bash
ncdu \
  -e \
  /path/to/directory
```

**Scan a directory and enable color output (if supported by terminal).**
```bash
ncdu \
  --color \
  dark \
  /path/to/directory
```

## Interactive UI Keybindings (Inside NCDU)

**Delete the currently selected file or directory.**
```text
d
```

**Toggle the display of hidden files.**
```text
h
```

**Sort the list by file/directory name.**
```text
n
```

**Sort the list by disk usage size.**
```text
s
```

**Toggle between displaying apparent size and disk usage.**
```text
a
```

**Show information about the currently selected item.**
```text
i
```

**Quit the application.**
```text
q
```
