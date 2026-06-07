# Calculus, *complete.*

A full single-variable course — every concept, principle, formula, and the demonstrations behind them — laid out basics → advanced. The chapter flow follows Adrian Banner's *The Calculus Lifesaver* (the Princeton review-course book), so it doubles as a companion to it.

[← Back to all guides](../README.md)

## Part A · Foundations

<a id="s0"></a>
### The big picture

All of calculus answers two questions about change, plus a discovery that they are opposites.

- **The derivative** — how fast is something changing right now? (slope, speed, rate)
- **The integral** — how much has accumulated in total? (area, distance, sum)

> **Principle — the one idea under everything**
>
> Both are built by taking a familiar quantity (a slope between two points; the area of a rectangle) and pushing it to a **limit**, letting a gap shrink to zero. Master limits and the rest is bookkeeping.

#### The whole course on one line

> Foundations → Limits → Derivatives → Integrals ↔ (FTC) → Series → Further topics

<a id="s1"></a>
### Functions, graphs & lines

*Calculus studies functions, so we start with what they are and how they behave.*

> **Concept — a function**
>
> A **function** assigns exactly one output to each input. The **domain** is the set of legal inputs; the **range** is the set of outputs produced. The **vertical line test**: a graph is a function only if no vertical line hits it twice.

**Lines — the three forms**

$$\text{slope } m=\frac{y_2-y_1}{x_2-x_1},\quad y-y_1=m(x-x_1),\quad y=mx+b$$

*The slope is the prototype of the derivative: rise over run. Calculus generalizes it to curves.*

> **Concept — inverse functions**
>
> An inverse $f^{-1}$ reverses $f$: if $f(a)=b$ then $f^{-1}(b)=a$. A function has an inverse only if it is **one-to-one** (passes the **horizontal line test**). To find it, swap $x$ and $y$ and solve. Geometrically, the graph reflects across the line $y=x$.

**Composition & symmetry**

$$(f\circ g)(x)=f\big(g(x)\big)$$

***Even** function: $f(-x)=f(x)$ (symmetric across the y-axis, e.g. $x^2,\cos x$). **Odd**: $f(-x)=-f(x)$ (symmetric through the origin, e.g. $x^3,\sin x$).*

<a id="s2"></a>
### Trigonometry review

*Trig functions are everywhere in calculus; these identities are the ones you will actually reuse.*

> **Concept — radians and the unit circle**
>
> Angles are measured in **radians** (arc length on the unit circle), not degrees, because the clean derivative $(\sin x)'=\cos x$ only holds in radians. On the unit circle, a point at angle $\theta$ is $(\cos\theta,\sin\theta)$. **ASTC** ("All Students Take Calculus") records which functions are positive in each quadrant.

**Pythagorean identities**

$$\sin^2\theta+\cos^2\theta=1,\quad 1+\tan^2\theta=\sec^2\theta,\quad 1+\cot^2\theta=\csc^2\theta$$

**Addition formulas**

$$\sin(A\pm B)=\sin A\cos B\pm\cos A\sin B,\quad \cos(A\pm B)=\cos A\cos B\mp\sin A\sin B$$

**Double-angle & power-reduction**

$$\sin 2\theta=2\sin\theta\cos\theta,\qquad \cos 2\theta=\cos^2\theta-\sin^2\theta$$

$$\sin^2\theta=\frac{1-\cos2\theta}{2},\qquad \cos^2\theta=\frac{1+\cos2\theta}{2}$$

*The power-reduction pair is essential for integrating $\sin^2$ and $\cos^2$ in Section 19.*

## Part B · Limits & continuity

<a id="s3"></a>
### Limits: the basic idea

*Where is the function heading as the input approaches a value — even if it never arrives?*

