## ASUS ROG Zephyrus G15 Setup Guide for Fedora 44 KDE

This document outlines the complete procedure for configuring and optimizing ASUS ROG hardware running Fedora 44 KDE, specifically targeting the AMD Ryzen 9 6900HS and NVIDIA RTX 3070 Ti architecture.

## Overview

This configuration replaces legacy repositories with the official Terra repository, provisions `asusctl` for system controls, and deploys `cardwire` for modern hybrid graphics management.

---

## Step 1: Clean Up Legacy Repositories and Packages

Remove deprecated COPR repositories and old software versions to prevent dependency errors.

~~~bash
sudo dnf copr remove \
  -y \
  lukenukem/asus-linux

sudo dnf remove \
  -y \
  asusctl \
  supergfxctl \
  asusctl-rog-gui
~~~

## Step 2: Install the Terra Repository

Add the official Terra repository maintained by Fyra Labs to source modern ASUS packages.

~~~bash
sudo dnf install \
  -y \
  --nogpgcheck \
  --repofrompath 'terra,https://repos.fyralabs.com/terra$releasever' \
  terra-release

sudo dnf update \
  -y \
  --refresh
~~~

## Step 3: Install ASUS Utilities and Cardwire

Install the core management tools while allowing DNF to automatically resolve conflicts with default package managers like `switcheroo-control`.

~~~bash
sudo dnf install \
  -y \
  --allowerasing \
  asusctl \
  cardwire \
  asusctl-rog-gui
~~~

## Step 4: Enable System Daemons

Enable the required background services to manage hardware states.

~~~bash
sudo systemctl enable \
  --now \
  cardwired.service
~~~

---

## Managing GPU Modes

* **Integrated Mode (Max Battery):**

    ~~~bash
    cardwire \
      set \
      integrated
    ~~~

* **Hybrid Mode (Default):**

    ~~~bash
    cardwire \
      set \
      hybrid
    ~~~

* **Dedicated Mode (Max Performance):**

    ~~~bash
    cardwire \
      set \
      dedicated
    ~~~

* **Check Status:**

    ~~~bash
    cardwire \
      status
    ~~~

## Verification

To verify that the NVIDIA GPU has successfully powered down to save battery in integrated mode, inspect the power state on the PCI bus:

~~~bash
cat \
  /sys/bus/pci/devices/0000:01:00.0/power_state
~~~

*(A return value of `D3cold` indicates the GPU is successfully powered off).*
