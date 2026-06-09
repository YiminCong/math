**English** · [中文](regression.zh.md)

# Regression, *the best line and beyond.*

From a single straight line through a cloud of points to the full machinery of linear models — least squares as calculus, the matrix geometry of projection, honest inference, and the generalizations (logistic, GLMs, ridge & lasso) that power modern data science. Every core result is **demonstrated** from first principles, with every symbol defined the first time it appears and every algebraic step justified, so that a reader with no prior mathematics can follow the entire path. The threads back to calculus, probability, and linear algebra are made explicit.

[← Back to all guides](../README.md)

## Part A · Simple linear regression

<a id="s0"></a>
### The big picture: modeling relationships

Regression answers a question that correlation only hints at: given that two (or many) measured quantities tend to move together, can we write down an explicit *function* that predicts one of them from the others — and can we say honestly how good that prediction is? This is the workhorse of applied statistics and the doorway to machine learning.

Before any formula, fix the vocabulary in plain words.

- A **variable** is just a measured quantity that can take different values from one observation to the next — height, temperature, price.
- The **response** (written $y$) is the variable we want to predict or explain.
- A **predictor** (also called an *independent variable*, *feature*, or *covariate*, written $x$ or, when there are several, $\mathbf{x}$) is a variable we use to make that prediction. The bold $\mathbf{x}$ means a *list* of several predictors bundled together; we call such a list a **vector**.
- An **observation** (or *data point*) is one complete measured row: one value of $y$ together with its matching predictor value(s). We collect $n$ of them and index them $i = 1, 2, \dots, n$. The subscript $i$ is a label, like a row number; $y_i$ is "the $y$ of the $i$-th observation."

With that vocabulary, here is the entire idea of regression in three moves.

- **Signal + noise.** We assume the response $y$ is a *systematic* (predictable, repeatable) function of the predictors, plus a *random* leftover called **error** or **noise**. In symbols, $y = f(\mathbf{x}) + \varepsilon$. Here $f$ (the letter $f$ for "function") is the systematic part — the rule that turns predictors into a prediction — and $\varepsilon$ (the Greek letter *epsilon*) is the random part, the part no predictor can explain. We will always assume the noise has **mean zero**, meaning that on average it neither pushes $y$ up nor pulls it down; the symbol for "the average value of" is $E[\cdot]$ (read "expected value"), so this assumption is written $E[\varepsilon] = 0$.
- **Estimate.** We do not know the true function $f$. We *fit* it — choose a specific function from a family — by making it match the data as closely as possible. "As closely as possible" must be measured by a number we agree to minimize, called a **loss**. The usual loss is **squared error**: we square each miss and add them up. To *minimize* means to make as small as we can.
- **Infer & predict.** A single fitted number (say a slope) is never the whole story; we also attach **uncertainty** to it — a range that honestly expresses how much the number might change if we collected fresh data. We do the same for predictions of future $y$ values.

> **Principle — the regression model decomposes data into structure and noise**
>
> Every regression writes $ \text{observed} = \text{model} + \text{residual} $. The **model** is the systematic part we can predict; the **residual** is what is left over after the model has done its best. The art is choosing a model rich enough to capture the real structure but simple enough not to chase the random noise. The **linear model** — in which the response is a weighted sum of (functions of) the predictors — is the foundation of the whole subject because it is interpretable, has exact closed-form solutions (formulas, not just trial-and-error search), and underpins almost everything more advanced.

**The general supervised-learning frame**

$$y_i = f(\mathbf{x}_i) + \varepsilon_i,\qquad E[\varepsilon_i]=0,\qquad i=1,\dots,n$$

Reading the symbols one by one: $y_i$ is the response of observation $i$; $\mathbf{x}_i$ is the bundle of predictors for that same observation; $f$ is the unknown systematic rule; $\varepsilon_i$ is that observation's random error; $E[\varepsilon_i] = 0$ says each error averages to zero across hypothetical repeats; and "$i = 1, \dots, n$" says the equation holds for every one of the $n$ observations. The phrase **supervised learning** simply means we learn the rule $f$ from examples whose answers $y_i$ we already know.

*Linear models take the special form $f(\mathbf{x}) = \boldsymbol{\beta}^\top \mathbf{x}$ — a weighted sum of the predictors, where $\boldsymbol{\beta}$ (bold Greek *beta*) is the vector of weights and the symbol $^\top$ (read "transpose," explained in §s5) turns the bundling into a sum. GLMs (§s11) let a known function of the average response be such a weighted sum. Nonparametric methods (§s13) let $f$ be a flexible curve. The same loss-and-fit logic runs through all of them.*

#### The whole guide on one line

> Best line → Least squares as calculus → Matrix form & projection → Inference & ANOVA → Logistic & GLMs → Regularization & beyond

Read that arrow-by-arrow: we begin with the single best straight line through a scatter of points; we show that finding it is exactly the calculus problem of minimizing a function; we rewrite everything compactly using matrices and discover that fitting is *geometric projection*; we add honest uncertainty (confidence intervals, the $t$-test and $F$-test); we generalize to yes/no responses (logistic) and to a whole family of response types (GLMs); and we finish with methods (ridge, lasso) that tame models with many predictors.

> **Connection — picking up where the Statistics guide left off**
>
> The introductory Statistics companion ends at **correlation & the least-squares line** (its Section 13). This guide starts exactly there and derives, generalizes, and stress-tests it. Keep its big idea in mind — the **z-score**, which answers "how far from the average is this value, measured in standard deviations?" — because every $t$-ratio and $F$-ratio in this guide is that same idea in disguise: an estimate, minus what we'd expect, divided by a measure of its spread.

#### A worked feel for "structure + noise"

Suppose five students study $x = 1, 2, 3, 4, 5$ hours and score $y = 52, 58, 61, 70, 74$ on a test. The scores generally rise with study time (structure), but not by a perfectly fixed amount each hour (noise). Regression will (in §s1) find the single straight line $\hat y = \hat\beta_0 + \hat\beta_1 x$ that best summarizes the rising trend, then quantify how much of the score variation that trend explains and how much is leftover noise. We will return to these exact numbers repeatedly so you can see every formula produce a concrete value.

<a id="s1"></a>
### Simple linear regression & least squares

*One predictor, one response, one straight line — fitted by minimizing the sum of squared vertical distances.*

**The simple linear regression model**

$$y_i = \beta_0 + \beta_1 x_i + \varepsilon_i,\qquad \varepsilon_i \stackrel{\text{iid}}{\sim}(0,\sigma^2)$$

Symbol by symbol: $y_i$ is the response of observation $i$; $x_i$ is its single predictor; $\beta_0$ (beta-zero) is the **intercept** — the height of the line where $x = 0$; $\beta_1$ (beta-one) is the **slope** — how many units $y$ rises for each one-unit rise in $x$; and $\varepsilon_i$ is the random error of that observation. The decoration "$\stackrel{\text{iid}}{\sim}(0,\sigma^2)$" reads: the errors are **iid** (independent and identically distributed — each error is unrelated to the others and all are drawn from the same pattern), with **mean** $0$ and **variance** $\sigma^2$. The *mean* is the long-run average; the *variance* (Greek $\sigma^2$, sigma-squared) is the average squared distance from that mean, a number measuring spread — bigger $\sigma^2$ means noisier data.

*$\beta_0$ and $\beta_1$ are unknown **parameters** — fixed but unknown numbers of nature we hope to recover. The **fitted line** is $\hat y = \hat\beta_0 + \hat\beta_1 x$, where the hat "$\hat{\ }$" marks an *estimate* (our data-based guess of an unknown quantity). The $i$-th **residual** is $e_i = y_i - \hat y_i$: the leftover gap between the actual response and the line's prediction. Do not confuse the residual $e_i$ (observed leftover, computable from data) with the error $\varepsilon_i$ (the unobservable true noise).*

> **Concept — why squared (not absolute) error?**
>
> We measure misfit by the **sum of squared residuals** $\sum e_i^2$ (the symbol $\sum$, capital Greek *sigma*, means "add up over all observations"). Why square each gap rather than take its absolute size? Three reasons. First, squaring is **smooth** — differentiable everywhere — so the tools of calculus (derivatives) apply cleanly. Second, squaring penalizes one big miss far more than several small ones, which usually matches what we want. Third — and most deeply — when the errors follow the bell-shaped **Normal** distribution, the least-squares fit is *also* the **maximum-likelihood** fit (the parameter values that make the observed data most probable). Using absolute error instead gives a median-like fit ($L_1$ regression) that is more robust to outliers but has no tidy closed-form formula.

**Demonstration — deriving the slope & intercept by minimizing the sum of squares**

We want the pair $(\beta_0, \beta_1)$ making $\sum e_i^2$ as small as possible. The method: treat the sum as a function of these two unknowns and use calculus, where the smallest value of a smooth function occurs where its slope (derivative) is zero.

1. **Write the objective.** Define the loss as a function of the two unknowns:

   $$S(\beta_0,\beta_1)=\sum_{i=1}^{n}\big(y_i-\beta_0-\beta_1 x_i\big)^2.$$

   Each term $(y_i - \beta_0 - \beta_1 x_i)$ is the residual for observation $i$ when the line has intercept $\beta_0$ and slope $\beta_1$; squaring and summing gives total misfit. *Reason:* this is exactly the squared-error loss defined above.
2. **Set both partial derivatives to zero.** A function of two variables is smallest (when, as here, it curves upward like a bowl) at the point where it is flat in *both* directions — that is, where both **partial derivatives** are zero. A partial derivative differentiates with respect to one variable while holding the other fixed. Using the chain rule (the derivative of $(\cdot)^2$ is $2(\cdot)$ times the derivative of the inside):

   $$\frac{\partial S}{\partial \beta_0}=\sum 2\big(y_i-\beta_0-\beta_1 x_i\big)(-1)=-2\sum\big(y_i-\beta_0-\beta_1 x_i\big)=0,$$

   $$\frac{\partial S}{\partial \beta_1}=\sum 2\big(y_i-\beta_0-\beta_1 x_i\big)(-x_i)=-2\sum x_i\big(y_i-\beta_0-\beta_1 x_i\big)=0.$$

   *Reason:* these are the **first-order conditions** of calculus optimization — at a minimum of a smooth function the gradient vanishes.
3. **Solve the first equation for the intercept.** Divide the first equation by $-2$ and split the sum: $\sum y_i - n\beta_0 - \beta_1 \sum x_i = 0$, because $\sum \beta_0 = n\beta_0$ (adding the constant $\beta_0$ a total of $n$ times). This is the first **normal equation** $\sum y_i = n\beta_0 + \beta_1 \sum x_i$. Dividing by $n$ and writing $\bar y = \frac1n\sum y_i$, $\bar x = \frac1n \sum x_i$ for the **sample means** (the ordinary averages):

   $$\hat\beta_0 = \bar y - \hat\beta_1 \bar x.$$

   *Reason:* pure algebra plus the definition of the average. The hats appear because we have now committed to the minimizing values.
