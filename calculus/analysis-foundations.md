**English** · [中文](analysis-foundations.zh.md)

# Calculus, *made rigorous.*

The companion that goes underneath the formulas. Here every limit is an $\varepsilon$, every theorem is **stated precisely and proved**, and the whole edifice — continuity, derivatives, integrals, series — is rebuilt from one foundation: the **completeness** of the real numbers.

[← Back to all guides](../README.md)

## Part A · Numbers & sequences

<a id="s0"></a>
### The big picture: why rigor, and the role of $\varepsilon$

Calculus computes with infinity. Analysis is the discipline that makes those computations *true* rather than merely suggestive. Before we prove anything, this section explains, in plain words, what we are doing and why, and it introduces the handful of symbols that will recur on every page.

#### What problem are we solving?

For two centuries calculus ran on intuition about "infinitely small" quantities. It worked spectacularly — and it also produced paradoxes: divergent series summed to nonsense, "continuous" functions with no derivative anywhere, and arguments that proved $1=0$. The nineteenth-century project of **Cauchy, Weierstrass, Bolzano, Dedekind** and others replaced the vague infinitesimal with a single precise idea: the **limit**, defined by $\varepsilon$.

#### The symbols you will see everywhere

Before anything else, here is the vocabulary, defined from scratch. Do not assume you already know these; we will use them constantly.

- A **set** is a collection of objects considered as one whole; the objects are its **elements**. We write $x\in S$ to mean "$x$ is an element of the set $S$," and $x\notin S$ for "$x$ is not." The **empty set** $\varnothing$ is the set with no elements at all.
- $\mathbb{N}=\{1,2,3,\dots\}$ is the set of **natural numbers** (the counting numbers). $\mathbb{Z}=\{\dots,-2,-1,0,1,2,\dots\}$ is the **integers**. $\mathbb{Q}$ is the **rationals**, the numbers expressible as a fraction $p/q$ with $p,q$ integers and $q\ne 0$. $\mathbb{R}$ is the **real numbers**, which we build carefully in §s1.
- The symbol $\forall$ means "for all / for every," and $\exists$ means "there exists." So "$\forall\varepsilon>0\ \exists\delta>0$" reads "for every positive number $\varepsilon$ there exists a positive number $\delta$."
- The symbol $\Rightarrow$ means "implies," and $\iff$ means "if and only if" (each side implies the other).
- $\varepsilon$ (the Greek letter epsilon) and $\delta$ (delta) are, by long tradition, names for small positive numbers used to measure closeness. There is nothing special about the letters; they are just labels for a **tolerance** (how close we demand) and a **margin** (how close we arrange the input to be).
- The **absolute value** $|x|$ is $x$ if $x\ge 0$ and $-x$ if $x<0$; it measures the *distance from $0$*. Then $|x-y|$ is the distance between $x$ and $y$. The key fact we use endlessly is the **triangle inequality**: $|x+y|\le|x|+|y|$, and its consequence $|x-z|\le|x-y|+|y-z|$ (going from $x$ to $z$ via $y$ never shortens the trip).

> **Principle — what "rigor" buys you**
>
> The informal idea "$f(x)$ gets close to $L$ as $x$ gets close to $a$" hides the questions: *how* close, and *who chooses first?* The $\varepsilon$–$\delta$ definition answers both: **an adversary names a tolerance $\varepsilon>0$, and you must produce a $\delta$ that meets it.** Every theorem of calculus becomes a guarantee you can actually deliver on, not a picture you hope is right.

To make this concrete, here is the "game" once, slowly. Suppose someone claims that the numbers $a_n=1/n$ get close to $0$. To *prove* it, imagine an adversary who challenges you with a tolerance, say $\varepsilon=0.001$. You must respond with a threshold — a stage $N$ — and promise that from term $N$ onward, every $a_n$ is within $0.001$ of $0$. Here $a_n=1/n<0.001$ as soon as $n>1000$, so you answer $N=1001$. The adversary may then try a smaller tolerance, say $\varepsilon=10^{-9}$; you answer $N=10^9+1$. Rigor is the demand that you can answer *any* challenge, no matter how small, with a definite rule. We will see in §s1 that the ability to always answer rests on one fact about $\mathbb{R}$.

> **Concept — the one foundation: completeness**
>
> The rationals $\mathbb{Q}$ have a hole at $\sqrt 2$; the sequence $1,1.4,1.41,1.414,\dots$ "wants" to converge but has nowhere in $\mathbb{Q}$ to land. The real numbers $\mathbb{R}$ are built precisely to have **no holes**. That single property — **completeness** — is the engine behind every existence theorem ahead: that bounded monotone sequences converge, that continuous functions attain maxima, that integrals exist.

Why is $\sqrt 2$ not a rational number? Here is a full proof, so the claim "hole at $\sqrt 2$" is not taken on faith.

**Proof — $\sqrt 2$ is irrational (no fraction squares to $2$)**

1. Suppose, for contradiction, that $\sqrt 2 = p/q$ for integers $p,q$ with $q\ne 0$, and assume the fraction is in lowest terms — meaning $p$ and $q$ share no common factor greater than $1$. (Any fraction can be reduced to lowest terms by cancelling common factors, so this loses no generality.)
2. Squaring both sides gives $2 = p^2/q^2$, hence $p^2 = 2q^2$. Therefore $p^2$ is even (it is two times an integer).
3. If $p^2$ is even then $p$ is even: because if $p$ were odd, $p=2k+1$, then $p^2=4k^2+4k+1$ would be odd. So $p=2m$ for some integer $m$.
4. Substitute: $(2m)^2 = 2q^2$, i.e. $4m^2 = 2q^2$, so $q^2 = 2m^2$. By the same reasoning as step 3, $q$ is even.
5. But then $p$ and $q$ are both even, sharing the common factor $2$ — contradicting "lowest terms" from step 1. The assumption was impossible, so no such fraction exists; $\sqrt 2\notin\mathbb{Q}$. $\blacksquare$

This is exactly the "hole": the number whose square is $2$ exists on the number line but is missing from $\mathbb{Q}$. Completeness (§s1) is the axiom guaranteeing $\mathbb{R}$ contains it and every other such limiting value.

#### The whole subject on one line

> Real numbers & completeness → limits of sequences → continuity → derivatives → integrals → series of functions → power series

Each arrow is a chapter of this guide, and each later topic is *defined and proved using only the earlier ones*. Nothing is assumed that has not first been built.

> **Connection — this guide vs. the others**
>
> The *Complete Calculus* and *Derived from Scratch* guides tell you the rules and show you the manipulations. This guide answers the next question — **why are those rules valid?** Whenever you used a limit, a continuity assumption, or "$dx$," there was a theorem underneath; here we name it and prove it.

#### Common pitfalls before we begin

- Do not read $\varepsilon$ as a single fixed small number. It is *every* positive number in turn; a claim "holds for all $\varepsilon>0$" must survive arbitrarily tiny challenges.
- The *order* of quantifiers matters enormously. "$\forall\varepsilon\,\exists N$" (the $N$ may depend on $\varepsilon$) is weaker than "$\exists N\,\forall\varepsilon$" (one $N$ for all $\varepsilon$). Swapping them silently is the most common error in the subject; §s10 is built around exactly this distinction.

<a id="s1"></a>
### The real numbers: ordered field, completeness & the supremum

*Everything rests on knowing exactly what $\mathbb{R}$ is. It is the unique complete ordered field — and the word "complete" is what distinguishes it from $\mathbb{Q}$.*

We now define, from the ground up, what kind of object $\mathbb{R}$ is. A definition by *axioms* lists the properties we demand; any object having all of them behaves like $\mathbb{R}$.

#### The ordered-field axioms

A **field** is a set $F$ with two operations, addition $+$ and multiplication $\cdot$, satisfying:

- **Associativity:** $(a+b)+c=a+(b+c)$ and $(a\cdot b)\cdot c=a\cdot(b\cdot c)$ — grouping does not matter.
- **Commutativity:** $a+b=b+a$ and $a\cdot b=b\cdot a$ — order does not matter.
- **Identities:** there are special elements $0$ and $1$ (with $0\ne 1$) such that $a+0=a$ and $a\cdot 1=a$ for all $a$.
- **Inverses:** every $a$ has an additive inverse $-a$ with $a+(-a)=0$; every $a\ne 0$ has a multiplicative inverse $a^{-1}$ with $a\cdot a^{-1}=1$.
- **Distributivity:** $a\cdot(b+c)=a\cdot b+a\cdot c$ — multiplication spreads over addition.

A field is **ordered** if it also carries a relation $<$ ("less than") that is:

- **Total:** for any $a,b$ exactly one of $a<b$, $a=b$, $b<a$ holds.
- **Transitive:** $a<b$ and $b<c$ imply $a<c$.
- **Compatible with $+$:** $a<b\Rightarrow a+c<b+c$ for every $c$.
- **Compatible with $\cdot$ by positives:** $a<b$ and $0<c$ imply $a\cdot c<b\cdot c$.

*The rationals $\mathbb{Q}$ satisfy **all** of this — so the axioms so far do not single out $\mathbb{R}$.* We write $a\le b$ for "$a<b$ or $a=b$," and $a>b$ for "$b<a$."

#### Bounds, supremum & infimum

To state the missing axiom we first need vocabulary for "edges" of a set.

- Let $S$ be a set of real numbers. A number $u$ is an **upper bound** of $S$ if no element of $S$ exceeds it:

$$u \text{ is an upper bound of } S \iff \forall x\in S,\ x\le u.$$

- Symmetrically, $\ell$ is a **lower bound** of $S$ if $\ell\le x$ for every $x\in S$. A set with an upper bound is **bounded above**; with a lower bound, **bounded below**; with both, **bounded**.
- Among all upper bounds, the *smallest* one (if it exists) is the **supremum**, or **least upper bound**; the *largest* lower bound is the **infimum**:

$$\sup S = \text{the } least \text{ upper bound of } S;\qquad \inf S = \text{the } greatest \text{ lower bound.}$$

The supremum deserves a working characterization we will quote dozens of times.

