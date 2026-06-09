[English](index-theory.md) · **中文**

# 指标理论与 Atiyah–Singer 定理，*用拓扑学计数解.*

*这是对数学中最深刻的桥梁之一的一份自洽而严格的引论：一个分析量——某个微分方程解的个数减去求解它的障碍个数——必然等于一个拓扑量，而后者可以通过对特征类积分来计算。我们从 Fredholm 算子及其指标这一最朴素的概念出发，经由椭圆性与 Hodge 理论建立到 Dirac 算子，最终抵达 Atiyah–Singer 指标定理，并将 Gauss–Bonnet 定理、符号差定理与 Riemann–Roch 定理作为特例加以恢复，最后以热核证明的概要以及反常的物理学收束全篇。几何与分析是目标，物理是动机；每一个符号都有定义，每一个在本层次上能证明的论断都给出证明。*

[← 返回全部指南](../README.zh.md)

**预备知识。** 本指南依托三份姊妹指南，并在每一处用到时重述相应事实。从**微分拓扑与特征类**指南（[`differential-topology.md`](../topology/differential-topology.md)）我们借用 de Rham 上同调、Euler 示性数、特征类（Chern 类 $c_k$、Pontryagin 类 $p_k$、Euler 类 $e$）、用曲率表示这些类的 Chern–Weil 构造，以及 Gauss–Bonnet–Chern 定理。从**泛函分析与 Hilbert 空间**指南（[`functional-analysis.md`](../functional-analysis/functional-analysis.md)）我们借用 Banach 与 Hilbert 空间、有界算子与紧算子、伴随算子，以及闭值域定理。从**微分几何与张量**指南（[`differential-geometry.md`](differential-geometry.md)）我们借用光滑流形、切丛与余切丛、向量丛、微分形式、外微分 $d$、楔积 $\wedge$、Riemann 度量，以及联络及其曲率。除单变量微积分之外，不假定读者对偏微分方程有任何先备知识；所需的分析事实都会被精确陈述并加以说明。

## 第 A 部分 · 分析的一面——算子及其指标

<a id="s0"></a>
### 动机——分析数据等于拓扑数据

本指南的唯一思想可凝练为一句口号：**一个自然微分算子的核与余核携带一个整数，它在你形变几何时无法移动，而这个整数仅凭拓扑就可以算出。**

#### 我们要解决什么问题？

设你有一个线性方程 $Du = f$，其中 $D$ 是某个线性算子（设想成像 Laplace 算子那样的微分算子），作用在函数或向量丛的截面上。两个基本问题随之而来：

1. **唯一性。** 齐次方程 $Du = 0$ 有多少个独立解？这些解构成 $D$ 的**核**，记作 $\ker D = \{u : Du = 0\}$。其维数 $\dim\ker D$ 衡量唯一性失败的严重程度。
2. **可解性。** 对哪些右端项 $f$，$Du = f$ 可解？障碍位于**余核** $\mathrm{coker} D = (\text{目标空间})/(\mathrm{im} D)$ 之中，其中 $\mathrm{im} D = \{Du\}$ 是值域。其维数 $\dim\mathrm{coker} D$ 计数 $f$ 必须满足的约束个数。

这两个数都很脆弱：$D$ 的微小改变就能创造或消灭一个解，从而升高或降低 $\dim\ker D$。但它们的**差**

$$
\mathrm{ind} D \;=\; \dim\ker D \;-\; \dim\mathrm{coker} D
$$

却是刚性的。这个差就是**分析指标**。这个奇迹由 Michael Atiyah 与 Isadore Singer 于 1963 年发现：对于紧流形上的*椭圆*算子（我们将在 s2 中精确化这一类），$\mathrm{ind} D$ 等于一个你可以从流形及所涉及的丛的拓扑读出的数——**拓扑指标**——完全不需要援引算子系数的任何细节。

#### 为什么这既令人惊讶又有用

考虑与有限维线性代数的类比。若 $A: \mathbb{R}^n \to \mathbb{R}^m$ 是一个矩阵，秩—零化度定理给出 $\dim\ker A = n - \mathrm{rank} A$ 与 $\dim\mathrm{coker} A = m - \mathrm{rank} A$，于是

$$
\dim\ker A - \dim\mathrm{coker} A = (n - \mathrm{rank} A) - (m - \mathrm{rank} A) = n - m.
$$

矩阵的指标就是 $n - m$：它只依赖于源空间与目标空间的*形状*，绝不依赖于矩阵的元素。指标理论正是这一事实的无穷维后裔。在无穷维中没有固定的“$n-m$”，但对于恰当的算子仍有一个替代物幸存下来，而这个替代物是*拓扑的*。

回报极其丰厚。计数几何偏微分方程的解（调和形式、全纯截面、调和旋量）是困难的分析；计算特征数则是有限的拓扑。指标定理把前者换成后者。它把 Gauss–Bonnet 定理（由曲率给出 Euler 示性数）、Hirzebruch 符号差定理以及代数几何的 Riemann–Roch 定理统一为一个陈述，并解释了量子场论中的反常。

> **直觉。** 把指标想成一个“受拓扑保护”的计数，就像一条闭环绕某个洞缠绕的次数：你可以摆动这条环，但缠绕数只在你撕裂它时才会跳变。摆动 $D$ 会移动 $\ker$ 与 $\mathrm{coker}$，但解只能*成对地*出现或消失，从而使差保持不变。

整体计划：Fredholm 算子与指标的稳定性（s1）；微分算子、符号、椭圆性（s2）；椭圆正则性与有限性（s3）；de Rham 复形与作为指标的 Euler 示性数（s4）；Hodge 定理（s5）；Clifford 代数与 Dirac 算子（s6）；拓扑指标的各项成分——Chern 特征标、Todd 类、$\hat A$-亏格（s7）；指标定理本身（s8）；其著名特例（s9）；热核证明的概要（s10）；以及反常的物理（s11）。

<a id="s1"></a>
### Fredholm 算子与分析指标；在扰动下的稳定性

我们将精确刻画*拥有*良定整数指标的那一类算子，并证明指标在微小扰动或紧扰动下不会改变。这一稳定性是整个理论的发动机。

#### 定义与基本对象

> **定义——Fredholm 算子。**
>
> 设 $H_1, H_2$ 为 Hilbert 空间（完备的内积空间；见泛函分析指南）。一个有界线性算子 $T: H_1 \to H_2$ 称为 **Fredholm 算子**，如果
> - $\ker T = \{x \in H_1 : Tx = 0\}$ 是有限维的；
> - 值域 $\mathrm{im} T = \{Tx : x \in H_1\}$ 在 $H_2$ 中是闭的；
> - $\mathrm{coker} T = H_2 / \mathrm{im} T$ 是有限维的。
>
> 其**（分析）指标**是整数
> $$
> \mathrm{ind} T = \dim\ker T - \dim\mathrm{coker} T.
> $$

这里“有界”意味着存在常数 $C$ 使得对一切 $x$ 有 $\|Tx\| \le C\|x\|$，这等价于 $T$ 连续。商空间 $H_2/\mathrm{im} T$ 是等价类 $[y]$ 之集合，其中 $y \sim y'$ 当且仅当 $y - y' \in \mathrm{im} T$；其维数衡量 $T$ 距离满射有多远。

一个简洁的重新表述用到**伴随算子** $T^*: H_2 \to H_1$，它由 $\langle Tx, y\rangle = \langle x, T^* y\rangle$ 对一切 $x,y$ 定义。当 $\mathrm{im} T$ 闭时，闭值域定理（泛函分析指南）给出正交分解 $H_2 = \mathrm{im} T \oplus (\mathrm{im} T)^\perp$ 以及恒等式 $(\mathrm{im} T)^\perp = \ker T^*$。于是 $\mathrm{coker} T \cong \ker T^*$ 作为向量空间成立，并且

$$
\mathrm{ind} T = \dim\ker T - \dim\ker T^*.
$$

这是我们将不断使用的形式：指标是 $Tx = 0$ 的解的个数与 $T^* y = 0$ 的解的个数之差。

> **典型例（一个移位算子）。** 取 $H_1 = H_2 = \ell^2$，即平方可和序列 $x = (x_0, x_1, x_2, \dots)$（满足 $\sum |x_n|^2 < \infty$）的空间。定义**右移位** $S(x_0, x_1, \dots) = (0, x_0, x_1, \dots)$。
> - $\ker S = 0$：若 $Sx = 0$ 则每个 $x_n = 0$。故 $\dim\ker S = 0$。
> - $\mathrm{im} S = \{y : y_0 = 0\}$，它是闭的，而 $\mathrm{coker} S$ 是一维的（由 $(1,0,0,\dots)$ 的类张成）。故 $\dim\mathrm{coker} S = 1$。
> - 因此 $\mathrm{ind} S = 0 - 1 = -1$。
>
> 左移位 $S^*(x_0, x_1, \dots) = (x_1, x_2, \dots)$ 是其伴随算子，满足 $\ker S^* = \mathrm{span}\{(1,0,0,\dots)\}$，$\dim = 1$，从而验证 $\mathrm{ind} S = \dim\ker S - \dim\ker S^* = 0 - 1 = -1$。幂 $S^k$ 的指标为 $-k$：指标遍历整个 $\mathbb Z$，故这个整数确实携带信息。

