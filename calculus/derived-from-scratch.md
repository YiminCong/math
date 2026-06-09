**English** · [中文](derived-from-scratch.zh.md)

# Calculus, *derived.*

Not just a list of formulas — every core formula below is **demonstrated**: shown where it comes from, step by step. The order runs basics → advanced, and each piece is built from the one before it. This version assumes you bring *no* mathematical background at all: every symbol is named in plain words the first time it appears, every algebra step is shown, and every claim is justified by an earlier rule that we name out loud.

[← Back to all guides](../README.md)

<a id="s0"></a>
## The big picture before any symbols

*One map to hold in your head.*

Before any formula, let us agree on what calculus even *is*, in ordinary words.

**What "calculus" means.** The word comes from the Latin for "small pebble" — the pebbles people once used for counting. Today it names the mathematics of *change* and *accumulation*. There are exactly two central questions, and a third fact that ties them together.

- **The derivative** asks: *how fast is this changing right now?* Think of the speedometer in a car. At one frozen instant it reads, say, 60 km/h — a *rate*, a *slope*, a *speed*. The derivative is the tool that produces that instantaneous number.
- **The integral** asks: *how much has accumulated in total?* Think of the odometer in the same car: it has added up all the little distances travelled into one total. The integral is the tool that produces that running total — an *area*, a *distance*, a *sum*.

**The key trick that powers everything: the limit.** Both tools are built by taking something simple that we already understand — the slope between two points, or the area of a rectangle — and then *pushing it to a limit*: we let a small gap shrink toward zero and watch what number the result heads toward. The word "limit" here means exactly that: *the value something approaches.* Because both tools rest on limits, limits must come first.

#### Why we cannot just "plug in zero"

You might ask: if the gap shrinks to zero, why not set it to zero from the start? Because the quantities we care about are *fractions* whose top and bottom both shrink to zero at once, like the slope (rise over run) of two points that merge into one. Plugging in zero gives the meaningless symbol $\tfrac{0}{0}$. The limit is the careful, honest way to ask "what number is this fraction heading toward?" without ever dividing by zero. Everything that follows is a disciplined way of answering that question.

### The whole course on one line

> Limits → Derivatives → Integrals ↔ (linked by the FTC) → Series → Multivariable

Read left to right, each topic is built from the one before it. "FTC" is the **Fundamental Theorem of Calculus**, the bridge in the middle.

> **The thread to follow**
>
> The **Fundamental Theorem of Calculus** (Section 7) says differentiation and integration undo each other, the way addition undoes subtraction. Because of it, every integration formula in Sections 8–9 is a differentiation formula from Sections 3–4 read backwards — and we will literally derive them that way.

**A worked taste of the whole idea.** Suppose a ball's height after $t$ seconds is $h(t) = 5t^2$ metres.
- *Derivative question:* how fast is it rising at $t = 2$? We will learn (Section 2–3) that the rate is $h'(t) = 10t$, so at $t = 2$ the speed is $10 \times 2 = 20$ metres per second.
- *Integral question:* a tap pours water at a rate of $10t$ litres per second; how much water after $2$ seconds? We will learn (Section 7–8) that the total is $5t^2$ evaluated at $t=2$, namely $5 \times 4 = 20$ litres.

Notice the two answers come from the *same pair of formulas read in opposite directions*. That mirror is the whole subject in miniature.

<a id="s1"></a>
## Limits & continuity

*A limit answers: where is the function heading as the input approaches a value — even if it never arrives?*

**Words first.** A **function** $f$ is a rule that takes an input number (we usually call it $x$) and returns exactly one output number (we write it $f(x)$, read "f of x"). The set of allowed inputs is the **domain**. A **limit** asks about the *trend* of the outputs as the input is dialled toward some target $a$ — *regardless of what happens exactly at $a$ itself*.

**Intuitive limit**

$$\lim_{x \to a} f(x) = L$$

*As $x$ gets arbitrarily close to $a$, $f(x)$ gets arbitrarily close to $L$.* The symbol $\lim$ is short for "limit"; $x \to a$ is read "$x$ approaches $a$"; $L$ is the value being approached.

**Worked example (an honest $\tfrac{0}{0}$).** Consider $f(x) = \dfrac{x^2 - 1}{x - 1}$. At $x = 1$ this is $\tfrac{0}{0}$, undefined. But for every $x \neq 1$ we may simplify, because $x^2 - 1 = (x-1)(x+1)$ (a factoring identity: the difference of two squares):

$$f(x) = \frac{(x-1)(x+1)}{x-1} = x + 1 \quad (x \neq 1).$$

As $x$ heads to $1$, $x + 1$ heads to $2$. So $\lim_{x \to 1} f(x) = 2$, even though $f(1)$ does not exist. This is exactly the kind of "where is it heading?" question limits answer.

**Formal (ε–δ) definition**

$$\forall\, \varepsilon>0,\; \exists\, \delta>0 \;:\; 0<|x-a|<\delta \implies |f(x)-L|<\varepsilon$$

*Name any tolerance ε around L; I can find a window δ around a that keeps me inside it.* Here $\forall$ means "for every," $\exists$ means "there exists," $\varepsilon$ (epsilon) is a tiny target tolerance, $\delta$ (delta) is the input window we choose, and $|u|$ is the **absolute value** of $u$ — its size ignoring sign, so $|{-3}| = 3$. The clause $0 < |x-a|$ deliberately excludes the point $x = a$ itself, matching the idea "even if it never arrives." Read as a game: an opponent picks how close to $L$ you must land ($\varepsilon$); you must always be able to answer with a window around $a$ ($\delta$) that forces it. If you can always answer, the limit is $L$.

**One-sided & existence**

$$\lim_{x\to a^-}f(x)=\lim_{x\to a^+}f(x)=L \iff \lim_{x\to a}f(x)=L$$

*The two-sided limit exists only when the left and right approaches agree.* The notation $a^-$ means "approach $a$ from the left (smaller values)"; $a^+$ means "from the right (larger values)"; $\iff$ means "if and only if" (each side forces the other). If the two one-sided limits disagree, the plain limit does not exist — picture a stairstep that jumps at $a$.

**Limits at infinity / infinite limits**

$$\lim_{x\to\infty}\frac{1}{x}=0, \qquad \lim_{x\to 0^+}\frac{1}{x}=+\infty$$

The symbol $\infty$ ("infinity") is not a number but a shorthand for "grows without bound." Left equation: as $x$ grows huge, $1/x$ becomes tiny, heading to $0$ (e.g. $1/1000 = 0.001$). Right equation: as $x$ shrinks toward $0$ from the positive side, $1/x$ explodes upward (e.g. $1/0.001 = 1000$).

### Limit laws (how limits combine)

**Why we care.** Computing every limit from the ε–δ definition would be exhausting. These laws let us build complicated limits out of simple ones by treating $\lim$ almost like ordinary arithmetic.

If $\lim f = L$ and $\lim g = M$ (both existing and finite):

$$\lim (f \pm g)=L\pm M,\quad \lim (fg)=LM,\quad \lim \tfrac{f}{g}=\tfrac{L}{M}\,(M\neq0),\quad \lim cf=cL$$

In words: the limit of a sum is the sum of the limits; of a product, the product; of a quotient, the quotient (as long as the bottom limit $M$ is not zero); and a constant multiplier $c$ slides outside. These hold because if $f$ is trapped near $L$ and $g$ near $M$, then $f+g$ is trapped near $L+M$, and likewise for the others; each can be proven from the ε–δ definition by choosing tolerances carefully.

**Worked example.** $\lim_{x\to 2}(3x^2 - x) = 3\lim_{x\to2}x^2 - \lim_{x\to2}x = 3(2^2) - 2 = 12 - 2 = 10$, using the constant-multiple, difference, and product laws in turn.

**Squeeze (sandwich) theorem**

$$g(x)\le f(x)\le h(x)\ \text{and}\ \lim g=\lim h=L \implies \lim f=L$$

*If a function is trapped between two others that meet at the same value, it is forced to that value too.* The symbol $\le$ means "less than or equal to." Intuition: if you are walking between two friends who both arrive at the same door, you arrive there as well — you have no choice. This theorem is the tool we need for the first special limit below.

### The special limits — and where they come from

**Three limits to know**

