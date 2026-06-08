**English** · [中文](probability.zh.md)

# Probability, *made rigorous.*

A full course in mathematical probability — from Kolmogorov's axioms through random variables and their moments to the limit theorems that anchor all of statistics. Every core result is **demonstrated**, and the threads to calculus and inference are made explicit.

[← Back to all guides](../README.md)

## Part A · Foundations

<a id="s0"></a>
### The big picture: chance made rigorous

*Probability is the mathematics of uncertainty — a calculus of how likely things are, built on a tiny set of axioms and reaching all the way to the deep limit theorems.*

For centuries probability was a collection of clever tricks for gamblers. In 1933 Andrey Kolmogorov gave it a rigorous foundation: probability is simply a **measure** — a way of assigning a "size" between 0 and 1 to subsets of a space of outcomes. From three short axioms, the entire subject unfolds by deduction.

- **Model** — encode an experiment as a sample space, events, and a probability measure.
- **Quantify** — attach numbers to outcomes via *random variables*, and summarize them with expectation, variance, and moments.
- **Take limits** — let the number of repetitions grow, and watch order emerge: the laws of large numbers and the central limit theorem.

> **Principle — the two faces of probability**
>
> The **frequentist** reading says $P(A)$ is the long-run fraction of times $A$ occurs in repeated trials; the **subjective** reading says it is a coherent degree of belief. Kolmogorov's axioms are neutral: they describe what any sensible notion of probability must satisfy, leaving the interpretation to you. The mathematics is the same either way.

#### The whole subject on one line

> Axioms → Conditioning & Bayes → Random variables & moments → Joint behavior → Inequalities → Laws of large numbers & the CLT

> **Connection — probability is the engine under statistics**
>
> In the companion *Statistics* guide, probability runs "population $\to$ sample" while inference runs "sample $\to$ population." This guide builds that engine in full: the sampling distributions, standard errors, and Normal approximations used there are theorems proved here in Part D.

<a id="s1"></a>
### Sample spaces, events & the axioms (Kolmogorov)

*Everything begins with a set of outcomes, a collection of events, and a measure on them.*

> **Concept — the probability triple**
>
> A probability model is a triple $(\Omega,\mathcal F,P)$. The **sample space** $\Omega$ is the set of all possible outcomes $\omega$. The **event space** $\mathcal F$ is a collection of subsets of $\Omega$ (the events) closed under complements and countable unions — a $\sigma$-algebra. The **probability measure** $P:\mathcal F\to[0,1]$ assigns each event a likelihood.

**Kolmogorov's axioms**

$$\text{(1)}\ \ P(A)\ge 0\quad\text{for all }A\in\mathcal F$$

$$\text{(2)}\ \ P(\Omega)=1$$

$$\text{(3)}\ \ P\!\Big(\bigcup_{i=1}^{\infty}A_i\Big)=\sum_{i=1}^{\infty}P(A_i)\quad\text{for disjoint }A_i$$

*Axiom (3) is **countable additivity** — the one assumption that does the real work, giving continuity of probability and making limits behave.*

**Demonstration — consequences forced by the axioms**

1. Since $A\cup A^c=\Omega$ are disjoint, $P(A)+P(A^c)=P(\Omega)=1$, so

   $$P(A^c)=1-P(A),\qquad P(\varnothing)=0.$$
2. Write $B=A\cup(B\setminus A)$ disjointly when $A\subseteq B$; additivity gives $P(B)=P(A)+P(B\setminus A)\ge P(A)$, so $P$ is monotone.
3. Split $A\cup B=A\cup(B\setminus A)$ and $B=(A\cap B)\cup(B\setminus A)$, both disjoint, then subtract:

   $$P(A\cup B)=P(A)+P(B)-P(A\cap B).$$

*The inclusion–exclusion rule is not an axiom — it is a theorem. So is monotonicity, and so is $0\le P(A)\le1$.*

**Inclusion–exclusion & continuity**

$$P\!\Big(\bigcup_{i=1}^n A_i\Big)=\sum_i P(A_i)-\sum_{i\lt j}P(A_i\cap A_j)+\cdots+(-1)^{n+1}P\!\Big(\bigcap_{i=1}^n A_i\Big)$$

$$A_n\uparrow A\ \Rightarrow\ P(A_n)\to P(A),\qquad A_n\downarrow A\ \Rightarrow\ P(A_n)\to P(A)$$

*Continuity from below/above is a direct consequence of countable additivity; it is what lets us pass to limits of events.*

> **Concept — equally likely outcomes**
>
> When $\Omega$ is finite with all outcomes equally likely, the measure collapses to counting: $P(A)=|A|/|\Omega|$. This is the classical "favorable over total" probability — and it is exactly why the next section is about counting.

<a id="s2"></a>
### Counting: permutations, combinations & the binomial theorem

*In a uniform model, probability is counting. The combinatorics here powers every discrete distribution that follows.*

**The fundamental counting principles**

$$\text{permutations: }\ P(n,k)=\frac{n!}{(n-k)!},\qquad \text{combinations: }\ \binom nk=\frac{n!}{k!\,(n-k)!}$$

*If a task is a sequence of independent choices with $n_1,n_2,\dots$ options, the total is the **product** $n_1 n_2\cdots$. Permutations count ordered arrangements; combinations count unordered selections.*

**Demonstration — why $\binom nk$ divides out the orderings**

1. Choosing an ordered list of $k$ from $n$ items gives $P(n,k)=n(n-1)\cdots(n-k+1)=\tfrac{n!}{(n-k)!}$ ways.
2. Each unordered set of $k$ items can be ordered in $k!$ ways, so it is counted $k!$ times in that list.
3. Divide to remove the overcount:

   $$\binom nk=\frac{P(n,k)}{k!}=\frac{n!}{k!\,(n-k)!}.$$

*The binomial coefficient is "choose $k$, ignoring order."*

