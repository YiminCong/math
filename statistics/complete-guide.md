**English** · [中文](complete-guide.zh.md)

# Statistics, *connected.*

A full first course — describing data, the probability that underlies it, and the inference it powers — laid out basics → advanced. Every core formula is **demonstrated**, and the threads linking them are made explicit.

[← Back to all guides](../README.md)

## Part A · Describing data

<a id="s0"></a>
### The big picture

Statistics is the science of learning from data *in the presence of variability*. It has three movements, and the whole subject is the bridge between them.

- **Describe** — summarize the data you have (center, spread, shape).
- **Model** — use *probability* to describe the random process that generated it.
- **Infer** — reason backward from a sample to the population, with honest uncertainty.

> **Principle — the core problem**
>
> We almost never see the whole **population**; we see a **sample**. Statistics quantifies how much a sample can tell us about the population, and how confident we may be. Probability runs "population → sample"; inference runs "sample → population." They are inverses.

#### The whole course on one line

> Describe data → Probability → Random variables & the Normal → Sampling distributions → Confidence intervals & tests → Regression

<a id="s1"></a>
### Data & variables

*Before any formula: know what kind of thing you are measuring. It dictates every method that follows.*

> **Concept — population vs sample, parameter vs statistic**
>
> A **population** is everyone/everything of interest; a **sample** is the subset you actually observe. A number describing the population is a **parameter** (fixed, usually unknown — written with Greek letters $\mu,\sigma,p$); the same number computed from a sample is a **statistic** (random, observed — written $\bar x, s, \hat p$). All of inference is using statistics to estimate parameters.

**Types of variables**

***Categorical** (qualitative): labels — nominal (no order, e.g. color) or ordinal (ordered, e.g. ratings). **Numerical** (quantitative): discrete (counts) or continuous (measurements). The variable type decides whether you summarize with proportions or with means, and which test applies.*

> **Principle — random sampling is what makes inference valid**
>
> A **simple random sample** gives every member an equal chance of selection. This is not a technicality: it is the assumption that lets probability theory apply to real data. **Bias** (systematic error from how data is collected) cannot be fixed by a bigger sample — only by better sampling.

<a id="s2"></a>
### Describing center & spread

*Two questions summarize any dataset: where is it centered, and how spread out is it?*

**Measures of center**

$$\text{mean }\ \bar x=\frac1n\sum_{i=1}^n x_i,\qquad \text{population }\ \mu=\frac1N\sum_{i=1}^N x_i$$

***Median** = middle value (robust to outliers). **Mode** = most frequent. The mean is pulled toward a skew; the median resists it.*

**Measures of spread**

$$\text{variance }\ \sigma^2=\frac1N\sum(x_i-\mu)^2,\qquad s^2=\frac{1}{n-1}\sum(x_i-\bar x)^2$$

$$\text{SD}=\sqrt{\text{variance}},\qquad \text{IQR}=Q_3-Q_1,\qquad \text{range}=\max-\min$$

> **Concept — why variance squares the deviations**
>
> Deviations $x_i-\bar x$ always sum to zero, so we can't just average them. Squaring makes them positive and punishes large misses heavily; the square root at the end (the **standard deviation**) returns to the original units, so it reads as a "typical distance from the mean."

**Demonstration — why the sample variance divides by $n-1$**

1. We measure spread around the sample mean $\bar x$, but $\bar x$ is itself fitted to the data — it sits closer to the points than the true $\mu$ would.
2. So $\sum(x_i-\bar x)^2$ is systematically too small as an estimate of the true spread.
3. Using $\bar x$ costs one "degree of freedom": only $n-1$ of the deviations are free (they must sum to 0). Dividing by $n-1$ instead of $n$ corrects the bias, so that $E[s^2]=\sigma^2$.

*This is **Bessel's correction**. For a known population mean, you would divide by $n$.*

<a id="s3"></a>
### Distributions & visualizing data

*Center and spread don't capture shape — and shape changes everything.*