#### 稳定性定理及其证明

> **定理（指标的稳定性）。** 设 $T: H_1 \to H_2$ 为 Fredholm 算子。
> (a) 若 $K: H_1 \to H_2$ 是**紧的**（把有界集映为闭包紧的集），则 $T + K$ 是 Fredholm 算子且 $\mathrm{ind}(T+K) = \mathrm{ind} T$。
> (b) 存在 $\varepsilon > 0$，使得每个满足 $\|B\| < \varepsilon$ 的有界算子 $B$ 都使 $T+B$ 为 Fredholm 算子且 $\mathrm{ind}(T+B) = \mathrm{ind} T$。

我们证明两个论断的核心：指标是不变的。我们用到一个结构性事实，即 **Atkinson 定理**，先建立它。

> **Atkinson 定理。** $T$ 是 Fredholm 算子当且仅当它**模紧算子可逆**：存在有界算子 $P$（一个*拟逆*）使得 $PT - I = K_1$ 且 $TP - I = K_2$，其中 $K_1, K_2$ 为紧算子。

**Atkinson 定理之证明（⇒）。**
1. 设 $T$ 为 Fredholm 算子。由定义 $\ker T$ 有限维且 $\mathrm{im} T$ 闭并有有限维补。把 $T$ 限制到 $(\ker T)^\perp$；限制 $T_0: (\ker T)^\perp \to \mathrm{im} T$ 是 Hilbert 空间之间的有界双射（因去掉核后单射，到值域上满射）。*理由：* 去掉核使 $T$ 单射，其值域不变。
2. 由有界逆定理（开映射定理在完备空间下的推论，泛函分析指南），$T_0^{-1}: \mathrm{im} T \to (\ker T)^\perp$ 有界。
3. 定义 $P: H_2 \to H_1$ 为 $P = T_0^{-1} \circ \Pi$，其中 $\Pi: H_2 \to \mathrm{im} T$ 是正交投影。则 $P$ 有界（有界映射的复合）。
4. 计算 $TP - I$。在 $\mathrm{im} T$ 上，$TP = T T_0^{-1} = I$；在 $(\mathrm{im} T)^\perp$ 上，$\Pi = 0$ 故 $TP = 0$。于是 $TP - I = -(I - \Pi)$，即到 $(\mathrm{im} T)^\perp$ 上投影的相反数，它是有限秩的（因 $\mathrm{coker} T$ 有限维），从而是紧的。*理由：* 有限秩算子是紧的。
5. 类似地 $PT - I = -(\text{到 } \ker T \text{ 上的投影})$，有限秩，从而紧。这完成了（⇒）。$\qquad\blacksquare$

**稳定性 (a) 之证明，指标不变性。** 我们用 Atkinson 定理与一个无行列式的计数论证。
1. 设 $T$ 为 Fredholm 算子，拟逆为 $P$，故 $PT = I + K_1$，$TP = I + K_2$，其中 $K_i$ 紧。对紧算子 $K$，算子 $T+K$ 满足 $P(T+K) = I + K_1 + PK$ 与 $(T+K)P = I + K_2 + KP$；由于 $PK$ 与 $KP$ 紧（紧算子与有界算子复合为紧），$T+K$ 也以 $P$ 为拟逆，故由 Atkinson 定理（⇐，它来自 Riesz 理论：$I + \text{紧}$ 是指标为 $0$ 的 Fredholm 算子）知 $T+K$ 为 Fredholm 算子。*理由：* 拟逆条件正是 Fredholm 性之所是。
2. 为看出指标不变，考虑路径 $T_t = T + tK$，$t \in [0,1]$。由第 1 步每个 $T_t$ 都是 Fredholm 算子。我们证明 $t \mapsto \mathrm{ind} T_t$ 是局部常值的；它取整数值且（下面将证）连续，故在 $[0,1]$ 上为常值。

**稳定性 (b) 之证明，局部常值性。** 这是关键引理；(a) 的常值性随之而来。我们用关于指标的两个标准事实，二者都可由泛函分析指南中的定义证得：指标在**复合下可加**，对 Fredholm 算子 $A,B$ 有 $\mathrm{ind}(AB)=\mathrm{ind} A+\mathrm{ind} B$；指标在**可逆算子及 $I+(\text{紧})$ 上为零**（后者即 Riesz 理论：$I+\text{紧}$ 是指标为 $0$ 的 Fredholm 算子）。
1. 固定 Fredholm 算子 $T$ 及其拟逆 $P$（Atkinson 定理），故 $PT=I+K_1$，$K_1$ 紧。对 $PT$ 用可加性得 $\mathrm{ind} P+\mathrm{ind} T=\mathrm{ind}(I+K_1)=0$，故 $\mathrm{ind} P=-\mathrm{ind} T$。*理由：* 可加性与 $I+\text{紧}$ 的指标。
2. 取任意有界 $B$，满足 $\|B\|<\varepsilon:=1/\|P\|$（若 $P=0$ 则 $T$ 本身可逆，结论平凡）。于是 $\|PB\|\le\|P\|\,\|B\|<1$，故由 Neumann 级数 $\sum(-PB)^k$ 知 $I+PB$ 可逆。*理由：* 恒等算子的范数 $<1$ 扰动可逆。
3. 计算 $P(T+B)=PT+PB=I+K_1+PB=(I+PB)+K_1$。把可逆部分提出：
$$
P(T+B)=(I+PB)\big(I+(I+PB)^{-1}K_1\big).
$$
此处 $(I+PB)^{-1}K_1$ 紧（有界 $\circ$ 紧），故右因子为 $I+(\text{紧})$，指标为 $0$，而左因子可逆，指标为 $0$。由可加性 $\mathrm{ind}\big(P(T+B)\big)=0$。特别地 $T+B$ 为 Fredholm 算子（其拟逆为 $(\text{右因子})^{-1}\!\!\mod\text{紧}\cdot(I+PB)^{-1}P$）。*理由：* 可加性与可逆算子、$I+\text{紧}$ 的指标。
4. 对乘积 $P(T+B)$ 再次用可加性：$\mathrm{ind} P+\mathrm{ind}(T+B)=\mathrm{ind}\big(P(T+B)\big)=0$，故由第 1 步 $\mathrm{ind}(T+B)=-\mathrm{ind} P=\mathrm{ind} T$。这对一切 $\|B\|<\varepsilon$ 成立，正是局部常值性。$\qquad\blacksquare$

对 (a)，沿路径 $T_t = T + tK$ 应用 (b)：用有限多个区间覆盖 $[0,1]$，在每个区间上指标常值，故 $\mathrm{ind} T_0 = \mathrm{ind} T_1$，即 $\mathrm{ind}(T) = \mathrm{ind}(T+K)$。

> **这为何重要。** 稳定性正是*为什么*指标是拓扑的原因。两个能通过椭圆算子相互形变（或仅相差低阶、从而“类紧”项）的椭圆算子具有相同的指标。所以指标只依赖于一个离散的形变类——这恰是拓扑所度量的那类数据。陷阱：*单个*维数 $\dim\ker T$ 与 $\dim\mathrm{coker} T$ **不**稳定；只有差稳定。绝不要指望从拓扑算出 $\dim\ker$。

<a id="s2"></a>
### 微分算子、它们的主符号，以及椭圆性

s1 的 Fredholm 理论生活在 Hilbert 空间上。为把它应用于几何，我们需要由微分构造出的算子，以及决定 Fredholm 性的关键不变量：**主符号**。

#### 丛上的微分算子

> **定义——微分算子。** 设 $E, F \to M$ 是光滑流形 $M$ 上的光滑复向量丛（一个丛为每个点 $x$ 指定一个向量空间 $E_x$，随之光滑变化；截面是光滑的选取 $s(x)\in E_x$）。记 $\Gamma(E)$ 为光滑截面。一个**阶 $\le m$ 的线性微分算子**是线性映射 $D: \Gamma(E) \to \Gamma(F)$，它在任意局部坐标卡 $(x^1,\dots,x^n)$ 与局部平凡化下形如
> $$
> D = \sum_{|\alpha| \le m} A_\alpha(x)\, \partial^\alpha,
> $$
> 其中 $\alpha = (\alpha_1,\dots,\alpha_n)$ 是多重指标，$|\alpha| = \alpha_1 + \cdots + \alpha_n$，$\partial^\alpha = \partial_{x^1}^{\alpha_1}\cdots\partial_{x^n}^{\alpha_n}$，每个 $A_\alpha(x)$ 是矩阵值的光滑函数（线性映射 $E_x \to F_x$）。若某个 $|\alpha| = m$ 的 $A_\alpha$ 非零，则阶为 $m$。

例子：梯度、散度、外微分 $d$，以及 Laplace 算子 $\Delta = -\sum_i \partial_{x^i}^2$（$2$ 阶）。

#### 主符号

控制 Fredholm 性的 $D$ 之行为是它的**最高阶部分**，以几何方式打包。

