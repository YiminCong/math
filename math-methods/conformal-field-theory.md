**English** · [中文](conformal-field-theory.zh.md)

# Conformal Field Theory, *symmetry taken to infinity.*

*A self-contained first course in two-dimensional conformal field theory — from the question "what survives when a physical system forgets its scale?" to the Virasoro algebra, the operator product expansion, the conformal bootstrap of correlation functions, the representation theory of Virasoro modules, the minimal models, and modular invariance on the torus. Every term is defined in words on first use, every formula is motivated, and every derivation is a numbered, gap-free chain of reasons. We build on basic algebra and single-variable calculus, and we draw on two companion guides: [Complex Analysis](../complex-analysis/complex-analysis.md) for holomorphic functions, Laurent series, and contour integration, and [Group Theory / Lie Representations](../group-theory/lie-representations.md) for Lie algebras and their representations. Each borrowed fact is restated in one line where it is used.*

[← Back to all guides](../README.md)

## Part A · Why conformal symmetry, and why two dimensions

<a id="s0"></a>
### Motivation: critical phenomena, RG fixed points, and string theory

#### What this guide is about, in one breath

A **symmetry** of a physical system is a transformation of space (and time) that leaves the system's laws unchanged. Ordinary symmetries — translations, rotations — form a finite-dimensional group, and they constrain a theory only a little. A **conformal symmetry** is a transformation that preserves *angles* but not necessarily lengths: it may stretch the space differently at different points, as long as it does so uniformly in all directions at each point. In most dimensions the conformal symmetries still form a finite group. But in *two* dimensions, as we will prove in §s1–s2, there are *infinitely many* independent conformal transformations. A theory invariant under infinitely many symmetries is constrained so tightly that one can often solve it *exactly*, with no approximation. This guide is the mathematics of that miracle.

#### Three motivating arenas

- **Critical phenomena.** Heat a magnet. Below a special temperature $T_c$ — the **critical temperature** — it is magnetized; above it, not. Exactly *at* $T_c$ the magnet is **scale invariant**: zoom in on a snapshot of the up/down spins and the new picture looks statistically identical to the old. There is no characteristic length — the **correlation length** (the typical distance over which two spins "know about" each other) has become infinite. A scale-invariant statistical system, when also rotation- and translation-invariant and local, is almost always invariant under the full conformal group. The two-dimensional **Ising model** (a square grid of spins $\pm1$, each preferring to align with its neighbors) sits at such a critical point, and we will identify it in §s10 as the conformal field theory with **central charge** $c=\tfrac12$.

- **The renormalization group and its fixed points.** The **renormalization group** (RG) is the procedure of repeatedly "coarse-graining" a system — averaging out short-distance detail and rescaling — and watching how its effective description flows. A **fixed point** of this flow is a theory that maps to *itself* under coarse-graining: it is scale invariant, hence (under the mild assumptions above) conformally invariant. Fixed points govern the large-distance physics of *every* theory that flows to them, so classifying conformal field theories classifies the possible long-distance behaviors of matter. This is why CFT is the language of critical phenomena.

- **String theory.** A **string** is a one-dimensional object that, as it moves through spacetime, sweeps out a two-dimensional surface called the **worldsheet** (just as a moving point sweeps out a one-dimensional worldline). The quantum theory of the string is a field theory living on that two-dimensional worldsheet, and the freedom to redraw the worldsheet's coordinates without changing the physics is exactly two-dimensional conformal invariance. The consistency conditions of string theory — including the famous requirement of 26 (or, with supersymmetry, 10) spacetime dimensions — are conditions on a two-dimensional CFT.

#### Why two dimensions is uniquely powerful

In $d>2$ dimensions the conformal group is finite-dimensional (we count its parameters in §s1): it is the group $SO(d+1,1)$, with $\tfrac12(d+1)(d+2)$ generators. Finite symmetry pins down some data (it fixes the form of two- and three-point correlation functions, §s7) but cannot solve the theory. In $d=2$, by contrast, the local conformal transformations are the **holomorphic maps** of the complex plane (§s2), of which there are infinitely many. The corresponding **infinite-dimensional** algebra of generators — the Witt algebra (§s2), promoted in the quantum theory to the Virasoro algebra (§s3) — is so large that it organizes the entire spectrum of the theory into a few representations and fixes the dynamics. This is the sense in which $d=2$ takes symmetry "to infinity."

#### The whole guide on one line

> conformal group in $d$ dim → holomorphic maps in 2D → Witt → Virasoro & central charge → primary fields → radial quantization & state–operator map → OPE & stress tensor → correlators fixed by symmetry → Ward identities → Verma modules & null states → minimal models → modular invariance

#### Common pitfalls

- "Conformal" means **angle-preserving**, not **shape-preserving**. A conformal map can grossly distort a figure's overall shape; it only preserves angles *locally*, between curves crossing at a point.
- Scale invariance and conformal invariance are *not* identical in general — full conformal invariance is a stronger statement. For the local, unitary theories of this guide the two coincide, but the implication "scale $\Rightarrow$ conformal" is a theorem with hypotheses, not a definition.

<a id="s1"></a>
### Conformal transformations in $d$ dimensions; the conformal group

#### What & why

Before specializing to two dimensions we define the conformal group in *any* dimension $d$, count its generators, and see exactly where $d=2$ breaks the pattern. This makes the later infinitude concrete: we will literally watch a finite count become infinite.

#### Defining a conformal transformation through the metric

We work in flat $d$-dimensional space with coordinates $x=(x^1,\dots,x^d)$. The **metric** $g_{\mu\nu}$ is the array of numbers that turns coordinate differences into squared distances: an infinitesimal displacement $dx^\mu$ has squared length $ds^2=g_{\mu\nu}\,dx^\mu dx^\nu$. (Repeated indices are summed — the **Einstein summation convention** — so $g_{\mu\nu}dx^\mu dx^\nu$ means $\sum_{\mu,\nu}g_{\mu\nu}dx^\mu dx^\nu$.) In flat Euclidean space $g_{\mu\nu}=\delta_{\mu\nu}$, the **Kronecker delta** ($1$ if $\mu=\nu$, else $0$), so $ds^2=(dx^1)^2+\cdots+(dx^d)^2$.

