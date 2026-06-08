**English** · [中文](derived-from-scratch.zh.md)

# Calculus, *derived.*

Not just a list of formulas — every core formula below is **demonstrated**: shown where it comes from, step by step. The order runs basics → advanced, and each piece is built from the one before it.

[← Back to all guides](../README.md)

<a id="s0"></a>
## The big picture before any symbols

*One map to hold in your head.*

All of calculus is two questions about change, plus a discovery that they are opposites.

- **The derivative** asks: *how fast is this changing right now?* (a slope, a speed, a rate)
- **The integral** asks: *how much has accumulated in total?* (an area, a distance, a sum)

Both are built by taking something simple — a slope between two points, the area of a rectangle — and pushing it to a **limit**, letting a gap shrink to zero. So limits come first.

### The whole course on one line

> Limits → Derivatives → Integrals ↔ (linked by the FTC) → Series → Multivariable

> **The thread to follow**
>
> The **Fundamental Theorem of Calculus** (Section 7) says differentiation and integration undo each other. Because of it, every integration formula in Sections 8–9 is a differentiation formula from Sections 3–4 read backwards — and we will literally derive them that way.

<a id="s1"></a>
## Limits & continuity

*A limit answers: where is the function heading as the input approaches a value — even if it never arrives?*

**Intuitive limit**

$$\lim_{x \to a} f(x) = L$$

*As $x$ gets arbitrarily close to $a$, $f(x)$ gets arbitrarily close to $L$.*

**Formal (ε–δ) definition**

$$\forall\, \varepsilon>0,\; \exists\, \delta>0 \;:\; 0<|x-a|<\delta \implies |f(x)-L|<\varepsilon$$

*Name any tolerance ε around L; I can find a window δ around a that keeps me inside it.*

**One-sided & existence**

$$\lim_{x\to a^-}f(x)=\lim_{x\to a^+}f(x)=L \iff \lim_{x\to a}f(x)=L$$

*The two-sided limit exists only when the left and right approaches agree.*

**Limits at infinity / infinite limits**

$$\lim_{x\to\infty}\frac{1}{x}=0, \qquad \lim_{x\to 0^+}\frac{1}{x}=+\infty$$

### Limit laws (how limits combine)

If $\lim f = L$ and $\lim g = M$:

$$\lim (f \pm g)=L\pm M,\quad \lim (fg)=LM,\quad \lim \tfrac{f}{g}=\tfrac{L}{M}\,(M\neq0),\quad \lim cf=cL$$

**Squeeze (sandwich) theorem**

$$g(x)\le f(x)\le h(x)\ \text{and}\ \lim g=\lim h=L \implies \lim f=L$$

### The special limits — and where they come from

**Three limits to know**

$$\lim_{x\to0}\frac{\sin x}{x}=1,\qquad \lim_{x\to0}\frac{1-\cos x}{x}=0,\qquad \lim_{x\to0}\frac{e^{x}-1}{x}=1$$

**Demonstration — why $ \lim_{x\to0}\frac{\sin x}{x}=1 $**

