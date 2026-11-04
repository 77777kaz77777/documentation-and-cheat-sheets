# Commands to monitor NVIDIA GPU performance and CUDA workloads

## Hardware Monitoring Tools

**Monitor GPU usage, VRAM consumption, and temperature, updating every 1 second:**
```bash
watch -n 1 nvidia-smi
```

**Built-in looping mode, updating every 2 seconds:**
```bash
nvidia-smi -l 2
```

**Stream minimal GPU metrics to the console in CSV format:**
```bash
nvidia-smi --query-gpu=utilization.gpu,memory.used,temperature.gpu --format=csv -l 1
```

**Interactive, `htop`-style visual monitor for NVIDIA GPUs (requires installation: `sudo dnf install nvtop`):**
```bash
nvtop
```

## Process Management

**Identify PID and users of applications currently accessing the NVIDIA GPU:**
```bash
fuser -v /dev/nvidia*
```

**List detailed process information running on the GPU:**
```bash
nvidia-smi -q -d PIDS
```

**Force-terminate a frozen process locking GPU VRAM:**
```bash
kill -9 <PID>
```

## Prime Render Offload (Fedora/Wayland)

Launch any application utilizing the discrete NVIDIA GPU instead of integrated graphics by prepending these environment variables:

```bash
__NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia <application_executable>

```
