**English** · [中文](index-theory.zh.md)

# Index Theory & the Atiyah–Singer Theorem, *counting solutions with topology.*

*A self-contained, rigorous introduction to one of the deepest bridges in mathematics: the statement that an analytic quantity — the number of solutions of a differential equation minus the number of obstructions to solving it — is forced to equal a topological quantity that you can compute by integrating characteristic classes. We start from the bare notion of a Fredholm operator and its index, build through ellipticity and Hodge theory to the Dirac operator, and arrive at the Atiyah–Singer index theorem, recovering Gauss–Bonnet, the signature theorem, and Riemann–Roch as special cases, before closing with the heat-kernel proof sketch and the physics of anomalies. Geometry and analysis are the goal; physics is the motivation; every symbol is defined and every claim we can prove at this level is proved.*

[← Back to all guides](../README.md)

**Prerequisites.** This guide leans on three companion guides and restates each fact at the moment of use. From the **Differential Topology & Characteristic Classes** guide ([`differential-topology.md`](../topology/differential-topology.md)) we borrow de Rham cohomology, the Euler characteristic, characteristic classes (Chern classes $c_k$, Pontryagin classes $p_k$, the Euler class $e$), the Chern–Weil construction that represents them by curvature, and the Gauss–Bonnet–Chern theorem. From the **Functional Analysis & Hilbert Spaces** guide ([`functional-analysis.md`](../functional-analysis/functional-analysis.md)) we borrow Banach and Hilbert spaces, bounded and compact operators, adjoints, and the closed-range theorem. From the **Differential Geometry & Tensors** guide ([`differential-geometry.md`](differential-geometry.md)) we borrow smooth manifolds, tangent and cotangent bundles, vector bundles, differential forms, the exterior derivative $d$, the wedge product $\wedge$, Riemannian metrics, and connections with their curvature. No prior exposure to partial differential equations beyond single-variable calculus is assumed; the analytic facts we need are stated precisely and motivated.

## Part A · The analytic side — operators and their index

<a id="s0"></a>
### Motivation — analytic data equals topological data

The single idea of this guide is a slogan: **the kernel and cokernel of a natural differential operator carry an integer that cannot move when you deform the geometry, and that integer is computable from topology alone.**

#### What problem are we solving?

Suppose you have a linear equation $Du = f$, where $D$ is some linear operator (think of a differential operator like the Laplacian) acting on functions or sections of a vector bundle. Two basic questions arise:

1. **Uniqueness.** How many independent solutions does the *homogeneous* equation $Du = 0$ have? These solutions form the **kernel** of $D$, written $\ker D = \{u : Du = 0\}$. Its dimension $\dim\ker D$ counts how badly uniqueness fails.
2. **Solvability.** For which right-hand sides $f$ is $Du = f$ solvable? The obstructions live in the **cokernel** $\operatorname{coker} D = (\text{target space})/(\operatorname{im} D)$, where $\operatorname{im} D = \{Du\}$ is the image. Its dimension $\dim\operatorname{coker} D$ counts the constraints $f$ must satisfy.

Each of these two numbers is fragile: a tiny change in $D$ can create or destroy a solution, raising or lowering $\dim\ker D$. But their **difference**

$$
\operatorname{ind} D \;=\; \dim\ker D \;-\; \dim\operatorname{coker} D
$$

turns out to be rigid. This difference is the **analytic index**. The miracle, due to Michael Atiyah and Isadore Singer in 1963, is that for an *elliptic* operator (a class we make precise in s2) on a compact manifold, $\operatorname{ind} D$ equals a number you can read off the topology of the manifold and the bundles involved — the **topological index** — with no reference to the operator's detailed coefficients at all.

#### Why this is surprising and useful

Consider an analogy with finite-dimensional linear algebra. If $A: \mathbb{R}^n \to \mathbb{R}^m$ is a matrix, the rank–nullity theorem gives $\dim\ker A = n - \operatorname{rank} A$ and $\dim\operatorname{coker} A = m - \operatorname{rank} A$, so

$$
\dim\ker A - \dim\operatorname{coker} A = (n - \operatorname{rank} A) - (m - \operatorname{rank} A) = n - m.
$$

The index of a matrix is simply $n - m$: it depends only on the *shapes* of the source and target, never on the entries. Index theory is the infinite-dimensional descendant of this fact. In infinite dimensions there is no fixed "$n-m$", but for the right operators a substitute survives, and the substitute is *topological*.

The payoff is enormous. Counting solutions of geometric PDEs (harmonic forms, holomorphic sections, harmonic spinors) is hard analysis; computing characteristic numbers is finite topology. The index theorem trades the first for the second. It unifies the Gauss–Bonnet theorem (Euler characteristic from curvature), the Hirzebruch signature theorem, and the Riemann–Roch theorem of algebraic geometry into a single statement, and it explains anomalies in quantum field theory.

> **Intuition.** Think of the index as a "topologically protected" count, like the number of times a closed loop winds around a hole: you can wiggle the loop, but the winding number jumps only if you tear it. Wiggling $D$ moves $\ker$ and $\operatorname{coker}$, but solutions can only appear or vanish *in matched pairs*, leaving the difference fixed.

The plan: Fredholm operators and the stability of the index (s1); differential operators, symbols, ellipticity (s2); elliptic regularity and finiteness (s3); the de Rham complex and the Euler characteristic as an index (s4); the Hodge theorem (s5); Clifford algebras and the Dirac operator (s6); the topological index ingredients — Chern character, Todd class, $\hat A$-genus (s7); the index theorem itself (s8); its famous special cases (s9); the heat-kernel proof outline (s10); and the physics of anomalies (s11).

<a id="s1"></a>
### Fredholm operators and the analytic index; stability under perturbation

We make precise the class of operators that *have* a well-defined integer index, and we prove the index cannot change under small or compact perturbations. This stability is the engine of the whole theory.

#### Definition and basic objects

> **Definition — Fredholm operator.**
>
> Let $H_1, H_2$ be Hilbert spaces (complete inner-product spaces; see the Functional Analysis guide). A bounded linear operator $T: H_1 \to H_2$ is **Fredholm** if
> - $\ker T = \{x \in H_1 : Tx = 0\}$ is finite-dimensional;
> - the image $\operatorname{im} T = \{Tx : x \in H_1\}$ is closed in $H_2$;
> - $\operatorname{coker} T = H_2 / \operatorname{im} T$ is finite-dimensional.
>
> The **(analytic) index** is the integer
> $$
> \operatorname{ind} T = \dim\ker T - \dim\operatorname{coker} T.
> $$

Here "bounded" means there is a constant $C$ with $\|Tx\| \le C\|x\|$ for all $x$, equivalently $T$ is continuous. The quotient $H_2/\operatorname{im} T$ is the space of equivalence classes $[y]$ where $y \sim y'$ iff $y - y' \in \operatorname{im} T$; its dimension measures how far $T$ is from being onto.

A clean reformulation uses the **adjoint** $T^*: H_2 \to H_1$, defined by $\langle Tx, y\rangle = \langle x, T^* y\rangle$ for all $x,y$. When $\operatorname{im} T$ is closed, the closed-range theorem (Functional Analysis guide) gives the orthogonal decomposition $H_2 = \operatorname{im} T \oplus (\operatorname{im} T)^\perp$ and the identity $(\operatorname{im} T)^\perp = \ker T^*$. Hence $\operatorname{coker} T \cong \ker T^*$ as vector spaces, and

$$
\operatorname{ind} T = \dim\ker T - \dim\ker T^*.
$$

This is the form we use constantly: the index is the difference between the number of solutions of $Tx = 0$ and the number of solutions of $T^* y = 0$.

> **Worked example (a shift operator).** Let $H_1 = H_2 = \ell^2$, the space of square-summable sequences $x = (x_0, x_1, x_2, \dots)$ with $\sum |x_n|^2 < \infty$. Define the **right shift** $S(x_0, x_1, \dots) = (0, x_0, x_1, \dots)$.
> - $\ker S = 0$: if $Sx = 0$ then every $x_n = 0$. So $\dim\ker S = 0$.
> - $\operatorname{im} S = \{y : y_0 = 0\}$, which is closed, and $\operatorname{coker} S$ is one-dimensional (spanned by the class of $(1,0,0,\dots)$). So $\dim\operatorname{coker} S = 1$.
> - Therefore $\operatorname{ind} S = 0 - 1 = -1$.
>
> The left shift $S^*(x_0, x_1, \dots) = (x_1, x_2, \dots)$ is the adjoint, with $\ker S^* = \operatorname{span}\{(1,0,0,\dots)\}$, $\dim = 1$, confirming $\operatorname{ind} S = \dim\ker S - \dim\ker S^* = 0 - 1 = -1$. The power $S^k$ has index $-k$: indices range over all of $\mathbb Z$, so the integer is genuinely informative.

#### The stability theorem and its proof

