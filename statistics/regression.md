# Regression, *the best line and beyond.*

From a single straight line through a cloud of points to the full machinery of linear models — least squares as calculus, the matrix geometry of projection, honest inference, and the generalizations (logistic, GLMs, ridge & lasso) that power modern data science. Every core result is **demonstrated**, and the threads back to calculus, probability, and linear algebra are made explicit.

[← Back to all guides](../README.md)

## Part A · Simple linear regression

<a id="s0"></a>
### The big picture: modeling relationships

Regression answers a question correlation only hints at: given that two (or many) variables move together, can we write down a *function* that predicts one from the others — and quantify how good that prediction is? It is the workhorse of applied statistics and the gateway to machine learning.

- **Signal + noise** — we assume the response $y$ is a systematic function of predictors plus random error: $y=f(\mathbf{x})+\varepsilon$.
- **Estimate** — fit the unknown function (here a line/plane) by minimizing a loss, usually squared error.
- **Infer & predict** — attach uncertainty to the fitted coefficients and to future predictions.

> **Principle — the regression model decomposes data into structure and noise**
>
> Every regression writes $ \text{observed} = \text{model} + \text{residual} $. The art is choosing a model rich enough to capture the structure but simple enough not to fit the noise. The **linear model** — response a linear combination of (functions of) predictors — is the foundation because it is interpretable, has closed-form solutions, and underpins almost everything more advanced.

**The general supervised-learning frame**

$$y_i = f(\mathbf{x}_i) + \varepsilon_i,\qquad E[\varepsilon_i]=0,\qquad i=1,\dots,n$$

*Linear models take $f(\mathbf{x})=\boldsymbol{\beta}^\top\mathbf{x}$. GLMs let a known function of $E[y]$ be linear. Nonparametric methods let $f$ be flexible. The same loss-and-fit logic runs through all of them.*

#### The whole guide on one line

> Best line → Least squares as calculus → Matrix form & projection → Inference & ANOVA → Logistic & GLMs → Regularization & beyond

> **Connection — picking up where the Statistics guide left off**
>
> The introductory Statistics companion ends at **correlation & the least-squares line** (its Section 13). This guide starts exactly there and derives, generalizes, and stress-tests it. Keep its big idea in mind — the **z-score** and the question "how far from expectation, in standard deviations?" — because every t-ratio and F-ratio here is that same idea.

<a id="s1"></a>
### Simple linear regression & least squares

*One predictor, one response, one straight line — fitted by minimizing the sum of squared vertical distances.*

**The simple linear regression model**

$$y_i = \beta_0 + \beta_1 x_i + \varepsilon_i,\qquad \varepsilon_i \stackrel{\text{iid}}{\sim}(0,\sigma^2)$$

*$\beta_0$ (intercept) and $\beta_1$ (slope) are unknown **parameters**; $\varepsilon_i$ is random noise with mean 0 and constant variance $\sigma^2$. The fitted line is $\hat y = \hat\beta_0 + \hat\beta_1 x$, and the $i$th **residual** is $e_i = y_i - \hat y_i$.*

> **Concept — why squared (not absolute) error?**
>
> We measure misfit by the **sum of squared residuals** $\sum e_i^2$. Squaring is smooth (differentiable everywhere, so calculus applies), penalizes large misses heavily, and — crucially — under Normal errors the least-squares fit is also the **maximum-likelihood** fit. Absolute error gives the median-like $L_1$ fit (robust, but no closed form).

**Demonstration — deriving the slope & intercept by minimizing the sum of squares**

1. The objective is a function of two unknowns:

   $$S(\beta_0,\beta_1)=\sum_{i=1}^{n}\big(y_i-\beta_0-\beta_1 x_i\big)^2.$$
2. This is an unconstrained optimization — set both partial derivatives to zero (the calculus first-order conditions):

   $$\frac{\partial S}{\partial \beta_0}=-2\sum\big(y_i-\beta_0-\beta_1 x_i\big)=0,\qquad \frac{\partial S}{\partial \beta_1}=-2\sum x_i\big(y_i-\beta_0-\beta_1 x_i\big)=0.$$
3. The first equation gives the normal equations piece $\sum y_i = n\beta_0 + \beta_1\sum x_i$; dividing by $n$,

   $$\hat\beta_0 = \bar y - \hat\beta_1 \bar x.$$
4. Substitute back into the second equation and simplify using $\sum(x_i-\bar x)=0$:

   $$\hat\beta_1=\frac{\sum (x_i-\bar x)(y_i-\bar y)}{\sum (x_i-\bar x)^2}=\frac{S_{xy}}{S_{xx}}.$$
5. The second derivative (Hessian) of $S$ is positive definite, so this stationary point is the unique global minimum.

*Because $\hat\beta_0=\bar y-\hat\beta_1\bar x$, the fitted line always passes through the centroid $(\bar x,\bar y)$.*

**The slope in correlation form**

$$\hat\beta_1 = r\,\frac{s_y}{s_x},\qquad r=\frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}$$

*where $s_x,s_y$ are the sample SDs and $r$ the correlation. The slope is the correlation rescaled by the ratio of spreads — regression and correlation are two faces of one quantity.*

**Demonstration — $\hat\beta_1 = r\,s_y/s_x$**

