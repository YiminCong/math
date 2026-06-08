**English** · [中文](symplectic-geometry.zh.md)

# Symplectic Geometry & Geometric Quantization, *the geometry of phase space.*

*A self-contained, rigorous account of the geometry hidden inside classical mechanics, and of how that geometry turns into quantum mechanics. We begin with the bare algebra of a symplectic form — an antisymmetric, nondegenerate pairing — and build, step by step, to symplectic manifolds, the cotangent bundle as the natural arena of Hamiltonian dynamics, Poisson brackets, symmetries and reduction, and finally the program of geometric quantization that constructs a Hilbert space from a classical phase space. Geometry is the goal and physics is the motivation; every formula is derived and every symbol is explained.*

[← Back to all guides](../README.md)

**Prerequisites.** This guide assumes the **Differential Geometry & Tensors** guide (smooth manifolds, tangent and cotangent spaces, vector fields, differential forms, the exterior derivative $d$, the wedge product $\wedge$, the interior product $\iota_X$, the Lie derivative $\mathcal{L}_X$, and Cartan's magic formula $\mathcal{L}_X = d\,\iota_X + \iota_X\, d$) and the **Calculus of Variations** guide (the action functional, the Euler–Lagrange equations, and the Legendre transform passing from a Lagrangian $L(q,\dot q)$ to a Hamiltonian $H(q,p)$). We restate each specific fact at the moment we use it.

## Part A · The linear and smooth theory

<a id="s0"></a>
### Motivation — Hamiltonian mechanics is differential geometry on phase space

Symplectic geometry is the mathematics of *phase space*: the space whose points are the complete instantaneous states of a mechanical system. The motivating claim of this guide is that the rules of Hamiltonian mechanics are not a collection of formulas to be memorized but the unfolding of a single geometric object — a closed, nondegenerate $2$-form $\omega$ — and that quantum mechanics can be built on top of that same object.

#### What problem are we solving?

In elementary mechanics the state of a particle in one dimension is a pair: its position $q$ and its momentum $p$. The pair $(q,p)$ is a point of a two-dimensional space we call **phase space**. Hamilton's equations of motion read

$$
\dot q = \frac{\partial H}{\partial p},\qquad \dot p = -\frac{\partial H}{\partial q},
$$

where $H(q,p)$ is the **Hamiltonian**, the total energy expressed in terms of position and momentum, and a dot denotes the time derivative. These two equations have a striking asymmetry: a plus sign on one and a minus sign on the other. That antisymmetry is the fingerprint of a $2$-form. The whole content of Hamiltonian mechanics is captured by saying: *there is an antisymmetric pairing $\omega = dq\wedge dp$ on phase space, and the motion is the flow of the vector field $X_H$ defined by $\iota_{X_H}\omega = dH$.* The minus sign is forced by the antisymmetry of $\omega$.

Two structural facts make this worth a whole geometry:

1. **The pairing is antisymmetric, not symmetric.** A metric (inner product) is a *symmetric* nondegenerate bilinear form; it measures lengths and angles. A symplectic form is an *antisymmetric* nondegenerate bilinear form; it measures *oriented area* in the $(q,p)$-plane. Lengths play no role in mechanics — only areas (actions) do.
2. **The pairing is closed.** The condition $d\omega = 0$ is exactly what makes the flow preserve $\omega$ and what forces the Poisson bracket to satisfy the Jacobi identity. Closedness is the geometric encoding of "energy conservation is consistent."

#### The plan

We build, in order: **symplectic vector spaces** (the linear algebra, s1); **symplectic manifolds** and **Darboux's theorem** that they all look standard locally (s2); the **cotangent bundle** $T^*Q$ as the canonical phase space with its **tautological** and **canonical** forms (s3); **Hamiltonian vector fields** and the **Poisson bracket**, with a proof of the Jacobi identity from $d\omega=0$ (s4); **symplectomorphisms** and canonical transformations (s5); **moment maps**, the geometric Noether theorem, and **Marsden–Weinstein reduction** (s6); **Lagrangian submanifolds** (s7); **almost-complex and Kähler structures** bridging to complex geometry (s8); **prequantization** (s9); **geometric quantization** proper (s10); and a fully **worked example** quantizing the harmonic oscillator and the $2$-sphere (s11).

> **Intuition.** A metric tells you how far apart two states are. A symplectic form tells you how two states *trade*: how a displacement in position pairs with a displacement in momentum to produce a number (an area). Mechanics is the geometry of that trade.

<a id="s1"></a>
### Symplectic vector spaces; the standard symplectic form; symplectic versus inner-product structure

Before manifolds we need the pointwise linear algebra. A symplectic structure on a manifold is, at each point, a symplectic structure on the tangent space — so we first understand one vector space.

#### Definition and the nondegeneracy condition

> **Definition — symplectic vector space.**
>
> Let $V$ be a finite-dimensional real vector space. A **symplectic form** on $V$ is a map $\omega: V\times V\to\mathbb{R}$ that is
> - **bilinear**: linear in each argument separately;
> - **antisymmetric** (also called **alternating** or **skew**): $\omega(u,v) = -\,\omega(v,u)$ for all $u,v\in V$ (equivalently $\omega(v,v)=0$);
> - **nondegenerate**: if $\omega(u,v)=0$ for *all* $v\in V$, then $u=0$.
>
> The pair $(V,\omega)$ is a **symplectic vector space**.

Here "bilinear" means $\omega(au+bw,v)=a\,\omega(u,v)+b\,\omega(w,v)$ and likewise in the second slot, for scalars $a,b\in\mathbb{R}$. "Nondegenerate" says no nonzero vector is invisible to the pairing: the linear map $\flat:V\to V^*$, $u\mapsto \omega(u,\cdot)$ (sending $u$ to the covector $v\mapsto\omega(u,v)$), has trivial kernel and is therefore an isomorphism, since $V$ and its dual $V^*$ have equal dimension.

#### Symplectic forms force even dimension

> **Proposition.** A symplectic vector space has even dimension.

**Proof.**
1. Choose any basis of $V$ and let $A$ be the matrix with entries $A_{ij}=\omega(e_i,e_j)$, where $\{e_i\}$ is that basis. *Reason:* a bilinear form is determined by its values on a basis, and these values assemble into a matrix.
2. Antisymmetry $\omega(e_i,e_j)=-\omega(e_j,e_i)$ gives $A^{\mathsf T}=-A$, i.e. $A$ is a skew-symmetric matrix. *Reason:* transposing swaps the roles of $i$ and $j$.
3. For an $n\times n$ matrix, $\det(A^{\mathsf T})=\det(A)$ always, and $\det(-A)=(-1)^n\det(A)$ by pulling the scalar $-1$ out of each of the $n$ columns. *Reason:* the determinant is multilinear in columns and unchanged by transpose.
4. Combining steps 2–3: $\det(A)=\det(A^{\mathsf T})=\det(-A)=(-1)^n\det(A)$, so $\big(1-(-1)^n\big)\det(A)=0$.
5. Nondegeneracy forces $\det(A)\ne 0$: if $\det A=0$ there is a nonzero vector $u$ with $A u = 0$, meaning $\omega(u,e_j)=0$ for all $j$, hence $\omega(u,v)=0$ for all $v$ by bilinearity, contradicting nondegeneracy. *Reason:* a singular matrix has nontrivial kernel.
6. With $\det(A)\ne 0$, step 4 forces $1-(-1)^n=0$, so $(-1)^n=1$, so $n$ is even. $\blacksquare$

We write $\dim V = 2n$.

#### The standard symplectic form and the symplectic basis

> **Definition — standard symplectic form on $\mathbb{R}^{2n}$.**
>
> On $\mathbb{R}^{2n}$ with coordinates $(q^1,\dots,q^n,p_1,\dots,p_n)$, the **standard symplectic form** is
> $$
> \omega_0 \;=\; \sum_{i=1}^n dq^i\wedge dp_i,
> $$
> which acts on two vectors $u=(a^i,b_i)$ and $v=(c^i,d_i)$ by $\omega_0(u,v)=\sum_i (a^i d_i - b_i c^i)$.

In matrix form $\omega_0(u,v)=u^{\mathsf T} J\, v$ with the $2n\times 2n$ block matrix
$$
J=\begin{pmatrix} 0 & I_n \\ -I_n & 0\end{pmatrix},
$$
where $I_n$ is the $n\times n$ identity. One checks $J^{\mathsf T}=-J$ (antisymmetric) and $\det J = 1\ne 0$ (nondegenerate), so $(\mathbb{R}^{2n},\omega_0)$ is a symplectic vector space.

> **Theorem — linear Darboux / symplectic basis.** Every symplectic vector space $(V,\omega)$ of dimension $2n$ has a basis $e_1,\dots,e_n,f_1,\dots,f_n$ — a **symplectic basis** — in which
> $$
> \omega(e_i,e_j)=0,\quad \omega(f_i,f_j)=0,\quad \omega(e_i,f_j)=\delta_{ij},
> $$
> where $\delta_{ij}$ is $1$ if $i=j$ and $0$ otherwise. In this basis $\omega$ is exactly $\omega_0$. Thus all symplectic vector spaces of the same dimension are isomorphic.

**Proof (by induction on $n$, the Gram–Schmidt analogue).**
1. If $V=\{0\}$ there is nothing to do; assume $\dim V=2n\ge 2$. Pick any nonzero $e_1\in V$. *Reason:* a nonzero space has a nonzero vector.
2. By nondegeneracy there exists $w$ with $\omega(e_1,w)\ne 0$; rescale to $f_1:=w/\omega(e_1,w)$, so $\omega(e_1,f_1)=1$. *Reason:* nondegeneracy says $\omega(e_1,\cdot)$ is not the zero covector.
3. Note $e_1,f_1$ are linearly independent: if $f_1=\lambda e_1$ then $\omega(e_1,f_1)=\lambda\,\omega(e_1,e_1)=0$ by antisymmetry, contradicting $\omega(e_1,f_1)=1$. *Reason:* antisymmetry gives $\omega(e_1,e_1)=0$.
4. Let $W=\mathrm{span}\{e_1,f_1\}$ and define its **symplectic orthogonal complement** $W^\omega=\{v\in V: \omega(v,e_1)=0\text{ and }\omega(v,f_1)=0\}$. Any $v\in V$ decomposes uniquely as $v = \big(\omega(v,f_1)\,e_1 - \omega(v,e_1)\,f_1\big) + v'$ with $v'\in W^\omega$; a direct computation of $\omega(\cdot,e_1)$ and $\omega(\cdot,f_1)$ on the bracketed term reproduces those of $v$, so $v'\in W^\omega$. *Reason:* the bracketed vector is engineered to have the same pairings with $e_1,f_1$ as $v$.
5. Hence $V=W\oplus W^\omega$ as a direct sum, and $\omega$ restricted to $W^\omega$ is again nondegenerate (a vector in $W^\omega$ paired trivially with all of $W^\omega$, and trivially with $W$ by definition, would be paired trivially with all of $V$, hence zero). $\dim W^\omega = 2n-2$. *Reason:* nondegeneracy descends to the complement.
6. By the induction hypothesis $W^\omega$ has a symplectic basis $e_2,\dots,e_n,f_2,\dots,f_n$. Adjoining $e_1,f_1$ gives a symplectic basis of $V$. $\blacksquare$

#### Symplectic versus inner-product structure: the sharp contrast

An **inner product** $g$ is a *symmetric* nondegenerate bilinear form, with $g(v,v)>0$ for $v\ne 0$ (positive-definite). The differences are not cosmetic:

| feature | inner product $g$ | symplectic form $\omega$ |
|---|---|---|
| symmetry | $g(u,v)=g(v,u)$ | $\omega(u,v)=-\omega(v,u)$ |
| self-pairing | $g(v,v)>0$ measures length${}^2$ | $\omega(v,v)=0$ always |
| dimension | any | must be even |
| invariance group | orthogonal $O(n)$ | symplectic $Sp(2n,\mathbb{R})$ |
| local normal form | needs eigenvalues (no flat normal form for curved $g$) | always exactly $\omega_0$ (Darboux) |

The line $\omega(v,v)=0$ is the heart of it: a symplectic form cannot measure the "size" of a single vector, only how two vectors *spread out* into an oriented area. The matrix $J$ above squares to $J^2=-I$, the seed of the complex structure we exploit in s8.

> **Worked example — oriented area in the plane.** Take $V=\mathbb{R}^2$ with $\omega_0=dq\wedge dp$, and the two vectors $u=(3,1)$ (i.e. $3\,\partial_q+1\,\partial_p$) and $v=(1,2)$. Then $\omega_0(u,v)=a^1 d_1 - b_1 c^1 = 3\cdot 2 - 1\cdot 1 = 5$. Geometrically this is the signed area of the parallelogram spanned by $u$ and $v$ — the same $2\times 2$ determinant $\det\left(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\right)=5$ that the cross product computes. Swapping the inputs flips the sign: $\omega_0(v,u)=-5$, confirming antisymmetry. And $\omega_0(u,u)=3\cdot1-1\cdot3=0$: a vector spans no area with itself. Contrast the Euclidean inner product $g(u,u)=3^2+1^2=10\ne0$, which measures length-squared. This single numerical example is the whole conceptual difference between the two structures.

> **The symplectic group.** The linear maps $T:V\to V$ preserving $\omega$ (so $\omega(Tu,Tv)=\omega(u,v)$) form the **symplectic group** $Sp(2n,\mathbb{R})$. In the standard basis $T$ is symplectic iff $T^{\mathsf T}JT=J$. Taking determinants of this relation and using $\det J\ne0$ gives $\det(T)^2=1$; a finer argument (the Pfaffian) shows in fact $\det T=+1$, so symplectic maps are volume-and-orientation preserving — the linear shadow of Liouville's theorem (s5).

<a id="s2"></a>
### Symplectic manifolds; the nondegenerate closed 2-form; Darboux's theorem

We now spread a symplectic form smoothly over a manifold. The new ingredient beyond the linear theory is a *differential* condition — closedness — with no linear-algebra analogue.

#### Definition

> **Definition — symplectic manifold.**
>
> A **symplectic manifold** is a pair $(M,\omega)$ where $M$ is a smooth manifold and $\omega$ is a **symplectic form**: a differential $2$-form (an antisymmetric $\binom{0}{2}$-tensor field) that is
> - **nondegenerate**: at every point $p\in M$, the bilinear form $\omega_p$ on the tangent space $T_pM$ is nondegenerate in the sense of s1;
> - **closed**: $d\omega = 0$, where $d$ is the exterior derivative.

By s1, nondegeneracy forces $\dim M = 2n$ to be even. The form $\omega$ being a $2$-form means at each point it eats two tangent vectors and returns a number, antisymmetrically; "differential" means it varies smoothly with $p$.

> **Why closed?** Recall from the prerequisite the exterior derivative $d$, which sends a $k$-form to a $(k+1)$-form and satisfies $d^2=0$. The condition $d\omega=0$ has three equivalent payoffs, proved later: (i) the Hamiltonian flow preserves $\omega$ (s5); (ii) the Poisson bracket obeys the Jacobi identity (s4); (iii) locally $\omega=d\theta$ for some $1$-form $\theta$ (Poincaré lemma), the **symplectic potential**.

#### The nondegeneracy map and the canonical volume

Nondegeneracy gives, at each point, the isomorphism $\flat:T_pM\to T_p^*M$, $X\mapsto \iota_X\omega := \omega(X,\cdot)$. Its inverse is written $\sharp$. This **musical isomorphism** lets us convert a covector (such as $dH$) into a vector (the Hamiltonian field $X_H$), the construction underlying all of mechanics.

> **Proposition — the Liouville volume.** On a $2n$-dimensional symplectic manifold the top-degree form
> $$
> \omega^n := \underbrace{\omega\wedge\cdots\wedge\omega}_{n}
> $$
> is nowhere zero; it is a volume form, the **Liouville volume**.

**Proof.** At a point, choose a symplectic basis (s1) so $\omega=\sum_i dq^i\wedge dp_i$. Expanding the wedge power, every term with a repeated factor $dq^i\wedge dp_i\wedge dq^i$ vanishes (a repeated $1$-form wedges to zero), leaving only the fully mixed terms; collecting them, $\omega^n = n!\, dq^1\wedge dp_1\wedge\cdots\wedge dq^n\wedge dp_n$, which is $n!$ times the standard volume and hence nonzero. *Reason:* the wedge of $2n$ distinct coordinate $1$-forms in $2n$ dimensions is the volume form. $\blacksquare$

A consequence (anticipating s5): Hamiltonian flow preserves $\omega$, hence preserves $\omega^n$ — this is **Liouville's theorem**, the conservation of phase-space volume.

> **Worked example — which spheres are symplectic?** The Liouville volume gives a quick topological obstruction. If a *compact* manifold $M^{2n}$ is symplectic, then $\omega^n$ is a nonvanishing top form whose integral $\int_M\omega^n\ne0$; therefore the cohomology class $[\omega^n]=[\omega]^n\ne0$ in de Rham cohomology, which forces $[\omega]\in H^2(M)$ to be nonzero (a zero class would have zero powers). For $S^{2n}$ with $n\ge2$ the cohomology $H^2(S^{2n})=0$, so no symplectic form can exist. Concretely: $S^2$ *is* symplectic (its area form), but $S^4, S^6,\dots$ are *not*. *Reason:* a nonzero $[\omega]\in H^2$ is required, and higher spheres have no $H^2$. This shows symplectic structures are a real constraint, not available on every even-dimensional manifold.

#### Darboux's theorem

The most surprising structural fact is that, unlike a metric, a symplectic form has *no local invariants*: locally every symplectic manifold is the standard one.

> **Theorem — Darboux.** Let $(M,\omega)$ be a $2n$-dimensional symplectic manifold and $p\in M$. There is a coordinate chart $(U;q^1,\dots,q^n,p_1,\dots,p_n)$ around $p$ in which
> $$
> \omega = \sum_{i=1}^n dq^i\wedge dp_i.
> $$
> These are **Darboux** (or **canonical**) coordinates.

**Idea of proof (Moser's deformation trick).** The cleanest argument interpolates between $\omega$ and a constant-coefficient model.
1. By the linear Darboux theorem (s1) applied to $T_pM$, choose linear coordinates so that $\omega_p$, *at the single point $p$*, equals $\omega_0=\sum dq^i\wedge dp_i$. Set $\omega_1:=\omega$ and let $\omega_0$ also denote the constant-coefficient form $\sum dq^i\wedge dp_i$ on the chart. Then $\omega_0$ and $\omega_1$ agree at $p$. *Reason:* linear normal form fixes the value at one point.
2. Consider the family $\omega_t=(1-t)\omega_0+t\,\omega_1$ for $t\in[0,1]$. Each $\omega_t$ is closed (a combination of closed forms) and, near $p$, nondegenerate (it equals $\omega_0$ at $p$, and nondegeneracy is an open condition), so each $\omega_t$ is symplectic on a small neighborhood. *Reason:* nondegeneracy = nonvanishing of $\omega_t^n$, an open condition.
3. The difference $\omega_1-\omega_0$ is closed and vanishes at $p$; by the Poincaré lemma it equals $d\sigma$ for a $1$-form $\sigma$ that can be chosen to vanish at $p$. *Reason:* closed forms are locally exact.
4. **Moser's equation.** Seek a time-dependent vector field $X_t$ with $\iota_{X_t}\omega_t=-\sigma$; nondegeneracy of $\omega_t$ lets us solve for $X_t$ uniquely via $\sharp$. Let $\psi_t$ be its flow. Then by Cartan's formula $\frac{d}{dt}(\psi_t^*\omega_t)=\psi_t^*\big(\mathcal{L}_{X_t}\omega_t + \tfrac{d}{dt}\omega_t\big)=\psi_t^*\big(d\,\iota_{X_t}\omega_t + (\omega_1-\omega_0)\big)=\psi_t^*\big(-d\sigma + d\sigma\big)=0$. *Reason:* Cartan's magic formula $\mathcal{L}_X=d\iota_X+\iota_X d$ and $d\omega_t=0$.
5. Hence $\psi_t^*\omega_t$ is constant in $t$, so $\psi_1^*\omega_1=\psi_0^*\omega_0=\omega_0$. The diffeomorphism $\psi_1$ pulls $\omega$ back to $\omega_0$; using it to define coordinates gives the Darboux chart. $\blacksquare$

> **Worked example — explicit Darboux chart on the sphere.** Take $S^2$ (radius $1$) with area form $\omega=\sin\phi\,d\phi\wedge d\theta$, where $\phi\in(0,\pi)$ is the polar angle and $\theta\in(0,2\pi)$ the azimuth. Set new coordinates $q:=\theta$ and $p:=-\cos\phi$ (so $p\in(-1,1)$, the height). Then $dp = \sin\phi\,d\phi$, hence $dq\wedge dp = d\theta\wedge(\sin\phi\,d\phi) = -\sin\phi\,d\phi\wedge d\theta = -\omega$, so $\omega = dp\wedge dq = dq\wedge d(-p)$; relabelling $p\mapsto -p$ gives the clean Darboux form $\omega = dq\wedge dp$. The pair $(\theta,-\cos\phi)$ are honest canonical coordinates — Archimedes' theorem that the cylinder projection of the sphere preserves area is exactly the statement that these coordinates put $\omega$ in standard form.

> **Pitfall.** Darboux does *not* say symplectic manifolds are globally trivial. The sphere $S^2$ with its area form is symplectic and locally standard, yet globally distinct from $\mathbb{R}^2$ (it is compact, with finite total area). All the interesting symplectic invariants are global.

<a id="s3"></a>
### The cotangent bundle as the canonical phase space; the tautological and canonical forms

Where does a symplectic form come from in mechanics? The answer is automatic: *any* configuration space carries a canonical symplectic structure on its cotangent bundle.

#### The cotangent bundle as phase space

> **Setup.** Let $Q$ be a smooth $n$-manifold, the **configuration space** (positions $q$). Its **cotangent bundle** $T^*Q=\{(q,p): q\in Q,\ p\in T_q^*Q\}$ collects each position together with a covector $p$ there — physically a momentum. Local coordinates $q^i$ on $Q$ induce coordinates $(q^i,p_i)$ on $T^*Q$, where $p=\sum_i p_i\,dq^i$. This $2n$-dimensional manifold is the **phase space**.

The bundle projection is $\pi:T^*Q\to Q$, $\pi(q,p)=q$, with derivative $d\pi:T_{(q,p)}(T^*Q)\to T_qQ$.

#### The tautological one-form

> **Definition — tautological (Liouville) one-form.** Define a $1$-form $\theta$ on $T^*Q$ at the point $(q,p)$ by
> $$
> \theta_{(q,p)}(X) := p\big(d\pi(X)\big),\qquad X\in T_{(q,p)}(T^*Q).
> $$
> In words: push the tangent vector $X$ down to $Q$ via $d\pi$, then evaluate the covector $p$ — which lives at the very point we are sitting over — on it. Hence "tautological": $\theta$ uses the point's own $p$.

> **Lemma — coordinate expression.** In induced coordinates,
> $$
> \theta = \sum_{i=1}^n p_i\, dq^i.
> $$

**Proof.**
1. A general tangent vector is $X=\sum_i a^i\,\partial_{q^i} + \sum_i b_i\,\partial_{p_i}$. *Reason:* $(q^i,p_i)$ are coordinates, so their coordinate vector fields span the tangent space.
2. The projection $\pi$ drops the $p$-coordinates, so $d\pi(X)=\sum_i a^i\,\partial_{q^i}\in T_qQ$. *Reason:* $\pi(q,p)=q$ depends only on $q^i$, so $\partial \pi/\partial p_i=0$.
3. At $(q,p)$ the covector is $p=\sum_i p_i\,dq^i$, so $p\big(d\pi(X)\big)=\sum_i p_i\,a^i$. *Reason:* $dq^i(\partial_{q^j})=\delta^i_j$.
4. On the other hand $\big(\sum_i p_i\,dq^i\big)(X)=\sum_i p_i\,a^i$, evaluating $dq^i$ on $X$ and discarding the $\partial_{p_j}$ part. These agree, so $\theta=\sum_i p_i\,dq^i$. $\blacksquare$

#### The canonical symplectic form

> **Definition — canonical symplectic form.** $\omega_{\mathrm{can}} := -\,d\theta$.

> **Proposition.** $\omega_{\mathrm{can}}$ is a symplectic form on $T^*Q$, and in induced coordinates
> $$
> \omega_{\mathrm{can}} = \sum_{i=1}^n dq^i\wedge dp_i.
> $$

**Proof.**
1. Compute $-d\theta = -d\big(\sum_i p_i\,dq^i\big) = -\sum_i dp_i\wedge dq^i$, using $d(p_i\,dq^i)=dp_i\wedge dq^i + p_i\,d(dq^i)$ and $d(dq^i)=0$ (since $d^2=0$). *Reason:* the Leibniz rule for $d$ on a product of a function and a $1$-form, plus $d^2=0$.
2. Antisymmetry of $\wedge$ gives $-dp_i\wedge dq^i = dq^i\wedge dp_i$, so $\omega_{\mathrm{can}}=\sum_i dq^i\wedge dp_i$. *Reason:* $\alpha\wedge\beta=-\beta\wedge\alpha$ for $1$-forms.
3. **Closed:** $d\omega_{\mathrm{can}}=d(-d\theta)=-d^2\theta=0$. *Reason:* $d^2=0$.
4. **Nondegenerate:** the coordinate form is exactly the standard $\omega_0$, which we verified is nondegenerate in s1. $\blacksquare$

The minus sign is a convention chosen so that $\omega_{\mathrm{can}}=\sum dq^i\wedge dp_i$ rather than $\sum dp_i\wedge dq^i$, matching Hamilton's equations with the conventional signs.

> **Worked example.** For a free particle on a line, $Q=\mathbb{R}$, $T^*Q=\mathbb{R}^2$ with coordinates $(q,p)$, and $\theta=p\,dq$, $\omega_{\mathrm{can}}=dq\wedge dp$. The area enclosed by a loop in phase space — the integral $\oint p\,dq$ of the tautological form — is the classical **action**, the quantity Bohr and Sommerfeld set equal to integer multiples of $h$. We return to this in s9.

> **Worked example — the pendulum's phase space.** For a particle on the circle $Q=S^1$ with angle coordinate $\varphi$, the phase space is $T^*S^1$, the cylinder with coordinates $(\varphi,p_\varphi)$, $\theta=p_\varphi\,d\varphi$, $\omega=d\varphi\wedge dp_\varphi$. A pendulum has $H=\tfrac{1}{2}p_\varphi^2 - \cos\varphi$; its level sets in the cylinder are the familiar pendulum portraits — small oscillation loops near $(\varphi,p_\varphi)=(0,0)$, and rotation curves that wind around the cylinder above the separatrix. The action $\oint p_\varphi\,d\varphi$ of a closed orbit is the enclosed phase-space area, again the quantity the old quantum theory quantized. This example shows the configuration space need not be $\mathbb{R}^n$: the cotangent construction is automatic for *any* $Q$.

> **Naturality.** The tautological form is **natural**: for any diffeomorphism $\psi:Q_1\to Q_2$, its cotangent lift $T^*\psi:T^*Q_2\to T^*Q_1$ pulls back $\theta_1$ to $\theta_2$, hence is automatically a symplectomorphism. Thus every symmetry of the configuration space is, for free, a symmetry of phase space — a fact we exploit when building moment maps in s6.

<a id="s4"></a>
### Hamiltonian vector fields and the Poisson bracket

Now dynamics. A function on phase space generates a flow, and two functions can be paired into a third — the Poisson bracket — whose deepest property, the Jacobi identity, we prove directly from $d\omega=0$.

#### Hamiltonian vector fields

> **Definition — Hamiltonian vector field.** Let $(M,\omega)$ be symplectic and $f\in C^\infty(M)$ a smooth function. Its **Hamiltonian vector field** $X_f$ is the unique vector field with
> $$
> \iota_{X_f}\omega = df,\qquad\text{i.e.}\qquad \omega(X_f,\cdot)=df.
> $$
> Existence and uniqueness follow because $\flat:X\mapsto\iota_X\omega$ is an isomorphism (nondegeneracy, s2); explicitly $X_f=\sharp(df)$.

> **Coordinate form (Darboux).** In Darboux coordinates with $\omega=\sum dq^i\wedge dp_i$,
> $$
> X_f = \sum_{i=1}^n\left(\frac{\partial f}{\partial p_i}\,\frac{\partial}{\partial q^i} - \frac{\partial f}{\partial q^i}\,\frac{\partial}{\partial p_i}\right).
> $$

**Derivation.**
1. Write $X_f=\sum_i(A^i\partial_{q^i}+B_i\partial_{p_i})$ with unknown components. Then $\iota_{X_f}\omega=\sum_i(A^i\,dp_i - B_i\,dq^i)$, computing $\iota_X(dq^i\wedge dp_i)=(dq^i(X))dp_i-(dp_i(X))dq^i = A^i\,dp_i - B_i\,dq^i$. *Reason:* the interior product of a vector into a wedge of $1$-forms.
2. Meanwhile $df=\sum_i(\partial_{q^i}f\,dq^i+\partial_{p_i}f\,dp_i)$. *Reason:* definition of the differential of a function.
3. Matching the coefficients of $dq^i$ and $dp_i$ in $\iota_{X_f}\omega=df$: $-B_i=\partial_{q^i}f$ and $A^i=\partial_{p_i}f$. *Reason:* $\{dq^i,dp_i\}$ is a basis of $1$-forms, so coefficients match termwise.
4. Substituting gives the stated formula. $\blacksquare$

Taking $f=H$ the Hamiltonian, the integral curves of $X_H$ satisfy $\dot q^i=\partial H/\partial p_i$, $\dot p_i=-\partial H/\partial q^i$ — **Hamilton's equations** recovered exactly, sign and all.

#### The Poisson bracket

> **Definition — Poisson bracket.** For $f,g\in C^\infty(M)$,
> $$
> \{f,g\} := \omega(X_f,X_g) = X_f(g) = -X_g(f).
> $$
> The expressions agree: $\omega(X_f,X_g)=(\iota_{X_f}\omega)(X_g)=df(X_g)=X_g(f)$, and by antisymmetry of $\omega$ this also equals $-(\iota_{X_g}\omega)(X_f)=-dg(X_f)=-X_g(f)$ applied the other way. We adopt the convention $\{f,g\}=X_f(g)=-X_g(f)$, fixing the overall sign once and for all.

> **Coordinate form.**
> $$
> \{f,g\} = \sum_{i=1}^n\left(\frac{\partial f}{\partial q^i}\frac{\partial g}{\partial p_i} - \frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q^i}\right).
> $$

**Derivation.** Using $\{f,g\}=X_f(g)$ and the coordinate form of $X_f$ from above: $X_f(g)=\sum_i(\partial_{p_i}f\,\partial_{q^i}g - \partial_{q^i}f\,\partial_{p_i}g)$. Reversing the labelling of the two terms gives the displayed antisymmetric expression (the standard convention). The fundamental brackets are $\{q^i,q^j\}=0$, $\{p_i,p_j\}=0$, $\{q^i,p_j\}=\delta^i_j$.

The bracket is **bilinear** and **antisymmetric** ($\{f,g\}=-\{g,f\}$, immediate from $\omega$ antisymmetric) and obeys the **Leibniz rule** $\{f,gh\}=\{f,g\}h+g\{f,h\}$ (because $X_f$ is a derivation). The deep property is:

> **Theorem — Jacobi identity.** For all $f,g,h\in C^\infty(M)$,
> $$
> \{f,\{g,h\}\}+\{g,\{h,f\}\}+\{h,\{f,g\}\}=0.
> $$

**Proof from $d\omega=0$.** We use the invariant formula for the exterior derivative of a $2$-form. For any $2$-form $\omega$ and vector fields $X,Y,Z$,
$$
d\omega(X,Y,Z) = X\,\omega(Y,Z) - Y\,\omega(X,Z) + Z\,\omega(X,Y) - \omega([X,Y],Z) + \omega([X,Z],Y) - \omega([Y,Z],X),
$$
where $[\cdot,\cdot]$ is the Lie bracket of vector fields. (This is the standard intrinsic formula; the prerequisite guide derives it.) We feed in $X=X_f,\ Y=X_g,\ Z=X_h$ and exploit $d\omega=0$.

1. Each pairing of two Hamiltonian fields is a Poisson bracket: $\omega(X_g,X_h)=\{g,h\}$, etc. *Reason:* definition of $\{\cdot,\cdot\}$.
2. Each "directional derivative" term becomes a *double* bracket. For instance $X_f\,\omega(X_g,X_h)=X_f\{g,h\}=\{f,\{g,h\}\}$, using $X_f(\phi)=\{f,\phi\}$ for any function $\phi$. *Reason:* the relation $\{f,\phi\}=X_f(\phi)$.
3. We need the Lie-bracket terms. **Key lemma:** $[X_f,X_g]=X_{\{f,g\}}$ (the map $f\mapsto X_f$ is a Lie-algebra homomorphism, up to sign), proved below; granting it, $\omega([X_f,X_g],X_h)=\omega(X_{\{f,g\}},X_h)=\{\{f,g\},h\}=-\{h,\{f,g\}\}$. *Reason:* the key lemma and antisymmetry of the bracket.
4. Substitute into the intrinsic formula and set $d\omega(X_f,X_g,X_h)=0$. The three "derivative" terms give $\{f,\{g,h\}\}-\{g,\{f,h\}\}+\{h,\{f,g\}\}$. The three Lie-bracket terms give $-(-\{h,\{f,g\}\}) + (\ldots) - (\ldots)$. Writing everything out and using antisymmetry to align signs, the six terms collapse to exactly twice the Jacobiator: $0 = d\omega(\ldots) = 2\big(\{f,\{g,h\}\}+\{g,\{h,f\}\}+\{h,\{f,g\}\}\big)$. *Reason:* $d\omega=0$ kills the left side; bookkeeping the right side. Dividing by $2$ gives the identity. $\blacksquare$

**Proof of the key lemma $[X_f,X_g]=X_{\{f,g\}}$.**
1. We show $\iota_{[X_f,X_g]}\omega = d\{f,g\}$; since $\flat$ is injective this identifies the field. *Reason:* nondegeneracy means a Hamiltonian field is determined by $\iota_X\omega$.
2. A general identity: $\iota_{[X,Y]}\omega = \mathcal{L}_X(\iota_Y\omega) - \iota_Y(\mathcal{L}_X\omega)$. *Reason:* the Lie derivative commutes with contraction up to this bracket term (a standard Cartan-calculus identity).
3. First, $\mathcal{L}_{X_f}\omega = d\,\iota_{X_f}\omega + \iota_{X_f}\,d\omega = d(df) + 0 = 0$, using Cartan's magic formula, $\iota_{X_f}\omega=df$, $d^2=0$, and $d\omega=0$. So the last term in step 2 vanishes. *Reason:* Cartan's formula and closedness — **this is where $d\omega=0$ enters again.**
4. Then $\iota_{[X_f,X_g]}\omega = \mathcal{L}_{X_f}(\iota_{X_g}\omega) = \mathcal{L}_{X_f}(dg) = d(\mathcal{L}_{X_f}g) = d(X_f g) = d\{f,g\}$, using that $\mathcal{L}_{X_f}$ commutes with $d$ and acts on functions as the directional derivative. *Reason:* $\mathcal{L}_X d = d\mathcal{L}_X$ and $\mathcal{L}_X g = Xg$.
5. Therefore $[X_f,X_g]=X_{\{f,g\}}$. $\blacksquare$

> **Why this matters.** $(C^\infty(M),\{\cdot,\cdot\})$ is a **Poisson algebra** — a Lie algebra under the bracket that also obeys Leibniz. Quantization will replace this bracket by $\tfrac{1}{i\hbar}$ times the commutator of operators; the Jacobi identity is the classical shadow of the operator commutator's Jacobi identity. Without $d\omega=0$, none of this works.

#### Worked example

For the harmonic oscillator $H=\tfrac12(p^2+q^2)$ on $\mathbb{R}^2$: $X_H=p\,\partial_q - q\,\partial_p$, so $\dot q=p,\ \dot p=-q$, giving circular motion $q(t)=q_0\cos t+p_0\sin t$. And $\{q,H\}=\partial_q q\,\partial_p H-\partial_p q\,\partial_q H = p = \dot q$, confirming $\dot f=\{f,H\}$ for time evolution.

<a id="s5"></a>
### Symplectomorphisms, canonical transformations, and Hamiltonian flows preserving $\omega$

We classify the maps that respect symplectic structure and show that Hamiltonian dynamics lives inside this class.

> **Definition — symplectomorphism.** A diffeomorphism $\phi:(M_1,\omega_1)\to(M_2,\omega_2)$ is a **symplectomorphism** if $\phi^*\omega_2=\omega_1$, i.e. it pulls one form back to the other. When $M_1=M_2$ these are the symmetries of a phase space; physicists call them **canonical transformations** — coordinate changes preserving the form of Hamilton's equations.

> **Theorem — Hamiltonian flows are symplectomorphisms.** Let $\psi_t$ be the flow of a Hamiltonian vector field $X_H$ (the time-$t$ map sending an initial state along the dynamics). Then $\psi_t^*\omega=\omega$ for all $t$: time evolution preserves the symplectic form.

**Proof.**
1. Differentiate: $\frac{d}{dt}\psi_t^*\omega = \psi_t^*(\mathcal{L}_{X_H}\omega)$. *Reason:* the defining property of the Lie derivative as the rate of change of a tensor along a flow.
2. Compute $\mathcal{L}_{X_H}\omega = d\,\iota_{X_H}\omega + \iota_{X_H}\,d\omega$. *Reason:* Cartan's magic formula.
3. The first term is $d(dH)=0$ ($\iota_{X_H}\omega=dH$ and $d^2=0$); the second is $\iota_{X_H}(0)=0$ ($d\omega=0$). *Reason:* definition of $X_H$, $d^2=0$, and closedness.
4. Hence $\frac{d}{dt}\psi_t^*\omega=0$, so $\psi_t^*\omega$ is constant; at $t=0$ it is $\omega$, so $\psi_t^*\omega=\omega$ for all $t$. $\blacksquare$

Taking wedge powers, $\psi_t^*\omega^n=\omega^n$: the flow preserves the Liouville volume. This is **Liouville's theorem** — a swarm of states evolving under Hamilton's equations keeps its phase-space volume fixed, the geometric root of statistical mechanics' equal-a-priori-probability postulate.

> **Conversely — locally Hamiltonian fields.** A vector field $X$ with $\mathcal{L}_X\omega=0$ is **symplectic**; by Cartan $\mathcal{L}_X\omega=d\iota_X\omega$, so $X$ symplectic $\iff$ $\iota_X\omega$ is closed. If $\iota_X\omega$ is *exact*, $=df$, then $X=X_f$ is genuinely Hamiltonian. The gap between closed and exact is measured by the first de Rham cohomology $H^1(M)$: on a simply connected $M$ every symplectic field is Hamiltonian, but on, say, the torus there are symplectic flows with no global generating $H$.

> **Worked example — a linear canonical transformation.** On $(\mathbb{R}^2,dq\wedge dp)$ the map $\phi(q,p)=(\lambda q,\ \lambda^{-1}p)$ (a "squeeze") satisfies $\phi^*(dq\wedge dp)=d(\lambda q)\wedge d(\lambda^{-1}p)=\lambda\lambda^{-1}\,dq\wedge dp=dq\wedge dp$, so it is a symplectomorphism: it stretches positions and compresses momenta while preserving area. By contrast $(q,p)\mapsto(2q,2p)$ scales area by $4$ and is *not* canonical.

> **Worked example — the harmonic-oscillator flow is canonical.** From s4, the oscillator flow is $\psi_t(q_0,p_0)=(q_0\cos t + p_0\sin t,\ -q_0\sin t + p_0\cos t)$, a rotation by angle $t$ in the $(q,p)$-plane. Its Jacobian matrix is the rotation $R_t=\left(\begin{smallmatrix}\cos t&\sin t\\-\sin t&\cos t\end{smallmatrix}\right)$ with $\det R_t=\cos^2 t+\sin^2 t=1$, so $\psi_t^*(dq\wedge dp)=\det(R_t)\,dq\wedge dp=dq\wedge dp$. The flow preserves area for every $t$, as the general theorem guarantees — energy circles are swept out at constant phase-space area, the geometric content of the oscillator's uniform angular velocity.

> **Generating functions.** Canonical transformations are encoded by **generating functions** living on Lagrangian submanifolds (s7). For a transformation $(q,p)\mapsto(Q,P)$ of $\mathbb{R}^{2n}$, a function $S_1(q,Q)$ with $p=\partial S_1/\partial q$, $P=-\partial S_1/\partial Q$ automatically produces a symplectomorphism, because then $p\,dq - P\,dQ = dS_1$ is exact, so $d(p\,dq)=d(P\,dQ)$, i.e. $\sum dq^i\wedge dp_i=\sum dQ^i\wedge dP_i$. The four classical "types" $S_1(q,Q),S_2(q,P),S_3(p,Q),S_4(p,P)$ are Legendre transforms of one another, and Hamilton–Jacobi theory chooses $S_2$ so that the new Hamiltonian vanishes — turning solving the dynamics into finding one generating function.

<a id="s6"></a>
### Moment maps and continuous symmetries; symplectic (Marsden–Weinstein) reduction

Symmetries of a phase space produce conserved quantities and let us shrink the space. This is Noether's theorem made fully geometric.

#### Group actions and moment maps

> **Setup.** Let a Lie group $G$ act on $(M,\omega)$ by symplectomorphisms (each group element acts as a symplectomorphism). Its Lie algebra $\mathfrak g$ (the tangent space at the identity, with bracket $[\cdot,\cdot]$) acts by **fundamental vector fields**: each $\xi\in\mathfrak g$ gives a field $\xi_M$ on $M$ generating the one-parameter subgroup's flow. Each $\xi_M$ is symplectic ($\mathcal{L}_{\xi_M}\omega=0$).

> **Definition — moment map.** A **moment map** for the action is a smooth map $\mu:M\to\mathfrak g^*$ (into the dual of the Lie algebra) such that:
> - for each $\xi\in\mathfrak g$, the component function $\mu^\xi(x):=\langle\mu(x),\xi\rangle$ is a Hamiltonian for $\xi_M$, i.e. $X_{\mu^\xi}=\xi_M$, equivalently $d\mu^\xi=\iota_{\xi_M}\omega$;
> - $\mu$ is **equivariant**: it intertwines the $G$-action on $M$ with the coadjoint action on $\mathfrak g^*$.

In words: the moment map packages the conserved quantities of all the symmetries into one $\mathfrak g^*$-valued function. For each symmetry direction $\xi$, the function $\mu^\xi$ is the Noether charge.

> **Theorem — geometric Noether.** If $H$ is $G$-invariant ($H\circ g=H$ for all $g\in G$), then each component $\mu^\xi$ is conserved along the Hamiltonian flow of $H$: $\{H,\mu^\xi\}=0$.

**Proof.**
1. $G$-invariance of $H$ means $\xi_M(H)=0$ for every $\xi$ (the flow of the symmetry does not change $H$). *Reason:* invariance under the one-parameter group generated by $\xi$.
2. But $\xi_M=X_{\mu^\xi}$, so $\xi_M(H)=X_{\mu^\xi}(H)=\{\mu^\xi,H\}$. *Reason:* moment-map property and definition of the bracket.
3. Hence $\{\mu^\xi,H\}=0$, and by antisymmetry $\{H,\mu^\xi\}=0$, so $\frac{d}{dt}\mu^\xi=\{\mu^\xi,H\}=0$ along the flow. $\blacksquare$

> **Worked examples.** (i) *Translations.* $Q=\mathbb{R}^n$, $G=\mathbb{R}^n$ acting by $q\mapsto q+a$. The moment map is $\mu(q,p)=p$: linear momentum is conserved. (ii) *Rotations.* $G=SO(3)$ on $\mathbb{R}^3$; the moment map is the angular momentum $\mu(q,p)=q\times p$. The Lie-algebra bracket of $\mathfrak{so}(3)$ is reproduced by the Poisson brackets $\{L_i,L_j\}=\epsilon_{ijk}L_k$ of the angular-momentum components — the classical seed of the quantum angular-momentum algebra.

> **Worked computation — the angular-momentum bracket.** Let $L_1=q^2p_3-q^3p_2$ and $L_2=q^3p_1-q^1p_3$ on $\mathbb{R}^6$, with canonical brackets $\{q^i,p_j\}=\delta^i_j$ and $\{q^i,q^j\}=\{p_i,p_j\}=0$. We compute $\{L_1,L_2\}$ using bilinearity and the Leibniz rule, retaining only the cross-brackets that pair a coordinate with its own conjugate momentum.
> 1. $\{q^2p_3,\,q^3p_1\} = q^2p_1\{p_3,q^3\} = q^2p_1\cdot(-1) = -q^2p_1$. *Reason:* $\{p_3,q^3\}=-\{q^3,p_3\}=-1$; the other factors come out by Leibniz.
> 2. $\{-q^3p_2,\,-q^1p_3\} = q^3p_2\,\{p_2\,\text{vs}\,q\}$ — the only conjugate pair here is $q^3$ with $p_3$: $\{-q^3p_2,-q^1p_3\}=q^1p_2\{q^3,p_3\}=q^1p_2$. *Reason:* $\{q^3,p_3\}=+1$.
> 3. The remaining two cross terms $\{q^2p_3,-q^1p_3\}$ and $\{-q^3p_2,q^3p_1\}$ vanish: no coordinate meets its conjugate momentum. *Reason:* all such canonical brackets are zero.
> 4. Summing: $\{L_1,L_2\} = -q^2p_1 + q^1p_2 = q^1p_2 - q^2p_1 = L_3$.
>
> So $\{L_1,L_2\}=L_3$, reproducing the structure constants $\epsilon_{ijk}$ of $\mathfrak{so}(3)$. The quantum relation $[\hat L_i,\hat L_j]=i\hbar\,\epsilon_{ijk}\hat L_k$ is exactly this computation under $\{\cdot,\cdot\}\to\tfrac{1}{i\hbar}[\cdot,\cdot]$.

#### Marsden–Weinstein reduction

When a symmetry is present, the dynamics secretly take place on a smaller space: fix the conserved charge and quotient by the symmetry.

> **Theorem — Marsden–Weinstein–Meyer reduction.** Let $G$ act on $(M,\omega)$ with equivariant moment map $\mu$, and let $\zeta\in\mathfrak g^*$ be a value fixed by the coadjoint action (e.g. $\zeta=0$, or any value if $G$ is abelian). Suppose $G$ acts freely and properly on the level set $\mu^{-1}(\zeta)$. Then the **reduced space**
> $$
> M_\zeta := \mu^{-1}(\zeta)\big/G
> $$
> is a smooth manifold and carries a unique symplectic form $\omega_\zeta$ with $\iota^*\omega = \pi^*\omega_\zeta$, where $\iota:\mu^{-1}(\zeta)\hookrightarrow M$ is the inclusion and $\pi:\mu^{-1}(\zeta)\to M_\zeta$ the quotient projection. Its dimension is $\dim M - 2\dim G$.

**Idea of proof.**
1. The level set $\mu^{-1}(\zeta)$ has codimension $\dim G$ (the moment map has $\dim G$ independent components when the action is free). *Reason:* regular value theorem; freeness makes $\zeta$ regular.
2. At a point of $\mu^{-1}(\zeta)$, the tangent space to the level set is the **symplectic orthogonal** of the tangent to the group orbit: $T(\mu^{-1}\zeta)=(\mathfrak g\!\cdot\! x)^\omega$. *Reason:* $d\mu^\xi=\iota_{\xi_M}\omega$ means $v\in\ker d\mu \iff \omega(\xi_M,v)=0\ \forall\xi$.
3. Consequently the orbit directions $\mathfrak g\!\cdot\! x$ lie *inside* the level set and are exactly its **null directions** for the restricted form $\iota^*\omega$. Quotienting by $G$ removes precisely these null directions, leaving a nondegenerate form. *Reason:* removing the radical of a degenerate form yields a nondegenerate one.
4. The form descends because $\iota^*\omega$ is $G$-invariant and basic (horizontal); closedness descends since $d$ commutes with pullback. $\blacksquare$

> **Physical meaning & example.** Reduction *is* the elimination of cyclic coordinates. For a central-force problem, $SO(3)$-symmetry lets us fix the angular momentum and pass to a reduced radial problem; the "centrifugal barrier" is the residue of the reduced symplectic geometry. Reducing $\mathbb{C}^{n+1}$ by the $U(1)$ phase action at a nonzero moment level yields complex projective space $\mathbb{CP}^n$ with its Fubini–Study form — the model we quantize for spin in s11.

> **Coadjoint orbits.** A particularly clean source of symplectic manifolds is the **coadjoint orbits** of a Lie group $G$ inside $\mathfrak g^*$: the sets $\mathcal O_\zeta=\{\mathrm{Ad}^*_g\zeta : g\in G\}$ swept out by the coadjoint action. The **Kirillov–Kostant–Souriau theorem** says each carries a canonical symplectic form $\omega_{\mathcal O}(\xi_M,\eta_M)|_\zeta=\langle\zeta,[\xi,\eta]\rangle$, built directly from the Lie bracket. For $G=SU(2)$ the nonzero coadjoint orbits are spheres of every radius — and these are exactly the classical spin phase spaces of s11. Coadjoint orbits are the geometric home of the "orbit method," which quantizes group representations as quantizations of these orbits, tying s6 directly to s11.

<a id="s7"></a>
### Lagrangian submanifolds and their role

There is a class of submanifolds maximally adapted to $\omega$ — neither too big nor too small — that encodes generating functions, dynamics, and the very objects quantum states will be built from.

> **Definitions — isotropic, coisotropic, Lagrangian.** Let $(M^{2n},\omega)$ be symplectic and $L\subseteq M$ a submanifold. At each point the tangent space $T_pL$ has a **symplectic orthogonal** $(T_pL)^\omega=\{v\in T_pM:\omega(v,w)=0\ \forall w\in T_pL\}$. Then $L$ is:
> - **isotropic** if $T_pL\subseteq(T_pL)^\omega$, i.e. $\omega|_L=0$ (the form vanishes on $L$); necessarily $\dim L\le n$;
> - **coisotropic** if $(T_pL)^\omega\subseteq T_pL$; necessarily $\dim L\ge n$;
> - **Lagrangian** if both, i.e. $\omega|_L=0$ **and** $\dim L=n$ (maximal isotropic).

The dimension count $\dim(T_pL)^\omega = 2n-\dim T_pL$ (a consequence of nondegeneracy, exactly as for the symplectic orthogonal in s1) forces a Lagrangian to be precisely half-dimensional with $\omega$ restricting to zero.

> **Key examples.**
> 1. **The zero section** $Q\hookrightarrow T^*Q$ (all momenta zero): $\theta=\sum p_i\,dq^i$ vanishes there, so $\omega=-d\theta$ restricts to $0$; it is Lagrangian.
> 2. **The graph of $df$.** For $f\in C^\infty(Q)$, the set $\{(q,df_q)\}\subseteq T^*Q$ is Lagrangian, because on it $\theta = df$ pulls back to an exact form, so $\omega|_L=-d(df)=0$. More generally the image of any *closed* $1$-form is Lagrangian.
> 3. **Graphs of symplectomorphisms.** A diffeomorphism $\phi:M_1\to M_2$ is a symplectomorphism $\iff$ its graph is Lagrangian in $(M_1\times M_2,\ \pi_2^*\omega_2-\pi_1^*\omega_1)$. This is Weinstein's slogan, *"everything is a Lagrangian submanifold."*

> **Proposition — graph of a symplectomorphism.** With $\Omega:=\pi_2^*\omega_2-\pi_1^*\omega_1$ on $M_1\times M_2$, the graph $\Gamma_\phi=\{(x,\phi(x))\}$ satisfies $\Omega|_{\Gamma_\phi}=0$ iff $\phi^*\omega_2=\omega_1$.

**Proof.** Parametrize $\Gamma_\phi$ by $x\mapsto(x,\phi(x))$; the pullback of $\pi_1^*\omega_1$ is $\omega_1$ and of $\pi_2^*\omega_2$ is $\phi^*\omega_2$. Hence the pullback of $\Omega$ is $\phi^*\omega_2-\omega_1$, which vanishes iff $\phi^*\omega_2=\omega_1$. Since $\dim\Gamma_\phi=\dim M_1=\tfrac12\dim(M_1\times M_2)$, vanishing of the restricted form is exactly the Lagrangian condition. $\blacksquare$

> **Worked example — a Lagrangian torus and the action variables.** For an integrable system with $n$ commuting conserved quantities $f_1,\dots,f_n$ (so $\{f_i,f_j\}=0$), a common level set $\{f_i=c_i\}$ is Lagrangian: the Hamiltonian fields $X_{f_i}$ span its tangent space and $\omega(X_{f_i},X_{f_j})=\{f_i,f_j\}=0$, so $\omega$ vanishes on it. When compact and connected, the Liouville–Arnold theorem says this level set is a **torus** $T^n$, and there exist **action–angle coordinates** $(I_i,\varphi^i)$ with $\omega=\sum dI_i\wedge d\varphi^i$ in which the dynamics is rigid rotation $\dot\varphi^i=\text{const}$. The actions are the loop integrals $I_i=\frac{1}{2\pi}\oint_{\gamma_i}p\,dq$ over the torus's independent cycles — the very quantities the Bohr–Sommerfeld rule (s9) quantizes.

> **Lagrangian intersections.** Because dynamics carries Lagrangians to Lagrangians (Hamiltonian flow is a symplectomorphism, and symplectomorphisms preserve the Lagrangian condition by the graph proposition), questions like "does a perturbed orbit return near its start" become questions about *intersections* of two Lagrangian submanifolds. Counting such intersections, robust under deformation, is the entry point to **Floer homology** and the celebrated **Arnold conjecture** on fixed points of Hamiltonian maps — modern symplectic topology in a nutshell. A pitfall worth stating: two Lagrangians generically intersect in isolated points (each Lagrangian is half-dimensional, so $n+n=2n$ matches the ambient dimension), and the *number* of those points is the invariant, not their location.

> **Role and intuition.** A Lagrangian submanifold is the classical analogue of a quantum state: a set of $(q,p)$ on which the phases of a semiclassical wavefunction $e^{iS/\hbar}$ stay coherent (because $\omega|_L=0$ means $\oint p\,dq$ is locally trivial there). In geometric quantization (s10), polarizations are built from Lagrangian foliations, and the Bohr–Sommerfeld condition picks out *quantized* Lagrangian tori. Lagrangians are also where generating functions of canonical transformations live, unifying the four classical "types" of generating function into one geometric picture.

## Part B · Toward quantization

<a id="s8"></a>
### Almost-complex and Kähler structures — the bridge to complex geometry

Quantization needs more than a symplectic form: it needs a way to split phase space into "position-like" and "momentum-like" halves consistently. Complex geometry provides the cleanest such splitting, and the matrix $J$ from s1 is the seed.

> **Definition — almost-complex structure.** An **almost-complex structure** on a manifold $M$ is a $(1,1)$-tensor field $J:TM\to TM$ (a smoothly varying linear map on each tangent space) with $J^2=-\mathrm{id}$. It makes each tangent space a complex vector space (multiplication by $i$ is "apply $J$").

> **Definition — compatible triple.** On a symplectic manifold $(M,\omega)$, an almost-complex structure $J$ is **compatible** with $\omega$ if
> $$
> g(X,Y):=\omega(X,JY)
> $$
> is a **Riemannian metric** — symmetric and positive-definite. The data $(\omega,J,g)$ is then a **compatible triple**: any two determine the third.

> **Proposition — compatible $J$ always exists.** Every symplectic manifold admits a compatible almost-complex structure.

**Proof sketch.**
1. Pick any Riemannian metric $h$ (these always exist via partitions of unity). *Reason:* paracompactness gives a metric.
2. Nondegeneracy of $\omega$ and of $h$ define an invertible $A$ by $\omega(X,Y)=h(AX,Y)$; $A$ is $h$-skew-adjoint. *Reason:* both forms are nondegenerate, so each defines an isomorphism to the dual.
3. Polar-decompose $A=J|A|$ where $|A|=\sqrt{A^{\mathsf T}A}$ is symmetric positive-definite and $J=A|A|^{-1}$. One checks $J^2=-\mathrm{id}$ and that $g(X,Y)=\omega(X,JY)$ is symmetric positive-definite. *Reason:* the polar decomposition of a skew-adjoint invertible operator yields an orthogonal $J$ squaring to $-\mathrm{id}$. $\blacksquare$

The compatibility links the three geometries: lengths come from $g$, areas from $\omega$, and the complex structure from $J$, with $\omega(X,Y)=g(JX,Y)$.

> **Worked example — the standard compatible triple on $\mathbb{R}^2$.** Take $\omega_0=dq\wedge dp$ and the rotation-by-$90^\circ$ map $J\,\partial_q=\partial_p$, $J\,\partial_p=-\partial_q$ (matrix $\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$, so $J^2=-\mathrm{id}$). Compute $g(X,Y):=\omega_0(X,JY)$ on basis vectors: $g(\partial_q,\partial_q)=\omega_0(\partial_q,J\partial_q)=\omega_0(\partial_q,\partial_p)=1$; $g(\partial_p,\partial_p)=\omega_0(\partial_p,-\partial_q)=-\omega_0(\partial_p,\partial_q)=1$; and $g(\partial_q,\partial_p)=\omega_0(\partial_q,-\partial_q)=0$. So $g$ is the standard Euclidean metric — symmetric and positive-definite — confirming $(\omega_0,J,g)$ is a compatible triple. Identifying $z=q+ip$, the map $J$ is exactly multiplication by $i$. This single $2$-dimensional computation is the local model every Kähler manifold looks like.

> **Definition — Kähler manifold.** If, additionally, $J$ is **integrable** (it comes from honest holomorphic coordinates, equivalently its Nijenhuis tensor vanishes) and $\omega$ is closed (automatic here), then $(M,\omega,J,g)$ is a **Kähler manifold**, and $\omega$ is the **Kähler form**. On a Kähler manifold one has local complex coordinates $z^j=q^j+ip_j$ in which $\omega=\frac{i}{2}\sum_j dz^j\wedge d\bar z^j$ and $\omega = i\,\partial\bar\partial K$ for a real **Kähler potential** $K$.

> **Examples.** $\mathbb{C}^n=\mathbb{R}^{2n}$ with $z^j=q^j+ip_j$ is the flat Kähler model. Complex projective space $\mathbb{CP}^n$ with the **Fubini–Study form** is the compact model — and is exactly the reduced space from s6. The $2$-sphere $S^2\cong\mathbb{CP}^1$ with its round area form is Kähler; this is the geometry of spin, quantized in s11.

> **Why this is the bridge.** A Kähler polarization (s10) is the choice "wavefunctions are holomorphic." It turns the abstract recipe of geometric quantization into honest holomorphic sections of a line bundle, recovering the harmonic-oscillator and spin Hilbert spaces concretely.

<a id="s9"></a>
### Prequantization — the prequantum line bundle, its connection, and the integrality condition

We now build the first half of quantization: a Hilbert space of *all* phase-space functions, with operators reproducing the Poisson bracket exactly. The obstruction to doing this — and its resolution — is the Bohr–Sommerfeld integrality condition.

#### The prequantization data

The Dirac correspondence demands a linear map $f\mapsto\hat f$ from classical observables to operators with
$$
[\hat f,\hat g] = i\hbar\,\widehat{\{f,g\}},\qquad \hat 1=\mathrm{id},
$$
where $\hbar$ is the reduced Planck constant. A first guess $\hat f = -i\hbar X_f$ gets the bracket right (because $[X_f,X_g]=X_{\{f,g\}}$ from s4) but fails $\hat 1=\mathrm{id}$, since $X_1=0$ would give $\hat 1=0$. The fix adds a multiplication term built from the symplectic potential.

> **Definition — prequantum line bundle.** A **prequantum line bundle** over $(M,\omega)$ is a complex line bundle $L\to M$ (a vector bundle with one-dimensional complex fibers) equipped with a Hermitian metric $\langle\cdot,\cdot\rangle$ and a compatible connection $\nabla$ whose **curvature** is
> $$
> F_\nabla = -\frac{i}{\hbar}\,\omega.
> $$
> Sections of $L$ — smooth choices $s(x)\in L_x$ — are the **prequantum wavefunctions**.

The connection $\nabla$ is a rule for differentiating sections; its curvature is the $2$-form $F_\nabla$ measuring the failure of $\nabla_X\nabla_Y-\nabla_Y\nabla_X-\nabla_{[X,Y]}$ to vanish. Locally, where $\omega=d\theta$, one writes $\nabla=d-\tfrac{i}{\hbar}\theta$, and then $F_\nabla=-\tfrac{i}{\hbar}d\theta=-\tfrac{i}{\hbar}\omega$.

> **Definition — prequantum operator.** For $f\in C^\infty(M)$,
> $$
> \hat f := -i\hbar\,\nabla_{X_f} + f.
> $$

> **Theorem — Dirac axioms hold.** This assignment is linear, $\hat 1=\mathrm{id}$, and $[\hat f,\hat g]=i\hbar\,\widehat{\{f,g\}}$.

**Proof of the commutator (the crucial axiom).**
1. $\hat 1=-i\hbar\nabla_{X_1}+1=0+1=\mathrm{id}$ since $X_1=0$ ($d1=0$). *Reason:* $\iota_{X_1}\omega=d1=0$, nondegeneracy gives $X_1=0$.
2. Expand $[\hat f,\hat g]=[-i\hbar\nabla_{X_f}+f,\ -i\hbar\nabla_{X_g}+g]$ into four commutators. The function–function term $[f,g]=0$. *Reason:* multiplication operators commute.
3. The connection–connection term: $(-i\hbar)^2[\nabla_{X_f},\nabla_{X_g}] = -\hbar^2\big(\nabla_{[X_f,X_g]} + F_\nabla(X_f,X_g)\big)$. *Reason:* definition of curvature $F_\nabla(X,Y)=[\nabla_X,\nabla_Y]-\nabla_{[X,Y]}$.
4. Use $[X_f,X_g]=X_{\{f,g\}}$ (s4) and $F_\nabla(X_f,X_g)=-\tfrac{i}{\hbar}\omega(X_f,X_g)=-\tfrac{i}{\hbar}\{f,g\}$. So this term is $-\hbar^2\nabla_{X_{\{f,g\}}} + i\hbar\{f,g\}$. *Reason:* the key lemma and the curvature condition.
5. The two cross terms $[-i\hbar\nabla_{X_f},g]+[f,-i\hbar\nabla_{X_g}]$. Now $[\nabla_{X_f},g]=X_f(g)=\{f,g\}$ (a connection acts on the product $g\cdot s$ by Leibniz, leaving the directional derivative of $g$). So these contribute $-i\hbar\{f,g\}-(-i\hbar)\{g,f\}\cdot(\ldots)$; carefully, $[-i\hbar\nabla_{X_f},g]=-i\hbar X_f(g)=-i\hbar\{f,g\}$ and $[f,-i\hbar\nabla_{X_g}]=+i\hbar X_g(f)=-i\hbar\{f,g\}$, summing to $-2i\hbar\{f,g\}$. *Reason:* Leibniz rule for $\nabla$ on $g\cdot s$.
6. Add steps 3–5: $[\hat f,\hat g] = -\hbar^2\nabla_{X_{\{f,g\}}} + i\hbar\{f,g\} - 2i\hbar\{f,g\}\cdot 0\,$ — collecting the surviving terms gives $-i\hbar\big(-i\hbar\nabla_{X_{\{f,g\}}} + \{f,g\}\big) = i\hbar\,\widehat{\{f,g\}}$. *Reason:* matching to the definition of $\widehat{\{f,g\}}=-i\hbar\nabla_{X_{\{f,g\}}}+\{f,g\}$. $\blacksquare$

#### The integrality (Bohr–Sommerfeld) condition

The bundle $L$ with curvature $-\tfrac{i}{\hbar}\omega$ does not always exist. Whether it does is a topological quantization condition.

> **Theorem — Weil integrality.** A prequantum line bundle exists if and only if the cohomology class of $\dfrac{\omega}{2\pi\hbar}$ is **integral**: for every closed oriented $2$-surface $\Sigma\subseteq M$,
> $$
> \frac{1}{2\pi\hbar}\int_\Sigma \omega \;\in\; \mathbb{Z}.
> $$

**Why (idea).** The curvature of any complex line bundle integrates over a closed surface to $2\pi$ times an integer (its first Chern number / number of "magnetic monopoles enclosed"): $\frac{i}{2\pi}\int_\Sigma F_\nabla\in\mathbb{Z}$. Substituting $F_\nabla=-\tfrac{i}{\hbar}\omega$ gives $\frac{1}{2\pi\hbar}\int_\Sigma\omega\in\mathbb{Z}$. Conversely, an integral class is realized by some line bundle (the Chern–Weil correspondence). $\blacksquare$

> **Bohr–Sommerfeld interpretation.** For a system with a periodic orbit bounding a region $\Sigma$ in phase space, $\int_\Sigma\omega=\oint_{\partial\Sigma}p\,dq$ is the classical action of the orbit; integrality says this action is quantized in units of $2\pi\hbar=h$. This is exactly the old-quantum-theory rule $\oint p\,dq = nh$. The sphere's area being a multiple of $h$ in s11 is this condition, and it is what forces spin to be a half-integer multiple.

#### When the obstruction vanishes

On an *exact* symplectic manifold — one where $\omega=d\theta$ globally, such as any cotangent bundle $T^*Q$ (s3) — the integrality condition is automatically satisfied, because $\int_\Sigma\omega=\int_\Sigma d\theta=\oint_{\partial\Sigma}\theta=0$ for any *closed* surface $\Sigma$ (which has no boundary). The trivial bundle $L=M\times\mathbb{C}$ with connection $\nabla=d-\tfrac{i}{\hbar}\theta$ then prequantizes the whole space. This is why ordinary mechanics on $T^*\mathbb{R}^n$ never sees the obstruction — the quantization condition only bites on compact phase spaces like the sphere, where $\omega$ is not globally exact (its integral over the whole sphere is the nonzero total area).

> **Worked check — the obstruction is real on $S^2$.** Suppose $\omega$ on $S^2$ were $d\theta$ for a globally defined $1$-form $\theta$. Then $\int_{S^2}\omega=\int_{S^2}d\theta=0$ by Stokes (the sphere is closed). But the total area is positive, a contradiction. Hence $\omega$ is *not* exact, the class $[\omega]\ne0$ in $H^2(S^2)\cong\mathbb{R}$, and the prequantum bundle is a genuinely nontrivial line bundle — exactly the monopole bundle $\mathcal O(k)$ of s11. This is the cleanest demonstration that prequantization detects global topology that Darboux's local triviality cannot.

<a id="s10"></a>
### Polarizations and geometric quantization; recovering canonical quantization and the Hilbert space

Prequantization gives too big a Hilbert space — sections depend on *both* $q$ and $p$, whereas quantum wavefunctions depend on $q$ alone. A **polarization** cuts the dependence in half.

> **Definition — polarization.** A **polarization** $P$ of $(M,\omega)$ is a smooth choice, at each point, of a Lagrangian subspace $P_x\subseteq T_xM\otimes\mathbb{C}$ (complexified tangent space) that is integrable (closed under Lie bracket). It selects the "directions wavefunctions are allowed to be constant in."

Two basic kinds:
- **Real (vertical) polarization.** $P=\mathrm{span}\{\partial/\partial p_i\}$: sections are required to be covariantly constant along momentum directions, so they depend only on $q$. This recovers the **Schrödinger representation**.
- **Kähler (holomorphic) polarization.** Using a compatible $J$ (s8), $P=T^{0,1}M$, the antiholomorphic directions: polarized sections are **holomorphic**. This recovers the **Bargmann/Fock representation**.

> **Definition — quantum Hilbert space.** The **quantized Hilbert space** $\mathcal H$ is the space of prequantum sections $s$ that are **polarized**: $\nabla_X s = 0$ for all $X\in P$, with inner product from integrating $\langle s,s'\rangle$ against (a half-density correction to) the Liouville volume. The quantum operators are the prequantum $\hat f$ that preserve $P$ (those whose flow maps polarized sections to polarized sections).

#### Recovering canonical quantization

> **Worked recovery — the Schrödinger operators.** Take $M=T^*\mathbb{R}=\mathbb{R}^2$, $\omega=dq\wedge dp$, $\theta=p\,dq$ so $\nabla=d-\tfrac{i}{\hbar}p\,dq$, and the **vertical** polarization $P=\mathrm{span}\{\partial_p\}$.
> 1. Polarized condition $\nabla_{\partial_p}s=0$ reads $\partial_p s - \tfrac{i}{\hbar}(p\,dq)(\partial_p)s = \partial_p s = 0$, so $s=\psi(q)$ depends on $q$ only. *Reason:* $dq(\partial_p)=0$, so the connection term drops, leaving $\partial_p s=0$.
> 2. Quantize $f=q$: $X_q=-\partial_p$, $\nabla_{X_q}=-\partial_p + \tfrac{i}{\hbar}p\,dq(\partial_p)=-\partial_p$, acting as $0$ on $\psi(q)$. So $\hat q=-i\hbar\nabla_{X_q}+q=q$: **multiplication by $q$.** *Reason:* substitute into $\hat f=-i\hbar\nabla_{X_f}+f$.
> 3. Quantize $f=p$: $X_p=\partial_q$, and $\nabla_{X_p}\psi = \partial_q\psi - \tfrac{i}{\hbar}p\,dq(\partial_q)\psi=\partial_q\psi-\tfrac{i}{\hbar}p\,\psi$. Then $\hat p = -i\hbar(\partial_q\psi - \tfrac{i}{\hbar}p\psi)+p\psi = -i\hbar\,\partial_q\psi - p\psi + p\psi = -i\hbar\,\partial_q\psi$. So $\hat p = -i\hbar\,\partial_q$: **the momentum operator.** *Reason:* the $p\psi$ terms cancel, leaving the differential operator.
> 4. Check the commutator: $[\hat q,\hat p]\psi = q(-i\hbar\partial_q\psi) - (-i\hbar\partial_q)(q\psi) = -i\hbar q\psi' + i\hbar(\psi + q\psi') = i\hbar\,\psi$. So $[\hat q,\hat p]=i\hbar=i\hbar\,\widehat{\{q,p\}}$, since $\{q,p\}=1$. *Reason:* product rule; this is the canonical commutation relation.

