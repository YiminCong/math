[English](fiber-bundles-gauge.md) · **中文**

# 纤维丛与规范理论，*力的几何学。*

*这是一篇自洽且严格的导引，介绍隐藏在基本力背后的几何。我们从纤维丛的朴素概念出发——一个"由许多份纤维沿底空间粘合而成"的空间——并一步步搭建起现代物理的机器：主丛、联络、曲率、和乐、Yang–Mills 理论，以及对它们进行分类的拓扑不变量。贯穿全文反复出现的启示是：一个力场就是丛上的一个联络，其场强就是曲率，而规范不变性就是重新标记纤维的自由。几何是目标；规范理论是动机；每个公式都被推导，每个符号都被解释。*

[← 返回全部指南](../README.zh.md)

**预备知识。** 本指南假定读者已读过 **微分几何与张量** 指南（光滑流形与图卡、切空间与余切空间、向量场、微分形式、外微分 $d$ 与楔积 $\wedge$，以及联络/协变导数）。我们在用到每个借来的事实时都用一行重新陈述它。我们也轻度依赖 **群论** 指南中关于矩阵李群及其李代数的内容；所需事实会随用随复述。

## A 部分 · 丛

<a id="s0"></a>
### 动机——规范场作为联络；为什么物理活在丛上，而不仅在时空上

二十世纪物理学最深刻的教训是：基本力——电磁力、弱力、强力——并不是涂抹在时空之上的额外"东西"。它们就是*几何*：每种力都是一种比较粒子在不同点处内部状态的方式，而这种比较恰恰就是几何学家所称的**联络**。

#### 我们要解决什么问题？

在预备指南中，联络让我们能够比较流形 $M$（时空）不同点处的*切向量*。但一个带电粒子携带的不只是速度。一个电子拥有量子力学的相位；一个夸克在一个 3 维内部空间中携带"色"标签。这些内部数据活在附着于每一点的一个向量空间中——一个**纤维**——而要做物理，我们必须比较不同点处的纤维。并没有典范的方式去这样做，正如在弯曲曲面上没有典范的方式去比较切向量一样。比较方式的一个*选择*就是**规范场**。

两个事实驱动整个学科：

1. **内部对称性。** 若我们用一个对称群 $G$ 的元素去旋转内部标签，物理保持不变（对电磁力 $G=U(1)$，即相位的圆周；对强力 $G=SU(3)$）。这种重新标记的自由就是**规范对称性**。
2. **没有整体标架。** 通常并不存在唯一一致的方式同时给全部时空上的内部状态标记——这些标签必须逐片缝合，而缝合之处正是拓扑（有时还有物理，如磁单极子的情形）藏身之所。

把"每一点上有一个纤维、它们被一致地粘合、且有一个对称群作用在纤维上"打包起来的数学对象就是**纤维丛**。它上面的联络就是规范场；它的曲率就是**场强**（电磁场 $F_{\mu\nu}$、胶子场……）；而支配其动力学的作用量就是 **Yang–Mills**。本指南的目的是让这句话的每个字都变得精确。

#### 计划

我们按顺序搭建：**纤维丛**（这些空间，s1）、**向量丛与截面**（s2）、**主丛与结构群**（s3）、主丛上的**联络**（s4）、**局部规范势** $A$ 及其变换方式（s5）、**曲率**与场强 $F=dA+A\wedge A$（s6）、**平行移动、和乐与 Wilson 圈**（s7）、**物质场上的协变导数**（s8）、以 Maxwell 作为阿贝尔情形的 **Yang–Mills 理论**（s9）、**特征类**（Chern 类、Chern–Simons）（s10），最后是**物理例子**——Dirac 单极子、Aharonov–Bohm 效应与瞬子（s11）。

> **直觉。** 始终在脑中保留一幅图像：丛是一个"加厚"的流形——底的每一点之上都坐落着纤维的一整份拷贝。联络是一条*在相邻纤维之间如何滑动的无穷小规则*。曲率衡量这种滑动绕一个小圈时不对易的程度。其余一切都是为保持这些局部规则在整体上一致而做的记账。

<a id="s1"></a>
### 纤维丛——全空间、底、纤维、投影、局部平凡化

纤维丛是"一族全同的空间，底的每一点上各放一份，粘合起来使得局部看像乘积而整体上可能扭曲"这一概念的精确表述。

#### 定义

> **定义 — 纤维丛。**
>
> 一个**纤维丛**是一个四元组 $(E,M,\pi,F)$，由以下组成：
> - 一个光滑流形 $E$，称为**全空间**；
> - 一个光滑流形 $M$，称为**底空间**；
> - 一个光滑满射 $\pi:E\to M$，称为**投影**；
> - 一个光滑流形 $F$，称为**典型纤维**，
>
> 使得 $\pi$ 是**局部平凡的**：每一点 $x\in M$ 都有一个开邻域 $U\subseteq M$ 和一个微分同胚（具有光滑逆的光滑映射）
> $$
> \phi_U:\ \pi^{-1}(U)\ \xrightarrow{\ \sim\ }\ U\times F
> $$
> 使得 $\mathrm{pr}_1\circ\phi_U=\pi$，其中 $\mathrm{pr}_1:U\times F\to U$ 是到第一因子的投影。对 $(U,\phi_U)$ 称为一个**局部平凡化**。

把它拆开来看：$\pi^{-1}(\{x\})$ 是**在 $x$ 上的纤维**，记作 $E_x$；条件 $\mathrm{pr}_1\circ\phi_U=\pi$ 迫使 $\phi_U$ 把纤维 $E_x$ 微分同胚地搬到 $\{x\}\times F$ 上，所以每个纤维都是 $F$ 的一份拷贝。"局部平凡"意味着：放大到底的一小片 $U$，则 $E$ 在其上方的部分恰是乘积 $U\times F$——平淡无奇、毫无扭曲。有趣的内容是*整体的*：重叠片上的各个局部乘积图像是如何粘合的。

#### 转移函数

> **定义 — 转移函数。**
>
> 设 $(U_\alpha,\phi_\alpha)$ 与 $(U_\beta,\phi_\beta)$ 是两个满足 $U_\alpha\cap U_\beta\ne\varnothing$ 的局部平凡化。在重叠区上，复合
> $$
> \phi_\alpha\circ\phi_\beta^{-1}:\ (U_\alpha\cap U_\beta)\times F\ \to\ (U_\alpha\cap U_\beta)\times F
> $$
> 保持底点（两侧都投影到同一个 $x$），所以它具有形式 $(x,f)\mapsto\big(x,\ g_{\alpha\beta}(x)\cdot f\big)$，其中 $g_{\alpha\beta}:U_\alpha\cap U_\beta\to \mathrm{Diff}(F)$ 是到纤维变换的光滑映射。这些 $g_{\alpha\beta}$ 就是**转移函数**。

转移函数编码了粘合——即"扭曲"。它们满足两个直接由定义推出的相容性条件：

1. **对角线上为恒等：** $g_{\alpha\alpha}(x)=\mathrm{id}$，因为 $\phi_\alpha\circ\phi_\alpha^{-1}$ 是恒等。
2. **上闭链条件：** 在三重重叠区 $U_\alpha\cap U_\beta\cap U_\gamma$ 上，
   $$
   g_{\alpha\beta}(x)\,g_{\beta\gamma}(x)=g_{\alpha\gamma}(x),
   $$
   因为 $(\phi_\alpha\phi_\beta^{-1})(\phi_\beta\phi_\gamma^{-1})=\phi_\alpha\phi_\gamma^{-1}$。令 $\gamma=\alpha$ 得 $g_{\alpha\beta}=g_{\beta\alpha}^{-1}$。

> **直觉。** 一个丛*就是*它的底、它的纤维和它的转移函数，在重新标记的意义下确定。平凡丛是那些能整体地选取所有 $g_{\alpha\beta}=\mathrm{id}$ 的丛；非平凡丛则做不到。

