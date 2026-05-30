#!/usr/bin/env python3
"""Batch-update all HTML files: extract inline CSS, add favicon, add modul nav."""

import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))

# === Shared inline CSS block found in all content pages ===
SHARED_CSS = """    <style>
        :root {
            --bg: #0d1117;
            --bg-card: #161b22;
            --border: #30363d;
            --text: #e6edf3;
            --text-muted: #8b949e;
            --accent: #58a6ff;
            --link: #58a6ff;
            --code-bg: #1c2333;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.7;
        }
        .container {
            max-width: 880px;
            margin: 0 auto;
            padding: 2rem 1.5rem 4rem;
        }
        .top-nav {
            display: flex;
            align-items: center;
            gap: 1rem;
            padding: 0.75rem 1.5rem;
            background: var(--bg-card);
            border-bottom: 1px solid var(--border);
            position: sticky;
            top: 0;
            z-index: 10;
        }
        .top-nav a {
            color: var(--accent);
            text-decoration: none;
            font-size: 0.9rem;
        }
        .top-nav a:hover { text-decoration: underline; }
        .top-nav .title-nav {
            font-size: 0.85rem;
            color: var(--text-muted);
            margin-left: auto;
        }
        h1 { font-size: 2rem; font-weight: 700; margin-bottom: 1rem; padding-bottom: 0.5rem; border-bottom: 1px solid var(--border); }
        h2 { font-size: 1.5rem; font-weight: 600; margin-top: 2rem; margin-bottom: 0.75rem; }
        h3 { font-size: 1.2rem; font-weight: 600; margin-top: 1.5rem; margin-bottom: 0.5rem; }
        h4 { font-size: 1.05rem; font-weight: 600; margin-top: 1.25rem; margin-bottom: 0.5rem; }
        p { margin-bottom: 1rem; color: var(--text-muted); }
        strong { color: var(--text); }
        a { color: var(--link); }
        ul, ol { margin-bottom: 1rem; padding-left: 1.5rem; color: var(--text-muted); }
        li { margin-bottom: 0.3rem; }
        blockquote {
            border-left: 4px solid var(--accent);
            padding: 0.75rem 1rem;
            margin: 1rem 0;
            background: rgba(88,166,255,0.06);
            border-radius: 0 6px 6px 0;
            color: var(--text-muted);
        }
        blockquote p { margin-bottom: 0; }
        hr { border: none; border-top: 1px solid var(--border); margin: 2rem 0; }
        table { width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.9rem; }
        th, td { padding: 0.5rem 0.75rem; border: 1px solid var(--border); text-align: left; }
        th { background: var(--bg-card); font-weight: 600; }
        td { color: var(--text-muted); }
        code {
            font-family: 'JetBrains Mono', 'Fira Code', Consolas, monospace;
            font-size: 0.85em;
            background: var(--code-bg);
            padding: 0.15em 0.4em;
            border-radius: 4px;
            color:rgb(255, 198, 109);
        }
        pre {
            background: var(--code-bg);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 1rem;
            margin: 1rem 0;
            overflow-x: auto;
        }
        pre code { background: none; padding: 0; font-size: 0.85rem; line-height: 1.6; color: inherit; }
        @media (max-width: 720px) { .container { padding: 1rem; } h1 { font-size: 1.5rem; } }
    </style>"""

FAVICON = '    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🐍</text></svg>">'

CSS_REPLACEMENT_ROOT = f'    <link rel="stylesheet" href="style.css">\n{FAVICON}'
CSS_REPLACEMENT_MODUL = f'    <link rel="stylesheet" href="../style.css">\n{FAVICON}'

# === Modul navigation mapping ===
MODUL_ORDER = [
    ("00-setup",          "🔧 Setup"),
    ("01-variabel-tipe-data", "📦 Variabel & Tipe Data"),
    ("02-string",         "🧵 String"),
    ("03-list-tuple",     "📋 List & Tuple"),
    ("04-dictionary-set", "🔑 Dictionary & Set"),
    ("05-percabangan",    "🔀 Percabangan"),
    ("06-perulangan",     "🔄 Perulangan"),
    ("07-function",       "⚡ Function"),
    ("08-error-exception","❌ Error & Exception"),
    ("09-file-io",        "📁 File I/O"),
    ("10-module-pip",     "📦 Module & pip"),
    ("11-list-comprehension", "🌀 List Comprehension"),
    ("12-oop-dasar",      "🧱 OOP Dasar"),
    ("13-proyek-akhir",   "🏆 Proyek Akhir"),
]


