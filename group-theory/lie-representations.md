**English** · [中文](lie-representations.zh.md)

# Lie Algebra Representation Theory, *classifying symmetry.*

*A second course that takes the Lie algebras introduced in the group-theory guide and pushes all the way to the classification of the simple Lie algebras and their irreducible representations — root systems, Dynkin diagrams, highest weights, the Weyl character formula — with every definition spelled out, every theorem proved or carefully justified, and the physics of particle multiplets kept always in view. The single payoff to keep in mind: classifying representations classifies the multiplets of states nature can build.*

[← Back to all guides](../README.md)

> **How to read this guide.** The one prerequisite is the **Group Theory & Representations** guide ([`group-theory.md`](group-theory.md)), which built groups, *representations* (homomorphisms $\rho:G\to GL(V)$ realizing group elements as matrices), *Lie groups* (groups that are also smooth manifolds, like the rotations), *Lie algebras* (their tangent spaces of infinitesimal generators), and the ladder analysis of $\mathfrak{su}(2)$ (spin). Whenever we lean on one of those facts we restate it in a single line so this guide stands alone. We assume ordinary algebra and a little single-variable calculus; everything specific — *ideal*, *Killing form*, *Cartan subalgebra*, *root*, *weight*, *Dynkin diagram*, *Verma module*, *Weyl group*, *Casimir* — is defined the first time it appears and illustrated with real numbers. Nothing is left to the reader; where we use a hard input from outside (Lie's third theorem, Weyl's unitarian trick) we say so explicitly and explain its content. Where the physics illuminates, we say so, but this is a **math** guide: claims are proved.

---

## Part A — Structure of Lie algebras

<a id="s0"></a>
### Motivation: why classifying representations classifies the possible particle multiplets

**What and why.** In quantum mechanics a physical state is a vector $|\psi\rangle$ in a complex vector space, and a continuous symmetry of the system — a rotation, an isospin transformation, the $SU(3)$ flavor symmetry — acts on states by a linear operator. The collection of these operators forms a **representation** of a Lie group $G$: a smooth homomorphism $\rho:G\to GL(V)$ assigning to each symmetry $g$ an invertible matrix $\rho(g)$ on the state space $V$, with $\rho(gh)=\rho(g)\rho(h)$. States that the symmetry shuffles among themselves — and that cannot be split into smaller such families — form a **multiplet**, mathematically an **irreducible representation** (a representation with no proper nonzero subspace mapped into itself by every $\rho(g)$).

Two facts, established in the prerequisite, set up everything here.

