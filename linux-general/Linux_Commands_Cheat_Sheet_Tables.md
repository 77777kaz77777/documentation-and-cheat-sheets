# Linux Commands Cheat Sheet (Tabular Format)

## 1. File Operations Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `access` | Check read, write, and execute permissions | `access -r file.txt` |
| `basename` | Strip directory and suffix from filenames | `basename /var/log/syslog` |
| `cat` | Concatenate files and print on the standard output | `cat file.txt` |
| `cksum` | Print CRC checksum and byte count | `cksum file.txt` |
| `cmp` | Compare two files byte by byte | `cmp file1.txt file2.txt` |
| `compress` | Compress data into .Z format | `compress file.txt` |
| `cp` | Copy files and directories | `cp source.txt dest.txt` |
| `cpio` | Copy files to and from archives | `find . -name "*.txt" &#124; cpio -o > archive.cpio` |
| `csplit` | Split a file into context-determined pieces | `csplit file.txt /pattern/` |
| `cut` | Remove sections from each line of files | `cut -d',' -f1 file.csv` |
| `diff` | Find differences between two files | `diff file1.txt file2.txt` |
| `diff3` | Compare three files line by line | `diff3 file1.txt file2.txt file3.txt` |
| `echo` | Display a line of text | `echo "Hello World"` |
| `expand` | Convert tabs to spaces | `expand -t 4 file.txt` |
| `file` | Determine file type | `file archive.tar.gz` |
| `fold` | Wrap each input line to fit in specified width | `fold -w 80 file.txt` |
| `head` | Output the first part of files | `head -n 10 file.txt` |
| `join` | Join lines of two files on a common field | `join file1.txt file2.txt` |
| `less` | View file contents interactively (allows backward movement) | `less file.txt` |
| `ln` | Make links between files (hard or symbolic) | `ln -s /path/to/target linkname` |
| `locate` | Find files by name using a database | `locate my_script.sh` |
| `look` | Display lines beginning with a given string | `look "word" file.txt` |
| `more` | File perusal filter for viewing one screen at a time | `more file.txt` |
| `mv` | Move or rename files and directories | `mv oldname.txt newname.txt` |
| `od` | Dump files in octal and other formats | `od -c file.txt` |
| `paste` | Merge lines of files side-by-side | `paste file1.txt file2.txt` |
| `readlink` | Print resolved symbolic link or canonical file name | `readlink -f /path/to/symlink` |
| `rename` | Rename multiple files using regular expressions | `rename 's/\.htm$/.html/' *.htm` |
| `rev` | Reverse the order of characters in every line | `rev file.txt` |
| `rm` | Remove files or directories | `rm -rf directory/` |
| `shred` | Overwrite a file to hide its contents, and optionally delete it | `shred -u secret.txt` |
| `sort` | Sort lines of text files | `sort file.txt` |
| `split` | Split a file into pieces | `split -l 100 file.txt` |
| `tac` | Concatenate and print files in reverse order (last line first) | `tac file.txt` |
| `tail` | Output the last part of files | `tail -f /var/log/messages` |
| `tar` | Store and extract files from an archive | `tar -czvf archive.tar.gz folder/` |
| `tee` | Read from standard input and write to standard output and files | `echo "data" &#124; tee output.txt` |
| `touch` | Change file timestamps or create an empty file | `touch newfile.txt` |
| `unexpand` | Convert spaces to tabs | `unexpand -a file.txt` |
| `uniq` | Report or omit repeated lines | `uniq file.txt` |
| `wc` | Print newline, word, and byte counts for each file | `wc -l file.txt` |

## 2. Directory Operations Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `cd` | Change the shell working directory | `cd /var/log` |
| `dir` | List directory contents (similar to ls) | `dir -l` |
| `dirname` | Strip non-directory suffix from file name | `dirname /var/log/syslog` |
| `dirs` | Display list of currently remembered directories | `dirs -v` |
| `du` | Estimate file and directory space usage | `du -sh /home/user/` |
| `find` | Search for files in a directory hierarchy | `find / -name "*.conf"` |
| `lsblk` | List information about block devices | `lsblk` |
| `mkdir` | Make directories | `mkdir -p /tmp/newdir/subdir` |
| `mount` | Mount a filesystem | `mount /dev/sda1 /mnt` |
| `pwd` | Print name of current/working directory | `pwd` |
| `rmdir` | Remove empty directories | `rmdir emptydir/` |
| `tree` | List contents of directories in a tree-like format | `tree /etc` |

