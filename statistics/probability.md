**English** · [中文](probability.zh.md)

# Probability, *made rigorous.*

A full course in mathematical probability — from Kolmogorov's axioms through random variables and their moments to the limit theorems that anchor all of statistics. Every core result is **demonstrated**, and the threads to calculus and inference are made explicit.

[← Back to all guides](../README.md)

> **How to read this guide.** This version assumes *no* prior mathematics beyond basic arithmetic and a little algebra. Every symbol is defined in words the first time it appears, every formula is stated plainly before it is used, and every claim is proved in a numbered list where each step says both *what* is done and *why* it is allowed. Whenever a later section needs an earlier result, that result is restated in one line. Nothing is left "to the reader."

## Part A · Foundations

<a id="s0"></a>
### The big picture: chance made rigorous

*Probability is the mathematics of uncertainty — a calculus of how likely things are, built on a tiny set of axioms and reaching all the way to the deep limit theorems.*

For centuries probability was a collection of clever tricks for gamblers. In 1933 Andrey Kolmogorov gave it a rigorous foundation: probability is simply a **measure** — a way of assigning a "size" between 0 and 1 to subsets of a space of outcomes. From three short axioms, the entire subject unfolds by deduction.

#### What "probability" is going to mean

Imagine any experiment whose result you cannot predict with certainty: flipping a coin, rolling a die, measuring tomorrow's temperature. Probability theory is a precise language for talking about such experiments. It has exactly three ingredients, and everything else is built from them:

- **Model** — encode an experiment as a sample space, events, and a probability measure. The *sample space* is the list of everything that could happen; an *event* is a question with a yes/no answer ("did we roll an even number?"); the *probability measure* is the rule that assigns each event a number measuring how likely it is.
- **Quantify** — attach numbers to outcomes via *random variables* (a random variable is just a measurement read off the result of the experiment), and summarize them with expectation (the long-run average), variance (how spread out the values are), and moments (finer shape information).
- **Take limits** — let the number of repetitions grow, and watch order emerge: the laws of large numbers (averages settle down) and the central limit theorem (those averages become bell-shaped).

#### A first worked example to fix ideas

Roll one fair six-sided die. The list of possible results is $\{1,2,3,4,5,6\}$. Because the die is fair, each face is equally likely, so each has probability $1/6$. The event "the result is even" is the set $\{2,4,6\}$, which contains $3$ of the $6$ outcomes, so its probability is $3/6 = 1/2$. We just used the rule "favorable outcomes divided by total outcomes" — the simplest possible probability calculation, and the one §s1 will justify rigorously.

> **Principle — the two faces of probability**
>
> The **frequentist** reading says $P(A)$ (read "the probability of event $A$") is the long-run fraction of times $A$ occurs in repeated trials; the **subjective** reading says it is a coherent degree of belief. Kolmogorov's axioms are neutral: they describe what any sensible notion of probability must satisfy, leaving the interpretation to you. The mathematics is the same either way.

#### The whole subject on one line

> Axioms → Conditioning & Bayes → Random variables & moments → Joint behavior → Inequalities → Laws of large numbers & the CLT

Read left to right, this is the dependency chain of the entire guide. Each arrow means "the next topic is built out of the previous one." Keep it in mind as a map.

> **Connection — probability is the engine under statistics**
>
> In the companion *Statistics* guide, probability runs "population $\to$ sample" while inference runs "sample $\to$ population." This guide builds that engine in full: the sampling distributions, standard errors, and Normal approximations used there are theorems proved here in Part D.

<a id="s1"></a>
### Sample spaces, events & the axioms (Kolmogorov)

*Everything begins with a set of outcomes, a collection of events, and a measure on them.*

#### Defining the pieces

Before any formula, here are the words.

- An **outcome**, written $\omega$ (the Greek letter omega), is one complete result of the experiment — for one die roll, an outcome is a single number like $3$.
- The **sample space** $\Omega$ (capital omega) is the *set* (collection) of *all* possible outcomes. For one die, $\Omega=\{1,2,3,4,5,6\}$.
- An **event** is a subset of $\Omega$ — any collection of outcomes we might ask about. "Even" is the event $\{2,4,6\}$. The empty set $\varnothing$ (the event containing no outcomes, "nothing happens") and the whole space $\Omega$ ("something happens") are both events.
- The **complement** of an event $A$, written $A^c$, is the set of all outcomes *not* in $A$ — "$A$ did not happen."
- A **union** $A\cup B$ is the event "$A$ or $B$ (or both) happened"; an **intersection** $A\cap B$ is "$A$ and $B$ both happened." Two events are **disjoint** (or *mutually exclusive*) if they cannot both happen, i.e. $A\cap B=\varnothing$.

> **Concept — the probability triple**
>
> A probability model is a triple $(\Omega,\mathcal F,P)$. The **sample space** $\Omega$ is the set of all possible outcomes $\omega$. The **event space** $\mathcal F$ (script F) is a collection of subsets of $\Omega$ (the events) closed under complements and countable unions — a structure called a $\sigma$-algebra ("sigma-algebra"). "Closed under complements and countable unions" means: if $A$ is an event then $A^c$ is too, and if $A_1,A_2,\dots$ are events then so is their union. The **probability measure** $P:\mathcal F\to[0,1]$ assigns each event a number between $0$ and $1$ (its likelihood). The notation $P:\mathcal F\to[0,1]$ reads "$P$ is a function taking an event and returning a number in the interval from $0$ to $1$."

**Kolmogorov's axioms**

An *axiom* is a starting rule we simply require, without proof; the whole theory is what we can deduce from these three.

$$\text{(1)}\ \ P(A)\ge 0\quad\text{for all }A\in\mathcal F$$

$$\text{(2)}\ \ P(\Omega)=1$$

$$\text{(3)}\ \ P\!\Big(\bigcup_{i=1}^{\infty}A_i\Big)=\sum_{i=1}^{\infty}P(A_i)\quad\text{for disjoint }A_i$$

In words: (1) probabilities are never negative; (2) the probability that *something* in $\Omega$ happens is exactly $1$ (certainty); (3) if you have a list of events $A_1,A_2,\dots$, no two of which can happen together, then the probability that *some one* of them happens equals the sum of their individual probabilities. The big union symbol $\bigcup_{i=1}^{\infty}A_i$ means "$A_1$ or $A_2$ or $A_3$ or ..." and the big sum $\sum_{i=1}^{\infty}P(A_i)$ means "$P(A_1)+P(A_2)+\cdots$."

*Axiom (3) is **countable additivity** — the one assumption that does the real work, giving continuity of probability and making limits behave.*

**Demonstration — consequences forced by the axioms**

We now prove three facts that are *not* axioms but follow from them. Each step names the rule it uses.

1. **Complement rule and the empty set.** The events $A$ and $A^c$ are disjoint (an outcome cannot be both in $A$ and not in $A$) and together make up everything: $A\cup A^c=\Omega$. Apply axiom (3) to the two-event list $A,A^c$ (a finite list is allowed: pad it with empty sets, which we handle below) to get $P(A)+P(A^c)=P(\Omega)$. By axiom (2), $P(\Omega)=1$. Therefore

   $$P(A^c)=1-P(A),\qquad P(\varnothing)=0.$$

   The second equation comes from taking $A=\Omega$: then $A^c=\varnothing$, so $P(\varnothing)=1-P(\Omega)=1-1=0$.
2. **Monotonicity (bigger event, bigger probability).** Suppose $A\subseteq B$ ("every outcome in $A$ is also in $B$"). The set $B\setminus A$ ("the part of $B$ outside $A$") is disjoint from $A$, and together they rebuild $B$: $B=A\cup(B\setminus A)$. By additivity (axiom 3), $P(B)=P(A)+P(B\setminus A)$. By axiom (1), $P(B\setminus A)\ge0$, so $P(B)\ge P(A)$. Thus larger events have at least as large a probability. Combined with $P(A)\ge0$ and $P(A)=1-P(A^c)\le 1$, this gives $0\le P(A)\le 1$ for every event.
3. **Inclusion–exclusion for two events.** We want $P(A\cup B)$ without double-counting the overlap. Split each piece into disjoint parts. First, $A\cup B = A\cup(B\setminus A)$, a disjoint union, so by additivity $P(A\cup B)=P(A)+P(B\setminus A)$. Second, $B=(A\cap B)\cup(B\setminus A)$, also disjoint, so $P(B)=P(A\cap B)+P(B\setminus A)$, i.e. $P(B\setminus A)=P(B)-P(A\cap B)$. Substitute the second into the first:

   $$P(A\cup B)=P(A)+P(B)-P(A\cap B).$$

*The inclusion–exclusion rule is not an axiom — it is a theorem. So is monotonicity, and so is $0\le P(A)\le1$.*

**Worked example — inclusion–exclusion with a die.** Let $A=\{2,4,6\}$ (even) and $B=\{4,5,6\}$ (greater than $3$). Then $P(A)=3/6$, $P(B)=3/6$, and $A\cap B=\{4,6\}$ so $P(A\cap B)=2/6$. The formula gives $P(A\cup B)=3/6+3/6-2/6=4/6=2/3$. Check by listing: $A\cup B=\{2,4,5,6\}$, which is $4$ of $6$ outcomes, $=2/3$. The formula and the direct count agree.

**Inclusion–exclusion & continuity**

The two-event rule extends to any finite number of events:

$$P\!\Big(\bigcup_{i=1}^n A_i\Big)=\sum_i P(A_i)-\sum_{i\lt j}P(A_i\cap A_j)+\cdots+(-1)^{n+1}P\!\Big(\bigcap_{i=1}^n A_i\Big)$$

The pattern: add all single-event probabilities, subtract all pairwise overlaps, add back all triple overlaps, and so on, alternating signs. The factor $(-1)^{n+1}$ just produces this alternating $+,-,+,\dots$ pattern.

$$A_n\uparrow A\ \Rightarrow\ P(A_n)\to P(A),\qquad A_n\downarrow A\ \Rightarrow\ P(A_n)\to P(A)$$

Here $A_n\uparrow A$ means the events grow: $A_1\subseteq A_2\subseteq\cdots$ and their union is $A$; $A_n\downarrow A$ means they shrink to $A$. The arrow "$\to$" means "approaches as $n$ grows without bound."

*Continuity from below/above is a direct consequence of countable additivity; it is what lets us pass to limits of events.* (Sketch: for growing events, write $A$ as the disjoint union of the "new pieces" $A_n\setminus A_{n-1}$ and apply axiom (3); the partial sums of a convergent series approach the full sum.)