1. Start from $\hat\beta_1=S_{xy}/S_{xx}$ and recall $r=S_{xy}/\sqrt{S_{xx}S_{yy}}$, so $S_{xy}=r\sqrt{S_{xx}S_{yy}}$.
2. Substitute:

   $$\hat\beta_1=\frac{r\sqrt{S_{xx}S_{yy}}}{S_{xx}}=r\,\sqrt{\frac{S_{yy}}{S_{xx}}}.$$
3. Since $s_y=\sqrt{S_{yy}/(n-1)}$ and $s_x=\sqrt{S_{xx}/(n-1)}$, the $(n-1)$ cancels:

   $$\hat\beta_1=r\,\frac{s_y}{s_x}.$$

*If $x$ and $y$ are standardized ($s_x=s_y=1$), the slope *is* the correlation — and "regression to the mean" appears, since $|r|\le 1$.*

> **Connection — this is the calculus optimization you already know**
>
> Minimizing $S(\beta_0,\beta_1)$ by setting partial derivatives to zero is precisely the multivariable optimization of a calculus course, applied to data. The positive-definite Hessian is the second-derivative test guaranteeing a minimum. Regression is calculus optimization with a statistical interpretation bolted on.

<a id="s2"></a>
### The Gauss–Markov theorem & properties of the estimators

*Why least squares is special: among all linear unbiased estimators, it has the smallest variance.*

**Unbiasedness of the slope**

$$E[\hat\beta_1]=\beta_1,\qquad E[\hat\beta_0]=\beta_0$$

$$\operatorname{Var}(\hat\beta_1)=\frac{\sigma^2}{S_{xx}},\qquad \operatorname{Var}(\hat\beta_0)=\sigma^2\!\left(\frac1n+\frac{\bar x^2}{S_{xx}}\right)$$

*More spread in $x$ (larger $S_{xx}$) means a more tightly pinned slope. This is why good experimental design spreads predictor values out.*

**Demonstration — $\hat\beta_1$ is unbiased and find its variance**

1. Write the slope as a linear combination of the responses: $\hat\beta_1=\sum c_i y_i$ with weights $c_i=(x_i-\bar x)/S_{xx}$. Note $\sum c_i=0$ and $\sum c_i x_i=1$.
2. Take the expectation, using $E[y_i]=\beta_0+\beta_1 x_i$:

   $$E[\hat\beta_1]=\sum c_i(\beta_0+\beta_1 x_i)=\beta_0\underbrace{\textstyle\sum c_i}_{0}+\beta_1\underbrace{\textstyle\sum c_i x_i}_{1}=\beta_1.$$
3. For the variance, the $y_i$ are independent with variance $\sigma^2$:

   $$\operatorname{Var}(\hat\beta_1)=\sum c_i^2\,\sigma^2=\frac{\sigma^2}{S_{xx}^2}\sum(x_i-\bar x)^2=\frac{\sigma^2}{S_{xx}}.$$

*No Normality assumption was needed — only $E[\varepsilon]=0$, constant variance, and independence.*

> **Principle — Gauss–Markov: OLS is BLUE**
>
> Under the assumptions of linearity, zero-mean errors, **homoscedasticity** (constant variance), and uncorrelated errors, the ordinary least squares estimator is the **Best Linear Unbiased Estimator**: among all estimators that are both linear in $\mathbf{y}$ and unbiased, OLS has the minimum variance. "Best" here means smallest variance, not smallest possible error.

**Demonstration — sketch of why OLS is BLUE**

1. Consider any other linear unbiased estimator $\tilde\beta_1=\sum d_i y_i$. Unbiasedness forces $\sum d_i=0$ and $\sum d_i x_i=1$, the same constraints the OLS weights $c_i$ satisfy.
2. Write $d_i = c_i + \delta_i$. The constraints imply $\sum \delta_i = 0$ and $\sum \delta_i x_i = 0$, from which $\sum c_i \delta_i = 0$ (the cross term vanishes).
3. Then the variance splits cleanly:

   $$\operatorname{Var}(\tilde\beta_1)=\sigma^2\sum d_i^2=\sigma^2\Big(\sum c_i^2 + \sum \delta_i^2\Big)=\operatorname{Var}(\hat\beta_1)+\sigma^2\sum\delta_i^2.$$
4. Since $\sum\delta_i^2\ge 0$, any deviation from the OLS weights can only increase the variance.

*OLS sits at the bottom of the variance bowl among linear unbiased competitors — the Gauss–Markov optimum.*

**Estimating the error variance**

$$\hat\sigma^2 = s^2 = \frac{1}{n-2}\sum_{i=1}^n e_i^2 = \frac{\text{SSE}}{n-2}$$

*Divide by $n-2$, not $n$: two parameters ($\beta_0,\beta_1$) were estimated, costing two **degrees of freedom**. This makes $s^2$ unbiased for $\sigma^2$ — the same logic as Bessel's $n-1$ in the intro guide, generalized.*

<a id="s3"></a>
### Inference for slope & intercept; confidence & prediction intervals

*From point estimates to honest uncertainty: testing whether a slope is real, and bracketing future outcomes.*

**The t-statistic for a coefficient**

$$t = \frac{\hat\beta_1 - \beta_1^{(0)}}{\operatorname{SE}(\hat\beta_1)},\qquad \operatorname{SE}(\hat\beta_1)=\frac{s}{\sqrt{S_{xx}}}$$