def make_modul_nav(current_slug):
    """Generate prev/next navigation HTML for a modul page."""
    current_index = None
    for i, (slug, _) in enumerate(MODUL_ORDER):
        if slug == current_slug:
            current_index = i
            break

    if current_index is None:
        return ""

    prev_slug, prev_title = MODUL_ORDER[current_index - 1] if current_index > 0 else (None, None)
    next_slug, next_title = MODUL_ORDER[current_index + 1] if current_index < len(MODUL_ORDER) - 1 else (None, None)

    parts = []
    if prev_slug:
        parts.append(f'        <a href="{prev_slug}.html">« {prev_title}</a>')
    else:
        parts.append('        <span class="modul-nav-disabled">« Awal</span>')

    parts.append('        <span class="modul-nav-center">⬅ <a href="../index.html">Index</a></span>')

    if next_slug:
        parts.append(f'        <a href="{next_slug}.html">{next_title} »</a>')
    else:
        parts.append('        <span class="modul-nav-disabled">Selesai »</span>')

    nav_html = '    <nav class="modul-nav">\n' + '\n'.join(parts) + '\n    </nav>'
    return nav_html


def replace_in_file(filepath, old, new):
    """Replace old string with new string in file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if old in content:
        content = content.replace(old, new)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def insert_before_closing_div(filepath, insertion):
    """Insert HTML before the closing </div> of .container."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the last </div> before </div>\n    <script>
    pattern = r'(</div>\n    <script>document\.querySelectorAll)'
    result = re.sub(pattern, insertion + r'\n\1', content)
    
    if result != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(result)
        return True
    return False


def update_root_page(filename):
    """Update root content pages (pengantar, cheat-sheet, etc.)."""
    filepath = os.path.join(BASE, filename)
    if not os.path.exists(filepath):
        return False, "file not found"
    
    replaced = replace_in_file(filepath, SHARED_CSS, CSS_REPLACEMENT_ROOT)
    if not replaced:
        return False, "CSS block not found"
    
    return True, "ok"


def update_modul_page(slug):
    """Update a modul HTML page."""
    filename = f"{slug}.html"
    filepath = os.path.join(BASE, 'modul', filename)
    if not os.path.exists(filepath):
        return False, "file not found"
    
    replaced = replace_in_file(filepath, SHARED_CSS, CSS_REPLACEMENT_MODUL)
    if not replaced:
        return False, "CSS block not found"
    
    nav_html = make_modul_nav(slug)
    inserted = insert_before_closing_div(filepath, nav_html)
    if not inserted:
        return False, "could not insert nav"
    
    return True, "ok"


def update_index():
    """Update index.html — add favicon, minor responsive tweaks."""
    filepath = os.path.join(BASE, 'index.html')
    if not os.path.exists(filepath):
        return False, "file not found"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    favicon_tag = '<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🐍</text></svg>">'
    content = content.replace('</title>', f'</title>\n    {favicon_tag}')
    
    css_link = '<link rel="stylesheet" href="style.css">'
    if css_link not in content:
        content = content.replace('<title>', f'    {css_link}\n    <title>')
    
    old_responsive = """        @media (max-width: 720px) {
            .hero h1 { font-size: 1.8rem; }
            .two-col { grid-template-columns: 1fr; gap: 0; }
            .grid { grid-template-columns: 1fr; }
        }"""
    
    new_responsive = """        @media (max-width: 768px) {
            .hero h1 { font-size: 1.8rem; }
            .two-col { grid-template-columns: 1fr; gap: 0; }
            .grid { grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); }
            .hero { padding: 2.5rem 0 2rem; }
            .hero .info { gap: 1rem; font-size: 0.82rem; }
        }
        @media (max-width: 480px) {
            .hero h1 { font-size: 1.4rem; }
            .hero .info { flex-direction: column; align-items: center; gap: 0.5rem; }
            .grid { grid-template-columns: 1fr; }
            .link-list { grid-template-columns: 1fr; }
            .card { padding: 1rem; }
            .section { padding: 1.5rem 0; }
        }"""
    
    content = content.replace(old_responsive, new_responsive)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True, "ok"


def main():
    results = []
    
    # 1. Update index.html
    ok, msg = update_index()
    results.append(("index.html", ok, msg))
    
    # 2. Update root content pages
    root_pages = ["pengantar.html", "cheat-sheet.html", "bank-soal.html",
                  "error-dictionary.html", "tips-mengajar.html", "mini-projek.html"]
    for page in root_pages:
        ok, msg = update_root_page(page)
        results.append((page, ok, msg))
    
    # 3. Update modul pages
    for slug, _ in MODUL_ORDER:
        ok, msg = update_modul_page(slug)
        results.append((f"modul/{slug}.html", ok, msg))
    
    # Print report
    print("=" * 60)
    print("📋  HTML UPDATE REPORT")
    print("=" * 60)
    success = 0
    failed = 0
    for name, ok, msg in results:
        status = "✅" if ok else "❌"
        print(f"  {status}  {name:40s}  {msg}")
        if ok:
            success += 1
        else:
            failed += 1
    print("=" * 60)
    print(f"  Total: {len(results)}  |  ✅ {success}  |  ❌ {failed}")
    print("=" * 60)


if __name__ == "__main__":
    main()
