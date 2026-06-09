**English** · [中文](connected-map.zh.md)

# Calculus, *connected.*

Every formula here grows out of one of two ideas: **the limit**, and what happens when you let something get infinitely small. Read it top to bottom and each piece will lean on the one before it.

This version assumes **no prior mathematics beyond ordinary arithmetic and basic algebra** (adding, multiplying, fractions, and solving simple equations). Every symbol is defined in words the first time it appears, every formula is derived step by step with a reason given for each step, and every idea is followed by a worked example using real numbers. Nothing is left "to the reader."

[← Back to all guides](../README.md)

<a id="s0"></a>
## The big picture before any symbols

*If you hold one map in your head, hold this one.*

Before any formula, let us agree on what a few everyday words mean, because we will use them constantly.

- A **function** is a rule that takes a number in and gives exactly one number out. We write it as $f(x)$, read "f of x." Here $x$ is the **input** (the number we feed in) and $f(x)$ is the **output** (the number that comes out). Example: if the rule is "square the input," then $f(x)=x^2$, and feeding in $3$ gives $f(3)=9$.
- A **variable** is a letter standing for a number that can change, like $x$.
- A **constant** is a fixed number that does not change, often written $c$.
- A **slope** measures steepness: how much the output goes up for each step the input takes to the right. On a straight line through two points, slope $=\dfrac{\text{change in output}}{\text{change in input}}$.
- An **area** is the amount of flat space inside a shape, measured in squares.

All of calculus is two questions about change, plus a stunning discovery that they are opposites.

- **The derivative** asks: *how fast is this changing right now?* (a slope, a speed, a rate)
- **The integral** asks: *how much has accumulated in total?* (an area, a distance, a sum)

Both are built by taking something you understand for ordinary numbers (a slope between two points, the area of a rectangle) and pushing it to a **limit** — letting a gap shrink toward zero. So we must understand limits first.

### Why "pushing to a limit" is the key trick

Suppose you want the *exact* speed of a car at one precise instant. Speed is distance divided by time, but at a single instant no time passes, so you would be dividing by zero — meaningless. The escape is to measure the average speed over a tiny stretch of time, then over an even tinier stretch, and watch what number these averages approach. That approached number is the **limit**, and it gives the instantaneous speed without ever literally dividing by zero. This single move — approach, don't arrive — appears everywhere below.

### The whole course on one line

> Limits → Derivatives → Integrals ↔ (linked by the FTC) → Series → Multivariable

Read it as: limits make derivatives possible; derivatives and integrals turn out to be opposites (joined by the **Fundamental Theorem of Calculus**, abbreviated **FTC**); series let us rebuild functions from their derivatives; and multivariable calculus repeats the whole story in more than one dimension.

> **The connection to watch for**
>
> The single most important relationship in the subject is the **Fundamental Theorem of Calculus** (Section 7): differentiation and integration undo each other. Every integration formula in Sections 8–9 is just a differentiation formula from Sections 3–4 read backwards.

#### A first numeric taste

Take $f(x)=x^2$ and ask for its slope near $x=3$. Pick a small step $h=0.1$. The two points are $(3, 9)$ and $(3.1, 3.1^2)=(3.1, 9.61)$. The slope between them is

$$\frac{9.61-9}{3.1-3}=\frac{0.61}{0.1}=6.1$$

Now shrink the step to $h=0.01$: the points are $(3,9)$ and $(3.01, 9.0601)$, giving slope $\dfrac{0.0601}{0.01}=6.01$. The averages are marching toward $6$. Keep that number $6$ in mind; by the end of Section 2 we will see it is exactly the derivative of $x^2$ at $x=3$.

<a id="s1"></a>
## Limits & continuity

The foundation. A limit answers: where is the function *heading* as the input approaches a value — even if it never arrives?

**What a limit means in plain words.** Imagine walking toward a doorway. The limit is the doorway you are heading for, regardless of whether you ever actually step through it. For a function, we slide the input $x$ closer and closer to some target value $a$ and watch where the output $f(x)$ is heading.

**Intuitive limit**

$$\lim_{x \to a} f(x) = L$$

*Reading the symbols:* "$\lim$" is short for **limit**; "$x \to a$" is read "$x$ approaches $a$"; $L$ is the value being approached. The whole line says: as $x$ gets arbitrarily close to $a$, $f(x)$ gets arbitrarily close to $L$. Note $x$ never has to equal $a$ — we only care about the trend nearby.

**Worked example of an intuitive limit.** Let $f(x)=\dfrac{x^2-1}{x-1}$. At $x=1$ this is $\frac{0}{0}$, undefined. But for any $x\neq 1$ we can simplify, because $x^2-1=(x-1)(x+1)$ (a standard factoring identity, "difference of squares"):

$$\frac{x^2-1}{x-1}=\frac{(x-1)(x+1)}{x-1}=x+1\quad(x\neq 1)$$

So as $x\to 1$, $f(x)\to 1+1=2$. The function has a hole at $x=1$, yet it is heading for $2$. That heading value is the limit.

**Formal (ε–δ) definition**

$$\forall\, \varepsilon>0,\; \exists\, \delta>0 \;:\; 0<|x-a|<\delta \implies |f(x)-L|<\varepsilon$$

*Reading the symbols:* "$\forall$" means "for every"; "$\exists$" means "there exists"; $\varepsilon$ (epsilon) and $\delta$ (delta) are small positive numbers; "$|x-a|$" is the **absolute value** of $x-a$, meaning its distance from zero ignoring sign, so $|x-a|$ is the distance between $x$ and $a$; "$\implies$" means "leads to." In words: *name any tolerance $\varepsilon$ around $L$; I can find a window $\delta$ around $a$ so that whenever $x$ is within $\delta$ of $a$ (but not equal to $a$), $f(x)$ lands within $\varepsilon$ of $L$.* This is the rigorous engine behind everything else: it pins down "arbitrarily close" with no hand-waving.

**Worked ε–δ verification.** Show $\lim_{x\to 3}(2x+1)=7$.

