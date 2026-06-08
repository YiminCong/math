**English** · [中文](differential-equations.zh.md)

# Differential equations, *solved.*

A full first course — from a single separable equation to systems, the Laplace transform, and the heat equation — laid out basics → expert. Every core method is **demonstrated** on a worked example, every symbol is defined in words, and every derivation is written as a numbered, gap-free chain of reasons. The threads back to integration and linear algebra are made explicit.

[← Back to all guides](../README.md)

## Part A · First-order equations

<a id="s0"></a>
### The big picture: what a differential equation is

#### What this section says, in one breath

A differential equation is a sentence about *change*. Ordinary algebra hands you an equation like $x+3=7$ and asks "what *number* makes this true?" A differential equation instead hands you a rule about how fast something is changing and asks "what *function* makes this true?" Solving one means turning a statement about rates into a statement about the quantity itself.

#### Every term, defined from zero

- A **variable** is a symbol standing for a number that can change, e.g. $x$.
- A **function** $y(x)$ is a machine that takes an input number $x$ and returns one output number, written $y$. We say "$y$ depends on $x$." Here $x$ is the **independent variable** (the input we are free to choose) and $y$ is the **dependent variable** (the output it determines).
- The **derivative** of $y$ with respect to $x$, written $y'$ or $\dfrac{dy}{dx}$, is the *instantaneous rate of change* of $y$ as $x$ changes: how much output you get per tiny unit of input. If $y$ is position and $x$ is time, $y'$ is velocity.
- A **second derivative** $y''=\dfrac{d^2y}{dx^2}$ is the rate of change of the rate of change (e.g. acceleration). Higher derivatives $y^{(n)}$ continue the pattern.
- An **integral** $\int f(x)\,dx$ is the reverse of differentiation (the **antiderivative**): a function whose derivative is $f$. The **Fundamental Theorem of Calculus** says differentiating and integrating undo each other.

> **Definition — ordinary differential equation (ODE)**
>
> An **ordinary differential equation** relates an unknown function $y(x)$ to one or more of its derivatives. "Ordinary" means there is exactly **one** independent variable, so only ordinary (not partial) derivatives appear. A **solution** is a function — not a number — that, when substituted in, makes the equation a true statement for every $x$ in some interval.

Three labels classify any ODE:

