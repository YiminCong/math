**English** · [中文](complete-guide.zh.md)

# Calculus, *complete.*

A full single-variable course — every concept, principle, formula, and the demonstrations behind them — laid out basics → advanced, written so that a reader with **no mathematical background** can follow every single step. The chapter flow follows Adrian Banner's *The Calculus Lifesaver* (the Princeton review-course book), so it doubles as a companion to it.

[← Back to all guides](../README.md)

## Part A · Foundations

<a id="s0"></a>
### The big picture

**What this section says and why we care.** Calculus is the mathematics of *change* and *accumulation*. Before any formulas, it helps to know the destination. This section names the two central questions of the whole subject and the single trick that answers both. Everything later is detail hung on this frame.

**Two questions about change.** All of single-variable calculus answers two questions, plus a discovery that they are opposites.

- **The derivative** — how fast is something changing *right now*? (slope of a graph, speed of a car, rate of growth)
- **The integral** — how much has accumulated *in total*? (area under a graph, total distance travelled, a running sum)

Let us define the words we just used, since we promised to assume nothing.

- A **graph** is a picture: for each input number we plot a point whose height is the output number. The collection of all such points is a curve.
- The **slope** of a straight line is how much the height goes up for each step of one unit to the right. A road that rises 3 metres for every 100 metres travelled has slope $3/100$.
- **Area** is the amount of flat space a region covers, measured in unit squares.

> **Principle — the one idea under everything**
>
> Both the derivative and the integral are built by taking a familiar quantity (a slope between two points; the area of a rectangle) and pushing it to a **limit**: we let a small gap shrink toward zero and watch what number the result heads for. Master limits and the rest is bookkeeping.

#### Why a limit is needed (intuition)

The slope formula needs *two* points. But "how fast right now" is about a *single* instant — one point. The resolution: take two points very close together, compute the ordinary slope, then slide them together and see what value the slope approaches. That "approaches" is the limit. The same move builds area: chop a curved region into many thin rectangles whose areas we *can* add, then let the rectangles become infinitely thin.

#### Worked taste of the idea

Suppose a ball's height after $t$ seconds is $t^2$ metres. Its average speed between $t=1$ and $t=1.1$ is the change in height divided by the change in time: $\frac{1.1^2-1^2}{1.1-1}=\frac{1.21-1}{0.1}=\frac{0.21}{0.1}=2.1$ metres per second. Between $t=1$ and $t=1.01$ it is $\frac{1.01^2-1}{0.01}=\frac{0.0201}{0.01}=2.01$. The numbers head toward $2$. As we will prove in §s6, the *instantaneous* speed at $t=1$ is exactly $2$. That heading-toward-$2$ is a limit in action.

#### The whole course on one line

> Foundations → Limits → Derivatives → Integrals ↔ (FTC) → Series → Further topics

Read it as: we first build foundations, then limits; limits build derivatives and integrals; the **Fundamental Theorem of Calculus (FTC)** reveals those two are inverse operations; series let us rebuild functions from derivatives; and further topics extend the reach.

<a id="s1"></a>
### Functions, graphs & lines

**What this section says and why we care.** Calculus studies functions, so we must first nail down what a function is, how to picture it, and the simplest one of all — a straight line — because the slope of a line is the seed from which the derivative grows.

> **Concept — a function**
>
> A **function** is a rule that assigns to each input **exactly one** output. The **domain** is the set of all legal inputs; the **range** is the set of all outputs that actually come out. The **vertical line test** says: a graph represents a function only if no vertical line crosses it more than once (because one input may not have two outputs).

Let us define every term.

- **Input / output:** we feed a number in (the input, often called $x$) and a number comes out (the output, often called $y$ or $f(x)$). The notation $f(x)$ is read "$f$ of $x$" and means "the output of rule $f$ when the input is $x$."
- **Set:** simply a collection of numbers.
- A **vertical line** is a perfectly up-and-down line; every point on it shares the same input $x$. If such a line hit the graph twice, that single input would have two outputs — forbidden.

**Worked example (function or not).** Let $f(x)=x^2$. Input $3$ gives output $9$; input $-3$ also gives $9$. That is fine: two inputs sharing one output is allowed. What is *not* allowed is one input giving two outputs. The sideways parabola $x=y^2$ fails the vertical line test (input $x=4$ would give both $y=2$ and $y=-2$), so it is not a function of $x$.

#### Lines — the three forms

A straight line is fully described once we know how steep it is and where it sits. The three standard forms are:

$$\text{slope } m=\frac{y_2-y_1}{x_2-x_1},\quad y-y_1=m(x-x_1),\quad y=mx+b$$

Definitions of every symbol:

- $(x_1,y_1)$ and $(x_2,y_2)$ are two known points on the line.
- $m$ is the **slope** — "rise over run," the change in height $y_2-y_1$ divided by the change in horizontal position $x_2-x_1$.
- The middle equation is **point-slope form**: it says that starting from the known point $(x_1,y_1)$, the height changes by $m$ for every unit of horizontal change.
- $b$ in $y=mx+b$ is the **$y$-intercept**: the height where the line crosses the vertical axis (the value of $y$ when $x=0$).

**Worked example.** Through the points $(1,2)$ and $(3,8)$: slope $m=\frac{8-2}{3-1}=\frac{6}{2}=3$. Point-slope from $(1,2)$: $y-2=3(x-1)$. Multiply out: $y-2=3x-3$, so $y=3x-1$. Here the intercept is $b=-1$. Check: at $x=3$, $y=3(3)-1=8$. Correct.

*The slope is the prototype of the derivative: rise over run. Calculus generalizes "rise over run" from straight lines to curved graphs by using the limit of §s0.*

> **Concept — inverse functions**
>
> An **inverse** of $f$, written $f^{-1}$, undoes $f$: if $f(a)=b$ then $f^{-1}(b)=a$. A function has an inverse only if it is **one-to-one**, meaning different inputs always give different outputs (it passes the **horizontal line test**: no horizontal line meets the graph twice). To find the inverse, swap $x$ and $y$ and solve for $y$. Geometrically, the graph of $f^{-1}$ is the mirror image of $f$ across the line $y=x$.

Caution: $f^{-1}$ does **not** mean $1/f$; the $-1$ here marks "the undoing rule," not a reciprocal.

**Worked example.** Let $f(x)=2x+1$. Swap to get $x=2y+1$. Solve: $x-1=2y$, so $y=\frac{x-1}{2}$. Thus $f^{-1}(x)=\frac{x-1}{2}$. Check: $f(3)=7$ and $f^{-1}(7)=\frac{7-1}{2}=3$. The undoing works.

#### Composition & symmetry

To **compose** functions is to feed the output of one into another:

$$(f\circ g)(x)=f\big(g(x)\big)$$

This is read "$f$ after $g$": first apply $g$ to $x$, then apply $f$ to the result. Order matters.

**Worked example.** With $f(x)=x^2$ and $g(x)=x+3$: $(f\circ g)(2)=f(g(2))=f(5)=25$, whereas $(g\circ f)(2)=g(f(2))=g(4)=7$. Different — composition is not commutative.

An **even** function satisfies $f(-x)=f(x)$; its graph is symmetric across the $y$-axis (mirror left-right). Examples: $x^2$ and $\cos x$. An **odd** function satisfies $f(-x)=-f(x)$; its graph is symmetric through the origin (a half-turn maps it onto itself). Examples: $x^3$ and $\sin x$. Check for $x^2$: $(-x)^2=x^2$, even. For $x^3$: $(-x)^3=-x^3$, odd.

<a id="s2"></a>
### Trigonometry review

**What this section says and why we care.** Trigonometric ("trig") functions describe anything that repeats — waves, rotations, vibrations — and they appear constantly in calculus. We collect the identities you will actually reuse and explain where each comes from, so they are not magic.

> **Concept — radians and the unit circle**
>
> The **unit circle** is the circle of radius $1$ centred at the origin. An angle measured in **radians** equals the length of the arc it cuts off on this circle. We use radians, not degrees, because the clean derivative $(\sin x)'=\cos x$ (proved in §s8) only holds in radians. On the unit circle, the point at angle $\theta$ has coordinates $(\cos\theta,\sin\theta)$ — that *is* the definition of cosine and sine. **ASTC** ("All Students Take Calculus") records the sign pattern by quadrant: in quadrants I, II, III, IV the positive functions are **A**ll, **S**ine, **T**angent, **C**osine respectively.

Definitions:

- $\sin\theta$ (sine) is the vertical coordinate of the point at angle $\theta$ on the unit circle; $\cos\theta$ (cosine) is its horizontal coordinate.
- $\tan\theta=\dfrac{\sin\theta}{\cos\theta}$ (tangent); $\cot\theta=\dfrac{\cos\theta}{\sin\theta}$ (cotangent); $\sec\theta=\dfrac{1}{\cos\theta}$ (secant); $\csc\theta=\dfrac{1}{\sin\theta}$ (cosecant).
- A full turn is $2\pi$ radians ($\approx 6.283$), equal to $360°$, so $\pi$ radians $=180°$.

#### Pythagorean identities

$$\sin^2\theta+\cos^2\theta=1,\quad 1+\tan^2\theta=\sec^2\theta,\quad 1+\cot^2\theta=\csc^2\theta$$

(The notation $\sin^2\theta$ means $(\sin\theta)^2$.)

**Derivation (numbered, every step justified).**

1. The point $(\cos\theta,\sin\theta)$ lies on the unit circle. *Reason:* definition of sine and cosine above.
2. Every point $(x,y)$ on a circle of radius $1$ centred at the origin satisfies $x^2+y^2=1$. *Reason:* the distance from the origin equals the radius, and distance squared is $x^2+y^2$ by the Pythagorean theorem.
3. Substitute $x=\cos\theta$, $y=\sin\theta$: $\cos^2\theta+\sin^2\theta=1$. This is the first identity.
4. Divide both sides of step 3 by $\cos^2\theta$ (allowed when $\cos\theta\neq0$): $\frac{\sin^2\theta}{\cos^2\theta}+1=\frac{1}{\cos^2\theta}$, i.e. $\tan^2\theta+1=\sec^2\theta$. *Reason:* the definitions of $\tan$ and $\sec$ above.
5. Divide step 3 instead by $\sin^2\theta$: $1+\cot^2\theta=\csc^2\theta$, by the same reasoning with $\cot$ and $\csc$.

**Worked example.** If $\sin\theta=\tfrac35$ and $\theta$ is in quadrant I, then from identity 1, $\cos^2\theta=1-\tfrac{9}{25}=\tfrac{16}{25}$, so $\cos\theta=\tfrac45$ (positive in quadrant I by ASTC). Then $\tan\theta=\tfrac{3/5}{4/5}=\tfrac34$.

