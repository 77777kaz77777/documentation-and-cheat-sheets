## provides a quick-reference guide for using the grubby utility to view, switch, and modify Linux kernel boot parameters and default entries directly from the command line

## Viewing Kernel Information

| Action | Command Syntax | Example |
| :--- | :--- | :--- |
| Display the current default kernel path | `sudo grubby --default-kernel` | `sudo grubby --default-kernel` |
| View detailed boot config for a specific kernel | `sudo grubby --info=/path/to/vmlinuz` | `sudo grubby --info=/boot/vmlinuz-7.2.4-200.fc44.x86_64` |
| List configuration for all installed kernels | `sudo grubby --info=ALL` | `sudo grubby --info=ALL` |

## Managing the Default Boot Kernel

| Action | Command Syntax | Example |
| :--- | :--- | :--- |
| Set a new default kernel using explicit path | `sudo grubby --set-default=/path/to/vmlinuz` | `sudo grubby --set-default=/boot/vmlinuz-7.2.4-200.fc44.x86_64` |
| Set a new default kernel using menu index (0 is first) | `sudo grubby --set-default-index=<index>` | `sudo grubby --set-default-index=0` |

## Modifying Kernel Boot Arguments

| Action | Command Syntax | Example |
| :--- | :--- | :--- |
| Add or modify arguments for a specific kernel | `sudo grubby --update-kernel=/path/to/vmlinuz --args="<args>"` | `sudo grubby --update-kernel=/boot/vmlinuz-7.2.4-200.fc44.x86_64 --args="intel_pstate=disable"` |
| Add or modify arguments across all kernels | `sudo grubby --update-kernel=ALL --args="<args>"` | `sudo grubby --update-kernel=ALL --args="mitigations=off"` |
| Remove arguments from a specific kernel | `sudo grubby --update-kernel=/path/to/vmlinuz --remove-args="<args>"` | `sudo grubby --update-kernel=/boot/vmlinuz-7.2.4-200.fc44.x86_64 --remove-args="rhgb quiet"` |
| Remove arguments across all kernels | `sudo grubby --update-kernel=ALL --remove-args="<args>"` | `sudo grubby --update-kernel=ALL --remove-args="rhgb quiet"` |
| Add and remove arguments concurrently | `sudo grubby --update-kernel=<target> --args="<args>" --remove-args="<args>"` | `sudo grubby --update-kernel=ALL --args="nomodeset" --remove-args="rhgb quiet"` |
