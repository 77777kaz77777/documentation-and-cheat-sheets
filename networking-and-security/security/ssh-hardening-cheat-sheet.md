# SSH and sshd Hardening Cheat Sheet

Quick-reference guide for SSH keys, client configuration, and locking down the OpenSSH server.

The goal is **key-only login**: no passwords, no direct root login, and SSH reachable only from networks you trust. Work through the sections in order and **keep an existing SSH session open** while you change the server, so a mistake can't lock you out.

---

## 1. Create and Use SSH Keys

```bash
# Create an Ed25519 key with a passphrase
ssh-keygen -t ed25519 -C "kaz@laptop"

# Copy the public key to a server
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@server

# Without ssh-copy-id
cat ~/.ssh/id_ed25519.pub | ssh user@server 'mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys'

# Test that the key works
ssh -i ~/.ssh/id_ed25519 -o PasswordAuthentication=no user@server
```

### Agent (Type the Passphrase Once)

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
ssh-add -l
```

KDE, GNOME, and macOS usually start an agent for you.

### Key Management

```bash
# Change a key's passphrase
ssh-keygen -p -f ~/.ssh/id_ed25519

# Show a key's fingerprint
ssh-keygen -lf ~/.ssh/id_ed25519.pub

# Remove an old host key after a server reinstall
ssh-keygen -R server
```

### Hardware Security Keys (FIDO2)

```bash
ssh-keygen -t ed25519-sk -C "kaz@yubikey"
```

The private key can't be used without the physical key plugged in and touched.

---

## 2. Client Configuration (`~/.ssh/config`)

```text
Host homelab
    HostName 100.101.102.103
    User kaz
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes

Host *.home.lan
    User kaz
    ForwardAgent no

Host *
    ServerAliveInterval 30
    AddKeysToAgent yes
```

```bash
chmod 600 ~/.ssh/config
ssh homelab
```

### Handy Client Commands

```bash
# Local port forward: reach a server's localhost:9090 at your localhost:9090
ssh -L 9090:localhost:9090 homelab

# Jump through a bastion host
ssh -J bastion user@internal-host

# Copy files
scp file.txt homelab:/tmp/
rsync -avz ./dir/ homelab:/srv/dir/
```

---

## 3. Harden the Server

Put your settings in a drop-in file so package updates don't overwrite them. OpenSSH uses the **first** value it reads for each setting, so a file named `00-` wins.

`/etc/ssh/sshd_config.d/00-hardening.conf`:

```text
# Authentication
PermitRootLogin no
PasswordAuthentication no
KbdInteractiveAuthentication no
PubkeyAuthentication yes
AuthenticationMethods publickey
PermitEmptyPasswords no

# Limit who and how often
AllowUsers kaz
MaxAuthTries 3
LoginGraceTime 30

# Reduce attack surface
X11Forwarding no
AllowAgentForwarding no
AllowTcpForwarding local
PermitTunnel no

