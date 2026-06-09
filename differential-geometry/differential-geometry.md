**English** · [中文](differential-geometry.zh.md)

# Differential Geometry & Tensors, *the language of general relativity.*

*A self-contained, rigorous first course in the geometry of smooth spaces. We start with the bare idea of a manifold — a space that looks like flat $\mathbb{R}^n$ up close — and build, step by step, to the machinery Einstein needed: tangent spaces, tensors, the metric, connections, curvature, and finally the field equations of general relativity. Throughout, geometry is the goal and physics is the motivation; every formula is derived, every index is explained.*

[← Back to all guides](../README.md)

**Prerequisites.** This guide assumes the **Linear Algebra** guide (vector spaces, dual spaces, bilinear forms, determinants) and the **Multivariable/vector calculus** guide (partial derivatives, the chain rule, the Jacobian, line and surface integrals). We restate the specific facts we borrow as we use them.

## Part A · Smooth spaces and their calculus

<a id="s0"></a>
### Motivation — curved spacetime and coordinate-free physics

Differential geometry is the mathematics of *smoothly curved spaces*. The motivating question of this guide is physical: how do we do calculus — derivatives, integrals, conservation laws — on a space that is not flat $\mathbb{R}^n$, and how do we write physical laws so they do not secretly depend on the coordinate grid we happened to draw?

#### What problem are we solving?

Vector calculus, as developed in the prerequisite guide, lives on $\mathbb{R}^n$ with a fixed Cartesian coordinate system and a fixed notion of "the same direction at different points." Two facts about $\mathbb{R}^n$ are quietly doing all the work there:

1. **Global coordinates.** Every point has a single set of numbers $(x^1,\dots,x^n)$ that labels it, valid everywhere at once.
2. **A canonical way to compare vectors at different points.** A vector at the point $p$ and a vector at a far-away point $q$ both live in copies of $\mathbb{R}^n$ that we silently identify, so "the gradient is constant" or "this vector field is uniform" makes sense.

Neither fact survives on a curved space. On the surface of the Earth there is *no* single coordinate chart without a singularity (every flat map of the globe distorts or tears somewhere). And there is no coordinate-independent way to say a wind vector in Tokyo "points the same way" as one in London: the surface curves between them.

General relativity makes this concrete. Einstein's insight was that **gravity is not a force but the curvature of spacetime**, and that the laws of physics must take the same form in every coordinate system — there is no preferred frame. To express such laws we need objects that transform predictably when we change coordinates (these are **tensors**), a notion of distance built into the space itself (the **metric**), and a way to differentiate that respects curvature (the **covariant derivative**). Curvature, encoded in the **Riemann tensor**, is what bends the paths of freely falling bodies; the **Einstein field equations** tie that curvature to the matter and energy present.

#### The plan

We will build, in order: **manifolds** (the spaces, s1), **tangent vectors** (the infinitesimal arrows, s2), **vector fields and covectors** (s3), **tensors** (the transforming multilinear objects, s4), the **metric** (geometry: lengths and angles, s5), **differential forms** and integration (s6–s7), the **connection and covariant derivative** (s8), **geodesics** (straightest paths, s9), **curvature** (s10–s11), the **Einstein equations** (s12), and finally **symmetries** via Lie derivatives and Killing vectors (s13).

> **Intuition.** Keep two pictures in mind. *Locally* a manifold is indistinguishable from flat space — calculus works as usual in any one chart. *Globally* the charts must be stitched together, and the stitching is where curvature hides. Tensor calculus is the bookkeeping that keeps local computations consistent with the global, coordinate-free truth.

<a id="s1"></a>
### Manifolds — charts, atlases, and smooth structure

A manifold is the precise notion of "a space that looks like $\mathbb{R}^n$ when you zoom in." The surface of a sphere, the torus, the configuration space of a robot arm, and spacetime are all manifolds.

#### Charts and atlases

> **Definition — topological manifold.**
>
> An $n$-dimensional **topological manifold** $M$ is a topological space (a set with a notion of open sets) that is **Hausdorff** (distinct points have disjoint open neighborhoods), **second countable** (it has a countable base of open sets), and **locally Euclidean of dimension $n$**: every point $p\in M$ has an open neighborhood $U$ and a homeomorphism $\varphi: U \to \varphi(U)\subseteq \mathbb{R}^n$ onto an open subset of $\mathbb{R}^n$. The pair $(U,\varphi)$ is a **chart**; the component functions $\varphi(p)=(x^1(p),\dots,x^n(p))$ are **local coordinates**.

A homeomorphism is a continuous bijection with continuous inverse, so a chart is a continuous, invertible labeling of a patch of $M$ by $n$ real numbers. The number $n$ is the **dimension**.

> **Definition — atlas and transition maps.**
>
> An **atlas** is a collection of charts $\{(U_\alpha,\varphi_\alpha)\}$ whose domains cover $M$, i.e. $\bigcup_\alpha U_\alpha = M$. Where two charts overlap, $U_\alpha\cap U_\beta\ne\varnothing$, the **transition map**
>
> $$
> \varphi_\beta\circ\varphi_\alpha^{-1}:\ \varphi_\alpha(U_\alpha\cap U_\beta)\ \to\ \varphi_\beta(U_\alpha\cap U_\beta)
> $$
>
> is a map between open subsets of $\mathbb{R}^n$ — an honest function of $n$ real variables.

The transition map says how the two coordinate grids relate on the overlap. It is the object on which we impose smoothness.

> **Definition — smooth manifold.**
>
> A **smooth ($C^\infty$) structure** on $M$ is an atlas all of whose transition maps are infinitely differentiable as maps $\mathbb{R}^n\to\mathbb{R}^n$, and which is *maximal* (contains every chart compatible with it). A **smooth manifold** is a topological manifold with a chosen smooth structure. A function $f:M\to\mathbb{R}$ is **smooth** if for every chart $(U,\varphi)$ the composite $f\circ\varphi^{-1}:\varphi(U)\to\mathbb{R}$ is smooth in the ordinary calculus sense. We write $C^\infty(M)$ for the set of smooth real functions on $M$.

Why demand smooth transition maps? Because we want to define derivatives on $M$ *through charts*, and the answer must not depend on which chart we use. The chain rule guarantees consistency exactly when the transition maps are differentiable. This is the recurring theme: **a geometric object on $M$ is a chart-wise description plus a rule for how the description changes under transition maps**, such that the two always agree.

#### Worked example — the 2-sphere with two charts

Let $S^2=\{(X,Y,Z)\in\mathbb{R}^3 : X^2+Y^2+Z^2=1\}$, the unit sphere. We exhibit a two-chart smooth atlas using **stereographic projection**.

Let $N=(0,0,1)$ be the north pole and $S=(0,0,-1)$ the south pole.

1. **Chart from the north.** On $U_N = S^2\setminus\{N\}$ define $\varphi_N$ by projecting from $N$ onto the plane $Z=0$. A line from $N=(0,0,1)$ through $(X,Y,Z)$ meets $Z=0$ at
   $$
   \varphi_N(X,Y,Z) = (u,v) = \left(\frac{X}{1-Z},\ \frac{Y}{1-Z}\right).
   $$
   This is defined because $Z\ne 1$ on $U_N$, so $1-Z\ne 0$. It is a homeomorphism onto all of $\mathbb{R}^2$, with inverse obtained by intersecting the line with the sphere.
2. **Chart from the south.** On $U_S = S^2\setminus\{S\}$ define $\varphi_S$ by projecting from $S=(0,0,-1)$:
   $$
   \varphi_S(X,Y,Z) = (a,b) = \left(\frac{X}{1+Z},\ \frac{Y}{1+Z}\right),
   $$
   defined because $Z\ne -1$ on $U_S$.
3. **The domains cover $S^2$.** Every point fails to be in at most one of $U_N,U_S$ (only $N\notin U_N$, only $S\notin U_S$), and $N\ne S$, so $U_N\cup U_S = S^2$.
4. **The transition map.** On the overlap $U_N\cap U_S = S^2\setminus\{N,S\}$ we compute $\varphi_S\circ\varphi_N^{-1}$. A standard computation (substitute the inverse of $\varphi_N$ into $\varphi_S$, using $X^2+Y^2+Z^2=1$) gives the clean result
   $$
   (a,b) = \frac{(u,v)}{u^2+v^2}.
   $$
   This is **inversion in the unit circle**. On the overlap we have $(u,v)\ne(0,0)$ (the origin corresponds to the south pole $S$, excluded), so $u^2+v^2>0$ and the map is smooth — indeed each component is a ratio of polynomials with nonvanishing denominator, hence $C^\infty$ by the quotient rule.