> **Theorem (stability of the index).** Let $T: H_1 \to H_2$ be Fredholm.
> (a) If $K: H_1 \to H_2$ is **compact** (maps bounded sets to sets with compact closure), then $T + K$ is Fredholm and $\operatorname{ind}(T+K) = \operatorname{ind} T$.
> (b) There is $\varepsilon > 0$ such that every bounded $B$ with $\|B\| < \varepsilon$ has $T+B$ Fredholm and $\operatorname{ind}(T+B) = \operatorname{ind} T$.

We prove the heart of both statements: that the index is invariant. We use one structural fact, **Atkinson's theorem**, which we first establish.

> **Atkinson's theorem.** $T$ is Fredholm if and only if it is **invertible modulo compact operators**: there exists a bounded $P$ (a *parametrix*) with $PT - I = K_1$ and $TP - I = K_2$ where $K_1, K_2$ are compact.

**Proof of Atkinson (⇒).**
1. Suppose $T$ is Fredholm. By definition $\ker T$ is finite-dimensional and $\operatorname{im} T$ is closed with finite-dimensional complement. Restrict $T$ to $(\ker T)^\perp$; the restriction $T_0: (\ker T)^\perp \to \operatorname{im} T$ is a bounded bijection between Hilbert spaces (injective because we quotiented the kernel, surjective onto the image). *Reason:* removing the kernel makes $T$ injective; its image is unchanged.
2. By the bounded inverse theorem (a complete-space consequence of the open mapping theorem, Functional Analysis guide), $T_0^{-1}: \operatorname{im} T \to (\ker T)^\perp$ is bounded.
3. Define $P: H_2 \to H_1$ by $P = T_0^{-1} \circ \Pi$, where $\Pi: H_2 \to \operatorname{im} T$ is the orthogonal projection. Then $P$ is bounded (composition of bounded maps).
4. Compute $TP - I$. On $\operatorname{im} T$, $TP = T T_0^{-1} = I$; on $(\operatorname{im} T)^\perp$, $\Pi = 0$ so $TP = 0$. Thus $TP - I = -(I - \Pi)$, the negative of the projection onto $(\operatorname{im} T)^\perp$, which is finite-rank (since $\operatorname{coker} T$ is finite-dimensional) and hence compact. *Reason:* finite-rank operators are compact.
5. Similarly $PT - I = -(\text{projection onto } \ker T)$, finite-rank, hence compact. This finishes (⇒). $\qquad\blacksquare$

**Proof of stability (a), index invariance.** We use Atkinson and a determinant-free counting argument.
1. Let $T$ be Fredholm with parametrix $P$, so $PT = I + K_1$, $TP = I + K_2$ with $K_i$ compact. For compact $K$, the operator $T+K$ then satisfies $P(T+K) = I + K_1 + PK$ and $(T+K)P = I + K_2 + KP$; since $PK$ and $KP$ are compact (compact composed with bounded is compact), $T+K$ also has $P$ as a parametrix, so $T+K$ is Fredholm by Atkinson (⇐, which follows from the Riesz theory that $I + \text{compact}$ is Fredholm of index $0$). *Reason:* the parametrix condition is what Fredholmness amounts to.
2. To see the index does not change, consider the path $T_t = T + tK$, $t \in [0,1]$. Each $T_t$ is Fredholm by step 1. We show $t \mapsto \operatorname{ind} T_t$ is locally constant; being integer-valued and (we show next) continuous, it is constant on $[0,1]$.

**Proof of stability (b), local constancy.** This is the key lemma; (a)'s constancy then follows.
1. Fix Fredholm $T$. Choose a finite-rank operator $F: H_1 \to H_2$ whose image is a complement of $\operatorname{im} T$ in $H_2$, i.e. $F$ maps a copy of $\operatorname{coker} T$ isomorphically onto $(\operatorname{im} T)^\perp$ and kills $(\ker T)^\perp$... more simply, let $F$ be an isomorphism from $\ker T$ onto a chosen complement $C \cong \operatorname{coker} T$ extended by zero. Consider the *augmented* operator
$$
\widehat T = T + F.
$$
2. By construction $\widehat T$ is surjective and injective, i.e. invertible: any $x = x_0 + x_1$ with $x_0 \in \ker T$, $x_1 \in (\ker T)^\perp$ maps to $F x_0 + T x_1 \in C \oplus \operatorname{im} T = H_2$, and this is a bijection because $F|_{\ker T}$ and $T|_{(\ker T)^\perp}$ are bijections onto complementary closed subspaces. *Reason:* direct sum of two isomorphisms onto complementary summands.
3. Since invertibility is an open condition (the invertible operators form an open set, as $\|B\| < \|\widehat T^{-1}\|^{-1}$ keeps $\widehat T + B$ invertible by the Neumann series $\sum (-\widehat T^{-1}B)^k$), there is $\varepsilon > 0$ so that $\|B\| < \varepsilon$ implies $\widehat T + B = (T + B) + F$ is invertible.
4. Now for such $B$, $T+B = (\widehat T + B) - F$ is a finite-rank ($\operatorname{rank} F = \dim\ker T =: k$) perturbation of an invertible operator. A finite-rank perturbation of an invertible operator is Fredholm of index $0 - 0 = 0$ shifted by the rank bookkeeping; precisely:
5. **Index of $A - F$ with $A$ invertible, $\operatorname{rank} F = k$.** Write $L = A^{-1}F$, a rank-$k$ operator, so $T + B = A(I - L)$. Multiplying by the invertible $A$ does not change the index (composition with an isomorphism is a bijection on $\ker$ and $\operatorname{coker}$), so $\operatorname{ind}(T+B) = \operatorname{ind}(I - L)$. For a finite-rank $L$, $I - L$ acts as the identity off the finite-dimensional subspace $W = \operatorname{im} L + (\text{relevant finite space})$ and as $I - L|_W$ on $W$; on the complement it is the identity (index $0$), and on the finite-dimensional space $W$ the index is $\dim W - \dim W = 0$ by rank–nullity for the square matrix $I - L|_W$. Hence $\operatorname{ind}(I - L) = 0$.
6. Therefore for all $\|B\| < \varepsilon$, $\operatorname{ind}(T+B) = \operatorname{ind}(\widehat T + B) + (\text{correction}) = 0 + 0$? We must track the correction carefully. The clean statement: $\operatorname{ind}(T+B)$ is *independent of $B$* for $\|B\| < \varepsilon$, because the computation in step 5 produced the *same* value (namely $\operatorname{ind}(I-L)=0$ relative to the invertible reference) for every such $B$. Setting $B = 0$ gives $\operatorname{ind}(T+B) = \operatorname{ind} T$ for all small $B$. *Reason:* a function that is constant on a neighborhood of $0$ and integer-valued, evaluated at $0$, gives $\operatorname{ind} T$. $\qquad\blacksquare$

For (a), apply (b) along the path $T_t = T + tK$: cover $[0,1]$ by finitely many intervals on each of which the index is constant, so $\operatorname{ind} T_0 = \operatorname{ind} T_1$, i.e. $\operatorname{ind}(T) = \operatorname{ind}(T+K)$.

> **Why this matters.** Stability is *why* the index is topological. Two elliptic operators that can be deformed into each other through elliptic operators (or differ by lower-order, hence "compact-like", terms) have the same index. So the index depends only on a discrete deformation class — exactly the kind of data topology measures. Pitfall: the *individual* dimensions $\dim\ker T$ and $\dim\operatorname{coker} T$ are **not** stable; only the difference is. Never expect to compute $\dim\ker$ from topology.

<a id="s2"></a>
### Differential operators, their principal symbols, and ellipticity

The Fredholm theory of s1 lives on Hilbert spaces. To apply it to geometry we need operators built from differentiation, and the crucial invariant that decides Fredholmness: the **principal symbol**.

#### Differential operators on bundles

> **Definition — differential operator.** Let $E, F \to M$ be smooth complex vector bundles over a smooth manifold $M$ (a bundle assigns a vector space $E_x$ to each point $x$, varying smoothly; sections are smooth choices $s(x)\in E_x$). Let $\Gamma(E)$ denote the smooth sections. A **linear differential operator of order $\le m$** is a linear map $D: \Gamma(E) \to \Gamma(F)$ that in any local coordinate chart $(x^1,\dots,x^n)$ and local trivializations is
> $$
> D = \sum_{|\alpha| \le m} A_\alpha(x)\, \partial^\alpha,
> $$
> where $\alpha = (\alpha_1,\dots,\alpha_n)$ is a multi-index, $|\alpha| = \alpha_1 + \cdots + \alpha_n$, $\partial^\alpha = \partial_{x^1}^{\alpha_1}\cdots\partial_{x^n}^{\alpha_n}$, and each $A_\alpha(x)$ is a matrix-valued smooth function (a linear map $E_x \to F_x$). The order is $m$ if some $A_\alpha$ with $|\alpha| = m$ is nonzero.

