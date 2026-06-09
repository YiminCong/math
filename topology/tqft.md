**English** · [中文](tqft.zh.md)

# Higher Categories & Topological Quantum Field Theory, *invariants from gluing.*

*A from-scratch course in the categorical machine that turns the geometry of cutting and gluing manifolds into computable topological invariants: cobordism categories, monoidal and symmetric monoidal categories, the Atiyah–Segal axioms, the equivalence between two-dimensional TQFTs and commutative Frobenius algebras, the three-dimensional theories of Reshetikhin–Turaev and Witten–Chern–Simons that produce the Jones polynomial, and finally the higher-categorical summit — extended TQFT and the cobordism hypothesis. Every categorical and algebraic word is defined the first time it appears, every theorem is stated precisely, and the central equivalence is proved with no gaps.*

[← Back to all guides](../README.md)

> **How to read this guide.** Three earlier guides are useful but not strictly required. From the *Algebraic Topology* guide we borrow the words *manifold*, *homeomorphism*, *homology*, and *invariant*; each is restated in one line on first use. From the *Homological Algebra* guide we borrow the language of *category*, *functor*, and *natural transformation*; these are fully redefined in §s2 so the guide is self-contained. From the *Group Theory* guide we borrow *group*, *vector space*, and *linear map*. We assume only ordinary linear algebra and a little single-variable calculus. Nothing is "left to the reader": every claim is argued.

---

## Part A — From geometry to algebra

<a id="s0"></a>
### Motivation: TQFTs as functors that compute topological invariants by cutting and gluing

**What & why.** A *topological invariant* is a quantity assigned to a space that does not change under continuous deformation — for example a number, a vector space, or a polynomial that is the same for two spaces whenever one can be bent into the other without tearing. The hard part of topology is *computing* such invariants. The central idea of a **topological quantum field theory (TQFT)** is a computational strategy: cut a complicated manifold into simple standard pieces, assign known algebraic data to each piece, and *multiply the pieces back together* algebraically to recover the invariant of the whole. The slogan is **invariants from gluing**.

A **manifold** is a space that locally looks like ordinary Euclidean space $\mathbb{R}^n$ for some fixed $n$, its *dimension*; a circle is a $1$-manifold, a sphere or torus is a $2$-manifold. A **closed manifold** is one that is compact (no points run off to infinity) and has no boundary. The basic objects a TQFT studies are closed manifolds together with the *cobordisms* between them — manifolds-with-boundary that interpolate from one closed manifold to another, the precise notion of "a piece you can glue."

Here is the strategy in one picture. Suppose $X$ is a closed $n$-manifold we want to assign a number $Z(X)$. Cut $X$ along an $(n-1)$-manifold $\Sigma$ into two halves $M_1$ and $M_2$, each a cobordism with boundary $\Sigma$. A TQFT assigns:

- to the cut $\Sigma$, a *vector space* $Z(\Sigma)$ — a "state space";
- to each half $M_i$, a *vector* (or covector) in that space;
- and it declares that gluing the halves corresponds to *pairing the vectors*, $Z(X)=\langle Z(M_1), Z(M_2)\rangle$.

The miracle, made precise by the **Atiyah–Segal axioms** (§s3), is that this is consistent: however you cut, you get the same answer, because the assignment is a *functor* — a structure-preserving map of categories — from a category of manifolds-and-cobordisms to a category of vector spaces.

> **The thread of the whole guide.** Build the geometric category $\mathrm{Cob}(n)$ of cobordisms (§s1); learn the categorical grammar of "gluing in two directions," namely monoidal and symmetric monoidal categories (§s2); state the Atiyah–Segal definition of a TQFT as a symmetric monoidal functor (§s3); prove that in dimension two this data is *exactly* a commutative Frobenius algebra (§s4–s5); survey the much richer three-dimensional theories and the quantum invariants of knots they produce (§s6–s7); then climb to higher categories (§s8) and the cobordism hypothesis (§s9–s10), which classifies *all* sufficiently structured TQFTs by a single piece of algebra; and finish with the physics — anyons and topological quantum computation (§s11).

> **Why a physicist cares.** In quantum mechanics a system has a *Hilbert space of states* and time evolution is a linear operator on it. A TQFT is the limiting case where the dynamics depends only on the *topology* of spacetime, not on a metric or a clock — there is no energy, only shape. Such theories describe the long-distance physics of *topological phases of matter* (§s11), where the ground-state degeneracy is a topological invariant and excitations called *anyons* braid around each other to perform robust quantum computations.

We begin with the geometry: what exactly are the pieces we glue?

<a id="s1"></a>
### Cobordisms and the cobordism category $\mathrm{Cob}(n)$

**What & why.** To "cut and glue" we need a precise object that is "a manifold with two distinguished ends." That object is a *cobordism*. Assembling all closed $(n-1)$-manifolds as objects and all $n$-dimensional cobordisms as arrows produces the **cobordism category** $\mathrm{Cob}(n)$, the geometric stage on which every TQFT plays.

> **Definition — manifold with boundary.**
> An **$n$-manifold with boundary** is a space $M$ in which every point has a neighborhood homeomorphic either to $\mathbb{R}^n$ (an *interior* point) or to the half-space $\mathbb{R}^n_{\ge 0}=\{(x_1,\dots,x_n):x_n\ge 0\}$ (a *boundary* point). The set of boundary points is the **boundary** $\partial M$, itself a closed $(n-1)$-manifold. A **homeomorphism** is a continuous bijection with continuous inverse — the precise meaning of "the same shape." We work throughout with *oriented* manifolds: each carries a consistent choice of "handedness," and $\overline{\Sigma}$ denotes $\Sigma$ with the opposite orientation.

> **Definition — cobordism.**
> Let $\Sigma_0$ and $\Sigma_1$ be closed oriented $(n-1)$-manifolds. A **cobordism from $\Sigma_0$ to $\Sigma_1$** is a compact oriented $n$-manifold $M$ with boundary, together with an orientation-preserving identification
> $$
> \partial M \;\cong\; \overline{\Sigma_0}\,\sqcup\,\Sigma_1 ,
> $$
> where $\sqcup$ is disjoint union. We call $\Sigma_0$ the **incoming** (source) boundary and $\Sigma_1$ the **outgoing** (target) boundary, and write $M:\Sigma_0\to\Sigma_1$. The orientation reversal on the incoming end is the bookkeeping that makes gluing work: an outgoing end of one cobordism must match the *reversed* incoming end of the next.

*Worked example — the pair of pants.* Take $n=2$. The circle $S^1$ is a closed $1$-manifold. The "pair of pants" is a sphere with three holes: a surface $P$ with $\partial P=\overline{S^1\sqcup S^1}\sqcup S^1$. Read as a cobordism $P:S^1\sqcup S^1\to S^1$, it is "two circles come in, one circle goes out" — geometrically, two loops merging into one. We will see in §s5 that this single surface *is* the multiplication of a Frobenius algebra.

> **Definition — gluing (composition of cobordisms).**
> Given $M:\Sigma_0\to\Sigma_1$ and $N:\Sigma_1\to\Sigma_2$, their **composite** $N\circ M:\Sigma_0\to\Sigma_2$ is formed by gluing $M$ and $N$ along their common boundary $\Sigma_1$:
> $$
> N\circ M \;=\; M\cup_{\Sigma_1} N .
> $$
> Concretely one identifies the outgoing copy of $\Sigma_1$ in $M$ with the incoming copy of $\Sigma_1$ in $N$ point-for-point. A standard theorem of differential topology (the *collar neighborhood theorem*: every boundary has a neighborhood looking like $\Sigma_1\times[0,1)$) guarantees the result is again a smooth manifold with boundary $\overline{\Sigma_0}\sqcup\Sigma_2$.

A subtlety: gluing is only associative and unital *up to homeomorphism*, not on the nose, because a glued cylinder is homeomorphic but not equal to the original. The standard fix is to take **arrows of $\mathrm{Cob}(n)$ to be cobordisms up to orientation-preserving homeomorphism fixing the boundary** (equivalently, diffeomorphism in the smooth setting). Then composition is strictly associative, and the *cylinder* $\Sigma\times[0,1]:\Sigma\to\Sigma$ acts as an identity, because gluing a collar onto a manifold reproduces it up to the chosen equivalence.

> **Definition — the cobordism category $\mathrm{Cob}(n)$.**
> The category $\mathrm{Cob}(n)$ has:
> - **objects**: closed oriented $(n-1)$-manifolds;
> - **arrows** $\Sigma_0\to\Sigma_1$: equivalence classes of $n$-dimensional cobordisms $M:\Sigma_0\to\Sigma_1$ under boundary-fixing homeomorphism;
> - **composition**: gluing, $N\circ M=M\cup_{\Sigma_1}N$;
> - **identity** of $\Sigma$: the cylinder $\Sigma\times[0,1]$.

Let us verify the category axioms, since they are the foundation of everything.

