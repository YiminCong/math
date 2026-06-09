#!/usr/bin/env bash
set -euo pipefail
rm -rf docs && mkdir -p docs/assets
cp -r calculus complex-analysis differential-geometry functional-analysis \
      group-theory linear-algebra math-methods statistics topology docs/
cp README.md README.zh.md docs/
cp assets/mathjax.js docs/assets/
python3 -m mkdocs build -d "${1:-site}"
