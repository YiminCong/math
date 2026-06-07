# Inference, *from data to truth.*

A rigorous course in mathematical statistics — how a random sample is turned into estimates, intervals, tests, and posterior beliefs about unknown parameters. Every principle is given as a precise definition and every key theorem is **demonstrated**, with the threads to probability and calculus made explicit.

[← Back to all guides](../README.md)

## Part A · Foundations

<a id="s0"></a>
### The big picture: from data to conclusions

*Probability describes a known mechanism producing random data. Inference reverses the arrow: given the data, what was the mechanism?*

In **mathematical statistics** we posit a *statistical model*: a family of probability distributions $\{f(x\mid\theta):\theta\in\Theta\}$ indexed by an unknown parameter $\theta$. We observe data $X_1,\dots,X_n$ drawn from one member of the family, and our job is to say what $\theta$ is. There are three classic deliverables.

- **Point estimation** — a single best guess $\hat\theta$ for $\theta$ (Part B).
- **Interval estimation & testing** — a range for $\theta$ with a stated confidence, or a yes/no decision about a hypothesis (Part C).
- **Prediction / belief updating** — and, in the Bayesian view, a full posterior distribution for $\theta$ (Part D).

> **Principle — the inferential inversion**
>
> Probability runs **parameter $\to$ data**: fix $\theta$, and $f(x\mid\theta)$ tells you how the data behaves. Inference runs **data $\to$ parameter**: fix the data, and ask which $\theta$ is plausible. The *likelihood function* (Section 3) is exactly $f(x\mid\theta)$ read in this reversed direction, and it is the hinge of the entire subject.

#### The whole course on one line

> Model & likelihood → sufficiency → point estimators (MoM, MLE) → evaluate them (bias, MSE, Cramér–Rao, MVUE) → intervals & tests (pivots, Neyman–Pearson, LRT) → Bayes & the bootstrap

> **Connection — building on the intro Statistics guide**
>
> The intro guide introduced $\bar x$, $s^2$, confidence intervals and p-values operationally. This guide supplies the *why*: why divide by $n-1$, why $t$ appears, why $\bar X\pm 1.96\,\sigma/\sqrt n$ is correct, and what makes an estimator "good." It is the theory beneath the recipes.

<a id="s1"></a>
### Populations, samples & sampling distributions

*A statistic is a function of random data, so it is itself a random variable. Its distribution is the object every inference is built on.*

**Random sample (i.i.d.)**

$$X_1,\dots,X_n \ \text{i.i.d.}\ \sim f(x\mid\theta),\qquad \text{joint density } f(\mathbf x\mid\theta)=\prod_{i=1}^n f(x_i\mid\theta)$$

*"i.i.d." = independent and identically distributed. Independence factorizes the joint density into a product — the structural fact that powers likelihood, sufficiency, and the CLT.*

> **Concept — statistic vs estimator vs estimate**
>
> A **statistic** $T=T(X_1,\dots,X_n)$ is any function of the sample that does not depend on $\theta$. An **estimator** is a statistic used to guess a parameter, e.g. $\hat\theta=\bar X$; it is random. Its realized value on observed data, $\hat\theta=4.2$, is an **estimate**. The distribution of an estimator across all possible samples is its **sampling distribution**.

**Mean and variance of the sample mean**

$$E[\bar X]=\mu,\qquad \operatorname{Var}(\bar X)=\frac{\sigma^2}{n},\qquad \text{SE}(\bar X)=\frac{\sigma}{\sqrt n}$$

*The estimator $\bar X$ is centered on the truth and gets tighter as $n$ grows — the seed of consistency (Section 6).*

**Demonstration — sampling distribution of $\bar X$ for a normal sample**

1. Let $X_i\ \text{i.i.d.}\ \sim N(\mu,\sigma^2)$. A linear combination of independent normals is normal, so $\bar X$ is normal.
2. Its mean and variance are computed above: $E[\bar X]=\mu$, $\operatorname{Var}(\bar X)=\sigma^2/n$. Hence

   $$\bar X\sim N\!\left(\mu,\ \frac{\sigma^2}{n}\right),\qquad Z=\frac{\bar X-\mu}{\sigma/\sqrt n}\sim N(0,1).$$
3. For a non-normal population the Central Limit Theorem gives the same limiting form: $Z\xrightarrow{d}N(0,1)$ as $n\to\infty$.

*Exact for normals, asymptotic in general — this single distribution underwrites the $z$- and $t$-intervals of Part C.*

> **Connection — the Probability guide (CLT & MGFs)**
>
> That $\bar X$ is normal for normal data, and asymptotically normal otherwise, is the CLT proved there via moment generating functions. Sampling distributions are just transformations of random variables; the algebra of $E$, $\operatorname{Var}$, and MGFs from probability is the toolkit.

<a id="s2"></a>
### Statistics, sufficiency & the factorization theorem

*Some statistics squeeze every drop of information about $\theta$ out of the data. These sufficient statistics let us compress the sample without losing anything.*

> **Concept — sufficiency**
>
> A statistic $T$ is **sufficient** for $\theta$ if the conditional distribution of the data given $T$ does not depend on $\theta$. Intuitively: once you know $T$, the rest of the sample is "noise" carrying no further information about $\theta$. For a normal sample, $(\sum X_i,\sum X_i^2)$ is sufficient — the individual order of the data is irrelevant.

**Fisher–Neyman factorization theorem**

$$T \text{ is sufficient for }\theta \iff f(\mathbf x\mid\theta)=g\big(T(\mathbf x),\theta\big)\,h(\mathbf x)$$

*The joint density factors into a piece $g$ that touches $\theta$ only through $T$, times a piece $h$ free of $\theta$. Read off $T$ by isolating where $\theta$ and the data meet.*

**Demonstration — a sufficient statistic for Bernoulli $p$ via factorization**