## 3. File Permission and Ownership Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `chmod` | Change file mode bits (permissions) | `chmod 755 script.sh` |
| `chattr` | Change file attributes on a Linux file system | `chattr +i file.txt` |
| `chown` | Change file owner and group | `chown user:group file.txt` |
| `chgrp` | Change group ownership | `chgrp wheel file.txt` |

## 4. User Management Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `chage` | Change user password expiry information | `chage -l username` |
| `chfn` | Change real user name and information | `chfn username` |
| `chsh` | Change login shell | `chsh -s /bin/zsh username` |
| `chpasswd` | Update passwords in batch mode | `echo "user:newpass" &#124; chpasswd` |
| `finger` | User information lookup program | `finger username` |
| `id` | Print real and effective user and group IDs | `id username` |
| `passwd` | Change user password | `passwd username` |
| `pinky` | Lightweight finger program | `pinky -l username` |
| `useradd` | Create a new user or update default new user information | `useradd -m newuser` |
| `userdel` | Delete a user account and related files | `userdel -r olduser` |
| `usermod` | Modify a user account | `usermod -aG wheel username` |
| `users` | Print the user names of users currently logged in | `users` |
| `who` | Show who is logged on | `who` |
| `whoami` | Print effective userid | `whoami` |

## 5. Group Management Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `groupadd` | Create a new group | `groupadd developers` |
| `groupdel` | Delete a group | `groupdel developers` |
| `groupmod` | Modify a group definition | `groupmod -n devs developers` |
| `groups` | Print the groups a user is in | `groups username` |
| `gpasswd` | Administer /etc/group and /etc/gshadow | `gpasswd -a username developers` |
| `grpck` | Verify integrity of group files | `grpck` |
| `grpconv` | Create shadow group file from group file | `grpconv` |

## 6. Process Management Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `accton` | Turn process accounting on or off | `accton /var/account/pacct` |
| `bg` | Put a job in the background | `bg %1` |
| `chrt` | Manipulate the real-time attributes of a process | `chrt -p 1234` |
| `fg` | Bring a job to the foreground | `fg %1` |
| `kill` | Send a signal to a process | `kill -9 1234` |
| `mpstat` | Report processors related statistics | `mpstat -P ALL 1` |
| `pidof` | Find the process ID of a running program | `pidof sshd` |
| `pmap` | Report memory map of a process | `pmap 1234` |
| `ps` | Report a snapshot of the current processes | `ps aux` |
| `top` | Display Linux processes dynamically | `top` |
| `htop` | Interactive process viewer | `htop` |
| `strace` | Trace system calls and signals | `strace -p 1234` |
| `time` | Run programs and summarize system resource usage | `time ls -l` |
| `watch` | Execute a program periodically, showing output fullscreen | `watch -n 1 free -m` |
| `vmstat` | Report virtual memory statistics | `vmstat 1 5` |
| `uptime` | Tell how long the system has been running | `uptime` |
| `w` | Show who is logged on and what they are doing | `w` |

