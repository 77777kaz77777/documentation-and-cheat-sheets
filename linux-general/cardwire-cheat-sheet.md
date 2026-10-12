## Cardwire Cheat Sheet

## Core Commands

* **Switch to Integrated Mode (Max Battery):**

~~~bash
cardwire \
  set \
  integrated
~~~

* **Switch to Smart Mode (Dynamic/Optimal Performance):**

~~~bash
cardwire \
  set \
  smart
~~~

* **Switch to Hybrid Mode (Standard Offloading):**

~~~bash
cardwire \
  set \
  hybrid
~~~

* **Switch to Manual Mode (Manual Control):**

~~~bash
cardwire \
  set \
  manual
~~~

* **Check Current Status:**

~~~bash
cardwire \
  get
~~~

## Hardware Verification

* **Check NVIDIA Power State:**

~~~bash
cat \
  /sys/bus/pci/devices/0000:01:00.0/power_state
~~~

*(Expected output is `D3cold` when the GPU is successfully powered off).*
