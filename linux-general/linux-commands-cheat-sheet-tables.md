## Essential Linux commands, administration tools, and text editor shortcuts organized into tables

## 1. File Operations Commands

**`access` — Check read, write, and execute permissions:**

```bash
access -r file.txt
```

**`basename` — Strip directory and suffix from filenames:**

```bash
basename /var/log/syslog
```

**`cat` — Concatenate files and print on the standard output:**

```bash
cat file.txt
```

**`cksum` — Print CRC checksum and byte count:**

```bash
cksum file.txt
```

**`cmp` — Compare two files byte by byte:**

```bash
cmp file1.txt file2.txt
```

**`compress` — Compress data into .Z format:**

```bash
compress file.txt
```

**`cp` — Copy files and directories:**

```bash
cp source.txt dest.txt
```

**`cpio` — Copy files to and from archives:**

```bash
find . -name "*.txt" | cpio -o > archive.cpio
```

**`csplit` — Split a file into context-determined pieces:**

```bash
csplit file.txt /pattern/
```

**`cut` — Remove sections from each line of files:**

```bash
cut -d',' -f1 file.csv
```

**`diff` — Find differences between two files:**

```bash
diff file1.txt file2.txt
```

**`diff3` — Compare three files line by line:**

```bash
diff3 file1.txt file2.txt file3.txt
```

**`echo` — Display a line of text:**

```bash
echo "Hello World"
```

**`expand` — Convert tabs to spaces:**

```bash
expand -t 4 file.txt
```

**`file` — Determine file type:**

```bash
file archive.tar.gz
```

**`fold` — Wrap each input line to fit in specified width:**

```bash
fold -w 80 file.txt
```

**`head` — Output the first part of files:**

```bash
head -n 10 file.txt
```

**`join` — Join lines of two files on a common field:**

```bash
join file1.txt file2.txt
```

**`less` — View file contents interactively (allows backward movement):**

```bash
less file.txt
```

**`ln` — Make links between files (hard or symbolic):**

```bash
ln -s /path/to/target linkname
```

**`locate` — Find files by name using a database:**

```bash
locate my_script.sh
```

**`look` — Display lines beginning with a given string:**

```bash
look "word" file.txt
```

**`more` — File perusal filter for viewing one screen at a time:**

```bash
more file.txt
```

**`mv` — Move or rename files and directories:**

```bash
mv oldname.txt newname.txt
```

**`od` — Dump files in octal and other formats:**

```bash
od -c file.txt
```

**`paste` — Merge lines of files side-by-side:**

```bash
paste file1.txt file2.txt
```

**`readlink` — Print resolved symbolic link or canonical file name:**

```bash
readlink -f /path/to/symlink
```

**`rename` — Rename multiple files using regular expressions:**

```bash
rename 's/\.htm$/.html/' *.htm
```

**`rev` — Reverse the order of characters in every line:**

```bash
rev file.txt
```

**`rm` — Remove files or directories:**

```bash
rm -rf directory/
```

**`shred` — Overwrite a file to hide its contents, and optionally delete it:**

```bash
shred -u secret.txt
```

**`sort` — Sort lines of text files:**

```bash
sort file.txt
```

**`split` — Split a file into pieces:**

```bash
split -l 100 file.txt
```

**`tac` — Concatenate and print files in reverse order (last line first):**

```bash
tac file.txt
```

**`tail` — Output the last part of files:**

```bash
tail -f /var/log/messages
```

**`tar` — Store and extract files from an archive:**

```bash
tar -czvf archive.tar.gz folder/
```

**`tee` — Read from standard input and write to standard output and files:**

```bash
echo "data" | tee output.txt
```

**`touch` — Change file timestamps or create an empty file:**

```bash
touch newfile.txt
```

**`unexpand` — Convert spaces to tabs:**

```bash
unexpand -a file.txt
```

**`uniq` — Report or omit repeated lines:**

```bash
uniq file.txt
```

**`wc` — Print newline, word, and byte counts for each file:**

```bash
wc -l file.txt
```

## 2. Directory Operations Commands

**`cd` — Change the shell working directory:**

```bash
cd /var/log
```

**`dir` — List directory contents (similar to ls):**

```bash
dir -l
```

**`dirname` — Strip non-directory suffix from file name:**

```bash
dirname /var/log/syslog
```

**`dirs` — Display list of currently remembered directories:**