1. Start from what we must control: $|f(x)-L|=|(2x+1)-7|=|2x-6|$. *(Reason: substitute $f$ and $L$.)*
2. Factor out the $2$: $|2x-6|=2\,|x-3|$. *(Reason: $|2t|=2|t|$ for the absolute value of a doubled quantity.)*
3. We want $2|x-3|<\varepsilon$, i.e. $|x-3|<\varepsilon/2$. *(Reason: divide both sides of the inequality by the positive number $2$.)*
4. So choose $\delta=\varepsilon/2$. Then $0<|x-3|<\delta$ gives $|f(x)-7|=2|x-3|<2\delta=\varepsilon$. *(Reason: substitute the chosen $\delta$.)*

A specific $\delta$ that works for every $\varepsilon$ proves the limit exactly. For instance with $\varepsilon=0.1$ we use $\delta=0.05$.

### Limit laws (how limits combine)

These laws let us compute big limits from small ones without returning to the ε–δ machinery each time. Suppose $\lim_{x\to a} f = L$ and $\lim_{x\to a} g = M$ (so both pieces individually head somewhere). Then limits pass cleanly through arithmetic:

$$\lim (f \pm g) = L \pm M \qquad \lim (fg)=LM \qquad \lim \frac{f}{g}=\frac{L}{M}\;(M\neq 0)$$

$$\lim\, c\,f = cL \qquad \lim \big(f(x)\big)^n = L^{\,n}$$

*In words:* the limit of a sum is the sum of the limits; likewise for differences, products, and quotients (as long as the bottom limit $M$ is not zero, since dividing by zero is undefined); a constant multiplier $c$ slides out front; and a power of a function has the power of the limit.

**Worked example using the laws.** Compute $\lim_{x\to 2}(3x^2-5)$.

1. $\lim_{x\to 2} x = 2$. *(Reason: the function $x$ heads to the value $2$.)*
2. $\lim_{x\to 2} x^2 = 2^2 = 4$. *(Reason: power law with $n=2$.)*
3. $\lim_{x\to 2} 3x^2 = 3\cdot 4 = 12$. *(Reason: constant-multiple law with $c=3$.)*
4. $\lim_{x\to 2} 5 = 5$. *(Reason: a constant heads to itself.)*
5. $\lim_{x\to 2}(3x^2-5)=12-5=7$. *(Reason: difference law.)*

**Squeeze (sandwich) theorem**

$$g(x)\le f(x)\le h(x)\ \text{ and }\ \lim_{x\to a}g=\lim_{x\to a}h=L \implies \lim_{x\to a}f=L$$

*In words:* if $f$ is trapped between a lower function $g$ and an upper function $h$ ("$\le$" means "less than or equal to"), and both the trap walls head to the same value $L$, then $f$ has nowhere to go but $L$ too. Intuition: if two friends squeezing you on both sides are both walking toward a door, you must reach that door as well.

**Worked squeeze example.** Find $\lim_{x\to 0} x^2\sin(1/x)$. The factor $\sin(1/x)$ wobbles forever between $-1$ and $1$, so it has no limit on its own. But:

1. $-1\le \sin(1/x)\le 1$ always. *(Reason: sine is always between $-1$ and $1$.)*
2. Multiply through by $x^2$, which is $\ge 0$, so the inequalities keep their direction: $-x^2\le x^2\sin(1/x)\le x^2$. *(Reason: multiplying an inequality by a non-negative number preserves it.)*
3. $\lim_{x\to 0}(-x^2)=0$ and $\lim_{x\to 0}x^2=0$. *(Reason: power and constant-multiple laws.)*
4. Both walls go to $0$, so by the squeeze theorem the middle goes to $0$. *(Reason: squeeze theorem.)*

### Special limits worth memorizing

$$\lim_{x\to 0}\frac{\sin x}{x}=1 \qquad \lim_{x\to 0}\frac{1-\cos x}{x}=0 \qquad \lim_{x\to\infty}\Big(1+\tfrac{1}{x}\Big)^{x}=e$$

*The first one is the seed of the derivative of sine. The last one is where the number $e\approx 2.71828$ is born.* Here "$x\to\infty$" means "$x$ grows without bound." Numerically, the third limit: at $x=10$ we get $(1.1)^{10}\approx 2.594$; at $x=1000$ we get $(1.001)^{1000}\approx 2.717$ — closing in on $e$.

**Continuity at a point**

$$f \text{ is continuous at } a \iff \lim_{x\to a} f(x) = f(a)$$

*Reading "$\iff$":* "if and only if," meaning the two sides are completely equivalent. **Continuous** means you can draw the graph through that point without lifting your pen. *Three things must agree:* the limit exists, the value $f(a)$ exists, and they match. No holes, jumps, or breaks.

**Worked continuity check.** Is $f(x)=\dfrac{x^2-1}{x-1}$ continuous at $x=1$? Above we found the limit is $2$, but $f(1)$ is undefined ($\frac{0}{0}$). Since the value does not exist, the equality fails — so $f$ is **not** continuous at $1$; it has a removable hole there.

> **Why this matters next**
>
> A function must be continuous to be differentiable. And the derivative itself is *defined* as a limit — so Section 2 is really just one careful application of everything above.

<a id="s2"></a>
## What a derivative *is*

*Take the slope between two points, then slide them together. That limit is the derivative.*

**The idea in plain words.** The **derivative** of a function at a point is the exact slope of the curve right there — equivalently, the instantaneous rate at which the output changes as the input nudges forward. We get it by computing the slope between two nearby points and then letting their gap shrink to nothing, using the limit from Section 1.

**The definition (limit of a difference quotient)**

$$f'(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}$$

*Reading the symbols:* $f'(x)$ (read "f prime of x") is the derivative; $h$ is a small step in the input; $f(x+h)$ is the output a step later; $f(x+h)-f(x)$ is the change in output ("rise"); dividing by $h$ (the "run") gives slope. The quantity $\frac{f(x+h)-f(x)}{h}$ is the slope of a line through two nearby points — the **secant** line. Letting $h\to 0$ tilts the secant into the **tangent** line, the line just grazing the curve at one point.

**Equivalent form (at a specific point a)**

$$f'(a)=\lim_{x\to a}\frac{f(x)-f(a)}{x-a}$$

This says the same thing with the second point named directly as $x$ approaching $a$, instead of stepping a distance $h$. Setting $x=a+h$ turns one form into the other.

### What it means

