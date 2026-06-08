[English](probability.md) · **中文**

# 概率论，*臻于严格。*

一门完整的数学概率论课程——从柯尔莫哥洛夫公理出发，经由随机变量及其矩，直至支撑全部统计学的极限定理。每一个核心结论都有**演示**，并将通往微积分与推断的脉络明确点出。

[← 返回全部指南](../README.zh.md)

## A 部分 · 基础

<a id="s0"></a>
### 全局图景：使随机性变得严格

*概率论是关于不确定性的数学——一套关于事物可能性大小的演算，建立在一小组公理之上，并一路延伸至深刻的极限定理。*

数个世纪以来，概率论只是赌徒们的一堆巧妙技巧。1933 年，安德雷·柯尔莫哥洛夫为它奠定了严格的基础：概率不过是一种**测度**——一种为某个结果空间的子集赋予介于 0 与 1 之间的"大小"的方式。从三条简短的公理出发，整门学科都可以通过演绎逐步展开。

- **建模**——把一个试验编码为样本空间、事件和一个概率测度。
- **量化**——通过*随机变量*把数附给结果，并用期望、方差和矩来概括它们。
- **取极限**——让重复次数增多，观察秩序如何浮现：大数定律和中心极限定理。

> **原理 — 概率的两副面孔**
>
> **频率派**的解读说 $P(A)$ 是在反复试验中 $A$ 发生的长期频率；**主观派**的解读说它是一种自洽的置信度。柯尔莫哥洛夫的公理是中立的：它们描述任何合理的概率概念必须满足什么，而把解释留给你。无论哪一种，数学都是一样的。

#### 一行话概括整门学科

> 公理 → 条件概率与贝叶斯 → 随机变量与矩 → 联合行为 → 不等式 → 大数定律与 CLT

> **联系 — 概率是统计学之下的引擎**
>
> 在配套的《统计学》指南中，概率沿"总体 $\to$ 样本"运行，而推断沿"样本 $\to$ 总体"运行。本指南完整地构建那台引擎：那里所用的抽样分布、标准误和正态近似，都是本指南 D 部分中证明的定理。

<a id="s1"></a>
### 样本空间、事件与公理（柯尔莫哥洛夫）

*一切都始于一个结果集合、一族事件，以及它们上面的一个测度。*

> **概念 — 概率三元组**
>
> 一个概率模型是一个三元组 $(\Omega,\mathcal F,P)$。**样本空间** $\Omega$ 是所有可能结果 $\omega$ 的集合。**事件空间** $\mathcal F$ 是 $\Omega$ 的子集（即事件）的一个族，对取补和可数并封闭——即一个 $\sigma$-代数。**概率测度** $P:\mathcal F\to[0,1]$ 为每个事件赋予一个可能性。

**柯尔莫哥洛夫公理**

$$\text{(1)}\ \ P(A)\ge 0\quad\text{for all }A\in\mathcal F$$

$$\text{(2)}\ \ P(\Omega)=1$$

$$\text{(3)}\ \ P\!\Big(\bigcup_{i=1}^{\infty}A_i\Big)=\sum_{i=1}^{\infty}P(A_i)\quad\text{for disjoint }A_i$$

*公理 (3) 是**可数可加性**——真正起作用的那一条假设，它给出概率的连续性，并使极限表现良好。*

**演示 — 公理所迫使的推论**

1. 由于 $A\cup A^c=\Omega$ 是不相交的，$P(A)+P(A^c)=P(\Omega)=1$，于是

   $$P(A^c)=1-P(A),\qquad P(\varnothing)=0.$$
2. 当 $A\subseteq B$ 时，把 $B=A\cup(B\setminus A)$ 写成不相交之并；可加性给出 $P(B)=P(A)+P(B\setminus A)\ge P(A)$，故 $P$ 是单调的。
3. 把 $A\cup B=A\cup(B\setminus A)$ 与 $B=(A\cap B)\cup(B\setminus A)$ 都拆成不相交之并，再相减：

   $$P(A\cup B)=P(A)+P(B)-P(A\cap B).$$

*容斥法则不是公理——它是一条定理。单调性也是定理，$0\le P(A)\le1$ 也是。*

**容斥原理与连续性**

$$P\!\Big(\bigcup_{i=1}^n A_i\Big)=\sum_i P(A_i)-\sum_{i\lt j}P(A_i\cap A_j)+\cdots+(-1)^{n+1}P\!\Big(\bigcap_{i=1}^n A_i\Big)$$

$$A_n\uparrow A\ \Rightarrow\ P(A_n)\to P(A),\qquad A_n\downarrow A\ \Rightarrow\ P(A_n)\to P(A)$$

*从下/从上的连续性是可数可加性的直接推论；正是它让我们能够对事件取极限。*

> **概念 — 等可能结果**
>
> 当 $\Omega$ 有限且所有结果等可能时，测度退化为计数：$P(A)=|A|/|\Omega|$。这就是古典的"有利情形除以全部情形"的概率——也正是为什么下一节讲的是计数。

<a id="s2"></a>
### 计数：排列、组合与二项式定理

*在均匀模型里，概率就是计数。这里的组合学为随后的每一个离散分布提供动力。*

**基本计数原理**

$$\text{permutations: }\ P(n,k)=\frac{n!}{(n-k)!},\qquad \text{combinations: }\ \binom nk=\frac{n!}{k!\,(n-k)!}$$

*如果一项任务是一连串独立的选择，分别有 $n_1,n_2,\dots$ 个选项，那么总数是**乘积** $n_1 n_2\cdots$。排列计数有序的排列方式；组合计数无序的选取方式。*

**演示 — 为什么 $\binom nk$ 要把各种排序除掉**

1. 从 $n$ 个物品中选取 $k$ 个排成有序列表，共有 $P(n,k)=n(n-1)\cdots(n-k+1)=\tfrac{n!}{(n-k)!}$ 种方式。
2. 每一个由 $k$ 个物品组成的无序集合都可以按 $k!$ 种方式排序，所以它在那个列表中被计数了 $k!$ 次。
3. 相除以去掉这种重复计数：

   $$\binom nk=\frac{P(n,k)}{k!}=\frac{n!}{k!\,(n-k)!}.$$

*二项式系数就是"选 $k$ 个，不计顺序"。*

