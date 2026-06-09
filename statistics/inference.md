**English** · [中文](inference.zh.md)

# Inference, *from data to truth.*

A rigorous course in mathematical statistics — how a random sample is turned into estimates, intervals, tests, and posterior beliefs about unknown parameters. Every principle is given as a precise definition and every key theorem is **demonstrated**, with the threads to probability and calculus made explicit. This expanded edition assumes **no prior mathematical background**: every symbol is defined in words the first time it appears, every derivation is a numbered list in which each step states *what* is done and *why* it is allowed, and every result is followed by a fully worked numeric example.

[← Back to all guides](../README.md)

## Part A · Foundations

<a id="s0"></a>
### The big picture: from data to conclusions

*Probability describes a known mechanism producing random data. Inference reverses the arrow: given the data, what was the mechanism?*

#### What this section is about, in plain words

Imagine a factory that stamps out coins. You do not know whether the coins are fair. You flip one coin 100 times and see 58 heads. The question "what is the true chance of heads for this coin?" is a question of **statistical inference**: you have *data* (58 heads out of 100) and you want to recover a *fact about the mechanism* (the true probability of heads). Probability theory would go the other way — it would start from "the coin lands heads with probability 0.5" and predict how many heads you are likely to see. Inference runs that reasoning backwards.

#### Defining every term we will use

- **Data.** The numbers we actually observe. We write them $x_1, x_2, \dots, x_n$, where $n$ is the **sample size** (how many observations we have). Lower-case letters denote the specific numbers we saw.
- **Random variable.** A quantity whose value is determined by a random experiment before we look. We write random variables with capital letters: $X_1, X_2, \dots, X_n$. Once the experiment is run, $X_i$ "becomes" the observed number $x_i$.
- **Parameter.** An unknown fixed number (or list of numbers) describing the mechanism. We write it $\theta$ (the Greek letter "theta"). In the coin example $\theta$ is the true probability of heads.
- **Parameter space.** The set of all values $\theta$ is allowed to take, written $\Theta$ (capital theta). For a coin probability, $\Theta = [0,1]$, the interval of numbers from $0$ to $1$.
- **Probability density (or mass) function.** A function $f(x \mid \theta)$ that says how likely each data value $x$ is when the parameter equals $\theta$. The vertical bar "$\mid$" is read "given." For discrete data (counts) it gives a probability directly; for continuous data it gives a density whose area gives probabilities. (Density vs. mass is a distinction from the Probability guide; we use "density" loosely for both.)
- **Statistical model.** The whole family of candidate distributions, written $\{f(x\mid\theta): \theta\in\Theta\}$. The curly braces mean "the set of," and the colon is read "such that." So this is "the set of distributions $f(x\mid\theta)$ such that $\theta$ ranges over $\Theta$."

In **mathematical statistics** we posit such a statistical model. We observe data $X_1,\dots,X_n$ drawn from one (unknown) member of the family, and our job is to say what $\theta$ is. There are three classic deliverables.

- **Point estimation** — a single best guess $\hat\theta$ for $\theta$ (Part B). The "hat" $\hat{\,}$ over a symbol always means "an estimate of."
- **Interval estimation & testing** — a range of values for $\theta$ with a stated confidence, or a yes/no decision about a claim (Part C).
- **Prediction / belief updating** — and, in the Bayesian view, a full probability distribution for $\theta$ describing our remaining uncertainty (Part D).

> **Principle — the inferential inversion**
>
> Probability runs **parameter $\to$ data**: fix $\theta$, and $f(x\mid\theta)$ tells you how the data behaves. Inference runs **data $\to$ parameter**: fix the data, and ask which $\theta$ is plausible. The *likelihood function* (Section 3) is exactly $f(x\mid\theta)$ read in this reversed direction, and it is the hinge of the entire subject.

#### A tiny worked example to fix ideas

Suppose the model is "each flip is heads with unknown probability $\theta$." We flip $n=3$ times and observe heads, tails, heads, i.e. the data $x_1=1, x_2=0, x_3=1$ (coding heads as $1$, tails as $0$). The probability the model assigns to this exact sequence, if the true value were $\theta$, is

$$f(x_1,x_2,x_3\mid\theta)=\theta\cdot(1-\theta)\cdot\theta=\theta^2(1-\theta).$$

Reading this as a function of $\theta$ (data fixed) is inference's reversed direction. If $\theta=0.5$ it gives $0.125$; if $\theta=0.7$ it gives $0.147$; if $\theta=0.9$ it gives $0.081$. The value $\theta=0.7$ makes the observed data more probable than $0.5$ or $0.9$, which already hints that the "most likely" $\theta$ sits near two-thirds — exactly the fraction of heads we saw. Section 5 will make this precise.

#### The whole course on one line

> Model & likelihood → sufficiency → point estimators (MoM, MLE) → evaluate them (bias, MSE, Cramér–Rao, MVUE) → intervals & tests (pivots, Neyman–Pearson, LRT) → Bayes & the bootstrap

> **Connection — building on the intro Statistics guide**
>
> The intro guide introduced $\bar x$, $s^2$, confidence intervals and p-values operationally. This guide supplies the *why*: why divide by $n-1$, why $t$ appears, why $\bar X\pm 1.96\,\sigma/\sqrt n$ is correct, and what makes an estimator "good." It is the theory beneath the recipes.

#### Common pitfalls

- The parameter $\theta$ is **fixed but unknown**, not random (until Part D, where the Bayesian view deliberately treats it as random to encode belief). The randomness in Parts A–C lives in the *data*.
- An "estimate" like $\hat\theta=0.58$ is one number; the *rule* that produced it (Section 1) is the object we actually study.

<a id="s1"></a>
### Populations, samples & sampling distributions

*A statistic is a function of random data, so it is itself a random variable. Its distribution is the object every inference is built on.*

#### Plain-language orientation

We rarely measure an entire **population** (every coin the factory will ever make). Instead we take a **sample** — a handful of observations — and compute a summary number from it, like the average. Because the sample is random, that summary number is random too: a different sample would give a different average. The pattern of values the summary takes across all possible samples is its **sampling distribution**, and understanding that pattern is what lets us attach error bars and confidence to our conclusions.

#### Definitions

- **Population.** The complete collection of all possible observations, described by a true distribution $F$ (or density $f$).
- **Sample.** The observations we actually collect, $X_1,\dots,X_n$.
- **Independent.** Two random variables are independent if knowing one tells you nothing about the other; formally their joint density factors into the product of their separate densities.
- **Identically distributed.** All the $X_i$ follow the same distribution $f(x\mid\theta)$.

**Random sample (i.i.d.)**

$$X_1,\dots,X_n \ \text{i.i.d.}\ \sim f(x\mid\theta),\qquad \text{joint density } f(\mathbf x\mid\theta)=\prod_{i=1}^n f(x_i\mid\theta)$$

Here "$\sim$" is read "is distributed as." The bold $\mathbf x=(x_1,\dots,x_n)$ is the whole list of data. The symbol $\prod_{i=1}^n$ is a **product** over $i=1,2,\dots,n$ — the multiplication analogue of the summation sign $\sum$. So $\prod_{i=1}^n f(x_i\mid\theta)=f(x_1\mid\theta)\times f(x_2\mid\theta)\times\cdots\times f(x_n\mid\theta)$.

*"i.i.d." = independent and identically distributed. Independence is what turns the joint density into a single product — the structural fact that powers likelihood, sufficiency, and the Central Limit Theorem.*

**Why does independence give a product?** By the definition of independence, the joint density of independent variables equals the product of their individual densities. Because they are also identically distributed, every individual density is the *same* function $f(\cdot\mid\theta)$, just evaluated at a different data point. Multiplying these together gives $\prod_{i=1}^n f(x_i\mid\theta)$.

> **Concept — statistic vs estimator vs estimate**
>
> A **statistic** $T=T(X_1,\dots,X_n)$ is any function of the sample that does not depend on the unknown $\theta$ (you must be able to compute it from data alone). An **estimator** is a statistic used to guess a parameter, e.g. $\hat\theta=\bar X$; it is random. Its realized value on observed data, $\hat\theta=4.2$, is an **estimate**. The distribution of an estimator across all possible samples is its **sampling distribution**.

Here $\bar X$ (read "X-bar") denotes the **sample mean**, defined as $\bar X = \frac1n\sum_{i=1}^n X_i$ — add up all the observations and divide by how many there are.

**Mean and variance of the sample mean**

$$E[\bar X]=\mu,\qquad \operatorname{Var}(\bar X)=\frac{\sigma^2}{n},\qquad \text{SE}(\bar X)=\frac{\sigma}{\sqrt n}$$

New symbols: $E[\,\cdot\,]$ is the **expected value** (the long-run average of a random quantity); $\mu$ (the Greek "mu") is the population mean $E[X]$; $\operatorname{Var}$ is the **variance** (the average squared distance from the mean, a measure of spread); $\sigma^2$ (sigma-squared) is the population variance $\operatorname{Var}(X)$; $\sigma$ is the **standard deviation** (the square root of the variance); and SE is the **standard error**, the standard deviation of the *estimator*.

**Demonstration — mean and variance of $\bar X$, every step justified**

1. By definition $\bar X=\frac1n\sum_{i=1}^n X_i$.
2. Apply **linearity of expectation** (the expected value of a sum is the sum of the expected values, and a constant factor pulls out): $E[\bar X]=\frac1n\sum_{i=1}^n E[X_i]$.
3. Each $X_i$ is identically distributed with mean $\mu$, so $E[X_i]=\mu$ for every $i$. Summing $n$ copies of $\mu$ gives $\frac1n\cdot n\mu=\mu$. Hence $E[\bar X]=\mu$.
4. For the variance, use the rule that for **independent** variables the variance of a sum is the sum of the variances, and a constant factor $c$ comes out squared: $\operatorname{Var}(cY)=c^2\operatorname{Var}(Y)$. With $c=\frac1n$,

   $$\operatorname{Var}(\bar X)=\operatorname{Var}\!\Big(\tfrac1n\sum_{i=1}^n X_i\Big)=\tfrac{1}{n^2}\sum_{i=1}^n \operatorname{Var}(X_i).$$
5. Each $\operatorname{Var}(X_i)=\sigma^2$, and summing $n$ copies gives $\frac{1}{n^2}\cdot n\sigma^2=\frac{\sigma^2}{n}$. Taking the square root gives the standard error $\sigma/\sqrt n$.

*The estimator $\bar X$ is centered on the truth ($E[\bar X]=\mu$) and gets tighter as $n$ grows (the variance shrinks like $1/n$) — the seed of consistency (Section 6).*

**Worked numeric example.** Suppose a population has mean $\mu=10$ and standard deviation $\sigma=4$. Take a sample of size $n=16$. Then $E[\bar X]=10$ and $\operatorname{Var}(\bar X)=\frac{4^2}{16}=\frac{16}{16}=1$, so $\text{SE}(\bar X)=\sqrt 1=1$. Quadrupling the sample size to $n=64$ would give $\text{SE}=4/\sqrt{64}=4/8=0.5$ — to halve the error you must quadruple the data.

**Demonstration — sampling distribution of $\bar X$ for a normal sample**

1. Let $X_i\ \text{i.i.d.}\ \sim N(\mu,\sigma^2)$. The notation $N(\mu,\sigma^2)$ means the **normal** (bell-curve) distribution with mean $\mu$ and variance $\sigma^2$. A standard fact from probability is that any linear combination of independent normal variables is again normal. Since $\bar X$ is a linear combination ($\frac1n$ times a sum), $\bar X$ is normal.
2. Its mean and variance were computed above: $E[\bar X]=\mu$, $\operatorname{Var}(\bar X)=\sigma^2/n$. A normal distribution is completely determined by its mean and variance, so

   $$\bar X\sim N\!\left(\mu,\ \frac{\sigma^2}{n}\right),\qquad Z=\frac{\bar X-\mu}{\sigma/\sqrt n}\sim N(0,1).$$
3. The transformation in step 2, subtracting the mean and dividing by the standard deviation, is called **standardizing**; it turns any normal into the **standard normal** $N(0,1)$ (mean $0$, variance $1$). We verify: $E[Z]=\frac{E[\bar X]-\mu}{\sigma/\sqrt n}=0$ and $\operatorname{Var}(Z)=\frac{\operatorname{Var}(\bar X)}{\sigma^2/n}=1$.
4. For a non-normal population the **Central Limit Theorem (CLT)** gives the same limiting form: $Z\xrightarrow{d}N(0,1)$ as $n\to\infty$. The arrow $\xrightarrow{d}$ means "converges in distribution" — for large $n$ the distribution of $Z$ is approximately standard normal regardless of the population's shape.

*Exact for normals, asymptotic in general — this single distribution underwrites the $z$- and $t$-intervals of Part C.*

