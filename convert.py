#!/usr/bin/env python3
"""
convert-all-nested.py
Recursively scans the entire repository for any Markdown file, converts 
all tables into standalone bold labels with fenced code blocks, and fixes 
inline-code bullet lists.
"""

import re
from pathlib import Path

# Files to skip (conceptual tables like OSI layers or repo index)
SKIP_FILES = {
    "README.md",
    "networking-cheatsheet.md",
    "linux-upstream-midstream-downstream-explained.md",
    "ss-command-options-cheat-sheet.md",
    "vim-vi-editor-cheat-sheet.md",
    "alacritty-keybindings-cheatsheet.md",
    "kde-plasma-wayland-shortcuts-cheat-sheet.md",
    "sublime-text-linux-shortcuts.md",
    "raid-cheatsheet.md",
}

def get_code_lang(filepath: Path) -> str:
    name = filepath.name.lower()
    if any(k in name for k in ("powershell", "hyper-v", "winget", "sysinternals", "windows-cmd")):
        return "powershell"
    return "bash"

def clean_cell(text: str) -> str:
    text = text.strip()
    text = text.replace("&#124;", "|").replace("\\|", "|").replace("\\vert{}", "|")
    return text

def strip_backticks_and_bold(text: str) -> str:
    text = text.strip()
    if text.startswith("**") and text.endswith("**"):
        text = text[2:-2].strip()
    if text.startswith("`") and text.endswith("`") and text.count("`") == 2:
        text = text[1:-1].strip()
    return text

def is_separator_or_empty_header(cells: list[str]) -> bool:
    if all(re.match(r"^:?-{2,}:?$", c) or c == "" for c in cells):
        return True
    return False

def convert_table_block(table_lines: list[str], filepath: Path) -> list[str]:
    lang = get_code_lang(filepath)
    rows = []
    for line in table_lines:
        raw_cells = [clean_cell(c) for c in line.strip().strip("|").split("|")]
        rows.append(raw_cells)

    if len(rows) < 2:
        return table_lines

    header_idx = 0
    for idx, r in enumerate(rows):
        if any(c for c in r) and not is_separator_or_empty_header(r):
            header_idx = idx
            break

    headers = [strip_backticks_and_bold(c).lower() for c in rows[header_idx]]

    # Skip conversion for non-command reference tables (like keyboard shortcuts)
    if any(h in ("shortcut", "category", "mode/category", "trait", "layer", "protocol", "concept", "flag") for h in headers):
        return table_lines

    out = []
    for r in rows[header_idx + 1:]:
        if is_separator_or_empty_header(r):
            continue
        if [strip_backticks_and_bold(c).lower() for c in r] == headers:
            continue

        # 2-Column Table (Command/Action | Description)
        if len(headers) == 2 and len(r) >= 2:
            col0, col1 = r[0], r[1]
            if not col0 or not col1:
                continue

            if headers[0] in ("command", "option", "command syntax") and headers[1] in ("description", "action", "effect", "example"):
                cmd = strip_backticks_and_bold(col0)
                desc = strip_backticks_and_bold(col1).rstrip(".")
                out.append(f"**{desc}:**")
                out.append(f"```{lang}")
                out.append(cmd)
                out.append("```")
                out.append("")
            else:
                label = strip_backticks_and_bold(col0).rstrip(":")
                cmd = strip_backticks_and_bold(col1)
                out.append(f"**{label}:**")
                out.append(f"```{lang}")
                out.append(cmd)
                out.append("```")
                out.append("")

        # 3-Column Table (Command | Description | Example)
        elif len(headers) == 3 and len(r) >= 3:
            c0, c1, c2 = r[0], r[1], r[2]
            cmd_name = strip_backticks_and_bold(c0)
            desc = strip_backticks_and_bold(c1).rstrip(".")
            example = strip_backticks_and_bold(c2)
            
            # Handle clipped code strings in cuda monitoring
            if example == 'printf "Result: %04d':
                example = 'printf "Result: %04d\\n" 42'

            out.append(f"**`{cmd_name}` — {desc}:**")
            out.append(f"```{lang}")
            out.append(example)
            out.append("```")
            out.append("")

    return out if out else table_lines

def process_file(filepath: Path) -> bool:
    if filepath.name in SKIP_FILES:
        return False

    original = filepath.read_text(encoding="utf-8")
    lines = original.splitlines()
    out = []
    i = 0
    in_code_block = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            in_code_block = not in_code_block
            out.append(line)
            i += 1
            continue

        if in_code_block:
            out.append(line)
            i += 1
            continue

        # Detect tables anywhere in the file
        if stripped.startswith("|") and stripped.endswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|") and lines[i].strip().endswith("|"):
                table_lines.append(lines[i])
                i += 1
            converted = convert_table_block(table_lines, filepath)
            out.extend(converted)
            continue

        out.append(line)
        i += 1

    result = "\n".join(out)
    result = re.sub(r"\n{3,}", "\n\n", result).strip() + "\n"

    if result != original:
        filepath.write_text(result, encoding="utf-8")
        return True
    return False

if __name__ == "__main__":
    repo_root = Path(".")
    modified_count = 0
    # Recursively find all markdown files in any subfolder
    for md_file in sorted(repo_root.glob("**/*.md")):
        if ".git" in md_file.parts:
            continue
        if process_file(md_file):
            print(f"Modernized: {md_file}")
            modified_count += 1
    print(f"\nSuccessfully converted {modified_count} nested Markdown files!")