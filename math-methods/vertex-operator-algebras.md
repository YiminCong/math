**English** · [中文](vertex-operator-algebras.zh.md)

# Vertex Operator Algebras, *the algebra of two-dimensional conformal symmetry.*

*A self-contained first course in vertex (operator) algebras — the rigorous algebraic skeleton that hides inside the operator product expansion of two-dimensional conformal field theory. We begin with the question "how do we make the singular product of two quantum fields into honest algebra?", build the language of formal distributions and normal ordering, state and unpack the axioms of a vertex algebra (state–field correspondence, vacuum, translation, locality), prove the reconstruction theorem, add a conformal structure and the central charge, and then work the central examples by hand: the free boson, lattice algebras and bosonization, and the affine Kac–Moody algebras with their Sugawara stress tensor. We close with modules, Zhu's associative algebra, characters and modular invariance, and the spectacular appearance of the Monster group in Monstrous Moonshine. Every term is defined in words on first use, every formula is motivated, and every derivation is a numbered, gap-free chain of reasons. We assume basic algebra and single-variable calculus, and we lean on two companion guides: [Conformal Field Theory](conformal-field-theory.md) for the OPE, the Virasoro algebra, and radial quantization, and [Lie Representation Theory](../group-theory/lie-representations.md) for Lie algebras, their representations, and Kac–Moody algebras. Each borrowed fact is restated in one line where it is used.*

[← Back to all guides](../README.md)

## Part A · From physics to formal algebra

<a id="s0"></a>
### Motivation: making the OPE into rigorous algebra

#### What & why, in one breath

In two-dimensional conformal field theory one writes products of quantum fields $A(z)B(w)$ that *blow up* as the points collide, $z\to w$, and tames them with the **operator product expansion** (OPE): an expansion of the singular product as a sum of less-and-less singular terms,
$$
A(z)B(w)\;\sim\;\sum_{n}\frac{\{A_{(n)}B\}(w)}{(z-w)^{n+1}},
$$
where each numerator $\{A_{(n)}B\}(w)$ is again a field of the theory. (We restate this from the [CFT guide](conformal-field-theory.md): the OPE encodes how two local operators, brought close, look like a single local operator with calculable coefficients.) Physicists manipulate these expansions freely. The goal of this guide is to turn that manipulation into a *theorem-proving* algebraic structure — a **vertex algebra** — in which the OPE coefficients are genuine algebra operations satisfying precise axioms. The payoff is enormous: questions of consistency, classification of theories, and deep number theory (modular forms, the Monster) become provable statements rather than formal slogans.

#### The word "chiral"

A 2D CFT generically depends on a point through two independent coordinates, a holomorphic one $z$ and an antiholomorphic one $\bar z$ (the [CFT guide](conformal-field-theory.md) explains this splitting). The part depending on $z$ alone — built from holomorphic fields like the stress tensor $T(z)$ — is called the **chiral** (or **holomorphic**) part of the theory; "chiral" means "of one handedness." A **chiral algebra** is the algebra of these holomorphic fields under the OPE. A vertex algebra is the precise mathematical definition of a chiral algebra. So the slogan is:

> vertex algebra = chiral algebra = the rigorous algebra of the holomorphic OPE.

#### What goes wrong if we are naive

A first instinct is to treat $A(z)$ as an "operator-valued function" and multiply pointwise. This fails on three counts, each of which the formalism must fix:

- **Singularities.** $A(z)B(w)$ has poles at $z=w$; there is no value "at $z=w$." We must keep the whole Laurent-type expansion, not a single product.
- **Operator ordering.** In a quantum theory operators do not commute; the product depends on which acts first. We need a canonical ordering (normal ordering).
- **Not honest functions.** $A(z)=\sum_n A_{(n)} z^{-n-1}$ is a *formal* series with operator coefficients, doubly infinite in $n$. It need not converge anywhere; it is a **formal distribution**, an object to be paired against test series, not evaluated at a number.

#### The whole guide on one line

> OPE in CFT → formal distributions & normal ordering → vertex-algebra axioms (state–field map, vacuum, translation, locality) → reconstruction theorem → conformal structure & central charge → free boson → lattices & bosonization → affine Kac–Moody & Sugawara → modules & rationality → Zhu's algebra → characters & modular invariance → Monster & Moonshine.

#### Pitfall

A vertex algebra is *not* an associative or Lie algebra with one bilinear product. It carries *infinitely many* bilinear products $A_{(n)}B$, one for each integer $n$, packaged into a single generating object $Y(A,z)B$. Forgetting this — looking for a single "multiplication" — is the most common early confusion.

<a id="s1"></a>
### Formal distributions, fields, and normal ordering

#### What & why

Before axioms we need the alphabet. Everything in a vertex algebra is built from **formal power series in a variable $z$ with coefficients that are operators on a vector space**. This section defines those series, the special ones called *fields*, the formal **delta function** that is the algebraic shadow of the OPE's poles, and the **normal-ordered product** that fixes operator ordering.

#### Formal distributions

Fix a vector space $V$ over the complex numbers $\mathbb{C}$, and let $\mathrm{End}V$ denote the space of linear maps $V\to V$ (its "endomorphisms" — the operators).

> **Definition — formal distribution.** A **formal distribution** in the variable $z$ with values in $\mathrm{End}V$ is a doubly infinite series
> $$
> a(z)\;=\;\sum_{n\in\mathbb{Z}} a_{(n)}\,z^{-n-1},\qquad a_{(n)}\in\mathrm{End}V.
> $$
> The space of all such is written $(\mathrm{End}V)[[z,z^{-1}]]$. The number $a_{(n)}$ is the **$n$-th mode** of $a(z)$. The peculiar exponent $-n-1$ is a convention chosen so that $a_{(n)}$ is recovered by a formal residue (defined below); it makes later formulas clean.

The double square brackets mean "all coefficients allowed, both positive and negative powers, no convergence required." We *cannot* in general multiply two such series (the coefficient of a given power would be an infinite sum). Multiplication is only defined under the field condition next.

> **Definition — formal residue.** The **residue** of a formal distribution is the coefficient of $z^{-1}$:
> $$
> \mathrm{Res}_z a(z)\;=\;a_{(0)}.
> $$
> This is the algebraic analogue of $\frac1{2\pi i}\oint a(z)\,dz$ from contour integration (see [Complex Analysis](../complex-analysis/complex-analysis.md): the contour integral of a Laurent series picks out the $z^{-1}$ coefficient). We use $\mathrm{Res}$ purely formally — no contour, no convergence.

#### Fields

> **Definition — field.** A formal distribution $a(z)=\sum_n a_{(n)} z^{-n-1}\in(\mathrm{End}V)[[z,z^{-1}]]$ is a **field** on $V$ if for every vector $v\in V$ only finitely many *positive*-mode terms act nontrivially:
> $$
> a_{(n)}\,v=0\quad\text{for all }n\text{ sufficiently large (depending on }v).
> $$

The point of the field condition is that it makes $a(z)v$ a series with values in $V((z))$ — formal Laurent series, meaning finitely many negative powers of $z$ once truncated from below; concretely $a(z)v=\sum_{n} (a_{(n)}v)\,z^{-n-1}$ terminates above in $n$, so it is a genuine Laurent series in $z$. Such series *can* be substituted into one another and multiplied at $z\neq w$, which is what makes the whole theory work.

#### The formal delta function

The single most important formal distribution is built from *two* variables.

> **Definition — formal delta function.**
> $$
> \delta(z-w)\;=\;\sum_{n\in\mathbb{Z}} z^{-n-1} w^{n}\;=\;\sum_{n\in\mathbb{Z}} w^{n} z^{-n-1}.
> $$

It is a formal distribution in $z$ and $w$ together. Its defining property is the *sifting* property, the algebraic mirror of the Dirac delta from the [Fourier guide](fourier-transforms.md).

> **Lemma (sifting).** For any field $a(z)$,
> $$
> \mathrm{Res}_z\,a(z)\,\delta(z-w)\;=\;a(w).
> $$

*Proof.*
1. Write $a(z)=\sum_m a_{(m)} z^{-m-1}$ and $\delta(z-w)=\sum_n z^{-n-1}w^n$. *(Definitions.)*
2. Their product, collecting powers, is $\sum_{m,n} a_{(m)}\, z^{-m-1}z^{-n-1} w^n=\sum_{m,n} a_{(m)} w^n z^{-m-n-2}$. *(Multiply series; this is legal here because for each fixed power of $z$ the $w$-coefficient is a single operator, no infinite sum arises.)*
3. Take $\mathrm{Res}_z$, i.e. keep the coefficient of $z^{-1}$. This requires $-m-n-2=-1$, i.e. $m=-n-1$. *(Definition of residue.)*
4. Substituting $m=-n-1$ leaves $\sum_n a_{(-n-1)} w^n=\sum_n a_{(-n-1)} w^n$. Reindex $k=-n-1$, so $n=-k-1$: $\sum_k a_{(k)} w^{-k-1}=a(w)$. *(Reindexing a sum over all integers, allowed.)*
$\blacksquare$

Two central identities follow by matching modes exactly as above. First,
$$
(z-w)\,\delta(z-w)\;=\;0.
$$
*Proof.* Multiply: $(z-w)\sum_m z^{-m-1}w^m=\sum_m z^{-m}w^m-\sum_m z^{-m-1}w^{m+1}$. Reindex the second sum by $m'=m+1$ to get $\sum_{m'} z^{-m'}w^{m'}$, identical to the first. Their difference telescopes to $0$. *(Reindexing a sum over all of $\mathbb{Z}$ is allowed because no boundary terms exist.)* $\blacksquare$ Second,
$$
(z-w)\,\partial_w\,\delta(z-w)\;=\;-\,\delta(z-w).
$$
*Proof.* Differentiate the first identity in $w$: $\partial_w[(z-w)\delta(z-w)]=-\delta(z-w)+(z-w)\partial_w\delta(z-w)=0$, so $(z-w)\partial_w\delta(z-w)=\delta(z-w)\cdot(?)$ — rearranging gives exactly $(z-w)\partial_w\delta=-\delta$. *(Product rule on a formal distribution, term by term.)* $\blacksquare$ More generally $(z-w)^{k+1}\partial_w^{k}\delta(z-w)=0$ for each $k\ge0$, by induction using these two facts. These tell us *how many derivatives of $\delta$ survive multiplication by powers of $(z-w)$* — precisely the data of how singular an OPE is. The general principle, the **decomposition theorem for local distributions**, states: a formal distribution $f(z,w)$ killed by $(z-w)^N$ is a finite sum $f(z,w)=\sum_{j=0}^{N-1}c^j(w)\,\frac{1}{j!}\partial_w^{j}\delta(z-w)$ for unique fields $c^j(w)$. This is the algebraic engine behind the commutator-to-OPE dictionary.

