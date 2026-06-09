[English](differential-geometry.md) · **中文**

# 微分几何与张量，*广义相对论的语言。*

*一门自成体系、严谨的光滑空间几何入门课程。我们从流形这一最基本的概念出发——一个在近处看起来像平坦的 $\mathbb{R}^n$ 的空间——并一步步搭建出爱因斯坦所需的工具：切空间、张量、度量、联络、曲率，最终到达广义相对论的场方程。全程以几何为目标、以物理为动机；每一个公式都被推导，每一个指标都被解释。*

[← 返回全部指南](../README.zh.md)

**预备知识。** 本指南假定读者已掌握**线性代数**指南（向量空间、对偶空间、双线性形式、行列式）以及**多元/向量微积分**指南（偏导数、链式法则、雅可比矩阵、线积分与面积分）。我们会在用到所借用的具体事实时重新陈述它们。

## A 部分 · 光滑空间及其微积分

<a id="s0"></a>
### 动机 —— 弯曲时空与无坐标物理

微分几何是关于*光滑弯曲空间*的数学。本指南的核心动机源于物理：我们如何在一个并非平坦的 $\mathbb{R}^n$ 的空间上做微积分——求导、积分、守恒律——又如何书写物理定律，使它们不会暗中依赖于我们碰巧画出的坐标网格？

#### 我们要解决什么问题？

预备指南中所发展的向量微积分，活动于带有固定笛卡尔坐标系以及固定的"不同点处的相同方向"概念的 $\mathbb{R}^n$ 上。关于 $\mathbb{R}^n$ 的两个事实在那里悄悄承担了全部工作：

1. **全局坐标。** 每个点都有唯一一组数 $(x^1,\dots,x^n)$ 来标记它，并且处处同时有效。
2. **比较不同点处向量的一种典范方式。** 点 $p$ 处的向量与远处点 $q$ 处的向量都活在 $\mathbb{R}^n$ 的副本中，而我们默默地将它们等同起来，于是"梯度是常向量"或"这个向量场是均匀的"才有意义。

这两个事实在弯曲空间上都无法存活。在地球表面上，*不存在*任何无奇点的单一坐标图（每一张平面地球地图都会在某处发生畸变或撕裂）。而且也不存在与坐标无关的方式来说东京的风向量与伦敦的风向量"指向相同方向"：表面在它们之间弯曲了。

广义相对论把这一点变得具体。爱因斯坦的洞见在于：**引力不是一种力，而是时空的曲率**，并且物理定律在每一个坐标系中都必须取相同的形式——不存在优越参考系。要表达这样的定律，我们需要在更换坐标时以可预测方式变换的对象（这些就是**张量**）、一个内蕴于空间本身的距离概念（**度量**），以及一种尊重曲率的求导方式（**协变导数**）。曲率，编码在**黎曼张量**中，正是它使自由下落物体的路径发生弯曲；**爱因斯坦场方程**则把曲率与所在的物质和能量联系起来。

#### 计划

我们将按顺序搭建：**流形**（空间，s1）、**切向量**（无穷小箭头，s2）、**向量场与余向量**（s3）、**张量**（按变换律变换的多线性对象，s4）、**度量**（几何：长度与角度，s5）、**微分形式**与积分（s6–s7）、**联络与协变导数**（s8）、**测地线**（最直的路径，s9）、**曲率**（s10–s11）、**爱因斯坦方程**（s12），最后通过李导数与基灵向量讨论**对称性**（s13）。

> **直觉。** 心里始终装着两幅图景。*局部地*看，流形与平坦空间无法区分——在任何单一坐标图中微积分照常运作。*整体地*看，各坐标图必须被缝合在一起，而曲率正藏在这种缝合之中。张量微积分就是那套记账方法，它使局部计算与整体的、无坐标的真相保持一致。

<a id="s1"></a>
### 流形 —— 坐标图、图册与光滑结构

流形是"放大来看像 $\mathbb{R}^n$ 的空间"这一概念的精确化。球面、环面、机械臂的位形空间以及时空，都是流形。

#### 坐标图与图册

> **定义 —— 拓扑流形。**
>
> 一个 $n$ 维**拓扑流形** $M$ 是一个拓扑空间（带有开集概念的集合），它是 **豪斯多夫的**（不同的点有不相交的开邻域）、**第二可数的**（有可数的开集基），并且是 **$n$ 维局部欧氏的**：每个点 $p\in M$ 都有一个开邻域 $U$，以及一个到 $\mathbb{R}^n$ 某开子集上的同胚 $\varphi: U \to \varphi(U)\subseteq \mathbb{R}^n$。这对 $(U,\varphi)$ 称为**坐标图**；其分量函数 $\varphi(p)=(x^1(p),\dots,x^n(p))$ 称为**局部坐标**。

同胚是一个具有连续逆的连续双射，因此一个坐标图就是用 $n$ 个实数对 $M$ 的一小块进行的连续、可逆的标记。数 $n$ 是其**维数**。

> **定义 —— 图册与转移映射。**
>
> 一个**图册**是一族坐标图 $\{(U_\alpha,\varphi_\alpha)\}$，其定义域覆盖 $M$，即 $\bigcup_\alpha U_\alpha = M$。在两个坐标图重叠之处 $U_\alpha\cap U_\beta\ne\varnothing$，**转移映射**
>
> $$
> \varphi_\beta\circ\varphi_\alpha^{-1}:\ \varphi_\alpha(U_\alpha\cap U_\beta)\ \to\ \varphi_\beta(U_\alpha\cap U_\beta)
> $$
>
> 是 $\mathbb{R}^n$ 的开子集之间的映射——一个名副其实的 $n$ 个实变量的函数。

转移映射说明在重叠区上两套坐标网格如何彼此关联。它正是我们对其施加光滑性要求的对象。

> **定义 —— 光滑流形。**
>
> $M$ 上的一个**光滑（$C^\infty$）结构**是一个图册，其所有转移映射作为 $\mathbb{R}^n\to\mathbb{R}^n$ 的映射都是无穷次可微的，并且它是*极大的*（包含与之相容的每一个坐标图）。一个**光滑流形**是带有所选光滑结构的拓扑流形。函数 $f:M\to\mathbb{R}$ 是**光滑的**，如果对每个坐标图 $(U,\varphi)$，复合 $f\circ\varphi^{-1}:\varphi(U)\to\mathbb{R}$ 在通常微积分意义下是光滑的。我们用 $C^\infty(M)$ 记 $M$ 上光滑实函数的集合。

为何要求转移映射光滑？因为我们想要*通过坐标图*在 $M$ 上定义导数，而答案不能依赖于所用的坐标图。链式法则恰恰在转移映射可微时保证了一致性。这就是反复出现的主题：**$M$ 上的一个几何对象，是分坐标图的描述加上该描述在转移映射下如何变化的规则**，使得二者始终相符。

#### 范例 —— 用两个坐标图覆盖的 2-球面

设 $S^2=\{(X,Y,Z)\in\mathbb{R}^3 : X^2+Y^2+Z^2=1\}$，即单位球面。我们用**球极投影**给出一个由两个坐标图组成的光滑图册。

设 $N=(0,0,1)$ 为北极，$S=(0,0,-1)$ 为南极。

1. **从北极投影的坐标图。** 在 $U_N = S^2\setminus\{N\}$ 上，通过从 $N$ 向平面 $Z=0$ 投影来定义 $\varphi_N$。从 $N=(0,0,1)$ 出发经过 $(X,Y,Z)$ 的直线交 $Z=0$ 于
   $$
   \varphi_N(X,Y,Z) = (u,v) = \left(\frac{X}{1-Z},\ \frac{Y}{1-Z}\right).
   $$
   这是有定义的，因为在 $U_N$ 上 $Z\ne 1$，故 $1-Z\ne 0$。它是到整个 $\mathbb{R}^2$ 的同胚，其逆由该直线与球面相交得到。
2. **从南极投影的坐标图。** 在 $U_S = S^2\setminus\{S\}$ 上，通过从 $S=(0,0,-1)$ 投影来定义 $\varphi_S$：
   $$
   \varphi_S(X,Y,Z) = (a,b) = \left(\frac{X}{1+Z},\ \frac{Y}{1+Z}\right),
   $$
   有定义是因为在 $U_S$ 上 $Z\ne -1$。
