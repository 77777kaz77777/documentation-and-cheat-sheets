## SELinux Context Resolution

The SELinux denial occurs because `fedora.img` currently has an `unlabeled_t` context. The virtualization daemon (`rpc-virtqemud`) requires virtual machine disk images to have the `virt_image_t` context to access and manage them securely.

To permanently resolve this and prevent future denials for new virtual machines in your storage pool, you must define the default SELinux context for the directory and apply it to all existing files within it.

### Execution Steps

Execute the following commands to update the SELinux policy and restore the correct labels:

```bash
sudo semanage fcontext \
  -a \
  -t virt_image_t \
  "/mnt/storage/vms(/.*)?"

sudo restorecon \
  -R \
  -v \
  /mnt/storage/vms
```

### Command Breakdown

* The `semanage` command permanently adds a rule to the SELinux policy, ensuring any file created in `/mnt/storage/vms` is automatically labeled as `virt_image_t`.
* The `restorecon` command traverses the directory recursively (`-R`) and applies the newly defined policy to `fedora.img` and any other existing files, outputting the changes (`-v`).

### Verification & Sources
* The `semanage fcontext` and `restorecon` commands are standard, verified procedures for SELinux labeling on RHEL/Fedora-based systems.
* Source: Red Hat Official Documentation - [Managing confined services (SELinux for Virtualization)](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/using_selinux/managing-confined-services_using-selinux)

Did the virtual machine boot successfully after applying the SELinux context update?