#### Normal ordering

To define a product of two fields at the *same* point we must order modes. Decompose any field into its **annihilation** and **creation** parts:
$$
a(z)_+=\sum_{n\ge 0} a_{(n)} z^{-n-1},\qquad a(z)_-=\sum_{n<0} a_{(n)} z^{-n-1},
$$
so $a(z)=a(z)_++a(z)_-$. The subscript $+$ collects the **annihilation modes** $a_{(n)}$ with $n\ge0$ (which, by the field condition, kill any vector eventually), and $-$ the **creation modes** $a_{(n)}$ with $n<0$.

> **Definition — normal-ordered product.** The **normal-ordered product** of two fields, written $\,{:}a(z)b(w){:}\,$, places creation modes to the left of annihilation modes:
> $$
> {:}a(z)b(w){:}\;=\;a(z)_-\,b(w)\;+\;b(w)\,a(z)_+.
> $$
> The same-point product is $\,{:}a(z)b(z){:}\,$, obtained by setting $w=z$ afterward; the ordering above is exactly what makes this substitution well defined (each coefficient is a finite sum).

The intuition: creation operators raise energy and act first conceptually ("create the state"), annihilation operators lower energy and act last; normal ordering subtracts the divergent vacuum contribution that arises when an annihilation mode meets a creation mode. This is the rigorous version of the physicist's ":  :" symbol.

#### Worked example with real numbers

Let $V$ have a basis indexed by integers and suppose two fields have only the modes $a_{(0)},a_{(-1)}$ and $b_{(0)},b_{(-1)}$ nonzero (a tiny toy). Then $a(z)_+=a_{(0)}z^{-1}$, $a(z)_-=a_{(-1)}z^{0}=a_{(-1)}$. Normal ordering gives
$$
{:}a(z)b(z){:}\;=\;a_{(-1)}\,b(z)\;+\;b(z)\,a_{(0)}z^{-1}.
$$
If concretely $a_{(0)}=b_{(0)}=0$ and $a_{(-1)}=b_{(-1)}=M$ for a single matrix $M$, then $\,{:}a(z)b(z){:}=M\cdot(M z^{0})=M^2$, a finite operator — whereas the *naive* product $a(z)b(z)$ at $z=w$ would have produced an ill-defined coincidence. Normal ordering returned a sensible answer.

#### Contractions and Wick's theorem

The difference between the full product and its normal ordering is the **contraction**:
$$
a(z)\,b(w)\;-\;{:}a(z)b(w){:}\;=\;\underbracket{a(z)b(w)}\;,
$$
where the underbracket denotes the singular part — a $c$-number-valued (or central) formal distribution supported at $z=w$. For free fields (boson, fermion) every higher correlation is a sum over all ways of pairing the fields into contractions: this is **Wick's theorem**, the computational backbone of §s5–s7. We use it repeatedly: to compute an OPE of normal-ordered products, contract each field of one factor with each field of the other in all possible ways, leaving the rest normal-ordered.

#### Pitfall

Normal ordering is **not associative or commutative** as an honest product: $\,{:}{:}ab{:}c{:}\neq{:}a{:}bc{:}{:}\,$ in general, and the failure is measured by exactly the contractions just defined. The whole machinery of vertex algebras exists precisely to control these failures in a coordinate-independent way.

## Part B · The axioms and their first consequences

<a id="s2"></a>
### The axioms of a vertex algebra

#### What & why

We now write the definition. A vertex algebra packages a vector space of **states**, a distinguished **vacuum** state, a **translation** operator, and a rule $Y$ assigning to each state a field — the **state–field correspondence** — subject to a compatibility called **locality**. Read the axioms as the rigorous skeleton of the physical picture: states ↔ operators (the state–operator map of radial quantization from the [CFT guide](conformal-field-theory.md)), and operators that are far apart commute up to the controlled singularity of the OPE.

> **Definition — vertex algebra.** A **vertex algebra** is a quadruple $(V,\,|0\rangle,\,T,\,Y)$ where:
> - $V$ is a $\mathbb{C}$-vector space, the **space of states**;
> - $|0\rangle\in V$ is the **vacuum vector**, a distinguished state;
> - $T:V\to V$ is a linear map, the **translation operator** (also called the **infinitesimal translation**);
> - $Y(\cdot,z):V\to(\mathrm{End}V)[[z,z^{-1}]]$ is the **state–field correspondence**, sending each state $A\in V$ to a field
> $$
> Y(A,z)=\sum_{n\in\mathbb{Z}} A_{(n)}\,z^{-n-1},\qquad A_{(n)}\in\mathrm{End}V,
> $$
> called the **vertex operator** of $A$;
>
> subject to the axioms:
>
> 1. **(Field axiom)** For every $A$, $Y(A,z)$ is a field: $A_{(n)}B=0$ for $n$ large (depending on $A,B$).
> 2. **(Vacuum axiom)** $Y(|0\rangle,z)=\mathrm{id}_V$ (the identity field, all modes zero except the constant term), and for every $A$,
> $$
> Y(A,z)|0\rangle\;\in\;A+zV[[z]],\qquad\text{i.e.}\quad Y(A,z)|0\rangle\big|_{z=0}=A.
> $$
> The state $A$ is "created from the vacuum by its own field at $z=0$."
> 3. **(Translation axiom)** $T|0\rangle=0$, and for every $A$,
> $$
> [\,T,\,Y(A,z)\,]\;=\;\partial_z\,Y(A,z).
> $$
> Translation acts on fields as the derivative in $z$.
> 4. **(Locality axiom)** For every pair $A,B$ there is an integer $N\ge0$ with
> $$
> (z-w)^{N}\,\big[\,Y(A,z),\,Y(B,w)\,\big]\;=\;0
> $$
> as a formal distribution in $z,w$. The fields are then said to be **mutually local**.

#### Unpacking each axiom in words

- **State–field correspondence $Y$.** This is the heart. To every *state* $A$ it attaches an *operator-valued field* $Y(A,z)$. In CFT language it is the state–operator map made into structure: the state is the field acting on the vacuum at the origin.
- **Vacuum.** $|0\rangle$ is the "empty" state. Its field is the identity (doing nothing). The second part, $Y(A,z)|0\rangle\to A$ as $z\to0$, says the correspondence is *invertible at the origin*: you can recover the state from its field.
- **Translation.** $T$ generates motion in $z$. The bracket relation says "shifting the field is the same as differentiating it" — the algebraic form of $\partial_z = $ "generator of translations."
- **Locality.** Two fields generally don't commute, but multiplying by a high enough power of $(z-w)$ — which *kills poles at $z=w$* — makes the commutator vanish. The minimal such $N$ is the **order of locality**, and it counts the depth of the singular OPE between $A$ and $B$. Locality is the rigorous replacement for "fields at separated points commute."

#### The OPE lives inside the axioms

The modes $A_{(n)}B$ are exactly the OPE coefficients of §s0. Indeed define the **$n$-th product** $A_{(n)}B$ as the $n$-th mode of $Y(A,z)$ applied to $B$. Then locality is equivalent (this is the **Borcherds identity**, the master axiom — we state it rather than prove the full equivalence, which is a long mode-by-mode computation) to a single identity among the $n$-th products:
$$
\sum_{j\ge0}\binom{m}{j}\big(A_{(n+j)}B\big)_{(m+k-j)}C
=\sum_{j\ge0}(-1)^{j}\binom{n}{j}\Big(A_{(m+n-j)}\big(B_{(k+j)}C\big)-(-1)^{n}B_{(n+k-j)}\big(A_{(m+j)}C\big)\Big),
$$
for all integers $m,n,k$. This one identity simultaneously encodes associativity-up-to-poles and skew-symmetry of the products; it is the vertex-algebra analogue of the Jacobi identity for Lie algebras.

#### Two consequences proved directly

**(i) The translation operator is determined by $Y$:**
$$
T A \;=\; A_{(-2)}|0\rangle \;=\; \partial_z\,Y(A,z)|0\rangle\big|_{z=0}.
$$
*Proof.*
1. From the translation axiom, $[T,Y(A,z)]=\partial_z Y(A,z)$. Apply both sides to $|0\rangle$. *(Allowed: both sides are operators.)*
2. The left side is $T\,Y(A,z)|0\rangle - Y(A,z)\,T|0\rangle$. The second term vanishes since $T|0\rangle=0$. *(Translation axiom, part 1.)*
3. So $T\,Y(A,z)|0\rangle=\partial_z Y(A,z)|0\rangle$. Set $z=0$. On the left, $Y(A,z)|0\rangle\to A$ by the vacuum axiom, giving $TA$. *(Vacuum axiom.)*
4. On the right, $\partial_z Y(A,z)|0\rangle$ at $z=0$ is the coefficient of $z^1$ in $Y(A,z)|0\rangle$ times $1$, which is $A_{(-2)}|0\rangle$ (since the $z^1$ coefficient of $\sum_n A_{(n)}|0\rangle z^{-n-1}$ comes from $-n-1=1$, i.e. $n=-2$). *(Read off the mode; derivative brings down the power.)*
$\blacksquare$

