# Linux Commands: Users, Processes and System

Users and groups, processes and jobs, disks, hardware info, kernel modules, power, logs and time.

Part of the [Linux commands cheat sheet](linux-commands-cheat-sheet-tables.md).

## User Management Commands

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

## Group Management Commands

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

## Process Management Commands

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

## Job Scheduling Commands

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

## Disk and File System Commands

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

## Hardware and System Information Commands

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

## Kernel and Module Management Commands

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

## System Control and Power Commands

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

## Logging and Monitoring Commands

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

## Date and Time Commands

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
