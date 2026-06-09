**English** · [中文](stochastic-pdes.zh.md)

# Stochastic Partial Differential Equations, *fields driven by noise.*

*A self-contained first course in partial differential equations that are kicked at every point of space and every instant of time by randomness. We build Gaussian measures on infinite-dimensional spaces, define space–time white noise and the cylindrical Wiener process, solve the stochastic heat equation by the semigroup (mild) formula, develop Itô calculus in a Hilbert space, prove existence and uniqueness for semilinear equations by a contraction argument, confront the analytically ill-posed Kardar–Parisi–Zhang equation, measure the Hölder regularity of solutions and watch it collapse with spatial dimension, and meet the modern machinery — the Da Prato–Debussche trick, regularity structures, and paracontrolled calculus — that renormalizes the divergences. We finish with stochastic quantization, where the $\Phi^4$ quantum field measure appears as the equilibrium of an SPDE. Every term is defined on first use, every formula motivated, and every derivation is a numbered, gap-free chain of reasons. Built on basic calculus together with the companion Stochastic Processes & Path Integrals, Partial Differential Equations, and Functional Analysis guides.*

[← Back to all guides](../README.md)

## Part A · From randomness to fields

<a id="s0"></a>
### Motivation — noisy fields: growing interfaces, turbulence, and the dynamics of quantum field theory

#### What this guide is about, in one breath

An ordinary **partial differential equation (PDE)** — an equation relating a function $u(t,x)$ of time $t$ and space $x$ to its partial derivatives — describes a *deterministic* field: give me the initial shape and the boundary conditions and the field is fixed for all time. But many fields in nature are not deterministic. A burning sheet of paper has an edge that advances raggedly; a crystal grows with a roughened surface; the velocity of a turbulent fluid fluctuates at every point; a quantum field jitters because of vacuum fluctuations. The mathematics that captures "a field that obeys a PDE *while being buffeted by chance at every point*" is the theory of **stochastic partial differential equations (SPDEs)**. An SPDE is, loosely, a PDE with an extra random forcing term, written schematically

$$
\partial_t u = \mathcal{L}u + F(u) + \xi,
$$

where $\mathcal{L}$ is a differential operator (say the Laplacian $\Delta$), $F$ is a nonlinearity, and $\xi$ is a **noise** — a random function of space and time. This guide builds that theory from the ground up.

#### Four motivating pictures

- **Growing interfaces.** Imagine the edge between burnt and unburnt paper, or the surface of a film deposited atom by atom. Let $h(t,x)$ be the height of the interface above the horizontal position $x$ at time $t$. Locally the surface tends to smooth itself (a diffusion term $\nu\,\partial_x^2 h$), it grows faster where it is tilted (a nonlinear term $\tfrac{\lambda}{2}(\partial_x h)^2$), and random deposition adds noise $\xi$. This is exactly the **Kardar–Parisi–Zhang (KPZ) equation** (§s6), one of the most studied and most singular SPDEs.

- **Turbulence.** The Navier–Stokes equations of fluid flow, driven by a random force to model stirring, are an SPDE. Even the simplest stochastically forced models inherit the central difficulty: nonlinear interaction of fluctuations across all scales.

- **Quantum field theory in disguise.** The **stochastic quantization** program of Parisi and Wu (§s10) says: to sample the probability measure of a Euclidean quantum field — for instance the $\Phi^4$ measure of a self-interacting scalar field — run an SPDE forward in a fictitious extra "time" until it reaches equilibrium. The invariant measure of the SPDE *is* the quantum field measure. Thus SPDEs are a computational and conceptual gateway into **constructive quantum field theory** (§s11).

- **Noise-driven pattern formation.** Chemical reaction–diffusion systems, population models, and phase-separation dynamics all become SPDEs once one admits that reactions and migrations are intrinsically random at the microscopic level.

#### The whole guide on one line

> Gaussian measures → white noise → cylindrical Wiener process → stochastic heat equation → infinite-dimensional Itô calculus → existence/uniqueness → KPZ → regularity → Da Prato–Debussche → regularity structures → stochastic quantization → Euclidean QFT

#### The three prerequisites, restated in one line each

We lean on three companion guides; here is the single most important fact from each, restated so this guide stands alone.

- From **Stochastic Processes & Path Integrals**: a **Brownian motion (Wiener process)** $W_t$ is a random continuous path with $W_0=0$, independent increments, and $W_t-W_s\sim\mathcal{N}(0,t-s)$ (a normal/Gaussian variable of mean $0$ and variance $t-s$); the **Itô integral** $\int_0^t \sigma_s\,dW_s$ defines integration against this path, with the **Itô isometry** $\mathbb{E}\big[(\int_0^t\sigma_s\,dW_s)^2\big]=\mathbb{E}\int_0^t\sigma_s^2\,ds$.

- From **Partial Differential Equations**: the **heat equation** $\partial_t u=\Delta u$ has solution $u(t)=e^{t\Delta}u_0$, where the **heat semigroup** $e^{t\Delta}$ smooths the initial data $u_0$ by convolving it with the Gaussian heat kernel; $\Delta=\sum_i\partial_{x_i}^2$ is the **Laplacian**.

- From **Functional Analysis**: a **Hilbert space** $H$ is a complete vector space with an inner product $\langle\cdot,\cdot\rangle$; a **bounded linear operator** $A:H\to H$ has finite norm $\|A\|=\sup_{\|x\|=1}\|Ax\|$; an operator is **trace class** if the sum of its eigenvalues converges absolutely, and **Hilbert–Schmidt** if the sum of squares of its eigenvalues (its matrix entries) converges.

#### Common pitfalls, stated up front

- The noise $\xi$ is *not* an ordinary function. As we will prove (§s1), white noise has no pointwise values; it lives only as a generalized object (a distribution). Treating $\xi(t,x)$ as a number is the original sin that the whole edifice of this guide is built to avoid.
- "Adding a little noise" to a PDE can change its mathematical nature completely. For the KPZ equation the naive equation has *no solution at all* in the classical sense (§s6); making sense of it required a Fields-Medal-winning theory.

<a id="s1"></a>
### Gaussian measures on function spaces and white noise

#### What & why

In finite dimensions a Gaussian random vector is governed by a mean vector and a covariance matrix. To randomize an entire *function* — an element of an infinite-dimensional space — we need the analogue: a **Gaussian measure** on a function space. White noise is the most important such measure. We build it carefully because every later object (space–time white noise, the cylindrical Wiener process, the solution of the stochastic heat equation) is assembled from it.

#### Finite-dimensional Gaussians, restated

A random vector $X=(X_1,\dots,X_n)\in\mathbb{R}^n$ is **Gaussian** with mean $0$ and covariance matrix $Q$ (a symmetric positive semidefinite $n\times n$ matrix) when, for every fixed vector $v\in\mathbb{R}^n$, the scalar $\langle v,X\rangle=\sum_i v_iX_i$ is a one-dimensional normal variable with mean $0$ and variance $\langle v,Qv\rangle$. The cleanest fingerprint is the **characteristic function** (the expectation of the complex exponential):

$$
\mathbb{E}\big[e^{i\langle v,X\rangle}\big]=\exp\!\Big(-\tfrac12\langle v,Qv\rangle\Big).
$$

This single formula, read for all $v$, *defines* the law of $X$. We will lift exactly this formula to infinite dimensions.

#### Gaussian measures on a Hilbert space — definition

> **Definition — Gaussian measure on a Hilbert space.**
> Let $H$ be a separable Hilbert space (one with a countable orthonormal basis). A probability measure $\mu$ on $H$ is **Gaussian with mean $0$ and covariance operator $Q$** (where $Q:H\to H$ is symmetric, positive, and **trace class**) if for every $v\in H$
> $$
> \int_H e^{i\langle v,x\rangle}\,\mu(dx)=\exp\!\Big(-\tfrac12\langle v,Qv\rangle\Big).
> $$

The requirement that $Q$ be **trace class** — that $\mathrm{Tr}Q=\sum_k\langle Qe_k,e_k\rangle<\infty$ for an orthonormal basis $\{e_k\}$ — is not a technicality but the heart of the matter. Here is why, derived completely.

> **Proposition.** If a Gaussian measure $\mu$ with covariance $Q$ lives on $H$ (so $\int_H\|x\|^2\,\mu(dx)<\infty$), then $\mathrm{Tr}Q<\infty$.

**Derivation.**
1. Fix an orthonormal basis $\{e_k\}_{k\ge1}$ of $H$. By definition of the norm via Parseval's identity (a Hilbert-space fact), $\|x\|^2=\sum_k\langle x,e_k\rangle^2$ for every $x\in H$.
2. Take the expectation under $\mu$ and exchange sum and integral, allowed because all terms are nonnegative (monotone convergence theorem): $\int_H\|x\|^2\,\mu(dx)=\sum_k\int_H\langle x,e_k\rangle^2\,\mu(dx)$.
3. For each fixed $k$, the scalar $\langle x,e_k\rangle$ is, by the defining characteristic function with $v=e_k$, a one-dimensional centered normal with variance $\langle Qe_k,e_k\rangle$. Hence its second moment is exactly $\int_H\langle x,e_k\rangle^2\,\mu(dx)=\langle Qe_k,e_k\rangle$, by the definition of variance.
4. Combining steps 2 and 3: $\int_H\|x\|^2\,\mu(dx)=\sum_k\langle Qe_k,e_k\rangle=\mathrm{Tr}Q$.
5. The left side is finite by hypothesis, so $\mathrm{Tr}Q<\infty$. $\blacksquare$