3. **定义域覆盖 $S^2$。** 每个点至多不属于 $U_N,U_S$ 之一（只有 $N\notin U_N$，只有 $S\notin U_S$），而 $N\ne S$，因此 $U_N\cup U_S = S^2$。
4. **转移映射。** 在重叠区 $U_N\cap U_S = S^2\setminus\{N,S\}$ 上我们计算 $\varphi_S\circ\varphi_N^{-1}$。一个标准计算（把 $\varphi_N$ 的逆代入 $\varphi_S$，并利用 $X^2+Y^2+Z^2=1$）给出简洁的结果
   $$
   (a,b) = \frac{(u,v)}{u^2+v^2}.
   $$
   这是**关于单位圆的反演**。在重叠区上有 $(u,v)\ne(0,0)$（原点对应被排除的南极 $S$），故 $u^2+v^2>0$，该映射是光滑的——实际上每个分量都是分母不为零的多项式之比，因此由商法则知是 $C^\infty$ 的。

由于这唯一的转移映射是光滑的，$\{(U_N,\varphi_N),(U_S,\varphi_S)\}$ 是一个光滑图册，使 $S^2$ 成为光滑 2-流形。两个坐标图确实是必需的：没有任何单一坐标图能覆盖整个 $S^2$，因为 $S^2$ 是紧的，而它在 $\mathbb{R}^2$ 中的任何同胚像都将是开集，可以证明 $S^2$ 不同胚于 $\mathbb{R}^2$ 的任何开子集。

> **常见陷阱。** 坐标*不是*流形。点 $N$ 是 $S^2$ 中完全正当的一个点；它只是没有 $(u,v)$ 标号而已。像这样的"坐标奇点"是坐标图的产物，而非空间的产物。物理中时空奇点与坐标奇点之分正是这种区别（史瓦西视界是坐标产物；中心奇点则是真实的）。

<a id="s2"></a>
### 切向量与切空间

在流形的每一点，我们都想要一个由"无穷小方向"组成的向量空间——**切空间**。在 $\mathbb{R}^3$ 中的曲面上，这就是熟悉的切平面。但流形没有可以依托的周围空间，因此我们需要一个内蕴的定义。

#### 两幅等价的图景

有两个标准的内蕴定义；我们二者并用并证明它们一致。

> **定义 —— 经由曲线的切向量。**
>
> **过 $p$ 的光滑曲线**是光滑映射 $\gamma:(-\varepsilon,\varepsilon)\to M$，满足 $\gamma(0)=p$。两条曲线在 $p$ 处**等价**，如果在 $p$ 周围某个（等价地，每个）坐标图 $\varphi$ 中它们的坐标速度相等：$\tfrac{d}{dt}\big(\varphi\circ\gamma_1\big)(0) = \tfrac{d}{dt}\big(\varphi\circ\gamma_2\big)(0)$。**$p$ 处的切向量**就是曲线的一个等价类。

链式法则使"每个坐标图"等同于"某个坐标图"：在转移映射 $\psi=\varphi_\beta\circ\varphi_\alpha^{-1}$ 之下，速度按雅可比矩阵 $D\psi$ 变换，而它是可逆的，故两条曲线的速度在一个坐标图中相等当且仅当在所有坐标图中相等。

> **定义 —— 作为求导子的切向量。**
>
> **$p$ 处的求导子**是一个满足 **莱布尼茨（乘积）法则** 的线性映射 $v:C^\infty(M)\to\mathbb{R}$：
>
> $$
> v(fg) = v(f)\,g(p) + f(p)\,v(g)\qquad\text{for all }f,g\in C^\infty(M).
> $$
>
> **切空间** $T_pM$ 是 $p$ 处所有求导子的集合。在 $(v+w)(f)=v(f)+w(f)$ 与 $(cv)(f)=c\,v(f)$ 之下它是一个实向量空间。

其动机：切向量应当能让你对任意函数取*方向导数*。给定一条代表某方向的曲线 $\gamma$，定义 $v(f) = \tfrac{d}{dt}f(\gamma(t))\big|_{0}$。线性性显然；莱布尼茨法则就是 $\tfrac{d}{dt}\big(f(\gamma)g(\gamma)\big)$ 的普通乘积法则。

#### 坐标基

在 $p$ 周围固定一个坐标图 $\varphi=(x^1,\dots,x^n)$。定义 $n$ 个求导子：对 $\mu=1,\dots,n$，
$$
\left.\frac{\partial}{\partial x^\mu}\right|_p (f) \;=\; \frac{\partial (f\circ\varphi^{-1})}{\partial x^\mu}\Big|_{\varphi(p)} ,
$$
即 $f$ 的坐标表达式的普通偏导数。我们记 $\partial_\mu := \partial/\partial x^\mu$。

> **定理 —— 坐标基。**
>
> 求导子 $\partial_1|_p,\dots,\partial_n|_p$ 构成 $T_pM$ 的一组基；因此 $\dim T_pM = n = \dim M$。

*证明。*
1. **它们张成空间。** 设 $v\in T_pM$，$f\in C^\infty(M)$。在以 $p$ 为中心的坐标中工作（即 $\varphi(p)=0$）。把**带积分余项的泰勒定理**应用于 $f\circ\varphi^{-1}$，存在光滑函数 $g_\mu$，满足 $g_\mu(0)=\partial_\mu(f\circ\varphi^{-1})(0)$，使得在坐标中 $f = f(p) + \sum_\mu x^\mu\, g_\mu$。对其作用 $v$：由线性性，$v(f) = v(f(p)) + \sum_\mu v(x^\mu g_\mu)$。常数 $f(p)$ 满足 $v(\text{const})=0$（把莱布尼茨法则应用于 $1=1\cdot 1$：$v(1)=v(1)+v(1)$，故 $v(1)=0$，于是 $v(c)=0$）。由莱布尼茨法则，$v(x^\mu g_\mu)=v(x^\mu)g_\mu(p)+x^\mu(p)v(g_\mu)$，而 $x^\mu(p)=0$，故这等于 $v(x^\mu)\,\partial_\mu f|_p$。因此 $v(f)=\sum_\mu v(x^\mu)\,\partial_\mu|_p(f)$，即 $v=\sum_\mu v(x^\mu)\,\partial_\mu|_p$。所以 $\partial_\mu$ 张成空间。
2. **它们线性无关。** 设 $\sum_\mu c^\mu \partial_\mu|_p = 0$ 作为求导子成立。将其作用于坐标函数 $x^\nu$：$\partial_\mu|_p(x^\nu) = \delta^\nu_\mu$（$x^\nu$ 关于 $x^\mu$ 的偏导数）。故对每个 $\nu$ 有 $0 = \sum_\mu c^\mu \delta^\nu_\mu = c^\nu$。所有系数皆为零。

因此 $\partial_\mu$ 是一组基。$\blacksquare$

我们用**爱因斯坦求和约定**（在 s4 中完整引入）把一般切向量写成 $v = v^\mu \partial_\mu$：一个重复的指标，一上一下，便对 $1,\dots,n$ 求和。数 $v^\mu = v(x^\mu)$ 是 $v$ 在此坐标图中的**分量**。

#### 分量如何变换

若 $\tilde x^\nu$ 是另一个坐标图，链式法则给出 $\partial_\mu = \dfrac{\partial \tilde x^\nu}{\partial x^\mu}\,\tilde\partial_\nu$，将 $v=v^\mu\partial_\mu = \tilde v^\nu \tilde\partial_\nu$ 相匹配便得到**逆变变换律**
$$
\tilde v^\nu = \frac{\partial \tilde x^\nu}{\partial x^\mu}\, v^\mu .
$$
这就是"向量"变换的原型；分量以这种方式（带*上方*雅可比因子）变换的对象称为**逆变的**，以一个上指标标记。

> **范例 —— 球面的切空间。** 在 $S^2$ 北极坐标图 $(u,v)$ 中，曲线 $\gamma(t)=\varphi_N^{-1}(t,0)$ 在 $t=0$ 处的速度就是基向量 $\partial_u|_p$。切向量 $3\partial_u - \partial_v$ 的分量为 $(v^u,v^v)=(3,-1)$；它是球面切平面中一个真正的箭头，其表达完全不需离开曲面。

<a id="s3"></a>
### 向量场、前推与余向量（1-形式）

现在我们给*每一个*点都附上一个切向量，学习映射如何搬动切向量，并认识其对偶对象——余向量。

#### 向量场

> **定义 —— 向量场。**
>
> 一个**（光滑）向量场** $X$ 光滑地给每个 $p\in M$ 指派一个切向量 $X_p\in T_pM$：在任何坐标图中，$X = X^\mu(x)\,\partial_\mu$，其分量函数 $X^\mu$ 光滑。等价地，$X$ 作用于一个函数给出一个函数：$(Xf)(p)=X_p(f)\in\mathbb{R}$，且 $Xf\in C^\infty(M)$。