```bash
dirs -v
```

**`du` — Estimate file and directory space usage:**

```bash
du -sh /home/user/
```

**`find` — Search for files in a directory hierarchy:**

```bash
find / -name "*.conf"
```

**`lsblk` — List information about block devices:**

```bash
lsblk
```

**`mkdir` — Make directories:**

```bash
mkdir -p /tmp/newdir/subdir
```

**`mount` — Mount a filesystem:**

```bash
mount /dev/sda1 /mnt
```

**`pwd` — Print name of current/working directory:**

```bash
pwd
```

**`rmdir` — Remove empty directories:**

```bash
rmdir emptydir/
```

**`tree` — List contents of directories in a tree-like format:**

```bash
tree /etc
```

## 3. File Permission and Ownership Commands

**`chmod` — Change file mode bits (permissions):**

```bash
chmod 755 script.sh
```

**`chattr` — Change file attributes on a Linux file system:**

```bash
chattr +i file.txt
```

**`chown` — Change file owner and group:**

```bash
chown user:group file.txt
```

**`chgrp` — Change group ownership:**

```bash
chgrp wheel file.txt
```

## 4. User Management Commands

**`chage` — Change user password expiry information:**

```bash
chage -l username
```

**`chfn` — Change real user name and information:**

```bash
chfn username
```

**`chsh` — Change login shell:**

```bash
chsh -s /bin/zsh username
```

**`chpasswd` — Update passwords in batch mode:**

```bash
echo "user:newpass" | chpasswd
```

**`finger` — User information lookup program:**

```bash
finger username
```

**`id` — Print real and effective user and group IDs:**

```bash
id username
```

**`passwd` — Change user password:**

```bash
passwd username
```

**`pinky` — Lightweight finger program:**

```bash
pinky -l username
```

**`useradd` — Create a new user or update default new user information:**

```bash
useradd -m newuser
```

**`userdel` — Delete a user account and related files:**

```bash
userdel -r olduser
```

**`usermod` — Modify a user account:**

```bash
usermod -aG wheel username
```

**`users` — Print the user names of users currently logged in:**

```bash
users
```

**`who` — Show who is logged on:**

```bash
who
```

**`whoami` — Print effective userid:**

```bash
whoami
```

## 5. Group Management Commands

**`groupadd` — Create a new group:**

```bash
groupadd developers
```

**`groupdel` — Delete a group:**

```bash
groupdel developers
```

**`groupmod` — Modify a group definition:**

```bash
groupmod -n devs developers
```

**`groups` — Print the groups a user is in:**

```bash
groups username
```

**`gpasswd` — Administer /etc/group and /etc/gshadow:**

```bash
gpasswd -a username developers
```

**`grpck` — Verify integrity of group files:**

```bash
grpck
```

**`grpconv` — Create shadow group file from group file:**

```bash
grpconv
```

## 6. Process Management Commands

**`accton` — Turn process accounting on or off:**

```bash
accton /var/account/pacct
```

**`bg` — Put a job in the background:**

```bash
bg %1
```

**`chrt` — Manipulate the real-time attributes of a process:**

```bash
chrt -p 1234
```

**`fg` — Bring a job to the foreground:**

```bash
fg %1
```

**`kill` — Send a signal to a process:**

```bash
kill -9 1234
```

**`mpstat` — Report processors related statistics:**

```bash
mpstat -P ALL 1
```

**`pidof` — Find the process ID of a running program:**

```bash
pidof sshd
```

**`pmap` — Report memory map of a process:**

```bash
pmap 1234
```

**`ps` — Report a snapshot of the current processes:**

```bash
ps aux
```

**`top` — Display Linux processes dynamically:**

```bash
top
```

**`htop` — Interactive process viewer:**

```bash
htop
```

**`strace` — Trace system calls and signals:**

```bash
strace -p 1234
```

**`time` — Run programs and summarize system resource usage:**

```bash
time ls -l
```

**`watch` — Execute a program periodically, showing output fullscreen:**

```bash
watch -n 1 free -m
```

**`vmstat` — Report virtual memory statistics:**

```bash
vmstat 1 5
```

**`uptime` — Tell how long the system has been running:**

```bash
uptime
```

**`w` — Show who is logged on and what they are doing:**

```bash
w
```

## 7. Networking Commands

**`arp` — Manipulate the system ARP cache:**

```bash
arp -a
```

