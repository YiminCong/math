# Calculus, *made rigorous.*

The companion that goes underneath the formulas. Here every limit is an $\varepsilon$, every theorem is **stated precisely and proved**, and the whole edifice — continuity, derivatives, integrals, series — is rebuilt from one foundation: the **completeness** of the real numbers.

[← Back to all guides](../README.md)

## Part A · Numbers & sequences

<a id="s0"></a>
### The big picture: why rigor, and the role of $\varepsilon$

Calculus computes with infinity. Analysis is the discipline that makes those computations *true* rather than merely suggestive.

For two centuries calculus ran on intuition about "infinitely small" quantities. It worked spectacularly — and it also produced paradoxes: divergent series summed to nonsense, "continuous" functions with no derivative anywhere, and arguments that proved $1=0$. The nineteenth-century project of **Cauchy, Weierstrass, Bolzano, Dedekind** and others replaced the vague infinitesimal with a single precise idea: the **limit**, defined by $\varepsilon$.

> **Principle — what "rigor" buys you**
>
> The informal idea "$f(x)$ gets close to $L$ as $x$ gets close to $a$" hides the questions: *how* close, and *who chooses first?* The $\varepsilon$–$\delta$ definition answers both: **an adversary names a tolerance $\varepsilon>0$, and you must produce a $\delta$ that meets it.** Every theorem of calculus becomes a guarantee you can actually deliver on, not a picture you hope is right.

> **Concept — the one foundation: completeness**
>
> The rationals $\mathbb{Q}$ have a hole at $\sqrt 2$; the sequence $1,1.4,1.41,1.414,\dots$ "wants" to converge but has nowhere in $\mathbb{Q}$ to land. The real numbers $\mathbb{R}$ are built precisely to have **no holes**. That single property — **completeness** — is the engine behind every existence theorem ahead: that bounded monotone sequences converge, that continuous functions attain maxima, that integrals exist.

#### The whole subject on one line

> Real numbers & completeness → limits of sequences → continuity → derivatives → integrals → series of functions → power series

> **Connection — this guide vs. the others**
>
> The *Complete Calculus* and *Derived from Scratch* guides tell you the rules and show you the manipulations. This guide answers the next question — **why are those rules valid?** Whenever you used a limit, a continuity assumption, or "$dx$," there was a theorem underneath; here we name it and prove it.

<a id="s1"></a>
### The real numbers: ordered field, completeness & the supremum

*Everything rests on knowing exactly what $\mathbb{R}$ is. It is the unique complete ordered field — and the word "complete" is what distinguishes it from $\mathbb{Q}$.*

**The ordered-field axioms**

*$\mathbb{R}$ is a **field**: $+$ and $\cdot$ are associative, commutative, distributive, with identities $0,1$ and inverses ($-x$, and $x^{-1}$ for $x\ne 0$). It is **ordered**: a relation $\lt$ that is total, transitive, respects addition ($a\lt b\Rightarrow a+c\lt b+c$) and respects multiplication by positives ($a\lt b,\ c\gt 0\Rightarrow ac\lt bc$). The rationals $\mathbb{Q}$ satisfy all of this too — so the axioms so far do *not* single out $\mathbb{R}$.*

**Bounds, supremum & infimum**

$$u \text{ is an upper bound of } S \iff \forall x\in S,\ x\le u.$$

$$\sup S = \text{the } least \text{ upper bound of } S;\qquad \inf S = \text{the } greatest \text{ lower bound.}$$

*$M=\sup S$ means: (i) $M$ is an upper bound, and (ii) for every $\varepsilon>0$ there is $x\in S$ with $x\gt M-\varepsilon$ (nothing smaller than $M$ works as a bound). This characterization is used in nearly every proof below.*

> **Axiom — completeness (the least-upper-bound property)**
>
> This is the defining axiom of $\mathbb{R}$: **every nonempty subset of $\mathbb{R}$ that is bounded above has a supremum in $\mathbb{R}$.** The set $\{x\in\mathbb{Q}: x^2\lt 2\}$ is bounded above but has no supremum *in $\mathbb{Q}$* — its would-be sup is $\sqrt 2$, which is missing. Completeness says $\mathbb{R}$ has no such gaps.

**Proof — the Archimedean property: $\mathbb{N}$ is unbounded in $\mathbb{R}$**

1. Claim: for every $x\in\mathbb{R}$ there is $n\in\mathbb{N}$ with $n\gt x$. Suppose not — then $\mathbb{N}$ is bounded above.
2. Since $\mathbb{N}\ne\varnothing$ is bounded above, completeness gives $s=\sup\mathbb{N}\in\mathbb{R}$.
3. Then $s-1$ is not an upper bound (it is less than the least one), so some $m\in\mathbb{N}$ satisfies $m\gt s-1$, i.e. $m+1\gt s$.

   $$m+1\in\mathbb{N}\ \text{yet}\ m+1\gt s=\sup\mathbb{N}.$$
4. That contradicts $s$ being an upper bound of $\mathbb{N}$. Hence $\mathbb{N}$ is unbounded.

*Corollary: for any $\varepsilon>0$ there is $n$ with $1/n\lt\varepsilon$ (take $n\gt 1/\varepsilon$). This tiny fact is what lets $1/n\to 0$ drive countless limits. $\blacksquare$*

**Proof — $\mathbb{Q}$ is dense in $\mathbb{R}$**

1. Given $a\lt b$, we find a rational in $(a,b)$. By Archimedes pick $n$ with $1/n\lt b-a$, so $nb-na\gt 1$.
2. An interval of length greater than $1$ contains an integer: let $m$ be the least integer with $m\gt na$. Then $m-1\le na$, so $m\le na+1\lt nb$.
3. Thus $na\lt m\lt nb$, and dividing by $n$:

   $$a\lt \frac{m}{n}\lt b.$$

