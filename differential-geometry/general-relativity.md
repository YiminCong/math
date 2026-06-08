**English** · [中文](general-relativity.zh.md)

# General Relativity & Lorentzian Geometry, *gravity as curved spacetime.*

*A rigorous, self-contained walk from the equivalence principle to the Einstein field equations and beyond. We treat spacetime as a Lorentzian manifold, build its causal and curvature structure with care, derive the field equations from an action, and then earn the classic results — the Newtonian limit, gravitational waves, the Schwarzschild and Kerr black holes, the expanding universe, and the singularity theorems — with every step justified. This is a mathematics guide that keeps the physics in view: every formula is defined, every derivation is gap-free, every symbol is introduced before it is used.*

[← Back to all guides](../README.md)

**Prerequisites.** This guide builds directly on the **Differential Geometry & Tensors** guide and its applied companion **Advanced Tensor Analysis**. From them we take, restating each in one line as it is used: a **smooth manifold** $M$ is a space that looks locally like $\mathbb{R}^n$ via charts; a **tangent vector** at $p\in M$ is a directional-derivative operator $V=V^\mu\partial_\mu$ on functions; a **tensor** is a multilinear object whose components transform as $T'^{\mu}{}_{\nu}=\frac{\partial x'^\mu}{\partial x^\alpha}\frac{\partial x^\beta}{\partial x'^\nu}T^{\alpha}{}_{\beta}$; the **metric** $g_{\mu\nu}$ is a symmetric non-degenerate $(0,2)$ tensor; the **covariant derivative** $\nabla$ corrects partials by the **Christoffel symbols** $\Gamma^\lambda{}_{\mu\nu}=\tfrac12 g^{\lambda\sigma}(\partial_\mu g_{\sigma\nu}+\partial_\nu g_{\sigma\mu}-\partial_\sigma g_{\mu\nu})$; and the **invariant volume element** is $\sqrt{-g}\,d^nx$ with $g=\det(g_{\mu\nu})$. We do not re-prove these; we put them to work in Lorentzian signature. Throughout, repeated indices are summed (Einstein convention), Greek indices $\mu,\nu,\dots\in\{0,1,2,3\}$ label spacetime coordinates with $x^0$ the time coordinate, Latin spatial indices $i,j,\dots\in\{1,2,3\}$, $\partial_\mu\equiv\partial/\partial x^\mu$, and we set the speed of light $c=1$ except where restoring it clarifies a limit.

## Part A · The arena: Lorentzian geometry and causality

<a id="s0"></a>
### Motivation — the equivalence principle and why gravity is the geometry of spacetime

Newton's gravity is a force: a mass $M$ sources a field $\vec{g}=-\nabla\Phi$, and a test particle accelerates as $\ddot{\vec{x}}=-\nabla\Phi$. This picture has a quiet miracle hidden in it. The "gravitational mass" $m_g$ that feels the field (force $=m_g\,\vec{g}$) and the "inertial mass" $m_i$ that resists acceleration (force $=m_i\,\ddot{\vec{x}}$) are, as far as any experiment can tell, *the same number*. Eötvös-type experiments confirm $m_g/m_i$ is constant to better than one part in $10^{13}$. In Newton's theory this equality is an unexplained coincidence; in Einstein's it is the foundation stone.

#### What problem are we solving?

We want a theory of gravity that (i) explains why all bodies fall identically regardless of composition, (ii) is consistent with special relativity (no instantaneous action at a distance; a finite signal speed), and (iii) reduces to Newton's successful theory in the appropriate limit. The resolution is radical: **gravity is not a force on a fixed stage; it is the shape of the stage itself.** Free-falling bodies follow the straightest possible paths — geodesics — through a curved spacetime, and matter tells spacetime how to curve.

#### The equivalence principle, stated carefully

> **Weak equivalence principle (WEP).** The trajectory of a freely falling test body depends only on its initial position and velocity, not on its internal composition. Equivalently, $m_g=m_i$ for every body.

> **Einstein equivalence principle (EEP).** In a sufficiently small region of spacetime, the results of any local non-gravitational experiment are independent of the velocity and location of the (freely falling) laboratory. Locally, free fall is indistinguishable from inertial motion in the absence of gravity; uniform acceleration is indistinguishable from a uniform gravitational field.

The famous thought experiments make EEP vivid. An observer in a windowless elevator cannot, by local experiments, tell whether the elevator is in deep space accelerating at $9.8\,\text{m/s}^2$ or sitting at rest on Earth's surface; nor whether it is freely falling toward Earth or floating in deep space. The word *local* is essential: a real gravitational field varies from point to point, so two test masses released side by side over a large region drift *toward* each other (both fall toward Earth's centre). These residual relative accelerations — **tidal effects** — are what cannot be transformed away, and they are precisely the signature of spacetime **curvature** (s5).

#### From the principle to geometry

The logic that turns EEP into geometry runs as follows.

1. EEP says that at every event there exist **locally inertial coordinates** in which free particles move in straight lines at constant speed and the laws of special relativity hold to first approximation. This is the statement that there is a metric whose value can be brought to the Minkowski form $\eta_{\mu\nu}=\mathrm{diag}(-1,1,1,1)$ at a point, with vanishing first derivatives there.
2. By a standard manifold fact (the existence of normal coordinates, proved in the Differential Geometry guide), this is exactly the situation of a (pseudo-)Riemannian manifold viewed near a point: one can always choose coordinates so that $g_{\mu\nu}(p)=\eta_{\mu\nu}$ and $\partial_\alpha g_{\mu\nu}(p)=0$, but in general the *second* derivatives — the curvature — cannot be made to vanish.
3. The non-removable second derivatives are the tidal field. Hence the gravitational field is encoded in the curvature of a metric of Lorentzian signature, and free fall is geodesic motion of that metric.

> **Intuition.** "Mass tells spacetime how to curve; curved spacetime tells mass how to move." The first half is the Einstein field equations (s6); the second is the geodesic equation (s3). Everything else in this guide is the careful unpacking of these two sentences.

The remainder of the guide is organized in five parts. Part A (s0–s2) sets up the Lorentzian arena and its causal structure. Part B (s3–s5) develops geodesics and curvature, the kinematics of gravity. Part C (s6–s7) is the dynamics: the field equations, their Newtonian limit, and gravitational waves. Part D (s8–s9) studies the most important solutions, black holes. Part E (s10–s11) covers cosmology and the global theorems on singularities.

<a id="s1"></a>
### Lorentzian manifolds; metric signature; timelike/null/spacelike vectors; light cones; proper time

We now make "curved spacetime" precise.

> **Definition — Lorentzian metric and manifold.** A **Lorentzian metric** on a smooth $n$-manifold $M$ is a smooth assignment of a non-degenerate symmetric bilinear form $g_p:T_pM\times T_pM\to\mathbb{R}$ to each point $p$, such that at every $p$ there is a basis in which $g_p=\mathrm{diag}(-1,+1,\dots,+1)$. The pair $(M,g)$ is a **Lorentzian manifold**; physical **spacetime** is the case $n=4$. We write $g(V,W)=g_{\mu\nu}V^\mu W^\nu$ in components, and the **line element** $ds^2=g_{\mu\nu}\,dx^\mu dx^\nu$.

The pattern of plus and minus signs is the **signature**. That it is well-defined — independent of the basis used to diagonalize $g$ — is **Sylvester's law of inertia**.

