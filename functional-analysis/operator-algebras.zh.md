[English](operator-algebras.md) · **中文**

# 算子代数与代数量子场论，*作为代数的量子理论。*

*一门严格的算子代数入门课程，围绕一个视角转换展开：我们不再固定一个 Hilbert 空间并从中读出可观测量，而是把**可观测量代数**当作首要对象，让 Hilbert 空间作为表示而出现。我们从 Banach 代数与 C\*-恒等式出发，经过把交换 C\*-代数变成空间的 Gelfand 理论、从态重建 Hilbert 空间的 GNS 构造、von Neumann 代数与双交换子定理、因子的 Murray–von Neumann 分类、模理论，最终抵达正则对易关系与代数量子场论的 Haag–Kastler 公理。每个术语在首次出现时都被定义，每条定理都给出证明或给出其关键步骤的证明，且每一步都注明其依据。*

[← 返回全部指南](../README.zh.md)

> **如何阅读本指南。** 我们假定读者熟悉**泛函分析与 Hilbert 空间**指南（Banach 空间、Hilbert 空间、有界算子、伴随、有界算子的谱、谱定理）。当我们用到其中的事实时，会用一行话重述它。所有算子代数特有的内容——*Banach 代数*、*C\*-代数*、*代数中的谱*、*Gelfand 变换*、*态*、*GNS 表示*、*von Neumann 代数*、*因子*、*迹*、*模自同构*、*CCR/CAR*、*局部可观测量网*——都在首次出现处定义，并配有具体的数值例子。没有什么是"留给读者"的。在物理能照亮数学的地方我们会指出来，但这是一门**数学**指南：论断都被证明。

---

## A 部分 — 可观测量的代数

<a id="s0"></a>
### 为什么用代数：可观测量先于态

在通常的量子力学中，人们固定一个 Hilbert 空间 $\mathcal H$——对单个粒子是 $L^2(\mathbb R)$——并声明**态**是单位向量 $\psi\in\mathcal H$（至多差一个相位），而**可观测量**是 $\mathcal H$ 上的自伴算子。这就是*以 Hilbert 空间为先*的图景，对单个粒子它运作得极为漂亮。

但它有一个隐藏的假设：存在一个天赋的、人人通用的 Hilbert 空间。在量子统计力学（无穷多粒子、热平衡）和量子场论（无穷多自由度，空间每一点对应一个）中，这个假设失效了。把同一组物理可观测量在 Hilbert 空间上表示出来有不等价的方式——*不等价表示*——过早地选定其中一个就丢弃了物理。**Haag 定理**（我们将在 s11 抵达）直截了当地说：场论的相互作用绘景根本不可能存在于自由场的 Hilbert 空间上。

由 von Neumann、Segal、Haag 和 Kastler 提出的**量子理论的代数方法**通过颠倒构造顺序修补了这一点。我们把可观测量的集合连同我们能对它们施行的运算当作首要对象：

- 我们可以把两个可观测量相加并对其作数乘（线性结构）；
- 我们可以把它们相乘（一个代数——运算的复合，或者把多次测量的乘积兼容化）；
- 我们可以构造伴随 $A^*$（"复共轭转置"的抽象版本，编码了真实测量是自伴的这一事实，$A=A^*$）；
- 而且我们有一个范数 $\|A\|$，度量可观测量所能取到的最大值。

把这四样东西——以及它们之间恰到好处的相容性，即 **C\*-恒等式** $\|A^*A\|=\|A\|^2$——打包在一起的结构，就是 **C\*-代数**。整本指南的口号是：

> 一个量子系统是一个可观测量的 C\*-代数 $\mathcal A$。一个**态**不是一个向量，而是一个归一化的正线性泛函 $\omega:\mathcal A\to\mathbb C$，它给每个可观测量赋予其期望值 $\omega(A)=\langle A\rangle$。Hilbert 空间是*导出的*：每个态 $\omega$ 都通过 **GNS 构造**建立自己的表示。

这不仅仅是一个推广；它是一次重组，使正确的东西成为首要的。期望值 $\langle A\rangle$ 才是实验所测量的，所以"态即泛函"比"态即向量"更贴近物理。又因为许多不等价的 Hilbert 空间表示可以承载同一个代数，所以代数才是那个不变的、与观察者无关的对象。

> **物理上的着力点。** 在 Hilbert 空间图景中你问"波函数是什么？"在代数图景中你问"每个可观测量的期望值是什么？"——而波函数（当它存在时）是从这些数重建出来的。后一个问题总有答案；前一个有时没有。

计划如下：定义 Banach 代数与 C\*-代数（s1），理解抽象代数内部的谱（s2），证明交换 C\*-代数*恰好*是某个空间上函数的代数（s3，Gelfand），从态建立 Hilbert 空间（s4，GNS），研究表示（s5），然后丰富到 von Neumann 代数（s6），对它们分类（s7），加入迹与模理论（s8），用代数方式实现正则对易关系（s9），最后组装出代数量子场论的公理（s10–s11）。

<a id="s1"></a>
### Banach 代数与 C\*-代数

**是什么以及为什么。** 我们想要一个集合，其元素能相加、数乘、相乘，并能度量大小，所有这些都连续地配合在一起，使极限的行为良好。这就是 Banach 代数。加上一个伴随，再加上一条把伴随与范数联系起来的恒等式，就得到 C\*-代数——"Hilbert 空间上算子"的抽象提炼。

我们从泛函分析指南中回顾：一个**赋范向量空间**是 $\mathbb C$ 上的向量空间 $V$ 连同一个函数 $\|\cdot\|:V\to[0,\infty)$，满足 $\|v\|=0\iff v=0$、$\|\lambda v\|=|\lambda|\,\|v\|$ 以及三角不等式 $\|v+w\|\le\|v\|+\|w\|$；如果它是完备的（每个 Cauchy 列都收敛），它就是一个 **Banach 空间**。

> **定义 — 代数。** 一个（结合的、含单位的、复的）**代数**是一个复向量空间 $\mathcal A$，连同一个乘法 $\mathcal A\times\mathcal A\to\mathcal A$，记作 $(a,b)\mapsto ab$，它是结合的（$(ab)c=a(bc)$）、双线性的（对每个变元线性）、并有一个**单位** $1\in\mathcal A$，对所有 $a$ 满足 $1a=a1=a$。如果对所有 $a,b$ 有 $ab=ba$，则该代数是**交换的**。

> **定义 — Banach 代数。** 一个 **Banach 代数**是一个代数 $\mathcal A$，它同时是一个 Banach 空间，其范数是**次乘性的**：
>
> $$
> \|ab\|\le\|a\|\,\|b\|\qquad\text{for all }a,b\in\mathcal A,
> $$
>
> 且（对于本文通篇所用的含单位情形）$\|1\|=1$。

次乘性恰好使乘法连续：若 $a_n\to a$ 且 $b_n\to b$，则 $a_nb_n\to ab$，因为 $\|a_nb_n-ab\|\le\|a_n\|\,\|b_n-b\|+\|a_n-a\|\,\|b\|\to0$（三角不等式、次乘性，以及收敛列 $\|a_n\|$ 的有界性）。

> **定义 — 对合与 \*-代数。** 代数 $\mathcal A$ 上的一个**对合**是一个映射 $a\mapsto a^*$，它是共轭线性的（$(\lambda a+b)^*=\overline\lambda\,a^*+b^*$）、反转乘积（$(ab)^*=b^*a^*$）、并且是自身的逆（$(a^*)^*=a$）。带有对合的代数是一个 **\*-代数**。元素 $a^*$ 是 $a$ 的**伴随**。若 $a=a^*$ 则元素是**自伴的**，若 $a^*a=aa^*$ 则是**正规的**，而（在含单位代数中）若 $a^*a=aa^*=1$ 则是**酉的**。

> **定义 — C\*-代数。** 一个 **C\*-代数**是一个 Banach \*-代数 $\mathcal A$，其范数满足 **C\*-恒等式**：
>
> $$
> \|a^*a\|=\|a\|^2\qquad\text{for all }a\in\mathcal A.
> $$

C\*-恒等式看似平淡无奇，却异常刚硬：它从代数结构中唯一地钉死了范数（我们将在 s2 看到范数等于一个谱半径），所以一个 C\*-代数*至多有一个* C\*-范数。这就是为什么抽象代数本身、而非任何手工选定的范数，才是那个不变的对象。

我们将不断用到的第一个推论：对合是**等距的**。事实上，由 C\*-恒等式与次乘性，
$$
\|a\|^2=\|a^*a\|\le\|a^*\|\,\|a\|,
$$
所以除以 $\|a\|$（对 $a\ne0$）得到 $\|a\|\le\|a^*\|$。把 $a$ 换成 $a^*$ 并利用 $(a^*)^*=a$ 得到 $\|a^*\|\le\|a\|$。故 $\|a^*\|=\|a\|$。*（C\*-恒等式；次乘性；对合是对合。）*

> **定义 — 需记在心的例子。**
> 1. **矩阵** $M_n(\mathbb C)$，即 $n\times n$ 复矩阵，配以矩阵乘法、伴随 $a^*=\overline{a}^{\,\mathsf T}$（共轭转置）以及算子范数 $\|a\|=\sup_{\|x\|=1}\|ax\|$。这是一个非交换的 C\*-代数（对 $n\ge2$）。
> 2. **连续函数** $C(X)$，定义在紧 Hausdorff 空间 $X$ 上，配以逐点运算、对合 $f^*=\overline f$（复共轭）以及上确界范数 $\|f\|=\sup_{x\in X}|f(x)|$。这是一个*交换*的 C\*-代数。（一个空间 $X$ 是**紧 Hausdorff** 的，如果它的每个开覆盖都有有限子覆盖，且不同的点有不相交的邻域。）
> 3. **有界算子** $B(\mathcal H)$，定义在 Hilbert 空间 $\mathcal H$ 上，配以复合、Hilbert 空间伴随以及算子范数。这是一切 C\*-代数之母。

