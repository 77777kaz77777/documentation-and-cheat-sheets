# Linux Commands: Shell and Text Processing

Shell built-ins and scripting, keyboard shortcuts, redirection, environment variables and text tools.

Part of the [Linux commands cheat sheet](linux-commands-cheat-sheet-tables.md).

## Shell Built-in and Scripting Commands

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

## Bash Shortcuts Commands

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

## IO Redirection Commands

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

## Environment Variable Commands

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

## Text Processing and Formatting Commands

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