> **Characterization of the supremum**
>
> $M=\sup S$ means exactly two things together: **(i)** $M$ is an upper bound ($x\le M$ for all $x\in S$); and **(ii)** nothing smaller is an upper bound — equivalently, for every $\varepsilon>0$ there is some $x\in S$ with $x>M-\varepsilon$.

Why is (ii) the right way to say "smallest"? If some $M-\varepsilon$ (a number below $M$) were *still* an upper bound, then $M$ would not be the *least* upper bound. So "least" is the same as "you cannot lower the bar by any positive amount $\varepsilon$ without letting an element of $S$ poke above it." We will use clause (ii) — "$M-\varepsilon$ is not an upper bound, so some element beats it" — as a tool to *produce* elements of $S$ on demand.

Worked example. Let $S=\{1-\tfrac1n : n\in\mathbb{N}\}=\{0,\tfrac12,\tfrac23,\tfrac34,\dots\}$. Claim: $\sup S=1$. Check (i): each $1-\tfrac1n<1$, so $1$ is an upper bound. Check (ii): given $\varepsilon>0$, we need $1-\tfrac1n>1-\varepsilon$, i.e. $\tfrac1n<\varepsilon$, i.e. $n>\tfrac1\varepsilon$; such an $n$ exists (this is the Archimedean property, proved just below), and that element exceeds $1-\varepsilon$. Note $1\notin S$: a supremum need not belong to the set.

> **Axiom — completeness (the least-upper-bound property)**
>
> This is the defining axiom of $\mathbb{R}$: **every nonempty subset of $\mathbb{R}$ that is bounded above has a supremum in $\mathbb{R}$.** The set $\{x\in\mathbb{Q}: x^2\lt 2\}$ is bounded above but has no supremum *in $\mathbb{Q}$* — its would-be sup is $\sqrt 2$, which is missing (§s0 proved $\sqrt2\notin\mathbb{Q}$). Completeness says $\mathbb{R}$ has no such gaps.

By taking negatives one gets the mirror statement for free: every nonempty set bounded below has an infimum, namely $\inf S = -\sup(-S)$, where $-S=\{-x:x\in S\}$. (If $u$ bounds $-S$ above then $-u$ bounds $S$ below, and the least upper bound of $-S$ corresponds to the greatest lower bound of $S$.)

#### The Archimedean property

This first consequence of completeness is small but powerful: it says the natural numbers are not trapped below any ceiling.

**Proof — the Archimedean property: $\mathbb{N}$ is unbounded in $\mathbb{R}$**

1. Claim: for every $x\in\mathbb{R}$ there is $n\in\mathbb{N}$ with $n>x$. Suppose not — then some $x$ is an upper bound of $\mathbb{N}$, so $\mathbb{N}$ is bounded above.
2. The set $\mathbb{N}$ is nonempty (it contains $1$) and is now assumed bounded above, so by the **completeness axiom** the supremum $s=\sup\mathbb{N}\in\mathbb{R}$ exists.
3. Apply clause (ii) of the supremum characterization with $\varepsilon=1$: $s-1$ is *not* an upper bound, so there is $m\in\mathbb{N}$ with $m>s-1$. Adding $1$ to both sides (allowed: $<$ is compatible with $+$) gives $m+1>s$.
4. But $m+1$ is again a natural number (the naturals are closed under adding $1$):

   $$m+1\in\mathbb{N}\ \text{yet}\ m+1\gt s=\sup\mathbb{N}.$$
5. This says an element of $\mathbb{N}$ exceeds the upper bound $s$ — contradicting clause (i) that $s$ bounds $\mathbb{N}$ above. The assumption in step 1 was false, so $\mathbb{N}$ is unbounded. $\blacksquare$

**Corollary (the workhorse).** For any $\varepsilon>0$ there is $n\in\mathbb{N}$ with $1/n<\varepsilon$. *Proof:* by the theorem there is $n>1/\varepsilon$; since both sides are positive, taking reciprocals reverses the inequality to $1/n<\varepsilon$. This tiny fact is what makes $1/n\to 0$ (§s2) and thereby drives countless limits.

Worked example of the corollary. To force $1/n<0.0007$, the corollary says pick $n>1/0.0007\approx 1428.57$, so $n=1429$ works: indeed $1/1429\approx 0.000700\ldots<0.0007$.

#### Density of the rationals

**Proof — $\mathbb{Q}$ is dense in $\mathbb{R}$ (a rational lies in every open interval)**

1. Given reals $a<b$, we produce a rational strictly between them. First scale the gap so it is wider than $1$: by the Archimedean corollary pick $n\in\mathbb{N}$ with $\tfrac1n<b-a$. Multiplying by $n>0$ (compatible with $\cdot$) gives $nb-na>1$.
2. An interval of real length greater than $1$ must contain an integer. Make this precise: let $m$ be the least integer strictly greater than $na$. (Such a least integer exists because the integers above $na$ are bounded below by $na$ and the integers are "discrete" — there is a smallest one once you are above a fixed real; this uses the Archimedean property to know integers above $na$ exist at all.) By minimality, $m-1\le na$, hence $m\le na+1$.
3. Combine: $m\le na+1$ and from step 1 $na+1<nb$, so $m<nb$. Together with $m>na$ we have $na<m<nb$. Dividing all three parts by $n>0$:

   $$a\lt \frac{m}{n}\lt b.$$
   Since $m/n$ is a quotient of integers with $n\ne0$, it is rational. $\blacksquare$

Worked example. Find a rational strictly between $a=\sqrt2\approx1.41421$ and $b=1.415$. Here $b-a\approx0.00079$; pick $n=2000$ (so $1/n=0.0005<b-a$). Then $na\approx2828.43$, so the least integer above it is $m=2829$, and $m/n=2829/2000=1.4145$, which indeed satisfies $1.41421<1.4145<1.415$.

> **Connection — why this comes first**
>
> Every "the limit exists" claim you took on faith in calculus is ultimately cashed out as a supremum produced by completeness. Lose this axiom and continuous functions can skip over zero, bounded sequences need not converge, and the integral may not exist. $\mathbb{R}$ is engineered so none of that happens.

<a id="s2"></a>
### Sequences and their limits (the $\varepsilon$–$N$ definition)

*The simplest infinite process. Master the $\varepsilon$–$N$ definition here and the $\varepsilon$–$\delta$ of continuity is the same idea with a different clock.*

#### What is a sequence?

A **sequence** of real numbers is an unending list $a_1,a_2,a_3,\dots$ — formally, a rule assigning to each natural number $n$ a real number $a_n$, called the **$n$-th term**. We write $(a_n)$ for the whole sequence. Examples: $a_n=1/n$ gives $1,\tfrac12,\tfrac13,\dots$; $a_n=(-1)^n$ gives $-1,1,-1,1,\dots$; $a_n=n$ gives $1,2,3,\dots$.

#### Definition — convergence of a sequence

We say the sequence **converges to the limit $L$**, written $a_n\to L$, when its terms eventually stay arbitrarily close to $L$:

$$a_n \to L \iff \forall\varepsilon>0\ \ \exists N\in\mathbb{N}\ \ \forall n\ge N:\ \ |a_n-L|\lt\varepsilon.$$

*Read it as the game of §s0: the adversary picks any tolerance $\varepsilon>0$; you must name a threshold $N$ past which **all** terms $a_n$ sit within distance $\varepsilon$ of $L$. If you can always answer, the limit is $L$.* Unpacking the symbols: $|a_n-L|<\varepsilon$ says the distance from $a_n$ to $L$ is below $\varepsilon$; "$\forall n\ge N$" says this holds for every term from the $N$-th onward (only finitely many early terms may misbehave). A sequence that converges to some $L$ is called **convergent**; otherwise **divergent**.

**Worked example — $1/n\to 0$, with the $\varepsilon$–$N$ rule made explicit.**

1. Fix any $\varepsilon>0$. We must find $N$ so that $n\ge N\Rightarrow|1/n-0|<\varepsilon$, i.e. $1/n<\varepsilon$.
2. By the Archimedean corollary (§s1) there is $N\in\mathbb{N}$ with $1/N<\varepsilon$.
3. For every $n\ge N$ we have $1/n\le 1/N<\varepsilon$ (larger denominator, smaller fraction), so $|1/n-0|=1/n<\varepsilon$. Since $\varepsilon$ was arbitrary, $1/n\to0$. $\blacksquare$

#### Proof — limits are unique

A sequence cannot sneak up on two different numbers at once.

1. Suppose, for contradiction, that $a_n\to L$ and $a_n\to L'$ with $L\ne L'$. Then $|L-L'|>0$. Set the tolerance to half that gap: $\varepsilon=\tfrac{|L-L'|}{2}>0$.
2. By $a_n\to L$ there is $N_1$ with $|a_n-L|<\varepsilon$ for all $n\ge N_1$. By $a_n\to L'$ there is $N_2$ with $|a_n-L'|<\varepsilon$ for all $n\ge N_2$. For any single $n\ge\max(N_1,N_2)$, *both* inequalities hold at once.
3. Apply the triangle inequality (§s0), routing from $L$ to $L'$ through that term $a_n$:

   $$|L-L'|\le|L-a_n|+|a_n-L'|\lt\varepsilon+\varepsilon=2\varepsilon=|L-L'|.$$
4. This reads $|L-L'|<|L-L'|$, which is impossible (no number is less than itself). The assumption $L\ne L'$ fails, so the limit, if it exists, is unique — justifying the phrase "*the* limit." $\blacksquare$

#### Proof — convergent sequences are bounded

1. Let $a_n\to L$. Apply the definition with the specific tolerance $\varepsilon=1$: there is $N$ with $|a_n-L|<1$ for all $n\ge N$. By the triangle inequality $|a_n|=|(a_n-L)+L|\le|a_n-L|+|L|<1+|L|$, so $|a_n|<|L|+1$ for every $n\ge N$.
2. Only finitely many terms are left unaccounted for, namely $a_1,\dots,a_{N-1}$. Take the largest magnitude among everything in sight:

   $$M=\max\big(|a_1|,\dots,|a_{N-1}|,\ |L|+1\big).$$
   (A maximum of finitely many numbers always exists.)
3. Then $|a_n|\le M$ for *every* $n$: for $n<N$ it is one of the listed terms; for $n\ge N$ it is below $|L|+1\le M$ by step 1. So $(a_n)$ is bounded. $\blacksquare$