> **Connection — the Probability guide (CLT & MGFs)**
>
> That $\bar X$ is normal for normal data, and asymptotically normal otherwise, is the CLT proved there via moment generating functions (MGFs). Sampling distributions are just transformations of random variables; the algebra of $E$, $\operatorname{Var}$, and MGFs from probability is the toolkit.

#### Common pitfalls

- The standard *deviation* $\sigma$ measures spread in the population; the standard *error* $\sigma/\sqrt n$ measures spread of the estimator. They differ by the factor $\sqrt n$.
- "$\bar X$ is normal" is *exact* only for normal data; for other populations it is an approximation that improves with $n$.

<a id="s2"></a>
### Statistics, sufficiency & the factorization theorem

*Some statistics squeeze every drop of information about $\theta$ out of the data. These sufficient statistics let us compress the sample without losing anything.*

#### Plain-language orientation

If you flip a coin 100 times, do you really need the exact order of heads and tails to estimate the coin's bias? Intuitively no — only the *total count* of heads matters. A **sufficient statistic** is a precise version of this intuition: a summary of the data that retains all the information about $\theta$, so that once you know it, the leftover detail in the data is irrelevant noise.

#### Definitions

- **Conditional distribution.** The distribution of one quantity once another is held fixed. "The distribution of the data given $T=t$" describes what data patterns are possible once we are told the summary equals $t$.
- A statistic $T$ does *not* depend on $\theta$, so it is computable from data alone (recall Section 1).

> **Concept — sufficiency**
>
> A statistic $T$ is **sufficient** for $\theta$ if the conditional distribution of the data given $T$ does not depend on $\theta$. Intuitively: once you know $T$, the rest of the sample is "noise" carrying no further information about $\theta$. For a normal sample, $(\sum X_i,\sum X_i^2)$ is sufficient — the individual order of the data is irrelevant.

**Fisher–Neyman factorization theorem**

$$T \text{ is sufficient for }\theta \iff f(\mathbf x\mid\theta)=g\big(T(\mathbf x),\theta\big)\,h(\mathbf x)$$

The symbol "$\iff$" means "if and only if" (the statements on each side are equivalent). The theorem says: $T$ is sufficient exactly when the joint density splits into a product of two pieces — a piece $g$ that involves $\theta$ but touches the data only through the summary $T(\mathbf x)$, times a piece $h(\mathbf x)$ that involves the data but not $\theta$ at all.

*To find a sufficient statistic, write out the joint density and isolate where $\theta$ and the data meet; whatever function of the data $\theta$ "talks to" is the sufficient statistic $T$.*

**Why the factorization implies sufficiency (intuition with justification).** If the density factors as $g(T,\theta)h(\mathbf x)$, then for two data sets with the *same* value of $T$, the dependence on $\theta$ (the factor $g$) is identical; they differ only through $h$, which carries no $\theta$. Dividing the joint density by the density of $T$ to form the conditional distribution, the $\theta$-bearing factor cancels, leaving something free of $\theta$ — which is the definition of sufficiency.

**Demonstration — a sufficient statistic for Bernoulli $p$ via factorization**

A **Bernoulli($p$)** random variable equals $1$ ("success") with probability $p$ and $0$ ("failure") with probability $1-p$. Its mass function can be written compactly as $f(x\mid p)=p^x(1-p)^{1-x}$ for $x\in\{0,1\}$: plug in $x=1$ to get $p$, and $x=0$ to get $1-p$.

1. For $X_i\ \text{i.i.d.}\ \sim\text{Bernoulli}(p)$, multiply the individual mass functions (independence, Section 1):

   $$f(\mathbf x\mid p)=\prod_{i=1}^n p^{x_i}(1-p)^{1-x_i}.$$
2. Use the exponent rule $a^{b}a^{c}=a^{b+c}$ to combine the powers: the $p$ factors give $p^{\sum x_i}$ and the $(1-p)$ factors give $(1-p)^{\sum(1-x_i)}=(1-p)^{n-\sum x_i}$ (since $\sum_{i=1}^n 1 = n$). Thus

   $$f(\mathbf x\mid p)=p^{\sum x_i}(1-p)^{\,n-\sum x_i}.$$
3. This depends on the data only through $T=\sum_{i=1}^n x_i$, the total number of successes. Set $g(T,p)=p^{T}(1-p)^{n-T}$ and $h(\mathbf x)=1$.
4. By the factorization theorem, $T=\sum X_i$ (equivalently $\bar X=T/n$) is sufficient for $p$.

*Knowing the total number of successes is as good as knowing the full sequence of $0$s and $1$s.*

**Worked numeric example.** With $n=5$ flips and data $1,0,1,1,0$, we have $T=\sum x_i=3$. The factorization tells us that *any* other sequence with three heads — say $1,1,1,0,0$ — carries exactly the same information about $p$. Both give the density $p^3(1-p)^2$.

> **Principle — minimal sufficiency & completeness**
>
> A **minimal** sufficient statistic is the coarsest sufficient summary — a function of every other sufficient statistic, so it compresses as much as possible without losing information. A statistic $T$ is **complete** if the only function $\varphi$ with $E_\theta[\varphi(T)]=0$ for all $\theta$ is the function that is zero everywhere. Completeness is the technical ingredient that makes the Rao–Blackwell estimator (Section 8) the *unique* best one: it forbids two different unbiased functions of $T$ from existing.

> **Connection — the exponential family**
>
> Many distributions (normal, Bernoulli, Poisson, exponential, gamma) belong to the **exponential family** $f(x\mid\theta)=h(x)\exp\{\eta(\theta)T(x)-A(\theta)\}$, where $\exp\{\cdot\}$ is the exponential function $e^{(\cdot)}$. Factorization is then immediate (the $\exp\{\eta(\theta)\sum T(x_i)\}$ piece is $g$, and $\prod h(x_i)$ is $h$), and $\sum T(X_i)$ is automatically a complete sufficient statistic — a unifying thread through estimation theory.

#### Common pitfall

- A sufficient statistic is sufficient *for a particular model*. The total $\sum X_i$ is sufficient for Bernoulli $p$, but it would not capture everything for a model where the order of outcomes mattered.

<a id="s3"></a>
### The likelihood function

*Flip the joint density around: treat the data as fixed and $\theta$ as the variable. That re-reading is the likelihood, and almost everything follows from it.*

#### Plain-language orientation

The joint density $f(\mathbf x\mid\theta)$ is, before we collect data, a recipe for how data behaves at a known $\theta$. After we collect data, the numbers $\mathbf x$ are frozen, and only $\theta$ is unknown. The **likelihood** is the very same formula, now viewed as a function of $\theta$. It answers: "for each candidate $\theta$, how well does it explain the data I actually saw?"

**Likelihood and log-likelihood**

$$L(\theta)=f(\mathbf x\mid\theta)=\prod_{i=1}^n f(x_i\mid\theta),\qquad \ell(\theta)=\log L(\theta)=\sum_{i=1}^n \log f(x_i\mid\theta)$$

New symbols: $L(\theta)$ is the **likelihood**; $\ell(\theta)$ (script-ell) is the **log-likelihood**, the natural logarithm of $L$. The natural logarithm $\log$ (base $e\approx 2.718$) is the inverse of the exponential. We use the key logarithm law $\log(ab)=\log a+\log b$: the logarithm of a product is the sum of the logarithms. That law is exactly why the product in $L$ becomes a *sum* in $\ell$, which is far easier to differentiate.

*$L(\theta)$ is **not** a probability distribution over $\theta$; it need not integrate to one. It only *ranks* values of $\theta$ by how well they explain the observed data.*

> **Principle — the likelihood principle**
>
> All the information the data carry about $\theta$ is contained in the likelihood function. Two experiments yielding proportional likelihoods (one a constant multiple of the other) should lead to the same inference about $\theta$. Taking the log turns the product into a sum, which is why the **score function** $\ell'(\theta)$ and Fisher information (Section 7) are additive over independent observations.

**The score function**

$$U(\theta)=\frac{\partial}{\partial\theta}\ell(\theta)=\sum_{i=1}^n \frac{\partial}{\partial\theta}\log f(x_i\mid\theta),\qquad E_\theta[U(\theta)]=0$$

New symbols: $\frac{\partial}{\partial\theta}$ is the **partial derivative** with respect to $\theta$ — the rate of change of the function as $\theta$ varies (when there is only one variable it is just the ordinary derivative). $U(\theta)$ is the **score**: the slope of the log-likelihood. The subscript on $E_\theta$ reminds us the average is taken assuming $\theta$ is the true value.

*The score has mean zero at the true $\theta$. Setting the score to zero locates a peak of the likelihood — pure calculus optimization.*

**Demonstration — the score has expectation zero**

1. Start from the fact that a density integrates to one: $\int f(x\mid\theta)\,dx=1$ for **every** $\theta$. (The integral sign $\int\cdots dx$ means "total area under the curve," which for a probability density is always $1$.)
2. Differentiate both sides with respect to $\theta$. The right side is the constant $1$, whose derivative is $0$. On the left, a **regularity condition** (smoothness of $f$ that lets us swap the order of differentiation and integration) permits moving the derivative inside the integral:

   $$\int \frac{\partial}{\partial\theta} f(x\mid\theta)\,dx=0.$$
3. Use the **log-derivative identity** $\frac{\partial}{\partial\theta}\log f = \frac{1}{f}\frac{\partial}{\partial\theta} f$, which follows from the chain rule for $\log$. Rearranged, it says $\frac{\partial}{\partial\theta} f = f\cdot\frac{\partial}{\partial\theta}\log f$. Substitute into step 2:

   $$\int \Big(\frac{\partial}{\partial\theta}\log f(x\mid\theta)\Big) f(x\mid\theta)\,dx=0.$$
4. By the definition of expectation, $\int g(x) f(x\mid\theta)\,dx = E_\theta[g(X)]$. With $g=\frac{\partial}{\partial\theta}\log f$, the left side is exactly $E_\theta\!\big[\frac{\partial}{\partial\theta}\log f(X\mid\theta)\big]=E_\theta[U(\theta)]$. Therefore $E_\theta[U(\theta)]=0$.

*This little lemma is the workhorse behind both the MLE's consistency and the Cramér–Rao bound.*

**Worked numeric example (Bernoulli score).** For one Bernoulli observation, $\log f(x\mid p)=x\log p+(1-x)\log(1-p)$. Differentiating in $p$ gives the score $\frac{\partial}{\partial p}\log f=\frac{x}{p}-\frac{1-x}{1-p}$. Check the mean-zero claim by averaging over $X$ (which is $1$ with probability $p$ and $0$ with probability $1-p$):

$$E_p\Big[\tfrac{X}{p}-\tfrac{1-X}{1-p}\Big]=\frac{p}{p}-\frac{1-p}{1-p}=1-1=0.\ \checkmark$$

> **Connection — calculus: optimization is setting the score to zero**
>
> Maximizing $\ell(\theta)$ is the calculus problem "find the critical point": solve $\ell'(\theta)=0$ and check that the second derivative is negative, $\ell''(\theta)\lt 0$, confirming a peak rather than a valley. The negative second derivative $-\ell''$ measures how sharply the likelihood peaks — and that curvature *is* the observed Fisher information (Section 7).

## Part B · Point estimation

<a id="s4"></a>
### The method of moments

*The oldest recipe for an estimator: match the theoretical moments of the model to the empirical moments of the data, then solve.*

#### Plain-language orientation

A **moment** is an average of a power of the data. The first moment is just the mean; the second moment is the average of the squares; and so on. The model predicts these averages as formulas in $\theta$. The **method of moments** simply says: set the model's predicted average equal to the average you actually measured, and solve for $\theta$. It is the most direct estimator imaginable.

#### Definitions

- **Theoretical (population) $k$-th moment:** $\mu_k(\theta)=E_\theta[X^k]$, the expected value of the $k$-th power, computed from the model.
- **Empirical (sample) $k$-th moment:** $m_k=\frac1n\sum_{i=1}^n X_i^k$, the average of the $k$-th powers of the data.

**Method of moments (MoM)**

$$\text{set } \mu_k(\theta)=E_\theta[X^k] \ \text{equal to}\ m_k=\frac1n\sum_{i=1}^n X_i^k,\quad k=1,2,\dots$$

*Use as many moment equations as there are unknown parameters, then solve for $\theta$. Simple, always available, but rarely optimal.*

**Demonstration — MoM estimators for Poisson, Bernoulli & normal**