4. **Substitute and solve for the slope.** Put $\beta_0 = \bar y - \beta_1 \bar x$ into the second equation. After substitution each bracket becomes $y_i - \bar y - \beta_1(x_i - \bar x)$, so the second normal equation reads $\sum x_i\big[(y_i - \bar y) - \beta_1(x_i - \bar x)\big] = 0$. Using the algebraic fact $\sum (x_i - \bar x) = 0$ (the deviations from the mean cancel), we may replace the leading $x_i$ by $(x_i - \bar x)$ without changing the equation, giving $\sum (x_i - \bar x)(y_i - \bar y) - \beta_1 \sum (x_i - \bar x)^2 = 0$. Solving:

   $$\hat\beta_1=\frac{\sum (x_i-\bar x)(y_i-\bar y)}{\sum (x_i-\bar x)^2}=\frac{S_{xy}}{S_{xx}}.$$

   Here we *name* two recurring quantities: $S_{xx} = \sum (x_i - \bar x)^2$ (the total squared spread of $x$ about its mean) and $S_{xy} = \sum (x_i - \bar x)(y_i - \bar y)$ (how $x$ and $y$ co-vary about their means). *Reason:* substitution, the mean-deviation identity, and algebra.
5. **Confirm it is a minimum, not a maximum or saddle.** The matrix of second partial derivatives (the **Hessian**) of $S$ is $\begin{psmallmatrix} 2n & 2\sum x_i \\ 2\sum x_i & 2\sum x_i^2\end{psmallmatrix}$. Its determinant equals $4\big(n\sum x_i^2 - (\sum x_i)^2\big) = 4n\,S_{xx} > 0$ whenever the $x_i$ are not all identical, and its top-left entry $2n > 0$; a symmetric matrix with positive top-left entry and positive determinant is **positive definite**, which is the second-derivative test certifying a strict local minimum — and since $S$ is a sum of squares (a bowl that opens upward everywhere) this local minimum is the unique global minimum. *Reason:* the multivariable second-derivative test.

*Because $\hat\beta_0=\bar y-\hat\beta_1\bar x$, rearranged as $\bar y = \hat\beta_0 + \hat\beta_1 \bar x$, the fitted line always passes through the centroid $(\bar x,\bar y)$ — the balance point of the data.*

**Worked example — the five students.** Using $x = 1,2,3,4,5$ and $y = 52,58,61,70,74$:

- Means: $\bar x = \frac{1+2+3+4+5}{5} = 3$, and $\bar y = \frac{52+58+61+70+74}{5} = \frac{315}{5} = 63$.
- Deviations $x_i - \bar x$: $-2,-1,0,1,2$. Deviations $y_i - \bar y$: $-11,-5,-2,7,11$.
- $S_{xy} = (-2)(-11)+(-1)(-5)+(0)(-2)+(1)(7)+(2)(11) = 22+5+0+7+22 = 56$.
- $S_{xx} = (-2)^2+(-1)^2+0^2+1^2+2^2 = 4+1+0+1+4 = 10$.
- Slope: $\hat\beta_1 = S_{xy}/S_{xx} = 56/10 = 5.6$. Intercept: $\hat\beta_0 = \bar y - \hat\beta_1 \bar x = 63 - 5.6\times 3 = 63 - 16.8 = 46.2$.

So the best line is $\hat y = 46.2 + 5.6\,x$: each extra study-hour is associated with about $5.6$ more points. Check the centroid: at $x = 3$, $\hat y = 46.2 + 16.8 = 63 = \bar y$. The line passes through $(\bar x, \bar y)$ as proved.

**The slope in correlation form**

$$\hat\beta_1 = r\,\frac{s_y}{s_x},\qquad r=\frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}$$

Here $s_x$ and $s_y$ are the **sample standard deviations** of $x$ and $y$ — the typical distance of a value from its mean, defined by $s_x = \sqrt{S_{xx}/(n-1)}$ and likewise for $y$ (we explain the $n-1$ in §s2). The quantity $r$ is the **correlation coefficient**: a unitless number between $-1$ and $+1$ measuring how tightly the points hug a straight line ($S_{yy} = \sum (y_i - \bar y)^2$ is the total spread of $y$). The slope is the correlation rescaled by the ratio of spreads — regression and correlation are two faces of one quantity.

**Demonstration — $\hat\beta_1 = r\,s_y/s_x$**

1. Start from $\hat\beta_1=S_{xy}/S_{xx}$ (from the previous demonstration) and from the definition $r=S_{xy}/\sqrt{S_{xx}S_{yy}}$, which rearranges to $S_{xy}=r\sqrt{S_{xx}S_{yy}}$. *Reason:* multiply both sides of the definition of $r$ by $\sqrt{S_{xx}S_{yy}}$.
2. Substitute that expression for $S_{xy}$ into the slope:

   $$\hat\beta_1=\frac{r\sqrt{S_{xx}S_{yy}}}{S_{xx}}=r\,\frac{\sqrt{S_{xx}}\sqrt{S_{yy}}}{S_{xx}}=r\,\frac{\sqrt{S_{yy}}}{\sqrt{S_{xx}}}=r\,\sqrt{\frac{S_{yy}}{S_{xx}}}.$$

   *Reason:* $\sqrt{S_{xx}S_{yy}} = \sqrt{S_{xx}}\sqrt{S_{yy}}$ and cancelling one factor of $\sqrt{S_{xx}}$ against the $S_{xx}$ below.
3. Since $s_y=\sqrt{S_{yy}/(n-1)}$ and $s_x=\sqrt{S_{xx}/(n-1)}$, their ratio is $s_y/s_x = \sqrt{S_{yy}/(n-1)} / \sqrt{S_{xx}/(n-1)} = \sqrt{S_{yy}/S_{xx}}$ — the $(n-1)$ cancels top and bottom. Therefore:

   $$\hat\beta_1=r\,\frac{s_y}{s_x}.$$

   *Reason:* the definition of the standard deviations and cancellation.

**Worked example (continued).** With $S_{yy} = (-11)^2+(-5)^2+(-2)^2+7^2+11^2 = 121+25+4+49+121 = 320$, the correlation is $r = S_{xy}/\sqrt{S_{xx}S_{yy}} = 56/\sqrt{10\times 320} = 56/\sqrt{3200} = 56/56.569 \approx 0.990$. The spreads are $s_x = \sqrt{10/4} = 1.581$ and $s_y = \sqrt{320/4} = \sqrt{80} = 8.944$. Check: $r\,s_y/s_x = 0.990 \times 8.944/1.581 = 0.990 \times 5.657 = 5.6 = \hat\beta_1$. The two formulas agree.

*If $x$ and $y$ are standardized so that $s_x = s_y = 1$, the slope *is* the correlation. Because $|r| \le 1$, a standardized prediction is always pulled toward the mean — this is the original "regression to the mean," from which the whole subject takes its name.*

> **Connection — this is the calculus optimization you already know**
>
> Minimizing $S(\beta_0,\beta_1)$ by setting partial derivatives to zero is precisely the multivariable optimization of a calculus course, applied to data. The positive-definite Hessian is the second-derivative test guaranteeing a minimum. Regression is calculus optimization with a statistical interpretation bolted on.

<a id="s2"></a>
### The Gauss–Markov theorem & properties of the estimators

*Why least squares is special: among all sensible linear methods that get the answer right on average, it has the smallest wobble.*

Two new words must be pinned down first. An estimator is **unbiased** if its average value over many hypothetical datasets equals the true parameter — it does not systematically over- or under-shoot. The **variance** of an estimator measures how much it bounces around from one dataset to the next; smaller variance means a more reliable, repeatable estimate. We want estimators that are both unbiased and low-variance.

**Unbiasedness of the slope**

$$E[\hat\beta_1]=\beta_1,\qquad E[\hat\beta_0]=\beta_0$$

$$\operatorname{Var}(\hat\beta_1)=\frac{\sigma^2}{S_{xx}},\qquad \operatorname{Var}(\hat\beta_0)=\sigma^2\!\left(\frac1n+\frac{\bar x^2}{S_{xx}}\right)$$

The first line says least squares hits the true intercept and slope on average. The second gives the variances: notice $S_{xx}$ sits in the denominator of $\operatorname{Var}(\hat\beta_1)$, so *more spread in $x$ (larger $S_{xx}$) means a more tightly pinned slope*. This is exactly why good experiment design spreads the predictor values far apart.

**Demonstration — $\hat\beta_1$ is unbiased and find its variance**

1. **Express the slope as a weighted sum of responses.** From $\hat\beta_1 = \sum (x_i - \bar x)(y_i - \bar y)/S_{xx}$, and using $\sum (x_i - \bar x)\bar y = \bar y \sum (x_i - \bar x) = 0$, the $\bar y$ drops out, leaving $\hat\beta_1 = \sum c_i y_i$ with **weights** $c_i = (x_i - \bar x)/S_{xx}$. Two facts about these weights follow directly: $\sum c_i = \frac{1}{S_{xx}}\sum(x_i - \bar x) = 0$, and $\sum c_i x_i = \frac{1}{S_{xx}}\sum (x_i-\bar x)x_i = \frac{1}{S_{xx}}\sum(x_i-\bar x)^2 = 1$ (the last sum is $S_{xx}$). *Reason:* algebra and the mean-deviation identity $\sum(x_i-\bar x)=0$.
2. **Take the expectation.** Expectation is **linear** — the average of a weighted sum is the weighted sum of the averages — and $E[y_i] = \beta_0 + \beta_1 x_i$ because $E[\varepsilon_i] = 0$:

   $$E[\hat\beta_1]=\sum c_i E[y_i]=\sum c_i(\beta_0+\beta_1 x_i)=\beta_0\underbrace{\textstyle\sum c_i}_{0}+\beta_1\underbrace{\textstyle\sum c_i x_i}_{1}=\beta_1.$$

   *Reason:* linearity of expectation and the two weight facts from step 1.
3. **Compute the variance.** For *independent* quantities the variance of a weighted sum is the sum of the squared weights times each variance (cross terms vanish because independent variables do not co-vary), and each $y_i$ has variance $\sigma^2$:

   $$\operatorname{Var}(\hat\beta_1)=\sum c_i^2\,\operatorname{Var}(y_i)=\sigma^2\sum c_i^2=\frac{\sigma^2}{S_{xx}^2}\sum(x_i-\bar x)^2=\frac{\sigma^2}{S_{xx}^2}\,S_{xx}=\frac{\sigma^2}{S_{xx}}.$$

   *Reason:* the variance-of-a-sum rule for independent terms, then $\sum c_i^2 = \sum (x_i-\bar x)^2/S_{xx}^2 = S_{xx}/S_{xx}^2 = 1/S_{xx}$.

*No Normality assumption was needed here — only $E[\varepsilon] = 0$, constant variance $\sigma^2$, and independence.*

**Worked example (continued).** Suppose the true noise level is $\sigma = 2$, so $\sigma^2 = 4$. With $S_{xx} = 10$ from the students, $\operatorname{Var}(\hat\beta_1) = 4/10 = 0.4$, giving a standard deviation of the slope of $\sqrt{0.4} \approx 0.632$. Had we spread study times over $0,2,4,6,8$ hours instead (same five points, wider), $S_{xx}$ would be $40$ and the slope variance would drop to $4/40 = 0.1$ — four times more precise from wider design alone.

> **Principle — Gauss–Markov: OLS is BLUE**
>
> Under four assumptions — linearity of the mean, zero-mean errors, **homoscedasticity** (every error has the same variance $\sigma^2$; "homo-" same, "-scedastic" spread), and uncorrelated errors — the ordinary least squares estimator (**OLS**) is the **Best Linear Unbiased Estimator**: among all estimators that are both *linear in* $\mathbf{y}$ (a weighted sum of the responses) and *unbiased*, OLS has the minimum variance. "Best" means smallest variance, not smallest possible error on any one dataset.