> **定义——主符号。** 对余向量 $\xi \in T_x^* M$（切空间上的线性泛函；坐标中 $\xi = \sum_i \xi_i\, dx^i$），$m$ 阶算子 $D = \sum_{|\alpha|\le m} A_\alpha \partial^\alpha$ 的**主符号**是线性映射 $\sigma_m(D)(x,\xi): E_x \to F_x$，它由仅保留最高阶项并以 $\partial_{x^i} \mapsto i\,\xi_i$ 替换而定义：
> $$
> \sigma_m(D)(x,\xi) = i^m \sum_{|\alpha| = m} A_\alpha(x)\, \xi^\alpha,
> \qquad \xi^\alpha := \xi_1^{\alpha_1}\cdots\xi_n^{\alpha_n}.
> $$

因子 $i = \sqrt{-1}$ 来自 Fourier 变换：$\partial_{x^i}$ 作用在 $e^{i\langle x,\xi\rangle}$ 上产生 $i\xi_i\, e^{i\langle x,\xi\rangle}$。符号记录了 $D$ 如何作用于频率为 $\xi$ 的快速振荡波；高频行为完全由最高阶系数支配。一个真正不依赖坐标的陈述成立：$\sigma_m(D)$ 是余切丛 $T^*M$ 上良定的丛映射 $\pi^* E \to \pi^* F$（其中 $\pi: T^*M \to M$），且关于 $\xi$ 是 $m$ 次齐次的。

> **典型例（Laplace 算子的符号）。** 对作用在函数上的 $\Delta = -\sum_i \partial_{x^i}^2$（$E=F=$ 平凡线丛），最高阶项即 $\Delta$ 全体，其中 $\alpha = 2e_i$ 时 $A_\alpha = -1$，否则为 $0$。于是
> $$
> \sigma_2(\Delta)(x,\xi) = i^2 \sum_i (-1)\,\xi_i^2 = (-1)\cdot(-1)\sum_i \xi_i^2 = |\xi|^2.
> $$
> 对 $\xi \ne 0$ 这是一个非零数（一个可逆的 $1\times 1$“矩阵”）。这种非退化性恰恰是*椭圆性*。

#### 椭圆性

> **定义——椭圆算子。** $m$ 阶算子 $D: \Gamma(E)\to\Gamma(F)$ 称为**椭圆的**，如果对每个 $x\in M$ 与每个非零 $\xi \in T_x^*M$，主符号 $\sigma_m(D)(x,\xi): E_x \to F_x$ 都是**同构**（特别地 $E$ 与 $F$ 秩相同）。

“椭圆”一词来自二阶标量偏微分方程的分类：$a\partial_x^2 + 2b\partial_x\partial_y + c\partial_y^2$ 的符号是 $-(a\xi_1^2 + 2b\xi_1\xi_2 + c\xi_2^2)$，它对一切 $\xi\ne 0$ 非零，恰当二次型为定型时——即把方程分类为椭圆型（如 $\Delta$）的条件 $b^2 - ac < 0$，与之相对的是双曲型（波动方程，$b^2 - ac > 0$）或抛物型（热方程，$b^2 - ac = 0$）。波动算子 $\partial_t^2 - \partial_x^2$ 的符号是 $-(\xi_t^2 - \xi_x^2)$，它在锥 $\xi_t = \pm\xi_x$ 上消失：它**不是**椭圆的，确实也没有有限指标。椭圆性精确地是使符号“在所有方向上可逆”的条件，而这正是我们构造拟逆并援引 s1 所需要的。

> **直觉。** 椭圆性是说算子的主部没有“特征方向”——信息不能沿此方向不被光滑化地传播——没有激波前沿，没有光锥。于是 $Du = 0$ 的解在系数所允许的范围内尽可能光滑（见下一节）。陷阱：低阶项与椭圆性无关；对任意光滑势 $V(x)$，$\Delta + V(x)$ 都是椭圆的，因为符号忽略 $V$。

<a id="s3"></a>
### 椭圆正则性，以及为何紧流形上的椭圆算子是 Fredholm 的

本节给出桥梁：*紧*流形上的椭圆算子在恰当的 Hilbert 空间上定义出一个 Fredholm 算子，于是 s1 的指标得以适用。我们精确陈述两个分析定理并解释关键思想；完整证明属于偏微分方程课程，但每一项要素都会被点名。

#### Sobolev 空间——恰当的 Hilbert 空间

为使用 Hilbert 空间的 Fredholm 理论，我们不能在 $\Gamma(E)$ 上工作（光滑截面构成 Fréchet 空间而非 Hilbert 空间）。我们在 **Sobolev 范数**下完备化。

> **定义——Sobolev 空间。** 固定 $M$ 上以及 $E$ 上的度量（使截面有逐点范数，并有体积形式 $dV$）。对整数 $s \ge 0$，Sobolev 空间 $H^s(E)$ 是 $\Gamma(E)$ 在如下范数下的完备化：
> $$
> \|u\|_s^2 = \sum_{|\alpha|\le s} \int_M |\partial^\alpha u|^2 \, dV.
> $$
> 它是一个 Hilbert 空间，其元素是直到 $s$ 阶导数都平方可积的截面（导数取分布意义；见泛函分析指南）。

$m$ 阶微分算子延拓为有界映射 $D: H^s(E) \to H^{s-m}(F)$，因为微分 $m$ 次耗费 $m$ 阶正则性。这些空间之间的相互作用由两个定理支配。

#### 两个分析定理

> **定理（椭圆正则性 / Gårding 不等式）。** 设 $D$ 是紧流形 $M$ 上的 $m$ 阶椭圆算子。则：
> (i) **先验估计。** 存在常数 $C$ 使得
> $$
> \|u\|_s \le C\big(\|Du\|_{s-m} + \|u\|_{s-1}\big) \qquad \text{对一切 } u.
> $$
> (ii) **正则性。** 若 $u$ 是 $Du = f$ 的分布解且 $f$ 光滑，则 $u$ 光滑。更一般地，$f \in H^{s-m}$ 迫使 $u \in H^s$。

> **定理（椭圆算子的 Fredholm 性）。** *紧*流形 $M$ 上的 $m$ 阶椭圆算子 $D$，视为 $D: H^s(E) \to H^{s-m}(F)$，是 Fredholm 算子。进而 $\ker D$ 由光滑截面组成，$\dim\ker D < \infty$，$\dim\mathrm{coker} D < \infty$，且 $\mathrm{coker} D \cong \ker D^*$，其中 $D^*$ 是形式伴随（亦椭圆）。因此 $\mathrm{ind} D = \dim\ker D - \dim\ker D^*$ 是良定整数，**不依赖于 $s$**。

#### 证明的关键思想

我们不重现完整的偏微分方程论证，但这里给出完整的逻辑骨架——每一步都由一件点名的工具来证成。

1. **由符号构造拟逆。** 因为 $\sigma_m(D)(x,\xi)$ 对 $\xi\ne 0$ 可逆（椭圆性），可以构造一个 $-m$ 阶的**拟微分算子** $Q$，其符号在最高阶等于 $\sigma_m(D)^{-1}$。拟微分算子通过允许符号为 $(x,\xi)$ 的光滑函数（如 $|\xi|^{-m}$）来推广微分算子，它经由 Fourier 变换 $Qu(x) = (2\pi)^{-n}\int e^{i\langle x,\xi\rangle} q(x,\xi)\,\hat u(\xi)\,d\xi$ 定义。*这之所以可能的理由：* 符号的可逆性让我们能在 $\xi$ 上逐点求逆并把各片拼接起来。
2. **拟逆恒等式。** 这个 $Q$ 满足 $QD = I + R_1$ 与 $DQ = I + R_2$，其中 $R_1, R_2$ 是*负*阶的拟微分算子——它们提升一阶导数。*理由：* 把 $Q$（符号 $\approx \sigma_m^{-1}$）与 $D$（符号 $\sigma_m$）复合得主符号 $I$；误差由符号演算降为低阶。
3. **光滑化算子是紧的（Rellich 定理）。** 在*紧*流形上，对 $s > s'$，包含 $H^s \hookrightarrow H^{s'}$ 是紧算子（Rellich–Kondrachov）。由于 $R_1, R_2$ 把 $H^s$ 映入 $H^{s+1}$ 再包含回来，它们是紧的。*理由：* $M$ 的紧性使有界导数集列紧——这正是用到 $M$ 紧性之处。
4. **应用 Atkinson 定理。** 第 2–3 步说 $D$ 模紧算子可逆：它有拟逆 $Q$，使 $QD - I$、$DQ - I$ 紧。由 Atkinson 定理（s1），$D$ 是 Fredholm 算子。
5. **正则性给出核的光滑性。** 若 $Du = 0$ 则 $u = Qf - R_1 u = -R_1 u$ 提升一阶导数；自举（$u \in H^s \Rightarrow u \in H^{s+1} \Rightarrow \cdots$）表明 $u \in \bigcap_s H^s = $ 光滑截面（Sobolev 嵌入：$\bigcap_s H^s = C^\infty$）。*理由：* 反复应用先验估计。
6. **指标不依赖于 $s$。** 由于 $\ker D$ 光滑（故无论 $s$ 为何都相同），$\ker D^*$ 亦然，指标 $\dim\ker D - \dim\ker D^*$ 看不见 $s$。$\qquad\blacksquare$

