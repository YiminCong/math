**English** · [中文](partial-differential-equations.zh.md)

# Partial Differential Equations of Physics, *the equations of fields and waves.*

*A self-contained first course in the partial differential equations that govern physics — from the meaning and classification of a PDE, through the wave, heat, and Laplace equations, to separation of variables, Sturm–Liouville theory, the special geometries of spheres and cylinders, Green's functions, and the Schrödinger equation. Every symbol is defined in words, every formula is motivated, and every derivation is a numbered, gap-free chain of reasons. Built on basic algebra, single-variable calculus, and a little partial differentiation; the bridges to Fourier analysis and the special functions are made explicit.*

[← Back to all guides](../README.md)

## Part A · What a PDE is and how to read one

<a id="s0"></a>
### Motivation and classification of second-order linear PDEs

#### What & why, in one breath

An **ordinary differential equation** (ODE) relates a function of *one* variable to its derivatives — for example $y''(x)+y(x)=0$. A **partial differential equation** (PDE) relates a function of *several* variables to its **partial derivatives**: rates of change with respect to one variable while the others are held fixed. The unknown is now a field — a temperature $u(x,t)$ spread over space and time, the height $u(x,t)$ of a vibrating string, the electric potential $u(x,y,z)$ filling a room. Almost every fundamental law of classical and quantum physics is a PDE, because physics is local: what a field does *here and now* is dictated by its values and slopes in an infinitesimal neighborhood, which is exactly what derivatives encode.

#### Notation, defined from zero

- A function of several variables: $u(x,y)$, $u(x,t)$, etc. The inputs are **independent variables**; $u$ is the **dependent variable** or **field**.
- A **partial derivative** $\dfrac{\partial u}{\partial x}$ means: differentiate $u$ with respect to $x$ while treating every other variable as a constant. We abbreviate it $u_x$. Second partials: $u_{xx}=\partial^2 u/\partial x^2$, and the **mixed partial** $u_{xy}=\partial^2 u/(\partial x\,\partial y)$.
- **Clairaut's theorem** (stated, used throughout): if the second partials of $u$ are continuous, then mixed partials are equal, $u_{xy}=u_{yx}$. We assume enough smoothness that this always holds.
- The **order** of a PDE is the order of its highest derivative. Most of physics lives at order two.
- The **Laplacian** is the sum of unmixed second partials, written $\nabla^2 u$ or $\Delta u$. In two space dimensions $\nabla^2 u = u_{xx}+u_{yy}$; in three, $u_{xx}+u_{yy}+u_{zz}$.

#### Linear, and why it is the gift that keeps giving

A PDE is **linear** if the unknown $u$ and all its derivatives appear only to the first power, never multiplied together, and only multiplied by known functions of the independent variables. The general second-order linear PDE in two variables $x,y$ is

$$
A\,u_{xx} + 2B\,u_{xy} + C\,u_{yy} + D\,u_x + E\,u_y + F\,u = G,
$$

where $A,B,C,D,E,F,G$ are given functions of $x,y$. It is **homogeneous** if $G=0$.