**对 $M_n(\mathbb C)$ 验证 C\*-恒等式——例题。** 先平凡地取 $n=1$：一个 $1\times1$ 矩阵是一个数 $z$，$z^*=\overline z$，$\|z\|=|z|$，而 $\|z^*z\|=|\,\overline z z\,|=|z|^2=\|z\|^2$。对一般的 $n$，设 $a\in M_n(\mathbb C)$。算子范数满足 $\|a\|^2=\sup_{\|x\|=1}\|ax\|^2=\sup_{\|x\|=1}\langle ax,ax\rangle=\sup_{\|x\|=1}\langle a^*ax,x\rangle$（伴随的定义）。矩阵 $a^*a$ 是自伴且正的，所以由有限维谱定理它有一组带非负本征值的标准正交本征基；$\langle a^*ax,x\rangle$ 在单位 $x$ 上的上确界就是它的最大本征值 $\lambda_{\max}$。但 $\lambda_{\max}$ 也是 $\|a^*a\|$，即自伴算子 $a^*a$ 的算子范数（其范数等于其谱半径，即最大的 $|\lambda|$）。故 $\|a\|^2=\lambda_{\max}=\|a^*a\|$。*（算子范数的定义；伴随的定义；对正自伴矩阵 $a^*a$ 用谱定理。）*

**易错点。** 次乘性 $\|ab\|\le\|a\|\|b\|$ 一般是*严格*的：取 $a=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}$ 则 $a^2=0$，故 $\|a^2\|=0<\|a\|^2$。C\*-恒等式之所以特殊，正是因为它在组合 $a^*a$ 上强制了*等式*。

<a id="s2"></a>
### 谱、谱半径与 Gelfand–Mazur

**是什么以及为什么。** 在单个矩阵中，本征值是那些使 $a-\lambda 1$ 不可逆的数 $\lambda$。同样的定义在任何 Banach 代数中都成立，无需引用向量或本征向量——它纯粹关乎可逆性。这个"代数中的谱"是从代数通向数的桥梁，是后续一切的基础。

> **定义 — 可逆、谱、预解式。** 设 $\mathcal A$ 是含单位的 Banach 代数，$a\in\mathcal A$。若存在 $b\in\mathcal A$ 使 $ab=ba=1$，则称 $a$ **可逆**。$a$ 的**谱**是
>
> $$
> \sigma(a)=\{\lambda\in\mathbb C:\ a-\lambda 1\ \text{is not invertible in }\mathcal A\}.
> $$
>
> 其补集 $\rho(a)=\mathbb C\setminus\sigma(a)$ 是**预解集**，而对 $\lambda\in\rho(a)$，元素 $(a-\lambda1)^{-1}$ 是**预解式**。

> **引理 — Neumann 级数（在 1 附近的可逆性）。** 若 $\|x\|<1$，则 $1-x$ 可逆，且 $(1-x)^{-1}=\sum_{k=0}^\infty x^k$。

**证明。**
1. 部分和 $s_n=\sum_{k=0}^n x^k$ 构成 Cauchy 列：对 $m>n$，$\|s_m-s_n\|\le\sum_{k=n+1}^m\|x\|^k\le\sum_{k=n+1}^\infty\|x\|^k=\dfrac{\|x\|^{n+1}}{1-\|x\|}\to0$。*（三角不等式；次乘性给出 $\|x^k\|\le\|x\|^k$；几何级数，因 $\|x\|<1$ 而有效。）*
2. 由于 $\mathcal A$ 完备，$s_n\to s:=\sum_{k\ge0}x^k$ 存在。*（Banach 空间完备性。）*
3. 由裂项相消计算 $(1-x)s_n=s_n(1-x)=1-x^{n+1}$。令 $n\to\infty$：$\|x^{n+1}\|\le\|x\|^{n+1}\to0$，且乘法连续，故 $(1-x)s=s(1-x)=1$。*（裂项相消；乘法的连续性。）*
4. 于是 $s$ 是 $1-x$ 的双边逆。$\blacksquare$

> **定理 — 谱是非空、紧的，且由范数界定。** 对含单位 Banach 代数中的任何 $a$，$\sigma(a)$ 是 $\mathbb C$ 的非空紧子集，含于圆盘 $\{|\lambda|\le\|a\|\}$ 中。

**证明（关键步骤）。**
1. *有界性。* 若 $|\lambda|>\|a\|$，则 $a-\lambda1=-\lambda(1-\lambda^{-1}a)$ 且 $\|\lambda^{-1}a\|=\|a\|/|\lambda|<1$，所以由 Neumann 级数 $1-\lambda^{-1}a$ 可逆；故 $a-\lambda1$ 可逆，$\lambda\notin\sigma(a)$。于是 $\sigma(a)\subseteq\{|\lambda|\le\|a\|\}$。*（Neumann 引理。）*
2. *闭性。* 可逆元素的集合是开的（若 $b$ 可逆且 $\|c-b\|<1/\|b^{-1}\|$，则 $c=b(1-b^{-1}(b-c))$ 由 Neumann 级数可逆），且 $\lambda\mapsto a-\lambda1$ 连续，所以 $\rho(a)$ 开而 $\sigma(a)$ 闭。在 $\mathbb C$ 中既闭又有界即紧。*（可逆元的开性；连续映射下开集的原像是开集。）*
3. *非空性。* 预解式 $R(\lambda)=(a-\lambda1)^{-1}$ 是 $\rho(a)$ 上一个解析的 $\mathcal A$-值函数（其导数为 $R(\lambda)^2$，来自预解恒等式）。若 $\sigma(a)$ 为空，则 $R$ 是整的，且当 $|\lambda|\to\infty$ 时 $\|R(\lambda)\|\to0$：由 $R(\lambda)=-\lambda^{-1}(1-\lambda^{-1}a)^{-1}$ 及 Neumann 级数得 $\|R(\lambda)\|\le|\lambda|^{-1}/(1-\|a\|/|\lambda|)\to0$。由 Banach 空间值的 **Liouville 定理**（对任一有界线性泛函 $\phi$：$\phi(R(\lambda))$ 是有界整标量函数，故为常数；因其在无穷处消失，故为 $0$；对所有 $\phi$ 成立，故由 Hahn–Banach 得 $R\equiv0$），有 $R\equiv0$——这不可能，因为 $R(\lambda)$ 可逆。矛盾。$\blacksquare$

> **定义 — 谱半径。** $a$ 的**谱半径**是 $r(a)=\sup\{|\lambda|:\lambda\in\sigma(a)\}$（因 $\sigma(a)$ 非空且有界而良定义）。

> **定理 — Gelfand 谱半径公式。** $\displaystyle r(a)=\lim_{n\to\infty}\|a^n\|^{1/n}=\inf_{n\ge1}\|a^n\|^{1/n}.$

证明用到 $R(\lambda)$ 有一个 Laurent 展开 $\sum_{n\ge0}\lambda^{-n-1}a^n$，对 $|\lambda|>r(a)$ 收敛，其收敛半径由 $\limsup\|a^n\|^{1/n}$ 支配；匹配半径即得公式。我们陈述它；我们所需的推论在下面。

> **推论 — C\*-范数是一个谱半径。** 在 C\*-代数中，对自伴的 $a$，$\|a\|=r(a)$。

**证明。**
1. 对自伴的 $a$，C\*-恒等式给出 $\|a^2\|=\|a^*a\|=\|a\|^2$。*（取 $a^*=a$ 的 C\*-恒等式。）*
2. 迭代之，由归纳法 $\|a^{2^k}\|=\|a\|^{2^k}$：假设 $\|a^{2^k}\|=\|a\|^{2^k}$，注意 $a^{2^k}$ 自伴，故 $\|a^{2^{k+1}}\|=\|(a^{2^k})^2\|=\|a^{2^k}\|^2=\|a\|^{2^{k+1}}$。*（把步骤 1 用于自伴的 $a^{2^k}$。）*
3. 于是对所有 $k$ 有 $\|a^{2^k}\|^{1/2^k}=\|a\|$，所以谱半径公式中的极限等于 $\|a\|$：$r(a)=\|a\|$。*（沿子列 $n=2^k$ 用谱半径公式。）* $\blacksquare$

这就是前面所承诺的刚性：自伴元的范数由谱决定，从而由代数决定。由于对*每个* $a$ 都有 $\|a\|^2=\|a^*a\|=r(a^*a)$（因 $a^*a$ 自伴），整个范数都是由代数决定的。

> **定理 — Gelfand–Mazur。** 一个含单位的 Banach 代数，若其中每个非零元素都可逆（一个**可除代数**），则它等距同构于 $\mathbb C$。

**证明。**
1. 取任一 $a\in\mathcal A$。由非空性定理，$\sigma(a)\ne\emptyset$；取 $\lambda\in\sigma(a)$。*（谱非空。）*
2. 则 $a-\lambda1$ 不可逆。由假设，唯一不可逆的元素是 $0$，所以 $a-\lambda1=0$，即 $a=\lambda1$。*（可除代数假设。）*
3. 于是每个元素都是 $1$ 的数乘；映射 $\lambda1\mapsto\lambda$ 是到 $\mathbb C$ 上的等距代数同构。$\blacksquare$

**例题。** 在 $M_2(\mathbb C)$ 中取 $a=\begin{psmallmatrix}2&0\\0&3\end{psmallmatrix}$。则 $a-\lambda1$ 恰当 $\det\begin{psmallmatrix}2-\lambda&0\\0&3-\lambda\end{psmallmatrix}=(2-\lambda)(3-\lambda)=0$ 时不可逆，所以 $\sigma(a)=\{2,3\}$，$r(a)=3=\|a\|$（与推论一致，因 $a$ 自伴），确认了代数中的谱重现了通常的本征值。

**例题 — 谱半径可以小于范数。** 取幂零元 $a=\begin{psmallmatrix}0&5\\0&0\end{psmallmatrix}$。则 $a^2=0$，所以由半径公式 $r(a)=\lim\|a^n\|^{1/n}=0$：谱是 $\sigma(a)=\{0\}$。然而 $\|a\|=5\ne0$。这*并不*与 s2 推论矛盾，因为 $a$ **不是**自伴的（$a^*=\begin{psmallmatrix}0&0\\5&0\end{psmallmatrix}\ne a$）；等式 $\|a\|=r(a)$ 是正规元素的特权。这个教训通篇都很重要：对一般元素，范数看到的比谱更多，只有 C\*-恒等式（作用在*自伴*组合 $a^*a$ 上，对它 $r(a^*a)=\|a^*a\|=\|a\|^2=25$）才能恢复出范数。

**易错点 — 谱依赖于所在的代数（还是不依赖？）。** 先验地，若我们扩大代数（有更多元素可作为逆），$\sigma(a)$ 可能收缩。对 Banach 代数，谱在嵌入下确实可能改变。一个 C\*-代数特有的愉快定理是**谱不变性（spectral permanence）**：若 $\mathcal B\subseteq\mathcal A$ 是含单位的 C\*-子代数，则对每个 $a\in\mathcal B$ 有 $\sigma_{\mathcal B}(a)=\sigma_{\mathcal A}(a)$。谱是内蕴的——在哪个 C\*-代数里计算它都无所谓。正是这一点让我们能够谈论"一个可观测量的谱"而无需指明表示。