> **Concept — shape & skew**
>
> A distribution can be **symmetric**, **right-skewed** (a long tail of large values; mean > median), or **left-skewed** (mean < median). The relationship of mean to median is a quick read on skew. **Histograms** show shape; **boxplots** show the five-number summary (min, $Q_1$, median, $Q_3$, max).

**Percentiles, z-scores & outliers**

$$z=\frac{x-\mu}{\sigma}\qquad(\text{how many SDs from the mean})$$

$$\text{outlier if }\ xQ_3+1.5\,\text{IQR}$$

> **Connection — the z-score is the thread of the whole course**
>
> The z-score strips away units and scale: it turns any value into "distance from center, measured in standard deviations." This single idea returns as the **standard Normal** (Section 8), the **test statistic** (Section 11), and the basis of **correlation** (Section 13).

## Part B · Probability

<a id="s4"></a>
### Probability basics

*The mathematics of chance — the engine that lets a sample speak about a population.*

> **Concept — sample space & events**
>
> The **sample space** $S$ is the set of all possible outcomes; an **event** is a subset of it. A probability $P(A)$ measures how likely event $A$ is, on a scale from 0 (impossible) to 1 (certain).

**The axioms & basic rules**

$$0\le P(A)\le 1,\qquad P(S)=1,\qquad P(A^c)=1-P(A)$$

$$P(A\cup B)=P(A)+P(B)-P(A\cap B)$$

*The subtraction in the addition rule avoids double-counting the overlap. For **mutually exclusive** events the overlap is 0.*

<a id="s5"></a>
### Conditional probability & Bayes' theorem

*How knowing one thing changes the probability of another — and how to flip the conditioning around.*

**Conditional probability, multiplication, independence**

$$P(A\mid B)=\frac{P(A\cap B)}{P(B)},\qquad P(A\cap B)=P(A\mid B)\,P(B)$$

$$A,B \text{ independent} \iff P(A\cap B)=P(A)P(B)$$

**Bayes' theorem**

$$P(A\mid B)=\frac{P(B\mid A)\,P(A)}{P(B)},\qquad P(B)=\sum_i P(B\mid A_i)P(A_i)$$

**Demonstration — Bayes' theorem in one line**

1. Write the joint probability two ways using the multiplication rule:

   $$P(A\cap B)=P(A\mid B)P(B)=P(B\mid A)P(A).$$
2. Set the right two equal and divide by $P(B)$:

   $$P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}.$$

*Bayes simply reverses the direction of conditioning — turning "probability of the evidence given the cause" into "probability of the cause given the evidence."*

> **Principle — why Bayes surprises people**
>
> For a rare condition, even an accurate test produces many false positives, because the few true cases are swamped by the large healthy population. Bayes forces you to weight the test result by the **base rate** $P(A)$ — the lesson at the heart of medical screening and spam filters alike.

<a id="s6"></a>
### Random variables & expectation

*A random variable attaches a number to each outcome; expectation is its long-run average.*

**Expectation & variance**

$$E[X]=\sum_x x\,P(x)\quad\text{(discrete)},\qquad E[X]=\int x\,f(x)\,dx\quad\text{(continuous)}$$

$$\operatorname{Var}(X)=E\big[(X-\mu)^2\big]=E[X^2]-\big(E[X]\big)^2$$

> **Connection — this is where calculus enters**
>
> For continuous variables, the probability density $f(x)$ plays the role of a function, and **probability is area under it**: $P(a\le X\le b)=\int_a^b f(x)\,dx$. Expectation is an integral. The Normal curve, percentiles, and p-values are all areas — the integral calculus you already know.

**Linearity & sums**

$$E[aX+b]=aE[X]+b,\qquad E[X+Y]=E[X]+E[Y]$$

$$\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X),\qquad \operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)\ \text{(if independent)}$$

**Demonstration — $\operatorname{Var}(X)=E[X^2]-(E[X])^2$**

1. Expand the square inside the definition:

   $$E\big[(X-\mu)^2\big]=E\big[X^2-2\mu X+\mu^2\big].$$
