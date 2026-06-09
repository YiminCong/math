**English** · [中文](functional-analysis.zh.md)

# Functional Analysis & Hilbert Spaces, *the rigorous home of quantum mechanics.*

*A first rigorous course in functional analysis, built for the place its language is spoken most precisely — quantum mechanics, where a state is a vector in an infinite-dimensional Hilbert space and every observable is a (possibly unbounded) self-adjoint operator. We start from metric completeness, climb through Banach and Hilbert spaces to the spectral theorem and the functional calculus, and end with distributions and the rigged-Hilbert-space picture that makes Dirac's $\delta$ and continuous spectra honest. Every term is defined the first time it appears, and every theorem is proved or its proof sketched with all key steps named.*

[← Back to all guides](../README.md)

> **How to read this guide.** We assume the **Linear Algebra** guide (vector spaces, linear maps, inner products, adjoints, the finite-dimensional spectral theorem) and the **Analysis-foundations** guide (limits, $\varepsilon$–$N$ arguments, suprema, Cauchy sequences, and the completeness of $\mathbb{R}$). When we use a fact from either, we restate it in one line. Everything specific to functional analysis — *Banach space*, *Hilbert space*, *orthonormal basis*, *bounded operator*, *adjoint*, *spectrum*, *compact operator*, *self-adjointness*, *distribution* — is defined where it first appears, with a worked numerical example. Nothing is "left to the reader." Where the physics illuminates the mathematics we point it out, but this is a **math** guide: claims are proved.

---

## Part A — Spaces: completeness, norms, and inner products

<a id="s0"></a>
### Why functional analysis: infinite-dimensional state spaces and operators

Finite-dimensional linear algebra describes a qubit perfectly: its state lives in $\mathbb{C}^2$, an observable is a $2\times 2$ Hermitian matrix, and the spectral theorem guarantees a complete orthonormal eigenbasis. But the moment we ask about a particle that can sit *anywhere on a line*, the state is no longer a list of two complex numbers — it is a **wavefunction** $\psi(x)$, a complex-valued function of position. The "components" of the state are now indexed by a continuum, and the natural state space is infinite-dimensional.

This single jump breaks almost everything we took for granted in finite dimensions, and **functional analysis** is the subject that repairs it carefully:

- In $\mathbb{C}^n$ every linear map is continuous and bounded. In infinite dimensions there are *unbounded* operators — and the two most important observables, **position** $\hat{x}\psi(x)=x\,\psi(x)$ and **momentum** $\hat{p}\psi=-i\hbar\,\psi'$, are exactly of this dangerous kind. They are only defined on *part* of the space, and the difference between "symmetric" and "self-adjoint" — invisible in finite dimensions — becomes the difference between a sensible observable and a broken one.
- In $\mathbb{C}^n$ every Cauchy sequence converges. In a general normed space it need not, and limits of wavefunctions (the heart of every approximation in physics) only make sense if the space is **complete**. Completeness is the property that earns the name **Banach space**, and with an inner product, **Hilbert space**.
- In $\mathbb{C}^n$ a Hermitian matrix always has eigenvalues. The momentum operator on the line has *no eigenvectors in the space at all* — the "eigenfunction" $e^{ipx/\hbar}$ is not square-integrable. Its values form a **continuous spectrum**, and the eigenvalue concept must be generalized to the **spectrum** and tamed by the **spectral theorem** for unbounded operators, with Dirac's $\delta$ and the **rigged Hilbert space** providing the bookkeeping.

So the plan is honest: build the analysis rigorously — completeness first, then norms, then inner products, then operators and their spectra — and at each milestone read off the quantum-mechanical meaning. The recurring slogan is that **a Hilbert space is exactly a vector space where geometry (lengths and angles) survives into infinitely many dimensions, provided we also demand that limits stay inside.** Let us make each word of that precise.

> **The physical hook.** A wavefunction $\psi$ is normalized so that $\int |\psi(x)|^2\,dx = 1$; the integral is the total probability of finding the particle somewhere. The space of such functions, $L^2(\mathbb{R})$, is the prototype Hilbert space, and the integral $\int|\psi|^2$ is the squared length $\|\psi\|^2$. Geometry *is* probability here.

<a id="s1"></a>
### Metric spaces and completeness revisited; Cauchy sequences

**What and why.** Before lengths and angles we need only the bare notion of **distance**, because completeness — the guarantee that limits exist — is purely a statement about distances. We recall the definitions briefly (they live in the Analysis-foundations guide) and then build the machinery we will lean on.

> **Definition — metric space.** A **metric space** is a set $X$ together with a function $d:X\times X\to\mathbb{R}$, the **metric** (or distance), such that for all $x,y,z\in X$:
> 1. **(Non-negativity & identity)** $d(x,y)\ge 0$, and $d(x,y)=0$ iff $x=y$;
> 2. **(Symmetry)** $d(x,y)=d(y,x)$;
> 3. **(Triangle inequality)** $d(x,z)\le d(x,y)+d(y,z)$.

The triangle inequality is the workhorse: it is the formal statement that "a detour is never shorter than the direct route," and almost every estimate in this guide is a chain of triangle inequalities.

> **Definition — convergence and Cauchy sequence.** A sequence $(x_n)_{n\ge 1}$ in $X$ **converges to** $x\in X$ if for every $\varepsilon>0$ there is an $N$ such that $d(x_n,x)<\varepsilon$ for all $n\ge N$; we write $x_n\to x$. The sequence is **Cauchy** if for every $\varepsilon>0$ there is an $N$ such that $d(x_m,x_n)<\varepsilon$ for all $m,n\ge N$ (the terms eventually huddle together, *without naming a limit*).

> **Definition — completeness.** A metric space $X$ is **complete** if *every* Cauchy sequence in $X$ converges to a point of $X$.

The recalled fact we will use repeatedly, proved in the Analysis-foundations guide, is: **$\mathbb{R}$ (and hence $\mathbb{C}$ and $\mathbb{R}^n$) is complete.** This is the *completeness axiom* in action.

> **Lemma — every convergent sequence is Cauchy.** If $x_n\to x$ then $(x_n)$ is Cauchy.

**Proof.**
1. Let $\varepsilon>0$. Since $x_n\to x$, choose $N$ with $d(x_n,x)<\varepsilon/2$ for all $n\ge N$. *(definition of convergence, applied with the tolerance $\varepsilon/2$)*
2. For any $m,n\ge N$, the triangle inequality gives $d(x_m,x_n)\le d(x_m,x)+d(x,x_n)<\varepsilon/2+\varepsilon/2=\varepsilon$. *(metric axiom 3, then the bound from step 1 for both terms)*
3. Thus the Cauchy condition holds for this $\varepsilon$; as $\varepsilon$ was arbitrary, $(x_n)$ is Cauchy. $\blacksquare$

The converse — Cauchy implies convergent — is *precisely* completeness and can fail. Here is the canonical failure, the one that motivates everything.

**Worked example — an incomplete space.** Let $X=\mathbb{Q}$ with $d(x,y)=|x-y|$. Define $x_1=1$, $x_2=1.4$, $x_3=1.41$, $x_4=1.414,\dots$, the decimal truncations of $\sqrt 2$. Then $|x_m-x_n|\le 10^{-\min(m,n)+1}\to 0$, so $(x_n)$ is Cauchy. But its only possible limit is $\sqrt2\notin\mathbb{Q}$, so it does **not** converge in $X$. The space $\mathbb{Q}$ has "holes." Completing it — filling the holes — gives $\mathbb{R}$.

> **Definition — completion (statement).** Every metric space $X$ has a **completion** $\widehat{X}$: a complete metric space containing (an isometric copy of) $X$ as a dense subset, unique up to distance-preserving bijection. *(Construction: take equivalence classes of Cauchy sequences in $X$, with two declared equal when their termwise distance tends to $0$; this is exactly how $\mathbb{R}$ is built from $\mathbb{Q}$.)* We will invoke this when we promote nice function spaces to complete ones.

> **Definition — open, closed, dense.** A set $U\subseteq X$ is **open** if around every point of $U$ there is a small ball $B(x,r)=\{y:d(x,y)<r\}$ entirely inside $U$. A set is **closed** if its complement is open; equivalently, $C$ is closed iff every convergent sequence with terms in $C$ has its limit in $C$. A set $D$ is **dense** in $X$ if every point of $X$ is a limit of points of $D$ (the rationals are dense in the reals).

> **Pitfall.** "Cauchy" and "convergent" are *not* synonyms; they coincide only in complete spaces. A sequence can crowd together forever and still have no destination *inside the space*. This is not pedantry: in quantum mechanics one constantly builds a wavefunction as a limit of approximations, and that limit only exists because $L^2$ is complete.

> **Lemma — a closed subset of a complete space is complete.** If $X$ is complete and $C\subseteq X$ is closed, then $C$ (with the same metric) is complete.

**Proof.**
1. Let $(x_n)$ be Cauchy in $C$. It is then Cauchy in $X$, which is complete, so $x_n\to x$ for some $x\in X$. *(completeness of the ambient space)*
2. Each $x_n\in C$ and $C$ is closed, so the limit $x\in C$ (the sequential characterization of closedness). Thus the Cauchy sequence converges *inside* $C$. $\blacksquare$

This little lemma is used constantly: to prove a concrete space complete we often realize it as a closed subset of one already known to be complete. It also explains why "closed subspace" — not just "subspace" — is the right hypothesis throughout the operator theory ahead.

**Worked example — why completeness is the engine of existence theorems.** The **Banach fixed-point theorem** says: in a complete metric space, a **contraction** $f$ (one with $d(f(x),f(y))\le q\,d(x,y)$ for a fixed $q<1$) has a unique fixed point, found as the limit of the iterates $x,f(x),f(f(x)),\dots$. The reason the limit *exists* is exactly completeness: the iterates form a Cauchy sequence (their gaps shrink geometrically like $q^n$), and only a complete space guarantees that Cauchy sequence a destination. This single theorem powers the existence-and-uniqueness proof for differential equations — so the abstract word "complete" is what makes "the solution exists" a theorem rather than a hope. We will see the same pattern (Cauchy partial sums $\Rightarrow$ a limit exists) drive the Fourier expansion in §s4 and the Neumann series in §s8.

<a id="s2"></a>
### Normed vector spaces and Banach spaces

**What and why.** A metric gives distance but no algebra; a vector space gives algebra but no distance. We want both, compatibly. A **norm** measures the length of a vector, and "distance" becomes "length of the difference." When such a space is complete, we call it a **Banach space**, after Stefan Banach — these are the spaces in which infinite sums and limits of vectors are guaranteed to make sense.

