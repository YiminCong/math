[English](homological-algebra.md) · **中文**

# 同调代数与谱序列，*（上）同调背后的机器。*

*一门从零开始讲授驱动一切（上）同调理论之代数的课程：正合列与图追踪、链复形、消解、导出函子* $\mathrm{Tor}$ *与* $\mathrm{Ext}$*、万有系数定理与 Künneth 定理，最后是谱序列——一种用以组织那些任何单条长正合列都无法企及的计算的记账装置。每个代数术语在首次出现时都给出定义，每条定理都无遗漏地加以论证。*

[← 返回全部指南](../README.zh.md)

> **如何阅读本指南。** 此前的两份指南有帮助但并非严格必需。我们从《群论》指南借用*群*、*阿贝尔群*、*同态*、*核*、*像*、*商*与*正合列*等词；每个都在首次使用处用一行重述。我们从《代数拓扑》指南借用这样的思想：一个空间产生一个*链复形*，其同调是一种拓扑不变量——§s10 会回到这幅图景。我们仅假定普通的算术和一点单变量微积分。没有任何东西“留给读者”：每个论断都给出证明。

---

## A 部分 —— 正合性的代数

<a id="s0"></a>
### 动机：作为一切（上）同调之组织机器的导出函子与谱序列

同调与上同调理论遍布数学的各个角落——拓扑空间的同调、群的上同调、层的上同调、模的 Tor 与 Ext。它们表面看上去各不相同，却共享同一台引擎。本指南就来构建这台引擎。

这台引擎有两半。

- **导出函子。** 代数对象上的许多自然运算*几乎*是正合的——它们保持正合列的*部分*结构，却在某一处将其破坏。**导出函子**是一种系统化的装置，它在每个度数上精确地度量被破坏了多少。两个原型是 $\mathrm{Tor}$（度量张量积不正合的程度）和 $\mathrm{Ext}$（度量 $\mathrm{Hom}$ 不正合的程度）。带系数的奇异同调、万有系数定理与 Künneth 公式，都是关于这两个函子的论断。

- **谱序列。** 当一个对象同时沿*两个*方向构造而成时——被子空间过滤的空间、复形的复形、带底空间与纤维的纤维化——其同调通常无法一步读出。**谱序列**是一部逐次逼近的“电影”：一列页 $E_1, E_2, E_3,\dots$，每一页通过取同调由前一页算出，在良好情形下*收敛*到答案。它是包含长正合列、Künneth 公式以及纤维化的 Leray–Serre 计算作为特例的总工具。

> **全指南的主线。** 建立正合性的语言（§s1–s2），学会把对象消解为简单部件（§s3），将其转化为导出函子（§s4），在拓扑中兑现它（§s5），把这一模式抽象为范畴论（§s6），最后把双复形与过滤的二维记账装配为谱序列（§s7–s11）。

> **一个例子作为预览。** 考虑最简单的非正合性：把正合列 $0\to\mathbb{Z}\xrightarrow{\times2}\mathbb{Z}\to\mathbb{Z}/2\to0$ 与 $\mathbb{Z}/2$ 做张量积会破坏单射性（§s4）。度量这一破坏的单一数值是 $\mathrm{Tor}_1^{\mathbb{Z}}(\mathbb{Z}/2,\mathbb{Z}/2)=\mathbb{Z}/2$。正是同一个 $\mathrm{Tor}$ 使得 $H_2(\mathbb{RP}^2;\mathbb{Z}/2)$ 非零（§s5），而同一圈思想在二维中运行，便计算出 Hopf 纤维化的同调（§s10），以及从正规子群与商的上同调出发计算群的上同调（§s11）。一套机制，多种面貌。

自始至终，核心对象是**模**，即“阿贝尔群”与“向量空间”的共同推广。我们就从这里开始。

<a id="s1"></a>
### 模、正合列与图追踪——蛇引理与五引理

**是什么与为什么。** 为了统一地做代数，我们需要一种足够灵活、能够囊括阿贝尔群、向量空间以及“整数上的向量空间”的单一对象。这个对象就是*环上的模*。于是“正合性”——精确地说，即一个映射的像恰是下一个映射的核——便成为整门学科的语法，而*图追踪*则是我们在这门语法中证明命题的方式。

> **定义 —— 环。**
> 一个**环** $R$ 是一个带有两种运算（加法 $+$ 与乘法 $\cdot$）的集合，使得 $(R,+)$ 是阿贝尔群（加法满足结合律与交换律，有零元 $0$，且每个元素都有负元），乘法满足结合律并有单位元 $1$，且乘法对加法满足分配律：$a(b+c)=ab+ac$ 以及 $(a+b)c=ac+bc$。若总有 $ab=ba$，则该环是**交换**的。*例：* 整数 $\mathbb{Z}$，以及任意域，如有理数 $\mathbb{Q}$ 或实数 $\mathbb{R}$。

> **定义 —— 模。**
> 环 $R$ 上的一个**左模**（即“$R$-模”）是一个阿贝尔群 $(M,+)$ 连同一个数乘 $R\times M\to M$，记作 $(r,m)\mapsto rm$，对一切 $r,s\in R$ 与 $m,n\in M$ 满足：
> $$
> r(m+n)=rm+rn,\quad (r+s)m=rm+sm,\quad (rs)m=r(sm),\quad 1\,m=m.
> $$
> *例：* 一个 $\mathbb{Z}$-模*恰好*是一个阿贝尔群（用 $n$ 做数乘就是“把 $m$ 自身相加 $n$ 次”）；域 $k$ 上的一个模*恰好*是 $k$ 上的一个向量空间。所以“模”是两者共同的母概念。

> **定义 —— 模同态（= $R$-线性映射）。**
> $R$-模之间的映射 $f:M\to N$ 若同时保持两种运算，则称为**同态**：$f(m+m')=f(m)+f(m')$ 且 $f(rm)=rf(m)$。它的**核**是 $\ker f=\{m:f(m)=0\}$，**像**是 $\mathrm{im}f=\{f(m):m\in M\}$；二者都是子模。$f$ 是**单射**（一对一）当且仅当 $\ker f=0$，是**满射**（映上）当且仅当 $\mathrm{im}f=N$。双射同态是**同构**，记作 $\cong$。

> **定义 —— 商模。**
> 若 $K\subseteq M$ 是子模，则**商** $M/K$ 的元素是陪集 $m+K=\{m+k:k\in K\}$，运算为 $(m+K)+(m'+K)=(m+m')+K$ 与 $r(m+K)=rm+K$。映射 $\pi:M\to M/K$，$\pi(m)=m+K$，是核为 $K$ 的满同态。*（下面要用到的第一同构定理：任意同态 $f:M\to N$ 诱导 $M/\ker f\cong \mathrm{im} f$。）*

> **定义 —— 正合列。**
> $R$-模与同态构成的序列 $\cdots\to A\xrightarrow{\,f\,}B\xrightarrow{\,g\,}C\to\cdots$ 在 $B$ 处**正合**，若 $\mathrm{im}f=\ker g$。若它在每个内部模处都正合，则称它**正合**。**短正合列（SES）**是形如
> $$
> 0\to A\xrightarrow{\,f\,}B\xrightarrow{\,g\,}C\to 0
> $$
> 的正合列，它可展开为：$f$ 是单射（在 $A$ 处正合：$\mathrm{im}(0\to A)=0=\ker f$），$g$ 是满射（在 $C$ 处正合：$\mathrm{im}g=\ker(C\to0)=C$），且 $\mathrm{im}f=\ker g$，故由第一同构定理 $C\cong B/\mathrm{im}f$。

*已解例。* $0\to \mathbb{Z}\xrightarrow{\,\times 2\,}\mathbb{Z}\xrightarrow{\bmod 2}\mathbb{Z}/2\to 0$ 是 $\mathbb{Z}$-模的短正合列：乘以 $2$ 是单射，模 $2$ 约化是满射，而“$\times 2$”的像是偶整数，恰是“模 $2$”的核。我们将反复使用这条正合列。

*第二个已解例（手工核验正合性）。* 考虑 $\mathbb{Z}\xrightarrow{\,f\,}\mathbb{Z}\xrightarrow{\,g\,}\mathbb{Z}/6$，其中 $f=\times3$ 而 $g=\bmod 6$。它在中间的 $\mathbb{Z}$ 处正合吗？计算 $\mathrm{im}f=3\mathbb{Z}=\{\dots,-3,0,3,6,\dots\}$ 与 $\ker g=6\mathbb{Z}$。由于 $3\mathbb{Z}\neq6\mathbb{Z}$（例如 $3\in\mathrm{im}f$ 但 $g(3)=3\neq0$，故 $3\notin\ker g$），该序列在中间处**不**正合。把 $f$ 换成 $\times6$：现在 $\mathrm{im}f=6\mathbb{Z}=\ker g$，于是它正合。这正是后面每个证明都归结到的那种显式的“核对像”记账。

#### 图追踪

**交换图**是一幅由模与箭头构成的图，其中任意两条具有相同起点与终点的有向路径给出相等的复合映射。**图追踪**通过在这样的图中追踪单个元素来证明命题，每一步都以正合性或交换性为依据。两个基础性结果是蛇引理与五引理。

> **蛇引理。** 给定一个行正合的交换图
> $$
> \begin{array}{ccccccccc}
> & & A & \xrightarrow{\,f\,} & B & \xrightarrow{\,g\,} & C & \to & 0\\
> & & \downarrow{\scriptstyle a} & & \downarrow{\scriptstyle b} & & \downarrow{\scriptstyle c} & & \\
> 0 & \to & A' & \xrightarrow{\,f'\,} & B' & \xrightarrow{\,g'\,} & C' & &
> \end{array}
> $$
> 则存在一条正合列
> $$
> \ker a\to\ker b\to\ker c\xrightarrow{\;\partial\;}\mathrm{coker}a\to\mathrm{coker}b\to\mathrm{coker}c,
> $$
> 其中 $\mathrm{coker}a=A'/\mathrm{im}a$ 是**余核**，而 $\partial$ 是**连接同态**。若 $f$ 是单射，则该序列左端可补上 $0\to\ker a$；若 $g'$ 是满射，则右端可补上 $\mathrm{coker}c\to 0$。

**证明（完整图追踪）。**