1. **Poisson($\lambda$).** The Poisson distribution counts rare events and has the property $E[X]=\lambda$ (its single parameter is also its mean). Matching the first theoretical moment $\lambda$ to the first empirical moment $\bar X$ gives one equation, $\lambda=\bar X$, so $\hat\lambda_{\text{MoM}}=\bar X$.
2. **Bernoulli($p$).** Here $E[X]=p$. Matching to $\bar X$ gives $\hat p_{\text{MoM}}=\bar X$ — the sample proportion of successes.
3. **Normal($\mu,\sigma^2$).** Two unknowns, so we need two equations. The first moment $E[X]=\mu$ matched to $\bar X$ gives $\hat\mu=\bar X$. The second moment is $E[X^2]=\operatorname{Var}(X)+(E[X])^2=\sigma^2+\mu^2$ (using the identity $\operatorname{Var}(X)=E[X^2]-(E[X])^2$ rearranged). Match it to $\frac1n\sum X_i^2$:

   $$\sigma^2+\mu^2=\frac1n\sum_{i=1}^n X_i^2 \ \Rightarrow\ \hat\sigma^2_{\text{MoM}}=\frac1n\sum_{i=1}^n X_i^2-\hat\mu^2=\frac1n\sum_{i=1}^n X_i^2-\bar X^2.$$
4. Finally, the algebraic identity $\frac1n\sum X_i^2-\bar X^2=\frac1n\sum (X_i-\bar X)^2$ (proved by expanding the right side: $\frac1n\sum(X_i^2-2X_i\bar X+\bar X^2)=\frac1n\sum X_i^2-2\bar X\cdot\bar X+\bar X^2=\frac1n\sum X_i^2-\bar X^2$) lets us write

   $$\hat\sigma^2_{\text{MoM}}=\frac1n\sum_{i=1}^n (X_i-\bar X)^2.$$

*Note the divisor is $n$, not $n-1$: the MoM variance is biased downward (see Section 6).*

**Worked numeric example (Poisson).** A call center logs the number of calls in each of $n=5$ minutes: $2, 4, 3, 5, 6$. Then $\bar X=(2+4+3+5+6)/5=20/5=4$, so $\hat\lambda_{\text{MoM}}=4$ calls per minute.

**Worked numeric example (normal variance).** For data $2,4,6$, the mean is $\bar X=4$. Squared deviations: $(2-4)^2=4$, $(4-4)^2=0$, $(6-4)^2=4$, summing to $8$. Then $\hat\sigma^2_{\text{MoM}}=8/3\approx 2.667$ (dividing by $n=3$), whereas the unbiased version would divide by $n-1=2$ giving $4$.

> **Principle — when to reach for MoM**
>
> MoM shines when the likelihood is awkward to maximize or as a starting value for iterative MLE. It is consistent under mild conditions (its estimates approach the truth as $n$ grows) but generally less efficient than the MLE: it ignores the full shape of the likelihood, using only a few moments.

<a id="s5"></a>
### Maximum likelihood estimation

*Pick the parameter value that makes the observed data most probable. The MLE is the dominant estimator in modern statistics.*

#### Plain-language orientation

Among all candidate values of $\theta$, the **maximum likelihood estimate** is the one under which the data we saw would have been most probable. It is the single $\theta$ that "best explains" the observations. Because the likelihood is a product (hard to differentiate) and the log-likelihood is a sum (easy), we maximize the log; since $\log$ only ever increases, the location of the peak is the same either way.

**The maximum likelihood estimator**

$$\hat\theta_{\text{MLE}}=\arg\max_{\theta\in\Theta} L(\theta)=\arg\max_{\theta\in\Theta} \ell(\theta),\qquad \text{solve } U(\theta)=\ell'(\theta)=0$$

The operator $\arg\max_{\theta} $ means "the value of $\theta$ at which the following expression is largest" (as opposed to $\max$, which would be the largest value itself).

*Maximizing $\ell$ is equivalent to maximizing $L$ (because $\log$ is an increasing function, so it preserves the location of the maximum), but turns products into sums. Confirm a maximum with $\ell''(\hat\theta)\lt 0$.*

**Why maximizing $\ell$ and $L$ give the same answer.** If $\log$ is strictly increasing, then $L(\theta_1)>L(\theta_2)$ holds if and only if $\log L(\theta_1)>\log L(\theta_2)$. So the ordering of $\theta$ values by $L$ is identical to their ordering by $\ell$, and in particular the top-ranked $\theta$ is the same.

**Demonstration — MLE for Bernoulli $p$**

1. From Section 2, $L(p)=p^{\sum x_i}(1-p)^{n-\sum x_i}$. Take logs using $\log(ab)=\log a+\log b$ and $\log(a^c)=c\log a$:

   $$\ell(p)=\Big(\sum x_i\Big)\log p+\Big(n-\sum x_i\Big)\log(1-p).$$
2. Differentiate term by term. Recall $\frac{d}{dp}\log p=\frac1p$ and, by the chain rule, $\frac{d}{dp}\log(1-p)=\frac{-1}{1-p}$. Set the score to zero:

   $$\ell'(p)=\frac{\sum x_i}{p}-\frac{n-\sum x_i}{1-p}=0.$$
3. Multiply through by $p(1-p)$ (allowed since $0<p<1$ makes it nonzero): $(1-p)\sum x_i-p(n-\sum x_i)=0$. Expand: $\sum x_i - p\sum x_i - pn + p\sum x_i=0$, i.e. $\sum x_i - pn=0$. Solve:

   $$\hat p_{\text{MLE}}=\frac{1}{n}\sum_{i=1}^n x_i=\bar X.$$
4. Check it is a maximum: $\ell''(p)=-\frac{\sum x_i}{p^2}-\frac{n-\sum x_i}{(1-p)^2}<0$ everywhere, so the critical point is a peak.

*Here MLE and MoM coincide; in general they differ.*

**Worked numeric example.** Flip a coin $n=10$ times, observe $7$ heads. Then $\hat p_{\text{MLE}}=7/10=0.7$. The data are most probable under a $0.7$-heads coin.

**Demonstration — MLE for normal $(\mu,\sigma^2)$**

1. The normal density is $f(x\mid\mu,\sigma^2)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\!\big(-\frac{(x-\mu)^2}{2\sigma^2}\big)$. Taking logs of the product over $i$ (and using $\log\exp(u)=u$),

   $$\ell(\mu,\sigma^2)=-\frac n2\log(2\pi)-\frac n2\log\sigma^2-\frac{1}{2\sigma^2}\sum_{i=1}^n(x_i-\mu)^2.$$
2. Partial derivative in $\mu$ (only the last term depends on $\mu$; chain rule on the square): $\partial\ell/\partial\mu=\frac{1}{\sigma^2}\sum(x_i-\mu)$. Set to zero: $\sum(x_i-\mu)=0\Rightarrow \sum x_i = n\mu\Rightarrow \hat\mu=\bar X$.
3. Partial derivative in $\sigma^2$ (treat $\sigma^2$ as a single variable $v$; $\frac{d}{dv}\log v=\frac1v$ and $\frac{d}{dv}(1/v)=-1/v^2$): $\partial\ell/\partial\sigma^2=-\frac{n}{2\sigma^2}+\frac{1}{2\sigma^4}\sum(x_i-\mu)^2$. Set to zero and substitute $\mu=\hat\mu=\bar X$:

   $$\frac{1}{2\sigma^4}\sum(x_i-\bar X)^2=\frac{n}{2\sigma^2}\ \Rightarrow\ \hat\sigma^2_{\text{MLE}}=\frac1n\sum_{i=1}^n (x_i-\bar X)^2.$$
4. **Confirm it is the maximizer.** As $\mu\to\pm\infty$ or $\sigma^2\to 0^+$ or $\sigma^2\to\infty$, the term $-\frac n2\log\sigma^2-\frac1{2\sigma^2}\sum(x_i-\mu)^2$ drives $\ell\to-\infty$; since $\ell$ is smooth on the open region $\{\sigma^2>0\}$ and tends to $-\infty$ at every boundary, its interior critical point — being unique — must be the global maximum (formally, the Hessian is negative definite there, e.g. $\partial^2\ell/\partial\mu^2=-n/\sigma^2<0$).

*Again the divisor is $n$. The MLE of the variance is biased — quantified next section.*

**Worked numeric example.** For data $2,4,6$: $\hat\mu=\bar X=4$, and (from the Section 4 example) $\hat\sigma^2_{\text{MLE}}=8/3\approx 2.667$.

> **Principle — why the MLE is so prized**
>
> Under regularity conditions the MLE is **consistent** (homes in on the true $\theta$), **asymptotically normal** (its sampling distribution becomes a bell curve), and **asymptotically efficient** — it attains the Cramér–Rao bound in the limit (Section 7). It is also **invariant**: the MLE of any function $g(\theta)$ is simply $g(\hat\theta_{\text{MLE}})$. Its single weakness is finite-sample bias.

**Asymptotic normality of the MLE**

$$\sqrt n\,(\hat\theta_{\text{MLE}}-\theta)\ \xrightarrow{d}\ N\!\Big(0,\ \frac{1}{I_1(\theta)}\Big)$$

*$I_1(\theta)$ is the Fisher information in one observation (Section 7). This statement is the engine of Wald intervals and tests: for large $n$, $\hat\theta_{\text{MLE}}$ is approximately $N(\theta,\,1/(nI_1(\theta)))$.*

> **Connection — calculus optimization, applied to data**
>
> Finding $\hat\theta_{\text{MLE}}$ is the same "set the derivative to zero, check the second derivative" routine from calculus, now applied to $\ell(\theta)$. When no closed form exists, numerical methods (Newton–Raphson, which uses $\ell''$) take over — and $\ell''$ is again the information.

<a id="s6"></a>
### Evaluating estimators: bias, variance, MSE & consistency

*An estimator is a random variable; we judge it by where it centers, how much it scatters, and whether it homes in on the truth as data accumulate.*

#### Plain-language orientation

Two darts players: one whose throws cluster tightly but all to the left of the bullseye (low scatter, but a systematic offset), and one whose throws center on the bullseye but spread widely (no offset, but high scatter). **Bias** measures the systematic offset; **variance** measures the scatter; **mean squared error (MSE)** combines both into a single score. A good estimator keeps the total small.

**Bias, variance and mean squared error**

$$\operatorname{Bias}(\hat\theta)=E[\hat\theta]-\theta,\qquad \operatorname{MSE}(\hat\theta)=E\big[(\hat\theta-\theta)^2\big]$$

$$\operatorname{MSE}(\hat\theta)=\operatorname{Var}(\hat\theta)+\big[\operatorname{Bias}(\hat\theta)\big]^2$$

In words: the bias is how far the estimator's average lands from the truth; the MSE is the average squared miss; and the MSE splits exactly into scatter plus offset-squared.

*An estimator is **unbiased** when $E[\hat\theta]=\theta$ (zero bias). MSE trades off scatter against systematic offset — sometimes a little bias buys a lot less variance.*

**Demonstration — the bias–variance decomposition of MSE**

1. Add and subtract the estimator's own mean $E[\hat\theta]$ inside the error: $(\hat\theta-\theta)=(\hat\theta-E[\hat\theta])+(E[\hat\theta]-\theta)$. This is legal because we add and subtract the same quantity, a net change of zero.
2. Square both sides using $(a+b)^2=a^2+2ab+b^2$, then take expectations (linearity of $E$ from Section 1):

   $$E[(\hat\theta-\theta)^2]=E[(\hat\theta-E\hat\theta)^2]+2(E\hat\theta-\theta)\,E[\hat\theta-E\hat\theta]+(E\hat\theta-\theta)^2.$$

   Here $(E\hat\theta-\theta)$ is a constant, so it pulls out of the expectation in the cross term.
3. The cross term vanishes because $E[\hat\theta-E\hat\theta]=E[\hat\theta]-E[\hat\theta]=0$ (the mean of a deviation from the mean is zero).
4. What remains is $E[(\hat\theta-E\hat\theta)^2]$, which is the **definition of variance** $\operatorname{Var}(\hat\theta)$, plus $(E\hat\theta-\theta)^2$, which is $\operatorname{Bias}(\hat\theta)^2$. Hence $\operatorname{MSE}=\operatorname{Var}+\operatorname{Bias}^2$.

*The same "add and subtract the mean" move underlies the identity $\operatorname{Var}(X)=E[X^2]-(E[X])^2$.*

**Demonstration — the MLE of normal variance is biased, with its MSE**

1. Recall from Section 5 that $\hat\sigma^2_{\text{MLE}}=\frac1n\sum(X_i-\bar X)^2$. Define the **unbiased sample variance** $S^2=\frac{1}{n-1}\sum(X_i-\bar X)^2$. Comparing the two, $\hat\sigma^2_{\text{MLE}}=\frac{n-1}{n}S^2$ (because $\frac{1}{n}=\frac{n-1}{n}\cdot\frac{1}{n-1}$).
2. A key sampling fact for normal data (proved in the Probability guide): $\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}$, where $\chi^2_{n-1}$ is the **chi-squared distribution with $n-1$ degrees of freedom** — the distribution of a sum of $n-1$ squared independent standard normals, with mean $n-1$ and variance $2(n-1)$. From this, $E[S^2]=\sigma^2$ (so $S^2$ is unbiased) and $\operatorname{Var}(S^2)=\frac{2\sigma^4}{n-1}$ (rescaling: $\operatorname{Var}(S^2)=(\frac{\sigma^2}{n-1})^2\operatorname{Var}(\chi^2_{n-1})=\frac{\sigma^4}{(n-1)^2}\cdot 2(n-1)=\frac{2\sigma^4}{n-1}$).
3. Take expectations of step 1: $E[\hat\sigma^2_{\text{MLE}}]=\frac{n-1}{n}E[S^2]=\frac{n-1}{n}\sigma^2$. Hence

   $$\operatorname{Bias}=\frac{n-1}{n}\sigma^2-\sigma^2=-\frac{\sigma^2}{n}.$$

   The bias is negative: the MLE *under*-estimates the variance on average.