The contrapositive is the lesson: **if $Q$ is not trace class, the Gaussian measure does not live on $H$ — it spills out onto a larger space.** White noise is precisely the case $Q=I$ (the identity), whose trace $\sum_k 1=\infty$ is infinite. This is the rigorous statement that *white noise is too rough to be a genuine $H$-valued random element*; it lives only in a bigger space of distributions.

#### White noise — definition

> **Definition — white noise.**
> Let $H$ be a separable Hilbert space (for concreteness $H=L^2(D)$, the square-integrable functions on a domain $D$, with inner product $\langle f,g\rangle=\int_D f(x)g(x)\,dx$). **White noise** on $H$ is the Gaussian object $\xi$ whose covariance operator is the identity $I$: for every pair $f,g\in H$ the pairings $\langle\xi,f\rangle$ and $\langle\xi,g\rangle$ are jointly centered normal with
> $$
> \mathbb{E}\big[\langle\xi,f\rangle\,\langle\xi,g\rangle\big]=\langle f,g\rangle=\int_D f(x)g(x)\,dx.
> $$

The intuition packed into this formula: white noise is "as random as possible, with no correlation between distinct points." Test it against two functions and the answer is just their overlap; in particular $\mathbb{E}\langle\xi,f\rangle^2=\|f\|^2$, so the noise has unit strength in every direction.

#### The "delta-correlated" heuristic, made precise

Physicists write white noise as a function $\xi(x)$ with $\mathbb{E}[\xi(x)\xi(y)]=\delta(x-y)$, where $\delta$ is the Dirac delta (the "function" that is zero except at the origin and integrates to $1$). This is only a heuristic, but we can show it is *consistent* with the rigorous definition.

1. Pretend $\xi(x)$ has pointwise values and $\mathbb{E}[\xi(x)\xi(y)]=\delta(x-y)$.
2. Then $\mathbb{E}\big[\langle\xi,f\rangle\langle\xi,g\rangle\big]=\mathbb{E}\big[\int f(x)\xi(x)\,dx\int g(y)\xi(y)\,dy\big]=\int\int f(x)g(y)\,\mathbb{E}[\xi(x)\xi(y)]\,dx\,dy$, exchanging integral and expectation by linearity.
3. Substitute the delta correlation: $=\int\int f(x)g(y)\,\delta(x-y)\,dx\,dy=\int f(x)g(x)\,dx=\langle f,g\rangle$, using the sifting property $\int g(y)\delta(x-y)\,dy=g(x)$ of the Dirac delta.
4. This reproduces the rigorous covariance exactly. So the delta-correlation heuristic and the trace-$I$ definition agree *when paired against test functions* — but only the paired version is mathematically legitimate, because step 1 (pointwise values) is false.

#### Worked example — white noise on a finite interval and its Fourier coefficients

Take $D=[0,2\pi]$ and the orthonormal basis $e_k(x)=\tfrac{1}{\sqrt{2\pi}}e^{ikx}$, $k\in\mathbb{Z}$. The **Fourier coefficients** of white noise are $\xi_k:=\langle\xi,e_k\rangle$.

1. Each $\xi_k$ is centered normal; by the covariance formula $\mathbb{E}[\xi_k\overline{\xi_j}]=\langle e_k,e_j\rangle=\delta_{kj}$ (Kronecker delta: $1$ if $k=j$, else $0$). So the coefficients are **independent standard normals**, one per frequency.
2. The formal series $\xi=\sum_k\xi_k e_k$ has expected squared norm $\mathbb{E}\sum_k|\xi_k|^2=\sum_k 1=\infty$, confirming numerically that white noise is *not* in $L^2$.
3. But pair against a smooth $f=\sum_k\hat f_k e_k$ with rapidly decaying coefficients: $\langle\xi,f\rangle=\sum_k\xi_k\overline{\hat f_k}$ has finite variance $\sum_k|\hat f_k|^2=\|f\|^2<\infty$. The pairing tames the divergence — exactly the role test functions play.

#### The Cameron–Martin space — which directions the measure "feels"

A Gaussian measure with covariance $Q$ has a distinguished dense subspace, the **Cameron–Martin space** $H_Q:=Q^{1/2}(H)$, with inner product $\langle h,k\rangle_{H_Q}=\langle Q^{-1/2}h,Q^{-1/2}k\rangle$. Its meaning: shifting the measure by a vector $h$ produces an *equivalent* measure (same null sets) precisely when $h\in H_Q$; shift by any other direction and the shifted measure becomes mutually singular (lives on a disjoint set). We record why this matters here.

1. For white noise $Q=I$, naively $H_Q=H$ — but white noise does not live on $H$ (§s1), so the honest statement uses the ambient distribution space: the Cameron–Martin space is $H=L^2$ sitting densely inside the larger support space.
2. The practical upshot, used in §s10: the $\Phi^4$ measure is built by *tilting* (reweighting) a Gaussian measure, and the tilt $e^{-\frac14\int\phi^4}$ is a legitimate change of measure only because it respects this structure. Shifts and tilts that leave the measure equivalent are the only ones we may perform freely.

#### Common pitfalls

- White noise is *not* "a Gaussian function." It is a Gaussian *measure on a space of distributions*; its samples have no pointwise values.
- The identity covariance $Q=I$ looks innocent but is the source of every regularity headache in this guide: it has infinite trace, so the noise must be smoothed (by a semigroup, §s3) before it lands back in a function space.
- The Cameron–Martin space is *strictly smaller* than the support: the measure assigns probability one to configurations *outside* its own Cameron–Martin space. This counterintuitive fact (the "shifts you can make" are negligible among "the configurations you see") is special to infinite dimensions.

<a id="s2"></a>
### Space–time white noise and cylindrical Wiener processes in a Hilbert space

#### What & why

For an *evolution* equation we need noise that is random in space **and** in time. The clean way to package "white in time, white in space" is the **cylindrical Wiener process** — an infinite-dimensional Brownian motion, one independent Brownian motion per spatial mode. This object is the driver of every SPDE in the guide.

#### Space–time white noise — definition

> **Definition — space–time white noise.**
> Space–time white noise $\xi$ on $[0,\infty)\times D$ is the centered Gaussian field characterized by
> $$
> \mathbb{E}\big[\langle\xi,\varphi\rangle\,\langle\xi,\psi\rangle\big]=\int_0^\infty\!\!\int_D \varphi(t,x)\,\psi(t,x)\,dx\,dt
> $$
> for space–time test functions $\varphi,\psi$. Heuristically $\mathbb{E}[\xi(t,x)\xi(s,y)]=\delta(t-s)\,\delta(x-y)$: uncorrelated across distinct times and distinct points.

#### The cylindrical Wiener process — construction

Fix a separable Hilbert space $H$ with orthonormal basis $\{e_k\}_{k\ge1}$ (think $H=L^2(D)$, the spatial directions).

> **Definition — cylindrical Wiener process.**
> Let $\{\beta_k(t)\}_{k\ge1}$ be a sequence of *independent* standard real Brownian motions. The **cylindrical Wiener process** on $H$ is the formal series
> $$
> W(t)=\sum_{k=1}^\infty \beta_k(t)\,e_k.
> $$

The name "cylindrical" is a warning: this series does *not* converge in $H$. We make that precise and then fix it.

> **Proposition.** The series $W(t)=\sum_k\beta_k(t)e_k$ diverges in $H$ for every $t>0$: $\mathbb{E}\|W(t)\|^2=\infty$.

**Derivation.**
1. By orthonormality of $\{e_k\}$, $\|W(t)\|^2=\sum_k\beta_k(t)^2$ (Parseval).
2. Take expectations and exchange with the sum (monotone convergence, nonnegative terms): $\mathbb{E}\|W(t)\|^2=\sum_k\mathbb{E}[\beta_k(t)^2]$.
3. Each $\beta_k(t)\sim\mathcal{N}(0,t)$, so $\mathbb{E}[\beta_k(t)^2]=t$ (variance of Brownian motion at time $t$).
4. Hence $\mathbb{E}\|W(t)\|^2=\sum_k t=\infty$ for $t>0$. $\blacksquare$

So just like white noise (§s1), the cylindrical Wiener process is too big for $H$. The standard cure is a covariance: replace $I$ by a trace-class $Q$.

> **Definition — $Q$-Wiener process.**
> Let $Q:H\to H$ be symmetric, positive, trace class, with eigenpairs $Qe_k=\lambda_k e_k$, $\lambda_k\ge0$, $\sum_k\lambda_k<\infty$. The **$Q$-Wiener process** is
> $$
> W^Q(t)=\sum_{k=1}^\infty \sqrt{\lambda_k}\,\beta_k(t)\,e_k.
> $$

> **Proposition.** $W^Q(t)$ converges in mean square in $H$, with $\mathbb{E}\|W^Q(t)\|^2=t\mathrm{Tr}Q<\infty$.

**Derivation.**
1. As above, $\mathbb{E}\|W^Q(t)\|^2=\sum_k\lambda_k\,\mathbb{E}[\beta_k(t)^2]$ by orthonormality and independence.
2. $=\sum_k\lambda_k\,t=t\sum_k\lambda_k=t\mathrm{Tr}Q$, using $\mathbb{E}[\beta_k(t)^2]=t$ and the definition of trace.
3. By hypothesis $\mathrm{Tr}Q<\infty$, so the partial sums form a Cauchy sequence in $L^2(\Omega;H)$ and converge. $\blacksquare$

#### How white noise and the cylindrical process are two views of one object

