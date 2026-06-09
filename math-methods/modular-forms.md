**English** · [中文](modular-forms.zh.md)

# Modular Forms & Number Theory in Physics, *symmetry of the upper half-plane.*

*A self-contained first course in the theory of modular forms — from the simple question "what functions on the upper half-plane look the same after we shuffle their coordinate by an integer matrix?" to Eisenstein series, the discriminant and the $j$-invariant, the valence formula counting zeros, Hecke operators and their eigenforms, theta functions and lattice sums, the Dedekind eta function, $L$-functions and modularity, and finally the role of all this in physics: the modular invariance of partition functions, T-duality, and Eisenstein series in string amplitudes. Every term is defined in words on first use, every formula is motivated, and every derivation is a numbered, gap-free chain of reasons. We assume only basic algebra and single-variable calculus, and we draw on two companion guides: [Complex Analysis](../complex-analysis/complex-analysis.md) for holomorphic functions, Laurent series, and contour integration, and [Group Theory](../group-theory/group-theory.md) for groups, generators, and quotients. Each borrowed fact is restated in one line where it is used.*

[← Back to all guides](../README.md)

## Part A · The stage and its symmetry

<a id="s0"></a>
### Motivation: partition functions, lattice sums, and dualities

#### What this guide is about, in one breath

A **modular form** is a function of one complex variable $\tau$, living in the **upper half-plane** $\mathbb{H}$ (the complex numbers with positive imaginary part), that transforms in a very rigid, prescribed way when $\tau$ is replaced by $\frac{a\tau+b}{c\tau+d}$ for any $2\times2$ integer matrix of determinant $1$. That rigidity is so strong that the space of such functions of a given "weight" is *finite-dimensional* — usually just a handful of dimensions. As a result, two modular forms that agree in a few Taylor coefficients must agree *everywhere*, and this turns deep arithmetic statements into finite checks. The same rigidity is why modular forms appear all over physics: whenever a physical quantity is invariant under a discrete symmetry that acts like an integer matrix — a **duality** — that quantity is forced to be a modular form, and we can pin it down.

#### Three motivating arenas

- **Partition functions on the torus.** In statistical mechanics and quantum field theory the **partition function** $Z$ is the master quantity that encodes all thermodynamic and quantum information; it is a weighted sum over all states of the system. When the underlying space-time is a **torus** (a doughnut surface, the product of two circles), the torus has a *shape* described by a single complex number $\tau$ called the **modular parameter**. Two values of $\tau$ related by an integer matrix describe the *same physical torus* — they are merely two ways of choosing which loop on the doughnut to call "the time direction." Physics cannot depend on this arbitrary choice, so $Z(\tau)$ must be invariant (or nearly invariant) under those matrices: $Z$ is a modular object. This is the **modular invariance** developed in §s11, and it is the central consistency condition of two-dimensional conformal field theory and string theory.

- **Lattice sums.** A **lattice** is a regular grid of points in space — for example all integer combinations $m\,\vec{e}_1 + n\,\vec{e}_2$ of two basis vectors. Sums over a lattice of a quantity like $e^{-t\,|\vec v|^2}$ (a Gaussian weight) appear in counting energy levels, in computing Casimir energies, and in number theory when we ask "in how many ways is an integer a sum of squares?" These sums are **theta functions** (§s8), and they are modular forms. The bridge that proves their modularity is the **Poisson summation formula**, a statement that summing a function over a lattice equals summing its Fourier transform over the dual lattice.

- **Dualities.** A **duality** is an exact equivalence between two descriptions of the same physics that look different on the surface — for instance a theory at radius $R$ being identical to one at radius $1/R$ (**T-duality**, §s11), or a theory at coupling $g$ being identical to one at coupling $1/g$ (S-duality, also called electric–magnetic duality). When dualities combine, they often generate exactly the group of integer matrices $SL(2,\mathbb{Z})$, and the physical observables become modular forms or functions of the duality parameter. The numbers that count black-hole microstates in string theory, for instance, are coefficients of modular forms.

#### The whole guide on one line

> upper half-plane $\mathbb{H}$ → action of $SL(2,\mathbb{Z})$ by Möbius maps → fundamental domain & generators $S,T$ → modular forms of weight $k$ → Eisenstein series & $q$-expansions → $\Delta$, $j$, the graded ring → valence formula → Hecke operators & eigenforms → theta functions & Poisson summation → Dedekind $\eta$ & the CFT partition function → $L$-functions & modularity → physics

#### Common pitfalls

- "Modular" here has nothing to do with modular *arithmetic* (clock arithmetic); the word refers to the **moduli** (shape parameters) of a torus.
- A modular form is *not* invariant — it picks up a factor $(c\tau+d)^k$. Only the weight-zero **modular functions** (like $j$) are genuinely invariant. Keeping track of that factor is the whole game.

<a id="s1"></a>
### The modular group $SL(2,\mathbb{Z})$ acting on $\mathbb{H}$

#### What & why

We first build the stage and the actors. The stage is the upper half-plane $\mathbb{H}$. The actors are the integer matrices of determinant $1$, and the way they "act" is by **Möbius transformations** (fractional-linear maps). We must check three things carefully: that these maps send $\mathbb{H}$ into itself, that they form a group, and that two specific matrices act identically, which forces us to pass to a quotient group.

#### Definitions

> **Definition — upper half-plane.** $\mathbb{H} = \{\tau \in \mathbb{C} : \operatorname{Im}\tau > 0\}$, the set of complex numbers $\tau = x + iy$ with $y>0$. We write $\operatorname{Im}\tau$ for the imaginary part $y$ and $\operatorname{Re}\tau$ for the real part $x$.

> **Definition — the modular group.** $SL(2,\mathbb{Z})$ is the set of $2\times 2$ matrices $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ with **integer** entries $a,b,c,d$ and **determinant** $ad-bc=1$. ("$SL$" stands for *special* — determinant one — *linear* group; "$\mathbb{Z}$" because the entries are integers.) It is a group under matrix multiplication, with identity $I=\begin{pmatrix}1&0\\0&1\end{pmatrix}$.

> **Definition — the action by Möbius transformation.** A matrix $\gamma = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ acts on $\tau$ by
> $$
> \gamma\cdot\tau \;=\; \frac{a\tau + b}{c\tau + d}.
> $$
> This is called a **Möbius** (or **fractional-linear**) transformation.

(Restated prerequisite from [Group Theory](../group-theory/group-theory.md): a **group** is a set with an associative product, an identity, and inverses. A group **acts** on a set $X$ if each group element $g$ gives a map $X\to X$ with $I$ acting as the identity map and $(gh)\cdot x = g\cdot(h\cdot x)$.)

#### Theorem 1 — the action is well-defined: $\mathbb{H}\to\mathbb{H}$

**Claim.** If $\tau\in\mathbb{H}$ and $\gamma\in SL(2,\mathbb{Z})$, then $\gamma\cdot\tau\in\mathbb{H}$.

**Proof (gap-free).**

1. Write $\tau = x+iy$ with $y=\operatorname{Im}\tau>0$. Compute the imaginary part of $\gamma\cdot\tau$. Multiply numerator and denominator by the complex conjugate $\overline{c\tau+d}=c\bar\tau+d$:
   $$
   \frac{a\tau+b}{c\tau+d} = \frac{(a\tau+b)(c\bar\tau+d)}{|c\tau+d|^2}.
   $$
   *(Reason: $\frac{z}{w}=\frac{z\bar w}{|w|^2}$, the standard rationalization of a complex denominator, valid because $|w|^2=w\bar w$ is real and positive when $w\ne0$.)*
2. Expand the numerator: $(a\tau+b)(c\bar\tau+d) = ac\,|\tau|^2 + ad\,\tau + bc\,\bar\tau + bd$. Its imaginary part: $|\tau|^2$ and $bd$ are real (contribute $0$); $\operatorname{Im}(ad\,\tau)=ad\,y$ and $\operatorname{Im}(bc\,\bar\tau)=-bc\,y$. So
   $$
   \operatorname{Im}\big((a\tau+b)(c\bar\tau+d)\big) = (ad-bc)\,y.
   $$
   *(Reason: for real $r$, $\operatorname{Im}(r\tau)=r\,y$ and $\operatorname{Im}(r\bar\tau)=-r\,y$, since $\bar\tau=x-iy$.)*
3. Therefore
   $$
   \operatorname{Im}(\gamma\cdot\tau) = \frac{(ad-bc)\,y}{|c\tau+d|^2} = \frac{y}{|c\tau+d|^2},
   $$
   using $ad-bc=1$. *(Reason: definition of $SL(2,\mathbb{Z})$.)*
4. Since $y>0$ and $|c\tau+d|^2>0$ (the denominator is nonzero because if $c\tau+d=0$ then $\tau=-d/c$ would be real, contradicting $y>0$, or $c=d=0$ contradicting $ad-bc=1$), we get $\operatorname{Im}(\gamma\cdot\tau)>0$, i.e. $\gamma\cdot\tau\in\mathbb{H}$. $\blacksquare$

The identity in step 3,
$$
\operatorname{Im}(\gamma\cdot\tau) = \frac{\operatorname{Im}\tau}{|c\tau+d|^2},
$$
will be used constantly; commit it to memory.

#### Theorem 2 — it is a group action; the factor $(c\tau+d)$ composes

The key bookkeeping object is the **automorphy factor** $j(\gamma,\tau) := c\tau+d$, the denominator that appears.

**Claim (cocycle / chain rule).** For $\gamma_1,\gamma_2\in SL(2,\mathbb{Z})$,
$$
j(\gamma_1\gamma_2,\tau) = j(\gamma_1,\gamma_2\cdot\tau)\,j(\gamma_2,\tau).
$$

**Proof.**

1. Let $\gamma_1=\begin{pmatrix}a&b\\c&d\end{pmatrix}$, $\gamma_2=\begin{pmatrix}a'&b'\\c'&d'\end{pmatrix}$. Their product (matrix multiplication) is $\gamma_1\gamma_2=\begin{pmatrix}aa'+bc' & ab'+bd'\\ ca'+dc' & cb'+dd'\end{pmatrix}$.
2. By definition $j(\gamma_1\gamma_2,\tau) = (ca'+dc')\tau + (cb'+dd')$.
3. Compute the right-hand side. $j(\gamma_2,\tau)=c'\tau+d'$ and $\gamma_2\cdot\tau=\frac{a'\tau+b'}{c'\tau+d'}$, so
   $$
   j(\gamma_1,\gamma_2\cdot\tau) = c\cdot\frac{a'\tau+b'}{c'\tau+d'}+d = \frac{c(a'\tau+b')+d(c'\tau+d')}{c'\tau+d'}.
   $$
