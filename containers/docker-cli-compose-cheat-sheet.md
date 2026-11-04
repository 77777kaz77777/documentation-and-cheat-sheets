## Reference guide for essential Docker and Docker Compose commands

## Docker CLI Essentials

**Run a Container:**
```bash
docker run -d --name [name] [image]
```

**List Running Containers:**
```bash
docker ps
```

**List All Containers:**
```bash
docker ps -a
```

**Stop a Container:**
```bash
docker stop [container_id/name]
```

**Start a Container:**
```bash
docker start [container_id/name]
```

**Remove a Container:**
```bash
docker rm -f [container_id/name]
```

**List Local Images:**
```bash
docker images
```

**Remove an Image:**
```bash
docker rmi [image_id]
```

**View Logs:**
```bash
docker logs -f [container_name]
```

**Enter Container Shell:**
```bash
docker exec -it [container_name] /bin/bash
```

**Prune (Clean) System:**
```bash
docker system prune -a
```

## Docker Compose Commands

**Start Services (Background):**
```bash
docker-compose up -d
```

**Stop & Remove Services:**
```bash
docker-compose down
```

**Stop Services (Keep Data):**
```bash
docker-compose stop
```

**Build/Rebuild Services:**
```bash
docker-compose build
```

**View Composite Logs:**
```bash
docker-compose logs -f
```

**Check Service Status:**
```bash
docker-compose ps
```

**Restart Services:**
```bash
docker-compose restart
```

**Pull New Images:**
```bash
docker-compose pull
```

## Helpful Shortcuts & Tips

### Container Cleanup

```bash
docker system prune --volumes
```

### Port Mapping & Volumes

- **Ports:** `-p 8080:80` (Access the app via port 8080 on your machine).
- **Volumes:** `-v /my/data:/data` (Syncs a local folder to the container).
