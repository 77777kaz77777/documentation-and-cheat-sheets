#!/usr/bin/env python3
"""generate_redirects.py: write redirect pages for moved guides.

Run after `zensical build`. For every old address in redirects.yml it writes a
tiny HTML page into site/ that forwards the browser to the page's new address,
keeping any #section in the link. GitHub Pages has no server-side redirects,
so this is the standard way to keep old links working.
"""
import html
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

import yaml

SITE = Path(sys.argv[1] if len(sys.argv) > 1 else "site")
config = yaml.safe_load(Path("tools/redirects.yml").read_text(encoding="utf-8"))
base = urlparse(yaml.safe_load(
    "\n".join(l for l in Path("mkdocs.yml").read_text(encoding="utf-8").splitlines() if l.startswith("site_url:"))
)["site_url"]).path.rstrip("/") + "/"

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Moved: {title}</title>
<link rel="canonical" href="{url}">
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url={url}">
<script>location.replace({url_js} + location.hash);</script>
</head>
<body>
<p>This page has moved to <a href="{url}">{title}</a>.</p>
</body>
</html>
"""


def built_url(page_md: str) -> str:
    """The URL the build gave a .md page (directory or .html style)."""
    stem = page_md[:-3] if page_md.endswith(".md") else page_md
    if (SITE / stem / "index.html").exists():
        return base + stem + "/"
    if (SITE / f"{stem}.html").exists():
        return base + stem + ".html"
    raise SystemExit(f"redirect target not built: {page_md}")


def write(old_stem: str, url: str, title: str) -> int:
    page = TEMPLATE.format(url=html.escape(url), url_js=json.dumps(url), title=html.escape(title))
    written = 0
    # Cover both URL styles for the old address: /old/ and /old.html
    for path in (SITE / old_stem / "index.html", SITE / f"{old_stem}.html"):
        if path.exists():
            raise SystemExit(f"refusing to overwrite a real page: {path}")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(page, encoding="utf-8")
        written += 1
    return written


count = 0
for old, new in (config.get("pages") or {}).items():
    count += write(old[:-3], built_url(new), Path(new).stem.replace("-", " "))
for old, new in (config.get("folders") or {}).items():
    count += write(old.rstrip("/"), base + new.rstrip("/") + "/", new.rstrip("/").replace("-", " "))
print(f"wrote {count} redirect pages")
