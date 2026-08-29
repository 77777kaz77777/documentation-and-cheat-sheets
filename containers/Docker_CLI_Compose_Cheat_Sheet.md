## Core commands for spinning up Docker containers, managing images, and using Compose.

##  Docker CLI Essentials
| Action | Command |
| :--- | :--- |
| **Run a Container** | `docker run -d --name [name] [image]` |
| **List Running Containers** | `docker ps` |
| **List All Containers** | `docker ps -a` |
| **Stop a Container** | `docker stop [container_id/name]` |
| **Start a Container** | `docker start [container_id/name]` |
| **Remove a Container** | `docker rm -f [container_id/name]` |
| **List Local Images** | `docker images` |
| **Remove an Image** | `docker rmi [image_id]` |
| **View Logs** | `docker logs -f [container_name]` |
| **Enter Container Shell** | `docker exec -it [container_name] /bin/bash` |
| **Prune (Clean) System** | `docker system prune -a` |

##  Docker Compose Commands
| Action | Command |
| :--- | :--- |
| **Start Services (Background)** | `docker-compose up -d` |
| **Stop & Remove Services** | `docker-compose down` |
| **Stop Services (Keep Data)** | `docker-compose stop` |
| **Build/Rebuild Services** | `docker-compose build` |
| **View Composite Logs** | `docker-compose logs -f` |
| **Check Service Status** | `docker-compose ps` |
| **Restart Services** | `docker-compose restart` |
| **Pull New Images** | `docker-compose pull` |

##  Helpful Shortcuts & Tips

### Container Cleanup
```bash
docker system prune --volumes
```

### Port Mapping & Volumes
* **Ports:** `-p 8080:80` (Access the app via port 8080 on your machine).
* **Volumes:** `-v /my/data:/data` (Syncs a local folder to the container).