$$\lim_{x\to0}\frac{\sin x}{x}=1,\qquad \lim_{x\to0}\frac{1-\cos x}{x}=0,\qquad \lim_{x\to0}\frac{e^{x}-1}{x}=1$$

Here $\sin$ and $\cos$ are the **sine** and **cosine**, the two basic functions of an angle (measured in **radians**, where a full turn is $2\pi$); $e \approx 2.71828$ is **Euler's number**, the natural growth constant. These three "$0/0$" limits are the seeds from which the derivatives of $\sin$, $\cos$, and $e^x$ grow (Sections 3–4).

**Demonstration — why $ \lim_{x\to0}\frac{\sin x}{x}=1 $**

Geometric setup: draw a circle of radius $1$ and a small positive angle $x$ (in radians). Comparing the areas/lengths of a triangle inside the wedge, the wedge itself, and a triangle outside gives the chain of inequalities below.

1. For a small angle $x$ (in radians, $0 < x < \tfrac{\pi}{2}$), the geometry of the unit circle gives

   $$\sin x < x < \tan x.$$
   The reason: the straight segment $\sin x$ is shorter than the arc $x$, which is shorter than the tangent segment $\tan x$ — each enclosing the previous.
2. Divide every part by $\sin x>0$ (dividing an inequality by a positive number keeps the directions):

   $$1 < \frac{x}{\sin x} < \frac{1}{\cos x}.$$
   (Here $\tan x = \tfrac{\sin x}{\cos x}$, so $\tfrac{\tan x}{\sin x} = \tfrac{1}{\cos x}$.)
3. Take reciprocals of all three. Taking reciprocals of positive quantities *reverses* each inequality:

   $$\cos x < \frac{\sin x}{x} < 1.$$
4. As $x\to0$, $\cos 0 = 1$, so $\cos x\to1$; the right bound is the constant $1$. The fraction $\tfrac{\sin x}{x}$ is squeezed between two things heading to $1$, so by the **Squeeze Theorem** (just above) it also $\to 1$.

*This single limit is what makes $(\sin x)'=\cos x$ work in Section 4.*

**Worked numeric check.** With $x = 0.01$ radian: $\sin(0.01) \approx 0.00999983$, so $\tfrac{\sin x}{x} \approx 0.999983$ — already practically $1$, exactly as the proof predicts.

**Continuity at a point**

$$f \text{ continuous at } a \iff \lim_{x\to a} f(x)=f(a)$$

*Limit exists, the value $f(a)$ exists, and they match — no hole, jump, or break.* Informally, a function is **continuous** if you can draw its graph without lifting your pen. The earlier example $\tfrac{x^2-1}{x-1}$ fails this at $x=1$: the limit is $2$ but $f(1)$ does not exist — a "hole."

**Intermediate Value Theorem**

$$f \text{ continuous on } [a,b],\ N \text{ between } f(a),f(b) \implies \exists\, c\in(a,b):\ f(c)=N$$

*A continuous curve can't skip a value — it must pass through every height in between.* The notation $[a,b]$ is the closed interval from $a$ to $b$ (endpoints included); $(a,b)$ is the open interval (endpoints excluded).

**Worked example (this is why root-finding works).** Let $f(x) = x^2 - 2$, continuous everywhere. Then $f(1) = -1$ (negative) and $f(2) = 2$ (positive). Since $N = 0$ lies between $-1$ and $2$, the theorem guarantees some $c$ in $(1,2)$ with $f(c) = 0$ — i.e. $c = \sqrt{2} \approx 1.414$. The theorem promises the root *exists* without telling us its value.

> **Why this matters next**
>
> Differentiability (Section 2) requires continuity, and the derivative is itself *defined* as a limit. Section 2 is one careful application of everything above.

<a id="s2"></a>
## The definition of the derivative

*Take the slope between two points, then slide them together.*

**Words first.** The **slope** of a straight line is "rise over run" — how much the line climbs ($\Delta y$, change in output) for a given step sideways ($\Delta x$, change in input). The Greek letter $\Delta$ ("delta") means "change in." A curved graph has no single slope, but over a *tiny* stretch it looks almost straight; the **derivative** captures that local, instantaneous slope.

**Definition (limit of a difference quotient)**

$$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$$

*$\frac{f(x+h)-f(x)}{h}$ is the slope of a secant line through two nearby points; $h\to0$ tilts it into the tangent.* The symbol $f'(x)$ (read "f prime of x") is the derivative. The number $h$ is the small horizontal gap between the two input points $x$ and $x+h$. A **secant line** cuts the curve at two points; the **tangent line** touches it at one. As $h$ shrinks to $0$ the two points merge and the secant rotates into the tangent — whose slope is exactly $f'(x)$.

**Equivalent form at a point**

$$f'(a)=\lim_{x\to a}\frac{f(x)-f(a)}{x-a}$$

This says the same thing with the second point named $x$ instead of $x+h$; setting $x = a + h$ turns one form into the other.

`$f'(x)$ — Lagrange` · `$\dfrac{dy}{dx}$ — Leibniz` · `$\dot y$ — Newton` · `$D_xf$ — operator`

These are four notations for the *same* derivative, named after their inventors. $\tfrac{dy}{dx}$ is read "dee y dee x" and is meant to evoke "tiny change in $y$ over tiny change in $x$."

**Demonstration — derivative of $f(x)=x^2$ from the definition**

1. Substitute $f(x) = x^2$ into the definition (so $f(x+h) = (x+h)^2$):

   $$f'(x)=\lim_{h\to0}\frac{(x+h)^2-x^2}{h}.$$
2. Expand the top using $(x+h)^2 = x^2 + 2xh + h^2$ (multiply it out: $(x+h)(x+h)$), then cancel $x^2 - x^2$:

   $$(x+h)^2-x^2 = x^2+2xh+h^2-x^2 = 2xh+h^2.$$
3. Divide by $h$. This is allowed because inside the limit $h \neq 0$ (recall the ε–δ definition excludes the point itself, §s1):

   $$\frac{2xh+h^2}{h}=2x+h.$$
4. Let $h\to0$. By the sum and constant limit laws (§s1), $2x + h \to 2x + 0$:

   $$f'(x)=2x.$$

*Matches the power rule $nx^{n-1}$ (here $n=2$, giving $2x^{1}$). Next we prove that rule in general.*

**Worked numeric example.** The slope of $y = x^2$ at $x = 3$ is $f'(3) = 2 \times 3 = 6$. Sanity check with a small secant ($h = 0.001$): $\tfrac{(3.001)^2 - 3^2}{0.001} = \tfrac{9.006001 - 9}{0.001} = 6.001$ — right next to $6$, confirming the limit.

**Common pitfall.** You cannot find the slope by plugging $h = 0$ directly into Step 1; you get $\tfrac{0}{0}$. The cancellation in Step 3 is what makes the limit legal — this is the "honest $0/0$" idea from §s0.

<a id="s3"></a>
## The differentiation rules — each one proven

*Every rule below is derived from the limit definition. Once proven, you never touch the definition again.*

**Why we care.** Using the limit definition every time would be slow and error-prone. These rules are reusable shortcuts: prove each once from the definition (§s2), then differentiate any combination of functions by pattern-matching.

**Constant & basic rules**

$$\frac{d}{dx}[c]=0,\quad \frac{d}{dx}[cf]=cf',\quad (f\pm g)'=f'\pm g'$$

Here $c$ is a **constant** (a fixed number that does not depend on $x$); $\tfrac{d}{dx}[\cdot]$ means "the derivative with respect to $x$ of."

**Demonstration of the three basic rules.**
1. *Constant:* with $f(x) = c$, the difference quotient is $\tfrac{c - c}{h} = \tfrac{0}{h} = 0$ for every $h \neq 0$, so its limit is $0$. A flat line has slope $0$.
2. *Constant multiple:* $\lim_{h\to0}\tfrac{cf(x+h)-cf(x)}{h} = c\lim_{h\to0}\tfrac{f(x+h)-f(x)}{h} = cf'(x)$, factoring $c$ out by the constant limit law (§s1).
3. *Sum/difference:* $\lim_{h\to0}\tfrac{[f(x+h)\pm g(x+h)]-[f(x)\pm g(x)]}{h}$ splits into two separate quotients by the sum limit law (§s1), giving $f' \pm g'$.