向量场可以相加、被函数数乘，并且——这是关键——通过**李括号** $[X,Y]f := X(Yf)-Y(Xf)$ 相乘，其结果仍是一个向量场（由混合偏导相等，二阶项相消）。我们将在 s13 中回到李括号。

#### 映射的微分（前推）

> **定义 —— 前推 / 微分。**
>
> 设 $F:M\to N$ 光滑，$p\in M$。**微分**（或**前推**）$dF_p = F_{*p}:T_pM\to T_{F(p)}N$ 对切向量 $v$（视为求导子）的作用定义为
>
> $$
> \big(dF_p(v)\big)(g) = v(g\circ F)\qquad\text{for } g\in C^\infty(N).
> $$

在曲线图景中这是最自然不过的：若 $v=[\gamma]$，则 $dF_p(v)=[F\circ\gamma]$——像曲线的速度。在 $M$ 上的坐标 $x^\mu$ 与 $N$ 上的坐标 $y^a$ 中，$F$ 由 $y^a=F^a(x)$ 给出，$dF_p$ 的矩阵就是**雅可比矩阵** $\partial F^a/\partial x^\mu$：
$$
\big(dF_p(v)\big)^a = \frac{\partial F^a}{\partial x^\mu}\, v^\mu .
$$
*为何如此：* 把定义应用于 $g=y^a$ 并用链式法则。前推就是雅可比矩阵的无坐标版本。（除非 $F$ 可逆，否则一般无法把向量*拉回*；但函数和余向量可以自由拉回，这正是余向量如此有用的原因。）

#### 余向量与余切空间

> **定义 —— 余切空间与余向量。**
>
> **余切空间** $T_p^*M$ 是 $T_pM$ 的对偶向量空间：线性映射 $\omega:T_pM\to\mathbb{R}$ 的集合。它的元素称为**余向量**（也称一点处的**1-形式**，或**协变向量**）。

回忆线性代数中的结论：$n$ 维空间的对偶仍是 $n$ 维的，且 $V$ 的一组基 $\{e_\mu\}$ 诱导出 $V^*$ 的一组**对偶基** $\{e^\mu\}$，由 $e^\mu(e_\nu)=\delta^\mu_\nu$ 定义。

> **定义 —— 函数的微分，以及对偶基 $dx^\mu$。**
>
> 对 $f\in C^\infty(M)$，其**微分** $df_p\in T_p^*M$ 是余向量 $df_p(v) = v(f)$。应用于坐标函数 $x^\mu$，便给出余向量 $dx^\mu$，满足
>
> $$
> dx^\mu(\partial_\nu) = \partial_\nu(x^\mu) = \delta^\mu_\nu .
> $$

所以 $\{dx^\mu\}$ 恰好是坐标基 $\{\partial_\mu\}$ 的对偶基。每个余向量都是 $\omega = \omega_\mu\, dx^\mu$，其分量为 $\omega_\mu=\omega(\partial_\mu)$（下指标）。对函数，$df = \partial_\mu f\, dx^\mu$——微分就是以不变方式写出的梯度。

#### 余向量分量如何变换

由 $dx^\mu = \dfrac{\partial x^\mu}{\partial \tilde x^\nu} d\tilde x^\nu$ 并匹配分量，**协变变换律**为
$$
\tilde\omega_\nu = \frac{\partial x^\mu}{\partial \tilde x^\nu}\,\omega_\mu .
$$
与向量的逆变律相比较：余向量以*逆*雅可比因子（下指标）变换，向量以*正*雅可比因子（上指标）变换。这种相反的行为正是配对 $\omega(v)=\omega_\mu v^\mu$ **与坐标无关**的原因：两个雅可比因子由链式法则 $\frac{\partial x^\mu}{\partial \tilde x^\nu}\frac{\partial \tilde x^\nu}{\partial x^\rho}=\delta^\mu_\rho$ 相乘得到单位。这种不变性是全部张量微积分的种子。

## B 部分 · 张量与度量

<a id="s4"></a>
### 张量 —— 变换律、指标记号、记账的尺度

张量是由切空间与余切空间的若干副本构造出的多线性对象。张量是物理定律所用的器件，因为它们的变换律使张量间的方程在*所有*坐标系中同时成立。

#### 定义

> **定义 —— 一点处的张量。**
>
> $p$ 处的一个 **$(k,l)$ 型张量** 是一个多线性映射
>
> $$
> T:\ \underbrace{T_p^*M\times\cdots\times T_p^*M}_{k}\ \times\ \underbrace{T_pM\times\cdots\times T_pM}_{l}\ \longrightarrow\ \mathbb{R},
> $$
>
> 它对其 $k+l$ 个槽位中的每一个都是线性的。一个**张量场**光滑地给每一点指派这样一个张量。

例子：一个 $(1,0)$ 型张量吞掉一个余向量，它就是一个向量（由二次对偶 $V^{**}\cong V$）；一个 $(0,1)$ 型张量是一个余向量；一个 $(0,2)$ 型张量是一个双线性形式（度量将是其中之一）。

#### 分量与指标记号

把基元素送入槽位即得**分量**。对一个 $(k,l)$ 型张量，
$$
T^{\mu_1\cdots\mu_k}{}_{\nu_1\cdots\nu_l} = T\big(dx^{\mu_1},\dots,dx^{\mu_k},\,\partial_{\nu_1},\dots,\partial_{\nu_l}\big).
$$
上指标（"逆变槽"）与余向量参数配对；下指标（"协变槽"）与向量参数配对。整个张量可如下复原
$$
T = T^{\mu_1\cdots\mu_k}{}_{\nu_1\cdots\nu_l}\ \partial_{\mu_1}\otimes\cdots\otimes\partial_{\mu_k}\otimes dx^{\nu_1}\otimes\cdots\otimes dx^{\nu_l},
$$
其中 $\otimes$ 是线性代数中的张量积。

> **爱因斯坦求和约定。** 在单一一项中恰好**出现两次、一上一下的指标会自动对 $1,\dots,n$ 求和**；求和号被省略。这样的指标称为**缩并的**（或"哑指标"），可以自由更名。未重复的指标是**自由的**，在方程两边必须匹配。例如：$\omega_\mu v^\mu$ 表示 $\sum_{\mu=1}^n \omega_\mu v^\mu$；方程 $w^\mu = A^\mu{}_\nu v^\nu$ 有自由指标 $\mu$ 与求和指标 $\nu$。

#### 变换律

定义性质——使张量成为张量的东西——就是在更换坐标图时分量如何变化。每个上指标带来一个因子 $\partial\tilde x/\partial x$（像向量），每个下指标带来一个因子 $\partial x/\partial\tilde x$（像余向量）：
$$
\tilde T^{\alpha_1\cdots\alpha_k}{}_{\beta_1\cdots\beta_l}
= \frac{\partial \tilde x^{\alpha_1}}{\partial x^{\mu_1}}\cdots\frac{\partial \tilde x^{\alpha_k}}{\partial x^{\mu_k}}\,
\frac{\partial x^{\nu_1}}{\partial \tilde x^{\beta_1}}\cdots\frac{\partial x^{\nu_l}}{\partial \tilde x^{\beta_l}}\,
T^{\mu_1\cdots\mu_k}{}_{\nu_1\cdots\nu_l}.
$$
这直接由多线性性以及 s2–s3 的基变换律得出。反之，一个服从此律的数组*定义*了一个张量——这是实用的、"物理学家式"的定义，我们将不断使用它。

> **为何重要。** 若一个张量的分量在某个坐标图中全为零，则变换律（关于 $T$ 是线性且齐次的）使它们在*每个*坐标图中都为零。因此 **一旦在某个坐标系中验证了张量方程 $A=B$，它就在所有坐标系中成立。** 这正是"物理定律在每个参考系中相同"的数学内涵。

#### 运算：缩并与升降指标

- **缩并**令一个上指标与一个下指标相等并求和，使型降低 $(1,1)$。例如，由 $T^\mu{}_\nu$ 得到的**迹** $T^\mu{}_\mu$ 是一个标量，在坐标变换下不变（雅可比因子如 s3 那样相消）。
- **升降指标**使用度量（见下一节）：$V_\mu = g_{\mu\nu}V^\nu$ 下降，$V^\mu = g^{\mu\nu}V_\nu$ 上升，其中 $g^{\mu\nu}$ 是逆度量。由于 $g$ 是张量，这些运算与坐标无关。