Because the single transition map is smooth, $\{(U_N,\varphi_N),(U_S,\varphi_S)\}$ is a smooth atlas, making $S^2$ a smooth 2-manifold. Two charts genuinely are needed: no single chart can cover all of $S^2$, because $S^2$ is compact while any homeomorphic image in $\mathbb{R}^2$ would be open and bounded-or-not, and one can show $S^2$ is not homeomorphic to any open subset of $\mathbb{R}^2$.

> **Common pitfall.** Coordinates are *not* the manifold. The point $N$ is a perfectly good point of $S^2$; it merely has no $(u,v)$ label. A "coordinate singularity" like this is an artifact of the chart, not of the space. Spacetime singularities versus coordinate singularities is exactly this distinction in physics (the Schwarzschild horizon is a coordinate artifact; the central singularity is real).

<a id="s2"></a>
### Tangent vectors and the tangent space

At each point of a manifold we want a vector space of "infinitesimal directions" — the **tangent space**. On a surface in $\mathbb{R}^3$ this is the familiar tangent plane. But a manifold has no surrounding space to lean on, so we need an intrinsic definition.

#### Two equivalent pictures

There are two standard intrinsic definitions; we use both and show they agree.

> **Definition — tangent vector via curves.**
>
> A **smooth curve through $p$** is a smooth map $\gamma:(-\varepsilon,\varepsilon)\to M$ with $\gamma(0)=p$. Two curves are **equivalent at $p$** if in some (equivalently every) chart $\varphi$ around $p$ their coordinate velocities agree: $\tfrac{d}{dt}\big(\varphi\circ\gamma_1\big)(0) = \tfrac{d}{dt}\big(\varphi\circ\gamma_2\big)(0)$. A **tangent vector at $p$** is an equivalence class of curves.

The chain rule makes "every chart" equivalent to "some chart": under a transition map $\psi=\varphi_\beta\circ\varphi_\alpha^{-1}$, the velocity transforms by the Jacobian $D\psi$, which is invertible, so the velocities of two curves agree in one chart iff they agree in all.

> **Definition — tangent vector as a derivation.**
>
> A **derivation at $p$** is a linear map $v:C^\infty(M)\to\mathbb{R}$ satisfying the **Leibniz (product) rule**
>
> $$
> v(fg) = v(f)\,g(p) + f(p)\,v(g)\qquad\text{for all }f,g\in C^\infty(M).
> $$
>
> The **tangent space** $T_pM$ is the set of all derivations at $p$. It is a real vector space under $(v+w)(f)=v(f)+w(f)$ and $(cv)(f)=c\,v(f)$.

The motivation: a tangent vector should let you take a *directional derivative* of any function. Given a curve $\gamma$ representing a direction, define $v(f) = \tfrac{d}{dt}f(\gamma(t))\big|_{0}$. Linearity is clear; the Leibniz rule is the ordinary product rule for $\tfrac{d}{dt}\big(f(\gamma)g(\gamma)\big)$.

#### The coordinate basis

Fix a chart $\varphi=(x^1,\dots,x^n)$ around $p$. Define $n$ derivations: for $\mu=1,\dots,n$,
$$
\left.\frac{\partial}{\partial x^\mu}\right|_p (f) \;=\; \frac{\partial (f\circ\varphi^{-1})}{\partial x^\mu}\Big|_{\varphi(p)} ,
$$
the ordinary partial derivative of the chart-expression of $f$. We abbreviate $\partial_\mu := \partial/\partial x^\mu$.

> **Theorem — the coordinate basis.**
>
> The derivations $\partial_1|_p,\dots,\partial_n|_p$ form a basis of $T_pM$; hence $\dim T_pM = n = \dim M$.

*Proof.*
1. **They span.** Let $v\in T_pM$ and let $f\in C^\infty(M)$. Work in coordinates centered at $p$ (so $\varphi(p)=0$). By **Taylor's theorem with integral remainder** applied to $f\circ\varphi^{-1}$, there exist smooth functions $g_\mu$ with $g_\mu(0)=\partial_\mu(f\circ\varphi^{-1})(0)$ such that, in coordinates, $f = f(p) + \sum_\mu x^\mu\, g_\mu$. Apply $v$: linearity gives $v(f) = v(f(p)) + \sum_\mu v(x^\mu g_\mu)$. The constant $f(p)$ has $v(\text{const})=0$ (apply Leibniz to $1=1\cdot 1$: $v(1)=v(1)+v(1)$, so $v(1)=0$, hence $v(c)=0$). By Leibniz, $v(x^\mu g_\mu)=v(x^\mu)g_\mu(p)+x^\mu(p)v(g_\mu)$, and $x^\mu(p)=0$, so this is $v(x^\mu)\,\partial_\mu f|_p$. Therefore $v(f)=\sum_\mu v(x^\mu)\,\partial_\mu|_p(f)$, i.e. $v=\sum_\mu v(x^\mu)\,\partial_\mu|_p$. So the $\partial_\mu$ span.
2. **They are independent.** Suppose $\sum_\mu c^\mu \partial_\mu|_p = 0$ as a derivation. Apply it to the coordinate function $x^\nu$: $\partial_\mu|_p(x^\nu) = \delta^\nu_\mu$ (the partial of $x^\nu$ with respect to $x^\mu$). So $0 = \sum_\mu c^\mu \delta^\nu_\mu = c^\nu$ for each $\nu$. All coefficients vanish.

Hence the $\partial_\mu$ are a basis. $\blacksquare$

We write a general tangent vector as $v = v^\mu \partial_\mu$ using the **Einstein summation convention** (introduced fully in s4): a repeated index, once up and once down, is summed over $1,\dots,n$. The numbers $v^\mu = v(x^\mu)$ are the **components** of $v$ in this chart.

#### How components transform

If $\tilde x^\nu$ is another chart, the chain rule gives $\partial_\mu = \dfrac{\partial \tilde x^\nu}{\partial x^\mu}\,\tilde\partial_\nu$, and matching $v=v^\mu\partial_\mu = \tilde v^\nu \tilde\partial_\nu$ yields the **contravariant transformation law**
$$
\tilde v^\nu = \frac{\partial \tilde x^\nu}{\partial x^\mu}\, v^\mu .
$$
This is the prototype "vector" transformation; an object whose components transform this way (with the *upper* Jacobian) is **contravariant**, marked by an upper index.

> **Worked example — the sphere's tangent space.** On $S^2$ in the north chart $(u,v)$, the velocity of the curve $\gamma(t)=\varphi_N^{-1}(t,0)$ at $t=0$ is the basis vector $\partial_u|_p$. A tangent vector $3\partial_u - \partial_v$ has components $(v^u,v^v)=(3,-1)$; it is a genuine arrow in the tangent plane to the sphere, expressed without ever leaving the surface.

<a id="s3"></a>
### Vector fields, the pushforward, and covectors (one-forms)

Now we attach a tangent vector to *every* point, learn how maps move tangent vectors, and meet the dual objects — covectors.

#### Vector fields

> **Definition — vector field.**
>
> A **(smooth) vector field** $X$ assigns to each $p\in M$ a tangent vector $X_p\in T_pM$, smoothly: in any chart, $X = X^\mu(x)\,\partial_\mu$ with smooth component functions $X^\mu$. Equivalently $X$ acts on a function to give a function: $(Xf)(p)=X_p(f)\in\mathbb{R}$, and $Xf\in C^\infty(M)$.

Vector fields can be added, scaled by functions, and — crucially — multiplied via the **Lie bracket** $[X,Y]f := X(Yf)-Y(Xf)$, which is again a vector field (the second-order terms cancel by equality of mixed partials). We return to the bracket in s13.

#### The differential (pushforward) of a map

> **Definition — pushforward / differential.**
>
> Let $F:M\to N$ be smooth and $p\in M$. The **differential** (or **pushforward**) $dF_p = F_{*p}:T_pM\to T_{F(p)}N$ is defined on a tangent vector $v$ (as a derivation) by
>
> $$
> \big(dF_p(v)\big)(g) = v(g\circ F)\qquad\text{for } g\in C^\infty(N).
> $$