4. Variance: $\operatorname{Var}(\hat\sigma^2_{\text{MLE}})=\big(\tfrac{n-1}{n}\big)^2\operatorname{Var}(S^2)=\big(\tfrac{n-1}{n}\big)^2\frac{2\sigma^4}{n-1}=\frac{2(n-1)\sigma^4}{n^2}$. Add the bias squared $\big(\frac{\sigma^2}{n}\big)^2=\frac{\sigma^4}{n^2}$:

   $$\operatorname{MSE}(\hat\sigma^2_{\text{MLE}})=\frac{2(n-1)\sigma^4}{n^2}+\frac{\sigma^4}{n^2}=\frac{(2n-1)\,\sigma^4}{n^2}.$$

*Strikingly, $\hat\sigma^2_{\text{MLE}}$ has **smaller** MSE than the unbiased $S^2$ (whose MSE is its variance, $2\sigma^4/(n-1)$): a textbook case where accepting a little bias lowers the total error.*

**Worked numeric example.** Let $\sigma^2=1$ and $n=5$. Then $\operatorname{MSE}(S^2)=\frac{2}{4}=0.5$, while $\operatorname{MSE}(\hat\sigma^2_{\text{MLE}})=\frac{2\cdot5-1}{25}=\frac{9}{25}=0.36$. The biased MLE wins on MSE here.

> **Principle — consistency**
>
> An estimator is **consistent** if $\hat\theta_n\xrightarrow{p}\theta$ as $n\to\infty$ (the arrow $\xrightarrow{p}$ means "converges in probability": for any tiny tolerance, the chance of missing $\theta$ by more than that tolerance goes to $0$). A sufficient condition is $\operatorname{MSE}(\hat\theta_n)\to 0$ (mean-square consistency), which forces convergence in probability via **Chebyshev's inequality** $P(|\hat\theta-\theta|\ge\varepsilon)\le \operatorname{MSE}/\varepsilon^2$. Both the biased and unbiased variance estimators are consistent, since their bias ($\sim 1/n$) and variance ($\sim 1/n$) each vanish — bias matters in small samples, not the limit.

> **Connection — the intro guide's $n-1$ finally explained**
>
> The intro guide simply asserted "divide by $n-1$ so that $E[S^2]=\sigma^2$." Here we see exactly why: the MLE divisor $n$ produces a bias of $-\sigma^2/n$, and the $n-1$ (Bessel) correction removes it. The "lost degree of freedom" is the $n-1$ in the $\chi^2_{n-1}$ above — estimating $\bar X$ from the same data uses up one degree of freedom.

<a id="s7"></a>
### Fisher information & the Cramér–Rao lower bound

*There is a hard floor on how precise any unbiased estimator can be. Fisher information measures how much a sample tells you about $\theta$; its reciprocal is that floor.*

#### Plain-language orientation

Some experiments are more informative than others. If the likelihood has a sharp, narrow peak, the data pin down $\theta$ tightly; if it is broad and flat, many values of $\theta$ explain the data nearly equally well. **Fisher information** quantifies this sharpness. The remarkable **Cramér–Rao bound** then says no unbiased estimator can have smaller variance than one over the information — there is a fundamental speed limit on precision.

**Fisher information**

$$I(\theta)=E\!\left[\Big(\frac{\partial}{\partial\theta}\log f(X\mid\theta)\Big)^2\right]=-\,E\!\left[\frac{\partial^2}{\partial\theta^2}\log f(X\mid\theta)\right]$$

$$I_n(\theta)=n\,I_1(\theta)\quad\text{(information adds over i.i.d. observations)}$$

The first expression is the **variance of the score** (its average squared value, since the score has mean zero by Section 3). The second, equal to it under regularity, is the **expected negative curvature** of the log-likelihood — the second derivative measures how the slope changes, i.e. how bent the curve is. The subscripts distinguish information in one observation ($I_1$) from information in the whole sample ($I_n$).

**Why information adds.** Because $\ell(\theta)=\sum_i \log f(x_i\mid\theta)$ is a sum (Section 3), its second derivative is the sum of the per-observation second derivatives. Taking $-E[\cdot]$ of each i.i.d. term gives the same $I_1(\theta)$, and summing $n$ of them gives $I_n(\theta)=nI_1(\theta)$.

**Demonstration — the two formulas for $I(\theta)$ agree**

1. Start from the mean-zero identity of Section 3, written as $\int (\partial_\theta\log f)\,f\,dx=0$ (abbreviating $\partial_\theta=\frac{\partial}{\partial\theta}$).
2. Differentiate this in $\theta$ (passing the derivative inside, by regularity), using the product rule on $(\partial_\theta\log f)\cdot f$:

   $$\int \big(\partial_\theta^2\log f\big) f\,dx + \int (\partial_\theta\log f)\,(\partial_\theta f)\,dx=0.$$
3. In the second integral substitute $\partial_\theta f = f\,\partial_\theta\log f$ (the log-derivative identity from Section 3), giving $\int (\partial_\theta\log f)^2 f\,dx$.
4. So $E[\partial_\theta^2\log f]+E[(\partial_\theta\log f)^2]=0$, i.e. $E[(\partial_\theta\log f)^2]=-E[\partial_\theta^2\log f]$, which is exactly the claimed equality.

*Information is the variance of the score, equivalently the expected curvature of the log-likelihood. A sharply peaked likelihood means high information means precise estimation.*

**Demonstration — Fisher information for Bernoulli $p$**

1. One observation: $\log f(x\mid p)=x\log p+(1-x)\log(1-p)$.
2. Score (first derivative, from Section 3): $\frac{\partial}{\partial p}\log f=\frac{x}{p}-\frac{1-x}{1-p}$. Second derivative (using $\frac{d}{dp}(1/p)=-1/p^2$ and the chain rule): $\frac{\partial^2}{\partial p^2}\log f=-\frac{x}{p^2}-\frac{1-x}{(1-p)^2}$.
3. Take $-E[\cdot]$, using $E[X]=p$ so $E[1-X]=1-p$:

   $$I_1(p)=\frac{E[X]}{p^2}+\frac{E[1-X]}{(1-p)^2}=\frac{p}{p^2}+\frac{1-p}{(1-p)^2}=\frac1p+\frac1{1-p}=\frac{1}{p(1-p)}.$$

   The last step combines fractions over the common denominator $p(1-p)$: $\frac{1}{p}+\frac{1}{1-p}=\frac{(1-p)+p}{p(1-p)}=\frac{1}{p(1-p)}$.

*So $I_n(p)=n/[p(1-p)]$ — the more extreme $p$ (near $0$ or $1$), the larger the information per trial.*

**Cramér–Rao lower bound (CRLB)**

$$\text{for any unbiased }\hat\theta:\qquad \operatorname{Var}(\hat\theta)\ \ge\ \frac{1}{I_n(\theta)}=\frac{1}{n\,I_1(\theta)}$$

*No unbiased estimator can beat this variance. An estimator that attains it is **efficient**; its **relative efficiency** is the ratio of the bound to its actual variance (a number between $0$ and $1$, with $1$ meaning fully efficient).*

**Demonstration — the Cramér–Rao bound**