> **The superposition principle.** If $u_1$ and $u_2$ each solve a homogeneous linear PDE $\mathcal{L}u=0$ (where $\mathcal{L}$ is the linear differential operator collecting all the terms), then so does any combination $c_1 u_1 + c_2 u_2$.
>
> *Proof.* $\mathcal{L}$ is linear, meaning $\mathcal{L}(c_1u_1+c_2u_2)=c_1\mathcal{L}u_1+c_2\mathcal{L}u_2$ — this is just the fact that differentiation is linear ($(f+g)'=f'+g'$, $(cf)'=cf'$) applied term by term. Each term $\mathcal{L}u_i=0$ by hypothesis, so the sum is $c_1\cdot0+c_2\cdot0=0$. $\blacksquare$

Superposition is the engine of nearly every method in this guide: we will build complicated solutions by summing simple ones.

#### Classification: the discriminant

The three great equations of physics — wave, heat, Laplace — behave completely differently, and the difference is captured by a single number built from the top (second-order) coefficients. By analogy with the conic sections $Ax^2+2Bxy+Cy^2=\text{const}$, whose shape is fixed by the **discriminant** $B^2-AC$, we classify the PDE at a point by:

$$
\Delta = B^2 - AC.
$$

> **Definition — classification.** A second-order linear PDE is, at a point,
> - **elliptic** if $\Delta = B^2-AC < 0$;
> - **parabolic** if $\Delta = B^2-AC = 0$;
> - **hyperbolic** if $\Delta = B^2-AC > 0$.

Why this trichotomy matters — the three archetypes, each verified below:

- **Laplace** $u_{xx}+u_{yy}=0$: here $A=1,B=0,C=1$, so $\Delta=0-1=-1<0$, **elliptic**. Models *equilibrium* (steady-state heat, electrostatics). Smooth everywhere; data is given on a closed boundary.
- **Heat** $u_t = \kappa\,u_{xx}$: rename variables so $y=t$; then the only second-order term is $u_{xx}$, giving $A=1,B=0,C=0$, so $\Delta=0$, **parabolic**. Models *irreversible diffusion*; data is an initial profile plus boundary values; smooths data out and runs one way in time.
- **Wave** $u_{tt}=c^2 u_{xx}$, i.e. $c^2u_{xx}-u_{tt}=0$ with $y=t$: $A=c^2,B=0,C=-1$, so $\Delta=0-(c^2)(-1)=c^2>0$, **hyperbolic**. Models *propagation*; data is initial position and velocity; carries sharp signals at finite speed and is reversible.

#### What the names *mean* (intuition)

The discriminant controls the **characteristics**, special curves along which information travels (s1). Hyperbolic equations have two families of real characteristics (signals run along them at finite speed); parabolic have one; elliptic have none (no preferred directions, influence is instantaneous and global). This is why a hyperbolic wave keeps a thrown stone's splash sharp, a parabolic diffusion blurs it instantly everywhere, and an elliptic potential has no "time" at all.

#### Which data makes each problem well-posed

A problem is **well-posed** (Hadamard's criterion) if a solution exists, is unique, and depends continuously on the data. The right data differs by class, and getting it wrong makes the problem ill-posed:
- **Hyperbolic** (wave): give the field *and* its time-derivative at the initial instant on an open region, plus boundary values — this is the **Cauchy/initial-value problem**. Two conditions because the equation is second order in the time-like variable.
- **Parabolic** (heat): give the field at the initial instant plus boundary values for all later times — an **initial-boundary-value problem**. Only one initial condition (first order in time), and only *forward* in time.
- **Elliptic** (Laplace): there is no time; give the field (Dirichlet) or its normal derivative (Neumann) on the *entire closed boundary* — a **boundary-value problem**. Trying to pose Cauchy data for Laplace's equation is ill-posed: tiny ripples in the data explode (Hadamard's example $u=\frac1n\sin(nx)\sinh(ny)$ has data $O(1/n)$ but interior values $O(e^{ny}/n)$).

Matching data to class is the single most common source of error in setting up a physical PDE, and the rest of the guide always respects it.

#### Worked classification

Classify $u_{xx} + 4u_{xy} + 3u_{yy} = 0$. Match to the template: $A=1$, $2B=4\Rightarrow B=2$, $C=3$. Then $\Delta = B^2-AC = 4-1\cdot3 = 1>0$: **hyperbolic**. (We will see in s1 it factors into two transport equations.)

#### Reducing to canonical form (the deeper meaning of the classes)

The classification is not just a label: it tells you the *simplest shape* into which a change of variables can squeeze the equation. By rotating/shearing coordinates one can always remove the cross term and rescale, reaching a **canonical form**:
- hyperbolic $\to$ $u_{\xi\eta}=\text{lower order}$ (or, rotated, $u_{ss}-u_{\tau\tau}=\cdots$), the **wave** template;
- parabolic $\to$ $u_{\eta\eta}=\text{lower order}$, the **heat** template;
- elliptic $\to$ $u_{\xi\xi}+u_{\eta\eta}=\text{lower order}$, the **Laplace** template.

We will actually carry out the hyperbolic reduction for the wave equation in s2 (the change to characteristic coordinates $\xi=x-ct,\eta=x+ct$ produces exactly $u_{\xi\eta}=0$). The lesson: there are really only *three* second-order linear PDEs, and every such equation is locally one of them in disguise. That is why this guide spends Part B on precisely those three.

#### Common pitfalls

- The classification can change from point to point if $A,B,C$ depend on position. The Tricomi equation $y\,u_{xx}+u_{yy}=0$ is elliptic for $y>0$ and hyperbolic for $y<0$.
- The coefficient is $2B$, not $B$, in the standard form. Halve the mixed coefficient before computing $\Delta$.

<a id="s1"></a>
### First-order PDEs and the method of characteristics

#### What & why

Before second order, master first order — it carries the cleanest physical picture: **transport**. A first-order PDE turns out to say "the unknown is constant along certain moving curves." Finding those curves, the **characteristics**, reduces the PDE to ODEs we can already solve. This idea reappears for the wave equation (s2) and is the backbone of classification (s0).

#### The transport equation and the idea

Consider the **linear transport (advection) equation** for $u(x,t)$ with constant speed $c$:

$$
u_t + c\,u_x = 0,
$$

with **initial condition** $u(x,0)=f(x)$, where $f$ is a given function (the profile at time zero).

> **Claim.** The solution is $u(x,t)=f(x-ct)$: the initial shape $f$ slides rigidly to the right at speed $c$.

*Derivation by characteristics, gap-free.*
1. Introduce a curve in the $(x,t)$-plane parametrized by $s$: $\big(x(s),t(s)\big)$. We will choose it cleverly. Define the value of $u$ along it as $U(s)=u\big(x(s),t(s)\big)$.
2. Differentiate $U$ with the chain rule (valid because $u$ is assumed differentiable): $\dfrac{dU}{ds}=u_x\dfrac{dx}{ds}+u_t\dfrac{dt}{ds}$.
3. *Choose* the curve so that $\dfrac{dt}{ds}=1$ and $\dfrac{dx}{ds}=c$. This is a free choice of parametrization, always available. Then step 2 becomes $\dfrac{dU}{ds}=c\,u_x+u_t$.
4. The right side is exactly the left side of the PDE, which equals $0$. Therefore $\dfrac{dU}{ds}=0$: **$u$ is constant along the chosen curve.** These curves are the *characteristics*.
5. Solve the curve ODEs from step 3: $t(s)=s+t_0$ and $x(s)=cs+x_0$. Taking the start at $s=0$ on the initial line $t=0$, set $t_0=0$ so $t=s$, and let $x_0=\xi$ (the foot of the characteristic). Then $x=ct+\xi$, i.e. $\xi = x-ct$ is constant along the curve.
6. Since $u$ is constant along the characteristic and at $t=0$ equals $f(\xi)=f(x_0)$, we get $u(x,t)=f(\xi)=f(x-ct)$. $\blacksquare$

#### Worked example with real numbers

Let $c=2$ and $f(x)=e^{-x^2}$ (a bump centered at the origin). The solution is $u(x,t)=e^{-(x-2t)^2}$. At $t=0$ the bump peaks at $x=0$; at $t=3$ it peaks where $x-2\cdot3=0$, i.e. $x=6$. The bump has moved $6$ units in $3$ seconds — speed $2$, with shape unchanged. Check the PDE: $u_t = e^{-(x-2t)^2}\cdot(-2)(x-2t)(-2)=4(x-2t)u$, and $u_x = -2(x-2t)u$, so $u_t+2u_x = 4(x-2t)u + 2\cdot(-2)(x-2t)u = 0$. Confirmed.

#### A variable-coefficient example

Solve $u_t + x\,u_x = 0$, $u(x,0)=f(x)$. Characteristic ODEs: $\dfrac{dt}{ds}=1$, $\dfrac{dx}{ds}=x$. From the second, $x(s)=x_0 e^{s}$; with $t=s$ this gives $x=x_0 e^{t}$, so the conserved quantity is $\xi = x e^{-t}$. Hence $u(x,t)=f(x e^{-t})$. Sanity check: $u_t = f'(xe^{-t})\cdot x\cdot(-e^{-t})$ and $x\,u_x = x\cdot f'(xe^{-t})\,e^{-t}$; they cancel.

#### Intuition and pitfalls

- A first-order PDE has *one* family of characteristics; that is why it propagates data in a single direction. Second-order hyperbolic equations will have *two*.
- Pitfall: characteristics can cross when the speed depends on $u$ (nonlinear case, e.g. Burgers' equation), and where they cross the smooth solution breaks down — that is a **shock**. The linear cases above never form shocks.

#### The general recipe (so you can solve any of them)

For a general first-order linear PDE $a(x,t)\,u_x + b(x,t)\,u_t = c(x,t)$ the method is mechanical:
1. Write the **characteristic system** $\dfrac{dx}{ds}=a$, $\dfrac{dt}{ds}=b$, $\dfrac{dU}{ds}=c$, where $U(s)=u$ along the curve. (The first two trace the curve; the third tells how $u$ changes along it.)
2. Solve the first two to get the curves and a conserved label $\xi$ (the constant of integration that names which characteristic you are on).
3. Solve the third ODE for $U$ in terms of $s$ and the label.
4. Re-express $s$ and the label in terms of $x,t$ and fit the initial data on $t=0$.

When $c=0$ (homogeneous) step 3 says $u$ is constant along characteristics, recovering the picture above. When $c\neq0$ the value of $u$ *grows or decays* as it rides the characteristic — a forced transport.

#### A forced example with numbers

Solve $u_t + u_x = u$, $u(x,0)=\cos x$. System: $\dot t=1,\dot x=1,\dot U=U$ (dots are $d/ds$). With $t=s$, $x=s+\xi$ so $\xi=x-t$; and $\dot U=U\Rightarrow U=U_0 e^{s}=U_0 e^{t}$. At $s=0$, $U_0=\cos\xi=\cos(x-t)$. Hence $u(x,t)=e^{t}\cos(x-t)$: the cosine wave both translates at speed $1$ and is amplified by $e^t$. Check: $u_t = e^t\cos(x-t)+e^t\sin(x-t)$, $u_x=-e^t\sin(x-t)$; sum $u_t+u_x=e^t\cos(x-t)=u$. Confirmed.

## Part B · The three classical equations

<a id="s2"></a>
### The wave equation in 1D; d'Alembert's solution

#### What & why

The **wave equation** describes anything whose restoring force is proportional to curvature: a plucked string, a sound wave, light in vacuum. In one space dimension it reads

$$
u_{tt} = c^2\,u_{xx},
$$

where $u(x,t)$ is the displacement, $t$ time, $x$ position, and $c>0$ a constant with units of speed. We derive it physically in s7; here we *solve* it completely on the infinite line and read off the physics. d'Alembert's 1747 solution is the most beautiful closed form in the subject.

#### The factoring trick

The wave operator factors like a difference of squares. Treating $\partial_t$ and $\partial_x$ as symbols (legitimate because they commute by Clairaut's theorem, s0):

$$
\partial_t^2 - c^2\partial_x^2 = (\partial_t - c\,\partial_x)(\partial_t + c\,\partial_x).
$$

So the wave equation is $(\partial_t - c\partial_x)(\partial_t + c\partial_x)u = 0$: apply the right factor, then the left. Each factor is a transport operator from s1.

#### Full derivation via characteristic coordinates

1. **Change variables** to $\xi = x - ct$ and $\eta = x + ct$. These are the two characteristic families ($\xi$ const = right-movers, $\eta$ const = left-movers). The map is invertible: $x=\tfrac12(\xi+\eta)$, $t=\tfrac1{2c}(\eta-\xi)$.
2. **Transform the derivatives** with the chain rule. Since $\xi_x=1,\eta_x=1,\xi_t=-c,\eta_t=c$:
$$
u_x = u_\xi + u_\eta, \qquad u_t = -c\,u_\xi + c\,u_\eta.
$$
3. **Second derivatives**, applying the operators again (Clairaut lets us treat $u_{\xi\eta}=u_{\eta\xi}$):
$$
u_{xx} = u_{\xi\xi} + 2u_{\xi\eta} + u_{\eta\eta},\qquad
u_{tt} = c^2\big(u_{\xi\xi} - 2u_{\xi\eta} + u_{\eta\eta}\big).
$$
4. **Substitute** into $u_{tt}-c^2u_{xx}=0$:
$$
c^2(u_{\xi\xi}-2u_{\xi\eta}+u_{\eta\eta}) - c^2(u_{\xi\xi}+2u_{\xi\eta}+u_{\eta\eta}) = -4c^2 u_{\xi\eta}=0.
$$
Since $c\neq0$, this is simply $u_{\xi\eta}=0$.
5. **Integrate twice.** $u_{\xi\eta}=0$ says $\partial_\eta(u_\xi)=0$, so $u_\xi$ does not depend on $\eta$: $u_\xi = p(\xi)$ for some function $p$. Integrate in $\xi$: $u = F(\xi) + G(\eta)$, where $F'=p$ and $G$ is the constant of integration (constant in $\xi$, hence an arbitrary function of $\eta$).
6. **Return to $x,t$:**
$$
u(x,t) = F(x-ct) + G(x+ct).
$$
This is the **general solution**: an arbitrary right-moving shape $F$ plus an arbitrary left-moving shape $G$. $\blacksquare$

#### Fitting the initial data — d'Alembert's formula

Suppose $u(x,0)=\phi(x)$ (initial position) and $u_t(x,0)=\psi(x)$ (initial velocity), with $\phi,\psi$ given.

1. At $t=0$: $F(x)+G(x)=\phi(x)$. (★)
2. $u_t = -c\,F'(x-ct)+c\,G'(x+ct)$; at $t=0$: $-cF'(x)+cG'(x)=\psi(x)$, so $G'(x)-F'(x)=\psi(x)/c$. Integrate from a reference $0$ to $x$: $G(x)-F(x)=\dfrac1c\displaystyle\int_0^x\psi(\sigma)\,d\sigma + K$, with $K$ a constant. (★★)
3. Solve the linear system (★),(★★) for $F$ and $G$:
$$
F(x)=\tfrac12\phi(x)-\tfrac1{2c}\!\int_0^x\!\psi -\tfrac{K}{2},\qquad
G(x)=\tfrac12\phi(x)+\tfrac1{2c}\!\int_0^x\!\psi +\tfrac{K}{2}.
$$
4. Substitute $x\to x-ct$ in $F$ and $x\to x+ct$ in $G$ and add; the constants $K$ cancel and the two integrals combine into one over $[x-ct,\,x+ct]$:

$$
\boxed{\,u(x,t)=\tfrac12\big[\phi(x-ct)+\phi(x+ct)\big]+\tfrac1{2c}\int_{x-ct}^{x+ct}\psi(\sigma)\,d\sigma\,}
$$

This is **d'Alembert's formula**. $\blacksquare$

#### Interpretation

- The position term is the initial profile split into two half-amplitude copies, one traveling right, one left at speed $c$.
- The velocity term spreads as a growing "tent": the value at $(x,t)$ depends only on the initial data inside the interval $[x-ct,\,x+ct]$, the **domain of dependence**. Information travels at most at speed $c$ — *finite propagation speed*, the hallmark of hyperbolic equations.

#### Worked example

Take $c=1$, $\phi(x)=0$, $\psi(x)=1$ on $[-1,1]$ and $0$ outside (a region given an initial kick). Then $u(x,t)=\tfrac12\int_{x-t}^{x+t}\psi$. For $x=0,t=0.5$: the interval $[-0.5,0.5]$ lies inside $[-1,1]$, so $\int\psi = 1$ and $u=\tfrac12$. For $x=0,t=2$: interval $[-2,2]$, but $\psi=1$ only on $[-1,1]$ of length $2$, so $\int\psi=2$ and $u=1$. The disturbance has spread and the central value saturated — a clean illustration of finite-speed spreading.

#### Conservation of energy (why waves don't fade)

Define the **energy** of the wave on the whole line as
$$
E(t)=\frac12\int_{-\infty}^{\infty}\big(u_t^2 + c^2 u_x^2\big)\,dx,
$$
the kinetic part ($u_t^2$, motion) plus the potential part ($c^2u_x^2$, stretching).

> **Claim.** $E(t)$ is constant in time (for data decaying at infinity).

*Proof.*
1. Differentiate under the integral: $E'(t)=\int (u_t u_{tt} + c^2 u_x u_{xt})\,dx$.
2. In the second term integrate by parts in $x$: $\int c^2 u_x u_{xt}\,dx = [c^2 u_x u_t]_{-\infty}^\infty - \int c^2 u_{xx}u_t\,dx$. The boundary term vanishes (data decays), leaving $-\int c^2 u_{xx}u_t\,dx$.
3. So $E'(t)=\int u_t(u_{tt}-c^2u_{xx})\,dx$. The parenthesis is zero by the wave equation. Hence $E'(t)=0$. $\blacksquare$

This is why a frictionless wave keeps ringing — contrast the heat equation, which dissipates. Energy conservation is the hyperbolic counterpart to the heat equation's maximum principle and likewise gives uniqueness.

#### Pitfalls

- d'Alembert needs the *whole line*. On an interval (a real string) you must reflect the data at the ends to enforce boundary conditions; that reflection is exactly the Fourier/normal-mode picture of s7.
- The formula needs $\phi\in C^2$, $\psi\in C^1$ for a classical solution; rougher data gives a *weak* solution that still propagates at speed $c$.

<a id="s3"></a>
### The heat / diffusion equation

#### What & why

The **heat equation** governs how temperature, concentration, or any diffusing quantity smooths out over time:

$$
u_t = \kappa\,u_{xx},
$$

with $u(x,t)$ the temperature, $\kappa>0$ the **thermal diffusivity** (units length$^2$/time). In three dimensions $u_t=\kappa\nabla^2 u$. Unlike the wave equation, it is irreversible: heat flows from hot to cold and cannot be un-stirred.

#### Physical derivation (gap-free)

We combine two physical laws over a thin slab $[x,x+\Delta x]$.

1. **Conservation of energy.** The heat energy in the slab is $\int_x^{x+\Delta x}\rho c\,u\,dx'$, where $\rho$ is mass density and $c$ the specific heat ($\rho c$ = heat per unit length per degree). Its rate of change equals the net heat flowing in:
$$
\frac{d}{dt}\int_x^{x+\Delta x}\rho c\,u\,dx' = q(x,t)-q(x+\Delta x,t),
$$
where $q$ is the **heat flux** (energy per time crossing a point, positive to the right). This is bookkeeping: what accumulates equals in minus out.
2. **Fourier's law of conduction** (the constitutive physics): heat flows down the temperature gradient, $q = -k\,u_x$, with $k>0$ the conductivity. Hot points push heat toward cold ones.
3. Substitute and use the fundamental theorem of calculus on the right: $q(x)-q(x+\Delta x) = -[q(x+\Delta x)-q(x)] = -\int_x^{x+\Delta x} q_{x'}\,dx'$. So
$$
\int_x^{x+\Delta x}\big(\rho c\,u_t + q_{x'}\big)dx' = 0.
$$
4. This holds for *every* slab, of every width and position. A continuous integrand whose integral over every interval is zero must itself be zero (if it were positive somewhere, by continuity it would be positive on a small interval, giving a positive integral — contradiction). Hence $\rho c\,u_t + q_x = 0$.
5. Insert Fourier's law $q=-k u_x$: $\rho c\,u_t - k\,u_{xx}=0$, i.e. $u_t = \dfrac{k}{\rho c}\,u_{xx} = \kappa\,u_{xx}$ with $\kappa=k/(\rho c)$. $\blacksquare$

#### Basic properties

- **Smoothing.** Even a jagged initial profile becomes infinitely smooth for any $t>0$. The diffusion kernel (below) is a Gaussian, and convolving with a smooth Gaussian smooths everything.
- **Infinite propagation speed.** The fundamental solution
$$
G(x,t)=\frac{1}{\sqrt{4\pi\kappa t}}\,e^{-x^2/(4\kappa t)}
$$
is nonzero for *all* $x$ the instant $t>0$. A point heat source is felt (tinily) everywhere immediately — the parabolic counterpart to the wave's finite speed.
- **Maximum principle.** A solution attains its largest and smallest values on the boundary of the space-time region (at the initial time or on the spatial edges), never strictly inside. Physically: with no internal sources, you cannot get hotter than your hottest input. This forbids spontaneous hot spots and underlies uniqueness.

> **Verification that $G$ solves the heat equation** (one dimension). Let $G=(4\pi\kappa t)^{-1/2}e^{-x^2/4\kappa t}$.
> Compute $G_t$ and $G_{xx}$ directly. Writing $a=4\kappa t$, $G=(\pi a)^{-1/2}e^{-x^2/a}$ with $a=4\kappa t$.
> $G_x = G\cdot(-2x/a)$, and $G_{xx}=G\big[(-2/a)+( -2x/a)^2\big]=G\big[-2/a + 4x^2/a^2\big]$.
> $G_t$: from $\ln G = -\tfrac12\ln(\pi a) - x^2/a$ and $da/dt=4\kappa$, $\tfrac{G_t}{G}= -\tfrac{1}{2a}\cdot4\kappa + \tfrac{x^2}{a^2}\cdot4\kappa = \kappa\big(-2/a + 4x^2/a^2\big)$.
> Thus $G_t = \kappa\,G\big(-2/a+4x^2/a^2\big)=\kappa\,G_{xx}$. $\blacksquare$

#### Worked example

A unit of heat deposited at the origin spreads as $u(x,t)=G(x,t)$. Its **width** grows like $\sqrt{t}$: the standard deviation of the Gaussian is $\sigma=\sqrt{2\kappa t}$. With $\kappa=1$, at $t=0.5$ the spread is $\sigma=1$; to double the spread to $\sigma=2$ requires $t=2$ — *four times* as long. Diffusion is slow: distance grows as the square root of time, never linearly. This $\sqrt{t}$ law is why a sugar cube takes minutes to sweeten still coffee but seconds when you stir.

Concretely, with $\kappa=1$: at $t=1$ the peak height is $G(0,1)=1/\sqrt{4\pi}\approx0.282$ and the value one unit away is $G(1,1)=0.282\,e^{-1/4}\approx0.220$. At $t=4$ the peak has dropped to $1/\sqrt{16\pi}\approx0.141$ — half as tall, twice as wide — while the *total* heat $\int G\,dx=1$ is unchanged. Heat is neither created nor destroyed; it only redistributes, the peak falling exactly as fast as the tails rise.

#### Where the Gaussian kernel comes from

The kernel $G$ is not pulled from thin air; it is forced by **scaling**. The heat equation is invariant under the rescaling $x\to\lambda x$, $t\to\lambda^2 t$ (because $u_t$ carries one $t$ and $u_{xx}$ carries two $x$'s, matching the parabolic discriminant of s0). So solutions starting from a point source must depend on $x$ and $t$ only through the dimensionless combination $\eta=x/\sqrt{t}$.

*Derivation of the profile (gap-free sketch).*
1. Seek $u=t^{-1/2}F(\eta)$ with $\eta=x/\sqrt{4\kappa t}$ (the $t^{-1/2}$ prefactor keeps the total heat $\int u\,dx$ constant in time, as a point source demands).
2. Substitute into $u_t=\kappa u_{xx}$ and use the chain rule. After simplification the PDE becomes the ODE $F'' + 2\eta F' + 2F = 0$, which is $\big(F' + 2\eta F\big)' = 0$.
3. Integrate once: $F'+2\eta F = $ const $=0$ (the constant is zero so $F$ decays both ways). This is separable: $F'/F = -2\eta$, giving $\ln F = -\eta^2 + $ const, so $F = C e^{-\eta^2}$.
4. Restore variables: $u = C\,t^{-1/2}e^{-x^2/4\kappa t}$. Fixing $\int_{-\infty}^\infty u\,dx = 1$ with the Gaussian integral $\int e^{-x^2/4\kappa t}dx=\sqrt{4\pi\kappa t}$ gives $C=1/\sqrt{4\pi\kappa}$, reproducing $G$ from above. $\blacksquare$

This is the same self-similar reasoning that explains why dye blobs, smoke, and rumors all spread with a bell-shaped profile widening as $\sqrt{t}$.

#### Pitfalls

- Running the heat equation *backward* ($t<0$) is wildly unstable — tiny errors blow up. You cannot reconstruct a past temperature precisely. Irreversibility is mathematical, not just physical.

<a id="s4"></a>
### The Laplace and Poisson equations; harmonic functions; the mean-value property

#### What & why

Set the time derivative to zero in the heat or wave equation and you get the **steady state**: nothing changes, the field has settled. What remains is

$$
\nabla^2 u = 0 \quad(\textbf{Laplace}), \qquad \nabla^2 u = f \quad(\textbf{Poisson}),
$$

where $f$ is a given source density. Laplace's equation governs electrostatic potential in charge-free space, steady temperature, ideal fluid flow, and gravity in empty regions; Poisson's adds sources (charges, masses). A solution of Laplace's equation is called a **harmonic function**.

#### The mean-value property

> **Theorem (mean-value).** If $u$ is harmonic in a region, then its value at any point equals its average over any circle (2D) or sphere (3D) centered there and lying in the region:
> $$
> u(\mathbf{x}_0)=\frac{1}{2\pi R}\oint_{|\mathbf{x}-\mathbf{x}_0|=R} u\,ds \quad(\text{2D}).
> $$

*Derivation in 2D, gap-free.*
1. Define the spherical average $M(R)=\dfrac{1}{2\pi}\displaystyle\int_0^{2\pi} u(\mathbf{x}_0 + R\hat{n}(\theta))\,d\theta$, where $\hat n(\theta)=(\cos\theta,\sin\theta)$. As $R\to0$, $M(R)\to u(\mathbf{x}_0)$ by continuity.
2. Differentiate under the integral (allowed since $u$ is smooth): $M'(R)=\dfrac{1}{2\pi}\int_0^{2\pi}\nabla u\cdot\hat n\,d\theta$. The integrand is the outward normal derivative $\partial u/\partial r$.
3. Multiply by $R$ to get the flux: $2\pi R\,M'(R)=\displaystyle\oint_{|\mathbf{x}-\mathbf{x}_0|=R}\frac{\partial u}{\partial r}\,ds = \iint_{\text{disk}}\nabla^2 u\,dA$ by the **divergence theorem** ($\oint\nabla u\cdot\hat n\,ds = \iint\nabla\cdot\nabla u\,dA = \iint\nabla^2u\,dA$).
4. Since $u$ is harmonic, $\nabla^2 u=0$, so the right side is $0$. Hence $M'(R)=0$ for all $R$: $M$ is **constant**.
5. A constant function equals its limit, $M(R)=M(0^+)=u(\mathbf{x}_0)$. That is the mean-value property. $\blacksquare$

#### Consequence: the maximum principle and uniqueness

> **Maximum principle.** A non-constant harmonic function attains its maximum and minimum only on the boundary.
>
> *Reason.* If $u$ had an interior maximum at $\mathbf{x}_0$, the average over a small circle would be $\le u(\mathbf{x}_0)$ with strict inequality somewhere unless $u$ is constant on the circle; but the mean-value property forces the average to *equal* $u(\mathbf{x}_0)$. The only escape is $u$ constant on every small circle, hence constant. $\blacksquare$

> **Uniqueness of the Dirichlet problem.** Laplace's (or Poisson's) equation with prescribed boundary values has at most one solution.
>
> *Reason.* If $u_1,u_2$ both solve it with the same data, $w=u_1-u_2$ is harmonic with $w=0$ on the boundary. By the maximum principle its max and min are both $0$, so $w\equiv0$ and $u_1=u_2$. $\blacksquare$

#### Worked example

Is $u(x,y)=x^2-y^2$ harmonic? $u_{xx}=2$, $u_{yy}=-2$, sum $=0$: yes. Check the mean-value property at the origin on the unit circle: on $x=\cos\theta,y=\sin\theta$, $u=\cos^2\theta-\sin^2\theta=\cos2\theta$, whose average over $[0,2\pi]$ is $0=u(0,0)$. Consistent.

#### A Poisson worked example

Solve $\nabla^2 u = -6$ (a uniform source) on the disk $r\le 1$ with $u=0$ on the rim, seeking a radially symmetric solution $u(r)$.
1. The radial Laplacian in 2D is $\nabla^2u = u_{rr}+\frac1r u_r = \frac1r(r u_r)_r$. Set $\frac1r(ru_r)_r=-6$.
2. Multiply by $r$ and integrate: $(ru_r)_r=-6r\Rightarrow ru_r=-3r^2 + C_1\Rightarrow u_r=-3r + C_1/r$.
3. Finiteness at $r=0$ forces $C_1=0$ (else $u_r$ blows up). Integrate: $u=-\tfrac32 r^2 + C_2$.
4. Boundary $u(1)=0$: $-\tfrac32 + C_2=0\Rightarrow C_2=\tfrac32$. So $u(r)=\tfrac32(1-r^2)$.
Check: $u_{rr}=-3$, $\frac1r u_r = \frac1r(-3r)=-3$, sum $-6$. Correct. The solution is a paraboloid — the steady temperature of a disk heated uniformly throughout with its edge held cold, or the deflection of a pressurized circular membrane.

#### Harmonic functions and analytic functions (a bridge)

In 2D there is a beautiful link to complex analysis: the real and imaginary parts of any analytic function are harmonic. Take $f(z)=z^2=(x+iy)^2=(x^2-y^2)+i(2xy)$. Its real part $x^2-y^2$ is the harmonic function above; its imaginary part $2xy$ is also harmonic ($u_{xx}=0,u_{yy}=0$). The two are **harmonic conjugates**, tied by the Cauchy–Riemann equations. This is why complex analysis is the natural tool for 2D electrostatics and ideal fluid flow.

#### Pitfall

- Poisson's equation is *not* governed by the maximum principle in the same way — sources create interior extrema. But uniqueness still holds because the *difference* of two Poisson solutions is harmonic.

## Part C · The master method: separation of variables

<a id="s5"></a>
### Separation of variables — the general method

#### What & why

Almost every solvable boundary-value problem in physics yields to one idea: guess that the solution is a *product* of functions each depending on a single variable, $u(x,t)=X(x)\,T(t)$. Plugging in collapses one PDE into several ODEs. The catch — that a single product rarely fits the data — is cured by superposition (s0): sum many products into a series.

#### The method, step by step (template)

Take the heat equation $u_t=\kappa u_{xx}$ on $0\le x\le L$ with $u(0,t)=u(L,t)=0$ (ends held at zero) and $u(x,0)=f(x)$.

1. **Assume a product.** Try $u(x,t)=X(x)T(t)$, neither factor identically zero.
2. **Substitute.** $u_t=X T'$, $u_{xx}=X''T$. The PDE becomes $X T' = \kappa X'' T$.
3. **Separate.** Divide by $\kappa X T$ (legal wherever $XT\neq0$):
$$
\frac{T'}{\kappa T} = \frac{X''}{X}.
$$
4. **The separation argument (the crux).** The left side depends only on $t$; the right side only on $x$. Two functions of *independent* variables can be equal for all $x,t$ only if both equal the *same constant*. (Reason: fix $t$ and vary $x$ — the left side cannot change, so the right side is forced constant; symmetrically the left side is constant.) Call the constant $-\lambda$ (the sign chosen for convenience):
$$
X'' = -\lambda X, \qquad T' = -\lambda\kappa\,T.
$$
5. **Apply boundary conditions to the spatial ODE.** $u(0,t)=X(0)T(t)=0$ for all $t$ forces $X(0)=0$ (else $T\equiv0$). Likewise $X(L)=0$. This is a **boundary-value problem** for $X$, an eigenvalue problem (s6).
6. **Solve the eigenvalue problem.** $X''=-\lambda X$ with $X(0)=X(L)=0$ has nonzero solutions only for $\lambda_n=(n\pi/L)^2$, $n=1,2,\dots$, namely $X_n=\sin(n\pi x/L)$. (Negative or zero $\lambda$ give only $X\equiv0$ once the boundary conditions are imposed — verified in s8.)
7. **Solve the time ODE** for each: $T_n' = -\lambda_n\kappa T_n\Rightarrow T_n(t)=e^{-\lambda_n\kappa t}$.
8. **Superpose.** Each product $X_nT_n$ solves the PDE and the boundary conditions; by superposition so does
$$
u(x,t)=\sum_{n=1}^{\infty} b_n \sin\!\frac{n\pi x}{L}\,e^{-\kappa(n\pi/L)^2 t}.
$$
9. **Fit the initial data** by choosing the $b_n$ so that $\sum b_n\sin(n\pi x/L)=f(x)$ — a Fourier sine series (s8).

#### Why the constant sign matters (intuition)

We chose $-\lambda$ so that decaying time behavior $e^{-\lambda\kappa t}$ corresponds to $\lambda>0$, which is exactly the sign the boundary conditions select. Diffusion *must* decay; the math agrees only for that sign. This consistency is the Sturm–Liouville theory of s6.

#### Handling non-homogeneous boundary conditions (the steady-state trick)

Separation needs *homogeneous* boundary conditions (zeros) to produce an eigenvalue problem; data like $u(0,t)=A$, $u(L,t)=B$ would couple the modes. The cure: split off a **steady state**. Suppose the ends are held at $A$ and $B$ forever. Write $u(x,t)=v(x,t)+w(x)$, where:
1. $w(x)$ is the *equilibrium* solving $w''=0$ with $w(0)=A,w(L)=B$, namely the straight line $w(x)=A+(B-A)x/L$. (Steady states satisfy the time-independent equation.)
2. Then $v=u-w$ satisfies the *same* heat equation (since $w_t=0$ and $w_{xx}=0$, subtracting changes nothing) but now with *homogeneous* ends $v(0,t)=v(L,t)=0$.
3. Solve $v$ by the sine series above, with initial data $f(x)-w(x)$. Add $w$ back at the end.

Physically: the rod relaxes to the linear temperature profile $w$, and $v$ is the transient that dies away. This reduce-to-homogeneous move is used constantly.

#### Pitfalls

- The product guess is not the *general* solution; it is a *family* whose sums are general. Never stop at one term.
- Separation works only when the geometry and operator align (rectangles in Cartesian, disks in polar, etc.). The right coordinate system is half the battle (s10, s11).
- You cannot separate an *inhomogeneous* PDE or boundary condition directly; first remove the inhomogeneity (steady-state subtraction above, or eigenfunction expansion of the source).

<a id="s6"></a>
### Sturm–Liouville theory and eigenfunction expansions

#### What & why

Separation of variables always produces a spatial eigenvalue problem. **Sturm–Liouville (SL) theory** is the unifying statement that *all* such problems have real eigenvalues and a complete, orthogonal set of eigenfunctions — guaranteeing that step 9 above (expanding the data) always works. It is the rigorous backbone behind Fourier, Legendre, and Bessel expansions alike.

#### The Sturm–Liouville form

> **Definition.** A **regular Sturm–Liouville problem** on $[a,b]$ is
> $$
> \frac{d}{dx}\!\left[p(x)\,\frac{dy}{dx}\right] + \big[q(x) + \lambda\,w(x)\big]\,y = 0,
> $$
> with $p>0$, $w>0$ continuous, plus homogeneous boundary conditions at $a$ and $b$ (e.g. $y=0$, or $y'=0$, or a mix). $\lambda$ is the **eigenvalue**; nonzero $y$ are **eigenfunctions**; $w$ is the **weight**.

Define the **inner product** $\langle f,g\rangle = \displaystyle\int_a^b f(x)g(x)w(x)\,dx$. Two functions are **orthogonal** if $\langle f,g\rangle=0$.

#### Orthogonality of eigenfunctions (gap-free proof)

> **Theorem.** Eigenfunctions $y_m,y_n$ for distinct eigenvalues $\lambda_m\neq\lambda_n$ are orthogonal with weight $w$.

*Proof.*
1. Write the operator $\mathcal{L}y=(py')'+qy$, so the equation is $\mathcal{L}y_n=-\lambda_n w\,y_n$ (and likewise for $m$).
2. Form $y_m\mathcal{L}y_n - y_n\mathcal{L}y_m$. The $q$-terms cancel, leaving $y_m(py_n')' - y_n(py_m')'$.
3. **Lagrange's identity:** this equals $\dfrac{d}{dx}\big[p(y_m y_n' - y_n y_m')\big]$. *Check by product rule:* expanding the derivative gives $p'(y_my_n'-y_ny_m') + p(y_m'y_n'+y_my_n'' - y_n'y_m'-y_ny_m'')$; the $y_m'y_n'$ terms cancel and the rest regroups to $y_m(py_n')'-y_n(py_m')'$. Confirmed.
4. Integrate over $[a,b]$. The right side is $\big[p(y_my_n'-y_ny_m')\big]_a^b$, which **vanishes** because the homogeneous boundary conditions make the bracket zero at both ends (e.g. if $y=0$ there, the bracket is $0$; if $y'=0$, likewise).
5. The left side, using $\mathcal{L}y_n=-\lambda_n w y_n$, equals $\int_a^b\big[y_m(-\lambda_n w y_n) - y_n(-\lambda_m w y_m)\big]dx = (\lambda_m-\lambda_n)\int_a^b y_m y_n w\,dx$.
6. So $(\lambda_m-\lambda_n)\langle y_m,y_n\rangle = 0$. Since $\lambda_m\neq\lambda_n$, we conclude $\langle y_m,y_n\rangle=0$. $\blacksquare$

#### Reality of the eigenvalues (proof)

> **Theorem.** Every eigenvalue of a regular SL problem is real.

*Proof.*
1. Suppose $\lambda$ is an eigenvalue with eigenfunction $y$, possibly complex. Take the SL equation $\mathcal{L}y=-\lambda w y$ and its complex conjugate $\mathcal{L}\bar y = -\bar\lambda w\bar y$ (the coefficients $p,q,w$ are real, so $\mathcal{L}$ is unchanged under conjugation).
2. Form $\bar y\,\mathcal{L}y - y\,\mathcal{L}\bar y$. By Lagrange's identity (proved above) this is a total derivative whose integral over $[a,b]$ vanishes by the boundary conditions.
3. The same integral equals $(\bar\lambda-\lambda)\int_a^b |y|^2 w\,dx$ (substituting the eigen-relations and noting $y\bar y=|y|^2$).
4. Since $w>0$ and $y\not\equiv0$, the integral $\int|y|^2 w\,dx>0$. Therefore $\bar\lambda-\lambda=0$, i.e. $\lambda$ is real. $\blacksquare$

This is the PDE-level reason that physical observables — energies, frequencies — come out real.

#### The full SL theorem (stated)

> For a regular SL problem: (i) the eigenvalues are **real** and form an increasing sequence $\lambda_1<\lambda_2<\cdots\to\infty$; (ii) the eigenfunctions $\{y_n\}$ are orthogonal with weight $w$ and can be normalized to $\langle y_n,y_n\rangle=1$; (iii) they are **complete**: any reasonable function $f$ on $[a,b]$ expands as $f=\sum_n c_n y_n$ converging in the mean-square sense.

#### Computing the coefficients

Given completeness, write $f=\sum_n c_n y_n$. Take $\langle\,\cdot\,,y_m\rangle$ of both sides and use orthonormality $\langle y_n,y_m\rangle=\delta_{nm}$:
$$
\langle f, y_m\rangle = \sum_n c_n\langle y_n,y_m\rangle = c_m, \qquad\text{so}\qquad c_m=\int_a^b f(x)\,y_m(x)\,w(x)\,dx.
$$
This single formula generates *every* expansion coefficient in the rest of the guide.

#### Worked example

The Fourier sine basis: $p=1,q=0,w=1$ on $[0,L]$, $y(0)=y(L)=0$. Eigenfunctions $y_n=\sin(n\pi x/L)$, eigenvalues $\lambda_n=(n\pi/L)^2$. Check orthogonality directly: $\int_0^L\sin\frac{m\pi x}{L}\sin\frac{n\pi x}{L}dx = \tfrac12\int_0^L[\cos\frac{(m-n)\pi x}{L}-\cos\frac{(m+n)\pi x}{L}]dx = 0$ for $m\neq n$ (both cosines integrate to zero over the interval), and $=L/2$ for $m=n$. So $\langle y_n,y_n\rangle=L/2$ and $c_n=\frac{2}{L}\int_0^L f\sin\frac{n\pi x}{L}dx$. (See the Fourier guide [`fourier-transforms.md`](fourier-transforms.md) for the convergence theory.)

#### Why the eigenvalues are positive (the Rayleigh quotient)

For the basic problem $-y''=\lambda y$ on $[0,L]$ with $y(0)=y(L)=0$, we can see $\lambda>0$ without solving. Multiply by $y$ and integrate:
$$
\lambda\int_0^L y^2\,dx = -\int_0^L y\,y''\,dx = -[yy']_0^L + \int_0^L (y')^2\,dx = \int_0^L (y')^2\,dx,
$$
where the boundary term vanishes because $y=0$ at both ends (integration by parts, s2's tool). The right side is $\ge0$, and it is $>0$ unless $y'\equiv0$, i.e. unless $y$ is constant — which the boundary conditions force to be zero. So $\lambda = \dfrac{\int (y')^2}{\int y^2} > 0$ for any genuine eigenfunction. This ratio is the **Rayleigh quotient**; it shows mechanically why the heat equation can only decay and the box's ground-state energy is strictly positive. The smallest eigenvalue is the *minimum* of this quotient over all admissible functions — a variational characterization linking back to the calculus of variations ([`calculus-of-variations.md`](calculus-of-variations.md)).

#### Pitfall

- Orthogonality requires the *correct weight* $w$. For Legendre $w=1$, for Bessel $w=x$. Forgetting the weight gives wrong coefficients.

## Part D · Worked boundary-value problems

<a id="s7"></a>
### The vibrating string: normal modes from separation of variables

#### What & why

A guitar string fixed at both ends, length $L$, displacement $u(x,t)$. We first derive its equation, then find the **normal modes** — the pure tones — by separation.

#### Deriving the wave equation for the string

1. Consider a small piece $[x,x+\Delta x]$ of a string with tension $T$ (constant) and linear mass density $\rho$. Assume small slopes so the string stays nearly horizontal.
2. The vertical force is the difference of the vertical tension components at the two ends: $T\sin\theta(x+\Delta x)-T\sin\theta(x)$. For small angles $\sin\theta\approx\tan\theta=u_x$, so the net vertical force is $T[u_x(x+\Delta x)-u_x(x)]\approx T\,u_{xx}\,\Delta x$.
3. Newton's second law: mass $\times$ acceleration $=$ force: $(\rho\Delta x)u_{tt}=T u_{xx}\Delta x$. Cancel $\Delta x$:
$$
u_{tt}=c^2 u_{xx},\qquad c^2=T/\rho. \qquad\blacksquare
$$
The wave speed rises with tension and falls with mass — tighten a string and the pitch goes up, exactly as observed.

#### Separation and the modes

Boundary conditions $u(0,t)=u(L,t)=0$ (fixed ends), initial shape $u(x,0)=\phi(x)$ and velocity $u_t(x,0)=\psi(x)$.

1. Put $u=X(x)T(t)$. Then $XT''=c^2X''T$, divide by $c^2XT$: $\dfrac{T''}{c^2T}=\dfrac{X''}{X}=-\lambda$.
2. Spatial problem $X''=-\lambda X$, $X(0)=X(L)=0$. As in s8, only $\lambda_n=(n\pi/L)^2$ give nonzero $X_n=\sin(n\pi x/L)$.
3. Temporal: $T''=-c^2\lambda_n T$, an oscillator, with solution $T_n=a_n\cos\omega_n t + b_n\sin\omega_n t$, $\omega_n=c\,n\pi/L$.
4. Superpose:
$$
u(x,t)=\sum_{n=1}^\infty \sin\frac{n\pi x}{L}\Big(a_n\cos\omega_n t + b_n\sin\omega_n t\Big).
$$
5. Fit data: $a_n=\dfrac2L\int_0^L\phi\sin\frac{n\pi x}{L}dx$ (from $u(x,0)=\phi$), and $b_n\omega_n=\dfrac2L\int_0^L\psi\sin\frac{n\pi x}{L}dx$ (from $u_t(x,0)=\psi$), both by the SL coefficient formula (s6).

#### Interpretation and worked example

Each term is a **normal mode**: a standing wave with fixed shape $\sin(n\pi x/L)$ oscillating at frequency $\omega_n=c n\pi/L$. The lowest, $n=1$, is the **fundamental**; the rest are **harmonics** at integer multiples — this integer ratio is *why* a vibrating string sounds musical.

Example: a string plucked into a triangle peaking at the center, $L=1$, released from rest ($\psi=0$). Then $b_n=0$ and $a_n = \frac{8}{n^2\pi^2}\sin(n\pi/2)$, which is $0$ for even $n$ and alternates $\pm$ for odd $n$. So $a_1=8/\pi^2$, $a_3=-8/(9\pi^2)$, .... The triangle is built from odd harmonics with rapidly shrinking amplitudes — the fundamental dominates, giving the perceived pitch.

#### Energy in each mode (orthogonality at work)

Because the modes are orthogonal (s6), the string's total energy splits cleanly into a sum over modes with *no cross terms*. The energy in mode $n$ is proportional to $\omega_n^2(a_n^2+b_n^2)$ — each harmonic carries its own energy, independent of the others. This is why you can excite one harmonic (touch the string at its midpoint to kill even modes) without feeding the rest: the modes are dynamically decoupled, exactly as orthogonal SL eigenfunctions must be. The same fact, in quantum mechanics, becomes "energy eigenstates evolve independently" (s13).

#### Pitfall

- The fixed-end condition selects *only* $\sin$, not $\cos$. Different boundary conditions (free ends, $u_x=0$) would select cosines and shift the spectrum.

<a id="s8"></a>
### The heat equation on an interval: the Fourier-series solution

#### What & why

We finish the template of s5 rigorously: heat in a rod $0\le x\le L$, ends at zero temperature, initial profile $f(x)$. The point here is to *prove* which eigenvalues survive and to compute a numeric example.

#### Solving the eigenvalue problem completely

Spatial problem: $X''=-\lambda X$, $X(0)=X(L)=0$. We rule out the wrong signs.

1. **Case $\lambda<0$**, write $\lambda=-\mu^2$. General solution $X=Ae^{\mu x}+Be^{-\mu x}$. $X(0)=0\Rightarrow A+B=0$; $X(L)=0\Rightarrow Ae^{\mu L}+Be^{-\mu L}=0$. Substituting $B=-A$: $A(e^{\mu L}-e^{-\mu L})=0$. Since $\mu\neq0$, $e^{\mu L}-e^{-\mu L}=2\sinh\mu L\neq0$, forcing $A=0$, hence $X\equiv0$. No eigenvalue.
2. **Case $\lambda=0$.** $X''=0\Rightarrow X=Ax+B$. $X(0)=0\Rightarrow B=0$; $X(L)=0\Rightarrow AL=0\Rightarrow A=0$. Only $X\equiv0$.
3. **Case $\lambda>0$**, write $\lambda=\mu^2$. $X=A\cos\mu x+B\sin\mu x$. $X(0)=0\Rightarrow A=0$. $X(L)=0\Rightarrow B\sin\mu L=0$. Nonzero $B$ needs $\sin\mu L=0$, i.e. $\mu L=n\pi$, $n=1,2,\dots$. So $\lambda_n=(n\pi/L)^2$, $X_n=\sin(n\pi x/L)$. $\blacksquare$

Thus only positive eigenvalues survive — consistent with the decaying time factor $e^{-\kappa\lambda_n t}$ demanded by diffusion.

#### Assembling the solution

$$
u(x,t)=\sum_{n=1}^\infty b_n\sin\frac{n\pi x}{L}\,e^{-\kappa(n\pi/L)^2 t},\qquad b_n=\frac2L\int_0^L f(x)\sin\frac{n\pi x}{L}\,dx.
$$
The coefficient formula is the SL result (s6) with weight $1$ and norm $L/2$.

#### Worked example with numbers

Rod of length $L=\pi$, $\kappa=1$, initial uniform temperature $f(x)=100$ (a hot rod plunged into ice baths at both ends). Then
$$
b_n=\frac{2}{\pi}\int_0^\pi 100\sin(nx)\,dx = \frac{200}{\pi}\cdot\frac{1-\cos n\pi}{n} = \frac{200}{\pi}\cdot\frac{1-(-1)^n}{n},
$$
which is $\dfrac{400}{n\pi}$ for odd $n$ and $0$ for even $n$. So
$$
u(x,t)=\frac{400}{\pi}\sum_{n\ \text{odd}}\frac{1}{n}\sin(nx)\,e^{-n^2 t}.
$$
At $t=0$ this is the Fourier sine series of the constant $100$ (it overshoots near the ends — the Gibbs phenomenon, see [`fourier-transforms.md`](fourier-transforms.md)). For $t>0$, the $e^{-n^2 t}$ factors crush the high harmonics fast: by $t=1$ the $n=3$ term is down by $e^{-8}\approx3\times10^{-4}$ relative to $n=1$. The rod's temperature collapses onto the smooth fundamental $\frac{400}{\pi}\sin x\,e^{-t}$ almost immediately — the smoothing property in action.

#### Pitfall

- The fundamental decays slowest, so the *long-time* temperature is essentially the single mode $\propto\sin(\pi x/L)e^{-\kappa(\pi/L)^2 t}$. The decay rate $\kappa(\pi/L)^2$ shows long rods cool far more slowly (quadratically in $L$).

<a id="s9"></a>
### Laplace's equation in a rectangle (worked in full)

#### What & why

Steady temperature (or electrostatic potential) on a rectangular plate $0\le x\le a$, $0\le y\le b$, with the value prescribed on the boundary. This is the model elliptic boundary-value problem, and separation handles it once we respect that there is no "time."

#### The problem and the trick of one inhomogeneous side

Solve $\nabla^2 u = u_{xx}+u_{yy}=0$ on the rectangle with
$$
u(0,y)=0,\quad u(a,y)=0,\quad u(x,0)=0,\quad u(x,b)=g(x).
$$
(Three sides grounded; the top edge carries the data $g$. A general boundary is the sum of four such problems by superposition.)

#### Full separation

1. $u=X(x)Y(y)$ gives $X''Y+XY''=0$, so $\dfrac{X''}{X}=-\dfrac{Y''}{Y}=-\lambda$ (separation constant).
2. **Choose which factor carries the eigenvalue problem by the homogeneous directions.** The conditions $u(0,y)=u(a,y)=0$ give $X(0)=X(a)=0$ — a complete SL problem in $x$. So we put $X''=-\lambda X$. By s8, $\lambda_n=(n\pi/a)^2$, $X_n=\sin(n\pi x/a)$.
3. The $y$-equation is then $Y''=\lambda_n Y$ (note the *opposite* sign — no oscillation, but exponential growth/decay), with general solution $Y_n=C_n\cosh(n\pi y/a)+D_n\sinh(n\pi y/a)$.
4. **Apply the homogeneous $y$-condition** $u(x,0)=0\Rightarrow Y_n(0)=0\Rightarrow C_n=0$. So $Y_n=D_n\sinh(n\pi y/a)$.
5. Superpose:
$$
u(x,y)=\sum_{n=1}^\infty D_n\sin\frac{n\pi x}{a}\,\sinh\frac{n\pi y}{a}.
$$
6. **Fit the inhomogeneous edge** $u(x,b)=g(x)$: $\sum_n D_n\sinh(n\pi b/a)\sin(n\pi x/a)=g(x)$. This is a Fourier sine series; by the SL coefficient formula,
$$
D_n\sinh\frac{n\pi b}{a}=\frac{2}{a}\int_0^a g(x)\sin\frac{n\pi x}{a}\,dx,
\quad\text{so}\quad
D_n=\frac{2}{a\,\sinh(n\pi b/a)}\int_0^a g(x)\sin\frac{n\pi x}{a}\,dx. \qquad\blacksquare
$$

#### Worked example with numbers

Square plate $a=b=\pi$, top edge held at $g(x)=\sin x$ (just the first harmonic), other edges at $0$. Then only $n=1$ survives: $D_1\sinh\pi = \frac{2}{\pi}\int_0^\pi\sin x\sin x\,dx = \frac{2}{\pi}\cdot\frac{\pi}{2}=1$, so $D_1=1/\sinh\pi$. The full solution is
$$
u(x,y)=\frac{\sin x\,\sinh y}{\sinh\pi}.
$$
Check: $u_{xx}=-u$ (from $\sin x$) and $u_{yy}=+u$ (from $\sinh y$), summing to $0$ — harmonic. At $y=\pi$: $u=\sin x\cdot\sinh\pi/\sinh\pi=\sin x=g(x)$. At $y=0$: $\sinh0=0$ so $u=0$. All conditions met.

#### A second worked example (general top edge)

Now hold the top edge at a constant $u(x,\pi)=100$ on the unit-style square $a=b=\pi$. The coefficient integral is the same one as the heated-rod example (s8): $\int_0^\pi 100\sin(nx)dx = \frac{200}{n}(1-(-1)^n)$, nonzero only for odd $n$. So
$$
D_n=\frac{2}{\pi\sinh(n\pi)}\cdot\frac{200(1-(-1)^n)}{2n},
$$
giving $D_n=\dfrac{400}{n\pi\sinh(n\pi)}$ for odd $n$. The solution
$$
u(x,y)=\frac{400}{\pi}\sum_{n\ \text{odd}}\frac{\sin(nx)\sinh(ny)}{n\,\sinh(n\pi)}
$$
equals $100$ along the top, $0$ on the other three sides, and is harmonic inside. Because $\sinh(n\pi)$ grows like $e^{n\pi}/2$, the $n=3$ coefficient is already about $e^{-2\pi}\approx2\times10^{-3}$ times the $n=1$ one *before* the spatial decay — the series converges extremely fast in the interior, a hallmark of elliptic smoothing.

#### Interpretation and pitfall

- The data on the top edge "diffuses" downward, decaying like $\sinh(n\pi y/a)/\sinh(n\pi b/a)$; high harmonics ($n$ large) decay fastest as you move away from the edge — Laplace's equation smooths boundary roughness into the interior, the elliptic analogue of heat smoothing.
- Pitfall: you *must* assign the eigenvalue problem to the homogeneous-boundary direction. Putting it on $y$ here would give the wrong basis and no way to fit the data.
- The corners where the top edge ($u=100$) meets a side ($u=0$) hold conflicting data; the solution is genuinely discontinuous there and the series shows Gibbs oscillations near the corners, harmless in the interior.

## Part E · Other coordinate systems and Green's functions

<a id="s10"></a>
### Spherical coordinates → the Legendre equation and spherical harmonics

#### What & why

Spheres are everywhere in physics: the potential of a charge, the orbitals of an atom. In **spherical coordinates** $(r,\theta,\varphi)$ — radius, polar angle, azimuth — the Laplacian becomes
$$
\nabla^2 u=\frac{1}{r^2}\partial_r\!\big(r^2\partial_r u\big)+\frac{1}{r^2\sin\theta}\partial_\theta\!\big(\sin\theta\,\partial_\theta u\big)+\frac{1}{r^2\sin^2\theta}\partial_{\varphi\varphi}u .
$$
Separating variables here produces the equations of the most important special functions.

#### Separation

1. Write $u=R(r)\,\Theta(\theta)\,\Phi(\varphi)$ and substitute into $\nabla^2u=0$; multiply by $r^2/(R\Theta\Phi)$.
2. The azimuthal part separates first: $\dfrac{\Phi''}{\Phi}=-m^2$ (constant), giving $\Phi=e^{\pm im\varphi}$. Periodicity $\Phi(\varphi+2\pi)=\Phi(\varphi)$ forces $m$ to be an integer.
3. The remaining radial-polar split introduces a second constant, conventionally $\ell(\ell+1)$. The **radial equation** is $\big(r^2R'\big)'=\ell(\ell+1)R$, an Euler equation solved by $R=r^\ell$ and $R=r^{-(\ell+1)}$.
4. The **polar equation**, after substituting $x=\cos\theta$ (so $dx=-\sin\theta\,d\theta$), becomes the **associated Legendre equation**
$$
\frac{d}{dx}\!\Big[(1-x^2)\frac{dP}{dx}\Big]+\Big[\ell(\ell+1)-\frac{m^2}{1-x^2}\Big]P=0 .
$$

#### The link to the Special Functions guide

This is a singular Sturm–Liouville problem ($p=1-x^2$ vanishing at $x=\pm1$). Demanding solutions that stay finite at the poles $x=\pm1$ forces $\ell$ to be a non-negative integer with $|m|\le\ell$; the solutions are the **associated Legendre functions** $P_\ell^m(x)$, and for $m=0$ the **Legendre polynomials** $P_\ell(x)$, orthogonal on $[-1,1]$ with weight $1$. The angular products $Y_\ell^m(\theta,\varphi)=P_\ell^m(\cos\theta)e^{im\varphi}$ are the **spherical harmonics**, a complete orthonormal basis on the sphere. *The construction of $P_\ell$ (Rodrigues' formula, the generating function, recurrence relations, and orthogonality) is developed in full in the companion guide* [`special-functions.md`](special-functions.md); *here we only show how the PDE produces them.*

#### Worked example

The exterior potential of a point charge is $u=q/(4\pi\varepsilon_0 r)$, the $\ell=0$, $R=r^{-1}$ radial solution — spherically symmetric, no angular dependence. A pure dipole field $\propto\cos\theta/r^2$ is the $\ell=1$, $m=0$ piece: $R=r^{-2}$, $P_1(\cos\theta)=\cos\theta$. These are the first two terms of the **multipole expansion**, which is exactly the spherical-harmonic series of an arbitrary charge distribution's potential.

#### The two-constant separation, made explicit

To see where $\ell(\ell+1)$ enters, take the *interior* problem $\nabla^2u=0$ with $u=R(r)Y(\theta,\varphi)$ and no azimuthal dependence ($m=0$ for brevity). Substituting and multiplying by $r^2/(RY)$:
$$
\frac{(r^2R')'}{R} = -\frac{1}{Y\sin\theta}\big(\sin\theta\,Y_\theta\big)_\theta .
$$
The left side depends only on $r$, the right only on $\theta$; by the separation argument (s5) both equal a constant. Calling it $\ell(\ell+1)$ (a choice that makes the angular equation have polynomial solutions) gives the radial Euler equation $r^2R''+2rR'-\ell(\ell+1)R=0$ with solutions $r^\ell$ and $r^{-\ell-1}$, and the Legendre equation for the angular factor. The constant's peculiar form $\ell(\ell+1)$ is dictated entirely by demanding regularity at the poles.

#### Pitfall

- The two separation constants are linked: once you fix $m$ (azimuthal), the allowed $\ell$ satisfy $\ell\ge|m|$. They are not independent.

<a id="s11"></a>
### Cylindrical coordinates → the Bessel equation

#### What & why

Drums, waveguides, optical fibers, heat in a wire — all have cylindrical symmetry. In **cylindrical coordinates** $(\rho,\varphi,z)$ the Laplacian is
$$
\nabla^2 u=\frac1\rho\partial_\rho(\rho\,\partial_\rho u)+\frac1{\rho^2}\partial_{\varphi\varphi}u+\partial_{zz}u .
$$

#### Separation to Bessel's equation

1. Set $u=R(\rho)\Phi(\varphi)Z(z)$. The $\varphi$-part gives $\Phi=e^{\pm in\varphi}$ with integer $n$ (periodicity), and the $z$-part gives $Z''=k^2 Z$, so $Z=e^{\pm kz}$ (or oscillatory if the sign is chosen oppositely, depending on the problem).
2. The radial equation, with separation constants $n$ and $k$, becomes
$$
\rho^2 R'' + \rho R' + (k^2\rho^2 - n^2)R = 0 .
$$
3. Substituting $s=k\rho$ turns this into **Bessel's equation of order $n$:**
$$
s^2\frac{d^2R}{ds^2}+s\frac{dR}{ds}+(s^2-n^2)R=0 .
$$

#### The link to the Special Functions guide

The solutions are the **Bessel functions** $J_n(s)$ (regular at the origin) and $Y_n(s)$ (singular there, discarded when the axis is included). On a disk of radius $a$ with $R(a)=0$ they form a singular Sturm–Liouville system: the allowed $k$ are $k=\alpha_{n,j}/a$, where $\alpha_{n,j}$ is the $j$-th zero of $J_n$, and the $J_n(\alpha_{n,j}\rho/a)$ are orthogonal on $[0,a]$ with weight $\rho$. *Their series definition, recurrences, asymptotics, and the zeros are treated in full in* [`special-functions.md`](special-functions.md); *we only derive the equation here.*

#### Worked example

A circular drumhead of radius $a$ fixed at the rim, vibrating axisymmetrically ($n=0$). Its modes are $J_0(\alpha_{0,j}\rho/a)\cos(\omega_j t)$ with frequencies $\omega_j = c\,\alpha_{0,j}/a$. The first zeros are $\alpha_{0,1}\approx2.405$, $\alpha_{0,2}\approx5.520$. The frequency ratio $\omega_2/\omega_1\approx5.520/2.405\approx2.295$ is *not* an integer — unlike the string (s7). This is precisely *why a drum sounds inharmonic and "thuddy"* rather than producing a clear musical pitch.

#### Heat on a disk (the Fourier–Bessel series)

The cooling of a circular plate, initial temperature $f(\rho)$ (radially symmetric), rim held at $0$, illustrates the full machinery. Separation $u=R(\rho)T(t)$ gives $T_j(t)=e^{-\kappa(\alpha_{0,j}/a)^2 t}$ and $R_j=J_0(\alpha_{0,j}\rho/a)$, so
$$
u(\rho,t)=\sum_{j=1}^\infty c_j\,J_0\!\Big(\frac{\alpha_{0,j}\rho}{a}\Big)\,e^{-\kappa(\alpha_{0,j}/a)^2 t}.
$$
The coefficients come from the SL formula (s6) with weight $w=\rho$:
$$
c_j=\frac{\displaystyle\int_0^a f(\rho)\,J_0(\alpha_{0,j}\rho/a)\,\rho\,d\rho}{\displaystyle\int_0^a J_0(\alpha_{0,j}\rho/a)^2\,\rho\,d\rho}.
$$
The weight $\rho$ is the Jacobian of polar area $dA=\rho\,d\rho\,d\varphi$ — the geometry itself supplies the SL weight. As with the rod (s8), the lowest mode $j=1$ decays slowest, so a hot disk relaxes toward the smooth profile $J_0(\alpha_{0,1}\rho/a)$ with $\alpha_{0,1}\approx2.405$.

#### Pitfall

- $Y_n$ blows up at $\rho=0$; keep it only for annular regions (e.g. a washer) that exclude the axis.

<a id="s12"></a>
### Green's functions for PDEs; the Green's function of the Laplacian

#### What & why

A **Green's function** $G$ is the response of a linear system to a unit point source — a single sharp "ping." Because any source is a superposition of point sources, knowing $G$ lets you solve the equation for *any* source by integration. This is the PDE incarnation of "impulse response → convolution" (see the Fourier guide, [`fourier-transforms.md`](fourier-transforms.md)).

#### Definition

For Poisson's equation $\nabla^2 u = -f$ (electrostatics convention, $f$ the source density), the Green's function solves
$$
\nabla^2 G(\mathbf{x},\mathbf{x}') = -\delta(\mathbf{x}-\mathbf{x}'),
$$
where $\delta$ is the **Dirac delta**: zero except at $\mathbf{x}=\mathbf{x}'$, with total integral $1$ (a unit point source). Then, by superposition, $u(\mathbf{x})=\int G(\mathbf{x},\mathbf{x}')f(\mathbf{x}')\,d^3x'$, *because* applying $\nabla^2$ pulls inside the integral and turns each $G$ into $-\delta$, reproducing $-f$.

#### Deriving the 3D Green's function (the Coulomb potential)

By symmetry the response to a source at the origin depends only on $r=|\mathbf{x}|$, so $G=G(r)$. Away from the origin the source is zero, so we solve $\nabla^2 G=0$ for $r>0$ and fix the strength by the point-source condition.

1. **Radial Laplacian.** For a function of $r$ alone, $\nabla^2 G = \dfrac{1}{r^2}\dfrac{d}{dr}\!\Big(r^2\dfrac{dG}{dr}\Big)$ (the $\theta,\varphi$ terms vanish). Setting this to $0$ for $r>0$: $\dfrac{d}{dr}(r^2G')=0$, so $r^2 G' = -A$ (constant), giving $G' = -A/r^2$ and
$$
G(r)=\frac{A}{r}+B.
$$
We take $B=0$ so $G\to0$ at infinity (the natural physical normalization).
2. **Fix $A$ by integrating the defining equation over a small ball** $B_\epsilon$ of radius $\epsilon$ around the origin:
$$
\int_{B_\epsilon}\nabla^2 G\,dV = -\int_{B_\epsilon}\delta\,dV = -1,
$$
the right side being the total source strength, $1$, by the delta's defining property.
3. **Convert the left side with the divergence theorem:** $\int_{B_\epsilon}\nabla^2 G\,dV = \int_{B_\epsilon}\nabla\cdot(\nabla G)\,dV = \oint_{\partial B_\epsilon}\nabla G\cdot\hat n\,dS = \oint \dfrac{dG}{dr}\,dS$.
4. **Evaluate the flux.** With $G=A/r$, $G'=-A/r^2$. On the sphere $r=\epsilon$ of area $4\pi\epsilon^2$, the integrand is constant: $\oint G'\,dS = (-A/\epsilon^2)(4\pi\epsilon^2) = -4\pi A$.
5. **Match:** $-4\pi A = -1$, so $A=\dfrac{1}{4\pi}$. Therefore
$$
\boxed{\,G(\mathbf{x},\mathbf{x}')=\frac{1}{4\pi\,|\mathbf{x}-\mathbf{x}'|}\,}
$$
the **Newtonian/Coulomb potential** of a unit point source. $\blacksquare$

#### Reconstructing the physics

With this $G$, the potential of a charge density $\rho/\varepsilon_0=f$ is $u(\mathbf{x})=\dfrac{1}{4\pi}\int\dfrac{f(\mathbf{x}')}{|\mathbf{x}-\mathbf{x}'|}d^3x'$ — exactly Coulomb's law summed over all source elements. The abstract Green's function *is* the familiar $1/r$ potential.

#### Worked check

For a single point charge $q$ at the origin, $f=q\,\delta(\mathbf{x})/\varepsilon_0$, the integral collapses (the delta picks out $\mathbf{x}'=0$) to $u=\dfrac{q}{4\pi\varepsilon_0 r}$ — the standard Coulomb potential. Consistent with s10's $\ell=0$ radial solution.

#### Boundary conditions and the method of images

The free-space $G=1/(4\pi r)$ ignores boundaries. For a region with a grounded wall ($u=0$ on it), add an **image source** to cancel the potential there. Classic case: a point charge at height $d$ above a grounded plane $z=0$. Place a fictitious *negative* charge at $z=-d$ (the mirror image). The Green's function becomes
$$
G(\mathbf{x},\mathbf{x}')=\frac{1}{4\pi}\left(\frac{1}{|\mathbf{x}-\mathbf{x}'|}-\frac{1}{|\mathbf{x}-\mathbf{x}'_{\text{img}}|}\right),
$$
which vanishes on $z=0$ by symmetry (the two distances are equal there), satisfying the boundary condition while keeping the correct singularity inside the region. This trick converts hard boundary-value problems into free-space sums.

#### Symmetry of the Green's function

> **Reciprocity.** $G(\mathbf{x},\mathbf{x}')=G(\mathbf{x}',\mathbf{x})$ — the response at $\mathbf{x}$ to a source at $\mathbf{x}'$ equals the response at $\mathbf{x}'$ to a source at $\mathbf{x}$.

This follows from Green's second identity applied to $G(\cdot,\mathbf{x}_1)$ and $G(\cdot,\mathbf{x}_2)$, the boundary terms vanishing under homogeneous conditions. Physically it is the statement that "you hear me exactly as well as I hear you" — a deep and useful symmetry, visible already in the free-space form where $1/|\mathbf{x}-\mathbf{x}'|$ is manifestly symmetric.

#### Pitfall

- The Green's function depends on dimension: in 2D the Laplacian's Green's function is $-\frac{1}{2\pi}\ln r$ (logarithmic, no decay at infinity), not $1/r$. Always rederive for the right dimension.

<a id="s13"></a>
### The Schrödinger equation as a PDE

#### What & why

Quantum mechanics is, mathematically, a PDE for a complex field $\psi(x,t)$, the **wavefunction**, whose modulus squared $|\psi|^2$ gives the probability density of finding the particle. The **time-dependent Schrödinger equation** in 1D is

$$
i\hbar\,\psi_t = -\frac{\hbar^2}{2m}\psi_{xx} + V(x)\psi,
$$

where $\hbar$ is the reduced Planck constant, $m$ the mass, and $V$ the potential energy. It is first order in time (like the heat equation) but with an $i$ — making solutions oscillate rather than decay.

#### Separation: the stationary states

1. Separate $\psi(x,t)=\phi(x)\,T(t)$. Substituting and dividing by $\phi T$:
$$
i\hbar\frac{T'}{T} = \frac{1}{\phi}\Big(-\frac{\hbar^2}{2m}\phi'' + V\phi\Big) = E,
$$
a constant (separation, s5), which has units of energy.
2. Time part: $i\hbar T'=ET\Rightarrow T(t)=e^{-iEt/\hbar}$ — a pure phase, $|T|=1$. The probability $|\psi|^2=|\phi|^2$ is time-independent: a **stationary state**.
3. Space part: the **time-independent Schrödinger equation**
$$
-\frac{\hbar^2}{2m}\phi'' + V(x)\phi = E\phi,
$$
an eigenvalue problem — energies $E$ are the eigenvalues. This is a Sturm–Liouville problem (s6), so $E$ is real and eigenfunctions are orthogonal.

#### Worked example 1: the particle in a box

Let $V=0$ on $0\le x\le L$ and $V=\infty$ outside (impenetrable walls), forcing $\phi(0)=\phi(L)=0$.
1. Inside, $-\frac{\hbar^2}{2m}\phi''=E\phi$, i.e. $\phi''=-k^2\phi$ with $k^2=2mE/\hbar^2$. This is the *same* eigenvalue problem as the string and the heated rod (s8).
2. By s8, $\phi_n=\sin(n\pi x/L)$, $k_n=n\pi/L$, $n=1,2,\dots$.
3. The energies follow from $E=\hbar^2k^2/2m$:
$$
E_n=\frac{\hbar^2}{2m}\Big(\frac{n\pi}{L}\Big)^2=\frac{n^2\pi^2\hbar^2}{2mL^2}.
$$
Energy is **quantized** — only discrete levels exist, scaling as $n^2$. The lowest, $E_1>0$, is the **zero-point energy**: the particle can never be perfectly at rest, a direct consequence of the boundary conditions (the same conditions that gave a guitar string its fundamental tone). Normalizing, $\int_0^L|\phi_n|^2dx=1$ gives $\phi_n=\sqrt{2/L}\sin(n\pi x/L)$.

Numbers: an electron ($m\approx9.1\times10^{-31}$ kg) in a box $L=1$ nm has $E_1=\frac{\pi^2\hbar^2}{2mL^2}\approx6\times10^{-20}$ J $\approx0.38$ eV — the right scale for atomic and molecular energies.

#### Worked example 2: the free particle

Let $V=0$ on the whole line, no walls. Then $\phi''=-k^2\phi$ has solutions $\phi=e^{\pm ikx}$ for *any* real $k$ — the spectrum is **continuous**, no quantization. The full solution
$$
\psi_k(x,t)=e^{i(kx-\omega t)},\qquad \omega=\frac{E}{\hbar}=\frac{\hbar k^2}{2m},
$$
is a traveling **plane wave** with momentum $p=\hbar k$. The relation $\omega=\hbar k^2/2m$ (not $\omega=ck$) means different wavelengths travel at different speeds — **dispersion** — so a localized wave packet (a superposition $\int A(k)\psi_k\,dk$, a Fourier integral; see [`fourier-transforms.md`](fourier-transforms.md)) spreads as it moves, the quantum analogue of diffusion.

#### The general solution as an eigenfunction expansion

The stationary states $\phi_n$ are the eigenfunctions of a Sturm–Liouville operator, hence orthonormal and complete (s6). So *any* initial wavefunction expands as $\psi(x,0)=\sum_n c_n\phi_n(x)$ with $c_n=\int\overline{\phi_n}\,\psi(x,0)\,dx$, and time evolution simply attaches each mode's phase:
$$
\psi(x,t)=\sum_n c_n\,\phi_n(x)\,e^{-iE_n t/\hbar}.
$$
This is identical in form to the heat-equation series (s8) — but with an *imaginary* exponent, so modes rotate in phase instead of decaying. The probabilities $|c_n|^2$ are the chances of measuring energy $E_n$, fixed in time because each $|e^{-iE_nt/\hbar}|=1$.

#### Worked superposition

In the box, prepare $\psi(x,0)=\frac{1}{\sqrt2}(\phi_1+\phi_2)$ (equal mix of ground and first excited states). Then
$$
\psi(x,t)=\frac1{\sqrt2}\big(\phi_1 e^{-iE_1t/\hbar}+\phi_2 e^{-iE_2t/\hbar}\big),
$$
and $|\psi|^2$ contains a cross term $\propto\cos\big((E_2-E_1)t/\hbar\big)\phi_1\phi_2$ — the probability density *sloshes* back and forth at the **Bohr frequency** $\omega=(E_2-E_1)/\hbar$. With the box energies $E_n\propto n^2$, this is $\omega=3E_1/\hbar$. Interference between stationary states is what makes a quantum system actually *do* anything in time.

#### Interpretation and pitfall

- Confinement (a box) gives discrete levels; freedom gives a continuum. The boundary conditions, not the equation alone, decide the spectrum — the central lesson of the whole guide.
- Pitfall: $\psi$ is complex and not directly observable; only $|\psi|^2$ and expectation values are physical. The phase $e^{-iEt/\hbar}$ is invisible in a single stationary state but crucial in superpositions, where it produces interference and time evolution.

#### The unity of the three equations, one last time

Notice how every method in this guide returned. The Schrödinger equation is first-order in time like the **heat equation** (s3) — but the factor $i$ turns real decay $e^{-\lambda t}$ into pure rotation $e^{-i\lambda t}$, so probability is conserved instead of dissipated. Its stationary states are a **Sturm–Liouville** problem (s6), giving real energies and orthogonal eigenfunctions. The box reuses the *exact* eigenproblem of the vibrating **string** (s7) and the cooling **rod** (s8). The free particle is solved by **Fourier** superposition of plane waves, with the dispersion $\omega\propto k^2$ making wave packets spread — diffusion in disguise. And in three dimensions with a central potential, separation in **spherical coordinates** (s10) produces the same Legendre and radial equations that gave electrostatic multipoles. The three classical equations and the single method of expanding in the right orthogonal basis are not separate topics; they are one idea wearing different clothes.

---

*This guide built the partial differential equations of physics from the ground up: the meaning and classification of a PDE, the method of characteristics, the wave equation with d'Alembert's traveling-wave solution, the heat equation derived from conservation and Fourier's law, and the Laplace/Poisson equations with the mean-value property and maximum principle. Separation of variables, grounded in Sturm–Liouville theory's orthogonal complete eigenfunctions, then solved the vibrating string, the cooling rod, and the rectangular plate; spherical and cylindrical geometries delivered the Legendre and Bessel equations that the Special Functions guide develops in full; Green's functions reproduced the Coulomb potential; and the Schrödinger equation revealed quantization as nothing more than a boundary-value problem. The single thread: the laws of fields and waves are linear PDEs, and superposition plus the right basis turns them into arithmetic.*
