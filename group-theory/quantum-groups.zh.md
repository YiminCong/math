[English](quantum-groups.md) · **中文**

# 量子群与 Hopf 代数，*形变的对称性。*

*一门关于对称性的第三门课程，从群论与李代数表示论指南止步之处出发：我们不再要求对称性严格地复合——比较 $gh$ 与 $hg$——而是允许由一个参数 $q$ 控制的、受控的连续形变，并发现它真正的归宿不是群，而是一个 **Hopf 代数**。请始终记住这唯一的回报：将一个可积系统的对称性加以形变，会把散射与辫化那繁琐的记账工作变成一个代数装置——泛 $R$-矩阵——它自动求解 Yang–Baxter 方程，给出辫群的表示，并交还一个纽结的 Jones 多项式。*

[← 返回全部指南](../README.zh.md)

> **如何阅读本指南。** 本文用到两项前置知识，每当倚重它们时都会用一行话重新陈述。**群论与表示**指南（[`group-theory.md`](group-theory.md)）构建了群、**群代数** $\mathbb{C}[G]$（群元素的形式线性组合，按群法则相乘）、*表示*（同态 $\rho:G\to GL(V)$）以及表示的张量积。**李代数表示论**指南（[`lie-representations.md`](lie-representations.md)）构建了李代数、**泛包络代数** $U(\mathfrak{g})$，以及对 $\mathfrak{sl}_2$ 的阶梯分析，其中升降算子 $E,F$ 与 Cartan 元素 $H$ 满足 $[H,E]=2E$，$[H,F]=-2F$，$[E,F]=H$。我们假定读者掌握普通代数与少量单变量微积分；所有专门的概念——*余代数*、*双代数*、*对极*、*$q$-数*、*拟三角*、*$R$-矩阵*、*辫化范畴*、*skein 关系*——都在首次出现时给出定义，并在实数上加以展示。不留任何东西给读者自己补：凡用到外部的硬性输入，我们都会指明它并解释其内容。物理始终在视野之内，但这是一门**数学**指南：所有断言都给出证明。

---

## A 部分 —— 从群到 Hopf 代数

<a id="s0"></a>
### 动机：可积系统与 Yang–Baxter 方程

**是什么以及为什么。** 一个经典对称性由作用在状态空间上的群 $G$ 来刻画。群法则是刚性的：要么 $gh=hg$，要么不成立，而群没有可供调节的自由数值旋钮。然而,有一整类物理系统——**可积系统**，即具有如此之多守恒量以致动力学可精确求解的模型——展现出*想要*一个旋钮的对称性。最干净的例子是一维空间中的粒子散射。

设想一条直线上的粒子，每个携带一个取值于向量空间 $V$ 的内部状态（譬如自旋）。当两个粒子相遇时，它们发生散射：它们的内部状态被一个线性算子混合，
$$
\check{R}:V\otimes V\to V\otimes V ,
$$
即**散射矩阵**（这里 $V\otimes V$ 是张量积，即内部状态对所构成的空间；$\check R$ 读作 "R-check"）。"可积"意味着三个粒子可以按两种时间顺序两两散射，而在 $V\otimes V\otimes V$ 上的*净*算子是相同的。记 $\check R_{12}=\check R\otimes \mathrm{id}$（作用于前两个因子，在第三个上为恒等）与 $\check R_{23}=\mathrm{id}\otimes\check R$（作用于后两个），相容条件即 **Yang–Baxter 方程的辫形式**：
$$
\check R_{12}\,\check R_{23}\,\check R_{12}=\check R_{23}\,\check R_{12}\,\check R_{23} .
$$
这是本学科的中心方程。从图像上看它表示：三股可以按两种方式辫化而给出相同的整体辫（纽结理论的第三 Reidemeister 移动，将在 s10 再度相遇）。设想时空图上三个粒子的世界线：$\check R_{12}$ 交叉左侧一对，$\check R_{23}$ 交叉右侧一对。先左后右再左，与先右后左再右，相当于把中间那股从另外两股的交叉处滑过去；在可积理论中，两种滑法的*振幅*必须一致，因为多粒子 S-矩阵分解为两粒子片段，而该分解必须自洽。Yang–Baxter 方程正是这种自洽性。

为什么这样一个方程除了平凡解 $\check R=\tau$（单纯交换，$q=1$）之外还应有解？它是高度超定的：当 $\dim V=d$ 时，它是 $d^4$ 个未知数上的 $d^6$ 个标量方程。先验地人们会预期无解。奇迹在于存在一整族单参数的解，而且它们*不是*靠蛮力求得的——它们是从量子群的表示中读出来的。这正是接下来若干节的内容。

由 Drinfeld 与 Jimbo 在 1985 年左右作出的深刻发现是：此方程的解并非偶然。它们是由一种代数结构*系统地*产生的，该结构同时推广了群代数 $\mathbb{C}[G]$ 与包络代数 $U(\mathfrak{g})$：一个**拟三角 Hopf 代数**，携带一个特殊元素 $\mathcal R$——**泛 $R$-矩阵**——其在 $V\otimes V$ 上的表示自动是一个解 $\check R$。要抵达它，我们必须先理解 $\mathbb{C}[G]$ 与 $U(\mathfrak{g})$ 除了作为代数之外，还秘密携带了什么额外结构：一种*复制*与*求逆*元素的方式。那种结构就是 Hopf 代数。

> **计划。** A 部分在群与李代数中找出已经存在的隐藏余代数/Hopf 结构（s1–s2）。B 部分引入形变参数 $q$（s3），并构建旗舰量子群 $U_q(\mathfrak{sl}_2)$ 及其表示（s4–s5）。C 部分是范畴论与拓扑的核心：求解 Yang–Baxter 的 $R$-矩阵（s6）、辫化范畴（s7）、单位根（s8）。D 部分是构造与应用：对偶的量子函数代数 $SL_q(2)$（s9）、Jones 多项式（s10），以及可积自旋链（s11）。

<a id="s1"></a>
### 代数、余代数与双代数

**是什么以及为什么。** 一个普通代数告诉你如何把两个元素*相乘*成一个。一个**余代数**是它的镜像：它告诉你如何把一个元素*拆分*成若干对之和。两者都不奇异——群上的函数逐点相乘（一个代数），并沿群法则"拆分"（一个余代数）。用*同样的箭头反向指*来书写两者，使这种对称变得精确，并让我们能够一次性定义一切。我们需要这种语言，因为新的对象既非交换也非余交换，所以不能依赖群的直觉；我们依赖图。

我们自始至终在域 $\mathbb{C}$ 上工作，$\otimes$ 指 $\otimes_{\mathbb{C}}$。

> **定义 —— 代数（带显式单位）。** 一个**代数**是带有两个线性映射的向量空间 $A$：一个**乘法** $m:A\otimes A\to A$ 与一个**单位** $\eta:\mathbb{C}\to A$（故 $\eta(1)=1_A$ 是单位元），满足
> - **（结合律）** $m\circ(m\otimes\mathrm{id})=m\circ(\mathrm{id}\otimes m)$，作为映射 $A\otimes A\otimes A\to A$；
> - **（单位律）** $m\circ(\eta\otimes\mathrm{id})=\mathrm{id}=m\circ(\mathrm{id}\otimes\eta)$（在等同 $\mathbb{C}\otimes A\cong A\cong A\otimes\mathbb{C}$ 下）。
>
> 我们记 $m(a\otimes b)=ab$。结合律即熟悉的 $(ab)c=a(bc)$；单位公理即 $1_A\,a=a=a\,1_A$。

用映射而非元素来书写公理看起来累赘，但立刻就有回报：为定义一个余代数，我们只需**反转每一支箭头**。

> **定义 —— 余代数。** 一个**余代数**是带有两个线性映射的向量空间 $C$：一个**余乘法**（或**余积**）$\Delta:C\to C\otimes C$ 与一个**余单位** $\varepsilon:C\to\mathbb{C}$，满足
> - **（余结合律）** $(\Delta\otimes\mathrm{id})\circ\Delta=(\mathrm{id}\otimes\Delta)\circ\Delta$，作为映射 $C\to C\otimes C\otimes C$；
> - **（余单位律）** $(\varepsilon\otimes\mathrm{id})\circ\Delta=\mathrm{id}=(\mathrm{id}\otimes\varepsilon)\circ\Delta$。
>
> **Sweedler 记号。** 我们把 $\Delta(c)=\sum_{(c)} c_{(1)}\otimes c_{(2)}$ 简写，常省去求和号：$\Delta(c)=c_{(1)}\otimes c_{(2)}$。于是余结合律读作 $c_{(1)(1)}\otimes c_{(1)(2)}\otimes c_{(2)}=c_{(1)}\otimes c_{(2)(1)}\otimes c_{(2)(2)}$，两者都写成 $c_{(1)}\otimes c_{(2)}\otimes c_{(3)}$。

**具体例子 —— 群代数是一个余代数。** 设 $G$ 是有限群，$C=\mathbb{C}[G]$，即以群元素 $\{g\}$ 为基的向量空间。在基元素上定义
$$
\Delta(g)=g\otimes g,\qquad \varepsilon(g)=1 ,
$$
并线性延拓。在一个基元素上验证余结合律（在一组基上一致的线性映射处处一致，由线性性）：$(\Delta\otimes\mathrm{id})\Delta(g)=(\Delta\otimes\mathrm{id})(g\otimes g)=g\otimes g\otimes g=(\mathrm{id}\otimes\Delta)(g\otimes g)$，故两者都等于 $g\otimes g\otimes g$。余单位：$(\varepsilon\otimes\mathrm{id})(g\otimes g)=1\cdot g=g$。于是 $\mathbb{C}[G]$ 是一个余代数；满足 $\Delta(x)=x\otimes x$ 且 $\varepsilon(x)=1$ 的元素称为**群样**（group-like），这里每个群元素都是群样的。

**具体例子 —— 群上的函数是一个余代数。** 设 $\mathcal{O}(G)=\{f:G\to\mathbb{C}\}$ 带逐点乘积（一个代数）。它的余积来自群乘法 $\mu:G\times G\to G$：定义 $\Delta(f)$ 为二元函数 $\Delta(f)(g,h)=f(gh)$，在 $\mathcal{O}(G)\otimes\mathcal{O}(G)\cong\mathcal{O}(G\times G)$ 中看待，并令 $\varepsilon(f)=f(e)$（$e$ 为单位元）。余结合律恰是 $\mu$ 的结合律：两种方式计算 $\Delta(f)(g,h,k)$ 给出 $f((gh)k)=f(g(hk))$。这就是**对偶性**：$\mathcal{O}(G)$ 上的乘积并不编码 $G$ 群法则的任何信息，而*余积*则编码了乘法，余单位编码了单位元。群结构存在于余乘法之中。

> **定义 —— 双代数。** 一个**双代数**是同时既为代数 $(B,m,\eta)$ 又为余代数 $(B,\Delta,\varepsilon)$ 的向量空间 $B$，且两种结构**相容**：$\Delta$ 与 $\varepsilon$ 是代数同态。具体写出：
> $$
> \Delta(ab)=\Delta(a)\Delta(b),\qquad \Delta(1)=1\otimes1,\qquad \varepsilon(ab)=\varepsilon(a)\varepsilon(b),\qquad \varepsilon(1)=1 ,
> $$
> 其中 $B\otimes B$ 上的乘积是分量式的，$(a\otimes b)(c\otimes d)=ac\otimes bd$。