**`curl` — Transfer a URL:**

```bash
curl -O http://example.com/file.zip
```

**`host` — DNS lookup utility:**

```bash
host example.com
```

**`hostid` — Print the numeric identifier for the current host:**

```bash
hostid
```

**`hostname` — Show or set the system's host name:**

```bash
hostname
```

**`hostnamectl` — Control the system hostname:**

```bash
hostnamectl set-hostname server1
```

**`ifconfig` — Configure a network interface:**

```bash
ifconfig eth0
```

**`iftop` — Display bandwidth usage on an interface:**

```bash
iftop -i eth0
```

**`ifup` — Bring a network interface up:**

```bash
ifup eth0
```

**`ip` — Show / manipulate routing, network devices, interfaces and tunnels:**

```bash
ip addr show
```

**`ipcrm` — Remove a message queue, semaphore set, or shared memory id:**

```bash
ipcrm -m 1234
```

**`ipcs` — Provide information on ipc facilities:**

```bash
ipcs -m
```

**`iptables` — Administration tool for IPv4 packet filtering and NAT:**

```bash
iptables -L
```

**`iptables-save` — Dump iptables rules to stdout:**

```bash
iptables-save > /etc/iptables/rules.v4
```

**`iwconfig` — Configure a wireless network interface:**

```bash
iwconfig wlan0
```

**``nc`(`netcat`)` — Arbitrary TCP and UDP connections and listens:**

```bash
nc -lvp 8080
```

**`netstat` — Print network connections, routing tables, interface statistics, etc:**

```bash
netstat -tuln
```

**`nmcli` — Command-line tool for controlling NetworkManager:**

```bash
nmcli connection show
```

**`nslookup` — Query Internet name servers interactively:**

```bash
nslookup example.com
```

**`ping` — Send ICMP ECHO_REQUEST to network hosts:**

```bash
ping 8.8.8.8
```

**`rcp` — Remote file copy:**

```bash
rcp file.txt host:/tmp/
```

**`route` — Show / manipulate the IP routing table:**

```bash
route -n
```

**`rsync` — Fast, versatile, remote (and local) file-copying tool:**

```bash
rsync -avz /local/dir/ user@remote:/remote/dir/
```

**`scp` — Secure copy:**

```bash
scp file.txt user@remote:/tmp/
```

**`ssh` — OpenSSH SSH client:**

```bash
ssh user@remote
```

**`tracepath` — Traces path to a network host discovering MTU:**

```bash
tracepath 8.8.8.8
```

**`traceroute` — Print the route packets trace to network host:**

```bash
traceroute example.com
```

**`vnstat` — Console-based network traffic monitor:**

```bash
vnstat -i eth0
```

**`wget` — The non-interactive network downloader:**

```bash
wget http://example.com/file.iso
```

## 8. Job Scheduling Commands

**`atd` — Job spooling daemon:**

```bash
systemctl status atd
```

**`atrm` — Remove jobs spooled by at:**

```bash
atrm 1
```

**`atq` — Lists the user's pending jobs:**

```bash
atq
```

**`batch` — Execute commands when system load levels permit:**

```bash
echo "sh ./script.sh" | batch
```

**`cron` — Daemon to execute scheduled commands:**

```bash
systemctl status crond
```

**`crontab` — Maintain crontab files for individual users:**

```bash
crontab -e
```

## 9. Disk and File System Commands

**`cfdisk` — Display or manipulate disk partition table:**

```bash
cfdisk /dev/sda
```

**`df` — Report file system disk space usage:**

```bash
df -h
```

**`dosfsck` — Check and repair MS-DOS file systems:**

```bash
dosfsck /dev/sdb1
```

**`dump` — ext2/3/4 filesystem backup:**

```bash
dump -0u -f /tmp/backup.dump /dev/sda1
```

**`dumpe2fs` — Dump ext2/3/4 filesystem information:**

```bash
dumpe2fs /dev/sda1
```

**`fdisk` — Manipulate disk partition table:**

```bash
fdisk -l
```

**`mount` — Mount a filesystem:**

```bash
mount /dev/sda1 /mnt
```

**`restore` — Restore files or file systems from backups made with dump:**

```bash
restore -r -f /tmp/backup.dump
```

**`sync` — Synchronize cached writes to persistent storage:**

```bash
sync
```

## 10. Hardware and System Information Commands

**`acpi` — Show battery status and other ACPI information:**

