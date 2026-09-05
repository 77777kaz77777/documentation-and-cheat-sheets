## Cardwire Cheat Sheet

## Core Commands

* **Switch to Integrated Mode (Max Battery):**
~~~bash
cardwire \
  set \
  integrated
~~~

* **Switch to Hybrid Mode (Default):**
~~~bash
cardwire \
  set \
  hybrid
~~~

* **Switch to Dedicated Mode (Max Performance):**
~~~bash
cardwire \
  set \
  dedicated
~~~

* **Check Current Status:**
~~~bash
cardwire \
  status
~~~

## Hardware Verification

* **Check NVIDIA Power State:**
~~~bash
cat \
  /sys/bus/pci/devices/0000:01:00.0/power_state
~~~

*(Expected output is `D3cold` when the GPU is successfully powered off).*