In the curve picture this is the natural thing: if $v=[\gamma]$ then $dF_p(v)=[F\circ\gamma]$ — the velocity of the image curve. In coordinates $x^\mu$ on $M$ and $y^a$ on $N$, with $F$ given by $y^a=F^a(x)$, the matrix of $dF_p$ is the **Jacobian** $\partial F^a/\partial x^\mu$:
$$
\big(dF_p(v)\big)^a = \frac{\partial F^a}{\partial x^\mu}\, v^\mu .
$$
*Why:* apply the definition to $g=y^a$ and use the chain rule. The pushforward is the coordinate-free version of the Jacobian. (Pulling vectors *back* is generally impossible unless $F$ is invertible; but functions and covectors pull back freely, which is why covectors are so useful.)

#### Covectors and the cotangent space

> **Definition — cotangent space and covectors.**
>
> The **cotangent space** $T_p^*M$ is the dual vector space of $T_pM$: the set of linear maps $\omega:T_pM\to\mathbb{R}$. Its elements are **covectors** (also **one-forms** at a point, or **covariant vectors**).

Recall from linear algebra: the dual of an $n$-dimensional space is $n$-dimensional, and a basis $\{e_\mu\}$ of $V$ induces a **dual basis** $\{e^\mu\}$ of $V^*$ defined by $e^\mu(e_\nu)=\delta^\mu_\nu$.

> **Definition — the differential of a function, and the dual basis $dx^\mu$.**
>
> For $f\in C^\infty(M)$, its **differential** $df_p\in T_p^*M$ is the covector $df_p(v) = v(f)$. Applied to the coordinate functions $x^\mu$, this gives covectors $dx^\mu$ with
>
> $$
> dx^\mu(\partial_\nu) = \partial_\nu(x^\mu) = \delta^\mu_\nu .
> $$

So $\{dx^\mu\}$ is exactly the dual basis to the coordinate basis $\{\partial_\mu\}$. Every covector is $\omega = \omega_\mu\, dx^\mu$ with components $\omega_\mu=\omega(\partial_\mu)$ (lower index). For a function, $df = \partial_\mu f\, dx^\mu$ — the differential is the gradient written invariantly.

#### How covector components transform

From $dx^\mu = \dfrac{\partial x^\mu}{\partial \tilde x^\nu} d\tilde x^\nu$ and matching components, the **covariant transformation law** is
$$
\tilde\omega_\nu = \frac{\partial x^\mu}{\partial \tilde x^\nu}\,\omega_\mu .
$$
Compare with the contravariant law for vectors: a covector transforms with the *inverse* Jacobian (lower index), a vector with the *direct* Jacobian (upper index). This opposite behavior is precisely why the pairing $\omega(v)=\omega_\mu v^\mu$ is **coordinate-independent**: the two Jacobians multiply to the identity by the chain rule $\frac{\partial x^\mu}{\partial \tilde x^\nu}\frac{\partial \tilde x^\nu}{\partial x^\rho}=\delta^\mu_\rho$. This invariance is the seed of all tensor calculus.

## Part B · Tensors and the metric

<a id="s4"></a>
### Tensors — transformation law, index notation, the metric of bookkeeping

A tensor is a multilinear object built from copies of the tangent and cotangent spaces. Tensors are the gadgets of which physical laws are made, because their transformation law makes equations between them hold in *all* coordinate systems at once.

#### Definition

> **Definition — tensor at a point.**
>
> A **tensor of type $(k,l)$** at $p$ is a multilinear map
>
> $$
> T:\ \underbrace{T_p^*M\times\cdots\times T_p^*M}_{k}\ \times\ \underbrace{T_pM\times\cdots\times T_pM}_{l}\ \longrightarrow\ \mathbb{R},
> $$
>
> linear in each of its $k+l$ slots. A **tensor field** assigns such a tensor smoothly to each point.

Examples: a $(1,0)$-tensor eats one covector and is just a vector (by double duality $V^{**}\cong V$); a $(0,1)$-tensor is a covector; a $(0,2)$-tensor is a bilinear form (the metric will be one).

#### Components and index notation

Feed basis elements into the slots to get **components**. For a $(k,l)$-tensor,
$$
T^{\mu_1\cdots\mu_k}{}_{\nu_1\cdots\nu_l} = T\big(dx^{\mu_1},\dots,dx^{\mu_k},\,\partial_{\nu_1},\dots,\partial_{\nu_l}\big).
$$
Upper indices ("contravariant slots") pair with covector arguments; lower indices ("covariant slots") with vector arguments. The whole tensor is recovered as
$$
T = T^{\mu_1\cdots\mu_k}{}_{\nu_1\cdots\nu_l}\ \partial_{\mu_1}\otimes\cdots\otimes\partial_{\mu_k}\otimes dx^{\nu_1}\otimes\cdots\otimes dx^{\nu_l},
$$
where $\otimes$ is the tensor product from linear algebra.

> **Einstein summation convention.** An index that appears exactly **twice in a single term, once up and once down, is automatically summed** over $1,\dots,n$; the summation sign is dropped. Such an index is **contracted** (or "dummy") and may be renamed freely. A non-repeated index is **free** and must match on both sides of an equation. Example: $\omega_\mu v^\mu$ means $\sum_{\mu=1}^n \omega_\mu v^\mu$; the equation $w^\mu = A^\mu{}_\nu v^\nu$ has free index $\mu$ and summed index $\nu$.

#### The transformation law

The defining property — what makes a tensor a tensor — is how components change under a chart change. Each upper index brings a factor $\partial\tilde x/\partial x$ (like a vector) and each lower index a factor $\partial x/\partial\tilde x$ (like a covector):
$$
\tilde T^{\alpha_1\cdots\alpha_k}{}_{\beta_1\cdots\beta_l}
= \frac{\partial \tilde x^{\alpha_1}}{\partial x^{\mu_1}}\cdots\frac{\partial \tilde x^{\alpha_k}}{\partial x^{\mu_k}}\,
\frac{\partial x^{\nu_1}}{\partial \tilde x^{\beta_1}}\cdots\frac{\partial x^{\nu_l}}{\partial \tilde x^{\beta_l}}\,
T^{\mu_1\cdots\mu_k}{}_{\nu_1\cdots\nu_l}.
$$
This follows directly from multilinearity and the basis transformation laws of s2–s3. Conversely, an array obeying this law *defines* a tensor — this is the practical, "physicist's" definition and we use it constantly.

> **Why this matters.** If a tensor's components are all zero in one chart, the transformation law (being linear and homogeneous in $T$) makes them zero in *every* chart. Hence **a tensor equation $A=B$, once verified in one coordinate system, holds in all of them.** This is the mathematical content of "the laws of physics are the same in every frame."

#### Operations: contraction and raising/lowering

- **Contraction** sets one upper and one lower index equal and sums, lowering the type by $(1,1)$. E.g. from $T^\mu{}_\nu$ the **trace** $T^\mu{}_\mu$ is a scalar, invariant under coordinate change (the Jacobians cancel as in s3).
- **Raising and lowering** indices uses the metric (next section): $V_\mu = g_{\mu\nu}V^\nu$ lowers, $V^\mu = g^{\mu\nu}V_\nu$ raises, where $g^{\mu\nu}$ is the inverse metric. These are coordinate-free because $g$ is a tensor.

> **Common pitfall.** The components $\partial_\mu f$ of $df$ form a covector (lower index), *not* a vector, even though we call it "the gradient." Turning it into a vector (the direction of steepest ascent) requires the metric to raise the index: $(\mathrm{grad} f)^\mu = g^{\mu\nu}\partial_\nu f$. In flat Cartesian space $g^{\mu\nu}=\delta^{\mu\nu}$, so the distinction is invisible — which is why it is so often missed.

<a id="s5"></a>
### The metric tensor — lengths, angles, and index gymnastics

The metric is what upgrades a bare smooth manifold to a *geometry*: it lets us measure lengths of curves, angles between vectors, areas, and volumes. In relativity the metric *is* the gravitational field.

#### Definition

