[English](inference.md) · **中文**

# 推断，*从数据到真相。*

一门严谨的数理统计课程——如何把随机样本转化为对未知参数的估计、区间、检验以及后验信念。每条原理都以精确的定义给出，每个关键定理都给出**演示**，并把与概率论和微积分的脉络明确地呈现出来。

[← 返回全部指南](../README.zh.md)

## A 部分 · 基础

<a id="s0"></a>
### 全局图景：从数据到结论

*概率论描述一个已知机制如何产生随机数据。推断则把箭头反转：给定数据，机制是什么？*

在**数理统计**中我们设定一个*统计模型*：一族概率分布 $\{f(x\mid\theta):\theta\in\Theta\}$，由一个未知参数 $\theta$ 编号。我们观测到从该族某一成员中抽出的数据 $X_1,\dots,X_n$，而我们的任务是说出 $\theta$ 是什么。有三类经典的产出。

- **点估计** —— 对 $\theta$ 给出单一的最佳猜测 $\hat\theta$（B 部分）。
- **区间估计与检验** —— 给出 $\theta$ 的一个带有声明置信度的范围，或对某个假设作出是/否的判定（C 部分）。
- **预测 / 信念更新** —— 以及，在贝叶斯视角下，$\theta$ 的一个完整后验分布（D 部分）。

> **原理 —— 推断的反转**
>
> 概率论沿着**参数 $\to$ 数据**的方向运行：固定 $\theta$，则 $f(x\mid\theta)$ 告诉你数据如何表现。推断沿着**数据 $\to$ 参数**的方向运行：固定数据，问哪个 $\theta$ 是可信的。*似然函数*（第 3 节）正是按此反方向阅读的 $f(x\mid\theta)$，它是整个学科的枢纽。

#### 整门课程浓缩为一行

> 模型与似然 → 充分性 → 点估计量（矩法、极大似然）→ 评价它们（偏差、均方误差、Cramér–Rao、最小方差无偏估计）→ 区间与检验（枢轴量、Neyman–Pearson、似然比检验）→ 贝叶斯与自助法

> **联系 —— 在入门《统计学》指南之上构建**
>
> 入门指南从操作层面引入了 $\bar x$、$s^2$、置信区间和 p 值。本指南提供*为什么*：为什么除以 $n-1$，为什么 $t$ 会出现，为什么 $\bar X\pm 1.96\,\sigma/\sqrt n$ 是正确的，以及什么使一个估计量"好"。这是配方背后的理论。

<a id="s1"></a>
### 总体、样本与抽样分布

*统计量是随机数据的函数，因此它本身就是一个随机变量。它的分布是每一个推断赖以建立的对象。*

**随机样本（独立同分布）**

$$X_1,\dots,X_n \ \text{i.i.d.}\ \sim f(x\mid\theta),\qquad \text{joint density } f(\mathbf x\mid\theta)=\prod_{i=1}^n f(x_i\mid\theta)$$

*"i.i.d." = 独立且同分布。独立性把联合密度分解为一个乘积——这一结构性事实驱动了似然、充分性和中心极限定理。*

> **概念 —— 统计量 vs 估计量 vs 估计值**
>
> **统计量** $T=T(X_1,\dots,X_n)$ 是样本的任意一个不依赖于 $\theta$ 的函数。**估计量**是用来猜测参数的统计量，例如 $\hat\theta=\bar X$；它是随机的。它在观测数据上的实现值，如 $\hat\theta=4.2$，是一个**估计值**。一个估计量在所有可能样本上的分布是它的**抽样分布**。

**样本均值的均值与方差**

$$E[\bar X]=\mu,\qquad \operatorname{Var}(\bar X)=\frac{\sigma^2}{n},\qquad \text{SE}(\bar X)=\frac{\sigma}{\sqrt n}$$

*估计量 $\bar X$ 以真值为中心，并随 $n$ 增大而越来越紧——这是相合性的萌芽（第 6 节）。*

**演示 —— 正态样本下 $\bar X$ 的抽样分布**

1. 设 $X_i\ \text{i.i.d.}\ \sim N(\mu,\sigma^2)$。独立正态变量的线性组合仍为正态，故 $\bar X$ 是正态的。
2. 它的均值和方差已在上面算出：$E[\bar X]=\mu$，$\operatorname{Var}(\bar X)=\sigma^2/n$。因此

   $$\bar X\sim N\!\left(\mu,\ \frac{\sigma^2}{n}\right),\qquad Z=\frac{\bar X-\mu}{\sigma/\sqrt n}\sim N(0,1).$$
3. 对于非正态总体，中心极限定理给出相同的极限形式：当 $n\to\infty$ 时 $Z\xrightarrow{d}N(0,1)$。

*对正态精确，对一般情形渐近成立——这一个分布支撑了 C 部分的 $z$ 区间和 $t$ 区间。*

> **联系 —— 《概率论》指南（中心极限定理与矩母函数）**
>
> $\bar X$ 在正态数据下是正态的，而在其他情形下渐近正态，这就是那里通过矩母函数证明的中心极限定理。抽样分布不过是随机变量的变换；概率论中 $E$、$\operatorname{Var}$ 和矩母函数的代数正是工具箱。

<a id="s2"></a>
### 统计量、充分性与因子分解定理

*某些统计量把数据中关于 $\theta$ 的每一滴信息都榨取出来。这些充分统计量让我们在不丢失任何信息的情况下压缩样本。*

> **概念 —— 充分性**
>
> 如果给定 $T$ 时数据的条件分布不依赖于 $\theta$，则统计量 $T$ 对 $\theta$ 是**充分的**。直观地说：一旦你知道了 $T$，样本的其余部分就是不再携带关于 $\theta$ 的任何信息的"噪声"。对正态样本，$(\sum X_i,\sum X_i^2)$ 是充分的——数据的个别次序无关紧要。

**Fisher–Neyman 因子分解定理**

$$T \text{ is sufficient for }\theta \iff f(\mathbf x\mid\theta)=g\big(T(\mathbf x),\theta\big)\,h(\mathbf x)$$

*联合密度分解为只通过 $T$ 触及 $\theta$ 的一部分 $g$，乘以与 $\theta$ 无关的一部分 $h$。通过分离 $\theta$ 与数据相遇之处即可读出 $T$。*

**演示 —— 通过因子分解得到伯努利 $p$ 的充分统计量**