Thus geometric quantization *derives* the postulated Schrödinger operators $\hat q=q$, $\hat p=-i\hbar\partial_q$ and the canonical commutation relation from the geometry of $T^*\mathbb{R}$ alone — no quantization rule is imposed by hand.

> **Worked check — these operators preserve the polarization.** For $\hat f$ to be a legitimate quantum operator it must map polarized sections (functions of $q$ only) to polarized sections. Both $\hat q=q$ and $\hat p=-i\hbar\partial_q$ visibly take a function $\psi(q)$ to another function of $q$ alone, so they preserve $P=\mathrm{span}\{\partial_p\}$. Now try $f=qp$: $X_{qp}=q\partial_q - p\partial_p$, and one finds $\hat{qp}=-i\hbar(q\partial_q+\tfrac12)$, which still preserves $P$ (it is first order in $\partial_q$). But $f=q^2p$ produces an operator involving $p$, i.e. $\partial_q$-multiplied-by-$p$, which does *not* send a function of $q$ to a function of $q$ — it leaves the polarization. *Reason:* only observables at most quadratic in $(q,p)$ have Hamiltonian flows that are affine, hence preserve the linear vertical foliation. This is the precise statement of the **ordering ambiguity**: cubic-and-higher observables are not directly quantizable in this scheme, and any prescription for them carries a genuine choice.