> **Concept — what a limit is (and isn't)**
>
> $\lim_{x\to a}f(x)=L$ describes the **height the function approaches** near $a$. It does *not* care about (and need not equal) the actual value $f(a)$ — the function may have a hole there. That gap between "approaching" and "arriving" is the whole point.

**One-sided limits & existence**

$$\lim_{x\to a^-}f(x)=\lim_{x\to a^+}f(x)=L \iff \lim_{x\to a}f(x)=L$$

*The two-sided limit exists only when both approaches agree. A **jump** means it does not exist.*

**Limits at infinity / infinite limits (asymptotes)**

$$\lim_{x\to\infty}\frac1x=0\ \text{(horizontal asymptote)},\qquad \lim_{x\to0^+}\frac1x=+\infty\ \text{(vertical asymptote)}$$

**Formal ε–δ definition**

$$\forall\,\varepsilon>0,\ \exists\,\delta>0:\ 0<|x-a|<\delta \implies |f(x)-L|<\varepsilon$$

*"Name any tolerance ε around L; I can find a window δ around a that keeps me inside it." The rigorous engine.*

**Limit laws & the Sandwich (Squeeze) principle**

$$\lim(f\pm g)=L\pm M,\ \ \lim(fg)=LM,\ \ \lim\tfrac fg=\tfrac LM\,(M\neq0)$$

$$g\le f\le h,\ \lim g=\lim h=L \implies \lim f=L$$

<a id="s4"></a>
### How to compute limits

*When direct substitution gives $0/0$ or $\infty/\infty$, reshape the expression first.*

> **Principle — substitute first, then fix**
>
> Always try plugging in. If you get a number, that's the limit. If you get $0/0$, the function has a removable feature — **factor and cancel**, or **multiply by a conjugate**, to remove it. If you get $\infty/\infty$, **divide by the highest power**.

**Demonstration — the three core techniques**

1. Factor & cancel (rational, $0/0$):

   $$\lim_{x\to2}\frac{x^2-4}{x-2}=\lim_{x\to2}\frac{(x-2)(x+2)}{x-2}=\lim_{x\to2}(x+2)=4.$$
2. Conjugate (roots, $0/0$): multiply top and bottom by $\sqrt{x}+1$ to clear the root, then cancel the offending factor.
3. Highest power ($x\to\infty$):

   $$\lim_{x\to\infty}\frac{3x^2+1}{5x^2-x}=\lim_{x\to\infty}\frac{3+\frac1{x^2}}{5-\frac1x}=\frac35.$$

**Demonstration — the famous $ \lim_{x\to0}\frac{\sin x}{x}=1 $**

1. Area comparison in the unit circle for $0

   $$\sin x < x < \tan x.$$
2. Divide by $\sin x$ and invert:

   $$\cos x < \frac{\sin x}{x} < 1.$$
3. As $x\to0$, $\cos x\to1$; the Squeeze principle forces the middle to $1$.

*This is what powers $(\sin x)'=\cos x$ in Section 8.*

<a id="s5"></a>
### Continuity & differentiability

*Two pillars: a function that flows without breaks, and one smooth enough to have a slope.*

**Continuity at a point**

$$f \text{ continuous at } a \iff \lim_{x\to a}f(x)=f(a)$$

*Limit exists, value exists, and they match — no hole, jump, or blow-up.*

> **Principle — the Intermediate Value Theorem (IVT)**
>
> If $f$ is continuous on $[a,b]$ and $N$ lies between $f(a)$ and $f(b)$, then $f(c)=N$ for some $c$ in between. A continuous curve cannot skip a value — which is exactly why a sign change guarantees a root.

> **Principle — the Extreme Value Theorem (EVT)**
>
> A continuous function on a **closed, bounded** interval $[a,b]$ always attains a maximum and a minimum somewhere on it. This is what makes "find the largest value" a well-posed problem in optimization (Section 12).

> **Concept — differentiability, and its link to continuity**
>
> A function is **differentiable** where it has a well-defined tangent slope. Key principle: **differentiable ⟹ continuous**, but not the reverse. $|x|$ is continuous everywhere yet has no slope at the corner $x=0$ (its left and right slopes disagree). Smoothness is strictly stronger than mere connectedness.

## Part C · The derivative

<a id="s6"></a>
### The definition of the derivative

*Take the slope between two points, then slide them together.*

**Definition**

$$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}=\lim_{t\to x}\frac{f(t)-f(x)}{t-x}$$

> **Concept — three meanings, one object**
>
> The derivative is simultaneously: the **slope of the tangent line**, the **instantaneous rate of change**, and (if $s(t)$ is position) the **velocity**. The difference quotient is average velocity over a tiny interval; the limit makes it instantaneous.

**Demonstration — $f(x)=x^2$ from the definition**

1. 

   $$\frac{(x+h)^2-x^2}{h}=\frac{2xh+h^2}{h}=2x+h.$$
2. Let $h\to0$:

   $$f'(x)=2x.$$

<a id="s7"></a>
### The differentiation rules — each one proven

*Every rule is derived once from the limit definition; then you only use the rules.*

**Basic rules**