> **Definition — conformal transformation.** A smooth, invertible change of coordinates $x\mapsto x'(x)$ is **conformal** if it rescales the metric by a single positive function $\Omega(x)^2$, the same factor in every direction at each point:
> $$
> g_{\mu\nu}\big(x'\big)\,\frac{\partial x'^{\rho}}{\partial x^{\mu}}\frac{\partial x'^{\sigma}}{\partial x^{\nu}} \;=\; \Omega(x)^{2}\,g_{\rho\sigma}(x).
> $$
> The factor $\Omega(x)$ is the **local scale factor**. Because the same $\Omega$ multiplies all directions, the *angle* between any two vectors — a ratio of dot products — is unchanged, while lengths are scaled by $\Omega$. This is the precise meaning of "angle-preserving."

#### The infinitesimal condition

To find all conformal transformations we look at those infinitesimally close to the identity. Write $x'^\mu=x^\mu+\epsilon^\mu(x)$ with $\epsilon$ small, and $\Omega(x)^2=1+\omega(x)$ with $\omega$ small.

1. **Linearize the metric condition.** Substituting into the definition and keeping only first-order terms in $\epsilon$, the change in the flat metric is $\partial_\mu\epsilon_\nu+\partial_\nu\epsilon_\mu$, where $\epsilon_\mu=\delta_{\mu\nu}\epsilon^\nu$ and $\partial_\mu=\partial/\partial x^\mu$. *(Reason: differentiate $x'^\rho=x^\rho+\epsilon^\rho$ to get $\partial x'^\rho/\partial x^\mu=\delta^\rho_\mu+\partial_\mu\epsilon^\rho$, multiply out, and drop the $(\partial\epsilon)^2$ term.)* The condition becomes
$$
\partial_\mu\epsilon_\nu+\partial_\nu\epsilon_\mu=\omega(x)\,\delta_{\mu\nu}.
$$

2. **Solve for $\omega$ by taking a trace.** Set $\mu=\nu$ and sum (contract with $\delta^{\mu\nu}$). The left side becomes $2\,\partial_\mu\epsilon^\mu$ and the right becomes $\omega\,\delta^\mu_\mu=\omega\,d$. *(Reason: $\delta^\mu_\mu=d$, the trace of the identity in $d$ dimensions.)* Hence
$$
\omega=\frac{2}{d}\,\partial_\mu\epsilon^\mu,
\qquad
\partial_\mu\epsilon_\nu+\partial_\nu\epsilon_\mu=\frac{2}{d}\,(\partial\cdot\epsilon)\,\delta_{\mu\nu}.
$$
This is the **conformal Killing equation**: its solutions $\epsilon^\mu(x)$ are exactly the infinitesimal conformal transformations.

3. **Extract a third-derivative constraint.** Acting with derivatives and combining the equation with itself (apply $\partial^\rho$, permute indices, add and subtract) yields, after a standard manipulation, $(d-1)\,\partial^2\partial_\mu(\partial\cdot\epsilon)=0$ and $(2-d)\,\partial_\mu\partial_\nu(\partial\cdot\epsilon)=0$. *(Reason: these follow by linear algebra from the Killing equation; the key point is the explicit factors of $d$.)* For $d>2$ the factor $(2-d)\neq0$ forces $\partial_\mu\partial_\nu(\partial\cdot\epsilon)=0$, so $\partial\cdot\epsilon$ is **at most linear** in $x$, hence $\epsilon^\mu$ is at most **quadratic** in $x$. For $d=2$ the factor vanishes and the constraint disappears — this is the first sign that $d=2$ is special.

#### The finite generators (any $d\ge 3$)

Because $\epsilon^\mu$ is at most quadratic, the most general solution is a sum of four kinds of terms. Each is a generator of the conformal group:

- **Translations** $\epsilon^\mu=a^\mu$ (constant): shift the origin. $d$ parameters.
- **Rotations** $\epsilon^\mu=\omega^\mu{}_\nu x^\nu$ with $\omega_{\mu\nu}=-\omega_{\nu\mu}$ (antisymmetric): rigidly rotate. $\tfrac12 d(d-1)$ parameters.
- **Dilations** $\epsilon^\mu=\lambda\, x^\mu$: uniform rescaling $x\mapsto e^{\lambda}x$. $1$ parameter. This is the new symmetry beyond rigid motions — it stretches all distances by a common factor and is exactly the "forget the scale" symmetry of §s0.
- **Special conformal transformations** (SCTs) $\epsilon^\mu=2(b\cdot x)x^\mu-x^2 b^\mu$. $d$ parameters. Finitely, an SCT is an **inversion** $x^\mu\mapsto x^\mu/x^2$, followed by a translation by $b^\mu$, followed by another inversion. It is the least intuitive generator; geometrically it is the conformal map that an inversion makes out of an ordinary translation.

> **Counting (the punchline).** Total parameters $=d+\tfrac12 d(d-1)+1+d=\tfrac12(d+1)(d+2)$. This is exactly the dimension of the group $SO(d+1,1)$ — the rotation group of a space with $d+1$ "space" and $1$ "time" direction. So in $d\ge3$ the conformal group is the *finite-dimensional* Lie group $SO(d+1,1)$. *(We use here the one fact from [Lie Representations](../group-theory/lie-representations.md) that a Lie group's dimension equals the number of independent infinitesimal generators.)*

#### Worked count in $d=4$

Translations $4$, rotations $\tfrac12\cdot4\cdot3=6$, dilation $1$, SCTs $4$, total $15$. And $\tfrac12(4+1)(4+2)=\tfrac12\cdot5\cdot6=15$. The four-dimensional conformal group is $SO(5,1)$, with $15$ generators — the symmetry group exploited in modern studies of gauge theory.

#### Why $d=2$ is special, stated now

In step 3 the factor $(2-d)$ that forced $\epsilon^\mu$ to be quadratic *vanishes* at $d=2$. The constraint evaporates, and $\epsilon^\mu$ may be an *arbitrary* solution of the two-dimensional Killing equation — which, we show next, is the statement that a certain function is **holomorphic**. Holomorphic functions form an infinite-dimensional space (any convergent power series), so the conformal "group" in two dimensions has infinitely many generators. §s2 makes this exact.

<a id="s2"></a>
### Conformal maps in 2D as holomorphic maps; the Witt algebra

#### What & why

We now specialize to $d=2$ and prove the central structural fact of the whole subject: *infinitesimal conformal maps in two dimensions are exactly holomorphic functions.* From there we read off an infinite set of generators and compute the algebra they close into — the **Witt algebra**.

#### From the Killing equation to the Cauchy–Riemann equations

Work in the Euclidean plane with coordinates $(x^1,x^2)$ and metric $\delta_{\mu\nu}$. At $d=2$ the conformal Killing equation $\partial_\mu\epsilon_\nu+\partial_\nu\epsilon_\mu=(\partial\cdot\epsilon)\,\delta_{\mu\nu}$ has three components:

1. **The $(1,1)$ and $(2,2)$ components** read $2\partial_1\epsilon_1=\partial_1\epsilon_1+\partial_2\epsilon_2$ and $2\partial_2\epsilon_2=\partial_1\epsilon_1+\partial_2\epsilon_2$. Subtracting gives $\partial_1\epsilon_1=\partial_2\epsilon_2$. *(Reason: at $d=2$, $\tfrac{2}{d}=1$, so the trace term is just $\partial\cdot\epsilon=\partial_1\epsilon_1+\partial_2\epsilon_2$.)*

2. **The $(1,2)$ component** reads $\partial_1\epsilon_2+\partial_2\epsilon_1=0$, i.e. $\partial_1\epsilon_2=-\partial_2\epsilon_1$.

3. **Recognize the Cauchy–Riemann equations.** The two relations $\partial_1\epsilon_1=\partial_2\epsilon_2$ and $\partial_1\epsilon_2=-\partial_2\epsilon_1$ are precisely the **Cauchy–Riemann equations** for the complex function $\epsilon(z):=\epsilon_1+i\epsilon_2$ of $z:=x^1+ix^2$. *(Reason — restating the one fact we borrow from [Complex Analysis](../complex-analysis/complex-analysis.md): a function $f=u+iv$ of $z=x+iy$ is holomorphic — complex-differentiable — exactly when $\partial u/\partial x=\partial v/\partial y$ and $\partial u/\partial y=-\partial v/\partial x$.)* Thus $\epsilon(z)$ is **holomorphic**: it depends on $z$ but not on the conjugate $\bar z=x^1-ix^2$.

#### Complex coordinates and the holomorphic/antiholomorphic split

It is cleaner to use $z$ and $\bar z$ as independent coordinates. Then the corresponding derivatives are
$$
\partial \equiv \partial_z=\tfrac12(\partial_1-i\partial_2),
\qquad
\bar\partial\equiv\partial_{\bar z}=\tfrac12(\partial_1+i\partial_2),
$$
and the line element factorizes as $ds^2=dz\,d\bar z$. An infinitesimal conformal map is then $z\mapsto z+\epsilon(z)$, $\bar z\mapsto \bar z+\bar\epsilon(\bar z)$, where $\epsilon$ depends only on $z$ (holomorphic) and $\bar\epsilon$ only on $\bar z$ (**antiholomorphic**). The full transformation factorizes into an independent holomorphic piece and an antiholomorphic piece. We develop the holomorphic part; the antiholomorphic part is its mirror image, with bars on everything, and the two sectors combine at the end.

> **Finite version.** Integrating the infinitesimal maps, a *finite* two-dimensional conformal transformation is any holomorphic map $z\mapsto f(z)$ (together with an independent $\bar z\mapsto \bar f(\bar z)$). Holomorphic maps preserve angles — this is the classical geometric meaning of "conformal" from complex analysis — so the two notions of "conformal" coincide. There are infinitely many such $f$, confirming the infinite-dimensionality promised in §s1.

#### The generators and the Witt algebra

To organize this infinite set, expand a holomorphic infinitesimal map in powers of $z$. A basis of "elementary" infinitesimal maps is $\epsilon(z)=-z^{n+1}$ for each integer $n$, with associated **generator** (a differential operator acting on functions of $z$)
$$
\ell_n=-z^{n+1}\,\partial_z,\qquad n\in\mathbb{Z}.
$$
Here the minus sign and the $n+1$ power are conventions chosen so the algebra below comes out clean. The antiholomorphic copies are $\bar\ell_n=-\bar z^{n+1}\partial_{\bar z}$.

> **Theorem (Witt algebra).** The generators satisfy the **commutator** relations
> $$
> [\ell_m,\ell_n]=(m-n)\,\ell_{m+n},
> \qquad
> [\bar\ell_m,\bar\ell_n]=(m-n)\,\bar\ell_{m+n},
> \qquad
> [\ell_m,\bar\ell_n]=0,
> $$
> where the **commutator** of two operators is $[A,B]:=AB-BA$ (it measures their failure to commute). This infinite-dimensional Lie algebra is the **Witt algebra**. The vanishing of $[\ell_m,\bar\ell_n]$ says the holomorphic and antiholomorphic sectors are completely independent.

**Proof (gap-free).**
1. Compute $\ell_m\ell_n f$ for a test function $f(z)$. By definition $\ell_n f=-z^{n+1}f'$, so
$$
\ell_m\ell_n f=-z^{m+1}\partial_z\!\big(-z^{n+1}f'\big)=z^{m+1}\big[(n+1)z^{n}f'+z^{n+1}f''\big].
$$
*(Reason: the product rule on $z^{n+1}f'$.)*
2. Simplify: $\ell_m\ell_n f=(n+1)z^{m+n+1}f'+z^{m+n+2}f''$.
3. Swap $m\leftrightarrow n$ to get $\ell_n\ell_m f=(m+1)z^{m+n+1}f'+z^{m+n+2}f''$. *(Reason: the expression in step 2 is symmetric under the swap except for the coefficient $n+1\to m+1$.)*
4. Subtract. The $f''$ terms cancel identically, leaving
$$
[\ell_m,\ell_n]f=\big[(n+1)-(m+1)\big]z^{m+n+1}f'=(n-m)\,z^{m+n+1}f'.
$$
5. Recognize the right side: $(n-m)z^{m+n+1}f'=-(n-m)\,\ell_{m+n}f=(m-n)\,\ell_{m+n}f$. *(Reason: $\ell_{m+n}=-z^{m+n+1}\partial_z$.)* Hence $[\ell_m,\ell_n]=(m-n)\ell_{m+n}$. The antiholomorphic computation is identical with bars; the cross-commutator vanishes because $\partial_z$ and $\partial_{\bar z}$ commute and act on independent variables. $\blacksquare$

#### The finite subalgebra inside the infinite one

Among all the $\ell_n$, exactly three — $\ell_{-1},\ell_0,\ell_{+1}$ — together with their bars, generate transformations that are **globally well-defined** on the sphere (the plane plus its point at infinity). They are
- $\ell_{-1}=-\partial_z$: **translations**;
- $\ell_0=-z\partial_z$: **dilations and rotations** (a complex rescaling);
- $\ell_{+1}=-z^2\partial_z$: **special conformal transformations**.

From the Witt relations, $\{\ell_{-1},\ell_0,\ell_{+1}\}$ close among themselves ($[\ell_0,\ell_{\pm1}]=\mp\ell_{\pm1}$, $[\ell_{-1},\ell_{+1}]=-2\ell_0$); with the bars this is a six-real-parameter group, the **global conformal group** $SL(2,\mathbb{C})$, acting by **Möbius transformations** $z\mapsto\frac{az+b}{cz+d}$ with $ad-bc=1$. The other generators ($|n|\ge2$) are only *locally* defined — $z^{n+1}\partial_z$ is singular at $z=0$ or $z=\infty$ — but they are the true source of the theory's power: they act as symmetries of *local* operators even though they are not global symmetries of the sphere.

#### Pitfall

The "infinite-dimensional conformal group" is, strictly, only an infinite-dimensional *algebra* of local generators; only its $SL(2,\mathbb{C})$ subgroup integrates to honest globally invertible maps of the sphere. The looseness in calling the whole thing a "group" is standard but should be kept in mind.

## Part B · The quantum algebra and its fields

<a id="s3"></a>
### The Virasoro algebra and the central charge

#### What & why

The Witt algebra is the *classical* symmetry. In the *quantum* theory the generators become operators on a Hilbert space, and a subtle but unavoidable thing happens: the algebra acquires an extra term, a number that commutes with everything. This number is the **central charge** $c$, the single most important label of a CFT. We define a central extension, prove that the Witt algebra admits essentially one, and identify it as the **Virasoro algebra**.

#### Central extensions, defined

> **Definition — central extension.** Given a Lie algebra with generators $L_n$ and brackets $[L_m,L_n]=(m-n)L_{m+n}$, a **central extension** adjoins a new element $C$ that (i) commutes with every $L_n$ (it is **central**) and (ii) appears on the right of the bracket:
> $$
> [L_m,L_n]=(m-n)L_{m+n}+C\,p(m,n),
> $$
> where $p(m,n)$ is a number-valued function. "Central" means $[C,L_n]=0$ for all $n$, so $C$ can be replaced by its numerical value $c$ on any irreducible representation (by **Schur's lemma**, the one fact we borrow from [Lie Representations](../group-theory/lie-representations.md): an operator commuting with an irreducible action is a multiple of the identity).

Why does quantum mechanics force this? Operators are defined only up to a phase, so a *classical* symmetry that closes exactly may, when realized on quantum states, close only up to a state-independent number — a so-called **anomaly**. The central charge is precisely such an anomaly.

#### Constraining $p(m,n)$

We determine $p(m,n)$ from consistency, not from a specific model.

1. **Antisymmetry.** Since $[L_m,L_n]=-[L_n,L_m]$, the function must satisfy $p(m,n)=-p(n,m)$. *(Reason: the bracket is antisymmetric, and $(m-n)L_{m+n}$ already is; so the added term must be too.)* In particular $p(n,n)=0$.

2. **Absorb low modes.** One can redefine $L_0\to L_0+\text{const}$ and shift $L_n$ by multiples of $C$ for $n\neq0$. Using this freedom we may set $p(1,-1)$ to a convenient value and $p(n,0)=0$ for all $n$. *(Reason: a redefinition $\tilde L_n=L_n+a_n C$ changes $p$ by $(m-n)a_{m+n}$ terms, which can cancel selected components.)*

3. **Impose the Jacobi identity.** Every Lie algebra obeys the **Jacobi identity** $[L_l,[L_m,L_n]]+[L_m,[L_n,L_l]]+[L_n,[L_l,L_m]]=0$. *(Reason: this is automatic for commutators $[A,B]=AB-BA$ and must survive the extension since $C$ is central.)* Substituting the extended bracket and collecting the $C$-terms gives the recursion
$$
(m-n)\,p(m+n,l)+(n-l)\,p(n+l,m)+(l-m)\,p(l+m,n)=0.
$$

4. **Solve the recursion.** Set $l=-m-n$ so that all $C$-terms involve $p(\cdot,0)=0$ except a chain relating $p(m,-m)$ at different $m$. Working through the recursion (a finite induction on $m$) forces $p(m,-m)$ to be a **cubic polynomial in $m$ that is odd** (by antisymmetry $p(m,-m)=-p(-m,m)$). The general odd cubic is $\alpha m^3+\beta m$. Both coefficients are physical only up to the redefinitions of step 2, which can shift the linear term; the standard normalization fixes the result.

> **Result — the Virasoro algebra.** The unique nontrivial central extension of the Witt algebra is the **Virasoro algebra**:
> $$
> [L_m,L_n]=(m-n)\,L_{m+n}+\frac{c}{12}\,m\,(m^2-1)\,\delta_{m+n,0},
> $$
> with an independent antiholomorphic copy $[\bar L_m,\bar L_n]=(m-n)\bar L_{m+n}+\frac{\bar c}{12}m(m^2-1)\delta_{m+n,0}$ and $[L_m,\bar L_n]=0$. The number $c$ is the **central charge** (and $\bar c$ its antiholomorphic partner). The combination $m(m^2-1)=m^3-m$ is the odd cubic of step 4, normalized so that the central term vanishes for $m\in\{-1,0,1\}$.

#### Why the central term vanishes for $m=-1,0,1$

The factor $m(m^2-1)=(m-1)m(m+1)$ is zero at $m=-1,0,1$. Therefore the **global** subalgebra $\{L_{-1},L_0,L_{+1}\}$ is *unaffected* by the central charge — $SL(2,\mathbb{C})$ remains an exact, anomaly-free symmetry. The anomaly lives entirely in the higher modes. This is consistent with §s2: only the higher modes were "local," and only they can carry the quantum anomaly.

#### Worked check of the Jacobi consistency at small modes

Take $(m,n,l)=(2,-1,-1)$. The recursion from step 3 reads $(2-(-1))p(1,-1)+(-1-(-1))p(-2,2)+(-1-2)p(-3,-1)$. The middle term has coefficient $0$; with $p(1,-1)=\frac{c}{12}\cdot1\cdot0=0$ and $p(-3,-1)=0$ (since $-3-1\neq0$, the Kronecker delta kills it) the identity reads $0=0$, consistent. Taking $(m,n,l)=(2,-2,0)$ tests the genuine central term: $p(2,-2)=\frac{c}{12}\cdot2\cdot3=\frac{c}{2}$, and one checks the three-term sum cancels because $p(\cdot,0)=0$. These confirm the cubic is the consistent choice.

<a id="s4"></a>
### Primary and quasi-primary fields; conformal weights

#### What & why

A CFT is built from **fields** — functions $\phi(z,\bar z)$ of position whose values are operators. Conformal symmetry sorts fields by how they transform under conformal maps. The best-behaved ones, **primary fields**, transform in the simplest possible way and carry two numbers, the **conformal weights** $(h,\bar h)$, which encode their size and spin. These weights are the "quantum numbers" of the theory.

#### Conformal weights, defined through the transformation law

> **Definition — primary field.** A field $\phi(z,\bar z)$ is **primary** with weights $(h,\bar h)$ if under *every* conformal map $z\mapsto w(z)$, $\bar z\mapsto\bar w(\bar z)$ it transforms as
> $$
> \phi(z,\bar z)=\left(\frac{dw}{dz}\right)^{h}\left(\frac{d\bar w}{d\bar z}\right)^{\bar h}\,\phi'\big(w,\bar w\big),
> $$
> i.e. it picks up only the local stretching factors $dw/dz$ raised to power $h$ and $d\bar w/d\bar z$ raised to power $\bar h$. The numbers $h$ (the **holomorphic weight**) and $\bar h$ (the **antiholomorphic weight**) are real. A field obeying this law only for the *global* $SL(2,\mathbb{C})$ maps (Möbius transformations) but not necessarily for all local maps is called **quasi-primary**. Every primary is quasi-primary; the converse fails (the stress tensor of §s6 is a famous quasi-primary that is not primary).

The transformation law is the exact analogue of how a density transforms under a change of variables: a quantity $\phi\,(dz)^h(d\bar z)^{\bar h}$ is invariant, so $\phi$ is a "$(h,\bar h)$-density." This is why $h$ controls how the field scales when you rescale lengths.

#### Scaling dimension and spin

Combine the weights into two physical labels:
- **Scaling dimension** $\Delta=h+\bar h$: under a pure dilation $z\mapsto\lambda z$ the field scales as $\phi\mapsto\lambda^{-\Delta}\phi$, so $\Delta$ measures how the field shrinks or grows when you zoom. *(Derivation: with $w=\lambda z$, $dw/dz=\lambda$, so the law gives $\phi'=\lambda^{-h}\bar\lambda^{-\bar h}\phi$; for real $\lambda$ this is $\lambda^{-\Delta}$.)*
- **Spin** $s=h-\bar h$: under a pure rotation $z\mapsto e^{i\theta}z$ the field picks up $e^{-is\theta}$, so $s$ measures how it turns. *(Derivation: $dw/dz=e^{i\theta}$, $d\bar w/d\bar z=e^{-i\theta}$, giving the phase $e^{-i(h-\bar h)\theta}$.)*

#### Infinitesimal form and the action of $L_n$

Setting $w=z+\epsilon(z)$ with $\epsilon=-\sum_n a_n z^{n+1}$ and expanding the transformation law to first order gives the **variation** of a primary under the generator $\ell_n$:
$$
\delta_n\phi(z)=-\big[z^{n+1}\partial_z+h(n+1)z^{n}\big]\phi(z).
$$
**Derivation.**
1. With $w=z+\epsilon$, $dw/dz=1+\epsilon'$, so $(dw/dz)^h\approx1+h\epsilon'$. *(Reason: $(1+x)^h\approx1+hx$ for small $x$.)*
2. And $\phi'(w)=\phi'(z+\epsilon)\approx\phi(z)+\epsilon\,\phi'(z)+\delta\phi$, keeping first order. *(Reason: Taylor expansion plus the operator's own change $\delta\phi=\phi'-\phi$.)*
3. The law $\phi=(1+h\epsilon')(\phi+\epsilon\phi'+\delta\phi)$ to first order gives $0=h\epsilon'\phi+\epsilon\phi'+\delta\phi$, so $\delta\phi=-(\epsilon\partial+h\epsilon')\phi$.
4. Insert $\epsilon=-z^{n+1}$ (the basis map of §s2), so $\epsilon'=-(n+1)z^n$, giving the boxed result. $\blacksquare$

This formula is the bridge to the algebra: it shows the generators act on a primary partly by moving it ($z^{n+1}\partial_z$, a transport term) and partly by scaling it ($h(n+1)z^n$, a weight term). In §s6 the same data will reappear inside the operator product expansion.

#### Worked example

The simplest nontrivial primary is the field $\phi=\partial X$ in the **free boson** CFT, where $X(z,\bar z)$ is a massless scalar field (the position of a string). One computes $h=1,\bar h=0$, so $\Delta=1$, $s=1$: it scales like an inverse length and carries one unit of spin, exactly as a holomorphic one-form $\phi\,dz$ should. We will not need the free boson's details, but it is the standard first example, with $c=1$.

#### Pitfall

A primary is *not* the same as an eigenfield of dilations alone — that is only quasi-primary. The defining feature of a true primary is that it transforms simply under *all* the local generators, equivalently (§s9) that it is annihilated by all the *lowering* operators $L_n$ with $n>0$.

<a id="s5"></a>
### Radial quantization and the state–operator correspondence

#### What & why

To do quantum mechanics we need a Hilbert space of **states** and a notion of **time**. In a CFT on the plane the natural "time" is the *radius* $|z|$: we slice the plane into circles of growing radius and call moving outward "later." This **radial quantization** turns the plane into a cylinder of history and leads to one of the most beautiful facts in the subject — the **state–operator correspondence**, a perfect dictionary between operators and quantum states.

#### Radial quantization, constructed

1. **From cylinder to plane.** Put the theory on an infinite cylinder of circumference $2\pi$, with coordinate $w=\tau+i\sigma$ ($\tau$ = time along the cylinder, $\sigma\in[0,2\pi)$ = the angle around it). Map it to the plane by $z=e^{w}=e^{\tau}e^{i\sigma}$. *(Reason: $e^w$ is holomorphic, hence a conformal map by §s2.)* Then constant-time slices ($\tau=$ const) become **circles** $|z|=e^\tau$, and the infinite past $\tau\to-\infty$ shrinks to the single point $z=0$.

2. **Time ordering becomes radial ordering.** Earlier times sit at smaller radii. The Hamiltonian — the generator of time translation $\partial_\tau$ — becomes the generator of dilations $z\partial_z+\bar z\partial_{\bar z}$, i.e. $L_0+\bar L_0$. *(Reason: $\partial_\tau=z\partial_z+\bar z\partial_{\bar z}$ since $z=e^w$, $\partial_\tau z=z$.)* So **energy = scaling dimension**: a state of energy $E$ on the cylinder has $E=\Delta=h+\bar h$ (up to a constant shift). This is why dimensions are the spectrum of a CFT.

#### The in-state and the state–operator map

> **Definition — in-state.** For a field $\phi$ of weight $(h,\bar h)$, define the state
> $$
> |\phi\rangle:=\lim_{z,\bar z\to0}\phi(z,\bar z)\,|0\rangle,
> $$
> where $|0\rangle$ is the **vacuum** (the unique state invariant under the global group, $L_n|0\rangle=0$ for $n\ge-1$). Because $z=0$ is the infinite past, inserting an operator there *creates an incoming state* in the far past.

> **Theorem (state–operator correspondence).** The map $\phi\mapsto|\phi\rangle$ is a *bijection* between local operators and states of the Hilbert space. Conversely every state is $\lim_{z\to0}\Phi(z)|0\rangle$ for a unique local operator $\Phi$.

**Why it holds (sketch with reasons).**
1. Any state lives on some circle $|z|=r$. Using a dilation (an exact symmetry, §s3) we may shrink $r\to0$ without changing the physics. *(Reason: dilations are part of the anomaly-free $SL(2,\mathbb{C})$.)*
2. As $r\to0$ the circle collapses to a point, and the only data that can survive on a point is a local operator insertion. So states at the origin $\leftrightarrow$ local operators.
3. The vacuum corresponds to the identity operator $\mathbf 1$ ($|0\rangle=\lim_{z\to0}\mathbf 1\,|0\rangle$), and a primary $\phi$ corresponds to a **highest-weight state** (defined in §s9). $\blacksquare$

#### The mode expansion and $L_n$ as contour integrals

The generators $L_n$ act on states. Concretely, for the stress tensor $T(z)$ (§s6) one defines the **modes**
$$
L_n=\frac{1}{2\pi i}\oint dz\;z^{n+1}\,T(z),
$$
a **contour integral** around the origin. *(Reason — borrowing from [Complex Analysis](../complex-analysis/complex-analysis.md): the contour integral $\frac{1}{2\pi i}\oint z^{n+1}T(z)\,dz$ extracts the coefficient of $z^{-n-2}$ in the Laurent expansion of $T$, which is exactly the $n$-th mode.)* Acting on the vacuum these modes are organized so that $L_n|0\rangle=0$ for $n\ge-1$ — the requirement that $T(z)|0\rangle$ be regular (non-singular) at $z=0$, which forces the negative-index, "creation," modes to do all the work of building states.

#### Worked example: the energy of a primary

Apply $L_0$ to $|\phi\rangle=\lim_{z\to0}\phi(z)|0\rangle$. From the infinitesimal law of §s4 with $n=0$, $L_0\phi(0)|0\rangle=h\,\phi(0)|0\rangle$, so $L_0|\phi\rangle=h|\phi\rangle$. The state's holomorphic energy is exactly the weight $h$. With the bar sector, the cylinder energy is $h+\bar h=\Delta$, confirming "energy = dimension."

<a id="s6"></a>
### The OPE; the stress-energy tensor and the $TT$ OPE

#### What & why

When two operators sit at nearby points, their product can be re-expanded as a single sum of operators at one of the points — this is the **operator product expansion** (OPE), the algebraic heart of CFT. Among all fields one is distinguished: the **stress-energy tensor** $T(z)$, which *generates* the conformal transformations. Its self-OPE — the $TT$ OPE — encodes the entire Virasoro algebra, including the central charge.

#### The OPE, defined

> **Definition — operator product expansion.** For local operators $A(z)$ and $B(w)$, there is an expansion valid inside correlation functions, as $z\to w$,
> $$
> A(z)\,B(w)=\sum_{k}\frac{C_k(w)}{(z-w)^{n_k}},
> $$
> where the $C_k(w)$ are local operators and the powers $n_k$ are fixed by the weights. The terms with $n_k>0$ are the **singular part** (they blow up as $z\to w$); the regular part is the rest. The singular part carries all the algebraic content — it is what commutators are made of.

#### The stress tensor

The **stress-energy tensor** $T_{\mu\nu}$ is the conserved current associated with translations; conformal invariance makes it **traceless** ($T^\mu{}_\mu=0$) and conservation then makes its components holomorphic/antiholomorphic. In complex coordinates the independent pieces are a holomorphic field $T(z)\equiv T_{zz}$ and an antiholomorphic $\bar T(\bar z)\equiv T_{\bar z\bar z}$. $T(z)$ is the generator of conformal transformations: the variation of any field under a map $\epsilon$ is the contour integral $\delta_\epsilon\phi(w)=\frac{1}{2\pi i}\oint dz\,\epsilon(z)T(z)\phi(w)$, which is exactly why the modes $L_n=\frac{1}{2\pi i}\oint z^{n+1}T\,dz$ of §s5 generate the algebra.

#### The $T\phi$ OPE encodes "primary"

The statement "$\phi$ is primary of weight $h$" is *equivalent* to the OPE
$$
T(z)\,\phi(w,\bar w)=\frac{h}{(z-w)^2}\,\phi(w,\bar w)+\frac{1}{z-w}\,\partial_w\phi(w,\bar w)+\text{regular}.
$$
**Derivation.** The double-pole coefficient $h\phi$ is the *weight* term and the single-pole coefficient $\partial\phi$ is the *transport* term of the infinitesimal law $\delta_n\phi=-(z^{n+1}\partial+h(n+1)z^n)\phi$ from §s4. Concretely:
1. Compute $\delta_\epsilon\phi(w)=\frac{1}{2\pi i}\oint_w dz\,\epsilon(z)\,T(z)\phi(w)$ using the OPE above.
2. The double pole, by the residue rule $\frac{1}{2\pi i}\oint\frac{\epsilon(z)}{(z-w)^2}dz=\epsilon'(w)$, contributes $h\,\epsilon'(w)\phi$. *(Reason — Cauchy's integral formula for derivatives, from [Complex Analysis](../complex-analysis/complex-analysis.md): $\frac{1}{2\pi i}\oint\frac{f(z)}{(z-w)^2}dz=f'(w)$.)*
3. The single pole contributes $\epsilon(w)\partial\phi$ by the residue rule $\frac{1}{2\pi i}\oint\frac{\epsilon(z)}{z-w}dz=\epsilon(w)$.
4. Sum: $\delta_\epsilon\phi=h\epsilon'\phi+\epsilon\partial\phi$, matching §s4. So the OPE *is* the transformation law. $\blacksquare$

#### The $TT$ OPE and the central charge

> **The $TT$ OPE.** The stress tensor's product with itself is
> $$
> T(z)\,T(w)=\frac{c/2}{(z-w)^{4}}+\frac{2\,T(w)}{(z-w)^{2}}+\frac{\partial_w T(w)}{z-w}+\text{regular}.
> $$

The structure mirrors the $T\phi$ OPE with two differences: $T$ has weight $h=2$ (hence the coefficient $2$ on the double pole), and there is an *extra* leading term $\frac{c/2}{(z-w)^4}$, a fourth-order pole with no operator — only the number $c$. That extra term is precisely the central charge: it is the OPE-language version of the anomaly of §s3. The presence of the $(z-w)^{-4}$ term also shows $T$ is **not primary** (a primary would have no pole higher than the double pole), only quasi-primary.

#### From the $TT$ OPE back to the Virasoro algebra

We close the loop: the $TT$ OPE *implies* the Virasoro algebra of §s3.
1. The commutator of modes is a double contour integral, $[L_m,L_n]=\big(\oint_0\frac{dw}{2\pi i}-\big)\oint_w\frac{dz}{2\pi i}\,z^{m+1}w^{n+1}T(z)T(w)$, where the $z$-contour encircles $w$. *(Reason: the commutator of contour-integral charges equals the contour integral of the OPE's singular part — the standard "radial ordering" manipulation of deforming contours.)*
2. Insert the $TT$ OPE and read off residues of each pole. The $(z-w)^{-2}$ term with $2T$ gives, after the residue rule, the $(m-n)L_{m+n}$ piece; the $(z-w)^{-1}$ term combines into the same; and the $(z-w)^{-4}$ term with $c/2$ gives, by the third-derivative residue $\frac{1}{3!}\partial_w^3$, the central term.
3. Evaluating $\frac{1}{2\pi i}\oint w^{n+1}\,\frac{c}{2}\cdot\frac{1}{3!}\partial_w^3 z^{m+1}\big|_{z=w}\,dw$ yields $\frac{c}{12}(m^3-m)\delta_{m+n,0}$. *(Reason: $\partial_w^3 w^{m+1}=(m+1)m(m-1)w^{m-2}$, and $\frac{1}{2\pi i}\oint w^{m+n-1}dw=\delta_{m+n,0}$; the factor $\frac{1}{2}\cdot\frac{1}{6}\cdot(m+1)m(m-1)=\frac{c}{12}m(m^2-1)/c\cdots$ assembles to $\frac{c}{12}(m^3-m)$.)*

The Virasoro algebra and the $TT$ OPE are thus two encodings of the same content.

## Part C · Constraints, correlators, and Ward identities

<a id="s7"></a>
### Correlation functions fixed by conformal symmetry

#### What & why

A **correlation function** (or **correlator**) $\langle\phi_1(z_1)\cdots\phi_n(z_n)\rangle$ is the quantum average of a product of fields — the basic observable of the theory. The power of conformal symmetry is that it *fixes the functional form* of the two- and three-point correlators completely, leaving only a few constants. We derive these now using only the global $SL(2,\mathbb{C})$ invariance.

#### Setup: invariance under the global group

A correlator of quasi-primaries is invariant under global conformal maps: under $z\mapsto w(z)$,
$$
\langle\phi_1(z_1)\cdots\rangle=\prod_i\left(\frac{dw}{dz}\Big|_{z_i}\right)^{h_i}\big\langle\phi_1(w_1)\cdots\big\rangle,
$$
the product of each field's transformation factor (for brevity we suppress the bar sector; it tags along identically). We impose invariance under the three global generators: translations, dilations+rotations, and SCTs.

#### The two-point function

> **Result.** For two quasi-primaries of weights $(h_1,\bar h_1),(h_2,\bar h_2)$,
> $$
> \langle\phi_1(z_1,\bar z_1)\,\phi_2(z_2,\bar z_2)\rangle=
> \begin{cases}
> \dfrac{C_{12}}{(z_{12})^{2h}\,(\bar z_{12})^{2\bar h}}, & h_1=h_2=h,\ \bar h_1=\bar h_2=\bar h,\\[2mm]
> 0,& \text{otherwise,}
> \end{cases}
> $$
> where $z_{12}=z_1-z_2$ and $C_{12}$ is a constant (set to $1$ by normalizing fields).

**Derivation.**
1. **Translation invariance** $\Rightarrow$ the correlator depends only on the difference $z_{12}$. *(Reason: invariance under $z\to z+a$ forbids dependence on the absolute positions.)* Write it as $f(z_{12})$.
2. **Rotation + dilation (scaling)** $\Rightarrow$ under $z\to\lambda z$ the correlator scales by $\lambda^{-h_1-h_2}$, so $f(\lambda z_{12})=\lambda^{-(h_1+h_2)}f(z_{12})$, forcing $f(z_{12})=C_{12}\,z_{12}^{-(h_1+h_2)}$. *(Reason: a function with that homogeneity is a pure power.)*
3. **SCT invariance** $\Rightarrow$ under $z\mapsto z/(1-bz)$ the factors $dw/dz=(1-bz)^{-2}$ at the two points must combine so the answer is unchanged. Working through, this is consistent *only if* $h_1=h_2$. *(Reason: the SCT factor $(1-bz_1)(1-bz_2)$ cross-terms cancel exactly when the exponents are equal; unequal exponents leave an uncancelled $b$-dependence, which is forbidden by invariance.)* Hence two primaries of unequal weight have vanishing two-point function. $\blacksquare$

#### The three-point function

> **Result.** For three quasi-primaries (holomorphic part shown),
> $$
> \langle\phi_1\phi_2\phi_3\rangle=\frac{C_{123}}{z_{12}^{\,h_1+h_2-h_3}\,z_{23}^{\,h_2+h_3-h_1}\,z_{13}^{\,h_1+h_3-h_2}},
> $$
> with $z_{ij}=z_i-z_j$ and a single constant $C_{123}$, the **structure constant** (or **OPE coefficient**).

**Derivation.**
1. Translation invariance $\Rightarrow$ depend only on $z_{12},z_{13},z_{23}$.
2. Make the ansatz $\prod_{i<j}z_{ij}^{a_{ij}}$ and impose scaling: under $z\to\lambda z$ each $z_{ij}\to\lambda z_{ij}$, so $\sum_{i<j}a_{ij}=-(h_1+h_2+h_3)$.
3. Impose SCT invariance; this yields three more linear equations. Solving the linear system gives $a_{12}=-(h_1+h_2-h_3)$, $a_{13}=-(h_1+h_3-h_2)$, $a_{23}=-(h_2+h_3-h_1)$. *(Reason: the unique solution of the four linear constraints — one from scaling, three from SCTs — is this symmetric assignment.)* $\blacksquare$

> **Why this is the bootstrap.** The two-point function fixes the *normalization*; the three-point function fixes everything except the numbers $C_{123}$. The full set of weights $\{h_i\}$ and structure constants $\{C_{123}\}$ is called the **CFT data**; the **conformal bootstrap** program is the statement that consistency (associativity of the OPE, modular invariance) determines this data. Four-point and higher correlators are *not* fixed by symmetry alone — they depend on **cross-ratios** like $x=\frac{z_{12}z_{34}}{z_{13}z_{24}}$, the invariant combinations that survive all global maps — and require the dynamics.

#### Worked example: the Ising spin two-point function

In the $c=\tfrac12$ Ising CFT (§s10) the spin field $\sigma$ has $h=\bar h=\tfrac1{16}$, so $\Delta=\tfrac18$. The two-point function is therefore $\langle\sigma(z,\bar z)\sigma(0)\rangle=|z|^{-1/4}$, i.e. $\langle\sigma\sigma\rangle\sim r^{-1/4}$ at separation $r$. This power law — the **critical exponent** $\eta=\tfrac14$ — is a measured prediction for the 2D Ising magnet at its critical temperature, fixed entirely by the value $h=\tfrac1{16}$.

<a id="s8"></a>
### Conformal Ward identities

#### What & why

A **Ward identity** is the precise statement, *inside correlation functions*, of a symmetry: it says how inserting the symmetry's current ($T(z)$) into a correlator reproduces the transformation of the other fields. The conformal Ward identities turn the abstract symmetry into a computational tool, and they are the engine behind both the correlator forms of §s7 and the recursion relations of §s9.

#### The identity

> **Conformal Ward identity.** For primaries $\phi_i$ of weights $h_i$,
> $$
> \big\langle T(z)\,\phi_1(w_1)\cdots\phi_n(w_n)\big\rangle
> =\sum_{i=1}^{n}\left[\frac{h_i}{(z-w_i)^2}+\frac{1}{z-w_i}\,\partial_{w_i}\right]\big\langle\phi_1(w_1)\cdots\phi_n(w_n)\big\rangle.
> $$

**Derivation.**
1. The variation of the correlator under an infinitesimal conformal map $\epsilon(z)$ is, by the definition of $T$ as the generator (§s6), $\delta\langle\prod\phi_i\rangle=-\frac{1}{2\pi i}\oint dz\,\epsilon(z)\langle T(z)\prod\phi_i\rangle$, the contour enclosing all the $w_i$.
2. On the other hand, the variation equals the sum of the individual field variations, $\delta\langle\prod\phi_i\rangle=\sum_i\langle\phi_1\cdots\delta_\epsilon\phi_i\cdots\phi_n\rangle$, with $\delta_\epsilon\phi_i=-(\epsilon\partial+h_i\epsilon')\phi_i$ from §s4.
3. Equate the two for *all* $\epsilon$. Since $\epsilon$ is arbitrary, the integrands must match: the correlator $\langle T(z)\prod\phi_i\rangle$ must have exactly the poles whose residues reproduce step 2 — a double pole $h_i/(z-w_i)^2$ and a single pole $\partial_{w_i}/(z-w_i)$ at each $w_i$. *(Reason: by the residue rules of §s6, those poles integrate against $\epsilon$ to give $\epsilon'h_i$ and $\epsilon\partial$, matching the field variations.)*
4. There can be no other singularities (no other operators sit between the $\phi_i$) and the correlator vanishes as $z\to\infty$ (because $T$ has weight $2$, $\langle T(z)\cdots\rangle\sim z^{-4}$), so the poles listed are the *entire* answer. $\blacksquare$

#### Consequence: the global Ward identities

Multiply the Ward identity by $z^{n+1}$ for $n=-1,0,1$ and integrate; the requirement that $\langle T(z)\cdots\rangle$ has no poles at infinity for these $n$ gives three constraints:
$$
\sum_i\partial_{w_i}\langle\cdots\rangle=0,\qquad
\sum_i(w_i\partial_{w_i}+h_i)\langle\cdots\rangle=0,\qquad
\sum_i(w_i^2\partial_{w_i}+2h_iw_i)\langle\cdots\rangle=0.
$$
These are exactly translation, scaling, and SCT invariance — *the same three conditions* we imposed by hand in §s7. The Ward identity thus *derives* the constraints of §s7 systematically and, crucially, extends them to correlators that *also* contain $T$ itself, which is what §s9 needs.

#### Worked check on the two-point function

Apply the scaling identity $\sum_i(w_i\partial_{w_i}+h_i)$ to $\langle\phi(w_1)\phi(w_2)\rangle=C\,w_{12}^{-2h}$. Compute $w_1\partial_{w_1}(w_{12}^{-2h})+w_2\partial_{w_2}(w_{12}^{-2h})=-2h\,w_{12}^{-2h-1}(w_1-w_2)=-2h\,w_{12}^{-2h}$, and adding $2h\,w_{12}^{-2h}$ (the $h_1+h_2=2h$ term) gives $0$. The identity holds, confirming the form found in §s7.

## Part D · Representations, minimal models, and the torus

<a id="s9"></a>
### Representation theory of Virasoro: Verma modules, descendants, null states

#### What & why

The Hilbert space of a CFT is built from **representations** of the Virasoro algebra. Each primary field gives a **highest-weight state** from which an entire tower of states is generated by the raising operators — a **Verma module**. Sometimes this tower contains a **null state** (a state of zero norm), and removing it gives an **irreducible** representation. The bookkeeping of null states (via the **Kac determinant**) is what produces the discrete list of allowed CFTs in §s10.

#### Highest-weight states and descendants

> **Definition.** A **highest-weight state** $|h\rangle$ of weight $h$ satisfies
> $$
> L_0|h\rangle=h|h\rangle,\qquad L_n|h\rangle=0\ \ \text{for all }n>0.
> $$
> The first equation says $|h\rangle$ has definite energy $h$ (§s5); the second says it is annihilated by all **lowering operators** $L_{n>0}$ (which decrease $L_0$-energy by $n$, since $[L_0,L_n]=-nL_n$). By the state–operator map (§s5), $|h\rangle=|\phi\rangle$ for a primary $\phi$ of weight $h$.

Acting with **raising operators** $L_{-n}$ ($n>0$, which *raise* energy by $n$) builds **descendant states**:
$$
L_{-n_1}L_{-n_2}\cdots L_{-n_k}\,|h\rangle,\qquad n_1\ge n_2\ge\cdots\ge1.
$$
> **Definition — Verma module.** The **Verma module** $V(c,h)$ is the span of $|h\rangle$ and all its descendants. Its states at energy $h+N$ (those built from $L_{-n}$'s with $\sum n_i=N$) form **level $N$**; the count of independent such states is $p(N)$, the **number of partitions** of $N$. The integer $N$ is the **level**.

**Why $[L_0,L_{-n}]=nL_{-n}$ (so descendants raise energy).** From Virasoro, $[L_0,L_{-n}]=(0-(-n))L_{-n}=nL_{-n}$. Hence $L_0(L_{-n}|h\rangle)=(L_{-n}L_0+nL_{-n})|h\rangle=(h+n)L_{-n}|h\rangle$. So $L_{-n}|h\rangle$ has energy $h+n$. *(Reason: direct use of the bracket.)*

#### Worked level count

- Level $0$: just $|h\rangle$. $p(0)=1$ state.
- Level $1$: $L_{-1}|h\rangle$. $p(1)=1$ state.
- Level $2$: $L_{-2}|h\rangle$ and $L_{-1}^2|h\rangle=L_{-1}L_{-1}|h\rangle$. $p(2)=2$ states.
- Level $3$: $L_{-3},\,L_{-1}L_{-2},\,L_{-1}^3$. $p(3)=3$ states.

The generating function for these counts is $\prod_{n\ge1}(1-q^n)^{-1}=\sum_N p(N)q^N$, which will reappear as the **character** in §s11.

#### Null states

> **Definition — null (singular) state.** A descendant $|\chi\rangle$ at some level $N>0$ is **null** (or **singular**) if it is *itself* a highest-weight state: $L_n|\chi\rangle=0$ for all $n>0$, yet $|\chi\rangle\neq0$. A null state has zero inner product with the whole module (including itself), so it is physically invisible and must be **quotiented out** (set to zero) to get the genuine, irreducible representation.

**Worked example (level 2 null state).** Seek $|\chi\rangle=(L_{-2}+aL_{-1}^2)|h\rangle$ that is annihilated by $L_1$ and $L_2$.
1. Impose $L_1|\chi\rangle=0$. Using $[L_1,L_{-2}]=3L_{-1}$ and $[L_1,L_{-1}]=2L_0$, one finds $L_1|\chi\rangle=(3+a\cdot(2(2h+1)))\,L_{-1}|h\rangle$... carefully: $L_1L_{-1}^2|h\rangle=(4h+2)L_{-1}|h\rangle$, so $L_1|\chi\rangle=(3+a(4h+2))L_{-1}|h\rangle$. Setting to zero: $a=-\frac{3}{2(2h+1)}$.
2. Impose $L_2|\chi\rangle=0$. Using $[L_2,L_{-2}]=4L_0+\tfrac{c}{2}$ and $L_2L_{-1}^2|h\rangle=6h|h\rangle$, one gets $L_2|\chi\rangle=(4h+\tfrac{c}{2}+6ah)|h\rangle$. Setting to zero and inserting $a$ from step 1 gives the condition
$$
2(2h+1)\left(4h+\tfrac{c}{2}\right)=18h\quad\Longrightarrow\quad
h=\frac{1}{16}\Big(5-c\pm\sqrt{(c-1)(c-25)}\Big).
$$
*(Reason: substitute $a=-\tfrac{3}{2(2h+1)}$ and solve the resulting quadratic in $h$.)* For special $(c,h)$ this is satisfied and the module has a level-2 null state. The Ising spin $h=\tfrac1{16}$ at $c=\tfrac12$ is exactly such a case — its null state gives a differential equation for $\langle\sigma\sigma\sigma\sigma\rangle$.

#### The Kac determinant and unitarity

> **The Kac determinant.** At level $N$, form the **Gram matrix** $M_N$ of inner products of the $p(N)$ basis descendants. Its determinant — the **Kac determinant** — factorizes as
> $$
> \det M_N=\alpha_N\prod_{\substack{r,s\ge1\\ rs\le N}}\big(h-h_{r,s}(c)\big)^{p(N-rs)},
> \qquad
> h_{r,s}(c)=\frac{(r\beta-s/\beta)^2-(\beta-1/\beta)^2}{4},
> $$
> where $\alpha_N>0$ is a known constant and $\beta$ is fixed by $c=1-6(\beta-1/\beta)^2$. A null state appears at level $N$ exactly when $h=h_{r,s}$ for some $rs=N$ (the corresponding factor vanishes).

> **Unitarity bound.** A representation is **unitary** (all states have non-negative norm — required for a sensible quantum theory) only if $\det M_N\ge0$ for all $N$. Analyzing the signs gives the **Friedan–Qiu–Shenker theorem**: for $c\ge1$, unitary reps exist for all $h\ge0$; but for $0\le c<1$, unitarity forces $c$ and $h$ onto a *discrete* list,
> $$
> c=1-\frac{6}{m(m+1)},\quad m=3,4,5,\dots,\qquad
> h_{r,s}=\frac{\big((m+1)r-ms\big)^2-1}{4m(m+1)},
> $$
> with $1\le r\le m-1$, $1\le s\le r$. These discrete theories are the **minimal models** of §s10.

The logic is the punchline of the whole representation theory: *demanding a unitary, infinite-dimensional Virasoro representation with $c<1$ is so restrictive that only a countable list of theories survives.* Symmetry has been taken to infinity, and infinity has answered with a finite menu.

<a id="s10"></a>
### Minimal models and the $c<1$ classification

#### What & why

A **minimal model** is a CFT whose entire field content consists of *finitely many* primaries, each carrying a null state. The null states close the OPE onto a finite set, so the theory is completely solvable. The minimal models realize the discrete $c<1$ list of §s9 and include the most famous critical point in physics, the **2D Ising model**.

#### Definition and the Kac table

> **Definition — minimal model $\mathcal M(p,p')$.** For two coprime integers $p>p'\ge2$, the minimal model has central charge
> $$
> c=1-\frac{6(p-p')^2}{p\,p'},
> $$
> and a *finite* set of primaries with weights given by the **Kac table**
> $$
> h_{r,s}=\frac{(pr-p's)^2-(p-p')^2}{4pp'},\qquad 1\le r\le p'-1,\ \ 1\le s\le p-1,
> $$
> with the identification $h_{r,s}=h_{p'-r,\,p-s}$ (so each weight is counted once). The number of distinct primaries is $\tfrac12(p-1)(p'-1)$.

The **unitary** minimal models are the subfamily $p'=m$, $p=m+1$ of §s9, with $c=1-\frac{6}{m(m+1)}$.

#### Why finitely many fields: the fusion closes

Because every primary in a minimal model has a null descendant, its OPEs with other primaries are restricted: only a finite set of primaries can appear on the right-hand side. This bookkeeping — which primaries can fuse to which — is the **fusion algebra**, and its closure on a finite set is what makes the model "minimal." *(Reason: a null state, set to zero, becomes a differential equation that the correlators must satisfy; the equation admits solutions only for specific weights on the right of the OPE, truncating the sum.)*

#### The Ising model as $c=\tfrac12$

> **The Ising CFT $=\mathcal M(4,3)$.** Take $p=4,p'=3$:
> $$
> c=1-\frac{6(4-3)^2}{4\cdot3}=1-\frac{6}{12}=\frac12.
> $$
> Its Kac table (with $1\le r\le2$, $1\le s\le3$, identified) yields exactly **three** primaries:
> $$
> h_{1,1}=0\ (\text{identity }\mathbf 1),\qquad
> h_{2,1}=\tfrac12\ (\text{energy }\varepsilon),\qquad
> h_{1,2}=\tfrac1{16}\ (\text{spin }\sigma).
> $$

**Check of $h_{1,2}$.** With $p=4,p'=3,r=1,s=2$: $h_{1,2}=\frac{(4\cdot1-3\cdot2)^2-(4-3)^2}{4\cdot4\cdot3}=\frac{(4-6)^2-1}{48}=\frac{4-1}{48}=\frac{3}{48}=\frac1{16}$. This is the spin weight used in §s7's worked example. With $\bar h=\tfrac1{16}$ too, $\Delta_\sigma=\tfrac18$ gives the critical exponent $\eta=\tfrac14$ — a number measured in real two-dimensional magnets and reproduced by no input other than "the theory is the unitary $c=\tfrac12$ CFT." The energy field $\varepsilon$ has $\Delta=1$ and governs how the system responds to temperature; its weight $h_{2,1}=\tfrac12$ controls the specific-heat exponent.

#### The fusion rules of Ising (worked)

The three Ising primaries fuse as
$$
\sigma\times\sigma=\mathbf 1+\varepsilon,\qquad
\sigma\times\varepsilon=\sigma,\qquad
\varepsilon\times\varepsilon=\mathbf 1.
$$
Read: two spins can combine into the identity or the energy field but nothing else; this finite, closed table is the algebraic fingerprint of the Ising universality class, and it is forced by the null states of §s9.

#### Pitfall

Not every $c<1$ value gives a *unitary* model — only the discrete $m$-series does. Non-unitary minimal models (e.g. the Yang–Lee edge singularity, $\mathcal M(5,2)$, with $c=-\tfrac{22}{5}$) are perfectly good CFTs and describe real physics (here, the partition-function zeros of the Ising model in an imaginary field), but they have negative-norm states and so are not statistical-mechanics critical points in the usual sense.

<a id="s11"></a>
### Modular invariance and the torus partition function (overview)

#### What & why

Putting a CFT on a **torus** (a doughnut surface) introduces a powerful new consistency condition: the torus can be described by different but equivalent shape parameters, and the theory must give the *same* answer for all of them. This is **modular invariance**, and it is the final filter that selects which collections of Virasoro representations assemble into a genuine CFT. It also completes the bootstrap: together with crossing symmetry of four-point functions, modular invariance fixes the spectrum.

#### The torus and its modular parameter

Build a torus by taking the complex plane and identifying points that differ by either of two lattice vectors, $1$ and $\tau$ (a complex number with $\mathrm{Im}\,\tau>0$). The shape of the torus is captured entirely by this single **modular parameter** $\tau$. Two parameters $\tau$ and $\tau'$ describe the *same* torus whenever they are related by a **modular transformation**
$$
\tau\mapsto\frac{a\tau+b}{c\tau+d},\qquad
\begin{pmatrix}a&b\\c&d\end{pmatrix}\in SL(2,\mathbb{Z}),
$$
i.e. integers with $ad-bc=1$. This group is generated by just two moves: $T:\tau\mapsto\tau+1$ (a shear) and $S:\tau\mapsto-1/\tau$ (which swaps the two cycles of the torus).

#### The partition function and characters

> **Definition — torus partition function.** The **partition function** is the trace over the Hilbert space
> $$
> Z(\tau,\bar\tau)=\operatorname{Tr}\Big(q^{L_0-c/24}\,\bar q^{\bar L_0-\bar c/24}\Big),
> \qquad q=e^{2\pi i\tau}.
> $$
> The operator $q^{L_0-c/24}$ weights each state by its energy (recall $L_0$ = energy, §s5); the shift $-c/24$ is the universal **Casimir energy** of the cylinder, and its appearance is another face of the central charge.

Grouping states by which Virasoro representation they belong to, the trace factorizes into **characters**:
$$
Z=\sum_{h,\bar h}N_{h,\bar h}\;\chi_h(\tau)\,\overline{\chi_{\bar h}(\tau)},
\qquad
\chi_h(\tau)=\operatorname{Tr}_{V(c,h)}q^{L_0-c/24}=\frac{q^{\,h-c/24}}{\prod_{n\ge1}(1-q^n)}\ (\text{for a generic Verma module}),
$$
where $N_{h,\bar h}$ are non-negative integers counting how many times each representation appears. The denominator $\prod(1-q^n)^{-1}=\sum p(N)q^N$ is exactly the partition-counting generating function of §s9 — the characters *are* the level-by-level state counts, dressed with energy.

#### The modular invariance condition

> **Modular invariance.** $Z$ must be invariant under the generators $S$ and $T$:
> $$
> Z(\tau+1,\bar\tau+1)=Z(\tau,\bar\tau),\qquad
> Z(-1/\tau,-1/\bar\tau)=Z(\tau,\bar\tau).
> $$
> Under these the characters transform *among themselves* by fixed matrices, $\chi_h(-1/\tau)=\sum_{h'}S_{hh'}\chi_{h'}(\tau)$ and $\chi_h(\tau+1)=\sum_{h'}T_{hh'}\chi_{h'}(\tau)$ (with $T$ diagonal). So modular invariance becomes the *finite linear-algebra* condition that the matrix $N_{h,\bar h}$ commute with $S$ and $T$.

For a minimal model the number of characters is finite, so this is a finite, solvable matrix equation. Its solutions are the **modular invariants**; the simplest, $N_{h,\bar h}=\delta_{h\bar h}$ (the **diagonal** or **A-series**), always works, and others give the celebrated **ADE classification** of minimal-model partition functions.

#### Worked sketch: the Ising partition function

The $c=\tfrac12$ Ising model has three characters $\chi_{0},\chi_{1/2},\chi_{1/16}$. The diagonal modular invariant
$$
Z_{\text{Ising}}=|\chi_0|^2+|\chi_{1/2}|^2+|\chi_{1/16}|^2
$$
is invariant under $S$ and $T$ (one checks the $3\times3$ modular matrices $S,T$ acting on $(\chi_0,\chi_{1/2},\chi_{1/16})$ leave the sum of squared moduli fixed). This single expression encodes the full operator content of the 2D Ising critical point — identity, energy, and spin — and its invariance is the statement that the theory is consistent on every torus. That a doughnut's many descriptions must agree is the last, global incarnation of the conformal symmetry we followed from the plane all the way to infinity.

#### Pitfall and outlook

Modular invariance is a *necessary* condition for a consistent CFT, not by itself sufficient — one must also satisfy crossing (associativity of the OPE) on the sphere. The two conditions together constitute the **conformal bootstrap**, the modern program that, in two dimensions, fully solves the minimal models and, in higher dimensions, numerically corners theories like the 3D Ising model. The torus is where the local symmetry of §s2 finally meets the global topology of spacetime.

---

*This guide built two-dimensional conformal field theory from the ground up: the conformal group in $d$ dimensions and the singular role of $d=2$, where conformal maps become holomorphic functions and the finite symmetry blossoms into the infinite-dimensional Witt algebra. Quantizing turned Witt into the Virasoro algebra, whose unique central extension introduced the central charge $c$ — derived from the Jacobi identity and re-derived from the $TT$ OPE. Primary fields, labeled by conformal weights $(h,\bar h)$, were placed in one-to-one correspondence with quantum states by radial quantization, and the operator product expansion organized their short-distance products. Conformal symmetry then fixed the two- and three-point functions completely, the Ward identities systematized those constraints, and the representation theory of Virasoro — Verma modules, descendants, null states, and the Kac determinant — produced the unitarity bounds that collapse the $c<1$ world to a discrete list of minimal models, the Ising model sitting at $c=\tfrac12$ with its spin weight $\tfrac1{16}$. Finally, modular invariance on the torus tied the spectrum together globally. The single thread: in two dimensions, demanding invariance under infinitely many conformal transformations constrains a quantum theory so completely that whole families of them can be written down and solved exactly — symmetry, taken to infinity, becomes a method of exact solution.*