1. *核上的诱导映射。* 若 $x\in\ker a\subseteq A$，则由左方形交换性 $b(f(x))=f'(a(x))=f'(0)=0$，故 $f$ 限制为 $\ker a\to\ker b$。同理 $g$ 限制为 $\ker b\to\ker c$。*（方形的交换性）*
2. *余核上的诱导映射。* 若 $y\in A'$，则 $f'$ 把 $\mathrm{im}a$ 送入 $\mathrm{im}b$（因为 $f'(a(x))=b(f(x))\in\mathrm{im}b$），故 $f'$ 下降为 $\bar f':\mathrm{coker}a\to\mathrm{coker}b$，$\bar f'(y+\mathrm{im}a)=f'(y)+\mathrm{im}b$。同理 $g'$ 下降为 $\bar g'$。*（再次用交换性，加上商的泛性质）*
3. *定义连接映射 $\partial:\ker c\to\mathrm{coker}a$。* 取 $z\in\ker c\subseteq C$。由于 $g$ 是满射（顶行在 $C$ 处正合），选 $b_0\in B$ 使 $g(b_0)=z$。则 $g'(b(b_0))=c(g(b_0))=c(z)=0$，故 $b(b_0)\in\ker g'=\mathrm{im}f'$（底行在 $B'$ 处正合）。选唯一的 $a_0\in A'$ 使 $f'(a_0)=b(b_0)$（唯一是因为 $f'$ 是单射）。令 $\partial(z)=a_0+\mathrm{im}a\in\mathrm{coker}a$。*（$g$ 的满射性；交换性；在 $B'$ 处正合；$f'$ 的单射性）*
4. *$\partial$ 是良定义的。* 设 $b_1$ 是另一个提升，$g(b_1)=z$。则 $g(b_0-b_1)=0$，故对某 $w\in A$ 有 $b_0-b_1=f(w)$（在 $B$ 处正合）。于是 $b(b_0)-b(b_1)=b(f(w))=f'(a(w))$。因此对应的 $a_0$ 值相差 $a(w)\in\mathrm{im}a$，故它们在 $\mathrm{coker}a$ 中一致。$a_0$ 的选取无关性是自动的，因为 $f'$ 是单射。从而 $\partial$ 是良定义的同态（把所有选取都做成可加的即得线性性）。*（在 $B$ 处正合；交换性；coker 的定义）*
5. *在 $\ker b$ 处正合。* 若 $x\in\ker a$，则 $g(f(x))=0$（顶行在 $B$ 处正合），故 $\mathrm{im}(\ker a\to\ker b)\subseteq\ker(\ker b\to\ker c)$。反之若 $u\in\ker b$ 且 $g(u)=0$，则对某 $x\in A$ 有 $u=f(x)$（在 $B$ 处正合）；且 $f'(a(x))=b(f(x))=b(u)=0$，故 $a(x)=0$（$f'$ 单射），即 $x\in\ker a$。于是 $u$ 落在像中。*（在 $B$ 处正合；$f'$ 的单射性）*
6. *在 $\ker c$ 处正合。* 若 $u\in\ker b$，追踪 $\partial(g(u))$：$g(u)$ 的一个提升就是 $u$ 本身，$b(u)=0=f'(0)$，故 $\partial(g(u))=0$。反之若 $z\in\ker c$ 满足 $\partial(z)=0$，则在构造中 $a_0\in\mathrm{im}a$，设 $a_0=a(w)$；则 $b(b_0)=f'(a_0)=f'(a(w))=b(f(w))$，故 $b_0-f(w)\in\ker b$ 且 $g(b_0-f(w))=g(b_0)=z$，从而把 $z$ 展示为 $\ker b\to\ker c$ 像中的元素。*（定义；交换性；在 $B$ 处正合）*
7. *在 $\mathrm{coker}a$ 处正合。* 对满足 $\partial(z)=a_0+\mathrm{im}a$ 的 $z\in\ker c$，有 $\bar f'(\partial(z))=f'(a_0)+\mathrm{im}b=b(b_0)+\mathrm{im}b=0$，故 $\bar f'\circ\partial=0$。反之若 $a_0+\mathrm{im}a\in\ker\bar f'$，则对某 $b_0\in B$ 有 $f'(a_0)=b(b_0)$；令 $z=g(b_0)$，则 $c(z)=c(g(b_0))=g'(b(b_0))=g'(f'(a_0))=0$（底行在 $B'$ 处正合），故 $z\in\ker c$ 且由构造 $\partial(z)=a_0+\mathrm{im}a$。*（交换性；在 $B'$ 处正合）*
8. *在 $\mathrm{coker}b$ 处正合。* 第 5 步的镜像，对偶到余核上：由 $g'f'=0$ 得 $\bar g'\circ\bar f'=0$，而被 $\bar g'$ 零化的类，凭借 $g$ 的满射性与底行的正合性，来自 $\mathrm{coker}a$。这一论证是第 5 步的形式对偶（反转所有箭头并把核换成余核）。*（在 $B'$ 处与在 $C$ 处正合）* $\;\blacksquare$

> **五引理。** 在一个行正合的交换图
> $$
> \begin{array}{ccccccccc}
> A_1 & \to & A_2 & \to & A_3 & \to & A_4 & \to & A_5\\
> \downarrow{\scriptstyle f_1} & & \downarrow{\scriptstyle f_2} & & \downarrow{\scriptstyle f_3} & & \downarrow{\scriptstyle f_4} & & \downarrow{\scriptstyle f_5}\\
> B_1 & \to & B_2 & \to & B_3 & \to & B_4 & \to & B_5
> \end{array}
> $$
> 中，若 $f_1$ 是满射，$f_5$ 是单射，且 $f_2,f_4$ 是同构，则 $f_3$ 是同构。

**证明。** 把水平映射记作 $\alpha_i:A_i\to A_{i+1}$ 与 $\beta_i:B_i\to B_{i+1}$。

1. *（$f_3$ 单射。）* 设 $x\in\ker f_3$。则 $f_4(\alpha_3(x))=\beta_3(f_3(x))=0$，而 $f_4$ 单射给出 $\alpha_3(x)=0$，故 $x\in\ker\alpha_3=\mathrm{im}\alpha_2$（顶行在 $A_3$ 处正合）；写 $x=\alpha_2(w)$。则 $\beta_2(f_2(w))=f_3(\alpha_2(w))=f_3(x)=0$，故 $f_2(w)\in\ker\beta_2=\mathrm{im}\beta_1$；写 $f_2(w)=\beta_1(v)$。由于 $f_1$ 是满射，$v=f_1(u)$；则 $\beta_1(f_1(u))=f_2(\alpha_1(u))$，故 $f_2(w)=f_2(\alpha_1(u))$，而 $f_2$ 单射给出 $w=\alpha_1(u)$。从而 $x=\alpha_2(w)=\alpha_2(\alpha_1(u))=0$（顶行在 $A_2$ 处正合）。故 $\ker f_3=0$。*（$f_4,f_2$ 的单射性；正合性；$f_1$ 的满射性）*
2. *（$f_3$ 满射。）* 设 $y\in B_3$。则 $\beta_3(y)\in B_4$；由于 $f_4$ 是满射，对某 $t\in A_4$ 有 $\beta_3(y)=f_4(t)$。现 $f_5(\alpha_4(t))=\beta_4(f_4(t))=\beta_4(\beta_3(y))=0$（底行在 $B_4$ 处正合），而 $f_5$ 单射给出 $\alpha_4(t)=0$，故 $t\in\ker\alpha_4=\mathrm{im}\alpha_3$；写 $t=\alpha_3(s)$。考虑 $y-f_3(s)$：$\beta_3(y-f_3(s))=f_4(t)-\beta_3(f_3(s))=f_4(t)-f_4(\alpha_3(s))=f_4(t)-f_4(t)=0$，故 $y-f_3(s)\in\ker\beta_3=\mathrm{im}\beta_2$；写 $y-f_3(s)=\beta_2(p)$。由于 $f_2$ 是满射，$p=f_2(q)$，且 $\beta_2(f_2(q))=f_3(\alpha_2(q))$，故 $y-f_3(s)=f_3(\alpha_2(q))$，给出 $y=f_3(s+\alpha_2(q))\in\mathrm{im}f_3$。*（$f_4,f_5,f_2$ 的满射性/单射性；正合性）* $\;\blacksquare$

> **已解例 —— 蛇引理给出对 $0\to\mathbb{Z}/2\to\mathbb{Z}/4\to\mathbb{Z}/2\to0$ 的分析。** 把蛇引理应用于这样的图：行为 $0\to\mathbb{Z}\xrightarrow{\times2}\mathbb{Z}\to\mathbb{Z}/2\to0$（顶行）与同一行（底行），竖直映射在两个 $\mathbb{Z}$ 上为 $a=b=\times2$，而 $c$ 是 $\mathbb{Z}/2$ 上的诱导映射（它是 $0$，因为 $2\equiv0$）。则 $\ker a=\ker b=0$，$\ker c=\mathbb{Z}/2$，$\mathrm{coker}a=\mathrm{coker}b=\mathbb{Z}/2$，$\mathrm{coker}c=\mathbb{Z}/2$。蛇序列读作
> $$
> 0\to0\to\mathbb{Z}/2\xrightarrow{\partial}\mathbb{Z}/2\to\mathbb{Z}/2\to\mathbb{Z}/2\to0,
> $$
> 正合性迫使 $\partial$ 为单射。按第 3 步追踪 $\partial$ 的构造：把 $\ker c=\mathbb{Z}/2$ 的生成元提升到 $1\in\mathbb{Z}$（顶行），施以 $b=\times2$ 得 $2\in\mathbb{Z}$（底行），沿 $f'=\times2$ 拉回得 $1\in\mathbb{Z}$，投影到 $1\in\mathrm{coker}a=\mathbb{Z}/2$——于是 $\partial$ 把生成元送到生成元，是一个同构。这个连接映射正是检测 $\mathbb{Z}/4$ 与 $\mathbb{Z}/2\oplus\mathbb{Z}/2$ 之差异的 Bockstein 同态。

**陷阱。** 图追踪使用*元素*，这对模是合法的，但对任意抽象情形并非如此；§s6 解释这些引理如何凭借更细致的论证在任意阿贝尔范畴中存活。此外，蛇引理的连接映射 $\partial$ 是典范的，*尽管*第 3 步中做了选择——良定义性的核验并非走过场，它正是该引理的核心。

<a id="s2"></a>
### 链复形、同调与链同伦

**是什么与为什么。** 单条正合列没有“洞”。同调的要点在于研究*未能*正合的序列并度量这一失败。承载这一思想的载体就是链复形。

> **定义 —— 链复形。**
> $R$-模的一个**链复形** $C_\bullet$ 是一族 $(C_n)_{n\in\mathbb{Z}}$ 连同**边界映射** $\partial_n:C_n\to C_{n-1}$，对一切 $n$ 满足 $\partial_{n-1}\circ\partial_n=0$。条件 $\partial\partial=0$ 即 $\mathrm{im}\partial_{n+1}\subseteq\ker\partial_n$。$\ker\partial_n$ 中的元素是**闭链** $Z_n$；$\mathrm{im}\partial_{n+1}$ 中的元素是**边缘链** $B_n$。

> **定义 —— 同调。**
> **第 $n$ 阶同调**是商模
> $$
> H_n(C_\bullet)=\ker\partial_n/\mathrm{im}\partial_{n+1}=Z_n/B_n.
> $$
> 它度量“不是边缘链的闭链”。该复形在 $C_n$ 处正合当且仅当 $H_n=0$；于是**同调是非正合性的精确度量。** **上链复形**是把箭头升起的同物，$d^n:C^n\to C^{n+1}$，$d^{n+1}d^n=0$；其**上同调**是 $H^n=\ker d^n/\mathrm{im}d^{n-1}$。

*已解例。* 设 $C_1=\mathbb{Z}\xrightarrow{\times 2}C_0=\mathbb{Z}$，其余 $C_n=0$。则 $\partial_1=\times2$，$\partial_0=0$。度数 $0$ 处的闭链：整个 $\mathbb{Z}$（因 $\partial_0=0$）。度数 $0$ 处的边缘链：$\mathrm{im}(\times2)=2\mathbb{Z}$。故 $H_0=\mathbb{Z}/2\mathbb{Z}$。度数 $1$ 处：闭链 $=\ker(\times2)=0$，故 $H_1=0$。该复形“看见”了挠 $\mathbb{Z}/2$。

> **定义 —— 链映射。**
> 一个**链映射** $f_\bullet:C_\bullet\to D_\bullet$ 是一族 $f_n:C_n\to D_n$，与边界映射交换：$\partial^D_n f_n=f_{n-1}\partial^C_n$。链映射把闭链送到闭链、边缘链送到边缘链，因此在同调上诱导 $f_*:H_n(C)\to H_n(D)$。

**演示 —— $f_*$ 是良定义的。**
1. 若 $z\in Z_n(C)$，则 $\partial^D f(z)=f(\partial^C z)=f(0)=0$，故 $f(z)\in Z_n(D)$。*（链映射条件）*
2. 若 $z=\partial^C w\in B_n(C)$，则 $f(z)=f(\partial^C w)=\partial^D f(w)\in B_n(D)$。*（链映射条件）*
3. 因此 $f$ 把 $Z_n$ 映到 $Z_n$、$B_n$ 映到 $B_n$，故公式 $f_*(z+B_n)=f(z)+B_n$ 与代表元的选取无关——是 $H_n$ 上一个良定义的同态。*（商的泛性质）* $\;\blacksquare$