> **常见陷阱。** $df$ 的分量 $\partial_\mu f$ 构成一个余向量（下指标），*而非*向量，尽管我们称它为"梯度"。要把它变成向量（最陡上升的方向）需要用度量升指标：$(\mathrm{grad} f)^\mu = g^{\mu\nu}\partial_\nu f$。在平坦笛卡尔空间中 $g^{\mu\nu}=\delta^{\mu\nu}$，所以这种区别不可见——这正是它常被忽视的原因。

<a id="s5"></a>
### 度量张量 —— 长度、角度与指标体操

度量是将一个赤裸的光滑流形升级为*几何*的东西：它使我们能够测量曲线的长度、向量间的夹角、面积与体积。在相对论中，度量*就是*引力场。

#### 定义

> **定义 —— （伪）黎曼度量。**
>
> 一个**度量** $g$ 是一个光滑的 $(0,2)$ 型张量场，它在每一点都是**对称的**（$g(v,w)=g(w,v)$）且**非退化的**（若对一切 $w$ 有 $g(v,w)=0$，则 $v=0$）。若另外对一切 $v\ne0$ 有 $g(v,v)>0$，则它是**黎曼的**（每个 $T_pM$ 上的真正内积）；若 $g$ 的符号差为 $(-,+,+,+)$，则它是**洛伦兹的**，即时空的情形。分量：$g_{\mu\nu}=g(\partial_\mu,\partial_\nu)$，一个对称矩阵。

#### 线元

度量最常通过**线元** $ds^2$ 来书写，它是无穷小位移 $dx^\mu$ 的平方长度：
$$
ds^2 = g_{\mu\nu}\,dx^\mu\,dx^\nu .
$$
曲线 $\gamma:[a,b]\to M$ 的**长度**，其坐标速度为 $\dot x^\mu = dx^\mu/dt$，则为
$$
L[\gamma] = \int_a^b \sqrt{\,g_{\mu\nu}(\gamma(t))\,\dot x^\mu \dot x^\nu\,}\; dt ,
$$
（对洛伦兹度量则按符号约定使用 $|g_{\mu\nu}\dot x^\mu\dot x^\nu|$）。向量 $v,w$ 间的**夹角** $\theta$ 来自 $\cos\theta = g(v,w)/\sqrt{g(v,v)\,g(w,w)}$，正是线性代数中的内积公式。

#### 逆度量与指标体操

由于 $g_{\mu\nu}$ 非退化，矩阵 $(g_{\mu\nu})$ 可逆。其逆定义了**逆度量** $g^{\mu\nu}$，一个对称的 $(2,0)$ 型张量，由
$$
g^{\mu\rho}g_{\rho\nu} = \delta^\mu_\nu
$$
给出。先降后升回到原来：$g^{\mu\rho}(g_{\rho\nu}V^\nu) = g^{\mu\rho}V_\rho = V^\mu$。正是这种一致性使得用 $g$ 升降指标良定义。

#### 范例 1 —— 极坐标下的平坦平面

从 $ds^2 = dx^2 + dy^2$（欧氏）出发，其中 $x=r\cos\theta$，$y=r\sin\theta$。

1. 微分：$dx = \cos\theta\,dr - r\sin\theta\,d\theta$，$dy=\sin\theta\,dr + r\cos\theta\,d\theta$（乘积与链式法则）。
2. 平方再相加。交叉项 $dr\,d\theta$ 的系数为 $2(-\cos\theta\sin\theta\, r + \sin\theta\cos\theta\, r)=0$。$dr^2$ 的系数为 $\cos^2\theta+\sin^2\theta=1$；$d\theta^2$ 的系数为 $r^2(\sin^2\theta+\cos^2\theta)=r^2$。
3. 因此
   $$
   ds^2 = dr^2 + r^2\,d\theta^2,\qquad (g_{\mu\nu}) = \begin{pmatrix} 1 & 0 \\ 0 & r^2\end{pmatrix},\qquad (g^{\mu\nu})=\begin{pmatrix}1 & 0 \\ 0 & r^{-2}\end{pmatrix}.
   $$
此空间仍是平坦的（我们将在 s10 中确认曲率为零）；那个 $r^2$ 是弯曲*坐标*的产物，而非弯曲*空间*的产物。

#### 范例 2 —— 圆球面

在 $S^2$ 上取纬度–经度坐标图（余纬 $\theta\in(0,\pi)$，经度 $\phi$），嵌入为 $(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta)$，同样的微分给出**半径为 1 的圆球度量**：
$$
ds^2 = d\theta^2 + \sin^2\theta\, d\phi^2,\qquad (g_{\mu\nu})=\begin{pmatrix}1&0\\0&\sin^2\theta\end{pmatrix}.
$$
这个度量*是*弯曲的——不存在能把它整体变为 $d\theta^2+d\phi^2$ 的坐标变换，这正是每一张平面地球地图都会畸变的精确原因。我们将在 s10 中证明其曲率非零。

> **直觉。** 度量是一个"标尺场"：在每一点它告诉你如何把坐标差转换为真实距离。更换坐标会改变标尺的分量，但不改变它所测的距离——距离是不变量，分量只是记账。

## C 部分 · 形式与积分

<a id="s6"></a>
### 微分形式、楔积与外微分

微分形式是*完全反对称的*协变张量。它们恰是无需额外结构便能在流形上积分的对象，并且把梯度、旋度、散度以及微积分基本定理统一为单一算子 $d$。

#### 形式与楔积

> **定义 —— $k$-形式。**
>
> 一个 **$k$-形式** 是一个**交错的** $(0,k)$ 型张量场：当交换任意两个参数时它变号（因此当两个参数重合时它为零）。$0$-形式是函数；$1$-形式是余向量场。

> **定义 —— 楔积。**
>
> $k$-形式 $\alpha$ 与 $l$-形式 $\beta$ 的**楔积**是将张量积 $\alpha\otimes\beta$ 反对称化所得的 $(k+l)$-形式。在基 1-形式上它由 $dx^\mu\wedge dx^\nu = -\,dx^\nu\wedge dx^\mu$（故 $dx^\mu\wedge dx^\mu=0$）生成，并按双线性与结合律延拓。它是**分次交换的**：$\alpha\wedge\beta = (-1)^{kl}\beta\wedge\alpha$。

每个 $k$-形式都是 $\omega = \tfrac{1}{k!}\,\omega_{\mu_1\cdots\mu_k}\,dx^{\mu_1}\wedge\cdots\wedge dx^{\mu_k}$，其分量完全反对称。在 $n$ 维流形上，最高次数为 $n$：不存在非零的 $(n+1)$-形式，因为必有某个指标重复。

#### 外微分

> **定义 —— 外微分。**
>
> **外微分** $d$ 把 $k$-形式映为 $(k+1)$-形式。在 $0$-形式（函数）$f$ 上它是微分 $df = \partial_\mu f\,dx^\mu$。在一般形式 $\omega = \tfrac1{k!}\omega_{\mu_1\cdots\mu_k}dx^{\mu_1}\wedge\cdots\wedge dx^{\mu_k}$ 上，
>
> $$
> d\omega = \frac1{k!}\,\partial_\nu \omega_{\mu_1\cdots\mu_k}\; dx^\nu\wedge dx^{\mu_1}\wedge\cdots\wedge dx^{\mu_k}.
> $$
>
> 它是线性的，并对 $k$-形式 $\alpha$ 服从**分次莱布尼茨法则** $d(\alpha\wedge\beta) = d\alpha\wedge\beta + (-1)^{k}\alpha\wedge d\beta$。

#### 定理：$d^2 = 0$

> **定理。** 对每个形式 $\omega$，$d(d\omega)=0$。

*证明。* 只需在 $0$-形式上证明它并通过莱布尼茨法则传播即可；我们通过在函数上展示其机理直接给出（高次情形逐指标重复同样的论证）。
1. 设 $f$ 为函数。则 $df = \partial_\mu f\, dx^\mu$，一个 $1$-形式。
2. 用定义再次作用 $d$：$d(df) = \partial_\nu\partial_\mu f\; dx^\nu\wedge dx^\mu$，对 $\mu,\nu$ 求和。
3. 把双重和拆为对称系数与反对称基。系数 $\partial_\nu\partial_\mu f$ 由 **克莱罗/施瓦茨定理**（光滑函数混合偏导相等）**关于 $\mu,\nu$ 对称**。基因子 $dx^\nu\wedge dx^\mu$ 由楔积法则**关于 $\mu,\nu$ 反对称**。
4. 对所有 $\mu,\nu$ 求和的（关于 $\mu\nu$ 对称）乘以（关于 $\mu\nu$ 反对称）为零：交换哑名 $\mu\leftrightarrow\nu$ 使对称因子不变而反对称因子变号，故该和等于自身的相反数，因此为 $0$。具体地 $\sum_{\mu,\nu}\partial_\nu\partial_\mu f\,dx^\nu\wedge dx^\mu = \tfrac12\sum_{\mu,\nu}(\partial_\nu\partial_\mu f-\partial_\mu\partial_\nu f)\,dx^\nu\wedge dx^\mu = 0$。
5. 对一般的 $k$-形式，额外的外因子 $dx^{\mu_1}\wedge\cdots$ 原封不动地随行，而对两个新的求导指标的同样的对称乘反对称相消给出 $d(d\omega)=0$。$\blacksquare$