1. 对 $X_i\ \text{i.i.d.}\ \sim\text{Bernoulli}(p)$，联合分布律为

   $$f(\mathbf x\mid p)=\prod_{i=1}^n p^{x_i}(1-p)^{1-x_i}=p^{\sum x_i}(1-p)^{\,n-\sum x_i}.$$
2. 它仅通过 $T=\sum_{i=1}^n x_i$ 依赖于数据。写成 $g(T,p)=p^{T}(1-p)^{n-T}$ 与 $h(\mathbf x)=1$。
3. 由因子分解定理，$T=\sum X_i$（等价地 $\bar X$）对 $p$ 是充分的。

*知道成功的总次数和知道由 $0$ 与 $1$ 组成的完整序列一样好。*

> **原理 —— 最小充分性与完备性**
>
> **最小**充分统计量是最粗的充分概括——是其他每个充分统计量的函数。一个统计量是**完备的**，如果它的任何非零函数对所有 $\theta$ 都不具有期望 $0$；完备性是使 Rao–Blackwell 估计量（第 8 节）成为*唯一*最优者的技术要件。

> **联系 —— 指数族**
>
> 许多分布（正态、伯努利、泊松、指数、伽马）属于**指数族** $f(x\mid\theta)=h(x)\exp\{\eta(\theta)T(x)-A(\theta)\}$。此时因子分解立即成立，且 $\sum T(X_i)$ 自动是一个完备充分统计量——这是贯穿估计理论的一条统一线索。

<a id="s3"></a>
### 似然函数

*把联合密度反转过来：把数据当作固定，把 $\theta$ 当作变量。这种重新解读就是似然，几乎一切都由它推出。*

**似然与对数似然**

$$L(\theta)=f(\mathbf x\mid\theta)=\prod_{i=1}^n f(x_i\mid\theta),\qquad \ell(\theta)=\log L(\theta)=\sum_{i=1}^n \log f(x_i\mid\theta)$$

*$L(\theta)$ *不是*关于 $\theta$ 的概率分布；它无需积分为一。它按各 $\theta$ 值解释观测数据的优劣对它们排序。*

> **原理 —— 似然原理**
>
> 数据携带的关于 $\theta$ 的全部信息都包含在似然函数中。两个产生成比例似然的实验应导致关于 $\theta$ 的相同推断。取对数把乘积变为和，这正是**得分函数** $\ell'(\theta)$ 和 Fisher 信息（第 7 节）对独立观测可加的原因。

**得分函数**

$$U(\theta)=\frac{\partial}{\partial\theta}\ell(\theta)=\sum_{i=1}^n \frac{\partial}{\partial\theta}\log f(x_i\mid\theta),\qquad E_\theta[U(\theta)]=0$$

*得分在真值 $\theta$ 处均值为零。把它置零就定位了似然的极大值——纯粹的微积分优化。*

**演示 —— 得分的期望为零**

1. 由于对每个 $\theta$ 都有 $\int f(x\mid\theta)\,dx=1$，对两边关于 $\theta$ 求导（正则性允许我们把导数移入积分内）：

   $$\int \frac{\partial}{\partial\theta} f(x\mid\theta)\,dx=0.$$
2. 利用恒等式 $\frac{\partial}{\partial\theta} f = f\cdot\frac{\partial}{\partial\theta}\log f$：

   $$\int \Big(\frac{\partial}{\partial\theta}\log f(x\mid\theta)\Big) f(x\mid\theta)\,dx=0.$$
3. 左边恰为 $E_\theta\!\big[\frac{\partial}{\partial\theta}\log f(X\mid\theta)\big]$，故 $E_\theta[U(\theta)]=0$。

*这个小引理是极大似然估计的相合性和 Cramér–Rao 界两者背后的主力。*

> **联系 —— 微积分：优化就是把得分置零**
>
> 极大化 $\ell(\theta)$ 就是那个微积分问题"找临界点"：解 $\ell'(\theta)=0$ 并验证 $\ell''(\theta)\lt 0$。负的二阶导数 $-\ell''$ 度量似然峰有多陡——而这条曲率*正是*观测到的 Fisher 信息。

## B 部分 · 点估计

<a id="s4"></a>
### 矩法

*关于估计量最古老的配方：把模型的理论矩与数据的经验矩相匹配，然后求解。*

**矩法（MoM）**

$$\text{set } \mu_k(\theta)=E_\theta[X^k] \ \text{equal to}\ m_k=\frac1n\sum_{i=1}^n X_i^k,\quad k=1,2,\dots$$

*用与未知参数同样多的矩方程，然后解出 $\theta$。简单、总是可用，但很少是最优的。*

**演示 —— 泊松、伯努利与正态的矩法估计量**

1. 泊松($\lambda$)：$E[X]=\lambda$。匹配到 $\bar X$：$\hat\lambda_{\text{MoM}}=\bar X$。
2. 伯努利($p$)：$E[X]=p$。匹配到 $\bar X$：$\hat p_{\text{MoM}}=\bar X$。
3. 正态($\mu,\sigma^2$)：一阶矩 $E[X]=\mu$ 给出 $\hat\mu=\bar X$；二阶矩 $E[X^2]=\sigma^2+\mu^2$ 匹配到 $\frac1n\sum X_i^2$ 给出

   $$\hat\sigma^2_{\text{MoM}}=\frac1n\sum_{i=1}^n X_i^2-\bar X^2=\frac1n\sum_{i=1}^n (X_i-\bar X)^2.$$

*注意除数是 $n$，而非 $n-1$：矩法方差是向下有偏的（见第 6 节）。*

> **原理 —— 何时求助于矩法**
>
> 当似然难以极大化时，或作为迭代极大似然的初值时，矩法大放异彩。它在温和条件下相合，但一般不如极大似然有效：它忽略了似然的完整形状，只用了少数几个矩。

<a id="s5"></a>
### 极大似然估计

*挑选使观测数据最可能出现的参数值。极大似然估计是现代统计学中占主导地位的估计量。*

**极大似然估计量**

$$\hat\theta_{\text{MLE}}=\arg\max_{\theta\in\Theta} L(\theta)=\arg\max_{\theta\in\Theta} \ell(\theta),\qquad \text{solve } U(\theta)=\ell'(\theta)=0$$