- **Geometrically:** the slope of the tangent line to the curve at $x$.
- **Physically:** the instantaneous rate of change. If $s(t)$ is position at time $t$, then $s'(t)$ is velocity (how fast position changes).

### The many ways to write it

`$f'(x)$ — Lagrange` · `$\dfrac{dy}{dx}$ — Leibniz` · `$\dot{y}$ — Newton` · `$D_x f$ — operator`

These are four notations for the **same** object. Leibniz's $\frac{dy}{dx}$ literally suggests "tiny change in $y$ divided by tiny change in $x$," matching the slope picture; here $y$ means the output, often written $y=f(x)$.

> **Demonstration — derive the power rule from scratch**
>
> Let $f(x)=x^2$. Plug into the definition:
>
> $$ f'(x)=\lim_{h\to0}\frac{(x+h)^2-x^2}{h}=\lim_{h\to0}\frac{x^2+2xh+h^2-x^2}{h} $$
>
> $$ =\lim_{h\to0}\frac{2xh+h^2}{h}=\lim_{h\to0}(2x+h)=2x. $$
>
> So $\frac{d}{dx}x^2 = 2x$ — exactly what the power rule $nx^{n-1}$ predicts. The rules in Section 3 are shortcuts so you never have to do this by hand again.

**Step-by-step reasons for that derivation.**

1. Substitute $f(x)=x^2$ into the definition: numerator becomes $(x+h)^2-x^2$. *(Reason: definition of the derivative.)*
2. Expand $(x+h)^2=x^2+2xh+h^2$. *(Reason: the algebra identity $(a+b)^2=a^2+2ab+b^2$.)*
3. The $x^2$ and $-x^2$ cancel, leaving $2xh+h^2$. *(Reason: $x^2-x^2=0$.)*
4. Factor out $h$: $2xh+h^2=h(2x+h)$, then divide by $h$ (allowed because $h\neq 0$ while we approach): get $2x+h$. *(Reason: factoring and cancellation, valid since $h\ne0$ in the limit process.)*
5. Let $h\to 0$: $2x+h\to 2x$. *(Reason: sum and constant limit laws from §s1.)*

**Numeric check.** At $x=3$, the rule gives $f'(3)=2\cdot 3=6$ — exactly the value the shrinking secants approached back in §s0 ($6.1$, then $6.01$, …).

<a id="s3"></a>
## Differentiation rules

*These let you differentiate any combination of functions without returning to the limit definition.* "To differentiate" means "to compute the derivative of."

**Constant**

$$\frac{d}{dx}[c]=0$$

*Why:* a constant function never changes, so its rate of change is $0$. Proof from the definition: $f(x)=c$ gives $\frac{c-c}{h}=\frac{0}{h}=0$, and the limit of $0$ is $0$ (§s1 constant limit). 

**Power rule — the workhorse**

$$\frac{d}{dx}\big[x^{n}\big]=n\,x^{\,n-1}$$

*In words:* bring the exponent $n$ down as a multiplier, then lower the exponent by one. We proved the case $n=2$ in §s2. 

**Worked example.** $\frac{d}{dx}x^5 = 5x^{4}$. At $x=2$: $5\cdot 2^4 = 5\cdot 16 = 80$.

**Constant multiple**

$$\frac{d}{dx}\big[c\,f(x)\big]=c\,f'(x)$$

*Why:* a constant factor scales every slope by the same amount; it factors out of the limit by the constant-multiple limit law (§s1).

**Sum / difference**

$$(f\pm g)'=f'\pm g'$$

*Why:* the derivative is a limit, and the limit of a sum is the sum of the limits (§s1). So derivatives split across $+$ and $-$.

**Worked example combining three rules.** Differentiate $f(x)=3x^4 - 7x + 2$.

1. $\frac{d}{dx}3x^4 = 3\cdot 4x^3 = 12x^3$. *(Reason: constant-multiple then power rule.)*
2. $\frac{d}{dx}(-7x)=-7\cdot 1x^0=-7$. *(Reason: power rule with $n=1$, since $x^0=1$.)*
3. $\frac{d}{dx}2 = 0$. *(Reason: constant rule.)*
4. Add: $f'(x)=12x^3-7$. *(Reason: sum/difference rule.)*

**Product rule**

$$(fg)' = f'g + fg'$$

*"First times derivative of second, plus second times derivative of first."* Note it is **not** $f'g'$ — that is the classic trap.

**Derivation of the product rule.**

1. By definition, $(fg)'=\lim_{h\to0}\dfrac{f(x+h)g(x+h)-f(x)g(x)}{h}$. *(Reason: derivative definition applied to the product.)*
2. Add and subtract $f(x+h)g(x)$ in the numerator (it cancels, so value unchanged): numerator $= f(x+h)g(x+h)-f(x+h)g(x)+f(x+h)g(x)-f(x)g(x)$. *(Reason: adding zero in a clever form.)*
3. Group: $= f(x+h)\big[g(x+h)-g(x)\big]+g(x)\big[f(x+h)-f(x)\big]$. *(Reason: factoring common terms.)*
4. Divide by $h$ and split into two limits: $\lim f(x+h)\cdot\frac{g(x+h)-g(x)}{h}+\lim g(x)\cdot\frac{f(x+h)-f(x)}{h}$. *(Reason: sum limit law.)*
5. As $h\to0$: $f(x+h)\to f(x)$ because differentiability forces continuity — $f(x+h)-f(x)=\frac{f(x+h)-f(x)}{h}\cdot h\to f'(x)\cdot 0=0$ — and the two difference quotients become $g'$ and $f'$. Result: $f g' + g f'$. *(Reason: definition of derivative, continuity of $f$, and product limit law.)*

**Worked example.** $\frac{d}{dx}\big[x^2\sin x\big]=2x\sin x + x^2\cos x$, using $(\sin x)'=\cos x$ from §s4.

**Quotient rule**

$$\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^{2}}$$

*"Low d-high minus high d-low, over low squared,"* where "low" $=g$ (the bottom) and "high" $=f$ (the top). It follows from the product rule applied to $f\cdot g^{-1}$ together with the chain rule below.

**Derivation of the quotient rule.**