> **Concept — equally likely outcomes**
>
> When $\Omega$ is finite with all outcomes equally likely, the measure collapses to counting: $P(A)=|A|/|\Omega|$, where $|A|$ means "the number of outcomes in $A$." This is the classical "favorable over total" probability — and it is exactly why the next section is about counting.

<a id="s2"></a>
### Counting: permutations, combinations & the binomial theorem

*In a uniform model, probability is counting. The combinatorics here powers every discrete distribution that follows.*

Recall from §s1: when all outcomes are equally likely, $P(A)=|A|/|\Omega|$. So to find probabilities we must count sets. Two ideas dominate: arrangements where *order matters* (permutations) and selections where it *does not* (combinations).

#### Definitions

- The **factorial** $n!$ (read "$n$ factorial") means $n!=n\times(n-1)\times\cdots\times2\times1$, the product of all whole numbers from $1$ up to $n$. By convention $0!=1$. For example $4!=4\cdot3\cdot2\cdot1=24$.
- A **permutation** is an ordered arrangement; a **combination** is an unordered selection.

**The fundamental counting principles**

$$\text{permutations: }\ P(n,k)=\frac{n!}{(n-k)!},\qquad \text{combinations: }\ \binom nk=\frac{n!}{k!\,(n-k)!}$$

The symbol $\binom nk$ is read "$n$ choose $k$" — the number of ways to pick $k$ items from $n$ when order is ignored.

*If a task is a sequence of independent choices with $n_1,n_2,\dots$ options, the total is the **product** $n_1 n_2\cdots$. Permutations count ordered arrangements; combinations count unordered selections.* This product rule is intuitive: if you choose a shirt ($3$ options) then a hat ($2$ options), there are $3\times2=6$ outfits, because each shirt pairs with each hat.

**Demonstration — why $\binom nk$ divides out the orderings**

1. **Count ordered lists.** To build an ordered list of $k$ distinct items chosen from $n$: the first slot has $n$ choices, the second has $n-1$ (one item used up), and so on down to the $k$th slot with $n-k+1$ choices. By the product rule (just stated), the number of ordered lists is $P(n,k)=n(n-1)\cdots(n-k+1)$. Multiplying and dividing by $(n-k)!$ turns the tail into a full factorial: $P(n,k)=\tfrac{n!}{(n-k)!}$.
2. **Each unordered set was counted many times.** A single set of $k$ items can be arranged into $k!$ different ordered lists (by step 1 with $n=k$: $P(k,k)=k!$). So in the count of ordered lists, every unordered set appears exactly $k!$ times.
3. **Divide to remove the overcount.** Dividing the ordered count by $k!$ leaves the unordered count:

   $$\binom nk=\frac{P(n,k)}{k!}=\frac{n!}{k!\,(n-k)!}.$$

*The binomial coefficient is "choose $k$, ignoring order."*

**Worked example — a poker-style count.** How many $2$-card hands come from a $5$-card deck? Order does not matter, so $\binom52=\tfrac{5!}{2!\,3!}=\tfrac{120}{2\cdot6}=\tfrac{120}{12}=10$. Listing confirms: from cards $\{a,b,c,d,e\}$ the pairs are $ab,ac,ad,ae,bc,bd,be,cd,ce,de$ — exactly $10$.

**The binomial theorem & Pascal's rule**

$$(x+y)^n=\sum_{k=0}^{n}\binom nk x^k y^{n-k},\qquad \binom nk=\binom{n-1}{k-1}+\binom{n-1}{k}$$

*Setting $x=y=1$ gives $\sum_k\binom nk=2^n$: the number of subsets of an $n$-set. Pascal's rule builds the triangle row by row.* (Pascal's rule says each entry is the sum of the two above it.)

**Demonstration — the binomial theorem by counting**

1. **Write out the product.** $(x+y)^n=\underbrace{(x+y)(x+y)\cdots(x+y)}_{n\text{ factors}}$. When you multiply this out, every term is formed by picking either $x$ or $y$ from each of the $n$ factors and multiplying the picks together.
2. **Group terms by how many $x$'s appear.** A term that took $x$ from exactly $k$ of the factors (and $y$ from the other $n-k$) equals $x^k y^{n-k}$. The number of ways to decide *which* $k$ of the $n$ factors supply the $x$ is, by definition from the previous demonstration, $\binom nk$ (an unordered choice of $k$ factors out of $n$).
3. **Sum over all possible $k$.** Adding up the contributions for $k=0,1,\dots,n$:

   $$(x+y)^n=\sum_{k=0}^n\binom nk x^k y^{n-k}.$$

**Worked example — checking $n=3$.** $(x+y)^3=\binom30 y^3+\binom31 x y^2+\binom32 x^2 y+\binom33 x^3 = y^3+3xy^2+3x^2y+x^3$. Setting $x=y=1$: $\binom30+\binom31+\binom32+\binom33=1+3+3+1=8=2^3$, the number of subsets of a $3$-element set — confirming the identity.

*This identity is precisely why the binomial distribution's probabilities sum to 1* (we will use it in §s7).

> **Concept — distinguishable vs not, replacement vs not**
>
> The four classic counting regimes: ordered with replacement $n^k$ (each of $k$ picks independently chooses among $n$); ordered without $\tfrac{n!}{(n-k)!}$; unordered without $\binom nk$; unordered with replacement $\binom{n+k-1}{k}$ (the "stars and bars" formula). "With replacement" means an item can be chosen again; "without" means it cannot. Identifying which regime you are in is the whole art of combinatorial probability.

<a id="s3"></a>
### Conditional probability, independence & Bayes' theorem

*How information reshapes probability — and how to invert the direction of conditioning.*

#### The idea of conditioning

Sometimes we learn a partial fact before the full result is known, and we want to update our probabilities. "Given that the die came up even, what is the chance it is a $4$?" *Conditioning* is the operation that performs this update.

**Conditioning, the chain rule & independence**

$$P(A\mid B)=\frac{P(A\cap B)}{P(B)}\quad(P(B)\gt0)$$

Read $P(A\mid B)$ as "the probability of $A$ given $B$." The definition says: restrict attention to the world where $B$ happened (so $P(B)$ becomes the new "total"), and ask what fraction of that world also has $A$ (the overlap $A\cap B$). We need $P(B)>0$ so we are not dividing by zero.

$$P(A_1\cap\cdots\cap A_n)=P(A_1)\,P(A_2\mid A_1)\cdots P(A_n\mid A_1\cap\cdots\cap A_{n-1})$$

This is the **chain rule**: the probability that *all* of several events happen can be built up one event at a time, each conditioned on those before it.

$$A\perp B \iff P(A\cap B)=P(A)P(B) \iff P(A\mid B)=P(A)$$

The symbol $A\perp B$ means "$A$ and $B$ are independent." The double arrow $\iff$ means "is equivalent to / true exactly when."

*Conditioning on $B$ restricts the world to $B$ and renormalizes. Independence means $B$ carries no information about $A$* — learning $B$ does not change the probability of $A$.

**Demonstration — the chain rule for two then many events.**

1. By the definition above, $P(A_2\mid A_1)=\tfrac{P(A_1\cap A_2)}{P(A_1)}$. Multiply both sides by $P(A_1)$: $P(A_1\cap A_2)=P(A_1)P(A_2\mid A_1)$. That is the chain rule for two events.
2. To extend, treat $A_1\cap\cdots\cap A_{n-1}$ as a single event $B$ and apply the two-event rule to $B$ and $A_n$; repeating peels off one factor at a time, producing the full product.

**Worked example — the equivalence of the two independence forms.** If $P(A\cap B)=P(A)P(B)$, divide both sides by $P(B)$ (assuming $P(B)>0$): the left side becomes $P(A\mid B)$ by definition, the right becomes $P(A)$. So $P(A\mid B)=P(A)$. The steps reverse, so the two conditions are equivalent. Numerically: a fair die, $A=\{$even$\}$ with $P(A)=1/2$, $B=\{$at most $4\}=\{1,2,3,4\}$ with $P(B)=4/6$. Then $A\cap B=\{2,4\}$, $P(A\cap B)=2/6=1/3$, and $P(A)P(B)=\tfrac12\cdot\tfrac46=\tfrac13$. They match, so $A$ and $B$ are independent here.

**Law of total probability & Bayes' theorem**

A **partition** $\{A_i\}$ of $\Omega$ is a collection of disjoint events that together cover everything (exactly one $A_i$ happens). Then:

$$P(B)=\sum_i P(B\mid A_i)\,P(A_i)\quad\text{for a partition }\{A_i\}$$

$$P(A_i\mid B)=\frac{P(B\mid A_i)\,P(A_i)}{\sum_j P(B\mid A_j)\,P(A_j)}$$

**Demonstration — law of total probability, then Bayes' theorem**

1. **Total probability.** Since the $A_i$ partition $\Omega$, the events $B\cap A_i$ are disjoint and their union is $B$. By additivity (axiom 3, §s1), $P(B)=\sum_i P(B\cap A_i)$. By the chain rule (above), $P(B\cap A_i)=P(B\mid A_i)P(A_i)$. Substituting gives the displayed formula.
2. **Two ways to write the joint.** The chain rule gives the joint probability of $A$ and $B$ in two directions:

   $$P(A\cap B)=P(A\mid B)P(B)=P(B\mid A)P(A).$$
3. **Solve for the reversed conditional.** Equate the right-hand expressions and divide by $P(B)$ (assume $P(B)>0$):

   $$P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}.$$

   Finally expand $P(B)$ by total probability over a partition $\{A_j\}$ to get the denominator $\sum_j P(B\mid A_j)P(A_j)$, which yields the boxed Bayes formula.

*Bayes turns "likelihood of the evidence given the cause" into "probability of the cause given the evidence."*

**Worked example — a medical test (base rates).** A disease affects $1\%$ of people, so the prior is $P(D)=0.01$ and $P(D^c)=0.99$. A test is $99\%$ accurate both ways: $P(+\mid D)=0.99$ (true positive) and $P(+\mid D^c)=0.01$ (false positive). A person tests positive — what is the chance they are sick? By Bayes:

$$P(D\mid +)=\frac{P(+\mid D)P(D)}{P(+\mid D)P(D)+P(+\mid D^c)P(D^c)}=\frac{0.99\cdot0.01}{0.99\cdot0.01+0.01\cdot0.99}=\frac{0.0099}{0.0198}=0.5.$$

Despite the "$99\%$ accurate" test, the chance of actually being sick is only $50\%$, because healthy people vastly outnumber sick ones and supply just as many positives.

> **Principle — base rates dominate**
>
> For a rare condition, even a highly accurate test yields many false positives, because the few true cases are swamped by the large healthy majority. Bayes forces you to weight the test result by the **prior** $P(A)$. This single insight underlies medical screening, spam filtering, and all of Bayesian inference.

