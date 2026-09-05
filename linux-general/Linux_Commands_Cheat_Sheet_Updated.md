# Linux Commands Cheat Sheet (With Examples)

## 1. File Operations Commands

- `access`: `access -r file.txt` (Check read permission)
- `basename`: `basename /var/log/syslog` -> `syslog`
- `cat`: `cat file.txt` (View file content)
- `cksum`: `cksum file.txt` (Print CRC checksum and byte count)
- `cmp`: `cmp file1.txt file2.txt` (Compare two files byte by byte)
- `compress`: `compress file.txt` (Compress file into .Z format)
- `cp`: `cp source.txt dest.txt` (Copy file)
- `cpio`: `find . -name "*.txt" | cpio -o > archive.cpio` (Create archive)
- `csplit`: `csplit file.txt /pattern/` (Split file into sections by context)
- `cut`: `cut -d',' -f1 file.csv` (Extract first column of CSV)
- `diff`: `diff file1.txt file2.txt` (Find differences between files)
- `diff3`: `diff3 file1.txt file2.txt file3.txt` (Compare three files)
- `echo`: `echo "Hello World"` (Print text to standard output)
- `expand`: `expand -t 4 file.txt` (Convert tabs to spaces)
- `file`: `file archive.tar.gz` (Determine file type)
- `fold`: `fold -w 80 file.txt` (Wrap input lines to fit 80 columns)
- `head`: `head -n 10 file.txt` (Output the first 10 lines)
- `join`: `join file1.txt file2.txt` (Join lines of two files on a common field)
- `less`: `less file.txt` (View file contents interactively)
- `ln`: `ln -s /path/to/target linkname` (Create a symbolic link)
- `locate`: `locate my_script.sh` (Find files by name)
- `look`: `look "word" file.txt` (Display lines beginning with a given string)
- `more`: `more file.txt` (View file one screen at a time)
- `mv`: `mv oldname.txt newname.txt` (Rename or move a file)
- `od`: `od -c file.txt` (Dump files in octal and other formats)
- `paste`: `paste file1.txt file2.txt` (Merge lines of files)
- `readlink`: `readlink -f /path/to/symlink` (Print resolved symbolic link)
- `rename`: `rename 's/\.htm$/.html/' *.htm` (Rename multiple files)
- `rev`: `rev file.txt` (Reverse lines of a file or files)
- `rm`: `rm -rf directory/` (Remove files or directories)
- `shred`: `shred -u secret.txt` (Overwrite a file to hide its contents and delete it)
- `sort`: `sort file.txt` (Sort lines of text files)
- `split`: `split -l 100 file.txt` (Split a file into pieces of 100 lines)
- `tac`: `tac file.txt` (Concatenate and print files in reverse)
- `tail`: `tail -f /var/log/messages` (Output the last part of files and follow changes)
- `tar`: `tar -czvf archive.tar.gz folder/` (Store and extract files from an archive)
- `tee`: `echo "data" | tee output.txt` (Read from standard input and write to standard output and files)
- `touch`: `touch newfile.txt` (Change file timestamps or create empty file)
- `unexpand`: `unexpand -a file.txt` (Convert spaces to tabs)
- `uniq`: `uniq file.txt` (Report or omit repeated lines)
- `wc`: `wc -l file.txt` (Print newline, word, and byte counts)

## 2. Directory Operations Commands

- `cd`: `cd /var/log` (Change directory)
- `dir`: `dir -l` (List directory contents)
- `dirname`: `dirname /var/log/syslog` -> `/var/log`
- `dirs`: `dirs -v` (Display list of currently remembered directories)
- `du`: `du -sh /home/user/` (Estimate file space usage)
- `find`: `find / -name "*.conf"` (Search for files in a directory hierarchy)
- `lsblk`: `lsblk` (List block devices)
- `mkdir`: `mkdir -p /tmp/newdir/subdir` (Make directories)
- `mount`: `mount /dev/sda1 /mnt` (Mount a filesystem)
- `pwd`: `pwd` (Print name of current/working directory)
- `rmdir`: `rmdir emptydir/` (Remove empty directories)
- `tree`: `tree /etc` (List contents of directories in a tree-like format)

