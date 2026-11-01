#!/usr/bin/env python3
# generate_nav.py
from pathlib import Path
import re

ROOT_DIR = Path(".")
MKDOCS_FILE = ROOT_DIR / "mkdocs.yml"

EXCLUDE_DIRS = {
    ".git",
    ".github",
    ".obsidian",
    "site",
    "stylesheets",
    "__pycache__",
    ".venv",
    "venv",
}

ACRONYMS = {
    "cli": "CLI",
    "lxc": "LXC",
    "ssh": "SSH",
    "dns": "DNS",
    "kde": "KDE",
    "gpu": "GPU",
    "amdgpu": "AMDGPU",
    "nvidia": "NVIDIA",
    "grub": "GRUB",
    "ssd": "SSD",
    "nvme": "NVMe",
    "btrfs": "BTRFS",
    "rog": "ROG",
    "asus": "ASUS",
    "vm": "VM",
    "vms": "VMs",
    "kvm": "KVM",
    "qemu": "QEMU",
    "proxmox": "Proxmox",
    "macos": "macOS",
    "ios": "iOS",
    "ip": "IP",
    "ufw": "UFW",
    "vpn": "VPN",
    "usb": "USB",
    "cpu": "CPU",
    "ram": "RAM",
    "bios": "BIOS",
    "uefi": "UEFI",
    "lvm": "LVM",
    "zfs": "ZFS",
    "smb": "SMB",
    "nfs": "NFS",
    "api": "API",
    "gui": "GUI",
    "tui": "TUI",
    "os": "OS",
}

LOWERCASE_WORDS = {"and", "or", "for", "in", "on", "to", "with", "of", "via", "vs"}


def format_label(raw_name: str) -> str:
    """Convert a filename or directory slug into a clean human-readable title."""
    stem = re.sub(r"\.md$", "", raw_name, flags=re.IGNORECASE)
    if stem.upper() == "README":
        return "Overview"

    # Separate trailing version numbers attached to words like fedora44 -> fedora 44
    stem = re.sub(r"([a-zA-Z])(\d+)", r"\1 \2", stem)
    words = re.split(r"[-_\s]+", stem.strip())

    formatted = []
    for i, word in enumerate(words):
        if not word:
            continue
        low = word.lower()
        if low in ACRONYMS:
            formatted.append(ACRONYMS[low])
        elif i > 0 and low in LOWERCASE_WORDS:
            formatted.append(low)
        else:
            formatted.append(word.capitalize())

    title = " ".join(formatted)
    title = title.replace("Cheatsheet", "Cheat Sheet")
    return title


def build_nav_lines(directory: Path, indent: int = 2) -> list[str]:
    """Recursively scan directories and build YAML nav lines."""
    lines: list[str] = []
    prefix = " " * indent

    # 1. Markdown files in current directory (sorted cleanly)
    md_files = sorted(
        [
            f
            for f in directory.iterdir()
            if f.is_file() and f.suffix.lower() == ".md"
        ],
        key=lambda p: (0 if p.name.upper() == "README.MD" else 1, p.name.lower()),
    )

    for md_file in md_files:
        if directory == ROOT_DIR and md_file.name.upper() == "README.MD":
            continue
        rel_path = md_file.relative_to(ROOT_DIR).as_posix()
        label = format_label(md_file.name)
        lines.append(f'{prefix}- "{label}": {rel_path}')

    # 2. Subdirectories in current directory (sorted cleanly)
    subdirs = sorted(
        [
            d
            for d in directory.iterdir()
            if d.is_dir()
            and d.name not in EXCLUDE_DIRS
            and not d.name.startswith(".")
        ],
        key=lambda p: p.name.lower(),
    )

    for subdir in subdirs:
        child_lines = build_nav_lines(subdir, indent + 4)
        if child_lines:
            section_label = format_label(subdir.name)
            lines.append(f'{prefix}- "{section_label}":')
            lines.extend(child_lines)

    return lines


def main() -> None:
    if not MKDOCS_FILE.exists():
        raise FileNotFoundError("mkdocs.yml not found in current directory.")

    content = MKDOCS_FILE.read_text(encoding="utf-8")

    # Strip any previous nav: block at the end of mkdocs.yml
    content_without_nav = re.sub(
        r"\n*nav:\s*\n(?:[ \t]*-.*\n?)*", "\n", content, flags=re.MULTILINE
    ).rstrip()

    nav_lines = ["nav:", '  - "Home": README.md']
    nav_lines.extend(build_nav_lines(ROOT_DIR, indent=2))

    updated_content = content_without_nav + "\n\n" + "\n".join(nav_lines) + "\n"
    MKDOCS_FILE.write_text(updated_content, encoding="utf-8")
    print("Successfully updated nav: section in mkdocs.yml")


if __name__ == "__main__":
    main()