> **Definition — normed vector space.** Let $V$ be a vector space over $\mathbb{F}$ ($=\mathbb{R}$ or $\mathbb{C}$). A **norm** is a function $\|\cdot\|:V\to\mathbb{R}$ such that for all $u,v\in V$ and $\lambda\in\mathbb{F}$:
> 1. **(Non-negativity & definiteness)** $\|v\|\ge 0$, and $\|v\|=0$ iff $v=0$;
> 2. **(Absolute homogeneity)** $\|\lambda v\|=|\lambda|\,\|v\|$;
> 3. **(Triangle inequality)** $\|u+v\|\le \|u\|+\|v\|$.
>
> The pair $(V,\|\cdot\|)$ is a **normed vector space**.

> **Lemma — a norm induces a metric.** Setting $d(u,v):=\|u-v\|$ makes $(V,d)$ a metric space.

**Proof.**
1. $d(u,v)=\|u-v\|\ge 0$, and equals $0$ iff $u-v=0$, i.e. $u=v$ (norm axiom 1). *(identity of indiscernibles)*
2. $d(u,v)=\|u-v\|=\|(-1)(v-u)\|=|-1|\,\|v-u\|=\|v-u\|=d(v,u)$ (norm axiom 2 with $\lambda=-1$). *(symmetry)*
3. $d(u,w)=\|u-w\|=\|(u-v)+(v-w)\|\le\|u-v\|+\|v-w\|=d(u,v)+d(v,w)$ (norm axiom 3). *(triangle inequality)* $\blacksquare$

> **Definition — Banach space.** A **Banach space** is a normed vector space that is **complete** in the induced metric: every Cauchy sequence of vectors converges to a vector in the space.

**Worked examples of norms.**

- **Euclidean $\mathbb{R}^n$:** $\|x\|_2=\big(\sum_{i=1}^n x_i^2\big)^{1/2}$. Complete, hence Banach. The familiar length.
- **The sequence spaces $\ell^p$** ($1\le p<\infty$): vectors are infinite sequences $x=(x_1,x_2,\dots)$ of scalars with
$$
\|x\|_p=\Big(\sum_{k=1}^\infty |x_k|^p\Big)^{1/p}<\infty.
$$
For $p=\infty$, $\ell^\infty$ consists of **bounded** sequences with $\|x\|_\infty=\sup_k|x_k|$. Each $\ell^p$ is a Banach space.
- **The Lebesgue spaces $L^p[a,b]$** ($1\le p<\infty$): (equivalence classes of) measurable functions $f$ with
$$
\|f\|_p=\Big(\int_a^b |f(x)|^p\,dx\Big)^{1/p}<\infty,
$$
two functions identified when they differ only on a set of measure zero. Each $L^p$ is Banach (the Riesz–Fischer theorem). We treat the measure-theoretic underpinning as a black box from analysis; the *one* fact we need is that $L^p$ is complete.
- **Continuous functions $C[a,b]$** with the **supremum norm** $\|f\|_\infty=\sup_{x\in[a,b]}|f(x)|$. This is Banach: a uniformly Cauchy sequence of continuous functions converges uniformly to a continuous limit (a theorem from the Analysis-foundations guide).

That the $\ell^p$ and $L^p$ formulas are genuine *norms* rests on one inequality worth stating, since we use its $p=2$ case constantly.

> **Theorem — Minkowski's inequality (the triangle inequality for $\|\cdot\|_p$).** For $1\le p<\infty$ and $x,y\in\ell^p$, $\ \|x+y\|_p\le\|x\|_p+\|y\|_p$.

For $p=2$ this is the Cauchy–Schwarz corollary we prove in §s3; for general $p$ it follows from **Hölder's inequality** $\sum|x_k y_k|\le\|x\|_p\|y\|_q$ (with $\tfrac1p+\tfrac1q=1$). We will only need $p=2$ in detail, so we record the general statement and prove the $p=2$ case where it is cleanest. The other two norm axioms (definiteness and homogeneity) are immediate from the corresponding properties of $|\cdot|$.

To make "$L^p$ is complete" concrete, here is the completeness proof in the cleanest model, $\ell^2$ — the same three-move pattern (a Cauchy sequence forces coordinatewise limits, assemble them, check the assembled vector is the limit *in norm*) recurs for every $L^p$.

> **Theorem — $\ell^2$ is complete.** Every Cauchy sequence in $\ell^2$ converges in $\ell^2$.

**Proof.**
1. Let $(x^{(n)})_n$ be Cauchy in $\ell^2$, where $x^{(n)}=(x^{(n)}_1,x^{(n)}_2,\dots)$. For each fixed coordinate $k$, $|x^{(m)}_k-x^{(n)}_k|\le\|x^{(m)}-x^{(n)}\|_2\to0$, so the scalar sequence $(x^{(n)}_k)_n$ is Cauchy in $\mathbb{C}$, which is complete; let $x_k:=\lim_n x^{(n)}_k$. *(coordinatewise limits exist by completeness of $\mathbb{C}$)*
2. **The candidate limit $x=(x_k)$ lies in $\ell^2$.** Given $\varepsilon>0$ choose $N$ with $\|x^{(m)}-x^{(n)}\|_2<\varepsilon$ for $m,n\ge N$. For any finite $K$, $\sum_{k=1}^K|x^{(m)}_k-x^{(n)}_k|^2<\varepsilon^2$; let $m\to\infty$ (finite sum, so limits pass inside) to get $\sum_{k=1}^K|x_k-x^{(n)}_k|^2\le\varepsilon^2$. *(pass to the coordinatewise limit in a finite sum)*
3. Let $K\to\infty$: $\sum_{k=1}^\infty|x_k-x^{(n)}_k|^2\le\varepsilon^2$, i.e. $x-x^{(n)}\in\ell^2$ with $\|x-x^{(n)}\|_2\le\varepsilon$. Then $x=(x-x^{(n)})+x^{(n)}\in\ell^2$ (sum of two $\ell^2$ vectors). *(monotone limit of partial sums)*
4. The same bound $\|x-x^{(n)}\|_2\le\varepsilon$ for all $n\ge N$ says exactly $x^{(n)}\to x$ in $\ell^2$. $\blacksquare$

**Worked example — a normed space that is NOT complete.** Take $C[0,1]$ but with the $L^1$-norm $\|f\|_1=\int_0^1|f|$ instead of the sup-norm. Let $f_n$ be the continuous "ramp" equal to $0$ on $[0,\tfrac12]$, equal to $1$ on $[\tfrac12+\tfrac1n,1]$, and linear in between. For $m>n$, $\|f_m-f_n\|_1\le\tfrac1n\to0$, so $(f_n)$ is Cauchy. Its pointwise limit is the discontinuous step $\mathbf 1_{(1/2,1]}$, which is **not** in $C[0,1]$, and no continuous function is its $L^1$-limit. So $(C[0,1],\|\cdot\|_1)$ is incomplete; its completion is exactly $L^1[0,1]$. This is *why* Lebesgue's $L^p$ spaces — not the continuous functions — are the right setting: completeness demands them.

> **Theorem — equivalence of norms in finite dimensions.** On a finite-dimensional vector space $V$ (over $\mathbb{R}$ or $\mathbb{C}$), any two norms $\|\cdot\|_a$ and $\|\cdot\|_b$ are **equivalent**: there are constants $0<c\le C$ with
>
> $$
> c\,\|v\|_a\le \|v\|_b\le C\,\|v\|_a\qquad\text{for all }v\in V.
> $$

**Proof.**
1. Equivalence of norms is an equivalence relation (reflexive, symmetric by inverting constants, transitive by multiplying constants), so it suffices to show every norm $\|\cdot\|$ is equivalent to one fixed reference norm. Fix a basis $e_1,\dots,e_n$ and let $\|\cdot\|_a$ be the **Euclidean norm of the coordinates**: $\|v\|_a=(\sum_i|\alpha_i|^2)^{1/2}$ where $v=\sum_i\alpha_i e_i$. *(reduce to a single comparison)*
2. **Upper bound.** For $v=\sum_i\alpha_i e_i$, the triangle inequality and homogeneity give $\|v\|\le\sum_i|\alpha_i|\,\|e_i\|$. By the Cauchy–Schwarz inequality for the finite sum, $\sum_i|\alpha_i|\,\|e_i\|\le\big(\sum_i|\alpha_i|^2\big)^{1/2}\big(\sum_i\|e_i\|^2\big)^{1/2}=C\,\|v\|_a$ with $C=(\sum_i\|e_i\|^2)^{1/2}$. So $\|v\|\le C\|v\|_a$. *(norm axioms 2,3 then Cauchy–Schwarz)*
3. **The map $v\mapsto\|v\|$ is continuous in the $\|\cdot\|_a$-topology.** By the reverse triangle inequality $\big|\,\|u\|-\|v\|\,\big|\le\|u-v\|\le C\|u-v\|_a$, so small change in coordinates means small change in $\|\cdot\|$. *(reverse triangle inequality, then step 2)*
4. **Lower bound.** The **unit sphere** $S=\{v:\|v\|_a=1\}$ is closed and bounded in coordinates, hence **compact** (Heine–Borel in $\mathbb{F}^n$, from the Analysis-foundations guide). A continuous real function on a compact set attains its minimum (extreme value theorem). So $m:=\min_{v\in S}\|v\|$ is attained at some $v_0\in S$. Since $\|v_0\|_a=1\ne 0$, $v_0\ne 0$, so $\|v_0\|>0$ (norm axiom 1); thus $m>0$. *(compactness + extreme value theorem + definiteness)*
5. For any $v\ne 0$, $v/\|v\|_a\in S$, so $\|v/\|v\|_a\|\ge m$, i.e. $\|v\|\ge m\|v\|_a$. Take $c=m$. Combining with step 2, $c\|v\|_a\le\|v\|\le C\|v\|_a$. $\blacksquare$

> **Why this matters — and why it fails in infinite dimensions.** In finite dimensions all norms give the same convergent sequences, so "the topology" is unambiguous; this is why finite-dimensional quantum systems (qubits) never worry about which norm to use. In infinite dimensions equivalence fails dramatically: a sequence can converge in $L^2$ but not in $L^\infty$. Choosing the right norm becomes a real modeling decision, and the unit ball is no longer compact (a fact we will need for compact operators in §s9).

**Worked example — inequivalence.** On $C[0,1]$, let $f_n(x)=x^n$. Then $\|f_n\|_2=(\int_0^1 x^{2n}dx)^{1/2}=(2n+1)^{-1/2}\to 0$, yet $\|f_n\|_\infty=\sup_{[0,1]}x^n=1$ for all $n$. So $f_n\to 0$ in the $2$-norm but not in the sup-norm; no constants $c,C$ can relate the two norms. Infinite dimensions genuinely differ.

<a id="s3"></a>
### Inner product spaces and Hilbert spaces; the parallelogram law

**What and why.** A norm gives length but not *angle*. To do geometry — orthogonality, projection, Fourier analysis — we need an **inner product**, the infinite-dimensional descendant of the dot product. A complete inner product space is a **Hilbert space**, and it is the exact mathematical home of quantum states.

