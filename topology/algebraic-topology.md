# Topology, *turned into algebra.*

A full first course in algebraic topology — how to attach groups, rings, and exact sequences to spaces so that continuous maps become homomorphisms and "shape" becomes computable. Every core theorem is **demonstrated**, and the functorial thread that ties them all together is made explicit.

[← Back to all guides](../README.md)

## Part A · Homotopy & the fundamental group

<a id="s0"></a>
### The big picture: turning spaces into algebra

Topology studies properties of spaces preserved by continuous deformation — properties invariant under *homeomorphism*. But proving two spaces are *not* homeomorphic is hard directly: you would have to rule out every possible map. Algebraic topology offers a way out.

- **Attach** an algebraic object (a group, a ring, a sequence of groups) to every space.
- **Functoriality** — every continuous map induces a homomorphism, respecting composition and identities.
- **Invariance** — homeomorphic (indeed homotopy-equivalent) spaces get isomorphic algebra, so different algebra proves different spaces.

> **Principle — the central strategy**
>
> An **invariant** is a functor $F$ from spaces & continuous maps to groups & homomorphisms. Because $F(f\circ g)=F(f)\circ F(g)$ and $F(\mathrm{id})=\mathrm{id}$, a homeomorphism $X\cong Y$ forces an isomorphism $F(X)\cong F(Y)$. Contrapositive: if $F(X)\not\cong F(Y)$, then $X$ and $Y$ are *not* homeomorphic. We trade a hard topological question for a tractable algebraic one.

> **Connection — why "functor" is the load-bearing word**
>
> Every chapter is one functor: $\pi_1$ (a group), $\pi_n$ (abelian groups), $H_n$ (homology, abelian groups), $H^n$ (cohomology, a graded ring). The proofs differ; the logic — induced maps, invariance, computation — never does.

#### The whole course on one line

> Homotopy → $\pi_1$ → $\pi_1(S^1)\cong\mathbb{Z}$ → van Kampen → covering spaces → homology → cohomology & duality

<a id="s1"></a>
### Homotopy of maps & homotopy equivalence

*The slackening of "equal" to "continuously deformable" is the move that makes everything compute. Most invariants see only homotopy type, not homeomorphism type.*

> **Definition — homotopy**
>
> Two continuous maps $f,g:X\to Y$ are **homotopic**, written $f\simeq g$, if there is a continuous $H:X\times[0,1]\to Y$ with $H(x,0)=f(x)$ and $H(x,1)=g(x)$. Think of $H$ as a movie: at each time $t$, $H(-,t)$ is a map, sliding continuously from $f$ to $g$. For paths we usually demand **endpoints fixed** (homotopy rel $\{0,1\}$).

**Demonstration — homotopy is an equivalence relation**

1. Reflexive: $f\simeq f$ via the constant homotopy $H(x,t)=f(x)$, which is continuous as a composite of continuous maps.
2. Symmetric: if $H$ is a homotopy $f\simeq g$, then $\overline H(x,t)=H(x,1-t)$ is continuous (composition with $t\mapsto 1-t$) and runs $g\simeq f$.
3. Transitive: given $H:f\simeq g$ and $K:g\simeq h$, splice them: At $t=\tfrac12$ both pieces equal $g(x)$, so by the pasting lemma (continuous on two closed sets that agree on the overlap) $L$ is continuous.

   $$L(x,t)=\begin{cases} H(x,2t), & 0\le t\le \tfrac12,\$$2pt] K(x,2t-1), & \tfrac12\le t\le 1.\end{cases}$$

*Equivalence classes $[f]$ are well defined; this is the raw material of every homotopy invariant.*

> **Definition — homotopy equivalence & contractibility**
>
> A map $f:X\to Y$ is a **homotopy equivalence** if there is $g:Y\to X$ with $g\circ f\simeq \mathrm{id}_X$ and $f\circ g\simeq \mathrm{id}_Y$; then $X\simeq Y$ are **homotopy equivalent**. A space homotopy equivalent to a point is **contractible**. A **deformation retraction** of $X$ onto a subspace $A$ is a homotopy from $\mathrm{id}_X$ to a retraction $r:X\to A$ fixing $A$; it exhibits $A\hookrightarrow X$ as a homotopy equivalence.

**Examples to keep in mind**

*$\mathbb{R}^n$ is contractible (slide everything to the origin: $H(x,t)=(1-t)x$). The punctured plane $\mathbb{R}^2\setminus\{0\}$ deformation-retracts onto $S^1$ via $H(x,t)=(1-t)x+t\,x/|x|$. An annulus, a Möbius band, and $S^1$ are all homotopy equivalent though pairwise non-homeomorphic — homotopy is genuinely coarser.*

> **Connection — to general topology**
>
> Homeomorphism $\Rightarrow$ homotopy equivalence, never the reverse. Algebraic-topology invariants are designed to be *homotopy* invariants, so they are automatically topological invariants — but they cannot, by construction, distinguish a disk from a point.

<a id="s2"></a>
### The fundamental group $\pi_1$

*The first and most intuitive functor: loops at a basepoint, up to homotopy, with concatenation as the operation. It detects one-dimensional holes.*

> **Definition — loops, concatenation, the group**
>
> Fix $x_0\in X$. A **loop** at $x_0$ is a path $\gamma:[0,1]\to X$ with $\gamma(0)=\gamma(1)=x_0$. The **fundamental group** $\pi_1(X,x_0)$ is the set of homotopy classes (rel endpoints) of loops, with product $[\,\alpha\,][\,\beta\,]=[\alpha\cdot\beta]$ where $$ (\alpha\cdot\beta)(s)=\begin{cases}\alpha(2s),&0\le s\le\tfrac12,\\ \beta(2s-1),&\tfrac12\le s\le1.\end{cases} $$