> **Definition — (pseudo-)Riemannian metric.**
>
> A **metric** $g$ is a smooth $(0,2)$-tensor field that at each point is **symmetric** ($g(v,w)=g(w,v)$) and **nondegenerate** (if $g(v,w)=0$ for all $w$, then $v=0$). If additionally $g(v,v)>0$ for all $v\ne0$ it is **Riemannian** (a genuine inner product on each $T_pM$); if $g$ has signature $(-,+,+,+)$ it is **Lorentzian**, the case of spacetime. Components: $g_{\mu\nu}=g(\partial_\mu,\partial_\nu)$, a symmetric matrix.

#### The line element

The metric is most often written through the **line element** $ds^2$, the squared length of an infinitesimal displacement $dx^\mu$:
$$
ds^2 = g_{\mu\nu}\,dx^\mu\,dx^\nu .
$$
The **length of a curve** $\gamma:[a,b]\to M$, with coordinate velocity $\dot x^\mu = dx^\mu/dt$, is then
$$
L[\gamma] = \int_a^b \sqrt{\,g_{\mu\nu}(\gamma(t))\,\dot x^\mu \dot x^\nu\,}\; dt ,
$$
(for a Lorentzian metric one uses $|g_{\mu\nu}\dot x^\mu\dot x^\nu|$ with sign conventions). The **angle** $\theta$ between vectors $v,w$ comes from $\cos\theta = g(v,w)/\sqrt{g(v,v)\,g(w,w)}$, exactly the inner-product formula from linear algebra.

#### The inverse metric and index gymnastics

Because $g_{\mu\nu}$ is nondegenerate, the matrix $(g_{\mu\nu})$ is invertible. Its inverse defines the **inverse metric** $g^{\mu\nu}$, a symmetric $(2,0)$-tensor, by
$$
g^{\mu\rho}g_{\rho\nu} = \delta^\mu_\nu .
$$
Lowering then raising returns the original: $g^{\mu\rho}(g_{\rho\nu}V^\nu) = g^{\mu\rho}V_\rho = V^\mu$. This consistency is why raising/lowering with $g$ is well-defined.

#### Worked example 1 — flat plane in polar coordinates

Start from $ds^2 = dx^2 + dy^2$ (Euclidean) with $x=r\cos\theta$, $y=r\sin\theta$.

1. Differentials: $dx = \cos\theta\,dr - r\sin\theta\,d\theta$, $dy=\sin\theta\,dr + r\cos\theta\,d\theta$ (product and chain rules).
2. Square and add. The cross terms $dr\,d\theta$ carry coefficient $2(-\cos\theta\sin\theta\, r + \sin\theta\cos\theta\, r)=0$. The $dr^2$ coefficient is $\cos^2\theta+\sin^2\theta=1$; the $d\theta^2$ coefficient is $r^2(\sin^2\theta+\cos^2\theta)=r^2$.
3. Hence
   $$
   ds^2 = dr^2 + r^2\,d\theta^2,\qquad (g_{\mu\nu}) = \begin{pmatrix} 1 & 0 \\ 0 & r^2\end{pmatrix},\qquad (g^{\mu\nu})=\begin{pmatrix}1 & 0 \\ 0 & r^{-2}\end{pmatrix}.
   $$
The space is still flat (we will confirm zero curvature in s10); the $r^2$ is an artifact of curved *coordinates*, not curved *space*.

#### Worked example 2 — the round sphere

On $S^2$ with the latitude–longitude chart (colatitude $\theta\in(0,\pi)$, longitude $\phi$) embedded as $(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta)$, the same differentiation gives the **round metric of radius 1**:
$$
ds^2 = d\theta^2 + \sin^2\theta\, d\phi^2,\qquad (g_{\mu\nu})=\begin{pmatrix}1&0\\0&\sin^2\theta\end{pmatrix}.
$$
This metric *is* curved — there is no coordinate change turning it into $d\theta^2+d\phi^2$ globally, which is the precise reason every flat map of the Earth distorts. We will prove its curvature is nonzero in s10.

> **Intuition.** The metric is a "ruler field": at each point it tells you how to convert coordinate differences into real distances. Changing coordinates changes the ruler's components but not the distances it measures — distance is the invariant, components are bookkeeping.

## Part C · Forms and integration

<a id="s6"></a>
### Differential forms, the wedge product, and the exterior derivative

Differential forms are the *totally antisymmetric* covariant tensors. They are exactly the objects one can integrate over a manifold without extra structure, and they unify grad, curl, div, and the fundamental theorem of calculus into a single operator $d$.

#### Forms and the wedge product

> **Definition — $k$-form.**
>
> A **$k$-form** is a $(0,k)$-tensor field that is **alternating**: it changes sign when any two arguments are swapped (hence vanishes if two arguments coincide). A $0$-form is a function; a $1$-form is a covector field.

> **Definition — wedge product.**
>
> The **wedge product** of a $k$-form $\alpha$ and an $l$-form $\beta$ is the $(k+l)$-form obtained by antisymmetrizing the tensor product $\alpha\otimes\beta$. On basis one-forms it is generated by $dx^\mu\wedge dx^\nu = -\,dx^\nu\wedge dx^\mu$ (so $dx^\mu\wedge dx^\mu=0$), extended bilinearly and associatively. It is **graded-commutative**: $\alpha\wedge\beta = (-1)^{kl}\beta\wedge\alpha$.

Every $k$-form is $\omega = \tfrac{1}{k!}\,\omega_{\mu_1\cdots\mu_k}\,dx^{\mu_1}\wedge\cdots\wedge dx^{\mu_k}$ with totally antisymmetric components. On an $n$-manifold the top degree is $n$: there are no nonzero $(n+1)$-forms, since some index must repeat.

#### The exterior derivative

> **Definition — exterior derivative.**
>
> The **exterior derivative** $d$ maps $k$-forms to $(k+1)$-forms. On a $0$-form (function) $f$ it is the differential $df = \partial_\mu f\,dx^\mu$. On a general form $\omega = \tfrac1{k!}\omega_{\mu_1\cdots\mu_k}dx^{\mu_1}\wedge\cdots\wedge dx^{\mu_k}$,
>
> $$
> d\omega = \frac1{k!}\,\partial_\nu \omega_{\mu_1\cdots\mu_k}\; dx^\nu\wedge dx^{\mu_1}\wedge\cdots\wedge dx^{\mu_k}.
> $$
>
> It is linear and obeys the **graded Leibniz rule** $d(\alpha\wedge\beta) = d\alpha\wedge\beta + (-1)^{k}\alpha\wedge d\beta$ for a $k$-form $\alpha$.

#### Theorem: $d^2 = 0$

> **Theorem.** For every form $\omega$, $d(d\omega)=0$.

*Proof.* It suffices to prove it on a $0$-form and propagate by the Leibniz rule; we show it directly on a general form by exhibiting the mechanism on a function (the higher-degree case repeats it index-by-index).
1. Let $f$ be a function. Then $df = \partial_\mu f\, dx^\mu$, a $1$-form.
2. Apply $d$ again using the definition: $d(df) = \partial_\nu\partial_\mu f\; dx^\nu\wedge dx^\mu$, summing over $\mu,\nu$.
3. Split the double sum into the symmetric coefficient and antisymmetric basis. The coefficient $\partial_\nu\partial_\mu f$ is **symmetric in $\mu,\nu$** by **Clairaut/Schwarz's theorem** (equality of mixed partial derivatives for smooth functions). The basis factor $dx^\nu\wedge dx^\mu$ is **antisymmetric in $\mu,\nu$** by the wedge rule.
4. A sum over all $\mu,\nu$ of (symmetric in $\mu\nu$) times (antisymmetric in $\mu\nu$) is zero: swapping the dummy names $\mu\leftrightarrow\nu$ leaves the symmetric factor unchanged but flips the antisymmetric one, so the sum equals its own negative, hence is $0$. Concretely $\sum_{\mu,\nu}\partial_\nu\partial_\mu f\,dx^\nu\wedge dx^\mu = \tfrac12\sum_{\mu,\nu}(\partial_\nu\partial_\mu f-\partial_\mu\partial_\nu f)\,dx^\nu\wedge dx^\mu = 0$.
5. For a general $k$-form the extra exterior factors $dx^{\mu_1}\wedge\cdots$ ride along unchanged, and the same symmetric-times-antisymmetric cancellation in the two new derivative indices gives $d(d\omega)=0$. $\blacksquare$

