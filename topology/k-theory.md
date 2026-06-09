**English** · [中文](k-theory.zh.md)

# Topological K-Theory, *vector bundles as a generalized cohomology.*

*A self-contained, rigorous first course in topological K-theory. The idea is disarmingly simple: instead of triangulating a space and counting cells, we look at the families of vector spaces — the **vector bundles** — that live over the space, and we package them into an algebraic invariant. That invariant turns out to obey almost all the rules of ordinary cohomology, but with a single extraordinary new symmetry — Bott periodicity — that ordinary cohomology lacks. Every term is defined on first use, every theorem is motivated in plain words before it is stated, and every claim is argued rather than asserted.*

[← Back to all guides](../README.md)

> **How to read this guide.** We assume the **Algebraic Topology** guide (homotopy of maps, homotopy equivalence, the cohomology groups $H^n(X;G)$, the cup product, suspension $\Sigma X$, the long exact sequence of a pair, and the notion of a generalized cohomology theory via the Eilenberg–Steenrod axioms) and the **Differential Topology** guide (smooth manifold, vector bundle, tangent bundle, characteristic classes, the Chern classes $c_i$ and the Thom isomorphism). We also use a little linear algebra (vector space, direct sum, tensor product, dual) and group theory (abelian group, ring). Whenever we lean on one of these, we restate the exact fact we need in one line. No prior K-theory is assumed; every new word — *Grothendieck group*, *reduced K-theory*, *Bott periodicity*, *Chern character*, *Clifford algebra* — is defined the first time it appears.

---

## Part A · From bundles to a group

<a id="s0"></a>
### Motivation — classifying vector bundles, and a cohomology theory built out of them

A **vector bundle** over a topological space $X$ is, informally, a continuously varying family of vector spaces — one vector space $E_x$ (the **fiber**) attached to each point $x\in X$, glued together so that locally it looks like a product $U\times\mathbb{C}^n$. (The precise definition is in §s1.) The simplest examples are the **trivial bundle** $X\times\mathbb{C}^n$, where every fiber is the same copy of $\mathbb{C}^n$, and the **tangent bundle** of a smooth manifold, whose fiber at $x$ is the tangent space $T_xM$.

Two basic questions drive the whole subject:

- **Classification.** Given $X$, how many vector bundles of rank $n$ does it carry, up to isomorphism? On a contractible space the answer is "only the trivial one," but on the sphere $S^2$ there are infinitely many line bundles, indexed by an integer (the degree). Classifying bundles is hard because the set of isomorphism classes is just a set with an addition (direct sum) that has no inverses.

- **An invariant from bundles.** Ordinary cohomology $H^*(X)$ is built from a chosen combinatorial skeleton (cells, simplices). Could we instead build a functorial invariant *directly* out of the bundles on $X$ — something that assigns to each space a ring, to each continuous map a ring homomorphism, and that we can actually compute? 