*Between any two reals lies a rational — the reason rational approximation works everywhere. $\blacksquare$*

> **Connection — why this comes first**
>
> Every "the limit exists" claim you took on faith in calculus is ultimately cashed out as a supremum produced by completeness. Lose this axiom and continuous functions can skip over zero, bounded sequences need not converge, and the integral may not exist. $\mathbb{R}$ is engineered so none of that happens.

<a id="s2"></a>
### Sequences and their limits (the $\varepsilon$–$N$ definition)

*The simplest infinite process. Master the $\varepsilon$–$N$ definition here and the $\varepsilon$–$\delta$ of continuity is the same idea with a different clock.*

**Definition — convergence of a sequence**

$$a_n \to L \iff \forall\varepsilon>0\ \ \exists N\in\mathbb{N}\ \ \forall n\ge N:\ \ |a_n-L|\lt\varepsilon.$$

*Read it as a game: the adversary picks any tolerance $\varepsilon$; you must name a threshold $N$ past which *all* terms sit within $\varepsilon$ of $L$. If you can always answer, the limit is $L$.*

**Proof — limits are unique**

1. Suppose $a_n\to L$ and $a_n\to L'$ with $L\ne L'$. Let $\varepsilon=\tfrac{|L-L'|}{2}\gt 0$.
2. Get $N_1$ with $|a_n-L|\lt\varepsilon$ for $n\ge N_1$, and $N_2$ with $|a_n-L'|\lt\varepsilon$ for $n\ge N_2$. For $n\ge\max(N_1,N_2)$, both hold.
3. Triangle inequality: i.e. $|L-L'|\lt|L-L'|$, impossible.

   $$|L-L'|\le|L-a_n|+|a_n-L'|\lt\varepsilon+\varepsilon=|L-L'|,$$

*A sequence cannot converge to two different values — "the" limit is well defined. $\blacksquare$*

**Proof — convergent sequences are bounded**

1. Let $a_n\to L$. Take $\varepsilon=1$: there is $N$ with $|a_n-L|\lt 1$, hence $|a_n|\lt|L|+1$ for all $n\ge N$.
2. Only finitely many terms remain: $a_1,\dots,a_{N-1}$. Set

   $$M=\max\big(|a_1|,\dots,|a_{N-1}|,\ |L|+1\big).$$
3. Then $|a_n|\le M$ for every $n$.

*Boundedness is necessary for convergence — though, as we'll see, not sufficient. $\blacksquare$*

**Theorem — the algebra of limits**

$$\text{If } a_n\to A,\ b_n\to B,\text{ then } a_n+b_n\to A+B,\ \ a_nb_n\to AB,\ \ \tfrac{a_n}{b_n}\to\tfrac{A}{B}\ (B\ne 0).$$

**Proof — the limit of a sum is the sum of limits**

1. Let $a_n\to A$, $b_n\to B$, and fix $\varepsilon>0$. The trick: spend half the budget on each sequence.
2. Choose $N_1$ so that $n\ge N_1\Rightarrow|a_n-A|\lt\tfrac{\varepsilon}{2}$, and $N_2$ so that $n\ge N_2\Rightarrow|b_n-B|\lt\tfrac{\varepsilon}{2}$.
3. For $n\ge N=\max(N_1,N_2)$, the triangle inequality gives

   $$|(a_n+b_n)-(A+B)|\le|a_n-A|+|b_n-B|\lt\tfrac{\varepsilon}{2}+\tfrac{\varepsilon}{2}=\varepsilon.$$

*The "$\varepsilon/2$ trick" — split the tolerance among the pieces — recurs throughout analysis. $\blacksquare$*

**Proof — the limit of a product is the product of limits**

1. Write the difference and insert a cross term:

   $$a_nb_n-AB=a_n b_n - a_n B + a_n B - AB = a_n(b_n-B)+B(a_n-A).$$
2. Since $(a_n)$ converges it is bounded: $|a_n|\le M$ for all $n$ (previous proof). So

   $$|a_nb_n-AB|\le M\,|b_n-B|+|B|\,|a_n-A|.$$
3. Given $\varepsilon>0$, make $|b_n-B|\lt\dfrac{\varepsilon}{2M}$ and $|a_n-A|\lt\dfrac{\varepsilon}{2(|B|+1)}$ for large $n$; then the right side is $\lt\tfrac{\varepsilon}{2}+\tfrac{\varepsilon}{2}=\varepsilon$.

*Inserting $\pm a_nB$ is the "add and subtract" technique — the workhorse of multiplicative limit proofs. $\blacksquare$*

> **Connection — the rules you used informally**
>
> "The limit of a sum/product is the sum/product of limits" was a rule you applied without thought. It is a *theorem*, and this is its proof. The same statements for functions (Section 5) follow by exactly this argument with $\delta$ in place of $N$.

<a id="s3"></a>
### Monotone convergence, Bolzano–Weierstrass & Cauchy sequences

*Three existence theorems — each a different way completeness guarantees a limit you can't compute by hand.*

**Theorem — Monotone Convergence**

$$\text{Every bounded monotone sequence converges.}$$

*If $(a_n)$ is increasing and bounded above, then $a_n\to\sup\{a_n\}$; if decreasing and bounded below, $a_n\to\inf\{a_n\}$. Monotone *and* bounded is enough — you needn't know the limit in advance.*

**Proof — monotone & bounded $\Rightarrow$ convergent (via the supremum)**

1. Let $(a_n)$ be increasing and bounded above. The set $S=\{a_n:n\in\mathbb{N}\}$ is nonempty and bounded above, so by completeness $L=\sup S$ exists.
2. Fix $\varepsilon>0$. Since $L-\varepsilon$ is not an upper bound, some term $a_N\gt L-\varepsilon$.
3. Because the sequence increases, for all $n\ge N$: $a_N\le a_n\le L$. Therefore

   $$L-\varepsilon\lt a_N\le a_n\le L\lt L+\varepsilon\ \Rightarrow\ |a_n-L|\lt\varepsilon.$$

*This is the cleanest place to see completeness *create* a limit out of thin air. $\blacksquare$*

**Theorem — Bolzano–Weierstrass**

$$\text{Every bounded sequence in } \mathbb{R} \text{ has a convergent subsequence.}$$

**Proof — Bolzano–Weierstrass by bisection**

1. Let $(a_n)$ lie in $[A,B]$. Bisect: at least one half contains infinitely many terms — call it $I_1$, of length $\tfrac{B-A}{2}$. Pick $a_{n_1}\in I_1$.
2. Repeat: bisect $I_1$, keep a half $I_2$ with infinitely many terms (length $\tfrac{B-A}{4}$), and pick $a_{n_2}\in I_2$ with $n_2\gt n_1$. Continue, building nested intervals $I_1\supset I_2\supset\cdots$ with lengths $\to 0$.
3. The left endpoints increase and are bounded, so by Monotone Convergence they tend to a point $L$ (the unique point in all $I_k$, by the Nested Interval Property). Since $a_{n_k}\in I_k$ and $|I_k|\to 0$:

   $$|a_{n_k}-L|\le|I_k|=\frac{B-A}{2^{k}}\to 0.$$

*A bounded sequence may wander forever, but it must *cluster* somewhere. This is the compactness of $[A,B]$ in disguise. $\blacksquare$*

**Definition — Cauchy sequence**

$$(a_n) \text{ is Cauchy} \iff \forall\varepsilon>0\ \exists N\ \forall m,n\ge N:\ |a_n-a_m|\lt\varepsilon.$$

*The terms eventually cluster among *themselves* — no mention of a limit $L$. This lets you prove convergence without knowing the target.*

**Proof — every convergent sequence is Cauchy**

1. Suppose $a_n\to L$ and fix $\varepsilon>0$. Choose $N$ with $|a_n-L|\lt\tfrac{\varepsilon}{2}$ for all $n\ge N$.
2. For any $m,n\ge N$, route through $L$:

   $$|a_n-a_m|\le|a_n-L|+|L-a_m|\lt\tfrac{\varepsilon}{2}+\tfrac{\varepsilon}{2}=\varepsilon.$$

*Convergence $\Rightarrow$ Cauchy is easy and holds in any metric space. $\blacksquare$*

**Proof — every Cauchy sequence in $\mathbb{R}$ converges (completeness of $\mathbb{R}$)**

1. A Cauchy sequence is bounded: take $\varepsilon=1$, get $N$ with $|a_n-a_N|\lt 1$ for $n\ge N$, then bound as in Section 2.
2. By Bolzano–Weierstrass it has a convergent subsequence $a_{n_k}\to L$.
3. Now show the whole sequence $\to L$. Fix $\varepsilon>0$; get $N$ with $|a_n-a_m|\lt\tfrac{\varepsilon}{2}$ for $m,n\ge N$, and pick $n_k\ge N$ with $|a_{n_k}-L|\lt\tfrac{\varepsilon}{2}$. For $n\ge N$:

   $$|a_n-L|\le|a_n-a_{n_k}|+|a_{n_k}-L|\lt\tfrac{\varepsilon}{2}+\tfrac{\varepsilon}{2}=\varepsilon.$$

*In $\mathbb{R}$, Cauchy $\iff$ convergent. This **Cauchy criterion** is "completeness" restated for sequences, and underlies the convergence of series and integrals. $\blacksquare$*

<a id="s4"></a>
### Limit superior & limit inferior

Even sequences that don't converge have a "ceiling" and "floor" of long-run behavior — and these *always* exist.

**Definition — $\limsup$ and $\liminf$**

$$\limsup_{n\to\infty} a_n=\lim_{n\to\infty}\Big(\sup_{k\ge n} a_k\Big),\qquad \liminf_{n\to\infty} a_n=\lim_{n\to\infty}\Big(\inf_{k\ge n} a_k\Big).$$

*Let $s_n=\sup_{k\ge n}a_k$. As $n$ grows we sup over a smaller tail, so $s_n$ is decreasing; if bounded below it converges (Monotone Convergence) — that limit is $\limsup$. For a bounded sequence both always exist in $\mathbb{R}$.*

> **Concept — what they capture**
>
> $\limsup a_n$ is the largest value the sequence approaches infinitely often (its biggest subsequential limit); $\liminf a_n$ is the smallest. For $a_n=(-1)^n$: $\limsup=1$, $\liminf=-1$. They pin down a sequence's eventual range even when no single limit exists.

**Proof — $a_n\to L \iff \limsup a_n=\liminf a_n=L$**

1. ($\Rightarrow$) If $a_n\to L$, then for $\varepsilon>0$ all terms past some $N$ lie in $(L-\varepsilon,L+\varepsilon)$, so for $n\ge N$ both $\sup_{k\ge n}a_k$ and $\inf_{k\ge n}a_k$ lie in $[L-\varepsilon,L+\varepsilon]$. Letting $\varepsilon\to 0$ forces both to $L$.
2. ($\Leftarrow$) Suppose $\liminf=\limsup=L$. Always $\inf_{k\ge n}a_k\le a_n\le\sup_{k\ge n}a_k$.

   $$\liminf a_n\ \le\ a_n\ \le\ \limsup a_n.$$
3. The outer two both tend to $L$, so by the Squeeze Theorem $a_n\to L$.

*Convergence is exactly the collapse of the gap between the eventual ceiling and floor. $\blacksquare$*

> **Connection — the root and ratio tests**
>
> The convergence tests for series you used (root test, ratio test) are stated rigorously with $\limsup$: a series $\sum a_n$ converges absolutely if $\limsup|a_n|^{1/n}\lt 1$. Because $\limsup$ always exists, these tests always have something to say — even for erratic terms.

## Part B · Continuity & differentiation

<a id="s5"></a>
### Limits of functions and continuity ($\varepsilon$–$\delta$)

*The same game as $\varepsilon$–$N$, now with input distance $\delta$ controlling output distance $\varepsilon$.*

**Definition — limit of a function**

$$\lim_{x\to a} f(x)=L \iff \forall\varepsilon>0\ \exists\delta>0:\ 0\lt|x-a|\lt\delta\ \Rightarrow\ |f(x)-L|\lt\varepsilon.$$

*"$0\lt|x-a|$" excludes $x=a$ itself: the limit is about approach, not the value at $a$.*

**Definition — continuity at a point**

$$f \text{ continuous at } a \iff \forall\varepsilon>0\ \exists\delta>0:\ |x-a|\lt\delta\ \Rightarrow\ |f(x)-f(a)|\lt\varepsilon.$$

*Equivalently $\lim_{x\to a}f(x)=f(a)$: the limit exists, $f(a)$ is defined, and they agree. Now $x=a$ is allowed (it trivially satisfies the conclusion).*

**Proof — $f(x)=x^2$ is continuous at every $a$**

1. Fix $a$ and $\varepsilon>0$. We must control $|x^2-a^2|=|x-a|\,|x+a|$.
2. Restrict the search to $|x-a|\lt 1$; then $|x|\lt|a|+1$, so $|x+a|\le|x|+|a|\lt 2|a|+1$.
3. Choose $\delta=\min\!\Big(1,\ \dfrac{\varepsilon}{2|a|+1}\Big)$. Then $|x-a|\lt\delta$ gives

   $$|x^2-a^2|=|x-a|\,|x+a|\lt\frac{\varepsilon}{2|a|+1}\cdot(2|a|+1)=\varepsilon.$$

*The "bound the awkward factor first, then choose $\delta$" pattern handles most explicit $\varepsilon$–$\delta$ proofs. $\blacksquare$*

**Theorem — sequential criterion for continuity**

$$f \text{ continuous at } a \iff \big(x_n\to a \Rightarrow f(x_n)\to f(a)\big)\ \text{for every sequence } x_n.$$

*A bridge between Part A and Part B: it lets you reuse all sequence theorems for functions, and lets you *disprove* continuity by exhibiting one bad sequence.*

**Proof — composition of continuous functions is continuous**

1. Let $g$ be continuous at $a$ and $f$ continuous at $b=g(a)$; show $f\circ g$ is continuous at $a$. Fix $\varepsilon>0$.
2. By continuity of $f$ at $b$: there is $\eta>0$ with $|y-b|\lt\eta\Rightarrow|f(y)-f(b)|\lt\varepsilon$.
3. By continuity of $g$ at $a$: there is $\delta>0$ with $|x-a|\lt\delta\Rightarrow|g(x)-b|\lt\eta$. Chain them:

   $$|x-a|\lt\delta\ \Rightarrow\ |g(x)-b|\lt\eta\ \Rightarrow\ |f(g(x))-f(b)|\lt\varepsilon.$$

*Continuity passes through composition — the rigorous basis for differentiating composite functions. $\blacksquare$*

> **Connection — "you can plug in"**
>
> In the first calculus course, evaluating a limit by "plugging in" worked precisely *because* the function was continuous. Continuity is the formal statement that $\lim_{x\to a}f=f(a)$ — the permission slip for substitution.

<a id="s6"></a>
### Theorems on continuous functions: IVT, EVT & uniform continuity

*On a closed bounded interval, continuity is astonishingly strong. Three theorems show why — and all three need completeness.*

**Theorem — Intermediate Value Theorem (IVT)**

$$f \text{ continuous on } [a,b],\ \ f(a)\lt y\lt f(b)\ \Rightarrow\ \exists c\in(a,b):\ f(c)=y.$$

**Proof — IVT via the supremum**

1. WLOG $y=0$ with $f(a)\lt 0\lt f(b)$ (replace $f$ by $f-y$). Let $S=\{x\in[a,b]:f(x)\lt 0\}$. It is nonempty ($a\in S$) and bounded above by $b$, so $c=\sup S$ exists by completeness.
2. Suppose $f(c)\lt 0$. By continuity $f$ stays negative on a small interval around $c$, so points slightly right of $c$ are in $S$ — contradicting $c=\sup S$.
3. Suppose $f(c)\gt 0$. By continuity $f$ stays positive just left of $c$, so a smaller number is already an upper bound for $S$ — again contradicting $c=\sup S$. Hence

   $$f(c)=0.$$

*A continuous graph cannot jump across a value — proved, not drawn. This is the root of every root-finding bisection method. $\blacksquare$*

**Theorem — Extreme Value Theorem (EVT)**

$$f \text{ continuous on } [a,b]\ \Rightarrow\ f \text{ is bounded and attains a max and a min on } [a,b].$$

**Proof — EVT via Bolzano–Weierstrass**

1. Bounded: if not, there are $x_n\in[a,b]$ with $|f(x_n)|\to\infty$. By Bolzano–Weierstrass a subsequence $x_{n_k}\to x^*\in[a,b]$; continuity gives $f(x_{n_k})\to f(x^*)$, a finite number — contradicting $|f(x_{n_k})|\to\infty$.
2. Attained: let $M=\sup_{[a,b]}f$ (exists, now that $f$ is bounded). Pick $x_n$ with $f(x_n)\to M$.
3. By Bolzano–Weierstrass, $x_{n_k}\to c\in[a,b]$; continuity gives $f(c)=\lim f(x_{n_k})=M$. The min is identical applied to $-f$.

   $$f(c)=M=\max_{[a,b]}f.$$

*The closed, bounded interval (compactness) is essential: $f(x)=1/x$ on $(0,1]$ is continuous but unbounded. $\blacksquare$*

**Definition — uniform continuity**

$$f \text{ uniformly continuous on } I \iff \forall\varepsilon>0\ \exists\delta>0\ \forall x,y\in I:\ |x-y|\lt\delta\Rightarrow|f(x)-f(y)|\lt\varepsilon.$$

*The crucial difference from ordinary continuity: **one $\delta$ works for the whole interval at once** — it may not depend on the point. $f(x)=1/x$ on $(0,1)$ is continuous but not uniformly so: near 0 you need ever-tinier $\delta$.*

**Proof — Heine–Cantor: continuous on $[a,b]$ $\Rightarrow$ uniformly continuous**

1. Suppose not. Then there is $\varepsilon_0>0$ such that for every $\delta=\tfrac1n$ there exist $x_n,y_n\in[a,b]$ with $|x_n-y_n|\lt\tfrac1n$ yet $|f(x_n)-f(y_n)|\ge\varepsilon_0$.
2. By Bolzano–Weierstrass, a subsequence $x_{n_k}\to c\in[a,b]$. Since $|x_{n_k}-y_{n_k}|\lt\tfrac{1}{n_k}\to 0$, also $y_{n_k}\to c$.
3. By continuity at $c$, both $f(x_{n_k})\to f(c)$ and $f(y_{n_k})\to f(c)$, so their difference $\to 0$ — contradicting $|f(x_{n_k})-f(y_{n_k})|\ge\varepsilon_0$.

   $$0=\lim|f(x_{n_k})-f(y_{n_k})|\ge\varepsilon_0\gt 0.$$

*Compactness upgrades pointwise continuity to uniform — the fact that makes the Riemann integral of a continuous function exist (Section 8). $\blacksquare$*

> **Theorem — Heine–Borel (named)**
>
> A subset of $\mathbb{R}$ (or $\mathbb{R}^n$) is **compact** — every open cover has a finite subcover — *if and only if* it is **closed and bounded**. This is the abstract engine behind EVT and Heine–Cantor; "closed bounded interval" is the simplest compact set.

<a id="s7"></a>
### Differentiation: the Mean Value Theorem & Taylor's theorem with remainder

*The derivative is a limit; the MVT is the theorem that turns it into global information; Taylor's theorem quantifies the error of polynomial approximation.*

**Definition — the derivative**

$$f'(a)=\lim_{h\to 0}\frac{f(a+h)-f(a)}{h},$$

*when this limit exists. Differentiability is strictly stronger than continuity, as the next result shows.*

**Proof — differentiable $\Rightarrow$ continuous**

1. Suppose $f'(a)$ exists. For $x\ne a$ write

   $$f(x)-f(a)=\frac{f(x)-f(a)}{x-a}\cdot(x-a).$$
2. As $x\to a$, the first factor $\to f'(a)$ and the second $\to 0$; by the product rule for limits the product $\to f'(a)\cdot 0=0$.
3. Hence $\lim_{x\to a}f(x)=f(a)$, i.e. $f$ is continuous at $a$.

*The converse fails: $|x|$ is continuous but not differentiable at 0; Weierstrass's function is continuous *everywhere* yet differentiable *nowhere*. $\blacksquare$*

**Theorem — Rolle & the Mean Value Theorem**

$$\textbf{Rolle: } f\in C[a,b],\ \text{diff. on }(a,b),\ f(a)=f(b)\ \Rightarrow\ \exists c:\ f'(c)=0.$$

$$\textbf{MVT: } \exists c\in(a,b):\ f'(c)=\frac{f(b)-f(a)}{b-a}.$$

**Proof — Rolle's theorem, then the MVT from it**

1. Rolle: $f$ is continuous on $[a,b]$, so by EVT it attains a max and min. If both occur at endpoints then $f$ is constant and $f'\equiv 0$. Otherwise an extremum occurs at an interior point $c$.
2. At an interior extremum the one-sided difference quotients have opposite signs in the limit, forcing $f'(c)=0$ (Fermat's interior-extremum lemma).

   $$f'(c)=0.$$