> **Connection to vector calculus.** In $\mathbb{R}^3$: $d$ on a $0$-form is $\mathrm{grad}$; on a $1$-form it is $\mathrm{curl}$; on a $2$-form it is $\mathrm{div}$. Then $d^2=0$ encodes the two classical identities $\mathrm{curl}\,\mathrm{grad}=0$ and $\mathrm{div}\,\mathrm{curl}=0$ at once. This is why forms are the natural language.

<a id="s7"></a>
### Integration of forms and the general Stokes' theorem

A $k$-form is *exactly* the kind of object you integrate over a $k$-dimensional region, because its antisymmetry is built to match the orientation-sensitivity of integration (swapping two coordinates flips both the form and the volume element's sign, so the integral is well-defined and orientation-aware).

#### Integration

On an oriented $n$-manifold, a top-degree ($n$-)form $\omega = h\,dx^1\wedge\cdots\wedge dx^n$ is integrated chart-by-chart as the ordinary multiple integral $\int h\,dx^1\cdots dx^n$. The **change-of-variables theorem** guarantees this is chart-independent: under a coordinate change the form's coefficient picks up the Jacobian determinant, exactly canceling the Jacobian factor in the multiple-integral substitution rule. (This is the deep reason forms, not arbitrary tensors, are the integrands: the determinant is the antisymmetric object.) To integrate a $k$-form over a $k$-dimensional submanifold, **pull it back** to the parameter domain and integrate there.

#### The general Stokes' theorem

> **Theorem — Stokes' theorem.**
>
> Let $M$ be an oriented smooth $n$-manifold with boundary $\partial M$ (given the induced orientation), and let $\omega$ be a compactly supported $(n-1)$-form. Then
>
> $$
> \int_M d\omega = \int_{\partial M}\omega .
> $$

The proof reduces, via a partition of unity and charts, to the half-space case, where it is the fundamental theorem of calculus applied one coordinate at a time. The single statement specializes to the classical theorems:

- **$n=1$:** with $\omega=f$ a $0$-form on $[a,b]$, $\int_a^b df = f(b)-f(a)$ — the **fundamental theorem of calculus**.
- **$n=2$:** **Green's theorem**.
- **$n=3$, $(n-1)$-form:** the **divergence theorem**; for a $1$-form over a surface, the **Kelvin–Stokes (curl) theorem**.

So all the integral theorems of vector calculus are one theorem: *the integral of a derivative over a region equals the original over the boundary.*

#### A word on de Rham cohomology

A form $\omega$ is **closed** if $d\omega=0$ and **exact** if $\omega=d\eta$ for some $\eta$. Since $d^2=0$ (s6), every exact form is closed. The reverse can fail, and the failure measures the **holes** of $M$:
$$
H^k_{\mathrm{dR}}(M) = \frac{\{\text{closed }k\text{-forms}\}}{\{\text{exact }k\text{-forms}\}} .
$$
The **de Rham cohomology** $H^k_{\mathrm{dR}}(M)$ is a vector space whose dimension counts $k$-dimensional holes. The classic example: on $\mathbb{R}^2\setminus\{0\}$ the angle form $\omega=\tfrac{-y\,dx+x\,dy}{x^2+y^2}$ is closed ($d\omega=0$) but not exact (its loop integral around the origin is $2\pi\ne0$, while exact forms integrate to $0$ over closed loops by Stokes). The de Rham theorem identifies $H^k_{\mathrm{dR}}(M)$ with the topological cohomology of $M$ — a bridge between calculus and topology.

## Part D · Connection and curvature

<a id="s8"></a>
### The covariant derivative and Christoffel symbols

To differentiate a vector field we must compare vectors at *different* points — but they live in different tangent spaces, and (s0) there is no canonical identification. The extra structure that supplies one is a **connection**, and the resulting derivative is the **covariant derivative** $\nabla$.

#### Why $\partial_\mu V^\nu$ is not a tensor

Differentiate the vector transformation law $\tilde V^\alpha = \frac{\partial\tilde x^\alpha}{\partial x^\mu}V^\mu$. By the product rule,
$$
\tilde\partial_\beta \tilde V^\alpha = \frac{\partial x^\nu}{\partial\tilde x^\beta}\frac{\partial \tilde x^\alpha}{\partial x^\mu}\,\partial_\nu V^\mu \;+\; \frac{\partial x^\nu}{\partial\tilde x^\beta}\frac{\partial^2 \tilde x^\alpha}{\partial x^\nu\partial x^\mu}V^\mu .
$$
The first term is the tensor law for a $(1,1)$-tensor; the **second term**, with a second derivative of the coordinate change, spoils it. So the naive partial derivative of a vector field is *not* a tensor. We need a correction term that cancels exactly this junk.

#### The connection

> **Definition — affine connection / covariant derivative.**
>
> A **connection** $\nabla$ assigns to vector fields a covariant derivative $\nabla_\mu$ acting on tensor fields, linear and obeying the Leibniz rule, reducing to $\partial_\mu$ on functions. On a vector field its components are
>
> $$
> \nabla_\mu V^\nu = \partial_\mu V^\nu + \Gamma^\nu{}_{\mu\rho}\,V^\rho,
> $$
>
> where the $\Gamma^\nu{}_{\mu\rho}$ are the **connection coefficients** (**Christoffel symbols** when derived from a metric). On a covector: $\nabla_\mu \omega_\nu = \partial_\mu\omega_\nu - \Gamma^\rho{}_{\mu\nu}\omega_\rho$. The signs are fixed by demanding $\nabla_\mu(\omega_\nu V^\nu)=\partial_\mu(\omega_\nu V^\nu)$, since $\omega_\nu V^\nu$ is a scalar.

For $\nabla_\mu V^\nu$ to be a tensor, $\Gamma$ must itself transform *inhomogeneously*, with a second-derivative term precisely canceling the offending term above. (The $\Gamma$ are therefore *not* tensors — their non-tensorial transformation is the whole point.)

#### The Levi-Civita connection: deriving Christoffel symbols from the metric

On a (pseudo-)Riemannian manifold there is a unique natural connection.

> **Theorem (Fundamental theorem of Riemannian geometry).** There is a unique connection that is
> - **metric-compatible:** $\nabla_\mu g_{\nu\rho}=0$ (lengths and angles are preserved by parallel transport), and
> - **torsion-free (symmetric):** $\Gamma^\rho{}_{\mu\nu}=\Gamma^\rho{}_{\nu\mu}$.
>
> Its coefficients, the **Christoffel symbols**, are
>
> $$
> \Gamma^\rho{}_{\mu\nu} = \tfrac12\, g^{\rho\sigma}\big(\partial_\mu g_{\sigma\nu} + \partial_\nu g_{\sigma\mu} - \partial_\sigma g_{\mu\nu}\big).
> $$

*Derivation.*
1. Write metric compatibility three times, cycling the indices:
   $$
   \partial_\mu g_{\nu\rho} = \Gamma^\sigma{}_{\mu\nu}g_{\sigma\rho} + \Gamma^\sigma{}_{\mu\rho}g_{\nu\sigma}\quad(\text{i}),
   $$
   $$
   \partial_\nu g_{\rho\mu} = \Gamma^\sigma{}_{\nu\rho}g_{\sigma\mu} + \Gamma^\sigma{}_{\nu\mu}g_{\rho\sigma}\quad(\text{ii}),
   $$
   $$
   \partial_\rho g_{\mu\nu} = \Gamma^\sigma{}_{\rho\mu}g_{\sigma\nu} + \Gamma^\sigma{}_{\rho\nu}g_{\mu\sigma}\quad(\text{iii}),
   $$
   each obtained by expanding $0=\nabla_\mu g_{\nu\rho}=\partial_\mu g_{\nu\rho}-\Gamma^\sigma{}_{\mu\nu}g_{\sigma\rho}-\Gamma^\sigma{}_{\mu\rho}g_{\nu\sigma}$ and rearranging.
2. Compute (i) + (ii) − (iii). Using the **symmetry** $\Gamma^\sigma{}_{\mu\nu}=\Gamma^\sigma{}_{\nu\mu}$ and the symmetry $g_{\sigma\rho}=g_{\rho\sigma}$, four of the six $\Gamma g$ terms cancel in pairs, leaving
   $$
   \partial_\mu g_{\nu\rho} + \partial_\nu g_{\rho\mu} - \partial_\rho g_{\mu\nu} = 2\,\Gamma^\sigma{}_{\mu\nu}\,g_{\sigma\rho}.
   $$
3. Solve for $\Gamma$ by contracting with the inverse metric $g^{\rho\lambda}$ (which exists by s5) and using $g^{\rho\lambda}g_{\sigma\rho}=\delta^\lambda_\sigma$:
   $$
   \Gamma^\lambda{}_{\mu\nu} = \tfrac12\, g^{\lambda\rho}\big(\partial_\mu g_{\nu\rho}+\partial_\nu g_{\rho\mu}-\partial_\rho g_{\mu\nu}\big),
   $$
   which is the claimed formula (rename $\rho\to\sigma$, $\lambda\to\rho$). Uniqueness follows because every step was forced; existence, because this formula does define a metric-compatible torsion-free connection (substitute back to check). $\blacksquare$

#### Worked example — Christoffel symbols of the plane in polar coordinates

With $g_{rr}=1$, $g_{\theta\theta}=r^2$, $g^{rr}=1$, $g^{\theta\theta}=r^{-2}$ (off-diagonals zero), the only nonzero metric derivative is $\partial_r g_{\theta\theta}=2r$. The formula gives:
$$
\Gamma^r{}_{\theta\theta} = \tfrac12 g^{rr}(-\partial_r g_{\theta\theta}) = -r,\qquad
\Gamma^\theta{}_{r\theta}=\Gamma^\theta{}_{\theta r} = \tfrac12 g^{\theta\theta}\partial_r g_{\theta\theta} = \tfrac{1}{r},
$$
all others zero. These are the familiar terms in the polar-coordinate acceleration $\ddot r - r\dot\theta^2$ and $\ddot\theta + \tfrac2r\dot r\dot\theta$ — the "fictitious" centrifugal and Coriolis terms are Christoffel symbols.

<a id="s9"></a>
### Parallel transport and geodesics

A **geodesic** is the manifold's notion of a "straight line." There are two ways to make this precise — *straightest* (zero turning) and *shortest* (extremal length) — and the Levi-Civita connection makes them agree.

#### Parallel transport

> **Definition — parallel transport.**
>
> A vector field $V$ is **parallel-transported** along a curve $x^\mu(\lambda)$ if its covariant derivative along the curve vanishes:
>
> $$
> \frac{DV^\mu}{d\lambda} := \dot x^\nu\nabla_\nu V^\mu = \frac{dV^\mu}{d\lambda} + \Gamma^\mu{}_{\nu\rho}\,\dot x^\nu V^\rho = 0 .
> $$

This is the connection's promised rule for "carrying a vector while keeping it as constant as the curved space allows." Metric compatibility ensures lengths and angles are preserved under transport.

#### Geodesics as straightest paths

> **Definition — geodesic (straightest).** A curve is a **geodesic** if it parallel-transports its own tangent vector: $\frac{D\dot x^\mu}{d\lambda}=0$. Explicitly,
>
> $$
> \boxed{\ \ddot x^\mu + \Gamma^\mu{}_{\nu\rho}\,\dot x^\nu\dot x^\rho = 0\ }
> $$
>
> the **geodesic equation**, where dots are $d/d\lambda$ for an **affine parameter** $\lambda$.

This is "go straight: don't turn." The $\Gamma$ term is the correction that distinguishes genuine turning from the coordinate grid bending.

#### Geodesics as shortest paths — derivation via the calculus of variations

We now derive the *same* equation by extremizing length, confirming the two notions coincide.

The arc length is $L=\int \sqrt{g_{\mu\nu}\dot x^\mu\dot x^\nu}\,d\lambda$. It is technically cleaner (and equivalent for the extremals, when $\lambda$ is affine) to extremize the **energy functional** $S=\int \mathcal{L}\,d\lambda$ with $\mathcal{L}=\tfrac12 g_{\mu\nu}(x)\dot x^\mu\dot x^\nu$.

1. **Euler–Lagrange equations.** Extremals of $S$ satisfy, for each coordinate $x^\sigma$, the Euler–Lagrange equation $\frac{d}{d\lambda}\frac{\partial\mathcal L}{\partial\dot x^\sigma} - \frac{\partial\mathcal L}{\partial x^\sigma}=0$ (standard variational calculus: the first variation vanishes for all endpoint-fixed perturbations).
2. **Compute $\partial\mathcal L/\partial\dot x^\sigma$.** Since $\mathcal L=\tfrac12 g_{\mu\nu}\dot x^\mu\dot x^\nu$ and $g$ does not depend on $\dot x$, differentiating in $\dot x^\sigma$ (which hits each of the two velocity factors) and using symmetry $g_{\mu\nu}=g_{\nu\mu}$ gives $\partial\mathcal L/\partial\dot x^\sigma = g_{\sigma\nu}\dot x^\nu$.
3. **Time-derivative.** $\frac{d}{d\lambda}\big(g_{\sigma\nu}\dot x^\nu\big) = (\partial_\mu g_{\sigma\nu})\dot x^\mu\dot x^\nu + g_{\sigma\nu}\ddot x^\nu$, by the product and chain rules ($g$ depends on $\lambda$ through $x(\lambda)$).
4. **Compute $\partial\mathcal L/\partial x^\sigma$.** Only $g_{\mu\nu}$ depends on position: $\partial\mathcal L/\partial x^\sigma = \tfrac12(\partial_\sigma g_{\mu\nu})\dot x^\mu\dot x^\nu$.
5. **Assemble.** The Euler–Lagrange equation becomes
   $$
   g_{\sigma\nu}\ddot x^\nu + (\partial_\mu g_{\sigma\nu})\dot x^\mu\dot x^\nu - \tfrac12(\partial_\sigma g_{\mu\nu})\dot x^\mu\dot x^\nu = 0 .
   $$
6. **Symmetrize the middle term.** Because $\dot x^\mu\dot x^\nu$ is symmetric in $\mu,\nu$, we may replace $(\partial_\mu g_{\sigma\nu})\dot x^\mu\dot x^\nu$ by its symmetrization $\tfrac12(\partial_\mu g_{\sigma\nu}+\partial_\nu g_{\sigma\mu})\dot x^\mu\dot x^\nu$. Then
   $$
   g_{\sigma\nu}\ddot x^\nu + \tfrac12\big(\partial_\mu g_{\sigma\nu}+\partial_\nu g_{\sigma\mu}-\partial_\sigma g_{\mu\nu}\big)\dot x^\mu\dot x^\nu = 0 .
   $$
7. **Recognize the Christoffel symbol.** Contract with $g^{\rho\sigma}$. The first term becomes $\ddot x^\rho$; the bracket is exactly $2g_{\sigma\lambda}\Gamma^\lambda{}_{\mu\nu}$ from s8, so $g^{\rho\sigma}\cdot\tfrac12(\cdots) = \Gamma^\rho{}_{\mu\nu}$. Result:
   $$
   \ddot x^\rho + \Gamma^\rho{}_{\mu\nu}\dot x^\mu\dot x^\nu = 0 .
   $$
This is identical to the straightest-path geodesic equation. **The shortest path and the straightest path coincide** — for the Levi-Civita connection. $\blacksquare$

> **Worked example — great circles on the sphere.** On $S^2$ with $ds^2=d\theta^2+\sin^2\theta\,d\phi^2$, the geodesic equations (using $\Gamma^\theta{}_{\phi\phi}=-\sin\theta\cos\theta$, $\Gamma^\phi{}_{\theta\phi}=\cot\theta$) are solved by the equator $\theta=\pi/2$ ($\ddot\theta=0$, and $\Gamma^\theta{}_{\phi\phi}=-\sin\tfrac\pi2\cos\tfrac\pi2=0$, consistent), traversed at constant rate. By rotational symmetry every **great circle** is a geodesic — the shortest air routes on Earth.

<a id="s10"></a>
### Curvature — the Riemann tensor, Ricci, and the Bianchi identities

Curvature measures the failure of the manifold to be flat. The clean operational definition: **on a curved space, covariant derivatives do not commute**, and parallel transport around a closed loop rotates a vector.

#### The Riemann curvature tensor

> **Definition — Riemann tensor via the commutator.**
>
> For a torsion-free connection, the **Riemann curvature tensor** $R^\rho{}_{\sigma\mu\nu}$ is defined by its action through the commutator of covariant derivatives on a vector field:
>
> $$
> (\nabla_\mu\nabla_\nu - \nabla_\nu\nabla_\mu)V^\rho = R^\rho{}_{\sigma\mu\nu}\,V^\sigma .
> $$

That the left side is *algebraic* in $V$ (no derivatives of $V$ survive) is what makes $R$ a genuine $(1,3)$-tensor; it is a theorem, proved by expanding both $\nabla\nabla$ terms and watching the $\partial V$ pieces cancel by symmetry.

> **Theorem — Riemann in terms of Christoffel symbols.**
>
> $$
> R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}.
> $$