```bash
acpi -V
```

**`acpi_available` — Test whether ACPI subsystem is available:**

```bash
acpi_available
```

**`acpid` — Advanced Configuration and Power Interface event daemon:**

```bash
systemctl restart acpid
```

**`arch` — Print machine hardware name:**

```bash
arch
```

**`dmesg` — Print or control the kernel ring buffer:**

```bash
dmesg -T
```

**`dmidecode` — DMI table decoder:**

```bash
dmidecode -t memory
```

**`dstat` — Versatile resource statistics tool:**

```bash
dstat
```

**`free` — Display amount of free and used memory in the system:**

```bash
free -m
```

**`hdparm` — Get/set SATA/IDE device parameters:**

```bash
hdparm -tT /dev/sda
```

**`hwclock` — Query or set the hardware clock:**

```bash
hwclock --show
```

**`iostat` — Report CPU and input/output statistics for devices:**

```bash
iostat -x 1
```

**`iotop` — Simple top-like I/O monitor:**

```bash
iotop
```

**`lsusb` — List USB devices:**

```bash
lsusb
```

**`lshw` — Extract detailed information on the hardware configuration:**

```bash
lshw -short
```

**`uname` — Print system information:**

```bash
uname -a
```

## 11. Compression and Archiving Commands

**`ar` — Create, modify, and extract from archives:**

```bash
ar rcs lib.a obj1.o obj2.o
```

**`bzcmp` — Compare bzip2 compressed files:**

```bash
bzcmp file1.bz2 file2.bz2
```

**`bzdiff` — Compare bzip2 compressed files:**

```bash
bzdiff file1.bz2 file2.bz2
```

**`bzgrep` — Search bzip2 compressed files for a regular expression:**

```bash
bzgrep "search" file.bz2
```

**`bzip2` — A block-sorting file compressor:**

```bash
bzip2 file.txt
```

**`bzless` — File perusal filter for crt viewing of bzip2 compressed text:**

```bash
bzless file.bz2
```

**`bzmore` — File perusal filter for crt viewing of bzip2 compressed text:**

```bash
bzmore file.bz2
```

**`gunzip` — Compress or expand files:**

```bash
gunzip file.gz
```

**`gzip` — Compress or expand files:**

```bash
gzip file.txt
```

**`gzexe` — Compress executable files in place:**

```bash
gzexe script.sh
```

**`zip` — Package and compress files:**

```bash
zip -r archive.zip folder/
```

**`zdiff` — Compare compressed files:**

```bash
zdiff file1.gz file2.gz
```

**`zgrep` — Search possibly compressed files for a regular expression:**

```bash
zgrep "search" file.gz
```

## 12. Text Processing and Formatting Commands

**`awk` — Pattern scanning and processing language:**

```bash
awk '{print $1}' file.txt
```

**`aspell` — Interactive spell checker:**

```bash
aspell check file.txt
```

**`banner` — Print large banner on printer/stdout:**

```bash
banner Hello
```

**`bc` — An arbitrary precision calculator language:**

```bash
echo "10 + 5" | bc
```

**`col` — Filter reverse line feeds from input:**

```bash
man ls | col -b > ls.txt
```

**`colcrt` — Filter nroff output for CRT previewing:**

```bash
colcrt file.txt
```

**`colrm` — Remove columns from a file:**

```bash
colrm 1 5 < file.txt
```

**`column` — Columnate lists:**

```bash
mount | column -t
```

**`dc` — An arbitrary precision calculator:**

```bash
dc -e '10 5 + p'
```

**`egrep` — Print lines matching a pattern (grep -E):**

```bash
egrep "pattern1|pattern2" file.txt
```

**`fgrep` — Print lines matching a pattern (grep -F):**

```bash
fgrep "exact string" file.txt
```

**`fmt` — Simple optimal text formatter:**

```bash
fmt -w 60 file.txt
```

**`grep` — Print lines matching a pattern:**

```bash
grep "error" /var/log/syslog
```

**`sdiff` — Side-by-side merge of file differences:**

```bash
sdiff file1.txt file2.txt
```

**`sed` — Stream editor for filtering and transforming text:**

```bash
sed 's/old/new/g' file.txt
```

**`tr` — Translate or delete characters:**

```bash
cat file.txt | tr 'a-z' 'A-Z'
```

**`unix2dos` — UNIX to DOS text file format converter:**