#### 例子

**例 1 — 平凡丛（一个圆柱）。** 取底 $M=S^1$（一个圆）、纤维 $F=[-1,1]$（一个区间）、全空间 $E=S^1\times[-1,1]$，$\pi$ 是到 $S^1$ 的投影。这就是**圆柱**。单一的平凡化（恒等）处处适用；没有扭曲。它是一个*整体乘积*。

**例 2 — 非平凡丛（Möbius 带）。** 取同样的底 $S^1$ 与纤维 $[-1,1]$，但带翻转地粘合。用两段弧 $U_1,U_2$ 覆盖 $S^1$，它们在两个小区间上重叠。在一个重叠区上用 $g_{12}(x)=\mathrm{id}$（映射 $f\mapsto f$）；在另一个上用 $g_{12}(x)=-\mathrm{id}$（翻转 $f\mapsto -f$）。所得全空间就是 **Möbius 带**。它处处*局部*为 $U\times[-1,1]$，但*整体*上却不是圆柱：它只有一条边，而不是两条，并且是不可定向的。这具体说明了局部平凡并不蕴含整体平凡——拓扑被转移函数所携带。

> **范例 — 区分两者。** 沿 Möbius 带的底走一圈，跟随平凡化。因为有一个重叠区翻转了纤维，一个处于"高度 $+\tfrac12$"的点回来时位于高度 $-\tfrac12$。在圆柱上它回到 $+\tfrac12$。单值性（走一圈后的净纤维变换）为 $-\mathrm{id}\ne\mathrm{id}$，故两个丛不同构。此处结构群约化为 $\{\pm 1\}=\mathbb{Z}_2$。

**例 3 — 切丛。** 对一个光滑 $n$ 维流形 $M$，**切丛** $TM=\bigsqcup_{x\in M}T_xM$（所有切空间的无交并）是一个纤维丛，纤维为 $F=\mathbb{R}^n$，投影 $\pi$ 把 $x$ 处的切向量送到 $x$。带坐标 $x^i$ 的图卡 $(U,\varphi)$ 经 $v=v^i\partial_i\mapsto(x,(v^1,\dots,v^n))$ 给出平凡化 $\pi^{-1}(U)\cong U\times\mathbb{R}^n$。转移函数是坐标变换的 **Jacobi 矩阵**：若 $\tilde x=\tilde x(x)$，则 $g_{\alpha\beta}(x)=\big(\partial\tilde x^i/\partial x^j\big)\in GL(n,\mathbb{R})$（可逆 $n\times n$ 矩阵群），恰是 $v$ 的分量所遵守的变换律。对 $M=S^2$，切丛是非平凡的——"毛球定理"说 $S^2$ 上没有处处非零的连续向量场，而平凡丛本会提供这样的场。

<a id="s2"></a>
### 向量丛；截面；重新审视切丛与余切丛

物理上最感兴趣的纤维是*向量空间*：一个粒子的内部状态是一个向量（波函数的一个分量、一个色向量）。纤维为向量空间、由线性映射粘合的丛就是**向量丛**。

#### 定义

> **定义 — 向量丛。**
>
> 一个**（实的、秩 $k$ 的）向量丛**是一个纤维丛 $\pi:E\to M$，其典型纤维为 $F=\mathbb{R}^k$，使得：
> - 每个纤维 $E_x=\pi^{-1}(x)$ 带有 $k$ 维实向量空间结构，且
> - 局部平凡化 $\phi_U:\pi^{-1}(U)\to U\times\mathbb{R}^k$ 限制在每个纤维上是一个**线性同构** $E_x\to\{x\}\times\mathbb{R}^k$。
>
> 因此转移函数取值于一般线性群：$g_{\alpha\beta}:U_\alpha\cap U_\beta\to GL(k,\mathbb{R})$。（复向量丛把 $\mathbb{R}$ 换成 $\mathbb{C}$，把 $GL(k,\mathbb{R})$ 换成 $GL(k,\mathbb{C})$。）

要求转移是*线性的*（而非 $\mathbb{R}^k$ 的任意微分同胚），正是使得"把纤维的两个元素相加"或"用一个数缩放"与平凡化无关地有良定义的原因。

#### 截面

> **定义 — 截面。**
>
> 丛 $\pi:E\to M$ 的一个**截面**是一个光滑映射 $s:M\to E$，满足 $\pi\circ s=\mathrm{id}_M$；也就是说，$s$ 给每个底点 $x$ 指派*其自身纤维* $E_x$ 中的一个元素 $s(x)$。我们用 $\Gamma(E)$ 表示（光滑）截面之集。一个**局部截面**只在某开集 $U\subseteq M$ 上定义。

从物理上看，向量丛的一个截面*就是一个物质场*：它在每个时空点选取内部向量的一个值（一个电子的波函数、一个色向量）。零截面 $s(x)=0_{E_x}$ 对向量丛总是存在；一个向量丛是平凡的当且仅当它容许 $k$ 个在每点都线性无关的截面（一个**整体标架**），因为这些截面让我们能够通过读出分量来定义整体平凡化。

> **陷阱。** 即便对线丛（秩 $1$），*处处非零*的截面也未必存在：把 Möbius 带视为 $S^1$ 上的实线丛时，它没有处处非零的截面，因为任何截面在定向翻转之后都必须穿过零（介值定理）。截面是整体对象，能感受拓扑。

#### 重新审视切丛与余切丛

切丛 $TM$（s1）是一个秩 $n$ 的实向量丛；它的截面恰是**向量场**，$\Gamma(TM)=\mathfrak{X}(M)$。对偶的构造给出**余切丛** $T^*M=\bigsqcup_x T_x^*M$，其纤维 $T_x^*M$ 是 $T_xM$ 上线性泛函的对偶向量空间。它的截面是 **1-形式**（余向量场），$\Gamma(T^*M)=\Omega^1(M)$。在坐标变换 $\tilde x(x)$ 之下：

- 切分量按 Jacobi 矩阵 $J=(\partial\tilde x^i/\partial x^j)$ 变换：$\tilde v^i=J^i{}_j v^j$；
- 余切分量按*逆转置* $(J^{-1})^T$ 变换：$\tilde\omega_i=(J^{-1})^j{}_i\,\omega_j$，

从而配对 $\omega_i v^i$ 不变。更一般地，张量丛 $T^{(p,q)}M$ 的纤维由 $TM$ 与 $T^*M$ 的张量积构造而成，其截面就是预备指南中的 $(p,q)$ 张量场。微分 $p$-形式是 $\Lambda^p T^*M$（交错 $p$-余向量之丛）的截面。

> **范例 — $S^2$ 上的秩 2 丛。** 切丛 $TS^2$ 的纤维为 $\mathbb{R}^2$。用两个球极投影图卡（北与南，如预备指南所述）覆盖 $S^2$。在重叠区（去掉两极的球面，一个环带）上，转移函数是坐标变换 $(u,v)\mapsto(u,v)/(u^2+v^2)$ 的 Jacobi 矩阵。计算这个 Jacobi 矩阵会发现它是一个*旋转加缩放*，当你绕赤道一圈时它绕转两次。那个绕数 $2$ 就是 $S^2$ 的 **Euler 数**，而它的非零性正是 $TS^2$ 非平凡、且毛球定理成立的原因。

<a id="s3"></a>
### 主 $G$-丛与结构群；标架丛；伴随丛

向量丛记录了"内部向量"。但规范*对称性*——重新标记它们的群 $G$——本身就是几何的。直接携带对称性、以该群作为纤维的丛就是**主丛**。它是规范理论的中心对象。

#### 结构群