#### Addition formulas

$$\sin(A\pm B)=\sin A\cos B\pm\cos A\sin B,\quad \cos(A\pm B)=\cos A\cos B\mp\sin A\sin B$$

(The symbol $\pm$ means "use $+$ for the $+$ case and $-$ for the $-$ case"; $\mp$ is the opposite sign.) These say the sine/cosine of a sum of angles can be built from the sines and cosines of the parts. We will not re-derive them from rotations here (that belongs to a trig course), but we *use* them honestly: the proof of $(\sin x)'=\cos x$ in §s8 relies precisely on $\sin(x+h)=\sin x\cos h+\cos x\sin h$.

**Worked example.** $\cos(75°)=\cos(45°+30°)=\cos45°\cos30°-\sin45°\sin30°=\tfrac{\sqrt2}{2}\cdot\tfrac{\sqrt3}{2}-\tfrac{\sqrt2}{2}\cdot\tfrac12=\tfrac{\sqrt6-\sqrt2}{4}\approx0.259$.

#### Double-angle & power-reduction

$$\sin 2\theta=2\sin\theta\cos\theta,\qquad \cos 2\theta=\cos^2\theta-\sin^2\theta$$

$$\sin^2\theta=\frac{1-\cos2\theta}{2},\qquad \cos^2\theta=\frac{1+\cos2\theta}{2}$$

**Derivation of the double-angle formulas.**

1. Set $A=B=\theta$ in the addition formula $\sin(A+B)=\sin A\cos B+\cos A\sin B$. This gives $\sin2\theta=\sin\theta\cos\theta+\cos\theta\sin\theta=2\sin\theta\cos\theta$.
2. Set $A=B=\theta$ in $\cos(A+B)=\cos A\cos B-\sin A\sin B$: $\cos2\theta=\cos^2\theta-\sin^2\theta$.

**Derivation of the power-reduction formulas.**

3. From the Pythagorean identity, $\sin^2\theta=1-\cos^2\theta$. Substitute into $\cos2\theta=\cos^2\theta-\sin^2\theta$ from step 2: $\cos2\theta=\cos^2\theta-(1-\cos^2\theta)=2\cos^2\theta-1$.
4. Solve step 3 for $\cos^2\theta$: $\cos^2\theta=\frac{1+\cos2\theta}{2}$.
5. Similarly $\cos2\theta=(1-\sin^2\theta)-\sin^2\theta=1-2\sin^2\theta$, so $\sin^2\theta=\frac{1-\cos2\theta}{2}$.

*The power-reduction pair is essential for integrating $\sin^2$ and $\cos^2$ in §s19, because it trades a hard squared term for a plain cosine that we can integrate directly.*

## Part B · Limits & continuity

<a id="s3"></a>
### Limits: the basic idea

**What this section says and why we care.** A limit captures "where is the function heading as the input approaches some value," even if the function never actually reaches that value (or is undefined there). This is the single concept on which derivatives and integrals are built.

> **Concept — what a limit is (and isn't)**
>
> The statement $\lim_{x\to a}f(x)=L$ (read "the limit of $f(x)$ as $x$ approaches $a$ equals $L$") describes the **height the outputs approach** as the input $x$ gets close to $a$. It does *not* care about, and need not equal, the actual value $f(a)$ — the graph may even have a hole there. The whole subtlety of calculus lives in this gap between *approaching* and *arriving*.

**Worked example of the gap.** Let $f(x)=\frac{x^2-1}{x-1}$. At $x=1$ the formula gives $\frac{0}{0}$, which is undefined — there is a hole. But for every $x\neq1$ we may cancel: $\frac{(x-1)(x+1)}{x-1}=x+1$. As $x$ approaches $1$, $x+1$ approaches $2$. So $\lim_{x\to1}f(x)=2$ even though $f(1)$ does not exist.

#### One-sided limits & existence

$$\lim_{x\to a^-}f(x)=\lim_{x\to a^+}f(x)=L \iff \lim_{x\to a}f(x)=L$$

Definitions: $x\to a^-$ means $x$ approaches $a$ from the **left** (from smaller values); $x\to a^+$ from the **right** (larger values). The symbol $\iff$ means "if and only if" — the two sides are logically equivalent. The statement says the ordinary (two-sided) limit exists **only when** both one-sided limits exist and agree.

*If the two sides head to different heights, the graph has a **jump** and the two-sided limit does not exist.* Example: the sign function jumps from $-1$ (left of $0$) to $+1$ (right of $0$), so $\lim_{x\to0}$ does not exist.

#### Limits at infinity / infinite limits (asymptotes)

$$\lim_{x\to\infty}\frac1x=0\ \text{(horizontal asymptote)},\qquad \lim_{x\to0^+}\frac1x=+\infty\ \text{(vertical asymptote)}$$

Definitions: $x\to\infty$ means $x$ grows without bound. A **horizontal asymptote** is a horizontal line the graph hugs far out. A **vertical asymptote** is a vertical line near which the outputs blow up to $\pm\infty$. The first limit says $1/x$ is squeezed toward $0$ as $x$ grows huge (e.g. $1/1000=0.001$); the second says $1/x$ explodes as $x$ shrinks toward $0$ from the positive side (e.g. $1/0.001=1000$).

#### Formal ε–δ definition

$$\forall\,\varepsilon>0,\ \exists\,\delta>0:\ 0<|x-a|<\delta \implies |f(x)-L|<\varepsilon$$

This is the rigorous engine behind every casual word "approaches." Symbols: $\forall$ = "for every," $\exists$ = "there exists," $\varepsilon$ (epsilon) and $\delta$ (delta) are small positive numbers, $|u|$ is the **absolute value** (distance of $u$ from $0$, always non-negative), and $\implies$ means "implies." Read in words: *"Name any tolerance $\varepsilon$ for how close the output must be to $L$; I can supply a window $\delta$ around $a$ so that every input within $\delta$ of $a$ (but not equal to $a$) produces an output within $\varepsilon$ of $L$."* The condition $0<|x-a|$ excludes $x=a$ itself, matching "we don't care about the value at $a$."

#### Limit laws & the Sandwich (Squeeze) principle

$$\lim(f\pm g)=L\pm M,\ \ \lim(fg)=LM,\ \ \lim\tfrac fg=\tfrac LM\,(M\neq0)$$

$$g\le f\le h,\ \lim g=\lim h=L \implies \lim f=L$$

Here $L=\lim f$ and $M=\lim g$ at the same point. The first line says limits respect addition, subtraction, multiplication, and division (the last only when the bottom limit $M$ is not zero). The second line is the **Sandwich (Squeeze) principle**: if $f$ is trapped between $g$ and $h$, and both outer functions head to the same $L$, then $f$ is forced to $L$ too — it has nowhere else to go.

**Worked example of the Squeeze.** Consider $f(x)=x^2\sin(1/x)$ near $0$. Since $-1\le\sin(1/x)\le1$, we have $-x^2\le x^2\sin(1/x)\le x^2$. As $x\to0$ both $-x^2$ and $x^2$ go to $0$, so by the Squeeze principle $\lim_{x\to0}x^2\sin(1/x)=0$.

<a id="s4"></a>
### How to compute limits

**What this section says and why we care.** When you simply plug the target value in, you sometimes get a meaningful number (done) and sometimes get a meaningless form like $\frac00$ or $\frac\infty\infty$. These meaningless forms are called **indeterminate** — they do not by themselves tell you the answer. This section gives the standard reshaping tricks that resolve them.

> **Principle — substitute first, then fix**
>
> Always try plugging in. If you get a number, that's the limit (this works whenever the function is continuous there — see §s5). If you get $\frac00$, the trouble is a removable feature: **factor and cancel**, or **multiply by a conjugate**, to delete it. If you get $\frac\infty\infty$, **divide top and bottom by the highest power** of $x$.

#### Demonstration — the three core techniques

1. **Factor & cancel** (rational function, $\frac00$):

   $$\lim_{x\to2}\frac{x^2-4}{x-2}=\lim_{x\to2}\frac{(x-2)(x+2)}{x-2}=\lim_{x\to2}(x+2)=4.$$

   Step justification: at $x=2$ the original gives $\frac00$. We factor $x^2-4=(x-2)(x+2)$ (difference of squares), cancel the common factor $x-2$ (legal because in a limit $x\neq2$, so $x-2\neq0$), then substitute $x=2$ into the now-continuous $x+2$.

2. **Conjugate** (roots, $\frac00$): consider $\lim_{x\to1}\frac{\sqrt{x}-1}{x-1}$. Multiply top and bottom by the conjugate $\sqrt{x}+1$:

   $$\frac{\sqrt{x}-1}{x-1}\cdot\frac{\sqrt{x}+1}{\sqrt{x}+1}=\frac{x-1}{(x-1)(\sqrt{x}+1)}=\frac{1}{\sqrt{x}+1}\xrightarrow[x\to1]{}\frac12.$$

   Step justification: $(\sqrt{x}-1)(\sqrt{x}+1)=x-1$ (difference of squares clears the root), then cancel $x-1$, then substitute.

3. **Highest power** ($x\to\infty$, $\frac\infty\infty$):

   $$\lim_{x\to\infty}\frac{3x^2+1}{5x^2-x}=\lim_{x\to\infty}\frac{3+\frac1{x^2}}{5-\frac1x}=\frac35.$$

   Step justification: divide every term by $x^2$ (the highest power present). As $x\to\infty$, $\frac1{x^2}\to0$ and $\frac1x\to0$ by §s3, leaving $\frac{3}{5}$.

#### Demonstration — the famous $\lim_{x\to0}\frac{\sin x}{x}=1$

This limit (here $x$ is in radians, see §s2) is the heart of trig calculus.

1. For small positive $x$, compare three areas inside the unit circle: a small triangle, a circular sector, and a larger triangle. Their areas give the inequality

   $$\sin x < x < \tan x.$$

   *Reason:* the sector of angle $x$ has area $\tfrac12 x$ (radius $1$), squeezed between the inner triangle of area $\tfrac12\sin x$ and the outer triangle of area $\tfrac12\tan x$; multiply through by $2$.
2. Divide every part by $\sin x$ (positive for small $x>0$, so inequalities keep direction), then take reciprocals (which reverses inequalities):

   $$\cos x < \frac{\sin x}{x} < 1.$$
3. As $x\to0$, $\cos x\to1$ and the right end is $1$. By the Squeeze principle (§s3) the middle is forced to $1$. (For $x<0$ the same value follows because $\frac{\sin x}{x}$ is even.)

*This is exactly what powers $(\sin x)'=\cos x$ in §s8.*

<a id="s5"></a>
### Continuity & differentiability

**What this section says and why we care.** Two quality grades for a function: **continuity** (it flows without breaks) and **differentiability** (it is smooth enough to have a slope). Many big theorems require one or the other, so we pin both down.

#### Continuity at a point

$$f \text{ continuous at } a \iff \lim_{x\to a}f(x)=f(a)$$

In words, three things must all hold and agree: the value $f(a)$ exists, the limit $\lim_{x\to a}f(x)$ exists, and they are equal. Visually: no hole (limit exists but value missing or different), no jump (one-sided limits disagree), and no blow-up (infinite limit).

**Worked example.** $f(x)=x^2$ is continuous at $x=3$ because $\lim_{x\to3}x^2=9=f(3)$. By contrast $g(x)=\frac{x^2-1}{x-1}$ from §s3 is *not* continuous at $x=1$: the limit is $2$ but $g(1)$ does not exist (a hole). We could *repair* it by defining $g(1)=2$.

> **Principle — the Intermediate Value Theorem (IVT)**
>
> If $f$ is continuous on the closed interval $[a,b]$ and $N$ is any number between $f(a)$ and $f(b)$, then there is at least one $c$ in $(a,b)$ with $f(c)=N$. A continuous curve cannot skip a value. ($[a,b]$ means all $x$ with $a\le x\le b$; $(a,b)$ excludes the endpoints.)

**Why we care / worked example.** Let $f(x)=x^3-x-1$. It is continuous (polynomials are). $f(1)=-1<0$ and $f(2)=5>0$. Since $0$ lies between $-1$ and $5$, IVT guarantees a root $c$ in $(1,2)$ where $f(c)=0$. This is the rigorous reason a sign change forces a root — the basis of Newton's method in §s12.

> **Principle — the Extreme Value Theorem (EVT)**
>
> A function continuous on a **closed, bounded** interval $[a,b]$ always attains a maximum value and a minimum value somewhere on that interval. ("Closed" = endpoints included; "bounded" = finite length.) This is what makes "find the largest value" a well-posed problem in optimization (§s12).

The hypotheses matter: $f(x)=1/x$ on the *open* interval $(0,1]$ has no maximum (it shoots to $\infty$ near $0$), precisely because the interval is not closed.

> **Concept — differentiability, and its link to continuity**
>
> A function is **differentiable** at a point where it has a single well-defined tangent slope (the derivative of §s6 exists there). Key principle: **differentiable ⟹ continuous**, but not the reverse. The function $|x|$ (absolute value) is continuous everywhere yet has no slope at the corner $x=0$, because the slope coming from the left is $-1$ and from the right is $+1$ — they disagree, so no single tangent slope exists. Smoothness is strictly stronger than mere unbroken connectedness.

*Proof that differentiable ⟹ continuous (sketch made honest):* if $f'(a)$ exists then $\lim_{x\to a}\big(f(x)-f(a)\big)=\lim_{x\to a}\frac{f(x)-f(a)}{x-a}\cdot(x-a)=f'(a)\cdot0=0$ by the product limit law (§s3), so $\lim_{x\to a}f(x)=f(a)$, which is continuity.

## Part C · The derivative

<a id="s6"></a>
### The definition of the derivative

**What this section says and why we care.** Here we make "slope of a curve / instantaneous rate" precise, using the limit of §s3. This single definition generates every differentiation rule that follows.

#### Definition

$$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}=\lim_{t\to x}\frac{f(t)-f(x)}{t-x}$$