## 7. Networking Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `arp` | Manipulate the system ARP cache | `arp -a` |
| `curl` | Transfer a URL | `curl -O http://example.com/file.zip` |
| `host` | DNS lookup utility | `host example.com` |
| `hostid` | Print the numeric identifier for the current host | `hostid` |
| `hostname` | Show or set the system's host name | `hostname` |
| `hostnamectl` | Control the system hostname | `hostnamectl set-hostname server1` |
| `ifconfig` | Configure a network interface | `ifconfig eth0` |
| `iftop` | Display bandwidth usage on an interface | `iftop -i eth0` |
| `ifup` | Bring a network interface up | `ifup eth0` |
| `ip` | Show / manipulate routing, network devices, interfaces and tunnels | `ip addr show` |
| `ipcrm` | Remove a message queue, semaphore set, or shared memory id | `ipcrm -m 1234` |
| `ipcs` | Provide information on ipc facilities | `ipcs -m` |
| `iptables` | Administration tool for IPv4 packet filtering and NAT | `iptables -L` |
| `iptables-save` | Dump iptables rules to stdout | `iptables-save > /etc/iptables/rules.v4` |
| `iwconfig` | Configure a wireless network interface | `iwconfig wlan0` |
| `nc` (`netcat`) | Arbitrary TCP and UDP connections and listens | `nc -lvp 8080` |
| `netstat` | Print network connections, routing tables, interface statistics, etc. | `netstat -tuln` |
| `nmcli` | Command-line tool for controlling NetworkManager | `nmcli connection show` |
| `nslookup` | Query Internet name servers interactively | `nslookup example.com` |
| `ping` | Send ICMP ECHO_REQUEST to network hosts | `ping 8.8.8.8` |
| `rcp` | Remote file copy | `rcp file.txt host:/tmp/` |
| `route` | Show / manipulate the IP routing table | `route -n` |
| `rsync` | Fast, versatile, remote (and local) file-copying tool | `rsync -avz /local/dir/ user@remote:/remote/dir/` |
| `scp` | Secure copy | `scp file.txt user@remote:/tmp/` |
| `ssh` | OpenSSH SSH client | `ssh user@remote` |
| `tracepath` | Traces path to a network host discovering MTU | `tracepath 8.8.8.8` |
| `traceroute` | Print the route packets trace to network host | `traceroute example.com` |
| `vnstat` | Console-based network traffic monitor | `vnstat -i eth0` |
| `wget` | The non-interactive network downloader | `wget http://example.com/file.iso` |

## 8. Job Scheduling Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `atd` | Job spooling daemon | `systemctl status atd` |
| `atrm` | Remove jobs spooled by at | `atrm 1` |
| `atq` | Lists the user's pending jobs | `atq` |
| `batch` | Execute commands when system load levels permit | `echo "sh ./script.sh" &#124; batch` |
| `cron` | Daemon to execute scheduled commands | `systemctl status crond` |
| `crontab` | Maintain crontab files for individual users | `crontab -e` |

## 9. Disk and File System Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `cfdisk` | Display or manipulate disk partition table | `cfdisk /dev/sda` |
| `df` | Report file system disk space usage | `df -h` |
| `dosfsck` | Check and repair MS-DOS file systems | `dosfsck /dev/sdb1` |
| `dump` | ext2/3/4 filesystem backup | `dump -0u -f /tmp/backup.dump /dev/sda1` |
| `dumpe2fs` | Dump ext2/3/4 filesystem information | `dumpe2fs /dev/sda1` |
| `fdisk` | Manipulate disk partition table | `fdisk -l` |
| `mount` | Mount a filesystem | `mount /dev/sda1 /mnt` |
| `restore` | Restore files or file systems from backups made with dump | `restore -r -f /tmp/backup.dump` |
| `sync` | Synchronize cached writes to persistent storage | `sync` |

## 10. Hardware and System Information Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `acpi` | Show battery status and other ACPI information | `acpi -V` |
| `acpi_available` | Test whether ACPI subsystem is available | `acpi_available` |
| `acpid` | Advanced Configuration and Power Interface event daemon | `systemctl restart acpid` |
| `arch` | Print machine hardware name | `arch` |
| `dmesg` | Print or control the kernel ring buffer | `dmesg -T` |
| `dmidecode` | DMI table decoder | `dmidecode -t memory` |
| `dstat` | Versatile resource statistics tool | `dstat` |
| `free` | Display amount of free and used memory in the system | `free -m` |
| `hdparm` | Get/set SATA/IDE device parameters | `hdparm -tT /dev/sda` |
| `hwclock` | Query or set the hardware clock | `hwclock --show` |
| `iostat` | Report CPU and input/output statistics for devices | `iostat -x 1` |
| `iotop` | Simple top-like I/O monitor | `iotop` |
| `lsusb` | List USB devices | `lsusb` |
| `lshw` | Extract detailed information on the hardware configuration | `lshw -short` |
| `uname` | Print system information | `uname -a` |

