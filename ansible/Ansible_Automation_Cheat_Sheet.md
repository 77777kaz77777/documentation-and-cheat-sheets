# Quick-reference CLI and syntax cheat sheet for Ansible
## 🚀 Ansible Ad-Hoc Commands

| Action | Command |
| :--- | :--- |
| **Ping all hosts** | `ansible all -m ping` |
| **Ping with custom inventory** | `ansible all -i inventory.ini -m ping` |
| **Check uptime** | `ansible all -a "uptime"` |
| **Install a package** | `ansible webservers -m apt -a "name=nginx state=present" --become` |
| **Restart a service** | `ansible db -m service -a "name=mysql state=restarted" --become` |
| **Copy a file** | `ansible all -m copy -a "src=/etc/hosts dest=/tmp/hosts"` |
| **Gather facts** | `ansible hostname -m setup` |

## 📝 Playbook Management

| Action | Command |
| :--- | :--- |
| **Run a playbook** | `ansible-playbook site.yml` |
| **Run with custom inventory** | `ansible-playbook -i inventory.ini site.yml` |
| **Check for syntax errors** | `ansible-playbook site.yml --syntax-check` |
| **Dry run (Check mode)** | `ansible-playbook site.yml --check` |
| **Run specific tags** | `ansible-playbook site.yml --tags "packages,config"` |
| **Skip specific tags** | `ansible-playbook site.yml --skip-tags "debug"` |
| **Limit to one host/group** | `ansible-playbook site.yml --limit "webserver01"` |
| **Step-by-step execution**| `ansible-playbook site.yml --step` |

## 🔐 Ansible Vault (Secrets)

| Action | Command |
| :--- | :--- |
| **Create encrypted file** | `ansible-vault create secret.yml` |
| **Encrypt existing file** | `ansible-vault encrypt vars.yml` |
| **Decrypt a file** | `ansible-vault decrypt vars.yml` |
| **Edit encrypted file** | `ansible-vault edit secret.yml` |
| **Run with vault pass prompt** | `ansible-playbook site.yml --ask-vault-pass` |
| **Run with vault pass file** | `ansible-playbook site.yml --vault-password-file ~/.vault_pass.txt` |

## 🏗️ Inventory & Roles

| Action | Command |
| :--- | :--- |
| **List hosts in a group** | `ansible webservers --list-hosts` |
| **Create a new role** | `ansible-galaxy init my_new_role` |
| **Install role from Galaxy**| `ansible-galaxy install geerlingguy.apache` |
| **Install roles from requirements**| `ansible-galaxy install -r requirements.yml` |
| **List installed roles** | `ansible-galaxy list` |

## 🔍 Useful Variables & Debugging

* **Debug a variable:**

```yaml
- name: Print a variable
  debug:
    msg: "The value of foo is {{ foo }}"
```

* **Common Magic Variables:**
  * `{{ inventory_hostname }}`: The name of the current host as defined in the inventory.
  * `{{ groups['webservers'] }}`: List of all hosts in the 'webservers' group.
  * `{{ ansible_default_ipv4.address }}`: The primary IP of the managed node (requires fact-gathering).
  * `{{ hostvars['hostname']['var_name'] }}`: Access variables assigned to another host.

## 🛠️ Configuration Tips

* **The `ansible.cfg` file:** Ansible evaluates configuration files in the following order of precedence:
  1. `ANSIBLE_CONFIG` (environment variable)
  2. `./ansible.cfg` (current directory)
  3. `~/.ansible.cfg` (user home directory)
  4. `/etc/ansible/ansible.cfg` (default)
* **Privilege Escalation (Become):** 
  * Use `--become` (or `-b`) to run operations with privileges (default sudo). 
  * Use `-K` (or `--ask-become-pass`) in the CLI to prompt for the sudo password.
  * Use `--become-user [user]` to escalate to a user other than root.