<a id="s3"></a>
### 交换 C\*-代数与 Gelfand 变换

**是什么以及为什么。** 例子 $C(X)$——紧 Hausdorff 空间上的连续函数——是交换的。Gelfand 的伟大定理说反过来也对：*每个*交换含单位 C\*-代数都是某个紧 Hausdorff 空间 $X$ 上的 $C(X)$，而 $X$ 作为"求值映射"的空间被恢复出来。这是代数与几何之间的完美字典，也是谱定理背后的抽象引擎。

> **定义 — 特征标。** 交换含单位 Banach 代数 $\mathcal A$ 的一个**特征标**（或乘性线性泛函）是一个非零的代数同态 $\chi:\mathcal A\to\mathbb C$：它线性、$\chi(ab)=\chi(a)\chi(b)$ 且 $\chi(1)=1$。所有特征标的集合是**谱**（或**极大理想空间**）$\widehat{\mathcal A}$，也称作 **Gelfand 谱**。

> **引理 — 特征标自动有界，$\|\chi\|=1$，且 $\chi(a)\in\sigma(a)$。**

**证明。**
1. 对 $\|a\|<1$ 的 $a$，$1-a$ 可逆（Neumann 级数），而同态把可逆元送到可逆元（非零标量），所以 $\chi(1-a)=1-\chi(a)\ne0$；这排除了 $\|a\|<1$ 时 $|\chi(a)|\ge1$ 的可能。经放缩，$|\chi(a)|\le\|a\|$，所以 $\chi$ 有界且 $\|\chi\|\le1$；而 $\chi(1)=1$ 给出 $\|\chi\|=1$。*（Neumann；同态保持可逆性。）*
2. 元素 $a-\chi(a)1$ 满足 $\chi(a-\chi(a)1)=0$，所以它落在 $\chi$ 的核中，那是一个真理想，因而不可逆；故 $\chi(a)\in\sigma(a)$。*（特征标的核是一个极大理想，其中不含可逆元。）* $\blacksquare$

> **定义 — 弱\* 拓扑与 Gelfand 变换。** 给 $\widehat{\mathcal A}$ 赋予**弱\* 拓扑**：使每个求值 $\chi\mapsto\chi(a)$ 连续的最弱拓扑。**Gelfand 变换**把 $a\in\mathcal A$ 送到函数 $\widehat a:\widehat{\mathcal A}\to\mathbb C$，$\widehat a(\chi)=\chi(a)$。

由引理，$\widehat{\mathcal A}$ 位于对偶 $\mathcal A^*$ 的闭单位球内，而后者由 **Banach–Alaoglu 定理**（泛函分析指南中的事实：对偶空间的闭单位球是弱\*-紧的）是**弱\*-紧的**。可验证 $\widehat{\mathcal A}$ 弱\*-闭，因而是紧 Hausdorff 的。所以 $\widehat a\in C(\widehat{\mathcal A})$ 总成立。

> **定理 — Gelfand–Naimark（交换情形）。** 设 $\mathcal A$ 是交换含单位 C\*-代数。Gelfand 变换 $a\mapsto\widehat a$ 是一个等距 \*-同构
>
> $$
> \mathcal A\ \xrightarrow{\ \cong\ }\ C(\widehat{\mathcal A}).
> $$
>
> 也就是说：它线性、乘性，把 $a^*$ 送到 $\overline{\widehat a}$，保范，并且是到整个 $C(\widehat{\mathcal A})$ 的双射。

**证明（关键步骤）。**
1. *同态。* $\widehat{ab}(\chi)=\chi(ab)=\chi(a)\chi(b)=\widehat a(\chi)\widehat b(\chi)$，线性性显然；所以 $a\mapsto\widehat a$ 是代数同态。*（特征标的定义。）*
2. *$\widehat a$ 的值域是谱。* 在交换情形中，$\lambda\in\sigma(a)$ 当且仅当对某个特征标 $\chi$ 有 $\lambda=\chi(a)$（每个极大理想都是唯一一个特征标的核）。故 $\widehat a(\widehat{\mathcal A})=\sigma(a)$。*（特征标与极大理想的对应，交换 Banach 代数所特有。）*
3. *等距。* 对自伴的 $a$，由 s2 推论 $\|\widehat a\|_\infty=\sup_\chi|\chi(a)|=\sup\{|\lambda|:\lambda\in\sigma(a)\}=r(a)=\|a\|$。对一般的 $a$，$\|\widehat a\|_\infty^2=\|\,\overline{\widehat a}\,\widehat a\,\|_\infty=\|\widehat{a^*a}\|_\infty=\|a^*a\|=\|a\|^2$，这里把自伴情形用在 $a^*a$ 上并用了 C\*-恒等式。所以映射等距，因而单射。*（s2 推论；C\*-恒等式。）*
4. *保 \*。* 对自伴的 $a$，$\sigma(a)\subseteq\mathbb R$（自伴元的谱是实的——s4 中借助态证明，或者直接借助 $\|e^{ita}\|=1$），所以 $\widehat a$ 取实值，再把 $a$ 分解为实部与虚部 $a=\frac{a+a^*}2+i\frac{a-a^*}{2i}$，即可对一般元素推出 $\widehat{a^*}=\overline{\widehat a}$。*（自伴元谱的实性。）*
5. *满射。* 像是 $C(\widehat{\mathcal A})$ 的一个 \*-子代数，它含有常数、分离点（若 $\chi_1\ne\chi_2$，它们在某个 $a$ 上不同，所以 $\widehat a$ 分离它们），并且是闭的（完备空间的等距像）。**Stone–Weierstrass 定理**（$C(X)$ 的自伴、分离点、含单位的子代数是稠密的）迫使该像就是整个 $C(\widehat{\mathcal A})$。$\blacksquare$

这是一个真正的*对偶*：交换含单位 C\*-代数与紧 Hausdorff 空间是同一份数据的两种看法。"非交换几何"就是把一般（非交换）C\*-代数当作某个没有底层点集的"量子空间"上函数代数来处理的纲领。

> **推论 — 连续函数演算。** 若 $a$ 是 C\*-代数的一个正规元素，则它生成的 C\*-子代数 $\cong C(\sigma(a))$，在此同构下 $a\leftrightarrow(\text{恒等函数 }z\mapsto z)$。于是对任意连续 $f:\sigma(a)\to\mathbb C$，都有一个良定义的元素 $f(a)$，且 $\|f(a)\|=\sup_{z\in\sigma(a)}|f(z)|$。

**例题。** 设 $\mathcal A=C[0,1]$，即 $[0,1]$ 上的连续函数。它的特征标*恰好*是点求值 $\chi_t(f)=f(t)$，$t\in[0,1]$：任何特征标都由其在坐标函数 $g(x)=x$ 上的值确定，即 $\chi(g)=t\in\sigma(g)=[0,1]$，然后对多项式 $f$ 有 $\chi(f)=f(t)$，再由稠密性对所有 $f$ 成立。所以 $\widehat{\mathcal A}\cong[0,1]$，而 Gelfand 变换是恒等映射 $C[0,1]\to C[0,1]$。我们出发时的空间正是 Gelfand 重建出来的空间。

**例题 — 把本征值作为 Gelfand 谱恢复出来。** 设 $a=\begin{psmallmatrix}2&0\\0&3\end{psmallmatrix}\in M_2(\mathbb C)$，并令 $\mathcal A$ 是它与 $1$ 一起生成的交换 C\*-子代数——也就是 $a$ 的所有多项式，这里就是对角矩阵 $\{\mathrm{diag}(\alpha,\beta)\}\cong\mathbb C^2$。一个特征标必须把投影 $p=\begin{psmallmatrix}1&0\\0&0\end{psmallmatrix}$ 送到一个数 $\chi(p)$，满足 $\chi(p)^2=\chi(p^2)=\chi(p)$，所以 $\chi(p)\in\{0,1\}$；两种选择给出两个求值"读第 $1$ 个元"和"读第 $2$ 个元"。因此 $\widehat{\mathcal A}$ 是一个两点空间，而 Gelfand 变换把 $a$ 送到函数 $\{1,2\}\to\mathbb C$，取值 $2$ 和 $3$。该函数的值域 $\{2,3\}$ 恰是 $\sigma(a)$：Gelfand 把矩阵变成了*视为谱上函数的它的本征值列表*。这正是连续函数演算的实际运作——$f(a)$ 是矩阵 $\mathrm{diag}(f(2),f(3))$。

**直觉。** Gelfand 对偶说的是"可观测量的交换代数与经典相空间是一回事"。一个*经典*系统由空间（态）上的函数（可观测量）描述；Gelfand 说任何交换 C\*-代数**就是**这样一个函数代数，其空间 $\widehat{\mathcal A}$ 是从代数重建出来的。而量子力学恰恰是当可观测量代数被允许*非交换*时所发生的事——此时没有底层的点空间，只有代数。这一句话就是非交换几何的概念种子。

## B 部分 — 态、表示与 GNS 构造

<a id="s4"></a>
### 正元素、态与 GNS 构造

**是什么以及为什么。** 我们现在能纯代数地精确说出"态"是什么（一个归一化的正泛函，一种期望值的赋予），然后施行本学科的核心奇迹：从单个态我们重建出一个 Hilbert 空间和一个表示，在其中该态变成某个向量 $\Omega$ 的 $\langle\Omega,\cdot\,\Omega\rangle$。这就是 **GNS 构造**（Gelfand–Naimark–Segal），从代数回到 Hilbert 空间的桥梁。

> **定义 — 正元素。** 在 C\*-代数 $\mathcal A$ 中，若 $a$ 自伴且 $\sigma(a)\subseteq[0,\infty)$，则元素 $a$ 是**正的**，记作 $a\ge0$。等价地（一条定理）对某个 $b\in\mathcal A$ 有 $a=b^*b$。

等价性"正 $\iff a=b^*b$"是代数的脊梁。一个方向：若 $a\ge0$，则由函数演算 $b=\sqrt a$（在 $\sigma(a)\subseteq[0,\infty)$ 上用 $f(z)=\sqrt z$）是自伴的，且 $b^*b=b^2=a$。反方向——对每个 $b$ 有 $b^*b\ge0$——是非平凡的那一半 *（不加证明地陈述——一个深刻的结果）*；它依赖于 C\*-恒等式，并保证正元素构成一个对加法封闭的锥。