## 11. Compression and Archiving Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `ar` | Create, modify, and extract from archives | `ar rcs lib.a obj1.o obj2.o` |
| `bzcmp` | Compare bzip2 compressed files | `bzcmp file1.bz2 file2.bz2` |
| `bzdiff` | Compare bzip2 compressed files | `bzdiff file1.bz2 file2.bz2` |
| `bzgrep` | Search bzip2 compressed files for a regular expression | `bzgrep "search" file.bz2` |
| `bzip2` | A block-sorting file compressor | `bzip2 file.txt` |
| `bzless` | File perusal filter for crt viewing of bzip2 compressed text | `bzless file.bz2` |
| `bzmore` | File perusal filter for crt viewing of bzip2 compressed text | `bzmore file.bz2` |
| `gunzip` | Compress or expand files | `gunzip file.gz` |
| `gzip` | Compress or expand files | `gzip file.txt` |
| `gzexe` | Compress executable files in place | `gzexe script.sh` |
| `zip` | Package and compress files | `zip -r archive.zip folder/` |
| `zdiff` | Compare compressed files | `zdiff file1.gz file2.gz` |
| `zgrep` | Search possibly compressed files for a regular expression | `zgrep "search" file.gz` |

## 12. Text Processing and Formatting Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `awk` | Pattern scanning and processing language | `awk '{print $1}' file.txt` |
| `aspell` | Interactive spell checker | `aspell check file.txt` |
| `banner` | Print large banner on printer/stdout | `banner Hello` |
| `bc` | An arbitrary precision calculator language | `echo "10 + 5" &#124; bc` |
| `col` | Filter reverse line feeds from input | `man ls &#124; col -b > ls.txt` |
| `colcrt` | Filter nroff output for CRT previewing | `colcrt file.txt` |
| `colrm` | Remove columns from a file | `colrm 1 5 < file.txt` |
| `column` | Columnate lists | `mount &#124; column -t` |
| `dc` | An arbitrary precision calculator | `dc -e '10 5 + p'` |
| `egrep` | Print lines matching a pattern (grep -E) | `egrep "pattern1&#124;pattern2" file.txt` |
| `fgrep` | Print lines matching a pattern (grep -F) | `fgrep "exact string" file.txt` |
| `fmt` | Simple optimal text formatter | `fmt -w 60 file.txt` |
| `grep` | Print lines matching a pattern | `grep "error" /var/log/syslog` |
| `sdiff` | Side-by-side merge of file differences | `sdiff file1.txt file2.txt` |
| `sed` | Stream editor for filtering and transforming text | `sed 's/old/new/g' file.txt` |
| `tr` | Translate or delete characters | `cat file.txt &#124; tr 'a-z' 'A-Z'` |
| `unix2dos` | UNIX to DOS text file format converter | `unix2dos file.txt` |

## 13. Kernel and Module Management Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `depmod` | Generate modules.dep and map files | `depmod -a` |
| `insmod` | Insert a module into the Linux Kernel | `insmod module.ko` |
| `lsmod` | Show the status of modules in the Linux Kernel | `lsmod` |
| `modinfo` | Show information about a Linux Kernel module | `modinfo e1000e` |
| `rmmod` | Remove a module from the Linux Kernel | `rmmod module_name` |
| `systemctl` | Control the systemd system and service manager | `systemctl status network` |

## 14. System Control and Power Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `halt` | Instruct the hardware to stop all CPU functions | `halt` |
| `poweroff` | Power off the system | `poweroff` |
| `reboot` | Reboot the system | `reboot` |
| `shutdown` | Halt, power-off or reboot the machine | `shutdown -h now` |