**Power rule**

$$\frac{d}{dx}\big[x^{n}\big]=n\,x^{\,n-1}$$

In words: bring the exponent $n$ down as a multiplier, then lower the exponent by one.

**Demonstration — power rule (via the binomial theorem)**

The **binomial theorem** is the rule for expanding $(x+h)^n$; we only need its first two terms plus the fact that all the rest carry $h^2$ or higher.

1. Definition (§s2) with $f(x) = x^n$:

   $$f'(x)=\lim_{h\to0}\frac{(x+h)^n-x^n}{h}.$$
2. Binomial expansion (here $\tfrac{n(n-1)}{2}$ is the coefficient of the third term; "$\cdots$" hides terms with $h^3$ and up):

   $$(x+h)^n = x^n + n x^{n-1}h + \tfrac{n(n-1)}{2}x^{n-2}h^2+\cdots+h^n.$$
3. Subtract $x^n$; the leading $x^n$ cancels, and every surviving term has at least one factor of $h$:

   $$(x+h)^n-x^n = n x^{n-1}h + \tfrac{n(n-1)}{2}x^{n-2}h^2+\cdots$$
4. Divide by $h$ (legal since $h \neq 0$ inside the limit), lowering each term's power of $h$ by one:

   $$n x^{n-1} + \tfrac{n(n-1)}{2}x^{n-2}h + \cdots$$
5. Let $h\to0$: every term still carrying an $h$ vanishes (constant-times-$h \to 0$ by the limit laws, §s1), leaving only the first term:

   $$f'(x)=n x^{n-1}.$$

**Worked example.** $\tfrac{d}{dx}[x^5] = 5x^4$. At $x = 2$ this is $5 \times 16 = 80$.

**★ The famous, everyday derivatives you'll reach for most**

$$\frac{d}{dx}\,e^{x}=e^{x} \qquad \frac{d}{dx}\sqrt{x}=\frac{1}{2\sqrt{x}} \qquad \frac{d}{dx}\,\frac{1}{x}=-\frac{1}{x^{2}}$$

*$e^x$ is the single most famous derivative in mathematics — the only function (up to a constant multiple) that is its own derivative, which is why it governs growth, decay, and compound interest. The other two are the everyday special cases of the power rule that appear constantly.* (We prove $(e^x)' = e^x$ fully in §s4.)

**Demonstration — the two everyday cases are just the power rule**

1. Square root: a square root is a power, $\sqrt{x}=x^{1/2}$ (because $(x^{1/2})^2 = x$). Apply $nx^{n-1}$ with $n = \tfrac12$, and recall $x^{-1/2} = \tfrac{1}{\sqrt x}$:

   $$\frac{d}{dx}x^{1/2}=\tfrac{1}{2}x^{-1/2}=\frac{1}{2\sqrt{x}}.$$
2. Reciprocal: a reciprocal is a negative power, $\dfrac{1}{x}=x^{-1}$. Apply the same rule with $n = -1$, and recall $x^{-2} = \tfrac{1}{x^2}$:

   $$\frac{d}{dx}x^{-1}=-1\cdot x^{-2}=-\frac{1}{x^{2}}.$$

*The power rule works for any exponent — fractional or negative — not just whole numbers.* For instance $\tfrac{d}{dx}\sqrt{x}$ at $x = 4$ is $\tfrac{1}{2\sqrt4} = \tfrac{1}{4} = 0.25$.

**Product rule**

$$(fg)' = f'g + fg'$$

*"Derivative of first times second, plus first times derivative of second." Not $f'g'$.* (A common pitfall is to multiply the two derivatives; the demonstration shows why that is wrong.)

**Demonstration — product rule (the add-and-subtract trick)**

1. Definition (§s2) applied to the product $fg$:

   $$(fg)'=\lim_{h\to0}\frac{f(x+h)g(x+h)-f(x)g(x)}{h}.$$
2. Add and subtract $f(x+h)g(x)$ in the numerator. This changes nothing (we added $0$), but it creates a shared factor we can group:

   $$f(x+h)g(x+h)-f(x+h)g(x)+f(x+h)g(x)-f(x)g(x).$$
3. Group the first pair and the second pair, factoring out the common factor in each:

   $$f(x+h)\big[g(x+h)-g(x)\big]+g(x)\big[f(x+h)-f(x)\big].$$
4. Divide by $h$ and split the limit (sum and product limit laws, §s1):

   $$\lim_{h\to0} f(x+h)\frac{g(x+h)-g(x)}{h}+\lim_{h\to0} g(x)\frac{f(x+h)-f(x)}{h}.$$
5. As $h\to0$: $f(x+h)\to f(x)$ because differentiability forces continuity — $f(x+h)-f(x) = \tfrac{f(x+h)-f(x)}{h}\cdot h \to f'(x)\cdot 0 = 0$ — the first quotient becomes $g'$, and the second becomes $f'$:

   $$(fg)'=f g' + g f'.$$

**Worked example.** With $f = x^2,\ g = x^3$: $(fg)' = (2x)(x^3) + (x^2)(3x^2) = 2x^4 + 3x^4 = 5x^4$. Check: $fg = x^5$, whose derivative by the power rule is indeed $5x^4$.

**Quotient rule**

$$\left(\frac{f}{g}\right)'=\frac{f'g-fg'}{g^{2}}$$

*"Low d-high minus high d-low, over low squared"* (here "low" is the denominator $g$, "high" the numerator $f$, "d" means "derivative of").

**Demonstration — quotient rule (straight from the product rule)**

1. Let $Q=\dfrac{f}{g}$. Multiplying both sides by $g$ gives $f = Q\,g$.
2. Differentiate both sides with the product rule (just proven):

   $$f' = Q'g + Q g'.$$
3. Solve for $Q'$ algebraically (subtract $Qg'$, then divide by $g$):

   $$Q' = \frac{f'-Qg'}{g}.$$
4. Replace $Q$ with $f/g$ and combine over a common denominator (multiply top and bottom by $g$):

   $$Q'=\frac{f'-\frac{f}{g}g'}{g}=\frac{f'g-fg'}{g^2}.$$

*Notice the quotient rule isn't separate magic — it's the product rule, rearranged.*

**Worked example.** $\left(\tfrac{x}{x+1}\right)' = \tfrac{(1)(x+1) - (x)(1)}{(x+1)^2} = \tfrac{x+1-x}{(x+1)^2} = \tfrac{1}{(x+1)^2}$.

**Chain rule (functions inside functions)**

$$\frac{d}{dx}\,f\big(g(x)\big)=f'\big(g(x)\big)\cdot g'(x) \qquad\Big(\tfrac{dy}{dx}=\tfrac{dy}{du}\cdot\tfrac{du}{dx}\Big)$$

A **composition** $f(g(x))$ means "do $g$ first, then feed the result into $f$" — a function nested inside another, like $\sin(x^2)$.

**Demonstration — chain rule (the intuition that makes it obvious)**

Let $u = g(x)$ be the inside, and $y = f(u)$ the outside, so $y$ depends on $u$ and $u$ depends on $x$.

1. Write the change in $y$ caused by a change in $x$ as a product of ratios (multiply and divide by $\Delta u$, the change in the inside):

   $$\frac{\Delta y}{\Delta x}=\frac{\Delta y}{\Delta u}\cdot\frac{\Delta u}{\Delta x}.$$
2. As $\Delta x\to0$, the inside change $\Delta u\to0$ too (since $g$ is continuous, §s1), so both ratios become derivatives.
3. Each ratio becomes a derivative in the limit (§s2):

   $$\frac{dy}{dx}=\frac{dy}{du}\cdot\frac{du}{dx}=f'(g(x))\,g'(x).$$

*Differentiate the outer layer, keep the inside intact, multiply by the inside's derivative.* (A careful proof handles the rare case $\Delta u = 0$ separately, but the ratio picture gives the right answer and the right intuition.)

**Worked example.** For $y = (x^2 + 1)^3$: outer is $u^3$ (derivative $3u^2$), inner is $u = x^2+1$ (derivative $2x$). So $y' = 3(x^2+1)^2 \cdot 2x = 6x(x^2+1)^2$.

> **Forward link (remember these two)**
>
> Read backwards, the **product rule becomes integration by parts** and the **chain rule becomes u-substitution** — the two main integration techniques in Section 9. We'll derive both from these.