> **Definition — inner product (complex case).** An **inner product** on a complex vector space $H$ is a map $\langle\cdot,\cdot\rangle:H\times H\to\mathbb{C}$ such that for all $x,y,z\in H$ and $\lambda\in\mathbb{C}$:
> 1. **(Conjugate symmetry)** $\langle x,y\rangle=\overline{\langle y,x\rangle}$;
> 2. **(Linearity in the second slot)** $\langle x,\lambda y+z\rangle=\lambda\langle x,y\rangle+\langle x,z\rangle$;
> 3. **(Positive definiteness)** $\langle x,x\rangle\ge 0$, with equality iff $x=0$.
>
> (Physicists' convention: linear in the *right* argument, conjugate-linear in the left. Conjugate symmetry forces $\langle x,x\rangle=\overline{\langle x,x\rangle}$, so $\langle x,x\rangle$ is real, making axiom 3 meaningful.) The induced **norm** is $\|x\|:=\sqrt{\langle x,x\rangle}$.

> **Theorem — Cauchy–Schwarz inequality.** For all $x,y\in H$,
>
> $$
> |\langle x,y\rangle|\le \|x\|\,\|y\|.
> $$

**Proof.**
1. If $y=0$ both sides are $0$ (use $\langle x,0\rangle=0$, which follows from linearity: $\langle x,0\rangle=\langle x,0+0\rangle=2\langle x,0\rangle$). Assume $y\ne 0$. *(dispose of the trivial case)*
2. For any $\lambda\in\mathbb{C}$, positive definiteness gives $0\le\langle x-\lambda y,\,x-\lambda y\rangle$. Expand using axioms 1 and 2:
$$
0\le \|x\|^2-\overline{\lambda}\langle y,x\rangle-\lambda\langle x,y\rangle+|\lambda|^2\|y\|^2.
$$
*(bilinear/sesquilinear expansion)*
3. Choose $\lambda=\langle y,x\rangle/\|y\|^2$ (allowed since $\|y\|^2\ne 0$). Using $\langle x,y\rangle=\overline{\langle y,x\rangle}$, the two middle terms each equal $|\langle y,x\rangle|^2/\|y\|^2$ and the last equals the same; the inequality collapses to
$$
0\le \|x\|^2-\frac{|\langle y,x\rangle|^2}{\|y\|^2}.
$$
*(substitute the optimal $\lambda$ — the value that minimizes the quadratic)*
4. Rearranging, $|\langle y,x\rangle|^2\le\|x\|^2\|y\|^2$; take square roots and use $|\langle x,y\rangle|=|\langle y,x\rangle|$. $\blacksquare$

> **Corollary — the norm axioms hold.** Cauchy–Schwarz gives the triangle inequality: $\|x+y\|^2=\|x\|^2+2\,\mathrm{Re}\langle x,y\rangle+\|y\|^2\le\|x\|^2+2\|x\|\|y\|+\|y\|^2=(\|x\|+\|y\|)^2$. So $\|\cdot\|=\sqrt{\langle\cdot,\cdot\rangle}$ is genuinely a norm. *(used $\mathrm{Re}\,z\le|z|$ then Cauchy–Schwarz)*

> **Definition — Hilbert space.** A **Hilbert space** is an inner product space that is **complete** in the induced norm. (Every Hilbert space is in particular a Banach space whose norm comes from an inner product.)

**Worked examples.**

- **$\ell^2$:** square-summable sequences with $\langle x,y\rangle=\sum_k\overline{x_k}\,y_k$. Complete — the prototype *separable* infinite-dimensional Hilbert space. (The sum defining $\langle x,y\rangle$ converges absolutely by Cauchy–Schwarz applied to the partial sums, so the inner product is well-defined.)
- **$L^2[a,b]$:** square-integrable functions with $\langle f,g\rangle=\int_a^b \overline{f(x)}\,g(x)\,dx$. The home of wavefunctions on an interval; $L^2(\mathbb{R})$ on the whole line.

> **Definition — orthogonality and the Pythagorean theorem.** Two vectors are **orthogonal**, written $x\perp y$, if $\langle x,y\rangle=0$. If $x\perp y$ then $\|x+y\|^2=\|x\|^2+\langle x,y\rangle+\langle y,x\rangle+\|y\|^2=\|x\|^2+\|y\|^2$ — the **Pythagorean theorem**, valid in any inner product space and used in every projection argument below.

**Worked example — Cauchy–Schwarz with real numbers in $L^2$.** Take $f(x)=x$ and $g(x)=1$ on $[0,1]$. Then $\langle f,g\rangle=\int_0^1 x\,dx=\tfrac12$, $\|f\|_2=(\int_0^1 x^2)^{1/2}=\tfrac1{\sqrt3}$, $\|g\|_2=1$. Cauchy–Schwarz predicts $\tfrac12\le\tfrac1{\sqrt3}\cdot1\approx0.577$ — true, and *not* an equality because $f$ and $g$ are not parallel (one is not a scalar multiple of the other). Equality in Cauchy–Schwarz holds exactly when one vector is a scalar multiple of the other, which is why $|\langle x,y\rangle|=\|x\|\|y\|$ is the rigorous meaning of "perfectly aligned."

**Worked example — orthogonalization (Gram–Schmidt) in $L^2[-1,1]$.** Start from $1,x,x^2,\dots$ and orthogonalize using $\langle f,g\rangle=\int_{-1}^1 fg$. The first vector is $p_0=1$ (norm $\sqrt2$). For $p_1$, subtract the component along $p_0$: $\langle 1,x\rangle=\int_{-1}^1 x\,dx=0$, so $x$ is already orthogonal to $1$; $p_1=x$. For $p_2$, $\langle 1,x^2\rangle=\int_{-1}^1 x^2=\tfrac23$ and $\langle x,x^2\rangle=\int_{-1}^1 x^3=0$, so $p_2=x^2-\tfrac{2/3}{2}\cdot 1=x^2-\tfrac13$. These are (unnormalized) **Legendre polynomials**, an orthogonal family that reappears as the angular wavefunctions of the hydrogen atom — Gram–Schmidt in $L^2$ literally manufactures the special functions of physics.

> **Theorem — parallelogram law.** In any inner product space,
>
> $$
> \|x+y\|^2+\|x-y\|^2=2\|x\|^2+2\|y\|^2.
> $$

**Proof.**
1. Expand each squared norm by sesquilinearity: $\|x+y\|^2=\|x\|^2+\langle x,y\rangle+\langle y,x\rangle+\|y\|^2$ and $\|x-y\|^2=\|x\|^2-\langle x,y\rangle-\langle y,x\rangle+\|y\|^2$. *(definition $\|v\|^2=\langle v,v\rangle$, expanded)*
2. Add the two: the cross terms $\pm(\langle x,y\rangle+\langle y,x\rangle)$ cancel, leaving $2\|x\|^2+2\|y\|^2$. $\blacksquare$

> **Why the parallelogram law matters.** It is the *exact* fingerprint of an inner-product norm: a norm comes from an inner product **iff** it satisfies the parallelogram law (the inner product is then recovered by the **polarization identity** $\langle x,y\rangle=\tfrac14\sum_{k=0}^3 i^k\|x+i^k y\|^2$). This lets us test a Banach space for "secret geometry."

**Worked example — a Banach space that is not Hilbert.** Take $C[0,1]$ with the sup-norm, $f(x)=1$ and $g(x)=x$. Then $\|f\|_\infty=1$, $\|g\|_\infty=1$, $\|f+g\|_\infty=2$, $\|f-g\|_\infty=1$. The parallelogram law would require $4+1=2+2$, i.e. $5=4$ — false. So the sup-norm on $C[0,1]$ admits **no** inner product; this space has length but no angles.

<a id="s4"></a>
### Orthonormal bases in Hilbert space; Bessel, Parseval, Fourier expansion

**What and why.** In $\mathbb{C}^n$ an orthonormal basis lets us write every vector as a finite sum of its components along the basis directions. In a Hilbert space we want the same — but now the sum is *infinite*, and we must prove it converges. This is the mathematics underneath Fourier series and the expansion of a quantum state in energy eigenstates.

> **Definition — orthonormal system.** A family $\{e_k\}_{k\in K}$ in a Hilbert space $H$ is **orthonormal** if $\langle e_j,e_k\rangle=\delta_{jk}$ (the **Kronecker delta**: $1$ if $j=k$, else $0$). It is an **orthonormal basis** (ONB) if additionally its closed linear span is all of $H$ — equivalently (we will prove this) every $x\in H$ equals $\sum_k\langle e_k,x\rangle e_k$.

The numbers $\hat{x}_k:=\langle e_k,x\rangle$ are the **Fourier coefficients** of $x$.

> **Theorem — Bessel's inequality.** For any orthonormal system $\{e_k\}$ and any $x\in H$,
>
> $$
> \sum_k |\langle e_k,x\rangle|^2\le \|x\|^2.
> $$

**Proof.** (Finite case first; the infinite case follows by taking a supremum.)
1. Let $S_n=\sum_{k=1}^n\langle e_k,x\rangle e_k$ be the partial sum (the projection of $x$ onto $\mathrm{span}(e_1,\dots,e_n)$). Consider $\|x-S_n\|^2\ge 0$ (positive definiteness). *(set up the non-negative remainder)*
2. Expand: $\|x-S_n\|^2=\langle x-S_n,x-S_n\rangle=\|x\|^2-\langle x,S_n\rangle-\langle S_n,x\rangle+\|S_n\|^2$. *(sesquilinear expansion)*
3. Compute each piece using orthonormality. $\langle S_n,x\rangle=\sum_k\overline{\langle e_k,x\rangle}\langle e_k,x\rangle=\sum_k|\langle e_k,x\rangle|^2$. By conjugate symmetry $\langle x,S_n\rangle$ equals the same real sum. And $\|S_n\|^2=\sum_{j,k}\overline{\langle e_j,x\rangle}\langle e_k,x\rangle\langle e_j,e_k\rangle=\sum_k|\langle e_k,x\rangle|^2$ (off-diagonal terms vanish since $\langle e_j,e_k\rangle=\delta_{jk}$). *(orthonormality kills cross terms)*
4. Substitute: $0\le\|x-S_n\|^2=\|x\|^2-2\sum_k|\langle e_k,x\rangle|^2+\sum_k|\langle e_k,x\rangle|^2=\|x\|^2-\sum_{k=1}^n|\langle e_k,x\rangle|^2$. *(arithmetic)*
5. Hence $\sum_{k=1}^n|\langle e_k,x\rangle|^2\le\|x\|^2$ for every $n$. The partial sums are bounded above by $\|x\|^2$ and increasing, so the series converges and $\sum_k|\langle e_k,x\rangle|^2\le\|x\|^2$. $\blacksquare$

> **Theorem — Fourier expansion converges, and Parseval.** Let $\{e_k\}_{k\ge 1}$ be an orthonormal basis of $H$ (closed span $=H$). Then for every $x\in H$:
>
> $$
> x=\sum_{k=1}^\infty \langle e_k,x\rangle\,e_k,\qquad \|x\|^2=\sum_{k=1}^\infty|\langle e_k,x\rangle|^2\ \ (\textbf{Parseval}).
> $$

**Proof.**
1. **The series converges in $H$.** Let $S_n=\sum_{k=1}^n\langle e_k,x\rangle e_k$. For $m>n$, $\|S_m-S_n\|^2=\sum_{k=n+1}^m|\langle e_k,x\rangle|^2$ (orthonormality, as in the Bessel computation). By Bessel the full series $\sum_k|\langle e_k,x\rangle|^2$ converges, so its tail $\to 0$; hence $(S_n)$ is **Cauchy** in $H$. Since $H$ is complete, $S_n\to s$ for some $s\in H$. *(completeness is used here — this step fails in an incomplete space)*
2. **The limit is $x$.** Compute $\langle e_j,\,x-s\rangle=\langle e_j,x\rangle-\langle e_j,s\rangle$. Inner product is continuous (Cauchy–Schwarz: $|\langle e_j,S_n\rangle-\langle e_j,s\rangle|\le\|e_j\|\|S_n-s\|\to 0$), so $\langle e_j,s\rangle=\lim_n\langle e_j,S_n\rangle=\langle e_j,x\rangle$ (for $n\ge j$ only the $k=j$ term survives). Thus $\langle e_j,x-s\rangle=0$ for all $j$. *(continuity of the inner product)*
3. So $x-s$ is orthogonal to every $e_j$, hence to their span, hence (by continuity) to the **closed** span, which is all of $H$. In particular $x-s\perp(x-s)$, giving $\|x-s\|^2=0$, so $x=s$ (definiteness). This is where "basis" (closed span $=H$) is essential. *(used that the ONB is total)*
4. **Parseval.** From step 4 of Bessel's proof, $\|x-S_n\|^2=\|x\|^2-\sum_{k=1}^n|\langle e_k,x\rangle|^2$. Since $S_n\to x$, the left side $\to 0$, so $\sum_{k=1}^\infty|\langle e_k,x\rangle|^2=\|x\|^2$. $\blacksquare$

**Worked example — Fourier series.** In $L^2[-\pi,\pi]$ the functions $e_k(x)=\frac{1}{\sqrt{2\pi}}e^{ikx}$, $k\in\mathbb{Z}$, are orthonormal: $\langle e_j,e_k\rangle=\frac{1}{2\pi}\int_{-\pi}^\pi e^{i(k-j)x}dx=\delta_{jk}$. They form an ONB, so every $f\in L^2[-\pi,\pi]$ has $f=\sum_k c_k e_k$ with $c_k=\langle e_k,f\rangle=\frac{1}{\sqrt{2\pi}}\int_{-\pi}^\pi e^{-ikx}f(x)dx$, and Parseval reads $\int_{-\pi}^\pi|f|^2=\sum_k|c_k|^2$. Take $f(x)=x$. Then $c_k=\frac{1}{\sqrt{2\pi}}\int_{-\pi}^\pi xe^{-ikx}dx=\frac{(-1)^k\, i\sqrt{2\pi}}{k}$ for $k\ne 0$ and $c_0=0$, so $|c_k|^2=2\pi/k^2$. Parseval gives $\int_{-\pi}^\pi x^2\,dx=\tfrac{2\pi^3}{3}=\sum_{k\ne 0}2\pi/k^2=2\pi\cdot 2\sum_{k\ge1}1/k^2$, which yields the celebrated $\sum_{k\ge1}1/k^2=\pi^2/6$. Geometry of $L^2$ computes a number.

> **Quantum reading.** Expanding a state $|\psi\rangle=\sum_k c_k|e_k\rangle$ in an orthonormal eigenbasis is exactly this Fourier expansion; $|c_k|^2$ are the **Born-rule probabilities**, and Parseval $\sum_k|c_k|^2=\|\psi\|^2=1$ is the statement that probabilities sum to one.

> **Definition — separable, and existence of an ONB.** A Hilbert space is **separable** if it has a countable dense subset; equivalently, it has a countable orthonormal basis (obtained by applying Gram–Schmidt to a countable dense set). All the Hilbert spaces of ordinary quantum mechanics — $\ell^2$, $L^2(\mathbb{R})$, $L^2[a,b]$ — are separable. We assume separability throughout, which is why we may always index the ONB by $k=1,2,3,\dots$.

**Worked example — the standard basis of $\ell^2$.** The vectors $e_k=(0,\dots,0,1,0,\dots)$ (a single $1$ in slot $k$) are orthonormal, and their closed span is all of $\ell^2$: given $x=(x_1,x_2,\dots)\in\ell^2$, the partial sums $\sum_{k=1}^n x_k e_k$ converge to $x$ because the tail $\sum_{k>n}|x_k|^2\to0$ (the series $\sum|x_k|^2$ converges). The Fourier coefficients are simply $\langle e_k,x\rangle=x_k$, and Parseval reads $\sum_k|x_k|^2=\|x\|_2^2$ — true by definition of the norm. So abstract Fourier expansion, in $\ell^2$, is just "a vector is the list of its components," now justified as a convergent infinite sum.

> **Pitfall — "basis" means closed span, not algebraic span.** In a finite-dimensional space a basis spans *by finite combinations*. In a Hilbert space the standard $\{e_k\}$ of $\ell^2$ do **not** span by finite combinations (no finite combination equals $(1,\tfrac12,\tfrac13,\dots)$); they span only after taking the closure, i.e. allowing convergent infinite sums. Confusing the two notions of "span" is the most common infinite-dimensional error.

---

## Part B — Operators and duality

<a id="s5"></a>
### The Riesz representation theorem; the dual space; bra–ket made rigorous

**What and why.** A **linear functional** assigns a number to each vector linearly — it is a "measuring device." The collection of continuous functionals is the **dual space**, and the Riesz theorem says that in a Hilbert space every such functional is secretly "take the inner product with a fixed vector." This is what makes Dirac's bra $\langle\phi|$ a genuine, rigorous object.

> **Definition — bounded linear functional & dual space.** A **linear functional** on $H$ is a linear map $f:H\to\mathbb{F}$. It is **bounded** if there is $C\ge 0$ with $|f(x)|\le C\|x\|$ for all $x$; the smallest such $C$ is $\|f\|:=\sup_{\|x\|=1}|f(x)|$. The set of bounded linear functionals, with this norm, is the **(continuous) dual space** $H^*$. (For linear maps, **bounded $=$ continuous**, proved in §s6.)

> **Lemma — orthogonal projection.** Let $M\subseteq H$ be a **closed** subspace. Every $x\in H$ has a unique decomposition $x=m+n$ with $m\in M$ and $n\in M^\perp:=\{n:\langle n,m'\rangle=0\ \forall m'\in M\}$. The vector $m=:P_M x$ is the **nearest point of $M$ to $x$**.

**Proof (key steps).**
1. Let $d=\inf_{m'\in M}\|x-m'\|$ and pick $m_n\in M$ with $\|x-m_n\|^2\to d^2$. *(approach the infimum)*
2. The parallelogram law applied to $a=x-m_i$, $b=x-m_j$ gives, after rearranging and using $\tfrac{m_i+m_j}{2}\in M$ (so $\|x-\tfrac{m_i+m_j}{2}\|\ge d$):
$$
\|m_i-m_j\|^2=2\|x-m_i\|^2+2\|x-m_j\|^2-4\big\|x-\tfrac{m_i+m_j}{2}\big\|^2\le 2\|x-m_i\|^2+2\|x-m_j\|^2-4d^2.
$$
As $i,j\to\infty$ the right side $\to 2d^2+2d^2-4d^2=0$, so $(m_n)$ is **Cauchy**; by completeness $m_n\to m\in M$ (closed). *(parallelogram law + completeness + closedness)*
3. By continuity $\|x-m\|=d$. Set $n=x-m$. For any $m'\in M$ and $t\in\mathbb{R}$, $d^2\le\|n-tm'\|^2=d^2-2t\,\mathrm{Re}\langle n,m'\rangle+t^2\|m'\|^2$; the coefficient of $t$ must vanish (else small $t$ beats $d^2$), giving $\mathrm{Re}\langle n,m'\rangle=0$; repeating with $im'$ gives the imaginary part, so $\langle n,m'\rangle=0$. Thus $n\in M^\perp$. *(first-order optimality)*
4. Uniqueness: if $m+n=m'+n'$ with $m,m'\in M$, $n,n'\in M^\perp$, then $m-m'=n'-n$ lies in $M\cap M^\perp=\{0\}$ (a vector orthogonal to itself is $0$). $\blacksquare$

> **Theorem — Riesz representation.** For every bounded linear functional $f\in H^*$ there is a **unique** vector $y_f\in H$ such that
>
> $$
> f(x)=\langle y_f,\,x\rangle\quad\text{for all }x\in H,\qquad\text{and}\qquad \|f\|=\|y_f\|.
> $$

**Proof.**
1. If $f=0$, take $y_f=0$. Otherwise the **kernel** $M=\ker f=\{x:f(x)=0\}$ is a closed (since $f$ is continuous) proper subspace, so $M^\perp\ne\{0\}$ by the projection lemma. Pick $z\in M^\perp$, $z\ne 0$. *(produce a direction orthogonal to the kernel)*
2. For any $x\in H$, the vector $u=f(x)\,z-f(z)\,x$ satisfies $f(u)=f(x)f(z)-f(z)f(x)=0$, so $u\in M$, hence $\langle z,u\rangle=0$. *(construct an element of the kernel)*
3. Expand $0=\langle z,u\rangle=f(x)\langle z,z\rangle-f(z)\langle z,x\rangle$, so $f(x)=\dfrac{f(z)}{\|z\|^2}\langle z,x\rangle=\langle y_f,x\rangle$ with $y_f=\dfrac{\overline{f(z)}}{\|z\|^2}z$. *(solve for $f(x)$; conjugate appears from conjugate-linearity of the left slot)*
4. **Uniqueness:** if $\langle y,x\rangle=\langle y',x\rangle$ for all $x$, take $x=y-y'$ to get $\|y-y'\|^2=0$, so $y=y'$. **Norm:** by Cauchy–Schwarz $|f(x)|=|\langle y_f,x\rangle|\le\|y_f\|\|x\|$ so $\|f\|\le\|y_f\|$; and $f(y_f/\|y_f\|)=\|y_f\|$ shows $\|f\|\ge\|y_f\|$. Hence $\|f\|=\|y_f\|$. $\blacksquare$

> **Bra–ket made rigorous.** Write a vector ("ket") as $|x\rangle\in H$. Riesz says each ket $|y\rangle$ defines a *unique* bounded functional ("bra") $\langle y|:=\langle y,\cdot\rangle$, and conversely. The pairing $\langle y|x\rangle$ is literally the inner product $\langle y,x\rangle$. So Dirac's notation is not mysticism: bras are the dual space, and the bra–ket bracket is the inner product. The map $|y\rangle\mapsto\langle y|$ is conjugate-linear and norm-preserving — an *antilinear isometry* $H\to H^*$.

**Worked example.** On $L^2[0,1]$, the "evaluate the average" functional $f(g)=\int_0^1 g(x)dx$ is bounded ($|f(g)|\le\|1\|_2\|g\|_2=\|g\|_2$ by Cauchy–Schwarz). Its Riesz vector is $y_f=\mathbf{1}$, the constant function $1$: indeed $\langle\mathbf 1,g\rangle=\int_0^1\overline{1}\,g=f(g)$, and $\|f\|=\|\mathbf 1\|_2=1$.

> **Pitfall — pointwise evaluation is NOT a bounded functional on $L^2$.** It is tempting to define "evaluate at $x_0$," $g\mapsto g(x_0)$, as a functional. But $L^2$ elements are equivalence classes defined only up to measure-zero changes, so $g(x_0)$ is not even well-defined, and there is no $y\in L^2$ with $\langle y,g\rangle=g(x_0)$ for all $g$. This is precisely the object that *forces* us into distributions (§s12): the would-be Riesz vector is the Dirac delta, which lives outside the Hilbert space. Riesz works for *bounded* functionals only; pointwise evaluation is unbounded, and its honest home is the rigging $\Phi'$.

> **Reflexivity, briefly.** Riesz shows $H\cong H^*$ (antilinearly), so applying it twice gives $H\cong H^{**}$ linearly: Hilbert spaces are **reflexive**. This self-duality is special — for general Banach spaces $X^{**}$ can be strictly larger than $X$ (e.g. $c_0\subsetneq\ell^\infty=(c_0)^{**}$). The clean self-duality of Hilbert space is one more reason quantum mechanics chooses it: bras and kets are mirror images of one another with nothing left over.

<a id="s6"></a>
### Bounded linear operators and the operator norm

**What and why.** Observables and time-evolution act on states, so we need linear *operators* $T:H\to H$ (or between two spaces). The crucial quantitative handle is the **operator norm**, which measures the largest stretch $T$ can inflict. Bounded operators form a Banach space — even an algebra — of their own.

> **Definition — bounded operator & operator norm.** A linear map $T:X\to Y$ between normed spaces is **bounded** if
>
> $$
> \|T\|:=\sup_{x\ne 0}\frac{\|Tx\|_Y}{\|x\|_X}=\sup_{\|x\|=1}\|Tx\|_Y<\infty.
> $$
>
> The number $\|T\|$ is the **operator norm**. Write $\mathcal{B}(X,Y)$ for the bounded operators, $\mathcal{B}(H)=\mathcal{B}(H,H)$.

> **Theorem — bounded $\Leftrightarrow$ continuous.** For a linear map $T$, the following are equivalent: (i) $T$ is bounded; (ii) $T$ is continuous everywhere; (iii) $T$ is continuous at $0$.

**Proof.**
1. **(i)$\Rightarrow$(ii):** If $\|Tx\|\le\|T\|\|x\|$, then $\|Tx-Tx_0\|=\|T(x-x_0)\|\le\|T\|\|x-x_0\|$, so $T$ is (Lipschitz, hence) continuous. *(linearity + the bound)*
2. **(ii)$\Rightarrow$(iii):** trivial (continuity everywhere includes at $0$).
3. **(iii)$\Rightarrow$(i):** Continuity at $0$ with $\varepsilon=1$ gives $\delta>0$ such that $\|x\|\le\delta\Rightarrow\|Tx\|\le 1$. For any $x\ne 0$, the vector $\delta x/\|x\|$ has norm $\delta$, so $\|T(\delta x/\|x\|)\|\le 1$, i.e. $\|Tx\|\le\tfrac{1}{\delta}\|x\|$. Thus $\|T\|\le 1/\delta<\infty$. $\blacksquare$

> **Theorem — $\mathcal{B}(X,Y)$ is a normed space, and is complete when $Y$ is.** The operator norm satisfies the norm axioms, and if $Y$ is a Banach space then $\mathcal{B}(X,Y)$ is a Banach space.

**Proof (completeness, the key part).**
1. The norm axioms follow from those of $\|\cdot\|_Y$ (e.g. triangle: $\|(S+T)x\|\le\|Sx\|+\|Tx\|\le(\|S\|+\|T\|)\|x\|$). *(pointwise estimates)*
2. Let $(T_n)$ be Cauchy in $\mathcal{B}(X,Y)$. For each fixed $x$, $\|T_n x-T_m x\|\le\|T_n-T_m\|\|x\|\to 0$, so $(T_n x)$ is Cauchy in $Y$; since $Y$ is complete it converges. Define $Tx:=\lim_n T_n x$. *(use completeness of the target)*
3. $T$ is linear (limits respect $+$ and scalar multiplication). It is bounded: Cauchy sequences are bounded, say $\|T_n\|\le M$, so $\|Tx\|=\lim\|T_n x\|\le M\|x\|$. *(pass the bound to the limit)*
4. $T_n\to T$ in operator norm: given $\varepsilon$, pick $N$ with $\|T_n-T_m\|<\varepsilon$ for $m,n\ge N$; let $m\to\infty$ in $\|(T_n-T_m)x\|<\varepsilon\|x\|$ to get $\|(T_n-T)x\|\le\varepsilon\|x\|$, so $\|T_n-T\|\le\varepsilon$. $\blacksquare$

> **The algebra structure.** Composition is **submultiplicative**: $\|ST\|\le\|S\|\|T\|$, because $\|STx\|\le\|S\|\|Tx\|\le\|S\|\|T\|\|x\|$. With $\|I\|=1$, $\mathcal{B}(H)$ is a **Banach algebra**. This submultiplicativity is what makes operator power series like $e^{T}=\sum T^n/n!$ converge.

**Worked example — a multiplication operator.** On $L^2[0,1]$ define $(Tf)(x)=x\,f(x)$. Then $\|Tf\|_2^2=\int_0^1 x^2|f|^2\le\int_0^1|f|^2=\|f\|_2^2$, so $\|T\|\le 1$. Taking $f$ concentrated near $x=1$ shows $\|T\|=1$. (This is a baby version of the position operator, here *bounded* because the interval is finite — on the whole line it becomes unbounded; see §s10.)

<a id="s7"></a>
### Adjoint operators; self-adjoint, unitary, projection operators

**What and why.** The **adjoint** $T^*$ is the operator that "moves to the other side of the inner product." Three special classes — **self-adjoint** ($T=T^*$, the observables), **unitary** ($U^*=U^{-1}$, the symmetries and time-evolutions), and **projections** ($P=P^*=P^2$, the measurements) — are the entire grammar of quantum mechanics.

> **Theorem & Definition — the adjoint exists and is unique.** For $T\in\mathcal{B}(H)$ there is a unique $T^*\in\mathcal{B}(H)$ with
>
> $$
> \langle T^*x,\,y\rangle=\langle x,\,Ty\rangle\qquad\text{for all }x,y\in H,\qquad \|T^*\|=\|T\|.
> $$

**Proof.**
1. Fix $x$. The map $y\mapsto\langle x,Ty\rangle$ is linear in $y$ and bounded ($|\langle x,Ty\rangle|\le\|x\|\|T\|\|y\|$ by Cauchy–Schwarz), so it is a functional in $H^*$. *(check it is a bounded functional)*
2. By **Riesz** there is a unique vector, call it $T^*x$, with $\langle T^*x,y\rangle=\langle x,Ty\rangle$ for all $y$. This defines a map $x\mapsto T^*x$. *(invoke §s5)*
3. $T^*$ is linear: $\langle T^*(\alpha x_1+x_2),y\rangle=\langle\alpha x_1+x_2,Ty\rangle=\overline\alpha\langle x_1,Ty\rangle+\langle x_2,Ty\rangle=\langle\alpha T^*x_1+T^*x_2,y\rangle$ for all $y$, so the two sides' Riesz vectors agree. *(conjugate-linearity of the left slot matches)*
4. Boundedness and norm equality: $\|T^*x\|^2=\langle T^*x,T^*x\rangle=\langle x,TT^*x\rangle\le\|x\|\|T\|\|T^*x\|$, giving $\|T^*x\|\le\|T\|\|x\|$, so $\|T^*\|\le\|T\|$. Symmetrically (since $T^{**}=T$) $\|T\|\le\|T^*\|$. $\blacksquare$

> **Basic identities.** $(S+T)^*=S^*+T^*$, $(\lambda T)^*=\overline\lambda\,T^*$, $(ST)^*=T^*S^*$ (note the order flip), $T^{**}=T$. Each follows by moving operators across the inner product and using uniqueness; e.g. $\langle(ST)^*x,y\rangle=\langle x,STy\rangle=\langle S^*x,Ty\rangle=\langle T^*S^*x,y\rangle$.

> **Definitions — the three special classes.**
> - $T$ is **self-adjoint** (Hermitian) if $T=T^*$, i.e. $\langle Tx,y\rangle=\langle x,Ty\rangle$ for all $x,y$.
> - $U$ is **unitary** if it is a bijection with $U^*=U^{-1}$ (equivalently $U^*U=UU^*=I$).
> - $P$ is an **orthogonal projection** if $P=P^*=P^2$.

> **Theorem — self-adjoint operators have real "expectation" and real eigenvalues.** If $T=T^*$ then $\langle x,Tx\rangle\in\mathbb{R}$ for all $x$, and every eigenvalue of $T$ is real.

**Proof.**
1. $\overline{\langle x,Tx\rangle}=\langle Tx,x\rangle$ (conjugate symmetry) $=\langle x,T^*x\rangle=\langle x,Tx\rangle$ (self-adjointness). A number equal to its own conjugate is real. *(conjugate symmetry + $T=T^*$)*
2. If $Tx=\lambda x$ with $x\ne 0$: $\lambda\|x\|^2=\langle x,Tx\rangle\in\mathbb{R}$ and $\|x\|^2>0$, so $\lambda\in\mathbb{R}$. $\blacksquare$

> **Theorem — the $C^*$ identity.** For every $T\in\mathcal{B}(H)$, $\ \|T^*T\|=\|T\|^2$.

**Proof.**
1. **One direction.** $\|T^*T\|\le\|T^*\|\|T\|=\|T\|^2$ by submultiplicativity (§s6) and $\|T^*\|=\|T\|$. *(submultiplicative + norm equality of the adjoint)*
2. **The other.** For $\|x\|\le1$, $\|Tx\|^2=\langle Tx,Tx\rangle=\langle x,T^*Tx\rangle\le\|x\|\,\|T^*Tx\|\le\|T^*T\|$ (Cauchy–Schwarz, then the operator bound). Taking the supremum over $\|x\|\le1$, $\|T\|^2\le\|T^*T\|$. Combining the two gives equality. $\blacksquare$

This innocuous-looking identity is the defining axiom of a **$C^*$-algebra**, the abstract algebraic skeleton of quantum theory; it rigidly links the algebraic operation $T\mapsto T^*$ to the metric quantity $\|T\|$, and it is the reason self-adjoint operators are so tightly controlled.

> **Theorem — unitary operators preserve the inner product (and vice versa).** $U$ is unitary $\Rightarrow$ $\langle Ux,Uy\rangle=\langle x,y\rangle$ for all $x,y$; in particular $\|Ux\|=\|x\|$.

**Proof.** $\langle Ux,Uy\rangle=\langle x,U^*Uy\rangle=\langle x,Iy\rangle=\langle x,y\rangle$, using the adjoint relation then $U^*U=I$. Setting $y=x$ gives $\|Ux\|^2=\|x\|^2$. $\blacksquare$

> **Theorem — eigenvectors of a self-adjoint operator for distinct eigenvalues are orthogonal.** If $Tx=\lambda x$, $Ty=\mu y$ with $\lambda\ne\mu$ (both real, by the earlier theorem), then $\langle x,y\rangle=0$.

**Proof.** $\lambda\langle x,y\rangle=\langle \lambda x,y\rangle=\langle Tx,y\rangle=\langle x,Ty\rangle=\langle x,\mu y\rangle=\mu\langle x,y\rangle$ (using $T=T^*$ in the middle and that $\lambda$ is real, so $\overline\lambda=\lambda$). Hence $(\lambda-\mu)\langle x,y\rangle=0$, and since $\lambda\ne\mu$, $\langle x,y\rangle=0$. $\blacksquare$ This is why the spectral theorem can promise an *orthonormal* eigenbasis: distinct measured values automatically give orthogonal (distinguishable) states.

> **Theorem — projections and orthogonal decomposition.** If $P=P^*=P^2$, then $H=\mathrm{ran}(P)\oplus\ker(P)$ orthogonally, and $P$ is the orthogonal projection onto $M=\mathrm{ran}(P)$.

**Proof (key steps).**
1. **Idempotence splits the space.** Any $x$ writes as $x=Px+(x-Px)$ with $Px\in\mathrm{ran}P$ and $P(x-Px)=Px-P^2x=Px-Px=0$, so $x-Px\in\ker P$. *(uses $P^2=P$)*
2. **The pieces are orthogonal.** For $m=Pa\in\mathrm{ran}P$ and $n\in\ker P$: $\langle m,n\rangle=\langle Pa,n\rangle=\langle a,P^*n\rangle=\langle a,Pn\rangle=\langle a,0\rangle=0$. *(uses $P=P^*$ then $n\in\ker P$)*
3. Hence the decomposition is the orthogonal one of the projection lemma (§s5), so $P=P_M$. $\blacksquare$

**Worked example.** On $\mathbb{C}^2$ with standard inner product, $P=\begin{psmallmatrix}1&0\\0&0\end{psmallmatrix}$ satisfies $P^*=P$ and $P^2=P$; it projects onto the first coordinate axis. The Pauli matrix $\sigma_x=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}$ is self-adjoint with eigenvalues $\pm 1$ (real, as guaranteed). And $U=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}$ (a $90^\circ$ rotation) is unitary: $U^*U=I$, and it preserves lengths.