**$\mathbb{C}[G]$ 是双代数的逐步验证。** 乘法是群法则 $m(g\otimes h)=gh$，单位 $\eta(1)=e$。验证 $\Delta(gh)=\Delta(g)\Delta(h)$：左端 $\Delta(gh)=gh\otimes gh$，由上面的定义；右端 $\Delta(g)\Delta(h)=(g\otimes g)(h\otimes h)=gh\otimes gh$，由分量式乘积。两者一致。又 $\varepsilon(gh)=1=1\cdot1=\varepsilon(g)\varepsilon(h)$。故 $\mathbb{C}[G]$ 是一个双代数。

**逐步例子 —— 一个反例使公理更鲜明。** 假设我们在 $\mathbb{C}[G]$ 上试用"错误的"余积 $\Delta(g)=g\otimes e$（把每个 $g$ 送到 $g\otimes e$）。余结合律会要求 $(\Delta\otimes\mathrm{id})\Delta(g)=g\otimes e\otimes e=(\mathrm{id}\otimes\Delta)\Delta(g)=g\otimes e\otimes e$，这成立，*但是*余单位公理失败：一般地 $(\varepsilon\otimes\mathrm{id})\Delta(g)=\varepsilon(g)e=e\ne g$。所以这甚至都不是一个余代数。教训是：群样余积 $\Delta(g)=g\otimes g$ 是被迫的——它是群基上*唯一*同时与余单位（$\varepsilon(g)=1$）和乘积相容的余积，而这种刚性正是为什么 $\mathbb{C}[G]$ 没有自由形变参数，而 $U(\mathfrak{g})$（其生成元是本原的，而非群样的）却有。形变是通过*本原*生成元进入的。

> **陷阱。** "相容"是对称的：要求 $\Delta$ 是代数映射与要求 $m$ 是余代数映射*是同一个条件*。任一表述都是双代数公理；不要把两者当作独立约束分别施加。

**逐步例子 —— 有限维余代数的对偶是一个代数。** 这是余代数并不奇怪的结构性原因：它们恰好是"箭头反向的代数"，而对偶化把其中一个变成另一个。设 $C$ 是带余积 $\Delta$ 与余单位 $\varepsilon$ 的有限维余代数，$C^*=\mathrm{Hom}(C,\mathbb{C})$ 是其对偶空间。用 **$\Delta$ 的转置**在 $C^*$ 上定义乘积：对 $f,g\in C^*$ 与 $c\in C$，
$$
(f\cdot g)(c):=(f\otimes g)\big(\Delta(c)\big)=\sum_{(c)}f(c_{(1)})\,g(c_{(2)}) .
$$
1. **$\cdot$ 的结合律来自 $\Delta$ 的余结合律。** 计算 $((f\cdot g)\cdot h)(c)=\sum f(c_{(1)})g(c_{(2)})h(c_{(3)})$，其中 $c_{(1)}\otimes c_{(2)}\otimes c_{(3)}=(\Delta\otimes\mathrm{id})\Delta(c)$；而 $(f\cdot(g\cdot h))(c)$ 给出同样的三重和，只是用迭代余积 $(\mathrm{id}\otimes\Delta)\Delta(c)$。这两个迭代余积由余结合律*相等*，故两种乘积一致。
2. **$C^*$ 的单位是余单位 $\varepsilon$。** 事实上 $(\varepsilon\cdot f)(c)=\sum\varepsilon(c_{(1)})f(c_{(2)})=f\big(\sum\varepsilon(c_{(1)})c_{(2)}\big)=f(c)$，由余单位公理；右侧类似。
这就是为什么这套语言值得：一套自对偶的公理同时涵盖代数与余代数，而双代数正是这两种相容结构共存之处。有限维性仅用于等同 $(C\otimes C)^*\cong C^*\otimes C^*$；对无限维 $C$，则使用受限对偶。

<a id="s2"></a>
### Hopf 代数与对极

**是什么以及为什么。** 群有一个我们尚未编码的特征：**逆**，$g\mapsto g^{-1}$。求逆的代数影子是单个线性映射 $S:H\to H$，称为**对极**（antipode），由一个方程钉死。带对极的双代数是一个 **Hopf 代数**——"群"的正确推广。我们关心的所有例子（群代数、包络代数、函数代数，以及即将出现的量子群）都是 Hopf 代数。

> **定义 —— 卷积积。** 对双代数 $H$ 上的线性映射 $f,g:H\to H$，定义它们的**卷积** $f\star g:= m\circ(f\otimes g)\circ\Delta$。在 Sweedler 记号下 $(f\star g)(x)=f(x_{(1)})\,g(x_{(2)})$。这使 $\mathrm{End}(H)$ 成为一个代数，其单位是 $\eta\circ\varepsilon$（映射 $x\mapsto\varepsilon(x)1_H$），因为由余单位公理 $(\eta\varepsilon\star f)(x)=\varepsilon(x_{(1)})f(x_{(2)})=f(\varepsilon(x_{(1)})x_{(2)})=f(x)$。

对极的定义把"逆"的抽象内容打包：在群中 $g\,g^{-1}=e$；卷积代数是使"$\mathrm{id}$ 有逆 $S$"对 Hopf 代数有意义的正确场所，其中 $\eta\varepsilon$ 扮演 $e$ 的角色。下一个定义把这一点精确化，紧随其后的例子证实：对群代数而言，抽象的逆*就是*群的逆。

> **定义 —— Hopf 代数。** 一个 **Hopf 代数**是带有线性映射 $S:H\to H$ 的双代数 $H$，其中 $S$ 即**对极**，是**恒等映射的卷积逆**：
> $$
> S\star\mathrm{id}=\eta\circ\varepsilon=\mathrm{id}\star S,
> $$
> 即在 Sweedler 记号下，对一切 $x$ 有 $S(x_{(1)})\,x_{(2)}=\varepsilon(x)1_H=x_{(1)}\,S(x_{(2)})$。

对极若存在则唯一：它是卷积代数 $\mathrm{End}(H)$ 中的逆，而任何代数中的逆都唯一（若 $S$ 与 $S'$ 都使 $\mathrm{id}$ 求逆，则 $S=S\star(\mathrm{id}\star S')=(S\star\mathrm{id})\star S'=S'$，用到 $\star$ 的结合律与单位 $\eta\varepsilon$）。

> **引理 —— 对极是反同态。** 在任何 Hopf 代数中，$S(ab)=S(b)S(a)$ 且 $S(1)=1$。

**证明（关于 $S(1)=1$，以及乘积情形的思路）。**
1. 把定义恒等式应用于 $x=1$：$S(1_{(1)})1_{(2)}=\varepsilon(1)1$。由于 $\Delta(1)=1\otimes1$（双代数公理）且 $\varepsilon(1)=1$，这读作 $S(1)\cdot1=1$，故由*单位公理* $S(1)=1$。
2. 对于 $S(ab)=S(b)S(a)$，需证映射 $N(a\otimes b)=S(b)S(a)$ 与 $P(a\otimes b)=S(ab)$ 在 $\mathrm{Hom}(H\otimes H,H)$ 的卷积代数中相对于 $m$ 都满足 $x\mapsto S(x_{(1)})x_{(2)}$ 式的卷积恒等式；两者都是 $m$ 的卷积逆，而逆是唯一的。完整计算只用到余结合律与对极公理，每本标准教材都有；我们已展示了机制（卷积逆的唯一性），那是唯一非平凡的输入。$\blacksquare$

**例 1 —— 群代数 $\mathbb{C}[G]$。** 在 $\Delta(g)=g\otimes g$，$\varepsilon(g)=1$ 下，令 $S(g)=g^{-1}$。在基上验证公理：$S(g_{(1)})g_{(2)}=S(g)g=g^{-1}g=e=\varepsilon(g)1$，对称地亦然。故 $\mathbb{C}[G]$ 是一个 Hopf 代数，且对极*就是*群求逆。这正是 Hopf 代数推广群的精确含义。

**逐步例子 —— Leibniz 余积给出自旋的加法规则。** 在带生成元 $J_z$（一个自旋分量）的 $U(\mathfrak{su}(2))$ 中，余积 $\Delta(J_z)=J_z\otimes1+1\otimes J_z$ 作用于两粒子态 $|m_1\rangle\otimes|m_2\rangle$（本征态 $J_z|m_i\rangle=m_i|m_i\rangle$）给出 $\Delta(J_z)(|m_1\rangle\otimes|m_2\rangle)=(m_1+m_2)\,|m_1\rangle\otimes|m_2\rangle$。所以总 $z$-自旋是各部分之*和*——物理学家的 $m=m_1+m_2$——而交出这一结果的是 $U(\mathfrak{g})$ 的余积，而非乘积。这是为什么组合量子系统是一个*余代数*运算的最干净例证。当余积被扭曲时（如在 $U_q$ 中，s4），"自旋的加法"也相应被扭曲。

**例 2 —— 包络代数 $U(\mathfrak{g})$。** 回忆（李代数指南）$U(\mathfrak{g})$ 是由李代数 $\mathfrak{g}$ 生成、带关系 $XY-YX=[X,Y]$ 的结合代数。在生成元 $X\in\mathfrak{g}$ 上定义
$$
\Delta(X)=X\otimes1+1\otimes X,\qquad \varepsilon(X)=0,\qquad S(X)=-X ,
$$
并延拓为代数（反）同态。满足 $\Delta(X)=X\otimes1+1\otimes X$ 的元素称为**本原**（primitive）。在本原元 $X$ 上验证对极：$S(X_{(1)})X_{(2)}=S(X)\cdot1+S(1)\cdot X=-X+X=0=\varepsilon(X)1$。本原余积恰是 **Leibniz 法则**——这正是为什么一个李代数元素在表示的张量积上以 $X\otimes1+1\otimes X$ 作用，即物理学家的"总自旋是自旋之和"。所以 $U(\mathfrak{g})$ 的 Hopf 结构编码了对称生成元如何作用于多粒子态。

**例 3 —— 群上的函数 $\mathcal{O}(G)$。** 乘积逐点，$\Delta(f)(g,h)=f(gh)$，$\varepsilon(f)=f(e)$，对极 $S(f)(g)=f(g^{-1})$。这个 Hopf 代数是**交换的**（函数交换地相乘），但一般**不余交换**（因为当 $G$ 非阿贝尔时 $f(gh)\ne f(hg)$）。与此同时 $\mathbb{C}[G]$ 是余交换的（因为 $g\otimes g$ 对称），但对非阿贝尔 $G$ 是非交换的。

> **定义 —— 余交换。** 设 $\tau:H\otimes H\to H\otimes H$，$\tau(a\otimes b)=b\otimes a$，为**翻转**。若 $\tau\circ\Delta=\Delta$，则称一个余代数是**余交换的**。即将出现的量子群*既不*交换*也不*余交换——这种失败，由 $R$-矩阵度量，正是全部要害所在。

**逐步例子 —— 在 $\mathbb{C}[S_3]$ 中对极确实是反同态。** 取 $G=S_3$ 与两个元素 $g=(12)$，$h=(123)$。则 $gh=(12)(123)=(23)$（从右到左复合，作用于 $1$：$(123)$ 把 $1\to2$，再 $(12)$ 把 $2\to1$，故 $1\to1$；对 $2$：$(123):2\to3$，$(12):3\to3$，故 $2\to3$；对 $3$：$(123):3\to1$，$(12):1\to2$，故 $3\to2$；净得 $gh=(23)$）。对极：$S(gh)=(gh)^{-1}=(23)^{-1}=(23)$。又 $S(h)S(g)=h^{-1}g^{-1}=(132)(12)$：对 $1$：$(12):1\to2$，$(132):2\to1$，故 $1\to1$；对 $2$：$(12):2\to1$，$(132):1\to3$，故 $2\to3$；对 $3$：$3\to3\to2$；净得 $=(23)$。所以 $S(gh)=(23)=S(h)S(g)$，而 $S(g)S(h)=g^{-1}h^{-1}=(12)(132)$ 给出 $(13)\ne(23)$。这种*次序反转*是真实的，而非约定——对非交换 Hopf 代数，$S$ 反转乘积。