- **Order** — the highest derivative that appears. $y'=ky$ is **first order** (only $y'$); $y''+y=0$ is **second order** ($y''$ is the highest).
- **Linear vs nonlinear** — the equation is **linear** when $y$ and its derivatives each appear only to the first power, are never multiplied by one another, and sit inside no other function (no $y^2$, no $y\,y'$, no $\sin y$). The general linear form is
  $$a_n(x)\,y^{(n)}+\cdots+a_1(x)\,y'+a_0(x)\,y=g(x),$$
  where the **coefficients** $a_k(x)$ and the **forcing term** $g(x)$ are known functions of $x$ only. Anything else is **nonlinear**.
- **ODE vs PDE** — one independent variable gives an ODE; several independent variables give **partial** derivatives and a **partial differential equation** (PDE, §s17).

> **Principle — solving = integrating with structure**
>
> The simplest ODE is $y'=f(x)$, where the right side has no $y$ in it. By the definition of an antiderivative it is solved by a single integration: $y=\int f(x)\,dx+C$. Every method in this guide is a way of **reducing a harder equation to integrations you can already do**. The arbitrary constant $C$ is the fingerprint of a differential equation: because differentiating any constant gives zero, infinitely many functions differing by a constant share the same derivative. A first-order ODE therefore has a *one-parameter family* of solutions, and an **initial condition** $y(x_0)=y_0$ (the value of $y$ at one chosen input $x_0$) selects exactly one curve from the family.

**General vs particular solution**

$$y'=f(x)\ \Longrightarrow\ y=\int f(x)\,dx+C \quad(\text{general}),\qquad y(x_0)=y_0\ \text{fixes}\ C\ (\text{particular}).$$

A **general solution** carries the arbitrary constants and describes the whole family; a **particular solution** has the constants pinned to specific numbers by extra conditions. An $n$th-order ODE carries $n$ arbitrary constants and needs $n$ conditions to pin down a unique solution.

**Worked example — verifying a solution and fixing the constant.**

1. Claim: $y=\int 2x\,dx+C=x^2+C$ solves $y'=2x$. *Reason:* differentiate $x^2+C$; by the power rule $\frac{d}{dx}x^2=2x$ and the derivative of a constant is $0$, so $y'=2x$. The equation holds for every $x$, so it is indeed a solution — and a whole family, one curve per value of $C$.
2. Impose $y(1)=5$. *Reason (definition of initial condition):* substitute $x=1,\ y=5$: $\ 5=1^2+C$, so $C=4$.
3. The particular solution is $y=x^2+4$. Check: $y(1)=1+4=5$ ✓ and $y'=2x$ ✓.

#### The whole course on one line

> First-order (separable, linear) → Modeling → Second-order linear → Systems & phase plane → Laplace transform → Series & numerics → PDEs & Fourier

#### Common pitfalls

- Forgetting the $+C$. A first-order answer without an arbitrary constant is only one curve out of infinitely many.
- Confusing "order" (highest derivative) with "degree" (highest power); this guide uses order throughout.
- Calling an equation linear when a term like $y^2$ or $yy'$ is present — those are nonlinear and the linear toolkit of Part B does not apply.

> **Connection — this is calculus, aimed**
>
> You already know how to differentiate and integrate. Differential equations turn that machinery into a tool for prediction: physics, biology, finance and engineering all speak in rates of change, so their laws are differential equations. Learning to solve them is learning to run the laws forward in time.

<a id="s1"></a>
### Slope fields, solution curves & separable equations

#### What this section says, in one breath

Before any formula you can *see* a first-order equation. Writing it as $y'=f(x,y)$ means: at every point of the plane the equation tells you a slope. Draw a tiny segment with that slope at each point and you get a field of arrows; the solutions are exactly the curves that flow along the arrows. The **separable** equations are the subclass we can solve by splitting the two variables onto opposite sides and integrating each.

#### Every term, defined from zero

- The **$xy$-plane** is the set of all points $(x,y)$; the horizontal coordinate is the input $x$, the vertical is the output $y$.
- A **slope** is the steepness of a line, "rise over run." A line through a point with slope $m$ rises $m$ units for each $1$ unit moved right.
- $f(x,y)$ means a formula that may use **both** coordinates of a point.

> **Concept — the slope field**
>
> An equation $y'=f(x,y)$ assigns to each point $(x,y)$ the number $f(x,y)$, and we *interpret that number as the slope a solution must have there*. Drawing a short segment of that slope at many points produces the **slope field** (also called direction field). A **solution curve** is a curve that is tangent to the field everywhere — at each of its points its own slope equals the prescribed $f(x,y)$. This geometric picture exists even when no algebraic formula for the solution does, and an **initial point** $(x_0,y_0)$ picks out exactly one curve threading through the field (this is the existence/uniqueness story of §s5).

> **Definition — separable equation**
>
> A first-order ODE is **separable** when its right side factors into a function of $x$ alone times a function of $y$ alone:
> $$\frac{dy}{dx}=g(x)\,h(y).$$
> Here $g(x)$ uses only the input and $h(y)$ uses only the output.

**Statement of the method.**

$$\frac{dy}{dx}=g(x)\,h(y)\ \Longrightarrow\ \int\frac{dy}{h(y)}=\int g(x)\,dx+C.$$

In words: collect everything with a $y$ (including the $dy$) on the left, everything with an $x$ on the right, then integrate each side. Watch for **constant solutions**: any $y^*$ with $h(y^*)=0$ makes $y'=0$, so $y\equiv y^*$ is a flat solution that the division step would hide.

**Derivation — why "separating" is legitimate.** The phrase "multiply both sides by $dx$" looks like illegal symbol-pushing; here is the honest justification.

1. Start from $\dfrac{dy}{dx}=g(x)\,h(y)$ and assume $h(y)\ne0$ on the interval of interest. Divide both sides by $h(y)$:
   $$\frac{1}{h(y)}\frac{dy}{dx}=g(x).$$
   *Reason:* dividing both sides of a true equation by the same nonzero quantity keeps it true.
2. Integrate both sides with respect to $x$:
   $$\int \frac{1}{h(y)}\frac{dy}{dx}\,dx=\int g(x)\,dx.$$
   *Reason:* if two functions of $x$ are equal everywhere, their antiderivatives agree up to a constant.
3. On the left, apply the **substitution rule** (the chain rule run backward): since $\dfrac{dy}{dx}\,dx$ is the differential $dy$, the integral $\int \frac{1}{h(y)}\frac{dy}{dx}\,dx$ equals $\int \frac{1}{h(y)}\,dy$.
   $$\int \frac{dy}{h(y)}=\int g(x)\,dx+C.$$
   *Reason:* substitution states $\int F(y)\frac{dy}{dx}\,dx=\int F(y)\,dy$; here $F(y)=1/h(y)$. The single constant $C$ absorbs the constants from both sides.

So separation is exactly the substitution rule; nothing illegal happened.

**Demonstration — solving a separable initial-value problem.**

1. Solve $\dfrac{dy}{dx}=\dfrac{x}{y}$ with $y(0)=3$. The right side is $x\cdot\frac1y$, a product of an $x$-part and a $y$-part, so it is separable with $g(x)=x,\ h(y)=1/y$. Separate by multiplying both sides by $y$ (the "$dx$" form):
   $$y\,dy = x\,dx.$$
   *Reason:* multiply $\frac{dy}{dx}=\frac{x}{y}$ by $y\,dx$.
2. Integrate both sides, using the power rule $\int t\,dt=\tfrac12 t^2$ on each:
   $$\int y\,dy=\int x\,dx \ \Longrightarrow\ \tfrac12 y^2=\tfrac12 x^2+C_1.$$
3. Multiply by $2$ and rename the constant ($C:=2C_1$, still arbitrary):
   $$y^2 = x^2 + C.$$
4. Apply $y(0)=3$. *Reason (definition of initial condition):* substitute $x=0,\ y=3$: $\,9=0+C$, so $C=9$ and
   $$y=\sqrt{x^2+9}\quad(\text{positive root, to match }y(0)=3>0).$$
   We take the positive square root because $y(0)=3$ is positive and a solution curve cannot jump signs.

The general solution $y^2-x^2=C$ is a family of hyperbolas; the initial condition selects one branch. Pitfall: had $h(y)=1/y$ been written as $h(y)=y$ we would have looked for $h(y^*)=0$ at $y^*=0$ — but $y=0$ makes the original right side undefined, so it is excluded rather than a constant solution.

<a id="s2"></a>
### First-order linear equations & the integrating factor

#### What this section says, in one breath

This is the most important first-order class. A first-order **linear** equation can always be solved by multiplying through by one cleverly chosen function — the **integrating factor** — which turns the entire left side into the derivative of a single product. After that, one integration finishes the job.

#### Every term, defined from zero

- **Standard form** of a first-order linear ODE is the arrangement where the coefficient of $y'$ is exactly $1$:
  $$\frac{dy}{dx}+P(x)\,y = Q(x).$$
  $P(x)$ is whatever multiplies $y$; $Q(x)$ is everything with no $y$. You must reach this form *before* reading off $P$ and $Q$.
- The **product rule** of differentiation: $(uv)'=u'v+uv'$ for any two differentiable functions $u,v$.
- $e$ is Euler's number ($\approx 2.71828$); $e^{(\cdots)}$ is the exponential function, the unique function equal to its own derivative: $\frac{d}{dx}e^{x}=e^{x}$.

> **Definition — integrating factor**
>
> The **integrating factor** for $\dfrac{dy}{dx}+P(x)y=Q(x)$ is
> $$\mu(x)=e^{\int P(x)\,dx}.$$
> Multiplying the equation by $\mu$ makes the left side collapse to $(\mu y)'$, a single derivative.

**Statement of the solution formula.**

$$y=\frac{1}{\mu(x)}\!\left(\int \mu(x)\,Q(x)\,dx + C\right).$$

**Derivation — where $\mu=e^{\int P\,dx}$ comes from.**

1. We want a multiplier $\mu(x)$ so that after multiplying, the left side $\mu y' + \mu P y$ equals the derivative of the product $\mu y$. By the **product rule** (restated above), $(\mu y)'=\mu y'+\mu' y$.
2. Compare $\mu y'+\mu P y$ with $\mu y'+\mu' y$. The $\mu y'$ terms already match; matching the coefficient of $y$ requires
   $$\mu' = \mu P.$$
   *Reason:* two expressions are identically equal only if the coefficients of $y$ agree.
3. This little equation for $\mu$ is itself **separable** (§s1): write $\frac{d\mu}{\mu}=P\,dx$ and integrate both sides.
   $$\ln|\mu| = \int P\,dx \ \Longrightarrow\ \mu=e^{\int P\,dx}.$$
   *Reason:* $\int \frac{d\mu}{\mu}=\ln|\mu|$ by the definition of the natural logarithm as the antiderivative of $1/\mu$; then exponentiate both sides to undo the $\ln$. We may drop the absolute value and any constant of integration because we only need *one* working multiplier.
4. With this $\mu$, the equation becomes $(\mu y)'=\mu Q$. Integrate once:
   $$\mu y=\int \mu Q\,dx + C,$$
   and divide by $\mu$ to get the boxed formula. *Reason:* integrating a derivative recovers the function, by the Fundamental Theorem of Calculus.

**Demonstration — a worked linear equation.**

1. Solve $x y' + 2y = x^3$. First reach standard form by dividing every term by $x$ (allowed since we work where $x\ne0$):
   $$y' + \frac{2}{x}\,y = x^2,\qquad P(x)=\frac{2}{x},\ Q(x)=x^2.$$
2. Compute the integrating factor. *Reason:* $\int \frac2x\,dx=2\ln|x|$, and $e^{2\ln|x|}=(e^{\ln|x|})^2=|x|^2=x^2$.
   $$\mu=e^{\int (2/x)\,dx}=e^{2\ln|x|}=x^2.$$
3. Multiply the standard-form equation by $\mu=x^2$. The left side becomes $(x^2 y)'$ by construction, and the right becomes $x^2\cdot x^2=x^4$:
   $$(x^2 y)' = x^4.$$
   Integrate both sides ($\int x^4\,dx=\tfrac{x^5}{5}$):
   $$x^2 y = \frac{x^5}{5}+C.$$
4. Solve for $y$ by dividing by $x^2$:
   $$y=\frac{x^3}{5}+\frac{C}{x^2}.$$

**Numeric check.** Take $C=0$, so $y=x^3/5$. Then $y'=3x^2/5$ and $xy'+2y=x\cdot\tfrac{3x^2}{5}+2\cdot\tfrac{x^3}{5}=\tfrac{3x^3+2x^3}{5}=x^3$ ✓. The $C/x^2$ piece is the solution of the **homogeneous** part $y'+\tfrac2x y=0$ (set $Q=0$); the $x^3/5$ is one **particular** response to $Q=x^2$.

> **Connection — superposition appears early**
>
> The answer splits as *homogeneous* $+$ *particular* — the same structure that will organize all of Part B (§s7–§s11). The integrating factor is the first-order shadow of the broader linear theory.

<a id="s3"></a>
### Exact equations

#### What this section says, in one breath

Some first-order equations are secretly the total differential of a hidden two-variable function $F(x,y)$. If we can recognize this, the solutions are simply the level curves $F(x,y)=C$, and we recover $F$ by integration.

#### Every term, defined from zero

- A **two-variable function** $F(x,y)$ outputs one number from a pair of inputs.
- A **partial derivative** $F_x=\dfrac{\partial F}{\partial x}$ is the rate of change of $F$ as $x$ varies while $y$ is held fixed; $F_y$ holds $x$ fixed instead.
- The **total differential** of $F$ is $dF=F_x\,dx+F_y\,dy$: the small change in $F$ produced by small changes $dx$ and $dy$.
- A **level curve** $F(x,y)=C$ is the set of points where $F$ takes a fixed value $C$; along it $dF=0$.
- **Clairaut's theorem** (equality of mixed partials): if $F$ has continuous second partials then $F_{xy}=F_{yx}$ — differentiating in $x$ then $y$ gives the same result as $y$ then $x$.

> **Definition — exact equation**
>
> Write a first-order ODE in the symmetric form $M(x,y)\,dx+N(x,y)\,dy=0$. It is **exact** when this left side is the total differential $dF$ of some function $F$, i.e. when $F_x=M$ and $F_y=N$ for some $F$.

**Statement — exactness test and solution.**

$$M(x,y)\,dx+N(x,y)\,dy=0 \ \text{ is exact} \iff \frac{\partial M}{\partial y}=\frac{\partial N}{\partial x}.$$

$$\text{Then } \exists\,F:\ F_x=M,\ F_y=N,\quad\text{and the solution is}\quad F(x,y)=C.$$

**Derivation — why the test $M_y=N_x$ detects exactness.**

1. Suppose the equation is exact, so $F_x=M$ and $F_y=N$ for some $F$ with continuous second partials.
2. Differentiate $F_x=M$ with respect to $y$: $F_{xy}=M_y$. Differentiate $F_y=N$ with respect to $x$: $F_{yx}=N_x$.
   *Reason:* differentiate equal functions by the same variable to keep equality.
3. By **Clairaut's theorem** $F_{xy}=F_{yx}$, hence $M_y=N_x$. So exactness *forces* the test to pass.
4. Conversely, when $M_y=N_x$ on a region with no holes, one can construct $F$ by the integration procedure below; the equality is exactly the consistency condition that makes the construction succeed.

**Derivation — why $F=C$ solves the equation.** Along any solution curve, $y$ is a function of $x$, so $F$ becomes a function of $x$ alone. By the chain rule $\frac{d}{dx}F(x,y(x))=F_x+F_y\frac{dy}{dx}=M+N\frac{dy}{dx}$. The ODE says $M+N\frac{dy}{dx}=0$ (divide $M\,dx+N\,dy=0$ by $dx$), so $\frac{dF}{dx}=0$, meaning $F$ is constant along the curve. Hence $F(x,y)=C$.

**Demonstration — testing and solving an exact equation.**

1. Solve $(2xy+3)\,dx+(x^2-1)\,dy=0$. Read off $M=2xy+3,\ N=x^2-1$.
2. Apply the test. *Reason:* $M_y$ differentiates $2xy+3$ in $y$ (treat $x$ as constant) giving $2x$; $N_x$ differentiates $x^2-1$ in $x$ giving $2x$.
   $$M_y=2x,\qquad N_x=2x.$$
   They are equal, so the equation is exact.
3. Recover $F$ by integrating $F_x=M$ in $x$, holding $y$ constant. The "constant" of integration may depend on $y$, so call it $g(y)$:
   $$F=\int(2xy+3)\,dx = x^2 y+3x+g(y).$$
4. Pin down $g$ by enforcing $F_y=N$. Differentiate the line above in $y$: $F_y=x^2+g'(y)$. Set equal to $N=x^2-1$:
   $$x^2+g'(y)=x^2-1\ \Rightarrow\ g'(y)=-1\ \Rightarrow\ g(y)=-y.$$
5. Therefore $F=x^2y+3x-y$ and the implicit solution is
   $$x^2 y + 3x - y = C.$$

**Numeric check.** Differentiate $F=x^2y+3x-y$ implicitly: $dF=(2xy+3)\,dx+(x^2-1)\,dy$, which is exactly the original left side, confirming exactness. When $M_y\ne N_x$ one can sometimes restore exactness by multiplying by an integrating factor $\mu$ — the same idea as §s2, generalized to two variables.

> **Connection — Clairaut's theorem is the engine**
>
> The test $M_y=N_x$ is literally the equality of mixed partials $F_{xy}=F_{yx}$. Exact equations are vector calculus in disguise: $M\,dx+N\,dy$ is exact iff the field $(M,N)$ is **conservative**, with $F$ its **potential** function.

<a id="s4"></a>
### Substitutions: homogeneous & Bernoulli equations

#### What this section says, in one breath

When an equation is neither separable nor linear, the right *change of variable* can convert it into one that is. Two classic substitutions cover a wide range: $v=y/x$ for homogeneous equations and $v=y^{1-n}$ for Bernoulli equations.

#### Every term, defined from zero

- A **substitution** (change of variable) replaces the unknown $y$ by a new unknown $v$ related to it, hoping the equation for $v$ is easier. After solving for $v$ you translate back.
- A function $F(y/x)$ depends on $x$ and $y$ only through their **ratio** $y/x$.

> **Definition — homogeneous (ratio) equation**
>
> A first-order ODE is **homogeneous** in this sense when it can be written
> $$\frac{dy}{dx}=F\!\left(\frac{y}{x}\right).$$
> The substitution is $v=\dfrac{y}{x}$, so $y=vx$ and, by the **product rule**, $\dfrac{dy}{dx}=v+x\dfrac{dv}{dx}$.

**Why the substitution always separates.** Substituting gives $v+x\frac{dv}{dx}=F(v)$, hence $x\frac{dv}{dx}=F(v)-v$, i.e. $\frac{dv}{F(v)-v}=\frac{dx}{x}$ — a separable equation in $v$ and $x$ (§s1).

> **Definition — Bernoulli equation**
>
> A **Bernoulli equation** has the form
> $$\frac{dy}{dx}+P(x)\,y = Q(x)\,y^{n}\qquad(n\ne 0,1),$$
> nonlinear because of the power $y^n$. The substitution $v=y^{1-n}$ turns it linear:
> $$\frac{dv}{dx}+(1-n)P(x)\,v=(1-n)Q(x).$$

**Derivation — why $v=y^{1-n}$ linearizes Bernoulli.**

1. Differentiate $v=y^{1-n}$ using the chain rule: $v'=(1-n)y^{-n}y'$.
2. Divide the Bernoulli equation by $y^n$: $y^{-n}y'+P\,y^{1-n}=Q$. *Reason:* dividing by the nonzero quantity $y^n$.
3. Recognize the pieces: $y^{-n}y'=\frac{v'}{1-n}$ (from step 1) and $y^{1-n}=v$. Substitute:
   $$\frac{v'}{1-n}+P\,v=Q.$$
4. Multiply by $(1-n)$ to get the linear equation $v'+(1-n)P\,v=(1-n)Q$, solvable by the integrating factor of §s2.

**Demonstration — solving a Bernoulli equation.**

1. Solve $y'+\dfrac{1}{x}y = x y^2$. Here $P=1/x,\ Q=x,\ n=2$, so set $v=y^{1-2}=y^{-1}$; then $v'=-y^{-2}y'$.
2. Divide by $y^2$: $\,y^{-2}y' + \tfrac1x y^{-1} = x$. Replace $y^{-2}y'=-v'$ and $y^{-1}=v$:
   $$-v' + \frac1x v = x \ \Longrightarrow\ v' - \frac1x v = -x.$$
   *Reason:* multiply through by $-1$ to put $v'$ alone with a $+$ sign.
3. This is linear with $P_{\text{new}}=-\tfrac1x$. Integrating factor $\mu=e^{-\int dx/x}=e^{-\ln|x|}=x^{-1}$. Multiply through; the left becomes $(x^{-1}v)'$ and the right $x^{-1}\cdot(-x)=-1$:
   $$(x^{-1}v)'=-1\ \Rightarrow\ x^{-1}v=-x+C\ \Rightarrow\ v=-x^2+Cx.$$
4. Return to $y$ via $y=1/v$:
   $$y=\frac{1}{Cx-x^2}.$$

**Numeric check.** Take $C=2$, so $y=1/(2x-x^2)$. At $x=1$: $y=1/(2-1)=1$. Compute $y'=-\frac{(2-2x)}{(2x-x^2)^2}$; at $x=1$, $y'=-\frac{0}{1}=0$. The equation predicts $y'=xy^2-\tfrac1x y=1\cdot1-1\cdot1=0$ ✓.

> **Connection — a recurring strategy**
>
> "Find the substitution that flattens the nonlinearity" returns throughout: $v=y/x$ here, $v=y^{1-n}$ for Bernoulli, reduction of order in §s8, and the moving frame of the phase plane in §s12.

<a id="s5"></a>
### Existence, uniqueness & autonomous equations (stability)

#### What this section says, in one breath

Before solving, two questions matter: does a solution exist at all, and is it the *only* one? A theorem answers both from continuity conditions. And for equations that do not depend on $x$ explicitly — **autonomous** equations — we can read off long-term behavior without ever solving.

#### Every term, defined from zero

- A function is **continuous** if its graph has no jumps or breaks — small input changes give small output changes.
- **Existence** means at least one solution through the given starting point exists; **uniqueness** means there is exactly one.
- An **autonomous** equation has the form $y'=f(y)$: the rate depends on the current value $y$ but not directly on $x$ (or $t$).
- An **equilibrium** (or critical point) $y^*$ is a value where $f(y^*)=0$, so $y'=0$ and the constant function $y\equiv y^*$ is a solution.

> **Theorem — Picard–Lindelöf (existence & uniqueness)**
>
> For the IVP $y'=f(x,y),\ y(x_0)=y_0$: if $f$ and its partial derivative $\dfrac{\partial f}{\partial y}$ are both continuous in a rectangle around $(x_0,y_0)$, then a **unique** solution exists on some interval around $x_0$.
> $$y'=f(x,y),\ y(x_0)=y_0:\quad \text{if } f \text{ and } \frac{\partial f}{\partial y}\text{ are continuous near }(x_0,y_0),$$
> then a unique solution exists locally. Continuity of $f$ alone already guarantees existence; continuity of $f_y$ adds uniqueness.

> **Concept — why uniqueness can fail**
>
> Consider $y'=\sqrt{y},\ y(0)=0$. Two different functions both satisfy it: the flat $y\equiv0$ and the parabola $y=\tfrac14 x^2$ (check: $y'=\tfrac12 x$ and $\sqrt{y}=\sqrt{x^2/4}=x/2$ for $x\ge0$ ✓). Uniqueness broke because $f_y=\tfrac1{2\sqrt y}$ blows up at $y=0$, violating the theorem's hypothesis. Where the hypotheses hold, distinct solution curves can never touch or cross — that is the geometric content of uniqueness.