*Derivation.*
1. Expand $\nabla_\nu V^\rho = \partial_\nu V^\rho + \Gamma^\rho{}_{\nu\sigma}V^\sigma$; call this $W^\rho{}_\nu$ (a $(1,1)$-tensor).
2. Apply $\nabla_\mu$ to the $(1,1)$-tensor $W$: $\nabla_\mu W^\rho{}_\nu = \partial_\mu W^\rho{}_\nu + \Gamma^\rho{}_{\mu\lambda}W^\lambda{}_\nu - \Gamma^\lambda{}_{\mu\nu}W^\rho{}_\lambda$.
3. Substitute $W$ and expand. Antisymmetrize in $\mu\leftrightarrow\nu$ (subtract the same with $\mu,\nu$ swapped). The terms $\partial_\mu\partial_\nu V^\rho$ are symmetric and cancel; the connection terms $\Gamma^\lambda{}_{\mu\nu}$ are symmetric in $\mu\nu$ (torsion-free) and cancel; what survives is exactly the displayed combination acting on $V^\sigma$. $\blacksquare$

#### Symmetries

Lowering the first index, $R_{\rho\sigma\mu\nu}=g_{\rho\lambda}R^\lambda{}_{\sigma\mu\nu}$ satisfies (for the Levi-Civita connection):
$$
R_{\rho\sigma\mu\nu} = -R_{\sigma\rho\mu\nu} = -R_{\rho\sigma\nu\mu} = R_{\mu\nu\rho\sigma},\qquad R_{\rho[\sigma\mu\nu]}=0 ,
$$
i.e. antisymmetry in the first pair, antisymmetry in the second pair, symmetry under swapping the pairs, and the **first (algebraic) Bianchi identity** $R_{\rho\sigma\mu\nu}+R_{\rho\mu\nu\sigma}+R_{\rho\nu\sigma\mu}=0$. These cut the number of independent components in $n=4$ down to $20$.