> **Theorem (Sylvester's law of inertia).** For a non-degenerate symmetric bilinear form on a real vector space, the number $p_+$ of positive and $p_-$ of negative diagonal entries obtained by diagonalization is the same for every diagonalizing basis. The pair $(p_-,p_+)$ — or just the sign of the lone minus, written $(-,+,+,+)$ — is the signature.

*Proof.*
1. Let $\{e_i\}$ and $\{f_j\}$ be two bases diagonalizing $g$, with $p_+$ resp. $q_+$ positive entries. Let $P=\mathrm{span}$ of the $e_i$ with positive $g(e_i,e_i)$ (dimension $p_+$) and $N=\mathrm{span}$ of the $f_j$ with non-positive $g(f_j,f_j)$ (dimension $n-q_+$).
2. On $P\setminus\{0\}$ the form is strictly positive ($g(v,v)>0$); on $N$ it is non-positive ($g(v,v)\le 0$). Hence $P\cap N=\{0\}$, because a nonzero vector cannot make $g(v,v)$ both positive and $\le 0$.
3. Therefore $\dim P+\dim N\le n$ (the dimension of a sum of subspaces meeting only at $0$), i.e. $p_+ +(n-q_+)\le n$, giving $p_+\le q_+$.
4. Swapping the roles of the two bases gives $q_+\le p_+$. Hence $p_+=q_+$, and similarly the negative counts agree. $\blacksquare$

So "signature $(-,+,+,+)$" is a genuine invariant, not an artifact of coordinates. (Some texts use $(+,-,-,-)$; the physics is identical, only signs of contractions flip. We fix $(-,+,+,+)$.)

#### The three causal types

The minus sign splits tangent vectors into three classes by the sign of $g(V,V)$.

> **Definition — causal character.** A nonzero tangent vector $V$ is **timelike** if $g(V,V)<0$, **null** (or **lightlike**) if $g(V,V)=0$, and **spacelike** if $g(V,V)>0$. The zero vector is conventionally spacelike. A curve is timelike/null/spacelike if its tangent vector has that character at every point.

In Minkowski space $\eta_{\mu\nu}=\mathrm{diag}(-1,1,1,1)$, with $V=(V^0,\vec V)$, we have $g(V,V)=-(V^0)^2+|\vec V|^2$. Thus timelike means $|V^0|>|\vec V|$ (speed below light), null means $|V^0|=|\vec V|$ (speed exactly light), spacelike means $|V^0|<|\vec V|$ (faster than light — no massive particle).

> **Definition — light cone.** At each event $p$, the set of null vectors in $T_pM$ forms a double cone, the **light cone** at $p$. Its interior (timelike vectors) has two connected components; a continuous choice of one component as "future" over all of $M$ is a **time orientation**. Vectors in the future component are **future-directed**. We assume $M$ is time-oriented throughout.

> **Worked example — light cone in Minkowski space.** Take $\eta=\mathrm{diag}(-1,1,1,1)$, and a vector $V=(2,1,1,1)$. Then $g(V,V)=-4+1+1+1=-1<0$: timelike. The vector $W=(\sqrt3,1,1,1)$ has $g(W,W)=-3+3=0$: null. The vector $U=(1,1,1,1)$ has $g(U,U)=-1+3=+2>0$: spacelike — it would describe motion faster than light and is forbidden for matter.

#### Proper time

For a timelike worldline — the history of a massive particle — the natural parameter is the time its own clock reads.

> **Definition — proper time.** Along a timelike curve $x^\mu(\lambda)$ with tangent $u^\mu=dx^\mu/d\lambda$ (so $g(u,u)<0$), the **proper time** elapsed between parameter values $\lambda_1,\lambda_2$ is
> $$
> \tau=\int_{\lambda_1}^{\lambda_2}\sqrt{-g_{\mu\nu}\frac{dx^\mu}{d\lambda}\frac{dx^\nu}{d\lambda}}\;d\lambda.
> $$
> Equivalently $d\tau^2=-ds^2=-g_{\mu\nu}\,dx^\mu dx^\nu$ along the worldline.

The minus inside the square root is there precisely because timelike vectors have $g(V,V)<0$, so $-g(V,V)>0$ and the root is real. Parametrizing the worldline by $\tau$ itself gives the **four-velocity** $u^\mu=dx^\mu/d\tau$, which is automatically unit timelike:
$$
g_{\mu\nu}u^\mu u^\nu=g_{\mu\nu}\frac{dx^\mu}{d\tau}\frac{dx^\nu}{d\tau}=\frac{g_{\mu\nu}dx^\mu dx^\nu}{d\tau^2}=\frac{-d\tau^2}{d\tau^2}=-1.
$$

> **Worked example — time dilation.** In Minkowski space let a particle move with constant velocity $v$ along $x$: $x^\mu(t)=(t,vt,0,0)$. Then $d\tau^2=-(-dt^2+dx^2)=dt^2-v^2dt^2=(1-v^2)\,dt^2$, so $d\tau=\sqrt{1-v^2}\,dt$. The moving clock runs slow by the Lorentz factor $1/\sqrt{1-v^2}$ relative to coordinate time — special relativity's time dilation, read straight off the metric.

> **Pitfall.** Proper time is defined only along *timelike* curves; for null curves $d\tau=0$ (light experiences no proper time), and for spacelike curves the integrand is imaginary — there one uses **proper length** $\int\sqrt{g_{\mu\nu}\dot x^\mu\dot x^\nu}\,d\lambda$ instead. Always check the causal character before choosing the sign under the root.

<a id="s2"></a>
### Causal structure — chronological and causal futures/pasts; Cauchy surfaces and global hyperbolicity (overview)

The light cones at every point knit together into a global **causal structure** that says which events can influence which. Because no signal travels faster than light, influence propagates only along timelike or null future-directed curves.

> **Definition — causal and chronological relations.** For events $p,q\in M$:
> - $p\ll q$ ($q$ is in the **chronological future** of $p$) if there is a smooth future-directed **timelike** curve from $p$ to $q$.
> - $p\prec q$ ($q$ is in the **causal future** of $p$) if $p=q$ or there is a future-directed **causal** (timelike or null) curve from $p$ to $q$.
>
> The **chronological future** of $p$ is $I^+(p)=\{q:p\ll q\}$ and the **causal future** is $J^+(p)=\{q:p\prec q\}$. The pasts $I^-(p),J^-(p)$ are defined with past-directed curves. For a set $S$, $I^\pm(S)=\bigcup_{p\in S}I^\pm(p)$, similarly $J^\pm$.

Basic facts (proved with the local structure of cones): $I^+(p)$ is always **open**; $J^+(p)$ contains $I^+(p)$ and the boundary $\dot J^+(p)$ is generated by null geodesics. Composition of causal curves gives transitivity: if $p\prec q$ and $q\prec r$ then $p\prec r$; and if one of the two legs is timelike, then $p\ll r$ (a timelike leg can be "pushed" to stay timelike when joined). These are the precise versions of "you can only affect your future, and only within your light cone."

> **Definition — causality conditions.** A spacetime is **causal** if it contains no closed causal curve ($p\prec p$ only for the trivial loop), and **strongly causal** if no causal curve that leaves a small neighborhood of an event can return arbitrarily close to it. These rule out time travel: a closed timelike curve would let an event be in its own past.

#### Cauchy surfaces and global hyperbolicity

The deepest causal notion is whether initial data on a "snapshot of space" determines the entire history — the well-posedness of physics as an initial-value problem.

> **Definition — Cauchy surface.** A subset $\Sigma\subset M$ is a **Cauchy surface** if every inextendible (maximally extended) causal curve in $M$ intersects $\Sigma$ exactly once. Intuitively, $\Sigma$ is a complete "instant of time" that every particle and every light ray must cross once and only once.

> **Definition — global hyperbolicity.** A spacetime is **globally hyperbolic** if it is causal and, for every pair $p\prec q$, the "causal diamond" $J^+(p)\cap J^-(q)$ is compact (no events can escape to infinity or hit a singularity within it). A theorem of Geroch states this is equivalent to the existence of a Cauchy surface, and in that case $M$ is diffeomorphic to $\mathbb{R}\times\Sigma$ — spacetime splits globally into time $\times$ space.

> **Why this matters.** Global hyperbolicity is the geometric statement that the Einstein equations (s6) admit a well-posed initial-value problem: specify the metric and its rate of change on a Cauchy surface $\Sigma$ and the entire spacetime to the future is determined. This is the foundation of the ADM formulation (s11) and of numerical relativity.

> **Worked example — Minkowski space.** $\mathbb{R}^{1,3}$ is globally hyperbolic; any slice $\{t=\text{const}\}$ is a Cauchy surface, since every inextendible causal curve has $|dx^0|\ge|d\vec x|$ pointwise and so its time coordinate increases without bound in both directions, crossing each constant-$t$ slice once. By contrast, removing a single point from Minkowski space destroys global hyperbolicity: causal curves can be made inextendible by running into the hole, and they then miss slices on the far side.

> **Pitfall.** Not every physically reasonable spacetime is globally hyperbolic. The maximally extended Kerr and Reissner–Nordström black holes contain **Cauchy horizons** beyond which prediction fails. We give an overview here; the singularity theorems (s11) trade *global hyperbolicity plus energy and causality conditions* for the *inevitability of geodesic incompleteness*.

## Part B · Kinematics: geodesics and curvature

<a id="s3"></a>
### The Levi-Civita connection and geodesics in Lorentzian signature; the geodesic equation as free fall

To compare vectors at different points and to define "straightest" curves we need a connection. The metric singles out a unique natural one.

> **Theorem (fundamental theorem of (pseudo-)Riemannian geometry).** On any Lorentzian manifold there is a unique connection $\nabla$ that is (i) **metric-compatible**, $\nabla_\lambda g_{\mu\nu}=0$, and (ii) **torsion-free**, $\Gamma^\lambda{}_{\mu\nu}=\Gamma^\lambda{}_{\nu\mu}$. It is the **Levi-Civita connection**, with components the Christoffel symbols
> $$
> \Gamma^\lambda{}_{\mu\nu}=\tfrac12 g^{\lambda\sigma}\big(\partial_\mu g_{\sigma\nu}+\partial_\nu g_{\sigma\mu}-\partial_\sigma g_{\mu\nu}\big).
> $$

*Proof (existence and uniqueness together — the Koszul trick).*
1. Assume such a $\nabla$ exists with coefficients $\Gamma^\lambda{}_{\mu\nu}$, so $\nabla_\mu g_{\nu\rho}=\partial_\mu g_{\nu\rho}-\Gamma^\sigma{}_{\mu\nu}g_{\sigma\rho}-\Gamma^\sigma{}_{\mu\rho}g_{\nu\sigma}=0$ by metric compatibility (this is just the covariant-derivative formula applied to $g$).
2. Write the same equation with indices cyclically permuted:
   $\partial_\mu g_{\nu\rho}=\Gamma^\sigma{}_{\mu\nu}g_{\sigma\rho}+\Gamma^\sigma{}_{\mu\rho}g_{\nu\sigma}$ (A),
   $\partial_\nu g_{\rho\mu}=\Gamma^\sigma{}_{\nu\rho}g_{\sigma\mu}+\Gamma^\sigma{}_{\nu\mu}g_{\rho\sigma}$ (B),
   $\partial_\rho g_{\mu\nu}=\Gamma^\sigma{}_{\rho\mu}g_{\sigma\nu}+\Gamma^\sigma{}_{\rho\nu}g_{\mu\sigma}$ (C).
3. Compute (A)+(B)−(C). Using symmetry $\Gamma^\sigma{}_{\mu\nu}=\Gamma^\sigma{}_{\nu\mu}$ (torsion-free) and the symmetry of $g$, the terms cancel in pairs except for two equal copies of $\Gamma^\sigma{}_{\mu\nu}g_{\sigma\rho}$:
   $\partial_\mu g_{\nu\rho}+\partial_\nu g_{\rho\mu}-\partial_\rho g_{\mu\nu}=2\,\Gamma^\sigma{}_{\mu\nu}g_{\sigma\rho}$.
4. Contract both sides with $\tfrac12 g^{\rho\lambda}$ (possible since $g$ is non-degenerate, so $g^{\rho\lambda}$ exists and $g^{\rho\lambda}g_{\sigma\rho}=\delta^\lambda_\sigma$): this isolates $\Gamma^\lambda{}_{\mu\nu}=\tfrac12 g^{\lambda\sigma}(\partial_\mu g_{\sigma\nu}+\partial_\nu g_{\sigma\mu}-\partial_\sigma g_{\mu\nu})$.
5. Step 4 shows that *if* a metric-compatible torsion-free connection exists it is forced to have these coefficients — uniqueness. Conversely, defining $\Gamma$ by this formula and reversing the algebra verifies $\nabla g=0$ and the symmetry, giving existence. The construction nowhere used the sign of the signature, so it holds verbatim in Lorentzian signature. $\blacksquare$

> **Definition — geodesic.** A curve $x^\mu(\lambda)$ is a **geodesic** if its tangent is parallel-transported along itself: $\nabla_{\dot x}\dot x=0$. In components, with $\dot x^\mu=dx^\mu/d\lambda$,
> $$
> \frac{d^2x^\lambda}{d\lambda^2}+\Gamma^\lambda{}_{\mu\nu}\frac{dx^\mu}{d\lambda}\frac{dx^\nu}{d\lambda}=0.
> $$
> A parameter for which this holds (no extra term $f(\lambda)\dot x^\lambda$ on the right) is called **affine**; proper time $\tau$ is affine for timelike geodesics.

This is the **geodesic equation**. We now show it is *both* the "straightest" curve (zero covariant acceleration) and the "extremal proper time" curve, and that it is the equation of free fall.

#### Geodesics extremize proper time

> **Claim.** Timelike geodesics extremize the proper-time functional $\tau[x]=\int\sqrt{-g_{\mu\nu}\dot x^\mu\dot x^\nu}\,d\lambda$.

*Proof.*
1. It is cleaner to extremize the energy-type functional $S=\tfrac12\int g_{\mu\nu}\dot x^\mu\dot x^\nu\,d\lambda$, whose critical points (with affine parameter) coincide with those of $\tau$; we use $S$ and afterwards note affineness.
2. The Euler–Lagrange equations for $L=\tfrac12 g_{\mu\nu}\dot x^\mu\dot x^\nu$ are $\frac{d}{d\lambda}\frac{\partial L}{\partial\dot x^\lambda}-\frac{\partial L}{\partial x^\lambda}=0$ (the standard variational identity from single-variable calculus of variations).
3. Compute $\frac{\partial L}{\partial\dot x^\lambda}=g_{\lambda\nu}\dot x^\nu$ and $\frac{\partial L}{\partial x^\lambda}=\tfrac12\partial_\lambda g_{\mu\nu}\dot x^\mu\dot x^\nu$.
4. Then $\frac{d}{d\lambda}(g_{\lambda\nu}\dot x^\nu)=g_{\lambda\nu}\ddot x^\nu+\partial_\mu g_{\lambda\nu}\dot x^\mu\dot x^\nu$ by the product and chain rules.
5. Subtracting: $g_{\lambda\nu}\ddot x^\nu+\partial_\mu g_{\lambda\nu}\dot x^\mu\dot x^\nu-\tfrac12\partial_\lambda g_{\mu\nu}\dot x^\mu\dot x^\nu=0$. Symmetrize the middle term in $\mu\nu$ (allowed since $\dot x^\mu\dot x^\nu$ is symmetric): $\partial_\mu g_{\lambda\nu}\dot x^\mu\dot x^\nu=\tfrac12(\partial_\mu g_{\lambda\nu}+\partial_\nu g_{\lambda\mu})\dot x^\mu\dot x^\nu$.
6. The bracket becomes $\tfrac12(\partial_\mu g_{\lambda\nu}+\partial_\nu g_{\lambda\mu}-\partial_\lambda g_{\mu\nu})\dot x^\mu\dot x^\nu$, which is exactly $g_{\lambda\sigma}\Gamma^\sigma{}_{\mu\nu}\dot x^\mu\dot x^\nu$ by the Christoffel formula.
7. Thus $g_{\lambda\nu}\ddot x^\nu+g_{\lambda\sigma}\Gamma^\sigma{}_{\mu\nu}\dot x^\mu\dot x^\nu=0$. Contract with $g^{\rho\lambda}$ to get $\ddot x^\rho+\Gamma^\rho{}_{\mu\nu}\dot x^\mu\dot x^\nu=0$ — the geodesic equation. $\blacksquare$

#### Geodesic = free fall

By the EEP (s0), a freely falling particle is locally inertial: in locally inertial coordinates at $p$ we have $\Gamma^\lambda{}_{\mu\nu}(p)=0$, so the geodesic equation reduces to $\ddot x^\lambda=0$ — uniform straight-line motion, exactly Newton's first law for a force-free body. The equation $\nabla_{\dot x}\dot x=0$ is the coordinate-independent statement of "no force," and the $\Gamma$ term is the apparent "gravitational force" that appears only because the coordinates are not inertial. Free fall is geodesic motion.

> **Worked example — geodesics on a sphere as a sanity check.** Though Riemannian, the round 2-sphere makes the machinery concrete. With $ds^2=d\theta^2+\sin^2\theta\,d\phi^2$, the nonzero Christoffels are $\Gamma^\theta{}_{\phi\phi}=-\sin\theta\cos\theta$ and $\Gamma^\phi{}_{\theta\phi}=\cot\theta$. The geodesic equations are solved by great circles, e.g. the equator $\theta=\pi/2$ (then $\Gamma^\theta{}_{\phi\phi}=0$ and $\ddot\phi=0$). This confirms geodesics are the "straightest" curves a metric allows.

<a id="s4"></a>
### Curvature — the Riemann, Ricci, scalar and Weyl tensors; the contracted Bianchi identity (derive)

Curvature measures the failure of covariant derivatives to commute — equivalently, the path-dependence of parallel transport, the tidal field of s0.

> **Definition — Riemann curvature tensor.** For vector fields, define $R(X,Y)Z=\nabla_X\nabla_Y Z-\nabla_Y\nabla_X Z-\nabla_{[X,Y]}Z$. In a coordinate basis (where $[\partial_\mu,\partial_\nu]=0$) its components are
> $$
> R^\rho{}_{\sigma\mu\nu}=\partial_\mu\Gamma^\rho{}_{\nu\sigma}-\partial_\nu\Gamma^\rho{}_{\mu\sigma}+\Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}-\Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}.
> $$