---

## Part C — Spectra and the spectral theorem

<a id="s8"></a>
### The spectrum and the resolvent; generalizing eigenvalues

**What and why.** In $\mathbb{C}^n$, $\lambda$ is an eigenvalue iff $T-\lambda I$ fails to be invertible. In infinite dimensions invertibility can fail in *new* ways — the operator can be injective with non-closed or non-dense range — so "eigenvalue" splits into a richer notion: the **spectrum**.

> **Definition — resolvent set and spectrum.** For $T\in\mathcal{B}(H)$, the **resolvent set** is $\rho(T)=\{\lambda\in\mathbb{C}:\ T-\lambda I\text{ is bijective with bounded inverse}\}$, and $R(\lambda)=(T-\lambda I)^{-1}$ is the **resolvent**. The **spectrum** is the complement $\sigma(T)=\mathbb{C}\setminus\rho(T)$. It splits into three disjoint pieces:
> - **Point spectrum** $\sigma_p$: $T-\lambda I$ is **not injective** — there is an eigenvector. ($\lambda$ is a genuine eigenvalue.)
> - **Continuous spectrum** $\sigma_c$: $T-\lambda I$ is injective with **dense but not closed** range (so the inverse exists on a dense set but is unbounded).
> - **Residual spectrum** $\sigma_r$: $T-\lambda I$ is injective but its range is **not dense**.