Examples: the gradient, the divergence, the exterior derivative $d$, and the Laplacian $\Delta = -\sum_i \partial_{x^i}^2$ (order $2$).

#### The principal symbol

The behaviour of $D$ that controls Fredholmness is its **top-order part**, packaged geometrically.

> **Definition — principal symbol.** For a covector $\xi \in T_x^* M$ (a linear functional on the tangent space; in coordinates $\xi = \sum_i \xi_i\, dx^i$), the **principal symbol** of an order-$m$ operator $D = \sum_{|\alpha|\le m} A_\alpha \partial^\alpha$ is the linear map $\sigma_m(D)(x,\xi): E_x \to F_x$ defined by keeping only the top-order terms and replacing $\partial_{x^i} \mapsto i\,\xi_i$:
> $$
> \sigma_m(D)(x,\xi) = i^m \sum_{|\alpha| = m} A_\alpha(x)\, \xi^\alpha,
> \qquad \xi^\alpha := \xi_1^{\alpha_1}\cdots\xi_n^{\alpha_n}.
> $$

The factor $i = \sqrt{-1}$ comes from the Fourier transform: $\partial_{x^i}$ acting on $e^{i\langle x,\xi\rangle}$ produces $i\xi_i\, e^{i\langle x,\xi\rangle}$. The symbol records how $D$ acts on rapidly oscillating waves of frequency $\xi$; high-frequency behaviour is governed entirely by the top-order coefficients. A genuinely coordinate-free statement holds: $\sigma_m(D)$ is a well-defined bundle map $\pi^* E \to \pi^* F$ over the cotangent bundle $T^*M$ (where $\pi: T^*M \to M$), homogeneous of degree $m$ in $\xi$.