**The binomial theorem & Pascal's rule**

$$(x+y)^n=\sum_{k=0}^{n}\binom nk x^k y^{n-k},\qquad \binom nk=\binom{n-1}{k-1}+\binom{n-1}{k}$$

*Setting $x=y=1$ gives $\sum_k\binom nk=2^n$: the number of subsets of an $n$-set. Pascal's rule builds the triangle row by row.*

**Demonstration — the binomial theorem by counting**

1. Expand $(x+y)^n=(x+y)(x+y)\cdots(x+y)$: each term picks either $x$ or $y$ from each of the $n$ factors.
2. A term with exactly $k$ copies of $x$ (and $n-k$ of $y$) is $x^k y^{n-k}$; the number of ways to choose which $k$ factors supply $x$ is $\binom nk$.
3. Summing over $k$ gives

   $$(x+y)^n=\sum_{k=0}^n\binom nk x^k y^{n-k}.$$

*This identity is precisely why the binomial distribution's probabilities sum to 1.*

> **Concept — distinguishable vs not, replacement vs not**
>
> The four classic counting regimes: ordered with replacement $n^k$; ordered without $\tfrac{n!}{(n-k)!}$; unordered without $\binom nk$; unordered with replacement $\binom{n+k-1}{k}$ (stars and bars). Identifying which regime you are in is the whole art of combinatorial probability.

<a id="s3"></a>
### Conditional probability, independence & Bayes' theorem

*How information reshapes probability — and how to invert the direction of conditioning.*

**Conditioning, the chain rule & independence**

$$P(A\mid B)=\frac{P(A\cap B)}{P(B)}\quad(P(B)\gt0)$$

$$P(A_1\cap\cdots\cap A_n)=P(A_1)\,P(A_2\mid A_1)\cdots P(A_n\mid A_1\cap\cdots\cap A_{n-1})$$

$$A\perp B \iff P(A\cap B)=P(A)P(B) \iff P(A\mid B)=P(A)$$

*Conditioning on $B$ restricts the world to $B$ and renormalizes. Independence means $B$ carries no information about $A$.*

**Law of total probability & Bayes' theorem**

$$P(B)=\sum_i P(B\mid A_i)\,P(A_i)\quad\text{for a partition }\{A_i\}$$

$$P(A_i\mid B)=\frac{P(B\mid A_i)\,P(A_i)}{\sum_j P(B\mid A_j)\,P(A_j)}$$

**Demonstration — Bayes' theorem in two lines**

1. The multiplication rule writes the joint probability two ways:

   $$P(A\cap B)=P(A\mid B)P(B)=P(B\mid A)P(A).$$
2. Equate the right-hand expressions and divide by $P(B)$, then expand $P(B)$ by total probability:

   $$P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}.$$

*Bayes turns "likelihood of the evidence given the cause" into "probability of the cause given the evidence."*

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
> A **random variable** $X$ is a (measurable) function $X:\Omega\to\mathbb R$ that assigns a number to each outcome. It does not "have" a value until the experiment is run; what it has is a *distribution* — the way probability is spread across its possible values.

**The cumulative distribution function (CDF)**

$$F_X(x)=P(X\le x)$$

*Every CDF is non-decreasing, right-continuous, with $F(-\infty)=0$ and $F(+\infty)=1$. The CDF exists for *every* random variable, discrete or continuous, and determines the distribution completely.*

**PMF (discrete) and PDF (continuous)**

$$\text{discrete: }\ p_X(x)=P(X=x),\qquad \sum_x p_X(x)=1$$

$$\text{continuous: }\ f_X(x)=F_X'(x),\qquad P(a\le X\le b)=\int_a^b f_X(x)\,dx,\qquad \int_{-\infty}^{\infty}f_X=1$$

*For a continuous variable, $P(X=x)=0$ for every single point: probability is **area**, not height. The density $f$ can exceed 1; only its integral is constrained.*

**Demonstration — recovering probabilities from the CDF**

1. For any $a\lt b$, the event $\{X\le b\}$ splits into the disjoint $\{X\le a\}$ and $\{a\lt X\le b\}$.
2. By additivity, $P(a\lt X\le b)=F(b)-F(a)$.
3. The jump of $F$ at a point is the point mass: Continuous CDFs have no jumps, so each point has probability zero.

   $$P(X=x)=F(x)-F(x^-).$$

*The CDF is the universal currency: differentiate it for a density, difference it for a mass function.*

> **Connection — this is where calculus enters**
>
> For continuous variables the density plays the role of an ordinary function and probability is the integral under it. Expectations, percentiles, p-values, and the Normal curve are all areas — the integral calculus you already know, applied to $f_X$.

<a id="s5"></a>
### Expectation, variance & moments

*Expectation is the center of mass of a distribution; variance is its moment of inertia; higher moments fill in the shape.*

**Expectation & the law of the unconscious statistician**

$$E[X]=\sum_x x\,p_X(x)\quad\text{(discrete)},\qquad E[X]=\int_{-\infty}^{\infty} x\,f_X(x)\,dx\quad\text{(continuous)}$$

$$E[g(X)]=\sum_x g(x)\,p_X(x)\quad\text{or}\quad \int g(x)\,f_X(x)\,dx$$

*LOTUS: to average $g(X)$ you need not find the distribution of $g(X)$ — just integrate $g$ against the density of $X$.*

**Variance, moments & linearity**

$$\operatorname{Var}(X)=E\big[(X-\mu)^2\big]=E[X^2]-\big(E[X]\big)^2$$

$$E[aX+b]=aE[X]+b,\qquad \operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$$

$$\mu_k=E\big[(X-\mu)^k\big]:\quad \text{skewness}=\tfrac{\mu_3}{\sigma^3},\quad \text{kurtosis}=\tfrac{\mu_4}{\sigma^4}$$

*Expectation is linear unconditionally; variance scales by the square and is shift-invariant.*