1. **Composition is well-defined.** If $M\cong M'$ and $N\cong N'$ by boundary-fixing homeomorphisms, the homeomorphisms agree on the shared $\Sigma_1$ and so glue to a homeomorphism $M\cup N\cong M'\cup N'$. *Reason:* a map defined piecewise on a gluing is continuous when the pieces agree on the overlap (the *pasting lemma* of general topology).
2. **Associativity.** For $M:\Sigma_0\to\Sigma_1$, $N:\Sigma_1\to\Sigma_2$, $P:\Sigma_2\to\Sigma_3$, both $(P\circ N)\circ M$ and $P\circ(N\circ M)$ are the manifold obtained by gluing all three along $\Sigma_1$ and $\Sigma_2$. *Reason:* gluing along disjoint boundary components is independent of order, so the two triple-gluings are literally the same manifold; in particular homeomorphic, hence equal as arrows.
3. **Identity law.** $M\circ(\Sigma_0\times[0,1])$ glues a collar onto the incoming end of $M$. *Reason:* the collar neighborhood theorem gives a homeomorphism $M\cup(\Sigma_0\times[0,1])\cong M$ fixing the far boundary, so the composite equals $M$ as an arrow; likewise on the outgoing side.

Thus $\mathrm{Cob}(n)$ is a genuine category. It has one more crucial structure — *disjoint union* of manifolds, $\sqcup$ — which lets us "place cobordisms side by side." Formalizing side-by-side placement is the job of the next section.

> **Worked example — the toy category $\mathrm{Cob}(1)$.** Take $n=1$. The closed $0$-manifolds are finite sets of oriented points; write $+$ for a positively-oriented point and $-$ for a negatively-oriented one. The $1$-dimensional cobordisms are compact $1$-manifolds-with-boundary — disjoint unions of *intervals* and *circles*. Up to homeomorphism every such cobordism is built from four pieces: the identity interval $+\to+$, the "cup" $\mathrm{coev}:\varnothing\to(-{}+)$ (a $\cup$-shaped arc joining nothing to a $-,+$ pair), the "cap" $\mathrm{ev}:(+{}-)\to\varnothing$ (a $\cap$-shaped arc), and the circle $S^1:\varnothing\to\varnothing$. The single nontrivial relation is the *zigzag*: straightening an $\cup$ then $\cap$ arc gives a plain interval,
> $$
> (\mathrm{ev}\otimes 1)\circ(1\otimes\mathrm{coev})=1_{+}.
> $$
> We will see in §s3 that this very identity forces every TQFT state space to be finite-dimensional, and in §s10 that it is the defining equation of a *dualizable object*. The small category $\mathrm{Cob}(1)$ is already the cobordism hypothesis in miniature.

<a id="s2"></a>
### Monoidal and symmetric monoidal categories

**What & why.** Composition in $\mathrm{Cob}(n)$ glues cobordisms *end to end* (in "time"). But we can also set two cobordisms *side by side* (in "space") using disjoint union. A category with such a side-by-side operation, compatible with composition, is a **monoidal category**; if side-by-side order does not matter up to a coherent swap, it is **symmetric monoidal**. These are exactly the structures a TQFT must preserve.

First, the categorical vocabulary, restated so the guide stands alone.

> **Definition — category.**
> A **category** $\mathcal{C}$ consists of a collection of **objects**; for each pair of objects $A,B$ a set of **arrows** (morphisms) $\mathcal{C}(A,B)$; a **composition** $\circ:\mathcal{C}(B,C)\times\mathcal{C}(A,B)\to\mathcal{C}(A,C)$; and for each object $A$ an **identity** arrow $1_A\in\mathcal{C}(A,A)$, satisfying associativity $h\circ(g\circ f)=(h\circ g)\circ f$ and unit laws $1_B\circ f=f=f\circ 1_A$. *Example:* $\mathbf{Vect}_k$, with objects vector spaces over a field $k$ and arrows linear maps.

> **Definition — functor.**
> A **functor** $F:\mathcal{C}\to\mathcal{D}$ assigns to each object $A$ an object $F(A)$ and to each arrow $f:A\to B$ an arrow $F(f):F(A)\to F(B)$, preserving identities $F(1_A)=1_{F(A)}$ and composition $F(g\circ f)=F(g)\circ F(f)$. A functor is the precise notion of "structure-preserving map of categories" — it is what a TQFT *is*.

> **Definition — natural transformation and natural isomorphism.**
> Given functors $F,G:\mathcal{C}\to\mathcal{D}$, a **natural transformation** $\eta:F\Rightarrow G$ is a family of arrows $\eta_A:F(A)\to G(A)$, one per object, such that for every $f:A\to B$ the square commutes: $G(f)\circ\eta_A=\eta_B\circ F(f)$. If every $\eta_A$ is an isomorphism, $\eta$ is a **natural isomorphism**, written $F\cong G$. "Natural" means "uniform in $A$, with no arbitrary choices."

Now the side-by-side structure.

> **Definition — monoidal category.**
> A **monoidal category** is a category $\mathcal{C}$ equipped with:
> - a functor $\otimes:\mathcal{C}\times\mathcal{C}\to\mathcal{C}$ (the **tensor product**), sending $(A,B)\mapsto A\otimes B$;
> - a distinguished object $\mathbf{1}$ (the **unit**);
> - natural isomorphisms the **associator** $\alpha_{A,B,C}:(A\otimes B)\otimes C\xrightarrow{\sim}A\otimes(B\otimes C)$, and **unitors** $\lambda_A:\mathbf{1}\otimes A\xrightarrow{\sim}A$, $\rho_A:A\otimes\mathbf{1}\xrightarrow{\sim}A$;
>
> subject to two **coherence axioms**: the *pentagon* (the two ways of reassociating $((A\otimes B)\otimes C)\otimes D$ agree) and the *triangle* (the associator and unitors are compatible on $A\otimes\mathbf{1}\otimes B$).

The point of coherence, made into a theorem by Mac Lane, is that *all* such reassociations agree, so we may safely drop parentheses.

> **Theorem (Mac Lane coherence, stated).** In any monoidal category, every diagram built from $\alpha,\lambda,\rho$ and their inverses commutes. Consequently each monoidal category is equivalent to a *strict* one, where $\otimes$ is literally associative and unital and the structure isomorphisms are identities.

We will use coherence as a license to write $A\otimes B\otimes C$ without parentheses; the full proof is a long induction on the pentagon and is treated as background. A monoidal category lets us multiply objects; to *swap* two factors we need symmetry.

> **Definition — symmetric monoidal category.**
> A monoidal category is **symmetric** if it carries a natural isomorphism the **braiding** $\beta_{A,B}:A\otimes B\xrightarrow{\sim}B\otimes A$ satisfying:
> - **symmetry**: $\beta_{B,A}\circ\beta_{A,B}=1_{A\otimes B}$ (swapping twice does nothing);
> - **hexagon axioms**: $\beta$ is compatible with the associator (swapping past a tensor factor can be done one factor at a time).

> **Worked example — $(\mathbf{Vect}_k,\otimes,k)$.** Take the usual tensor product of vector spaces, unit $\mathbf{1}=k$ (the ground field as a $1$-dimensional space), associator the canonical $(U\otimes V)\otimes W\cong U\otimes(V\otimes W)$, unitors $k\otimes V\cong V$ via $c\otimes v\mapsto cv$, and braiding $\beta(v\otimes w)=w\otimes v$. Symmetry $\beta^2=1$ holds because swapping $v\otimes w\mapsto w\otimes v\mapsto v\otimes w$ returns the original. This is the *target* category of an ordinary TQFT.

> **Worked example — $(\mathrm{Cob}(n),\sqcup,\varnothing)$.** Disjoint union $\sqcup$ is the tensor product; the empty $(n-1)$-manifold $\varnothing$ is the unit (disjoint union with nothing changes nothing). The braiding $\beta_{\Sigma_0,\Sigma_1}$ is the cobordism $(\Sigma_0\sqcup\Sigma_1)\times[0,1]$ that *crosses the two cylinders over*, realizing the swap geometrically. Symmetry $\beta^2=1$ holds because in dimension $n-1\ge 1$ there is enough room to undo a crossing by a homeomorphism — this is why ordinary cobordism categories are *symmetric*, not merely *braided*. (In §s6 we shall meet $3$-dimensional structures where crossings *cannot* be undone, the source of knot invariants.) So $\mathrm{Cob}(n)$ is a symmetric monoidal category — the source of every TQFT.

Let us verify one coherence axiom by hand, to see that these conditions are concrete checks, not decoration.

> **Worked verification — the triangle axiom in $\mathbf{Vect}_k$.** The triangle axiom demands that the two ways of simplifying $A\otimes\mathbf{1}\otimes B$ agree:
> $$
> (1_A\otimes\lambda_B)\circ\alpha_{A,\mathbf{1},B}=\rho_A\otimes 1_B.
> $$
> Take $A=B=k^2$ and the unit $\mathbf 1=k$. Pick $a\otimes c\otimes b\in A\otimes k\otimes B$ with $a,b\in k^2$, $c\in k$. The associator $\alpha$ merely reparenthesizes, $a\otimes(c\otimes b)$; then $1_A\otimes\lambda_B$ sends $c\otimes b\mapsto cb$, giving $a\otimes(cb)$. The right side $\rho_A\otimes 1_B$ sends $a\otimes c\mapsto ca$, giving $(ca)\otimes b=a\otimes(cb)$ by bilinearity (scalars pass through $\otimes$). The two outputs are equal element-by-element, so the triangle commutes. *Reason it works:* both routes do the same arithmetic — multiply by the scalar $c$ once. This is the kind of bookkeeping Mac Lane coherence guarantees in *every* monoidal category at once.

