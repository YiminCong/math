# Calculus, *connected.*

Every formula here grows out of one of two ideas: **the limit**, and what happens when you let something get infinitely small. Read it top to bottom and each piece will lean on the one before it.

[← Back to all guides](../README.md)

<a id="s0"></a>
## The big picture before any symbols

*If you hold one map in your head, hold this one.*

All of calculus is two questions about change, plus a stunning discovery that they are opposites.

- **The derivative** asks: *how fast is this changing right now?* (a slope, a speed, a rate)
- **The integral** asks: *how much has accumulated in total?* (an area, a distance, a sum)

Both are built by taking something you understand for ordinary numbers (a slope between two points, the area of a rectangle) and pushing it to a **limit** — letting a gap shrink toward zero. So we must understand limits first.

### The whole course on one line

> Limits → Derivatives → Integrals ↔ (linked by the FTC) → Series → Multivariable

> **The connection to watch for**
>
> The single most important relationship in the subject is the **Fundamental Theorem of Calculus** (Section 7): differentiation and integration undo each other. Every integration formula in Sections 8–9 is just a differentiation formula from Sections 3–4 read backwards.

<a id="s1"></a>
## Limits & continuity

The foundation. A limit answers: where is the function *heading* as the input approaches a value — even if it never arrives?

**Intuitive limit**

$$\lim_{x \to a} f(x) = L$$

*As $x$ gets arbitrarily close to $a$, $f(x)$ gets arbitrarily close to $L$.*

**Formal (ε–δ) definition**

$$\forall\, \varepsilon>0,\; \exists\, \delta>0 \;:\; 0<|x-a|<\delta \implies |f(x)-L|<\varepsilon$$

*"Name any tolerance ε around L; I can find a window δ around a that keeps me inside it." This is the rigorous engine behind everything else.*

### Limit laws (how limits combine)

If $\lim_{x\to a} f = L$ and $\lim_{x\to a} g = M$, then limits pass cleanly through arithmetic:

$$\lim (f \pm g) = L \pm M \qquad \lim (fg)=LM \qquad \lim \frac{f}{g}=\frac{L}{M}\;(M\neq 0)$$

$$\lim\, c\,f = cL \qquad \lim \big(f(x)\big)^n = L^{\,n}$$

**Squeeze (sandwich) theorem**

$$g(x)\le f(x)\le h(x)\ \text{ and }\ \lim_{x\to a}g=\lim_{x\to a}h=L \implies \lim_{x\to a}f=L$$

### Special limits worth memorizing

$$\lim_{x\to 0}\frac{\sin x}{x}=1 \qquad \lim_{x\to 0}\frac{1-\cos x}{x}=0 \qquad \lim_{x\to\infty}\Big(1+\tfrac{1}{x}\Big)^{x}=e$$

*The first one is the seed of the derivative of sine. The last one is where the number e is born.*

**Continuity at a point**

$$f \text{ is continuous at } a \iff \lim_{x\to a} f(x) = f(a)$$

*Three things must agree: the limit exists, the value exists, and they match. No holes, jumps, or breaks.*

> **Why this matters next**
>
> A function must be continuous to be differentiable. And the derivative itself is *defined* as a limit — so Section 2 is really just one careful application of everything above.

<a id="s2"></a>
## What a derivative *is*

*Take the slope between two points, then slide them together. That limit is the derivative.*

**The definition (limit of a difference quotient)**

$$f'(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}$$

*$\frac{f(x+h)-f(x)}{h}$ is the slope of a line through two nearby points (the "secant"). Letting $h\to 0$ tilts it into the tangent line.*

**Equivalent form (at a specific point a)**

$$f'(a)=\lim_{x\to a}\frac{f(x)-f(a)}{x-a}$$

### What it means

- **Geometrically:** the slope of the tangent line to the curve at $x$.
- **Physically:** the instantaneous rate of change. If $s(t)$ is position, $s'(t)$ is velocity.