> **与向量微积分的联系。** 在 $\mathbb{R}^3$ 中：$d$ 作用于 $0$-形式是 $\mathrm{grad}$；作用于 $1$-形式是 $\mathrm{curl}$；作用于 $2$-形式是 $\mathrm{div}$。于是 $d^2=0$ 一举编码了两个经典恒等式 $\mathrm{curl}\,\mathrm{grad}=0$ 与 $\mathrm{div}\,\mathrm{curl}=0$。这正是形式之所以是自然语言的原因。

<a id="s7"></a>
### 形式的积分与广义斯托克斯定理

$k$-形式*恰好*是你要在 $k$ 维区域上积分的那种对象，因为它的反对称性正是为匹配积分的定向敏感性而生（交换两个坐标会同时翻转形式与体积元的符号，故积分良定义且能感知定向）。

#### 积分

在一个定向的 $n$ 维流形上，一个最高次（$n$-）形式 $\omega = h\,dx^1\wedge\cdots\wedge dx^n$ 逐坐标图地作为普通重积分 $\int h\,dx^1\cdots dx^n$ 来积分。**换元定理**保证这与坐标图无关：在坐标变换下，形式的系数会带上雅可比行列式，恰好抵消重积分代换法则中的雅可比因子。（这正是形式而非任意张量才是被积对象的深层原因：行列式才是那个反对称的对象。）要在一个 $k$ 维子流形上对一个 $k$-形式积分，**把它拉回**到参数域并在那里积分。

#### 广义斯托克斯定理

> **定理 —— 斯托克斯定理。**
>
> 设 $M$ 是带边界 $\partial M$ 的定向光滑 $n$ 维流形（$\partial M$ 取诱导定向），$\omega$ 是一个具紧支集的 $(n-1)$-形式。则
>
> $$
> \int_M d\omega = \int_{\partial M}\omega .
> $$

其证明通过单位分解与坐标图归结为半空间情形，在那里它就是逐个坐标地应用的微积分基本定理。这单一陈述特殊化为各经典定理：

- **$n=1$：** 取 $\omega=f$ 为 $[a,b]$ 上的 $0$-形式，$\int_a^b df = f(b)-f(a)$——**微积分基本定理**。
- **$n=2$：** **格林定理**。
- **$n=3$，$(n-1)$-形式：** **散度定理**；对曲面上的 $1$-形式，则是 **开尔文–斯托克斯（旋度）定理**。

于是向量微积分的所有积分定理都是同一个定理：*导数在一个区域上的积分等于原函数在边界上的取值。*

#### 关于德拉姆上同调的几句话

一个形式 $\omega$ 称为**闭的**，如果 $d\omega=0$；称为**恰当的**，如果对某个 $\eta$ 有 $\omega=d\eta$。由于 $d^2=0$（s6），每个恰当形式都是闭的。反之则可能失败，而这种失败度量了 $M$ 的**洞**：
$$
H^k_{\mathrm{dR}}(M) = \frac{\{\text{closed }k\text{-forms}\}}{\{\text{exact }k\text{-forms}\}} .
$$
**德拉姆上同调** $H^k_{\mathrm{dR}}(M)$ 是一个向量空间，其维数计数 $k$ 维的洞。经典例子：在 $\mathbb{R}^2\setminus\{0\}$ 上，角形式 $\omega=\tfrac{-y\,dx+x\,dy}{x^2+y^2}$ 是闭的（$d\omega=0$）但不恰当（它绕原点的环路积分为 $2\pi\ne0$，而由斯托克斯定理恰当形式沿闭环积分为 $0$）。德拉姆定理把 $H^k_{\mathrm{dR}}(M)$ 与 $M$ 的拓扑上同调等同起来——这是微积分与拓扑之间的一座桥梁。

## D 部分 · 联络与曲率

<a id="s8"></a>
### 协变导数与克里斯托弗符号

要对向量场求导，我们必须比较*不同*点处的向量——但它们活在不同的切空间中，且（s0）不存在典范的等同。提供这种等同的额外结构就是**联络**，由此得到的导数就是**协变导数** $\nabla$。

#### 为何 $\partial_\mu V^\nu$ 不是张量

对向量变换律 $\tilde V^\alpha = \frac{\partial\tilde x^\alpha}{\partial x^\mu}V^\mu$ 求导。由乘积法则，
$$
\tilde\partial_\beta \tilde V^\alpha = \frac{\partial x^\nu}{\partial\tilde x^\beta}\frac{\partial \tilde x^\alpha}{\partial x^\mu}\,\partial_\nu V^\mu \;+\; \frac{\partial x^\nu}{\partial\tilde x^\beta}\frac{\partial^2 \tilde x^\alpha}{\partial x^\nu\partial x^\mu}V^\mu .
$$
第一项是 $(1,1)$ 型张量的变换律；**第二项**带有坐标变换的二阶导数，破坏了它。故向量场的朴素偏导数*不是*张量。我们需要一个恰好抵消这堆废料的修正项。

#### 联络

> **定义 —— 仿射联络 / 协变导数。**
>
> 一个**联络** $\nabla$ 给向量场指派一个作用于张量场的协变导数 $\nabla_\mu$，它是线性的、服从莱布尼茨法则，并在函数上退化为 $\partial_\mu$。在向量场上它的分量是
>
> $$
> \nabla_\mu V^\nu = \partial_\mu V^\nu + \Gamma^\nu{}_{\mu\rho}\,V^\rho,
> $$
>
> 其中 $\Gamma^\nu{}_{\mu\rho}$ 是**联络系数**（当由度量导出时即**克里斯托弗符号**）。在余向量上：$\nabla_\mu \omega_\nu = \partial_\mu\omega_\nu - \Gamma^\rho{}_{\mu\nu}\omega_\rho$。符号由要求 $\nabla_\mu(\omega_\nu V^\nu)=\partial_\mu(\omega_\nu V^\nu)$ 确定，因为 $\omega_\nu V^\nu$ 是标量。

为使 $\nabla_\mu V^\nu$ 成为张量，$\Gamma$ 本身必须*非齐次地*变换，带一个恰好抵消上述讨厌项的二阶导数项。（因此 $\Gamma$ *不是*张量——它非张量性的变换正是其全部要义。）

#### 列维-奇维塔联络：从度量导出克里斯托弗符号

在（伪）黎曼流形上存在唯一的自然联络。

> **定理（黎曼几何基本定理）。** 存在唯一的联络，它是
> - **与度量相容的：** $\nabla_\mu g_{\nu\rho}=0$（长度和角度在平行移动下被保持），并且
> - **无挠的（对称的）：** $\Gamma^\rho{}_{\mu\nu}=\Gamma^\rho{}_{\nu\mu}$。
>
> 它的系数，即**克里斯托弗符号**，为
>
> $$
> \Gamma^\rho{}_{\mu\nu} = \tfrac12\, g^{\rho\sigma}\big(\partial_\mu g_{\sigma\nu} + \partial_\nu g_{\sigma\mu} - \partial_\sigma g_{\mu\nu}\big).
> $$

*推导。*
1. 三次写出度量相容性，循环置换指标：
   $$
   \partial_\mu g_{\nu\rho} = \Gamma^\sigma{}_{\mu\nu}g_{\sigma\rho} + \Gamma^\sigma{}_{\mu\rho}g_{\nu\sigma}\quad(\text{i}),
   $$
   $$
   \partial_\nu g_{\rho\mu} = \Gamma^\sigma{}_{\nu\rho}g_{\sigma\mu} + \Gamma^\sigma{}_{\nu\mu}g_{\rho\sigma}\quad(\text{ii}),
   $$
   $$
   \partial_\rho g_{\mu\nu} = \Gamma^\sigma{}_{\rho\mu}g_{\sigma\nu} + \Gamma^\sigma{}_{\rho\nu}g_{\mu\sigma}\quad(\text{iii}),
   $$
   每一式都通过展开 $0=\nabla_\mu g_{\nu\rho}=\partial_\mu g_{\nu\rho}-\Gamma^\sigma{}_{\mu\nu}g_{\sigma\rho}-\Gamma^\sigma{}_{\mu\rho}g_{\nu\sigma}$ 并整理得到。
