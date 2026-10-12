# How to tweak and customize system info outputs using Fastfetch

Customizing **Fastfetch** (the speedy, highly configurable successor to Neofetch) is done using a structured JSONC (JSON with Comments) configuration system. This allows you to easily format modules, change colors, insert custom text, and swap out logos.

---

## 1. Generate Your Configuration File

By default, Fastfetch pulls from system presets. To build your own, generate a local configuration file:

```bash
fastfetch --gen-config
```

This creates a default configuration file located at `~/.config/fastfetch/config.jsonc` (Linux/macOS). Open it with any text editor:

```bash
nano ~/.config/fastfetch/config.jsonc
```

> 💡 **Tip:** If you use an editor like VS Code or Helix, leave the `$schema` line at the top intact—it provides real-time autocomplete suggestions and validation while editing.

---

## 2. Understanding the Config Structure

The JSONC file is broken down into three major pillars:

```jsonc
{
  "$schema": "https://github.com/fastfetch-cli/fastfetch/raw/dev/doc/json_schema.json",
  "logo": {
    // 1. Logo aesthetics (ASCII art, custom images, padding)
  },
  "display": {
    // 2. Global styling (colors, key layouts, dividers)
  },
  "modules": [
    // 3. System information pieces to show or hide
  ]
}
```

---

## 3. Customizing the Logo

The `"logo"` block handles the visual art displayed on the left side of your terminal fetch.

### Switch to a Built-in OS Logo

```jsonc
"logo": {
    "source": "arch", // Try "ubuntu", "fedora", "apple", "windows", etc.
    "padding": {
        "right": 2
    }
}
```

### Use a Custom Image (Kitty/Sixel Protocol)

If your terminal emulator supports images (Kitty, WezTerm, Alacritty with graphics support, iTerm2):

```jsonc
"logo": {
    "type": "auto",
    "source": "~/Pictures/my_cool_avatar.png",
    "width": 30,
    "height": 15
}
```

### Use Custom ASCII Art

Save text art in a plain file (e.g., `~/.config/fastfetch/my_ascii.txt`) and reference it:

```jsonc
"logo": {
    "source": "~/.config/fastfetch/my_ascii.txt"
}
```

---

## 4. Customizing Colors and Global Layouts

The `"display"` block alters how text elements behave next to the logo:

```jsonc
"display": {
    "separator": " ➜  ", // Changes the classic colon (:) to a custom symbol
    "color": {
        "keys": "cyan",   // Colors the module label (e.g., OS, Kernel)
        "title": "magenta" // Colors username@hostname
    },
    "key": {
        "width": 12 // Aligns all keys vertically
    }
}
```

**Available basic colors:** `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`, and bright variants like `bright_blue`.

---

## 5. Adding, Removing, and Tweaking Modules

The `"modules"` array controls what information prints.

### Basic Module Array (Simple Strings)

```jsonc
"modules": [
    "title",
    "separator",
    "os",
    "host",
    "kernel",
    "uptime",
    "packages",
    "shell",
    "display",
    "break", // Inserts an empty line
    "colors" // Displays the color blocks at the bottom
]
```

### Advanced Modules (Objects with Parameters)

Replace simple strings with objects to customize layout, labels, colors, and format strings:

```jsonc
"modules": [
    "title",
    "separator",
    {
        "type": "os",
        "key": "System",
        "keyColor": "yellow"
    },
    {
        "type": "cpu",
        "format": "{name} ({cores-physical}C/{cores-logical}T) @ {freq-max}" 
    },
    {
        "type": "memory",
        "key": "RAM Usage",
        "percent": {
            "type": 3, // Outputs both a bar graph and a textual percentage
            "green": 40,
            "yellow": 80
        }
    }
]
```

> 💡 **Tip:** View all placeholders for a module using `fastfetch -h cpu-format` or `fastfetch -h memory-format`.

---

## 6. Going Wild with Nerd Fonts (Icons)

If a Nerd Font is installed in your terminal, copy-paste icons directly into `"key"` properties:

```jsonc
{
    "type": "os",
    "key": " 󰍹 OS"
},
{
    "type": "kernel",
    "key": " 󰅐 Kernel"
},
{
    "type": "uptime",
    "key": " 󰔛 Uptime"
}
```

---

## 7. Testing and Launching Automatically

Run `fastfetch` in your terminal to view changes instantly. Fastfetch will print detailed error lines if your JSON syntax is invalid.

### Launch on Terminal Startup

- **Bash / Zsh:** Add `fastfetch` to the bottom of `~/.bashrc` or `~/.zshrc`.
- **Fish:** Add `fastfetch` inside the interactive block in `~/.config/fish/config.fish`.
