#!/usr/bin/env python3
import os
import re
from pathlib import Path

def remove_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex looks for "---" at the very start, captures everything until the next "---", and removes it along with trailing newlines
    new_content = re.sub(r'^---\n.*?\n---\n*', '', content, flags=re.DOTALL)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    repo_root = Path(".")
    modified_count = 0
    
    for root, _, files in os.walk(repo_root):
        if '.git' in root or '.github' in root:
            continue
            
        for file in files:
            if file.endswith('.md'):
                file_path = Path(root) / file
                if remove_frontmatter(file_path):
                    print(f"Stripped frontmatter: {file_path}")
                    modified_count += 1
                    
    print(f"\nSuccessfully removed frontmatter from {modified_count} files.")

if __name__ == "__main__":
    main()