2. 计算 (i) + (ii) − (iii)。利用**对称性** $\Gamma^\sigma{}_{\mu\nu}=\Gamma^\sigma{}_{\nu\mu}$ 以及对称性 $g_{\sigma\rho}=g_{\rho\sigma}$，六个 $\Gamma g$ 项中有四个成对相消，剩下
   $$
   \partial_\mu g_{\nu\rho} + \partial_\nu g_{\rho\mu} - \partial_\rho g_{\mu\nu} = 2\,\Gamma^\sigma{}_{\mu\nu}\,g_{\sigma\rho}.
   $$
3. 用逆度量 $g^{\rho\lambda}$（由 s5 存在）缩并并利用 $g^{\rho\lambda}g_{\sigma\rho}=\delta^\lambda_\sigma$ 解出 $\Gamma$：
   $$
   \Gamma^\lambda{}_{\mu\nu} = \tfrac12\, g^{\lambda\rho}\big(\partial_\mu g_{\nu\rho}+\partial_\nu g_{\rho\mu}-\partial_\rho g_{\mu\nu}\big),
   $$
   这就是所断言的公式（把 $\rho\to\sigma$、$\lambda\to\rho$ 更名）。唯一性由每一步都是被迫的而得；存在性，则因为这个公式确实定义了一个与度量相容的无挠联络（代回检验即可）。$\blacksquare$

#### 范例 —— 极坐标下平面的克里斯托弗符号

由 $g_{rr}=1$，$g_{\theta\theta}=r^2$，$g^{rr}=1$，$g^{\theta\theta}=r^{-2}$（非对角元为零），唯一非零的度量导数是 $\partial_r g_{\theta\theta}=2r$。该公式给出：
$$
\Gamma^r{}_{\theta\theta} = \tfrac12 g^{rr}(-\partial_r g_{\theta\theta}) = -r,\qquad
\Gamma^\theta{}_{r\theta}=\Gamma^\theta{}_{\theta r} = \tfrac12 g^{\theta\theta}\partial_r g_{\theta\theta} = \tfrac{1}{r},
$$
其余皆为零。这些正是极坐标加速度 $\ddot r - r\dot\theta^2$ 与 $\ddot\theta + \tfrac2r\dot r\dot\theta$ 中熟悉的那些项——"虚拟的"离心项与科里奥利项就是克里斯托弗符号。

<a id="s9"></a>
### 平行移动与测地线

**测地线**是流形对"直线"的概念。有两种方式把它精确化——*最直*（零转向）与*最短*（极值长度）——而列维-奇维塔联络使二者一致。

#### 平行移动

> **定义 —— 平行移动。**
>
> 向量场 $V$ 沿曲线 $x^\mu(\lambda)$ **平行移动**，如果它沿该曲线的协变导数为零：
>
> $$
> \frac{DV^\mu}{d\lambda} := \dot x^\nu\nabla_\nu V^\mu = \frac{dV^\mu}{d\lambda} + \Gamma^\mu{}_{\nu\rho}\,\dot x^\nu V^\rho = 0 .
> $$

这就是联络所承诺的规则——"在弯曲空间所允许的范围内尽量保持向量不变地携带它"。度量相容性确保长度和角度在移动下被保持。

#### 测地线作为最直的路径

> **定义 —— 测地线（最直）。** 一条曲线是**测地线**，如果它平行移动自身的切向量：$\frac{D\dot x^\mu}{d\lambda}=0$。显式地，
>
> $$
> \boxed{\ \ddot x^\mu + \Gamma^\mu{}_{\nu\rho}\,\dot x^\nu\dot x^\rho = 0\ }
> $$
>
> 即**测地线方程**，其中点表示对**仿射参数** $\lambda$ 的 $d/d\lambda$。

这就是"走直线：别转弯"。$\Gamma$ 项是把真正的转向与坐标网格的弯曲区别开来的修正。

#### 测地线作为最短的路径 —— 经由变分法的推导

我们现在通过对长度取极值来推导*同一个*方程，确认这两个概念重合。

弧长是 $L=\int \sqrt{g_{\mu\nu}\dot x^\mu\dot x^\nu}\,d\lambda$。在技术上更干净（且当 $\lambda$ 为仿射参数时对极值曲线等价）的做法是对**能量泛函** $S=\int \mathcal{L}\,d\lambda$ 取极值，其中 $\mathcal{L}=\tfrac12 g_{\mu\nu}(x)\dot x^\mu\dot x^\nu$。

1. **欧拉–拉格朗日方程。** $S$ 的极值曲线对每个坐标 $x^\sigma$ 满足欧拉–拉格朗日方程 $\frac{d}{d\lambda}\frac{\partial\mathcal L}{\partial\dot x^\sigma} - \frac{\partial\mathcal L}{\partial x^\sigma}=0$（标准变分法：对一切固定端点的扰动，一阶变分为零）。
2. **计算 $\partial\mathcal L/\partial\dot x^\sigma$。** 由于 $\mathcal L=\tfrac12 g_{\mu\nu}\dot x^\mu\dot x^\nu$ 且 $g$ 不依赖于 $\dot x$，对 $\dot x^\sigma$ 求导（它命中两个速度因子中的每一个）并利用对称性 $g_{\mu\nu}=g_{\nu\mu}$ 给出 $\partial\mathcal L/\partial\dot x^\sigma = g_{\sigma\nu}\dot x^\nu$。
3. **时间导数。** $\frac{d}{d\lambda}\big(g_{\sigma\nu}\dot x^\nu\big) = (\partial_\mu g_{\sigma\nu})\dot x^\mu\dot x^\nu + g_{\sigma\nu}\ddot x^\nu$，由乘积与链式法则（$g$ 经由 $x(\lambda)$ 依赖于 $\lambda$）。
4. **计算 $\partial\mathcal L/\partial x^\sigma$。** 只有 $g_{\mu\nu}$ 依赖于位置：$\partial\mathcal L/\partial x^\sigma = \tfrac12(\partial_\sigma g_{\mu\nu})\dot x^\mu\dot x^\nu$。
5. **组装。** 欧拉–拉格朗日方程变为
   $$
   g_{\sigma\nu}\ddot x^\nu + (\partial_\mu g_{\sigma\nu})\dot x^\mu\dot x^\nu - \tfrac12(\partial_\sigma g_{\mu\nu})\dot x^\mu\dot x^\nu = 0 .
   $$
6. **对中间项对称化。** 由于 $\dot x^\mu\dot x^\nu$ 关于 $\mu,\nu$ 对称，我们可以把 $(\partial_\mu g_{\sigma\nu})\dot x^\mu\dot x^\nu$ 替换为其对称化 $\tfrac12(\partial_\mu g_{\sigma\nu}+\partial_\nu g_{\sigma\mu})\dot x^\mu\dot x^\nu$。于是
   $$
   g_{\sigma\nu}\ddot x^\nu + \tfrac12\big(\partial_\mu g_{\sigma\nu}+\partial_\nu g_{\sigma\mu}-\partial_\sigma g_{\mu\nu}\big)\dot x^\mu\dot x^\nu = 0 .
   $$
7. **识别克里斯托弗符号。** 用 $g^{\rho\sigma}$ 缩并。第一项变为 $\ddot x^\rho$；括号恰好是 s8 中的 $2g_{\sigma\lambda}\Gamma^\lambda{}_{\mu\nu}$，故 $g^{\rho\sigma}\cdot\tfrac12(\cdots) = \Gamma^\rho{}_{\mu\nu}$。结果：
   $$
   \ddot x^\rho + \Gamma^\rho{}_{\mu\nu}\dot x^\mu\dot x^\nu = 0 .
   $$
这与最直路径的测地线方程完全相同。**最短路径与最直路径重合**——对列维-奇维塔联络而言。$\blacksquare$

> **范例 —— 球面上的大圆。** 在 $S^2$ 上取 $ds^2=d\theta^2+\sin^2\theta\,d\phi^2$，测地线方程（用 $\Gamma^\theta{}_{\phi\phi}=-\sin\theta\cos\theta$，$\Gamma^\phi{}_{\theta\phi}=\cot\theta$）由赤道 $\theta=\pi/2$ 解出（$\ddot\theta=0$，且 $\Gamma^\theta{}_{\phi\phi}=-\sin\tfrac\pi2\cos\tfrac\pi2=0$，自洽），以恒定速率走过。由旋转对称性，每一条**大圆**都是测地线——这就是地球上最短的航线。

