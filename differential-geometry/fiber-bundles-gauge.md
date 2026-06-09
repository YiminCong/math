**English** · [中文](fiber-bundles-gauge.zh.md)

# Fiber Bundles & Gauge Theory, *the geometry of forces.*

*A self-contained, rigorous introduction to the geometry behind the fundamental forces. We begin with the bare idea of a fiber bundle — a space that is "many copies of a fiber, glued over a base" — and build, step by step, to the machinery of modern physics: principal bundles, connections, curvature, holonomy, Yang–Mills theory, and the topological invariants that classify them. The recurring revelation is that a force field is a connection on a bundle, its field strength is curvature, and gauge invariance is the freedom to relabel fibers. Geometry is the goal; gauge theory is the motivation; every formula is derived and every symbol is explained.*

[← Back to all guides](../README.md)

**Prerequisites.** This guide assumes the **Differential Geometry & Tensors** guide (smooth manifolds and charts, tangent and cotangent spaces, vector fields, differential forms, the exterior derivative $d$ and wedge product $\wedge$, and connections/covariant derivatives). We restate each borrowed fact in one line where we use it. We also lean lightly on the **Group Theory** guide for matrix Lie groups and their Lie algebras; the needed facts are recalled inline.

## Part A · Bundles

<a id="s0"></a>
### Motivation — gauge fields as connections; why physics lives on bundles, not just spacetime

The deepest lesson of twentieth-century physics is that the fundamental forces — electromagnetism, the weak force, the strong force — are not extra "stuff" painted on top of spacetime. They are *geometry*: each force is a way of comparing internal states of a particle at different points, and that comparison is exactly what a geometer calls a **connection**.

#### What problem are we solving?

In the prerequisite guide, a connection let us compare *tangent vectors* at different points of a manifold $M$ (spacetime). But a charged particle carries more than a velocity. An electron has a quantum-mechanical phase; a quark carries a "color" label in a 3-dimensional internal space. These internal data live in a vector space attached to each point — a **fiber** — and to do physics we must compare fibers at different points. There is no canonical way to do so, just as there was no canonical way to compare tangent vectors on a curved surface. A *choice* of comparison is the **gauge field**.

Two facts drive the whole subject:

1. **Internal symmetry.** The physics is unchanged if we rotate the internal labels by an element of a symmetry group $G$ (for electromagnetism $G=U(1)$, the circle of phases; for the strong force $G=SU(3)$). This relabeling freedom is **gauge symmetry**.
2. **No global frame.** Often there is no single consistent way to label the internal states over all of spacetime at once — the labels must be stitched together patch by patch, and the stitching is where the topology (and sometimes the physics, as for the magnetic monopole) hides.

The mathematical object that packages "a fiber over every point, glued consistently, with a symmetry group acting on the fibers" is a **fiber bundle**. A connection on it is the gauge field; its curvature is the **field strength** (the electromagnetic field $F_{\mu\nu}$, the gluon field, …); and the action that governs its dynamics is **Yang–Mills**. The point of this guide is to make every word of that sentence precise.

#### The plan

We build, in order: **fiber bundles** (the spaces, s1), **vector bundles and sections** (s2), **principal bundles and structure groups** (s3), **connections** on a principal bundle (s4), the **local gauge potential** $A$ and how it transforms (s5), **curvature** and the field strength $F=dA+A\wedge A$ (s6), **parallel transport, holonomy, and Wilson loops** (s7), the **covariant derivative on matter fields** (s8), **Yang–Mills theory** with Maxwell as the abelian case (s9), **characteristic classes** (Chern classes, Chern–Simons) (s10), and finally **physical examples** — the Dirac monopole, the Aharonov–Bohm effect, and instantons (s11).

> **Intuition.** Keep one picture in mind throughout: a bundle is a "thick" manifold — over each point of the base sits a whole copy of a fiber. A connection is an *infinitesimal rule for how to slide between neighboring fibers*. Curvature measures the failure of that sliding to commute around a small loop. Everything else is bookkeeping that keeps these local rules globally consistent.

<a id="s1"></a>
### Fiber bundles — total space, base, fiber, projection, local trivializations

A fiber bundle is the precise notion of "a family of identical spaces, one over each point of a base, glued together so that locally it looks like a product but globally it may twist."

#### The definition

> **Definition — fiber bundle.**
>
> A **fiber bundle** is a tuple $(E,M,\pi,F)$ consisting of:
> - a smooth manifold $E$, the **total space**;
> - a smooth manifold $M$, the **base space**;
> - a smooth surjection $\pi:E\to M$, the **projection**;
> - a smooth manifold $F$, the **typical fiber**,
>
> such that $\pi$ is **locally trivial**: every point $x\in M$ has an open neighborhood $U\subseteq M$ and a diffeomorphism (a smooth map with smooth inverse)
> $$
> \phi_U:\ \pi^{-1}(U)\ \xrightarrow{\ \sim\ }\ U\times F
> $$
> such that $\mathrm{pr}_1\circ\phi_U=\pi$, where $\mathrm{pr}_1:U\times F\to U$ is projection onto the first factor. The pair $(U,\phi_U)$ is a **local trivialization**.

Unpacking this: $\pi^{-1}(\{x\})$ is the **fiber over $x$**, written $E_x$; the condition $\mathrm{pr}_1\circ\phi_U=\pi$ forces $\phi_U$ to carry the fiber $E_x$ diffeomorphically onto $\{x\}\times F$, so every fiber is a copy of $F$. "Locally trivial" means: zoom into a small patch $U$ of the base, and the part of $E$ above it is just the product $U\times F$ — boring and untwisted. The interesting content is *global*: how the local product pictures over overlapping patches are glued.

#### Transition functions

> **Definition — transition functions.**
>
> Let $(U_\alpha,\phi_\alpha)$ and $(U_\beta,\phi_\beta)$ be two local trivializations with $U_\alpha\cap U_\beta\ne\varnothing$. On the overlap, the composite
> $$
> \phi_\alpha\circ\phi_\beta^{-1}:\ (U_\alpha\cap U_\beta)\times F\ \to\ (U_\alpha\cap U_\beta)\times F
> $$
> preserves the base point (both sides project to the same $x$), so it has the form $(x,f)\mapsto\big(x,\ g_{\alpha\beta}(x)\cdot f\big)$ for a smooth map $g_{\alpha\beta}:U_\alpha\cap U_\beta\to \mathrm{Diff}(F)$ into transformations of the fiber. The $g_{\alpha\beta}$ are the **transition functions**.

The transition functions encode the gluing — the "twist." They satisfy two consistency conditions that follow directly from their definition:

1. **Identity on the diagonal:** $g_{\alpha\alpha}(x)=\mathrm{id}$, because $\phi_\alpha\circ\phi_\alpha^{-1}$ is the identity.
2. **Cocycle condition:** on triple overlaps $U_\alpha\cap U_\beta\cap U_\gamma$,
   $$
   g_{\alpha\beta}(x)\,g_{\beta\gamma}(x)=g_{\alpha\gamma}(x),
   $$
   because $(\phi_\alpha\phi_\beta^{-1})(\phi_\beta\phi_\gamma^{-1})=\phi_\alpha\phi_\gamma^{-1}$. Setting $\gamma=\alpha$ gives $g_{\alpha\beta}=g_{\beta\alpha}^{-1}$.

> **Intuition.** A bundle *is* its base, its fiber, and its transition functions, up to relabeling. Trivial bundles are those for which we can choose all $g_{\alpha\beta}=\mathrm{id}$ globally; nontrivial ones cannot.

#### Examples