$$\tfrac{d}{dx}[c]=0,\quad \tfrac{d}{dx}[x^n]=nx^{n-1},\quad (cf)'=cf',\quad (f\pm g)'=f'\pm g'$$

**★ The famous, everyday derivatives**

$$\tfrac{d}{dx}e^{x}=e^{x},\qquad \tfrac{d}{dx}\sqrt{x}=\tfrac{1}{2\sqrt{x}},\qquad \tfrac{d}{dx}\tfrac1x=-\tfrac{1}{x^{2}}$$

*$e^x$ is the most famous derivative in math — the only function (up to a constant) equal to its own derivative, which is why it governs growth and decay. The other two are the everyday special cases of the power rule.*

**Demonstration — power rule (binomial theorem)**

1. $(x+h)^n=x^n+nx^{n-1}h+\tfrac{n(n-1)}2x^{n-2}h^2+\cdots$
2. Subtract $x^n$, divide by $h$:

   $$nx^{n-1}+\tfrac{n(n-1)}2x^{n-2}h+\cdots$$
3. Let $h\to0$: everything with an $h$ dies, leaving $nx^{n-1}$. Works for fractional and negative $n$ too.

**Product, quotient, chain**

$$(fg)'=f'g+fg',\quad \Big(\tfrac fg\Big)'=\tfrac{f'g-fg'}{g^2},\quad \tfrac{d}{dx}f(g(x))=f'(g(x))g'(x)$$

**Demonstration — product rule (add-and-subtract)**

1. Insert $\pm f(x+h)g(x)$ in the numerator of the difference quotient.
2. Regroup:

   $$f(x+h)\frac{g(x+h)-g(x)}h+g(x)\frac{f(x+h)-f(x)}h.$$
3. Let $h\to0$: $\Rightarrow fg'+gf'$. The quotient rule then follows by writing $f=(f/g)\,g$ and applying this; the chain rule follows from $\frac{\Delta y}{\Delta x}=\frac{\Delta y}{\Delta u}\frac{\Delta u}{\Delta x}$.

> **Forward link**
>
> Read backwards, the **product rule → integration by parts** and the **chain rule → u-substitution** (Section 18). We derive both there.

<a id="s8"></a>
### Derivatives of every standard function

*Trig, exponential, logarithmic, inverse, and hyperbolic — with the key proofs.*

| Function | Derivative | Function | Derivative |
| --- | --- | --- | --- |
| $\sin x$ | $\cos x$ | $\sec x$ | $\sec x\tan x$ |
| $\cos x$ | $-\sin x$ | $\csc x$ | $-\csc x\cot x$ |
| $\tan x$ | $\sec^2 x$ | $\cot x$ | $-\csc^2 x$ |
| $e^x$ | $e^x$ | $\ln x$ | $1/x$ |
| $a^x$ | $a^x\ln a$ | $\log_a x$ | $1/(x\ln a)$ |
| $\arcsin x$ | $1/\sqrt{1-x^2}$ | $\arctan x$ | $1/(1+x^2)$ |
| $\sinh x$ | $\cosh x$ | $\cosh x$ | $\sinh x$ |

> **Concept — where $e$ comes from**
>
> $e$ is *defined* as the base that makes the exponential its own derivative. Equivalently, from continuously compounded interest: $e=\lim_{n\to\infty}(1+\tfrac1n)^n\approx2.718$. The number is chosen precisely so that $\frac{e^h-1}{h}\to1$.

**Demonstration — $(\sin x)'=\cos x$ and $(e^x)'=e^x$**

1. For sine, expand $\sin(x+h)=\sin x\cos h+\cos x\sin h$; the difference quotient splits into

   $$\sin x\frac{\cos h-1}{h}+\cos x\frac{\sin h}{h}\to \sin x\cdot0+\cos x\cdot1=\cos x.$$
2. For $e^x$, factor:

   $$\frac{e^{x+h}-e^x}{h}=e^x\frac{e^h-1}{h}\to e^x\cdot1=e^x.$$

**Derivative of an inverse function**

$$\big(f^{-1}\big)'(x)=\frac{1}{f'\!\big(f^{-1}(x)\big)}$$

*Proof idea: differentiate $f(f^{-1}(x))=x$ by the chain rule. This is exactly how $(\ln x)'=1/x$ and the inverse-trig derivatives are obtained.*

