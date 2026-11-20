# Linux Commands: Editors, Terminals and Dev Tools

Text editors, terminal multiplexers and sessions, build tools, help pages, printing and media.

Part of the [Linux commands cheat sheet](linux-commands-cheat-sheet-tables.md).

## Text Editors in Linux

**`nano` — Nano's ANOther editor:**

```bash
nano file.txt
```

**`vi` — Programmer's text editor:**

```bash
vi file.txt
```

**`vim` — Vi IMproved:**

```bash
vim file.txt
```

**`ed` — Line-oriented text editor:**

```bash
ed file.txt
```

**`emacs` — GNU project Emacs editor:**

```bash
emacs file.txt
```

### Nano Shortcuts Commands

| Category            | Shortcut   | Description                                                              |
| :------------------ | :--------- | :----------------------------------------------------------------------- |
| **File Operations** | `Ctrl + O` | Save (write) the current file                                            |
|                     | `Ctrl + X` | Exit Nano                                                                |
|                     | `Ctrl + R` | Read and insert another file                                             |
| **Navigation**      | `Ctrl + Y` | Scroll up one page                                                       |
|                     | `Ctrl + V` | Scroll down one page                                                     |
|                     | `Alt + \`  | Go to a specific line number                                             |
|                     | `Alt + ,`  | Move to the beginning of the current line                                |
|                     | `Alt + .`  | Move to the end of the current line                                      |
| **Editing**         | `Ctrl + K` | Cut/delete text from the cursor to the end of the line (or marked block) |
|                     | `Ctrl + U` | Uncut (paste) the last cut text                                          |
|                     | `Ctrl + 6` | Mark a block of text                                                     |
|                     | `Alt + 6`  | Copy the marked block                                                    |
|                     | `Ctrl + J` | Justify (format) the current paragraph                                   |
| **Search/Replace**  | `Ctrl + W` | Search for a string                                                      |
|                     | `Alt + W`  | Search and replace a string                                              |
|                     | `Alt + R`  | Repeat the last search                                                   |

### VI/VIM Shortcuts Commands

| Mode/Category        | Shortcut       | Description                                       |
| :------------------- | :------------- | :------------------------------------------------ |
| **Insert & Replace** | `i`            | Insert before cursor                              |
|                      | `a`            | Insert after cursor                               |
|                      | `A`            | Insert at the end of the line                     |
|                      | `o`            | Insert a new line below and switch to insert mode |
|                      | `R`            | Replace mode                                      |
|                      | `r`            | Replace single character                          |
|                      | `s`            | Substitute character                              |
|                      | `S`            | Delete line and substitute                        |
|                      | `C`            | Change to end of line                             |
| **Delete & Change**  | `x`            | Delete character                                  |
|                      | `dd`           | Delete line                                       |
|                      | `3dd`          | Delete 3 lines                                    |
|                      | `D`            | Delete to end of line                             |
|                      | `dw`           | Delete word                                       |
|                      | `4dw`          | Delete 4 words                                    |
|                      | `cw`           | Change word                                       |
| **Undo & Restore**   | `u`            | Undo                                              |
|                      | `U`            | Restore current line                              |
|                      | `~`            | Toggle case                                       |
|                      | `Esc`          | Exit mode                                         |
| **Normal Mode**      | `yy`           | Copy (yank) current line                          |
|                      | `p`            | Paste                                             |
|                      | `Ctrl + R`     | Redo                                              |
| **Command Mode**     | `:w`           | Save                                              |
|                      | `:q`           | Quit                                              |
|                      | `:q!`          | Quit without saving                               |
|                      | `:wq` or `:x`  | Save and quit                                     |
|                      | `:set nu`      | Show line numbers                                 |
|                      | `:s/old/new/g` | Replace in file                                   |
| **Visual Mode**      | `v`            | Select text                                       |
|                      | `y`            | Copy selected                                     |
|                      | `d`            | Delete selected                                   |
|                      | `p`            | Paste                                             |

## Terminal and Session Management Commands

**`agetty` — Alternative Linux getty:**

```bash
agetty tty1 9600
```

**`chvt` — Change foreground virtual terminal:**

```bash
chvt 3
```

**`reset` — Terminal initialization:**

```bash
reset
```

**`screen` — Screen manager with VT100/ANSI terminal emulation:**

```bash
screen -S mysession
```

**`showkey` — Examine the codes sent by the keyboard:**

```bash
showkey -a
```

**`stty` — Change and print terminal line settings:**

```bash
stty -a
```

**`tty` — Print the file name of the terminal connected to standard input:**

```bash
tty
```

**`xdg-open` — Opens a file or URL in the user's preferred application:**

```bash
xdg-open index.html
```

## Development and Build Automation Commands

**`aclocal` — Create aclocal.m4 by scanning configure.ac:**

```bash
aclocal
```

**`addr2line` — Convert addresses into file names and line numbers:**

```bash
addr2line -e myprog 0x400500
```

**`autoconf` — Generate configuration scripts:**

```bash
autoconf
```

**`autoheader` — Create a template header for configure:**

```bash
autoheader
```

**`automake` — Automatically create Makefile.in's from Makefile.am's:**

```bash
automake --add-missing
```

**`autoreconf` — Update generated configuration files:**

```bash
autoreconf -i
```

**`autoupdate` — Update a configure.ac to a newer Autoconf:**

```bash
autoupdate
```

**`bison` — GNU parser generator:**

```bash
bison -d parser.y
```

**`cc` — C compiler:**

```bash
cc main.c -o main
```

**`cpp` — The C Preprocessor:**

```bash
cpp main.c
```

**`ctags` — Generate tag files for source code:**

```bash
ctags -R .
```

**`g++` — GNU C++ compiler:**

```bash
g++ main.cpp -o main
```

**`gcc` — GNU C compiler:**

```bash
gcc main.c -o main
```

**`gdb` — The GNU Debugger:**

```bash
gdb ./myprog
```

**`ranlib` — Generate index to archive:**

```bash
ranlib libmy.a
```

**`readelf` — Displays information about ELF files:**

```bash
readelf -a myprog
```

## Help and Documentation Commands

**`apropos` — Search the manual page names and descriptions:**

```bash
apropos network
```

**`help` — Display information about builtin commands:**

```bash
help cd
```

**`info` — Read Info documents:**

```bash
info bash
```

**`man` — An interface to the system reference manuals:**

```bash
man ls
```

**`whatis` — Display one-line manual page descriptions:**

```bash
whatis ls
```

**`which` — Locate a command:**

```bash
which python
```

## Printing and Media Commands

**`amixer` — Command-line mixer for ALSA soundcard driver:**

```bash
amixer set Master 50%
```

**`aplay` — Command-line sound player for ALSA soundcard driver:**

```bash
aplay sound.wav
```

**`aplaymidi` — Standard MIDI File player for ALSA sequencer:**

```bash
aplaymidi -p 14:0 file.mid
```

**`cupsd` — Common UNIX Printing System daemon:**

```bash
systemctl restart cupsd
```

**`eject` — Eject removable media:**

```bash
eject /dev/cdrom
```

**`import` — Saves any visible window on an X server and outputs it as an image file:**

```bash
import screenshot.png
```