> **陷阱。** $M$ 的紧性是本质的。在 $\mathbb R^n$ 上，包含 $H^s \hookrightarrow H^{s'}$ *不*紧（质量可逃逸至无穷），Rellich 定理失效，椭圆算子未必是 Fredholm 的——例如 $\mathbb R^n$ 上的 $\Delta$ 有直到 $0$ 的连续谱，没有有限指标。紧流形假设被内置于指标定理的每一个陈述之中。

## 第 B 部分 · 几何化身——de Rham、Hodge、Dirac

<a id="s4"></a>
### de Rham 复形与作为指标的 Euler 示性数

我们现在邂逅第一个真正几何的椭圆算子，以及第一次把指标与拓扑不变量等同起来。教训是：**Euler 示性数是一个指标。**

#### de Rham 复形

设 $M$ 是 $n$ 维紧定向 Riemann 流形。令 $\Omega^k = \Gamma(\Lambda^k T^*M)$ 为光滑微分 $k$-形式（切向量上的交错 $k$-线性函数；见微分几何指南）。**外微分** $d: \Omega^k \to \Omega^{k+1}$ 是满足 $d^2 = 0$ 的一阶微分算子。序列

$$
0 \to \Omega^0 \xrightarrow{d} \Omega^1 \xrightarrow{d} \cdots \xrightarrow{d} \Omega^n \to 0
$$

就是 **de Rham 复形**。因为 $d^2 = 0$，我们有 $\mathrm{im}(d:\Omega^{k-1}\to\Omega^k) \subseteq \ker(d:\Omega^k\to\Omega^{k+1})$，而 **de Rham 上同调**是商

$$
H^k_{\mathrm{dR}}(M) = \frac{\ker(d:\Omega^k\to\Omega^{k+1})}{\mathrm{im}(d:\Omega^{k-1}\to\Omega^k)}.
$$

de Rham 的一个定理（微分拓扑指南）把 $H^k_{\mathrm{dR}}(M)$ 与 $M$ 的拓扑上同调等同起来；特别地其维数 $b_k = \dim H^k_{\mathrm{dR}}(M)$，即**第 $k$ 个 Betti 数**，是拓扑不变量。

#### 把复形折叠成单个椭圆算子

复形不是单个算子，但我们可以把它折叠。利用 Riemann 度量，由 $\int_M \langle d\alpha, \beta\rangle\, dV = \int_M \langle \alpha, d^*\beta\rangle\, dV$ 定义**形式伴随** $d^*: \Omega^{k+1}\to\Omega^k$。按奇偶把形式分为偶与奇：

$$
\Omega^{\mathrm{ev}} = \bigoplus_{k \text{ even}} \Omega^k, \qquad \Omega^{\mathrm{odd}} = \bigoplus_{k \text{ odd}} \Omega^k,
$$

并定义单个算子

$$
D = d + d^* : \Omega^{\mathrm{ev}} \to \Omega^{\mathrm{odd}}.
$$

> **命题。** $D = d+d^*$ 是椭圆的。

**证明。**
1. $d$ 在 $(x,\xi)$ 处的符号是 $\sigma(d)(\xi)\,\omega = i\,\xi\wedge\omega$（与 $i\xi$ 作外乘），因为 $d$ 在坐标中是 $\sum dx^i \wedge \partial_{x^i}$，而符号法则把 $\partial_{x^i}\mapsto i\xi_i$。*理由：* 主符号的定义（s2）。
2. $d^*$ 的符号是 $\sigma(d^*)(\xi)\,\omega = -i\,\iota_{\xi^\sharp}\omega$（与度量对偶向量 $\xi^\sharp$ 作内乘），即 $i\xi\wedge(\cdot)$ 在内积下的伴随。*理由：* 楔乘的伴随是缩并。
3. 于是 $\sigma(D)(\xi) = i(\xi\wedge \,\cdot\; -\; \iota_{\xi^\sharp})$。其平方为 $\sigma(D)(\xi)^2 = -(\xi\wedge\iota_{\xi^\sharp} + \iota_{\xi^\sharp}\,\xi\wedge\,\cdot)$。恒等式 $\xi\wedge\iota_{\xi^\sharp} + \iota_{\xi^\sharp}\,(\xi\wedge\cdot) = |\xi|^2\,\mathrm{id}$（Clifford/Cartan 关系）给出 $\sigma(D)(\xi)^2 = -|\xi|^2\,\mathrm{id}$。*理由：* 缩并—楔乘的反对易子等于长度的平方。
4. 对 $\xi\ne 0$，$\sigma(D)(\xi)^2 = -|\xi|^2\,\mathrm{id}$ 可逆，故 $\sigma(D)(\xi)$ 可逆。因此 $D$ 椭圆。$\qquad\blacksquare$

#### 作为 $D$ 之指标的 Euler 示性数

> **定理。** $\displaystyle \mathrm{ind}(d+d^*: \Omega^{\mathrm{ev}}\to\Omega^{\mathrm{odd}}) = \chi(M)$，即 **Euler 示性数** $\chi(M) = \sum_{k=0}^n (-1)^k b_k$。

**证明。**
1. $D = d+d^*: \Omega^{\mathrm{ev}}\to\Omega^{\mathrm{odd}}$ 的伴随是 $D^* = d+d^*: \Omega^{\mathrm{odd}}\to\Omega^{\mathrm{ev}}$（因 $(d)^* = d^*$ 且 $(d^*)^* = d$）。故 $\mathrm{ind} D = \dim\ker(D|_{\mathrm{ev}}) - \dim\ker(D|_{\mathrm{odd}})$。
2. 定义 **Hodge–Laplace 算子** $\Delta = (d+d^*)^2 = dd^* + d^*d$（交叉项 $d^2, (d^*)^2$ 消失）。形式 $\omega$ 是**调和的**（$\Delta\omega = 0$）当且仅当 $D\omega = 0$：事实上 $\langle\Delta\omega,\omega\rangle = \|d\omega\|^2 + \|d^*\omega\|^2$，它为零当且仅当 $d\omega = 0$ 且 $d^*\omega = 0$，即当且仅当 $(d+d^*)\omega = 0$。*理由：* 范数平方之和为零当且仅当每一项都为零。
3. 令 $\mathcal H^k = \{\omega\in\Omega^k : \Delta\omega = 0\}$ 为调和 $k$-形式。由第 2 步，$\ker(D|_{\mathrm{ev}}) = \bigoplus_{k\text{ even}}\mathcal H^k$ 且 $\ker(D|_{\mathrm{odd}}) = \bigoplus_{k\text{ odd}}\mathcal H^k$。
4. Hodge 定理（s5，下面将证）断言 $\dim\mathcal H^k = b_k$。承认这一点，
$$
\mathrm{ind} D = \sum_{k\text{ even}} b_k - \sum_{k\text{ odd}} b_k = \sum_{k=0}^n (-1)^k b_k = \chi(M). \qquad\blacksquare
$$

> **典型例（$2$ 维球面）。** 对 $M = S^2$：$b_0 = 1$（连通），$b_1 = 0$（单连通），$b_2 = 1$（定向闭曲面）。则 $\chi(S^2) = 1 - 0 + 1 = 2$。因此 $S^2$ 上 $d+d^*$ 的指标为 $2$——与经典事实“$S^2$ 上每个光滑向量场都有零点，总次数为 $2$”（毛球定理）相符。对环面 $T^2$：$b_0=1, b_1=2, b_2=1$，故 $\chi = 0$，环面确实容许处处非零的向量场。

这是整个学科的原型：一个分析指标（椭圆偏微分方程解空间的 $\dim$）等于一个拓扑不变量（$\chi$）。Gauss–Bonnet 定理（s9）会把同一个 $\chi$ 算作曲率积分，从而补全这个三角。

<a id="s5"></a>
### Hodge 定理——上同调的调和代表元

前面第 4 步我们欠下了事实 $\dim\mathcal H^k = b_k$。这就是 **Hodge 定理**，是“分析计算拓扑”最干净的例证。我们陈述它，指出其唯一的分析输入，并由该输入证明与上同调的等同。

> **定理（Hodge）。** 设 $M$ 是紧定向 Riemann 流形。对每个 $k$：
> (a) $\dim\mathcal H^k < \infty$。
> (b) **Hodge 分解：** $\Omega^k = \mathcal H^k \oplus \mathrm{im} d \oplus \mathrm{im} d^*$，一个正交直和。
> (c) 每个 de Rham 上同调类都有*唯一的*调和代表元；映射 $\mathcal H^k \to H^k_{\mathrm{dR}}(M)$，$\omega \mapsto [\omega]$，是同构。特别地 $\dim\mathcal H^k = b_k$。

#### 分析输入

*唯一*困难的分析事实是：

> **分析输入。** $\Omega^k$ 上的 Hodge–Laplace 算子 $\Delta = dd^* + d^*d$ 是椭圆的（其符号为 $|\xi|^2\,\mathrm{id}$，完全如 s4 第 3 步那样计算后取平方）、自伴的、非负的。由 s3 它是 Fredholm 算子；由于自伴，$\mathrm{coker}\Delta \cong \ker\Delta = \mathcal H^k$，故 $\mathrm{im}\Delta = (\ker\Delta)^\perp$ 闭，且 $\Omega^k = \mathcal H^k \oplus \mathrm{im}\Delta$ 正交，其中 $\mathcal H^k$ 有限维。

其余一切都是这一分解上的线性代数。

#### 由该输入证明 (b) 与 (c)

1. **分解 $\Delta$ 的值域。** 由输入，$\Omega^k = \mathcal H^k \oplus \mathrm{im}\Delta$。现在 $\mathrm{im}\Delta = \mathrm{im}(dd^* + d^*d) \subseteq \mathrm{im} d + \mathrm{im} d^*$。反过来 $\mathrm{im} d$ 与 $\mathrm{im} d^*$ 都与 $\mathcal H^k$ 正交：若 $\omega$ 调和，则 $\langle\omega, d\alpha\rangle = \langle d^*\omega,\alpha\rangle = 0$（因 $d^*\omega=0$），类似地 $\langle\omega, d^*\beta\rangle = \langle d\omega,\beta\rangle = 0$。*理由：* 调和形式是 $d$-闭且 $d^*$-闭的（s4 第 2 步）。
2. **$\mathrm{im} d \perp \mathrm{im} d^*$。** $\langle d\alpha, d^*\beta\rangle = \langle d^2\alpha,\beta\rangle = 0$，因 $d^2 = 0$。*理由：* de Rham 复形是一个复形。
3. 把 1–2 与输入结合得正交分裂 $\Omega^k = \mathcal H^k \oplus \mathrm{im} d \oplus \mathrm{im} d^*$，证明 (b)。
4. **上同调 = 调和形式。** 取闭形式 $\omega$（$d\omega = 0$）。由 (b) 写 $\omega = h + d\alpha + d^*\beta$。作用 $d$：$0 = d\omega = d(d^*\beta)$（因 $dh=0$，$d^2\alpha=0$）。则 $0 = \langle dd^*\beta, \beta\rangle = \|d^*\beta\|^2$，故 $d^*\beta = 0$，于是它的值域项消失。*理由：* 范数为零当且仅当向量为零。
5. 于是 $\omega = h + d\alpha$，其中 $h$ 调和：每个闭形式都是一个调和形式加一个恰当形式，故在 $H^k_{\mathrm{dR}}$ 中 $[\omega] = [h]$。映射 $\mathcal H^k \to H^k_{\mathrm{dR}}$ 是**满射**。
6. **单射性。** 若 $h$ 调和且 $[h] = 0$，则 $h = d\gamma$ 恰当；但 $\langle h, h\rangle = \langle h, d\gamma\rangle = \langle d^* h, \gamma\rangle = 0$，因 $d^* h = 0$。故 $h = 0$。映射是**单射**。
7. 第 5–6 步给出同构 $\mathcal H^k \cong H^k_{\mathrm{dR}}(M)$，故 $\dim\mathcal H^k = b_k$，由输入它有限。这证明了 (a) 与 (c)。$\qquad\blacksquare$

> **典型例。** 在连通的 $M$ 上，$\mathcal H^0 = \{$常数$\}$：$\Delta f = 0$（$f$ 为函数）意味着 $d^*df = 0$，故 $\|df\|^2 = \langle d^*df, f\rangle = 0$，于是 $df = 0$ 且 $f$ 局部常值，即在每个连通分支上常值。故 $\dim\mathcal H^0 = b_0 = $ 连通分支数——以分析方式恢复了这一拓扑事实。

> **直觉。** Hodge 理论说：在每个上同调类中恰好存在一个“最小能量”代表元，即调和的那一个，它极小化 $\|d\alpha\|^2 + \|d^*\alpha\|^2$。拓扑（类）约束分析（极小元）。陷阱：这需要度量来定义 $d^*$ 与 $\Delta$；调和代表元依赖于度量，但其*存在性与唯一性*不依赖。

<a id="s6"></a>
### Clifford 代数、旋量与 Dirac 算子

de Rham 算子 $d+d^*$ 是一个椭圆算子；而指标定理对一个范例最为干净，那就是 **Dirac 算子**，其平方是一个 Laplace 算子，其符号由 **Clifford 代数**构造。Dirac 在寻求波动/Laplace 算子的一阶“平方根”时发现了它。

#### Clifford 代数

> **定义——Clifford 代数。** 设 $V$ 是带内积 $\langle\cdot,\cdot\rangle$ 的实向量空间。**Clifford 代数** $\mathrm{Cl}(V)$ 是由 $V$ 生成、服从关系
> $$
> v\cdot w + w\cdot v = -2\langle v,w\rangle\, 1 \qquad (v,w\in V)
> $$
> 的结合代数。特别地 $v\cdot v = -|v|^2$，而对标准正交基 $e_i$，$e_i e_j + e_j e_i = -2\delta_{ij}$。

这是“对二次型取平方根”的代数骨架：若 $D = \sum e_i \partial_{x^i}$ 作用时 $e_i$ 按 Clifford 方式相乘，则 $D^2 = \sum_{i,j} e_i e_j \partial_{x^i}\partial_{x^j} = -\sum_i \partial_{x^i}^2 = \Delta$，因为非对角项由反对称性 $e_ie_j = -e_je_i$ 相消，而对角项给出 $e_i^2 = -1$。Clifford 关系*恰恰*是使交叉项相消的东西。

#### 旋量与旋量表示

一个 **Clifford 模**（或**旋量空间**）$S$ 是携带表示 $c: \mathrm{Cl}(V) \to \mathrm{End}(S)$ 的向量空间，即线性映射 $c(v): S\to S$ 满足 $c(v)c(w) + c(w)c(v) = -2\langle v,w\rangle$。对偶数维 $\dim V = 2m$，存在（在同构意义下）唯一的不可约复旋量空间，维数为 $2^m$，带有 $\mathbb Z/2$ 分次 $S = S^+ \oplus S^-$ 分成半旋量，且与向量的 Clifford 乘法交换 $S^+ \leftrightarrow S^-$（它是*奇*的）。Riemann 流形上的一个**自旋结构**是在每个切空间上对这种旋量空间 $S_x$ 作出全局、相容的选取，并经由 **Spin 群**（旋转群 $SO(n)$ 的二重覆盖）沿流形扭转。并非每个流形都容许自旋结构；障碍是第二 Stiefel–Whitney 类 $w_2$（微分拓扑指南）。当它存在时我们得到**旋量丛** $S = S^+ \oplus S^-$。

#### Dirac 算子

> **定义——Dirac 算子。** 设 $M$ 是带旋量丛 $S = S^+\oplus S^-$ 与由 Levi-Civita 联络诱导的 $S$ 上联络 $\nabla$ 的自旋 Riemann 流形。**Dirac 算子**是
> $$
> {D\!\!\!/} = \sum_i c(e_i)\,\nabla_{e_i} : \Gamma(S) \to \Gamma(S),
> $$
> 其中 $\{e_i\}$ 是局部标准正交标架，$c$ 是 Clifford 乘法。由于 $c$ 是奇的，${D\!\!\!/}$ 交换分次：它限制为
> $$
> {D\!\!\!/}^+ : \Gamma(S^+) \to \Gamma(S^-), \qquad {D\!\!\!/}^- : \Gamma(S^-) \to \Gamma(S^+),
> $$
> 且 ${D\!\!\!/}^- = ({D\!\!\!/}^+)^*$。

> **命题。** ${D\!\!\!/}$ 是椭圆的，其主符号是 $\sigma({D\!\!\!/})(\xi) = i\,c(\xi)$。

**证明。**
1. ${D\!\!\!/} = \sum_i c(e_i)\nabla_{e_i}$ 的最高阶部分把 $\nabla_{e_i}\mapsto i\xi_i$ 替换，给出 $\sigma({D\!\!\!/})(\xi) = i\sum_i \xi_i\, c(e_i) = i\,c(\xi^\sharp)$。*理由：* 符号的定义（s2）；联络的低阶 Christoffel 项被舍去。
2. 取平方：$\sigma({D\!\!\!/})(\xi)^2 = i^2\, c(\xi)c(\xi) = -(-|\xi|^2) = |\xi|^2$，由 Clifford 关系 $c(\xi)^2 = -|\xi|^2$。*理由：* Clifford 恒等式。
3. 对 $\xi\ne 0$，$\sigma({D\!\!\!/})(\xi)^2 = |\xi|^2 \ne 0$，故 $\sigma({D\!\!\!/})(\xi)$ 可逆。椭圆。$\qquad\blacksquare$

由 s3，在紧自旋流形上 ${D\!\!\!/}^+: \Gamma(S^+)\to\Gamma(S^-)$ 是 Fredholm 算子，带有良定的整数指标

$$
\mathrm{ind}{D\!\!\!/}^+ = \dim\ker{D\!\!\!/}^+ - \dim\ker{D\!\!\!/}^-.
$$

$\ker{D\!\!\!/}$ 中的元素是**调和旋量**。Atiyah–Singer 定理（s8）恰恰以拓扑方式计算这个数——而值得注意的是，答案是 $\hat A$-亏格（s7）。

> **Lichnerowicz 公式与第一份回报。** Weitzenböck 恒等式 ${D\!\!\!/}^2 = \nabla^*\nabla + \tfrac14 R$ 成立，其中 $\nabla^*\nabla \ge 0$ 是联络 Laplace 算子，$R$ 是数量曲率。若处处 $R > 0$，则对 ${D\!\!\!/}\psi = 0$ 我们得到 $0 = \|\nabla\psi\|^2 + \tfrac14\int R|\psi|^2 \ge \tfrac14\int R|\psi|^2 \ge 0$，迫使 $\psi = 0$。故正数量曲率的紧自旋流形有 $\ker{D\!\!\!/} = 0$，从而 $\mathrm{ind}{D\!\!\!/}^+ = 0$，从而 $\hat A(M) = 0$——这是正数量曲率的一个拓扑障碍，竟是通过分析发现的。这是定理威力的一瞥。

> **陷阱。** 两个不同的算子常常都被称为“Dirac”：上面的纯旋量 Dirac 算子，以及耦合到带联络的辅助丛 $E$ 的**扭转**版本 ${D\!\!\!/}_E = {D\!\!\!/}\otimes \nabla^E$。一般指标定理是对扭转算子陈述的，它把 de Rham、符号差与 Dolbeault 算子作为特殊的 $E$ 加以涵盖。

## 第 C 部分 · 拓扑的一面与定理

<a id="s7"></a>
### 拓扑指标——Chern 特征标、Todd 类与 Â-亏格

指标定理的右端是由特征类构造的**拓扑指标**。我们定义三位主角——Chern 特征标、Todd 类与 $\hat A$-亏格——并解释它们如何组装。我们使用 Chern–Weil 理论（微分拓扑指南）：特征类由联络曲率 $2$-形式 $\Omega$ 的一个多项式表示，其在 $M$ 上的积分是一个拓扑数。

#### 用一行写出经由 Chern–Weil 的特征类

对带联络（曲率为 $\Omega$，一个 $\mathrm{End}(E)$-值的 $2$-形式）的复向量丛 $E$，**全 Chern 类**是 $c(E) = \det\!\big(I + \tfrac{i}{2\pi}\Omega\big) = 1 + c_1 + c_2 + \cdots$，其中 $c_k$ 是闭 $2k$-形式，其上同调类不依赖于联络。形式地分解 $c(E) = \prod_j (1 + x_j)$；$x_j$ 是 **Chern 根**（形式的 $2$ 次类；它们的对称函数是真正的类）。

#### Chern 特征标

> **定义——Chern 特征标。** $\displaystyle \mathrm{ch}(E) = \sum_j e^{x_j} = \mathrm{rank}(E) + c_1 + \tfrac12(c_1^2 - 2c_2) + \cdots = \mathrm{tr}\,\exp\!\Big(\tfrac{i}{2\pi}\Omega\Big).$

其定义性优点在于可加性与可乘性：

> **命题。** $\mathrm{ch}(E\oplus F) = \mathrm{ch}(E) + \mathrm{ch}(F)$ 且 $\mathrm{ch}(E\otimes F) = \mathrm{ch}(E)\,\mathrm{ch}(F)$。

**证明。** 对直和，Chern 根是并 $\{x_j\}\cup\{y_k\}$，故 $\sum e^{x_j} + \sum e^{y_k}$ 相加。对张量积，根是和 $x_j + y_k$，故 $\mathrm{ch}(E\otimes F) = \sum_{j,k} e^{x_j+y_k} = (\sum_j e^{x_j})(\sum_k e^{y_k}) = \mathrm{ch}(E)\mathrm{ch}(F)$，用到 $e^{a+b}=e^a e^b$。*理由：* 指数把根之和变为乘积。$\qquad\blacksquare$

这正是为什么 Chern 特征标是拓扑一面上的自然对象：指标在算子直和下可加、在流形乘积下可乘，而 $\mathrm{ch}$ 是具有这些性质的万有类。

#### Todd 类与 Â-亏格

> **定义——Todd 类。** $\displaystyle \mathrm{Td}(E) = \prod_j \frac{x_j}{1 - e^{-x_j}} = 1 + \tfrac12 c_1 + \tfrac{1}{12}(c_1^2 + c_2) + \cdots$（用到 $\frac{x}{1-e^{-x}} = 1 + \tfrac{x}{2} + \tfrac{x^2}{12} - \cdots$，即 Bernoulli 数的生成级数）。

> **定义——Â-亏格。** 对（复化的）切丛，Pontryagin 根为 $\pm x_j$，
> $$
> \hat A(M) = \prod_j \frac{x_j/2}{\sinh(x_j/2)} = 1 - \tfrac{1}{24}p_1 + \tfrac{1}{5760}(7p_1^2 - 4p_2) + \cdots,
> $$
> 其中 $p_k$ 是 Pontryagin 类（微分拓扑指南）。

两者都是可乘的“亏格”：$\mathrm{Td}(E\oplus F) = \mathrm{Td}(E)\mathrm{Td}(F)$，$\hat A$ 类似，理由是与 $\mathrm{ch}$ 相同的“按根取乘积”结构（证明完全相同：根的可乘函数在直和下可乘）。

#### 组装拓扑指标

对流形 $M^n$ 上带符号类的椭圆算子 $D$，拓扑指标在其对扭转 Dirac 算子 ${D\!\!\!/}_E$ 最常用的形式下为

$$
\mathrm{ind}_{\mathrm{top}}({D\!\!\!/}_E) = \int_M \hat A(M)\,\mathrm{ch}(E),
$$

即取乘积的最高次（$n$-形式）分量并积分。对一般椭圆算子，公式是 $\int_M (-1)^n \mathrm{ch}(\sigma(D))\mathrm{Td}(TM\otimes\mathbb C)$，经由符号类来求值，但每个经典情形都归约到上面那样的 Dirac 型公式。下一节将陈述把这一积分与分析指标等同起来的定理。

> **典型计算（$4$ 维流形上的次数计数）。** 在 $M^4$ 上，$\hat A = 1 - \tfrac{1}{24}p_1$，且 $\mathrm{ch}(E) = r + c_1 + \tfrac12(c_1^2 - 2c_2)$，其中 $r = \mathrm{rank} E$。乘积的 $4$-形式部分是 $\tfrac12(c_1^2 - 2c_2) - \tfrac{r}{24}p_1$。于是
> $$
> \mathrm{ind}{D\!\!\!/}_E = \int_{M^4}\Big[\tfrac12 c_1(E)^2 - c_2(E) - \tfrac{r}{24}p_1(M)\Big].
> $$
> 当 $E$ 平凡（$r=1, c_1=c_2=0$）：$\mathrm{ind}{D\!\!\!/} = -\tfrac{1}{24}\int_{M^4} p_1 = \hat A(M)$，一个整数——这是自旋 $4$ 维流形的 $p_1$ 上一个非平凡的整性约束。

<a id="s8"></a>
### Atiyah–Singer 指标定理与“分析 = 拓扑”的含义

我们现在可以完整陈述定理并拆解这个等式。

> **定理（Atiyah–Singer，1963）。** 设 $M$ 是无边界的紧定向光滑流形，$D: \Gamma(E)\to\Gamma(F)$ 是椭圆微分（或拟微分）算子。则分析指标等于拓扑指标：
> $$
> \mathrm{ind}_{\mathrm{an}}(D) \;=\; \mathrm{ind}_{\mathrm{top}}(D),
> $$
> 其中 $\mathrm{ind}_{\mathrm{an}}(D) = \dim\ker D - \dim\mathrm{coker} D$（s1，由 s3 良定）且
> $$
> \mathrm{ind}_{\mathrm{top}}(D) = (-1)^n\!\int_{M}\mathrm{ch}\big([\sigma(D)]\big)\,\mathrm{Td}(TM\otimes\mathbb C),
> $$
> 其中 $[\sigma(D)] \in K(T^*M)$ 是主符号的 K-理论类，$n = \dim M$。对扭转 Dirac 算子，这归约为 $\mathrm{ind}{D\!\!\!/}_E = \int_M \hat A(M)\,\mathrm{ch}(E)$。

#### 两端的含义以及为何这个等式深刻

- **左端是分析。** $\dim\ker D$ 与 $\dim\mathrm{coker} D$ 需要在 $M$ 上求解偏微分方程——找出 $Du = 0$ 的所有解以及所有障碍。它们以复杂的方式依赖于度量、联络与系数的精确细节。每一个都确实困难且各自依赖度量。
- **右端是拓扑。** $\mathrm{ch}, \mathrm{Td}, \hat A$ 是曲率的多项式，其*积分*不依赖于任何选取（Chern–Weil：特征类的积分是同伦/配边不变量）。你可以仅凭流形的拓扑与丛的拓扑算出右端，常常可以手算。
- **等式说这两种截然不同的计算总是一致。** 分析学家对解的计数被拓扑逐个整数地强制。反过来，拓扑学家的积分总是整数（它计数某物），这是一个整性定理，从多项式公式（那些 $\tfrac{1}{24}$、$\tfrac{1}{5760}$ 必须共谋以给出整数）来看绝非显然。

#### 它为何成立？证明策略的结构

有三个经典证明；它们都共享如下逻辑：*两端都是形变不变量，且在生成元上吻合*。

1. **配边证明（原始，1963）。** $\mathrm{ind}_{\mathrm{an}}$ 与 $\mathrm{ind}_{\mathrm{top}}$ 都在配边下不变，并且在生成全部符号类的运算（直和、乘积、嵌入）下表现相同。Atiyah–Singer 归约到在一个生成集（经由嵌入到球面构造）上验证相等，并在那里加以验证。发动机是**分析指标的稳定性**（s1）：它正是让你能自由形变的东西。
2. **K-理论证明（1968）。** 把指标重新表述为同态 $K(T^*M)\to\mathbb Z$。分析指标与拓扑指标都是这样的同态，且在嵌入下自然；通过一个公理化刻画（在一点上的归一化 + 可乘性 + 切除）证明它们一致。稳定性（s1）再次支撑自然性。
3. **热核证明（s10）。** 把指标直接算作热迹的一个极限，并证明该极限定域化为一个曲率积分，而它*就是*拓扑指标。这是最分析的一个，也是我们将概述的那个。

#### 对原型的一致性检验

对 $D = d+d^*$（s4），定理必须给出 $\chi(M)$。确实，该算子的拓扑指标算得 $\int_M e(M)$，即 Euler 类，由 Gauss–Bonnet–Chern 它等于 $\chi(M)$——与 s4 的分析答案相符。我们将在 s9 中追溯这一点。

> **直觉。** 设想全体椭圆算子（或符号）的空间。它分裂为连通分支（“形变类”）；指标在每个分支上常值（s1）。拓扑提供了一个独立的不变量——特征数积分——它也在每个分支上常值。定理说这两个局部常值函数*相等*，而不仅仅是各自常值。证明就是逐分支挑一个代表元来核验它们吻合的苦工。陷阱：定理要求 $M$ 紧、无边界，且 $D$ 椭圆；带边界时需要 Atiyah–Patodi–Singer 修正（一个额外的 $\eta$-不变量项），而无椭圆性则根本没有有限指标。

<a id="s9"></a>
### 恢复的特例：Gauss–Bonnet–Chern、符号差定理、Riemann–Roch

定理的统一威力可由给它喂入三个不同的椭圆算子、看着三个著名经典定理落下而看到。每一个都是被某特定丛扭转的 Dirac 型算子的指标。

#### Gauss–Bonnet–Chern（算子：$d+d^*$，完整 de Rham）

算子 $D = d+d^*:\Omega^{\mathrm{ev}}\to\Omega^{\mathrm{odd}}$ 由 s4 有分析指标 $\chi(M)$。其拓扑指标是 **Euler 类** $e(TM)$ 的积分：

$$
\chi(M) = \mathrm{ind}(d+d^*) = \int_M e(TM).
$$

由 Chern–Weil，Euler 类在偶数维 $n = 2m$ 由曲率的 **Pfaffian** 表示：$e(TM) = \frac{1}{(2\pi)^m m!}\mathrm{Pf}(\Omega)$。在二维中这是 $\frac{1}{2\pi}K\,dA$，其中 $K$ 是 Gauss 曲率，给出经典的 **Gauss–Bonnet 定理**

$$
\chi(M^2) = \frac{1}{2\pi}\int_M K\, dA.
$$

> **典型例。** 对单位 $S^2$，$K = 1$ 且 $\mathrm{Area} = 4\pi$，故 $\frac{1}{2\pi}\int K\,dA = \frac{4\pi}{2\pi} = 2 = \chi(S^2)$。三种计算——计数调和形式（s4）、此处的曲率积分、以及拓扑 $1-0+1$——都给出 $2$。

#### Hirzebruch 符号差定理（算子：符号差算子）

在维数 $n = 4k$ 的定向流形上，**Hodge 星** $\star$ 在中维形式上给出一个对合 $\tau$，把 $\Omega^{\mathrm{ev}} = \Omega^+\oplus\Omega^-$ 分裂成 $\pm 1$ 特征空间。**符号差算子** $D_{\mathrm{sig}} = d+d^*:\Omega^+\to\Omega^-$ 的分析指标等于**符号差** $\mathrm{sign}(M)$——即 $H^{2k}(M)$ 上相交形式的符号差（对称配对 $\alpha\wedge\beta$ 的正特征值个数减负特征值个数）。拓扑指标是 **$L$-亏格**（一个 Pontryagin 多项式）：

$$
\mathrm{sign}(M) = \int_M L(M), \qquad L = 1 + \tfrac13 p_1 + \tfrac{1}{45}(7p_2 - p_1^2) + \cdots
$$

> **典型例。** 在 $M^4$ 上，$\mathrm{sign}(M) = \tfrac13\int_{M} p_1$。对复射影平面 $\mathbb{CP}^2$，$\int p_1 = 3$（因 $p_1 = 3$ 倍生成元），给出 $\mathrm{sign} = 1$——正确，因为 $H^2(\mathbb{CP}^2)=\mathbb Z$ 带正的自相交。

#### Hirzebruch–Riemann–Roch（算子：Dolbeault 算子）

在带全纯向量丛 $E$ 的紧复流形 $X$ 上，**Dolbeault 算子** $\bar\partial + \bar\partial^*:\Omega^{0,\mathrm{ev}}(E)\to\Omega^{0,\mathrm{odd}}(E)$ 的分析指标等于**全纯 Euler 示性数**

$$
\chi(X,E) = \sum_q (-1)^q \dim H^q(X, \mathcal O(E)),
$$

即层上同调维数的交错和（全纯截面的空间及其高阶障碍）。拓扑指标是

$$
\chi(X,E) = \int_X \mathrm{ch}(E)\,\mathrm{Td}(TX),
$$

即 **Hirzebruch–Riemann–Roch 定理**。这正是 Todd 类赢得其位置之处。

> **典型例（Riemann 曲面）。** 对亏格 $g$ 的紧 Riemann 曲面 $X$ 与次数 $d$ 的线丛 $L$：$\dim X = 1$，$\mathrm{Td}(TX) = 1 + \tfrac12 c_1(TX)$，$\mathrm{ch}(L) = 1 + c_1(L)$。$2$ 次部分是 $c_1(L) + \tfrac12 c_1(TX)$，而 $\int_X c_1(L) = d$，$\int_X c_1(TX) = 2 - 2g$（Euler 示性数）。故
> $$
> \chi(X,L) = d + \tfrac12(2-2g) = d - g + 1,
> $$
> 即 $\dim H^0 - \dim H^1 = d - g + 1$，即曲线的**经典 Riemann–Roch 定理**。指标定理把 $19$ 世纪的代数几何用一行重现。

> **字典小结。** 用空丛扭转 Dirac → $\hat A$-亏格；用整个外丛扭转 → Euler 类（Gauss–Bonnet）；用自对偶分裂扭转 → $L$-亏格（符号差）；用 Dolbeault/全纯结构扭转 → Todd 类（Riemann–Roch）。一个定理，四座经典里程碑。

## 第 D 部分 · 证明概要与物理

<a id="s10"></a>
### 热核方法——McKean–Singer 与超对称相消

我们概述最分析的证明，它把指标算作热迹并证明它定域化为拓扑积分。这是物理学家钟爱的路线，因为“超对称相消”是反复出现的量子场论机制。

#### McKean–Singer 公式

设 $D = {D\!\!\!/}^+: \Gamma(S^+)\to\Gamma(S^-)$，伴随为 $D^* = {D\!\!\!/}^-$。构造两个 Laplace 算子 $\Delta^+ = D^* D$（在 $S^+$ 上）与 $\Delta^- = D D^*$（在 $S^-$ 上）。两者都是非负的椭圆自伴算子，故各自有离散谱 $0 \le \lambda_0 \le \lambda_1 \le \cdots \to \infty$，特征空间有限维。

> **定理（McKean–Singer）。** 对每个 $t > 0$，
> $$
> \mathrm{ind} D = \mathrm{Tr}\big(e^{-t\Delta^+}\big) - \mathrm{Tr}\big(e^{-t\Delta^-}\big) =: \mathrm{Str}\big(e^{-t{D\!\!\!/}^2}\big),
> $$
> 即热算子的**超迹**，*不依赖于 $t$*。

**证明（相消）。**
1. **非零特征值成对出现。** 设 $\Delta^+\phi = \lambda\phi$ 且 $\lambda \ne 0$。则 $\psi := D\phi$ 满足 $\Delta^-\psi = DD^*D\phi = D\Delta^+\phi = \lambda D\phi = \lambda\psi$，且 $\psi\ne 0$（否则 $D^*D\phi = 0$ 迫使 $\lambda = 0$）。故 $D$ 把 $\Delta^+$ 的 $\lambda$-特征空间映到 $\Delta^-$ 的 $\lambda$-特征空间。对称地 $D^*$ 映回，而 $D^*D = \lambda$ 在 $+$ 侧表明这两个映射互逆（相差 $\lambda$ 倍），从而是**同构**。*理由：* $D$ 交织 $\Delta^+$ 与 $\Delta^-$。
2. 因此对每个 $\lambda > 0$，特征空间 $V_\lambda^+$ 与 $V_\lambda^-$ 维数*相等*。在超迹
$$
\mathrm{Tr}(e^{-t\Delta^+}) - \mathrm{Tr}(e^{-t\Delta^-}) = \sum_\lambda e^{-t\lambda}\big(\dim V_\lambda^+ - \dim V_\lambda^-\big)
$$
中，每个 $\lambda > 0$ 贡献 $e^{-t\lambda}(d - d) = 0$。*理由：* 第 1 步的配对。
3. 只有 $\lambda = 0$ 幸存：$\dim V_0^+ - \dim V_0^- = \dim\ker D - \dim\ker D^* = \mathrm{ind} D$，其中 $e^{-t\cdot 0} = 1$。故超迹对一切 $t$ 都等于 $\mathrm{ind} D$。$\qquad\blacksquare$

这就是**超对称相消**：玻色（$S^+$）与费米（$S^-$）激发态成对相消；只有基态（零模）贡献于指标。$t$ 无关性是要害所在。

#### 当 $t \to 0$ 时的定域化

既然超迹与 $t$ 无关，就在极限 $t\to 0^+$ 下求值，那里热核在对角线附近定域化，并可由局部几何算出。

1. **热核的小时间展开。** $e^{-t\Delta}$ 的核 $k_t(x,y)$ 当 $t\to 0$ 时有渐近展开
$$
\mathrm{Str} k_t(x,x) \sim (4\pi t)^{-n/2}\sum_{j\ge 0} t^j\, a_j(x),
$$
其中 $a_j(x)$ 是曲率及其协变导数的万有多项式（**Seeley–DeWitt 系数**），是局部量。*理由：* 热方程的拟逆构造。
2. **只有常数项能幸存。** 积分后，$\mathrm{ind} D = \int_M \mathrm{Str} k_t(x,x)\,dV \sim (4\pi t)^{-n/2}\sum_j t^j\int_M a_j$。左端是常数 $\mathrm{ind} D$，故除 $t^0$ 外 $t$ 的一切幂在极限中必须消失：$j < n/2$ 的 $t^{-n/2+j}$ 项积分为零，而 $t\to0$ 极限挑出 $j = n/2$（对偶数 $n$），给出
$$
\mathrm{ind} D = \int_M a_{n/2}(x)\,(4\pi)^{-n/2}\,dV.
$$
*理由：* 在一个 $t$-无关恒等式两端匹配 $t$ 的幂。
3. **辨认幸存的系数。** 深刻的一步（Patodi、Gilkey，以及使之透明的 **Getzler 重标度**）是：定域化的超迹 $\mathrm{Str} a_{n/2}$ 恰好是 $\hat A(M)\mathrm{ch}(E)$ 的最高次分量。Getzler 的技巧重标度 Clifford 变量与坐标，使热算子极限为一个**谐振子**（Mehler 公式），其超迹有闭形式可算，且*就是* $\hat A\mathrm{ch}$ 的被积函数。*理由：* 重标度后的极限把几何热核变成量子振子的精确可解 Gauss 函数。
4. 综合：$\mathrm{ind}{D\!\!\!/}_E = \int_M \hat A(M)\mathrm{ch}(E)$，即指标定理。$\qquad\blacksquare$（概要）

> **直觉。** 指标是一个数（无 $t$），故我们可以在任意时间尺度上计算它；在 $t\to 0$ 时热尚未扩散，故答案由*局部*曲率构成，却等于一个*整体*拓扑积分。“相消的奇迹”在于除基态外一切都被消去，剩下的恰是一个完美的特征类。陷阱：小 $t$ 展开有许多看似发散的项（$t^{-n/2}$）；定理保证在取*超*迹后它们全部相消——用普通迹则不会。

<a id="s11"></a>
### 物理——反常、费米子零模与瞬子

指标定理对物理学家而言不是猎奇：它计算**反常**、计数**费米子零模**，并奠定**瞬子**物理的基础。我们逐一概述，并定义术语。

#### 费米子零模与路径积分

在量子场论中，背景规范场 $A$ 中的 Dirac 费米子由（扭转的）Dirac 算子 ${D\!\!\!/}_A$ 支配。一个**零模**是 ${D\!\!\!/}_A\psi = 0$ 的解——一个可归一化的调和旋量。指标 $\mathrm{ind}{D\!\!\!/}_A = n_+ - n_-$ 计数左手减右手零模（$n_\pm = \dim\ker{D\!\!\!/}^\pm$）。由指标定理这是规范场强的一个拓扑积分：

$$
n_+ - n_- = \int_M \hat A(M)\,\mathrm{ch}(E_A),
$$

故零模个数由规范场的拓扑所固定。在费米子路径积分中，每个零模都必须被一个费米子插入“吸收”（Grassmann 积分给出零，除非每个零模都被配对），故指标直接控制哪些关联函数非零——即 **'t Hooft 顶点**。

#### 手征反常

一个经典对称性在量子化后无法存续，就是一个**反常**。无质量费米子的**手征（轴）对称性** $\psi \to e^{i\alpha\gamma_5}\psi$ 在经典上守恒：轴流 $j_5^\mu = \bar\psi\gamma^\mu\gamma_5\psi$ 满足 $\partial_\mu j_5^\mu = 0$。在量子力学上它被破坏：

$$
\partial_\mu j_5^\mu = \frac{1}{16\pi^2}\,\epsilon^{\mu\nu\rho\sigma}\mathrm{tr}(F_{\mu\nu}F_{\rho\sigma}) = 2\,\big(\text{瞬子密度}\big).
$$

在时空上积分，轴荷的总变化等于 $2(n_+ - n_-) = 2\mathrm{ind}{D\!\!\!/}_A$。**Atiyah–Singer 定理是手征反常的数学内容**：反常的不守恒积分为指标，一个整数。右端恰是规范丛的 $\mathrm{ch}_2 = \tfrac12 c_1^2 - c_2$（s7），即第二 Chern 特征标——与指标公式中出现的同一个特征类。

> **典型联系。** 在 $S^4$ 上（紧化后的 Euclid 时空），$\hat A(S^4) = 1$（它是球面，$p_1 = 0$），故 $\mathrm{ind}{D\!\!\!/}_A = \int_{S^4}\mathrm{ch}_2(E_A) = \frac{1}{8\pi^2}\int \mathrm{tr}(F\wedge F)$，这就是**瞬子数**（第二 Chern 数）$k$。于是电荷为 $k$ 的瞬子背景恰有 $k$ 个净费米子零模。$SU(2)$ 基本表示中著名的“每个瞬子一个零模”就是 $k=1$ 时的这个公式。

#### 瞬子

一个**瞬子**是 Euclid Yang–Mills 方程的有限作用量解（纤维丛与规范指南）；其拓扑荷是整数 $k = \frac{1}{8\pi^2}\int\mathrm{tr}(F\wedge F) = c_2(E)[M]$，一个 Chern 数。指标定理说同一个整数计数该背景中的费米子零模，从而把以下三者联系起来：(i) 规范丛的拓扑（Chern 数），(ii) Dirac 算子的分析（零模），(iii) 量子反常（手征荷的不守恒）。这个数 $k$ 还经由另一个指标计算（线性化的自对偶算子）支配**瞬子模空间**的维数，对 $S^4$ 上的 $SU(2)$ 为 $8k - 3$——它本身就是一个 Atiyah–Singer 指标。标准模型与弦论中的反常相消条件（如 Green–Schwarz 机制），归根结底是说某些指标论的特征类之和为零。

> **直觉。** 每当物理学家说“这是受拓扑保护的”、“这个对称性是反常的”或“恰有 $k$ 个零模”，背后就有一个指标定理。物理无法改变的那个整数是分析指标，而拓扑是确定其值的东西。陷阱：*引力*反常涉及时空自身的 $\hat A(M)$，而不仅是规范丛；混合反常与纯引力反常是同一个 $\hat A\mathrm{ch}$ 多项式的更高次分量。

---

*本指南把指标理论从其分析的种子建立到其物理的繁花：一个 Fredholm 算子携带一个整数指标——解减去障碍——它在扰动下刚性不变（s1），而椭圆性（s2）加上紧流形上的椭圆正则性（s3）恰恰是使一个几何微分算子成为 Fredholm 的东西。de Rham 算子把 Euler 示性数实现为一个指标（s4），Hodge 理论把每个上同调类钉在唯一的调和代表元上（s5），而 Clifford 代数式的 Dirac 算子（s6）是其指标为 $\hat A$-亏格的范例。在拓扑的一面，Chern 特征标、Todd 类与 $\hat A$-亏格（s7）组装成一个曲率积分，而 Atiyah–Singer 定理（s8）宣布这个积分等于分析指标——把 Gauss–Bonnet、Hirzebruch 符号差与 Riemann–Roch 作为一族加以恢复（s9）。热核证明（s10）经由超对称相消与小时间定域化计算指标，而物理（s11）把整个结构读作反常、费米子零模与瞬子。把任意一个方框定义或编号证明当作参考随时返回，并把这唯一的论点放在眼前：一个自然方程的解的计数并非可以随意为何——拓扑把它固定，直到最后一个整数。*