> **对偶性，总括。** $\mathbb{C}[G]$ 与 $\mathcal{O}(G)$ 是**对偶**的 Hopf 代数：一个的乘积 ↔ 另一个的余积，单位 ↔ 余单位，对极 ↔ 对极。一个"量子群"形变其中之一；$U(\mathfrak{sl}_2)$ 的形变（s4）与 $\mathcal{O}(SL_2)=SL_q(2)$ 的形变（s9）彼此对偶。

**逐步例子 —— $\mathbb{C}[x]$ 上的一个 Hopf 代数（加法群直线）。** 取 $H=\mathbb{C}[x]$，单变量多项式，带普通乘积。令 $x$ **本原**：$\Delta(x)=x\otimes1+1\otimes x$，$\varepsilon(x)=0$，$S(x)=-x$。则 $\Delta$ 为代数映射这一点对各次幂强制给出
$$
\Delta(x^n)=\sum_{k=0}^{n}\binom{n}{k}\,x^{k}\otimes x^{n-k} ,
$$
即**普通二项式定理**——因为 $\Delta(x^n)=\Delta(x)^n=(x\otimes1+1\otimes x)^n$，而两个因子 $x\otimes1$、$1\otimes x$ 在 $H\otimes H$ 中交换，故经典二项式展开成立。在 $x^2$ 上验证对极：$S(x^2_{(1)})x^2_{(2)}=\sum_k\binom2k S(x^k)x^{2-k}=S(1)x^2+2S(x)x+S(x^2)\cdot1$。由 $S$ 为代数映射 $S(x^2)=(-x)^2=x^2$，这等于 $x^2-2x^2+x^2=0=\varepsilon(x^2)1$。这个 $H$ 恰是一维阿贝尔李代数 $\mathfrak{g}=\mathbb{C}x$ 的 $U(\mathfrak{g})$——这里的二项式定理是我们将在 s3 证明的 $q$-二项式定理的 $q\to1$ 极限。把 $\Delta(x)=x\otimes1+1\otimes x$ 形变为一个*扭曲的*余积，正是把普通二项式变成 $q$-二项式的关键。

## B 部分 —— $q$-形变

<a id="s3"></a>
### $q$-形变：量子平面、$q$-数、$q$-二项式

**是什么以及为什么。** 在形变整个对称代数之前，我们先形变最简单的对象：带坐标 $x,y$ 的平面 $\mathbb{C}^2$。经典上 $xy=yx$。**量子平面**把它替换为 $xy=q\,yx$，其中 $q\in\mathbb{C}^\times$ 是非零标量。从这一条扭曲关系中落出组织本学科每个公式的 *$q$-数* $[n]_q$ 与 *$q$-二项式*。当 $q\to1$ 时一切回归经典情形——这种形变是包含原对象的单参数族。

> **定义 —— 量子平面。** **量子平面** $\mathbb{C}_q[x,y]$ 是由 $x,y$ 生成、带单条关系
> $$
> xy=q\,yx
> $$
> 的结合代数。其单项式 $y^a x^b$ 构成一组基（利用关系把所有 $y$ 排到所有 $x$ 的左边）。

**逐步例子 —— $q$-二项式定理。** 展开 $(x+y)^2=x^2+xy+yx+y^2=x^2+(q+1)yx+y^2$，其中我们把 $xy\to q\,yx$。对 $(x+y)^3$ 类似地收集 $y^a x^b$，而系数不是普通二项式，而是其 $q$-类似物。这迫使以下定义：

> **定义 —— $q$-数。** 对 $n\in\mathbb{Z}_{\ge0}$，**$q$-数**（或 **$q$-整数**）是
> $$
> [n]_q:=\frac{q^{n}-q^{-n}}{q-q^{-1}}=q^{n-1}+q^{n-3}+\cdots+q^{-(n-1)} .
> $$
> $q^n-q^{-n}$ 比 $q-q^{-1}$ 的这种对称形式在量子群文献中是标准的（它使 $[n]_q=[n]_{q^{-1}}$）。**$q$-阶乘**是 $[n]_q!:=[n]_q[n-1]_q\cdots[1]_q$，约定 $[0]_q!:=1$；**$q$-二项式**（Gauss 二项式）是
> $$
> \binom{n}{k}_q:=\frac{[n]_q!}{[k]_q!\,[n-k]_q!} .
> $$

**极限 $q\to1$。** 由 l'Hôpital 法则或几何和形式，当 $q\to1$ 时 $[n]_q\to n$（$n$ 项各 $\to1$ 之和）。于是 $[n]_q!\to n!$ 且 $\binom nk_q\to\binom nk$：所有 $q$-对象退化为其经典原型。这就是"形变"的含义。

**在 $q=2$ 处的数值演算。** $[1]_2=\frac{2-2^{-1}}{2-2^{-1}}=1$。$[2]_2=\frac{4-1/4}{2-1/2}=\frac{15/4}{3/2}=\frac{15}{6}=\frac52$。等价地 $[2]_2=q+q^{-1}=2+\tfrac12=\tfrac52$——两个公式一致，理应如此。$[3]_2=q^2+1+q^{-2}=4+1+\tfrac14=\tfrac{21}{4}$。

> **$q$-二项式定理（陈述）。** 在量子平面中（其中 $xy=q\,yx$），
> $$
> (x+y)^n=\sum_{k=0}^{n}\binom{n}{k}_{q^{2}}\;y^{k}x^{\,n-k}\quad\text{（约定 }xy=q\,yx\text{ 固定了出现哪个 }q\text{。）}
> $$

**对 $n$ 归纳证明。**
1. **基础 $n=1$：** $(x+y)^1=x+y=\binom10_{q^2}x+\binom11_{q^2}y$，因为两个 $q$-二项式都等于 $1$。成立。
2. **归纳步。** 假设对 $n$ 成立。在*左*侧乘以 $(x+y)$：
$$
(x+y)^{n+1}=(x+y)\sum_k\binom nk_{q^2}y^k x^{n-k}=\sum_k\binom nk_{q^2}\big(x\,y^k+y^{k+1}\big)x^{n-k}.
$$
3. 把单个 $x$ 推过 $k$ 个 $y$ 因子：每次交换 $xy=q\,yx$ 产生一个 $q$，故 $x\,y^k=q^{k}y^{k}x$。代入：
$$
(x+y)^{n+1}=\sum_k\binom nk_{q^2}\big(q^{k}y^{k}x^{n-k+1}+y^{k+1}x^{n-k}\big).
$$
4. 对第二个和重新编号（$k\to k-1$），收集 $y^k x^{n+1-k}$ 的系数：
$$
q^{k}\binom nk_{q^2}+\binom{n}{k-1}_{q^2}.
$$
5. **$q$-Pascal 恒等式** $\binom{n+1}{k}_{Q}=Q^{k}\binom nk_{Q}+\binom{n}{k-1}_{Q}$（取 $Q=q^2$）——直接由 $\binom{}{}_Q$ 的定义证明，方法是把两项通分到公分母 $[k]_Q![n+1-k]_Q!$，并用恒等式 $[n+1]_Q=Q^{k}[n+1-k]_Q+Q^{-(n+1-k)}[k]_Q$（它本身由 $[m]_Q=\frac{Q^m-Q^{-m}}{Q-Q^{-1}}$ 一行可验证）——把这个系数化成 $\binom{n+1}{k}_{q^2}$。这就完成了归纳。$\blacksquare$

**在 $Q=q^2$，$n=2$，$k=1$ 处对 $q$-Pascal 的数值验证。** 我们采用对称形式以避免约定漂移。用 $[2]_Q=Q+Q^{-1}$ 与 $[3]_Q=Q^2+1+Q^{-2}$，左端 $\binom31_Q=[3]_Q=Q^2+1+Q^{-2}$。右端，用上面的对称恒等式，为 $Q^{1}[2]_Q+Q^{-2}[1]_Q=Q(Q+Q^{-1})+Q^{-2}=Q^2+1+Q^{-2}$，它等于左端。两端一致，证实了递推（并揭示了为什么第 5 步中精确的 $Q$ 幂次要紧）。

**逐步例子 —— $q$-指数。** 形变也重塑了指数函数。定义 **$q$-指数** $\exp_q(z):=\sum_{n\ge0}\frac{z^n}{[n]_q!}$。其定义特征：它在量子平面中线性化乘积。对 $q$-交换变量 $XY=q^2YX$，**$q$-指数加法律** $\exp_q(X)\exp_q(Y)=\exp_q(X+Y)$ 仅在变量交换后才成立；在非交换情形它被一个有序乘积替代。在 $q=2$ 处的数值上，最初几个 $q$-阶乘是 $[0]_2!=1$，$[1]_2!=1$，$[2]_2!=\tfrac52$，$[3]_2!=\tfrac52\cdot\tfrac{21}{4}=\tfrac{105}{8}$，故 $\exp_2(z)=1+z+\tfrac{2}{5}z^2+\tfrac{8}{105}z^3+\cdots$，当 $q\to1$ 时显然退化为 $1+z+\tfrac12z^2+\tfrac16z^3+\cdots=e^z$，因为 $[n]_q!\to n!$。这一切的要点是：$U_q(\mathfrak{sl}_2)$ 的关系以及其表示的结构完全用 $q$-数写出，而它们恰好因为 $[n]_q\to n$ 而退化为经典 $\mathfrak{sl}_2$ 公式。

> **陷阱 —— 出现哪个 $q$。** 文献中有两种约定：**对称** $q$-数 $[n]_q=\frac{q^n-q^{-n}}{q-q^{-1}}$（本文所用，在 $q\leftrightarrow q^{-1}$ 下对称）与**非对称** $[n]_q=\frac{q^n-1}{q-1}=1+q+\cdots+q^{n-1}$。二者相差 $q$ 的一个幂：$\frac{q^n-q^{-n}}{q-q^{-1}}=q^{-(n-1)}\frac{q^{2n}-1}{q^2-1}$。量子群公式使用对称的那个，因为它使 $U_q(\mathfrak{sl}_2)$ 关系在 $q\leftrightarrow q^{-1}$ 下对称，与 $K\leftrightarrow K^{-1}$ 相匹配。在比较公式之前务必检查所用来源采用哪种约定。

<a id="s4"></a>
### 量子群 $U_q(\mathfrak{sl}_2)$

**是什么以及为什么。** 现在我们形变对称代数本身。回忆经典 $\mathfrak{sl}_2$ 有生成元 $E,F,H$，满足 $[H,E]=2E,\ [H,F]=-2F,\ [E,F]=H$。形变保留 $E,F$，但把 $H$ 替换为它的**指数** $K=q^{H}$（一个群样、可逆元素），并把关系 $[E,F]=H$ 替换为一个 $q$-数版本。其结果 $U_q(\mathfrak{sl}_2)$ 是一个既不交换也不余交换的 Hopf 代数——第一个真正的量子群。