> **Concept — simple harmonic motion**
>
> Because $(\sin)'=\cos$ and $(\cos)'=-\sin$, the function $y=\sin(\omega t)$ satisfies $y''=-\omega^2 y$: acceleration proportional to displacement, pointing back to center. That single relationship is why sines and cosines model springs, pendulums, sound, and AC current.

<a id="s9"></a>
### Implicit differentiation & related rates

*For curves not solved for y, and for problems where several quantities change together in time.*

**Demonstration — implicit slope on $x^2+y^2=25$**

1. Differentiate, treating $y$ as a function of $x$:

   $$2x+2y\frac{dy}{dx}=0.$$
2. Solve:

   $$\frac{dy}{dx}=-\frac xy.$$

*Every $y$-term picks up $dy/dx$ — the chain rule at work.*

> **Principle — related rates**
>
> When variables are tied by an equation and all change with time, **differentiate the relation with respect to $t$**. Each variable contributes its own rate via the chain rule, linking the unknown rate to known ones.

**Demonstration — a ladder sliding down a wall**

1. Relation (Pythagoras):

   $$x^2+y^2=L^2.$$
2. Differentiate in $t$:

   $$2x\frac{dx}{dt}+2y\frac{dy}{dt}=0.$$
3. Solve for the wanted rate: Plug in the known position and $dx/dt$.

   $$\frac{dy}{dt}=-\frac{x}{y}\frac{dx}{dt}.$$

**Higher-order derivatives**

$$f''=\frac{d}{dx}f',\qquad f^{(n)}=\frac{d^n y}{dx^n}$$

*Position → velocity $s'$ → acceleration $s''$. The second derivative also controls concavity (Section 10).*

## Part D · Using derivatives

<a id="s10"></a>
### Extrema, Rolle's theorem & the Mean Value Theorem

*How the derivative reveals the shape, peaks, and valleys of a graph.*

> **Concept — extrema & critical points**
>
> A **local max/min** can only occur where $f'(x)=0$ or $f'$ is undefined — a **critical point**. (Fermat's principle: at a smooth peak the tangent is horizontal.) For a **global** extremum on $[a,b]$, also check the endpoints — guaranteed to exist by the EVT.

**Rolle's theorem → Mean Value Theorem**

$$\exists\,c\in(a,b):\ f'(c)=\frac{f(b)-f(a)}{b-a}$$

*Rolle's theorem is the case $f(a)=f(b)$ (so $f'(c)=0$). The MVT: somewhere your instantaneous rate equals your average rate — the rigorous basis for "if $f'>0$ then $f$ increases."*

**Concavity, inflection & the derivative tests**

$$f''>0:\text{concave up},\quad f''<0:\text{concave down},\quad f''\text{ changes sign}:\text{inflection}$$

$$f'(c)=0:\ f''(c)>0\Rightarrow\text{min},\quad f''(c)<0\Rightarrow\text{max}$$

<a id="s11"></a>
### Curve sketching — the table-of-signs method

*A systematic recipe that turns the derivatives into a complete picture of a graph.*

> **Principle — read the function from its derivatives**
>
> $f$ tells you height; $f'$ tells you up/down; $f''$ tells you the bend. A graph is fully pinned down by combining these three sign patterns with intercepts and asymptotes.

**The method, in order**

<a id="s12"></a>
### Optimization, linearization & Newton's method

*Three of the most useful real-world applications of the derivative.*

> **Principle — optimization**
>
> To maximize or minimize a real quantity: write it as a function of one variable (using a constraint to eliminate the others), differentiate, set $f'=0$, and test the critical points (and endpoints). The EVT guarantees the best value exists.

**Linearization & the differential**

$$L(x)=f(a)+f'(a)(x-a),\qquad dy=f'(x)\,dx$$

*Near a point, replace the curve by its tangent line for a quick estimate. The error shrinks like $(x-a)^2$. Extended forever, this becomes the Taylor series (Section 25).*

**Newton's method (root-finding)**

$$x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$$

*Follow the tangent line to where it hits the x-axis, repeat. It converges astonishingly fast (roughly doubling correct digits each step) when started near a root.*

<a id="s13"></a>
### L'Hôpital's rule — every indeterminate form

*A derivative-powered tool for limits that other methods can't crack.*

**The rule (for $0/0$ or $\infty/\infty$)**

$$\lim_{x\to a}\frac{f(x)}{g(x)}=\lim_{x\to a}\frac{f'(x)}{g'(x)}$$

