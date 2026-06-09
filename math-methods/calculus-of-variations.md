**English** · [中文](calculus-of-variations.zh.md)

# Calculus of Variations, *the principle behind the laws of physics.*

*A self-contained first course in the calculus of variations — from the question "which curve makes a quantity smallest?" to the Euler–Lagrange equation, Hamilton's principle, Noether's theorem, and field theory. Every term is defined in words, every formula is motivated, and every derivation is a numbered, gap-free chain of reasons. Built on basic algebra and single-variable calculus; the bridges to mechanics and differential geometry are made explicit.*

[← Back to all guides](../README.md)

## Part A · The setting

<a id="s0"></a>
### Motivation: least action, the brachistochrone, geodesics

#### What this guide is about, in one breath

Ordinary calculus asks: of all the *numbers* $x$, which one makes a function $f(x)$ smallest? You answer by setting $f'(x)=0$. The calculus of variations asks a richer question: of all the *curves* (or functions) joining two points, which one makes some total quantity — a length, a time, an energy — smallest? The astonishing discovery of physics is that nature itself answers such a question: a huge swath of physical law can be written as "the actual path is the one that makes a certain integral stationary." This guide builds the mathematics that makes that statement precise and then shows it generating Newton's laws, conservation laws, and field equations.

#### Three motivating problems

- **The principle of least action.** A particle moving under gravity, a planet orbiting the sun, a ray of light bending through glass — each follows a path that makes a quantity called the **action** stationary (often a minimum). Instead of pushing the particle step by step with forces, we hand it the whole journey at once and ask which journey is "best." This is the deepest organizing idea in physics, and it is a variational problem.

- **The brachistochrone** (Greek: "shortest time"). Posed by Johann Bernoulli in 1696: a bead slides without friction down a wire from point $A$ to a lower point $B$ not directly below it. Among all possible wire shapes, which gets the bead from $A$ to $B$ in the *least time*? The straight line is not the answer; the answer is an arc of a **cycloid** (the curve traced by a point on a rolling wheel). We solve this fully in §s3.

- **Geodesics.** What is the shortest path between two points? On a flat plane it is a straight line; on a sphere it is a great-circle arc (why airplanes over the Pacific seem to swing north). A **geodesic** is the "straightest possible" curve on a surface, and finding it is again a problem of minimizing a total length. We treat this in §s6.

#### What these have in common

In every case the unknown is a **function** — the shape $y(x)$ of a curve — and the quantity to minimize is a **number computed from that whole function** by integrating along it: a time, a length, an energy. A rule that eats a function and returns a single number is called a **functional**. The calculus of variations is the calculus of functionals: it gives the analogue of "set the derivative to zero" for functionals, and that analogue is the **Euler–Lagrange equation** (§s2).

#### The whole guide on one line

> Functionals → first variation → Euler–Lagrange equation → worked curves → fields & constraints → geodesics → mechanics (Hamilton) → Noether → Hamiltonian form → classical fields

#### Common pitfalls

- "Stationary" is not the same as "minimum." Setting the first variation to zero finds *stationary* points; they may be minima, maxima, or saddle-like. We discuss this in §s2.
- The unknown is the *whole function at once*, not its value at one point. You cannot solve the brachistochrone by optimizing the bead's height at a single $x$; the curve's value at every point is coupled to its neighbors through the slope $y'$.

<a id="s1"></a>
### Functionals and the variation; the functional derivative

#### What & why

To imitate ordinary calculus we need three ingredients: a thing to optimize (here a functional), a notion of "moving a little" (here a *variation* of the function), and a notion of "rate of change" (here the *first variation*, the functional analogue of a derivative). This section defines all three carefully so the derivation in §s2 has no gaps.

#### Every term, defined from zero