> **Concept — pairwise vs mutual independence**
>
> Events can be pairwise independent yet not mutually independent: independence of every pair does not force $P(A\cap B\cap C)=P(A)P(B)P(C)$. Mutual independence requires the product rule to hold for *every* sub-collection — a strictly stronger condition.

> **Connection — forward to inference**
>
> Bayes' theorem is the hinge between this guide and statistical inference: the Bayesian update "prior $\times$ likelihood $\to$ posterior" is exactly this formula with a probability distribution over the unknown parameter in place of the discrete events $A_i$.

## Part B · Random variables

<a id="s4"></a>
### Random variables & distribution functions (CDF, PMF, PDF)

*A random variable is a number read off the outcome. Its distribution is fully captured by one function: the CDF.*

> **Concept — a random variable is a function**
>
> A **random variable** $X$ is a (measurable) function $X:\Omega\to\mathbb R$ that assigns a number to each outcome. "$\mathbb R$" is the set of all real numbers (the number line). "Measurable" is a technical condition (§s18) ensuring the events we ask about are genuine events; for everything here it is automatically satisfied. A random variable does not "have" a value until the experiment is run; what it has is a *distribution* — the way probability is spread across its possible values. Example: roll two dice and let $X$ be their sum; then $X$ maps the outcome $(3,4)$ to the number $7$.

A random variable is **discrete** if it takes values in a list of separated points (like $0,1,2,\dots$) and **continuous** if it can take any value in an interval (like any real number between $0$ and $1$).

**The cumulative distribution function (CDF)**

$$F_X(x)=P(X\le x)$$

In words, $F_X(x)$ is the probability that the random variable $X$ comes out at most $x$. As $x$ sweeps from left to right, $F_X$ accumulates probability — hence "cumulative."

*Every CDF is non-decreasing* (bigger $x$ can only include more outcomes, so probability cannot drop — this is monotonicity from §s1), *right-continuous, with $F(-\infty)=0$ and $F(+\infty)=1$* (no probability sits below $-\infty$; all of it lies below $+\infty$). *The CDF exists for every random variable, discrete or continuous, and determines the distribution completely.*

**PMF (discrete) and PDF (continuous)**

$$\text{discrete: }\ p_X(x)=P(X=x),\qquad \sum_x p_X(x)=1$$

The **probability mass function (PMF)** $p_X(x)$ gives the probability that $X$ equals exactly $x$. The masses over all possible values sum to $1$ (some value must occur — axiom (2), §s1).

$$\text{continuous: }\ f_X(x)=F_X'(x),\qquad P(a\le X\le b)=\int_a^b f_X(x)\,dx,\qquad \int_{-\infty}^{\infty}f_X=1$$

The **probability density function (PDF)** $f_X$ is the derivative (slope) of the CDF. The symbol $\int_a^b f_X(x)\,dx$ is the *integral* — the area under the curve $f_X$ between $a$ and $b$ — and that area equals the probability of landing in $[a,b]$.

*For a continuous variable, $P(X=x)=0$ for every single point: probability is **area**, not height.* The area over a single point has zero width, hence zero area. *The density $f$ can exceed 1; only its integral is constrained* (a tall, narrow spike can have height above $1$ yet total area $1$).

**Demonstration — recovering probabilities from the CDF**

1. **Split an event into disjoint pieces.** For any $a\lt b$, the event $\{X\le b\}$ is the disjoint union of $\{X\le a\}$ and $\{a\lt X\le b\}$ (a value at most $b$ is either at most $a$, or strictly between $a$ and $b$).
2. **Apply additivity.** By axiom (3) (§s1), $P(X\le b)=P(X\le a)+P(a\lt X\le b)$, i.e. $F(b)=F(a)+P(a\lt X\le b)$. Rearrange:

   $$P(a\lt X\le b)=F(b)-F(a).$$
3. **Point mass as a jump.** Letting $a$ approach $b$ from below, the probability concentrated exactly at $b$ is the size of the jump in $F$ there, written $F(x)-F(x^-)$ where $F(x^-)$ is the value just to the left:

   $$P(X=x)=F(x)-F(x^-).$$

   For continuous $F$ there are no jumps, so every single point has probability zero, consistent with the boxed statement above.

*The CDF is the universal currency: differentiate it for a density, difference it for a mass function.*

**Worked example — a continuous CDF.** Let $X$ be Uniform on $[0,1]$, meaning equally likely to land anywhere in that interval, with $f_X(x)=1$ for $0\le x\le1$ and $0$ elsewhere. Then $F_X(x)=\int_0^x 1\,dt=x$ for $0\le x\le1$. The probability $P(0.2\le X\le0.5)=F(0.5)-F(0.2)=0.5-0.2=0.3$ — exactly the width of the sub-interval, as uniformity demands. And $P(X=0.4)=0$ because $F$ has no jump there.

> **Connection — this is where calculus enters**
>
> For continuous variables the density plays the role of an ordinary function and probability is the integral under it. Expectations, percentiles, p-values, and the Normal curve are all areas — the integral calculus you already know, applied to $f_X$.

<a id="s5"></a>
### Expectation, variance & moments

*Expectation is the center of mass of a distribution; variance is its moment of inertia; higher moments fill in the shape.*

#### What expectation means

The **expectation** (or *expected value*, or *mean*) of $X$ is the long-run average value you would get by repeating the experiment many times. It is a weighted average of the possible values, each weighted by how likely it is.

**Expectation & the law of the unconscious statistician**

$$E[X]=\sum_x x\,p_X(x)\quad\text{(discrete)},\qquad E[X]=\int_{-\infty}^{\infty} x\,f_X(x)\,dx\quad\text{(continuous)}$$

For a discrete variable, multiply each value $x$ by its probability $p_X(x)$ and add; for a continuous one, replace the sum by an integral and the mass by the density.

$$E[g(X)]=\sum_x g(x)\,p_X(x)\quad\text{or}\quad \int g(x)\,f_X(x)\,dx$$

*LOTUS* (the "law of the unconscious statistician")*: to average $g(X)$ you need not find the distribution of $g(X)$ — just integrate $g$ against the density of $X$.* Here $g$ is any function, e.g. $g(X)=X^2$.

**Worked example — expectation of one die.** $E[X]=\sum_{x=1}^6 x\cdot\tfrac16=\tfrac{1+2+3+4+5+6}{6}=\tfrac{21}{6}=3.5$. The average roll is $3.5$, even though no single face shows $3.5$ — the mean need not be an attainable value.

**Variance, moments & linearity**

The **variance** measures how far, on average, $X$ falls from its mean $\mu=E[X]$; it is the average *squared* deviation. We square so that overshoots and undershoots do not cancel.

$$\mathrm{Var}(X)=E\big[(X-\mu)^2\big]=E[X^2]-\big(E[X]\big)^2$$

The square root of the variance is the **standard deviation** $\sigma$, in the same units as $X$.

$$E[aX+b]=aE[X]+b,\qquad \mathrm{Var}(aX+b)=a^2\mathrm{Var}(X)$$

These say expectation is **linear** (scaling by $a$ and shifting by $b$ pass straight through), while variance ignores the shift $b$ (shifting moves the whole distribution without changing its spread) and scales by $a^2$ (squaring because variance is a squared quantity).

$$\mu_k=E\big[(X-\mu)^k\big]:\quad \text{skewness}=\tfrac{\mu_3}{\sigma^3},\quad \text{kurtosis}=\tfrac{\mu_4}{\sigma^4}$$

The **$k$-th central moment** $\mu_k$ averages the $k$-th power of the deviation. The third moment (rescaled) measures **skewness** (lopsidedness); the fourth measures **kurtosis** (how heavy the tails are).

*Expectation is linear unconditionally; variance scales by the square and is shift-invariant.*

**Demonstration — linearity of expectation.**

1. By LOTUS with $g(x)=ax+b$: $E[aX+b]=\int(ax+b)f_X(x)\,dx$ (continuous case; the discrete sum is identical).
2. Split the integral and pull out constants: $=a\int x f_X(x)\,dx + b\int f_X(x)\,dx$.
3. The first integral is $E[X]$ by definition; the second is $\int f_X = 1$ (§s4). Hence $E[aX+b]=aE[X]+b$.

**Demonstration — the computational variance formula**

1. **Expand the square** in the definition, using $\mu=E[X]$ (a constant):

   $$\mathrm{Var}(X)=E\big[(X-\mu)^2\big]=E\big[X^2-2\mu X+\mu^2\big].$$
2. **Use linearity** (just proved) and the fact that $E[X]=\mu$:

   $$=E[X^2]-2\mu\,E[X]+\mu^2=E[X^2]-2\mu^2+\mu^2.$$
3. **Collect terms:**

   $$\mathrm{Var}(X)=E[X^2]-\mu^2=E[X^2]-(E[X])^2.$$

*"Mean of the square minus the square of the mean" — the everyday variance formula.*

**Worked example — variance of one die.** We have $\mu=3.5$. The mean square is $E[X^2]=\tfrac{1^2+2^2+3^2+4^2+5^2+6^2}{6}=\tfrac{91}{6}\approx15.167$. So $\mathrm{Var}(X)=15.167-3.5^2=15.167-12.25=2.917$, and the standard deviation is $\sqrt{2.917}\approx1.708$.

**Demonstration — variance scales by $a^2$.**

1. Let $Y=aX+b$. Its mean is $E[Y]=a\mu+b$ (linearity).
2. The deviation is $Y-E[Y]=(aX+b)-(a\mu+b)=a(X-\mu)$ — the shift $b$ cancels.
3. Square and take expectation: $\mathrm{Var}(Y)=E[a^2(X-\mu)^2]=a^2E[(X-\mu)^2]=a^2\mathrm{Var}(X)$, using linearity to pull out the constant $a^2$.

**Demonstration — $E[X]$ for a non-negative variable via its tail**

