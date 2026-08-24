# Advanced Linux Permissions, Ownership, and Access Control Reference Guide

## 1. Numeric (Octal) Permission Breakdown

Permissions are represented by a 3-digit (or 4-digit) octal number. Each digit is the sum of the permissions for **Owner (u)**, **Group (g)**, and **Others (o)**.

### Permission Values
*   **4:** Read (`r`) - Ability to view file contents or list directory contents.
*   **2:** Write (`w`) - Ability to modify file contents or add/remove files in a directory.
*   **1:** Execute (`x`) - Ability to run a file as a program or enter a directory (`cd`).
*   **0:** No permission (`-`)

---

## 2. Symbolic Permission Notation

Instead of numbers, permissions can be modified using letters to add (`+`), remove (`-`), or exactly set (`=`) access.

### Targets
*   **u:** User (Owner)
*   **g:** Group
*   **o:** Others
*   **a:** All (User, Group, and Others)

### Examples of Symbolic Modifications

**Add execute permission for the owner:**
~~~bash
chmod \
  u+x \
  <file>
~~~

**Remove write permission for group and others:**
~~~bash
chmod \
  go-w \
  <file>
~~~

**Set exact permissions (read/write for owner, read-only for group/others):**
~~~bash
chmod \
  u=rw,go=r \
  <file>
~~~

---

## 3. Special Permissions (SUID, SGID, and Sticky Bit)

Special bits alter the default execution or ownership behavior.

### SUID (Set Owner User ID)
*   **Numeric:** `4000` (e.g., `4755`)
*   **Symbolic:** `u+s`
*   **Function:** Executes the file with the privileges of the file's owner (commonly root), not the user running it (e.g., `/usr/bin/passwd`).

~~~bash
chmod \
  u+s \
  <executable_file>
~~~

### SGID (Set Group ID)
*   **Numeric:** `2000` (e.g., `2755`)
*   **Symbolic:** `g+s`
*   **Function:** On a file, runs it with group privileges. On a directory, forces all newly created files within it to inherit the directory's group ownership rather than the creator's primary group.

~~~bash
chmod \
  g+s \
  <shared_directory>
~~~

### Sticky Bit
*   **Numeric:** `1000` (e.g., `1777`)
*   **Symbolic:** `+t`
*   **Function:** Used on shared directories (`/tmp`). Prevents users from deleting or renaming files they do not own, even if they have write access to the directory.

~~~bash
chmod \
  +t \
  <shared_directory>
~~~

---

## 4. Comprehensive Numeric Configuration Matrix

### Common Production & Desktop Permissions

**777 (rwxrwxrwx)**
*   Read, write, and execute for everyone. (Dangerous for sensitive files).

~~~bash
chmod \
  777 \
  <file_or_directory>
~~~

**755 (rwxr-xr-x)**
*   Owner has full access; group and others have read and execute access. (Standard for directories and executable scripts).

~~~bash
chmod \
  755 \
  <file_or_directory>
~~~

**700 (rwx------)**
*   Owner has full access; group and others have no access. (Standard for private directories like `~/.ssh`).

~~~bash
chmod \
  700 \
  <file_or_directory>
~~~

**644 (rw-r--r--)**
*   Owner can read and write; group and others can only read. (Standard for configuration files and documents).

~~~bash
chmod \
  644 \
  <file_or_directory>
~~~

**600 (rw-------)**
*   Owner can read and write; group and others have no access. (Standard for private files like SSH private keys).

~~~bash
chmod \
  600 \
  <file_or_directory>
~~~

---

## 5. Changing Permissions and Ownership Commands

**Modify file or directory permissions recursively.**
~~~bash
chmod \
  -R \
  755 \
  <path>
~~~

**Change file owner and group.**
~~~bash
chown \
  <user>:<group> \
  <file_or_directory>
~~~

**Change file owner recursively.**
~~~bash
chown \
  -R \
  <user> \
  <directory>
~~~

**View current permissions, ownership, and hidden files.**
~~~bash
ls \
  -la \
  <path>
~~~

---

## 6. Access Control Lists (ACLs)

Standard permissions only allow one owner and one group. ACLs permit assigning permissions to specific additional users or groups.

**View current ACLs on a file or directory.**
~~~bash
getfacl \
  <file_or_directory>
~~~

**Modify (add/change) an ACL to give a specific user read and write access.**
~~~bash
setfacl \
  -m \
  u:<specific_user>:rw \
  <file_or_directory>
~~~

**Remove a specific user's ACL entry.**
~~~bash
setfacl \
  -x \
  u:<specific_user> \
  <file_or_directory>
~~~

**Remove all ACLs from a file.**
~~~bash
setfacl \
  -b \
  <file_or_directory>
~~~

---

## 7. Extended File Attributes (Immutable Files)

Attributes sit below standard permissions and can restrict root users. Highly relevant for protecting critical system files or BTRFS subvolume roots.

**Make a file immutable (cannot be deleted, renamed, or modified by anyone, including root).**
~~~bash
sudo \
  chattr \
  +i \
  <file>
~~~

**Remove the immutable attribute.**
~~~bash
sudo \
  chattr \
  -i \
  <file>
~~~

**List extended attributes on a file.**
~~~bash
lsattr \
  <file>
~~~

---

## 8. SELinux Security Contexts 

For systems enforcing SELinux, standard permissions are evaluated first, followed by SELinux policies.

**List files with their SELinux security contexts.**
~~~bash
ls \
  -Z \
  <path>
~~~

**Restore the default SELinux context for a file based on system policy (useful after moving files).**
~~~bash
restorecon \
  -v \
  <file_or_directory>
~~~

**Change a file's SELinux context type manually.**
~~~bash
chcon \
  -t \
  <context_type> \
  <file>
~~~