> **Theorem — the spectrum is nonempty, compact, and bounded by $\|T\|$.** For $T\in\mathcal{B}(H)$ over $\mathbb{C}$: $\sigma(T)$ is a nonempty closed subset of $\{\lambda:|\lambda|\le\|T\|\}$.

**Proof (key steps).**
1. **Neumann series.** If $|\lambda|>\|T\|$, then $T-\lambda I=-\lambda(I-T/\lambda)$ and $\|T/\lambda\|<1$, so $(I-T/\lambda)^{-1}=\sum_{n\ge0}(T/\lambda)^n$ converges in $\mathcal{B}(H)$ (geometric series, submultiplicativity, completeness of $\mathcal{B}(H)$ from §s6). Hence $\lambda\in\rho(T)$, so $\sigma(T)\subseteq\{|\lambda|\le\|T\|\}$ — **bounded**. *(geometric series in a Banach algebra)*
2. **Closed.** $\rho(T)$ is open: if $\lambda_0\in\rho(T)$, the same Neumann-series argument shows all $\lambda$ near $\lambda_0$ are in $\rho(T)$ (invertibility is an open condition). So $\sigma(T)$, its complement, is closed; closed and bounded in $\mathbb{C}$ means **compact**. *(perturbation of invertible operators)*
3. **Nonempty.** The resolvent $\lambda\mapsto R(\lambda)$ is operator-valued **analytic** on $\rho(T)$ and $\to 0$ as $|\lambda|\to\infty$. If $\sigma(T)$ were empty, $R$ would be entire and bounded, hence $\equiv 0$ by Liouville's theorem (vector-valued version) — impossible since $R(\lambda)$ is invertible. So $\sigma(T)\ne\varnothing$. *(Liouville's theorem from complex analysis)* $\blacksquare$