**Demonstration — why OLS is BLUE**

1. **Take any rival linear unbiased estimator.** Write it as $\tilde\beta_1 = \sum d_i y_i$ with some weights $d_i$ (the tilde marks the rival). For it to be unbiased we need, by the same expectation computation as above, $\sum d_i = 0$ and $\sum d_i x_i = 1$ — the *same* two constraints the OLS weights $c_i$ satisfy. *Reason:* repeat step 2 of the previous demonstration with $d_i$ in place of $c_i$ and demand the result equal $\beta_1$ for all $\beta_0,\beta_1$.
2. **Split the rival weights from the OLS weights.** Write $d_i = c_i + \delta_i$, defining the *difference* $\delta_i = d_i - c_i$. Subtracting the constraint pairs, $\sum \delta_i = \sum d_i - \sum c_i = 0 - 0 = 0$ and $\sum \delta_i x_i = \sum d_i x_i - \sum c_i x_i = 1 - 1 = 0$. From these, the **cross term** vanishes: $\sum c_i \delta_i = \sum \frac{x_i - \bar x}{S_{xx}}\delta_i = \frac{1}{S_{xx}}\big(\sum x_i \delta_i - \bar x \sum \delta_i\big) = \frac{1}{S_{xx}}(0 - 0) = 0$. *Reason:* substitute $c_i = (x_i-\bar x)/S_{xx}$ and apply the two facts about $\delta_i$.
3. **Split the variance.** Because the $y_i$ are independent with variance $\sigma^2$:

   $$\operatorname{Var}(\tilde\beta_1)=\sigma^2\sum d_i^2=\sigma^2\sum (c_i+\delta_i)^2=\sigma^2\Big(\sum c_i^2 + 2\sum c_i\delta_i + \sum \delta_i^2\Big)=\operatorname{Var}(\hat\beta_1)+\sigma^2\sum\delta_i^2.$$

   *Reason:* expand the square; the middle cross term is zero by step 2; $\sigma^2 \sum c_i^2 = \operatorname{Var}(\hat\beta_1)$ from before.
4. **Conclude.** A sum of squares is never negative, so $\sum \delta_i^2 \ge 0$, hence $\operatorname{Var}(\tilde\beta_1) \ge \operatorname{Var}(\hat\beta_1)$, with equality only when every $\delta_i = 0$, i.e. when the rival *is* OLS. *Reason:* squares are non-negative. Therefore no linear unbiased estimator beats OLS for variance.

*OLS sits at the very bottom of the variance bowl among all linear unbiased competitors — the Gauss–Markov optimum.*

**Estimating the error variance**

$$\hat\sigma^2 = s^2 = \frac{1}{n-2}\sum_{i=1}^n e_i^2 = \frac{\text{SSE}}{n-2}$$

Here $\text{SSE} = \sum e_i^2$ is the **sum of squared errors** (residuals), and $s^2$ is our estimate of the unknown noise variance $\sigma^2$.

> **Concept — why divide by $n-2$**
>
> A **degree of freedom** is an independent piece of information left in the data after we have spent some on estimating parameters. We started with $n$ residuals, but they are not all free: fitting $\hat\beta_0$ and $\hat\beta_1$ forced two exact relations on them ($\sum e_i = 0$ and $\sum x_i e_i = 0$, the normal equations). That uses up two pieces of information, leaving $n - 2$ free. Dividing by $n - 2$ rather than $n$ exactly compensates and makes $s^2$ **unbiased** for $\sigma^2$, i.e. $E[s^2] = \sigma^2$ (stated here; the proof is the degrees-of-freedom argument that $E[\text{SSE}] = (n-2)\sigma^2$, exactly as Bessel's $n-1$ correction gives $E[\text{SSE}] = (n-1)\sigma^2$ for a plain sample). This is the same logic as the intro Statistics guide, here generalized to two estimated parameters.

**Worked example (continued).** Fitted values $\hat y = 46.2 + 5.6x$ at $x=1,\dots,5$ are $51.8, 57.4, 63.0, 68.6, 74.2$. Residuals $e_i = y_i - \hat y_i$: $0.2, 0.6, -2.0, 1.4, -0.2$. Then $\text{SSE} = 0.04 + 0.36 + 4.0 + 1.96 + 0.04 = 6.4$, and $s^2 = 6.4/(5-2) = 6.4/3 \approx 2.133$, so $s \approx 1.461$. (As a check, $\sum e_i = 0.2+0.6-2.0+1.4-0.2 = 0$ exactly, as the normal equations require.)

<a id="s3"></a>
### Inference for slope & intercept; confidence & prediction intervals

*From point estimates to honest uncertainty: testing whether a slope is real, and bracketing future outcomes.*

A **hypothesis test** asks whether the data are surprising under a tentative assumption called the **null hypothesis** $H_0$. A **standard error** (SE) is the estimated standard deviation of an estimator — how far it typically lands from its target. A **confidence interval** is a range, computed from data, designed to contain the unknown parameter a stated fraction (e.g. 95%) of the time across repeats.

**The t-statistic for a coefficient**

$$t = \frac{\hat\beta_1 - \beta_1^{(0)}}{\operatorname{SE}(\hat\beta_1)},\qquad \operatorname{SE}(\hat\beta_1)=\frac{s}{\sqrt{S_{xx}}}$$

The numerator is "how far the estimate landed from the hypothesized value $\beta_1^{(0)}$"; the denominator rescales that distance into *standard-error units*. The standard error replaces the unknown $\sigma$ in $\sqrt{\sigma^2/S_{xx}} = \sigma/\sqrt{S_{xx}}$ (from §s2) by its estimate $s$.

*Under Normal errors and the null hypothesis $H_0:\beta_1=\beta_1^{(0)}$, this ratio follows a **$t$-distribution** with $n-2$ degrees of freedom — a bell shape like the Normal but with heavier tails. The common choice $\beta_1^{(0)} = 0$ asks the basic question "is there any linear relationship at all?"*

> **Concept — why $t$, and why $n-2$ df**
>
> If we somehow knew the true $\sigma$, the standardized slope $(\hat\beta_1 - \beta_1)/(\sigma/\sqrt{S_{xx}})$ would be *exactly* a standard Normal. But we do not know $\sigma$; we estimate it by $s$, which is itself random. Plugging in a noisy denominator adds extra uncertainty, fattening the tails — and that fatter-tailed shape is precisely Student's $t$-distribution. The degrees of freedom are $n - 2$ because, as in §s2, estimating the two coefficients consumed two pieces of information.

**Confidence interval for the slope**

$$\hat\beta_1 \pm t^{*}_{n-2}\;\frac{s}{\sqrt{S_{xx}}}$$

This is the universal template "estimate $\pm$ critical value $\times$ standard error." The **critical value** $t^*_{n-2}$ is the cutoff from the $t$-distribution that leaves the desired tail probability (for 95% confidence, the central 95% lies between $-t^*$ and $+t^*$).

**Worked example (continued).** $\operatorname{SE}(\hat\beta_1) = s/\sqrt{S_{xx}} = 1.461/\sqrt{10} = 1.461/3.162 = 0.462$. To test $H_0: \beta_1 = 0$: $t = 5.6/0.462 = 12.1$ on $n - 2 = 3$ degrees of freedom. The two-sided 5% critical value is $t^*_3 = 3.182$. Since $12.1 > 3.182$, we reject $H_0$ — the slope is convincingly nonzero. A 95% confidence interval for the slope is $5.6 \pm 3.182 \times 0.462 = 5.6 \pm 1.47 = [4.13,\,7.07]$.

> **Principle — confidence interval vs prediction interval**
>
> Two very different questions arise at a new predictor value $x_0$. A **confidence interval for the mean response** brackets $E[y \mid x_0]$ — the *average* $y$ among all units having $x = x_0$. A **prediction interval** brackets a *single future observation* $y_0$, so it must also include the irreducible noise $\sigma^2$ of that one new point. The prediction interval is therefore always wider, and it stays wide even as the sample size $n \to \infty$ (we can pin down an average perfectly, but never a single coin flip).

**Confidence vs prediction interval at $x_0$**

$$\hat y_0 \pm t^{*}_{n-2}\,s\sqrt{\frac1n+\frac{(x_0-\bar x)^2}{S_{xx}}}\quad\text{(mean response)}$$

$$\hat y_0 \pm t^{*}_{n-2}\,s\sqrt{1+\frac1n+\frac{(x_0-\bar x)^2}{S_{xx}}}\quad\text{(new observation)}$$

The lone extra $1$ under the second root is the variance contributed by the fresh error $\varepsilon_0$ of the new point. Both intervals widen as $x_0$ moves away from the data center $\bar x$, because the $(x_0 - \bar x)^2$ term grows.

**Demonstration — why both intervals widen away from $\bar x$**

1. **Rewrite the fitted mean.** Using $\hat\beta_0 = \bar y - \hat\beta_1\bar x$ (from §s1), the prediction at $x_0$ is $\hat y_0 = \hat\beta_0 + \hat\beta_1 x_0 = \bar y - \hat\beta_1 \bar x + \hat\beta_1 x_0 = \bar y + \hat\beta_1 (x_0 - \bar x)$. *Reason:* substitute the intercept formula and group the slope terms.
2. **Combine the two sources of variance.** The terms $\bar y$ and $\hat\beta_1$ are uncorrelated: $\operatorname{Cov}(\bar y,\hat\beta_1)=\operatorname{Cov}\!\big(\tfrac1n\sum y_i,\sum c_i y_i\big)=\tfrac{\sigma^2}{n}\sum c_i=0$, since the weights $c_i=(x_i-\bar x)/S_{xx}$ sum to zero (step 1 of the §s2 demonstration). So the variance of their combination is the sum of the parts. With $\operatorname{Var}(\bar y) = \sigma^2/n$ (the variance of an average of $n$ independent points) and $\operatorname{Var}(\hat\beta_1) = \sigma^2/S_{xx}$ (from §s2):

   $$\operatorname{Var}(\hat y_0)=\operatorname{Var}(\bar y)+(x_0-\bar x)^2\operatorname{Var}(\hat\beta_1)=\frac{\sigma^2}{n}+(x_0-\bar x)^2\frac{\sigma^2}{S_{xx}}=\sigma^2\!\left(\frac1n+\frac{(x_0-\bar x)^2}{S_{xx}}\right).$$

   *Reason:* variance of a sum of uncorrelated terms, and the constant $(x_0-\bar x)$ comes out squared. Estimating $\sigma^2$ by $s^2$ and taking the square root gives the mean-response interval's width.
3. **Read off the shape.** The term $(x_0 - \bar x)^2$ grows *quadratically* as $x_0$ leaves the center, so the interval bows outward into a hyperbola — narrowest at $\bar x$, ever-wider in both directions. *Reason:* a squared distance increases without bound.
4. **Add the new point's own noise.** For predicting a single new $y_0 = \beta_0 + \beta_1 x_0 + \varepsilon_0$, the fresh error $\varepsilon_0$ is independent of the fitted line and has variance $\sigma^2$, so it adds on: $\operatorname{Var}(y_0 - \hat y_0) = \sigma^2 + \operatorname{Var}(\hat y_0) = \sigma^2\big(1 + \frac1n + \frac{(x_0-\bar x)^2}{S_{xx}}\big)$. *Reason:* independence makes variances add; this produces the extra $+1$.

*Predictions are most trustworthy near the heart of the observed $x$-range; extrapolating far outside it is dangerous.*

**Worked example (continued).** Predict at $x_0 = 6$ (one hour beyond the data). Point prediction $\hat y_0 = 46.2 + 5.6\times 6 = 79.8$. With $\bar x = 3$, $(x_0 - \bar x)^2 = 9$. Mean-response half-width: $t^*_3\, s\sqrt{\frac15 + \frac{9}{10}} = 3.182\times 1.461\times\sqrt{0.2 + 0.9} = 4.648\times\sqrt{1.1} = 4.648\times1.049 = 4.88$, giving $[74.9, 84.7]$. Prediction interval half-width adds the $+1$: $4.648\times\sqrt{1 + 1.1} = 4.648\times\sqrt{2.1} = 4.648\times1.449 = 6.74$, giving $[73.1, 86.5]$ — visibly wider, as the principle promised.

> **Connection — to Inference (t/F distributions, MLE)**
>
> The $t$-ratio here is identical in spirit to the one-sample $t$-test of the Inference guide. Under Normal errors the least-squares estimates coincide with the **maximum-likelihood** estimates, and the $t$ and (later) $F$ sampling distributions are exactly the ones that course derives from the Normal.

<a id="s4"></a>
### Assessing fit: R², residuals & diagnostics

*A fitted line is not automatically a good one. Two tools: a single goodness-of-fit number, and a careful look at what is left over.*

**The sums-of-squares decomposition**

$$\underbrace{\sum(y_i-\bar y)^2}_{\text{SST}} = \underbrace{\sum(\hat y_i-\bar y)^2}_{\text{SSR}} + \underbrace{\sum(y_i-\hat y_i)^2}_{\text{SSE}}$$

Three named quantities: **SST** (total sum of squares) is the total up-and-down variation of $y$ about its mean — the variation we hope to explain. **SSR** (regression sum of squares) is the variation the fitted line *does* explain — how much the predictions $\hat y_i$ themselves vary about $\bar y$. **SSE** (error sum of squares) is the leftover the line could not explain. In words: total variation = explained + unexplained.

**Demonstration — why SST = SSR + SSE (the cross term vanishes)**

1. **Split each centered response.** Write $y_i - \bar y = (\hat y_i - \bar y) + (y_i - \hat y_i)$ — just adding and subtracting $\hat y_i$. The second bracket is the residual $e_i$. Square both sides and sum over $i$:

   $$\text{SST}=\sum\big[(\hat y_i-\bar y)+e_i\big]^2=\underbrace{\sum(\hat y_i-\bar y)^2}_{\text{SSR}}+\underbrace{\sum e_i^2}_{\text{SSE}}+2\sum(\hat y_i-\bar y)e_i.$$

   *Reason:* the algebraic identity $(a+b)^2 = a^2 + b^2 + 2ab$ applied term by term, then summed.
2. **Show the cross term is zero.** Since $\hat y_i - \bar y = \hat\beta_1(x_i - \bar x)$ (from §s3 step 1), the cross term is $2\hat\beta_1\sum(x_i - \bar x)e_i = 2\hat\beta_1\big(\sum x_i e_i - \bar x\sum e_i\big)$. The normal equations from §s1/§s2 say exactly $\sum e_i = 0$ and $\sum x_i e_i = 0$. *Reason:* both are the first-order conditions of least squares — the residuals are built to satisfy them.
3. **Conclude.** With both sums zero the cross term is $0$, leaving $\text{SST} = \text{SSR} + \text{SSE}$. *Reason:* substitute the zeros from step 2 into step 1.

*Geometrically (anticipating §s6): the residual vector is perpendicular to the fitted-value direction, so SST = SSR + SSE is the Pythagorean theorem in $n$-dimensional space.*

**The coefficient of determination**

$$R^2 = \frac{\text{SSR}}{\text{SST}} = 1 - \frac{\text{SSE}}{\text{SST}}$$

$R^2$ (read "R-squared") is the **fraction of the variance in $y$ explained by the model** — a number between $0$ (the line explains nothing) and $1$ (the line explains everything). The two forms are equal because $\text{SSR} = \text{SST} - \text{SSE}$ from the decomposition, so $\text{SSR}/\text{SST} = 1 - \text{SSE}/\text{SST}$. In simple regression, $R^2 = r^2$ exactly (the square of the correlation from §s1).

**Worked example (continued).** $\text{SST} = S_{yy} = 320$ and $\text{SSE} = 6.4$, so $R^2 = 1 - 6.4/320 = 1 - 0.02 = 0.98$. The line explains 98% of the score variation. Check against correlation: $r = 0.990$ (from §s1) gives $r^2 = 0.980$ — the identity $R^2 = r^2$ holds.

> **Concept — R² is necessary but not sufficient**
>
> A high $R^2$ does *not* certify a correct model. It can be inflated by piling on junk predictors, and it says nothing about whether the line shape, the constant variance, or the independence assumptions actually hold. **Anscombe's quartet** — four datasets with identical $R^2$ but wildly different shapes (one curved, one driven by a single outlier) — is the classic warning. Always look at the **residual plots** as well.

**Residual diagnostics — what to plot, what it reveals**

A **residual plot** graphs the leftovers $e_i$ to expose patterns the single number $R^2$ hides.

- ***Residuals vs fitted values:*** ideally a shapeless horizontal band. A curved band signals **nonlinearity** (the straight-line form is wrong); a funnel (spreading out) signals **heteroscedasticity** (non-constant variance).
- ***Q–Q plot of residuals:*** plots sorted residuals against the values a Normal would produce; points hugging the diagonal support Normal errors, systematic departures flag non-Normality.
- ***Residuals vs order/time:*** waves or runs flag **autocorrelation** (errors correlated across observations).
- ***Leverage & Cook's distance:*** numerical measures identifying high-influence points that single-handedly steer the fit (a single far-out $x$ can dominate).

> **Principle — the four assumptions, mnemonic "LINE"**
>
> **L**inearity of the mean response, **I**ndependence of the errors, **N**ormality of the errors (needed for *exact* $t$/$F$ inference, not for unbiasedness), and **E**qual variance (homoscedasticity). The diagnostics above are how you check each letter. Violations do not always invalidate the fit, but they change which inferences you can trust.

> **Connection — to the Statistics guide's correlation**
>
> The identity $R^2 = r^2$ ties this section straight back to the introductory guide: the correlation $r$ you computed there *is* the square root of the variance explained here. Regression promotes correlation from "do they move together?" to "by how much, and how reliably?"

## Part B · Multiple linear regression

<a id="s5"></a>
### The multiple regression model in matrix form

*With many predictors, scalar algebra becomes unwieldy. Linear algebra makes the whole theory compact and exact.*

First, the language of **matrices and vectors**, defined plainly. A **vector** is an ordered list of numbers, written as a column; e.g. $\mathbf{y}$ stacks all $n$ responses $y_1, \dots, y_n$. A **matrix** is a rectangular grid of numbers with rows and columns; "$n \times p$" means $n$ rows and $p$ columns. The **transpose** (superscript $^\top$) flips a matrix over its diagonal, turning rows into columns; for a column vector, $\mathbf{a}^\top \mathbf{b} = \sum a_i b_i$ is the **dot product** (multiply matching entries and add) — this is how matrix notation hides a $\sum$. **Matrix multiplication** $\mathbf{A}\mathbf{B}$ combines rows of $\mathbf{A}$ with columns of $\mathbf{B}$ by dot products. The **identity matrix** $\mathbf{I}$ has $1$s on its diagonal and $0$s elsewhere and acts like the number $1$. The **inverse** $\mathbf{A}^{-1}$ is the matrix that undoes $\mathbf{A}$, satisfying $\mathbf{A}^{-1}\mathbf{A} = \mathbf{I}$ (it exists only when $\mathbf{A}$ is square and non-degenerate).

**The model, stacked into matrices**

$$\mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon},\qquad E[\boldsymbol{\varepsilon}]=\mathbf{0},\quad \operatorname{Cov}(\boldsymbol{\varepsilon})=\sigma^2\mathbf{I}$$

