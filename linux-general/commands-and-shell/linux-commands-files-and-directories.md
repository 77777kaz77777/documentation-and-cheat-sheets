# Linux Commands: Files and Directories

Create, copy, move, find, archive and verify files, and manage permissions and ownership.

Part of the [Linux commands cheat sheet](linux-commands-cheat-sheet-tables.md).

## File Operations Commands

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

## Directory Operations Commands

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

## File Permission and Ownership Commands

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

## Compression and Archiving Commands

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

## Checksum and File Integrity Commands

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