**Demonstration — the computational variance formula**

1. Expand the square in the definition:

   $$\operatorname{Var}(X)=E\big[(X-\mu)^2\big]=E\big[X^2-2\mu X+\mu^2\big].$$
2. Use linearity and $E[X]=\mu$:

   $$=E[X^2]-2\mu\,E[X]+\mu^2=E[X^2]-2\mu^2+\mu^2.$$
3. Collect terms:

   $$\operatorname{Var}(X)=E[X^2]-\mu^2=E[X^2]-(E[X])^2.$$

*"Mean of the square minus the square of the mean" — the everyday variance formula.*

**Demonstration — $E[X]$ for a non-negative variable via its tail**

1. For $X\ge0$ continuous, write $x=\int_0^x dt=\int_0^\infty \mathbf 1\{t\lt x\}\,dt$.
2. Take expectations and swap order (Tonelli):

   $$E[X]=\int_0^\infty E[\mathbf 1\{t\lt X\}]\,dt=\int_0^\infty P(X\gt t)\,dt.$$

*The expectation equals the area above the CDF — a tail-sum formula reused throughout the limit theorems.*

<a id="s6"></a>
### Moment generating & characteristic functions

*Encode all moments in a single function. Transforms turn convolutions into products and make the CLT a one-line limit.*

**MGF and characteristic function**

$$M_X(t)=E\big[e^{tX}\big],\qquad \varphi_X(t)=E\big[e^{itX}\big]$$

$$M_X^{(k)}(0)=E[X^k],\qquad M_X(t)=\sum_{k=0}^{\infty}\frac{E[X^k]}{k!}\,t^k$$

*The MGF "generates" moments by differentiation at 0. The characteristic function $\varphi$ always exists (since $|e^{itX}|=1$) and uniquely determines the distribution.*

**Demonstration — why $M^{(k)}(0)=E[X^k]$**

1. Expand the exponential inside the expectation:

   $$M_X(t)=E\Big[\sum_{k=0}^\infty \frac{(tX)^k}{k!}\Big]=\sum_{k=0}^\infty \frac{t^k}{k!}E[X^k].$$
2. This is a Taylor series in $t$; the coefficient of $t^k$ is $E[X^k]/k!$.
3. Differentiating $k$ times and setting $t=0$ extracts that coefficient:

   $$M_X^{(k)}(0)=E[X^k].$$

*Differentiation replaces integration — the practical reason MGFs are so convenient.*

**Demonstration — computing the exponential MGF and its moments**

1. For $X\sim\text{Exp}(\lambda)$, $f(x)=\lambda e^{-\lambda x}$ on $x\ge0$:

   $$M_X(t)=\int_0^\infty e^{tx}\lambda e^{-\lambda x}\,dx=\lambda\int_0^\infty e^{-(\lambda-t)x}\,dx=\frac{\lambda}{\lambda-t},\ \ t\lt\lambda.$$
2. Differentiate: $M'(t)=\dfrac{\lambda}{(\lambda-t)^2}$, so $E[X]=M'(0)=1/\lambda$.
3. Differentiate again: $M''(t)=\dfrac{2\lambda}{(\lambda-t)^3}$, so $E[X^2]=2/\lambda^2$ and

   $$\operatorname{Var}(X)=\frac{2}{\lambda^2}-\frac1{\lambda^2}=\frac1{\lambda^2}.$$

*One transform delivered both the mean and the variance with no further integration.*

**The key property: MGF of a sum**

$$X\perp Y\ \Rightarrow\ M_{X+Y}(t)=M_X(t)\,M_Y(t)$$

*Because $e^{t(X+Y)}=e^{tX}e^{tY}$ and independence factors the expectation. Sums of independent variables $\leftrightarrow$ products of transforms — the basis of convolution and of the CLT proof.*

> **Connection — calculus: Taylor series & transforms**
>
> The MGF is just the exponential generating function of the moment sequence; reading off moments is reading Taylor coefficients. The characteristic function is the Fourier transform of the density — which is why inverting it recovers the distribution.

<a id="s7"></a>
### Common discrete distributions

*A handful of named laws model most counting situations. Know each one's story, mean, variance, and MGF.*

| Distribution | PMF $p(k)$ | Mean | Variance | MGF $M(t)$ |
| --- | --- | --- | --- | --- |
| Bernoulli($p$) | $p^k(1-p)^{1-k},\ k\in\{0,1\}$ | $p$ | $p(1-p)$ | $1-p+pe^{t}$ |
| Binomial($n,p$) | $\binom nk p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ | $(1-p+pe^{t})^n$ |
| Geometric($p$) | $(1-p)^{k-1}p,\ k\ge1$ | $1/p$ | $(1-p)/p^2$ | $\dfrac{pe^{t}}{1-(1-p)e^{t}}$ |
| Neg. Binomial($r,p$) | $\binom{k-1}{r-1}p^r(1-p)^{k-r}$ | $r/p$ | $r(1-p)/p^2$ | $\big(\tfrac{pe^{t}}{1-(1-p)e^{t}}\big)^r$ |
| Poisson($\lambda$) | $e^{-\lambda}\lambda^k/k!$ | $\lambda$ | $\lambda$ | $e^{\lambda(e^{t}-1)}$ |

**Demonstration — building the Binomial from Bernoulli (mean & variance)**

1. Write $X=X_1+\cdots+X_n$ as a sum of i.i.d. Bernoulli($p$) indicators, each with $E[X_i]=p$ and $\operatorname{Var}(X_i)=p(1-p)$.
2. By linearity (no independence needed):

   $$E[X]=\sum_{i=1}^n E[X_i]=np.$$
3. By independence, variances add:

   $$\operatorname{Var}(X)=\sum_{i=1}^n \operatorname{Var}(X_i)=np(1-p).$$
