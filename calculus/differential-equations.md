**English** · [中文](differential-equations.zh.md)

# Differential equations, *solved.*

A full first course — from a single separable equation to systems, the Laplace transform, and the heat equation — laid out basics → expert. Every core method is **demonstrated** on a worked example, and the threads back to integration and linear algebra are made explicit.

[← Back to all guides](../README.md)

## Part A · First-order equations

<a id="s0"></a>
### The big picture: what a differential equation is

A differential equation is a sentence about *change*. Instead of telling you a quantity, it tells you the rule its rate of change obeys — and solving it means finding the quantity itself.

An **ordinary differential equation** (ODE) relates an unknown function $y(x)$ to its derivatives. A **solution** is a function — not a number — that satisfies the equation on some interval.

- **Order** — the highest derivative present. $y'=ky$ is first order; $y''+y=0$ is second order.
- **Linear vs nonlinear** — linear means $y$ and its derivatives appear only to the first power and are not multiplied together: $a_n(x)y^{(n)}+\cdots+a_1(x)y'+a_0(x)y=g(x)$.
- **ODE vs PDE** — one independent variable (ODE) versus several, giving partial derivatives (PDE, Section 17).

> **Principle — solving = integrating with structure**
>
> The simplest ODE is $y'=f(x)$, solved by one integration: $y=\int f\,dx+C$. Every method in this guide is a way of **reducing a harder equation to integrations you can do**. The arbitrary constant $C$ is the signature of a differential equation: a first-order ODE has a one-parameter family of solutions, and an **initial condition** $y(x_0)=y_0$ selects one curve from the family.

**General vs particular solution**

$$y'=f(x)\ \Longrightarrow\ y=\int f(x)\,dx+C \quad(\text{general}),\qquad y(x_0)=y_0\ \text{fixes}\ C\ (\text{particular}).$$

*An $n$th-order ODE carries $n$ arbitrary constants and needs $n$ conditions to pin down a unique solution.*

#### The whole course on one line

> First-order (separable, linear) → Modeling → Second-order linear → Systems & phase plane → Laplace transform → Series & numerics → PDEs & Fourier

> **Connection — this is calculus, aimed**
>
> You already know how to differentiate and integrate. Differential equations turn that machinery into a tool for prediction: physics, biology, finance and engineering all speak in rates of change, so their laws are differential equations. Learning to solve them is learning to run the laws forward.

<a id="s1"></a>
### Slope fields, solution curves & separable equations

Before any formula, you can *see* a first-order equation: $y'=f(x,y)$ assigns a slope to every point of the plane. Solutions are the curves that follow those slopes.

> **Concept — the slope field**
>
> An equation $y'=f(x,y)$ is a field of little arrows: at each $(x,y)$ draw a short segment with slope $f(x,y)$. A **solution curve** is one that is tangent to the arrows everywhere. This geometric picture exists even when no formula does, and an **initial point** picks out exactly one curve threading through the field.

**Separable equations**

$$\frac{dy}{dx}=g(x)\,h(y)\ \Longrightarrow\ \int\frac{dy}{h(y)}=\int g(x)\,dx+C.$$

*If the right-hand side factors into an $x$-part times a $y$-part, gather each variable on its own side and integrate. Watch for constant solutions where $h(y)=0$.*

**Demonstration — solving a separable IVP**

1. Solve $\dfrac{dy}{dx}=\dfrac{x}{y}$ with $y(0)=3$. Separate the variables:

   $$y\,dy = x\,dx.$$
2. Integrate both sides:

   $$\int y\,dy=\int x\,dx \ \Longrightarrow\ \tfrac12 y^2=\tfrac12 x^2+C_1.$$
3. Multiply by 2 and rename the constant:

   $$y^2 = x^2 + C.$$
4. Apply $y(0)=3$: $\,9=0+C$, so $C=9$ and the solution curve is

   $$y=\sqrt{x^2+9}\quad(\text{positive root, to match }y(0)=3>0).$$

*The general solution $y^2-x^2=C$ is a family of hyperbolas; the initial condition selects one.*

> **Connection — why "separating" is legitimate**
>
> The shorthand "multiply by $dx$" is justified by the chain rule: if $\frac1{h(y)}\frac{dy}{dx}=g(x)$, integrate both sides in $x$; substitution turns $\int \frac1{h(y)}\frac{dy}{dx}\,dx$ into $\int \frac{dy}{h(y)}$. Separation is the chain rule run backward.

<a id="s2"></a>
### First-order linear equations & the integrating factor

*The most important first-order class. A clever multiplier turns the whole left side into a single derivative, after which one integration finishes the job.*

**Standard form & the integrating factor**

$$\frac{dy}{dx}+P(x)\,y = Q(x),\qquad \mu(x)=e^{\int P(x)\,dx}.$$

$$y=\frac{1}{\mu(x)}\!\left(\int \mu(x)\,Q(x)\,dx + C\right).$$

