#!/usr/bin/env python3
import os
import re
import shutil
from pathlib import Path

# 1. Map files to their new subdirectories inside linux-general/
linux_general_moves = {
    "package-management": [
        "apt_command_reference.md", "apk_command_reference.md", "brew_command_reference.md",
        "dnf_command_reference.md", "pacman_command_reference.md", "zypper_command_reference.md",
        "flatpak_command_reference.md", "appimage_installation_guide.md"
    ],
    "storage-and-filesystems": [
        "btrfs_cheat_sheet.md", "ZFS_Administration_Cheat_Sheet.md", "raid_cheatsheet.md",
        "nvme_cli_cheat_sheet.md", "nvme_troubleshooting_guide.md", "smartctl_cheat_sheet.md",
        "storage_management_reference.md"
    ],
    "desktop-environments": [
        "KDE_Plasma_Wayland_Shortcuts_Cheat_Sheet.md", "alacritty-font-rendering-fix.md",
        "alacritty_keybindings_cheatsheet.md", "Fastfetch_Configuration_Guide.md",
        "Sublime_Text_Linux_Shortcuts.md"
    ],
    "hardware-and-firmware": [
        "fwupdmgr_Firmware_Update_Cheat_Sheet.md", "disable-amdgpu-grub.md",
        "wifi-hardware-replacement-guide.md"
    ]
}

def to_kebab_case(filename):
    name, ext = os.path.splitext(filename)
    # Replace underscores and spaces with dashes, convert to lowercase
    kebab_name = re.sub(r'[_ ]+', '-', name).lower()
    return f"{kebab_name}{ext}"

def inject_frontmatter(filepath, title):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Only inject if frontmatter doesn't already exist
    if not content.startswith('---'):
        frontmatter = f"---\ntitle: \"{title}\"\n---\n\n"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(frontmatter + content)

def main():
    repo_root = Path(".")
    linux_gen_dir = repo_root / "linux-general"

    # Step 1: Reorganize linux-general
    if linux_gen_dir.exists():
        print("Reorganizing linux-general directory...")
        for new_folder, files in linux_general_moves.items():
            target_dir = linux_gen_dir / new_folder
            target_dir.mkdir(parents=True, exist_ok=True)

            for file in files:
                source_file = linux_gen_dir / file
                if source_file.exists():
                    shutil.move(str(source_file), str(target_dir / file))
                    print(f"  Moved: {file} -> {new_folder}/")

    # Step 2: Rename all files to kebab-case and inject frontmatter
    print("\nApplying kebab-case and YAML frontmatter...")
    for root, _, files in os.walk(repo_root):
        # Skip hidden directories like .git or .github
        if '.git' in root or '.github' in root:
            continue

        for file in files:
            if file.endswith('.md'):
                old_path = Path(root) / file
                new_name = to_kebab_case(file)
                new_path = Path(root) / new_name

                # Rename file
                if old_path != new_path:
                    old_path.rename(new_path)
                    print(f"  Renamed: {file} -> {new_name}")
                
                # Generate a clean title for the frontmatter
                clean_title = new_name.replace('-', ' ').replace('.md', '').title()
                
                # Inject YAML frontmatter
                inject_frontmatter(new_path, clean_title)

    print("\nAutomation complete. Run 'git status' to review the modifications.")

if __name__ == "__main__":
    main()