<a id="s3"></a>
### The Atiyah–Segal axioms: a TQFT as a symmetric monoidal functor

**What & why.** We now have a source category $\mathrm{Cob}(n)$ (geometry) and a target category $\mathbf{Vect}_k$ (algebra), both symmetric monoidal. Atiyah's insight (following Segal's axioms for conformal field theory) is that a TQFT is nothing more nor less than a structure-preserving map between them. This single definition encodes "states, gluing, and side-by-side" all at once.

> **Definition — $n$-dimensional TQFT (Atiyah–Segal).**
> An **$n$-dimensional topological quantum field theory** over a field $k$ is a *symmetric monoidal functor*
> $$
> Z:\big(\mathrm{Cob}(n),\sqcup,\varnothing\big)\longrightarrow\big(\mathbf{Vect}_k,\otimes,k\big).
> $$
> Unwinding the words, $Z$ assigns:
> - to each closed oriented $(n-1)$-manifold $\Sigma$, a vector space $Z(\Sigma)$ (its **state space**);
> - to each cobordism $M:\Sigma_0\to\Sigma_1$, a linear map $Z(M):Z(\Sigma_0)\to Z(\Sigma_1)$ (its **amplitude** or **transition map**);
>
> subject to the following axioms, each of which is exactly one clause of "symmetric monoidal functor."

> **The axioms unpacked.**
> 1. **Functoriality (gluing).** $Z(N\circ M)=Z(N)\circ Z(M)$ and $Z(\Sigma\times[0,1])=1_{Z(\Sigma)}$. *Meaning:* the invariant of a glued manifold is the composite of the pieces' maps; the cylinder does nothing. This is the gluing law.
> 2. **Monoidality (disjoint union).** A natural isomorphism $Z(\Sigma_0\sqcup\Sigma_1)\cong Z(\Sigma_0)\otimes Z(\Sigma_1)$ and $Z(\varnothing)\cong k$. *Meaning:* side-by-side becomes tensor product; the empty manifold gets the ground field.
> 3. **Symmetry.** $Z$ intertwines the swap cobordism with the swap of vector spaces: $Z(\beta_{\Sigma_0,\Sigma_1})=\beta_{Z(\Sigma_0),Z(\Sigma_1)}$.

Two consequences follow immediately and are worth recording because they are how TQFTs produce *numbers*.

> **Closed manifolds give numbers.** A *closed* oriented $n$-manifold $X$ has empty boundary, so it is a cobordism $X:\varnothing\to\varnothing$. Hence
> $$
> Z(X):Z(\varnothing)\to Z(\varnothing),\qquad\text{i.e.}\qquad Z(X):k\to k,
> $$
> which is multiplication by a scalar $Z(X)\in k$. *Reason:* a linear map $k\to k$ is determined by where it sends $1$. This scalar is the numerical invariant of $X$. By functoriality it is computed by cutting $X$ into cobordisms and composing the resulting maps — invariants from gluing, made literal.

> **State spaces are finite-dimensional.** For each closed $\Sigma$, the vector space $Z(\Sigma)$ is finite-dimensional. *Proof:* Let $C=\Sigma\times[0,1]$, the cylinder. As a cobordism it can be re-read in two ways: as the identity $\Sigma\to\Sigma$, and — by bending it — as a cobordism $\varnothing\to\Sigma\sqcup\overline{\Sigma}$ (the "cup," call its image $\mathrm{coev}$) followed in another bend by $\Sigma\sqcup\overline{\Sigma}\to\varnothing$ (the "cap," call it $\mathrm{ev}$). The *S-diagram* (zigzag) identity $(\mathrm{ev}\otimes 1)\circ(1\otimes\mathrm{coev})=1_\Sigma$, which holds as a homeomorphism of cobordisms (straightening a zigzag), forces $Z(\Sigma)$ to be a *dualizable* object of $\mathbf{Vect}_k$. *Reason:* a vector space is dualizable in $(\mathbf{Vect}_k,\otimes)$ if and only if it is finite-dimensional — the coevaluation $k\to V\otimes V^\ast$, $1\mapsto\sum e_i\otimes e_i^\ast$, exists only with a finite basis. Hence $\dim Z(\Sigma)<\infty$. This single argument is the seed of the cobordism hypothesis (§s9).

> **Intuition and pitfalls.** *Intuition:* think of $Z(\Sigma)$ as the Hilbert space of a quantum system living on the spatial slice $\Sigma$, and $Z(M)$ as the time-evolution operator for the spacetime $M$ — except the "evolution" depends only on topology. *Pitfall 1:* the gluing axiom requires the gluing to match orientations; reversing an end requires $\overline{\Sigma}$, whose state space is the *dual* $Z(\Sigma)^\ast$. *Pitfall 2:* finite-dimensionality is forced, not assumed; theories that want infinite-dimensional state spaces (most of "real" quantum field theory) are *not* topological.

> **Worked example — the trivial $1$d TQFT, computed end to end.** Let $n=1$, so $\mathrm{Cob}(1)$ is the toy category of §s1. Define $Z$ by $Z(+)=V$ for a fixed finite-dimensional space $V=k^d$ and $Z(-)=V^\ast$, with $Z(\mathrm{coev})=\mathrm{coev}:k\to V\otimes V^\ast$, $1\mapsto\sum_i e_i\otimes e_i^\ast$, and $Z(\mathrm{ev})=\mathrm{ev}:V^\ast\otimes V\to k$, $f\otimes v\mapsto f(v)$. The closed $1$-manifold is the circle $S^1:\varnothing\to\varnothing$, obtained by gluing a cup to a cap, so
> $$
> Z(S^1)=\mathrm{ev}\circ\mathrm{coev}:k\to k,\qquad 1\mapsto \mathrm{ev}\Big(\sum_i e_i\otimes e_i^\ast\Big)=\sum_i e_i^\ast(e_i)=\sum_i 1=d .
> $$
> So the circle's invariant is $Z(S^1)=d=\dim V$ — the categorical *trace of the identity*. With $V=k^3$ we get the number $3$. This is the smallest nontrivial instance of "invariants from gluing": a number ($\dim V$) extracted by composing a cup and a cap, the whole computation forced by the zigzag relation of §s1.

The definition is elegant but abstract. The next two sections make it utterly concrete in dimension two, where a TQFT turns out to be a single, small algebraic gadget.

## Part B — Dimension two: the complete classification

<a id="s4"></a>
### Two-dimensional TQFTs equal commutative Frobenius algebras

**What & why.** In dimension $n=2$ the source category $\mathrm{Cob}(2)$ has a *complete and explicit* description: every closed $1$-manifold is a disjoint union of circles, and every surface-with-boundary is built by gluing a handful of standard pieces. This makes it possible to classify *all* $2$d TQFTs. The answer is a perfect dictionary: a $2$d TQFT is the same thing as a **commutative Frobenius algebra**. We state the theorem, define the algebra, and prove the equivalence.

> **Definition — algebra (over a field $k$).**
> An **algebra** is a vector space $A$ over $k$ with a bilinear **multiplication** $m:A\otimes A\to A$ and a **unit** $u:k\to A$ (picking out $1=u(1)$) such that $m$ is associative, $m\circ(m\otimes 1)=m\circ(1\otimes m)$, and unital, $m\circ(u\otimes 1)=1_A=m\circ(1\otimes u)$. It is **commutative** if $m\circ\beta=m$, where $\beta$ swaps the two factors.

> **Definition — coalgebra.**
> Dually, a **coalgebra** has a **comultiplication** $\Delta:A\to A\otimes A$ and a **counit** $\varepsilon:A\to k$ that are coassociative and counital — the same diagrams with all arrows reversed.

> **Definition — Frobenius algebra.**
> A **Frobenius algebra** over $k$ is a vector space $A$ that is simultaneously an algebra $(m,u)$ and a coalgebra $(\Delta,\varepsilon)$, such that the **Frobenius relation** holds:
> $$
> (m\otimes 1)\circ(1\otimes\Delta)\;=\;\Delta\circ m\;=\;(1\otimes m)\circ(\Delta\otimes 1).
> $$
> Equivalently and more concretely, a Frobenius algebra is a finite-dimensional algebra $A$ equipped with a linear functional $\varepsilon:A\to k$ (the **counit** or **trace**) whose associated pairing
> $$
> \langle a,b\rangle:=\varepsilon(m(a,b))=\varepsilon(ab)
> $$
> is **nondegenerate** (if $\langle a,b\rangle=0$ for all $b$ then $a=0$). It is **commutative** if its multiplication is commutative. The two descriptions agree: given $\varepsilon$ with nondegenerate pairing, one *defines* $\Delta$ as the unique map making the Frobenius relation hold; conversely $\Delta,\varepsilon$ recover the pairing.