Definitions of symbols:

- $f'(x)$ (read "$f$ prime of $x$") is the **derivative** of $f$ at $x$.
- $h$ is a small change in the input; $x+h$ is a nearby input.
- $\frac{f(x+h)-f(x)}{h}$ is the **difference quotient**: the ordinary "rise over run" slope between the two points $(x,f(x))$ and $(x+h,f(x+h))$. Rise $=f(x+h)-f(x)$, run $=h$.
- Taking $\lim_{h\to0}$ slides the two points together. The two forms are the same idea with $t=x+h$.

> **Concept — three meanings, one object**
>
> The derivative is simultaneously: the **slope of the tangent line** to the graph at $x$; the **instantaneous rate of change** of the output per unit input; and, if $s(t)$ is position at time $t$, the **velocity** $s'(t)$. The difference quotient is the average velocity over a tiny interval; the limit makes it instantaneous.

#### Demonstration — $f(x)=x^2$ from the definition

1. Form the difference quotient and expand the square:

   $$\frac{(x+h)^2-x^2}{h}=\frac{x^2+2xh+h^2-x^2}{h}=\frac{2xh+h^2}{h}=2x+h.$$

   *Justification:* $(x+h)^2=x^2+2xh+h^2$ (multiplying out); the $x^2$ terms cancel; divide each remaining term by $h$ (legal since $h\neq0$ in the limit).
2. Let $h\to0$. The term $h$ vanishes, leaving

   $$f'(x)=2x.$$

   *Justification:* limit laws (§s3) — the limit of $2x+h$ as $h\to0$ is $2x+0$.

**Numeric check.** At $x=1$ this gives $f'(1)=2$, matching the heading-toward-$2$ we observed numerically in §s0. At $x=3$, $f'(3)=6$.

<a id="s7"></a>
### The differentiation rules — each one proven

**What this section says and why we care.** Computing every derivative from the limit definition would be exhausting. Instead we prove a handful of rules *once*, then only use the rules. Each is derived honestly from §s6.

#### Basic rules

$$\tfrac{d}{dx}[c]=0,\quad \tfrac{d}{dx}[x^n]=nx^{n-1},\quad (cf)'=cf',\quad (f\pm g)'=f'\pm g'$$

Notation: $\frac{d}{dx}[\,\cdot\,]$ means "the derivative with respect to $x$ of"; $c$ is a constant (a fixed number). In words: the derivative of a constant is $0$ (a flat line has slope $0$); the **power rule** says the derivative of $x^n$ is $n x^{n-1}$; a constant multiplier pulls out; and the derivative of a sum is the sum of derivatives.

**Proof of $(f\pm g)'=f'\pm g'$.** The difference quotient of $f+g$ is $\frac{[f(x+h)+g(x+h)]-[f(x)+g(x)]}{h}=\frac{f(x+h)-f(x)}{h}+\frac{g(x+h)-g(x)}{h}$ (regrouping). Taking $h\to0$ and using the sum limit law (§s3) gives $f'+g'$. The constant rule $(cf)'=cf'$ follows the same way, factoring $c$ out of the quotient.

#### ★ The famous, everyday derivatives

$$\tfrac{d}{dx}e^{x}=e^{x},\qquad \tfrac{d}{dx}\sqrt{x}=\tfrac{1}{2\sqrt{x}},\qquad \tfrac{d}{dx}\tfrac1x=-\tfrac{1}{x^{2}}$$

*$e^x$ is the most famous derivative in mathematics — the only function (up to a constant multiple) that equals its own derivative, which is why it governs growth and decay (§s29).* The other two are everyday special cases of the power rule:

- $\sqrt{x}=x^{1/2}$, so the power rule gives $\tfrac12 x^{1/2-1}=\tfrac12 x^{-1/2}=\frac{1}{2\sqrt{x}}$.
- $\tfrac1x=x^{-1}$, so the power rule gives $-1\cdot x^{-2}=-\frac{1}{x^2}$.

#### Demonstration — power rule via the binomial theorem (for positive integer $n$)

1. Expand using the **binomial theorem** (which says $(x+h)^n$ is a sum of terms, the first two being $x^n$ and $n x^{n-1}h$):

   $$(x+h)^n=x^n+nx^{n-1}h+\tfrac{n(n-1)}2x^{n-2}h^2+\cdots+h^n.$$
2. Subtract $x^n$ and divide by $h$ (every remaining term has at least one factor $h$):

   $$\frac{(x+h)^n-x^n}{h}=nx^{n-1}+\tfrac{n(n-1)}2x^{n-2}h+\cdots+h^{n-1}.$$
3. Let $h\to0$: every term still containing $h$ becomes $0$, leaving $nx^{n-1}$. *Justification:* limit laws. The result also holds for fractional and negative $n$ (provable later with logarithmic or implicit differentiation), as the two special cases above illustrate.

**Worked example.** $\frac{d}{dx}\big[4x^3-2x+7\big]=4\cdot3x^2-2\cdot1+0=12x^2-2$, using the power, constant-multiple, sum, and constant rules together.

#### Product, quotient, chain

$$(fg)'=f'g+fg',\quad \Big(\tfrac fg\Big)'=\tfrac{f'g-fg'}{g^2},\quad \tfrac{d}{dx}f(g(x))=f'(g(x))g'(x)$$

In words: the **product rule** — derivative of a product is (derivative of first)(second) + (first)(derivative of second). The **quotient rule** handles a fraction. The **chain rule** handles a composition (a function inside a function): differentiate the outer function at the inner value, then multiply by the derivative of the inner.

#### Demonstration — product rule (add-and-subtract trick)

1. Write the difference quotient of $fg$ and insert $-f(x+h)g(x)+f(x+h)g(x)$ (adding zero, a legal move):

   $$\frac{f(x+h)g(x+h)-f(x)g(x)}{h}=\frac{f(x+h)g(x+h)-f(x+h)g(x)+f(x+h)g(x)-f(x)g(x)}{h}.$$
2. Group into two pieces:

   $$f(x+h)\frac{g(x+h)-g(x)}h+g(x)\frac{f(x+h)-f(x)}h.$$
3. Let $h\to0$. Then $f(x+h)\to f(x)$ (because $f$ is continuous, §s5), the first fraction $\to g'(x)$, and the second $\to f'(x)$. By the product and sum limit laws this gives $f g'+g f'$.

The quotient rule follows by writing $f=(f/g)\cdot g$ and applying the product rule, then solving for $(f/g)'$. The chain rule follows from the cancellation $\frac{\Delta y}{\Delta x}=\frac{\Delta y}{\Delta u}\cdot\frac{\Delta u}{\Delta x}$ in the limit (where $u=g(x)$).

**Worked example (chain rule).** $\frac{d}{dx}(x^2+1)^5$: outer is $u^5$ with derivative $5u^4$, inner is $u=x^2+1$ with derivative $2x$. Result: $5(x^2+1)^4\cdot2x=10x(x^2+1)^4$.

> **Forward link**
>
> Read backwards, the **product rule becomes integration by parts** and the **chain rule becomes u-substitution** (§s18). We derive both there from these rules.

<a id="s8"></a>
### Derivatives of every standard function