*Under Normal errors and $H_0:\beta_1=\beta_1^{(0)}$, this follows a $t$-distribution with $n-2$ degrees of freedom. Testing $\beta_1^{(0)}=0$ asks "is there any linear relationship at all?"*

> **Concept — why $t$, and why $n-2$ df**
>
> If we knew $\sigma$, the standardized slope would be exactly Normal. But we estimate it with $s$, injecting extra uncertainty — fatter tails — exactly as in the one-sample t-test. The degrees of freedom drop to $n-2$ because fitting two coefficients uses up two pieces of information.

**Confidence interval for the slope**

$$\hat\beta_1 \pm t^{*}_{n-2}\;\frac{s}{\sqrt{S_{xx}}}$$

*"estimate ± critical value × standard error" — the universal CI template, now for a regression coefficient.*

> **Principle — confidence interval vs prediction interval**
>
> Two very different questions at a new $x_0$. A **confidence interval for the mean response** brackets $E[y\mid x_0]$ — the average $y$ at $x_0$. A **prediction interval** brackets a single future observation $y_0$, so it must add the irreducible noise $\sigma^2$ of one new point. The prediction interval is always wider, and stays wide even as $n\to\infty$.

**Confidence vs prediction interval at $x_0$**

$$\hat y_0 \pm t^{*}_{n-2}\,s\sqrt{\frac1n+\frac{(x_0-\bar x)^2}{S_{xx}}}\quad\text{(mean response)}$$

$$\hat y_0 \pm t^{*}_{n-2}\,s\sqrt{1+\frac1n+\frac{(x_0-\bar x)^2}{S_{xx}}}\quad\text{(new observation)}$$

*The lone extra $1$ under the root is the variance of the new $\varepsilon_0$. Both intervals fan out as $x_0$ moves away from $\bar x$ — extrapolation is dangerous.*

**Demonstration — why both intervals widen away from $\bar x$**

1. The fitted mean at $x_0$ is $\hat y_0=\hat\beta_0+\hat\beta_1 x_0=\bar y+\hat\beta_1(x_0-\bar x)$.
2. Its variance combines the uncertainty in $\bar y$ and in the slope:

   $$\operatorname{Var}(\hat y_0)=\frac{\sigma^2}{n}+(x_0-\bar x)^2\operatorname{Var}(\hat\beta_1)=\sigma^2\!\left(\frac1n+\frac{(x_0-\bar x)^2}{S_{xx}}\right).$$
3. The $(x_0-\bar x)^2$ term grows quadratically as you leave the data center — the interval bows outward into a hyperbola.
4. For a new observation add the fresh noise $\operatorname{Var}(\varepsilon_0)=\sigma^2$, producing the extra $+1$.

*Predictions are most trustworthy near the heart of the observed $x$-range.*

> **Connection — to Inference (t/F distributions, MLE)**
>
> The $t$-ratio here is identical in spirit to the one-sample $t$-test of the Inference guide. Under Normal errors, the least-squares estimates coincide with the **maximum-likelihood** estimates, and the $t$ and (later) $F$ sampling distributions are exactly the ones that course derives from the Normal.

<a id="s4"></a>
### Assessing fit: R², residuals & diagnostics

*A fitted line is not automatically a good one. Two tools: a single goodness-of-fit number, and a careful look at what's left over.*

**The sums-of-squares decomposition**

$$\underbrace{\sum(y_i-\bar y)^2}_{\text{SST}} = \underbrace{\sum(\hat y_i-\bar y)^2}_{\text{SSR}} + \underbrace{\sum(y_i-\hat y_i)^2}_{\text{SSE}}$$

*Total variation = variation explained by the model (regression) + variation left unexplained (error/residual).*

**Demonstration — why SST = SSR + SSE (the cross term vanishes)**

1. Split each centered response: $y_i-\bar y = (\hat y_i-\bar y)+(y_i-\hat y_i)$, then square and sum:

   $$\text{SST}=\text{SSR}+\text{SSE}+2\sum(\hat y_i-\bar y)(y_i-\hat y_i).$$
2. The normal equations give $\sum e_i=0$ and $\sum x_i e_i = 0$; since $\hat y_i-\bar y=\hat\beta_1(x_i-\bar x)$ is a linear function of $x_i$, the cross term is a combination of $\sum e_i$ and $\sum x_i e_i$.
3. Both are zero, so the cross term vanishes:

   $$\sum(\hat y_i-\bar y)(y_i-\hat y_i)=0.$$

*Geometrically: the residual vector is orthogonal to the fitted-values direction — the Pythagorean theorem in $n$-space (foreshadowing the hat matrix in Section 6).*

**The coefficient of determination**

$$R^2 = \frac{\text{SSR}}{\text{SST}} = 1 - \frac{\text{SSE}}{\text{SST}}$$

*The fraction of variance in $y$ explained by the model. In simple regression $R^2=r^2$ exactly. $R^2=0.7$ means the line accounts for 70% of the variability.*

> **Concept — R² is necessary but not sufficient**
>
> A high $R^2$ does not certify a correct model: it can be inflated by adding junk predictors, and it says nothing about whether the linear form, constant variance, or independence assumptions hold. Anscombe's quartet — four datasets with identical $R^2$ but wildly different shapes — is the classic warning. Always look at the **residual plots**.

**Residual diagnostics — what to plot, what it reveals**