**Worked examples.**

- **Point spectrum (matrix-like).** A self-adjoint compact operator (§s9) has spectrum consisting of eigenvalues plus possibly $0$.
- **Continuous spectrum.** On $L^2[0,1]$ the multiplication operator $(Mf)(x)=xf(x)$ has $\sigma(M)=[0,1]$, but **no eigenvalues**: $xf(x)=\lambda f(x)$ forces $f=0$ a.e. (since $x=\lambda$ only at one point). For $\lambda\in[0,1]$, $(M-\lambda I)$ is injective with dense, non-closed range — pure continuous spectrum. This is the model for the position operator's continuous spectrum.
- **Residual spectrum.** The unilateral shift $S(x_1,x_2,\dots)=(0,x_1,x_2,\dots)$ on $\ell^2$ has $0$ in its residual spectrum: $S$ is injective but $\mathrm{ran}\,S=\{y:y_1=0\}$ is not dense.

**Worked example — a resolvent computed explicitly.** Let $D=\mathrm{diag}(1,\tfrac12,\tfrac13,\dots)$ on $\ell^2$, i.e. $(Dx)_k=x_k/k$. This is self-adjoint and bounded ($\|D\|=1$). For $\lambda\notin\{1,\tfrac12,\tfrac13,\dots\}\cup\{0\}$ the resolvent is the diagonal operator $R(\lambda)x=\big(\tfrac{x_k}{1/k-\lambda}\big)_k$, bounded because $|1/k-\lambda|$ is bounded below. Each reciprocal $\tfrac1k$ is an eigenvalue (eigenvector $e_k$): point spectrum $\{1,\tfrac12,\tfrac13,\dots\}$. But $\lambda=0$ is also in $\sigma(D)$ even though it is **not** an eigenvalue ($Dx=0$ forces $x=0$): it is the limit of the eigenvalues, and $D$ is not boundedly invertible there because $1/k\to0$ makes $R(\lambda)$ blow up. So $\sigma(D)=\{0\}\cup\{1/k:k\ge1\}$ — eigenvalues accumulating at $0$, with $0$ itself in the continuous spectrum. This is exactly the spectral shape the compact self-adjoint theorem (§s9) predicts.

> **The resolvent identity.** For $\lambda,\mu\in\rho(T)$, $R(\lambda)-R(\mu)=(\lambda-\mu)R(\lambda)R(\mu)$ — proved by left-multiplying by $(T-\lambda I)$ and right-multiplying by $(T-\mu I)$ and simplifying. It is the algebraic backbone of the analyticity used in step 3 above and of perturbation theory in quantum mechanics (how energy levels shift when the Hamiltonian changes slightly).

> **Quantum reading.** The set of possible measured values of an observable is its spectrum, *not* merely its eigenvalues. Position and momentum have purely continuous spectra ($\mathbb{R}$); a particle in a box has discrete (point) spectrum. The spectrum is the rigorous "set of measurable outcomes."

<a id="s9"></a>
### Compact operators and the spectral theorem for compact self-adjoint operators

**What and why.** **Compact operators** are the infinite-dimensional operators that behave most like matrices — they are limits of finite-rank operators and their spectra are discrete (eigenvalues accumulating only at $0$). For compact *self-adjoint* operators we get a clean spectral theorem: a genuine orthonormal eigenbasis, exactly as in finite dimensions.

> **Definition — compact operator.** $T\in\mathcal{B}(H)$ is **compact** if it maps the unit ball to a set whose closure is compact — equivalently, every bounded sequence $(x_n)$ has a subsequence with $(Tx_n)$ convergent. Equivalently again, $T$ is a norm-limit of finite-rank operators.

The slogan: compact operators "almost" reduce infinite dimensions to finite ones. (Recall from §s2 that the unit ball is **not** compact in infinite dimensions; compact operators are precisely those that restore compactness on the image.)

> **Lemma — the identity is compact iff $H$ is finite-dimensional.** If $\dim H=\infty$, the identity $I$ is **not** compact.

**Proof.** Take an orthonormal sequence $(e_n)$ (exists since $\dim H=\infty$). It is bounded ($\|e_n\|=1$), but $\|Ie_n-Ie_m\|^2=\|e_n-e_m\|^2=\|e_n\|^2+\|e_m\|^2=2$ for $n\ne m$ (Pythagoras, orthonormality), so no subsequence of $(Ie_n)$ is Cauchy, hence none converges. So $I$ fails the compactness criterion. $\blacksquare$ This is the sharpest statement of "infinite dimensions are not compact," and it is why a *general* bounded operator (like $I$) has no discrete spectral theorem — only the compact ones do.