**Demonstration — $\pi_1(X,x_0)$ is a group**

1. Well defined: if $\alpha\simeq\alpha'$ and $\beta\simeq\beta'$ rel endpoints, the side-by-side homotopy $H\cdot K$ shows $\alpha\cdot\beta\simeq\alpha'\cdot\beta'$. So the product on classes is unambiguous.
2. Associativity: $(\alpha\cdot\beta)\cdot\gamma$ and $\alpha\cdot(\beta\cdot\gamma)$ differ only in the speeds at which the three loops are traversed. A reparametrization $\varphi:[0,1]\to[0,1]$ (a homotopy of the time-axis) carries one to the other, so the classes are equal.
3. Identity: the constant loop $c_{x_0}$ satisfies $[c]\,[\alpha]=[\alpha]=[\alpha]\,[c]$: the loop "wait then go" is reparametrized to "go," again by a homotopy of $[0,1]$.
4. Inverses: let $\bar\alpha(s)=\alpha(1-s)$. The homotopy $H(s,t)=\alpha\big(\text{shrink}\big)$ that pulls the round trip $\alpha\cdot\bar\alpha$ back to $x_0$ shows $[\alpha][\bar\alpha]=[c]$.

*All four axioms hold up to endpoint-fixing homotopy — which is exactly why we quotient by it.*

**Demonstration — basepoint independence on a path-connected space**

1. Let $h:[0,1]\to X$ be a path from $x_0$ to $x_1$. Define the change-of-basepoint map

   $$\beta_h:\pi_1(X,x_1)\to\pi_1(X,x_0),\qquad \beta_h[\gamma]=[\,h\cdot\gamma\cdot\bar h\,].$$
2. It is a homomorphism: $\beta_h[\gamma\cdot\delta]=[h\cdot\gamma\cdot\delta\cdot\bar h]=[h\cdot\gamma\cdot\bar h]\,[h\cdot\delta\cdot\bar h]$, inserting $\bar h\cdot h\simeq c$.
3. It is invertible with inverse $\beta_{\bar h}$, since $\beta_h\beta_{\bar h}=\beta_{h\cdot\bar h}=\beta_c=\mathrm{id}$.

*So $\pi_1(X,x_0)\cong\pi_1(X,x_1)$: on a path-connected space we may write $\pi_1(X)$ up to isomorphism. (The isomorphism is canonical only up to inner automorphism.)*

**Functoriality & the induced homomorphism**

$$f:X\to Y,\ f(x_0)=y_0 \ \Longrightarrow\ f_*:\pi_1(X,x_0)\to\pi_1(Y,y_0),\quad f_*[\gamma]=[f\circ\gamma]$$

$$(g\circ f)_*=g_*\circ f_*,\qquad (\mathrm{id}_X)_*=\mathrm{id},\qquad f\simeq g\ (\text{rel }x_0)\Rightarrow f_*=g_*$$

*These three lines make $\pi_1$ a functor and prove homotopy invariance: $X\simeq Y$ gives $\pi_1(X)\cong\pi_1(Y)$.*

> **Definition — simply connected**
>
> $X$ is **simply connected** if it is path-connected and $\pi_1(X)=0$ (every loop contracts). Examples: $\mathbb{R}^n$, any convex set, and $S^n$ for $n\ge 2$.

> **Connection — to group theory**
>
> $\pi_1$ is generally *non-abelian* (e.g. surfaces, wedges of circles), so the full machinery of free groups, presentations $\langle\text{gens}\mid\text{rels}\rangle$, and normal subgroups enters. This is the bridge into combinatorial group theory.

<a id="s3"></a>
### The circle: $\pi_1(S^1)\cong\mathbb{Z}$ and the winding number

*The foundational computation. Once $\pi_1(S^1)\cong\mathbb{Z}$ is in hand, the great applications fall out almost for free.*

**Theorem**

$$\pi_1(S^1,\,1)\ \cong\ \mathbb{Z},\qquad [\gamma]\ \longmapsto\ \deg(\gamma)=\text{winding number}.$$

*The generator is the loop $\omega(s)=e^{2\pi i s}$; the integer is how many net times a loop wraps around.*

> **Concept — the exponential covering**
>
> The key tool is $p:\mathbb{R}\to S^1,\ p(t)=e^{2\pi i t}$. It wraps the line around the circle, with each point having a discrete fiber $p^{-1}(1)=\mathbb{Z}$. $\mathbb{R}$ is contractible, so loops downstairs become genuine displacements upstairs — a number.

**Demonstration — the covering-space proof**

1. Path lifting. Every path $\gamma:[0,1]\to S^1$ with $\gamma(0)=1$ has a unique lift $\tilde\gamma:[0,1]\to\mathbb{R}$ with $\tilde\gamma(0)=0$ and $p\circ\tilde\gamma=\gamma$. (Cover $S^1$ by evenly-covered arcs; lift piecewise using the local inverses of $p$; uniqueness because two lifts differ by a locally constant — hence constant — integer.)
2. Homotopy lifting. A homotopy of paths $\gamma_t$ lifts to a homotopy $\tilde\gamma_t$ with $\tilde\gamma_t(0)=0$; by uniqueness the endpoints $\tilde\gamma_t(1)$ vary continuously in the discrete set $\mathbb{Z}$, hence are constant.
3. The degree map. Define $\Phi[\gamma]=\tilde\gamma(1)\in\mathbb{Z}$. Step 2 shows it depends only on the homotopy class; it is well defined.
4. Homomorphism. To lift $\alpha\cdot\beta$ starting at $0$: lift $\alpha$ to $\tilde\alpha$ ending at $m$, then lift $\beta$ starting at $m$ — that lift is $m+\tilde\beta$, ending at $m+n$. So $\Phi[\alpha\cdot\beta]=m+n=\Phi[\alpha]+\Phi[\beta]$.
5. Surjective: $\omega_n(s)=e^{2\pi i n s}$ lifts to $t\mapsto nt$, so $\Phi[\omega_n]=n$.
6. Injective: if $\Phi[\gamma]=0$ then $\tilde\gamma$ is a loop in the contractible $\mathbb{R}$, so $\tilde\gamma\simeq 0$ rel endpoints; pushing down by $p$ gives $\gamma\simeq c$. Hence $[\gamma]=1$.