***Residuals vs fitted:** a curved band signals nonlinearity; a funnel signals heteroscedasticity. **Q–Q plot of residuals:** departures from the diagonal flag non-Normal errors. **Residuals vs order/time:** patterns flag autocorrelation. **Leverage & Cook's distance:** identify high-influence points that single-handedly steer the fit.*

> **Principle — the four assumptions, mnemonic "LINE"**
>
> **L**inearity of the mean, **I**ndependence of errors, **N**ormality of errors (needed for exact $t$/$F$ inference, not for unbiasedness), and **E**qual variance (homoscedasticity). Diagnostics are how you check each. Violations don't always invalidate the fit, but they change which inferences are trustworthy.

> **Connection — to the Statistics guide's correlation**
>
> The identity $R^2=r^2$ ties this section straight back to the introductory guide: the correlation you computed there *is* the square root of the variance explained here. Regression promotes correlation from "do they move together?" to "by how much, and how reliably?"

## Part B · Multiple linear regression

<a id="s5"></a>
### The multiple regression model in matrix form

*With many predictors, scalar algebra becomes unwieldy. Linear algebra makes the whole theory compact and exact.*

**The model, stacked into matrices**

$$\mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon},\qquad E[\boldsymbol{\varepsilon}]=\mathbf{0},\quad \operatorname{Cov}(\boldsymbol{\varepsilon})=\sigma^2\mathbf{I}$$

$$\mathbf{y}\in\mathbb{R}^{n},\quad \mathbf{X}\in\mathbb{R}^{n\times p},\quad \boldsymbol{\beta}\in\mathbb{R}^{p}$$

*Each row of $\mathbf{X}$ is one observation's predictors; the first column is usually all 1's to carry the intercept. $\boldsymbol{\beta}$ collects all coefficients. The single equation $\mathbf{y}=\mathbf{X}\boldsymbol{\beta}+\boldsymbol{\varepsilon}$ holds for every row at once.*

> **Concept — the design matrix $\mathbf{X}$**
>
> The matrix $\mathbf{X}$ is called the **design matrix** because, in an experiment, you literally design it. Its columns can be raw predictors, transformations ($x^2,\log x$), dummy variables for categories, or interactions — anything *linear in the coefficients*. "Linear model" means linear in $\boldsymbol{\beta}$, not in $x$: $y=\beta_0+\beta_1 x+\beta_2 x^2$ is a perfectly linear model.

**Interpreting a coefficient**

*$\beta_j$ is the expected change in $y$ for a one-unit increase in $x_j$, **holding all other predictors fixed**. This "all else equal" clause is what separates multiple regression from a pile of simple regressions — it adjusts each predictor for the others.*

> **Connection — to linear algebra**
>
> From here on, regression *is* linear algebra: fitting is solving a linear system, the fit is an orthogonal projection, variances live in $(\mathbf{X}^\top\mathbf{X})^{-1}$, and collinearity is near-singularity. The eigenvalues of $\mathbf{X}^\top\mathbf{X}$ govern stability. Everything reduces to vectors, matrices, and the geometry of subspaces.

<a id="s6"></a>
### Least squares via linear algebra: the normal equations & hat matrix

*The single most important computation in the subject — and its beautiful geometric meaning as projection.*

**The normal equations & the OLS estimator**

$$\mathbf{X}^\top\mathbf{X}\,\hat{\boldsymbol{\beta}} = \mathbf{X}^\top\mathbf{y}\quad\Longrightarrow\quad \hat{\boldsymbol{\beta}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$$

*Valid whenever $\mathbf{X}$ has full column rank (no exact collinearity), so $\mathbf{X}^\top\mathbf{X}$ is invertible.*

**Demonstration — deriving the normal equations by matrix calculus**

1. Write the loss as a squared norm:

   $$S(\boldsymbol{\beta})=\|\mathbf{y}-\mathbf{X}\boldsymbol{\beta}\|^2=(\mathbf{y}-\mathbf{X}\boldsymbol{\beta})^\top(\mathbf{y}-\mathbf{X}\boldsymbol{\beta}).$$
2. Expand:

   $$S=\mathbf{y}^\top\mathbf{y}-2\boldsymbol{\beta}^\top\mathbf{X}^\top\mathbf{y}+\boldsymbol{\beta}^\top\mathbf{X}^\top\mathbf{X}\boldsymbol{\beta}.$$
3. Take the gradient with respect to $\boldsymbol{\beta}$ and set it to zero:

   $$\nabla_{\boldsymbol\beta}S=-2\mathbf{X}^\top\mathbf{y}+2\mathbf{X}^\top\mathbf{X}\boldsymbol{\beta}=\mathbf{0}.$$
4. Rearrange into the normal equations and solve:

   $$\mathbf{X}^\top\mathbf{X}\,\hat{\boldsymbol\beta}=\mathbf{X}^\top\mathbf{y}\;\Rightarrow\;\hat{\boldsymbol\beta}=(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}.$$
5. The Hessian $2\mathbf{X}^\top\mathbf{X}$ is positive semidefinite (positive definite at full rank), so this is the global minimum.

*The same "set the derivative to zero" move as Section 1 — now in vector form, solving every coefficient simultaneously.*

**The hat matrix**

$$\hat{\mathbf{y}}=\mathbf{X}\hat{\boldsymbol\beta}=\underbrace{\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top}_{\mathbf{H}}\,\mathbf{y}=\mathbf{H}\mathbf{y}$$

*$\mathbf{H}$ "puts the hat on $\mathbf{y}$." Its diagonal entries $h_{ii}$ are the **leverages** — how much each observation pulls its own fitted value. Residuals are $\mathbf{e}=(\mathbf{I}-\mathbf{H})\mathbf{y}$.*

**Demonstration — $\mathbf{H}$ is a projection (symmetric & idempotent)**

1. Symmetric: since $(\mathbf{X}^\top\mathbf{X})^{-1}$ is symmetric,

   $$\mathbf{H}^\top=\big(\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\big)^\top=\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top=\mathbf{H}.$$
2. Idempotent: the inner $\mathbf{X}^\top\mathbf{X}$ cancels its inverse,

   $$\mathbf{H}^2=\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\underbrace{\mathbf{X}^\top\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}}_{=\,\mathbf{I}}\mathbf{X}^\top=\mathbf{H}.$$