> **Principle — reduce every form to a fraction**
>
> L'Hôpital only applies to $\tfrac00$ and $\tfrac\infty\infty$. The other indeterminate forms must first be **rewritten as one of these**:

| Form | How to convert |
| --- | --- |
| $0\cdot\infty$ | Rewrite as $\dfrac{0}{1/\infty}$ or $\dfrac{\infty}{1/0}$ |
| $\infty-\infty$ | Combine over a common denominator |
| $1^\infty,\ 0^0,\ \infty^0$ | Take $\ln$, find the limit, then exponentiate |

> **Why it works**
>
> Near $a$, $f\approx f'(a)(x-a)$ and $g\approx g'(a)(x-a)$; the common $(x-a)$ cancels, leaving $f'/g'$. It's local linearization again.

## Part E · Integration

<a id="s14"></a>
### Sums, area & the idea of the integral

*Before the shortcut (the FTC) comes the definition: area as an infinite sum.*

**Sigma notation & useful sums**

$$\sum_{i=1}^{n}c=nc,\quad \sum_{i=1}^{n}i=\frac{n(n+1)}2,\quad \sum_{i=1}^{n}i^2=\frac{n(n+1)(2n+1)}6$$

> **Concept — a telescoping sum**
>
> If terms cancel in cascade — $\sum (a_i-a_{i+1})=a_1-a_{n+1}$ — almost everything collapses. This is the discrete shadow of the Fundamental Theorem, where an integral collapses to its endpoint values.

**The Riemann sum → the integral**

$$\int_a^b f(x)\,dx=\lim_{n\to\infty}\sum_{i=1}^{n}f(x_i^*)\,\Delta x,\qquad \Delta x=\frac{b-a}{n}$$

*Slice the region into n rectangles, sum their areas, let the slices vanish. The integral *is* this limit. **Signed area**: regions below the axis count as negative.*

<a id="s15"></a>
### The definite integral

*Its defining properties, and two staples: area between curves and average value.*

**Properties**

$$\int_a^b f=-\int_b^a f,\quad \int_a^a f=0,\quad \int_a^b f=\int_a^c f+\int_c^b f$$

$$\int_a^b(f\pm g)=\int_a^b f\pm\int_a^b g,\qquad \int_a^b cf=c\int_a^b f$$

**Area between curves & average value**

$$A=\int_a^b\big[\text{top}-\text{bottom}\big]\,dx,\qquad \bar f=\frac{1}{b-a}\int_a^b f\,dx$$

> **Principle — the Mean Value Theorem for integrals**
>
> A continuous function attains its own average value somewhere: $\exists\,c$ with $f(c)=\bar f$. Geometrically, a rectangle of height $f(c)$ has exactly the same area as the region under the curve.

<a id="s16"></a>
### The Fundamental Theorem of Calculus

*The hinge of the subject — differentiation and integration are opposites.*

**First FTC — differentiation undoes integration**

$$\frac{d}{dx}\int_a^x f(t)\,dt=f(x)$$

**Second FTC — antiderivatives evaluate integrals**

$$\int_a^b f(x)\,dx=F(b)-F(a),\quad F'=f$$

**Demonstration — why the First FTC is true**

1. Let $A(x)=\int_a^x f(t)\,dt$. A small step $h$ adds a thin strip:

   $$A(x+h)-A(x)\approx f(x)\,h.$$
2. Divide by $h$ and let $h\to0$:

   $$A'(x)=f(x).$$

*Accumulation and rate are inverse operations. The Second FTC follows because any two antiderivatives differ only by a constant.*

**Indefinite integral**

$$\int f(x)\,dx=F(x)+C,\qquad F'=f$$

*The $+C$ appears because differentiation erases constants.*

<a id="s17"></a>
### The basic integral table

*Each line is a Section 7–8 derivative reversed. Verify any by differentiating the right side.*

| Integral | Result | Integral | Result |
| --- | --- | --- | --- |
| $\int x^n dx\,(n\neq-1)$ | $\frac{x^{n+1}}{n+1}+C$ | $\int\frac1x dx$ | $\ln\vert x\vert +C$ |
| $\int e^x dx$ | $e^x+C$ | $\int a^x dx$ | $\frac{a^x}{\ln a}+C$ |
| $\int\cos x dx$ | $\sin x+C$ | $\int\sin x dx$ | $-\cos x+C$ |
| $\int\sec^2 x dx$ | $\tan x+C$ | $\int\sec x\tan x dx$ | $\sec x+C$ |
| $\int\frac{dx}{1+x^2}$ | $\arctan x+C$ | $\int\frac{dx}{\sqrt{1-x^2}}$ | $\arcsin x+C$ |
| $\int\tan x dx$ | $\ln\vert \sec x\vert +C$ | $\int\sec x dx$ | $\ln\vert \sec x+\tan x\vert +C$ |