## 15. Logging and Monitoring Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `journalctl` | Query the systemd journal | `journalctl -u sshd -f` |
| `last` | Show listing of last logged in users | `last username` |
| `history` | GNU History Library (show previous commands) | `history &#124; grep command` |
| `sar` | Collect, report, or save system activity information | `sar -u 1 3` |
| `script` | Make typescript of terminal session | `script session.log` |
| `scriptreplay` | Play back typescripts, using timing information | `scriptreplay timing.log session.log` |

## 16. Checksum and File Integrity Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `md5sum` | Compute and check MD5 message digest | `md5sum file.iso` |
| `cksum` | Print CRC checksum and byte counts | `cksum file.txt` |
| `sum` | Checksum and count the blocks in a file | `sum file.txt` |

## 17. Date and Time Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `cal` | Displays a calendar | `cal 2026` |
| `date` | Print or set the system date and time | `date "+%Y-%m-%d %H:%M:%S"` |
| `uptime` | Tell how long the system has been running | `uptime` |

## 18. Mail and User Communication Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `biff` | Be notified if mail arrives and who it is from | `biff y` |
| `mailq` | Print the mail queue | `mailq` |
| `write` | Send a message to another user | `write username` |
| `wall` | Send a message to everybody's terminal | `wall "System will go down in 10 minutes"` |

## 19. Printing and Media Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `amixer` | Command-line mixer for ALSA soundcard driver | `amixer set Master 50%` |
| `aplay` | Command-line sound player for ALSA soundcard driver | `aplay sound.wav` |
| `aplaymidi` | Standard MIDI File player for ALSA sequencer | `aplaymidi -p 14:0 file.mid` |
| `cupsd` | Common UNIX Printing System daemon | `systemctl restart cupsd` |
| `eject` | Eject removable media | `eject /dev/cdrom` |
| `import` | Saves any visible window on an X server and outputs it as an image file | `import screenshot.png` |

## 20. Shell Built-in and Scripting Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `alias` | Define or display aliases | `alias ll='ls -l'` |
| `bind` | Set Readline key bindings and variables | `bind -P` |
| `break` | Exit from a for, while, or until loop | `break` |
| `builtin` | Run a shell builtin, passing it args | `builtin cd /tmp` |
| `case` | Conditional construct in shell scripts | `case $VAR in ... esac` |
| `continue` | Resume the next iteration of a loop | `continue` |
| `declare` | Set variables and attributes | `declare -i NUM=5` |
| `enable` | Enable and disable shell builtins | `enable -n cd` |
| `env` | Set environment and execute command, or print environment | `env &#124; grep USER` |
| `eval` | Construct command by concatenating arguments | `eval "ls -l"` |
| `exec` | Replace the shell with the given command | `exec bash` |
| `exit` | Exit the shell | `exit 0` |
| `expect` | Programmed dialogue with interactive programs | `expect script.exp` |
| `export` | Set export attribute for shell variables | `export PATH=$PATH:/new/dir` |
| `expr` | Evaluate expressions | `expr 5 + 3` |
| `factor` | Print the prime factors | `factor 100` |
| `fc` | Process command history list | `fc -l` |
| `function` | Define shell functions | `function myfunc() { echo "hi"; }` |
| `for` | Loop construct | `for i in {1..5}; do echo $i; done` |
| `if` | Conditional construct | `if [ -f file ]; then echo "Exists"; fi` |
| `let` | Evaluate arithmetic expressions | `let "a = 5 + 3"` |
| `printf` | Format and print data | `printf "Result: %04d
" 42` |
| `read` | Read a line from standard input | `read -p "Enter name: " name` |
| `return` | Return from a shell function | `return 1` |
| `select` | Generate menus from list of words | `select opt in "A" "B"; do echo $opt; break; done` |
| `seq` | Print a sequence of numbers | `seq 1 5` |
| `setsid` | Run a program in a new session | `setsid my_script.sh` |
| `shift` | Shift positional parameters | `shift 2` |
| `source` | Execute commands from a file in the current shell | `source ~/.bashrc` |
| `type` | Display information about command type | `type ls` |
| `until` | Loop construct | `until [ $i -gt 5 ]; do ... done` |
| `while` | Loop construct | `while true; do ... done` |
| `yes` | Output a string repeatedly until killed | `yes "y" &#124; rm -r dir/` |
| `sudo` | Execute a command as another user | `sudo dnf update` |
| `sleep` | Delay for a specified amount of time | `sleep 5` |