### The many ways to write it

`$f'(x)$ — Lagrange` · `$\dfrac{dy}{dx}$ — Leibniz` · `$\dot{y}$ — Newton` · `$D_x f$ — operator`

> **Demonstration — derive the power rule from scratch**
>
> Let $f(x)=x^2$. Plug into the definition:
>
> $$ f'(x)=\lim_{h\to0}\frac{(x+h)^2-x^2}{h}=\lim_{h\to0}\frac{x^2+2xh+h^2-x^2}{h} $$
>
> $$ =\lim_{h\to0}\frac{2xh+h^2}{h}=\lim_{h\to0}(2x+h)=2x. $$
>
> So $\frac{d}{dx}x^2 = 2x$ — exactly what the power rule $nx^{n-1}$ predicts. The rules in Section 3 are shortcuts so you never have to do this by hand again.

<a id="s3"></a>
## Differentiation rules

*These let you differentiate any combination of functions without returning to the limit definition.*

**Constant**

$$\frac{d}{dx}[c]=0$$

**Power rule — the workhorse**

$$\frac{d}{dx}\big[x^{n}\big]=n\,x^{\,n-1}$$

**Constant multiple**

$$\frac{d}{dx}\big[c\,f(x)\big]=c\,f'(x)$$

**Sum / difference**

$$(f\pm g)'=f'\pm g'$$

**Product rule**

$$(fg)' = f'g + fg'$$

*"First times derivative of second, plus second times derivative of first." Not f'g' — that's the classic trap.*

**Quotient rule**

$$\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^{2}}$$

*"Low d-high minus high d-low, over low squared."*

**Chain rule — for functions inside functions**

$$\frac{d}{dx}\,f\big(g(x)\big)=f'\big(g(x)\big)\cdot g'(x) \qquad\text{or}\qquad \frac{dy}{dx}=\frac{dy}{du}\cdot\frac{du}{dx}$$

*Differentiate the outer layer, keep the inside intact, then multiply by the derivative of the inside.*

> **Forward link**
>
> Keep the **product rule** and **chain rule** in mind. Read backwards, the product rule becomes *integration by parts* and the chain rule becomes *u-substitution* — the two big integration techniques in Section 9.

<a id="s4"></a>
## Derivatives of the standard functions

*Combine these with the rules above and you can differentiate almost anything.*

### Exponential & logarithmic

| Function | Derivative |
| --- | --- |
| $e^{x}$ | $e^{x}$  *(the function that is its own derivative)* |
| $a^{x}$ | $a^{x}\ln a$ |
| $\ln x$ | $\dfrac{1}{x}$ |
| $\log_a x$ | $\dfrac{1}{x\ln a}$ |

### Trigonometric

| Function | Derivative | Function | Derivative |
| --- | --- | --- | --- |
| $\sin x$ | $\cos x$ | $\cot x$ | $-\csc^{2}x$ |
| $\cos x$ | $-\sin x$ | $\sec x$ | $\sec x\tan x$ |
| $\tan x$ | $\sec^{2}x$ | $\csc x$ | $-\csc x\cot x$ |

### Inverse trigonometric

| Function | Derivative |
| --- | --- |
| $\arcsin x$ | $\dfrac{1}{\sqrt{1-x^{2}}}$ |
| $\arccos x$ | $-\dfrac{1}{\sqrt{1-x^{2}}}$ |
| $\arctan x$ | $\dfrac{1}{1+x^{2}}$ |

> **A quiet symmetry**
>
> Notice the pairs: $(\sin)'=\cos$ and $(\cos)'=-\sin$. Differentiating sine four times returns you to sine. These cycles are exactly why $\sin$ and $\cos$ describe everything that oscillates.

<a id="s5"></a>
## Implicit, logarithmic & higher-order derivatives

*Three extensions for when y is tangled up, the exponents are messy, or you need to differentiate more than once.*