4. The MGF multiplies: $M_{X_i}(t)=1-p+pe^t$, so $M_X(t)=(1-p+pe^t)^n$, confirming the table.

*Decompose into simple pieces, then sum — the recurring move of probability.*

**Demonstration — mean and variance of the Poisson**

1. Compute the mean directly:

   $$E[X]=\sum_{k=0}^\infty k\,\frac{e^{-\lambda}\lambda^k}{k!}=\lambda e^{-\lambda}\sum_{k=1}^\infty\frac{\lambda^{k-1}}{(k-1)!}=\lambda e^{-\lambda}e^{\lambda}=\lambda.$$
2. For the variance use the MGF $M(t)=e^{\lambda(e^t-1)}$: $M'(t)=\lambda e^t M(t)$, so $E[X]=M'(0)=\lambda$.
3. Differentiate again: $M''(t)=\lambda e^t M(t)+(\lambda e^t)^2 M(t)$, giving $E[X^2]=\lambda+\lambda^2$, hence

   $$\operatorname{Var}(X)=\lambda+\lambda^2-\lambda^2=\lambda.$$

*The Poisson's signature: its mean and variance coincide.*

**Demonstration — mean of the Geometric and its memorylessness**

1. With $q=1-p$, $E[X]=\sum_{k\ge1}k\,q^{k-1}p=p\sum_{k\ge1}kq^{k-1}=p\cdot\dfrac{1}{(1-q)^2}=\dfrac1p$ using $\sum_{k\ge1}kq^{k-1}=(1-q)^{-2}$.
2. Memorylessness: $P(X\gt m+n\mid X\gt m)=\dfrac{q^{m+n}}{q^{m}}=q^{n}=P(X\gt n)$.

*The geometric is the unique discrete memoryless law — the exponential's discrete twin.*

> **Connection — the Poisson as a binomial limit**
>
> Let $n\to\infty$ and $p\to0$ with $np\to\lambda$. Then $(1-p+pe^t)^n=(1+\tfrac{\lambda}{n}(e^t-1))^n\to e^{\lambda(e^t-1)}$, the Poisson MGF. So the Poisson is the law of rare events — many trials, tiny success probability.

<a id="s8"></a>
### Common continuous distributions

*The continuous catalog: each is a density, an integral, and a transform. The Normal sits at the center of it all.*

| Distribution | PDF $f(x)$ | Mean | Variance | MGF $M(t)$ |
| --- | --- | --- | --- | --- |
| Uniform($a,b$) | $\dfrac{1}{b-a}$ on $[a,b]$ | $\dfrac{a+b}{2}$ | $\dfrac{(b-a)^2}{12}$ | $\dfrac{e^{tb}-e^{ta}}{t(b-a)}$ |
| Exponential($\lambda$) | $\lambda e^{-\lambda x},\ x\ge0$ | $1/\lambda$ | $1/\lambda^2$ | $\dfrac{\lambda}{\lambda-t},\ t\lt\lambda$ |
| Gamma($\alpha,\lambda$) | $\dfrac{\lambda^\alpha x^{\alpha-1}e^{-\lambda x}}{\Gamma(\alpha)},\ x\ge0$ | $\alpha/\lambda$ | $\alpha/\lambda^2$ | $\big(\tfrac{\lambda}{\lambda-t}\big)^\alpha$ |
| Normal($\mu,\sigma^2$) | $\dfrac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/2\sigma^2}$ | $\mu$ | $\sigma^2$ | $e^{\mu t+\sigma^2 t^2/2}$ |
| Beta($\alpha,\beta$) | $\dfrac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)},\ x\in[0,1]$ | $\dfrac{\alpha}{\alpha+\beta}$ | $\dfrac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$ | — |

**Demonstration — mean and variance of the Uniform$(a,b)$**

1. Mean:

   $$E[X]=\int_a^b \frac{x}{b-a}\,dx=\frac{1}{b-a}\cdot\frac{b^2-a^2}{2}=\frac{a+b}{2}.$$
2. Second moment:

   $$E[X^2]=\int_a^b\frac{x^2}{b-a}\,dx=\frac{b^3-a^3}{3(b-a)}=\frac{a^2+ab+b^2}{3}.$$
3. Subtract the squared mean:

   $$\operatorname{Var}(X)=\frac{a^2+ab+b^2}{3}-\frac{(a+b)^2}{4}=\frac{(b-a)^2}{12}.$$

*Spread depends only on the width $b-a$, as symmetry demands.*

**Demonstration — mean and variance of the Exponential by integration**

1. Integrate by parts:

   $$E[X]=\int_0^\infty x\,\lambda e^{-\lambda x}\,dx=\Big[-xe^{-\lambda x}\Big]_0^\infty+\int_0^\infty e^{-\lambda x}\,dx=\frac1\lambda.$$
2. Similarly $E[X^2]=\int_0^\infty x^2\lambda e^{-\lambda x}\,dx=\dfrac{2}{\lambda^2}$.
3. Hence $\operatorname{Var}(X)=\dfrac{2}{\lambda^2}-\dfrac{1}{\lambda^2}=\dfrac{1}{\lambda^2}$, matching the MGF result of Section 6.

*The exponential is memoryless: $P(X\gt s+t\mid X\gt s)=e^{-\lambda t}=P(X\gt t)$.*

**Demonstration — the Normal MGF gives mean $\mu$ and variance $\sigma^2$**

1. For $Z\sim N(0,1)$, complete the square:

   $$M_Z(t)=\frac{1}{\sqrt{2\pi}}\int e^{tz-z^2/2}\,dz=e^{t^2/2}\cdot\frac{1}{\sqrt{2\pi}}\int e^{-(z-t)^2/2}\,dz=e^{t^2/2}.$$