$$\mathbf{y}\in\mathbb{R}^{n},\quad \mathbf{X}\in\mathbb{R}^{n\times p},\quad \boldsymbol{\beta}\in\mathbb{R}^{p}$$

Reading it: $\mathbf{y}$ is the length-$n$ vector of responses; $\mathbf{X}$ is the $n \times p$ **design matrix** whose row $i$ holds observation $i$'s predictors (usually a leading column of all $1$s to carry the intercept); $\boldsymbol\beta$ is the length-$p$ vector of coefficients; $\boldsymbol\varepsilon$ is the length-$n$ error vector. The notation "$\in \mathbb{R}^n$" means "is a list of $n$ real numbers." $E[\boldsymbol\varepsilon] = \mathbf{0}$ says every error averages to zero. $\operatorname{Cov}(\boldsymbol\varepsilon) = \sigma^2\mathbf{I}$ is the **covariance matrix** of the errors: its diagonal $\sigma^2$ says each error has the same variance (homoscedasticity), and its zero off-diagonals say different errors are uncorrelated (independence). The single line $\mathbf{y} = \mathbf{X}\boldsymbol\beta + \boldsymbol\varepsilon$ encodes all $n$ scalar equations $y_i = \beta_0 + \beta_1 x_{i1} + \cdots + \varepsilon_i$ at once.

> **Concept — the design matrix $\mathbf{X}$**
>
> $\mathbf{X}$ is called the **design matrix** because in a planned experiment you literally choose (design) its entries. Its columns can be raw predictors, transformations ($x^2$, $\log x$), **dummy variables** for categories (§s9), or interactions — anything *linear in the coefficients*. "Linear model" means linear in $\boldsymbol\beta$, **not** in $x$: the curve $y = \beta_0 + \beta_1 x + \beta_2 x^2$ is a perfectly valid linear model because it is a weighted sum of the *known* quantities $1, x, x^2$ with unknown weights $\boldsymbol\beta$.

**Worked example — a tiny design matrix.** For the five students, predicting score from study hours with an intercept, the design matrix and vectors are

$$\mathbf{X}=\begin{bmatrix}1&1\\1&2\\1&3\\1&4\\1&5\end{bmatrix},\qquad \mathbf{y}=\begin{bmatrix}52\\58\\61\\70\\74\end{bmatrix},\qquad \boldsymbol\beta=\begin{bmatrix}\beta_0\\\beta_1\end{bmatrix}.$$

Row $i$ reads "$1 \cdot \beta_0 + x_i \cdot \beta_1$," reproducing $\hat y_i = \beta_0 + \beta_1 x_i$. We solve this exact system in §s6.

**Interpreting a coefficient**

*$\beta_j$ is the expected change in $y$ for a one-unit increase in the $j$-th predictor $x_j$, **holding all other predictors fixed**. This "all else equal" clause is what separates multiple regression from a pile of separate simple regressions — each coefficient is automatically *adjusted* for the others. For example, a coefficient on "bedrooms" in a house-price model is the value of one more bedroom among houses of the same size, not confounded with the fact that bigger houses tend to have more bedrooms.*

> **Connection — to linear algebra**
>
> From here on, regression *is* linear algebra: fitting is solving a linear system, the fit is an orthogonal **projection**, the coefficient variances live inside $(\mathbf{X}^\top\mathbf{X})^{-1}$, and **collinearity** (predictors nearly redundant) is near-singularity of that matrix. The **eigenvalues** of $\mathbf{X}^\top\mathbf{X}$ govern numerical stability. Everything reduces to vectors, matrices, and the geometry of subspaces.