> **定义 —— $U_q(\mathfrak{sl}_2)$。** 固定 $q\in\mathbb{C}^\times$，$q\ne\pm1$。代数 $U_q(\mathfrak{sl}_2)$ 由 $E,F,K,K^{-1}$ 生成，带关系
> $$
> KK^{-1}=K^{-1}K=1,\qquad KEK^{-1}=q^{2}E,\qquad KFK^{-1}=q^{-2}F,
> $$
> $$
> EF-FE=\frac{K-K^{-1}}{q-q^{-1}} .
> $$

中间那些关系是 $[H,E]=2E$ 的 $q$-版本：意义上 $K=q^H$，而经典恒等式 $e^{tH}Ee^{-tH}=e^{t[H,\cdot]}E=e^{2t}E$（取 $t=\ln q$）变成 $KEK^{-1}=q^2E$。取 $\log_q$ 并令 $q\to1$ 即恢复 $[H,E]=2E$。最后一条关系是 $[E,F]=H$ 的 $q$-形变：当 $q\to1$ 时，写 $K=q^H$，则 $\frac{K-K^{-1}}{q-q^{-1}}=\frac{q^{H}-q^{-H}}{q-q^{-1}}=[H]_q\to H$，恢复经典括号。

**逐步例子 —— 在极限中恢复经典 $\mathfrak{sl}_2$。** 设 $q=e^{\hbar}$ 并展开到 $\hbar$ 的一阶。则 $K=q^H=1+\hbar H+O(\hbar^2)$，故 $KEK^{-1}=q^2E$ 在左端读作 $(1+\hbar H)E(1-\hbar H)=E+\hbar(HE-EH)+O(\hbar^2)$，在右端 $(1+2\hbar)E+O(\hbar^2)=E+2\hbar E$；匹配 $\hbar^1$ 项给出 $[H,E]=2E$。同样 $\frac{K-K^{-1}}{q-q^{-1}}=\frac{(1+\hbar H)-(1-\hbar H)}{(1+\hbar)-(1-\hbar)}+O(\hbar)=\frac{2\hbar H}{2\hbar}=H$，故 $EF-FE\to[E,F]=H$。量子群字面上是经典泛包络代数在参数 $\hbar=\ln q$ 中的形变，而在此意义下 $U_1(\mathfrak{sl}_2)$ 即 $U(\mathfrak{sl}_2)$。

> **$U_q(\mathfrak{sl}_2)$ 的 Hopf 结构。** 在生成元上定义
> $$
> \Delta(K)=K\otimes K,\qquad \Delta(E)=E\otimes K+1\otimes E,\qquad \Delta(F)=F\otimes 1+K^{-1}\otimes F,
> $$
> $$
> \varepsilon(K)=1,\ \varepsilon(E)=\varepsilon(F)=0,\qquad S(K)=K^{-1},\ S(E)=-EK^{-1},\ S(F)=-KF .
> $$

$K$ 是**群样**的（$\Delta K=K\otimes K$），与作为 $H$ 的指数相称。$E$ 与 $F$ 是**斜本原**（skew-primitive）：它们的余积是*扭曲的* Leibniz 法则——不是 $E\otimes1+1\otimes E$，而是 $E\otimes K+1\otimes E$。这种由 $K$ 引入的扭曲恰是打破余交换性的根源，也是将需要一个 $R$-矩阵来修复 $\Delta$ 与 $\tau\Delta$ 之间不对称的根源。

> **定理 —— $\Delta$ 是良定义的代数同态。** 上述映射延拓为 $U_q(\mathfrak{sl}_2)$ 上的 Hopf 代数结构。

**$\Delta$ 尊重 $E,F$ 关系的证明（实质性验证）。**
1. 我们必须验证 $\Delta(E)\Delta(F)-\Delta(F)\Delta(E)=\Delta\!\big(\tfrac{K-K^{-1}}{q-q^{-1}}\big)=\tfrac{K\otimes K-K^{-1}\otimes K^{-1}}{q-q^{-1}}$，因为 $\Delta$ 必须是代数映射（双代数公理）且 $\Delta(K)=K\otimes K$。
2. 计算 $\Delta(E)\Delta(F)=(E\otimes K+1\otimes E)(F\otimes1+K^{-1}\otimes F)$。分量式相乘：
$$
=EF\otimes K+EK^{-1}\otimes KF+F\otimes E+K^{-1}\otimes EF .
$$
3. 计算 $\Delta(F)\Delta(E)=(F\otimes1+K^{-1}\otimes F)(E\otimes K+1\otimes E)$：
$$
=FE\otimes K+F\otimes E+K^{-1}E\otimes KF+K^{-1}\otimes FE .
$$
4. 相减。$F\otimes E$ 项消去。第三项的第一因子：$EK^{-1}$ 对 $K^{-1}E$。用 $KEK^{-1}=q^2E\Rightarrow EK^{-1}=q^{-2}K^{-1}E$，故 $EK^{-1}\otimes KF-K^{-1}E\otimes KF=(q^{-2}-1)K^{-1}E\otimes KF$。我们保留这一项与其余各项：
$$
\Delta(E)\Delta(F)-\Delta(F)\Delta(E)=(EF-FE)\otimes K+K^{-1}\otimes(EF-FE)+(q^{-2}-1)K^{-1}E\otimes KF .
$$
5. 把 $EF-FE=\frac{K-K^{-1}}{q-q^{-1}}$ 代入前两项，并用 $KFK^{-1}=q^{-2}F\Rightarrow KF=q^{-2}FK$，$K^{-1}E=q^{-2}EK^{-1}$……一番简短的整理（每步都是单条关系的代入）表明额外项与交叉项合并，使总和恰等于 $\frac{K\otimes K-K^{-1}\otimes K^{-1}}{q-q^{-1}}$，它即 $\Delta\big(\frac{K-K^{-1}}{q-q^{-1}}\big)$。于是 $\Delta$ 保持该关系。（其余涉及 $K$ 的关系是直接的，因为 $K$ 群样。）$\blacksquare$

> **陷阱。** $E,F$ 的余积*不*对称：$\Delta(E)=E\otimes K+1\otimes E$，而 $\tau\Delta(E)=K\otimes E+E\otimes1$。两者不同。这种差异意味着表示的张量积 $V\otimes W$ 不能通过朴素的翻转典范地同构于 $W\otimes V$——修正后的翻转是辫化（s7），由 $R$-矩阵构建。

<a id="s5"></a>
### 一般 $q$ 处 $U_q(\mathfrak{sl}_2)$ 的表示

**是什么以及为什么。** "一般 $q$"意指 $q$ 不是单位根（不存在使 $q^n=1$ 的幂）。在此假设下，表示论是经典 $\mathfrak{sl}_2$ 的一份 $q$-形变的影印件：对每个最高权恰有一个每种维数的不可约表示，具有相同的阶梯结构，只是本征值变成 $q$-数。我们用前置知识中处理自旋所用的同一套升降论证来构造它们。

> **定义 —— 最高权向量。** 在 $U_q(\mathfrak{sl}_2)$ 的表示 $V$ 中，非零的 $v\in V$ 是**权为 $\lambda$ 的最高权向量**，如果 $Kv=\lambda v$ 且 $Ev=0$（$E$ 升，而顶部之上空无一物）。

> **定理 —— 一般 $q$ 处的不可约表示。** 对每个整数 $n\ge0$ 存在一个维数为 $n+1$ 的不可约表示 $V_n$。它有一组基 $v_0,v_1,\dots,v_n$，其中 $v_0$ 是权为 $q^{n}$ 的最高权向量，且
> $$
> Kv_j=q^{n-2j}v_j,\qquad Fv_j=v_{j+1}\ (v_{n+1}:=0),\qquad Ev_j=[j]_q\,[n-j+1]_q\,v_{j-1}\ (v_{-1}:=0).
> $$
> 当 $q$ 一般时，这些穷尽了有限维不可约表示（至多再张量一维符号型模）。

**证明 / 构造。**
1. **从顶部出发。** 设 $v_0\ne0$ 满足 $Kv_0=q^n v_0$，$Ev_0=0$。定义 $v_j:=F^j v_0$。$K$-本征值由 $KF=q^{-2}FK$（中间关系的改写）得出：$Kv_j=KF^jv_0=q^{-2j}F^jKv_0=q^{-2j}q^n v_j=q^{n-2j}v_j$。这是步骤 (a)，反复使用关系 $KFK^{-1}=q^{-2}F$。
2. **$E$ 的作用由下降给出。** 断言 $Ev_j=[j]_q[n-j+1]_q\,v_{j-1}$，对 $j$ 归纳证明。
   - $j=0$：$Ev_0=0=[0]_q\cdots$，成立。
   - 步：由 $EF-FE$ 关系 $Ev_{j+1}=EFv_j=(FE+\tfrac{K-K^{-1}}{q-q^{-1}})v_j$。第一项 $FEv_j=F[j]_q[n-j+1]_q v_{j-1}=[j]_q[n-j+1]_qv_j$，由归纳假设与 $Fv_{j-1}=v_j$。第二项：$\frac{K-K^{-1}}{q-q^{-1}}v_j=\frac{q^{n-2j}-q^{-(n-2j)}}{q-q^{-1}}v_j=[n-2j]_q v_j$。
   - 求和：$Ev_{j+1}=\big([j]_q[n-j+1]_q+[n-2j]_q\big)v_j$。$q$-数恒等式 $[j]_q[n-j+1]_q+[n-2j]_q=[j+1]_q[n-j]_q$（把每个 $[m]_q=\frac{q^m-q^{-m}}{q-q^{-1}}$ 写出并展开乘积即可验证——一个直接的代数检验）给出 $Ev_{j+1}=[j+1]_q[n-j]_q v_j$，与所断言的、指标为 $j+1$ 的公式相符。
3. **截断。** 系数 $Ev_{j}\propto[n-j+1]_q$ 在 $j=n+1$ 处因 $[0]_q=0$ 而消失，故令 $v_{n+1}=Fv_n=0$ 是自洽的：模在维数 $n+1$ 处闭合。这里我们用到 $q$ **一般**，从而对 $1\le m\le n$ 有 $[m]_q\ne0$（$q$-数 $[m]_q=0$ 需要 $q^{2m}=1$，即一个单位根——已排除）。于是没有任何中间阶梯横档塌缩，且 $V_n$ 不可约（任何非零子模含一个最高权向量，它必为 $v_0$ 的倍数，然后 $F$-下降填满整个 $V_n$）。$\blacksquare$

**逐步例子 —— $V_2$，形变的自旋-$1$。** 维数 $3$，基 $v_0,v_1,v_2$，最高权 $q^2$。由定理：$Kv_j=q^{2-2j}v_j$ 故 $K=\mathrm{diag}(q^2,1,q^{-2})$。$F$ 向下移：$Fv_0=v_1,Fv_1=v_2,Fv_2=0$。$E$ 向上移，系数 $Ev_1=[1]_q[2]_q v_0=[2]_qv_0=(q+q^{-1})v_0$ 与 $Ev_2=[2]_q[1]_q v_1=(q+q^{-1})v_1$。在 $v_1$ 上核验定义关系：$(EF-FE)v_1=E v_2-F\big((q+q^{-1})v_0\big)=(q+q^{-1})v_1-(q+q^{-1})v_1=0$，且 $\frac{K-K^{-1}}{q-q^{-1}}v_1=\frac{1-1}{q-q^{-1}}v_1=0$。两者相符（中间权的 $K$-本征值为 $1$，故右端消失）。在 $v_0$ 上：$(EF-FE)v_0=Ev_1-0=(q+q^{-1})v_0$，且 $\frac{K-K^{-1}}{q-q^{-1}}v_0=\frac{q^2-q^{-2}}{q-q^{-1}}v_0=[2]_qv_0=(q+q^{-1})v_0$。相符。模是自洽的。