2. For $X=\mu+\sigma Z$: $M_X(t)=e^{\mu t}M_Z(\sigma t)=e^{\mu t+\sigma^2 t^2/2}$.
3. Then $M_X'(0)=\mu$ and $M_X''(0)=\mu^2+\sigma^2$, so $E[X]=\mu$ and $\operatorname{Var}(X)=\sigma^2$.

*The two parameters $\mu,\sigma^2$ are literally the mean and variance — and the standardizing $Z=(X-\mu)/\sigma$ is the z-score of the Statistics guide.*

> **Connection — one family, many faces**
>
> Exponential = Gamma($1,\lambda$); a sum of $n$ i.i.d. exponentials is Gamma($n,\lambda$) (Section 13); the chi-square with $k$ degrees of freedom is Gamma($k/2,1/2$). The Beta governs proportions and is the conjugate prior to the binomial — the bridge to Bayesian inference.

<a id="s9"></a>
### Functions & transformations of random variables

*If you know the law of $X$, what is the law of $Y=g(X)$? Two reliable methods: the CDF method and the Jacobian.*

**The change-of-variables formula**

$$\text{CDF method: }\ F_Y(y)=P(g(X)\le y),\quad\text{then }f_Y=F_Y'$$

$$\text{Jacobian (monotone }g): \ f_Y(y)=f_X\big(g^{-1}(y)\big)\,\Big|\frac{d}{dy}g^{-1}(y)\Big|$$

*The CDF method always works; the Jacobian formula is its shortcut when $g$ is smooth and one-to-one. For many-to-one $g$, sum over all preimages.*

**Demonstration — the probability integral transform**

1. Let $X$ have continuous, strictly increasing CDF $F$, and set $U=F(X)$. For $u\in(0,1)$:

   $$F_U(u)=P(F(X)\le u)=P\big(X\le F^{-1}(u)\big)=F\big(F^{-1}(u)\big)=u.$$
2. So $U\sim\text{Uniform}(0,1)$. Conversely $X=F^{-1}(U)$ has CDF $F$.

*This is how computers simulate any distribution: feed a uniform random number through $F^{-1}$.*

**Demonstration — the square of a standard Normal is chi-square (Jacobian, two branches)**

1. Let $Z\sim N(0,1)$ and $Y=Z^2$. For $y\gt0$, $g(z)=z^2$ is two-to-one with preimages $\pm\sqrt y$.
2. Use the CDF method: $F_Y(y)=P(-\sqrt y\le Z\le\sqrt y)=2\Phi(\sqrt y)-1$.
3. Differentiate via the chain rule:

   $$f_Y(y)=2\varphi(\sqrt y)\cdot\frac{1}{2\sqrt y}=\frac{1}{\sqrt{2\pi y}}e^{-y/2},\quad y\gt0.$$

*This is the $\chi^2_1$ density = Gamma($\tfrac12,\tfrac12$) — the foundation of the chi-square tests in the Statistics guide.*

**Demonstration — a linear transform of a Normal stays Normal**

1. Let $X\sim N(\mu,\sigma^2)$, $Y=aX+b$ with $a\gt0$. Then $g^{-1}(y)=(y-b)/a$ and $\big|\tfrac{d}{dy}g^{-1}\big|=1/a$.
2. Substitute into the Jacobian formula:

   $$f_Y(y)=\frac{1}{a}\cdot\frac{1}{\sigma\sqrt{2\pi}}\exp\!\Big(-\frac{((y-b)/a-\mu)^2}{2\sigma^2}\Big)=\frac{1}{(a\sigma)\sqrt{2\pi}}\exp\!\Big(-\frac{(y-(a\mu+b))^2}{2a^2\sigma^2}\Big).$$

*So $Y\sim N(a\mu+b,\,a^2\sigma^2)$: the Normal family is closed under affine maps — which is exactly why standardizing works.*

## Part C · Multiple random variables

<a id="s10"></a>
### Joint, marginal & conditional distributions

*Two or more random variables live together in a joint law; marginals and conditionals are the views you take of it.*

**Joint, marginal & conditional densities**

$$\text{joint CDF: }\ F(x,y)=P(X\le x,\,Y\le y),\qquad f(x,y)=\frac{\partial^2 F}{\partial x\,\partial y}$$

$$\text{marginal: }\ f_X(x)=\int f(x,y)\,dy,\qquad \text{conditional: }\ f_{Y\mid X}(y\mid x)=\frac{f(x,y)}{f_X(x)}$$

$$X\perp Y \iff f(x,y)=f_X(x)\,f_Y(y)$$

*The marginal integrates out the other variable; the conditional renormalizes a slice. Independence means the joint factors into its marginals.*

**Demonstration — marginalizing a joint uniform on the unit triangle**

1. Let $(X,Y)$ be uniform on $\{0\lt x\lt y\lt1\}$, so $f(x,y)=2$ there (area $=\tfrac12$, density $=1/\text{area}$).
2. Marginal of $X$: integrate over $y$ from $x$ to $1$:

   $$f_X(x)=\int_x^1 2\,dy=2(1-x),\quad 0\lt x\lt1.$$
3. Conditional of $Y$ given $X=x$: i.e. $Y\mid X=x$ is uniform on $(x,1)$.

   $$f_{Y\mid X}(y\mid x)=\frac{2}{2(1-x)}=\frac{1}{1-x},\quad x\lt y\lt1,$$

*Here $X$ and $Y$ are dependent: the joint does not factor.*

> **Concept — expectation over a joint law**
>
> For any $g$, $E[g(X,Y)]=\iint g(x,y)\,f(x,y)\,dx\,dy$. In particular $E[XY]$ is computed against the joint density — and it is exactly this quantity that measures how the variables move together (next section).

<a id="s11"></a>
### Covariance, correlation & independence

*Covariance measures co-movement; correlation rescales it to a unitless number in $[-1,1]$.*

**Covariance, correlation & variance of a sum**

$$\operatorname{Cov}(X,Y)=E[XY]-E[X]E[Y],\qquad \rho=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}$$