1. For $X_i\ \text{i.i.d.}\ \sim\text{Bernoulli}(p)$, the joint pmf is

   $$f(\mathbf x\mid p)=\prod_{i=1}^n p^{x_i}(1-p)^{1-x_i}=p^{\sum x_i}(1-p)^{\,n-\sum x_i}.$$
2. This depends on the data only through $T=\sum_{i=1}^n x_i$. Write $g(T,p)=p^{T}(1-p)^{n-T}$ and $h(\mathbf x)=1$.
3. By the factorization theorem, $T=\sum X_i$ (equivalently $\bar X$) is sufficient for $p$.

*Knowing the total number of successes is as good as knowing the full sequence of $0$s and $1$s.*

> **Principle — minimal sufficiency & completeness**
>
> A **minimal** sufficient statistic is the coarsest sufficient summary — a function of every other sufficient statistic. A statistic is **complete** if no nonzero function of it has expectation $0$ for all $\theta$; completeness is the technical ingredient that makes the Rao–Blackwell estimator (Section 8) the *unique* best one.

> **Connection — the exponential family**
>
> Many distributions (normal, Bernoulli, Poisson, exponential, gamma) belong to the **exponential family** $f(x\mid\theta)=h(x)\exp\{\eta(\theta)T(x)-A(\theta)\}$. Factorization is then immediate, and $\sum T(X_i)$ is automatically a complete sufficient statistic — a unifying thread through estimation theory.

<a id="s3"></a>
### The likelihood function

*Flip the joint density around: treat the data as fixed and $\theta$ as the variable. That re-reading is the likelihood, and almost everything follows from it.*

**Likelihood and log-likelihood**

$$L(\theta)=f(\mathbf x\mid\theta)=\prod_{i=1}^n f(x_i\mid\theta),\qquad \ell(\theta)=\log L(\theta)=\sum_{i=1}^n \log f(x_i\mid\theta)$$

*$L(\theta)$ is *not* a probability distribution over $\theta$; it need not integrate to one. It ranks values of $\theta$ by how well they explain the observed data.*

> **Principle — the likelihood principle**
>
> All the information the data carry about $\theta$ is contained in the likelihood function. Two experiments yielding proportional likelihoods should lead to the same inference about $\theta$. The log turns the product into a sum, which is why the **score function** $\ell'(\theta)$ and Fisher information (Section 7) are additive over independent observations.

**The score function**

$$U(\theta)=\frac{\partial}{\partial\theta}\ell(\theta)=\sum_{i=1}^n \frac{\partial}{\partial\theta}\log f(x_i\mid\theta),\qquad E_\theta[U(\theta)]=0$$

*The score has mean zero at the true $\theta$. Setting it to zero locates the maximum of the likelihood — pure calculus optimization.*

**Demonstration — the score has expectation zero**

1. Since $\int f(x\mid\theta)\,dx=1$ for every $\theta$, differentiate both sides with respect to $\theta$ (regularity lets us pass the derivative inside):

   $$\int \frac{\partial}{\partial\theta} f(x\mid\theta)\,dx=0.$$
2. Use the identity $\frac{\partial}{\partial\theta} f = f\cdot\frac{\partial}{\partial\theta}\log f$:

   $$\int \Big(\frac{\partial}{\partial\theta}\log f(x\mid\theta)\Big) f(x\mid\theta)\,dx=0.$$
3. The left side is exactly $E_\theta\!\big[\frac{\partial}{\partial\theta}\log f(X\mid\theta)\big]$, so $E_\theta[U(\theta)]=0$.

*This little lemma is the workhorse behind both the MLE's consistency and the Cramér–Rao bound.*

> **Connection — calculus: optimization is setting the score to zero**
>
> Maximizing $\ell(\theta)$ is the calculus problem "find the critical point": solve $\ell'(\theta)=0$ and check $\ell''(\theta)\lt 0$. The negative second derivative $-\ell''$ measures how sharply the likelihood peaks — and that curvature *is* the observed Fisher information.

## Part B · Point estimation

<a id="s4"></a>
### The method of moments

*The oldest recipe for an estimator: match the theoretical moments of the model to the empirical moments of the data, then solve.*

**Method of moments (MoM)**

$$\text{set } \mu_k(\theta)=E_\theta[X^k] \ \text{equal to}\ m_k=\frac1n\sum_{i=1}^n X_i^k,\quad k=1,2,\dots$$

*Use as many moment equations as there are unknown parameters, then solve for $\theta$. Simple, always available, but rarely optimal.*

**Demonstration — MoM estimators for Poisson, Bernoulli & normal**

1. Poisson($\lambda$): $E[X]=\lambda$. Match to $\bar X$: $\hat\lambda_{\text{MoM}}=\bar X$.
2. Bernoulli($p$): $E[X]=p$. Match to $\bar X$: $\hat p_{\text{MoM}}=\bar X$.
3. Normal($\mu,\sigma^2$): first moment $E[X]=\mu$ gives $\hat\mu=\bar X$; second moment $E[X^2]=\sigma^2+\mu^2$ matched to $\frac1n\sum X_i^2$ gives

   $$\hat\sigma^2_{\text{MoM}}=\frac1n\sum_{i=1}^n X_i^2-\bar X^2=\frac1n\sum_{i=1}^n (X_i-\bar X)^2.$$

*Note the divisor is $n$, not $n-1$: the MoM variance is biased downward (see Section 6).*

> **Principle — when to reach for MoM**
>
> MoM shines when the likelihood is awkward to maximize or as a starting value for iterative MLE. It is consistent under mild conditions but generally less efficient than the MLE: it ignores the full shape of the likelihood, using only a few moments.

<a id="s5"></a>
### Maximum likelihood estimation

*Pick the parameter value that makes the observed data most probable. The MLE is the dominant estimator in modern statistics.*

**The maximum likelihood estimator**

$$\hat\theta_{\text{MLE}}=\arg\max_{\theta\in\Theta} L(\theta)=\arg\max_{\theta\in\Theta} \ell(\theta),\qquad \text{solve } U(\theta)=\ell'(\theta)=0$$