## 21. Bash Shortcuts Commands

### Navigation Shortcuts

| Shortcut | Description |
| :--- | :--- |
| `Ctrl + A` | Move to the beginning of the line |
| `Ctrl + E` | Move to the end of the line |
| `Ctrl + B` | Move back one character |
| `Ctrl + F` | Move forward one character |
| `Alt + B` | Move back one word |
| `Alt + F` | Move forward one word |

### Editing Shortcuts

| Shortcut | Description |
| :--- | :--- |
| `Ctrl + U` | Cut/delete text from the cursor to the beginning of the line |
| `Ctrl + K` | Cut/delete text from the cursor to the end of the line |
| `Ctrl + W` | Cut/delete the word before the cursor |
| `Ctrl + Y` | Paste the last cut text |
| `Ctrl + L` | Clear the terminal screen |
| `Ctrl + C` | Terminate the currently running command |

### History Shortcuts

| Shortcut | Description |
| :--- | :--- |
| `Ctrl + R` | Search command history (reverse search) |
| `Ctrl + G` | Exit history search mode |
| `Ctrl + P` | Go to the previous command in history |
| `Ctrl + N` | Go to the next command in history |

## 22. Development and Build Automation Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `aclocal` | Create aclocal.m4 by scanning configure.ac | `aclocal` |
| `addr2line` | Convert addresses into file names and line numbers | `addr2line -e myprog 0x400500` |
| `autoconf` | Generate configuration scripts | `autoconf` |
| `autoheader` | Create a template header for configure | `autoheader` |
| `automake` | Automatically create Makefile.in's from Makefile.am's | `automake --add-missing` |
| `autoreconf` | Update generated configuration files | `autoreconf -i` |
| `autoupdate` | Update a configure.ac to a newer Autoconf | `autoupdate` |
| `bison` | GNU parser generator | `bison -d parser.y` |
| `cc` | C compiler | `cc main.c -o main` |
| `cpp` | The C Preprocessor | `cpp main.c` |
| `ctags` | Generate tag files for source code | `ctags -R .` |
| `g++` | GNU C++ compiler | `g++ main.cpp -o main` |
| `gcc` | GNU C compiler | `gcc main.c -o main` |
| `gdb` | The GNU Debugger | `gdb ./myprog` |
| `ranlib` | Generate index to archive | `ranlib libmy.a` |
| `readelf` | Displays information about ELF files | `readelf -a myprog` |

## 23. Terminal and Session Management Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `agetty` | Alternative Linux getty | `agetty tty1 9600` |
| `chvt` | Change foreground virtual terminal | `chvt 3` |
| `reset` | Terminal initialization | `reset` |
| `screen` | Screen manager with VT100/ANSI terminal emulation | `screen -S mysession` |
| `showkey` | Examine the codes sent by the keyboard | `showkey -a` |
| `stty` | Change and print terminal line settings | `stty -a` |
| `tty` | Print the file name of the terminal connected to standard input | `tty` |
| `xdg-open` | Opens a file or URL in the user's preferred application | `xdg-open index.html` |

## 24. Help and Documentation Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `apropos` | Search the manual page names and descriptions | `apropos network` |
| `help` | Display information about builtin commands | `help cd` |
| `info` | Read Info documents | `info bash` |
| `man` | An interface to the system reference manuals | `man ls` |
| `whatis` | Display one-line manual page descriptions | `whatis ls` |
| `which` | Locate a command | `which python` |

## 25. Text Editors in Linux

| Command | Description | Example |
| :--- | :--- | :--- |
| `nano` | Nano's ANOther editor | `nano file.txt` |
| `vi` | Programmer's text editor | `vi file.txt` |
| `vim` | Vi IMproved | `vim file.txt` |
| `ed` | Line-oriented text editor | `ed file.txt` |
| `emacs` | GNU project Emacs editor | `emacs file.txt` |