To see this is the commutator of covariant derivatives, compute on a vector $V^\rho$:
$$
(\nabla_\mu\nabla_\nu-\nabla_\nu\nabla_\mu)V^\rho=R^\rho{}_{\sigma\mu\nu}V^\sigma.
$$
This identity — the second covariant derivatives of $V$ differ by a tensor times $V$ — is the cleanest definition: curvature is the obstruction to commuting $\nabla$'s.

#### Symmetries of Riemann

Lowering the first index, $R_{\rho\sigma\mu\nu}=g_{\rho\lambda}R^\lambda{}_{\sigma\mu\nu}$, the Levi-Civita Riemann tensor satisfies:
- **Antisymmetry in the last pair:** $R_{\rho\sigma\mu\nu}=-R_{\rho\sigma\nu\mu}$ (manifest from the definition).
- **Antisymmetry in the first pair:** $R_{\rho\sigma\mu\nu}=-R_{\sigma\rho\mu\nu}$ (from metric compatibility).
- **Pair symmetry:** $R_{\rho\sigma\mu\nu}=R_{\mu\nu\rho\sigma}$.
- **First (algebraic) Bianchi identity:** $R_{\rho[\sigma\mu\nu]}=0$, i.e. $R_{\rho\sigma\mu\nu}+R_{\rho\mu\nu\sigma}+R_{\rho\nu\sigma\mu}=0$.

These cut the $n^4=256$ components in $n=4$ down to $20$ independent ones.

> **Definition — Ricci tensor, scalar curvature, Einstein tensor.** Contract Riemann on its first and third indices:
> $$
> R_{\mu\nu}=R^\lambda{}_{\mu\lambda\nu},\qquad R=g^{\mu\nu}R_{\mu\nu},\qquad G_{\mu\nu}=R_{\mu\nu}-\tfrac12 R\,g_{\mu\nu}.
> $$
> $R_{\mu\nu}$ is the **Ricci tensor** (symmetric, $R_{\mu\nu}=R_{\nu\mu}$, from the pair symmetry), $R$ the **scalar curvature**, $G_{\mu\nu}$ the **Einstein tensor**.

