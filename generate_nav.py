import os
import yaml
from pathlib import Path

def build_nav(directory='.'):
    nav = []
    for path in sorted(Path(directory).iterdir()):
        if path.name.startswith('.') or path.name in ['assets', 'site', 'utils', 'venv']:
            continue
        
        if path.is_file():
            if path.suffix != '.md':
                continue
            if path.name == 'index.md' and directory == '.':
                nav.insert(0, {'Home': 'index.md'})
            elif path.name != 'index.md':
                nav.append({path.name: str(path)})
        elif path.is_dir():
            sub_nav = build_nav(path)
            if sub_nav:
                dir_name = path.name.replace('-', ' ').title()
                nav.append({dir_name: sub_nav})
    return nav

with open('mkdocs.yml', 'r') as f:
    config = yaml.safe_load(f)

config['nav'] = build_nav()

with open('mkdocs.yml', 'w') as f:
    yaml.dump(config, f, default_flow_style=False, sort_keys=False)