First, a symmetry that leaves the Hamiltonian invariant forces states in one multiplet to be **degenerate** (equal energy): if $\rho(g)$ commutes with the energy operator $H$ for all $g$, then $H$ acts as a single scalar on each irreducible block (by Schur's lemma — a homomorphism commuting with an irreducible representation is a scalar multiple of the identity). So the observed pattern of degeneracies *is* the decomposition of the state space into irreducibles. The proton–neutron near-degeneracy is an isospin doublet; the eight light baryons are an $SU(3)$ octet.

Second, near the identity a Lie group is governed by its **Lie algebra** $\mathfrak{g}$, the vector space of infinitesimal generators with a bracket $[\,\cdot\,,\cdot\,]$, and a representation of the group differentiates to a representation of the algebra (and, for the simply connected group, conversely). So the seemingly analytic problem "which matrices can realize this symmetry?" becomes the purely algebraic problem "which representations does this Lie algebra have?" That algebraic problem has a *complete and finite answer*: the irreducible representations of a semisimple Lie algebra are catalogued by their **highest weights**, points in a lattice, and the algebras themselves fall into a short list (the $A_n,B_n,C_n,D_n$ families and five exceptionals).

So the slogan of this guide is precise, not poetic: **to classify the representations of $\mathfrak{g}$ is to classify the multiplets of states that a $\mathfrak{g}$-symmetric theory can contain.** When Gell-Mann arranged the hadrons into octets and decuplets, he was reading off the irreducible representations of $\mathfrak{su}(3)$; the empty corner of the baryon decuplet was a representation slot with no particle yet found, and the $\Omega^-$ filled it. We build the machinery that makes such predictions inevitable.

> **The plan.** Part A nails down the structure theory: which Lie algebras are "semisimple" (the good ones), and the Killing form that detects them. Part B is the geometric heart: Cartan subalgebra, roots, Dynkin diagrams, and the classification theorem. Part C is representations proper: weights, highest-weight theory, Verma modules, the Weyl character formula. Part D works $\mathfrak{su}(2)$ and $\mathfrak{su}(3)$ in full, handles tensor products and branching, and ends with the Casimir operators that label states in the laboratory.

<a id="s1"></a>
### Lie algebras revisited: structure constants, ideals, the adjoint representation

**What and why.** We restate the definition of a Lie algebra from the prerequisite and immediately develop the three tools used everywhere below: a basis expansion (*structure constants*), the substructures that can be "divided out" (*ideals*), and the single most important representation an algebra has of itself (the *adjoint*).

> **Definition — Lie algebra.** A **Lie algebra** over a field $\mathbb{F}$ (we take $\mathbb{F}=\mathbb{R}$ or $\mathbb{C}$) is a vector space $\mathfrak{g}$ equipped with a bilinear map $[\,\cdot\,,\cdot\,]:\mathfrak{g}\times\mathfrak{g}\to\mathfrak{g}$, the **bracket**, satisfying for all $X,Y,Z\in\mathfrak{g}$:
> 1. **(Antisymmetry)** $[X,Y]=-[Y,X]$ (so $[X,X]=0$);
> 2. **(Jacobi identity)** $[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0$.
>
> A **subalgebra** is a subspace closed under the bracket. The **dimension** of $\mathfrak{g}$ is its dimension as a vector space.

The motivating model: for matrices, $[X,Y]=XY-YX$ (the **commutator**). This is bilinear and antisymmetric by inspection, and the Jacobi identity is a direct expansion (every product $XYZ$ appears once with $+$ and once with $-$ and they cancel in threes — we verify this in the worked example). The infinitesimal generators of a matrix Lie group form such an algebra; e.g. $\mathfrak{su}(2)$ is the traceless anti-Hermitian $2\times2$ matrices under the commutator.

> **Definition — structure constants.** Fix a basis $\{T_a\}_{a=1}^{n}$ of $\mathfrak{g}$ ($n=\dim\mathfrak{g}$). Since each bracket $[T_a,T_b]$ is again in $\mathfrak{g}$, it expands uniquely in the basis:
> $$
> [T_a,T_b]=\sum_{c=1}^{n} f_{ab}{}^{c}\,T_c .
> $$
> The numbers $f_{ab}{}^{c}\in\mathbb{F}$ are the **structure constants**. They encode the entire bracket: antisymmetry forces $f_{ab}{}^{c}=-f_{ba}{}^{c}$, and the Jacobi identity becomes the quadratic relation $\sum_e\big(f_{ab}{}^{e}f_{ec}{}^{d}+f_{bc}{}^{e}f_{ea}{}^{d}+f_{ca}{}^{e}f_{eb}{}^{d}\big)=0$ for all $a,b,c,d$.

> **Definition — ideal.** A subspace $\mathfrak{a}\subseteq\mathfrak{g}$ is an **ideal** if $[\mathfrak{g},\mathfrak{a}]\subseteq\mathfrak{a}$, i.e. $[X,A]\in\mathfrak{a}$ for every $X\in\mathfrak{g}$ and $A\in\mathfrak{a}$. (Compare a *normal subgroup* in the prerequisite: an ideal is exactly the substructure you can "quotient by," because the bracket descends to the quotient space $\mathfrak{g}/\mathfrak{a}$.)

Ideals are the Lie-algebra analogue of normal subgroups. The whole algebra $\mathfrak{g}$ and the zero subspace $\{0\}$ are always ideals (the **trivial** ideals). An algebra with no others (and $\dim\mathfrak{g}>1$, with nonzero bracket) is called **simple** — these are the indivisible atoms we classify.

> **Definition — the adjoint representation.** For $X\in\mathfrak{g}$ define the linear map $\mathrm{ad}_X:\mathfrak{g}\to\mathfrak{g}$ by $\mathrm{ad}_X(Y)=[X,Y]$. The assignment $X\mapsto\mathrm{ad}_X$ is the **adjoint representation**, $\mathrm{ad}:\mathfrak{g}\to\mathfrak{gl}(\mathfrak{g})$, where $\mathfrak{gl}(\mathfrak{g})$ is the algebra of all linear maps on $\mathfrak{g}$ under the commutator.

> **Lemma — the adjoint is a Lie-algebra homomorphism.** For all $X,Y\in\mathfrak{g}$, $\mathrm{ad}_{[X,Y]}=[\mathrm{ad}_X,\mathrm{ad}_Y]$, where the right bracket is the commutator of operators.

**Proof.**
1. Apply both sides to an arbitrary $Z\in\mathfrak{g}$; it suffices to show they agree on every $Z$ (a linear map is determined by its values, by *linearity*).
2. Left side: $\mathrm{ad}_{[X,Y]}(Z)=[[X,Y],Z]$, by the *definition of $\mathrm{ad}$*.
3. Right side: $[\mathrm{ad}_X,\mathrm{ad}_Y](Z)=\mathrm{ad}_X\mathrm{ad}_Y(Z)-\mathrm{ad}_Y\mathrm{ad}_X(Z)=[X,[Y,Z]]-[Y,[X,Z]]$, by the *definition of operator commutator* and of $\mathrm{ad}$.
4. The Jacobi identity, written as $[[X,Y],Z]=[X,[Y,Z]]-[Y,[X,Z]]$ (rearrange the three cyclic terms using *antisymmetry* on the last), shows steps 2 and 3 are equal. $\blacksquare$

This lemma says the adjoint really is a representation: it sends brackets to commutators, exactly the defining property of a Lie-algebra homomorphism. The adjoint is where *roots* will live (s3).

**Worked example — $\mathfrak{su}(2)$ structure constants and the adjoint.** Take the standard generators $J_1,J_2,J_3$ with $[J_a,J_b]=\sum_c \varepsilon_{abc}J_c$, where $\varepsilon_{abc}$ is the totally antisymmetric symbol ($\varepsilon_{123}=+1$). So the structure constants are $f_{ab}{}^{c}=\varepsilon_{abc}$. Compute $\mathrm{ad}_{J_3}$ in the basis $(J_1,J_2,J_3)$:
$$
\mathrm{ad}_{J_3}(J_1)=[J_3,J_1]=J_2,\quad \mathrm{ad}_{J_3}(J_2)=[J_3,J_2]=-J_1,\quad \mathrm{ad}_{J_3}(J_3)=0 .
$$
As a matrix (columns = images of $J_1,J_2,J_3$):
$$
\mathrm{ad}_{J_3}=\begin{pmatrix}0&-1&0\\ 1&0&0\\ 0&0&0\end{pmatrix}.
$$
This is the generator of rotations about the $3$-axis acting on a $3$-vector — the adjoint of $\mathfrak{su}(2)$ is the vector (spin-$1$) representation, recovering a fact from the prerequisite from pure algebra. Let us also *verify Jacobi numerically* on $(J_1,J_2,J_3)$: $[J_1,[J_2,J_3]]+[J_2,[J_3,J_1]]+[J_3,[J_1,J_2]] = [J_1,J_1]+[J_2,J_2]+[J_3,J_3]=0+0+0=0$. Good.

> **Pitfall.** Structure constants depend on the chosen basis; statements about the algebra (like "$\mathfrak{g}$ is simple") must not secretly depend on the basis. The cure is to build *basis-independent* objects — the first of which, the Killing form, is next.

<a id="s2"></a>
### Solvable, nilpotent, and semisimple Lie algebras; the Killing form; Cartan's criterion

**What and why.** Just as integers split into primes, Lie algebras split into building blocks. At one extreme are the "fully non-simple" algebras built only from repeated brackets that eventually vanish — the **solvable** and **nilpotent** ones, the analogue of abelian/triangular. At the other extreme are the **semisimple** algebras, sums of simple pieces, which have a beautiful representation theory. We need a computable test to tell which is which: the **Killing form** and **Cartan's criterion**.

> **Definition — derived and lower central series.** Set $\mathfrak{g}^{(0)}=\mathfrak{g}$ and $\mathfrak{g}^{(k+1)}=[\mathfrak{g}^{(k)},\mathfrak{g}^{(k)}]$ (the span of all brackets of pairs from $\mathfrak{g}^{(k)}$); this is the **derived series**. Set $\mathfrak{g}^{[0]}=\mathfrak{g}$ and $\mathfrak{g}^{[k+1]}=[\mathfrak{g},\mathfrak{g}^{[k]}]$; this is the **lower central series**. Each term is an ideal (a bracket with anything in $\mathfrak{g}$ stays inside).

> **Definitions — solvable, nilpotent.** $\mathfrak{g}$ is **solvable** if $\mathfrak{g}^{(k)}=\{0\}$ for some $k$ (repeatedly bracketing the derived parts eventually kills everything). $\mathfrak{g}$ is **nilpotent** if $\mathfrak{g}^{[k]}=\{0\}$ for some $k$. Nilpotent $\Rightarrow$ solvable, since $\mathfrak{g}^{(k)}\subseteq\mathfrak{g}^{[k]}$ for all $k$ (an easy induction: $\mathfrak{g}^{(k+1)}=[\mathfrak{g}^{(k)},\mathfrak{g}^{(k)}]\subseteq[\mathfrak{g},\mathfrak{g}^{[k]}]=\mathfrak{g}^{[k+1]}$).

**Examples.** Every **abelian** algebra (all brackets zero) is nilpotent: $\mathfrak{g}^{(1)}=\{0\}$ already. The algebra of strictly upper-triangular $n\times n$ matrices (zeros on and below the diagonal) is nilpotent — each commutator pushes the nonzero band one step further from the diagonal until it falls off. The algebra of *all* upper-triangular matrices is solvable but not nilpotent.

> **Definition — radical and semisimple.** Every finite-dimensional Lie algebra has a unique maximal solvable ideal, the **radical** $\mathrm{rad}\mathfrak{g}$ (the sum of all solvable ideals is solvable, so a largest one exists). $\mathfrak{g}$ is **semisimple** if $\mathrm{rad}\mathfrak{g}=\{0\}$ — no nonzero solvable ideals at all. Equivalently (a theorem we use, due to Cartan), a semisimple algebra is a direct sum of simple algebras.

Semisimple is the sweet spot: "as far from solvable as possible." We now build the detector.

> **Definition — Killing form.** The **Killing form** is the symmetric bilinear form $\kappa:\mathfrak{g}\times\mathfrak{g}\to\mathbb{F}$,
> $$
> \kappa(X,Y)=\mathrm{tr}\big(\mathrm{ad}_X\,\mathrm{ad}_Y\big),
> $$
> the trace of the composition of the two adjoint operators. It is symmetric because $\mathrm{tr}(AB)=\mathrm{tr}(BA)$, and it is **invariant**: $\kappa([X,Y],Z)=\kappa(X,[Y,Z])$.

**Proof of invariance.**
1. By the lemma in s1, $\mathrm{ad}_{[X,Y]}=\mathrm{ad}_X\mathrm{ad}_Y-\mathrm{ad}_Y\mathrm{ad}_X$. Write $A=\mathrm{ad}_X,B=\mathrm{ad}_Y,C=\mathrm{ad}_Z$.
2. Then $\kappa([X,Y],Z)=\mathrm{tr}((AB-BA)C)=\mathrm{tr}(ABC)-\mathrm{tr}(BAC)$, by *linearity of trace* and step 1.
3. Likewise $\kappa(X,[Y,Z])=\mathrm{tr}(A(BC-CB))=\mathrm{tr}(ABC)-\mathrm{tr}(ACB)$.
4. By *cyclicity of trace*, $\mathrm{tr}(BAC)=\mathrm{tr}(ACB)$. Hence steps 2 and 3 are equal. $\blacksquare$

The Killing form is basis-independent (it is a trace) — the invariant object we wanted in s1. Its key feature is **non-degeneracy**: $\kappa$ is non-degenerate if the only $X$ with $\kappa(X,Y)=0$ for all $Y$ is $X=0$.

> **Theorem — Cartan's criterion for semisimplicity.** A finite-dimensional Lie algebra $\mathfrak{g}$ is semisimple **if and only if** its Killing form $\kappa$ is non-degenerate.

We use this as a working tool; its proof rests on Cartan's criterion for *solvability* (a solvable algebra is exactly one whose Killing form vanishes on $[\mathfrak{g},\mathfrak{g}]$, proved via the structure of nilpotent operators), and the fact that the radical is precisely the **kernel** (degeneracy subspace) of $\kappa$. We give the direction that powers our examples.

**Proof that a nonzero abelian ideal forces degeneracy (so non-degenerate $\Rightarrow$ semisimple).**
1. Suppose $\mathfrak{a}\ne\{0\}$ is an abelian ideal ($[\mathfrak{a},\mathfrak{a}]=0$). Take $A\in\mathfrak{a}$, $X\in\mathfrak{g}$; we show $\kappa(A,X)=0$, so every $A\in\mathfrak{a}$ lies in the degeneracy subspace, making $\kappa$ degenerate.
2. Consider the operator $T=\mathrm{ad}_A\mathrm{ad}_X$. The map $\mathrm{ad}_X$ sends $\mathfrak{g}$ into $\mathfrak{g}$, and because $\mathfrak{a}$ is an ideal $\mathrm{ad}_A$ maps $\mathfrak{g}$ *into* $\mathfrak{a}$ (since $[A,\,\cdot\,]\in\mathfrak{a}$, as $\mathfrak{a}$ is an ideal). So $\mathrm{ad}_A\mathfrak{g}\subseteq\mathfrak{a}$.
3. Then $T(\mathfrak{g})=\mathrm{ad}_A(\mathrm{ad}_X\mathfrak{g})\subseteq\mathrm{ad}_A\mathfrak{g}\subseteq\mathfrak{a}$, and $T(\mathfrak{a})=\mathrm{ad}_A\mathrm{ad}_X\mathfrak{a}\subseteq\mathrm{ad}_A\mathfrak{g}\subseteq\mathfrak{a}$; moreover $T^2(\mathfrak{g})\subseteq\mathrm{ad}_A\mathrm{ad}_X\mathfrak{a}\subseteq\mathrm{ad}_A\mathfrak{a}=[A,\mathfrak{a}]\subseteq[\mathfrak{a},\mathfrak{a}]=0$, using that $\mathfrak{a}$ is *abelian*. So $T$ is **nilpotent** ($T^2=0$).
4. A nilpotent operator has all eigenvalues $0$, hence trace $0$: $\kappa(A,X)=\mathrm{tr}T=0$. Since $X$ was arbitrary, $A$ is in the degeneracy subspace. $\blacksquare$

**Worked example — $\kappa$ for $\mathfrak{su}(2)$.** Using $f_{ab}{}^c=\varepsilon_{abc}$, the matrix entries of $\mathrm{ad}_{T_a}$ are $(\mathrm{ad}_{T_a})_{cb}=\varepsilon_{acb}$. Then
$$
\kappa(T_a,T_b)=\mathrm{tr}(\mathrm{ad}_{T_a}\mathrm{ad}_{T_b})=\sum_{c,d}\varepsilon_{acd}\varepsilon_{bdc}=-\sum_{c,d}\varepsilon_{acd}\varepsilon_{bcd}=-2\,\delta_{ab},
$$
using the identity $\sum_{c,d}\varepsilon_{acd}\varepsilon_{bcd}=2\delta_{ab}$. So $\kappa=-2\,I$, which is non-degenerate ($\det=-8\ne0$): by Cartan's criterion $\mathfrak{su}(2)$ is semisimple, indeed simple. The form is negative-definite — a signature of a **compact** algebra, which is why $\mathfrak{su}(2)$ integrates to the compact group $SU(2)$.

> **Pitfall.** "Semisimple" is *not* "has no abelian subalgebra" — every algebra has plenty. It means no abelian (more generally solvable) *ideal*. The Cartan subalgebra (s3) is abelian but is not an ideal, so it does not violate semisimplicity.

## Part B — Roots and the classification

<a id="s3"></a>
### The Cartan subalgebra and the root space decomposition (running example $\mathfrak{su}(3)$)

**What and why.** To analyze $\mathfrak{su}(2)$ in the prerequisite we picked the single commuting generator $J_3$, diagonalized it, and watched the raising/lowering operators $J_\pm$ shift its eigenvalue by $\pm1$. The general theory copies this: pick a *maximal* set of mutually commuting generators (the **Cartan subalgebra**), simultaneously diagonalize their adjoint action on $\mathfrak{g}$, and the nonzero shift-vectors that appear are the **roots**. This decomposes the whole algebra into a commuting core plus root spaces — the master diagram of the subject.

We work over $\mathbb{C}$ from now on (complexify the algebra; e.g. $\mathfrak{su}(2)$ complexifies to $\mathfrak{sl}(2,\mathbb{C})$, spanned by $H,E,F$ below). Over $\mathbb{C}$ operators can be diagonalized, which the analysis needs.

> **Definition — Cartan subalgebra (CSA).** A **Cartan subalgebra** $\mathfrak{h}\subseteq\mathfrak{g}$ is a maximal abelian subalgebra all of whose elements act diagonalizably under $\mathrm{ad}$ (such elements are called **semisimple**). Its dimension is the **rank** $r$ of $\mathfrak{g}$. For semisimple $\mathfrak{g}$ all Cartan subalgebras have the same dimension, so rank is well-defined.

Because the elements of $\mathfrak{h}$ commute, their adjoint operators $\{\mathrm{ad}_H:H\in\mathfrak{h}\}$ commute, and commuting diagonalizable operators are **simultaneously diagonalizable** (a standard linear-algebra fact: a common eigenbasis exists). So $\mathfrak{g}$ breaks into joint eigenspaces.

> **Definition — root space decomposition.** For a linear functional $\alpha\in\mathfrak{h}^{*}$ (a linear map $\mathfrak{h}\to\mathbb{C}$) define the **root space**
> $$
> \mathfrak{g}_\alpha=\{\,X\in\mathfrak{g} : [H,X]=\alpha(H)\,X \text{ for all } H\in\mathfrak{h}\,\}.
> $$
> The nonzero $\alpha$ with $\mathfrak{g}_\alpha\ne\{0\}$ are the **roots**; the set of roots is $\Phi$. The zero-functional space is $\mathfrak{g}_0=\mathfrak{h}$ itself (the CSA is its own centralizer, for semisimple $\mathfrak{g}$). The whole algebra is the direct sum
> $$
> \mathfrak{g}=\mathfrak{h}\ \oplus\ \bigoplus_{\alpha\in\Phi}\mathfrak{g}_\alpha .
> $$

A root $\alpha$ is the vector of "shifts" that the generator $X\in\mathfrak{g}_\alpha$ produces in the eigenvalues of the CSA — exactly the multi-dimensional version of "$J_\pm$ shifts $J_3$ by $\pm1$."

> **Proposition — basic properties of roots.** For a semisimple $\mathfrak{g}$:
> 1. $[\mathfrak{g}_\alpha,\mathfrak{g}_\beta]\subseteq\mathfrak{g}_{\alpha+\beta}$ (brackets add roots).
> 2. Each root space is **one-dimensional**: $\dim\mathfrak{g}_\alpha=1$.
> 3. If $\alpha\in\Phi$ then $-\alpha\in\Phi$, and the only multiples of $\alpha$ that are roots are $\pm\alpha$.
> 4. For $\alpha\in\Phi$, the triple $\{E_\alpha\in\mathfrak{g}_\alpha,\ E_{-\alpha}\in\mathfrak{g}_{-\alpha},\ H_\alpha=[E_\alpha,E_{-\alpha}]\}$ spans a subalgebra isomorphic to $\mathfrak{sl}(2,\mathbb{C})$.

**Proof of (1).** Let $X\in\mathfrak{g}_\alpha,Y\in\mathfrak{g}_\beta,H\in\mathfrak{h}$. Then
$$
[H,[X,Y]]=[[H,X],Y]+[X,[H,Y]]
$$
by the *Jacobi identity* (in the form $\mathrm{ad}_H$ is a derivation). The first term is $[\alpha(H)X,Y]=\alpha(H)[X,Y]$ and the second is $\beta(H)[X,Y]$, by the *definition of root space* and *bilinearity*. Summing, $[H,[X,Y]]=(\alpha+\beta)(H)\,[X,Y]$, so $[X,Y]\in\mathfrak{g}_{\alpha+\beta}$. $\blacksquare$

Property (4) is the engine of the whole theory: **every root gives a copy of the $\mathfrak{su}(2)$ ladder**. Because we already know $\mathfrak{su}(2)$ representations completely (eigenvalues of $H$ are integers, symmetric about $0$), we can transfer that knowledge to constrain how roots and weights sit relative to one another (s4, s6).

> **The $\mathfrak{sl}(2)$ inside each root.** Normalize so that $H_\alpha,E_\alpha,E_{-\alpha}$ satisfy $[H_\alpha,E_\alpha]=2E_\alpha$, $[H_\alpha,E_{-\alpha}]=-2E_{-\alpha}$, $[E_\alpha,E_{-\alpha}]=H_\alpha$. This is *exactly* the $\mathfrak{sl}(2,\mathbb{C})$ relations with $H\leftrightarrow H_\alpha$. The element $H_\alpha\in\mathfrak{h}$ is the **coroot** of $\alpha$.

**Worked example — $\mathfrak{su}(3)$ root system.** Complexify to $\mathfrak{sl}(3,\mathbb{C})$, the traceless $3\times3$ complex matrices, dimension $8$. The CSA $\mathfrak{h}$ is the diagonal traceless matrices, rank $2$. Let $E_{ij}$ ($i\ne j$) be the matrix with a single $1$ in row $i$, column $j$. For diagonal $H=\mathrm{diag}(h_1,h_2,h_3)$ (with $h_1+h_2+h_3=0$),
$$
[H,E_{ij}]=(h_i-h_j)\,E_{ij},
$$
since $HE_{ij}$ has the $i$th diagonal entry scaling and $E_{ij}H$ the $j$th. So $E_{ij}$ is a root vector with root $\alpha=L_i-L_j$, where $L_i(H)=h_i$ reads off the $i$th diagonal entry. The six roots are $\pm(L_1-L_2),\ \pm(L_2-L_3),\ \pm(L_1-L_3)$. Plotting them in the plane $h_1+h_2+h_3=0$ (with the inner product from the Killing form) gives **six vectors of equal length at $60^\circ$ spacings — a regular hexagon.** This hexagon is the $A_2$ root system, and it is the geometric DNA of the Eightfold Way.

> **Pitfall.** The CSA is not unique as a *set* (any conjugate works), but its dimension — the rank — and the resulting root system are intrinsic. Choosing a CSA is like choosing axes; the physics (multiplet shapes) is axis-independent.

<a id="s4"></a>
### Root systems: simple roots, the Cartan matrix, and Dynkin diagrams

**What and why.** The set $\Phi$ of roots is not an arbitrary collection of vectors; the $\mathfrak{sl}(2)$-from-each-root structure (s3) forces sharp geometric constraints. Abstracting these constraints gives the notion of a **root system**, a finite set of vectors closed under certain reflections. Remarkably, a root system is determined by a tiny amount of data — a handful of **simple roots**, packaged in a **Cartan matrix** and drawn as a **Dynkin diagram** — and that data is what the classification (s5) enumerates.

> **Definition — root system.** A finite set $\Phi$ of nonzero vectors in a Euclidean space $E$ (with inner product $(\cdot,\cdot)$) is a **root system** if:
> 1. $\Phi$ spans $E$ and, for each $\alpha\in\Phi$, the only multiples of $\alpha$ in $\Phi$ are $\pm\alpha$;
> 2. for each $\alpha$, the **reflection** $s_\alpha(v)=v-\dfrac{2(v,\alpha)}{(\alpha,\alpha)}\alpha$ (reflection across the hyperplane perpendicular to $\alpha$) maps $\Phi$ to itself;
> 3. (**integrality**) for all $\alpha,\beta\in\Phi$, the integer $\langle\beta,\alpha\rangle:=\dfrac{2(\beta,\alpha)}{(\alpha,\alpha)}\in\mathbb{Z}$.

The integrality in (3) is not an assumption we impose by taste — it is *forced* by the $\mathfrak{sl}(2)$ of each root acting on the root spaces, since (s3, property 4 plus s6) eigenvalues of any $H_\alpha$ are integers. This single fact is astonishingly restrictive.

> **Theorem — the angle between two roots is quantized.** For distinct roots $\alpha,\beta$ with angle $\theta$, the product $\langle\beta,\alpha\rangle\langle\alpha,\beta\rangle = \dfrac{4(\alpha,\beta)^2}{(\alpha,\alpha)(\beta,\beta)}=4\cos^2\theta$ is a non-negative integer $\le 4$, hence $\in\{0,1,2,3,4\}$. Excluding the parallel case ($\theta=0,\pi$, giving $4$), the only possibilities are $4\cos^2\theta\in\{0,1,2,3\}$, i.e. $\theta\in\{90^\circ,120^\circ,135^\circ,150^\circ\}$ (and supplements $60^\circ,45^\circ,30^\circ$).

**Proof.**
1. Both $\langle\beta,\alpha\rangle$ and $\langle\alpha,\beta\rangle$ are integers, by integrality (axiom 3).
2. Their product is $\dfrac{2(\beta,\alpha)}{(\alpha,\alpha)}\cdot\dfrac{2(\alpha,\beta)}{(\beta,\beta)}=\dfrac{4(\alpha,\beta)^2}{(\alpha,\alpha)(\beta,\beta)}$, by *substitution*.
3. By the *Cauchy–Schwarz definition* $\cos\theta=\dfrac{(\alpha,\beta)}{\|\alpha\|\,\|\beta\|}$, this product equals $4\cos^2\theta$, a real number in $[0,4]$.
4. Being a product of integers in $[0,4]$, it lies in $\{0,1,2,3,4\}$. Solving $4\cos^2\theta=k$ gives the listed angles. $\blacksquare$

That a continuous quantity (an angle) is pinned to four discrete values is exactly why there are only finitely many root systems. We now reduce the data further.

> **Definition — positive and simple roots.** Choose a linear functional on $E$ that is nonzero on every root (a "generic direction"). A root is **positive** ($\alpha>0$) if it has positive value, **negative** otherwise; $\Phi=\Phi^{+}\sqcup\Phi^{-}$ with $\Phi^{-}=-\Phi^{+}$. A positive root is **simple** if it is *not* the sum of two positive roots. The set $\Delta=\{\alpha_1,\dots,\alpha_r\}$ of simple roots is a **basis** of $E$ ($r=\mathrm{rank}$), and every positive root is a *non-negative integer combination* of simple roots.

> **Definition — Cartan matrix.** With simple roots $\alpha_1,\dots,\alpha_r$, the **Cartan matrix** is the $r\times r$ integer matrix
> $$
> A_{ij}=\langle\alpha_i,\alpha_j\rangle=\frac{2(\alpha_i,\alpha_j)}{(\alpha_j,\alpha_j)} .
> $$
> Its diagonal is $A_{ii}=2$; off-diagonal entries are in $\{0,-1,-2,-3\}$ (from the angle quantization, since distinct simple roots make obtuse angles, so $(\alpha_i,\alpha_j)\le0$).

> **Definition — Dynkin diagram.** Draw one node per simple root. Join nodes $i\ne j$ by $A_{ij}A_{ji}\in\{0,1,2,3\}$ edges. When the two roots have different lengths (a double or triple bond), put an arrow pointing from the longer root to the shorter. This picture encodes the whole Cartan matrix, hence (it can be shown via reconstruction of $\Phi$ from $\Delta$) the whole algebra.

**Worked example — $A_2=\mathfrak{su}(3)$.** From s3 the positive roots can be taken as $\alpha_1=L_1-L_2$, $\alpha_2=L_2-L_3$, with the third positive root $\alpha_1+\alpha_2=L_1-L_3$ (so it is *not* simple — it is a sum of positive roots). All roots have equal length; the angle between $\alpha_1$ and $\alpha_2$ is $120^\circ$. Then
$$
A=\begin{pmatrix}2 & -1\\ -1 & 2\end{pmatrix},
$$
since $A_{12}=2\cos120^\circ\cdot\frac{\|\alpha_1\|}{\|\alpha_2\|}=2(-\tfrac12)(1)=-1$. The Dynkin diagram is two nodes joined by a single edge: $\circ\!-\!\circ$. This is the simplest non-trivial diagram, and it *is* $\mathfrak{su}(3)$.

> **Pitfall.** The Cartan integers $\langle\alpha_i,\alpha_j\rangle$ are generally **not symmetric** ($A_{ij}\ne A_{ji}$ when roots differ in length); only their product is what the diagram records. Forgetting the arrow loses the distinction between $B_n$ and $C_n$.

<a id="s5"></a>
### The classification of the simple Lie algebras ($A_n,B_n,C_n,D_n$ and the exceptionals)

**What and why.** Here is the summit. The angle/length constraints on root systems are so tight that the connected Dynkin diagrams can be listed completely — and each one corresponds to exactly one simple Lie algebra over $\mathbb{C}$. This is the **Cartan–Killing classification**, one of the great theorems of mathematics. We state it and explain the logic that makes the list finite.

> **Theorem — classification of simple Lie algebras.** Over $\mathbb{C}$, every finite-dimensional simple Lie algebra corresponds to exactly one connected Dynkin diagram, and the complete list is:
> - four infinite **classical** families:
>   - $A_n\ (n\ge1)$: $\mathfrak{sl}(n+1,\mathbb{C})$, the traceless matrices — compact real form $\mathfrak{su}(n+1)$;
>   - $B_n\ (n\ge2)$: $\mathfrak{so}(2n+1,\mathbb{C})$, odd orthogonal;
>   - $C_n\ (n\ge3)$: $\mathfrak{sp}(2n,\mathbb{C})$, symplectic;
>   - $D_n\ (n\ge4)$: $\mathfrak{so}(2n,\mathbb{C})$, even orthogonal;
> - five **exceptional** algebras: $G_2,F_4,E_6,E_7,E_8$ (dimensions $14,52,78,133,248$).

The diagrams: $A_n$ is a chain of $n$ nodes with single bonds; $B_n$ and $C_n$ are chains ending in a double bond (arrow distinguishing them); $D_n$ is a chain that forks into two nodes at one end; $G_2$ is two nodes with a triple bond; $F_4$ is four nodes with a central double bond; the $E$ series are forked diagrams with a short branch.

**The logic that bounds the list (sketch with the key steps).**
1. A connected Dynkin diagram comes from a set of unit-or-scaled vectors with pairwise angles in $\{90^\circ,120^\circ,135^\circ,150^\circ\}$ and obtuse pairings (s4). Call such a configuration **admissible**.
2. **No loops.** If the diagram contained a cycle, summing the simple roots in the cycle and squaring the length yields, using each bond contributes $2(\alpha_i,\alpha_j)\le-(\alpha_i,\alpha_i)$, a non-positive norm for a nonzero vector — contradicting positive-definiteness of the inner product. So diagrams are **trees**.
3. **Bounded branching.** A node can have at most three bonds total (counting multiplicities): if a node $\beta$ is joined to neighbors $\gamma_1,\dots,\gamma_k$ (mutually orthogonal, since non-adjacent simple roots are orthogonal), then $\sum_i \cos^2(\beta,\gamma_i)<1$ because $\beta$ has a component out of their span; each bond contributes $\ge\tfrac14$ to that sum, forcing $\le 3$ bonds. This kills all but the listed shapes: at most one double/triple bond, at most one branch node of degree three.
4. **Eigenvalue test.** Finitely many candidate trees remain; a determinant/eigenvalue computation on the associated symmetric matrix (it must be positive-definite) discards the rest, leaving exactly $A_n,B_n,C_n,D_n,G_2,F_4,E_6,E_7,E_8$.
5. **Existence.** Conversely each surviving diagram is *realized*: the classical ones by explicit matrix algebras, the exceptionals by direct (if intricate) construction. So the correspondence diagram $\leftrightarrow$ algebra is a bijection. $\blacksquare$ (for the bound; existence cited)

**Worked example — reading dimensions off $A_n$.** For $A_n=\mathfrak{su}(n+1)$: rank $n$, and the roots are $L_i-L_j$ for $i\ne j$ among $n+1$ indices, giving $n(n+1)$ roots, plus the rank-$n$ CSA: total $\dim=n(n+1)+n=n(n+2)$. Check $n=1$: $\dim=3$ ($\mathfrak{su}(2)$, correct); $n=2$: $\dim=8$ ($\mathfrak{su}(3)$, correct, matching the eight Gell-Mann matrices).

> **Why physics meets the exceptionals.** Grand-unified theories have proposed $SU(5)$ ($A_4$), $SO(10)$ ($D_5$), and $E_6$ as gauge groups precisely because their representations can package one generation of quarks and leptons into a single multiplet. The classification is therefore a finite menu of candidate symmetries of nature.

> **Pitfall — low-rank coincidences.** The ranges ($B_n$ from $n\ge2$, etc.) avoid double-counting accidental isomorphisms: $A_1=B_1=C_1$ ($\mathfrak{su}(2)\cong\mathfrak{so}(3)\cong\mathfrak{sp}(2)$), $B_2\cong C_2$, $D_2\cong A_1\times A_1$, $D_3\cong A_3$. These are real isomorphisms, not errors, and matter when you identify a physical symmetry.

## Part C — Representation theory

<a id="s6"></a>
### Weights, the weight lattice, and the highest-weight theorem

**What and why.** With the algebra's skeleton (roots) in hand, we turn to its representations. The eigenvalues of the CSA on a representation are the **weights** — the generalization of the eigenvalue $m$ of $J_3$. Just as a spin-$j$ representation is pinned down by its top eigenvalue $m=j$, every irreducible representation of a semisimple algebra is pinned down by a single **highest weight**. This is the central classification theorem of the whole subject.

> **Definition — weights of a representation.** Let $\rho:\mathfrak{g}\to\mathfrak{gl}(V)$ be a representation. Since $\mathfrak{h}$ is abelian and (in a finite-dimensional representation of a semisimple algebra) acts diagonalizably, $V$ splits into joint eigenspaces:
> $$
> V=\bigoplus_{\mu} V_\mu,\qquad V_\mu=\{v\in V:\rho(H)v=\mu(H)\,v\ \forall H\in\mathfrak{h}\}.
> $$
> Each $\mu\in\mathfrak{h}^{*}$ with $V_\mu\ne0$ is a **weight**; $\dim V_\mu$ is its **multiplicity**. (Roots are the weights of the *adjoint* representation, s3.)

> **How root vectors move weights.** If $v\in V_\mu$ and $E_\alpha\in\mathfrak{g}_\alpha$, then $\rho(E_\alpha)v\in V_{\mu+\alpha}$. Proof: for $H\in\mathfrak{h}$, $\rho(H)\rho(E_\alpha)v=\rho(E_\alpha)\rho(H)v+\rho([H,E_\alpha])v=\mu(H)\rho(E_\alpha)v+\alpha(H)\rho(E_\alpha)v=(\mu+\alpha)(H)\rho(E_\alpha)v$, using that $\rho$ is a *homomorphism* ($\rho([H,E_\alpha])=[\rho(H),\rho(E_\alpha)]$) and $[H,E_\alpha]=\alpha(H)E_\alpha$. So $\rho(E_\alpha)$ is a raising/lowering operator shifting the weight by the root $\alpha$.

> **Definition — integral weights and the weight lattice.** Applying the $\mathfrak{sl}(2)$-of-each-root (s3) to a weight forces $\langle\mu,\alpha\rangle=\dfrac{2(\mu,\alpha)}{(\alpha,\alpha)}\in\mathbb{Z}$ for every root $\alpha$ — because $\mu(H_\alpha)$ is an eigenvalue of the $H_\alpha$ in an $\mathfrak{sl}(2)$ representation, hence an integer. Such $\mu$ are **integral weights**; they form a lattice $P$, the **weight lattice**. The basis of $P$ **dual** to the simple coroots is the set of **fundamental weights** $\{\omega_1,\dots,\omega_r\}$ defined by $\langle\omega_i,\alpha_j\rangle=\delta_{ij}$.

> **Definition — dominant weight, highest weight.** Fix the positive roots (s4). A weight $\mu$ is **dominant** if $\langle\mu,\alpha_i\rangle\ge0$ for all simple roots $\alpha_i$ (equivalently $\mu=\sum_i m_i\omega_i$ with integers $m_i\ge0$, the **Dynkin labels**). In an irreducible representation there is a unique weight $\lambda$, the **highest weight**, such that $\lambda+\alpha$ is *not* a weight for any positive root $\alpha$ (no raising operator escapes it); its weight space is one-dimensional.

> **Theorem — theorem of the highest weight (Cartan–Weyl).** Let $\mathfrak{g}$ be a semisimple Lie algebra. The map
> $$
> \big\{\text{irreducible finite-dim representations}\big\}/\!\cong\ \ \xrightarrow{\ \sim\ }\ \big\{\text{dominant integral weights }\lambda\big\}
> $$
> sending each irreducible to its highest weight is a **bijection**. Every dominant integral weight is the highest weight of exactly one irreducible representation $V(\lambda)$, and isomorphic representations have equal highest weight.

**Proof of uniqueness/injectivity (the part we can do cleanly here).**
1. *(Highest weight exists.)* $V$ is finite-dimensional, so among its finitely many weights pick one, $\lambda$, maximal for the ordering "$\mu\preceq\mu'$ iff $\mu'-\mu$ is a sum of positive roots." Then $\lambda+\alpha$ is not a weight for any positive $\alpha$, since it would exceed $\lambda$. So a highest weight exists.
2. *(Its weight space is one-dimensional and generates.)* Let $0\ne v_\lambda\in V_\lambda$. Repeatedly apply lowering operators $\rho(E_{-\alpha})$; by the weight-shift rule each lands in a lower weight space, and the span $W$ of all such images is $\mathfrak{g}$-invariant (raising operators applied to a string of lowerings can be rewritten, via the commutation relations, as lower-order strings — the **PBW** reordering of s7). Since $V$ is irreducible and $W\ne0$, $W=V$. So $V$ is generated by the single vector $v_\lambda$.
3. *(Highest weight determines the representation.)* If $V,V'$ are irreducible with the same highest weight $\lambda$, form $V\oplus V'$ and the diagonal highest-weight vector $(v_\lambda,v'_\lambda)$; the subrepresentation it generates is irreducible and projects onto each factor non-trivially, so by Schur's lemma the projections are isomorphisms, giving $V\cong V'$. Hence the map is injective. $\blacksquare$ (Surjectivity — that *every* dominant $\lambda$ occurs — is the content of s7's Verma-module construction.)

**Worked example — fundamental weights of $\mathfrak{su}(3)$.** Rank $2$, simple roots $\alpha_1,\alpha_2$ at $120^\circ$, equal length $\sqrt2$ (so $(\alpha_i,\alpha_i)=2$). Solving $\langle\omega_i,\alpha_j\rangle=\delta_{ij}$ gives $\omega_1,\omega_2$ as the two "outer" directions of the hexagon. The defining representation $\mathbf 3$ has highest weight $\omega_1$ (Dynkin labels $(1,0)$); its conjugate $\overline{\mathbf3}$ has $\omega_2=(0,1)$; the adjoint octet $\mathbf 8$ has $\omega_1+\omega_2=(1,1)$. Every $SU(3)$ multiplet is labeled by a pair $(p,q)=(m_1,m_2)$ of non-negative integers, the Dynkin labels.

> **Pitfall.** "Highest" depends on the chosen positive system / generic direction. Different choices permute weights by the Weyl group (s8), so the *representation* is unchanged though the labelled "highest" vector moves. Always fix one positive system and stick with it.

<a id="s7"></a>
### Building an irreducible representation from its highest weight (Verma modules)

**What and why.** The highest-weight theorem says each dominant $\lambda$ labels one irreducible, but we want to *construct* it and compute its weights. The clean construction is the **Verma module**: build the "freest possible" highest-weight representation by formally applying all lowering operators, then quotient out the part that should vanish. This both proves existence (surjectivity in s6) and gives an algorithm for the weight diagram.

> **Definition — universal enveloping algebra and PBW.** The **universal enveloping algebra** $U(\mathfrak{g})$ is the associative algebra generated by $\mathfrak{g}$ subject only to $XY-YX=[X,Y]$. Representations of $\mathfrak{g}$ are the same as $U(\mathfrak{g})$-modules. The **Poincaré–Birkhoff–Witt (PBW) theorem** states that, fixing an ordered basis of $\mathfrak{g}$ split as (lowering $E_{-\alpha}$) $\,\cdot\,$ (Cartan $H$) $\,\cdot\,$ (raising $E_\alpha$), the ordered monomials form a basis of $U(\mathfrak{g})$ — any product can be reordered into this normal form using the commutation relations.

> **Definition — Verma module.** For a weight $\lambda$, the **Verma module** $M(\lambda)$ is generated by one vector $v_\lambda$ with the rules: $\rho(H)v_\lambda=\lambda(H)v_\lambda$ (it has weight $\lambda$) and $\rho(E_\alpha)v_\lambda=0$ for every positive root $\alpha$ (it is "highest"), with *no other relations*. By PBW, a basis of $M(\lambda)$ is
> $$
> \big\{\,\rho(E_{-\beta_1})^{k_1}\cdots\rho(E_{-\beta_N})^{k_N}\,v_\lambda\ :\ k_i\ge0\,\big\},
> $$
> running over the positive roots $\beta_1,\dots,\beta_N$. The monomial with exponents $k_i$ has weight $\lambda-\sum_i k_i\beta_i$.

$M(\lambda)$ is *infinite-dimensional* — we have applied lowering operators with no limit. It contains a unique maximal proper submodule $N(\lambda)$ (the sum of all submodules avoiding $v_\lambda$).

> **Theorem — construction of the irreducible.** The quotient $V(\lambda)=M(\lambda)/N(\lambda)$ is the irreducible representation with highest weight $\lambda$. If $\lambda$ is **dominant integral**, $V(\lambda)$ is **finite-dimensional**, completing the highest-weight bijection of s6.

**Why dominance gives finite dimension (the mechanism).**
1. For each simple root $\alpha_i$, the triple $H_i,E_i,E_{-i}$ is an $\mathfrak{sl}(2)$ (s3). The vector $v_\lambda$ has $H_i$-eigenvalue $m_i=\langle\lambda,\alpha_i\rangle\ge0$, an integer (dominant integral).
2. In $\mathfrak{sl}(2)$ representation theory (prerequisite), a highest weight $m_i\ge0$ forces $E_{-i}^{\,m_i+1}v_\lambda$ to be a *new* highest-weight vector of weight $\lambda-(m_i+1)\alpha_i$, and consistency requires it to vanish in the irreducible quotient.
3. These vanishing relations (one per simple root) chop the infinite Verma module down to finitely many surviving weights — precisely the weights $\le\lambda$ that survive all the $\mathfrak{sl}(2)$ truncations. The surviving set is finite and Weyl-symmetric (s8). $\blacksquare$ (mechanism; full proof via Weyl's theorem on complete reducibility)

**Worked example — building $\mathbf3$ of $\mathfrak{su}(3)$ from $\lambda=\omega_1=(1,0)$.**
1. Start with $v_\lambda$ at weight $\omega_1$. Its Dynkin labels are $(1,0)$: $\langle\lambda,\alpha_1\rangle=1$, $\langle\lambda,\alpha_2\rangle=0$.
2. Since $\langle\lambda,\alpha_2\rangle=0$, the $\alpha_2$-string from $v_\lambda$ has length $1$: applying $E_{-\alpha_2}$ gives $0$. Applying $E_{-\alpha_1}$ (label $1$) gives one new state at weight $\omega_1-\alpha_1$.
3. From that state, its $\alpha_2$-label is now $1$, so applying $E_{-\alpha_2}$ gives a third state at weight $\omega_1-\alpha_1-\alpha_2$. Applying any further lowering gives $0$.
4. Three states, weights forming a triangle: this is the quark triangle $u,d,s$ of the prerequisite. Dimension $3$, confirmed.

> **Pitfall.** The Verma module is infinite-dimensional and reducible; the *physical* multiplet is the finite quotient. Skipping the quotient (forgetting the $E_{-i}^{m_i+1}v_\lambda=0$ relations) produces spurious "states" with no place in nature.

<a id="s8"></a>
### The Weyl group, the Weyl character formula, and the Weyl dimension formula

**What and why.** The weight diagram of any representation has a hidden symmetry: it is invariant under the group of reflections generated by the roots, the **Weyl group**. Exploiting this symmetry, Weyl derived a closed formula for the **character** (the bookkeeping function recording every weight with multiplicity) and, as a corollary, a one-line formula for the **dimension** of $V(\lambda)$. These turn weight-counting from a hand search into arithmetic.

> **Definition — Weyl group.** The **Weyl group** $W$ is the group generated by the reflections $s_{\alpha_i}$ in the simple roots, acting on weight space by $s_\alpha(\mu)=\mu-\langle\mu,\alpha\rangle\,\alpha$. It is finite, permutes the roots, and acts simply transitively on the possible choices of positive system. For $\mathfrak{su}(2)$, $W=\mathbb{Z}_2$ ($\mu\mapsto-\mu$); for $\mathfrak{su}(3)=A_2$, $W$ is the symmetry group of the hexagon, the order-$6$ dihedral group $S_3$.

> **Definition — character.** The **character** of a representation $V$ is the formal sum over weights, $\mathrm{ch} V=\sum_\mu (\dim V_\mu)\,e^{\mu}$, where $e^\mu$ are formal exponentials with $e^\mu e^\nu=e^{\mu+\nu}$. It records all weights and multiplicities at once, and $\mathrm{ch}V|_{\text{set }e^\mu\to1}=\dim V$.

> **Definition — Weyl vector and the sign.** Let $\rho=\tfrac12\sum_{\alpha>0}\alpha$ be the **Weyl vector** (half the sum of positive roots; equals $\sum_i\omega_i$). For $w\in W$ let $\det(w)=(-1)^{\ell(w)}$ where $\ell(w)$ is the number of reflections needed to write $w$ (the **sign** of $w$).

> **Theorem — Weyl character formula.** For the irreducible $V(\lambda)$ with $\lambda$ dominant integral,
> $$
> \mathrm{ch}V(\lambda)\ =\ \frac{\displaystyle\sum_{w\in W}\det(w)\,e^{\,w(\lambda+\rho)}}{\displaystyle\sum_{w\in W}\det(w)\,e^{\,w(\rho)}} .
> $$
> The denominator equals the **Weyl denominator** $\displaystyle\prod_{\alpha>0}\big(e^{\alpha/2}-e^{-\alpha/2}\big)$.

The idea of the proof (cited in full from Weyl): the numerator and denominator are each *antisymmetric* under $W$ (the sign flips with each reflection), the ratio is therefore $W$-symmetric like a genuine character, and matching it against the highest weight $\lambda$ plus the multiplicity bookkeeping pins it uniquely. We extract the practical corollary in full.

> **Corollary — Weyl dimension formula.**
> $$
> \dim V(\lambda)\ =\ \prod_{\alpha>0}\frac{(\lambda+\rho,\alpha)}{(\rho,\alpha)} ,
> $$
> a product over the positive roots.

**Derivation of the dimension formula from the character formula.**
1. $\dim V(\lambda)$ is the character with every $e^\mu$ set to $1$. But setting $e^\mu\to1$ makes both numerator and denominator of the Weyl character formula vanish (each is an alternating sum that is $0$ at the "origin"), an indeterminate $0/0$.
2. Resolve it by the standard limiting trick: replace $e^\mu\to e^{t(\mu,\rho)}$ for a real parameter $t$ and let $t\to0$ (this is differentiating the alternating sums; legitimate because both are analytic in $t$).
3. The denominator becomes $\prod_{\alpha>0}\big(e^{t(\alpha,\rho)/2}-e^{-t(\alpha,\rho)/2}\big)\sim\prod_{\alpha>0} t(\alpha,\rho)$ as $t\to0$, since each factor $e^{x}-e^{-x}=2\sinh x\sim 2x$ to leading order, here with $x=t(\alpha,\rho)/2$, giving $\sim t(\alpha,\rho)$.
4. The numerator, by the same expansion with $\lambda+\rho$ in place of $\rho$, becomes $\sim\prod_{\alpha>0}t(\alpha,\lambda+\rho)$.
5. Taking the ratio, the powers of $t$ cancel ($|\Phi^+|$ factors each) and
$$
\dim V(\lambda)=\prod_{\alpha>0}\frac{(\lambda+\rho,\alpha)}{(\rho,\alpha)} . \qquad\blacksquare
$$

**Worked example — dimensions of $\mathfrak{su}(3)$ multiplets.** The three positive roots are $\alpha_1,\alpha_2,\alpha_1+\alpha_2$, and $\rho=\omega_1+\omega_2$. For $\lambda=(p,q)=p\,\omega_1+q\,\omega_2$, evaluating the products (using $(\omega_i,\alpha_j)=\tfrac12(\alpha_j,\alpha_j)\delta_{ij}=\delta_{ij}$ in this normalization) gives the famous closed form
$$
\dim V(p,q)=\tfrac12(p+1)(q+1)(p+q+2).
$$
Check: $(p,q)=(1,0)\Rightarrow\tfrac12\cdot2\cdot1\cdot3=3$ (the $\mathbf3$); $(1,1)\Rightarrow\tfrac12\cdot2\cdot2\cdot4=8$ (the octet $\mathbf8$); $(3,0)\Rightarrow\tfrac12\cdot4\cdot1\cdot5=10$ (the baryon decuplet $\mathbf{10}$). The arithmetic reproduces the Eightfold Way multiplet sizes exactly.

> **Pitfall.** The dimension formula uses $\lambda+\rho$, not $\lambda$; forgetting the Weyl vector $\rho$ is the most common error and gives nonsensical (often zero) dimensions.

## Part D — Worked theory and physics

<a id="s9"></a>
### $\mathfrak{su}(2)$ and $\mathfrak{su}(3)$ worked completely: multiplets and the eightfold way

**What and why.** We now assemble everything for the two algebras physics uses most, computing their irreducibles end to end so the abstract machinery becomes concrete numbers and pictures.

**$\mathfrak{su}(2)$ in full.** Rank $1$; complexified to $\mathfrak{sl}(2,\mathbb{C})$ with $[H,E]=2E,[H,F]=-2F,[E,F]=H$ (here $E=J_+,F=J_-,H=2J_3$). One simple root $\alpha$, one fundamental weight $\omega=\tfrac12\alpha$, Weyl group $\{1,-1\}$.
- Dominant integral weights are $\lambda=n\,\omega$, $n=0,1,2,\dots$ (Dynkin label $n$); physically $n=2j$ so spin $j=n/2$.
- The representation $V(n\omega)$ has weights $n,n-2,\dots,-n+2,-n$ (in $H$-eigenvalues), each multiplicity $1$.
- Dimension by Weyl: one positive root $\alpha$, $\rho=\omega$, $\dim=\dfrac{(\lambda+\rho,\alpha)}{(\rho,\alpha)}=\dfrac{(n+1)\omega\cdot\alpha}{\omega\cdot\alpha}=n+1=2j+1$. This is the familiar count of magnetic sub-states $m=-j,\dots,j$.

So $\mathfrak{su}(2)$ irreducibles are exactly the spin-$j$ multiplets, recovered from the general theory.

**$\mathfrak{su}(3)$ in full.** Rank $2$; six roots forming a hexagon (s3); positive roots $\alpha_1,\alpha_2,\alpha_1+\alpha_2$; Weyl group $S_3$ (order $6$); fundamental weights $\omega_1,\omega_2$.
- Multiplets labeled $(p,q)$, dimension $\tfrac12(p+1)(q+1)(p+q+2)$ (s8).
- The weight diagram of $V(p,q)$ is a hexagon (or triangle when $p$ or $q=0$) with outer boundary of side lengths $p$ and $q$, and **interior multiplicities** that increase by $1$ as you step inward across each ring until the rings become triangular, then stay constant. For the octet $(1,1)$: a hexagon of six outer weights plus the center with multiplicity $2$ ($6+2=8$).

**The Eightfold Way, derived.** Identify the three states of $\mathbf 3=(1,0)$ with quarks $u,d,s$ at weights (isospin $t_3$, hypercharge $y$):
$$
u:(\tfrac12,\tfrac13),\quad d:(-\tfrac12,\tfrac13),\quad s:(0,-\tfrac23).
$$
Then:
- **Mesons** $q\bar q$: $\mathbf3\otimes\overline{\mathbf3}=\mathbf8\oplus\mathbf1$ (dimensions $3\times3=9=8+1$). The octet is the pseudoscalar mesons $\pi^{\pm,0},K^{\pm},K^0,\bar K^0,\eta$; their weights are obtained by adding a quark weight to an antiquark weight, filling a hexagon with a doubly-occupied center.
- **Baryons** $qqq$: $\mathbf3\otimes\mathbf3\otimes\mathbf3=\mathbf{10}\oplus\mathbf8\oplus\mathbf8\oplus\mathbf1$ (dimensions $27=10+8+8+1$). The decuplet $\mathbf{10}=(3,0)$ is a triangle; its bottom-tip slot, weight $(0,-1)$ with three $s$ quarks, was the **$\Omega^-$**, predicted by this triangle and discovered in 1964.

The Gell-Mann–Nishijima relation $Q=t_3+\tfrac12 y$ converts each weight into electric charge; for $u$, $Q=\tfrac12+\tfrac12\cdot\tfrac13=\tfrac23$, the correct fractional quark charge. **The multiplet structure of hadrons is literally the irreducible-representation theory of $\mathfrak{su}(3)$.**

> **Pitfall.** Flavor $SU(3)$ is only approximate (the $s$ quark is heavier), so multiplets are split in mass; the *grouping* is exact representation theory, the *degeneracy* is broken by symmetry-violating terms. Do not expect equal masses, only equal quantum-number patterns.

<a id="s10"></a>
### Tensor products, branching rules, and Young tableaux for $\mathfrak{su}(n)$

**What and why.** Combining systems (two quarks, quark + antiquark) means tensoring representations; the result is reducible and decomposing it is "addition of multiplets." For $\mathfrak{su}(n)$ there is a beautiful combinatorial bookkeeping — **Young tableaux** — that performs these decompositions by drawing boxes.

> **Definition — tensor product of representations.** Given $\rho:\mathfrak{g}\to\mathfrak{gl}(V)$ and $\sigma:\mathfrak{g}\to\mathfrak{gl}(W)$, the **tensor product** acts on $V\otimes W$ (dimension $\dim V\cdot\dim W$) by the **sum** of generators: $(\rho\otimes\sigma)(X)=\rho(X)\otimes I+I\otimes\sigma(X)$. Consequently weights *add*: the weights of $V\otimes W$ are $\{\mu+\nu:\mu\in\mathrm{wt}V,\nu\in\mathrm{wt}W\}$ with multiplicities multiplied.

> **Method — decomposition by weights.** To decompose $V\otimes W=\bigoplus_i V(\lambda_i)$: list all summed weights, find the highest, peel off the irreducible with that highest weight (subtract its known weight diagram), and repeat. This is the multi-dimensional version of the $\mathfrak{su}(2)$ Clebsch–Gordan algorithm.

**Worked example — $\mathbf 3\otimes\mathbf3$ of $\mathfrak{su}(3)$.** The $9$ summed weights have highest weight $\omega_1+\omega_1=2\omega_1=(2,0)$, giving the symmetric sextet $\mathbf6$ ($\dim=\tfrac12\cdot3\cdot1\cdot4=6$). The remaining $3$ weights have highest weight $\omega_2=(0,1)$, the antisymmetric $\overline{\mathbf3}$. So
$$
\mathbf3\otimes\mathbf3=\mathbf6\oplus\overline{\mathbf3},\qquad 9=6+3.
$$

> **Definition — Young diagram and tableau.** A **Young diagram** is a left-justified array of boxes with row lengths $\lambda_1\ge\lambda_2\ge\cdots\ge0$. For $\mathfrak{su}(n)$ a diagram with at most $n-1$ rows labels an irreducible representation (columns of length $n$ may be deleted). The Dynkin labels are recovered from the differences of row lengths: $m_i=\lambda_i-\lambda_{i+1}$.

> **Rule — dimension via the hook-content formula (for $\mathfrak{su}(n)$).** $\dim=\prod_{\text{boxes}}\dfrac{n+c(\text{box})}{h(\text{box})}$, where $c=(\text{column}-\text{row})$ is the **content** and $h$ is the **hook length** (boxes to the right plus below plus itself). The **Littlewood–Richardson rule** decomposes a tensor product by combinatorially placing the boxes of one diagram into another.

**Worked example — $\mathfrak{su}(3)$ via boxes.** A single box $\square$ is $\mathbf3$. Then $\square\otimes\square$ = (two boxes in a row) $\oplus$ (two boxes in a column): the row is the symmetric $\mathbf6$, the column is $\overline{\mathbf3}$ (a height-$2$ column in $\mathfrak{su}(3)$), reproducing $\mathbf3\otimes\mathbf3=\mathbf6\oplus\overline{\mathbf3}$. For three boxes, $\mathbf3\otimes\mathbf3\otimes\mathbf3$ gives the row-of-3 ($\mathbf{10}$), two L-shaped tableaux ($\mathbf8\oplus\mathbf8$), and the column-of-3 (a full column, $=\mathbf1$): $\mathbf{10}\oplus\mathbf8\oplus\mathbf8\oplus\mathbf1$, exactly the baryon decomposition of s9.

> **Definition — branching rule.** A **branching rule** tells how an irreducible of $\mathfrak{g}$ decomposes when restricted to a subalgebra $\mathfrak{g}'\subset\mathfrak{g}$ (you simply read off which $\mathfrak{g}'$-weights the $\mathfrak{g}$-weights contain). Example: restricting $\mathfrak{su}(3)\to\mathfrak{su}(2)\times\mathfrak{u}(1)$ (isospin $\times$ hypercharge), the octet branches as $\mathbf8\to\mathbf3_0\oplus\mathbf2_{+1}\oplus\mathbf2_{-1}\oplus\mathbf1_0$ — recognizable as the $\Sigma$/$\Lambda$, nucleon, $\Xi$, and singlet content of the baryon octet.

> **Pitfall.** The generators add ($X\otimes I+I\otimes X$), but the *group elements* multiply ($\rho(g)\otimes\sigma(g)$); using the multiplicative rule at the algebra level is the classic addition-of-angular-momentum error.

<a id="s11"></a>
### Casimir operators, their eigenvalues, and physics applications (labeling states)

**What and why.** A multiplet needs labels. The CSA gives $r$ commuting labels *within* a multiplet (the weights). To label the multiplet *itself* — to say "this is the octet, that is the decuplet" — we need operators that are constant on each irreducible. These are the **Casimir operators**, built from the algebra and commuting with everything; by Schur's lemma they act as scalars on each irreducible, and those scalars are exactly the multiplet labels physicists quote.

> **Definition — quadratic Casimir.** Pick a basis $\{T_a\}$ and let $g^{ab}$ be the inverse of the Killing form matrix $g_{ab}=\kappa(T_a,T_b)$. The **quadratic Casimir** is the element of $U(\mathfrak{g})$
> $$
> C_2=\sum_{a,b} g^{ab}\,T_a T_b .
> $$
> It is **central**: $[C_2,X]=0$ for all $X\in\mathfrak{g}$.

**Proof that $C_2$ is central.**
1. Compute $[C_2,T_c]=\sum_{a,b}g^{ab}\big([T_a,T_c]T_b+T_a[T_b,T_c]\big)$, by the *Leibniz rule* for commutators with a product.
2. Substitute $[T_a,T_c]=\sum_d f_{ac}{}^{d}T_d$ and likewise for the other term, getting a sum of $f$'s contracted with $g^{ab}$ and two $T$'s.
3. Define $f_{abc}=\sum_d g_{cd} f_{ab}{}^{d}$. *Invariance of the Killing form* (s2), $\kappa([T_a,T_c],T_b)=\kappa(T_a,[T_c,T_b])$, says exactly that $f_{abc}$ is **totally antisymmetric** in its three indices.
4. The two terms in step 2, after raising indices with $g^{ab}$, become a contraction of the *symmetric* tensor $T_aT_b$-summed against the *antisymmetric* $f_{abc}$ (with relabeling), which vanishes. Hence $[C_2,T_c]=0$ for all $c$. $\blacksquare$

> **Theorem — Casimir eigenvalue (Freudenthal–Weyl).** On the irreducible $V(\lambda)$, the quadratic Casimir acts as the scalar
> $$
> C_2\big|_{V(\lambda)}=(\lambda,\lambda+2\rho)=(\lambda+\rho,\lambda+\rho)-(\rho,\rho),
> $$
> with $\rho$ the Weyl vector and $(\cdot,\cdot)$ the inner product induced by the Killing form.

**Proof.**
1. By Schur's lemma (an operator commuting with an irreducible representation is a scalar), $C_2$ acts as one number on $V(\lambda)$; compute it on the highest-weight vector $v_\lambda$.
2. Split $C_2$ into Cartan part and root parts: $C_2=\sum_{i,j}g^{ij}H_iH_j+\sum_{\alpha>0}(E_\alpha E_{-\alpha}+E_{-\alpha}E_\alpha)$, reorganized using the root space decomposition.
3. On $v_\lambda$: raising operators $E_\alpha$ ($\alpha>0$) annihilate it (highest weight, s6), so only $E_\alpha E_{-\alpha}$ survives via the commutator $E_\alpha E_{-\alpha}=E_{-\alpha}E_\alpha+[E_\alpha,E_{-\alpha}]=E_{-\alpha}E_\alpha+H_\alpha$, and $E_{-\alpha}E_\alpha v_\lambda=0$.
4. Collecting: $C_2 v_\lambda=\big((\lambda,\lambda)+\sum_{\alpha>0}(\lambda,\alpha)\big)v_\lambda=(\lambda,\lambda+2\rho)v_\lambda$, using $2\rho=\sum_{\alpha>0}\alpha$ from the *definition of the Weyl vector*. $\blacksquare$

**Worked example — Casimir of $\mathfrak{su}(2)$.** Here $C_2$ is (up to normalization) $J^2=J_1^2+J_2^2+J_3^2$. For spin $j$, $\lambda=2j\,\omega$ and the formula gives the eigenvalue $\propto j(j+1)$ — the famous $J^2|j,m\rangle=j(j+1)|j,m\rangle$, now seen as a special case of $(\lambda,\lambda+2\rho)$. It is the *same number* for every $m$ in the multiplet: a multiplet label.

**Worked example — Casimir of $\mathfrak{su}(3)$.** With $\lambda=(p,q)$ the formula evaluates to
$$
C_2(p,q)=\tfrac13\big(p^2+q^2+pq+3p+3q\big),
$$
so $\mathbf3=(1,0)\Rightarrow C_2=\tfrac43$, the octet $(1,1)\Rightarrow C_2=3$, the decuplet $(3,0)\Rightarrow C_2=6$. Distinct multiplets get distinct Casimir values — exactly the second label (beyond isospin and hypercharge) needed to name a state completely.

> **How states are labeled in the lab.** A hadron's quantum numbers are: the **Casimir(s)** naming its $SU(3)$ multiplet (which octet/decuplet), then the **weight** $(t_3,y)$ locating it within that multiplet, then a further $\mathfrak{su}(2)$ Casimir $j(j+1)$ and weight $m$ for spin. The number of independent Casimirs equals the **rank** $r$ (for $\mathfrak{su}(3)$ there are two: the quadratic and a cubic), and together with the $r$ weight labels they fully address every state. This is the operational meaning of the entire classification: *the conserved quantum numbers that label particles are the eigenvalues of the Casimir operators and the weights of the representation.*

> **Pitfall.** Higher-rank algebras need *more than one* Casimir to separate all irreducibles ($\mathfrak{su}(3)$ needs the cubic Casimir too — the quadratic alone does not distinguish all $(p,q)$ from $(q,p)$ pairs). The count is exactly the rank.

---

*We began with a single promise: that classifying representations classifies the multiplets nature allows. We made it good. The structure theory (Killing form, semisimplicity) isolated the good algebras; the root systems and Dynkin diagrams reduced each to a few integers and gave the finite Cartan–Killing list; the highest-weight theorem and Verma construction turned each dominant weight into a concrete multiplet; the Weyl formulas counted dimensions and weights in closed form; and the Casimir operators handed back the very quantum numbers experimenters tabulate. The hexagon of $\mathfrak{su}(3)$ is not a metaphor for the Eightfold Way — it is the weight diagram, and the $\Omega^-$ sat waiting in an empty corner of the lattice until the mathematics was believed. Read once for the arc from Killing form to Casimir eigenvalue; return to any boxed theorem when you need the machine. Symmetry, classified, is the catalogue of what can exist.*