4. Multiply: $j(\gamma_1,\gamma_2\cdot\tau)\,j(\gamma_2,\tau) = c(a'\tau+b')+d(c'\tau+d') = (ca'+dc')\tau+(cb'+dd')$, which matches step 2. $\blacksquare$

**Consequence — it is an action.** Applying the Möbius formula to a product gives $(\gamma_1\gamma_2)\cdot\tau = \gamma_1\cdot(\gamma_2\cdot\tau)$; this follows because both the numerator and denominator compose the same way (the cocycle handles the denominator; an identical computation handles the numerator). With $I\cdot\tau=\tau$, the axioms of a group action hold.

#### Passing to $PSL(2,\mathbb{Z})$

The matrices $\gamma$ and $-\gamma=\begin{pmatrix}-a&-b\\-c&-d\end{pmatrix}$ give the *same* Möbius map, because numerator and denominator both flip sign and the signs cancel:
$$
\frac{-a\tau-b}{-c\tau-d}=\frac{a\tau+b}{c\tau+d}.
$$
The only scalar matrices in $SL(2,\mathbb{Z})$ are $\pm I$. Hence the group that *genuinely* acts on $\mathbb{H}$ (acts faithfully, i.e. only the identity acts trivially) is the quotient

> **Definition — the projective modular group.** $PSL(2,\mathbb{Z}) := SL(2,\mathbb{Z})/\{\pm I\}$, where we declare $\gamma$ and $-\gamma$ to be the same element. ("$P$" for *projective*, the standard name for quotienting a linear group by its scalars.)

When we discuss the abstract symmetry of $\mathbb{H}$ we mean $PSL(2,\mathbb{Z})$; when weights are *odd* the sign matters and we keep $SL(2,\mathbb{Z})$ — a distinction that will explain in §s3 why odd-weight forms vanish.

#### Worked example

Take $\gamma=\begin{pmatrix}1&3\\1&4\end{pmatrix}$ (check: $1\cdot4-3\cdot1=1$, valid) and $\tau=i$. Then $\gamma\cdot i = \frac{i+3}{i+4} = \frac{(3+i)(4-i)}{|4+i|^2}=\frac{12-3i+4i+1}{17}=\frac{13+i}{17}$, with imaginary part $\frac{1}{17}$. The master formula predicts $\operatorname{Im}=\frac{\operatorname{Im} i}{|i+4|^2}=\frac{1}{17}$ — agreement.

#### Intuition: why integer matrices, and what they "do"

Picture $\tau$ as encoding a **lattice** in the plane: the lattice $\Lambda_\tau$ generated by the two vectors $1$ and $\tau$ (thinking of complex numbers as points of the plane). A different choice of basis for the *same* lattice replaces $(1,\tau)$ by $(c\tau+d,\,a\tau+b)$ for some integer matrix of determinant $\pm1$; dividing through to normalize the first basis vector to $1$ gives exactly $\tau\mapsto\frac{a\tau+b}{c\tau+d}$. So the modular group is precisely **"all the ways to rebase the same lattice."** Two values of $\tau$ in the same orbit describe geometrically identical lattices (hence identical tori, hence identical physics in §s11). This is the single mental model that makes every later construction natural: Eisenstein series sum over lattice points, theta functions sum a Gaussian over the lattice, and modular invariance is independence of the basis choice.

#### Common pitfalls

- The condition $ad-bc=1$ (not $\pm1$) is what keeps us in the upper half-plane; a determinant $-1$ matrix would send $\mathbb H$ to the *lower* half-plane (flip the sign in Theorem 1, step 3). The full group of basis changes is $GL(2,\mathbb Z)$ with determinant $\pm1$, but only the determinant-$+1$ subgroup preserves orientation and $\mathbb H$.
- $c\tau+d$ is never zero on $\mathbb H$ but *can* be small, which is exactly when $\gamma\cdot\tau$ has large imaginary part — the mechanism we exploit in the reduction algorithm of §s2.

<a id="s2"></a>
### The fundamental domain and the generators $S$ and $T$

#### What & why

Since $PSL(2,\mathbb{Z})$ shuffles points of $\mathbb{H}$ around, each "physically distinct" point really stands for a whole orbit of equivalent points. A **fundamental domain** is a region containing exactly one representative of (almost) every orbit — a single "tile" whose images under the group cover all of $\mathbb{H}$ without overlap. We will identify the standard tile and use it to prove that the whole infinite group is generated by just two simple matrices, $S$ and $T$.

#### The two distinguished elements

> **Definition.** $T = \begin{pmatrix}1 & 1\\0 & 1\end{pmatrix}$, acting as $T\cdot\tau = \frac{\tau+1}{1}=\tau+1$ — **translation** by $1$.
>
> $S = \begin{pmatrix}0 & -1\\1 & 0\end{pmatrix}$, acting as $S\cdot\tau = \frac{-1}{\tau}$ — **inversion**.

Two relations, checked by matrix multiplication: $S^2 = \begin{pmatrix}-1&0\\0&-1\end{pmatrix}=-I$, which is the identity in $PSL(2,\mathbb{Z})$; and $(ST)^3 = -I$ as well. So in $PSL(2,\mathbb{Z})$ we have $S^2 = 1$ and $(ST)^3 = 1$.

#### Definition of the fundamental domain

> **Definition — the standard fundamental domain.**
> $$
> \mathcal{F} = \left\{ \tau\in\mathbb{H} : |\operatorname{Re}\tau|\le \tfrac12 \ \text{ and } \ |\tau|\ge 1 \right\}.
> $$
> It is the region above the unit circle and between the vertical lines $\operatorname{Re}\tau=\pm\frac12$.

#### Theorem 3 — $S$ and $T$ generate, and $\mathcal{F}$ is a fundamental domain

**Claim.** (i) Every $\tau\in\mathbb{H}$ has an $SL(2,\mathbb{Z})$-image in $\mathcal{F}$. (ii) The subgroup $G=\langle S,T\rangle$ generated by $S$ and $T$ is all of $PSL(2,\mathbb{Z})$.

**Proof (the two claims are proved together by the standard reduction algorithm).**