1. **Write the value as an integral of indicators.** For $X\ge0$ continuous, $x=\int_0^x dt=\int_0^\infty \mathbf 1\{t\lt x\}\,dt$, where the **indicator** $\mathbf 1\{t<x\}$ equals $1$ when $t<x$ and $0$ otherwise (so the integral just measures the length from $0$ to $x$).
2. **Take expectations and swap order** (justified by Tonelli's theorem, §s18, since everything is non-negative):

   $$E[X]=\int_0^\infty E[\mathbf 1\{t\lt X\}]\,dt=\int_0^\infty P(X\gt t)\,dt.$$

   The middle step uses $E[\mathbf 1\{t<X\}]=P(X>t)$: the expectation of an indicator is the probability of the event it indicates.

*The expectation equals the area above the CDF — a tail-sum formula reused throughout the limit theorems.*

<a id="s6"></a>
### Moment generating & characteristic functions

*Encode all moments in a single function. Transforms turn convolutions into products and make the CLT a one-line limit.*

#### Why a "transform"?

A *transform* repackages a whole distribution into one function of a helper variable $t$. The point is that hard operations on distributions (like adding independent variables) become easy operations on transforms (like multiplying).

**MGF and characteristic function**

$$M_X(t)=E\big[e^{tX}\big],\qquad \varphi_X(t)=E\big[e^{itX}\big]$$

The **moment generating function (MGF)** $M_X(t)$ is the expected value of $e^{tX}$, where $e$ is the base of natural exponentials ($\approx2.718$). The **characteristic function (CF)** $\varphi_X(t)$ uses $i$, the imaginary unit with $i^2=-1$; this version always exists (explained below).

$$M_X^{(k)}(0)=E[X^k],\qquad M_X(t)=\sum_{k=0}^{\infty}\frac{E[X^k]}{k!}\,t^k$$

The superscript $(k)$ means "differentiated $k$ times." So the $k$-th derivative of the MGF, evaluated at $t=0$, returns the $k$-th moment $E[X^k]$.

*The MGF "generates" moments by differentiation at 0. The characteristic function $\varphi$ always exists (since $|e^{itX}|=1$, the quantity inside the average never blows up) and uniquely determines the distribution.*

**Demonstration — why $M^{(k)}(0)=E[X^k]$**

1. **Expand the exponential** using the series $e^u=\sum_{k=0}^\infty \tfrac{u^k}{k!}$ with $u=tX$, then move the expectation inside the sum (allowed when the series converges):

   $$M_X(t)=E\Big[\sum_{k=0}^\infty \frac{(tX)^k}{k!}\Big]=\sum_{k=0}^\infty \frac{t^k}{k!}E[X^k].$$
2. **Recognize a Taylor series.** This is a power series in $t$ whose coefficient of $t^k$ is $E[X^k]/k!$.
3. **Differentiate $k$ times and set $t=0$.** Differentiating a power series $k$ times and evaluating at $0$ isolates exactly that coefficient times $k!$, i.e. it returns $E[X^k]$:

   $$M_X^{(k)}(0)=E[X^k].$$

*Differentiation replaces integration — the practical reason MGFs are so convenient.*

**Demonstration — computing the exponential MGF and its moments**

1. **Set up the integral.** For $X\sim\text{Exp}(\lambda)$ (the exponential distribution, §s8) the density is $f(x)=\lambda e^{-\lambda x}$ for $x\ge0$. So

   $$M_X(t)=\int_0^\infty e^{tx}\lambda e^{-\lambda x}\,dx=\lambda\int_0^\infty e^{-(\lambda-t)x}\,dx=\frac{\lambda}{\lambda-t},\ \ t\lt\lambda.$$

   The integral $\int_0^\infty e^{-cx}dx=1/c$ for $c>0$; here $c=\lambda-t$, requiring $t<\lambda$ so the exponent stays negative and the area is finite.
2. **First derivative gives the mean.** $M'(t)=\dfrac{\lambda}{(\lambda-t)^2}$, so $E[X]=M'(0)=\lambda/\lambda^2=1/\lambda$.
3. **Second derivative gives the second moment.** $M''(t)=\dfrac{2\lambda}{(\lambda-t)^3}$, so $E[X^2]=M''(0)=2\lambda/\lambda^3=2/\lambda^2$, and by the variance formula (§s5):

   $$\mathrm{Var}(X)=\frac{2}{\lambda^2}-\frac1{\lambda^2}=\frac1{\lambda^2}.$$

**Worked example — numbers.** If $\lambda=2$ then $E[X]=1/2=0.5$ and $\mathrm{Var}(X)=1/4=0.25$, with standard deviation $0.5$. (For the exponential, mean and standard deviation always coincide.)

**The key property: MGF of a sum**

$$X\perp Y\ \Rightarrow\ M_{X+Y}(t)=M_X(t)\,M_Y(t)$$

**Demonstration.** $M_{X+Y}(t)=E[e^{t(X+Y)}]=E[e^{tX}e^{tY}]$. Because $X$ and $Y$ are independent (§s3), the expectation of the product factors into the product of expectations: $=E[e^{tX}]\,E[e^{tY}]=M_X(t)M_Y(t)$.

*Sums of independent variables $\leftrightarrow$ products of transforms — the basis of convolution and of the CLT proof.*

> **Connection — calculus: Taylor series & transforms**
>
> The MGF is just the exponential generating function of the moment sequence; reading off moments is reading Taylor coefficients. The characteristic function is the Fourier transform of the density — which is why inverting it recovers the distribution.

<a id="s7"></a>
### Common discrete distributions

*A handful of named laws model most counting situations. Know each one's story, mean, variance, and MGF.*

Each row below is a named recipe for assigning probabilities to whole numbers. The PMF column gives $p(k)=P(X=k)$.

| Distribution | PMF $p(k)$ | Mean | Variance | MGF $M(t)$ |
| --- | --- | --- | --- | --- |
| Bernoulli($p$) | $p^k(1-p)^{1-k},\ k\in\{0,1\}$ | $p$ | $p(1-p)$ | $1-p+pe^{t}$ |
| Binomial($n,p$) | $\binom nk p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ | $(1-p+pe^{t})^n$ |
| Geometric($p$) | $(1-p)^{k-1}p,\ k\ge1$ | $1/p$ | $(1-p)/p^2$ | $\dfrac{pe^{t}}{1-(1-p)e^{t}}$ |
| Neg. Binomial($r,p$) | $\binom{k-1}{r-1}p^r(1-p)^{k-r}$ | $r/p$ | $r(1-p)/p^2$ | $\big(\tfrac{pe^{t}}{1-(1-p)e^{t}}\big)^r$ |
| Poisson($\lambda$) | $e^{-\lambda}\lambda^k/k!$ | $\lambda$ | $\lambda$ | $e^{\lambda(e^{t}-1)}$ |

**The stories.** A **Bernoulli($p$)** is a single yes/no trial succeeding with probability $p$ (it outputs $1$ for success, $0$ for failure). A **Binomial($n,p$)** counts successes in $n$ independent Bernoulli trials. A **Geometric($p$)** counts trials up to and including the first success. A **Negative Binomial($r,p$)** counts trials up to the $r$-th success. A **Poisson($\lambda$)** counts rare events in a fixed interval with average rate $\lambda$.

**Demonstration — building the Binomial from Bernoulli (mean & variance)**

1. **Decompose.** Write $X=X_1+\cdots+X_n$ as a sum of independent, identically distributed ("i.i.d.") Bernoulli($p$) indicators, each scoring $1$ for a success. Each has $E[X_i]=p$ (since $E[X_i]=1\cdot p+0\cdot(1-p)=p$) and $\mathrm{Var}(X_i)=p(1-p)$ (since $E[X_i^2]=p$ as $X_i^2=X_i$, so variance $=p-p^2=p(1-p)$).
2. **Sum the means** using linearity of expectation (§s5; no independence needed):

   $$E[X]=\sum_{i=1}^n E[X_i]=np.$$
3. **Sum the variances.** For *independent* variables, variances add (proved in §s11):

   $$\mathrm{Var}(X)=\sum_{i=1}^n \mathrm{Var}(X_i)=np(1-p).$$
4. **Multiply the MGFs.** Each Bernoulli has $M_{X_i}(t)=E[e^{tX_i}]=(1-p)e^{0}+pe^{t}=1-p+pe^t$; since the $X_i$ are independent, MGFs multiply (§s6), so $M_X(t)=(1-p+pe^t)^n$, confirming the table.

*Decompose into simple pieces, then sum — the recurring move of probability.*

**Worked example — Binomial numbers.** For $n=10$, $p=0.3$: mean $=np=3$, variance $=np(1-p)=10\cdot0.3\cdot0.7=2.1$. The chance of exactly $2$ successes is $\binom{10}{2}(0.3)^2(0.7)^8=45\cdot0.09\cdot0.05765\approx0.2335$.

**Demonstration — mean and variance of the Poisson**

1. **Mean directly from the PMF.** Pull out one factor of $\lambda$ and shift the index ($j=k-1$):

   $$E[X]=\sum_{k=0}^\infty k\,\frac{e^{-\lambda}\lambda^k}{k!}=\lambda e^{-\lambda}\sum_{k=1}^\infty\frac{\lambda^{k-1}}{(k-1)!}=\lambda e^{-\lambda}\sum_{j=0}^\infty\frac{\lambda^{j}}{j!}=\lambda e^{-\lambda}e^{\lambda}=\lambda.$$

   The last sum is the exponential series $\sum_j \lambda^j/j!=e^\lambda$.
2. **Confirm via the MGF.** With $M(t)=e^{\lambda(e^t-1)}$, the chain rule gives $M'(t)=\lambda e^t M(t)$, so $E[X]=M'(0)=\lambda\cdot1\cdot1=\lambda$.
3. **Second moment and variance.** Differentiate again: $M''(t)=\lambda e^t M(t)+(\lambda e^t)^2 M(t)$, so $M''(0)=\lambda+\lambda^2=E[X^2]$, hence

   $$\mathrm{Var}(X)=\lambda+\lambda^2-\lambda^2=\lambda.$$

*The Poisson's signature: its mean and variance coincide.*

**Demonstration — mean of the Geometric and its memorylessness**

1. **Mean via a summation identity.** With $q=1-p$,

   $$E[X]=\sum_{k\ge1}k\,q^{k-1}p=p\sum_{k\ge1}kq^{k-1}=p\cdot\frac{1}{(1-q)^2}=\frac{p}{p^2}=\frac1p,$$

   using the standard identity $\sum_{k\ge1}kq^{k-1}=(1-q)^{-2}$ for $|q|<1$ (it is the derivative of the geometric series $\sum_{k\ge0}q^k=(1-q)^{-1}$).
2. **Memorylessness.** Using $P(X>m)=q^m$ (no success in the first $m$ trials) and the definition of conditioning (§s3),

   $$P(X\gt m+n\mid X\gt m)=\frac{P(X>m+n)}{P(X>m)}=\frac{q^{m+n}}{q^{m}}=q^{n}=P(X\gt n).$$

   The past $m$ failures are "forgotten": the future looks like a fresh start.

*The geometric is the unique discrete memoryless law — the exponential's discrete twin.*

> **Connection — the Poisson as a binomial limit**
>
> Let $n\to\infty$ and $p\to0$ with $np\to\lambda$. Then the binomial MGF behaves as $(1-p+pe^t)^n=(1+\tfrac{\lambda}{n}(e^t-1))^n\to e^{\lambda(e^t-1)}$, the Poisson MGF, using the limit $(1+x/n)^n\to e^x$. So the Poisson is the law of rare events — many trials, tiny success probability.

<a id="s8"></a>
### Common continuous distributions

*The continuous catalog: each is a density, an integral, and a transform. The Normal sits at the center of it all.*

Each row gives a density $f(x)$; probabilities are areas under it (§s4).

| Distribution | PDF $f(x)$ | Mean | Variance | MGF $M(t)$ |
| --- | --- | --- | --- | --- |
| Uniform($a,b$) | $\dfrac{1}{b-a}$ on $[a,b]$ | $\dfrac{a+b}{2}$ | $\dfrac{(b-a)^2}{12}$ | $\dfrac{e^{tb}-e^{ta}}{t(b-a)}$ |
| Exponential($\lambda$) | $\lambda e^{-\lambda x},\ x\ge0$ | $1/\lambda$ | $1/\lambda^2$ | $\dfrac{\lambda}{\lambda-t},\ t\lt\lambda$ |
| Gamma($\alpha,\lambda$) | $\dfrac{\lambda^\alpha x^{\alpha-1}e^{-\lambda x}}{\Gamma(\alpha)},\ x\ge0$ | $\alpha/\lambda$ | $\alpha/\lambda^2$ | $\big(\tfrac{\lambda}{\lambda-t}\big)^\alpha$ |
| Normal($\mu,\sigma^2$) | $\dfrac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/2\sigma^2}$ | $\mu$ | $\sigma^2$ | $e^{\mu t+\sigma^2 t^2/2}$ |
| Beta($\alpha,\beta$) | $\dfrac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)},\ x\in[0,1]$ | $\dfrac{\alpha}{\alpha+\beta}$ | $\dfrac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$ | — |