**(ii) Creation property (skew-symmetry seed):** $Y(A,z)|0\rangle=e^{zT}A$.
*Proof.*
1. Let $f(z)=Y(A,z)|0\rangle$. By step 3 above, $\partial_z f(z)=T f(z)$. *(Derived from translation + vacuum.)*
2. The unique formal power-series solution with $f(0)=A$ is $f(z)=e^{zT}A=\sum_{k\ge0}\frac{z^k}{k!}T^kA$. *(Solving the formal ODE $f'=Tf$, $f(0)=A$; coefficients match term by term.)*
3. By the vacuum axiom $f(0)=A$, so the boundary condition holds and $Y(A,z)|0\rangle=e^{zT}A$. $\blacksquare$

#### Skew-symmetry, a consequence of locality

A third structural consequence, which we record because it is used constantly, is **skew-symmetry**:
$$
Y(A,z)B\;=\;e^{zT}\,Y(B,-z)\,A.
$$
In words: swapping the two arguments of a vertex operator costs a sign change in $z$ and a translation $e^{zT}$ — the algebraic shadow of "moving operator $A$ past operator $B$." It is the vertex-algebra analogue of the antisymmetry $[x,y]=-[y,x]$ of a Lie bracket, and it is *derived* from locality plus the creation property $Y(A,z)|0\rangle=e^{zT}A$ (§s2 consequence ii), not assumed. Concretely, for the $(-1)$-product it gives $A_{(-1)}B=B_{(-1)}A+\sum_{j\ge0}\frac{(-1)^j}{(j+1)!}T^{j+1}(B_{(j)}A)$ — the commutativity of normal ordering "up to total derivatives," a fact we lean on in §s5.

#### Worked micro-example

The simplest vertex algebra is $V=\mathbb{C}$, the **trivial** one: $|0\rangle=1$, $T=0$, $Y(\lambda,z)=\lambda\cdot\mathrm{id}$. All axioms hold ($Y(|0\rangle,z)=\mathrm{id}$; $Y(A,z)|0\rangle=\lambda\to\lambda=A$; $[T,\cdot]=0=\partial_z(\text{constant})$; commutators vanish so $N=0$). It is the "point" of vertex-algebra geometry — small, but it shows the axioms are consistent.

#### Pitfall

Locality with exponent $N$ does **not** mean the fields commute; it means their commutator is a *finite* sum of derivatives of the delta function, $[Y(A,z),Y(B,w)]=\sum_{j=0}^{N-1}\frac{1}{j!}\big(A_{(j)}B\big)(w)\,\partial_w^{j}\delta(z-w)$. This "commutator formula" (proved by combining locality with the delta identities of §s1) is how the singular OPE is read off, term by term.

<a id="s3"></a>
### The reconstruction theorem

#### What & why

Defining a vertex algebra abstractly is one thing; *building* one is another. In practice we know a few **generating fields** (say, a boson current $a(z)$, or a stress tensor $T(z)$) and their OPEs, and we want a theorem that says: "if these fields satisfy the obvious conditions, there is a unique vertex algebra they generate, and here is the formula for *every* vertex operator." That theorem is **reconstruction** (also called **existence**). It is the workhorse: every example below is built with it.

#### Statement

> **Theorem (Reconstruction / Existence).** Let $V$ be a vector space with a vector $|0\rangle$, an operator $T$ with $T|0\rangle=0$, and a collection of fields $\{a^{i}(z)=\sum_n a^{i}_{(n)}z^{-n-1}\}_{i\in I}$ such that:
> 1. **(Translation covariance)** $[T,a^{i}(z)]=\partial_z a^{i}(z)$ for all $i$;
> 2. **(Vacuum)** $a^{i}(z)|0\rangle\in a^{i}_{(-1)}|0\rangle + zV[[z]]$, i.e. the fields are regular on the vacuum at $z=0$;
> 3. **(Mutual locality)** the $a^{i}(z)$ are pairwise mutually local;
> 4. **(Generation)** the vectors
> $$
> a^{i_1}_{(-n_1-1)}\,a^{i_2}_{(-n_2-1)}\cdots a^{i_k}_{(-n_k-1)}\,|0\rangle,\qquad n_1,\dots,n_k\ge0,
> $$
> span $V$ (the states are built by acting with creation modes on the vacuum).
>
> Then there is a **unique** vertex-algebra structure $Y$ on $(V,|0\rangle,T)$ such that $Y(a^{i}_{(-1)}|0\rangle,z)=a^{i}(z)$. Moreover the vertex operator of a general spanning vector is
> $$
> Y\!\Big(a^{i_1}_{(-n_1-1)}\cdots a^{i_k}_{(-n_k-1)}|0\rangle,\,z\Big)
> =\frac{1}{n_1!\cdots n_k!}\;{:}\,\partial_z^{n_1}a^{i_1}(z)\,\cdots\,\partial_z^{n_k}a^{i_k}(z)\,{:}\,.
> $$

#### How it builds vertex operators — the mechanism

The formula is the entire content of "building from generators." Read it in three moves:

1. **A state is a word in creation modes.** Generation (hypothesis 4) says every state is $a^{i_1}_{(-n_1-1)}\cdots|0\rangle$. The mode $a^{i}_{(-n-1)}$ corresponds, the formula says, to the *field* $\frac{1}{n!}\partial_z^{n} a^{i}(z)$ — taking $n$ derivatives raises the singularity order by $n$, matching the shift $(-1)\to(-n-1)$ in the mode.
2. **A product of modes becomes a normal-ordered product of fields.** Several creation modes acting in sequence map to the normal-ordered product $\,{:}\cdots{:}\,$ of the corresponding fields — normal ordering is forced because that is the only same-point product that is well defined (§s1).
3. **Uniqueness from locality.** Locality (hypothesis 3) guarantees these normal-ordered products satisfy the Borcherds identity, hence give a genuine vertex algebra; and it forces uniqueness, because two local fields agreeing on the vacuum agree everywhere (a "uniqueness theorem" / "Goddard's lemma": a field local to the vacuum-creating field with the same action on $|0\rangle$ is equal to it).

#### Sketch of the uniqueness lemma (the engine)

> **Lemma (Goddard uniqueness).** If $a(z)$ and $b(z)$ are both local with respect to all $Y(C,w)$, both translation-covariant, and $a(z)|0\rangle=b(z)|0\rangle$, then $a(z)=b(z)$.

*Proof sketch.*
1. Set $d(z)=a(z)-b(z)$; then $d(z)|0\rangle=0$ and $d$ is local to everything. *(Linearity.)*
2. For any state $C=Y(C,w)|0\rangle$ approximant, locality gives $(z-w)^N[d(z),Y(C,w)]=0$, so $(z-w)^N d(z)Y(C,w)|0\rangle=(z-w)^N Y(C,w)d(z)|0\rangle=0$. *(Locality + $d(z)|0\rangle=0$.)*
3. A formal distribution killed by a power of $(z-w)$ and vanishing on $|0\rangle$ for a spanning set of $C$ must vanish, because multiplication by $(z-w)^N$ is injective on the relevant space of Laurent series. *(Injectivity of $(z-w)^N\cdot$ on $V((w))((z))$.)*
4. Hence $d(z)=0$, i.e. $a(z)=b(z)$. $\blacksquare$

#### Worked example with real numbers (a free fermion preview)

Take one generating field $b(z)$ with the locality $(z-w)^1[b(z),b(w)]_+=0$ in the *anti*commuting (super) version, modes $\{b_{(m)},b_{(n)}\}=\delta_{m+n,-1}$. Reconstruction produces the **free fermion** vertex superalgebra; the state $b_{(-1)}|0\rangle$ has field $b(z)$, and $b_{(-2)}|0\rangle$ has field $\partial_z b(z)$, exactly as the formula dictates with $n=1$, $1/1!=1$. We will see the bosonic analogue fully in §s5.

#### Associativity, the other face of the axioms

It is worth seeing why reconstruction is even possible: the deep fact it rests on is that locality is *equivalent* to **associativity of the OPE**. Concretely, for three states $A,B,C$ there is an integer $M$ with
$$
(z+w)^{M}\,Y(A,z+w)\,Y(B,w)\,C\;=\;(z+w)^{M}\,Y\big(Y(A,z)B,\,w\big)\,C,
$$
read as formal series expanded in the appropriate domains. The left side is "act with $A$ then $B$"; the right side is "first fuse $A$ and $B$ via the OPE $Y(A,z)B$, then act." Their agreement after clearing poles is the rigorous form of the physicist's statement that the OPE is associative — you may bring operators together in any order. Borcherds' identity (§s2) is precisely the bookkeeping that makes locality, skew-symmetry, and this associativity a single statement. Reconstruction works because normal-ordered products of local fields automatically satisfy it.

#### Pitfall

Reconstruction needs all four hypotheses. Dropping **generation** leaves a vertex algebra strictly larger than the one you described; dropping **locality** breaks the Borcherds identity and you get no vertex algebra at all. Checking locality of your generators is the real work in any construction.

## Part C · Conformal structure and the first examples

<a id="s4"></a>
### Conformal vertex algebras, the Virasoro element, and the central charge

#### What & why

A bare vertex algebra has translation $T$ but no notion of *scaling* or *energy*. A **conformal** vertex algebra adds a single distinguished state $\omega$ — the **conformal vector** — whose field is the stress tensor and whose modes generate the **Virasoro algebra**. The number $c$ appearing there is the **central charge**, the same anomaly we met in the [CFT guide](conformal-field-theory.md), now an invariant of the algebra.

#### The Virasoro algebra, restated

From the [CFT guide](conformal-field-theory.md): the **Virasoro algebra** is the Lie algebra with basis $\{L_n\}_{n\in\mathbb{Z}}$ and central element $C$, with brackets
$$
[L_m,L_n]=(m-n)L_{m+n}+\frac{C}{12}\,(m^3-m)\,\delta_{m+n,0},\qquad [L_m,C]=0.
$$
On a representation $C$ acts as a scalar $c\cdot\mathrm{id}$, the **central charge**. It is the unique (up to scale) central extension of the **Witt algebra** $[L_m,L_n]=(m-n)L_{m+n}$ of holomorphic vector fields $-z^{n+1}\partial_z$.

#### Definition of a conformal structure

> **Definition — conformal vertex algebra.** A vertex algebra $V$ is **conformal of central charge $c$** if there is a state $\omega\in V$, the **conformal vector**, whose field
> $$
> Y(\omega,z)=\sum_{n\in\mathbb{Z}}L_n\,z^{-n-2}\qquad(\text{so }L_n=\omega_{(n+1)})
> $$
> — written with the shifted exponent $-n-2$ because $\omega$ has *conformal weight 2*, like a stress tensor — has modes $L_n$ satisfying:
> 1. **(Virasoro)** $[L_m,L_n]=(m-n)L_{m+n}+\frac{c}{12}(m^3-m)\delta_{m+n,0}$;
> 2. **(Translation)** $L_{-1}=T$ (the $-1$ mode is the translation operator);
> 3. **(Grading / Hamiltonian)** $L_0$ is diagonalizable on $V$ with integer (or in graded cases, rational) eigenvalues bounded below; the $L_0$-eigenvalue of a state is its **conformal weight** (or **energy**) $\Delta$, and $V=\bigoplus_{\Delta} V_\Delta$.

A state $A$ with $L_0 A=\Delta A$ and $L_n A=0$ for $n>0$ is a **(quasi-)primary**/highest-weight state; the grading by $\Delta$ is the algebraic shadow of energy.

#### Where the central charge comes from — the structural statement

In the [CFT guide](conformal-field-theory.md) the $\frac{c}{12}(m^3-m)$ term was derived from the Jacobi identity (it is the unique cocycle) and re-derived from the $TT$ OPE
$$
T(z)T(w)\sim\frac{c/2}{(z-w)^4}+\frac{2T(w)}{(z-w)^2}+\frac{\partial T(w)}{z-w}.
$$
In vertex-algebra language this OPE *is* the statement that $\omega_{(3)}\omega=\frac{c}{2}|0\rangle$, $\omega_{(1)}\omega=2\omega$, $\omega_{(0)}\omega=\partial\omega=T\omega$, and $\omega_{(n)}\omega=0$ for $n\ge4$. Let us verify that these $n$-th products reproduce the Virasoro relation, *deriving* the $(m^3-m)$ structure from the OPE.

**Derivation of the Virasoro bracket from the $TT$ OPE.**
1. The commutator formula (§s2 pitfall) gives, for the local pair $(\omega,\omega)$,
$$
[L_m,L_n]=\sum_{j\ge0}\binom{m+1}{j}\big(\omega_{(j)}\omega\big)_{(m+n+2-j)} ,
$$
which is the general mode-commutator formula $[a_{(p)},b_{(q)}]=\sum_j\binom{p}{j}(a_{(j)}b)_{(p+q-j)}$ applied with $p=m+1$, $q=n+1$ via the weight-2 shift $L_n=\omega_{(n+1)}$ (equivalently $\omega_{(k)}=L_{k-1}$). *(Commutator formula for modes.)*
2. Only $j=0,1,3$ contribute, since $\omega_{(j)}\omega=0$ otherwise. *(From the OPE data above.)*
3. **$j=0$:** $\binom{m+1}{0}(\omega_{(0)}\omega)_{(m+n+2)}=(T\omega)_{(m+n+2)}=(\partial\omega)_{(m+n+2)}$. On modes the translation operator acts by $(\partial A)_{(k)}=-k\,A_{(k-1)}$, so with $k=m+n+2$ this is $-(m+n+2)\,\omega_{(m+n+1)}=-(m+n+2)\,L_{m+n}$. *(Property $TA=\partial A$ shifts a mode and brings down its index.)*
4. **$j=1$:** $\binom{m+1}{1}(\omega_{(1)}\omega)_{(m+n+1)}=(m+1)\,(2\omega)_{(m+n+1)}=2(m+1)\,\omega_{(m+n+1)}=2(m+1)\,L_{m+n}$. Adding steps 3 and 4, the coefficient of $L_{m+n}$ is $-(m+n+2)+2(m+1)=(m-n)$, giving the term $(m-n)L_{m+n}$. *(Arithmetic of the two contributions.)*
5. **$j=3$:** $\binom{m+1}{3}(\omega_{(3)}\omega)_{(m+n-1)}=\binom{m+1}{3}\big(\tfrac{c}{2}|0\rangle\big)_{(m+n-1)}$. Since $|0\rangle_{(k)}=\delta_{k,-1}\mathrm{id}$, the mode $(m+n-1)$ acts as the identity exactly when $m+n-1=-1$, i.e. $m+n=0$, giving the term $\frac{c}{2}\binom{m+1}{3}\delta_{m+n,0}$. *(Vacuum mode acts as identity only in degree $-1$.)*
6. Finally $\frac{c}{2}\binom{m+1}{3}=\frac{c}{2}\cdot\frac{(m+1)m(m-1)}{6}=\frac{c}{12}(m^3-m)$. *(Expand the binomial: $(m+1)m(m-1)=m^3-m$.)*
7. Assembling: $[L_m,L_n]=(m-n)L_{m+n}+\frac{c}{12}(m^3-m)\delta_{m+n,0}$, exactly the Virasoro algebra. $\blacksquare$

So the central charge is *manufactured by the binomial $\binom{m+1}{3}$*, which is why it is cubic in $m$ — a fact that looked mysterious in CFT becomes a one-line binomial identity here.

#### Worked example with real numbers

For the central charge in step 6 with $m=2$: $\binom{3}{3}=1$ and $m^3-m=8-2=6$, so $\frac{c}{2}\cdot1=\frac{c}{12}\cdot6=\frac{c}{2}$. Consistent. For $m=1$: $\binom{2}{3}=0$ and $m^3-m=0$ — the central term vanishes for $m=\pm1,0$, which is why the subalgebra $\{L_{-1},L_0,L_1\}\cong\mathfrak{sl}_2$ is *anomaly-free* (it is the global conformal algebra of the [CFT guide](conformal-field-theory.md)).

#### Pitfall

The conformal vector $\omega$ is *extra data*, not automatic. The same vertex algebra can admit different $\omega$'s with different $c$'s (this is real and important — it changes the "energy" grading). A vertex algebra with no chosen $\omega$ has no central charge.

<a id="s5"></a>
### The Heisenberg (free boson) vertex algebra

#### What & why

This is the fundamental example — the algebraic free boson. Everything later (lattices, affine algebras, the Monster's pieces) is built from copies of it. We construct it by reconstruction, compute its OPE, find its conformal vector, and read off $c=1$.

#### The Heisenberg Lie algebra

> **Definition — Heisenberg algebra.** The (rank-1) **Heisenberg algebra** $\hat{\mathfrak{h}}$ has basis $\{a_n\}_{n\in\mathbb{Z}}$ and a central element $\mathbf{1}$, with brackets
> $$
> [a_m,a_n]=m\,\delta_{m+n,0}\,\mathbf{1},\qquad [a_m,\mathbf{1}]=0.
> $$
> The modes with $m>0$ are **annihilation**, $m<0$ **creation**, and $a_0$ is the central "momentum."

This is the canonical-commutation relation of an infinite set of oscillators (compare the harmonic oscillator $[a,a^\dagger]=1$; here the $n$ scales each one).

#### The Fock space and the field

> **Definition — Fock space.** Let $\mathbf{1}$ act as $1$ and let $|0\rangle$ be a vector with $a_n|0\rangle=0$ for $n\ge0$. The **Fock space** $V=\pi_0$ is spanned by
> $$
> a_{-n_1}a_{-n_2}\cdots a_{-n_k}|0\rangle,\qquad n_1\ge n_2\ge\cdots\ge n_k\ge1.
> $$
> Define the generating field $a(z)=\sum_{n\in\mathbb{Z}}a_n\,z^{-n-1}$.

By construction $a(z)$ is a field (annihilation modes kill $|0\rangle$), $a(z)|0\rangle=\sum_{n\le -1}a_n z^{-n-1}|0\rangle\in a_{-1}|0\rangle+zV[[z]]$, and with $T$ defined by $[T,a_n]=-n\,a_{n-1}$ (so $[T,a(z)]=\partial_z a(z)$) the field is translation-covariant. We must check **locality**.

#### The OPE of the current — derivation

**Claim.** $a(z)a(w)\sim\dfrac{1}{(z-w)^2}$, equivalently $(z-w)^2[a(z),a(w)]=0$ (locality with $N=2$).

*Derivation.*
1. Compute the commutator of fields: $[a(z),a(w)]=\sum_{m,n}[a_m,a_n]\,z^{-m-1}w^{-n-1}=\sum_{m,n}m\,\delta_{m+n,0}z^{-m-1}w^{-n-1}$. *(Substitute the Heisenberg bracket.)*
2. Set $n=-m$: $=\sum_{m}m\,z^{-m-1}w^{m-1}=\partial_w\Big(\sum_m z^{-m-1}w^{m}\Big)\cdot$ … carefully: $\sum_m m\,z^{-m-1}w^{m-1}=\partial_w\sum_m z^{-m-1}w^{m}=\partial_w\,\delta(z-w)$. *(Recognize the delta function $\delta(z-w)=\sum_m z^{-m-1}w^m$ from §s1 and differentiate in $w$.)*
3. So $[a(z),a(w)]=\partial_w\,\delta(z-w)$. *(Steps 1–2.)*
4. Multiply by $(z-w)^2$. Using the identity $(z-w)\partial_w\delta(z-w)=-\delta(z-w)$ from §s1, we get $(z-w)^2\partial_w\delta(z-w)=(z-w)\cdot(-\delta(z-w))=-(z-w)\delta(z-w)=0$, since $(z-w)\delta(z-w)=0$ (a basic delta identity: $(z-w)\sum_m z^{-m-1}w^m=\sum_m(z^{-m}w^m-z^{-m-1}w^{m+1})$ telescopes to $0$). *(Delta identities of §s1.)*
5. Therefore $(z-w)^2[a(z),a(w)]=0$: the field is local with $N=2$. *(Definition of locality.)* And the surviving singular term, by the commutator formula, is the double pole $1/(z-w)^2$ with coefficient $a_{(1)}a=\mathbf{1}=|0\rangle$. $\blacksquare$

By reconstruction (§s3) we now have a vertex algebra, the **Heisenberg vertex algebra** $\pi_0$. Its vertex operators are normal-ordered products of derivatives of $a(z)$, e.g.
$$
Y(a_{-1}a_{-1}|0\rangle,z)={:}a(z)a(z){:}\,,\qquad Y(a_{-2}|0\rangle,z)=\partial_z a(z).
$$

#### The conformal vector and $c=1$

> **Claim.** $\omega=\tfrac12\,a_{-1}a_{-1}|0\rangle$ is a conformal vector with central charge $c=1$. Its field is the **Sugawara-type** stress tensor $T(z)=\tfrac12{:}a(z)a(z){:}$.

*Derivation that $c=1$.*
1. Write $L_n=\omega_{(n+1)}=\tfrac12\sum_{k\in\mathbb{Z}}{:}a_k a_{n-k}{:}\,$, where normal ordering means $a_{\min}$ to the right. *(Expand the modes of $\tfrac12{:}aa{:}$.)*
2. Compute $[L_m,L_n]$ using $[a_m,a_n]=m\delta_{m+n,0}$. The leading term, by the standard oscillator computation (each $a$ contracted once), gives $(m-n)L_{m+n}$. *(Bilinear expansion; the $\delta$'s collapse the double sum.)*
3. The central term arises from the *double contraction* of all four oscillators, which is the normal-ordering "anomaly." Carrying out the reordering of $a_k a_{n-k}$ past $a_l a_{m-l}$ produces $\sum_{k>0}k(m-k)\delta_{m+n,0}$-type sums; regularized by normal ordering this evaluates to $\frac{1}{12}(m^3-m)\delta_{m+n,0}$ with coefficient $c=1$. *(The finite part of the reordering sum; the same computation as the CFT mode anomaly with a single boson.)*
4. Hence $[L_m,L_n]=(m-n)L_{m+n}+\frac{1}{12}(m^3-m)\delta_{m+n,0}$, i.e. $c=1$. $\blacksquare$

The numerical anchor: a *single* free boson carries central charge $c=1$. (We will see in §s6 that $d$ bosons give $c=d$.)

#### Pinning down the anomaly coefficient by hand

To make step 3 above non-hand-wavy, compute the central term directly for the smallest case. We want the number $A(m)$ defined by $[L_m,L_{-m}]=2mL_0+A(m)\cdot\mathrm{id}$ on the vacuum sector.
1. From $L_n=\tfrac12\sum_k {:}a_k a_{n-k}{:}$, expand $[L_m,L_{-m}]$ and apply it to $|0\rangle$. Only terms whose net mode is $0$ and which produce a pure number (all oscillators contracted) survive on $|0\rangle$ once we project onto the vacuum. *(Field condition: uncontracted annihilators kill $|0\rangle$.)*
2. The double contraction of the four oscillators in $L_m L_{-m}$, minus the reordered piece in $L_{-m}L_m$, leaves the finite sum
$$
A(m)=\frac12\sum_{k=1}^{m-1}k(m-k)\cdot 1=\frac12\sum_{k=1}^{m-1}k(m-k),
$$
each factor $k$ and $(m-k)$ coming from a commutator $[a_k,a_{-k}]=k$. *(Heisenberg bracket, counted once per contraction.)*
3. Evaluate the sum: $\sum_{k=1}^{m-1}k(m-k)=m\sum k-\sum k^2=m\cdot\frac{(m-1)m}{2}-\frac{(m-1)m(2m-1)}{6}=\frac{m(m-1)(m+1)}{6}=\frac{m^3-m}{6}$. *(Standard $\sum k$ and $\sum k^2$ formulas.)*
4. Hence $A(m)=\frac12\cdot\frac{m^3-m}{6}=\frac{m^3-m}{12}$, i.e. $\frac{c}{12}(m^3-m)$ with $c=1$. *(Match to the Virasoro form.)* For $m=2$: $A(2)=\frac{8-2}{12}=\frac12$, a clean rational number you can verify by hand from $[L_2,L_{-2}]$ directly. $\blacksquare$

#### Worked example with real numbers

The state $a_{-1}|0\rangle$ has $L_0$-weight $1$: indeed $L_0=\tfrac12\sum_k{:}a_k a_{-k}{:}=\tfrac12 a_0^2+\sum_{k\ge1}a_{-k}a_k$, so $L_0\,a_{-1}|0\rangle=\big(\sum_{k\ge1}a_{-k}a_k\big)a_{-1}|0\rangle=a_{-1}(a_1 a_{-1})|0\rangle=a_{-1}\cdot 1\cdot|0\rangle=a_{-1}|0\rangle$, using $[a_1,a_{-1}]=1$. Weight $=1$. Likewise $a_{-2}|0\rangle$ has weight $2$, and $a_{-1}a_{-1}|0\rangle$ has weight $2$. The dimensions of the weight spaces are the **partition numbers** $p(0)=1,p(1)=1,p(2)=2,\dots$ — our first hint of modular forms (§s10).

#### Pitfall

The vacuum is *not* annihilated by $a_0$ in general — extending to nonzero momentum $\alpha$ gives Fock modules $\pi_\alpha$ with $a_0=\alpha$, the building blocks of lattice algebras next. Confusing $\pi_0$ (vacuum module) with $\bigoplus_\alpha\pi_\alpha$ is a frequent slip.

<a id="s6"></a>
### Lattice vertex algebras and bosonization

#### What & why

The free boson alone is "structureless." Glue together infinitely many momentum sectors $\pi_\alpha$ labeled by a **lattice** of allowed momenta, and you get the richest elementary examples — **lattice vertex algebras** $V_L$ — including, for special lattices, the affine $\mathfrak{sl}_2$ at level 1 and (for the **Leech lattice**) a key ingredient of the Moonstrous Monster algebra. **Bosonization** is the technique of writing these new vertex operators as exponentials of the boson, $e^{\alpha\varphi(z)}$.

#### Lattices

> **Definition — even lattice.** A **lattice** $L$ is a free abelian group $\mathbb{Z}^d$ equipped with a symmetric integer-valued bilinear form $\langle\cdot,\cdot\rangle$. It is **even** if $\langle\alpha,\alpha\rangle\in2\mathbb{Z}$ for all $\alpha\in L$, and **positive-definite** if $\langle\alpha,\alpha\rangle>0$ for $\alpha\neq0$.

Evenness is exactly the condition that makes the construction below produce *commuting* (bosonic) vertex operators with integer-spaced singularities.

#### Construction

Take $d$ commuting copies of the Heisenberg algebra (one $a^i(z)$ per lattice direction, $[a^i_m,a^j_n]=m\delta^{ij}\delta_{m+n,0}$), giving central charge $c=d$. The total space is
$$
V_L=\bigoplus_{\alpha\in L}\pi_\alpha\otimes \mathbb{C}e^{\alpha},
$$
where $\pi_\alpha$ is the Fock module of momentum $\alpha$ and $e^\alpha$ is a formal symbol tracking the momentum sector. The new generating fields are the **vertex operators of momentum $\alpha$**:
$$
Y(e^\alpha,z)=e^{\alpha}\,z^{\alpha\cdot a_0}\,\exp\!\Big(\sum_{n<0}\frac{-\alpha\cdot a_n}{n}z^{-n}\Big)\exp\!\Big(\sum_{n>0}\frac{-\alpha\cdot a_n}{n}z^{-n}\Big),
$$
which is the exponential "$\,{:}e^{\alpha\varphi(z)}{:}\,$" with $\varphi(z)$ the formal boson whose derivative is $\partial\varphi=a$. (The operator $e^\alpha$ shifts momentum by $\alpha$; the factor $z^{\alpha\cdot a_0}$ supplies the fractional power $z^{\langle\alpha,\beta\rangle}$ when acting in sector $\beta$.)

#### The key OPE — why evenness matters

**Claim.** $Y(e^\alpha,z)\,Y(e^\beta,w)\sim (z-w)^{\langle\alpha,\beta\rangle}\,{:}e^{\alpha\varphi(z)}e^{\beta\varphi(w)}{:}\,$, with the prefactor $(z-w)^{\langle\alpha,\beta\rangle}$.

*Derivation idea.*
1. For exponentials of free fields, the **Baker–Campbell–Hausdorff / Wick** formula gives $e^{A}e^{B}=e^{B}e^{A}e^{[A,B]}$ when $[A,B]$ is central; here $A=\alpha\varphi(z)_-$, $B=\beta\varphi(w)_+$ contractions produce a $c$-number. *(BCH for free fields.)*
2. The single contraction $\langle\alpha\varphi(z)\,\beta\varphi(w)\rangle=\langle\alpha,\beta\rangle\log(z-w)$ exponentiates to the factor $\exp\big(\langle\alpha,\beta\rangle\log(z-w)\big)=(z-w)^{\langle\alpha,\beta\rangle}$. *(Free-boson propagator $\langle\varphi(z)\varphi(w)\rangle=\log(z-w)$, from $\partial\varphi\,\partial\varphi\sim(z-w)^{-2}$ integrated twice.)*
3. The exponent $\langle\alpha,\beta\rangle$ is an **integer** because $L$ is a lattice; locality (no branch cut) requires this to be an integer for all $\alpha,\beta$, and for the self-OPE $\langle\alpha,\alpha\rangle$ must be *even* so that $Y(e^\alpha,z)Y(e^\alpha,w)$ has the symmetry of a boson (sign $(-1)^{\langle\alpha,\alpha\rangle}=+1$). *(Evenness $\Leftrightarrow$ bosonic locality.)* A subtle sign — a **2-cocycle** $\varepsilon(\alpha,\beta)=\pm1$ — must be inserted to fix antisymmetric signs; this is the famous cocycle of lattice VOAs.
$\blacksquare$

#### Bosonization in one sentence

**Bosonization** is the statement that these exponential operators $e^{\pm\varphi}$ behave like *fermions or like extra currents* even though they are built from a single boson — a free fermion equals $\,{:}e^{\pm\varphi}{:}\,$ on the lattice $L=\mathbb{Z}$, and the $\mathfrak{sl}_2$ currents equal them on $L=\sqrt2\,\mathbb{Z}$ (the root lattice $A_1$). It trades a hard theory for a free boson.

#### Why the $z^{\alpha\cdot a_0}$ factor — and where conformal weight comes from

The factor $z^{\alpha\cdot a_0}$ is not cosmetic; it is what makes $Y(e^\alpha,z)$ a *field of definite weight*. Acting in momentum sector $\beta$, $a_0$ reads off $\beta$, so $z^{\alpha\cdot a_0}=z^{\langle\alpha,\beta\rangle}$, supplying exactly the fractional power that the OPE prefactor $(z-w)^{\langle\alpha,\beta\rangle}$ demands for consistency. The conformal weight of $e^\alpha$ under the boson stress tensor $T=\tfrac12{:}aa{:}$ is
$$
\Delta(e^\alpha)=\tfrac12\langle\alpha,\alpha\rangle,
$$
a positive integer when $L$ is even — *another* reason evenness is forced: half-integer weights would make $e^\alpha$ a fermion-like field, breaking the bosonic (integer-moded) structure of a vertex algebra. *Derivation of the weight.* Apply $L_0=\tfrac12 a_0^2+\sum_{n\ge1}a_{-n}a_n$ to the lowest state $e^\alpha|0\rangle$ of sector $\alpha$: the oscillator part annihilates it (no creation modes excited), and $\tfrac12 a_0^2$ gives $\tfrac12\langle\alpha,\alpha\rangle$. *(Definition of $L_0$ from §s5 plus $a_0 e^\alpha|0\rangle=\langle\alpha,\cdot\rangle$.)*

#### Worked example with real numbers — the $A_1$ root lattice

Let $L=\mathbb{Z}\alpha$ with $\langle\alpha,\alpha\rangle=2$ (the $A_1$ lattice). Then:
- The three fields $e^{\alpha}(z),\;e^{-\alpha}(z),\;\alpha\cdot a(z)$ have weight $1$ (compute: $L_0\,e^{\pm\alpha}|0\rangle=\tfrac12\langle\alpha,\alpha\rangle|\cdots\rangle=\tfrac12\cdot2=1$). Three weight-1 currents.
- Their OPEs reproduce the **affine $\widehat{\mathfrak{sl}_2}$ at level 1**: $e^{\alpha}(z)e^{-\alpha}(w)\sim\frac{1}{(z-w)^2}+\frac{\alpha\cdot a(w)}{z-w}$, with the $(z-w)^{\langle\alpha,-\alpha\rangle}=(z-w)^{-2}$ pole from the claim above. This is the **Frenkel–Kac construction** — affine algebras *built from a lattice boson*.

So a single even lattice produces a Kac–Moody current algebra, the subject of §s7.

#### Pitfall

Forgetting the **cocycle** $\varepsilon(\alpha,\beta)$ gives the wrong signs and a non-associative product. The cocycle is not optional; it is the price of turning the additive lattice into operators that multiply correctly.

<a id="s7"></a>
### Affine Kac–Moody vertex algebras and the Sugawara construction

#### What & why

Currents — weight-1 fields $J^a(z)$ valued in a Lie algebra $\mathfrak{g}$ — are the symmetry generators of a CFT (the [CFT guide](conformal-field-theory.md) and [Lie reps guide](../group-theory/lie-representations.md) introduce these). Their modes form an **affine Kac–Moody algebra** $\hat{\mathfrak{g}}$. The **Sugawara construction** then *manufactures the stress tensor $T(z)$ out of the currents themselves*, deriving Virasoro and the central charge from the current OPE — the cleanest illustration of "conformal symmetry hidden inside an algebra."

#### Affine Kac–Moody algebras, restated

From the [Lie reps guide](../group-theory/lie-representations.md): given a finite-dimensional simple Lie algebra $\mathfrak{g}$ with basis $\{t^a\}$, structure constants $[t^a,t^b]=\sum_c f^{ab}{}_c t^c$, and Killing form normalized so $\langle t^a,t^b\rangle=\delta^{ab}$, the **affine algebra** $\hat{\mathfrak g}$ has generators $t^a_n$ ($n\in\mathbb{Z}$) and central $K$, with
$$
[t^a_m,t^b_n]=\sum_c f^{ab}{}_c\,t^c_{m+n}+m\,k\,\delta^{ab}\delta_{m+n,0},
$$
where $k$ (the eigenvalue of $K$) is the **level**, a number measuring the central extension.

#### The current vertex algebra $V_k(\mathfrak g)$

Build the Fock-like space on a vacuum with $t^a_n|0\rangle=0$ for $n\ge0$, and set $J^a(z)=\sum_n t^a_n z^{-n-1}$. The current OPE encoding the bracket is
$$
J^a(z)J^b(w)\sim\frac{k\,\delta^{ab}}{(z-w)^2}+\sum_c\frac{f^{ab}{}_c\,J^c(w)}{z-w}.
$$
By reconstruction (§s3) — the currents are mutually local with $N=2$, exactly as one checks from this OPE using the delta identities of §s1 — this is the **affine vertex algebra** $V_k(\mathfrak g)$, central charge to be determined.

#### The Sugawara stress tensor

> **Definition — Sugawara construction.** Define
> $$
> T(z)=\frac{1}{2(k+h^\vee)}\sum_a {:}J^a(z)J^a(z){:}\,,
> $$
> where $h^\vee$ is the **dual Coxeter number** of $\mathfrak g$ (a positive integer attached to $\mathfrak g$; e.g. $h^\vee=N$ for $\mathfrak{sl}_N$, so $h^\vee=2$ for $\mathfrak{sl}_2$), provided $k+h^\vee\neq0$.

> **Theorem (Sugawara).** This $T(z)$ is a conformal vector with central charge
> $$
> c=\frac{k\,\dim\mathfrak g}{k+h^\vee},
> $$
> the currents $J^a$ are primaries of weight $1$ under it, and the modes $L_n$ satisfy Virasoro.

#### Derivation of Virasoro and $c$ from the currents

*Sketch with the key steps and reasons.*
1. **Why the normalization $\tfrac1{2(k+h^\vee)}$.** Demand that $J^a$ be primary of weight 1, i.e. $T(z)J^a(w)\sim\frac{J^a(w)}{(z-w)^2}+\frac{\partial J^a(w)}{z-w}$. Computing $T(z)J^a(w)$ by Wick-contracting one $J$ in $T$ with the external $J^a$ produces two contractions: one through the central term $k\delta$, one through the structure constants $f$, which combine via the identity $\sum_{b,c}f^{ab}{}_c f^{cb}{}_d=-2h^\vee\delta^a_d$ (definition of $h^\vee$ via the quadratic Casimir in the adjoint). *(Casimir identity from [Lie reps](../group-theory/lie-representations.md).)*
2. Summing the two contributions gives a coefficient $\frac{2k+2h^\vee}{2(k+h^\vee)}=1$ in front of $\frac{J^a}{(z-w)^2}$ — *this* is why the denominator must be $k+h^\vee$. *(Forcing the primary condition.)* If $k+h^\vee=0$ ("critical level") the construction fails — a famous fact tied to geometric Langlands (§s11).
3. **The central charge.** Compute $T(z)T(w)$ by Wick contractions of the quartic $\,{:}JJ{:}\,{:}JJ{:}$. The most singular, quartic-pole term has coefficient $\frac{1}{(z-w)^4}$ times $\frac{c}{2}$, where the combinatorics of double-contracting all currents yields
$$
\frac{c}{2}=\frac{1}{2}\cdot\frac{k\dim\mathfrak g}{k+h^\vee}\quad\Rightarrow\quad c=\frac{k\dim\mathfrak g}{k+h^\vee}.
$$
*(Counting the $\dim\mathfrak g$ ways to fully contract two currents against two, each giving a factor $k$, normalized by $[2(k+h^\vee)]^2$ and using the Casimir to reduce one $k$ to $k+h^\vee$.)*
4. The remaining poles reproduce $\frac{2T(w)}{(z-w)^2}+\frac{\partial T(w)}{z-w}$, so $T$ obeys the $TT$ OPE and hence (by §s4's derivation) the Virasoro algebra with this $c$. $\blacksquare$

#### Worked example with real numbers — $\widehat{\mathfrak{sl}_2}$ at level $1$

Here $\dim\mathfrak{sl}_2=3$, $h^\vee=2$, $k=1$, so
$$
c=\frac{1\cdot3}{1+2}=\frac{3}{3}=1.
$$
This matches §s6: the $A_1$ lattice boson had $c=1$ and produced exactly $\widehat{\mathfrak{sl}_2}$ at level 1. Two completely different constructions — Sugawara from currents, Frenkel–Kac from a lattice — agree to the number $c=1$. For level $k$ general, $c=\frac{3k}{k+2}$; e.g. $k=2$ gives $c=\frac{6}{4}=\frac32$, the central charge appearing in the parafermion / Ising-times-free-boson story.

#### The dual Coxeter number, concretely

Because $h^\vee$ controls everything, here is how to read it off. For a simple Lie algebra $\mathfrak g$ the **dual Coxeter number** $h^\vee$ is defined by the adjoint Casimir: $\sum_{b,c}f^{ab}{}_c f^{db}{}_c=2h^\vee\,\delta^{ad}$ (the adjoint representation's quadratic Casimir equals $2h^\vee$ in the normalization $\langle t^a,t^b\rangle=\delta^{ab}$). The values for the classical series (from the [Lie reps guide](../group-theory/lie-representations.md)) are: $h^\vee=N$ for $\mathfrak{sl}_N$ ($A_{N-1}$), $h^\vee=2N-1$ for $\mathfrak{so}_{2N+1}$ ($B_N$), $h^\vee=N+1$ for $\mathfrak{sp}_{2N}$ ($C_N$), $h^\vee=2N-2$ for $\mathfrak{so}_{2N}$ ($D_N$); and the exceptional values $h^\vee=12,18,30$ for $E_6,E_7,E_8$. As a check, $\mathfrak{sl}_2$ has $h^\vee=2$, matching our worked example. As the level $k\to\infty$, $c=\frac{k\dim\mathfrak g}{k+h^\vee}\to\dim\mathfrak g$, the classical count of one boson per generator — the quantum correction $h^\vee$ becomes negligible at large level, exactly as one expects of an anomaly.

#### Pitfall

The shift $k\mapsto k+h^\vee$ is *quantum*: classically (think of currents as commuting) one would write $c=\dim\mathfrak g$, but normal ordering injects the $h^\vee$. Omitting $h^\vee$ is the single most common error in Sugawara computations. The denominator also warns of the **critical level** $k=-h^\vee$, where $c\to\infty$ and the Sugawara $T$ ceases to exist — a singularity that, far from pathological, is the doorway to geometric Langlands (§s11).

## Part D · Representation theory, modularity, and Moonshine

<a id="s8"></a>
### Modules over a vertex algebra; rationality

#### What & why

A vertex algebra is the algebra of *symmetries*; its **modules** are the spaces those symmetries act on — the "sectors" or "primary fields" of the CFT. The good vertex algebras, the **rational** ones, have only finitely many irreducible modules, which is what makes a CFT solvable and its characters modular (§s10).

#### Definition of a module

> **Definition — module.** A **module** over a vertex algebra $V$ is a vector space $M$ together with a state–field map $Y_M(\cdot,z):V\to(\mathrm{End}M)[[z,z^{-1}]]$, $Y_M(A,z)=\sum_n A^M_{(n)}z^{-n-1}$, such that:
> 1. $Y_M(|0\rangle,z)=\mathrm{id}_M$;
> 2. each $Y_M(A,z)$ is a field on $M$;
> 3. the **Borcherds identity** holds for the $Y_M$-products with one factor in $M$ — i.e. the same master identity of §s2 but with $C\in M$.

In words: $M$ carries an action of *all* the vertex operators, compatibly with their mutual products. The vertex algebra $V$ is itself the **adjoint module** (the "vacuum sector").

For a conformal $V$, a module is graded by $L_0$-eigenvalue: $M=\bigoplus_{\Delta} M_\Delta$, with the smallest $\Delta$ the **conformal weight** of the module (the [CFT guide](conformal-field-theory.md)'s primary weight $h$). The lowest-weight vectors are the **primary states** of that sector; the rest are **descendants**, obtained by acting with creation modes $L_{-n}$ and (for an affine algebra) $t^a_{-n}$, exactly mirroring the Verma-module construction of the [CFT guide](conformal-field-theory.md). A module is **irreducible** if it has no proper nonzero submodule closed under all vertex operators — physically, a single irreducible "tower" built on one primary.

There is also a notion of **intertwining operator** (the [CFT guide](conformal-field-theory.md)'s fusion of primaries): a field $\mathcal{Y}(\cdot,z)$ taking a state of one module to maps between two others, $\mathcal{Y}:M^1\to\mathrm{Hom}(M^2,M^3)[[z^{\pm}]]z^{\Delta}$. The dimensions of the spaces of these are the **fusion rules** $N_{ij}^k$, the integers counting how module $M^i$ and $M^j$ combine to produce $M^k$. Their consistency with modularity is the celebrated **Verlinde formula**, $N_{ij}^k=\sum_l \frac{S_{il}S_{jl}\overline{S_{kl}}}{S_{0l}}$, which computes fusion from the $S$-matrix of §s10 — one of the most striking outputs of the whole theory.

#### Rationality

> **Definition — rational vertex algebra (working version).** A conformal vertex algebra is **rational** if every module is completely reducible (a direct sum of irreducibles) and there are only **finitely many** isomorphism classes of irreducible modules. A closely related finiteness, **$C_2$-cofiniteness** (the space $V/C_2(V)$ is finite-dimensional, where $C_2(V)=\mathrm{span}\{A_{(-2)}B\}$), is the technical hypothesis under which the modularity theorem of §s10 is proved.

Rationality is the algebraic meaning of "the CFT has a finite, well-behaved spectrum." Lattice VOAs $V_L$ for $L$ even positive-definite, and affine $V_k(\mathfrak g)$ at positive *integer* level $k$, are rational; the bare Heisenberg algebra is *not* (it has a continuum of Fock modules $\pi_\alpha$).

#### Worked example with real numbers — modules of $\widehat{\mathfrak{sl}_2}$ at level $k=1$

At level 1, $\widehat{\mathfrak{sl}_2}$ has exactly **two** irreducible modules: the vacuum module ($\mathfrak{sl}_2$-spin $0$, weight $0$) and the spin-$\tfrac12$ module (weight $h=\frac{j(j+1)}{k+2}=\frac{\frac12\cdot\frac32}{3}=\frac{3/4}{3}=\frac14$). Two modules, weights $0$ and $\frac14$ — a finite list, confirming rationality, and these two weights will become the two characters of §s10.

#### Pitfall

"Module of a vertex algebra" is more rigid than "representation of its mode Lie algebra": a module must respect *all* the $n$-th products, not just the commutators. Many representations of the affine Lie algebra are *not* admissible vertex-algebra modules (e.g. wrong level, or non-integrable), and rationality fails outside positive integer level.

<a id="s9"></a>
### Zhu's associative algebra and the classification of modules

#### What & why

Counting and classifying vertex-algebra modules looks hard — they are infinite-dimensional, graded by energy. **Zhu's algebra** is a brilliant reduction: it manufactures from the infinite-dimensional $V$ a single *ordinary associative algebra* $A(V)$ whose representations correspond to (lowest-weight pieces of) $V$-modules. Module theory collapses to ordinary algebra.

#### The construction (overview)

> **Definition — Zhu's algebra.** On a conformal vertex algebra $V$, define two bilinear operations using shifted modes:
> $$
> A*B=\mathrm{Res}_z\,Y(A,z)\frac{(1+z)^{\Delta_A}}{z}\,B,\qquad
> A\circ B=\mathrm{Res}_z\,Y(A,z)\frac{(1+z)^{\Delta_A}}{z^2}\,B,
> $$
> for $A$ of weight $\Delta_A$ (extended linearly). Let $O(V)=\mathrm{span}\{A\circ B\}$ and define
> $$
> A(V)=V/O(V),
> $$
> with multiplication induced by $*$. Then $A(V)$ is an **associative algebra** with unit $|0\rangle+O(V)$.

The "$\,*\,$" product is a cleverly weighted residue that survives passing to the quotient by $O(V)$; proving $*$ is associative on $A(V)$ is Zhu's theorem (a substantial mode computation we do not reproduce, but the shape is: $O(V)$ is exactly the ideal that kills non-associativity and projects onto the **zero modes** $A_{(\Delta_A-1)}$ acting on lowest-weight states).

#### The classification theorem

> **Theorem (Zhu).** There is a bijection
> $$
> \{\text{irreducible }\mathbb{Z}_{\ge0}\text{-graded }V\text{-modules}\}\;\longleftrightarrow\;\{\text{irreducible }A(V)\text{-modules}\}
> $$
> sending a $V$-module $M=\bigoplus_\Delta M_\Delta$ to its **lowest-weight space** $M_{\Delta_{\min}}$, on which the zero modes $o(A)=A_{(\Delta_A-1)}$ act and realize the $A(V)$-action.

So: classify the modules of *one finite-dimensional-ish associative algebra* $A(V)$, and you have classified all the (graded) modules of the vertex algebra. In particular, $V$ is rational and $C_2$-cofinite only if $A(V)$ is a finite-dimensional semisimple algebra.

#### Worked example with real numbers

For the Virasoro vertex algebra at central charge $c$, Zhu's algebra is a *polynomial ring* $A(V)\cong\mathbb{C}[x]$ where $x$ corresponds to $\omega$ and acts as $L_0$ on the lowest-weight state — so its irreducible modules are points $x=h$, i.e. highest-weight Virasoro reps of weight $h$. For a **minimal model** (the [CFT guide](conformal-field-theory.md)'s $c<1$ rational theories), $O(V)$ contains the null-vector relation, which *factors* the polynomial: $A(V)=\mathbb{C}[x]/p(x)$ with $p$ having exactly the finitely many roots $h_{r,s}$. For the Ising model $c=\tfrac12$, $p$ has three roots $h\in\{0,\tfrac1{16},\tfrac12\}$ — recovering the three primaries by pure algebra. Three modules, finite, rational.

#### Why the weighted residue — intuition

The strange factors $(1+z)^{\Delta_A}$ are a change of coordinate from the plane to the cylinder (equivalently, the torus's time circle). Under the exponential map $z\mapsto\log(1+z)$ a weight-$\Delta_A$ field picks up the Jacobian $(1+z)^{\Delta_A}$; the residue then extracts the **zero mode** $o(A)=A_{(\Delta_A-1)}$, the only mode that preserves the energy grading and hence acts on a fixed weight space. So Zhu's product $A*B$ is, conceptually, "compose zero modes on the lowest-weight space," and $O(V)$ is exactly the kernel of the map $V\to\mathrm{End}(M_{\Delta_{\min}})$. This is why $A(V)$-modules and lowest-weight spaces of $V$-modules coincide: both are "what the zero modes do."

#### Pitfall

Zhu's algebra sees only the **lowest-weight space** and the **zero modes**; it forgets the higher descendants. It classifies modules but does not by itself give their full character — for that we need §s10. Also, $A(V)$ can be infinite-dimensional (e.g. Heisenberg, free boson) precisely when $V$ is *not* rational.

<a id="s10"></a>
### Characters and modular invariance (Zhu's theorem)

#### What & why

The **character** of a module records the dimensions of its energy levels in one generating function. The miracle — **Zhu's modularity theorem** — is that for a rational, $C_2$-cofinite vertex algebra these characters are **modular forms**: they transform nicely under $\tau\mapsto-1/\tau$ and $\tau\mapsto\tau+1$. This is the deep link between vertex algebras and number theory, and the precise reason 2D CFT partition functions are modular invariant (the torus story of the [CFT guide](conformal-field-theory.md)).

#### The character

> **Definition — character.** For a module $M=\bigoplus_\Delta M_\Delta$ of a conformal $V$ with central charge $c$, the **character** (or **graded dimension**) is
> $$
> \chi_M(\tau)=\mathrm{tr}_M\,q^{\,L_0-c/24}=q^{\,\Delta_{\min}-c/24}\sum_{n\ge0}(\dim M_{\Delta_{\min}+n})\,q^{n},\qquad q=e^{2\pi i\tau},
> $$
> with $\tau$ in the upper half-plane ($\mathrm{Im}\tau>0$, so $|q|<1$ and the series converges). The shift $-c/24$ is the **Casimir/Virasoro shift**; it is exactly what makes the character modular.

The variable $\tau$ is the **modular parameter** of a torus (a [Complex Analysis](../complex-analysis/complex-analysis.md) object): the torus is $\mathbb{C}/(\mathbb{Z}+\tau\mathbb{Z})$, and $\mathrm{tr}\,q^{L_0-c/24}$ is the **partition function** of the CFT on that torus.

#### The modular group

The two transformations
$$
S:\tau\mapsto-\frac1\tau,\qquad T:\tau\mapsto\tau+1,
$$
generate $SL(2,\mathbb{Z})$, the **modular group** (they describe the two ways to cut and reglue a torus without changing it). A function modular under them is a **modular form** (see [Special Functions](special-functions.md) for the theta and eta functions that appear).

#### Zhu's theorem

> **Theorem (Zhu, modular invariance).** Let $V$ be rational and $C_2$-cofinite with irreducible modules $M_1,\dots,M_r$. Then:
> 1. each character $\chi_{M_i}(\tau)$ converges to a holomorphic function on the upper half-plane;
> 2. the span $\{\chi_{M_1},\dots,\chi_{M_r}\}$ is **invariant under $SL(2,\mathbb{Z})$**: there are constant matrices $S_{ij},T_{ij}$ with
> $$
> \chi_{M_i}(-1/\tau)=\sum_j S_{ij}\,\chi_{M_j}(\tau),\qquad \chi_{M_i}(\tau+1)=\sum_j T_{ij}\,\chi_{M_j}(\tau).
> $$
> The matrix $T$ is diagonal with entries $e^{2\pi i(\Delta_i-c/24)}$; $S$ is symmetric and unitary.

In one line: **the characters of a rational VOA form a finite-dimensional representation of $SL(2,\mathbb{Z})$.** This is why CFT partition functions can be made modular invariant — one combines $|\chi_i|^2$ so that the $S,T$ action cancels.

#### Why the $-c/24$ shift makes things modular — the mechanism

The shift is not a convention chosen for prettiness; it is *forced* by the geometry of the torus. The partition function on the torus $\mathbb{C}/(\mathbb{Z}+\tau\mathbb{Z})$ is a trace over the Hilbert space weighted by the operator $q^{L_0-c/24}\bar q^{\bar L_0-c/24}$ that implements "propagate once around the time cycle." The $-c/24$ is the **Casimir energy** of the vacuum on a circle — the regularized sum $\frac12\sum_{n\ge1} n=-\frac1{24}$ (zeta-regularized $\zeta(-1)=-\tfrac1{12}$, halved) per unit central charge. Without it, $L_0$ alone is not the correct generator of the modular $T:\tau\mapsto\tau+1$, and the trace fails to transform. With it, $T$ acts diagonally by the phase $e^{2\pi i(\Delta-c/24)}$, which is exactly the $T$-matrix of the theorem. So the abstract anomaly $c$ of §s4 reappears as the ground-state energy that tunes modularity.

#### Worked example with real numbers — the free boson and the $\eta$ function

For the Heisenberg algebra $c=1$, the vacuum character is
$$
\chi_{\pi_0}(\tau)=q^{-1/24}\sum_{n\ge0}p(n)\,q^{n}=q^{-1/24}\prod_{m\ge1}\frac1{1-q^m}=\frac{1}{\eta(\tau)},
$$
where $p(n)$ are the partition numbers (counted in §s5) and $\eta(\tau)=q^{1/24}\prod_{m\ge1}(1-q^m)$ is the **Dedekind eta function** (see [Special Functions](special-functions.md)). Since $\eta(-1/\tau)=\sqrt{-i\tau}\,\eta(\tau)$, the character $1/\eta$ is modular of weight $-\tfrac12$ — the $-c/24=-1/24$ shift was precisely the exponent of $q$ needed for this. The mysterious $1/24$ of string theory is the algebraic $c/24$.

#### Worked example — $\widehat{\mathfrak{sl}_2}$ level 1 (two characters)

The two modules (weights $0$ and $\frac14$, §s8) have characters that are ratios of theta functions, $\chi_0=\Theta_{0}/\eta$ and $\chi_{1/2}=\Theta_{1}/\eta$. Under $S$ they mix by the $2\times2$ matrix
$$
S=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},
$$
and one checks $S^2=\mathrm{id}$ (since $\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}1&1\\1&-1\end{pmatrix}=\frac12\begin{pmatrix}2&0\\0&2\end{pmatrix}=\mathrm{id}$), consistent with the modular relation $S^2=\mathrm{id}$ in $PSL(2,\mathbb{Z})$. The modular-invariant combination $|\chi_0|^2+|\chi_{1/2}|^2$ is the partition function. This is a finite-dimensional $SL(2,\mathbb{Z})$ representation, exactly as the theorem promises.

#### Pitfall

Without $C_2$-cofiniteness the characters can fail to be modular (the Heisenberg algebra is borderline: $1/\eta$ is *almost* modular but only because of the special $c=1$). Logarithmic CFTs (non-semisimple module categories) need quasi-modular / vector-valued generalizations. Modularity is a theorem *with hypotheses*, not a universal law.

<a id="s11"></a>
### The Monster, Monstrous Moonshine, and geometric Langlands

#### What & why

We end with the two summits that vertex algebras were, in part, invented to reach. **Monstrous Moonshine** connects the largest sporadic finite simple group — the **Monster** — to modular functions, and the bridge *is* a particular vertex operator algebra. **Geometric Langlands** is a vast geometric program in which vertex algebras at the critical level play a starring role. Both show the structure of §s0–s10 is not a formalism but a discovery engine.

#### The Monster and the $j$-function

The **Monster group** $\mathbb{M}$ is the largest of the 26 sporadic finite simple groups, of order roughly $8\times10^{53}$. The **$j$-function** is the fundamental modular function (see [Special Functions](special-functions.md)):
$$
j(\tau)=\frac1q+744+196884\,q+21493760\,q^2+\cdots,\qquad q=e^{2\pi i\tau},
$$
the unique (up to constant) $SL(2,\mathbb{Z})$-invariant holomorphic function on the upper half-plane with a simple pole at $q=0$. **McKay's observation (1978):** the coefficient $196884=196883+1$, and $196883$ is the dimension of the smallest nontrivial irreducible representation of the Monster. The next coefficient $21493760=21296876+196883+1$ also decomposes into Monster representation dimensions. Coincidence seemed impossible — Conway and Norton called it **Monstrous Moonshine**.

#### The Moonshine module — a vertex operator algebra

> **Theorem (Frenkel–Lepowsky–Meurman; Borcherds).** There is a vertex operator algebra $V^\natural$, the **Moonshine module**, with central charge $c=24$, such that:
> 1. its automorphism group is exactly the Monster $\mathbb{M}$;
> 2. its graded dimension is $\sum_n(\dim V^\natural_n)q^{n-1}=j(\tau)-744$;
> 3. for each Monster element $g$, the graded **trace** (a "twisted character") $T_g(\tau)=\sum_n\mathrm{tr}(g\,|\,V^\natural_n)q^{n-1}$ is a special modular function — a **Hauptmodul** — as Conway and Norton conjectured.

*How it is built (in our language).* $V^\natural$ is constructed from the **Leech lattice** $\Lambda$ (the unique even self-dual rank-24 lattice with no vectors of squared length 2): take the lattice VOA $V_\Lambda$ of §s6 (central charge $c=24$), then form a $\mathbb{Z}_2$-**orbifold** — keep the part invariant under the lattice symmetry $\alpha\mapsto-\alpha$ and adjoin a "twisted module." The Monster emerges as the symmetry group of this orbifold VOA. So the Monster is, literally, the automorphism group of a particular chiral algebra — the §s2 axioms applied to one extraordinary example. Borcherds proved the full Moonshine conjectures by inventing **generalized Kac–Moody (Borcherds) algebras** and a "no-ghost" argument tying $V^\natural$ to a Lie algebra whose denominator identity forces the $T_g$ to be Hauptmoduls — work for which he received the Fields Medal in 1998.

#### Why the Leech lattice, and why $c=24$

Two numerical facts make $V^\natural$ work, and both are checkable. First, $c=24$: the Leech lattice has rank $24$, so the lattice VOA $V_\Lambda$ has $24$ free bosons and central charge $c=24$ (§s5, $c=d$). Second, the *absence of weight-1 currents*: ordinarily a lattice VOA has extra weight-1 fields from vectors $\alpha$ with $\langle\alpha,\alpha\rangle=2$ (recall $\Delta(e^\alpha)=\tfrac12\langle\alpha,\alpha\rangle=1$, §s6). The Leech lattice is the unique even self-dual rank-24 lattice with **no** such vectors, so $V_\Lambda$ has no unwanted currents; the $\mathbb{Z}_2$-orbifold then removes the remaining $24$ bosonic currents $a^i$, leaving a VOA whose weight-1 space is *empty*. A VOA with $c=24$ and no weight-1 states has an automorphism group that is a finite group rather than a continuous one — room for the Monster.

#### Worked example with real numbers

The first nontrivial graded dimension: $\dim V^\natural_2=196884$, and item 2 says the $q^1$ coefficient of $j-744$ is $196884$ — matching the $j$-function above exactly. Item 1 then forces $196884=196883+1$ to be a sum of Monster representation dimensions (the trivial rep, dimension 1, plus the 196883), which is McKay's observation *derived* rather than observed. As a second check, the next level: $\dim V^\natural_3=21493760=21296876+196883+1$, again a sum of Monster irreducible dimensions (the $21296876$-dimensional irrep, plus the $196883$, plus the trivial), matching the $j$-function's $q^2$ coefficient $21493760$. The vertex algebra explains the coincidences.

#### A word on geometric Langlands

Recall from §s7 that the Sugawara construction *fails* at the **critical level** $k=-h^\vee$, where $k+h^\vee=0$. Far from a defect, this is the gateway to deep geometry: at the critical level the affine vertex algebra $V_{-h^\vee}(\mathfrak g)$ has an enormous **center** — its center is the algebra of functions on the space of "**opers**," a moduli space attached to the Langlands-dual group $\mathfrak g^\vee$ (a result of Feigin–Frenkel). The **geometric Langlands correspondence** seeks an equivalence between sheaves on the moduli of $\mathfrak g$-bundles on a curve and sheaves on the moduli of $\mathfrak g^\vee$-local systems; vertex algebras at the critical level provide the local building blocks of one side, with the Feigin–Frenkel center realizing the Langlands dual on the nose. In short: the very value of $k$ that breaks Sugawara is where the richest mathematics begins, and vertex algebras are the local language of that mathematics.

#### Pitfall

Moonshine is *not* unique to the Monster: **umbral** and **Mathieu moonshine** attach other finite groups to other (mock) modular forms, again through vertex-algebra-like structures. The lesson is structural, not coincidental — finite symmetry plus chiral algebra plus modularity repeatedly produces deep number theory.

---

*This guide built vertex operator algebras from the physical OPE up to the Monster. We turned the singular product of conformal fields into formal distributions and normal ordering, then into the four axioms of a vertex algebra — state–field correspondence, vacuum, translation, and locality — whose master form is the Borcherds identity. The reconstruction theorem let us build vertex operators from a handful of generating fields, and a conformal vector $\omega$ added the Virasoro algebra and the central charge $c$, manufactured by the binomial $\binom{m+1}{3}=\tfrac16(m^3-m)$. We worked the free boson ($c=1$) by hand, glued momentum sectors into lattice algebras and bosonized them, and derived Virasoro from currents by the Sugawara construction with its quantum shift $k\mapsto k+h^\vee$ and central charge $c=k\dim\mathfrak g/(k+h^\vee)$. Modules, rationality, and Zhu's associative algebra collapsed the representation theory to ordinary algebra; Zhu's modularity theorem made the characters into a finite $SL(2,\mathbb{Z})$ representation, the rigorous source of the partition function's modular invariance and of the Dedekind $\eta$ and $j$ functions. Finally the Moonshine module $V^\natural$ revealed the Monster as the automorphism group of one $c=24$ chiral algebra, and the critical level $k=-h^\vee$ opened onto geometric Langlands. The single thread: a vertex algebra is the rigorous algebra of two-dimensional conformal symmetry, and once made rigorous, that algebra turns out to encode some of the deepest objects in modern mathematics.*