$$\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y)$$

$$\operatorname{Cov}(aX+b,\,cY+d)=ac\,\operatorname{Cov}(X,Y)$$

*$\rho\in[-1,1]$ is the average product of the two variables' z-scores. Independence $\Rightarrow$ $\operatorname{Cov}=0$, but not conversely.*

**Demonstration — independence implies zero covariance (and why not the reverse)**

1. If $X\perp Y$, the joint factors so $E[XY]=\iint xy\,f_X(x)f_Y(y)\,dx\,dy=E[X]E[Y]$.
2. Hence $\operatorname{Cov}(X,Y)=E[XY]-E[X]E[Y]=0$.
3. The converse fails: let $X\sim N(0,1)$ and $Y=X^2$. Then $E[XY]=E[X^3]=0=E[X]E[Y]$, so $\operatorname{Cov}=0$, yet $Y$ is a deterministic function of $X$ — maximally dependent.

*Covariance sees only *linear* association; zero covariance is not independence.*

**Demonstration — $|\rho|\le1$ via Cauchy–Schwarz**

1. The Cauchy–Schwarz inequality for random variables: $\big(E[UV]\big)^2\le E[U^2]\,E[V^2]$.
2. Apply it to the centered variables $U=X-\mu_X,\ V=Y-\mu_Y$:

   $$\operatorname{Cov}(X,Y)^2\le \operatorname{Var}(X)\,\operatorname{Var}(Y).$$
3. Divide by $\sigma_X^2\sigma_Y^2$: with equality iff $Y$ is an exact linear function of $X$.

   $$\rho^2\le1\ \Rightarrow\ -1\le\rho\le1,$$

*Correlation is bounded precisely because Cauchy–Schwarz bounds the inner product by the norms.*

> **Connection — to regression in the Statistics guide**
>
> The least-squares slope is $b_1=\rho\,\sigma_Y/\sigma_X$ and $R^2=\rho^2$. The correlation coefficient computed from data is the sample version of the $\rho$ defined here from a joint distribution.

<a id="s12"></a>
### Conditional expectation & the tower property

*Conditional expectation is the best prediction of one variable given another — and it averages back to the unconditional mean.*

**Conditional expectation & its laws**

$$E[X\mid Y=y]=\int x\,f_{X\mid Y}(x\mid y)\,dx,\qquad E[X\mid Y]=g(Y)\ \text{is a random variable}$$

$$\text{tower: }\ E\big[E[X\mid Y]\big]=E[X]$$

$$\text{law of total variance: }\ \operatorname{Var}(X)=E\big[\operatorname{Var}(X\mid Y)\big]+\operatorname{Var}\big(E[X\mid Y]\big)$$

*$E[X\mid Y]$ is the function of $Y$ that best predicts $X$ in mean-square. It is itself random because $Y$ is.*

**Demonstration — the tower property $E[E[X\mid Y]]=E[X]$**

1. By definition the inner expectation is $E[X\mid Y=y]=\int x\,f_{X\mid Y}(x\mid y)\,dx$.
2. Average it over the distribution of $Y$:

   $$E\big[E[X\mid Y]\big]=\int\!\Big(\int x\,f_{X\mid Y}(x\mid y)\,dx\Big)f_Y(y)\,dy.$$
3. Use $f_{X\mid Y}(x\mid y)\,f_Y(y)=f(x,y)$ and swap the order of integration:

   $$=\int x\Big(\int f(x,y)\,dy\Big)dx=\int x\,f_X(x)\,dx=E[X].$$

*"Average the conditional averages, weighting by the conditioner" — and you recover the grand average.*

**Demonstration — total variance from the tower property**

1. Let $m(Y)=E[X\mid Y]$. Write $\operatorname{Var}(X\mid Y)=E[X^2\mid Y]-m(Y)^2$.
2. Take expectations: $E[\operatorname{Var}(X\mid Y)]=E[X^2]-E[m(Y)^2]$ by the tower property on $E[X^2\mid Y]$.
3. Add $\operatorname{Var}(m(Y))=E[m(Y)^2]-(E[X])^2$; the $E[m(Y)^2]$ cancels, leaving

   $$E[\operatorname{Var}(X\mid Y)]+\operatorname{Var}(E[X\mid Y])=E[X^2]-(E[X])^2=\operatorname{Var}(X).$$

*Variance splits into "within-group" plus "between-group" — exactly the decomposition behind ANOVA.*

> **Connection — martingales (Section 18)**
>
> Conditional expectation given a $\sigma$-algebra is the abstract version of this idea, and a martingale is a process whose conditional expectation of the future, given the past, equals the present. The tower property is the engine of that whole theory.

<a id="s13"></a>
### Sums of random variables & convolutions

*The density of a sum of independent variables is the convolution of their densities — and transforms turn that convolution into a product.*

**The convolution formula**

$$Z=X+Y,\ X\perp Y:\quad f_Z(z)=\int_{-\infty}^{\infty} f_X(x)\,f_Y(z-x)\,dx$$

$$\text{discrete: }\ p_Z(z)=\sum_{x}p_X(x)\,p_Y(z-x),\qquad M_Z(t)=M_X(t)\,M_Y(t)$$

*Adding independent variables $\leftrightarrow$ convolving densities $\leftrightarrow$ multiplying transforms. The last is usually the easy route.*

**Demonstration — the sum of two independent Uniform$(0,1)$ is triangular**

1. With $f_X=f_Y=1$ on $[0,1]$, the convolution is $f_Z(z)=\int_0^1 \mathbf 1\{0\le z-x\le1\}\,dx$, the length of the overlap.
2. For $0\le z\le1$: $x$ ranges over $[0,z]$, so $f_Z(z)=z$.
3. For $1\le z\le2$: $x$ ranges over $[z-1,1]$, so $f_Z(z)=2-z$. Together:

   $$f_Z(z)=\begin{cases}z,&0\le z\le1\\ 2-z,&1\le z\le2\end{cases}$$