<a id="s10"></a>
### 曲率 —— 黎曼张量、里奇张量与比安基恒等式

曲率度量流形偏离平坦的程度。一个干净的操作性定义：**在弯曲空间上，协变导数不可交换**，并且沿闭环平行移动会旋转一个向量。

#### 黎曼曲率张量

> **定义 —— 经由对易子的黎曼张量。**
>
> 对无挠联络，**黎曼曲率张量** $R^\rho{}_{\sigma\mu\nu}$ 通过协变导数在向量场上的对易子的作用来定义：
>
> $$
> (\nabla_\mu\nabla_\nu - \nabla_\nu\nabla_\mu)V^\rho = R^\rho{}_{\sigma\mu\nu}\,V^\sigma .
> $$

左边关于 $V$ 是*代数性的*（$V$ 的导数无一幸存），这一点使 $R$ 成为一个真正的 $(1,3)$ 型张量；这是一个定理，通过展开两个 $\nabla\nabla$ 项并观察 $\partial V$ 部分按对称性相消而证明。

> **定理 —— 用克里斯托弗符号表示的黎曼张量。**
>
> $$
> R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}.
> $$

*推导。*
1. 展开 $\nabla_\nu V^\rho = \partial_\nu V^\rho + \Gamma^\rho{}_{\nu\sigma}V^\sigma$；称其为 $W^\rho{}_\nu$（一个 $(1,1)$ 型张量）。
2. 对 $(1,1)$ 型张量 $W$ 作用 $\nabla_\mu$：$\nabla_\mu W^\rho{}_\nu = \partial_\mu W^\rho{}_\nu + \Gamma^\rho{}_{\mu\lambda}W^\lambda{}_\nu - \Gamma^\lambda{}_{\mu\nu}W^\rho{}_\lambda$。
3. 代入 $W$ 并展开。对 $\mu\leftrightarrow\nu$ 反对称化（减去把 $\mu,\nu$ 交换后的同一式）。项 $\partial_\mu\partial_\nu V^\rho$ 对称而相消；联络项 $\Gamma^\lambda{}_{\mu\nu}$ 关于 $\mu\nu$ 对称（无挠）而相消；幸存下来的恰是所展示的、作用于 $V^\sigma$ 的组合。$\blacksquare$

#### 对称性

下降第一个指标，$R_{\rho\sigma\mu\nu}=g_{\rho\lambda}R^\lambda{}_{\sigma\mu\nu}$ 满足（对列维-奇维塔联络）：
$$
R_{\rho\sigma\mu\nu} = -R_{\sigma\rho\mu\nu} = -R_{\rho\sigma\nu\mu} = R_{\mu\nu\rho\sigma},\qquad R_{\rho[\sigma\mu\nu]}=0 ,
$$
即关于第一对反对称、关于第二对反对称、在交换两对时对称，以及**第一（代数）比安基恒等式** $R_{\rho\sigma\mu\nu}+R_{\rho\mu\nu\sigma}+R_{\rho\nu\sigma\mu}=0$。这些在 $n=4$ 时把独立分量数减少到 $20$ 个。

#### 里奇张量与标量

> **定义。** **里奇张量**是缩并 $R_{\sigma\nu} = R^\mu{}_{\sigma\mu\nu}$（由黎曼对称性知它是对称的，$R_{\sigma\nu}=R_{\nu\sigma}$）。**里奇标量**（标量曲率）是全迹 $R = g^{\sigma\nu}R_{\sigma\nu}$。

#### 第二（微分）比安基恒等式

> **定理。** $\ \nabla_\lambda R_{\rho\sigma\mu\nu} + \nabla_\mu R_{\rho\sigma\nu\lambda} + \nabla_\nu R_{\rho\sigma\lambda\mu} = 0.$

最漂亮的证明用一点 $p$ 处的**法坐标**：在这种坐标中 $\Gamma^\rho{}_{\mu\nu}(p)=0$（对任何无挠联络它们都存在，通过一个杀掉 $\Gamma$ 对称部分的二次坐标变换得到）。在 $p$ 处，$\nabla$ 退化为 $\partial$，且 $R^\rho{}_{\sigma\mu\nu}=\partial_\mu\Gamma^\rho{}_{\nu\sigma}-\partial_\nu\Gamma^\rho{}_{\mu\sigma}$，故 $\nabla_\lambda R$ 涉及 $\partial_\lambda\partial_{[\mu}\Gamma$；对 $\lambda,\mu,\nu$ 的循环和由混合偏导相等而相消。作为在一个坐标图中于任意点 $p$ 成立的张量方程，它处处在所有坐标图中成立（s4）。$\blacksquare$

#### 范例 —— 球面是弯曲的，平面不是

对极坐标平面（$\Gamma^r{}_{\theta\theta}=-r$，$\Gamma^\theta{}_{r\theta}=1/r$），直接代入黎曼公式给出 $R^\rho{}_{\sigma\mu\nu}=0$ 处处成立——尽管坐标弯曲，平面仍是**平坦的**。对单位球面（$\Gamma^\theta{}_{\phi\phi}=-\sin\theta\cos\theta$，$\Gamma^\phi{}_{\theta\phi}=\cot\theta$）则求得 $R^\theta{}_{\phi\theta\phi}=\sin^2\theta$，给出里奇张量 $R_{\theta\theta}=1$，$R_{\phi\phi}=\sin^2\theta$，以及里奇标量 $R = g^{\theta\theta}R_{\theta\theta}+g^{\phi\phi}R_{\phi\phi} = 1 + 1 = 2$（对单位球面；一般地对半径 $a$ 有 $R=2/a^2$）。正的常曲率，与直觉相符。

<a id="s11"></a>
### 测地偏离与曲率的物理意义

曲率不会被单个自由下落的观测者直接感知到——由等效原理，孤立的自由下落物体无法把引力与自由空间区分开。曲率*确实*产生的是**潮汐力**：邻近的测地线彼此加速靠近或远离。

#### 测地偏离方程

考虑一族单参数测地线 $x^\mu(\lambda,s)$，$s$ 标记相邻的测地线。设 $T^\mu = \partial x^\mu/\partial\lambda$ 为切向量，$S^\mu=\partial x^\mu/\partial s$ 为指向相邻测地线的**偏离向量**。

> **定理 —— 测地偏离（雅可比方程）。**
>
> $$
> \frac{D^2 S^\rho}{d\lambda^2} = -\,R^\rho{}_{\sigma\mu\nu}\,T^\sigma S^\mu T^\nu .
> $$
>
> 邻近测地线的相对加速度*完全*由黎曼张量支配。

*推导梗概。* $T$ 与 $S$ 都是该族的坐标向量场，故它们的李括号为零，这（对无挠联络）给出 $\nabla_T S = \nabla_S T$。计算二阶协变导数 $\frac{D^2S}{d\lambda^2}=\nabla_T\nabla_T S = \nabla_T\nabla_S T$，经由黎曼张量的定义（s10）交换导数，并用测地线方程 $\nabla_T T=0$ 丢掉一项。幸存的项就是上面的曲率缩并。$\blacksquare$

#### 物理意义：潮汐力

在牛顿引力中，一团自由下落的粒子沿径向被拉伸、横向被压缩——这就是月球抬起两个海洋隆起的**潮汐场**。在广义相对论中，那个潮汐场*就是*黎曼张量：$\frac{D^2S^\rho}{d\lambda^2}=-R^\rho{}_{\sigma\mu\nu}T^\sigma S^\mu T^\nu$ 是相对论的潮汐方程，而在牛顿极限下 $R^i{}_{0j0}\to \partial_i\partial_j\Phi$（引力势的二阶导数）。

> **直觉。** 两位旅行者从赤道出发，沿各自的经线一路向正北（两者都是测地线）*起初平行*移动，却*会聚*并在极点相遇。他们没有感到任何侧向力，但他们的间隔却加速归零——纯粹是曲率，没有力。这就是广义相对论中的引力。

## E 部分 · 广义相对论与对称性

<a id="s12"></a>
### 爱因斯坦场方程 —— 广义相对论的结构

现在我们把各部分组装成支配时空的方程。指导性要求：它应把**曲率**（几何）与**能量–动量**（物质）联系起来，是一个张量方程（与参考系无关，s4），关于度量是二阶的（像牛顿引力那样，$\nabla^2\Phi=4\pi G\rho$），并尊重**局部能量–动量守恒** $\nabla_\mu T^{\mu\nu}=0$。

#### 爱因斯坦张量

物质一侧是**应力–能量张量** $T_{\mu\nu}$，一个对称的 $(0,2)$ 型张量，编码能量密度、动量与应力，满足 $\nabla^\mu T_{\mu\nu}=0$。因此几何一侧必须是一个对称的 $(0,2)$ 型张量，由度量及其前两阶导数构造，且**散度恒等于零**。我们来构造它。

1. **缩并第二比安基恒等式**（s10）：从 $\nabla_\lambda R_{\rho\sigma\mu\nu}+\nabla_\mu R_{\rho\sigma\nu\lambda}+\nabla_\nu R_{\rho\sigma\lambda\mu}=0$ 出发。
2. 升起并缩并指标（先 $g^{\rho\mu}$，再 $g^{\sigma\nu}$），用度量相容性 $\nabla g=0$ 把度量穿过导数，并用黎曼对称性辨认出里奇部分。结果是**缩并的比安基恒等式**
   $$
   \nabla^\mu R_{\mu\nu} = \tfrac12\,\nabla_\nu R .
   $$
3. **重排**为一个无散度的组合：
   $$
   \nabla^\mu\!\left(R_{\mu\nu} - \tfrac12 g_{\mu\nu}R\right) = \nabla^\mu R_{\mu\nu} - \tfrac12\nabla_\nu R = 0 ,
   $$
   其中用到度量相容性给出的 $\nabla^\mu(g_{\mu\nu}R)=\nabla_\nu R$。
4. **定义爱因斯坦张量**
   $$
   G_{\mu\nu} := R_{\mu\nu} - \tfrac12 g_{\mu\nu}R ,\qquad \nabla^\mu G_{\mu\nu}=0 .
   $$
它是对称的，由 $g$ 的二阶导数构造，并*自动*守恒——恰好与 $T_{\mu\nu}$ 匹配。

#### 场方程

> **爱因斯坦场方程。**
>
> $$
> R_{\mu\nu} - \tfrac12 g_{\mu\nu}R + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4}\,T_{\mu\nu} .
> $$
>
> 这里 $G$ 是牛顿常数，$c$ 是光速，$\Lambda$ 是**宇宙学常数**（同样无散度，因为 $\nabla g=0$，故被允许）。常数 $8\pi G/c^4$ 由要求在弱、慢、静场下取得**牛顿极限** $\nabla^2\Phi=4\pi G\rho$ 而确定。

