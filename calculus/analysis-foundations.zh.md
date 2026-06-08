[English](analysis-foundations.md) · **中文**

# 微积分，*变得严格。*

这本伴读读物深入到公式之下。在这里，每一个极限都是一个 $\varepsilon$，每一个定理都被**精确陈述并加以证明**，整座大厦——连续性、导数、积分、级数——都从一个根基重建：实数的**完备性**。

[← 返回全部指南](../README.zh.md)

## 第 A 部分 · 数与数列

<a id="s0"></a>
### 总览：为何要严格，以及 $\varepsilon$ 的角色

微积分在与无穷打交道时进行计算。分析这门学科使那些计算*真正成立*，而不仅仅是看上去合理。

两个世纪以来，微积分依靠关于"无穷小"量的直觉运行。它取得了惊人的成功——同时也制造了悖论：发散级数求和得出荒谬结果，处处不可导的"连续"函数，以及证明 $1=0$ 的论证。十九世纪由**柯西、魏尔斯特拉斯、波尔查诺、戴德金**等人推进的工程，用一个单一而精确的思想取代了含糊的无穷小：由 $\varepsilon$ 定义的**极限**。

> **原理 —— "严格"给你带来什么**
>
> 那个非正式的说法"当 $x$ 接近 $a$ 时 $f(x)$ 接近 $L$"隐藏了两个问题：*多么*接近，以及*谁先选?* $\varepsilon$–$\delta$ 定义同时回答了这两点：**一个对手指定一个容差 $\varepsilon>0$，而你必须拿出一个满足它的 $\delta$。** 微积分的每一个定理都成为你真正能兑现的保证，而不是一幅你寄望它正确的图画。

> **概念 —— 唯一的根基：完备性**
>
> 有理数 $\mathbb{Q}$ 在 $\sqrt 2$ 处有一个洞；数列 $1,1.4,1.41,1.414,\dots$ "想"收敛，却在 $\mathbb{Q}$ 中无处落脚。实数 $\mathbb{R}$ 正是为了**没有洞**而构造出来的。那一条性质——**完备性**——是前方每一个存在性定理背后的引擎：有界单调数列收敛，连续函数取得最大值，积分存在。

#### 整门学科浓缩为一行

> 实数与完备性 → 数列的极限 → 连续性 → 导数 → 积分 → 函数项级数 → 幂级数

> **联系 —— 本指南与其他指南**
>
> 《完整微积分》和《从零导出》这两本指南告诉你规则、展示给你各种操作。本指南回答下一个问题——**为什么那些规则是有效的?** 每当你用到一个极限、一个连续性假设或"$dx$"，其下都有一个定理；在这里我们指出它并证明它。

<a id="s1"></a>
### 实数：有序域、完备性与上确界

*一切都建立在确切知道 $\mathbb{R}$ 是什么之上。它是唯一的完备有序域——而"完备"一词正是把它与 $\mathbb{Q}$ 区分开来的东西。*

**有序域公理**

*$\mathbb{R}$ 是一个**域**：$+$ 与 $\cdot$ 满足结合律、交换律、分配律，有单位元 $0,1$ 以及逆元（$-x$，以及当 $x\ne 0$ 时的 $x^{-1}$）。它是**有序的**：一个关系 $\lt$，它是全序的、传递的，与加法相容（$a\lt b\Rightarrow a+c\lt b+c$），并与乘以正数相容（$a\lt b,\ c\gt 0\Rightarrow ac\lt bc$）。有理数 $\mathbb{Q}$ 也满足所有这些——所以到目前为止的公理*并未*把 $\mathbb{R}$ 单独刻画出来。*

**界、上确界与下确界**

$$u \text{ is an upper bound of } S \iff \forall x\in S,\ x\le u.$$

$$\sup S = \text{the } least \text{ upper bound of } S;\qquad \inf S = \text{the } greatest \text{ lower bound.}$$

*$M=\sup S$ 意味着：(i) $M$ 是一个上界，且 (ii) 对每个 $\varepsilon>0$ 存在 $x\in S$ 使得 $x\gt M-\varepsilon$（任何小于 $M$ 的数都不能充当上界）。下面几乎每个证明都用到这一刻画。*

> **公理 —— 完备性（最小上界性质）**
>
> 这是 $\mathbb{R}$ 的定义性公理：**$\mathbb{R}$ 中每一个有上界的非空子集在 $\mathbb{R}$ 中都有上确界。** 集合 $\{x\in\mathbb{Q}: x^2\lt 2\}$ 有上界，却*在 $\mathbb{Q}$ 中*没有上确界——它本应是的上确界是 $\sqrt 2$，而那是缺失的。完备性说 $\mathbb{R}$ 没有这样的缝隙。

**证明 —— 阿基米德性质：$\mathbb{N}$ 在 $\mathbb{R}$ 中无界**

1. 断言：对每个 $x\in\mathbb{R}$ 存在 $n\in\mathbb{N}$ 使 $n\gt x$。假设不然——那么 $\mathbb{N}$ 有上界。
2. 由于 $\mathbb{N}\ne\varnothing$ 且有上界，完备性给出 $s=\sup\mathbb{N}\in\mathbb{R}$。
3. 那么 $s-1$ 不是上界（它小于最小的那个），所以某个 $m\in\mathbb{N}$ 满足 $m\gt s-1$，即 $m+1\gt s$。

   $$m+1\in\mathbb{N}\ \text{yet}\ m+1\gt s=\sup\mathbb{N}.$$
4. 这与 $s$ 是 $\mathbb{N}$ 的上界相矛盾。因此 $\mathbb{N}$ 无界。

*推论：对任何 $\varepsilon>0$ 存在 $n$ 使 $1/n\lt\varepsilon$（取 $n\gt 1/\varepsilon$）。正是这个微小的事实使得 $1/n\to 0$ 驱动无数极限。$\blacksquare$*

**证明 —— $\mathbb{Q}$ 在 $\mathbb{R}$ 中稠密**

1. 给定 $a\lt b$，我们在 $(a,b)$ 中找一个有理数。由阿基米德性质取 $n$ 使 $1/n\lt b-a$，于是 $nb-na\gt 1$。
2. 一个长度大于 $1$ 的区间含有一个整数：设 $m$ 为满足 $m\gt na$ 的最小整数。那么 $m-1\le na$，所以 $m\le na+1\lt nb$。
3. 于是 $na\lt m\lt nb$，除以 $n$：

   $$a\lt \frac{m}{n}\lt b.$$