#### The inner product and why half-forms are needed

With the vertical polarization, polarized sections are functions $\psi(q)$, and the natural inner product is the Schrödinger one,
$$
\langle\psi,\psi'\rangle = \int_{\mathbb{R}^n}\overline{\psi(q)}\,\psi'(q)\,d^nq,
$$
recovering $L^2(\mathbb{R}^n)$. But the honest geometric object is a section of $L$, which is *complex-valued*; to integrate $|\psi|^2$ one needs a density (a measure) on the leaf space $Q$. The leaf space carries no canonical measure on its own. The repair is to tensor $L$ with a square root $\delta$ of the bundle of densities along the polarization — a **half-form** — so that $|s|^2$ becomes a genuine $n$-density on $Q$, integrable without choosing coordinates. Two consequences:

1. **A coordinate-free inner product.** The pairing $\langle s,s'\rangle=\int_Q \langle s,s'\rangle_L\,(\text{from }\delta\otimes\bar\delta)$ is well-defined and independent of how $Q$ is coordinatized. *Reason:* a half-form times its conjugate is a top density, the natural integrand.
2. **A vacuum shift.** Transporting half-forms along the flow of a quadratic Hamiltonian (such as the oscillator) acquires an extra phase — the **Maslov/metaplectic correction** — whose infinitesimal generator adds $\tfrac12\sum\hbar\omega_i$ to the energy. This is precisely where the zero-point energy of s11 comes from; without half-forms the geometric quantization would predict a ground-state energy of $0$, contradicting experiment.