The time-derivative of the cylindrical Wiener process *is* space–time white noise. Formally $\dot W(t)=\sum_k\dot\beta_k(t)e_k$, and since each $\dot\beta_k$ is one-dimensional white noise in time with $\mathbb{E}[\dot\beta_k(t)\dot\beta_j(s)]=\delta_{kj}\delta(t-s)$, the field $\dot W$ has covariance $\sum_k e_k(x)e_k(y)\,\delta(t-s)=\delta(x-y)\delta(t-s)$ by the completeness relation $\sum_k e_k(x)e_k(y)=\delta(x-y)$ for an orthonormal basis. This is precisely space–time white noise from the definition above. The two objects are the same noise written in two notations: $W$ is its time-integral, $\dot W$ its raw form.

#### Worked example — counting modes that converge

Let $H=L^2([0,2\pi])$ with the basis from §s1. Choose $Q$ diagonal with $\lambda_k=1/k^2$. Then $\mathrm{Tr}Q=\sum_{k\ge1}k^{-2}=\pi^2/6<\infty$ (the Basel sum), so $W^Q$ lives in $H$. If instead $\lambda_k=1/k$ then $\sum 1/k=\infty$ diverges (harmonic series) and the process again escapes $H$. The borderline is sharp: trace-class is exactly the dividing line between "$H$-valued" and "merely cylindrical."

#### Where the cylindrical process *does* converge

If the cylindrical $W(t)=\sum_k\beta_k(t)e_k$ diverges in $H$, in what space does it live? The answer is any larger Hilbert space $U\supset H$ into which the embedding $J:H\hookrightarrow U$ is **Hilbert–Schmidt** (so $\sum_k\|Je_k\|_U^2<\infty$). Then $\mathbb{E}\|W(t)\|_U^2=t\sum_k\|Je_k\|_U^2<\infty$ by the same computation as the $Q$-Wiener proposition, and $W(t)$ is a genuine $U$-valued process. Concretely one takes $U$ to be a **negative Sobolev space** $H^{-s}$ (functions allowed to be distributions of negative smoothness $s$) with $s$ large enough that the embedding $L^2\hookrightarrow H^{-s}$ is Hilbert–Schmidt — in $d=1$ any $s>\tfrac12$ works, since the embedding's squared Hilbert–Schmidt norm is $\sum_k(1+k^2)^{-s}$, finite for $s>\tfrac12$. This is the rigorous home of "white noise as a process": not in $L^2$, but in a space of distributions chosen exactly large enough to absorb the infinite trace.

#### Common pitfalls

- "Cylindrical" does not mean a different kind of noise; it means the *same* white noise viewed as failing to converge in $H$ but converging in a larger space.
- The eigenvalues $\lambda_k$ are not free physics — for genuine space–time white noise they are all $1$ (i.e. $Q=I$), and the convergence must be recovered another way (by the smoothing of the equation, §s3), not by tampering with the noise.

## Part B · Solving the linear equation

<a id="s3"></a>
### The stochastic heat equation and the mild (semigroup) solution

#### What & why

The simplest non-trivial SPDE is the **stochastic heat equation (SHE)**: the heat equation forced by space–time white noise. It is the harmonic oscillator of the subject — explicitly solvable, and the template for everything nonlinear. Our goal is to *derive* its solution and show in what sense it exists.

> **The stochastic heat equation.**
> $$
> \partial_t u(t,x)=\Delta u(t,x)+\xi(t,x),\qquad u(0,\cdot)=u_0,
> $$
> with $\xi$ space–time white noise, $\Delta$ the Laplacian, on a domain $D$ with (say) periodic boundary conditions.

#### The obstacle and the idea

We cannot differentiate $\xi$, so the equation has no classical meaning. The way out, borrowed from the deterministic theory, is the **variation-of-constants / Duhamel formula**: rewrite a forced linear equation using the semigroup of the unforced one, moving all derivatives onto the *known* smooth semigroup and away from the rough noise.

#### Restating the deterministic ingredient

From the PDE guide: the heat equation $\partial_t v=\Delta v$, $v(0)=v_0$, is solved by $v(t)=S(t)v_0:=e^{t\Delta}v_0$, where the family $\{S(t)\}_{t\ge0}$ is the **heat semigroup**: $S(0)=I$, $S(t)S(s)=S(t+s)$ (the **semigroup property**), and $\tfrac{d}{dt}S(t)v_0=\Delta S(t)v_0$. Concretely, in the Fourier basis $e_k$ with $\Delta e_k=-\gamma_k e_k$ (so $\gamma_k\ge0$ are the eigenvalues of $-\Delta$), the semigroup acts by $S(t)e_k=e^{-\gamma_k t}e_k$ — it damps high frequencies exponentially. *This damping is the entire reason the SHE has a solution.*

#### Deriving the mild solution

> **Derivation of the mild formula.**
> 1. For the deterministic forced equation $\partial_t u=\Delta u+f(t)$, $u(0)=u_0$, define $w(s):=S(t-s)u(s)$ for $0\le s\le t$. Differentiate in $s$ by the product rule: $w'(s)=-\Delta S(t-s)u(s)+S(t-s)u'(s)$, since $\tfrac{d}{ds}S(t-s)=-\Delta S(t-s)$.
> 2. Substitute $u'(s)=\Delta u(s)+f(s)$: $w'(s)=-\Delta S(t-s)u(s)+S(t-s)\Delta u(s)+S(t-s)f(s)$. The operators $\Delta$ and $S(t-s)$ commute (both are diagonal in the same eigenbasis), so the first two terms cancel: $w'(s)=S(t-s)f(s)$.
> 3. Integrate from $0$ to $t$: $w(t)-w(0)=\int_0^t S(t-s)f(s)\,ds$. Now $w(t)=S(0)u(t)=u(t)$ and $w(0)=S(t)u_0$, giving the **Duhamel/variation-of-constants formula**
> $$
> u(t)=S(t)u_0+\int_0^t S(t-s)f(s)\,ds.
> $$
> 4. Replace the deterministic forcing $f(s)\,ds$ by the noise increment $dW(s)$ (the cylindrical Wiener process whose time-derivative is white noise, §s2). This yields the **mild solution** of the SHE:
> $$
> u(t)=S(t)u_0+\int_0^t S(t-s)\,dW(s).
> $$

The crucial move is that *no derivative of the noise appears.* The noise is integrated against the smooth, exponentially damping operator $S(t-s)$. We now prove this integral is a genuine $H$-valued random variable even though the noise itself is not.

#### The stochastic convolution is well-defined

> **Theorem (existence of the mild solution).** With periodic boundary conditions in spatial dimension $d=1$, the **stochastic convolution** $Z(t):=\int_0^t S(t-s)\,dW(s)$ is a well-defined element of $H=L^2(D)$ with finite second moment.

**Derivation (mode by mode).**
1. Expand in the eigenbasis: $Z(t)=\sum_k Z_k(t)e_k$ with $Z_k(t)=\int_0^t e^{-\gamma_k(t-s)}\,d\beta_k(s)$, since $S(t-s)e_k=e^{-\gamma_k(t-s)}e_k$ and $dW=\sum_k d\beta_k\,e_k$.
2. Each $Z_k$ is an Itô integral of a deterministic integrand, hence centered Gaussian. By the **Itô isometry** (restated prerequisite), $\mathbb{E}[Z_k(t)^2]=\int_0^t e^{-2\gamma_k(t-s)}\,ds=\dfrac{1-e^{-2\gamma_k t}}{2\gamma_k}$ for $\gamma_k>0$.
3. Sum over modes: $\mathbb{E}\|Z(t)\|^2=\sum_k\dfrac{1-e^{-2\gamma_k t}}{2\gamma_k}\le\sum_k\dfrac{1}{2\gamma_k}$, bounding the numerator by $1$.
4. In dimension $d=1$ on $[0,2\pi]$ the eigenvalues are $\gamma_k\sim k^2$, so $\sum_k\frac{1}{2\gamma_k}\sim\sum_k\frac{1}{2k^2}<\infty$ (Basel-type sum). Therefore $\mathbb{E}\|Z(t)\|^2<\infty$ and $Z(t)\in H$. $\blacksquare$

This is the punchline of the linear theory: **the heat semigroup's damping $e^{-2\gamma_k t}$, summed against $\gamma_k\sim k^2$, converts the divergent white noise into a convergent, genuinely function-valued field — in one space dimension.** Note where dimension enters: in $d$ dimensions $\gamma_k\sim|k|^2$ but the number of modes with $\gamma_k\le R$ grows like $R^{d/2}$, so $\sum_k\gamma_k^{-1}$ converges precisely when $d<2$; among integer dimensions this means $d=1$ alone, with $d=2$ already diverging (logarithmically) and higher $d$ diverging faster. This single estimate foreshadows §s7: SPDEs with white noise are function-valued only in low dimension.

#### Numerical check of the convergence boundary

Let us put numbers on step 4 versus the failure in $d=2$. On $[0,2\pi]$ the one-dimensional bound is $\sum_{k\ge1}\frac{1}{2k^2}=\frac{1}{2}\cdot\frac{\pi^2}{6}\approx0.822$ — a finite, modest number, so $Z(t)$ is comfortably in $L^2$. On the two-dimensional torus the eigenvalues are $\gamma_{(j,k)}=j^2+k^2$ and the sum becomes $\sum_{(j,k)\ne(0,0)}\frac{1}{2(j^2+k^2)}$; approximating by the integral $\int_1^R\frac{2\pi r\,dr}{2r^2}=\pi\log R\to\infty$, the sum diverges logarithmically. The transition from $0.822$ (convergent, $d=1$) to $\log R\to\infty$ (divergent, $d=2$) is the entire reason the SHE is function-valued in one dimension and only distribution-valued in two.