**二项式定理与帕斯卡法则**

$$(x+y)^n=\sum_{k=0}^{n}\binom nk x^k y^{n-k},\qquad \binom nk=\binom{n-1}{k-1}+\binom{n-1}{k}$$

*令 $x=y=1$ 得到 $\sum_k\binom nk=2^n$：一个 $n$ 元集的子集个数。帕斯卡法则逐行构建出三角形。*

**演示 — 用计数证明二项式定理**

1. 展开 $(x+y)^n=(x+y)(x+y)\cdots(x+y)$：每一项都从这 $n$ 个因子中各取 $x$ 或 $y$。
2. 恰好含 $k$ 个 $x$（以及 $n-k$ 个 $y$）的项是 $x^k y^{n-k}$；选出哪 $k$ 个因子贡献 $x$ 的方式数为 $\binom nk$。
3. 对 $k$ 求和给出

   $$(x+y)^n=\sum_{k=0}^n\binom nk x^k y^{n-k}.$$

*这个恒等式正是二项分布的诸概率之和等于 1 的原因。*

> **概念 — 可区分与否、有放回与否**
>
> 四种经典的计数情形：有序有放回 $n^k$；有序无放回 $\tfrac{n!}{(n-k)!}$；无序无放回 $\binom nk$；无序有放回 $\binom{n+k-1}{k}$（隔板法）。判断自己处于哪一种情形，正是组合概率的全部技艺所在。

<a id="s3"></a>
### 条件概率、独立性与贝叶斯定理

*信息如何重塑概率——以及如何把条件的方向反转过来。*

**条件化、链式法则与独立性**

$$P(A\mid B)=\frac{P(A\cap B)}{P(B)}\quad(P(B)\gt0)$$

$$P(A_1\cap\cdots\cap A_n)=P(A_1)\,P(A_2\mid A_1)\cdots P(A_n\mid A_1\cap\cdots\cap A_{n-1})$$

$$A\perp B \iff P(A\cap B)=P(A)P(B) \iff P(A\mid B)=P(A)$$

*以 $B$ 为条件就是把世界限制在 $B$ 上并重新归一化。独立意味着 $B$ 不携带任何关于 $A$ 的信息。*

**全概率公式与贝叶斯定理**

$$P(B)=\sum_i P(B\mid A_i)\,P(A_i)\quad\text{for a partition }\{A_i\}$$

$$P(A_i\mid B)=\frac{P(B\mid A_i)\,P(A_i)}{\sum_j P(B\mid A_j)\,P(A_j)}$$

**演示 — 两行推出贝叶斯定理**

1. 乘法法则把联合概率写成两种形式：

   $$P(A\cap B)=P(A\mid B)P(B)=P(B\mid A)P(A).$$
2. 令右边两式相等并除以 $P(B)$，再用全概率公式展开 $P(B)$：

   $$P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}.$$

*贝叶斯定理把"在原因已知时证据的似然"变成"在证据已知时原因的概率"。*

> **原理 — 基础发生率占主导**
>
> 对于一种罕见状况，即使一项检验高度准确，也会产生许多假阳性，因为少量真正的病例被庞大的健康多数所淹没。贝叶斯定理迫使你用**先验** $P(A)$ 给检验结果加权。这一个洞见支撑了医学筛查、垃圾邮件过滤，以及全部贝叶斯推断。

> **概念 — 两两独立与相互独立**
>
> 事件可以两两独立却并不相互独立：每一对都独立并不能强制 $P(A\cap B\cap C)=P(A)P(B)P(C)$ 成立。相互独立要求乘积法则对*每一个*子族都成立——这是一个严格更强的条件。

> **联系 — 向前通往推断**
>
> 贝叶斯定理是本指南与统计推断之间的枢纽：贝叶斯更新"先验 $\times$ 似然 $\to$ 后验"正是这条公式，只不过把离散事件 $A_i$ 换成了关于未知参数的一个概率分布。

## B 部分 · 随机变量

<a id="s4"></a>
### 随机变量与分布函数（CDF、PMF、PDF）

*随机变量是从结果上读出的一个数。它的分布被一个函数完全刻画：CDF。*

> **概念 — 随机变量是一个函数**
>
> **随机变量** $X$ 是一个（可测）函数 $X:\Omega\to\mathbb R$，它为每个结果赋一个数。在试验运行之前它并不"拥有"一个值；它所拥有的是一个*分布*——概率在它各个可能取值上铺开的方式。

**累积分布函数（CDF）**

$$F_X(x)=P(X\le x)$$

*每个 CDF 都是非减的、右连续的，且 $F(-\infty)=0$、$F(+\infty)=1$。CDF 对*每一个*随机变量都存在，无论离散还是连续，并完全决定了分布。*

**PMF（离散）与 PDF（连续）**

$$\text{discrete: }\ p_X(x)=P(X=x),\qquad \sum_x p_X(x)=1$$

$$\text{continuous: }\ f_X(x)=F_X'(x),\qquad P(a\le X\le b)=\int_a^b f_X(x)\,dx,\qquad \int_{-\infty}^{\infty}f_X=1$$

*对于连续变量，每一个单点处 $P(X=x)=0$：概率是**面积**，而非高度。密度 $f$ 可以超过 1；只有它的积分受到约束。*

**演示 — 从 CDF 恢复概率**

1. 对任意 $a\lt b$，事件 $\{X\le b\}$ 拆成不相交的 $\{X\le a\}$ 与 $\{a\lt X\le b\}$。
2. 由可加性，$P(a\lt X\le b)=F(b)-F(a)$。
3. $F$ 在某点的跳跃就是该点的点质量：连续的 CDF 没有跳跃，故每个点的概率为零。

   $$P(X=x)=F(x)-F(x^-).$$

*CDF 是通用货币：对它求导得到密度，对它取差得到质量函数。*

> **联系 — 这里是微积分登场之处**
>
> 对于连续变量，密度扮演普通函数的角色，而概率就是它下方的积分。期望、百分位数、p 值和正态曲线全都是面积——正是你已经掌握的那门积分学，应用到 $f_X$ 上。

<a id="s5"></a>
### 期望、方差与矩

*期望是一个分布的质心；方差是它的转动惯量；高阶矩则填补它的形状。*

**期望与无意识统计学家定律**

