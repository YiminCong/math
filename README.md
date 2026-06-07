# Math Guides

A small library of illustrated, self-contained reference guides for **calculus**
and **statistics**. Each guide is a single HTML file that renders math with
[KaTeX](https://katex.org/) — open it in any browser, no build step required.

## Start here

Open **[`index.html`](index.html)** for a landing page that links to every guide
and lets you **search across every section at once** (type `/` to jump to the
search box).

## What's inside

### Calculus — [`calculus/`](calculus/)

| Guide | File | Best for |
| --- | --- | --- |
| **The Complete Companion** | [`calculus/complete-guide.html`](calculus/complete-guide.html) | A full single-variable course (30 sections), following the flow of Banner's *Calculus Lifesaver* |
| **Derived from Scratch** | [`calculus/derived-from-scratch.html`](calculus/derived-from-scratch.html) | Every core formula demonstrated step by step — the "why" |
| **From the Ground Up** | [`calculus/connected-map.html`](calculus/connected-map.html) | A fast, big-picture map of how the ideas connect |
| **Glossary (EN ↔ 中文)** | [`calculus/glossary.html`](calculus/glossary.html) | A searchable English ↔ Simplified-Chinese term reference |

### Statistics — [`statistics/`](statistics/)

| Guide | File | Best for |
| --- | --- | --- |
| **The Complete Companion** | [`statistics/complete-guide.html`](statistics/complete-guide.html) | A first course: describing data, probability, and inference (15 sections) |

## Viewing locally

The files work by double-clicking, but to let the in-page links and search
behave like a site, serve the folder:

```sh
python3 -m http.server
# then open http://localhost:8000
```

Fonts and the KaTeX math fonts load from a CDN, so an internet connection gives
the best-looking result.
