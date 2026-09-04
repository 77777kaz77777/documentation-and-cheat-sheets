
## Setting up the Alacritty terminal on Fedora, complete with custom fonts and themes

## Step 1: Install Alacritty

Install the terminal emulator directly from the standard Fedora repositories.

```bash
sudo dnf install alacritty
```

## Step 2: Install JetBrains Mono Nerd Font

This configuration requires the Nerd Font variant for correct glyph and icon rendering, which must be installed locally. Execute the following sequential commands to download, extract, and apply the font cache:

```bash
curl -LO https://github.com/ryanoasis/nerd-fonts/releases/latest/download/JetBrainsMono.zip
mkdir -p ~/.local/share/fonts/JetBrainsMono
unzip JetBrainsMono.zip -d ~/.local/share/fonts/JetBrainsMono
fc-cache -fv
rm JetBrainsMono.zip
```

## Step 3: Apply the Alacritty Configuration

Alacritty looks for its configuration file in your home directory's `.config` folder.

### 3.1 Create the Directory

```bash
mkdir -p ~/.config/alacritty
```

### 3.2 Create the Configuration File

```bash
nano ~/.config/alacritty/alacritty.toml
```

### 3.3 Add Configuration Parameters

Paste the following complete configuration into the file and save:

```toml
# Alacritty terminal configuration
# =====================================================================
# ALACRITTY - MATTE BLACK HARDWARE INTERFACE (FULL PRO CONFIGURATION)
# =====================================================================

# --- GENERAL SETTINGS ---
# Tells Alacritty to reload changes immediately when you save this file
[general]
live_config_reload = true

[env]
TERM = "xterm-256color"

# --- WINDOW CONFIGURATION ---
[window]
padding = { x = 12, y = 12 }
decorations = "Full"        # Enables Minimize, Maximize, and Close buttons
opacity = 1.0               # Matte black look (change to 0.9 if you want slight transparency)
blur = true                 # Enables background blur if your desktop compositor supports it
startup_mode = "Windowed"   # Can be "Windowed", "Maximized", or "Fullscreen"
dynamic_title = true        # Allows running apps (like bash/nvim) to update the window title

# --- FONT CONFIGURATION ---
[font]
size = 17.0

[font.normal]
family = "JetBrainsMono Nerd Font"
style = "Regular"

[font.bold]
family = "JetBrainsMono Nerd Font"
style = "Bold"

[font.italic]
family = "JetBrainsMono Nerd Font"
style = "Italic"

[font.bold_italic]
family = "JetBrainsMono Nerd Font"
style = "Bold Italic"

# --- SCROLLBACK BUFFER ---
[scrolling]
history = 10000             # Remember 10,000 lines of terminal text scrollback
multiplier = 3              # Number of lines scrolled per mouse wheel tick

# --- CURSOR ---
[cursor]
style = { shape = "Block", blinking = "On" }
blink_interval = 750        # Blink speed in milliseconds
unfocused_hollow = true     # Turns cursor into an empty box when the window loses focus

# --- SELECTION & CLIPBOARD ---
[selection]
save_to_clipboard = true    # Automatically copy highlighted text to your clipboard

# --- MATTE BLACK COLOR SCHEME ---
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

# --- KEYBOARD BINDINGS ---
# Handy layout mapping for basic quality of life terminal actions
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
action = "SpawnNewInstance"  # Opens a fresh terminal window in your current path
```

## Step 4: Verification Steps

* **Launch Alacritty**: Open the application from your KDE Plasma launcher or run `alacritty` in your existing terminal.
* **Test the Font & Glyphs**: The text should render in JetBrains Mono. To confirm the Nerd Font icons are working, run:

  ```bash
  echo -e "\ue712"
  ```

  If successful, it will output a Linux penguin icon (``).
* **Confirm Window Styling**: Ensure the window has a uniform 12px padding around the edges, standard minimize/maximize window decorations, and a matte black (`#121212`) background.
* **Test Custom Keybindings**:
  * Highlight any text, press **Ctrl + C** to copy, and **Ctrl + V** to paste.
  * Press **Ctrl + =** to increase font size, **Ctrl + -** to decrease it, and **Ctrl + 0** to reset it to 12.0.
  * Press **Ctrl + Shift + Enter** to spawn a fresh Alacritty window pointing to your current working directory.
* **Test Live Reload**: Open `~/.config/alacritty/alacritty.toml` in your text editor. Temporarily change `opacity = 1.0` to `0.5`, and save the file. The terminal window should immediately become transparent without requiring a restart. Revert back to `1.0` and save again.