#### Worked example — the equilibrium variance of one Fourier mode

Take mode $k$ with $\gamma_k=k^2$. As $t\to\infty$, $\mathbb{E}[Z_k(t)^2]\to\frac{1}{2\gamma_k}=\frac{1}{2k^2}$. So in equilibrium the $k$-th mode of the SHE is a centered normal of variance $1/(2k^2)$: high frequencies are strongly suppressed, low frequencies dominate. The equilibrium field $\sum_k\mathcal{N}(0,\tfrac{1}{2k^2})\,e_k$ is in fact (a version of) **Brownian motion in the space variable** — the SHE relaxes to a spatially Brownian random field.

#### Common pitfalls

- The mild solution is a *definition by formula*, not a function satisfying the PDE pointwise; it solves the equation in an integrated sense only.
- The finiteness in step 4 is dimension-dependent. In $d\ge2$ the same computation diverges and $Z(t)\notin L^2$; the SHE solution becomes a distribution, not a function.

<a id="s4"></a>
### Itô calculus in infinite dimensions and the stochastic convolution

#### What & why

To handle nonlinear and more general SPDEs we need to integrate operator-valued processes against the cylindrical Wiener process and to differentiate functionals of the solution. This section lifts the finite-dimensional Itô calculus from the Stochastic Processes guide to a Hilbert space.

#### The infinite-dimensional Itô integral

Let $\Phi(s)$ be a process taking values in operators from $H$ to another Hilbert space $K$ (predictable, i.e. not anticipating the future). The **stochastic integral** $\int_0^t\Phi(s)\,dW(s)$ against a $Q$-Wiener process is defined, exactly as in finite dimensions, first for simple (piecewise-constant) integrands and then extended by an isometry.

> **Itô isometry (Hilbert-space form).**
> $$
> \mathbb{E}\Big\|\int_0^t\Phi(s)\,dW(s)\Big\|_K^2=\mathbb{E}\int_0^t\big\|\Phi(s)\,Q^{1/2}\big\|_{\mathrm{HS}}^2\,ds,
> $$
> where $\|A\|_{\mathrm{HS}}^2=\sum_k\|Ae_k\|^2$ is the squared **Hilbert–Schmidt norm**.

**Derivation for a simple integrand.**
1. Let $\Phi$ be constant on a single interval $[a,b]$, equal to a (deterministic, for clarity) operator $\Phi_0$. Then $\int\Phi\,dW=\Phi_0(W(b)-W(a))=\Phi_0\sum_k\sqrt{\lambda_k}(\beta_k(b)-\beta_k(a))e_k$.
2. Compute the squared norm's expectation. Cross terms vanish because distinct $\beta_k$ are independent and centered, so $\mathbb{E}[(\beta_k(b)-\beta_k(a))(\beta_j(b)-\beta_j(a))]=\delta_{kj}(b-a)$.
3. Thus $\mathbb{E}\|\Phi_0(W(b)-W(a))\|^2=(b-a)\sum_k\lambda_k\|\Phi_0 e_k\|^2=(b-a)\sum_k\|\Phi_0 Q^{1/2}e_k\|^2=(b-a)\|\Phi_0 Q^{1/2}\|_{\mathrm{HS}}^2$, using $Q^{1/2}e_k=\sqrt{\lambda_k}e_k$.
4. Summing over consecutive intervals gives the stated formula for simple integrands; the general case follows by density (approximate $\Phi$ in the Hilbert–Schmidt norm and pass to the limit, the isometry guaranteeing the limit exists). $\blacksquare$

The appearance of the **Hilbert–Schmidt norm** is the deep structural fact: an integrand must be Hilbert–Schmidt (after composing with $Q^{1/2}$) for its integral to be square-integrable. For the SHE the integrand is the semigroup $S(t-s)$, and the content of §s3 was exactly that $S(t-s)$ *is* Hilbert–Schmidt in $d=1$.

#### The stochastic convolution, revisited as the key tool

> **Definition — stochastic convolution.** For a semigroup $S(\cdot)$ and cylindrical noise $W$,
> $$
> W_A(t):=\int_0^t S(t-s)\,dW(s).
> $$

Unlike an ordinary Itô integral, the integrand $S(t-s)$ depends on the *upper limit* $t$, so $W_A$ is **not** a martingale and its increments are correlated. This is a genuine new feature of SPDEs. Two facts we use repeatedly:

> **Factorization / regularity.** $W_A$ has the same time-regularity as the deterministic convolution of the noise with the heat kernel — Hölder continuous of order just under $\tfrac14$ in time and $\tfrac12$ in space in $d=1$ (proved in §s7).

> **Markov property of the solution.** Even though $W_A$ is not a martingale, the SHE solution $u(t)=S(t)u_0+W_A(t)$ is a Markov process in $H$: its future depends on the past only through the present, because the noise increments after time $t$ are independent of everything up to $t$.

#### Itô's formula in a Hilbert space

For a twice-Fréchet-differentiable functional $F:H\to\mathbb{R}$ and a process $X(t)=X(0)+\int_0^t b(s)\,ds+\int_0^t\Phi(s)\,dW(s)$,

$$
F(X(t))=F(X(0))+\int_0^t\langle F'(X(s)),dX(s)\rangle+\tfrac12\int_0^t\mathrm{Tr}\big[F''(X(s))\,\Phi(s)Q\Phi(s)^*\big]\,ds.
$$

The new feature versus calculus is the second-order **trace term**, the exact analogue of the $\tfrac12 F''\,(dW)^2=\tfrac12 F''\,dt$ correction in one dimension, now summed over all noise directions via the trace. This is the engine for computing invariant measures in §s10.

#### Worked example — the expected energy of the SHE

Let $F(u)=\tfrac12\|u\|^2$, so $F'(u)=u$ and $F''(u)=I$. Apply Itô's formula to $u(t)$ solving the SHE ($b=\Delta u$, $\Phi=I$, $Q=I$ formally, but regularize):
1. The drift term gives $\int_0^t\langle u,\Delta u\rangle\,ds=-\int_0^t\|\nabla u\|^2\,ds\le0$ (integration by parts; energy is dissipated by diffusion).
2. The trace term gives $\tfrac12\int_0^t\mathrm{Tr}(I\cdot Q)\,ds=\tfrac12 t\mathrm{Tr}Q$ (energy is injected by noise at constant rate $\tfrac12\mathrm{Tr}Q$ per unit time).
3. Balancing injection against dissipation gives the stationary energy. With $Q=I$ truncated to $N$ modes, injection is $\tfrac12 N$ and the equilibrium energy is finite mode-by-mode but diverges as $N\to\infty$ — the same $d$-dependent divergence as before.

#### Common pitfalls

- The integrand condition is Hilbert–Schmidt, *not* merely bounded. A bounded operator can fail to be Hilbert–Schmidt (e.g. the identity on infinite-dimensional $H$), and then its stochastic integral diverges.
- $W_A$ is not a martingale; do not apply martingale inequalities to it directly. Use the factorization method instead.

## Part C · Nonlinear equations and their pathologies

<a id="s5"></a>
### Existence and uniqueness for semilinear SPDEs via a fixed-point argument

#### What & why

Real models have nonlinearities. The cleanest tractable class is **semilinear** SPDEs — linear leading operator plus a nonlinear lower-order term — and the standard existence proof is a **Banach fixed-point (contraction mapping) argument**, the same technique that proves existence for ordinary differential equations, lifted to the mild formulation.

> **The semilinear SPDE.**
> $$
> \partial_t u=\Delta u+F(u)+\sigma(u)\,\xi,\qquad u(0)=u_0,
> $$
> with mild form
> $$
> u(t)=S(t)u_0+\int_0^t S(t-s)F(u(s))\,ds+\int_0^t S(t-s)\sigma(u(s))\,dW(s).
> $$

We assume $F$ and $\sigma$ are **Lipschitz**: there is a constant $L$ with $\|F(a)-F(b)\|\le L\|a-b\|$ and likewise for $\sigma$ (in Hilbert–Schmidt norm after composing with $Q^{1/2}$). "Lipschitz" means the map cannot stretch distances by more than a fixed factor.

#### The Banach fixed-point theorem, restated

From Functional Analysis: if $(\mathcal{X},d)$ is a complete metric space and $\mathcal{T}:\mathcal{X}\to\mathcal{X}$ is a **contraction** — $d(\mathcal{T}x,\mathcal{T}y)\le\theta\,d(x,y)$ for some $\theta<1$ — then $\mathcal{T}$ has a unique fixed point $x^*=\mathcal{T}x^*$, found as the limit of iterates $x_{n+1}=\mathcal{T}x_n$.

#### The existence theorem and its proof

> **Theorem.** If $F,\sigma$ are Lipschitz and $u_0\in L^2(\Omega;H)$, the semilinear SPDE has a unique mild solution on $[0,T]$ in the space $\mathcal{X}$ of predictable $H$-valued processes with $\|u\|_{\mathcal{X}}^2:=\sup_{t\le T}\mathbb{E}\|u(t)\|^2<\infty$.