*Boundedness is necessary for convergence — though, as §s3 shows with $(-1)^n$, not sufficient.* This is a classic pitfall: bounded does **not** imply convergent.

#### Theorem — the algebra of limits

Limits respect the arithmetic operations:

$$\text{If } a_n\to A,\ b_n\to B,\text{ then } a_n+b_n\to A+B,\ \ a_nb_n\to AB,\ \ \tfrac{a_n}{b_n}\to\tfrac{A}{B}\ (B\ne 0).$$

**Proof — the limit of a sum is the sum of limits**

1. Let $a_n\to A$, $b_n\to B$, and fix $\varepsilon>0$. Strategy: spend half the tolerance budget on each sequence — the "$\varepsilon/2$ trick."
2. Since $a_n\to A$, choose $N_1$ so that $n\ge N_1\Rightarrow|a_n-A|<\tfrac\varepsilon2$. Since $b_n\to B$, choose $N_2$ so that $n\ge N_2\Rightarrow|b_n-B|<\tfrac\varepsilon2$. (We may demand tolerance $\tfrac\varepsilon2$ because $\tfrac\varepsilon2$ is itself a positive number, and the definition works for *every* positive tolerance.)
3. For $n\ge N=\max(N_1,N_2)$ both hold, and the triangle inequality gives

   $$|(a_n+b_n)-(A+B)|=|(a_n-A)+(b_n-B)|\le|a_n-A|+|b_n-B|\lt\tfrac\varepsilon2+\tfrac\varepsilon2=\varepsilon.$$
4. As $\varepsilon$ was arbitrary, $a_n+b_n\to A+B$ by the definition of convergence. $\blacksquare$

**Proof — the limit of a product is the product of limits**

1. We measure the error and rewrite it by *adding and subtracting* the cross term $a_nB$ (a quantity we invent to split the problem):

   $$a_nb_n-AB=a_nb_n-a_nB+a_nB-AB=a_n(b_n-B)+B(a_n-A).$$
2. Take absolute values and use the triangle inequality plus $|xy|=|x||y|$:

   $$|a_nb_n-AB|\le|a_n|\,|b_n-B|+|B|\,|a_n-A|.$$
3. Since $(a_n)$ converges it is bounded (proved just above): there is $M>0$ with $|a_n|\le M$ for all $n$. So $|a_nb_n-AB|\le M\,|b_n-B|+|B|\,|a_n-A|$.
4. Fix $\varepsilon>0$. Using $a_n\to A$, choose $N_1$ with $|a_n-A|<\dfrac{\varepsilon}{2(|B|+1)}$ for $n\ge N_1$ (we write $|B|+1$ instead of $|B|$ so the denominator is never $0$, even when $B=0$). Using $b_n\to B$, choose $N_2$ with $|b_n-B|<\dfrac{\varepsilon}{2M}$ for $n\ge N_2$.
5. For $n\ge\max(N_1,N_2)$:

   $$|a_nb_n-AB|\le M\cdot\frac{\varepsilon}{2M}+|B|\cdot\frac{\varepsilon}{2(|B|+1)}\lt\frac\varepsilon2+\frac\varepsilon2=\varepsilon,$$
   where $|B|/(|B|+1)<1$. Hence $a_nb_n\to AB$. $\blacksquare$

**Worked example — combining the rules.** Let $a_n=2+\tfrac1n$ and $b_n=3-\tfrac5n$. Since $\tfrac1n\to0$ (proved above) and constants converge to themselves, the sum rule gives $a_n\to2$ and $b_n\to3$. The product rule then gives $a_nb_n\to2\cdot3=6$. Direct check: $a_nb_n=6-\tfrac{10}n+\tfrac3n-\tfrac5{n^2}=6-\tfrac7n-\tfrac5{n^2}\to6$, agreeing.

> **Connection — the rules you used informally**
>
> "The limit of a sum/product is the sum/product of limits" was a rule you applied without thought. It is a *theorem*, and this is its proof. The same statements for functions (§s5) follow by exactly this argument with $\delta$ in place of $N$.

<a id="s3"></a>
### Monotone convergence, Bolzano–Weierstrass & Cauchy sequences

*Three existence theorems — each a different way completeness guarantees a limit you can't compute by hand.*

First, vocabulary. A sequence $(a_n)$ is **increasing** if $a_n\le a_{n+1}$ for all $n$ (each term is at least the previous), **decreasing** if $a_n\ge a_{n+1}$, and **monotone** if it is one or the other. A **subsequence** of $(a_n)$ is what you get by keeping some of the terms in their original order: choose indices $n_1<n_2<n_3<\cdots$ and form $a_{n_1},a_{n_2},\dots$. For example, from $(-1)^n$ the even-index subsequence is the constant $1,1,1,\dots$.

#### Theorem — Monotone Convergence

$$\text{Every bounded monotone sequence converges.}$$

*If $(a_n)$ is increasing and bounded above, then $a_n\to\sup\{a_n\}$; if decreasing and bounded below, $a_n\to\inf\{a_n\}$. Monotone **and** bounded is enough — you needn't know the limit in advance.*

**Proof — monotone & bounded $\Rightarrow$ convergent (via the supremum)**

1. Let $(a_n)$ be increasing and bounded above. The set $S=\{a_n:n\in\mathbb{N}\}$ of its values is nonempty and bounded above, so by the **completeness axiom** (§s1) the supremum $L=\sup S$ exists.
2. Fix $\varepsilon>0$. By clause (ii) of the supremum characterization (§s1), $L-\varepsilon$ is not an upper bound, so some term $a_N>L-\varepsilon$.
3. Because the sequence is increasing, for all $n\ge N$ we have $a_n\ge a_N$; and because $L$ is an upper bound (clause (i)), $a_n\le L$. Therefore

   $$L-\varepsilon\lt a_N\le a_n\le L\lt L+\varepsilon\ \Rightarrow\ |a_n-L|\lt\varepsilon.$$
4. As $\varepsilon$ was arbitrary, $a_n\to L=\sup S$. The decreasing case is identical using $\inf$. $\blacksquare$

**Worked example.** Let $a_1=1$ and $a_{n+1}=\tfrac12(a_n+\tfrac2{a_n})$ (the Babylonian iteration for $\sqrt2$). One checks each $a_n\ge\sqrt2$ and the sequence is decreasing and bounded below by $\sqrt2$; Monotone Convergence then *guarantees a limit $L$ exists* without computing it. Passing to the limit in the recursion (using the algebra of limits, §s2) gives $L=\tfrac12(L+\tfrac2L)$, so $L^2=2$, $L=\sqrt2$. Completeness is what let us assert $L$ existed before we found it.

#### Theorem — Bolzano–Weierstrass

$$\text{Every bounded sequence in } \mathbb{R} \text{ has a convergent subsequence.}$$

**Proof — Bolzano–Weierstrass by bisection**

1. Let $(a_n)$ lie in a closed interval $[A,B]$ (boundedness gives such an interval). Cut $[A,B]$ in half at its midpoint. At least one of the two halves contains $a_n$ for infinitely many indices $n$ — because if *both* halves held only finitely many, the whole interval would too, yet it holds all of them. Call a half with infinitely many terms $I_1$; its length is $\tfrac{B-A}{2}$. Pick an index $n_1$ with $a_{n_1}\in I_1$.
2. Repeat the cut on $I_1$: one half, call it $I_2$, again contains infinitely many terms; its length is $\tfrac{B-A}{4}$. Because infinitely many indices land in $I_2$, we can choose one $n_2>n_1$ with $a_{n_2}\in I_2$. Continuing forever builds nested intervals $I_1\supset I_2\supset\cdots$ with lengths $|I_k|=\tfrac{B-A}{2^k}\to0$ and indices $n_1<n_2<\cdots$, i.e. a genuine subsequence $a_{n_k}\in I_k$.
3. The left endpoints $\ell_k$ of the $I_k$ form an increasing sequence bounded above by $B$, so by **Monotone Convergence** they converge to some $L$, and (because the lengths shrink to $0$) $L$ is the unique point lying in every $I_k$. Since $a_{n_k}$ and $L$ both lie in $I_k$, their distance is at most the length of $I_k$:

   $$|a_{n_k}-L|\le|I_k|=\frac{B-A}{2^{k}}\to 0.$$
4. Given $\varepsilon>0$, choose $k$ with $\tfrac{B-A}{2^k}<\varepsilon$ (possible since $\tfrac{B-A}{2^k}\to0$); then $|a_{n_k}-L|<\varepsilon$ for all larger $k$ too. Hence $a_{n_k}\to L$. $\blacksquare$

*A bounded sequence may wander forever, but it must **cluster** somewhere.* Example: $a_n=(-1)^n$ does not converge, yet its even-index subsequence converges to $1$ and its odd-index subsequence to $-1$ — two convergent subsequences, exactly as the theorem promises at least one.

#### Definition — Cauchy sequence

$$(a_n) \text{ is Cauchy} \iff \forall\varepsilon>0\ \exists N\ \forall m,n\ge N:\ |a_n-a_m|\lt\varepsilon.$$

*The terms eventually cluster among **themselves** — there is no mention of a limit $L$. This lets us prove convergence without knowing the target in advance, which is exactly the situation in series and integrals.*

**Proof — every convergent sequence is Cauchy**

1. Suppose $a_n\to L$ and fix $\varepsilon>0$. Choose $N$ with $|a_n-L|<\tfrac\varepsilon2$ for all $n\ge N$ (apply the definition of convergence with tolerance $\tfrac\varepsilon2$).
2. For any $m,n\ge N$, route through $L$ with the triangle inequality:

   $$|a_n-a_m|\le|a_n-L|+|L-a_m|\lt\tfrac\varepsilon2+\tfrac\varepsilon2=\varepsilon.$$
3. So the Cauchy condition holds; convergence $\Rightarrow$ Cauchy. $\blacksquare$

**Proof — every Cauchy sequence in $\mathbb{R}$ converges (completeness of $\mathbb{R}$)**