1. Write $\frac{f}{g}=f\cdot g^{-1}$ and apply the product rule: $\left(\frac{f}{g}\right)'=f'\,g^{-1}+f\,(g^{-1})'$. *(Reason: product rule on the two factors $f$ and $g^{-1}$.)*
2. By the chain rule on $g^{-1}=g^{-1}$ (power rule outer, $g$ inner): $(g^{-1})'=-g^{-2}g'$. *(Reason: chain rule, since $\frac{d}{dg}g^{-1}=-g^{-2}$.)*
3. Substitute: $\left(\frac{f}{g}\right)'=\frac{f'}{g}-\frac{fg'}{g^{2}}$. *(Reason: insert step 2.)*
4. Put over the common denominator $g^2$: $\frac{f'}{g}=\frac{f'g}{g^2}$, so the result is $\frac{f'g-fg'}{g^{2}}$. *(Reason: combine the two fractions.)*

**Worked example.** $\dfrac{d}{dx}\dfrac{x}{x^2+1}=\dfrac{(1)(x^2+1)-(x)(2x)}{(x^2+1)^2}=\dfrac{1-x^2}{(x^2+1)^2}$.

**Chain rule — for functions inside functions**

$$\frac{d}{dx}\,f\big(g(x)\big)=f'\big(g(x)\big)\cdot g'(x) \qquad\text{or}\qquad \frac{dy}{dx}=\frac{dy}{du}\cdot\frac{du}{dx}$$

A **composite** function $f(g(x))$ is one function fed into another. *In words:* differentiate the outer layer (leaving the inside intact), then multiply by the derivative of the inside. Intuition with Leibniz form: if $y$ changes $\frac{dy}{du}$ times as fast as $u$, and $u$ changes $\frac{du}{dx}$ times as fast as $x$, the rates multiply.

**Worked example.** Differentiate $y=(3x+1)^4$. Outer is "fourth power," inner is $u=3x+1$.

1. Derivative of outer: $4u^3 = 4(3x+1)^3$. *(Reason: power rule on the outer layer.)*
2. Derivative of inner: $\frac{d}{dx}(3x+1)=3$. *(Reason: constant-multiple, power, constant rules.)*
3. Multiply: $y'=4(3x+1)^3\cdot 3 = 12(3x+1)^3$. *(Reason: chain rule.)*

> **Forward link**
>
> Keep the **product rule** and **chain rule** in mind. Read backwards, the product rule becomes *integration by parts* and the chain rule becomes *u-substitution* — the two big integration techniques in Section 9.

<a id="s4"></a>
## Derivatives of the standard functions

*Combine these with the rules above and you can differentiate almost anything.* These are the "atoms"; Section 3 gives the rules for assembling them.

### Exponential & logarithmic

An **exponential** function $a^x$ raises a fixed base $a$ to a variable power $x$. A **logarithm** $\log_a x$ asks "what power of $a$ gives $x$?"; $\ln x$ is the special case with base $e$ (the number from §s1), called the **natural logarithm**.

| Function | Derivative |
| --- | --- |
| $e^{x}$ | $e^{x}$  *(the function that is its own derivative)* |
| $a^{x}$ | $a^{x}\ln a$ |
| $\ln x$ | $\dfrac{1}{x}$ |
| $\log_a x$ | $\dfrac{1}{x\ln a}$ |

**Why $e^x$ is its own derivative (sketch).** From the definition, $(e^x)'=\lim_{h\to0}\frac{e^{x+h}-e^x}{h}=e^x\lim_{h\to0}\frac{e^h-1}{h}$, and the special limit defining $e$ makes that last limit equal $1$. So $(e^x)'=e^x\cdot 1=e^x$. *(Reason: derivative definition, factoring $e^x$ out, and the limit $\lim_{h\to0}\frac{e^h-1}{h}=1$ which is the defining property of $e$.)*

**Worked example.** $\frac{d}{dx}\big[5\,e^x\big]=5e^x$; at $x=0$ this is $5\cdot 1 = 5$ (since $e^0=1$).

### Trigonometric

The **trigonometric** functions $\sin x$, $\cos x$, etc. describe positions on a circle; $x$ here is an angle measured in **radians** (the natural angle unit, where a full circle is $2\pi$).

| Function | Derivative | Function | Derivative |
| --- | --- | --- | --- |
| $\sin x$ | $\cos x$ | $\cot x$ | $-\csc^{2}x$ |
| $\cos x$ | $-\sin x$ | $\sec x$ | $\sec x\tan x$ |
| $\tan x$ | $\sec^{2}x$ | $\csc x$ | $-\csc x\cot x$ |

**Why $(\sin x)'=\cos x$ (sketch).** The definition gives $\lim_{h\to0}\frac{\sin(x+h)-\sin x}{h}$. Using the identity $\sin(x+h)=\sin x\cos h+\cos x\sin h$ and the special limits $\frac{\sin h}{h}\to1$ and $\frac{1-\cos h}{h}\to0$ from §s1, this collapses to $\cos x$. *(Reason: angle-addition identity and the two special trig limits.)*

**Worked example.** $\frac{d}{dx}\sin(2x)=\cos(2x)\cdot 2 = 2\cos(2x)$, using the chain rule (§s3) with inner $u=2x$.

### Inverse trigonometric

An **inverse** function undoes another; $\arcsin x$ answers "which angle has sine equal to $x$?"

| Function | Derivative |
| --- | --- |
| $\arcsin x$ | $\dfrac{1}{\sqrt{1-x^{2}}}$ |
| $\arccos x$ | $-\dfrac{1}{\sqrt{1-x^{2}}}$ |
| $\arctan x$ | $\dfrac{1}{1+x^{2}}$ |

**Worked example.** $\frac{d}{dx}\arctan x$ at $x=1$ is $\frac{1}{1+1^2}=\frac{1}{2}$.

> **A quiet symmetry**
>
> Notice the pairs: $(\sin)'=\cos$ and $(\cos)'=-\sin$. Differentiating sine four times returns you to sine. These cycles are exactly why $\sin$ and $\cos$ describe everything that oscillates.

<a id="s5"></a>
## Implicit, logarithmic & higher-order derivatives

*Three extensions for when y is tangled up, the exponents are messy, or you need to differentiate more than once.*

**Implicit differentiation**

$$\frac{d}{dx}\big[\,y\,\big]=\frac{dy}{dx},\qquad \frac{d}{dx}\big[\,y^{2}\,\big]=2y\frac{dy}{dx}$$

An equation defines $y$ **implicitly** when $y$ is not written alone on one side (e.g. $x^2+y^2=25$, a circle). We treat $y$ as a hidden function of $x$; every time we differentiate a $y$-term, the chain rule (§s3) attaches a factor $\frac{dy}{dx}$.

**Worked example.** Find $\frac{dy}{dx}$ for $x^2+y^2=25$ at the point $(3,4)$.

1. Differentiate each term in $x$: $\frac{d}{dx}x^2=2x$. *(Reason: power rule.)*
2. $\frac{d}{dx}y^2 = 2y\frac{dy}{dx}$. *(Reason: chain rule, since $y$ depends on $x$.)*
3. $\frac{d}{dx}25 = 0$. *(Reason: constant rule.)*
4. So $2x+2y\frac{dy}{dx}=0$, giving $\frac{dy}{dx}=-\frac{x}{y}$. *(Reason: solve the equation for $\frac{dy}{dx}$.)*
5. At $(3,4)$: $\frac{dy}{dx}=-\frac{3}{4}$. *(Reason: substitute the point.)*

**Logarithmic differentiation**

$$y=f(x)^{g(x)} \;\Rightarrow\; \ln y = g(x)\ln f(x) \;\Rightarrow\; \frac{y'}{y}=\frac{d}{dx}\big[g\ln f\big]$$

*Take $\ln$ of both sides first to turn powers into products* (using $\ln(a^b)=b\ln a$). Essential for things like $x^{x}$, where both base and exponent vary.

**Worked example.** Differentiate $y=x^x$.

1. $\ln y = x\ln x$. *(Reason: logarithm power rule.)*
2. Differentiate both sides; left side by chain rule is $\frac{y'}{y}$; right side by product rule is $\ln x + x\cdot\frac1x=\ln x+1$. *(Reason: chain rule and product rule.)*
3. So $y' = y(\ln x + 1)=x^x(\ln x+1)$. *(Reason: multiply both sides by $y$.)*

**Higher-order derivatives**

$$f''(x)=\frac{d}{dx}f'(x),\qquad f^{(n)}(x)=\frac{d^{\,n}y}{dx^{\,n}}$$

The **second derivative** $f''$ is the derivative of the derivative — the rate of change of the rate of change. If $s(t)$ is position, $s'$ is velocity and $s''$ is acceleration.

**Worked example.** For $f(x)=x^3$: $f'(x)=3x^2$, $f''(x)=6x$, $f'''(x)=6$, and $f^{(4)}(x)=0$.

<a id="s6"></a>
## Putting derivatives to work

*The payoff: tangent lines, shapes of curves, optimization, and limits that looked impossible.*

**Tangent line at x = a**

$$y - f(a) = f'(a)\,(x-a)$$

This is the straight line touching the curve at $x=a$. *Why:* it passes through $(a,f(a))$ and has slope $f'(a)$, the derivative there; the formula is the point-slope form of a line.

**Worked example.** For $f(x)=x^2$ at $a=3$: $f(3)=9$, $f'(3)=6$, so the tangent is $y-9=6(x-3)$, i.e. $y=6x-9$.

### Reading the shape of a curve

- $f'(x)>0$ → function **increasing** (going up as $x$ grows); $f'(x)<0$ → **decreasing**.
- **Critical points** where $f'(x)=0$ or is undefined are candidates for maxima/minima (peaks and valleys).
- $f''(x)>0$ → **concave up** (shaped like a cup); $f''(x)<0$ → **concave down** (shaped like a cap).
- **Inflection point**: where $f''$ changes sign (the curve switches from cup to cap or vice versa).

**Second-derivative test**

$$f'(c)=0:\quad f''(c)>0 \Rightarrow \text{local min},\qquad f''(c)<0 \Rightarrow \text{local max}$$

*Why:* at a flat spot ($f'(c)=0$), if the curve is cup-shaped ($f''>0$) the point is a bottom (minimum); if cap-shaped ($f''<0$) it is a top (maximum).

**Worked optimization example.** Minimize $f(x)=x^2-4x+7$.

1. $f'(x)=2x-4$. Set to $0$: $x=2$. *(Reason: power and constant rules; critical point.)*
2. $f''(x)=2>0$, so $x=2$ is a local minimum. *(Reason: second-derivative test.)*
3. Minimum value: $f(2)=4-8+7=3$. *(Reason: substitute.)*

**Mean Value Theorem**

$$\exists\, c\in(a,b):\quad f'(c)=\frac{f(b)-f(a)}{b-a}$$

*In words:* somewhere strictly inside the interval $(a,b)$, the instantaneous slope $f'(c)$ equals the average slope across the whole interval. (Rolle's theorem is the special case where $f(a)=f(b)$, giving $f'(c)=0$.)

**Worked example.** For $f(x)=x^2$ on $[0,4]$: average slope $=\frac{16-0}{4-0}=4$. Solve $f'(c)=2c=4$, so $c=2$ lies in $(0,4)$, as promised.

**L'Hôpital's rule — for 0/0 or ∞/∞**

$$\lim_{x\to a}\frac{f(x)}{g(x)} = \lim_{x\to a}\frac{f'(x)}{g'(x)}$$

An **indeterminate form** like $\frac{0}{0}$ tells you nothing on its own. When a limit takes that shape, differentiate top and bottom **separately** and try again — a loop back to Section 1.

**Worked example.** $\lim_{x\to0}\frac{\sin x}{x}$ is $\frac{0}{0}$. Differentiate: $\frac{\cos x}{1}\to\cos 0 = 1$. This recovers the special limit from §s1.

**Linear approximation & differentials**

$$f(x)\approx f(a)+f'(a)(x-a),\qquad dy=f'(x)\,dx$$

*Near a point, every smooth curve looks like its tangent line,* so we estimate nearby outputs using the tangent. The **differential** $dy=f'(x)\,dx$ packages "small change in output $\approx$ slope times small change in input."

**Worked example.** Estimate $\sqrt{4.1}$ with $f(x)=\sqrt x$, $a=4$. Then $f(4)=2$, $f'(x)=\frac{1}{2\sqrt x}$ so $f'(4)=\frac14$. Approximation: $\sqrt{4.1}\approx 2+\frac14(0.1)=2.025$. (True value $\approx 2.0248$.)

<a id="s7"></a>
## The antiderivative & the Fundamental Theorem

*The hinge of the entire subject. Here the derivative and the integral are revealed to be two sides of one coin.*

**Indefinite integral (antiderivative)**

$$\int f(x)\,dx = F(x)+C \quad\text{where}\quad F'(x)=f(x)$$

*Reading the symbols:* "$\int$" is the **integral sign**; "$dx$" marks $x$ as the variable; $F$ is an **antiderivative** of $f$ (a function whose derivative is $f$); $C$ is an arbitrary constant. Integrating means asking "what function has THIS as its derivative?" The $+C$ appears because constants vanish when differentiated, so infinitely many functions differing by a constant all work.

**Worked example.** $\int 3x^2\,dx = x^3 + C$, because $\frac{d}{dx}(x^3+C)=3x^2$.

**Definite integral as a limit of Riemann sums**

$$\int_{a}^{b} f(x)\,dx = \lim_{n\to\infty}\sum_{i=1}^{n} f(x_i^{*})\,\Delta x$$

*Reading the symbols:* the numbers $a$ and $b$ are the **limits of integration** (the start and end on the $x$-axis); "$\sum$" means "add up"; $n$ is the number of rectangles; $\Delta x=\frac{b-a}{n}$ is the width of each; $x_i^*$ is a sample point in the $i$-th strip; $f(x_i^*)\,\Delta x$ is the area of one thin rectangle. Slice the area under the curve into $n$ rectangles, add them, then let $n\to\infty$ so the slices become infinitely thin. The integral **is** an infinite sum — the same "push to a limit" move that built the derivative.

**Worked example.** Estimate $\int_0^2 x\,dx$ with $n=4$ rectangles using right endpoints. Then $\Delta x=0.5$, sample points $0.5,1,1.5,2$, heights equal to those. Sum $=(0.5+1+1.5+2)(0.5)=5\cdot0.5=2.5$. The exact answer (the area of a triangle of base $2$, height $2$) is $2$; finer slices close the gap.

### The Fundamental Theorem of Calculus

This is the bridge promised in §s0. It comes in two parts.

**Part 1 — differentiation undoes integration**

$$\frac{d}{dx}\int_{a}^{x} f(t)\,dt = f(x)$$

*In words:* if you build an area-so-far function (integrate $f$ from $a$ up to a moving right edge $x$) and then differentiate it, you get $f$ back. Accumulating then measuring the rate returns the original.

**Part 2 — integration is evaluated by antiderivatives**

$$\int_{a}^{b} f(x)\,dx = F(b)-F(a),\quad F'=f$$

*In words:* to compute a definite integral, find any antiderivative $F$ and subtract its values at the endpoints. No infinite summing required.

**Worked example using Part 2.** $\int_0^2 x\,dx$. An antiderivative of $x$ is $F(x)=\frac{x^2}{2}$. Then $F(2)-F(0)=\frac{4}{2}-0=2$ — matching the exact area above, with no rectangles at all.

> **The payoff**
>
> Part 2 is astonishing: to find an area (an infinite sum of rectangles), you don't add anything — you just find an antiderivative and subtract two values. This is why every derivative formula in Sections 3–4 instantly becomes an integral formula in Section 8, simply by reading the table backwards.

<a id="s8"></a>
## The basic integral table

*Each line is a derivative rule run in reverse. Compare it directly to Sections 3–4.* To check any line, just differentiate the right side and confirm you get the integrand back (FTC, §s7).

**Power rule for integrals (reverse of the power rule)**

$$\int x^{n}\,dx = \frac{x^{\,n+1}}{n+1}+C \quad (n\neq -1)$$

*Why:* differentiate $\frac{x^{n+1}}{n+1}$ by the power rule (§s3): bring down $n+1$, lower the power, and the $n+1$ cancels, leaving $x^n$. The case $n=-1$ is forbidden because it would divide by $n+1=0$.

**Worked example.** $\int x^3\,dx=\frac{x^4}{4}+C$. Check: $\frac{d}{dx}\frac{x^4}{4}=\frac{4x^3}{4}=x^3$. 

**The n = −1 exception**

$$\int \frac{1}{x}\,dx = \ln|x|+C$$

*Why:* from §s4, $(\ln x)'=\frac1x$; the absolute value lets it work for negative $x$ too.

| Integral | Result | Reverse of… |
| --- | --- | --- |
| $\int e^{x}\,dx$ | $e^{x}+C$ | $(e^x)'=e^x$ |
| $\int a^{x}\,dx$ | $\dfrac{a^{x}}{\ln a}+C$ | $(a^x)'=a^x\ln a$ |
| $\int \cos x\,dx$ | $\sin x+C$ | $(\sin x)'=\cos x$ |
| $\int \sin x\,dx$ | $-\cos x+C$ | $(\cos x)'=-\sin x$ |
| $\int \sec^{2}x\,dx$ | $\tan x+C$ | $(\tan x)'=\sec^2 x$ |
| $\int \dfrac{1}{1+x^{2}}\,dx$ | $\arctan x+C$ | $(\arctan x)'=\frac{1}{1+x^2}$ |
| $\int \dfrac{1}{\sqrt{1-x^{2}}}\,dx$ | $\arcsin x+C$ | $(\arcsin x)'=\frac{1}{\sqrt{1-x^2}}$ |

**Worked definite example.** $\int_0^{\pi/2}\cos x\,dx = [\sin x]_0^{\pi/2}=\sin\frac{\pi}{2}-\sin 0 = 1-0 = 1$ (FTC Part 2, §s7).

> **How to read this section**
>
> Don't memorize this table separately. If you know the derivative table cold, you already know the integral table — just flip the arrow. That is the whole point of the Fundamental Theorem.

<a id="s9"></a>
## Integration techniques

*When an integral doesn't match the table, these tools reshape it until it does. Two of them are differentiation rules in reverse.*

**u-substitution — the chain rule, reversed**

$$\int f\big(g(x)\big)\,g'(x)\,dx = \int f(u)\,du,\qquad u=g(x)$$

*In words:* spot an inside function $g(x)$ and its derivative $g'(x)$ both present; rename the inside as $u$, so $du=g'(x)\,dx$. This undoes the chain rule (§s3).

**Worked example.** $\int 2x(x^2+1)^3\,dx$. Let $u=x^2+1$, so $du=2x\,dx$.

1. Replace: integral becomes $\int u^3\,du$. *(Reason: substitution $u=x^2+1$, $du=2x\,dx$.)*
2. Integrate: $\frac{u^4}{4}+C$. *(Reason: power rule for integrals, §s8.)*
3. Restore $u$: $\frac{(x^2+1)^4}{4}+C$. *(Reason: undo the substitution.)*

**Integration by parts — the product rule, reversed**

$$\int u\,dv = uv - \int v\,du$$

This comes straight from integrating the product rule $(uv)'=u'v+uv'$ and rearranging. Use it for products like $\int x e^{x}\,dx$ or $\int x\ln x\,dx$.

**Worked example.** $\int x e^x\,dx$. Choose $u=x$ (so $du=dx$) and $dv=e^x\,dx$ (so $v=e^x$).

1. Apply the formula: $\int x e^x\,dx = x e^x - \int e^x\,dx$. *(Reason: integration by parts with the choices above.)*
2. $\int e^x\,dx = e^x+C$. *(Reason: integral table, §s8.)*
3. Result: $x e^x - e^x + C = e^x(x-1)+C$. *(Reason: substitute and factor.)*

**Trigonometric substitution**

$$\sqrt{a^2-x^2}\Rightarrow x=a\sin\theta,\quad \sqrt{a^2+x^2}\Rightarrow x=a\tan\theta,\quad \sqrt{x^2-a^2}\Rightarrow x=a\sec\theta$$

*Trade an awkward square root for a clean trig identity.* For example, $\sqrt{a^2-x^2}$ with $x=a\sin\theta$ becomes $a\cos\theta$, using $1-\sin^2\theta=\cos^2\theta$.

**Partial fractions**

$$\frac{P(x)}{(x-r_1)(x-r_2)} = \frac{A}{x-r_1}+\frac{B}{x-r_2}$$

*Break a complicated rational function into simple pieces,* each of which integrates to a logarithm or arctangent (§s8).

**Worked example.** Write $\frac{1}{(x-1)(x+1)}=\frac{A}{x-1}+\frac{B}{x+1}$. Multiply out: $1=A(x+1)+B(x-1)$. Set $x=1$: $1=2A$, so $A=\frac12$. Set $x=-1$: $1=-2B$, so $B=-\frac12$. Hence the integral is $\frac12\ln|x-1|-\frac12\ln|x+1|+C$.

### Useful properties of definite integrals

$$\int_a^b f\,dx = -\int_b^a f\,dx,\qquad \int_a^a f\,dx = 0,\qquad \int_a^b f\,dx = \int_a^c f\,dx + \int_c^b f\,dx$$

*In words:* swapping the endpoints flips the sign; an interval of zero width has zero area; and an integral can be split at any in-between point $c$ and the pieces added.

> **The mirror, made explicit**
>
> Chain rule ⟷ u-substitution. Product rule ⟷ integration by parts. Differentiation has clean, always-works rules; integration is the reverse search, so it needs clever techniques. Same relationships, harder direction.

<a id="s10"></a>
## Putting integrals to work

*Anything that accumulates — area, volume, length, averages — is an integral.* The recipe is always: describe one tiny slice, then integrate to add up infinitely many (the Riemann idea, §s7).

**Area between two curves**

$$A=\int_a^b \big[\,f(x)-g(x)\,\big]\,dx$$

*Why:* a thin vertical strip at position $x$ has height $f(x)-g(x)$ (top minus bottom) and width $dx$; integrating sums all strips.

**Worked example.** Area between $f(x)=x+2$ and $g(x)=x^2$ where they cross. They meet where $x+2=x^2$, i.e. $x^2-x-2=0=(x-2)(x+1)$, so $x=-1$ and $x=2$. Then $A=\int_{-1}^{2}(x+2-x^2)\,dx=\left[\frac{x^2}{2}+2x-\frac{x^3}{3}\right]_{-1}^{2}$. At $x=2$: $2+4-\frac{8}{3}=\frac{10}{3}$. At $x=-1$: $\frac12-2+\frac13=-\frac{7}{6}$. Difference: $\frac{10}{3}+\frac{7}{6}=\frac{27}{6}=\frac{9}{2}$.

**Volume of revolution — disk method**

$$V=\pi\int_a^b \big[f(x)\big]^2\,dx$$

*Why:* spinning the curve around the $x$-axis sweeps thin disks of radius $f(x)$; one disk has area $\pi[f(x)]^2$ and thickness $dx$.

**Worked example.** Spin $f(x)=x$ on $[0,1]$ (a cone): $V=\pi\int_0^1 x^2\,dx=\pi\left[\frac{x^3}{3}\right]_0^1=\frac{\pi}{3}$.

**Volume of revolution — shell method**

$$V=2\pi\int_a^b x\,f(x)\,dx$$

*Why:* this builds the solid from nested cylindrical shells of radius $x$, height $f(x)$, thickness $dx$; one shell unrolls to a sheet of area $2\pi x\,f(x)$.

**Arc length of a curve**

$$L=\int_a^b \sqrt{1+\big[f'(x)\big]^2}\;dx$$

*Why:* a tiny piece of curve is the hypotenuse of a right triangle with legs $dx$ and $f'(x)\,dx$; the Pythagorean theorem gives its length $\sqrt{1+[f'(x)]^2}\,dx$.

**Average value of a function**

$$\bar f=\frac{1}{b-a}\int_a^b f(x)\,dx$$

*Why:* total accumulation divided by the length of the interval is the average height, mirroring how an ordinary average is a sum divided by a count.

**Worked example.** Average of $f(x)=x^2$ on $[0,3]$: $\frac{1}{3}\int_0^3 x^2\,dx=\frac13\left[\frac{x^3}{3}\right]_0^3=\frac13\cdot 9 = 3$.

> **The common thread**
>
> Every formula here follows the same recipe: take a tiny slice (a sliver of area, a thin disk, a short segment), write its size, then integrate to add up infinitely many of them. That is the Riemann-sum idea from Section 7 applied over and over.

<a id="s11"></a>
## Sequences & series

*What happens when you add infinitely many terms? Sometimes the total is finite — and that lets us rebuild functions from their derivatives.* A **sequence** is an ordered list of numbers; a **series** is what you get by adding a sequence's terms. A series **converges** if its running total settles toward a single finite number, and **diverges** otherwise.

**Geometric series**

$$\sum_{n=0}^{\infty} a r^{n} = \frac{a}{1-r}\quad (|r|<1)$$

Here each term is the previous one times a fixed **ratio** $r$, starting from $a$. *Why it converges when $|r|<1$:* work with the finite partial sum $S_n=a+ar+\cdots+ar^{n-1}$ first, so nothing is assumed about an infinite total. Then $rS_n=ar+ar^2+\cdots+ar^{n}$, and subtracting cancels every middle term: $S_n-rS_n=a-ar^{n}$, so $S_n=\frac{a(1-r^{n})}{1-r}$. Now let $n\to\infty$: when $|r|<1$, $r^{n}\to0$, hence $S_n\to\frac{a}{1-r}$. *(Reason: the partial-sum formula is plain algebra; convergence enters only at the last step, where $r^{n}\to0$.)*

**Worked example.** $\frac12+\frac14+\frac18+\cdots$ has $a=\frac12$, $r=\frac12$, sum $=\frac{1/2}{1-1/2}=1$.

**p-series (convergence test case)**

$$\sum_{n=1}^{\infty}\frac{1}{n^{p}}\ \text{converges} \iff p>1$$

*In words:* the sum of reciprocal $p$-th powers settles down exactly when $p>1$. With $p=1$ it diverges (the famous harmonic series); with $p=2$ it converges.

### Convergence tests (does the sum settle down?)

| Test | Rule of thumb |
| --- | --- |
| Ratio test | $\lim\left\vert \dfrac{a_{n+1}}{a_n}\right\vert =L$; converges if $L<1$ |
| Comparison | Bound your series by a known one |
| Integral test | $\sum a_n$ and $\int f\,dx$ converge together |

**Worked ratio-test example.** For $\sum \frac{1}{n!}$, the ratio $\frac{1/(n+1)!}{1/n!}=\frac{1}{n+1}\to 0 = L<1$, so it converges (and in fact sums to $e$).

**Taylor series — a function rebuilt from its derivatives**

$$f(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}\,(x-a)^{n}$$

*Reading the symbols:* $f^{(n)}(a)$ is the $n$-th derivative at $a$ (§s5); $n!$ ("$n$ factorial") is $1\cdot2\cdots n$. The **Maclaurin series** is the special case $a=0$. This is the linear approximation of Section 6 continued to infinitely many derivatives — each derivative pins down one more term.

### The famous expansions

$$e^{x}=\sum_{n=0}^{\infty}\frac{x^{n}}{n!}=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots$$

$$\sin x = x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots \qquad \cos x = 1-\frac{x^2}{2!}+\frac{x^4}{4!}-\cdots$$

$$\frac{1}{1-x}=\sum_{n=0}^{\infty}x^{n}\quad(|x|<1)$$

**Worked example.** Approximate $e^{0.1}$ with the first three terms: $1+0.1+\frac{0.01}{2}=1.105$. (True value $\approx 1.10517$.)

> **A glimpse of the unity**
>
> Feed $x=i\theta$ into the series for $e^x$ and compare with $\sin$ and $\cos$, and you land on Euler's formula $e^{i\theta}=\cos\theta+i\sin\theta$. The series built from derivatives quietly ties exponentials to oscillation.

<a id="s12"></a>
## A peek at multivariable calculus

*The same two ideas — slope and accumulation — in more than one dimension.* Now a function takes several inputs, e.g. $f(x,y)$ depends on both $x$ and $y$ (think of height above a point on a map).

**Partial derivative**

$$\frac{\partial f}{\partial x}=\lim_{h\to0}\frac{f(x+h,\,y)-f(x,\,y)}{h}$$

The curly "$\partial$" marks a **partial derivative**: differentiate with respect to one variable while treating the others as constants. It is exactly the Section 2 definition, holding $y$ still.

**Worked example.** For $f(x,y)=x^2y+y^3$: treating $y$ as constant, $\frac{\partial f}{\partial x}=2xy$; treating $x$ as constant, $\frac{\partial f}{\partial y}=x^2+3y^2$.

**Gradient (vector of all partials)**

$$\nabla f = \left\langle \frac{\partial f}{\partial x},\ \frac{\partial f}{\partial y},\ \frac{\partial f}{\partial z} \right\rangle$$

The symbol "$\nabla$" is read "del." The **gradient** collects all the partial derivatives into one arrow (a **vector**) that points in the direction of steepest increase — the multivariable cousin of the derivative.

**Worked example.** For $f(x,y)=x^2+y^2$, $\nabla f=\langle 2x, 2y\rangle$; at the point $(1,1)$ it is $\langle 2,2\rangle$, pointing outward and uphill.

**Double integral (accumulation over a region)**

$$\iint_{R} f(x,y)\,dA = \int_{c}^{d}\!\int_{a}^{b} f(x,y)\,dx\,dy$$

A **double integral** adds up $f$ over a flat region $R$, where $dA$ is a tiny patch of area; we compute it as an inner integral in $x$, then an outer integral in $y$. It gives the volume under a surface, from the same Riemann-sum idea — now stacking tiny boxes instead of rectangles.

**Worked example.** $\int_0^1\!\int_0^1 (x+y)\,dx\,dy$. Inner: $\int_0^1(x+y)\,dx=\left[\frac{x^2}{2}+yx\right]_0^1=\frac12+y$. Outer: $\int_0^1(\frac12+y)\,dy=\left[\frac{y}{2}+\frac{y^2}{2}\right]_0^1=\frac12+\frac12=1$.

> **Where it all goes**
>
> From here the path continues to the great integral theorems (Green's, Stokes', Divergence) — each one a higher-dimensional Fundamental Theorem of Calculus, saying again that what happens on a boundary is governed by what happens inside.

---

*Read it once for the shape, then return to any section as a reference. The deepest habit to build: whenever you meet a new formula, ask which earlier idea it is secretly a version of. In calculus, almost everything is.*