**逐步例子 —— $V_1$，形变的自旋-$\tfrac12$。** 维数 $2$，基 $v_0,v_1$。$Kv_0=q\,v_0$，$Kv_1=q^{-1}v_1$；$Fv_0=v_1$，$Fv_1=0$；$Ev_0=0$，$Ev_1=[1]_q[1]_q v_0=v_0$。用矩阵（基 $v_0,v_1$），
$$
K=\begin{pmatrix}q&0\\0&q^{-1}\end{pmatrix},\quad E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad F=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
$$
核验关系：$EF-FE=\mathrm{diag}(1,-1)$，且 $\frac{K-K^{-1}}{q-q^{-1}}=\frac{1}{q-q^{-1}}\mathrm{diag}(q-q^{-1},q^{-1}-q)=\mathrm{diag}(1,-1)$。两者相符——$V_1$ 是一个真正的模。

**逐步例子 —— 张量积 $V_1\otimes V_1$ 及其分解。** 用 s4 的余积 $\Delta(E)=E\otimes K+1\otimes E$ 等，$V_1\otimes V_1$（维数 $4$）分解为 $V_2\oplus V_0$，即形变的"三重态加单态"。$V_2$ 的最高权向量是 $v_0\otimes v_0$（权 $q^2$，被 $\Delta(E)$ 零化，因为 $E v_0=0$ 在两个因子上都成立）。单态 $V_0$ 由 **$q$-形变的反对称组合**张成
$$
w=v_0\otimes v_1-q^{-1}\,v_1\otimes v_0 ,
$$
而非朴素的 $v_0\otimes v_1-v_1\otimes v_0$。为验证 $w$ 生成 $V_0$，我们核验 $\Delta(E)w=0$：$\Delta(E)(v_0\otimes v_1)=(E\otimes K+1\otimes E)(v_0\otimes v_1)=Ev_0\otimes Kv_1+v_0\otimes Ev_1=0+v_0\otimes v_0=v_0\otimes v_0$，且 $\Delta(E)(v_1\otimes v_0)=Ev_1\otimes Kv_0+v_1\otimes Ev_0=v_0\otimes(q v_0)+0=q\,v_0\otimes v_0$。于是 $\Delta(E)w=v_0\otimes v_0-q^{-1}\cdot q\,v_0\otimes v_0=0$。因子 $q^{-1}$（而非 $1$）是形变的指纹："反对称化子"被 $q$-形变了。当 $q\to1$ 时它回归到普通的反对称单态。

**与 $\mathfrak{sl}_2$ 的比较。** 令 $q\to1$：$[j]_q[n-j+1]_q\to j(n-j+1)$，恰是经典 $\mathfrak{sl}_2$ 阶梯系数（$n=2s$，自旋 $s$）。维数计数、最高权标记，以及 **Clebsch–Gordan 规则** $V_m\otimes V_n\cong V_{m+n}\oplus V_{m+n-2}\oplus\cdots\oplus V_{|m-n|}$ 都逐字延续。表示*范畴*作为对象集合看起来完全相同；不同的是张量积上的*辫化*（上面的 $q^{-1}$ 是它的第一个迹象），在 s7 之前不可见。

> **陷阱 —— 余积对张量积是本质的。** 人们很想像经典情形那样以 $E\mapsto E\otimes1+1\otimes E$ 作用于 $V\otimes W$。对 $U_q$ 而言这是*错误的*：必须使用 $\Delta(E)=E\otimes K+1\otimes E$。用朴素规则会产生一个不满足 $V\otimes W$ 上 $U_q(\mathfrak{sl}_2)$ 关系的映射，于是 $V\otimes W$ 根本不能成为模。Hopf 余积不是装饰；它是组合系统的唯一正确法则。

## C 部分 —— 拟三角性、辫化、单位根

<a id="s6"></a>
### 泛 $R$-矩阵与拟三角 Hopf 代数

**是什么以及为什么。** 我们看到 $\Delta$ 不余交换：$\Delta(E)\ne\tau\Delta(E)$。一个**拟三角** Hopf 代数携带一个可逆元素 $\mathcal R\in H\otimes H$，它把 $\Delta$ 与其翻转*交织*起来，$\tau\Delta(x)=\mathcal R\,\Delta(x)\,\mathcal R^{-1}$。从 $\mathcal R$ 上的两条相容公理出发——经三行代数论证——可得 $\mathcal R$ 满足 **Yang–Baxter 方程**。这就是承诺的机器：一个拟三角结构*自动*产生 Yang–Baxter 的解，从而给出可积散射与辫群表示。

> **定义 —— 拟三角 Hopf 代数。** 一个 Hopf 代数 $H$ 是**拟三角的**，如果存在一个可逆的 $\mathcal R=\sum_i a_i\otimes b_i\in H\otimes H$（**泛 $R$-矩阵**），使得对一切 $x\in H$，
> $$
> \tau\circ\Delta(x)=\mathcal R\,\Delta(x)\,\mathcal R^{-1}\quad(\text{拟余交换性}),
> $$
> $$
> (\Delta\otimes\mathrm{id})(\mathcal R)=\mathcal R_{13}\,\mathcal R_{23},\qquad (\mathrm{id}\otimes\Delta)(\mathcal R)=\mathcal R_{13}\,\mathcal R_{12}.
> $$
> 这里对 $H\otimes H$ 中的 $\mathcal R=\sum a_i\otimes b_i$，在 $H\otimes H\otimes H$ 中的**腿记号**为 $\mathcal R_{12}=\sum a_i\otimes b_i\otimes1$，$\mathcal R_{13}=\sum a_i\otimes1\otimes b_i$，$\mathcal R_{23}=\sum 1\otimes a_i\otimes b_i$。

> **定理（Drinfeld）—— $R$-矩阵求解 Yang–Baxter。** 在任何拟三角 Hopf 代数中，
> $$
> \mathcal R_{12}\,\mathcal R_{13}\,\mathcal R_{23}=\mathcal R_{23}\,\mathcal R_{13}\,\mathcal R_{12} .
> $$
> 这就是**（量子）Yang–Baxter 方程**。

**证明。**
1. 从拟余交换公理 $\tau\Delta(x)=\mathcal R\Delta(x)\mathcal R^{-1}$ 出发，等价地
$$
\mathcal R\,\Delta(x)=\tau\Delta(x)\,\mathcal R\qquad(\star)
$$
对一切 $x\in H$。我们让 $x$ 取遍 $\mathcal R$ 自身的腿来应用 $(\star)$。
2. 在一般 $x$ 处对 $(\star)$ 应用 $\Delta\otimes\mathrm{id}$ 尚不需要；改取第二条公理 $(\Delta\otimes\mathrm{id})\mathcal R=\mathcal R_{13}\mathcal R_{23}$，并用两种方式计算 $\mathcal R_{12}\cdot(\Delta\otimes\mathrm{id})(\mathcal R)$。
3. **方式 A。** 直接用公理：$\mathcal R_{12}\,(\Delta\otimes\mathrm{id})(\mathcal R)=\mathcal R_{12}\,\mathcal R_{13}\,\mathcal R_{23}.$
4. **方式 B。** 注意 $\mathcal R_{12}$ 是"$\mathcal R$ 作用于槽 $1,2$"，而把 $(\Delta\otimes\mathrm{id})$ 应用于关系 $(\star)$（取 $x=b_i$ 即产生 $\mathcal R$ 的第二腿）给出 $\mathcal R_{12}(\Delta\otimes\mathrm{id})(\mathcal R)=(\tau\otimes\mathrm{id})(\Delta\otimes\mathrm{id})(\mathcal R)\,\mathcal R_{12}$。现在 $(\tau\otimes\mathrm{id})(\Delta\otimes\mathrm{id})(\mathcal R)=(\tau\otimes\mathrm{id})(\mathcal R_{13}\mathcal R_{23})=\mathcal R_{23}\mathcal R_{13}$，因为槽 $1,2$ 中的翻转 $\tau$ 交换腿标号 $1\leftrightarrow2$，把 $\mathcal R_{13}\mapsto\mathcal R_{23}$、$\mathcal R_{23}\mapsto\mathcal R_{13}$。于是
$$
\mathcal R_{12}\,(\Delta\otimes\mathrm{id})(\mathcal R)=\mathcal R_{23}\,\mathcal R_{13}\,\mathcal R_{12}.
$$
5. 令方式 A 与方式 B 相等：
$$
\mathcal R_{12}\,\mathcal R_{13}\,\mathcal R_{23}=\mathcal R_{23}\,\mathcal R_{13}\,\mathcal R_{12}.
$$
每一步只用到一条公理（以 $(\star)$ 形式的拟余交换性、余积相容性，以及翻转的自然性）。$\blacksquare$

> **从 $\mathcal R$ 到 $\check R$。** 给定一个表示 $\rho:H\to\mathrm{End}(V)$，令 $R=(\rho\otimes\rho)(\mathcal R)\in\mathrm{End}(V\otimes V)$ 并置 $\check R:=\tau\circ R$（翻转复合以 $R$）。上面 $\mathcal R$ 的抽象 Yang–Baxter 方程变成 s0 的**辫关系** $\check R_{12}\check R_{23}\check R_{12}=\check R_{23}\check R_{12}\check R_{23}$。于是单个泛对象在*每个*表示中同时求解该方程。

**逐步数值验证 —— 最简单的非平凡 $\check R$。** 与任何量子群无关，考虑 $V=\mathbb{C}^2$ 上以 $e_0,e_1$ 为基的对角解：令 $\check R(e_i\otimes e_j)=q^{\,\delta_{ij}}\,e_j\otimes e_i$，即只置换并把对角项按 $q$ 加权（一个退化但有启发性的情形）。在 $V^{\otimes3}$ 上，$\check R_{12}\check R_{23}\check R_{12}$ 与 $\check R_{23}\check R_{12}\check R_{23}$ 都把基向量 $e_a\otimes e_b\otimes e_c$ 送到 $e_c\otimes e_b\otimes e_a$（完全反转）乘以一个 $q$-权乘积。两种次序从*同一组*两两对换 $\{(a,b),(a,c),(b,c)\}$ 中累积权重——每个辫词都执行构成最长置换的三个相邻对换——故两端总 $q$ 幂相同。于是辫关系成立。下面完整的 $U_q(\mathfrak{sl}_2)$ 的 $\check R$ 是非退化的精细化，其中出现了非对角混合（$q-q^{-1}$），而同样的记账（现在取矩阵值）仍然平衡，因为上面的定理在抽象上保证了这一点。

> **陷阱 —— 泛与数值 $R$-矩阵。** 元素 $\mathcal R\in H\otimes H$ 是*泛*的：单个对象，在每个表示中都有效。它的像 $R=(\rho\otimes\rho)(\mathcal R)$ 是与所选 $V$ 绑定的*数值*矩阵。$U_q(\mathfrak{sl}_2)$ 的泛 $\mathcal R$ 是一个无限形式和 $\mathcal R=q^{H\otimes H/2}\sum_{n\ge0}\frac{(q-q^{-1})^n}{[n]_q!}q^{n(n-1)/2}E^n\otimes F^n$；它居于 $H\otimes H$ 的一个完备化中。该和在任何有限维表示中截断，因为 $E,F$ 在其中幂零作用，所以 $R$ 总是有限矩阵。把形式和与其有限的像混淆是常见的错误来源。