1. *A Cauchy sequence is bounded.* Apply the Cauchy condition with $\varepsilon=1$: there is $N$ with $|a_n-a_N|<1$ for all $n\ge N$, so $|a_n|<|a_N|+1$ for $n\ge N$; bound the finitely many earlier terms as in §s2 to get a global bound $M$.
2. By **Bolzano–Weierstrass**, the bounded sequence has a convergent subsequence $a_{n_k}\to L$ for some $L\in\mathbb{R}$.
3. We show the *whole* sequence converges to that same $L$. Fix $\varepsilon>0$. By Cauchy, get $N$ with $|a_n-a_m|<\tfrac\varepsilon2$ for all $m,n\ge N$. Since $a_{n_k}\to L$, pick one index $n_k\ge N$ with $|a_{n_k}-L|<\tfrac\varepsilon2$. Then for any $n\ge N$:

   $$|a_n-L|\le|a_n-a_{n_k}|+|a_{n_k}-L|\lt\tfrac\varepsilon2+\tfrac\varepsilon2=\varepsilon,$$
   where $|a_n-a_{n_k}|<\tfrac\varepsilon2$ because both $n,n_k\ge N$. Hence $a_n\to L$. $\blacksquare$

*In $\mathbb{R}$, Cauchy $\iff$ convergent.* This **Cauchy criterion** is "completeness" restated for sequences; it is the standard way to prove a series or an integral converges, since you can check the terms bunch together without already knowing the sum.

<a id="s4"></a>
### Limit superior & limit inferior

Even sequences that don't converge have a "ceiling" and "floor" of long-run behavior — and these *always* exist (for bounded sequences), unlike the ordinary limit.

#### Definition — $\limsup$ and $\liminf$

For each $n$, look only at the **tail** $\{a_k:k\ge n\}$ and take its supremum and infimum. Then let $n\to\infty$:

$$\limsup_{n\to\infty} a_n=\lim_{n\to\infty}\Big(\sup_{k\ge n} a_k\Big),\qquad \liminf_{n\to\infty} a_n=\lim_{n\to\infty}\Big(\inf_{k\ge n} a_k\Big).$$

*Why do these limits exist? Write $s_n=\sup_{k\ge n}a_k$. As $n$ grows we take the supremum over a **smaller** set (a shorter tail), and the sup of a subset can only be $\le$ the sup of the bigger set; so $s_n$ is **decreasing**. If the sequence is bounded below, $s_n$ is bounded below too, and by Monotone Convergence (§s3) it converges — that limit is $\limsup a_n$.* The same argument (with $\inf_{k\ge n}$ increasing) handles $\liminf$. So for a bounded sequence **both always exist in $\mathbb{R}$**, even when $\lim a_n$ does not.

> **Concept — what they capture**
>
> $\limsup a_n$ is the largest value the sequence approaches infinitely often (its biggest subsequential limit); $\liminf a_n$ is the smallest. For $a_n=(-1)^n$: $\limsup=1$, $\liminf=-1$. They pin down a sequence's eventual range even when no single limit exists.

**Worked example — $a_n=(-1)^n$.** For every $n$, the tail $\{a_k:k\ge n\}$ contains both $+1$ and $-1$, so $\sup_{k\ge n}a_k=1$ and $\inf_{k\ge n}a_k=-1$ for all $n$. Hence $\limsup=\lim 1=1$ and $\liminf=\lim(-1)=-1$. They differ, which (by the theorem below) is exactly why $(-1)^n$ has no ordinary limit.

#### Proof — $a_n\to L \iff \limsup a_n=\liminf a_n=L$

1. ($\Rightarrow$) Suppose $a_n\to L$. Fix $\varepsilon>0$; there is $N$ with $L-\varepsilon<a_k<L+\varepsilon$ for all $k\ge N$. Then for any $n\ge N$, the number $L+\varepsilon$ is an upper bound of the tail and $L-\varepsilon$ a lower bound, so $L-\varepsilon\le\inf_{k\ge n}a_k\le\sup_{k\ge n}a_k\le L+\varepsilon$. Letting $\varepsilon\to0$ squeezes both $\liminf$ and $\limsup$ to $L$.
2. ($\Leftarrow$) Suppose $\liminf a_n=\limsup a_n=L$. For every $n$, the term $a_n$ lies between the inf and sup of its own tail (it is a member of that tail), so

   $$\inf_{k\ge n}a_k\ \le\ a_n\ \le\ \sup_{k\ge n}a_k.$$
3. The lower bound sequence $\inf_{k\ge n}a_k$ and the upper bound sequence $\sup_{k\ge n}a_k$ both tend to $L$ by hypothesis. By the **Squeeze Theorem** — if $x_n\le a_n\le y_n$ and $x_n,y_n\to L$ then $a_n\to L$, proved next — we conclude $a_n\to L$. $\blacksquare$

**Proof of the Squeeze Theorem used above.** Suppose $x_n\le a_n\le y_n$ with $x_n\to L$ and $y_n\to L$. Fix $\varepsilon>0$; pick $N_1$ with $|x_n-L|<\varepsilon$ and $N_2$ with $|y_n-L|<\varepsilon$ for indices past them. For $n\ge\max(N_1,N_2)$: $L-\varepsilon<x_n\le a_n\le y_n<L+\varepsilon$, hence $|a_n-L|<\varepsilon$. So $a_n\to L$. $\blacksquare$

*Convergence is exactly the collapse of the gap between the eventual ceiling and floor.*

> **Connection — the root and ratio tests**
>
> The convergence tests for series you used (root test, ratio test) are stated rigorously with $\limsup$: a series $\sum a_n$ converges absolutely if $\limsup|a_n|^{1/n}\lt 1$. Because $\limsup$ always exists, these tests always have something to say — even for erratic terms. We use exactly this in §s12 to pin down the radius of convergence.

## Part B · Continuity & differentiation

<a id="s5"></a>
### Limits of functions and continuity ($\varepsilon$–$\delta$)

*The same game as $\varepsilon$–$N$, now with input distance $\delta$ controlling output distance $\varepsilon$.*

A **function** $f$ on a set $D\subseteq\mathbb{R}$ (its **domain**) assigns to each input $x\in D$ exactly one output $f(x)\in\mathbb{R}$. We now make precise what it means for the outputs to approach a value as the inputs approach a point.

#### Definition — limit of a function

$$\lim_{x\to a} f(x)=L \iff \forall\varepsilon>0\ \exists\delta>0:\ 0\lt|x-a|\lt\delta\ \Rightarrow\ |f(x)-L|\lt\varepsilon.$$

*Here $\varepsilon$ is the output tolerance (how close $f(x)$ must come to $L$) and $\delta$ the input margin (how close $x$ must come to $a$). The clause "$0<|x-a|$" excludes $x=a$ itself: the limit is about the **approach**, not the value at $a$.* The structure is identical to §s2's $\varepsilon$–$N$, with "$x$ within $\delta$ of $a$" playing the role of "$n\ge N$."

#### Definition — continuity at a point

$$f \text{ continuous at } a \iff \forall\varepsilon>0\ \exists\delta>0:\ |x-a|\lt\delta\ \Rightarrow\ |f(x)-f(a)|\lt\varepsilon.$$

*Equivalently, $\lim_{x\to a}f(x)=f(a)$: the limit exists, $f(a)$ is defined, and they agree. Now $x=a$ is allowed (it trivially satisfies the conclusion, since $|f(a)-f(a)|=0<\varepsilon$).* Intuitively, continuity means small changes in input produce small changes in output — no jumps.

#### Proof — $f(x)=x^2$ is continuous at every $a$

1. Fix a point $a$ and a tolerance $\varepsilon>0$. We must control $|x^2-a^2|$. Factor it: $|x^2-a^2|=|x-a|\,|x+a|$. The factor $|x-a|$ we can make small directly; the factor $|x+a|$ we must bound.
2. To bound $|x+a|$, first restrict attention to inputs with $|x-a|<1$. Then $|x|=|(x-a)+a|\le|x-a|+|a|<1+|a|$, so $|x+a|\le|x|+|a|<(1+|a|)+|a|=2|a|+1$.
3. Now choose $\delta=\min\!\Big(1,\ \dfrac{\varepsilon}{2|a|+1}\Big)$ (the smaller of the two guarantees both $|x-a|<1$ and $|x-a|<\tfrac{\varepsilon}{2|a|+1}$). Then for $|x-a|<\delta$:

   $$|x^2-a^2|=|x-a|\,|x+a|\lt\frac{\varepsilon}{2|a|+1}\cdot(2|a|+1)=\varepsilon.$$
4. Since $\varepsilon$ was arbitrary, $f(x)=x^2$ is continuous at $a$, and $a$ was arbitrary, so it is continuous everywhere. $\blacksquare$

**Worked example with numbers.** Take $a=3$, $\varepsilon=0.1$. Then $2|a|+1=7$, and $\delta=\min(1,0.1/7)=0.1/7\approx0.01428$. Check $x=3.01$ (within $\delta$): $|x^2-9|=|9.0601-9|=0.0601<0.1$. The recipe works.

*The "bound the awkward factor first, then choose $\delta$" pattern handles most explicit $\varepsilon$–$\delta$ proofs.*

#### Theorem — sequential criterion for continuity

$$f \text{ continuous at } a \iff \big(x_n\to a \Rightarrow f(x_n)\to f(a)\big)\ \text{for every sequence } x_n.$$

**Proof.**
1. ($\Rightarrow$) Suppose $f$ is continuous at $a$ and $x_n\to a$. Fix $\varepsilon>0$; continuity gives $\delta>0$ with $|x-a|<\delta\Rightarrow|f(x)-f(a)|<\varepsilon$. Since $x_n\to a$, there is $N$ with $|x_n-a|<\delta$ for $n\ge N$; then $|f(x_n)-f(a)|<\varepsilon$ for $n\ge N$. So $f(x_n)\to f(a)$.
2. ($\Leftarrow$) We prove the contrapositive: if $f$ is *not* continuous at $a$, we build a bad sequence. Failure of continuity means there is some $\varepsilon_0>0$ such that **no** $\delta$ works; in particular for each $\delta=\tfrac1n$ there is a point $x_n$ with $|x_n-a|<\tfrac1n$ yet $|f(x_n)-f(a)|\ge\varepsilon_0$. Then $x_n\to a$ but $f(x_n)\not\to f(a)$ — contradicting the sequential condition. $\blacksquare$