*极大化 $\ell$ 等价于极大化 $L$（对数是增函数），但把乘积变成了和。用 $\ell''(\hat\theta)\lt 0$ 确认是极大值。*

**演示 —— 伯努利 $p$ 的极大似然估计**

1. 对数似然：$\ell(p)=\big(\sum x_i\big)\log p+\big(n-\sum x_i\big)\log(1-p)$。
2. 得分置零：

   $$\ell'(p)=\frac{\sum x_i}{p}-\frac{n-\sum x_i}{1-p}=0.$$
3. 求解：$(1-p)\sum x_i=p\,(n-\sum x_i)\Rightarrow \sum x_i=pn$，故

   $$\hat p_{\text{MLE}}=\frac{1}{n}\sum_{i=1}^n x_i=\bar X.$$

*这里极大似然与矩法重合；一般情形下两者不同。*

**演示 —— 正态 $(\mu,\sigma^2)$ 的极大似然估计**

1. $\ell(\mu,\sigma^2)=-\frac n2\log(2\pi)-\frac n2\log\sigma^2-\frac{1}{2\sigma^2}\sum(x_i-\mu)^2$。
2. $\partial\ell/\partial\mu=\frac{1}{\sigma^2}\sum(x_i-\mu)=0\Rightarrow \hat\mu=\bar X$。
3. $\partial\ell/\partial\sigma^2=-\frac{n}{2\sigma^2}+\frac{1}{2\sigma^4}\sum(x_i-\mu)^2=0\Rightarrow$

   $$\hat\sigma^2_{\text{MLE}}=\frac1n\sum_{i=1}^n (x_i-\bar X)^2.$$

*除数又是 $n$。方差的极大似然估计是有偏的——下一节量化它。*

> **原理 —— 极大似然为何如此受推崇**
>
> 在正则条件下，极大似然估计是**相合的**、**渐近正态的**且**渐近有效的**——它在极限下达到 Cramér–Rao 界（第 7 节）。它还具有**不变性**：$g(\theta)$ 的极大似然估计是 $g(\hat\theta_{\text{MLE}})$。它唯一的弱点是有限样本下的偏差。

**极大似然估计的渐近正态性**

$$\sqrt n\,(\hat\theta_{\text{MLE}}-\theta)\ \xrightarrow{d}\ N\!\Big(0,\ \frac{1}{I_1(\theta)}\Big)$$

*$I_1(\theta)$ 是单个观测中的 Fisher 信息（第 7 节）。这是 Wald 区间与检验的发动机。*

> **联系 —— 应用于数据的微积分优化**
>
> 求 $\hat\theta_{\text{MLE}}$ 就是微积分中那套"把导数置零、检验二阶导数"的常规操作，现在应用于 $\ell(\theta)$。当不存在闭式解时，数值方法（Newton–Raphson，它用到 $\ell''$）接管——而 $\ell''$ 又是信息。

<a id="s6"></a>
### 评价估计量：偏差、方差、均方误差与相合性

*估计量是一个随机变量；我们以它在何处取中心、散布多大、以及随数据积累是否锁定真值来评判它。*

**偏差、方差与均方误差**

$$\operatorname{Bias}(\hat\theta)=E[\hat\theta]-\theta,\qquad \operatorname{MSE}(\hat\theta)=E\big[(\hat\theta-\theta)^2\big]$$

$$\operatorname{MSE}(\hat\theta)=\operatorname{Var}(\hat\theta)+\big[\operatorname{Bias}(\hat\theta)\big]^2$$

*当 $E[\hat\theta]=\theta$ 时估计量是**无偏的**。均方误差在散布与系统性偏移之间权衡——有时一点点偏差能换来少得多的方差。*

**演示 —— 均方误差的偏差–方差分解**

1. 加入并减去 $E[\hat\theta]$：$(\hat\theta-\theta)=(\hat\theta-E[\hat\theta])+(E[\hat\theta]-\theta)$。
2. 平方并取期望：

   $$E[(\hat\theta-\theta)^2]=E[(\hat\theta-E\hat\theta)^2]+2(E\hat\theta-\theta)E[\hat\theta-E\hat\theta]+(E\hat\theta-\theta)^2.$$
3. 交叉项因 $E[\hat\theta-E\hat\theta]=0$ 而消失，剩下 $\operatorname{MSE}=\operatorname{Var}+\operatorname{Bias}^2$。

*这与 $\operatorname{Var}(X)=E[X^2]-(E[X])^2$ 中"加减均值"的手法相同。*

**演示 —— 正态方差的极大似然估计有偏，及其均方误差**

1. 回顾 $\hat\sigma^2_{\text{MLE}}=\frac1n\sum(X_i-\bar X)^2=\frac{n-1}{n}S^2$，其中 $S^2=\frac{1}{n-1}\sum(X_i-\bar X)^2$ 是无偏版本。
2. 正态的一个关键抽样事实：$\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}$，故 $E[S^2]=\sigma^2$ 且 $\operatorname{Var}(S^2)=\frac{2\sigma^4}{n-1}$。
3. 因此 $E[\hat\sigma^2_{\text{MLE}}]=\frac{n-1}{n}\sigma^2$，给出偏差

   $$\operatorname{Bias}=\frac{n-1}{n}\sigma^2-\sigma^2=-\frac{\sigma^2}{n}.$$
4. 方差：$\operatorname{Var}(\hat\sigma^2_{\text{MLE}})=\big(\tfrac{n-1}{n}\big)^2\frac{2\sigma^4}{n-1}=\frac{2(n-1)\sigma^4}{n^2}$。加上偏差平方，

   $$\operatorname{MSE}(\hat\sigma^2_{\text{MLE}})=\frac{2(n-1)\sigma^4}{n^2}+\frac{\sigma^4}{n^2}=\frac{(2n-1)\,\sigma^4}{n^2}.$$

*引人注目的是，$\hat\sigma^2_{\text{MLE}}$ 的均方误差*小于*无偏的 $S^2$（其均方误差为 $2\sigma^4/(n-1)$）：这是偏差获利的教科书式案例。*

> **原理 —— 相合性**
>
> 如果当 $n\to\infty$ 时 $\hat\theta_n\xrightarrow{p}\theta$，则估计量是**相合的**。一个充分条件是 $\operatorname{MSE}(\hat\theta_n)\to 0$（均方相合性，借助 Chebyshev）。有偏和无偏的方差估计量都是相合的，因为它们的偏差和方差各自都趋于零——偏差在小样本中要紧，在极限下则不然。