**Worked example — a compact diagonal operator.** The operator $D$ of §s8, $(Dx)_k=x_k/k$, is compact: it is the norm-limit of the finite-rank truncations $D_n x=(x_1,\tfrac{x_2}2,\dots,\tfrac{x_n}n,0,0,\dots)$, since $\|D-D_n\|=\sup_{k>n}\tfrac1k=\tfrac1{n+1}\to0$. By the spectral theorem its eigenvectors $e_k$ form an ONB, eigenvalues $1/k\to0$, and indeed $Dx=\sum_k\tfrac1k\langle e_k,x\rangle e_k$ — the abstract theorem, made completely explicit.

> **Theorem — spectral theorem (compact self-adjoint).** Let $T\in\mathcal{B}(H)$ be compact and self-adjoint, $H$ a separable Hilbert space. Then there is an orthonormal system of eigenvectors $\{e_k\}$ with real eigenvalues $\{\lambda_k\}$, $\lambda_k\to 0$, such that
>
> $$
> Tx=\sum_k \lambda_k\,\langle e_k,x\rangle\,e_k\qquad\text{for all }x\in H,
> $$
>
> and the $\{e_k\}$ together with an orthonormal basis of $\ker T$ form an ONB of $H$.

**Proof sketch — with all key steps.**
1. **There is a maximal-modulus eigenvalue.** Set $m:=\sup_{\|x\|=1}|\langle x,Tx\rangle|$; for self-adjoint $T$ the operator norm equals this numerical radius, $\|T\|=m$. *(Proof of $\|T\|=m$: clearly $m\le\|T\|$ by Cauchy–Schwarz. For the reverse, the polarization-type identity $\langle T(x+y),x+y\rangle-\langle T(x-y),x-y\rangle=4\,\mathrm{Re}\langle Tx,y\rangle$ — valid since $T=T^*$ makes the quadratic form real — bounds $4\,\mathrm{Re}\langle Tx,y\rangle\le m(\|x+y\|^2+\|x-y\|^2)=2m(\|x\|^2+\|y\|^2)$ by the parallelogram law; taking $\|x\|=\|y\|=1$ and choosing the phase of $y$ to make $\langle Tx,y\rangle$ real gives $\mathrm{Re}\langle Tx,y\rangle=|\langle Tx,y\rangle|\le m$, and supping over such $y$ gives $\|Tx\|\le m$, so $\|T\|\le m$.)* Take $x_n$ with $\langle x_n,Tx_n\rangle\to\lambda_1$, $|\lambda_1|=\|T\|$. *(reduce to a variational problem)*
2. **Compactness produces an eigenvector.** If $\lambda_1=0$ then $\|T\|=0$, so $T=0$; the eigenexpansion is the empty sum and $H=\ker T$, and we are done. Otherwise $\lambda_1\ne0$: compute $\|Tx_n-\lambda_1 x_n\|^2=\|Tx_n\|^2-2\lambda_1\langle x_n,Tx_n\rangle+\lambda_1^2\le 2\lambda_1^2-2\lambda_1\langle x_n,Tx_n\rangle\to 0$. By compactness pass to a subsequence with $Tx_n\to y$; then $\lambda_1 x_n\to y$ too, so $x_n\to e_1:=y/\lambda_1$, and $Te_1=\lambda_1 e_1$ with $\|e_1\|=1$. So $\lambda_1$ is a genuine eigenvalue. *(this is where compactness is essential — it converts a near-eigenvector into an exact one)*
3. **Induct on the orthogonal complement.** $T$ maps $\{e_1\}^\perp$ into itself (self-adjointness: if $x\perp e_1$ then $\langle e_1,Tx\rangle=\langle Te_1,x\rangle=\lambda_1\langle e_1,x\rangle=0$). The restriction $T|_{\{e_1\}^\perp}$ is again compact self-adjoint; repeat to extract $\lambda_2,e_2$, etc. *(invariance of the orthogonal complement)*
4. **Eigenvalues decay to zero.** The $|\lambda_k|$ are non-increasing. If infinitely many $|\lambda_k|\ge\delta>0$, the orthonormal $e_k$ would satisfy $\|Te_k-Te_j\|^2=\lambda_k^2+\lambda_j^2\ge2\delta^2$, so $(Te_k)$ has no convergent subsequence — contradicting compactness. Hence $\lambda_k\to0$. *(compactness forces decay)*
5. **Completeness of the eigenexpansion.** Let $M=\overline{\mathrm{span}}\{e_k\}$. On $M^\perp$ the operator $T$ is compact self-adjoint with $\|T|_{M^\perp}\|=\sup|\langle x,Tx\rangle|$; if this were nonzero it would yield another eigenvalue/eigenvector orthogonal to all $e_k$ — contradiction. So $T|_{M^\perp}=0$, i.e. $M^\perp\subseteq\ker T$. Adjoining an ONB of $\ker T$ gives an ONB of $H$, and the Fourier expansion (§s4) yields $Tx=\sum_k\lambda_k\langle e_k,x\rangle e_k$. $\blacksquare$

**Worked example — an integral operator.** On $L^2[0,1]$ define $(Kf)(x)=\int_0^1 k(x,y)f(y)\,dy$ with continuous symmetric kernel $k(x,y)=k(y,x)$. Such a **Hilbert–Schmidt** operator is compact and self-adjoint, so it has an orthonormal eigenbasis $\{e_k\}$ with $\lambda_k\to0$ and $k(x,y)=\sum_k\lambda_k e_k(x)\overline{e_k(y)}$ (Mercer's theorem). For the explicit kernel $k(x,y)=\min(x,y)$ the eigenfunctions are $e_k(x)=\sqrt2\sin\big((k-\tfrac12)\pi x\big)$ with eigenvalues $\lambda_k=\big((k-\tfrac12)\pi\big)^{-2}\to0$ — the modes of a vibrating string.

---

## Part D — Unbounded operators, the general theorem, and distributions

<a id="s10"></a>
### Unbounded operators, domains, and symmetric vs. self-adjoint

**What and why.** The position and momentum operators are **unbounded**: there is no constant $C$ with $\|\hat p\psi\|\le C\|\psi\|$. Unbounded operators cannot be defined on the whole space; they live on a **domain**, and the careful distinction between *symmetric* and *self-adjoint* — meaningless in finite dimensions — decides whether an observable is physically legitimate.

> **Definition — unbounded operator and its domain.** An (unbounded) operator on $H$ is a linear map $T:D(T)\to H$ defined on a **domain** $D(T)$, a dense subspace of $H$. (Densely defined so the adjoint can be built.)

> **Definition — symmetric and self-adjoint.**
> - $T$ is **symmetric** if $\langle Tx,y\rangle=\langle x,Ty\rangle$ for all $x,y\in D(T)$.
> - The **adjoint** $T^*$ has domain $D(T^*)=\{y:\ x\mapsto\langle y,Tx\rangle\text{ is bounded on }D(T)\}$, with $\langle T^*y,x\rangle=\langle y,Tx\rangle$.
> - $T$ is **self-adjoint** if $T=T^*$ **including equality of domains**: $D(T)=D(T^*)$.
>
> Symmetric means $T\subseteq T^*$ (the adjoint extends $T$); self-adjoint means they are *exactly* equal. The domains are the whole subtlety.

> **Why the distinction is not pedantic.** The spectral theorem (§s11), hence a real spectrum and a well-defined functional calculus (so that $e^{-iHt/\hbar}$ is unitary and probability is conserved), holds for **self-adjoint** operators, *not* merely symmetric ones. A symmetric operator that is not self-adjoint may have **no** spectral decomposition and complex "deficiency" — physically, probability can leak out the boundary. Choosing a self-adjoint extension is choosing a **boundary condition**.

**Worked example — momentum on an interval.** Let $\hat p=-i\,\frac{d}{dx}$ on $L^2[0,1]$.
- On the domain $D_0=\{\psi\in C^1:\ \psi(0)=\psi(1)=0\}$, integration by parts gives $\langle\hat p\phi,\psi\rangle=\langle\phi,\hat p\psi\rangle+i[\,\overline{\phi}\psi\,]_0^1$; the boundary term vanishes, so $\hat p$ is **symmetric**. But $D(\hat p^*)$ is larger (it imposes no boundary condition), so $\hat p\ne\hat p^*$: **not self-adjoint**.
- To make it self-adjoint, impose **periodic** boundary conditions $\psi(1)=e^{i\theta}\psi(0)$. Each $\theta\in[0,2\pi)$ gives a *different* self-adjoint extension, with eigenfunctions $e^{i(2\pi n+\theta)x}$ and real eigenvalues $2\pi n+\theta$. The boundary condition is a physical choice (e.g. a particle on a ring with magnetic flux $\theta$).

**Worked example — position and momentum on the line.** On $L^2(\mathbb{R})$: $\hat x\psi(x)=x\psi(x)$ with domain $\{\psi:\int x^2|\psi|^2<\infty\}$, and $\hat p\psi=-i\hbar\psi'$ on the analogous Sobolev domain. Both are self-adjoint (no boundary to worry about), both unbounded, neither has eigenvectors *in* $L^2$, and both have spectrum $\mathbb{R}$ (continuous). The famous commutator $[\hat x,\hat p]=i\hbar I$ holds on the common dense domain; the impossibility of this relation for *bounded* operators (their commutator's spectrum could not contain a nonzero constant times $I$) is precisely why these observables *must* be unbounded.

**Worked example — the harmonic oscillator (pure point spectrum on the line).** The Hamiltonian $H=\tfrac12(\hat p^2+\hat x^2)$ on $L^2(\mathbb{R})$ is unbounded but **essentially self-adjoint** on the Schwartz functions, and — unlike $\hat x$ and $\hat p$ — it *does* have a complete orthonormal eigenbasis inside $L^2$: the Hermite functions $\psi_n(x)=c_n H_n(x)e^{-x^2/2}$ with eigenvalues $E_n=n+\tfrac12$, $n=0,1,2,\dots$. So a single self-adjoint operator can have purely discrete spectrum even on the whole line, provided the potential confines the particle. This is the rigorous content of "quantized energy levels": the spectrum is the *discrete* set $\{n+\tfrac12\}$, and the spectral theorem (§s11) reduces here to the Fourier expansion of §s4 in the Hermite basis.

> **Pitfall.** "Symmetric" textbooks sometimes call "Hermitian," but for unbounded operators Hermitian/symmetric is **weaker** than self-adjoint. Verifying $\langle Tx,y\rangle=\langle x,Ty\rangle$ is not enough; you must check the domains match. This is the single most common rigor error in physics computations.

> **Closed operators and essential self-adjointness, in one line.** An operator is **closed** if its graph is closed; symmetric operators are not automatically closed, and a symmetric operator with a *unique* self-adjoint extension (the good case, e.g. $H$ above on Schwartz functions) is called **essentially self-adjoint**. The technical machinery (deficiency indices) measures exactly how many self-adjoint extensions a symmetric operator admits: zero, one, or a whole family — the three regimes we met with momentum on an interval.

<a id="s11"></a>
### The general spectral theorem and the functional calculus

