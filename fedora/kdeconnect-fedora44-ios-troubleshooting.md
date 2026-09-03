## KDE Connect fails to pair or discover devices (specifically iPhones) on Fedora 44 KDE Plasma, even after adding firewall rules to the `home` zone

# Troubleshooting KDE Connect: Fedora 44 KDE to iOS

**Issue:** KDE Connect fails to pair or discover devices (specifically iPhones) on Fedora 44 KDE Plasma, even after adding firewall rules to the `home` zone.

**Root Causes:**

1. Fedora's active network interface defaults to `FedoraWorkstation` or `public` zones, causing `home` zone rules to be ignored.
2. Fedora 44 (Plasma 6) utilizes D-Bus activation for KDE Connect; standard `systemctl` restart commands will fail if the daemon is killed.
3. iOS aggressively filters UDP broadcast packets, often requiring manual IP configuration.

---

## Step 1: Clear Stale Configurations

Start from a clean slate by killing any hung processes and backing up the old configuration files.

```bash
killall kdeconnectd
mv ~/.config/kdeconnect ~/.config/kdeconnect.bak
```

## Step 2: Apply Firewall Rules to the Correct Zones

Fedora defaults active connections to `FedoraWorkstation` or `public`. Apply the KDE Connect service rules to these zones instead of `home`.

```bash
sudo firewall-cmd \
  --permanent \
  --zone=FedoraWorkstation \
  --add-service=kdeconnect

sudo firewall-cmd \
  --permanent \
  --zone=public \
  --add-service=kdeconnect

sudo firewall-cmd --reload
```

*Verification:* Check your active zone with `firewall-cmd --get-active-zones` to ensure your interface (e.g., `wlan0`) is covered by the zones above.

## Step 3: Restart the KDE Connect Daemon

Because Fedora 44 uses D-Bus for KDE Connect, `systemctl --user restart plasma-kdeconnect.service` will return an error. Use the direct executable or D-Bus refresh instead.

**Option A (Direct execution):**

```bash
/usr/libexec/kdeconnectd &
```

**Option B (Trigger via D-Bus):**

```bash
kdeconnect-cli --refresh
```

*Verification:* Run `kdeconnect-cli -l`. If it outputs a list of devices (even if it says 0 devices found) without a D-Bus error, the daemon is successfully running.

## Step 4: Force iOS Pairing via IP Address (If Auto-Discovery Fails)

If the firewall is open and the daemon is running but the iPhone still cannot see the Fedora machine, bypass UDP broadcast restrictions by directly inputting the local IP.

1. Retrieve the Fedora machine's local IP address:

```bash
ip -br a
```

*(Note the IPv4 address assigned to your active connection, e.g., `192.168.8.x` on a GL.iNet router).*

1. Open the KDE Connect app on the iPhone.
2. Tap the **three-dot menu** (top right corner).
3. Select **Add device by IP**.
4. Input the Fedora machine's IPv4 address and initiate pairing.

---

**Sources & Verification:**

* Commands utilize standard Fedora Linux native tooling (`firewalld` for port management, `iproute2` for network queries).
* Daemon paths reflect the official KDE Plasma 6 file system hierarchy (`/usr/libexec/kdeconnectd`).
* Workarounds for iOS discovery align with KDE Connect official documentation for Apple devices.