Here $\Gamma(\alpha)$ is the **Gamma function**, a continuous extension of the factorial with $\Gamma(n)=(n-1)!$ for whole numbers, and $B(\alpha,\beta)=\Gamma(\alpha)\Gamma(\beta)/\Gamma(\alpha+\beta)$ is the **Beta function**, a normalizing constant making the Beta density integrate to $1$.

**Demonstration — mean and variance of the Uniform$(a,b)$**

1. **Mean.** Using $\int_a^b x\,dx=\tfrac{b^2-a^2}{2}$ and factoring $b^2-a^2=(b-a)(b+a)$:

   $$E[X]=\int_a^b \frac{x}{b-a}\,dx=\frac{1}{b-a}\cdot\frac{b^2-a^2}{2}=\frac{a+b}{2}.$$
2. **Second moment.** Using $\int_a^b x^2\,dx=\tfrac{b^3-a^3}{3}$ and factoring $b^3-a^3=(b-a)(a^2+ab+b^2)$:

   $$E[X^2]=\int_a^b\frac{x^2}{b-a}\,dx=\frac{b^3-a^3}{3(b-a)}=\frac{a^2+ab+b^2}{3}.$$
3. **Subtract the squared mean** (§s5) and simplify the algebra over a common denominator $12$:

   $$\mathrm{Var}(X)=\frac{a^2+ab+b^2}{3}-\frac{(a+b)^2}{4}=\frac{4(a^2+ab+b^2)-3(a+b)^2}{12}=\frac{(b-a)^2}{12}.$$

*Spread depends only on the width $b-a$, as symmetry demands.*

**Worked example — Uniform numbers.** On $[0,10]$: mean $=(0+10)/2=5$, variance $=(10-0)^2/12=100/12\approx8.33$, standard deviation $\approx2.89$.

**Demonstration — mean and variance of the Exponential by integration**

1. **Mean by parts.** Integration by parts with $u=x$, $dv=\lambda e^{-\lambda x}dx$:

   $$E[X]=\int_0^\infty x\,\lambda e^{-\lambda x}\,dx=\Big[-xe^{-\lambda x}\Big]_0^\infty+\int_0^\infty e^{-\lambda x}\,dx=0+\frac1\lambda=\frac1\lambda.$$

   The boundary term vanishes because $xe^{-\lambda x}\to0$ as $x\to\infty$ and is $0$ at $x=0$.
2. **Second moment** similarly (or by parts twice): $E[X^2]=\int_0^\infty x^2\lambda e^{-\lambda x}\,dx=\dfrac{2}{\lambda^2}$.
3. **Variance** (§s5): $\mathrm{Var}(X)=\dfrac{2}{\lambda^2}-\dfrac{1}{\lambda^2}=\dfrac{1}{\lambda^2}$, matching the MGF result of §s6.

*The exponential is memoryless: $P(X\gt s+t\mid X\gt s)=e^{-\lambda t}=P(X\gt t)$* (same algebra as the geometric in §s7, with $P(X>x)=e^{-\lambda x}$).

**Demonstration — the Normal MGF gives mean $\mu$ and variance $\sigma^2$**

1. **Standard Normal MGF by completing the square.** For $Z\sim N(0,1)$ (density $\tfrac{1}{\sqrt{2\pi}}e^{-z^2/2}$), combine the exponents $tz-\tfrac{z^2}{2}=-\tfrac12(z-t)^2+\tfrac{t^2}{2}$:

   $$M_Z(t)=\frac{1}{\sqrt{2\pi}}\int e^{tz-z^2/2}\,dz=e^{t^2/2}\cdot\frac{1}{\sqrt{2\pi}}\int e^{-(z-t)^2/2}\,dz=e^{t^2/2}.$$

   The remaining integral is the total area under a (shifted) standard Normal density, which equals $1$ (§s4).
2. **General Normal by shifting and scaling.** Any $X\sim N(\mu,\sigma^2)$ can be written $X=\mu+\sigma Z$. Then $M_X(t)=E[e^{t(\mu+\sigma Z)}]=e^{\mu t}E[e^{(\sigma t)Z}]=e^{\mu t}M_Z(\sigma t)=e^{\mu t+\sigma^2 t^2/2}$.
3. **Differentiate at $0$** (§s6): $M_X'(0)=\mu$ gives $E[X]=\mu$, and $M_X''(0)=\mu^2+\sigma^2$ gives $E[X^2]=\mu^2+\sigma^2$, so $\mathrm{Var}(X)=\sigma^2$.

*The two parameters $\mu,\sigma^2$ are literally the mean and variance — and the standardizing $Z=(X-\mu)/\sigma$ is the z-score of the Statistics guide.*

**Worked example — Normal standardizing.** If heights are $N(170, 10^2)$ (mean $170$ cm, standard deviation $10$ cm), a height of $185$ cm has z-score $(185-170)/10=1.5$ — it lies $1.5$ standard deviations above the mean. Using a Normal table, $P(X\le185)=P(Z\le1.5)\approx0.933$.

> **Connection — one family, many faces**
>
> Exponential = Gamma($1,\lambda$); a sum of $n$ i.i.d. exponentials is Gamma($n,\lambda$) (§s13); the chi-square with $k$ degrees of freedom is Gamma($k/2,1/2$). The Beta governs proportions and is the conjugate prior to the binomial — the bridge to Bayesian inference.

<a id="s9"></a>
### Functions & transformations of random variables

*If you know the law of $X$, what is the law of $Y=g(X)$? Two reliable methods: the CDF method and the Jacobian.*

When we apply a function $g$ to a random variable $X$, the result $Y=g(X)$ is a new random variable, and we want its distribution.

**The change-of-variables formula**

$$\text{CDF method: }\ F_Y(y)=P(g(X)\le y),\quad\text{then }f_Y=F_Y'$$

The **CDF method**: find the cumulative distribution of $Y$ directly from the event $\{g(X)\le y\}$, then differentiate (§s4) to get the density.

$$\text{Jacobian (monotone }g): \ f_Y(y)=f_X\big(g^{-1}(y)\big)\,\Big|\frac{d}{dy}g^{-1}(y)\Big|$$

The **Jacobian formula** is a shortcut when $g$ is strictly increasing or decreasing (so it has an inverse $g^{-1}$). The factor $\big|\tfrac{d}{dy}g^{-1}(y)\big|$ (absolute value of the derivative of the inverse) accounts for how $g$ stretches or compresses the axis.

*The CDF method always works; the Jacobian formula is its shortcut when $g$ is smooth and one-to-one. For many-to-one $g$, sum over all preimages.*

**Demonstration — the probability integral transform**

1. **Apply the CDF method.** Let $X$ have continuous, strictly increasing CDF $F$, and set $U=F(X)$. Because $F$ is increasing it has an inverse $F^{-1}$, so for $u\in(0,1)$:

   $$F_U(u)=P(F(X)\le u)=P\big(X\le F^{-1}(u)\big)=F\big(F^{-1}(u)\big)=u.$$

   The middle step applies $F^{-1}$ to both sides inside the probability (allowed since $F$ is increasing); the last step uses $F(F^{-1}(u))=u$.
2. **Identify the result.** A random variable with CDF $F_U(u)=u$ on $(0,1)$ is exactly Uniform$(0,1)$ (its CDF, §s4). Conversely, $X=F^{-1}(U)$ then has CDF $F$.

*This is how computers simulate any distribution: feed a uniform random number through $F^{-1}$.*

**Worked example.** To simulate an Exponential($\lambda$), whose CDF is $F(x)=1-e^{-\lambda x}$, invert: setting $u=1-e^{-\lambda x}$ and solving gives $x=-\tfrac1\lambda\ln(1-u)$. Drawing $U=0.5$ with $\lambda=1$ yields $x=-\ln(0.5)\approx0.693$.

**Demonstration — the square of a standard Normal is chi-square (Jacobian, two branches)**

1. **Identify the preimages.** Let $Z\sim N(0,1)$ and $Y=Z^2$. For $y\gt0$, the map $g(z)=z^2$ is two-to-one: both $+\sqrt y$ and $-\sqrt y$ map to $y$.
2. **Use the CDF method** since $g$ is not one-to-one: $\{Z^2\le y\}=\{-\sqrt y\le Z\le\sqrt y\}$, so with $\Phi$ the standard Normal CDF, $F_Y(y)=\Phi(\sqrt y)-\Phi(-\sqrt y)=2\Phi(\sqrt y)-1$ (by the symmetry $\Phi(-z)=1-\Phi(z)$).
3. **Differentiate via the chain rule.** With $\varphi=\Phi'$ the standard Normal density, $\tfrac{d}{dy}\Phi(\sqrt y)=\varphi(\sqrt y)\cdot\tfrac{1}{2\sqrt y}$:

   $$f_Y(y)=2\varphi(\sqrt y)\cdot\frac{1}{2\sqrt y}=\frac{1}{\sqrt{2\pi y}}e^{-y/2},\quad y\gt0.$$