## 3. File Permission and Ownership Commands

- `chmod`: `chmod 755 script.sh` (Change file mode bits)
- `chattr`: `chattr +i file.txt` (Change file attributes on a Linux file system)
- `chown`: `chown user:group file.txt` (Change file owner and group)
- `chgrp`: `chgrp wheel file.txt` (Change group ownership)

## 4. User Management Commands

- `chage`: `chage -l username` (Change user password expiry information)
- `chfn`: `chfn username` (Change real user name and information)
- `chsh`: `chsh -s /bin/zsh username` (Change login shell)
- `chpasswd`: `echo "user:newpass" | chpasswd` (Update passwords in batch mode)
- `finger`: `finger username` (User information lookup program)
- `id`: `id username` (Print real and effective user and group IDs)
- `passwd`: `passwd username` (Change user password)
- `pinky`: `pinky -l username` (Lightweight finger program)
- `username`: Not a standard command (typically an env var `$USER` or `whoami`).
- `useradd`: `useradd -m newuser` (Create a new user or update default new user information)
- `userdel`: `userdel -r olduser` (Delete a user account and related files)
- `usermod`: `usermod -aG wheel username` (Modify a user account)
- `users`: `users` (Print the user names of users currently logged in)
- `who`: `who` (Show who is logged on)
- `whoami`: `whoami` (Print effective userid)

## 5. Group Management Commands

- `groupadd`: `groupadd developers` (Create a new group)
- `groupdel`: `groupdel developers` (Delete a group)
- `groupmod`: `groupmod -n devs developers` (Modify a group definition)
- `groups`: `groups username` (Print the groups a user is in)
- `gpasswd`: `gpasswd -a username developers` (Administer /etc/group and /etc/gshadow)
- `grpck`: `grpck` (Verify integrity of group files)
- `grpconv`: `grpconv` (Create shadow group file from group file)

## 6. Process Management Commands

- `accton`: `accton /var/account/pacct` (Turn process accounting on or off)
- `bg`: `bg %1` (Put a job in the background)
- `chrt`: `chrt -p 1234` (Manipulate the real-time attributes of a process)
- `fg`: `fg %1` (Bring a job to the foreground)
- `kill`: `kill -9 1234` (Send a signal to a process)
- `mpstat`: `mpstat -P ALL 1` (Report processors related statistics)
- `pidof`: `pidof sshd` (Find the process ID of a running program)
- `pmap`: `pmap 1234` (Report memory map of a process)
- `ps`: `ps aux` (Report a snapshot of the current processes)
- `top`: `top` (Display Linux processes)
- `htop`: `htop` (Interactive process viewer)
- `strace`: `strace -p 1234` (Trace system calls and signals)
- `time`: `time ls -l` (Run programs and summarize system resource usage)
- `watch`: `watch -n 1 free -m` (Execute a program periodically, showing output fullscreen)
- `vmstat`: `vmstat 1 5` (Report virtual memory statistics)
- `uptime`: `uptime` (Tell how long the system has been running)
- `w`: `w` (Show who is logged on and what they are doing)

## 7. Networking Commands