**Derivation.**
1. Define the map $\mathcal{T}$ by the right-hand side of the mild form: $(\mathcal{T}u)(t)=S(t)u_0+\int_0^t S(t-s)F(u(s))\,ds+\int_0^t S(t-s)\sigma(u(s))\,dW(s)$. A fixed point of $\mathcal{T}$ is exactly a mild solution. $\mathcal{X}$ with the norm above is complete (a fact from functional analysis), so Banach's theorem applies once we show $\mathcal{T}$ is a contraction for small $T$.
2. Take two inputs $u,v$. By linearity, $(\mathcal{T}u-\mathcal{T}v)(t)=\int_0^t S(t-s)[F(u)-F(v)]\,ds+\int_0^t S(t-s)[\sigma(u)-\sigma(v)]\,dW(s)$. The initial-data term cancels.
3. **Drift estimate.** Using $\|S(t-s)\|\le1$ (the heat semigroup is a contraction), the Cauchy–Schwarz inequality on $[0,t]$, and the Lipschitz bound on $F$:
$$
\mathbb{E}\Big\|\int_0^t S(t-s)[F(u)-F(v)]\,ds\Big\|^2\le t\int_0^t\mathbb{E}\|F(u(s))-F(v(s))\|^2\,ds\le tL^2\int_0^t\mathbb{E}\|u(s)-v(s)\|^2\,ds.
$$
4. **Noise estimate.** By the Itô isometry (§s4), $\|S(t-s)\|\le1$, and the Lipschitz bound on $\sigma$:
$$
\mathbb{E}\Big\|\int_0^t S(t-s)[\sigma(u)-\sigma(v)]\,dW\Big\|^2\le\int_0^t\mathbb{E}\|\sigma(u(s))-\sigma(v(s))\|_{\mathrm{HS}}^2\,ds\le L^2\int_0^t\mathbb{E}\|u(s)-v(s)\|^2\,ds.
$$
(For genuine white noise one needs $S(t-s)$ Hilbert–Schmidt, as in §s3, supplying an extra singular but still integrable factor $(t-s)^{-1/2}$ in $d=1$; this turns the plain time integral $\int_0^t(\cdots)\,ds$ into the weighted one $\int_0^t(t-s)^{-1/2}(\cdots)\,ds$, so the contraction *constant* changes — the resulting bound is $L^2(T^2+2\sqrt{T})$ rather than $L^2(T^2+T)$ — though it still vanishes as $T\to0$, so existence and uniqueness are unaffected.)
5. Add steps 3 and 4 and take the supremum over $t\le T$: $\|\mathcal{T}u-\mathcal{T}v\|_{\mathcal{X}}^2\le L^2(T^2+T)\,\|u-v\|_{\mathcal{X}}^2$.
6. Choose $T$ small enough that $\theta^2:=L^2(T^2+T)<1$. Then $\mathcal{T}$ is a contraction, so by Banach's theorem it has a unique fixed point on $[0,T]$: a unique mild solution.
7. **Globalization.** Restart the argument from $u(T)$ on $[T,2T]$ and concatenate. Since the small step size $T$ depends only on $L$ (not on the data), iterating covers any finite interval, giving a unique global solution. $\blacksquare$

#### Worked example — a Lipschitz reaction term

Take $F(u)=\sin u$ (acting pointwise). Then $|F(a)-F(b)|=|\sin a-\sin b|\le|a-b|$ by the mean value theorem (since $|\cos|\le1$), so $F$ is Lipschitz with $L=1$. The theorem applies and the stochastic reaction–diffusion equation $\partial_t u=\Delta u+\sin u+\xi$ has a unique mild solution. Contrast with $F(u)=u^2$ (the KPZ-type nonlinearity), which is *not* globally Lipschitz — and indeed needs the entire machinery of Part D.

#### Worked example — the contraction constant with explicit numbers

Take $L=1$ (the $\sin$ example) and additive noise $\sigma\equiv1$. From step 5, $\theta^2=L^2(T^2+T)=T^2+T$. To guarantee contraction we need $\theta<1$, i.e. $T^2+T<1$. Solving the quadratic $T^2+T-1=0$ gives the positive root $T_*=\frac{-1+\sqrt5}{2}\approx0.618$. So on any interval of length below $\approx0.618$ the map is a contraction and the Picard iterates $u_{n+1}=\mathcal{T}u_n$ converge geometrically: $\|u_n-u^*\|_{\mathcal X}\le\theta^n\|u_0-u^*\|_{\mathcal X}$. Concretely with $T=0.5$, $\theta=\sqrt{0.75}\approx0.866$, so the error shrinks by about $13\%$ per iteration. The restart trick (step 7) then tiles $[0,\infty)$ by intervals of length $0.5$, so the unique solution extends to all time.

#### Common pitfalls

- The argument needs *global* Lipschitz bounds. Polynomial nonlinearities like $u^2$ or $u^3$ are only locally Lipschitz; one must either truncate, use energy estimates, or move to renormalization (§s8).
- Smallness of $T$ is essential for the contraction; existence on all of $[0,\infty)$ comes from the restart trick, which works only because the step size does not shrink.

<a id="s6"></a>
### The Kardar–Parisi–Zhang (KPZ) equation and why it is analytically ill-posed

#### What & why

The KPZ equation models a randomly growing one-dimensional interface and is the canonical example of an SPDE that is *not* covered by the Lipschitz theory — in fact the naive equation has no classical solution at all. Understanding *why* it fails is the motivation for everything in Part D.

> **The KPZ equation.** For interface height $h(t,x)$, $x\in\mathbb{R}$ (or a circle),
> $$
> \partial_t h=\nu\,\partial_x^2 h+\tfrac{\lambda}{2}(\partial_x h)^2+\xi,
> $$
> with $\nu>0$ the surface tension, $\lambda$ the growth coupling, and $\xi$ space–time white noise. The three terms are: smoothing ($\partial_x^2 h$), slope-dependent growth ($(\partial_x h)^2$, the **KPZ nonlinearity**), and random deposition ($\xi$).

#### Why the equation is ill-posed — the precise obstruction

**Derivation of the obstruction.**
1. Drop the nonlinearity: the linear part $\partial_t h=\nu\partial_x^2 h+\xi$ is the SHE of §s3. Its solution is, at fixed time, a spatial process of the regularity of Brownian motion: $h$ is Hölder continuous of order $\tfrac12-\varepsilon$ in $x$ but **not** differentiable (§s7 quantifies this).
2. The nonlinear term needs $\partial_x h$, the spatial derivative. But $h$ is only Brownian-rough, so $\partial_x h$ exists only as a distribution (a generalized function), of negative regularity $-\tfrac12-\varepsilon$.
3. The term then demands the **square** $(\partial_x h)^2$ of a distribution. Squaring is multiplication, and multiplication of two distributions of negative regularity is **not defined** — the standard rule (from the theory of distributions) is that a product $f\cdot g$ makes sense only if the sum of their regularities (Hölder exponents) is positive. Here $(-\tfrac12)+(-\tfrac12)=-1<0$. The product is genuinely undefined.
4. Therefore the right-hand side of KPZ contains an undefined object, and the equation has no classical solution. $\blacksquare$

This is not a failure of cleverness but a real divergence: any regularization (smoothing the noise at scale $\epsilon$) produces a $(\partial_x h_\epsilon)^2$ whose average blows up like $1/\epsilon$ as $\epsilon\to0$. The infinity must be *subtracted* (renormalized), which is the subject of §s8–s9.

#### The Cole–Hopf rescue (for KPZ specifically)

There is a famous trick special to KPZ. Set $Z=e^{(\lambda/2\nu)h}$.

**Derivation.**
1. Differentiate: $\partial_t Z=\tfrac{\lambda}{2\nu}Z\,\partial_t h$ and $\partial_x^2 Z=\tfrac{\lambda}{2\nu}Z\big(\partial_x^2 h+\tfrac{\lambda}{2\nu}(\partial_x h)^2\big)$ by the chain and product rules.
2. Substitute the KPZ equation for $\partial_t h$: $\partial_t Z=\tfrac{\lambda}{2\nu}Z\big(\nu\partial_x^2 h+\tfrac{\lambda}{2}(\partial_x h)^2+\xi\big)$.
3. Compare with step 1's expression for $\nu\partial_x^2 Z=\tfrac{\lambda}{2}Z\partial_x^2 h+\tfrac{\lambda^2}{4\nu}Z(\partial_x h)^2$. The $(\partial_x h)^2$ terms match, so they cancel when we subtract, leaving $\partial_t Z=\nu\partial_x^2 Z+\tfrac{\lambda}{2\nu}Z\,\xi$ — the **multiplicative stochastic heat equation**, which is *linear* in $Z$ and has the Lipschitz-type theory of §s5 (with multiplicative noise).
4. So $h=\tfrac{2\nu}{\lambda}\log Z$ defines the **Cole–Hopf solution** of KPZ. (A subtlety: even this transformation hides an infinite constant, the **Itô correction** to the chain rule, which is exactly the renormalization in disguise.)

The Cole–Hopf trick works only for KPZ's special structure. For generic singular SPDEs no such trick exists, motivating the general theories of §s9.

#### Worked example — the divergence of the regularized nonlinearity

Smooth the noise to $\xi_\epsilon$ (correlation length $\epsilon$). The linear solution $h_\epsilon$ then has $\mathbb{E}[(\partial_x h_\epsilon)^2]\sim c/\epsilon$ for a constant $c>0$: as the smoothing is removed ($\epsilon\to0$) the expected squared slope diverges linearly. The renormalized KPZ equation replaces $(\partial_x h)^2$ by $(\partial_x h_\epsilon)^2-c/\epsilon$, subtracting the divergence by hand; the limit then exists. This concrete infinity is what §s8 makes systematic.

#### Common pitfalls

- KPZ being ill-posed does *not* mean it has no solution physically; it means the *equation as written* is meaningless and must be reinterpreted (Cole–Hopf, or renormalization).
- The Cole–Hopf solution and the renormalized solution agree, but proving this required deep work; the equivalence is a theorem, not a definition.