$$E[X]=\sum_x x\,p_X(x)\quad\text{(discrete)},\qquad E[X]=\int_{-\infty}^{\infty} x\,f_X(x)\,dx\quad\text{(continuous)}$$

$$E[g(X)]=\sum_x g(x)\,p_X(x)\quad\text{or}\quad \int g(x)\,f_X(x)\,dx$$

*LOTUS（无意识统计学家定律）：要对 $g(X)$ 求平均，你无需先求出 $g(X)$ 的分布——只要把 $g$ 对 $X$ 的密度做积分即可。*

**方差、矩与线性性**

$$\operatorname{Var}(X)=E\big[(X-\mu)^2\big]=E[X^2]-\big(E[X]\big)^2$$

$$E[aX+b]=aE[X]+b,\qquad \operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$$

$$\mu_k=E\big[(X-\mu)^k\big]:\quad \text{skewness}=\tfrac{\mu_3}{\sigma^3},\quad \text{kurtosis}=\tfrac{\mu_4}{\sigma^4}$$

*期望无条件地具有线性性；方差按平方缩放，且对平移不变。*

**演示 — 方差的计算公式**

1. 展开定义中的平方：

   $$\operatorname{Var}(X)=E\big[(X-\mu)^2\big]=E\big[X^2-2\mu X+\mu^2\big].$$
2. 利用线性性和 $E[X]=\mu$：

   $$=E[X^2]-2\mu\,E[X]+\mu^2=E[X^2]-2\mu^2+\mu^2.$$
3. 合并各项：

   $$\operatorname{Var}(X)=E[X^2]-\mu^2=E[X^2]-(E[X])^2.$$

*"平方的均值减去均值的平方"——日常使用的方差公式。*

**演示 — 非负变量的 $E[X]$ 由其尾部给出**

1. 对连续的 $X\ge0$，写 $x=\int_0^x dt=\int_0^\infty \mathbf 1\{t\lt x\}\,dt$。
2. 取期望并交换次序（托内利定理）：

   $$E[X]=\int_0^\infty E[\mathbf 1\{t\lt X\}]\,dt=\int_0^\infty P(X\gt t)\,dt.$$

*期望等于 CDF 上方的面积——一个在极限定理中反复使用的尾部求和公式。*

<a id="s6"></a>
### 矩生成函数与特征函数

*把全部矩编码进单个函数。变换把卷积变成乘积，并使 CLT 成为一行式的极限。*

**MGF 与特征函数**

$$M_X(t)=E\big[e^{tX}\big],\qquad \varphi_X(t)=E\big[e^{itX}\big]$$

$$M_X^{(k)}(0)=E[X^k],\qquad M_X(t)=\sum_{k=0}^{\infty}\frac{E[X^k]}{k!}\,t^k$$

*MGF 通过在 0 处求导来"生成"矩。特征函数 $\varphi$ 总是存在（因为 $|e^{itX}|=1$），并唯一地决定分布。*

**演示 — 为什么 $M^{(k)}(0)=E[X^k]$**

1. 把期望里的指数展开：

   $$M_X(t)=E\Big[\sum_{k=0}^\infty \frac{(tX)^k}{k!}\Big]=\sum_{k=0}^\infty \frac{t^k}{k!}E[X^k].$$
2. 这是一个关于 $t$ 的泰勒级数；$t^k$ 的系数是 $E[X^k]/k!$。
3. 求导 $k$ 次并令 $t=0$ 就提取出那个系数：

   $$M_X^{(k)}(0)=E[X^k].$$

*求导取代了积分——这正是 MGF 如此方便的实际原因。*

**演示 — 计算指数分布的 MGF 及其各阶矩**

1. 对 $X\sim\text{Exp}(\lambda)$，$f(x)=\lambda e^{-\lambda x}$（$x\ge0$）：

   $$M_X(t)=\int_0^\infty e^{tx}\lambda e^{-\lambda x}\,dx=\lambda\int_0^\infty e^{-(\lambda-t)x}\,dx=\frac{\lambda}{\lambda-t},\ \ t\lt\lambda.$$
2. 求导：$M'(t)=\dfrac{\lambda}{(\lambda-t)^2}$，故 $E[X]=M'(0)=1/\lambda$。
3. 再求导：$M''(t)=\dfrac{2\lambda}{(\lambda-t)^3}$，故 $E[X^2]=2/\lambda^2$，于是

   $$\operatorname{Var}(X)=\frac{2}{\lambda^2}-\frac1{\lambda^2}=\frac1{\lambda^2}.$$

*一个变换无需再做积分就同时给出了均值和方差。*

**关键性质：和的 MGF**

$$X\perp Y\ \Rightarrow\ M_{X+Y}(t)=M_X(t)\,M_Y(t)$$

*因为 $e^{t(X+Y)}=e^{tX}e^{tY}$，而独立性使期望可分解为乘积。独立变量之和 $\leftrightarrow$ 变换之积——这是卷积以及 CLT 证明的基础。*

> **联系 — 微积分：泰勒级数与变换**
>
> MGF 不过是矩序列的指数型生成函数；读出各阶矩就是读出泰勒系数。特征函数是密度的傅里叶变换——这正是为什么对它求逆就能恢复分布。

<a id="s7"></a>
### 常见离散分布

*少数几个有名字的分布律就能为大多数计数情形建模。要记住每一个的来历、均值、方差和 MGF。*

| 分布 | PMF $p(k)$ | 均值 | 方差 | MGF $M(t)$ |
| --- | --- | --- | --- | --- |
| 伯努利($p$) | $p^k(1-p)^{1-k},\ k\in\{0,1\}$ | $p$ | $p(1-p)$ | $1-p+pe^{t}$ |
| 二项($n,p$) | $\binom nk p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ | $(1-p+pe^{t})^n$ |
| 几何($p$) | $(1-p)^{k-1}p,\ k\ge1$ | $1/p$ | $(1-p)/p^2$ | $\dfrac{pe^{t}}{1-(1-p)e^{t}}$ |
| 负二项($r,p$) | $\binom{k-1}{r-1}p^r(1-p)^{k-r}$ | $r/p$ | $r(1-p)/p^2$ | $\big(\tfrac{pe^{t}}{1-(1-p)e^{t}}\big)^r$ |
| 泊松($\lambda$) | $e^{-\lambda}\lambda^k/k!$ | $\lambda$ | $\lambda$ | $e^{\lambda(e^{t}-1)}$ |