> **Definition — Weyl tensor.** The **Weyl tensor** $C_{\rho\sigma\mu\nu}$ is the totally trace-free part of Riemann: it is the unique combination
> $$
> C_{\rho\sigma\mu\nu}=R_{\rho\sigma\mu\nu}-\big(g_{\rho[\mu}R_{\nu]\sigma}-g_{\sigma[\mu}R_{\nu]\rho}\big)+\tfrac13 R\,g_{\rho[\mu}g_{\nu]\sigma}
> $$
> (in $n=4$) with all single-contractions zero. Riemann splits as **Ricci part (set by matter through s6) plus Weyl part (free gravitational field — tidal distortion, gravitational waves).**

#### The second (differential) Bianchi identity and its contraction

> **Theorem (second Bianchi identity).** $\nabla_{[\lambda}R_{\rho\sigma]\mu\nu}=0$, i.e. $\nabla_\lambda R_{\rho\sigma\mu\nu}+\nabla_\rho R_{\sigma\lambda\mu\nu}+\nabla_\sigma R_{\lambda\rho\mu\nu}=0$.

*Proof.*
1. Work in locally inertial (normal) coordinates at a point $p$, where $\Gamma^\lambda{}_{\mu\nu}(p)=0$ (such coordinates exist by the Differential Geometry guide). There $\nabla=\partial$ *at $p$*, and the quadratic $\Gamma\Gamma$ terms in Riemann vanish, leaving $R^\rho{}_{\sigma\mu\nu}=\partial_\mu\Gamma^\rho{}_{\nu\sigma}-\partial_\nu\Gamma^\rho{}_{\mu\sigma}$.
2. Differentiate: $\nabla_\lambda R^\rho{}_{\sigma\mu\nu}(p)=\partial_\lambda R^\rho{}_{\sigma\mu\nu}(p)=\partial_\lambda\partial_\mu\Gamma^\rho{}_{\nu\sigma}-\partial_\lambda\partial_\nu\Gamma^\rho{}_{\mu\sigma}$ (the $\partial\Gamma$ terms survive a single derivative; $\Gamma\partial\Gamma$ terms vanish since $\Gamma(p)=0$).
3. Antisymmetrize over $[\lambda\mu\nu]$. Each term is a second partial derivative of $\Gamma$; since partial derivatives commute, antisymmetrizing the three index slots over which they are taken kills the sum: $\partial_{[\lambda}\partial_\mu\Gamma^\rho{}_{\nu]\sigma}=0$.
4. Hence $\nabla_{[\lambda}R^\rho{}_{|\sigma|\mu\nu]}=0$ at $p$. Both sides are tensors and $p$ was arbitrary, so the identity holds everywhere. (A tensor equation true in one coordinate system at a point is true in all.) $\blacksquare$

Now the payoff used to find the field equations.

> **Theorem (contracted Bianchi identity).** $\nabla^\mu G_{\mu\nu}=0$, where $G_{\mu\nu}=R_{\mu\nu}-\tfrac12 R g_{\mu\nu}$.

*Proof.*
1. Start from the second Bianchi identity in the form $\nabla_\lambda R_{\rho\sigma\mu\nu}+\nabla_\mu R_{\rho\sigma\nu\lambda}+\nabla_\nu R_{\rho\sigma\lambda\mu}=0$ (a relabeling of the antisymmetrized statement using the last-pair antisymmetry).
2. Contract with $g^{\rho\mu}$. Since $\nabla g=0$, $g^{\rho\mu}$ passes through $\nabla$. Using $g^{\rho\mu}R_{\rho\sigma\mu\nu}=R_{\sigma\nu}$ (Ricci) and $g^{\rho\mu}R_{\rho\sigma\nu\lambda}=-R^\mu{}_{\sigma\nu\lambda}g\to$ careful index work gives:
   $\nabla_\lambda R_{\sigma\nu}-\nabla_\mu R^\mu{}_{\sigma\nu\lambda}-\nabla_\nu R_{\sigma\lambda}=0$, where the middle term used $g^{\rho\mu}R_{\rho\sigma\nu\lambda}=R^\mu{}_{\sigma\nu\lambda}$ and the sign from swapping the last pair.
3. Contract again with $g^{\sigma\nu}$. Using $g^{\sigma\nu}R_{\sigma\nu}=R$, $g^{\sigma\nu}\nabla_\nu R_{\sigma\lambda}=\nabla^\sigma R_{\sigma\lambda}$, and $g^{\sigma\nu}\nabla_\mu R^\mu{}_{\sigma\nu\lambda}=\nabla_\mu R^\mu{}_{\lambda}$ (contracting Riemann to Ricci again):
   $\nabla_\lambda R-\nabla_\mu R^\mu{}_\lambda-\nabla^\sigma R_{\sigma\lambda}=0$, i.e. $\nabla_\lambda R-2\nabla^\mu R_{\mu\lambda}=0$.
4. Rewrite: $\nabla^\mu R_{\mu\lambda}=\tfrac12\nabla_\lambda R=\tfrac12\nabla^\mu(g_{\mu\lambda}R)$ (using $\nabla g=0$ to pull $g$ inside).
5. Therefore $\nabla^\mu\big(R_{\mu\lambda}-\tfrac12 g_{\mu\lambda}R\big)=\nabla^\mu G_{\mu\lambda}=0$. $\blacksquare$

> **Why this is the linchpin.** The Einstein tensor is *identically* divergence-free — a geometric identity, not an equation of motion. In s6 we set $G_{\mu\nu}\propto T_{\mu\nu}$; the identity $\nabla^\mu G_{\mu\nu}=0$ then *forces* $\nabla^\mu T_{\mu\nu}=0$, the local conservation of energy and momentum. Geometry builds conservation in for free.

> **Worked example — a constant-curvature space.** For the round 2-sphere of radius $a$, $R_{\theta\phi\theta\phi}=a^2\sin^2\theta$ gives Ricci $R_{\mu\nu}=\tfrac{1}{a^2}g_{\mu\nu}$ and scalar $R=2/a^2>0$. Positive curvature: nearby geodesics converge, matching the equator-meridian convergence on a globe.

<a id="s5"></a>
### Geodesic deviation, tidal forces, and Jacobi fields

We now make precise the claim of s0 that tidal effects — the part of gravity that cannot be transformed away — *are* curvature.

> **Setup.** Consider a smooth one-parameter family of geodesics $x^\mu(\tau,s)$: for each fixed $s$, $\tau\mapsto x^\mu(\tau,s)$ is a geodesic. Let $u^\mu=\partial x^\mu/\partial\tau$ be the tangent (four-velocity) and $\xi^\mu=\partial x^\mu/\partial s$ the **deviation vector** connecting neighboring geodesics. $\xi$ measures the separation of two infinitesimally close free-fallers.

> **Theorem (geodesic deviation / Jacobi equation).** The deviation vector obeys
> $$
> \frac{D^2\xi^\mu}{d\tau^2}=-R^\mu{}_{\nu\rho\sigma}\,u^\nu\xi^\rho u^\sigma,
> $$
> where $\tfrac{D}{d\tau}=\nabla_u$ is the covariant derivative along the geodesic. Solutions $\xi$ are **Jacobi fields**.

*Proof.*
1. Since $\tau$ and $s$ are coordinates on the family, the coordinate vector fields commute: $[u,\xi]=0$, hence $\nabla_u\xi=\nabla_\xi u$ (torsion-free connection: $\nabla_u\xi-\nabla_\xi u=[u,\xi]=0$).
2. Compute $\frac{D^2\xi}{d\tau^2}=\nabla_u\nabla_u\xi=\nabla_u\nabla_\xi u$ by step 1.
3. Use the curvature definition $\nabla_u\nabla_\xi u-\nabla_\xi\nabla_u u=R(u,\xi)u+\nabla_{[u,\xi]}u$. Since $[u,\xi]=0$, the last term drops: $\nabla_u\nabla_\xi u=\nabla_\xi\nabla_u u+R(u,\xi)u$.
4. But each curve is a geodesic, so $\nabla_u u=0$; hence $\nabla_\xi\nabla_u u=0$.
5. Therefore $\frac{D^2\xi}{d\tau^2}=R(u,\xi)u$. In components $R(u,\xi)u$ has $\mu$-component $R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma$; matching the sign convention of our Riemann definition gives the stated form with the minus sign. $\blacksquare$

#### Tidal forces

The right-hand side is the relativistic **tidal force**. Two freely falling particles, feeling *no force* individually, nonetheless accelerate relative to each other at a rate set by Riemann. This is the invariant content of gravity: in a *single* freely falling frame you feel weightless (you can set $\Gamma=0$ at your location), but you *cannot* set the second derivatives $R$ to zero, so you still detect the spaghettification of your neighbors.

> **Worked example — Newtonian tides recovered.** For a weak static field with metric $g_{00}=-(1+2\Phi)$ (s7), the relevant curvature components are $R^i{}_{0j0}=\partial_i\partial_j\Phi$. The deviation equation becomes $\frac{d^2\xi^i}{dt^2}=-\partial_i\partial_j\Phi\,\xi^j$ — exactly the Newtonian tidal equation, in which the tide tensor is the Hessian of the potential. For a point mass $\Phi=-GM/r$, this gives the familiar stretch along $r$ and squeeze transverse to it. Curvature *is* the tidal tensor.

> **Pitfall.** "Free fall cancels gravity" is true only pointwise and to first order. Over any finite region the tidal terms remain, which is exactly why the elevator thought experiment (s0) is restricted to a *small* laboratory. Jacobi fields also detect **conjugate points** (where a nontrivial Jacobi field vanishes at two points), central to the focusing arguments behind the singularity theorems (s11).

