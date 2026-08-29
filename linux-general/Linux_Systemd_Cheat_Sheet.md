# Everyday commands for handling services and logs with Systemd and journalctl.

Systemd is the system and service manager responsible for controlling system units, background services, boots, and logs.

| Action | Command |
| :--- | :--- |
| **Check Service Status** | `sudo systemctl status [service_name]` |
| **Start a Service** | `sudo systemctl start [service_name]` |
| **Stop a Service** | `sudo systemctl stop [service_name]` |
| **Restart a Service** | `sudo systemctl restart [service_name]` |
| **Enable Service on Boot** | `sudo systemctl enable --now [service_name]` |
| **Disable Service on Boot** | `sudo systemctl disable [service_name]` |
| **View Real-Time Service Logs** | `sudo journalctl -u [service_name] -f` |
| **View System Logs (Since Boot)** | `sudo journalctl -b` |
| **Reload Systemd Manager Configuration** | `sudo systemctl daemon-reload` |
| **Check Failed Units** | `systemctl --failed` |