2. Apply linearity, and use $E[X]=\mu$:

   $$=E[X^2]-2\mu\,\mu+\mu^2=E[X^2]-\mu^2.$$

*The handy "mean of the square minus the square of the mean."*

<a id="s7"></a>
### Common distributions

*A handful of named distributions model most real situations. Know each one's story, mean, and variance.*

| Distribution | Models | Mean | Variance |
| --- | --- | --- | --- |
| Bernoulli($p$) | one yes/no trial | $p$ | $p(1-p)$ |
| Binomial($n,p$) | $\#$ successes in $n$ trials | $np$ | $np(1-p)$ |
| Geometric($p$) | trials until first success | $1/p$ | $(1-p)/p^2$ |
| Poisson($\lambda$) | rare events per interval | $\lambda$ | $\lambda$ |
| Uniform($a,b$) | equally likely on $[a,b]$ | $(a+b)/2$ | $(b-a)^2/12$ |
| Normal($\mu,\sigma^2$) | sums of many small effects | $\mu$ | $\sigma^2$ |
| Exponential($\lambda$) | waiting time between events | $1/\lambda$ | $1/\lambda^2$ |

**The binomial probability**

$$P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}$$

*$\binom nk$ counts the orderings of $k$ successes; $p^k(1-p)^{n-k}$ is the probability of any one such ordering.*

**Demonstration — why the binomial mean is $np$**

1. A Binomial is just a sum of $n$ independent Bernoulli trials: $X=X_1+\cdots+X_n$, each with mean $p$.
2. By linearity of expectation (no independence even needed):

   $$E[X]=E[X_1]+\cdots+E[X_n]=np.$$
3. Since the trials are independent, variances add too: $\operatorname{Var}(X)=np(1-p)$.

*Decomposing into simple pieces, then summing, is the recurring move of probability.*

<a id="s8"></a>
### The Normal distribution & the Central Limit Theorem

*The bell curve, and the theorem that explains why it appears everywhere.*

**The Normal density & standardizing**

$$f(x)=\frac{1}{\sigma\sqrt{2\pi}}\,e^{-\frac{(x-\mu)^2}{2\sigma^2}},\qquad Z=\frac{X-\mu}{\sigma}\sim N(0,1)$$

*Any Normal becomes the **standard Normal** by the z-score from Section 3. That's why one table (or one function) handles them all.*

> **Principle — the empirical (68–95–99.7) rule**
>
> For a Normal distribution, about **68%** of values lie within 1 SD of the mean, **95%** within 2 SD, and **99.7%** within 3 SD. This is why "2 standard errors" later becomes a 95% confidence interval.

> **Principle — the Central Limit Theorem (CLT)**
>
> Take samples of size $n$ from *any* population with mean $\mu$ and SD $\sigma$. As $n$ grows, the distribution of the **sample mean** $\bar X$ becomes approximately Normal — *regardless of the population's shape* — centered at $\mu$ with SD $\sigma/\sqrt n$. This is the single most important result in statistics: it is why Normal-based inference works on skewed, weird, real data.

> **Connection — the spine of all inference**
>
> Normal density (area = probability) → z-scores standardize → CLT makes $\bar X$ Normal → so confidence intervals and z/t-tests in Part C are all just statements about areas under a bell curve.

## Part C · Statistical inference

<a id="s9"></a>
### Sampling distributions & the standard error

*A statistic computed from a random sample is itself random. Its distribution is the key to inference.*

> **Concept — the sampling distribution**
>
> If you took every possible sample of size $n$ and computed $\bar x$ for each, those values would form the **sampling distribution** of the mean. Its spread — the **standard error** — measures how much an estimate bounces around from sample to sample. It is *not* the spread of the data; it is the spread of the *estimate*.

**Standard error of the mean & proportion**

$$\text{SE}(\bar X)=\frac{\sigma}{\sqrt n},\qquad \text{SE}(\hat p)=\sqrt{\frac{p(1-p)}{n}}$$