<a id="s6"></a>
### Least squares via linear algebra: the normal equations & hat matrix

*The single most important computation in the subject — and its beautiful geometric meaning as projection.*

**The normal equations & the OLS estimator**

$$\mathbf{X}^\top\mathbf{X}\,\hat{\boldsymbol{\beta}} = \mathbf{X}^\top\mathbf{y}\quad\Longrightarrow\quad \hat{\boldsymbol{\beta}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$$

The left equation is the matrix form of the normal equations (one per coefficient); the right one solves it by multiplying through by the inverse $(\mathbf{X}^\top\mathbf{X})^{-1}$.

*This is valid whenever $\mathbf{X}$ has **full column rank** — meaning no predictor column is an exact weighted combination of the others (no exact collinearity) — because that is precisely when the square matrix $\mathbf{X}^\top\mathbf{X}$ has an inverse.*

**Demonstration — deriving the normal equations by matrix calculus**

1. **Write the loss as a squared length.** The **norm** $\|\mathbf{v}\|$ of a vector is its length, and $\|\mathbf{v}\|^2 = \mathbf{v}^\top\mathbf{v}$ is the sum of its squared entries. So the total squared misfit is

   $$S(\boldsymbol{\beta})=\|\mathbf{y}-\mathbf{X}\boldsymbol{\beta}\|^2=(\mathbf{y}-\mathbf{X}\boldsymbol{\beta})^\top(\mathbf{y}-\mathbf{X}\boldsymbol{\beta}).$$

   *Reason:* $\mathbf{y} - \mathbf{X}\boldsymbol\beta$ is the residual vector, and summing its squared entries is exactly $\sum e_i^2$ from §s1 — the same loss, in matrix dress.
2. **Expand the product.** Multiplying out and using $(\mathbf{X}\boldsymbol\beta)^\top = \boldsymbol\beta^\top\mathbf{X}^\top$ (the transpose reverses order) and the fact that the scalar $\boldsymbol\beta^\top\mathbf{X}^\top\mathbf{y}$ equals its own transpose $\mathbf{y}^\top\mathbf{X}\boldsymbol\beta$:

   $$S=\mathbf{y}^\top\mathbf{y}-2\boldsymbol{\beta}^\top\mathbf{X}^\top\mathbf{y}+\boldsymbol{\beta}^\top\mathbf{X}^\top\mathbf{X}\boldsymbol{\beta}.$$

   *Reason:* distribute the transpose-product and combine the two equal cross terms into $-2$.
3. **Take the gradient and set it to zero.** The **gradient** $\nabla_{\boldsymbol\beta}$ is the vector of partial derivatives with respect to each coefficient. Two standard matrix-calculus rules apply: $\nabla(\boldsymbol\beta^\top\mathbf{a}) = \mathbf{a}$ and $\nabla(\boldsymbol\beta^\top\mathbf{M}\boldsymbol\beta) = 2\mathbf{M}\boldsymbol\beta$ for symmetric $\mathbf{M}$ (here $\mathbf{M} = \mathbf{X}^\top\mathbf{X}$ is symmetric). Thus

   $$\nabla_{\boldsymbol\beta}S=-2\mathbf{X}^\top\mathbf{y}+2\mathbf{X}^\top\mathbf{X}\boldsymbol{\beta}=\mathbf{0}.$$

   *Reason:* apply the two gradient rules to the three terms of step 2 (the constant $\mathbf{y}^\top\mathbf{y}$ has zero gradient).
4. **Rearrange and solve.** Move the first term across and divide by $2$:

   $$\mathbf{X}^\top\mathbf{X}\,\hat{\boldsymbol\beta}=\mathbf{X}^\top\mathbf{y}\;\Rightarrow\;\hat{\boldsymbol\beta}=(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}.$$

   *Reason:* algebra, then left-multiply both sides by the inverse $(\mathbf{X}^\top\mathbf{X})^{-1}$, which cancels to the identity on the left.
5. **Confirm a minimum.** The Hessian (second-derivative matrix) is $2\mathbf{X}^\top\mathbf{X}$. For any nonzero vector $\mathbf{v}$, $\mathbf{v}^\top(\mathbf{X}^\top\mathbf{X})\mathbf{v} = \|\mathbf{X}\mathbf{v}\|^2 \ge 0$, so the Hessian is **positive semidefinite** — and strictly positive definite when $\mathbf{X}$ has full column rank (then $\mathbf{X}\mathbf{v} \ne \mathbf{0}$). *Reason:* the second-derivative test; a positive-definite Hessian guarantees the unique global minimum.

*This is the same "set the derivative to zero" move as §s1 — now in vector form, solving for every coefficient simultaneously.*

**Worked example (continued).** For the students' $\mathbf{X}$ above, $\mathbf{X}^\top\mathbf{X} = \begin{bmatrix} n & \sum x_i \\ \sum x_i & \sum x_i^2\end{bmatrix} = \begin{bmatrix} 5 & 15 \\ 15 & 55\end{bmatrix}$ (since $\sum x_i = 15$, $\sum x_i^2 = 1+4+9+16+25 = 55$), and $\mathbf{X}^\top\mathbf{y} = \begin{bmatrix}\sum y_i \\ \sum x_i y_i\end{bmatrix} = \begin{bmatrix} 315 \\ 1003\end{bmatrix}$ (since $\sum x_i y_i = 52+116+183+280+370 = 1003$). The inverse of a $2\times2$ matrix $\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}$ is $\frac{1}{ad-bc}\begin{psmallmatrix}d&-b\\-c&a\end{psmallmatrix}$; here $ad-bc = 5\cdot55 - 15\cdot15 = 275 - 225 = 50$, so $(\mathbf{X}^\top\mathbf{X})^{-1} = \frac{1}{50}\begin{psmallmatrix}55 & -15 \\ -15 & 5\end{psmallmatrix}$. Then

$$\hat{\boldsymbol\beta}=\frac{1}{50}\begin{bmatrix}55&-15\\-15&5\end{bmatrix}\begin{bmatrix}315\\1003\end{bmatrix}=\frac{1}{50}\begin{bmatrix}55\cdot315-15\cdot1003\\-15\cdot315+5\cdot1003\end{bmatrix}=\frac{1}{50}\begin{bmatrix}2310\\280\end{bmatrix}=\begin{bmatrix}46.2\\5.6\end{bmatrix}.$$

The matrix machinery reproduces $\hat\beta_0 = 46.2$, $\hat\beta_1 = 5.6$ from §s1 exactly — confirming the two derivations agree.

**The hat matrix**

$$\hat{\mathbf{y}}=\mathbf{X}\hat{\boldsymbol\beta}=\underbrace{\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top}_{\mathbf{H}}\,\mathbf{y}=\mathbf{H}\mathbf{y}$$

*The matrix $\mathbf{H}$ is the **hat matrix** because it "puts the hat on $\mathbf{y}$" — it turns observed responses into fitted ones. Its diagonal entries $h_{ii}$ are the **leverages**, measuring how strongly each observation pulls its own fitted value (high leverage = an extreme predictor value with outsized influence). The residual vector is $\mathbf{e} = \mathbf{y} - \hat{\mathbf{y}} = (\mathbf{I} - \mathbf{H})\mathbf{y}$.*

**Demonstration — $\mathbf{H}$ is a projection (symmetric & idempotent)**

A matrix that is both **symmetric** ($\mathbf{H}^\top = \mathbf{H}$) and **idempotent** ($\mathbf{H}^2 = \mathbf{H}$, applying it twice does no more than once) is precisely an **orthogonal projection** — it drops any vector perpendicularly onto a subspace.

1. **Symmetric.** Because $(\mathbf{X}^\top\mathbf{X})^{-1}$ is symmetric (the inverse of a symmetric matrix is symmetric), and transposing reverses the order of a product:

   $$\mathbf{H}^\top=\big(\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\big)^\top=\mathbf{X}\big((\mathbf{X}^\top\mathbf{X})^{-1}\big)^\top\mathbf{X}^\top=\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top=\mathbf{H}.$$

   *Reason:* the transpose rule $(\mathbf{A}\mathbf{B}\mathbf{C})^\top = \mathbf{C}^\top\mathbf{B}^\top\mathbf{A}^\top$ and symmetry of the inner inverse.
2. **Idempotent.** Multiplying $\mathbf{H}$ by itself, the inner $\mathbf{X}^\top\mathbf{X}$ meets its own inverse and cancels to $\mathbf{I}$:

   $$\mathbf{H}^2=\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\underbrace{\mathbf{X}^\top\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}}_{=\,\mathbf{I}}\mathbf{X}^\top=\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top=\mathbf{H}.$$

   *Reason:* $(\mathbf{X}^\top\mathbf{X})(\mathbf{X}^\top\mathbf{X})^{-1} = \mathbf{I}$ by definition of the inverse, and $\mathbf{I}$ drops out of products.
3. **Therefore a projection onto the column space of $\mathbf{X}$.** Symmetric + idempotent = orthogonal projection. The subspace it projects onto is the **column space** of $\mathbf{X}$ (all vectors reachable as $\mathbf{X}\boldsymbol\beta$, i.e. all possible fitted vectors). So $\hat{\mathbf{y}} = \mathbf{H}\mathbf{y}$ is the *closest point* in that subspace to $\mathbf{y}$. *Reason:* the defining theorem of orthogonal projections.
4. **Residual is orthogonal to the predictors.** Compute $\mathbf{X}^\top\mathbf{e} = \mathbf{X}^\top(\mathbf{I}-\mathbf{H})\mathbf{y} = \mathbf{X}^\top\mathbf{y} - \mathbf{X}^\top\mathbf{H}\mathbf{y}$. But $\mathbf{X}^\top\mathbf{H} = \mathbf{X}^\top\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top = \mathbf{X}^\top$, so $\mathbf{X}^\top\mathbf{e} = \mathbf{X}^\top\mathbf{y} - \mathbf{X}^\top\mathbf{y} = \mathbf{0}$. *Reason:* this is exactly the normal equations $\mathbf{X}^\top\mathbf{X}\hat{\boldsymbol\beta} = \mathbf{X}^\top\mathbf{y}$ restated — the residual is perpendicular to every predictor column.

*Least squares is dropping a perpendicular from $\mathbf{y}$ onto the space spanned by the predictors. The decomposition SST = SSR + SSE from §s4 is the Pythagorean theorem for the resulting right triangle.*

**Covariance of the estimator**

$$\operatorname{Cov}(\hat{\boldsymbol\beta})=\sigma^2(\mathbf{X}^\top\mathbf{X})^{-1}$$

The **covariance matrix** $\operatorname{Cov}(\hat{\boldsymbol\beta})$ collects the variances of each coefficient (on its diagonal) and the covariances between pairs (off-diagonal). Its diagonal square roots are the standard errors. *Geometrically: directions in which the predictors carry little variation (small eigenvalues of $\mathbf{X}^\top\mathbf{X}$) produce large coefficient variance — the seed of multicollinearity in §s7.*