1. Let $\hat\theta$ be unbiased and let $U=U(\theta)$ be the score, with $E[U]=0$ (Section 3) and $\operatorname{Var}(U)=I_n(\theta)$ (the definition of information as the score's variance).
2. We show $\operatorname{Cov}(\hat\theta,U)=1$. Start from unbiasedness $E[\hat\theta]=\int \hat\theta(\mathbf x) f(\mathbf x\mid\theta)\,d\mathbf x=\theta$. Differentiate in $\theta$ (regularity allows passing inside): $\int \hat\theta\,\partial_\theta f\,d\mathbf x=1$. Substitute $\partial_\theta f=f\,U$ (log-derivative identity): $\int \hat\theta\,U\,f\,d\mathbf x = E[\hat\theta U]=1$. Since $E[U]=0$, the covariance is $\operatorname{Cov}(\hat\theta,U)=E[\hat\theta U]-E[\hat\theta]E[U]=1-0=1$.
3. Apply the **Cauchy–Schwarz inequality** for covariances, $\operatorname{Cov}(A,B)^2\le\operatorname{Var}(A)\operatorname{Var}(B)$ (the covariance can never exceed the product of the spreads). With $A=\hat\theta$, $B=U$:

   $$1=\operatorname{Cov}(\hat\theta,U)^2\le \operatorname{Var}(\hat\theta)\,\operatorname{Var}(U)=\operatorname{Var}(\hat\theta)\,I_n(\theta).$$
4. Divide both sides by $I_n(\theta)>0$:

   $$\operatorname{Var}(\hat\theta)\ge\frac{1}{I_n(\theta)}.$$

*Illustration: for Bernoulli, $\hat p=\bar X$ has $\operatorname{Var}(\bar X)=\frac{p(1-p)}{n}$ (Section 1, since $\operatorname{Var}(X)=p(1-p)$ for a Bernoulli). The bound is $\frac{1}{I_n(p)}=\frac{p(1-p)}{n}$ — they are equal, so $\bar X$ attains the floor and is **efficient**.*

**Worked numeric example.** With $p=0.5$ and $n=100$, $I_n=\frac{100}{0.5\cdot0.5}=400$, so the CRLB is $1/400=0.0025$, and indeed $\operatorname{Var}(\bar X)=\frac{0.25}{100}=0.0025$. The standard error is $\sqrt{0.0025}=0.05$.

> **Connection — curvature, calculus & the MLE**
>
> The form $I=-E[\ell'']$ is literally the expected second derivative — the calculus measure of how curved the log-likelihood is at its peak. This is why the MLE's asymptotic variance (Section 5) is $1/I_n(\theta)$: a curvier likelihood pins $\theta$ down more tightly.

<a id="s8"></a>
### Rao–Blackwell & minimum-variance unbiased estimators

*Given any unbiased estimator, conditioning on a sufficient statistic can only improve it. With completeness, this yields the unique best unbiased estimator.*

#### Plain-language orientation

Suppose you have a rough, unbiased guess that uses only part of the data. Section 2 told us a sufficient statistic holds *all* the information about $\theta$. The **Rao–Blackwell theorem** says: average your rough guess over the irrelevant detail (i.e. condition on the sufficient statistic), and you get a new estimator that is still unbiased but has *no more* variance — usually strictly less. Add **completeness** and this improved estimator is provably the single best unbiased estimator.

#### Definitions

- **Conditional expectation** $E[\tilde\theta\mid T]$: the average value of $\tilde\theta$ among all data sets sharing a given value of $T$. It is itself a function of $T$, hence a valid statistic.
- **MVUE:** the **minimum-variance unbiased estimator** — the unbiased estimator with the smallest possible variance.

**Rao–Blackwell theorem**

$$\text{if } E[\tilde\theta]=\theta \text{ and } T \text{ is sufficient, then } \hat\theta=E[\tilde\theta\mid T] \text{ satisfies } E[\hat\theta]=\theta,\quad \operatorname{Var}(\hat\theta)\le \operatorname{Var}(\tilde\theta)$$

**Demonstration — why Rao–Blackwell works**

1. **Unbiasedness is preserved.** The **law of total expectation** says $E\big[E[\tilde\theta\mid T]\big]=E[\tilde\theta]$. Since $\hat\theta=E[\tilde\theta\mid T]$, this gives $E[\hat\theta]=E[\tilde\theta]=\theta$.
2. **Variance does not increase.** The **law of total variance** states $\operatorname{Var}(\tilde\theta)=\operatorname{Var}\big(E[\tilde\theta\mid T]\big)+E\big[\operatorname{Var}(\tilde\theta\mid T)\big]$. The first term is $\operatorname{Var}(\hat\theta)$; the second is an average of variances, hence $\ge 0$. Dropping a non-negative term, $\operatorname{Var}(\tilde\theta)\ge\operatorname{Var}(\hat\theta)$.
3. **Why $T$ must be sufficient.** If $T$ were not sufficient, $E[\tilde\theta\mid T]$ could still depend on the unknown $\theta$ (through the conditional distribution), making it uncomputable and not a valid statistic. Sufficiency guarantees the conditional distribution is free of $\theta$, so $\hat\theta$ is a genuine estimator.

**Demonstration — Rao–Blackwellize a crude Poisson estimator**

1. Let $X_1,\dots,X_n\ \text{i.i.d.}\ \sim\text{Poisson}(\lambda)$; we want to estimate $g(\lambda)=e^{-\lambda}$, which equals $P(X=0)$ (the probability of zero events).
2. A crude unbiased estimator uses only the first observation: $\tilde g=\mathbf{1}\{X_1=0\}$, the indicator that is $1$ if $X_1=0$ and $0$ otherwise. Its expectation is $E[\tilde g]=P(X_1=0)=e^{-\lambda}$, so it is unbiased — but wasteful, ignoring $X_2,\dots,X_n$.
3. The total $T=\sum X_i$ is sufficient and complete for $\lambda$ (it is the exponential-family statistic, Section 2). Rao–Blackwellize by conditioning: $\hat g=E[\mathbf 1\{X_1=0\}\mid T]=P(X_1=0\mid T)$.
4. A standard fact: given the total $T=t$, the count $X_1$ is distributed as $\text{Binomial}(t,1/n)$ (each of the $t$ events lands in slot $1$ with probability $1/n$). The probability of zero in slot $1$ is $\big(1-\frac1n\big)^t$. Therefore

   $$\hat g=P(X_1=0\mid T=t)=\Big(1-\tfrac1n\Big)^{t}=\Big(\tfrac{n-1}{n}\Big)^{\sum X_i}.$$

*This improved estimator is unbiased (by Rao–Blackwell) with smaller variance — and, by completeness, it is the unique MVUE of $e^{-\lambda}$.*

**Worked numeric example.** With $n=4$ and observed total $T=2$, the crude estimator using only $X_1$ would give either $0$ or $1$; the Rao–Blackwellized estimate is the smooth $\big(\frac{3}{4}\big)^2=\frac{9}{16}\approx 0.5625$, a far more sensible guess for $e^{-\lambda}$.

**Lehmann–Scheffé theorem (MVUE)**

$$T \text{ complete \& sufficient},\ \ E[\,\varphi(T)\,]=\theta \ \Longrightarrow\ \varphi(T) \text{ is the unique MVUE of }\theta$$

*If an unbiased function of a complete sufficient statistic exists, it is **the** minimum-variance unbiased estimator. Completeness guarantees uniqueness.*

**Why uniqueness follows from completeness.** Suppose $\varphi_1(T)$ and $\varphi_2(T)$ were two unbiased functions of the complete sufficient $T$. Their difference $d(T)=\varphi_1(T)-\varphi_2(T)$ has $E[d(T)]=\theta-\theta=0$ for all $\theta$. By the definition of **completeness** (Section 2), the only such function is identically zero, so $\varphi_1=\varphi_2$. Thus the unbiased function of $T$ is unique, and Rao–Blackwell shows it beats every other unbiased estimator.

> **Principle — the route to the best unbiased estimator**
>
> (1) Find a complete sufficient statistic $T$ (often via the exponential family). (2) Find any unbiased estimator. (3) Condition it on $T$, or directly find a function of $T$ with the right mean. The result is the MVUE. For a normal sample, $\bar X$ is the MVUE of $\mu$ and $S^2$ the MVUE of $\sigma^2$.

> **Connection — sufficiency pays off**
>
> Section 2 promised that sufficiency would let us improve estimators "for free." Rao–Blackwell is the payoff: the information-preserving compression $T$ is exactly what we condition on to shed irrelevant variance.

## Part C · Interval estimation & testing

<a id="s9"></a>
### Confidence intervals via pivotal quantities

*A confidence interval is built from a pivot: a function of data and parameter whose distribution is fixed and known. Invert its known quantiles to bracket $\theta$.*

#### Plain-language orientation

A single best guess $\hat\theta$ is never exactly right. A **confidence interval** instead reports a *range* of plausible values, together with a confidence level like 95%. The trick to building one is a **pivot**: a cleverly arranged combination of the data and the unknown $\theta$ whose probability distribution is completely known and does not involve $\theta$. Because we know the pivot's distribution, we know between which two cutoffs it falls 95% of the time; rearranging that statement to isolate $\theta$ produces the interval.

#### Definitions

- **Quantile.** The cutoff below which a given fraction of a distribution lies. For the standard normal, $z_{\alpha/2}$ is the point with area $\alpha/2$ to its right.
- **$\alpha$ (alpha).** The allowed error rate; confidence level is $1-\alpha$. For 95% confidence, $\alpha=0.05$.

**Pivotal quantity**

$$Q(\mathbf X,\theta)\ \text{is a pivot if its distribution does not depend on }\theta.$$

*From $P(a\le Q\le b)=1-\alpha$, algebraically isolate $\theta$ to get a random interval that covers $\theta$ with probability $1-\alpha$.*

**Demonstration — CI for a normal mean, $\sigma$ known**

1. Pivot: from Section 1, $Z=\dfrac{\bar X-\mu}{\sigma/\sqrt n}\sim N(0,1)$. Its distribution (standard normal) does not involve $\mu$, so it is a valid pivot.
2. Bracket it using the symmetric standard-normal cutoffs $\pm z_{\alpha/2}$: by definition of these quantiles, $P\big(-z_{\alpha/2}\le Z\le z_{\alpha/2}\big)=1-\alpha$.
3. Substitute $Z$ and solve the double inequality for $\mu$. Start from $-z_{\alpha/2}\le \frac{\bar X-\mu}{\sigma/\sqrt n}\le z_{\alpha/2}$. Multiply all three parts by $\sigma/\sqrt n>0$ (preserves the inequalities): $-z_{\alpha/2}\frac{\sigma}{\sqrt n}\le \bar X-\mu\le z_{\alpha/2}\frac{\sigma}{\sqrt n}$. Subtract $\bar X$ and multiply by $-1$ (which **reverses** the inequalities), giving

   $$\bar X-z_{\alpha/2}\frac{\sigma}{\sqrt n}\ \le\ \mu\ \le\ \bar X+z_{\alpha/2}\frac{\sigma}{\sqrt n}.$$

*For $\alpha=0.05$, $z_{\alpha/2}=z_{0.025}=1.96$ — the "two standard errors" of the empirical rule.*

**Worked numeric example.** Suppose $\sigma=10$, $n=25$, and $\bar X=50$. The standard error is $\sigma/\sqrt n=10/5=2$. A 95% interval is $50\pm 1.96\times 2 = 50\pm 3.92$, i.e. $[46.08,\ 53.92]$.

**Demonstration — CI for a normal mean, $\sigma$ unknown (the $t$ pivot)**

1. In practice $\sigma$ is unknown, so replace it by the sample standard deviation $S=\sqrt{S^2}$. The candidate pivot is $T=\dfrac{\bar X-\mu}{S/\sqrt n}$. It is no longer standard normal because the denominator is now random.
2. Rewrite $T=\dfrac{(\bar X-\mu)/(\sigma/\sqrt n)}{S/\sigma}$. The numerator is $N(0,1)$ (Section 1). For the denominator, recall from Section 6 that $\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}$, so $S/\sigma=\sqrt{\chi^2_{n-1}/(n-1)}$, and (for normal data) it is *independent* of the numerator.
3. By the **definition of Student's $t$** (a standard normal divided by the square root of an independent chi-squared over its degrees of freedom; see Section 12), $T\sim t_{n-1}$, the $t$ distribution with $n-1$ degrees of freedom — and crucially this distribution involves neither $\mu$ nor $\sigma$, so $T$ is a valid pivot.
4. Invert exactly as before, using the $t$ cutoffs $t_{n-1,\alpha/2}$:

   $$\bar X\ \pm\ t_{n-1,\,\alpha/2}\,\frac{S}{\sqrt n}.$$

*The fatter $t$ tails (larger cutoffs) are the price of estimating $\sigma$; as $n\to\infty$, $t_{n-1}\to N(0,1)$ and the two intervals merge.*

**Worked numeric example.** With $n=10$ ($9$ degrees of freedom), $\bar X=50$, $S=10$, and $t_{9,0.025}=2.262$: the standard error is $10/\sqrt{10}\approx 3.162$, so the interval is $50\pm 2.262\times 3.162=50\pm 7.15$, i.e. $[42.85,\ 57.15]$ — wider than the $\sigma$-known case, reflecting the extra uncertainty.

> **Principle — what confidence means**
>
> Confidence is a property of the **procedure**, not of one interval. "95% confidence" means: across repeated samples, the random interval covers the fixed $\theta$ $95\%$ of the time. Once computed, a particular interval like $[46.08, 53.92]$ either contains $\theta$ or not — there is no probability left to assign.

> **Connection — pivots unify the intro guide's intervals**
>
> Every CI in the intro guide — for a mean, a proportion, a variance (using a $\chi^2$ pivot) — is one pivot inverted. The recipe "estimate $\pm$ critical value $\times$ SE" is the special case where the pivot is approximately $N(0,1)$.

<a id="s10"></a>
### Hypothesis testing: errors, power & the Neyman–Pearson lemma

*A test partitions the data space into "reject" and "don't reject." Among all level-$\alpha$ tests, which is most powerful? For simple hypotheses, Neyman–Pearson gives the exact answer.*

#### Plain-language orientation

A **hypothesis test** is a courtroom for a claim about $\theta$. The **null hypothesis** $H_0$ is the default ("the coin is fair"); the **alternative** $H_1$ is the rival ("the coin is biased"). We design a rule that looks at the data and either rejects $H_0$ or not. Two mistakes are possible: convicting the innocent (rejecting a true $H_0$) and acquitting the guilty (failing to reject a false $H_0$). We cap the first error rate at $\alpha$ and then make the second as small as possible.

#### Definitions

- **Type I error:** rejecting $H_0$ when it is actually true. Its probability is $\alpha$.
- **Type II error:** failing to reject $H_0$ when $H_1$ is true. Its probability is $\beta$.
- **Power:** the probability of correctly rejecting a false $H_0$, equal to $1-\beta$.
- **Simple hypothesis:** one that fixes $\theta$ to a single value (e.g. $\theta=\theta_0$), as opposed to a **composite** one (e.g. $\theta>\theta_0$).

**Errors, size and power**

$$\alpha=P_{\theta_0}(\text{reject }H_0)\ \text{(Type I)},\qquad \beta=P_{\theta_1}(\text{fail to reject }H_0)\ \text{(Type II)}$$

$$\text{power}=1-\beta=P_{\theta_1}(\text{reject }H_0)$$

*A test has **size** $\alpha$ (its maximum Type I rate) and a **power function** $\beta(\theta)=P_\theta(\text{reject})$ giving the rejection probability at each $\theta$. We fix $\alpha$ and maximize power.*

**Neyman–Pearson lemma**

$$\text{For }H_0:\theta=\theta_0 \text{ vs } H_1:\theta=\theta_1,\ \text{the most powerful size-}\alpha\text{ test rejects when } \frac{L(\theta_1)}{L(\theta_0)}\ge k.$$

*The likelihood ratio is the optimal test statistic for two simple hypotheses; choose the threshold $k$ so the size equals $\alpha$.*

**Demonstration — Neyman–Pearson optimality**

A **test** is described by a function $\phi(\mathbf x)\in\{0,1\}$ that equals $1$ where we reject and $0$ where we do not. Its size is $E_{\theta_0}[\phi]$ and its power is $E_{\theta_1}[\phi]$.

1. Let $\phi^*$ be the likelihood-ratio (LR) test, rejecting (i.e. $\phi^*=1$) exactly where $L(\theta_1)\ge k\,L(\theta_0)$, with $k$ chosen so its size is exactly $\alpha$. Let $\phi$ be any competing test with size $\le\alpha$.
2. Consider the product $(\phi^*-\phi)\big(L(\theta_1)-kL(\theta_0)\big)$ at every data point. Where $\phi^*=1$: by the rule, $L(\theta_1)-kL(\theta_0)\ge0$, and $\phi^*-\phi=1-\phi\ge0$, so the product is $\ge0$. Where $\phi^*=0$: the rule gives $L(\theta_1)-kL(\theta_0)<0$, and $\phi^*-\phi=-\phi\le0$, so again the product is $\ge0$ (negative times non-positive). Hence pointwise the product is $\ge 0$, so its integral is too:

   $$\int (\phi^*-\phi)\big(L(\theta_1)-kL(\theta_0)\big)\,d\mathbf x\ \ge\ 0.$$
3. Expand the integral into two pieces, recognizing $\int \phi^* L(\theta_1)=\text{power}(\phi^*)$ etc.:

   $$\big[\text{power}(\phi^*)-\text{power}(\phi)\big]-k\big[\text{size}(\phi^*)-\text{size}(\phi)\big]\ge0.$$