**Example 1 — the trivial bundle (a cylinder).** Take base $M=S^1$ (a circle), fiber $F=[-1,1]$ (an interval), total space $E=S^1\times[-1,1]$, and $\pi$ the projection onto $S^1$. This is the **cylinder**. A single trivialization (the identity) works everywhere; no twisting. It is a *global product*.

**Example 2 — a nontrivial bundle (the Möbius band).** Take the same base $S^1$ and fiber $[-1,1]$, but glue with a flip. Cover $S^1$ by two arcs $U_1,U_2$ overlapping in two small intervals. On one overlap use $g_{12}(x)=\mathrm{id}$ (the map $f\mapsto f$); on the other use $g_{12}(x)=-\mathrm{id}$ (the flip $f\mapsto -f$). The resulting total space is the **Möbius band**. It is *locally* $U\times[-1,1]$ everywhere, yet *globally* it is not the cylinder: it has one edge, not two, and is non-orientable. This shows concretely that local triviality does not imply global triviality — the transition functions carry the topology.

> **Worked example — distinguishing them.** Travel once around the base of the Möbius band, following the trivialization. Because one overlap flips the fiber, a point at "height $+\tfrac12$" returns to height $-\tfrac12$. On the cylinder it returns to $+\tfrac12$. The monodromy (net fiber transformation after one loop) is $-\mathrm{id}\ne\mathrm{id}$, so the bundles are not isomorphic. The structure group here is reduced to $\{\pm 1\}=\mathbb{Z}_2$.

**Example 3 — the tangent bundle.** For a smooth $n$-manifold $M$, the **tangent bundle** $TM=\bigsqcup_{x\in M}T_xM$ (the disjoint union of all tangent spaces) is a fiber bundle with fiber $F=\mathbb{R}^n$ and projection $\pi$ sending a tangent vector at $x$ to $x$. A chart $(U,\varphi)$ with coordinates $x^i$ gives a trivialization $\pi^{-1}(U)\cong U\times\mathbb{R}^n$ via $v=v^i\partial_i\mapsto(x,(v^1,\dots,v^n))$. The transition functions are the **Jacobian matrices** of the coordinate changes: if $\tilde x=\tilde x(x)$, then $g_{\alpha\beta}(x)=\big(\partial\tilde x^i/\partial x^j\big)\in GL(n,\mathbb{R})$ (the group of invertible $n\times n$ matrices), exactly the transformation law $v$-components obey. For $M=S^2$ the tangent bundle is nontrivial — the "hairy ball theorem" says $S^2$ has no nowhere-zero continuous vector field, which a trivial bundle would supply.

<a id="s2"></a>
### Vector bundles; sections; the tangent and cotangent bundles revisited

The fibers of greatest physical interest are *vector spaces*: the internal state of a particle is a vector (a wavefunction component, a color vector). A bundle whose fibers are vector spaces, glued by linear maps, is a **vector bundle**.

#### Definition

> **Definition — vector bundle.**
>
> A **(real, rank-$k$) vector bundle** is a fiber bundle $\pi:E\to M$ whose typical fiber is $F=\mathbb{R}^k$, such that:
> - each fiber $E_x=\pi^{-1}(x)$ carries the structure of a $k$-dimensional real vector space, and
> - the local trivializations $\phi_U:\pi^{-1}(U)\to U\times\mathbb{R}^k$ restrict on each fiber to a **linear isomorphism** $E_x\to\{x\}\times\mathbb{R}^k$.
>
> Consequently the transition functions take values in the general linear group: $g_{\alpha\beta}:U_\alpha\cap U_\beta\to GL(k,\mathbb{R})$. (Complex vector bundles replace $\mathbb{R}$ by $\mathbb{C}$ and $GL(k,\mathbb{R})$ by $GL(k,\mathbb{C})$.)

The requirement that transitions be *linear* (not arbitrary diffeomorphisms of $\mathbb{R}^k$) is what makes "add two elements of a fiber" or "scale by a number" well-defined independent of trivialization.

#### Sections

> **Definition — section.**
>
> A **section** of a bundle $\pi:E\to M$ is a smooth map $s:M\to E$ with $\pi\circ s=\mathrm{id}_M$; that is, $s$ assigns to each base point $x$ an element $s(x)$ *of its own fiber* $E_x$. We write $\Gamma(E)$ for the set of (smooth) sections. A **local section** is defined only over an open $U\subseteq M$.