<a id="s4"></a>
## Derivatives of every standard function

*With the rules above plus a few key limits, each of these can be demonstrated.*

**Trigonometric**

$$(\sin x)'=\cos x,\quad (\cos x)'=-\sin x,\quad (\tan x)'=\sec^2 x$$

$$(\cot x)'=-\csc^2 x,\quad (\sec x)'=\sec x\tan x,\quad (\csc x)'=-\csc x\cot x$$

Reminder of the names: $\tan x = \tfrac{\sin x}{\cos x}$ (tangent), $\cot x = \tfrac{\cos x}{\sin x}$ (cotangent), $\sec x = \tfrac{1}{\cos x}$ (secant), $\csc x = \tfrac{1}{\sin x}$ (cosecant).

**Demonstration — $(\sin x)'=\cos x$**

1. Definition (§s2):

   $$(\sin x)'=\lim_{h\to0}\frac{\sin(x+h)-\sin x}{h}.$$
2. Use the angle-addition formula $\sin(x+h)=\sin x\cos h+\cos x\sin h$ (a standard trig identity):

   $$=\lim_{h\to0}\frac{\sin x\cos h+\cos x\sin h-\sin x}{h}.$$
3. Group the two $\sin x$ terms ($\sin x\cos h - \sin x = \sin x(\cos h - 1)$) and split into two limits (§s1):

   $$=\sin x\lim_{h\to0}\frac{\cos h-1}{h}+\cos x\lim_{h\to0}\frac{\sin h}{h}.$$
4. Insert the special limits from §s1 $\big(\tfrac{\cos h-1}{h}\to0,\ \tfrac{\sin h}{h}\to1\big)$:

   $$=\sin x\cdot 0 + \cos x\cdot 1 = \cos x.$$

*$\tan,\sec,\csc,\cot$ then follow by the quotient rule on $\sin/\cos$.* For example, $(\tan x)' = \left(\tfrac{\sin x}{\cos x}\right)' = \tfrac{\cos x\cos x - \sin x(-\sin x)}{\cos^2 x} = \tfrac{\cos^2 x + \sin^2 x}{\cos^2 x} = \tfrac{1}{\cos^2 x} = \sec^2 x$, using the Pythagorean identity $\sin^2 x + \cos^2 x = 1$.

**Exponential & logarithmic**

$$(e^{x})'=e^{x},\quad (a^{x})'=a^{x}\ln a,\quad (\ln x)'=\frac{1}{x},\quad (\log_a x)'=\frac{1}{x\ln a}$$

Here $a^x$ is an exponential with base $a$; $\ln x$ is the **natural logarithm** (the inverse of $e^x$, so $\ln(e^x) = x$); $\log_a x$ is the logarithm to base $a$.

**Demonstration — $(e^x)'=e^x$**

1. Definition (§s2):

   $$(e^x)'=\lim_{h\to0}\frac{e^{x+h}-e^{x}}{h}.$$
2. Factor $e^{x}$ out, using the exponent law $e^{x+h} = e^x e^h$ (so $e^{x+h} - e^x = e^x(e^h - 1)$); $e^x$ does not depend on $h$:

   $$=e^{x}\lim_{h\to0}\frac{e^{h}-1}{h}.$$
3. That remaining limit equals $1$ (a special limit from §s1 — in fact it is the very property that *defines* $e$):

   $$=e^{x}\cdot 1 = e^{x}.$$

*$e^x$ is the unique function that is its own derivative.* The base-$a$ case follows by writing $a^x = e^{x\ln a}$ and applying the chain rule (§s3): $(a^x)' = e^{x\ln a}\cdot \ln a = a^x \ln a$.

**Demonstration — $(\ln x)'=\tfrac1x$ (via inverse functions)**

An **inverse function** undoes another; $\ln$ and $e^x$ are inverses.

1. Let $y=\ln x$. By the definition of $\ln$ this means

   $$e^{y}=x.$$
2. Differentiate both sides with respect to $x$. The right side gives $1$; the left needs the chain rule (§s3) because $y$ depends on $x$:

   $$e^{y}\cdot\frac{dy}{dx}=1.$$
3. Solve for $dy/dx$ and recall $e^{y}=x$ from Step 1:

   $$\frac{dy}{dx}=\frac{1}{e^{y}}=\frac{1}{x}.$$

**Worked example.** The slope of $y = \ln x$ at $x = 2$ is $\tfrac12 = 0.5$.

**Inverse trigonometric**

$$(\arcsin x)'=\frac{1}{\sqrt{1-x^2}},\quad (\arccos x)'=-\frac{1}{\sqrt{1-x^2}},\quad (\arctan x)'=\frac{1}{1+x^2}$$

These "arc" functions are the inverses of $\sin,\cos,\tan$: $\arctan x$ returns the angle whose tangent is $x$.

**Demonstration — $(\arctan x)'=\tfrac{1}{1+x^2}$**

1. Let $y=\arctan x$, which by definition means

   $$\tan y = x.$$
2. Differentiate both sides; the left uses $(\tan y)' = \sec^2 y$ (from above) times $\tfrac{dy}{dx}$ (chain rule, §s3):

   $$\sec^2 y\cdot\frac{dy}{dx}=1 \;\Rightarrow\; \frac{dy}{dx}=\frac{1}{\sec^2 y}.$$
3. Use the identity $\sec^2 y = 1+\tan^2 y$ (divide $\sin^2 + \cos^2 = 1$ by $\cos^2$) and $\tan y = x$ from Step 1:

   $$\frac{dy}{dx}=\frac{1}{1+\tan^2 y}=\frac{1}{1+x^2}.$$

**Hyperbolic functions**

$$\sinh x=\frac{e^x-e^{-x}}{2},\quad \cosh x=\frac{e^x+e^{-x}}{2}$$

$$(\sinh x)'=\cosh x,\quad (\cosh x)'=\sinh x,\quad (\tanh x)'=\mathrm{sech}^2 x$$

The **hyperbolic sine/cosine** ($\sinh, \cosh$, pronounced "sinch, cosh") are cousins of $\sin,\cos$ built from $e^x$ instead of circles; they describe hanging cables and relativity.

**Demonstration — $(\sinh x)' = \cosh x$.** Differentiate term by term using $(e^x)' = e^x$ and $(e^{-x})' = -e^{-x}$ (chain rule, §s3):

$$(\sinh x)' = \frac{e^x - (-e^{-x})}{2} = \frac{e^x + e^{-x}}{2} = \cosh x.$$

*Defined from $e^x$; their derivatives follow in one line from $(e^x)'=e^x$. Note $(\cosh)'=+\sinh$, unlike the trig minus sign.*

> **A quiet symmetry**
>
> Differentiating $\sin$ four times returns to $\sin$ ($\sin \to \cos \to -\sin \to -\cos \to \sin$). That cycle is exactly why sine and cosine describe everything that oscillates — and it reappears in their Taylor series in Section 11.

<a id="s5"></a>
## Implicit, logarithmic & higher-order derivatives

*For when y is tangled up, the exponents are messy, or you differentiate more than once.*

**Implicit differentiation**

$$\frac{d}{dx}[y]=\frac{dy}{dx},\qquad \frac{d}{dx}\big[y^{2}\big]=2y\frac{dy}{dx}$$

**Why we care.** Sometimes $y$ is not written alone as "$y = $ something"; it is tangled into an equation like $x^2 + y^2 = 25$. **Implicit differentiation** lets us find the slope without untangling $y$ first. The trick: treat $y$ as a hidden function of $x$, so every $y$ term needs the chain rule (§s3). That is why $\tfrac{d}{dx}[y^2] = 2y\tfrac{dy}{dx}$ — the outer power rule gives $2y$, then we multiply by $\tfrac{dy}{dx}$, the derivative of the inside $y$.

**Demonstration — slope on the circle $x^2+y^2=25$**

1. Differentiate both sides. The $x^2$ term gives $2x$; the $y^2$ term needs the chain rule (giving $2y\tfrac{dy}{dx}$); the constant $25$ gives $0$ (§s3):

   $$2x+2y\frac{dy}{dx}=0.$$
2. Solve for the slope (subtract $2x$, divide by $2y$):

   $$\frac{dy}{dx}=-\frac{x}{y}.$$