*Always put the equation in standard form first (coefficient of $y'$ equal to 1) before reading off $P$ and $Q$.*

**Demonstration — deriving the integrating factor $\mu=e^{\int P\,dx}$**

1. We want a multiplier $\mu(x)$ so that $\mu y' + \mu P y$ becomes the derivative of a product $(\mu y)'$. By the product rule, $(\mu y)'=\mu y'+\mu' y$.
2. Matching the two requires the coefficient of $y$ to agree:

   $$\mu' = \mu P.$$
3. This is itself separable: $\dfrac{d\mu}{\mu}=P\,dx$, so integrating gives

   $$\ln|\mu| = \int P\,dx \ \Longrightarrow\ \mu=e^{\int P\,dx}.$$
4. With this $\mu$, the equation collapses to $(\mu y)'=\mu Q$; integrate once:

   $$\mu y=\int \mu Q\,dx + C.$$

*The integrating factor is precisely the function that makes the left side an exact derivative.*

**Demonstration — a worked linear equation**

1. Solve $x y' + 2y = x^3$. First divide by $x$ to reach standard form:

   $$y' + \frac{2}{x}\,y = x^2,\qquad P=\frac{2}{x},\ Q=x^2.$$
2. Integrating factor:

   $$\mu=e^{\int (2/x)\,dx}=e^{2\ln|x|}=x^2.$$
3. Multiply through: $(x^2 y)' = x^2\cdot x^2 = x^4$. Integrate:

   $$x^2 y = \frac{x^5}{5}+C.$$
4. Solve for $y$:

   $$y=\frac{x^3}{5}+\frac{C}{x^2}.$$

*The $C/x^2$ piece is the solution of the homogeneous part $y'+\tfrac2x y=0$; the $x^3/5$ is a particular response to $Q$.*

> **Connection — superposition appears early**
>
> The answer splits as *homogeneous* $+$ *particular* — the same structure that will organize all of Part B. The integrating factor is the first-order shadow of the broader linear theory.

<a id="s3"></a>
### Exact equations

*Some equations are already the differential of a hidden function $F(x,y)$. Recognizing this lets you solve them by reading off level curves.*

**Exactness test & solution**

$$M(x,y)\,dx+N(x,y)\,dy=0 \ \text{ is exact} \iff \frac{\partial M}{\partial y}=\frac{\partial N}{\partial x}.$$

$$\text{Then } \exists\,F:\ F_x=M,\ F_y=N,\quad\text{and the solution is}\quad F(x,y)=C.$$

*Exactness says $M\,dx+N\,dy$ is the total differential $dF=F_x\,dx+F_y\,dy$. Solutions are the level curves of $F$.*

**Demonstration — testing and solving an exact equation**

1. Solve $(2xy+3)\,dx+(x^2-1)\,dy=0$. Here $M=2xy+3,\ N=x^2-1$.
2. Test exactness: Equal, so the equation is exact.

   $$M_y=2x,\qquad N_x=2x.$$
3. Integrate $F_x=M$ in $x$, treating $y$ as constant:

   $$F=\int(2xy+3)\,dx = x^2 y+3x+g(y).$$
4. Differentiate in $y$ and match $F_y=N$: $x^2+g'(y)=x^2-1$, so $g'(y)=-1$, giving $g(y)=-y$.
5. Therefore the implicit solution is

   $$x^2 y + 3x - y = C.$$

*When $M_y\ne N_x$, one can sometimes restore exactness with an integrating factor $\mu$ — the same idea as Section 2, generalized.*

> **Connection — Clairaut's theorem is the engine**
>
> The test $M_y=N_x$ is exactly the equality of mixed partials $F_{xy}=F_{yx}$. Exact equations are vector calculus in disguise: $M\,dx+N\,dy$ is exact iff the field $(M,N)$ is conservative, with $F$ its potential.

<a id="s4"></a>
### Substitutions: homogeneous & Bernoulli equations

*When an equation is neither separable nor linear, the right change of variable can convert it into one that is. Two classic substitutions cover a wide range.*

**Homogeneous equations**

$$\frac{dy}{dx}=F\!\left(\frac{y}{x}\right)\quad\text{substitute}\quad v=\frac{y}{x},\ y=vx,\ \frac{dy}{dx}=v+x\frac{dv}{dx}.$$

*The substitution always makes the equation separable in $v$ and $x$.*

**Bernoulli equations**

$$\frac{dy}{dx}+P(x)\,y = Q(x)\,y^{n}\quad\text{substitute}\quad v=y^{1-n}.$$

$$\Longrightarrow\ \frac{dv}{dx}+(1-n)P(x)\,v=(1-n)Q(x)\quad(\text{now linear in }v).$$

**Demonstration — solving a Bernoulli equation**

1. Solve $y'+\dfrac{1}{x}y = x y^2$. Here $n=2$, so set $v=y^{1-2}=y^{-1}$, giving $v'=-y^{-2}y'$.
2. Divide the equation by $y^2$: $\,y^{-2}y' + \tfrac1x y^{-1} = x$. In terms of $v$:

   $$-v' + \frac1x v = x \ \Longrightarrow\ v' - \frac1x v = -x.$$
3. This is linear with $P=-\tfrac1x$: $\mu=e^{-\int dx/x}=x^{-1}$. Then $(x^{-1}v)'=-1$:

   $$x^{-1}v=-x+C \ \Longrightarrow\ v=-x^2+Cx.$$
4. Return to $y$ via $y=1/v$:

   $$y=\frac{1}{Cx-x^2}.$$

*Bernoulli's trick linearizes a nonlinear equation by raising $y$ to a clever power.*

> **Connection — a recurring strategy**
>
> "Find the substitution that flattens the nonlinearity" returns throughout: $v=y/x$ here, $v=y^{1-n}$ for Bernoulli, reduction of order in Section 8, and the moving frame of the phase plane in Section 12.

<a id="s5"></a>
### Existence, uniqueness & autonomous equations (stability)

*Before solving, two questions matter: does a solution exist, and is it the only one? And for equations that don't depend on $x$ explicitly, we can read off long-term behavior without solving at all.*

**Existence & uniqueness (Picard–Lindelöf)**

$$y'=f(x,y),\ y(x_0)=y_0:\quad \text{if } f \text{ and } \frac{\partial f}{\partial y}\text{ are continuous near }(x_0,y_0),$$

*then a unique solution exists on some interval around $x_0$. Continuity of $f$ alone guarantees existence; continuity of $f_y$ guarantees uniqueness.*

> **Concept — why uniqueness can fail**
>
> $y'=\sqrt{y},\ y(0)=0$ has both $y\equiv0$ and $y=\tfrac14 x^2$ as solutions, because $f_y=\tfrac1{2\sqrt y}$ blows up at $y=0$. The hypotheses of the theorem are exactly what rules out such branching: solution curves can never cross where they hold.

**Autonomous equations & equilibria**

$$\frac{dy}{dx}=f(y):\quad \text{equilibria are roots } f(y^*)=0.$$

$$f'(y^*)<0\Rightarrow\text{stable (sink)},\qquad f'(y^*)>0\Rightarrow\text{unstable (source)}.$$

*A **phase line** marks where $f(y)>0$ (arrows up) and $f(y)<0$ (arrows down); arrows point toward stable equilibria.*

**Demonstration — stability by linearization**

1. Take $y'=y(1-y)$. Equilibria: $f(y)=y-y^2=0$ at $y^*=0$ and $y^*=1$.
2. Compute $f'(y)=1-2y$. Evaluate at each equilibrium:

   $$f'(0)=1>0\ (\text{unstable}),\qquad f'(1)=-1<0\ (\text{stable}).$$
3. So any positive start drifts away from 0 and toward 1: $y=1$ is the carrying capacity (the logistic story of Section 6).

*Near an equilibrium, $y'\approx f'(y^*)(y-y^*)$: exponential growth or decay, whose sign is the whole verdict.*

<a id="s6"></a>
### Modeling: growth/decay, mixing, cooling, the logistic equation

*The payoff of Part A: real phenomena translate into first-order ODEs, and the methods above solve them. Modeling is the art of writing "rate of change $=$ ..." correctly.*

**Exponential growth/decay & Newton's cooling**

$$\frac{dy}{dt}=ky \ \Rightarrow\ y=y_0 e^{kt},\qquad \frac{dT}{dt}=-k\,(T-T_{\text{env}}) \ \Rightarrow\ T=T_{\text{env}}+(T_0-T_{\text{env}})e^{-kt}.$$

*$k>0$: growth (populations, interest). $k<0$: decay (radioactivity, half-life $t_{1/2}=\ln 2/|k|$).*

**The logistic equation**

$$\frac{dP}{dt}=rP\!\left(1-\frac{P}{K}\right)\ \Longrightarrow\ P(t)=\frac{K}{1+A e^{-rt}},\quad A=\frac{K-P_0}{P_0}.$$

*$r$ is the intrinsic growth rate, $K$ the carrying capacity. $P\to K$ as $t\to\infty$ — the stable equilibrium of Section 5.*

**Demonstration — a mixing (tank) problem**

1. A 100 L tank holds pure water. Brine at 2 g/L flows in at 5 L/min; the well-stirred mixture flows out at 5 L/min. Let $S(t)$ be grams of salt. Rate in $=2\cdot5=10$ g/min; rate out $=\dfrac{S}{100}\cdot5$ g/min.
2. The balance law gives a linear ODE:

   $$\frac{dS}{dt}=10-\frac{S}{20},\qquad S(0)=0.$$
3. Standard form $S'+\tfrac1{20}S=10$, integrating factor $\mu=e^{t/20}$:

   $$(e^{t/20}S)'=10\,e^{t/20}\ \Rightarrow\ e^{t/20}S=200\,e^{t/20}+C.$$
4. So $S=200+Ce^{-t/20}$; $S(0)=0$ gives $C=-200$:

   $$S(t)=200\big(1-e^{-t/20}\big).$$

*As $t\to\infty$, $S\to200$ g — i.e. 2 g/L throughout, the inflow concentration. The model agrees with intuition.*

> **Connection — the logistic solution comes from partial fractions**
>
> Separating $\frac{dP}{P(1-P/K)}=r\,dt$ requires the integral $\int\frac{dP}{P(1-P/K)}$, which splits via **partial fractions** into $\frac1P+\frac{1/K}{1-P/K}$. The algebra you learned for integration is exactly what produces the S-curve.

## Part B · Second-order linear equations

<a id="s7"></a>
### Linear ODE theory: superposition, independence & the Wronskian

*Second-order linear equations have a beautiful, complete structure borrowed from linear algebra: their solutions form a vector space, and a basis of two functions describes them all.*

**The linear second-order equation**

$$y''+p(x)\,y'+q(x)\,y=g(x).$$

*If $g\equiv0$ the equation is **homogeneous**; otherwise **nonhomogeneous**. $p,q,g$ continuous guarantees a unique solution to any IVP $y(x_0)=a,\ y'(x_0)=b$.*

> **Principle — superposition & the solution structure**
>
> For the homogeneous equation, any linear combination of solutions is again a solution. The general solution is $y=c_1 y_1+c_2 y_2$ for two **linearly independent** solutions $y_1,y_2$. For the nonhomogeneous equation, the general solution is **$y=y_h+y_p$**: the full homogeneous family plus any one particular solution.

**The Wronskian & independence**

$$W(y_1,y_2)=\begin{vmatrix} y_1 & y_2\\ y_1' & y_2'\end{vmatrix}=y_1 y_2'-y_2 y_1'.$$

*For solutions of the same linear ODE, $W\ne0$ at one point $\iff$ $y_1,y_2$ are linearly independent (a **fundamental set**). Abel's theorem: $W(x)=W(x_0)\,e^{-\int p\,dx}$, so $W$ is either always zero or never zero.*

**Demonstration — independence via the Wronskian**

1. Are $y_1=e^{x}$ and $y_2=e^{2x}$ independent? Compute the Wronskian:

   $$W=\begin{vmatrix} e^{x} & e^{2x}\\ e^{x} & 2e^{2x}\end{vmatrix}=2e^{3x}-e^{3x}=e^{3x}.$$
2. Since $e^{3x}\ne0$ for all $x$, the functions are linearly independent and form a fundamental set.

*Two solutions with nonzero Wronskian span the whole 2-dimensional solution space.*

> **Connection — this is linear algebra**
>
> The solution set of a homogeneous linear ODE is a **vector space**; $y_1,y_2$ are a basis, and "order $n$" means "dimension $n$." The Wronskian is the determinant that tests for a basis — the function-space analog of independence of vectors.

<a id="s8"></a>
### Homogeneous equations with constant coefficients

*The workhorse case. Guessing $y=e^{rx}$ converts the differential equation into an algebraic one — and the roots of that polynomial dictate everything.*

**The characteristic equation**

$$ay''+by'+cy=0\ \xrightarrow{\ y=e^{rx}\ }\ ar^2+br+c=0.$$

*Each root $r$ gives a solution $e^{rx}$; the discriminant $b^2-4ac$ decides which of three cases applies.*

**The three cases**

$$\textbf{Distinct real } r_1\ne r_2:\quad y=c_1e^{r_1 x}+c_2e^{r_2 x}.$$

$$\textbf{Repeated } r:\quad y=(c_1+c_2 x)\,e^{r x}.$$

$$\textbf{Complex } r=\alpha\pm\beta i:\quad y=e^{\alpha x}\big(c_1\cos\beta x+c_2\sin\beta x\big).$$

**Demonstration — all three cases, worked**

1. Distinct real. $y''-5y'+6y=0$: characteristic $r^2-5r+6=(r-2)(r-3)=0$, so

   $$y=c_1 e^{2x}+c_2 e^{3x}.$$
2. Repeated root. $y''-4y'+4y=0$: $r^2-4r+4=(r-2)^2=0$, giving $r=2$ twice. The second solution is $xe^{2x}$:

   $$y=(c_1+c_2 x)\,e^{2x}.$$
3. Complex roots. $y''+2y'+5y=0$: $r^2+2r+5=0\Rightarrow r=\dfrac{-2\pm\sqrt{4-20}}{2}=-1\pm2i$. Hence

   $$y=e^{-x}\big(c_1\cos 2x+c_2\sin 2x\big).$$

*Euler's formula $e^{i\beta x}=\cos\beta x+i\sin\beta x$ is what turns complex exponentials into real sinusoids.*

**Demonstration — where $xe^{rx}$ comes from (reduction of order)**

1. With a repeated root $r$, one solution is $y_1=e^{rx}$. Seek a second as $y_2=u(x)e^{rx}$ and substitute into $y''-2ry'+r^2y=0$.
2. The $u$ and $u'$ terms cancel by construction (because $r$ solves the characteristic equation twice), leaving

   $$u''e^{rx}=0\ \Rightarrow\ u''=0.$$
3. So $u=c_1+c_2 x$, and the independent new piece is $y_2=xe^{rx}$.

*A repeated root costs a degree of freedom; multiplying by $x$ restores it — exactly as in resonance (Section 11).*

<a id="s9"></a>
### Nonhomogeneous: undetermined coefficients

*To solve $ay''+by'+cy=g(x)$, find the homogeneous solution $y_h$ (Section 8), then guess a particular $y_p$ shaped like $g$. The general solution is $y_h+y_p$.*

**The guess table**

$$g(x)=e^{\alpha x}\ \to\ Ae^{\alpha x};\quad g=\sin\beta x\text{ or }\cos\beta x\ \to\ A\cos\beta x+B\sin\beta x.$$

$$g=\text{polynomial of degree }n\ \to\ A_n x^n+\cdots+A_1 x+A_0.$$

*Products and sums of these use products and sums of the guesses. Solve for the coefficients by substituting.*

> **Principle — the modification rule**
>
> If your guess already solves the homogeneous equation, it contributes nothing on substitution. **Multiply the guess by $x$** (or $x^2$ for a double root) until no term duplicates a homogeneous solution. This is the same "$x$ saves a degenerate case" phenomenon as the repeated root.

**Demonstration — undetermined coefficients, worked**

1. Solve $y''-3y'+2y=4e^{3x}$. Homogeneous: $r^2-3r+2=(r-1)(r-2)\Rightarrow y_h=c_1e^{x}+c_2 e^{2x}$.
2. $g=4e^{3x}$, and $r=3$ is not a root, so guess $y_p=Ae^{3x}$. Then $y_p'=3Ae^{3x},\ y_p''=9Ae^{3x}$.
3. Substitute: $(9A-9A+2A)e^{3x}=4e^{3x}\Rightarrow 2A=4\Rightarrow A=2$, so $y_p=2e^{3x}$.
4. General solution:

   $$y=c_1 e^{x}+c_2 e^{2x}+2e^{3x}.$$

*Had $g$ been $4e^{2x}$ (a homogeneous root), we would instead guess $Axe^{2x}$ by the modification rule.*

<a id="s10"></a>
### Nonhomogeneous: variation of parameters

*When $g(x)$ is not a nice exponential/polynomial/sinusoid (say $\sec x$ or $\ln x$), undetermined coefficients fails. Variation of parameters always works — at the cost of two integrals.*

**The formula**

$$y_p=-y_1\!\int\frac{y_2\,g}{W}\,dx + y_2\!\int\frac{y_1\,g}{W}\,dx,\qquad W=W(y_1,y_2).$$

*Here $y_1,y_2$ are a fundamental set of the homogeneous equation, $g$ is the right side in standard form (coefficient of $y''$ equal to 1), and $W$ is their Wronskian.*

**Demonstration — deriving variation of parameters**

1. Replace the constants in $y_h=c_1y_1+c_2y_2$ by functions: seek $y_p=u_1 y_1+u_2 y_2$.
2. Two unknowns need two equations. Impose the convenient constraint $u_1'y_1+u_2'y_2=0$ (it kills extra terms in $y_p'$).
3. Substituting $y_p$ into $y''+py'+qy=g$ and using that $y_1,y_2$ solve the homogeneous equation leaves the second equation:

   $$u_1'y_1'+u_2'y_2'=g.$$
4. Solve the 2×2 linear system for $u_1',u_2'$ by Cramer's rule:

   $$u_1'=-\frac{y_2\,g}{W},\qquad u_2'=\frac{y_1\,g}{W}.$$
5. Integrate to get $u_1,u_2$, giving the boxed formula.

*The Wronskian in the denominator is the determinant of that very linear system — Section 7 reappears.*

**Demonstration — applying it to $y''+y=\sec x$**

1. Homogeneous: $y_1=\cos x,\ y_2=\sin x$, with $W=\cos^2x+\sin^2x=1$.
2. Then $u_1'=-\dfrac{\sin x\sec x}{1}=-\tan x\Rightarrow u_1=\ln|\cos x|$, and $u_2'=\dfrac{\cos x\sec x}{1}=1\Rightarrow u_2=x$.
3. Assemble $y_p=u_1\cos x+u_2\sin x$:

   $$y_p=\cos x\,\ln|\cos x|+x\sin x.$$
4. General solution:

   $$y=c_1\cos x+c_2\sin x+\cos x\,\ln|\cos x|+x\sin x.$$

*No finite guess could have produced the $\ln|\cos x|$ term — variation of parameters is the universal method.*

<a id="s11"></a>
### Applications: mechanical & electrical vibrations, resonance

*The same constant-coefficient equation $my''+cy'+ky=F(t)$ governs a mass on a spring and a series RLC circuit. One piece of mathematics, two physical worlds.*

**The vibration equation & its analogs**

$$m y'' + c y' + k y = F(t)\qquad\Longleftrightarrow\qquad L q'' + R q' + \tfrac1C q = E(t).$$

*mass $m\leftrightarrow$ inductance $L$; damping $c\leftrightarrow$ resistance $R$; stiffness $k\leftrightarrow$ inverse capacitance $1/C$; displacement $y\leftrightarrow$ charge $q$.*

**Damping regimes (free, $F=0$)**

$$\omega_0=\sqrt{k/m};\quad c^2-4mk>0:\text{ overdamped},\ =0:\text{ critically damped},\ <0:\text{ underdamped}.$$

*Underdamped motion is a decaying oscillation $e^{-(c/2m)t}\cos(\omega_d t-\phi)$; the three regimes are precisely the three discriminant cases of Section 8.*

**Demonstration — pure resonance**

1. Undamped, driven at the natural frequency: $y''+\omega_0^2 y=F_0\cos\omega_0 t$. Homogeneous solution: $c_1\cos\omega_0 t+c_2\sin\omega_0 t$.
2. The driving term $\cos\omega_0 t$ already solves the homogeneous equation, so by the modification rule guess $y_p=t(A\cos\omega_0 t+B\sin\omega_0 t)$.
3. Substituting and matching gives

   $$y_p=\frac{F_0}{2\omega_0}\,t\,\sin\omega_0 t.$$
4. The factor $t$ means the amplitude grows without bound: resonance.

*Driving a system at its natural frequency feeds energy in step every cycle — the bridge-and-soldiers, wineglass-shattering effect.*

> **Connection — resonance is the repeated-root $x$ again**
>
> The runaway $t\sin\omega_0 t$ is the same mechanism as the $xe^{rx}$ of a double characteristic root: when the forcing frequency hits the natural one, the would-be solution degenerates and $t$ appears to restore independence. Adding even a little damping $c>0$ shifts the roots off the imaginary axis and caps the amplitude.

## Part C · Systems, transforms & series

<a id="s12"></a>
### Systems of linear ODEs: the eigenvalue method & phase plane

*Coupled equations, and any higher-order equation, become a single vector equation $\mathbf{x}'=A\mathbf{x}$. Its solutions are read straight off the eigenvalues and eigenvectors of $A$.*

**The eigenvalue method**

$$\mathbf{x}'=A\mathbf{x},\quad \text{try } \mathbf{x}=\mathbf{v}\,e^{\lambda t}\ \Rightarrow\ A\mathbf{v}=\lambda\mathbf{v}.$$

$$\mathbf{x}(t)=c_1\mathbf{v}_1 e^{\lambda_1 t}+c_2\mathbf{v}_2 e^{\lambda_2 t}\quad(\text{distinct eigenvalues}).$$

*Eigenvalues $\lambda$ solve $\det(A-\lambda I)=0$; each eigenvector $\mathbf v$ gives a straight-line solution. Complex $\lambda$ give spirals; repeated $\lambda$ need a generalized eigenvector.*

**Phase-plane classification by eigenvalues**

$$\lambda_1,\lambda_2<0:\text{ stable node};\quad >0:\text{ unstable node};\quad \text{opposite signs}:\text{ saddle}.$$

$$\lambda=\alpha\pm\beta i:\ \alpha<0\ \text{stable spiral},\ \alpha>0\ \text{unstable spiral},\ \alpha=0\ \text{center}.$$

**Demonstration — solving a 2×2 system**

1. Solve $\mathbf{x}'=\begin{pmatrix}1&2\\2&1\end{pmatrix}\mathbf{x}$. Characteristic: $\det(A-\lambda I)=(1-\lambda)^2-4=0\Rightarrow \lambda=3,\,-1$.
2. For $\lambda=3$: $(A-3I)\mathbf v=0$ gives $\begin{pmatrix}-2&2\\2&-2\end{pmatrix}\mathbf v=0$, so $\mathbf v_1=\begin{pmatrix}1\\1\end{pmatrix}$.
3. For $\lambda=-1$: $\begin{pmatrix}2&2\\2&2\end{pmatrix}\mathbf v=0$, so $\mathbf v_2=\begin{pmatrix}1\\-1\end{pmatrix}$.
4. General solution:

   $$\mathbf{x}(t)=c_1\begin{pmatrix}1\\1\end{pmatrix}e^{3t}+c_2\begin{pmatrix}1\\-1\end{pmatrix}e^{-t}.$$

*Opposite-sign eigenvalues $\Rightarrow$ a **saddle**: trajectories rush in along $\mathbf v_2$ and out along $\mathbf v_1$.*

> **Connection — second-order = a 2D system**
>
> Setting $x_1=y,\ x_2=y'$ turns $y''+by'+cy=0$ into $\mathbf{x}'=\begin{pmatrix}0&1\\-c&-b\end{pmatrix}\mathbf{x}$. The characteristic polynomial of this matrix is exactly $r^2+br+c$ from Section 8 — the eigenvalue method and the characteristic equation are the same computation.

<a id="s13"></a>
### The Laplace transform

*A transform that turns calculus into algebra: derivatives become multiplication, and differential equations become equations you can solve by hand, then invert.*

**Definition & the key property**

$$\mathcal{L}\{f(t)\}=F(s)=\int_0^\infty e^{-st}f(t)\,dt.$$

$$\mathcal{L}\{f'\}=sF(s)-f(0),\qquad \mathcal{L}\{f''\}=s^2F(s)-sf(0)-f'(0).$$

*The derivative rule bakes the initial conditions in from the start — that is the whole point.*

**Demonstration — computing $\mathcal{L}\{e^{at}\}$ from the definition**

1. Apply the definition:

   $$\mathcal{L}\{e^{at}\}=\int_0^\infty e^{-st}e^{at}\,dt=\int_0^\infty e^{-(s-a)t}\,dt.$$
2. Integrate, assuming $s>a$ so the exponential decays:

   $$=\left[\frac{-1}{s-a}e^{-(s-a)t}\right]_0^\infty=0-\left(\frac{-1}{s-a}\right).$$
3. Therefore

   $$\mathcal{L}\{e^{at}\}=\frac{1}{s-a},\quad s>a.$$

*Setting $a=0$ recovers $\mathcal{L}\{1\}=1/s$. The same definite integral builds the whole table below.*

**Transform table**

> **Connection — linearity & partial fractions return**
>
> Like integration, the Laplace transform is **linear**: $\mathcal{L}\{af+bg\}=aF+bG$. Inverting almost always means splitting a rational $F(s)$ by partial fractions until each piece matches a table row — the same algebra used for the logistic integral in Section 6.

<a id="s14"></a>
### Solving initial-value problems with Laplace; step & impulse inputs

*The transform's reason for existing: solve an IVP in three moves — transform, solve the algebra for $Y(s)$, invert. It shines exactly where other methods struggle: discontinuous and impulsive forcing.*

**Step and impulse functions**

$$u_c(t)=\begin{cases}0,&t $u_c$ switches a forcing term on at $t=c$; the Dirac delta $\delta$ models an instantaneous kick (a hammer blow, a voltage spike).$$

<a id="s15"></a>
### Series solutions & the method of Frobenius

*When coefficients are variable ($p,q$ functions of $x$), there may be no elementary solution. We build one as a power series, determining its coefficients one recurrence at a time.*

**Power-series solution about an ordinary point**

$$y=\sum_{n=0}^\infty a_n (x-x_0)^n,\qquad y'=\sum_{n\ge1} n a_n x^{n-1},\ \ y''=\sum_{n\ge2} n(n-1)a_n x^{n-2}.$$

*An **ordinary point** is where $p,q$ are analytic. Substitute, align powers, and force the coefficient of each $x^n$ to zero to get a recurrence for the $a_n$.*

**Demonstration — series solution of $y'=y$**

1. Assume $y=\sum_{n\ge0}a_n x^n$, so $y'=\sum_{n\ge1} n a_n x^{n-1}=\sum_{n\ge0}(n+1)a_{n+1}x^{n}$.
2. Set $y'=y$ coefficient by coefficient: $(n+1)a_{n+1}=a_n$, the recurrence

   $$a_{n+1}=\frac{a_n}{n+1}.$$
3. Iterating from $a_0$: $a_n=\dfrac{a_0}{n!}$. Hence

   $$y=a_0\sum_{n\ge0}\frac{x^n}{n!}=a_0 e^{x}.$$

*The series machinery rediscovers $e^x$ — reassuring, and the method works when no closed form exists (Airy, Hermite, Bessel).*

**Frobenius: regular singular points**

$$y=x^{r}\sum_{n=0}^\infty a_n x^{n},\qquad \text{indicial equation}\ r(r-1)+p_0 r+q_0=0.$$

*At a **regular singular point**, prepend the factor $x^r$. The two roots $r$ of the indicial equation give the leading behavior; they generate Bessel and Legendre functions, central to physics.*

> **Connection — this is the Taylor series, solved for**
>
> A power-series solution is just a Taylor series whose coefficients are unknown until the ODE pins them down. Differentiating a series term-by-term — legitimate inside its radius of convergence — is the calculus that makes the recurrence possible.

<a id="s16"></a>
### Numerical methods: Euler, improved Euler & Runge–Kutta

*Most differential equations cannot be solved in closed form. Numerical methods march the solution forward in small steps, trading exactness for universality.*

**The three workhorse schemes**

$$\textbf{Euler:}\quad y_{n+1}=y_n+h\,f(x_n,y_n).$$

$$\textbf{Improved (Heun):}\quad y_{n+1}=y_n+\tfrac{h}{2}\big[f(x_n,y_n)+f(x_{n+1},\,y_n+hf(x_n,y_n))\big].$$

$$\textbf{RK4:}\quad y_{n+1}=y_n+\tfrac{h}{6}\big(k_1+2k_2+2k_3+k_4\big).$$

*Local error per step: Euler $O(h^2)$, Heun $O(h^3)$, RK4 $O(h^5)$ — so RK4 is far more accurate for the same step.*

> **Concept — Euler is the tangent-line approximation**
>
> At each point the slope field gives a direction $f(x_n,y_n)$; Euler simply steps a distance $h$ along that tangent line and repeats. It is the linear approximation $y(x+h)\approx y(x)+hy'(x)$ iterated — accurate for small $h$, drifting for large $h$.

**Demonstration — one Euler-method table**

1. Approximate $y'=x+y,\ y(0)=1$ on $[0,0.3]$ with step $h=0.1$. Update rule: $y_{n+1}=y_n+0.1\,(x_n+y_n)$.
2. Step through:

   $$\begin{array}{c|c|c|c} n & x_n & y_n & f=x_n+y_n\\\hline 0 & 0.0 & 1.0000 & 1.0000\\ 1 & 0.1 & 1.1000 & 1.2000\\ 2 & 0.2 & 1.2200 & 1.4200\\ 3 & 0.3 & 1.3620 & \\ \end{array}$$
3. Each row: $y_{n+1}=y_n+0.1\,f$. E.g. $y_1=1+0.1(1.0)=1.10$; $y_2=1.10+0.1(1.20)=1.22$; $y_3=1.22+0.1(1.42)=1.362$.
4. The exact solution is $y=2e^{x}-x-1$, giving $y(0.3)=2e^{0.3}-1.3\approx1.3997$. Euler's $1.3620$ trails it — the truncation error.

*Halving $h$ roughly halves Euler's error; RK4 would nail $y(0.3)$ to several digits in the same three steps.*

<a id="s17"></a>
### A first look at PDEs & Fourier series

*When a quantity varies in both space and time — temperature along a rod, a vibrating string — its law is a partial differential equation. Separation of variables reduces it to ODEs, and Fourier series stitch the pieces back together.*

**The three classic linear PDEs**

$$\textbf{Heat:}\ u_t=\alpha\,u_{xx},\qquad \textbf{Wave:}\ u_{tt}=c^2 u_{xx},\qquad \textbf{Laplace:}\ u_{xx}+u_{yy}=0.$$

*Heat (diffusion) smooths data over time; wave propagates it; Laplace describes steady states.*

**Demonstration — separating variables in the heat equation**

1. Seek a product solution $u(x,t)=X(x)\,T(t)$ for $u_t=\alpha u_{xx}$. Substitute:

   $$X T' = \alpha X'' T.$$
2. Divide by $\alpha X T$ to separate the variables:

   $$\frac{T'}{\alpha T}=\frac{X''}{X}.$$
3. The left side depends only on $t$, the right only on $x$; equal functions of independent variables must be a constant $-\lambda$:

   $$\frac{X''}{X}=-\lambda,\qquad \frac{T'}{\alpha T}=-\lambda.$$
4. This yields two ODEs — $X''+\lambda X=0$ and $T'+\alpha\lambda T=0$ — solved by the methods of Part B:

   $$X_n=\sin\!\Big(\frac{n\pi x}{L}\Big),\qquad T_n=e^{-\alpha(n\pi/L)^2 t}.$$

*Boundary conditions $u(0,t)=u(L,t)=0$ force $\lambda=(n\pi/L)^2$: the allowed modes are quantized.*

**Fourier series: building the full solution**

$$f(x)=\frac{a_0}{2}+\sum_{n=1}^\infty\!\Big(a_n\cos\frac{n\pi x}{L}+b_n\sin\frac{n\pi x}{L}\Big),\quad b_n=\frac{2}{L}\!\int_0^L f(x)\sin\frac{n\pi x}{L}\,dx.$$

*Superpose the modes $X_n T_n$ and choose the coefficients $b_n$ (the Fourier coefficients of the initial temperature) so the sum matches $u(x,0)=f(x)$.*

> **Connection — orthogonality, the inner product of functions**
>
> The coefficient formula works because $\int_0^L \sin\frac{m\pi x}{L}\sin\frac{n\pi x}{L}\,dx=0$ for $m\ne n$: the sines are **orthogonal**, like perpendicular basis vectors. Fourier series are the eigenfunction expansion of Section 12 carried into infinite dimensions — linear algebra, integration, and differential equations meeting in one idea.

---

*A first course in differential equations — first-order methods, the full second-order linear theory, systems and the phase plane, the Laplace transform, series solutions, numerics, and a gateway to PDEs and Fourier analysis. Every method is demonstrated on a worked example, and the threads back to integration and linear algebra are made explicit. Read once for the architecture; return to any box as a reference. Remember: solving a differential equation is always reducing it to integrations you can do.*