*Maximizing $\ell$ is equivalent to maximizing $L$ (log is increasing) but turns products into sums. Confirm a maximum with $\ell''(\hat\theta)\lt 0$.*

**Demonstration — MLE for Bernoulli $p$**

1. Log-likelihood: $\ell(p)=\big(\sum x_i\big)\log p+\big(n-\sum x_i\big)\log(1-p)$.
2. Score to zero:

   $$\ell'(p)=\frac{\sum x_i}{p}-\frac{n-\sum x_i}{1-p}=0.$$
3. Solve: $(1-p)\sum x_i=p\,(n-\sum x_i)\Rightarrow \sum x_i=pn$, so

   $$\hat p_{\text{MLE}}=\frac{1}{n}\sum_{i=1}^n x_i=\bar X.$$

*Here MLE and MoM coincide; in general they differ.*

**Demonstration — MLE for normal $(\mu,\sigma^2)$**

1. $\ell(\mu,\sigma^2)=-\frac n2\log(2\pi)-\frac n2\log\sigma^2-\frac{1}{2\sigma^2}\sum(x_i-\mu)^2$.
2. $\partial\ell/\partial\mu=\frac{1}{\sigma^2}\sum(x_i-\mu)=0\Rightarrow \hat\mu=\bar X$.
3. $\partial\ell/\partial\sigma^2=-\frac{n}{2\sigma^2}+\frac{1}{2\sigma^4}\sum(x_i-\mu)^2=0\Rightarrow$

   $$\hat\sigma^2_{\text{MLE}}=\frac1n\sum_{i=1}^n (x_i-\bar X)^2.$$

*Again the divisor is $n$. The MLE of the variance is biased — quantified next section.*

> **Principle — why the MLE is so prized**
>
> Under regularity conditions the MLE is **consistent**, **asymptotically normal**, and **asymptotically efficient** — it attains the Cramér–Rao bound in the limit (Section 7). It is also **invariant**: the MLE of $g(\theta)$ is $g(\hat\theta_{\text{MLE}})$. Its single weakness is finite-sample bias.

**Asymptotic normality of the MLE**

$$\sqrt n\,(\hat\theta_{\text{MLE}}-\theta)\ \xrightarrow{d}\ N\!\Big(0,\ \frac{1}{I_1(\theta)}\Big)$$

*$I_1(\theta)$ is the Fisher information in one observation (Section 7). This is the engine of Wald intervals and tests.*

> **Connection — calculus optimization, applied to data**
>
> Finding $\hat\theta_{\text{MLE}}$ is the same "set the derivative to zero, check the second derivative" routine from calculus, now applied to $\ell(\theta)$. When no closed form exists, numerical methods (Newton–Raphson, which uses $\ell''$) take over — and $\ell''$ is again the information.

<a id="s6"></a>
### Evaluating estimators: bias, variance, MSE & consistency

*An estimator is a random variable; we judge it by where it centers, how much it scatters, and whether it homes in on the truth as data accumulate.*

**Bias, variance and mean squared error**

$$\operatorname{Bias}(\hat\theta)=E[\hat\theta]-\theta,\qquad \operatorname{MSE}(\hat\theta)=E\big[(\hat\theta-\theta)^2\big]$$

$$\operatorname{MSE}(\hat\theta)=\operatorname{Var}(\hat\theta)+\big[\operatorname{Bias}(\hat\theta)\big]^2$$

*An estimator is **unbiased** when $E[\hat\theta]=\theta$. MSE trades off scatter against systematic offset — sometimes a little bias buys a lot less variance.*

**Demonstration — the bias–variance decomposition of MSE**

1. Insert and subtract $E[\hat\theta]$: $(\hat\theta-\theta)=(\hat\theta-E[\hat\theta])+(E[\hat\theta]-\theta)$.
2. Square and take expectation:

   $$E[(\hat\theta-\theta)^2]=E[(\hat\theta-E\hat\theta)^2]+2(E\hat\theta-\theta)E[\hat\theta-E\hat\theta]+(E\hat\theta-\theta)^2.$$
3. The cross term vanishes because $E[\hat\theta-E\hat\theta]=0$, leaving $\operatorname{MSE}=\operatorname{Var}+\operatorname{Bias}^2$.

*The same "add and subtract the mean" move as $\operatorname{Var}(X)=E[X^2]-(E[X])^2$.*

**Demonstration — the MLE of normal variance is biased, with its MSE**

1. Recall $\hat\sigma^2_{\text{MLE}}=\frac1n\sum(X_i-\bar X)^2=\frac{n-1}{n}S^2$, where $S^2=\frac{1}{n-1}\sum(X_i-\bar X)^2$ is the unbiased version.
2. A key sampling fact for normals: $\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}$, so $E[S^2]=\sigma^2$ and $\operatorname{Var}(S^2)=\frac{2\sigma^4}{n-1}$.
3. Hence $E[\hat\sigma^2_{\text{MLE}}]=\frac{n-1}{n}\sigma^2$, giving bias

   $$\operatorname{Bias}=\frac{n-1}{n}\sigma^2-\sigma^2=-\frac{\sigma^2}{n}.$$
4. Variance: $\operatorname{Var}(\hat\sigma^2_{\text{MLE}})=\big(\tfrac{n-1}{n}\big)^2\frac{2\sigma^4}{n-1}=\frac{2(n-1)\sigma^4}{n^2}$. Adding bias squared,

   $$\operatorname{MSE}(\hat\sigma^2_{\text{MLE}})=\frac{2(n-1)\sigma^4}{n^2}+\frac{\sigma^4}{n^2}=\frac{(2n-1)\,\sigma^4}{n^2}.$$

*Strikingly, $\hat\sigma^2_{\text{MLE}}$ has *smaller* MSE than the unbiased $S^2$ (whose MSE is $2\sigma^4/(n-1)$): a textbook case where bias pays.*