#### Ricci tensor and scalar

> **Definition.** The **Ricci tensor** is the contraction $R_{\sigma\nu} = R^\mu{}_{\sigma\mu\nu}$ (it is symmetric, $R_{\sigma\nu}=R_{\nu\sigma}$, from the Riemann symmetries). The **Ricci scalar** (scalar curvature) is the full trace $R = g^{\sigma\nu}R_{\sigma\nu}$.

#### The second (differential) Bianchi identity

> **Theorem.** $\ \nabla_\lambda R_{\rho\sigma\mu\nu} + \nabla_\mu R_{\rho\sigma\nu\lambda} + \nabla_\nu R_{\rho\sigma\lambda\mu} = 0.$

The slickest proof uses **normal coordinates** at a point $p$: coordinates in which $\Gamma^\rho{}_{\mu\nu}(p)=0$ (these exist for any torsion-free connection, by a quadratic coordinate change killing the symmetric part of $\Gamma$). At $p$, $\nabla$ reduces to $\partial$ and $R^\rho{}_{\sigma\mu\nu}=\partial_\mu\Gamma^\rho{}_{\nu\sigma}-\partial_\nu\Gamma^\rho{}_{\mu\sigma}$, so $\nabla_\lambda R$ involves $\partial_\lambda\partial_{[\mu}\Gamma$; the cyclic sum over $\lambda,\mu,\nu$ cancels by equality of mixed partials. Being a tensor equation true at the arbitrary point $p$ in one chart, it holds everywhere in all charts (s4). $\blacksquare$

#### Worked example — the sphere is curved, the plane is not

For the polar plane ($\Gamma^r{}_{\theta\theta}=-r$, $\Gamma^\theta{}_{r\theta}=1/r$), a direct substitution into the Riemann formula gives $R^\rho{}_{\sigma\mu\nu}=0$ everywhere — the plane is **flat** despite curved coordinates. For the unit sphere ($\Gamma^\theta{}_{\phi\phi}=-\sin\theta\cos\theta$, $\Gamma^\phi{}_{\theta\phi}=\cot\theta$) one finds $R^\theta{}_{\phi\theta\phi}=\sin^2\theta$, giving Ricci $R_{\theta\theta}=1$, $R_{\phi\phi}=\sin^2\theta$ and Ricci scalar $R = g^{\theta\theta}R_{\theta\theta}+g^{\phi\phi}R_{\phi\phi} = 1 + 1 = 2$ (for the unit sphere; in general $R=2/a^2$ for radius $a$). Positive constant curvature, matching intuition.

<a id="s11"></a>
### Geodesic deviation and the physical meaning of curvature

Curvature is not directly felt by a single freely falling observer — by the equivalence principle a lone freely falling body cannot tell gravity from free space. What curvature *does* produce is **tidal forces**: nearby geodesics accelerate toward or away from each other.

#### The geodesic deviation equation

Consider a one-parameter family of geodesics $x^\mu(\lambda,s)$, $s$ labeling neighboring geodesics. Let $T^\mu = \partial x^\mu/\partial\lambda$ be the tangent and $S^\mu=\partial x^\mu/\partial s$ the **separation vector** pointing to the neighbor.

> **Theorem — geodesic deviation (Jacobi equation).**
>
> $$
> \frac{D^2 S^\rho}{d\lambda^2} = -\,R^\rho{}_{\sigma\mu\nu}\,T^\sigma S^\mu T^\nu .
> $$
>
> The relative acceleration of nearby geodesics is governed *entirely* by the Riemann tensor.

*Sketch of derivation.* Both $T$ and $S$ are coordinate vector fields of the family, so their Lie bracket vanishes, which (for a torsion-free connection) gives $\nabla_T S = \nabla_S T$. Compute the second covariant derivative $\frac{D^2S}{d\lambda^2}=\nabla_T\nabla_T S = \nabla_T\nabla_S T$, commute the derivatives introducing the Riemann tensor via its definition (s10), and use the geodesic equation $\nabla_T T=0$ to drop one term. The surviving term is the curvature contraction above. $\blacksquare$

#### Physical meaning: tidal forces

In Newtonian gravity, a cloud of freely falling particles is stretched along the radial direction and squeezed transversely — the **tidal field** of the Moon raising two ocean bulges. In general relativity that tidal field *is* the Riemann tensor: $\frac{D^2S^\rho}{d\lambda^2}=-R^\rho{}_{\sigma\mu\nu}T^\sigma S^\mu T^\nu$ is the relativistic tidal equation, and in the Newtonian limit $R^i{}_{0j0}\to \partial_i\partial_j\Phi$ (second derivatives of the gravitational potential).

> **Intuition.** Two travelers starting at the equator heading due north along separate meridians (both geodesics) move *parallel at first* but *converge* and meet at the pole. They felt no sideways force, yet their separation accelerated to zero — pure curvature, no force. That is gravity in GR.

## Part E · General relativity and symmetry

<a id="s12"></a>
### The Einstein field equations — the structure of general relativity

We now assemble the pieces into the equation that governs spacetime. The guiding requirements: it should relate **curvature** (geometry) to **energy–momentum** (matter), be a tensor equation (frame-independent, s4), be second-order in the metric (like Newtonian gravity, where $\nabla^2\Phi=4\pi G\rho$), and respect **local energy–momentum conservation** $\nabla_\mu T^{\mu\nu}=0$.

#### The Einstein tensor

The matter side is the **stress–energy tensor** $T_{\mu\nu}$, a symmetric $(0,2)$-tensor encoding energy density, momentum, and stresses, satisfying $\nabla^\mu T_{\mu\nu}=0$. The geometry side must therefore be a symmetric $(0,2)$-tensor, built from the metric and its first two derivatives, with **identically vanishing divergence**. We construct it.

1. **Contract the second Bianchi identity** (s10): start from $\nabla_\lambda R_{\rho\sigma\mu\nu}+\nabla_\mu R_{\rho\sigma\nu\lambda}+\nabla_\nu R_{\rho\sigma\lambda\mu}=0$.
2. Raise and contract indices ($g^{\rho\mu}$ then $g^{\sigma\nu}$), using metric compatibility $\nabla g=0$ to move the metric through the derivatives and the Riemann symmetries to identify Ricci pieces. The result is the **contracted Bianchi identity**
   $$
   \nabla^\mu R_{\mu\nu} = \tfrac12\,\nabla_\nu R .
   $$
3. **Rearrange** into a divergence-free combination:
   $$
   \nabla^\mu\!\left(R_{\mu\nu} - \tfrac12 g_{\mu\nu}R\right) = \nabla^\mu R_{\mu\nu} - \tfrac12\nabla_\nu R = 0 ,
   $$
   using $\nabla^\mu(g_{\mu\nu}R)=\nabla_\nu R$ from metric compatibility.
4. **Define the Einstein tensor**
   $$
   G_{\mu\nu} := R_{\mu\nu} - \tfrac12 g_{\mu\nu}R ,\qquad \nabla^\mu G_{\mu\nu}=0 .
   $$
It is symmetric, built from second derivatives of $g$, and *automatically* conserved — exactly matching $T_{\mu\nu}$.

#### The field equations

> **The Einstein field equations.**
>
> $$
> R_{\mu\nu} - \tfrac12 g_{\mu\nu}R + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4}\,T_{\mu\nu} .
> $$
>
> Here $G$ is Newton's constant, $c$ the speed of light, and $\Lambda$ the **cosmological constant** (also divergence-free since $\nabla g=0$, hence allowed). The constant $8\pi G/c^4$ is fixed by demanding the **Newtonian limit** $\nabla^2\Phi=4\pi G\rho$ in weak, slow, static fields.