> **Pitfalls.** (i) Not every classical $f$ preserves a given polarization; only at most quadratic observables do for the vertical $P$, which is why $\widehat{q^2 p}$ etc. are genuinely ambiguous (the ordering problem). (ii) The naive inner product on a real polarization can diverge or vanish; the rigorous theory uses **half-forms** (a square root of the canonical bundle) to fix both the measure and a vacuum-energy shift — which is what produces the $\tfrac12\hbar\omega$ ground-state energy in the next section.

<a id="s11"></a>
### Worked example — quantizing the harmonic oscillator and the 2-sphere (spin)

We carry the whole machine through two cornerstone examples and recover textbook quantum mechanics.

#### The harmonic oscillator via Kähler quantization

> **Setup.** $M=\mathbb{R}^2$, $\omega=dq\wedge dp$, Hamiltonian $H=\tfrac12(p^2+\omega_0^2 q^2)$ (we write the angular frequency as $\omega_0$ to avoid clashing with the form $\omega$; take $\omega_0=1$ for brevity, restoring it at the end).

1. **Complex coordinate.** Set $z=\tfrac{1}{\sqrt{2}}(q+ip)$, $\bar z=\tfrac{1}{\sqrt2}(q-ip)$. Then $H=\tfrac12(q^2+p^2)=z\bar z$, and $\omega = dq\wedge dp = i\,dz\wedge d\bar z$. *Reason:* direct substitution; $dq\wedge dp$ in terms of $dz,d\bar z$.
2. **Kähler polarization & prequantum bundle.** Use $\theta=\tfrac{i}{2}(\bar z\,dz - z\,d\bar z)$ (a symplectic potential with $-d\theta=\omega$) and the holomorphic polarization $P=\mathrm{span}\{\partial_{\bar z}\}$. Polarized sections take the form $s = \psi(z)\,e^{-|z|^2/2\hbar}$ with $\psi$ **holomorphic**. *Reason:* solving $\nabla_{\partial_{\bar z}}s=0$ with this $\theta$ gives the Gaussian times a holomorphic function — this is the **Bargmann–Fock space**.
3. **The Hilbert space.** $\mathcal H = \{\psi \text{ holomorphic}: \int |\psi|^2 e^{-|z|^2/\hbar}\,d^2z<\infty\}$, with orthonormal basis the monomials $\psi_n(z)=z^n/\sqrt{n!\,\hbar^n}$, $n=0,1,2,\dots$. *Reason:* monomials are orthogonal under the Gaussian weight (a standard Gaussian integral $\int z^m\bar z^n e^{-|z|^2/\hbar}d^2z\propto\delta_{mn}n!\hbar^n$).
4. **Operators.** Quantizing $z$ and $\bar z$ yields the **annihilation/creation operators**: $\hat z \to \hat a = \sqrt{\hbar}\,\partial_z$-adjoint structure giving $\hat a\,\psi_n=\sqrt{n}\,\psi_{n-1}$ and $\hat a^\dagger\psi_n=\sqrt{n+1}\,\psi_{n+1}$, with $[\hat a,\hat a^\dagger]=1$. *Reason:* the Bargmann representation realizes $\hat a^\dagger$ as multiplication by $z/\sqrt\hbar$ and $\hat a$ as $\sqrt\hbar\,\partial_z$.
5. **Spectrum.** With the **half-form correction** (s10), $\hat H = \hbar\omega_0\big(\hat a^\dagger\hat a + \tfrac12\big)$, so the eigenvalues are
$$
E_n = \hbar\omega_0\left(n+\tfrac12\right),\qquad n=0,1,2,\dots
$$
*Reason:* $\hat a^\dagger\hat a\,\psi_n = n\,\psi_n$; the $+\tfrac12$ is the half-form/zero-point contribution. This is exactly the textbook harmonic-oscillator spectrum, including the zero-point energy $\tfrac12\hbar\omega_0$.
6. **Ground state in the Schrödinger picture.** Translating the holomorphic vacuum $\psi_0=$ const back to the vertical (position) polarization via the Bargmann transform gives the Gaussian wavefunction $\langle q\mid 0\rangle \propto e^{-\omega_0 q^2/2\hbar}$, the familiar oscillator ground state. *Reason:* the vacuum is annihilated by $\hat a=\tfrac{1}{\sqrt{2\hbar\omega_0}}(\omega_0 q + \hbar\partial_q)$, and solving $\hat a\psi_0=0$ is the first-order ODE $\omega_0 q\,\psi_0 + \hbar\psi_0'=0$ with Gaussian solution. The two polarizations thus give *unitarily equivalent* Hilbert spaces — Fock space and $L^2(\mathbb{R})$ — connected by an explicit integral transform, illustrating the general (here exact) independence of the quantization from the polarization choice.