我们首先注意到，一个丛的转移函数往往并不落在整个 $\mathrm{Diff}(F)$ 或整个 $GL(k)$ 中，而落在一个作用于 $F$ 的更小的群 $G$ 中。我们于是称 $G$ 为该丛的**结构群**。对每个纤维上带有选定度量的实向量丛，转移可取在正交群 $O(k)$ 中；对带 Hermite 纤维的复丛，可取在酉群 $U(k)$ 中。回顾（群论指南）：一个**李群**是同时也是带光滑乘法与求逆的光滑流形的群；像 $U(1)$、$SU(2)$、$SU(3)$ 这样的矩阵群就是相关的例子。

#### 主丛

> **定义 — 主 $G$-丛。**
>
> 设 $G$ 为李群。一个**主 $G$-丛**是一个纤维丛 $\pi:P\to M$，其纤维就是 $G$ 本身，连同一个光滑的**右作用** $P\times G\to P$，$(p,g)\mapsto p\cdot g$，使得：
> - $G$ **自由地**作用（$p\cdot g=p$ 蕴含 $g=e$，即恒等元）且**在每个纤维上传递地**作用（一个纤维的任意两点相差一个唯一的群元素），从而纤维恰是该作用的**轨道**，且
> - 局部平凡化是 $G$-**等变的**：$\phi_U(p\cdot g)=\phi_U(p)\cdot g$，其中 $G$ 通过在第二因子上的右乘作用于 $U\times G$。

右作用是"用一个群元素重新标记内部标架"的抽象版本。关键在于，主丛在每个纤维中*没有偏好的点*——在你选取一个平凡化（一个"规范"）之前，$\pi^{-1}(x)\cong G$ 中没有典范的单位元。一个平凡化与一个**局部截面** $\sigma:U\to P$（在每点选取一个"参考标架"）是相同的数据：给定 $\sigma$，纤维的每个点都唯一地写成 $\sigma(x)\cdot g$，这定义了 $\phi_U(\sigma(x)\cdot g)=(x,g)$。

> **关键事实 — 主丛平凡当且仅当它容许整体截面。** （$\Rightarrow$）平凡化 $P\cong M\times G$ 给出截面 $x\mapsto(x,e)$。（$\Leftarrow$）整体截面 $\sigma$ 给出平凡化 $\sigma(x)\cdot g\mapsto(x,g)$，由自由性与传递性可知它是良定义且 $G$-等变的。这是"向量丛平凡当且仅当它有整体标架"的主丛类比。

#### 标架丛

> **定义 — 标架丛。**
>
> 对一个秩 $k$ 的向量丛 $E\to M$，**标架丛** $FE$ 在 $x$ 上的纤维是 $E_x$ 的所有有序基（**标架**）$(e_1,\dots,e_k)$ 之集。群 $GL(k,\mathbb{R})$ 通过 $\big(e_a\big)\cdot g=\big(e_b\, g^b{}_a\big)$（换基）自由且传递地作用于标架，使 $FE$ 成为一个主 $GL(k,\mathbb{R})$-丛。

对 $E=TM$，这就是**切标架丛** $F(TM)$。若 $M$ 带有 Riemann 度量，我们可以限制到*正交*标架，得到一个主 $O(k)$-丛（正交标架丛）——这是广义相对论中标架场/四标架的几何归宿。

#### 伴随丛

主丛是主导对象；向量丛是由它*恢复*出来的。

> **定义 — 伴随丛。**
>
> 设 $\pi:P\to M$ 为主 $G$-丛，设 $\rho:G\to GL(V)$ 为 $G$ 在向量空间 $V$ 上的一个**表示**（到 $V$ 的线性映射的同态；群论指南）。**伴随向量丛**为
> $$
> P\times_\rho V\ :=\ (P\times V)\big/\sim,\qquad (p\cdot g,\,v)\sim(p,\,\rho(g)v),
> $$
> 即 $P\times V$ 在等价关系"用 $g$ 移动标架并用 $\rho(g)$ 移动分量使物理向量保持不变"下的商。它是 $M$ 上一个以 $V$ 为纤维、以 $\rho(G)$ 为结构群的向量丛。

> **直觉。** $P$ 储存*所有可能的标架以及群如何置换它们*。一个表示 $\rho$ 说明*给定种类的物质如何响应*一次标架变换。把它们配对（$P\times_\rho V$）就重建出物理场丛。一个主丛，许多伴随物质丛——电子、夸克、Higgs 场——各经由其自身的表示。这就是为什么规范理论把主丛放在首位。

> **范例 — 标架丛重新给出切丛。** 取 $P=F(TM)$（$TM$ 的标架，群为 $GL(n,\mathbb{R})$）和 $\rho=\mathrm{id}$，即在 $V=\mathbb{R}^n$ 上的定义表示。则 $P\times_\rho\mathbb{R}^n\cong TM$：一个标架 $(e_a)$ 连同分量 $v\in\mathbb{R}^n$ 表示向量 $e_a v^a$，而关系 $(e_a g^a{}_b,\,v)\sim(e_a,\,g v)$ 恰是该向量与基无关这一陈述。我们绕了一整圈回到起点。

## B 部分 · 联络与曲率

<a id="s4"></a>
### 主丛上的联络——联络 1-形式、水平子空间与竖直子空间

联络回答这样一个问题：*给定一个纤维中的一点，相邻纤维中哪些点算作"同一个、经移动而来的"？* 在主丛上最清晰的表述是把全空间的切空间分解为"沿纤维"和"横越到邻居"。

#### 竖直与水平

在一点 $p\in P$ 处，切空间 $T_pP$ 含有切于纤维的方向。因为纤维是一个 $G$-轨道，每个李代数元素 $\xi\in\mathfrak{g}$（$G$ 的**李代数**，即它在单位元处的切空间，带括号 $[\cdot,\cdot]$）生成一条过 $p$ 的曲线 $p\cdot\exp(t\xi)$，其速度是一个竖直向量。

> **定义 — 竖直子空间。** **竖直子空间**为 $V_p=\ker(d\pi_p)\subseteq T_pP$：投影到底中为零的方向，即切于纤维的方向。映射 $\xi\mapsto \frac{d}{dt}\big|_0\,p\cdot\exp(t\xi)$ 称为**基本向量场** $\xi^\#$，是一个线性同构 $\mathfrak{g}\xrightarrow{\sim}V_p$。

并不存在典范的"水平"补；选取一个*就是*联络。

> **定义 — 联络（Ehresmann）。**
>
> 主 $G$-丛 $P$ 上的一个**联络**是在每点 $p\in P$ 处对一个**水平子空间** $H_p\subseteq T_pP$ 的光滑选取，使得
> 1. $T_pP=V_p\oplus H_p$（水平补竖直），且
> 2. 该选取是 $G$-等变的：$H_{p\cdot g}=(R_g)_*H_p$，其中 $R_g$ 是用 $g$ 的右平移，$(R_g)_*$ 是其微分。

条件 2 说明水平方向在一个纤维上是一致的——用群平移把水平送到水平。$P$ 中一条道路若其速度处处落在 $H$ 中则称为**水平的**；这是"无改变地移动"的精确概念，将在 s7 中展开。

#### 联络 1-形式

这一分解被一个取值于 $\mathfrak{g}$ 的 1-形式紧凑地编码。