- `arp`: `arp -a` (Manipulate the system ARP cache)
- `curl`: `curl -O http://example.com/file.zip` (Transfer a URL)
- `host`: `host example.com` (DNS lookup utility)
- `hostid`: `hostid` (Print the numeric identifier for the current host)
- `hostname`: `hostname` (Show or set the system's host name)
- `hostnamectl`: `hostnamectl set-hostname server1` (Control the system hostname)
- `ifconfig`: `ifconfig eth0` (Configure a network interface)
- `iftop`: `iftop -i eth0` (Display bandwidth usage on an interface)
- `ifup`: `ifup eth0` (Bring a network interface up)
- `ip`: `ip addr show` (Show / manipulate routing, network devices, interfaces and tunnels)
- `ipcrm`: `ipcrm -m 1234` (Remove a message queue, semaphore set, or shared memory id)
- `ipcs`: `ipcs -m` (Provide information on ipc facilities)
- `iptables`: `iptables -L` (Administration tool for IPv4 packet filtering and NAT)
- `iptables-save`: `iptables-save > /etc/iptables/rules.v4` (Dump iptables rules to stdout)
- `iwconfig`: `iwconfig wlan0` (Configure a wireless network interface)
- `nc` (`netcat`): `nc -lvp 8080` (Arbitrary TCP and UDP connections and listens)
- `netstat`: `netstat -tuln` (Print network connections, routing tables, interface statistics, etc.)
- `nmcli`: `nmcli connection show` (Command-line tool for controlling NetworkManager)
- `nslookup`: `nslookup example.com` (Query Internet name servers interactively)
- `ping`: `ping 8.8.8.8` (Send ICMP ECHO_REQUEST to network hosts)
- `rcp`: `rcp file.txt host:/tmp/` (Remote file copy)
- `route`: `route -n` (Show / manipulate the IP routing table)
- `rsync`: `rsync -avz /local/dir/ user@remote:/remote/dir/` (Fast, versatile, remote (and local) file-copying tool)
- `scp`: `scp file.txt user@remote:/tmp/` (Secure copy)
- `ssh`: `ssh user@remote` (OpenSSH SSH client)
- `tracepath`: `tracepath 8.8.8.8` (Traces path to a network host discovering MTU)
- `traceroute`: `traceroute example.com` (Print the route packets trace to network host)
- `vnstat`: `vnstat -i eth0` (Console-based network traffic monitor)
- `wget`: `wget http://example.com/file.iso` (The non-interactive network downloader)

## 8. Job Scheduling Commands

- `atd`: `systemctl status atd` (Job spooling daemon)
- `atrm`: `atrm 1` (Remove jobs spooled by at)
- `atq`: `atq` (Lists the user's pending jobs)
- `batch`: `echo "sh ./script.sh" | batch` (Execute commands when system load levels permit)
- `cron`: `systemctl status crond` (Daemon to execute scheduled commands)
- `crontab`: `crontab -e` (Maintain crontab files for individual users)

## 9. Disk and File System Commands

- `cfdisk`: `cfdisk /dev/sda` (Display or manipulate disk partition table)
- `df`: `df -h` (Report file system disk space usage)
- `dosfsck`: `dosfsck /dev/sdb1` (Check and repair MS-DOS file systems)
- `dump`: `dump -0u -f /tmp/backup.dump /dev/sda1` (ext2/3/4 filesystem backup)
- `dumpe2fs`: `dumpe2fs /dev/sda1` (Dump ext2/3/4 filesystem information)
- `fdisk`: `fdisk -l` (Manipulate disk partition table)
- `mount`: `mount /dev/sda1 /mnt` (Mount a filesystem)
- `restore`: `restore -r -f /tmp/backup.dump` (Restore files or file systems from backups made with dump)
- `sync`: `sync` (Synchronize cached writes to persistent storage)

## 10. Hardware and System Information Commands

- `acpi`: `acpi -V` (Show battery status and other ACPI information)
- `acpi_available`: `acpi_available` (Test whether ACPI subsystem is available)
- `acpid`: `systemctl restart acpid` (Advanced Configuration and Power Interface event daemon)
- `arch`: `arch` (Print machine hardware name)
- `dmesg`: `dmesg -T` (Print or control the kernel ring buffer)
- `dmidecode`: `dmidecode -t memory` (DMI table decoder)
- `dstat`: `dstat` (Versatile resource statistics tool)
- `free`: `free -m` (Display amount of free and used memory in the system)
- `hdparm`: `hdparm -tT /dev/sda` (Get/set SATA/IDE device parameters)
- `hwclock`: `hwclock --show` (Query or set the hardware clock)
- `iostat`: `iostat -x 1` (Report Central Processing Unit statistics and input/output statistics for devices and partitions)
- `iotop`: `iotop` (Simple top-like I/O monitor)
- `lsusb`: `lsusb` (List USB devices)
- `lshw`: `lshw -short` (Extract detailed information on the hardware configuration of the machine)
- `uname`: `uname -a` (Print system information)

## 11. Compression and Archiving Commands

- `ar`: `ar rcs lib.a obj1.o obj2.o` (Create, modify, and extract from archives)
- `bzcmp`: `bzcmp file1.bz2 file2.bz2` (Compare bzip2 compressed files)
- `bzdiff`: `bzdiff file1.bz2 file2.bz2` (Compare bzip2 compressed files)
- `bzgrep`: `bzgrep "search" file.bz2` (Search possibly bzip2 compressed files for a regular expression)
- `bzip2`: `bzip2 file.txt` (A block-sorting file compressor)
- `bzless`: `bzless file.bz2` (File perusal filter for crt viewing of bzip2 compressed text)
- `bzmore`: `bzmore file.bz2` (File perusal filter for crt viewing of bzip2 compressed text)
- `gunzip`: `gunzip file.gz` (Compress or expand files)
- `gzip`: `gzip file.txt` (Compress or expand files)
- `gzexe`: `gzexe script.sh` (Compress executable files in place)
- `zip`: `zip -r archive.zip folder/` (Package and compress files)
- `zdiff`: `zdiff file1.gz file2.gz` (Compare compressed files)
- `zgrep`: `zgrep "search" file.gz` (Search possibly compressed files for a regular expression)

## 12. Text Processing and Formatting Commands

- `awk`: `awk '{print $1}' file.txt` (Pattern scanning and processing language)
- `aspell`: `aspell check file.txt` (Interactive spell checker)
- `banner`: `banner Hello` (Print large banner on printer/stdout)
- `bc`: `echo "10 + 5" | bc` (An arbitrary precision calculator language)
- `col`: `man ls | col -b > ls.txt` (Filter reverse line feeds from input)
- `colcrt`: `colcrt file.txt` (Filter nroff output for CRT previewing)
- `colrm`: `colrm 1 5 < file.txt` (Remove columns from a file)
- `column`: `mount | column -t` (Columnate lists)
- `dc`: `dc -e '10 5 + p'` (An arbitrary precision calculator)
- `egrep`: `egrep "pattern1|pattern2" file.txt` (Print lines matching a pattern (grep -E))
- `fgrep`: `fgrep "exact string" file.txt` (Print lines matching a pattern (grep -F))
- `fmt`: `fmt -w 60 file.txt` (Simple optimal text formatter)
- `grep`: `grep "error" /var/log/syslog` (Print lines matching a pattern)
- `sdiff`: `sdiff file1.txt file2.txt` (Side-by-side merge of file differences)
- `sed`: `sed 's/old/new/g' file.txt` (Stream editor for filtering and transforming text)
- `tr`: `cat file.txt | tr 'a-z' 'A-Z'` (Translate or delete characters)
- `unix2dos`: `unix2dos file.txt` (UNIX to DOS text file format converter)

## 13. Kernel and Module Management Commands

- `depmod`: `depmod -a` (Generate modules.dep and map files)
- `insmod`: `insmod module.ko` (Simple program to insert a module into the Linux Kernel)
- `lsmod`: `lsmod` (Show the status of modules in the Linux Kernel)
- `modinfo`: `modinfo e1000e` (Show information about a Linux Kernel module)
- `rmmod`: `rmmod module_name` (Simple program to remove a module from the Linux Kernel)
- `systemctl`: `systemctl status network` (Control the systemd system and service manager)

## 14. System Control and Power Commands

- `halt`: `halt` (Instruct the hardware to stop all CPU functions)
- `poweroff`: `poweroff` (Power off the system)
- `reboot`: `reboot` (Reboot the system)
- `shutdown`: `shutdown -h now` (Halt, power-off or reboot the machine)

## 15. Logging and Monitoring Commands

- `journalctl`: `journalctl -u sshd -f` (Query the systemd journal)
- `last`: `last username` (Show listing of last logged in users)
- `history`: `history | grep command` (GNU History Library)
- `sar`: `sar -u 1 3` (Collect, report, or save system activity information)
- `script`: `script session.log` (Make typescript of terminal session)
- `scriptreplay`: `scriptreplay timing.log session.log` (Play back typescripts, using timing information)

## 16. Checksum and File Integrity Commands

- `md5sum`: `md5sum file.iso` (Compute and check MD5 message digest)
- `cksum`: `cksum file.txt` (Print CRC checksum and byte counts)
- `sum`: `sum file.txt` (Checksum and count the blocks in a file)

## 17. Date and Time Commands

- `cal`: `cal 2026` (Displays a calendar)
- `date`: `date "+%Y-%m-%d %H:%M:%S"` (Print or set the system date and time)
- `uptime`: `uptime` (Tell how long the system has been running)

## 18. Mail and User Communication Commands

- `biff`: `biff y` (Be notified if mail arrives and who it is from)
- `mailq`: `mailq` (Print the mail queue)
- `write`: `write username` (Send a message to another user)
- `wall`: `wall "System will go down in 10 minutes"` (Send a message to everybody's terminal)

## 19. Printing and Media Commands

- `amixer`: `amixer set Master 50%` (Command-line mixer for ALSA soundcard driver)
- `aplay`: `aplay sound.wav` (Command-line sound player for ALSA soundcard driver)
- `aplaymidi`: `aplaymidi -p 14:0 file.mid` (Standard MIDI File player for ALSA sequencer)
- `cupsd`: `systemctl restart cupsd` (Common UNIX Printing System daemon)
- `eject`: `eject /dev/cdrom` (Eject removable media)
- `import`: `import screenshot.png` (Saves any visible window on an X server and outputs it as an image file)

## 20. Shell Built-in and Scripting Commands

- `alias`: `alias ll='ls -l'` (Define or display aliases)
- `bind`: `bind -P` (Set Readline key bindings and variables)
- `break`: `break` (Exit from a for, while, or until loop)
- `builtin`: `builtin cd /tmp` (Run a shell builtin, passing it args)
- `case`: `case $VAR in ... esac` (Conditional construct in shell scripts)
- `continue`: `continue` (Resume the next iteration of a loop)
- `declare`: `declare -i NUM=5` (Set variables and attributes)
- `enable`: `enable -n cd` (Enable and disable shell builtins)
- `env`: `env | grep USER` (Set environment and execute command, or print environment)
- `eval`: `eval "ls -l"` (Construct command by concatenating arguments)
- `exec`: `exec bash` (Replace the shell with the given command)
- `exit`: `exit 0` (Exit the shell)
- `expect`: `expect script.exp` (Programmed dialogue with interactive programs)
- `export`: `export PATH=$PATH:/new/dir` (Set export attribute for shell variables)
- `expr`: `expr 5 + 3` (Evaluate expressions)
- `factor`: `factor 100` (Print the prime factors)
- `fc`: `fc -l` (Process command history list)
- `function`: `function myfunc() { echo "hi"; }` (Define shell functions)
- `for`: `for i in {1..5}; do echo $i; done` (Loop construct)
- `if`: `if [ -f file ]; then echo "Exists"; fi` (Conditional construct)
- `let`: `let "a = 5 + 3"` (Evaluate arithmetic expressions)
- `printf`: `printf "Result: %04d
" 42` (Format and print data)
- `read`: `read -p "Enter name: " name` (Read a line from standard input)
- `return`: `return 1` (Return from a shell function)
- `select`: `select opt in "A" "B"; do echo $opt; break; done` (Generate menus from list of words)
- `seq`: `seq 1 5` (Print a sequence of numbers)
- `setsid`: `setsid my_script.sh` (Run a program in a new session)
- `shift`: `shift 2` (Shift positional parameters)
- `source`: `source ~/.bashrc` (Execute commands from a file in the current shell)
- `type`: `type ls` (Display information about command type)
- `until`: `until [ $i -gt 5 ]; do ... done` (Loop construct)
- `while`: `while true; do ... done` (Loop construct)
- `yes`: `yes "y" | rm -r dir/` (Output a string repeatedly until killed)
- `sudo`: `sudo dnf update` (Execute a command as another user)
- `sleep`: `sleep 5` (Delay for a specified amount of time)

---

## 21. Bash Shortcuts Commands

### Navigation Shortcuts

- `Ctrl + A` : Move to the beginning of the line
- `Ctrl + E` : Move to the end of the line
- `Ctrl + B` : Move back one character
- `Ctrl + F` : Move forward one character
- `Alt + B` : Move back one word
- `Alt + F` : Move forward one word

### Editing Shortcuts

- `Ctrl + U` : Cut/delete text from the cursor to the beginning of the line
- `Ctrl + K` : Cut/delete text from the cursor to the end of the line
- `Ctrl + W` : Cut/delete the word before the cursor
- `Ctrl + Y` : Paste the last cut text
- `Ctrl + L` : Clear the terminal screen
- `Ctrl + C` : Terminate the currently running command

### History Shortcuts

- `Ctrl + R` : Search command history (reverse search)
- `Ctrl + G` : Exit history search mode
- `Ctrl + P` : Go to the previous command in history
- `Ctrl + N` : Go to the next command in history

---

## 22. Development and Build Automation Commands

- `aclocal`: `aclocal` (Create aclocal.m4 by scanning configure.ac)
- `addr2line`: `addr2line -e myprog 0x400500` (Convert addresses into file names and line numbers)
- `autoconf`: `autoconf` (Generate configuration scripts)
- `autoheader`: `autoheader` (Create a template header for configure)
- `automake`: `automake --add-missing` (Automatically create Makefile.in's from Makefile.am's)
- `autoreconf`: `autoreconf -i` (Update generated configuration files)
- `autoupdate`: `autoupdate` (Update a configure.ac to a newer Autoconf)
- `bison`: `bison -d parser.y` (GNU parser generator)
- `cc`: `cc main.c -o main` (C compiler)
- `cpp`: `cpp main.c` (The C Preprocessor)
- `ctags`: `ctags -R .` (Generate tag files for source code)
- `g++`: `g++ main.cpp -o main` (GNU C++ compiler)
- `gcc`: `gcc main.c -o main` (GNU C compiler)
- `gdb`: `gdb ./myprog` (The GNU Debugger)
- `ranlib`: `ranlib libmy.a` (Generate index to archive)
- `readelf`: `readelf -a myprog` (Displays information about ELF files)

## 23. Terminal and Session Management Commands

- `agetty`: `agetty tty1 9600` (Alternative Linux getty)
- `chvt`: `chvt 3` (Change foreground virtual terminal)
- `reset`: `reset` (Terminal initialization)
- `screen`: `screen -S mysession` (Screen manager with VT100/ANSI terminal emulation)
- `showkey`: `showkey -a` (Examine the codes sent by the keyboard)
- `stty`: `stty -a` (Change and print terminal line settings)
- `tty`: `tty` (Print the file name of the terminal connected to standard input)
- `xdg-open`: `xdg-open index.html` (Opens a file or URL in the user's preferred application)

## 24. Help and Documentation Commands

- `apropos`: `apropos network` (Search the manual page names and descriptions)
- `help`: `help cd` (Display information about builtin commands)
- `info`: `info bash` (Read Info documents)
- `man`: `man ls` (An interface to the system reference manuals)
- `whatis`: `whatis ls` (Display one-line manual page descriptions)
- `which`: `which python` (Locate a command)

## 25. Text Editors in Linux

- `nano`: `nano file.txt` (Nano's ANOther editor)
- `vi`: `vi file.txt` (Programmer's text editor)
- `vim`: `vim file.txt` (Vi IMproved)
- `ed`: `ed file.txt` (Line-oriented text editor)
- `emacs`: `emacs file.txt` (GNU project Emacs editor)

### Nano Shortcuts Commands

**File Operations**

- `Ctrl + O` : Save (write) the current file
- `Ctrl + X` : Exit Nano
- `Ctrl + R` : Read and insert another file

**Navigation**

- `Ctrl + Y` : Scroll up one page
- `Ctrl + V` : Scroll down one page
- `Alt + \` : Go to a specific line number
- `Alt + ,` : Move to the beginning of the current line
- `Alt + .` : Move to the end of the current line

**Editing**

- `Ctrl + K` : Cut/delete text from the cursor to the end of the line (or marked block)
- `Ctrl + U` : Uncut (paste) the last cut text
- `Ctrl + 6` : Mark a block of text
- `Alt + 6` : Copy the marked block
- `Ctrl + J` : Justify (format) the current paragraph

**Search and Replace**

- `Ctrl + W` : Search for a string
- `Alt + W` : Search and replace a string
- `Alt + R` : Repeat the last search

### VI/VIM Shortcuts Commands

**Insert & Replace Mode**

- `i` : Insert before cursor
- `a` : Insert after cursor
- `A` : Insert at the end of the line
- `o` : Insert a new line below and switch to insert mode
- `R` : Replace mode
- `r` : Replace single character
- `s` : Substitute character
- `S` : Delete line and substitute
- `C` : Change to end of line

**Delete & Change**

- `x` : Delete character
- `dd` : Delete line
- `3dd` : Delete 3 lines
- `D` : Delete to end of line
- `dw` : Delete word
- `4dw` : Delete 4 words
- `cw` : Change word

**Undo & Restore**

- `u` : Undo
- `U` : Restore current line
- `~` : Toggle case
- `Esc` : Exit mode

**Vim Normal Mode**

- `yy` : Copy (yank) current line
- `p` : Paste
- `Ctrl + R` : Redo

**Vim Command Mode**

- `:w` : Save
- `:q` : Quit
- `:q!` : Quit without saving
- `:wq` or `:x` : Save and quit
- `:set nu` : Show line numbers
- `:s/old/new/g` : Replace in file

**Vim Visual Mode**

- `v` : Select text
- `y` : Copy selected
- `d` : Delete selected
- `p` : Paste

---

## 26. IO Redirection Commands

- `cmd < file` : `sort < names.txt` (Redirect input)
- `cmd > file` : `echo "Hello" > out.txt` (Redirect output (overwrite))
- `cmd >> file` : `echo "World" >> out.txt` (Redirect output (append))
- `cmd 2> file` : `ls no_exist_dir 2> errors.txt` (Redirect error output)
- `cmd 2>&1` : `make 2>&1 | tee build.log` (Redirect stderr to stdout)
- `cmd &> file` : `make &> build.log` (Redirect stdout and stderr)
- `cmd 1>&2` : `echo "Error!" 1>&2` (Redirect stdout to stderr)
- `cmd > /dev/null` : `ping 8.8.8.8 > /dev/null` (Discard standard output)
- `cmd1 <(cmd2)` : `diff <(ls dir1) <(ls dir2)` (Process substitution)

## 27. Environment Variable Commands

- `export VARIABLE_NAME=value` : `export PATH=$PATH:/opt/bin` (Set and export an environment variable)
- `echo $VARIABLE_NAME` : `echo $USER` (Display value of a variable)
- `env` : `env` (List all environment variables)
- `unset VARIABLE_NAME` : `unset JAVA_HOME` (Remove an environment variable)
- `export -p` : `export -p` (List all exported variables)
- `env VAR1=value COMMAND` : `env LC_ALL=C sort file.txt` (Set variable temporarily for a command)
- `printenv` : `printenv PATH` (Display environment variables)