**What this section says and why we care.** This is the master table — trig, exponential, logarithmic, inverse, and hyperbolic functions — with the key proofs. Together with §s7's rules, it lets you differentiate essentially anything.

| Function | Derivative | Function | Derivative |
| --- | --- | --- | --- |
| $\sin x$ | $\cos x$ | $\sec x$ | $\sec x\tan x$ |
| $\cos x$ | $-\sin x$ | $\csc x$ | $-\csc x\cot x$ |
| $\tan x$ | $\sec^2 x$ | $\cot x$ | $-\csc^2 x$ |
| $e^x$ | $e^x$ | $\ln x$ | $1/x$ |
| $a^x$ | $a^x\ln a$ | $\log_a x$ | $1/(x\ln a)$ |
| $\arcsin x$ | $1/\sqrt{1-x^2}$ | $\arctan x$ | $1/(1+x^2)$ |
| $\sinh x$ | $\cosh x$ | $\cosh x$ | $\sinh x$ |

Definitions of the less familiar entries: $\ln x$ is the **natural logarithm** (the inverse of $e^x$: $\ln$ answers "$e$ to what power gives $x$?"); $\log_a x$ is the logarithm base $a$; $\arcsin$ and $\arctan$ are the inverse sine and inverse tangent (they return the angle); $\sinh x=\frac{e^x-e^{-x}}{2}$ and $\cosh x=\frac{e^x+e^{-x}}{2}$ are the **hyperbolic** sine and cosine.

> **Concept — where $e$ comes from**
>
> $e$ is *defined* as the unique base making the exponential its own derivative. Equivalently it arises from continuously compounded interest: $e=\lim_{n\to\infty}\left(1+\tfrac1n\right)^n\approx2.71828$. The number is chosen precisely so that the limit $\frac{e^h-1}{h}\to1$ as $h\to0$.

#### Demonstration — $(\sin x)'=\cos x$ and $(e^x)'=e^x$

1. **Sine.** Expand $\sin(x+h)=\sin x\cos h+\cos x\sin h$ (addition formula, §s2). The difference quotient becomes

   $$\frac{\sin(x+h)-\sin x}{h}=\sin x\cdot\frac{\cos h-1}{h}+\cos x\cdot\frac{\sin h}{h}.$$

   As $h\to0$: $\frac{\sin h}{h}\to1$ (§s4) and $\frac{\cos h-1}{h}\to0$ (a companion limit, provable by multiplying by $\frac{\cos h+1}{\cos h+1}$ and using $\frac{\sin h}{h}\to1$). So the quotient $\to \sin x\cdot0+\cos x\cdot1=\cos x$.
2. **Exponential.** Factor:

   $$\frac{e^{x+h}-e^x}{h}=\frac{e^x e^h-e^x}{h}=e^x\cdot\frac{e^h-1}{h}\xrightarrow[h\to0]{}e^x\cdot1=e^x,$$

   using $e^{x+h}=e^x e^h$ (exponent rule) and the defining limit $\frac{e^h-1}{h}\to1$ above.

**Worked example.** $\frac{d}{dx}\big[e^x\sin x\big]=e^x\sin x+e^x\cos x=e^x(\sin x+\cos x)$ by the product rule (§s7) with these two derivatives.

#### Derivative of an inverse function

$$\big(f^{-1}\big)'(x)=\frac{1}{f'\!\big(f^{-1}(x)\big)}$$

**Proof.** By definition $f\big(f^{-1}(x)\big)=x$. Differentiate both sides with respect to $x$. The left side, by the chain rule (§s7), is $f'\big(f^{-1}(x)\big)\cdot\big(f^{-1}\big)'(x)$; the right side is $1$. Solving gives the boxed formula.

This is exactly how the table's $\ln$ and inverse-trig derivatives are obtained. **Example ($\ln$):** with $f=e^x$ (so $f'=e^x$) and $f^{-1}=\ln$, the formula gives $(\ln x)'=\frac{1}{e^{\ln x}}=\frac{1}{x}$, since $e^{\ln x}=x$.

