# Math Guides

An illustrated, self-contained **calculus curriculum** — from precalculus
foundations all the way to graduate-level rigor — plus a growing set of other
subjects. Every guide is a single HTML file that renders math with
[KaTeX](https://katex.org/); open it in any browser, no build step required.

## Start here

Open **[`index.html`](index.html)**. It offers three ways in:

- **The learning path** — nine ordered steps from starter to expertise.
- **Browse by topic** — jump straight to a single idea.
- **Search** — one box searches every section of every guide and deep-links to it
  (press `/` to focus). Each guide also has its own in-page section search.

## The calculus learning path

| Step | Focus | Where |
| --- | --- | --- |
| 0 · Foundations | Functions, lines, trigonometry | [`complete-guide.html#s1`](calculus/complete-guide.html#s1) |
| 1 · Calculus I | Limits & continuity | [`complete-guide.html#s3`](calculus/complete-guide.html#s3) |
| 2 · Calculus I | Derivatives & their uses | [`complete-guide.html#s6`](calculus/complete-guide.html#s6) |
| 3 · Calculus II | Integrals & their uses | [`complete-guide.html#s14`](calculus/complete-guide.html#s14) |
| 4 · Calculus II | Sequences & series | [`complete-guide.html#s23`](calculus/complete-guide.html#s23) |
| 5 · Calculus II | Parametric, polar & complex | [`complete-guide.html#s26`](calculus/complete-guide.html#s26) |
| 6 · Calculus III | Multivariable & vector calculus | [`multivariable-vector.html`](calculus/multivariable-vector.html) |
| 7 · Advanced | Differential equations | [`differential-equations.html`](calculus/differential-equations.html) |
| 8 · Expertise | Foundations of analysis (rigor) | [`analysis-foundations.html`](calculus/analysis-foundations.html) |

## The topology learning path

| Step | Focus | Where |
| --- | --- | --- |
| 0 · Foundations | Sets, functions & metric spaces | [`general-topology.html#s1`](topology/general-topology.html#s1) |
| 1 · Point-set | Topological spaces, basis, closure | [`general-topology.html#s3`](topology/general-topology.html#s3) |
| 2 · Point-set | Continuity & constructions | [`general-topology.html#s7`](topology/general-topology.html#s7) |
| 3 · Point-set | Connectedness & compactness | [`general-topology.html#s10`](topology/general-topology.html#s10) |
| 4 · Point-set | Separation, countability & metrization | [`general-topology.html#s16`](topology/general-topology.html#s16) |
| 5 · Point-set | Convergence & completeness (nets, filters, Baire) | [`general-topology.html#s20`](topology/general-topology.html#s20) |
| 6 · Algebraic | Homotopy & the fundamental group | [`algebraic-topology.html#s0`](topology/algebraic-topology.html#s0) |
| 7 · Algebraic | Covering spaces | [`algebraic-topology.html#s6`](topology/algebraic-topology.html#s6) |
| 8 · Expertise | Homology & cohomology | [`algebraic-topology.html#s9`](topology/algebraic-topology.html#s9) |

## What's inside

### Calculus — [`calculus/`](calculus/)

**Core course**

| Guide | File | Covers |
| --- | --- | --- |
| The Complete Companion | [`complete-guide.html`](calculus/complete-guide.html) | Full single-variable course (Calc I & II), 30 sections, after Banner's *Calculus Lifesaver* |
| Multivariable & Vector Calculus | [`multivariable-vector.html`](calculus/multivariable-vector.html) | Calc III: partials, gradients, Lagrange, multiple integrals, Green's/Stokes'/Divergence |
| Differential Equations | [`differential-equations.html`](calculus/differential-equations.html) | First/second-order ODEs, systems, Laplace, series & numerical methods |
| Foundations of Analysis | [`analysis-foundations.html`](calculus/analysis-foundations.html) | Rigorous theory: completeness, ε–δ, uniform convergence, the Riemann integral, proved |

**Companions & reference**

| Guide | File | Best for |
| --- | --- | --- |
| Derived from Scratch | [`derived-from-scratch.html`](calculus/derived-from-scratch.html) | A proof-first companion to single-variable calculus |
| From the Ground Up | [`connected-map.html`](calculus/connected-map.html) | A fast, big-picture map of how the ideas connect |
| Glossary (EN ↔ 中文) | [`glossary.html`](calculus/glossary.html) | Searchable English ↔ Simplified-Chinese term reference |

### Topology — [`topology/`](topology/)

| Guide | File | Covers |
| --- | --- | --- |
| General Topology | [`general-topology.html`](topology/general-topology.html) | Point-set: metric & topological spaces, continuity, connectedness & compactness, separation axioms, metrization, nets/filters, Baire (23 sections) |
| Algebraic Topology | [`algebraic-topology.html`](topology/algebraic-topology.html) | Homotopy & the fundamental group, covering spaces, singular/simplicial homology & cohomology (15 sections) |
| Glossary (EN ↔ 中文) | [`glossary.html`](topology/glossary.html) | Searchable English ↔ Simplified-Chinese topology term reference |

### Statistics — [`statistics/`](statistics/)

| Guide | File | Covers |
| --- | --- | --- |
| The Complete Companion | [`complete-guide.html`](statistics/complete-guide.html) | A first course: describing data, probability, and inference (15 sections) |

*(More subjects can be added alongside these.)*

## Viewing locally

The files work by double-clicking, but to let the in-page links and search behave
like a site, serve the folder:

```sh
python3 -m http.server
# then open http://localhost:8000
```

Fonts and the KaTeX math fonts load from a CDN, so an internet connection gives
the best-looking result.