1. For a small angle $x$ (in radians, $0

   $$\sin x < x < \tan x.$$
2. Divide every part by $\sin x>0$:

   $$1 < \frac{x}{\sin x} < \frac{1}{\cos x}.$$
3. Flip all three (reversing the inequalities):

   $$\cos x < \frac{\sin x}{x} < 1.$$
4. As $x\to0$, $\cos x\to1$. The fraction is squeezed between two things heading to 1, so by the Squeeze Theorem it also $\to1$.

*This single limit is what makes $(\sin x)'=\cos x$ work in Section 4.*

**Continuity at a point**

$$f \text{ continuous at } a \iff \lim_{x\to a} f(x)=f(a)$$

*Limit exists, value exists, and they match — no hole, jump, or break.*

**Intermediate Value Theorem**

$$f \text{ continuous on } [a,b],\ N \text{ between } f(a),f(b) \implies \exists\, c\in(a,b):\ f(c)=N$$

*A continuous curve can't skip a value — it must pass through every height in between. (This is why root-finding works.)*

> **Why this matters next**
>
> Differentiability requires continuity, and the derivative is itself *defined* as a limit. Section 2 is one careful application of everything above.

<a id="s2"></a>
## The definition of the derivative

*Take the slope between two points, then slide them together.*

**Definition (limit of a difference quotient)**

$$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$$

*$\frac{f(x+h)-f(x)}{h}$ is the slope of a secant line through two nearby points; $h\to0$ tilts it into the tangent.*

**Equivalent form at a point**

$$f'(a)=\lim_{x\to a}\frac{f(x)-f(a)}{x-a}$$

`$f'(x)$ — Lagrange` · `$\dfrac{dy}{dx}$ — Leibniz` · `$\dot y$ — Newton` · `$D_xf$ — operator`

**Demonstration — derivative of $f(x)=x^2$ from the definition**

1. Substitute into the definition:

   $$f'(x)=\lim_{h\to0}\frac{(x+h)^2-x^2}{h}.$$
2. Expand the top:

   $$(x+h)^2-x^2 = x^2+2xh+h^2-x^2 = 2xh+h^2.$$
3. Divide by $h$ (allowed since $h\neq0$ inside the limit):

   $$\frac{2xh+h^2}{h}=2x+h.$$
4. Let $h\to0$:

   $$f'(x)=2x.$$

*Matches the power rule $nx^{n-1}$. Next we prove that rule in general.*

<a id="s3"></a>
## The differentiation rules — each one proven

*Every rule below is derived from the limit definition. Once proven, you never touch the definition again.*

**Constant & basic rules**

$$\frac{d}{dx}[c]=0,\quad \frac{d}{dx}[cf]=cf',\quad (f\pm g)'=f'\pm g'$$

*These fall straight out of the limit laws in Section 1 (the limit of a sum is the sum of limits).*

**Power rule**

$$\frac{d}{dx}\big[x^{n}\big]=n\,x^{\,n-1}$$

**Demonstration — power rule (via the binomial theorem)**

1. Definition:

   $$f'(x)=\lim_{h\to0}\frac{(x+h)^n-x^n}{h}.$$
2. Binomial expansion:

   $$(x+h)^n = x^n + n x^{n-1}h + \tfrac{n(n-1)}{2}x^{n-2}h^2+\cdots+h^n.$$
3. Subtract $x^n$; every surviving term has at least one factor of $h$:

   $$(x+h)^n-x^n = n x^{n-1}h + \tfrac{n(n-1)}{2}x^{n-2}h^2+\cdots$$
4. Divide by $h$:

   $$n x^{n-1} + \tfrac{n(n-1)}{2}x^{n-2}h + \cdots$$
5. Let $h\to0$: every term still carrying an $h$ vanishes, leaving

   $$f'(x)=n x^{n-1}.$$

**★ The famous, everyday derivatives you'll reach for most**

$$\frac{d}{dx}\,e^{x}=e^{x} \qquad \frac{d}{dx}\sqrt{x}=\frac{1}{2\sqrt{x}} \qquad \frac{d}{dx}\,\frac{1}{x}=-\frac{1}{x^{2}}$$

*$e^x$ is the single most famous derivative in mathematics — the only function (up to a constant multiple) that is its own derivative, which is why it governs growth, decay, and compound interest. The other two are the everyday special cases of the power rule that appear constantly.*

**Demonstration — the two everyday cases are just the power rule**

1. Square root: write $\sqrt{x}=x^{1/2}$ and apply $nx^{n-1}$:

   $$\frac{d}{dx}x^{1/2}=\tfrac{1}{2}x^{-1/2}=\frac{1}{2\sqrt{x}}.$$
2. Reciprocal: write $\dfrac{1}{x}=x^{-1}$ and apply the same rule:

   $$\frac{d}{dx}x^{-1}=-1\cdot x^{-2}=-\frac{1}{x^{2}}.$$

*The power rule works for any exponent — fractional or negative — not just whole numbers.*

**Product rule**

$$(fg)' = f'g + fg'$$

*"Derivative of first times second, plus first times derivative of second." Not $f'g'$.*

**Demonstration — product rule (the add-and-subtract trick)**

1. Definition:

   $$(fg)'=\lim_{h\to0}\frac{f(x+h)g(x+h)-f(x)g(x)}{h}.$$
2. Add and subtract $f(x+h)g(x)$ in the numerator (it cancels to zero, so nothing changes):

   $$f(x+h)g(x+h)-f(x+h)g(x)+f(x+h)g(x)-f(x)g(x).$$
3. Group and factor:

   $$f(x+h)\big[g(x+h)-g(x)\big]+g(x)\big[f(x+h)-f(x)\big].$$
4. Divide by $h$ and split the limit:

   $$\lim f(x+h)\frac{g(x+h)-g(x)}{h}+\lim g(x)\frac{f(x+h)-f(x)}{h}.$$
5. As $h\to0$: $f(x+h)\to f(x)$, and the two quotients become $g'$ and $f'$:

   $$(fg)'=f g' + g f'.$$

**Quotient rule**

$$\left(\frac{f}{g}\right)'=\frac{f'g-fg'}{g^{2}}$$

*"Low d-high minus high d-low, over low squared."*

**Demonstration — quotient rule (straight from the product rule)**

1. Let $Q=\dfrac{f}{g}$, so that $f = Q\,g$.
2. Differentiate both sides with the product rule:

   $$f' = Q'g + Q g'.$$
3. Solve for $Q'$:

   $$Q' = \frac{f'-Qg'}{g}.$$
4. Replace $Q$ with $f/g$ and simplify over a common denominator:

   $$Q'=\frac{f'-\frac{f}{g}g'}{g}=\frac{f'g-fg'}{g^2}.$$

*Notice the quotient rule isn't separate magic — it's the product rule, rearranged.*

**Chain rule (functions inside functions)**

$$\frac{d}{dx}\,f\big(g(x)\big)=f'\big(g(x)\big)\cdot g'(x) \qquad\Big(\tfrac{dy}{dx}=\tfrac{dy}{du}\cdot\tfrac{du}{dx}\Big)$$

**Demonstration — chain rule (the intuition that makes it obvious)**

1. Write the change in $y$ caused by a change in $x$ as a product of ratios (multiply top and bottom by $\Delta u$):

   $$\frac{\Delta y}{\Delta x}=\frac{\Delta y}{\Delta u}\cdot\frac{\Delta u}{\Delta x}.$$
2. As $\Delta x\to0$, the inside change $\Delta u\to0$ too (since $g$ is continuous).
3. Each ratio becomes a derivative in the limit:

   $$\frac{dy}{dx}=\frac{dy}{du}\cdot\frac{du}{dx}=f'(g(x))\,g'(x).$$

*Differentiate the outer layer, keep the inside intact, multiply by the inside's derivative.*

> **Forward link (remember these two)**
>
> Read backwards, the **product rule becomes integration by parts** and the **chain rule becomes u-substitution** — the two main integration techniques in Section 9. We'll derive both from these.

<a id="s4"></a>
## Derivatives of every standard function

*With the rules above plus a few key limits, each of these can be demonstrated.*

**Trigonometric**

$$(\sin x)'=\cos x,\quad (\cos x)'=-\sin x,\quad (\tan x)'=\sec^2 x$$

$$(\cot x)'=-\csc^2 x,\quad (\sec x)'=\sec x\tan x,\quad (\csc x)'=-\csc x\cot x$$

**Demonstration — $(\sin x)'=\cos x$**

1. Definition:

   $$(\sin x)'=\lim_{h\to0}\frac{\sin(x+h)-\sin x}{h}.$$
2. Use the addition formula $\sin(x+h)=\sin x\cos h+\cos x\sin h$:

   $$=\lim_{h\to0}\frac{\sin x\cos h+\cos x\sin h-\sin x}{h}.$$
3. Group the $\sin x$ terms and split:

   $$=\sin x\lim_{h\to0}\frac{\cos h-1}{h}+\cos x\lim_{h\to0}\frac{\sin h}{h}.$$
4. Insert the special limits from Section 1 $\big(\frac{\cos h-1}{h}\to0,\ \frac{\sin h}{h}\to1\big)$:

   $$=\sin x\cdot 0 + \cos x\cdot 1 = \cos x.$$

*$\tan,\sec,\csc,\cot$ then follow by the quotient rule on $\sin/\cos$.*

**Exponential & logarithmic**

$$(e^{x})'=e^{x},\quad (a^{x})'=a^{x}\ln a,\quad (\ln x)'=\frac{1}{x},\quad (\log_a x)'=\frac{1}{x\ln a}$$

**Demonstration — $(e^x)'=e^x$**

1. Definition:

   $$(e^x)'=\lim_{h\to0}\frac{e^{x+h}-e^{x}}{h}.$$
2. Factor $e^{x}$ out (it doesn't depend on $h$):

   $$=e^{x}\lim_{h\to0}\frac{e^{h}-1}{h}.$$
3. That remaining limit equals $1$ (a special limit from Section 1 — in fact it's the property that defines $e$):

   $$=e^{x}\cdot 1 = e^{x}.$$

*$e^x$ is the unique function that is its own derivative.*

**Demonstration — $(\ln x)'=\tfrac1x$ (via inverse functions)**

1. Let $y=\ln x$. By definition this means

   $$e^{y}=x.$$
2. Differentiate both sides with respect to $x$, using the chain rule on the left:

   $$e^{y}\cdot\frac{dy}{dx}=1.$$
3. Solve for $dy/dx$ and recall $e^{y}=x$:

   $$\frac{dy}{dx}=\frac{1}{e^{y}}=\frac{1}{x}.$$

**Inverse trigonometric**

$$(\arcsin x)'=\frac{1}{\sqrt{1-x^2}},\quad (\arccos x)'=-\frac{1}{\sqrt{1-x^2}},\quad (\arctan x)'=\frac{1}{1+x^2}$$

**Demonstration — $(\arctan x)'=\tfrac{1}{1+x^2}$**

1. Let $y=\arctan x$, so

   $$\tan y = x.$$
2. Differentiate both sides:

   $$\sec^2 y\cdot\frac{dy}{dx}=1 \;\Rightarrow\; \frac{dy}{dx}=\frac{1}{\sec^2 y}.$$
3. Use the identity $\sec^2 y = 1+\tan^2 y$ and $\tan y = x$:

   $$\frac{dy}{dx}=\frac{1}{1+\tan^2 y}=\frac{1}{1+x^2}.$$

**Hyperbolic functions**

$$\sinh x=\frac{e^x-e^{-x}}{2},\quad \cosh x=\frac{e^x+e^{-x}}{2}$$

$$(\sinh x)'=\cosh x,\quad (\cosh x)'=\sinh x,\quad (\tanh x)'=\operatorname{sech}^2 x$$

*Defined from $e^x$; their derivatives follow in one line from $(e^x)'=e^x$. Note $(\cosh)'=+\sinh$, unlike the trig minus sign.*

> **A quiet symmetry**
>
> Differentiating $\sin$ four times returns to $\sin$. That cycle is exactly why sine and cosine describe everything that oscillates — and it reappears in their Taylor series in Section 11.

<a id="s5"></a>
## Implicit, logarithmic & higher-order derivatives

*For when y is tangled up, the exponents are messy, or you differentiate more than once.*

**Implicit differentiation**

$$\frac{d}{dx}[y]=\frac{dy}{dx},\qquad \frac{d}{dx}\big[y^{2}\big]=2y\frac{dy}{dx}$$

**Demonstration — slope on the circle $x^2+y^2=25$**

1. Differentiate both sides, treating $y$ as a function of $x$ (so $y^2$ needs the chain rule):

   $$2x+2y\frac{dy}{dx}=0.$$
2. Solve for the slope:

   $$\frac{dy}{dx}=-\frac{x}{y}.$$

*Every $y$-term picks up a $dy/dx$ — that's the chain rule from Section 3 doing the work.*

**Logarithmic differentiation**

$$y=f(x)^{g(x)} \Rightarrow \ln y=g\ln f \Rightarrow \frac{y'}{y}=\big(g\ln f\big)'$$

*Take $\ln$ first to turn an awkward power into a product. Essential for things like $x^{x}$.*

**Higher-order derivatives**

$$f''(x)=\frac{d}{dx}f'(x),\qquad f^{(n)}(x)=\frac{d^{\,n}y}{dx^{\,n}}$$

*If $s(t)$ is position: $s'$ is velocity, $s''$ is acceleration. The second derivative also controls concavity (Section 6).*

<a id="s6"></a>
## Putting derivatives to work

*Tangent lines, curve shapes, optimization, and impossible-looking limits.*

**Tangent line at $x=a$**

$$y-f(a)=f'(a)(x-a)$$

### Reading a curve from its derivatives

- $f'>0$: increasing   $f'<0$: decreasing
- **Critical points**: where $f'(x)=0$ or undefined — candidates for max/min
- $f''>0$: concave up (cup)   $f''<0$: concave down (cap)
- **Inflection point**: where $f''$ changes sign

**First & second derivative tests**

$$f'(c)=0:\quad f''(c)>0 \Rightarrow \text{local min},\qquad f''(c)<0 \Rightarrow \text{local max}$$

**Mean Value Theorem (and Rolle's case)**

$$\exists\,c\in(a,b):\ f'(c)=\frac{f(b)-f(a)}{b-a}$$

*Somewhere the instantaneous slope equals the average slope. Rolle's theorem is the case $f(a)=f(b)$, giving $f'(c)=0$.*

**L'Hôpital's rule (for $0/0$ or $\infty/\infty$)**

$$\lim_{x\to a}\frac{f(x)}{g(x)}=\lim_{x\to a}\frac{f'(x)}{g'(x)}$$

**Demonstration — why it works (the local-linear picture)**

1. Near $x=a$ with $f(a)=g(a)=0$, replace each function by its tangent line (Section 6):

   $$f(x)\approx f'(a)(x-a),\qquad g(x)\approx g'(a)(x-a).$$
2. Form the ratio; the common factor $(x-a)$ cancels:

   $$\frac{f(x)}{g(x)}\approx\frac{f'(a)(x-a)}{g'(a)(x-a)}=\frac{f'(a)}{g'(a)}.$$

*An indeterminate ratio is governed by the ratio of slopes. A neat loop back to Section 1.*

**Linear approximation & differentials**

$$f(x)\approx f(a)+f'(a)(x-a),\qquad dy=f'(x)\,dx$$

*Near a point, every smooth curve looks like its tangent line. Extended to infinitely many derivatives, this becomes the Taylor series in Section 11.*

<a id="s7"></a>
## The antiderivative & the Fundamental Theorem

*The hinge of the entire subject: derivative and integral are revealed to be opposites.*

**Indefinite integral (antiderivative)**

$$\int f(x)\,dx=F(x)+C \quad\text{where}\quad F'(x)=f(x)$$

*"What function has THIS as its derivative?" The $+C$ appears because constants vanish when differentiated.*

**Definite integral as a limit of Riemann sums**

$$\int_{a}^{b} f(x)\,dx=\lim_{n\to\infty}\sum_{i=1}^{n} f(x_i^{*})\,\Delta x,\qquad \Delta x=\frac{b-a}{n}$$

*Slice the area into n thin rectangles, add them, let the slices vanish. The integral IS an infinite sum — the same "push to a limit" that built the derivative.*

### The Fundamental Theorem of Calculus

**Part 1 — differentiation undoes integration**

$$\frac{d}{dx}\int_{a}^{x} f(t)\,dt=f(x)$$

**Part 2 — integrals are evaluated by antiderivatives**

$$\int_{a}^{b} f(x)\,dx=F(b)-F(a),\quad F'=f$$

**Demonstration — why Part 1 is true (the thin-strip argument)**

1. Define the running-area function

   $$A(x)=\int_a^x f(t)\,dt.$$
2. Increasing $x$ by a tiny $h$ adds a thin strip of width $h$ and height $\approx f(x)$:

   $$A(x+h)-A(x)\approx f(x)\cdot h.$$
3. Divide by $h$:

   $$\frac{A(x+h)-A(x)}{h}\approx f(x).$$
4. Let $h\to0$. The left side is exactly the definition of $A'(x)$:

   $$A'(x)=f(x).$$

*So the area function's derivative is the original function — accumulation and rate are inverse operations. Part 2 follows because any two antiderivatives differ by a constant.*

> **The payoff**
>
> To find an area (an infinite sum), you don't add anything — you find an antiderivative and subtract two values. This is why the entire integral table in Section 8 is just the derivative tables of Sections 3–4 read backwards.

<a id="s8"></a>
## The basic integral table

*Each line is a derivative rule reversed — verify any of them by differentiating the right-hand side.*

**Power rule for integrals**

$$\int x^{n}\,dx=\frac{x^{\,n+1}}{n+1}+C \quad(n\neq-1)$$

*Check: differentiate $\frac{x^{n+1}}{n+1}$ and the power rule gives back $x^n$.*

**The $n=-1$ exception**

$$\int \frac{1}{x}\,dx=\ln|x|+C$$

| Integral | Result | Reverse of… |
| --- | --- | --- |
| $\int e^{x}\,dx$ | $e^{x}+C$ | $(e^x)'=e^x$ |
| $\int a^{x}\,dx$ | $\dfrac{a^{x}}{\ln a}+C$ | $(a^x)'=a^x\ln a$ |
| $\int \cos x\,dx$ | $\sin x+C$ | $(\sin x)'=\cos x$ |
| $\int \sin x\,dx$ | $-\cos x+C$ | $(\cos x)'=-\sin x$ |
| $\int \sec^{2}x\,dx$ | $\tan x+C$ | $(\tan x)'=\sec^2 x$ |
| $\int \sec x\tan x\,dx$ | $\sec x+C$ | $(\sec x)'=\sec x\tan x$ |
| $\int \dfrac{1}{1+x^{2}}\,dx$ | $\arctan x+C$ | $(\arctan x)'=\frac{1}{1+x^2}$ |
| $\int \dfrac{1}{\sqrt{1-x^{2}}}\,dx$ | $\arcsin x+C$ | $(\arcsin x)'=\frac{1}{\sqrt{1-x^2}}$ |
| $\int \sinh x\,dx$ | $\cosh x+C$ | $(\cosh x)'=\sinh x$ |

### Three integrals that need a small trick

| Integral | Result | How |
| --- | --- | --- |
| $\int \tan x\,dx$ | $\ln\vert \sec x\vert +C$ | u-sub with $u=\cos x$ |
| $\int \ln x\,dx$ | $x\ln x-x+C$ | by parts (see §9) |
| $\int \sec x\,dx$ | $\ln\vert \sec x+\tan x\vert +C$ | multiply by a clever 1 |

> How to use this section
>
> Don't memorize this table separately. If you know the derivative tables in Sections 3–4, you already know this — just flip the arrow. That is the Fundamental Theorem in action.

<a id="s9"></a>
## Integration techniques — each one proven

*When an integral doesn't match the table, reshape it until it does. Two of these are differentiation rules in reverse, and we derive them that way.*

**u-substitution**

$$\int f\big(g(x)\big)g'(x)\,dx=\int f(u)\,du,\qquad u=g(x)$$

**Demonstration — u-sub is the chain rule, reversed**

1. Let $F$ be an antiderivative of $f$, so $F'=f$. By the chain rule:

   $$\frac{d}{dx}F\big(g(x)\big)=F'\big(g(x)\big)g'(x)=f\big(g(x)\big)g'(x).$$
2. Integrate both sides (integration undoes the derivative):

   $$\int f\big(g(x)\big)g'(x)\,dx=F\big(g(x)\big)+C.$$
3. That right side is exactly $\int f(u)\,du$ with $u=g(x)$.

**Integration by parts**

$$\int u\,dv=uv-\int v\,du$$

**Demonstration — by parts is the product rule, reversed**

1. Start from the product rule:

   $$(uv)'=u'v+uv'.$$
2. Integrate both sides over $x$:

   $$uv=\int u'v\,dx+\int uv'\,dx.$$
3. Solve for one of the integrals: i.e. $\displaystyle\int u\,dv=uv-\int v\,du.$

   $$\int uv'\,dx=uv-\int u'v\,dx,$$

*Use it on products like $\int x e^{x}\,dx$ or $\int \ln x\,dx$ (take $u=\ln x,\ dv=dx$).*

**Trigonometric substitution**

$$\sqrt{a^2-x^2}\!: x=a\sin\theta,\quad \sqrt{a^2+x^2}\!: x=a\tan\theta,\quad \sqrt{x^2-a^2}\!: x=a\sec\theta$$

*Trade an awkward square root for a clean trig identity.*

**Partial fractions**

$$\frac{P(x)}{(x-r_1)(x-r_2)}=\frac{A}{x-r_1}+\frac{B}{x-r_2}$$

*Break a rational function into simple pieces, each integrating to a log or arctangent.*

**Improper integrals**

$$\int_{a}^{\infty} f(x)\,dx=\lim_{t\to\infty}\int_{a}^{t} f(x)\,dx$$

*Infinite bounds (or vertical asymptotes) are handled as a limit; the integral "converges" if that limit is finite.*

### Properties of definite integrals

$$\int_a^b f=-\int_b^a f,\qquad \int_a^a f=0,\qquad \int_a^b f=\int_a^c f+\int_c^b f$$

> **The mirror, made explicit**
>
> Chain rule ⟷ u-substitution. Product rule ⟷ integration by parts. Differentiation has clean rules that always work; integration is the reverse search, so it needs clever moves. Same relationships, harder direction.

<a id="s10"></a>
## Putting integrals to work

*Anything that accumulates — area, volume, length, average — is an integral.*

**Area between two curves**

$$A=\int_a^b\big[f(x)-g(x)\big]\,dx$$

**Volume of revolution — disk method**

$$V=\pi\int_a^b\big[f(x)\big]^2\,dx$$

**Volume of revolution — shell method**

$$V=2\pi\int_a^b x\,f(x)\,dx$$

**Arc length**

$$L=\int_a^b\sqrt{1+\big[f'(x)\big]^2}\;dx$$

**Average value of a function**

$$\bar f=\frac{1}{b-a}\int_a^b f(x)\,dx$$

**Demonstration — where the arc-length formula comes from**

1. Approximate the curve by tiny straight segments. Each has horizontal run $dx$ and vertical rise $dy$.
2. By the Pythagorean theorem, the segment length is

   $$ds=\sqrt{dx^2+dy^2}.$$
3. Factor $dx$ out of the root and use $\frac{dy}{dx}=f'(x)$:

   $$ds=\sqrt{1+\big(\tfrac{dy}{dx}\big)^2}\,dx=\sqrt{1+[f'(x)]^2}\,dx.$$
4. Integrate (add up) all the tiny lengths from $a$ to $b$:

   $$L=\int_a^b\sqrt{1+[f'(x)]^2}\,dx.$$

*Every formula here uses the same recipe: write one tiny slice, then integrate to sum infinitely many — the Riemann idea from Section 7.*

<a id="s11"></a>
## Sequences & series

*Adding infinitely many terms — when the total is finite, we can rebuild functions from their derivatives.*

**Geometric series**

$$\sum_{n=0}^{\infty} a r^{n}=\frac{a}{1-r}\quad(|r|<1)$$

**Demonstration — the geometric sum formula**

1. Write the partial sum:

   $$S_n=a+ar+ar^2+\cdots+ar^{n-1}.$$
2. Multiply by $r$:

   $$rS_n=ar+ar^2+\cdots+ar^{n}.$$
3. Subtract — almost everything cancels:

   $$S_n-rS_n=a-ar^{n}\;\Rightarrow\; S_n=\frac{a(1-r^{n})}{1-r}.$$
4. If $|r|<1$, then $r^{n}\to0$ as $n\to\infty$:

   $$S=\frac{a}{1-r}.$$

**p-series**

$$\sum_{n=1}^{\infty}\frac{1}{n^{p}}\ \text{converges} \iff p>1$$

### The full toolkit of convergence tests

| Test | Statement |
| --- | --- |
| nth-term (divergence) | If $\lim a_n\neq 0$, the series diverges |
| Ratio test | $\lim\left\vert \frac{a_{n+1}}{a_n}\right\vert =L$; converges if $L<1$, diverges if $L>1$ |
| Root test | $\lim \vert a_n\vert ^{1/n}=L$; converges if $L<1$ |
| Comparison | Bound $a_n$ above/below by a known convergent/divergent series |
| Limit comparison | If $\lim \frac{a_n}{b_n}$ is finite & positive, both behave the same way |
| Integral test | $\sum a_n$ and $\int_1^\infty f\,dx$ converge or diverge together |
| Alternating series | $\sum(-1)^n b_n$ converges if $b_n$ decreases to $0$ |

**Taylor series — a function rebuilt from its derivatives**

$$f(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^{n}$$

*Maclaurin series is the case $a=0$. It is linear approximation (Section 6) continued to infinitely many derivatives.*

**Demonstration — why the coefficients are $f^{(n)}(a)/n!$**

1. Suppose $f(x)=c_0+c_1(x-a)+c_2(x-a)^2+\cdots$. Set $x=a$: every term but the first dies, so $c_0=f(a)$.
2. Differentiate once, then set $x=a$: only the linear term survives, giving $c_1=f'(a)$.
3. Differentiate $n$ times: the $(x-a)^n$ term becomes the constant $n!\,c_n$ and all others vanish at $x=a$:

   $$f^{(n)}(a)=n!\,c_n \;\Rightarrow\; c_n=\frac{f^{(n)}(a)}{n!}.$$

### The famous expansions

$$e^{x}=\sum_{n=0}^{\infty}\frac{x^{n}}{n!}=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots$$

$$\sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots,\qquad \cos x=1-\frac{x^2}{2!}+\frac{x^4}{4!}-\cdots$$

$$\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}-\cdots,\qquad \frac{1}{1-x}=\sum_{n=0}^{\infty}x^n\ (|x|<1)$$

> **A glimpse of the unity**
>
> Put $x=i\theta$ into the $e^x$ series and regroup using the $\sin$ and $\cos$ series: you land on Euler's formula $e^{i\theta}=\cos\theta+i\sin\theta$. The series built from derivatives quietly tie exponentials to oscillation.

<a id="s12"></a>
## A peek at multivariable calculus

*The same two ideas — slope and accumulation — in more than one dimension.*

**Partial derivative**

$$\frac{\partial f}{\partial x}=\lim_{h\to0}\frac{f(x+h,\,y)-f(x,\,y)}{h}$$

*Differentiate with respect to one variable while holding the others constant — the Section 2 definition, with $y$ frozen.*

**Gradient (vector of all partials)**

$$\nabla f=\left\langle \frac{\partial f}{\partial x},\ \frac{\partial f}{\partial y},\ \frac{\partial f}{\partial z}\right\rangle$$

*Points in the direction of steepest increase — the multivariable cousin of the derivative.*

**Multivariable chain rule**

$$\frac{df}{dt}=\frac{\partial f}{\partial x}\frac{dx}{dt}+\frac{\partial f}{\partial y}\frac{dy}{dt}$$

**Double integral (accumulation over a region)**

$$\iint_{R} f(x,y)\,dA=\int_{c}^{d}\!\int_{a}^{b} f(x,y)\,dx\,dy$$

*Volume under a surface — the Riemann idea again, stacking tiny boxes instead of rectangles.*

> **Where it all leads**
>
> From here the path runs to the great integral theorems (Green's, Stokes', Divergence) — each a higher-dimensional Fundamental Theorem, saying again that behavior on a boundary is governed by behavior inside.

---

*Read once for the shape, then return to any box as a reference. The habit that makes calculus click: whenever you meet a new formula, ask which earlier one it is secretly a version of — and try to reproduce its demonstration from memory. Almost everything here is built from limits, the product rule, and the chain rule.*
