## **Podman Command Line Cheat Sheet**
Podman is a daemonless, rootless container engine designed to manage containers, pods, and images, with a command-line interface nearly identical to Docker.

### ** Container Management**
| Action | Command |
| :--- | :--- |
| **List Running Containers** | `podman ps` |
| **List All Containers (Running & Stopped)** | `podman ps -a` |
| **Run a Container** | `podman run -dt --name [name] [image]` |
| **Run Interactively with Port Forwarding** | `podman run -it -p [host_port]:[container_port] [image]` |
| **Start a Stopped Container** | `podman start [name]` |
| **Stop a Container Gracefully** | `podman stop [name]` |
| **Restart a Container** | `podman restart [name]` |
| **Remove a Container** | `podman rm [name]` |
| **Force Remove a Running Container** | `podman rm -f [name]` |

### **🛠️ Execution & Inspection**
| Action | Command |
| :--- | :--- |
| **Open Shell Inside Container** | `podman exec -it [name] /bin/bash` |
| **Run Single Command Inside Container** | `podman exec [name] [command]` |
| **View Container Logs** | `podman logs [name]` |
| **Stream Container Logs Live** | `podman logs -f [name]` |
| **Inspect Container Details** | `podman inspect [name]` |
| **View Resource Usage (Stats)** | `podman stats` |

### **🖼️ Image Management**
| Action | Command |
| :--- | :--- |
| **List Local Images** | `podman images` |
| **Pull Image from Registry** | `podman pull [image_name]` |
| **Build Image from Containerfile/Dockerfile** | `podman build -t [tag_name] .` |
| **Remove a Local Image** | `podman rmi [image_id]` |
| **Tag an Image** | `podman tag [image] [new_image:tag]` |

### **Pods & Networking**
*Unlike Docker, Podman allows you to group containers into "Pods" (similar to Kubernetes pods).*
| Action | Command |
| :--- | :--- |
| **List Pods** | `podman pod ls` |
| **Create a New Pod** | `podman pod create --name [pod_name] -p [port]:[port]` |
| **Run Container Inside a Pod** | `podman run -d --pod [pod_name] --name [container_name] [image]` |
| **Stop a Pod** | `podman pod stop [pod_name]` |
| **Remove a Pod** | `podman pod rm [pod_name]` |
| **List Networks** | `podman network ls` |

### ** Volumes & Storage**
| Action | Command |
| :--- | :--- |
| **List Volumes** | `podman volume ls` |
| **Create a Volume** | `podman volume create [volume_name]` |
| **Inspect a Volume** | `podman volume inspect [volume_name]` |
| **Remove a Volume** | `podman volume rm [volume_name]` |
| **Prune Unused Data** | `podman system prune` |