3. A symmetric idempotent matrix is exactly an orthogonal projection — here onto the column space of $\mathbf{X}$. So $\hat{\mathbf{y}}$ is the point in that subspace closest to $\mathbf{y}$.
4. The residual $\mathbf{e}=(\mathbf{I}-\mathbf{H})\mathbf{y}$ is orthogonal to the column space: $\mathbf{X}^\top\mathbf{e}=\mathbf{0}$ — exactly the normal equations restated.

*Least squares = dropping a perpendicular from $\mathbf{y}$ onto the space spanned by the predictors. SST=SSR+SSE is the Pythagorean theorem for this right triangle.*

**Covariance of the estimator**

$$\operatorname{Cov}(\hat{\boldsymbol\beta})=\sigma^2(\mathbf{X}^\top\mathbf{X})^{-1}$$

*Standard errors are the square roots of its diagonal. The geometry: directions in which $\mathbf{X}$ carries little variation (small eigenvalues of $\mathbf{X}^\top\mathbf{X}$) give large coefficient variance — the seed of multicollinearity.*

> **Connection — projection & eigenvalues from linear algebra**
>
> $\mathbf{H}$ is the projection matrix; $\operatorname{trace}(\mathbf{H})=p$ equals the model degrees of freedom (it counts the dimension of the column space). The eigenvalues of $\mathbf{X}^\top\mathbf{X}$ decide both the stability of the inverse and the variance of $\hat{\boldsymbol\beta}$ — the very eigenvalue/conditioning ideas from linear algebra.

<a id="s7"></a>
### Inference, multicollinearity & model selection

*Testing individual coefficients, diagnosing when predictors fight each other, and choosing which to keep.*

**t-test for a single coefficient**

$$t_j = \frac{\hat\beta_j}{\operatorname{SE}(\hat\beta_j)},\qquad \operatorname{SE}(\hat\beta_j)=s\sqrt{[(\mathbf{X}^\top\mathbf{X})^{-1}]_{jj}}$$

*Distributed as $t_{n-p}$ under $H_0:\beta_j=0$. It tests $x_j$'s contribution *given all other predictors are in the model* — a partial, not marginal, effect.*

> **Concept — multicollinearity**
>
> When predictors are highly correlated, $\mathbf{X}^\top\mathbf{X}$ is nearly singular (tiny eigenvalues), so $(\mathbf{X}^\top\mathbf{X})^{-1}$ has huge entries and coefficient standard errors explode. Symptoms: a significant overall $F$ but no significant individual $t$'s; coefficients with the "wrong" sign that swing wildly when a predictor is added or dropped. It harms *interpretation and stability*, not necessarily prediction.

**The variance inflation factor**

$$\operatorname{VIF}_j=\frac{1}{1-R_j^2}$$

*where $R_j^2$ is from regressing $x_j$ on all other predictors. $\operatorname{VIF}_j>5$–$10$ flags problematic collinearity: the variance of $\hat\beta_j$ is inflated by that factor versus an orthogonal design.*

| Criterion | Formula / idea | What it rewards |
| --- | --- | --- |
| Adjusted $R^2$ | $1-\dfrac{\text{SSE}/(n-p)}{\text{SST}/(n-1)}$ | fit, penalizing extra parameters |
| AIC | $2p-2\ln\hat L$ | predictive fit, light penalty |
| BIC | $p\ln n-2\ln\hat L$ | parsimony, heavier penalty (grows with $n$) |
| Mallows' $C_p$ | $\dfrac{\text{SSE}_p}{\hat\sigma^2}-n+2p$ | low bias with few predictors |
| Cross-validation | held-out prediction error | honest out-of-sample accuracy |

> **Principle — selection is a bias–variance compromise**
>
> Adding predictors always lowers training SSE but eventually raises *test* error by fitting noise. Every criterion above trades fit against complexity; they differ in how steep the penalty is. Stepwise selection is convenient but optimistic (it invalidates the usual p-values); cross-validation and regularization (Section 12) are the modern defaults.

> **Connection — to MLE and information criteria**
>
> AIC and BIC are built from the maximized **log-likelihood** $\ln\hat L$ — the same MLE machinery from the Inference guide. Under Normal errors, maximizing the likelihood is minimizing SSE, so least squares and maximum likelihood agree, and the criteria simply add a complexity tax to the log-likelihood.

<a id="s8"></a>
### ANOVA & the F-test

*One test for the whole model: is the set of predictors, taken together, better than nothing?*

**The overall F-test**