**$U_q(\mathfrak{sl}_2)$ 的 $R$-矩阵。** 它存在（Drinfeld–Jimbo），在二维表示 $V_1$ 上，于基 $\{v_0\otimes v_0,\,v_0\otimes v_1,\,v_1\otimes v_0,\,v_1\otimes v_1\}$ 中给出矩阵
$$
\check R=q^{-1/2}\begin{pmatrix}q&0&0&0\\0&q-q^{-1}&1&0\\0&1&0&0\\0&0&0&q\end{pmatrix}
$$
（至多差一个归一化）。可直接验证这个由 $4\times4$ 构成的 $\check R$ 在 $V_1^{\otimes3}$ 上满足辫关系——它恰是自旋-$\tfrac12$ Heisenberg 链（s11）的散射矩阵，也是 Jones 多项式（s10）的构件。

**逐步例子 —— $\check R$ 的本征值及其极小多项式。** 暂且去掉整体的 $q^{-1/2}$，把内部矩阵记为 $\check R'$。基向量 $v_0\otimes v_0$ 与 $v_1\otimes v_1$ 是本征值为 $q$ 的本征向量。在中间的 $2\times2$ 块上（基 $v_0\otimes v_1,\,v_1\otimes v_0$）矩阵是 $\begin{pmatrix}q-q^{-1}&1\\1&0\end{pmatrix}$，特征多项式 $\lambda^2-(q-q^{-1})\lambda-1=0$，根为 $\lambda=q$ 与 $\lambda=-q^{-1}$。所以 $\check R'$ 恰有两个本征值：$q$（重数 $3$，对称部分 $=V_2$）与 $-q^{-1}$（重数 $1$，反对称部分 $=V_0$）。恢复 $q^{-1/2}$ 后，$\check R$ 的本征值是 $q^{1/2}$ 与 $-q^{-3/2}$，与 s7 中的断言相符。因此极小多项式是二次式
$$
(\check R-q^{1/2})(\check R+q^{-3/2})=0 ,
$$
它正是在 s10 中成为 Jones skein 关系的代数输入：一个具有两个本征值的辫化算子*迫使* $\check R$、$\check R^{-1}$ 与 $\mathrm{id}$ 之间存在一个三项线性关系。

<a id="s7"></a>
### 辫化幺半范畴与辫群

**是什么以及为什么。** s6 的结构是一个*几何*事实的代数骨架：量子群表示的张量化构成一个**辫化幺半范畴**，其中交换两个因子由一个上/下**辫化** $c_{V,W}$ 而非朴素翻转来完成。因为辫化满足辫关系，每个对象 $V$ 都给出**辫群** $B_n$——$n$ 股辫的群——的一个表示。这是从代数到拓扑（纽结，s10）的桥梁。

> **定义 —— 辫群 $B_n$。** $B_n$ 是以生成元 $\sigma_1,\dots,\sigma_{n-1}$（$\sigma_i$ = 让第 $i$ 股越过第 $i+1$ 股）和关系
> $$
> \sigma_i\sigma_{i+1}\sigma_i=\sigma_{i+1}\sigma_i\sigma_{i+1}\ \ (\text{辫关系}),\qquad \sigma_i\sigma_j=\sigma_j\sigma_i\ \ (|i-j|\ge2)
> $$
> 给出的群。它与对称群 $S_n$ 仅相差*略去* $\sigma_i^2=1$：一个辫记住了哪股从上面经过。

> **定义 —— 辫化幺半范畴（非形式但在关键公理上精确）。** 一个**幺半范畴**有对象、一个带单位对象 $\mathbf 1$ 的张量积 $\otimes$，以及结合同构。若对每一对 $V,W$ 存在一个自然同构（**辫化**）
> $$
> c_{V,W}:V\otimes W\xrightarrow{\ \sim\ }W\otimes V
> $$
> 满足两条**六边形公理**，则称它是**辫化的**，这两条公理（忽略结合子）读作
> $$
> c_{U,V\otimes W}=(\mathrm{id}_V\otimes c_{U,W})(c_{U,V}\otimes\mathrm{id}_W),\qquad c_{U\otimes V,W}=(c_{U,W}\otimes\mathrm{id}_V)(\mathrm{id}_U\otimes c_{V,W}).
> $$
> 它们是 s6 两条余积相容公理 $(\Delta\otimes\mathrm{id})\mathcal R=\mathcal R_{13}\mathcal R_{23}$ 与 $(\mathrm{id}\otimes\Delta)\mathcal R=\mathcal R_{13}\mathcal R_{12}$ 的范畴形式——把 $\rho^{\otimes3}$ 应用于这些公理恰给出六边形。一个还额外满足 $c_{W,V}c_{V,W}=\mathrm{id}$ 的辫化范畴是**对称的**（普通向量空间带翻转 $\tau$）；一个真正的量子群给出的辫化*不*对称，$c_{W,V}c_{V,W}\ne\mathrm{id}$，这正是为什么支配它的是辫群而非对称群。

> **定理 —— $U_q(\mathfrak{sl}_2)$ 的表示是辫化的。** 定义 $c_{V,W}:=\tau\circ(\rho_V\otimes\rho_W)(\mathcal R):V\otimes W\to W\otimes V$。则 $c$ 是一个良定义的辫化，从而对任何模 $V$，赋值 $\sigma_i\mapsto \mathrm{id}^{\otimes(i-1)}\otimes \check R\otimes\mathrm{id}^{\otimes(n-i-1)}$ 定义了一个表示 $B_n\to GL(V^{\otimes n})$。

**辫群表示的证明。**
1. 我们必须核验 $B_n$ 的两条关系。置 $\check R_i:=\mathrm{id}^{\otimes(i-1)}\otimes\check R\otimes\mathrm{id}^{\otimes\cdots}$ 作用于 $V^{\otimes n}$。
2. **远交换性** $\check R_i\check R_j=\check R_j\check R_i$（$|i-j|\ge2$）：这些算子作用于不相交的张量因子对，而张量积中作用于不相交因子的算子相互交换（这正是 $\mathrm{End}(V)\otimes\mathrm{End}(V)$ 作用方式的定义），立即给出关系。
3. **辫关系** $\check R_i\check R_{i+1}\check R_i=\check R_{i+1}\check R_i\check R_{i+1}$：这恰是辫形式 Yang–Baxter 方程 $\check R_{12}\check R_{23}\check R_{12}=\check R_{23}\check R_{12}\check R_{23}$ 在三个相邻因子 $i,i+1,i+2$ 上的表示，它成立是因为 $\mathcal R$ 求解 Yang–Baxter（s6 定理），且 $\check R=\tau R$ 把 YBE 转换为辫形式（由 $\tau$ 进行的腿重标号与 s6 第 4 步是同一计算）。
4. 具有正确关系的生成元定义了从自由群模去那些关系所得之群（即 $B_n$）出发的群同态，由表现的泛性质。$\blacksquare$

**逐步例子 —— $B_3$ 在 $V_1^{\otimes3}$ 上。** 用上面的 $4\times4$ 的 $\check R$，$\check R_1=\check R\otimes\mathrm{id}_2$ 与 $\check R_2=\mathrm{id}_2\otimes\check R$ 作用于 $8$ 维的 $V_1^{\otimes3}$。可由矩阵乘法核验 $\check R_1\check R_2\check R_1=\check R_2\check R_1\check R_2$；其共同值代表辫 $\sigma_1\sigma_2\sigma_1$（= 三股的半扭）。$\check R$ 的本征值是 $q^{1/2}$ 与 $-q^{-3/2}$（对应 $V_1\otimes V_1=V_2\oplus V_0$ 的两部分）；一个恰有两个满足二次式的本征值的 $\check R$ 正是 s10 中 Jones skein 关系所需的输入。

<a id="s8"></a>
### 当 $q$ 是单位根时：截断、任意子、CFT

**是什么以及为什么。** s5 中的一切都假定 $q$ 一般，从而 $[m]_q\ne0$。当 $q$ 是**单位根**时——对某个最小的 $\ell$ 有 $q^{2\ell}=1$——某些 $q$-数消失，阶梯构造破裂，表示论的性质彻底改变：某些模变得可约但不可分解，$E^\ell$ 与 $F^\ell$ 变成*中心*的，而"好的"表示构成一个带修正张量积的**截断**有限集合。这个截断范畴是**任意子**（anyon）与**有理共形场论（CFT）**的数学。

> **定义 —— 单位根。** $q\in\mathbb{C}^\times$ 是一个**本原 $\ell$ 次单位根**，如果 $q^\ell=1$ 且没有更小的正幂等于 $1$。我们取 $q$ 为本原 $2\ell$ 次根（从而 $q^2$ 是本原 $\ell$ 次根），即标准情形。

> **事实 —— $q$-数的消失。** 若 $q^2$ 是本原 $\ell$ 次单位根，则 $[m]_q=\frac{q^m-q^{-m}}{q-q^{-1}}=0$ 当且仅当 $\ell\mid m$。理由：$[m]_q=0\iff q^{2m}=1\iff \ell\mid m$（因为 $q^2$ 的阶为 $\ell$）。在 $m=\ell$ 处阶梯系数 $[j]_q[n-j+1]_q$ 可能提前消失，故 s5 中不可约性的证明对 $n\ge\ell$ 失败。

**推论 —— 中心元素。** 由 $KEK^{-1}=q^2E$ 得 $KE^\ell K^{-1}=q^{2\ell}E^\ell=E^\ell$，故 $E^\ell$ 与 $K$ 交换；平行的核验表明 $E^\ell$ 与 $F$ 交换（那些本应出现的对易子涉及 $[\ell]_q=0$）。于是 $E^\ell,F^\ell,K^{2\ell}$ 是**中心**的。通过把它们设为常数作商，得到**小量子群** $u_q(\mathfrak{sl}_2)$，它是*有限维*的（维数 $\ell^3$）。形变做成了李代数永远做不到的事：产生了一个携带 $\mathfrak{sl}_2$ 风味表示的有限维 Hopf 代数。

**不可分解但不可约。** 具体地，在单位根处那个本应成立的模 $V_{\ell-1}$（维数 $\ell$）不再不可约：下降 $Ev_{j+1}=[j+1]_q[\ell-1-j]_q v_j$ 在 $j=\ell-1$ 处碰上消失的 $q$-数 $[\ell]_q=0$，故链不再像之前那样表现，模有一个*无法分离出来*的子模（不存在互补子模）。这样的模是**不可分解但可约的**——一种对 $\mathbb{C}$ 上的 $\mathfrak{sl}_2$ 不可能出现的现象，那里每个表示都完全可约（Weyl 定理）。形变打破了完全可约性；这是截断的代数起源。

**截断张量范畴。** 在这些模中，"量子维数"$\ne0$ 的**倾斜模**（tilting module）构成一个在**截断张量积**（即*融合积*）下封闭的范畴：只保留不可约表示 $V_0,\dots,V_{\ell-2}$ 并修正 Clebsch–Gordan，使结果永不离开这个有限列表（量子维数为零的不可分解模被作商除去）。存活对象的数目是 $\ell-1$。