<a id="s7"></a>
### Regularity of solutions — Hölder continuity and the crucial role of spatial dimension

#### What & why

How rough is the solution of an SPDE? The answer controls everything: whether nonlinearities make sense (§s6), whether the solution is a function or a distribution, and which renormalizations are needed. The measuring stick is **Hölder continuity**, and the verdict depends decisively on the spatial dimension $d$.

> **Definition — Hölder continuity.** A function $f$ is **$\alpha$-Hölder** ($0<\alpha\le1$) if there is $C$ with $|f(x)-f(y)|\le C|x-y|^\alpha$ for all $x,y$. Larger $\alpha$ means smoother; $\alpha=1$ is Lipschitz, and "negative regularity $-\alpha$" denotes a distribution that becomes $\alpha$-Hölder only after smoothing.

#### The regularity of the stochastic convolution — quantitative statement

> **Theorem (regularity of the SHE solution).** In spatial dimension $d=1$, the mild solution $u$ of the stochastic heat equation is, almost surely, Hölder continuous of order $\tfrac12-\varepsilon$ in space and $\tfrac14-\varepsilon$ in time, for every $\varepsilon>0$, and these exponents are sharp.

**Derivation of the spatial exponent.**
1. Work mode by mode: $u(t,x)=\sum_k Z_k(t)e_k(x)$ with $\mathbb{E}[Z_k(t)^2]\le\frac{1}{2\gamma_k}\sim\frac{1}{2k^2}$ (from §s3).
2. Compute the spatial increment's variance for fixed $t$, using independence of the modes:
$$
\mathbb{E}|u(t,x)-u(t,y)|^2=\sum_k\mathbb{E}[Z_k(t)^2]\,|e_k(x)-e_k(y)|^2\le C\sum_k\frac{1}{k^2}\,\min(1,k^2|x-y|^2),
$$
using $|e_k(x)-e_k(y)|=\frac{1}{\sqrt{2\pi}}|e^{ikx}-e^{iky}|\le\min(2/\sqrt{2\pi},\,k|x-y|/\sqrt{2\pi})$ (the curve $e^{ik\cdot}$ moves at speed $k$ but is bounded).
3. Split the sum at $k_0=1/|x-y|$. For $k\le k_0$ use the bound $k^2|x-y|^2$: $\sum_{k\le k_0}|x-y|^2=k_0|x-y|^2=|x-y|$. For $k>k_0$ use the bound $1$: $\sum_{k>k_0}k^{-2}\sim 1/k_0=|x-y|$. Both halves give $O(|x-y|)$.
4. Hence $\mathbb{E}|u(t,x)-u(t,y)|^2\le C|x-y|$, i.e. variance $\sim|x-y|^{2\cdot(1/2)}$. By the **Kolmogorov continuity theorem** (a Gaussian-process fact: variance $\sim|x-y|^{2\alpha}$ gives Hölder exponent up to $\alpha$), $u$ is $(\tfrac12-\varepsilon)$-Hölder in space. $\blacksquare$

The time exponent $\tfrac14$ comes from a parallel computation: parabolic scaling makes one unit of time worth two units of space ($t\sim x^2$), so the spatial exponent $\tfrac12$ becomes the temporal exponent $\tfrac14$.

#### The role of dimension — the regularity ladder

The same estimate in $d$ dimensions has eigenvalues $\gamma_k\sim|k|^2$ but a mode count growing like $|k|^{d-1}$ per shell, giving $\sum_k\gamma_k^{-1}\sim\int |k|^{-2}|k|^{d-1}d|k|$, which converges only for $d<2$. The consequences:

- $d=1$: solution is a genuine **function**, Hölder of order $\tfrac12-$. Products like $u^2$ make sense; the Lipschitz theory of §s5 applies to polynomial nonlinearities after local truncation.
- $d=2$: borderline. The solution is a **distribution** of regularity $0-$ (just below continuous); products are logarithmically divergent and need renormalization. This is the home of the **$\Phi^4_2$** model.
- $d=3$: solution has regularity $-\tfrac12-$; products are strongly divergent and require the full theory of §s9. This is **$\Phi^4_3$**, the hardest case solved.
- $d\ge4$: the equations are **supercritical** — no renormalization is known to work; the small-scale fluctuations overwhelm the nonlinearity. This matches the physics fact that $\Phi^4$ is a free (Gaussian) theory in dimension $\ge4$.

#### The notion of subcriticality (local subcriticality)

The dividing line is captured by counting how the nonlinearity scales versus the noise under the **parabolic rescaling** $x\to\delta x$, $t\to\delta^2 t$. If the nonlinear term becomes *negligible* at small scales (it scales away faster than the noise), the equation is **subcritical** and amenable to renormalization; if it dominates, it is supercritical and out of reach. KPZ in $d=1$, $\Phi^4$ in $d=2,3$ are subcritical; $\Phi^4$ in $d\ge4$ is not.

#### Worked example — checking the product condition

In $d=1$, $u$ has regularity $\tfrac12$. The product rule needs the exponents of the factors to sum positive. For $u^2$: $\tfrac12+\tfrac12=1>0$, fine — $u^2$ is defined. For the KPZ nonlinearity $(\partial_x u)^2$: $\partial_x u$ has regularity $\tfrac12-1=-\tfrac12$, and $-\tfrac12-\tfrac12=-1<0$, undefined — exactly the §s6 obstruction, now read off the regularity ladder.

#### Common pitfalls

- Hölder $\tfrac12-\varepsilon$ does **not** include $\varepsilon=0$: the solution is strictly less regular than Lipschitz and is nowhere differentiable, just like Brownian motion.
- The dimension thresholds ($d=1$ function, $d=2$ marginal, $d\ge4$ hopeless) are not conventions; they come from the convergence of explicit mode sums, as derived above.

## Part D · Renormalization and modern theory

<a id="s8"></a>
### The Da Prato–Debussche trick and a first look at renormalization

#### What & why

When the nonlinearity is *almost* manageable — the solution is only slightly too rough — there is an elegant elementary method, due to Da Prato and Debussche, that handles the singularity by **splitting off the worst part explicitly** and solving for a smoother remainder. It is the gateway drug to the full theories of §s9 and the place where **renormalization** first appears concretely.

> **Model equation — the dynamical $\Phi^4_2$ equation.**
> $$
> \partial_t u=\Delta u-u^3+\xi\qquad\text{on the 2-torus},
> $$
> space–time white noise $\xi$, spatial dimension $d=2$. As in §s7 the solution is a distribution, so $u^3$ is undefined and must be renormalized.

#### The trick — derivation

The idea: the linear part already captures all the roughness, so subtract it.

**Derivation.**
1. Let $X:=W_A$ be the **stochastic convolution** solving the *linear* equation $\partial_t X=\Delta X+\xi$, $X(0)=0$ (§s3). $X$ has exactly the regularity of the noise-driven heat equation — the roughest part.
2. Write $u=X+v$, splitting the solution into the explicit rough part $X$ plus an unknown remainder $v$. Substitute into the equation: $\partial_t(X+v)=\Delta(X+v)-(X+v)^3+\xi$.
3. Subtract the linear equation $\partial_t X=\Delta X+\xi$: the noise $\xi$ and the linear terms in $X$ cancel, leaving
$$
\partial_t v=\Delta v-(X+v)^3.
$$
4. Expand the cube: $(X+v)^3=X^3+3X^2v+3Xv^2+v^3$. The dangerous terms are those containing powers of the rough $X$, especially $X^3$ and $X^2$.
5. **Renormalize.** The objects $X^2$ and $X^3$ are products of distributions and diverge. Replace them by their renormalized (**Wick-ordered**) versions $:\!X^2\!:\,=X^2-C$ and $:\!X^3\!:\,=X^3-3CX$, where $C=\mathbb{E}[X_\epsilon^2]\to\infty$ is the (divergent) variance of the regularized convolution. These **Wick powers** are constructed as honest limits (Itô-chaos / Gaussian computation): subtracting the diverging mean $C$ leaves a finite random distribution.
6. The remainder equation becomes $\partial_t v=\Delta v-\big(:\!X^3\!:+3:\!X^2\!:v+3Xv^2+v^3\big)$. Crucially, $v$ turns out to be **more regular** than $X$ (the smoothing of the heat operator beats the roughness of the lower-order products), regular enough that all the remaining products with $v$ are classically defined.
7. The remainder equation for $v$ now has a locally Lipschitz nonlinearity acting on a function-valued $v$, so the fixed-point theory of §s5 gives a unique local solution $v$, and hence $u=X+:v:$ is the renormalized solution. $\blacksquare$

#### What renormalization means here, plainly

The constant $C\to\infty$ is a *counterterm*. The original equation, regularized, is really $\partial_t u_\epsilon=\Delta u_\epsilon-(u_\epsilon^3-3C_\epsilon u_\epsilon)+\xi_\epsilon$: an *infinite mass shift* $3C_\epsilon u_\epsilon$ is added so that the limit exists. This is precisely the **mass renormalization** of quantum field theory (§s11), arising here from the failure of the product of distributions, not from any Feynman diagram. The same divergence, two languages.

#### Worked example — the Wick square as a limit