*$\Phi$ is a bijective homomorphism, so $\pi_1(S^1)\cong\mathbb{Z}$. $\;\blacksquare$*

> **Connection — winding number = a contour integral**
>
> For a loop in $\mathbb{C}\setminus\{0\}$ the same integer is $\dfrac{1}{2\pi i}\displaystyle\oint \dfrac{dz}{z}$. The topological degree and the complex-analytic winding number are literally the same invariant — the seam between algebraic topology and complex analysis.

<a id="s4"></a>
### The Seifert–van Kampen theorem

*A "divide and conquer" theorem: it computes $\pi_1$ of a union from the $\pi_1$ of the pieces and their overlap — exactly the tool that turns geometry into group presentations.*

**Theorem (Seifert–van Kampen)**

$$\pi_1(X)\ \cong\ \pi_1(U)\ *_{\pi_1(U\cap V)}\ \pi_1(V),$$

*i.e. the free product $\pi_1(U)*\pi_1(V)$ modulo the relations $i_*(w)=j_*(w)$ for every $w\in\pi_1(U\cap V)$, where $i,j$ are the two inclusions.*

**Demonstration — $\pi_1$ of a wedge of $n$ circles is free**

1. Take $X=S^1\vee\cdots\vee S^1$ ($n$ circles glued at one point). Thicken each circle to an open set $U_k\simeq S^1$ so that any overlap $U_j\cap U_k$ deformation-retracts to the wedge point, hence is contractible: $\pi_1(U_j\cap U_k)=0$.
2. With trivial amalgamating group, the pushout is the plain free product. Iterating van Kampen, the free group on $n$ generators, one generator per circle.

   $$\pi_1\Big(\bigvee_{k=1}^n S^1\Big)\cong\underbrace{\mathbb{Z}*\cdots*\mathbb{Z}}_{n}=F_n,$$

*For $n\ge 2$ this is non-abelian: $ab\ne ba$, reflecting that the two loops cannot be slid past each other.*

**Demonstration — $\pi_1$ of the orientable genus-$g$ surface**

1. Build $\Sigma_g$ as a $4g$-gon with edges identified in the word $a_1b_1a_1^{-1}b_1^{-1}\cdots a_gb_ga_g^{-1}b_g^{-1}$. Let $U$ be the open polygon (a disk, contractible) and $V$ a neighborhood of its boundary 1-skeleton (a wedge of $2g$ circles), with $U\cap V$ an annulus $\simeq S^1$.
2. $\pi_1(U)=1$, $\pi_1(V)=F_{2g}=\langle a_1,b_1,\dots,a_g,b_g\rangle$. The generator of $\pi_1(U\cap V)$ maps to the boundary word in $V$ and to $1$ in $U$.
3. The pushout therefore imposes one relation — the boundary word equals $1$:

   $$\pi_1(\Sigma_g)=\big\langle\, a_1,b_1,\dots,a_g,b_g \ \big|\ \textstyle\prod_{i=1}^g [a_i,b_i]=1 \,\big\rangle.$$

*For the torus ($g=1$) this is $\langle a,b\mid aba^{-1}b^{-1}=1\rangle\cong\mathbb{Z}^2$. Abelianizing gives $\mathbb{Z}^{2g}$, recovering $H_1$.*

> **Connection — pushouts & presentations**
>
> Van Kampen says $\pi_1$ sends gluing of spaces (pushouts in topology) to amalgamated free products (pushouts in groups). Every CW complex thus yields a *presentation* of its $\pi_1$: generators from 1-cells, relations from 2-cells.

<a id="s5"></a>
### Applications: Brouwer (2D), the fundamental theorem of algebra, no retraction

*A single computation, $\pi_1(S^1)\cong\mathbb{Z}$, now does real work. Each proof is the same move: a hypothetical map would induce an impossible homomorphism.*

**Demonstration — no retraction $r:D^2\to S^1$**

1. Suppose a retraction exists: $r:D^2\to S^1$ continuous with $r\circ\iota=\mathrm{id}_{S^1}$, where $\iota:S^1\hookrightarrow D^2$ is the inclusion of the boundary.
2. Apply the functor $\pi_1$:

   $$r_*\circ \iota_*=(\,r\circ\iota\,)_*=(\mathrm{id}_{S^1})_*=\mathrm{id}_{\mathbb{Z}}.$$
3. But $\iota_*:\pi_1(S^1)\to\pi_1(D^2)$ is $\mathbb{Z}\to 0$ (the disk is contractible), so $r_*\circ\iota_*$ factors through the trivial group and must be the zero map — it cannot be $\mathrm{id}_{\mathbb{Z}}$.

*Contradiction: no such retraction exists. $\;\blacksquare$*

**Demonstration — Brouwer fixed-point theorem in 2D**

1. Let $f:D^2\to D^2$ be continuous with no fixed point, so $f(x)\ne x$ for all $x$.
2. Define $r(x)$ = the point where the ray from $f(x)$ through $x$ meets $S^1$. Since $f(x)\ne x$ the ray is well defined and $r$ is continuous.
3. If $x\in S^1$ the ray already starts on the boundary at $x$, so $r(x)=x$: thus $r$ is a retraction $D^2\to S^1$ — impossible by the previous demonstration.