> **Theorem (Dijkgraaf; the 2d TQFT classification).**
> There is an equivalence of categories
> $$
> \{\,2\text{d TQFTs over }k\,\}\;\simeq\;\{\,\text{commutative Frobenius algebras over }k\,\}.
> $$
> Concretely, a $2$d TQFT $Z$ determines the commutative Frobenius algebra $A=Z(S^1)$, and conversely every commutative Frobenius algebra arises from a unique (up to isomorphism) $2$d TQFT.

We prove both directions. The proof rests on a generators-and-relations presentation of $\mathrm{Cob}(2)$.

> **Lemma (presentation of $\mathrm{Cob}(2)$).** Every object of $\mathrm{Cob}(2)$ is a disjoint union of circles, so it is determined by a number $\ge 0$ of circles; thus objects are the natural numbers under $\sqcup=+$. Every connected oriented surface-with-boundary is, up to homeomorphism, a sphere with some incoming holes, some outgoing holes, and $g$ handles, and every such surface is a composite of disjoint unions of the five **generating cobordisms**:
> $$
> \underbrace{S^1\!\sqcup S^1\to S^1}_{\text{pair of pants }m},\quad
> \underbrace{\varnothing\to S^1}_{\text{cap }u},\quad
> \underbrace{S^1\to S^1\!\sqcup S^1}_{\text{copants }\Delta},\quad
> \underbrace{S^1\to\varnothing}_{\text{cup }\varepsilon},\quad
> \underbrace{S^1\to S^1}_{\text{twist }\beta}.
> $$
> The relations among them are exactly: associativity and unit (for $m,u$), coassociativity and counit (for $\Delta,\varepsilon$), commutativity (the twist), and the Frobenius relation.

*Why the lemma holds (sketch with the key step).* This is *Morse theory* applied to the height function on a surface. Choose a smooth real function $h:M\to[0,1]$ with $h^{-1}(0)=\Sigma_0$, $h^{-1}(1)=\Sigma_1$, and only nondegenerate critical points at distinct heights (a *Morse function*; one always exists). As $t$ increases through $[0,1]$, the level set $h^{-1}(t)$ is a disjoint union of circles that changes only when $t$ passes a critical point. Each critical point of a $2$-manifold has *index* $0$, $1$, or $2$, and the elementary surface created there is:
- index $0$: a new circle is born — the **cap** $u:\varnothing\to S^1$;
- index $1$ joining two circles: the **pair of pants** $m:S^1\sqcup S^1\to S^1$ (or, read the other way, the **copants** $\Delta$);
- index $2$: a circle dies — the **cup** $\varepsilon:S^1\to\varnothing$.

So slicing $M$ between consecutive critical levels writes it as a composite of these elementary pieces tensored with identity cylinders. That the *relations* are exactly the listed ones is the substance of the *classification of surfaces* and *Cerf theory* (which controls how the decomposition changes when the Morse function is varied); the relations are precisely the moves that relate two Morse decompositions of the same surface. We take this presentation as established and proceed to the equivalence.

**Proof of the theorem.**

*Direction 1: a TQFT gives a commutative Frobenius algebra.* Let $Z$ be a $2$d TQFT and set $A:=Z(S^1)$.