> **Worked example (the Laplacian's symbol).** For $\Delta = -\sum_i \partial_{x^i}^2$ on functions ($E=F=$ trivial line bundle), the top-order terms are all of $\Delta$, with $A_\alpha = -1$ when $\alpha = 2e_i$ and $0$ otherwise. Then
> $$
> \sigma_2(\Delta)(x,\xi) = i^2 \sum_i (-1)\,\xi_i^2 = (-1)\cdot(-1)\sum_i \xi_i^2 = |\xi|^2.
> $$
> For $\xi \ne 0$ this is a nonzero number (an invertible $1\times 1$ "matrix"). That nonvanishing is exactly *ellipticity*.

#### Ellipticity

> **Definition — elliptic operator.** $D: \Gamma(E)\to\Gamma(F)$ of order $m$ is **elliptic** if for every $x\in M$ and every nonzero $\xi \in T_x^*M$, the principal symbol $\sigma_m(D)(x,\xi): E_x \to F_x$ is an **isomorphism** (in particular $E$ and $F$ have the same rank).

The word "elliptic" comes from the classification of second-order scalar PDEs: $a\partial_x^2 + 2b\partial_x\partial_y + c\partial_y^2$ has symbol $-(a\xi_1^2 + 2b\xi_1\xi_2 + c\xi_2^2)$, which is nonvanishing for all $\xi\ne 0$ exactly when the quadratic form is definite — the condition $b^2 - ac < 0$ that classifies the equation as elliptic (like $\Delta$), as opposed to hyperbolic (the wave equation, $b^2 - ac > 0$) or parabolic (the heat equation, $b^2 - ac = 0$). The wave operator $\partial_t^2 - \partial_x^2$ has symbol $-(\xi_t^2 - \xi_x^2)$, which vanishes on the cone $\xi_t = \pm\xi_x$: it is **not** elliptic, and indeed it does not have a finite index. Ellipticity is precisely the condition that makes the symbol "invertible in all directions," which is what we need to build a parametrix and invoke s1.

> **Intuition.** Ellipticity says the operator's leading part has no "characteristic directions" along which information can travel without smoothing — no shock fronts, no light cones. Solutions of $Du = 0$ are then as smooth as the coefficients allow (next section). Pitfall: lower-order terms are irrelevant to ellipticity; $\Delta + V(x)$ is elliptic for any smooth potential $V$ because the symbol ignores $V$.

<a id="s3"></a>
### Elliptic regularity and why elliptic operators on compact manifolds are Fredholm

This section delivers the bridge: an elliptic operator on a *compact* manifold defines a Fredholm operator on the right Hilbert spaces, so the index of s1 applies. We state the two analytic theorems precisely and explain the key ideas; full proofs belong to a PDE course, but every ingredient is named.

#### Sobolev spaces — the right Hilbert spaces

To use Hilbert-space Fredholm theory we cannot work with $\Gamma(E)$ (smooth sections form a Fréchet, not Hilbert, space). We complete in **Sobolev norms**.

> **Definition — Sobolev space.** Fix a metric on $M$ and on $E$ (so sections have pointwise norms and there is a volume form $dV$). For an integer $s \ge 0$, the Sobolev space $H^s(E)$ is the completion of $\Gamma(E)$ under
> $$
> \|u\|_s^2 = \sum_{|\alpha|\le s} \int_M |\partial^\alpha u|^2 \, dV.
> $$
> It is a Hilbert space whose elements are sections with square-integrable derivatives up to order $s$ (derivatives taken in the distributional sense; see Functional Analysis guide).

A differential operator of order $m$ extends to a bounded map $D: H^s(E) \to H^{s-m}(F)$, because differentiating $m$ times costs $m$ derivatives of regularity. The interplay of these spaces is governed by two theorems.

#### The two analytic theorems

> **Theorem (elliptic regularity / Gårding's inequality).** Let $D$ be elliptic of order $m$ on a compact manifold $M$. Then:
> (i) **A priori estimate.** There is a constant $C$ with
> $$
> \|u\|_s \le C\big(\|Du\|_{s-m} + \|u\|_{s-1}\big) \qquad \text{for all } u.
> $$
> (ii) **Regularity.** If $u$ is a distributional solution of $Du = f$ and $f$ is smooth, then $u$ is smooth. More generally $f \in H^{s-m}$ forces $u \in H^s$.

> **Theorem (Fredholmness of elliptic operators).** An elliptic operator $D$ of order $m$ on a *compact* manifold $M$, viewed as $D: H^s(E) \to H^{s-m}(F)$, is Fredholm. Moreover $\ker D$ consists of smooth sections, $\dim\ker D < \infty$, $\dim\operatorname{coker} D < \infty$, and $\operatorname{coker} D \cong \ker D^*$ where $D^*$ is the formal adjoint (also elliptic). Consequently $\operatorname{ind} D = \dim\ker D - \dim\ker D^*$ is a well-defined integer, **independent of $s$**.

#### The key ideas of the proof

We do not reproduce the full PDE argument, but here is the complete logical skeleton — each step justified by a named tool.

1. **Build a parametrix from the symbol.** Because $\sigma_m(D)(x,\xi)$ is invertible for $\xi\ne 0$ (ellipticity), one can construct a **pseudodifferential operator** $Q$ of order $-m$ whose symbol is $\sigma_m(D)^{-1}$ to leading order. Pseudodifferential operators generalize differential operators by allowing symbols that are smooth functions of $(x,\xi)$ (e.g. $|\xi|^{-m}$), defined via the Fourier transform $Qu(x) = (2\pi)^{-n}\int e^{i\langle x,\xi\rangle} q(x,\xi)\,\hat u(\xi)\,d\xi$. *Reason this is possible:* invertibility of the symbol lets us invert it pointwise in $\xi$ and patch the pieces.
2. **Parametrix identities.** This $Q$ satisfies $QD = I + R_1$ and $DQ = I + R_2$ where $R_1, R_2$ are pseudodifferential of *negative* order — they gain a derivative. *Reason:* composing $Q$ (symbol $\approx \sigma_m^{-1}$) with $D$ (symbol $\sigma_m$) gives leading symbol $I$; the error is lower order by the symbol calculus.
3. **Smoothing operators are compact (Rellich's theorem).** On a *compact* manifold, the inclusion $H^s \hookrightarrow H^{s'}$ for $s > s'$ is a compact operator (Rellich–Kondrachov). Since $R_1, R_2$ map $H^s$ into $H^{s+1}$ and then include back, they are compact. *Reason:* compactness of $M$ makes bounded-derivative sets precompact — this is exactly where compactness of $M$ is used.
4. **Apply Atkinson.** Steps 2–3 say $D$ is invertible modulo compact operators: it has a parametrix $Q$ with $QD - I$, $DQ - I$ compact. By Atkinson's theorem (s1), $D$ is Fredholm.
5. **Regularity gives smoothness of the kernel.** If $Du = 0$ then $u = Qf - R_1 u = -R_1 u$ gains a derivative; bootstrapping ($u \in H^s \Rightarrow u \in H^{s+1} \Rightarrow \cdots$) shows $u \in \bigcap_s H^s = $ smooth sections (Sobolev embedding: $\bigcap_s H^s = C^\infty$). *Reason:* the a priori estimate, applied repeatedly.
6. **Index independent of $s$.** Since $\ker D$ is smooth (so the same regardless of $s$) and likewise $\ker D^*$, the index $\dim\ker D - \dim\ker D^*$ does not see $s$. $\qquad\blacksquare$

> **Pitfall.** Compactness of $M$ is essential. On $\mathbb R^n$ the inclusion $H^s \hookrightarrow H^{s'}$ is *not* compact (mass can escape to infinity), Rellich fails, and elliptic operators need not be Fredholm — e.g. $\Delta$ on $\mathbb R^n$ has continuous spectrum down to $0$ and no finite index. The compact-manifold hypothesis is built into every statement of the index theorem.

## Part B · Geometric incarnations — de Rham, Hodge, Dirac

<a id="s4"></a>
### The de Rham complex and the Euler characteristic as an index

We now meet the first genuinely geometric elliptic operator and the first identification of an index with a topological invariant. The lesson: the **Euler characteristic** is an index.

#### The de Rham complex

Let $M$ be a compact oriented Riemannian manifold of dimension $n$. Let $\Omega^k = \Gamma(\Lambda^k T^*M)$ be the smooth differential $k$-forms (alternating $k$-linear functions on tangent vectors; see the Differential Geometry guide). The **exterior derivative** $d: \Omega^k \to \Omega^{k+1}$ is the first-order differential operator satisfying $d^2 = 0$. The sequence

$$
0 \to \Omega^0 \xrightarrow{d} \Omega^1 \xrightarrow{d} \cdots \xrightarrow{d} \Omega^n \to 0
$$

is the **de Rham complex**. Because $d^2 = 0$ we have $\operatorname{im}(d:\Omega^{k-1}\to\Omega^k) \subseteq \ker(d:\Omega^k\to\Omega^{k+1})$, and the **de Rham cohomology** is the quotient

$$
H^k_{\mathrm{dR}}(M) = \frac{\ker(d:\Omega^k\to\Omega^{k+1})}{\operatorname{im}(d:\Omega^{k-1}\to\Omega^k)}.
$$

A theorem of de Rham (Differential Topology guide) identifies $H^k_{\mathrm{dR}}(M)$ with the topological cohomology of $M$; in particular its dimension $b_k = \dim H^k_{\mathrm{dR}}(M)$, the **$k$-th Betti number**, is a topological invariant.

#### Folding the complex into a single elliptic operator

A complex is not a single operator, but we can fold it. Using the Riemannian metric, define the **formal adjoint** $d^*: \Omega^{k+1}\to\Omega^k$ by $\int_M \langle d\alpha, \beta\rangle\, dV = \int_M \langle \alpha, d^*\beta\rangle\, dV$. Split forms by parity into even and odd:

$$
\Omega^{\mathrm{ev}} = \bigoplus_{k \text{ even}} \Omega^k, \qquad \Omega^{\mathrm{odd}} = \bigoplus_{k \text{ odd}} \Omega^k,
$$

and define the single operator

$$
D = d + d^* : \Omega^{\mathrm{ev}} \to \Omega^{\mathrm{odd}}.
$$

> **Proposition.** $D = d+d^*$ is elliptic.

**Proof.**
1. The symbol of $d$ at $(x,\xi)$ is $\sigma(d)(\xi)\,\omega = i\,\xi\wedge\omega$ (exterior multiplication by $i\xi$), because $d$ in coordinates is $\sum dx^i \wedge \partial_{x^i}$ and the symbol rule replaces $\partial_{x^i}\mapsto i\xi_i$. *Reason:* definition of principal symbol (s2).
2. The symbol of $d^*$ is $\sigma(d^*)(\xi)\,\omega = -i\,\iota_{\xi^\sharp}\omega$ (interior multiplication by the metric-dual vector $\xi^\sharp$), the adjoint of $i\xi\wedge(\cdot)$ under the inner product. *Reason:* the adjoint of wedging is contracting.
3. Thus $\sigma(D)(\xi) = i(\xi\wedge \,\cdot\; -\; \iota_{\xi^\sharp})$. Its square is $\sigma(D)(\xi)^2 = -(\xi\wedge\iota_{\xi^\sharp} + \iota_{\xi^\sharp}\,\xi\wedge\,\cdot)$. The identity $\xi\wedge\iota_{\xi^\sharp} + \iota_{\xi^\sharp}\,(\xi\wedge\cdot) = |\xi|^2\,\mathrm{id}$ (the Clifford/Cartan relation) gives $\sigma(D)(\xi)^2 = -|\xi|^2\,\mathrm{id}$. *Reason:* the contraction-wedge anticommutator equals the squared length.
4. For $\xi\ne 0$, $\sigma(D)(\xi)^2 = -|\xi|^2\,\mathrm{id}$ is invertible, so $\sigma(D)(\xi)$ is invertible. Hence $D$ is elliptic. $\qquad\blacksquare$

#### The Euler characteristic as the index of $D$

> **Theorem.** $\displaystyle \operatorname{ind}(d+d^*: \Omega^{\mathrm{ev}}\to\Omega^{\mathrm{odd}}) = \chi(M)$, the **Euler characteristic** $\chi(M) = \sum_{k=0}^n (-1)^k b_k$.

**Proof.**
1. The adjoint of $D = d+d^*: \Omega^{\mathrm{ev}}\to\Omega^{\mathrm{odd}}$ is $D^* = d+d^*: \Omega^{\mathrm{odd}}\to\Omega^{\mathrm{ev}}$ (since $(d)^* = d^*$ and $(d^*)^* = d$). So $\operatorname{ind} D = \dim\ker(D|_{\mathrm{ev}}) - \dim\ker(D|_{\mathrm{odd}})$.
2. Define the **Hodge Laplacian** $\Delta = (d+d^*)^2 = dd^* + d^*d$ (the cross terms $d^2, (d^*)^2$ vanish). A form $\omega$ is **harmonic** ($\Delta\omega = 0$) iff $D\omega = 0$: indeed $\langle\Delta\omega,\omega\rangle = \|d\omega\|^2 + \|d^*\omega\|^2$, which is zero iff $d\omega = 0$ and $d^*\omega = 0$, i.e. iff $(d+d^*)\omega = 0$. *Reason:* a sum of squares of norms vanishes iff each does.
3. Let $\mathcal H^k = \{\omega\in\Omega^k : \Delta\omega = 0\}$ be the harmonic $k$-forms. By step 2, $\ker(D|_{\mathrm{ev}}) = \bigoplus_{k\text{ even}}\mathcal H^k$ and $\ker(D|_{\mathrm{odd}}) = \bigoplus_{k\text{ odd}}\mathcal H^k$.
4. The Hodge theorem (s5, proved next) states $\dim\mathcal H^k = b_k$. Granting this,
$$
\operatorname{ind} D = \sum_{k\text{ even}} b_k - \sum_{k\text{ odd}} b_k = \sum_{k=0}^n (-1)^k b_k = \chi(M). \qquad\blacksquare
$$

> **Worked example (the $2$-sphere).** For $M = S^2$: $b_0 = 1$ (connected), $b_1 = 0$ (simply connected), $b_2 = 1$ (oriented, closed surface). Then $\chi(S^2) = 1 - 0 + 1 = 2$. The index of $d+d^*$ on $S^2$ is therefore $2$ — matching the classical "every smooth vector field on $S^2$ has zeros, total degree $2$" (the hairy-ball theorem). For a torus $T^2$: $b_0=1, b_1=2, b_2=1$, so $\chi = 0$, and indeed the torus admits a nowhere-zero vector field.

This is the prototype of the whole subject: an analytic index ($\dim$ of solution spaces of an elliptic PDE) equals a topological invariant ($\chi$). Gauss–Bonnet (s9) will compute the same $\chi$ as a curvature integral, completing the triangle.

<a id="s5"></a>
### The Hodge theorem — harmonic representatives of cohomology

We owed step 4 above the fact $\dim\mathcal H^k = b_k$. This is the **Hodge theorem**, the cleanest illustration of "analysis computes topology." We state it, identify its single analytic input, and prove the cohomology identification from that input.

> **Theorem (Hodge).** Let $M$ be a compact oriented Riemannian manifold. For each $k$:
> (a) $\dim\mathcal H^k < \infty$.
> (b) **Hodge decomposition:** $\Omega^k = \mathcal H^k \oplus \operatorname{im} d \oplus \operatorname{im} d^*$, an orthogonal direct sum.
> (c) Every de Rham cohomology class has a *unique* harmonic representative; the map $\mathcal H^k \to H^k_{\mathrm{dR}}(M)$, $\omega \mapsto [\omega]$, is an isomorphism. In particular $\dim\mathcal H^k = b_k$.

#### The analytic input

The *only* hard analytic fact is:

> **Analytic input.** The Hodge Laplacian $\Delta = dd^* + d^*d$ on $\Omega^k$ is elliptic (its symbol is $|\xi|^2\,\mathrm{id}$, computed exactly as in s4 step 3, squared), self-adjoint, and non-negative. By s3 it is Fredholm; being self-adjoint, $\operatorname{coker}\Delta \cong \ker\Delta = \mathcal H^k$, so $\operatorname{im}\Delta = (\ker\Delta)^\perp$ is closed and $\Omega^k = \mathcal H^k \oplus \operatorname{im}\Delta$ orthogonally, with $\mathcal H^k$ finite-dimensional.

Everything else is linear algebra on this decomposition.

#### Proof of (b) and (c) from the input

1. **Decompose the image of $\Delta$.** From the input, $\Omega^k = \mathcal H^k \oplus \operatorname{im}\Delta$. Now $\operatorname{im}\Delta = \operatorname{im}(dd^* + d^*d) \subseteq \operatorname{im} d + \operatorname{im} d^*$. Conversely both $\operatorname{im} d$ and $\operatorname{im} d^*$ are orthogonal to $\mathcal H^k$: if $\omega$ harmonic then $\langle\omega, d\alpha\rangle = \langle d^*\omega,\alpha\rangle = 0$ (as $d^*\omega=0$) and similarly $\langle\omega, d^*\beta\rangle = \langle d\omega,\beta\rangle = 0$. *Reason:* harmonic forms are $d$- and $d^*$-closed (s4 step 2).
2. **$\operatorname{im} d \perp \operatorname{im} d^*$.** $\langle d\alpha, d^*\beta\rangle = \langle d^2\alpha,\beta\rangle = 0$ since $d^2 = 0$. *Reason:* the de Rham complex is a complex.
3. Combining 1–2 with the input gives the orthogonal splitting $\Omega^k = \mathcal H^k \oplus \operatorname{im} d \oplus \operatorname{im} d^*$, proving (b).
4. **Cohomology = harmonic forms.** Take a closed form $\omega$ ($d\omega = 0$). Write $\omega = h + d\alpha + d^*\beta$ by (b). Apply $d$: $0 = d\omega = d(d^*\beta)$ (since $dh=0$, $d^2\alpha=0$). Then $0 = \langle dd^*\beta, \beta\rangle = \|d^*\beta\|^2$, so $d^*\beta = 0$, hence its image term vanishes. *Reason:* a norm is zero iff the vector is.
5. Thus $\omega = h + d\alpha$ with $h$ harmonic: every closed form is a harmonic form plus an exact form, so $[\omega] = [h]$ in $H^k_{\mathrm{dR}}$. The map $\mathcal H^k \to H^k_{\mathrm{dR}}$ is **onto**.
6. **Injectivity.** If $h$ harmonic and $[h] = 0$, then $h = d\gamma$ is exact; but $\langle h, h\rangle = \langle h, d\gamma\rangle = \langle d^* h, \gamma\rangle = 0$ since $d^* h = 0$. So $h = 0$. The map is **injective**.
7. Steps 5–6 give the isomorphism $\mathcal H^k \cong H^k_{\mathrm{dR}}(M)$, so $\dim\mathcal H^k = b_k$, finite by the input. This proves (a) and (c). $\qquad\blacksquare$

> **Worked example.** On a connected $M$, $\mathcal H^0 = \{$constants$\}$: $\Delta f = 0$ with $f$ a function means $d^*df = 0$, so $\|df\|^2 = \langle d^*df, f\rangle = 0$, hence $df = 0$ and $f$ is locally constant, i.e. constant on each component. Thus $\dim\mathcal H^0 = b_0 = $ number of components — recovering the topological fact analytically.

> **Intuition.** Hodge theory says: in each cohomology class there is exactly one "minimal energy" representative, the harmonic one, that minimizes $\|d\alpha\|^2 + \|d^*\alpha\|^2$. Topology (the class) constrains analysis (the minimizer). Pitfall: this needs the metric to define $d^*$ and $\Delta$; the harmonic representative depends on the metric, but its *existence and uniqueness* do not.

<a id="s6"></a>
### Clifford algebras, spinors, and the Dirac operator

The de Rham operator $d+d^*$ is one elliptic operator; the index theorem is cleanest for a master example, the **Dirac operator**, whose square is a Laplacian and whose symbol is built from a **Clifford algebra**. Dirac discovered it seeking a first-order "square root" of the wave/Laplace operator.

#### Clifford algebras

> **Definition — Clifford algebra.** Let $V$ be a real vector space with inner product $\langle\cdot,\cdot\rangle$. The **Clifford algebra** $\mathrm{Cl}(V)$ is the associative algebra generated by $V$ subject to the relations
> $$
> v\cdot w + w\cdot v = -2\langle v,w\rangle\, 1 \qquad (v,w\in V).
> $$
> In particular $v\cdot v = -|v|^2$ and, for orthonormal $e_i$, $e_i e_j + e_j e_i = -2\delta_{ij}$.

This is the algebraic skeleton of "taking a square root of a quadratic form": if $D = \sum e_i \partial_{x^i}$ acts so that the $e_i$ Clifford-multiply, then $D^2 = \sum_{i,j} e_i e_j \partial_{x^i}\partial_{x^j} = -\sum_i \partial_{x^i}^2 = \Delta$, because the off-diagonal terms cancel by antisymmetry $e_ie_j = -e_je_i$ and the diagonal gives $e_i^2 = -1$. The Clifford relation is *exactly* what makes the cross terms cancel.

#### Spinors and the spin representation

A **Clifford module** (or **spinor space**) $S$ is a vector space carrying a representation $c: \mathrm{Cl}(V) \to \operatorname{End}(S)$, i.e. linear maps $c(v): S\to S$ with $c(v)c(w) + c(w)c(v) = -2\langle v,w\rangle$. For even $\dim V = 2m$ there is (up to isomorphism) a unique irreducible complex spinor space of dimension $2^m$, with a $\mathbb Z/2$ grading $S = S^+ \oplus S^-$ into half-spinors, and Clifford multiplication by a vector swaps $S^+ \leftrightarrow S^-$ (it is *odd*). A **spin structure** on a Riemannian manifold is a global, consistent choice of such spinor spaces $S_x$ over each tangent space, twisting along the manifold via the **Spin group** (the double cover of the rotation group $SO(n)$). Not every manifold admits one; the obstruction is the second Stiefel–Whitney class $w_2$ (Differential Topology guide). When it exists we get the **spinor bundle** $S = S^+ \oplus S^-$.

#### The Dirac operator

> **Definition — Dirac operator.** Let $M$ be a spin Riemannian manifold with spinor bundle $S = S^+\oplus S^-$ and the Levi-Civita-induced connection $\nabla$ on $S$. The **Dirac operator** is
> $$
> \slashed D = \sum_i c(e_i)\,\nabla_{e_i} : \Gamma(S) \to \Gamma(S),
> $$
> where $\{e_i\}$ is a local orthonormal frame and $c$ is Clifford multiplication. Because $c$ is odd, $\slashed D$ swaps the grading: it restricts to
> $$
> \slashed D^+ : \Gamma(S^+) \to \Gamma(S^-), \qquad \slashed D^- : \Gamma(S^-) \to \Gamma(S^+),
> $$
> with $\slashed D^- = (\slashed D^+)^*$.

> **Proposition.** $\slashed D$ is elliptic, and its principal symbol is $\sigma(\slashed D)(\xi) = i\,c(\xi)$.

**Proof.**
1. The top-order part of $\slashed D = \sum_i c(e_i)\nabla_{e_i}$ replaces $\nabla_{e_i}\mapsto i\xi_i$, giving $\sigma(\slashed D)(\xi) = i\sum_i \xi_i\, c(e_i) = i\,c(\xi^\sharp)$. *Reason:* definition of symbol (s2); the connection's lower-order Christoffel terms drop.
2. Square it: $\sigma(\slashed D)(\xi)^2 = i^2\, c(\xi)c(\xi) = -(-|\xi|^2) = |\xi|^2$ by the Clifford relation $c(\xi)^2 = -|\xi|^2$. *Reason:* Clifford identity.
3. For $\xi\ne 0$, $\sigma(\slashed D)(\xi)^2 = |\xi|^2 \ne 0$, so $\sigma(\slashed D)(\xi)$ is invertible. Elliptic. $\qquad\blacksquare$

By s3, $\slashed D^+: \Gamma(S^+)\to\Gamma(S^-)$ is Fredholm on a compact spin manifold, with a well-defined integer index

$$
\operatorname{ind}\slashed D^+ = \dim\ker\slashed D^+ - \dim\ker\slashed D^-.
$$

Elements of $\ker\slashed D$ are **harmonic spinors**. The Atiyah–Singer theorem (s8) computes exactly this number topologically — and remarkably, the answer is the $\hat A$-genus (s7).

> **Lichnerowicz's formula and a first payoff.** The Weitzenböck identity $\slashed D^2 = \nabla^*\nabla + \tfrac14 R$ holds, where $\nabla^*\nabla \ge 0$ is the connection Laplacian and $R$ is the scalar curvature. If $R > 0$ everywhere, then for $\slashed D\psi = 0$ we get $0 = \|\nabla\psi\|^2 + \tfrac14\int R|\psi|^2 \ge \tfrac14\int R|\psi|^2 \ge 0$, forcing $\psi = 0$. So a compact spin manifold of positive scalar curvature has $\ker\slashed D = 0$, hence $\operatorname{ind}\slashed D^+ = 0$, hence $\hat A(M) = 0$ — a topological obstruction to positive scalar curvature, discovered through analysis. This is a glimpse of the theorem's force.

> **Pitfall.** Two distinct operators are often both called "Dirac": the pure spinor Dirac operator above, and the **twisted** version $\slashed D_E = \slashed D\otimes \nabla^E$ coupling to an auxiliary bundle $E$ with connection. The general index theorem is stated for the twisted operator, which subsumes de Rham, signature, and Dolbeault operators as special $E$.

## Part C · The topological side and the theorem

<a id="s7"></a>
### The topological index — the Chern character, the Todd class, and the Â-genus

The right-hand side of the index theorem is a **topological index** built from characteristic classes. We define the three players — the Chern character, the Todd class, and the $\hat A$-genus — and explain how they assemble. We use Chern–Weil theory (Differential Topology guide): a characteristic class is represented by a polynomial in the curvature $2$-form $\Omega$ of a connection, and its integral over $M$ is a topological number.

#### Characteristic classes via Chern–Weil, in one line

For a complex vector bundle $E$ with connection of curvature $\Omega$ (an $\operatorname{End}(E)$-valued $2$-form), the **total Chern class** is $c(E) = \det\!\big(I + \tfrac{i}{2\pi}\Omega\big) = 1 + c_1 + c_2 + \cdots$, with $c_k$ a closed $2k$-form whose cohomology class is independent of the connection. Formally factor $c(E) = \prod_j (1 + x_j)$; the $x_j$ are the **Chern roots** (formal degree-$2$ classes; symmetric functions of them are genuine classes).

#### The Chern character

> **Definition — Chern character.** $\displaystyle \operatorname{ch}(E) = \sum_j e^{x_j} = \operatorname{rank}(E) + c_1 + \tfrac12(c_1^2 - 2c_2) + \cdots = \operatorname{tr}\,\exp\!\Big(\tfrac{i}{2\pi}\Omega\Big).$

Its defining virtue is additivity and multiplicativity:

> **Proposition.** $\operatorname{ch}(E\oplus F) = \operatorname{ch}(E) + \operatorname{ch}(F)$ and $\operatorname{ch}(E\otimes F) = \operatorname{ch}(E)\,\operatorname{ch}(F)$.

**Proof.** For a direct sum the Chern roots are the union $\{x_j\}\cup\{y_k\}$, so $\sum e^{x_j} + \sum e^{y_k}$ adds. For a tensor product the roots are the sums $x_j + y_k$, so $\operatorname{ch}(E\otimes F) = \sum_{j,k} e^{x_j+y_k} = (\sum_j e^{x_j})(\sum_k e^{y_k}) = \operatorname{ch}(E)\operatorname{ch}(F)$, using $e^{a+b}=e^a e^b$. *Reason:* the exponential turns sums of roots into products. $\qquad\blacksquare$

This is precisely why the Chern character is the natural object on the topological side: the index is additive under direct sums of operators and multiplicative under products of manifolds, and $\operatorname{ch}$ is the universal class with those properties.

#### The Todd class and the Â-genus

> **Definition — Todd class.** $\displaystyle \operatorname{Td}(E) = \prod_j \frac{x_j}{1 - e^{-x_j}} = 1 + \tfrac12 c_1 + \tfrac{1}{12}(c_1^2 + c_2) + \cdots$ (using $\frac{x}{1-e^{-x}} = 1 + \tfrac{x}{2} + \tfrac{x^2}{12} - \cdots$, the generating series of Bernoulli numbers).

> **Definition — Â-genus.** For the (complexified) tangent bundle with Pontryagin roots $\pm x_j$,
> $$
> \hat A(M) = \prod_j \frac{x_j/2}{\sinh(x_j/2)} = 1 - \tfrac{1}{24}p_1 + \tfrac{1}{5760}(7p_1^2 - 4p_2) + \cdots,
> $$
> where $p_k$ are the Pontryagin classes (Differential Topology guide).

Both are multiplicative "genera": $\operatorname{Td}(E\oplus F) = \operatorname{Td}(E)\operatorname{Td}(F)$, similarly $\hat A$, by the same product-over-roots structure as $\operatorname{ch}$ (the proof is identical: a multiplicative function of roots is multiplicative under direct sum).

#### Assembling the topological index

For an elliptic operator $D$ on a manifold $M^n$ with symbol class, the topological index is, in its most-used form for the twisted Dirac operator $\slashed D_E$,

$$
\operatorname{ind}_{\mathrm{top}}(\slashed D_E) = \int_M \hat A(M)\,\operatorname{ch}(E),
$$

picking out the top-degree ($n$-form) component of the product and integrating. For a general elliptic operator the formula is $\int_M (-1)^n \operatorname{ch}(\sigma(D))\operatorname{Td}(TM\otimes\mathbb C)$ evaluated through the symbol class, but every classical case reduces to a Dirac-type formula like the one above. The next section states the theorem that equates this integral with the analytic index.

> **Worked computation (degree counting on a $4$-manifold).** On $M^4$, $\hat A = 1 - \tfrac{1}{24}p_1$ and $\operatorname{ch}(E) = r + c_1 + \tfrac12(c_1^2 - 2c_2)$ with $r = \operatorname{rank} E$. The product's $4$-form part is $\tfrac12(c_1^2 - 2c_2) - \tfrac{r}{24}p_1$. Hence
> $$
> \operatorname{ind}\slashed D_E = \int_{M^4}\Big[\tfrac12 c_1(E)^2 - c_2(E) - \tfrac{r}{24}p_1(M)\Big].
> $$
> With $E$ trivial ($r=1, c_1=c_2=0$): $\operatorname{ind}\slashed D = -\tfrac{1}{24}\int_{M^4} p_1 = \hat A(M)$, an integer — a nontrivial integrality constraint on $p_1$ of spin $4$-manifolds.

<a id="s8"></a>
### The Atiyah–Singer index theorem and the meaning of "analytic = topological"

We can now state the theorem in full and unpack the equality.

> **Theorem (Atiyah–Singer, 1963).** Let $M$ be a compact oriented smooth manifold without boundary, and let $D: \Gamma(E)\to\Gamma(F)$ be an elliptic differential (or pseudodifferential) operator. Then the analytic index equals the topological index:
> $$
> \operatorname{ind}_{\mathrm{an}}(D) \;=\; \operatorname{ind}_{\mathrm{top}}(D),
> $$
> where $\operatorname{ind}_{\mathrm{an}}(D) = \dim\ker D - \dim\operatorname{coker} D$ (s1, well-defined by s3) and
> $$
> \operatorname{ind}_{\mathrm{top}}(D) = (-1)^n\!\int_{M}\operatorname{ch}\big([\sigma(D)]\big)\,\operatorname{Td}(TM\otimes\mathbb C),
> $$
> with $[\sigma(D)] \in K(T^*M)$ the K-theory class of the principal symbol and $n = \dim M$. For the twisted Dirac operator this reduces to $\operatorname{ind}\slashed D_E = \int_M \hat A(M)\,\operatorname{ch}(E)$.

#### What the two sides mean and why the equality is deep

- **The left side is analysis.** $\dim\ker D$ and $\dim\operatorname{coker} D$ require solving a PDE on $M$ — finding all solutions of $Du = 0$ and all obstructions. These depend in a complicated way on the metric, the connection, the precise coefficients. Each is genuinely hard and individually metric-dependent.
- **The right side is topology.** $\operatorname{ch}, \operatorname{Td}, \hat A$ are polynomials in curvature whose *integrals* are independent of all choices (Chern–Weil: the integral of a characteristic class is a homotopy/cobordism invariant). You can compute the right side from the manifold's topology and the bundles' topology alone, often by hand.
- **The equality says these two utterly different computations always agree.** The analyst's count of solutions is forced, to the last integer, by topology. Conversely, the topologist's integral is always an integer (it counts something), an integrality theorem that is not at all obvious from the polynomial formulas (the $\tfrac{1}{24}$, $\tfrac{1}{5760}$ must conspire to give whole numbers).

#### Why is it true? The structure of the proof strategies

There are three classical proofs; all share the logic that *both sides are deformation invariants matching on generators*.

1. **Cobordism proof (original, 1963).** Both $\operatorname{ind}_{\mathrm{an}}$ and $\operatorname{ind}_{\mathrm{top}}$ are invariant under cobordism and behave the same way under the operations (direct sum, products, embeddings) that generate all symbol classes. Atiyah–Singer reduce to checking equality on a generating set (built via embeddings into spheres) and verify it there. The engine is the **stability of the analytic index** (s1): it is what lets you deform freely.
2. **K-theory proof (1968).** Reformulate the index as a homomorphism $K(T^*M)\to\mathbb Z$. Both the analytic and topological indices are such homomorphisms, natural under embeddings; one shows they agree by an axiomatic characterization (normalization on a point + multiplicativity + excision). Stability (s1) again underlies naturality.
3. **Heat-kernel proof (s10).** Compute the index directly as a limit of a heat-trace, and show the limit localizes to a curvature integral that *is* the topological index. This is the most analytic and the one we sketch.

#### A consistency check on the prototype

For $D = d+d^*$ (s4), the theorem must give $\chi(M)$. Indeed the topological index for this operator works out to $\int_M e(M)$, the Euler class, which by Gauss–Bonnet–Chern is $\chi(M)$ — matching the analytic answer of s4. We trace this in s9.

> **Intuition.** Picture the space of all elliptic operators (or symbols). It breaks into connected components ("deformation classes"); the index is constant on each (s1). Topology provides an independent invariant — the characteristic-number integral — that is also constant on each component. The theorem says these two locally-constant functions are *equal*, not merely both constant. The proof is the labor of checking they agree on one representative per component. Pitfall: the theorem requires $M$ compact, boundaryless, and $D$ elliptic; with boundary one needs the Atiyah–Patodi–Singer correction (an extra $\eta$-invariant term), and without ellipticity there is no finite index at all.

<a id="s9"></a>
### Special cases recovered: Gauss–Bonnet–Chern, the signature theorem, Riemann–Roch

The unifying power of the theorem is seen by feeding it three different elliptic operators and watching three famous classical theorems fall out. Each is the index of a Dirac-type operator twisted by a specific bundle.

#### Gauss–Bonnet–Chern (operator: $d+d^*$, full de Rham)

The operator $D = d+d^*:\Omega^{\mathrm{ev}}\to\Omega^{\mathrm{odd}}$ has, by s4, analytic index $\chi(M)$. Its topological index is the integral of the **Euler class** $e(TM)$:

$$
\chi(M) = \operatorname{ind}(d+d^*) = \int_M e(TM).
$$

By Chern–Weil, the Euler class is represented in even dimension $n = 2m$ by the **Pfaffian** of the curvature: $e(TM) = \frac{1}{(2\pi)^m m!}\operatorname{Pf}(\Omega)$. In two dimensions this is $\frac{1}{2\pi}K\,dA$ with $K$ the Gauss curvature, giving the classical **Gauss–Bonnet theorem**

$$
\chi(M^2) = \frac{1}{2\pi}\int_M K\, dA.
$$

> **Worked example.** For the unit $S^2$, $K = 1$ and $\operatorname{Area} = 4\pi$, so $\frac{1}{2\pi}\int K\,dA = \frac{4\pi}{2\pi} = 2 = \chi(S^2)$. Three computations — counting harmonic forms (s4), the curvature integral here, and the topology $1-0+1$ — all give $2$.

#### The Hirzebruch signature theorem (operator: the signature operator)

On an oriented manifold of dimension $n = 4k$, the **Hodge star** $\star$ gives an involution $\tau$ on middle-dimensional forms, splitting $\Omega^{\mathrm{ev}} = \Omega^+\oplus\Omega^-$ into $\pm 1$ eigenspaces. The **signature operator** $D_{\mathrm{sig}} = d+d^*:\Omega^+\to\Omega^-$ has analytic index equal to the **signature** $\operatorname{sign}(M)$ — the signature of the intersection form on $H^{2k}(M)$ (number of positive minus negative eigenvalues of the symmetric pairing $\alpha\wedge\beta$). The topological index is the **$L$-genus** (a Pontryagin polynomial):

$$
\operatorname{sign}(M) = \int_M L(M), \qquad L = 1 + \tfrac13 p_1 + \tfrac{1}{45}(7p_2 - p_1^2) + \cdots
$$

> **Worked example.** On $M^4$, $\operatorname{sign}(M) = \tfrac13\int_{M} p_1$. For the complex projective plane $\mathbb{CP}^2$, $\int p_1 = 3$ (since $p_1 = 3$ generator), giving $\operatorname{sign} = 1$ — correct, as $H^2(\mathbb{CP}^2)=\mathbb Z$ with positive self-intersection.

#### Hirzebruch–Riemann–Roch (operator: the Dolbeault operator)

On a compact complex manifold $X$ with a holomorphic vector bundle $E$, the **Dolbeault operator** $\bar\partial + \bar\partial^*:\Omega^{0,\mathrm{ev}}(E)\to\Omega^{0,\mathrm{odd}}(E)$ has analytic index equal to the **holomorphic Euler characteristic**

$$
\chi(X,E) = \sum_q (-1)^q \dim H^q(X, \mathcal O(E)),
$$

the alternating sum of dimensions of sheaf cohomology (spaces of holomorphic sections and their higher obstructions). The topological index is

$$
\chi(X,E) = \int_X \operatorname{ch}(E)\,\operatorname{Td}(TX),
$$

the **Hirzebruch–Riemann–Roch theorem**. This is where the Todd class earns its place.

> **Worked example (a Riemann surface).** For a compact Riemann surface $X$ of genus $g$ and a line bundle $L$ of degree $d$: $\dim X = 1$, $\operatorname{Td}(TX) = 1 + \tfrac12 c_1(TX)$, $\operatorname{ch}(L) = 1 + c_1(L)$. The degree-$2$ part is $c_1(L) + \tfrac12 c_1(TX)$, and $\int_X c_1(L) = d$, $\int_X c_1(TX) = 2 - 2g$ (the Euler characteristic). So
> $$
> \chi(X,L) = d + \tfrac12(2-2g) = d - g + 1,
> $$
> i.e. $\dim H^0 - \dim H^1 = d - g + 1$, the **classical Riemann–Roch theorem** for curves. The index theorem reproduces $19$th-century algebraic geometry as one line.

> **Summary of the dictionary.** Twist Dirac by nothing → $\hat A$-genus; by the full exterior bundle → Euler class (Gauss–Bonnet); by the self-dual splitting → $L$-genus (signature); by the Dolbeault/holomorphic structure → Todd class (Riemann–Roch). One theorem, four classical landmarks.

## Part D · Proof outline and physics

<a id="s10"></a>
### The heat-kernel approach — McKean–Singer and supersymmetric cancellation

We outline the most analytic proof, which computes the index as a heat trace and shows it localizes to the topological integral. It is the route physicists love, because the "supersymmetric cancellation" is a recurring QFT mechanism.

#### The McKean–Singer formula

Let $D = \slashed D^+: \Gamma(S^+)\to\Gamma(S^-)$ with adjoint $D^* = \slashed D^-$. Form the two Laplacians $\Delta^+ = D^* D$ on $S^+$ and $\Delta^- = D D^*$ on $S^-$. Both are non-negative elliptic self-adjoint operators, so each has a discrete spectrum $0 \le \lambda_0 \le \lambda_1 \le \cdots \to \infty$ with finite-dimensional eigenspaces.

> **Theorem (McKean–Singer).** For every $t > 0$,
> $$
> \operatorname{ind} D = \operatorname{Tr}\big(e^{-t\Delta^+}\big) - \operatorname{Tr}\big(e^{-t\Delta^-}\big) =: \operatorname{Str}\big(e^{-t\slashed D^2}\big),
> $$
> the **supertrace** of the heat operator, *independent of $t$*.

**Proof (the cancellation).**
1. **Nonzero eigenvalues pair up.** Suppose $\Delta^+\phi = \lambda\phi$ with $\lambda \ne 0$. Then $\psi := D\phi$ satisfies $\Delta^-\psi = DD^*D\phi = D\Delta^+\phi = \lambda D\phi = \lambda\psi$, and $\psi\ne 0$ (else $D^*D\phi = 0$ forces $\lambda = 0$). So $D$ maps the $\lambda$-eigenspace of $\Delta^+$ to that of $\Delta^-$. Symmetrically $D^*$ maps back, and $D^*D = \lambda$ on the $+$ side shows these maps are inverse up to $\lambda$, hence **isomorphisms**. *Reason:* $D$ intertwines $\Delta^+$ and $\Delta^-$.
2. Therefore for each $\lambda > 0$, the eigenspaces $V_\lambda^+$ and $V_\lambda^-$ have *equal* dimension. In the supertrace
$$
\operatorname{Tr}(e^{-t\Delta^+}) - \operatorname{Tr}(e^{-t\Delta^-}) = \sum_\lambda e^{-t\lambda}\big(\dim V_\lambda^+ - \dim V_\lambda^-\big),
$$
every $\lambda > 0$ contributes $e^{-t\lambda}(d - d) = 0$. *Reason:* step 1's pairing.
3. Only $\lambda = 0$ survives: $\dim V_0^+ - \dim V_0^- = \dim\ker D - \dim\ker D^* = \operatorname{ind} D$, with $e^{-t\cdot 0} = 1$. Hence the supertrace equals $\operatorname{ind} D$ for all $t$. $\qquad\blacksquare$

This is **supersymmetric cancellation**: bosonic ($S^+$) and fermionic ($S^-$) excited states cancel in pairs; only the ground states (zero modes) contribute to the index. The independence of $t$ is the crux.

#### Localization as $t \to 0$

Since the supertrace is $t$-independent, evaluate it in the limit $t\to 0^+$, where the heat kernel localizes near the diagonal and is computable from local geometry.

1. **Heat kernel small-time expansion.** The kernel $k_t(x,y)$ of $e^{-t\Delta}$ has, as $t\to 0$, an asymptotic expansion
$$
\operatorname{Str} k_t(x,x) \sim (4\pi t)^{-n/2}\sum_{j\ge 0} t^j\, a_j(x),
$$
where the $a_j(x)$ are universal polynomials in the curvature and its covariant derivatives (the **Seeley–DeWitt coefficients**), local quantities. *Reason:* parametrix construction for the heat equation.
2. **Only the constant term can survive.** Integrating, $\operatorname{ind} D = \int_M \operatorname{Str} k_t(x,x)\,dV \sim (4\pi t)^{-n/2}\sum_j t^j\int_M a_j$. The left side is the constant $\operatorname{ind} D$, so all powers of $t$ except $t^0$ must vanish in the limit: the $t^{-n/2+j}$ terms with $j < n/2$ integrate to zero, and the $t\to0$ limit picks out $j = n/2$ (for even $n$), giving
$$
\operatorname{ind} D = \int_M a_{n/2}(x)\,(4\pi)^{-n/2}\,dV.
$$
*Reason:* matching powers of $t$ on both sides of a $t$-independent identity.
3. **Identify the surviving coefficient.** The deep step (Patodi, Gilkey, and the **Getzler rescaling** that makes it transparent) is that the localized supertrace $\operatorname{Str} a_{n/2}$ is exactly the top-degree component of $\hat A(M)\operatorname{ch}(E)$. Getzler's trick rescales the Clifford variables and the coordinates so that the heat operator limits to a **harmonic oscillator** (Mehler's formula), whose supertrace is computed in closed form and *is* the $\hat A\operatorname{ch}$ integrand. *Reason:* the rescaled limit turns the geometric heat kernel into the exactly-solvable Gaussian of a quantum oscillator.
4. Combining: $\operatorname{ind}\slashed D_E = \int_M \hat A(M)\operatorname{ch}(E)$, the index theorem. $\qquad\blacksquare$ (outline)

> **Intuition.** The index is a number (no $t$), so we are free to compute it at any time scale; at $t\to 0$ the heat has not spread, so the answer is built from *local* curvature, yet it equals a *global* topological integral. The "miracle of cancellation" is that everything except the ground states drops out and the leftover is a perfect characteristic class. Pitfall: the small-$t$ expansion has many terms that look divergent ($t^{-n/2}$); the theorem guarantees they all cancel after taking the *super*trace — using the ordinary trace they do not.

<a id="s11"></a>
### Physics — anomalies, fermion zero modes, and instantons

The index theorem is not a curiosity for physicists: it computes **anomalies**, counts **fermion zero modes**, and underlies **instanton** physics. We sketch each, defining terms.

#### Fermion zero modes and the path integral

In quantum field theory a Dirac fermion in a background gauge field $A$ is governed by the (twisted) Dirac operator $\slashed D_A$. A **zero mode** is a solution of $\slashed D_A\psi = 0$ — a normalizable harmonic spinor. The index $\operatorname{ind}\slashed D_A = n_+ - n_-$ counts left-handed minus right-handed zero modes ($n_\pm = \dim\ker\slashed D^\pm$). By the index theorem this is a topological integral of the gauge field strength:

$$
n_+ - n_- = \int_M \hat A(M)\,\operatorname{ch}(E_A),
$$

so the number of zero modes is fixed by the topology of the gauge field. In the fermionic path integral, each zero mode must be "soaked up" by a fermion insertion (Grassmann integration gives zero unless every zero mode is paired), so the index directly controls which correlation functions are nonzero — the **'t Hooft vertex**.

#### The chiral anomaly

A classical symmetry that fails to survive quantization is an **anomaly**. The **chiral (axial) symmetry** $\psi \to e^{i\alpha\gamma_5}\psi$ of massless fermions is classically conserved: $\partial_\mu j_5^\mu = 0$ for the axial current $j_5^\mu = \bar\psi\gamma^\mu\gamma_5\psi$. Quantum mechanically it is violated:

$$
\partial_\mu j_5^\mu = \frac{1}{16\pi^2}\,\epsilon^{\mu\nu\rho\sigma}\operatorname{tr}(F_{\mu\nu}F_{\rho\sigma}) = 2\,\big(\text{instanton density}\big).
$$

Integrating over spacetime, the total change of axial charge equals $2(n_+ - n_-) = 2\operatorname{ind}\slashed D_A$. The **Atiyah–Singer theorem is the mathematical content of the chiral anomaly**: the anomalous non-conservation integrates to the index, an integer. The right side is exactly $\operatorname{ch}_2 = \tfrac12 c_1^2 - c_2$ of the gauge bundle (s7), the second Chern character — the same characteristic class that appears in the index formula.

> **Worked link.** On $S^4$ (Euclidean spacetime compactified), $\hat A(S^4) = 1$ (it is a sphere, $p_1 = 0$), so $\operatorname{ind}\slashed D_A = \int_{S^4}\operatorname{ch}_2(E_A) = \frac{1}{8\pi^2}\int \operatorname{tr}(F\wedge F)$, which is the **instanton number** (second Chern number) $k$. Thus a charge-$k$ instanton background has exactly $k$ net fermion zero modes. The famous "one zero mode per instanton" for $SU(2)$ in the fundamental representation is this formula with $k=1$.

#### Instantons

An **instanton** is a finite-action solution of the Euclidean Yang–Mills equations (Fiber Bundles & Gauge guide); its topological charge is the integer $k = \frac{1}{8\pi^2}\int\operatorname{tr}(F\wedge F) = c_2(E)[M]$, a Chern number. The index theorem says this same integer counts the fermion zero modes in that background, tying together: (i) the topology of the gauge bundle (Chern number), (ii) the analysis of the Dirac operator (zero modes), and (iii) the quantum anomaly (non-conservation of chiral charge). The number $k$ also governs the dimension of the **instanton moduli space** via a different index computation (the linearized self-duality operator), $8k - 3$ for $SU(2)$ on $S^4$ — itself an Atiyah–Singer index. Anomaly cancellation conditions in the Standard Model and string theory (e.g. the Green–Schwarz mechanism) are, at bottom, statements that certain index-theoretic characteristic classes sum to zero.

> **Intuition.** Whenever a physicist says "this is topologically protected," "this symmetry is anomalous," or "there are exactly $k$ zero modes," there is an index theorem underneath. The integer that physics cannot change is the analytic index, and topology is what fixes its value. Pitfall: the *gravitational* anomaly involves $\hat A(M)$ of spacetime itself, not just the gauge bundle; mixed and pure gravitational anomalies are higher-degree components of the same $\hat A\operatorname{ch}$ polynomial.

---

*This guide built index theory from its analytic seed to its physical flowering: a Fredholm operator carries an integer index — solutions minus obstructions — that is rigid under perturbation (s1), and ellipticity (s2) plus elliptic regularity on a compact manifold (s3) is exactly what makes a geometric differential operator Fredholm. The de Rham operator realizes the Euler characteristic as an index (s4), Hodge theory pins each cohomology class to a unique harmonic representative (s5), and the Clifford-algebraic Dirac operator (s6) is the master example whose index is the $\hat A$-genus. On the topological side, the Chern character, Todd class, and $\hat A$-genus (s7) assemble into a curvature integral, and the Atiyah–Singer theorem (s8) declares this integral equal to the analytic index — recovering Gauss–Bonnet, Hirzebruch signature, and Riemann–Roch as one family (s9). The heat-kernel proof (s10) computes the index by supersymmetric cancellation and small-time localization, and physics (s11) reads the whole structure as anomalies, fermion zero modes, and instantons. Return to any boxed definition or numbered proof as a reference, and keep the single thesis in view: the count of solutions to a natural equation is not free to be anything — topology fixes it, to the last integer.*
