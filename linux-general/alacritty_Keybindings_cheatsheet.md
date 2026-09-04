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

## Detailed Breakdown

* **General Settings:** The `live_config_reload` instructs Alacritty to attach a filesystem watcher to the TOML file. When it detects a write event, it instantly applies the changes to the running instance. Setting `TERM = "xterm-256color"` ensures rich colors in terminal output.
* **Window Management:** The padding values push text 12 pixels away from the window borders. `dynamic_title = true` allows running processes to update the OS-level window title.
* **Typography:** The config binds specifically to "JetBrainsMono Nerd Font" at exactly 17.0pt with explicit style declarations to prevent artifacting from OS-level font rendering.
* **Scrolling & Buffer:** Holding 10,000 lines of standard output in memory (`history = 10000`) and mapping mouse scroll multiplier to 3 lines per physical click provides robust navigation.
* **Cursor Behavior:** `unfocused_hollow = true` acts as a clear visual indicator that input is no longer routed to that specific window.
* **Clipboard:** Highlighting text instantly copies it to the system clipboard via `save_to_clipboard = true`.
* **Keybindings:** Binding standard desktop shortcuts `Ctrl + C` and `Ctrl + V` standardizes interactions. **By doing this, you are explicitly switching the default `Ctrl + Shift + C` (Copy) and `Ctrl + Shift + V` (Paste) to `Ctrl + C` and `Ctrl + V`.** This intercepts the traditional UNIX interrupt signal (SIGINT) normally bound to `Ctrl + C`.