3. MVT: apply Rolle to the auxiliary function that subtracts the secant line, which satisfies $g(a)=g(b)=0$. Rolle gives $c$ with $g'(c)=0$, i.e. $f'(c)=\dfrac{f(b)-f(a)}{b-a}$.

   $$g(x)=f(x)-\Big[f(a)+\frac{f(b)-f(a)}{b-a}(x-a)\Big],$$

*EVT $\to$ Fermat $\to$ Rolle $\to$ MVT: a chain straight back to completeness. $\blacksquare$*

**Proof — MVT consequence: $f'=0$ everywhere $\Rightarrow f$ constant**

1. Take any $x_1\lt x_2$ in the interval. Apply the MVT on $[x_1,x_2]$: there is $c$ with

   $$f(x_2)-f(x_1)=f'(c)\,(x_2-x_1).$$
2. Since $f'(c)=0$, the right side is $0$, so $f(x_2)=f(x_1)$. As $x_1,x_2$ were arbitrary, $f$ is constant.

*This is exactly why "$+C$" appears in every antiderivative — two antiderivatives of the same function differ by a constant. $\blacksquare$*

**Theorem — Taylor's theorem with Lagrange remainder**

$$f(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k+R_n,\qquad R_n=\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}$$

*for some $\xi$ between $a$ and $x$, assuming $f$ is $(n+1)$-times differentiable. The remainder is an *exact* error, and $n=0$ is precisely the MVT.*