> **Don't memorize twice**
>
> If you know the derivative tables, you already know this one — just flip the arrow. That's the Fundamental Theorem in daily use.

<a id="s18"></a>
### Techniques of integration I — substitution, parts, partial fractions

*The first three workhorses; two are differentiation rules in reverse.*

**u-substitution & integration by parts**

$$\int f(g(x))g'(x)\,dx=\int f(u)\,du,\qquad \int u\,dv=uv-\int v\,du$$

**Demonstration — both come from earlier rules**

1. u-sub reverses the chain rule: since $\frac{d}{dx}F(g(x))=f(g(x))g'(x)$, integrating gives $F(g(x))+C=\int f(u)\,du$.
2. By parts reverses the product rule: integrate $(uv)'=u'v+uv'$ to get $uv=\int u'v+\int uv'$, then solve for $\int u\,dv=uv-\int v\,du$.

> **Concept — partial fractions**
>
> Any proper rational function splits into simple pieces — one term per linear or quadratic factor of the denominator — each of which integrates to a logarithm or an arctangent. Algebra first, calculus second.

**Partial-fraction form**

$$\frac{P(x)}{(x-r_1)(x-r_2)}=\frac{A}{x-r_1}+\frac{B}{x-r_2}$$

<a id="s19"></a>
### Techniques of integration II — trig integrals, trig substitution, reduction

*Methods aimed at powers of trig functions and stubborn square roots.*

> **Principle — powers of sin and cos**
>
> If a power is **odd**, peel off one factor to pair with $dx$ and convert the rest using $\sin^2+\cos^2=1$, then substitute. If **both are even**, use the power-reduction identities from Section 2 to lower the powers.

**Trig substitution (clearing roots)**

$$\sqrt{a^2-x^2}:x=a\sin\theta,\quad \sqrt{a^2+x^2}:x=a\tan\theta,\quad \sqrt{x^2-a^2}:x=a\sec\theta$$

*Each choice turns the root into a single trig function via a Pythagorean identity. Complete the square first if needed.*

**A reduction formula**

$$\int\sin^n x\,dx=-\frac{\sin^{n-1}x\cos x}{n}+\frac{n-1}{n}\int\sin^{n-2}x\,dx$$

*Derived by integration by parts; it lowers the power by 2 each time until you reach a base case. Such recursions tame high powers.*

<a id="s20"></a>
### Improper integrals

*Integrals with an infinite bound or an infinite value — handled as limits.*

**Definition by limit**

$$\int_a^\infty f\,dx=\lim_{t\to\infty}\int_a^t f\,dx$$

*The integral **converges** if this limit is finite, otherwise it **diverges**. Blow-ups inside the interval are split and handled the same way.*

**The p-test (the benchmark)**

$$\int_1^\infty\frac{dx}{x^p}\ \text{converges}\iff p>1,\qquad \int_0^1\frac{dx}{x^p}\ \text{converges}\iff p<1$$

> **Principle — comparison & absolute convergence**
>
> You can judge convergence without evaluating: if $0\le f\le g$ and $\int g$ converges, so does $\int f$ (**comparison test**). If $f/g$ tends to a finite positive number, both behave alike (**limit comparison**). And if $\int|f|$ converges, so does $\int f$ (**absolute convergence**).

<a id="s21"></a>
### Numerical integration

*When no antiderivative exists in closed form, approximate the integral directly.*

**Trapezoidal rule**

$$\int_a^b f\,dx\approx\frac{\Delta x}{2}\big[f_0+2f_1+2f_2+\cdots+2f_{n-1}+f_n\big]$$

*Replace each strip's top by a straight line. Error shrinks like $1/n^2$.*

**Simpson's rule (n even)**

$$\int_a^b f\,dx\approx\frac{\Delta x}{3}\big[f_0+4f_1+2f_2+4f_3+\cdots+4f_{n-1}+f_n\big]$$

*Fits parabolas instead of lines — far more accurate, with error like $1/n^4$.*

## Part F · Applications of the integral

<a id="s22"></a>
### Volumes, arc length & surface area

*Every formula follows the same recipe: write one tiny slice, then integrate.*