In Wheeler's slogan: *spacetime tells matter how to move* (matter follows geodesics, s9), *and matter tells spacetime how to curve* (the field equations). The two halves of this guide — geodesics and curvature — are the two halves of gravity.

> **Worked example — vacuum and the structure.** In vacuum ($T_{\mu\nu}=0$, $\Lambda=0$): contract the field equations with $g^{\mu\nu}$. Using $g^{\mu\nu}g_{\mu\nu}=n=4$, we get $R - \tfrac12\cdot4\cdot R = -R = 0$, so $R=0$, and then $R_{\mu\nu}=0$. **Vacuum spacetimes are Ricci-flat** — yet the *Riemann* tensor need not vanish, so gravity (tidal curvature) persists in empty space. The Schwarzschild solution outside a star is exactly such a Ricci-flat but Riemann-curved geometry; it predicts the bending of starlight and the precession of Mercury.

<a id="s13"></a>
### The Lie derivative and Killing vectors — symmetries and conserved quantities

Symmetries of a metric produce conserved quantities along geodesics — the geometric form of Noether's theorem. The right tool is the **Lie derivative**, which differentiates a tensor along the flow of a vector field *without needing a connection*.

#### The Lie derivative

> **Definition — Lie derivative.**
>
> Let $X$ be a vector field generating a flow $\phi_t$ (the solution of $\frac{d}{dt}\phi_t(p)=X_{\phi_t(p)}$). The **Lie derivative** of a tensor $T$ along $X$ is the rate of change of $T$ dragged back by the flow:
>
> $$
> \mathcal{L}_X T = \lim_{t\to0}\frac{\phi_t^*T - T}{t}.
> $$

It compares $T$ at nearby points by *transporting along the flow of $X$* rather than by a connection. Concrete formulas (derived from the definition by expanding the flow to first order):
- On a function: $\mathcal{L}_X f = X^\mu\partial_\mu f = X(f)$.
- On a vector field: $\mathcal{L}_X Y = [X,Y]$, the Lie bracket.
- On the metric (a $(0,2)$-tensor):
  $$
  (\mathcal{L}_X g)_{\mu\nu} = X^\lambda\partial_\lambda g_{\mu\nu} + g_{\lambda\nu}\partial_\mu X^\lambda + g_{\mu\lambda}\partial_\nu X^\lambda = \nabla_\mu X_\nu + \nabla_\nu X_\mu ,
  $$
  the last equality holding for the Levi-Civita connection (the Christoffel terms reorganize the partial derivatives into covariant ones — the non-tensorial $\Gamma$ pieces cancel because $\mathcal{L}_X g$ is a tensor).

#### Killing vectors

> **Definition — Killing vector.**
>
> A vector field $\xi$ is a **Killing vector field** if the metric is invariant under its flow, i.e. $\mathcal{L}_\xi g = 0$. Equivalently, by the formula above, it satisfies **Killing's equation**
>
> $$
> \nabla_\mu \xi_\nu + \nabla_\nu \xi_\mu = 0 .
> $$

Each Killing vector is an infinitesimal isometry — a direction in which the geometry "looks the same." For instance, $\partial_\phi$ on the round sphere or in axisymmetric spacetimes is Killing (rotational symmetry); $\partial_t$ in a static spacetime is Killing (time-translation symmetry).

#### Conserved quantities along geodesics

> **Theorem.** If $\xi$ is a Killing vector and $x^\mu(\lambda)$ a geodesic with tangent $u^\mu=\dot x^\mu$, then $\xi_\mu u^\mu$ is **constant along the geodesic**.

*Proof.*
1. Differentiate along the geodesic: $\frac{d}{d\lambda}(\xi_\mu u^\mu) = u^\nu\nabla_\nu(\xi_\mu u^\mu)$, since $\xi_\mu u^\mu$ is a scalar and $\frac{d}{d\lambda}=u^\nu\nabla_\nu$.
2. Apply the Leibniz rule: $u^\nu\nabla_\nu(\xi_\mu u^\mu) = u^\nu u^\mu\nabla_\nu\xi_\mu + \xi_\mu\,u^\nu\nabla_\nu u^\mu$.
3. The second term is $\xi_\mu\,(u^\nu\nabla_\nu u^\mu)=0$ by the **geodesic equation** $u^\nu\nabla_\nu u^\mu=0$ (s9).
4. The first term $u^\nu u^\mu\nabla_\nu\xi_\mu$ contracts the **symmetric** $u^\nu u^\mu$ against $\nabla_\nu\xi_\mu$. Split $\nabla_\nu\xi_\mu$ into symmetric and antisymmetric parts; the symmetric part is $\tfrac12(\nabla_\nu\xi_\mu+\nabla_\mu\xi_\nu)=0$ by **Killing's equation**, and the antisymmetric part contracted with the symmetric $u^\nu u^\mu$ vanishes (symmetric-times-antisymmetric, as in s6). So this term is $0$ too.
5. Hence $\frac{d}{d\lambda}(\xi_\mu u^\mu)=0$. $\blacksquare$

> **Worked example — conserved energy and angular momentum.** In a stationary, axisymmetric spacetime (e.g. Schwarzschild), $\xi_{(t)}=\partial_t$ and $\xi_{(\phi)}=\partial_\phi$ are Killing. The conserved quantities $-\xi_{(t)\mu}u^\mu$ and $\xi_{(\phi)\mu}u^\mu$ are precisely the **energy** and **angular momentum** per unit mass of an orbiting particle — the constants that let one integrate planetary orbits and light bending. Symmetry of the metric becomes a conservation law, exactly as Noether's theorem promises.

---

*This guide built differential geometry from the ground up — manifolds and charts, tangent vectors as derivations, tensors and their transformation law, the metric, forms and Stokes' theorem, the covariant derivative, geodesics, and curvature — and then read the whole edifice back as general relativity: matter moves along geodesics, curvature is the tidal field, and the Einstein equations tie the curvature of spacetime to the energy within it. Return to any boxed definition or numbered derivation as a reference. The one idea beneath it all is coordinate-freedom: write physics in tensors, and the laws hold in every frame — which is why this single subject is the language in which gravity is written.*
