#!/usr/bin/env python3
"""
modernize-repo.py
Converts CLI command tables and inline-code bullets into standalone bold labels
with fenced copy-pasteable code blocks (```bash / ```powershell) across
documentation-and-cheat-sheets, while preserving conceptual tables and README.md.
"""

import re
from pathlib import Path

# Files to skip completely (conceptual tables, keybinding matrices, or index)
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

# Fix [https://url](https://url) inside code blocks
BROKEN_MD_LINK_IN_CODE = re.compile(r"\[(https?://[^\]]+)\]\(\1\)")


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
        # Split by unescaped pipe
        raw_cells = [clean_cell(c) for c in line.strip().strip("|").split("|")]
        rows.append(raw_cells)

    if len(rows) < 2:
        return table_lines

    # Find header row (first non-empty, non-separator row)
    header_idx = 0
    for idx, r in enumerate(rows):
        if any(c for c in r) and not is_separator_or_empty_header(r):
            header_idx = idx
            break

    headers = [strip_backticks_and_bold(c).lower() for c in rows[header_idx]]

    # Skip conversion for non-command tables (e.g. Nano/Vim shortcuts in linux-commands-cheat-sheet-tables.md)
    if any(h in ("shortcut", "category", "mode/category", "trait", "layer", "protocol", "concept", "flag") for h in headers):
        return table_lines

    out = []
    for r in rows[header_idx + 1 :]:
        if is_separator_or_empty_header(r):
            continue
        if [strip_backticks_and_bold(c).lower() for c in r] == headers:
            continue

        # Repair broken pipe splits in fedora-quick-reference.md
        if len(headers) == 2 and len(r) > 2:
            r = [r[0], " | ".join(c for c in r[1:] if c)]

        # 1) 2-Column Table
        if len(headers) == 2 and len(r) >= 2:
            col0, col1 = r[0], r[1]
            if not col0 or not col1:
                continue

            # Determine which column is the command vs description
            if headers[0] in ("command", "option") and headers[1] in ("description", "action", "effect"):
                cmd = strip_backticks_and_bold(col0)
                desc = strip_backticks_and_bold(col1).rstrip(".")
                out.append(f"**{desc}:**")
                out.append(f"```{lang}")
                out.append(cmd)
                out.append("```")
                out.append("")
            else:
                # Action | Command
                label = strip_backticks_and_bold(col0).rstrip(":")
                # Extract trailing notes outside backticks if present
                m = re.match(r"^`([^`]+)`\s*(.+)$", col1)
                if m:
                    cmd, note = m.group(1).strip(), m.group(2).strip()
                    out.append(f"**{label}** {note}:")
                else:
                    cmd = strip_backticks_and_bold(col1)
                    out.append(f"**{label}:**")
                out.append(f"```{lang}")
                out.append(cmd)
                out.append("```")
                out.append("")

        # 2) 3-Column Table
        elif len(headers) == 3 and len(r) >= 3:
            c0, c1, c2 = r[0], r[1], r[2]

            # Case A: Action | CMD | PowerShell (windows-cmd-cheatsheet.md)
            if "cmd" in headers[1] and "powershell" in headers[2]:
                label = strip_backticks_and_bold(c0)
                cmd_val = strip_backticks_and_bold(c1)
                ps_val = strip_backticks_and_bold(c2)
                out.append(f"**{label} (CMD / PowerShell):**")
                out.append("```powershell")
                out.append(f"# CMD:        {cmd_val}")
                out.append(f"# PowerShell: {ps_val}")
                out.append("```")
                out.append("")

            # Case B: Action | Linux | Windows (pentesting-toolkit-cheat-sheet.md)
            elif "linux" in headers[1] and "windows" in headers[2]:
                label = strip_backticks_and_bold(c0)
                lin_val = strip_backticks_and_bold(c1)
                win_val = strip_backticks_and_bold(c2)
                out.append(f"**{label}:**")
                out.append("```bash")
                out.append(f"# Linux:   {lin_val}")
                out.append(f"# Windows: {win_val}")
                out.append("```")
                out.append("")

            # Case C: Action | Tool | Command (pentesting-toolkit-cheat-sheet.md)
            elif headers[1] == "tool":
                label = strip_backticks_and_bold(c0)
                tool = strip_backticks_and_bold(c1)
                cmd = strip_backticks_and_bold(c2)
                out.append(f"**{label} ({tool}):**")
                out.append(f"```{lang}")
                out.append(cmd)
                out.append("```")
                out.append("")

            # Case D: Action | GUI Equivalent | CLI Command (virt-manager-cheatsheet.md)
            elif "gui" in headers[1]:
                label = strip_backticks_and_bold(c0)
                gui = strip_backticks_and_bold(c1)
                cmd = strip_backticks_and_bold(c2)
                out.append(f"**{label}** *(GUI: {gui})*:")
                out.append(f"```{lang}")
                out.append(cmd)
                out.append("```")
                out.append("")

            # Case E: Action | Command Syntax | Example (grubby-command-reference.md)
            elif "syntax" in headers[1] and "example" in headers[2]:
                label = strip_backticks_and_bold(c0).rstrip(".")
                syntax = strip_backticks_and_bold(c1)
                example = strip_backticks_and_bold(c2)
                out.append(f"**{label}:**")
                out.append(f"```{lang}")
                if syntax != example:
                    out.append(f"# Syntax: {syntax}")
                out.append(example)
                out.append("```")
                out.append("")

            # Case F: Command | Description | Example (linux-commands-cheat-sheet-tables.md, nftables)
            else:
                cmd_name = strip_backticks_and_bold(c0)
                desc = strip_backticks_and_bold(c1).rstrip(".")
                example = strip_backticks_and_bold(c2)
                if example == 'printf "Result: %04d':
                    example = 'printf "Result: %04d\\n" 42'
                out.append(f"**`{cmd_name}` — {desc}:**")
                out.append(f"```{lang}")
                out.append(example)
                out.append("```")
                out.append("")

        # 3) 4-Column Table (iptables-cheat-sheet.md)
        elif len(headers) == 4 and len(r) >= 4:
            action = strip_backticks_and_bold(r[0])
            explanation = strip_backticks_and_bold(r[1]).rstrip(".")
            syntax = strip_backticks_and_bold(r[2])
            example = strip_backticks_and_bold(r[3])
            out.append(f"**{action}** — {explanation}:")
            out.append(f"```{lang}")
            if syntax != example:
                out.append(f"# Syntax: {syntax}")
            out.append(example)
            out.append("```")
            out.append("")

    return out if out else table_lines