4. Since $k\ge0$ and $\text{size}(\phi)\le\alpha=\text{size}(\phi^*)$, the bracket $\text{size}(\phi^*)-\text{size}(\phi)\ge0$, so the subtracted term $-k[\cdots]\le 0$. Moving it over, $\text{power}(\phi^*)-\text{power}(\phi)\ge k[\text{size}(\phi^*)-\text{size}(\phi)]\ge0$. Therefore $\text{power}(\phi^*)\ge\text{power}(\phi)$: the LR test is most powerful.

*Optimality of the likelihood ratio is the seed of every test in the next section.*

**Demonstration — the most powerful test for a normal mean**

1. $X_i\sim N(\mu,\sigma^2)$, $\sigma$ known, $H_0:\mu=\mu_0$ vs $H_1:\mu=\mu_1$ with $\mu_1>\mu_0$.
2. Compute the log of the likelihood ratio. Each likelihood is $\prod \frac{1}{\sqrt{2\pi}\sigma}\exp(-\frac{(x_i-\mu)^2}{2\sigma^2})$, and the constants cancel in the ratio. The exponent difference is $-\frac{1}{2\sigma^2}\sum[(x_i-\mu_1)^2-(x_i-\mu_0)^2]$. Expand the squares: $(x_i-\mu_1)^2-(x_i-\mu_0)^2 = -2x_i(\mu_1-\mu_0)+(\mu_1^2-\mu_0^2)$. Summing,

   $$\log\frac{L(\mu_1)}{L(\mu_0)}=\frac{(\mu_1-\mu_0)}{\sigma^2}\sum x_i+\text{const}=\frac{n(\mu_1-\mu_0)}{\sigma^2}\bar X+\text{const}.$$
3. Since $\mu_1-\mu_0>0$, the LR is an *increasing* function of $\bar X$. So "reject for large LR" is the same rule as "reject for large $\bar X$": reject when $\bar X\ge c$.
4. Choose $c$ so the size is $\alpha$. Under $H_0$, $\frac{\bar X-\mu_0}{\sigma/\sqrt n}\sim N(0,1)$, so $P_{\mu_0}(\bar X\ge c)=\alpha$ means $\frac{c-\mu_0}{\sigma/\sqrt n}=z_\alpha$, giving $c=\mu_0+z_\alpha\,\sigma/\sqrt n$. Equivalently, reject when $Z=\frac{\bar X-\mu_0}{\sigma/\sqrt n}\ge z_\alpha$.

*The familiar one-sided $z$-test is the Neyman–Pearson optimal test — and since the rejection rule does not depend on the specific $\mu_1$ (only on $\mu_1>\mu_0$), it is **uniformly most powerful** against all $\mu>\mu_0$.*

**Worked numeric example.** Test $H_0:\mu=100$ vs $H_1:\mu>100$ with $\sigma=15$, $n=9$, $\alpha=0.05$ (so $z_{0.05}=1.645$). The cutoff is $c=100+1.645\times 15/3=100+8.225=108.225$. If the observed $\bar X=110$, then $110>108.225$, so we reject $H_0$. Equivalently $Z=(110-100)/5=2.0>1.645$.

> **Connection — tests and intervals are duals**
>
> A level-$\alpha$ two-sided test of $H_0:\theta=\theta_0$ rejects exactly when $\theta_0$ lies outside the $1-\alpha$ confidence interval. The acceptance region of a test, inverted, *is* a confidence set — the same duality the intro guide hinted at, now made exact.

<a id="s11"></a>
### Likelihood-ratio, Wald & score tests

*For composite hypotheses and many parameters, three asymptotically equivalent tests dominate — all built from the likelihood, all approximately $\chi^2$.*

#### Plain-language orientation

The Neyman–Pearson lemma is perfect but only for two single values. Real questions are richer: "is $\mu$ equal to $100$, against *any* other value?" Three general-purpose tests handle this, all derived from the likelihood and all yielding a statistic that follows a chi-squared distribution for large samples. They look at the same peak of the log-likelihood from three angles — its height, its location, and its slope.

**The generalized likelihood-ratio statistic**

$$\Lambda=\frac{\sup_{\theta\in\Theta_0} L(\theta)}{\sup_{\theta\in\Theta} L(\theta)},\qquad -2\log\Lambda\ \xrightarrow{d}\ \chi^2_{r}$$

New symbols: $\sup$ ("supremum") means the largest achievable value; $\Theta_0$ is the restricted parameter set allowed under $H_0$, and $\Theta$ is the full set. So $\Lambda$ compares the best fit under $H_0$ to the best fit overall; it is always between $0$ and $1$, and small $\Lambda$ argues against $H_0$.

*$r$ is the number of restrictions imposed by $H_0$ (how many free parameters $H_0$ removes). Reject for large $-2\log\Lambda$. This limiting chi-squared is **Wilks' theorem**.*

**Demonstration — an LRT and its $\chi^2_1$ limit (Wilks)**

1. Normal sample, $\sigma$ known; test $H_0:\mu=\mu_0$ vs $H_1:\mu\ne\mu_0$. The numerator maximizes $L$ over the single allowed value $\mu_0$ (no choice); the denominator maximizes over all $\mu$, attained at the MLE $\hat\mu=\bar X$ (Section 5).
2. Plug into the normal log-likelihood and form $-2\log\Lambda = -2[\ell(\mu_0)-\ell(\bar X)]$. Only the sum-of-squares term depends on $\mu$:

   $$-2\log\Lambda=\frac{1}{\sigma^2}\Big[\sum(x_i-\mu_0)^2-\sum(x_i-\bar X)^2\Big].$$

   Expand using the identity $\sum(x_i-\mu_0)^2=\sum(x_i-\bar X)^2+n(\bar X-\mu_0)^2$ (a Pythagorean-type split, verified by adding and subtracting $\bar X$ inside the square and noting the cross term sums to zero). The $\sum(x_i-\bar X)^2$ cancels, leaving

   $$-2\log\Lambda=\frac{n(\bar X-\mu_0)^2}{\sigma^2}.$$
3. Under $H_0$, $\frac{\sqrt n(\bar X-\mu_0)}{\sigma}\sim N(0,1)$ (Section 1), and the square of a standard normal is by definition $\chi^2_1$ (Section 12). Hence

   $$-2\log\Lambda=\Big(\tfrac{\bar X-\mu_0}{\sigma/\sqrt n}\Big)^2=Z^2\sim\chi^2_1.$$

*Here Wilks' $\chi^2_1$ is exact (one restriction, $r=1$); in general it holds asymptotically as $n\to\infty$.*

**Worked numeric example.** With $\mu_0=100$, $\sigma=15$, $n=9$, $\bar X=110$: $-2\log\Lambda=\frac{9(110-100)^2}{225}=\frac{900}{225}=4.0$. The 5% cutoff for $\chi^2_1$ is $3.84$. Since $4.0>3.84$, reject $H_0$ (consistent with the $z$-test giving $Z=2.0$, and $2.0^2=4.0$).

**Wald and score (Rao) tests**

$$W=\frac{(\hat\theta-\theta_0)^2}{\widehat{\operatorname{Var}}(\hat\theta)}=I_n(\hat\theta)\,(\hat\theta-\theta_0)^2,\qquad R=\frac{U(\theta_0)^2}{I_n(\theta_0)}$$

*Both statistics $\xrightarrow{d}\chi^2_r$. The **Wald** test uses the MLE $\hat\theta$ and the curvature there ($\widehat{\operatorname{Var}}(\hat\theta)=1/I_n(\hat\theta)$ from Section 7); the **score** test uses the slope $U(\theta_0)$ of $\ell$ at $\theta_0$ and needs no MLE at all. LRT, Wald, and score agree asymptotically.*

**Worked numeric example (Wald, Bernoulli).** Test $H_0:p=0.5$ from $n=100$ flips with $40$ heads, so $\hat p=0.4$. The information at the MLE is $I_n(\hat p)=\frac{n}{\hat p(1-\hat p)}=\frac{100}{0.4\cdot0.6}=416.67$. Then $W=416.67\times(0.4-0.5)^2=416.67\times0.01=4.17>3.84$, so reject at the 5% level.

> **Principle — three views of one peak**
>
> Picture the log-likelihood curve near its maximum. The **LRT** measures the vertical drop in $\ell$ from $\hat\theta$ down to $\theta_0$; the **Wald** test measures the horizontal distance $\hat\theta-\theta_0$ (scaled by curvature); the **score** test measures the slope of $\ell$ at $\theta_0$. For a quadratic (normal) log-likelihood all three coincide exactly; in general they differ only in finite samples.

> **Connection — Cramér–Rao made operational**
>
> The Wald variance $1/I_n(\hat\theta)$ is the Cramér–Rao bound (Section 7) evaluated at the MLE — that section's floor returning as the standard error in the denominator. The score test uses $U(\theta_0)$ and $I_n(\theta_0)$ directly: the very quantities defined in Sections 3 and 7.

<a id="s12"></a>
### The standard tests & their sampling distributions (t, χ², F)

*Three distributions, all spawned by sampling from a normal population, supply the exact tests of classical statistics.*

#### Plain-language orientation

Almost every "named" test you meet — the $t$-test, the chi-squared test, the F-test of ANOVA — is built from one of three distributions. All three are *constructed* from the standard normal: square some normals and you get chi-squared; divide a normal by a scaled chi-squared and you get $t$; take a ratio of two chi-squareds and you get F. Knowing these constructions demystifies the whole classical toolkit.

**How the three arise from a normal sample**

$$Z=\frac{\bar X-\mu}{\sigma/\sqrt n}\sim N(0,1),\qquad \frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}$$

$$t_k=\frac{Z}{\sqrt{\chi^2_k/k}},\qquad F_{d_1,d_2}=\frac{\chi^2_{d_1}/d_1}{\chi^2_{d_2}/d_2}$$

Definitions in words: $\chi^2_k$ (chi-squared with $k$ degrees of freedom) is the distribution of $Z_1^2+\cdots+Z_k^2$, a sum of $k$ independent squared standard normals. $t_k$ is a standard normal divided by the square root of an *independent* $\chi^2_k$ scaled by its degrees of freedom. $F_{d_1,d_2}$ is a ratio of two independent chi-squareds, each divided by its own degrees of freedom.

*$\bar X\perp S^2$ for a normal sample (the symbol $\perp$ means "independent of"; the sample mean and sample variance are independent for normal data) — this independence is what makes the $t$ ratio's numerator and denominator independent, as the definition of $t_k$ requires.*

**Demonstration — $(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$ and $\bar X\perp S^2$ via the Helmert transformation**

*These two facts — quietly used above and in Section 6 — are the keystone of normal-sample theory. Here is their proof for $X_1,\dots,X_n\ \text{i.i.d.}\ \sim N(\mu,\sigma^2)$.*

1. **Standardize.** Put $Z_i=(X_i-\mu)/\sigma$. Then $Z_1,\dots,Z_n\ \text{i.i.d.}\ \sim N(0,1)$, so the random vector $\mathbf Z=(Z_1,\dots,Z_n)^\top$ has the **spherically symmetric** joint density $\propto\exp\!\big(-\tfrac12\sum_i z_i^2\big)=\exp\!\big(-\tfrac12\|\mathbf z\|^2\big)$. It depends on $\mathbf z$ only through its length $\|\mathbf z\|^2=\sum z_i^2$.
2. **Apply an orthogonal (Helmert) transformation.** Let $A$ be an $n\times n$ **orthogonal matrix** ($A^\top A=I$, i.e. its rows are mutually perpendicular unit vectors) whose **first row** is the constant vector $\big(\tfrac{1}{\sqrt n},\dots,\tfrac{1}{\sqrt n}\big)$; the remaining $n-1$ rows are any unit vectors completing an orthonormal basis (the classical **Helmert matrix** is one explicit choice). Define $\mathbf Y=A\mathbf Z$, i.e. $Y_j=\sum_i A_{ji}Z_i$.
3. **The transformed vector is again i.i.d. standard normal.** An orthogonal map preserves length, $\|\mathbf Y\|^2=\mathbf Z^\top A^\top A\,\mathbf Z=\|\mathbf Z\|^2$, and has Jacobian determinant $\pm1$, so the density of $\mathbf Y$ is $\propto\exp\!\big(-\tfrac12\|\mathbf y\|^2\big)$ — the *same* spherical form. That density factors as $\prod_j\exp(-\tfrac12 y_j^2)$, so $Y_1,\dots,Y_n\ \text{i.i.d.}\ \sim N(0,1)$. (Equivalently: a linear combination of independent normals is normal, and orthogonality makes the $Y_j$ uncorrelated, hence — being jointly normal — independent.)
4. **Identify the first coordinate.** $Y_1=\sum_i\tfrac{1}{\sqrt n}Z_i=\sqrt n\,\bar Z$, where $\bar Z=\frac1n\sum Z_i=(\bar X-\mu)/\sigma$. Thus $Y_1=\sqrt n\,(\bar X-\mu)/\sigma$ is a function of $\bar X$ alone.
5. **Identify the remaining coordinates as $S^2$.** Since $A$ preserves length, $\sum_{j=1}^n Y_j^2=\sum_{i=1}^n Z_i^2$. Subtract the first coordinate: by the algebra of step 4 and the identity $\sum_i(Z_i-\bar Z)^2=\sum_i Z_i^2-n\bar Z^2$,
   $$\sum_{j=2}^n Y_j^2=\sum_{i=1}^n Z_i^2-Y_1^2=\sum_{i=1}^n Z_i^2-n\bar Z^2=\sum_{i=1}^n(Z_i-\bar Z)^2=\frac{1}{\sigma^2}\sum_{i=1}^n(X_i-\bar X)^2=\frac{(n-1)S^2}{\sigma^2}.$$
6. **Read off both conclusions.** The right-hand side $\sum_{j=2}^n Y_j^2$ is a sum of $n-1$ independent squared standard normals, which is by definition $\chi^2_{n-1}$; hence $\dfrac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}$. Moreover $\bar X$ is a function of $Y_1$ only (step 4) while $S^2$ is a function of $Y_2,\dots,Y_n$ only (step 5), and these two groups of $Y_j$ are independent (step 3); therefore $\bar X\perp S^2$.