> **Principle — consistency**
>
> An estimator is **consistent** if $\hat\theta_n\xrightarrow{p}\theta$ as $n\to\infty$. A sufficient condition is $\operatorname{MSE}(\hat\theta_n)\to 0$ (mean-square consistency, via Chebyshev). Both the biased and unbiased variance estimators are consistent, since their bias and variance each vanish — bias matters in small samples, not the limit.

> **Connection — the intro guide's $n-1$ finally explained**
>
> The intro guide simply asserted "divide by $n-1$ so that $E[S^2]=\sigma^2$." Here we see exactly why: the MLE divisor $n$ is biased by $-\sigma^2/n$, and the $n-1$ (Bessel) correction removes it. The "lost degree of freedom" is the $\chi^2_{n-1}$ above.

<a id="s7"></a>
### Fisher information & the Cramér–Rao lower bound

*There is a hard floor on how precise any unbiased estimator can be. Fisher information measures how much a sample tells you about $\theta$; its reciprocal is that floor.*

**Fisher information**

$$I(\theta)=E\!\left[\Big(\frac{\partial}{\partial\theta}\log f(X\mid\theta)\Big)^2\right]=-\,E\!\left[\frac{\partial^2}{\partial\theta^2}\log f(X\mid\theta)\right]$$

$$I_n(\theta)=n\,I_1(\theta)\quad\text{(information adds over i.i.d. observations)}$$

*Information is the variance of the score, equivalently the expected curvature of the log-likelihood. A sharply peaked likelihood means high information means precise estimation.*

**Demonstration — Fisher information for Bernoulli $p$**

1. One observation: $\log f(x\mid p)=x\log p+(1-x)\log(1-p)$.
2. Score: $\frac{\partial}{\partial p}\log f=\frac{x}{p}-\frac{1-x}{1-p}$. Second derivative: $-\frac{x}{p^2}-\frac{1-x}{(1-p)^2}$.
3. Take $-E[\cdot]$ with $E[X]=p$:

   $$I_1(p)=\frac{p}{p^2}+\frac{1-p}{(1-p)^2}=\frac1p+\frac1{1-p}=\frac{1}{p(1-p)}.$$

*So $I_n(p)=n/[p(1-p)]$ — the more extreme $p$, the more informative each trial.*

**Cramér–Rao lower bound (CRLB)**

$$\text{for any unbiased }\hat\theta:\qquad \operatorname{Var}(\hat\theta)\ \ge\ \frac{1}{I_n(\theta)}=\frac{1}{n\,I_1(\theta)}$$

*No unbiased estimator can beat this variance. One that attains it is **efficient**; its **relative efficiency** is the ratio of the bound to its actual variance.*

**Demonstration — sketch of the Cramér–Rao bound**

1. Let $\hat\theta$ be unbiased and $U=U(\theta)$ the score, with $E[U]=0$ and $\operatorname{Var}(U)=I_n(\theta)$.
2. Differentiating $E[\hat\theta]=\theta$ under the integral gives $\operatorname{Cov}(\hat\theta,U)=1$.
3. Cauchy–Schwarz: $1=\operatorname{Cov}(\hat\theta,U)^2\le \operatorname{Var}(\hat\theta)\,\operatorname{Var}(U)=\operatorname{Var}(\hat\theta)\,I_n(\theta)$.
4. Rearrange:

   $$\operatorname{Var}(\hat\theta)\ge\frac{1}{I_n(\theta)}.$$

*Illustration: for Bernoulli, $\hat p=\bar X$ has $\operatorname{Var}=p(1-p)/n=1/I_n(p)$ — it attains the bound exactly, so $\bar X$ is efficient.*

> **Connection — curvature, calculus & the MLE**
>
> The form $I=-E[\ell'']$ is literally the expected second derivative — the calculus measure of how curved the log-likelihood is at its peak. This is why the MLE's asymptotic variance is $1/I_n(\theta)$: a curvier likelihood pins $\theta$ down more tightly.

<a id="s8"></a>
### Rao–Blackwell & minimum-variance unbiased estimators

*Given any unbiased estimator, conditioning on a sufficient statistic can only improve it. With completeness, this yields the unique best unbiased estimator.*

**Rao–Blackwell theorem**

$$\text{if } E[\tilde\theta]=\theta \text{ and } T \text{ is sufficient, then } \hat\theta=E[\tilde\theta\mid T] \text{ satisfies } E[\hat\theta]=\theta,\quad \operatorname{Var}(\hat\theta)\le \operatorname{Var}(\tilde\theta)$$

*Conditioning on a sufficient statistic preserves unbiasedness and never increases variance — "Rao–Blackwellizing" an estimator.*

**Demonstration — Rao–Blackwellize a crude Poisson estimator**

1. Let $X_1,\dots,X_n\ \text{i.i.d.}\ \sim\text{Poisson}(\lambda)$; we want to estimate $g(\lambda)=e^{-\lambda}=P(X=0)$.
2. A crude unbiased estimator: $\tilde g=\mathbf{1}\{X_1=0\}$, since $E[\tilde g]=P(X_1=0)=e^{-\lambda}$. But it uses only one observation — wasteful.
3. The total $T=\sum X_i$ is sufficient (and complete). Rao–Blackwellize: $\hat g=E[\mathbf 1\{X_1=0\}\mid T]=P(X_1=0\mid T)$.
4. Given $T=t$, the conditional distribution of $X_1$ is $\text{Binomial}(t,1/n)$, so

   $$\hat g=P(X_1=0\mid T=t)=\Big(1-\tfrac1n\Big)^{t}=\Big(\tfrac{n-1}{n}\Big)^{\sum X_i}.$$

*This improved estimator is unbiased with smaller variance — and, by completeness, it is the unique MVUE of $e^{-\lambda}$.*

**Lehmann–Scheffé theorem (MVUE)**

$$T \text{ complete \& sufficient},\ \ E[\,\varphi(T)\,]=\theta \ \Longrightarrow\ \varphi(T) \text{ is the unique MVUE of }\theta$$

