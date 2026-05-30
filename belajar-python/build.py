#!/usr/bin/env python3
"""Convert all .md files to static .html pages with proper styling."""

import os
import re
import html as html_mod

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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


def make_modul_nav(current_slug, index_path):
    """Generate prev/next navigation HTML for a modul page."""
    current_index = next((i for i, (slug, _) in enumerate(MODUL_ORDER) if slug == current_slug), None)
    if current_index is None:
        return ""

    prev_slug, prev_title = MODUL_ORDER[current_index - 1] if current_index > 0 else (None, None)
    next_slug, next_title = MODUL_ORDER[current_index + 1] if current_index < len(MODUL_ORDER) - 1 else (None, None)

    parts = []
    if prev_slug:
        parts.append(f'        <a href="{prev_slug}.html">« {prev_title}</a>')
    else:
        parts.append('        <span class="modul-nav-disabled">« Awal</span>')

    parts.append(f'        <span class="modul-nav-center">⬅ <a href="{index_path}">Index</a></span>')

    if next_slug:
        parts.append(f'        <a href="{next_slug}.html">{next_title} »</a>')
    else:
        parts.append('        <span class="modul-nav-disabled">Selesai »</span>')

    return '    <nav class="modul-nav">\n' + '\n'.join(parts) + '\n    </nav>'


def make_template(index_path, style_path, is_modul=False, modul_slug=None):
    FAVICON = '<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🐍</text></svg>">'

    nav_html = ""
    if is_modul and modul_slug:
        nav_html = "\n" + make_modul_nav(modul_slug, index_path)

    tmpl = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>__TITLE__ — Belajar Python</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <link rel="stylesheet" href="{style_path}">
    {FAVICON}
</head>
<body>
    <nav class="top-nav">
        <a href="{index_path}">⬅ Kembali ke Index</a>
        <span class="title-nav">__TITLE__</span>
    </nav>
    <div class="container">
__CONTENT__{nav_html}
    </div>
    <script>document.querySelectorAll('pre code').forEach(b=>hljs.highlightElement(b));</script>
