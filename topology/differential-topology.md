**English** · [中文](differential-topology.zh.md)

# Differential Topology & Characteristic Classes, *the shape of smooth spaces.*

*A self-contained, rigorous first course in the topology you can do with calculus. We take a smooth manifold — a space that looks like flat $\mathbb{R}^n$ up close and on which differentiation makes sense — and extract from it whole numbers and cohomology classes that do not change under deformation: degrees, Euler characteristics, characteristic classes. The thread is the unity of analysis (derivatives, integrals), topology (invariants under deformation), and geometry (curvature). Every theorem is motivated in plain words, every term is defined on first use, and every claim is argued, not asserted.*

[← Back to all guides](../README.md)

> **How to read this guide.** We assume the **General Topology** guide (topological space, open set, continuous map, homeomorphism, compact, connected, Hausdorff), the **Algebraic Topology** guide (homotopy, the fundamental group $\pi_1$, homology $H_n$, cohomology $H^n$, the Euler characteristic as an alternating sum of Betti numbers), and the **Differential Geometry** guide (smooth manifold, tangent space, differential forms, the exterior derivative $d$, the wedge product $\wedge$, integration of forms, connections and curvature). Whenever we lean on one of these, we restate the exact fact we need in one line. No prior differential topology is assumed; every new word — *immersion*, *transversal*, *degree*, *characteristic class* — is defined the first time it appears.

---

## Part A · The calculus of smooth maps

<a id="s0"></a>
### Motivation — global invariants from local calculus

A **smooth manifold** is a space $M$ that near every point looks like a piece of $\mathbb{R}^n$, with the looking-like-$\mathbb{R}^n$ identifications chosen so smoothly that "differentiable function on $M$" is a meaningful, coordinate-independent notion (precise definition in §s1). Examples: the circle $S^1$, the sphere $S^2$, the torus $T^2$, the space of rotations $SO(3)$.

Calculus is *local*: a derivative at a point sees only an infinitesimal neighborhood. Yet some quantities assembled from local calculus turn out to depend only on the *global* shape of $M$ and not on the particular function, metric, or coordinates used to compute them. Three running examples, each proved later in this guide:

- **The degree of a map** $f:M\to N$ between equal-dimensional closed manifolds is an integer that counts, with signs, how many times $M$ wraps around $N$. It is computed at a single well-chosen point yet is the same for *every* such point and is unchanged when $f$ is deformed (§s5).
- **The Euler characteristic** $\chi(M)$ — already met in algebraic topology as $\chi=\sum_k(-1)^k b_k$, the alternating sum of Betti numbers $b_k=\dim H_k(M;\mathbb{Q})$ — can be recovered by *counting zeros of a vector field* (§s6) or by *integrating curvature* (§s11). Three definitions, one number.
- **Characteristic classes** are cohomology classes attached to vector bundles (families of vector spaces over $M$) that obstruct the bundle from being trivial; they are built either by axioms (§s8) or by integrating curvature (§s10).

The astonishing fact organizing the whole subject is this **unity**: an analytic object (an integral of a curvature form), a topological object (an alternating sum of dimensions), and a geometric object (a sum of indices of a vector field) coincide. The Gauss–Bonnet theorem (§s11) is the first instance; the Atiyah–Singer index theorem (§s11) is the grand generalization. Our job is to build the vocabulary and prove the links.

> **Principle — the differential-topology strategy.**
> Use the derivative to convert a *nonlinear* map between curved spaces into a *linear* map between flat tangent spaces (§s2), at which point linear algebra applies pointwise. Then control the few points where the linear picture degenerates (critical points, non-transverse intersections, zeros of sections). The bookkeeping of those special points — counted with signs — is the global invariant.

**How the chapters fit together (a roadmap).** Part A is the calculus toolkit: what a smooth map is and what its derivative does (§s1–s2), the two theorems that *manufacture* manifolds and keep constructions generic (§s3 Sard, §s4 transversality). Part B spends that toolkit on two integer invariants got by *signed counting*: the degree of a map (§s5) and the Euler characteristic via vector-field indices (§s6). Part C lifts the counting into cohomology: de Rham theory and duality (§s7), then characteristic classes of bundles two ways — axiomatically (§s8–s9) and analytically from curvature (§s10) — culminating in the Gauss–Bonnet and Atiyah–Singer theorems (§s11) that identify the analytic, topological, and geometric incarnations of one number. A reader in a hurry can read §s0, §s5, §s6, and §s11 and still see the whole arc; the rest supplies the machinery and the proofs.

A single slogan threads it all: **degree, index, Euler number, Chern number, and analytic index are five names for "signed count of degeneracies," and each equals a curvature integral.** Everything below is the careful unpacking of that sentence.

<a id="s1"></a>
### Smooth manifolds and smooth maps; partitions of unity

> **Definition — chart, atlas, smooth manifold.**
> Let $M$ be a topological space that is **Hausdorff** (any two points have disjoint open neighborhoods) and **second countable** (it has a countable base of open sets); these mild conditions rule out pathologies. A **chart** is a pair $(U,\varphi)$ where $U\subseteq M$ is open and $\varphi:U\to \varphi(U)\subseteq\mathbb{R}^n$ is a homeomorphism onto an open subset of $\mathbb{R}^n$; it assigns *coordinates* $\varphi(p)=(x^1,\dots,x^n)$ to each point $p\in U$. Two charts $(U,\varphi)$, $(V,\psi)$ are **smoothly compatible** if the **transition map** $\psi\circ\varphi^{-1}:\varphi(U\cap V)\to\psi(U\cap V)$ — a map between open subsets of $\mathbb{R}^n$ — is infinitely differentiable ($C^\infty$), as is its inverse. An **atlas** is a collection of charts whose domains cover $M$, all pairwise smoothly compatible. A **smooth manifold of dimension $n$** is $M$ together with a maximal such atlas. The number $n$ is the **dimension**, written $\dim M$.

The point of the compatibility condition: "$f:M\to\mathbb{R}$ is smooth" can be defined as "$f\circ\varphi^{-1}$ is smooth on $\mathbb{R}^n$ for every chart," and the chain rule guarantees this does not depend on which chart we pick.

> **Definition — smooth map.**
> A map $f:M\to N$ between smooth manifolds is **smooth** if for every $p\in M$ there are charts $(U,\varphi)$ around $p$ and $(V,\psi)$ around $f(p)$ with $f(U)\subseteq V$ such that the **coordinate representative** $\psi\circ f\circ\varphi^{-1}:\varphi(U)\to\psi(V)$ is $C^\infty$ as a map between open subsets of Euclidean spaces. A smooth map with a smooth inverse is a **diffeomorphism**; then $M$ and $N$ are "the same smooth manifold relabelled."

**Worked example — the circle is a smooth $1$-manifold.** Let $S^1=\{(x,y):x^2+y^2=1\}$. Cover it by two charts: $U=S^1\setminus\{(0,1)\}$ with stereographic projection from the north pole, $\varphi(x,y)=x/(1-y)$, and $V=S^1\setminus\{(0,-1)\}$ from the south pole, $\psi(x,y)=x/(1+y)$. On the overlap $U\cap V$ (everything except the two poles) one computes the transition map $\psi\circ\varphi^{-1}(t)=1/t$, which is $C^\infty$ on $\mathbb{R}\setminus\{0\}$ with $C^\infty$ inverse $t\mapsto 1/t$. So the two charts are compatible and $S^1$ is a smooth $1$-manifold.

Now the workhorse tool. Calculus is local, but we constantly need to *assemble* local data (a vector field defined chart-by-chart, an integral over the whole manifold) into a global object without seams. The device that does the gluing is the partition of unity.

> **Definition — support; partition of unity.**
> The **support** of a function $f:M\to\mathbb{R}$ is $\operatorname{supp} f=\overline{\{p:f(p)\neq 0\}}$, the closure of the set where $f$ is nonzero. A family of functions $\{f_\alpha\}$ is **locally finite** if every point has a neighborhood meeting $\operatorname{supp} f_\alpha$ for only finitely many $\alpha$. Given an open cover $\{U_\alpha\}$ of $M$, a **partition of unity subordinate to $\{U_\alpha\}$** is a family of smooth functions $\rho_\alpha:M\to[0,1]$ with (i) $\operatorname{supp}\rho_\alpha\subseteq U_\alpha$, (ii) the family is locally finite, and (iii) $\sum_\alpha \rho_\alpha(p)=1$ for every $p\in M$ (a finite sum at each point by (ii)).

> **Theorem (existence of partitions of unity).** Every smooth manifold (Hausdorff, second countable) admits a smooth partition of unity subordinate to any given open cover.

The construction rests on a single explicit gadget — a smooth function that is positive on a ball and zero outside a slightly larger ball — so we exhibit it.

**Demonstration — the smooth bump function, the seed of every partition of unity.**