*This bridges Part A and Part B: it lets us reuse every sequence theorem for functions, and lets us **disprove** continuity by exhibiting one bad sequence.*

#### Proof — composition of continuous functions is continuous

1. Let $g$ be continuous at $a$ and $f$ continuous at $b=g(a)$; we show $f\circ g$ (the function $x\mapsto f(g(x))$) is continuous at $a$. Fix $\varepsilon>0$.
2. By continuity of $f$ at $b$, there is $\eta>0$ (eta, an output margin for $f$) with $|y-b|<\eta\Rightarrow|f(y)-f(b)|<\varepsilon$.
3. Treat that $\eta$ as the tolerance for $g$: by continuity of $g$ at $a$ there is $\delta>0$ with $|x-a|<\delta\Rightarrow|g(x)-b|<\eta$. Chain the two implications:

   $$|x-a|\lt\delta\ \Rightarrow\ |g(x)-b|\lt\eta\ \Rightarrow\ |f(g(x))-f(b)|\lt\varepsilon.$$
4. Since $f(b)=f(g(a))=(f\circ g)(a)$, this is exactly continuity of $f\circ g$ at $a$. $\blacksquare$

*Continuity passes through composition — the rigorous basis for differentiating composite functions (the chain rule).*

> **Connection — "you can plug in"**
>
> In the first calculus course, evaluating a limit by "plugging in" worked precisely *because* the function was continuous. Continuity is the formal statement that $\lim_{x\to a}f=f(a)$ — the permission slip for substitution.

<a id="s6"></a>
### Theorems on continuous functions: IVT, EVT & uniform continuity

*On a closed bounded interval, continuity is astonishingly strong. Three theorems show why — and all three need completeness.*

A few words on intervals: $[a,b]=\{x:a\le x\le b\}$ is **closed** (it contains its endpoints) and **bounded**; $(a,b)$ omits the endpoints. The combination *closed and bounded* is what powers everything here, via Bolzano–Weierstrass (§s3).

#### Theorem — Intermediate Value Theorem (IVT)

$$f \text{ continuous on } [a,b],\ \ f(a)\lt y\lt f(b)\ \Rightarrow\ \exists c\in(a,b):\ f(c)=y.$$

**Proof — IVT via the supremum**

1. Reduce to the case $y=0$: replace $f$ by $g(x)=f(x)-y$, which is continuous (difference of a continuous function and a constant), with $g(a)<0<g(b)$. We show $g(c)=0$ for some $c$. Define $S=\{x\in[a,b]:g(x)<0\}$.
2. $S$ is nonempty ($a\in S$ since $g(a)<0$) and bounded above (by $b$), so by **completeness** $c=\sup S$ exists, and $c\in[a,b]$.
3. Suppose $g(c)<0$. Note $c\ne b$ (since $g(b)>0$). By continuity at $c$ with tolerance $\varepsilon=\tfrac{|g(c)|}{2}$, there is $\delta>0$ on which $g$ stays negative; so points just to the right of $c$ (still in $[a,b]$) lie in $S$, giving elements of $S$ larger than $c$ — contradicting $c=\sup S$ (clause (i): $c$ bounds $S$).
4. Suppose $g(c)>0$. Note $c\ne a$. By continuity, $g$ stays positive on some interval $(c-\delta,c]$, so no point of $(c-\delta,b]$ is in $S$, meaning $c-\delta$ is already an upper bound of $S$ — contradicting that $c$ is the *least* upper bound (clause (ii)).
5. Both inequalities are impossible, so by trichotomy of $<$ (§s1), $g(c)=0$, i.e.

   $$f(c)=y. \qquad\blacksquare$$

**Worked example.** $f(x)=x^3+x-1$ is continuous, $f(0)=-1<0$ and $f(1)=1>0$, so the IVT guarantees a root $c\in(0,1)$ with $f(c)=0$ — the basis of the bisection method for finding it numerically.

#### Theorem — Extreme Value Theorem (EVT)

$$f \text{ continuous on } [a,b]\ \Rightarrow\ f \text{ is bounded and attains a max and a min on } [a,b].$$

**Proof — EVT via Bolzano–Weierstrass**

1. *Bounded.* Suppose not; then for each $n$ there is $x_n\in[a,b]$ with $|f(x_n)|>n$, so $|f(x_n)|\to\infty$. By **Bolzano–Weierstrass** (§s3) some subsequence $x_{n_k}\to x^*$, and $x^*\in[a,b]$ because the interval is closed (limits of points in $[a,b]$ stay in $[a,b]$). By the sequential criterion (§s5), $f(x_{n_k})\to f(x^*)$, a finite number — contradicting $|f(x_{n_k})|\to\infty$. So $f$ is bounded.
2. *Maximum attained.* Now that $f$ is bounded, $M=\sup_{x\in[a,b]}f(x)$ exists by completeness. By clause (ii) of the sup, for each $n$ there is $x_n$ with $f(x_n)>M-\tfrac1n$; combined with $f(x_n)\le M$ this forces $f(x_n)\to M$.
3. By Bolzano–Weierstrass, a subsequence $x_{n_k}\to c\in[a,b]$; by the sequential criterion $f(x_{n_k})\to f(c)$. But $f(x_{n_k})\to M$, and limits are unique (§s2), so $f(c)=M$:

   $$f(c)=M=\max_{[a,b]}f.$$
4. The minimum is obtained by applying everything above to $-f$ (whose max is the negative of the min of $f$). $\blacksquare$

*The closed, bounded interval is essential: $f(x)=1/x$ on $(0,1]$ is continuous but unbounded (no max), because $(0,1]$ is not closed.*

#### Definition — uniform continuity

$$f \text{ uniformly continuous on } I \iff \forall\varepsilon>0\ \exists\delta>0\ \forall x,y\in I:\ |x-y|\lt\delta\Rightarrow|f(x)-f(y)|\lt\varepsilon.$$

*The crucial difference from ordinary continuity is the **quantifier order**: here the single $\delta$ comes **before** "$\forall x,y$," so **one $\delta$ works for the whole interval at once** — it may not depend on the point. Ordinary continuity allows $\delta$ to shrink as you move around.* Example: $f(x)=1/x$ on $(0,1)$ is continuous at each point but **not** uniformly: near $0$ the function steepens without bound, so the same output gap $\varepsilon$ requires ever-tinier $\delta$, and no single $\delta$ serves all points.

#### Proof — Heine–Cantor: continuous on $[a,b]$ $\Rightarrow$ uniformly continuous

1. Suppose not. Then there is some $\varepsilon_0>0$ for which **no** $\delta$ works; in particular, taking $\delta=\tfrac1n$ in turn, there exist points $x_n,y_n\in[a,b]$ with $|x_n-y_n|<\tfrac1n$ yet $|f(x_n)-f(y_n)|\ge\varepsilon_0$.
2. By **Bolzano–Weierstrass**, the bounded sequence $(x_n)$ has a subsequence $x_{n_k}\to c\in[a,b]$. Since $|x_{n_k}-y_{n_k}|<\tfrac1{n_k}\to0$, the partner sequence satisfies $y_{n_k}=x_{n_k}+(y_{n_k}-x_{n_k})\to c$ as well (sum of limits, §s2).
3. By continuity of $f$ at $c$ and the sequential criterion (§s5), $f(x_{n_k})\to f(c)$ and $f(y_{n_k})\to f(c)$, so their difference tends to $0$:

   $$0=\lim_{k}\big|f(x_{n_k})-f(y_{n_k})\big|\ \ge\ \varepsilon_0\gt 0,$$
   where the inequality is the standing assumption $|f(x_{n_k})-f(y_{n_k})|\ge\varepsilon_0$. This is a contradiction ($0\ge\varepsilon_0>0$). Hence $f$ is uniformly continuous. $\blacksquare$

*Compactness upgrades pointwise continuity to uniform — the fact that makes the Riemann integral of a continuous function exist (§s8).*

> **Theorem — Heine–Borel (named)**
>
> A subset of $\mathbb{R}$ (or $\mathbb{R}^n$) is **compact** — every open cover has a finite subcover — *if and only if* it is **closed and bounded**. ("Open cover" means a collection of open intervals whose union contains the set; "finite subcover" means finitely many of them already suffice.) This is the abstract engine behind EVT and Heine–Cantor; "closed bounded interval" is the simplest compact set.

<a id="s7"></a>
### Differentiation: the Mean Value Theorem & Taylor's theorem with remainder

*The derivative is a limit; the MVT is the theorem that turns it into global information; Taylor's theorem quantifies the error of polynomial approximation.*

#### Definition — the derivative

The **derivative** of $f$ at $a$ measures the instantaneous rate of change — the limiting slope of the secant lines:

$$f'(a)=\lim_{h\to 0}\frac{f(a+h)-f(a)}{h},$$

*when this limit (in the sense of §s5) exists; $f$ is then **differentiable** at $a$. The quantity $\tfrac{f(a+h)-f(a)}{h}$ is the **difference quotient**, the slope of the line through $(a,f(a))$ and $(a+h,f(a+h))$.* Differentiability is strictly stronger than continuity, as the next result shows.

#### Proof — differentiable $\Rightarrow$ continuous

1. Suppose $f'(a)$ exists. For $x\ne a$, write the identity (multiply and divide by $x-a$):

   $$f(x)-f(a)=\frac{f(x)-f(a)}{x-a}\cdot(x-a).$$
2. As $x\to a$, the first factor tends to $f'(a)$ (by definition of the derivative, with $h=x-a$) and the second factor $(x-a)\to0$. By the product rule for limits (the function analogue of §s2), the product tends to $f'(a)\cdot 0=0$.
3. Therefore $\lim_{x\to a}\big(f(x)-f(a)\big)=0$, i.e. $\lim_{x\to a}f(x)=f(a)$, which is exactly continuity of $f$ at $a$ (§s5). $\blacksquare$

*The converse fails: $f(x)=|x|$ is continuous but not differentiable at $0$ (the left slope is $-1$, the right slope $+1$, so the difference quotient has no limit); Weierstrass's function is continuous **everywhere** yet differentiable **nowhere**.*