$$F=\frac{\text{SSR}/(p-1)}{\text{SSE}/(n-p)}=\frac{\text{MSR}}{\text{MSE}}$$

*Under $H_0:\beta_1=\cdots=\beta_{p-1}=0$ (all slopes zero), $F\sim F_{p-1,\,n-p}$. A large $F$ says the model explains far more variance per parameter than the leftover noise — at least one predictor matters.*

| Source | Sum of squares | df | Mean square | F |
| --- | --- | --- | --- | --- |
| Regression | $\text{SSR}=\sum(\hat y_i-\bar y)^2$ | $p-1$ | $\text{MSR}=\text{SSR}/(p-1)$ | $\text{MSR}/\text{MSE}$ |
| Error | $\text{SSE}=\sum(y_i-\hat y_i)^2$ | $n-p$ | $\text{MSE}=\text{SSE}/(n-p)$ |   |
| Total | $\text{SST}=\sum(y_i-\bar y)^2$ | $n-1$ |   |   |

**Demonstration — building the F-ratio**

1. Partition the variation: $\text{SST}=\text{SSR}+\text{SSE}$, and partition the degrees of freedom to match: $(n-1)=(p-1)+(n-p)$.
2. Under $H_0$, each sum of squares divided by $\sigma^2$ is an independent chi-square: $\text{SSR}/\sigma^2\sim\chi^2_{p-1}$ and $\text{SSE}/\sigma^2\sim\chi^2_{n-p}$ (their independence follows from the orthogonality of $\mathbf{H}$ and $\mathbf{I}-\mathbf{H}$).
3. An $F$ random variable is the ratio of two independent chi-squares each over its df:

   $$F=\frac{(\text{SSR}/\sigma^2)/(p-1)}{(\text{SSE}/\sigma^2)/(n-p)}=\frac{\text{MSR}}{\text{MSE}}\sim F_{p-1,\,n-p}.$$
4. The $\sigma^2$ cancels — so we never need to know it. Under $H_0$, $E[\text{MSR}]=E[\text{MSE}]=\sigma^2$, so $F\approx 1$; a real signal pushes $\text{MSR}$ above $\text{MSE}$.

*In simple regression the overall $F$ equals $t^2$ for the single slope — the two tests coincide.*

> **Concept — the partial (nested) F-test**
>
> To test a *subset* of coefficients, compare a full model to a reduced one: $F=\dfrac{(\text{SSE}_{\text{red}}-\text{SSE}_{\text{full}})/q}{\text{SSE}_{\text{full}}/(n-p)}$, where $q$ coefficients were dropped. This "extra sum of squares" $F$ is the engine behind comparing nested models and is how categorical variables with several levels are tested as a block.

> **Connection — same ANOVA, same F as the Statistics guide**
>
> The one-way ANOVA of the intro guide ("between-group variance over within-group variance") is a special case of this regression ANOVA, with group-membership dummies as predictors. Same $F$-distribution, same chi-square ratio logic from the Probability and Inference guides.

<a id="s9"></a>
### Categorical predictors, interactions & transformations

*How to feed categories, curvature, and conditional effects into a model that is still "linear."*

**Dummy (indicator) coding**

$$x_{\text{group B}}=\begin{cases}1 & \text{if obs is in group B}\\ 0 & \text{otherwise}\end{cases}$$

*A $k$-level category needs $k-1$ dummies; the omitted level is the **baseline**. Including all $k$ plus an intercept makes $\mathbf{X}$ rank-deficient — the "dummy variable trap" (perfect collinearity with the intercept column).*

> **Concept — what a dummy coefficient means**
>
> In $y=\beta_0+\beta_1 D$, the coefficient $\beta_1$ is the difference in mean $y$ between that group and the baseline. With a numeric predictor too, a dummy shifts the **intercept** (parallel lines, different heights). To let the *slope* differ by group, you need an interaction.

**Interaction terms**

$$y=\beta_0+\beta_1 x+\beta_2 D+\beta_3\,(x\cdot D)+\varepsilon$$

*For $D=0$ the slope in $x$ is $\beta_1$; for $D=1$ it is $\beta_1+\beta_3$. The interaction $\beta_3$ measures how the effect of $x$ **depends on** $D$ — non-parallel lines. Interactions between two numeric predictors work the same way: $\beta_3\,x_1 x_2$.*

## Part C · Generalized models & beyond

<a id="s10"></a>
### Logistic regression

*When the response is a yes/no outcome, a straight line breaks down. The logit link fixes it.*

> **Concept — why not just fit a line to 0/1 data?**
>
> Linear regression on a binary $y$ can predict probabilities below 0 or above 1, and its errors are neither Normal nor homoscedastic. Instead we model the **probability** $p=P(y=1\mid\mathbf{x})$ and pass it through a function that maps the whole real line into $(0,1)$ — the logistic (sigmoid) curve.

**The logistic model & the logit link**

$$p(\mathbf{x})=\frac{1}{1+e^{-\boldsymbol{\beta}^\top\mathbf{x}}},\qquad \operatorname{logit}(p)=\ln\frac{p}{1-p}=\boldsymbol{\beta}^\top\mathbf{x}$$

*The **log-odds** are linear in the predictors. So $e^{\beta_j}$ is an **odds ratio**: the multiplicative change in the odds of $y=1$ per unit increase in $x_j$.*

**Demonstration — the log-likelihood and its score equations**