1. Define $h:\mathbb{R}\to\mathbb{R}$ by $h(t)=e^{-1/t}$ for $t>0$ and $h(t)=0$ for $t\le 0$. For $t>0$ every derivative is a rational function in $1/t$ times $e^{-1/t}$; as $t\to 0^+$, $e^{-1/t}$ decays faster than any power $1/t^k$ grows (because $e^{1/t}\ge (1/t)^k/k!$ from the exponential series), so every derivative tends to $0$. Hence all one-sided derivatives at $0$ match the value $0$ from the left, and $h\in C^\infty(\mathbb{R})$. *(definition of $C^\infty$; comparison of exponential vs. polynomial growth)*
2. Set $g(t)=h(t)\,h(1-t)$. Then $g>0$ exactly on $0<t<1$ and $g=0$ elsewhere, and $g\in C^\infty$ as a product of $C^\infty$ functions. *(product rule keeps smoothness)*
3. Let $G(t)=\dfrac{\int_t^\infty g}{\int_0^1 g}$ (a normalized tail integral). By the fundamental theorem of calculus $G$ is $C^\infty$, with $G(t)=1$ for $t\le 0$ and $G(t)=0$ for $t\ge 1$, decreasing in between — a smooth step from $1$ down to $0$. *(integrating a $C^\infty$ function gives a $C^\infty$ function)*
4. Now define on $\mathbb{R}^n$ the **bump** $\beta(x)=G(|x|^2)$ rescaled: $\beta=1$ on the ball $|x|\le r$, $\beta=0$ outside $|x|\le R$ for chosen $0<r<R$, smooth and valued in $[0,1]$. We have a $C^\infty$ function equal to $1$ near a point and supported in any prescribed neighborhood. *(compose smooth $G$ with smooth $x\mapsto|x|^2$)*
5. To build the partition: by second countability and Hausdorffness $M$ admits a locally finite refinement of $\{U_\alpha\}$ by chart domains $\{V_i\}$, each carrying a bump $\beta_i\ge 0$ with $\operatorname{supp}\beta_i\subseteq V_i$ and $\sum_i\beta_i>0$ everywhere (every point sits inside some $V_i$ where its bump is positive). Set $\rho_i=\beta_i/\sum_j\beta_j$. The sum is locally finite, so $\rho_i\in C^\infty$, $\rho_i\ge 0$, and $\sum_i\rho_i=1$. Reindexing the $V_i$ into the original $U_\alpha$ gives the claimed partition. $\;\blacksquare$

**What partitions of unity buy you.** Three things we use repeatedly. (a) *Globalize local objects:* if each $U_\alpha$ carries an object $s_\alpha$ (a metric, a connection, a function), then $\sum_\alpha\rho_\alpha s_\alpha$ is a global object, provided the objects live in a *convex* set so that the weighted average makes sense — this is how every manifold gets a Riemannian metric (§s11) and how vector bundles get connections (§s10). (b) *Define integration over $M$:* write $\int_M\omega=\sum_\alpha\int_M\rho_\alpha\omega$, each summand supported in one chart where the ordinary multivariable integral applies (§s7). (c) *Extend functions:* a function defined near a closed set extends smoothly to all of $M$ by multiplying with a bump. The smooth category is *soft* — these constructions have no analogue for analytic or holomorphic functions, where rigidity forbids bumps.

> **Pitfall.** Partitions of unity require the manifold to be **paracompact** (here guaranteed by second countability + Hausdorff). Drop these and the existence theorem can fail. Also, a partition of unity is *not* unique; everything built from one (the integral, the metric) is the same in cohomology or up to a contractible choice, which is exactly why the resulting invariants are well defined.

**Worked example — gluing a global Riemannian metric.** A **Riemannian metric** is a smooth choice of inner product $g_p(\cdot,\cdot)$ on each tangent space $T_pM$. Locally, every chart $(U_\alpha,\varphi_\alpha)$ pulls back the standard dot product of $\mathbb{R}^n$ to a metric $g_\alpha$ on $U_\alpha$. These do not agree on overlaps, but we average them: with a subordinate partition $\{\rho_\alpha\}$ set
$$
g(p)=\sum_\alpha \rho_\alpha(p)\,g_\alpha(p).
$$
At each $p$ this is a positive combination (coefficients $\rho_\alpha(p)\ge0$ summing to $1$) of positive-definite forms, hence positive-definite — the crucial point is that *positive-definite inner products form a convex set*, so the average stays positive-definite. Thus **every** smooth manifold carries a Riemannian metric. The same averaging fails for, say, a *complex structure* (those do not form a convex set), which is why not every manifold is complex — the softness has limits, and tracking exactly where it fails is itself a source of invariants.

<a id="s2"></a>
### The differential; immersions, submersions, embeddings; Whitney

> **Definition — tangent space and the differential.**
> The **tangent space** $T_pM$ at $p\in M$ is the $n$-dimensional vector space of velocity vectors of smooth curves through $p$ (from the Differential Geometry guide); in a chart with coordinates $x^i$ it has basis $\partial/\partial x^1,\dots,\partial/\partial x^n$. Given a smooth $f:M\to N$, its **differential** (or **pushforward**) at $p$ is the linear map
> $$df_p:T_pM\to T_{f(p)}N$$
> sending the velocity of a curve $\gamma$ at $p$ to the velocity of $f\circ\gamma$ at $f(p)$. In coordinates $df_p$ is the **Jacobian matrix** $\big[\partial(\psi\circ f\circ\varphi^{-1})^a/\partial x^i\big]$ of partial derivatives of $f$'s coordinate representative.

The differential is the best *linear* approximation of $f$ at $p$. Its rank — the dimension of its image — classifies how $f$ behaves locally.

> **Definition — immersion, submersion, embedding.**
> A smooth map $f:M\to N$ is an **immersion** if $df_p$ is *injective* at every $p$ (so $\dim M\le\dim N$ and no tangent direction gets crushed); a **submersion** if $df_p$ is *surjective* at every $p$ (so $\dim M\ge\dim N$). An **embedding** is an immersion that is also a homeomorphism onto its image $f(M)$ (with the subspace topology) — an immersion with no self-crossings and no asymptotic self-approach. The image of an embedding is an **embedded submanifold**.

**Worked example — immersion vs. embedding.** The map $f:\mathbb{R}\to\mathbb{R}^2$, $f(t)=(\cos 2\pi t,\sin 2\pi t)$ has $df_t=2\pi(-\sin,\cos)\neq 0$, so it is an immersion, but it is not injective (period $1$), so not an embedding; restricted to $(0,1)$ it is injective yet still not an embedding because the image (a circle minus a point) is not homeomorphic to the open interval near the missing point — the ends come back together. The figure-eight curve $t\mapsto(\sin 2t,\sin t)$ on $(-\pi,\pi)$ is an injective immersion that is *not* an embedding: it is bijective onto its image but not a homeomorphism, since the crossing point has a neighborhood that looks like an "X," not a line.

**Worked example — a submersion and its fibers.** The projection $\pi:\mathbb{R}^3\setminus\{0\}\to S^2$, $\pi(x)=x/|x|$, has differential of rank $2$ everywhere (it kills only the radial direction), so it is a submersion. By the upcoming preimage theorem (§s3) every fiber $\pi^{-1}(u)$ is a $1$-manifold — indeed the open ray through $u$. More famously the **Hopf map** $h:S^3\to S^2$ (write $S^3\subset\mathbb{C}^2$ as pairs $(z_1,z_2)$ with $|z_1|^2+|z_2|^2=1$ and send them to the line they span in $\mathbb{CP}^1=S^2$) is a submersion whose fibers are *circles*, linked pairwise — the first hint that bundles over a base can twist (§s8).

A clean way to see why the rank of $df_p$ is the whole story is to write, in charts, the first-order Taylor expansion
$$
(\psi\circ f\circ\varphi^{-1})(x) = (\psi\circ f\circ\varphi^{-1})(x_0) + J(x_0)\,(x-x_0) + o(|x-x_0|),
$$
where $J(x_0)$ is the Jacobian, i.e. the matrix of $df_p$. To first order $f$ *is* the linear map $J$, so injectivity/surjectivity of $J$ governs the local behavior; the normal-form theorems below promote this first-order picture to an exact statement in well-chosen coordinates.

The basic structural fact behind both notions is the rank theorem: where the rank of $df$ is locally constant, $f$ looks in suitable coordinates like a linear projection or inclusion. We record the two extreme cases.

> **Theorem (local normal forms).** If $f$ is an immersion at $p$, there are charts in which $f(x^1,\dots,x^m)=(x^1,\dots,x^m,0,\dots,0)$ (standard inclusion $\mathbb{R}^m\hookrightarrow\mathbb{R}^n$). If $f$ is a submersion at $p$, there are charts in which $f(x^1,\dots,x^m)=(x^1,\dots,x^n)$ (standard projection $\mathbb{R}^m\twoheadrightarrow\mathbb{R}^n$).

These follow from the inverse function theorem applied to a completed/augmented map; we use them in §s3 to manufacture submanifolds.

> **Theorem (Whitney embedding theorem, statement).** Every smooth $n$-manifold (Hausdorff, second countable) admits a smooth **embedding** into $\mathbb{R}^{2n}$, and an immersion into $\mathbb{R}^{2n-1}$.