**Worked example.** On this circle of radius $5$, at the point $(3, 4)$ the slope is $-\tfrac{3}{4} = -0.75$. (Geometrically: the tangent to a circle is perpendicular to the radius, and the radius to $(3,4)$ has slope $\tfrac{4}{3}$, whose perpendicular slope is indeed $-\tfrac34$ — a check that confirms the method.)

*Every $y$-term picks up a $dy/dx$ — that's the chain rule from §s3 doing the work.*

**Logarithmic differentiation**

$$y=f(x)^{g(x)} \Rightarrow \ln y=g\ln f \Rightarrow \frac{y'}{y}=\big(g\ln f\big)'$$

*Take $\ln$ first to turn an awkward power into a product.* This uses the log law $\ln(f^g) = g\ln f$, and on the left $(\ln y)' = \tfrac{y'}{y}$ by the chain rule (§s3).

**Worked example — $y = x^x$.** Take $\ln$: $\ln y = x\ln x$. Differentiate: $\tfrac{y'}{y} = (1)\ln x + x\cdot\tfrac1x = \ln x + 1$ (product rule, §s3). So $y' = x^x(\ln x + 1)$. At $x = 1$: $y' = 1^1(\ln 1 + 1) = 1(0+1) = 1$.

**Higher-order derivatives**

$$f''(x)=\frac{d}{dx}f'(x),\qquad f^{(n)}(x)=\frac{d^{\,n}y}{dx^{\,n}}$$

A **higher-order derivative** is simply the derivative of a derivative. $f''$ ("f double prime") is the second derivative; $f^{(n)}$ is the $n$-th.

**Worked example.** For $f(x) = x^4$: $f'(x) = 4x^3$, $f''(x) = 12x^2$, $f'''(x) = 24x$, $f^{(4)}(x) = 24$, and $f^{(5)}(x) = 0$.

*If $s(t)$ is position: $s'$ is velocity (how fast position changes), $s''$ is acceleration (how fast velocity changes). The second derivative also controls concavity (Section 6).*

<a id="s6"></a>
## Putting derivatives to work

*Tangent lines, curve shapes, optimization, and impossible-looking limits.*

**Tangent line at $x=a$**

$$y-f(a)=f'(a)(x-a)$$

This is the equation of the straight line touching the curve at the point $(a, f(a))$, written in point-slope form: slope $f'(a)$ through that point.

**Worked example.** For $f(x) = x^2$ at $a = 3$: $f(3) = 9$, $f'(3) = 6$, so the tangent line is $y - 9 = 6(x - 3)$, i.e. $y = 6x - 9$.

### Reading a curve from its derivatives

- $f'>0$: increasing (going uphill as $x$ grows)   $f'<0$: decreasing (downhill)
- **Critical points**: where $f'(x)=0$ or undefined — these are the candidates for a peak (max) or valley (min), because at the top of a hill the slope is momentarily flat.
- $f''>0$: concave up (shaped like a cup $\smile$)   $f''<0$: concave down (shaped like a cap $\frown$)
- **Inflection point**: where $f''$ changes sign — the curve switches from cup to cap or back.

**First & second derivative tests**

$$f'(c)=0:\quad f''(c)>0 \Rightarrow \text{local min},\qquad f''(c)<0 \Rightarrow \text{local max}$$

Intuition: at a flat spot ($f'(c) = 0$), if the curve is cupped up ($f'' > 0$) you sit at the bottom of the cup — a minimum; if capped down ($f'' < 0$) you sit at the top — a maximum.

**Worked optimization example.** Maximize the area of a rectangle with perimeter $20$. If width $= x$, height $= 10 - x$, area $A(x) = x(10-x) = 10x - x^2$. Then $A'(x) = 10 - 2x = 0$ gives $x = 5$. Since $A''(x) = -2 < 0$, this is a maximum. The best rectangle is the $5 \times 5$ square, area $25$.

**Mean Value Theorem (and Rolle's case)**

$$\exists\,c\in(a,b):\ f'(c)=\frac{f(b)-f(a)}{b-a}$$

*Somewhere the instantaneous slope equals the average slope.* The right side is the average rate of change over $[a,b]$ (total rise over total run); the theorem guarantees at least one interior point $c$ where the tangent is parallel to that average. **Rolle's theorem** is the special case $f(a)=f(b)$, where the average slope is $0$, giving a flat tangent $f'(c)=0$.

**Worked example.** On $f(x) = x^2$ over $[0, 4]$: average slope $= \tfrac{16 - 0}{4 - 0} = 4$. Setting $f'(c) = 2c = 4$ gives $c = 2$, which lies in $(0,4)$ as promised.

**L'Hôpital's rule (for $0/0$ or $\infty/\infty$)**

$$\lim_{x\to a}\frac{f(x)}{g(x)}=\lim_{x\to a}\frac{f'(x)}{g'(x)}$$

An **indeterminate form** like $\tfrac00$ or $\tfrac\infty\infty$ is one where naive substitution gives no answer. This rule says: differentiate top and bottom separately and try again.

**Demonstration — why it works (the local-linear picture)**

1. Near $x=a$ with $f(a)=g(a)=0$, replace each function by its tangent line (§s6, linear approximation below):

   $$f(x)\approx f'(a)(x-a),\qquad g(x)\approx g'(a)(x-a).$$
2. Form the ratio; the common factor $(x-a)$ cancels:

   $$\frac{f(x)}{g(x)}\approx\frac{f'(a)(x-a)}{g'(a)(x-a)}=\frac{f'(a)}{g'(a)}.$$

*An indeterminate ratio is governed by the ratio of slopes. A neat loop back to §s1.*

**Worked example.** $\lim_{x\to0}\tfrac{\sin x}{x}$ is $\tfrac00$. By L'Hôpital, $= \lim_{x\to0}\tfrac{\cos x}{1} = \cos 0 = 1$ — matching the special limit we proved geometrically in §s1.

**Linear approximation & differentials**

$$f(x)\approx f(a)+f'(a)(x-a),\qquad dy=f'(x)\,dx$$

*Near a point, every smooth curve looks like its tangent line.* The term $dy = f'(x)\,dx$ is the **differential**: a tiny output change $dy$ equals the slope times a tiny input change $dx$.

**Worked example.** Estimate $\sqrt{4.1}$. Use $f(x) = \sqrt x$ at $a = 4$: $f(4) = 2$, $f'(4) = \tfrac{1}{2\sqrt4} = 0.25$. So $\sqrt{4.1} \approx 2 + 0.25(0.1) = 2.025$. (True value $\approx 2.0248$ — excellent for one step.)

*Extended to infinitely many derivatives, this becomes the Taylor series in Section 11.*

<a id="s7"></a>
## The antiderivative & the Fundamental Theorem

*The hinge of the entire subject: derivative and integral are revealed to be opposites.*

**Indefinite integral (antiderivative)**

$$\int f(x)\,dx=F(x)+C \quad\text{where}\quad F'(x)=f(x)$$

**Words first.** An **antiderivative** $F$ of $f$ is a function whose derivative is $f$ — it answers "what did I differentiate to get this?" The elongated-S symbol $\int$ is the **integral sign** (a stretched "S" for "sum"); $dx$ marks the variable; $C$ is the **constant of integration**.

*"What function has THIS as its derivative?" The $+C$ appears because constants vanish when differentiated* (recall $\tfrac{d}{dx}[c] = 0$, §s3), so the antiderivative is only pinned down up to an added constant.

**Worked example.** $\int 2x\,dx = x^2 + C$, because $\tfrac{d}{dx}[x^2 + C] = 2x$. We could equally write $x^2 + 7$; both are valid antiderivatives.

**Definite integral as a limit of Riemann sums**

$$\int_{a}^{b} f(x)\,dx=\lim_{n\to\infty}\sum_{i=1}^{n} f(x_i^{*})\,\Delta x,\qquad \Delta x=\frac{b-a}{n}$$

**Words first.** A **definite integral** computes the exact area under the curve $f$ between $x=a$ and $x=b$. The capital sigma $\sum$ means "add up"; $n$ is the number of thin rectangles; $\Delta x = \tfrac{b-a}{n}$ is each rectangle's width; $x_i^*$ is a sample point in the $i$-th rectangle, so $f(x_i^*)$ is its height. The sum of rectangle areas is a **Riemann sum**; letting $n \to \infty$ makes the rectangles infinitely thin and the sum exact.

*Slice the area into n thin rectangles, add them, let the slices vanish. The integral IS an infinite sum — the same "push to a limit" that built the derivative.*

**Worked example.** Estimate $\int_0^2 x\,dx$ with $n = 4$ rectangles ($\Delta x = 0.5$), using right endpoints $x_i^* = 0.5, 1, 1.5, 2$: sum $= (0.5+1+1.5+2)(0.5) = 5 \times 0.5 = 2.5$. The exact area is the triangle $\tfrac12(2)(2) = 2$; with more rectangles the estimate converges to $2$.

### The Fundamental Theorem of Calculus

**Part 1 — differentiation undoes integration**

$$\frac{d}{dx}\int_{a}^{x} f(t)\,dt=f(x)$$

The variable inside is renamed $t$ to avoid clashing with the upper limit $x$; the integral is a function *of* $x$ (its upper limit), and its derivative returns the original $f$.

**Part 2 — integrals are evaluated by antiderivatives**

$$\int_{a}^{b} f(x)\,dx=F(b)-F(a),\quad F'=f$$

This is the practical payoff: to get an area, find any antiderivative $F$ and subtract its values at the endpoints.

**Demonstration — why Part 1 is true (the thin-strip argument)**

1. Define the running-area function (area from $a$ up to a moving right edge $x$):

   $$A(x)=\int_a^x f(t)\,dt.$$
2. Increasing $x$ by a tiny $h$ adds a thin strip of width $h$ and height $\approx f(x)$, so its area is approximately base times height:

   $$A(x+h)-A(x)\approx f(x)\cdot h.$$
3. Divide by $h$:

   $$\frac{A(x+h)-A(x)}{h}\approx f(x).$$
4. Let $h\to0$. The left side is exactly the definition of $A'(x)$ (§s2), and the approximation becomes exact:

   $$A'(x)=f(x).$$

*So the area function's derivative is the original function — accumulation and rate are inverse operations. Part 2 follows because any two antiderivatives differ by a constant* (their difference has derivative $0$, hence is constant, §s6 via the Mean Value Theorem), so $A(x) = F(x) - F(a)$, and at $x = b$ this gives $\int_a^b f = F(b) - F(a)$.

**Worked example (Part 2).** $\int_0^2 x\,dx$: an antiderivative of $x$ is $F(x) = \tfrac{x^2}{2}$, so the area is $F(2) - F(0) = \tfrac{4}{2} - 0 = 2$ — confirming the limit computation above, with no adding required.

> **The payoff**
>
> To find an area (an infinite sum), you don't add anything — you find an antiderivative and subtract two values. This is why the entire integral table in Section 8 is just the derivative tables of Sections 3–4 read backwards.

<a id="s8"></a>
## The basic integral table

*Each line is a derivative rule reversed — verify any of them by differentiating the right-hand side.*

**Power rule for integrals**

$$\int x^{n}\,dx=\frac{x^{\,n+1}}{n+1}+C \quad(n\neq-1)$$

This is the power rule (§s3) run backwards: to undo "lower the exponent," we *raise* it by one and divide by the new exponent. The condition $n \neq -1$ avoids dividing by $n + 1 = 0$.

*Check: differentiate $\frac{x^{n+1}}{n+1}$ and the power rule gives back $x^n$.* Worked: $\int x^3\,dx = \tfrac{x^4}{4} + C$, and indeed $\tfrac{d}{dx}\tfrac{x^4}{4} = \tfrac{4x^3}{4} = x^3$.

**The $n=-1$ exception**

$$\int \frac{1}{x}\,dx=\ln|x|+C$$

The forbidden case $n = -1$ is rescued by recalling $(\ln x)' = \tfrac1x$ (§s4); the absolute value $|x|$ extends it to negative $x$.

The table below lists each standard integral beside the derivative rule it reverses. To verify any row, differentiate the middle column and confirm you recover the integrand on the left.

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

**Worked check of one row.** $\int \cos x\,dx = \sin x + C$, because $(\sin x)' = \cos x$ (§s4). Every row is verified the same way: differentiate the result, recover the integrand.

### Three integrals that need a small trick

These three are not direct reversals of a memorized derivative; each needs a single clever move, shown in §s9.

| Integral | Result | How |
| --- | --- | --- |
| $\int \tan x\,dx$ | $\ln\vert \sec x\vert +C$ | u-sub with $u=\cos x$ |
| $\int \ln x\,dx$ | $x\ln x-x+C$ | by parts (see §9) |
| $\int \sec x\,dx$ | $\ln\vert \sec x+\tan x\vert +C$ | multiply by a clever 1 |

**Worked check.** $\tfrac{d}{dx}(x\ln x - x) = (1\cdot\ln x + x\cdot\tfrac1x) - 1 = \ln x + 1 - 1 = \ln x$ (product rule, §s3), confirming $\int \ln x\,dx = x\ln x - x + C$.

> How to use this section
>
> Don't memorize this table separately. If you know the derivative tables in Sections 3–4, you already know this — just flip the arrow. That is the Fundamental Theorem in action.

<a id="s9"></a>
## Integration techniques — each one proven

*When an integral doesn't match the table, reshape it until it does. Two of these are differentiation rules in reverse, and we derive them that way.*

**u-substitution**

$$\int f\big(g(x)\big)g'(x)\,dx=\int f(u)\,du,\qquad u=g(x)$$

**Idea.** When you spot an inner function $g(x)$ alongside its derivative $g'(x)$, rename $u = g(x)$ to collapse the integral into a simple table form.

**Demonstration — u-sub is the chain rule, reversed**

1. Let $F$ be an antiderivative of $f$, so $F'=f$. By the chain rule (§s3):

   $$\frac{d}{dx}F\big(g(x)\big)=F'\big(g(x)\big)g'(x)=f\big(g(x)\big)g'(x).$$
2. Integrate both sides (integration undoes the derivative, §s7):

   $$\int f\big(g(x)\big)g'(x)\,dx=F\big(g(x)\big)+C.$$
3. That right side is exactly $\int f(u)\,du$ with $u=g(x)$, since $\int f(u)\,du = F(u) + C = F(g(x)) + C$.

**Worked example.** $\int 2x\,e^{x^2}\,dx$. Let $u = x^2$, so $du = 2x\,dx$. The integral becomes $\int e^u\,du = e^u + C = e^{x^2} + C$. Check: $(e^{x^2})' = e^{x^2}\cdot 2x$ (chain rule), the original integrand.

**Integration by parts**

$$\int u\,dv=uv-\int v\,du$$

**Idea.** For a *product* of two functions where one gets simpler when differentiated (like $\ln x$ or a polynomial), trade the hard integral for an easier one.

**Demonstration — by parts is the product rule, reversed**

1. Start from the product rule (§s3):

   $$(uv)'=u'v+uv'.$$
2. Integrate both sides over $x$ (the integral of $(uv)'$ is just $uv$, §s7):

   $$uv=\int u'v\,dx+\int uv'\,dx.$$
3. Solve for one of the integrals by subtracting $\int u'v\,dx$ from both sides. Writing $dv = v'\,dx$ and $du = u'\,dx$, this is $\displaystyle\int u\,dv=uv-\int v\,du$:

   $$\int uv'\,dx=uv-\int u'v\,dx.$$

*Use it on products like $\int x e^{x}\,dx$ or $\int \ln x\,dx$ (take $u=\ln x,\ dv=dx$).*

**Worked example — $\int x e^x\,dx$.** Choose $u = x$ (so $du = dx$) and $dv = e^x\,dx$ (so $v = e^x$). Then $\int x e^x\,dx = x e^x - \int e^x\,dx = x e^x - e^x + C$. Check: $(xe^x - e^x)' = (e^x + xe^x) - e^x = xe^x$.

**Demonstration — the $\int \sec x\,dx$ trick (the three table entries from §s8)**

The three "small-trick" integrals promised in §s8 are settled here. $\int \ln x\,dx = x\ln x - x + C$ is by parts (take $u=\ln x,\ dv=dx$, just above); $\int \tan x\,dx = \int \tfrac{\sin x}{\cos x}\,dx$ is u-sub with $u=\cos x$, $du=-\sin x\,dx$, giving $-\ln|u| + C = \ln|\sec x| + C$. The genuinely clever one is $\int \sec x\,dx$:

1. Multiply by a disguised $1$, namely $\dfrac{\sec x + \tan x}{\sec x + \tan x}$:

   $$\int \sec x\,dx = \int \sec x\cdot\frac{\sec x + \tan x}{\sec x + \tan x}\,dx = \int \frac{\sec^2 x + \sec x\tan x}{\sec x + \tan x}\,dx.$$
2. Notice the numerator is exactly the derivative of the denominator: $(\sec x + \tan x)' = \sec x\tan x + \sec^2 x$ (from §s4). So with $u = \sec x + \tan x$ we have $du = (\sec^2 x + \sec x\tan x)\,dx$, and the integral is $\int \tfrac{du}{u}$:

   $$\int \frac{du}{u} = \ln|u| + C = \ln|\sec x + \tan x| + C.$$

**Trigonometric substitution**

$$\sqrt{a^2-x^2}\!: x=a\sin\theta,\quad \sqrt{a^2+x^2}\!: x=a\tan\theta,\quad \sqrt{x^2-a^2}\!: x=a\sec\theta$$

*Trade an awkward square root for a clean trig identity.* For example, with $x = a\sin\theta$, the identity $1 - \sin^2\theta = \cos^2\theta$ turns $\sqrt{a^2 - x^2} = \sqrt{a^2 - a^2\sin^2\theta} = a\cos\theta$, eliminating the root.

**Worked sketch.** $\int \tfrac{dx}{\sqrt{1 - x^2}}$ with $x = \sin\theta$, $dx = \cos\theta\,d\theta$, becomes $\int \tfrac{\cos\theta}{\cos\theta}\,d\theta = \int d\theta = \theta + C = \arcsin x + C$ — recovering the table entry of §s8.

**Partial fractions**

$$\frac{P(x)}{(x-r_1)(x-r_2)}=\frac{A}{x-r_1}+\frac{B}{x-r_2}$$

*Break a rational function into simple pieces, each integrating to a log or arctangent.* Here $P(x)$ is a polynomial of lower degree than the bottom; $r_1, r_2$ are the roots of the denominator; $A, B$ are constants found by matching.

**Worked example.** $\tfrac{1}{(x-1)(x+1)} = \tfrac{A}{x-1} + \tfrac{B}{x+1}$. Multiplying out: $1 = A(x+1) + B(x-1)$. Set $x = 1$: $1 = 2A$, so $A = \tfrac12$. Set $x = -1$: $1 = -2B$, so $B = -\tfrac12$. Then $\int \tfrac{dx}{(x-1)(x+1)} = \tfrac12\ln|x-1| - \tfrac12\ln|x+1| + C$.

**Improper integrals**

$$\int_{a}^{\infty} f(x)\,dx=\lim_{t\to\infty}\int_{a}^{t} f(x)\,dx$$

*Infinite bounds (or vertical asymptotes) are handled as a limit; the integral "converges" if that limit is finite.*

**Worked example.** $\int_1^\infty \tfrac{1}{x^2}\,dx = \lim_{t\to\infty}\left[-\tfrac1x\right]_1^t = \lim_{t\to\infty}\left(-\tfrac1t + 1\right) = 0 + 1 = 1$. A region of infinite length but finite area $1$.

### Properties of definite integrals

$$\int_a^b f=-\int_b^a f,\qquad \int_a^a f=0,\qquad \int_a^b f=\int_a^c f+\int_c^b f$$

In words: reversing the limits flips the sign; a zero-width interval has zero area; and an integral can be split at any interior point $c$ and the pieces added. Each follows directly from the Riemann-sum definition (§s7) and Part 2 of the FTC.

> **The mirror, made explicit**
>
> Chain rule ⟷ u-substitution. Product rule ⟷ integration by parts. Differentiation has clean rules that always work; integration is the reverse search, so it needs clever moves. Same relationships, harder direction.

<a id="s10"></a>
## Putting integrals to work

*Anything that accumulates — area, volume, length, average — is an integral.*

The recipe is always the same: describe one infinitely thin slice of the quantity, then integrate (sum) the slices from $a$ to $b$ (the Riemann idea, §s7).

**Area between two curves**

$$A=\int_a^b\big[f(x)-g(x)\big]\,dx$$

A thin vertical strip at position $x$ has height $f(x) - g(x)$ (top curve minus bottom) and width $dx$; integrate to total the area.

**Worked example.** Area between $f(x) = x$ and $g(x) = x^2$ from $0$ to $1$: $\int_0^1 (x - x^2)\,dx = \left[\tfrac{x^2}{2} - \tfrac{x^3}{3}\right]_0^1 = \tfrac12 - \tfrac13 = \tfrac16$.

**Volume of revolution — disk method**

$$V=\pi\int_a^b\big[f(x)\big]^2\,dx$$

Spin the curve around the $x$-axis; each thin slice is a disk of radius $f(x)$, area $\pi[f(x)]^2$, thickness $dx$.

**Worked example.** Spin $f(x) = x$ from $0$ to $1$ (a cone): $V = \pi\int_0^1 x^2\,dx = \pi\left[\tfrac{x^3}{3}\right]_0^1 = \tfrac{\pi}{3}$, matching the cone-volume formula $\tfrac13\pi r^2 h$ with $r = h = 1$.

**Volume of revolution — shell method**

$$V=2\pi\int_a^b x\,f(x)\,dx$$

An alternative: each thin cylindrical shell has radius $x$, height $f(x)$, thickness $dx$, so its volume is (circumference $2\pi x$) × (height $f(x)$) × $dx$.

**Arc length**

$$L=\int_a^b\sqrt{1+\big[f'(x)\big]^2}\;dx$$

**Average value of a function**

$$\bar f=\frac{1}{b-a}\int_a^b f(x)\,dx$$

The average height of the curve over $[a,b]$: total area divided by width. **Worked example.** Average of $f(x) = x^2$ on $[0,3]$ is $\tfrac{1}{3}\int_0^3 x^2\,dx = \tfrac13\cdot\tfrac{27}{3} = \tfrac13\cdot 9 = 3$.

**Demonstration — where the arc-length formula comes from**

1. Approximate the curve by tiny straight segments. Each has horizontal run $dx$ and vertical rise $dy$.
2. By the Pythagorean theorem (the length of a right triangle's hypotenuse), the segment length is

   $$ds=\sqrt{dx^2+dy^2}.$$
3. Factor $dx$ out of the root (so $\sqrt{dx^2 + dy^2} = \sqrt{1 + (dy/dx)^2}\,dx$) and use $\frac{dy}{dx}=f'(x)$ (§s2):

   $$ds=\sqrt{1+\big(\tfrac{dy}{dx}\big)^2}\,dx=\sqrt{1+[f'(x)]^2}\,dx.$$
4. Integrate (add up) all the tiny lengths from $a$ to $b$:

   $$L=\int_a^b\sqrt{1+[f'(x)]^2}\,dx.$$

*Every formula here uses the same recipe: write one tiny slice, then integrate to sum infinitely many — the Riemann idea from §s7.*

<a id="s11"></a>
## Sequences & series

*Adding infinitely many terms — when the total is finite, we can rebuild functions from their derivatives.*

**Words first.** A **sequence** is an ordered list of numbers $a_1, a_2, a_3, \dots$. A **series** is what you get by adding them up: $a_1 + a_2 + a_3 + \cdots$. Surprisingly, adding *infinitely* many terms can give a *finite* total — that is what "converges" means. The **factorial** $n! = 1\cdot 2\cdots n$ (e.g. $4! = 24$) appears throughout.

**Geometric series**

$$\sum_{n=0}^{\infty} a r^{n}=\frac{a}{1-r}\quad(|r|<1)$$

A **geometric series** multiplies by the same ratio $r$ each step: $a, ar, ar^2, \dots$. It converges (to a finite sum) exactly when $|r| < 1$, so the terms shrink.

**Demonstration — the geometric sum formula**

1. Write the partial sum (the first $n$ terms):

   $$S_n=a+ar+ar^2+\cdots+ar^{n-1}.$$
2. Multiply every term by $r$:

   $$rS_n=ar+ar^2+\cdots+ar^{n}.$$
3. Subtract the second line from the first — every middle term cancels, leaving only the ends:

   $$S_n-rS_n=a-ar^{n}\;\Rightarrow\; S_n=\frac{a(1-r^{n})}{1-r}.$$
   (We factored $S_n(1 - r) = a(1 - r^n)$ and divided by $1 - r$.)
4. If $|r|<1$, then $r^{n}\to0$ as $n\to\infty$ (a shrinking number raised to higher powers vanishes), so $S_n \to \tfrac{a(1-0)}{1-r}$:

   $$S=\frac{a}{1-r}.$$

**Worked example.** $\tfrac12 + \tfrac14 + \tfrac18 + \cdots$ has $a = \tfrac12$, $r = \tfrac12$, sum $= \tfrac{1/2}{1 - 1/2} = \tfrac{1/2}{1/2} = 1$. (Half the room, then half what remains, forever — you fill the whole room.)

**p-series**

$$\sum_{n=1}^{\infty}\frac{1}{n^{p}}\ \text{converges} \iff p>1$$

A **p-series** adds reciprocal powers. It converges only when the exponent $p > 1$. The boundary case $p = 1$ (the **harmonic series** $1 + \tfrac12 + \tfrac13 + \cdots$) *diverges* — its sum grows without bound, even though the terms shrink to $0$. This warns us that shrinking terms are necessary but not sufficient for convergence.

### The full toolkit of convergence tests

These tests answer "does this series add up to something finite?" Choose whichever matches the series' shape.

| Test | Statement |
| --- | --- |
| nth-term (divergence) | If $\lim a_n\neq 0$, the series diverges |
| Ratio test | $\lim\left\vert \frac{a_{n+1}}{a_n}\right\vert =L$; converges if $L<1$, diverges if $L>1$ |
| Root test | $\lim \vert a_n\vert ^{1/n}=L$; converges if $L<1$ |
| Comparison | Bound $a_n$ above/below by a known convergent/divergent series |
| Limit comparison | If $\lim \frac{a_n}{b_n}$ is finite & positive, both behave the same way |
| Integral test | $\sum a_n$ and $\int_1^\infty f\,dx$ converge or diverge together |
| Alternating series | $\sum(-1)^n b_n$ converges if $b_n$ decreases to $0$ |

**Worked example (ratio test).** For $\sum \tfrac{1}{n!}$: $\left|\tfrac{a_{n+1}}{a_n}\right| = \tfrac{n!}{(n+1)!} = \tfrac{1}{n+1} \to 0 = L < 1$, so the series converges. (It converges to $e$ — see below.)

**Taylor series — a function rebuilt from its derivatives**

$$f(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^{n}$$

A **Taylor series** rebuilds a function as an infinite polynomial, using its derivatives at one point $a$. Here $f^{(n)}(a)$ is the $n$-th derivative at $a$ (§s5).

*Maclaurin series is the case $a=0$. It is linear approximation (§s6) continued to infinitely many derivatives.*

**Demonstration — why the coefficients are $f^{(n)}(a)/n!$**

1. Suppose $f(x)=c_0+c_1(x-a)+c_2(x-a)^2+\cdots$. Set $x=a$: every term with $(x-a)$ becomes $0$, leaving $c_0=f(a)$.
2. Differentiate once (power rule term by term, §s3), then set $x=a$: only the former linear term survives as the new constant $c_1$, giving $c_1=f'(a)$.
3. Differentiate $n$ times: the $(x-a)^n$ term becomes the constant $n!\,c_n$ (each differentiation peels off one factor: $n, n-1, \dots, 1$) and all other terms vanish at $x=a$:

   $$f^{(n)}(a)=n!\,c_n \;\Rightarrow\; c_n=\frac{f^{(n)}(a)}{n!}.$$

### The famous expansions

These are Maclaurin series ($a = 0$); each is obtained by plugging the function's derivatives at $0$ into the formula above.

$$e^{x}=\sum_{n=0}^{\infty}\frac{x^{n}}{n!}=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots$$

(Here every derivative of $e^x$ is $e^x$, equal to $1$ at $x = 0$, §s4, so every coefficient is $\tfrac{1}{n!}$.)

$$\sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots,\qquad \cos x=1-\frac{x^2}{2!}+\frac{x^4}{4!}-\cdots$$

$$\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}-\cdots,\qquad \frac{1}{1-x}=\sum_{n=0}^{\infty}x^n\ (|x|<1)$$

**Worked example.** Estimate $e^{0.1}$ from the first three terms: $1 + 0.1 + \tfrac{0.01}{2} = 1.105$. True value $\approx 1.10517$ — close already, and adding more terms improves it.

> **A glimpse of the unity**
>
> Put $x=i\theta$ into the $e^x$ series and regroup using the $\sin$ and $\cos$ series: you land on Euler's formula $e^{i\theta}=\cos\theta+i\sin\theta$ (where $i$ is the imaginary unit, $i^2 = -1$). The series built from derivatives quietly tie exponentials to oscillation.

<a id="s12"></a>
## A peek at multivariable calculus

*The same two ideas — slope and accumulation — in more than one dimension.*

So far functions took one input. **Multivariable calculus** studies functions of several inputs, like $f(x, y)$ — a surface (a landscape of hills) rather than a curve.

**Partial derivative**

$$\frac{\partial f}{\partial x}=\lim_{h\to0}\frac{f(x+h,\,y)-f(x,\,y)}{h}$$

The curly $\partial$ ("partial dee") signals we differentiate with respect to one variable while *holding the others constant*. It is the §s2 definition with $y$ frozen — the slope as you walk in the $x$-direction only.

*Differentiate with respect to one variable while holding the others constant — the §s2 definition, with $y$ frozen.*

**Worked example.** For $f(x,y) = x^2 y + y^3$: treating $y$ as a constant, $\tfrac{\partial f}{\partial x} = 2xy$; treating $x$ as a constant, $\tfrac{\partial f}{\partial y} = x^2 + 3y^2$.

**Gradient (vector of all partials)**

$$\nabla f=\left\langle \frac{\partial f}{\partial x},\ \frac{\partial f}{\partial y},\ \frac{\partial f}{\partial z}\right\rangle$$

The **gradient** $\nabla f$ ("del f") collects all partial derivatives into a single arrow (a **vector**). *Points in the direction of steepest increase — the multivariable cousin of the derivative.* On a hill, it points straight uphill, and its length is the steepness.

**Worked example.** For $f(x,y) = x^2 + y^2$ at $(1, 2)$: $\nabla f = \langle 2x, 2y\rangle = \langle 2, 4\rangle$ — pointing away from the origin, the steepest-uphill direction on this bowl.

**Multivariable chain rule**

$$\frac{df}{dt}=\frac{\partial f}{\partial x}\frac{dx}{dt}+\frac{\partial f}{\partial y}\frac{dy}{dt}$$

If $x$ and $y$ both depend on time $t$, the total rate of change of $f$ adds up the contributions through each variable — the §s3 chain rule, summed over every path of influence.

**Double integral (accumulation over a region)**

$$\iint_{R} f(x,y)\,dA=\int_{c}^{d}\!\int_{a}^{b} f(x,y)\,dx\,dy$$

A **double integral** sums a quantity over a two-dimensional region $R$; $dA$ is a tiny patch of area. *Volume under a surface — the Riemann idea again, stacking tiny boxes instead of rectangles.* We compute it as an inner integral (over $x$) wrapped in an outer one (over $y$).

**Worked example.** $\int_0^1\!\int_0^1 (x + y)\,dx\,dy$. Inner: $\int_0^1 (x+y)\,dx = \left[\tfrac{x^2}{2} + xy\right]_0^1 = \tfrac12 + y$. Outer: $\int_0^1 (\tfrac12 + y)\,dy = \tfrac12 + \tfrac12 = 1$.

> **Where it all leads**
>
> From here the path runs to the great integral theorems (Green's, Stokes', Divergence) — each a higher-dimensional Fundamental Theorem, saying again that behavior on a boundary is governed by behavior inside.

---

*Read once for the shape, then return to any box as a reference. The habit that makes calculus click: whenever you meet a new formula, ask which earlier one it is secretly a version of — and try to reproduce its demonstration from memory. Almost everything here is built from limits, the product rule, and the chain rule.*