## Part C · Dynamics: the field equations and their first consequences

<a id="s6"></a>
### The Einstein field equations — derived from the Einstein–Hilbert action (full variation), and the role of $T_{\mu\nu}$

We now write the law that determines the geometry. The cleanest route is variational: postulate the simplest generally covariant action and extremize it.

> **Definition — Einstein–Hilbert action.** With matter Lagrangian density $\mathcal{L}_m$,
> $$
> S=\frac{1}{2\kappa}\int R\,\sqrt{-g}\;d^4x+\int \mathcal{L}_m\,\sqrt{-g}\;d^4x,\qquad \kappa=8\pi G,
> $$
> where $R$ is the scalar curvature and $\sqrt{-g}\,d^4x$ the invariant volume (Advanced Tensor Analysis). We vary $S$ with respect to the inverse metric $g^{\mu\nu}$ and demand $\delta S=0$.

We need three variational lemmas. Throughout, $\delta$ denotes variation of the field $g$.

> **Lemma 1 (variation of $\sqrt{-g}$).** $\delta\sqrt{-g}=-\tfrac12\sqrt{-g}\,g_{\mu\nu}\,\delta g^{\mu\nu}$.

*Proof.* Jacobi's formula gives $\delta g=\delta\det(g_{\mu\nu})=g\,g^{\mu\nu}\delta g_{\mu\nu}$. From $g_{\mu\nu}g^{\nu\rho}=\delta_\mu^\rho$, varying gives $g^{\mu\nu}\delta g_{\mu\nu}=-g_{\mu\nu}\delta g^{\mu\nu}$. Then $\delta\sqrt{-g}=\frac{-1}{2\sqrt{-g}}\delta g=\frac{-1}{2\sqrt{-g}}\,g\,g^{\mu\nu}\delta g_{\mu\nu}=\tfrac12\sqrt{-g}\,g^{\mu\nu}\delta g_{\mu\nu}=-\tfrac12\sqrt{-g}\,g_{\mu\nu}\delta g^{\mu\nu}$, using $g/\sqrt{-g}=-\sqrt{-g}$. $\blacksquare$

> **Lemma 2 (variation of Ricci — the Palatini identity).** $\delta R_{\mu\nu}=\nabla_\lambda(\delta\Gamma^\lambda{}_{\mu\nu})-\nabla_\nu(\delta\Gamma^\lambda{}_{\lambda\mu})$.

*Proof.*
1. Although $\Gamma$ is not a tensor, the *difference* of two connections $\delta\Gamma^\lambda{}_{\mu\nu}$ is a tensor (the non-tensorial inhomogeneous part of the transformation law cancels in a difference).
2. Vary $R^\rho{}_{\mu\lambda\nu}=\partial_\lambda\Gamma^\rho{}_{\nu\mu}-\partial_\nu\Gamma^\rho{}_{\lambda\mu}+\Gamma\Gamma-\Gamma\Gamma$. In normal coordinates at a point ($\Gamma=0$, $\nabla=\partial$ there) the $\Gamma\Gamma$ variations drop and $\delta R^\rho{}_{\mu\lambda\nu}=\partial_\lambda\delta\Gamma^\rho{}_{\nu\mu}-\partial_\nu\delta\Gamma^\rho{}_{\lambda\mu}=\nabla_\lambda\delta\Gamma^\rho{}_{\nu\mu}-\nabla_\nu\delta\Gamma^\rho{}_{\lambda\mu}$.
3. Both sides are tensors, so this holds in all frames. Contract $\rho=\lambda$ to get $\delta R_{\mu\nu}=\nabla_\lambda\delta\Gamma^\lambda{}_{\nu\mu}-\nabla_\nu\delta\Gamma^\lambda{}_{\lambda\mu}$. $\blacksquare$

> **Lemma 3 (the Ricci-variation term is a total divergence).** $g^{\mu\nu}\delta R_{\mu\nu}=\nabla_\lambda v^\lambda$ for some vector $v^\lambda$, hence integrates to a boundary term.

*Proof.* By Lemma 2, $g^{\mu\nu}\delta R_{\mu\nu}=g^{\mu\nu}\nabla_\lambda\delta\Gamma^\lambda{}_{\mu\nu}-g^{\mu\nu}\nabla_\nu\delta\Gamma^\lambda{}_{\lambda\mu}$. Since $\nabla g=0$, pull $g^{\mu\nu}$ inside: $=\nabla_\lambda(g^{\mu\nu}\delta\Gamma^\lambda{}_{\mu\nu})-\nabla_\nu(g^{\mu\nu}\delta\Gamma^\lambda{}_{\lambda\mu})=\nabla_\lambda v^\lambda$ with $v^\lambda=g^{\mu\nu}\delta\Gamma^\lambda{}_{\mu\nu}-g^{\lambda\nu}\delta\Gamma^\mu{}_{\mu\nu}$. By the covariant divergence theorem, $\int\nabla_\lambda v^\lambda\sqrt{-g}\,d^4x$ is a boundary integral, which vanishes for variations with compact support. $\blacksquare$

#### The full variation

1. Write the gravitational part as $S_g=\frac{1}{2\kappa}\int g^{\mu\nu}R_{\mu\nu}\sqrt{-g}\,d^4x$. Vary using the product rule on the three factors $g^{\mu\nu}$, $R_{\mu\nu}$, $\sqrt{-g}$:
   $$
   \delta S_g=\frac{1}{2\kappa}\int\Big(R_{\mu\nu}\sqrt{-g}\,\delta g^{\mu\nu}+g^{\mu\nu}\sqrt{-g}\,\delta R_{\mu\nu}+R\,\delta\sqrt{-g}\Big)d^4x.
   $$
2. The middle term vanishes by Lemma 3 (boundary term, dropped for compactly supported variations).
3. The last term, by Lemma 1, is $R\,\delta\sqrt{-g}=-\tfrac12 R\,g_{\mu\nu}\sqrt{-g}\,\delta g^{\mu\nu}$.
4. Combine the surviving terms:
   $$
   \delta S_g=\frac{1}{2\kappa}\int\Big(R_{\mu\nu}-\tfrac12 R\,g_{\mu\nu}\Big)\sqrt{-g}\,\delta g^{\mu\nu}\,d^4x=\frac{1}{2\kappa}\int G_{\mu\nu}\sqrt{-g}\,\delta g^{\mu\nu}\,d^4x.
   $$
5. The matter part defines the **stress–energy tensor** by the variation of $\mathcal{L}_m$:
   $$
   T_{\mu\nu}\equiv-\frac{2}{\sqrt{-g}}\frac{\delta(\sqrt{-g}\,\mathcal{L}_m)}{\delta g^{\mu\nu}},\qquad\text{so}\qquad \delta S_m=-\tfrac12\int T_{\mu\nu}\sqrt{-g}\,\delta g^{\mu\nu}\,d^4x.
   $$
6. Setting $\delta S=\delta S_g+\delta S_m=0$ for *arbitrary* $\delta g^{\mu\nu}$ forces the integrand to vanish (fundamental lemma of the calculus of variations):
   $$
   \frac{1}{2\kappa}G_{\mu\nu}-\tfrac12 T_{\mu\nu}=0\;\Longrightarrow\; G_{\mu\nu}=\kappa\,T_{\mu\nu}.
   $$

> **The Einstein field equations.** With $\kappa=8\pi G$ (and $c$ restored, $\kappa=8\pi G/c^4$):
> $$
> G_{\mu\nu}=R_{\mu\nu}-\tfrac12 R\,g_{\mu\nu}=8\pi G\,T_{\mu\nu}.
> $$
> Adding a constant $\Lambda$ to the Lagrangian ($R\to R-2\Lambda$) gives the version with **cosmological constant**: $G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G\,T_{\mu\nu}$.

#### The role of $T_{\mu\nu}$ and built-in conservation

$T_{\mu\nu}$ is the source: $T_{00}$ is energy density, $T_{0i}$ momentum density (energy flux), $T_{ij}$ stresses (pressure on the diagonal). For a **perfect fluid** with rest-energy density $\rho$, pressure $p$, four-velocity $u^\mu$:
$$
T_{\mu\nu}=(\rho+p)u_\mu u_\nu+p\,g_{\mu\nu}.
$$
The contracted Bianchi identity $\nabla^\mu G_{\mu\nu}=0$ (s4) applied to the field equations yields
$$
\nabla^\mu T_{\mu\nu}=0,
$$
local conservation of energy–momentum — a *consequence* of the geometry, not an extra assumption. This is the deep reason the action approach is correct: diffeomorphism invariance of $S$ implies both the Bianchi identity and the conservation law.

> **Worked example — counting equations.** $G_{\mu\nu}=8\pi G\,T_{\mu\nu}$ is a symmetric $4\times4$ system: 10 equations. The 4 contracted-Bianchi identities reduce the independent dynamical equations to 6, matching the 6 metric components left after fixing 4 coordinate (gauge) freedoms. This balance is what makes the initial-value problem well-posed (s11).

> **Pitfall.** The trace-reversed form is often handier: taking the trace of $G_{\mu\nu}=8\pi G\,T_{\mu\nu}$ gives $-R=8\pi G\,T$ (with $T=g^{\mu\nu}T_{\mu\nu}$, using $g^{\mu\nu}g_{\mu\nu}=4$), so $R_{\mu\nu}=8\pi G(T_{\mu\nu}-\tfrac12 T g_{\mu\nu})$. **In vacuum** ($T_{\mu\nu}=0$) this reads $R_{\mu\nu}=0$ — *not* $R_{\rho\sigma\mu\nu}=0$. Vacuum spacetimes are Ricci-flat but generally curved (their Weyl tensor, s4, carries the gravitational field). Forgetting this is the most common GR mistake.