</body>
</html>"""
    return tmpl


def md_to_html(text):
    """Convert markdown to HTML (handles the subset used in this project)."""
    lines = text.split('\n')
    result = []
    i = 0
    in_code_block = False
    code_buffer = []
    in_table = False
    table_buffer = []
    in_list = False

    while i < len(lines):
        line = lines[i]

        # Code block
        if line.startswith('```'):
            if in_code_block:
                lang = code_buffer[0][3:] if code_buffer[0].startswith('```') else ''
                code_content = '\n'.join(code_buffer[1:])
                escaped = html_mod.escape(code_content)
                if lang:
                    result.append(f'<pre><code class="language-{html_mod.escape(lang)}">{escaped}</code></pre>')
                else:
                    result.append(f'<pre><code>{escaped}</code></pre>')
                code_buffer = []
                in_code_block = False
            else:
                in_code_block = True
                code_buffer = [line]
            i += 1
            continue

        if in_code_block:
            code_buffer.append(line)
            i += 1
            continue

        if in_table and not line.strip():
            in_table = False
            table_buffer.append('</table>\n')
            result.append(''.join(table_buffer))
            table_buffer = []
            i += 1
            continue

        # Table
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                in_table = True
                table_buffer = ['<table>\n']
            # Header separator row
            if re.match(r'^\|[\s\-:|]+\|$', line):
                i += 1
                continue
            cells = [c.strip() for c in line.split('|') if c.strip()]
            tag = 'th' if len(table_buffer) == 1 else 'td'
            table_buffer.append('<tr>')
            for cell in cells:
                cell = inline_md(cell)
                table_buffer.append(f'<{tag}>{cell}</{tag}>')
            table_buffer.append('</tr>\n')
            i += 1
            continue

        if in_table:
            in_table = False
            table_buffer.append('</table>\n')
            result.append(''.join(table_buffer))
            table_buffer = []

        # Headings
        m = re.match(r'^(#{1,4})\s+(.+)$', line)
        if m:
            level = len(m.group(1))
            content = inline_md(m.group(2))
            result.append(f'<h{level}>{content}</h{level}>')
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^---+\s*$', line) and not line.startswith('```'):
            result.append('<hr>')
            i += 1
            continue

        # Blockquote
        if line.startswith('> '):
            bq_content = inline_md(line[2:])
            result.append(f'<blockquote><p>{bq_content}</p></blockquote>')
            i += 1
            continue

        # Unordered list
        if re.match(r'^[\s]*[-*+]\s+', line):
            items = []
            while i < len(lines) and re.match(r'^[\s]*[-*+]\s+', lines[i]):
                item_text = re.sub(r'^[\s]*[-*+]\s+', '', lines[i])
                items.append(f'<li>{inline_md(item_text)}</li>')
                i += 1
            result.append('<ul>' + ''.join(items) + '</ul>')
            continue

        # Ordered list
        if re.match(r'^\s*\d+[.)]\s+', line):
            items = []
            while i < len(lines) and re.match(r'^\s*\d+[.)]\s+', lines[i]):
                item_text = re.sub(r'^\s*\d+[.)]\s+', '', lines[i])
                items.append(f'<li>{inline_md(item_text)}</li>')
                i += 1
            result.append('<ol>' + ''.join(items) + '</ol>')
            continue

        # Empty line
        if not line.strip():
            result.append('')
            i += 1
            continue

        # Paragraph
        result.append(f'<p>{inline_md(line)}</p>')
        i += 1

    if in_table:
        table_buffer.append('</table>\n')
        result.append(''.join(table_buffer))

    return '\n'.join(result)


def inline_md(text):
    """Convert inline markdown (bold, italic, code, links)."""
    # Inline code first (protect from other transforms)
    text = re.sub(r'`([^`]+)`', lambda m: f'<code>{html_mod.escape(m.group(1))}</code>', text)
    # Bold-italic ***text***
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    # Bold **text**
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic *text*
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', text)
    # Links [text](url)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    # Images ![alt](url)
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', text)
    # HTML entities
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    # Restore code tags
    text = text.replace('&lt;code&gt;', '<code>').replace('&lt;/code&gt;', '</code>')
    text = text.replace('&lt;strong&gt;', '<strong>').replace('&lt;/strong&gt;', '</strong>')
    text = text.replace('&lt;em&gt;', '<em>').replace('&lt;/em&gt;', '</em>')
    text = text.replace('&lt;a', '<a').replace('&lt;/a&gt;', '</a>')
    text = text.replace('&lt;img', '<img')
    text = text.replace('&amp;', '&')  # Restore original ampersands
    # But re-escape ampersands in text content (not in HTML tags)
    # This is getting complex, let's just do it simply
    return text


def convert_file(filepath, index_path, style_path, is_modul=False, modul_slug=None):
    with open(filepath, 'r', encoding='utf-8') as f:
        md_content = f.read()

    title_match = re.search(r'^#\s+(.+)$', md_content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else 'Materi'
    title = re.sub(r'^[^\w\s]{1,3}\s*', '', title)
    title = html_mod.escape(title)

    html_body = md_to_html(md_content)

    indented = '\n'.join('        ' + line for line in html_body.split('\n'))

    template = make_template(index_path, style_path, is_modul=is_modul, modul_slug=modul_slug)
    html_page = template.replace('__TITLE__', title).replace('__CONTENT__', indented)
    return html_page


def main():
    mappings = []

    # Convert all .md files in modul/
    modul_dir = os.path.join(BASE_DIR, 'modul')
    for fname in sorted(os.listdir(modul_dir)):
        if fname.endswith('.md'):
            src = os.path.join(modul_dir, fname)
            dst_name = fname[:-3] + '.html'
            dst = os.path.join(modul_dir, dst_name)
            modul_slug = fname[:-3]
            html = convert_file(src, '../index.html', '../style.css', is_modul=True, modul_slug=modul_slug)
            with open(dst, 'w', encoding='utf-8') as f:
                f.write(html)
            mappings.append((f'modul/{fname}', f'modul/{dst_name}'))
            print(f'  ✓ modul/{fname} → modul/{dst_name}')

    # Convert root .md files
    for fname in sorted(os.listdir(BASE_DIR)):
        if fname.endswith('.md') and fname != 'README.md':
            src = os.path.join(BASE_DIR, fname)
            dst_name = fname[:-3] + '.html'
            dst = os.path.join(BASE_DIR, dst_name)
            html = convert_file(src, 'index.html', 'style.css')
            with open(dst, 'w', encoding='utf-8') as f:
                f.write(html)
            mappings.append((fname, dst_name))
            print(f'  ✓ {fname} → {dst_name}')

    readme_src = os.path.join(BASE_DIR, 'README.md')
    if os.path.exists(readme_src):
        with open(readme_src, 'r', encoding='utf-8') as f:
            md_content = f.read()
        title = 'Pengantar'
        html_body = md_to_html(md_content)
        indented = '\n'.join('        ' + line for line in html_body.split('\n'))
        template = make_template('index.html', 'style.css')
        html_page = template.replace('__TITLE__', title).replace('__CONTENT__', indented)
        dst = os.path.join(BASE_DIR, 'pengantar.html')
        with open(dst, 'w', encoding='utf-8') as f:
            f.write(html_page)
        print(f'  ✓ README.md → pengantar.html')

    print(f'\n✅ {len(mappings) + 1} file HTML berhasil dibuat.')
    return mappings


if __name__ == '__main__':
    mappings = main()