*任意两个实数之间都有一个有理数——这就是有理逼近处处奏效的原因。$\blacksquare$*

> **联系 —— 为什么这个排在最前面**
>
> 你在微积分中凭信心接受的每一个"极限存在"的论断，最终都兑现为由完备性产生的一个上确界。失去这条公理，连续函数就能越过零点而不取到它，有界数列也未必收敛，积分也可能不存在。$\mathbb{R}$ 被精心打造，使这些事都不会发生。

<a id="s2"></a>
### 数列及其极限（$\varepsilon$–$N$ 定义）

*最简单的无穷过程。在这里掌握 $\varepsilon$–$N$ 定义，连续性的 $\varepsilon$–$\delta$ 就是同一个思想换了一只时钟。*

**定义 —— 数列的收敛**

$$a_n \to L \iff \forall\varepsilon>0\ \ \exists N\in\mathbb{N}\ \ \forall n\ge N:\ \ |a_n-L|\lt\varepsilon.$$

*把它读作一场博弈：对手任选一个容差 $\varepsilon$；你必须指出一个阈值 $N$，越过它之后*所有*项都落在 $L$ 的 $\varepsilon$ 范围内。如果你总能应答，极限就是 $L$。*

**证明 —— 极限是唯一的**

1. 假设 $a_n\to L$ 且 $a_n\to L'$，其中 $L\ne L'$。令 $\varepsilon=\tfrac{|L-L'|}{2}\gt 0$。
2. 取 $N_1$ 使得当 $n\ge N_1$ 时 $|a_n-L|\lt\varepsilon$，并取 $N_2$ 使得当 $n\ge N_2$ 时 $|a_n-L'|\lt\varepsilon$。对 $n\ge\max(N_1,N_2)$，两者同时成立。
3. 三角不等式：即 $|L-L'|\lt|L-L'|$，不可能。

   $$|L-L'|\le|L-a_n|+|a_n-L'|\lt\varepsilon+\varepsilon=|L-L'|,$$

*一个数列不能收敛到两个不同的值——"那个"极限是良定义的。$\blacksquare$*

**证明 —— 收敛数列是有界的**

1. 设 $a_n\to L$。取 $\varepsilon=1$：存在 $N$ 使 $|a_n-L|\lt 1$，因而对所有 $n\ge N$ 有 $|a_n|\lt|L|+1$。
2. 只剩下有限多项：$a_1,\dots,a_{N-1}$。令

   $$M=\max\big(|a_1|,\dots,|a_{N-1}|,\ |L|+1\big).$$
3. 那么对每个 $n$ 都有 $|a_n|\le M$。

*有界性是收敛的必要条件——不过正如我们将看到的，它并不充分。$\blacksquare$*

**定理 —— 极限的代数运算**

$$\text{If } a_n\to A,\ b_n\to B,\text{ then } a_n+b_n\to A+B,\ \ a_nb_n\to AB,\ \ \tfrac{a_n}{b_n}\to\tfrac{A}{B}\ (B\ne 0).$$

**证明 —— 和的极限等于极限的和**

1. 设 $a_n\to A$，$b_n\to B$，并固定 $\varepsilon>0$。窍门：把预算的一半花在每个数列上。
2. 选 $N_1$ 使 $n\ge N_1\Rightarrow|a_n-A|\lt\tfrac{\varepsilon}{2}$，并选 $N_2$ 使 $n\ge N_2\Rightarrow|b_n-B|\lt\tfrac{\varepsilon}{2}$。
3. 对 $n\ge N=\max(N_1,N_2)$，三角不等式给出

   $$|(a_n+b_n)-(A+B)|\le|a_n-A|+|b_n-B|\lt\tfrac{\varepsilon}{2}+\tfrac{\varepsilon}{2}=\varepsilon.$$

*"$\varepsilon/2$ 技巧"——把容差分配给各部分——贯穿整个分析学。$\blacksquare$*

**证明 —— 乘积的极限等于极限的乘积**

1. 写出差并插入一个交叉项：

   $$a_nb_n-AB=a_n b_n - a_n B + a_n B - AB = a_n(b_n-B)+B(a_n-A).$$
2. 由于 $(a_n)$ 收敛，它有界：对所有 $n$ 有 $|a_n|\le M$（上一个证明）。于是

   $$|a_nb_n-AB|\le M\,|b_n-B|+|B|\,|a_n-A|.$$
3. 给定 $\varepsilon>0$，对充分大的 $n$ 使 $|b_n-B|\lt\dfrac{\varepsilon}{2M}$ 且 $|a_n-A|\lt\dfrac{\varepsilon}{2(|B|+1)}$；那么右端 $\lt\tfrac{\varepsilon}{2}+\tfrac{\varepsilon}{2}=\varepsilon$。

*插入 $\pm a_nB$ 就是"加减同一项"技巧——乘法型极限证明的主力。$\blacksquare$*

> **联系 —— 你曾随手使用的规则**
>
> "和/积的极限等于极限的和/积"曾是你不假思索就用的规则。它是一个*定理*，而这就是它的证明。函数情形下的相同陈述（第 5 节）由完全相同的论证得出，只是用 $\delta$ 代替 $N$。

<a id="s3"></a>
### 单调收敛、波尔查诺–魏尔斯特拉斯与柯西数列

*三个存在性定理——每一个都是完备性保证一个你无法手算的极限的不同方式。*

**定理 —— 单调收敛**

$$\text{Every bounded monotone sequence converges.}$$

*若 $(a_n)$ 递增且有上界，则 $a_n\to\sup\{a_n\}$；若递减且有下界，则 $a_n\to\inf\{a_n\}$。单调*且*有界就足够了——你不必事先知道极限。*

**证明 —— 单调且有界 $\Rightarrow$ 收敛（借助上确界）**

1. 设 $(a_n)$ 递增且有上界。集合 $S=\{a_n:n\in\mathbb{N}\}$ 非空且有上界，所以由完备性存在 $L=\sup S$。
2. 固定 $\varepsilon>0$。由于 $L-\varepsilon$ 不是上界，某一项 $a_N\gt L-\varepsilon$。
3. 因为数列递增，对所有 $n\ge N$：$a_N\le a_n\le L$。因此

   $$L-\varepsilon\lt a_N\le a_n\le L\lt L+\varepsilon\ \Rightarrow\ |a_n-L|\lt\varepsilon.$$

*这是看完备性*凭空创造出*一个极限的最干净之处。$\blacksquare$*

**定理 —— 波尔查诺–魏尔斯特拉斯**

$$\text{Every bounded sequence in } \mathbb{R} \text{ has a convergent subsequence.}$$

**证明 —— 用二分法证明波尔查诺–魏尔斯特拉斯**

1. 设 $(a_n)$ 落在 $[A,B]$ 中。二等分：至少有一半含有无穷多项——称之为 $I_1$，长度为 $\tfrac{B-A}{2}$。取 $a_{n_1}\in I_1$。
2. 重复：二等分 $I_1$，保留一个含无穷多项的半区间 $I_2$（长度 $\tfrac{B-A}{4}$），并取 $a_{n_2}\in I_2$ 且 $n_2\gt n_1$。继续下去，构造嵌套区间 $I_1\supset I_2\supset\cdots$，其长度 $\to 0$。
3. 左端点递增且有界，所以由单调收敛它们趋向一点 $L$（由闭区间套性质，它是所有 $I_k$ 中的唯一公共点）。由于 $a_{n_k}\in I_k$ 且 $|I_k|\to 0$：

   $$|a_{n_k}-L|\le|I_k|=\frac{B-A}{2^{k}}\to 0.$$

*一个有界数列可以永远游荡，但它必定在某处*聚集*。这是 $[A,B]$ 的紧性的伪装。$\blacksquare$*

**定义 —— 柯西数列**

$$(a_n) \text{ is Cauchy} \iff \forall\varepsilon>0\ \exists N\ \forall m,n\ge N:\ |a_n-a_m|\lt\varepsilon.$$

*各项最终在*它们自己之间*聚集——完全不提及极限 $L$。这让你无需知道目标就能证明收敛。*

**证明 —— 每个收敛数列都是柯西的**

1. 设 $a_n\to L$ 并固定 $\varepsilon>0$。选 $N$ 使对所有 $n\ge N$ 有 $|a_n-L|\lt\tfrac{\varepsilon}{2}$。
2. 对任何 $m,n\ge N$，经由 $L$ 中转：

   $$|a_n-a_m|\le|a_n-L|+|L-a_m|\lt\tfrac{\varepsilon}{2}+\tfrac{\varepsilon}{2}=\varepsilon.$$

*收敛 $\Rightarrow$ 柯西很容易，并且在任何度量空间中都成立。$\blacksquare$*

**证明 —— $\mathbb{R}$ 中每个柯西数列都收敛（$\mathbb{R}$ 的完备性）**

1. 柯西数列有界：取 $\varepsilon=1$，得到 $N$ 使对 $n\ge N$ 有 $|a_n-a_N|\lt 1$，再如第 2 节那样定界。
2. 由波尔查诺–魏尔斯特拉斯，它有一个收敛子列 $a_{n_k}\to L$。
3. 现在证明整个数列 $\to L$。固定 $\varepsilon>0$；取 $N$ 使对 $m,n\ge N$ 有 $|a_n-a_m|\lt\tfrac{\varepsilon}{2}$，并取 $n_k\ge N$ 使 $|a_{n_k}-L|\lt\tfrac{\varepsilon}{2}$。对 $n\ge N$：

   $$|a_n-L|\le|a_n-a_{n_k}|+|a_{n_k}-L|\lt\tfrac{\varepsilon}{2}+\tfrac{\varepsilon}{2}=\varepsilon.$$

*在 $\mathbb{R}$ 中，柯西 $\iff$ 收敛。这个**柯西判别法**是为数列重新陈述的"完备性"，并且是级数和积分收敛的根基。$\blacksquare$*

<a id="s4"></a>
### 上极限与下极限

即使是不收敛的数列也有一个长期行为的"天花板"和"地板"——而它们*总是*存在。

**定义 —— $\limsup$ 与 $\liminf$**

$$\limsup_{n\to\infty} a_n=\lim_{n\to\infty}\Big(\sup_{k\ge n} a_k\Big),\qquad \liminf_{n\to\infty} a_n=\lim_{n\to\infty}\Big(\inf_{k\ge n} a_k\Big).$$

*令 $s_n=\sup_{k\ge n}a_k$。随着 $n$ 增大，我们在更小的尾部取上确界，所以 $s_n$ 递减；若有下界则它收敛（单调收敛）——那个极限就是 $\limsup$。对于有界数列，两者在 $\mathbb{R}$ 中总是存在。*

> **概念 —— 它们刻画了什么**
>
> $\limsup a_n$ 是数列无穷次逼近的最大值（其最大的子列极限）；$\liminf a_n$ 是最小的。对 $a_n=(-1)^n$：$\limsup=1$，$\liminf=-1$。即使不存在单一极限，它们也钉住了数列最终的取值范围。

**证明 —— $a_n\to L \iff \limsup a_n=\liminf a_n=L$**

1. （$\Rightarrow$）若 $a_n\to L$，则对 $\varepsilon>0$，越过某个 $N$ 之后所有项都落在 $(L-\varepsilon,L+\varepsilon)$ 中，所以对 $n\ge N$，$\sup_{k\ge n}a_k$ 与 $\inf_{k\ge n}a_k$ 都落在 $[L-\varepsilon,L+\varepsilon]$ 中。令 $\varepsilon\to 0$ 迫使两者都趋向 $L$。
2. （$\Leftarrow$）假设 $\liminf=\limsup=L$。总有 $\inf_{k\ge n}a_k\le a_n\le\sup_{k\ge n}a_k$。

   $$\liminf a_n\ \le\ a_n\ \le\ \limsup a_n.$$
3. 外侧的两者都趋向 $L$，所以由夹逼定理 $a_n\to L$。

*收敛恰恰是最终的天花板与地板之间的间隙坍缩为零。$\blacksquare$*

> **联系 —— 根值判别法与比值判别法**
>
> 你用过的级数收敛判别法（根值判别法、比值判别法）用 $\limsup$ 严格地陈述：级数 $\sum a_n$ 绝对收敛，如果 $\limsup|a_n|^{1/n}\lt 1$。因为 $\limsup$ 总是存在，这些判别法总有话可说——即便对那些飘忽不定的项也是如此。

## 第 B 部分 · 连续性与微分

<a id="s5"></a>
### 函数的极限与连续性（$\varepsilon$–$\delta$）

*与 $\varepsilon$–$N$ 同一场博弈，现在由输入距离 $\delta$ 控制输出距离 $\varepsilon$。*

**定义 —— 函数的极限**

$$\lim_{x\to a} f(x)=L \iff \forall\varepsilon>0\ \exists\delta>0:\ 0\lt|x-a|\lt\delta\ \Rightarrow\ |f(x)-L|\lt\varepsilon.$$

*"$0\lt|x-a|$"把 $x=a$ 本身排除在外：极限关乎逼近，而非在 $a$ 处的取值。*

**定义 —— 在一点处的连续性**

$$f \text{ continuous at } a \iff \forall\varepsilon>0\ \exists\delta>0:\ |x-a|\lt\delta\ \Rightarrow\ |f(x)-f(a)|\lt\varepsilon.$$

*等价地 $\lim_{x\to a}f(x)=f(a)$：极限存在，$f(a)$ 有定义，且二者一致。现在允许 $x=a$（它平凡地满足结论）。*

**证明 —— $f(x)=x^2$ 在每一点 $a$ 处连续**

1. 固定 $a$ 与 $\varepsilon>0$。我们必须控制 $|x^2-a^2|=|x-a|\,|x+a|$。
2. 把搜索限制在 $|x-a|\lt 1$；则 $|x|\lt|a|+1$，所以 $|x+a|\le|x|+|a|\lt 2|a|+1$。
3. 选 $\delta=\min\!\Big(1,\ \dfrac{\varepsilon}{2|a|+1}\Big)$。那么 $|x-a|\lt\delta$ 给出

   $$|x^2-a^2|=|x-a|\,|x+a|\lt\frac{\varepsilon}{2|a|+1}\cdot(2|a|+1)=\varepsilon.$$

*"先给棘手的因子定界，再选 $\delta$"这个套路能处理大多数显式的 $\varepsilon$–$\delta$ 证明。$\blacksquare$*

**定理 —— 连续性的序列判别准则**

$$f \text{ continuous at } a \iff \big(x_n\to a \Rightarrow f(x_n)\to f(a)\big)\ \text{for every sequence } x_n.$$

*第 A 部分与第 B 部分之间的一座桥梁：它让你为函数重用所有数列定理，也让你通过给出一个坏数列来*否证*连续性。*

**证明 —— 连续函数的复合仍连续**

1. 设 $g$ 在 $a$ 处连续，$f$ 在 $b=g(a)$ 处连续；证明 $f\circ g$ 在 $a$ 处连续。固定 $\varepsilon>0$。
2. 由 $f$ 在 $b$ 处连续：存在 $\eta>0$ 使 $|y-b|\lt\eta\Rightarrow|f(y)-f(b)|\lt\varepsilon$。
3. 由 $g$ 在 $a$ 处连续：存在 $\delta>0$ 使 $|x-a|\lt\delta\Rightarrow|g(x)-b|\lt\eta$。把它们串起来：

   $$|x-a|\lt\delta\ \Rightarrow\ |g(x)-b|\lt\eta\ \Rightarrow\ |f(g(x))-f(b)|\lt\varepsilon.$$

*连续性穿过复合传递——这是对复合函数求导的严格根据。$\blacksquare$*

> **联系 —— "你可以直接代入"**
>
> 在第一门微积分课程中，通过"代入"来求极限之所以奏效，恰恰*是因为*函数连续。连续性是 $\lim_{x\to a}f=f(a)$ 的正式陈述——代入的许可证。

<a id="s6"></a>
### 关于连续函数的定理：介值定理、最值定理与一致连续性

*在一个闭有界区间上，连续性强得惊人。三个定理说明了缘由——而且三个都需要完备性。*

**定理 —— 介值定理（IVT）**

$$f \text{ continuous on } [a,b],\ \ f(a)\lt y\lt f(b)\ \Rightarrow\ \exists c\in(a,b):\ f(c)=y.$$

**证明 —— 用上确界证明介值定理**

1. 不妨设 $y=0$ 且 $f(a)\lt 0\lt f(b)$（用 $f-y$ 替换 $f$）。令 $S=\{x\in[a,b]:f(x)\lt 0\}$。它非空（$a\in S$）且以 $b$ 为上界，所以由完备性存在 $c=\sup S$。
2. 假设 $f(c)\lt 0$。由连续性，$f$ 在 $c$ 附近的一个小区间上保持为负，所以 $c$ 稍右侧的点也在 $S$ 中——这与 $c=\sup S$ 矛盾。
3. 假设 $f(c)\gt 0$。由连续性，$f$ 在 $c$ 紧左侧保持为正，所以一个更小的数已经是 $S$ 的上界——再次与 $c=\sup S$ 矛盾。因此

   $$f(c)=0.$$

*一条连续的图像不能越过某个值而跳过去——这是被证明的，而非画出来的。这是每一种求根二分法的根源。$\blacksquare$*

**定理 —— 最值定理（EVT）**

$$f \text{ continuous on } [a,b]\ \Rightarrow\ f \text{ is bounded and attains a max and a min on } [a,b].$$

**证明 —— 用波尔查诺–魏尔斯特拉斯证明最值定理**

1. 有界：若不然，存在 $x_n\in[a,b]$ 使 $|f(x_n)|\to\infty$。由波尔查诺–魏尔斯特拉斯，某个子列 $x_{n_k}\to x^*\in[a,b]$；连续性给出 $f(x_{n_k})\to f(x^*)$，一个有限的数——与 $|f(x_{n_k})|\to\infty$ 矛盾。
2. 取到：令 $M=\sup_{[a,b]}f$（现在 $f$ 有界，它存在）。取 $x_n$ 使 $f(x_n)\to M$。
3. 由波尔查诺–魏尔斯特拉斯，$x_{n_k}\to c\in[a,b]$；连续性给出 $f(c)=\lim f(x_{n_k})=M$。对 $-f$ 应用同样的方法即得最小值。

   $$f(c)=M=\max_{[a,b]}f.$$

*闭的、有界的区间（紧性）是本质性的：$f(x)=1/x$ 在 $(0,1]$ 上连续却无界。$\blacksquare$*

**定义 —— 一致连续性**

$$f \text{ uniformly continuous on } I \iff \forall\varepsilon>0\ \exists\delta>0\ \forall x,y\in I:\ |x-y|\lt\delta\Rightarrow|f(x)-f(y)|\lt\varepsilon.$$

*与普通连续性的关键区别：**同一个 $\delta$ 一次性对整个区间都有效**——它可以不依赖于点。$f(x)=1/x$ 在 $(0,1)$ 上连续却非一致连续：靠近 0 时你需要越来越小的 $\delta$。*

**证明 —— 海涅–康托尔：在 $[a,b]$ 上连续 $\Rightarrow$ 一致连续**

1. 假设不然。那么存在 $\varepsilon_0>0$，使得对每个 $\delta=\tfrac1n$ 都存在 $x_n,y_n\in[a,b]$，满足 $|x_n-y_n|\lt\tfrac1n$ 却 $|f(x_n)-f(y_n)|\ge\varepsilon_0$。
2. 由波尔查诺–魏尔斯特拉斯，某个子列 $x_{n_k}\to c\in[a,b]$。由于 $|x_{n_k}-y_{n_k}|\lt\tfrac{1}{n_k}\to 0$，故 $y_{n_k}\to c$ 也成立。
3. 由在 $c$ 处的连续性，$f(x_{n_k})\to f(c)$ 且 $f(y_{n_k})\to f(c)$，所以它们的差 $\to 0$——与 $|f(x_{n_k})-f(y_{n_k})|\ge\varepsilon_0$ 矛盾。

   $$0=\lim|f(x_{n_k})-f(y_{n_k})|\ge\varepsilon_0\gt 0.$$

*紧性把逐点连续性升级为一致连续性——正是这个事实使得连续函数的黎曼积分存在（第 8 节）。$\blacksquare$*

> **定理 —— 海涅–博雷尔（命名）**
>
> $\mathbb{R}$（或 $\mathbb{R}^n$）的一个子集是**紧的**——每个开覆盖都有有限子覆盖——*当且仅当*它是**闭且有界的**。这是最值定理和海涅–康托尔背后的抽象引擎；"闭有界区间"是最简单的紧集。

<a id="s7"></a>
### 微分：中值定理与带余项的泰勒定理

*导数是一个极限；中值定理是把它转化为整体信息的定理；泰勒定理量化了多项式逼近的误差。*

**定义 —— 导数**

$$f'(a)=\lim_{h\to 0}\frac{f(a+h)-f(a)}{h},$$

*当此极限存在时。可微性严格强于连续性，正如下一个结果所示。*

**证明 —— 可微 $\Rightarrow$ 连续**

1. 假设 $f'(a)$ 存在。对 $x\ne a$ 写

   $$f(x)-f(a)=\frac{f(x)-f(a)}{x-a}\cdot(x-a).$$
2. 当 $x\to a$ 时，第一个因子 $\to f'(a)$，第二个 $\to 0$；由极限的乘积法则，乘积 $\to f'(a)\cdot 0=0$。
3. 因此 $\lim_{x\to a}f(x)=f(a)$，即 $f$ 在 $a$ 处连续。

*逆命题不成立：$|x|$ 连续但在 0 处不可微；魏尔斯特拉斯函数*处处*连续却*处处*不可微。$\blacksquare$*

**定理 —— 罗尔定理与中值定理**

$$\textbf{Rolle: } f\in C[a,b],\ \text{diff. on }(a,b),\ f(a)=f(b)\ \Rightarrow\ \exists c:\ f'(c)=0.$$

$$\textbf{MVT: } \exists c\in(a,b):\ f'(c)=\frac{f(b)-f(a)}{b-a}.$$

**证明 —— 罗尔定理，再由它得到中值定理**

1. 罗尔：$f$ 在 $[a,b]$ 上连续，所以由最值定理它取得最大值和最小值。若两者都在端点取得，则 $f$ 为常数且 $f'\equiv 0$。否则某个极值在内点 $c$ 处取得。
2. 在内部极值处，单侧差商在极限中符号相反，迫使 $f'(c)=0$（费马内部极值引理）。

   $$f'(c)=0.$$
3. 中值定理：把罗尔定理应用于减去割线的辅助函数，它满足 $g(a)=g(b)=0$。罗尔给出 $c$ 使 $g'(c)=0$，即 $f'(c)=\dfrac{f(b)-f(a)}{b-a}$。

   $$g(x)=f(x)-\Big[f(a)+\frac{f(b)-f(a)}{b-a}(x-a)\Big],$$

*最值定理 $\to$ 费马 $\to$ 罗尔 $\to$ 中值定理：一条径直追溯到完备性的链条。$\blacksquare$*

**证明 —— 中值定理的推论：处处 $f'=0$ $\Rightarrow f$ 为常数**

1. 取区间内任意 $x_1\lt x_2$。在 $[x_1,x_2]$ 上应用中值定理：存在 $c$ 使

   $$f(x_2)-f(x_1)=f'(c)\,(x_2-x_1).$$
2. 由于 $f'(c)=0$，右端为 $0$，所以 $f(x_2)=f(x_1)$。由于 $x_1,x_2$ 任意，$f$ 为常数。

*这正是为什么每个原函数中都出现"$+C$"——同一函数的两个原函数相差一个常数。$\blacksquare$*

**定理 —— 带拉格朗日余项的泰勒定理**

$$f(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k+R_n,\qquad R_n=\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}$$

*其中 $\xi$ 介于 $a$ 与 $x$ 之间，假设 $f$ 是 $(n+1)$ 次可微的。余项是一个*精确*的误差，而 $n=0$ 恰好就是中值定理。*

> **概念 —— 泰勒是高阶的中值定理**
>
> 泰勒定理用与中值定理相同的手法证明：减去 $n$ 次泰勒多项式，构造一个在 $a$ 和 $x$ 处高阶为零的辅助函数，并反复应用罗尔定理（或柯西中值定理）。拉格朗日余项是最后一次应用所剩下的——把 $f'(c)$ 推广为 $f^{(n+1)}(\xi)$。

> **联系 —— 你曾信赖的误差界**
>
> 当你用 $\sin x\approx x-\tfrac{x^3}{6}$ 近似并宣称"误差极小"时，拉格朗日余项就是那个严格的界：$|R_n|\le\dfrac{\max|f^{(n+1)}|}{(n+1)!}|x-a|^{n+1}$。正是它使泰勒级数值得信赖，而不只是形式上的。

## 第 C 部分 · 积分、级数及更远处

<a id="s8"></a>
### 黎曼积分：达布和与可积性判别准则

*"曲线下的面积"成为一个被夹在高估与低估之间的精确数。积分恰好在这道夹逼闭合时存在。*

**定义 —— 达布上和与下和**

$$L(f,P)=\sum_{i} m_i\,\Delta x_i,\quad U(f,P)=\sum_{i} M_i\,\Delta x_i,\quad m_i=\inf_{[x_{i-1},x_i]}f,\ M_i=\sup_{[x_{i-1},x_i]}f$$

*这里 $P$ 是 $[a,b]$ 的一个分割。$L$ 低估、$U$ 高估面积，在每个子区间上使用真正的下/上确界。*

**定义 —— 黎曼（达布）积分**

$$\underline{\int_a^b} f=\sup_P L(f,P),\qquad \overline{\int_a^b} f=\inf_P U(f,P).$$

$$f \text{ is integrable} \iff \underline{\int_a^b} f=\overline{\int_a^b} f,\ \text{the common value } \int_a^b f.$$

*加细一个分割会抬高 $L$ 并压低 $U$；下积分绝不超过上积分。可积意味着这道间隙可以被驱至零。*

**定理 —— 黎曼判别准则**

$$f \text{ integrable on } [a,b] \iff \forall\varepsilon>0\ \exists\text{ partition } P:\ U(f,P)-L(f,P)\lt\varepsilon.$$

**证明 —— $[a,b]$ 上每个连续 $f$ 都可积**

1. 由海涅–康托尔（第 6 节），$f$ 在 $[a,b]$ 上一致连续。固定 $\varepsilon>0$ 并选 $\delta$ 使 $|x-y|\lt\delta\Rightarrow|f(x)-f(y)|\lt\dfrac{\varepsilon}{b-a}$。
2. 取任意一个所有子区间宽度都 $\lt\delta$ 的分割。在每个子区间上，$M_i-m_i=\sup-\inf\le\dfrac{\varepsilon}{b-a}$（由最值定理，上下确界在相距 $\delta$ 之内的点处取得）。
3. 那么

   $$U(f,P)-L(f,P)=\sum_i (M_i-m_i)\,\Delta x_i\le\frac{\varepsilon}{b-a}\sum_i\Delta x_i=\frac{\varepsilon}{b-a}\cdot(b-a)=\varepsilon.$$
4. 由黎曼判别准则，$f$ 可积。

*一致连续性恰恰是让*一个*网格尺度就能同时控制处处振荡的东西。$\blacksquare$*

> **概念 —— 什么东西不可积**
>
> 狄利克雷函数（在有理数上为 1，在无理数上为 0）在每个分割上都有 $L=0$ 但 $U=b-a$，因为每个子区间都同时含有两类点——所以它*不是*黎曼可积的。黎曼可积性要求间断点"很小"（由勒贝格判别准则，测度为零）。这一局限引出第 13 节。

<a id="s9"></a>
### 微积分基本定理，加以证明

*这个定理把微积分的两半熔为一体：积分和微分是互逆的运算。两个方向都给出证明。*

**基本定理 —— 第一部分（对积分求导）**

$$f \text{ continuous on } [a,b],\quad F(x)=\int_a^x f(t)\,dt\ \Rightarrow\ F'(x)=f(x).$$

**证明 —— 基本定理第一部分**

1. 构造差商并利用积分的可加性：

   $$\frac{F(x+h)-F(x)}{h}=\frac1h\int_x^{x+h} f(t)\,dt.$$
2. 设 $m_h,M_h$ 为 $f$ 在 $[x,x+h]$ 上的最小值与最大值（由最值定理存在）。那么 $m_h\,h\le\int_x^{x+h}f\le M_h\,h$，所以除以 $h\gt 0$：

   $$m_h\le\frac{F(x+h)-F(x)}{h}\le M_h.$$
3. 当 $h\to 0$ 时，连续性迫使 $m_h\to f(x)$ 且 $M_h\to f(x)$。由夹逼定理，差商 $\to f(x)$，即 $F'(x)=f(x)$。

*每个连续函数都*拥有*一个原函数——也就是它自己的变上限积分。$\blacksquare$*

**基本定理 —— 第二部分（计算积分）**

$$G'=f \text{ on } [a,b],\ f \text{ integrable}\ \Rightarrow\ \int_a^b f(x)\,dx=G(b)-G(a).$$

**证明 —— 用中值定理证明基本定理第二部分**

1. 取任意分割 $a=x_0\lt x_1\lt\cdots\lt x_n=b$。裂项相消：

   $$G(b)-G(a)=\sum_{i=1}^{n}\big(G(x_i)-G(x_{i-1})\big).$$
2. 在每个 $[x_{i-1},x_i]$ 上对 $G$ 应用中值定理：存在 $c_i$ 使 $G(x_i)-G(x_{i-1})=G'(c_i)\,\Delta x_i=f(c_i)\,\Delta x_i$。
3. 于是 $G(b)-G(a)=\sum f(c_i)\,\Delta x_i$，一个黎曼和，被夹在 $L(f,P)$ 与 $U(f,P)$ 之间：

   $$L(f,P)\le G(b)-G(a)\le U(f,P).$$
4. 由于 $f$ 可积，加细 $P$ 把两个界都夹向 $\int_a^b f$。常量 $G(b)-G(a)$ 被困在中间，所以它等于 $\int_a^b f$。

*中值定理（因而完备性）是枢纽：它把 $G$ 的增量转化为 $f$ 的样本。$\blacksquare$*

> **联系 —— "求出原函数，代入端点"**
>
> 你从第一天起就在用的计算规则 $\int_a^b f = G(b)-G(a)$ *就是*基本定理第二部分。第一部分是它沉默的伙伴：它首先保证原函数 $G$ 对任何连续 $f$ 都存在，所以那条规则总有可施之处。

<a id="s10"></a>
### 函数序列与函数项级数：逐点收敛 vs 一致收敛

*当一个极限本身是一个函数时，它"如何"收敛极其重要。逐点与一致的区别正是天真的微积分崩溃之处。*

**定义 —— 逐点收敛**

$$f_n\to f \text{ pointwise} \iff \forall x\ \forall\varepsilon>0\ \exists N(x,\varepsilon):\ n\ge N\Rightarrow|f_n(x)-f(x)|\lt\varepsilon.$$

*这里 $N$ 可以依赖于 $x$——不同的点可能以截然不同的速率收敛。*

**定义 —— 一致收敛**

$$f_n\to f \text{ uniformly} \iff \forall\varepsilon>0\ \exists N\ \forall x\ \forall n\ge N:\ |f_n(x)-f(x)|\lt\varepsilon.$$

$$\text{equivalently}\quad \sup_x|f_n(x)-f(x)|\to 0.$$

*同一个 $N$ 同时对*所有*$x$ 都有效——$f_n$ 的整条图像都落在 $f$ 周围一条 $\varepsilon$ 带状区域里。量词的顺序就是一切：一致收敛把"$\exists N$"挪到了"$\forall x$"之前。*

> **概念 —— 警示性的例子**
>
> 在 $[0,1]$ 上，$f_n(x)=x^n$ 逐点收敛到 $f(x)=0$（对 $x\lt 1$）和 $f(1)=1$——这是连续函数的一个**不连续**极限。该收敛*不是*一致的：靠近 $x=1$ 时你总需要更大的 $n$。逐点收敛不保持连续性；一致收敛则保持。

**定理 —— 魏尔斯特拉斯 M 判别法**

$$|f_n(x)|\le M_n\ \forall x,\quad \sum_n M_n\lt\infty\ \Rightarrow\ \sum_n f_n \text{ converges uniformly (and absolutely).}$$

*一个由界组成的收敛数项级数迫使函数项级数一致收敛——这是证明幂级数一致收敛的日常工具。*

**证明 —— M 判别法（借助一致收敛的柯西判别准则）**

1. 令 $S_n=\sum_{k=1}^n f_k$。对 $m\gt n$ 和任意 $x$：

   $$|S_m(x)-S_n(x)|=\Big|\sum_{k=n+1}^{m} f_k(x)\Big|\le\sum_{k=n+1}^{m}|f_k(x)|\le\sum_{k=n+1}^{m} M_k.$$
2. 由于 $\sum M_k$ 收敛，其尾部 $\to 0$：给定 $\varepsilon>0$ 存在 $N$ 使对所有 $m\gt n\ge N$ 有 $\sum_{k=n+1}^{m}M_k\lt\varepsilon$——一个不依赖于 $x$ 的界。
3. 因此 $\sup_x|S_m(x)-S_n(x)|\lt\varepsilon$：部分和是一致柯西的，所以它们一致收敛到某个 $S$。

*数项的尾部一致地控制了函数项的尾部。$\blacksquare$*

<a id="s11"></a>
### 一致收敛的推论

*一致收敛恰恰是把极限与连续性、积分以及（小心地）微分交换次序所需的强度。*

**定理 —— 连续函数的一致极限仍连续**

$$f_n \text{ continuous},\ f_n\to f \text{ uniformly}\ \Rightarrow\ f \text{ continuous.}$$

**证明 —— 连续性被保持（$\varepsilon/3$ 论证）**

1. 固定 $a$ 与 $\varepsilon>0$。由一致收敛取 $n$ 使 $\sup_x|f_n(x)-f(x)|\lt\tfrac{\varepsilon}{3}$。
2. 该 $f_n$ 在 $a$ 处连续：取 $\delta$ 使 $|x-a|\lt\delta\Rightarrow|f_n(x)-f_n(a)|\lt\tfrac{\varepsilon}{3}$。
3. 经由 $f_n$ 把目标拆开：对 $|x-a|\lt\delta$，

   $$|f(x)-f(a)|\le|f(x)-f_n(x)|+|f_n(x)-f_n(a)|+|f_n(a)-f(a)|\lt\tfrac{\varepsilon}{3}+\tfrac{\varepsilon}{3}+\tfrac{\varepsilon}{3}=\varepsilon.$$

*外侧的两个三分之一需要一致性（同一个 $n$ 对所有 $x$）；中间的三分之一只是普通的连续性。$\blacksquare$*

**定理 —— 极限与积分的交换**

$$f_n\to f \text{ uniformly on } [a,b],\ f_n \text{ integrable}\ \Rightarrow\ \int_a^b f_n\to\int_a^b f.$$

**证明 —— 一致收敛允许逐项积分**

1. 令 $\varepsilon_n=\sup_x|f_n(x)-f(x)|$。一致收敛意味着 $\varepsilon_n\to 0$。（可证 $f$ 也可积；为做估计先假设之。）
2. 用差的积分给积分之差定界：

   $$\Big|\int_a^b f_n-\int_a^b f\Big|=\Big|\int_a^b (f_n-f)\Big|\le\int_a^b |f_n-f|.$$
3. 逐点使用一致界 $|f_n-f|\le\varepsilon_n$：

   $$\int_a^b|f_n-f|\le\varepsilon_n\,(b-a)\ \longrightarrow\ 0.$$

*$\sup$ 界 $\varepsilon_n$ 乘以区间长度控制了整个积分。逐点收敛*不够*——移动的"尖峰"函数逐点收敛到 0，却始终保持面积为 1。$\blacksquare$*

**定理 —— 对极限求导（微妙的情形）**

$$f_n\to f \text{ pointwise},\ f_n' \text{ continuous},\ f_n'\to g \text{ uniformly}\ \Rightarrow\ f'=g.$$

*微分*不*与 $f_n$ 的仅仅一致收敛交换次序；你必须假设**导数**一致收敛。证明：对 $f_n'\to g$ 积分（前一个定理），再应用微积分基本定理。*

> **联系 —— 何时"交换次序"是合法的**
>
> 随意地交换 $\lim$ 与 $\int$ 或 $\frac{d}{dx}$，或逐项对级数求和，*恰恰*由一致收敛来保证其正当性。早期微积分中那些著名的交换失败案例，全都是收敛仅为逐点的情形。

<a id="s12"></a>
### 幂级数与解析函数

*幂级数是行为最良好的无穷和——在它们的圆盘内部它们在紧集上一致收敛，并且可以自由地逐项求导和积分。*

**定义与定理 —— 收敛半径**

$$\sum_{n=0}^{\infty} c_n (x-a)^n,\qquad \frac1R=\limsup_{n\to\infty}|c_n|^{1/n}\quad(\text{Cauchy–Hadamard}).$$

*级数对 $|x-a|\lt R$ 绝对收敛，对 $|x-a|\gt R$ 发散。对 $\limsup$ 的使用（第 4 节）正是使 $R$ 总是良定义的东西。*

**证明 —— 在半径内收敛，且在紧集上一致收敛**

1. 固定 $r\lt R$。取 $\rho$ 使 $r\lt\rho\lt R$；则 $\limsup|c_n|^{1/n}\lt 1/\rho$，所以对充分大的 $n$，$|c_n|^{1/n}\lt 1/\rho$，即 $|c_n|\lt\rho^{-n}$。
2. 对 $|x-a|\le r$：$|c_n(x-a)^n|\le|c_n|r^n\lt (r/\rho)^n=:M_n$，而 $\sum M_n$ 是一个收敛的几何级数，因为 $r/\rho\lt 1$。
3. 由魏尔斯特拉斯 M 判别法（第 10 节），幂级数在 $\{|x-a|\le r\}$ 上一致收敛：

   $$\sum |c_n(x-a)^n|\le\sum (r/\rho)^n=\frac{1}{1-r/\rho}\lt\infty.$$

*在每一个闭子圆盘上的一致收敛，正是下面所有美妙运算的许可。$\blacksquare$*

> **定理 —— 逐项微积分**
>
> 在 $|x-a|\lt R$ 内部，一个幂级数定义了一个无穷可微的函数；它可以**逐项求导和积分**，且所得级数有相同的半径 $R$。因此 $c_n=\dfrac{f^{(n)}(a)}{n!}$：该级数就是它自己的泰勒级数。这由第 11 节应用于每个收敛为一致的闭子圆盘得出。

> **概念 —— 解析，以及为何 $C^\infty\ne$ 解析**
>
> 一个函数在 $a$ 处**解析**，如果它在 $a$ 附近等于一个收敛幂级数。解析 $\Rightarrow C^\infty$，但反之不然：$f(x)=e^{-1/x^2}$（取 $f(0)=0$）光滑，却在 0 处*所有*导数都为零，所以它的泰勒级数是 $0$，并不表示 $f$。光滑性弱于解析性。

> **联系 —— 泰勒级数，终于被证成**
>
> 写出 $e^x=\sum x^n/n!$ 或 $\sin x=\sum(-1)^n x^{2n+1}/(2n+1)!$ 并逐项操作它们——求导、积分、相乘——之所以严格，恰恰是因为幂级数在紧集上一致收敛。第 7 节的余项估计告诉你泰勒级数*何时*真的收敛回 $f$。

<a id="s13"></a>
### 一瞥更远处：度量空间、多元严格化与勒贝格

*同样的 $\varepsilon$ 思想远远推广到实数轴之外。一段简短的游览，看看分析接下来去往何方。*

**度量空间 —— 抽象距离**

$$d(x,y)\ge 0,\ \ d(x,y)=0\iff x=y,\ \ d(x,y)=d(y,x),\ \ d(x,z)\le d(x,y)+d(y,z).$$

*把 $|x-y|$ 换成任何满足这些公理的函数 $d$，每一个 $\varepsilon$ 定义都逐字转移过来：极限、连续性、柯西数列、紧性。$\mathbb{R}^n$、函数空间和序列空间全都成为同样定理的舞台。*

> **概念 —— 抽象的完备性与压缩原理**
>
> 一个度量空间是**完备的**，如果每个柯西数列都收敛——这是第 3 节那个关于 $\mathbb{R}$ 的定理的抽象版本。在一个完备空间中，**巴拿赫不动点定理**保证一个压缩映射 $d(Tx,Ty)\le k\,d(x,y)$（$k\lt 1$）有唯一的不动点。这单单一个结果就证明了微分方程的存在唯一性（皮卡–林德勒夫）以及反函数定理。

> **概念 —— 多元严格化**
>
> 在 $\mathbb{R}^n$ 中，导数成为一个**线性映射**（全导数 / 雅可比矩阵）：$f(a+h)=f(a)+Df(a)\,h+o(\|h\|)$。偏导数存在*不足以*保证可微；还需要它们连续。中值定理弱化为一个不等式，而隐函数定理和反函数定理——经由压缩原理证明——取代了一元情形的代数。

> **概念 —— 勒贝格积分**
>
> 黎曼积分在严重不连续的函数上卡壳（狄利克雷函数，第 8 节），并且在取极限时表现糟糕。**勒贝格的**想法：分割*值域*，而非定义域，并测量有多少定义域被映入每一个值域切片。这能积分远多得多的函数，并产生干净的收敛定理（单调收敛与控制收敛），在温和的假设下 $\lim\int=\int\lim$ 成立——修复了把极限与黎曼积分交换次序的脆弱性。

> **联系 —— 一个思想，无尽重用**
>
> 从数列的 $\varepsilon$–$N$，到函数的 $\varepsilon$–$\delta$，到度量空间中的 $d(x,y)$，再到测度论的积分——它都是*同一个*动作：把一个量控制在任何预先指定的容差之内。掌握那一个习惯，那么整个分析，无论多么抽象，都是熟悉的领地。

---

*一门严格的实分析入门课程——《完整微积分》和《从零导出》两本指南之下的理论。每个极限都是一个 $\varepsilon$；每个定理都从 $\mathbb{R}$ 的完备性出发被证明。先通读一遍把握整体架构，之后把任意一个证明方框当作参考随时回看。记住那唯一的脉络：把任何量控制在任何容差之内，无穷便变得安全。*