**Demonstration — the covariance formula.** Writing $\hat{\boldsymbol\beta} = \mathbf{A}\mathbf{y}$ with the constant matrix $\mathbf{A} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top$, the rule $\operatorname{Cov}(\mathbf{A}\mathbf{y}) = \mathbf{A}\operatorname{Cov}(\mathbf{y})\mathbf{A}^\top$ with $\operatorname{Cov}(\mathbf{y}) = \sigma^2\mathbf{I}$ gives $\operatorname{Cov}(\hat{\boldsymbol\beta}) = \sigma^2\mathbf{A}\mathbf{A}^\top = \sigma^2(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1} = \sigma^2(\mathbf{X}^\top\mathbf{X})^{-1}$, since the middle $\mathbf{X}^\top\mathbf{X}$ cancels one inverse. *Reason:* the linear-transformation rule for covariance and the inverse-cancellation from step 2 above.

**Worked example (continued).** With $\sigma^2$ estimated by $s^2 = 2.133$ and $(\mathbf{X}^\top\mathbf{X})^{-1} = \frac{1}{50}\begin{psmallmatrix}55&-15\\-15&5\end{psmallmatrix}$, the slope's variance is the bottom-right entry times $s^2$: $\frac{5}{50}\times 2.133 = 0.1\times 2.133 = 0.2133$, so $\operatorname{SE}(\hat\beta_1) = \sqrt{0.2133} = 0.462$ — matching §s3 exactly.

> **Connection — projection & eigenvalues from linear algebra**
>
> $\mathbf{H}$ is the projection matrix; its **trace** (sum of diagonal entries) equals $p$, the number of coefficients, which is the model's degrees of freedom — it counts the dimension of the column space. The eigenvalues of $\mathbf{X}^\top\mathbf{X}$ decide both the numerical stability of the inverse and the variance of $\hat{\boldsymbol\beta}$ — the very eigenvalue/conditioning ideas from linear algebra.

<a id="s7"></a>
### Inference, multicollinearity & model selection

*Testing individual coefficients, diagnosing when predictors fight each other, and choosing which to keep.*

**t-test for a single coefficient**

$$t_j = \frac{\hat\beta_j}{\operatorname{SE}(\hat\beta_j)},\qquad \operatorname{SE}(\hat\beta_j)=s\sqrt{[(\mathbf{X}^\top\mathbf{X})^{-1}]_{jj}}$$

The notation $[(\mathbf{X}^\top\mathbf{X})^{-1}]_{jj}$ means the $j$-th diagonal entry of that inverse matrix — the per-coefficient piece of the covariance from §s6. The ratio $t_j$ measures how many standard errors the estimate sits away from zero.

*Under $H_0:\beta_j=0$ this follows a $t$-distribution with $n-p$ degrees of freedom ($n$ observations minus $p$ estimated coefficients). Crucially it tests $x_j$'s contribution **given all other predictors are already in the model** — a partial effect, not a standalone one.*

> **Concept — multicollinearity**
>
> When two or more predictors are highly correlated, the matrix $\mathbf{X}^\top\mathbf{X}$ becomes nearly **singular** (its determinant near zero, equivalently it has tiny eigenvalues), so its inverse $(\mathbf{X}^\top\mathbf{X})^{-1}$ has huge entries — and by §s6 the coefficient standard errors explode. Tell-tale symptoms: a strongly significant overall $F$-test (§s8) but no significant individual $t$'s; coefficients with the "wrong" sign that swing wildly when one predictor is added or dropped. Multicollinearity harms *interpretation and stability*, but not necessarily prediction.

**The variance inflation factor**

$$\operatorname{VIF}_j=\frac{1}{1-R_j^2}$$

Here $R_j^2$ is the $R^2$ obtained by regressing predictor $x_j$ on *all the other predictors*. If $x_j$ is nearly predictable from the others, $R_j^2$ is near $1$ and the VIF blows up. *A rule of thumb: $\operatorname{VIF}_j > 5$ to $10$ flags problematic collinearity — the variance of $\hat\beta_j$ is inflated by exactly that factor compared with a perfectly orthogonal design.*

**Worked example — VIF.** If regressing $x_2$ on the remaining predictors yields $R_2^2 = 0.9$, then $\operatorname{VIF}_2 = 1/(1-0.9) = 10$: the standard error of $\hat\beta_2$ is $\sqrt{10} \approx 3.16$ times larger than it would be if $x_2$ were uncorrelated with the others. A modest $R_2^2 = 0.5$ gives only $\operatorname{VIF}_2 = 2$ ($\sqrt2 \approx 1.41$ times inflation) — usually tolerable.

| Criterion | Formula / idea | What it rewards |
| --- | --- | --- |
| Adjusted $R^2$ | $1-\dfrac{\text{SSE}/(n-p)}{\text{SST}/(n-1)}$ | fit, penalizing extra parameters |
| AIC | $2p-2\ln\hat L$ | predictive fit, light penalty |
| BIC | $p\ln n-2\ln\hat L$ | parsimony, heavier penalty (grows with $n$) |
| Mallows' $C_p$ | $\dfrac{\text{SSE}_p}{\hat\sigma^2}-n+2p$ | low bias with few predictors |
| Cross-validation | held-out prediction error | honest out-of-sample accuracy |

Reading the table: **adjusted $R^2$** is plain $R^2$ docked for each extra parameter, so it can fall when a useless predictor is added. **AIC** and **BIC** combine the maximized log-likelihood $\ln\hat L$ (how well the model fits, §s10) with a penalty proportional to the number of parameters $p$; BIC's penalty $p\ln n$ grows with sample size, so it prefers simpler models in large samples. **Mallows' $C_p$** estimates prediction error. **Cross-validation** repeatedly holds out part of the data, fits on the rest, and measures error on the held-out part — the most honest gauge of out-of-sample accuracy.

> **Principle — selection is a bias–variance compromise**
>
> Adding predictors *always* lowers the training SSE (more freedom to fit), but past a point it raises *test* error by fitting noise — **overfitting**. Every criterion above trades fit against complexity; they differ only in how steep the complexity penalty is. Stepwise selection is convenient but optimistic — it quietly invalidates the usual p-values by peeking at the data many times — so cross-validation and regularization (§s12) are the modern defaults.

> **Connection — to MLE and information criteria**
>
> AIC and BIC are built from the maximized **log-likelihood** $\ln\hat L$ — the same maximum-likelihood machinery from the Inference guide. Under Normal errors, maximizing the likelihood is the same as minimizing SSE, so least squares and maximum likelihood agree, and these criteria simply add a complexity tax on top of the log-likelihood.

<a id="s8"></a>
### ANOVA & the F-test

*One test for the whole model: is the set of predictors, taken together, better than nothing?*

**ANOVA** stands for **An**alysis **o**f **Va**riance — the technique of splitting total variation into named pieces (as in §s4) and comparing them.

**The overall F-test**

$$F=\frac{\text{SSR}/(p-1)}{\text{SSE}/(n-p)}=\frac{\text{MSR}}{\text{MSE}}$$

The numerator is the **mean square for regression** $\text{MSR} = \text{SSR}/(p-1)$ — explained variation per explanatory degree of freedom; the denominator is the **mean square error** $\text{MSE} = \text{SSE}/(n-p)$ — leftover variation per residual degree of freedom (this is the same $s^2$ from §s2, generalized). A "mean square" is just a sum of squares divided by its degrees of freedom.

*Under the null hypothesis $H_0:\beta_1=\cdots=\beta_{p-1}=0$ (all slopes zero — the predictors collectively useless), $F$ follows an **$F$-distribution** with $p-1$ and $n-p$ degrees of freedom. A large $F$ means the model explains far more variation per parameter than the residual noise, so at least one predictor matters.*

| Source | Sum of squares | df | Mean square | F |
| --- | --- | --- | --- | --- |
| Regression | $\text{SSR}=\sum(\hat y_i-\bar y)^2$ | $p-1$ | $\text{MSR}=\text{SSR}/(p-1)$ | $\text{MSR}/\text{MSE}$ |
| Error | $\text{SSE}=\sum(y_i-\hat y_i)^2$ | $n-p$ | $\text{MSE}=\text{SSE}/(n-p)$ |   |
| Total | $\text{SST}=\sum(y_i-\bar y)^2$ | $n-1$ |   |   |

**Demonstration — building the F-ratio**

1. **Partition variation and degrees of freedom.** From §s4, $\text{SST} = \text{SSR} + \text{SSE}$; the degrees of freedom split to match, $(n-1) = (p-1) + (n-p)$. *Reason:* the sums-of-squares decomposition and simple arithmetic on the df.
2. **Each piece is a scaled chi-square.** A **chi-square** distribution with $k$ degrees of freedom (written $\chi^2_k$) is the distribution of a sum of $k$ squared independent standard Normals. Under Normal errors and $H_0$, $\text{SSR}/\sigma^2 \sim \chi^2_{p-1}$ and $\text{SSE}/\sigma^2 \sim \chi^2_{n-p}$, and they are *independent* because $\mathbf{H}$ (which builds the fitted values) and $\mathbf{I} - \mathbf{H}$ (which builds the residuals) project onto perpendicular subspaces, as shown in §s6. *Reason:* sums of squares of Normal projections are chi-squares, and projections onto orthogonal subspaces are independent.
3. **Form the F-ratio.** An $F$ random variable with $(d_1, d_2)$ degrees of freedom is by definition the ratio of two independent chi-squares, each divided by its own df:

   $$F=\frac{(\text{SSR}/\sigma^2)/(p-1)}{(\text{SSE}/\sigma^2)/(n-p)}=\frac{\text{SSR}/(p-1)}{\text{SSE}/(n-p)}=\frac{\text{MSR}}{\text{MSE}}\sim F_{p-1,\,n-p}.$$

   *Reason:* the definition of the $F$-distribution; note the unknown $\sigma^2$ cancels top and bottom, so we never need its value.
4. **Interpret the scale.** Under $H_0$ one can show $E[\text{MSR}] = E[\text{MSE}] = \sigma^2$, so $F \approx 1$ when the predictors are useless; a genuine signal inflates SSR and pushes $F$ well above $1$. *Reason:* expected mean squares under the null.

*In simple regression ($p = 2$) the overall $F$ equals exactly the square of the slope's $t$-statistic — the two tests coincide.*

**Worked example (continued).** For the students, $\text{SSR} = \text{SST} - \text{SSE} = 320 - 6.4 = 313.6$, with $p - 1 = 1$ and $n - p = 3$. So $\text{MSR} = 313.6/1 = 313.6$, $\text{MSE} = 6.4/3 = 2.133$, and $F = 313.6/2.133 = 147.0$. Check the simple-regression identity: the slope's $t = 12.1$ (§s3), and $t^2 = 12.1^2 = 146.4 \approx F$ (small rounding). The 5% critical value $F_{1,3} = 10.13$ is far exceeded, so the predictor is highly significant.

> **Concept — the partial (nested) F-test**
>
> To test a *subset* of coefficients rather than all of them, compare a **full** model to a **reduced** one that omits those $q$ predictors:
>
> $$F=\dfrac{(\text{SSE}_{\text{red}}-\text{SSE}_{\text{full}})/q}{\text{SSE}_{\text{full}}/(n-p)}.$$
>
> The numerator is the **extra sum of squares** explained by the dropped predictors. This is the engine behind comparing nested models, and it is how a categorical variable with several levels (§s9) is tested as a single block.

> **Connection — same ANOVA, same F as the Statistics guide**
>
> The one-way ANOVA of the intro guide ("between-group variance over within-group variance") is a special case of this regression ANOVA, using group-membership dummy variables as the predictors. Same $F$-distribution, same chi-square-ratio logic carried over from the Probability and Inference guides.