*This is the $\chi^2_1$ density = Gamma($\tfrac12,\tfrac12$) — the foundation of the chi-square tests in the Statistics guide.*

**Demonstration — a linear transform of a Normal stays Normal**

1. **Set up the inverse.** Let $X\sim N(\mu,\sigma^2)$, $Y=aX+b$ with $a\gt0$. Then $g^{-1}(y)=(y-b)/a$ and its derivative is $\big|\tfrac{d}{dy}g^{-1}\big|=1/a$.
2. **Substitute into the Jacobian formula** (valid since $g$ is increasing):

   $$f_Y(y)=\frac{1}{a}\cdot\frac{1}{\sigma\sqrt{2\pi}}\exp\!\Big(-\frac{((y-b)/a-\mu)^2}{2\sigma^2}\Big)=\frac{1}{(a\sigma)\sqrt{2\pi}}\exp\!\Big(-\frac{(y-(a\mu+b))^2}{2a^2\sigma^2}\Big).$$

   The algebra rewrites $((y-b)/a-\mu)^2/\sigma^2$ as $(y-(a\mu+b))^2/(a\sigma)^2$ by multiplying top and bottom inside by $a^2$.

*So $Y\sim N(a\mu+b,\,a^2\sigma^2)$: the Normal family is closed under affine maps — which is exactly why standardizing works.* (Setting $a=1/\sigma$, $b=-\mu/\sigma$ turns $X$ into $Z\sim N(0,1)$.)

## Part C · Multiple random variables

<a id="s10"></a>
### Joint, marginal & conditional distributions

*Two or more random variables live together in a joint law; marginals and conditionals are the views you take of it.*

When two measurements $X$ and $Y$ come from the same experiment, their *joint* distribution describes them together. A **marginal** distribution looks at one variable alone (ignoring the other); a **conditional** distribution fixes one variable and looks at the other.

**Joint, marginal & conditional densities**

$$\text{joint CDF: }\ F(x,y)=P(X\le x,\,Y\le y),\qquad f(x,y)=\frac{\partial^2 F}{\partial x\,\partial y}$$

The joint CDF is the probability that $X\le x$ *and* $Y\le y$ simultaneously; the joint density $f(x,y)$ is its mixed second derivative (the two-variable analogue of differentiating a CDF, §s4).

$$\text{marginal: }\ f_X(x)=\int f(x,y)\,dy,\qquad \text{conditional: }\ f_{Y\mid X}(y\mid x)=\frac{f(x,y)}{f_X(x)}$$

The **marginal** $f_X$ integrates the other variable away. The **conditional** $f_{Y\mid X}$ is the joint divided by the marginal — the continuous version of $P(A\mid B)=P(A\cap B)/P(B)$ from §s3.

$$X\perp Y \iff f(x,y)=f_X(x)\,f_Y(y)$$

*The marginal integrates out the other variable; the conditional renormalizes a slice. Independence means the joint factors into its marginals.*

**Demonstration — marginalizing a joint uniform on the unit triangle**

1. **Find the density.** Let $(X,Y)$ be uniform on the triangle $\{0\lt x\lt y\lt1\}$. Uniform means constant density equal to $1/\text{area}$; the triangle has area $\tfrac12$, so $f(x,y)=2$ inside it and $0$ outside.
2. **Marginal of $X$.** Hold $x$ fixed and integrate over the allowed $y$, which run from $x$ up to $1$:

   $$f_X(x)=\int_x^1 2\,dy=2(1-x),\quad 0\lt x\lt1.$$
3. **Conditional of $Y$ given $X=x$.** Divide the joint by this marginal:

   $$f_{Y\mid X}(y\mid x)=\frac{2}{2(1-x)}=\frac{1}{1-x},\quad x\lt y\lt1,$$

   which is a constant in $y$ — so $Y\mid X=x$ is uniform on the interval $(x,1)$, of length $1-x$, consistent with density $1/(1-x)$.

*Here $X$ and $Y$ are dependent: the joint $f(x,y)=2$ does not equal the product $f_X(x)f_Y(y)$, so by the boxed criterion they are not independent.*

> **Concept — expectation over a joint law**
>
> For any function $g$ of two variables, $E[g(X,Y)]=\iint g(x,y)\,f(x,y)\,dx\,dy$ (LOTUS for two variables, §s5). In particular $E[XY]$ is computed against the joint density — and it is exactly this quantity that measures how the variables move together (next section).

<a id="s11"></a>
### Covariance, correlation & independence

*Covariance measures co-movement; correlation rescales it to a unitless number in $[-1,1]$.*

**Covariance, correlation & variance of a sum**

$$\mathrm{Cov}(X,Y)=E[XY]-E[X]E[Y],\qquad \rho=\frac{\mathrm{Cov}(X,Y)}{\sigma_X\sigma_Y}$$

The **covariance** is positive when $X$ and $Y$ tend to be large together (and small together) and negative when one tends to be large while the other is small. The **correlation** $\rho$ (Greek "rho") divides covariance by the two standard deviations $\sigma_X,\sigma_Y$ to produce a pure number between $-1$ and $1$ with no units.

$$\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)+2\mathrm{Cov}(X,Y)$$

$$\mathrm{Cov}(aX+b,\,cY+d)=ac\,\mathrm{Cov}(X,Y)$$

The last line: covariance ignores the shifts $b,d$ and scales by the product $ac$ of the multipliers.

*$\rho\in[-1,1]$ is the average product of the two variables' z-scores. Independence $\Rightarrow$ $\mathrm{Cov}=0$, but not conversely.*

**Demonstration — variance of a sum, and why independent variances add.**

1. By the definition of variance and expanding $((X+Y)-(\mu_X+\mu_Y))^2=((X-\mu_X)+(Y-\mu_Y))^2$:

   $$\mathrm{Var}(X+Y)=E\big[(X-\mu_X)^2\big]+E\big[(Y-\mu_Y)^2\big]+2E\big[(X-\mu_X)(Y-\mu_Y)\big].$$
2. The first two terms are $\mathrm{Var}(X)$ and $\mathrm{Var}(Y)$; the cross term is $2\mathrm{Cov}(X,Y)$ by definition. Hence the boxed formula.
3. If $X\perp Y$ then $\mathrm{Cov}(X,Y)=0$ (next demonstration), so the cross term vanishes and $\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)$ — the rule used for the Binomial in §s7.

**Demonstration — independence implies zero covariance (and why not the reverse)**

1. **Factor the joint expectation.** If $X\perp Y$, the joint density factors (§s10), so

   $$E[XY]=\iint xy\,f_X(x)f_Y(y)\,dx\,dy=\Big(\int x f_X(x)dx\Big)\Big(\int y f_Y(y)dy\Big)=E[X]E[Y].$$
2. **Covariance is zero.** Then $\mathrm{Cov}(X,Y)=E[XY]-E[X]E[Y]=0$.
3. **The converse fails.** Let $X\sim N(0,1)$ and $Y=X^2$. By symmetry $E[X]=0$ and $E[X^3]=0$, so $E[XY]=E[X^3]=0=E[X]E[Y]$, giving $\mathrm{Cov}=0$. Yet $Y$ is completely determined by $X$ — they are as dependent as possible.

*Covariance sees only *linear* association; zero covariance is not independence.*

**Worked example — covariance of two dice and their sum.** Let $X,Y$ be independent fair dice. Then $\mathrm{Cov}(X,Y)=0$, so $\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)=2.917+2.917=5.833$ (using $\mathrm{Var}=2.917$ from §s5).

**Demonstration — $|\rho|\le1$ via Cauchy–Schwarz**

1. **State the tool.** The Cauchy–Schwarz inequality for random variables says $\big(E[UV]\big)^2\le E[U^2]\,E[V^2]$ for any $U,V$ (proved as an inequality in §s14).
2. **Apply to centered variables** $U=X-\mu_X$, $V=Y-\mu_Y$. Then $E[UV]=\mathrm{Cov}(X,Y)$, $E[U^2]=\mathrm{Var}(X)$, $E[V^2]=\mathrm{Var}(Y)$, so

   $$\mathrm{Cov}(X,Y)^2\le \mathrm{Var}(X)\,\mathrm{Var}(Y).$$
3. **Divide by $\sigma_X^2\sigma_Y^2$:**

   $$\rho^2\le1\ \Rightarrow\ -1\le\rho\le1,$$

   with equality exactly when $Y$ is an exact linear function of $X$ (the equality case of Cauchy–Schwarz).

*Correlation is bounded precisely because Cauchy–Schwarz bounds the inner product by the norms.*

> **Connection — to regression in the Statistics guide**
>
> The least-squares slope is $b_1=\rho\,\sigma_Y/\sigma_X$ and $R^2=\rho^2$. The correlation coefficient computed from data is the sample version of the $\rho$ defined here from a joint distribution.

<a id="s12"></a>
### Conditional expectation & the tower property

*Conditional expectation is the best prediction of one variable given another — and it averages back to the unconditional mean.*

**Conditional expectation & its laws**

$$E[X\mid Y=y]=\int x\,f_{X\mid Y}(x\mid y)\,dx,\qquad E[X\mid Y]=g(Y)\ \text{is a random variable}$$

$E[X\mid Y=y]$ is the average of $X$ *once we know* $Y=y$ — computed against the conditional density of §s10. As $y$ varies it traces out a function $g(y)$; plugging in the random $Y$ gives $E[X\mid Y]=g(Y)$, which is itself random because $Y$ is.

$$\text{tower: }\ E\big[E[X\mid Y]\big]=E[X]$$

$$\text{law of total variance: }\ \mathrm{Var}(X)=E\big[\mathrm{Var}(X\mid Y)\big]+\mathrm{Var}\big(E[X\mid Y]\big)$$

*$E[X\mid Y]$ is the function of $Y$ that best predicts $X$ in mean-square. It is itself random because $Y$ is.*

**Demonstration — the tower property $E[E[X\mid Y]]=E[X]$**

1. **Inner expectation.** By definition $E[X\mid Y=y]=\int x\,f_{X\mid Y}(x\mid y)\,dx$.
2. **Average over $Y$.** Multiply by $f_Y(y)$ and integrate over $y$:

   $$E\big[E[X\mid Y]\big]=\int\!\Big(\int x\,f_{X\mid Y}(x\mid y)\,dx\Big)f_Y(y)\,dy.$$