*Hence every continuous self-map of the disk has a fixed point. $\;\blacksquare$*

**Demonstration — the fundamental theorem of algebra**

1. Let $p(z)=z^n+a_{n-1}z^{n-1}+\cdots+a_0$ with $n\ge 1$, and suppose $p$ has no root in $\mathbb{C}$.
2. For each radius $R\ge0$, the loop $\gamma_R(s)=\dfrac{p(Re^{2\pi i s})/p(R)}{|p(Re^{2\pi i s})/p(R)|}$ lives in $S^1$. As $R$ varies these are all homotopic (no root means the denominator never vanishes), so the winding number $\deg(\gamma_R)$ is constant in $R$; at $R=0$ it is $0$.
3. For $R$ very large, $z^n$ dominates, so $p(Re^{2\pi i s})$ winds like $(Re^{2\pi i s})^n$: $\deg(\gamma_R)=n$.
4. Constancy forces $n=0$, contradicting $n\ge1$.

*So $p$ must have a root: $\mathbb{C}$ is algebraically closed — proved by winding numbers. $\;\blacksquare$*

> **Connection — one template, many theorems**
>
> Each proof builds an impossible homomorphism out of a hypothetical map, leveraging $\pi_1(S^1)\cong\mathbb{Z}\ne 0$. Brouwer in all dimensions, the Borsuk–Ulam theorem, and the hairy-ball theorem follow the same pattern with higher invariants ($H_n$, degree).

## Part B · Covering spaces

<a id="s6"></a>
### Covering spaces & the lifting theorems

*Covering spaces are the geometric incarnation of subgroups of $\pi_1$. Lifting is the engine that already powered the circle computation.*

> **Definition — covering space**
>
> A continuous surjection $p:\tilde X\to X$ is a **covering map** if every $x\in X$ has an open neighborhood $U$ that is *evenly covered*: $p^{-1}(U)=\bigsqcup_\alpha V_\alpha$, a disjoint union of opens each mapped homeomorphically onto $U$ by $p$. The fibers $p^{-1}(x)$ are discrete; their common cardinality is the number of **sheets**. Examples: $\mathbb{R}\to S^1$ (infinite sheets), $S^1\xrightarrow{z\mapsto z^n}S^1$ ($n$ sheets), $S^n\to\mathbb{RP}^n$ (2 sheets).

**Lifting theorems**

$$f_*\big(\pi_1(Y,y_0)\big)\ \subseteq\ p_*\big(\pi_1(\tilde X,\tilde x_0)\big),$$

*and when it exists, it is unique.*

**Demonstration — $p_*$ is injective; sheets count the index**

1. Injectivity of $p_*$. If $\tilde\gamma$ is a loop in $\tilde X$ with $p\circ\tilde\gamma\simeq c$ in $X$, lift that nullhomotopy by the homotopy lifting property; uniqueness makes the lift a nullhomotopy of $\tilde\gamma$. So $\ker p_*=1$ and $p_*\pi_1(\tilde X)\hookrightarrow\pi_1(X)$ is a subgroup.
2. Fiber = cosets. For connected $\tilde X$, send a loop class $[\gamma]\in\pi_1(X,x_0)$ to the endpoint of its lift starting at $\tilde x_0$. This gives a bijection the right cosets of the subgroup.

   $$p^{-1}(x_0)\ \longleftrightarrow\ p_*\pi_1(\tilde X,\tilde x_0)\ \backslash\ \pi_1(X,x_0),$$

*Number of sheets $=$ index $[\pi_1(X):p_*\pi_1(\tilde X)]$. Covers are subgroups made visible.*

> **Connection — local-to-global**
>
> "Evenly covered" is a purely local condition, yet it forces the global lifting properties. This local-to-global passage is the same spirit as sheaf theory and as the gluing in van Kampen.

<a id="s7"></a>
### The Galois correspondence: classifying covers & deck transformations

*Covering spaces of a nice space $X$ are classified by subgroups of $\pi_1(X)$ — a dictionary formally identical to Galois theory's correspondence between field extensions and subgroups.*

**Theorem (Galois correspondence for covers)**

$$\left\{\begin{array}{c}\text{connected covers}\\ p:(\tilde X,\tilde x_0)\to(X,x_0)\end{array}\right\}\ \longleftrightarrow\ \left\{\begin{array}{c}\text{subgroups}\\ H\le\pi_1(X,x_0)\end{array}\right\},\qquad p\mapsto p_*\pi_1(\tilde X,\tilde x_0).$$

*Forgetting basepoints, isomorphism classes of covers $\leftrightarrow$ conjugacy classes of subgroups. Smaller subgroup $=$ bigger cover; the trivial subgroup $=$ the universal cover.*

> **Definition — deck transformations & normality**
>
> A **deck transformation** of $p:\tilde X\to X$ is a homeomorphism $\varphi:\tilde X\to\tilde X$ with $p\circ\varphi=p$; they form a group $\mathrm{Deck}(\tilde X/X)$. A cover is **normal (regular/Galois)** when $H=p_*\pi_1(\tilde X)$ is a normal subgroup — equivalently when deck transformations act transitively on each fiber.

**Demonstration — $\mathrm{Deck}\cong N(H)/H$**

1. A deck transformation is a self-lift of $p$ along $p$; by the lifting criterion such lifts correspond to elements of $\pi_1(X)$ that conjugate $H$ into itself, i.e. to the normalizer $N(H)$.
2. Two such elements give the same deck transformation iff they differ by an element of $H$ (which lifts to a loop, the identity deck map). Hence

   $$\mathrm{Deck}(\tilde X/X)\ \cong\ N(H)/H.$$