1. $A$ is finite-dimensional, by the dualizability argument of §s3 (*reason:* the bent cylinder forces $S^1$'s state space to be dualizable, hence finite-dimensional).
2. Define $m:=Z(\text{pants}):A\otimes A\to A$, $u:=Z(\text{cap}):k\to A$, $\Delta:=Z(\text{copants}):A\to A\otimes A$, $\varepsilon:=Z(\text{cup}):A\to k$. Each is a linear map because $Z$ sends cobordisms to linear maps (*reason:* $Z$ is a functor into $\mathbf{Vect}_k$); the monoidal structure converts $S^1\sqcup S^1$ into $A\otimes A$ and $\varnothing$ into $k$ (*reason:* $Z$ is monoidal).
3. **Associativity of $m$.** The two surfaces $\text{(pants)}\circ\text{(pants}\sqcup\text{id)}$ and $\text{(pants)}\circ\text{(id}\sqcup\text{pants)}$ are *the same* surface up to homeomorphism — both are a sphere with three incoming holes and one outgoing hole. Applying $Z$ and using functoriality and monoidality gives $m\circ(m\otimes 1)=m\circ(1\otimes m)$. *Reason:* $Z$ preserves composition and tensor, and assigns equal maps to homeomorphic cobordisms.
4. **Unit law.** Gluing a cap to one leg of the pants yields a cylinder (a disc-with-tube straightens to a tube). Hence $m\circ(u\otimes 1)=Z(\text{cylinder})=1_A$. *Reason:* $Z(\Sigma\times[0,1])=1_{Z(\Sigma)}$.
5. **Commutativity.** The pants precomposed with the twist cobordism equals the pants (you can rotate two incoming legs around each other within the surface). So $m\circ\beta=m$, where $\beta$ is the symmetry of $\mathbf{Vect}_k$ because $Z$ is *symmetric* monoidal. *Reason:* symmetry axiom of §s3.
6. **Coalgebra laws** follow identically from the upside-down surfaces (copants and cup), since turning every surface upside-down is a homeomorphism that swaps incoming/outgoing.
7. **Frobenius relation.** The surface "$\Delta$ then $m$" and the surface "$m$ then $\Delta$ run around one leg" are the same genus-zero, two-in two-out surface; applying $Z$ gives $\Delta\circ m=(m\otimes 1)\circ(1\otimes\Delta)$. *Reason:* equal cobordisms map to equal linear maps.
8. **Nondegeneracy.** The pairing $\langle a,b\rangle=\varepsilon(m(a,b))=Z(\text{cup}\circ\text{pants})$ is realized by the cobordism $S^1\sqcup S^1\to\varnothing$, the "pair of pants capped off." The bent-cylinder zigzag identity (the snake), valid as a homeomorphism, shows this pairing has the copants-cap as its inverse copairing $k\to A\otimes A$; a pairing with a two-sided dual copairing is nondegenerate. *Reason:* dualizability in $\mathbf{Vect}_k$ is nondegeneracy of the pairing.

Hence $A=Z(S^1)$ is a commutative Frobenius algebra.

*Direction 2: a commutative Frobenius algebra gives a TQFT.* Given $(A,m,u,\Delta,\varepsilon)$, define $Z(S^1)=A$, $Z(\bigsqcup_k S^1)=A^{\otimes k}$, $Z(\varnothing)=k$, and on the five generators send pants$\mapsto m$, cap$\mapsto u$, copants$\mapsto\Delta$, cup$\mapsto\varepsilon$, twist$\mapsto\beta$.

1. This *extends to a functor* because $\mathrm{Cob}(2)$ is *generated by these five arrows subject to exactly the algebra axioms* (the Lemma). *Reason:* by the universal property of a generators-and-relations presentation, a functor out of $\mathrm{Cob}(2)$ is the same as an assignment of the generators satisfying the relations — and the relations are precisely the Frobenius algebra axioms, which $A$ satisfies by hypothesis.
2. It is *monoidal* by construction ($\sqcup\mapsto\otimes$) and *symmetric* because we sent the twist to $\beta$, and commutativity of $A$ ensures the symmetry axiom.
3. *Uniqueness:* any two functors agreeing on the generators agree everywhere, since every arrow is a composite of generators. *Reason:* functoriality determines $Z$ on composites from its values on generators.

The two constructions are mutually inverse: starting from $Z$, reading off $A$, and rebuilding the functor returns $Z$ (they agree on generators); starting from $A$, building $Z$, and reading off $Z(S^1)$ returns $A$. Both are functorial in the obvious maps, giving the claimed equivalence of categories. $\qquad\blacksquare$

> **Worked decomposition — the torus as a composite of generators.** Read the torus $T^2$ as a cobordism $\varnothing\to\varnothing$. Slice it by height into four elementary pieces, bottom to top: a **cap** $u:\varnothing\to S^1$ (the bottom of the torus, a born circle), then a **copants** $\Delta:S^1\to S^1\sqcup S^1$ (the circle splits into two as we pass the lower handle), then a **pants** $m:S^1\sqcup S^1\to S^1$ (the two circles rejoin), then a **cup** $\varepsilon:S^1\to\varnothing$ (the top, a circle that dies). Hence
> $$
> T^2=\varepsilon\circ m\circ\Delta\circ u\;:\;\varnothing\to\varnothing,
> $$
> and applying $Z$ gives $Z(T^2)=\varepsilon\circ m\circ\Delta\circ u=\varepsilon\big(H(u(1))\big)$ with $H=m\circ\Delta$ — exactly the handle operator of §s5. This single decomposition is the geometric reason behind the genus formula: each handle contributes one factor of $H$, sandwiched between the birth $u$ and death $\varepsilon$ of a circle.

> **Pitfall.** *Commutativity is essential and comes from the symmetry of $\mathrm{Cob}(2)$.* If one studied *non-commutative* Frobenius algebras one would be describing surfaces with extra structure (e.g. a chosen ordering of boundary circles, as in *open* TQFTs). The clean statement "$2$d closed TQFT $=$ commutative Frobenius algebra" needs the symmetric structure.

<a id="s5"></a>
### Frobenius algebras and the pair-of-pants product/coproduct — a worked example

**What & why.** The classification of §s4 is only useful if we can *compute* with it. Here we work a complete numerical example: a specific commutative Frobenius algebra, its pants-product and copants-coproduct, and the resulting invariants of closed surfaces — including the beautiful formula $Z(\Sigma_g)=\dim A$ raised to a genus-dependent power for one natural choice.

> **The genus formula.** For a $2$d TQFT $Z$ with Frobenius algebra $A$, the invariant of the closed orientable surface $\Sigma_g$ of genus $g$ (a sphere with $g$ handles) is, for $g\ge 1$,
> $$
> Z(\Sigma_g)=\mathrm{tr}\!\big(H^{\,g-1}\big),\quad H:=m\circ\Delta:A\to A,
> $$
> where $H=m\circ\Delta$ is the **handle operator**, while the sphere is $Z(\Sigma_0)=\varepsilon\circ u=\varepsilon(u(1))$. *Why:* a genus-$g$ surface read as $\varnothing\to\varnothing$ is a cap $u$, then $g$ handles (each handle is "copants then pants," i.e. $H$), then a cup $\varepsilon$, giving the scalar $\varepsilon\circ H^{g}\circ u$; the cap-then-cup pair contributes one cylinder's worth of nondegenerate pairing, so for $g\ge 1$ this collapses to $\mathrm{tr}(H^{g-1})$. In particular the torus ($g=1$) gives $Z(\Sigma_1)=\mathrm{tr}(H^0)=\mathrm{tr}(1_A)=\dim A$, as the torus partition function must.

> **Worked example — group algebra of $\mathbb{Z}/2$.** Let $A=k[\mathbb{Z}/2]=k\{1,t\}$ with $t^2=1$, over $k=\mathbb{C}$. This is a commutative algebra of dimension $2$, with unit $u(1)=1$ and multiplication
> $$
> 1\cdot 1=1,\quad 1\cdot t=t,\quad t\cdot t=1.
> $$
> Define the counit (trace) by $\varepsilon(1)=0$, $\varepsilon(t)=1$ — chosen so the pairing is nondegenerate, as we verify.

Step 1 — **the pairing matrix.** With basis $\{1,t\}$,
$$
\langle 1,1\rangle=\varepsilon(1)=0,\quad \langle 1,t\rangle=\varepsilon(t)=1,\quad \langle t,t\rangle=\varepsilon(t^2)=\varepsilon(1)=0.
$$
So the Gram matrix is $\begin{pmatrix}0&1\\1&0\end{pmatrix}$, determinant $-1\ne 0$: the pairing is **nondegenerate**, confirming $(A,\varepsilon)$ is Frobenius. *(Reason: nondegeneracy $\iff$ invertible Gram matrix.)*

Step 2 — **the coproduct $\Delta$.** $\Delta$ is determined by the Frobenius relation; equivalently $\Delta(x)=\sum_i (x e^i)\otimes e_i$ where $\{e_i\},\{e^i\}$ are *dual bases* for the pairing. The dual basis to $\{1,t\}$ under the Gram matrix above is $\{e^1=t,\ e^t=1\}$ (since $\langle 1,t\rangle=1$, etc.). Then
$$
\Delta(1)=\sum_i e^i\otimes e_i=t\otimes 1+1\otimes t,\qquad
\Delta(t)=\sum_i (t\,e^i)\otimes e_i=(t\cdot t)\otimes1+(t\cdot1)\otimes t=1\otimes 1+t\otimes t.
$$

Step 3 — **the handle operator $H=m\circ\Delta$.**
$$
H(1)=m(t\otimes1+1\otimes t)=t+t=2t,\qquad
H(t)=m(1\otimes1+t\otimes t)=1+1=2\cdot 1.
$$
So in the basis $\{1,t\}$, $H=\begin{pmatrix}0&2\\2&0\end{pmatrix}$.

Step 4 — **surface invariants.** The sphere $\Sigma_0$: $Z(\Sigma_0)=\varepsilon(u(1))=\varepsilon(1)=0$. The torus $\Sigma_1$: $Z(\Sigma_1)=\mathrm{tr}(H^0)=\mathrm{tr}(1_A)=\dim A=2$, as it must. The genus-two surface: $Z(\Sigma_2)=\mathrm{tr}(H)=0$. The genus-three surface: $Z(\Sigma_3)=\mathrm{tr}(H^2)$, and $H^2=\begin{pmatrix}4&0\\0&4\end{pmatrix}$ so $\mathrm{tr}(H^2)=8$. In general $\mathrm{tr}(H^{g-1})=2^{g-1}\big(1+(-1)^{g-1}\big)$, since $H$ has eigenvalues $\pm 2$; thus $Z(\Sigma_g)=2^{g}$ for odd $g$ and $0$ for even $g$. These are genuine homeomorphism invariants of the surfaces, computed purely algebraically — invariants from gluing in action.

> **A cleaner choice — semisimple algebras and counting.** If instead one takes $A=k^N$ (the product algebra, $N$ orthogonal idempotents $e_1,\dots,e_N$ with $e_ie_j=\delta_{ij}e_i$) and $\varepsilon(e_i)=1/\theta_i$ for nonzero scalars $\theta_i$, then $H=m\circ\Delta$ acts on $e_i$ by multiplication by $\theta_i$, and
> $$
> Z(\Sigma_g)=\sum_{i=1}^{N}\theta_i^{\,g-1}.
> $$
> When all $\theta_i=1$ this is just $N$ for every genus — the simplest possible TQFT, "count the components of the value algebra." This is the algebraic shadow of *Dijkgraaf–Witten theory* for a finite group, where $\theta_i$ are sizes of conjugacy-class data.

> **Intuition and pitfalls.** *Intuition:* the pants is "merge two states into one" (a product), the copants is "split one state into a superposition" (a coproduct), and a handle is "split then re-merge," which is why $H=m\circ\Delta$. *Pitfall:* the coproduct is *not* a free choice — it is forced by the algebra plus the trace; changing $\varepsilon$ changes $\Delta$, $H$, and all the surface invariants, so the *trace is part of the data*, not an afterthought.

## Part C — Higher dimensions and quantum invariants

<a id="s6"></a>
### Three-dimensional TQFT and modular tensor categories; Reshetikhin–Turaev and Witten–Chern–Simons

**What & why.** In dimension three the story is far richer than a single algebra. The state spaces $Z(\Sigma)$ are attached to surfaces, the linear maps to $3$-manifolds, and — crucially — the gluing data is now controlled not by a Frobenius algebra but by a whole *category* of "labels," a **modular tensor category**. Two landmark constructions realize this: the *algebraic* Reshetikhin–Turaev construction and the *physical* Witten–Chern–Simons construction. We survey both.

> **Definition — ribbon / modular tensor category (informal but precise enough).**
> A **(braided) tensor category** is a category $\mathcal{C}$ with a tensor product $\otimes$, a unit object $\mathbf{1}$, and a *braiding* $\beta_{X,Y}:X\otimes Y\to Y\otimes X$ that need *not* satisfy $\beta^2=1$ (so swapping twice can be nontrivial — the source of knotting). A **ribbon category** adds compatible duals $X^\ast$ and a *twist* $\theta_X:X\to X$. A **modular tensor category (MTC)** is a ribbon category that is *semisimple* with finitely many simple objects $\{X_0=\mathbf{1},X_1,\dots,X_r\}$ such that the **$S$-matrix** $S_{ij}=\mathrm{tr}(\beta_{X_j,X_i}\circ\beta_{X_i,X_j})$ (the "double braiding trace," a Hopf-link invariant) is *invertible*. Invertibility of $S$ is the "modularity" — it is exactly what makes the gluing data of $3$-manifolds consistent.

> **Theorem (Reshetikhin–Turaev, stated).** Every modular tensor category $\mathcal{C}$ produces a $3$-dimensional TQFT $Z_{\mathcal{C}}$. It assigns:
> - to a closed surface $\Sigma$ with marked points labeled by simple objects, a finite-dimensional vector space $Z_{\mathcal{C}}(\Sigma)$ — the **space of conformal blocks**;
> - to a $3$-manifold (with embedded labeled ribbon graph), a linear map, computed combinatorially from a *surgery presentation* of the manifold using the $S$- and $T$-matrices of $\mathcal{C}$.
>
> In particular every closed $3$-manifold $M$ gets a numerical invariant $Z_{\mathcal{C}}(M)\in\mathbb{C}$.

The mechanism deserves one sentence of explanation: any closed $3$-manifold can be obtained from $S^3$ by *surgery* along a framed link (Lickorish–Wallace theorem), and the Reshetikhin–Turaev recipe assigns to that link a number using the MTC, normalized so that the two *Kirby moves* relating different surgery presentations of the *same* manifold leave the number unchanged — which is exactly where modularity (invertibility of $S$) is used.

> **Witten–Chern–Simons (physics origin).** Witten constructed the *same* $3$d invariants from a quantum field theory: the **Chern–Simons** theory for a compact gauge group $G$ (say $G=SU(2)$) at integer **level** $k$. Its action on a $3$-manifold $M$ with connection $A$ is
> $$
> S_{\mathrm{CS}}[A]=\frac{k}{4\pi}\int_M \mathrm{tr}\!\Big(A\wedge dA+\tfrac{2}{3}A\wedge A\wedge A\Big).
> $$
> The partition function $Z(M)=\int \mathcal{D}A\,e^{iS_{\mathrm{CS}}[A]}$ is *metric-independent* (the action uses no metric, only the orientation), hence a topological invariant. Its mathematical incarnation is the Reshetikhin–Turaev invariant for the MTC of $SU(2)_k$ — the representations of the corresponding quantum group / affine Lie algebra at level $k$.

> **The dictionary in dimension three.**
> $$
> \{\text{3d TQFTs (suitably framed)}\}\;\longleftrightarrow\;\{\text{modular tensor categories}\},
> $$
> the dimension-three analogue of "$2$d TQFT $=$ commutative Frobenius algebra." The jump in complexity — from an *algebra* to a *category* — is the first sign of the higher-categorical pattern that §s8–s10 make precise: as dimension rises, the controlling algebraic object climbs one categorical level.

> **The $S$ and $T$ matrices and the Verlinde formula.** The two finite matrices that drive every computation are the **$S$-matrix** (above) and the **$T$-matrix** $T_{ij}=\delta_{ij}\theta_i$, recording the twist (topological spin) $\theta_i$ of each simple object. They give a projective representation of the *mapping class group of the torus* $SL(2,\mathbb{Z})$, because that group is generated by two moves $S$ (swap the two cycles of the torus) and $T$ (Dehn twist) subject to $(ST)^3=S^2$ and $S^2=$ charge conjugation. The single most useful consequence is the **Verlinde formula**, expressing the fusion multiplicities purely through $S$:
> $$
> N_{ij}^{\,k}=\sum_{m}\frac{S_{im}\,S_{jm}\,\overline{S_{km}}}{S_{0m}} .
> $$
> *Reading:* the integers counting "how many ways anyons $i,j$ fuse to $k$" are computed by *diagonalizing braiding*. This is the $3$d analogue of how, in §s5, the handle operator $H$ diagonalized the genus formula — fusion and gluing are the same diagonalization, one categorical level up.

> **Worked touchpoint — the torus state count $\dim Z(T^2)$.** For any MTC, $\dim Z(\Sigma_g)$ for the genus-$g$ surface is again a *Verlinde number*; in the simplest case the torus gives
> $$
> \dim Z(T^2)=\#\{\text{simple objects}\}=r+1 .
> $$
> For the $SU(2)_k$ theory there are $k+1$ simple objects (spins $0,\tfrac12,\dots,\tfrac k2$), so $\dim Z(T^2)=k+1$. At $k=1$ (the simplest nonabelian-adjacent case) this is $2$; at $k=2$ it is $3$ — matching the three ground states of the $\nu=1/3$ quantum-Hall–type theory mentioned in §s11. The state count is literally the number of anyon types, the cleanest possible "topological invariant equals algebraic count."

> **Pitfall.** $3$d TQFTs are *not* symmetric — they are only *braided*, because in three dimensions two strands genuinely link and cannot be unlinked by a homeomorphism. This non-symmetry is not a defect: it is *the whole point*, because it is what lets the theory detect knotting, as we see next.

<a id="s7"></a>
### Quantum invariants of knots and 3-manifolds; the Jones polynomial from Chern–Simons

**What & why.** A **knot** is an embedding of the circle $S^1$ into $S^3$ (a closed loop in space), considered up to ambient isotopy (deforming without cutting). Telling knots apart is hard; *quantum invariants* from $3$d TQFT give powerful, computable knot polynomials, the most famous being the **Jones polynomial**. We explain how a TQFT produces it.

> **The construction.** Place a knot (or link) $L$ inside $S^3$ and *label its strands* by a chosen simple object $X$ of an MTC $\mathcal{C}$ (for the Jones polynomial: the $2$-dimensional fundamental representation of $SU(2)_k$). The Reshetikhin–Turaev functor reads the link diagram bottom-to-top as a composite of elementary tangles — *cups*, *caps*, and *crossings* — and assigns:
> - a cup/cap $\mapsto$ the duality maps $\mathrm{coev}_X,\mathrm{ev}_X$;
> - a positive crossing $\mapsto$ the braiding $\beta_{X,X}$; a negative crossing $\mapsto$ $\beta_{X,X}^{-1}$.
>
> The resulting scalar $J(L)\in\mathbb{C}$ is an isotopy invariant of $L$ because the braiding and duals satisfy exactly the relations (the *Reidemeister moves*) that relate any two diagrams of the same knot.

> **The skein relation.** For the $SU(2)_2$-type braiding the operator $\beta=\beta_{X,X}$ on $X\otimes X$ (a $4$-dimensional space) satisfies a quadratic minimal polynomial,
> $$
> \beta - \beta^{-1} = (q^{1/2}-q^{-1/2})\,\mathrm{id},\qquad q=e^{2\pi i/(k+2)} .
> $$
> Translated into pictures with $A=q^{1/4}$, this is the **Kauffman/Jones skein relation**
> $$
> A\,J(L_+)-A^{-1}J(L_-)=(A^2-A^{-2})\,J(L_0),
> $$
> where $L_+,L_-,L_0$ are three links identical except at one crossing (over, under, smoothed). Together with the normalization $J(\text{unknot})=1$, this recursion *computes* $J$ for any link.

> **Worked example — the Hopf link.** The Hopf link $H$ is two circles linked once. Resolve one crossing with the skein relation: smoothing gives the unknot (value $1$ up to the loop factor), the other resolution gives two unlinked circles (value $\delta=-A^2-A^{-2}$, the *loop value*). Carrying out the recursion,
> $$
> J(\text{Hopf}^+) = -A^4-A^{-4},
> $$
> a Laurent polynomial in $A$ that is *different* for the two distinct Hopf links of opposite linking (so it detects the linking, which no abelian invariant like homology can do for the link complement directly). For comparison the *trefoil* knot evaluates, with the substitution $t=A^{-4}$, to the classical Jones polynomial $J=V(t)=-t^{-4}+t^{-3}+t^{-1}$; written in $A$ this same polynomial is $J=-A^{16}+A^{12}+A^{4}$ (using $t^{-1}=A^4,\ t^{-3}=A^{12},\ t^{-4}=A^{16}$), which differs from its mirror image — proving the trefoil is *chiral* (not the same as its reflection), a fact the Jones polynomial detects and the older Alexander polynomial cannot.

> **The Reidemeister moves, made precise.** That $J(L)$ is a knot invariant rests on the *Reidemeister theorem*: two link diagrams represent isotopic links iff one is obtained from the other by a finite sequence of three local moves — **R1** (add/remove a kink), **R2** (slide one strand over another, creating/cancelling two opposite crossings), **R3** (slide a strand past a crossing). The TQFT assignment respects exactly these: **R2** holds because $\beta\circ\beta^{-1}=\mathrm{id}$ (the braiding is invertible); **R3** holds because the braiding satisfies the *Yang–Baxter equation* $(\beta\otimes 1)(1\otimes\beta)(\beta\otimes 1)=(1\otimes\beta)(\beta\otimes 1)(1\otimes\beta)$, the algebraic form of "slide past a crossing"; **R1** holds *up to a framing twist* $\theta_X$, which is why the *framed* invariant is the canonical one. Each Reidemeister move is matched by one ribbon-category axiom — the cleanest possible dictionary between pictures and algebra.

> **From knots to $3$-manifolds.** Combining §s6 and §s7: surgery on a framed link $L\subset S^3$ produces a $3$-manifold $M_L$, and summing the link invariant $J$ over all labelings, weighted by quantum dimensions, gives the Reshetikhin–Turaev $3$-manifold invariant $Z_{\mathcal{C}}(M_L)$. So one machine — the MTC — produces *both* knot polynomials and $3$-manifold invariants, unified by the gluing/surgery picture.

> **Intuition and pitfalls.** *Intuition:* a knot invariant is the "amplitude" for a loop of charge $X$ tracing out a worldline in topological spacetime; crossings are braiding events. *Pitfall:* the invariant depends on the *framing* of the knot (a choice of normal direction), shifting by powers of the twist $\theta_X$ under a change of framing; the Jones polynomial is the canonically-framed normalization. *Pitfall 2:* the Jones polynomial is a complete invariant for *neither* knots nor links — distinct knots can share it — but it is strong, computable, and historically the bridge from operator algebras (Jones's original route) to TQFT (Witten's).

## Part D — Higher categories and the cobordism hypothesis

<a id="s8"></a>
### Higher categories — the idea of $n$-categories and $(\infty,n)$-categories

**What & why.** Sections s4 and s6 revealed a pattern: the algebra controlling an $n$d TQFT climbs a categorical level as $n$ grows (a Frobenius *algebra* in $2$d, a modular *category* in $3$d). To organize this — and to make TQFTs that remember *all* the gluing data, including how to cut surfaces *and* the cuts of those cuts — we need **higher categories**, where there are morphisms between morphisms, and so on.

> **Definition — the idea of an $n$-category.**
> An ordinary category (a **$1$-category**) has objects and morphisms (call them **$1$-morphisms**) between objects. A **$2$-category** adds **$2$-morphisms**: morphisms *between $1$-morphisms*. Concretely, between two objects $A,B$ there is now not a *set* of arrows but a *category* $\mathcal{C}(A,B)$, whose objects are $1$-morphisms $A\to B$ and whose morphisms are $2$-morphisms. Iterating, an **$n$-category** has objects, $1$-morphisms, $2$-morphisms, …, up to $n$-morphisms, with composition at each level, coherently associative and unital.
>
> *Prototype:* the $2$-category $\mathbf{Cat}$ has categories as objects, functors as $1$-morphisms, and natural transformations as $2$-morphisms.

The bookkeeping of "coherently associative" becomes severe as $n$ grows: the associativity that held *on the nose* in a $1$-category should hold only *up to a $2$-isomorphism*, which must itself satisfy coherences up to $3$-isomorphisms, etc. Managing this honestly leads to the notion of a *weak* $n$-category, and in the limit to:

> **Definition — $(\infty,n)$-category (idea).**
> An **$(\infty,n)$-category** has morphisms of every level $1,2,3,\dots$, but all $k$-morphisms for $k>n$ are *invertible* (up to higher morphisms). So it has non-invertible structure only up to level $n$, and above that level everything is a coherent system of equivalences. The case $n=0$ recovers an **$\infty$-groupoid**, which — by Grothendieck's *homotopy hypothesis* — is the same as a *topological space up to homotopy*: objects are points, $1$-morphisms are paths, $2$-morphisms are homotopies of paths, and so on, all invertible.

> **Why this is the right setting for TQFT.** An *extended* TQFT (§s9) wants to assign data to manifolds of *every* dimension from $0$ up to $n$ at once: a number to an $n$-manifold, a vector space to an $(n-1)$-manifold, a category to an $(n-2)$-manifold, …, up to an $(n{-}1)$-category to a point. The natural home for "manifolds of all codimensions, with cobordisms between cobordisms between …" is an *$(\infty,n)$-category of cobordisms*, $\mathrm{Bord}_n$ (§s9). Higher categories are not a luxury here — they are forced by the desire to cut in every dimension.

> **Worked example — composition in the $2$-category $\mathbf{Cat}$.** Let $A,B,C$ be categories, $F,F':A\to B$ and $G,G':B\to C$ functors, and $\alpha:F\Rightarrow F'$, $\beta:G\Rightarrow G'$ natural transformations. There are now *two* ways to compose. **Vertical** composition stacks $2$-morphisms with the *same* source and target $1$-morphisms: if also $\alpha':F'\Rightarrow F''$, then $(\alpha'\cdot\alpha)_a=\alpha'_a\circ\alpha_a$ component-wise. **Horizontal** composition combines $2$-morphisms along a shared object: $(\beta*\alpha)_a=G'(\alpha_a)\circ\beta_{F(a)}=\beta_{F'(a)}\circ G(\alpha_a)$, the two expressions agreeing by naturality of $\beta$. The compatibility of the two compositions is the **interchange law** $(\beta'\cdot\beta)*(\alpha'\cdot\alpha)=(\beta'*\alpha')\cdot(\beta*\alpha)$, the defining coherence of any $2$-category. *Concrete check:* with all categories equal to $\mathbf{Set}$ and $F=G=\mathrm{id}$, horizontal composition reduces to ordinary composition of natural transformations and the interchange law is just associativity of function composition applied component-wise. This is the simplest place to *see* "morphisms between morphisms" doing real work.

> **Pitfall.** "Strictify and forget the coherences" *fails* above dimension two: not every weak $3$-category is equivalent to a strict one (the *braiding* of §s6 is a $3$-categorical phenomenon that a strict $3$-category cannot see). This is the precise sense in which higher dimensions are genuinely harder.

<a id="s9"></a>
### Extended TQFT and the cobordism hypothesis (Baez–Dolan / Lurie) — statement

**What & why.** An ordinary TQFT (§s3) assigns data only to top- and codimension-one manifolds, so it can be cut only along codimension-one slices. An **extended TQFT** assigns data all the way down to *points*, allowing cutting in every codimension — the fully local version of "invariants from gluing." The **cobordism hypothesis** is the astonishing classification theorem: such a theory is *completely determined by a single object*, the value on a point, subject to one finiteness condition.

> **Definition — the $(\infty,n)$-cobordism category $\mathrm{Bord}_n$.**
> $\mathrm{Bord}_n$ is the symmetric monoidal $(\infty,n)$-category with:
> - **objects**: $0$-manifolds (finite sets of framed points);
> - **$1$-morphisms**: $1$-dimensional cobordisms between them;
> - **$2$-morphisms**: $2$-dimensional cobordisms between those; …
> - **$n$-morphisms**: $n$-dimensional cobordisms;
> - and above level $n$, *diffeomorphisms* and their homotopies (all invertible).
>
> Tensor product is disjoint union; the unit is the empty manifold.

> **Definition — extended (fully local) TQFT.**
> A **fully extended $n$-dimensional TQFT** valued in a symmetric monoidal $(\infty,n)$-category $\mathcal{C}$ is a symmetric monoidal functor
> $$
> Z:\mathrm{Bord}_n^{\,\mathrm{fr}}\longrightarrow\mathcal{C},
> $$
> where $\mathrm{Bord}_n^{\,\mathrm{fr}}$ is the *framed* cobordism category (each manifold carries a trivialization of a stabilized tangent bundle — a rigidification needed for the cleanest statement). Such a $Z$ assigns an object of $\mathcal{C}$ to a point, a $1$-morphism to an interval, …, and a number to a closed $n$-manifold, all compatibly with gluing in every codimension.

> **Theorem (cobordism hypothesis; Baez–Dolan conjecture, Lurie's theorem — stated).**
> Let $\mathcal{C}$ be a symmetric monoidal $(\infty,n)$-category. Evaluation at the positively-framed point,
> $$
> Z\;\longmapsto\;Z(\mathrm{pt}_+),
> $$
> is an equivalence
> $$
> \big\{\text{framed fully extended }n\text{d TQFTs }Z:\mathrm{Bord}_n^{\,\mathrm{fr}}\to\mathcal{C}\big\}\;\xrightarrow{\ \simeq\ }\;\big\{\text{fully dualizable objects of }\mathcal{C}\big\}.
> $$
> In words: **a framed extended TQFT is freely determined by an arbitrary fully dualizable object of the target** — the value on a point — and every fully dualizable object arises from exactly one such theory.

> **What "freely determined" means.** Once you choose $Z(\mathrm{pt}_+)=X$, *every other value is forced*: the value on an interval is the dual structure of $X$, the value on a circle is the trace (the *dimension*) of $X$, and so on. The single object $X$ generates the entire functor by repeatedly applying duality and traces. This is the ultimate "invariants from gluing": the whole theory is reconstructed from its most local piece.

> **Unframed versions.** For oriented or unoriented theories (the geometrically natural ones), the framing is replaced by an action of the orthogonal group $O(n)$ on the space of fully dualizable objects, and the classification becomes: *oriented* extended TQFTs $\leftrightarrow$ *homotopy fixed points* of the $SO(n)$-action on fully dualizable objects. The extra structure (a fixed-point datum) is precisely a *higher-categorical Frobenius/trace structure* — recovering §s4 as the case $n=1$ packaged correctly.

> **Intuition.** The cobordism hypothesis says $\mathrm{Bord}_n^{\,\mathrm{fr}}$ is the *free* symmetric monoidal $(\infty,n)$-category on a single fully dualizable object. "Free on one generator" is exactly why a functor out of it is determined by where that generator goes — the same principle as §s4's "$\mathrm{Cob}(2)$ is generated by the pants-and-cap subject to Frobenius relations," now in maximal generality.

<a id="s10"></a>
### Fully dualizable objects and examples of the hypothesis at work

**What & why.** The cobordism hypothesis reduces "classify extended TQFTs" to "find fully dualizable objects." We define dualizability carefully, build the ladder of conditions, and show the hypothesis recovering and generalizing the earlier sections.

> **Definition — dualizable object.**
> In a symmetric monoidal category, an object $X$ is **dualizable** if there is an object $X^\ast$ and morphisms $\mathrm{coev}:\mathbf{1}\to X\otimes X^\ast$ and $\mathrm{ev}:X^\ast\otimes X\to\mathbf{1}$ satisfying the *zigzag (snake) identities*
> $$
> (\mathrm{ev}\otimes 1_X)\circ(1_X\otimes\mathrm{coev})=1_X,\qquad
> (1_{X^\ast}\otimes\mathrm{ev})\circ(\mathrm{coev}\otimes 1_{X^\ast})=1_{X^\ast}.
> $$
> *Example (already used in §s3):* in $\mathbf{Vect}_k$, $X$ is dualizable iff $\dim X<\infty$, with $X^\ast$ the usual dual space, $\mathrm{coev}(1)=\sum_i e_i\otimes e_i^\ast$, $\mathrm{ev}(f\otimes v)=f(v)$.

> **Definition — fully dualizable object.**
> In a symmetric monoidal *$(\infty,n)$-category*, $X$ is **fully dualizable** if it is dualizable *and* the duality maps $\mathrm{ev},\mathrm{coev}$ are themselves dualizable as $1$-morphisms (have adjoints), *and* those adjunction units/counits are dualizable as $2$-morphisms, … all the way up through level $n$. It is a *finiteness condition at every categorical level* — the higher analogue of "finite-dimensional."

> **Example 1 — $n=1$, target $\mathbf{Vect}_k$.** Fully dualizable objects of $\mathbf{Vect}_k$ are finite-dimensional vector spaces. The hypothesis says a $1$d framed extended TQFT is a finite-dimensional $V$; on the circle it computes $\dim V$, the trace of the identity. This is the categorical statement that "$Z(S^1)=\dim Z(\mathrm{pt})$," recovering the simplest invariant.

> **Example 2 — $n=2$, target the $2$-category of algebras.** Take $\mathcal{C}=\mathbf{Alg}_k$: objects are $k$-algebras, $1$-morphisms are bimodules, $2$-morphisms are bimodule maps. *Fully dualizable objects are exactly the finite-dimensional semisimple algebras* (more precisely, *separable* algebras). The cobordism hypothesis then says a $2$d *extended* TQFT is a separable algebra $A$, and its value on the circle — the trace of the identity bimodule — is the **center** $Z(A)$, which is a *commutative Frobenius algebra*. This *recovers Dijkgraaf's theorem* (§s4): the non-extended $2$d TQFT one reads off is exactly the commutative Frobenius algebra $Z(S^1)=$ center of $A$, and the extension downgrades cleanly to it. The extended theory carries *more* information (the algebra $A$, not just its center).

> **Example 3 — $n=3$ and modular tensor categories.** Take $\mathcal{C}$ a suitable $3$-category of *tensor categories*. Fully dualizable objects are *fusion categories* with appropriate finiteness; the resulting extended $3$d TQFTs include the Reshetikhin–Turaev theories of §s6 when the input is *modular*. The hypothesis thus *organizes* the $3$d landscape — the MTC is the value on a point (or circle), and the knot and $3$-manifold invariants of §s7 are its higher traces. The climb "algebra $\to$ category $\to$ tensor category" observed empirically in §s4–s6 is now *explained*: it is the climb in the categorical level of "fully dualizable object" as $n$ increases.

> **Worked example — the circle invariant is a trace, in any target.** The cobordism hypothesis predicts a universal formula: for a framed extended TQFT $Z$ with $Z(\mathrm{pt}_+)=X$, the value on the circle is the *dimension* (categorical trace of the identity) of $X$,
> $$
> Z(S^1)=\dim(X):=\mathrm{ev}_X\circ\beta\circ\mathrm{coev}_X .
> $$
> Specialize: in $\mathbf{Vect}_k$ this is $\dim_k V$ (a number) — recovering §s3's circle$=\dim$. In $\mathbf{Alg}_k$ (Example 2) the "dimension" of an algebra $A$ is its *center as an object*, the Hochschild homology $HH_0(A)=A/[A,A]$, which for separable $A$ is the commutative Frobenius algebra $Z(S^1)$ of the underlying $2$d theory. In a tensor-category target (Example 3) it is the *Drinfeld center / Hochschild category*. One formula — "the circle computes the trace of the point" — instantiates to the dimension of a vector space, the center of an algebra, and the modular data of a tensor category, as the dimension of the target climbs. That single pattern is the whole content of the hypothesis seen through one example.

> **The mechanism in one line.** Because $\mathrm{Bord}_n^{\,\mathrm{fr}}$ is free on a fully dualizable object, *constructing* a TQFT is *checking finiteness*: verify your candidate $X=Z(\mathrm{pt})$ is fully dualizable, and the entire functor — every invariant of every manifold — exists and is unique. This converts hard geometric existence questions into algebraic finiteness checks, which is the deepest payoff of the whole framework.

> **Pitfall.** Full dualizability is *much* stronger than dualizability: a finite-dimensional algebra is dualizable in $\mathbf{Alg}_k$ but *fully* dualizable only when *separable* (semisimple with separable center). Forgetting the higher conditions is the most common error in applying the hypothesis.

<a id="s11"></a>
### Physics — anyons, topological phases of matter, and topological quantum computation

**What & why.** The abstract machine of this guide is the exact mathematics of certain real materials. In two spatial dimensions, particles need not be bosons or fermions: they can be **anyons**, whose quantum states transform nontrivially under braiding. The low-energy physics of an anyon system *is* a $3$d TQFT (two space + one time), its anyons are the simple objects of a modular tensor category, and braiding them performs **topological quantum computation** — error-robust precisely because the answer is a topological invariant.

> **Topological phase of matter.** A **gapped** quantum many-body system (one with an energy gap above its ground states) is in a **topological phase** if its ground-state degeneracy and excitations depend only on the *topology* of the surface it lives on, not on local details. The number of ground states on a surface $\Sigma$ equals $\dim Z(\Sigma)$ for the associated TQFT $Z$ — a topological invariant. *Example:* the fractional quantum Hall state at filling $\nu=1/3$ has ground-state degeneracy $3$ on the torus, matching $\dim Z(T^2)=3$ for the corresponding $U(1)_3$ Chern–Simons theory.

> **Anyons as simple objects.** The quasiparticle excitations are the simple objects $X_0=\mathbf{1},X_1,\dots,X_r$ of a modular tensor category (§s6). Their data has direct physical meaning:
> - **fusion rules** $X_i\otimes X_j\cong\bigoplus_k N_{ij}^k X_k$ — what particle results when two anyons merge;
> - the **$S$-matrix** — the amplitude for braiding one anyon fully around another;
> - the **twist** $\theta_i$ — the phase an anyon acquires under a $2\pi$ self-rotation (its *topological spin*).

> **Abelian vs non-abelian anyons.** If every fusion $X_i\otimes X_j$ has a single outcome, braiding only multiplies the state by a phase: **abelian anyons** (as in the $\nu=1/3$ Hall state). If some fusion has *multiple* outcomes, the space of states with fixed total charge is multi-dimensional, and braiding acts as a nontrivial *matrix* on it: **non-abelian anyons**. The standard example is the **Fibonacci anyon** $\tau$ with the single nontrivial fusion rule $\tau\otimes\tau\cong\mathbf{1}\oplus\tau$; the dimension of the $n$-anyon state space then grows like the Fibonacci numbers (hence the name), giving an exponentially large computational space.

> **Topological quantum computation.** Encode a qubit in the multi-dimensional fusion space of non-abelian anyons; *compute* by physically braiding the anyons, which applies unitary matrices (the braiding representation of the MTC) to the encoded state; *read out* by fusing anyons and detecting the outcome. Because the applied unitary depends only on the *topology* of the braid — not on the speed or precise path — small perturbations cannot corrupt it: the computation is **topologically protected** against local errors. For Fibonacci anyons the braid group representation is *dense* in the unitary group, so braiding alone is **universal** for quantum computation.

> **Worked numerical touchpoint — Fibonacci dimensions.** Let $d_\tau$ be the *quantum dimension* of $\tau$, defined by the fusion rule via $d_\tau^2=1+d_\tau$ (the dimension is multiplicative and matches the fusion $\tau\otimes\tau=\mathbf 1\oplus\tau$). Solving, $d_\tau=\tfrac{1+\sqrt5}{2}=\varphi$, the golden ratio. The state space of $n$ Fibonacci anyons (with trivial total charge) has dimension the Fibonacci number $F_{n-1}$, and asymptotically $\dim\sim\varphi^{\,n}$ — an exponentially large, topologically protected Hilbert space built from a single fusion rule. This number $\varphi$ is at once a fact about a fusion category, a quantum dimension in an MTC, an entry of an $S$-matrix, and the size of a real computational resource — the unity of math and physics this guide set out to display.

> **Intuition and pitfalls.** *Intuition:* a TQFT is the universal language for "physics that remembers only shape," and topological phases are the materials in which nature actually speaks it. *Pitfall:* topological protection guards against *local* perturbations and *small* deformations, not against *changing the topology* (e.g. accidentally fusing anyons) — the protection is exactly as strong as the invariant is, no more. *Pitfall 2:* not every braided category is modular; only modularity (invertible $S$-matrix, §s6) guarantees a consistent anyon theory with a well-defined $3$-manifold/torus state count, which is why modularity is the physical as well as the mathematical good-behavior condition.

---

*A first course in topological quantum field theory and the higher categories that govern it — from the geometry of cobordisms and the Atiyah–Segal axioms, through the clean two-dimensional classification by commutative Frobenius algebras, to the three-dimensional theories that compute the Jones polynomial, and finally to the cobordism hypothesis, which classifies fully extended theories by a single fully dualizable object. Read once for the architecture: a TQFT is a functor that turns gluing into composition, so the invariant of a whole is the algebraic composite of its parts; the deeper the cut you allow — codimension one, then all codimensions — the higher the categorical level of the algebra that controls it, until at the summit a whole field theory is reconstructed from its value on a point. Return to any boxed definition or proof as a reference, and keep the slogan in view: invariants from gluing.*
