## How to install and set up the Podman Desktop GUI

Podman Desktop is a graphical user interface (GUI) that allows developers to easily manage containers, images, and pods without needing to memorize command-line operations.

## 1. How to Install Podman Desktop with Flatpak

If you are using Linux, Flatpak is the officially recommended way to install Podman Desktop. Open your terminal and run the following commands:

**Step 1: Add the Flathub Repository**
*(If you haven't already enabled Flathub on your system)*

```bash
flatpak remote-add --if-not-exists flathub [https://flathub.org/repo/flathub.flatpakrepo](https://flathub.org/repo/flathub.flatpakrepo)
```

**Step 2: Install Podman Desktop**

```bash
flatpak install flathub io.podman_desktop.PodmanDesktop
```

**Step 3: Launch the Application**
You can now launch it from your desktop's application menu, or via the terminal using:

```bash
flatpak run io.podman_desktop.PodmanDesktop
```

> **Note:** Podman Desktop is just the UI. You will also need the actual Podman engine installed on your system. If you don't have it, Podman Desktop will guide you through installing it on its first launch.

---

## 2. How to Use Podman Desktop

Once installed and running, Podman Desktop provides an intuitive interface for container management. Here is a breakdown of its core features:

### Dashboard

* The main screen shows the health of your container engine (e.g., Podman, Docker, etc.).
* It provides a quick summary of your running containers, pods, and system resource usage (CPU/Memory).

### Managing Images

* **Pulling Images:** Go to the **Images** tab. Click "Pull", enter a registry name (e.g., `docker.io/library/nginx` or `quay.io/fedora/fedora`), and download it.
* **Building Images:** You can click "Build" to select a local `Dockerfile` and build a container image directly from the GUI.

### Managing Containers

* **Starting a Container:** In the **Images** tab, click the "Play" (Run) button next to any downloaded image to instantly spin up a container. A prompt will let you configure ports, volumes, and environment variables before starting it.
* **Monitoring:** Go to the **Containers** tab to see a list of everything currently running or stopped.
* **Interacting:** Click on any active container to:
  * View live **Logs**.
  * Open a **Terminal** (TTY) directly inside the container.
  * Inspect the container's underlying JSON configuration.

### Working with Pods

* Podman uniquely supports **Pods** (a Kubernetes concept where multiple containers share the same network namespace and resources).
* In the **Pods** tab, you can group related containers together and manage them as a single entity. This makes it easy to test multi-container setups and transition your workloads to Kubernetes later.

### Extensions

* Podman Desktop is highly extensible. Go to **Settings > Extensions** to add features like Docker Compose support, local Kubernetes integration (Kind/Minikube), or developer tools.