**Statement — equilibria and their stability for $y'=f(y)$.**

$$\frac{dy}{dx}=f(y):\quad \text{equilibria are roots } f(y^*)=0.$$

$$f'(y^*)<0\Rightarrow\text{stable (sink)},\qquad f'(y^*)>0\Rightarrow\text{unstable (source)}.$$

A **phase line** is the $y$-axis marked with the sign of $f$: where $f(y)>0$ draw an up-arrow (solutions increase), where $f(y)<0$ a down-arrow. Arrows pointing *toward* an equilibrium mark it **stable**; *away*, **unstable**.

**Derivation — the linearization test.**

1. Let $y^*$ be an equilibrium and look at a nearby solution $y=y^*+\varepsilon$, where $\varepsilon$ is a small deviation. Then $y'=\varepsilon'$ since $y^*$ is constant.
2. Expand $f$ near $y^*$ using the **tangent-line (first-order Taylor) approximation**: $f(y^*+\varepsilon)\approx f(y^*)+f'(y^*)\varepsilon$. Since $f(y^*)=0$, this is $f'(y^*)\varepsilon$.
3. Therefore $\varepsilon'\approx f'(y^*)\,\varepsilon$. By §s6 this linear equation has solution $\varepsilon=\varepsilon_0 e^{f'(y^*)x}$.
   *Reason:* $y'=ky$ solves to $y=y_0e^{kx}$ (proved in §s6).
4. If $f'(y^*)<0$ the exponential decays, $\varepsilon\to0$, the deviation shrinks — **stable**. If $f'(y^*)>0$ it grows — **unstable**.

**Demonstration — stability by linearization.**

1. Take $y'=y(1-y)=y-y^2$, so $f(y)=y-y^2$. Equilibria: $f(y)=y(1-y)=0$ at $y^*=0$ and $y^*=1$.
2. Compute $f'(y)=1-2y$. Evaluate at each equilibrium:
   $$f'(0)=1>0\ (\text{unstable}),\qquad f'(1)=-1<0\ (\text{stable}).$$
3. Conclusion: any positive start drifts away from $0$ and toward $1$. So $y=1$ is the **carrying capacity** — the logistic story of §s6.

**Numeric check of the phase line.** At $y=0.5$, $f=0.5(1-0.5)=0.25>0$, so $y$ increases toward $1$ ✓. At $y=1.5$, $f=1.5(1-1.5)=-0.75<0$, so $y$ decreases toward $1$ ✓. Both arrows point at $y=1$: stable, exactly as the derivative test said.

<a id="s6"></a>
### Modeling: growth/decay, mixing, cooling, the logistic equation

#### What this section says, in one breath

This is the payoff of Part A: real-world phenomena translate into first-order ODEs, and the methods above solve them. Modeling is the craft of writing "rate of change $=$ ..." correctly, then turning the crank.

#### Every term, defined from zero

- A **rate constant** $k$ measures how fast a process runs; its sign decides growth ($k>0$) versus decay ($k<0$).
- **Half-life** $t_{1/2}$ is the time for a decaying quantity to fall to half its value.
- **Carrying capacity** $K$ is the population a logistic environment can sustain long-term.

**Statement — exponential growth/decay and Newton's law of cooling.**

$$\frac{dy}{dt}=ky \ \Rightarrow\ y=y_0 e^{kt},\qquad \frac{dT}{dt}=-k\,(T-T_{\text{env}}) \ \Rightarrow\ T=T_{\text{env}}+(T_0-T_{\text{env}})e^{-kt}.$$

Here $y_0=y(0)$ is the initial amount, $T$ is temperature, $T_{\text{env}}$ the surrounding temperature, $T_0=T(0)$.

**Derivation — solving $y'=ky$.**

1. $y'=ky$ is separable (§s1): $\frac{dy}{y}=k\,dt$.
2. Integrate: $\ln|y|=kt+C_1$. *Reason:* $\int\frac{dy}{y}=\ln|y|$, $\int k\,dt=kt$.
3. Exponentiate: $|y|=e^{kt+C_1}=e^{C_1}e^{kt}$. Absorb $\pm e^{C_1}$ into a single constant $y_0$: $y=y_0e^{kt}$.
4. Check the initial value: at $t=0$, $y=y_0e^0=y_0$ ✓. The **half-life** follows from $\tfrac12 y_0=y_0e^{kt_{1/2}}$, giving $e^{kt_{1/2}}=\tfrac12$, so $t_{1/2}=\ln2/|k|$.

> **Definition — the logistic equation**
>
> The **logistic equation** caps exponential growth at a carrying capacity $K$:
> $$\frac{dP}{dt}=rP\!\left(1-\frac{P}{K}\right)\ \Longrightarrow\ P(t)=\frac{K}{1+A e^{-rt}},\quad A=\frac{K-P_0}{P_0}.$$
> $r$ is the **intrinsic growth rate** (the per-capita rate when $P$ is tiny), $K$ the carrying capacity, $P_0=P(0)$.

**Derivation — solving the logistic equation by partial fractions.**

1. Separate: $\dfrac{dP}{P(1-P/K)}=r\,dt$.
2. Split the left integrand by **partial fractions**. We claim $\dfrac{1}{P(1-P/K)}=\dfrac1P+\dfrac{1/K}{1-P/K}$. *Check:* common denominator gives $\frac{(1-P/K)+(P/K)}{P(1-P/K)}=\frac{1}{P(1-P/K)}$ ✓.
3. Integrate each piece: $\int\frac{dP}{P}=\ln|P|$ and $\int\frac{(1/K)\,dP}{1-P/K}=-\ln|1-P/K|$ (substitution $w=1-P/K$). So $\ln\left|\frac{P}{1-P/K}\right|=rt+C$.
4. Exponentiate and solve for $P$. Writing $A=e^{-C}$ and applying $P(0)=P_0$ to get $A=\frac{K-P_0}{P_0}$ yields the boxed $P(t)=\frac{K}{1+Ae^{-rt}}$. As $t\to\infty$, $e^{-rt}\to0$ and $P\to K$ — the stable equilibrium of §s5.

**Demonstration — a mixing (tank) problem.**

1. A $100$ L tank holds pure water. Brine at $2$ g/L flows in at $5$ L/min; the well-stirred mixture flows out at $5$ L/min. Let $S(t)$ be grams of salt. Rate in $=(2\text{ g/L})(5\text{ L/min})=10$ g/min. Concentration in the tank is $S/100$ g/L, so rate out $=\frac{S}{100}\cdot5=\frac{S}{20}$ g/min.
2. **Balance law** (rate of change $=$ rate in $-$ rate out) gives a linear ODE:
   $$\frac{dS}{dt}=10-\frac{S}{20},\qquad S(0)=0.$$
3. Standard form $S'+\tfrac1{20}S=10$. Integrating factor $\mu=e^{\int (1/20)\,dt}=e^{t/20}$ (§s2). Multiply through:
   $$(e^{t/20}S)'=10\,e^{t/20}\ \Rightarrow\ e^{t/20}S=10\cdot 20\,e^{t/20}+C=200\,e^{t/20}+C.$$
   *Reason:* $\int 10 e^{t/20}\,dt=10\cdot20\,e^{t/20}=200e^{t/20}$.
4. So $S=200+Ce^{-t/20}$. Apply $S(0)=0$: $0=200+C$, giving $C=-200$:
   $$S(t)=200\big(1-e^{-t/20}\big).$$

**Numeric check.** At $t=0$: $S=200(1-1)=0$ ✓. As $t\to\infty$: $S\to200$ g, i.e. $200/100=2$ g/L throughout — exactly the inflow concentration, as intuition demands. At $t=20$ min: $S=200(1-e^{-1})\approx200(0.6321)=126.4$ g.

> **Connection — the logistic solution comes from partial fractions**
>
> The S-curve owes its shape to the algebra of **partial fractions** (step 2 above), the same technique used to evaluate integrals in a first calculus course. Integration, algebra, and modeling are one toolkit.

## Part B · Second-order linear equations

<a id="s7"></a>
### Linear ODE theory: superposition, independence & the Wronskian

#### What this section says, in one breath

Second-order linear equations have a complete structure borrowed from linear algebra: their solutions form a **vector space**, and a **basis** of just two functions describes all of them. The **Wronskian** is the determinant that checks whether two solutions form such a basis.

#### Every term, defined from zero

- A **vector space** is a collection of objects (here, functions) that can be added and scaled by numbers, with the results staying in the collection.
- A **linear combination** of $y_1,y_2$ is $c_1 y_1+c_2 y_2$ for constants $c_1,c_2$.
- Functions $y_1,y_2$ are **linearly independent** if the only way $c_1y_1+c_2y_2=0$ for all $x$ is $c_1=c_2=0$ — neither is a constant multiple of the other.
- A **basis** of a 2-dimensional space is a pair of independent elements; every element is a unique linear combination of them.
- A $2\times2$ **determinant** is $\begin{vmatrix}a&b\\c&d\end{vmatrix}=ad-bc$; it is zero exactly when the columns are proportional.

**Statement — the linear second-order equation.**

$$y''+p(x)\,y'+q(x)\,y=g(x).$$

If $g\equiv0$ the equation is **homogeneous**; otherwise **nonhomogeneous**. With $p,q,g$ continuous, every IVP $y(x_0)=a,\ y'(x_0)=b$ has a unique solution (the second-order existence/uniqueness theorem).

> **Principle — superposition & the solution structure**
>
> For the homogeneous equation, any linear combination of solutions is again a solution. The general solution is $y=c_1 y_1+c_2 y_2$ for two **linearly independent** solutions $y_1,y_2$. For the nonhomogeneous equation, the general solution is $y=y_h+y_p$: the full homogeneous family $y_h$ plus any one **particular** solution $y_p$.

**Derivation — superposition.**

1. Let $y_1,y_2$ solve the homogeneous equation $L[y]:=y''+py'+qy=0$, and form $y=c_1y_1+c_2y_2$.
2. The operator $L$ is **linear**: $L[c_1y_1+c_2y_2]=c_1L[y_1]+c_2L[y_2]$. *Reason:* differentiation is linear (the derivative of a sum is the sum of derivatives, constants pull out), and $L$ is built from derivatives.
3. Since $L[y_1]=0$ and $L[y_2]=0$, we get $L[y]=c_1\cdot0+c_2\cdot0=0$. Hence $y$ solves the homogeneous equation. ∎

**Derivation — why the nonhomogeneous general solution is $y_h+y_p$.** If $y$ and $y_p$ both satisfy $L[y]=g$, then $L[y-y_p]=L[y]-L[y_p]=g-g=0$, so $y-y_p$ is a homogeneous solution $y_h$. Therefore $y=y_h+y_p$.

**Statement — the Wronskian.**

$$W(y_1,y_2)=\begin{vmatrix} y_1 & y_2\\ y_1' & y_2'\end{vmatrix}=y_1 y_2'-y_2 y_1'.$$

For two solutions of the *same* linear ODE, $W\ne0$ at one point $\iff y_1,y_2$ are linearly independent (a **fundamental set**). **Abel's theorem** says $W(x)=W(x_0)\,e^{-\int p\,dx}$, so $W$ is either always zero or never zero.

**Derivation — nonzero Wronskian implies independence.**

1. Suppose $c_1y_1+c_2y_2=0$ for all $x$. Differentiate: $c_1y_1'+c_2y_2'=0$ for all $x$ too.
2. At a fixed point this is a $2\times2$ linear system in $(c_1,c_2)$ with coefficient matrix $\begin{pmatrix}y_1&y_2\\y_1'&y_2'\end{pmatrix}$, whose determinant is $W$.
3. If $W\ne0$ the matrix is invertible, so the only solution is $c_1=c_2=0$. *Reason:* a square system with nonzero determinant has only the trivial solution. Hence $y_1,y_2$ are independent. ∎

**Demonstration — independence via the Wronskian.**

1. Are $y_1=e^{x}$ and $y_2=e^{2x}$ independent? Compute $y_1'=e^x,\ y_2'=2e^{2x}$, then
   $$W=\begin{vmatrix} e^{x} & e^{2x}\\ e^{x} & 2e^{2x}\end{vmatrix}=e^x\cdot2e^{2x}-e^{2x}\cdot e^{x}=2e^{3x}-e^{3x}=e^{3x}.$$
2. Since $e^{3x}\ne0$ for every $x$, the functions are linearly independent and form a fundamental set: every solution of their common ODE is $c_1e^x+c_2e^{2x}$.

> **Connection — this is linear algebra**
>
> The solution set of a homogeneous linear ODE is a **vector space**; $y_1,y_2$ are a basis, and "order $n$" means "dimension $n$." The Wronskian is the determinant that tests for a basis — the function-space analog of independence of vectors.

<a id="s8"></a>
### Homogeneous equations with constant coefficients

#### What this section says, in one breath

The workhorse case is when $a,b,c$ are constants. Guessing $y=e^{rx}$ converts the differential equation into a quadratic equation in $r$ — the **characteristic equation** — and the roots of that polynomial dictate the whole solution.

#### Every term, defined from zero

- A **constant-coefficient** equation has number (not function) coefficients: $ay''+by'+cy=0$.
- A **root** of a polynomial is a value making it zero.
- The **discriminant** of $ar^2+br+c$ is $b^2-4ac$; its sign decides whether the two roots are real and distinct, real and repeated, or complex.
- A **complex number** $\alpha+\beta i$ has real part $\alpha$ and imaginary part $\beta$, with $i^2=-1$.
- **Euler's formula**: $e^{i\theta}=\cos\theta+i\sin\theta$.

**Statement — the characteristic equation.**

$$ay''+by'+cy=0\ \xrightarrow{\ y=e^{rx}\ }\ ar^2+br+c=0.$$

**Derivation — where the characteristic equation comes from.**

1. Try $y=e^{rx}$. Then $y'=re^{rx}$ and $y''=r^2e^{rx}$ (chain rule, each derivative pulls down an $r$).
2. Substitute: $a r^2 e^{rx}+b r e^{rx}+c e^{rx}=0$, i.e. $(ar^2+br+c)e^{rx}=0$.
3. Since $e^{rx}\ne0$ for all $x$, divide it out: $ar^2+br+c=0$. So each root $r$ produces a solution $e^{rx}$. ∎

**Statement — the three cases.**

$$\textbf{Distinct real } r_1\ne r_2:\quad y=c_1e^{r_1 x}+c_2e^{r_2 x}.$$

$$\textbf{Repeated } r:\quad y=(c_1+c_2 x)\,e^{r x}.$$

$$\textbf{Complex } r=\alpha\pm\beta i:\quad y=e^{\alpha x}\big(c_1\cos\beta x+c_2\sin\beta x\big).$$

**Derivation — why complex roots give real sinusoids.**

1. If $r=\alpha\pm\beta i$, the raw solutions are $e^{(\alpha+\beta i)x}$ and $e^{(\alpha-\beta i)x}=e^{\alpha x}e^{\pm i\beta x}$.
2. By **Euler's formula**, $e^{\pm i\beta x}=\cos\beta x\pm i\sin\beta x$.
3. Form real linear combinations (allowed by superposition, §s7): adding the two and dividing by $2$ gives $e^{\alpha x}\cos\beta x$; subtracting and dividing by $2i$ gives $e^{\alpha x}\sin\beta x$.
4. These two real solutions are independent (their Wronskian is $\beta e^{2\alpha x}\ne0$), so the general real solution is $e^{\alpha x}(c_1\cos\beta x+c_2\sin\beta x)$. ∎

**Demonstration — all three cases, worked.**

1. **Distinct real.** $y''-5y'+6y=0$: characteristic $r^2-5r+6=(r-2)(r-3)=0$, roots $2,3$, so
   $$y=c_1 e^{2x}+c_2 e^{3x}.$$
2. **Repeated root.** $y''-4y'+4y=0$: $r^2-4r+4=(r-2)^2=0$, root $2$ twice; the second independent solution is $xe^{2x}$ (derived below):
   $$y=(c_1+c_2 x)\,e^{2x}.$$
3. **Complex roots.** $y''+2y'+5y=0$: $r^2+2r+5=0\Rightarrow r=\dfrac{-2\pm\sqrt{4-20}}{2}=\dfrac{-2\pm\sqrt{-16}}{2}=-1\pm2i$. With $\alpha=-1,\beta=2$:
   $$y=e^{-x}\big(c_1\cos 2x+c_2\sin 2x\big).$$

**Numeric check (case 1).** With $y=e^{2x}$: $y''-5y'+6y=4e^{2x}-10e^{2x}+6e^{2x}=0$ ✓.

**Derivation — where $xe^{rx}$ comes from (reduction of order).**

1. With a repeated root $r$, the equation factors as $y''-2ry'+r^2y=0$. One solution is $y_1=e^{rx}$. Seek a second as $y_2=u(x)e^{rx}$ for an unknown function $u$.
2. Compute $y_2'=(u'+ru)e^{rx}$ and $y_2''=(u''+2ru'+r^2u)e^{rx}$ (product and chain rules). Substitute into $y''-2ry'+r^2y=0$ and factor out $e^{rx}$:
   $$\big(u''+2ru'+r^2u\big)-2r\big(u'+ru\big)+r^2u=u''+(2r-2r)u'+(r^2-2r^2+r^2)u=u''.$$
   *Reason:* the $u'$ and $u$ coefficients cancel precisely because $r$ is a double root.
3. So $u''e^{rx}=0\Rightarrow u''=0$, giving $u=c_1+c_2x$. The genuinely new piece is $y_2=xe^{rx}$. ∎

> **Connection — degeneracy and the factor $x$**
>
> A repeated root costs a degree of freedom; multiplying by $x$ restores it — exactly the mechanism behind resonance in §s11, and behind the modification rule in §s9.

<a id="s9"></a>
### Nonhomogeneous: undetermined coefficients

#### What this section says, in one breath

To solve $ay''+by'+cy=g(x)$, first find the homogeneous solution $y_h$ (§s8), then *guess* a particular solution $y_p$ shaped like $g$, plug it in, and solve for the unknown coefficients. The general solution is $y_h+y_p$ (§s7).

#### Every term, defined from zero

- An **ansatz** (educated guess) is a trial form with unknown constants to be determined.
- "**Duplicates a homogeneous solution**" means the guess, or a piece of it, already solves the homogeneous equation, so it contributes $0$ when substituted.

**Statement — the guess table.**

$$g(x)=e^{\alpha x}\ \to\ Ae^{\alpha x};\quad g=\sin\beta x\text{ or }\cos\beta x\ \to\ A\cos\beta x+B\sin\beta x.$$

$$g=\text{polynomial of degree }n\ \to\ A_n x^n+\cdots+A_1 x+A_0.$$

Products and sums of these use products and sums of the corresponding guesses. Determine the coefficients by substituting and matching.

> **Principle — the modification rule**
>
> If your guess already solves the homogeneous equation it contributes nothing on substitution (you would get $0=g$, impossible). **Multiply the guess by $x$** (or $x^2$ for a double root) until no term duplicates a homogeneous solution. This is the same "$x$ rescues a degenerate case" phenomenon as the repeated root of §s8.

**Demonstration — undetermined coefficients, worked.**

1. Solve $y''-3y'+2y=4e^{3x}$. Homogeneous part: $r^2-3r+2=(r-1)(r-2)=0$, so $y_h=c_1e^{x}+c_2e^{2x}$.
2. The forcing is $g=4e^{3x}$ and $\alpha=3$ is **not** a homogeneous root, so the guess $y_p=Ae^{3x}$ does not duplicate $y_h$. Compute $y_p'=3Ae^{3x},\ y_p''=9Ae^{3x}$.
3. Substitute into the left side: $9Ae^{3x}-3(3Ae^{3x})+2(Ae^{3x})=(9A-9A+2A)e^{3x}=2Ae^{3x}$. Set equal to $4e^{3x}$:
   $$2A=4\ \Rightarrow\ A=2,\qquad y_p=2e^{3x}.$$
4. General solution:
   $$y=c_1 e^{x}+c_2 e^{2x}+2e^{3x}.$$

**Numeric check.** With $y_p=2e^{3x}$: $y_p''-3y_p'+2y_p=18e^{3x}-18e^{3x}+4e^{3x}=4e^{3x}$ ✓. Had $g$ been $4e^{2x}$ (a homogeneous root), the modification rule would force the guess $Axe^{2x}$ instead.

<a id="s10"></a>
### Nonhomogeneous: variation of parameters

#### What this section says, in one breath

When $g(x)$ is *not* a tidy exponential, polynomial, or sinusoid (say $\sec x$ or $\ln x$), guessing fails. **Variation of parameters** always works: it replaces the constants in $y_h=c_1y_1+c_2y_2$ by functions $u_1(x),u_2(x)$ and solves for them with two integrals.

#### Every term, defined from zero

- "**Vary the parameters**" means promote the constants $c_1,c_2$ to unknown functions $u_1(x),u_2(x)$.
- **Cramer's rule** solves a $2\times2$ system $\begin{pmatrix}a&b\\c&d\end{pmatrix}\binom{x}{y}=\binom{e}{f}$ via $x=\frac{ed-bf}{ad-bc},\ y=\frac{af-ec}{ad-bc}$.

**Statement — the formula.**

$$y_p=-y_1\!\int\frac{y_2\,g}{W}\,dx + y_2\!\int\frac{y_1\,g}{W}\,dx,\qquad W=W(y_1,y_2).$$

Here $y_1,y_2$ are a fundamental set of the homogeneous equation (§s7), $g$ is the right side in **standard form** (coefficient of $y''$ equal to $1$), and $W$ is their Wronskian.

**Derivation — variation of parameters.**

1. Seek $y_p=u_1 y_1+u_2 y_2$ with $u_1,u_2$ unknown functions. We have two unknowns, so we may impose two equations.
2. Differentiate: $y_p'=u_1'y_1+u_2'y_2+u_1y_1'+u_2y_2'$. **Impose the convenient constraint** $u_1'y_1+u_2'y_2=0$ (our first equation), which removes the $u'$ terms and leaves $y_p'=u_1y_1'+u_2y_2'$.
3. Differentiate again: $y_p''=u_1'y_1'+u_2'y_2'+u_1y_1''+u_2y_2''$. Substitute $y_p,y_p',y_p''$ into $y''+py'+qy=g$ and group:
   $$u_1\underbrace{(y_1''+py_1'+qy_1)}_{=0}+u_2\underbrace{(y_2''+py_2'+qy_2)}_{=0}+(u_1'y_1'+u_2'y_2')=g.$$
   *Reason:* $y_1,y_2$ solve the homogeneous equation, so the bracketed terms vanish. This leaves the **second equation** $u_1'y_1'+u_2'y_2'=g$.
4. Now solve the $2\times2$ system $\begin{cases}u_1'y_1+u_2'y_2=0\\u_1'y_1'+u_2'y_2'=g\end{cases}$ for $u_1',u_2'$ by **Cramer's rule**; the determinant of the coefficient matrix is exactly $W=y_1y_2'-y_2y_1'$:
   $$u_1'=-\frac{y_2\,g}{W},\qquad u_2'=\frac{y_1\,g}{W}.$$
5. Integrate to get $u_1,u_2$ and substitute into $y_p=u_1y_1+u_2y_2$ to obtain the boxed formula. ∎

**Demonstration — applying it to $y''+y=\sec x$.**

1. Homogeneous solutions: $y_1=\cos x,\ y_2=\sin x$ (roots $r=\pm i$). Wronskian $W=\cos x\cdot\cos x-\sin x\cdot(-\sin x)=\cos^2x+\sin^2x=1$.
2. With $g=\sec x=1/\cos x$:
   $$u_1'=-\frac{\sin x\sec x}{1}=-\tan x\Rightarrow u_1=\ln|\cos x|,\qquad u_2'=\frac{\cos x\sec x}{1}=1\Rightarrow u_2=x.$$
   *Reason:* $\int -\tan x\,dx=\ln|\cos x|$ and $\int 1\,dx=x$.
3. Assemble $y_p=u_1\cos x+u_2\sin x$:
   $$y_p=\cos x\,\ln|\cos x|+x\sin x.$$
4. General solution:
   $$y=c_1\cos x+c_2\sin x+\cos x\,\ln|\cos x|+x\sin x.$$

No finite guess could have produced the $\ln|\cos x|$ term — variation of parameters is the universal method. The Wronskian denominator is the determinant of the very system in step 4, so §s7 reappears here.

<a id="s11"></a>
### Applications: mechanical & electrical vibrations, resonance

#### What this section says, in one breath

One constant-coefficient equation $my''+cy'+ky=F(t)$ governs both a mass on a spring and a series RLC circuit. Studying the discriminant cases of §s8 in this physical setting reveals damping, oscillation, and the dramatic phenomenon of **resonance**.

#### Every term, defined from zero

- **Mass** $m$ resists acceleration; **damping** $c$ removes energy (friction, resistance); **stiffness** $k$ pulls back toward equilibrium.
- The **natural frequency** $\omega_0=\sqrt{k/m}$ is how fast the undamped system oscillates on its own.
- **Resonance** is unbounded growth of amplitude when a system is driven exactly at its natural frequency.

**Statement — the vibration equation and its electrical analog.**

$$m y'' + c y' + k y = F(t)\qquad\Longleftrightarrow\qquad L q'' + R q' + \tfrac1C q = E(t).$$

The dictionary: mass $m\leftrightarrow$ inductance $L$; damping $c\leftrightarrow$ resistance $R$; stiffness $k\leftrightarrow$ inverse capacitance $1/C$; displacement $y\leftrightarrow$ charge $q$; force $F\leftrightarrow$ voltage $E$.

**Statement — damping regimes (free vibration, $F=0$).**

$$\omega_0=\sqrt{k/m};\quad c^2-4mk>0:\text{ overdamped},\ =0:\text{ critically damped},\ <0:\text{ underdamped}.$$

These are exactly the three discriminant cases of $mr^2+cr+k=0$ from §s8: two real roots (overdamped, no oscillation), a double root (critically damped, fastest non-oscillating return), and complex roots (underdamped, a decaying oscillation $e^{-(c/2m)t}\cos(\omega_d t-\phi)$).

**Demonstration — pure resonance.**

1. Undamped ($c=0$), driven at the natural frequency: $y''+\omega_0^2 y=F_0\cos\omega_0 t$. The characteristic equation $r^2+\omega_0^2=0$ gives $r=\pm i\omega_0$, so $y_h=c_1\cos\omega_0 t+c_2\sin\omega_0 t$.
2. The forcing $\cos\omega_0 t$ already appears in $y_h$, so by the **modification rule** (§s9) multiply the guess by $t$: $y_p=t(A\cos\omega_0 t+B\sin\omega_0 t)$.
3. Differentiating twice and substituting (the $t\cos,t\sin$ terms cancel against $\omega_0^2$, leaving only the derivative-of-$t$ pieces) matches coefficients to give
   $$y_p=\frac{F_0}{2\omega_0}\,t\,\sin\omega_0 t.$$
4. The explicit factor $t$ means the amplitude $\frac{F_0}{2\omega_0}t$ grows without bound: **resonance**.

**Numeric feel.** With $F_0=1,\omega_0=1$: at $t=10$ the envelope is $\frac{1}{2}\cdot10=5$; at $t=100$ it is $50$ — ten times larger. Driving in step with the natural rhythm pumps energy in every cycle (the wineglass-shattering, marching-soldiers effect).

> **Connection — resonance is the repeated-root $x$ again**
>
> The runaway $t\sin\omega_0 t$ is the same mechanism as the $xe^{rx}$ of a double characteristic root (§s8): when the forcing frequency hits the natural one, the would-be solution degenerates and a factor $t$ appears to restore independence. Adding even a little damping $c>0$ moves the roots off the imaginary axis and caps the amplitude.

## Part C · Systems, transforms & series

<a id="s12"></a>
### Systems of linear ODEs: the eigenvalue method & phase plane

#### What this section says, in one breath

Coupled equations — and any single higher-order equation — can be bundled into one **vector** equation $\mathbf{x}'=A\mathbf{x}$. Its solutions are read straight off the **eigenvalues** and **eigenvectors** of the matrix $A$.

#### Every term, defined from zero

- A **vector** $\mathbf{x}=\binom{x_1}{x_2}$ stacks several unknown functions; $\mathbf{x}'$ differentiates each entry.
- A **matrix** $A$ is a rectangular array of numbers acting on vectors by multiplication.
- An **eigenvector** $\mathbf v\ne0$ of $A$ is a direction $A$ merely stretches: $A\mathbf v=\lambda\mathbf v$. The stretch factor $\lambda$ is its **eigenvalue**.
- $\det(A-\lambda I)$ is the **characteristic polynomial**; its roots are the eigenvalues. $I$ is the identity matrix.

**Statement — the eigenvalue method.**

$$\mathbf{x}'=A\mathbf{x},\quad \text{try } \mathbf{x}=\mathbf{v}\,e^{\lambda t}\ \Rightarrow\ A\mathbf{v}=\lambda\mathbf{v}.$$

$$\mathbf{x}(t)=c_1\mathbf{v}_1 e^{\lambda_1 t}+c_2\mathbf{v}_2 e^{\lambda_2 t}\quad(\text{distinct eigenvalues}).$$

**Derivation — why trying $\mathbf{x}=\mathbf v e^{\lambda t}$ leads to the eigenvalue equation.**

1. Substitute $\mathbf x=\mathbf v e^{\lambda t}$ (with $\mathbf v$ a constant vector) into $\mathbf x'=A\mathbf x$. Differentiate: $\mathbf x'=\lambda\mathbf v e^{\lambda t}$.
2. The right side is $A\mathbf x=A\mathbf v e^{\lambda t}$. Equate: $\lambda\mathbf v e^{\lambda t}=A\mathbf v e^{\lambda t}$.
3. Divide by the nonzero scalar $e^{\lambda t}$: $A\mathbf v=\lambda\mathbf v$ — the **eigenvalue equation**. So $\lambda$ must be an eigenvalue and $\mathbf v$ a matching eigenvector. ∎

**Statement — phase-plane classification by eigenvalues.**

$$\lambda_1,\lambda_2<0:\text{ stable node};\quad >0:\text{ unstable node};\quad \text{opposite signs}:\text{ saddle}.$$

$$\lambda=\alpha\pm\beta i:\ \alpha<0\ \text{stable spiral},\ \alpha>0\ \text{unstable spiral},\ \alpha=0\ \text{center}.$$

**Demonstration — solving a 2×2 system.**

1. Solve $\mathbf{x}'=\begin{pmatrix}1&2\\2&1\end{pmatrix}\mathbf{x}$. The characteristic polynomial is $\det(A-\lambda I)=\det\begin{pmatrix}1-\lambda&2\\2&1-\lambda\end{pmatrix}=(1-\lambda)^2-4=0$.
   *Reason:* $2\times2$ determinant $=ad-bc$. So $(1-\lambda)^2=4\Rightarrow 1-\lambda=\pm2\Rightarrow\lambda=3$ or $\lambda=-1$.
2. For $\lambda=3$: solve $(A-3I)\mathbf v=0$, i.e. $\begin{pmatrix}-2&2\\2&-2\end{pmatrix}\mathbf v=0$. Both rows say $-2v_1+2v_2=0$, so $v_1=v_2$; take $\mathbf v_1=\begin{pmatrix}1\\1\end{pmatrix}$.
3. For $\lambda=-1$: $\begin{pmatrix}2&2\\2&2\end{pmatrix}\mathbf v=0$ gives $v_1=-v_2$; take $\mathbf v_2=\begin{pmatrix}1\\-1\end{pmatrix}$.
4. General solution:
   $$\mathbf{x}(t)=c_1\begin{pmatrix}1\\1\end{pmatrix}e^{3t}+c_2\begin{pmatrix}1\\-1\end{pmatrix}e^{-t}.$$

**Numeric check.** Plug the $\lambda=3$ piece $\mathbf x=\binom{1}{1}e^{3t}$ into the system: $\mathbf x'=3\binom11 e^{3t}$, and $A\binom11 e^{3t}=\binom{1+2}{2+1}e^{3t}=\binom33 e^{3t}=3\binom11 e^{3t}$ ✓. Opposite-sign eigenvalues mark a **saddle**: trajectories rush in along $\mathbf v_2$ (the $e^{-t}$ direction) and out along $\mathbf v_1$ (the $e^{3t}$ direction).

> **Connection — second-order = a 2D system**
>
> Setting $x_1=y,\ x_2=y'$ turns $y''+by'+cy=0$ into $\mathbf{x}'=\begin{pmatrix}0&1\\-c&-b\end{pmatrix}\mathbf{x}$. The characteristic polynomial of this matrix is exactly $r^2+br+c$ from §s8 — the eigenvalue method and the characteristic equation are one and the same computation.

<a id="s13"></a>
### The Laplace transform

#### What this section says, in one breath

The Laplace transform turns calculus into algebra: it converts a function of time $t$ into a function of a new variable $s$, in such a way that **differentiation becomes multiplication**. A differential equation in $t$ becomes an algebraic equation in $s$ that you solve by hand, then invert.

#### Every term, defined from zero

- An **improper integral** $\int_0^\infty(\cdots)\,dt$ means $\lim_{b\to\infty}\int_0^b(\cdots)\,dt$.
- A **transform** maps a whole function to another function; $\mathcal{L}$ is the Laplace operator, $F(s)$ its output.
- The transform is **linear**: $\mathcal{L}\{af+bg\}=aF+bG$.

**Statement — definition and the key derivative property.**

$$\mathcal{L}\{f(t)\}=F(s)=\int_0^\infty e^{-st}f(t)\,dt.$$

$$\mathcal{L}\{f'\}=sF(s)-f(0),\qquad \mathcal{L}\{f''\}=s^2F(s)-sf(0)-f'(0).$$

**Derivation — the derivative rule $\mathcal{L}\{f'\}=sF(s)-f(0)$.**

1. Apply the definition: $\mathcal{L}\{f'\}=\int_0^\infty e^{-st}f'(t)\,dt$.
2. Integrate by parts with $u=e^{-st},\ dv=f'(t)\,dt$, so $du=-se^{-st}\,dt,\ v=f(t)$:
   $$\mathcal{L}\{f'\}=\big[e^{-st}f(t)\big]_0^\infty+s\int_0^\infty e^{-st}f(t)\,dt.$$
   *Reason:* integration by parts $\int u\,dv=uv-\int v\,du$.
3. Assuming $f$ grows slower than $e^{st}$, the boundary term is $0-e^{0}f(0)=-f(0)$, and the remaining integral is $F(s)$. Hence $\mathcal{L}\{f'\}=sF(s)-f(0)$. The $f''$ rule follows by applying this twice. ∎

**Demonstration — computing $\mathcal{L}\{e^{at}\}$ from the definition.**

1. Apply the definition:
   $$\mathcal{L}\{e^{at}\}=\int_0^\infty e^{-st}e^{at}\,dt=\int_0^\infty e^{-(s-a)t}\,dt.$$
2. Integrate, assuming $s>a$ so the exponent is negative and the integral converges:
   $$=\left[\frac{-1}{s-a}e^{-(s-a)t}\right]_0^\infty=0-\left(\frac{-1}{s-a}\right).$$
   *Reason:* as $t\to\infty$ the exponential $\to0$ (since $s-a>0$); at $t=0$ it equals $1$.
3. Therefore
   $$\mathcal{L}\{e^{at}\}=\frac{1}{s-a},\quad s>a.$$

Setting $a=0$ recovers $\mathcal{L}\{1\}=1/s$. The same definite integral builds the rest of the table.

**Transform table (a starter set, each provable from the definition as above).**

$$\mathcal{L}\{1\}=\frac1s,\quad \mathcal{L}\{t\}=\frac1{s^2},\quad \mathcal{L}\{e^{at}\}=\frac1{s-a},\quad \mathcal{L}\{\cos\omega t\}=\frac{s}{s^2+\omega^2},\quad \mathcal{L}\{\sin\omega t\}=\frac{\omega}{s^2+\omega^2}.$$

> **Connection — linearity & partial fractions return**
>
> Like integration, the Laplace transform is **linear**: $\mathcal{L}\{af+bg\}=aF+bG$. Inverting almost always means splitting a rational $F(s)$ by **partial fractions** until each piece matches a table row — the very algebra used for the logistic integral in §s6.

<a id="s14"></a>
### Solving initial-value problems with Laplace; step & impulse inputs

#### What this section says, in one breath

Here is the transform's reason for existing: solve an IVP in three moves — **transform** the whole equation, **solve the algebra** for $Y(s)$, then **invert** to get $y(t)$. It shines exactly where other methods struggle: forcing that switches on suddenly (a **step**) or hits instantaneously (an **impulse**).

#### Every term, defined from zero

- The **Heaviside step function** $u_c(t)$ is $0$ before time $c$ and $1$ after; it switches a term on at $t=c$.
- The **Dirac delta** $\delta(t-c)$ models an instantaneous unit kick concentrated at $t=c$ (a hammer blow, a voltage spike); it satisfies $\int \delta(t-c)\,dt=1$.
- "**Invert**" means apply the inverse transform $\mathcal{L}^{-1}$ to recover the time-domain function.

**Statement — step and impulse functions.**

$$u_c(t)=\begin{cases}0,&t<c\\ 1,&t\ge c\end{cases},\qquad \mathcal{L}\{u_c(t)\}=\frac{e^{-cs}}{s},\qquad \mathcal{L}\{\delta(t-c)\}=e^{-cs}.$$

In words: $u_c$ switches a forcing term on at $t=c$, and its transform carries the tell-tale shift factor $e^{-cs}$; the Dirac delta $\delta$ models an instantaneous kick and transforms to the clean exponential $e^{-cs}$.

**Demonstration — solving an IVP by transform.**

1. Solve $y''+y=0$ with $y(0)=1,\ y'(0)=0$. Transform both sides. *Reason (derivative rule, §s13):* $\mathcal{L}\{y''\}=s^2Y-sy(0)-y'(0)=s^2Y-s$, and $\mathcal{L}\{y\}=Y$.
   $$s^2Y-s+Y=0.$$
2. Solve the algebra for $Y$:
   $$(s^2+1)Y=s\ \Rightarrow\ Y=\frac{s}{s^2+1}.$$
3. Invert using the table row $\mathcal{L}\{\cos\omega t\}=\frac{s}{s^2+\omega^2}$ with $\omega=1$:
   $$y(t)=\cos t.$$

**Numeric check.** $y=\cos t$ gives $y(0)=1,\ y'(0)=-\sin0=0$ ✓, and $y''+y=-\cos t+\cos t=0$ ✓. The initial conditions were baked in from the very first transform — no constants to chase at the end. For step or impulse forcing, the factor $e^{-cs}$ appears in $Y(s)$ and inverts (via the second shifting theorem) into a time-shifted, switched-on response.

<a id="s15"></a>
### Series solutions & the method of Frobenius

#### What this section says, in one breath

When the coefficients $p,q$ are functions of $x$, there may be no elementary formula for the solution. We then build the solution as an infinite **power series** and determine its coefficients one **recurrence** at a time. At nastier (singular) points the **Frobenius** method prepends a factor $x^r$.

#### Every term, defined from zero

- A **power series** $\sum_{n=0}^\infty a_n(x-x_0)^n$ is an "infinite polynomial" in $x-x_0$ with coefficients $a_n$.
- A function is **analytic** at a point if it equals a convergent power series there.
- An **ordinary point** is one where $p,q$ are analytic; a **regular singular point** is a mild kind of bad point where $xp$ and $x^2q$ are still analytic.
- A **recurrence** gives each coefficient in terms of earlier ones.

**Statement — power-series solution about an ordinary point.**

$$y=\sum_{n=0}^\infty a_n (x-x_0)^n,\qquad y'=\sum_{n\ge1} n a_n x^{n-1},\ \ y''=\sum_{n\ge2} n(n-1)a_n x^{n-2}.$$

The recipe: substitute these series, align powers of $x$, and force the coefficient of each $x^n$ to vanish, producing a recurrence for the $a_n$.

**Demonstration — series solution of $y'=y$.**

1. Assume $y=\sum_{n\ge0}a_n x^n$. Differentiate term by term: $y'=\sum_{n\ge1} n a_n x^{n-1}$. Re-index by $m=n-1$ to align powers: $y'=\sum_{n\ge0}(n+1)a_{n+1}x^{n}$.
   *Reason:* term-by-term differentiation is legitimate inside the radius of convergence.
2. Set $y'=y$ and match the coefficient of $x^n$ on each side: $(n+1)a_{n+1}=a_n$, i.e. the recurrence
   $$a_{n+1}=\frac{a_n}{n+1}.$$
3. Iterate from $a_0$: $a_1=a_0,\ a_2=a_0/2,\ a_3=a_0/(3!),\dots$, so $a_n=\dfrac{a_0}{n!}$. Hence
   $$y=a_0\sum_{n\ge0}\frac{x^n}{n!}=a_0 e^{x}.$$
   *Reason:* the series $\sum x^n/n!$ is the definition of $e^x$.

**Numeric check.** With $a_0=1$, the partial sum $1+1+\tfrac12+\tfrac16=2.6\overline{6}$ already approximates $e=2.71828\ldots$; adding $\tfrac1{24}$ gives $2.7083$. The method rediscovers $e^x$ — reassuring — and works identically when no closed form exists (Airy, Hermite, Bessel functions).

**Statement — Frobenius at a regular singular point.**

$$y=x^{r}\sum_{n=0}^\infty a_n x^{n},\qquad \text{indicial equation}\ r(r-1)+p_0 r+q_0=0.$$

At a regular singular point, prepend the factor $x^r$. The two roots $r$ of the **indicial equation** (where $p_0,q_0$ are the leading coefficients of $xp$ and $x^2q$) give the leading behavior; they generate Bessel and Legendre functions, central to physics.

> **Connection — this is the Taylor series, solved for**
>
> A power-series solution is just a **Taylor series** whose coefficients are unknown until the ODE pins them down. Differentiating a series term-by-term — legitimate inside its radius of convergence — is the calculus that makes the recurrence possible.

<a id="s16"></a>
### Numerical methods: Euler, improved Euler & Runge–Kutta

#### What this section says, in one breath

Most differential equations cannot be solved in closed form. **Numerical methods** march the solution forward in small steps of size $h$, computing approximate values $y_0,y_1,y_2,\dots$ at $x_0,x_0+h,x_0+2h,\dots$ They trade exactness for universality.

#### Every term, defined from zero

- The **step size** $h$ is the horizontal distance between successive computed points.
- **Local (truncation) error** is the error introduced in a single step; **order $O(h^p)$** means it shrinks like $h^p$ as $h\to0$.
- A **slope estimate** $f(x_n,y_n)$ is the direction the slope field gives at the current point.

**Statement — the three workhorse schemes.**

$$\textbf{Euler:}\quad y_{n+1}=y_n+h\,f(x_n,y_n).$$

$$\textbf{Improved (Heun):}\quad y_{n+1}=y_n+\tfrac{h}{2}\big[f(x_n,y_n)+f(x_{n+1},\,y_n+hf(x_n,y_n))\big].$$

$$\textbf{RK4:}\quad y_{n+1}=y_n+\tfrac{h}{6}\big(k_1+2k_2+2k_3+k_4\big).$$

Local error per step: Euler $O(h^2)$, Heun $O(h^3)$, RK4 $O(h^5)$ — so RK4 is far more accurate for the same step size.

> **Concept — Euler is the tangent-line approximation**
>
> At each point the slope field gives a direction $f(x_n,y_n)$; Euler steps a distance $h$ along that tangent line and repeats. It is the linear approximation $y(x+h)\approx y(x)+h\,y'(x)$ iterated — accurate for small $h$, drifting for large $h$.

**Demonstration — one Euler-method table.**

1. Approximate $y'=x+y,\ y(0)=1$ on $[0,0.3]$ with step $h=0.1$. Update rule: $y_{n+1}=y_n+0.1\,(x_n+y_n)$.
2. Step through, computing $f=x_n+y_n$ then advancing:
   $$\begin{array}{c|c|c|c} n & x_n & y_n & f=x_n+y_n\\\hline 0 & 0.0 & 1.0000 & 1.0000\\ 1 & 0.1 & 1.1000 & 1.2000\\ 2 & 0.2 & 1.2200 & 1.4200\\ 3 & 0.3 & 1.3620 & \\ \end{array}$$
3. Each row applies $y_{n+1}=y_n+0.1\,f$: $y_1=1+0.1(1.0)=1.10$; $y_2=1.10+0.1(1.20)=1.22$; $y_3=1.22+0.1(1.42)=1.362$.
4. The exact solution is $y=2e^{x}-x-1$ (check: $y'=2e^x-1$ and $x+y=x+2e^x-x-1=2e^x-1$ ✓, $y(0)=2-0-1=1$ ✓). It gives $y(0.3)=2e^{0.3}-1.3\approx1.3997$. Euler's $1.3620$ trails it by about $0.038$ — the accumulated truncation error.

Halving $h$ roughly halves Euler's error; RK4 would nail $y(0.3)$ to several digits in the same three steps.

<a id="s17"></a>
### A first look at PDEs & Fourier series

#### What this section says, in one breath

When a quantity varies in both space and time — temperature along a rod, a vibrating string — its law is a **partial differential equation**. The trick of **separation of variables** reduces a PDE to ordinary ODEs, and **Fourier series** stitch the pieces back into a solution matching the initial data.

#### Every term, defined from zero

- A **partial differential equation (PDE)** involves partial derivatives in more than one variable, e.g. $u_t$ (rate in time) and $u_{xx}$ (curvature in space) of $u(x,t)$.
- **Separation of variables** assumes $u(x,t)=X(x)T(t)$, a product of a space-only and a time-only factor.
- A **boundary condition** fixes the value of $u$ at the ends of the spatial domain.
- Functions are **orthogonal** on $[0,L]$ if the integral of their product is zero — the function-space version of perpendicular.

**Statement — the three classic linear PDEs.**

$$\textbf{Heat:}\ u_t=\alpha\,u_{xx},\qquad \textbf{Wave:}\ u_{tt}=c^2 u_{xx},\qquad \textbf{Laplace:}\ u_{xx}+u_{yy}=0.$$

Heat (diffusion) smooths data over time; wave propagates it at speed $c$; Laplace describes steady states.

**Demonstration — separating variables in the heat equation.**

1. Seek a product solution $u(x,t)=X(x)\,T(t)$ for $u_t=\alpha u_{xx}$. Then $u_t=X T'$ and $u_{xx}=X'' T$, so
   $$X T' = \alpha X'' T.$$
2. Divide by $\alpha X T$ (where nonzero) to separate the variables:
   $$\frac{T'}{\alpha T}=\frac{X''}{X}.$$
3. The left side depends only on $t$, the right only on $x$. Two functions of independent variables can be equal only if both equal the *same constant*, which we call $-\lambda$:
   $$\frac{X''}{X}=-\lambda,\qquad \frac{T'}{\alpha T}=-\lambda.$$
   *Reason:* if a function of $t$ alone equals a function of $x$ alone for all $x,t$, neither can actually vary, so both are constant.
4. This yields two ODEs — $X''+\lambda X=0$ and $T'+\alpha\lambda T=0$ — solved by the methods of Part B (§s8) and §s6:
   $$X_n=\sin\!\Big(\frac{n\pi x}{L}\Big),\qquad T_n=e^{-\alpha(n\pi/L)^2 t}.$$

The boundary conditions $u(0,t)=u(L,t)=0$ force $X(0)=X(L)=0$, which selects $\lambda=(n\pi/L)^2$ for integer $n$: the allowed **modes** are quantized.

**Statement — Fourier series: building the full solution.**

$$f(x)=\frac{a_0}{2}+\sum_{n=1}^\infty\!\Big(a_n\cos\frac{n\pi x}{L}+b_n\sin\frac{n\pi x}{L}\Big),\quad b_n=\frac{2}{L}\!\int_0^L f(x)\sin\frac{n\pi x}{L}\,dx.$$

Superpose the modes $X_nT_n$ (legitimate by linearity) and choose the coefficients $b_n$ — the Fourier coefficients of the initial temperature $f(x)$ — so the sum at $t=0$ matches $u(x,0)=f(x)$.

**Derivation — the coefficient formula via orthogonality.**

1. Suppose $f(x)=\sum_{m\ge1} b_m\sin\frac{m\pi x}{L}$. Multiply both sides by $\sin\frac{n\pi x}{L}$ and integrate over $[0,L]$.
2. Use **orthogonality**: $\int_0^L \sin\frac{m\pi x}{L}\sin\frac{n\pi x}{L}\,dx=0$ for $m\ne n$ and $=L/2$ for $m=n$. So every term except $m=n$ vanishes.
   *Reason:* product-to-sum identities make each $m\ne n$ integral a difference of full-period cosines, which integrate to zero.
3. The surviving term gives $\int_0^L f(x)\sin\frac{n\pi x}{L}\,dx=b_n\cdot\frac{L}{2}$, hence $b_n=\frac{2}{L}\int_0^L f(x)\sin\frac{n\pi x}{L}\,dx$. ∎

> **Connection — orthogonality, the inner product of functions**
>
> The coefficient formula works because the sines are **orthogonal**, like perpendicular basis vectors. Fourier series are the eigenfunction expansion of §s12 carried into infinite dimensions — linear algebra, integration, and differential equations meeting in a single idea.

---

*A first course in differential equations — first-order methods, the full second-order linear theory, systems and the phase plane, the Laplace transform, series solutions, numerics, and a gateway to PDEs and Fourier analysis. Every method is demonstrated on a worked example with actual numbers, every symbol is defined in words, and the threads back to integration and linear algebra are made explicit. Read once for the architecture; return to any box as a reference. Remember: solving a differential equation is always reducing it to integrations you can do.*