**演示 — 由伯努利构建二项分布（均值与方差）**

1. 把 $X=X_1+\cdots+X_n$ 写成 i.i.d. 伯努利($p$) 指示变量之和，每个满足 $E[X_i]=p$、$\operatorname{Var}(X_i)=p(1-p)$。
2. 由线性性（无需独立性）：

   $$E[X]=\sum_{i=1}^n E[X_i]=np.$$
3. 由独立性，方差相加：

   $$\operatorname{Var}(X)=\sum_{i=1}^n \operatorname{Var}(X_i)=np(1-p).$$
4. MGF 相乘：$M_{X_i}(t)=1-p+pe^t$，故 $M_X(t)=(1-p+pe^t)^n$，与表中一致。

*分解为简单部件，再求和——概率论反复出现的招式。*

**演示 — 泊松分布的均值与方差**

1. 直接计算均值：

   $$E[X]=\sum_{k=0}^\infty k\,\frac{e^{-\lambda}\lambda^k}{k!}=\lambda e^{-\lambda}\sum_{k=1}^\infty\frac{\lambda^{k-1}}{(k-1)!}=\lambda e^{-\lambda}e^{\lambda}=\lambda.$$
2. 求方差时用 MGF $M(t)=e^{\lambda(e^t-1)}$：$M'(t)=\lambda e^t M(t)$，故 $E[X]=M'(0)=\lambda$。
3. 再求导：$M''(t)=\lambda e^t M(t)+(\lambda e^t)^2 M(t)$，得 $E[X^2]=\lambda+\lambda^2$，因此

   $$\operatorname{Var}(X)=\lambda+\lambda^2-\lambda^2=\lambda.$$

*泊松分布的标志：它的均值与方差相等。*

**演示 — 几何分布的均值及其无记忆性**

1. 令 $q=1-p$，则 $E[X]=\sum_{k\ge1}k\,q^{k-1}p=p\sum_{k\ge1}kq^{k-1}=p\cdot\dfrac{1}{(1-q)^2}=\dfrac1p$，这里用到 $\sum_{k\ge1}kq^{k-1}=(1-q)^{-2}$。
2. 无记忆性：$P(X\gt m+n\mid X\gt m)=\dfrac{q^{m+n}}{q^{m}}=q^{n}=P(X\gt n)$。

*几何分布是唯一的离散无记忆分布律——指数分布的离散孪生。*

> **联系 — 作为二项极限的泊松分布**
>
> 令 $n\to\infty$、$p\to0$ 且 $np\to\lambda$。则 $(1-p+pe^t)^n=(1+\tfrac{\lambda}{n}(e^t-1))^n\to e^{\lambda(e^t-1)}$，即泊松的 MGF。所以泊松分布是稀有事件的分布律——许多次试验、极小的成功概率。

<a id="s8"></a>
### 常见连续分布

*连续分布的目录：每一个都是一个密度、一个积分和一个变换。正态分布坐落于这一切的中心。*

| 分布 | PDF $f(x)$ | 均值 | 方差 | MGF $M(t)$ |
| --- | --- | --- | --- | --- |
| 均匀($a,b$) | $\dfrac{1}{b-a}$ on $[a,b]$ | $\dfrac{a+b}{2}$ | $\dfrac{(b-a)^2}{12}$ | $\dfrac{e^{tb}-e^{ta}}{t(b-a)}$ |
| 指数($\lambda$) | $\lambda e^{-\lambda x},\ x\ge0$ | $1/\lambda$ | $1/\lambda^2$ | $\dfrac{\lambda}{\lambda-t},\ t\lt\lambda$ |
| 伽马($\alpha,\lambda$) | $\dfrac{\lambda^\alpha x^{\alpha-1}e^{-\lambda x}}{\Gamma(\alpha)},\ x\ge0$ | $\alpha/\lambda$ | $\alpha/\lambda^2$ | $\big(\tfrac{\lambda}{\lambda-t}\big)^\alpha$ |
| 正态($\mu,\sigma^2$) | $\dfrac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/2\sigma^2}$ | $\mu$ | $\sigma^2$ | $e^{\mu t+\sigma^2 t^2/2}$ |
| 贝塔($\alpha,\beta$) | $\dfrac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)},\ x\in[0,1]$ | $\dfrac{\alpha}{\alpha+\beta}$ | $\dfrac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$ | — |

**演示 — 均匀分布 Uniform$(a,b)$ 的均值与方差**

1. 均值：

   $$E[X]=\int_a^b \frac{x}{b-a}\,dx=\frac{1}{b-a}\cdot\frac{b^2-a^2}{2}=\frac{a+b}{2}.$$
2. 二阶矩：

   $$E[X^2]=\int_a^b\frac{x^2}{b-a}\,dx=\frac{b^3-a^3}{3(b-a)}=\frac{a^2+ab+b^2}{3}.$$
3. 减去均值的平方：

   $$\operatorname{Var}(X)=\frac{a^2+ab+b^2}{3}-\frac{(a+b)^2}{4}=\frac{(b-a)^2}{12}.$$

*离散程度只取决于宽度 $b-a$，正如对称性所要求的那样。*

**演示 — 用积分求指数分布的均值与方差**

1. 分部积分：

   $$E[X]=\int_0^\infty x\,\lambda e^{-\lambda x}\,dx=\Big[-xe^{-\lambda x}\Big]_0^\infty+\int_0^\infty e^{-\lambda x}\,dx=\frac1\lambda.$$
2. 类似地 $E[X^2]=\int_0^\infty x^2\lambda e^{-\lambda x}\,dx=\dfrac{2}{\lambda^2}$。
3. 因此 $\operatorname{Var}(X)=\dfrac{2}{\lambda^2}-\dfrac{1}{\lambda^2}=\dfrac{1}{\lambda^2}$，与第 6 节的 MGF 结果一致。

*指数分布是无记忆的：$P(X\gt s+t\mid X\gt s)=e^{-\lambda t}=P(X\gt t)$。*

**演示 — 正态分布的 MGF 给出均值 $\mu$ 与方差 $\sigma^2$**