**Volumes of revolution**

$$\text{disk/washer: } V=\pi\int_a^b\!\big([R]^2-[r]^2\big)dx,\qquad \text{shell: } V=2\pi\int_a^b x\,f(x)\,dx$$

**General solids by cross-section**

$$V=\int_a^b A(x)\,dx$$

*If you know the area $A(x)$ of each slice (square, triangle, semicircle…), just integrate it.*

**Arc length & surface of revolution**

$$L=\int_a^b\sqrt{1+[f'(x)]^2}\,dx,\qquad S=2\pi\int_a^b f(x)\sqrt{1+[f'(x)]^2}\,dx$$

**Demonstration — the arc-length integrand**

1. A tiny segment has run $dx$ and rise $dy$; by Pythagoras $ds=\sqrt{dx^2+dy^2}$.
2. Factor out $dx$: $ds=\sqrt{1+(dy/dx)^2}\,dx$. Integrate to total the length. Surface area multiplies each $ds$ by the circumference $2\pi f(x)$ it sweeps.

## Part G · Sequences & series

<a id="s23"></a>
### Sequences

*An ordered list of numbers; the question is where it heads.*

> **Concept — convergence of a sequence**
>
> $a_n\to L$ means the terms get and stay arbitrarily close to $L$. A sequence that is **bounded and monotonic** must converge (a foundational principle). Limits of sequences obey the same laws as limits of functions.

**Three key sequence limits**

$$\lim_{n\to\infty}r^n=0\ (|r|<1),\qquad \lim_{n\to\infty}n^{1/n}=1,\qquad \lim_{n\to\infty}\Big(1+\frac xn\Big)^n=e^x$$

<a id="s24"></a>
### Series & convergence tests

*Adding infinitely many terms — and the full toolkit for deciding whether the total is finite.*

**Geometric series & p-series**

$$\sum_{n=0}^\infty ar^n=\frac{a}{1-r}\ (|r|<1),\qquad \sum_{n=1}^\infty\frac1{n^p}\ \text{converges}\iff p>1$$

**Demonstration — the geometric sum**

1. $S_n=a+ar+\cdots+ar^{n-1}$; multiply by $r$ and subtract: $S_n-rS_n=a-ar^n$.
2. So $S_n=\frac{a(1-r^n)}{1-r}$; if $|r|<1$, $r^n\to0$, giving $\frac{a}{1-r}$.

| Test | Use it when… |
| --- | --- |
| nth-term (divergence) | $\lim a_n\neq0$ ⟹ diverges (a quick first check) |
| Ratio | factorials or $n$th powers; converges if $\lim\vert a_{n+1}/a_n\vert <1$ |
| Root | whole expression raised to the $n$; converges if $\lim\vert a_n\vert ^{1/n}<1$ |
| Comparison / limit comparison | terms resemble a known series |
| Integral | $a_n=f(n)$ with $f$ positive, decreasing |
| Alternating | signs alternate and $\vert a_n\vert $ decreases to 0 |

> **Principle — absolute vs conditional convergence**
>
> If $\sum|a_n|$ converges, the series converges **absolutely** (and you may reorder it freely). If $\sum a_n$ converges but $\sum|a_n|$ does not, it converges **conditionally** — fragile, and reordering can change the sum (e.g. the alternating harmonic series).

<a id="s25"></a>
### Taylor & power series

*Rebuilding a function from its derivatives — the climax of single-variable calculus.*

**Taylor's theorem with remainder**