> **定义 — 态。** 含单位 C\*-代数 $\mathcal A$ 上的一个**态**是一个线性泛函 $\omega:\mathcal A\to\mathbb C$，它
> - **正**：对所有 $a$ 有 $\omega(a^*a)\ge0$（任何"$|b|^2$"的期望都非负），且
> - **归一**：$\omega(1)=1$。

正泛函自动有界，且 $\|\omega\|=\omega(1)$，所以态有 $\|\omega\|=1$。我们把 $\omega(a)$ 读作可观测量 $a$ 在态 $\omega$ 中的期望值 $\langle a\rangle_\omega$。

> **引理 — GNS 半双线性形式与 Cauchy–Schwarz。** 对一个态 $\omega$，$\mathcal A$ 上的形式 $\langle a,b\rangle_\omega:=\omega(a^*b)$ 是半双线性的、半正定的，并满足 **Cauchy–Schwarz 不等式** $|\omega(a^*b)|^2\le\omega(a^*a)\,\omega(b^*b)$。

**证明。**
1. 半双线性性由 $\omega$ 的线性性与对合继承而来：$\langle a,b\rangle_\omega=\omega(a^*b)$ 对 $a$ 共轭线性、对 $b$ 线性。*（$\omega$ 的线性性；$(\lambda a)^*=\overline\lambda a^*$。）*
2. 正性：由态公理 $\langle a,a\rangle_\omega=\omega(a^*a)\ge0$。*（$\omega$ 的正性。）*
3. 任何半正定半双线性形式的 Cauchy–Schwarz 都源自对所有 $\lambda\in\mathbb C$ 的 $0\le\langle a+\lambda b,a+\lambda b\rangle_\omega$；取 $\lambda$ 使之极小化即得不等式，与内积情形完全一样。*（泛函分析指南中标准的正形式论证。）* $\blacksquare$

> **定义 — 表示。** C\*-代数 $\mathcal A$ 的一个**表示**是一对 $(\pi,\mathcal H)$，其中 $\mathcal H$ 是 Hilbert 空间，$\pi:\mathcal A\to B(\mathcal H)$ 是一个 \*-同态（线性、乘性、$\pi(a^*)=\pi(a)^*$、$\pi(1)=\mathrm{id}$）。若 $\{\pi(a)\Omega:a\in\mathcal A\}$ 在 $\mathcal H$ 中稠密，则向量 $\Omega\in\mathcal H$ 是**循环的**。

> **定理 — GNS 构造。** 设 $\omega$ 是含单位 C\*-代数 $\mathcal A$ 上的一个态。则存在一个 Hilbert 空间 $\mathcal H_\omega$、一个表示 $\pi_\omega:\mathcal A\to B(\mathcal H_\omega)$ 和一个单位循环向量 $\Omega_\omega\in\mathcal H_\omega$，使得
>
> $$
> \omega(a)=\langle\Omega_\omega,\ \pi_\omega(a)\,\Omega_\omega\rangle\qquad\text{for all }a\in\mathcal A.
> $$
>
> 该三元组在酉等价意义下唯一。

**证明（完整构造）。**
1. *预内积。* 在向量空间 $\mathcal A$ 上定义 $\langle a,b\rangle:=\omega(a^*b)$，由引理它半正定。它可能**退化**：某些非零的 $a$ 有 $\langle a,a\rangle=0$。*（GNS 形式。）*
2. *零空间是一个左理想。* 令 $N=\{a:\omega(a^*a)=0\}$。由 Cauchy–Schwarz，$a\in N$ 当且仅当对所有 $b$ 有 $\omega(b^*a)=0$；这使 $N$ 成为一个闭子空间。此外 $N$ 是一个**左理想**：若 $a\in N$ 且 $c\in\mathcal A$，则 $\omega((ca)^*(ca))=\omega(a^*c^*ca)\le\|c^*c\|\,\omega(a^*a)=0$（对 $x=c^*c\ge0$ 用 $\omega(a^*xa)\le\|x\|\,\omega(a^*a)$，因 $\|x\|1-x\ge0$）。所以 $ca\in N$。*（正性以及自伴 $x$ 的界 $x\le\|x\|1$。）*
3. *商与完备化。* 构造商向量空间 $\mathcal A/N$，用 $[a]$ 记 $a$ 的类。该形式下降为 $\mathcal A/N$ 上一个真正的内积：$\langle[a],[b]\rangle:=\omega(a^*b)$ 是良定义的（与代表元无关，因为 $N$ 恰是零方向），且现在是正*定*的。令 $\mathcal H_\omega$ 是 $\mathcal A/N$ 完备化所得的 Hilbert 空间。*（对半内积的零空间取商；内积空间的完备化，见泛函分析指南。）*
4. *表示。* 对 $c\in\mathcal A$ 定义 $\pi_\omega(c)[a]:=[ca]$。这是良定义的，因为 $N$ 是左理想（若 $a\in N$ 则 $ca\in N$，故该公式尊重类）。它有界：$\|\pi_\omega(c)[a]\|^2=\omega(a^*c^*ca)\le\|c\|^2\,\omega(a^*a)=\|c\|^2\|[a]\|^2$，因此 $\pi_\omega(c)$ 延拓为 $\mathcal H_\omega$ 上的有界算子，且 $\|\pi_\omega(c)\|\le\|c\|$。*（左理想性质；界 $c^*c\le\|c\|^2 1$。）*
5. *它是 \*-同态。* 线性性与 $\pi_\omega(cd)=\pi_\omega(c)\pi_\omega(d)$ 可从 $[cda]=c\cdot[da]$ 读出（结合性）。对于伴随，$\langle[a],\pi_\omega(c)[b]\rangle=\omega(a^*cb)=\omega((c^*a)^*b)=\langle\pi_\omega(c^*)[a],[b]\rangle$，所以 $\pi_\omega(c)^*=\pi_\omega(c^*)$。*（$\mathcal A$ 的结合性；内积的定义。）*
6. *循环向量。* 置 $\Omega_\omega:=[1]$。则 $\pi_\omega(a)\Omega_\omega=[a]$，所以轨道 $\{[a]:a\in\mathcal A\}=\mathcal A/N$ 按构造在 $\mathcal H_\omega$ 中稠密——$\Omega_\omega$ 是循环的。且 $\langle\Omega_\omega,\pi_\omega(a)\Omega_\omega\rangle=\langle[1],[a]\rangle=\omega(1^*a)=\omega(a)$；取 $a=1$，$\|\Omega_\omega\|^2=\omega(1)=1$。*（定义。）*
7. *唯一性。* 若 $(\pi',\mathcal H',\Omega')$ 是另一个这样的三元组，则映射 $\pi_\omega(a)\Omega_\omega\mapsto\pi'(a)\Omega'$ 在稠密循环轨道上良定义且等距（两个内积都等于 $\omega(a^*b)$），因而延拓为一个酉算子 $U$，它交缠两个表示并把 $\Omega_\omega$ 送到 $\Omega'$。$\blacksquare$

> **推论 — Gelfand–Naimark（一般情形）。** 每个 C\*-代数都等距 \*-同构于某个 Hilbert 空间 $\mathcal H$ 上 $B(\mathcal H)$ 的一个范数闭 \*-子代数。

**证明思路。** 取**普遍表示** $\pi=\bigoplus_\omega\pi_\omega$，即对所有态 $\omega$ 的所有 GNS 表示作直和。存在足够多的态（对每个自伴的 $a$ 都有一个态使 $|\omega(a)|=\|a\|$，由 $a$ 生成的交换子代数上一个特征标的 Hahn–Banach 延拓给出），使 $\pi$ 等距。所以 C\*-代数的抽象公理*恰好*刻画了有界算子的闭 \*-子代数——不多不少。

**例题。** 设 $\mathcal A=M_2(\mathbb C)$，$\omega(a)=\langle e_1,ae_1\rangle=a_{11}$（即 $(1,1)$ 元），这是"自旋向上"的向量态。它的零空间是 $N=\{a:\omega(a^*a)=0\}=\{a:a\text{ 的第 }1\text{ 列为 }0\}$，一个 $2$ 维左理想。则 $\mathcal A/N$ 是 $2$ 维的，由 $[E_{11}],[E_{21}]$（矩阵单位）张成，而 $\pi_\omega(a)$ 以左乘作用——在第一列上这就是 $a$ 作用于 $\mathbb C^2$。所以 GNS 重建出通常的 $\mathbb C^2$ 表示，$\Omega_\omega=e_1$，恰好从期望泛函恢复出教科书中的自旋-$\tfrac12$ Hilbert 空间。

**例题 — 混合态给出可约的 GNS 表示。** 在同一个 $\mathcal A=M_2(\mathbb C)$ 上取*迹*态 $\tau(a)=\tfrac12\mathrm{Tr}(a)=\tfrac12(a_{11}+a_{22})$。现在形式 $\langle a,b\rangle_\tau=\tfrac12\mathrm{Tr}(a^*b)$ 是*忠实的*：$\tau(a^*a)=\tfrac12\mathrm{Tr}(a^*a)=\tfrac12\sum_{ij}|a_{ij}|^2=0$ 迫使 $a=0$。所以零空间是 $N=\{0\}$，商就是整个 $M_2(\mathbb C)$，而 GNS Hilbert 空间是 $4$ 维的矩阵空间，配以内积 $\tfrac12\mathrm{Tr}(a^*b)$（归一化的 Hilbert–Schmidt 内积）。表示 $\pi_\tau(c)x=cx$ 是左乘，它分解为定义表示 $\mathbb C^2$ 的两份拷贝（每列一份），因而是**可约的**——这与 $\tau$ 是混合的、非纯的态这一事实（s5）相符。循环向量是 $\Omega_\tau=1$（单位矩阵），而且确实 $\langle 1,c\,1\rangle_\tau=\tfrac12\mathrm{Tr}(c)=\tau(c)$。把它与上面的纯态对比，后者的 GNS 空间只有 $2$ 维且不可约：*态越纯，它的 GNS 世界越小、越不可约。*

<a id="s5"></a>
### 表示、不可约性与纯态

**是什么以及为什么。** 不同的态给出不同的 GNS Hilbert 空间；其不可分解的构造单元对应于**纯态**与**不可约表示**。正是在这里，代数图景解释了*超选择*——当两个态无法相干叠加时，它们的表示就不等价。

> **定义 — 子表示、不可约。** 若对所有 $a$ 有 $\pi(a)\mathcal K\subseteq\mathcal K$，则闭子空间 $\mathcal K\subseteq\mathcal H$ 对表示 $\pi$ 是**不变的**。若唯一的不变闭子空间是 $\{0\}$ 与 $\mathcal H$，则表示是**不可约的**。

> **引理 — Schur 引理（C\*-版本）。** $\pi$ 不可约当且仅当与每个 $\pi(a)$ 交换的有界算子只有恒等的数乘，$\{\pi(\mathcal A)\}'=\mathbb C\,\mathrm{id}$。（这里 $S'=\{T\in B(\mathcal H):TS=ST\ \forall S\in\mathcal S\}$ 是**交换子**。）

**证明。**
1. （$\Leftarrow$）设交换子是 $\mathbb C\,\mathrm{id}$，令 $\mathcal K$ 不变。由于 $\pi$ 是 \*-表示，到 $\mathcal K$ 上的正交投影 $P$ 与所有 $\pi(a)$ 交换：$\mathcal K$ 的不变性以及（取伴随、用 $\pi(a^*)=\pi(a)^*$）$\mathcal K^\perp$ 的不变性给出 $P\pi(a)=\pi(a)P$。所以 $P\in\{\pi(\mathcal A)\}'=\mathbb C\,\mathrm{id}$，迫使 $P=0$ 或 $P=\mathrm{id}$，即 $\mathcal K=\{0\}$ 或 $\mathcal H$。*（对一个 \*-闭集，投影在交换子中当且仅当其值域不变。）*
2. （$\Rightarrow$）反之，若交换子中有某个非标量的自伴 $T$，则它的谱投影（函数演算）是非平凡的交换子投影，给出一个真不变子空间。一般的交换子元素可分解为自伴部分，二者都在交换子中。$\blacksquare$

> **定义 — 纯态。** 若一个态 $\omega$ 是所有态构成的凸集的极点，则它是**纯的**：只要 $\omega=t\,\omega_1+(1-t)\omega_2$，其中 $0<t<1$ 且 $\omega_i$ 是态，就有 $\omega_1=\omega_2=\omega$。非纯的态是**混合的**。

> **定理 — 纯性 $\iff$ 不可约性。** 一个态 $\omega$ 是纯的当且仅当它的 GNS 表示 $\pi_\omega$ 不可约。

**证明（关键步骤）。**
1. 在 (i) 满足 $\le\omega$ 的正泛函与 (ii) 交换子 $\{\pi_\omega(\mathcal A)\}'$ 中由 $\mathrm{id}$ 界定的正算子之间存在双射：泛函 $\omega'\le\omega$ 对应于 $\omega'(a)=\langle\Omega_\omega,\pi_\omega(a)T\Omega_\omega\rangle$，其中 $0\le T\le\mathrm{id}$ 是交换子中唯一的。*（关于态的 Radon–Nikodym 型引理，用到 $\Omega_\omega$ 的循环性。）*
2. $\omega$ 纯当且仅当唯一这样的 $T$ 是 $0$ 与 $\mathrm{id}$（无非平凡分裂），当且仅当交换子不含非平凡正压缩，当且仅当 $\{\pi_\omega(\mathcal A)\}'=\mathbb C\,\mathrm{id}$，当且仅当（Schur）$\pi_\omega$ 不可约。$\blacksquare$

**例题。** 在 $M_2(\mathbb C)$ 上，单位向量 $\psi$ 的向量态 $\omega(a)=\langle\psi,a\psi\rangle$ 是纯的（其 GNS 表示是不可约的 $\mathbb C^2$）。"最大混合"态 $\tau(a)=\tfrac12\mathrm{Tr}(a)=\tfrac12(a_{11}+a_{22})$ *不*纯：$\tau=\tfrac12\omega_{e_1}+\tfrac12\omega_{e_2}$，一个真凸组合。它的 GNS 表示是 $4$ 维的左正则表示 $M_2(\mathbb C)$ 作用于自身，它是可约的（是 $\mathbb C^2$ 的 $2$ 份拷贝）。

## C 部分 — Von Neumann 代数

<a id="s6"></a>
### Von Neumann 代数与双交换子定理

**是什么以及为什么。** C\*-代数在范数拓扑下闭。如果我们改在一个*更弱*的拓扑下取闭包——即算子的极限逐个矩阵元地取——我们得到 **von Neumann 代数**，它携带远为丰富的结构（大量投影、丰富的类型理论）。令人惊叹的**双交换子定理**说，这一分析意义下的闭包恰好与纯代数条件 $\mathcal M=\mathcal M''$ 一致。

> **定义 — 弱算子拓扑与强算子拓扑。** 在 $B(\mathcal H)$ 上：
> - $T_n\to T$ **强地**（SOT），若对每个 $\xi\in\mathcal H$ 有 $T_n\xi\to T\xi$（按范数）；
> - $T_n\to T$ **弱地**（WOT），若对所有 $\xi,\eta\in\mathcal H$ 有 $\langle\eta,T_n\xi\rangle\to\langle\eta,T\xi\rangle$。
> 两者都弱于范数收敛 $\|T_n-T\|\to0$。

> **定义 — von Neumann 代数。** 一个 **von Neumann 代数** $\mathcal M\subseteq B(\mathcal H)$ 是一个含单位的 \*-子代数，它在弱算子拓扑下闭。（等价地，在强算子拓扑下闭——两者给出相同的闭 \*-代数。）

> **定义 — 交换子。** 对 $\mathcal S\subseteq B(\mathcal H)$，**交换子**是 $\mathcal S'=\{T\in B(\mathcal H):TS=ST\ \forall S\in\mathcal S\}$。**双交换子**是 $\mathcal S''=(\mathcal S')'$。