1. Each $y_i$ is Bernoulli with success probability $p_i=p(\mathbf{x}_i)$, so the likelihood is

   $$L(\boldsymbol\beta)=\prod_{i=1}^n p_i^{\,y_i}(1-p_i)^{1-y_i}.$$
2. Take logs to get the log-likelihood:

   $$\ell(\boldsymbol\beta)=\sum_{i=1}^n\Big[y_i\ln p_i+(1-y_i)\ln(1-p_i)\Big].$$
3. Substituting $\operatorname{logit}(p_i)=\boldsymbol\beta^\top\mathbf{x}_i$ and differentiating gives the elegant score equations:

   $$\frac{\partial\ell}{\partial\boldsymbol\beta}=\sum_{i=1}^n\big(y_i-p_i\big)\mathbf{x}_i=\mathbf{X}^\top(\mathbf{y}-\mathbf{p})=\mathbf{0}.$$
4. These are nonlinear in $\boldsymbol\beta$ (since $p_i$ depends on $\boldsymbol\beta$) — no closed form. Solve iteratively by Newton–Raphson, a.k.a. iteratively reweighted least squares (IRLS).

*Note the residual $(y_i-p_i)$ is orthogonal to the predictors — the same orthogonality as OLS, now for the likelihood.*

> **Principle — interpretation by odds ratios & deviance**
>
> Coefficients live on the log-odds scale, so report $e^{\beta_j}$ as an odds ratio. Goodness of fit uses **deviance** $-2\ell$ (the GLM analogue of SSE); nested models are compared by the **likelihood-ratio test** $\Delta\text{deviance}\sim\chi^2$. Classification quality is judged by the ROC curve / AUC, not $R^2$.

> **Connection — to MLE and the Bernoulli**
>
> Logistic regression is maximum likelihood for the Bernoulli distribution of the Probability guide, with its parameter steered by a linear predictor. The likelihood-ratio test reuses the asymptotic $\chi^2$ theory of the Inference guide. Linear regression was MLE for the Normal; this is MLE for the Bernoulli — the same principle, a different distribution.

<a id="s11"></a>
### Generalized linear models (GLMs)

*Linear and logistic regression are two members of one family. The GLM names the pattern.*

> **Concept — the three ingredients of a GLM**
>
> Every GLM has (1) a **random component** — a response distribution from the exponential family (Normal, Bernoulli, Poisson, Gamma…); (2) a **systematic component** — a linear predictor $\eta=\boldsymbol\beta^\top\mathbf{x}$; and (3) a **link function** $g$ connecting them via $g(E[y])=\eta$. Choosing the distribution and link picks the model.

**The GLM template**

$$g\big(E[y\mid\mathbf{x}]\big)=\boldsymbol\beta^\top\mathbf{x},\qquad y\mid\mathbf{x}\sim \text{exponential family}$$

*Linear regression is a GLM with Normal response and identity link; logistic is Bernoulli with logit link; Poisson regression is counts with log link.*

| Model | Response distribution | Link $g(\mu)$ | Inverse (mean) |
| --- | --- | --- | --- |
| Linear regression | Normal | identity: $\mu$ | $\eta$ |
| Logistic regression | Bernoulli / Binomial | logit: $\ln\frac{\mu}{1-\mu}$ | $\frac{1}{1+e^{-\eta}}$ |
| Probit regression | Bernoulli | probit: $\Phi^{-1}(\mu)$ | $\Phi(\eta)$ |
| Poisson regression | Poisson | log: $\ln\mu$ | $e^{\eta}$ |
| Gamma regression | Gamma | inverse: $1/\mu$ | $1/\eta$ |

> **Principle — the canonical link & unified fitting**
>
> Each exponential-family distribution has a natural **canonical link** (logit for Bernoulli, log for Poisson, identity for Normal) that makes the math cleanest and the score equations take the form $\mathbf{X}^\top(\mathbf{y}-\boldsymbol\mu)=\mathbf{0}$. All GLMs are fit by the same algorithm — **IRLS** — and compared by deviance and likelihood-ratio tests. One framework, many response types.

> **Connection — the exponential family ties Probability together**
>
> The Normal, Bernoulli, Poisson, and Gamma of the Probability guide are all exponential-family members; the GLM is the single regression framework that handles each. The link function generalizes the logit of Section 10, and the identity link recovers ordinary least squares of Part A/B.

<a id="s12"></a>
### Regularization: ridge, lasso & the bias–variance tradeoff

*When predictors are many or collinear, plain OLS overfits. Shrinking the coefficients trades a little bias for a lot less variance.*

**Ridge regression (L2 penalty)**

$$\hat{\boldsymbol\beta}_{\text{ridge}}=\arg\min_{\boldsymbol\beta}\;\|\mathbf{y}-\mathbf{X}\boldsymbol\beta\|^2+\lambda\|\boldsymbol\beta\|_2^2$$

$$\hat{\boldsymbol\beta}_{\text{ridge}}=(\mathbf{X}^\top\mathbf{X}+\lambda\mathbf{I})^{-1}\mathbf{X}^\top\mathbf{y}$$

*The penalty $\lambda\ge 0$ shrinks coefficients toward zero. It has a closed form — and one with a beautiful side effect.*

**Demonstration — the ridge closed form, and why it always inverts**