1. 对 $Z\sim N(0,1)$，配方：

   $$M_Z(t)=\frac{1}{\sqrt{2\pi}}\int e^{tz-z^2/2}\,dz=e^{t^2/2}\cdot\frac{1}{\sqrt{2\pi}}\int e^{-(z-t)^2/2}\,dz=e^{t^2/2}.$$
2. 对 $X=\mu+\sigma Z$：$M_X(t)=e^{\mu t}M_Z(\sigma t)=e^{\mu t+\sigma^2 t^2/2}$。
3. 于是 $M_X'(0)=\mu$ 且 $M_X''(0)=\mu^2+\sigma^2$，故 $E[X]=\mu$、$\operatorname{Var}(X)=\sigma^2$。

*两个参数 $\mu,\sigma^2$ 字面上就是均值和方差——而标准化 $Z=(X-\mu)/\sigma$ 正是《统计学》指南里的 z 分数。*

> **联系 — 同一族，多副面孔**
>
> 指数分布 = 伽马($1,\lambda$)；$n$ 个 i.i.d. 指数变量之和是伽马($n,\lambda$)（第 13 节）；自由度为 $k$ 的卡方分布是伽马($k/2,1/2$)。贝塔分布支配比例，并且是二项分布的共轭先验——通往贝叶斯推断的桥梁。

<a id="s9"></a>
### 随机变量的函数与变换

*如果你知道 $X$ 的分布律，那么 $Y=g(X)$ 的分布律是什么？两种可靠的方法：CDF 法和雅可比法。*

**换元公式**

$$\text{CDF method: }\ F_Y(y)=P(g(X)\le y),\quad\text{then }f_Y=F_Y'$$

$$\text{Jacobian (monotone }g): \ f_Y(y)=f_X\big(g^{-1}(y)\big)\,\Big|\frac{d}{dy}g^{-1}(y)\Big|$$

*CDF 法总是有效；雅可比公式则是当 $g$ 光滑且一一对应时的捷径。对于多对一的 $g$，要对所有原像求和。*

**演示 — 概率积分变换**

1. 设 $X$ 具有连续、严格递增的 CDF $F$，令 $U=F(X)$。对 $u\in(0,1)$：

   $$F_U(u)=P(F(X)\le u)=P\big(X\le F^{-1}(u)\big)=F\big(F^{-1}(u)\big)=u.$$
2. 所以 $U\sim\text{Uniform}(0,1)$。反过来，$X=F^{-1}(U)$ 具有 CDF $F$。

*这就是计算机模拟任意分布的方法：把一个均匀随机数送入 $F^{-1}$。*

**演示 — 标准正态变量的平方是卡方（雅可比，两支）**

1. 设 $Z\sim N(0,1)$，$Y=Z^2$。对 $y\gt0$，$g(z)=z^2$ 是二对一的，原像为 $\pm\sqrt y$。
2. 用 CDF 法：$F_Y(y)=P(-\sqrt y\le Z\le\sqrt y)=2\Phi(\sqrt y)-1$。
3. 用链式法则求导：

   $$f_Y(y)=2\varphi(\sqrt y)\cdot\frac{1}{2\sqrt y}=\frac{1}{\sqrt{2\pi y}}e^{-y/2},\quad y\gt0.$$

*这就是 $\chi^2_1$ 的密度 = 伽马($\tfrac12,\tfrac12$)——《统计学》指南中卡方检验的基础。*

**演示 — 正态变量的线性变换仍是正态**

1. 设 $X\sim N(\mu,\sigma^2)$，$Y=aX+b$ 且 $a\gt0$。则 $g^{-1}(y)=(y-b)/a$，且 $\big|\tfrac{d}{dy}g^{-1}\big|=1/a$。
2. 代入雅可比公式：

   $$f_Y(y)=\frac{1}{a}\cdot\frac{1}{\sigma\sqrt{2\pi}}\exp\!\Big(-\frac{((y-b)/a-\mu)^2}{2\sigma^2}\Big)=\frac{1}{(a\sigma)\sqrt{2\pi}}\exp\!\Big(-\frac{(y-(a\mu+b))^2}{2a^2\sigma^2}\Big).$$

*所以 $Y\sim N(a\mu+b,\,a^2\sigma^2)$：正态族在仿射映射下封闭——这正是标准化之所以有效的原因。*

## C 部分 · 多个随机变量

<a id="s10"></a>
### 联合分布、边缘分布与条件分布

*两个或更多随机变量共处于一个联合分布律中；边缘分布和条件分布是你对它所取的视角。*

**联合、边缘与条件密度**

$$\text{joint CDF: }\ F(x,y)=P(X\le x,\,Y\le y),\qquad f(x,y)=\frac{\partial^2 F}{\partial x\,\partial y}$$

$$\text{marginal: }\ f_X(x)=\int f(x,y)\,dy,\qquad \text{conditional: }\ f_{Y\mid X}(y\mid x)=\frac{f(x,y)}{f_X(x)}$$

$$X\perp Y \iff f(x,y)=f_X(x)\,f_Y(y)$$

*边缘分布把另一个变量积分掉；条件分布把一个切片重新归一化。独立意味着联合分布可分解为各自的边缘分布之积。*

**演示 — 对单位三角形上的联合均匀分布求边缘**

1. 设 $(X,Y)$ 在 $\{0\lt x\lt y\lt1\}$ 上均匀分布，故在该区域上 $f(x,y)=2$（面积 $=\tfrac12$，密度 $=1/\text{面积}$）。
2. $X$ 的边缘分布：对 $y$ 从 $x$ 到 $1$ 积分：

   $$f_X(x)=\int_x^1 2\,dy=2(1-x),\quad 0\lt x\lt1.$$
3. 给定 $X=x$ 时 $Y$ 的条件分布：即 $Y\mid X=x$ 在 $(x,1)$ 上均匀分布。

   $$f_{Y\mid X}(y\mid x)=\frac{2}{2(1-x)}=\frac{1}{1-x},\quad x\lt y\lt1,$$

*这里 $X$ 与 $Y$ 是相依的：联合分布不可分解。*

> **概念 — 在联合分布律下取期望**
>
> 对任意 $g$，$E[g(X,Y)]=\iint g(x,y)\,f(x,y)\,dx\,dy$。特别地，$E[XY]$ 是对联合密度计算的——而正是这个量度量了两个变量如何一起变动（下一节）。