3. For a normal cover $N(H)=\pi_1(X)$, so $\mathrm{Deck}\cong\pi_1(X)/H$. For the universal cover $H=1$ and $\mathrm{Deck}\cong\pi_1(X)$.

*The deck group plays the role of the Galois group; $\pi_1(X)/H$ is its "Galois group over the base."*

> **Connection — to field theory**
>
> Replace "cover" by "field extension," "subgroup of $\pi_1$" by "subgroup of $\mathrm{Gal}$," "deck group" by "Galois group," "universal cover" by "separable closure." Both are instances of one categorical pattern: a fundamental group acting, with subgroups indexing intermediate objects.

<a id="s8"></a>
### The universal cover

*The biggest connected cover: simply connected, sitting above all the others. It is where $\pi_1$ materializes as a group of symmetries.*

**Theorem — existence & universal property**

$$X\ \cong\ \tilde X/\pi_1(X),\qquad \mathrm{Deck}(\tilde X/X)\cong\pi_1(X).$$

*If $X$ is path-connected, locally path-connected and semilocally simply connected, it has a **universal cover** $\tilde X$ with $\pi_1(\tilde X)=1$. It is universal: for any connected cover $Y\to X$ there is a covering map $\tilde X\to Y$. It is unique up to isomorphism, and*

**Demonstration — construction by homotopy classes of paths**

1. Fix $x_0$. Let $\tilde X=\{\,[\gamma]: \gamma \text{ a path from } x_0,\ \text{taken rel endpoints}\,\}$, with $p[\gamma]=\gamma(1)$.
2. Topologize $\tilde X$ using basic sets indexed by an evenly-covering neighborhood and a path class into it; semilocal simple connectivity makes this consistent (small loops are nullhomotopic in $X$).
3. $\tilde X$ is path-connected (concatenate to slide between classes) and simply connected: a loop upstairs is a homotopy of $\gamma$ downstairs, so its class is constant — it is the trivial loop.
4. $\pi_1(X)$ acts on $\tilde X$ by $[\alpha]\cdot[\gamma]=[\alpha\cdot\gamma]$, freely and properly discontinuously, with quotient $X$. This realizes $\pi_1(X)$ as the deck group.

*Examples: $\widetilde{S^1}=\mathbb{R}$, $\widetilde{T^2}=\mathbb{R}^2$ with deck group $\mathbb{Z}^2$, $\widetilde{\mathbb{RP}^n}=S^n$ with deck group $\mathbb{Z}/2$.*

> **Connection — geometry & group actions**
>
> A free, properly discontinuous action of $G$ on a simply connected $\tilde X$ gives $\pi_1(\tilde X/G)\cong G$. This is how flat tori, hyperbolic surfaces, and lens spaces are built — geometry from group actions on a universal cover.

## Part C · Homology & beyond

<a id="s9"></a>
### Simplicial & CW complexes

*To compute, we need spaces built from standard bricks. Simplices and cells make homology a problem in linear algebra.*

> **Definition — simplices & $\Delta$-complexes**
>
> The **standard $n$-simplex** is $\Delta^n=\{(t_0,\dots,t_n):t_i\ge0,\ \sum t_i=1\}$: a point, segment, triangle, tetrahedron, ... Its faces are obtained by deleting a vertex. A **$\Delta$-complex** glues simplices along faces by affine identifications, with a chosen vertex order fixing orientations.

> **Definition — CW complex**
>
> A **CW complex** is built skeleton by skeleton: start with discrete $0$-cells, then attach $n$-cells $e^n$ by maps $\varphi:\partial D^n=S^{n-1}\to X^{(n-1)}$. "C" = closure-finite, "W" = weak topology. Spheres, projective spaces, surfaces, and Grassmannians all have small, explicit CW structures.

**The boundary operator on simplices**

$$\partial_n[v_0,\dots,v_n]=\sum_{i=0}^{n}(-1)^i\,[v_0,\dots,\widehat{v_i},\dots,v_n]$$

*Drop each vertex in turn; the sign $(-1)^i$ encodes orientation. $[\,\widehat{v_i}\,]$ means "omit $v_i$."*

**Demonstration — the fundamental identity $\partial^2=0$**

1. Apply $\partial$ twice: $\partial_{n-1}\partial_n[v_0,\dots,v_n]=\sum_i(-1)^i\,\partial_{n-1}[\dots\widehat{v_i}\dots]$, expanding each inner boundary over the remaining vertices.
2. Each face $[\dots\widehat{v_i}\dots\widehat{v_j}\dots]$ with $i\lt j$ appears twice: once removing $v_i$ then $v_j$ (sign $(-1)^i(-1)^{j-1}$, since $v_j$ shifts left by one), and once removing $v_j$ then $v_i$ (sign $(-1)^j(-1)^i$).
3. The two signs are opposite, so every term cancels: $\partial_{n-1}\circ\partial_n=0$.

*"The boundary of a boundary is zero" is the algebraic heart of homology — it makes $\operatorname{im}\partial_{n+1}\subseteq\ker\partial_n$.*

> **Connection — to linear algebra**
>
> Fix a ring (usually $\mathbb{Z}$): the $n$-chains $C_n$ are the free module on the $n$-cells, and $\partial_n$ is a matrix. Homology is then just $\ker/\operatorname{im}$ of integer matrices — solvable by Smith normal form.

<a id="s10"></a>
### Singular homology

A definition that works for *every* space, no triangulation required — at the cost of enormous chain groups, redeemed by powerful theorems.

**The singular chain complex**