> **定义 —— 链同伦。**
> 两个链映射 $f_\bullet,g_\bullet:C_\bullet\to D_\bullet$ 是**链同伦的**，若存在一族 $h_n:C_n\to D_{n+1}$（不要求交换）满足
> $$
> f_n-g_n=\partial^D_{n+1}h_n+h_{n-1}\partial^C_n.
> $$
> 我们记 $f\simeq g$，并称 $h$ 为**链同伦**。

> **定理（同伦不变性）。** 若 $f\simeq g$，则在同调上 $f_*=g_*$。

**证明。**
1. 设 $z\in Z_n(C)$，故 $\partial^C z=0$。施以同伦恒等式：$f(z)-g(z)=\partial^D h(z)+h(\partial^C z)=\partial^D h(z)+h(0)=\partial^D h(z)$。*（同伦恒等式；$z$ 是闭链）*
2. 于是 $f(z)-g(z)\in B_n(D)$，故 $f(z)$ 与 $g(z)$ 在 $H_n(D)$ 中代表*同一*个类。*（边缘链与同调类的定义）*
3. 从而对每个闭链 $z$ 有 $f_*(z+B)=g_*(z+B)$，即 $f_*=g_*$。$\;\blacksquare$

> **定理（同调的长正合列）。** 链复形的短正合列 $0\to A_\bullet\xrightarrow{f}B_\bullet\xrightarrow{g}C_\bullet\to 0$（在每个度数上正合）诱导一条长正合列
> $$
> \cdots\to H_n(A)\xrightarrow{f_*}H_n(B)\xrightarrow{g_*}H_n(C)\xrightarrow{\partial_*}H_{n-1}(A)\to\cdots
> $$

**证明。** 把蛇引理（§s1）应用于这样的交换图：其两行是相邻度数上复形 SES 的 $\partial$-映射；蛇引理的连接映射*正是* $\partial_*$，而把所得六项正合列在所有 $n$ 上拼接即产生长正合列。具体地：每个度数上 $0\to A_n\to B_n\to C_n\to 0$ 正合，$\partial$ 与 $f,g$ 交换，蛇引理给出在每个 $H_n$ 处的正合性连同 $\partial_*$；核验相继的六项片段能够拼接，即是把蛇的 $\ker\to\mathrm{coker}$ 映射跨度数对接起来。$\;\blacksquare$

> **已解例 —— 长正合列的实际运用（偶对 $(D^2,S^1)$）。** 在代数拓扑中，圆盘 $D^2$ 具有一点的同调（$H_0=\mathbb{Z}$，所有更高阶为 $0$），而圆 $S^1$ 具有 $H_0=H_1=\mathbb{Z}$。相对链拼成复形的 SES $0\to C_\bullet(S^1)\to C_\bullet(D^2)\to C_\bullet(D^2,S^1)\to0$，给出长正合列
> $$
> \cdots\to H_2(D^2,S^1)\xrightarrow{\partial_*}H_1(S^1)\xrightarrow{i_*}H_1(D^2)\to H_1(D^2,S^1)\to H_0(S^1)\to\cdots
> $$
> 代入 $H_1(D^2)=0$，正合性迫使 $\partial_*:H_2(D^2,S^1)\to H_1(S^1)=\mathbb{Z}$ 为满射；与其左侧的 $H_2(D^2)=0$ 结合，它还是单射，故 $H_2(D^2,S^1)\cong\mathbb{Z}$。连接映射“$\partial_*$”——蛇的 $\partial$——恰是把圆检测为圆盘边缘的边界算子。这就是“一个 $2$-胞腔的边界是其界圆”这一事实的同调代数版本。

**直觉。** 同调把“未能正合”变成可计算的不变量；链同伦是“连续形变”的代数影子，这正是同伦等价的空间具有相等同调的原因。长正合列是主力工具：它把三个复形之间已知的关系转化为联系它们全部同调群的单一无穷正合梯子，而连接映射承载着几何内涵。

## B 部分 —— 消解与导出函子

<a id="s3"></a>
### 投射消解与内射消解（存在性）

**是什么与为什么。** 要“导出”一个函子，我们必须先把模替换为一个由特别简单的模构成的复形，使该函子能干净地处理。这些简单的模是*投射的*（对于像 $\otimes$ 这样的右正合函子）与*内射的*（对于像 $\mathrm{Hom}$ 这样的左正合函子）。本节定义它们，并证明消解总是存在。

> **定义 —— 自由模。**
> 一个 $R$-模 $F$ 是**自由的**，若它有一组基：$F\cong\bigoplus_{i\in I}R$，即 $R$ 的若干份的直和。每个模都是某自由模的商：把 $M$ 的生成元上的自由模映满到 $M$ 即可。

> **定义 —— 投射模。**
> $P$ 是**投射的**，若对每个满射 $g:B\twoheadrightarrow C$ 与每个映射 $f:P\to C$，都存在一个**提升** $\tilde f:P\to B$ 使 $g\tilde f=f$。等价地，每个满射 $B\twoheadrightarrow P$ 都**分裂**（有右逆）。

> **引理。** 每个自由模都是投射的。

**证明。** 设 $F$ 有基 $(e_i)$，$g:B\twoheadrightarrow C$ 是满射，$f:F\to C$。对每个 $i$ 选 $b_i\in B$ 使 $g(b_i)=f(e_i)$（因 $g$ 满射，可行）。定义 $\tilde f(\sum r_i e_i)=\sum r_i b_i$；因 $(e_i)$ 是一组基，这是 $R$-线性的，且 $g\tilde f(e_i)=g(b_i)=f(e_i)$，故 $g\tilde f=f$ 在一组基上成立，从而处处成立。*（$g$ 的满射性；基的泛性质）* $\;\blacksquare$

> **定义 —— 内射模。**
> $E$ 是**内射的**，若对每个单射 $j:A\hookrightarrow B$ 与每个映射 $f:A\to E$，都存在一个**延拓** $\tilde f:B\to E$ 使 $\tilde f j=f$。（这是把所有箭头反转后的投射性质。）

> **定义 —— 消解。**
> $M$ 的一个**投射消解**是一条正合列
> $$
> \cdots\to P_2\xrightarrow{d_2}P_1\xrightarrow{d_1}P_0\xrightarrow{\varepsilon}M\to 0
> $$
> 其中每个 $P_n$ 都是投射的。一个**内射消解**是一条正合列 $0\to M\xrightarrow{\eta}E^0\xrightarrow{d^0}E^1\to\cdots$，其中每个 $E^n$ 都是内射的。

> **定理（投射消解的存在性）。** 每个 $R$-模 $M$ 都有投射（实则自由）消解。

**证明（显式构造）。**
1. 选一个经 $\varepsilon:P_0\twoheadrightarrow M$ 映满到 $M$ 的自由模 $P_0$——取 $M$ 的一个生成集上的自由模作 $P_0$。由引理 $P_0$ 是投射的。*（每个模都是某自由模的商）*
2. 令 $K_0=\ker\varepsilon$。选一个映满到 $K_0$ 的自由模 $P_1$；与包含映射 $K_0\hookrightarrow P_0$ 复合得 $d_1:P_1\to P_0$，满足 $\mathrm{im}d_1=K_0=\ker\varepsilon$，给出在 $P_0$ 处的正合性。*（同一事实，应用于 $K_0$）*
3. 归纳地，给定 $d_n:P_n\to P_{n-1}$，令 $K_{n}=\ker d_n$ 并选自由模 $P_{n+1}\twoheadrightarrow K_n$；令 $d_{n+1}$ 为复合 $P_{n+1}\twoheadrightarrow K_n\hookrightarrow P_n$。则 $\mathrm{im}d_{n+1}=K_n=\ker d_n$，在 $P_n$ 处正合，且 $d_n d_{n+1}=0$。*（归纳；每个模都是某自由模的商）*
4. 所得复形是一个自由的、从而投射的消解。$\;\blacksquare$

对于 $\mathbb{Z}$ 上（以及任意环上）的内射消解，对偶的存在性定理成立；关键的输入是*每个阿贝尔群都嵌入某个可除群*，而可除阿贝尔群恰是内射 $\mathbb{Z}$-模。

> **定理（$\mathbb{Z}$ 上内射消解存在）。** 每个阿贝尔群 $M$ 都嵌入某内射阿贝尔群，从而有内射消解。

**证明梗概，承重一步给出证明。**
1. *（Baer 判别法，作为工具使用。）* 阿贝尔群 $E$ 是内射的当且仅当每个从理想 $n\mathbb{Z}$ 到 $E$ 的映射都延拓到 $\mathbb{Z}$；可验证这等价于 $E$ 是**可除的**（对每个 $e\in E$ 与 $0\neq n$ 存在 $e'$ 使 $ne'=e$）。*（Baer 判别法特化到 $\mathbb{Z}$）*
2. *嵌入。* 把 $M$ 写成自由群 $\bigoplus\mathbb{Z}$ 的商；该自由群嵌入 $\bigoplus\mathbb{Q}$，后者可除。可除群的商可除，而一个细致的推出（或显式的 $\mathrm{Hom}(\mathbb{Z},\mathbb{Q}/\mathbb{Z})$ 构造）把 $M$ 嵌入一个可除的、从而内射的群 $E^0$。*（可除性在取商下保持；第 1 步）*
3. 对 $E^0/M$ 迭代以构造 $E^1,E^2,\dots$，产生内射消解。$\;\blacksquare$

> **已解例 —— $\mathbb{Z}/6$ 在 $\mathbb{Z}$ 上的自由消解。** 遵循该构造。$P_0=\mathbb{Z}$，$\varepsilon:\mathbb{Z}\twoheadrightarrow\mathbb{Z}/6$ 为约化映射；$K_0=\ker\varepsilon=6\mathbb{Z}\cong\mathbb{Z}$。取 $P_1=\mathbb{Z}$ 经 $1\mapsto6$ 映满到 $6\mathbb{Z}$，故 $d_1=\times6:\mathbb{Z}\to\mathbb{Z}$。现 $\ker d_1=0$，故消解终止：
> $$
> 0\to\mathbb{Z}\xrightarrow{\times6}\mathbb{Z}\xrightarrow{\bmod6}\mathbb{Z}/6\to0.
> $$
> 它的长度为 $1$——这是有限生成阿贝尔群具有长度 $\leq1$ 的自由消解这一普遍现象，也正是 $\mathrm{Tor}_n$ 与 $\mathrm{Ext}^n$ 在 $\mathbb{Z}$ 上对 $n\geq2$ 消失的原因（§s4）。

**陷阱。** 对一般环，投射*并不*等同于自由（例如在 $\mathbb{Z}/6\cong\mathbb{Z}/2\times\mathbb{Z}/3$ 上，因子 $\mathbb{Z}/2$ 投射但不自由）；然而在 $\mathbb{Z}$ 上——更一般地在任何 PID 上——*每个*投射模都是自由的，所以对我们在此用到的一切，这两个概念是重合的。消解的选取极不唯一（不同的生成元、不同的自由覆盖），这恰是 §s4 的无关性定理不可或缺的原因：它保证导出函子看不出这种选取。

<a id="s4"></a>
### 导出函子 —— Tor 与 Ext，它们的定义与消解无关性

**是什么与为什么。** 一个只是*右正合*（保持余核但或许不保持核）的函子 $F$ 会在 SES 的左端丢失信息。**左导出函子** $L_nF$ 恢复这部分丢失的信息。把它应用于 $-\otimes_R N$ 便得 $\mathrm{Tor}$；对偶地，左正合的 $\mathrm{Hom}_R(-,N)$ 的**右导出函子** $R^nF$ 给出 $\mathrm{Ext}$。“导出”一词是字面意义上的：我们取该函子在 $M$ 的一个*消解*（§s3 中构造的简单模复形）上的行为，并逐度数读出所得复形的同调。度数 $0$ 返回原函子；更高的度数是新信息。