用惠勒的口号说：*时空告诉物质如何运动*（物质沿测地线运动，s9），*而物质告诉时空如何弯曲*（场方程）。本指南的两半——测地线与曲率——正是引力的两半。

> **范例 —— 真空与结构。** 在真空中（$T_{\mu\nu}=0$，$\Lambda=0$）：用 $g^{\mu\nu}$ 缩并场方程。利用 $g^{\mu\nu}g_{\mu\nu}=n=4$，我们得到 $R - \tfrac12\cdot4\cdot R = -R = 0$，故 $R=0$，进而 $R_{\mu\nu}=0$。**真空时空是里奇平坦的**——然而*黎曼*张量未必为零，所以引力（潮汐曲率）在空无一物的空间中仍然存在。恒星外部的史瓦西解正是这样一个里奇平坦但黎曼弯曲的几何；它预言了星光的偏折以及水星的进动。

<a id="s13"></a>
### 李导数与基灵向量 —— 对称性与守恒量

度量的对称性沿测地线产生守恒量——这是诺特定理的几何形式。合适的工具是**李导数**，它沿一个向量场的流对张量求导，*而无需联络*。

#### 李导数

> **定义 —— 李导数。**
>
> 设 $X$ 为生成流 $\phi_t$（方程 $\frac{d}{dt}\phi_t(p)=X_{\phi_t(p)}$ 的解）的向量场。张量 $T$ 沿 $X$ 的**李导数**是由流拉回的 $T$ 的变化率：
>
> $$
> \mathcal{L}_X T = \lim_{t\to0}\frac{\phi_t^*T - T}{t}.
> $$

它通过*沿 $X$ 的流移动*而非通过联络来比较邻近点处的 $T$。具体公式（由定义将流展开到一阶导出）：
- 在函数上：$\mathcal{L}_X f = X^\mu\partial_\mu f = X(f)$。
- 在向量场上：$\mathcal{L}_X Y = [X,Y]$，李括号。
- 在度量（一个 $(0,2)$ 型张量）上：
  $$
  (\mathcal{L}_X g)_{\mu\nu} = X^\lambda\partial_\lambda g_{\mu\nu} + g_{\lambda\nu}\partial_\mu X^\lambda + g_{\mu\lambda}\partial_\nu X^\lambda = \nabla_\mu X_\nu + \nabla_\nu X_\mu ,
  $$
  最后一个等号对列维-奇维塔联络成立（克里斯托弗项把偏导数重组为协变导数——非张量性的 $\Gamma$ 部分相消，因为 $\mathcal{L}_X g$ 是张量）。

#### 基灵向量

> **定义 —— 基灵向量。**
>
> 一个向量场 $\xi$ 是**基灵向量场**，如果度量在它的流下不变，即 $\mathcal{L}_\xi g = 0$。等价地，由上面的公式，它满足**基灵方程**
>
> $$
> \nabla_\mu \xi_\nu + \nabla_\nu \xi_\mu = 0 .
> $$

每个基灵向量都是一个无穷小等距——一个使几何"看起来一样"的方向。例如，圆球面上或轴对称时空中的 $\partial_\phi$ 是基灵向量（旋转对称性）；静态时空中的 $\partial_t$ 是基灵向量（时间平移对称性）。

#### 沿测地线的守恒量

> **定理。** 若 $\xi$ 是基灵向量，$x^\mu(\lambda)$ 是切向量为 $u^\mu=\dot x^\mu$ 的测地线，则 $\xi_\mu u^\mu$ **沿测地线为常数**。

*证明。*
1. 沿测地线求导：$\frac{d}{d\lambda}(\xi_\mu u^\mu) = u^\nu\nabla_\nu(\xi_\mu u^\mu)$，因为 $\xi_\mu u^\mu$ 是标量且 $\frac{d}{d\lambda}=u^\nu\nabla_\nu$。
2. 应用莱布尼茨法则：$u^\nu\nabla_\nu(\xi_\mu u^\mu) = u^\nu u^\mu\nabla_\nu\xi_\mu + \xi_\mu\,u^\nu\nabla_\nu u^\mu$。
3. 第二项由**测地线方程** $u^\nu\nabla_\nu u^\mu=0$（s9）知为 $\xi_\mu\,(u^\nu\nabla_\nu u^\mu)=0$。
4. 第一项 $u^\nu u^\mu\nabla_\nu\xi_\mu$ 把**对称的** $u^\nu u^\mu$ 与 $\nabla_\nu\xi_\mu$ 缩并。把 $\nabla_\nu\xi_\mu$ 拆为对称与反对称部分；对称部分 $\tfrac12(\nabla_\nu\xi_\mu+\nabla_\mu\xi_\nu)=0$ 由**基灵方程**而得，反对称部分与对称的 $u^\nu u^\mu$ 缩并则消失（对称乘反对称，如 s6 中所述）。故这一项也为 $0$。
5. 因此 $\frac{d}{d\lambda}(\xi_\mu u^\mu)=0$。$\blacksquare$

> **范例 —— 守恒的能量与角动量。** 在一个稳态、轴对称的时空中（例如史瓦西），$\xi_{(t)}=\partial_t$ 与 $\xi_{(\phi)}=\partial_\phi$ 是基灵向量。守恒量 $-\xi_{(t)\mu}u^\mu$ 与 $\xi_{(\phi)\mu}u^\mu$ 恰好是一个绕行粒子单位质量的**能量**与**角动量**——正是那些让人能够积分出行星轨道与光线偏折的常数。度量的对称性化为守恒律，正如诺特定理所承诺的那样。

---

*本指南从最基础处搭建起微分几何——流形与坐标图、作为求导子的切向量、张量及其变换律、度量、形式与斯托克斯定理、协变导数、测地线以及曲率——然后把整座大厦回读为广义相对论：物质沿测地线运动，曲率是潮汐场，而爱因斯坦方程把时空的曲率与其中的能量联系起来。可随时回到任何一个加框的定义或编号的推导作为参考。贯穿其下的那一个理念是无坐标性：用张量书写物理，定律便在每一个参考系中成立——这正是为何这门单一的学科是书写引力所用的语言。*
