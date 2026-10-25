## This document is a comprehensive Alacritty keybinding cheatsheet that outlines standard terminal shortcuts

## Custom Keybindings (Your Override Configuration)

| Action                       | Custom Keybinding      | Note                                               |
| :--------------------------- | :--------------------- | :------------------------------------------------- |
| **Copy Selection**           | `Ctrl + Shift + C`     |                                                    |
| **Paste**                    | `Ctrl + Shift + V`     |                                                    |
| **Increase Font Size**       | `Ctrl + =`             |                                                    |
| **Decrease Font Size**       | `Ctrl + -`             |                                                    |
| **Reset Font Size**          | `Ctrl + 0`             |                                                    |
| **Open New Terminal Window** | `Ctrl + Shift + Enter` | _Spawns a new Alacritty instance in current path._ |

## Default Keybindings

### Window & Application Management

| Action                  | Linux & Windows | macOS              |
| :---------------------- | :-------------- | :----------------- |
| **Toggle Fullscreen**   | `F11`           | `Cmd + Ctrl + F`   |
| **Hide Window**         | _N/A_           | `Cmd + H`          |
| **Hide Other Windows**  | _N/A_           | `Cmd + Option + H` |
| **Minimize Window**     | _N/A_           | `Cmd + M`          |
| **Quit Alacritty**      | _N/A_           | `Cmd + Q`          |
| **Clear Screen (Soft)** | `Ctrl + L`      | `Ctrl + L`         |

### Scrolling

| Action                   | Linux & Windows    | macOS            |
| :----------------------- | :----------------- | :--------------- |
| **Scroll Up One Line**   | `Shift + Up`       | `Cmd + Up`       |
| **Scroll Down One Line** | `Shift + Down`     | `Cmd + Down`     |
| **Scroll Up One Page**   | `Shift + PageUp`   | `Cmd + PageUp`   |
| **Scroll Down One Page** | `Shift + PageDown` | `Cmd + PageDown` |
| **Scroll to Top**        | `Shift + Home`     | `Cmd + Home`     |
| **Scroll to Bottom**     | `Shift + End`      | `Cmd + End`      |

### Vi Mode & Search

| Action                                 | Keybinding                                            |
| :------------------------------------- | :---------------------------------------------------- |
| **Toggle Vi Mode**                     | `Ctrl + Shift + Space` (macOS: `Cmd + Shift + Space`) |
| **Move Cursor (Left/Down/Up/Right)**   | `h` / `j` / `k` / `l`                                 |
| **Move Forward/Backward by Word**      | `w` / `b`                                             |
| **Move to End of Word**                | `e`                                                   |
| **Move to Start/End of Line**          | `0` or `^` / `$`                                      |
| **Move to Top / Bottom of Buffer**     | `g` / `G`                                             |
| **Start Selection (Visual Mode)**      | `v`                                                   |
| **Start Line Selection (Visual Line)** | `V`                                                   |
| **Toggle Block Selection**             | `Ctrl + V`                                            |
| **Copy Selection (Yank)**              | `y`                                                   |
| **Search Forward/Backward**            | `/` / `?`                                             |
| **Next / Previous Search Match**       | `n` / `N`                                             |
