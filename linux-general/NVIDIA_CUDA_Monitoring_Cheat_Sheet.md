# Commands to monitor NVIDIA GPU performance and CUDA workloads.

## Hardware Monitoring Tools

| Command | Description |
| :--- | :--- |
| `watch -n 1 nvidia-smi` | Monitor GPU usage, VRAM consumption, and temperature, updating every 1 second. |
| `nvidia-smi -l 2` | Built-in looping mode, updating every 2 seconds. |
| `nvidia-smi --query-gpu=utilization.gpu,memory.used,temperature.gpu --format=csv -l 1` | Stream minimal GPU metrics to the console in CSV format. |
| `nvtop` | Interactive, `htop`-style visual monitor for NVIDIA GPUs (requires installation: `sudo dnf install nvtop`). |

## Process Management

| Command | Description |
| :--- | :--- |
| `fuser -v /dev/nvidia*` | Identify PID and users of applications currently accessing the NVIDIA GPU. |
| `nvidia-smi -q -d PIDS` | List detailed process information running on the GPU. |
| `kill -9 <PID>` | Force-terminate a frozen process locking GPU VRAM. |

## Prime Render Offload (Fedora/Wayland)

Launch any application utilizing the discrete NVIDIA GPU instead of integrated graphics by prepending these environment variables:

```bash
__NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia <application_executable>