3. **Recombine the densities.** Since $f_{X\mid Y}(x\mid y)\,f_Y(y)=f(x,y)$ (the definition of conditional density rearranged, §s10), and swapping the integration order (Fubini, §s18):

   $$=\int x\Big(\int f(x,y)\,dy\Big)dx=\int x\,f_X(x)\,dx=E[X],$$

   where $\int f(x,y)\,dy=f_X(x)$ is the marginal (§s10).

*"Average the conditional averages, weighting by the conditioner" — and you recover the grand average.*

**Worked example — tower property.** A factory has two machines. Machine $1$ (chosen with probability $0.5$) makes parts averaging $10$ g; machine $2$ (probability $0.5$) averages $20$ g. Let $Y$ be the machine and $X$ the weight. Then $E[X\mid Y=1]=10$, $E[X\mid Y=2]=20$, and the tower property gives $E[X]=0.5\cdot10+0.5\cdot20=15$ g overall.

**Demonstration — total variance from the tower property**

1. **Define the conditional mean** $m(Y)=E[X\mid Y]$ and write the conditional variance $\mathrm{Var}(X\mid Y)=E[X^2\mid Y]-m(Y)^2$ (variance formula of §s5 applied inside the conditioning).
2. **Take expectations** and apply the tower property to $E[X^2\mid Y]$: $E[\mathrm{Var}(X\mid Y)]=E[X^2]-E[m(Y)^2]$.
3. **Add the variance of the conditional mean** $\mathrm{Var}(m(Y))=E[m(Y)^2]-(E[m(Y)])^2=E[m(Y)^2]-(E[X])^2$ (using $E[m(Y)]=E[X]$ by the tower property). The $E[m(Y)^2]$ terms cancel when added, leaving

   $$E[\mathrm{Var}(X\mid Y)]+\mathrm{Var}(E[X\mid Y])=E[X^2]-(E[X])^2=\mathrm{Var}(X).$$

*Variance splits into "within-group" plus "between-group" — exactly the decomposition behind ANOVA.*

> **Connection — martingales (§s18)**
>
> Conditional expectation given a $\sigma$-algebra is the abstract version of this idea, and a martingale is a process whose conditional expectation of the future, given the past, equals the present. The tower property is the engine of that whole theory.

<a id="s13"></a>
### Sums of random variables & convolutions

*The density of a sum of independent variables is the convolution of their densities — and transforms turn that convolution into a product.*

**The convolution formula**

$$Z=X+Y,\ X\perp Y:\quad f_Z(z)=\int_{-\infty}^{\infty} f_X(x)\,f_Y(z-x)\,dx$$

To get a total $z$, if $X=x$ then $Y$ must be $z-x$; multiplying their (independent) densities and summing over all splits $x$ gives the density of the sum. This operation is called **convolution**.

$$\text{discrete: }\ p_Z(z)=\sum_{x}p_X(x)\,p_Y(z-x),\qquad M_Z(t)=M_X(t)\,M_Y(t)$$

*Adding independent variables $\leftrightarrow$ convolving densities $\leftrightarrow$ multiplying transforms. The last is usually the easy route* (the MGF identity is from §s6).

**Demonstration — the sum of two independent Uniform$(0,1)$ is triangular**

1. **Set up the convolution.** With $f_X=f_Y=1$ on $[0,1]$ (and $0$ elsewhere), $f_Z(z)=\int_0^1 \mathbf 1\{0\le z-x\le1\}\,dx$ — the length of the set of $x$ for which both densities are nonzero.
2. **Case $0\le z\le1$.** The condition $0\le z-x\le1$ means $x\le z$ and $x\ge z-1$; combined with $0\le x\le1$ this gives $x\in[0,z]$, of length $z$. So $f_Z(z)=z$.
3. **Case $1\le z\le2$.** Now $x$ ranges over $[z-1,1]$, of length $1-(z-1)=2-z$. So $f_Z(z)=2-z$. Together:

   $$f_Z(z)=\begin{cases}z,&0\le z\le1\\ 2-z,&1\le z\le2\end{cases}$$

**Worked example — checking the area.** The triangle has base $2$ (from $0$ to $2$) and peak height $1$ (at $z=1$), so its area is $\tfrac12\cdot2\cdot1=1$ — confirming $f_Z$ is a valid density. The most likely sum is near $1$, the least likely near $0$ or $2$.

*The flat uniform convolves into a triangle — the first visible step toward the bell curve of the CLT.*

**Demonstration — the sum of $n$ i.i.d. Exponentials is Gamma (via MGFs)**

1. **Each term's MGF.** Each $X_i\sim\text{Exp}(\lambda)$ has $M_{X_i}(t)=\dfrac{\lambda}{\lambda-t}$ (§s6).
2. **Multiply for the sum.** For $S_n=X_1+\cdots+X_n$ of independent terms, MGFs multiply (§s6):

   $$M_{S_n}(t)=\Big(\frac{\lambda}{\lambda-t}\Big)^n.$$
3. **Match by uniqueness.** This is exactly the Gamma$(n,\lambda)$ MGF from the table in §s8. Since the MGF uniquely determines the distribution (§s6),

   $$S_n\sim\text{Gamma}(n,\lambda),\qquad f_{S_n}(s)=\frac{\lambda^n s^{n-1}e^{-\lambda s}}{(n-1)!}.$$

*Waiting times for $n$ Poisson arrivals add up to a Gamma — and the MGF made it a one-line proof.*

> **Connection — sums are the heart of the limit theorems**
>
> The sample mean $\bar X_n=\tfrac1n\sum X_i$ is a scaled sum. Understanding sums — their means, variances, and limiting shapes — is precisely the program of Part D.

## Part D · Limit theorems

<a id="s14"></a>
### Probability inequalities (Markov, Chebyshev, Jensen, Cauchy–Schwarz)

*Inequalities bound tail probabilities and expectations with almost no assumptions — the scaffolding of every convergence proof.*

An **inequality** here is a guaranteed bound — "this probability is no larger than that number" — that holds without knowing the full distribution.

**The four workhorse inequalities**

$$\text{Markov: }\ P(X\ge a)\le\frac{E[X]}{a}\quad(X\ge0,\ a\gt0)$$

$$\text{Chebyshev: }\ P\big(|X-\mu|\ge k\big)\le\frac{\sigma^2}{k^2}$$

$$\text{Jensen: }\ \varphi\text{ convex}\Rightarrow \varphi(E[X])\le E[\varphi(X)]$$

$$\text{Cauchy–Schwarz: }\ \big(E[XY]\big)^2\le E[X^2]\,E[Y^2]$$

Markov bounds the chance a non-negative variable is large by its mean over the threshold. Chebyshev bounds the chance of being far from the mean using the variance. Jensen relates the function of an average to the average of a function for **convex** $\varphi$ (one curving upward, like $x^2$). Cauchy–Schwarz bounds a product-average by the two squared-averages.

**Demonstration — Markov, then Chebyshev as a corollary**

1. **Markov via an indicator bound.** For $X\ge0$ and $a\gt0$, note $a\,\mathbf 1\{X\ge a\}\le X$ always: if $X\ge a$ the left side is $a\le X$; if $X<a$ the left side is $0\le X$. Take expectations of both sides (expectation preserves $\le$):

   $$a\,P(X\ge a)\le E[X]\ \Rightarrow\ P(X\ge a)\le\frac{E[X]}{a},$$

   using $E[\mathbf 1\{X\ge a\}]=P(X\ge a)$ (§s5).
2. **Chebyshev from Markov.** Apply Markov to the non-negative variable $(X-\mu)^2$ at level $k^2$:

   $$P\big((X-\mu)^2\ge k^2\big)\le\frac{E[(X-\mu)^2]}{k^2}=\frac{\sigma^2}{k^2}.$$
3. **Translate the event.** $(X-\mu)^2\ge k^2$ is the same as $|X-\mu|\ge k$ (taking square roots), giving Chebyshev's inequality.

*Chebyshev is just Markov applied to the squared deviation — the bound that powers the Weak Law.*

**Worked example — Chebyshev in action.** If $X$ has mean $\mu=50$ and standard deviation $\sigma=5$, the chance of being $15$ or more away ($k=15$) is at most $\sigma^2/k^2=25/225\approx0.111$. So at least about $89\%$ of the probability lies within $15$ of the mean — guaranteed, whatever the distribution.

**Demonstration — Jensen's inequality from a supporting line**

1. **Supporting line of a convex function.** A convex $\varphi$ lies on or above each of its tangent (supporting) lines. At the point $\mu=E[X]$ there is a slope $c$ with $\varphi(x)\ge\varphi(\mu)+c\,(x-\mu)$ for all $x$.
2. **Take expectations** of both sides (expectation preserves $\ge$ and is linear, §s5):

   $$E[\varphi(X)]\ge\varphi(\mu)+c\,(E[X]-\mu)=\varphi(\mu)+c\cdot0=\varphi(E[X]).$$

*Hence $E[X^2]\ge(E[X])^2$ (taking $\varphi(x)=x^2$, so variance $\ge0$) and $E[1/X]\ge1/E[X]$ for positive $X$ (taking $\varphi(x)=1/x$) — both special cases.*

(The Cauchy–Schwarz inequality used in §s11 follows from $E[(X-tY)^2]\ge0$ for all $t$: this is a quadratic in $t$ that is never negative, so its discriminant is $\le0$, which rearranges to $(E[XY])^2\le E[X^2]E[Y^2]$.)

<a id="s15"></a>
### Modes of convergence

*"A sequence of random variables converges" can mean several different things. The hierarchy among them organizes the limit theorems.*

A *sequence* $X_1,X_2,\dots$ of random variables can approach a limit $X$ in several distinct senses; we name four.

**Four modes of convergence**

$$\text{a.s.: }\ P\big(X_n\to X\big)=1$$

**Almost-sure (a.s.)** convergence: with probability $1$, the actual numbers $X_n$ settle to $X$ along the run.

$$\text{in prob.: }\ \forall\varepsilon\gt0,\ P\big(|X_n-X|\ge\varepsilon\big)\to0$$

**In probability:** for every tolerance $\varepsilon>0$ (read "$\forall\varepsilon>0$" as "for all positive $\varepsilon$"), the chance of being off by $\varepsilon$ or more shrinks to $0$.

$$\text{in }L^p:\ E\big[|X_n-X|^p\big]\to0$$

**In $L^p$:** the average $p$-th power of the error goes to $0$ (for $p=2$ this is mean-squared error).

$$\text{in distribution: }\ F_{X_n}(x)\to F_X(x)\ \text{at continuity points of }F_X$$

**In distribution:** the CDFs converge (only the *laws* match in the limit, not the variables themselves).

> **Principle — the hierarchy**
>
> Almost-sure and $L^p$ convergence each imply convergence **in probability**, which in turn implies convergence **in distribution**. The reverse arrows fail in general. Convergence in distribution is the weakest — it concerns only the laws, not the variables themselves — and it is the mode of the CLT.