- A **function** $y(x)$ takes a number $x$ and returns a number $y$. A **smooth** function is one that can be differentiated as many times as we need (here, at least twice continuously); we write $y\in C^2[a,b]$ for functions twice continuously differentiable on the closed interval $[a,b]$.
- A **functional** $J$ is a rule that takes an entire function $y$ as input and returns a single real number $J[y]$. We use square brackets $J[y]$ to stress that the input is a function, not a number. *Example:* the length of the graph of $y$ over $[a,b]$ is the functional $L[y]=\int_a^b\sqrt{1+y'(x)^2}\,dx$ (derived in §s3).

> **Definition — the standard functional**
>
> Throughout this guide the central object is
> $$
> J[y]=\int_a^b L\big(x,\,y(x),\,y'(x)\big)\,dx .
> $$
> Here $a<b$ are fixed numbers, $y$ ranges over smooth functions on $[a,b]$, and $L(x,y,y')$ — the **Lagrangian** (or **integrand**) — is a given smooth function of *three independent slots*: the position $x$, the value $y$, and the slope $y'$. To evaluate $J[y]$ you plug the curve's value and slope into $L$ at each $x$ and add up (integrate) along the interval.

A key subtlety: $L$ is treated as a function of three *independent* variables $x, y, y'$ when we differentiate it. The symbols $\partial L/\partial y$ and $\partial L/\partial y'$ mean "differentiate $L$ holding the other two slots fixed." Only *after* those partial derivatives are formed do we remember that, along an actual curve, $y$ and $y'$ are functions of $x$.

#### Admissible functions and fixed endpoints

We optimize over **admissible functions**: smooth functions on $[a,b]$ that pass through prescribed endpoints,
$$
y(a)=y_a,\qquad y(b)=y_b ,
$$
with $y_a,y_b$ given numbers. (The wire of the brachistochrone is pinned at $A$ and $B$.) This boundary condition is what makes the problem definite, and it is exactly what kills certain terms in the derivation below.

#### Varying the function

To probe whether a particular curve $y$ is optimal, we nudge it. Pick any smooth function $\eta(x)$ — the **variation direction** — that *vanishes at the endpoints*:
$$
\eta(a)=0,\qquad \eta(b)=0 .
$$
This last requirement guarantees the nudged curve still hits the same endpoints, so it stays admissible. Now form a one-parameter family of competitor curves
$$
y_\varepsilon(x)=y(x)+\varepsilon\,\eta(x),
$$
where $\varepsilon$ is a small real number. At $\varepsilon=0$ we recover $y$; as $\varepsilon$ grows we slide away in the direction $\eta$. The quantity $\delta y:=\varepsilon\eta$ is called the **variation of $y$** — the infinitesimal change in the *whole function*, the analogue of the small step $\Delta x$ in ordinary calculus.

#### The first variation: turning a functional problem into a calculus problem

Feed the family into $J$ and you get an ordinary function of the single number $\varepsilon$:
$$
\Phi(\varepsilon):=J[y+\varepsilon\eta]=\int_a^b L\big(x,\,y+\varepsilon\eta,\,y'+\varepsilon\eta'\big)\,dx .
$$
This is the master trick of the whole subject: by sliding along one direction $\eta$ we have collapsed an infinite-dimensional problem (optimize over all functions) into a one-dimensional one (optimize $\Phi$ over the number $\varepsilon$), which ordinary calculus handles.

> **Definition — first variation**
>
> The **first variation** of $J$ at $y$ in the direction $\eta$ is
> $$
> \delta J[y;\eta]:=\left.\frac{d}{d\varepsilon}\right|_{\varepsilon=0}J[y+\varepsilon\eta]=\Phi'(0).
> $$
> It is the directional derivative of the functional — how fast $J$ changes as we start moving the curve in the direction $\eta$.

> **Definition — stationary (extremal) function**
>
> A function $y$ is **stationary** for $J$ (and is called an **extremal**) if the first variation vanishes for *every* admissible direction:
> $$
> \delta J[y;\eta]=0\quad\text{for all smooth }\eta\text{ with }\eta(a)=\eta(b)=0 .
> $$
> This is the exact analogue of $f'(x)=0$: a genuine minimum or maximum must be stationary, because if $\Phi'(0)\neq0$ for some $\eta$ then moving a little along $+\eta$ or $-\eta$ would strictly decrease $J$, so $y$ could not be optimal.

#### The functional derivative

When we write the first variation in the form
$$
\delta J[y;\eta]=\int_a^b \frac{\delta J}{\delta y}(x)\,\eta(x)\,dx ,
$$
the function $\dfrac{\delta J}{\delta y}(x)$ multiplying $\eta$ is called the **functional derivative** of $J$. It is the continuous analogue of a gradient: where the gradient of an ordinary function is a *vector* of partial derivatives (one number per coordinate), the functional derivative is a *function* (one number per point $x$). Stationarity says this whole function is zero — and §s2 shows the functional derivative is precisely the left side of the Euler–Lagrange equation.

#### Worked example — the first variation of the length functional

Take $L=\sqrt{1+y'^2}$, so $J[y]=\int_a^b\sqrt{1+y'^2}\,dx$ (graph length).
1. Form $\Phi(\varepsilon)=\int_a^b\sqrt{1+(y'+\varepsilon\eta')^2}\,dx$. *Reason:* replace $y'$ by $y'+\varepsilon\eta'$ since $\frac{d}{dx}(y+\varepsilon\eta)=y'+\varepsilon\eta'$.
2. Differentiate under the integral sign (allowed because the integrand is smooth in $\varepsilon$ on a finite interval): $\Phi'(\varepsilon)=\int_a^b \frac{(y'+\varepsilon\eta')\,\eta'}{\sqrt{1+(y'+\varepsilon\eta')^2}}\,dx$, by the chain rule on $\sqrt{\,\cdot\,}$.
3. Set $\varepsilon=0$: $\displaystyle \delta J[y;\eta]=\int_a^b \frac{y'\,\eta'}{\sqrt{1+y'^2}}\,dx.$
This is the first variation; in §s3 we set it to zero and discover the straight line.

#### Common pitfalls

- $\eta$ must vanish at the endpoints; otherwise the competitor leaves the admissible set and the boundary terms in §s2 do not cancel.
- $\delta J=0$ detects *stationarity*, not minimality. Confirming a true minimum requires a "second variation" test, the analogue of $f''>0$, which we mention but do not develop.

## Part B · The fundamental equation

<a id="s2"></a>
### The Euler–Lagrange equation: full derivation

#### What & why

Stationarity, $\delta J[y;\eta]=0$ for all $\eta$, is one equation that must hold for *infinitely many* directions $\eta$. That is unwieldy. The Euler–Lagrange equation repackages "true for all $\eta$" into a single differential equation for $y$ alone — the workhorse of the entire subject. We derive it with no gaps, including the lemma that licenses the final step.

#### Step 1 — compute the first variation in general

1. Start from $\Phi(\varepsilon)=\displaystyle\int_a^b L\big(x,\,y+\varepsilon\eta,\,y'+\varepsilon\eta'\big)\,dx.$
2. Differentiate under the integral (the integrand is smooth in $\varepsilon$ and the interval is finite, so differentiation and integration may be exchanged):
   $$
   \Phi'(\varepsilon)=\int_a^b\left[\frac{\partial L}{\partial y}\,\eta+\frac{\partial L}{\partial y'}\,\eta'\right]dx .
   $$
   *Reason:* the chain rule for a function of several variables. As $\varepsilon$ changes, the second slot of $L$ changes at rate $\eta$ and the third slot at rate $\eta'$; multiply each by the corresponding partial derivative and add.
3. Set $\varepsilon=0$, so the partials are evaluated along the curve $y$ itself:
   $$
   \delta J[y;\eta]=\int_a^b\left[\frac{\partial L}{\partial y}\,\eta+\frac{\partial L}{\partial y'}\,\eta'\right]dx .
   $$

#### Step 2 — integrate the troublesome term by parts

The term containing $\eta'$ hides the freedom of $\eta$ inside a derivative; we move the derivative off $\eta$ and onto the coefficient.
4. Recall **integration by parts**: $\int_a^b u\,v'\,dx=\big[u v\big]_a^b-\int_a^b u'\,v\,dx$, valid for $C^1$ functions (it is the product rule $(uv)'=u'v+uv'$ integrated). Take $u=\dfrac{\partial L}{\partial y'}$ and $v=\eta$ (so $v'=\eta'$):
   $$
   \int_a^b \frac{\partial L}{\partial y'}\,\eta'\,dx=\left[\frac{\partial L}{\partial y'}\,\eta\right]_a^b-\int_a^b \frac{d}{dx}\!\left(\frac{\partial L}{\partial y'}\right)\eta\,dx .
   $$
5. The boundary term vanishes: $\big[\frac{\partial L}{\partial y'}\eta\big]_a^b=\frac{\partial L}{\partial y'}(b)\,\eta(b)-\frac{\partial L}{\partial y'}(a)\,\eta(a)=0$, *because* $\eta(a)=\eta(b)=0$ by the admissibility condition on the variation. This is exactly where the fixed-endpoint requirement earns its keep.

#### Step 3 — collect and apply the fundamental lemma

6. Substitute step 5 back into step 3:
   $$
   \delta J[y;\eta]=\int_a^b\left[\frac{\partial L}{\partial y}-\frac{d}{dx}\!\left(\frac{\partial L}{\partial y'}\right)\right]\eta\,dx .
   $$
   The bracket no longer contains $\eta'$; the entire freedom of the variation now sits in the single factor $\eta$. The bracket is the **functional derivative** $\dfrac{\delta J}{\delta y}$ promised in §s1.
7. Stationarity demands this integral be zero for *every* admissible $\eta$. To conclude that the bracket itself must vanish, we need:

> **Lemma — the fundamental lemma of the calculus of variations**
>
> Let $g$ be a continuous function on $[a,b]$. If $\displaystyle\int_a^b g(x)\,\eta(x)\,dx=0$ for **every** $C^1$ test function $\eta$ with $\eta(a)=\eta(b)=0$, then $g(x)=0$ for all $x\in[a,b]$. (Requiring only $C^1$ test functions makes the lemma easier to apply — the explicit bump below is $C^1$ — and it is enough for the $C^2$ Euler–Lagrange theory, since vanishing against the smaller class of $C^1$ bumps already forces $g\equiv0$; a fortiori it vanishes against all smooth $\eta$.)

*Proof of the lemma (by contradiction).*
1. Suppose $g$ is not identically zero. Then there is a point $c\in(a,b)$ with $g(c)\neq0$; say $g(c)>0$ (if $g(c)<0$ replace $g$ by $-g$).
2. Since $g$ is continuous, there is a small interval $[c-\rho,\,c+\rho]\subset(a,b)$ on which $g(x)>\tfrac12 g(c)>0$. *Reason:* continuity means values near $c$ stay near $g(c)$; pick the tolerance $\tfrac12 g(c)$.
3. Build a "bump" test function that is positive on that interval and zero outside it: let
   $$
   \eta(x)=\begin{cases}\big[(x-(c-\rho))(\,(c+\rho)-x)\big]^2,& x\in[c-\rho,c+\rho],\\[2pt]0,&\text{otherwise.}\end{cases}
   $$
   This $\eta$ is $C^1$ (at the junctions the squared factor and its first derivative both vanish, so $\eta$ and $\eta'$ match the zero piece; it is not $C^2$ there, but $C^1$ is all the lemma's hypothesis now demands), satisfies $\eta(a)=\eta(b)=0$, is $\ge0$ everywhere, and is strictly $>0$ on the open interval $(c-\rho,c+\rho)$.
4. Then $\int_a^b g\,\eta\,dx=\int_{c-\rho}^{c+\rho} g\,\eta\,dx>0$, because the integrand is a product of two positive quantities on a set of positive length and zero elsewhere. (An integral of a continuous function that is positive on an interval is positive.)
5. This contradicts the hypothesis that the integral is zero for *every* such $\eta$. Hence no such $c$ exists and $g\equiv0$. $\blacksquare$

8. Applying the lemma with $g=\dfrac{\partial L}{\partial y}-\dfrac{d}{dx}\big(\dfrac{\partial L}{\partial y'}\big)$ gives the result:

> **Theorem — the Euler–Lagrange equation**
>
> If $y$ is a stationary function (extremal) of $J[y]=\int_a^b L(x,y,y')\,dx$ over admissible functions with fixed endpoints, then $y$ satisfies
> $$
> \frac{\partial L}{\partial y}-\frac{d}{dx}\!\left(\frac{\partial L}{\partial y'}\right)=0 .
> $$
> This is a (generally second-order) ordinary differential equation for $y$. Its solutions are the candidate optimizers.

#### Reading the symbols carefully

In $\dfrac{d}{dx}\big(\dfrac{\partial L}{\partial y'}\big)$, the inner $\partial L/\partial y'$ is a function of $x,y,y'$; the outer $d/dx$ is a **total** derivative that, by the chain rule, accounts for $x$ changing directly *and* through $y(x)$ and $y'(x)$:
$$
\frac{d}{dx}\frac{\partial L}{\partial y'}=\frac{\partial^2 L}{\partial x\,\partial y'}+\frac{\partial^2 L}{\partial y\,\partial y'}\,y'+\frac{\partial^2 L}{\partial y'^2}\,y'' .
$$
The presence of $y''$ shows the equation is second order in general.

#### The Beltrami identity — a free first integral when $L$ has no explicit $x$

If $L$ does not depend on $x$ explicitly (i.e. $\partial L/\partial x=0$), the Euler–Lagrange equation has an immediate first integral that is often far easier to solve.
1. Compute the total derivative of $L$ along the curve: $\dfrac{dL}{dx}=\dfrac{\partial L}{\partial x}+\dfrac{\partial L}{\partial y}y'+\dfrac{\partial L}{\partial y'}y''$ (chain rule).
2. Compute $\dfrac{d}{dx}\!\Big(y'\dfrac{\partial L}{\partial y'}\Big)=y''\dfrac{\partial L}{\partial y'}+y'\dfrac{d}{dx}\dfrac{\partial L}{\partial y'}$ (product rule).
3. Subtract: $\dfrac{dL}{dx}-\dfrac{d}{dx}\!\Big(y'\dfrac{\partial L}{\partial y'}\Big)=\dfrac{\partial L}{\partial x}+y'\Big[\dfrac{\partial L}{\partial y}-\dfrac{d}{dx}\dfrac{\partial L}{\partial y'}\Big].$
4. The bracket is zero on an extremal (Euler–Lagrange). If also $\partial L/\partial x=0$, the right side is zero, so the left side is the derivative of a constant:

> **Beltrami identity** (valid when $\partial L/\partial x=0$):
> $$
> L-y'\,\frac{\partial L}{\partial y'}=\text{constant}.
> $$

This is the variational ancestor of energy conservation (§s8).

#### Common pitfalls

- $\partial L/\partial y'$ means differentiate $L$ treating $y'$ as an independent symbol; only afterward do you take $d/dx$ of the result along the curve. Mixing the two orders is the most common error.
- The Euler–Lagrange equation is *necessary* for an extremum but not *sufficient*; like $f'=0$, it can flag saddles.

## Part C · Worked curves

<a id="s3"></a>
### Worked examples: shortest path, brachistochrone, minimal surface of revolution

#### Example 1 — the shortest path in the plane is a straight line

We prove the "obvious" fact rigorously to see the machinery in action.
1. **Set up the functional.** A curve $y(x)$ from $(a,y_a)$ to $(b,y_b)$ has arc length $L[y]=\int_a^b\sqrt{1+y'^2}\,dx$. *Reason:* an infinitesimal piece of the graph has horizontal run $dx$ and rise $dy=y'\,dx$, so by the Pythagorean theorem its length is $\sqrt{dx^2+dy^2}=\sqrt{1+y'^2}\,dx$; integrating adds the pieces.
2. **Identify $L$.** Here $L=\sqrt{1+y'^2}$ depends only on $y'$, so $\partial L/\partial y=0$ and $\dfrac{\partial L}{\partial y'}=\dfrac{y'}{\sqrt{1+y'^2}}$ (chain rule on the square root).
3. **Euler–Lagrange.** With $\partial L/\partial y=0$ the equation reduces to $\dfrac{d}{dx}\dfrac{y'}{\sqrt{1+y'^2}}=0$, so $\dfrac{y'}{\sqrt{1+y'^2}}=c$ (a constant).
4. **Solve for the slope.** Squaring, $y'^2=c^2(1+y'^2)\Rightarrow y'^2(1-c^2)=c^2\Rightarrow y'=\dfrac{c}{\sqrt{1-c^2}}=:m$, a constant.
5. **Integrate.** $y=mx+k$: a straight line. The two constants $m,k$ are fixed by the endpoints. The shortest path is the straight segment, now *derived*, not assumed.

#### Example 2 — the brachistochrone is a cycloid

1. **Set up the time functional.** Drop the bead from $A=(0,0)$, measuring $y$ *downward* as positive, to $B$. Energy conservation gives speed $v=\sqrt{2gy}$ after falling height $y$ (kinetic energy $\tfrac12 mv^2$ equals lost potential energy $mgy$, so $v=\sqrt{2gy}$). Time to traverse arc length $ds=\sqrt{1+y'^2}\,dx$ at speed $v$ is $dt=ds/v$, so the total descent time is
   $$
   T[y]=\int_0^{x_B}\frac{\sqrt{1+y'^2}}{\sqrt{2gy}}\,dx .
   $$
2. **Identify $L$.** $L=\dfrac{\sqrt{1+y'^2}}{\sqrt{2gy}}$ has *no explicit $x$*, so the **Beltrami identity** applies.
3. **Apply Beltrami.** Compute $\dfrac{\partial L}{\partial y'}=\dfrac{1}{\sqrt{2gy}}\cdot\dfrac{y'}{\sqrt{1+y'^2}}$, then
   $$
   L-y'\frac{\partial L}{\partial y'}=\frac{1}{\sqrt{2gy}}\left[\sqrt{1+y'^2}-\frac{y'^2}{\sqrt{1+y'^2}}\right]=\frac{1}{\sqrt{2gy}}\cdot\frac{1}{\sqrt{1+y'^2}}=\text{const}.
   $$
   *Reason:* combine over the common denominator $\sqrt{1+y'^2}$; the numerator $\,(1+y'^2)-y'^2=1$.
4. **Reduce to an ODE.** Squaring and absorbing constants, $y\,(1+y'^2)=C$ for a constant $C=2R$. This is the defining differential equation of a **cycloid**.
5. **Solve by a parameter.** The substitution $y'=\cot(\theta/2)$ is chosen so that the awkward factor $1+y'^2$ collapses by the Pythagorean identity: $1+y'^2=1+\cot^2(\theta/2)=\csc^2(\theta/2)$, which is what makes the algebra below close. With it, $y=\dfrac{C}{\csc^2(\theta/2)}=C\sin^2(\theta/2)=\tfrac{C}{2}(1-\cos\theta)=R(1-\cos\theta)$, using the half-angle identity $\sin^2(\theta/2)=\tfrac12(1-\cos\theta)$. Now recover $x$ by integrating $dx=dy/y'$. Differentiating $y=R(1-\cos\theta)$ gives $dy=R\sin\theta\,d\theta$, so
   $$
   dx=\frac{dy}{y'}=\frac{R\sin\theta\,d\theta}{\cot(\theta/2)}=R\sin\theta\,\tan(\theta/2)\,d\theta.
   $$
   Half-angle simplification $\sin\theta=2\sin(\theta/2)\cos(\theta/2)$ turns $\sin\theta\,\tan(\theta/2)=2\sin^2(\theta/2)=1-\cos\theta$, so $dx=R(1-\cos\theta)\,d\theta$. Integrating (with $x=0$ at $\theta=0$) gives $x=R(\theta-\sin\theta)$.
   $$
   x=R(\theta-\sin\theta),\qquad y=R(1-\cos\theta).
   $$
   These are exactly the parametric equations of a cycloid — the curve traced by a point on a circle of radius $R$ rolling along a line. The fastest descent curve is therefore an arc of a cycloid, with $R$ chosen to pass through $B$.

#### Example 3 — the minimal surface of revolution is a catenoid

Spin a curve $y(x)\ge0$ about the $x$-axis; the surface (think of a soap film between two rings) has area $S[y]=\int_a^b 2\pi y\sqrt{1+y'^2}\,dx$ (each strip is a band of radius $y$ and slant width $\sqrt{1+y'^2}\,dx$). We minimize $S$.
1. **Identify $L$.** Drop the constant $2\pi$: $L=y\sqrt{1+y'^2}$, again with no explicit $x$, so use **Beltrami**.
2. **Apply Beltrami.** $\dfrac{\partial L}{\partial y'}=\dfrac{y\,y'}{\sqrt{1+y'^2}}$, and
   $$
   y\sqrt{1+y'^2}-y'\cdot\frac{y\,y'}{\sqrt{1+y'^2}}=\frac{y}{\sqrt{1+y'^2}}=c .
   $$
3. **Solve.** Thus $y=c\sqrt{1+y'^2}$, i.e. $y'=\sqrt{(y/c)^2-1}$. Separating variables, $\displaystyle\int\frac{dy}{\sqrt{(y/c)^2-1}}=\int dx$ gives $c\,\operatorname{arccosh}(y/c)=x-x_0$, hence
   $$
   y=c\,\cosh\!\frac{x-x_0}{c}.
   $$
   This is a **catenary**, and the surface it sweeps is a **catenoid** — the actual shape a soap film takes between two coaxial rings.

#### A concrete number

For Example 1 with $A=(0,0)$, $B=(3,4)$: step 4 gives $m=(4-0)/(3-0)=4/3$, $k=0$, so $y=\tfrac{4}{3}x$ and the length is $\int_0^3\sqrt{1+16/9}\,dx=\int_0^3\tfrac{5}{3}\,dx=5$ — the Pythagorean hypotenuse $\sqrt{3^2+4^2}=5$. The variational method reproduces elementary geometry, a sanity check.

#### Common pitfalls

- In the brachistochrone, measuring $y$ upward flips a sign and hides the cycloid; choose "down is positive" so $v=\sqrt{2gy}$ is real.
- Minimal-surface problems can fail to have a smooth solution when the rings are too far apart (the film breaks into two disks); the Euler–Lagrange equation finds a candidate, but existence still needs checking.

## Part D · Generalizations

<a id="s4"></a>
### Several functions and several independent variables (fields)

#### Several unknown functions

Often a state is described by *several* functions of one variable at once — e.g. a particle's three coordinates $y_1(x),y_2(x),y_3(x)$ as functions of time $x$. The functional becomes
$$
J[y_1,\dots,y_n]=\int_a^b L\big(x,\,y_1,\dots,y_n,\,y_1',\dots,y_n'\big)\,dx .
$$
Vary one function $y_k$ at a time with an independent bump $\eta_k$ (the others held fixed). Each variation must independently vanish, so repeating the §s2 derivation once per index gives a **system** of Euler–Lagrange equations:
$$
\frac{\partial L}{\partial y_k}-\frac{d}{dx}\!\left(\frac{\partial L}{\partial y_k'}\right)=0,\qquad k=1,\dots,n .
$$
1. Hold all $y_j$ ($j\neq k$) fixed and set $y_k\to y_k+\varepsilon\eta_k$, with $\eta_k(a)=\eta_k(b)=0$.
2. The first variation in this direction is $\int_a^b\big[\partial L/\partial y_k-\frac{d}{dx}(\partial L/\partial y_k')\big]\eta_k\,dx$, exactly as in §s2 since only the $k$-th slots move.
3. The fundamental lemma forces the bracket to vanish. As $k$ was arbitrary, all $n$ equations hold. *Reason for treating them independently:* the bumps $\eta_k$ can be chosen one at a time, so stationarity in each direction is a separate condition.

#### Several independent variables — fields

Now let the unknown be a function of *several* inputs, $u(x_1,\dots,x_m)$ — a **field**, e.g. the height $u(x,t)$ of a vibrating string at position $x$ and time $t$. The integral runs over a region $\Omega$ and the integrand depends on $u$ and its partial derivatives $u_{x_i}=\partial u/\partial x_i$:
$$
J[u]=\int_\Omega L\big(x_i,\,u,\,u_{x_1},\dots,u_{x_m}\big)\,dx_1\cdots dx_m .
$$
Vary $u\to u+\varepsilon\eta$ with $\eta=0$ on the boundary $\partial\Omega$. The first variation is
$$
\delta J=\int_\Omega\left[\frac{\partial L}{\partial u}\,\eta+\sum_{i=1}^m\frac{\partial L}{\partial u_{x_i}}\,\eta_{x_i}\right]dx .
$$
Integrate the second group of terms by parts in several variables: the **divergence theorem** turns $\int_\Omega (\partial L/\partial u_{x_i})\,\eta_{x_i}\,dx$ into a boundary integral (which vanishes since $\eta=0$ on $\partial\Omega$) minus $\int_\Omega \frac{\partial}{\partial x_i}(\partial L/\partial u_{x_i})\,\eta\,dx$. Collecting and applying the multivariable fundamental lemma gives:

> **Euler–Lagrange equation for a field**
> $$
> \frac{\partial L}{\partial u}-\sum_{i=1}^m\frac{\partial}{\partial x_i}\!\left(\frac{\partial L}{\partial u_{x_i}}\right)=0 .
> $$

This single equation is the engine of classical field theory (§s10).

#### Worked example — the vibrating string

With $u(x,t)$ and $L=\tfrac12\rho\,u_t^2-\tfrac12\tau\,u_x^2$ (kinetic minus elastic energy density; $\rho$ = mass per length, $\tau$ = tension), compute $\partial L/\partial u=0$, $\partial L/\partial u_t=\rho u_t$, $\partial L/\partial u_x=-\tau u_x$. The field equation gives $0-\big[\partial_t(\rho u_t)+\partial_x(-\tau u_x)\big]=0$, i.e.
$$
\rho\,u_{tt}=\tau\,u_{xx},
$$
the **wave equation**, with wave speed $\sqrt{\tau/\rho}$. The dynamics of the string fell straight out of a variational principle.

#### Common pitfalls

- With several variables you must integrate by parts in *each* derivative slot and discard *each* boundary term; missing one corrupts the equation.
- Treat $u$ and each $u_{x_i}$ as independent slots of $L$ when differentiating, exactly as with $y,y'$ before.

<a id="s5"></a>
### Constraints: Lagrange multipliers and isoperimetric problems

#### What & why

Real problems often optimize one functional *subject to another being fixed*: minimize area at fixed volume, minimize energy at fixed length. The tool is the same **Lagrange multiplier** idea from ordinary multivariable calculus, lifted to functionals.

#### Recall (one line)

In ordinary calculus, to extremize $f$ subject to $g=$ const, one solves $\nabla f=\lambda\nabla g$ for a number $\lambda$: at a constrained optimum the gradient of the objective is parallel to that of the constraint.

#### The variational version

To extremize $J[y]=\int_a^b L\,dx$ subject to the **isoperimetric constraint** $K[y]=\int_a^b G\,dx=\ell$ (a fixed number), introduce a constant **multiplier** $\lambda$ and extremize the combined functional $J-\lambda K$ freely:

> **Theorem.** An extremal of $J$ subject to $K=\ell$ satisfies the Euler–Lagrange equation of $L-\lambda G$:
> $$
> \frac{\partial(L-\lambda G)}{\partial y}-\frac{d}{dx}\frac{\partial(L-\lambda G)}{\partial y'}=0 ,
> $$
> for some constant $\lambda$, determined together with the integration constants by the endpoints and the constraint $K=\ell$.

*Why this works (sketch with reasons).* Admissible variations must keep $K$ fixed to first order, i.e. $\delta K=0$, so $\eta$ is no longer free — it is restricted to directions tangent to the constraint. The condition "$\delta J=0$ for all $\eta$ with $\delta K=0$" is, by the same linear-algebra fact behind ordinary Lagrange multipliers, equivalent to "$\delta J=\lambda\,\delta K$ for some constant $\lambda$ and *all* $\eta$," which is $\delta(J-\lambda K)=0$. Then the unconstrained derivation of §s2 applies to $L-\lambda G$.

#### Worked example — the hanging chain (catenary)

A uniform flexible chain of *fixed length* $\ell$ hangs between two posts; it settles into the shape of **lowest potential energy**. We derive that shape.
1. **Objective.** Potential energy is (mass density)$\times g\times$(height), summed: $J[y]=\int_a^b \rho g\,y\,\sqrt{1+y'^2}\,dx$ (the factor $\sqrt{1+y'^2}\,dx$ is the arc length of a piece, carrying mass $\rho\,ds$ at height $y$). Drop the constant $\rho g$.
2. **Constraint.** The chain's length is fixed: $K[y]=\int_a^b\sqrt{1+y'^2}\,dx=\ell$.
3. **Combine.** Extremize $L-\lambda G$ with $L-\lambda G=(y-\lambda)\sqrt{1+y'^2}$. No explicit $x$, so use **Beltrami**:
   $$
   (y-\lambda)\sqrt{1+y'^2}-y'\frac{(y-\lambda)y'}{\sqrt{1+y'^2}}=\frac{y-\lambda}{\sqrt{1+y'^2}}=c .
   $$
4. **Solve.** This is the catenoid equation of §s3 shifted by $\lambda$: $y-\lambda=c\cosh\frac{x-x_0}{c}$, i.e.
   $$
   y=\lambda+c\,\cosh\!\frac{x-x_0}{c}.
   $$
   The hanging chain is a **catenary**. The constants $\lambda,c,x_0$ are fixed by the two endpoint heights and the length constraint $K=\ell$.

#### Common pitfalls

- The multiplier $\lambda$ is an *unknown to be solved for*, not a free choice; the constraint equation supplies the extra equation needed to find it.
- "Isoperimetric" historically means "same perimeter" (the classic problem: maximize area enclosed by a curve of fixed length, whose answer is a circle); the name now covers any integral-constraint problem.

<a id="s6"></a>
### Geodesics as a variational problem

#### What & why

A **geodesic** is the locally shortest curve on a surface or, more generally, in a space with a notion of distance. Geodesics generalize "straight line" to curved spaces and are central to differential geometry and general relativity (where free-falling bodies trace geodesics of spacetime).

#### The metric and the length functional (one-line prerequisite restatement)

On a surface, distances are encoded by a **metric**: infinitesimal length squared is $ds^2=\sum_{i,j} g_{ij}(q)\,dq^i\,dq^j$, where $q^i$ are coordinates and $g_{ij}$ are given functions (the **metric tensor**). The length of a curve $q(t)$, $t\in[0,1]$, is
$$
L[q]=\int_0^1\sqrt{\sum_{i,j}g_{ij}(q)\,\dot q^i\dot q^j}\;dt,\qquad \dot q^i=\frac{dq^i}{dt}.
$$
A geodesic is an extremal of $L$.

#### Energy functional trick

The square-root integrand is awkward. Geodesics (up to reparametrization) also extremize the **energy** $E[q]=\tfrac12\int_0^1\sum_{i,j}g_{ij}\dot q^i\dot q^j\,dt$, whose Euler–Lagrange equations are cleaner and which selects the constant-speed parametrization.

#### Worked derivation — the geodesic equation

Take $L_E=\tfrac12 g_{ij}\dot q^i\dot q^j$ (summation over repeated indices implied). Apply the multi-function Euler–Lagrange equation (§s4) with the role of "$x$" played by $t$ and "$y_k$" by $q^k$:
1. $\dfrac{\partial L_E}{\partial q^k}=\tfrac12\,\partial_k g_{ij}\,\dot q^i\dot q^j$ (the metric depends on position).
2. $\dfrac{\partial L_E}{\partial \dot q^k}=g_{kj}\dot q^j$ (differentiate the quadratic form; the factor $\tfrac12$ and the two symmetric terms combine).
3. $\dfrac{d}{dt}\dfrac{\partial L_E}{\partial \dot q^k}=g_{kj}\ddot q^j+\partial_i g_{kj}\,\dot q^i\dot q^j$ (product + chain rule).
4. Euler–Lagrange ($\frac{d}{dt}\partial_{\dot q^k}L_E-\partial_{q^k}L_E=0$) gives $g_{kj}\ddot q^j+\big(\partial_i g_{kj}-\tfrac12\partial_k g_{ij}\big)\dot q^i\dot q^j=0$.
5. Symmetrizing the middle term and multiplying by the inverse metric $g^{mk}$ yields the **geodesic equation**
   $$
   \ddot q^m+\Gamma^m_{ij}\,\dot q^i\dot q^j=0,\qquad \Gamma^m_{ij}=\tfrac12 g^{mk}\big(\partial_i g_{kj}+\partial_j g_{ki}-\partial_k g_{ij}\big),
   $$
   where $\Gamma^m_{ij}$ are the **Christoffel symbols**. This is the precise statement that a geodesic has "zero acceleration" relative to the curved geometry.

#### Worked example — great circles on the sphere

On the unit sphere with coordinates $(\theta,\phi)$ (colatitude, longitude), $ds^2=d\theta^2+\sin^2\theta\,d\phi^2$, so $g_{\theta\theta}=1,\ g_{\phi\phi}=\sin^2\theta$. Since $L_E$ has no explicit $\phi$, the $\phi$-Euler–Lagrange equation gives a conserved quantity $\partial L_E/\partial\dot\phi=\sin^2\theta\,\dot\phi=$ const (an instance of §s8). Working through the $\theta$-equation, the solutions are exactly the **great circles** — the intersections of the sphere with planes through its center. This confirms the airplane intuition of §s0.

#### Common pitfalls

- Length is invariant under reparametrization, so the length functional's extremals are determined only up to how you run along them; the energy functional removes this ambiguity by fixing constant speed.
- Geodesics are *locally* shortest; a great-circle arc going "the long way around" is still a geodesic but not the global minimum.

## Part E · Mechanics

<a id="s7"></a>
### Hamilton's principle and Lagrangian mechanics

#### What & why

We now cash in the machinery: the laws of mechanics are a variational principle. Instead of Newton's "force causes acceleration," we posit a single scalar quantity and demand it be stationary; Newton's law then *follows*.

#### The action and Hamilton's principle

For a mechanical system with coordinate(s) $q(t)$, define the **Lagrangian** $L=T-V$, the kinetic energy minus the potential energy, and the **action**
$$
S[q]=\int_{t_1}^{t_2} L\big(q,\dot q,t\big)\,dt .
$$

> **Hamilton's principle.** The actual motion $q(t)$ between fixed configurations $q(t_1)$ and $q(t_2)$ is a **stationary point** of the action $S$.

By §s2 (with $x\to t$, $y\to q$), stationarity is equivalent to the Euler–Lagrange equation, here called the **equation of motion**:
$$
\frac{d}{dt}\frac{\partial L}{\partial \dot q}-\frac{\partial L}{\partial q}=0 .
$$

#### Deriving Newton's law from a Lagrangian

Consider one particle of mass $m$ in one dimension under a potential $V(q)$.
1. **Write the Lagrangian.** Kinetic energy $T=\tfrac12 m\dot q^2$, potential $V(q)$, so $L=\tfrac12 m\dot q^2-V(q)$.
2. **Compute the pieces.** $\dfrac{\partial L}{\partial \dot q}=m\dot q$ (the **momentum** $p$), and $\dfrac{\partial L}{\partial q}=-\dfrac{dV}{dq}$ (the **force** $F=-V'$, by definition of a potential).
3. **Euler–Lagrange.** $\dfrac{d}{dt}(m\dot q)-(-V'(q))=0\Rightarrow m\ddot q=-V'(q)=F.$
4. This is exactly **Newton's second law** $F=ma$. The variational principle does not merely agree with Newton — it *contains* him.

#### Why $T-V$ and not $T+V$?

A natural worry: why minus, not plus? The sign is fixed by requiring the equation of motion to come out right: only $L=T-V$ produces $m\ddot q=-V'$. With $T+V$ (the energy) one would get $m\ddot q=+V'$, the wrong sign. The action is *not* the energy; energy is a different combination (§s9).

#### Worked example — the simple harmonic oscillator

A mass on a spring has $V=\tfrac12 k q^2$, so $L=\tfrac12 m\dot q^2-\tfrac12 k q^2$. Then $\partial L/\partial\dot q=m\dot q$, $\partial L/\partial q=-kq$, and the equation of motion is $m\ddot q+kq=0$, with solution $q(t)=A\cos(\omega t+\varphi)$, $\omega=\sqrt{k/m}$ — sinusoidal oscillation, recovered from the action.

#### The payoff: generalized coordinates

Lagrangian mechanics shines because the equation $\frac{d}{dt}\partial_{\dot q}L=\partial_q L$ holds in *any* coordinates $q$ — angles, distances along a wire, whatever fits the problem — with no need to resolve forces into components. Choose coordinates that match the geometry, write $T-V$, and turn the crank.

#### Common pitfalls

- $L=T-V$ uses the energies expressed in your chosen coordinates; in non-Cartesian coordinates $T$ picks up metric factors (e.g. $\tfrac12 m(\dot r^2+r^2\dot\theta^2)$ in polar).
- Hamilton's principle requires *fixed endpoints in configuration*, not fixed velocities; you specify where the system is at $t_1$ and $t_2$.

<a id="s8"></a>
### Symmetries and Noether's theorem

#### What & why

The most beautiful theorem in this guide: **every continuous symmetry of the action yields a conserved quantity.** Time-shift symmetry gives energy conservation; space-shift symmetry gives momentum conservation; rotation symmetry gives angular momentum. Conservation laws are not accidents — they are shadows of symmetries.

#### Cyclic coordinates — the easy case first

If $L$ does not depend on a particular coordinate $q$ (only on $\dot q$), that $q$ is **cyclic** and the Euler–Lagrange equation gives an immediate conservation law: $\frac{d}{dt}\frac{\partial L}{\partial\dot q}=\frac{\partial L}{\partial q}=0$, so the **conjugate momentum** $p=\partial L/\partial\dot q$ is constant. *Example:* if $L$ is independent of position $x$, then linear momentum $p=m\dot x$ is conserved — translation symmetry $\Rightarrow$ momentum conservation, in one line.

#### Noether's theorem (statement)

> **Theorem (Noether).** Suppose the action is invariant (to first order) under a continuous family of transformations $q\to q+\varepsilon\,\psi(q,t)$ with infinitesimal generator $\psi$, meaning the Lagrangian changes by at most a total time derivative, $\delta L=\frac{d}{dt}F$. Then along any solution of the equations of motion the quantity
> $$
> Q=\frac{\partial L}{\partial \dot q}\,\psi-F
> $$
> is conserved: $\dfrac{dQ}{dt}=0$.

#### Derivation

1. Under $q\to q+\varepsilon\psi$, $\dot q\to\dot q+\varepsilon\dot\psi$. To first order in $\varepsilon$ the change in $L$ is $\delta L=\dfrac{\partial L}{\partial q}\psi+\dfrac{\partial L}{\partial \dot q}\dot\psi$ (chain rule).
2. On a solution, $\dfrac{\partial L}{\partial q}=\dfrac{d}{dt}\dfrac{\partial L}{\partial \dot q}$ (Euler–Lagrange, §s7). Substitute:
   $$
   \delta L=\frac{d}{dt}\!\left(\frac{\partial L}{\partial \dot q}\right)\psi+\frac{\partial L}{\partial \dot q}\dot\psi=\frac{d}{dt}\!\left(\frac{\partial L}{\partial \dot q}\,\psi\right),
   $$
   where the last equality is the product rule run backwards.
3. By hypothesis $\delta L=\dfrac{dF}{dt}$. Equate: $\dfrac{d}{dt}\big(\frac{\partial L}{\partial\dot q}\psi\big)=\dfrac{dF}{dt}$, so $\dfrac{d}{dt}\big(\frac{\partial L}{\partial\dot q}\psi-F\big)=0$. Hence $Q$ is conserved. $\blacksquare$

#### Energy from time-translation symmetry

Time symmetry needs a slightly different treatment because it shifts $t$ itself, but the conclusion is the Beltrami identity of §s2 in disguise.
1. Suppose $L$ has no explicit time dependence, $\partial L/\partial t=0$.
2. Compute the total time derivative $\dfrac{dL}{dt}=\dfrac{\partial L}{\partial q}\dot q+\dfrac{\partial L}{\partial \dot q}\ddot q$ (no $\partial L/\partial t$ term).
3. Using Euler–Lagrange to replace $\partial L/\partial q$ by $\frac{d}{dt}\partial_{\dot q}L$, this equals $\dfrac{d}{dt}\big(\dot q\,\frac{\partial L}{\partial\dot q}\big)$ (product rule).
4. Therefore $\dfrac{d}{dt}\Big(\dot q\,\dfrac{\partial L}{\partial \dot q}-L\Big)=0$. The conserved quantity
   $$
   H=\dot q\,\frac{\partial L}{\partial \dot q}-L
   $$
   is the **energy** (Hamiltonian, §s9). For $L=\tfrac12 m\dot q^2-V$, $H=m\dot q^2-(\tfrac12 m\dot q^2-V)=\tfrac12 m\dot q^2+V=T+V$ — exactly the total energy.

#### Worked example — momentum from translation symmetry

Two particles interacting through a potential depending only on their *separation*, $V(q_1-q_2)$, have $L=\tfrac12 m_1\dot q_1^2+\tfrac12 m_2\dot q_2^2-V(q_1-q_2)$. The shift $q_1\to q_1+\varepsilon,\ q_2\to q_2+\varepsilon$ leaves $V$ (hence $L$) unchanged, so $\delta L=0$ and $F=0$, $\psi=1$ for each. Noether's $Q=\frac{\partial L}{\partial\dot q_1}\cdot1+\frac{\partial L}{\partial\dot q_2}\cdot1=m_1\dot q_1+m_2\dot q_2$ — the **total linear momentum**, conserved. Translation invariance $\Rightarrow$ momentum conservation, proven.

#### Common pitfalls

- The symmetry must be *continuous* (a one-parameter family); a discrete symmetry like reflection gives no Noether charge.
- $\delta L$ may equal a total derivative $\frac{dF}{dt}$ without being literally zero; that still counts, and forgetting the $-F$ term gives a wrong (non-conserved) $Q$.

## Part F · Hamiltonian form and fields

<a id="s9"></a>
### The Hamiltonian formulation, the Legendre transform, and canonical equations

#### What & why

Lagrangian mechanics uses position and velocity $(q,\dot q)$ and gives second-order equations. The **Hamiltonian** formulation trades velocity for momentum $(q,p)$ and replaces each second-order equation by *two* first-order ones with a striking symmetry. This viewpoint underlies statistical mechanics, chaos theory, and the path to quantum mechanics.

#### The Legendre transform (the engine)

We want to swap the variable $\dot q$ for $p=\partial L/\partial\dot q$. The clean way to change variables in this manner is the **Legendre transform**.

> **Definition — Legendre transform.** Given $L(\dot q)$ (treat $q,t$ as parameters), define $p=\dfrac{\partial L}{\partial \dot q}$ and
> $$
> H(q,p,t)=p\,\dot q-L(q,\dot q,t),
> $$
> where $\dot q$ on the right is expressed in terms of $p$ by inverting $p=\partial L/\partial\dot q$. $H$ is the **Hamiltonian**.

The transform is well defined (invertible) provided $\partial^2 L/\partial\dot q^2\neq0$, which makes $p(\dot q)$ strictly monotonic so it can be inverted.

#### Deriving Hamilton's canonical equations

Take the differential of $H=p\dot q-L$ and compare coefficients.
1. $dH=\dot q\,dp+p\,d\dot q-\dfrac{\partial L}{\partial q}dq-\dfrac{\partial L}{\partial \dot q}d\dot q-\dfrac{\partial L}{\partial t}dt$ (product rule + chain rule).
2. The terms $p\,d\dot q$ and $-\frac{\partial L}{\partial\dot q}d\dot q$ cancel, *because* $p=\partial L/\partial\dot q$ by definition. This cancellation is the whole point of the Legendre transform: $H$ genuinely depends on $p$, not on $\dot q$.
3. So $dH=\dot q\,dp-\dfrac{\partial L}{\partial q}dq-\dfrac{\partial L}{\partial t}dt$. But also $dH=\dfrac{\partial H}{\partial q}dq+\dfrac{\partial H}{\partial p}dp+\dfrac{\partial H}{\partial t}dt$ by definition of the differential.
4. Match coefficients of the independent differentials $dq,dp,dt$:
   $$
   \frac{\partial H}{\partial p}=\dot q,\qquad \frac{\partial H}{\partial q}=-\frac{\partial L}{\partial q},\qquad \frac{\partial H}{\partial t}=-\frac{\partial L}{\partial t}.
   $$
5. From Euler–Lagrange, $\dfrac{\partial L}{\partial q}=\dfrac{d}{dt}\dfrac{\partial L}{\partial\dot q}=\dot p$. Substituting into the middle relation gives $\partial H/\partial q=-\dot p$. Collecting:

> **Hamilton's canonical equations**
> $$
> \dot q=\frac{\partial H}{\partial p},\qquad \dot p=-\frac{\partial H}{\partial q}.
> $$

These two first-order equations are equivalent to the single second-order Euler–Lagrange equation, but their symmetry between $q$ and $p$ is the gateway to deeper structure (phase space, Poisson brackets, quantization).

#### Conservation of energy, revisited

From the canonical equations, $\dfrac{dH}{dt}=\dfrac{\partial H}{\partial q}\dot q+\dfrac{\partial H}{\partial p}\dot p+\dfrac{\partial H}{\partial t}=(-\dot p)\dot q+\dot q\,\dot p+\dfrac{\partial H}{\partial t}=\dfrac{\partial H}{\partial t}$. The first two terms cancel identically, so if $H$ has no explicit time dependence ($\partial H/\partial t=0$), then $H$ is conserved — energy conservation, again, now almost trivial.

#### Worked example — the harmonic oscillator in Hamiltonian form

From $L=\tfrac12 m\dot q^2-\tfrac12 k q^2$: $p=m\dot q\Rightarrow\dot q=p/m$, and $H=p\dot q-L=\dfrac{p^2}{m}-\big(\tfrac12 m(p/m)^2-\tfrac12 kq^2\big)=\dfrac{p^2}{2m}+\tfrac12 kq^2$ — kinetic plus potential, the total energy. Canonical equations: $\dot q=\partial H/\partial p=p/m$ and $\dot p=-\partial H/\partial q=-kq$, which combine to $m\ddot q=-kq$, the same oscillator as in §s7.

#### Common pitfalls

- $H$ equals $T+V$ only when the coordinates are not explicitly time-dependent and $T$ is quadratic in the velocities; in general $H=p\dot q-L$ is the definition, and "energy" is whatever that yields.
- After forming $H$ you must eliminate $\dot q$ in favor of $p$; leaving a stray $\dot q$ inside $H$ is the classic mistake.

<a id="s10"></a>
### Field theory (brief): the Lagrangian density and field equations

#### What & why

The final generalization: the unknown is a **field** $\phi(x^\mu)$ — a quantity defined at every point of space and time, like the electromagnetic potential or the value of a quantum field. The same variational principle, with an integral over spacetime, produces the equations of all classical field theories. This is the bridge from this guide to electromagnetism and quantum field theory.

#### The Lagrangian density and the action

For a field $\phi$ depending on spacetime coordinates $x^\mu=(t,x,y,z)$, we do not have a single $L$ but a **Lagrangian density** $\mathcal{L}$ — Lagrangian *per unit volume* — that depends on the field and its spacetime derivatives $\partial_\mu\phi=\partial\phi/\partial x^\mu$:
$$
S[\phi]=\int \mathcal{L}\big(\phi,\,\partial_\mu\phi,\,x^\mu\big)\,d^4x ,
$$
where $d^4x=dt\,dx\,dy\,dz$ and the integral runs over a region of spacetime. The action is again a number; Hamilton's principle again demands it be stationary.

#### The field Euler–Lagrange equation

This is the case of §s4 with $m=4$ independent variables and the field playing the role of $u$. Varying $\phi\to\phi+\varepsilon\eta$ with $\eta=0$ on the boundary and applying the divergence theorem (integration by parts in spacetime) gives:

> **Euler–Lagrange equation for a field**
> $$
> \frac{\partial \mathcal{L}}{\partial \phi}-\partial_\mu\!\left(\frac{\partial \mathcal{L}}{\partial(\partial_\mu\phi)}\right)=0 ,
> $$
> with summation over the repeated index $\mu=0,1,2,3$.

*Derivation in brief, with reasons:*
1. First variation: $\delta S=\int\big[\frac{\partial\mathcal{L}}{\partial\phi}\eta+\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi)}\partial_\mu\eta\big]d^4x$ (chain rule, as in §s4).
2. Integrate the second term by parts: $\int\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi)}\partial_\mu\eta\,d^4x=\oint(\cdots)\,dS-\int\partial_\mu\big(\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi)}\big)\eta\,d^4x$ (divergence theorem).
3. The boundary integral vanishes since $\eta=0$ there.
4. Collect; the multivariable fundamental lemma forces the bracket to zero, giving the stated equation.

#### Worked example — the Klein–Gordon field

Take the relativistic scalar density $\mathcal{L}=\tfrac12\big(\partial_t\phi\big)^2-\tfrac12|\nabla\phi|^2-\tfrac12 m^2\phi^2$ (kinetic minus gradient minus mass terms; using units with wave speed $1$).
1. $\dfrac{\partial\mathcal{L}}{\partial\phi}=-m^2\phi$.
2. $\dfrac{\partial\mathcal{L}}{\partial(\partial_t\phi)}=\partial_t\phi$ and $\dfrac{\partial\mathcal{L}}{\partial(\partial_i\phi)}=-\partial_i\phi$.
3. Field equation: $-m^2\phi-\big[\partial_t(\partial_t\phi)+\partial_i(-\partial_i\phi)\big]=0$, i.e.
   $$
   \partial_t^2\phi-\nabla^2\phi+m^2\phi=0 ,
   $$
   the **Klein–Gordon equation**. Setting $m=0$ recovers the wave equation; the same template, with the right $\mathcal{L}$, yields Maxwell's equations and Einstein's equations.

#### Common pitfalls

- $\mathcal{L}$ is a *density*; the physical Lagrangian is its space integral $L=\int\mathcal{L}\,d^3x$.
- The index $\mu$ runs over *all four* spacetime directions; omitting the time derivative term gives a wrong, static equation.

---

*A complete first course in the calculus of variations: functionals and the first variation, the Euler–Lagrange equation derived gap-free from the fundamental lemma, the classic curves (straight line, brachistochrone cycloid, catenoid), generalizations to many functions and to fields, constrained problems via Lagrange multipliers, geodesics, and the full arc of analytical mechanics — Hamilton's principle, Noether's theorem, the Hamiltonian and the Legendre transform, and classical field theory. Every symbol is defined in words and every claim is proven. The single thread running through it all: nature's laws are the condition that an action be stationary.*