> **Concept — Taylor is a higher-order MVT**
>
> Taylor's theorem is proved by the same device as the MVT: subtract the degree-$n$ Taylor polynomial, build an auxiliary function vanishing to high order at $a$ and $x$, and apply Rolle (or Cauchy's MVT) repeatedly. The Lagrange remainder is the leftover from one final application — generalizing $f'(c)$ to $f^{(n+1)}(\xi)$.

> **Connection — error bounds you trusted**
>
> When you approximated $\sin x\approx x-\tfrac{x^3}{6}$ and claimed "the error is tiny," the Lagrange remainder is the rigorous bound: $|R_n|\le\dfrac{\max|f^{(n+1)}|}{(n+1)!}|x-a|^{n+1}$. It's what makes Taylor series trustworthy, not just formal.

## Part C · Integration, series & beyond

<a id="s8"></a>
### The Riemann integral: Darboux sums & the integrability criterion

*"Area under the curve" becomes a precise number squeezed between over- and under-estimates. The integral exists exactly when the squeeze closes.*

**Definition — Darboux upper & lower sums**

$$L(f,P)=\sum_{i} m_i\,\Delta x_i,\quad U(f,P)=\sum_{i} M_i\,\Delta x_i,\quad m_i=\inf_{[x_{i-1},x_i]}f,\ M_i=\sup_{[x_{i-1},x_i]}f$$

