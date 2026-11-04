## Essential commands for running daemonless containers with Podman

Podman is a daemonless, rootless container engine designed to manage containers, pods, and images, with a command-line interface nearly identical to Docker.

### **Container Management**

**List Running Containers:**
```bash
podman ps
```

**List All Containers (Running & Stopped):**
```bash
podman ps -a
```

**Run a Container:**
```bash
podman run -dt --name [name] [image]
```

**Run Interactively with Port Forwarding:**
```bash
podman run -it -p [host_port]:[container_port] [image]
```

**Start a Stopped Container:**
```bash
podman start [name]
```

**Stop a Container Gracefully:**
```bash
podman stop [name]
```

**Restart a Container:**
```bash
podman restart [name]
```

**Remove a Container:**
```bash
podman rm [name]
```

**Force Remove a Running Container:**
```bash
podman rm -f [name]
```

### **Execution & Inspection**

**Open Shell Inside Container:**
```bash
podman exec -it [name] /bin/bash
```

**Run Single Command Inside Container:**
```bash
podman exec [name] [command]
```

**View Container Logs:**
```bash
podman logs [name]
```

**Stream Container Logs Live:**
```bash
podman logs -f [name]
```

**Inspect Container Details:**
```bash
podman inspect [name]
```

**View Resource Usage (Stats):**
```bash
podman stats
```

### **Image Management**

**List Local Images:**
```bash
podman images
```

**Pull Image from Registry:**
```bash
podman pull [image_name]
```

**Build Image from Containerfile/Dockerfile:**
```bash
podman build -t [tag_name] .
```

**Remove a Local Image:**
```bash
podman rmi [image_id]
```

**Tag an Image:**
```bash
podman tag [image] [new_image:tag]
```

### **Pods & Networking**

_Unlike Docker, Podman allows you to group containers into "Pods" (similar to Kubernetes pods)._

**List Pods:**
```bash
podman pod ls
```

**Create a New Pod:**
```bash
podman pod create --name [pod_name] -p [port]:[port]
```

**Run Container Inside a Pod:**
```bash
podman run -d --pod [pod_name] --name [container_name] [image]
```

**Stop a Pod:**
```bash
podman pod stop [pod_name]
```

**Remove a Pod:**
```bash
podman pod rm [pod_name]
```

**List Networks:**
```bash
podman network ls
```

### **Volumes & Storage**

**List Volumes:**
```bash
podman volume ls
```

**Create a Volume:**
```bash
podman volume create [volume_name]
```

**Inspect a Volume:**
```bash
podman volume inspect [volume_name]
```

**Remove a Volume:**
```bash
podman volume rm [volume_name]
```

**Prune Unused Data:**
```bash
podman system prune
```