任何集合的交换子总是一个 von Neumann 代数：它是 \*-代数（若 $\mathcal S$ 是 \*-闭的）且 WOT-闭（交换是一个闭条件）。

> **定理 — von Neumann 双交换子定理。** 设 $\mathcal M\subseteq B(\mathcal H)$ 是含单位的 \*-子代数。下列条件等价：
> 1. $\mathcal M$ 在弱算子拓扑下闭（它是一个 von Neumann 代数）；
> 2. $\mathcal M$ 在强算子拓扑下闭；
> 3. $\mathcal M=\mathcal M''$。

**证明（实质性的蕴含 $\mathcal M''\subseteq\overline{\mathcal M}^{\,SOT}$）。**
1. 设 $T\in\mathcal M''$，固定 $\xi_1,\dots,\xi_n\in\mathcal H$ 与 $\varepsilon>0$；我们要找 $A\in\mathcal M$ 使对所有 $i$ 有 $\|(T-A)\xi_i\|<\varepsilon$（这是一个基本的 SOT-邻域）。*（SOT 闭包的定义。）*
2. *单个向量（$n=1$）。* 令 $\mathcal K=\overline{\mathcal M\xi}$（轨道的闭包），$P$ 是到 $\mathcal K$ 上的投影。由于 $\mathcal M\mathcal K\subseteq\mathcal K$ 且 $\mathcal M$ 是 \*-闭的，$P\in\mathcal M'$。因 $T\in\mathcal M''$，$T$ 与 $P$ 交换，故 $T\mathcal K\subseteq\mathcal K$。现在 $\xi=1\cdot\xi\in\mathcal K$（用 $1\in\mathcal M$），因此 $T\xi\in\mathcal K=\overline{\mathcal M\xi}$，所以某个 $A\in\mathcal M$ 有 $\|T\xi-A\xi\|<\varepsilon$。*（不变子空间给出交换子投影；双交换子中的 $T$ 与它交换。）*
3. *多个向量。* 把 $n=1$ 的论证用于**放大（amplification）**：$\mathcal H^{(n)}=\mathcal H\oplus\cdots\oplus\mathcal H$，其中 $\mathcal M$ 对角地作用为 $A^{(n)}=A\oplus\cdots\oplus A$。可验证 $(\mathcal M^{(n)})''=(\mathcal M'')^{(n)}$，所以 $T^{(n)}\in(\mathcal M^{(n)})''$，把单向量结果用于 $\xi=(\xi_1,\dots,\xi_n)\in\mathcal H^{(n)}$ 得到 $A$ 使 $\sum_i\|(T-A)\xi_i\|^2<\varepsilon^2$。*（放大技巧把一般情形归约为 $n=1$。）*
4. 故 $T\in\overline{\mathcal M}^{\,SOT}$。结合平凡的包含 $\mathcal M\subseteq\mathcal M''$ 以及（闭包事实）由于 $\mathcal M''$ 是 WOT-闭的而有 $\overline{\mathcal M}^{\,WOT}\subseteq\mathcal M''$，三个条件全部一致。$\blacksquare$

**含义。** 这条定理是分析（在某拓扑下的闭包）与代数（交换关系）之间的桥梁。它说：你能用 $\mathcal M$ *逼近*的算子，正是那些被 $\mathcal M$ 所尊重的每一个对称性*强制*落在 $\mathcal M$ 中的算子。在物理上，$\mathcal M'$ 是与 $\mathcal M$ 中所有可观测量交换的算子代数——即"对称性"——而 $\mathcal M=\mathcal M''$ 说可观测量恰好就是与对称性交换的那些。

> **定义 — 中心。** von Neumann 代数 $\mathcal M$ 的**中心**是 $Z(\mathcal M)=\mathcal M\cap\mathcal M'$，即与 $\mathcal M$ 中一切交换的元素。它总含 $\mathbb C\,\mathrm{id}$。

**例题。** 设 $\mathcal M\subseteq B(\mathbb C^2)$ 是对角矩阵 $\{\mathrm{diag}(\alpha,\beta)\}$。它的交换子 $\mathcal M'$ 也是对角矩阵（与 $\mathrm{diag}(1,2)$ 交换的矩阵必为对角）。则 $\mathcal M''=(\mathcal M')'=$ 再次是对角的 $=\mathcal M$——确认 $\mathcal M=\mathcal M''$。这里 $\mathcal M$ 交换，$\mathcal M=\mathcal M'$，中心就是整个 $\mathcal M$。