> **联系 —— 入门指南的 $n-1$ 终于得到解释**
>
> 入门指南只是断言"除以 $n-1$ 以使 $E[S^2]=\sigma^2$"。这里我们看到了确切的原因：极大似然的除数 $n$ 带来 $-\sigma^2/n$ 的偏差，而 $n-1$（Bessel）修正消除了它。那个"损失的自由度"就是上面的 $\chi^2_{n-1}$。

<a id="s7"></a>
### Fisher 信息与 Cramér–Rao 下界

*任何无偏估计量能达到的精度都有一个硬性下限。Fisher 信息度量一个样本告诉你多少关于 $\theta$ 的信息；它的倒数就是那个下限。*

**Fisher 信息**

$$I(\theta)=E\!\left[\Big(\frac{\partial}{\partial\theta}\log f(X\mid\theta)\Big)^2\right]=-\,E\!\left[\frac{\partial^2}{\partial\theta^2}\log f(X\mid\theta)\right]$$

$$I_n(\theta)=n\,I_1(\theta)\quad\text{(information adds over i.i.d. observations)}$$

*信息是得分的方差，等价地是对数似然的期望曲率。一个尖峰似然意味着高信息，意味着精确的估计。*

**演示 —— 伯努利 $p$ 的 Fisher 信息**

1. 单个观测：$\log f(x\mid p)=x\log p+(1-x)\log(1-p)$。
2. 得分：$\frac{\partial}{\partial p}\log f=\frac{x}{p}-\frac{1-x}{1-p}$。二阶导数：$-\frac{x}{p^2}-\frac{1-x}{(1-p)^2}$。
3. 取 $-E[\cdot]$ 并代入 $E[X]=p$：

   $$I_1(p)=\frac{p}{p^2}+\frac{1-p}{(1-p)^2}=\frac1p+\frac1{1-p}=\frac{1}{p(1-p)}.$$

*于是 $I_n(p)=n/[p(1-p)]$ ——$p$ 越极端，每次试验越具信息量。*

**Cramér–Rao 下界（CRLB）**

$$\text{for any unbiased }\hat\theta:\qquad \operatorname{Var}(\hat\theta)\ \ge\ \frac{1}{I_n(\theta)}=\frac{1}{n\,I_1(\theta)}$$

*没有无偏估计量能胜过这个方差。达到它的估计量是**有效的**；它的**相对效率**是该界与其实际方差之比。*

**演示 —— Cramér–Rao 界的概要**

1. 设 $\hat\theta$ 无偏，$U=U(\theta)$ 为得分，满足 $E[U]=0$ 且 $\operatorname{Var}(U)=I_n(\theta)$。
2. 在积分号下对 $E[\hat\theta]=\theta$ 求导给出 $\operatorname{Cov}(\hat\theta,U)=1$。
3. Cauchy–Schwarz 不等式：$1=\operatorname{Cov}(\hat\theta,U)^2\le \operatorname{Var}(\hat\theta)\,\operatorname{Var}(U)=\operatorname{Var}(\hat\theta)\,I_n(\theta)$。
4. 整理：

   $$\operatorname{Var}(\hat\theta)\ge\frac{1}{I_n(\theta)}.$$

*例证：对伯努利，$\hat p=\bar X$ 有 $\operatorname{Var}=p(1-p)/n=1/I_n(p)$ ——它恰好达到该界，故 $\bar X$ 是有效的。*

> **联系 —— 曲率、微积分与极大似然**
>
> 形式 $I=-E[\ell'']$ 字面上就是期望的二阶导数——对数似然在其峰处弯曲程度的微积分度量。这正是为什么极大似然的渐近方差是 $1/I_n(\theta)$：更弯的似然把 $\theta$ 钉得更紧。

<a id="s8"></a>
### Rao–Blackwell 与最小方差无偏估计量

*给定任意无偏估计量，对充分统计量取条件只会改善它。配合完备性，这就产生唯一的最优无偏估计量。*

**Rao–Blackwell 定理**

$$\text{if } E[\tilde\theta]=\theta \text{ and } T \text{ is sufficient, then } \hat\theta=E[\tilde\theta\mid T] \text{ satisfies } E[\hat\theta]=\theta,\quad \operatorname{Var}(\hat\theta)\le \operatorname{Var}(\tilde\theta)$$

*对充分统计量取条件保持无偏性且决不增大方差——把估计量"Rao–Blackwell 化"。*

**演示 —— 把一个粗糙的泊松估计量 Rao–Blackwell 化**

1. 设 $X_1,\dots,X_n\ \text{i.i.d.}\ \sim\text{Poisson}(\lambda)$；我们想估计 $g(\lambda)=e^{-\lambda}=P(X=0)$。
2. 一个粗糙的无偏估计量：$\tilde g=\mathbf{1}\{X_1=0\}$，因为 $E[\tilde g]=P(X_1=0)=e^{-\lambda}$。但它只用了一个观测——很浪费。
3. 总和 $T=\sum X_i$ 是充分的（且完备的）。Rao–Blackwell 化：$\hat g=E[\mathbf 1\{X_1=0\}\mid T]=P(X_1=0\mid T)$。
4. 给定 $T=t$，$X_1$ 的条件分布是 $\text{Binomial}(t,1/n)$，故

   $$\hat g=P(X_1=0\mid T=t)=\Big(1-\tfrac1n\Big)^{t}=\Big(\tfrac{n-1}{n}\Big)^{\sum X_i}.$$

*这个改进后的估计量无偏且方差更小——并且，由完备性，它是 $e^{-\lambda}$ 的唯一最小方差无偏估计量。*

**Lehmann–Scheffé 定理（最小方差无偏估计）**

$$T \text{ complete \& sufficient},\ \ E[\,\varphi(T)\,]=\theta \ \Longrightarrow\ \varphi(T) \text{ is the unique MVUE of }\theta$$

*如果存在一个完备充分统计量的无偏函数，它就是*那个*最小方差无偏估计量。完备性保证唯一性。*

