# Ansible Automation Cheat Sheet

## 🚀 Ansible Ad-Hoc Commands

| Action | Command |
| :--- | :--- |
| **Ping all hosts** | `ansible all -m ping` |
| **Check uptime** | `ansible all -a "uptime"` |
| **Install a package** | `ansible webservers -m apt -a "name=nginx state=present" --become` |
| **Restart a service** | `ansible db -m service -a "name=mysql state=restarted" --become` |
| **Copy a file** | `ansible all -m copy -a "src=/etc/hosts dest=/tmp/hosts"` |
| **Gather facts** | `ansible hostname -m setup` |

## 📝 Playbook Management

| Action | Command |
| :--- | :--- |
| **Run a playbook** | `ansible-playbook site.yml` |
| **Check for syntax errors** | `ansible-playbook site.yml --syntax-check` |
| **Dry run (Check mode)** | `ansible-playbook site.yml --check` |
| **Run specific tags** | `ansible-playbook site.yml --tags "packages,config"` |
| **Skip specific tags** | `ansible-playbook site.yml --skip-tags "debug"` |
| **Limit to one host** | `ansible-playbook site.yml --limit "webserver01"` |

## 🔐 Ansible Vault (Secrets)

| Action | Command |
| :--- | :--- |
| **Create encrypted file** | `ansible-vault create secret.yml` |
| **Encrypt existing file** | `ansible-vault encrypt vars.yml` |
| **Decrypt a file** | `ansible-vault decrypt vars.yml` |
| **Edit encrypted file** | `ansible-vault edit secret.yml` |
| **Run with vault pass** | `ansible-playbook site.yml --ask-vault-pass` |

## 🏗️ Inventory & Roles

* **List hosts in a group:** `ansible [group_name] --list-hosts`
* **Create a new role:** `ansible-galaxy init my_new_role`
* **Install role from Galaxy:** `ansible-galaxy install geerlingguy.apache`
* **List installed roles:** `ansible-galaxy list`

## 🔍 Useful Variables & Debugging

* **Debug a variable:**

```yaml
- name: Print a variable
  debug:
    msg: "The value of foo is {{ foo }}"
```

* **Common Magic Variables:**
  * `{{ inventory_hostname }}`: The name of the current host being configured.
  * `{{ groups['webservers'] }}`: List of all hosts in the 'webservers' group.
  * `{{ ansible_default_ipv4.address }}`: The primary IP of the managed node.

## 🛠️ Configuration Tips

* **The `ansible.cfg` file:** Ansible looks for configuration in the current directory first, then `~/.ansible.cfg`, then `/etc/ansible/ansible.cfg`.
* **Become (Sudo):** Use `--become` or `-K` in the CLI to prompt for the sudo password.