```bash
unix2dos file.txt
```

## 13. Kernel and Module Management Commands

**`depmod` — Generate modules.dep and map files:**

```bash
depmod -a
```

**`insmod` — Insert a module into the Linux Kernel:**

```bash
insmod module.ko
```

**`lsmod` — Show the status of modules in the Linux Kernel:**

```bash
lsmod
```

**`modinfo` — Show information about a Linux Kernel module:**

```bash
modinfo e1000e
```

**`rmmod` — Remove a module from the Linux Kernel:**

```bash
rmmod module_name
```

**`systemctl` — Control the systemd system and service manager:**

```bash
systemctl status network
```

## 14. System Control and Power Commands

**`halt` — Instruct the hardware to stop all CPU functions:**

```bash
halt
```

**`poweroff` — Power off the system:**

```bash
poweroff
```

**`reboot` — Reboot the system:**

```bash
reboot
```

**`shutdown` — Halt, power-off or reboot the machine:**

```bash
shutdown -h now
```

## 15. Logging and Monitoring Commands

**`journalctl` — Query the systemd journal:**

```bash
journalctl -u sshd -f
```

**`last` — Show listing of last logged in users:**

```bash
last username
```

**`history` — GNU History Library (show previous commands):**

```bash
history | grep command
```

**`sar` — Collect, report, or save system activity information:**

```bash
sar -u 1 3
```

**`script` — Make typescript of terminal session:**

```bash
script session.log
```

**`scriptreplay` — Play back typescripts, using timing information:**

```bash
scriptreplay timing.log session.log
```

## 16. Checksum and File Integrity Commands

**`md5sum` — Compute and check MD5 message digest:**

```bash
md5sum file.iso
```

**`cksum` — Print CRC checksum and byte counts:**

```bash
cksum file.txt
```

**`sum` — Checksum and count the blocks in a file:**

```bash
sum file.txt
```

## 17. Date and Time Commands

**`cal` — Displays a calendar:**

```bash
cal 2026
```

**`date` — Print or set the system date and time:**

```bash
date "+%Y-%m-%d %H:%M:%S"
```

**`uptime` — Tell how long the system has been running:**

```bash
uptime
```

## 18. Mail and User Communication Commands

**`biff` — Be notified if mail arrives and who it is from:**

```bash
biff y
```

**`mailq` — Print the mail queue:**

```bash
mailq
```

**`write` — Send a message to another user:**

```bash
write username
```

**`wall` — Send a message to everybody's terminal:**

```bash
wall "System will go down in 10 minutes"
```

## 19. Printing and Media Commands

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

## 20. Shell Built-in and Scripting Commands

**`alias` — Define or display aliases:**

```bash
alias ll='ls -l'
```

**`bind` — Set Readline key bindings and variables:**

```bash
bind -P
```

**`break` — Exit from a for, while, or until loop:**

```bash
break
```

**`builtin` — Run a shell builtin, passing it args:**

```bash
builtin cd /tmp
```

**`case` — Conditional construct in shell scripts:**

```bash
case $VAR in ... esac
```

**`continue` — Resume the next iteration of a loop:**

```bash
continue
```

**`declare` — Set variables and attributes:**

```bash
declare -i NUM=5
```

**`enable` — Enable and disable shell builtins:**

```bash
enable -n cd
```

**`env` — Set environment and execute command, or print environment:**

```bash
env | grep USER
```

**`eval` — Construct command by concatenating arguments:**

```bash
eval "ls -l"
```

**`exec` — Replace the shell with the given command:**

```bash
exec bash
```

**`exit` — Exit the shell:**

```bash
exit 0
```

**`expect` — Programmed dialogue with interactive programs:**

```bash
expect script.exp
```

**`export` — Set export attribute for shell variables:**

```bash
export PATH=$PATH:/new/dir
```

**`expr` — Evaluate expressions:**

```bash
expr 5 + 3
```

**`factor` — Print the prime factors:**

```bash
factor 100
```

**`fc` — Process command history list:**

```bash
fc -l
```

**`function` — Define shell functions:**

```bash
function myfunc() { echo "hi"; }
```

**`for` — Loop construct:**

```bash
for i in {1..5}; do echo $i; done
```

**`if` — Conditional construct:**

```bash
if [ -f file ]; then echo "Exists"; fi
```

**`let` — Evaluate arithmetic expressions:**

