# Commands to control fans, lighting, and performance profiles on ASUS ROG laptops (GA503RW) with asusctl.

## 💡 Keyboard Lighting (Aura RGB)

### Color Modes & Effects
> **Note:** Hex codes (`ffffff`, `ff0000`) define the color.

- **Static Color (Solid White):**
  ```bash
  asusctl aura effect static -c ffffff
  ```

- **Breathing Effect (Pulse):**
  ```bash
  asusctl aura effect breathe -c ff0000
  ```

- **Rainbow Cycle:**
  ```bash
  asusctl aura effect rainbow
  ```

- **Turn Keyboard Lights Completely Off:**
  ```bash
  asusctl aura effect off
  ```

### Keyboard Brightness
- **Set Brightness Level (Values: `0`, `1`, `2`, `3`):**
  ```bash
  asusctl leds -b 2
  ```

### Aura Power Behavior
- **Enable lights during boot, awake, and sleep:**
  ```bash
  asusctl aura power --boot true --awake true --sleep true
  ```

---

## 🚀 Performance Profiles & Fan Curves

### Power Profiles
Toggle your system's power delivery and fan behavior (corresponds to the physical ROG hotkey).

- **View current profile:**
  ```bash
  asusctl profile -p
  ```

- **Switch to Quiet mode:**
  ```bash
  asusctl profile -m Quiet
  ```

- **Switch to Balanced (Standard) mode:**
  ```bash
  asusctl profile -m Balanced
  ```

- **Switch to Performance mode:**
  ```bash
  asusctl profile -m Performance
  ```

- **Cycle to the next profile:**
  ```bash
  asusctl profile -n
  ```

### Custom Fan Curves
- **View active fan curves:**
  ```bash
  asusctl fan-curve -p
  ```

---

## 🔋 Battery Health & System

### Battery Charge Limit
Prolong battery lifespan when plugged in consistently by capping the max charge percentage.

- **Limit charge to 80%:**
  ```bash
  asusctl battery -c 80
  ```

- **Reset to 100% full charge:**
  ```bash
  asusctl battery -c 100
  ```

### Hardware Status
- **Show system hardware info and tool version:**
  ```bash
  asusctl info
  ```

---

## 🛠️ Troubleshooting Commands

If the tool stops responding or configurations don't apply, restart the background daemon:

```bash
sudo systemctl restart asusd
```