*If an unbiased function of a complete sufficient statistic exists, it is *the* minimum-variance unbiased estimator. Completeness guarantees uniqueness.*

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

**Pivotal quantity**

$$Q(\mathbf X,\theta)\ \text{is a pivot if its distribution does not depend on }\theta.$$

*From $P(a\le Q\le b)=1-\alpha$, algebraically isolate $\theta$ to get a random interval that covers $\theta$ with probability $1-\alpha$.*

**Demonstration — CI for a normal mean, $\sigma$ known**

1. Pivot: $Z=\dfrac{\bar X-\mu}{\sigma/\sqrt n}\sim N(0,1)$, free of $\mu$.
2. Bracket it: $P\big(-z_{\alpha/2}\le Z\le z_{\alpha/2}\big)=1-\alpha$.
3. Solve the inequalities for $\mu$:

   $$\bar X-z_{\alpha/2}\frac{\sigma}{\sqrt n}\ \le\ \mu\ \le\ \bar X+z_{\alpha/2}\frac{\sigma}{\sqrt n}.$$

*For $\alpha=0.05$, $z_{\alpha/2}=1.96$ — the "two standard errors" of the empirical rule.*

**Demonstration — CI for a normal mean, $\sigma$ unknown (the $t$ pivot)**

1. Replace $\sigma$ by $S$. The pivot $T=\dfrac{\bar X-\mu}{S/\sqrt n}$ is no longer normal: numerator $N(0,1)$ over an independent $\sqrt{\chi^2_{n-1}/(n-1)}$.
2. By definition that ratio is Student's $t$ with $n-1$ degrees of freedom: $T\sim t_{n-1}$, still free of $\mu$ and $\sigma$.
3. Invert:

   $$\bar X\ \pm\ t_{n-1,\,\alpha/2}\,\frac{S}{\sqrt n}.$$

*The fatter $t$ tails are the price of estimating $\sigma$; as $n\to\infty$, $t_{n-1}\to N(0,1)$.*

> **Principle — what confidence means**
>
> Confidence is a property of the **procedure**, not of one interval. "95% confidence" means: across repeated samples, the random interval covers the fixed $\theta$ $95\%$ of the time. Once computed, a particular interval either contains $\theta$ or not — there is no probability left.

> **Connection — pivots unify the intro guide's intervals**
>
> Every CI in the intro guide — for a mean, a proportion, a variance (using a $\chi^2$ pivot) — is one pivot inverted. The recipe "estimate $\pm$ critical value $\times$ SE" is the special case where the pivot is approximately $N(0,1)$.

<a id="s10"></a>
### Hypothesis testing: errors, power & the Neyman–Pearson lemma

*A test partitions the data space into "reject" and "don't reject." Among all level-$\alpha$ tests, which is most powerful? For simple hypotheses, Neyman–Pearson gives the exact answer.*

**Errors, size and power**

$$\alpha=P_{\theta_0}(\text{reject }H_0)\ \text{(Type I)},\qquad \beta=P_{\theta_1}(\text{fail to reject }H_0)\ \text{(Type II)}$$

$$\text{power}=1-\beta=P_{\theta_1}(\text{reject }H_0)$$

*A test has **size** $\alpha$ (max Type I rate) and a **power function** $\beta(\theta)=P_\theta(\text{reject})$. We fix $\alpha$ and maximize power.*

**Neyman–Pearson lemma**

$$\text{For }H_0:\theta=\theta_0 \text{ vs } H_1:\theta=\theta_1,\ \text{the most powerful size-}\alpha\text{ test rejects when } \frac{L(\theta_1)}{L(\theta_0)}\ge k.$$

*The likelihood ratio is the optimal test statistic for two simple hypotheses; choose $k$ so the size equals $\alpha$.*

**Demonstration — Neyman–Pearson optimality**

1. Let $\phi^*$ be the likelihood-ratio (LR) test rejecting when $L(\theta_1)\ge k\,L(\theta_0)$, with size exactly $\alpha$. Let $\phi$ be any other test of size $\le\alpha$.
2. Consider $(\phi^*-\phi)\big(L(\theta_1)-kL(\theta_0)\big)$. Where $\phi^*=1$ the second factor is $\ge0$; where $\phi^*=0$ it is $\le0$; in both regions the product is $\ge0$. So

   $$\int (\phi^*-\phi)\big(L(\theta_1)-kL(\theta_0)\big)\,d\mathbf x\ \ge\ 0.$$
3. Split: $\big[\text{power}(\phi^*)-\text{power}(\phi)\big]-k\big[\text{size}(\phi^*)-\text{size}(\phi)\big]\ge0$. Since $\text{size}(\phi)\le\alpha=\text{size}(\phi^*)$, the bracket on the right is $\ge0$.
4. Therefore $\text{power}(\phi^*)\ge\text{power}(\phi)$: the LR test is most powerful.

*Optimality of the likelihood ratio is the seed of every test in the next section.*

**Demonstration — the most powerful test for a normal mean**

1. $X_i\sim N(\mu,\sigma^2)$, $\sigma$ known, $H_0:\mu=\mu_0$ vs $H_1:\mu=\mu_1$ with $\mu_1\gt\mu_0$.
2. The LR is monotone in $\bar X$: $\log\frac{L(\mu_1)}{L(\mu_0)}=\frac{n(\mu_1-\mu_0)}{\sigma^2}\bar X+\text{const}$. Rejecting for large LR $\iff$ rejecting for large $\bar X$.
3. So reject when $\bar X\ge c$; choose $c$ so the size is $\alpha$: $c=\mu_0+z_\alpha\,\sigma/\sqrt n$. Equivalently reject when $Z=\frac{\bar X-\mu_0}{\sigma/\sqrt n}\ge z_\alpha$.

*The familiar one-sided $z$-test is the Neyman–Pearson optimal test — and since the rejection rule doesn't depend on the specific $\mu_1$, it is **uniformly most powerful** against all $\mu\gt\mu_0$.*