<a id="s9"></a>
### Categorical predictors, interactions & transformations

*How to feed categories, curvature, and conditional effects into a model that is still "linear."*

A **categorical predictor** takes labels, not numbers — colour, city, treatment group. We cannot multiply a coefficient by "red," so we encode categories numerically.

**Dummy (indicator) coding**

$$x_{\text{group B}}=\begin{cases}1 & \text{if obs is in group B}\\ 0 & \text{otherwise}\end{cases}$$

A **dummy** (or **indicator**) variable is $1$ when an observation belongs to a given category and $0$ otherwise. *A $k$-level category needs $k-1$ dummies; the omitted level is the **baseline** against which the others are compared. Including all $k$ dummies **and** an intercept makes $\mathbf{X}$ rank-deficient — the dummies sum to the all-ones intercept column, an exact collinearity called the **dummy variable trap** (the inverse in §s6 fails to exist).*

> **Concept — what a dummy coefficient means**
>
> In the model $y = \beta_0 + \beta_1 D$ with a single dummy $D$, the intercept $\beta_0$ is the mean $y$ in the baseline group ($D=0$), and $\beta_1$ is the *difference* in mean $y$ between the $D=1$ group and the baseline. With a numeric predictor also present, a dummy shifts the **intercept** — producing parallel lines at different heights, one per group. To let the *slope* differ by group, we need an interaction.

**Worked example — a dummy.** Suppose two teaching methods, with method B coded $D = 1$. Fitting $y = \beta_0 + \beta_1 x + \beta_2 D$ and obtaining $\hat\beta_0 = 46$, $\hat\beta_1 = 5.6$, $\hat\beta_2 = 3$ means: both methods have the same slope $5.6$ points per hour, but method B scores on average $3$ points higher at every study level (its line is shifted up by $\hat\beta_2 = 3$).

**Interaction terms**

$$y=\beta_0+\beta_1 x+\beta_2 D+\beta_3\,(x\cdot D)+\varepsilon$$

An **interaction** is a product term ($x \cdot D$) that lets one predictor's effect depend on another. *For the baseline group $D=0$ the term vanishes and the slope in $x$ is $\beta_1$; for $D=1$ the slope becomes $\beta_1 + \beta_3$. So $\beta_3$ measures how much the effect of $x$ **changes** between groups — non-parallel lines. Interactions between two numeric predictors work identically via $\beta_3\, x_1 x_2$.*

**Demonstration — reading the two slopes.** Substitute the two values of $D$ into the model. For $D=0$: $y = \beta_0 + \beta_1 x + 0 + 0 = \beta_0 + \beta_1 x$, a line with intercept $\beta_0$ and slope $\beta_1$. For $D=1$: $y = \beta_0 + \beta_1 x + \beta_2 + \beta_3 x = (\beta_0 + \beta_2) + (\beta_1 + \beta_3)x$, a line with intercept $\beta_0 + \beta_2$ and slope $\beta_1 + \beta_3$. *Reason:* direct substitution and grouping the constant and $x$ terms. Thus $\beta_2$ shifts the intercept and $\beta_3$ shifts the slope — exactly the "different height, different tilt" picture.

**Transformations.** Because "linear" means linear in $\boldsymbol\beta$ (§s5), we may replace $x$ by any fixed function of it — $x^2$ for curvature, $\log x$ for diminishing returns, $1/x$, and so on — and still fit by ordinary least squares. For example $y = \beta_0 + \beta_1 x + \beta_2 x^2$ fits a parabola through the data using the very same normal equations, simply with a column of $x^2$ added to $\mathbf{X}$.

## Part C · Generalized models & beyond

<a id="s10"></a>
### Logistic regression

*When the response is a yes/no outcome, a straight line breaks down. The logit link fixes it.*

A **binary** response takes only two values, coded $0$ and $1$ (no/yes, fail/pass, healthy/sick). We model not the $0/1$ value itself but the **probability** $p = P(y = 1 \mid \mathbf{x})$ that the outcome is a $1$ given the predictors.

> **Concept — why not just fit a line to 0/1 data?**
>
> Fitting an ordinary line to a binary $y$ has two fatal flaws. First, a line eventually exceeds $1$ and drops below $0$, yet a probability must stay in $[0,1]$. Second, the errors of a $0/1$ variable are neither Normal nor of constant variance, so the inference of Part A is invalid. The cure is to model the probability $p$ and pass the linear predictor through a function that squeezes the whole real line into the open interval $(0,1)$ — the **logistic** (S-shaped, "sigmoid") curve.

**The logistic model & the logit link**

$$p(\mathbf{x})=\frac{1}{1+e^{-\boldsymbol{\beta}^\top\mathbf{x}}},\qquad \operatorname{logit}(p)=\ln\frac{p}{1-p}=\boldsymbol{\beta}^\top\mathbf{x}$$

The left equation is the sigmoid: as the linear predictor $\boldsymbol\beta^\top\mathbf{x}$ runs from $-\infty$ to $+\infty$, $p$ rises smoothly from $0$ to $1$. The **odds** of an event are $p/(1-p)$ (e.g. $p = 0.8$ gives odds $4$, "4 to 1"); the **logit** is the natural log of the odds. *The right equation says the log-odds are a plain linear function of the predictors. Consequently $e^{\beta_j}$ is an **odds ratio** — the multiplicative factor by which the odds of $y=1$ change for a one-unit increase in $x_j$.*

**Demonstration — the logit and the sigmoid are inverses.** Starting from $p = 1/(1 + e^{-\eta})$ with $\eta = \boldsymbol\beta^\top\mathbf{x}$: then $1 - p = e^{-\eta}/(1 + e^{-\eta})$, so the odds $p/(1-p) = 1/e^{-\eta} = e^{\eta}$, and taking logs gives $\ln\frac{p}{1-p} = \eta = \boldsymbol\beta^\top\mathbf{x}$. *Reason:* algebra on the sigmoid and the law of logarithms $\ln e^\eta = \eta$. The two displayed equations are therefore the same statement read in opposite directions.

**Demonstration — the log-likelihood and its score equations**

1. **Write the likelihood.** Each $y_i$ is a **Bernoulli** trial — a single $0/1$ draw — with success probability $p_i = p(\mathbf{x}_i)$. The probability of observing the value $y_i$ is $p_i$ if $y_i = 1$ and $1 - p_i$ if $y_i = 0$, compactly $p_i^{y_i}(1-p_i)^{1-y_i}$. Independent observations multiply:

   $$L(\boldsymbol\beta)=\prod_{i=1}^n p_i^{\,y_i}(1-p_i)^{1-y_i}.$$

   The **likelihood** $L$ is the probability of the observed data as a function of the unknown $\boldsymbol\beta$. *Reason:* the Bernoulli probability and independence (probabilities of independent events multiply).
2. **Take logs.** Logs turn the product into a sum and the powers into multipliers (a strictly increasing transform, so it does not move the maximizer):

   $$\ell(\boldsymbol\beta)=\ln L=\sum_{i=1}^n\Big[y_i\ln p_i+(1-y_i)\ln(1-p_i)\Big].$$

   *Reason:* $\ln(ab) = \ln a + \ln b$ and $\ln(a^c) = c\ln a$.
3. **Differentiate and set to zero.** Substituting $p_i = 1/(1+e^{-\boldsymbol\beta^\top\mathbf{x}_i})$ and using the sigmoid's derivative $\frac{\partial p_i}{\partial\boldsymbol\beta} = p_i(1-p_i)\mathbf{x}_i$, the algebra collapses neatly to the **score equations**:

   $$\frac{\partial\ell}{\partial\boldsymbol\beta}=\sum_{i=1}^n\big(y_i-p_i\big)\mathbf{x}_i=\mathbf{X}^\top(\mathbf{y}-\mathbf{p})=\mathbf{0}.$$

   *Reason:* the chain rule plus the sigmoid derivative; the maximum of the smooth log-likelihood occurs where its gradient is zero.
4. **Solve iteratively.** These equations are *nonlinear* in $\boldsymbol\beta$ because $p_i$ itself depends on $\boldsymbol\beta$, so there is no closed-form formula. They are solved numerically by **Newton–Raphson**, which in this context is **iteratively reweighted least squares (IRLS)** — repeatedly solving a weighted least-squares problem until the estimates stop changing. *Reason:* nonlinearity rules out a direct inverse; Newton's method finds the root of the gradient.

*Notice the residual $(y_i - p_i)$ is orthogonal to the predictors — the same orthogonality as OLS in §s6, now for the likelihood instead of squared error.*

**Worked example — odds ratio.** A logistic model of passing an exam on study hours gives $\hat\beta_1 = 0.8$. Then $e^{0.8} = 2.23$: each extra study hour multiplies the *odds* of passing by about $2.23$. If a student currently has odds $1$ (a 50% chance), one more hour raises the odds to $2.23$, i.e. probability $2.23/(1+2.23) = 0.69$.

> **Principle — interpretation by odds ratios & deviance**
>
> Coefficients live on the log-odds scale, so report $e^{\beta_j}$ as an odds ratio. Goodness of fit is judged by the **deviance** $-2\ell$ (the GLM analogue of SSE); nested models are compared by the **likelihood-ratio test**, in which the drop in deviance follows a $\chi^2$ distribution. Classification quality is summarized by the ROC curve and its area (AUC), not by $R^2$.

> **Connection — to MLE and the Bernoulli**
>
> Logistic regression is maximum likelihood for the Bernoulli distribution of the Probability guide, with its success probability steered by a linear predictor. The likelihood-ratio test reuses the asymptotic $\chi^2$ theory of the Inference guide. Linear regression was MLE for the Normal; this is MLE for the Bernoulli — the same principle, a different distribution.

<a id="s11"></a>
### Generalized linear models (GLMs)

*Linear and logistic regression are two members of one family. The GLM names the pattern.*

> **Concept — the three ingredients of a GLM**
>
> Every **generalized linear model** has (1) a **random component** — a response distribution drawn from the **exponential family** (a broad class including the Normal, Bernoulli, Poisson, and Gamma); (2) a **systematic component** — the linear predictor $\eta = \boldsymbol\beta^\top\mathbf{x}$, the familiar weighted sum; and (3) a **link function** $g$ that connects them by $g(E[y]) = \eta$. Picking the distribution and the link picks the specific model.

**The GLM template**

$$g\big(E[y\mid\mathbf{x}]\big)=\boldsymbol\beta^\top\mathbf{x},\qquad y\mid\mathbf{x}\sim \text{exponential family}$$

In words: a known function $g$ of the *mean* response equals the linear predictor, and the response scatters around that mean according to an exponential-family distribution. *Ordinary linear regression is the GLM with a Normal response and the **identity** link ($g(\mu) = \mu$); logistic regression is Bernoulli with the **logit** link; Poisson regression models counts with the **log** link.*

| Model | Response distribution | Link $g(\mu)$ | Inverse (mean) |
| --- | --- | --- | --- |
| Linear regression | Normal | identity: $\mu$ | $\eta$ |
| Logistic regression | Bernoulli / Binomial | logit: $\ln\frac{\mu}{1-\mu}$ | $\frac{1}{1+e^{-\eta}}$ |
| Probit regression | Bernoulli | probit: $\Phi^{-1}(\mu)$ | $\Phi(\eta)$ |
| Poisson regression | Poisson | log: $\ln\mu$ | $e^{\eta}$ |
| Gamma regression | Gamma | inverse: $1/\mu$ | $1/\eta$ |