*The single trick — rotate the i.i.d. normal vector so that one new axis points along the all-ones direction (the mean) and the other $n-1$ axes span the orthogonal complement (the deviations) — delivers both facts at once, and shows transparently where the "$n-1$ degrees of freedom" come from: one axis was spent on $\bar X$.*

| Distribution | Definition | Used for | Test statistic |
| --- | --- | --- | --- |
| $t_k$ | $N(0,1)\big/\sqrt{\chi^2_k/k}$ | mean(s), $\sigma$ unknown; regression coefficients | $t=\dfrac{\bar X-\mu_0}{S/\sqrt n}$ |
| $\chi^2_k$ | sum of $k$ squared $N(0,1)$ | variance; goodness-of-fit; independence; LRT/Wald/score limits | $\dfrac{(n-1)S^2}{\sigma_0^2}$, $\ \sum\dfrac{(O-E)^2}{E}$ |
| $F_{d_1,d_2}$ | ratio of two scaled $\chi^2$ | compare two variances; ANOVA (3+ means) | $F=\dfrac{S_1^2}{S_2^2}$, $\ \dfrac{\text{MS}_{\text{between}}}{\text{MS}_{\text{within}}}$ |

**Demonstration — the one-sample $t$ statistic is genuinely $t_{n-1}$**

1. Write the statistic, then divide numerator and denominator by $\sigma$ to standardize: $\dfrac{\bar X-\mu}{S/\sqrt n}=\dfrac{(\bar X-\mu)/(\sigma/\sqrt n)}{S/\sigma}$. The numerator $(\bar X-\mu)/(\sigma/\sqrt n)$ is exactly $Z\sim N(0,1)$ (Section 1).
2. The denominator: $S/\sigma=\sqrt{S^2/\sigma^2}$. From $\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}$ we get $\frac{S^2}{\sigma^2}=\frac{\chi^2_{n-1}}{n-1}$, so $S/\sigma=\sqrt{\chi^2_{n-1}/(n-1)}$. For normal data this is independent of the numerator (because $\bar X\perp S^2$).
3. Substituting, the statistic equals $\dfrac{N(0,1)}{\sqrt{\chi^2_{n-1}/(n-1)}}$ with independent numerator and denominator — which is precisely the definition of $t_{n-1}$ given above. Therefore the one-sample $t$ statistic is exactly $t_{n-1}$.

*The $t$ distribution is not an approximation here — it is the exact sampling law, and the reason the intro guide's "use $t$ when $\sigma$ is unknown" is correct.*

**Worked numeric example (chi-squared variance test).** Test whether a process has variance $\sigma_0^2=4$ from $n=10$ items with observed $S^2=6$. The statistic is $\frac{(n-1)S^2}{\sigma_0^2}=\frac{9\times 6}{4}=13.5$, compared against $\chi^2_9$. The upper 5% cutoff of $\chi^2_9$ is $16.92$, so $13.5<16.92$ and we do not reject at the upper tail — the observed variance is not significantly large.

> **Connection — the Probability guide's distributions, put to work**
>
> The $\chi^2$, $t$, and $F$ defined abstractly in the Probability guide are exactly the sampling distributions of normal-data statistics. Classical inference is, in large part, bookkeeping with these three laws.

## Part D · Bayesian & nonparametric

<a id="s13"></a>
### Bayesian inference: priors, posteriors & conjugacy

*Treat $\theta$ itself as random. Encode beliefs in a prior, update with data via Bayes' theorem, and read off the posterior — a full distribution for $\theta$.*

#### Plain-language orientation

Until now $\theta$ was a fixed unknown. The **Bayesian** approach makes a bold move: treat $\theta$ as random, with a probability distribution describing what we believe *before* seeing data (the **prior**). After observing data, we use Bayes' theorem to update those beliefs into a **posterior** distribution. The posterior is a complete answer — not a single estimate but a whole curve of plausibility over $\theta$.

#### Definitions

- **Prior** $\pi(\theta)$: the distribution of $\theta$ before seeing data (the Greek $\pi$, "pi," denotes a density over the parameter).
- **Posterior** $\pi(\theta\mid\mathbf x)$: the distribution of $\theta$ after seeing data.
- **Evidence / marginal likelihood:** the denominator $\int L(\theta)\pi(\theta)\,d\theta$, a constant that makes the posterior integrate to $1$.
- **$\propto$ ("proportional to"):** equal up to a constant factor not involving $\theta$.

**Bayes' theorem for parameters**

$$\pi(\theta\mid\mathbf x)=\frac{L(\theta)\,\pi(\theta)}{\int L(\theta)\,\pi(\theta)\,d\theta}\ \propto\ \underbrace{L(\theta)}_{\text{likelihood}}\ \underbrace{\pi(\theta)}_{\text{prior}}$$

*Posterior $\propto$ likelihood $\times$ prior. The denominator (the marginal/evidence) is just the normalizing constant ensuring the posterior is a valid distribution.*

**Why this is Bayes' theorem.** Bayes' theorem for events says $P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}$. Identify $A$ with "$\theta$ takes a given value" (prior $\pi(\theta)$) and $B$ with "the data $\mathbf x$" (whose probability given $\theta$ is the likelihood $L(\theta)=f(\mathbf x\mid\theta)$). Then $P(A\mid B)$ becomes the posterior, $P(B\mid A)$ the likelihood, $P(A)$ the prior, and $P(B)$ the evidence — exactly the formula above, with densities replacing event probabilities.

> **Concept — conjugacy**
>
> A prior is **conjugate** to a likelihood if the resulting posterior belongs to the same family as the prior. Conjugate pairs make the update purely algebraic — no integration needed — and reveal the data's effect as a simple change of the family's parameters.

| Likelihood | Conjugate prior | Posterior |
| --- | --- | --- |
| Bernoulli / Binomial($p$) | Beta($\alpha,\beta$) | Beta($\alpha+\sum x_i,\ \beta+n-\sum x_i$) |
| Poisson($\lambda$) | Gamma($\alpha,\beta$) | Gamma($\alpha+\sum x_i,\ \beta+n$) |
| Normal mean ($\sigma^2$ known) | Normal($\mu_0,\tau_0^2$) | Normal (precision-weighted, below) |
| Normal precision ($\mu$ known) | Gamma | Gamma |
| Exponential($\lambda$) | Gamma($\alpha,\beta$) | Gamma($\alpha+n,\ \beta+\sum x_i$) |
| Multinomial | Dirichlet | Dirichlet |

**Demonstration — the Beta–Bernoulli update**

The **Beta($\alpha,\beta$)** distribution is a flexible curve on $[0,1]$ with density proportional to $p^{\alpha-1}(1-p)^{\beta-1}$ — a natural prior for a probability.

1. Prior $\pi(p)\propto p^{\alpha-1}(1-p)^{\beta-1}$; likelihood $L(p)\propto p^{\sum x_i}(1-p)^{n-\sum x_i}$ (from Section 2).
2. Multiply, combining powers with the rule $a^b a^c=a^{b+c}$:

   $$\pi(p\mid\mathbf x)\propto p^{\alpha-1}(1-p)^{\beta-1}\cdot p^{\sum x_i}(1-p)^{n-\sum x_i}=p^{\alpha+\sum x_i-1}(1-p)^{\beta+n-\sum x_i-1}.$$
3. Match the exponents to the Beta form $p^{a-1}(1-p)^{b-1}$: this is the kernel of $\text{Beta}\big(\alpha+\sum x_i,\ \beta+n-\sum x_i\big)$ — the same family, with the first parameter bumped by the number of successes and the second by the number of failures.

*The prior parameters $(\alpha,\beta)$ act like "pseudo-counts" of prior successes and failures.*

**Worked numeric example.** Start from a uniform prior $\text{Beta}(1,1)$ (all probabilities equally likely). Flip a coin $n=10$ times, observe $7$ heads ($\sum x_i=7$, failures $=3$). The posterior is $\text{Beta}(1+7,\ 1+3)=\text{Beta}(8,4)$. Its mean is $\frac{8}{8+4}=\frac{8}{12}\approx 0.667$ — pulled slightly below the raw $0.7$ by the prior's pseudo-counts.

> **Connection — Bayes' theorem from the Probability guide**
>
> This is the very same Bayes' theorem used for events, lifted to densities: $P(A\mid B)\propto P(B\mid A)P(A)$ becomes $\pi(\theta\mid x)\propto f(x\mid\theta)\pi(\theta)$. Frequentist and Bayesian inference share the likelihood; they differ only in whether $\theta$ gets a probability distribution.

<a id="s14"></a>
### Bayesian estimation & credible intervals

*From the posterior we extract point estimates and intervals — and the famous normal–normal update shows the posterior mean is a precision-weighted average of prior and data.*

#### Plain-language orientation

The posterior is a whole distribution, but often we want a single number or a range. The **posterior mean** is the natural single summary; a **credible interval** is the Bayesian range. Unlike a confidence interval, a credible interval lets you say honestly "there is a 95% probability that $\theta$ lies in here" — because in the Bayesian world $\theta$ has a probability distribution.

**Posterior point estimates**

$$\hat\theta_{\text{Bayes}}=E[\theta\mid\mathbf x]\ \text{(posterior mean, min. squared-error loss)},\qquad \hat\theta_{\text{MAP}}=\arg\max_\theta \pi(\theta\mid\mathbf x)$$

New term: **MAP** stands for **maximum a posteriori** — the value where the posterior density peaks (its mode).

*The posterior mean minimizes expected squared-error loss; the posterior median minimizes absolute loss; the MAP (mode) is the Bayesian analogue of the MLE with a prior penalty.*

**Why the posterior mean minimizes squared-error loss.** We seek the number $d$ minimizing $E[(\theta-d)^2\mid\mathbf x]$. Expand: $E[\theta^2\mid\mathbf x]-2dE[\theta\mid\mathbf x]+d^2$. Differentiate in $d$ and set to zero: $-2E[\theta\mid\mathbf x]+2d=0$, so $d=E[\theta\mid\mathbf x]$, the posterior mean. The second derivative is $2>0$, confirming a minimum.

**Demonstration — normal prior is conjugate; posterior mean is precision-weighted**

The **precision** of a normal distribution is the reciprocal of its variance; large precision means tight, confident beliefs.

1. Data summary $\bar X\mid\mu\sim N(\mu,\sigma^2/n)$ ($\sigma$ known), prior $\mu\sim N(\mu_0,\tau_0^2)$. The posterior is proportional to the product of the two normal densities; in the exponent we add the two quadratics in $\mu$.
2. The sum of two quadratics in $\mu$ is itself a quadratic, so the posterior is normal: $\mu\mid\mathbf x\sim N(\mu_n,\tau_n^2)$. Collecting the coefficient of $\mu^2$ in the exponent gives the posterior precision as the sum of the prior precision $1/\tau_0^2$ and the data precision $n/\sigma^2$:

   $$\frac{1}{\tau_n^2}=\frac{1}{\tau_0^2}+\frac{n}{\sigma^2}.$$
3. Collecting the coefficient of the linear term and dividing gives the posterior mean as the precision-weighted average of the prior mean $\mu_0$ and the data mean $\bar X$:

   $$\mu_n=\frac{\frac{1}{\tau_0^2}\,\mu_0+\frac{n}{\sigma^2}\,\bar X}{\frac{1}{\tau_0^2}+\frac{n}{\sigma^2}}.$$

   Each source is weighted by how precise it is — the more confident source pulls harder.

*As $n\to\infty$ the data precision $n/\sigma^2$ dominates, $\mu_n\to\bar X$, and the prior washes out — Bayesian and frequentist estimates converge.*