> **Connection — tests and intervals are duals**
>
> A level-$\alpha$ two-sided test of $H_0:\theta=\theta_0$ rejects exactly when $\theta_0$ lies outside the $1-\alpha$ confidence interval. The acceptance region of a test, inverted, *is* a confidence set — the same duality the intro guide hinted at, now exact.

<a id="s11"></a>
### Likelihood-ratio, Wald & score tests

*For composite hypotheses and many parameters, three asymptotically equivalent tests dominate — all built from the likelihood, all approximately $\chi^2$.*

**The generalized likelihood-ratio statistic**

$$\Lambda=\frac{\sup_{\theta\in\Theta_0} L(\theta)}{\sup_{\theta\in\Theta} L(\theta)},\qquad -2\log\Lambda\ \xrightarrow{d}\ \chi^2_{r}$$

*$r$ is the number of restrictions imposed by $H_0$ (the drop in free parameters). Reject for large $-2\log\Lambda$. This limit is **Wilks' theorem**.*

**Demonstration — an LRT and its $\chi^2_1$ limit (Wilks)**

1. Normal sample, $\sigma$ known; test $H_0:\mu=\mu_0$ vs $H_1:\mu\ne\mu_0$. Numerator maximizes $L$ at $\mu_0$; denominator at $\hat\mu=\bar X$.
2. Plug into the normal likelihood:

   $$-2\log\Lambda=\frac{1}{\sigma^2}\Big[\sum(x_i-\mu_0)^2-\sum(x_i-\bar X)^2\Big]=\frac{n(\bar X-\mu_0)^2}{\sigma^2}.$$
3. But $\frac{\sqrt n(\bar X-\mu_0)}{\sigma}\sim N(0,1)$ under $H_0$, so its square is exactly $\chi^2_1$:

   $$-2\log\Lambda=\Big(\tfrac{\bar X-\mu_0}{\sigma/\sqrt n}\Big)^2=Z^2\sim\chi^2_1.$$

*Here Wilks' $\chi^2_1$ is exact (one restriction, $r=1$); in general it holds asymptotically.*

**Wald and score (Rao) tests**

$$W=\frac{(\hat\theta-\theta_0)^2}{\widehat{\operatorname{Var}}(\hat\theta)}=I_n(\hat\theta)\,(\hat\theta-\theta_0)^2,\qquad R=\frac{U(\theta_0)^2}{I_n(\theta_0)}$$

*Both $\xrightarrow{d}\chi^2_r$. **Wald** uses the MLE and curvature at $\hat\theta$; **score** uses the slope of $\ell$ at $\theta_0$ and needs no MLE. LRT, Wald, and score agree asymptotically.*

> **Principle — three views of one peak**
>
> Picture the log-likelihood near its maximum. The **LRT** measures the vertical drop in $\ell$ from $\hat\theta$ to $\theta_0$; the **Wald** test measures the horizontal distance $\hat\theta-\theta_0$; the **score** test measures the slope of $\ell$ at $\theta_0$. For a quadratic (normal) log-likelihood all three coincide exactly; in general they differ only in finite samples.

> **Connection — Cramér–Rao made operational**
>
> The Wald variance $1/I_n(\hat\theta)$ is the Cramér–Rao bound evaluated at the MLE — Section 7 returning as the standard error in the denominator. The score test uses $U(\theta_0)$ and $I_n(\theta_0)$ directly: the very quantities defined in Section 3 and 7.

<a id="s12"></a>
### The standard tests & their sampling distributions (t, χ², F)

*Three distributions, all spawned by sampling from a normal population, supply the exact tests of classical statistics.*

**How the three arise from a normal sample**

$$Z=\frac{\bar X-\mu}{\sigma/\sqrt n}\sim N(0,1),\qquad \frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}$$

$$t_k=\frac{Z}{\sqrt{\chi^2_k/k}},\qquad F_{d_1,d_2}=\frac{\chi^2_{d_1}/d_1}{\chi^2_{d_2}/d_2}$$

*$\bar X\perp S^2$ for a normal sample (independence of mean and variance) — this is what makes the $t$ ratio's numerator and denominator independent.*

| Distribution | Definition | Used for | Test statistic |
| --- | --- | --- | --- |
| $t_k$ | $N(0,1)\big/\sqrt{\chi^2_k/k}$ | mean(s), $\sigma$ unknown; regression coefficients | $t=\dfrac{\bar X-\mu_0}{S/\sqrt n}$ |
| $\chi^2_k$ | sum of $k$ squared $N(0,1)$ | variance; goodness-of-fit; independence; LRT/Wald/score limits | $\dfrac{(n-1)S^2}{\sigma_0^2}$, $\ \sum\dfrac{(O-E)^2}{E}$ |
| $F_{d_1,d_2}$ | ratio of two scaled $\chi^2$ | compare two variances; ANOVA (3+ means) | $F=\dfrac{S_1^2}{S_2^2}$, $\ \dfrac{\text{MS}_{\text{between}}}{\text{MS}_{\text{within}}}$ |

**Demonstration — the one-sample $t$ statistic is genuinely $t_{n-1}$**

1. Write $\dfrac{\bar X-\mu}{S/\sqrt n}=\dfrac{(\bar X-\mu)/(\sigma/\sqrt n)}{S/\sigma}$. Numerator is $N(0,1)$.
2. Denominator: $S/\sigma=\sqrt{\dfrac{S^2}{\sigma^2}}=\sqrt{\dfrac{\chi^2_{n-1}/(n-1)\cdot\sigma^2}{\sigma^2}}=\sqrt{\chi^2_{n-1}/(n-1)}$, independent of the numerator.
3. That is exactly $\dfrac{N(0,1)}{\sqrt{\chi^2_{n-1}/(n-1)}}$, the definition of $t_{n-1}$.

*The $t$ distribution is not an approximation here — it is the exact sampling law, and the reason the intro guide's "use $t$ when $\sigma$ is unknown" is correct.*