The answer to the second question is **K-theory**, invented by Atiyah and Hirzebruch (following Grothendieck's algebraic construction). The recipe has two moves:

1. **Fix the missing inverses.** The isomorphism classes of bundles under $\oplus$ form a commutative monoid (an associative addition with a zero but no subtraction). The **Grothendieck group** construction (§s2) formally adjoins inverses, turning the monoid into an abelian group $K^0(X)$. Tensor product of bundles makes it a ring.

2. **Build higher groups and find periodicity.** Using the suspension $\Sigma X$ we define groups $K^{-n}(X)$ for all $n\ge 0$ (§s4), and the **Bott periodicity theorem** (§s5) collapses this infinite ladder to just two groups, $K^0$ and $K^{-1}$, repeating with period $2$. This periodicity has no analogue in ordinary cohomology and is the single feature that makes K-theory both rigid and computable.

The payoff is a **generalized cohomology theory** (§s6): K-theory satisfies every Eilenberg–Steenrod axiom except the dimension axiom (which says the cohomology of a point is concentrated in degree $0$). Replacing "the cohomology of a point" by "the K-theory of a point, which is $\mathbb{Z}$ in *every even degree*" is exactly Bott periodicity. From this single change flows the Chern character (§s7), the Thom isomorphism and push-forward (§s8), real K-theory with its eightfold periodicity (§s9), and the deep links to analysis and physics (§s10–s11).

> **Principle — the K-theory strategy.**
> Do not classify bundles one at a time. Instead, throw them all into one algebraic object that records only the information stable under adding trivial bundles, then exploit the resulting periodicity. "Stable" is the operative word: $K$-theory sees a bundle only up to the addition of trivial summands, and this stabilization is precisely what makes the theory rigid enough to compute and rich enough to detect index theory and D-brane charges.

**Roadmap.** Part A (§s1–s3) builds $K^0(X)$ from bundles and computes it for the point and the sphere. Part B (§s4–s6) erects the cohomology theory: higher groups, Bott periodicity, the axioms. Part C (§s7–s8) connects K-theory to ordinary cohomology via the Chern character and develops the push-forward needed for index theory. Part D (§s9–s11) surveys the real theory, analytic K-theory, and the appearances of K-theory in physics. A reader in a hurry can read §s0, §s2, §s5, and §s7 and still see the whole arc.

<a id="s1"></a>
### Vector bundles recap; operations; pullbacks and homotopy invariance

We work over the complex numbers unless stated otherwise; "vector space" means "finite-dimensional complex vector space," and $X$ denotes a **compact Hausdorff space** (compact: every open cover has a finite subcover; Hausdorff: distinct points have disjoint neighborhoods). Compactness is assumed throughout Parts A–B because it guarantees the key finiteness facts (every bundle is a summand of a trivial one, §s2).

> **Definition — vector bundle.**
> A (complex, rank $n$) **vector bundle** over $X$ is a topological space $E$ together with a continuous surjection $\pi:E\to X$ such that:
> (i) each **fiber** $E_x:=\pi^{-1}(x)$ carries the structure of an $n$-dimensional complex vector space;
> (ii) **local triviality**: every point of $X$ has an open neighborhood $U$ and a homeomorphism $\varphi:\pi^{-1}(U)\to U\times\mathbb{C}^n$ (a **local trivialization**) with $\varphi(E_x)=\{x\}\times\mathbb{C}^n$ and $\varphi$ restricting to a *linear* isomorphism $E_x\cong\mathbb{C}^n$ on each fiber.
> The number $n$ is the **rank**. A rank-$1$ bundle is a **line bundle**. The space $E$ is the **total space**, $X$ the **base**, $\pi$ the **projection**.

Where two trivializations $\varphi_\alpha,\varphi_\beta$ overlap, the composite $\varphi_\alpha\varphi_\beta^{-1}$ on $(U_\alpha\cap U_\beta)\times\mathbb{C}^n$ has the form $(x,v)\mapsto(x,g_{\alpha\beta}(x)v)$ for a continuous map $g_{\alpha\beta}:U_\alpha\cap U_\beta\to GL_n(\mathbb{C})$, the **transition functions**. These satisfy the **cocycle condition** $g_{\alpha\beta}g_{\beta\gamma}=g_{\alpha\gamma}$, and conversely any system of maps satisfying it builds a bundle by gluing. This is the concrete handle we use in examples.

**Worked example — the Möbius bundle via transition functions.** Cover $S^1$ (angle $\theta\in[0,2\pi)$) by two arcs $U=\{0<\theta<\pi+\epsilon\}$ and $V=\{\pi-\epsilon<\theta<2\pi+\epsilon\}$. Their overlap has two components, near $\theta=0$ and near $\theta=\pi$. Define a real line bundle by transition function $g_{UV}=+1$ on the component near $\theta=\pi$ and $g_{UV}=-1$ on the component near $\theta=0$. The single sign flip means a frame transported once around comes back negated: this is the **Möbius band**, the nontrivial real line bundle on $S^1$. With $g_{UV}\equiv+1$ everywhere we get the trivial cylinder. The cocycle condition is vacuous (only two charts), so the only invariant is the set of signs up to the equivalence of changing local frames — exactly $\mathbb{Z}/2=\{\text{cylinder},\text{Möbius}\}$, matching the clutching count $\pi_0(GL_1(\mathbb{R}))$ of §s3. (Complex line bundles on $S^1$ have no analogue because $\mathbb{C}^\times$ is connected — no sign to flip — so $\tilde K^0(S^1)=0$.)

> **Definition — section, morphism, isomorphism.**
> A **section** of $\pi:E\to X$ is a continuous map $s:X\to E$ with $\pi\circ s=\mathrm{id}_X$ (it picks a vector $s(x)\in E_x$ in each fiber). A **bundle morphism** $f:E\to F$ (over the same base) is a continuous map with $\pi_F\circ f=\pi_E$ that is linear on each fiber; it is an **isomorphism** if it has an inverse morphism. We write $\mathrm{Vect}_n(X)$ for the set of isomorphism classes of rank-$n$ bundles, and $\mathrm{Vect}(X)=\bigsqcup_n\mathrm{Vect}_n(X)$.

**The operations.** Every functorial operation on vector spaces extends fiberwise to bundles, because it can be applied to the transition functions and the cocycle condition is preserved.

> **Definition — direct sum, tensor product, dual.**
> Given bundles $E,F$ over $X$:
> - The **Whitney sum** (direct sum) $E\oplus F$ has fiber $(E\oplus F)_x=E_x\oplus F_x$, rank $\mathrm{rk}\,E+\mathrm{rk}\,F$, transition functions the block-diagonal $g^E_{\alpha\beta}\oplus g^F_{\alpha\beta}$.
> - The **tensor product** $E\otimes F$ has fiber $E_x\otimes F_x$, rank $(\mathrm{rk}\,E)(\mathrm{rk}\,F)$, transition functions $g^E_{\alpha\beta}\otimes g^F_{\alpha\beta}$.
> - The **dual** $E^*$ has fiber $(E_x)^*=\mathrm{Hom}(E_x,\mathbb{C})$, transition functions $(g^E_{\alpha\beta})^{-\top}$ (inverse transpose).

These obey the usual algebra of vector spaces, fiber by fiber: $\oplus$ is commutative and associative with the rank-$0$ bundle as identity, $\otimes$ is commutative and associative with the trivial line bundle $\underline{\mathbb{C}}:=X\times\mathbb{C}$ as identity, and $\otimes$ distributes over $\oplus$. We write $\underline{\mathbb{C}}^n=X\times\mathbb{C}^n$ for the trivial rank-$n$ bundle.

> **Definition — pullback.**
> Let $f:Y\to X$ be continuous and $\pi:E\to X$ a bundle. The **pullback** $f^*E$ is the bundle over $Y$ with total space $f^*E=\{(y,e)\in Y\times E:f(y)=\pi(e)\}$ and projection $(y,e)\mapsto y$; its fiber over $y$ is $E_{f(y)}$. If $E$ has transition functions $g_{\alpha\beta}$ over $\{U_\alpha\}$, then $f^*E$ has transition functions $g_{\alpha\beta}\circ f$ over $\{f^{-1}(U_\alpha)\}$.

Pullback is functorial: $(\mathrm{id})^*E\cong E$ and $(g\circ f)^*E\cong f^*(g^*E)$, and it commutes with $\oplus,\otimes,(-)^*$. The single most important property of bundles for K-theory is that pullback depends only on the homotopy class of the map.

> **Theorem (homotopy invariance of pullbacks).** Let $X$ be paracompact (compact Hausdorff suffices) and $E\to X$ a vector bundle. If $f_0,f_1:Y\to X$ are homotopic continuous maps, then $f_0^*E\cong f_1^*E$.

*Plain-language idea.* A homotopy is a bundle over $Y\times[0,1]$; we show such a bundle is, up to isomorphism, constant in the $[0,1]$ direction, so its two ends agree. We prove the engine and then deduce the theorem.

**Demonstration — bundles over $Y\times[0,1]$ are pulled back from $Y$.**

1. Let $H:Y\times[0,1]\to X$ be a homotopy from $f_0$ to $f_1$, and set $E_H:=H^*E$, a bundle over $Y\times[0,1]$. It suffices to show $E_H\cong p^*(E_H|_{Y\times\{0\}})$ where $p:Y\times[0,1]\to Y\times\{0\}$ is the projection, for then restricting to the two ends gives $f_1^*E=E_H|_{Y\times\{1\}}\cong E_H|_{Y\times\{0\}}=f_0^*E$. *(definition of pullback and restriction)*
2. **Local statement.** Over a point $y_0\in Y$, the bundle $E_H$ restricted to $\{y_0\}\times[0,1]$ is a bundle over an interval, hence trivial (an interval is contractible; any bundle over a contractible paracompact base is trivial — proved in §s3 via clutching/extension, or take it as the standard fact that bundles over $[0,1]$ admit a nowhere-zero frame by extending one from $\{0\}$). So there is a neighborhood $U$ of $y_0$ over which $E_H$ trivializes on $U\times[0,1]$ after possibly shrinking; the obstruction to extending a trivialization in the $t$-direction is the solution of a continuous linear extension problem on the interval, always solvable. *(local triviality; triviality over an interval)*
3. **Patching.** Cover $Y$ by such neighborhoods $U_i$ on which $E_H\cong p^*(E_H|_{U_i\times\{0\}})$. Choose a partition of unity $\{\rho_i\}$ subordinate to $\{U_i\}$ (exists by paracompactness). Using the isomorphisms over each $U_i$, build a global bundle isomorphism by **partition-of-unity interpolation** of the local trivializing frames, weighted by $\{\rho_i\}$; linearity of the gluing and convexity of the parameter $t$ make the interpolation well-defined and invertible. *(partition of unity glues local isomorphisms; convex combination stays in $GL$ via a homotopy-lifting argument)*
4. The result is a global isomorphism $E_H\cong p^*(E_H|_{Y\times\{0\}})$, completing the proof. *(steps 1–3)*

**Corollary (computational engine).** Bundles are a homotopy-invariant functor: $\mathrm{Vect}(X)$ depends only on the homotopy type of $X$. In particular, every bundle over a **contractible** space is trivial (take $Y=X$, $f_0=\mathrm{id}$, $f_1=$ constant; then $E\cong f_0^*E\cong f_1^*E=$ trivial).

**Pitfall.** Homotopy invariance needs paracompactness (so that partitions of unity exist). Over wild base spaces it can fail. For us $X$ is always compact Hausdorff, so we never have to worry.

<a id="s2"></a>
### The Grothendieck group construction; $K^0(X)$ as a ring; the reduced group $\tilde K^0(X)$

The set $\mathrm{Vect}(X)$ with $\oplus$ is a **commutative monoid**: an addition that is associative, commutative, and has an identity (the rank-$0$ bundle), but in general no inverses — you cannot "subtract" a bundle. K-theory begins by forcing inverses into existence by a universal algebraic device.

> **Definition — Grothendieck group of a commutative monoid.**
> Let $(M,+,0)$ be a commutative monoid. Its **Grothendieck group** $\mathcal G(M)$ is the abelian group defined as follows. On the set $M\times M$ (think of $(a,b)$ as the formal difference "$a-b$") impose the equivalence relation
> $$
> (a,b)\sim(c,d)\iff \exists\,k\in M:\ a+d+k=c+b+k.
> $$
> Set $\mathcal G(M)=(M\times M)/\!\sim$ with addition $[(a,b)]+[(c,d)]=[(a+c,b+d)]$. The class of $(a,0)$ is written $[a]$, and $[(a,b)]=[a]-[b]$.

The extra "$+k$" is essential: without it $\sim$ need not be transitive when $M$ has no cancellation. Let us verify $\mathcal G(M)$ really is a group and is universal.

**Demonstration — $\mathcal G(M)$ is an abelian group, universal among monoid homomorphisms to groups.**

1. **$\sim$ is an equivalence relation.** Reflexive and symmetric are immediate from the symmetric form $a+d+k=c+b+k$. Transitivity: if $a+d+k=c+b+k$ and $c+f+l=e+d+l$, add them and cancel-via-witness: $a+f+(d+k+c+l)=e+b+(d+k+c+l)$, so $(a,b)\sim(e,f)$ with witness $d+k+c+l$. *(commutativity and associativity of $+$ in $M$)*
2. **Addition is well-defined and abelian** because it is computed coordinatewise from the abelian $+$ on $M$ and respects $\sim$ (add the two witnesses). The identity is $[(0,0)]=[0]$. *(coordinatewise inheritance)*
3. **Inverses exist:** $[(a,b)]+[(b,a)]=[(a+b,a+b)]=[0]$ since $(a+b,a+b)\sim(0,0)$ with witness $0$. So $-[a]=[(0,a)]$. *(definition of $\sim$)*
4. **Universal property.** The map $\iota:M\to\mathcal G(M)$, $a\mapsto[a]$, is a monoid homomorphism, and for any abelian group $A$ and monoid homomorphism $\phi:M\to A$ there is a *unique* group homomorphism $\bar\phi:\mathcal G(M)\to A$ with $\bar\phi\circ\iota=\phi$, namely $\bar\phi([a]-[b])=\phi(a)-\phi(b)$ (well-defined because $\phi$ respects $\sim$, since $A$ is a group where the witness $k$ cancels). *(universal property of group completion)*

> **Definition — $K^0(X)$.**
> $K^0(X):=\mathcal G(\mathrm{Vect}(X))$, the Grothendieck group of isomorphism classes of complex vector bundles over $X$ under $\oplus$. Its elements, **virtual bundles**, are formal differences $[E]-[F]$.

**A cleaner description via stabilization.** On a compact base every class is the difference of an honest bundle and a *trivial* one.

> **Lemma (complementability).** For any vector bundle $E$ over a compact Hausdorff space $X$ there is a bundle $E'$ with $E\oplus E'\cong\underline{\mathbb{C}}^N$ for some $N$.

*Proof.* Cover $X$ by finitely many trivializing opens $U_1,\dots,U_m$ (finite by compactness); take a partition of unity $\{\rho_i\}$. The maps $\rho_i\cdot(\text{trivialization}_i):E\to\mathbb{C}^{n}$ assemble to a fiberwise-injective bundle map $E\hookrightarrow\underline{\mathbb{C}}^{mn}=:\underline{\mathbb{C}}^N$ (injective because at each point at least one $\rho_i>0$ and that component is injective). Put a Hermitian metric on $\underline{\mathbb{C}}^N$ (average local ones with $\{\rho_i\}$); then $E'=E^\perp$ is a bundle with $E\oplus E'\cong\underline{\mathbb{C}}^N$. $\square$

> **Corollary — stable form.** Every element of $K^0(X)$ equals $[E]-[\underline{\mathbb{C}}^n]$ for some bundle $E$ and integer $n$. Two bundles satisfy $[E]=[F]$ in $K^0(X)$ iff they are **stably isomorphic**: $E\oplus\underline{\mathbb{C}}^k\cong F\oplus\underline{\mathbb{C}}^k$ for some $k$ (this is the relation $\sim$ with the complementability lemma turning the witness into a trivial bundle).

> **Definition — the ring structure.**
> Tensor product makes $K^0(X)$ a **commutative ring**: define $([E]-[F])\cdot([E']-[F'])=[E\otimes E']+[F\otimes F']-[E\otimes F']-[F\otimes E']$. The multiplicative identity is $[\underline{\mathbb{C}}]$ (the trivial line bundle). Distributivity over $+$ follows from distributivity of $\otimes$ over $\oplus$ fiberwise.

That this is well-defined (independent of representatives) follows from the universal property applied twice, using that $\otimes$ is biadditive over $\oplus$.

**Worked example — multiplying in $K^0(S^2)$.** Using the basis $\{1,\beta\}$ with $\beta=H-1$ and the relation $\beta^2=0$ (§s3): the product of two general elements is
$$
(a+b\beta)(c+d\beta)=ac+(ad+bc)\beta+bd\,\beta^2=ac+(ad+bc)\beta.
$$
So $\tilde K^0(S^2)=\mathbb{Z}\beta$ is an ideal that squares to zero — multiplicatively trivial reduced K-theory. This nilpotence is generic on spheres: $\tilde K^0(S^n)$ always has vanishing products (any product of two positive-degree classes lands in $\tilde K^0(S^{n}\wedge S^{n})$-degree $>n$, which is forced to zero), so the ring information of a sphere is entirely in the additive group plus the unit. The interesting multiplicative structure appears on spaces like $\mathbb{CP}^n$, where $x^n\ne0$.

**Functoriality.** A continuous map $f:Y\to X$ induces $f^*:K^0(X)\to K^0(Y)$, a *ring homomorphism*, by $f^*([E]-[F])=[f^*E]-[f^*F]$ (pullback respects $\oplus,\otimes$). By homotopy invariance (§s1), homotopic maps induce equal homomorphisms; thus $K^0$ is a homotopy-invariant contravariant functor from compact spaces to commutative rings — the first cohomology-like property.

> **Definition — rank homomorphism and reduced K-theory.**
> Assume $X$ connected (so rank is a well-defined integer on each bundle). The **rank** $\mathrm{rk}:K^0(X)\to\mathbb{Z}$, $[E]-[F]\mapsto\mathrm{rk}\,E-\mathrm{rk}\,F$, is a surjective ring homomorphism. Its kernel is the **reduced K-theory**
> $$
> \tilde K^0(X):=\ker\big(\mathrm{rk}:K^0(X)\to\mathbb{Z}\big).
> $$
> Equivalently, picking a basepoint $x_0\in X$ with inclusion $i:\{x_0\}\hookrightarrow X$, one has $\tilde K^0(X)=\ker\big(i^*:K^0(X)\to K^0(\mathrm{pt})=\mathbb{Z}\big)$, and there is a canonical splitting
> $$
> K^0(X)\cong\tilde K^0(X)\oplus\mathbb{Z}.
> $$

The splitting holds because the constant map $X\to\{x_0\}$ gives a ring map $\mathbb{Z}=K^0(\mathrm{pt})\to K^0(X)$ that is a section of $i^*$; the image is the trivial bundles, and $\tilde K^0$ measures the "nontrivial part." In $\tilde K^0(X)$ a virtual bundle is recorded only up to addition of trivial bundles of any rank — the formal home of *stable* phenomena.

> **Intuition.** $K^0(X)$ answers "what are all bundles, up to subtraction and stabilization?" The integer part $\mathbb{Z}$ is the boring rank; $\tilde K^0(X)$ is where the topology lives. For $X=S^2$ we will find $\tilde K^0(S^2)\cong\mathbb{Z}$, generated by the difference $[H]-[\underline{\mathbb{C}}]$ of the Hopf line bundle and the trivial one (§s3).

**Worked example — the Grothendieck group of $\mathbb{N}$, with numbers.** Take $M=(\mathbb{N},+,0)$, the prototype monoid (it is $\mathrm{Vect}(\mathrm{pt})$). A pair $(a,b)$ means "$a-b$." Then $(3,1)\sim(5,3)$ because $3+3+0=5+1+0$, i.e. both represent $2$. The class of $(0,1)$ is the new element $-1$, which $\mathbb{N}$ lacked. The map $[a]-[b]\mapsto a-b$ is the iso $\mathcal G(\mathbb{N})\cong\mathbb{Z}$. The witness "$+k$" is invisible here because $\mathbb{N}$ has cancellation; it becomes essential for monoids like $\mathrm{Vect}(X)$ on spaces where $E\oplus G\cong F\oplus G$ does *not* force $E\cong F$ (only stable iso), so the witness $k$ encodes "$\oplus$ a trivial bundle." This is precisely why $K^0$ remembers bundles only up to stabilization.

**Pitfall — the map $\mathrm{Vect}(X)\to K^0(X)$ need not be injective.** Distinct bundles can become equal in $K^0$: if $E\oplus\underline{\mathbb{C}}^k\cong F\oplus\underline{\mathbb{C}}^k$ but $E\not\cong F$, then $[E]=[F]$. Such non-isomorphic *stably isomorphic* bundles exist (e.g. on high-dimensional spheres, the tangent bundle of $S^n$ is stably trivial — $TS^n\oplus\underline{\mathbb{R}}\cong\underline{\mathbb{R}}^{n+1}$ — yet $TS^n$ is nontrivial unless $n\in\{1,3,7\}$). K-theory deliberately forgets this distinction; that forgetting is what buys computability.

<a id="s3"></a>
### Worked examples — $K^0(\mathrm{point})$, $K^0(S^2)$, and the role of line bundles

**Example 1 — the point.** Over $X=\{*\}$ a vector bundle is just a finite-dimensional vector space, classified up to isomorphism by its dimension. So $\mathrm{Vect}(\mathrm{pt})\cong(\mathbb{N},+)$ and
$$
K^0(\mathrm{pt})=\mathcal G(\mathbb{N})=\mathbb{Z},\qquad \tilde K^0(\mathrm{pt})=0,
$$
with ring structure that of $\mathbb{Z}$ (tensor product of vector spaces multiplies dimensions). This is the analogue of $H^0(\mathrm{pt})=\mathbb{Z}$; the difference from ordinary cohomology will be that $K$ of a point is nonzero in *all even degrees* (§s5).

**Line bundles and clutching.** To compute $K^0(S^2)$ we need to know the bundles on a sphere. The tool is *clutching*: build a bundle on $S^n$ by trivializing over the two hemispheres and gluing along the equator.

> **Construction — clutching on $S^n$.** Write $S^n=D_+^n\cup_{S^{n-1}}D_-^n$ as two closed disks glued along their boundary equator $S^{n-1}$. A bundle trivial on each disk is determined, up to isomorphism, by a continuous **clutching function** $g:S^{n-1}\to GL_n(\mathbb{C})$ specifying how the two trivial bundles are identified over the equator. Homotopic clutching functions give isomorphic bundles, and $\oplus$ corresponds to block sum $g\mapsto g\oplus g'$. Thus
> $$
> \mathrm{Vect}_n(S^k)\cong[S^{k-1},GL_n(\mathbb{C})]=\pi_{k-1}(GL_n(\mathbb{C})),
> $$
> the set of homotopy classes of maps from the equator into $GL_n(\mathbb{C})$ (a group via $\pi_{k-1}$ since $GL_n$ is a topological group).

*Why homotopic clutching functions give isomorphic bundles:* a homotopy $g_t$ is a clutching function for a bundle over $S^k\times[0,1]$, whose ends are the two bundles; homotopy invariance of bundles over the cylinder (§s1) identifies them.

**Line bundles on $S^2$.** Here $n=1$, $k=2$: clutching functions are maps $g:S^1\to GL_1(\mathbb{C})=\mathbb{C}^\times$. Since $\mathbb{C}^\times\simeq S^1$ deformation-retracts onto the unit circle, $\pi_1(\mathbb{C}^\times)=\mathbb{Z}$, the **winding number** (degree) of $g$. Hence line bundles on $S^2$ are classified by an integer:
$$
\mathrm{Vect}_1(S^2)\cong\pi_1(\mathbb{C}^\times)=\mathbb{Z}.
$$
The generator (winding number $1$) is the **Hopf line bundle** $H$, the tautological line bundle of $\mathbb{CP}^1=S^2$ whose fiber over a line $\ell\subset\mathbb{C}^2$ is $\ell$ itself. Tensor product of line bundles adds winding numbers: $H^{\otimes m}$ has winding number $m$, so $\mathrm{Vect}_1(S^2)\cong\mathbb{Z}$ is a *group* under $\otimes$ (the **Picard group**), with $H$ the generator and $H^{-1}=H^*$.

> **A key relation — the fundamental product relation.** In $K^0(S^2)$,
> $$
> (\,[H]-1\,)^2=0,\qquad\text{equivalently}\qquad [H]^2=2[H]-1,
> $$
> where $1=[\underline{\mathbb{C}}]$. 

**Demonstration of the relation.** $(H-1)^2=H^2-2H+1=H\otimes H-2H+1$. As bundles, $H\otimes H\oplus\underline{\mathbb{C}}\cong H\oplus H$: both are rank-$2$ bundles on $S^2$, and clutching functions multiply under $\otimes$ and add (block) under $\oplus$, so $H\otimes H$ has clutching $z\mapsto z^2$ while $H\oplus H$ has $z\mapsto\mathrm{diag}(z,z)$; the matrices $\mathrm{diag}(z^2,1)$ and $\mathrm{diag}(z,z)$ are homotopic in $GL_2(\mathbb{C})$ (both have determinant winding $2$ and $GL_2(\mathbb{C})$ is connected with $\pi_1=\mathbb{Z}$ detected by determinant). Hence $H^2+1\cong 2H$ as bundles, giving $H^2-2H+1=0$ in $K^0(S^2)$. $\square$

> **Theorem (computation of $K^0(S^2)$).** As a ring,
> $$
> K^0(S^2)\cong\mathbb{Z}[H]/\big((H-1)^2\big),\qquad \tilde K^0(S^2)\cong\mathbb{Z}\ \text{generated by }(H-1).
> $$

*Proof sketch (full justification via Bott in §s5).* The relation $(H-1)^2=0$ shows the subring generated by $H$ is $\mathbb{Z}[H]/((H-1)^2)$, free of rank $2$ over $\mathbb{Z}$ with basis $\{1,H-1\}$. That these are *all* of $K^0(S^2)$ — i.e. $\tilde K^0(S^2)=\mathbb{Z}\langle H-1\rangle$ and not larger — is exactly the rank-$2$ statement of Bott periodicity (§s5), which we prove there. The reduced generator $\beta:=H-1$ is the **Bott class**; multiplication by $\beta$ implements the periodicity isomorphism. $\square$

**Sanity check against cohomology.** $H^*(S^2;\mathbb{Z})=\mathbb{Z}$ in degrees $0$ and $2$, total rank $2$ — matching $\mathrm{rank}_\mathbb{Z}K^0(S^2)=2$. The Chern character (§s7) will make this match an isomorphism after tensoring with $\mathbb{Q}$, sending $H-1$ to the generator of $H^2(S^2;\mathbb{Q})$.

**Example 4 — every bundle on $S^2$, not just lines.** Higher-rank bundles on $S^2$ are classified by $\mathrm{Vect}_n(S^2)=\pi_1(GL_n(\mathbb{C}))=\mathbb{Z}$ for every $n\ge1$, the integer again read off by the winding of the determinant of the clutching function (the determinant map $GL_n(\mathbb{C})\to\mathbb{C}^\times$ induces the iso on $\pi_1$ because $SL_n(\mathbb{C})$ is simply connected). So a rank-$n$ bundle $E$ on $S^2$ is determined up to isomorphism by $(n,c_1)$ with $c_1\in\mathbb{Z}$, and $E\cong H^{\otimes c_1}\oplus\underline{\mathbb{C}}^{n-1}$. This is a clean illustration of the **stable range**: once the rank exceeds the dimension's half, bundles split off trivial summands and only the "stable" data $(n,c_1)$ — exactly what $K^0$ records — survives. It is why $K^0(S^2)=\mathbb{Z}\{1\}\oplus\mathbb{Z}\{H-1\}$ captures *all* bundles, not an approximation.

**Example 5 — $K^0(S^1)$ and the role of connectedness of $GL$.** For the circle, clutching uses $\pi_0(GL_n(\mathbb{C}))$: a bundle on $S^1=D^1\cup_{S^0}D^1$ is glued along two points by an element of $GL_n(\mathbb{C})$, and homotopy classes of such are $\pi_0(GL_n(\mathbb{C}))=\{*\}$ since $GL_n(\mathbb{C})$ is path-connected. Hence every bundle on $S^1$ is trivial, $\tilde K^0(S^1)=0$, and $K^0(S^1)=\mathbb{Z}$. (Contrast the real case: $GL_n(\mathbb{R})$ has two components, so real line bundles on $S^1$ form $\mathbb{Z}/2$ — the Möbius band is the nontrivial one. This is the first hint that $KO$ differs from $K$.)

---

## Part B · K-theory as a cohomology theory

<a id="s4"></a>
### Higher K-groups $K^{-n}(X)$ via suspension; relative K-theory

Ordinary cohomology has groups $H^n$ in every degree. So far we have only $K^0$. We manufacture the higher (negative-degree) groups using the **suspension**, exactly as one defines higher homotopy groups by looping.

> **Definition — reduced suspension and basepoint.** For a space $X$ with basepoint $x_0$, the **reduced suspension** is $\Sigma X=(X\times[0,1])/\big(X\times\{0\}\cup X\times\{1\}\cup\{x_0\}\times[0,1]\big)$ — collapse top, bottom, and the basepoint-line to a single point. Thus $\Sigma S^n=S^{n+1}$. All spaces here are **pointed** compact Hausdorff and maps preserve basepoints.

> **Definition — negative K-groups.** For $n\ge 0$,
> $$
> \tilde K^{-n}(X):=\tilde K^0(\Sigma^n X),\qquad K^{-n}(X):=\tilde K^{-n}(X_+),
> $$
> where $\Sigma^n$ is the $n$-fold reduced suspension and $X_+=X\sqcup\{*\}$ is $X$ with a disjoint basepoint added (this trick lets unpointed/relative formulas read uniformly; note $\tilde K^0(X_+)=K^0(X)$).

The reason this is the *right* definition is that for ordinary reduced cohomology one has the **suspension isomorphism** $\tilde H^{n}(X)\cong\tilde H^{n+1}(\Sigma X)$; defining $\tilde K^{-n}(X)=\tilde K^0(\Sigma^n X)$ builds that suspension behavior into K-theory by fiat, so the resulting graded object will satisfy the suspension axiom automatically (§s6).

> **Definition — relative K-theory.** For a compact pair $(X,A)$ ($A\subseteq X$ closed), define the **quotient** $X/A$ (collapse $A$ to a point, the basepoint) and set
> $$
> K^0(X,A):=\tilde K^0(X/A),\qquad K^{-n}(X,A):=\tilde K^{-n}(X/A)=\tilde K^0(\Sigma^n(X/A)).
> $$
> When $A=\varnothing$, $X/\varnothing=X_+$ and we recover $K^{-n}(X)$. Relative classes are virtual bundles on $X$ trivialized over $A$, up to the equivalence that respects the trivialization.

> **Concrete model of relative classes (difference bundles).** An element of $K^0(X,A)$ is represented by a triple $(E,F,\alpha)$ of bundles $E,F$ on $X$ together with an isomorphism $\alpha:E|_A\cong F|_A$ over $A$; the class is "$[E]-[F]$ with the chosen trivialization on $A$." Two triples are equivalent if they agree after stabilization and homotopy of $\alpha$. This is the working description used in the index theorem (§s10).

**Worked example — $K^0(D^2,S^1)$.** The disk $D^2$ is contractible and $D^2/S^1\cong S^2$, so $K^0(D^2,S^1)=\tilde K^0(S^2)=\mathbb{Z}$. In the difference-bundle picture, a generator is the triple $(\underline{\mathbb{C}},\underline{\mathbb{C}},\alpha)$ where $\alpha:S^1\to GL_1(\mathbb{C})=\mathbb{C}^\times$ is the identity map $z\mapsto z$ of winding number $1$: two trivial line bundles on the disk glued over the boundary by a degree-one twist. Collapsing $S^1$ this is precisely the Hopf bundle's clutching data, recovering the Bott generator. The winding number of $\alpha$ is the integer invariant — a baby version of the "symbol class" of an elliptic operator (§s10), which is exactly such a difference bundle on the tangent space trivialized away from the zero section.

**Worked example — $K^{-n}(\mathrm{pt})$.** Here $X=\mathrm{pt}$, so $\Sigma^n(\mathrm{pt}_+)=\Sigma^n S^0=S^n$. Thus
$$
K^{-n}(\mathrm{pt})=\tilde K^0(S^n).
$$
We already found $\tilde K^0(S^0)=\mathbb{Z}$ (two points: $K^0(S^0)=\mathbb{Z}\oplus\mathbb{Z}$, and the reduced part — the kernel of restriction to the basepoint — is the remaining $\mathbb{Z}$; see below) and $\tilde K^0(S^2)=\mathbb{Z}$. The full pattern $\tilde K^0(S^n)=\mathbb{Z}$ for $n$ even and $0$ for $n$ odd is the content of Bott periodicity, to which we now turn. Concretely it gives
$$
K^{-n}(\mathrm{pt})=\begin{cases}\mathbb{Z}&n\text{ even}\\ 0&n\text{ odd.}\end{cases}
$$

(The careful value $\tilde K^0(S^0)$: a bundle on two points is a pair of vector spaces; reduced K-theory of $S^0$, with one point as basepoint, is $\mathbb{Z}$ — the rank of the bundle over the non-basepoint. Suspending once, $\tilde K^0(S^1)=\pi_0(GL(\mathbb{C}))=0$ since $GL_n(\mathbb{C})$ is connected. These two anchor the periodicity.)

<a id="s5"></a>
### Bott periodicity (statement, with the idea of the proof) and its consequences

The defining miracle of K-theory.

> **Theorem (Bott periodicity, complex case).** For every compact pointed space $X$ there is a natural isomorphism
> $$
> \beta:\tilde K^0(X)\xrightarrow{\ \cong\ }\tilde K^0(\Sigma^2 X)=\tilde K^{-2}(X),
> $$
> given by multiplication by the **Bott class** $b\in\tilde K^0(S^2)$, $b=[H]-1$. Equivalently $\tilde K^{-n}(X)\cong\tilde K^{-n-2}(X)$ for all $n$, and in particular
> $$
> \tilde K^0(S^n)=\begin{cases}\mathbb{Z}&n\text{ even}\\0&n\text{ odd.}\end{cases}
> $$

Here "multiplication by $b$" means the **external product** $\tilde K^0(X)\otimes\tilde K^0(S^2)\to\tilde K^0(X\wedge S^2)=\tilde K^0(\Sigma^2 X)$, where $X\wedge S^2=\Sigma^2 X$ is the **smash product** (product with both axes collapsed). The external product $[E]\cdot[F]=[E\boxtimes F]$ uses the bundle $E\boxtimes F$ on $X\times Y$ with fiber $E_x\otimes F_y$.

**The idea of the proof.** There are several proofs; the cleanest conceptual one is Atiyah's via **clutching and the structure of bundles over $\Sigma^2 X = $ a double suspension**, reducing to understanding bundles on $X\times S^2$ in terms of bundles on $X$.

1. By clutching (§s3), a bundle on $X\times S^2$ trivialized over $X\times D_\pm$ is given by a clutching function $X\times S^1\to GL(E_X)$ — a loop of automorphisms of a bundle over $X$, i.e. an element of the loop space data. So $\tilde K^0(\Sigma^2 X)$ is governed by homotopy classes of such clutching functions.
2. The technical heart is the **linearization / Laurent-polynomial** argument: any clutching function (a continuous loop $S^1\to GL$) is homotopic to a **Laurent polynomial** loop $\sum_{k=-N}^{N}A_k z^k$, then by adding trivial summands to a **linear** loop $A+Bz$ (a "linear clutching function"), and finally to one of the form $z\mapsto z\cdot p+(1-p)$ for a *projection* $p$. *(Stone–Weierstrass approximation in the loop variable; stabilization absorbs the polynomial degree.)*
3. Such projection-valued data is exactly a vector bundle on $X$ (the image of $p$). This produces an explicit inverse to multiplication by $b$, proving the map is an isomorphism. *(the projection $p$ defines a sub-bundle, recovering a class in $\tilde K^0(X)$.)*

The key analytic input is just the Stone–Weierstrass theorem (trigonometric polynomials are dense in continuous loops) plus the bookkeeping that stabilization (adding trivial bundles) lets us trade high-degree loops for linear ones. No characteristic-class machinery is needed; periodicity is, at bottom, a statement about $GL(\mathbb{C})$ and Laurent polynomials.

**Sketch — the idea of the degree-shift trick.** The heart of step 2 is that a clutching loop of monomial type can be lowered in degree by one at the cost of enlarging the bundle by a trivial summand. Concretely, for the loop $z\mapsto z\cdot\mathrm{id}_{\mathbb{C}^n}$ on $S^1$:

1. Form the rank-$2n$ loop $z\mapsto\begin{pmatrix}z\,\mathrm{id}&0\\0&\mathrm{id}\end{pmatrix}$, the original $\oplus$ a trivial (degree-$0$) loop. *(direct sum corresponds to adding a trivial bundle)*
2. Conjugate/homotope within $GL_{2n}(\mathbb{C})$ by the elementary loop with identity diagonal blocks and lower-left block $(1-z)\,\mathrm{id}$ (and its partners); a short matrix computation rewrites the loop as $z\mapsto z\,p+(1-p)$ for the projection $p=\mathrm{diag}(\mathrm{id}_n,0)$, plus a constant invertible factor that is homotopic to the identity. *(row operations are paths in $GL$; $GL_{2n}(\mathbb{C})$ is path-connected so constant invertible factors are negligible)*
3. The projection $p$ is now *constant*, but in the family version over $X$ it becomes an $X$-dependent projection $p(x)$, whose image is a sub-bundle $\mathrm{im}\,p\subseteq\underline{\mathbb{C}}^{2n}$ — an honest vector bundle on $X$, the output class in $\tilde K^0(X)$. *(a continuous family of projections defines a sub-bundle)*

This is the explicit inverse to $\times b$: from a loop (a class in $\tilde K^0(\Sigma^2 X)$) it manufactures a projection, hence a bundle on $X$. Checking it is two-sided inverse to multiplication by the Bott class completes the proof; the only nontrivial analytic fact used is density of Laurent polynomials, everything else is linear algebra of projections. $\square$

**Consequences.**

- **Two groups only.** The bigraded theory collapses: $\tilde K^{-n}$ depends only on $n\bmod 2$. Define $\tilde K^{-1}(X):=\tilde K^0(\Sigma X)$ and extend to all integers $n$ by $\tilde K^{n}:=\tilde K^{n\bmod 2}$, making K-theory a **$\mathbb{Z}/2$-graded** ($2$-periodic) cohomology theory.
- **$K^0(S^2)$ confirmed.** $\tilde K^0(S^2)=\tilde K^0(\Sigma^2 S^0)\cong\tilde K^0(S^0)=\mathbb{Z}$, generated by $b=H-1$, finishing the §s3 computation rigorously.
- **Coefficients of the theory.** $K^{-n}(\mathrm{pt})=\mathbb{Z}$ for even $n$, $0$ for odd $n$: K-theory has $\mathbb{Z}$ in every even degree. The graded ring $K^*(\mathrm{pt})=\mathbb{Z}[b,b^{-1}]$ with $b$ in degree $-2$ is the **coefficient ring**; inverting $b$ is the algebraic shadow of periodicity.

> **Pitfall.** Periodicity is period $2$ for *complex* K-theory; the *real* theory $KO$ has period $8$ (§s9). Confusing the two is the most common error. The period-$2$ statement also requires the complex Bott class $b\in\tilde K^0(S^2)$; the analogous real generator lives in $\tilde{KO}^0(S^8)$.

**Worked example — $K^*(S^n)$ for all $n$.** Combining the definition $\tilde K^{-i}(S^n)=\tilde K^0(\Sigma^i S^n)=\tilde K^0(S^{n+i})$ with Bott:
$$
\tilde K^0(S^n)=\begin{cases}\mathbb{Z}&n\text{ even}\\0&n\text{ odd,}\end{cases}\qquad
\tilde K^1(S^n)=\tilde K^0(S^{n+1})=\begin{cases}0&n\text{ even}\\\mathbb{Z}&n\text{ odd.}\end{cases}
$$
So odd spheres carry K-theory only in degree $1$, even spheres only in degree $0$ — the K-theory is concentrated opposite to the parity of the dimension. Unreduced: $K^0(S^{2k})=\mathbb{Z}^2$, $K^1(S^{2k})=0$; $K^0(S^{2k+1})=\mathbb{Z}$, $K^1(S^{2k+1})=\mathbb{Z}$. Compare ordinary cohomology, which spreads $\mathbb{Z}$ across degrees $0$ and $n$; K-theory squeezes the same total rank into a single parity, the hallmark of a $2$-periodic theory.

**Worked example — $K^0(\mathbb{CP}^n)$.** Let $L$ be the tautological line bundle on complex projective space $\mathbb{CP}^n$ (fiber over a line $\ell$ is $\ell$). Set $x=[L]-1\in\tilde K^0(\mathbb{CP}^n)$. The defining relation generalizes the $S^2=\mathbb{CP}^1$ computation: $L$ satisfies $(L-1)^{n+1}=0$, because the Koszul/Euler-sequence relation on $\mathbb{CP}^n$ kills the $(n+1)$-st power. Hence
$$
K^0(\mathbb{CP}^n)\cong\mathbb{Z}[x]/(x^{n+1}),
$$
a free $\mathbb{Z}$-module of rank $n+1$ with basis $1,x,\dots,x^n$, and $K^1(\mathbb{CP}^n)=0$. This matches $\sum_k\mathrm{rank}\,H^{2k}(\mathbb{CP}^n)=n+1$, as the Chern character will confirm (§s7). The truncated-polynomial ring is the K-theoretic shadow of the cohomology ring $H^*(\mathbb{CP}^n)=\mathbb{Z}[t]/(t^{n+1})$, with $x\leftrightarrow$ a unit times $t$ plus higher-order corrections.

<a id="s6"></a>
### The long exact sequence; K-theory as a generalized cohomology theory

We now verify that $\{\tilde K^{-n}\}$ obeys the Eilenberg–Steenrod axioms minus the dimension axiom — the definition of a (reduced) **generalized cohomology theory**.

> **Definition — reduced generalized cohomology theory.** A sequence of contravariant homotopy functors $\tilde h^n$ ($n\in\mathbb{Z}$) from pointed compact spaces to abelian groups, with natural **suspension isomorphisms** $\sigma:\tilde h^n(X)\cong\tilde h^{n+1}(\Sigma X)$, such that for every pointed pair (cofibration $A\hookrightarrow X$) the sequence
> $$
> \tilde h^n(X/A)\to\tilde h^n(X)\to\tilde h^n(A)
> $$
> is exact, satisfying the **wedge axiom** $\tilde h^n(\bigvee_\alpha X_\alpha)\cong\prod_\alpha\tilde h^n(X_\alpha)$. Dropping the *dimension axiom* ($\tilde h^n(S^0)=0$ for $n\ne 0$) is what makes it "generalized."

**The exact sequence of a pair.** The foundational exactness is for $K^0$ and a cofibration.

> **Proposition (exactness).** For a compact pair $(X,A)$, the inclusion $i:A\hookrightarrow X$ and collapse $q:X\to X/A$ give an exact sequence
> $$
> \tilde K^0(X/A)\xrightarrow{q^*}\tilde K^0(X)\xrightarrow{i^*}\tilde K^0(A).
> $$

**Demonstration (exactness at $\tilde K^0(X)$).**

1. **$i^*q^*=0$.** The composite $A\xrightarrow{i}X\xrightarrow{q}X/A$ sends $A$ to the basepoint, so it is null-homotopic; hence $i^*q^*=(q i)^*=0$ on reduced K-theory. *(homotopy invariance; reduced K of a point is $0$)*
2. **$\ker i^*\subseteq\mathrm{im}\,q^*$.** Take $[E]-[\underline{\mathbb{C}}^n]\in\ker i^*$, so $E|_A\oplus\underline{\mathbb{C}}^k\cong\underline{\mathbb{C}}^{n+k}|_A$ — i.e. $E$ (stabilized) is *trivial over $A$* via some isomorphism $\alpha$. A trivialization over $A$ lets us collapse $A$: the bundle $E\oplus\underline{\mathbb{C}}^k$ descends to a bundle $\bar E$ on $X/A$ (glue the trivialized fibers over $A$ to the single fiber over the basepoint using $\alpha$), and $q^*\bar E\cong E\oplus\underline{\mathbb{C}}^k$. Thus $[E]-[\underline{\mathbb{C}}^n]=q^*([\bar E]-[\underline{\mathbb{C}}^{n+k}])$. *(a bundle trivialized over $A$ is pulled back from the quotient — the difference-bundle description of §s4)*
3. Steps 1–2 give $\mathrm{im}\,q^*=\ker i^*$, exactness. $\square$

**Extending to a long exact sequence.** Splicing in suspensions via the **Puppe/cofiber sequence** $A\to X\to X/A\to\Sigma A\to\Sigma X\to\cdots$ and applying $\tilde K^0$ to each term, with the identification $\tilde K^0(\Sigma^k Y)=\tilde K^{-k}(Y)$, yields the **long exact sequence of the pair**:
$$
\cdots\to K^{-1}(A)\xrightarrow{\partial}K^0(X,A)\to K^0(X)\to K^0(A)\xrightarrow{\partial}K^1(X,A)\to\cdots
$$
By Bott periodicity ($K^{-2}\cong K^0$, $K^{-1}\cong K^1$) this wraps into a **six-term cyclic exact sequence**:
$$
\begin{array}{ccccc}
K^0(X,A)&\to&K^0(X)&\to&K^0(A)\\
\uparrow&&&&\downarrow\\
K^1(A)&\leftarrow&K^1(X)&\leftarrow&K^1(X,A)
\end{array}
$$
This six-term sequence — impossible in ordinary $\mathbb{Z}$-graded cohomology — is the computational workhorse of K-theory and the form in which it appears in operator algebras (§s10).

> **Verification of the axioms (summary).**
> *Functoriality + homotopy invariance:* §s1–s2. *Suspension iso:* built into the definition $\tilde K^{-n}(X)=\tilde K^0(\Sigma^n X)$. *Exactness:* the Proposition above, splice with Puppe. *Wedge axiom:* a bundle on a wedge $\bigvee X_\alpha$ restricts compatibly to each summand, and conversely glues, giving $\tilde K^0(\bigvee X_\alpha)\cong\prod\tilde K^0(X_\alpha)$. All Eilenberg–Steenrod axioms hold except dimension, which fails precisely because $K^{-2n}(\mathrm{pt})=\mathbb{Z}\ne 0$.

**Worked example — Mayer–Vietoris from the six-term sequence.** For $X=U\cup V$ (closed, nice), the relative sequences combine into
$$
\cdots\to K^0(X)\to K^0(U)\oplus K^0(V)\to K^0(U\cap V)\xrightarrow{\partial}K^1(X)\to\cdots,
$$
which recomputes $K^0(S^2)=\mathbb{Z}^2$: take $U,V$ the two hemispheres (each contractible, $K^0=\mathbb{Z}$) with $U\cap V\simeq S^1$ ($\tilde K^0(S^1)=0$, $K^1(S^1)=\mathbb{Z}$). The sequence forces $\tilde K^0(S^2)\cong\tilde K^1(S^1)\cong K^{-1}(\mathrm{pt})$-shift $=\mathbb{Z}$, consistent with Bott.

**Worked example — $K^*(S^1)$ from the six-term sequence, step by step.** Write $S^1=U\cup V$ as two overlapping arcs, each contractible, with $U\cap V\simeq\{2\text{ points}\}=S^0$. Reduced Mayer–Vietoris in K-theory reads
$$
\cdots\to\tilde K^0(S^1)\to\tilde K^0(U)\oplus\tilde K^0(V)\to\tilde K^0(S^0)\xrightarrow{\partial}\tilde K^1(S^1)\to\tilde K^1(U)\oplus\tilde K^1(V)\to\cdots
$$
Now $\tilde K^*(U)=\tilde K^*(V)=0$ (contractible). The sequence collapses to $0\to\tilde K^0(S^1)\to0$ and $0\to\tilde K^0(S^0)\xrightarrow{\partial}\tilde K^1(S^1)\to0$. The first gives $\tilde K^0(S^1)=0$. The second gives $\tilde K^1(S^1)\cong\tilde K^0(S^0)=\mathbb{Z}$. So $K^0(S^1)=\mathbb{Z}$, $K^1(S^1)=\mathbb{Z}$ — every step justified by exactness and the vanishing of reduced K-theory on contractible pieces, with no appeal to Bott. The connecting map $\partial$ here is the geometric origin of the degree-$1$ generator of $K^1(S^1)$: a unit $z\mapsto z$ on the overlap, the same winding that built the Möbius/Hopf clutching data.

---

## Part C · Bridges to cohomology and index theory

<a id="s7"></a>
### The Chern character and the rational isomorphism

K-theory and ordinary cohomology are different integrally (K-theory is $2$-periodic; $H^*$ is not), yet they become the *same* after tensoring with $\mathbb{Q}$. The comparison map is the **Chern character**, built from Chern classes.

> **Recall (from Differential Topology).** A complex vector bundle $E$ on $X$ has **Chern classes** $c_i(E)\in H^{2i}(X;\mathbb{Z})$, with total class $c(E)=1+c_1(E)+c_2(E)+\cdots$, satisfying the **Whitney sum formula** $c(E\oplus F)=c(E)\,c(F)$ (cup product) and naturality $c(f^*E)=f^*c(E)$. For a line bundle $L$, $c(L)=1+c_1(L)$.

The Chern character is the unique ring map $K^0\to H^{\mathrm{even}}(\,\cdot\,;\mathbb{Q})$ that is additive *and* multiplicative; the trick to define it is the **splitting principle** plus the exponential of Chern roots.

> **Definition — Chern character.** Suppose (splitting principle) $E$ formally splits as a sum of line bundles, $c(E)=\prod_{j=1}^n(1+x_j)$, where the **Chern roots** $x_j\in H^2$ are formal; the $i$-th elementary symmetric polynomial in the $x_j$ is $c_i(E)$. Define
> $$
> \mathrm{ch}(E)=\sum_{j=1}^n e^{x_j}=\sum_{j=1}^n\Big(1+x_j+\tfrac{x_j^2}{2!}+\cdots\Big)\in H^{\mathrm{even}}(X;\mathbb{Q}).
> $$
> Because $\sum_j e^{x_j}$ is symmetric in the $x_j$, it is a polynomial in the $c_i(E)$, so $\mathrm{ch}(E)$ is well-defined without reference to the formal splitting. Low terms:
> $$
> \mathrm{ch}(E)=\mathrm{rk}(E)+c_1(E)+\tfrac12\big(c_1(E)^2-2c_2(E)\big)+\cdots
> $$

**Demonstration — the low-order terms of $\mathrm{ch}$, derived.** Expand $\sum_j e^{x_j}=\sum_j(1+x_j+\tfrac{x_j^2}{2}+\cdots)$ and collect by cohomological degree using the elementary symmetric polynomials $e_k=c_k$ (Newton's identities relate power sums $p_k=\sum_j x_j^k$ to the $e_k$):

1. **Degree $0$:** $\sum_j 1=n=\mathrm{rk}(E)$. *(there are $n$ Chern roots)*
2. **Degree $2$:** $\sum_j x_j=p_1=e_1=c_1(E)$. *(Newton: $p_1=e_1$)*
3. **Degree $4$:** $\tfrac12\sum_j x_j^2=\tfrac12 p_2$. Newton's identity $p_2=e_1^2-2e_2$ gives $\tfrac12 p_2=\tfrac12(c_1^2-2c_2)=\tfrac12 c_1^2-c_2$. *(Newton: $p_2=e_1^2-2e_2$)*

So $\mathrm{ch}(E)=n+c_1+(\tfrac12 c_1^2-c_2)+\cdots$, the formula quoted above, now derived rather than asserted. The half-integer coefficient $\tfrac12$ is the structural reason the Chern character does not preserve integral lattices and only becomes an isomorphism after $\otimes\mathbb{Q}$.

> **Theorem (Chern character is a ring homomorphism).** $\mathrm{ch}:K^0(X)\to H^{\mathrm{even}}(X;\mathbb{Q})$ is a well-defined ring homomorphism: $\mathrm{ch}(E\oplus F)=\mathrm{ch}(E)+\mathrm{ch}(F)$ and $\mathrm{ch}(E\otimes F)=\mathrm{ch}(E)\,\mathrm{ch}(F)$.

**Demonstration of additivity and multiplicativity.**

1. **Additivity.** Chern roots of $E\oplus F$ are the union of those of $E$ and $F$ (Whitney formula $c(E\oplus F)=c(E)c(F)$ multiplies the factors $\prod(1+x_j)$). Hence $\mathrm{ch}(E\oplus F)=\sum_{j}e^{x_j}+\sum_k e^{y_k}=\mathrm{ch}(E)+\mathrm{ch}(F)$. Because $\mathrm{ch}$ is additive on $\oplus$, it extends to a homomorphism on the Grothendieck group $K^0$ by $\mathrm{ch}([E]-[F])=\mathrm{ch}(E)-\mathrm{ch}(F)$. *(universal property of $\mathcal G$, §s2)*
2. **Multiplicativity.** A line bundle has Chern root $x_j$; the tensor of lines $L\otimes M$ has first Chern class $c_1(L)+c_1(M)$ (Chern classes of line bundles add under $\otimes$), so its Chern root is $x_j+y_k$. Then the Chern roots of $E\otimes F$ are all sums $x_j+y_k$, and
> $$
> \mathrm{ch}(E\otimes F)=\sum_{j,k}e^{x_j+y_k}=\Big(\sum_j e^{x_j}\Big)\Big(\sum_k e^{y_k}\Big)=\mathrm{ch}(E)\,\mathrm{ch}(F),
> $$
> using $e^{a+b}=e^ae^b$. *(exponential law; bilinearity of $\otimes$ over $\oplus$)* $\square$

> **Theorem (rational isomorphism / Chern character iso).** For a finite CW complex $X$, the Chern character induces an isomorphism of $\mathbb{Z}/2$-graded rings
> $$
> \mathrm{ch}:K^*(X)\otimes_{\mathbb{Z}}\mathbb{Q}\ \xrightarrow{\ \cong\ }\ H^{\mathrm{even}}(X;\mathbb{Q})\oplus H^{\mathrm{odd}}(X;\mathbb{Q})=H^*(X;\mathbb{Q}),
> $$
> with $K^0\otimes\mathbb{Q}\cong H^{\mathrm{even}}$ and $K^1\otimes\mathbb{Q}\cong H^{\mathrm{odd}}$.

*Idea of proof.* Both sides are generalized cohomology theories (the right side via $H^{\mathrm{even/odd}}$ made $2$-periodic with $\mathbb{Q}$ coefficients), $\mathrm{ch}$ is a natural transformation between them, and it is an isomorphism on a point ($K^0(\mathrm{pt})\otimes\mathbb{Q}=\mathbb{Q}=H^0(\mathrm{pt};\mathbb{Q})$, all higher terms $0$). A natural transformation of cohomology theories that is an isomorphism on the point is an isomorphism on all finite complexes — this is the **comparison theorem**, proved by induction on cells using the five lemma and the long exact sequences. $\square$

**Worked example — $S^2$.** $\mathrm{ch}(H-1)=\mathrm{ch}(H)-1=e^{c_1(H)}-1=c_1(H)+\tfrac12 c_1(H)^2+\cdots$. On $S^2$, $c_1(H)$ generates $H^2(S^2;\mathbb{Z})=\mathbb{Z}$ and $c_1(H)^2\in H^4(S^2)=0$. So $\mathrm{ch}(H-1)=c_1(H)$, the generator of $H^2$. Thus $\mathrm{ch}$ sends the Bott generator $H-1$ of $\tilde K^0(S^2)=\mathbb{Z}$ to the generator of $H^2(S^2;\mathbb{Z})$, an isomorphism already over $\mathbb{Z}$ here. The integral lattices differ in general (e.g. on $\mathbb{CP}^n$ the $\mathrm{ch}$-image is not all of $H^{\mathrm{even}}(\mathbb{Z})$), which is why the clean statement needs $\otimes\mathbb{Q}$.

**Worked example — $\mathrm{ch}$ on $\mathbb{CP}^2$ with real numbers.** Let $t=c_1(L^{-1})\in H^2(\mathbb{CP}^2;\mathbb{Z})$ be the standard generator, so $H^*(\mathbb{CP}^2)=\mathbb{Z}[t]/(t^3)$ with $t,t^2$ generating $H^2,H^4$. For the dual line bundle the Chern root is $-t$ ... take instead $L^*$ with $c_1(L^*)=t$. Then
$$
\mathrm{ch}(L^*)=e^{t}=1+t+\tfrac{t^2}{2},\qquad \mathrm{ch}((L^*)^{\otimes 2})=e^{2t}=1+2t+2t^2,
$$
since $t^3=0$. As a check of multiplicativity, $\mathrm{ch}(L^*)^2=(1+t+\tfrac{t^2}{2})^2=1+2t+(1+1)t^2+\cdots=1+2t+2t^2$ (dropping $t^3,t^4$), matching $\mathrm{ch}((L^*)^2)$. The basis $\{1,\ L^*-1,\ (L^*-1)^2\}$ of $K^0(\mathbb{CP}^2)$ maps under $\mathrm{ch}$ to $\{1,\ t+\tfrac{t^2}{2},\ t^2\}$ (compute $(L^*-1)^2$: $\mathrm{ch}=(t+\tfrac{t^2}2)^2=t^2$), a $\mathbb{Q}$-basis of $H^{\mathrm{even}}(\mathbb{CP}^2;\mathbb{Q})=\mathbb{Q}\{1,t,t^2\}$ — confirming the rational isomorphism by exhibiting it on basis elements. Note the image $\{1, t+\tfrac{t^2}2, t^2\}$ is *not* the integral lattice $\{1,t,t^2\}$ (the middle vector has a half-integer $t^2$-coefficient), the concrete reason $\mathrm{ch}$ is an iso only after $\otimes\mathbb{Q}$.

> **Pitfall.** $\mathrm{ch}$ is an iso only after $\otimes\mathbb{Q}$. Integrally, K-theory carries *more* information than $H^*$: torsion phenomena and the integral lattice are genuinely different, which is exactly why K-theory detects things (like certain D-brane charges, §s11) that cohomology misses.

<a id="s8"></a>
### The Thom isomorphism, K-orientation, and the push-forward

To do *integration* in K-theory — to define a Gysin map / push-forward along a map of manifolds, the K-theoretic analogue of integrating a form — we need the K-theory Thom isomorphism and the notion of K-orientation.

> **Definition — Thom space.** For a rank-$n$ complex vector bundle $\pi:V\to X$ with a Hermitian metric, the **Thom space** is $X^V:=D(V)/S(V)$, the unit disk bundle with the unit sphere bundle collapsed. For a trivial bundle $X^{\underline{\mathbb{C}}^n}=\Sigma^{2n}(X_+)$.

> **Theorem (Thom isomorphism in K-theory).** Let $V\to X$ be a rank-$n$ complex vector bundle. There is a **Thom class** $\lambda_V\in\tilde K^0(X^V)$ such that multiplication by it is an isomorphism
> $$
> \Phi:K^0(X)\xrightarrow{\ \cong\ }\tilde K^0(X^V),\qquad \Phi(a)=\pi^*a\cdot\lambda_V.
> $$

**Construction of the Thom class (the K-theory Koszul/exterior class).** Over the total space of $V$, form the **exterior algebra complex**
$$
0\to\Lambda^0 V\xrightarrow{\,\wedge v\,}\Lambda^1 V\xrightarrow{\,\wedge v\,}\Lambda^2 V\to\cdots\to\Lambda^n V\to 0,
$$
where at the point $v\in V_x$ the map is exterior multiplication by the vector $v$. Off the zero section ($v\ne 0$) this complex is **exact** (the Koszul complex of a nonzero vector is acyclic — contract with $v/|v|^2$ to get a chain homotopy to zero). A complex of bundles exact outside a compact set (here, outside the disk's interior, after restricting to $D(V)$ and noting exactness on $S(V)$) defines a difference class supported on $X^V$:
$$
\lambda_V=\Big[\textstyle\sum_{i\ \mathrm{even}}\Lambda^i V\Big]-\Big[\textstyle\sum_{i\ \mathrm{odd}}\Lambda^i V\Big]\in\tilde K^0(X^V),
$$
the alternating sum $\sum_i(-1)^i[\Lambda^i V]$, trivialized over $S(V)$ by the Koszul homotopy (the difference-bundle description of §s4). That $\Phi$ is an isomorphism reduces, via clutching and Bott periodicity, to the case $V=\underline{\mathbb{C}}^n$ where $\tilde K^0(\Sigma^{2n}X_+)=\tilde K^{-2n}(X_+)\cong K^0(X)$ is exactly periodicity. $\square$

> **Definition — K-orientation; complex bundles are K-oriented.** A real vector bundle (or a map of manifolds via its stable normal/tangent bundle) is **K-orientable** if its Thom space carries a Thom class making $\Phi$ an isomorphism. The construction above shows **every complex vector bundle is canonically K-oriented**. More generally a real bundle is K-orientable iff it admits a $\mathrm{Spin}^c$ structure — the K-theoretic refinement of orientability. *(orientability $\leftrightarrow$ $w_1=0$ for ordinary cohomology; K-orientability $\leftrightarrow$ $\mathrm{Spin}^c$, i.e. $W_3=0$.)*

> **Definition — push-forward (Gysin map).** Let $f:X\to Y$ be a smooth map of closed manifolds that is K-oriented (e.g. an embedding with complex normal bundle, or any map between $\mathrm{Spin}^c$ manifolds). Then there is a **push-forward** (wrong-way / Gysin map)
> $$
> f_!:K^*(X)\to K^{*+d}(Y),\qquad d=\dim Y-\dim X,
> $$
> built by: (i) embedding $X\hookrightarrow Y\times\mathbb{R}^N$; (ii) applying the Thom isomorphism on a tubular neighborhood (its normal bundle is K-oriented); (iii) extending by zero and using Bott periodicity to descend the suspension. It satisfies functoriality $(g\circ f)_!=g_!f_!$ and the **projection formula** $f_!(f^*b\cdot a)=b\cdot f_!(a)$.

**Worked example — the Thom class of a line bundle over a point.** Take $X=\mathrm{pt}$ and $V=\mathbb{C}$ (a rank-$1$ bundle over a point). The Thom space is $\mathrm{pt}^{\mathbb{C}}=D^2/S^1=S^2$. The exterior-algebra complex is $0\to\Lambda^0\mathbb{C}=\mathbb{C}\xrightarrow{\wedge v}\Lambda^1\mathbb{C}=\mathbb{C}\to0$, i.e. multiplication by the scalar $v$, an isomorphism for $v\ne0$. The Thom class is $\lambda_V=[\Lambda^0]-[\Lambda^1]$ trivialized off $0$, which in $\tilde K^0(S^2)$ is exactly $-(H-1)$ up to sign — the Bott generator. So the K-theory Thom isomorphism $K^0(\mathrm{pt})=\mathbb{Z}\xrightarrow{\cong}\tilde K^0(S^2)=\mathbb{Z}$, $1\mapsto\lambda_V$, *is* Bott periodicity in disguise. This is the cleanest way to see why "the Thom class of $\underline{\mathbb{C}}^n$ generates $\tilde K^0(S^{2n})$" and why complex bundles being K-oriented is built on the same periodicity.

**Worked example — push-forward to a point and the index.** For $X$ a closed $\mathrm{Spin}^c$ manifold and $f:X\to\mathrm{pt}$, the push-forward
$$
f_!:K^0(X)\to K^0(\mathrm{pt})=\mathbb{Z}
$$
is the **K-theoretic integration / topological index**. The Atiyah–Singer index theorem (§s10) identifies $f_!([E])$ with the analytic index of a twisted Dirac operator, and the **Riemann–Roch–Grothendieck** compatibility
$$
\mathrm{ch}(f_!a)=f_*\big(\mathrm{ch}(a)\cdot\mathrm{Td}(X)\big)
$$
(where $f_*$ is ordinary cohomological integration and $\mathrm{Td}$ is the Todd class) is the precise statement that K-theory push-forward and cohomology integration agree up to the Todd correction — the source of the $\hat A$- and Todd-genus formulas in the index theorem.

---

## Part D · Variants, analysis, and physics

<a id="s9"></a>
### Clifford algebras and real K-theory ($KO$); the eightfold periodicity

Replacing complex bundles by **real** vector bundles gives **real K-theory** $KO^*(X)$, the Grothendieck group of real bundles under $\oplus$. The structure is governed by **Clifford algebras**, and the periodicity is $8$, not $2$.

> **Definition — Clifford algebra.** For $\mathbb{R}^n$ with the standard negative-definite form, the **Clifford algebra** $\mathrm{Cl}_n$ is the associative real algebra generated by $e_1,\dots,e_n$ subject to $e_ie_j+e_je_i=-2\delta_{ij}$. (So $e_i^2=-1$ and distinct generators anticommute.) Its representation theory is $8$-periodic: $\mathrm{Cl}_{n+8}\cong\mathrm{Cl}_n\otimes\mathbb{R}(16)$ (matrix algebra), a fact due to the real division algebras $\mathbb{R},\mathbb{C},\mathbb{H}$.

> **Theorem (real Bott periodicity).** $\tilde{KO}^{-n}(\mathrm{pt})=\tilde{KO}^0(S^n)$ is $8$-periodic in $n$, with values
> $$
> \begin{array}{c|cccccccc}
> n\bmod 8 & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7\\\hline
> KO^{-n}(\mathrm{pt}) & \mathbb{Z} & \mathbb{Z}/2 & \mathbb{Z}/2 & 0 & \mathbb{Z} & 0 & 0 & 0
> \end{array}
> $$
> and $KO^{-n-8}(\mathrm{pt})\cong KO^{-n}(\mathrm{pt})$.

The connection to Clifford algebras (Atiyah–Bott–Shapiro): the difference $KO^{-n}(\mathrm{pt})\cong M_n/i^*M_{n+1}$ where $M_n$ is the Grothendieck group of $\mathrm{Cl}_n$-modules and $i^*$ restricts along $\mathrm{Cl}_n\hookrightarrow\mathrm{Cl}_{n+1}$ — the representation theory of Clifford algebras *computes* the homotopy groups, and the $8$-fold periodicity of Clifford modules is real Bott periodicity. The appearance of $\mathbb{Z}/2$ in degrees $1,2$ is genuinely torsion and invisible to any rational invariant — a phenomenon ordinary cohomology with $\mathbb{Q}$ cannot see.

> **Overview — the periodicity clock.** Complex K-theory: period $2$, coefficients $\mathbb{Z},0,\mathbb{Z},0,\dots$ (driven by $\mathbb{C}$, one division algebra step). Real K-theory: period $8$, coefficients as above (driven by the $\mathbb{R}\to\mathbb{C}\to\mathbb{H}$ tower). There is also a "quaternionic / symplectic" theory $KSp$, and complexification $KO^*\to K^*$, realification $K^*\to KO^*$ relating them. The eightfold pattern is the same one appearing in the classification of free fermion topological phases (§s11) — the "tenfold way."

**Worked example — small Clifford algebras and the start of the table.** Compute the first few $\mathrm{Cl}_n$ from $e_ie_j+e_je_i=-2\delta_{ij}$:
$$
\mathrm{Cl}_0=\mathbb{R},\quad \mathrm{Cl}_1=\mathbb{C}\ (e_1^2=-1),\quad \mathrm{Cl}_2=\mathbb{H}\ (e_1,e_2,e_1e_2\text{ behave as }i,j,k),\quad \mathrm{Cl}_3=\mathbb{H}\oplus\mathbb{H}.
$$
The real division algebras $\mathbb{R},\mathbb{C},\mathbb{H}$ appear in the first three steps, and after eight steps a $16\times16$ real matrix algebra is reached, $\mathrm{Cl}_8\cong\mathbb{R}(16)$, whose module theory is Morita-equivalent to $\mathbb{R}=\mathrm{Cl}_0$ — this Morita equivalence *is* the eightfold periodicity. The $\mathbb{Z}/2$ entries $KO^{-1},KO^{-2}$ trace back to $\mathrm{Cl}_1=\mathbb{C}$ and $\mathrm{Cl}_2=\mathbb{H}$ having a restricted set of module dimensions, producing torsion in the cokernel $M_n/i^*M_{n+1}$.

**Worked example — $\tilde{KO}^0(S^1)=\mathbb{Z}/2$ concretely.** Real line bundles on $S^1$ are clutched by $\pi_0(GL_1(\mathbb{R}))=\pi_0(\mathbb{R}^\times)=\{\pm\}=\mathbb{Z}/2$: the trivial cylinder ($+$) and the Möbius band ($-$). In $\tilde{KO}^0(S^1)$ the Möbius class $\mu$ satisfies $2\mu=0$ because $\mu\oplus\mu$ (clutching $\mathrm{diag}(-1,-1)\in GL_2(\mathbb{R})$, which lies in the identity component) is trivial. This matches the table entry $KO^{-1}(\mathrm{pt})=\tilde{KO}^0(S^1)=\mathbb{Z}/2$ — a torsion class no rational or complex invariant can see, and the prototype of the $\mathbb{Z}_2$ topological insulator invariant (§s11).

<a id="s10"></a>
### Operator/analytic K-theory and K-homology; the link to index theory

K-theory has a purely analytic incarnation that works for (noncommutative) algebras, unifying with operator theory.

> **Definition — K-theory of a C\*-algebra.** For a unital C\*-algebra $A$ (a complex Banach $*$-algebra with $\|a^*a\|=\|a\|^2$, e.g. $A=C(X)$, continuous functions on compact $X$), define $K_0(A)$ as the Grothendieck group of **projections** $p=p^*=p^2$ in matrix algebras $M_\infty(A)$ up to (Murray–von Neumann) equivalence and stabilization, and $K_1(A)$ via homotopy classes of unitaries in $M_\infty(A)$. **Serre–Swan / Gelfand:** for $A=C(X)$, finitely generated projective $A$-modules correspond to vector bundles on $X$, giving
> $$
> K_0(C(X))\cong K^0(X),\qquad K_1(C(X))\cong K^1(X).
> $$
> Thus topological K-theory is the commutative case of operator K-theory; the latter extends the theory to *noncommutative spaces*.

The six-term exact sequence (§s6) appears here for an ideal $0\to I\to A\to A/I\to 0$, the cornerstone of computations in operator algebras.

**Worked example — the Toeplitz extension and the index of a Toeplitz operator.** A foundational operator-K computation: the Toeplitz C\*-algebra $\mathcal T$ (generated by the unilateral shift $S$ on $\ell^2(\mathbb{N})$) sits in a short exact sequence
$$
0\to\mathcal K\to\mathcal T\xrightarrow{\sigma}C(S^1)\to0,
$$
where $\mathcal K$ is the compact operators and $\sigma$ is the symbol map. The six-term sequence with $K_0(\mathcal K)=\mathbb{Z}$, $K_1(\mathcal K)=0$, $K_0(C(S^1))=\mathbb{Z}$, $K_1(C(S^1))=\mathbb{Z}$ has connecting map $\partial:K_1(C(S^1))=\mathbb{Z}\to K_0(\mathcal K)=\mathbb{Z}$ equal to **minus the winding number**: for an invertible symbol $f:S^1\to\mathbb{C}^\times$, the Toeplitz operator $T_f$ is Fredholm with $\mathrm{ind}(T_f)=-\mathrm{wind}(f)$. This is the simplest index theorem, and it is *computed by the K-theory boundary map* — the winding number of §s3 reappearing as an analytic index. It is the $1$-dimensional prototype of Atiyah–Singer.

> **Definition — K-homology.** The dual theory $K_*(X)$ (**K-homology**) is represented by **Fredholm modules** / abstract elliptic operators: a class is (roughly) a Hilbert space with a representation of $C(X)$ and a self-adjoint Fredholm operator $F$ that almost commutes with the representation. Concretely, an **elliptic differential operator** $D$ on a manifold $X$ (e.g. a Dirac operator) defines a K-homology class $[D]\in K_*(X)$.

> **Theorem (Atiyah–Singer index theorem, K-theoretic form).** For an elliptic operator $D$ on a closed manifold $X$, the **analytic index** $\mathrm{ind}(D)=\dim\ker D-\dim\mathrm{coker}\,D\in\mathbb{Z}$ equals the **topological index**: the pairing of the symbol class $[\sigma_D]\in K^0(TX)$ with the fundamental class, computed by pushing forward to a point,
> $$
> \mathrm{ind}(D)=p_!\,[\sigma_D]\in K^0(\mathrm{pt})=\mathbb{Z}.
> $$
> Via the Chern character and the Riemann–Roch formula (§s8) this becomes the cohomological index formula $\mathrm{ind}(D)=\int_X\mathrm{ch}(\sigma_D)\,\mathrm{Td}(TX\otimes\mathbb{C})$.

**Worked example — the index theorem on the torus and the simplest Gauss–Bonnet check.** For the de Rham / Euler operator $D=d+d^*$ on a closed oriented surface $\Sigma$, the analytic index is $\dim\ker-\dim\mathrm{coker}=\sum_k(-1)^k b_k=\chi(\Sigma)$, the Euler characteristic. The topological side computes $\int_\Sigma e(T\Sigma)$, the integral of the Euler class. On the torus $T^2$, $\chi=0$ and indeed $\int_{T^2}e=0$ (the torus is parallelizable, Euler class zero); on $S^2$, $\chi=2=\int_{S^2}e$. The K-theoretic statement packages the symbol of $d+d^*$ as a class in $K^0(T\Sigma)$ and pushes it to $\mathbb{Z}$, returning $\chi$ — the same number three ways (algebraic-topological alternating sum, analytic index, curvature integral), now seen as a single K-theory push-forward. This is the index theorem specializing to the classical Gauss–Bonnet theorem, with K-theory as the bookkeeping that makes the generalization to *any* elliptic operator automatic.

*Why K-theory is the natural language.* The index is **stable** (unchanged by adding invertible operators, by deformation of $D$, by stabilization of bundles) — exactly the equivalence relation K-theory imposes. The index map is literally the K-theory push-forward $p_!$ of §s8; Bott periodicity is what makes the symbol class on the *noncompact* $TX$ well-defined and the push-forward computable. The pairing $K^*(X)\times K_*(X)\to\mathbb{Z}$ between K-theory (bundles/symbols) and K-homology (operators) *is* the index, and the index theorem says the analytic and topological computations of this pairing coincide. This is the modern, most flexible statement of index theory and the gateway to the Baum–Connes conjecture and noncommutative geometry.

<a id="s11"></a>
### Physics — D-brane charges and the K-theory classification of topological phases of matter

K-theory is not merely an organizing principle for mathematicians; it is the correct home for two physical classification problems.

**D-brane charges in string theory (overview).** In Type II string theory, a **D-brane** is an extended object on which open strings end, carrying a gauge field (a Chan–Paton bundle) on its worldvolume. Naively a D-brane wrapping a cycle carries a charge in ordinary cohomology (the cycle's homology class with a Chern character of the gauge bundle). The refinement, due to Minasian–Moore and Witten:

> **Principle — D-brane charge lives in K-theory.** The conserved charge of a D-brane configuration in spacetime $X$ is classified by $K^0(X)$ (Type IIB) or $K^1(X)$ (Type IIA), not merely by $H^{\mathrm{even/odd}}(X;\mathbb{Z})$.

The physical reasons map precisely onto K-theory structure: (i) **brane–antibrane annihilation** is exactly the Grothendieck relation $[E]-[E]=0$ — a brane with bundle $E$ and an antibrane with bundle $E$ cancel, so only the virtual difference matters; (ii) **tachyon condensation** on a brane–antibrane pair $(E,F)$ with a tachyon field $T:E\to F$ produces, via the difference-bundle/Koszul construction, exactly the K-theory class $[E]-[F]$ supported where $T$ fails to be invertible — this is the Atiyah–Bott–Shapiro / Thom-class construction of §s8; (iii) the **Freed–Witten anomaly** says a brane can only wrap a $\mathrm{Spin}^c$ cycle — precisely the K-orientability condition of §s8. Subtleties (the H-flux) push the classification to **twisted K-theory**.

**Topological phases of matter (overview).** A **topological phase** of a gapped quantum system is an equivalence class of Hamiltonians under continuous deformation that keeps the energy gap open. For free fermions with given symmetries (time-reversal $T$, particle-hole $C$, chiral $S$), the **tenfold way** (Altland–Zirnbauer) organizes systems into ten symmetry classes, and:

> **Principle — topological phases are classified by K-theory.** The set of topological phases of free fermions in spatial dimension $d$ with a given symmetry class is a K-theory group; the ten classes correspond to the ten real/complex K-theory functors, and the dependence on $d$ follows the Bott periodicity clock — the $8$-fold real periodicity (§s9) is the **periodic table of topological insulators and superconductors** (Kitaev).

Concretely, the gapped Hamiltonian defines, via its occupied-states bundle (the projection onto negative-energy states), a class in $K^0$ or $KO^j$ of the Brillouin-zone torus / momentum space; topological invariants like the Chern number (integer quantum Hall) are $\mathrm{ch}$ of this class (§s7), while $\mathbb{Z}/2$ invariants (the quantum spin Hall / $\mathbb{Z}_2$ topological insulator) are exactly the torsion entries $\mathbb{Z}/2$ in the $KO$ table (§s9) — invisible to any cohomological/Chern-number invariant, and detectable only by K-theory. The eightfold shift of the table as one changes dimension or symmetry class is Bott periodicity made physical: the same algebra of Clifford modules that computes $KO^*(\mathrm{pt})$ predicts which phases exist.

**Worked example — the integer quantum Hall effect as a Chern number.** A $2$D electron gas in a magnetic field at filling of $\nu$ Landau levels has momentum space the Brillouin torus $T^2$. The occupied bands assemble into a rank-$\nu$ complex bundle $E\to T^2$, defining a class $[E]\in K^0(T^2)$. Its topological content is the first Chern number
$$
c_1(E)=\frac{1}{2\pi}\int_{T^2}F\in\mathbb{Z},
$$
the integral of the Berry curvature $F$ — equal to $\mathrm{ch}_1(E)$, the degree-$2$ part of the Chern character (§s7). The TKNN formula identifies the Hall conductance $\sigma_{xy}=c_1(E)\cdot e^2/h$: the quantized plateau is literally the integer K-theory invariant of the band bundle. Here $K^0$, complex (no antiunitary symmetry), class A of the tenfold way, in $d=2$ — and the table predicts $K^0(\mathrm{pt})$-type invariant $\mathbb{Z}$, exactly the observed integer quantization. The same bundle on $S^2$ (a single Dirac monopole, $c_1=1$) is the Hopf bundle $H$ of §s3: the IQHE generator and the Bott generator are the same object.

> **The unifying picture.** A bundle of ground states $\to$ a K-theory class $\to$ invariants via the Chern character (integer invariants) and the torsion of $KO$ ($\mathbb{Z}/2$ invariants), with Bott periodicity dictating the pattern across dimensions. Mathematics built to classify vector bundles turns out to count D-brane charges and tabulate states of matter — the same stability and periodicity that made K-theory computable make it physically inevitable.

---

*A first course in topological K-theory — from vector bundles and the Grothendieck group, through Bott periodicity and the generalized-cohomology axioms, to the Chern character, the Thom isomorphism and push-forward, and the analytic and physical incarnations of the theory. Read once for the architecture: bundles become a ring, the ring becomes a $2$-periodic cohomology theory, and that periodicity — a fact about $GL(\mathbb{C})$ and Laurent polynomials — is what lets K-theory compute the index of an elliptic operator, count the charge of a D-brane, and tabulate the topological phases of matter. Return to any boxed definition or demonstration as a reference, and keep the slogan in view: K-theory remembers a bundle only up to stabilization, and that forgetting is exactly what makes it rigid, periodic, and powerful.*
