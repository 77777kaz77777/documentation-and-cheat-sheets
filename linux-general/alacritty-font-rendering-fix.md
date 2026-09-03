# Alacritty Rendering Troubleshooting Guide (Fedora KDE)

## Problem

Visual artifacting, text clipping, and residual text remaining on the window margins in the Alacritty terminal.

## Root Cause

1. **Missing Font:** The configured `JetBrains Mono Nerd Font` is missing from the host system, causing character metric mismatches during font fallback.
2. **Wayland Compositor Redraw:** The Wayland compositor under KDE Plasma fails to refresh padded terminal margins correctly upon window resize.

## Solution

### Step 1: Install Required Nerd Fonts

Download and install the JetBrains Mono Nerd Font to the local user directory. Execute the following commands sequentially:

```bash
curl -LO [https://github.com/ryanoasis/nerd-fonts/releases/latest/download/JetBrainsMono.zip](https://github.com/ryanoasis/nerd-fonts/releases/latest/download/JetBrainsMono.zip)
mkdir -p ~/.local/share/fonts
unzip JetBrainsMono.zip -d ~/.local/share/fonts/JetBrainsMono
fc-cache -fv
rm JetBrainsMono.zip
```

Verify the font is registered with the system:

```bash
fc-list | grep -i "jetbrains"
```

### Step 2: Apply Full Configuration Fix

Update `~/.config/alacritty/alacritty.toml` to include proper font spacing in the family name and enable `dynamic_padding` to enforce Wayland margin redraws. Replace your existing configuration with this fully updated file:

```toml
[general]
live_config_reload = true

[env]
TERM = "xterm-256color"

[window]
padding = { x = 12, y = 12 }
dynamic_padding = true
decorations = "Full"
opacity = 1.0
blur = true
startup_mode = "Windowed"
dynamic_title = true

[font]
size = 17.0

[font.normal]
family = "JetBrains Mono Nerd Font"
style = "Regular"

[font.bold]
family = "JetBrains Mono Nerd Font"
style = "Bold"

[font.italic]
family = "JetBrains Mono Nerd Font"
style = "Italic"

[font.bold_italic]
family = "JetBrains Mono Nerd Font"
style = "Bold Italic"

[scrolling]
history = 10000
multiplier = 3

[cursor]
style = { shape = "Block", blinking = "On" }
blink_interval = 750
unfocused_hollow = true

[selection]
save_to_clipboard = true

[colors.primary]
background = "#121212"
foreground = "#e0e0e0"

[colors.selection]
text = "CellForeground"
background = "#282828"

[colors.normal]
black   = "#161616"
red     = "#c30010"
green   = "#90a959"
yellow  = "#f4bf75"
blue    = "#6a9fb5"
magenta = "#aa759f"
cyan    = "#75b5aa"
white   = "#e0e0e0"

[colors.bright]
black   = "#404040"
red     = "#e55555"
green   = "#aac474"
yellow  = "#feca88"
blue    = "#82b8c8"
magenta = "#c28cb8"
cyan    = "#93d3c3"
white   = "#ffffff"

[[keyboard.bindings]]
key = "V"
mods = "Control"
action = "Paste"

[[keyboard.bindings]]
key = "C"
mods = "Control"
action = "Copy"

[[keyboard.bindings]]
key = "0"
mods = "Control"
action = "ResetFontSize"

[[keyboard.bindings]]
key = "="
mods = "Control"
action = "IncreaseFontSize"

[[keyboard.bindings]]
key = "-"
mods = "Control"
action = "DecreaseFontSize"

[[keyboard.bindings]]
key = "Enter"
mods = "Control|Shift"
action = "SpawnNewInstance"
```

### Step 3: Restart Terminal

Close all active instances of Alacritty and launch a new instance for the font cache and configuration changes to take full effect.