#### Theorem — Rolle & the Mean Value Theorem

$$\textbf{Rolle: } f\in C[a,b],\ \text{diff. on }(a,b),\ f(a)=f(b)\ \Rightarrow\ \exists c:\ f'(c)=0.$$

$$\textbf{MVT: } \exists c\in(a,b):\ f'(c)=\frac{f(b)-f(a)}{b-a}.$$

(Here "$f\in C[a,b]$" means $f$ is continuous on the closed interval $[a,b]$.)

**Proof — Rolle's theorem**

1. Since $f$ is continuous on $[a,b]$, by the **EVT** (§s6) it attains a maximum and a minimum on $[a,b]$.
2. If both the max and the min occur at the endpoints, then since $f(a)=f(b)$ the max and min values are equal, so $f$ is constant; then $f'\equiv0$ and any interior $c$ works.
3. Otherwise an extremum occurs at some interior point $c\in(a,b)$. We invoke **Fermat's interior-extremum lemma** (proved next): at an interior extremum where $f$ is differentiable, $f'(c)=0$. Hence

   $$f'(c)=0.\qquad\blacksquare$$

**Proof of Fermat's lemma (used above).** Suppose $f$ has a local maximum at interior $c$ and $f'(c)$ exists. For small $h>0$, $f(c+h)-f(c)\le0$, so the difference quotient $\tfrac{f(c+h)-f(c)}{h}\le0$; letting $h\to0^+$ gives $f'(c)\le0$. For small $h<0$, $f(c+h)-f(c)\le0$ but now dividing by the negative $h$ flips the sign: $\tfrac{f(c+h)-f(c)}{h}\ge0$; letting $h\to0^-$ gives $f'(c)\ge0$. Both together force $f'(c)=0$. (A minimum is handled by applying this to $-f$.) $\blacksquare$

**Proof — the MVT from Rolle**

1. Subtract the secant line joining the endpoints. Define the auxiliary function

   $$g(x)=f(x)-\Big[f(a)+\frac{f(b)-f(a)}{b-a}(x-a)\Big].$$
   This $g$ is continuous on $[a,b]$ and differentiable on $(a,b)$ (it is $f$ minus a linear function).
2. Evaluate at the endpoints: $g(a)=f(a)-f(a)=0$, and $g(b)=f(b)-\big[f(a)+(f(b)-f(a))\big]=0$. So $g(a)=g(b)$.
3. By **Rolle's theorem** applied to $g$, there is $c\in(a,b)$ with $g'(c)=0$. Differentiating $g$ gives $g'(x)=f'(x)-\tfrac{f(b)-f(a)}{b-a}$, so $g'(c)=0$ means

   $$f'(c)=\frac{f(b)-f(a)}{b-a}.\qquad\blacksquare$$

*EVT $\to$ Fermat $\to$ Rolle $\to$ MVT: a chain straight back to completeness.*

#### Proof — MVT consequence: $f'=0$ everywhere $\Rightarrow f$ constant

1. Take any two points $x_1<x_2$ in the interval. Apply the **MVT** on $[x_1,x_2]$: there is $c\in(x_1,x_2)$ with

   $$f(x_2)-f(x_1)=f'(c)\,(x_2-x_1).$$
2. By hypothesis $f'(c)=0$, so the right side is $0$, giving $f(x_2)=f(x_1)$. Since $x_1,x_2$ were arbitrary, $f$ takes the same value everywhere; $f$ is constant. $\blacksquare$

*This is exactly why "$+C$" appears in every antiderivative: if $F'=G'$ then $(F-G)'=0$, so $F-G$ is a constant — two antiderivatives of the same function differ by a constant.*

#### Theorem — Taylor's theorem with Lagrange remainder

$$f(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k+R_n,\qquad R_n=\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}$$

*for some $\xi$ (the Greek letter xi) strictly between $a$ and $x$, assuming $f$ is $(n+1)$-times differentiable on the interval between them. Here $f^{(k)}$ is the $k$-th derivative and $k!=1\cdot2\cdots k$ is the factorial. The polynomial part is the **degree-$n$ Taylor polynomial**; $R_n$ is the **exact** error, and the case $n=0$ is precisely the MVT.*

> **Concept — Taylor is a higher-order MVT**
>
> Taylor's theorem is proved by the same device as the MVT: subtract the degree-$n$ Taylor polynomial, build an auxiliary function vanishing to high order at $a$ and $x$, and apply Rolle (or Cauchy's MVT) repeatedly. The Lagrange remainder is the leftover from one final application — generalizing $f'(c)$ to $f^{(n+1)}(\xi)$.

**Worked example — bounding the error in $\sin x\approx x-\tfrac{x^3}{6}$.** Here $f=\sin$, $a=0$, $n=3$ (the degree-3 polynomial is $x-\tfrac{x^3}6$, since the $x^2$ coefficient vanishes). The fourth derivative is $\sin$ again, with $|f^{(4)}|\le1$. For $|x|\le0.5$, the Lagrange remainder gives $|R_3|\le\dfrac{1}{4!}|x|^4\le\dfrac{(0.5)^4}{24}=\dfrac{0.0625}{24}\approx0.0026$. So the approximation is correct to better than three decimals on $[-0.5,0.5]$ — a guarantee, not a hope.

> **Connection — error bounds you trusted**
>
> When you approximated $\sin x\approx x-\tfrac{x^3}{6}$ and claimed "the error is tiny," the Lagrange remainder is the rigorous bound: $|R_n|\le\dfrac{\max|f^{(n+1)}|}{(n+1)!}|x-a|^{n+1}$. It's what makes Taylor series trustworthy, not just formal.

## Part C · Integration, series & beyond

<a id="s8"></a>
### The Riemann integral: Darboux sums & the integrability criterion

*"Area under the curve" becomes a precise number squeezed between over- and under-estimates. The integral exists exactly when the squeeze closes.*

A **partition** $P$ of $[a,b]$ is a finite list of points $a=x_0<x_1<\cdots<x_n=b$ chopping the interval into subintervals $[x_{i-1},x_i]$ of widths $\Delta x_i=x_i-x_{i-1}$. We approximate the area by rectangles over each subinterval.

#### Definition — Darboux upper & lower sums

On each subinterval take the lowest and highest values of $f$ (their inf and sup) as rectangle heights:

$$L(f,P)=\sum_{i} m_i\,\Delta x_i,\quad U(f,P)=\sum_{i} M_i\,\Delta x_i,\quad m_i=\inf_{[x_{i-1},x_i]}f,\ M_i=\sup_{[x_{i-1},x_i]}f.$$

*$L$ uses the shortest rectangles, so it **under**-estimates the area; $U$ uses the tallest, so it **over**-estimates. Always $L(f,P)\le U(f,P)$ since $m_i\le M_i$.* A basic fact (a **refinement** — adding points to $P$ — only raises $L$ and lowers $U$, because splitting a subinterval can only raise the local inf and lower the local sup) means the lower sums never exceed the upper sums, even for different partitions.

#### Definition — the Riemann (Darboux) integral

The best under-estimate and best over-estimate are:

$$\underline{\int_a^b} f=\sup_P L(f,P),\qquad \overline{\int_a^b} f=\inf_P U(f,P).$$

These are the **lower** and **upper integrals**; they exist by completeness whenever $f$ is bounded. We declare $f$ **integrable** when they coincide:

$$f \text{ is integrable} \iff \underline{\int_a^b} f=\overline{\int_a^b} f,\ \text{the common value } \int_a^b f.$$

*Integrability means the gap between best over- and under-estimate can be driven to zero — the squeeze closes on a single number.*

#### Theorem — Riemann's criterion

$$f \text{ integrable on } [a,b] \iff \forall\varepsilon>0\ \exists\text{ partition } P:\ U(f,P)-L(f,P)\lt\varepsilon.$$

**Proof of the criterion.** Always $\underline{\int}f\le\overline{\int}f$. ($\Leftarrow$) If for each $\varepsilon$ some $P$ has $U(f,P)-L(f,P)<\varepsilon$, then $0\le\overline{\int}f-\underline{\int}f\le U(f,P)-L(f,P)<\varepsilon$ for every $\varepsilon$, forcing $\overline{\int}f=\underline{\int}f$ (a nonnegative number below every $\varepsilon$ is $0$). ($\Rightarrow$) If $f$ is integrable with common value $I$, pick $P_1$ with $L(f,P_1)>I-\tfrac\varepsilon2$ (clause (ii) of sup) and $P_2$ with $U(f,P_2)<I+\tfrac\varepsilon2$ (clause (ii) of inf); their common refinement $P$ has $U(f,P)-L(f,P)<\varepsilon$. $\blacksquare$

**Proof — every continuous $f$ on $[a,b]$ is integrable**

1. By **Heine–Cantor** (§s6), $f$ is uniformly continuous on $[a,b]$. Fix $\varepsilon>0$ and choose $\delta>0$ so that $|x-y|<\delta\Rightarrow|f(x)-f(y)|<\dfrac{\varepsilon}{b-a}$ — one $\delta$ for the whole interval (this uniformity is the crux).
2. Take any partition with every subinterval narrower than $\delta$. On each subinterval $[x_{i-1},x_i]$, the sup $M_i$ and inf $m_i$ are attained at actual points (by **EVT**, §s6), say at $u_i,v_i$ in that subinterval; since $|u_i-v_i|\le\Delta x_i<\delta$, uniform continuity gives $M_i-m_i=f(u_i)-f(v_i)\le\dfrac{\varepsilon}{b-a}$.
3. Sum up:

   $$U(f,P)-L(f,P)=\sum_i (M_i-m_i)\,\Delta x_i\le\frac{\varepsilon}{b-a}\sum_i\Delta x_i=\frac{\varepsilon}{b-a}\cdot(b-a)=\varepsilon,$$
   using $\sum_i\Delta x_i=b-a$ (the widths add up to the whole interval).
4. By **Riemann's criterion**, $f$ is integrable. $\blacksquare$

*Uniform continuity is exactly what lets **one** mesh size control the oscillation everywhere at once.*