**Demonstration — $L^2$ convergence implies convergence in probability**

1. **Apply Markov to the squared error.** Suppose $E[(X_n-X)^2]\to0$. The variable $(X_n-X)^2$ is non-negative, so Markov (§s14) at level $\varepsilon^2$ gives

   $$P\big(|X_n-X|\ge\varepsilon\big)=P\big((X_n-X)^2\ge\varepsilon^2\big)\le\frac{E[(X_n-X)^2]}{\varepsilon^2}.$$
2. **Take the limit.** The right side $\to0$ for every fixed $\varepsilon\gt0$ (numerator $\to0$, denominator fixed), which is exactly convergence in probability.

*This Markov-based step is exactly how the Weak Law is proved in the next section.*

**Continuity theorem (the CLT tool)**

$$\varphi_{X_n}(t)\to\varphi_X(t)\ \forall t\ \iff\ X_n\xrightarrow{d}X$$

*Lévy's continuity theorem: convergence of characteristic functions (or MGFs where they exist) is equivalent to convergence in distribution (the arrow $\xrightarrow{d}$). This is the lever that proves the CLT.*

<a id="s16"></a>
### The Laws of Large Numbers

*Averages of many independent trials converge to the true mean. This is the theorem that justifies the frequentist interpretation of probability.*

The **sample mean** $\bar X_n=\tfrac1n(X_1+\cdots+X_n)$ is the average of the first $n$ observations. The laws of large numbers say it approaches the true mean $\mu$ as $n$ grows.

**Weak and Strong laws**

$$\text{WLLN: }\ \bar X_n\xrightarrow{P}\mu\quad\text{(convergence in probability)}$$

$$\text{SLLN: }\ \bar X_n\xrightarrow{a.s.}\mu\quad\text{(almost-sure convergence)}$$

*Both require i.i.d. $X_i$ ("independent, identically distributed") with finite mean $\mu$ (the WLLN here also uses finite variance). The strong law is the deeper statement* (a.s. convergence, the stronger mode of §s15).

**Demonstration — the Weak Law via Chebyshev**

1. **Mean of the average.** Let $X_1,\dots,X_n$ be i.i.d. with mean $\mu$, variance $\sigma^2$. By linearity (§s5), $E[\bar X_n]=\tfrac1n\sum E[X_i]=\tfrac1n(n\mu)=\mu$.
2. **Variance of the average shrinks.** Since the $X_i$ are independent their variances add (§s11), and $\mathrm{Var}(cX)=c^2\mathrm{Var}(X)$ with $c=1/n$:

   $$\mathrm{Var}(\bar X_n)=\frac{1}{n^2}\sum_{i=1}^n\mathrm{Var}(X_i)=\frac{n\sigma^2}{n^2}=\frac{\sigma^2}{n}.$$
3. **Apply Chebyshev** (§s14) to $\bar X_n$, whose mean is $\mu$:

   $$P\big(|\bar X_n-\mu|\ge\varepsilon\big)\le\frac{\mathrm{Var}(\bar X_n)}{\varepsilon^2}=\frac{\sigma^2}{n\varepsilon^2}\xrightarrow[n\to\infty]{}0.$$

   The bound goes to $0$, which is convergence in probability — the Weak Law.

**Worked example — coin flips.** Flip a fair coin ($p=0.5$, so $\sigma^2=p(1-p)=0.25$). After $n=10{,}000$ flips, Chebyshev bounds the chance the observed proportion is off by $\varepsilon=0.02$ or more: $\sigma^2/(n\varepsilon^2)=0.25/(10000\cdot0.0004)=0.0625$. So with at least $93.75\%$ assurance the proportion lands within $0.02$ of $0.5$.

> **Connection — why the standard error has a $\sqrt n$**
>
> The same computation $\mathrm{Var}(\bar X_n)=\sigma^2/n$ gives the standard error $\sigma/\sqrt n$ of the Statistics guide. The LLN says the estimate converges; the CLT (next) says *how fast* and *in what shape*.

<a id="s17"></a>
### The Central Limit Theorem

*Not only does the average converge to the mean — its fluctuations, properly scaled, become Normal regardless of the original distribution.*

**The Central Limit Theorem**

$$\frac{\bar X_n-\mu}{\sigma/\sqrt n}\ \xrightarrow{d}\ N(0,1)\qquad\Longleftrightarrow\qquad \sum_{i=1}^n X_i\ \approx\ N\big(n\mu,\ n\sigma^2\big)$$

The left side standardizes the sample mean: subtract its mean $\mu$ and divide by its standard deviation $\sigma/\sqrt n$ (from §s16). The theorem says this standardized quantity converges in distribution (§s15) to the standard Normal $N(0,1)$ — a bell curve — no matter the shape of the original $X_i$.

*For i.i.d. $X_i$ with finite mean $\mu$ and variance $\sigma^2$, the standardized sum converges in distribution to the standard Normal — whatever the shape of the original distribution.*

**Demonstration — the CLT via MGFs / characteristic functions**

1. **Standardize each term.** Set $Y_i=(X_i-\mu)/\sigma$, so $E[Y_i]=0$ and $\mathrm{Var}(Y_i)=E[Y_i^2]=1$ (§s5). The standardized sum is $S_n=\tfrac{1}{\sqrt n}\sum_{i=1}^n Y_i$, which equals the left-hand side of the theorem.
2. **MGFs multiply.** Because the $Y_i$ are i.i.d. and the sum is scaled by $1/\sqrt n$, the MGF-of-a-sum rule (§s6) gives $M_{S_n}(t)=\big[M_Y\!\big(t/\sqrt n\big)\big]^n$.
3. **Taylor-expand $M_Y$ about $0$** using $M_Y(0)=1$, $M_Y'(0)=E[Y]=0$, $M_Y''(0)=E[Y^2]=1$ (§s6):

   $$M_Y\!\Big(\frac{t}{\sqrt n}\Big)=1+0\cdot\frac{t}{\sqrt n}+\frac12\cdot1\cdot\frac{t^2}{n}+o\!\Big(\frac1n\Big)=1+\frac{t^2}{2n}+o\!\Big(\frac1n\Big),$$

   where $o(1/n)$ denotes terms vanishing faster than $1/n$.
4. **Raise to the $n$th power and take the limit** using $(1+x/n)^n\to e^x$:

   $$M_{S_n}(t)=\Big(1+\frac{t^2/2}{n}+o\big(\tfrac1n\big)\Big)^n\ \longrightarrow\ e^{t^2/2}.$$
5. **Identify the limit.** $e^{t^2/2}$ is the MGF of $N(0,1)$ (§s8); by the continuity theorem (§s15), convergence of MGFs implies $S_n\xrightarrow{d}N(0,1)$.

*The $\sqrt n$ scaling is exactly what keeps the variance at 1 while the higher terms vanish — the bell curve is the universal attractor of normalized sums.*

**Worked example — approximating a binomial.** Let $X\sim\text{Binomial}(100,0.5)$, so $\mu=np=50$ and $\sigma=\sqrt{np(1-p)}=\sqrt{25}=5$. The CLT approximates $X$ by $N(50,5^2)$. The chance of $X\ge60$ is about $P(Z\ge(60-50)/5)=P(Z\ge2)\approx0.0228$ — roughly $2.3\%$, computed entirely from a Normal table even though the exact distribution is a sum of $100$ coin flips.

> **Connection — the spine of all inference**
>
> Density = area → z-scores standardize → the CLT makes $\bar X$ Normal → so confidence intervals and z/t-tests in the Statistics guide are statements about areas under a bell curve. This theorem is why Normal-based inference works on skewed, real data.

<a id="s18"></a>
### A glimpse beyond: measure-theoretic probability & martingales

*Where the rigorous story leads next — the measure-theoretic foundation, and the dynamic theory of processes that evolve fairly in time.*

> **Concept — probability as measure theory**
>
> The fully rigorous setting treats $P$ as a **measure** on a $\sigma$-algebra $\mathcal F$ (the event space of §s1), and expectation as the **Lebesgue integral** $E[X]=\int_\Omega X\,dP$. A *measure* generalizes "size"; the *Lebesgue integral* is a way of integrating that handles far more functions than the ordinary (Riemann) integral. This unifies the discrete sum and the continuous integral into one operation, and lets us handle variables that are neither — mixtures, conditional expectations given a $\sigma$-algebra, and limits that the elementary theory cannot reach.

**The pillars of the rigorous theory**

*The **monotone & dominated convergence** theorems justify swapping limits with expectations (turning $\lim E[X_n]$ into $E[\lim X_n]$). **Fubini–Tonelli** justifies swapping the order of integration we used in the tower property (§s12) and tail-sum proofs (§s5). **Radon–Nikodym** defines densities and conditional expectation in full generality. These theorems make every "swap the order" step in this guide legitimate.*

**Martingales**

$$E\big[X_{n+1}\mid X_1,\dots,X_n\big]=X_n\quad(\text{martingale})$$

A **martingale** is a sequence whose expected next value, given the entire past, equals the present value — a precise model of a fair game.

*A martingale is a model of a fair game: the best forecast of tomorrow's value, given all of today's information, is today's value. Built directly on the conditional expectation of §s12.*

**Worked example — a fair random walk.** Let $S_n=Z_1+\cdots+Z_n$ where each $Z_i$ is $+1$ or $-1$ with probability $\tfrac12$ each (a coin-flip walk). Then $E[S_{n+1}\mid S_1,\dots,S_n]=S_n+E[Z_{n+1}]=S_n+0=S_n$, so $S_n$ is a martingale: knowing the whole history, your best guess for the next position is where you are now.

> **Principle — why martingales matter**
>
> The **optional stopping theorem** says a martingale's expectation is unchanged by a fair stopping rule (no gambling system beats a fair game), and **martingale convergence** guarantees bounded martingales settle to a limit. These tools generalize the laws of large numbers to dependent sequences and underlie stochastic calculus, Brownian motion, and the mathematics of finance.

> **Connection — the road onward**
>
> From here the paths branch: **stochastic processes** (Markov chains, Poisson processes, Brownian motion), **statistical inference** (the companion guide, where these distributions become estimators and tests), and **information theory** (entropy as expected surprise). All of them stand on the foundation built in this guide: a measure, random variables, their moments, and the limit theorems that tame randomness in the aggregate.

---

*A rigorous first course in probability theory — axioms, random variables, transforms, and the limit theorems behind statistical inference — built as a companion to the Complete Statistics guide. Read once for the architecture; return to any box as a reference. Remember: probability runs population → sample; statistics inverts it.*