Let $X_\epsilon$ be the convolution with noise smoothed at scale $\epsilon$, so $C_\epsilon=\mathbb{E}[X_\epsilon(x)^2]\sim\frac{1}{2\pi}\log(1/\epsilon)$ in $d=2$ (logarithmic divergence, matching §s7's marginal case). Define $:\!X_\epsilon^2\!:=X_\epsilon^2-C_\epsilon$. Then $\mathbb{E}[:\!X_\epsilon^2\!:]=0$ by construction, and one computes $\mathbb{E}\big[\big(\langle:\!X_\epsilon^2\!:,\varphi\rangle\big)^2\big]$ converges as $\epsilon\to0$ for smooth test $\varphi$: the centered square has a finite limit even though the raw square diverges. That finite limit *is* the Wick square $:\!X^2\!:$.

#### Common pitfalls

- The Da Prato–Debussche trick works only when *one* subtraction (the linear part) makes the remainder regular enough. In $d=3$ ($\Phi^4_3$) a single split is not enough — one must subtract a second, even rougher term, which is where regularity structures (§s9) become necessary.
- The counterterm $C$ is not "fudging." It is forced: without it the regularized solutions have no limit at all; with it they converge, and the limit is independent of the regularization (a renormalization-group universality statement).

<a id="s9"></a>
### Regularity structures and paracontrolled calculus (overview of the ideas)

#### What & why

When a single Da Prato–Debussche split is not enough (e.g. KPZ, $\Phi^4_3$), one needs a systematic theory to define, multiply, and renormalize all the divergent objects at once. Two such theories appeared around 2014: **regularity structures** (Hairer, Fields Medal 2014) and **paracontrolled calculus** (Gubinelli–Imkeller–Perkowski). We survey the ideas; the full machinery is beyond a first course, but the conceptual skeleton is graspable.

#### The core problem restated

Both theories solve the same difficulty: a singular SPDE forces us to multiply distributions whose regularities sum to a negative number (§s6, §s7). Classical analysis forbids this; these theories *enlarge the notion of a solution* so that the products become legal.

#### Regularity structures — the three ideas

1. **A solution is not a function but a "jet."** In ordinary Taylor analysis, a smooth function is described near each point by its Taylor polynomial — a list of coefficients (value, derivatives) attached to monomials $1,x,x^2,\dots$. Hairer's insight: for a singular SPDE, replace the monomials by an abstract **model** of symbols representing the *noise and its iterated integrals* (e.g. a symbol $\Xi$ for the noise, $\mathcal{I}(\Xi)$ for "noise convolved with the heat kernel," $\mathcal{I}(\Xi)^2$ for its square). A **modelled distribution** assigns to each spacetime point a linear combination of these symbols — a generalized Taylor expansion in the noise.

2. **Reconstruction theorem.** There is a canonical map (the **reconstruction operator** $\mathcal{R}$) turning an abstract modelled distribution into a genuine distribution, provided the local expansions are consistent at small scales. This is the analogue of "summing the Taylor series back into a function," and it is the technical heart of the theory.

3. **Renormalization as a group action.** The divergent products are tamed by redefining how the abstract symbols map to real distributions — a **renormalization group** acting on models. Different choices differ by counterterms (the $C\to\infty$ of §s8); the renormalized model gives a finite reconstructed solution. The **BPHZ theorem** (named after the QFT renormalization scheme of Bogoliubov–Parasiuk–Hepp–Zimmermann) provides a canonical, automatic choice of all counterterms.

#### Paracontrolled calculus — the alternative idea

Paracontrolled calculus reaches the same goal with **Littlewood–Paley** / **paraproduct** technology from harmonic analysis. The key device:

- A **paraproduct** $f\preccurlyeq g$ is the part of the product $fg$ built from "low-frequency $f$ times high-frequency $g$," which is *always* well-defined (no regularity obstruction); the dangerous part is the **resonant product** $f\odot g$ (comparable frequencies).
- One posits that the solution $u$ is **paracontrolled by** the stochastic convolution $X$: $u=u'\preccurlyeq X+\text{(smoother remainder)}$ for some derivative-like field $u'$. This **ansatz** says "$u$ looks locally like a multiple of $X$," mirroring the controlled-rough-paths idea from the theory of ordinary rough differential equations.
- Substituting the ansatz, the only remaining ill-defined object is a single resonant product of *explicit* noise quantities (computable once and for all, with its divergence subtracted as a counterterm). Everything else is classically defined. The SPDE then reduces to a well-posed equation for the remainder.

#### How the two theories relate

Both are systematic expansions of the solution in terms of explicitly renormalized noise objects; regularity structures use an abstract algebraic framework (good for arbitrarily many subtractions and general equations), paracontrolled calculus uses concrete Fourier analysis (more hands-on, fewer symbols, well-suited to equations needing only a few subtractions). Both prove **local well-posedness** of KPZ, $\Phi^4_3$, and many other previously intractable singular SPDEs, and both show the renormalized limit is **independent of the regularization** — the universality that justifies calling the answer "the" solution.

#### Worked example (conceptual) — counting the symbols for $\Phi^4_3$

For $\Phi^4_3$ the rough objects needed are: $X=\mathcal{I}(\Xi)$ (regularity $-\tfrac12-$), then $X^2$ (regularity $-1-$, divergent — Wick subtract a constant), $X^3$ (regularity $-\tfrac32-$, Wick subtract), and one further "resonant" object $X^2\cdot\mathcal{I}(X^3)$ that requires a *second*, logarithmically divergent counterterm. So $\Phi^4_3$ needs **two** distinct renormalization constants — one more than the single mass shift of $\Phi^4_2$ in §s8. This finite list of divergences is exactly what the theories organize automatically.

#### Common pitfalls

- These theories give *local* well-posedness and renormalized limits; they do not by themselves give global existence or identify the invariant measure — that is separate analysis (§s10).
- "Renormalization" here is not perturbative QFT with infinitely many diagrams. Subcriticality (§s7) guarantees only **finitely many** divergent objects, which is precisely why the theory closes.

## Part E · From SPDEs to quantum field theory

<a id="s10"></a>
### Stochastic quantization (Parisi–Wu) — the $\Phi^4$ measure as the invariant measure of an SPDE

#### What & why

We now reveal the deep purpose of all the machinery. Parisi and Wu (1981) proposed: to construct and sample a Euclidean quantum field — a probability measure on field configurations — *run an SPDE to equilibrium*. The **invariant (stationary) measure** of the dynamical $\Phi^4$ equation is exactly the **$\Phi^4$ quantum field measure**. SPDEs become a tool of constructive field theory.

> **The $\Phi^4$ measure (target).** Formally, on fields $\phi:D\to\mathbb{R}$,
> $$
> \nu(d\phi)\propto\exp\!\Big(-\!\int_D\big[\tfrac12|\nabla\phi|^2+\tfrac14\phi^4\big]dx\Big)\,\mathcal{D}\phi,
> $$
> the **Euclidean $\Phi^4$ measure**: a Gaussian (free-field) part $e^{-\frac12\int|\nabla\phi|^2}$ tilted by the quartic interaction $e^{-\frac14\int\phi^4}$. ($\mathcal{D}\phi$ is the formal "flat" measure on fields.)

> **The dynamical $\Phi^4$ equation (the SPDE).**
> $$
> \partial_t\phi=\Delta\phi-\phi^3+\sqrt{2}\,\xi,
> $$
> with $t$ a **fictitious extra time** (not physical time) and $\xi$ space–time white noise. This is the renormalized equation of §s8 with a specific noise normalization.

#### Why the invariant measure is the $\Phi^4$ measure — derivation

The mechanism is the infinite-dimensional analogue of a basic fact about diffusions: an overdamped Langevin equation $\dot\phi=-\nabla\mathcal{S}(\phi)+\sqrt2\,\xi$ relaxes to the **Gibbs measure** $\propto e^{-\mathcal{S}(\phi)}$.

**Derivation (finite-dimensional model, then lifted).**
1. Consider first finitely many variables $\phi\in\mathbb{R}^n$ obeying the SDE $d\phi=-\nabla\mathcal{S}(\phi)\,dt+\sqrt2\,dW$, a **gradient (Langevin) system** with potential $\mathcal{S}$.
2. The probability density $\rho(\phi,t)$ evolves by the **Fokker–Planck equation** (from the Stochastic Processes guide): $\partial_t\rho=\nabla\cdot(\rho\,\nabla\mathcal{S})+\Delta\rho$, where the first term is drift and the second (with coefficient matching $\sqrt2$) is diffusion.
3. Seek a stationary density $\rho_\infty$ with $\partial_t\rho_\infty=0$. Try $\rho_\infty\propto e^{-\mathcal{S}}$. Then $\nabla\rho_\infty=-\rho_\infty\nabla\mathcal{S}$, so $\Delta\rho_\infty=\nabla\cdot(\nabla\rho_\infty)=\nabla\cdot(-\rho_\infty\nabla\mathcal{S})$, which exactly cancels the drift term $\nabla\cdot(\rho_\infty\nabla\mathcal{S})$. Hence $\partial_t\rho_\infty=0$: the Gibbs measure $e^{-\mathcal{S}}$ is invariant.
4. **Identify the potential.** For the dynamical $\Phi^4$ equation the drift is $\Delta\phi-\phi^3$. This is $-\nabla\mathcal{S}$ for the **action functional** $\mathcal{S}(\phi)=\int\big[\tfrac12|\nabla\phi|^2+\tfrac14\phi^4\big]dx$, since the functional ("Fréchet") gradient of $\tfrac12\int|\nabla\phi|^2$ is $-\Delta\phi$ (integration by parts) and the gradient of $\tfrac14\int\phi^4$ is $\phi^3$. So drift $=-\nabla\mathcal{S}$ with exactly the $\Phi^4$ action.
5. **Lift to infinite dimensions.** Replacing $\mathbb{R}^n$ by the field space and the SDE by the SPDE, the same gradient/Gibbs computation (made rigorous via §s5 well-posedness and §s8–s9 renormalization) shows the invariant measure of the dynamical $\Phi^4$ equation is $\nu\propto e^{-\mathcal{S}(\phi)}$ — the Euclidean $\Phi^4$ measure. $\blacksquare$

#### What this buys us

- **Construction.** Running the SPDE and showing it has a (renormalized) invariant measure *constructs* the $\Phi^4$ measure — a major goal of constructive field theory, achieved by Hairer–Mattingly and others in $d=2,3$ via the dynamics.
- **Sampling.** Numerically, integrating the SPDE forward produces samples from the quantum field measure — the basis of certain Monte-Carlo schemes (Langevin sampling).
- **The same counterterm.** The mass renormalization $C\to\infty$ of §s8 is *forced* to make the SPDE well-posed, and it is the same counterterm that makes the $\Phi^4$ measure well-defined. The two renormalizations coincide — strong evidence the whole picture is consistent.

#### Worked example — the Ornstein–Uhlenbeck (free-field) case

Drop the $\phi^3$ term: $\partial_t\phi=\Delta\phi+\sqrt2\,\xi$ is an infinite-dimensional **Ornstein–Uhlenbeck process** (linear Langevin). By the derivation with $\mathcal{S}(\phi)=\tfrac12\int|\nabla\phi|^2$, its invariant measure is the **Gaussian free field** $\propto e^{-\frac12\int|\nabla\phi|^2}$ — the free quantum field. Mode by mode the equilibrium variance of the $k$-th mode is $1/\gamma_k\sim1/k^2$, matching the spatial-Brownian equilibrium found in §s3. The interacting case is this Gaussian free field tilted by $e^{-\frac14\int\phi^4}$.

#### Common pitfalls

- The fictitious time $t$ of stochastic quantization is **not** physical time and not the imaginary time of the path integral; it is an artificial relaxation parameter whose only job is to reach equilibrium.
- The invariant measure exists only after renormalization; the *unrenormalized* dynamical $\Phi^4$ equation in $d\ge2$ has no invariant probability measure on function space.

<a id="s11"></a>
### Physics — Euclidean quantum field theory, the dynamical approach, and constructive field theory

#### What & why

This closing section places the whole guide in its physical home. The SPDEs we solved are not just analysis exercises; they are one of the few rigorous routes into **quantum field theory (QFT)**, the framework underlying particle physics and critical phenomena.

#### Euclidean quantum field theory, restated

In the path-integral formulation (from the Stochastic Processes guide), quantum amplitudes are computed by summing $e^{iS/\hbar}$ over field histories. Rotating to **imaginary time** (the **Wick rotation** $t\to-i\tau$) turns the oscillatory $e^{iS}$ into a positive weight $e^{-S_E}$, where $S_E$ is the **Euclidean action**. The resulting **Euclidean QFT** is a *probability measure* on field configurations — exactly the kind of object (a Gaussian measure tilted by an interaction, §s1, §s10) this guide studies. For the scalar field with quartic self-interaction, $S_E=\int[\tfrac12|\nabla\phi|^2+\tfrac{m^2}2\phi^2+\tfrac\lambda4\phi^4]dx$, and the measure is the $\Phi^4$ measure of §s10.

#### The dynamical approach, summarized

The thread of this guide, read physically:

1. The Euclidean $\Phi^4$ measure is the equilibrium of the dynamical $\Phi^4$ SPDE (§s10) — stochastic quantization.
2. That SPDE is ill-posed because of distributional products (§s6, §s7) and requires renormalization (§s8, §s9).
3. The renormalization counterterms are exactly the **mass and coupling renormalizations** of perturbative QFT — but here they arise from analysis (failure of products) rather than from summing Feynman diagrams, and there are only **finitely many** of them because the theory is **subcritical** (§s7).
4. The dimension thresholds of §s7 — function-valued in $d=1$, renormalizable in $d=2,3$, trivial ("free") in $d\ge4$ — reproduce a famous physics result: $\Phi^4$ theory is believed **trivial** (non-interacting) in four spacetime dimensions, proven rigorously in $d\ge5$ and at $d=4$. The analysis and the physics agree.

#### Constructive field theory, and what was achieved

**Constructive quantum field theory** is the program of building QFT models as genuine mathematical objects (measures satisfying the **Osterwalder–Schrader axioms**, which guarantee a quantum theory can be reconstructed by un-rotating to real time). Historically this was done in the 1970s by Glimm, Jaffe, and others using cluster expansions. The SPDE / stochastic-quantization route, completed in $d=2$ and $d=3$ around 2014–2020 (Hairer, Gubinelli–Imkeller–Perkowski, Mourrat–Weber, Hairer–Mattingly, and others), gave an **independent construction** of $\Phi^4_2$ and $\Phi^4_3$ as invariant measures of renormalized SPDEs, together with new probabilistic information (e.g. exponential relaxation to equilibrium) inaccessible to the older methods.

#### Why physicists care about KPZ specifically

The KPZ equation (§s6) is the representative of a vast **universality class**: the long-time, large-scale statistics of growing interfaces — bacterial colonies, burning fronts, liquid-crystal turbulence, the corner growth of crystals — all converge to the same limiting fluctuation laws (governed by the **Tracy–Widom distributions** of random matrix theory), regardless of microscopic details. The renormalized KPZ equation is the continuum fixed point of this class. That a single ill-posed SPDE captures the universal physics of so many systems is one of the triumphs of the subject, and the rigorous construction of its solution (§s6, §s9) put this universality on a firm footing.

#### Worked example — reading off the renormalization from dimension

Take $\Phi^4$ and ask, from §s7, how many counterterms physics predicts.
1. $d=2$: the field has regularity $0-$; only $\phi^2$ diverges (logarithmically), needing **one** counterterm — a mass renormalization. This matches the single constant $C$ of §s8.
2. $d=3$: the field has regularity $-\tfrac12-$; $\phi^2$ and one composite object diverge, needing **two** counterterms — matching the two constants of §s9's $\Phi^4_3$ count and the two divergent Feynman diagrams (tadpole and sunset) of perturbative QFT.
3. $d\ge4$: supercritical; infinitely many divergences would be needed and no nontrivial limit survives — the triviality result. The counting from pure SPDE regularity reproduces, with no Feynman diagrams, the renormalization structure physicists derive perturbatively.

#### Worked example — power counting the dimension of the coupling

Physicists predict renormalizability by a dimensional argument; we recover it from the SPDE scaling of §s7. Assign the field $\phi$ a scaling dimension by demanding the free action $\int|\nabla\phi|^2\,d^dx$ be scale-invariant under $x\to\lambda x$: the volume element scales as $\lambda^d$, the gradient-squared as $\lambda^{-2}$, so $\phi$ must scale as $\lambda^{(2-d)/2}$, i.e. $\phi$ has **mass dimension** $\tfrac{d-2}{2}$.

1. The interaction $\int\phi^4\,d^dx$ then scales as $\lambda^{d}\cdot\lambda^{-4(d-2)/2}=\lambda^{d-2(d-2)}=\lambda^{4-d}$.
2. The coupling $\lambda_{\text{coupling}}$ multiplying it must carry mass dimension $d-4$ to make the action dimensionless.
3. **Reading the sign.** If $d<4$ the coupling has *positive* mass dimension: the interaction grows at large scales / shrinks at small scales — a **relevant**, super-renormalizable interaction (finitely many divergences). This is the subcritical regime of §s7, exactly $d=1,2,3$. If $d=4$ the coupling is dimensionless (marginal — the borderline triviality case), and if $d>4$ it is irrelevant and the theory is free.

This three-line computation reproduces, purely from scaling, the same $d=1,2,3$ versus $d\ge4$ dichotomy that the mode-sum convergence of §s7 produced — analysis and dimensional analysis agreeing on where renormalization is possible.

#### Common pitfalls

- Euclidean QFT is a *probability measure*; physical (Minkowski) quantities require analytic continuation back to real time, which the Osterwalder–Schrader axioms make rigorous but which can be delicate.
- The success in $d=2,3$ does not extend to the physically central case of four-dimensional non-abelian gauge theory (Yang–Mills); constructing that remains an open Millennium Prize problem, and the SPDE approach to it is an active frontier.

---

*This guide built the theory of stochastic partial differential equations from the ground up: Gaussian measures on function spaces, where the trace-class condition divides genuine random functions from the rougher white noise; space–time white noise and the cylindrical Wiener process, the infinite-dimensional Brownian motion that drives every equation; the stochastic heat equation, solved by the mild semigroup formula whose exponential damping converts divergent noise into a function-valued field in one dimension; Itô calculus in a Hilbert space, with its Hilbert–Schmidt isometry and trace correction; and existence and uniqueness for semilinear equations by a Banach contraction. We then met the pathologies — the KPZ equation, ill-posed because it multiplies distributions of negative regularity, and the regularity ladder that ties solvability to spatial dimension — and the cures: the Da Prato–Debussche split with its first renormalization counterterm, and the modern theories of regularity structures and paracontrolled calculus that organize all the divergences of subcritical equations into a finite, automatic renormalization. Finally stochastic quantization revealed the purpose of it all: the $\Phi^4$ quantum field measure is the equilibrium of a renormalized SPDE, and the counterterms that make the dynamics well-posed are the very mass and coupling renormalizations of Euclidean quantum field theory. The single thread: a field buffeted by white noise is too rough to obey its equation literally, and the disciplined subtraction of the resulting infinities — renormalization — is simultaneously the analytic price of making sense of the noise and the physical mechanism by which quantum fields are constructed.*