> **Concept — what fails to be integrable**
>
> The Dirichlet function ($1$ on rationals, $0$ on irrationals) has $m_i=0$ and $M_i=1$ on **every** subinterval — because each contains both a rational and an irrational by density (§s1) — so $L=0$ and $U=b-a$ on every partition, the gap never closes, and it is **not** Riemann integrable. Riemann integrability requires the discontinuities to be "small" (measure zero, by Lebesgue's criterion). This limitation motivates §s13.

<a id="s9"></a>
### The Fundamental Theorem of Calculus, proved

*The theorem that fuses the two halves of calculus: integration and differentiation are inverse operations. Both directions, proved.*

#### FTC — Part I (differentiating an integral)

$$f \text{ continuous on } [a,b],\quad F(x)=\int_a^x f(t)\,dt\ \Rightarrow\ F'(x)=f(x).$$

Here $F$ is the **accumulation function**: it records the running area from $a$ up to $x$.

**Proof — FTC Part I**

1. Form the difference quotient of $F$ and use **additivity** of the integral ($\int_a^{x+h}=\int_a^x+\int_x^{x+h}$, so the difference is the piece over $[x,x+h]$):

   $$\frac{F(x+h)-F(x)}{h}=\frac1h\int_x^{x+h} f(t)\,dt.$$
2. Let $m_h$ and $M_h$ be the minimum and maximum of $f$ on $[x,x+h]$ (they exist by **EVT**, §s6, since $f$ is continuous). Each rectangle bound gives $m_h\,h\le\int_x^{x+h}f\le M_h\,h$ (the integral of a function between two constant heights lies between the corresponding rectangle areas). Dividing by $h>0$:

   $$m_h\le\frac{F(x+h)-F(x)}{h}\le M_h.$$
3. As $h\to0$, the interval $[x,x+h]$ shrinks to the point $x$, and by continuity of $f$ both $m_h\to f(x)$ and $M_h\to f(x)$. By the **Squeeze Theorem** (§s4) the difference quotient is trapped and also $\to f(x)$. (For $h<0$ the same argument applies on $[x+h,x]$ with the inequalities oriented accordingly.) Therefore $F'(x)=f(x)$. $\blacksquare$

*Every continuous function **has** an antiderivative — namely its own running integral.*

#### FTC — Part II (evaluating an integral)

$$G'=f \text{ on } [a,b],\ f \text{ integrable}\ \Rightarrow\ \int_a^b f(x)\,dx=G(b)-G(a).$$

**Proof — FTC Part II via the MVT**

1. Take any partition $a=x_0<x_1<\cdots<x_n=b$. Write $G(b)-G(a)$ as a **telescoping** sum (consecutive terms cancel):

   $$G(b)-G(a)=\sum_{i=1}^{n}\big(G(x_i)-G(x_{i-1})\big).$$
2. Apply the **MVT** (§s7) to $G$ on each subinterval $[x_{i-1},x_i]$: there is $c_i$ in it with $G(x_i)-G(x_{i-1})=G'(c_i)\,\Delta x_i=f(c_i)\,\Delta x_i$ (using $G'=f$). So $G(b)-G(a)=\sum_i f(c_i)\,\Delta x_i$.
3. On each subinterval $m_i\le f(c_i)\le M_i$ (the sample value lies between the local inf and sup), so multiplying by $\Delta x_i>0$ and summing, the constant $G(b)-G(a)$ is trapped:

   $$L(f,P)\le G(b)-G(a)\le U(f,P).$$
4. Since $f$ is integrable, by Riemann's criterion (§s8) we can make $U(f,P)-L(f,P)<\varepsilon$, so both bounds are within $\varepsilon$ of $\int_a^b f$. The fixed number $G(b)-G(a)$ lies between them for *every* partition, hence within $\varepsilon$ of $\int_a^b f$ for every $\varepsilon$; therefore $G(b)-G(a)=\int_a^b f$. $\blacksquare$

**Worked example.** To compute $\int_0^2 3x^2\,dx$: an antiderivative is $G(x)=x^3$ (since $G'=3x^2$), so by FTC II the value is $G(2)-G(0)=8-0=8$.

> **Connection — "find the antiderivative, plug in the endpoints"**
>
> The computational rule $\int_a^b f = G(b)-G(a)$ you used from day one *is* FTC Part II. Part I is its silent partner: it guarantees the antiderivative $G$ exists in the first place for any continuous $f$, so the rule always has something to apply.

<a id="s10"></a>
### Sequences & series of functions: pointwise vs uniform convergence

*When a limit is itself a function, "how" it converges matters enormously. The distinction between pointwise and uniform is where naïve calculus breaks.*

Now the objects converging are whole **functions** $f_1,f_2,\dots$, and we ask in what sense they approach a limit function $f$.

#### Definition — pointwise convergence

$$f_n\to f \text{ pointwise} \iff \forall x\ \forall\varepsilon>0\ \exists N(x,\varepsilon):\ n\ge N\Rightarrow|f_n(x)-f(x)|\lt\varepsilon.$$

*This is just ordinary numerical convergence (§s2) at each fixed input $x$, one $x$ at a time. The notation $N(x,\varepsilon)$ stresses that the threshold may depend on **both** the tolerance and the point — different points may converge at wildly different rates.*

#### Definition — uniform convergence

$$f_n\to f \text{ uniformly} \iff \forall\varepsilon>0\ \exists N\ \forall x\ \forall n\ge N:\ |f_n(x)-f(x)|\lt\varepsilon.$$

$$\text{equivalently}\quad \sup_x|f_n(x)-f(x)|\to 0.$$

*The decisive change is again **quantifier order**: "$\exists N$" now precedes "$\forall x$," so **one $N$ serves all $x$ at once** — the entire graph of $f_n$ lies inside an $\varepsilon$-thick band around the graph of $f$. Uniform convergence implies pointwise (a single $N$ certainly works for each individual $x$), but not conversely.*

> **Concept — the cautionary example**
>
> On $[0,1]$, $f_n(x)=x^n$ converges pointwise to the limit $f$ given by $f(x)=0$ for $0\le x<1$ and $f(1)=1$ — a **discontinuous** limit of continuous functions. The convergence is **not** uniform: for any $n$, at $x$ close to $1$ the value $x^n$ is still near $1$, so $\sup_{x\in[0,1)}|x^n-0|=1\not\to0$. Pointwise convergence does not preserve continuity; uniform convergence will (§s11).

To verify $x^n$ is not uniform concretely: take $\varepsilon=\tfrac12$. For any proposed $N$, the point $x=(\tfrac12)^{1/N}\in(0,1)$ gives $f_N(x)=x^N=\tfrac12\not<\tfrac12$, so no single $N$ pushes *all* points within $\tfrac12$ of $0$.

#### Theorem — Weierstrass M-test

$$|f_n(x)|\le M_n\ \forall x,\quad \sum_n M_n\lt\infty\ \Rightarrow\ \sum_n f_n \text{ converges uniformly (and absolutely).}$$

*A convergent numerical series of bounds ("$\sum M_n<\infty$" means the partial sums of the constants $M_n$ converge) forces uniform convergence of the function series — the everyday tool for proving power series converge uniformly (§s12).*

**Proof — the M-test (via the Cauchy criterion for uniform convergence)**

1. Let $S_n=\sum_{k=1}^n f_k$ be the partial sums. For $m>n$ and any $x$, bound the block by the corresponding block of constants, using the triangle inequality and $|f_k(x)|\le M_k$:

   $$|S_m(x)-S_n(x)|=\Big|\sum_{k=n+1}^{m} f_k(x)\Big|\le\sum_{k=n+1}^{m}|f_k(x)|\le\sum_{k=n+1}^{m} M_k.$$
2. Since $\sum M_k$ converges, its partial sums form a convergent (hence Cauchy, §s3) sequence; so given $\varepsilon>0$ there is $N$ with $\sum_{k=n+1}^{m}M_k<\varepsilon$ for all $m>n\ge N$. Crucially this bound does **not** depend on $x$.
3. Therefore $\sup_x|S_m(x)-S_n(x)|\le\sum_{k=n+1}^m M_k<\varepsilon$ for $m>n\ge N$: the partial sums are **uniformly Cauchy**. At each fixed $x$ they form a Cauchy sequence of reals, which converges (§s3) to some value $S(x)$; and the uniform Cauchy bound, holding for all $x$, makes $S_n\to S$ uniformly. $\blacksquare$

*The numerical tail controls the function tail uniformly.*

<a id="s11"></a>
### Consequences of uniform convergence

*Uniform convergence is precisely the strength needed to interchange limits with continuity, integration, and (with care) differentiation.*

#### Theorem — uniform limit of continuous functions is continuous

$$f_n \text{ continuous},\ f_n\to f \text{ uniformly}\ \Rightarrow\ f \text{ continuous.}$$

**Proof — continuity is preserved (the $\varepsilon/3$ argument)**

1. Fix a point $a$ and tolerance $\varepsilon>0$. By **uniform convergence**, choose one index $n$ with $\sup_x|f_n(x)-f(x)|<\tfrac\varepsilon3$ — so both $|f_n(x)-f(x)|<\tfrac\varepsilon3$ for every $x$ and $|f_n(a)-f(a)|<\tfrac\varepsilon3$.
2. That single $f_n$ is continuous at $a$ (hypothesis), so there is $\delta>0$ with $|x-a|<\delta\Rightarrow|f_n(x)-f_n(a)|<\tfrac\varepsilon3$.
3. For $|x-a|<\delta$, route from $f(x)$ to $f(a)$ through $f_n(x)$ and $f_n(a)$ with the triangle inequality:

   $$|f(x)-f(a)|\le|f(x)-f_n(x)|+|f_n(x)-f_n(a)|+|f_n(a)-f(a)|\lt\tfrac\varepsilon3+\tfrac\varepsilon3+\tfrac\varepsilon3=\varepsilon.$$
4. Since $\varepsilon$ was arbitrary, $f$ is continuous at $a$; as $a$ was arbitrary, $f$ is continuous. $\blacksquare$

*The outer two thirds need uniformity (one $n$ for all $x$); the middle third is plain continuity of $f_n$. With only pointwise convergence, step 1 could not pin down a single $n$ valid near $a$, and the $x^n$ example (§s10) shows the conclusion can genuinely fail.*

#### Theorem — interchange of limit and integral

$$f_n\to f \text{ uniformly on } [a,b],\ f_n \text{ integrable}\ \Rightarrow\ \int_a^b f_n\to\int_a^b f.$$

**Proof — uniform convergence lets you integrate term-by-term**

1. Let $\varepsilon_n=\sup_x|f_n(x)-f(x)|$; uniform convergence says $\varepsilon_n\to0$. (One can show $f$ is integrable as well, since $U(f,P)-L(f,P)$ differs from that of $f_n$ by at most $2\varepsilon_n(b-a)$; we take this for the estimate.)
2. The difference of integrals is the integral of the difference (linearity), and the absolute value of an integral is at most the integral of the absolute value:

   $$\Big|\int_a^b f_n-\int_a^b f\Big|=\Big|\int_a^b (f_n-f)\Big|\le\int_a^b |f_n-f|.$$
3. Pointwise $|f_n(x)-f(x)|\le\varepsilon_n$ for all $x$ (definition of $\sup$), so integrating the constant bound:

   $$\int_a^b|f_n-f|\le\varepsilon_n\,(b-a)\ \longrightarrow\ 0.$$
4. Hence $\int_a^b f_n\to\int_a^b f$. $\blacksquare$

*The $\sup$-bound $\varepsilon_n$ times the interval length controls the whole integral. Pointwise convergence is **not** enough — a moving "spike" of height $n$ and width $1/n$ converges pointwise to $0$ at every fixed point, yet keeps area $1$, so $\int f_n=1\not\to0=\int f$.*

#### Theorem — differentiating a limit (the delicate case)

$$f_n\to f \text{ pointwise},\ f_n' \text{ continuous},\ f_n'\to g \text{ uniformly}\ \Rightarrow\ f'=g.$$

**Proof sketch with full reasoning.** By FTC Part II (§s9), $f_n(x)-f_n(x_0)=\int_{x_0}^x f_n'(t)\,dt$. The integrands converge uniformly to $g$, so by the interchange theorem just proved the right side $\to\int_{x_0}^x g(t)\,dt$; the left side $\to f(x)-f(x_0)$ by pointwise convergence. Thus $f(x)-f(x_0)=\int_{x_0}^x g$, and since $g$ is continuous (a uniform limit of the continuous $f_n'$, by the theorem above), FTC Part I (§s9) gives $f'(x)=g(x)$. $\blacksquare$