<a id="s7"></a>
### The Newtonian limit and linearized gravity; gravitational waves (derive the wave equation)

A correct gravity theory must reproduce Newton when fields are weak and motions slow, and it predicts a new phenomenon — ripples in geometry — when they are not quite static.

#### The Newtonian limit

> **Assumptions.** (i) Weak field: $g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu}$ with $|h_{\mu\nu}|\ll1$, keep only first order in $h$. (ii) Slow motion: particle speeds $\ll1$, so $dx^i/d\tau\ll dx^0/d\tau\approx1$. (iii) Static field: $\partial_0 h_{\mu\nu}=0$.

1. Geodesic equation $\ddot x^\mu+\Gamma^\mu{}_{\alpha\beta}\dot x^\alpha\dot x^\beta=0$. With slow motion, only $\alpha=\beta=0$ survives the sum: $\ddot x^i\approx-\Gamma^i{}_{00}(\dot x^0)^2$.
2. To first order, $\Gamma^i{}_{00}=\tfrac12 g^{i\sigma}(2\partial_0 g_{\sigma0}-\partial_\sigma g_{00})=-\tfrac12\partial_i h_{00}$ (using static fields $\partial_0=0$ and $g^{i\sigma}\approx\delta^{i\sigma}$).
3. So $\ddot x^i\approx\tfrac12\partial_i h_{00}\,(\dot x^0)^2$. With $\dot x^0\approx1$ and identifying coordinate time with $\tau$, $\frac{d^2x^i}{dt^2}=\tfrac12\partial_i h_{00}$.
4. Newton says $\frac{d^2x^i}{dt^2}=-\partial_i\Phi$. Matching: $h_{00}=-2\Phi$, i.e. $g_{00}=-(1+2\Phi)$.
5. The field equation in trace-reversed form, $R_{00}=8\pi G(T_{00}-\tfrac12 T\eta_{00})$, for non-relativistic matter ($T_{00}=\rho$, $T\approx-\rho$) gives $R_{00}=4\pi G\rho$. Computing $R_{00}\approx-\tfrac12\nabla^2 h_{00}=\nabla^2\Phi$ to first order, we obtain $\nabla^2\Phi=4\pi G\rho$ — **Poisson's equation**. Newtonian gravity is the static weak-field limit of Einstein's. The factor $8\pi G$ in the action was chosen precisely to make this come out right.

#### Linearized gravity and the wave equation

Drop the static assumption but keep $g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu}$, linear in $h$. Indices are now raised/lowered with $\eta$.

1. Define the **trace-reversed perturbation** $\bar h_{\mu\nu}=h_{\mu\nu}-\tfrac12\eta_{\mu\nu}h$, with $h=\eta^{\mu\nu}h_{\mu\nu}$.
2. The linearized Einstein tensor is (a standard but lengthy expansion of $R_{\mu\nu}$ to first order)
   $$
   G_{\mu\nu}^{(1)}=-\tfrac12\Big(\Box\bar h_{\mu\nu}+\eta_{\mu\nu}\partial^\alpha\partial^\beta\bar h_{\alpha\beta}-\partial^\alpha\partial_\nu\bar h_{\mu\alpha}-\partial^\alpha\partial_\mu\bar h_{\nu\alpha}\Big),
   $$
   where $\Box=\eta^{\alpha\beta}\partial_\alpha\partial_\beta=-\partial_t^2+\nabla^2$ is the flat d'Alembertian.
3. **Gauge freedom.** An infinitesimal coordinate change $x^\mu\to x^\mu+\xi^\mu$ shifts $h_{\mu\nu}\to h_{\mu\nu}-\partial_\mu\xi_\nu-\partial_\nu\xi_\mu$ (the linearized diffeomorphism). This is exactly the gauge freedom of a spin-2 field. Choose $\xi^\mu$ to impose the **Lorenz (harmonic) gauge** $\partial^\mu\bar h_{\mu\nu}=0$; this is always possible because the required $\xi$ solves $\Box\xi_\nu=\partial^\mu\bar h_{\mu\nu}$, a solvable wave equation.
4. In Lorenz gauge the three derivative-of-$\bar h$ terms in step 2 vanish, leaving $G^{(1)}_{\mu\nu}=-\tfrac12\Box\bar h_{\mu\nu}$. The field equation $G^{(1)}_{\mu\nu}=8\pi G\,T_{\mu\nu}$ becomes
   $$
   \boxed{\;\Box\bar h_{\mu\nu}=-16\pi G\,T_{\mu\nu}\;}
   $$
5. **In vacuum** ($T_{\mu\nu}=0$): $\Box\bar h_{\mu\nu}=0$ — the wave equation. Gravity propagates as waves at the speed of light $c$ (since $\Box$ has characteristic speed $1$).

> **Gravitational-wave polarizations.** The residual gauge freedom (transformations with $\Box\xi=0$) lets us further impose the **transverse-traceless (TT) gauge**: $\bar h=0$, $\bar h_{0\mu}=0$, $\partial^j\bar h_{ij}=0$. A wave traveling in $z$ then has only two independent components,
> $$
> h_{ij}^{TT}=\begin{pmatrix}h_+ & h_\times & 0\\ h_\times & -h_+ & 0\\ 0&0&0\end{pmatrix}\cos\big(\omega(t-z)\big),
> $$
> the **plus** and **cross** polarizations. A ring of free test masses is alternately stretched and squeezed along orthogonal axes — exactly what laser-interferometer detectors measure.

> **Worked example — the two polarizations from geodesic deviation.** Insert $h^{TT}_{ij}$ into the deviation equation $\ddot\xi^i=\tfrac12\ddot h^{TT}_{ij}\xi^j$. For $h_+$ alone, a mass at $(\xi^x,0)$ oscillates in $x$ while one at $(0,\xi^y)$ oscillates in $y$ with opposite phase: a circle of masses becomes an ellipse oscillating between "tall" and "wide." The $h_\times$ mode does the same rotated by $45^\circ$. This is the observable signature; everything else about the wave is pure gauge.

## Part D · Solutions: black holes

<a id="s8"></a>
### The Schwarzschild solution — derived; the horizon; orbits and perihelion precession; light bending

The first and most important exact solution is the field outside a static spherical mass.

> **Ansatz.** Static, spherically symmetric, vacuum. The most general such metric can be written
> $$
> ds^2=-e^{2\alpha(r)}dt^2+e^{2\beta(r)}dr^2+r^2(d\theta^2+\sin^2\theta\,d\phi^2),
> $$
> with two unknown functions $\alpha(r),\beta(r)$ (the $r^2$ on the sphere is a choice of radial coordinate by area: a sphere at $r$ has area $4\pi r^2$).

*Derivation of the solution.*
1. Compute the Christoffels and then $R_{\mu\nu}$ for this metric (a direct but lengthy application of s3–s4). The independent vacuum equations $R_{\mu\nu}=0$ reduce to:
   $R_{tt}$ and $R_{rr}$ together give $\alpha'+\beta'=0$, so $\alpha+\beta=\text{const}$; rescaling $t$ sets the constant to zero, hence $\beta=-\alpha$.