$$f(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k+R_n,\qquad R_n=\frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$$

*The remainder term $R_n$ bounds the error of the polynomial approximation — this is what makes Taylor series *usable* for estimates, not just elegant.*

**Demonstration — why coefficients are $f^{(n)}(a)/n!$**

1. Assume $f(x)=\sum c_k(x-a)^k$. Setting $x=a$ gives $c_0=f(a)$.
2. Differentiate $n$ times and set $x=a$: only the $(x-a)^n$ term survives as $n!\,c_n$, so $c_n=\frac{f^{(n)}(a)}{n!}$.

**The famous expansions**

$$e^x=\sum\frac{x^n}{n!},\quad \sin x=x-\frac{x^3}{3!}+\cdots,\quad \cos x=1-\frac{x^2}{2!}+\cdots$$

$$\frac1{1-x}=\sum x^n,\quad \ln(1+x)=x-\frac{x^2}2+\cdots,\quad (1+x)^k=\sum\binom{k}{n}x^n$$

> **Concept — radius of convergence**
>
> A power series $\sum c_n(x-a)^n$ converges only within a distance $R$ of its center $a$ (the **radius of convergence**, usually found by the ratio test), and you must check the two endpoints separately. Inside that interval you may **differentiate and integrate term by term** — the easiest way to generate new series from known ones.

## Part H · Further topics

<a id="s26"></a>
### Parametric equations

*Describe a curve by a moving point $(x(t),y(t))$ — ideal for paths and motion.*

**Slope, second derivative, arc length**

$$\frac{dy}{dx}=\frac{dy/dt}{dx/dt},\qquad L=\int_{t_1}^{t_2}\sqrt{\Big(\tfrac{dx}{dt}\Big)^2+\Big(\tfrac{dy}{dt}\Big)^2}\,dt$$

*The arc-length integrand is just $ds=\sqrt{dx^2+dy^2}$ again — speed integrated over time gives distance traveled.*

<a id="s27"></a>
### Polar coordinates

*Locate points by distance $r$ and angle $\theta$ instead of $x$ and $y$.*

**Conversion**

$$x=r\cos\theta,\quad y=r\sin\theta,\quad r^2=x^2+y^2,\quad \tan\theta=\frac yx$$

**Area enclosed by a polar curve**

$$A=\frac12\int_\alpha^\beta r(\theta)^2\,d\theta$$

*The slice here is a thin circular sector (area $\tfrac12 r^2\,d\theta$), not a rectangle — same "sum tiny slices" principle, new slice shape.*

<a id="s28"></a>
### Complex numbers & Euler's identity

*Where exponentials and trigonometry turn out to be the same thing.*

**Basics & polar form**

$$i^2=-1,\quad z=a+bi=r(\cos\theta+i\sin\theta)=re^{i\theta}$$

**Euler's formula, De Moivre & the identity**

$$e^{i\theta}=\cos\theta+i\sin\theta,\quad (\cos\theta+i\sin\theta)^n=\cos n\theta+i\sin n\theta,\quad e^{i\pi}+1=0$$

> **The unity**
>
> Substituting $x=i\theta$ into the Taylor series for $e^x$ and regrouping into the $\cos$ and $\sin$ series yields Euler's formula directly. The series built from derivatives ties exponential growth to oscillation.

<a id="s29"></a>
### Differential equations

*Equations involving a function and its derivatives — the language calculus speaks to science.*

> **Concept — what a differential equation is**
>
> It relates a quantity to its own rate of change. **Exponential growth/decay** $\frac{dy}{dt}=ky$ has solution $y=y_0e^{kt}$ — the purest statement that "change is proportional to amount."

**Separable equations**

$$\frac{dy}{dx}=g(x)h(y)\ \Rightarrow\ \int\frac{dy}{h(y)}=\int g(x)\,dx$$

**First-order linear (integrating factor)**

$$y'+P(x)y=Q(x),\qquad \mu=e^{\int P\,dx},\qquad (\mu y)'=\mu Q$$

**Constant-coefficient homogeneous**

$$ay''+by'+cy=0 \ \Rightarrow\ ar^2+br+c=0$$

*The roots of this characteristic quadratic decide the solution: two real roots → $e^{r_1x},e^{r_2x}$; a repeated root → $e^{rx},xe^{rx}$; complex roots → $e^{\alpha x}\cos\beta x,\ e^{\alpha x}\sin\beta x$ (oscillation, via Euler).*

<a id="beyond"></a>
### What comes next

This guide covers the standard **single-variable** course, the scope of the Princeton review book. The same two ideas — slope and accumulation — generalize:

- **Multivariable calculus:** partial derivatives $\partial f/\partial x$, the gradient $\nabla f$, and double/triple integrals $\iint,\iiint$.
- **Vector calculus:** Green's, Stokes', and the Divergence theorems — each a higher-dimensional Fundamental Theorem, again saying that behavior on a boundary is governed by behavior inside.

> **The habit to keep**
>
> Whenever you meet a new formula, ask which earlier one it is secretly a version of — and try to reproduce its demonstration. Nearly everything in calculus is built from limits, the product rule, and the chain rule.

---

*Structured to follow Adrian Banner's *The Calculus Lifesaver: All the Tools You Need to Excel at Calculus* (Princeton University Press) — a single-variable companion covering concepts, principles, formulas, and the demonstrations behind them. Read once for the shape; return to any box as a reference.*