*Differentiation does **not** commute with mere uniform convergence of $f_n$; you must assume the **derivatives** converge uniformly. This is why the hypothesis is on $f_n'$, not $f_n$.*

> **Connection — when "swap the order" is legal**
>
> Casually swapping $\lim$ with $\int$ or $\frac{d}{dx}$, or summing a series term-by-term, is justified *exactly* by uniform convergence. The famous failures of interchange in early calculus are all cases where convergence was only pointwise.

<a id="s12"></a>
### Power series & analytic functions

*Power series are the best-behaved infinite sums — inside their disk they converge uniformly on compacts and may be differentiated and integrated term-by-term freely.*

A **power series** centered at $a$ is a series of the form $\sum_{n=0}^\infty c_n(x-a)^n$, with fixed coefficients $c_n$ and variable $x$. The set of $x$ where it converges turns out to be an interval centered at $a$, whose half-width $R$ we now determine.

#### Definition & theorem — radius of convergence

$$\sum_{n=0}^{\infty} c_n (x-a)^n,\qquad \frac1R=\limsup_{n\to\infty}|c_n|^{1/n}\quad(\text{Cauchy–Hadamard}).$$

*The number $R\in[0,\infty]$ is the **radius of convergence**: the series converges absolutely for $|x-a|<R$ and diverges for $|x-a|>R$. The use of $\limsup$ (§s4) — which always exists — is what makes $R$ always well-defined, even when $|c_n|^{1/n}$ has no ordinary limit.*

**Proof — convergence inside the radius, with uniform convergence on compacts**

1. Fix any $r<R$. Choose a number $\rho$ strictly between them, $r<\rho<R$. From $\tfrac1R=\limsup|c_n|^{1/n}<\tfrac1\rho$, the definition of $\limsup$ as the eventual ceiling (§s4) gives: for all large $n$, $|c_n|^{1/n}<\tfrac1\rho$, i.e. $|c_n|<\rho^{-n}$.
2. For any $x$ with $|x-a|\le r$ and all such large $n$:

   $$|c_n(x-a)^n|=|c_n|\,|x-a|^n\le|c_n|\,r^n<\rho^{-n}r^n=(r/\rho)^n=:M_n.$$
   Since $r/\rho<1$, the series $\sum M_n=\sum(r/\rho)^n$ is a convergent geometric series.
3. By the **Weierstrass M-test** (§s10), the power series converges uniformly (and absolutely) on the closed disk $\{|x-a|\le r\}$:

   $$\sum_n |c_n(x-a)^n|\le\sum_n (r/\rho)^n=\frac{1}{1-r/\rho}\lt\infty.$$
   As $r<R$ was arbitrary, we get absolute convergence at every point of $|x-a|<R$ and uniform convergence on every closed sub-disk. (For $|x-a|>R$, the terms do not even tend to $0$, so the series diverges.) $\blacksquare$

**Worked example.** For $\sum x^n/n!$ (the series for $e^x$), $c_n=1/n!$. Using $n!\ge(n/e)^n$ one gets $|c_n|^{1/n}=(n!)^{-1/n}\le e/n\to0$, so $\limsup|c_n|^{1/n}=0$, hence $R=\infty$: the exponential series converges for all $x$, uniformly on every bounded interval.

> **Theorem — term-by-term calculus**
>
> Inside $|x-a|\lt R$, a power series defines an infinitely differentiable function; it may be **differentiated and integrated term-by-term**, and the resulting series have the same radius $R$. Consequently $c_n=\dfrac{f^{(n)}(a)}{n!}$: the series is its own Taylor series. This follows from §s11 applied on each compact sub-disk where convergence is uniform.

> **Concept — analytic, and why $C^\infty\ne$ analytic**
>
> A function is **analytic** at $a$ if it equals a convergent power series near $a$. ($C^\infty$ means infinitely differentiable.) Analytic $\Rightarrow C^\infty$, but **not** conversely: $f(x)=e^{-1/x^2}$ (with $f(0)=0$) is smooth yet has *all* derivatives zero at $0$, so its Taylor series is the zero series and does **not** represent $f$ (which is positive for $x\ne0$). Smoothness is strictly weaker than analyticity.

> **Connection — Taylor series, finally justified**
>
> Writing $e^x=\sum x^n/n!$ or $\sin x=\sum(-1)^n x^{2n+1}/(2n+1)!$ and manipulating them termwise — differentiating, integrating, multiplying — is rigorous precisely because power series converge uniformly on compacts. The remainder estimate of §s7 tells you *when* the Taylor series actually converges back to $f$.

<a id="s13"></a>
### A glimpse beyond: metric spaces, multivariable rigor & Lebesgue

*The same $\varepsilon$-ideas generalize far past the real line. A short tour of where analysis goes next.*

#### Metric spaces — abstracting distance

The only thing the $\varepsilon$-definitions truly used about $\mathbb{R}$ was the distance $|x-y|$ and its triangle inequality. Abstract that into a **metric** $d$ — a distance function on any set — required to satisfy:

$$d(x,y)\ge 0,\ \ d(x,y)=0\iff x=y,\ \ d(x,y)=d(y,x),\ \ d(x,z)\le d(x,y)+d(y,z).$$

*(In words: distances are nonnegative; zero distance means identical points; distance is symmetric; and the triangle inequality holds.) Replace $|x-y|$ by such a $d$ and every $\varepsilon$-definition transfers verbatim — limits, continuity, Cauchy sequences, compactness all read the same. $\mathbb{R}^n$ (with $d$ the straight-line distance), spaces of functions, and spaces of sequences all become arenas for the same theorems.*

> **Concept — completeness, abstractly & the contraction principle**
>
> A metric space is **complete** if every Cauchy sequence converges — the abstract version of §s3's theorem for $\mathbb{R}$. In a complete space, the **Banach fixed-point theorem** guarantees that a contraction (a map $T$ with $d(Tx,Ty)\le k\,d(x,y)$ for some fixed $k<1$) has a unique fixed point, found by iterating $T$ from any start. This single result proves existence and uniqueness for differential equations (Picard–Lindelöf) and the inverse function theorem.

> **Concept — multivariable rigor**
>
> In $\mathbb{R}^n$ the derivative becomes a **linear map** (the total derivative / Jacobian), defined by the best linear approximation $f(a+h)=f(a)+Df(a)\,h+o(\|h\|)$, where "$o(\|h\|)$" means an error shrinking faster than $\|h\|$. Merely having partial derivatives is **not** enough for differentiability; one needs them continuous. The MVT weakens to an inequality, and the Implicit and Inverse Function Theorems — proved via the contraction principle above — replace the one-variable algebra.

> **Concept — the Lebesgue integral**
>
> The Riemann integral chokes on badly discontinuous functions (the Dirichlet function, §s8) and behaves poorly under limits. **Lebesgue's** idea: partition the *range*, not the domain, and measure how much of the domain maps into each range slice. This integrates far more functions, and yields clean convergence theorems (Monotone & Dominated Convergence) under which $\lim\int=\int\lim$ holds with mild hypotheses — repairing the fragility of interchanging limits with Riemann integrals seen in §s11.

> **Connection — one idea, endlessly reused**
>
> From $\varepsilon$–$N$ for sequences to $\varepsilon$–$\delta$ for functions, to $d(x,y)$ in metric spaces, to measure-theoretic integration — it is the *same* move: control a quantity to within any prescribed tolerance. Master that one habit and all of analysis, however abstract, is familiar territory.

---

*A rigorous first course in real analysis — the theory beneath the Complete Calculus and Derived from Scratch guides. Every limit is an $\varepsilon$; every theorem is proved from the completeness of $\mathbb{R}$. Read once for the architecture, then return to any proof box as a reference. Remember the single thread: control any quantity to within any tolerance, and infinity becomes safe.*