> **Connection — the Probability guide's distributions, put to work**
>
> The $\chi^2$, $t$, and $F$ defined abstractly in the Probability guide are exactly the sampling distributions of normal-data statistics. Classical inference is, in large part, bookkeeping with these three laws.

## Part D · Bayesian & nonparametric

<a id="s13"></a>
### Bayesian inference: priors, posteriors & conjugacy

*Treat $\theta$ itself as random. Encode beliefs in a prior, update with data via Bayes' theorem, and read off the posterior — a full distribution for $\theta$.*

**Bayes' theorem for parameters**

$$\pi(\theta\mid\mathbf x)=\frac{L(\theta)\,\pi(\theta)}{\int L(\theta)\,\pi(\theta)\,d\theta}\ \propto\ \underbrace{L(\theta)}_{\text{likelihood}}\ \underbrace{\pi(\theta)}_{\text{prior}}$$

*Posterior $\propto$ likelihood $\times$ prior. The denominator (the marginal/evidence) is just the normalizing constant.*

> **Concept — conjugacy**
>
> A prior is **conjugate** to a likelihood if the posterior belongs to the same family as the prior. Conjugate pairs make the update purely algebraic — no integration needed — and reveal the data's effect as a change of the family's parameters.

| Likelihood | Conjugate prior | Posterior |
| --- | --- | --- |
| Bernoulli / Binomial($p$) | Beta($\alpha,\beta$) | Beta($\alpha+\sum x_i,\ \beta+n-\sum x_i$) |
| Poisson($\lambda$) | Gamma($\alpha,\beta$) | Gamma($\alpha+\sum x_i,\ \beta+n$) |
| Normal mean ($\sigma^2$ known) | Normal($\mu_0,\tau_0^2$) | Normal (precision-weighted, below) |
| Normal precision ($\mu$ known) | Gamma | Gamma |
| Exponential($\lambda$) | Gamma($\alpha,\beta$) | Gamma($\alpha+n,\ \beta+\sum x_i$) |
| Multinomial | Dirichlet | Dirichlet |

**Demonstration — the Beta–Bernoulli update**

1. Prior $\pi(p)\propto p^{\alpha-1}(1-p)^{\beta-1}$ (Beta), likelihood $L(p)\propto p^{\sum x_i}(1-p)^{n-\sum x_i}$.
2. Multiply:

   $$\pi(p\mid\mathbf x)\propto p^{\alpha+\sum x_i-1}(1-p)^{\beta+n-\sum x_i-1}.$$
3. This is the kernel of $\text{Beta}\big(\alpha+\sum x_i,\ \beta+n-\sum x_i\big)$ — same family, parameters bumped by the counts of successes and failures.

*The prior parameters $(\alpha,\beta)$ act like "pseudo-counts" of prior successes and failures.*

> **Connection — Bayes' theorem from the Probability guide**
>
> This is the very same Bayes' theorem used for events, lifted to densities: $P(A\mid B)\propto P(B\mid A)P(A)$ becomes $\pi(\theta\mid x)\propto f(x\mid\theta)\pi(\theta)$. Frequentist and Bayesian inference share the likelihood; they differ only in whether $\theta$ gets a probability distribution.

<a id="s14"></a>
### Bayesian estimation & credible intervals

*From the posterior we extract point estimates and intervals — and the famous normal–normal update shows the posterior mean is a precision-weighted average of prior and data.*

**Posterior point estimates**

$$\hat\theta_{\text{Bayes}}=E[\theta\mid\mathbf x]\ \text{(posterior mean, min. squared-error loss)},\qquad \hat\theta_{\text{MAP}}=\arg\max_\theta \pi(\theta\mid\mathbf x)$$

*The posterior mean minimizes expected squared-error loss; the posterior median minimizes absolute loss; the MAP (mode) is the Bayesian analogue of the MLE with a prior penalty.*

**Demonstration — normal prior is conjugate; posterior mean is precision-weighted**

1. Data $\bar X\mid\mu\sim N(\mu,\sigma^2/n)$ ($\sigma$ known), prior $\mu\sim N(\mu_0,\tau_0^2)$. Multiply the two normal kernels and complete the square in $\mu$.
2. The exponent is quadratic in $\mu$, so the posterior is normal: $\mu\mid\mathbf x\sim N(\mu_n,\tau_n^2)$ with precision adding,

   $$\frac{1}{\tau_n^2}=\frac{1}{\tau_0^2}+\frac{n}{\sigma^2}.$$
3. The posterior mean is the precision-weighted average of prior mean and sample mean:

   $$\mu_n=\frac{\frac{1}{\tau_0^2}\,\mu_0+\frac{n}{\sigma^2}\,\bar X}{\frac{1}{\tau_0^2}+\frac{n}{\sigma^2}}.$$

*As $n\to\infty$ the data precision $n/\sigma^2$ dominates, $\mu_n\to\bar X$, and the prior washes out — Bayesian and frequentist estimates converge.*

**Credible interval**

$$P\big(\theta\in C\mid\mathbf x\big)=1-\alpha,\qquad \text{e.g. } [\,q_{\alpha/2},\,q_{1-\alpha/2}\,]\ \text{of the posterior}$$

*Unlike a confidence interval, this *is* a direct probability statement about $\theta$ given the data — the interpretation people wrongly attach to confidence intervals.*

> **Principle — credible vs confidence**
>
> A 95% **credible** interval says "given the data and prior, $\theta$ lies here with probability 0.95." A 95% **confidence** interval makes a long-run frequency claim about the procedure. With a flat prior and a symmetric likelihood the two often numerically coincide, but their meanings differ sharply.

> **Connection — regularization is a prior**
>
> The MAP estimate with a normal prior on $\mu$ is exactly ridge-style shrinkage of $\bar X$ toward $\mu_0$. Penalized likelihood methods are MAP estimation in disguise — a bridge between Bayesian priors and the optimization view of estimation.

<a id="s15"></a>
### Nonparametric methods & the bootstrap