```bash
let "a = 5 + 3"
```

**`printf` — Format and print data:**

```bash
`printf "Result: %04d
```

**`read` — Read a line from standard input:**

```bash
read -p "Enter name: " name
```

**`return` — Return from a shell function:**

```bash
return 1
```

**`select` — Generate menus from list of words:**

```bash
select opt in "A" "B"; do echo $opt; break; done
```

**`seq` — Print a sequence of numbers:**

```bash
seq 1 5
```

**`setsid` — Run a program in a new session:**

```bash
setsid my_script.sh
```

**`shift` — Shift positional parameters:**

```bash
shift 2
```

**`source` — Execute commands from a file in the current shell:**

```bash
source ~/.bashrc
```

**`type` — Display information about command type:**

```bash
type ls
```

**`until` — Loop construct:**

```bash
until [ $i -gt 5 ]; do ... done
```

**`while` — Loop construct:**

```bash
while true; do ... done
```

**`yes` — Output a string repeatedly until killed:**

```bash
yes "y" | rm -r dir/
```

**`sudo` — Execute a command as another user:**

```bash
sudo dnf update
```

**`sleep` — Delay for a specified amount of time:**

```bash
sleep 5
```

## 21. Bash Shortcuts Commands

### Navigation Shortcuts

| Shortcut   | Description                       |
| :--------- | :-------------------------------- |
| `Ctrl + A` | Move to the beginning of the line |
| `Ctrl + E` | Move to the end of the line       |
| `Ctrl + B` | Move back one character           |
| `Ctrl + F` | Move forward one character        |
| `Alt + B`  | Move back one word                |
| `Alt + F`  | Move forward one word             |

### Editing Shortcuts

| Shortcut   | Description                                                  |
| :--------- | :----------------------------------------------------------- |
| `Ctrl + U` | Cut/delete text from the cursor to the beginning of the line |
| `Ctrl + K` | Cut/delete text from the cursor to the end of the line       |
| `Ctrl + W` | Cut/delete the word before the cursor                        |
| `Ctrl + Y` | Paste the last cut text                                      |
| `Ctrl + L` | Clear the terminal screen                                    |
| `Ctrl + C` | Terminate the currently running command                      |

### History Shortcuts

| Shortcut   | Description                             |
| :--------- | :-------------------------------------- |
| `Ctrl + R` | Search command history (reverse search) |
| `Ctrl + G` | Exit history search mode                |
| `Ctrl + P` | Go to the previous command in history   |
| `Ctrl + N` | Go to the next command in history       |

## 22. Development and Build Automation Commands

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

## 23. Terminal and Session Management Commands

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

## 24. Help and Documentation Commands

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

## 25. Text Editors in Linux

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

## 26. IO Redirection Commands

**`cmd < file` — Redirect input:**

```bash
sort < names.txt
```

**`cmd > file` — Redirect output (overwrite):**

```bash
echo "Hello" > out.txt
```

**`cmd >> file` — Redirect output (append):**

```bash
echo "World" >> out.txt
```

**`cmd 2> file` — Redirect error output:**

```bash
ls no_exist_dir 2> errors.txt
```

**`cmd 2>&1` — Redirect stderr to stdout:**

```bash
make 2>&1 | tee build.log
```

**`cmd &> file` — Redirect stdout and stderr:**

```bash
make &> build.log
```

**`cmd 1>&2` — Redirect stdout to stderr:**

```bash
echo "Error!" 1>&2
```

**`cmd > /dev/null` — Discard standard output:**

```bash
ping 8.8.8.8 > /dev/null
```

**`cmd1 <(cmd2)` — Process substitution:**

```bash
diff <(ls dir1) <(ls dir2)
```

## 27. Environment Variable Commands

**`export VARIABLE_NAME=value` — Set and export an environment variable:**

```bash
export PATH=$PATH:/opt/bin
```

**`echo $VARIABLE_NAME` — Display value of a variable:**

```bash
echo $USER
```

**`env` — List all environment variables:**

```bash
env
```

**`unset VARIABLE_NAME` — Remove an environment variable:**

```bash
unset JAVA_HOME
```

**`export -p` — List all exported variables:**

```bash
export -p
```

**`env VAR1=value COMMAND` — Set variable temporarily for a command:**

```bash
env LC_ALL=C sort file.txt
```

**`printenv` — Display environment variables:**

```bash
printenv PATH
```