**Worked numeric example.** Prior $\mu\sim N(\mu_0=0,\ \tau_0^2=1)$, so prior precision $=1$. Data: $\sigma^2=4$, $n=8$, $\bar X=3$, so data precision $=n/\sigma^2=8/4=2$. Posterior precision $=1+2=3$, so $\tau_n^2=1/3\approx 0.333$. Posterior mean $\mu_n=\frac{1\cdot0+2\cdot3}{3}=\frac{6}{3}=2$ — a compromise between the prior's $0$ and the data's $3$, leaning toward the data because it is twice as precise.

**Credible interval**

$$P\big(\theta\in C\mid\mathbf x\big)=1-\alpha,\qquad \text{e.g. } [\,q_{\alpha/2},\,q_{1-\alpha/2}\,]\ \text{of the posterior}$$

Here $q_{\alpha/2}$ and $q_{1-\alpha/2}$ are the lower and upper quantiles of the *posterior* distribution.

*Unlike a confidence interval, this **is** a direct probability statement about $\theta$ given the data — the interpretation people wrongly attach to confidence intervals.*

**Worked numeric example.** Continuing above, the posterior is $N(2,\ 0.333)$ with standard deviation $\sqrt{0.333}\approx 0.577$. A 95% credible interval is $2\pm 1.96\times 0.577=2\pm 1.13$, i.e. $[0.87,\ 3.13]$, and we may legitimately say "given the data and prior, $\theta$ lies in $[0.87, 3.13]$ with probability 0.95."

> **Principle — credible vs confidence**
>
> A 95% **credible** interval says "given the data and prior, $\theta$ lies here with probability 0.95." A 95% **confidence** interval makes a long-run frequency claim about the procedure (Section 9). With a flat prior and a symmetric likelihood the two often numerically coincide, but their meanings differ sharply.

> **Connection — regularization is a prior**
>
> The MAP estimate with a normal prior on $\mu$ is exactly ridge-style shrinkage of $\bar X$ toward $\mu_0$: maximizing the log-posterior adds a $-\frac{(\mu-\mu_0)^2}{2\tau_0^2}$ penalty to the log-likelihood. Penalized likelihood methods are MAP estimation in disguise — a bridge between Bayesian priors and the optimization view of estimation.

<a id="s15"></a>
### Nonparametric methods & the bootstrap

*When you won't assume a parametric model, let the data stand in for the population. The empirical distribution and resampling do the heavy lifting.*

#### Plain-language orientation

So far we always assumed a model family (normal, Poisson, etc.). **Nonparametric** methods drop that assumption and let the data speak for themselves. The key object is the **empirical distribution** — literally the histogram of the data treated as if it *were* the population. The **bootstrap** then estimates an estimator's uncertainty by repeatedly resampling from the data, sidestepping the need for any formula.

#### Definitions

- **Empirical distribution function (EDF)** $\hat F_n(x)$: the fraction of the data that are $\le x$.
- **Indicator** $\mathbf 1\{A\}$: equals $1$ when the statement $A$ is true, $0$ otherwise.
- **Resample (with replacement):** a new data set of size $n$ drawn from the observed values, where each draw is uniformly random and values can repeat.

**The empirical distribution function**

$$\hat F_n(x)=\frac1n\sum_{i=1}^n \mathbf 1\{X_i\le x\}\ \xrightarrow{\text{a.s.}}\ F(x)\quad(\text{Glivenko–Cantelli, uniformly})$$

The arrow $\xrightarrow{\text{a.s.}}$ means "almost surely" (with probability one). The **Glivenko–Cantelli theorem** guarantees $\hat F_n$ converges to the true $F$ uniformly — not just at each point but everywhere at once.

*$\hat F_n$ is the nonparametric MLE of $F$. Plug-in estimators replace the unknown $F$ by $\hat F_n$: the sample mean estimates the population mean, the sample median the population median, and so on.*

**Why $\hat F_n(x)\to F(x)$ at each $x$.** Fix $x$. Each indicator $\mathbf 1\{X_i\le x\}$ is a Bernoulli variable equal to $1$ with probability $F(x)=P(X\le x)$. So $\hat F_n(x)$ is the average of $n$ i.i.d. Bernoulli($F(x)$) variables, and by the **Law of Large Numbers** (Section 6 consistency, applied here) this average converges to its mean $F(x)$. Glivenko–Cantelli strengthens this to hold uniformly in $x$.

> **Concept — the bootstrap idea**
>
> To gauge the variability of a statistic $\hat\theta=T(\hat F_n)$ without a formula, treat the sample as the population: resample from it and watch how $\hat\theta$ varies. The **plug-in principle** — replace $F$ by $\hat F_n$ — is the whole trick.

**Demonstration — the nonparametric bootstrap for a standard error**

1. From the observed sample $\{x_1,\dots,x_n\}$, draw a resample of size $n$ with replacement: $\{x_1^*,\dots,x_n^*\}$. (Some original values appear multiple times, others not at all.)
2. Compute the statistic on the resample, $\hat\theta^{*(b)}=T(x_1^*,\dots,x_n^*)$ (e.g. the sample median).
3. Repeat steps 1–2 for $b=1,\dots,B$ (say $B=2000$) to get replicates $\hat\theta^{*(1)},\dots,\hat\theta^{*(B)}$.
4. Estimate the standard error by the spread (sample standard deviation) of the bootstrap replicates, where $\bar{\hat\theta}^{*}=\frac1B\sum_b \hat\theta^{*(b)}$ is their average:

   $$\widehat{\text{SE}}_{\text{boot}}=\sqrt{\frac{1}{B-1}\sum_{b=1}^B\big(\hat\theta^{*(b)}-\bar{\hat\theta}^{*}\big)^2}.$$
5. A simple $1-\alpha$ interval is the **percentile interval** $\big[\hat\theta^{*}_{(\alpha/2)},\ \hat\theta^{*}_{(1-\alpha/2)}\big]$ — the empirical quantiles of the replicates (e.g. the 2.5th and 97.5th percentiles for 95%).

*No distributional assumption, no CLT formula — the resampling reconstructs the sampling distribution from the data alone.*

**Worked numeric example (tiny, by hand).** Data $\{1, 5, 9\}$, statistic = the mean. One resample might be $\{5,5,9\}$ with mean $19/3\approx 6.33$; another $\{1,1,9\}$ with mean $11/3\approx 3.67$; another $\{1,5,5\}$ with mean $11/3\approx 3.67$. Across many such resamples the spread of these means estimates $\text{SE}(\bar X)$ — which here, since we know $\bar X$'s formula, should be near $\sqrt{\frac{\text{sample variance}}{3}}$, providing a sanity check the bootstrap reproduces without using that formula.

> **Connection — why the bootstrap works**
>
> The sampling distribution describes how $\hat\theta$ varies as samples are drawn from $F$. The bootstrap substitutes $\hat F_n$ for the unknown $F$ and draws from *it*. Glivenko–Cantelli guarantees $\hat F_n\approx F$, so bootstrap variability approximates true sampling variability — the plug-in principle made operational.

<a id="s16"></a>
### A glimpse beyond: decision theory & large-sample asymptotics

*A unifying frame — estimation and testing as decisions under loss — and the asymptotic machinery (delta method, efficiency) that makes the MLE the default tool.*

#### Plain-language orientation

Step back and view estimation and testing as special cases of one idea: making a **decision** under uncertainty, where mistakes carry a **loss**. The quality of a decision rule is its average loss, called **risk**. Separately, the **delta method** lets us carry the MLE's known approximate-normality through any smooth transformation, so we can put error bars on derived quantities like odds and rates.

#### Definitions

- **Decision rule** $\delta$: a function mapping observed data to an action (e.g. an estimate, or "reject/don't reject").
- **Loss function** $\ell(\theta, d)$: the penalty for taking action $d$ when the truth is $\theta$ (note: this $\ell$ is a loss, not the log-likelihood of earlier sections; the symbol is reused by convention).
- **Risk** $R(\theta,\delta)$: the expected loss, averaged over the data.

**Risk, the language of decisions**

$$R(\theta,\delta)=E_\theta\big[\,\ell(\theta,\delta(\mathbf X))\,\big],\qquad \text{e.g. squared-error loss } \ell(\theta,d)=(d-\theta)^2\Rightarrow R=\text{MSE}$$

*A decision rule $\delta$ maps data to actions; its **risk** is expected loss. With squared-error loss, the risk is exactly the MSE of Section 6 — so estimation is a special case of decision theory.*

**Why squared-error risk equals MSE.** With $\ell(\theta,d)=(d-\theta)^2$ and $d=\delta(\mathbf X)=\hat\theta$, the risk is $R=E_\theta[(\hat\theta-\theta)^2]$, which is the definition of mean squared error (Section 6).

> **Principle — admissibility, minimax & Bayes rules**
>
> A rule is **inadmissible** if another rule has $\le$ risk everywhere and strictly less somewhere (it is dominated, so never worth using). A **minimax** rule minimizes the worst-case risk $\max_\theta R(\theta,\delta)$; a **Bayes** rule minimizes risk averaged over a prior — it is the posterior-expected-loss minimizer of Section 14. Remarkably, in dimension $\ge3$ the sample mean is inadmissible (Stein's paradox): shrinkage estimators beat it everywhere.

**The delta method**

$$\sqrt n\,(\hat\theta-\theta)\xrightarrow{d}N(0,\sigma^2)\ \Longrightarrow\ \sqrt n\,\big(g(\hat\theta)-g(\theta)\big)\xrightarrow{d}N\!\big(0,\ [g'(\theta)]^2\sigma^2\big)$$

Here $g$ is any smooth transformation and $g'(\theta)$ its derivative. The result says: a transformed estimator is also approximately normal, with variance scaled by the squared slope $[g'(\theta)]^2$.

*A first-order Taylor expansion propagates asymptotic normality through a smooth transformation $g$ — the asymptotic version of error propagation, and pure calculus.*

**Demonstration — the delta method**

1. **Taylor-expand** $g$ about $\theta$ to first order (the calculus fact that a smooth function is locally well-approximated by its tangent line): $g(\hat\theta)\approx g(\theta)+g'(\theta)(\hat\theta-\theta)$. The error is of order $(\hat\theta-\theta)^2$, which is negligible compared to the linear term as $\hat\theta\to\theta$.
2. Subtract $g(\theta)$ and multiply by $\sqrt n$: $\sqrt n\,(g(\hat\theta)-g(\theta))\approx g'(\theta)\cdot\sqrt n\,(\hat\theta-\theta)$.
3. By assumption $\sqrt n(\hat\theta-\theta)\xrightarrow{d}N(0,\sigma^2)$. Multiplying a quantity converging to $N(0,\sigma^2)$ by the constant $g'(\theta)$ scales its variance by $[g'(\theta)]^2$ (recall $\operatorname{Var}(cY)=c^2\operatorname{Var}(Y)$, Section 1). By **Slutsky's theorem** (which lets us combine a convergent-in-distribution sequence with constants), the right side $\xrightarrow{d}N(0,[g'(\theta)]^2\sigma^2)$, and so does the left.

*This is how standard errors are obtained for odds, rates, and other transformed parameters.*

**Worked numeric example.** Suppose $\hat p=0.4$ from $n=100$, with $\operatorname{Var}(\hat p)=\frac{p(1-p)}{n}\approx\frac{0.4\cdot0.6}{100}=0.0024$. We want a standard error for the **log-odds** $g(p)=\log\frac{p}{1-p}$. Its derivative is $g'(p)=\frac{1}{p(1-p)}=\frac{1}{0.24}\approx 4.167$. By the delta method, $\operatorname{Var}(g(\hat p))\approx [g'(\hat p)]^2\operatorname{Var}(\hat p)=4.167^2\times 0.0024\approx 0.0417$, so the standard error of the log-odds is $\sqrt{0.0417}\approx 0.204$.

> **Principle — the asymptotic supremacy of the MLE**
>
> Under regularity, $\sqrt n(\hat\theta_{\text{MLE}}-\theta)\xrightarrow{d}N(0,1/I_1(\theta))$: the MLE is consistent, asymptotically normal, and asymptotically efficient — it attains the Cramér–Rao bound (Section 7) in the limit. This is why, absent special structure, maximum likelihood (and its Bayesian cousin) is the workhorse of statistical inference.

> **Connection — the whole guide, in one arc**
>
> Likelihood (s3) gives the score and information (s7); maximizing it gives the MLE (s5); information bounds its variance (s7–8) and sets the width of intervals (s9) and the scale of tests (s10–11); the same likelihood, times a prior, gives the posterior (s13–14); and where no model is assumed, the empirical distribution and the bootstrap (s15) stand in. One function — the likelihood — organizes the entire subject.

---

*A course in mathematical statistics — sufficiency, estimation, the Cramér–Rao bound, Neyman–Pearson and likelihood-ratio testing, the Bayesian update, and the bootstrap — each principle stated precisely and each theorem demonstrated. A companion to the intro Statistics and Probability guides. Return to any box as a reference, and remember: behind estimation, testing, and Bayes alike stands a single object, the likelihood function.*