> **定义 — 联络 1-形式。**
>
> **联络 1-形式** $\omega\in\Omega^1(P;\mathfrak{g})$（$P$ 上取值于李代数的 1-形式）由下列条件定义：
> - 对每个 $\xi\in\mathfrak{g}$，$\omega(\xi^\#)=\xi$（它读出竖直部分），且
> - $\ker\omega_p=H_p$（它的核是水平子空间）。
>
> 等价地，$\omega$ 把每个切向量投影到其竖直部分，并把它认同为 $\mathfrak{g}$ 的一个元素。$H$ 的等变性被编码为
> $$
> R_g^*\omega=\mathrm{Ad}_{g^{-1}}\circ\,\omega,
> $$
> 其中 $\mathrm{Ad}_{g^{-1}}(\xi)=g^{-1}\xi g$ 是 $G$ 在 $\mathfrak{g}$ 上的**伴随作用**。

> **为什么这两组数据一致。** 给定 $\omega$，令 $H_p=\ker\omega_p$；由于 $\omega$ 限制在 $V_p$ 上是同构 $V_p\cong\mathfrak{g}$（第一条），其核与 $V_p$ 只在 $0$ 处相交，且具有互补的维数，所以 $T_pP=V_p\oplus H_p$。反过来，一个分解把 $\omega$ 定义为"竖直投影再接 $V_p\cong\mathfrak{g}$"。因此联络的两种表述是等价的——我们用哪个方便就用哪个。

> **直觉。** $\omega$ 是一个"水平仪"：喂给它 $P$ 中的任何运动，它返回其中*纯属内部重新标记*（竖直）的部分，丢弃真正的底运动（水平）。说"没有发生内部变化"就是说沿该运动 $\omega=0$。接下来要讲的规范场，就是 $\omega$ 在选定规范中的样子。

<a id="s5"></a>
### 局部规范势 $A$ 与规范变换（$A$ 如何变换）

联络 1-形式 $\omega$ 住在上方的 $P$ 上，难以想象。物理学家在下方的时空 $M$ 上用**规范势** $A$ 工作——它是 $\omega$ 经选定局部截面（选定规范）的拉回。

#### 定义

> **定义 — 局部规范势。**
>
> 设 $\sigma_\alpha:U_\alpha\to P$ 为一个局部截面（一个规范选取）。**局部规范势**是拉回的 1-形式
> $$
> A_\alpha\ :=\ \sigma_\alpha^*\omega\ \in\ \Omega^1(U_\alpha;\mathfrak{g}),
> $$
> 它是片 $U_\alpha\subseteq M$ 上取值于 $\mathfrak{g}$ 的 1-形式。在坐标下 $A_\alpha=A_\mu\,dx^\mu$，其中每个 $A_\mu(x)\in\mathfrak{g}$ 是一个李代数元素。对矩阵群，$A_\mu$ 是一个 1-形式分量构成的矩阵；这就是物理中的**规范场**（光子势、胶子场）。

#### $A$ 在规范变换下如何变换

重叠区 $U_\alpha\cap U_\beta$ 上的两个规范 $\sigma_\alpha,\sigma_\beta$ 通过转移函数 $g_{\alpha\beta}:U_\alpha\cap U_\beta\to G$ 经 $\sigma_\beta=\sigma_\alpha\cdot g_{\alpha\beta}$ 相联系（在每点用一个群元素重新标记参考标架）。我们来推导 $A$ 由此产生的变化。记 $g:=g_{\alpha\beta}$。

> **定理 — 规范势的规范变换。**
> $$
> A_\beta\ =\ g^{-1}A_\alpha\,g\ +\ g^{-1}\,dg.
> $$

*证明。*
1. 由定义 $A_\beta=\sigma_\beta^*\omega$，且 $\sigma_\beta=R_g\circ\sigma_\alpha$ 后接作用——更仔细地说，$\sigma_\beta(x)=\sigma_\alpha(x)\cdot g(x)$，它是截面、右作用与映射 $x\mapsto g(x)$ 的复合。我们沿此复合把 $\omega$ 拉回。
2. 由作用映射 $P\times G\to P$ 的 **Leibniz 法则**，$x\mapsto\sigma_\alpha(x)\cdot g(x)$ 的微分分裂为两个贡献：一个是固定 $g$ 而移动 $\sigma_\alpha$，另一个是固定 $\sigma_\alpha$ 而移动 $g$。
3. **第一个贡献（移动 $\sigma_\alpha$）：** 固定 $g(x)=g$ 而变动第一槽得到 $R_g\circ\sigma_\alpha$。把 $\omega$ 拉回，由等变性 $R_g^*\omega=\mathrm{Ad}_{g^{-1}}\omega$（s4），$(\,R_g\circ\sigma_\alpha)^*\omega=\sigma_\alpha^*(R_g^*\omega)=\sigma_\alpha^*(\mathrm{Ad}_{g^{-1}}\omega)$。此时 $g$ 依赖位置，于是得到 $\mathrm{Ad}_{g(x)^{-1}}A_\alpha=g^{-1}A_\alpha g$（对矩阵群，$\mathrm{Ad}$ 的作用就是矩阵共轭）。
4. **第二个贡献（移动 $g$）：** 固定点 $\sigma_\alpha(x)$ 而变动 $g(x)$ 是沿纤维移动。当 $g$ 变动时 $p\cdot g(x)$ 的速度是 $g^{-1}dg\in\mathfrak g$ 的基本向量场（这一组合是 $G$ 经 $g$ 拉回的 **Maurer–Cartan 形式**；它是衡量无穷小群运动的典范 $\mathfrak g$-值 1-形式 $\theta=g^{-1}dg$）。在基本向量场上 $\omega$ 返回其生成元（$\omega$ 定义的第一条），给出 $g^{-1}dg$。
5. 把两个贡献相加：
   $$
   A_\beta=g^{-1}A_\alpha\,g+g^{-1}\,dg.\qquad\blacksquare
   $$

同一个公式，若把 $g$ 读作*单片内依赖时空的规范变换*（群元素之丛的一个截面），就是物理学家的**规范变换** $A\mapsto g^{-1}Ag+g^{-1}dg$。

#### 阿贝尔情形与一个范例

对 $G=U(1)$，群元素是相位 $g=e^{i\chi(x)}$，李代数是 $i\mathbb{R}$（纯虚数）；因为 $U(1)$ 阿贝尔，共轭 $g^{-1}Ag=A$ 是平凡的，而 $g^{-1}dg=e^{-i\chi}\,d(e^{i\chi})=i\,d\chi$。写 $A=iqA_\mu^{\mathrm{phys}}dx^\mu$，变换律坍缩为
$$
A_\mu^{\mathrm{phys}}\ \mapsto\ A_\mu^{\mathrm{phys}}+\tfrac{1}{q}\,\partial_\mu\chi,
$$
这恰是熟悉的**电磁规范变换** $A_\mu\mapsto A_\mu+\partial_\mu\lambda$。几何重现了教科书里的规则。

> **陷阱。** 非齐次项 $g^{-1}dg$ 正是 $A$ *不是*张量（不是伴随丛的截面）的原因：它不齐次地变换。由规范变换相联系的两个势描述*同一物理*；只有规范不变量（曲率的迹、和乐）才是可观测的。

<a id="s6"></a>
### 曲率——曲率 2-形式与场强 $F=dA+A\wedge A$（推导变换律）

曲率衡量水平移动绕一个圈无法闭合的程度——等价地，衡量两个无穷小规范运动无法对易的程度。它就是场强。

#### 上方的定义

> **定义 — 曲率 2-形式。**
>
> 联络 $\omega$ 的**曲率 2-形式**为
> $$
> \Omega\ :=\ d\omega+\tfrac12[\omega,\omega]\ \in\ \Omega^2(P;\mathfrak{g}),
> $$
> 其中 $d$ 是外微分，$[\omega,\omega]$ 是取李括号值的楔积：在向量 $u,v$ 上，$[\omega,\omega](u,v)=2[\omega(u),\omega(v)]$。等价地 $\Omega=d\omega\circ(\mathrm{水平投影})$——曲率是 $d\omega$ 的*水平*部分（**Cartan 结构方程**）。

对矩阵群，括号是对易子，且 $\tfrac12[\omega,\omega]=\omega\wedge\omega$（矩阵楔积），所以 $\Omega=d\omega+\omega\wedge\omega$。

#### 局部场强

> **定义 — 场强。**
>
> 经规范 $\sigma_\alpha$ 拉回，**场强**为
> $$
> F\ :=\ \sigma_\alpha^*\Omega\ =\ dA+A\wedge A\ \in\ \Omega^2(U_\alpha;\mathfrak{g}),
> $$
> 这里用了 $\sigma^*d\omega=d\sigma^*\omega=dA$（拉回与 $d$ 交换）以及 $\sigma^*(\omega\wedge\omega)=A\wedge A$。在分量中，取 $A=A_\mu dx^\mu$，
> $$
> F=\tfrac12 F_{\mu\nu}\,dx^\mu\wedge dx^\nu,\qquad F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu+[A_\mu,A_\nu].
> $$

> **分量公式的推导。**
> 1. 由 $d$ 在 1-形式上的定义，$dA=d(A_\mu dx^\mu)=\partial_\nu A_\mu\,dx^\nu\wedge dx^\mu$。重新标记并反对称化，$dA=\tfrac12(\partial_\mu A_\nu-\partial_\nu A_\mu)dx^\mu\wedge dx^\nu$，因为 $dx^\nu\wedge dx^\mu=-dx^\mu\wedge dx^\nu$（楔积反对称）。
> 2. $A\wedge A=A_\mu A_\nu\,dx^\mu\wedge dx^\nu=\tfrac12[A_\mu,A_\nu]\,dx^\mu\wedge dx^\nu$：楔积把 $dx$ 反对称化，所以矩阵乘积 $A_\mu A_\nu$ 只剩下反对称部分存活，而由对易子定义 $A_\mu A_\nu-A_\nu A_\mu=[A_\mu,A_\nu]$。
> 3. 相加：$F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu+[A_\mu,A_\nu]$。$\blacksquare$

对 $U(1)$，对易子消失，$F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$——即**电磁场张量**，编码 $\mathbf E$ 与 $\mathbf B$。

#### $F$ 如何变换（规范协变性）

> **定理。** 在带转移 $g$ 的规范变换下，
> $$
> F_\beta\ =\ g^{-1}F_\alpha\,g\qquad(\text{即 }F\mapsto g^{-1}Fg,\text{ 齐次伴随变换}).
> $$

*证明。* 用 $A_\beta=g^{-1}A_\alpha g+g^{-1}dg$（s5）；写 $A=A_\alpha$，省去楔号，并简记 $h=g^{-1}$，故 $dh=-g^{-1}(dg)g^{-1}$。
1. **计算 $dA_\beta$。** $dA_\beta=d(g^{-1}Ag)+d(g^{-1}dg)$。由 $d$ 在矩阵值形式乘积上的 Leibniz 法则（$d$ 越过 1-形式时带符号），
   $$
   d(g^{-1}Ag)=(dg^{-1})Ag - g^{-1}A\,(dg)\cdot(-1)\ \to\ (dg^{-1})\wedge A\,g + g^{-1}(dA)g - g^{-1}A\wedge dg.
   $$
   这里 $dg^{-1}=-g^{-1}(dg)g^{-1}$（对 $g^{-1}g=\mathrm{id}$ 求微分）。且 $d(g^{-1}dg)=(dg^{-1})\wedge dg=-g^{-1}(dg)g^{-1}\wedge dg$。
2. **计算 $A_\beta\wedge A_\beta$。** 展开 $(g^{-1}Ag+g^{-1}dg)\wedge(g^{-1}Ag+g^{-1}dg)$ 得四项：
   $$
   g^{-1}A\wedge A\,g\ +\ g^{-1}A\,(dg)\ +\ g^{-1}(dg)g^{-1}A g\ +\ g^{-1}(dg)g^{-1}\wedge dg,
   $$
   利用 $g\,g^{-1}=\mathrm{id}$ 化简中间的因子。
3. **相加 $dA_\beta+A_\beta\wedge A_\beta$ 并消去。** 归并各项：
   - $g^{-1}(dA)g+g^{-1}(A\wedge A)g=g^{-1}F\,g$——这是想要的结果。
   - 第 1 步的项 $g^{-1}A\wedge dg$ 抵消第 2 步的 $+g^{-1}A\,dg$。
   - 项 $-g^{-1}(dg)g^{-1}\wedge Ag$（来自第 1 步的 $dg^{-1}\wedge Ag$）抵消第 2 步的 $+g^{-1}(dg)g^{-1}Ag$。
   - 两个纯 $dg$ 项 $-g^{-1}(dg)g^{-1}\wedge dg$（第 1 步）与 $+g^{-1}(dg)g^{-1}\wedge dg$（第 2 步）相消。
4. 一切非齐次项相消，余下 $F_\beta=g^{-1}F_\alpha\,g$。$\blacksquare$

> **为什么这很重要。** $F$ *齐次地*变换（在伴随表示中），所以它是伴随丛的真正截面——一个张量。于是像 $\mathrm{tr}(F\wedge\star F)$ 这样的规范不变组合是良定义的可观测量。物理场是曲率，而不是规范势。阿贝尔 $U(1)$ 情形更强：共轭是平凡的，所以 $F$ 是*完全规范不变的*——正如我们所知，电磁场 $\mathbf E,\mathbf B$ 是直接可测的。

#### Bianchi 恒等式

对 $F=dA+A\wedge A$ 求微分给出一个恒等式，它由定义自动成立，是 Maxwell 方程组一半的几何内容。

> **定理 — Bianchi 恒等式。** $\quad dF+[A,F]=0$，写作 $D_A F=0$，其中 $D_A$ 是规范协变外微分。

*证明。*
1. $dF=d(dA)+d(A\wedge A)=0+(dA)\wedge A-A\wedge dA$，因为 $d^2=0$（$d$ 的幂零性），且 1-形式的 Leibniz 法则带符号 $d(A\wedge A)=dA\wedge A-A\wedge dA$。
2. 现在 $[A,F]=A\wedge F-F\wedge A=A\wedge(dA+A\wedge A)-(dA+A\wedge A)\wedge A=A\wedge dA + A\wedge A\wedge A - dA\wedge A - A\wedge A\wedge A$。
3. 三重 $A$ 项相消；加到第 1 步：$dF+[A,F]=(dA\wedge A-A\wedge dA)+(A\wedge dA-dA\wedge A)=0$。$\blacksquare$

对 $U(1)$ 这就是 $dF=0$，即 $\partial_{[\lambda}F_{\mu\nu]}=0$——恰是齐次 Maxwell 方程 $\nabla\cdot\mathbf B=0$ 与 $\nabla\times\mathbf E=-\partial_t\mathbf B$。

## C 部分 · 移动、物质与动力学

<a id="s7"></a>
### 平行移动、和乐与 Wilson 圈

联络的职责是沿底道路移动纤维元素。绕一圈并测量净变换就是**和乐**；它的迹是 **Wilson 圈**，即基本的规范不变可观测量。

#### 平行移动

> **定义 — 水平提升与平行移动。**
>
> 设 $\gamma:[0,1]\to M$ 为一条光滑道路，$p_0\in P$ 为 $\gamma(0)$ 上的一点。**水平提升**是唯一的道路 $\tilde\gamma:[0,1]\to P$，满足 $\pi\circ\tilde\gamma=\gamma$、$\tilde\gamma(0)=p_0$ 且 $\tilde\gamma$ 水平（速度在 $H$ 中，即 $\omega(\dot{\tilde\gamma})=0$）。沿 $\gamma$ 的**平行移动**是由跟随该提升所诱导的映射 $E_{\gamma(0)}\to E_{\gamma(1)}$（在一个伴随丛上）。

提升的存在唯一性来自求解一阶常微分方程 $\omega(\dot{\tilde\gamma})=0$，在一个规范中它写成
$$
\frac{d}{dt}U(t)=-A_\mu\big(\gamma(t)\big)\,\dot\gamma^\mu(t)\,U(t),\qquad U(0)=\mathrm{id},
$$
其中 $U(t)\in G$ 是移动矩阵。由标准的存在唯一性定理（微分方程指南），这个线性常微分方程有唯一解。它的解是**路径序指数**
$$
U[\gamma]=\mathcal P\exp\!\Big(-\!\int_\gamma A\Big),
$$
其中路径序 $\mathcal P$ 把较晚时刻的因子放在左边，因为不同点处的 $A_\mu$ 一般不对易（在非阿贝尔情形）。

> **范例 — 阿贝尔移动。** 对 $U(1)$，$A$ 们对易，序无关紧要，且 $U[\gamma]=\exp\!\big(-\int_\gamma A\big)=\exp\!\big(-i q\int_\gamma A^{\mathrm{phys}}\big)$。一个带电粒子的波函数获得相位 $\exp(iq\int_\gamma A^{\mathrm{phys}})$——这是 Aharonov–Bohm 相位的几何起源（s11）。

#### 和乐

> **定义 — 和乐。** 对一个基于 $x$ 的*圈* $\gamma$（$\gamma(0)=\gamma(1)=x$），平行移动回到同一纤维 $E_x$，给出一个自同构 $U[\gamma]\in G$，即 $\gamma$ 的**和乐**。所有基于 $x$ 的和乐之集构成**和乐群** $\mathrm{Hol}_x\subseteq G$。

和乐是曲率的积分化的、有限的版本。**Ambrose–Singer 定理**断言和乐群的李代数由曲率 $F$ 在流形上取值张成——平坦联络（在单连通底上 $F=0$）有平凡和乐，而曲率恰是一个无穷小圈的无穷小和乐：
$$
U[\partial\Sigma]\approx \mathrm{id}-F_{\mu\nu}\,\tfrac12\,\Delta S^{\mu\nu}+\cdots
$$
对一个围出定向面积元 $\Delta S^{\mu\nu}$ 的小圈。这是"曲率 = 绕一个小圈后无法回到出发点"的精确含义。

#### Wilson 圈

和乐 $U[\gamma]$ 依赖于规范：在 $g$ 之下它共轭，$U[\gamma]\mapsto g(x)^{-1}U[\gamma]g(x)$。要得到一个规范不变的数，取**迹**。

> **定义 — Wilson 圈。** $\displaystyle W[\gamma]=\mathrm{tr}\,\mathcal P\exp\!\Big(-\oint_\gamma A\Big).$ 因为 $\mathrm{tr}(g^{-1}Ug)=\mathrm{tr}(U)$（迹的循环性），$W[\gamma]$ 是**规范不变的**，从而是一个真正的可观测量。Wilson 圈是格点规范理论的基本可观测量，并探测 QCD 中的禁闭（面积律行为）。

<a id="s8"></a>
### 伴随丛上的协变导数；与物质场的最小耦合

一个物质场是伴随向量丛 $E=P\times_\rho V$ 的一个截面 $\psi$。为写出场方程，我们必须对 $\psi$ 求微分，但普通导数不是规范协变的。联络提供了修正：**协变导数**。

#### 定义

> **定义 — 协变导数（规范导数）。**
>
> 设 $\rho:G\to GL(V)$ 为表示，$d\rho:\mathfrak g\to\mathfrak{gl}(V)$ 为其诱导的李代数表示。对一个截面 $\psi$（在一个规范中，是 $U$ 上的一个 $V$-值函数），**协变导数**为
> $$
> D\psi=d\psi+\rho_*(A)\,\psi,\qquad\text{逐分量地 } D_\mu\psi=\partial_\mu\psi+\rho_*(A_\mu)\,\psi,
> $$
> 其中 $\rho_*=d\rho$ 把代数元素 $A_\mu$ 表示为 $V$ 上的一个算子。对矩阵群的定义表示，$\rho_*(A_\mu)=A_\mu$ 通过矩阵乘法作用。

#### 规范协变性——这一构造的要点

> **定理。** 若 $\psi$ 在规范变换下变为 $\psi\mapsto\rho(g)^{-1}\psi$（伴随丛截面的变换律），且 $A$ 按 s5 变换，则 $D_\mu\psi$ *齐次地*变换：$D_\mu\psi\mapsto\rho(g)^{-1}D_\mu\psi$。

*证明（矩阵/定义表示，$\rho_*(A)=A$）。* 写 $\psi'=g^{-1}\psi$，$A'=g^{-1}Ag+g^{-1}dg$。
1. $D'_\mu\psi'=\partial_\mu(g^{-1}\psi)+A'_\mu(g^{-1}\psi)$。
2. 由乘积法则 $\partial_\mu(g^{-1}\psi)=(\partial_\mu g^{-1})\psi+g^{-1}\partial_\mu\psi$。且 $\partial_\mu g^{-1}=-g^{-1}(\partial_\mu g)g^{-1}$（对 $g^{-1}g=\mathrm{id}$ 求微分）。
3. $A'_\mu g^{-1}\psi=(g^{-1}A_\mu g+g^{-1}\partial_\mu g)g^{-1}\psi=g^{-1}A_\mu\psi+g^{-1}(\partial_\mu g)g^{-1}\psi$。
4. 把第 2、3 步相加：项 $-g^{-1}(\partial_\mu g)g^{-1}\psi$ 与 $+g^{-1}(\partial_\mu g)g^{-1}\psi$ 相消，余下
   $$
   D'_\mu\psi'=g^{-1}\partial_\mu\psi+g^{-1}A_\mu\psi=g^{-1}(\partial_\mu\psi+A_\mu\psi)=g^{-1}D_\mu\psi.\qquad\blacksquare
   $$

因为 $D_\mu\psi$ 像 $\psi$ 本身那样变换，任何以规范不变方式由 $\psi$ 与 $D\psi$ 构造的表达式（例如对一个酉表示的 $|D_\mu\psi|^2$）都是 Lagrange 量中合法的一项。$A$ 的非齐次部分*恰恰*是为了抵消 $\partial_\mu\psi$ 的非齐次部分而存在的。

#### 最小耦合

> **原理 — 最小耦合。** 要使一个物质理论规范不变，把每个普通导数替换为协变导数：$\partial_\mu\to D_\mu=\partial_\mu+A_\mu$。这单一替换引入了物质与规范场之间的相互作用，除 $A$ 之中的耦合常数外没有自由参数。

> **范例 — 规范化的 Schrödinger/Dirac 方程（$U(1)$）。** 此处 $\rho_*(A_\mu)=iqA^{\mathrm{phys}}_\mu$，故 $D_\mu=\partial_\mu+iqA_\mu$。自由 Schrödinger 方程 $i\partial_t\psi=-\tfrac{1}{2m}\nabla^2\psi$ 在最小耦合下变成 $i(\partial_t+iq\phi)\psi=-\tfrac{1}{2m}(\nabla-iq\mathbf A)^2\psi$——恰是电磁场中带电粒子的 Schrödinger 方程。相对论性的 Dirac 情形给出 $(i\gamma^\mu D_\mu-m)\psi=0$。Lorentz 力定律以及电荷与电磁场的全部相互作用都编码在 $\partial\to D$ 之中。

#### 曲率作为协变导数的对易子

一个干净的恒等式把 s6 与 s8 联系起来：
$$
[D_\mu,D_\nu]\psi=F_{\mu\nu}\,\psi.
$$
*证明。* $D_\mu D_\nu\psi=(\partial_\mu+A_\mu)(\partial_\nu\psi+A_\nu\psi)=\partial_\mu\partial_\nu\psi+(\partial_\mu A_\nu)\psi+A_\nu\partial_\mu\psi+A_\mu\partial_\nu\psi+A_\mu A_\nu\psi.$ 在 $\mu\nu$ 上反对称化：对称的 $\partial_\mu\partial_\nu\psi$ 与混合的一阶导数项相消，余下 $(\partial_\mu A_\nu-\partial_\nu A_\mu+A_\mu A_\nu-A_\nu A_\mu)\psi=F_{\mu\nu}\psi$。$\blacksquare$ 所以**场强是协变导数无法对易的障碍**——这是预备指南中 Riemann 张量作为协变导数对易子的规范理论回响。

<a id="s9"></a>
### Yang–Mills 理论——Yang–Mills 作用量与场方程；作为 $U(1)$ 情形的 Maxwell 方程（推导）

我们现在赋予规范场自身的动力学。原理是：由场强构造最简单的规范不变、Lorentz 不变的作用量。

#### Hodge 星与作用量

回顾（预备指南）一个定向（伪）Riemann $n$ 维流形上的 **Hodge 星** $\star$ 用度量把 $p$-形式映到 $(n-p)$-形式，且 $\int_M \alpha\wedge\star\beta$ 是形式的自然内积。对 $\mathfrak g$-值形式我们还取一个迹（$\mathfrak g$ 上的一个不变内积，在尺度意义下即 **Killing 形式**）。

> **定义 — Yang–Mills 作用量。**
> $$
> S_{\mathrm{YM}}[A]=-\frac{1}{2g^2}\int_M \mathrm{tr}\big(F\wedge\star F\big)=-\frac{1}{4g^2}\int_M \mathrm{tr}\big(F_{\mu\nu}F^{\mu\nu}\big)\sqrt{|h|}\,d^nx,
> $$
> 其中 $g$ 是**耦合常数**，$h$ 是度量行列式，指标用时空度量升降。被积式是规范不变的，因为 $F\mapsto g^{-1}Fg$ 而迹在共轭下不变（循环性）。

#### 场方程

> **定理 — Yang–Mills 方程。** 在 $A$ 上对 $S_{\mathrm{YM}}$ 取极值给出
> $$
> D\star F=0,\qquad\text{即}\qquad D_\mu F^{\mu\nu}=\partial_\mu F^{\mu\nu}+[A_\mu,F^{\mu\nu}]=0,
> $$
> 连同自动成立的 Bianchi 恒等式 $DF=0$（s6）。

*推导。*
1. 取变分 $A\to A+\delta A$，其中 $\delta A$ 是在边界上为零的 $\mathfrak g$-值 1-形式。由 $F=dA+A\wedge A$，一阶变化为 $\delta F=d(\delta A)+\delta A\wedge A+A\wedge\delta A=D(\delta A)$，其中 $D(\delta A)=d(\delta A)+[A,\delta A]$ 是协变外微分（这*定义*了 $D$ 在伴随值形式上的作用；括号来自 $\delta A\wedge A+A\wedge\delta A=[A,\delta A]$ 作为 2-形式）。
2. 于是 $\delta S_{\mathrm{YM}}=-\frac{1}{g^2}\int_M\mathrm{tr}\big(\delta F\wedge\star F\big)=-\frac{1}{g^2}\int_M\mathrm{tr}\big(D(\delta A)\wedge\star F\big)$，用了作用量在每个 $F$ 因子中的线性性以及迹配对的对称性。
3. **分部积分。** 对伴随值形式，$\mathrm{tr}\big(D(\delta A)\wedge\star F\big)=d\,\mathrm{tr}(\delta A\wedge\star F)\pm\mathrm{tr}\big(\delta A\wedge D\star F\big)$，这是 $D$ 的协变 Leibniz 法则与迹循环性的结合（联络项带符号地从一个因子转移到另一个）。全微分项积分成一个边界项，由于在 $\partial M$ 上 $\delta A=0$（Stokes 定理）而消失。
4. 于是 $\delta S_{\mathrm{YM}}=\pm\frac{1}{g^2}\int_M\mathrm{tr}\big(\delta A\wedge D\star F\big)$。要求它对*所有* $\delta A$ 消失，由变分法基本引理迫使 $D\star F=0$。$\blacksquare$

#### 作为 $U(1)$ 情形的 Maxwell 方程

> **推导。** 对 $G=U(1)$ 代数阿贝尔，所有括号消失，$F=dA$ 且 $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$，迹是平凡的。
> 1. Yang–Mills 方程 $D_\mu F^{\mu\nu}=0$ 失去括号项，变成 $\partial_\mu F^{\mu\nu}=0$。
> 2. 这是**无源非齐次 Maxwell 方程** $\partial_\mu F^{\mu\nu}=0$，即 $\nabla\cdot\mathbf E=0$ 与 $\nabla\times\mathbf B=\partial_t\mathbf E$（无电荷的 Gauss 与 Ampère）。
> 3. Bianchi 恒等式 $dF=0$（s6）给出**齐次 Maxwell 方程** $\nabla\cdot\mathbf B=0$、$\nabla\times\mathbf E=-\partial_t\mathbf B$。
> 4. 加入一个物质流 $J^\nu$（来自最小耦合的带电物质，s8）使作用量增加 $\int A_\mu J^\mu$，并给出 $\partial_\mu F^{\mu\nu}=J^\nu$——完整的非齐次 Maxwell 方程。
>
> 所以**全部四个 Maxwell 方程就是 $U(1)$ Yang–Mills 方程加 Bianchi。** 非阿贝尔的 $G$ 增添了自相互作用 $[A_\mu,F^{\mu\nu}]$：胶子携带色荷并彼此相互作用，不像光子。$\blacksquare$

> **陷阱。** 非阿贝尔 Yang–Mills 方程在 $A$ 中是*非线性的*（因为 $F$ 与 $D$ 都含 $A$）。这种非线性——在电磁学中不存在——是强力中渐近自由与禁闭的根源，并使方程困难得多（Yang–Mills 质量隙问题至今仍是一个千禧年大奖问题）。

## D 部分 · 拓扑与物理

<a id="s10"></a>
### 特征类——Chern 类与 Chern–Simons 形式；拓扑不变量

一个丛的某些性质无法被联络的任何光滑形变所改变——它们是**拓扑不变量**，由对曲率的多项式积分计算得出。这些就是**特征类**。它们用一个整数回答"这个丛有多扭曲？"。

#### Chern–Weil 理论

> **定理 — Chern–Weil。** 设 $P(F)$ 为曲率 $F$ 的一个 $\mathrm{Ad}$ 不变多项式（在 $F\mapsto g^{-1}Fg$ 下不变）。则微分形式 $P(F)$ 是**闭的**（$dP(F)=0$），且它的 **de Rham 上同调类与联络 $A$ 无关**。因此它在闭链上的积分是丛的拓扑不变量。

*$P(F)$ 为何闭合的概述。* 由不变性与 Bianchi 恒等式 $DF=0$：$F$ 的不变多项式的外微分可用 $DF$ 表出（由不变性，联络项组装成协变导数），而 $DF=0$ 把它消掉。与 $A$ 无关是因为两个联络的差 $P(F_1)-P(F_0)$ 是一个恰当形式（一个超渡项）。

#### Chern 类

对一个*复*向量丛（结构群 $U(k)$，即物理上最核心的情形），$\frac{i}{2\pi}F$ 的不变多项式给出 **Chern 类**。

> **定义 — Chern 类。** 展开**全 Chern 类**
> $$
> c(F)=\det\!\Big(\mathrm{id}+\tfrac{i}{2\pi}F\Big)=1+c_1(F)+c_2(F)+\cdots,
> $$
> 其中 $c_j(F)$ 是次数为 $2j$ 的部分。特别地：
> $$
> c_1=\tfrac{i}{2\pi}\,\mathrm{tr}\,F,\qquad c_2=\tfrac{1}{8\pi^2}\big(\mathrm{tr}\,F\wedge\mathrm{tr}\,F-\mathrm{tr}(F\wedge F)\big).
> $$
> 在闭子流形上的积分 $\int_\Sigma c_j$ 是**整数**（Chern 数）。

> **范例 — $S^2$ 上 $U(1)$ 丛的第一 Chern 数。** 此处 $F$ 是一个普通的（纯虚的）2-形式，$c_1=\frac{i}{2\pi}F$。积分
> $$
> n=\int_{S^2}c_1=\frac{i}{2\pi}\int_{S^2}F
> $$
> 被迫为整数：把 $S^2$ 分成北、南两顶帽，势 $A_N,A_S$ 在赤道上相差一个规范变换 $g=e^{in\phi}$。由 Stokes，$\int_{S^2}F=\oint_{\mathrm{eq}}(A_N-A_S)=\oint g^{-1}dg=2\pi i\,n$，给出整数 $n$。这个整数是 Dirac 单极子的**磁荷**（s11），也是量子 Hall 效应的 **TKNN 整数**——一个无法连续改变的拓扑不变量。

#### Chern–Simons 形式

Chern 类是*闭的*，但在局部上是*恰当的*：$c_j(F)=d(\text{某物})$。那个"某物"就是 **Chern–Simons 形式**。

> **定义 — Chern–Simons 3-形式。** 对第二 Chern 类，$\mathrm{tr}(F\wedge F)=d\,\mathrm{CS}(A)$，其中
> $$
> \mathrm{CS}(A)=\mathrm{tr}\Big(A\wedge dA+\tfrac{2}{3}A\wedge A\wedge A\Big).
> $$

*验证 $d\,\mathrm{CS}(A)=\mathrm{tr}(F\wedge F)$。*
1. $d\,\mathrm{tr}(A\wedge dA)=\mathrm{tr}(dA\wedge dA)$（$A\wedge d(dA)$ 项因 $d^2=0$ 消失）。
2. $d\,\mathrm{tr}(\tfrac23 A\wedge A\wedge A)=\tfrac23\cdot 3\,\mathrm{tr}(dA\wedge A\wedge A)=2\,\mathrm{tr}(dA\wedge A\wedge A)$（Leibniz；由循环性这三项在迹下相等）。
3. 同时 $\mathrm{tr}(F\wedge F)=\mathrm{tr}\big((dA+A^2)\wedge(dA+A^2)\big)=\mathrm{tr}(dA\wedge dA)+2\,\mathrm{tr}(dA\wedge A\wedge A)+\mathrm{tr}(A^4)$，而 $\mathrm{tr}(A^4)=\mathrm{tr}(A\wedge A\wedge A\wedge A)=0$，由循环性连同把一个 1-形式越过其他三个所带的符号。
4. 第 1+2 步精确重现第 3 步：$d\,\mathrm{CS}(A)=\mathrm{tr}(F\wedge F)$。$\blacksquare$

在一个 3 维流形上的积分 $\int_M\mathrm{CS}(A)$ 是 **Chern–Simons 作用量**，它是拓扑场论、分数量子 Hall 效应理论以及纽结不变量的基础。在大规范变换下它移动 $2\pi$ 乘以一个整数，这使它的耦合量子化（即"能级" $k$）。

<a id="s11"></a>
### 物理例子——Dirac 磁单极子与 Aharonov–Bohm 效应；关于瞬子的一段话

我们以展示这套抽象机器在三个里程碑式现象中的运作来收尾，每一个都是丛的*拓扑*在物理上可观测的地方。

#### Dirac 磁单极子

磁单极子是磁场 $\mathbf B=\frac{q_m}{4\pi}\frac{\hat r}{r^2}$ 的一个假想点源。于是 $\int_{S^2}\mathbf B\cdot d\mathbf S=q_m\ne 0$，所以 $F$ 穿过任何围绕它的球面有非零通量——但 $F=dA$ 会经 Stokes 迫使通量消失。其解决是几何的。

> **解决 — 没有整体的势；一个非平凡 $U(1)$ 丛。** $S^2$ 上没有单一光滑的 $A$；改用两个片（s10 的顶帽），势 $A_N,A_S$ 在赤道上由一个 $U(1)$ 规范变换 $g=e^{iq q_m\phi/(2\pi)}$ 相联系。当 $\phi\to\phi+2\pi$ 时 $g$ 的光滑性（单值性，因为 $\psi$ 是丛的截面而非函数）要求指数前进 $2\pi i$ 的整数倍：
> $$
> q\,q_m=2\pi n,\qquad n\in\mathbb{Z}.
> $$

这就是 **Dirac 量子化条件**：*单个磁单极子的存在迫使所有电荷都是某个基本单位的整数倍。* 整数 $n$ 恰是该丛的第一 Chern 数（s10）。$A$ 的所谓奇点（"Dirac 弦"）是试图在需要两片处只用一片所产生的规范赝象；诚实的描述是 $S^2$ 上一个非平凡的主 $U(1)$-丛。

#### Aharonov–Bohm 效应

取一个携带通量 $\Phi$ 的无限长螺线管，其外部 $\mathbf B=0$。一个电子穿过螺线管外的无场区域，从其两侧经过，两束发生干涉。

> **分析。** 在外部 $F=0$，所以联络是*平坦*的；经典上没有力作用（$\mathbf E=\mathbf B=0$）。然而绕过螺线管的圈的和乐（s7），由 Stokes 应用于所围的（非单连通）区域，为
> $$
> U[\gamma]=\exp\!\Big(iq\oint_\gamma\mathbf A\cdot d\mathbf l\Big)=\exp\!\Big(iq\!\int_\Sigma F\Big)=\exp(iq\Phi)\ne 1.
> $$
> 两条路径之间的相对相位 $q\Phi$ 移动了干涉条纹——这是电子从未进入过的一个区域的一个可测效应。

教训是：在规范理论中*势 $A$（联络），而不仅是场 $F$（曲率），具有物理实在性*——但只通过规范不变的和乐体现。这个效应是拓扑的：它只依赖于所围的通量，即依赖于绕这个非单连通区域的圈的同伦类，并由 Tonomura 在实验上证实。它是物理活在丛上、而非仅活在时空场上这一点最干净的演示。

#### 关于瞬子的一段话

在欧氏 $4$ 维 Yang–Mills 理论中，有限作用量的场位形由第二 Chern 数分类，
$$
\nu=\frac{1}{8\pi^2}\int_{\mathbb{R}^4}\mathrm{tr}(F\wedge F)\in\mathbb{Z},
$$
即**瞬子数**（拓扑荷）。$\nu\ne 0$ 的位形是**瞬子**：**自对偶**方程 $F=\star F$ 的局部化、有限作用量的解，它们自动满足 Yang–Mills 方程（自对偶加 Bianchi $DF=0$ 给出 $D\star F=DF=0$）。对 $SU(2)$，最小瞬子（$\nu=1$）是 BPST 解。瞬子在拓扑不同的真空之间媒介量子隧穿，解决 QCD 中的 $U(1)$ 问题，并支撑强 CP 问题。它们是本指南主题最生动的例子：一个*丛的拓扑不变量*控制着真实的物理。

> **收尾直觉。** 这里的每个现象对纯局部的分析都是不可见的——局部上 $A$ 是纯规范，$F$ 为零或是一个温顺的场——然而每一个都产生一个由整数控制的可测效应：一个 Chern 数、一个绕数、一个瞬子荷。这就是丛几何的标志：纤维如何粘合的整体拓扑是物理的。

---

*本指南从头开始搭建了规范理论——纤维丛与向量丛、截面与标架、主丛及其伴随物质丛、作为水平分布以及作为 $1$-形式 $\omega$ 的联络、局部势 $A$ 及其非齐次规范律、齐次变换的曲率 $F=dA+A\wedge A$、平行移动与和乐、协变导数与最小耦合、以 Maxwell 作为其阿贝尔影子的 Yang–Mills 作用量，最后是把曲率积分化为整数的 Chern 类与 Chern–Simons 形式。其下贯穿一切的单一思想是：一个力就是一个联络——跨时空比较内部状态需要一个选择，规范对称性是那个选择中的自由，而曲率是不可避免的、可观测的残余。把任何带框的定义或带编号的推导当作参考随时回看——并记住最深刻的物理常常不住在时空之上的场中，而住在它上方纤维如何粘合的拓扑里。*