> **原理 —— 通向最优无偏估计量的路径**
>
> (1) 找一个完备充分统计量 $T$（通常借助指数族）。(2) 找任意一个无偏估计量。(3) 对它取关于 $T$ 的条件，或直接找一个具有正确均值的 $T$ 的函数。结果就是最小方差无偏估计量。对正态样本，$\bar X$ 是 $\mu$ 的最小方差无偏估计量，$S^2$ 是 $\sigma^2$ 的最小方差无偏估计量。

> **联系 —— 充分性收获回报**
>
> 第 2 节承诺充分性会让我们"免费"改善估计量。Rao–Blackwell 就是这个回报：保持信息的压缩 $T$ 正是我们用来取条件以抖落无关方差的对象。

## C 部分 · 区间估计与检验

<a id="s9"></a>
### 通过枢轴量构造置信区间

*置信区间由一个枢轴量建立：它是数据与参数的函数，其分布是固定且已知的。反转其已知的分位数来夹住 $\theta$。*

**枢轴量**

$$Q(\mathbf X,\theta)\ \text{is a pivot if its distribution does not depend on }\theta.$$

*由 $P(a\le Q\le b)=1-\alpha$，用代数把 $\theta$ 分离出来，得到一个以概率 $1-\alpha$ 覆盖 $\theta$ 的随机区间。*

**演示 —— 正态均值的置信区间，$\sigma$ 已知**

1. 枢轴量：$Z=\dfrac{\bar X-\mu}{\sigma/\sqrt n}\sim N(0,1)$，与 $\mu$ 无关。
2. 夹住它：$P\big(-z_{\alpha/2}\le Z\le z_{\alpha/2}\big)=1-\alpha$。
3. 对 $\mu$ 解这些不等式：

   $$\bar X-z_{\alpha/2}\frac{\sigma}{\sqrt n}\ \le\ \mu\ \le\ \bar X+z_{\alpha/2}\frac{\sigma}{\sqrt n}.$$

*对 $\alpha=0.05$，$z_{\alpha/2}=1.96$ ——这就是经验法则中的"两个标准误"。*

**演示 —— 正态均值的置信区间，$\sigma$ 未知（$t$ 枢轴量）**

1. 用 $S$ 替换 $\sigma$。枢轴量 $T=\dfrac{\bar X-\mu}{S/\sqrt n}$ 不再是正态的：分子为 $N(0,1)$，除以一个独立的 $\sqrt{\chi^2_{n-1}/(n-1)}$。
2. 按定义该比值是自由度为 $n-1$ 的学生 $t$：$T\sim t_{n-1}$，仍与 $\mu$ 和 $\sigma$ 无关。
3. 反转：

   $$\bar X\ \pm\ t_{n-1,\,\alpha/2}\,\frac{S}{\sqrt n}.$$

*更肥的 $t$ 尾部是估计 $\sigma$ 的代价；当 $n\to\infty$ 时，$t_{n-1}\to N(0,1)$。*

> **原理 —— 置信的含义**
>
> 置信是**过程**的属性，而非某一个区间的属性。"95% 置信"意味着：在重复抽样中，那个随机区间有 $95\%$ 的时候覆盖固定的 $\theta$。一旦算出，某个特定区间要么包含 $\theta$ 要么不包含——已无概率可言。

> **联系 —— 枢轴量统一了入门指南的各种区间**
>
> 入门指南中的每个置信区间——对均值、对比例、对方差（使用 $\chi^2$ 枢轴量）——都是某个枢轴量的反转。配方"估计 $\pm$ 临界值 $\times$ 标准误"是枢轴量近似为 $N(0,1)$ 的特殊情形。

<a id="s10"></a>
### 假设检验：错误、势与 Neyman–Pearson 引理

*一个检验把数据空间划分为"拒绝"和"不拒绝"。在所有水平为 $\alpha$ 的检验中，哪一个势最大？对简单假设，Neyman–Pearson 给出确切答案。*

**错误、检验大小与势**

$$\alpha=P_{\theta_0}(\text{reject }H_0)\ \text{(Type I)},\qquad \beta=P_{\theta_1}(\text{fail to reject }H_0)\ \text{(Type II)}$$

$$\text{power}=1-\beta=P_{\theta_1}(\text{reject }H_0)$$

*一个检验有**大小** $\alpha$（最大第一类错误率）和一个**势函数** $\beta(\theta)=P_\theta(\text{reject})$。我们固定 $\alpha$ 并极大化势。*

**Neyman–Pearson 引理**

$$\text{For }H_0:\theta=\theta_0 \text{ vs } H_1:\theta=\theta_1,\ \text{the most powerful size-}\alpha\text{ test rejects when } \frac{L(\theta_1)}{L(\theta_0)}\ge k.$$

*似然比是两个简单假设的最优检验统计量；选择 $k$ 使检验大小等于 $\alpha$。*

**演示 —— Neyman–Pearson 最优性**

1. 设 $\phi^*$ 为在 $L(\theta_1)\ge k\,L(\theta_0)$ 时拒绝的似然比（LR）检验，其大小恰为 $\alpha$。设 $\phi$ 为任意其他大小 $\le\alpha$ 的检验。
2. 考虑 $(\phi^*-\phi)\big(L(\theta_1)-kL(\theta_0)\big)$。在 $\phi^*=1$ 处第二个因子 $\ge0$；在 $\phi^*=0$ 处它 $\le0$；在两个区域里乘积都 $\ge0$。故

   $$\int (\phi^*-\phi)\big(L(\theta_1)-kL(\theta_0)\big)\,d\mathbf x\ \ge\ 0.$$
3. 拆分：$\big[\text{power}(\phi^*)-\text{power}(\phi)\big]-k\big[\text{size}(\phi^*)-\text{size}(\phi)\big]\ge0$。由于 $\text{size}(\phi)\le\alpha=\text{size}(\phi^*)$，右边括号中的项 $\ge0$。
4. 因此 $\text{power}(\phi^*)\ge\text{power}(\phi)$：LR 检验最强大。

*似然比的最优性是下一节每个检验的萌芽。*

**演示 —— 正态均值的最强大检验**