**What and why.** For a self-adjoint operator with mixed discrete/continuous spectrum, "sum over eigenvectors" must become an *integral*. The **spectral theorem** packages this as a **projection-valued measure**, and the **functional calculus** lets us apply any function to an operator — which is how $e^{-iHt/\hbar}$, $\sqrt{H}$, and the probability distribution of an observable are defined.

> **Theorem — spectral theorem (self-adjoint, statement).** Let $A$ be a self-adjoint operator on $H$. There is a unique **projection-valued measure** $E$ on the Borel subsets of $\sigma(A)\subseteq\mathbb{R}$ — assigning to each Borel set $\Omega$ an orthogonal projection $E(\Omega)$, with $E(\varnothing)=0$, $E(\mathbb{R})=I$, and $E$ countably additive on disjoint sets — such that
>
> $$
> A=\int_{\sigma(A)} \lambda\,\,dE(\lambda).
> $$
>
> Equivalently, $A$ is **unitarily equivalent to a multiplication operator** $M_g\,f=g\cdot f$ on some $L^2(\Omega,\mu)$: there is a unitary $U:H\to L^2(\Omega,\mu)$ with $UAU^{-1}=M_g$. (Every self-adjoint operator is "just multiplication by a real function," in suitable coordinates.)

This generalizes everything: when the spectrum is discrete, $E(\{\lambda_k\})$ is the projection onto the $\lambda_k$-eigenspace and the integral becomes the sum $\sum_k\lambda_k E(\{\lambda_k\})$ of §s9. When the spectrum is continuous (position, momentum), the integral is genuinely continuous and there are no eigenvectors at all.

> **Definition — functional calculus.** Given the spectral measure $E$ of a self-adjoint $A$ and a (bounded Borel) function $h:\sigma(A)\to\mathbb{C}$, define
>
> $$
> h(A):=\int_{\sigma(A)} h(\lambda)\,dE(\lambda).
> $$
>
> This is a $*$-homomorphism: $(h_1h_2)(A)=h_1(A)h_2(A)$, $\overline{h}(A)=h(A)^*$, and $h(A)$ is bounded with $\|h(A)\|=\sup_{\sigma(A)}|h|$.

> **How observables get their spectra and probabilities.** For an observable $A$ and a normalized state $\psi$, the real-valued function
>
> $$
> \mu_\psi(\Omega):=\langle\psi,\,E(\Omega)\,\psi\rangle=\|E(\Omega)\psi\|^2
> $$
>
> is a genuine **probability measure** on $\mathbb{R}$ (it is $\ge0$, and $\mu_\psi(\mathbb{R})=\langle\psi,\psi\rangle=1$). It is *the* probability distribution of the measured value of $A$ in state $\psi$ — the Born rule for continuous spectra. The expectation is $\langle\psi,A\psi\rangle=\int\lambda\,d\mu_\psi(\lambda)$.

> **Unitary dynamics.** With $h(\lambda)=e^{-i\lambda t/\hbar}$ (bounded, $|h|=1$) the functional calculus produces $U(t)=e^{-iAt/\hbar}=\int e^{-i\lambda t/\hbar}dE(\lambda)$, which is **unitary** because $\overline h\cdot h=1$ gives $U^*U=I$. So Schrödinger evolution is the functional calculus applied to the Hamiltonian — and unitarity (probability conservation) is automatic. **Stone's theorem** is the converse: every strongly continuous one-parameter unitary group $U(t)$ equals $e^{-iAt}$ for a unique self-adjoint generator $A$; this is the rigorous root of "every symmetry has a self-adjoint generator (observable)."

**Worked example.** For the position operator $\hat x$ on $L^2(\mathbb{R})$, the spectral measure is $E(\Omega)=$ multiplication by the indicator $\mathbf 1_\Omega(x)$. Then $\mu_\psi(\Omega)=\int_\Omega|\psi(x)|^2dx$ — exactly the familiar probability of finding the particle in the region $\Omega$. The "eigenvalue integral" $\hat x=\int_{\mathbb R}\lambda\,dE(\lambda)$ encodes $\hat x\psi=x\psi$. The general theorem reproduces the textbook rule.

<a id="s12"></a>
### Distributions: test functions, the Dirac delta, and rigged Hilbert spaces

**What and why.** The continuous spectrum has no eigenvectors in $H$, yet physicists write "position eigenstates" $|x\rangle$ with $\hat x|x\rangle=x|x\rangle$ and $\langle x|x'\rangle=\delta(x-x')$. **Distributions** make $\delta$ rigorous, and the **rigged Hilbert space** gives these generalized eigenvectors an honest home.

> **Definition — test functions and distributions.** A **test function** is a smooth function $\varphi:\mathbb{R}\to\mathbb{C}$ with compact support (it vanishes outside a bounded interval); their space is $\mathcal{D}=C_c^\infty(\mathbb{R})$. A **distribution** is a *continuous linear functional* $T:\mathcal{D}\to\mathbb{C}$, written $\langle T,\varphi\rangle$. Distributions are the dual space $\mathcal{D}'$. (Continuity is with respect to the natural notion of convergence in $\mathcal D$: uniform convergence of the functions and all their derivatives, with supports in a common bounded set.)

Every ordinary (locally integrable) function $f$ *is* a distribution via $\langle T_f,\varphi\rangle=\int f\varphi$, so distributions generalize functions.

> **Definition — the Dirac delta.** The **Dirac delta** $\delta$ is the distribution
>
> $$
> \langle\delta,\varphi\rangle:=\varphi(0).
> $$
>
> It is linear and continuous, hence a legitimate element of $\mathcal{D}'$. It is **not** a function: no locally integrable $f$ has $\int f\varphi=\varphi(0)$ for all $\varphi$ (such an $f$ would have to be $0$ off $\{0\}$, forcing $\int f\varphi=0$). The informal "$\int\delta(x)\varphi(x)dx=\varphi(0)$" is shorthand for this pairing.

> **Definition — derivative of a distribution.** The **distributional derivative** $T'$ is defined by transferring the derivative onto the test function:
>
> $$
> \langle T',\varphi\rangle:=-\langle T,\varphi'\rangle.
> $$
>
> This is the *only* definition that agrees with integration by parts for smooth $f$ (the boundary term vanishes because $\varphi$ has compact support). Consequence: **every** distribution is infinitely differentiable.

**Worked example — the Heaviside step and the delta.** Let $H(x)=1$ for $x>0$, $0$ for $x<0$ (a distribution via integration). Its distributional derivative:
1. $\langle H',\varphi\rangle=-\langle H,\varphi'\rangle=-\int_{-\infty}^\infty H(x)\varphi'(x)dx=-\int_0^\infty\varphi'(x)dx$. *(definition of $H'$ then of $H$ as a functional)*
2. $=-[\varphi(x)]_0^\infty=-\big(0-\varphi(0)\big)=\varphi(0)$, using that $\varphi$ vanishes at $+\infty$ (compact support). *(fundamental theorem of calculus)*
3. So $\langle H',\varphi\rangle=\varphi(0)=\langle\delta,\varphi\rangle$ for all $\varphi$, i.e. $H'=\delta$. The derivative of a jump is the delta — rigorously. $\blacksquare$

**Worked example — the delta as a limit.** The Gaussians $g_\epsilon(x)=\frac{1}{\sqrt{2\pi}\epsilon}e^{-x^2/2\epsilon^2}$ have $\int g_\epsilon=1$ and concentrate at $0$; for any test function $\langle g_\epsilon,\varphi\rangle=\int g_\epsilon\varphi\to\varphi(0)=\langle\delta,\varphi\rangle$ as $\epsilon\to0$. So $\delta$ is the limit (in $\mathcal{D}'$) of ever-sharper bumps — the picture physicists draw, made precise as convergence of *functionals*.

**Worked example — the Fourier transform of $\delta$, and plane waves.** Extending the Fourier transform to distributions (again by transferring it onto the test function, $\langle\widehat T,\varphi\rangle:=\langle T,\widehat\varphi\rangle$), one gets $\widehat\delta=$ the constant function $\tfrac1{\sqrt{2\pi}}$, and dually $\widehat{1}=\sqrt{2\pi}\,\delta$. Read physically: the position eigenstate $\delta$ has *flat* momentum content (all momenta equally), and a momentum eigenstate $e^{ipx}$ (the plane wave $\widehat{}\,$ of a delta in momentum space) is spread uniformly over all positions. The maximally localized and maximally spread states are exact Fourier transforms of each other — the rigorous root of the position–momentum uncertainty principle, and a computation that *only* makes sense for distributions, since neither $\delta$ nor $e^{ipx}$ is in $L^2$.

> **Definition — rigged Hilbert space (Gelfand triple).** A **rigged Hilbert space** is a chain
>
> $$
> \Phi\ \subseteq\ H\ \subseteq\ \Phi',
> $$
>
> where $\Phi$ is a dense subspace of "nice" states (e.g. the Schwartz functions, on which $\hat x,\hat p$ act freely), $H$ is the Hilbert space, and $\Phi'$ is the dual of $\Phi$ — a space of distributions large enough to contain the **generalized eigenvectors**.

> **How it legitimizes Dirac's notation.** The "position eigenstate" $|x_0\rangle$ is the distribution $\delta_{x_0}\in\Phi'$ defined by $\langle\delta_{x_0},\varphi\rangle=\varphi(x_0)$. It is not in $H$ (it has infinite norm), but it lives perfectly well in the rigging $\Phi'$, where $\hat x\,\delta_{x_0}=x_0\,\delta_{x_0}$ holds as an identity of distributions, and $\langle x_0|\psi\rangle=\psi(x_0)$ is the pairing. The continuous-spectrum "eigenbasis" $\{|x\rangle\}$ with $\int|x\rangle\langle x|\,dx=I$ is then the spectral measure of §s11 written in physicist's notation. The rigged Hilbert space is the structure that reconciles Dirac's eigenstates with von Neumann's rigorous spectral theory.

> **Quantum reading.** Three layers: states *physically prepared and measured* live in $\Phi$; the abstract Hilbert space $H$ carries the inner product and probabilities; and $\Phi'$ houses idealized objects ($\delta$, plane waves $e^{ipx}$) that are computational scaffolding, never literal states. Functional analysis is exactly the discipline that keeps these three honest.

---

*This guide built functional analysis from metric completeness up to the spectral theorem, the functional calculus, and the theory of distributions, then read the whole structure back as the rigorous home of quantum mechanics: a state is a unit vector in a Hilbert space, an observable is a self-adjoint operator, its measurable values are its spectrum, the probabilities come from a projection-valued measure via the Born rule, time evolution is the unitary functional calculus $e^{-iHt/\hbar}$, and Dirac's $\delta$ and continuous eigenstates live honestly in a rigged Hilbert space. Return to any boxed definition or numbered proof as a reference — and remember that completeness is what lets limits of wavefunctions exist, and that single guarantee is what makes the geometry of infinite dimensions, and hence quantum mechanics, possible at all.*