This is the precise sense in which "abstract manifold" is no more general than "submanifold of Euclidean space": every manifold *can* be realized concretely inside some $\mathbb{R}^N$. The dimension $2n$ is sharp (e.g. the Klein bottle, a $2$-manifold, needs $\mathbb{R}^4$; it does not embed in $\mathbb{R}^3$). The reason $2n$ appears is a transversality count (§s4): a generic projection of $M^n\subset\mathbb{R}^N$ to a hyperplane stays an embedding as long as the *secant directions* (lines through pairs of points of $M$) and *tangent directions* — a set of dimension at most $2n$ and $2n-1$ respectively — do not fill up the available $N-1$ directions, which holds once $N>2n$. Pushing $N$ down to exactly $2n$ is the delicate part. We do not prove the full theorem, but we can prove the easy half — embedding *compact* manifolds into *some* $\mathbb{R}^N$ — since it shows partitions of unity at work.

**Demonstration — every compact $n$-manifold embeds in some $\mathbb{R}^N$.**

1. Compactness gives a finite atlas $(U_1,\varphi_1),\dots,(U_k,\varphi_k)$ and a subordinate partition of unity $\rho_1,\dots,\rho_k$ with $\operatorname{supp}\rho_i\subseteq U_i$ (§s1). *(partition of unity exists)*
2. Define $F:M\to\mathbb{R}^{k(n+1)}$ by $F(p)=\big(\rho_1(p)\varphi_1(p),\dots,\rho_k(p)\varphi_k(p),\;\rho_1(p),\dots,\rho_k(p)\big)$, where $\rho_i\varphi_i$ is extended by $0$ off $U_i$ (smooth because $\rho_i$ vanishes near $\partial U_i$). $F$ is smooth. *(smoothness of each smooth block; bump extension from §s1)*
3. $F$ is an immersion: fix $p$, pick $i$ with $\rho_i(p)>0$; near $p$ the block $\rho_i\varphi_i$ together with $\rho_i$ recovers $\varphi_i$ (divide by $\rho_i$), whose differential is invertible, so $dF_p$ is injective. *(charts are diffeomorphisms, so $d\varphi_i$ is invertible)*
4. $F$ is injective: if $F(p)=F(q)$ then all $\rho_i(p)=\rho_i(q)$; choosing $i$ with $\rho_i(p)>0$ gives $\rho_i(q)>0$ too, so $p,q\in U_i$, and $\rho_i(p)\varphi_i(p)=\rho_i(q)\varphi_i(q)$ with equal positive $\rho_i$ forces $\varphi_i(p)=\varphi_i(q)$, hence $p=q$ since $\varphi_i$ is injective. *(charts are injective)*
5. An injective immersion from a *compact* space to a Hausdorff space is an embedding, because a continuous bijection from a compact space onto its (Hausdorff) image is automatically a homeomorphism. Thus $F$ embeds $M$ into $\mathbb{R}^{k(n+1)}$. (Whitney's harder theorem then pushes $N$ down to $2n$ by generic projections.) $\;\blacksquare$

<a id="s3"></a>
### Regular values, Sard's theorem, and manifolds as level sets

The single most useful way to *produce* manifolds: take a smooth function and look at a level set $f^{-1}(c)$. When is it a manifold? The answer is "almost always," made precise by regular values and Sard's theorem.

> **Definition — critical/regular point and value.**
> Let $f:M\to N$ be smooth. A point $p\in M$ is a **critical point** if $df_p$ fails to be surjective; otherwise it is a **regular point**. A value $c\in N$ is a **critical value** if some point of $f^{-1}(c)$ is critical; it is a **regular value** if *every* point of $f^{-1}(c)$ is regular (vacuously true if $f^{-1}(c)$ is empty).

> **Theorem (regular value / preimage theorem).** If $c$ is a regular value of $f:M^m\to N^n$, then $f^{-1}(c)$ is a smooth embedded submanifold of $M$ of dimension $m-n$, and for $p\in f^{-1}(c)$ its tangent space is $T_p f^{-1}(c)=\ker(df_p)$.

**Demonstration.**

1. Fix $p\in f^{-1}(c)$. Since $c$ is regular, $df_p:T_pM\to T_{c}N$ is surjective, i.e. $f$ is a submersion at $p$. *(definition of regular value)*
2. By the submersion normal form (§s2) choose charts in which $f$ is the standard projection $\pi(x^1,\dots,x^m)=(x^1,\dots,x^n)$ and $c=0$. *(local normal form for submersions)*
3. In these coordinates $f^{-1}(c)=\{x^1=\dots=x^n=0\}$, the coordinate slice $\{0\}\times\mathbb{R}^{m-n}$, which is exactly the chart picture of an $(m-n)$-dimensional submanifold. The coordinates $(x^{n+1},\dots,x^m)$ restrict to a chart for $f^{-1}(c)$ near $p$. *(slice is a coordinate subspace)*
4. The tangent space of the slice is $\{v:dx^1(v)=\dots=dx^n(v)=0\}=\ker(d\pi)=\ker(df_p)$. Doing this at every $p\in f^{-1}(c)$ gives an atlas; transition maps are restrictions of $M$'s, hence smooth. So $f^{-1}(c)$ is a smooth $(m-n)$-manifold with the stated tangent space. $\;\blacksquare$

**Worked example — the sphere as a level set.** Let $f:\mathbb{R}^{n+1}\to\mathbb{R}$, $f(x)=|x|^2=\sum (x^i)^2$. Then $df_x=2x^\top$, surjective onto $\mathbb{R}$ whenever $x\neq 0$. So every nonzero value, in particular $c=1$, is regular, and $S^n=f^{-1}(1)$ is a smooth $n$-manifold with $T_pS^n=\ker(df_p)=\{v:p\cdot v=0\}=p^\perp$ — the familiar "tangent plane perpendicular to the radius."

**Worked example — a matrix group as a level set.** Let $f:\mathrm{Mat}_{n}(\mathbb{R})\to \mathrm{Sym}_n(\mathbb{R})$ on square matrices be $f(A)=A^\top A$, landing in symmetric matrices. The orthogonal group is $O(n)=f^{-1}(I)$. To see $I$ is a regular value, compute the differential at $A\in O(n)$: for a curve $A+tB$,
$$
df_A(B)=\frac{d}{dt}\Big|_{0}(A+tB)^\top(A+tB)=A^\top B+B^\top A.
$$
Given any symmetric target $S$, choose $B=\tfrac12 A S$; then $A^\top B+B^\top A=\tfrac12 S+\tfrac12 S=S$ (using $A^\top A=I$), so $df_A$ is surjective. Hence $O(n)$ is a smooth manifold of dimension $n^2-\binom{n+1}{2}=\binom{n}{2}$, with tangent space at $I$ the **antisymmetric** matrices ($\ker df_I=\{B:B^\top+B=0\}$) — the Lie algebra $\mathfrak{so}(n)$. The preimage theorem turns "the solutions of $A^\top A=I$" into a manifold without ever finding a chart by hand.

Now, how special is a regular value? Sard's theorem says critical values are negligible.

> **Theorem (Sard).** For a smooth map $f:M\to N$, the set of critical values has **measure zero** in $N$ (it can be covered by sets of arbitrarily small total volume). Consequently the regular values are **dense**, and by Baire's theorem a *generic* value is regular.

We prove the cleanest instructive case, which already contains the idea.

**Demonstration — Sard when $\dim M<\dim N$ (the image is negligible).**

1. Suppose $m=\dim M<\dim N=n$. Cover $M$ by countably many chart cubes; it suffices to show each $f(\text{cube})$ has measure zero in $\mathbb{R}^n$, since a countable union of null sets is null. *(measure zero is preserved under countable unions)*
2. On a cube $Q\subseteq\mathbb{R}^m$, $f$ is $C^1$, hence **Lipschitz**: $|f(x)-f(y)|\le L|x-y|$ for some constant $L$ (the derivative is bounded on the compact cube). *(continuous derivative on compact set is bounded; mean value inequality)*
3. Subdivide $Q$ into $k^m$ subcubes of side $s/k$ (where $s$ is the side of $Q$). Each subcube has diameter $\le \sqrt m\,s/k$, so its image lies in a ball of radius $L\sqrt m\,s/k$, of volume $C/k^n$. The total volume of all image balls is $\le k^m\cdot C/k^n = C\,k^{\,m-n}$. *(Lipschitz bound + counting subcubes)*
4. Since $m<n$, $k^{m-n}\to 0$ as $k\to\infty$. So $f(Q)$ has arbitrarily small total cover volume, i.e. measure zero. Hence $f(M)$, the countable union, has measure zero — *every* point of $N$ off this null set is (vacuously) a regular value. $\;\blacksquare$

The general case ($m\ge n$) stratifies $M$ by the order of vanishing of derivatives and runs the same volume-counting on each stratum; the punchline is identical. The power of Sard is that we may always *perturb* a target value to a regular one, losing nothing measurable — the technical engine behind degree theory (§s5) and transversality (§s4).

> **Pitfall.** Sard concerns critical *values* (in the target), not critical *points* (in the source); a map may have a huge critical set yet still satisfy Sard, because many critical points can map to the same critical value. Example: a constant map has all points critical but only one critical value.

**Worked example — finding a regular value by hand.** Let $f:\mathbb{R}^2\to\mathbb{R}$, $f(x,y)=x^2-y^2$. The differential $df=(2x,-2y)$ vanishes only at the origin, so the *only* critical point is $(0,0)$ and the only critical value is $f(0,0)=0$. Every $c\neq0$ is therefore regular, and $f^{-1}(c)$ is a smooth $1$-manifold — a pair of hyperbola branches. The exceptional level $f^{-1}(0)$ is the crossed pair of lines $y=\pm x$, which is *not* a manifold at the origin (it looks like an "X"). This is Sard in miniature: the bad level is a single value, measure zero in $\mathbb{R}$, and every nearby value gives an honest manifold.

<a id="s4"></a>
### Transversality and its genericity

The preimage theorem (§s3) handled $f^{-1}(c)$ for a point $c$. Transversality is the same idea for the preimage of a *submanifold*, and for intersections of submanifolds. It is the language of "two things meet as cleanly as their dimensions allow."

> **Definition — transversality.**
> A smooth map $f:M\to N$ is **transversal** to a submanifold $Z\subseteq N$, written $f\pitchfork Z$, if at every $p$ with $f(p)\in Z$ the images and tangent of $Z$ together fill the target:
> $$df_p(T_pM)+T_{f(p)}Z=T_{f(p)}N.$$
> Two submanifolds $X,Z\subseteq N$ are **transversal** ($X\pitchfork Z$) if at every $q\in X\cap Z$, $T_qX+T_qZ=T_qN$. (The sum need not be direct; only its *span* must be everything.)

In words: the directions you can reach moving in $X$ plus the directions inside $Z$ cover all directions of the ambient space — there is no "shared blind spot." This is exactly the condition that makes the intersection a manifold.

> **Theorem (transversal preimage / intersection).** If $f\pitchfork Z$ then $f^{-1}(Z)$ is a submanifold of $M$ with **codimension** equal to the codimension of $Z$ in $N$ (codimension $=$ ambient dim $-$ submanifold dim), i.e. $\dim f^{-1}(Z)=\dim M-(\dim N-\dim Z)$. If $X\pitchfork Z$ in $N$ then $X\cap Z$ is a submanifold with $\dim(X\cap Z)=\dim X+\dim Z-\dim N$.

**Demonstration (preimage version).**

1. Near a point $c\in Z$, write $Z$ locally as a regular level set: there is a submersion $g:V\to\mathbb{R}^{k}$ on a neighborhood $V$ of $c$ in $N$ with $Z\cap V=g^{-1}(0)$, where $k=\operatorname{codim}Z$. *(a submanifold is locally a regular level set, by §s3 normal form)*
2. Consider $g\circ f$ near $p\in f^{-1}(Z)$. Its differential is $dg_{f(p)}\circ df_p$. The transversality condition $df_p(T_pM)+T_{f(p)}Z=T_{f(p)}N$ together with $T_{f(p)}Z=\ker dg_{f(p)}$ implies $dg_{f(p)}\big(df_p(T_pM)\big)=dg_{f(p)}(T_{f(p)}N)=\mathbb{R}^k$. So $d(g\circ f)_p$ is surjective. *(applying $dg$ to both summands; $dg$ kills $T_pZ$ and is onto)*
3. Hence $0$ is a regular value of $g\circ f$, and $f^{-1}(Z)=(g\circ f)^{-1}(0)$ locally is a submanifold of codimension $k$ by the preimage theorem (§s3). Patching over $Z$ gives the global statement. $\;\blacksquare$

**Worked example — dimension count.** In $N=\mathbb{R}^3$ ($\dim 3$), two surfaces $X,Z$ ($\dim 2$ each) meeting transversally intersect in a manifold of dimension $2+2-3=1$, a curve — exactly what two generic surfaces in space do. If instead they were tangent (sharing a tangent plane at a touching point), $T_qX+T_qZ$ would be only the common plane, $2<3$: *not* transversal, and the intersection can be a single bad point, not a clean curve.

> **Theorem (Thom transversality / genericity).** Transversality is **generic and stable**: given any $f:M\to N$ and submanifold $Z\subseteq N$, an arbitrarily small smooth perturbation of $f$ is transversal to $Z$; and if $M$ is compact, the maps transversal to $Z$ form an *open dense* set in the space of smooth maps.

The proof embeds the perturbations in a family and applies Sard's theorem (§s3) to a parametrized map — the critical values are negligible, so a generic parameter gives transversality. The moral: **transversality may always be assumed after an inoffensive wiggle.** This justifies "count intersections, count zeros" arguments throughout differential topology, because the count is taken in the clean, transversal, generic situation and then shown to be deformation-invariant.

**Demonstration sketch — why the parametric trick works.** The clever idea (the *parametric transversality theorem*) is worth stating precisely because it recurs.

1. Embed $f$ in a *family* $F:M\times S\to N$ depending on a parameter $s$ in some manifold $S$, arranged so that the whole family $F$ is transversal to $Z$ (often $S=\mathbb{R}^k$ and $F(p,s)=f(p)+s$, sliding the map by every vector). *(construct a manifestly transversal family)*
2. Then $W=F^{-1}(Z)$ is a manifold (transversal preimage theorem). Consider the projection $\pi:W\to S$. By Sard (§s3), the regular values of $\pi$ are dense in $S$. *(Sard applied to $\pi$)*
3. The key lemma: $s$ is a regular value of $\pi$ **iff** the individual map $f_s=F(\cdot,s)$ is transversal to $Z$. So a dense set of parameters $s$ gives a transversal $f_s$, each arbitrarily close to the original. *(unwinding the definitions of regular value and transversality)*

Concretely, for $f:M\to\mathbb{R}^n$ and any submanifold $Z$, the perturbed maps $f(p)+s$ are transversal to $Z$ for almost every constant vector $s$ — you literally just shift the map by a generic small amount, as in the displayed family
$$
F(p,s)=f(p)+s,\qquad s\in\mathbb{R}^n,
$$
and Sard does the rest.

## Part B · Counting with signs: degree and Euler characteristic

<a id="s5"></a>
### The degree of a smooth map

Let $f:M\to N$ be smooth between **closed** (compact, without boundary) manifolds of the *same* dimension $n$, with $N$ connected. At a regular value $c$ (which exists by Sard, §s3), $f^{-1}(c)$ is a $0$-manifold (§s3) inside the compact $M$, hence a *finite* set of points. The degree counts them — first ignoring orientation (mod 2), then with signs (the integer degree).

> **Definition — mod 2 degree.**
> For $f:M\to N$ as above and a regular value $c$, define
> $$\deg_2(f)=\#f^{-1}(c)\bmod 2\ \in\ \mathbb{Z}/2.$$

> **Theorem.** $\deg_2(f)$ is independent of the regular value $c$ and is a homotopy invariant (unchanged if $f$ is smoothly deformed). Hence it depends only on the homotopy class of $f$.

The key lemma is the *classification of compact $1$-manifolds with boundary*: every such is a finite disjoint union of circles and closed intervals; the intervals have exactly $2$ endpoints each, circles have none. So the boundary of a compact $1$-manifold always has an **even** number of points. This single fact drives the whole theory.

**Demonstration — $\deg_2$ is a homotopy invariant.**

1. Let $F:M\times[0,1]\to N$ be a smooth homotopy from $f_0$ to $f_1$, and let $c$ be a regular value of $F$ *and* of $f_0,f_1$ (exists by Sard applied to all three). Then $W=F^{-1}(c)$ is a compact $1$-manifold with boundary, by the preimage theorem for manifolds-with-boundary. *(Sard + preimage theorem)*
2. The boundary of $W$ lies in the boundary of $M\times[0,1]$, namely $M\times\{0\}\sqcup M\times\{1\}$, so $\partial W = f_0^{-1}(c)\times\{0\}\ \sqcup\ f_1^{-1}(c)\times\{1\}$. *(preimage of $c$ on each end is $f_i^{-1}(c)$)*
3. By the classification of compact $1$-manifolds, $\#\partial W$ is even. Therefore $\#f_0^{-1}(c)+\#f_1^{-1}(c)$ is even, i.e. $\#f_0^{-1}(c)\equiv \#f_1^{-1}(c)\pmod 2$. *(boundary of a compact $1$-manifold has even cardinality)*
4. A similar cobordism between two regular values $c,c'$ (join them by a path, pull back) shows independence of $c$. Hence $\deg_2(f)$ is well defined and homotopy invariant. $\;\blacksquare$

To get an *integer* (more information), orient everything and count with signs.

> **Definition — orientation and the integer degree.**
> An **orientation** of a manifold is a consistent choice of "positively oriented" ordered basis in each tangent space, varying continuously; equivalently a choice of nowhere-zero top-degree form. Let $M,N$ be closed, oriented, connected, $\dim M=\dim N=n$. At a regular value $c$, each $p\in f^{-1}(c)$ has $df_p:T_pM\to T_cN$ an isomorphism (equal dimensions, surjective); set the **local sign** $\operatorname{sign}(df_p)=+1$ if $df_p$ preserves orientation ($\det>0$ in oriented bases) and $-1$ if it reverses it. Define
> $$\deg(f)=\sum_{p\in f^{-1}(c)}\operatorname{sign}(df_p)\ \in\ \mathbb{Z}.$$

The same cobordism argument as above, now keeping track of orientations of the boundary $1$-manifold (the two endpoints of an interval carry *opposite* induced orientations), upgrades "even cardinality" to "signed count cancels," proving $\deg(f)$ is independent of $c$ and a homotopy invariant. In cohomology, $\deg(f)$ is the integer by which $f^*$ multiplies the fundamental cohomology class: $f^*[\omega]=\deg(f)\,[\omega']$ after normalizing $\int_N\omega'=1$, equivalently $\int_M f^*\omega=\deg(f)\int_N\omega$ (this is how we compute degrees by integration in §s7).

**Worked example — degree of $z\mapsto z^k$ on the circle.** Identify $S^1$ with unit complex numbers and let $f(z)=z^k$ for integer $k\ge 1$. A regular value, say $c=1$, has preimages the $k$-th roots of unity, $k$ points; at each, $f$ wraps in the same direction, so all signs are $+1$. Thus $\deg(f)=k$. For $k=-1$ ($z\mapsto \bar z=1/z$) the single sheet reverses orientation, $\deg=-1$. The degree literally counts winding.

**Worked example — the degree by integration.** The integral formula $\int_M f^*\omega=\deg(f)\int_N\omega$ lets us read the degree off an integral, never finding preimages. Take $f(z)=z^2$ on $S^1$ and the angle form $\omega=\tfrac{1}{2\pi}d\theta$, normalized so $\int_{S^1}\omega=1$. Writing $z=e^{i\theta}$, $f(z)=e^{2i\theta}$ has angle $2\theta$, so $f^*\omega=\tfrac{1}{2\pi}d(2\theta)=\tfrac{2}{2\pi}d\theta$, giving
$$
\deg(f)=\int_{S^1}f^*\omega=\frac{1}{2\pi}\int_0^{2\pi}2\,d\theta=2,
$$
matching the pointwise count. The two computations of degree — counting signed preimages and integrating a pulled-back form — must agree, which is the content of the cohomological description above.

**Application 1 — the Fundamental Theorem of Algebra.** Let $p(z)=z^n+a_{n-1}z^{n-1}+\dots+a_0$ with $n\ge 1$. Suppose $p$ had no root. Then $p:\mathbb{C}\to\mathbb{C}\setminus\{0\}$, and after compactifying to the sphere $S^2=\mathbb{C}\cup\{\infty\}$, $p$ extends to a smooth map $S^2\to S^2$. For large $|z|$, $p(z)\approx z^n$, which has degree $n$; the lower terms are a homotopy (scale $a_i\to t a_i$), so $\deg(p)=\deg(z^n)=n\ge 1$. But a map missing a value $0$ factors through $S^2\setminus\{0\}$, which is contractible, forcing $\deg(p)=0$. Contradiction $n\ge1$ vs $0$. So $p$ has a root. *(degree is a homotopy invariant and detects surjectivity)*

**Application 2 — the Hairy Ball Theorem.** *There is no nowhere-zero continuous tangent vector field on the even sphere $S^{2m}$.* Suppose $v(x)$ were a unit tangent field on $S^{2m}$ (normalize a nonzero one). Define $H(x,t)=\cos(\pi t)\,x+\sin(\pi t)\,v(x)$. Each $H(\cdot,t):S^{2m}\to S^{2m}$ is smooth (unit norm since $x\perp v(x)$), with $H(\cdot,0)=\operatorname{id}$ (degree $+1$) and $H(\cdot,1)=-\operatorname{id}$, the antipodal map. The antipodal map of $S^n$ has degree $(-1)^{n+1}$; for $n=2m$ that is $(-1)^{2m+1}=-1$. So a homotopy connects a map of degree $+1$ to one of degree $-1$, contradicting homotopy invariance of degree ($+1\neq-1$). Hence no such $v$ exists — "you cannot comb a hairy ball flat." (On *odd* spheres $S^{2m-1}$ a nonvanishing field exists, e.g. $v(x_1,x_2,\dots)=(-x_2,x_1,\dots)$, consistent with degree $+1=+1$.) $\;\blacksquare$

<a id="s6"></a>
### The Euler characteristic and Poincaré–Hopf

A vector field on $M$ is a smooth choice of tangent vector $X(p)\in T_pM$ at each $p$. The hairy-ball theorem said $S^2$ cannot carry a nonvanishing one. Poincaré–Hopf explains *why* and *how much*: the zeros, counted with a sign called the index, must add up to a topological invariant — the Euler characteristic.

> **Definition — index of an isolated zero.**
> Let $X$ be a vector field with an isolated zero at $p$ (so $X\neq 0$ on a small punctured neighborhood). In a chart, $X$ restricted to a small sphere $S^{n-1}_\varepsilon$ around $p$, normalized to $X/|X|$, defines a map $S^{n-1}_\varepsilon\to S^{n-1}$ (the **Gauss map of the field**). Its degree (§s5) is the **index** $\operatorname{ind}_p(X)\in\mathbb{Z}$. It measures how many times the field rotates around $p$.

Intuition in the plane ($n=2$): a *source* (arrows out) and a *sink* (arrows in) both have index $+1$; a *saddle* has index $-1$; a *center* (closed orbits) has index $+1$. Index is unchanged by perturbing $X$ near $p$, because degree is homotopy invariant (§s5).

**Worked example — indices of planar fields.** Identify the plane with $\mathbb{C}$ and consider $X(z)=z^m$ as a vector field (the vector at $z$ is the complex number $z^m$). On a small circle $z=\varepsilon e^{i\theta}$ the normalized field is $e^{im\theta}$, which winds $m$ times as $\theta$ runs once around, so
$$
\operatorname{ind}_0(z^m)=m.
$$
Thus $X(z)=z$ (identity, a source) has index $+1$; $X(z)=\bar z$ rewrites as a saddle and one checks index $-1$; $X(z)=z^2$ a "monkey saddle" of index $2$. Summing local windings is exactly what Poincaré–Hopf globalizes.

> **Theorem (Poincaré–Hopf).** For a vector field $X$ with only isolated zeros on a closed manifold $M$,
> $$\sum_{p:\,X(p)=0}\operatorname{ind}_p(X)\ =\ \chi(M),$$
> the Euler characteristic — independent of the field $X$.

**Demonstration — the structure of the proof, with the surface case explicit.**

1. *The sum is independent of $X$.* Given two fields $X_0,X_1$ with isolated zeros, build a generic homotopy $X_t$ between them (transversality, §s4) as a section over $M\times[0,1]$; its zero set is a compact $1$-manifold whose boundary is the (signed) zero sets of $X_0$ and $X_1$. The signed boundary count of a compact oriented $1$-manifold is $0$ (each interval contributes $+1$ and $-1$ at its ends), so $\sum\operatorname{ind}(X_0)=\sum\operatorname{ind}(X_1)$. *(cobordism/boundary argument as in §s5, now for sections)*
2. *The common value is $\chi(M)$.* Pick one convenient field built from a triangulation (or a Morse function, see below) whose index sum is visibly $\chi$. For a triangulation, place a source at each vertex (index $+1$), a saddle at the midpoint of each edge (index $-1$), and a source at the center of each face (index $+1$ in dimension $2$). The total is $V-E+F$, which is $\chi(M)$ by the algebraic-topology definition $\chi=\sum(-1)^k(\#k\text{-cells})$. By Step 1 every field gives this same sum. $\;\blacksquare$

> **Definition — Morse function and its link to $\chi$.**
> A **Morse function** $f:M\to\mathbb{R}$ is a smooth function whose critical points (where $df=0$) are all **nondegenerate** (the Hessian matrix of second derivatives is invertible there). The **index** of a nondegenerate critical point is the number of negative eigenvalues of the Hessian (the count of "downhill" directions). The gradient field $\nabla f$ has a zero exactly at each critical point, with vector-field index $(-1)^{\text{Morse index}}$, so Poincaré–Hopf gives
> $$\chi(M)=\sum_{\text{crit }p}(-1)^{\operatorname{ind}_M(p)}.$$

**Worked example — the torus.** On the standing torus $T^2$, height gives a Morse function with four critical points: a bottom minimum (index $0$, sign $+$), two saddles on the inner ring (index $1$, sign $-$ each), a top maximum (index $2$, sign $+$). Sum of signs: $1-1-1+1=0$, so $\chi(T^2)=0$ — consistent with the torus admitting a nonvanishing vector field (it does: the constant "around the tube" field). For the sphere $S^2$, height gives one min and one max, sum $1+1=2=\chi(S^2)$, and the hairy-ball obstruction is exactly that $\chi(S^2)=2\neq0$. The two parts of this guide just shook hands.

## Part C · Cohomology, bundles, and characteristic classes

<a id="s7"></a>
### de Rham cohomology revisited and Poincaré duality

From the Differential Geometry guide: a **differential $k$-form** $\omega$ is a smooth, antisymmetric multilinear gadget eating $k$ tangent vectors; the **exterior derivative** $d$ raises degree by one with $d^2=0$; a form is **closed** if $d\omega=0$ and **exact** if $\omega=d\eta$. Since exact $\Rightarrow$ closed ($d^2=0$), we may take the quotient.

> **Definition — de Rham cohomology.**
> The **$k$-th de Rham cohomology** of $M$ is
> $$H^k_{\mathrm{dR}}(M)=\frac{\{\text{closed }k\text{-forms}\}}{\{\text{exact }k\text{-forms}\}}=\frac{\ker(d:\Omega^k\to\Omega^{k+1})}{\operatorname{im}(d:\Omega^{k-1}\to\Omega^k)}.$$
> A class $[\omega]$ records "closed modulo exact."

> **Theorem (de Rham).** For a smooth manifold, $H^k_{\mathrm{dR}}(M)\cong H^k(M;\mathbb{R})$, the real singular cohomology of the Algebraic Topology guide. Analysis (forms) computes topology (cohomology), and the isomorphism is given by integrating forms over cycles: $[\omega]\mapsto\big(c\mapsto\int_c\omega\big)$, well defined by **Stokes' theorem** $\int_c d\eta=\int_{\partial c}\eta$.

So Betti numbers $b_k=\dim H^k_{\mathrm{dR}}$ are computable with calculus, and $\chi(M)=\sum(-1)^k b_k$ once more (§s6).

> **Theorem (Poincaré duality).** For a closed *oriented* $n$-manifold $M$, the wedge-then-integrate pairing
> $$H^k_{\mathrm{dR}}(M)\times H^{n-k}_{\mathrm{dR}}(M)\to\mathbb{R},\qquad ([\alpha],[\beta])\mapsto\int_M\alpha\wedge\beta,$$
> is **nondegenerate** (no nonzero class pairs to zero with everything). Hence $H^k_{\mathrm{dR}}(M)\cong H^{n-k}_{\mathrm{dR}}(M)$ and $b_k=b_{n-k}$.

**Demonstration — the pairing is well defined and orientation is the crux.**

1. If $\alpha,\beta$ are closed then $d(\alpha\wedge\beta)=d\alpha\wedge\beta\pm\alpha\wedge d\beta=0$, so $\alpha\wedge\beta$ is a closed $n$-form. *(Leibniz rule for $d$; both factors closed)*
2. Changing $\alpha$ by an exact form $d\gamma$ changes the integrand by $d\gamma\wedge\beta=d(\gamma\wedge\beta)$ (since $d\beta=0$), and $\int_M d(\gamma\wedge\beta)=\int_{\partial M}\gamma\wedge\beta=0$ because $M$ is closed ($\partial M=\varnothing$). So the integral depends only on the classes. *(Stokes' theorem; $M$ has no boundary)*
3. An *orientation* is precisely what makes $\int_M$ of a top form well defined with a consistent sign (it picks the volume form's sign in each chart); without it the integral is defined only up to sign and the pairing degenerates. Nondegeneracy is the deep part (Hodge theory or a Mayer–Vietoris induction), but the *well-definedness* above is the analytic heart. *(definition of integration of forms requires orientation)* $\;\blacksquare$

**Worked example.** On the closed oriented surface $\Sigma_g$ of genus $g$: $b_0=1$, $b_1=2g$, $b_2=1$. Poincaré duality predicts $b_0=b_2$ ($1=1$ ✓) and pairs $H^1$ with itself via the nondegenerate, skew **intersection form** of rank $2g$: each handle's two loops $a_i,b_i$ cross once. Then $\chi(\Sigma_g)=1-2g+1=2-2g$, matching the count of §s6 for $g=1$ ($\chi=0$).

**Worked example — de Rham cohomology of the circle by hand.** On $S^1$, a $0$-form is a function $f(\theta)$ and a $1$-form is $g(\theta)\,d\theta$ with $f,g$ periodic. Closed $0$-forms are constants ($df=f'\,d\theta=0\Rightarrow f$ constant), and there are no exact $0$-forms below degree $0$, so
$$
H^0_{\mathrm{dR}}(S^1)=\mathbb{R}.
$$
Every $1$-form is closed (it is already top degree, $d$ of it lands in $\Omega^2=0$). A $1$-form $g\,d\theta$ is exact iff $g=f'$ for a *periodic* $f$, which requires $\int_0^{2\pi}g\,d\theta=0$ (the average of a derivative of a periodic function is zero). So the obstruction to exactness is the single number $\int_0^{2\pi}g\,d\theta$, and
$$
H^1_{\mathrm{dR}}(S^1)=\mathbb{R},\quad\text{generated by }[d\theta].
$$
This recovers $b_0=b_1=1$ for $S^1$ purely by integrating, and Poincaré duality $b_0=b_1$ holds ($1=1$) for this oriented $1$-manifold.

<a id="s8"></a>
### Vector bundles and characteristic classes (axiomatic)

> **Definition — vector bundle.**
> A **real vector bundle of rank $r$** over $M$ is a smooth manifold $E$ with a smooth surjection $\pi:E\to M$ such that each **fiber** $E_p=\pi^{-1}(p)$ is an $r$-dimensional real vector space, and $E$ is **locally trivial**: every $p$ has a neighborhood $U$ with a diffeomorphism $\pi^{-1}(U)\cong U\times\mathbb{R}^r$ that is linear on fibers and commutes with projection to $U$. A **complex vector bundle** uses $\mathbb{C}^r$ fibers. A **section** is a smooth map $s:M\to E$ with $\pi\circ s=\operatorname{id}$ (a choice of vector in each fiber). The **trivial bundle** is $M\times\mathbb{R}^r$. The **tangent bundle** $TM=\bigsqcup_p T_pM$ is the prototype.

A bundle is *trivial* if globally $E\cong M\times\mathbb{R}^r$. Most are not — the Möbius band is a nontrivial rank-$1$ bundle over $S^1$. **Characteristic classes** are cohomology classes that detect this nontriviality: they vanish for trivial bundles, so a nonzero class proves nontriviality. They are *natural*: pulling a bundle back along a map pulls the class back the same way.

> **Definition / Theorem (Stiefel–Whitney classes, axiomatic).** To each real vector bundle $E\to M$ there is assigned a total class $w(E)=1+w_1(E)+w_2(E)+\dots$ with $w_i(E)\in H^i(M;\mathbb{Z}/2)$ satisfying:
> 1. **Naturality:** $w(f^*E)=f^*w(E)$ for smooth $f$.
> 2. **Whitney sum:** $w(E\oplus F)=w(E)\smile w(F)$ (cup product).
> 3. **Normalization:** for the tautological line bundle $\gamma^1$ over $\mathbb{RP}^1$, $w_1(\gamma^1)\neq 0$.
> 4. **Rank bound:** $w_i(E)=0$ for $i>\operatorname{rank}E$.
> These axioms determine the $w_i$ uniquely.

> **Definition / Theorem (Chern classes, axiomatic).** To each *complex* vector bundle $E\to M$ there is assigned $c(E)=1+c_1(E)+c_2(E)+\dots$ with $c_i(E)\in H^{2i}(M;\mathbb{Z})$ (integer coefficients, even degree!) satisfying the same naturality, Whitney-sum $c(E\oplus F)=c(E)\smile c(F)$, normalization on the tautological line bundle over $\mathbb{CP}^1$, and $c_i=0$ for $i>\operatorname{rank}_{\mathbb C}E$.

> **Definition (Pontryagin classes).** For a real bundle $E$, complexify ($E\otimes\mathbb{C}$) and set $p_i(E)=(-1)^i c_{2i}(E\otimes\mathbb{C})\in H^{4i}(M;\mathbb{Z})$. (Odd Chern classes of a complexification are $2$-torsion, hence dropped.)

**Why these matter — the obstruction principle.**

1. A trivial bundle $M\times\mathbb{R}^r$ is the pullback of the bundle over a point along the constant map; by naturality its characteristic classes are pulled back from $H^{>0}(\text{point})=0$, hence all higher classes vanish. *(naturality + cohomology of a point)*
2. Contrapositive: if some $w_i(E)\neq 0$ (or $c_i$, $p_i$), then $E$ is **not** trivial. The class is a computable *obstruction*. *(logical contrapositive)*

**Demonstration — how the axioms actually compute a class (the splitting principle).** The four axioms look like a wish list; here is how they pin down a number in practice.

1. *Reduce to line bundles.* The **splitting principle** says: for any bundle $E$ there is a map $f:M'\to M$ such that $f^*$ is injective on cohomology *and* $f^*E$ splits as a sum of line bundles $L_1\oplus\dots\oplus L_r$. So it suffices to know classes of line bundles, then use the Whitney-sum axiom. *(splitting principle, provable by iterating projectivizations)*
2. *Name the line generators.* Write $x_i=c_1(L_i)$ (for complex) — the **Chern roots**. Then by the Whitney-sum axiom,
$$
c(E)=\prod_{i=1}^{r}(1+x_i)=1+\Big(\sum_i x_i\Big)+\Big(\sum_{i<j}x_i x_j\Big)+\dots,
$$
so $c_k(E)$ is the $k$-th **elementary symmetric polynomial** in the Chern roots. *(Whitney sum + definition of $c_1$ of a line bundle)*
3. *Symmetry makes it well defined.* Although the individual $x_i$ live only upstairs on $M'$, every $c_k$ is symmetric in them, hence (by the fundamental theorem of symmetric polynomials) a polynomial in the genuine classes downstairs — so $c_k(E)\in H^{2k}(M)$ is unambiguous. *(symmetric functions descend along the injection $f^*$)*

This is the computational engine: every characteristic-class identity (e.g. $c_1(L\otimes L')=c_1(L)+c_1(L')$, or the relation between Chern and Pontryagin classes) becomes an identity among symmetric polynomials in the Chern roots.

**Worked example — the Möbius bundle.** Let $L\to S^1$ be the Möbius line bundle (glue $[0,1]\times\mathbb{R}$ by $(0,t)\sim(1,-t)$). A generic section must change sign as it goes around, so by the intermediate value theorem it has a zero — there is no nowhere-zero section, unlike the trivial bundle (which has the constant section $1$). This nontriviality is recorded by $w_1(L)\neq 0$ in $H^1(S^1;\mathbb{Z}/2)=\mathbb{Z}/2$, the unique nonzero class. The Whitney sum axiom then gives a clean computation: $L\oplus L$ has $w=(1+w_1)^2=1+2w_1+w_1^2=1$ over $\mathbb{Z}/2$ (since $2w_1=0$ and $w_1^2\in H^2(S^1)=0$), consistent with $L\oplus L$ being trivial.

> **Pitfall.** Characteristic classes are *obstructions*, so vanishing classes do **not** guarantee triviality (there are nontrivial bundles with all classes zero). They are necessary, not sufficient, witnesses — but in low dimensions and for line bundles they are complete invariants.

**Worked example — orientability detected by $w_1$.** The first Stiefel–Whitney class $w_1(TM)\in H^1(M;\mathbb{Z}/2)$ vanishes **iff** $M$ is orientable. Intuition: $w_1$ records whether a chosen orientation flips as you transport it around loops, and an orientation exists precisely when no loop flips it. For the Möbius band's core circle the tangent-plus-normal data flips once around, so $w_1\neq0$ and the band is nonorientable; for the cylinder it does not, $w_1=0$, orientable. This is the cleanest example of "a single cohomology class answers a yes/no topological question."

**Worked example — Chern number of the tautological bundle on $\mathbb{CP}^1$.** Over $\mathbb{CP}^1=S^2$ the **tautological line bundle** $\gamma$ assigns to each point (a complex line $\ell\subset\mathbb{C}^2$) the line $\ell$ itself as fiber. Its first Chern class satisfies
$$
\int_{\mathbb{CP}^1} c_1(\gamma) = -1,
$$
the generator of $H^2(\mathbb{CP}^1;\mathbb{Z})=\mathbb{Z}$. The dual (hyperplane) bundle has $\int c_1=+1$. These integers, the **Chern numbers**, classify all complex line bundles over $S^2$ completely: line bundles on $S^2$ are in bijection with $\mathbb{Z}$ via $\int_{S^2}c_1$. We rederive this very number from curvature in §s10.

<a id="s9"></a>
### The Euler class and the Euler characteristic

The **Euler class** is the characteristic class tied most directly to the counting of §s6. It lives on *oriented* real bundles of even rank and measures the obstruction to a nonvanishing section.

> **Definition — Euler class.**
> For an oriented real vector bundle $E\to M$ of rank $r$, the **Euler class** $e(E)\in H^r(M;\mathbb{Z})$ is the obstruction to a nowhere-zero section: take a generic section $s$ (transversal to the zero section, §s4); its zero set $Z=s^{-1}(0)$ is a submanifold of codimension $r$ (preimage theorem, §s3), and $e(E)$ is the cohomology class **Poincaré dual** to $[Z]$ — the class that integrates to the signed count of zeros over any complementary cycle.

> **Theorem (Euler class of the tangent bundle).** For a closed oriented $n$-manifold $M$,
> $$\int_M e(TM)=\chi(M).$$

**Demonstration — why this equals the Euler characteristic.**

1. A section of the tangent bundle $TM$ is exactly a vector field $X$ on $M$ (a tangent vector at each point). *(definition of $TM$, §s8)*
2. The zero set of a generic such section is the zero set of a generic vector field; its Poincaré-dual class integrated over $M$ is the **signed count of zeros** of $X$, with the local sign being precisely the vector-field index $\operatorname{ind}_p(X)$ of §s6. *(transversal zeros are isolated and signed by the local degree)*
3. So $\int_M e(TM)=\sum_p\operatorname{ind}_p(X)$. By Poincaré–Hopf (§s6) this sum is $\chi(M)$. Therefore $\int_M e(TM)=\chi(M)$. $\;\blacksquare$

**Relations to the other classes.** For a complex line bundle (rank-$2$ real, oriented), $e=c_1$, the first Chern class — the Euler class *is* a Chern class in this case. For a rank-$r$ oriented real bundle, $e(E)^2=p_{\,r/2}(E)$ (top Pontryagin class) when $r$ is even. And the top Stiefel–Whitney class is the mod-$2$ reduction $w_r(E)=e(E)\bmod 2$, which is why $\chi(M)\bmod 2$ obstructs nonvanishing fields even without orientation.

**Worked example — the sphere.** $TS^2$ is oriented of rank $2$, so $\int_{S^2}e(TS^2)=\chi(S^2)=2\neq0$: the Euler class is nonzero, $TS^2$ has no nowhere-zero section, recovering the hairy-ball theorem (§s5) as a statement about a single characteristic number. For $T^2$, $\int_{T^2}e=\chi(T^2)=0$, and indeed the torus has a nonvanishing field.

**Worked example — counting zeros via the Euler number.** Suppose someone builds a vector field on $S^2$ with exactly three zeros, two sources and one zero of some unknown index $k$. The Euler-class identity forces the signed total:
$$
\sum_p\operatorname{ind}_p(X)=\int_{S^2}e(TS^2)=\chi(S^2)=2 \;\Longrightarrow\; 1+1+k=2 \;\Longrightarrow\; k=0.
$$
So such a third zero would have to be *degenerate* (a perturbation splits it into zeros whose indices cancel). The Euler number constrains what zero configurations are even possible — topology disciplines analysis.

<a id="s10"></a>
### Chern–Weil theory — characteristic classes from curvature

So far characteristic classes were defined by axioms or by counting zeros. Chern–Weil builds them *analytically*, out of the **curvature** of a connection — making "characteristic class" an integral of a geometric quantity, the third leg of the unity in §s0.

> **Definition — connection and curvature (recalled from Differential Geometry).**
> A **connection** $\nabla$ on a vector bundle $E$ is a rule for differentiating sections along directions, producing a **connection $1$-form** (matrix of $1$-forms) $A$ in a local frame. Its **curvature** is the matrix of $2$-forms
> $$\Omega=dA+A\wedge A,$$
> measuring the failure of "parallel transport around small loops" to return vectors unchanged. Every bundle admits a connection (build local ones, glue with a partition of unity, §s1).

> **Theorem (Chern–Weil).** Let $P$ be an invariant polynomial on matrices (one with $P(g X g^{-1})=P(X)$ for invertible $g$ — e.g. trace, determinant, or coefficients of $\det(I+\tfrac{t}{2\pi i}X)$). Then the form $P(\Omega)$ built by substituting the curvature is **closed**, and its de Rham class is **independent of the connection**. Assigning these classes to bundles reproduces the Chern (and, via complexification, Pontryagin and Euler) classes axiomatically defined in §s8–s9. Concretely, for a complex bundle,
> $$c(E)=\Big[\det\Big(I+\tfrac{i}{2\pi}\Omega\Big)\Big],\qquad c_1(E)=\Big[\tfrac{i}{2\pi}\operatorname{tr}\Omega\Big].$$

**Demonstration — $P(\Omega)$ is closed and connection-independent.**

1. *Bianchi identity.* Differentiating $\Omega=dA+A\wedge A$ gives $d\Omega=dA\wedge A-A\wedge dA=\Omega\wedge A-A\wedge\Omega$, i.e. $d\Omega=[\Omega,A]$ in the bracket notation; covariantly, $d_\nabla\Omega=0$. *(apply $d$, use $d^2=0$ and the Leibniz rule)*
2. *Closedness.* For an invariant polynomial $P$, invariance implies an infinitesimal identity ($\sum \partial P/\partial X_{ij}\,[X,\cdot]=0$). Combined with the Bianchi identity, a direct computation gives $dP(\Omega)=0$: the candidate exact pieces cancel exactly because $P$ is invariant. So $P(\Omega)$ is a closed form and defines a de Rham class. *(invariance of $P$ + Bianchi)*
3. *Connection independence.* Given two connections $A_0,A_1$, set $A_t=A_0+t(A_1-A_0)$, $\alpha=A_1-A_0$ (a globally defined matrix of $1$-forms, since the difference of connections is tensorial). One computes
   $$\tfrac{d}{dt}P(\Omega_t)=d\big(\text{transgression form }TP(\alpha,\Omega_t)\big),$$
   an *exact* form. Integrating over $t\in[0,1]$, $P(\Omega_1)-P(\Omega_0)=d\big(\int_0^1 TP\,dt\big)$ is exact, so the classes agree. *(the difference is a total $d$, hence zero in cohomology)* $\;\blacksquare$

**Worked example — first Chern number of a line bundle on $S^2$.** Take the tautological line bundle on $\mathbb{CP}^1=S^2$ with its natural connection; the curvature integrates to $\int_{S^2}\tfrac{i}{2\pi}\Omega=-1$, an integer. This integer (a **Chern number**) is independent of connection by the theorem and equals the degree of the bundle's gluing map — the same integer that, in physics, is the **magnetic monopole charge** or the **first Chern number** of a Berry connection: curvature integrates to topology.

**Worked example — why the integral is quantized.** Cover $S^2$ by two caps, north $U_N$ and south $U_S$, on each of which the line bundle is trivial with its own connection $1$-form $A_N$, $A_S$; on the overlap (an equatorial annulus) they differ by a gauge transformation, $A_N-A_S=-i\,d\lambda$ for a phase $\lambda$. Then by Stokes,
$$
\int_{S^2}\frac{i}{2\pi}\Omega=\frac{i}{2\pi}\Big(\int_{U_N}dA_N+\int_{U_S}dA_S\Big)=\frac{i}{2\pi}\oint_{\text{eq}}(A_N-A_S)=\frac{1}{2\pi}\oint_{\text{eq}}d\lambda,
$$
which is $1/2\pi$ times the total phase change of $\lambda$ around the equator. Since the transition is single-valued, that phase change is an integer multiple of $2\pi$, so the integral is an **integer** — the topological quantization of magnetic charge (Dirac's argument), here derived as the integrality of $c_1$. Curvature is a smooth real thing; its integral is forced to be a whole number by the global gluing.

> **Pitfall.** $P(\Omega)$ has *real* coefficients, so Chern–Weil computes characteristic classes in $H^*(M;\mathbb{R})$ — it sees them up to torsion. Integer and $\mathbb{Z}/2$ refinements (the full Chern/Stiefel–Whitney classes) need the axiomatic/topological definitions of §s8.

<a id="s11"></a>
### Gauss–Bonnet and the Atiyah–Singer index theorem

We close where §s0 promised: an analytic integral equals a topological integer equals a geometric count.

> **Theorem (Gauss–Bonnet, surfaces).** For a closed oriented Riemannian surface $\Sigma$ with Gaussian curvature $K$ and area element $dA$,
> $$\frac{1}{2\pi}\int_\Sigma K\,dA\ =\ \chi(\Sigma).$$
> Here the **Gaussian curvature** $K$ is the geometric measure of intrinsic bending (positive on a sphere, zero on a flat torus, negative on a saddle), and $dA$ is the Riemannian area form.

This is the Chern–Weil identity for the tangent bundle of a surface: $\tfrac{1}{2\pi}K\,dA$ is precisely the Euler-class representative $e(T\Sigma)$ (§s9), so the integral is $\int_\Sigma e(T\Sigma)=\chi(\Sigma)$.

**Demonstration — assembling the three viewpoints.**

1. *Geometry $\to$ Euler class.* For an oriented Riemannian surface the Levi–Civita connection on $T\Sigma$ has curvature $2$-form whose Chern–Weil Euler representative is $\tfrac{1}{2\pi}K\,dA$. *(Chern–Weil, §s10, applied to the rank-$2$ oriented tangent bundle)*
2. *Euler class $\to$ topology.* By §s9, $\int_\Sigma e(T\Sigma)=\chi(\Sigma)$. *(Euler class integrates to the Euler characteristic)*
3. *Topology $\to$ counting.* By §s6, $\chi(\Sigma)=\sum_p\operatorname{ind}_p(X)$ for any vector field, the alternating cell count $V-E+F$. *(Poincaré–Hopf)*
4. Chaining: $\tfrac{1}{2\pi}\int_\Sigma K\,dA=\int_\Sigma e(T\Sigma)=\chi(\Sigma)=\sum\operatorname{ind}$. An analytic integral, a topological invariant, and a geometric count are one number. $\;\blacksquare$

**Worked example.** The unit sphere has $K=1$ everywhere and area $4\pi$, so $\tfrac{1}{2\pi}\int K\,dA=\tfrac{1}{2\pi}(4\pi)=2=\chi(S^2)$ ✓. The flat torus has $K\equiv 0$, giving $0=\chi(T^2)$ ✓. The genus-$g$ surface must average negative curvature for $g\ge 2$, since $\tfrac1{2\pi}\int K\,dA=2-2g<0$ — geometry is *forced* by topology.

**Worked example — geodesic triangles, the classical face of Gauss–Bonnet.** The local Gauss–Bonnet formula for a geodesic triangle $T$ (sides are shortest paths) with interior angles $\alpha,\beta,\gamma$ reads
$$
\int_T K\,dA = (\alpha+\beta+\gamma)-\pi.
$$
On the flat plane $K=0$, so the angles sum to exactly $\pi$ — ordinary Euclidean geometry. On the unit sphere $K=1$, so $\alpha+\beta+\gamma-\pi=\operatorname{Area}(T)>0$: spherical triangles have angle excess equal to their area (a triangle with three right angles covers an octant, area $\pi/2$, excess $3\cdot\tfrac\pi2-\pi=\tfrac\pi2$ ✓). On a saddle ($K<0$) triangles are angle-*deficient*. Summing this local statement over a triangulation, the interior angles assemble to $2\pi$ at each vertex and the boundary terms telescope, producing the global $\tfrac1{2\pi}\int_\Sigma K\,dA=\chi$ — which is how Gauss and Bonnet first found it, before bundles existed.

The vast generalization replaces "$\chi$ as alternating sum of cohomology" with "alternating sum of solution-space dimensions of a differential operator."

> **Theorem (Atiyah–Singer index theorem, statement).** Let $D$ be an **elliptic differential operator** on a closed manifold $M$ (elliptic: its highest-order part is invertible in every nonzero direction, the condition guaranteeing finite-dimensional kernel and cokernel). Its **analytic index** is
> $$\operatorname{ind}_a(D)=\dim\ker D-\dim\operatorname{coker}D,$$
> the net number of solutions. The theorem states this *analytic* integer equals a *topological* integer:
> $$\operatorname{ind}_a(D)=\int_M \operatorname{ch}(\sigma D)\,\operatorname{Td}(TM),$$
> a characteristic-class integral built from the symbol of $D$ (its Chern character $\operatorname{ch}$) and the manifold's tangent bundle (its Todd class $\operatorname{Td}$).

Gauss–Bonnet is the special case where $D$ is the de Rham operator $d+d^*$: its index is exactly the alternating sum of Betti numbers, namely $\chi(M)$, and the right-hand integral is $\int_M e(TM)$. Other choices of $D$ yield the Riemann–Roch theorem (holomorphic Euler characteristics), the signature theorem (Hirzebruch's $L$-genus), and the spin/Dirac index ($\hat A$-genus) — each an identity "number of solutions $=$ a characteristic number." In physics this is the engine behind anomaly cancellation and instanton counting. It is the mature form of the single idea of this guide: **local analytic data, integrated, computes a global topological invariant.**

> **Worked example — the index theorem reproduces Gauss–Bonnet, term by term.** Take $M$ a closed oriented surface and $D=d+d^\ast:\Omega^{\mathrm{even}}\to\Omega^{\mathrm{odd}}$ (the de Rham operator regrouped by parity). By **Hodge theory** the kernel of $D$ is the even harmonic forms and the cokernel is the odd harmonic forms, and harmonic forms represent cohomology, so
> $$
> \operatorname{ind}_a(D)=\big(b_0+b_2\big)-b_1=\sum_k(-1)^k b_k=\chi(M).
> $$
> The Atiyah–Singer right-hand side specializes for this $D$ to the Euler-class integral $\int_M e(TM)=\tfrac1{2\pi}\int_M K\,dA$. Equating the two sides is exactly Gauss–Bonnet. The index theorem thus *contains* the climax of this guide, and replaces "alternating sum of Betti numbers" with "net count of harmonic solutions" — analysis again equal to topology.

> **Worked example — a $4$-manifold signature.** For a closed oriented $4$-manifold $M$, choosing $D$ to be the signature operator gives Hirzebruch's identity
> $$
> \operatorname{sign}(M)=\frac{1}{3}\int_M p_1(TM),
> $$
> where $\operatorname{sign}(M)$ is the signature of the intersection form on $H^2(M)$ (a purely topological integer: $\#$positive $-$ $\#$negative eigenvalues) and $p_1$ is the first Pontryagin class (§s8). For $\mathbb{CP}^2$, $\operatorname{sign}=1$ and indeed $\tfrac13\int p_1=\tfrac13\cdot 3=1$ (here $\int_{\mathbb{CP}^2}p_1=3$ because the total Chern class $c(T\mathbb{CP}^2)=(1+h)^3$ gives $p_1=c_1^2-2c_2=9h^2-6h^2=3h^2$, and $\int_{\mathbb{CP}^2}h^2=1$). A signed eigenvalue count equals a curvature integral — the same miracle, one dimension up.

---

*A first course in differential topology — from smooth maps and Sard's theorem, through degree and Poincaré–Hopf, to characteristic classes, Chern–Weil theory, and the Atiyah–Singer summit. Read once for the architecture; return to any boxed definition or demonstration as a reference. Remember the through-line: the derivative linearizes, the special points are counted with signs, and that signed count — whether a degree, an Euler characteristic, an index, or a curvature integral — is the same global invariant, proving that analysis, topology, and geometry are three faces of one shape.*