1. $X_i\sim N(\mu,\sigma^2)$，$\sigma$ 已知，$H_0:\mu=\mu_0$ vs $H_1:\mu=\mu_1$ 且 $\mu_1\gt\mu_0$。
2. 似然比关于 $\bar X$ 单调：$\log\frac{L(\mu_1)}{L(\mu_0)}=\frac{n(\mu_1-\mu_0)}{\sigma^2}\bar X+\text{const}$。对大似然比拒绝 $\iff$ 对大 $\bar X$ 拒绝。
3. 故在 $\bar X\ge c$ 时拒绝；选择 $c$ 使大小为 $\alpha$：$c=\mu_0+z_\alpha\,\sigma/\sqrt n$。等价地，在 $Z=\frac{\bar X-\mu_0}{\sigma/\sqrt n}\ge z_\alpha$ 时拒绝。

*熟悉的单侧 $z$ 检验就是 Neyman–Pearson 最优检验——而由于拒绝规则不依赖于具体的 $\mu_1$，它是对一切 $\mu\gt\mu_0$ 的**一致最强大**检验。*

> **联系 —— 检验与区间互为对偶**
>
> $H_0:\theta=\theta_0$ 的水平为 $\alpha$ 的双侧检验恰好在 $\theta_0$ 落在 $1-\alpha$ 置信区间之外时拒绝。检验的接受域，反转之后，*就是*一个置信集——这就是入门指南暗示过的同一种对偶性，现在变得确切。

<a id="s11"></a>
### 似然比、Wald 与得分检验

*对复合假设和多参数，三种渐近等价的检验占主导——全都由似然建立，全都近似为 $\chi^2$。*

**广义似然比统计量**

$$\Lambda=\frac{\sup_{\theta\in\Theta_0} L(\theta)}{\sup_{\theta\in\Theta} L(\theta)},\qquad -2\log\Lambda\ \xrightarrow{d}\ \chi^2_{r}$$

*$r$ 是 $H_0$ 施加的约束数目（自由参数的减少量）。对大的 $-2\log\Lambda$ 拒绝。这个极限就是 **Wilks 定理**。*

**演示 —— 一个似然比检验及其 $\chi^2_1$ 极限（Wilks）**

1. 正态样本，$\sigma$ 已知；检验 $H_0:\mu=\mu_0$ vs $H_1:\mu\ne\mu_0$。分子在 $\mu_0$ 处极大化 $L$；分母在 $\hat\mu=\bar X$ 处。
2. 代入正态似然：

   $$-2\log\Lambda=\frac{1}{\sigma^2}\Big[\sum(x_i-\mu_0)^2-\sum(x_i-\bar X)^2\Big]=\frac{n(\bar X-\mu_0)^2}{\sigma^2}.$$
3. 但在 $H_0$ 下 $\frac{\sqrt n(\bar X-\mu_0)}{\sigma}\sim N(0,1)$，故其平方恰为 $\chi^2_1$：

   $$-2\log\Lambda=\Big(\tfrac{\bar X-\mu_0}{\sigma/\sqrt n}\Big)^2=Z^2\sim\chi^2_1.$$

*这里 Wilks 的 $\chi^2_1$ 是精确的（一个约束，$r=1$）；一般情形下它渐近成立。*

**Wald 与得分（Rao）检验**

$$W=\frac{(\hat\theta-\theta_0)^2}{\widehat{\operatorname{Var}}(\hat\theta)}=I_n(\hat\theta)\,(\hat\theta-\theta_0)^2,\qquad R=\frac{U(\theta_0)^2}{I_n(\theta_0)}$$

*两者都 $\xrightarrow{d}\chi^2_r$。**Wald** 使用极大似然估计和 $\hat\theta$ 处的曲率；**得分**使用 $\ell$ 在 $\theta_0$ 处的斜率且无需极大似然估计。似然比、Wald 与得分检验渐近一致。*

> **原理 —— 一个峰的三种视角**
>
> 想象对数似然在其极大值附近。**似然比检验**度量 $\ell$ 从 $\hat\theta$ 到 $\theta_0$ 的垂直落差；**Wald** 检验度量水平距离 $\hat\theta-\theta_0$；**得分**检验度量 $\ell$ 在 $\theta_0$ 处的斜率。对一个二次（正态）对数似然这三者完全重合；一般情形下它们只在有限样本中相异。

> **联系 —— 让 Cramér–Rao 付诸实用**
>
> Wald 方差 $1/I_n(\hat\theta)$ 是在极大似然估计处求值的 Cramér–Rao 界——第 7 节作为分母里的标准误回归。得分检验直接使用 $U(\theta_0)$ 和 $I_n(\theta_0)$：正是第 3 节和第 7 节定义的那些量。

<a id="s12"></a>
### 标准检验及其抽样分布（t、χ²、F）

*三个分布，全都源自从正态总体抽样，为经典统计学提供精确的检验。*

**这三者如何从正态样本产生**

$$Z=\frac{\bar X-\mu}{\sigma/\sqrt n}\sim N(0,1),\qquad \frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}$$

$$t_k=\frac{Z}{\sqrt{\chi^2_k/k}},\qquad F_{d_1,d_2}=\frac{\chi^2_{d_1}/d_1}{\chi^2_{d_2}/d_2}$$

*对正态样本 $\bar X\perp S^2$（均值与方差的独立性）——这正是使 $t$ 比值的分子与分母独立的原因。*

| 分布 | 定义 | 用于 | 检验统计量 |
| --- | --- | --- | --- |
| $t_k$ | $N(0,1)\big/\sqrt{\chi^2_k/k}$ | 均值，$\sigma$ 未知；回归系数 | $t=\dfrac{\bar X-\mu_0}{S/\sqrt n}$ |
| $\chi^2_k$ | $k$ 个 $N(0,1)$ 平方之和 | 方差；拟合优度；独立性；似然比/Wald/得分的极限 | $\dfrac{(n-1)S^2}{\sigma_0^2}$，$\ \sum\dfrac{(O-E)^2}{E}$ |
| $F_{d_1,d_2}$ | 两个缩放 $\chi^2$ 之比 | 比较两个方差；方差分析（3 个以上均值） | $F=\dfrac{S_1^2}{S_2^2}$，$\ \dfrac{\text{MS}_{\text{between}}}{\text{MS}_{\text{within}}}$ |

**演示 —— 单样本 $t$ 统计量确实是 $t_{n-1}$**

