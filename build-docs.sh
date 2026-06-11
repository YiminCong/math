#!/usr/bin/env bash
set -euo pipefail
rm -rf docs && mkdir -p docs/assets
cp -r calculus complex-analysis differential-geometry functional-analysis \
      group-theory linear-algebra math-methods statistics topology docs/
cp README.md README.zh.md docs/
cp assets/mathjax.js docs/assets/
# Adapt the copied Markdown for the MkDocs + i18n build:
#  1) drop the manual top-of-file language switcher (Material has its own selector;
#     the relative .zh.md link doesn't resolve under the i18n suffix layout)
#  2) rewrite link targets X.zh.md -> X.md so the i18n plugin resolves them to the
#     current language (e.g. the Chinese index's tables point to the /zh/ pages)
python3 - <<'PY'
import glob, io, re
sw = re.compile(r'(\*\*English\*\*|\[English\]).*(\[中文\]|\*\*中文\*\*)')
for f in glob.glob('docs/**/*.md', recursive=True):
    lines = io.open(f, encoding='utf-8').read().split('\n')
    if lines and sw.search(lines[0]):
        del lines[0]
        if lines and lines[0].strip() == '':
            del lines[0]
    text = '\n'.join(lines)
    text = re.sub(r'\]\(([^)\s]*?)\.zh\.md', r'](\1.md', text)   # link targets only
    io.open(f, 'w', encoding='utf-8').write(text)
PY
python3 -m mkdocs build -d "${1:-site}"