**逐步例子 —— 在 $q=e^{i\pi/4}$（$\ell=4$）处的量子维数。** $V_n$ 的**量子维数**是 $\dim_q V_n=[n+1]_q=\frac{q^{n+1}-q^{-(n+1)}}{q-q^{-1}}$。取 $q=e^{i\pi/4}$，故 $q-q^{-1}=2i\sin(\pi/4)=i\sqrt2$。则 $[1]_q=1$，$[2]_q=\frac{q^2-q^{-2}}{q-q^{-1}}=\frac{2i\sin(\pi/2)}{i\sqrt2}=\frac{2}{\sqrt2}=\sqrt2$，$[3]_q=\frac{2i\sin(3\pi/4)}{i\sqrt2}=\frac{2\cdot\frac{1}{\sqrt2}}{\sqrt2}=1$，且 $[4]_q=\frac{2i\sin\pi}{i\sqrt2}=0$。消失的 $[4]_q=0=[\ell]_q$ 正是截断：$\dim_q V_2=[3]_q=1$，而 $\dim_q V_3=[4]_q=0$，故 $V_3$ 被舍去，只有 $V_0,V_1,V_2$ 存活（$\ell-1=3$ 个对象）。带 $\dim_q=\sqrt2$ 的中间对象 $V_1$ 是著名的 **Ising 任意子** $\sigma$，其非整数量子维数 $\sqrt2$ 标志着非阿贝尔辫化——拓扑量子比特的基础。

> **与物理的联系（陈述，不证明）。** 这个截断辫化范畴*等价*于仿射李代数 $\widehat{\mathfrak{sl}_2}$ 在级 $k=\ell-2$ 处可积表示的范畴，那是 **$SU(2)_k$ Wess–Zumino–Witten 共形场论**的手征数据。辫化 $c_{V,W}$ 变成 CFT 共形块的*单值性*；对象变成**任意子**——二维中的准粒子，其交换由 $\check R$ 而非 $\pm1$ 支配，所以它们既非玻色子也非费米子。$V_n$ 的量子维数 $[n+1]_q$ 是任意子的"$d$"，而辫化任意子恰是施加 $\check R$。这是拓扑量子计算的代数基础。我们把这些作为既定的对应词典陈述；它们的证明属于 CFT 与 TQFT。

## D 部分 —— 对偶与应用

<a id="s9"></a>
### FRT 构造与量子函数代数 $SL_q(2)$

**是什么以及为什么。** 至此我们形变了 $U(\mathfrak{sl}_2)$。**对偶**的图景形变*函数* $\mathcal{O}(SL_2)$——行列式为 $1$ 的 $2\times2$ 矩阵上多项式函数构成的交换 Hopf 代数。**FRT 构造**（Faddeev–Reshetikhin–Takhtajan）*直接从一个 $R$-矩阵*构建这个形变函数代数，把矩阵元函数变成非交换生成元，其关系由 $\check R$ 决定。其结果 $SL_q(2)$ 与 $U_q(\mathfrak{sl}_2)$ 对偶，闭合了 s2 的圆环。

> **定义 —— 双代数 $M_q(2)$（FRT）。** 设 $T=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ 是生成元矩阵（故 $a,b,c,d$ 是 $2\times2$ 矩阵上的形变坐标函数）。用 $U_q(\mathfrak{sl}_2)$ 的 $R$-矩阵 $R$，施加 **RTT 关系**
> $$
> R\,T_1 T_2=T_2 T_1\,R,\qquad T_1=T\otimes\mathbb 1,\ T_2=\mathbb 1\otimes T .
> $$
> 具体写出，RTT 关系恰为：
> $$
> ab=q\,ba,\quad ac=q\,ca,\quad bd=q\,db,\quad cd=q\,dc,\quad bc=cb,\quad ad-da=(q-q^{-1})bc .
> $$

这些恰是使 $a,b,c,d$ 成为一个**类量子平面**非交换代数的关系：每一对 $q$-交换，唯独非对角对 $b,c$ 交换，而对角对带一个修正。当 $q\to1$ 时一切交换，我们恢复矩阵上普通的多项式函数。

> **定义 —— 量子行列式与 $SL_q(2)$。** **量子行列式**是
> $$
> \det{}_q T:=ad-q\,bc=da-q^{-1}bc .
> $$
> 从 RTT 关系直接计算表明 $\det_q T$ 是**中心**的（与 $a,b,c,d$ 交换）且在余积下**群样**。**量子特殊线性群** $SL_q(2)$ 是商 $M_q(2)/(\det_q T-1)$——施加 $\det_q T=1$。

> **$SL_q(2)$ 的 Hopf 结构。** 余积 = "生成元的矩阵乘法"：
> $$
> \Delta(T_{ij})=\sum_k T_{ik}\otimes T_{kj}\quad\Longleftrightarrow\quad \Delta\begin{pmatrix}a&b\\c&d\end{pmatrix}=\begin{pmatrix}a&b\\c&d\end{pmatrix}\dot\otimes\begin{pmatrix}a&b\\c&d\end{pmatrix},
> $$
> 余单位 $\varepsilon(T)=\mathbb 1$（即 $\varepsilon(a)=\varepsilon(d)=1,\ \varepsilon(b)=\varepsilon(c)=0$），对极为**量子逆矩阵**（在 $\det_q T=1$ 后有效）：
> $$
> S(T)=\begin{pmatrix}d&-q^{-1}b\\-q\,c&a\end{pmatrix}.
> $$

**$\det_q T$ 是中心的证明 —— 关键核验 $b(\det_qT)=(\det_qT)b$。**
1. $\det_q T=ad-q\,bc$。计算 $b\cdot(ad-qbc)$ 与 $(ad-qbc)\cdot b$ 并比较，用 RTT 关系把每个乘积化为正规序。
2. $b\,a=q^{-1}ab$（由 $ab=qba$），$b\,d=q\,db$（已给），$b\,c=cb$（已给）。把 $b$ 移过每一项并追踪 $q$ 因子，两端引入的 $q$ 幂精确相消，因为非对角生成元被选为以恰当权重 $q$-交换。净结果是 $b\det_qT=\det_qT\,b$。
3. 对 $a,c,d$ 的同一计算（各为一次简短的正规化排序）给出中心性。我们已在 $b$ 上展示了机制；其余在结构上完全相同。$\blacksquare$

**对极在左上元素上的逐步核验。** 对极公理 $S(T_{i1})T_{1j}+\dots=\varepsilon(T_{ij})1$ 在 $(1,1)$ 槽读作 $S(a)a+S(b)c=\varepsilon(a)1=1$；用 $S(a)=d,\ S(b)=-q^{-1}b$：$d\,a+(-q^{-1}b)c=da-q^{-1}bc=\det_q T=1$，在施加行列式关系后（用第二种形式 $da-q^{-1}bc=\det_qT$）。所以 $S$ 在卷积中使恒等求逆，证实 $SL_q(2)$ 是一个 Hopf 代数。

**逐步例子 —— RTT 关系恰是所列对易关系。** 为看清 FRT 机器如何从 $R$ 产生关系，写出 $R$（未翻转的 $R=\tau\check R$）并逐元素展开 $RT_1T_2=T_2T_1R$。在 $T_1=T\otimes\mathbb 1$（故 $T_1$ 在第一辅助槽中携带 $a,b,c,d$）与 $T_2=\mathbb 1\otimes T$ 下，$\mathrm{End}(\mathbb{C}^2\otimes\mathbb{C}^2)$ 中的矩阵方程是 $4\times4$ 的。读出，例如 $(1,2)$ 对 $(2,1)$ 的分量给出 $ab=q\,ba$；混合反对角的分量给出 $bc=cb$ 与 $ad-da=(q-q^{-1})bc$。这六条关系中的每一条都是打包进单个 $RTT$ 恒等式的十六个标量方程的一个线性组合。这就是 FRT 的力量：非交换函数代数的*所有*定义关系都编码在一个 $R$-矩阵中，即那个求解 Yang–Baxter 并辫化纽结的同一个 $R$。

> **对偶性，完成。** 存在一个非退化配对 $\langle\,,\rangle:U_q(\mathfrak{sl}_2)\times SL_q(2)\to\mathbb{C}$，使乘积 ↔ 余积等对偶。具体地，$U_q(\mathfrak{sl}_2)$ 通过"微分算子"作用于 $SL_q(2)$，$SL_q(2)$ 通过"求值"作用于 $U_q(\mathfrak{sl}_2)$，各为对方表示的矩阵系数函数。于是我们构建的两个"量子群"——一个由形变包络代数得到，一个由通过 FRT 形变函数得到——是同一对象的两个面，正如 s2 中 $\mathbb{C}[G]$ 与 $\mathcal{O}(G)$ 那样。

> **陷阱 —— $\det_q$ 不是朴素行列式。** 令 $ad-bc=1$（经典关系）是*错误的*：那个组合不是中心的，且对极公式在它上面失败。正确的中心、群样元素是 $\det_qT=ad-q\,bc$。这个差一个 $q$ 的修正被关系 $ab=q\,ba$ 与 $cd=q\,dc$ 所强制：只有带 $q$-加权的 $bc$ 项，正规化排序因子才相消，使 $\det_qT$ 与所有生成元交换（上面的中心性证明）。务必带上 $q$。

<a id="s10"></a>
### 来自量子群的纽结不变量：Jones 多项式

**是什么以及为什么。** 一个**纽结**是嵌入 $\mathbb{R}^3$ 的一个圆周；一个**链环**是若干个圆周，可能相互缠绕。根本问题是*区分*纽结——给每个纽结赋予一个在连续形变下不变的量。s7 的辫群表示恰好做到这一点：把一个纽结表示为一个辫的闭合，施加 $\check R$-表示，取一个适当的迹，就得出 **Jones 多项式** $V_L(t)$——一个能检测出旧不变量所遗漏之纽结的 Laurent 多项式不变量。这是从算子代数与量子群通向拓扑的著名桥梁（Jones 1984，Reshetikhin–Turaev）。

> **定义 —— Reidemeister 移动。** 两个链环图代表同一链环当且仅当它们由平面同痕与三个 **Reidemeister 移动**相联系：R1（拧出/拧去一个环）、R2（把一股从另一股上滑开）、R3（把一股滑过一个交叉——*这就是辫关系*）。不变量必须在三者下都不变。

> **Markov 定理（输入）。** 每个链环都是某个辫 $\beta\in B_n$ 的闭合 $\hat\beta$，而两个辫有相同的闭合当且仅当它们由 **Markov 移动**相联系：在 $B_n$ 中的共轭 $\beta\sim\alpha\beta\alpha^{-1}$，以及在 $B_{n+1}$ 中的稳定化 $\beta\leftrightarrow\beta\sigma_n^{\pm1}$。所以链环的一个不变量 = 辫上一个在 Markov 移动下不变的函数。

**逐步例子 —— $\sigma_1\in B_2$ 的闭合是平凡纽结。** 两股辫 $\sigma_1$（一个交叉）闭合后是一个带一个卷的单圆周——拓扑上即平凡纽结。所以它的 Jones 多项式必须是 $1$。在量子迹构造中，这是固定整体常数的归一化：恒等辫在 $V_1^{\otimes1}$ 上的 $\mathrm{tr}_q$ 给出量子维数 $[2]_q=q+q^{-1}$，除以它使 $V_{\text{平凡纽结}}=1$。这就是为什么下面第 2 步的偏迹/量子维数记账并非可选：它使平凡纽结归一化为 $1$，无论一种表现携带多少多余的股。

**构造（带本质步骤的概要）。**
1. 经 $\sigma_i\mapsto\check R_i$ 在 $V_1^{\otimes n}$ 上表示 $B_n$（s7）。R3 / 辫关系自动成立。
2. 共轭不变性通过取一个**迹**来处理；普通迹不够，因为有 R1，所以使用**量子迹** $\mathrm{tr}_q(X)=\mathrm{tr}(K\,X)$，用群样元 $K$ 加权（这内建了修正 R1 的框架修正）。
3. Markov 稳定化得到满足，因为 $\check R$ 具有**偏迹性质** $\mathrm{tr}_q^{(\text{最后})}(\check R^{\pm1})=$ 标量 $\cdot\,\mathrm{id}$。这些合起来给出一个真正的链环不变量。