$$\cdots\xrightarrow{\ \partial_{n+1}\ }C_n(X)\xrightarrow{\ \partial_n\ }C_{n-1}(X)\xrightarrow{\ \partial_{n-1}\ }\cdots\xrightarrow{\ \partial_1\ }C_0(X)\to 0.$$

$$H_n(X)=\frac{\ker\partial_n}{\operatorname{im}\partial_{n+1}}=\frac{\text{cycles }Z_n}{\text{boundaries }B_n}.$$

*A **singular $n$-simplex** is any continuous $\sigma:\Delta^n\to X$. Let $C_n(X)$ be the free abelian group on all of them, with $\partial_n$ defined by the same alternating-face formula. Then $\partial^2=0$, giving a chain complex*

> **Concept — what $H_n$ measures**
>
> A **cycle** is a chain with no boundary (a "closed loop/surface"); a **boundary** is one that bounds. $H_n$ counts $n$-dimensional holes: cycles that are *not* filled in. $H_0$ counts path-components; $H_1$ is the abelianization of $\pi_1$; higher $H_n$ see higher-dimensional voids.

**Demonstration — $H_0(X)\cong\mathbb{Z}^{\#\text{path-components}}$**

1. $\partial_0=0$, so $Z_0=C_0(X)$, the free group on points. A 1-simplex (path) $\sigma$ has $\partial_1\sigma=\sigma(1)-\sigma(0)$, so $B_0$ is generated by all differences of points joined by a path.
2. Thus two points are homologous iff they lie in the same path-component; $H_0=Z_0/B_0$ is free abelian with one generator per path-component.

*For path-connected $X$, $H_0(X)\cong\mathbb{Z}$. The "augmentation" $\sum n_i\sigma_i\mapsto\sum n_i$ makes this precise.*

**Hurewicz (degree 1)**

$$X\text{ path-connected}\ \Longrightarrow\ H_1(X)\ \cong\ \pi_1(X)^{\mathrm{ab}}=\pi_1(X)/[\pi_1,\pi_1].$$

*Homology is $\pi_1$ made abelian: it forgets the order of loops. So $H_1(\Sigma_g)\cong\mathbb{Z}^{2g}$, $H_1(\bigvee_n S^1)\cong\mathbb{Z}^n$.*

<a id="s11"></a>
### Homotopy invariance & the exact sequences

*The three pillars that make homology computable: invariance, the long exact sequence of a pair, and Mayer–Vietoris.*

**Functoriality & homotopy invariance**

$$f:X\to Y\ \Rightarrow\ f_*:H_n(X)\to H_n(Y),\qquad (g\circ f)_*=g_*f_*,\qquad f\simeq g\Rightarrow f_*=g_*.$$

*Consequently $X\simeq Y\Rightarrow H_n(X)\cong H_n(Y)$: homology is a homotopy invariant, so a contractible space has $H_n=0$ for $n\gt 0$ and $H_0=\mathbb{Z}$.*

> **Concept — exact sequences**
>
> A sequence $\cdots\to A\xrightarrow{\,f\,}B\xrightarrow{\,g\,}C\to\cdots$ is **exact** at $B$ if $\operatorname{im}f=\ker g$. Exactness is a bookkeeping device that lets unknown groups be pinned down by their neighbors. A **short exact sequence** $0\to A\to B\to C\to 0$ says $A\hookrightarrow B$ and $B\twoheadrightarrow C$ with kernel $A$.

**Long exact sequence of a pair $(X,A)$**

$$\cdots\to H_n(A)\xrightarrow{i_*}H_n(X)\xrightarrow{j_*}H_n(X,A)\xrightarrow{\ \partial\ }H_{n-1}(A)\xrightarrow{i_*}H_{n-1}(X)\to\cdots$$

*Relative homology $H_n(X,A)$ measures $X$ "modulo" $A$; the connecting map $\partial$ takes a relative cycle to the boundary it leaves behind in $A$. Exactness chains the three together.*

**Mayer–Vietoris**

$$\cdots\to H_n(U\cap V)\xrightarrow{(i_*,j_*)}H_n(U)\oplus H_n(V)\xrightarrow{k_*-l_*}H_n(X)\xrightarrow{\ \partial\ }H_{n-1}(U\cap V)\to\cdots$$

*For $X=U\cup V$ (interiors covering $X$). This is the homology analogue of van Kampen: it computes the whole from overlapping pieces.*

**Demonstration — Mayer–Vietoris gives $H_n(S^k)$**

1. Cover $S^k$ by two slightly overlapping hemispheres $U,V$, each contractible (so $H_*(U)=H_*(V)=H_*(\text{pt})$); the overlap $U\cap V\simeq S^{k-1}$ (an equatorial band).
2. For $n\ge 2$, the sequence has $H_n(U)\oplus H_n(V)=0$ on the left and $H_{n-1}(U)\oplus H_{n-1}(V)=0$ on the right, so $\partial:H_n(S^k)\xrightarrow{\cong}H_{n-1}(S^{k-1})$ is an isomorphism.
3. Induct from the base case $S^0$ (two points): $\tilde H_0(S^0)=\mathbb{Z}$. Shifting up $k$ times gives $\tilde H_n(S^k)=\mathbb{Z}$ when $n=k$, else $0$.

*$\displaystyle H_n(S^k)=\begin{cases}\mathbb{Z},& n=0 \text{ or } n=k,\\ 0,&\text{otherwise}\end{cases}$ (with $\mathbb{Z}^2$ at $n=0=k$ for $S^0$). $\;\blacksquare$*

> **Connection — homological algebra**
>
> The connecting map $\partial$ and the long exact sequence come from the *snake lemma* applied to a short exact sequence of chain complexes. This is the same machinery used throughout algebra — for $\mathrm{Tor}$, $\mathrm{Ext}$, and derived functors.

<a id="s12"></a>
### Computing homology: degree, Euler characteristic, Betti numbers

*Now we compute, and read the numerical invariants — Betti numbers and the Euler characteristic — straight off the homology.*

**Demonstration — simplicial homology of $S^1$, $S^2$, and the torus**

1. $S^1$ as one vertex $v$ and one edge $a$ (a loop). Then $\partial_1 a=v-v=0$, so $Z_1=\mathbb{Z}\langle a\rangle$, $B_1=0$: $H_1=\mathbb{Z}$. And $H_0=\mathbb{Z}$. So $H_*(S^1)=(\mathbb{Z},\mathbb{Z},0,\dots)$.
2. $S^2$ with two triangular faces glued along their common boundary: chain groups give $H_0=\mathbb{Z}$, $H_1=0$, $H_2=\mathbb{Z}$ (the two faces with opposite orientation sum to a 2-cycle bounding nothing).
3. Torus $T^2$ from the square $aba^{-1}b^{-1}$: one vertex, two edges $a,b$, one face $f$. Then $\partial_2 f=a+b-a-b=0$ so $H_2=\mathbb{Z}\langle f\rangle$; $\partial_1 a=\partial_1 b=0$ so $Z_1=\mathbb{Z}^2$ with $B_1=0$, giving $H_1=\mathbb{Z}^2$; and $H_0=\mathbb{Z}$.

*$H_*(T^2)=(\mathbb{Z},\ \mathbb{Z}^2,\ \mathbb{Z},\ 0,\dots)$ — one component, two independent loops, one void. $\;\blacksquare$*

**Degree of a map $f:S^n\to S^n$**

$$f_*:H_n(S^n)=\mathbb{Z}\to H_n(S^n)=\mathbb{Z}\quad\text{is multiplication by }\deg f.$$

*$\deg(\mathrm{id})=1$, $\deg(\text{constant})=0$, $\deg(g\circ f)=\deg g\cdot\deg f$, and the antipodal map has degree $(-1)^{n+1}$. Degree powers the hairy-ball theorem and higher-dimensional Brouwer.*

**Betti numbers & Euler characteristic**

$$b_n=\operatorname{rank} H_n(X)=\dim_{\mathbb{Q}} H_n(X;\mathbb{Q}),\qquad \chi(X)=\sum_{n\ge0}(-1)^n b_n.$$

*$b_0=\#$components, $b_1=\#$independent loops, $b_2=\#$independent voids. Torsion (e.g. the $\mathbb{Z}/2$ in $\mathbb{RP}^2$) does not affect $b_n$ or $\chi$.*

**Demonstration — Euler characteristic via Betti numbers**

1. For a finite complex let $c_n$ be the number of $n$-cells and $z_n=\operatorname{rank}Z_n$, $b_n^{\partial}=\operatorname{rank}B_n$. Rank–nullity on $\partial_n:C_n\to C_{n-1}$ gives $c_n=z_n+b_{n-1}^{\partial}$.
2. By definition $b_n=z_n-b_n^{\partial}$ (rank of $\ker$ minus rank of $\operatorname{im}$). Form the alternating sum:

   $$\sum_n(-1)^n c_n=\sum_n(-1)^n\big(z_n+b_{n-1}^{\partial}\big).$$
3. The $b^{\partial}$ terms telescope against the $z$ terms, leaving

   $$\sum_n(-1)^n c_n=\sum_n(-1)^n b_n=\chi(X).$$

*So $\chi$ computed from *cells* equals $\chi$ from *homology* — a topological invariant. For surfaces $V-E+F=2-2g$. $\;\blacksquare$*

| Space | $\pi_1$ | $H_0,H_1,H_2,\dots$ | $\chi$ |
| --- | --- | --- | --- |
| Point | $1$ | $\mathbb{Z},0,0,\dots$ | $1$ |
| $S^1$ | $\mathbb{Z}$ | $\mathbb{Z},\mathbb{Z},0,\dots$ | $0$ |
| $S^n\ (n\ge2)$ | $1$ | $\mathbb{Z},0,\dots,\mathbb{Z}\,(\deg n),0,\dots$ | $1+(-1)^n$ |
| Torus $T^2$ | $\mathbb{Z}^2$ | $\mathbb{Z},\mathbb{Z}^2,\mathbb{Z},0,\dots$ | $0$ |
| $\Sigma_g$ (genus $g$) | $\langle a_i,b_i\mid\prod[a_i,b_i]\rangle$ | $\mathbb{Z},\mathbb{Z}^{2g},\mathbb{Z},0,\dots$ | $2-2g$ |
| $\bigvee_n S^1$ | $F_n$ (free) | $\mathbb{Z},\mathbb{Z}^n,0,\dots$ | $1-n$ |
| $\mathbb{RP}^2$ | $\mathbb{Z}/2$ | $\mathbb{Z},\ \mathbb{Z}/2,\ 0,\dots$ | $1$ |
| $\mathbb{RP}^n$ ($n$ odd) | $\mathbb{Z}/2$ | $\mathbb{Z},\mathbb{Z}/2,\dots,\mathbb{Z}$ | $0$ |
| $\mathbb{RP}^n$ ($n$ even) | $\mathbb{Z}/2$ | $\mathbb{Z},\mathbb{Z}/2,\dots,0$ | $1$ |

> **Connection — abstract algebra reappears**
>
> Over $\mathbb{Z}$, the structure theorem for finitely generated abelian groups splits $H_n\cong\mathbb{Z}^{b_n}\oplus(\text{torsion})$. Betti numbers are the free rank; torsion (like $\mathbb{Z}/2$ for $\mathbb{RP}^n$) records subtler "twisting" invisible to $\chi$.

<a id="s13"></a>
### Cohomology & the cup product

Dualizing chains gives cohomology — the same Betti numbers, but now with a *ring* structure that homology lacks. The extra multiplication separates spaces homology cannot.

**The cochain complex & cohomology**

$$C^n(X;R)=\operatorname{Hom}(C_n(X),R),\qquad \delta=\partial^{*}:C^n\to C^{n+1},\qquad H^n(X;R)=\frac{\ker\delta}{\operatorname{im}\delta}.$$

*Coboundary $\delta$ is the transpose of $\partial$; $\delta^2=0$ since $\partial^2=0$. Arrows now point *up* in degree, making cohomology contravariant: $f:X\to Y$ gives $f^*:H^n(Y)\to H^n(X)$.*

**Universal coefficients**

$$0\to \operatorname{Ext}^1_{\mathbb{Z}}(H_{n-1}(X),R)\to H^n(X;R)\to \operatorname{Hom}(H_n(X),R)\to 0.$$

*Over a field, $\operatorname{Ext}=0$ and $H^n\cong\operatorname{Hom}(H_n,\text{field})$: same Betti numbers as homology. The novelty is multiplicative, not additive.*

> **Definition — the cup product & cohomology ring**
>
> The **cup product** $\smile:H^p(X;R)\times H^q(X;R)\to H^{p+q}(X;R)$ makes $H^*(X;R)=\bigoplus_n H^n$ a graded ring. It is graded-commutative: $\alpha\smile\beta=(-1)^{pq}\,\beta\smile\alpha$, and natural: $f^*(\alpha\smile\beta)=f^*\alpha\smile f^*\beta$.

**Demonstration — cup product separates $T^2$ from $S^2\vee S^1\vee S^1$**

1. Both spaces have identical homology and cohomology groups: $H^0=\mathbb{Z}$, $H^1=\mathbb{Z}^2$, $H^2=\mathbb{Z}$. Additive invariants cannot tell them apart.
2. For the torus, with $H^1=\langle\alpha,\beta\rangle$, the cup product is nondegenerate: $\alpha\smile\beta$ generates $H^2=\mathbb{Z}$ (and $\alpha\smile\alpha=0$). The ring is the exterior algebra $\Lambda[\alpha,\beta]$.
3. For the wedge $S^2\vee S^1\vee S^1$, any product of two classes from different wedge summands is $0$ (they share only the basepoint): $\alpha\smile\beta=0$. The product is trivial.

*Different ring structures $\Rightarrow$ the spaces are not homotopy equivalent — a distinction invisible to homology alone. $\;\blacksquare$*

> **Connection — to differential geometry**
>
> For smooth manifolds, **de Rham cohomology** (closed modulo exact differential forms) computes $H^*(X;\mathbb{R})$, and the cup product becomes the *wedge product* of forms. Topology, calculus on manifolds, and ring theory meet in one object.

<a id="s14"></a>
### A glimpse beyond: higher homotopy groups, manifolds & Poincaré duality

*Where the subject opens up: higher $\pi_n$ (hard but rich), the special structure of manifolds, and the duality that organizes their (co)homology.*

> **Definition — higher homotopy groups $\pi_n$**
>
> $\pi_n(X,x_0)$ is homotopy classes of based maps $S^n\to X$. For $n\ge2$ they are **abelian** (the Eckmann–Hilton argument: two commuting unital products on the same set must coincide and be commutative). Unlike homology, $\pi_n$ is brutally hard — even $\pi_k(S^n)$ for $k\gt n$ is largely mysterious (the "stable homotopy groups of spheres").

**Hurewicz theorem (general)**

$$\pi_k(X)=0\ \text{for } k\lt n\ (n\ge2)\ \Longrightarrow\ H_k(X)=0\ (0\lt k\lt n)\ \text{and}\ \pi_n(X)\cong H_n(X).$$

*The first nonzero homotopy and homology groups agree. This is the bridge from the computable ($H_*$) back to the elusive ($\pi_*$).*

**Poincaré duality**

$$M\text{ closed oriented }n\text{-manifold}\ \Longrightarrow\ H_k(M;\mathbb{Z})\ \cong\ H^{n-k}(M;\mathbb{Z}).$$

$$\text{In particular}\quad b_k(M)=b_{n-k}(M).$$

*Cap product with the fundamental class $[M]\in H_n(M)$ gives the isomorphism. Betti numbers are symmetric; for odd-dimensional closed orientable $M$ this forces $\chi(M)=0$.*

**Demonstration — duality on the genus-$g$ surface**

1. $\Sigma_g$ is a closed oriented $2$-manifold with $b_0=1,\ b_1=2g,\ b_2=1$.
2. Poincaré duality predicts $b_0=b_2$ ($\;1=1\;\checkmark$) and $b_1=b_1$ (trivially). The pairing $H^1\times H^1\to H^2\cong\mathbb{Z}$ is the cup product of Section 13 — the intersection form, a nondegenerate skew-symmetric pairing of rank $2g$.

*Geometrically, each loop $a_i$ has a dual loop $b_i$ crossing it exactly once: holes come in dual pairs. $\;\blacksquare$*

> **Connection — the larger landscape**
>
> From here: fiber bundles and the long exact sequence of a fibration, spectral sequences, characteristic classes (Chern, Stiefel–Whitney), K-theory, and the cobordism / surgery program that classifies manifolds. Every road still starts from one idea — a functor from spaces to algebra, computed via exact sequences.

---

*A first course in algebraic topology — concepts, definitions, theorems, and the demonstrations behind them — built as a companion to the Complete Statistics and Calculus guides. Read once for the shape; return to any box as a reference. Remember: every chapter is one functor turning continuous maps into homomorphisms, so that different algebra proves different spaces.*
