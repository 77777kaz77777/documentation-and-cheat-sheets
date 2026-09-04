## This document is a comprehensive Alacritty keybinding cheatsheet that outlines standard terminal shortcuts, my custom overrides—specifically the switch from the default Ctrl + Shift + C and V to Ctrl + C and V for copying and pasting—and a detailed breakdown of my terminal's configuration settings

## Custom Keybindings (Your Override Configuration)

| Action | Custom Keybinding | Note |
| :--- | :--- | :--- |
| **Copy Selection** | `Ctrl + C` | *Switches Copy from the default `Ctrl + Shift + C`. Warning: This overrides the default UNIX SIGINT (cancel program) command.* |
| **Paste** | `Ctrl + V` | *Switches Paste from the default `Ctrl + Shift + V` to match typical desktop applications.* |
| **Increase Font Size** | `Ctrl + =` | |
| **Decrease Font Size** | `Ctrl + -` | |
| **Reset Font Size** | `Ctrl + 0` | |
| **Open New Terminal Window** | `Ctrl + Shift + Enter` | *Spawns a new Alacritty instance in current path.* |

## Default Keybindings

### Window & Application Management

| Action | Linux & Windows | macOS |
| :--- | :--- | :--- |
| **Toggle Fullscreen** | `F11` | `Cmd + Ctrl + F` |
| **Hide Window** | *N/A* | `Cmd + H` |
| **Hide Other Windows** | *N/A* | `Cmd + Option + H` |
| **Minimize Window** | *N/A* | `Cmd + M` |
| **Quit Alacritty** | *N/A* | `Cmd + Q` |
| **Clear Screen (Soft)** | `Ctrl + L` | `Ctrl + L` |

### Scrolling

| Action | Linux & Windows | macOS |
| :--- | :--- | :--- |
| **Scroll Up One Line** | `Shift + Up` | `Cmd + Up` |
| **Scroll Down One Line** | `Shift + Down` | `Cmd + Down` |
| **Scroll Up One Page** | `Shift + PageUp` | `Cmd + PageUp` |
| **Scroll Down One Page** | `Shift + PageDown` | `Cmd + PageDown` |
| **Scroll to Top** | `Shift + Home` | `Cmd + Home` |
| **Scroll to Bottom** | `Shift + End` | `Cmd + End` |

### Vi Mode & Search

| Action | Keybinding |
| :--- | :--- |
| **Toggle Vi Mode** | `Ctrl + Shift + Space` (macOS: `Cmd + Shift + Space`) |
| **Move Cursor (Left/Down/Up/Right)** | `h` / `j` / `k` / `l` |
| **Move Forward/Backward by Word** | `w` / `b` |
| **Move to End of Word** | `e` |
| **Move to Start/End of Line** | `0` or `^` / `$` |
| **Move to Top / Bottom of Buffer** | `g` / `G` |
| **Start Selection (Visual Mode)** | `v` |
| **Start Line Selection (Visual Line)** | `V` |
| **Toggle Block Selection** | `Ctrl + V` |
| **Copy Selection (Yank)** | `y` |
| **Search Forward/Backward** | `/` / `?` |
| **Next / Previous Search Match** | `n` / `N` |