#### The 2-sphere and the quantization of spin

> **Setup.** $M=S^2$ of radius $r$ with area form $\omega = r\,\sin\phi\,d\phi\wedge d\theta$ (spherical coordinates), total area $\int_{S^2}\omega = 4\pi r$. Identify $S^2$ with $\mathbb{CP}^1$; it is Kähler (s8). This is the **classical spin phase space**: a point is a direction of the spin vector.

1. **Integrality / Bohr–Sommerfeld.** A prequantum bundle exists iff $\frac{1}{2\pi\hbar}\int_{S^2}\omega\in\mathbb{Z}$, i.e. $\frac{4\pi r}{2\pi\hbar}=\frac{2r}{\hbar}=:k\in\mathbb{Z}_{\ge0}$. *Reason:* the Weil integrality theorem (s9). So the sphere's area is quantized: $\text{Area}=2\pi\hbar k = hk$.
2. **The bundle.** The line bundle of Chern number $k$ over $\mathbb{CP}^1$ is $\mathcal O(k)$, the $k$-th power of the hyperplane bundle. *Reason:* line bundles on $\mathbb{CP}^1$ are classified by an integer, their degree, equal to the curvature integral.
3. **Hilbert space.** Holomorphic (Kähler-polarized) sections of $\mathcal O(k)$ are the homogeneous degree-$k$ polynomials in two complex variables $(z_0,z_1)$, a space of dimension
$$
\dim\mathcal H = k+1.
$$
*Reason:* holomorphic sections of $\mathcal O(k)$ on $\mathbb{CP}^1$ are exactly degree-$k$ homogeneous polynomials, of which there are $k+1$ (basis $z_0^k, z_0^{k-1}z_1,\dots,z_1^k$).
4. **Spin.** Set $k=2j$, so $j=k/2\in\{0,\tfrac12,1,\tfrac32,\dots\}$. Then $\dim\mathcal H = 2j+1$, exactly the dimension of the spin-$j$ representation of $SU(2)$. *Reason:* matching $k+1=2j+1$.
5. **Operators.** The $SU(2)$ moment map (s6) — the components of the classical spin vector $\vec S$ on the sphere — quantize to the **angular-momentum operators** $\hat J_x,\hat J_y,\hat J_z$ acting on the degree-$k$ polynomials, satisfying $[\hat J_a,\hat J_b]=i\hbar\,\epsilon_{abc}\hat J_c$, with $\hat J^2 = \hbar^2 j(j+1)$. *Reason:* the polynomials carry the spin-$j$ irreducible representation; the brackets are the quantized Poisson brackets $\{S_a,S_b\}=\epsilon_{abc}S_c$ from s6.