<a id="s11"></a>
### 协方差、相关与独立性

*协方差度量共同变动；相关把它重新缩放为一个落在 $[-1,1]$ 内的无量纲数。*

**协方差、相关与和的方差**

$$\operatorname{Cov}(X,Y)=E[XY]-E[X]E[Y],\qquad \rho=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}$$

$$\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y)$$

$$\operatorname{Cov}(aX+b,\,cY+d)=ac\,\operatorname{Cov}(X,Y)$$

*$\rho\in[-1,1]$ 是两个变量 z 分数乘积的平均。独立 $\Rightarrow$ $\operatorname{Cov}=0$，但反之不然。*

**演示 — 独立蕴含零协方差（以及为何反之不成立）**

1. 若 $X\perp Y$，联合分布可分解，于是 $E[XY]=\iint xy\,f_X(x)f_Y(y)\,dx\,dy=E[X]E[Y]$。
2. 因此 $\operatorname{Cov}(X,Y)=E[XY]-E[X]E[Y]=0$。
3. 逆命题不成立：令 $X\sim N(0,1)$ 且 $Y=X^2$。则 $E[XY]=E[X^3]=0=E[X]E[Y]$，故 $\operatorname{Cov}=0$，然而 $Y$ 是 $X$ 的确定性函数——最大程度地相依。

*协方差只看到*线性*关联；零协方差并不等于独立。*

**演示 — 由柯西-施瓦茨不等式得 $|\rho|\le1$**

1. 随机变量的柯西-施瓦茨不等式：$\big(E[UV]\big)^2\le E[U^2]\,E[V^2]$。
2. 把它应用于中心化变量 $U=X-\mu_X,\ V=Y-\mu_Y$：

   $$\operatorname{Cov}(X,Y)^2\le \operatorname{Var}(X)\,\operatorname{Var}(Y).$$
3. 除以 $\sigma_X^2\sigma_Y^2$：当且仅当 $Y$ 是 $X$ 的精确线性函数时取等号。

   $$\rho^2\le1\ \Rightarrow\ -1\le\rho\le1,$$

*相关之所以有界，恰恰是因为柯西-施瓦茨用范数界住了内积。*

> **联系 — 通往《统计学》指南中的回归**
>
> 最小二乘斜率是 $b_1=\rho\,\sigma_Y/\sigma_X$，且 $R^2=\rho^2$。由数据计算出的相关系数，正是这里由联合分布定义的 $\rho$ 的样本版本。

<a id="s12"></a>
### 条件期望与塔性质

*条件期望是在已知另一个变量时对一个变量的最佳预测——而它求平均后会回到无条件均值。*

**条件期望及其各定律**

$$E[X\mid Y=y]=\int x\,f_{X\mid Y}(x\mid y)\,dx,\qquad E[X\mid Y]=g(Y)\ \text{is a random variable}$$

$$\text{tower: }\ E\big[E[X\mid Y]\big]=E[X]$$

$$\text{law of total variance: }\ \operatorname{Var}(X)=E\big[\operatorname{Var}(X\mid Y)\big]+\operatorname{Var}\big(E[X\mid Y]\big)$$

*$E[X\mid Y]$ 是在均方意义下最佳预测 $X$ 的那个关于 $Y$ 的函数。它本身是随机的，因为 $Y$ 是随机的。*

**演示 — 塔性质 $E[E[X\mid Y]]=E[X]$**

1. 按定义，内层期望为 $E[X\mid Y=y]=\int x\,f_{X\mid Y}(x\mid y)\,dx$。
2. 对 $Y$ 的分布求平均：

   $$E\big[E[X\mid Y]\big]=\int\!\Big(\int x\,f_{X\mid Y}(x\mid y)\,dx\Big)f_Y(y)\,dy.$$
3. 利用 $f_{X\mid Y}(x\mid y)\,f_Y(y)=f(x,y)$ 并交换积分次序：

   $$=\int x\Big(\int f(x,y)\,dy\Big)dx=\int x\,f_X(x)\,dx=E[X].$$

*"对各条件平均再加权求平均，权重取条件变量"——你便恢复了总平均。*

**演示 — 由塔性质得全方差**

1. 令 $m(Y)=E[X\mid Y]$。写 $\operatorname{Var}(X\mid Y)=E[X^2\mid Y]-m(Y)^2$。
2. 取期望：由塔性质作用于 $E[X^2\mid Y]$，得 $E[\operatorname{Var}(X\mid Y)]=E[X^2]-E[m(Y)^2]$。
3. 加上 $\operatorname{Var}(m(Y))=E[m(Y)^2]-(E[X])^2$；$E[m(Y)^2]$ 抵消，剩下

   $$E[\operatorname{Var}(X\mid Y)]+\operatorname{Var}(E[X\mid Y])=E[X^2]-(E[X])^2=\operatorname{Var}(X).$$

*方差分裂为"组内"加"组间"——正是方差分析背后的那个分解。*

> **联系 — 鞅（第 18 节）**
>
> 给定一个 $\sigma$-代数的条件期望是这一想法的抽象版本，而鞅是这样一个过程：在已知过去时，对未来的条件期望等于现在。塔性质正是那整套理论的引擎。

<a id="s13"></a>
### 随机变量之和与卷积

*独立变量之和的密度是它们各自密度的卷积——而变换把那个卷积变成乘积。*

**卷积公式**

$$Z=X+Y,\ X\perp Y:\quad f_Z(z)=\int_{-\infty}^{\infty} f_X(x)\,f_Y(z-x)\,dx$$

$$\text{discrete: }\ p_Z(z)=\sum_{x}p_X(x)\,p_Y(z-x),\qquad M_Z(t)=M_X(t)\,M_Y(t)$$

*把独立变量相加 $\leftrightarrow$ 把密度做卷积 $\leftrightarrow$ 把变换相乘。最后一种通常是最省事的途径。*

**演示 — 两个独立 Uniform$(0,1)$ 之和是三角形分布**