*When you won't assume a parametric model, let the data stand in for the population. The empirical distribution and resampling do the heavy lifting.*

**The empirical distribution function**

$$\hat F_n(x)=\frac1n\sum_{i=1}^n \mathbf 1\{X_i\le x\}\ \xrightarrow{\text{a.s.}}\ F(x)\quad(\text{Glivenko–Cantelli, uniformly})$$

*$\hat F_n$ is the nonparametric MLE of $F$. Plug-in estimators replace $F$ by $\hat F_n$: the sample mean estimates the population mean, the sample median the population median, and so on.*

> **Concept — the bootstrap idea**
>
> To gauge the variability of a statistic $\hat\theta=T(\hat F_n)$ without a formula, treat the sample as the population: resample from it and watch how $\hat\theta$ varies. The **plug-in principle** — replace $F$ by $\hat F_n$ — is the whole trick.

**Demonstration — the nonparametric bootstrap for a standard error**

1. From the observed sample $\{x_1,\dots,x_n\}$, draw a resample of size $n$ with replacement: $\{x_1^*,\dots,x_n^*\}$.
2. Compute the statistic on the resample, $\hat\theta^{*(b)}=T(x_1^*,\dots,x_n^*)$ (e.g. the sample median).
3. Repeat for $b=1,\dots,B$ (say $B=2000$) to get $\hat\theta^{*(1)},\dots,\hat\theta^{*(B)}$.
4. Estimate the standard error by the spread of the bootstrap replicates:

   $$\widehat{\text{SE}}_{\text{boot}}=\sqrt{\frac{1}{B-1}\sum_{b=1}^B\big(\hat\theta^{*(b)}-\bar{\hat\theta}^{*}\big)^2}.$$
5. A simple $1-\alpha$ interval: the percentile interval $\big[\hat\theta^{*}_{(\alpha/2)},\ \hat\theta^{*}_{(1-\alpha/2)}\big]$ from the empirical quantiles of the replicates.

*No distributional assumption, no CLT formula — the resampling reconstructs the sampling distribution from the data alone.*

> **Connection — why the bootstrap works**
>
> The sampling distribution describes how $\hat\theta$ varies as samples are drawn from $F$. The bootstrap substitutes $\hat F_n$ for the unknown $F$ and draws from *it*. Glivenko–Cantelli guarantees $\hat F_n\approx F$, so bootstrap variability approximates true sampling variability — the plug-in principle made operational.

<a id="s16"></a>
### A glimpse beyond: decision theory & large-sample asymptotics

*A unifying frame — estimation and testing as decisions under loss — and the asymptotic machinery (delta method, efficiency) that makes the MLE the default tool.*

**Risk, the language of decisions**

$$R(\theta,\delta)=E_\theta\big[\,\ell(\theta,\delta(\mathbf X))\,\big],\qquad \text{e.g. squared-error loss } \ell(\theta,d)=(d-\theta)^2\Rightarrow R=\text{MSE}$$

*A decision rule $\delta$ maps data to actions; its **risk** is expected loss. With squared-error loss, risk is exactly the MSE of Section 6 — estimation is a special case of decision theory.*

> **Principle — admissibility, minimax & Bayes rules**
>
> A rule is **inadmissible** if another rule has $\le$ risk everywhere and strictly less somewhere. A **minimax** rule minimizes worst-case risk; a **Bayes** rule minimizes risk averaged over a prior — it is the posterior-expected-loss minimizer of Section 14. Remarkably, in dimension $\ge3$ the sample mean is inadmissible (Stein's paradox): shrinkage estimators beat it everywhere.

**The delta method**

$$\sqrt n\,(\hat\theta-\theta)\xrightarrow{d}N(0,\sigma^2)\ \Longrightarrow\ \sqrt n\,\big(g(\hat\theta)-g(\theta)\big)\xrightarrow{d}N\!\big(0,\ [g'(\theta)]^2\sigma^2\big)$$

*A first-order Taylor expansion propagates asymptotic normality through a smooth transformation $g$ — the asymptotic version of error propagation, and pure calculus.*

**Demonstration — the delta method in one line**

1. Taylor-expand $g$ about $\theta$: $g(\hat\theta)\approx g(\theta)+g'(\theta)(\hat\theta-\theta)$.
2. Multiply by $\sqrt n$: $\sqrt n\,(g(\hat\theta)-g(\theta))\approx g'(\theta)\cdot\sqrt n\,(\hat\theta-\theta)$.
3. The right side is $g'(\theta)$ times a quantity converging to $N(0,\sigma^2)$, giving variance $[g'(\theta)]^2\sigma^2$ by Slutsky's theorem.

*This is how standard errors are obtained for odds, rates, and other transformed parameters.*

> **Principle — the asymptotic supremacy of the MLE**
>
> Under regularity, $\sqrt n(\hat\theta_{\text{MLE}}-\theta)\xrightarrow{d}N(0,1/I_1(\theta))$: the MLE is consistent, asymptotically normal, and asymptotically efficient — it attains the Cramér–Rao bound in the limit. This is why, absent special structure, maximum likelihood (and its Bayesian cousin) is the workhorse of statistical inference.

> **Connection — the whole guide, in one arc**
>
> Likelihood (s3) gives the score and information (s7); maximizing it gives the MLE (s5); information bounds its variance (s7–8) and sets the width of intervals (s9) and the scale of tests (s10–11); the same likelihood, times a prior, gives the posterior (s13–14); and where no model is assumed, the empirical distribution and the bootstrap (s15) stand in. One function — the likelihood — organizes the entire subject.

---

*A course in mathematical statistics — sufficiency, estimation, the Cramér–Rao bound, Neyman–Pearson and likelihood-ratio testing, the Bayesian update, and the bootstrap — each principle stated precisely and each theorem demonstrated. A companion to the intro Statistics and Probability guides. Return to any box as a reference, and remember: behind estimation, testing, and Bayes alike stands a single object, the likelihood function.*