*The flat uniform convolves into a triangle — the first visible step toward the bell curve of the CLT.*

**Demonstration — the sum of $n$ i.i.d. Exponentials is Gamma (via MGFs)**

1. Each $X_i\sim\text{Exp}(\lambda)$ has MGF $M_{X_i}(t)=\dfrac{\lambda}{\lambda-t}$.
2. For the sum $S_n=X_1+\cdots+X_n$, MGFs multiply:

   $$M_{S_n}(t)=\Big(\frac{\lambda}{\lambda-t}\Big)^n.$$
3. This is exactly the Gamma$(n,\lambda)$ MGF from Section 8, so by uniqueness

   $$S_n\sim\text{Gamma}(n,\lambda),\qquad f_{S_n}(s)=\frac{\lambda^n s^{n-1}e^{-\lambda s}}{(n-1)!}.$$

*Waiting times for $n$ Poisson arrivals add up to a Gamma — and the MGF made it a one-line proof.*

> **Connection — sums are the heart of the limit theorems**
>
> The sample mean $\bar X_n=\tfrac1n\sum X_i$ is a scaled sum. Understanding sums — their means, variances, and limiting shapes — is precisely the program of Part D.

## Part D · Limit theorems

<a id="s14"></a>
### Probability inequalities (Markov, Chebyshev, Jensen, Cauchy–Schwarz)

*Inequalities bound tail probabilities and expectations with almost no assumptions — the scaffolding of every convergence proof.*

**The four workhorse inequalities**

$$\text{Markov: }\ P(X\ge a)\le\frac{E[X]}{a}\quad(X\ge0,\ a\gt0)$$

$$\text{Chebyshev: }\ P\big(|X-\mu|\ge k\big)\le\frac{\sigma^2}{k^2}$$

$$\text{Jensen: }\ \varphi\text{ convex}\Rightarrow \varphi(E[X])\le E[\varphi(X)]$$

$$\text{Cauchy–Schwarz: }\ \big(E[XY]\big)^2\le E[X^2]\,E[Y^2]$$

**Demonstration — Markov, then Chebyshev as a corollary**

1. For $X\ge0$ and $a\gt0$, use the indicator bound $a\,\mathbf 1\{X\ge a\}\le X$. Take expectations:

   $$a\,P(X\ge a)\le E[X]\ \Rightarrow\ P(X\ge a)\le\frac{E[X]}{a}.$$
2. Apply Markov to the non-negative variable $(X-\mu)^2$ at level $k^2$:

   $$P\big((X-\mu)^2\ge k^2\big)\le\frac{E[(X-\mu)^2]}{k^2}=\frac{\sigma^2}{k^2}.$$
3. The event $(X-\mu)^2\ge k^2$ is the same as $|X-\mu|\ge k$, giving Chebyshev's inequality.

*Chebyshev is just Markov applied to the squared deviation — the bound that powers the Weak Law.*

**Demonstration — Jensen's inequality from a supporting line**

1. A convex $\varphi$ lies above each tangent (supporting) line. At the point $\mu=E[X]$: $\varphi(x)\ge\varphi(\mu)+c\,(x-\mu)$ for the slope $c$.
2. Take expectations of both sides:

   $$E[\varphi(X)]\ge\varphi(\mu)+c\,(E[X]-\mu)=\varphi(\mu)=\varphi(E[X]).$$

*Hence $E[X^2]\ge(E[X])^2$ (so variance $\ge0$) and $E[1/X]\ge1/E[X]$ for positive $X$ — both special cases.*

<a id="s15"></a>
### Modes of convergence

*"A sequence of random variables converges" can mean several different things. The hierarchy among them organizes the limit theorems.*

**Four modes of convergence**

$$\text{a.s.: }\ P\big(X_n\to X\big)=1$$

$$\text{in prob.: }\ \forall\varepsilon\gt0,\ P\big(|X_n-X|\ge\varepsilon\big)\to0$$

$$\text{in }L^p:\ E\big[|X_n-X|^p\big]\to0$$

$$\text{in distribution: }\ F_{X_n}(x)\to F_X(x)\ \text{at continuity points of }F_X$$

> **Principle — the hierarchy**
>
> Almost-sure and $L^p$ convergence each imply convergence **in probability**, which in turn implies convergence **in distribution**. The reverse arrows fail in general. Convergence in distribution is the weakest — it concerns only the laws, not the variables themselves — and it is the mode of the CLT.

**Demonstration — $L^2$ convergence implies convergence in probability**

1. Suppose $E[(X_n-X)^2]\to0$. Apply Markov to the non-negative $(X_n-X)^2$ at level $\varepsilon^2$:

   $$P\big(|X_n-X|\ge\varepsilon\big)=P\big((X_n-X)^2\ge\varepsilon^2\big)\le\frac{E[(X_n-X)^2]}{\varepsilon^2}.$$
2. The right side $\to0$ for every fixed $\varepsilon\gt0$, which is convergence in probability.

*This Markov-based step is exactly how the Weak Law is proved in the next section.*

**Continuity theorem (the CLT tool)**

$$\varphi_{X_n}(t)\to\varphi_X(t)\ \forall t\ \iff\ X_n\xrightarrow{d}X$$

*Lévy's continuity theorem: convergence of characteristic functions is equivalent to convergence in distribution. This is the lever that proves the CLT.*

<a id="s16"></a>
### The Laws of Large Numbers

*Averages of many independent trials converge to the true mean. This is the theorem that justifies the frequentist interpretation of probability.*

**Weak and Strong laws**

$$\text{WLLN: }\ \bar X_n\xrightarrow{P}\mu\quad\text{(convergence in probability)}$$

$$\text{SLLN: }\ \bar X_n\xrightarrow{a.s.}\mu\quad\text{(almost-sure convergence)}$$

