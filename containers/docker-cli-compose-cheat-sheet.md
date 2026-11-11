# Docker and Docker Compose Command-Line Reference Guide

Essential modern commands for managing containers, images, volumes, networks, and multi-container applications using the structured Docker CLI syntax and Compose V2 plugin.

---

## Docker Container Management

**Run a Container in the Background:**
```bash
docker container run -d --name [container_name] [image_name]
```

**Run a Container with Port Mapping and Automatic Removal:**
```bash
docker container run -d --rm -p [host_port]:[container_port] --name [container_name] [image_name]
```

**List Running Containers:**
```bash
docker container ls
```

**List All Containers (Including Stopped):**
```bash
docker container ls -a
```

**Stop a Running Container:**
```bash
docker container stop [container_id_or_name]
```

**Start a Stopped Container:**
```bash
docker container start [container_id_or_name]
```

**Restart a Container:**
```bash
docker container restart [container_id_or_name]
```

**Force Remove a Container:**
```bash
docker container rm -f [container_id_or_name]
```

**Follow Container Logs:**
```bash
docker container logs -f [container_id_or_name]
```

**Open an Interactive Shell (Bash):**
```bash
docker container exec -it [container_id_or_name] /bin/bash
```

**Open an Interactive Shell (POSIX / Minimal Images):**
```bash
docker container exec -it [container_id_or_name] /bin/sh
```

---

## Docker Image Management

**List Local Images:**
```bash
docker image ls
```

**Pull an Image from a Registry:**
```bash
docker image pull [image_name]:[tag]
```

**Remove a Local Image:**
```bash
docker image rm [image_id_or_name]
```

**Build an Image from a Dockerfile (BuildKit):**
```bash
docker buildx build -t [image_name]:[tag] .
```

---

## Storage and Volume Management

**Attach a Named Volume (Modern Syntax):**
```bash
docker container run -d --mount type=volume,src=[volume_name],dst=[container_path] [image_name]
```

**Attach a Bind Mount (Modern Syntax):**
```bash
docker container run -d --mount type=bind,src=[host_path],dst=[container_path] [image_name]
```

**Create a Named Volume:**
```bash
docker volume create [volume_name]
```

**List Volumes:**
```bash
docker volume ls
```

**Inspect Volume Details:**
```bash
docker volume inspect [volume_name]
```

**Remove a Volume:**
```bash
docker volume rm [volume_name]
```

---

## Network Management

**Create a User-Defined Bridge Network:**
```bash
docker network create [network_name]
```

**List Docker Networks:**
```bash
docker network ls
```

**Connect a Running Container to a Network:**
```bash
docker network connect [network_name] [container_name]
```

**Disconnect a Container from a Network:**
```bash
docker network disconnect [network_name] [container_name]
```

**Remove a Network:**
```bash
docker network rm [network_name]
```

---

## Docker Compose V2 Operations

**Start Services in the Background:**
```bash
docker compose up -d
```

**Rebuild Images and Start Services:**
```bash
docker compose up -d --build
```

**Start Services in File Watch Mode (Hot Reload):**
```bash
docker compose watch
```

**Check Service Status:**
```bash
docker compose ps
```

**Follow Composite Service Logs:**
```bash
docker compose logs -f
```

**Restart Services:**
```bash
docker compose restart
```

**Stop Services Without Removing Containers:**
```bash
docker compose stop
```

**Stop and Remove Containers and Networks:**
```bash
docker compose down
```

**Stop and Remove Containers, Networks, and Named Volumes:**
```bash
docker compose down --volumes
```

**Pull Latest Service Images:**
```bash
docker compose pull
```

---

## System Maintenance & Cleanup

**Prune Stopped Containers, Unused Networks, and Dangling Images:**
```bash
docker system prune
```

**Prune All Unused Images and System Resources:**
```bash
docker system prune -a
```

**Prune All Unused Resources Including Volumes:**
```bash
docker system prune -a --volumes
```

---

## Sources & Official Documentation

* **Docker CLI Reference:** [https://docs.docker.com/reference/cli/docker/](https://docs.docker.com/reference/cli/docker/)
* **Docker Container CLI Documentation:** [https://docs.docker.com/reference/cli/docker/container/](https://docs.docker.com/reference/cli/docker/container/)
* **Docker Compose CLI Documentation:** [https://docs.docker.com/reference/cli/docker/compose/](https://docs.docker.com/reference/cli/docker/compose/)
* **Docker Volume CLI Documentation:** [https://docs.docker.com/reference/cli/docker/volume/](https://docs.docker.com/reference/cli/docker/volume/)
* **Docker Network CLI Documentation:** [https://docs.docker.com/reference/cli/docker/network/](https://docs.docker.com/reference/cli/docker/network/)