Physically, a section of a vector bundle *is a matter field*: it picks, at every spacetime point, a value of the internal vector (an electron's wavefunction, a color vector). The zero section $s(x)=0_{E_x}$ always exists for a vector bundle; a vector bundle is trivial if and only if it admits $k$ sections that are linearly independent at every point (a **global frame**), since those let us define a global trivialization by reading off components.

> **Pitfall.** A *nowhere-zero* section need not exist even for a line bundle (rank $1$): the Möbius band, viewed as a real line bundle over $S^1$, has no nowhere-zero section, because any section must cross zero after the orientation flip (intermediate value theorem). Sections are global objects and feel the topology.

#### The tangent and cotangent bundles, revisited

The tangent bundle $TM$ (s1) is a rank-$n$ real vector bundle; its sections are exactly **vector fields**, $\Gamma(TM)=\mathfrak{X}(M)$. The dual construction gives the **cotangent bundle** $T^*M=\bigsqcup_x T_x^*M$, whose fiber $T_x^*M$ is the dual vector space of linear functionals on $T_xM$. Its sections are **1-forms** (covector fields), $\Gamma(T^*M)=\Omega^1(M)$. Under a coordinate change $\tilde x(x)$:

- tangent components transform by the Jacobian $J=(\partial\tilde x^i/\partial x^j)$: $\tilde v^i=J^i{}_j v^j$;
- cotangent components transform by the *inverse-transpose* $(J^{-1})^T$: $\tilde\omega_i=(J^{-1})^j{}_i\,\omega_j$,

so that the pairing $\omega_i v^i$ is invariant. More generally, tensor bundles $T^{(p,q)}M$ have fibers built from tensor products of $TM$ and $T^*M$, and their sections are the $(p,q)$-tensor fields of the prerequisite guide. Differential $p$-forms are sections of $\Lambda^p T^*M$, the bundle of alternating $p$-covectors.

> **Worked example — a rank-2 bundle on $S^2$.** The tangent bundle $TS^2$ has fiber $\mathbb{R}^2$. Cover $S^2$ by two stereographic charts (north and south, as in the prerequisite guide). On the overlap (the sphere minus its poles, an annulus) the transition function is the Jacobian of the coordinate change $(u,v)\mapsto(u,v)/(u^2+v^2)$. Computing this Jacobian shows it is a *rotation-and-scaling* that winds twice as you circle the equator. That winding number $2$ is the **Euler number** of $S^2$, and its nonvanishing is precisely why $TS^2$ is nontrivial and the hairy-ball theorem holds.

<a id="s3"></a>
### Principal $G$-bundles and structure groups; the frame bundle; associated bundles

Vector bundles record "internal vectors." But the gauge *symmetry* — the group $G$ that relabels them — is itself geometric. The bundle that carries the symmetry directly, with the group as its fiber, is the **principal bundle**. It is the central object of gauge theory.

#### Structure group

We first note that the transition functions of a bundle often land not in all of $\mathrm{Diff}(F)$ or all of $GL(k)$ but in a smaller group $G$ acting on $F$. We then say $G$ is the **structure group** of the bundle. For a real vector bundle with a chosen metric on each fiber, the transitions can be taken in the orthogonal group $O(k)$; for a complex bundle with Hermitian fibers, in the unitary group $U(k)$. Recall (Group Theory guide): a **Lie group** is a group that is also a smooth manifold with smooth multiplication and inversion; matrix groups like $U(1)$, $SU(2)$, $SU(3)$ are the relevant examples.

#### Principal bundles

> **Definition — principal $G$-bundle.**
>
> Let $G$ be a Lie group. A **principal $G$-bundle** is a fiber bundle $\pi:P\to M$ whose fiber is $G$ itself, together with a smooth **right action** $P\times G\to P$, $(p,g)\mapsto p\cdot g$, such that:
> - $G$ acts **freely** ($p\cdot g=p$ implies $g=e$, the identity) and **transitively on each fiber** (any two points of a fiber differ by a unique group element), so the fibers are exactly the **orbits** of the action, and
> - the local trivializations are $G$-**equivariant**: $\phi_U(p\cdot g)=\phi_U(p)\cdot g$, where $G$ acts on $U\times G$ by right multiplication on the second factor.

The right action is the abstract version of "relabel the internal frame by a group element." Crucially, a principal bundle has *no preferred point* in each fiber — there is no canonical identity element of $\pi^{-1}(x)\cong G$ until you pick a trivialization (a "gauge"). A trivialization is the same data as a **local section** $\sigma:U\to P$ (a choice of "reference frame" at each point): given $\sigma$, every point of the fiber is uniquely $\sigma(x)\cdot g$, which defines $\phi_U(\sigma(x)\cdot g)=(x,g)$.

> **Key fact — a principal bundle is trivial iff it admits a global section.** ($\Rightarrow$) A trivialization $P\cong M\times G$ gives the section $x\mapsto(x,e)$. ($\Leftarrow$) A global section $\sigma$ gives the trivialization $\sigma(x)\cdot g\mapsto(x,g)$, which is well-defined and $G$-equivariant by freeness and transitivity. This is the principal-bundle analogue of "vector bundle trivial iff it has a global frame."

#### The frame bundle

> **Definition — frame bundle.**
>
> For a rank-$k$ vector bundle $E\to M$, the **frame bundle** $FE$ has fiber over $x$ the set of all ordered bases (**frames**) $(e_1,\dots,e_k)$ of $E_x$. The group $GL(k,\mathbb{R})$ acts freely and transitively on frames by $\big(e_a\big)\cdot g=\big(e_b\, g^b{}_a\big)$ (change of basis), making $FE$ a principal $GL(k,\mathbb{R})$-bundle.

For $E=TM$ this is the **bundle of tangent frames** $F(TM)$. If $M$ carries a Riemannian metric we can restrict to *orthonormal* frames, getting a principal $O(k)$-bundle (the orthonormal frame bundle) — this is the geometric home of vielbeins/tetrads in general relativity.

#### Associated bundles

The principal bundle is the master object; vector bundles are *recovered* from it.

> **Definition — associated bundle.**
>
> Let $\pi:P\to M$ be a principal $G$-bundle and let $\rho:G\to GL(V)$ be a **representation** of $G$ on a vector space $V$ (a homomorphism into linear maps of $V$; Group Theory guide). The **associated vector bundle** is
> $$
> P\times_\rho V\ :=\ (P\times V)\big/\sim,\qquad (p\cdot g,\,v)\sim(p,\,\rho(g)v),
> $$
> the quotient of $P\times V$ by the equivalence that "moving the frame by $g$ and the components by $\rho(g)$ leaves the physical vector fixed." It is a vector bundle over $M$ with fiber $V$ and structure group $\rho(G)$.

> **Intuition.** $P$ stores *all possible frames and how the group permutes them*. A representation $\rho$ says *how a given kind of matter responds* to a frame change. Pairing them ($P\times_\rho V$) reconstructs the physical field bundle. One principal bundle, many associated matter bundles — electrons, quarks, Higgs fields — each via its own representation. This is why gauge theory puts the principal bundle first.

> **Worked example — frame bundle gives back the tangent bundle.** Take $P=F(TM)$ (frames of $TM$, group $GL(n,\mathbb{R})$) and $\rho=\mathrm{id}$ the defining representation on $V=\mathbb{R}^n$. Then $P\times_\rho\mathbb{R}^n\cong TM$: a frame $(e_a)$ together with components $v\in\mathbb{R}^n$ represents the vector $e_a v^a$, and the relation $(e_a g^a{}_b,\,v)\sim(e_a,\,g v)$ is exactly the statement that this vector is basis-independent. We have come full circle.

## Part B · Connections and curvature

<a id="s4"></a>
### Connections on a principal bundle — the connection 1-form, horizontal and vertical subspaces

A connection answers the question: *given a point in one fiber, which points in nearby fibers count as "the same, transported"?* On a principal bundle the cleanest formulation is to split the tangent space of the total space into "along the fiber" and "across to neighbors."

#### Vertical and horizontal

At a point $p\in P$, the tangent space $T_pP$ contains directions tangent to the fiber. Because the fiber is a $G$-orbit, each Lie-algebra element $\xi\in\mathfrak{g}$ (the **Lie algebra** of $G$, i.e. its tangent space at the identity, with bracket $[\cdot,\cdot]$) generates a curve $p\cdot\exp(t\xi)$ through $p$, whose velocity is a vertical vector.

> **Definition — vertical subspace.** The **vertical subspace** is $V_p=\ker(d\pi_p)\subseteq T_pP$: the directions that project to zero in the base, i.e. tangent to the fiber. The map $\xi\mapsto \frac{d}{dt}\big|_0\,p\cdot\exp(t\xi)$, called the **fundamental vector field** $\xi^\#$, is a linear isomorphism $\mathfrak{g}\xrightarrow{\sim}V_p$.

There is no canonical "horizontal" complement; choosing one *is* the connection.

> **Definition — connection (Ehresmann).**
>
> A **connection** on a principal $G$-bundle $P$ is a smooth choice, at each $p\in P$, of a **horizontal subspace** $H_p\subseteq T_pP$ such that
> 1. $T_pP=V_p\oplus H_p$ (horizontal complements vertical), and
> 2. the choice is $G$-equivariant: $H_{p\cdot g}=(R_g)_*H_p$, where $R_g$ is right translation by $g$ and $(R_g)_*$ its differential.

Condition 2 says the horizontal directions are consistent across a fiber — translating by the group carries horizontal to horizontal. A path in $P$ is **horizontal** if its velocity lies in $H$ everywhere; this is the precise notion of "transported without change," developed in s7.

#### The connection 1-form

The split is encoded compactly by a $\mathfrak{g}$-valued 1-form.

> **Definition — connection 1-form.**
>
> The **connection 1-form** $\omega\in\Omega^1(P;\mathfrak{g})$ (a 1-form on $P$ valued in the Lie algebra) is defined by:
> - $\omega(\xi^\#)=\xi$ for every $\xi\in\mathfrak{g}$ (it reads off the vertical part), and
> - $\ker\omega_p=H_p$ (its kernel is the horizontal subspace).
>
> Equivalently, $\omega$ projects each tangent vector onto its vertical part and identifies that with an element of $\mathfrak{g}$. Equivariance of $H$ is encoded by
> $$
> R_g^*\omega=\mathrm{Ad}_{g^{-1}}\circ\,\omega,
> $$
> where $\mathrm{Ad}_{g^{-1}}(\xi)=g^{-1}\xi g$ is the **adjoint action** of $G$ on $\mathfrak{g}$.

> **Why these two data agree.** Given $\omega$, set $H_p=\ker\omega_p$; since $\omega$ restricted to $V_p$ is the isomorphism $V_p\cong\mathfrak{g}$ (first bullet), its kernel meets $V_p$ only in $0$ and has the complementary dimension, so $T_pP=V_p\oplus H_p$. Conversely a split defines $\omega$ as "vertical projection followed by $V_p\cong\mathfrak{g}$." The two formulations of a connection are therefore equivalent — we use whichever is convenient.

> **Intuition.** $\omega$ is a "level meter": fed any motion in $P$, it returns the part that is *purely internal relabeling* (vertical), discarding genuine base motion (horizontal). To say "no internal change happened" is to say $\omega=0$ along the motion. The gauge field, next, is what $\omega$ looks like in a chosen gauge.

<a id="s5"></a>
### The local gauge potential $A$ and gauge transformations (how $A$ transforms)

The connection 1-form $\omega$ lives upstairs on $P$, which is hard to picture. Physicists work downstairs on spacetime $M$ with the **gauge potential** $A$ — the pullback of $\omega$ by a chosen local section (a chosen gauge).

#### Definition

> **Definition — local gauge potential.**
>
> Let $\sigma_\alpha:U_\alpha\to P$ be a local section (a gauge choice). The **local gauge potential** is the pulled-back 1-form
> $$
> A_\alpha\ :=\ \sigma_\alpha^*\omega\ \in\ \Omega^1(U_\alpha;\mathfrak{g}),
> $$
> a $\mathfrak{g}$-valued 1-form on the patch $U_\alpha\subseteq M$. In coordinates $A_\alpha=A_\mu\,dx^\mu$ with each $A_\mu(x)\in\mathfrak{g}$ a Lie-algebra element. For a matrix group, $A_\mu$ is a matrix of 1-form components; this is the **gauge field** of physics (the photon potential, the gluon field).

#### How $A$ transforms under a change of gauge

Two gauges $\sigma_\alpha,\sigma_\beta$ over the overlap $U_\alpha\cap U_\beta$ are related by the transition function $g_{\alpha\beta}:U_\alpha\cap U_\beta\to G$ via $\sigma_\beta=\sigma_\alpha\cdot g_{\alpha\beta}$ (relabel the reference frame by a group element at each point). We derive the resulting change in $A$. Write $g:=g_{\alpha\beta}$.

> **Theorem — gauge transformation of the potential.**
> $$
> A_\beta\ =\ g^{-1}A_\alpha\,g\ +\ g^{-1}\,dg.
> $$

*Proof.*
1. By definition $A_\beta=\sigma_\beta^*\omega$ and $\sigma_\beta=R_g\circ\sigma_\alpha$ followed by the action — more carefully, $\sigma_\beta(x)=\sigma_\alpha(x)\cdot g(x)$, a composition of the section, the right action, and the map $x\mapsto g(x)$. We pull $\omega$ back through this composition.
2. The differential of $x\mapsto\sigma_\alpha(x)\cdot g(x)$ splits, by the **Leibniz rule for the action map** $P\times G\to P$, into two contributions: one moving $\sigma_\alpha$ with $g$ held fixed, and one moving $g$ with $\sigma_\alpha$ held fixed.
3. **First contribution (move $\sigma_\alpha$):** holding $g(x)=g$ fixed and varying the first slot gives $R_g\circ\sigma_\alpha$. Pulling $\omega$ back, $(\,R_g\circ\sigma_\alpha)^*\omega=\sigma_\alpha^*(R_g^*\omega)=\sigma_\alpha^*(\mathrm{Ad}_{g^{-1}}\omega)$ by the equivariance $R_g^*\omega=\mathrm{Ad}_{g^{-1}}\omega$ (s4). With $g$ now position-dependent this yields $\mathrm{Ad}_{g(x)^{-1}}A_\alpha=g^{-1}A_\alpha g$ (matrix conjugation is how $\mathrm{Ad}$ acts for matrix groups).
4. **Second contribution (move $g$):** holding the point $\sigma_\alpha(x)$ fixed and varying $g(x)$ moves along the fiber. The velocity of $p\cdot g(x)$ as $g$ varies is the fundamental vector field of $g^{-1}dg\in\mathfrak g$ (this combination is the **Maurer–Cartan form** of $G$ pulled back by $g$; it is the canonical $\mathfrak g$-valued 1-form $\theta=g^{-1}dg$ that measures infinitesimal group motion). On a fundamental vector field $\omega$ returns its generator (first bullet of the $\omega$ definition), giving $g^{-1}dg$.
5. Adding the two contributions:
   $$
   A_\beta=g^{-1}A_\alpha\,g+g^{-1}\,dg.\qquad\blacksquare
   $$

The same formula, read with $g$ a *spacetime-dependent gauge transformation within one patch* (a section of the bundle of group elements), is the physicist's **gauge transformation** $A\mapsto g^{-1}Ag+g^{-1}dg$.

#### The abelian case and a worked example

For $G=U(1)$, group elements are phases $g=e^{i\chi(x)}$ and the Lie algebra is $i\mathbb{R}$ (imaginary numbers); conjugation $g^{-1}Ag=A$ is trivial since $U(1)$ is abelian, and $g^{-1}dg=e^{-i\chi}\,d(e^{i\chi})=i\,d\chi$. Writing $A=iqA_\mu^{\mathrm{phys}}dx^\mu$ the law collapses to
$$
A_\mu^{\mathrm{phys}}\ \mapsto\ A_\mu^{\mathrm{phys}}+\tfrac{1}{q}\,\partial_\mu\chi,
$$
which is exactly the familiar **electromagnetic gauge transformation** $A_\mu\mapsto A_\mu+\partial_\mu\lambda$. The geometry has reproduced the textbook rule.

> **Pitfall.** The inhomogeneous term $g^{-1}dg$ is why $A$ is *not* a tensor (a section of an associated bundle): it does not transform homogeneously. Two potentials related by a gauge transformation describe the *same physics*; only gauge-invariant quantities (curvature traces, holonomies) are observable.

<a id="s6"></a>
### Curvature — the curvature 2-form and the field strength $F=dA+A\wedge A$ (derive the transformation law)

Curvature measures the failure of horizontal transport to close up around a loop — equivalently, the failure of two infinitesimal gauge motions to commute. It is the field strength.

#### Definition upstairs

> **Definition — curvature 2-form.**
>
> The **curvature 2-form** of a connection $\omega$ is
> $$
> \Omega\ :=\ d\omega+\tfrac12[\omega,\omega]\ \in\ \Omega^2(P;\mathfrak{g}),
> $$
> where $d$ is the exterior derivative and $[\omega,\omega]$ is the Lie-bracket-valued wedge: on vectors $u,v$, $[\omega,\omega](u,v)=2[\omega(u),\omega(v)]$. Equivalently $\Omega=d\omega\circ(\mathrm{horizontal\ projection})$ — curvature is the *horizontal* part of $d\omega$ (**Cartan's structure equation**).

For a matrix group the bracket is the commutator, and $\tfrac12[\omega,\omega]=\omega\wedge\omega$ (matrix wedge), so $\Omega=d\omega+\omega\wedge\omega$.

#### The local field strength

> **Definition — field strength.**
>
> Pulling back by a gauge $\sigma_\alpha$, the **field strength** is
> $$
> F\ :=\ \sigma_\alpha^*\Omega\ =\ dA+A\wedge A\ \in\ \Omega^2(U_\alpha;\mathfrak{g}),
> $$
> using $\sigma^*d\omega=d\sigma^*\omega=dA$ (pullback commutes with $d$) and $\sigma^*(\omega\wedge\omega)=A\wedge A$. In components, with $A=A_\mu dx^\mu$,
> $$
> F=\tfrac12 F_{\mu\nu}\,dx^\mu\wedge dx^\nu,\qquad F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu+[A_\mu,A_\nu].
> $$

> **Derivation of the component formula.**
> 1. $dA=d(A_\mu dx^\mu)=\partial_\nu A_\mu\,dx^\nu\wedge dx^\mu$ by the definition of $d$ on a 1-form. Relabeling and antisymmetrizing, $dA=\tfrac12(\partial_\mu A_\nu-\partial_\nu A_\mu)dx^\mu\wedge dx^\nu$, since $dx^\nu\wedge dx^\mu=-dx^\mu\wedge dx^\nu$ (wedge is antisymmetric).
> 2. $A\wedge A=A_\mu A_\nu\,dx^\mu\wedge dx^\nu=\tfrac12[A_\mu,A_\nu]\,dx^\mu\wedge dx^\nu$: the wedge antisymmetrizes the $dx$'s, so only the antisymmetric part of the matrix product $A_\mu A_\nu$ survives, and $A_\mu A_\nu-A_\nu A_\mu=[A_\mu,A_\nu]$ by definition of the commutator.
> 3. Add: $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu+[A_\mu,A_\nu]$. $\blacksquare$

For $U(1)$ the commutator vanishes and $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$ — the **electromagnetic field tensor**, encoding $\mathbf E$ and $\mathbf B$.

#### How $F$ transforms (the gauge covariance)

> **Theorem.** Under a gauge change with transition $g$,
> $$
> F_\beta\ =\ g^{-1}F_\alpha\,g\qquad(\text{i.e. }F\mapsto g^{-1}Fg,\text{ homogeneous adjoint transformation}).
> $$

*Proof.* Use $A_\beta=g^{-1}A_\alpha g+g^{-1}dg$ (s5); write $A=A_\alpha$, suppress wedge symbols, and abbreviate $h=g^{-1}$ so $dh=-g^{-1}(dg)g^{-1}$.
1. **Compute $dA_\beta$.** $dA_\beta=d(g^{-1}Ag)+d(g^{-1}dg)$. By the Leibniz rule for $d$ on products of matrix-valued forms (with sign for moving $d$ past a 1-form),
   $$
   d(g^{-1}Ag)=(dg^{-1})Ag - g^{-1}A\,(dg)\cdot(-1)\ \to\ (dg^{-1})\wedge A\,g + g^{-1}(dA)g - g^{-1}A\wedge dg.
   $$
   Here $dg^{-1}=-g^{-1}(dg)g^{-1}$ (differentiate $g^{-1}g=\mathrm{id}$). And $d(g^{-1}dg)=(dg^{-1})\wedge dg=-g^{-1}(dg)g^{-1}\wedge dg$.
2. **Compute $A_\beta\wedge A_\beta$.** Expanding $(g^{-1}Ag+g^{-1}dg)\wedge(g^{-1}Ag+g^{-1}dg)$ gives four terms:
   $$
   g^{-1}A\wedge A\,g\ +\ g^{-1}A\,(dg)\ +\ g^{-1}(dg)g^{-1}A g\ +\ g^{-1}(dg)g^{-1}\wedge dg,
   $$
   using $g\,g^{-1}=\mathrm{id}$ to simplify the middle factors.
3. **Add $dA_\beta+A_\beta\wedge A_\beta$ and cancel.** Collect terms:
   - $g^{-1}(dA)g+g^{-1}(A\wedge A)g=g^{-1}F\,g$ — the wanted result.
   - The term $g^{-1}A\wedge dg$ from step 1 cancels $+g^{-1}A\,dg$ from step 2.
   - The term $-g^{-1}(dg)g^{-1}\wedge Ag$ (from $dg^{-1}\wedge Ag$ in step 1) cancels $+g^{-1}(dg)g^{-1}Ag$ from step 2.
   - The two pure-$dg$ terms $-g^{-1}(dg)g^{-1}\wedge dg$ (step 1) and $+g^{-1}(dg)g^{-1}\wedge dg$ (step 2) cancel.
4. Everything inhomogeneous cancels, leaving $F_\beta=g^{-1}F_\alpha\,g$. $\blacksquare$

> **Why this matters.** $F$ transforms *homogeneously* (in the adjoint representation), so it is a genuine section of an associated bundle — a tensor. Gauge-invariant combinations like $\mathrm{tr}(F\wedge\star F)$ are then well-defined observables. Curvature, not the potential, is the physical field. The abelian $U(1)$ case is even stronger: conjugation is trivial, so $F$ is *fully gauge-invariant* — the electromagnetic field $\mathbf E,\mathbf B$ is directly measurable, as we know.

#### The Bianchi identity

Differentiating $F=dA+A\wedge A$ gives an identity, automatic from the definitions, that is the geometric content of half of Maxwell's equations.

> **Theorem — Bianchi identity.** $\quad dF+[A,F]=0$, written $D_A F=0$ with $D_A$ the gauge-covariant exterior derivative.

*Proof.*
1. $dF=d(dA)+d(A\wedge A)=0+(dA)\wedge A-A\wedge dA$, since $d^2=0$ (nilpotency of $d$) and Leibniz with the sign $d(A\wedge A)=dA\wedge A-A\wedge dA$ for 1-forms.
2. Now $[A,F]=A\wedge F-F\wedge A=A\wedge(dA+A\wedge A)-(dA+A\wedge A)\wedge A=A\wedge dA + A\wedge A\wedge A - dA\wedge A - A\wedge A\wedge A$.
3. The triple-$A$ terms cancel; adding to step 1: $dF+[A,F]=(dA\wedge A-A\wedge dA)+(A\wedge dA-dA\wedge A)=0$. $\blacksquare$

For $U(1)$ this is $dF=0$, i.e. $\partial_{[\lambda}F_{\mu\nu]}=0$ — exactly the homogeneous Maxwell equations $\nabla\cdot\mathbf B=0$ and $\nabla\times\mathbf E=-\partial_t\mathbf B$.

## Part C · Transport, matter, and dynamics

<a id="s7"></a>
### Parallel transport, holonomy, and Wilson loops

The connection's job is to transport fiber elements along base paths. Going around a loop and measuring the net transformation is **holonomy**; its trace is the **Wilson loop**, the basic gauge-invariant observable.

#### Parallel transport

> **Definition — horizontal lift and parallel transport.**
>
> Let $\gamma:[0,1]\to M$ be a smooth path and $p_0\in P$ a point over $\gamma(0)$. The **horizontal lift** is the unique path $\tilde\gamma:[0,1]\to P$ with $\pi\circ\tilde\gamma=\gamma$, $\tilde\gamma(0)=p_0$, and $\tilde\gamma$ horizontal (velocity in $H$, i.e. $\omega(\dot{\tilde\gamma})=0$). **Parallel transport** along $\gamma$ is the map $E_{\gamma(0)}\to E_{\gamma(1)}$ (on an associated bundle) induced by following the lift.

Existence and uniqueness of the lift follow from solving the first-order ODE $\omega(\dot{\tilde\gamma})=0$, which in a gauge reads
$$
\frac{d}{dt}U(t)=-A_\mu\big(\gamma(t)\big)\,\dot\gamma^\mu(t)\,U(t),\qquad U(0)=\mathrm{id},
$$
for the transport matrix $U(t)\in G$. This linear ODE has a unique solution by the standard existence-uniqueness theorem (Differential Equations guide). Its solution is the **path-ordered exponential**
$$
U[\gamma]=\mathcal P\exp\!\Big(-\!\int_\gamma A\Big),
$$
where path ordering $\mathcal P$ places later-time factors to the left because the $A_\mu$ at different points generally do not commute (in the nonabelian case).

> **Worked example — abelian transport.** For $U(1)$ the $A$'s commute, ordering is irrelevant, and $U[\gamma]=\exp\!\big(-\int_\gamma A\big)=\exp\!\big(-i q\int_\gamma A^{\mathrm{phys}}\big)$. A charged particle's wavefunction picks up the phase $\exp(iq\int_\gamma A^{\mathrm{phys}})$ — the geometric origin of the Aharonov–Bohm phase (s11).

#### Holonomy

> **Definition — holonomy.** For a *loop* $\gamma$ based at $x$ ($\gamma(0)=\gamma(1)=x$), parallel transport returns to the same fiber $E_x$, giving an automorphism $U[\gamma]\in G$, the **holonomy** of $\gamma$. The set of all holonomies based at $x$ forms the **holonomy group** $\mathrm{Hol}_x\subseteq G$.

Holonomy is the integrated, finite version of curvature. The **Ambrose–Singer theorem** states that the Lie algebra of the holonomy group is spanned by the curvature $F$ evaluated over the manifold — flat connections ($F=0$ on a simply connected base) have trivial holonomy, while curvature is exactly the infinitesimal holonomy of an infinitesimal loop:
$$
U[\partial\Sigma]\approx \mathrm{id}-F_{\mu\nu}\,\tfrac12\,\Delta S^{\mu\nu}+\cdots
$$
for a small loop bounding an oriented area element $\Delta S^{\mu\nu}$. This is the precise sense in which "curvature = failure to return to where you started after a small loop."

#### Wilson loops

Holonomy $U[\gamma]$ depends on the gauge: under $g$ it conjugates, $U[\gamma]\mapsto g(x)^{-1}U[\gamma]g(x)$. To get a gauge-invariant number, take the **trace**.

> **Definition — Wilson loop.** $\displaystyle W[\gamma]=\mathrm{tr}\,\mathcal P\exp\!\Big(-\oint_\gamma A\Big).$ Because $\mathrm{tr}(g^{-1}Ug)=\mathrm{tr}(U)$ (cyclicity of the trace), $W[\gamma]$ is **gauge-invariant** and hence a genuine observable. Wilson loops are the fundamental observables of lattice gauge theory and detect confinement in QCD (area-law behavior).

<a id="s8"></a>
### The covariant derivative on associated bundles; minimal coupling to matter fields

A matter field is a section $\psi$ of an associated vector bundle $E=P\times_\rho V$. To write field equations we must differentiate $\psi$, but the ordinary derivative is not gauge-covariant. The connection supplies the fix: the **covariant derivative**.

#### Definition

> **Definition — covariant derivative (gauge derivative).**
>
> Let $\rho:G\to GL(V)$ be the representation and $d\rho:\mathfrak g\to\mathfrak{gl}(V)$ its induced Lie-algebra representation. For a section $\psi$ (in a gauge, a $V$-valued function on $U$), the **covariant derivative** is
> $$
> D\psi=d\psi+\rho_*(A)\,\psi,\qquad\text{componentwise } D_\mu\psi=\partial_\mu\psi+\rho_*(A_\mu)\,\psi,
> $$
> where $\rho_*=d\rho$ represents the algebra element $A_\mu$ as an operator on $V$. For the defining representation of a matrix group, $\rho_*(A_\mu)=A_\mu$ acts by matrix multiplication.

#### Gauge covariance — the point of the construction

> **Theorem.** If $\psi\mapsto\rho(g)^{-1}\psi$ under a gauge change (the transformation law of an associated-bundle section), and $A$ transforms by s5, then $D_\mu\psi$ transforms *homogeneously*: $D_\mu\psi\mapsto\rho(g)^{-1}D_\mu\psi$.

*Proof (matrix/defining representation, $\rho_*(A)=A$).* Write $\psi'=g^{-1}\psi$, $A'=g^{-1}Ag+g^{-1}dg$.
1. $D'_\mu\psi'=\partial_\mu(g^{-1}\psi)+A'_\mu(g^{-1}\psi)$.
2. $\partial_\mu(g^{-1}\psi)=(\partial_\mu g^{-1})\psi+g^{-1}\partial_\mu\psi$ by the product rule. And $\partial_\mu g^{-1}=-g^{-1}(\partial_\mu g)g^{-1}$ (differentiate $g^{-1}g=\mathrm{id}$).
3. $A'_\mu g^{-1}\psi=(g^{-1}A_\mu g+g^{-1}\partial_\mu g)g^{-1}\psi=g^{-1}A_\mu\psi+g^{-1}(\partial_\mu g)g^{-1}\psi$.
4. Add steps 2 and 3: the terms $-g^{-1}(\partial_\mu g)g^{-1}\psi$ and $+g^{-1}(\partial_\mu g)g^{-1}\psi$ cancel, leaving
   $$
   D'_\mu\psi'=g^{-1}\partial_\mu\psi+g^{-1}A_\mu\psi=g^{-1}(\partial_\mu\psi+A_\mu\psi)=g^{-1}D_\mu\psi.\qquad\blacksquare
   $$

Because $D_\mu\psi$ transforms like $\psi$ itself, any expression built from $\psi$ and $D\psi$ in a gauge-invariant way (e.g. $|D_\mu\psi|^2$ for a unitary representation) is a legitimate term in a Lagrangian. The inhomogeneous part of $A$ exists *precisely* to cancel the inhomogeneous part of $\partial_\mu\psi$.

#### Minimal coupling

> **Principle — minimal coupling.** To make a matter theory gauge-invariant, replace every ordinary derivative by the covariant derivative: $\partial_\mu\to D_\mu=\partial_\mu+A_\mu$. This single substitution introduces the interaction between matter and the gauge field, with no free parameters beyond the coupling constant inside $A$.

> **Worked example — the gauged Schrödinger/Dirac equation ($U(1)$).** Here $\rho_*(A_\mu)=iqA^{\mathrm{phys}}_\mu$, so $D_\mu=\partial_\mu+iqA_\mu$. The free Schrödinger equation $i\partial_t\psi=-\tfrac{1}{2m}\nabla^2\psi$ becomes, under minimal coupling, $i(\partial_t+iq\phi)\psi=-\tfrac{1}{2m}(\nabla-iq\mathbf A)^2\psi$ — exactly the Schrödinger equation for a charged particle in an electromagnetic field. The relativistic Dirac case gives $(i\gamma^\mu D_\mu-m)\psi=0$. The Lorentz force law and the entire interaction of charges with electromagnetism are encoded in $\partial\to D$.

#### Curvature as commutator of covariant derivatives

A clean identity ties s6 and s8 together:
$$
[D_\mu,D_\nu]\psi=F_{\mu\nu}\,\psi.
$$
*Proof.* $D_\mu D_\nu\psi=(\partial_\mu+A_\mu)(\partial_\nu\psi+A_\nu\psi)=\partial_\mu\partial_\nu\psi+(\partial_\mu A_\nu)\psi+A_\nu\partial_\mu\psi+A_\mu\partial_\nu\psi+A_\mu A_\nu\psi.$ Antisymmetrizing in $\mu\nu$: the symmetric $\partial_\mu\partial_\nu\psi$ and the mixed first-derivative terms cancel, leaving $(\partial_\mu A_\nu-\partial_\nu A_\mu+A_\mu A_\nu-A_\nu A_\mu)\psi=F_{\mu\nu}\psi$. $\blacksquare$ So **field strength is the obstruction to covariant derivatives commuting** — the gauge-theory echo of the Riemann tensor as commutator of covariant derivatives in the prerequisite guide.

<a id="s9"></a>
### Yang–Mills theory — the Yang–Mills action and field equations; Maxwell's equations as the $U(1)$ case (derive)

We now give the gauge field its own dynamics. The principle: build the simplest gauge-invariant, Lorentz-invariant action from the field strength.

#### The Hodge star and the action

Recall (prerequisite guide) the **Hodge star** $\star$ on an oriented (pseudo-)Riemannian $n$-manifold maps $p$-forms to $(n-p)$-forms using the metric, and that $\int_M \alpha\wedge\star\beta$ is the natural inner product of forms. For $\mathfrak g$-valued forms we also take a trace (an invariant inner product on $\mathfrak g$, the **Killing form** up to scale).

> **Definition — Yang–Mills action.**
> $$
> S_{\mathrm{YM}}[A]=-\frac{1}{2g_{\mathrm{YM}}^2}\int_M \mathrm{tr}\big(F\wedge\star F\big)=-\frac{1}{4g_{\mathrm{YM}}^2}\int_M \mathrm{tr}\big(F_{\mu\nu}F^{\mu\nu}\big)\sqrt{-\det g}\,\,d^nx,
> $$
> where $g_{\mathrm{YM}}$ is the **coupling constant** (written $g_{\mathrm{YM}}$ to distinguish it from the gauge/transition elements $g$ of §s5–s8), $\sqrt{-\det g}$ is the invariant volume factor built from the determinant of the spacetime metric $g_{\mu\nu}$, and indices are raised with that same metric. The integrand is gauge-invariant because $F\mapsto g^{-1}Fg$ and the trace is conjugation-invariant (cyclicity).

#### The field equations

> **Theorem — Yang–Mills equations.** Extremizing $S_{\mathrm{YM}}$ over $A$ gives
> $$
> D\star F=0,\qquad\text{i.e.}\qquad D_\mu F^{\mu\nu}=\partial_\mu F^{\mu\nu}+[A_\mu,F^{\mu\nu}]=0,
> $$
> together with the Bianchi identity $DF=0$ (s6) which holds automatically.

*Derivation.*
1. Vary $A\to A+\delta A$ with $\delta A$ a $\mathfrak g$-valued 1-form vanishing on the boundary. From $F=dA+A\wedge A$, the first-order change is $\delta F=d(\delta A)+\delta A\wedge A+A\wedge\delta A=D(\delta A)$, where $D(\delta A)=d(\delta A)+[A,\delta A]$ is the covariant exterior derivative (this *defines* $D$ on adjoint-valued forms; the bracket arises because $\delta A\wedge A+A\wedge\delta A=[A,\delta A]$ as a 2-form).
2. Then $\delta S_{\mathrm{YM}}=-\frac{1}{g_{\mathrm{YM}}^2}\int_M\mathrm{tr}\big(\delta F\wedge\star F\big)=-\frac{1}{g_{\mathrm{YM}}^2}\int_M\mathrm{tr}\big(D(\delta A)\wedge\star F\big)$, using linearity of the action in each $F$ factor and symmetry of the trace pairing.
3. **Integrate by parts.** For adjoint-valued forms, $\mathrm{tr}\big(D(\delta A)\wedge\star F\big)=d\,\mathrm{tr}(\delta A\wedge\star F)\pm\mathrm{tr}\big(\delta A\wedge D\star F\big)$, the covariant Leibniz rule for $D$ combined with cyclicity of the trace (the connection terms shift from one factor to the other with a sign). The total-derivative term integrates to a boundary term that vanishes since $\delta A=0$ on $\partial M$ (Stokes' theorem).
4. Hence $\delta S_{\mathrm{YM}}=\pm\frac{1}{g_{\mathrm{YM}}^2}\int_M\mathrm{tr}\big(\delta A\wedge D\star F\big)$. Requiring this to vanish for *all* $\delta A$ forces $D\star F=0$ by the fundamental lemma of the calculus of variations. $\blacksquare$

#### Maxwell's equations as the $U(1)$ case

> **Derivation.** For $G=U(1)$ the algebra is abelian, all brackets vanish, $F=dA$ with $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$, and the trace is trivial.
> 1. The Yang–Mills equation $D_\mu F^{\mu\nu}=0$ loses its bracket term and becomes $\partial_\mu F^{\mu\nu}=0$.
> 2. This is the **source-free case of the inhomogeneous (sourced) Maxwell pair** $\partial_\mu F^{\mu\nu}=0$, i.e. $\nabla\cdot\mathbf E=0$ and $\nabla\times\mathbf B=\partial_t\mathbf E$ (Gauss and Ampère with no charges).
> 3. The Bianchi identity $dF=0$ (s6) gives the **homogeneous Maxwell equations** $\nabla\cdot\mathbf B=0$, $\nabla\times\mathbf E=-\partial_t\mathbf B$.
> 4. Adding a matter current $J^\nu$ (from minimally coupled charged matter, s8) modifies the action by $\int A_\mu J^\mu$ and yields $\partial_\mu F^{\mu\nu}=J^\nu$ — the full inhomogeneous Maxwell equations.
>
> So **all four Maxwell equations are the $U(1)$ Yang–Mills equations plus Bianchi.** Nonabelian $G$ adds the self-interaction $[A_\mu,F^{\mu\nu}]$: gluons carry color charge and interact with each other, unlike photons. $\blacksquare$

> **Pitfall.** The nonabelian Yang–Mills equations are *nonlinear* in $A$ (because $F$ and $D$ both contain $A$). This nonlinearity — absent in electromagnetism — is responsible for asymptotic freedom and confinement in the strong force, and makes the equations vastly harder (the Yang–Mills mass-gap problem remains a Millennium Prize problem).

## Part D · Topology and physics

<a id="s10"></a>
### Characteristic classes — Chern classes and the Chern–Simons form; topological invariants

Some properties of a bundle cannot be changed by any smooth deformation of the connection — they are **topological invariants**, computed by integrating polynomials in the curvature. These are **characteristic classes**. They answer "how twisted is the bundle?" with an integer.

#### Chern–Weil theory

> **Theorem — Chern–Weil.** Let $P(F)$ be an $\mathrm{Ad}$-invariant polynomial in the curvature $F$ (invariant under $F\mapsto g^{-1}Fg$). Then the differential form $P(F)$ is **closed** ($dP(F)=0$) and its **de Rham cohomology class is independent of the connection** $A$. Its integrals over cycles are therefore topological invariants of the bundle.

*Sketch of why $P(F)$ is closed.* By invariance and the Bianchi identity $DF=0$: the exterior derivative of an invariant polynomial in $F$ can be written in terms of $DF$ (the connection terms assemble into covariant derivatives by invariance), and $DF=0$ kills it. Independence of $A$ follows because the difference $P(F_1)-P(F_0)$ for two connections is an exact form (a transgression).

#### Chern classes

For a *complex* vector bundle (structure group $U(k)$, the physically central case), the invariant polynomials of $\frac{i}{2\pi}F$ give the **Chern classes**.

> **Definition — Chern classes.** Expand the **total Chern class**
> $$
> c(F)=\det\!\Big(\mathrm{id}+\tfrac{i}{2\pi}F\Big)=1+c_1(F)+c_2(F)+\cdots,
> $$
> where $c_j(F)$ is the degree-$2j$ part. In particular:
> $$
> c_1=\tfrac{i}{2\pi}\,\mathrm{tr}\,F,\qquad c_2=\tfrac{1}{8\pi^2}\big(\mathrm{tr}\,F\wedge\mathrm{tr}\,F-\mathrm{tr}(F\wedge F)\big).
> $$
> Integrals $\int_\Sigma c_j$ over closed submanifolds are **integers** (Chern numbers).

> **Worked example — the first Chern number of a $U(1)$ bundle over $S^2$.** Here $F$ is an ordinary (imaginary) 2-form and $c_1=\frac{i}{2\pi}F$. The integral
> $$
> n=\int_{S^2}c_1=\frac{i}{2\pi}\int_{S^2}F
> $$
> is forced to be an integer: split $S^2$ into northern and southern caps with potentials $A_N,A_S$ differing by a gauge transformation $g=e^{in\phi}$ on the equator. By Stokes, $\int_{S^2}F=\oint_{\mathrm{eq}}(A_N-A_S)=\oint g^{-1}dg=2\pi i\,n$, giving integer $n$. This integer is the **magnetic charge** of a Dirac monopole (s11) and the **TKNN integer** of the quantum Hall effect — a topological invariant that cannot change continuously.

#### The Chern–Simons form

The Chern classes are *closed* but, locally, *exact*: $c_j(F)=d(\text{something})$. That "something" is the **Chern–Simons form**.

> **Definition — Chern–Simons 3-form.** For the second Chern class, $\mathrm{tr}(F\wedge F)=d\,\mathrm{CS}(A)$ with
> $$
> \mathrm{CS}(A)=\mathrm{tr}\Big(A\wedge dA+\tfrac{2}{3}A\wedge A\wedge A\Big).
> $$

*Verification that $d\,\mathrm{CS}(A)=\mathrm{tr}(F\wedge F)$.*
1. $d\,\mathrm{tr}(A\wedge dA)=\mathrm{tr}(dA\wedge dA)$ (the $A\wedge d(dA)$ term vanishes by $d^2=0$).
2. $d\,\mathrm{tr}(\tfrac23 A\wedge A\wedge A)=\tfrac23\cdot 3\,\mathrm{tr}(dA\wedge A\wedge A)=2\,\mathrm{tr}(dA\wedge A\wedge A)$ (Leibniz; the three terms are equal under the trace by cyclicity).
3. Meanwhile $\mathrm{tr}(F\wedge F)=\mathrm{tr}\big((dA+A^2)\wedge(dA+A^2)\big)=\mathrm{tr}(dA\wedge dA)+2\,\mathrm{tr}(dA\wedge A\wedge A)+\mathrm{tr}(A^4)$, and $\mathrm{tr}(A^4)=\mathrm{tr}(A\wedge A\wedge A\wedge A)=0$ by cyclicity together with the sign from moving a 1-form past three others.
4. Steps 1+2 reproduce steps 3 exactly: $d\,\mathrm{CS}(A)=\mathrm{tr}(F\wedge F)$. $\blacksquare$

The integral $\int_M\mathrm{CS}(A)$ over a 3-manifold is the **Chern–Simons action**, the basis of topological field theory, the theory of the fractional quantum Hall effect, and knot invariants. Under large gauge transformations it shifts by $2\pi$ times an integer, which quantizes its coupling (the "level" $k$).

<a id="s11"></a>
### Physical examples — the Dirac magnetic monopole and the Aharonov–Bohm effect; a word on instantons

We close by showing the abstract machinery at work in three landmark phenomena, each a place where the *topology* of the bundle is physically observable.

#### The Dirac magnetic monopole

A magnetic monopole is a hypothetical point source of magnetic field $\mathbf B=\frac{q_m}{4\pi}\frac{\hat r}{r^2}$. Then $\int_{S^2}\mathbf B\cdot d\mathbf S=q_m\ne 0$, so $F$ has nonzero flux through any sphere surrounding it — but $F=dA$ would force the flux to vanish by Stokes. The resolution is geometric.

> **Resolution — no global potential; a nontrivial $U(1)$ bundle.** There is no single smooth $A$ on $S^2$; instead use two patches (s10's caps) with potentials $A_N,A_S$ related on the equator by a $U(1)$ gauge transformation $g=e^{iq q_m\phi/(2\pi)}$. Smoothness of $g$ as $\phi\to\phi+2\pi$ (single-valuedness, since $\psi$ is a section of the bundle, not a function) requires the exponent to advance by an integer multiple of $2\pi i$:
> $$
> q\,q_m=2\pi n,\qquad n\in\mathbb{Z}.
> $$

This reconciles with the §s10 worked example $g=e^{in\phi}$: writing $n=q\,q_m/(2\pi)$, the equatorial transition $g=e^{iq q_m\phi/(2\pi)}=e^{in\phi}$, and single-valuedness ($q q_m=2\pi n$) is exactly the condition $n\in\mathbb{Z}$ used there.

This is the **Dirac quantization condition**: *the existence of a single magnetic monopole forces all electric charges to be integer multiples of a basic unit.* The integer $n$ is precisely the first Chern number of the bundle (s10). The would-be singularity of $A$ (the "Dirac string") is a gauge artifact of trying to use one patch where two are needed; the honest description is a nontrivial principal $U(1)$-bundle over $S^2$.

#### The Aharonov–Bohm effect

Take an infinite solenoid carrying flux $\Phi$, with $\mathbf B=0$ outside it. An electron travels through the field-free region outside, on either side of the solenoid, and the two beams interfere.

> **Analysis.** Outside, $F=0$, so the connection is *flat*; classically no force acts ($\mathbf E=\mathbf B=0$). Yet the holonomy (s7) around a loop encircling the solenoid is, by Stokes applied to the enclosed (non-simply-connected) region,
> $$
> U[\gamma]=\exp\!\Big(iq\oint_\gamma\mathbf A\cdot d\mathbf l\Big)=\exp\!\Big(iq\!\int_\Sigma F\Big)=\exp(iq\Phi)\ne 1.
> $$
> The relative phase $q\Phi$ between the two paths shifts the interference pattern — a measurable effect of a region the electron never entered.

The lesson: in gauge theory the *potential $A$ (the connection), not just the field $F$ (the curvature), has physical reality* — but only through gauge-invariant holonomies. The effect is topological: it depends only on the enclosed flux, i.e. on the homotopy class of the loop around the non-simply-connected region, and was confirmed experimentally by Tonomura. It is the cleanest demonstration that physics lives on bundles, not merely on spacetime fields.

#### A word on instantons

In Euclidean $4$-dimensional Yang–Mills theory, finite-action field configurations are classified by the second Chern number,
$$
\nu=\frac{1}{8\pi^2}\int_{\mathbb{R}^4}\mathrm{tr}(F\wedge F)\in\mathbb{Z},
$$
the **instanton number** (topological charge). Configurations with $\nu\ne 0$ are **instantons**: localized, finite-action solutions of the **self-dual** equation $F=\star F$, which automatically solve the Yang–Mills equations (self-duality plus Bianchi $DF=0$ gives $D\star F=DF=0$). For $SU(2)$ the minimal instanton ($\nu=1$) is the BPST solution. Instantons mediate quantum tunneling between topologically distinct vacua, resolve the $U(1)$ problem in QCD, and underlie the strong-CP question. They are the most vivid example of the theme of this guide: a *topological invariant of a bundle* controlling genuine physics.

> **Closing intuition.** Each phenomenon here is invisible to a purely local analysis — locally $A$ is pure gauge, $F$ is zero or a tame field — yet each produces a measurable effect controlled by an integer: a Chern number, a winding, an instanton charge. That is the signature of bundle geometry: the global topology of how fibers are glued is physical.

---

*This guide built gauge theory from the ground up — fiber and vector bundles, sections and frames, principal bundles and their associated matter bundles, connections as horizontal distributions and as the $1$-form $\omega$, the local potential $A$ and its inhomogeneous gauge law, curvature $F=dA+A\wedge A$ transforming homogeneously, parallel transport and holonomy, the covariant derivative and minimal coupling, the Yang–Mills action with Maxwell as its abelian shadow, and finally the Chern classes and Chern–Simons forms that turn curvature integrals into integers. The single idea beneath all of it is that a force is a connection: comparing internal states across spacetime requires a choice, gauge symmetry is the freedom in that choice, and curvature is the unavoidable, observable residue. Return to any boxed definition or numbered derivation as a reference — and remember that the deepest physics often lives not in the fields over spacetime but in the topology of how the fibers above it are glued.*