### Nano Shortcuts Commands

| Category | Shortcut | Description |
| :--- | :--- | :--- |
| **File Operations** | `Ctrl + O` | Save (write) the current file |
| | `Ctrl + X` | Exit Nano |
| | `Ctrl + R` | Read and insert another file |
| **Navigation** | `Ctrl + Y` | Scroll up one page |
| | `Ctrl + V` | Scroll down one page |
| | `Alt + \` | Go to a specific line number |
| | `Alt + ,` | Move to the beginning of the current line |
| | `Alt + .` | Move to the end of the current line |
| **Editing** | `Ctrl + K` | Cut/delete text from the cursor to the end of the line (or marked block) |
| | `Ctrl + U` | Uncut (paste) the last cut text |
| | `Ctrl + 6` | Mark a block of text |
| | `Alt + 6` | Copy the marked block |
| | `Ctrl + J` | Justify (format) the current paragraph |
| **Search/Replace** | `Ctrl + W` | Search for a string |
| | `Alt + W` | Search and replace a string |
| | `Alt + R` | Repeat the last search |

### VI/VIM Shortcuts Commands

| Mode/Category | Shortcut | Description |
| :--- | :--- | :--- |
| **Insert & Replace** | `i` | Insert before cursor |
| | `a` | Insert after cursor |
| | `A` | Insert at the end of the line |
| | `o` | Insert a new line below and switch to insert mode |
| | `R` | Replace mode |
| | `r` | Replace single character |
| | `s` | Substitute character |
| | `S` | Delete line and substitute |
| | `C` | Change to end of line |
| **Delete & Change** | `x` | Delete character |
| | `dd` | Delete line |
| | `3dd` | Delete 3 lines |
| | `D` | Delete to end of line |
| | `dw` | Delete word |
| | `4dw` | Delete 4 words |
| | `cw` | Change word |
| **Undo & Restore** | `u` | Undo |
| | `U` | Restore current line |
| | `~` | Toggle case |
| | `Esc` | Exit mode |
| **Normal Mode** | `yy` | Copy (yank) current line |
| | `p` | Paste |
| | `Ctrl + R` | Redo |
| **Command Mode** | `:w` | Save |
| | `:q` | Quit |
| | `:q!` | Quit without saving |
| | `:wq` or `:x` | Save and quit |
| | `:set nu` | Show line numbers |
| | `:s/old/new/g` | Replace in file |
| **Visual Mode** | `v` | Select text |
| | `y` | Copy selected |
| | `d` | Delete selected |
| | `p` | Paste |

## 26. IO Redirection Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `cmd < file` | Redirect input | `sort < names.txt` |
| `cmd > file` | Redirect output (overwrite) | `echo "Hello" > out.txt` |
| `cmd >> file` | Redirect output (append) | `echo "World" >> out.txt` |
| `cmd 2> file` | Redirect error output | `ls no_exist_dir 2> errors.txt` |
| `cmd 2>&1` | Redirect stderr to stdout | `make 2>&1 &#124; tee build.log` |
| `cmd &> file` | Redirect stdout and stderr | `make &> build.log` |
| `cmd 1>&2` | Redirect stdout to stderr | `echo "Error!" 1>&2` |
| `cmd > /dev/null` | Discard standard output | `ping 8.8.8.8 > /dev/null` |
| `cmd1 <(cmd2)` | Process substitution | `diff <(ls dir1) <(ls dir2)` |

## 27. Environment Variable Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `export VARIABLE_NAME=value` | Set and export an environment variable | `export PATH=$PATH:/opt/bin` |
| `echo $VARIABLE_NAME` | Display value of a variable | `echo $USER` |
| `env` | List all environment variables | `env` |
| `unset VARIABLE_NAME` | Remove an environment variable | `unset JAVA_HOME` |
| `export -p` | List all exported variables | `export -p` |
| `env VAR1=value COMMAND` | Set variable temporarily for a command | `env LC_ALL=C sort file.txt` |
| `printenv` | Display environment variables | `printenv PATH` |
