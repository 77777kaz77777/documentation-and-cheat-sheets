
# Essential keyboard shortcuts for getting around KDE Plasma on Wayland.

## KWin Window Management

* `Meta + Left/Right/Up/Down` - Snap active window to screen halves or corners (Quarter Tiling).
* `Meta + Page Up / Page Down` - Maximize / Minimize active window.
* `Meta + W` - Trigger the Overview effect (exposes all open windows and virtual desktops).
* `Alt + Tab` - Cycle through windows (Forward).
* `Alt + Shift + Tab` - Cycle through windows (Backward).
* `Alt + F3` - Open the Window Operations menu (Move, Resize, specific application settings).

## KRunner & Quick Launch

* `Alt + Space` (or `Meta`) - Open KRunner / Application Launcher (search apps, execute shell commands, calculate math).
* `Meta + [1-9]` - Launch or switch to the application pinned to the Task Manager at the corresponding position.
* `Ctrl + Esc` - Open the KDE System Activity Monitor (quick task manager for killing frozen apps).

## Virtual Desktops

* `Meta + Ctrl + Left/Right` - Switch to the previous/next virtual desktop.
* `Meta + Ctrl + D` - Show the desktop (Minimize all windows).
* `Meta + Shift + Left/Right` - Move the currently active window to the adjacent virtual desktop.

## Session & Display Management

* `Meta + P` - Open the Display Configuration OSD (useful for quick multi-monitor projection switching).
* `Meta + L` - Lock the session.
* `Ctrl + Alt + Delete` - Open the logout/shutdown prompt.
* `qdbus org.kde.KWin /KWin reconfigure` - Reload KWin configurations without restarting the entire Plasma session.