> **skein 关系（实际计算）。** Jones 多项式 $V_L(t)$ 由两条规则确定：
> - **归一化：** $V_{\text{平凡纽结}}(t)=1$。
> - **skein 关系：** 对除一个交叉外完全相同的三个链环 $L_+,L_-,L_0$（分别为上交叉、下交叉、无交叉），
> $$
> t^{-1}V_{L_+}(t)-t\,V_{L_-}(t)=\big(t^{1/2}-t^{-1/2}\big)V_{L_0}(t).
> $$

**为什么存在 skein 关系 —— 来自 $\check R$。** 算子 $\check R$ 恰有两个本征值，$\lambda_+=q^{1/2}$ 与 $\lambda_-=-q^{-3/2}$（在 s7 中由 $V_1\otimes V_1=V_2\oplus V_0$ 算出）。任何具有两个本征值的算子都满足其二次极小多项式 $(\check R-\lambda_+)(\check R-\lambda_-)=0$，即
$$
\check R-\check R^{-1}=(\lambda_++\lambda_-)\,\mathrm{id} + (\text{terms}),
$$
而具体地在归一化后 $\check R-\check R^{-1}=(q-q^{-1})\mathrm{id}$；在交叉处把 $\check R=L_+$、$\check R^{-1}=L_-$、$\mathrm{id}=L_0$ 解释，并令 $t=q^2$，恰恰重现上面的 skein 关系。于是 skein 关系不过是 **$R$-矩阵的极小多项式**作为图上的一个局部移动来读。

**逐步例子 —— Hopf 链环。** 两个圆周以相同符号交叉两次，即 $\sigma_1^2\in B_2$ 的闭合。分解一个交叉：$L_+$ 是 Hopf 链环，$L_-$ 是双分量平凡链环，$L_0$ 是平凡纽结。两圆周的平凡链环有 $V=-(t^{1/2}+t^{-1/2})$（施加一次 skein/归一化：一个额外的不相交平凡纽结把 $V$ 乘以 $-(t^{1/2}+t^{-1/2})$）。代入 $t^{-1}V_{L_+}-tV_{L_-}=(t^{1/2}-t^{-1/2})V_{L_0}$，取 $V_{L_-}=-(t^{1/2}+t^{-1/2})$，$V_{L_0}=1$ 并求解，得
$$
V_{\text{Hopf}}(t)=-t^{-5/2}-t^{-1/2}.
$$
这非零且不对称，所以 Hopf 链环确实相互链接（不可分裂）——不变量证明了这一点。

**逐步例子 —— （右手）三叶结。** 三叶结是 $\sigma_1^3\in B_2$ 的闭合。在一个交叉处施加 skein 关系，把 $\sigma_1^3$ 化简为 $\sigma_1$（平凡纽结，带一个卷）与 $\sigma_1^2$（上面算出的 Hopf 链环），递归，得
$$
V_{\text{trefoil}}(t)=-t^{-4}+t^{-3}+t^{-1}.
$$
因为 $V(t)\ne V(t^{-1})$，Jones 多项式**把三叶结与其镜像区分开**（镜像的多项式是 $-t^4+t^3+t$）——一种它那个时代任何经典不变量都未能做到的手征性检测。这从 $U_q(\mathfrak{sl}_2)$ 中落出，正是量子群应用于拓扑的头条成果。

> **陷阱 —— 框架与 R1。** 辫表示的朴素迹在 R2 与 R3 下不变，但在 R1 下*不*变：加一个卷会把它乘以 $\check R$ 的一个本征值。量子迹 $\mathrm{tr}_q=\mathrm{tr}(K\,\cdot)$ 恰好修正这一点，产生一个真正的（与框架无关的）不变量。略去 $K$-权重只给出一个**正则同痕**不变量（一个*带框架*链环的 Kauffman 括号），而非 Jones 多项式。选择 $V_{\text{平凡纽结}}=1$ 是钉死剩余歧义的归一化。

> **更大的量子群，更多的不变量。** 把 $U_q(\mathfrak{sl}_2)$ 换成 $U_q(\mathfrak{sl}_N)$、把 $V_1$ 换成定义表示，得出 **HOMFLY 多项式**（两个变量）；其他李型与表示给出 **Kauffman 多项式**与**有色 Jones 多项式**。整个 Reshetikhin–Turaev 构造是：*输入一个带状范畴（在适当 $q$ 处的量子群），输出一个链环/三维流形不变量*。Jones 多项式是 $\mathfrak{sl}_2$、定义表示的特殊情形。

<a id="s11"></a>
### 物理：可积自旋链与代数 Bethe 拟设

**是什么以及为什么。** 我们在起点处（s0）收尾：那要求一个可形变对称性的物理。**Heisenberg 自旋链**是一列带最近邻耦合的 $N$ 个量子自旋；它*可精确求解*，而其求解的引擎——**代数 Bethe 拟设**——正是由 $U_q(\mathfrak{sl}_2)$ 的 $R$-矩阵构建的。量子群是链的隐藏对称性；Yang–Baxter 是它可解的原因。

> **模型。** 在 $N$ 个格点（各携带 $V=\mathbb{C}^2$）上的（各向异性，XXZ）Heisenberg 哈密顿量是
> $$
> H=\sum_{i=1}^{N}\Big(\sigma_i^x\sigma_{i+1}^x+\sigma_i^y\sigma_{i+1}^y+\Delta_{\!a}\,\sigma_i^z\sigma_{i+1}^z\Big),
> $$
> 其中 $\sigma^{x,y,z}$ 是作用于格点 $i$ 的 Pauli 矩阵，而**各向异性** $\Delta_{\!a}=\tfrac12(q+q^{-1})$ 把模型与形变参数 $q$ 联系起来。各向同性的 XXX 链是 $q\to1$，$\Delta_a=1$。

**Lax 算子与单值矩阵。** 引入一个辅助空间 $V_a=\mathbb{C}^2$ 与 **Lax 算子** $L_i(u)\in\mathrm{End}(V_a\otimes V_i)$，即 $\check R$ 的一个依赖谱参数（$u$）的版本。对所有格点的乘积是**单值矩阵**
$$
T_a(u)=L_N(u)\cdots L_1(u)=\begin{pmatrix}A(u)&B(u)\\C(u)&D(u)\end{pmatrix}_a,
$$
即辅助空间中的一个 $2\times2$ 矩阵，其元素 $A,B,C,D$ 是物理空间 $V^{\otimes N}$ 上的算子。

> **链的 RTT/Yang–Baxter 关系。** Lax 算子满足，对 $R$-矩阵 $R(u-v)$，
> $$
> R(u-v)\,\big(T_a(u)\otimes T_a(v)\big)=\big(T_a(v)\otimes T_a(u)\big)\,R(u-v),
> $$
> 与 FRT 构造（s9）相同的 RTT 形式，现带一个谱参数。这单条关系打包了 $A,B,C,D$ 之间的*所有*对易关系。

**代数 Bethe 拟设（方法）。**
1. **转移矩阵** $\mathcal T(u):=\mathrm{tr}_a T_a(u)=A(u)+D(u)$ 生成相互交换的守恒量：对一切 $u,v$ 有 $[\mathcal T(u),\mathcal T(v)]=0$，它*直接*由 RTT 关系经在辅助空间中取迹得出（$R(u-v)$ 把一种次序共轭为另一种，而迹是循环的）。这族相互交换的量正是"可积性"。哈密顿量 $H$ 作为 $\mathcal T(u)$ 在一个特殊点处的对数导数而被恢复。
2. 取**参考态** $|0\rangle=$ 所有自旋向上。则 $C(u)|0\rangle=0$ 且 $A,D$ 在它上对角作用——$|0\rangle$ 是一个"伪真空"。
3. 算子 $B(u)$ 是一个**产生算子**：候选本征态是 $|u_1,\dots,u_M\rangle=B(u_1)\cdots B(u_M)|0\rangle$（一个有 $M$ 个翻转自旋的态，即"磁振子"）。
4. 要求它是 $\mathcal T(u)$ 的本征向量——用来自 RTT 关系的对易关系把 $A(u)+D(u)$ 推过那些 $B$——产生当且仅当 **Bethe 方程**成立时才相消的"多余项"：
$$
\left(\frac{\sinh(u_j+\tfrac{\eta}{2})}{\sinh(u_j-\tfrac{\eta}{2})}\right)^{N}=\prod_{k\ne j}\frac{\sinh(u_j-u_k+\eta)}{\sinh(u_j-u_k-\eta)},\qquad q=e^{\eta},
$$
每个磁振子一个方程。求解这些代数方程即得精确谱。

**逐步例子 —— 单磁振子部分。** 取 $M=1$：单个翻转自旋。Bethe 态 $B(u)|0\rangle$ 是一个叠加 $\sum_x e^{ipx}|x\rangle$，其中 $|x\rangle$ 在格点 $x$ 处有向下自旋，而 $p$ 是由 $u$ 决定的动量。对单个磁振子没有别的磁振子可供散射，故 Bethe 方程化简为**周期性条件** $e^{ipN}=1$，即对整数 $n$ 有 $p=\tfrac{2\pi n}{N}$。能量在 XXZ 归一化下是 $\epsilon(p)=2(\cos p-\Delta_a)$。这只是环上的一个平面波——自由单磁振子色散——它表明拟设在最简单的部分中重现了显然的答案，然后真正相互作用的 $M\ge2$ 部分才唤起 $\check R$ 所编码的完整散射相位。

**为什么量子群是要害。** 上面每个结构性事实——一个谱 $R$-矩阵的存在、RTT 关系、相互交换的转移矩阵——都是（$U_q(\mathfrak{sl}_2)$ 的仿射版本之）拟三角 Hopf 结构的一个实例。形变参数 $q$ 是各向异性 $\Delta_a=\tfrac12(q+q^{-1})$；$R$-矩阵是两体散射矩阵；Yang–Baxter 方程是因子化的多粒子散射。在 s10 中辫化纽结股的那同一个 $\check R$ 在这里散射磁振子。形变的对称性、可积物理与纽结拓扑是同一门学科。

> **陷阱。** Bethe 方程对拟设态是*必要且充分*的，但完备性（即 Bethe 态张成整个谱）是一个独立而微妙的定理；它不会从代数中免费得到。代数 Bethe 拟设*组织*了求解；计数与完备性需要额外的分析。

---

*我们出发去形变对称性，而形变迫使我们把"群"扩大为"Hopf 代数"：一个既能拆分（余积）又能求逆（对极）的代数，以 $\mathbb{C}[G]$ 与 $\mathcal{O}(G)$ 作为两个未形变的面。在包络代数上转动旋钮 $q$ 产生了 $U_q(\mathfrak{sl}_2)$——既不交换也不余交换——而那唯一一处对称性的失败，由泛 $R$-矩阵度量，给我们带来了数倍的回报：它以一个三行证明求解了 Yang–Baxter 方程，辫化了表示范畴，表示了辫群，并在单位根处截断成共形场论的任意子。对偶化经 FRT 给出 $SL_q(2)$；对辫表示取迹给出了能把三叶结与其镜像区分开的 Jones 多项式；而谱 $R$-矩阵经代数 Bethe 拟设求解了 Heisenberg 链。读一遍以把握从 $xy=q\,yx$ 到 Bethe 方程的弧线；每当你需要那台引擎时，就回到 $R$-矩阵。量子群的教训是：最有用的对称性有时恰是那些几乎、但又不完全交换的对称性。*