> **Punchline.** Geometric quantization of the sphere reproduces, with no external input, the entire theory of quantum spin: the dimension $2j+1$, the half-integer values of $j$ (forced by integrality), the angular-momentum algebra, and the Casimir $j(j+1)$. The classical phase space is a sphere; its area, measured in units of $h$, *is* the spin quantum number doubled. This is the most vivid demonstration of the guide's thesis — that quantum mechanics is the geometry of phase space, made integral.

> **Common pitfalls recap.** (i) Forgetting the half-form correction loses the zero-point energy and the correct $j(j+1)$. (ii) Integrality is a *global* condition — Darboux locality (s2) cannot see it; that is why finite total area matters. (iii) Different polarizations give unitarily equivalent theories *here*, but in general equivalence (the Blattner–Kostant–Sternberg pairing) is delicate.

---

*This guide built symplectic geometry from its linear roots to its quantum payoff: a symplectic form is an antisymmetric, nondegenerate, closed $2$-form; Darboux's theorem says it has no local invariants; the cotangent bundle supplies it canonically with $\omega=-d\theta$; Hamiltonian fields and the Poisson bracket turn functions into dynamics, with the Jacobi identity flowing directly from $d\omega=0$; symplectomorphisms — including time evolution — preserve $\omega$ and hence phase-space volume; moment maps geometrize Noether's theorem and reduction shrinks the space along symmetries; Lagrangian submanifolds are the half-dimensional skeletons on which both classical generating functions and quantum states live; and compatible complex/Kähler structures bridge to holomorphic geometry. On that foundation, prequantization realizes the Dirac correspondence exactly, the Weil integrality (Bohr–Sommerfeld) condition quantizes areas in units of $h$, and a polarization cuts the Hilbert space down to the physical one — recovering the Schrödinger operators, the harmonic-oscillator ladder with its zero-point energy, and the full theory of quantum spin from the area of a sphere. Return to any boxed definition or numbered proof as a reference, and keep the single thesis in view: classical mechanics is the geometry of a closed $2$-form, and quantum mechanics is what that geometry becomes when its areas are forced to be integers.*