1. 当 $f_X=f_Y=1$（在 $[0,1]$ 上）时，卷积为 $f_Z(z)=\int_0^1 \mathbf 1\{0\le z-x\le1\}\,dx$，即重叠部分的长度。
2. 对 $0\le z\le1$：$x$ 取遍 $[0,z]$，故 $f_Z(z)=z$。
3. 对 $1\le z\le2$：$x$ 取遍 $[z-1,1]$，故 $f_Z(z)=2-z$。合在一起：

   $$f_Z(z)=\begin{cases}z,&0\le z\le1\\ 2-z,&1\le z\le2\end{cases}$$

*平坦的均匀分布卷积成一个三角形——朝着 CLT 的钟形曲线迈出的第一个可见步骤。*

**演示 — $n$ 个 i.i.d. 指数变量之和是伽马（用 MGF）**

1. 每个 $X_i\sim\text{Exp}(\lambda)$ 的 MGF 是 $M_{X_i}(t)=\dfrac{\lambda}{\lambda-t}$。
2. 对和 $S_n=X_1+\cdots+X_n$，各 MGF 相乘：

   $$M_{S_n}(t)=\Big(\frac{\lambda}{\lambda-t}\Big)^n.$$
3. 这恰好是第 8 节中伽马$(n,\lambda)$ 的 MGF，故由唯一性

   $$S_n\sim\text{Gamma}(n,\lambda),\qquad f_{S_n}(s)=\frac{\lambda^n s^{n-1}e^{-\lambda s}}{(n-1)!}.$$

*$n$ 次泊松到达的等待时间加起来是一个伽马分布——而 MGF 把它变成了一行式的证明。*

> **联系 — 和是极限定理的核心**
>
> 样本均值 $\bar X_n=\tfrac1n\sum X_i$ 是一个被缩放的和。理解和——它们的均值、方差和极限形状——正是 D 部分的纲领。

## D 部分 · 极限定理

<a id="s14"></a>
### 概率不等式（马尔可夫、切比雪夫、詹森、柯西-施瓦茨）

*不等式几乎不需要任何假设就能界住尾部概率和期望——是每一个收敛性证明的脚手架。*

**四个常用主力不等式**

$$\text{Markov: }\ P(X\ge a)\le\frac{E[X]}{a}\quad(X\ge0,\ a\gt0)$$

$$\text{Chebyshev: }\ P\big(|X-\mu|\ge k\big)\le\frac{\sigma^2}{k^2}$$

$$\text{Jensen: }\ \varphi\text{ convex}\Rightarrow \varphi(E[X])\le E[\varphi(X)]$$

$$\text{Cauchy–Schwarz: }\ \big(E[XY]\big)^2\le E[X^2]\,E[Y^2]$$

**演示 — 先马尔可夫，再把切比雪夫作为推论**

1. 对 $X\ge0$、$a\gt0$，用指示函数界 $a\,\mathbf 1\{X\ge a\}\le X$。取期望：

   $$a\,P(X\ge a)\le E[X]\ \Rightarrow\ P(X\ge a)\le\frac{E[X]}{a}.$$
2. 把马尔可夫应用于非负变量 $(X-\mu)^2$，水平取 $k^2$：

   $$P\big((X-\mu)^2\ge k^2\big)\le\frac{E[(X-\mu)^2]}{k^2}=\frac{\sigma^2}{k^2}.$$
3. 事件 $(X-\mu)^2\ge k^2$ 与 $|X-\mu|\ge k$ 相同，便得到切比雪夫不等式。

*切比雪夫不过是把马尔可夫应用于平方偏差——给弱大数定律提供动力的那个界。*

**演示 — 由支撑线证明詹森不等式**

1. 凸函数 $\varphi$ 位于其每一条切线（支撑线）之上。在点 $\mu=E[X]$ 处：$\varphi(x)\ge\varphi(\mu)+c\,(x-\mu)$，其中斜率为 $c$。
2. 对两边取期望：

   $$E[\varphi(X)]\ge\varphi(\mu)+c\,(E[X]-\mu)=\varphi(\mu)=\varphi(E[X]).$$

*于是 $E[X^2]\ge(E[X])^2$（故方差 $\ge0$），且对正的 $X$ 有 $E[1/X]\ge1/E[X]$——两者都是特例。*

<a id="s15"></a>
### 收敛的各种模式

*"一列随机变量收敛"可以有几种不同的含义。它们之间的层级关系组织起各个极限定理。*

**四种收敛模式**

$$\text{a.s.: }\ P\big(X_n\to X\big)=1$$

$$\text{in prob.: }\ \forall\varepsilon\gt0,\ P\big(|X_n-X|\ge\varepsilon\big)\to0$$

$$\text{in }L^p:\ E\big[|X_n-X|^p\big]\to0$$

$$\text{in distribution: }\ F_{X_n}(x)\to F_X(x)\ \text{at continuity points of }F_X$$

> **原理 — 层级关系**
>
> 几乎处处收敛和 $L^p$ 收敛都各自蕴含**依概率**收敛，而依概率收敛又蕴含**依分布**收敛。反向的箭头一般不成立。依分布收敛是最弱的——它只关乎分布律，而不关乎变量本身——并且它正是 CLT 所用的那种模式。

**演示 — $L^2$ 收敛蕴含依概率收敛**

1. 设 $E[(X_n-X)^2]\to0$。把马尔可夫应用于非负的 $(X_n-X)^2$，水平取 $\varepsilon^2$：

   $$P\big(|X_n-X|\ge\varepsilon\big)=P\big((X_n-X)^2\ge\varepsilon^2\big)\le\frac{E[(X_n-X)^2]}{\varepsilon^2}.$$
2. 对每个固定的 $\varepsilon\gt0$，右边 $\to0$，这就是依概率收敛。

*这个基于马尔可夫的步骤，正是下一节中证明弱大数定律的方法。*

**连续性定理（CLT 的工具）**

$$\varphi_{X_n}(t)\to\varphi_X(t)\ \forall t\ \iff\ X_n\xrightarrow{d}X$$

*列维连续性定理：特征函数的收敛等价于依分布收敛。这就是证明 CLT 的杠杆。*

<a id="s16"></a>
### 大数定律

*许多独立试验的平均收敛到真实的均值。这正是为概率的频率派解释提供依据的定理。*

**弱大数定律与强大数定律**

$$\text{WLLN: }\ \bar X_n\xrightarrow{P}\mu\quad\text{(convergence in probability)}$$