*Both require i.i.d. $X_i$ with finite mean $\mu$ (the WLLN here also uses finite variance). The strong law is the deeper statement.*

**Demonstration — the Weak Law via Chebyshev**

1. Let $X_1,\dots,X_n$ be i.i.d. with mean $\mu$, variance $\sigma^2$. Then $E[\bar X_n]=\mu$.
2. The variance of the average shrinks:

   $$\operatorname{Var}(\bar X_n)=\frac{1}{n^2}\sum_{i=1}^n\operatorname{Var}(X_i)=\frac{\sigma^2}{n}.$$
3. Apply Chebyshev to $\bar X_n$:

   $$P\big(|\bar X_n-\mu|\ge\varepsilon\big)\le\frac{\operatorname{Var}(\bar X_n)}{\varepsilon^2}=\frac{\sigma^2}{n\varepsilon^2}\xrightarrow[n\to\infty]{}0.$$

*As $n$ grows the average concentrates on $\mu$ — that is convergence in probability, the Weak Law.*

> **Connection — why the standard error has a $\sqrt n$**
>
> The same computation $\operatorname{Var}(\bar X_n)=\sigma^2/n$ gives the standard error $\sigma/\sqrt n$ of the Statistics guide. The LLN says the estimate converges; the CLT (next) says *how fast* and *in what shape*.

<a id="s17"></a>
### The Central Limit Theorem

*Not only does the average converge to the mean — its fluctuations, properly scaled, become Normal regardless of the original distribution.*

**The Central Limit Theorem**

$$\frac{\bar X_n-\mu}{\sigma/\sqrt n}\ \xrightarrow{d}\ N(0,1)\qquad\Longleftrightarrow\qquad \sum_{i=1}^n X_i\ \approx\ N\big(n\mu,\ n\sigma^2\big)$$

*For i.i.d. $X_i$ with finite mean $\mu$ and variance $\sigma^2$, the standardized sum converges in distribution to the standard Normal — whatever the shape of the original distribution.*

**Demonstration — the CLT via MGFs / characteristic functions**

1. Standardize each term: $Y_i=(X_i-\mu)/\sigma$, so $E[Y_i]=0,\ \operatorname{Var}(Y_i)=1$. The scaled sum is $S_n=\tfrac{1}{\sqrt n}\sum_{i=1}^n Y_i$.
2. Independence makes MGFs multiply: $M_{S_n}(t)=\big[M_Y\!\big(t/\sqrt n\big)\big]^n$.
3. Taylor-expand $M_Y$ about 0 using $M_Y(0)=1,\ M_Y'(0)=0,\ M_Y''(0)=1$:

   $$M_Y\!\Big(\frac{t}{\sqrt n}\Big)=1+\frac{t^2}{2n}+o\!\Big(\frac1n\Big).$$
4. Raise to the $n$th power and take the limit:

   $$M_{S_n}(t)=\Big(1+\frac{t^2/2}{n}+o\big(\tfrac1n\big)\Big)^n\ \longrightarrow\ e^{t^2/2}.$$
5. But $e^{t^2/2}$ is the MGF of $N(0,1)$; by the continuity theorem, $S_n\xrightarrow{d}N(0,1)$.

*The $\sqrt n$ scaling is exactly what keeps the variance at 1 while the higher terms vanish — the bell curve is the universal attractor of normalized sums.*

> **Connection — the spine of all inference**
>
> Density = area → z-scores standardize → the CLT makes $\bar X$ Normal → so confidence intervals and z/t-tests in the Statistics guide are statements about areas under a bell curve. This theorem is why Normal-based inference works on skewed, real data.

<a id="s18"></a>
### A glimpse beyond: measure-theoretic probability & martingales

*Where the rigorous story leads next — the measure-theoretic foundation, and the dynamic theory of processes that evolve fairly in time.*

> **Concept — probability as measure theory**
>
> The fully rigorous setting treats $P$ as a **measure** on a $\sigma$-algebra $\mathcal F$, and expectation as the **Lebesgue integral** $E[X]=\int_\Omega X\,dP$. This unifies the discrete sum and the continuous integral into one operation, and lets us handle variables that are neither — mixtures, conditional expectations given a $\sigma$-algebra, and limits that the elementary theory cannot reach.

**The pillars of the rigorous theory**

***Monotone & dominated convergence** justify swapping limits with expectations. **Fubini–Tonelli** justifies swapping the order of integration we used in the tower property and tail-sum proofs. **Radon–Nikodym** defines densities and conditional expectation in full generality. These theorems make every "swap the order" step in this guide legitimate.*

**Martingales**

$$E\big[X_{n+1}\mid X_1,\dots,X_n\big]=X_n\quad(\text{martingale})$$

*A martingale is a model of a fair game: the best forecast of tomorrow's value, given all of today's information, is today's value. Built directly on the conditional expectation of Section 12.*

> **Principle — why martingales matter**
>
> The **optional stopping theorem** says a martingale's expectation is unchanged by a fair stopping rule (no gambling system beats a fair game), and **martingale convergence** guarantees bounded martingales settle to a limit. These tools generalize the laws of large numbers to dependent sequences and underlie stochastic calculus, Brownian motion, and the mathematics of finance.

> **Connection — the road onward**
>
> From here the paths branch: **stochastic processes** (Markov chains, Poisson processes, Brownian motion), **statistical inference** (the companion guide, where these distributions become estimators and tests), and **information theory** (entropy as expected surprise). All of them stand on the foundation built in this guide: a measure, random variables, their moments, and the limit theorems that tame randomness in the aggregate.

---

*A rigorous first course in probability theory — axioms, random variables, transforms, and the limit theorems behind statistical inference — built as a companion to the Complete Statistics guide. Read once for the architecture; return to any box as a reference. Remember: probability runs population → sample; statistics inverts it.*