1. The objective is $S(\boldsymbol\beta)=(\mathbf{y}-\mathbf{X}\boldsymbol\beta)^\top(\mathbf{y}-\mathbf{X}\boldsymbol\beta)+\lambda\boldsymbol\beta^\top\boldsymbol\beta$.
2. Set the gradient to zero:

   $$\nabla S=-2\mathbf{X}^\top\mathbf{y}+2\mathbf{X}^\top\mathbf{X}\boldsymbol\beta+2\lambda\boldsymbol\beta=\mathbf{0}.$$
3. Collect terms and solve:

   $$(\mathbf{X}^\top\mathbf{X}+\lambda\mathbf{I})\,\hat{\boldsymbol\beta}=\mathbf{X}^\top\mathbf{y}\;\Rightarrow\;\hat{\boldsymbol\beta}_{\text{ridge}}=(\mathbf{X}^\top\mathbf{X}+\lambda\mathbf{I})^{-1}\mathbf{X}^\top\mathbf{y}.$$
4. Adding $\lambda\mathbf{I}$ lifts every eigenvalue of $\mathbf{X}^\top\mathbf{X}$ by $\lambda>0$, so the matrix is always invertible — ridge works even when $p>n$ or predictors are collinear, where OLS fails outright.

*Ridge is OLS with a numerically stabilized, better-conditioned normal-equations matrix — collinearity's cure.*

**Lasso (L1 penalty)**

$$\hat{\boldsymbol\beta}_{\text{lasso}}=\arg\min_{\boldsymbol\beta}\;\|\mathbf{y}-\mathbf{X}\boldsymbol\beta\|^2+\lambda\|\boldsymbol\beta\|_1$$

*The L1 norm $\sum|\beta_j|$ has corners on the axes, so the solution often lands exactly at $\beta_j=0$ — lasso does **automatic variable selection**. No closed form; solved by coordinate descent or LARS. The **elastic net** blends both penalties.*

> **Principle — the bias–variance tradeoff**
>
> Expected prediction error decomposes as $\text{error}=\text{bias}^2+\text{variance}+\sigma^2_{\text{irreducible}}$. OLS is unbiased but can have huge variance with many/collinear predictors. Regularization deliberately *adds bias* (shrinks coefficients) to *cut variance* more, lowering total error. The penalty $\lambda$, tuned by cross-validation, dials the position along this curve.

> **Connection — eigenvalues, Gauss–Markov & Bayes**
>
> Gauss–Markov said OLS is best *among unbiased* estimators; ridge escapes that by allowing bias and so can beat OLS in mean-squared error. The $\lambda\mathbf{I}$ term directly raises the small eigenvalues of $\mathbf{X}^\top\mathbf{X}$ — the conditioning fix from linear algebra. And ridge is exactly the **Bayesian** posterior mode under a Normal prior on $\boldsymbol\beta$ (lasso under a Laplace prior) — the Bayes/Bayes-theorem thread of the earlier guides.

<a id="s13"></a>
### A glimpse beyond: mixed models, time series & nonparametric regression

*Where the assumptions of ordinary regression break, three large extensions take over.*

**Mixed-effects models — when independence fails**

$$\mathbf{y}=\mathbf{X}\boldsymbol\beta+\mathbf{Z}\mathbf{b}+\boldsymbol\varepsilon,\qquad \mathbf{b}\sim N(\mathbf{0},\mathbf{G})$$

*Grouped/clustered data (students within schools, repeated measures on a patient) violate independence. **Random effects** $\mathbf{b}$ model group-level deviations; $\boldsymbol\beta$ are the population **fixed effects**. Fitted by REML/ML.*

**Time series — when errors are autocorrelated**

*When observations are ordered in time, errors are correlated, breaking Gauss–Markov. Models such as **AR($p$)**, **MA($q$)**, and **ARIMA** regress a series on its own past; generalized least squares and the Durbin–Watson statistic address autocorrelated residuals. Forecasting replaces "hold others fixed" with "extrapolate the dynamics."*

**Nonparametric regression — when the form is unknown**

$$y_i=f(x_i)+\varepsilon_i,\qquad f\ \text{flexible, not a fixed formula}$$

***Splines**, **LOESS**, **kernel smoothers**, and **generalized additive models (GAMs)** let the data dictate the curve. **Regression trees**, **random forests**, and **gradient boosting** push further into machine learning. A smoothing parameter plays $\lambda$'s role on the same bias–variance tradeoff.*

> **Principle — one loss-and-fit idea, ever generalizing**
>
> Every model in this guide is the same three-step story: **posit** a structure (line, plane, link, flexible curve), **fit** it by optimizing a loss or likelihood (set the gradient to zero — calculus), and **assess** it with honest, out-of-sample uncertainty. The mathematics scales from a single straight line to deep learning without changing its skeleton.

> **Connection — the whole arc**
>
> Correlation (Statistics) → least squares as calculus optimization → projection & eigenvalues (linear algebra) → t/F sampling distributions and MLE (Inference) → GLMs over the exponential family (Probability) → regularization as a Bayesian prior. Regression is where every earlier subject converges into one practical tool.

---

*A complete companion to regression and linear models — from the best straight line through a scatterplot to GLMs, regularization, and the frontier of mixed models and machine learning. Every core result is demonstrated, and threaded back to calculus (optimization), linear algebra (projection, eigenvalues), and the probability and inference that make the uncertainty honest. Read once for the shape; return to any box as a reference. Remember the skeleton: posit a structure, fit by minimizing a loss, assess with honest uncertainty.*