**Demonstration — why the standard error has a $\sqrt n$**

1. Write the sample mean as a sum: $\bar X=\frac1n(X_1+\cdots+X_n)$, each $X_i$ with variance $\sigma^2$.
2. Use $\operatorname{Var}(aX)=a^2\operatorname{Var}(X)$ and that independent variances add:

   $$\operatorname{Var}(\bar X)=\frac1{n^2}\sum\operatorname{Var}(X_i)=\frac1{n^2}\,(n\sigma^2)=\frac{\sigma^2}{n}.$$
3. Take the square root:

   $$\text{SE}=\frac{\sigma}{\sqrt n}.$$

*To halve your uncertainty you must **quadruple** the sample — the famous diminishing returns of $\sqrt n$.*

<a id="s10"></a>
### Confidence intervals

*An estimate is more honest as a range than a single number. A confidence interval is that range.*

**The general form**

$$\text{estimate}\ \pm\ (\text{critical value})\times\text{SE}$$

$$\bar x \pm z^{*}\frac{\sigma}{\sqrt n}\quad(\sigma\text{ known}),\qquad \bar x \pm t^{*}\frac{s}{\sqrt n}\quad(\sigma\text{ unknown})$$

$$\hat p \pm z^{*}\sqrt{\tfrac{\hat p(1-\hat p)}{n}}$$

> **Concept — what "95% confident" actually means**
>
> It does *not* mean "95% chance the true value is in this interval" (the parameter is fixed, not random). It means: the **procedure** produces intervals that capture the true value 95% of the time across repeated samples. For a 95% interval with large $n$, $z^{*}\approx1.96$ — the "2 SD" of the empirical rule.

> **Connection — why the t-distribution appears**
>
> When $\sigma$ is unknown we estimate it with $s$, adding extra uncertainty. The **t-distribution** is a slightly fatter-tailed Normal that accounts for this; as $n\to\infty$, $s\to\sigma$ and t converges back to the Normal $z$.

<a id="s11"></a>
### Hypothesis testing

*A formal way to ask: is what I observed surprising enough to rule out mere chance?*

> **Concept — the logic of a test**
>
> Assume a **null hypothesis** $H_0$ ("nothing is going on") and ask: if it were true, how likely is data as extreme as mine? If that probability — the **p-value** — is very small, the data is hard to explain by chance, so we reject $H_0$ in favor of the **alternative** $H_a$. It is proof by (probabilistic) contradiction.

**The test statistic & p-value**

$$z=\frac{\bar x-\mu_0}{\sigma/\sqrt n},\qquad t=\frac{\bar x-\mu_0}{s/\sqrt n}$$

*It's a z-score again: how many standard errors the estimate sits from the null value. The p-value is the tail area beyond it. Reject $H_0$ when $p<\alpha$ (typically $\alpha=0.05$).*

**The two errors & power**

$$\text{Type I }(\alpha):\text{ reject a true }H_0,\qquad \text{Type II }(\beta):\text{ fail to reject a false }H_0$$

$$\text{Power}=1-\beta=\text{chance of detecting a real effect}$$

> **Principle — the trade-off you can't escape**
>
> Lowering $\alpha$ (fewer false alarms) raises $\beta$ (more missed effects), and vice versa. Only a **larger sample** shrinks both at once — because it shrinks the standard error. A non-significant result is "not enough evidence," *not* "proof of no effect."

> **Connection — intervals and tests are the same coin**
>
> A two-sided test at level $\alpha$ rejects $H_0:\mu=\mu_0$ exactly when $\mu_0$ falls *outside* the $(1-\alpha)$ confidence interval. Confidence intervals and hypothesis tests are two views of one calculation.

<a id="s12"></a>
### The common tests

*Which test to run is decided by your variable types and number of groups.*

