#!/usr/bin/env python3
import os
from pathlib import Path

def remove_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    if not lines:
        return False

    # Check if the first line is the start of YAML frontmatter
    if lines[0].strip() == '---':
        end_idx = -1
        # Find the closing '---'
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                end_idx = i
                break
        
        if end_idx != -1:
            # Slice the array to keep only the content after the frontmatter
            new_lines = lines[end_idx + 1:]
            
            # Strip any lingering blank lines at the new top of the file
            while new_lines and new_lines[0].strip() == '':
                new_lines.pop(0)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
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
