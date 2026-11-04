# Quick-reference CLI and syntax cheat sheet for Ansible

## 🚀 Ansible Ad-Hoc Commands

**Ping all hosts:**
```bash
ansible all -m ping
```

**Ping with custom inventory:**
```bash
ansible all -i inventory.ini -m ping
```

**Check uptime:**
```bash
ansible all -a "uptime"
```

**Install a package:**
```bash
ansible webservers -m apt -a "name=nginx state=present" --become
```

**Restart a service:**
```bash
ansible db -m service -a "name=mysql state=restarted" --become
```

**Copy a file:**
```bash
ansible all -m copy -a "src=/etc/hosts dest=/tmp/hosts"
```

**Gather facts:**
```bash
ansible hostname -m setup
```

## 📝 Playbook Management

**Run a playbook:**
```bash
ansible-playbook site.yml
```

**Run with custom inventory:**
```bash
ansible-playbook -i inventory.ini site.yml
```

**Check for syntax errors:**
```bash
ansible-playbook site.yml --syntax-check
```

**Dry run (Check mode):**
```bash
ansible-playbook site.yml --check
```

**Run specific tags:**
```bash
ansible-playbook site.yml --tags "packages,config"
```

**Skip specific tags:**
```bash
ansible-playbook site.yml --skip-tags "debug"
```

**Limit to one host/group:**
```bash
ansible-playbook site.yml --limit "webserver01"
```

**Step-by-step execution:**
```bash
ansible-playbook site.yml --step
```

## 🔐 Ansible Vault (Secrets)

**Create encrypted file:**
```bash
ansible-vault create secret.yml
```

**Encrypt existing file:**
```bash
ansible-vault encrypt vars.yml
```

**Decrypt a file:**
```bash
ansible-vault decrypt vars.yml
```

**Edit encrypted file:**
```bash
ansible-vault edit secret.yml
```

**Run with vault pass prompt:**
```bash
ansible-playbook site.yml --ask-vault-pass
```

**Run with vault pass file:**
```bash
ansible-playbook site.yml --vault-password-file ~/.vault_pass.txt
```

## 🏗️ Inventory & Roles

**List hosts in a group:**
```bash
ansible webservers --list-hosts
```

**Create a new role:**
```bash
ansible-galaxy init my_new_role
```

**Install role from Galaxy:**
```bash
ansible-galaxy install geerlingguy.apache
```

**Install roles from requirements:**
```bash
ansible-galaxy install -r requirements.yml
```

**List installed roles:**
```bash
ansible-galaxy list
```

## 🔍 Useful Variables & Debugging

- **Debug a variable:**

```yaml
- name: Print a variable
  debug:
    msg: "The value of foo is {{ foo }}"
```

- **Common Magic Variables:**
  - `{{ inventory_hostname }}`: The name of the current host as defined in the inventory.
  - `{{ groups['webservers'] }}`: List of all hosts in the 'webservers' group.
  - `{{ ansible_default_ipv4.address }}`: The primary IP of the managed node (requires fact-gathering).
  - `{{ hostvars['hostname']['var_name'] }}`: Access variables assigned to another host.

## 🛠️ Configuration Tips

- **The `ansible.cfg` file:** Ansible evaluates configuration files in the following order of precedence:
  1. `ANSIBLE_CONFIG` (environment variable)
  2. `./ansible.cfg` (current directory)
  3. `~/.ansible.cfg` (user home directory)
  4. `/etc/ansible/ansible.cfg` (default)
- **Privilege Escalation (Become):**
  - Use `--become` (or `-b`) to run operations with privileges (default sudo).
  - Use `-K` (or `--ask-become-pass`) in the CLI to prompt for the sudo password.
  - Use `--become-user [user]` to escalate to a user other than root.