$$\text{SLLN: }\ \bar X_n\xrightarrow{a.s.}\mu\quad\text{(almost-sure convergence)}$$

*两者都要求 $X_i$ 为 i.i.d. 且均值 $\mu$ 有限（这里的 WLLN 还用到方差有限）。强大数定律是更深刻的陈述。*

**演示 — 用切比雪夫证明弱大数定律**

1. 设 $X_1,\dots,X_n$ 为 i.i.d.，均值 $\mu$、方差 $\sigma^2$。则 $E[\bar X_n]=\mu$。
2. 平均的方差缩小：

   $$\operatorname{Var}(\bar X_n)=\frac{1}{n^2}\sum_{i=1}^n\operatorname{Var}(X_i)=\frac{\sigma^2}{n}.$$
3. 把切比雪夫应用于 $\bar X_n$：

   $$P\big(|\bar X_n-\mu|\ge\varepsilon\big)\le\frac{\operatorname{Var}(\bar X_n)}{\varepsilon^2}=\frac{\sigma^2}{n\varepsilon^2}\xrightarrow[n\to\infty]{}0.$$

*随着 $n$ 增大，平均集中到 $\mu$ 上——这就是依概率收敛，即弱大数定律。*

> **联系 — 为什么标准误中有一个 $\sqrt n$**
>
> 同一个计算 $\operatorname{Var}(\bar X_n)=\sigma^2/n$ 给出《统计学》指南中的标准误 $\sigma/\sqrt n$。大数定律说估计会收敛；CLT（下一节）说*以多快的速度*以及*以何种形状*收敛。

<a id="s17"></a>
### 中心极限定理

*不只是平均收敛到均值——经过适当缩放后，它的涨落会变成正态，无论原始分布如何。*

**中心极限定理**

$$\frac{\bar X_n-\mu}{\sigma/\sqrt n}\ \xrightarrow{d}\ N(0,1)\qquad\Longleftrightarrow\qquad \sum_{i=1}^n X_i\ \approx\ N\big(n\mu,\ n\sigma^2\big)$$

*对于均值 $\mu$、方差 $\sigma^2$ 有限的 i.i.d. $X_i$，标准化后的和依分布收敛到标准正态——无论原始分布的形状如何。*

**演示 — 用 MGF / 特征函数证明 CLT**

1. 把每一项标准化：$Y_i=(X_i-\mu)/\sigma$，故 $E[Y_i]=0,\ \operatorname{Var}(Y_i)=1$。被缩放的和是 $S_n=\tfrac{1}{\sqrt n}\sum_{i=1}^n Y_i$。
2. 独立性使 MGF 相乘：$M_{S_n}(t)=\big[M_Y\!\big(t/\sqrt n\big)\big]^n$。
3. 利用 $M_Y(0)=1,\ M_Y'(0)=0,\ M_Y''(0)=1$，把 $M_Y$ 在 0 处泰勒展开：

   $$M_Y\!\Big(\frac{t}{\sqrt n}\Big)=1+\frac{t^2}{2n}+o\!\Big(\frac1n\Big).$$
4. 取 $n$ 次幂并求极限：

   $$M_{S_n}(t)=\Big(1+\frac{t^2/2}{n}+o\big(\tfrac1n\big)\Big)^n\ \longrightarrow\ e^{t^2/2}.$$
5. 而 $e^{t^2/2}$ 正是 $N(0,1)$ 的 MGF；由连续性定理，$S_n\xrightarrow{d}N(0,1)$。

*$\sqrt n$ 的缩放恰好使方差保持为 1，同时让高阶项消失——钟形曲线是被归一化的和的普适吸引子。*

> **联系 — 一切推断的脊梁**
>
> 密度 = 面积 → z 分数进行标准化 → CLT 使 $\bar X$ 趋于正态 → 于是《统计学》指南中的置信区间和 z/t 检验都是关于钟形曲线下面积的陈述。正是这条定理使得基于正态的推断能够作用于偏斜的、真实的数据。

<a id="s18"></a>
### 向更远处一瞥：测度论概率与鞅

*严格的故事接下来通向何处——测度论基础，以及随时间公平演化的过程的动态理论。*

> **概念 — 作为测度论的概率**
>
> 在完全严格的框架里，$P$ 被视作 $\sigma$-代数 $\mathcal F$ 上的一个**测度**，而期望被视作**勒贝格积分** $E[X]=\int_\Omega X\,dP$。这把离散求和与连续积分统一成一种运算，并让我们能处理那些既非离散也非连续的变量——混合型、给定一个 $\sigma$-代数的条件期望，以及初等理论无法触及的极限。

**严格理论的支柱**

***单调收敛与控制收敛**为交换极限与期望提供依据。**富比尼-托内利**为我们在塔性质和尾部求和证明中所用的交换积分次序提供依据。**拉东-尼科迪姆**在完全的一般性下定义密度和条件期望。这些定理使本指南中每一步"交换次序"都合法。*

**鞅**

$$E\big[X_{n+1}\mid X_1,\dots,X_n\big]=X_n\quad(\text{martingale})$$

*鞅是一个公平博弈的模型：在已知今天的全部信息时，对明天值的最佳预报就是今天的值。它直接建立在第 12 节的条件期望之上。*

> **原理 — 鞅为何重要**
>
> **可选停止定理**说鞅的期望不会被一个公平的停止规则改变（没有任何赌博系统能赢过一场公平博弈），而**鞅收敛定理**保证有界的鞅会稳定到一个极限。这些工具把大数定律推广到相依的序列，并支撑起随机微积分、布朗运动以及金融数学。

> **联系 — 前行的道路**
>
> 从这里道路分岔：**随机过程**（马尔可夫链、泊松过程、布朗运动）、**统计推断**（配套指南，在那里这些分布成为估计量和检验），以及**信息论**（熵作为期望的意外程度）。它们全都立足于本指南所建立的基础：一个测度、随机变量、它们的矩，以及在整体上驯服随机性的极限定理。

---

*一门严格的概率论入门课程——公理、随机变量、变换，以及支撑统计推断的极限定理——作为《完整统计学指南》的姊妹篇而构建。先通读一遍把握其结构；之后随时回到任何一个方框作为参考。记住：概率运行的方向是总体 → 样本；统计学则把它反转过来。*