> **Concept — simple harmonic motion**
>
> Because $(\sin)'=\cos$ and $(\cos)'=-\sin$, the function $y=\sin(\omega t)$ satisfies $y''=-\omega^2 y$: its acceleration is proportional to its displacement and points back toward the centre. That single relationship is why sines and cosines model springs, pendulums, sound, and alternating current. (Verify: $y'=\omega\cos(\omega t)$, $y''=-\omega^2\sin(\omega t)=-\omega^2 y$, by the chain rule.)

<a id="s9"></a>
### Implicit differentiation & related rates

**What this section says and why we care.** Two close cousins. **Implicit differentiation** finds slopes on curves that are not solved for $y$ (like a circle). **Related rates** problems link the speeds of several quantities that change together over time. Both are the chain rule (§s7) applied with care.

#### Demonstration — implicit slope on $x^2+y^2=25$ (a circle of radius 5)

1. Differentiate both sides with respect to $x$, treating $y$ as a hidden function of $x$ (so every $y$-term carries a $\frac{dy}{dx}$ by the chain rule):

   $$2x+2y\frac{dy}{dx}=0.$$

   *Justification:* $\frac{d}{dx}x^2=2x$ (power rule); $\frac{d}{dx}y^2=2y\cdot\frac{dy}{dx}$ (chain rule, since $y$ depends on $x$); $\frac{d}{dx}25=0$.
2. Solve for the slope:

   $$\frac{dy}{dx}=-\frac xy.$$

**Worked example.** At the point $(3,4)$ on the circle, the slope is $-\tfrac34$. The tangent line there is $y-4=-\tfrac34(x-3)$.

> **Principle — related rates**
>
> When several variables are tied by an equation and all change with time $t$, **differentiate the relation with respect to $t$**. Each variable contributes its own rate ($\frac{d}{dt}$) via the chain rule, linking an unknown rate to known ones.

#### Demonstration — a ladder sliding down a wall

A ladder of fixed length $L$ leans against a wall; its base is $x$ from the wall and its top is $y$ up the wall.

1. Relation (Pythagoras): $x^2+y^2=L^2$.
2. Differentiate in $t$ (chain rule, $L$ constant): $2x\frac{dx}{dt}+2y\frac{dy}{dt}=0$.
3. Solve for the wanted rate: $\frac{dy}{dt}=-\frac{x}{y}\frac{dx}{dt}$.

**Worked example with numbers.** Let $L=10$, and suppose the base slides out at $\frac{dx}{dt}=1$ ft/s. When $x=6$, then $y=\sqrt{100-36}=8$. So $\frac{dy}{dt}=-\frac{6}{8}\cdot1=-0.75$ ft/s — the top slides *down* at $0.75$ ft/s (negative = decreasing height).

#### Higher-order derivatives

$$f''=\frac{d}{dx}f',\qquad f^{(n)}=\frac{d^n y}{dx^n}$$

The **second derivative** $f''$ is the derivative of the derivative; $f^{(n)}$ is the $n$-th derivative (apply the operation $n$ times). *Position $s$ → velocity $s'$ → acceleration $s''$.* The second derivative also controls concavity (§s10). **Example:** if $f=x^4$ then $f'=4x^3$, $f''=12x^2$, $f'''=24x$, $f^{(4)}=24$, and all higher ones are $0$.

## Part D · Using derivatives

<a id="s10"></a>
### Extrema, Rolle's theorem & the Mean Value Theorem

**What this section says and why we care.** The derivative reveals a graph's shape — where it rises, falls, peaks, and bends. We define the key points and prove the Mean Value Theorem, the workhorse behind "the sign of $f'$ tells you whether $f$ rises."

> **Concept — extrema & critical points**
>
> A **local maximum** (resp. **minimum**) is a point higher (resp. lower) than all nearby points. A local extremum of a differentiable function can only occur where $f'(x)=0$ or $f'$ is undefined — such a point is a **critical point**. (This is **Fermat's principle**: at a smooth peak or valley the tangent is horizontal, slope $0$.) For a **global** extremum on $[a,b]$, also check the endpoints — existence is guaranteed by the EVT (§s5).

**Why Fermat's principle holds (proof).** Suppose $f$ has a local maximum at $c$ and $f'(c)$ exists. For $x$ slightly above $c$, $f(x)\le f(c)$, so the right-hand difference quotient $\frac{f(x)-f(c)}{x-c}\le0$; for $x$ slightly below, it is $\ge0$. Both one-sided limits equal $f'(c)$, so $f'(c)\le0$ and $f'(c)\ge0$, forcing $f'(c)=0$.

#### Rolle's theorem → Mean Value Theorem

$$\exists\,c\in(a,b):\ f'(c)=\frac{f(b)-f(a)}{b-a}$$

**Rolle's theorem** is the special case $f(a)=f(b)$: if a differentiable curve returns to the same height, somewhere in between its slope is $0$ (by EVT it has a high or low point inside, where Fermat gives $f'(c)=0$). The **Mean Value Theorem (MVT)** is the tilted version: somewhere your *instantaneous* rate equals your *average* rate over $[a,b]$.

**Proof of MVT from Rolle's.** Define $g(x)=f(x)-\big[f(a)+\frac{f(b)-f(a)}{b-a}(x-a)\big]$ — the function minus the straight line joining the endpoints. Then $g(a)=g(b)=0$, so Rolle's theorem gives a $c$ with $g'(c)=0$. But $g'(x)=f'(x)-\frac{f(b)-f(a)}{b-a}$, so $f'(c)=\frac{f(b)-f(a)}{b-a}$.

*Consequence we use everywhere: if $f'>0$ on an interval, then for any $a<b$ there, MVT gives $f(b)-f(a)=f'(c)(b-a)>0$, so $f$ is increasing. This is the rigorous basis of the rising/falling test.*

**Worked example.** On $[0,2]$ with $f(x)=x^2$: average rate $=\frac{4-0}{2-0}=2$. Set $f'(c)=2c=2$, so $c=1\in(0,2)$. Confirmed.

#### Concavity, inflection & the derivative tests

$$f''>0:\text{concave up},\quad f''<0:\text{concave down},\quad f''\text{ changes sign}:\text{inflection}$$

$$f'(c)=0:\ f''(c)>0\Rightarrow\text{min},\quad f''(c)<0\Rightarrow\text{max}$$

**Concave up** means the curve bends like a cup (holds water); **concave down** bends like a cap. An **inflection point** is where the bending switches. The **second-derivative test**: at a critical point where $f'(c)=0$, if the curve is cup-shaped ($f''>0$) it is a local minimum; if cap-shaped ($f''<0$) a local maximum.

**Worked example.** $f(x)=x^3-3x$: $f'=3x^2-3=0$ at $x=\pm1$. $f''=6x$. At $x=1$, $f''=6>0$ → local min; at $x=-1$, $f''=-6<0$ → local max. Inflection where $f''=0$, i.e. $x=0$.

<a id="s11"></a>
### Curve sketching — the table-of-signs method

**What this section says and why we care.** A systematic recipe converts the three pieces of information $f,f',f''$ into a complete, accurate picture of a graph without plotting hundreds of points.

> **Principle — read the function from its derivatives**
>
> $f$ tells you height; $f'$ tells you whether the graph goes up or down; $f''$ tells you which way it bends. Combining these three sign patterns with intercepts and asymptotes pins the graph down completely.

#### The method, in order

1. **Domain:** find which inputs are legal (exclude divisions by zero, even roots of negatives).
2. **Intercepts:** set $x=0$ for the $y$-intercept; set $f(x)=0$ for $x$-intercepts.
3. **Symmetry:** check even ($f(-x)=f(x)$) or odd ($f(-x)=-f(x)$), §s1.
4. **Asymptotes:** vertical where the function blows up; horizontal from $\lim_{x\to\pm\infty}f$ (§s3).
5. **First derivative:** solve $f'=0$ and mark a sign table; $f'>0$ rising, $f'<0$ falling; sign changes give local extrema (§s10).
6. **Second derivative:** solve $f''=0$ and mark a sign table; $f''>0$ concave up, $f''<0$ concave down; sign changes give inflection points.
7. **Assemble** the curve from this information.

**Worked example.** For $f(x)=x^3-3x$ (from §s10): domain all reals; intercepts at $x=0$ and $x=\pm\sqrt3$; odd function; no asymptotes; rising on $(-\infty,-1)$ and $(1,\infty)$, falling on $(-1,1)$; local max $(-1,2)$, local min $(1,-2)$; concave down for $x<0$, up for $x>0$, inflection at $(0,0)$. These facts draw the classic "wiggle" cubic.

<a id="s12"></a>
### Optimization, linearization & Newton's method

**What this section says and why we care.** Three of the most useful real-world payoffs of the derivative: finding best values, approximating a curve by a line for quick estimates, and solving equations numerically.

> **Principle — optimization**
>
> To maximize or minimize a real quantity: write it as a function of **one** variable (using any constraint to eliminate the others), differentiate, set $f'=0$, and test the critical points (and endpoints). The EVT (§s5) guarantees a best value exists on a closed interval.

**Worked example (the classic fence/box).** A farmer has $100$ m of fence for a rectangular pen against a wall (wall side needs no fence). Let width $x$ and length $y$, with $2x+y=100$, so $y=100-2x$. Area $A=xy=x(100-2x)=100x-2x^2$. Then $A'=100-4x=0$ gives $x=25$, and $A''=-4<0$ confirms a maximum. So $x=25$, $y=50$, maximum area $1250\ \text{m}^2$.

#### Linearization & the differential

$$L(x)=f(a)+f'(a)(x-a),\qquad dy=f'(x)\,dx$$

$L(x)$ is the **linearization** (tangent-line approximation) of $f$ near $a$: replace the curve by its tangent line for a quick estimate. The **differential** $dy=f'(x)\,dx$ packages the same idea: a tiny input change $dx$ produces an approximate output change $dy$. The error of the approximation shrinks like $(x-a)^2$ as $x\to a$. Extended forever, this becomes the Taylor series (§s25).

**Worked example.** Estimate $\sqrt{4.1}$. Use $f(x)=\sqrt x$ at $a=4$: $f(4)=2$, $f'(x)=\frac{1}{2\sqrt x}$ so $f'(4)=\tfrac14$. Then $L(4.1)=2+\tfrac14(0.1)=2.025$. (True value $\approx2.0248$ — excellent.)

#### Newton's method (root-finding)

$$x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$$

To solve $f(x)=0$: from a guess $x_n$, follow the tangent line down to where it hits the $x$-axis; that landing point is the next, better guess $x_{n+1}$. Repeat. It converges astonishingly fast (roughly doubling the number of correct digits each step) when started near a root.

**Worked example.** Solve $x^2-2=0$ (so $x=\sqrt2$) with $f(x)=x^2-2$, $f'(x)=2x$. The rule becomes $x_{n+1}=x_n-\frac{x_n^2-2}{2x_n}=\frac{x_n}{2}+\frac{1}{x_n}$. Start $x_0=1.5$: $x_1=0.75+0.6667=1.41667$; $x_2=0.70833+0.70588=1.41422$, already correct to 5 decimals ($\sqrt2\approx1.41421$).

<a id="s13"></a>
### L'Hôpital's rule — every indeterminate form

**What this section says and why we care.** A derivative-powered tool for limits that factoring and conjugates cannot crack — and a system for converting *every* indeterminate form into a shape it can handle.

#### The rule (for $\tfrac00$ or $\tfrac\infty\infty$)

$$\lim_{x\to a}\frac{f(x)}{g(x)}=\lim_{x\to a}\frac{f'(x)}{g'(x)}$$

It applies **only** when direct substitution gives the indeterminate forms $\tfrac00$ or $\tfrac\infty\infty$, and when the right-hand limit exists. You replace numerator and denominator by their derivatives and try again.

**Worked example.** $\lim_{x\to0}\frac{\sin x}{x}$ is $\tfrac00$. Differentiate top and bottom: $\frac{\cos x}{1}\to\cos0=1$. (Same answer as the geometric proof in §s4, now in one line.)

> **Principle — reduce every form to a fraction**
>
> The other indeterminate forms must first be **rewritten** as $\tfrac00$ or $\tfrac\infty\infty$:

| Form | How to convert |
| --- | --- |
| $0\cdot\infty$ | Rewrite as $\dfrac{0}{1/\infty}$ or $\dfrac{\infty}{1/0}$ |
| $\infty-\infty$ | Combine over a common denominator |
| $1^\infty,\ 0^0,\ \infty^0$ | Take $\ln$, find the limit, then exponentiate |

**Worked example ($0\cdot\infty$).** $\lim_{x\to0^+}x\ln x$: rewrite as $\frac{\ln x}{1/x}$ (form $\frac{-\infty}{\infty}$). L'Hôpital: $\frac{1/x}{-1/x^2}=-x\to0$. So the limit is $0$.

> **Why it works**
>
> Near $a$, linearization (§s12) gives $f(x)\approx f'(a)(x-a)$ and $g(x)\approx g'(a)(x-a)$ when $f(a)=g(a)=0$. Their ratio $\frac{f'(a)(x-a)}{g'(a)(x-a)}$ has the common factor $(x-a)$ cancel, leaving $\frac{f'(a)}{g'(a)}$. It is local linearization again.

## Part E · Integration

<a id="s14"></a>
### Sums, area & the idea of the integral

**What this section says and why we care.** Before the shortcut (the Fundamental Theorem) comes the *definition*: the integral is the area under a curve, computed as the limit of a sum of thin rectangles. We first need notation for sums.

#### Sigma notation & useful sums

$$\sum_{i=1}^{n}c=nc,\quad \sum_{i=1}^{n}i=\frac{n(n+1)}2,\quad \sum_{i=1}^{n}i^2=\frac{n(n+1)(2n+1)}6$$

The symbol $\sum_{i=1}^{n}$ (capital sigma) means "add up the following expression as $i$ runs from $1$ to $n$." So $\sum_{i=1}^{n}c=c+c+\cdots+c$ ($n$ copies) $=nc$.

**Proof of $\sum_{i=1}^n i=\frac{n(n+1)}2$ (Gauss's pairing).** Write the sum forwards $S=1+2+\cdots+n$ and backwards $S=n+(n-1)+\cdots+1$. Add term by term: each of the $n$ columns totals $n+1$, so $2S=n(n+1)$, giving $S=\frac{n(n+1)}2$. **Check:** $n=4$ gives $\frac{4\cdot5}2=10=1+2+3+4$.

> **Concept — a telescoping sum**
>
> If consecutive terms cancel in a cascade — $\sum_{i=1}^n (a_i-a_{i+1})=a_1-a_{n+1}$ — almost everything collapses, leaving only the first and last pieces. (Each $-a_{i+1}$ is cancelled by the next $+a_{i+1}$.) This is the discrete shadow of the Fundamental Theorem, where an integral collapses to its endpoint values.

#### The Riemann sum → the integral

$$\int_a^b f(x)\,dx=\lim_{n\to\infty}\sum_{i=1}^{n}f(x_i^*)\,\Delta x,\qquad \Delta x=\frac{b-a}{n}$$

Definitions: we slice $[a,b]$ into $n$ equal strips of width $\Delta x=\frac{b-a}{n}$. In each strip we pick a sample point $x_i^*$ and build a rectangle of height $f(x_i^*)$ and width $\Delta x$; its area is $f(x_i^*)\Delta x$. The **Riemann sum** $\sum f(x_i^*)\Delta x$ totals these rectangle areas. The **integral** $\int_a^b f\,dx$ *is* the limit as the strips become infinitely thin ($n\to\infty$). **Signed area:** strips below the axis (negative $f$) count as negative area.

**Worked example.** Compute $\int_0^1 x\,dx$ from the definition with right endpoints $x_i^*=\frac{i}{n}$, $\Delta x=\frac1n$. Sum $=\sum_{i=1}^n \frac{i}{n}\cdot\frac1n=\frac{1}{n^2}\sum i=\frac{1}{n^2}\cdot\frac{n(n+1)}2=\frac{n+1}{2n}=\frac12+\frac{1}{2n}\to\frac12$. So the area of the triangle under $y=x$ from $0$ to $1$ is $\frac12$ — matching base $\times$ height $/2$.

<a id="s15"></a>
### The definite integral

**What this section says and why we care.** With the integral defined, we list the algebraic properties it obeys (which follow directly from it being a limit of sums) and two indispensable applications: area between curves and average value.

#### Properties

$$\int_a^b f=-\int_b^a f,\quad \int_a^a f=0,\quad \int_a^b f=\int_a^c f+\int_c^b f$$

$$\int_a^b(f\pm g)=\int_a^b f\pm\int_a^b g,\qquad \int_a^b cf=c\int_a^b f$$

These say, in order: reversing the limits flips the sign; an integral over zero width is zero; you may split the interval at any interior point $c$ and add; the integral of a sum is the sum of integrals; constants pull out. Each follows from the Riemann-sum definition (§s14) and the limit laws (§s3) — e.g. the sum rule comes from the fact that a Riemann sum of $f+g$ splits into the Riemann sums of $f$ and $g$.

#### Area between curves & average value

$$A=\int_a^b\big[\text{top}-\text{bottom}\big]\,dx,\qquad \bar f=\frac{1}{b-a}\int_a^b f\,dx$$

The area between two curves is the integral of (upper curve) minus (lower curve). The **average value** $\bar f$ generalizes the everyday average: total accumulation $\int_a^b f$ divided by the length $b-a$.

**Worked example (average value).** The average of $f(x)=x^2$ on $[0,3]$ is $\frac{1}{3}\int_0^3 x^2\,dx=\frac13\cdot\frac{27}{3}=\frac13\cdot9=3$ (using $\int_0^3 x^2\,dx=\frac{x^3}{3}\big|_0^3=9$ from §s16–s17).

> **Principle — the Mean Value Theorem for integrals**
>
> A continuous function attains its own average value somewhere: there is a $c$ in $[a,b]$ with $f(c)=\bar f$. Geometrically, a rectangle of width $b-a$ and height $f(c)$ has exactly the same area as the region under the curve. (Proof: apply IVT, §s5, to $f$ between its min and max, since $\bar f$ lies between them.)

<a id="s16"></a>
### The Fundamental Theorem of Calculus

**What this section says and why we care.** This is the hinge of the entire subject: differentiation and integration are *inverse operations*. It turns the hard limit-of-sums into the easy "find an antiderivative and subtract."

#### First FTC — differentiation undoes integration

$$\frac{d}{dx}\int_a^x f(t)\,dt=f(x)$$

The function $A(x)=\int_a^x f(t)\,dt$ accumulates area from $a$ up to a moving right end $x$. The First FTC says its derivative is just $f(x)$: the rate at which area accumulates equals the current height.

#### Second FTC — antiderivatives evaluate integrals

$$\int_a^b f(x)\,dx=F(b)-F(a),\quad F'=f$$

An **antiderivative** $F$ of $f$ is any function whose derivative is $f$. The Second FTC says: to get the definite integral, find any antiderivative and subtract its values at the endpoints.

#### Demonstration — why the First FTC is true

1. Let $A(x)=\int_a^x f(t)\,dt$. Increasing the right end by a small $h$ adds a thin strip whose area, for continuous $f$, is approximately a rectangle of height $f(x)$ and width $h$:

   $$A(x+h)-A(x)\approx f(x)\,h.$$

   *Justification:* over a tiny interval $f$ barely changes (continuity, §s5), so the added sliver is nearly that rectangle. Precisely, the MVT for integrals (§s15) gives $A(x+h)-A(x)=f(c)\,h$ for some $c$ between $x$ and $x+h$.
2. Divide by $h$ and let $h\to0$: $\frac{A(x+h)-A(x)}{h}=f(c)\to f(x)$, since $c\to x$ and $f$ is continuous. Hence $A'(x)=f(x)$.

*The Second FTC follows: if $F'=f$ then $F$ and $A$ have the same derivative, so they differ only by a constant (a consequence of the MVT, §s10): $F(x)=A(x)+C$. Then $F(b)-F(a)=A(b)-A(a)=\int_a^b f-0=\int_a^b f$.*

#### Indefinite integral

$$\int f(x)\,dx=F(x)+C,\qquad F'=f$$

The **indefinite integral** (or **antiderivative**) is the whole family of functions with derivative $f$. The constant $C$ appears because differentiation erases constants, so antiderivatives are only determined up to an added constant.

**Worked example.** $\int x^2\,dx=\frac{x^3}{3}+C$ (check: $\frac{d}{dx}\frac{x^3}{3}=x^2$). Then $\int_0^3 x^2\,dx=\frac{3^3}{3}-\frac{0^3}{3}=9-0=9$, confirming the value used in §s15.

<a id="s17"></a>
### The basic integral table

**What this section says and why we care.** Every entry below is simply a §s7–s8 derivative read backwards. You can verify any line by differentiating the right-hand side and recovering the integrand.

| Integral | Result | Integral | Result |
| --- | --- | --- | --- |
| $\int x^n dx\,(n\neq-1)$ | $\frac{x^{n+1}}{n+1}+C$ | $\int\frac1x dx$ | $\ln\vert x\vert +C$ |
| $\int e^x dx$ | $e^x+C$ | $\int a^x dx$ | $\frac{a^x}{\ln a}+C$ |
| $\int\cos x dx$ | $\sin x+C$ | $\int\sin x dx$ | $-\cos x+C$ |
| $\int\sec^2 x dx$ | $\tan x+C$ | $\int\sec x\tan x dx$ | $\sec x+C$ |
| $\int\frac{dx}{1+x^2}$ | $\arctan x+C$ | $\int\frac{dx}{\sqrt{1-x^2}}$ | $\arcsin x+C$ |
| $\int\tan x dx$ | $\ln\vert \sec x\vert +C$ | $\int\sec x dx$ | $\ln\vert \sec x+\tan x\vert +C$ |

**Verification example.** The power rule for integrals: differentiate $\frac{x^{n+1}}{n+1}$ to get $\frac{(n+1)x^n}{n+1}=x^n$ — recovering the integrand, as required. (The exclusion $n\neq-1$ is exactly the case $\int\frac1x\,dx=\ln|x|+C$, separately listed.)

> **Don't memorize twice**
>
> If you know the derivative tables of §s7–s8, you already know this one — just flip the arrow. That is the Fundamental Theorem in daily use.

<a id="s18"></a>
### Techniques of integration I — substitution, parts, partial fractions

**What this section says and why we care.** Most integrals are not in the table directly; we reshape them until they are. The first three workhorse methods follow — and two of them are just §s7's differentiation rules run backwards.

#### u-substitution & integration by parts

$$\int f(g(x))g'(x)\,dx=\int f(u)\,du,\qquad \int u\,dv=uv-\int v\,du$$

**u-substitution** replaces a chunk $u=g(x)$ (with $du=g'(x)\,dx$) to simplify a composition. **Integration by parts** handles a product of two functions.

#### Demonstration — both come from earlier rules

1. **u-sub reverses the chain rule.** Since $\frac{d}{dx}F(g(x))=f(g(x))g'(x)$ where $F'=f$ (chain rule, §s7), integrating both sides gives $\int f(g(x))g'(x)\,dx=F(g(x))+C=\int f(u)\,du$ with $u=g(x)$.
2. **By parts reverses the product rule.** From $(uv)'=u'v+uv'$ (§s7), integrate both sides: $uv=\int u'v\,dx+\int uv'\,dx$. Rearrange and use $dv=v'\,dx$, $du=u'\,dx$: $\int u\,dv=uv-\int v\,du$.

**Worked example (u-sub).** $\int 2x\cos(x^2)\,dx$: let $u=x^2$, $du=2x\,dx$. Then it becomes $\int\cos u\,du=\sin u+C=\sin(x^2)+C$. (Check by differentiating: $\cos(x^2)\cdot2x$. Correct.)

**Worked example (by parts).** $\int x e^x\,dx$: let $u=x$ (so $du=dx$) and $dv=e^x\,dx$ (so $v=e^x$). Then $\int x e^x\,dx=xe^x-\int e^x\,dx=xe^x-e^x+C$.

> **Concept — partial fractions**
>
> Any **proper** rational function (a polynomial over a polynomial, with the top of lower degree than the bottom) splits into simpler pieces — one term per linear or quadratic factor of the denominator — each of which integrates to a logarithm or an arctangent. The work is algebra first, calculus second.

#### Partial-fraction form

$$\frac{P(x)}{(x-r_1)(x-r_2)}=\frac{A}{x-r_1}+\frac{B}{x-r_2}$$

**Worked example.** $\frac{1}{(x-1)(x+1)}=\frac{A}{x-1}+\frac{B}{x+1}$. Multiply out: $1=A(x+1)+B(x-1)$. Set $x=1$: $1=2A$, so $A=\tfrac12$. Set $x=-1$: $1=-2B$, so $B=-\tfrac12$. Hence $\int\frac{dx}{(x-1)(x+1)}=\tfrac12\ln|x-1|-\tfrac12\ln|x+1|+C$.

<a id="s19"></a>
### Techniques of integration II — trig integrals, trig substitution, reduction

**What this section says and why we care.** Specialized methods for two recurring difficulties: powers of trig functions, and integrals containing stubborn square roots like $\sqrt{a^2-x^2}$.

> **Principle — powers of sin and cos**
>
> If a power of $\sin$ or $\cos$ is **odd**, peel off one factor to pair with $dx$, convert the remaining even power using $\sin^2+\cos^2=1$ (§s2), then u-substitute. If **both** powers are even, use the power-reduction identities from §s2 to lower them.

**Worked example (odd power).** $\int\sin^3 x\,dx=\int\sin^2 x\cdot\sin x\,dx=\int(1-\cos^2 x)\sin x\,dx$. Let $u=\cos x$, $du=-\sin x\,dx$: $=-\int(1-u^2)\,du=-u+\frac{u^3}{3}+C=-\cos x+\frac{\cos^3 x}{3}+C$.

#### Trig substitution (clearing roots)

$$\sqrt{a^2-x^2}:x=a\sin\theta,\quad \sqrt{a^2+x^2}:x=a\tan\theta,\quad \sqrt{x^2-a^2}:x=a\sec\theta$$

Each choice turns the root into a single trig function via a Pythagorean identity (§s2). For example, with $x=a\sin\theta$, $\sqrt{a^2-x^2}=\sqrt{a^2-a^2\sin^2\theta}=a\sqrt{\cos^2\theta}=a\cos\theta$. (Complete the square first if the expression is $\sqrt{x^2+bx+c}$.)

**Worked example.** $\int\frac{dx}{\sqrt{1-x^2}}$ with $x=\sin\theta$, $dx=\cos\theta\,d\theta$: $=\int\frac{\cos\theta}{\cos\theta}\,d\theta=\int d\theta=\theta+C=\arcsin x+C$ — recovering the table entry of §s17.

#### A reduction formula

$$\int\sin^n x\,dx=-\frac{\sin^{n-1}x\cos x}{n}+\frac{n-1}{n}\int\sin^{n-2}x\,dx$$

Derived by integration by parts (§s18), it lowers the power by $2$ each time until it reaches a base case ($\int\sin x\,dx$ or $\int 1\,dx$). Such **recursions** tame high powers systematically.

**Worked example.** For $n=2$: $\int\sin^2 x\,dx=-\frac{\sin x\cos x}{2}+\frac12\int 1\,dx=-\frac{\sin x\cos x}{2}+\frac{x}{2}+C$ (equivalently $\frac{x}{2}-\frac{\sin2x}{4}+C$).

<a id="s20"></a>
### Improper integrals

**What this section says and why we care.** Some integrals have an infinite bound, or the function blows up inside the interval. We give them meaning as **limits** of ordinary integrals.

#### Definition by limit

$$\int_a^\infty f\,dx=\lim_{t\to\infty}\int_a^t f\,dx$$

We integrate up to a finite cutoff $t$, then let $t\to\infty$. The integral **converges** if this limit is a finite number, and **diverges** if it is infinite or fails to exist. A blow-up at a point inside the interval is handled the same way, by splitting the interval and taking a one-sided limit toward the bad point.

**Worked example.** $\int_1^\infty\frac{dx}{x^2}=\lim_{t\to\infty}\left[-\frac1x\right]_1^t=\lim_{t\to\infty}\left(-\frac1t+1\right)=1$. Converges. By contrast $\int_1^\infty\frac{dx}{x}=\lim_{t\to\infty}[\ln x]_1^t=\lim_{t\to\infty}\ln t=\infty$. Diverges.

#### The p-test (the benchmark)

$$\int_1^\infty\frac{dx}{x^p}\ \text{converges}\iff p>1,\qquad \int_0^1\frac{dx}{x^p}\ \text{converges}\iff p<1$$

These two benchmark families are worth memorizing because comparison tests measure other integrals against them. (The two worked examples above are the cases $p=2$ and $p=1$ of the first family, confirming the rule.)

> **Principle — comparison & absolute convergence**
>
> You can judge convergence without evaluating. **Comparison test:** if $0\le f\le g$ and $\int g$ converges, then $\int f$ converges (smaller positive area under a finite one is finite). **Limit comparison:** if $f/g$ tends to a finite positive number, $\int f$ and $\int g$ converge or diverge together. **Absolute convergence:** if $\int|f|$ converges, then $\int f$ converges.

**Worked example (comparison).** $\int_1^\infty\frac{dx}{x^2+1}$ converges because $\frac{1}{x^2+1}\le\frac{1}{x^2}$ and $\int_1^\infty\frac{dx}{x^2}=1$ converges.

<a id="s21"></a>
### Numerical integration

**What this section says and why we care.** Many integrals have no antiderivative expressible in elementary functions (e.g. $\int e^{-x^2}dx$). We then approximate the value directly from sampled heights.

#### Trapezoidal rule

$$\int_a^b f\,dx\approx\frac{\Delta x}{2}\big[f_0+2f_1+2f_2+\cdots+2f_{n-1}+f_n\big]$$

Here we sample at $n+1$ equally spaced points $x_0=a,\dots,x_n=b$ with $\Delta x=\frac{b-a}{n}$ and write $f_i=f(x_i)$. We replace each strip's curved top by a straight line, making each strip a trapezoid; the formula sums their areas. (Interior heights are doubled because each is shared by two adjacent trapezoids.) The error shrinks like $1/n^2$.

**Worked example.** Approximate $\int_0^1 x^2\,dx$ with $n=2$ ($\Delta x=0.5$): heights $f_0=0,f_1=0.25,f_2=1$. Estimate $=\frac{0.5}{2}[0+2(0.25)+1]=0.25\cdot1.5=0.375$. (Exact value $\tfrac13\approx0.333$; the overestimate is expected since $x^2$ is concave up.)

#### Simpson's rule (n even)

$$\int_a^b f\,dx\approx\frac{\Delta x}{3}\big[f_0+4f_1+2f_2+4f_3+\cdots+4f_{n-1}+f_n\big]$$

Simpson's rule fits **parabolas** through points in pairs of strips (so $n$ must be even), giving far more accuracy; the error shrinks like $1/n^4$. The coefficient pattern is $1,4,2,4,2,\dots,4,1$.

**Worked example.** Same integral $\int_0^1 x^2\,dx$ with $n=2$: $\frac{0.5}{3}[0+4(0.25)+1]=\frac{0.5}{3}\cdot2=\frac13$ — exact, because Simpson is exact for quadratics.

## Part F · Applications of the integral

<a id="s22"></a>
### Volumes, arc length & surface area

**What this section says and why we care.** Every geometric quantity here follows one recipe: describe one infinitesimally thin slice, then integrate (sum) the slices. This is the §s14 idea applied to volume, length, and surface.

#### Volumes of revolution

$$\text{disk/washer: } V=\pi\int_a^b\!\big([R]^2-[r]^2\big)dx,\qquad \text{shell: } V=2\pi\int_a^b x\,f(x)\,dx$$

When a region is spun about an axis it sweeps out a solid. The **disk/washer method** slices perpendicular to the axis; each slice is a disk (or a washer with outer radius $R$ and inner radius $r$) of area $\pi(R^2-r^2)$ and thickness $dx$. The **shell method** slices into thin cylindrical shells of radius $x$, height $f(x)$, thickness $dx$, surface $2\pi x f(x)$.

**Worked example.** Spin $y=\sqrt x$, $0\le x\le4$, about the $x$-axis. Disks of radius $R=\sqrt x$: $V=\pi\int_0^4(\sqrt x)^2\,dx=\pi\int_0^4 x\,dx=\pi\cdot\frac{x^2}{2}\Big|_0^4=\pi\cdot8=8\pi$.

#### General solids by cross-section

$$V=\int_a^b A(x)\,dx$$

If you know the area $A(x)$ of each cross-sectional slice (square, triangle, semicircle, …), simply integrate it: stacking slices of area $A(x)$ and thickness $dx$ totals the volume.

#### Arc length & surface of revolution

$$L=\int_a^b\sqrt{1+[f'(x)]^2}\,dx,\qquad S=2\pi\int_a^b f(x)\sqrt{1+[f'(x)]^2}\,dx$$

#### Demonstration — the arc-length integrand

1. A tiny piece of curve has horizontal run $dx$ and vertical rise $dy$. By the Pythagorean theorem its length is $ds=\sqrt{dx^2+dy^2}$.
2. Factor $dx$ out of the square root: $ds=\sqrt{1+(dy/dx)^2}\,dx=\sqrt{1+[f'(x)]^2}\,dx$. Integrating $ds$ from $a$ to $b$ totals the length. For a surface of revolution, multiply each $ds$ by the circumference $2\pi f(x)$ it sweeps as it rotates, giving $S$.

**Worked example.** Length of $y=\tfrac23 x^{3/2}$ from $x=0$ to $x=3$: $f'(x)=x^{1/2}$, so $1+[f']^2=1+x$ and $L=\int_0^3\sqrt{1+x}\,dx=\frac{2}{3}(1+x)^{3/2}\big|_0^3=\frac23(8-1)=\frac{14}{3}$.

## Part G · Sequences & series

<a id="s23"></a>
### Sequences

**What this section says and why we care.** A **sequence** is an ordered, infinite list of numbers $a_1,a_2,a_3,\dots$. The central question is where the list heads as you go further out — its limit.

> **Concept — convergence of a sequence**
>
> $a_n\to L$ (the sequence **converges** to $L$) means the terms get and stay arbitrarily close to $L$ as $n$ grows (the $\varepsilon$–$\delta$ idea of §s3 with $n\to\infty$). A sequence that is **bounded** (stays within fixed limits) and **monotonic** (always non-increasing, or always non-decreasing) must converge — the Monotone Convergence principle. Sequence limits obey the same laws as function limits.

**Three key sequence limits**

$$\lim_{n\to\infty}r^n=0\ (|r|<1),\qquad \lim_{n\to\infty}n^{1/n}=1,\qquad \lim_{n\to\infty}\Big(1+\frac xn\Big)^n=e^x$$

The first: repeatedly multiplying by a number smaller than $1$ in size drives the result to $0$ (e.g. $0.5^{10}\approx0.001$). The third is the continuous-compounding definition of $e^x$ generalizing the $e$ of §s8.

**Worked example.** $a_n=\frac{2n+1}{n}$. Divide top and bottom by $n$: $a_n=2+\frac1n\to2$. The sequence converges to $2$.

<a id="s24"></a>
### Series & convergence tests

**What this section says and why we care.** A **series** is the sum of all terms of a sequence, $\sum_{n=1}^\infty a_n$. Adding infinitely many numbers may give a finite total or may blow up; this section is the full toolkit for deciding which.

A series' value is defined as the limit of its **partial sums** $S_N=a_1+\cdots+a_N$ as $N\to\infty$ — connecting series back to §s23.

#### Geometric series & p-series

$$\sum_{n=0}^\infty ar^n=\frac{a}{1-r}\ (|r|<1),\qquad \sum_{n=1}^\infty\frac1{n^p}\ \text{converges}\iff p>1$$

A **geometric series** multiplies by a fixed ratio $r$ each step; it converges exactly when $|r|<1$. A **p-series** sums reciprocal powers; it mirrors the improper-integral p-test of §s20.

#### Demonstration — the geometric sum

1. Let $S_n=a+ar+\cdots+ar^{n-1}$. Multiply by $r$: $rS_n=ar+ar^2+\cdots+ar^n$. Subtract: $S_n-rS_n=a-ar^n$ (the middle terms telescope, §s14).
2. So $S_n(1-r)=a(1-r^n)$, giving $S_n=\frac{a(1-r^n)}{1-r}$. If $|r|<1$ then $r^n\to0$ (§s23), so $S_n\to\frac{a}{1-r}$.

**Worked example.** $\sum_{n=0}^\infty\left(\tfrac12\right)^n=\frac{1}{1-\tfrac12}=2$ (here $a=1$, $r=\tfrac12$). Concretely $1+\tfrac12+\tfrac14+\tfrac18+\cdots=2$.

| Test | Use it when… |
| --- | --- |
| nth-term (divergence) | $\lim a_n\neq0$ ⟹ diverges (a quick first check) |
| Ratio | factorials or $n$th powers; converges if $\lim\vert a_{n+1}/a_n\vert <1$ |
| Root | whole expression raised to the $n$; converges if $\lim\vert a_n\vert ^{1/n}<1$ |
| Comparison / limit comparison | terms resemble a known series |
| Integral | $a_n=f(n)$ with $f$ positive, decreasing |
| Alternating | signs alternate and $\vert a_n\vert $ decreases to 0 |

**Worked example (ratio test).** For $\sum\frac{1}{n!}$: $\frac{a_{n+1}}{a_n}=\frac{n!}{(n+1)!}=\frac{1}{n+1}\to0<1$, so the series converges (in fact to $e$, §s25).

> **Principle — absolute vs conditional convergence**
>
> If $\sum|a_n|$ converges, the series converges **absolutely** (and you may reorder its terms freely without changing the sum). If $\sum a_n$ converges but $\sum|a_n|$ does not, it converges **conditionally** — fragile, and reordering can change the sum (the alternating harmonic series $1-\tfrac12+\tfrac13-\cdots$ is the classic example).

<a id="s25"></a>
### Taylor & power series

**What this section says and why we care.** The climax of single-variable calculus: any sufficiently smooth function can be rebuilt as an infinite polynomial whose coefficients come from its derivatives. This is how calculators compute $\sin$, $e^x$, and the rest.

#### Taylor's theorem with remainder

$$f(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k+R_n,\qquad R_n=\frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$$

Here $f^{(k)}(a)$ is the $k$-th derivative at the center $a$, and $k!$ ("$k$ factorial") $=k\cdot(k-1)\cdots2\cdot1$. The sum is the **Taylor polynomial**; $R_n$ is the **remainder** (error), with $c$ some point between $a$ and $x$. The remainder bound is what makes Taylor series *usable* for guaranteed-accurate estimates, not just elegant.

#### Demonstration — why the coefficients are $f^{(n)}(a)/n!$

1. Assume $f(x)=\sum_k c_k(x-a)^k$. Setting $x=a$ kills every term with a factor $(x-a)$, leaving $c_0=f(a)$.
2. Differentiate $n$ times (using the power rule repeatedly) and then set $x=a$. Every term below degree $n$ has differentiated to $0$, and every term above still carries a factor $(x-a)$ which vanishes at $a$; only the degree-$n$ term survives, contributing $n!\,c_n$. Hence $f^{(n)}(a)=n!\,c_n$, i.e. $c_n=\frac{f^{(n)}(a)}{n!}$.

#### The famous expansions

$$e^x=\sum\frac{x^n}{n!},\quad \sin x=x-\frac{x^3}{3!}+\cdots,\quad \cos x=1-\frac{x^2}{2!}+\cdots$$

$$\frac1{1-x}=\sum x^n,\quad \ln(1+x)=x-\frac{x^2}2+\cdots,\quad (1+x)^k=\sum\binom{k}{n}x^n$$

**Worked example.** Estimate $e^{0.1}$ with the first three terms of $e^x=1+x+\frac{x^2}{2}+\cdots$: $1+0.1+\frac{0.01}{2}=1.105$. (True $e^{0.1}\approx1.10517$.) The next term $\frac{x^3}{6}\approx0.000167$ bounds the small remaining error.

> **Concept — radius of convergence**
>
> A power series $\sum c_n(x-a)^n$ converges only within a distance $R$ of its center $a$ — the **radius of convergence**, usually found by the ratio test (§s24) — and the two endpoints must be checked separately. Inside that interval you may **differentiate and integrate term by term**, the easiest way to manufacture new series from known ones.

**Worked example (radius).** For $\frac{1}{1-x}=\sum x^n$, the ratio test gives $\left|\frac{x^{n+1}}{x^n}\right|=|x|<1$, so $R=1$: the series converges for $-1<x<1$, matching the geometric condition of §s24.

## Part H · Further topics

<a id="s26"></a>
### Parametric equations

**What this section says and why we care.** Instead of $y$ as a function of $x$, we describe a curve by a moving point $(x(t),y(t))$ tracked by a parameter $t$ (often time). This naturally handles paths, loops, and motion that a single $y=f(x)$ cannot.

#### Slope, second derivative, arc length

$$\frac{dy}{dx}=\frac{dy/dt}{dx/dt},\qquad L=\int_{t_1}^{t_2}\sqrt{\Big(\tfrac{dx}{dt}\Big)^2+\Big(\tfrac{dy}{dt}\Big)^2}\,dt$$

The slope formula is the chain rule (§s7) rearranged: $\frac{dy}{dx}=\frac{dy}{dt}\div\frac{dx}{dt}$. The arc-length integrand is again $ds=\sqrt{dx^2+dy^2}$ from §s22, now with both $dx$ and $dy$ expressed through $t$ — speed integrated over time gives distance travelled.

**Worked example.** The unit circle $x=\cos t$, $y=\sin t$, $0\le t\le2\pi$: $\frac{dx}{dt}=-\sin t$, $\frac{dy}{dt}=\cos t$, so $L=\int_0^{2\pi}\sqrt{\sin^2 t+\cos^2 t}\,dt=\int_0^{2\pi}1\,dt=2\pi$ — the known circumference.

<a id="s27"></a>
### Polar coordinates

**What this section says and why we care.** Polar coordinates locate a point by its distance $r$ from the origin and its angle $\theta$, instead of horizontal/vertical position $x,y$. Many curves (circles, spirals, flowers) are far simpler in polar form.

#### Conversion

$$x=r\cos\theta,\quad y=r\sin\theta,\quad r^2=x^2+y^2,\quad \tan\theta=\frac yx$$

These come straight from the unit-circle definitions of §s2 scaled by the radius $r$. The first two go polar→rectangular; the last two go rectangular→polar.

#### Area enclosed by a polar curve

$$A=\frac12\int_\alpha^\beta r(\theta)^2\,d\theta$$

The thin slice here is a circular **sector** (a pie wedge) of angle $d\theta$ and radius $r$, whose area is $\tfrac12 r^2\,d\theta$ — not a rectangle. Same "sum tiny slices" principle as §s14, new slice shape.

**Worked example.** Area of the circle $r=2$: $A=\frac12\int_0^{2\pi}2^2\,d\theta=\frac12\cdot4\cdot2\pi=4\pi$, matching $\pi r^2=\pi\cdot2^2$.

<a id="s28"></a>
### Complex numbers & Euler's identity

**What this section says and why we care.** Allowing a "number" $i$ whose square is $-1$ unifies exponentials and trigonometry — they turn out to be the same thing viewed from different angles.

#### Basics & polar form

$$i^2=-1,\quad z=a+bi=r(\cos\theta+i\sin\theta)=re^{i\theta}$$

A **complex number** $z=a+bi$ has a **real part** $a$ and an **imaginary part** $b$; we plot it at point $(a,b)$. Its distance from the origin is $r=\sqrt{a^2+b^2}$ (the **modulus**) and its angle is $\theta$ (the **argument**), giving the **polar form** $r(\cos\theta+i\sin\theta)$.

#### Euler's formula, De Moivre & the identity

$$e^{i\theta}=\cos\theta+i\sin\theta,\quad (\cos\theta+i\sin\theta)^n=\cos n\theta+i\sin n\theta,\quad e^{i\pi}+1=0$$

**Euler's formula** is the first equation; **De Moivre's theorem** (the second) follows from it by raising to the $n$-th power, since $\big(e^{i\theta}\big)^n=e^{in\theta}$. The third, **Euler's identity**, is the case $\theta=\pi$: $e^{i\pi}=\cos\pi+i\sin\pi=-1$, so $e^{i\pi}+1=0$ — linking the five constants $e,i,\pi,1,0$.

> **The unity**
>
> Substitute $x=i\theta$ into the Taylor series for $e^x$ (§s25). The powers of $i$ cycle $i,-1,-i,1,\dots$, so the terms regroup into exactly the real $\cos\theta$ series and $i$ times the $\sin\theta$ series, yielding $e^{i\theta}=\cos\theta+i\sin\theta$. The series built from derivatives ties exponential growth to oscillation.

<a id="s29"></a>
### Differential equations

**What this section says and why we care.** A **differential equation** relates a function to its own derivatives. It is the language calculus speaks to physics, biology, and engineering, where laws naturally describe rates of change.

> **Concept — what a differential equation is**
>
> It is an equation involving an unknown function and its derivatives; **solving** it means finding the function. The simplest important one, **exponential growth/decay** $\frac{dy}{dt}=ky$, says the rate of change is proportional to the current amount; its solution is $y=y_0 e^{kt}$, where $y_0$ is the starting value. (Check: $y'=k y_0 e^{kt}=ky$.)

#### Separable equations

$$\frac{dy}{dx}=g(x)h(y)\ \Rightarrow\ \int\frac{dy}{h(y)}=\int g(x)\,dx$$

If the right side factors into an $x$-part times a $y$-part, **separate** the variables (gather $y$'s with $dy$, $x$'s with $dx$) and integrate each side.

**Worked example.** $\frac{dy}{dx}=xy$: separate to $\frac{dy}{y}=x\,dx$, integrate to $\ln|y|=\frac{x^2}{2}+C$, exponentiate to $y=A e^{x^2/2}$ (with $A=\pm e^{C}$).

#### First-order linear (integrating factor)

$$y'+P(x)y=Q(x),\qquad \mu=e^{\int P\,dx},\qquad (\mu y)'=\mu Q$$

For this form, multiply through by the **integrating factor** $\mu=e^{\int P\,dx}$. The trick is that the left side becomes the exact derivative $(\mu y)'$ (by the product rule, §s7, since $\mu'=P\mu$), so we can integrate both sides directly: $\mu y=\int\mu Q\,dx$.

#### Constant-coefficient homogeneous

$$ay''+by'+cy=0 \ \Rightarrow\ ar^2+br+c=0$$

Guessing $y=e^{rx}$ turns the differential equation into the **characteristic quadratic** $ar^2+br+c=0$ (because $y'=re^{rx}$, $y''=r^2 e^{rx}$, and $e^{rx}$ cancels). Its roots decide the solution: two distinct real roots give $e^{r_1 x},e^{r_2 x}$; a repeated root gives $e^{rx}$ and $x e^{rx}$; complex roots $\alpha\pm\beta i$ give $e^{\alpha x}\cos\beta x$ and $e^{\alpha x}\sin\beta x$ (oscillation, via Euler's formula §s28).

**Worked example.** $y''-5y'+6y=0$: characteristic $r^2-5r+6=(r-2)(r-3)=0$, roots $2,3$. General solution $y=C_1 e^{2x}+C_2 e^{3x}$.

<a id="beyond"></a>
### What comes next

This guide covers the standard **single-variable** course, the scope of the Princeton review book. The same two ideas — slope and accumulation — generalize:

- **Multivariable calculus:** partial derivatives $\partial f/\partial x$ (the slope in one direction while holding others fixed), the gradient $\nabla f$ (the vector of all partials, pointing uphill), and double/triple integrals $\iint,\iiint$ (accumulation over areas and volumes).
- **Vector calculus:** Green's, Stokes', and the Divergence theorems — each a higher-dimensional Fundamental Theorem, again saying that behavior on a boundary is governed by behavior inside.

> **The habit to keep**
>
> Whenever you meet a new formula, ask which earlier one it is secretly a version of — and try to reproduce its demonstration. Nearly everything in calculus is built from limits (§s3), the product rule (§s7), and the chain rule (§s7).

---

*Structured to follow Adrian Banner's *The Calculus Lifesaver: All the Tools You Need to Excel at Calculus* (Princeton University Press) — a single-variable companion covering concepts, principles, formulas, and the demonstrations behind them. Read once for the shape; return to any box as a reference.*
