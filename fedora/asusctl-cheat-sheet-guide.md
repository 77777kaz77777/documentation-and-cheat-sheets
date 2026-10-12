# Commands to control fans, lighting, and performance profiles on ASUS ROG laptops (GA503RW) with asusctl

# asusctl v6.5.0 Reference Guide

## 💡 Keyboard Lighting (Aura RGB)

### Color Modes & Effects

> **Note:** Hex codes (`ffffff`, `ff0000`) define the color.

* **Static Color (Solid White):**

~~~bash
asusctl aura static \
  -c ffffff
~~~

* **Breathing Effect (Pulse):**

~~~bash
asusctl aura breathe \
  -c ff0000
~~~

* **Rainbow Cycle:**

~~~bash
asusctl aura rainbow-cycle
~~~

* **Turn Keyboard Lights Off:**

~~~bash
asusctl aura static \
  -c 000000
~~~

### Keyboard Brightness

* **Set Brightness Level (Values: `Off`, `Low`, `Med`, `High`):**

~~~bash
asusctl \
  -k Med
~~~

* **Cycle Next Lighting Mode:**

~~~bash
asusctl aura \
  --next-mode
~~~

### Aura Power Behavior

* **Enable lights during boot, awake, and sleep:**

~~~bash
asusctl aura power \
  --boot true \
  --awake true \
  --sleep true
~~~

---

## 🚀 Performance Profiles & Fan Curves

### Power Profiles

Toggle system power delivery and fan behavior (corresponds to physical ROG hotkey).

* **View active profile:**

~~~bash
asusctl profile \
  -p
~~~

* **Switch to Quiet mode:**

~~~bash
asusctl profile set \
  Quiet
~~~

* **Switch to Balanced (Standard) mode:**

~~~bash
asusctl profile set \
  Balanced
~~~

* **Switch to Performance mode:**

~~~bash
asusctl profile set \
  Performance
~~~

* **Cycle to next profile:**

~~~bash
asusctl profile next
~~~

### Custom Fan Curves

* **View active fan curves:**

~~~bash
asusctl fan-curve \
  -p
~~~

---

## 🔋 Battery Health & System

### Battery Charge Limit

Prolong battery lifespan when plugged in consistently by capping max charge percentage.

* **Limit charge to 80%:**

~~~bash
asusctl battery limit \
  80
~~~

* **Reset to 100% full charge:**

~~~bash
asusctl battery limit \
  100
~~~

* **View battery limit and status:**

~~~bash
asusctl battery info
~~~

### Hardware Status

* **Show system hardware info and tool version:**

~~~bash
asusctl info
~~~

* **Show supported hardware features:**

~~~bash
asusctl info \
  --show-supported
~~~

---

## 🛠️ Troubleshooting Commands

If the tool stops responding or configurations do not apply, restart the background daemon:

~~~bash
sudo systemctl restart \
  asusd
~~~

---