*for a partition $P$ of $[a,b]$. $L$ under-estimates, $U$ over-estimates the area, using the true inf/sup on each subinterval.*

**Definition — the Riemann (Darboux) integral**

$$\underline{\int_a^b} f=\sup_P L(f,P),\qquad \overline{\int_a^b} f=\inf_P U(f,P).$$

$$f \text{ is integrable} \iff \underline{\int_a^b} f=\overline{\int_a^b} f,\ \text{the common value } \int_a^b f.$$

*Refining a partition raises $L$ and lowers $U$; the lower integral never exceeds the upper. Integrability means the gap can be driven to zero.*

**Theorem — Riemann's criterion**

$$f \text{ integrable on } [a,b] \iff \forall\varepsilon>0\ \exists\text{ partition } P:\ U(f,P)-L(f,P)\lt\varepsilon.$$

**Proof — every continuous $f$ on $[a,b]$ is integrable**

1. By Heine–Cantor (Section 6), $f$ is uniformly continuous on $[a,b]$. Fix $\varepsilon>0$ and choose $\delta$ so that $|x-y|\lt\delta\Rightarrow|f(x)-f(y)|\lt\dfrac{\varepsilon}{b-a}$.
2. Take any partition with all subintervals of width $\lt\delta$. On each, $M_i-m_i=\sup-\inf\le\dfrac{\varepsilon}{b-a}$ (the sup and inf are attained by EVT, at points within $\delta$).
3. Then

   $$U(f,P)-L(f,P)=\sum_i (M_i-m_i)\,\Delta x_i\le\frac{\varepsilon}{b-a}\sum_i\Delta x_i=\frac{\varepsilon}{b-a}\cdot(b-a)=\varepsilon.$$