1. Fix $\tau\in\mathbb{H}$. Consider the subgroup $G=\langle S,T\rangle$, and look at the orbit $G\cdot\tau$. Recall from §s1 that $\operatorname{Im}(\gamma\cdot\tau)=\operatorname{Im}\tau/|c\tau+d|^2$. As $\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ ranges over $G$, the integers $(c,d)$ take values in a set of integer pairs; for fixed $\tau$, $|c\tau+d|^2 = (c x + d)^2 + (cy)^2$ grows without bound as $|c|,|d|\to\infty$, so it attains a *minimum* over the lattice of pairs. *(Reason: a positive-definite quadratic form in integers $(c,d)$ takes only finitely many values below any bound, so a minimum exists.)* Choose $\gamma_0\in G$ achieving the **maximum** of $\operatorname{Im}(\gamma\cdot\tau)$. Set $\tau' = \gamma_0\cdot\tau$; among all $G$-images, $\tau'$ has the largest imaginary part.
2. Apply a power of $T$ to bring the real part into range: replace $\tau'$ by $T^n\tau' = \tau'+n$ choosing the integer $n$ so that $|\operatorname{Re}(\tau'+n)|\le\frac12$. *(Reason: translating by integers shifts the real part by integers; one of them lands in any half-open interval of length $1$.)* This does not change the imaginary part, so $\tau'$ is still of maximal imaginary part in its orbit. Rename this point $\tau'$.
3. **Claim: $|\tau'|\ge 1$.** Suppose not, $|\tau'|<1$. Apply $S$: $S\tau' = -1/\tau'$ has imaginary part $\operatorname{Im}(\tau')/|\tau'|^2 > \operatorname{Im}(\tau')$ (since $|\tau'|^2<1$). *(Reason: master formula with $c=1,d=0$.)* This contradicts maximality of $\operatorname{Im}\tau'$. Hence $|\tau'|\ge1$.
4. Steps 2–3 put $\tau'\in\mathcal{F}$, and $\tau'$ was obtained from $\tau$ using only $S$ and $T$. This proves **(i)** with the image landing in $\mathcal{F}$ via an element of $G$.
5. **Now prove (ii).** Let $\gamma\in PSL(2,\mathbb{Z})$ be *arbitrary*. Pick any point $\tau_0$ in the *interior* of $\mathcal{F}$ (so it is not on the boundary, e.g. $\tau_0 = 2i$). By step 4 there is $g\in G$ with $g\cdot(\gamma\cdot\tau_0)\in\mathcal{F}$. We will show $g\gamma\in G$, hence $\gamma=g^{-1}(g\gamma)\in G$. To finish we need the **uniqueness** part below.
6. **Uniqueness of interior representatives.** *Claim:* if $\tau_0$ is interior to $\mathcal{F}$ and $h\cdot\tau_0\in\mathcal{F}$ for some $h\in PSL(2,\mathbb{Z})$, then $h=1$ and $h\cdot\tau_0=\tau_0$. Write $h=\begin{pmatrix}a&b\\c&d\end{pmatrix}$. Both $\tau_0$ and $h\tau_0$ lie in $\mathcal{F}$, so both have imaginary part $\ge \sqrt3/2$ (the minimum height in $\mathcal F$, attained at the corners $e^{\pm i\pi/3}$). Suppose $c\ne0$. Then $|c\tau_0+d|^2 = (c\operatorname{Re}\tau_0+d)^2+(c\operatorname{Im}\tau_0)^2 \ge c^2\operatorname{Im}\tau_0^2 \ge c^2\cdot\frac34 \ge \frac34$ when $|c|=1$. For the height not to decrease we need $|c\tau_0+d|\le1$; combined with $\operatorname{Im}\tau_0 > \sqrt3/2$ (strict, interior) one checks $|c\tau_0+d|^2 \ge \frac34 + (\text{positive})>$ the value compatible with both points in $\mathcal F$ unless $c=0$. *(Reason: the strict interior bound $\operatorname{Im}\tau_0>\sqrt3/2$ makes $c^2\operatorname{Im}\tau_0^2>3/4$ for $|c|\ge1$, forcing the height to strictly drop, contradicting that $h\tau_0$ is also as high as required.)* So $c=0$. Then $ad=1$ with integers gives $a=d=\pm1$, so $h=\pm\begin{pmatrix}1&b\\0&1\end{pmatrix}=T^b$ in $PSL$, acting as $\tau_0\mapsto\tau_0+b$; for $\tau_0+b$ to stay with $|\operatorname{Re}|\le\frac12$ while $|\operatorname{Re}\tau_0|<\frac12$ strictly forces $b=0$. Thus $h=1$.
7. Apply step 6 to $h=g\gamma$ with the interior point $\tau_0$: $g\gamma\cdot\tau_0\in\mathcal{F}$ and $\tau_0$ interior force $g\gamma=1$, i.e. $\gamma=g^{-1}\in G$. Since $\gamma$ was arbitrary, $G=PSL(2,\mathbb{Z})$. $\blacksquare$

This simultaneously shows $\mathcal{F}$ is a fundamental domain: every orbit meets it, and an *interior* point of $\mathcal F$ is the unique representative of its orbit (boundary points are identified in pairs — left edge with right edge by $T$, and the two halves of the lower arc by $S$).

#### Worked example of the reduction

Reduce $\tau = \frac{1}{2}+ \frac{1}{4}i$... actually take $\tau= 2 + \tfrac{1}{10}i$ (low and far right). Step 2: subtract $T^2$ to get $\frac{1}{10}i$ — but $|\tfrac{1}{10}i|<1$. Step 3: apply $S$: $-1/(\tfrac{i}{10}) = 10i$, height $10$. Now $|10i|=10\ge1$ and real part $0$: $10i\in\mathcal F$. The reducing element is $S T^{-2}$.

#### A second worked reduction

Reduce $\tau = -\tfrac{3}{7}+\tfrac{1}{14}i$. It already has $|\operatorname{Re}\tau|=\tfrac37\le\tfrac12$, but $|\tau|^2=\tfrac{9}{49}+\tfrac{1}{196}<1$, so it is below the arc. Apply $S$: $S\tau=-1/\tau$. Compute $-1/\tau = -\overline\tau/|\tau|^2$; with $|\tau|^2=\frac{36+1}{196}=\frac{37}{196}$ and $\overline\tau=-\frac37-\frac{1}{14}i$, we get $-1/\tau=\frac{(3/7)+(1/14)i}{37/196}=\frac{196}{37}\big(\tfrac37+\tfrac{1}{14}i\big)=\frac{84}{37}+\frac{14}{37}i$. The new height is $\frac{14}{37}$, larger than $\frac{1}{14}$ as promised by step 3. Now bring the real part in: $\frac{84}{37}\approx2.27$, subtract $T^2$ to get $\frac{84}{37}-2=\frac{10}{37}\approx0.27$, within $|\cdot|\le\frac12$, and $|\tfrac{10}{37}+\tfrac{14}{37}i|^2=\frac{100+196}{1369}=\frac{296}{1369}<1$ — still below the arc, so repeat $S$ once more. Each pass strictly increases the height, and since heights in an orbit have a maximum, the algorithm terminates inside $\mathcal F$. This is the constructive content of Theorem 3.

#### The orbifold picture and pitfalls

The quotient $\mathbb{H}/PSL(2,\mathbb{Z})$, made by gluing the edges of $\mathcal F$, is a sphere with two special **orbifold points** — at $\tau=i$ (fixed by $S$, an order-2 symmetry) and at $\tau=\rho:=e^{2\pi i/3}$ (fixed by $ST$, order 3) — plus one **cusp** at $\tau\to i\infty$. The cusp is the "point at infinity" where $\operatorname{Im}\tau\to\infty$; it is where we will demand good behavior of modular forms. The order-2 and order-3 symmetries here are the source of the $\tfrac12$ and $\tfrac13$ that will appear in the valence formula (§s6) and in the dimension formula (§s5) — every appearance of those fractions traces back to these two fixed points.

*Pitfalls:* (i) the boundary of $\mathcal F$ is not "free" — points on it are glued, so $\mathcal F$ has only the interior as unique representatives. (ii) The presentation of $PSL(2,\mathbb Z)$ is $\langle S,T\mid S^2=(ST)^3=1\rangle$, which makes it the **free product** $\mathbb Z/2 * \mathbb Z/3$; this means a generic element has a *unique* reduced word in $S$ and $T$, the algebraic shadow of the unique reduction path.

## Part B · Modular forms and the canonical examples

<a id="s3"></a>
### Modular forms of weight $k$; modular functions

#### What & why

We now define the objects of study. A modular form is holomorphic on $\mathbb{H}$, transforms with a factor $(c\tau+d)^k$, and is "tame" at the cusp. Each of these three conditions is essential; we explain why and extract the immediate consequences.

#### The definition

> **Definition — modular form of weight $k$.** Let $k$ be an integer. A function $f:\mathbb{H}\to\mathbb{C}$ is a **modular form of weight $k$** for $SL(2,\mathbb{Z})$ if:
> 1. **(Holomorphy)** $f$ is holomorphic on $\mathbb{H}$ — complex-differentiable everywhere (restated from [Complex Analysis](../complex-analysis/complex-analysis.md): holomorphic means locally given by a convergent power series).
> 2. **(Modularity / weight $k$)** For all $\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in SL(2,\mathbb{Z})$,
> $$
> f\!\left(\frac{a\tau+b}{c\tau+d}\right) = (c\tau+d)^k\, f(\tau).
> $$
> 3. **(Holomorphy at the cusp)** $f$ stays bounded as $\operatorname{Im}\tau\to\infty$.
>
> If in addition $f\to 0$ as $\operatorname{Im}\tau\to\infty$ (the constant term of its expansion below vanishes), $f$ is a **cusp form**.

> **Definition — modular function.** A **modular function** is a *weight-zero* meromorphic (allowed poles) function with $f(\gamma\cdot\tau)=f(\tau)$ — genuinely invariant — and at most a pole at the cusp. The $j$-invariant (§s5) is the prototype.

#### Two immediate consequences

1. **Periodicity and the $q$-expansion.** Taking $\gamma=T$ ($c=0,d=1$) in condition 2 gives $f(\tau+1)=f(\tau)$: every modular form is periodic with period $1$. A holomorphic, $1$-periodic function can be written as a Laurent series in
   $$
   q := e^{2\pi i\tau},
   $$
   the **nome**. *(Reason: $\tau\mapsto q$ maps the strip $0\le\operatorname{Re}\tau<1$ onto the punctured unit disk; periodicity makes $f$ a single-valued function of $q$, hence a Laurent series $\sum_{n} a_n q^n$ by the complex-analysis theorem on annular domains.)* As $\operatorname{Im}\tau\to\infty$, $q=e^{2\pi i(x+iy)}=e^{2\pi i x}e^{-2\pi y}\to 0$. So the cusp is $q=0$, and condition 3 (boundedness) becomes: **no negative powers of $q$**, i.e.
   $$
   f(\tau) = \sum_{n=0}^{\infty} a_n q^n.
   $$
   A cusp form is one with $a_0=0$.

2. **Odd weight forces $f\equiv 0$.** Take $\gamma=-I$ ($a=d=-1$, $b=c=0$). The left side is $f(\tau)$ (since $-I$ acts trivially on $\tau$), the right side is $(-1)^k f(\tau)$. If $k$ is odd, $f=-f$, so $f\equiv0$. *(Reason: $(c\tau+d)^k=(-1)^k$ here.)* Hence only **even** weights have nonzero forms for the full modular group.

#### Why each condition matters (pitfalls)

- Drop holomorphy at the cusp and you admit functions like $1/\Delta$ (§s5) with poles there — those are *weakly holomorphic* and form an infinite-dimensional space; the finiteness magic is lost.
- The transformation factor $(c\tau+d)^k$ is *not* a typo for invariance: it is exactly the factor that makes "$f(\tau)\,(d\tau)^{k/2}$" an invariant object, which is why weight-$k$ forms integrate naturally and why the weight is tied to differentials of order $k/2$.

#### Why weight-$k$ forms multiply weights — and a first dimension count

If $f$ has weight $k$ and $g$ has weight $\ell$, then $fg$ satisfies $(fg)(\gamma\tau)=(c\tau+d)^{k}(c\tau+d)^{\ell}f(\tau)g(\tau)=(c\tau+d)^{k+\ell}(fg)(\tau)$, so $fg$ has weight $k+\ell$. *(Reason: the automorphy factors simply multiply.)* This is what makes the collection of all modular forms a **graded ring** (§s5). A ratio $f/g$ of two weight-$k$ forms has weight $0$, hence is a modular *function* — this is how the invariant $j$ will be built. As a sanity check that the spaces are small: a weight-$0$ holomorphic modular form is bounded on the compact quotient $\mathbb H/SL(2,\mathbb Z)\cup\{\text{cusp}\}$, and a bounded holomorphic function on a compact Riemann surface is constant (maximum modulus principle, from [Complex Analysis](../complex-analysis/complex-analysis.md)). So $\dim M_0=1$ — already a glimpse of the finiteness we prove in general in §s6.

<a id="s4"></a>
### Eisenstein series $G_{2k}$, their $q$-expansions, and the $E_2$ anomaly

#### What & why

We need actual nonzero examples. The most natural way to *build* a weight-$k$ function is to **average** something simple over the group — sum $1/(\text{denominator})^k$ over all the automorphy factors. This is the **Eisenstein series**. We construct it, prove it is modular, and compute its $q$-expansion explicitly, which secretly contains the **divisor-sum** functions of number theory. We then meet the borderline case $E_2$, which fails modularity by a computable "anomaly."

#### Definition and convergence

> **Definition — Eisenstein series.** For an even integer $2k\ge 4$,
> $$
> G_{2k}(\tau) = \sum_{(m,n)\ne(0,0)} \frac{1}{(m\tau+n)^{2k}},
> $$
> the sum over all integer pairs $(m,n)$ except $(0,0)$.

**Convergence.** The series converges absolutely for $2k>2$. *(Reason: $|m\tau+n|$ is comparable to $\sqrt{m^2+n^2}$ uniformly on compact subsets of $\mathbb H$, and $\sum_{(m,n)\ne0}(m^2+n^2)^{-k}$ converges precisely when $2k>2$ by the integral test in two dimensions — the radial integral $\int^\infty r^{1-2k}\,dr$ converges for $2k>2$.)* Absolute convergence lets us reorder terms freely, which we use next.

#### Modularity

**Claim.** $G_{2k}$ has weight $2k$: $G_{2k}(\gamma\cdot\tau)=(c\tau+d)^{2k}G_{2k}(\tau)$.

**Proof.**

1. Substitute $\tau\mapsto\frac{a\tau+b}{c\tau+d}$:
   $$
   m\cdot\frac{a\tau+b}{c\tau+d}+n = \frac{m(a\tau+b)+n(c\tau+d)}{c\tau+d} = \frac{(ma+nc)\tau+(mb+nd)}{c\tau+d}.
   $$
2. Define new integers $m' = ma+nc$, $n' = mb+nd$, i.e. $(m',n')=(m,n)\gamma$. Because $\gamma\in SL(2,\mathbb{Z})$ is invertible over the integers (its inverse $\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$ also has integer entries and determinant 1), the map $(m,n)\mapsto(m',n')$ is a **bijection** of $\mathbb{Z}^2\setminus\{0\}$ onto itself. *(Reason: a linear map with integer-invertible matrix permutes the lattice.)*
3. Therefore
   $$
   G_{2k}(\gamma\cdot\tau) = \sum_{(m,n)\ne0}\frac{(c\tau+d)^{2k}}{(m'\tau+n')^{2k}} = (c\tau+d)^{2k}\sum_{(m',n')\ne0}\frac{1}{(m'\tau+n')^{2k}} = (c\tau+d)^{2k}G_{2k}(\tau),
   $$
   where reordering the absolutely convergent sum over the bijected indices is legitimate. $\blacksquare$

Holomorphy on $\mathbb{H}$ and boundedness at the cusp follow because the series converges uniformly on compacta and term-by-term $\to n^{-2k}$ as $\operatorname{Im}\tau\to\infty$. So $G_{2k}$ is a genuine modular form of weight $2k$.

#### Deriving the $q$-expansion

We compute the limit and the expansion. The tool is the **Lipschitz / cotangent identity**: for $\tau\in\mathbb{H}$,
$$
\sum_{n=-\infty}^{\infty}\frac{1}{(\tau+n)^{2k}} = \frac{(-2\pi i)^{2k}}{(2k-1)!}\sum_{r=1}^{\infty} r^{2k-1} q^{r},\qquad q=e^{2\pi i\tau}.
$$

*Derivation of the cotangent identity (the engine).*

1. Start from the partial-fraction expansion of cotangent (a standard complex-analysis identity, proved by comparing poles and periodicity):
   $$
   \pi\cot(\pi\tau) = \frac1\tau + \sum_{n=1}^\infty\Big(\frac{1}{\tau+n}+\frac{1}{\tau-n}\Big) = \sum_{n=-\infty}^\infty \frac{1}{\tau+n}.
   $$
2. Independently, $\pi\cot\pi\tau = \pi\frac{\cos\pi\tau}{\sin\pi\tau}$. Write $\cos,\sin$ via exponentials: $\pi\cot\pi\tau = \pi i\,\frac{e^{i\pi\tau}+e^{-i\pi\tau}}{e^{i\pi\tau}-e^{-i\pi\tau}} = \pi i\,\frac{q+1}{q-1}$ with $q=e^{2\pi i\tau}$. Rearrange: $\pi i\frac{q+1}{q-1} = \pi i\big(1+\frac{2}{q-1}\big) = \pi i - 2\pi i\frac{1}{1-q} = \pi i -2\pi i\sum_{r=0}^\infty q^r$. *(Reason: geometric series $\frac{1}{1-q}=\sum q^r$, valid since $|q|<1$ for $\operatorname{Im}\tau>0$.)*
3. Equate steps 1 and 2: $\sum_{n}\frac{1}{\tau+n} = \pi i - 2\pi i\sum_{r=0}^\infty q^r = -\pi i - 2\pi i\sum_{r=1}^\infty q^r$.
4. Differentiate both sides $2k-1$ times with respect to $\tau$. On the left, $\frac{d^{2k-1}}{d\tau^{2k-1}}\frac{1}{\tau+n} = \frac{(-1)^{2k-1}(2k-1)!}{(\tau+n)^{2k}}=\frac{-(2k-1)!}{(\tau+n)^{2k}}$. On the right, $\frac{d}{d\tau}q^r = 2\pi i\,r\,q^r$, so differentiating $2k-1$ times multiplies the $r$-th term by $(2\pi i r)^{2k-1}$. *(Reason: term-by-term differentiation of a uniformly convergent series of holomorphic functions, allowed on $\mathbb H$.)* This yields
   $$
   -(2k-1)!\sum_n\frac{1}{(\tau+n)^{2k}} = -2\pi i\sum_{r=1}^\infty (2\pi i r)^{2k-1}q^r,
   $$
   and solving gives the boxed identity above. $\checkmark$

*Now assemble $G_{2k}$.* Split the lattice sum by whether $m=0$:
$$
G_{2k}(\tau) = \underbrace{\sum_{n\ne0}\frac{1}{n^{2k}}}_{m=0} + \sum_{m\ne0}\sum_{n}\frac{1}{(m\tau+n)^{2k}}.
$$
1. The $m=0$ piece is $2\zeta(2k)$, where $\zeta(s)=\sum_{n\ge1}n^{-s}$ is the **Riemann zeta function**; the factor $2$ collects $\pm n$.
2. For each $m\ne0$ the inner sum is $\sum_n (m\tau+n)^{-2k}$; apply the cotangent identity with $\tau\to m\tau$, giving $\frac{(-2\pi i)^{2k}}{(2k-1)!}\sum_{r\ge1}r^{2k-1}q^{mr}$ (for $m>0$; the $m<0$ terms double it since $2k$ is even). Summing over $m\ge1$ and collecting powers $q^{N}$ with $N=mr$:
   $$
   2\sum_{m\ge1}\frac{(-2\pi i)^{2k}}{(2k-1)!}\sum_{r\ge1}r^{2k-1}q^{mr} = \frac{2(2\pi i)^{2k}}{(2k-1)!}\sum_{N\ge1}\Big(\sum_{r\mid N} r^{2k-1}\Big)q^N,
   $$
   where $\sum_{r\mid N}r^{2k-1}=:\sigma_{2k-1}(N)$ is the **divisor power sum** (sum of the $(2k-1)$-th powers of the divisors of $N$); $(-2\pi i)^{2k}=(2\pi i)^{2k}$ since $2k$ is even.
3. Combine. Using the value $\zeta(2k)=\frac{(-1)^{k+1}B_{2k}(2\pi)^{2k}}{2(2k)!}$ ($B_{2k}$ the **Bernoulli numbers**, defined by $\frac{t}{e^t-1}=\sum B_n\frac{t^n}{n!}$), the standard **normalized Eisenstein series** $E_{2k}:=G_{2k}/(2\zeta(2k))$ has constant term $1$ and the clean expansion
   $$
   E_{2k}(\tau) = 1 - \frac{4k}{B_{2k}}\sum_{N\ge1}\sigma_{2k-1}(N)\,q^N.
   $$

**Concrete cases** (with $B_2=\tfrac16,\,B_4=-\tfrac1{30},\,B_6=\tfrac1{42}$):
$$
E_4 = 1 + 240\sum_{N\ge1}\sigma_3(N)q^N = 1+240q+2160q^2+\cdots,
$$
$$
E_6 = 1 - 504\sum_{N\ge1}\sigma_5(N)q^N = 1-504q-16632q^2-\cdots.
$$

#### The $E_2$ anomaly

For $2k=2$ the lattice sum diverges (the case $2k=2$ fails the convergence test), but a conditionally convergent regularization defines
$$
E_2(\tau) = 1 - 24\sum_{N\ge1}\sigma_1(N)q^N.
$$
It is holomorphic and $1$-periodic but **fails** the $S$-transformation by an additive **anomaly**:
$$
E_2\!\left(-\tfrac1\tau\right) = \tau^2 E_2(\tau) + \frac{12\tau}{2\pi i} = \tau^2 E_2(\tau) - \frac{6i\tau}{\pi}.
$$
*Reason in one line:* the conditional rearrangement of the borderline-divergent double sum picks up a boundary term, exactly the extra $\frac{6i\tau}{\pi}$. $E_2$ is the prototype of a **quasimodular form**. The combination $\widehat{E}_2(\tau)=E_2(\tau)-\frac{3}{\pi\operatorname{Im}\tau}$ *is* modular of weight 2 but no longer holomorphic — the same trade-off (holomorphy vs. exact modularity) that recurs as the "modular anomaly" in §s9 and §s11.

#### Worked example: the Ramanujan derivative identities

$E_2$ is not just a curiosity; it generates the derivatives of modular forms. Writing $D=\frac{1}{2\pi i}\frac{d}{d\tau}=q\frac{d}{dq}$ (which lowers a $q^n$ to $n\,q^n$), one has the **Ramanujan identities**
$$
DE_2 = \frac{E_2^2-E_4}{12},\qquad DE_4 = \frac{E_2E_4-E_6}{3},\qquad DE_6=\frac{E_2E_6-E_4^2}{2}.
$$
*Why these hold (one line):* $Df$ for a weight-$k$ form $f$ is not modular (differentiation breaks the transformation by a term proportional to $E_2$), but the corrected derivative $Df-\frac{k}{12}E_2 f$ *is* a weight-$(k+2)$ form (the **Serre derivative** $\vartheta_k$); expanding in the low-dimensional spaces $M_4,M_6,M_8$ and matching the first $q$-coefficients pins the constants above. Check the first: $DE_4=240\sum n\sigma_3(n)q^n=240q+\cdots$, and $\frac{E_2E_4-E_6}{3}=\frac{(1-24q)(1+240q)-(1-504q)}{3}+\cdots=\frac{(216+504)q}{3}+\cdots=240q+\cdots$. Agreement. These identities show $\Delta'/\Delta=E_2$ (so $E_2$ is the logarithmic derivative of the discriminant), tying $E_2$ to the zero-counting of §s6.

<a id="s5"></a>
### The discriminant $\Delta$, the $j$-invariant, and the graded ring

#### What & why

From $E_4$ and $E_6$ we can build *every* modular form by addition and multiplication; the collection of all forms is a **graded ring**, and we will compute its dimensions exactly. The first new building block is the **discriminant** $\Delta$, the simplest cusp form, and from it the **$j$-invariant**, the simplest modular function.

#### The discriminant

> **Definition.**
> $$
> \Delta(\tau) = \frac{E_4(\tau)^3 - E_6(\tau)^2}{1728}.
> $$

It is a modular form of weight $12$ (a product/sum of weights $4\cdot3=12$ and $6\cdot2=12$). Its constant term: $E_4^3 = (1+240q+\cdots)^3 = 1+720q+\cdots$ and $E_6^2=(1-504q+\cdots)^2 = 1-1008q+\cdots$; the difference is $1728q+\cdots$, so dividing by $1728$ gives constant term $0$ and
$$
\Delta(\tau) = q - 24q^2 + 252q^3 - 1472q^4 + \cdots = q\prod_{n=1}^\infty(1-q^n)^{24}.
$$
Thus $\Delta$ is a **cusp form** of weight 12, and (the product formula, proved in §s9 via the eta function) it is **never zero** on $\mathbb H$ — it vanishes only at the cusp $q=0$, to first order. The coefficients $\tau(N)$ of $\Delta=\sum\tau(N)q^N$ are **Ramanujan's tau function**.

#### The $j$-invariant

> **Definition.**
> $$
> j(\tau) = \frac{E_4(\tau)^3}{\Delta(\tau)} = 1728\,\frac{E_4^3}{E_4^3-E_6^2}.
> $$

It has weight $12-12=0$, so it is genuinely $SL(2,\mathbb{Z})$-**invariant**: $j(\gamma\tau)=j(\tau)$. Since $\Delta=q+\cdots$ and $E_4^3=1+720q+\cdots$, the expansion is
$$
j(\tau) = \frac1q + 744 + 196884\,q + 21493760\,q^2+\cdots,
$$
a *pole* at the cusp. $j$ is a modular function. **Fundamental fact:** $j:\mathbb{H}/SL(2,\mathbb{Z})\to\mathbb{C}$ is a bijection — every complex value is attained exactly once per fundamental domain. So modular functions are exactly the rational functions of $j$.

#### The graded ring and the dimension formula

> **Definition — graded ring.** Let $M_k$ be the (finite-dimensional) vector space of modular forms of weight $k$, and $S_k\subset M_k$ the subspace of cusp forms. The direct sum $M_* = \bigoplus_{k} M_k$ is a **graded ring**: the product of a weight-$k$ and a weight-$\ell$ form has weight $k+\ell$.

> **Theorem 4 (Structure & dimensions).** Every modular form is a polynomial in $E_4$ and $E_6$:
> $$
> M_* = \mathbb{C}[E_4,E_6],
> $$
> with $E_4,E_6$ algebraically independent. Consequently the dimension of $M_k$ (for even $k\ge0$) is
> $$
> \dim M_k = \begin{cases} \big\lfloor k/12\big\rfloor & k\equiv 2 \pmod{12},\\[2pt] \big\lfloor k/12\big\rfloor + 1 & k\not\equiv 2 \pmod{12}, \end{cases}
> $$
> and $\dim M_k=0$ for odd $k$ or $k<0$.

**Proof sketch with the key step made rigorous (full proof needs §s6).**

1. *Counting monomials.* A monomial $E_4^a E_6^b$ has weight $4a+6b$. For a given even weight $k$, the number of solutions $(a,b)\in\mathbb{Z}_{\ge0}^2$ to $4a+6b=k$ equals the dimension claimed above. *(Reason: elementary counting of nonnegative solutions of $2a+3b=k/2$.)*
2. *Independence and spanning* are proved using the valence formula of §s6, which shows a form of weight $<12$ is determined by its constant term (so $\dim M_0=1,M_2=0,M_4=M_6=M_8=M_{10}=1$), and that multiplication by $\Delta$ gives an isomorphism $M_{k-12}\xrightarrow{\sim}S_k$. Induction then yields all dimensions. $\blacksquare$

**Worked dimensions.** $\dim M_0=1$ (constants), $M_2=0$, $M_4=1$ ($E_4$), $M_6=1$ ($E_6$), $M_8=1$ ($E_4^2$, so $E_8=E_4^2$ — a hidden identity forcing $\sigma_7$ relations!), $M_{10}=1$ ($E_4E_6$), $M_{12}=2$ (spanned by $E_4^3$ and $\Delta$), and the first cusp form appears at weight $12$.

#### The identity $E_8=E_4^2$ unpacked — a number-theory bonus

Because $\dim M_8=1$ and both $E_8$ and $E_4^2$ are weight-$8$ forms with constant term $1$, they must be *equal*. Matching the $q^N$ coefficients gives a nontrivial arithmetic identity for free:
$$
\sigma_7(N) = \sigma_3(N) + 120\sum_{m=1}^{N-1}\sigma_3(m)\,\sigma_3(N-m).
$$
*(Reason: $E_8=1+480\sum\sigma_7(N)q^N$ on the left; squaring $E_4=1+240\sum\sigma_3(N)q^N$ and collecting the convolution on the right; the leading $480$ vs. $2\cdot240$ and the convolution $240^2=57600=480\cdot120$ produce the stated coefficients.)* Check $N=1$: $\sigma_7(1)=1$, and the right side is $\sigma_3(1)+0=1$. Check $N=2$: $\sigma_7(2)=1+128=129$, right side $\sigma_3(2)+120\sigma_3(1)^2=9+120=129$. Agreement. This is the cleanest illustration of the guide's thesis: a *dimension count* (finite, structural) forces an *infinite* family of identities among divisor sums.

<a id="s6"></a>
### The valence formula — counting zeros by contour integration

#### What & why

The dimension formula above rests on a single counting law: a nonzero modular form of weight $k$ has a fixed *total* number of zeros, $k/12$, distributed over the fundamental domain (with special fractional weights at the orbifold points). This is the **valence formula**, and we prove it by integrating the logarithmic derivative $f'/f$ around the boundary of $\mathcal F$ — the **argument principle** in action.

#### Statement

> **Theorem 5 (Valence formula).** Let $f\ne0$ be a modular form of weight $k$. Write $\operatorname{ord}_p(f)$ for the order of vanishing of $f$ at a point $p$. Then
> $$
> \operatorname{ord}_\infty(f) + \tfrac12\operatorname{ord}_i(f) + \tfrac13\operatorname{ord}_\rho(f) + \sum_{p\ne i,\rho,\infty} \operatorname{ord}_p(f) \;=\; \frac{k}{12},
> $$
> where $\rho=e^{2\pi i/3}$, $\operatorname{ord}_\infty$ is the order in $q$ at the cusp, and the sum is over orbit-representatives in $\mathcal F$ interior plus boundary (counted once).

The fractions $\tfrac12,\tfrac13$ reflect the orbifold symmetry orders at $i$ and $\rho$ (§s2).

#### Proof by contour integration

The idea: by the **argument principle** (restated from [Complex Analysis](../complex-analysis/complex-analysis.md): $\frac{1}{2\pi i}\oint \frac{f'}{f}\,d\tau$ equals the number of zeros minus poles enclosed), integrate $\frac{1}{2\pi i}\frac{f'}{f}$ around $\partial\mathcal F$. Since $f$ is holomorphic (no poles in $\mathbb H$), the integral counts the interior zeros; we then evaluate the same integral edge-by-edge using modularity, and the two evaluations are equated.

1. **The contour.** Take $\partial\mathcal F$: up the right edge $\operatorname{Re}\tau=\frac12$ to a high cutoff $\operatorname{Im}\tau=Y$, across the top, down the left edge $\operatorname{Re}\tau=-\frac12$, and along the bottom arc $|\tau|=1$. Indent with small circular arcs around the corner points $i,\rho,\rho+1$ (so the contour avoids zeros there), and use a horizontal segment at height $Y$ near the cusp. Assume (generic case) $f$ has no zeros on the edges except possibly at $i,\rho$.
2. **Top segment $\leftrightarrow$ cusp.** The horizontal piece at height $Y$, traversed right-to-left, contributes $\frac{1}{2\pi i}\int \frac{f'}{f}d\tau$. Change variable to $q=e^{2\pi i\tau}$: this segment maps to a small circle around $q=0$ traversed clockwise, and the integral equals $-\operatorname{ord}_\infty(f)$. *(Reason: $\frac{1}{2\pi i}\oint_{|q|=\epsilon}\frac{dq}{q}\cdot(\text{order})$; the leading $q$-power of $f$ gives its order at the cusp.)* So this part contributes $-\operatorname{ord}_\infty(f)$ to the count.
3. **Left and right edges cancel via $T$.** The map $T:\tau\mapsto\tau+1$ carries the left edge to the right edge. Since $f(\tau+1)=f(\tau)$, the integrand $\frac{f'}{f}$ takes equal values at corresponding points, but the two edges are traversed in *opposite* directions, so their contributions **cancel**. *(Reason: periodicity of $f$ under $T$.)*
4. **The bottom arc splits at $i$; $S$ relates the halves.** The arc $|\tau|=1$ is mapped to itself by $S:\tau\mapsto-1/\tau$, which swaps the two halves (from $\rho$ to $i$, and from $i$ to $\rho+1$). Modularity $f(-1/\tau)=\tau^k f(\tau)$ gives, on differentiating logarithmically, $\frac{f'}{f}(-1/\tau)\cdot\frac{1}{\tau^2} = \frac{k}{\tau}+\frac{f'}{f}(\tau)$. Integrating the difference of the two half-arcs leaves the residual $\frac{1}{2\pi i}\int \frac{k}{\tau}\,d\tau$ over a quarter-turn (from $\rho$ to $i$ is a $\frac{1}{12}$ turn of argument from $\frac{2\pi}{3}$ to $\frac{\pi}{2}$), evaluating to $\frac{k}{12}$. *(Reason: $\frac{1}{2\pi i}\int_C \frac{d\tau}{\tau}=\frac{\Delta(\arg)}{2\pi}$; the net argument swept is $\frac{2\pi}{12}$.)* This produces the $\frac{k}{12}$ on the right-hand side.
5. **Corner indentations give the orbifold fractions.** The small arc around $i$ subtends angle $\pi$ (half a full turn, since $i$ is a fixed point of order 2 and the domain has interior angle $\pi$ there), contributing $-\frac12\operatorname{ord}_i(f)$. The arcs around $\rho$ and $\rho+1$ together subtend angle $\frac{2\pi}{3}$ (order-3 fixed point), contributing $-\frac13\operatorname{ord}_\rho(f)$. *(Reason: an indentation of angle $\theta$ around a zero of order $m$ contributes $-\frac{\theta}{2\pi}m$ to the argument-principle count.)*
6. **Equate.** The total contour integral equals $\sum_{p\,\text{interior}}\operatorname{ord}_p(f)$ (the genuine interior zeros, by the argument principle). Summing the edge contributions from steps 2–5 and moving terms across gives exactly the valence formula. $\blacksquare$

#### Worked consequences

- $\Delta$ has weight $12$, so total zero count $=1$. Its $q$-expansion starts $q$, i.e. $\operatorname{ord}_\infty\Delta=1$. That *uses up the entire budget*, so $\Delta$ has **no zeros in $\mathbb H$** — confirming the claim of §s5 and justifying that division by $\Delta$ is allowed.
- $E_4$ has weight $4$: budget $\frac{4}{12}=\frac13$, which can only be $\frac13\operatorname{ord}_\rho$, so $E_4(\rho)=0$ and $E_4$ vanishes nowhere else. Likewise $E_6$ has budget $\frac{6}{12}=\frac12$: $E_6(i)=0$ and nowhere else.

#### How the valence formula yields the dimension formula

The valence formula is the engine for Theorem 4. Two consequences:
1. **Low weights are forced.** For $0\le k<12$ the total budget $\frac{k}{12}<1$. Since interior orders are nonnegative integers and the orbifold contributions are multiples of $\frac13$ and $\frac12$, only specific combinations sum to $\frac{k}{12}$, and in each case a nonzero form is determined up to scale by its constant term — giving $\dim M_k\le1$ for $k\in\{0,4,6,8,10\}$ and $\dim M_2=0$ (the budget $\frac16$ is unreachable by any allowed nonnegative combination of $1,\frac12,\frac13$). The Eisenstein series supply the matching nonzero element, so equality holds.
2. **Multiplication by $\Delta$ is an isomorphism $M_{k-12}\xrightarrow{\sim}S_k$.** If $f\in M_{k-12}$ then $\Delta f\in S_k$ (weights add to $k$; $\Delta$'s zero at the cusp makes the product a cusp form). Conversely if $g\in S_k$ then $g$ vanishes at the cusp, and since $\Delta$ is nonvanishing on $\mathbb H$ with a simple zero only at the cusp, $g/\Delta$ is holomorphic everywhere including the cusp, so $g/\Delta\in M_{k-12}$. *(Reason: dividing by a form with a single simple cusp-zero and no interior zeros preserves holomorphy.)* Hence $\dim S_k=\dim M_{k-12}$, and $\dim M_k=\dim S_k+1$ whenever an Eisenstein series of weight $k$ exists (i.e. $k\ge4$ even). Induction from the base cases gives the full formula. This is precisely the inductive step deferred in §s5. $\blacksquare$

## Part C · Deeper structure and arithmetic

<a id="s7"></a>
### Hecke operators and Hecke eigenforms

#### What & why

The coefficients $\tau(N)$ of $\Delta$ satisfy startling multiplicative relations, e.g. $\tau(mn)=\tau(m)\tau(n)$ for coprime $m,n$. These come from a family of linear operators $T_n$ — the **Hecke operators** — that act on each space $M_k$ and commute with each other. Their simultaneous eigenvectors, the **Hecke eigenforms**, are the "atoms" of the theory and the ones with arithmetic meaning.

#### Definition

> **Definition — Hecke operator.** For a prime $p$, the operator $T_p$ acts on a weight-$k$ form $f(\tau)=\sum a_n q^n$ by
> $$
> (T_p f)(\tau) = \sum_n \Big(a_{pn} + p^{k-1} a_{n/p}\Big) q^n,
> $$
> where $a_{n/p}:=0$ if $p\nmid n$. More invariantly, $T_p$ averages $f$ over the $p+1$ sublattices of index $p$:
> $$
> (T_pf)(\tau)= p^{k-1}f(p\tau) + \frac1p\sum_{j=0}^{p-1} f\!\Big(\frac{\tau+j}{p}\Big).
> $$

**Why it maps $M_k$ to $M_k$ (one line).** Each term is a weight-$k$ pullback under a degree-$p$ map, and the sum over the $p+1$ cosets is permuted by $SL(2,\mathbb{Z})$, so $T_pf$ is again modular of weight $k$; holomorphy at the cusp is preserved because the $q$-formula has no negative powers.

> **Definition — Hecke eigenform.** A nonzero $f\in M_k$ that is a simultaneous eigenvector for all $T_n$: $T_n f=\lambda_n f$. **Normalized** if $a_1=1$.

#### Theorem 6 — eigenvalues are coefficients; coefficients are multiplicative

**Claim.** If $f=\sum a_nq^n$ is a normalized eigenform, then $a_n=\lambda_n$, and the coefficients satisfy $a_m a_n = a_{mn}$ for $\gcd(m,n)=1$, and $a_p a_{p^r}=a_{p^{r+1}}+p^{k-1}a_{p^{r-1}}$.

**Proof.**

1. Compare the coefficient of $q^1$ on both sides of $T_pf=\lambda_p f$. From the definition, the $q^1$-coefficient of $T_pf$ is $a_p + p^{k-1}a_{1/p}=a_p$ (since $a_{1/p}=0$). The $q^1$-coefficient of $\lambda_p f$ is $\lambda_p a_1=\lambda_p$. Hence $\lambda_p=a_p$. *(Reason: matching coefficients of equal power series.)*
2. The general relations follow from the **composition law** of Hecke operators, $T_mT_n=\sum_{d\mid\gcd(m,n)}d^{k-1}T_{mn/d^2}$, applied to the eigenform and read off coefficient by coefficient. In particular for coprime $m,n$ the sum has one term, giving $a_ma_n=a_{mn}$; for prime powers it gives the recursion stated. $\blacksquare$

#### Worked example: $\Delta$ is an eigenform

$S_{12}$ is one-dimensional (only $\Delta$ up to scale), so $\Delta$ is automatically a Hecke eigenform. Hence its coefficients $\tau(N)$ are multiplicative: $\tau(2)\tau(3)=\tau(6)$. Check: $\tau(2)=-24,\ \tau(3)=252,\ \tau(6)=-6048$, and indeed $(-24)(252)=-6048$. The recursion at $p=2$: $\tau(2)\tau(4)=\tau(8)+2^{11}\tau(2)$, i.e. $(-24)(-1472)=\tau(8)+2048(-24)$, giving $\tau(8)=35328+49152=84480$. These multiplicative relations were *conjectured by Ramanujan* and *proved by Hecke* exactly via this theory.

#### Intuition and the Euler product

Why should averaging over sublattices (a geometric operation) produce *multiplicativity* (an arithmetic miracle)? Because the index-$p$ sublattices for *different* primes are independent: refining by $p$ and then by a coprime $q$ is the same as refining by $pq$ in one step, with no overlap. That independence is the geometric source of $a_{mn}=a_ma_n$ for coprime $m,n$. The payoff is that the $L$-function (§s10) factors as an **Euler product** over primes,
$$
L(f,s)=\prod_p\frac{1}{1-a_p\,p^{-s}+p^{k-1-2s}},
$$
the local quadratic factor coming directly from the prime-power recursion $a_pa_{p^r}=a_{p^{r+1}}+p^{k-1}a_{p^{r-1}}$. *(Reason: summing the geometric-like series $\sum_r a_{p^r}p^{-rs}$ with that recursion gives exactly the inverse quadratic.)* This is the same Euler-product structure as the Riemann zeta function $\zeta(s)=\prod_p(1-p^{-s})^{-1}$, and it is what makes modular $L$-functions arithmetic.

#### Pitfall

Hecke operators are defined consistently only with the $p^{k-1}$ "weight factor" — drop it and they no longer map $M_k$ to itself, and the eigenvalue/coefficient identity breaks. The factor is the same $(c\tau+d)^k$ bookkeeping as everywhere else, now attached to the degree-$p$ covering maps.

<a id="s8"></a>
### Theta functions, the Jacobi theta, and lattice sums

#### What & why

Eisenstein series came from averaging; **theta functions** come from *Gaussian lattice sums* and are the modular forms most directly tied to physics (partition functions of free fields) and to counting problems (sums of squares). Their modularity is a corollary of the **Poisson summation formula**, which we state and apply.

#### Definitions

> **Definition — Jacobi theta function.**
> $$
> \theta(\tau) = \sum_{n=-\infty}^{\infty} q^{n^2/2} = \sum_{n\in\mathbb Z} e^{\pi i n^2 \tau}, \qquad q=e^{2\pi i\tau}.
> $$
> More generally, for an even lattice $\Lambda$ with quadratic form $Q$, the **lattice theta function** is $\Theta_\Lambda(\tau)=\sum_{v\in\Lambda}q^{Q(v)/2}$.

#### Poisson summation

> **Theorem 7 (Poisson summation).** For a nice (Schwartz) function $g:\mathbb R\to\mathbb C$ with Fourier transform $\hat g(\xi)=\int_{-\infty}^\infty g(x)e^{-2\pi i x\xi}\,dx$,
> $$
> \sum_{n\in\mathbb Z} g(n) = \sum_{m\in\mathbb Z}\hat g(m).
> $$

*(Restated from [Fourier analysis] within Complex Analysis prerequisites: a rapidly decaying function equals the sum of its Fourier transform values; the proof periodizes $g$ and expands in a Fourier series.)*

#### Theorem 8 — the $S$-transformation of $\theta$

**Claim.**
$$
\theta\!\left(-\frac1\tau\right) = \sqrt{-i\tau}\;\theta(\tau).
$$
So $\theta$ transforms with weight $\frac12$ (a half-integer weight; it is a modular form for a congruence subgroup, not the full group, but the transformation law is exact).

**Proof via Poisson summation.**

1. Set $\tau=it$ with $t>0$ first (then continue analytically). Define $g(x)=e^{-\pi t x^2}$, a Gaussian. Its Fourier transform is $\hat g(\xi)=\frac{1}{\sqrt t}e^{-\pi \xi^2/t}$. *(Reason: the Gaussian is its own Fourier transform up to scaling; $\int e^{-\pi t x^2}e^{-2\pi i x\xi}dx = \frac1{\sqrt t}e^{-\pi\xi^2/t}$, the standard Gaussian integral after completing the square.)*
2. Apply Poisson summation: $\sum_n e^{-\pi t n^2} = \frac{1}{\sqrt t}\sum_m e^{-\pi m^2/t}$.
3. Recognize $\theta(it)=\sum_n e^{-\pi t n^2}$ (set $\tau=it$ so $e^{\pi i n^2\tau}=e^{-\pi t n^2}$) and $\theta(i/t)=\sum_m e^{-\pi m^2/t}$. Step 2 reads $\theta(it)=\frac{1}{\sqrt t}\theta(i/t)$.
4. Note $-1/\tau = -1/(it) = i/t$ and $\sqrt{-i\tau}=\sqrt{-i\cdot it}=\sqrt t$. So step 3 is exactly $\theta(-1/\tau)=\sqrt{-i\tau}\,\theta(\tau)$ on the imaginary axis; by the **identity theorem** (two holomorphic functions agreeing on a set with a limit point agree everywhere), it holds on all of $\mathbb H$. $\blacksquare$

The companion law $\theta(\tau+2)=\theta(\tau)$ (period 2, since $q^{n^2/2}$ shifts by $e^{\pi i n^2}=\pm1$, actually period... $\theta(\tau+1)=\sum e^{\pi i n^2(\tau+1)}=\sum e^{\pi i n^2}q^{n^2/2}$ which is the *third* theta, so $\theta$ has period $2$) generates, with $S$, the subgroup $\Gamma_\theta$.

#### Worked application: sums of squares

The number $r_k(N)$ of ways to write $N$ as a sum of $k$ squares is the $q^N$-coefficient of $\theta(\tau)^k$ (since $\theta^k=\sum_{n_1,\dots,n_k}q^{(n_1^2+\cdots+n_k^2)/2}$). Because $\theta^4$ is a weight-$2$ modular form on $\Gamma_0(4)$ and that space is spanned by Eisenstein series, one *derives* **Jacobi's four-square theorem**: $r_4(N)=8\sum_{d\mid N,\,4\nmid d}d$. The modularity turns a hard counting problem into a divisor sum — the recurring theme of the subject.

**Numerical check.** Take $N=1$: divisors $d\mid1$ with $4\nmid d$ is just $d=1$, so $r_4(1)=8$. Directly: $1=(\pm1)^2$ in one of four coordinate slots, each with a sign, $=4\times2=8$ representations. Take $N=2$: divisors $1,2$ (neither divisible by $4$), sum $3$, so $r_4(2)=24$. Directly: $2=1^2+1^2$ using two of the four slots; choose the two slots ($\binom42=6$ ways), each nonzero coordinate has a sign ($2^2=4$), giving $24$. Agreement — the modular machine reproduces the brute-force count.

#### Even unimodular lattices and the dimension $8\mathbb Z$

A lattice theta function $\Theta_\Lambda$ for an **even unimodular** lattice (integer inner products, all norms even, determinant $1$) is a modular form of weight $n/2$ where $n=\dim\Lambda$. Modularity forces $n\equiv0\pmod 8$. *(Reason: weight must be even integer for a form on the full group, and the $\theta$ transformation phase is consistent only when $8\mid n$.)* In dimension $8$ this gives the $E_8$ lattice, whose theta function is $\Theta_{E_8}=E_4$ — so the deep object $E_4$ is literally a count of $E_8$ lattice vectors by length. In dimension $24$ the **Leech lattice** appears, and the difference $\Theta_{\text{Leech}}-E_4^3$ is a weight-$12$ cusp form, hence a multiple of $\Delta$. This is the bridge from modular forms to sphere packing and to the monstrous moonshine surrounding $j$.

<a id="s9"></a>
### The Dedekind eta function and the CFT/string partition function

#### What & why

The **Dedekind eta function** $\eta$ is the most physical modular object: it is essentially the partition function of a single free boson or a string oscillator, and its $24$th power is $\Delta$. Its transformation law contains the **central charge** of conformal field theory and the **modular anomaly** that fixes the critical dimension of strings.

#### Definition and the product formula for $\Delta$

> **Definition — Dedekind eta.**
> $$
> \eta(\tau) = q^{1/24}\prod_{n=1}^\infty (1-q^n), \qquad q=e^{2\pi i\tau}.
> $$

Comparing with §s5, $\eta(\tau)^{24} = q\prod_n(1-q^n)^{24} = \Delta(\tau)$. So $\Delta=\eta^{24}$, which (since the product never vanishes on $\mathbb H$, each factor $1-q^n\ne0$ for $|q|<1$) re-proves $\Delta\ne0$ on $\mathbb H$.

#### Theorem 9 — the $\eta$ transformation law

**Claim.**
$$
\eta(\tau+1) = e^{\pi i/12}\,\eta(\tau), \qquad \eta\!\left(-\frac1\tau\right) = \sqrt{-i\tau}\;\eta(\tau).
$$

**Proof of the two laws.**

1. *Translation.* $\eta(\tau+1)=e^{2\pi i(\tau+1)/24}\prod(1-q^ne^{2\pi i n})=e^{\pi i/12}q^{1/24}\prod(1-q^n)=e^{\pi i/12}\eta(\tau)$, since $e^{2\pi i n}=1$. *(Reason: only the prefactor $q^{1/24}$ picks up the phase $e^{2\pi i/24}=e^{\pi i/12}$.)*
2. *Inversion.* Take the logarithm: $\log\eta(\tau)=\frac{\pi i\tau}{12}+\sum_{n\ge1}\log(1-q^n)=\frac{\pi i\tau}{12}-\sum_{n\ge1}\sum_{m\ge1}\frac{q^{nm}}{m}$. The double sum is $-\sum_{m\ge1}\frac1m\frac{q^m}{1-q^m}$. One then evaluates the difference $\log\eta(-1/\tau)-\log\eta(\tau)$ by contour-integrating $\cot$ kernels (the same Lipschitz technology as §s4) and finds the $\frac12\log(-i\tau)$ term plus a constant; the constant is pinned by checking the fixed point $\tau=i$ (where $-1/i=i$, so $\eta(i)=\sqrt{-i\cdot i}\,\eta(i)=\eta(i)$ consistent). The clean modern proof uses that $\eta^{24}=\Delta$ has weight 12, so $\eta$ has weight $\frac{12}{24}=\frac12$ up to a 24th root of unity, which the explicit constant determination fixes to $\sqrt{-i\tau}$. $\blacksquare$

#### The CFT partition function and the central charge

In a $1+1$ dimensional conformal field theory on a torus of modular parameter $\tau$, the partition function is
$$
Z(\tau,\bar\tau) = \operatorname{Tr}\,q^{L_0-c/24}\,\bar q^{\bar L_0 - c/24},
$$
where $L_0$ is the energy operator, $c$ is the **central charge** (a number measuring the "number of degrees of freedom"), and the shift $-c/24$ is the **Casimir energy** of the cylinder. (Restated from the [Conformal Field Theory](conformal-field-theory.md) guide: modular invariance of $Z$ is the torus consistency condition.) For a single free boson ($c=1$),
$$
Z_{\text{boson}}(\tau) \propto \frac{1}{\sqrt{\operatorname{Im}\tau}\;|\eta(\tau)|^2}.
$$

**The modular anomaly = central charge.** Under $S:\tau\to-1/\tau$, the factor $q^{-c/24}=e^{-2\pi i\tau(-c/24)}$ combines with the $\eta$ inversion law. The would-be anomalous phase $e^{\pi i/12}$ per oscillator under $T$ is exactly $e^{2\pi i\, c/24}$ with $c=\frac12$ per real boson contribution — so the requirement that $Z$ be modular invariant forces the $-c/24$ shift to take its precise value. The "$24$" in $\eta$ and the "$26$" critical dimension of the bosonic string ($26 = 24 + 2$ transverse vs. light-cone) are the *same* $24$: cancelling the modular ($\eta$) anomaly requires $24$ transverse oscillators, hence $c=24\cdot1=24$ matching the $\eta^{24}=\Delta$ weight-12 structure.

<a id="s10"></a>
### $L$-functions, the Mellin transform, and modularity

#### What & why

Attached to a modular form is a **Dirichlet series** built from its coefficients — its **$L$-function** — which carries the deep arithmetic. The bridge between the modular form (a function on $\mathbb H$) and its $L$-function (a function on $\mathbb C$) is the **Mellin transform**, and the modular $S$-transformation becomes a **functional equation** for $L$. This is the technology behind the **modularity theorem** (formerly the Taniyama–Shimura conjecture) used to prove Fermat's Last Theorem.

#### Definitions

> **Definition — $L$-function of a cusp form.** For a cusp form $f=\sum_{n\ge1}a_nq^n$ of weight $k$,
> $$
> L(f,s) = \sum_{n=1}^\infty \frac{a_n}{n^s},
> $$
> a **Dirichlet series** in the complex variable $s$, convergent for $\operatorname{Re}s$ large.

> **Definition — Mellin transform.** For a function $h(t)$ on $(0,\infty)$, $\ \mathcal M[h](s)=\int_0^\infty h(t)\,t^{s}\,\frac{dt}{t}$.

#### Theorem 10 — the completed $L$-function and its functional equation

**Claim.** Define the **completed $L$-function** $\Lambda(f,s) = (2\pi)^{-s}\Gamma(s)\,L(f,s)$ ($\Gamma$ the gamma function). Then $\Lambda(f,s)$ extends to an entire function of $s$ and satisfies the **functional equation**
$$
\Lambda(f,s) = (-1)^{k/2}\,\Lambda(f,\,k-s).
$$

**Proof.**

1. *Mellin-transform the form along the imaginary axis.* Put $\tau=it$ ($t>0$), so $q=e^{-2\pi t}$ and $f(it)=\sum_{n\ge1}a_n e^{-2\pi n t}$. Compute
   $$
   \int_0^\infty f(it)\,t^s\,\frac{dt}{t} = \sum_{n\ge1}a_n\int_0^\infty e^{-2\pi n t}t^s\frac{dt}{t} = \sum_{n\ge1}a_n\,(2\pi n)^{-s}\Gamma(s) = (2\pi)^{-s}\Gamma(s)L(f,s)=\Lambda(f,s).
   $$
   *(Reason: $\int_0^\infty e^{-at}t^{s-1}dt = a^{-s}\Gamma(s)$, the definition of $\Gamma$ after rescaling; interchange of sum and integral is justified by absolute convergence since $f$ is a cusp form, decaying exponentially as $t\to\infty$.)*
2. *Split and use modularity.* Break the integral at $t=1$: $\Lambda=\int_0^1+\int_1^\infty$. In $\int_0^1$ substitute $t\to1/t$ and use the $S$-law $f(i/t)=f(-1/(it))=(it)^k f(it)=i^k t^k f(it)$ — for $S=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ acting on $\tau=it$ with $i^k=(-1)^{k/2}$ for even $k$. This converts $\int_0^1 \to (-1)^{k/2}\int_1^\infty f(it)t^{k-s}\frac{dt}{t}$.
3. *Symmetric form.* Adding the two pieces,
   $$
   \Lambda(f,s) = \int_1^\infty f(it)\big(t^s + (-1)^{k/2}t^{k-s}\big)\frac{dt}{t}.
   $$
   The integrand decays exponentially at $t=\infty$ (cusp form), so the integral converges for **all** $s$ — $\Lambda$ is entire. *(Reason: exponential decay beats any power $t^{s}$.)*
4. *Read off symmetry.* The right side is manifestly invariant under $s\mapsto k-s$ together with multiplying by $(-1)^{k/2}$, which is the stated functional equation. $\blacksquare$

#### A statement of modularity

> **Theorem (Modularity, statement only).** Every **elliptic curve** over $\mathbb Q$ (a cubic equation $y^2=x^3+ax+b$ with rational $a,b$ and nonzero discriminant) is **modular**: its arithmetic $L$-function $L(E,s)=\sum a_n n^{-s}$, built by counting points of $E$ over each finite field, equals $L(f,s)$ for some weight-$2$ Hecke eigenform $f$ of level $N$ (the conductor of $E$). Equivalently, $\sum a_n q^n$ is a modular form.

This is the Taniyama–Shimura–Weil conjecture, proved by Wiles and Taylor (and extended by Breuil–Conrad–Diamond–Taylor). Its weight-2 case for **semistable** curves, combined with Ribet's theorem, yields **Fermat's Last Theorem**: a hypothetical solution $a^p+b^p=c^p$ would build a non-modular elliptic curve, contradicting modularity. The functional equation of Theorem 10 (generalized to level $N$) is the analytic shadow of this deep correspondence.

#### Worked example

For $\Delta$ (weight $12$), $L(\Delta,s)=\sum\tau(n)n^{-s}$, and the functional equation relates $s\leftrightarrow 12-s$ with sign $(-1)^6=+1$, so $\Lambda(\Delta,s)=\Lambda(\Delta,12-s)$, symmetric about $\operatorname{Re}s=6$. Multiplicativity of $\tau$ (§s7) makes $L(\Delta,s)$ factor as an **Euler product** $\prod_p(1-\tau(p)p^{-s}+p^{11-2s})^{-1}$.

#### Why the Mellin transform is the right bridge

The reason the Mellin transform converts modularity into a functional equation is structural: the multiplicative group $(0,\infty)$ acts on $t$ by scaling, and the Mellin transform is its **Fourier transform**, diagonalizing scaling into the variable $s$. The $S$-transformation $\tau\mapsto-1/\tau$ restricts on the imaginary axis to the inversion $t\mapsto 1/t$ — a reflection of the multiplicative group — and Fourier-transforming a reflection produces $s\mapsto k-s$. So the symmetry $s\leftrightarrow k-s$ is the *Mellin shadow* of the inversion symmetry $S$, exactly as the $q$-expansion is the *Fourier shadow* of the translation $T$. The two generators of §s2 thus govern the two analytic faces of a modular form: $T$ gives the Dirichlet series, $S$ gives its functional equation.

#### The Ramanujan–Petersson bound (statement)

The size of the eigenvalues is itself controlled: for a weight-$k$ Hecke eigenform, $|a_p|\le 2\,p^{(k-1)/2}$. For $\Delta$ this is $|\tau(p)|\le 2p^{11/2}$, Ramanujan's conjecture, proved by Deligne as a consequence of the Weil conjectures in algebraic geometry. It says the two roots of the local Euler factor $1-a_pX+p^{k-1}X^2$ are complex conjugates of equal modulus $p^{(k-1)/2}$ — the "Riemann hypothesis" for these local factors. The appearance of deep geometry (étale cohomology) to bound coefficients of a $q$-series is a measure of how far the arithmetic of modular forms reaches.

## Part D · Physics

<a id="s11"></a>
### Modular invariance, T-duality, and Eisenstein series in string amplitudes

#### What & why

We close by collecting the physics that motivated §s0, now with the machinery to state it precisely: why partition functions *must* be modular, how T-duality realizes $SL(2,\mathbb{Z})$ physically, and where Eisenstein series appear in scattering amplitudes.

#### Modular invariance of the torus partition function

A two-dimensional field theory on a torus is specified by a modular parameter $\tau$ (the torus's shape). Two tori with $\tau$ and $\gamma\cdot\tau$ ($\gamma\in SL(2,\mathbb{Z})$) are the *same* surface — $\gamma$ is a **large diffeomorphism** (a coordinate change not connected to the identity, i.e. a relabeling of which cycle is "space" vs. "time").

> **Physical requirement.** The partition function must satisfy $Z(\gamma\cdot\tau,\overline{\gamma\cdot\tau}) = Z(\tau,\bar\tau)$ for all $\gamma\in SL(2,\mathbb{Z})$.

For the free boson (§s9), $Z=\frac{1}{\sqrt{\operatorname{Im}\tau}|\eta(\tau)|^2}$ is invariant precisely because:
1. $\operatorname{Im}\tau$ transforms as $\operatorname{Im}(\gamma\tau)=\operatorname{Im}\tau/|c\tau+d|^2$ (master formula, §s1), contributing $|c\tau+d|$;
2. $|\eta(\gamma\tau)|^2$ transforms by $|c\tau+d|^{1}$ from each of $\eta,\bar\eta$ (weight $\tfrac12$ each), contributing $|c\tau+d|^{-1}$ when in the denominator squared... the powers cancel exactly. *(Reason: the weight-$\frac12$ of $\eta$ and the weight-$(-\frac12)$ of $(\operatorname{Im}\tau)^{-1/2}$ are tuned to cancel — this is the modular-invariance condition, and it is what fixes $c=1$ for a single boson and the $-c/24$ Casimir shift.)*

The constraint is so strong that for a CFT to be consistent, its spectrum of states must organize into a modular-invariant combination of characters — the **modular bootstrap**.

#### T-duality as $SL(2,\mathbb{Z})$

Compactify a string on a circle of radius $R$. The string has **momentum modes** (energy $\sim n/R$, integer $n$) and **winding modes** (energy $\sim wR$, integer $w$, counting how many times the string wraps the circle). The spectrum is *invariant* under
$$
R \longleftrightarrow \frac{\alpha'}{R},\qquad n\longleftrightarrow w,
$$
exchanging momentum and winding ($\alpha'$ is the string length-squared). This is **T-duality**. For a string on a 2-torus, the two radii and the $B$-field combine into a complex modulus $\rho$, and T-dualities plus large diffeomorphisms generate an $SL(2,\mathbb{Z})\times SL(2,\mathbb{Z})$ acting on the torus moduli $(\tau,\rho)$ by exactly the Möbius transformations of §s1. Physical quantities are therefore modular functions/forms of these moduli — and that is *why* the mathematics of this guide governs string compactifications.

#### Eisenstein series in string amplitudes

The low-energy effective action of type IIB string theory contains a famous **$R^4$ correction** (a four-graviton interaction). Its coefficient, as a function of the complex coupling $\tau = \frac{\theta}{2\pi}+\frac{i}{g_s}$ (axion–dilaton, with string coupling $g_s$), is required by S-duality $SL(2,\mathbb{Z})$ to be modular invariant of weight $0$, and it equals the **non-holomorphic Eisenstein series**
$$
E_{3/2}(\tau) = \sum_{(m,n)\ne(0,0)} \frac{(\operatorname{Im}\tau)^{3/2}}{|m\tau+n|^{3}}.
$$
Its $q$-expansion has exactly two power-law terms (tree-level and one-loop in $g_s$) plus exponentially small **D-instanton** corrections — a structure *predicted purely by modularity*. The appearance of $E_{3/2}$ (and higher $E_s$ for higher corrections) is one of the cleanest places where the Eisenstein series of §s4 enter physics directly, their automorphy encoding the non-perturbative completion of a perturbative expansion.

#### Worked structure of $E_{3/2}$: how modularity predicts physics

The non-holomorphic Eisenstein series $E_s(\tau)=\sum_{(m,n)\ne0}\frac{(\operatorname{Im}\tau)^s}{|m\tau+n|^{2s}}$ has, by a Poisson-summation computation in the $n$ variable (the same tool as §s8), an exact expansion of the form
$$
E_s(\tau)=2\zeta(2s)\,y^s + 2\sqrt\pi\,\frac{\Gamma(s-\tfrac12)\zeta(2s-1)}{\Gamma(s)}\,y^{1-s} + (\text{exponentially small in } y),
$$
with $y=\operatorname{Im}\tau=1/g_s$. Read physically at $s=\tfrac32$: the first term $\sim y^{3/2}=g_s^{-3/2}$ is the **tree-level** contribution, the second $\sim y^{-1/2}=g_s^{1/2}$ is the **one-loop** contribution, and the exponentially small remainder $\sim e^{-2\pi y}=e^{-2\pi/g_s}$ are the **D-instanton** effects. *(Reason: powers of $y=1/g_s$ are powers of the coupling, and $e^{-1/g_s}$ is the hallmark of a non-perturbative instanton.)* Crucially, perturbation theory alone could never tell you there are *exactly two* power-law terms and no others — that the series truncates after tree and one loop is a *theorem* forced by $SL(2,\mathbb Z)$ invariance plus the eigenvalue equation $\Delta_{\mathbb H}E_s=s(s-1)E_s$ (with $\Delta_{\mathbb H}$ the hyperbolic Laplacian). Modularity thereby *predicts* the entire non-perturbative coupling dependence of a physical coefficient. This is the sharpest payoff of the whole guide: rigidity becomes prediction.

#### Pitfalls and the unifying picture

- T-duality is *exact*, not approximate: it is a true equivalence of theories, the physical incarnation of the $S$ generator.
- "Modular invariant" in physics usually means weight $0$ (a modular *function*); the weight-$k$ forms enter as building blocks (characters, theta functions) that *combine* into invariants.
- The single thread: a discrete symmetry acting as integer Möbius transformations forces physical observables to be modular, and the rigidity of modular forms then *determines* those observables — from the spectrum of a CFT to the non-perturbative coefficients of string amplitudes.

---

*This guide built the theory of modular forms from its foundation — the action of $SL(2,\mathbb{Z})$ on the upper half-plane by Möbius transformations, its fundamental domain, and the generators $S$ and $T$ proven to generate the whole group — up through the canonical forms: Eisenstein series with their divisor-sum $q$-expansions and the $E_2$ anomaly, the discriminant $\Delta=\eta^{24}$, the $j$-invariant, and the finite-dimensional graded ring $\mathbb{C}[E_4,E_6]$ whose dimensions follow from the valence formula proved by contour integration. We then reached the arithmetic heart — Hecke operators and the multiplicativity of eigenform coefficients, theta functions modular by Poisson summation, the Dedekind eta carrying the CFT central charge, and $L$-functions whose Mellin-transform functional equation underlies the modularity theorem and Fermat's Last Theorem. Finally physics closed the circle: partition functions must be modular invariant because large diffeomorphisms of the torus act as $SL(2,\mathbb{Z})$, T-duality realizes that symmetry physically, and Eisenstein series fix the non-perturbative coefficients of string amplitudes. The lesson throughout: symmetry under integer Möbius transformations is so rigid that it turns infinite questions into finite, exactly solvable ones — the same miracle, whether the question is arithmetic or physical.*