| Test | Use when… | Statistic |
| --- | --- | --- |
| z-test | one mean/proportion, $\sigma$ known or large $n$ | $z=\frac{\bar x-\mu_0}{\sigma/\sqrt n}$ |
| One-sample t | one mean, $\sigma$ unknown | $t=\frac{\bar x-\mu_0}{s/\sqrt n}$ |
| Two-sample t | compare two group means | $t=\frac{\bar x_1-\bar x_2}{\text{SE}}$ |
| Paired t | before/after on the same subjects | t on the differences |
| Chi-square $\chi^2$ | categorical: fit or independence | $\chi^2=\sum\frac{(O-E)^2}{E}$ |
| ANOVA (F-test) | compare 3+ group means | $F=\frac{\text{between-group var}}{\text{within-group var}}$ |

> **Concept — what chi-square and F are really doing**
>
> **Chi-square** compares observed counts $O$ to those expected $E$ under the null; large discrepancies pile up into a big statistic. **ANOVA** asks whether the spread *between* group means is large relative to the natural spread *within* groups — if groups differ more than random noise predicts, at least one mean is different.

## Part D · Relationships between variables

<a id="s13"></a>
### Correlation & regression

*From "are two variables related?" to "draw the best line through them."*

**Covariance & the correlation coefficient**

$$\operatorname{Cov}(X,Y)=E[XY]-E[X]E[Y],\qquad r=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\,\sigma_Y}$$

*$r$ lies in $[-1,1]$: it is the covariance rescaled by both SDs — exactly the average product of the two variables' z-scores. $\pm1$ means perfectly linear; 0 means no linear relationship.*

**The least-squares regression line**

$$\hat y=b_0+b_1x,\qquad b_1=r\,\frac{s_y}{s_x},\qquad b_0=\bar y-b_1\bar x$$

$$R^2=r^2=\text{fraction of variance in }y\text{ explained by }x$$

**Demonstration — deriving the slope by minimizing error (calculus!)**

1. Choose the line that minimizes the total squared residual:

   $$S(b_0,b_1)=\sum_i\big(y_i-b_0-b_1x_i\big)^2.$$
2. This is an optimization problem — set the partial derivatives to zero:

   $$\frac{\partial S}{\partial b_0}=0,\qquad \frac{\partial S}{\partial b_1}=0.$$
3. Solving the two resulting "normal equations" gives

   $$b_1=\frac{\sum(x_i-\bar x)(y_i-\bar y)}{\sum(x_i-\bar x)^2},\qquad b_0=\bar y-b_1\bar x.$$

*Notice the line always passes through $(\bar x,\bar y)$. And this is the calculus optimization of the other guide — derivatives set to zero — applied to data.*

> **Principle — correlation is not causation**
>
> A strong $r$ means two variables move together, not that one causes the other. A hidden **confounding variable** can drive both. Only a randomized experiment — not regression on observational data — can establish cause.

## Part E · Perspective

<a id="s14"></a>
### Pitfalls & the bigger picture

*Knowing the formulas is half the battle; using them honestly is the other half.*

> **Principle — the common traps**
>
> **p-hacking / multiple comparisons:** test enough things and something looks "significant" by luck — so pre-register and adjust. **Significant ≠ important:** a tiny, useless effect can be statistically significant with a huge $n$; always report an **effect size**, not just a p-value. **Sampling bias** beats sample size: a biased million-person poll is worse than a clean thousand-person one.

**Two philosophies of inference**

***Frequentist** (this guide's default): parameters are fixed; probability describes long-run frequencies of procedures (p-values, confidence intervals). **Bayesian**: parameters have probability distributions; you start with a prior belief and update it with data via Bayes' theorem (Section 5) into a posterior. Two valid lenses on the same uncertainty.*

> **The habit to keep**
>
> Trace every inference back to its source of randomness. Behind every confidence interval and p-value sits one engine — the sampling distribution made Normal by the CLT — and behind the whole subject sits one z-score idea: *how far from what we'd expect, measured in standard deviations?*

---

*A first course in statistics and probability — concepts, principles, formulas, and the demonstrations behind them — built as a companion to the Complete Calculus guide. Read once for the shape; return to any box as a reference. Remember: probability runs population → sample; inference runs sample → population.*