4. By Riemann's criterion, $f$ is integrable.

*Uniform continuity is exactly what lets *one* mesh size control the oscillation everywhere at once. $\blacksquare$*

> **Concept — what fails to be integrable**
>
> The Dirichlet function (1 on rationals, 0 on irrationals) has $L=0$ but $U=b-a$ on every partition, since each subinterval contains both kinds of point — so it is *not* Riemann integrable. Riemann integrability requires the discontinuities to be "small" (measure zero, by Lebesgue's criterion). This limitation motivates Section 13.

<a id="s9"></a>
### The Fundamental Theorem of Calculus, proved

*The theorem that fuses the two halves of calculus: integration and differentiation are inverse operations. Both directions, proved.*

**FTC — Part I (differentiating an integral)**

$$f \text{ continuous on } [a,b],\quad F(x)=\int_a^x f(t)\,dt\ \Rightarrow\ F'(x)=f(x).$$

**Proof — FTC Part I**

1. Form the difference quotient and use additivity of the integral:

   $$\frac{F(x+h)-F(x)}{h}=\frac1h\int_x^{x+h} f(t)\,dt.$$
2. Let $m_h,M_h$ be the min and max of $f$ on $[x,x+h]$ (exist by EVT). Then $m_h\,h\le\int_x^{x+h}f\le M_h\,h$, so dividing by $h\gt 0$:

   $$m_h\le\frac{F(x+h)-F(x)}{h}\le M_h.$$
3. As $h\to 0$, continuity forces $m_h\to f(x)$ and $M_h\to f(x)$. By the Squeeze Theorem the difference quotient $\to f(x)$, i.e. $F'(x)=f(x)$.

*Every continuous function *has* an antiderivative — namely its own running integral. $\blacksquare$*

**FTC — Part II (evaluating an integral)**

$$G'=f \text{ on } [a,b],\ f \text{ integrable}\ \Rightarrow\ \int_a^b f(x)\,dx=G(b)-G(a).$$

**Proof — FTC Part II via the MVT**

1. Take any partition $a=x_0\lt x_1\lt\cdots\lt x_n=b$. Telescope:

   $$G(b)-G(a)=\sum_{i=1}^{n}\big(G(x_i)-G(x_{i-1})\big).$$
2. Apply the MVT to $G$ on each $[x_{i-1},x_i]$: there is $c_i$ with $G(x_i)-G(x_{i-1})=G'(c_i)\,\Delta x_i=f(c_i)\,\Delta x_i$.
3. So $G(b)-G(a)=\sum f(c_i)\,\Delta x_i$, a Riemann sum, trapped between $L(f,P)$ and $U(f,P)$:

   $$L(f,P)\le G(b)-G(a)\le U(f,P).$$
4. Since $f$ is integrable, refining $P$ squeezes both bounds to $\int_a^b f$. The constant $G(b)-G(a)$ is caught in the middle, so it equals $\int_a^b f$.

*The MVT (hence completeness) is the hinge: it converts increments of $G$ into samples of $f$. $\blacksquare$*

> **Connection — "find the antiderivative, plug in the endpoints"**
>
> The computational rule $\int_a^b f = G(b)-G(a)$ you used from day one *is* FTC Part II. Part I is its silent partner: it guarantees the antiderivative $G$ exists in the first place for any continuous $f$, so the rule always has something to apply.

<a id="s10"></a>
### Sequences & series of functions: pointwise vs uniform convergence

*When a limit is itself a function, "how" it converges matters enormously. The distinction between pointwise and uniform is where naïve calculus breaks.*

**Definition — pointwise convergence**

$$f_n\to f \text{ pointwise} \iff \forall x\ \forall\varepsilon>0\ \exists N(x,\varepsilon):\ n\ge N\Rightarrow|f_n(x)-f(x)|\lt\varepsilon.$$

*Here $N$ may depend on $x$ — different points may converge at wildly different rates.*

**Definition — uniform convergence**

$$f_n\to f \text{ uniformly} \iff \forall\varepsilon>0\ \exists N\ \forall x\ \forall n\ge N:\ |f_n(x)-f(x)|\lt\varepsilon.$$

$$\text{equivalently}\quad \sup_x|f_n(x)-f(x)|\to 0.$$

*One $N$ works for *all* $x$ simultaneously — the whole graph of $f_n$ lies in an $\varepsilon$-band around $f$. Quantifier order is everything: uniform moves "$\exists N$" in front of "$\forall x$."*

> **Concept — the cautionary example**
>
> On $[0,1]$, $f_n(x)=x^n$ converges pointwise to $f(x)=0$ for $x\lt 1$ and $f(1)=1$ — a **discontinuous** limit of continuous functions. The convergence is *not* uniform: near $x=1$ you always need a larger $n$. Pointwise convergence does not preserve continuity; uniform convergence will.

**Theorem — Weierstrass M-test**

$$|f_n(x)|\le M_n\ \forall x,\quad \sum_n M_n\lt\infty\ \Rightarrow\ \sum_n f_n \text{ converges uniformly (and absolutely).}$$

*A convergent numerical series of bounds forces uniform convergence of the function series — the everyday tool for proving power series converge uniformly.*

**Proof — the M-test (via the Cauchy criterion for uniform convergence)**

1. Let $S_n=\sum_{k=1}^n f_k$. For $m\gt n$ and any $x$:

   $$|S_m(x)-S_n(x)|=\Big|\sum_{k=n+1}^{m} f_k(x)\Big|\le\sum_{k=n+1}^{m}|f_k(x)|\le\sum_{k=n+1}^{m} M_k.$$
2. Since $\sum M_k$ converges, its tails $\to 0$: given $\varepsilon>0$ there is $N$ with $\sum_{k=n+1}^{m}M_k\lt\varepsilon$ for all $m\gt n\ge N$ — a bound independent of $x$.
3. Hence $\sup_x|S_m(x)-S_n(x)|\lt\varepsilon$: the partial sums are uniformly Cauchy, so they converge uniformly to some $S$.

*The numerical tail controls the function tail uniformly. $\blacksquare$*

<a id="s11"></a>
### Consequences of uniform convergence

*Uniform convergence is precisely the strength needed to interchange limits with continuity, integration, and (with care) differentiation.*

**Theorem — uniform limit of continuous functions is continuous**

$$f_n \text{ continuous},\ f_n\to f \text{ uniformly}\ \Rightarrow\ f \text{ continuous.}$$

**Proof — continuity is preserved (the $\varepsilon/3$ argument)**

1. Fix $a$ and $\varepsilon>0$. By uniform convergence pick $n$ with $\sup_x|f_n(x)-f(x)|\lt\tfrac{\varepsilon}{3}$.
2. That $f_n$ is continuous at $a$: pick $\delta$ with $|x-a|\lt\delta\Rightarrow|f_n(x)-f_n(a)|\lt\tfrac{\varepsilon}{3}$.
3. Split the target through $f_n$: for $|x-a|\lt\delta$,

   $$|f(x)-f(a)|\le|f(x)-f_n(x)|+|f_n(x)-f_n(a)|+|f_n(a)-f(a)|\lt\tfrac{\varepsilon}{3}+\tfrac{\varepsilon}{3}+\tfrac{\varepsilon}{3}=\varepsilon.$$

*The outer two thirds need uniformity (one $n$ for all $x$); the middle third is plain continuity. $\blacksquare$*

**Theorem — interchange of limit and integral**

$$f_n\to f \text{ uniformly on } [a,b],\ f_n \text{ integrable}\ \Rightarrow\ \int_a^b f_n\to\int_a^b f.$$

**Proof — uniform convergence lets you integrate term-by-term**

1. Let $\varepsilon_n=\sup_x|f_n(x)-f(x)|$. Uniform convergence means $\varepsilon_n\to 0$. (One shows $f$ is integrable too; assume it for the estimate.)
2. Bound the difference of integrals by the integral of the difference:

   $$\Big|\int_a^b f_n-\int_a^b f\Big|=\Big|\int_a^b (f_n-f)\Big|\le\int_a^b |f_n-f|.$$
3. Use the uniform bound $|f_n-f|\le\varepsilon_n$ pointwise:

   $$\int_a^b|f_n-f|\le\varepsilon_n\,(b-a)\ \longrightarrow\ 0.$$

*The $\sup$-bound $\varepsilon_n$ times the interval length controls the whole integral. Pointwise convergence is *not* enough — moving "spike" functions converge pointwise to 0 yet keep area 1. $\blacksquare$*

**Theorem — differentiating a limit (the delicate case)**

$$f_n\to f \text{ pointwise},\ f_n' \text{ continuous},\ f_n'\to g \text{ uniformly}\ \Rightarrow\ f'=g.$$

*Differentiation does *not* commute with mere uniform convergence of $f_n$; you must assume the **derivatives** converge uniformly. Proof: integrate $f_n'\to g$ (previous theorem), then apply FTC.*

> **Connection — when "swap the order" is legal**
>
> Casually swapping $\lim$ with $\int$ or $\frac{d}{dx}$, or summing a series term-by-term, is justified *exactly* by uniform convergence. The famous failures of interchange in early calculus are all cases where convergence was only pointwise.

<a id="s12"></a>
### Power series & analytic functions

*Power series are the best-behaved infinite sums — inside their disk they converge uniformly on compacts and may be differentiated and integrated term-by-term freely.*

**Definition & theorem — radius of convergence**

$$\sum_{n=0}^{\infty} c_n (x-a)^n,\qquad \frac1R=\limsup_{n\to\infty}|c_n|^{1/n}\quad(\text{Cauchy–Hadamard}).$$

*The series converges absolutely for $|x-a|\lt R$ and diverges for $|x-a|\gt R$. The use of $\limsup$ (Section 4) is what makes $R$ always well-defined.*

**Proof — convergence inside the radius, with uniform convergence on compacts**

1. Fix $r\lt R$. Pick $\rho$ with $r\lt\rho\lt R$; then $\limsup|c_n|^{1/n}\lt 1/\rho$, so for large $n$, $|c_n|^{1/n}\lt 1/\rho$, i.e. $|c_n|\lt\rho^{-n}$.
2. For $|x-a|\le r$: $|c_n(x-a)^n|\le|c_n|r^n\lt (r/\rho)^n=:M_n$, and $\sum M_n$ is a convergent geometric series since $r/\rho\lt 1$.
3. By the Weierstrass M-test (Section 10) the power series converges uniformly on $\{|x-a|\le r\}$:

   $$\sum |c_n(x-a)^n|\le\sum (r/\rho)^n=\frac{1}{1-r/\rho}\lt\infty.$$

*Uniform convergence on every closed sub-disk is what licenses all the nice operations below. $\blacksquare$*

> **Theorem — term-by-term calculus**
>
> Inside $|x-a|\lt R$, a power series defines an infinitely differentiable function; it may be **differentiated and integrated term-by-term**, and the resulting series have the same radius $R$. Consequently $c_n=\dfrac{f^{(n)}(a)}{n!}$: the series is its own Taylor series. This follows from Section 11 applied on each compact sub-disk where convergence is uniform.

> **Concept — analytic, and why $C^\infty\ne$ analytic**
>
> A function is **analytic** at $a$ if it equals a convergent power series near $a$. Analytic $\Rightarrow C^\infty$, but not conversely: $f(x)=e^{-1/x^2}$ (with $f(0)=0$) is smooth yet has *all* derivatives zero at 0, so its Taylor series is $0$ and does not represent $f$. Smoothness is weaker than analyticity.

> **Connection — Taylor series, finally justified**
>
> Writing $e^x=\sum x^n/n!$ or $\sin x=\sum(-1)^n x^{2n+1}/(2n+1)!$ and manipulating them termwise — differentiating, integrating, multiplying — is rigorous precisely because power series converge uniformly on compacts. The remainder estimate of Section 7 tells you *when* the Taylor series actually converges back to $f$.

<a id="s13"></a>
### A glimpse beyond: metric spaces, multivariable rigor & Lebesgue

*The same $\varepsilon$-ideas generalize far past the real line. A short tour of where analysis goes next.*

**Metric spaces — abstracting distance**

$$d(x,y)\ge 0,\ \ d(x,y)=0\iff x=y,\ \ d(x,y)=d(y,x),\ \ d(x,z)\le d(x,y)+d(y,z).$$

*Replace $|x-y|$ by any function $d$ satisfying these axioms and every $\varepsilon$-definition transfers verbatim: limits, continuity, Cauchy sequences, compactness. $\mathbb{R}^n$, function spaces, and sequence spaces all become arenas for the same theorems.*

> **Concept — completeness, abstractly & the contraction principle**
>
> A metric space is **complete** if every Cauchy sequence converges — the abstract version of Section 3's theorem for $\mathbb{R}$. In a complete space, the **Banach fixed-point theorem** guarantees a contraction $d(Tx,Ty)\le k\,d(x,y)$ with $k\lt 1$ has a unique fixed point. This single result proves existence and uniqueness for differential equations (Picard–Lindelöf) and the inverse function theorem.

> **Concept — multivariable rigor**
>
> In $\mathbb{R}^n$ the derivative becomes a **linear map** (the total derivative / Jacobian): $f(a+h)=f(a)+Df(a)\,h+o(\|h\|)$. Partial derivatives existing is *not* enough for differentiability; one needs them continuous. The MVT weakens to an inequality, and the Implicit and Inverse Function Theorems — proved via the contraction principle — replace the one-variable algebra.

> **Concept — the Lebesgue integral**
>
> The Riemann integral chokes on badly discontinuous functions (the Dirichlet function, Section 8) and behaves poorly under limits. **Lebesgue's** idea: partition the *range*, not the domain, and measure how much domain maps into each range slice. This integrates far more functions, and yields clean convergence theorems (Monotone & Dominated Convergence) where $\lim\int=\int\lim$ holds under mild hypotheses — repairing the fragility of interchanging limits with Riemann integrals.

> **Connection — one idea, endlessly reused**
>
> From $\varepsilon$–$N$ for sequences to $\varepsilon$–$\delta$ for functions, to $d(x,y)$ in metric spaces, to measure-theoretic integration — it is the *same* move: control a quantity to within any prescribed tolerance. Master that one habit and all of analysis, however abstract, is familiar territory.

---

*A rigorous first course in real analysis — the theory beneath the Complete Calculus and Derived from Scratch guides. Every limit is an $\varepsilon$; every theorem is proved from the completeness of $\mathbb{R}$. Read once for the architecture, then return to any proof box as a reference. Remember the single thread: control any quantity to within any tolerance, and infinity becomes safe.*