# Bullet patterns to convert to fenced blocks:
# 1) - `opkg update` : Description
BULLET_CMD_FIRST = re.compile(r"^[\*\-]\s+`([^`]+)`\s*:\s*(.+)$")
# 2) - **Action:** `command`
BULLET_LABEL_FIRST = re.compile(r"^[\*\-]\s+\*\*(.+?):?\*\*:?\s*`([^`]+)`\s*(.*)$")


def process_file(filepath: Path) -> bool:
    if filepath.name in SKIP_FILES:
        return False

    original = filepath.read_text(encoding="utf-8")
    text = original

    # 1. Fix corrupted [https://...](https://...) links inside code blocks
    text = BROKEN_MD_LINK_IN_CODE.sub(r"\1", text)

    # 2. Fix escaped \vert{} in linux-export-command-guide.md
    text = text.replace(r"\vert{}", "|")

    # 3. Remove trailing conversational sentences in proxmox & windows-powershell-ad
    text = re.sub(
        r"\n\s*Would you like me to (include|create) [^\n]+\?\s*$",
        "\n",
        text,
        flags=re.MULTILINE,
    )

    lang = get_code_lang(filepath)
    lines = text.splitlines()
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

        # Detect start of a Markdown table
        if stripped.startswith("|") and stripped.endswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|") and lines[i].strip().endswith("|"):
                table_lines.append(lines[i])
                i += 1
            converted = convert_table_block(table_lines, filepath)
            out.extend(converted)
            continue

        # Convert bullet command items (- `cmd` : desc) in opkg-cheatsheet.md
        m_cmd_first = BULLET_CMD_FIRST.match(stripped)
        if m_cmd_first and filepath.name == "opkg-cheatsheet.md":
            cmd, desc = m_cmd_first.groups()
            out.append(f"**`{cmd}`** — {desc.strip()}")
            out.append(f"```{lang}")
            out.append(cmd.strip())
            out.append("```")
            out.append("")
            i += 1
            continue

        # Convert bullet label items (- **Label:** `cmd`) in winget, windows-cmd, pentesting, nmcli
        m_label_first = BULLET_LABEL_FIRST.match(stripped)
        if m_label_first and filepath.name in (
            "winget-cheat-sheet.md",
            "windows-cmd-cheatsheet.md",
            "pentesting-toolkit-cheat-sheet.md",
            "nmcli-cheat-sheet.md",
            "hyper-v-powershell-cheat-sheet.md",
        ):
            label, cmd, extra = m_label_first.groups()
            label = label.strip().rstrip(":")
            extra_str = f" {extra.strip()}" if extra.strip() else ""
            out.append(f"**{label}:**{extra_str}")
            out.append(f"```{lang}")
            out.append(cmd.strip())
            out.append("```")
            out.append("")
            i += 1
            continue

        out.append(line)
        i += 1

    result = "\n".join(out)
    # Collapse 3+ consecutive newlines to 2
    result = re.sub(r"\n{3,}", "\n\n", result).strip() + "\n"

    if result != original:
        filepath.write_text(result, encoding="utf-8")
        return True
    return False


if __name__ == "__main__":
    repo_root = Path(".")
    modified_count = 0
    for md_file in sorted(repo_root.rglob("*.md")):
        if ".git" in md_file.parts:
            continue
        if process_file(md_file):
            print(f"Updated: {md_file}")
            modified_count += 1
    print(f"\nDone! Modernized {modified_count} Markdown files.")