**例题 — 通过放大得到一个因子及其交换子。** 设 $\mathcal M=M_2(\mathbb C)\otimes 1_3$ 作用于 $\mathcal H=\mathbb C^2\otimes\mathbb C^3=\mathbb C^6$，即分块标量算子 $a\otimes 1$，它对第一个因子施加一个固定的 $2\times2$ 矩阵，对第二个因子什么也不做。直接计算（或张量积的**交换定理**）给出 $\mathcal M'=1_2\otimes M_3(\mathbb C)$，即只作用于第二个因子的算子。则 $\mathcal M''=(1_2\otimes M_3)'=M_2(\mathbb C)\otimes1_3=\mathcal M$，再次验证双交换子定理。中心是 $Z(\mathcal M)=\mathcal M\cap\mathcal M'=(M_2\otimes1)\cap(1\otimes M_3)=\mathbb C\,1_6$——平凡——所以 $\mathcal M$ 是一个**因子**（类型 I$_2$，为 s7 作铺垫）。这是最简单的例证，说明张量积 Hilbert 空间上的一个因子"占有"一个张量因子并把另一个交给它的交换子——这就是二体量子系统、观察者对环境的代数骨架。

**易错点 — 范数闭还不够。** 一个 C\*-代数（范数闭）未必是 von Neumann 代数（WOT-闭）。例：无穷维 $\mathcal H$ 上的紧算子 $K(\mathcal H)$ 构成一个 C\*-代数，但*不*是 WOT-闭的——到越来越大子空间上的有限秩投影强收敛到 $1$，而 $1$ 不紧。它的 WOT 闭包（等价地它的双交换子）是整个 $B(\mathcal H)$。所以 $K(\mathcal H)''=B(\mathcal H)\ne K(\mathcal H)$，双交换子定理正确地报告了 $K(\mathcal H)$ 不是 von Neumann 代数。

<a id="s7"></a>
### 因子与 Murray–von Neumann 分类

**是什么以及为什么。** 一个 von Neumann 代数，若其中心尽可能小——仅有标量——就不能被分裂成独立的几块；它是一个**因子**，即不可约的构造单元。Murray 与 von Neumann 发现了一个令人震惊的事实：因子分为不同的**类型**，按其投影能"多大"来区分，由一个无需取整数值乃至离散值的维数函数度量。

> **定义 — 因子。** 一个 von Neumann 代数 $\mathcal M$ 是一个**因子**，如果它的中心平凡：$Z(\mathcal M)=\mathcal M\cap\mathcal M'=\mathbb C\,\mathrm{id}$。（每个 von Neumann 代数都是因子的"直积分"，所以因子是原子。）

> **定义 — 投影与等价。** **投影**是满足 $p=p^*=p^2$ 的 $p\in\mathcal M$。两个投影 $p,q$ **（Murray–von Neumann）等价**，$p\sim q$，如果存在一个**部分等距** $v\in\mathcal M$，使 $v^*v=p$ 且 $vv^*=q$（即 $v$ 把 $p$ 的值域等距地映到 $q$ 的值域）。若对某个子投影 $q'$ 有 $p\sim q'\le q$，则记 $p\preceq q$。

这个 $\preceq$ 把因子的投影全序化（一条定理），其行为如同一种"大小"。若投影 $p$ 不等价于它自身的某个真子投影（$p\sim q\le p\Rightarrow q=p$），则它是**有限的**；否则是**无限的**。这是 Dedekind 关于有限集与无限集之区分（一个集合是无限的当且仅当它与某真子集一一对应）的算子代数版本。

> **定理 — Murray–von Neumann 分类。** 每个因子都恰好落入下列类型之一，由其投影上一个归一化**维数函数** $d(p)$ 的值域刻画：
> - **类型 I$_n$**（$n\in\{1,2,\dots\}$）：$d$ 取值于 $\{0,1,2,\dots,n\}$；该因子 $\cong B(\mathbb C^n)=M_n(\mathbb C)$。**类型 I$_\infty$**：取值 $\{0,1,2,\dots,\infty\}$；对可分无穷维 $\mathcal H$，该因子 $\cong B(\mathcal H)$。
> - **类型 II$_1$**：$d$ 取连续统 $[0,1]$ 中*所有*的值，且单位有限。存在连续统多个不等价的投影大小，但没有极小（原子）投影。
> - **类型 II$_\infty$**：取值 $[0,\infty]$；单位无限，但该因子有一个有限子投影。
> - **类型 III**：唯一的取值是 $\{0,\infty\}$——每个非零投影都无限且等价于单位；根本*没有*迹。

**证明结构（分类所依赖的内容）。**
1. *比较定理。* 在一个因子中，对任意两个投影 $p,q$，要么 $p\preceq q$，要么 $q\preceq p$。*（用到中心的平凡性：会阻碍比较的那个中心投影是 $0$ 或 $1$。）*
2. *维数函数。* 在投影的等价类上，$\preceq$ 是全序，且存在一个本质唯一的可加函数 $d$（在正交投影上可加，当 $pq=0$ 时 $d(p)+d(q)=d(p+q)$），在有限情形由 $d(1)=1$ 归一化。*（可加性来自部分等距；至多差一个尺度而唯一。）*
3. *值域二分* *（不加证明地陈述——一个深刻的结果）*。$d$ 可能的值域恰是所列的五个集合；出现哪一个就是类型。深刻之处在于*连续*值域 $[0,1]$（类型 II$_1$）与*退化*值域 $\{0,\infty\}$（类型 III）确实会出现——von Neumann 用群-测度空间构造与无穷张量积构造造出了类型 II$_1$。$\blacksquare$

**含义与物理。** 类型 I 是通常的量子力学——固定 Hilbert 空间上的可观测量，带有极小投影（秩一，"纯态作为向量存在"）。类型 II 和 III *没有极小投影*：你可以永远把一个投影对半分下去。类型 III 因子是**量子场论**中的一般情形——时空中任何有界区域的局部可观测量代数都是一个类型 III$_1$ 因子（Buchholz–Fredenhagen 等人的定理）。这就是为什么场论没有可归一化的"局域在一个区域内的最小激发"，以及为什么局部态高度纠缠。

**例题（超有限 II$_1$ 因子）。** 取 $2\times2$ 矩阵代数的无穷张量积配以迹态，$\mathcal R=\overline{\bigotimes_{k=1}^\infty M_2(\mathbb C)}$（在乘积迹 $\tau=\bigotimes\frac12\mathrm{Tr}$ 的 GNS 表示中取弱闭包）。对每个 $k$ 都存在一个"迹 $1/2^k$"的投影，把它们组合起来便实现了每个二进有理数，再由闭包实现 $[0,1]$ 中每个实值——所以 $d$ 有连续值域，$\mathcal R$ 是一个没有极小投影的 II$_1$ 因子。

**例题 — 有限性即 Dedekind 有限性，具体地说。** 在 $\mathcal M=B(\mathcal H)$，$\mathcal H=\ell^2(\mathbb N)$（类型 I$_\infty$）中，单位 $1$ 是一个*无限*投影：单边移位 $v(e_n)=e_{n+1}$ 是一个部分等距，$v^*v=1$ 但 $vv^*=1-p_0$，即抹去第一个基向量的投影。所以 $1\sim 1-p_0\lneq1$——单位等价于它自身的一个真子投影，恰是 Dedekind 的"无限集与某真子集一一对应"。在 II$_1$ 因子中这不可能：迹会给出 $\tau(1)=\tau(1-p_0)=\tau(1)-\tau(p_0)$，迫使 $\tau(p_0)=0$ 从而 $p_0=0$（忠实性）。*忠实有限迹的存在*恰是使单位有限的东西，把类型 II$_1$ 与无限类型区分开。类型 III 是相反的极端：$1$ 无限，而*每个*非零投影都等价于 $1$，所以唯一可设想的迹值是 $0$ 与 $\infty$——根本不可能存在有限迹。

**直觉 — 为什么物理遇上类型 III。** QFT 中的局部代数，对嵌套于其中的每个区域，都含有局域化任意精细的可观测量，而真空把所有尺度纠缠在一起。没有"最小不可分激发"可称为极小投影，且纠缠如此之强，以致任何局部投影都能被代数旋转到任何其它投影——这是类型 III$_1$ 的标志。迹的缺失是这一物理事实的数学面貌：*一个区域内的能量与纠缠熵不可归一化*；这就是为什么朴素的"盒中态数"计数发散，必须加以正规化。

<a id="s8"></a>
### 迹，以及对 Tomita–Takesaki 模理论的初探

**是什么以及为什么。** **迹**是一个对乘法顺序不敏感的态，$\tau(ab)=\tau(ba)$——即矩阵迹的抽象版本，也恰是类型 II$_1$ 因子所拥有而类型 III 因子所缺的东西。当不存在迹时，态仍携带动力学信息：**Tomita–Takesaki 理论**表明，von Neumann 代数上*每个*忠实态都生成一个典范的单参数自同构群，即**模流**——一个仅由代数与态构造出来的内蕴时间概念。

> **定义 — 迹。** von Neumann 代数 $\mathcal M$ 上的一个**迹态**是一个态 $\tau$，对所有 $a,b\in\mathcal M$ 具有**迹性质** $\tau(ab)=\tau(ba)$。若 $\tau(a^*a)=0\Rightarrow a=0$，则它是**忠实的**。

> **命题 — II$_1$ 因子有唯一的忠实迹态。** 维数函数 $d$ 延拓为唯一的迹：在投影上 $\tau(p)=d(p)$，再由线性与连续性延拓。

**证明梗概。**
1. *存在性。* 对投影定义 $\tau(p)=d(p)$；经谱分解（函数演算把 $a=\int\lambda\,dp_\lambda$）延拓到自伴元，再由线性延拓到整个 $\mathcal M$。迹性质 $\tau(ab)=\tau(ba)$ 先对部分等距成立（因为 $v^*v\sim vv^*$ 有相等的 $d$），再由线性/稠密性延拓。*（维数函数的可加性以及 $v^*v,vv^*$ 的等价。）*
2. *唯一性。* 任何两个迹在投影上一致，因为 $d$ 是因子中投影类上唯一的归一化可加函数（s7），故由稠密性处处一致。$\blacksquare$

> **定理 — Tomita–Takesaki（陈述）。** 设 $\mathcal M\subseteq B(\mathcal H)$ 是带有一个**循环且分离**向量 $\Omega$ 的 von Neumann 代数（循环：$\mathcal M\Omega$ 稠密；分离：$a\Omega=0\Rightarrow a=0$）。由
>
> $$
> S\,a\Omega=a^*\Omega\qquad(a\in\mathcal M),
> $$
>
> 定义反线性算子 $S$，并令 $S=J\Delta^{1/2}$ 是它的**极分解**，其中 $J$ 反酉（**模共轭**），$\Delta=S^*S>0$（**模算子**）。则：
> 1. $J\mathcal M J=\mathcal M'$——用 $J$ 共轭把代数与它的交换子互换；
> 2. 对所有 $t\in\mathbb R$ 有 $\Delta^{it}\mathcal M\Delta^{-it}=\mathcal M$——**模自同构群** $\sigma_t(a)=\Delta^{it}a\Delta^{-it}$ 保持 $\mathcal M$。

