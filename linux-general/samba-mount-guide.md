## Commands and configurations for connecting, temporarily mounting, and permanently automounting local SMB/CIFS network shares.

## Connecting via Dolphin (GUI)

* Open the **Dolphin** file manager.
* Press **Ctrl + L** to focus the address bar.
* Type `smb://ip` and press **Enter**.
* Enter your Samba username and password when prompted.
* Right-click the connected folder in the main view and select **Add to Places** to pin it permanently to your sidebar.

## Permanent Mount via /etc/fstab (CLI)

* Install the required CIFS utilities:
  ~~~bash
  sudo dnf install cifs-utils
  ~~~

* Create a local directory for the mount point:
  ~~~bash
  sudo mkdir -p /mnt/network_drive
  ~~~

* Create a secure file to store your credentials:
  ~~~bash
  nano ~/.smbcredentials
  ~~~

* Add your Samba login details to the file:
  ~~~ini
  username=your_samba_user
  password=your_samba_password
  ~~~

* Restrict permissions on the credentials file:
  ~~~bash
  chmod 600 ~/.smbcredentials
  ~~~

* Edit your filesystem table:
  ~~~bash
  sudo nano /etc/fstab
  ~~~

* Append this line to the bottom of the file (update the IP, share name, and your Linux username):
  ~~~fstab
  //ip/<share_name> /mnt/network_drive cifs credentials=/home/<your_username>/.smbcredentials,uid=1000,gid=1000,iocharset=utf8,x-systemd.automount 0 0
  ~~~

* Reload the system daemon and mount the drive:
  ~~~bash
  sudo systemctl daemon-reload
  sudo mount -a
  ~~~