> **定义 —— 张量积（我们将要导出的运算）。**
> 对右 $R$-模 $M$ 与左 $R$-模 $N$，**张量积** $M\otimes_R N$ 是由符号 $m\otimes n$ 生成的阿贝尔群，受制于双线性 $(m+m')\otimes n=m\otimes n+m'\otimes n$、$m\otimes(n+n')=m\otimes n+m\otimes n'$ 以及 $mr\otimes n=m\otimes rn$。它是**右正合**的：把 $-\otimes_R N$ 应用于 $A\to B\to C\to0$ 得到正合列 $A\otimes N\to B\otimes N\to C\otimes N\to 0$，但最左边的映射可能不是单射。

*失败例。* 把 $0\to\mathbb{Z}\xrightarrow{\times2}\mathbb{Z}\to\mathbb{Z}/2\to0$ 与 $N=\mathbb{Z}/2$ 做张量积。映射 $\mathbb{Z}\otimes\mathbb{Z}/2\xrightarrow{\times2}\mathbb{Z}\otimes\mathbb{Z}/2$ 变成 $\mathbb{Z}/2\xrightarrow{\times2=0}\mathbb{Z}/2$，即零映射——**不是**单射。这“缺失的核”正是 $\mathrm{Tor}$ 将要检测的。

> **定义 —— 导出函子（左）。**
> 要为右正合函子 $F$ 计算 $L_nF(M)$：取 $M$ 的一个投射消解 $P_\bullet\to M$，删去 $M$ 得 $\cdots\to P_1\to P_0\to0$，施以 $F$ 得复形 $F(P_\bullet)$，并令
> $$
> L_nF(M)=H_n\big(F(P_\bullet)\big).
> $$
> 定义 $\mathrm{Tor}_n^R(M,N)=L_n(-\otimes_R N)(M)=H_n(P_\bullet\otimes_R N)$。

> **定义 —— 导出函子（右）与 Ext。**
> 对偶地，对左正合的 $F$，把 $F$ 应用于一个内射消解 $M\to E^\bullet$ 并令 $R^nF(M)=H^n(F(E^\bullet))$。定义 $\mathrm{Ext}^n_R(M,N)=R^n\mathrm{Hom}_R(-,N)(M)=H^n(\mathrm{Hom}_R(P_\bullet,N))$，在第一个变量中使用 $M$ 的投射消解（两种配方一致）。

> **定理（与消解无关）。** $L_nF(M)$ 在典范同构意义下不依赖于所选的投射消解。

**证明。** 它依赖于*比较定理*。

1. **比较定理。** 给定投射消解 $P_\bullet\to M$ 与 $Q_\bullet\to M'$ 以及映射 $\phi:M\to M'$，存在一个提升 $\phi$ 的链映射 $\tilde\phi:P_\bullet\to Q_\bullet$，在链同伦意义下唯一。*证明：* 利用 $P_n$ 的投射性，通过满射 $Q_n\twoheadrightarrow\ker(Q_{n-1}\to Q_{n-2})$ 提升，归纳地构造 $\tilde\phi_n$；至于在同伦意义下的唯一性，把同一提升应用于两个提升之差，其差落在边缘链中。*（§s3 的投射提升性质）*
2. 取 $M'=M$，$\phi=\mathrm{id}$，以及两个消解 $P_\bullet,Q_\bullet$。比较定理给出提升 $\mathrm{id}$ 的链映射 $\tilde\phi:P\to Q$ 与 $\tilde\psi:Q\to P$。则 $\tilde\psi\tilde\phi$ 与 $\mathrm{id}_P$ 都提升 $\mathrm{id}_M$，故由唯一性它们链同伦；同理 $\tilde\phi\tilde\psi\simeq\mathrm{id}_Q$。*（比较定理）*
3. 施以 $F$。链同伦 $f-g=\partial h+h\partial$ 在可加函子 $F$ 之下映为 $F(f)-F(g)=F(\partial)F(h)+F(h)F(\partial)$——仍是链同伦。从而 $F(\tilde\phi)$ 与 $F(\tilde\psi)$ 在同调上互逆（由 §s2 同伦不变性），给出*典范*同构 $H_n(F(P))\cong H_n(F(Q))$。*（$F$ 的可加性；§s2 同伦不变性）* $\;\blacksquare$

> **计算 —— $\mathrm{Tor}_1^{\mathbb{Z}}(\mathbb{Z}/2,\mathbb{Z}/2)$。**
> $\mathbb{Z}/2$ 的投射（自由）消解：$0\to\mathbb{Z}\xrightarrow{\times2}\mathbb{Z}\to0$（然后 $\to\mathbb{Z}/2$）。与 $\mathbb{Z}/2$ 做张量积并删去增广：$0\to\mathbb{Z}/2\xrightarrow{\times2=0}\mathbb{Z}/2\to0$。同调：$H_0=\mathbb{Z}/2$（$0$ 的余核）$=\mathrm{Tor}_0=\mathbb{Z}/2\otimes\mathbb{Z}/2$；$H_1=\ker(0)/\mathrm{im}=\mathbb{Z}/2$。故 $\mathrm{Tor}_1^{\mathbb{Z}}(\mathbb{Z}/2,\mathbb{Z}/2)=\mathbb{Z}/2$——恰是失败例中那“缺失的核”。

> **计算 —— $\mathrm{Ext}^1_{\mathbb{Z}}(\mathbb{Z}/2,\mathbb{Z})$。**
> 把 $\mathrm{Hom}_{\mathbb{Z}}(-,\mathbb{Z})$ 应用于 $0\to\mathbb{Z}\xrightarrow{\times2}\mathbb{Z}\to0$：得 $0\to\mathbb{Z}\xrightarrow{\times2}\mathbb{Z}\to0$（因为 $\mathrm{Hom}(\mathbb{Z},\mathbb{Z})=\mathbb{Z}$，而 $\times2$ 的对偶是 $\times2$）。上同调：$H^0=\ker(\times2)=0=\mathrm{Ext}^0=\mathrm{Hom}(\mathbb{Z}/2,\mathbb{Z})$；$H^1=\mathbb{Z}/2\mathbb{Z}=\mathrm{Ext}^1$。故 $\mathrm{Ext}^1_{\mathbb{Z}}(\mathbb{Z}/2,\mathbb{Z})=\mathbb{Z}/2$。

**关键事实（每条都可如上证明）。** $\mathrm{Tor}_0=\otimes$，$\mathrm{Ext}^0=\mathrm{Hom}$；在 $\mathbb{Z}$ 上，对 $n\geq2$ 有 $\mathrm{Tor}_n=\mathrm{Ext}^n=0$（因为自由阿贝尔群的每个子群都是自由的，故消解长度为 $1$）；任一变量中的 SES 都产生一条 $\mathrm{Tor}$ 或 $\mathrm{Ext}$ 的**长正合列**（把 §s2 的长正合列应用于消解复形）。

> **定理（$\mathrm{Tor}$ 的长正合列）。** 右 $R$-模的短正合列 $0\to A'\to A\to A''\to0$ 与一个固定的左模 $N$ 产生一条长正合列
> $$
> \cdots\to\mathrm{Tor}_1(A',N)\to\mathrm{Tor}_1(A,N)\to\mathrm{Tor}_1(A'',N)\to A'\otimes N\to A\otimes N\to A''\otimes N\to0.
> $$

**推导。**
1. 选投射消解 $P'_\bullet\to A'$ 与 $P''_\bullet\to A''$。**马蹄引理**（标准结果；不加证明地陈述）断言：给定 SES $0\to A'\to A\to A''\to0$ 两个外项 $A',A''$ 的投射消解，便可拼出中间项的一个投射消解 $P_\bullet\to A$，其中 $P_n=P'_n\oplus P''_n$，并嵌入复形的逐度数分裂 SES $0\to P'_\bullet\to P_\bullet\to P''_\bullet\to0$。*（马蹄引理；因 $P''_n$ 投射而逐度数分裂）*
2. 与 $N$ 做张量积。由于复形的 SES 在每个度数上分裂，$0\to P'_\bullet\otimes N\to P_\bullet\otimes N\to P''_\bullet\otimes N\to0$ 仍是短正合的。*（逐度数分裂的 SES 在任意可加函子下存活）*
3. 应用 §s2 的长正合同调列。其同调群按定义即 $\mathrm{Tor}_n$，而右端 $\mathrm{Tor}_0=\otimes$ 凭 $\otimes$ 的右正合性以 $\to A''\otimes N\to0$ 收尾。*（§s2 长正合列；$\mathrm{Tor}_0=\otimes$）* $\;\blacksquare$

> **定理（$\mathrm{Tor}$ 的平衡性）。** $\mathrm{Tor}_n^R(M,N)$ 可通过消解*任一*变量来计算：$H_n(P^M_\bullet\otimes N)\cong H_n(M\otimes Q^N_\bullet)$，其中 $P^M_\bullet\to M$ 与 $Q^N_\bullet\to N$ 是投射消解。

**推导。** 构造双复形 $P^M_\bullet\otimes Q^N_\bullet$，其中 $C_{p,q}=P^M_p\otimes Q^N_q$ 并带两个张量化的微分。运行 §s9 的两个双复形谱序列。由于每个 $P^M_p$ 投射（平坦），把消解 $Q^N_\bullet\to N$ 与 $P^M_p$ 做张量积仍保持正合，故一个谱序列坍缩为 $H_n(P^M_\bullet\otimes N)$；由对称性另一个坍缩为 $H_n(M\otimes Q^N_\bullet)$。两者都收敛到 $H_n(\mathrm{Tot})$，故二者同构。*（§s9 的退化双复形谱序列；投射模的平坦性）* $\;\blacksquare$

> **诠释 —— $\mathrm{Ext}^1$ 分类扩张。** $A$ 被 $B$ 的一个**扩张**是 SES $0\to B\to E\to A\to0$；两个扩张*等价*，若它们由一个固定 $B$ 与 $A$ 的中间项同构相联系。等价类的集合与 $\mathrm{Ext}^1_R(A,B)$ 之间有自然双射，其中**分裂**扩张 $E=A\oplus B$ 对应于 $0$。*例：* $\mathrm{Ext}^1_{\mathbb{Z}}(\mathbb{Z}/2,\mathbb{Z})=\mathbb{Z}/2$ 有两个类——分裂扩张 $0\to\mathbb{Z}\to\mathbb{Z}\oplus\mathbb{Z}/2\to\mathbb{Z}/2\to0$（类 $0$）与非分裂扩张 $0\to\mathbb{Z}\xrightarrow{\times2}\mathbb{Z}\to\mathbb{Z}/2\to0$（非零类）。$\mathrm{Ext}^1$ 的非消失恰是真正扭曲的扩张之存在。

<a id="s5"></a>
### 万有系数定理与 Künneth 公式（导出）

**是什么与为什么。** 在拓扑中人们先计算整系数同调，然后想要其他系数下的同调或上同调，以及乘积空间的同调。两个答案都由 $\mathrm{Tor}$ 与 $\mathrm{Ext}$ 支配。我们将两者都导出。我们使用一个由**自由**阿贝尔群构成的链复形 $C_\bullet$（奇异链的情形），正是这一点使下面的分裂成为可能。

> **万有系数定理（同调）。** 设 $C_\bullet$ 是自由阿贝尔群的链复形，$G$ 是阿贝尔群。存在一条关于 $G$ 自然的短正合列
> $$
> 0\to H_n(C)\otimes G\to H_n(C\otimes G)\to \mathrm{Tor}_1^{\mathbb{Z}}(H_{n-1}(C),G)\to 0,
> $$
> 且它（非自然地）分裂，故 $H_n(C\otimes G)\cong (H_n(C)\otimes G)\oplus\mathrm{Tor}_1^{\mathbb{Z}}(H_{n-1}(C),G)$。

**推导。**
1. 设 $Z_n,B_n\subseteq C_n$ 为闭链与边缘链。由于 $C_n$ 是自由阿贝尔群而 $B_{n-1}\subseteq C_{n-1}$ 是自由阿贝尔群的子群，$B_{n-1}$ 是自由的。因此 SES $0\to Z_n\to C_n\xrightarrow{\partial}B_{n-1}\to0$ **分裂**（$B_{n-1}$ 自由 $\Rightarrow$ 投射 $\Rightarrow$ 该满射分裂）。*（自由阿贝尔群的子群是自由的；§s3 投射性）*
2. 把 $Z_\bullet$ 与 $B_\bullet$ 视为带**零**微分的链复形。第 1 步的分裂 SES 是链复形的 SES $0\to Z_\bullet\to C_\bullet\xrightarrow{\partial} B_{\bullet-1}\to0$，其中 $B_{\bullet-1}$ 是 $B$ 的移位。*（逐度数分裂）*
3. 与 $G$ 做张量积。由于每一项都自由（从而 SES 分裂），张量化的序列 $0\to Z_\bullet\otimes G\to C_\bullet\otimes G\to B_{\bullet-1}\otimes G\to0$ 仍是短正合的。*（分裂 SES 在施以任意可加函子后仍分裂，从而正合）*
4. 它的长正合同调列（§s2）的连接映射等于包含映射 $B_n\hookrightarrow Z_n$ 与 $G$ 的张量积，即 $i\otimes\mathrm{id}_G:B_n\otimes G\to Z_n\otimes G$。（这一辨识恰是把 §s1 的蛇引理连接映射应用于第 3 步的分裂 SES：由于 $Z_\bullet$ 与 $B_\bullet$ 带零微分，张量后唯一残存的微分就是边缘到闭链的包含 $i:B_n\hookrightarrow Z_n$，故 $\partial_*=i\otimes\mathrm{id}_G$。）拼接对每个 $n$ 给出
> $$
> 0\to\mathrm{coker}(i\otimes\mathrm{id})_n\to H_n(C\otimes G)\to\ker(i\otimes\mathrm{id})_{n-1}\to0.
> $$
*（长正合列；辨识连接映射）*
5. 现使用 $H_n(C)$ 的自由消解 $0\to B_n\xrightarrow{i}Z_n\to H_n(C)\to0$（因 $B_n,Z_n$ 自由，它是由自由群构成的消解）。与 $G$ 做张量积并取同调：由 $\mathrm{Tor}$ 从这一长度为一的自由消解所得的定义，$\mathrm{coker}(i\otimes\mathrm{id})=H_n(C)\otimes G$ 且 $\ker(i\otimes\mathrm{id})=\mathrm{Tor}_1^{\mathbb{Z}}(H_n(C),G)$。*（$\otimes$ 作为 $\mathrm{Tor}_0$ 与 $\mathrm{Tor}_1$ 的定义，§s4）*
6. 代入第 4 步即给出所述 SES。**分裂：** 由于 $Z_n$ 是 $C_n$ 的直和因子（第 1 步），选一个收缩 $C_n\to Z_n$；它诱导 $H_n(C\otimes G)\to H_n(C)\otimes G$，分裂第一个映射。$\;\blacksquare$

> **万有系数定理（上同调）。** 当 $C_\bullet$ 自由时，存在一条分裂 SES
> $$
> 0\to\mathrm{Ext}^1_{\mathbb{Z}}(H_{n-1}(C),G)\to H^n(\mathrm{Hom}(C,G))\to\mathrm{Hom}(H_n(C),G)\to0.
> $$
> *推导：* 与上面相同，只是把 $\otimes G$ 换成 $\mathrm{Hom}(-,G)$；现在连接映射从同一长度为一的自由消解产生 $\mathrm{Hom}=\mathrm{Ext}^0$ 与 $\mathrm{Ext}^1$。*（对偶化第 1–6 步）*

> **Künneth 公式。** 对阿贝尔群的自由链复形 $C_\bullet,D_\bullet$，存在一条分裂 SES
> $$
> 0\to\bigoplus_{i+j=n}H_i(C)\otimes H_j(D)\to H_n(C\otimes D)\to\bigoplus_{i+j=n-1}\mathrm{Tor}_1^{\mathbb{Z}}(H_i(C),H_j(D))\to0.
> $$

**推导。**
1. 如 UCT 第 1 步，分裂每个 $0\to Z_i(C)\to C_i\to B_{i-1}(C)\to0$，使 $C_\bullet$ 分解；把 $C_\bullet$ 视为由带零微分的自由复形 $Z_\bullet$ 与 $B_\bullet$ 构造而成。*（自由阿贝尔群的子群是自由的；分裂）*
2. SES $0\to Z_\bullet\to C_\bullet\to B_{\bullet-1}\to0$ 在 $\mathbb{Z}$ 上与*复形* $D_\bullet$ 做张量积后仍是短正合的（各项自由）。*（分裂 SES 在 $\otimes$ 下存活）*
3. 取长正合同调列。利用 $H_*(Z_\bullet\otimes D)=\bigoplus Z_i(C)\otimes H_j(D)$（对 $B$ 亦然，零微分使同调成为逐项张量），连接映射又是 $i\otimes\mathrm{id}$，即包含 $B_i\hookrightarrow Z_i$。*（零微分复形的同调；连接映射的辨识）*
4. 由长度为一的自由消解 $0\to B_i\to Z_i\to H_i(C)\to0$（§s4），$i\otimes\mathrm{id}_{H_j(D)}$ 的余核与核分别是 $H_i(C)\otimes H_j(D)$ 与 $\mathrm{Tor}_1(H_i(C),H_j(D))$。对 $i+j=n$ 与 $i+j=n-1$ 求和即给出该公式；分裂与之前一样来自收缩。$\;\blacksquare$

> **已解例 —— $\mathbb{RP}^2$ 带系数的同调。** 整系数同调：$H_0=\mathbb{Z},\ H_1=\mathbb{Z}/2,\ H_2=0$。取 $G=\mathbb{Z}/2$：UCT 给出 $H_2(\mathbb{RP}^2;\mathbb{Z}/2)\cong(H_2\otimes\mathbb{Z}/2)\oplus\mathrm{Tor}_1(H_1,\mathbb{Z}/2)=0\oplus\mathrm{Tor}_1(\mathbb{Z}/2,\mathbb{Z}/2)=\mathbb{Z}/2$。所以尽管 $H_2(\mathbb{RP}^2;\mathbb{Z})=0$，度数 $2$ 处的模-2 同调却非零——$\mathrm{Tor}$ 项*创生*了一个类。这就是 $H_*(\mathbb{RP}^2;\mathbb{Z}/2)$ 中著名的“额外的” $\mathbb{Z}/2$。

> **已解例 —— 经 Ext 项计算 $\mathbb{RP}^2$ 在 $\mathbb{Z}$ 上的上同调。** 上同调 UCT 给出 $H^n(\mathbb{RP}^2;\mathbb{Z})\cong\mathrm{Hom}(H_n,\mathbb{Z})\oplus\mathrm{Ext}^1(H_{n-1},\mathbb{Z})$。在度数 $2$：$\mathrm{Hom}(H_2,\mathbb{Z})=\mathrm{Hom}(0,\mathbb{Z})=0$ 而 $\mathrm{Ext}^1(H_1,\mathbb{Z})=\mathrm{Ext}^1(\mathbb{Z}/2,\mathbb{Z})=\mathbb{Z}/2$，故 $H^2(\mathbb{RP}^2;\mathbb{Z})=\mathbb{Z}/2$。在度数 $1$：$\mathrm{Hom}(\mathbb{Z}/2,\mathbb{Z})=0$ 而 $\mathrm{Ext}^1(\mathbb{Z},\mathbb{Z})=0$，故 $H^1=0$。上同调把同调的挠*上移*一个度数——这是 $\mathrm{Ext}$ 项的标志。

> **叉积与 Künneth 映射。** Künneth SES 中的第一个映射 $H_i(C)\otimes H_j(D)\to H_{i+j}(C\otimes D)$ 是**同调叉积** $\alpha\otimes\beta\mapsto\alpha\times\beta$，把一对闭链类送到它们张量的类。当所有群都自由时（例如系数在域 $k$ 中），$\mathrm{Tor}$ 项消失，Künneth 成为干净的同构 $H_n(C\otimes D)\cong\bigoplus_{i+j=n}H_i(C)\otimes H_j(D)$。*域上之例：* $H_*(T^2;k)=H_*(S^1;k)\otimes H_*(S^1;k)$，给出环面的 Betti 数 $1,2,1$——两个独立的环路与一个 $2$-胞腔。

## C 部分 —— 范畴语言与双复形

<a id="s6"></a>
### 范畴、函子、自然变换与阿贝尔范畴（一个实用引论）

**是什么与为什么。** 以上所有内容都用到了诸如“自然地”与“函子”这样的措辞。范畴论使它们精确化，并让蛇引理/五引理与导出函子得以在超出模的情形中（层、复形自身）安身。我们只给出够用的部分。

> **定义 —— 范畴。**
> 一个**范畴** $\mathcal{C}$ 由一组**对象**构成；对每个有序对 $(X,Y)$ 有一个**态射**集 $\mathrm{Hom}(X,Y)$；一个满足结合律的复合 $\mathrm{Hom}(Y,Z)\times\mathrm{Hom}(X,Y)\to\mathrm{Hom}(X,Z)$，$(g,f)\mapsto g\circ f$；以及对每个 $X$ 一个恒等态射 $\mathrm{id}_X$，满足 $\mathrm{id}_Y\circ f=f=f\circ\mathrm{id}_X$。*例：* $\mathbf{Set}$（集合与函数），$R\text{-}\mathbf{Mod}$（$R$-模与同态），$\mathbf{Top}$（空间与连续映射）。

> **定义 —— 函子。**
> 一个**函子** $F:\mathcal{C}\to\mathcal{D}$ 给每个对象 $X$ 指派一个对象 $F(X)$，给每个态射 $f:X\to Y$ 指派一个态射 $F(f):F(X)\to F(Y)$，满足 $F(g\circ f)=F(g)\circ F(f)$ 与 $F(\mathrm{id}_X)=\mathrm{id}_{F(X)}$。**反变**函子反转箭头：$F(f):F(Y)\to F(X)$。*例：* 同调 $H_n:\mathbf{Top}\to\mathbf{Ab}$ 是一个（协变）函子；$\mathrm{Hom}_R(-,N)$ 是反变的。

> **定义 —— 自然变换。**
> 给定函子 $F,G:\mathcal{C}\to\mathcal{D}$，一个**自然变换** $\eta:F\Rightarrow G$ 给每个对象 $X$ 指派一个态射 $\eta_X:F(X)\to G(X)$，使得对每个 $f:X\to Y$ 方形交换：$G(f)\circ\eta_X=\eta_Y\circ F(f)$。UCT 中的“自然”恰指此意。若每个 $\eta_X$ 都是同构，则 $\eta$ 是一个**自然同构**。

*已解例。* 映射 $\eta_M:M\to M^{**}=\mathrm{Hom}(\mathrm{Hom}(M,k),k)$，$\eta_M(m)(\phi)=\phi(m)$，是从恒等函子到向量空间上双对偶函子的一个自然变换；方形交换是因为对线性的 $f:M\to N$，由直接代入有 $f^{**}\circ\eta_M=\eta_N\circ f$。在有限维空间上它是一个自然同构。

> **定义 —— 阿贝尔范畴。**
> 一个**阿贝尔范畴**是这样一个范畴：（i）$\mathrm{Hom}$-集是阿贝尔群且复合是双线性的，（ii）有一个零对象且所有有限直和存在，（iii）每个态射都有核与余核，（iv）每个单态射都是其余核的核，且每个满态射都是其核的余核。$R\text{-}\mathbf{Mod}$ 是原型；阿贝尔群的层构成另一例。

> **定理（Freyd–Mitchell 嵌入，陈述）。** 每个小阿贝尔范畴都精确地嵌入为某环 $R$ 上 $R\text{-}\mathbf{Mod}$ 的一个全子范畴。

**推论（为何图追踪在任意阿贝尔范畴中合法）。** 由于该嵌入正合且全，任何在 $R\text{-}\mathbf{Mod}$ 中靠追踪*元素*可证的命题——蛇引理、五引理、长正合列——在每个阿贝尔范畴中都成立。因此我们可以“假装对象有元素”。*（Freyd–Mitchell）*

> **定义 —— 伴随函子。**
> 函子 $F:\mathcal{C}\to\mathcal{D}$ 与 $G:\mathcal{D}\to\mathcal{C}$ 构成一个**伴随对**（$F$ 左伴随于 $G$），若对一切 $X,Y$ 有自然同构
> $$
> \mathrm{Hom}_{\mathcal{D}}(F(X),Y)\cong\mathrm{Hom}_{\mathcal{C}}(X,G(Y)).
> $$
> 其原型是**张量–Hom 伴随** $\mathrm{Hom}(M\otimes_R N,\,P)\cong\mathrm{Hom}\big(M,\mathrm{Hom}_R(N,P)\big)$。

> **为何正合性行为是被迫的。** 左伴随保持一切*余极限*（特别是余核），因而是**右正合**的——这正是 $\otimes$（左伴随）右正合并需要左导出函子 $\mathrm{Tor}$ 的原因。右伴随保持一切*极限*（核），因而是**左正合**的——这就是 $\mathrm{Hom}(-,N)$ 与 $(-)^G$ 左正合并需要右导出函子 $\mathrm{Ext}$ 与 $H^*(G;-)$ 的原因。整个 $\mathrm{Tor}$/$\mathrm{Ext}$ 二分法都是这一条伴随事实的影子。*（伴随保持（余）极限）*

**演示 —— 左伴随 $F$ 是右正合的。**
1. 右正合性意味着：应用于 $A\to B\to C\to0$，结果 $F(A)\to F(B)\to F(C)\to0$ 正合，即 $F(C)$ 是 $F(A)\to F(B)$ 的余核。*（右正合的定义）*
2. 余核是一个余极限（$A\to B$ 与 $0$ 的余等化子）。*（余核 = 余极限）*
3. 左伴随保持余极限：$\mathrm{Hom}(F(\mathrm{colim}),Y)\cong\mathrm{Hom}(\mathrm{colim},G(Y))\cong\lim\mathrm{Hom}(-,G(Y))\cong\lim\mathrm{Hom}(F(-),Y)\cong\mathrm{Hom}(\mathrm{colim}F(-),Y)$，然后 Yoneda 辨识出 $F(\mathrm{colim})=\mathrm{colim}F(-)$。所以 $F$ 把余核送到余核，这恰是右正合性。*（伴随；反变 $\mathrm{Hom}$ 把余极限变为极限；Yoneda）* $\;\blacksquare$

**陷阱。** 在一般范畴中，一个态射可以既是单态射又是满态射却不是同构（例如环范畴中的 $\mathbb{Z}\hookrightarrow\mathbb{Q}$）；阿贝尔范畴恰是“单 + 满 $\Rightarrow$ 同构”成立的情形，而这正是图引理悄然使用的。

<a id="s7"></a>
### 双复形与全复形

**是什么与为什么。** 许多构造天然地由*两个*整数（行与列）来标号。把它们打包为一个双复形，再坍缩为单一的**全复形**，是通往谱序列的技术桥梁。

> **定义 —— 双复形。**
> 一个**双复形** $C_{\bullet\bullet}=(C_{p,q})$ 是一个模的网格，带水平映射 $d^h:C_{p,q}\to C_{p-1,q}$ 与竖直映射 $d^v:C_{p,q}\to C_{p,q-1}$，满足
> $$
> d^h d^h=0,\qquad d^v d^v=0,\qquad d^h d^v + d^v d^h = 0.
> $$
> （符号约定 $d^hd^v+d^vd^h=0$——反交换——正是使全微分平方为零的原因；某些作者改用交换的方形并插入符号 $(-1)^p$。）

> **定义 —— 全复形。**
> **全复形** $\mathrm{Tot}(C)_\bullet$ 满足
> $$
> \mathrm{Tot}(C)_n=\bigoplus_{p+q=n}C_{p,q},\qquad D=d^h+d^v.
> $$

> **引理。** $D\circ D=0$，故 $\mathrm{Tot}(C)$ 是一个链复形。

**证明。**
1. 展开 $D^2=(d^h+d^v)(d^h+d^v)=d^hd^h+d^hd^v+d^vd^h+d^vd^v$。*（分配律）*
2. 首项与末项消失（$d^hd^h=0$，$d^vd^v=0$）。*（双复形公理）*
3. 中间两项由反交换公理 $d^hd^v+d^vd^h=0$。*（双复形公理）*
4. 从而 $D^2=0$。$\;\blacksquare$

*已解例。* 取只有一非零行的双复形 $\cdots\to C_{1,0}\to C_{0,0}$。则 $\mathrm{Tot}$ 就是那一行，而 $H_n(\mathrm{Tot})$ 是该行的普通同调。更有趣地，一个 $2\times2$ 方形 $C_{1,1}\to C_{1,0}$，$C_{1,1}\to C_{0,1}$ 等，全化为 $C_{1,1}\xrightarrow{(d^h,d^v)}C_{1,0}\oplus C_{0,1}\xrightarrow{d^v - d^h}C_{0,0}$，其中间同调恰是 §s9 中一个 $2$-页谱序列将要计算的对象。

> **已解例 —— 迭代同调可能与全同调不一致。** 考虑 $2\times2$ 第一象限双复形（位于 $(0,0),(1,0),(0,1),(1,1)$ 的项）全等于 $\mathbb{Z}$，两个非零水平映射与两个非零竖直映射都是恒等映射，符号安排得使方形反交换。先取竖直同调：每列 $\mathbb{Z}\xrightarrow{\mathrm{id}}\mathbb{Z}$ 正合，故处处 $H^v=0$，从而“$H^h(H^v)=0$”。现直接计算 $H_*(\mathrm{Tot})$：$\mathrm{Tot}_2=C_{1,1}=\mathbb{Z}$，$\mathrm{Tot}_1=C_{1,0}\oplus C_{0,1}=\mathbb{Z}^2$，$\mathrm{Tot}_0=C_{0,0}=\mathbb{Z}$，其中 $D_2=(\mathrm{id},\mathrm{id})$ 单射，$D_1=(\mathrm{id},-\mathrm{id})$ 映满到 $\mathbb{Z}$ 且核为反对角线 $=\mathrm{im}D_2$。故 $H_*(\mathrm{Tot})=0$ 也成立——此处二者一致，因为该复形无圈。把一个映射扰动为 $\times2$，则两个迭代同调与全同调将出现差异，差异由 $E^2$ 页上一个非零 $d^2$ 记录（§s9）。这正是谱序列“修正”朴素迭代同调的精确意义。

**取同调的两种方式。** 人们可以先沿列取同调（用 $d^v$），再沿行取（用诱导的 $d^h$），或反过来。这两个答案通常彼此不同、也与 $H_*(\mathrm{Tot})$ 不同。谱序列是把这些“迭代同调”与 $H_*(\mathrm{Tot})$ 精确联系起来的机器：每一个都从其 $E^2$ 页上的某个迭代同调出发，并收敛到 $H_*(\mathrm{Tot})$，故微分恰好度量这一差距。

## D 部分 —— 谱序列

<a id="s8"></a>
### 谱序列 —— 页、微分与收敛（具体化的定义）

**是什么与为什么。** 一个谱序列是一列二维网格（“页”），每一页通过取同调由前一页得到，旨在以逐次逼近计算一个困难的同调。我们给出朴素的定义，然后把每个词都具体化。

> **定义 —— （同调型）谱序列。**
> 一个**谱序列**（$R$-模的，自第 $r_0$ 页开始）是一族
> $$
> \big\{E^r_{p,q},\ d^r:E^r_{p,q}\to E^r_{p-r,\,q+r-1}\big\}_{r\geq r_0}
> $$
> 使得每个 $d^r$ 满足 $d^r\circ d^r=0$，连同同构
> $$
> E^{r+1}_{p,q}\cong H_{p,q}(E^r)=\frac{\ker\big(d^r:E^r_{p,q}\to E^r_{p-r,q+r-1}\big)}{\mathrm{im}\big(d^r:E^r_{p+r,q-r+1}\to E^r_{p,q}\big)}.
> $$
> 因此每一页都是前一页关于其微分 $d^r$ 的同调。$d^r$ 的双度数是 $(-r,\,r-1)$：随 $r$ 增大，微分变得“更长更平”。

> **定义 —— 极限页 $E^\infty$。**
> 固定 $(p,q)$。随 $r$ 增大，$E^r_{p,q}$ 是前者的一个子商。在**第一象限**情形（除非 $p,q\geq0$ 否则 $E^r_{p,q}=0$），对每个固定的 $(p,q)$，进出的微分最终都指向象限之外，故对一切大的 $r$，位置 $(p,q)$ 进出的 $d^r=0$。于是 $E^{r}_{p,q}=E^{r+1}_{p,q}=\cdots$ 稳定；其公共值即 $E^\infty_{p,q}$。

> **定义 —— 收敛。**
> 谱序列**收敛**到一个分次模 $H_\bullet$（记作 $E^r_{p,q}\Rightarrow H_{p+q}$），若 $H_n$ 带有一个过滤 $0=F_{-1}\subseteq F_0\subseteq\cdots\subseteq F_n=H_n$，且有同构
> $$
> E^\infty_{p,q}\cong F_p H_{p+q}/F_{p-1}H_{p+q}.
> $$
> 用语言说：极限页是答案上某过滤的**相伴分次**。从反对角线 $p+q=n$ 上的 $E^\infty_{p,q}$ 恢复 $H_n$ 是一个**扩张问题**（必须把各部件重新拼装起来），它可能有若干个解。

**具体阅读指南。**
1. 画出网格，$p$ 横向、$q$ 竖向。$E^2$ 页通常有一个可解释的项（例如 §s10 中的 $H_p(\text{底};H_q(\text{纤维}))$）。
2. $d^2$ 向左两格、向上一格：$(p,q)\to(p-2,q+1)$。取同调得到 $E^3$。
3. $d^3$ 向左三格、向上两格；如此等等。一直进行到微分消亡为止。
4. 沿反对角线 $p+q=n$ 读出 $E^\infty$；解出 $H_n$ 的扩张问题。

> **已解例 —— 两列谱序列坍缩为长正合列。** 设除 $p=0$ 与 $p=1$ 两列外 $E^2_{p,q}=0$。则 $d^2:(p,q)\to(p-2,q+1)$ 总落在某个零列中，故 $d^2=0$ 且 $E^2=E^\infty$。$H_n$ 上的过滤只有两步，给出 SES $0\to E^\infty_{0,n}\to H_n\to E^\infty_{1,n-1}\to0$。把它们在所有 $n$ 上拼接产生一条长正合列——表明 LES 是最简单的非平凡谱序列。

> **已解例 —— 解一个扩张问题。** 设沿反对角线 $p+q=2$，极限页给出 $E^\infty_{0,2}=\mathbb{Z}/2$ 与 $E^\infty_{2,0}=\mathbb{Z}/2$，该对角线上其余项全为零。收敛性提供一个过滤 $0\subseteq F_0H_2\subseteq F_2H_2=H_2$，其中 $F_0H_2=E^\infty_{0,2}=\mathbb{Z}/2$ 而 $H_2/F_0H_2=E^\infty_{2,0}=\mathbb{Z}/2$。于是 $H_2$ 是一个扩张 $0\to\mathbb{Z}/2\to H_2\to\mathbb{Z}/2\to0$，由（§s4）$\mathrm{Ext}^1(\mathbb{Z}/2,\mathbb{Z}/2)=\mathbb{Z}/2$ 分类：要么 $H_2=\mathbb{Z}/2\oplus\mathbb{Z}/2$，要么 $H_2=\mathbb{Z}/4$。谱序列本身无法判定；这就是**扩张问题**，而解决它（此处即知道环结构或一个 Bockstein）是此技术的代价。

**陷阱。** $E^\infty$ 只给出 $H_n$ 的*相伴分次*，而非 $H_n$ 本身。若各部件例如是 $\mathbb{Z}/2$ 与 $\mathbb{Z}/2$，答案可能是 $\mathbb{Z}/4$ 或 $\mathbb{Z}/2\oplus\mathbb{Z}/2$；解决这一点需要额外输入。此外“收敛”要求过滤是穷尽的且有界的——在第一象限情形是自动的，一般情形则不然。第二个常见错误是忘记双度数：在同调型标号下 $d^r$ 的双度数是 $(-r,r-1)$，但在上同调型（上）标号下是 $(r,1-r)$——第二页上同调微分 $d_2:E_2^{p,q}\to E_2^{p+2,q-1}$ 向*右*两格、向*下*一格，如 §s11 的 LHS 五项序列所示。

<a id="s9"></a>
### 过滤复形与双复形的谱序列（导出）

**是什么与为什么。** 谱序列并非凭空而来——每一个都来自一个*过滤复形*。我们将其构造出来，并证明各页是逐次同调。双复形谱序列则是过滤按列进行的特例。

> **定义 —— 过滤复形。**
> 链复形 $(C_\bullet,D)$ 的一个**过滤**是一族嵌套的子复形 $\cdots\subseteq F_{p-1}C\subseteq F_pC\subseteq F_{p+1}C\subseteq\cdots$，满足 $D(F_pC)\subseteq F_pC$。它是**有界的**，若对每个 $n$ 存在 $s<t$ 使 $F_sC_n=0$ 且 $F_tC_n=C_n$。

> **定理（过滤复形的谱序列）。** $C_\bullet$ 上的一个有界过滤确定一个谱序列，满足
> $$
> E^0_{p,q}=F_pC_{p+q}/F_{p-1}C_{p+q},\qquad E^1_{p,q}=H_{p+q}\big(F_pC/F_{p-1}C\big),
> $$
> 它收敛到 $H_{p+q}(C)$，其过滤由 $F_\bullet$ 诱导。

**推导（正合偶构造）。**
1. *建立群。* 对每个 $p$，包含 $F_{p-1}C\hookrightarrow F_pC$ 给出复形的 SES $0\to F_{p-1}C\to F_pC\to F_pC/F_{p-1}C\to0$，从而（由 §s2）给出同调的长正合列。定义
> $$
> A_{p,q}=H_{p+q}(F_pC),\qquad E^1_{p,q}=H_{p+q}(F_pC/F_{p-1}C).
> $$
*（复形 SES 的长正合列，§s2）*
2. *正合偶。* 这些长正合列装配为映射的单一图：$i:A_{p-1}\to A_p$（由包含诱导）、$j:A_p\to E^1$（商映射）、$k:E^1\to A_{p-1}$（连接映射），构成一个**正合偶**：在 $A,E,A$ 各处正合。*（每条 LES 的正合性）*
3. *导出该偶。* 定义 $d^1=j\circ k:E^1\to E^1$。则 $d^1d^1=jk\,jk=j(kj)k=0$，因为由在 $A$ 处的正合性 $kj=0$。令 $E^2=\ker d^1/\mathrm{im}d^1$ 并把 $A$ 替换为 $iA$；可验证新的三元组 $(iA,E^2,\dots)$ 又是一个正合偶——即**导出偶**。*（在 $A$ 处正合给出 $kj=0$）*
4. *迭代。* 第 $r$ 个导出偶有 $E^r$ 与双度数 $(-r,r-1)$ 的微分 $d^r=j^{(r)}k^{(r)}$，且由构造 $E^{r+1}=H(E^r,d^r)$。这恰是一个谱序列的数据（§s8）。*（归纳：把该偶导出 $r$ 次）*
5. *收敛。* 有界性使每个 $H_n(C)$ 上的过滤有限，故 $E^r$ 稳定到 $E^\infty$，而追踪各导出偶辨识出 $E^\infty_{p,q}=F_pH_{p+q}(C)/F_{p-1}H_{p+q}(C)$。*（有界过滤 $\Rightarrow$ 稳定，§s8）* $\;\blacksquare$

> **推论（双复形谱序列）。** 一个第一象限双复形 $C_{\bullet\bullet}$ 给出**两个**收敛到 $H_*(\mathrm{Tot}\,C)$ 的谱序列：
> $$
> {}^{I}\!E^2_{p,q}=H^h_p\big(H^v_q(C)\big)\ \Rightarrow\ H_{p+q}(\mathrm{Tot}\,C),\qquad
> {}^{II}\!E^2_{p,q}=H^v_p\big(H^h_q(C)\big)\ \Rightarrow\ H_{p+q}(\mathrm{Tot}\,C).
> $$

**推导。** 把 $\mathrm{Tot}\,C$ 按列过滤：$F_p(\mathrm{Tot}\,C)_n=\bigoplus_{i\leq p}C_{i,n-i}$。这是一个有界过滤（第一象限），故过滤复形定理适用。在 $E^0$ 页上唯一存活的微分是竖直的 $d^v$（水平部分升高过滤），故 $E^1={}H^v(C)$；诱导的 $d^1$ 是水平映射，故 $E^2=H^h(H^v(C))$——即第一个谱序列。改为按行过滤则给出第二个。两者都收敛到 $H_*(\mathrm{Tot})$，因为它们都来自*同一*复形的有界过滤。*（过滤复形定理；把 $d^0,d^1$ 辨识为 $d^v,d^h$）* $\;\blacksquare$

> **已解例 —— 一个退化的双复形。** 若一个第一象限双复形除行 $q=0$ 外各列均正合，则对 $q>0$ 有 $H^v_q(C)=0$，故 ${}^IE^2$ 集中在第 $0$ 行：${}^IE^2_{p,0}=H^h_p(\text{列同调之行})$，所有更高行为零。于是每个 $d^r$（$r\geq2$）都为零（源或靶落在某零行），故 $E^2=E^\infty$ 且 $H_n(\mathrm{Tot}\,C)\cong H^h_n(H^v_0(C))$。这种“在 $E^2$ 处坍缩”是许多比较定理背后的主力（例如两个消解计算出同一导出函子——$\mathrm{Tor}$ 的平衡性）。

> **边缘映射。** 一个第一象限谱序列总有两个到与自其靶的典范映射，即**边缘同态**。沿底行，复合 $H_n(\mathrm{Tot})\twoheadrightarrow E^\infty_{n,0}\hookrightarrow E^2_{n,0}$ 是一个自然映射 $H_n\to E^2_{n,0}$；沿左列，$E^2_{0,n}\twoheadrightarrow E^\infty_{0,n}\hookrightarrow H_n(\mathrm{Tot})$。*它们良定义的推导：* $E^\infty_{n,0}$ 是 $E^2_{n,0}$ 的一个*商*，因为所有进入的微分 $d^r:E^r_{n+r,1-r}\to E^r_{n,0}$ 都消失（其源在第一象限之下），故只有外出的微分起作用，留下 $E^\infty_{n,0}$ 作为一个子商，而它实则是 $E^2_{n,0}$ 的一个商；对偶地 $E^\infty_{0,n}$ 是 $E^2_{0,n}$ 的一个*子对象*。收敛过滤随后把 $E^\infty_{n,0}$ 置于 $H_n$ 的顶部商、把 $E^\infty_{0,n}$ 置于底部子对象。*（进出微分的第一象限消失；§s8 的收敛过滤）* 这些边缘映射正是在 §s11 中特化为**膨胀（inflation）** 映射 $H^p(Q;M^N)\to H^p(G;M)$ 与**限制（restriction）** 映射 $H^q(G;M)\to H^q(N;M)^Q$ 的对象。

<a id="s10"></a>
### 纤维化的 Leray–Serre 谱序列 —— 一个已解计算

**是什么与为什么。** 拓扑中使用最多的单个谱序列从纤维化的底空间与纤维的同调计算其全空间的同调。我们陈述它并运行一个完整计算。

> **定义 —— 纤维化（Serre）。** 一个连续映射 $\pi:E\to B$ 是一个**（Serre）纤维化**，若它对立方体具有同伦提升性质：$B$ 中一个立方体的任意同伦，给定其起点的一个提升，便提升为 $E$ 中的一个同伦。**纤维**是 $F=\pi^{-1}(b_0)$。*例：* Hopf 映射 $S^1\to S^3\xrightarrow{\pi}S^2$ 的纤维是 $S^1$。

> **定理（Leray–Serre，同调）。** 对纤维化 $F\to E\xrightarrow{\pi}B$，其中 $B$ 道路连通且在 $H_*(F)$ 上平凡作用（单连通底空间情形），存在一个第一象限谱序列
> $$
> E^2_{p,q}=H_p\big(B;\,H_q(F)\big)\ \Rightarrow\ H_{p+q}(E).
> $$
> 微分是 $d^r:E^r_{p,q}\to E^r_{p-r,q+r-1}$，而 $E^\infty$ 是 $H_*(E)$ 某过滤的相伴分次。

**已解计算 —— 由 Hopf 纤维化 $S^1\to S^3\to S^2$ 求 $S^3$ 的同调。** 我们将*验证* $H_*(S^3)$，并在此过程中钉定一个微分。

1. *$E^2$ 页。* 底空间 $B=S^2$ 满足 $H_p(S^2)=\mathbb{Z}$（$p=0,2$）否则为 $0$。纤维 $F=S^1$ 满足 $H_q(S^1)=\mathbb{Z}$（$q=0,1$）否则为 $0$。在平凡作用下，$E^2_{p,q}=H_p(S^2)\otimes H_q(S^1)$（无 $\mathrm{Tor}$，因一切皆自由）。非零项：
> $$
> E^2_{0,0}=\mathbb{Z},\quad E^2_{2,0}=\mathbb{Z},\quad E^2_{0,1}=\mathbb{Z},\quad E^2_{2,1}=\mathbb{Z},
> $$
其余皆 $0$。*（自由系数下的 Künneth，§s5；给定的 $S^1,S^2$ 同调）*
2. *哪些微分可以非零？* $d^2:E^2_{p,q}\to E^2_{p-2,q+1}$。唯一可能非零的 $d^2$ 联结 $E^2_{2,0}=\mathbb{Z}\to E^2_{0,1}=\mathbb{Z}$（因其他源/靶皆 $0$）。把这个映射记作 $\delta$。所有 $r\geq3$ 的 $d^r$ 都消失（双度数把它们推出四个被占据的位置之外）。*（$d^2$ 的双度数；网格仅有四个非零项）*
3. *凭借在角落已知答案确定 $\delta$。* 全空间是 $S^3$：$H_0=\mathbb{Z}$，$H_1=0$，$H_2=0$，$H_3=\mathbb{Z}$。收敛性表明 $\bigoplus_{p+q=n}E^\infty_{p,q}$（作为相伴分次）必须与 $H_n(S^3)$ 匹配。
> - $n=1$：只有 $E^2_{0,1}=\mathbb{Z}$ 有贡献。为使 $H_1(S^3)=0$ 我们需要 $E^\infty_{0,1}=0$，即 $\delta:E^2_{2,0}\to E^2_{0,1}$ 必须**映满** $\mathbb{Z}$。
> - $n=2$：只有 $E^2_{2,0}=\mathbb{Z}$ 有贡献。为使 $H_2(S^3)=0$ 我们需要 $E^\infty_{2,0}=0$，即 $\delta$ 必须**单射**（$\ker\delta=0$）。
> 二者合起来：$\delta:\mathbb{Z}\to\mathbb{Z}$ 是同构，故它是 $\pm1$。*（收敛性：$E^\infty=H_*(S^3)$ 的相伴分次）*
4. *核验存活的角落。* 在 $d^2=\delta$（同构）之后，$E^3_{2,0}=E^3_{0,1}=0$，而 $E^3_{0,0}=\mathbb{Z}$ 与 $E^3_{2,1}=\mathbb{Z}$ 原封不动地存活（没有微分触及它们）。它们稳定下来：$E^\infty_{0,0}=\mathbb{Z}$ 给出 $H_0(S^3)=\mathbb{Z}$ ✓，而 $E^\infty_{2,1}=\mathbb{Z}$（$p+q=3$）给出 $H_3(S^3)=\mathbb{Z}$ ✓。*（稳定化；收敛性）*
5. *结论。* 谱序列重现了 $H_*(S^3)=(\mathbb{Z},0,0,\mathbb{Z})$，并迫使 Hopf 纤维化的横越（transgression）$\delta$ 为同构——这是 Hopf 丛非平凡性的代数指纹。$\;\blacksquare$

**第二个计算 —— 由道路纤维化求环路空间同调 $H_*(\Omega S^3)$。** **道路–环路纤维化** $\Omega S^3\to PS^3\xrightarrow{\pi}S^3$ 具有可缩的全空间 $PS^3$（基于点的道路之道路空间）、纤维为环路空间 $\Omega S^3$、底空间为 $S^3$。我们*反过来*使用它：已知 $E$ 可缩，我们推出 $H_*(\Omega S^3)$。

1. *我们已知的。* $H_*(PS^3)=H_*(\text{点})$：度数 $0$ 处为 $\mathbb{Z}$，否则为 $0$。底空间 $S^3$：$H_p(S^3)=\mathbb{Z}$（$p=0,3$），否则为 $0$。令 $h_q=H_q(\Omega S^3)$ 为未知量。
2. *$E^2$ 页。* 因底空间单连通，$E^2_{p,q}=H_p(S^3)\otimes h_q$（自由，在未证明之前无 $\mathrm{Tor}$）。唯一非零的列是 $p=0$ 与 $p=3$：$E^2_{0,q}=h_q$ 而 $E^2_{3,q}=h_q$。*（Künneth，平凡作用）*
3. *唯一可能的微分。* 因两列相距三格，唯一可能非零的微分是 $d^3:E^3_{3,q}\to E^3_{0,q+2}$，即 $h_q\to h_{q+2}$。*（$d^3$ 的双度数 $(-3,2)$；其他 $d^r$ 落在零列）*
4. *迫出答案。* 由于 $E^\infty$ 必须是一点的（除 $E^\infty_{0,0}=\mathbb{Z}$ 外皆零），每个 $d^3$ 都必须是同构 $h_q\xrightarrow{\sim}h_{q+2}$（$q\geq0$）（否则一个存活的类会给出 $PS^3$ 在正度数处的非零同调），唯一例外是 $E^2_{0,0}=h_0=\mathbb{Z}$ 必须存活。从 $h_0=\mathbb{Z}$（道路连通的环路空间）与 $h_1$ 出发：位置 $(0,1)$ 只能被来自 $(3,-1)=0$ 的 $d^3$ 杀灭，故为使 $E^\infty_{0,1}=0$，$h_1$ 必须本就消失；于是 $h_1=0$。然后 $d^3:h_0\to h_2$ 同构给出 $h_2=\mathbb{Z}$；由同样的奇偶论证 $h_3$ 必须消失；$d^3:h_2\to h_4$ 给出 $h_4=\mathbb{Z}$；归纳地 $h_{2k}=\mathbb{Z}$ 且 $h_{2k+1}=0$。*（向一点收敛迫使微分确定）*
5. *结论。* $H_q(\Omega S^3)=\mathbb{Z}$（$q$ 偶），$0$（$q$ 奇）——重现了 $\Omega S^3$ 具有一个单一度数-$2$ 生成元上的无穷“分次幂”代数之同调这一已知事实。$\;\blacksquare$

**直觉。** $E^2$ 页是“带纤维同调系数的底空间同调”。微分记录纤维随你绕底空间移动时如何扭转；一个非零的 $d^r$ 意味着该丛真正非平凡。把一个已知全空间*反过来*运行（如道路纤维化中那样）便计算出纤维——这是通往环路空间同调、并最终通往同伦群的标准途径。**陷阱：** 当 $\pi_1(B)$ 在 $H_*(F)$ 上非平凡作用时，必须在 $E^2$ 页上使用*局部*（扭曲）系数——上面的平凡作用假设是关键的。

<a id="s11"></a>
### 群上同调与 Lyndon–Hochschild–Serre 谱序列（概览）

**是什么与为什么。** 把“空间”替换为“群”便得到**群上同调**，即取不变量的导出函子。一个群的短正合列于是扮演纤维化的角色，而其谱序列——Lyndon–Hochschild–Serre（LHS）——把整个群的上同调与一个正规子群及商的上同调联系起来。

**是什么与为什么。** 群上同调回答诸如“$Q$ 被一个阿贝尔群的扩张有多少个？”与“哪些对称性可以提升？”这样的问题。它是不变量的导出函子，由 §s3–s4 的消解机器应用于群环来计算。本节末尾的谱序列是 Leray–Serre 序列的群论镜像。

> **定义 —— $G$-模。**
> 一个 **$G$-模** $M$ 是一个带有群 $G$ 通过自同构作用的阿贝尔群；等价地是**群环** $\mathbb{Z}[G]$（有限形式和 $\sum n_g\, g$，用群法则相乘）上的一个模。**不变量**是 $M^G=\{m: gm=m\ \forall g\}$，且 $(-)^G=\mathrm{Hom}_{\mathbb{Z}[G]}(\mathbb{Z},-)$，其中 $\mathbb{Z}$ 带平凡作用。

> **定义 —— 群上同调。**
> $H^n(G;M)=\mathrm{Ext}^n_{\mathbb{Z}[G]}(\mathbb{Z},M)=R^n(-)^G(M)$，即取 $G$-不变量的右导出函子（§s4）。故 $H^0(G;M)=M^G$，而更高的 $H^n$ 度量不变量不正合的程度。*例：* $H^1(G;M)$ 分类“模主交叉同态的交叉同态”；对平凡作用 $H^1(G;M)=\mathrm{Hom}(G,M)$。

> **完整计算 —— 由自由消解求 $H^n(\mathbb{Z}/2;\mathbb{Z})$。** 设 $G=\mathbb{Z}/2=\langle t\mid t^2=1\rangle$，故 $\mathbb{Z}[G]=\mathbb{Z}[t]/(t^2-1)$。平凡模 $\mathbb{Z}$ 在 $\mathbb{Z}[G]$ 上有一个标准的**周期性**自由消解：
> $$
> \cdots\to\mathbb{Z}[G]\xrightarrow{\,t-1\,}\mathbb{Z}[G]\xrightarrow{\,t+1\,}\mathbb{Z}[G]\xrightarrow{\,t-1\,}\mathbb{Z}[G]\xrightarrow{\,\varepsilon\,}\mathbb{Z}\to0,
> $$
> 其中 $\varepsilon(t)=1$ 是增广。可验证在 $\mathbb{Z}[G]$ 中 $(t-1)(t+1)=t^2-1=0$ 且 $(t+1)(t-1)=0$，正合性则因为 $\ker\varepsilon$ 由 $t-1$ 生成、$\ker(t-1)$ 由 $t+1$ 生成，等等。施以 $\mathrm{Hom}_{\mathbb{Z}[G]}(-,\mathbb{Z})$（$\mathbb{Z}$ 平凡）；每个 $\mathrm{Hom}_{\mathbb{Z}[G]}(\mathbb{Z}[G],\mathbb{Z})=\mathbb{Z}$，$t-1$ 的对偶变为乘以 $\varepsilon(t)-1=0$，而 $t+1$ 的对偶变为 $\varepsilon(t)+1=2$。上链复形是
> $$
> \mathbb{Z}\xrightarrow{0}\mathbb{Z}\xrightarrow{2}\mathbb{Z}\xrightarrow{0}\mathbb{Z}\xrightarrow{2}\cdots
> $$
> 上同调：$H^0=\mathbb{Z}$；在奇度数 $H^{2k+1}=\ker(2)/\mathrm{im}(0)=0$；在正偶度数 $H^{2k}=\ker(0)/\mathrm{im}(2)=\mathbb{Z}/2$。故 $H^n(\mathbb{Z}/2;\mathbb{Z})=\mathbb{Z},0,\mathbb{Z}/2,0,\mathbb{Z}/2,\dots$——与 $H^*(\mathbb{RP}^\infty;\mathbb{Z})$ 同样的模式，因为 $\mathbb{RP}^\infty$ 是分类空间 $B(\mathbb{Z}/2)$，而群上同调*就是*分类空间的上同调。

> **定理（Lyndon–Hochschild–Serre）。** 对群的短正合列 $1\to N\to G\to Q\to1$ 与一个 $G$-模 $M$，存在一个第一象限谱序列
> $$
> E_2^{p,q}=H^p\big(Q;\,H^q(N;M)\big)\ \Rightarrow\ H^{p+q}(G;M).
> $$

**它从何而来（概览）。** 函子“取 $G$-不变量”分解为“取 $N$-不变量，再取 $Q=G/N$-不变量”：$M^G=(M^N)^Q$。LHS 是这个函子复合的 **Grothendieck 谱序列**——即一条普遍定理：对一对可复合函子 $F,F'$，若 $F$ 把内射对象/无圈对象送到 $F'$-无圈对象，则存在一个谱序列 $R^pF'\big(R^qF(M)\big)\Rightarrow R^{p+q}(F'\circ F)(M)$。具体地它是一个合适的双重消解的双复形谱序列（§s9）。*（复合函子 / Grothendieck 谱序列，由 §s9 构造）*

> **已解之用 —— 五项正合列。** 恰如 §s8 的两列例子那样读取 LHS 的低度数角落，对任意 $1\to N\to G\to Q\to1$ 给出
> $$
> 0\to H^1(Q;M^N)\to H^1(G;M)\to H^1(N;M)^Q\xrightarrow{\,d_2\,} H^2(Q;M^N)\to H^2(G;M).
> $$
> *推导：* 满足 $p+q\leq2$ 的项 $E_2^{p,q}$ 与单个 $d_2:E_2^{0,1}\to E_2^{2,0}$ 是低度数中仅有的可以非零的；用收敛过滤（§s8）装配它们的核/余核即给出这五项。这尤其重现了 Galois 上同调的膨胀–限制序列。*（第一象限谱序列的低度数读取，§s8）*

**直觉。** 一个正规子群 $N\trianglelefteq G$ 行为如同一个“纤维”，而 $Q=G/N$ 如同一个“底空间”；LHS 是分类空间纤维化 $BN\to BG\to BQ$ 的代数 Leray–Serre 谱序列。整份指南闭合了回路：同一套二维记账装置计算空间、模与群的（上）同调。

---

*一门从零开始讲授同调代数与谱序列的课程：正合性与图追踪、链复形、消解、导出函子 $\mathrm{Tor}$ 与 $\mathrm{Ext}$、万有系数定理与 Künneth 定理、使其可移植的范畴语言，以及组织一切计算的谱序列——过滤型、双复形型、Leray–Serre 型与 Lyndon–Hochschild–Serre 型。先通读一遍以把握整体架构；再回到任意盒子去看证明。底层的单一思想：度量正合性的失败，然后在二维中将这一度量记账。*