# Drop dead sessions
ClientAliveInterval 300
ClientAliveCountMax 2
```

Check that the main `/etc/ssh/sshd_config` has `Include /etc/ssh/sshd_config.d/*.conf` near the top (Fedora, RHEL, Rocky, Debian, and Ubuntu do by default).

### Apply Safely

```bash
# 1. Check the syntax
sudo sshd -t

# 2. Show the effective settings
sudo sshd -T | grep -iE "permitrootlogin|passwordauthentication|kbdinteractive|allowusers|authenticationmethods"

# 3. Reload (existing sessions stay connected)
sudo systemctl reload sshd    # Debian/Ubuntu: ssh

# 4. In a NEW terminal, confirm you can still log in before closing the old one
ssh homelab
```

### Confirm Passwords Are Refused

```bash
ssh -o PubkeyAuthentication=no -o PreferredAuthentications=password user@server
```

You should see `Permission denied (publickey)` without a password prompt.

---

## 4. Restrict Where SSH Is Reachable

### firewalld: VPN Only

```bash
# Allow SSH only on the Tailscale interface
sudo firewall-cmd --permanent --zone=trusted --add-interface=tailscale0
sudo firewall-cmd --permanent --remove-service=ssh
sudo firewall-cmd --reload
sudo firewall-cmd --list-all --zone=trusted
```

After this, SSH only works over Tailscale. If Tailscale goes down you'll need a local console (keyboard and screen) to get back in.

### Listen Only on One Address

```text
ListenAddress 100.101.102.103
```

`sshd` starts before Tailscale on boot, so this can fail to bind. Firewall rules are usually the safer way to limit access.

### Change the Port (with SELinux)

A different port reduces log noise but isn't real security. If you do it, label the port for SELinux and open it:

```bash
sudo semanage port -a -t ssh_port_t -p tcp 2222
sudo firewall-cmd --permanent --add-port=2222/tcp && sudo firewall-cmd --reload
```

Then set `Port 2222` in the drop-in file and reload `sshd`.

---

## 5. Brute-Force Protection with Fail2ban

```bash
sudo dnf install fail2ban    # EPEL on RHEL/Rocky; apt install fail2ban on Debian
```

`/etc/fail2ban/jail.d/sshd.local`:

```ini
[sshd]
enabled = true
backend = systemd
maxretry = 5
findtime = 10m
bantime = 1h
```

```bash
sudo systemctl enable --now fail2ban
sudo fail2ban-client status sshd
sudo fail2ban-client set sshd unbanip 203.0.113.5
```

Not needed if SSH is only reachable over a VPN.

---

## 6. Audit & Monitor

```bash
# Successful and failed logins
sudo journalctl -u sshd --since today | grep -E "Accepted|Failed|Invalid"

# Currently logged-in users
who

# Last logins
last -n 20

# Check host key fingerprints (to compare on first connect)
for k in /etc/ssh/ssh_host_*_key.pub; do ssh-keygen -lf "$k"; done
```

`ssh-audit` (in many distro repos) scans a server and flags weak algorithms:

```bash
ssh-audit localhost
```

---

## 7. Troubleshooting

| Problem | Check |
| --- | --- |
| Key still asks for a password | Permissions: `~/.ssh` must be `700`, `authorized_keys` `600`, home not group-writable |
| `Permission denied (publickey)` | Wrong key offered: use `ssh -v` and `IdentitiesOnly yes` |
| Key ignored on SELinux systems | Run `restorecon -Rv ~/.ssh` |
| Settings seem ignored | An earlier file in `sshd_config.d/` sets them first; check `sshd -T` |
| `sshd` won't start after a port change | Missing `semanage port` label; see `journalctl -u sshd` |
| `REMOTE HOST IDENTIFICATION HAS CHANGED` | Server was reinstalled: verify, then `ssh-keygen -R host` |

```bash
# Verbose client output shows which keys are tried and why login fails
ssh -vvv homelab
```

---

## Quick Reference

```bash
ssh-keygen -t ed25519                  # create key
ssh-copy-id user@server                # install key
sudo sshd -t                           # check config syntax
sudo sshd -T | grep -i password        # effective settings
sudo systemctl reload sshd             # apply changes
ssh -vvv host                          # debug login
sudo journalctl -u sshd -f             # watch logins
```

---

## Sources & Verification

- **Server options:** [sshd_config(5)](https://man.openbsd.org/sshd_config)
- **Client options:** [ssh_config(5)](https://man.openbsd.org/ssh_config)

## Related guides

- [Firewalld Cheat Sheet](fedora-firewall-cheat-sheet.md)
- [Fedora SELinux Management Cheat Sheet](fedora-selinux-management-cheat-sheet.md)
- [Security Auditing Cheat Sheet](security-auditing-cheat-sheet.md)
- [Tailscale Mesh Networking Cheat Sheet](../networking/tailscale-mesh-cli-cheat-sheet.md)