1. 写 $\dfrac{\bar X-\mu}{S/\sqrt n}=\dfrac{(\bar X-\mu)/(\sigma/\sqrt n)}{S/\sigma}$。分子是 $N(0,1)$。
2. 分母：$S/\sigma=\sqrt{\dfrac{S^2}{\sigma^2}}=\sqrt{\dfrac{\chi^2_{n-1}/(n-1)\cdot\sigma^2}{\sigma^2}}=\sqrt{\chi^2_{n-1}/(n-1)}$，与分子独立。
3. 这恰好是 $\dfrac{N(0,1)}{\sqrt{\chi^2_{n-1}/(n-1)}}$，即 $t_{n-1}$ 的定义。

*这里 $t$ 分布不是一个近似——它是精确的抽样规律，也是入门指南"$\sigma$ 未知时用 $t$"正确的原因。*

> **联系 —— 让《概率论》指南的分布派上用场**
>
> 在《概率论》指南中抽象定义的 $\chi^2$、$t$ 和 $F$ 恰好是正态数据统计量的抽样分布。经典推断在很大程度上就是用这三条规律记账。

## D 部分 · 贝叶斯与非参数

<a id="s13"></a>
### 贝叶斯推断：先验、后验与共轭

*把 $\theta$ 本身视为随机的。把信念编码进一个先验，通过贝叶斯定理用数据更新，然后读出后验——$\theta$ 的一个完整分布。*

**关于参数的贝叶斯定理**

$$\pi(\theta\mid\mathbf x)=\frac{L(\theta)\,\pi(\theta)}{\int L(\theta)\,\pi(\theta)\,d\theta}\ \propto\ \underbrace{L(\theta)}_{\text{likelihood}}\ \underbrace{\pi(\theta)}_{\text{prior}}$$

*后验 $\propto$ 似然 $\times$ 先验。分母（边际/证据）只是归一化常数。*

> **概念 —— 共轭**
>
> 如果后验与先验属于同一族，则先验对似然是**共轭的**。共轭对使更新纯粹是代数运算——无需积分——并把数据的作用揭示为该族参数的改变。

| 似然 | 共轭先验 | 后验 |
| --- | --- | --- |
| 伯努利 / 二项($p$) | Beta($\alpha,\beta$) | Beta($\alpha+\sum x_i,\ \beta+n-\sum x_i$) |
| 泊松($\lambda$) | Gamma($\alpha,\beta$) | Gamma($\alpha+\sum x_i,\ \beta+n$) |
| 正态均值（$\sigma^2$ 已知） | Normal($\mu_0,\tau_0^2$) | Normal（精度加权，见下） |
| 正态精度（$\mu$ 已知） | Gamma | Gamma |
| 指数($\lambda$) | Gamma($\alpha,\beta$) | Gamma($\alpha+n,\ \beta+\sum x_i$) |
| 多项 | Dirichlet | Dirichlet |

**演示 —— Beta–伯努利更新**

1. 先验 $\pi(p)\propto p^{\alpha-1}(1-p)^{\beta-1}$（Beta），似然 $L(p)\propto p^{\sum x_i}(1-p)^{n-\sum x_i}$。
2. 相乘：

   $$\pi(p\mid\mathbf x)\propto p^{\alpha+\sum x_i-1}(1-p)^{\beta+n-\sum x_i-1}.$$
3. 这是 $\text{Beta}\big(\alpha+\sum x_i,\ \beta+n-\sum x_i\big)$ 的核——同一族，参数被成功与失败的计数撑大。

*先验参数 $(\alpha,\beta)$ 起着先验成功与失败"伪计数"的作用。*

> **联系 —— 来自《概率论》指南的贝叶斯定理**
>
> 这与用于事件的同一个贝叶斯定理一样，只是提升到密度：$P(A\mid B)\propto P(B\mid A)P(A)$ 变成 $\pi(\theta\mid x)\propto f(x\mid\theta)\pi(\theta)$。频率派与贝叶斯推断共享似然；它们的区别仅在于 $\theta$ 是否获得一个概率分布。

<a id="s14"></a>
### 贝叶斯估计与可信区间

*从后验中我们提取点估计和区间——而著名的正态–正态更新表明后验均值是先验与数据的精度加权平均。*

**后验点估计**

$$\hat\theta_{\text{Bayes}}=E[\theta\mid\mathbf x]\ \text{(posterior mean, min. squared-error loss)},\qquad \hat\theta_{\text{MAP}}=\arg\max_\theta \pi(\theta\mid\mathbf x)$$

*后验均值最小化期望平方误差损失；后验中位数最小化绝对损失；最大后验（众数）是带先验惩罚的极大似然的贝叶斯类比。*

**演示 —— 正态先验共轭；后验均值是精度加权的**

1. 数据 $\bar X\mid\mu\sim N(\mu,\sigma^2/n)$（$\sigma$ 已知），先验 $\mu\sim N(\mu_0,\tau_0^2)$。把两个正态核相乘并对 $\mu$ 配方。
2. 指数关于 $\mu$ 是二次的，故后验为正态：$\mu\mid\mathbf x\sim N(\mu_n,\tau_n^2)$，精度相加，

   $$\frac{1}{\tau_n^2}=\frac{1}{\tau_0^2}+\frac{n}{\sigma^2}.$$
3. 后验均值是先验均值与样本均值的精度加权平均：

   $$\mu_n=\frac{\frac{1}{\tau_0^2}\,\mu_0+\frac{n}{\sigma^2}\,\bar X}{\frac{1}{\tau_0^2}+\frac{n}{\sigma^2}}.$$

*当 $n\to\infty$ 时数据精度 $n/\sigma^2$ 占主导，$\mu_n\to\bar X$，先验被冲刷掉——贝叶斯与频率派估计收敛到一起。*

**可信区间**

$$P\big(\theta\in C\mid\mathbf x\big)=1-\alpha,\qquad \text{e.g. } [\,q_{\alpha/2},\,q_{1-\alpha/2}\,]\ \text{of the posterior}$$

*与置信区间不同，这*确实*是给定数据时关于 $\theta$ 的一个直接概率陈述——人们错误地附加给置信区间的那种解释。*

> **原理 —— 可信 vs 置信**
>
> 95% **可信**区间说"给定数据和先验，$\theta$ 以 0.95 的概率落在这里"。95% **置信**区间对过程作一个长期频率断言。在平坦先验和对称似然下两者常常在数值上重合，但它们的含义截然不同。