**解释。**
1. 向量态 $\omega(a)=\langle\Omega,a\Omega\rangle$ 仅通过 $\Delta$ 就在代数上定义了一个典范动力学 $\sigma_t$。没有任何手工选定的时钟：*态本身*告诉可观测量如何演化。这就是著名的口号"态包含时间"（Connes–Rovelli **热时间假说**）。
2. 当 $\tau$ 是迹时，$S$ 本质上仅为 $J$，而 $\Delta=1$，所以模流平凡（$\sigma_t=\mathrm{id}$）。非平凡的模流恰是*非迹*态的症状——这是类型 III 中、因而场论中的一般情形。
3. 关系 $\sigma_t(a)=\Delta^{it}a\Delta^{-it}$ 连同 KMS 条件（s11）把 $\omega$ 标定为动力学 $\sigma_t$ 在逆温度 $\beta=-1$ 处的热平衡态。平衡与模流是同一现象。

**例题。** 设 $\mathcal M=M_n(\mathbb C)$ 通过左乘作用于 $\mathcal H=M_n(\mathbb C)$（Hilbert–Schmidt 内积 $\langle x,y\rangle=\mathrm{Tr}(x^*y)$），循环-分离向量 $\Omega=\rho^{1/2}$，其中 $\rho>0$ 是密度矩阵（$\rho>0$，$\mathrm{Tr}\,\rho=1$），给出态 $\omega(a)=\mathrm{Tr}(\rho a)$。则 $S(a\rho^{1/2})=a^*\rho^{1/2}$ 解开为 $\Delta(x)=\rho x\rho^{-1}$，而模流是 $\sigma_t(a)=\rho^{it}a\rho^{-it}$——恰是由"Hamilton 量" $-\log\rho$ 生成的 Heisenberg 演化。所以 $\omega$ 是 $\beta=1$ 处的 **Gibbs 态** $\rho=e^{-H}/\mathrm{Tr}\,e^{-H}$，而模流就是热时间。当 $\rho=\frac1n 1$（迹）时，$\Delta=1$ 且流平凡——与第 (2) 点相符。

## D 部分 — 代数量子场论

<a id="s9"></a>
### 正则（反）对易关系：Weyl、CCR、CAR

**是什么以及为什么。** 量子化一个场意味着把经典 Poisson 括号变成对易子：$[\,\widehat q,\widehat p\,]=i\hbar$。但无界算子难以放进 C\*-代数（它们没有范数）。补救办法是指数化为有界酉算子——即 **Weyl 算子**——其对易关系成为一个代数恒等式。对费米子则用*反对易子*，直接给出有界的 **CAR 代数**。

> **定义 — Heisenberg CCR（无界形式）。** 单自由度的**正则对易关系**是在合适定义域上的关系，
>
> $$
> [\,\widehat q,\widehat p\,]=\widehat q\widehat p-\widehat p\widehat q=i\hbar\,1.
> $$
>
> 没有有界算子能满足它：如果有，对两边取迹（在有限维中）给出 $0=i\hbar n$，不可能；在无穷维中 $\|\,[\widehat q,\widehat p]\,\|$ 将不得不界住 $|\hbar|$ 乘以无界的幂（Wintner 定理）。故 $\widehat q,\widehat p$ 必然无界。

> **定义 — Weyl 算子与 CCR 代数。** 引入有界酉算子 $W(s,t)=e^{i(s\widehat q+t\widehat p)}$，$(s,t)\in\mathbb R^2$。Baker–Campbell–Hausdorff 公式把 CCR 变成 **Weyl 关系**：
>
> $$
> W(s_1,t_1)\,W(s_2,t_2)=e^{-\tfrac{i\hbar}{2}(s_1 t_2-s_2 t_1)}\,W(s_1+s_2,\ t_1+t_2).
> $$
>
> 由符号 $W(f)$ 生成的 C\*-代数，其中 $f$ 取自一个辛空间 $(V,\sigma)$，满足 $W(f)W(g)=e^{-\frac i2\sigma(f,g)}W(f+g)$ 与 $W(f)^*=W(-f)$，称为 **Weyl（CCR）代数** $\mathrm{CCR}(V,\sigma)$。

> **定理 — Stone–von Neumann。** 对有限多个自由度，Weyl 关系的每个由强连续酉算子给出的不可约表示都酉等价于 $L^2(\mathbb R^n)$ 上的标准 Schrödinger 表示。

这是有限维量子化的*唯一性*——而它在**无穷维中的失效**（无穷多自由度，即场）正是 QFT 拥有不等价表示的原因，也是 Haag 定理（s11）的技术根源。

> **定义 — CAR 代数。** 对费米子，给定一个 Hilbert 空间 $\mathfrak h$（"单粒子空间"），对**产生/湮灭算子** $a(f),a^*(f)$（$f\in\mathfrak h$）而言，**正则反对易关系**为
>
> $$
> \{a(f),a^*(g)\}=a(f)a^*(g)+a^*(g)a(f)=\langle f,g\rangle\,1,\qquad \{a(f),a(g)\}=0.
> $$
>
> 由于 $\|a(f)\|=\|f\|$（把 C\*-恒等式用于这些关系的一个推论——下面证明），它们*确实*有界，所以 **CAR 代数** $\mathrm{CAR}(\mathfrak h)$ 是一个真正的 C\*-代数，无需指数化。

**$\|a(f)\|=\|f\|$ 的证明。**
1. 由 CAR，$a(f)^*a(f)+a(f)a(f)^*=\langle f,f\rangle1=\|f\|^2 1$，且 $a(f)^2=0$（在第二个关系中令 $g=f$）。*（CAR 关系。）*
2. 令 $x=a(f)^*a(f)\ge0$。则 $x^2=a(f)^*a(f)a(f)^*a(f)=a(f)^*(\|f\|^21-a(f)^*a(f))a(f)=\|f\|^2 x-a(f)^*a(f)^{*}a(f)a(f)$，而最后一项消失，因为 $a(f)^2=0$ 给出 $a(f)a(f)=0$。所以 $x^2=\|f\|^2x$。*（代入反对易子；用 $a(f)^2=0$。）*
3. 于是 $\sigma(x)\subseteq\{0,\|f\|^2\}$，所以 $\|x\|=\|f\|^2$（对 $f\ne0$ 它非零）。由 C\*-恒等式 $\|a(f)\|^2=\|a(f)^*a(f)\|=\|x\|=\|f\|^2$，故 $\|a(f)\|=\|f\|$。*（由 $x^2=\|f\|^2x$ 得谱；C\*-恒等式。）* $\blacksquare$

**例题（单个费米模）。** 取 $\dim\mathfrak h=1$，对单位 $f$ 写 $a=a(f)$。则 $\{a,a^*\}=1$，$a^2=0$。在 $\mathbb C^2$ 上用 $a=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}$ 表示：确实 $a^2=0$，$a^*a=\begin{psmallmatrix}0&0\\0&1\end{psmallmatrix}$，$aa^*=\begin{psmallmatrix}1&0\\0&0\end{psmallmatrix}$，且 $a^*a+aa^*=1$。数算子 $a^*a$ 有本征值 $0$（空）与 $1$（占据）——Pauli 不相容原理（$a^2=0$ 意味着"同一模中不能有两个费米子"）直接从代数中冒出来。而且 $\|a\|=1=\|f\|$，与定理相符。

<a id="s10"></a>
### 代数量子场论：Haag–Kastler 公理

**是什么以及为什么。** 代数量子场论（AQFT）把"可观测量先于态"的口号变成相对论量子场论的基础。首要对象不是某点处的场算子（一个奇异对象），而是给时空每个区域指派该区域内*可测量*的可观测量 C\*-代数。一个 QFT *就是*这样一种指派——一个**局部代数网**——满足编码局域性与相对论协变性的公理。

> **定义 — 局部可观测量网。** 设 $\mathcal O\mapsto\mathfrak A(\mathcal O)$ 给 Minkowski 时空 $\mathbb R^{1,3}$ 中每个有界开区域 $\mathcal O$ 指派一个 C\*-代数 $\mathfrak A(\mathcal O)\subseteq\mathfrak A$，即局域于 $\mathcal O$ 的可观测量，全都位于一个整体 C\*-代数 $\mathfrak A=\overline{\bigcup_{\mathcal O}\mathfrak A(\mathcal O)}$ 之内。这种指派是一个**网**。

> **定义 — Haag–Kastler 公理。** 一个网 $\mathcal O\mapsto\mathfrak A(\mathcal O)$ 是一个（Haag–Kastler）**QFT**，如果：
> 1. **等调性（单调性）**：$\mathcal O_1\subseteq\mathcal O_2\Rightarrow\mathfrak A(\mathcal O_1)\subseteq\mathfrak A(\mathcal O_2)$。更大的区域中能做更多测量。
> 2. **微观因果性 / 局域性**：若 $\mathcal O_1$ 与 $\mathcal O_2$ **类空分离**（没有速度 $\le c$ 的信号连接它们），则它们的代数逐元交换：$[\mathfrak A(\mathcal O_1),\mathfrak A(\mathcal O_2)]=\{0\}$。类空分离的测量互不干扰——这是 Einstein 因果性的代数形式。
> 3. **Poincaré 协变性**：Poincaré 群（Lorentz 变换与时空平移）通过自同构 $\alpha_g:\mathfrak A\to\mathfrak A$ 作用，满足 $\alpha_g(\mathfrak A(\mathcal O))=\mathfrak A(g\mathcal O)$。物理是相对论不变的。
> 4. **谱条件（能量正性）**：在真空表示中，时间平移的生成元（Hamilton 量）有非负谱，且能量-动量落在前向光锥内。
> 5. **真空**：存在一个 Poincaré 不变态 $\omega_0$（**真空**），其 GNS 表示含有唯一一个不变向量 $\Omega_0$。

