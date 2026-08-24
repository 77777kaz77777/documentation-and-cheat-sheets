This document provides a step-by-step procedure for configuring a Fedora Linux system to automatically decrypt a LUKS2-encrypted root volume during the boot process #utilizing the hardware TPM (Trusted Platform Module) 2.0 chip. By implementing `systemd-cryptenroll`, this configuration binds the decryption key to PCR 7 (Secure Boot #state). This ensures seamless, passwordless boots under normal conditions, while automatically reverting to a manual passphrase prompt if the hardware configuration or #Secure Boot environment is modified or tampered with.

## 1. Install Dependencies

Install the required packages to interact with the TPM 2.0 chip using `systemd-cryptenroll`.

**Command:**

```bash
sudo dnf \
install \
tpm2-tss \
tpm2-tools
```

**Example Output:**

```text
Dependencies resolved.
================================================================================
 Package             Architecture   Version              Repository        Size
================================================================================
Installing:
 tpm2-tools          x86_64         5.5-1.fc44           fedora           1.2 M
 tpm2-tss            x86_64         4.0.1-3.fc44         fedora           1.5 M

Transaction Summary
================================================================================
Install  2 Packages
...
Complete!
```

## 2. Configure Dracut for Early Boot

The `initramfs` must load the TPM modules before attempting to mount the encrypted root filesystem. Create the required configuration file.

**Command:**

```bash
echo 'add_dracutmodules+=" tpm2-tss "' \
| sudo tee \
/etc/dracut.conf.d/tpm2.conf
```

**Full File Content (`/etc/dracut.conf.d/tpm2.conf`):**

```text
add_dracutmodules+=" tpm2-tss "
```

## 3. Identify Your LUKS Device Partition

Find the exact partition containing your encrypted volume.

**Command:**

```bash
lsblk \
-f
```

## 4. Enroll the TPM into the LUKS Volume

Bind the unlock process to PCR 7, which ensures the drive only unlocks if the Secure Boot state remains untampered. Replace `/dev/<YOUR_PARTITION>` with the specific partition identified in the previous step.

**Command:**

```bash
sudo systemd-cryptenroll \
--tpm2-device=auto \
--tpm2-pcrs=7 \
/dev/<YOUR_PARTITION>
```

**Example Output:**

```text
New TPM2 token enrolled as key slot 1.
```

*(You can verify the enrollment with `sudo systemd-cryptenroll /dev/<YOUR_PARTITION>`, which will show the new `tpm2` keyslot alongside your existing password slot.)*

## 5. Update Crypttab

Modify your configuration to instruct the system to use the TPM during boot by adding the `tpm2-device=auto` option. Replace `<YOUR-UUID>` with the exact UUID of your LUKS partition.

**Command:**

```bash
sudo nano \
/etc/crypttab
```

**Full Updated File Template (`/etc/crypttab`):**

```text
luks-<YOUR-UUID> \
UUID=<YOUR-UUID> \
none \
discard,tpm2-device=auto
```

## 6. Rebuild Initramfs and Reboot

Apply the changes to the boot image and restart the machine to verify the configuration.

**Commands:**

```bash
sudo dracut \
-f \
--regenerate-all
```

```bash
sudo \
reboot
```

**Example Output (dracut):**

```text
dracut: Executing: /usr/bin/dracut -f --regenerate-all
dracut: *** Including module: tpm2-tss ***
dracut: *** Including module: crypt ***
dracut: *** Creating image file '/boot/initramfs-6.9.X-XXX.fc44.x86_64.img' ***
dracut: *** Creating initramfs image file '/boot/initramfs-6.9.X-XXX.fc44.x86_64.img' done ***
```

---

**Sources & Verification:**

* **ArchWiki:** Systemd-cryptenroll and TPM 2.0 configuration
* **Freedesktop.org Manual:** crypttab(5) syntax for `tpm2-device`
* **Fedora Magazine:** Native LUKS decoupling and TPM integration documentation