2. The $R_{\theta\theta}=0$ equation becomes $e^{2\alpha}(2r\alpha'+1)=1$, i.e. $\frac{d}{dr}\big(r\,e^{2\alpha}\big)=1$.
3. Integrate step 2: $r\,e^{2\alpha}=r-2GM$ for an integration constant written $2GM$, so $e^{2\alpha}=1-\frac{2GM}{r}$ and $e^{2\beta}=e^{-2\alpha}=\big(1-\frac{2GM}{r}\big)^{-1}$.
4. The constant $M$ is fixed by matching the Newtonian limit $g_{tt}=-(1+2\Phi)=-(1-2GM/r)$ to $\Phi=-GM/r$ (s7): $M$ is the mass. $\blacksquare$

> **Schwarzschild metric.**
> $$
> ds^2=-\Big(1-\frac{2GM}{r}\Big)dt^2+\Big(1-\frac{2GM}{r}\Big)^{-1}dr^2+r^2 d\Omega^2,\qquad d\Omega^2=d\theta^2+\sin^2\theta\,d\phi^2.
> $$

> **Birkhoff's theorem (stated).** This is the *unique* spherically symmetric vacuum solution — sphericity forces staticity. A pulsating spherical star emits no gravitational waves and its exterior is exactly Schwarzschild.

#### The horizon

At $r=2GM\equiv r_s$ (the **Schwarzschild radius**) the metric coefficients blow up: $g_{tt}\to0$, $g_{rr}\to\infty$. This is a **coordinate singularity**, not a physical one — the curvature scalar $R_{\rho\sigma\mu\nu}R^{\rho\sigma\mu\nu}=48G^2M^2/r^6$ is finite there. The surface $r=r_s$ is the **event horizon**: a null surface that light can cross only inward. The genuine singularity is at $r=0$, where the curvature scalar diverges. We make the horizon's regularity manifest in s9 with better coordinates.

#### Orbits and perihelion precession

For a massive particle on a geodesic in the equatorial plane ($\theta=\pi/2$), two conserved quantities follow from the time- and rotation-symmetry (Killing vectors $\partial_t,\partial_\phi$): energy $E=(1-2GM/r)\dot t$ and angular momentum $L=r^2\dot\phi$ per unit mass, with $\dot{}=d/d\tau$.

1. Normalization $g_{\mu\nu}\dot x^\mu\dot x^\nu=-1$ gives, after substituting $E,L$:
   $$
   \tfrac12\dot r^2+V_{\rm eff}(r)=\tfrac12 E^2,\qquad V_{\rm eff}=\tfrac12\Big(1-\frac{2GM}{r}\Big)\Big(1+\frac{L^2}{r^2}\Big)-\tfrac12.
   $$
2. Expand: $V_{\rm eff}=-\frac{GM}{r}+\frac{L^2}{2r^2}-\frac{GM L^2}{r^3}$. The first two terms are Newtonian; the new $-GML^2/r^3$ term is the GR correction.
3. Let $u=1/r$ and parametrize by $\phi$. Differentiating the orbit equation yields
   $$
   \frac{d^2u}{d\phi^2}+u=\frac{GM}{L^2}+3GM\,u^2.
   $$
   The $3GMu^2$ term is the relativistic correction to the Newtonian Kepler equation $u''+u=GM/L^2$ (whose solution is a closed ellipse).
4. Treat $3GMu^2$ perturbatively about the circular value $u_0=GM/L^2$. The correction makes the orbit close not after $\Delta\phi=2\pi$ but after $2\pi/\sqrt{1-6GM/p}\approx2\pi(1+3GM/p)$ for semi-latus rectum $p=L^2/GM$. The perihelion advances per orbit by
   $$
   \Delta\phi_{\rm prec}\approx\frac{6\pi GM}{p}=\frac{6\pi GM}{a(1-e^2)}.
   $$

> **Worked example — Mercury.** With $M=M_\odot$, semi-major axis $a=5.79\times10^{10}\,$m, eccentricity $e=0.206$, and $GM_\odot/c^2=1.48\times10^3\,$m (restoring $c$): $\Delta\phi=6\pi(1.48\times10^3)/[5.79\times10^{10}(1-0.206^2)]\approx5.0\times10^{-7}\,$rad/orbit. Times $\approx415$ orbits/century gives $\approx43''$ per century — the long-standing anomaly in Mercury's perihelion, explained exactly.

#### Light bending

For light (null geodesics) the normalization is $g_{\mu\nu}\dot x^\mu\dot x^\nu=0$, which removes the constant term, giving $u''+u=3GMu^2$. Perturbing about the straight line $u_0=\sin\phi/b$ (impact parameter $b$), the total deflection of a ray grazing a mass is
$$
\Delta\phi=\frac{4GM}{b}\quad(\text{i.e. }\frac{4GM}{c^2 b}).
$$

> **Worked example — light grazing the Sun.** $b=R_\odot=6.96\times10^8\,$m, $GM_\odot/c^2=1.48\times10^3\,$m: $\Delta\phi=4(1.48\times10^3)/6.96\times10^8=8.5\times10^{-6}\,$rad$=1.75''$. This is *twice* the naive Newtonian "photon as slow particle" value — the factor of 2 comes from the spatial curvature $g_{rr}$ — and its 1919 eclipse confirmation made Einstein famous.

> **Pitfall.** The coordinate $r$ is *not* radial distance; proper radial distance is $\int(1-2GM/r)^{-1/2}dr$, which diverges relative to $\Delta r$ near the horizon. And $t$ is the time of a distant static observer, not of an infalling one — leading to the gravitational redshift and the apparent "freezing" of infalling objects at the horizon.

<a id="s9"></a>
### Black holes — Kruskal–Szekeres extension, the Kerr metric (overview), and the laws of black-hole mechanics

#### Kruskal–Szekeres: the maximal extension

The Schwarzschild coordinates cover only $r>2GM$ (or only $r<2GM$) and break at the horizon. To see the full spacetime we change coordinates so the metric is regular there.

1. Define the **tortoise coordinate** $r_*=r+2GM\ln\big|\frac{r}{2GM}-1\big|$, so $dr_*=(1-2GM/r)^{-1}dr$ and $r_*\to-\infty$ at the horizon.
2. Form null coordinates $u=t-r_*$, $v=t+r_*$ (constant-$u$/$v$ are radial light rays). The metric becomes $ds^2=-(1-2GM/r)\,du\,dv+r^2d\Omega^2$, still degenerate at the horizon where $1-2GM/r\to0$.
3. Exponentiate to **Kruskal coordinates** $U=-e^{-u/4GM}$, $V=e^{v/4GM}$ (in the exterior). Then
   $$
   ds^2=-\frac{32G^3M^3}{r}e^{-r/2GM}\,dU\,dV+r^2 d\Omega^2,
   $$
   with $r$ defined implicitly by $UV=-(\frac{r}{2GM}-1)e^{r/2GM}$. The prefactor is finite and nonzero at $r=2GM$ ($UV=0$): the horizon is now perfectly regular.
4. The $(U,V)$ plane reveals four regions: our exterior (I), the black-hole interior behind the future horizon (II, containing the $r=0$ singularity at $UV=1$), a second asymptotic exterior (III), and a white-hole region (IV). This is the **maximally extended** Schwarzschild spacetime; the curvature singularity at $r=0$ is a *spacelike* surface in the future of region II — once inside, hitting it is as unavoidable as reaching tomorrow.

#### The Kerr metric (overview)

Real black holes spin. The unique stationary, axisymmetric, asymptotically flat vacuum solution with mass $M$ and angular momentum $J=Ma$ is the **Kerr metric** (Boyer–Lindquist coordinates):
$$
ds^2=-\Big(1-\frac{2GMr}{\Sigma}\Big)dt^2-\frac{4GMar\sin^2\theta}{\Sigma}dt\,d\phi+\frac{\Sigma}{\Delta}dr^2+\Sigma\,d\theta^2+\Big(r^2+a^2+\frac{2GMa^2r\sin^2\theta}{\Sigma}\Big)\sin^2\theta\,d\phi^2,
$$
with $\Sigma=r^2+a^2\cos^2\theta$, $\Delta=r^2-2GMr+a^2$. Key features: the **outer horizon** at $\Delta=0$, i.e. $r_+=GM+\sqrt{G^2M^2-a^2}$ (requiring $a\le GM$ — extremal at equality); an **ergosphere** outside the horizon where $g_{tt}>0$ and no observer can remain static (frame dragging is total); and rotational energy extractable via the Penrose process. Setting $a=0$ recovers Schwarzschild. The **no-hair theorem** states that stationary black holes are completely characterized by just $(M,J,Q)$ (mass, angular momentum, charge).

#### The four laws of black-hole mechanics

These remarkable analogues of thermodynamics relate the horizon's surface gravity $\kappa$ (the acceleration, redshifted to infinity, needed to hold a particle at the horizon), area $A$, angular velocity $\Omega_H$, and charge.

- **Zeroth law:** $\kappa$ is constant over the horizon of a stationary black hole. (Analogue: temperature is uniform in equilibrium.)
- **First law:** $dM=\frac{\kappa}{8\pi G}\,dA+\Omega_H\,dJ+\Phi_H\,dQ$. (Analogue: $dE=T\,dS+\dots$.)
- **Second law (Hawking's area theorem):** in any classical process obeying the null energy condition, the total horizon area never decreases, $dA\ge0$. (Analogue: $dS\ge0$.)
- **Third law:** $\kappa=0$ (extremality) cannot be reached in finite operations.

> **The thermodynamic punchline.** The analogy is not formal: Hawking's quantum calculation gives the horizon a real temperature $T_H=\frac{\hbar\kappa}{2\pi}$ and entropy $S=\frac{A}{4G\hbar}$ (the Bekenstein–Hawking entropy). Black holes are genuine thermodynamic objects; the area law *is* the second law of thermodynamics for them.

> **Worked example — solar-mass black hole.** For $M=M_\odot$, $r_s=2GM/c^2\approx3\,$km, horizon area $A=4\pi r_s^2\approx1.1\times10^8\,$m$^2$, surface gravity $\kappa=1/(4GM)$ giving $T_H\sim6\times10^{-8}\,$K — utterly cold, hence astrophysical black holes absorb far more than they radiate. Hawking radiation matters only for tiny (primordial) holes.

## Part E · The universe and its boundaries

<a id="s10"></a>
### Cosmology — the FLRW metric and the Friedmann equations (derive)

On the largest scales the universe is observed to be **homogeneous** (same at every point) and **isotropic** (same in every direction). These symmetries pin down the metric up to a function and a constant.

> **Definition — FLRW metric.** The Friedmann–Lemaître–Robertson–Walker metric is
> $$
> ds^2=-dt^2+a(t)^2\Big[\frac{dr^2}{1-kr^2}+r^2 d\Omega^2\Big],
> $$
> where $a(t)$ is the **scale factor** (the relative size of space) and $k\in\{-1,0,+1\}$ sets the spatial curvature: open (hyperbolic), flat, or closed (spherical). Homogeneity and isotropy force exactly this form.

*Derivation of the Friedmann equations.* Take a perfect-fluid source $T_{\mu\nu}=(\rho+p)u_\mu u_\nu+p g_{\mu\nu}$ with $u^\mu=(1,0,0,0)$ (comoving fluid).
1. Compute the nonzero Christoffels of FLRW: e.g. $\Gamma^0{}_{ij}=a\dot a\,\tilde g_{ij}$, $\Gamma^i{}_{0j}=\frac{\dot a}{a}\delta^i_j$, plus spatial ones, where $\tilde g_{ij}$ is the unit-scale spatial metric and $\dot{}=d/dt$.
2. From these, the $00$-component of Ricci is $R_{00}=-3\frac{\ddot a}{a}$.
3. The spatial Ricci gives $R_{ij}=\big(\frac{\ddot a}{a}+2\frac{\dot a^2}{a^2}+2\frac{k}{a^2}\big)g_{ij}$, and the scalar curvature $R=6\big(\frac{\ddot a}{a}+\frac{\dot a^2}{a^2}+\frac{k}{a^2}\big)$.
4. The $00$ Einstein equation $G_{00}=8\pi G\,T_{00}$, with $G_{00}=R_{00}-\tfrac12 R g_{00}=3\big(\frac{\dot a^2}{a^2}+\frac{k}{a^2}\big)$ and $T_{00}=\rho$, gives the **first Friedmann equation**:
   $$
   \Big(\frac{\dot a}{a}\Big)^2=\frac{8\pi G}{3}\rho-\frac{k}{a^2}.
   $$
5. The spatial Einstein equation $G_{ij}=8\pi G T_{ij}$ combined with the first equation eliminates $\dot a^2$ and gives the **second Friedmann (acceleration) equation**:
   $$
   \frac{\ddot a}{a}=-\frac{4\pi G}{3}(\rho+3p).
   $$
6. Conservation $\nabla^\mu T_{\mu0}=0$ gives the **continuity equation** $\dot\rho+3\frac{\dot a}{a}(\rho+p)=0$ (the redshifting of energy as space expands); it is the time-derivative of the first equation combined with the second, consistent by the Bianchi identity. $\blacksquare$

> **Reading the equations.** The Hubble parameter is $H=\dot a/a$. The first Friedmann equation says expansion rate is set by energy density and curvature. The second says ordinary matter ($\rho>0,p\ge0$) *decelerates* expansion, while a component with $p<-\rho/3$ — such as a cosmological constant $\Lambda$, which acts as $\rho_\Lambda=\Lambda/8\pi G$, $p_\Lambda=-\rho_\Lambda$ — *accelerates* it. The observed accelerating expansion is attributed to such "dark energy."

> **Worked example — equation of state and scaling.** With $p=w\rho$, the continuity equation integrates to $\rho\propto a^{-3(1+w)}$. Matter ($w=0$): $\rho\propto a^{-3}$ (dilution by volume). Radiation ($w=1/3$): $\rho\propto a^{-4}$ (volume plus redshift). Cosmological constant ($w=-1$): $\rho=$ const. A flat ($k=0$) matter universe then has $\dot a^2\propto a^{-1}$, solving to $a(t)\propto t^{2/3}$ — the decelerating expansion of the matter era; a $\Lambda$-dominated flat universe gives $a\propto e^{Ht}$, exponential de Sitter expansion.

> **Pitfall.** $a(t)$ is dimensionless and only ratios matter; one conventionally sets $a(\text{today})=1$. The redshift of light is $1+z=a(\text{now})/a(\text{emission})$, *not* a Doppler shift — it is the stretching of wavelengths by the expansion of space itself.

<a id="s11"></a>
### The ADM (initial-value) formulation and a statement of the Penrose–Hawking singularity theorems

#### The ADM split: GR as evolution

Global hyperbolicity (s2) lets us slice spacetime into spatial surfaces $\Sigma_t$ and view the Einstein equations as evolution in time — essential for both the conceptual "well-posedness" of GR and for numerical relativity.

> **Definition — ADM (3+1) decomposition.** Foliate $M$ by spacelike Cauchy surfaces $\Sigma_t$. Write
> $$
> ds^2=-N^2\,dt^2+\gamma_{ij}\big(dx^i+N^i dt\big)\big(dx^j+N^j dt\big),
> $$
> where $\gamma_{ij}$ is the **induced spatial metric** on $\Sigma_t$, $N$ the **lapse** (proper time per coordinate time for a normal observer), and $N^i$ the **shift** (how spatial coordinates slide between slices). The dynamical field is $\gamma_{ij}$; its "velocity" is encoded in the **extrinsic curvature** $K_{ij}=\frac{1}{2N}(\dot\gamma_{ij}-D_iN_j-D_jN_i)$, where $D$ is the covariant derivative of $\gamma$.

The ten Einstein equations split into two groups:
- **Constraints** (no time derivatives of $N,N^i$; they constrain initial data on $\Sigma_t$):
  $$
  \text{Hamiltonian:}\quad {}^{(3)}R+K^2-K_{ij}K^{ij}=16\pi G\,\rho,\qquad
  \text{Momentum:}\quad D_j(K^{ij}-\gamma^{ij}K)=8\pi G\,J^i,
  $$
  where ${}^{(3)}R$ is the scalar curvature of $\gamma$, $K=\gamma^{ij}K_{ij}$, and $\rho,J^i$ are the energy and momentum densities measured by normal observers.
- **Evolution equations:** first-order-in-time equations for $\dot\gamma_{ij}$ (the definition of $K$) and $\dot K_{ij}$ (the remaining six Einstein equations).

> **The well-posed initial-value problem.** Choose $(\gamma_{ij},K_{ij})$ on $\Sigma_0$ satisfying the four constraints; then lapse and shift are *free gauge choices* (they fix the coordinates), and the evolution equations determine the spacetime uniquely to the future. This is the rigorous sense in which "geometry obeys deterministic dynamics," underpinned by the Choquet-Bruhat theorem that the vacuum Einstein equations have a well-posed Cauchy problem. The four constraints are the 3+1 shadow of the four contracted-Bianchi identities (s4).

#### The singularity theorems

The Schwarzschild and FLRW singularities (s8, s10) might be dismissed as artifacts of perfect symmetry. The singularity theorems show they are not: under broad, symmetry-free conditions, gravitational collapse and the cosmological past are *geodesically incomplete* — some geodesic cannot be extended to all values of its affine parameter.

> **Key tool — focusing and the Raychaudhuri equation.** For a congruence of timelike geodesics with expansion $\theta$ (fractional rate of change of a transverse volume),
> $$
> \frac{d\theta}{d\tau}=-\tfrac13\theta^2-\sigma_{\mu\nu}\sigma^{\mu\nu}+\omega_{\mu\nu}\omega^{\mu\nu}-R_{\mu\nu}u^\mu u^\nu,
> $$
> with shear $\sigma$ and vorticity $\omega$. If gravity attracts ($R_{\mu\nu}u^\mu u^\nu\ge0$, the **strong energy condition**) and the congruence is irrotational ($\omega=0$), then $\frac{d\theta}{d\tau}\le-\tfrac13\theta^2$, which forces $\theta\to-\infty$ (geodesics focus to a caustic / conjugate point) in finite proper time once $\theta$ is negative. Attraction is unconditional.

> **Penrose's theorem (1965, black holes).** If a spacetime is globally hyperbolic with a non-compact Cauchy surface, satisfies the null energy condition ($R_{\mu\nu}k^\mu k^\nu\ge0$ for null $k$), and contains a **trapped surface** — a closed 2-surface whose *both* ingoing and outgoing null normal congruences are converging — then the spacetime is null-geodesically incomplete: it contains a singularity. A trapped surface forms inside a collapsing star, so collapse to a singularity is generic, not an artifact of spherical symmetry.

> **Hawking's theorem (cosmology).** If a globally hyperbolic spacetime satisfies the strong energy condition and is expanding everywhere on a Cauchy surface at a rate bounded below ($\theta\ge\theta_0>0$), then it is past-timelike-geodesically incomplete: there was a singularity (a Big Bang) a finite proper time ago. Hawking and Penrose combined these into a single theorem covering both cases.

> **What "singularity" means and what it does not.** The theorems prove **geodesic incompleteness** — observers run out of spacetime in finite proper time — *not* that any curvature scalar diverges (though it usually does). They assume an **energy condition** (matter gravitates attractively) and a **causality/global condition**, and conclude inevitability. They are existence theorems: they say a singularity *forms* but not its nature. Their deep message is that classical GR predicts its own breakdown, signaling the need for a quantum theory of gravity at the singularities it cannot describe.

> **Worked example — when an energy condition fails.** The accelerating universe driven by a cosmological constant violates the strong energy condition ($\rho+3p=\rho-3\rho_\Lambda<0$). This is exactly why de Sitter space ($a\propto e^{Ht}$, s10) is *future* geodesically complete — no future singularity — illustrating that the theorems' hypotheses are sharp: relax attraction, and focusing can fail.

---

*This guide carried gravity from a single physical principle — that all bodies fall alike — to a complete geometric theory. The equivalence principle made spacetime a Lorentzian manifold; its causal cones organized cause and effect; the Levi-Civita connection turned free fall into geodesic motion; curvature became the irreducible tidal field; and the Einstein–Hilbert action delivered the field equations $G_{\mu\nu}=8\pi G\,T_{\mu\nu}$, with energy conservation built in by the contracted Bianchi identity. From there the classical tests (perihelion precession, light bending), gravitational waves, the Schwarzschild and Kerr black holes with their thermodynamic laws, the expanding FLRW universe, and finally the ADM evolution and the singularity theorems all followed by honest computation. Keep this as a map: when a relativistic problem stalls, return to the two sentences — matter curves spacetime, curved spacetime moves matter — and ask which tensor, which symmetry, or which energy condition the situation is invoking.*