**为什么这是正确的打包方式。**
1. 这些公理只涉及代数与区域，从不涉及某个特定的 Hilbert 空间或场。两个有相同网的理论物理上等同；网是那个不变量。*（s0 的可观测量优先原则。）*
2. 微观因果性是时空因果结构进入的*唯一*之处——"相对论"的全部内容就是"类空代数交换"。这使因果性明显成为一个代数性质。
3. **Haag 对偶性**（常作为附加要求）陈述 $\mathfrak A(\mathcal O)'=\mathfrak A(\mathcal O')$，其中 $\mathcal O'$ 是类空补：一个局部代数的交换子是因果上不相连区域的代数。这是双交换子定理（s6）在 AQFT 中的化身，并直接联系到 Tomita–Takesaki：真空在楔形区域上的模流是 Lorentz 推动（**Bisognano–Wichmann 定理**），相应的 KMS 温度是加速观察者感受到的 **Unruh 温度**。

> **定理（Reeh–Schlieder，陈述）。** 在带谱条件的 Haag–Kastler 网中，对任何因果补非空的区域，真空 $\Omega_0$ 对其每个局部代数 $\mathfrak A(\mathcal O)$ 都是**循环且分离**的。

**含义。** 从单个有界区域出发，通过用局部可观测量作用于真空，可以逼近整体理论的*任何*态——甚至描述宇宙遥远另一端粒子的态。这是真空纠缠的一个尖锐陈述，而且（经由 s8）它正是驱动模理论的那个循环-分离假设：每个局部代数 $\mathfrak A(\mathcal O)$ 都携带一个由真空构造的典范模流。

**例题（自由标量场，示意性地）。** 对自由 Klein–Gordon 场，人们把 $\mathfrak A(\mathcal O)$ 构造为支撑于 $\mathcal O$ 内的实试验函数空间上的 Weyl（CCR）代数，辛形式由对易子分布 $\sigma(f,g)=\int(f\,\partial_0 g-g\,\partial_0 f)$ 给出。等调性成立，因为更大的支撑集包含更小的；微观因果性成立，因为对类空分离的支撑，对易子分布消失（场的因果传播子支撑于光锥内）；Poincaré 协变性继承自对试验函数的作用。事实表明局部代数是类型 III$_1$ 因子（s7）——这是 AQFT 的一般情形。

<a id="s11"></a>
### KMS 条件、热态与 Haag 定理

**是什么以及为什么。** 在没有迹的情况下（类型 III 中不可能有）如何说"热平衡"？答案是 **KMS 条件**——一个解析性条件，把 $\omega(a\,\sigma_t(b))$ 与 $\omega(\sigma_t(b)\,a)$ 跨复时间平面上的一条带状区域联系起来。它在有限系统中刻画 Gibbs 态，并把它*推广*到 $e^{-\beta H}/\mathrm{Tr}\,e^{-\beta H}$ 毫无意义的系统。它还直接回连到模理论，以及 Haag 为相互作用场所指出的障碍。

> **定义 — C\*-代数上的动力学。** 一个 **(C\*-)动力学系统**是一个 C\*-代数 $\mathfrak A$ 连同一个强连续的单参数自同构群 $t\mapsto\sigma_t$（时间演化），满足 $\sigma_{s+t}=\sigma_s\sigma_t$、$\sigma_t(a^*)=\sigma_t(a)^*$。

> **定义 — KMS 条件。** $(\mathfrak A,\sigma)$ 上的一个态 $\omega$ 满足**逆温度 $\beta>0$ 处的 KMS 条件**（Kubo–Martin–Schwinger），如果对某个稠密集中的所有 $a,b$，存在一个函数 $F_{a,b}$，它在带状区域 $\{z:0\le\mathrm{Im}\,z\le\beta\}$ 上有界且连续、在其内部解析，且边界值为
>
> $$
> F_{a,b}(t)=\omega\!\big(a\,\sigma_t(b)\big),\qquad F_{a,b}(t+i\beta)=\omega\!\big(\sigma_t(b)\,a\big).
> $$

> **命题 — 有限系统：KMS $\iff$ Gibbs。** 对 $\mathfrak A=M_n(\mathbb C)$、$\sigma_t(a)=e^{itH}ae^{-itH}$，唯一的 $\beta$-KMS 态是 **Gibbs 态** $\omega_\beta(a)=\dfrac{\mathrm{Tr}(e^{-\beta H}a)}{\mathrm{Tr}(e^{-\beta H})}$。

**证明。**
1. 取如上定义的 $\omega_\beta$，并置 $F_{a,b}(z)=\dfrac{1}{\mathrm{Tr}(e^{-\beta H})}\mathrm{Tr}\big(e^{-\beta H}a\,e^{izH}be^{-izH}\big)$。这个整函数对 $z$ 解析（矩阵指数是整的），在带状区域上有界（有限维）。*（有限维解析性。）*
2. 在 $z=t$（实）处，由定义 $F_{a,b}(t)=\omega_\beta(a\sigma_t(b))$。*（$\sigma_t$ 的定义。）*
3. 在 $z=t+i\beta$ 处：把共轭的解析延拓显式写出，$\sigma_{t+i\beta}(b)=e^{i(t+i\beta)H}\,b\,e^{-i(t+i\beta)H}$，并用 $e^{i(t+i\beta)H}=e^{itH}e^{-\beta H}$，所以 $F_{a,b}(t+i\beta)=\frac{1}{Z}\mathrm{Tr}(e^{-\beta H}a\,e^{itH}e^{-\beta H}be^{\beta H}e^{-itH})$；用迹的循环性把 $e^{-\beta H}$ 移动并用 $\sigma_t(b)=e^{itH}be^{-itH}$，这等于 $\omega_\beta(\sigma_t(b)\,a)$。*（矩阵迹的循环性；$Z=\mathrm{Tr}\,e^{-\beta H}$。）*
4. 所以 $\omega_\beta$ 是 KMS 的。唯一性：KMS 边界条件迫使两点函数与 Gibbs 态的相匹配，而这些函数确定了态。$\blacksquare$

> **定理 — KMS $\iff$ 模（通往 s8 的桥梁）。** 一个忠实态 $\omega$ 对动力学 $\sigma_t$ 是 $\beta$-KMS 的，当且仅当（在重标时间之后）$\sigma_t$ 是 $\omega$ 的**模自同构群**，即来自 Tomita–Takesaki 的 $\sigma_{-t/\beta}=\sigma_t^\omega=\Delta^{it}\cdot\Delta^{-it}$。

这是统一整本指南的点睛之笔：平衡（KMS）、内蕴时间（模流）与类型 III 代数的结构*是同一套数学*。热态存在并由 KMS 刻画，即使在没有密度矩阵、没有迹的地方亦然——这恰是量子场论以及热力学极限下量子统计力学的领域。

> **定理 — Haag 定理（陈述）。** 在满足 Wightman/Haag–Kastler 公理的相对论 QFT 中，如果某固定时刻的相互作用场酉等价于该时刻的自由场（如教科书微扰论的**相互作用绘景**所假设），那么该相互作用理论实际上是自由的——其 $S$-矩阵平凡。

**含义，以及它如何闭合循环。**
1. 相互作用绘景预设了一个同时承载自由场与相互作用场的 Hilbert 空间，二者由一个酉算子联系。Haag 定理说，对一个真正相互作用的相对论理论这不可能：自由与相互作用的**真空表示酉不等价**。
2. 根本原因是 Stone–von Neumann 在无穷多自由度中的失效（s9）：有无穷多模时，Weyl 关系容许连续统多个不等价的不可约表示，自由场与相互作用场坐落在不同的表示中。
3. 这是对 s0 代数观点最强的辩护：必须把**抽象的可观测量代数**当作首要的，因为*没有单个 Hilbert 空间*是足够的。表示——真空、各温度下的热态、带电的超选择扇区——都是逐态地由 GNS 导出的。代数就是理论；Hilbert 空间是它的影子。

**例题（不等价性的一个有限缩影）。** 考虑无穷张量积 $\bigotimes_{k=1}^\infty\mathbb C^2$ 以及两个乘积态：$\omega=\bigotimes\langle\uparrow,\cdot\,\uparrow\rangle$（所有自旋向上）和 $\omega'=\bigotimes\langle\theta,\cdot\,\theta\rangle$，其中每个自旋偏转一个固定的小角度 $\theta$。每个都定义一个 GNS 表示。因为对 $\theta\ne0$ 有 $\prod_k|\langle\uparrow,\theta\rangle|=\prod_k\cos(\theta/2)=0$（无穷多个 $<1$ 的数的乘积），这两个态是**不相交的（disjoint）**：没有酉算子交缠它们的 GNS 表示。同一个代数上两个局部不可区分、整体不等价的世界——正是使 Haag 定理成立的同一机制（无穷多自由度）。

**例题 — $\beta\to0$ 与 $\beta\to\infty$ 处的 KMS。** 回到 $\mathfrak A=M_2(\mathbb C)$，Hamilton 量 $H=\mathrm{diag}(0,E)$（$E>0$），动力学 $\sigma_t(a)=e^{itH}ae^{-itH}$。$\beta$-KMS（Gibbs）态是
$$
\omega_\beta(a)=\frac{a_{11}+e^{-\beta E}a_{22}}{1+e^{-\beta E}}.
$$
当 $\beta\to\infty$（零温）时它趋于 $\omega_\infty(a)=a_{11}$，即基态——一个*纯*态，唯一的最低能量向量。当 $\beta\to0$（无穷温）时它趋于 $\omega_0(a)=\tfrac12(a_{11}+a_{22})$，即最大混合的迹态，对它模流平凡（s8）。所以 KMS 族在纯基态与无穷温度的迹混沌之间插值，而模算子 $\Delta=e^{-\beta H}\cdot\,e^{\beta H}$ 随 $\beta$ 连续形变——单个代数对象编码了系统的全部热力学。这个有限例子是一般定理的种子：KMS 态是平衡态，模流是它们内置的动力学，而在热力学或场论极限（类型 III）中这是定义平衡的*唯一*方式，因为没有 Gibbs 公式幸存下来。

---

*我们一开始就贬黜了 Hilbert 空间、抬举了可观测量代数，而数学在每一步都回报了这一选择：C\*-恒等式使范数成为一个谱不变量（s1–s2）；Gelfand 把交换代数变成空间并给出函数演算（s3）；GNS 从态重建出 Hilbert 空间（s4–s5）；von Neumann 的双交换子把分析与代数联系起来并开启了因子的类型理论（s6–s7）；迹与模流揭示出态暗中携带一个动力学，KMS 内蕴地标定了平衡（s8、s11）；而 CCR/CAR 代数与 Haag–Kastler 公理把这一切组装成相对论量子场论，在那里 Haag 定理证明了代数立场不是奢侈品而是必需品。如此解读，量子世界是一个由"可被测量者"构成的代数——而每个 Hilbert 空间不过是它众多忠实复述中的一种。*