The "Inverse (mean)" column undoes the link to recover the mean $\mu$ from the linear predictor $\eta$ — e.g. for Poisson, $\mu = e^\eta$ guarantees a positive count, and $\Phi$ in the probit row is the Normal cumulative distribution function.

> **Principle — the canonical link & unified fitting**
>
> Each exponential-family distribution has a natural **canonical link** (logit for Bernoulli, log for Poisson, identity for Normal) that makes the mathematics cleanest and forces the score equations into the unified form $\mathbf{X}^\top(\mathbf{y} - \boldsymbol\mu) = \mathbf{0}$ — exactly the orthogonality seen in §s6 and §s10. All GLMs are fit by one algorithm, **IRLS**, and compared by deviance and likelihood-ratio tests. One framework, many response types.

> **Connection — the exponential family ties Probability together**
>
> The Normal, Bernoulli, Poisson, and Gamma distributions of the Probability guide are all exponential-family members, and the GLM is the single regression framework that handles each. The link function generalizes the logit of §s10, and the identity link recovers the ordinary least squares of Parts A and B.

<a id="s12"></a>
### Regularization: ridge, lasso & the bias–variance tradeoff

*When predictors are many or collinear, plain OLS overfits. Shrinking the coefficients trades a little bias for a lot less variance.*

**Regularization** means adding a penalty term to the loss that discourages large coefficients, pulling them toward zero (this pulling is called **shrinkage**). The benefit is explained by the **bias–variance tradeoff** at the end of the section.

**Ridge regression (L2 penalty)**

$$\hat{\boldsymbol\beta}_{\text{ridge}}=\arg\min_{\boldsymbol\beta}\;\|\mathbf{y}-\mathbf{X}\boldsymbol\beta\|^2+\lambda\|\boldsymbol\beta\|_2^2$$

$$\hat{\boldsymbol\beta}_{\text{ridge}}=(\mathbf{X}^\top\mathbf{X}+\lambda\mathbf{I})^{-1}\mathbf{X}^\top\mathbf{y}$$

Here "$\arg\min$" means "the value of $\boldsymbol\beta$ that minimizes what follows." The added penalty $\lambda\|\boldsymbol\beta\|_2^2 = \lambda\sum\beta_j^2$ is the **squared L2 norm** (sum of squared coefficients) scaled by a chosen constant $\lambda \ge 0$ (the **tuning parameter**). Larger $\lambda$ shrinks coefficients harder; $\lambda = 0$ recovers ordinary least squares.

**Demonstration — the ridge closed form, and why it always inverts**

1. **Write the penalized objective.** $S(\boldsymbol\beta) = (\mathbf{y} - \mathbf{X}\boldsymbol\beta)^\top(\mathbf{y} - \mathbf{X}\boldsymbol\beta) + \lambda\boldsymbol\beta^\top\boldsymbol\beta$. *Reason:* squared error from §s6 plus the L2 penalty written as a dot product $\boldsymbol\beta^\top\boldsymbol\beta = \sum\beta_j^2$.
2. **Differentiate and set to zero.** Using the same gradient rules as §s6 ($\nabla(\boldsymbol\beta^\top\boldsymbol\beta) = 2\boldsymbol\beta$):

   $$\nabla S=-2\mathbf{X}^\top\mathbf{y}+2\mathbf{X}^\top\mathbf{X}\boldsymbol\beta+2\lambda\boldsymbol\beta=\mathbf{0}.$$

   *Reason:* the gradient of the squared-error part is $-2\mathbf{X}^\top\mathbf{y} + 2\mathbf{X}^\top\mathbf{X}\boldsymbol\beta$ (from §s6), plus $2\lambda\boldsymbol\beta$ from the penalty.
3. **Collect and solve.** Factor $\boldsymbol\beta$ from the two middle terms using $\mathbf{X}^\top\mathbf{X}\boldsymbol\beta + \lambda\boldsymbol\beta = (\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I})\boldsymbol\beta$ (the $\mathbf{I}$ lets us add the scalar $\lambda$ to a matrix):

   $$(\mathbf{X}^\top\mathbf{X}+\lambda\mathbf{I})\,\hat{\boldsymbol\beta}=\mathbf{X}^\top\mathbf{y}\;\Rightarrow\;\hat{\boldsymbol\beta}_{\text{ridge}}=(\mathbf{X}^\top\mathbf{X}+\lambda\mathbf{I})^{-1}\mathbf{X}^\top\mathbf{y}.$$

   *Reason:* algebra, then left-multiply by the inverse.
4. **Why it always inverts.** Adding $\lambda\mathbf{I}$ raises *every* eigenvalue of $\mathbf{X}^\top\mathbf{X}$ by $\lambda$. Since $\mathbf{X}^\top\mathbf{X}$ has all eigenvalues $\ge 0$, every eigenvalue of $\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I}$ is $\ge \lambda > 0$, so the matrix is strictly positive definite and therefore invertible — even when $p > n$ or predictors are perfectly collinear, cases where plain OLS fails outright. *Reason:* a matrix is invertible exactly when none of its eigenvalues is zero, and we have just bounded them all below by $\lambda$.

*Ridge is OLS with a numerically stabilized, better-conditioned normal-equations matrix — a direct cure for collinearity.*

**Worked example — ridge shrinkage.** Suppose in a one-predictor problem $\mathbf{X}^\top\mathbf{X} = 10$ and $\mathbf{X}^\top\mathbf{y} = 56$, so OLS gives $\hat\beta = 5.6$. With $\lambda = 5$, ridge gives $\hat\beta = 56/(10 + 5) = 56/15 = 3.73$ — shrunk toward zero. With $\lambda = 90$, $\hat\beta = 56/100 = 0.56$ — shrunk much further. As $\lambda \to \infty$ the coefficient is driven to $0$.

**Lasso (L1 penalty)**

$$\hat{\boldsymbol\beta}_{\text{lasso}}=\arg\min_{\boldsymbol\beta}\;\|\mathbf{y}-\mathbf{X}\boldsymbol\beta\|^2+\lambda\|\boldsymbol\beta\|_1$$

The **L1 norm** $\|\boldsymbol\beta\|_1 = \sum|\beta_j|$ sums the *absolute* sizes of the coefficients. Its constraint region (a diamond) has sharp corners exactly on the axes, so the minimizer frequently lands precisely at $\beta_j = 0$ — meaning **lasso performs automatic variable selection**, switching irrelevant predictors entirely off. There is no closed form (the absolute value is not differentiable at zero); it is solved by **coordinate descent** or the LARS algorithm. The **elastic net** blends the L1 and L2 penalties to get both selection and stability.

> **Principle — the bias–variance tradeoff**
>
> Expected prediction error splits into three parts: $\text{error} = \text{bias}^2 + \text{variance} + \sigma^2_{\text{irreducible}}$. **Bias** is systematic error (how far the average prediction is from the truth); **variance** is instability (how much the prediction jumps with new data); the **irreducible** part is the noise no model can remove. OLS is unbiased but can have enormous variance when predictors are many or collinear. Regularization deliberately *adds a little bias* (by shrinking) in order to *cut variance a lot*, lowering the total. The tuning parameter $\lambda$, chosen by cross-validation (§s7), slides the model along this tradeoff curve.

> **Connection — eigenvalues, Gauss–Markov & Bayes**
>
> Gauss–Markov (§s2) said OLS is best *among unbiased* estimators; ridge escapes that verdict by *allowing* bias, and so can beat OLS in total mean-squared error. The $\lambda\mathbf{I}$ term directly lifts the small eigenvalues of $\mathbf{X}^\top\mathbf{X}$ — the conditioning fix from linear algebra (§s6). And ridge is exactly the **Bayesian** posterior mode under a Normal prior on $\boldsymbol\beta$ (lasso under a Laplace prior) — connecting to the Bayes-theorem thread of the earlier guides.

<a id="s13"></a>
### A glimpse beyond: mixed models, time series & nonparametric regression

*Where the assumptions of ordinary regression break, three large extensions take over.*

**Mixed-effects models — when independence fails**

$$\mathbf{y}=\mathbf{X}\boldsymbol\beta+\mathbf{Z}\mathbf{b}+\boldsymbol\varepsilon,\qquad \mathbf{b}\sim N(\mathbf{0},\mathbf{G})$$

When data come in groups (students within schools, repeated measurements on the same patient), observations within a group are correlated, violating the independence assumption of §s5. The fix adds **random effects** $\mathbf{b}$ — group-level deviations modeled as a random draw $N(\mathbf{0}, \mathbf{G})$ (a Normal vector with mean zero and covariance matrix $\mathbf{G}$) — alongside the population-level **fixed effects** $\boldsymbol\beta$. The matrix $\mathbf{Z}$ maps each random effect to the rows it influences. Fitting uses restricted/maximum likelihood (REML/ML). *The fixed effects $\boldsymbol\beta$ describe the average relationship; the random effects $\mathbf{b}$ let each group depart from it.*

**Time series — when errors are autocorrelated**

*When observations are ordered in time, today's error tends to resemble yesterday's — **autocorrelation** — which breaks the uncorrelated-errors assumption behind Gauss–Markov. Models such as **AR($p$)** (autoregressive: regress the series on its own past $p$ values), **MA($q$)** (moving average of past shocks), and **ARIMA** (combining both with differencing for trends) handle this. Generalized least squares and the **Durbin–Watson** statistic detect and correct autocorrelated residuals. Here "hold other predictors fixed" is replaced by "extrapolate the dynamics forward."*

**Nonparametric regression — when the form is unknown**

$$y_i=f(x_i)+\varepsilon_i,\qquad f\ \text{flexible, not a fixed formula}$$

*When we cannot assume a straight line or any fixed equation, **nonparametric** methods let the data dictate the shape of $f$. **Splines** (smooth piecewise polynomials), **LOESS** (local fitting), **kernel smoothers** (weighted local averages), and **generalized additive models (GAMs)** all bend to follow the data. **Regression trees**, **random forests**, and **gradient boosting** push further into machine learning. In each, a **smoothing parameter** plays the role of $\lambda$ from §s12 on the very same bias–variance tradeoff — too flexible overfits, too rigid underfits.*

> **Principle — one loss-and-fit idea, ever generalizing**
>
> Every model in this guide is the same three-step story: **posit** a structure (a line, a plane, a link function, a flexible curve), **fit** it by optimizing a loss or a likelihood (set the gradient to zero — calculus), and **assess** it with honest, out-of-sample uncertainty. The mathematics scales from a single straight line all the way to deep learning without ever changing this skeleton.

> **Connection — the whole arc**
>
> Correlation (Statistics) → least squares as calculus optimization → projection & eigenvalues (linear algebra) → $t$/$F$ sampling distributions and MLE (Inference) → GLMs over the exponential family (Probability) → regularization as a Bayesian prior. Regression is where every earlier subject converges into one practical tool.

---

*A complete companion to regression and linear models — from the best straight line through a scatterplot to GLMs, regularization, and the frontier of mixed models and machine learning. Every core result is demonstrated, and threaded back to calculus (optimization), linear algebra (projection, eigenvalues), and the probability and inference that make the uncertainty honest. Read once for the shape; return to any box as a reference. Remember the skeleton: posit a structure, fit by minimizing a loss, assess with honest uncertainty.*