**Implicit differentiation**

$$\frac{d}{dx}\big[\,y\,\big]=\frac{dy}{dx},\qquad \frac{d}{dx}\big[\,y^{2}\,\big]=2y\frac{dy}{dx}$$

*When y is defined implicitly (e.g. $x^2+y^2=25$), differentiate both sides treating y as a function of x — every y-term picks up a $dy/dx$ by the chain rule — then solve for $dy/dx$.*

**Logarithmic differentiation**

$$y=f(x)^{g(x)} \;\Rightarrow\; \ln y = g(x)\ln f(x) \;\Rightarrow\; \frac{y'}{y}=\frac{d}{dx}\big[g\ln f\big]$$

*Take ln of both sides first to turn powers into products. Essential for things like $x^{x}$.*

**Higher-order derivatives**

$$f''(x)=\frac{d}{dx}f'(x),\qquad f^{(n)}(x)=\frac{d^{\,n}y}{dx^{\,n}}$$

*Second derivative = rate of change of the rate of change. If $s(t)$ is position, $s'$ is velocity and $s''$ is acceleration.*

<a id="s6"></a>
## Putting derivatives to work

*The payoff: tangent lines, shapes of curves, optimization, and limits that looked impossible.*

**Tangent line at x = a**

$$y - f(a) = f'(a)\,(x-a)$$

### Reading the shape of a curve

- $f'(x)>0$ → function **increasing**; $f'(x)<0$ → **decreasing**.
- **Critical points** where $f'(x)=0$ or is undefined are candidates for maxima/minima.
- $f''(x)>0$ → **concave up** (cup); $f''(x)<0$ → **concave down** (cap).
- **Inflection point**: where $f''$ changes sign.

**Second-derivative test**

$$f'(c)=0:\quad f''(c)>0 \Rightarrow \text{local min},\qquad f''(c)<0 \Rightarrow \text{local max}$$

**Mean Value Theorem**

$$\exists\, c\in(a,b):\quad f'(c)=\frac{f(b)-f(a)}{b-a}$$

*Somewhere in the interval, the instantaneous slope equals the average slope. (Rolle's theorem is the special case where $f(a)=f(b)$, giving $f'(c)=0$.)*

**L'Hôpital's rule — for 0/0 or ∞/∞**

$$\lim_{x\to a}\frac{f(x)}{g(x)} = \lim_{x\to a}\frac{f'(x)}{g'(x)}$$

*When a limit is an indeterminate form, differentiate top and bottom separately and try again. A beautiful loop back to Section 1.*

**Linear approximation & differentials**

$$f(x)\approx f(a)+f'(a)(x-a),\qquad dy=f'(x)\,dx$$

*Near a point, every smooth curve looks like its tangent line. This idea, extended, becomes Taylor series in Section 11.*

<a id="s7"></a>
## The antiderivative & the Fundamental Theorem

*The hinge of the entire subject. Here the derivative and the integral are revealed to be two sides of one coin.*

**Indefinite integral (antiderivative)**

$$\int f(x)\,dx = F(x)+C \quad\text{where}\quad F'(x)=f(x)$$

*Integrating means asking "what function has THIS as its derivative?" The $+C$ appears because constants vanish when differentiated.*

**Definite integral as a limit of Riemann sums**

$$\int_{a}^{b} f(x)\,dx = \lim_{n\to\infty}\sum_{i=1}^{n} f(x_i^{*})\,\Delta x$$

*Slice the area under the curve into n thin rectangles, add them, and let the slices become infinitely thin. The integral IS an infinite sum — note the same "push to a limit" move that built the derivative.*

### The Fundamental Theorem of Calculus

**Part 1 — differentiation undoes integration**

$$\frac{d}{dx}\int_{a}^{x} f(t)\,dt = f(x)$$

**Part 2 — integration is evaluated by antiderivatives**

$$\int_{a}^{b} f(x)\,dx = F(b)-F(a),\quad F'=f$$

> **The payoff**
>
> Part 2 is astonishing: to find an area (an infinite sum of rectangles), you don't add anything — you just find an antiderivative and subtract two values. This is why every derivative formula in Sections 3–4 instantly becomes an integral formula in Section 8, simply by reading the table backwards.

<a id="s8"></a>
## The basic integral table

*Each line is a derivative rule run in reverse. Compare it directly to Sections 3–4.*

**Power rule for integrals (reverse of the power rule)**

$$\int x^{n}\,dx = \frac{x^{\,n+1}}{n+1}+C \quad (n\neq -1)$$

**The n = −1 exception**

$$\int \frac{1}{x}\,dx = \ln|x|+C$$

| Integral | Result | Reverse of… |
| --- | --- | --- |
| $\int e^{x}\,dx$ | $e^{x}+C$ | $(e^x)'=e^x$ |
| $\int a^{x}\,dx$ | $\dfrac{a^{x}}{\ln a}+C$ | $(a^x)'=a^x\ln a$ |
| $\int \cos x\,dx$ | $\sin x+C$ | $(\sin x)'=\cos x$ |
| $\int \sin x\,dx$ | $-\cos x+C$ | $(\cos x)'=-\sin x$ |
| $\int \sec^{2}x\,dx$ | $\tan x+C$ | $(\tan x)'=\sec^2 x$ |
| $\int \dfrac{1}{1+x^{2}}\,dx$ | $\arctan x+C$ | $(\arctan x)'=\frac{1}{1+x^2}$ |
| $\int \dfrac{1}{\sqrt{1-x^{2}}}\,dx$ | $\arcsin x+C$ | $(\arcsin x)'=\frac{1}{\sqrt{1-x^2}}$ |

> **How to read this section**
>
> Don't memorize this table separately. If you know the derivative table cold, you already know the integral table — just flip the arrow. That is the whole point of the Fundamental Theorem.

<a id="s9"></a>
## Integration techniques

*When an integral doesn't match the table, these tools reshape it until it does. Two of them are differentiation rules in reverse.*

**u-substitution — the chain rule, reversed**

$$\int f\big(g(x)\big)\,g'(x)\,dx = \int f(u)\,du,\qquad u=g(x)$$

*Spot an inside function and its derivative both present; rename the inside as u. This undoes the chain rule from Section 3.*

**Integration by parts — the product rule, reversed**

$$\int u\,dv = uv - \int v\,du$$

*Comes straight from integrating the product rule $(uv)'=u'v+uv'$. Use it for products like $\int x e^{x}\,dx$ or $\int x\ln x\,dx$.*

**Trigonometric substitution**

$$\sqrt{a^2-x^2}\Rightarrow x=a\sin\theta,\quad \sqrt{a^2+x^2}\Rightarrow x=a\tan\theta,\quad \sqrt{x^2-a^2}\Rightarrow x=a\sec\theta$$

*Trade an awkward square root for a clean trig identity.*

**Partial fractions**

$$\frac{P(x)}{(x-r_1)(x-r_2)} = \frac{A}{x-r_1}+\frac{B}{x-r_2}$$

*Break a complicated rational function into simple pieces, each of which integrates to a logarithm or arctangent.*

### Useful properties of definite integrals

$$\int_a^b f\,dx = -\int_b^a f\,dx,\qquad \int_a^a f\,dx = 0,\qquad \int_a^b f\,dx = \int_a^c f\,dx + \int_c^b f\,dx$$

> **The mirror, made explicit**
>
> Chain rule ⟷ u-substitution. Product rule ⟷ integration by parts. Differentiation has clean, always-works rules; integration is the reverse search, so it needs clever techniques. Same relationships, harder direction.

<a id="s10"></a>
## Putting integrals to work

*Anything that accumulates — area, volume, length, averages — is an integral.*

**Area between two curves**

$$A=\int_a^b \big[\,f(x)-g(x)\,\big]\,dx$$

**Volume of revolution — disk method**

$$V=\pi\int_a^b \big[f(x)\big]^2\,dx$$

**Volume of revolution — shell method**

$$V=2\pi\int_a^b x\,f(x)\,dx$$

**Arc length of a curve**

$$L=\int_a^b \sqrt{1+\big[f'(x)\big]^2}\;dx$$

**Average value of a function**

$$\bar f=\frac{1}{b-a}\int_a^b f(x)\,dx$$

> **The common thread**
>
> Every formula here follows the same recipe: take a tiny slice (a sliver of area, a thin disk, a short segment), write its size, then integrate to add up infinitely many of them. That is the Riemann-sum idea from Section 7 applied over and over.

<a id="s11"></a>
## Sequences & series

*What happens when you add infinitely many terms? Sometimes the total is finite — and that lets us rebuild functions from their derivatives.*

**Geometric series**

$$\sum_{n=0}^{\infty} a r^{n} = \frac{a}{1-r}\quad (|r|<1)$$

**p-series (convergence test case)**

$$\sum_{n=1}^{\infty}\frac{1}{n^{p}}\ \text{converges} \iff p>1$$

### Convergence tests (does the sum settle down?)

| Test | Rule of thumb |
| --- | --- |
| Ratio test | $\lim\left\vert \dfrac{a_{n+1}}{a_n}\right\vert =L$; converges if $L<1$ |
| Comparison | Bound your series by a known one |
| Integral test | $\sum a_n$ and $\int f\,dx$ converge together |

**Taylor series — a function rebuilt from its derivatives**

$$f(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}\,(x-a)^{n}$$

*Maclaurin series is the special case $a=0$. This is the linear approximation of Section 6, continued to infinitely many derivatives.*

### The famous expansions

$$e^{x}=\sum_{n=0}^{\infty}\frac{x^{n}}{n!}=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots$$

$$\sin x = x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots \qquad \cos x = 1-\frac{x^2}{2!}+\frac{x^4}{4!}-\cdots$$

$$\frac{1}{1-x}=\sum_{n=0}^{\infty}x^{n}\quad(|x|<1)$$

> **A glimpse of the unity**
>
> Feed $x=i\theta$ into the series for $e^x$ and compare with $\sin$ and $\cos$, and you land on Euler's formula $e^{i\theta}=\cos\theta+i\sin\theta$. The series built from derivatives quietly ties exponentials to oscillation.

<a id="s12"></a>
## A peek at multivariable calculus

*The same two ideas — slope and accumulation — in more than one dimension.*

**Partial derivative**

$$\frac{\partial f}{\partial x}=\lim_{h\to0}\frac{f(x+h,\,y)-f(x,\,y)}{h}$$

*Differentiate with respect to one variable while treating the others as constants. Exactly the Section 2 definition, holding y still.*

**Gradient (vector of all partials)**

$$\nabla f = \left\langle \frac{\partial f}{\partial x},\ \frac{\partial f}{\partial y},\ \frac{\partial f}{\partial z} \right\rangle$$

*Points in the direction of steepest increase — the multivariable cousin of the derivative.*

**Double integral (accumulation over a region)**

$$\iint_{R} f(x,y)\,dA = \int_{c}^{d}\!\int_{a}^{b} f(x,y)\,dx\,dy$$

*Volume under a surface, built from the same Riemann-sum idea — now stacking tiny boxes instead of rectangles.*

> **Where it all goes**
>
> From here the path continues to the great integral theorems (Green's, Stokes', Divergence) — each one a higher-dimensional Fundamental Theorem of Calculus, saying again that what happens on a boundary is governed by what happens inside.

---

*Read it once for the shape, then return to any section as a reference. The deepest habit to build: whenever you meet a new formula, ask which earlier idea it is secretly a version of. In calculus, almost everything is.*