> **联系 —— 正则化就是一个先验**
>
> 在 $\mu$ 上用正态先验的最大后验估计恰好是把 $\bar X$ 向 $\mu_0$ 作岭回归式收缩。惩罚似然方法就是伪装的最大后验估计——这是贝叶斯先验与估计的优化视角之间的一座桥。

<a id="s15"></a>
### 非参数方法与自助法

*当你不愿假设一个参数模型时，让数据替代总体。经验分布和重抽样担起重活。*

**经验分布函数**

$$\hat F_n(x)=\frac1n\sum_{i=1}^n \mathbf 1\{X_i\le x\}\ \xrightarrow{\text{a.s.}}\ F(x)\quad(\text{Glivenko–Cantelli, uniformly})$$

*$\hat F_n$ 是 $F$ 的非参数极大似然估计。插入式估计量用 $\hat F_n$ 替换 $F$：样本均值估计总体均值，样本中位数估计总体中位数，依此类推。*

> **概念 —— 自助法的想法**
>
> 要在没有公式的情况下衡量统计量 $\hat\theta=T(\hat F_n)$ 的变异性，就把样本当作总体：从中重抽样并观察 $\hat\theta$ 如何变化。**插入式原理**——用 $\hat F_n$ 替换 $F$——就是全部诀窍。

**演示 —— 用非参数自助法估计标准误**

1. 从观测样本 $\{x_1,\dots,x_n\}$ 中有放回地抽取一个容量为 $n$ 的重抽样：$\{x_1^*,\dots,x_n^*\}$。
2. 在重抽样上计算统计量，$\hat\theta^{*(b)}=T(x_1^*,\dots,x_n^*)$（例如样本中位数）。
3. 对 $b=1,\dots,B$（比如 $B=2000$）重复以得到 $\hat\theta^{*(1)},\dots,\hat\theta^{*(B)}$。
4. 用自助复制的散布来估计标准误：

   $$\widehat{\text{SE}}_{\text{boot}}=\sqrt{\frac{1}{B-1}\sum_{b=1}^B\big(\hat\theta^{*(b)}-\bar{\hat\theta}^{*}\big)^2}.$$
5. 一个简单的 $1-\alpha$ 区间：由复制的经验分位数得到的百分位区间 $\big[\hat\theta^{*}_{(\alpha/2)},\ \hat\theta^{*}_{(1-\alpha/2)}\big]$。

*没有分布假设，没有中心极限定理公式——重抽样仅凭数据本身重建了抽样分布。*

> **联系 —— 自助法为何有效**
>
> 抽样分布描述当样本从 $F$ 中抽取时 $\hat\theta$ 如何变化。自助法用 $\hat F_n$ 代替未知的 $F$ 并从*它*中抽取。Glivenko–Cantelli 保证 $\hat F_n\approx F$，故自助变异性逼近真实抽样变异性——插入式原理付诸实用。

<a id="s16"></a>
### 越界一瞥：决策论与大样本渐近

*一个统一框架——把估计和检验视为损失下的决策——以及那套使极大似然成为默认工具的渐近机制（delta 方法、效率）。*

**风险，决策的语言**

$$R(\theta,\delta)=E_\theta\big[\,\ell(\theta,\delta(\mathbf X))\,\big],\qquad \text{e.g. squared-error loss } \ell(\theta,d)=(d-\theta)^2\Rightarrow R=\text{MSE}$$

*一个决策规则 $\delta$ 把数据映射到行动；它的**风险**是期望损失。在平方误差损失下，风险恰为第 6 节的均方误差——估计是决策论的一个特例。*

> **原理 —— 可容许性、极小极大与贝叶斯规则**
>
> 一个规则是**不可容许的**，如果存在另一个规则处处风险 $\le$ 且在某处严格更小。一个**极小极大**规则最小化最坏情形风险；一个**贝叶斯**规则最小化对先验取平均的风险——它就是第 14 节的后验期望损失最小化者。值得注意的是，在维数 $\ge3$ 时样本均值是不可容许的（Stein 悖论）：收缩估计量处处胜过它。

**delta 方法**

$$\sqrt n\,(\hat\theta-\theta)\xrightarrow{d}N(0,\sigma^2)\ \Longrightarrow\ \sqrt n\,\big(g(\hat\theta)-g(\theta)\big)\xrightarrow{d}N\!\big(0,\ [g'(\theta)]^2\sigma^2\big)$$

*一阶 Taylor 展开把渐近正态性通过一个光滑变换 $g$ 传播——误差传播的渐近版本，纯粹的微积分。*

**演示 —— 一行写出 delta 方法**

1. 把 $g$ 在 $\theta$ 附近 Taylor 展开：$g(\hat\theta)\approx g(\theta)+g'(\theta)(\hat\theta-\theta)$。
2. 乘以 $\sqrt n$：$\sqrt n\,(g(\hat\theta)-g(\theta))\approx g'(\theta)\cdot\sqrt n\,(\hat\theta-\theta)$。
3. 右边是 $g'(\theta)$ 乘以一个收敛到 $N(0,\sigma^2)$ 的量，由 Slutsky 定理给出方差 $[g'(\theta)]^2\sigma^2$。

*这就是如何为优势比、率以及其他变换后参数得到标准误。*

> **原理 —— 极大似然的渐近至上**
>
> 在正则性下，$\sqrt n(\hat\theta_{\text{MLE}}-\theta)\xrightarrow{d}N(0,1/I_1(\theta))$：极大似然估计是相合的、渐近正态的且渐近有效的——它在极限下达到 Cramér–Rao 界。这就是为什么在没有特殊结构时，极大似然（及其贝叶斯表亲）是统计推断的主力。

> **联系 —— 整篇指南，浓缩为一条弧线**
>
> 似然（s3）给出得分与信息（s7）；极大化它给出极大似然估计（s5）；信息为它的方差设界（s7–8），并设定区间的宽度（s9）和检验的尺度（s10–11）；同一个似然，乘以一个先验，给出后验（s13–14）；而在不假设模型之处，经验分布和自助法（s15）顶上。一个函数——似然——组织起整个学科。

---

*一门数理统计课程——充分性、估计、Cramér–Rao 界、Neyman–Pearson 与似然比检验、贝叶斯更新以及自助法——每条原理都被精确陈述，每个定理都被演示。它是入门《统计学》和《概率论》指南的伴读。把任何方框当作参考随时回看，并记住：在估计、检验和贝叶斯背后，统统站着同一个对象——似然函数。*
