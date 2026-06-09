[English](symplectic-geometry.md) · **中文**

# 辛几何与几何量子化，*相空间的几何学。*

*本文自成体系、严谨地讲述隐藏在经典力学内部的几何，以及这种几何如何转化为量子力学。我们从辛形式的纯代数出发——一个反对称、非退化的配对——并一步步构建辛流形、作为哈密顿动力学天然舞台的余切丛、泊松括号、对称性与约化，最终抵达从经典相空间构造希尔伯特空间的几何量子化纲领。几何是目标，物理是动机；每一个公式都被推导，每一个符号都被解释。*

[← 返回全部指南](../README.zh.md)

**预备知识。** 本指南假定读者已掌握 **微分几何与张量** 指南（光滑流形、切空间与余切空间、向量场、微分形式、外微分 $d$、楔积 $\wedge$、内积 $\iota_X$、李导数 $\mathcal{L}_X$，以及嘉当魔法公式 $\mathcal{L}_X = d\,\iota_X + \iota_X\, d$）以及 **变分法** 指南（作用量泛函、欧拉–拉格朗日方程，以及从拉格朗日量 $L(q,\dot q)$ 过渡到哈密顿量 $H(q,p)$ 的勒让德变换）。我们会在每一处用到具体事实时重新陈述它。

## 第 A 部分 · 线性与光滑理论

<a id="s0"></a>
### 动机 —— 哈密顿力学就是相空间上的微分几何

辛几何是 *相空间* 的数学：相空间中的每个点是某个力学系统的完整瞬时状态。本指南的核心论断是，哈密顿力学的规则并非一堆需要死记硬背的公式，而是单一几何对象——一个闭的、非退化的 $2$-形式 $\omega$——的展开，而量子力学可以建立在同一个对象之上。

#### 我们要解决什么问题？

在初等力学中，一维粒子的状态是一对量：它的位置 $q$ 和动量 $p$。这一对 $(q,p)$ 是二维空间中的一个点，我们称之为 **相空间**。哈密顿运动方程写作

$$
\dot q = \frac{\partial H}{\partial p},\qquad \dot p = -\frac{\partial H}{\partial q},
$$

其中 $H(q,p)$ 是 **哈密顿量**，即用位置与动量表示的总能量，而点号表示对时间求导。这两个方程有一个引人注目的不对称性：一个带加号，另一个带减号。这种反对称性正是 $2$-形式的指纹。哈密顿力学的全部内容可以一句话概括为：*相空间上存在一个反对称配对 $\omega = dq\wedge dp$，运动是由 $\iota_{X_H}\omega = dH$ 定义的向量场 $X_H$ 的流。* 那个减号正是由 $\omega$ 的反对称性所强制的。

有两个结构性事实使这值得发展成一整门几何：

1. **配对是反对称的，而非对称的。** 度量（内积）是一个 *对称的* 非退化双线性形式；它度量长度与角度。辛形式是一个 *反对称的* 非退化双线性形式；它度量 $(q,p)$-平面中的 *有向面积*。长度在力学中不起作用——只有面积（作用量）才起作用。
2. **配对是闭的。** 条件 $d\omega = 0$ 恰好使得流保持 $\omega$，并迫使泊松括号满足雅可比恒等式。闭性是“能量守恒是自洽的”这一事实的几何编码。

#### 计划

我们按顺序构建：**辛向量空间**（线性代数，s1）；**辛流形** 以及说明它们局部看起来都标准的 **达布定理**（s2）；作为典范相空间、带有 **重言** 与 **典范** 形式的 **余切丛** $T^*Q$（s3）；**哈密顿向量场** 与 **泊松括号**，并从 $d\omega=0$ 出发证明雅可比恒等式（s4）；**辛同胚** 与正则变换（s5）；**矩映射**、几何版诺特定理，以及 **马斯登–韦恩斯坦约化**（s6）；**拉格朗日子流形**（s7）；连通向复几何的 **概复结构与凯勒结构**（s8）；**预量子化**（s9）；正式的 **几何量子化**（s10）；以及一个完整的 **范例**，量子化谐振子与 $2$-球面（s11）。

> **直觉。** 度量告诉你两个状态相距多远。辛形式告诉你两个状态如何 *交易*：位置上的位移如何与动量上的位移配对而产生一个数（一块面积）。力学就是这种交易的几何学。

<a id="s1"></a>
### 辛向量空间；标准辛形式；辛结构与内积结构的对比

在讨论流形之前，我们需要逐点的线性代数。流形上的辛结构在每一点处都是切空间上的一个辛结构——因此我们先理解一个向量空间。

#### 定义与非退化条件

> **定义 —— 辛向量空间。**
>
> 设 $V$ 是一个有限维实向量空间。$V$ 上的 **辛形式** 是一个映射 $\omega: V\times V\to\mathbb{R}$，它满足
> - **双线性**：对每个变量分别是线性的；
> - **反对称**（也称 **交替** 或 **斜对称**）：对所有 $u,v\in V$ 有 $\omega(u,v) = -\,\omega(v,u)$（等价于 $\omega(v,v)=0$）；
> - **非退化**：若对 *所有* $v\in V$ 都有 $\omega(u,v)=0$，则 $u=0$。
>
> 序对 $(V,\omega)$ 称为 **辛向量空间**。

这里“双线性”意味着对标量 $a,b\in\mathbb{R}$ 有 $\omega(au+bw,v)=a\,\omega(u,v)+b\,\omega(w,v)$，第二个变量位置同理。“非退化”表示没有非零向量对配对是不可见的：线性映射 $\flat:V\to V^*$，$u\mapsto \omega(u,\cdot)$（把 $u$ 送到余向量 $v\mapsto\omega(u,v)$），具有平凡核，因而是一个同构，因为 $V$ 与其对偶 $V^*$ 维数相等。

#### 辛形式迫使维数为偶

> **命题。** 辛向量空间的维数是偶数。

**证明。**
1. 任取 $V$ 的一组基，令 $A$ 为元素 $A_{ij}=\omega(e_i,e_j)$ 构成的矩阵，其中 $\{e_i\}$ 是该基。*理由：* 双线性形式由它在基上的取值决定，而这些取值汇集成一个矩阵。
2. 反对称性 $\omega(e_i,e_j)=-\omega(e_j,e_i)$ 给出 $A^{\mathsf T}=-A$，即 $A$ 是反对称矩阵。*理由：* 转置交换了 $i$ 与 $j$ 的角色。
3. 对一个 $n\times n$ 矩阵，恒有 $\det(A^{\mathsf T})=\det(A)$，而把标量 $-1$ 从 $n$ 列中的每一列提出可得 $\det(-A)=(-1)^n\det(A)$。*理由：* 行列式关于列是多重线性的，且转置不改变行列式。
4. 综合第 2–3 步：$\det(A)=\det(A^{\mathsf T})=\det(-A)=(-1)^n\det(A)$，于是 $\big(1-(-1)^n\big)\det(A)=0$。
5. 非退化性迫使 $\det(A)\ne 0$：若 $\det A=0$，则存在非零向量 $u$ 使 $A u = 0$，意味着对所有 $j$ 有 $\omega(u,e_j)=0$，由双线性进而对所有 $v$ 有 $\omega(u,v)=0$，与非退化性矛盾。*理由：* 奇异矩阵有非平凡核。
6. 既然 $\det(A)\ne 0$，第 4 步迫使 $1-(-1)^n=0$，于是 $(-1)^n=1$，故 $n$ 为偶数。$\blacksquare$

我们记 $\dim V = 2n$。

#### 标准辛形式与辛基

> **定义 —— $\mathbb{R}^{2n}$ 上的标准辛形式。**
>
> 在带有坐标 $(q^1,\dots,q^n,p_1,\dots,p_n)$ 的 $\mathbb{R}^{2n}$ 上，**标准辛形式** 为
> $$
> \omega_0 \;=\; \sum_{i=1}^n dq^i\wedge dp_i,
> $$
> 它作用在两个向量 $u=(a^i,b_i)$ 与 $v=(c^i,d_i)$ 上为 $\omega_0(u,v)=\sum_i (a^i d_i - b_i c^i)$。

用矩阵形式写作 $\omega_0(u,v)=u^{\mathsf T} J\, v$，其中 $2n\times 2n$ 的分块矩阵为
$$
J=\begin{pmatrix} 0 & I_n \\ -I_n & 0\end{pmatrix},
$$
此处 $I_n$ 是 $n\times n$ 单位矩阵。容易验证 $J^{\mathsf T}=-J$（反对称）以及 $\det J = 1\ne 0$（非退化），故 $(\mathbb{R}^{2n},\omega_0)$ 是辛向量空间。

> **定理 —— 线性达布 / 辛基。** 每个 $2n$ 维辛向量空间 $(V,\omega)$ 都有一组基 $e_1,\dots,e_n,f_1,\dots,f_n$——称为 **辛基**——使得
> $$
> \omega(e_i,e_j)=0,\quad \omega(f_i,f_j)=0,\quad \omega(e_i,f_j)=\delta_{ij},
> $$
> 其中 $\delta_{ij}$ 在 $i=j$ 时为 $1$，否则为 $0$。在此基下 $\omega$ 恰为 $\omega_0$。因此所有同维的辛向量空间都是同构的。

**证明（对 $n$ 归纳，格拉姆–施密特法的类比）。**
1. 若 $V=\{0\}$ 则无需证明；设 $\dim V=2n\ge 2$。任取非零 $e_1\in V$。*理由：* 非零空间有非零向量。
2. 由非退化性存在 $w$ 使 $\omega(e_1,w)\ne 0$；重新标度令 $f_1:=w/\omega(e_1,w)$，于是 $\omega(e_1,f_1)=1$。*理由：* 非退化性表明 $\omega(e_1,\cdot)$ 不是零余向量。
3. 注意 $e_1,f_1$ 线性无关：若 $f_1=\lambda e_1$，则由反对称性 $\omega(e_1,f_1)=\lambda\,\omega(e_1,e_1)=0$，与 $\omega(e_1,f_1)=1$ 矛盾。*理由：* 反对称性给出 $\omega(e_1,e_1)=0$。
4. 令 $W=\mathrm{span}\{e_1,f_1\}$，并定义其 **辛正交补** $W^\omega=\{v\in V: \omega(v,e_1)=0\text{ 且 }\omega(v,f_1)=0\}$。任意 $v\in V$ 唯一地分解为 $v = \big(\omega(v,f_1)\,e_1 - \omega(v,e_1)\,f_1\big) + v'$，其中 $v'\in W^\omega$；对括号内的项直接计算 $\omega(\cdot,e_1)$ 与 $\omega(\cdot,f_1)$ 可重现 $v$ 的相应值，故 $v'\in W^\omega$。*理由：* 括号内的向量被特意构造成与 $v$ 对 $e_1,f_1$ 有相同的配对。
5. 因此 $V=W\oplus W^\omega$ 为直和，而 $\omega$ 限制在 $W^\omega$ 上仍非退化（$W^\omega$ 中一个向量若与整个 $W^\omega$ 平凡配对、又按定义与 $W$ 平凡配对，则它与整个 $V$ 平凡配对，从而为零）。$\dim W^\omega = 2n-2$。*理由：* 非退化性下降到补空间。
6. 由归纳假设，$W^\omega$ 有辛基 $e_2,\dots,e_n,f_2,\dots,f_n$。添上 $e_1,f_1$ 即得 $V$ 的辛基。$\blacksquare$

#### 辛结构与内积结构：鲜明的对比

**内积** $g$ 是一个 *对称的* 非退化双线性形式，且对 $v\ne 0$ 有 $g(v,v)>0$（正定）。两者的差异并非表面修饰：

| 特征 | 内积 $g$ | 辛形式 $\omega$ |
|---|---|---|
| 对称性 | $g(u,v)=g(v,u)$ | $\omega(u,v)=-\omega(v,u)$ |
| 自配对 | $g(v,v)>0$ 度量长度${}^2$ | 恒有 $\omega(v,v)=0$ |
| 维数 | 任意 | 必为偶数 |
| 不变群 | 正交群 $O(n)$ | 辛群 $Sp(2n,\mathbb{R})$ |
| 局部标准型 | 需要特征值（弯曲的 $g$ 无平坦标准型） | 总是恰为 $\omega_0$（达布） |

$\omega(v,v)=0$ 这一行是核心所在：辛形式无法度量单个向量的“大小”，只能度量两个向量如何 *展开* 成一块有向面积。上面那个矩阵 $J$ 的平方为 $J^2=-I$，这是我们在 s8 中利用的复结构的种子。

> **范例 —— 平面中的有向面积。** 取 $V=\mathbb{R}^2$，$\omega_0=dq\wedge dp$，两个向量 $u=(3,1)$（即 $3\,\partial_q+1\,\partial_p$）与 $v=(1,2)$。则 $\omega_0(u,v)=a^1 d_1 - b_1 c^1 = 3\cdot 2 - 1\cdot 1 = 5$。从几何上看，这是由 $u$ 与 $v$ 张成的平行四边形的有符号面积——与叉积所计算的同一个 $2\times 2$ 行列式 $\det\left(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\right)=5$。交换输入会翻转符号：$\omega_0(v,u)=-5$，这确认了反对称性。而 $\omega_0(u,u)=3\cdot1-1\cdot3=0$：一个向量与自身张不出面积。与之对照，欧氏内积 $g(u,u)=3^2+1^2=10\ne0$，它度量的是长度平方。这一个数值例子就是两种结构之间全部的概念差异。

> **辛群。** 保持 $\omega$ 的线性映射 $T:V\to V$（即 $\omega(Tu,Tv)=\omega(u,v)$）构成 **辛群** $Sp(2n,\mathbb{R})$。在标准基下，$T$ 为辛的当且仅当 $T^{\mathsf T}JT=J$。对此关系取行列式并利用 $\det J\ne0$，得 $\det(T)^2=1$；更精细的论证（普法夫值）实际上表明 $\det T=+1$，因此辛映射保持体积与定向——这是刘维尔定理（s5）的线性投影。

<a id="s2"></a>
### 辛流形；非退化闭 2-形式；达布定理

我们现在把辛形式光滑地铺展在流形上。超出线性理论的新成分是一个 *微分* 条件——闭性——它没有线性代数中的类比。

#### 定义

> **定义 —— 辛流形。**
>
> **辛流形** 是一对 $(M,\omega)$，其中 $M$ 是光滑流形，$\omega$ 是 **辛形式**：一个微分 $2$-形式（一个反对称的 $\binom{0}{2}$-张量场），满足
> - **非退化**：在每一点 $p\in M$，切空间 $T_pM$ 上的双线性形式 $\omega_p$ 在 s1 的意义下非退化；
> - **闭**：$d\omega = 0$，其中 $d$ 是外微分。

由 s1，非退化性迫使 $\dim M = 2n$ 为偶。$\omega$ 是 $2$-形式意味着它在每一点吞入两个切向量并反对称地返回一个数；“微分”意味着它随 $p$ 光滑变化。

> **为何要闭？** 回忆预备知识中的外微分 $d$，它把 $k$-形式送到 $(k+1)$-形式且满足 $d^2=0$。条件 $d\omega=0$ 有三个等价的回报，将在后文证明：(i) 哈密顿流保持 $\omega$（s5）；(ii) 泊松括号满足雅可比恒等式（s4）；(iii) 局部上 $\omega=d\theta$ 对某个 $1$-形式 $\theta$ 成立（庞加莱引理），称为 **辛势**。

#### 非退化映射与典范体积

非退化性在每一点给出同构 $\flat:T_pM\to T_p^*M$，$X\mapsto \iota_X\omega := \omega(X,\cdot)$。其逆记作 $\sharp$。这个 **音乐同构** 让我们把余向量（例如 $dH$）转化为向量（哈密顿场 $X_H$），这是全部力学背后的构造。

> **命题 —— 刘维尔体积。** 在 $2n$ 维辛流形上，最高次形式
> $$
> \omega^n := \underbrace{\omega\wedge\cdots\wedge\omega}_{n}
> $$
> 处处非零；它是一个体积形式，称为 **刘维尔体积**。

**证明。** 在某点选取辛基（s1），使 $\omega=\sum_i dq^i\wedge dp_i$。展开这个楔幂，每个含重复因子 $dq^i\wedge dp_i\wedge dq^i$ 的项都为零（重复的 $1$-形式楔积为零），只剩下完全混合的项；汇集这些项得 $\omega^n = n!\, dq^1\wedge dp_1\wedge\cdots\wedge dq^n\wedge dp_n$，这是标准体积的 $n!$ 倍，因而非零。*理由：* $2n$ 维中 $2n$ 个不同坐标 $1$-形式的楔积就是体积形式。$\blacksquare$

一个推论（预告 s5）：哈密顿流保持 $\omega$，从而保持 $\omega^n$——这就是 **刘维尔定理**，即相空间体积守恒。

> **范例 —— 哪些球面是辛的？** 刘维尔体积给出一个快速的拓扑障碍。若一个 *紧* 流形 $M^{2n}$ 是辛的，则 $\omega^n$ 是一个处处非零的最高次形式，其积分 $\int_M\omega^n\ne0$；因此在德拉姆上同调中上同调类 $[\omega^n]=[\omega]^n\ne0$，这迫使 $[\omega]\in H^2(M)$ 非零（零类的幂都为零）。对 $n\ge2$ 的 $S^{2n}$，上同调 $H^2(S^{2n})=0$，故不存在辛形式。具体地说：$S^2$ *是* 辛的（其面积形式），但 $S^4, S^6,\dots$ 则 *不是*。*理由：* 需要非零的 $[\omega]\in H^2$，而高维球面没有 $H^2$。这表明辛结构是一个真正的约束，并非在每个偶维流形上都能找到。

#### 达布定理

最令人惊讶的结构性事实是，与度量不同，辛形式 *没有局部不变量*：每个辛流形局部上都是标准的那个。

> **定理 —— 达布。** 设 $(M,\omega)$ 是 $2n$ 维辛流形，$p\in M$。在 $p$ 附近存在坐标卡 $(U;q^1,\dots,q^n,p_1,\dots,p_n)$，使得
> $$
> \omega = \sum_{i=1}^n dq^i\wedge dp_i.
> $$
> 这些称为 **达布**（或 **典范**）坐标。

**证明思路（莫泽形变技巧）。** 最干净的论证是在 $\omega$ 与一个常系数模型之间进行插值。
1. 对 $T_pM$ 应用线性达布定理（s1），选取线性坐标使 $\omega_p$ *在单点 $p$* 等于 $\omega_0=\sum dq^i\wedge dp_i$。令 $\omega_1:=\omega$，并让 $\omega_0$ 也表示坐标卡上的常系数形式 $\sum dq^i\wedge dp_i$。则 $\omega_0$ 与 $\omega_1$ 在 $p$ 处相等。*理由：* 线性标准型确定了在一点的值。
2. 考虑族 $\omega_t=(1-t)\omega_0+t\,\omega_1$，$t\in[0,1]$。每个 $\omega_t$ 都是闭的（闭形式的组合），且在 $p$ 附近非退化（它在 $p$ 处等于 $\omega_0$，而非退化是开条件），故每个 $\omega_t$ 在一个小邻域上都是辛的。*理由：* 非退化即 $\omega_t^n$ 不为零，这是开条件。
3. 差 $\omega_1-\omega_0$ 是闭的且在 $p$ 处为零；由庞加莱引理，它等于 $d\sigma$，其中 $1$-形式 $\sigma$ 可选取为在 $p$ 处为零。*理由：* 闭形式局部上是恰当的。
4. **莫泽方程。** 寻找一个含时向量场 $X_t$ 使 $\iota_{X_t}\omega_t=-\sigma$；$\omega_t$ 的非退化性让我们通过 $\sharp$ 唯一地解出 $X_t$。设 $\psi_t$ 为其流。则由嘉当公式 $\frac{d}{dt}(\psi_t^*\omega_t)=\psi_t^*\big(\mathcal{L}_{X_t}\omega_t + \tfrac{d}{dt}\omega_t\big)=\psi_t^*\big(d\,\iota_{X_t}\omega_t + (\omega_1-\omega_0)\big)=\psi_t^*\big(-d\sigma + d\sigma\big)=0$。*理由：* 嘉当魔法公式 $\mathcal{L}_X=d\iota_X+\iota_X d$ 以及 $d\omega_t=0$。
5. 因此 $\psi_t^*\omega_t$ 关于 $t$ 是常数，故 $\psi_1^*\omega_1=\psi_0^*\omega_0=\omega_0$。微分同胚 $\psi_1$ 把 $\omega$ 拉回到 $\omega_0$；用它来定义坐标即得达布卡。$\blacksquare$

> **范例 —— 球面上显式的达布卡。** 取 $S^2$（半径 $1$），面积形式 $\omega=\sin\phi\,d\phi\wedge d\theta$，其中 $\phi\in(0,\pi)$ 是极角，$\theta\in(0,2\pi)$ 是方位角。设新坐标 $q:=\theta$ 与 $p:=-\cos\phi$（于是 $p\in(-1,1)$，即高度）。则 $dp = \sin\phi\,d\phi$，故 $dq\wedge dp = d\theta\wedge(\sin\phi\,d\phi) = -\sin\phi\,d\phi\wedge d\theta = -\omega$，于是 $\omega = dp\wedge dq = dq\wedge d(-p)$；把 $p\mapsto -p$ 重新标记即得干净的达布形式 $\omega = dq\wedge dp$。这对 $(\theta,-\cos\phi)$ 是货真价实的典范坐标——阿基米德定理说球面的圆柱投影保持面积，这恰恰就是这些坐标把 $\omega$ 化为标准形式这一陈述。

> **陷阱。** 达布定理 *并不* 说辛流形整体上是平凡的。带面积形式的球面 $S^2$ 是辛的且局部标准，但整体上不同于 $\mathbb{R}^2$（它是紧的，总面积有限）。所有有趣的辛不变量都是整体性的。

<a id="s3"></a>
### 余切丛作为典范相空间；重言形式与典范形式

力学中辛形式从何而来？答案是自动的：*任何* 位形空间在其余切丛上都自带一个典范辛结构。

#### 余切丛作为相空间

> **设置。** 设 $Q$ 是一个光滑 $n$-流形，即 **位形空间**（位置 $q$）。其 **余切丛** $T^*Q=\{(q,p): q\in Q,\ p\in T_q^*Q\}$ 把每个位置与该处的一个余向量 $p$ 收集在一起——物理上即动量。$Q$ 上的局部坐标 $q^i$ 在 $T^*Q$ 上诱导坐标 $(q^i,p_i)$，其中 $p=\sum_i p_i\,dq^i$。这个 $2n$ 维流形就是 **相空间**。

丛投影为 $\pi:T^*Q\to Q$，$\pi(q,p)=q$，其导数为 $d\pi:T_{(q,p)}(T^*Q)\to T_qQ$。

#### 重言一形式

> **定义 —— 重言（刘维尔）一形式。** 在 $T^*Q$ 上的点 $(q,p)$ 处定义 $1$-形式 $\theta$ 为
> $$
> \theta_{(q,p)}(X) := p\big(d\pi(X)\big),\qquad X\in T_{(q,p)}(T^*Q).
> $$
> 用语言说：通过 $d\pi$ 把切向量 $X$ 下推到 $Q$，再用余向量 $p$——它就栖息于我们所在的那一点——去作用它。故称“重言”：$\theta$ 使用的是该点自身的 $p$。

> **引理 —— 坐标表达式。** 在诱导坐标下，
> $$
> \theta = \sum_{i=1}^n p_i\, dq^i.
> $$

**证明。**
1. 一般切向量为 $X=\sum_i a^i\,\partial_{q^i} + \sum_i b_i\,\partial_{p_i}$。*理由：* $(q^i,p_i)$ 是坐标，故它们的坐标向量场张成切空间。
2. 投影 $\pi$ 丢掉 $p$-坐标，故 $d\pi(X)=\sum_i a^i\,\partial_{q^i}\in T_qQ$。*理由：* $\pi(q,p)=q$ 只依赖于 $q^i$，故 $\partial \pi/\partial p_i=0$。
3. 在 $(q,p)$ 处余向量为 $p=\sum_i p_i\,dq^i$，故 $p\big(d\pi(X)\big)=\sum_i p_i\,a^i$。*理由：* $dq^i(\partial_{q^j})=\delta^i_j$。
4. 另一方面 $\big(\sum_i p_i\,dq^i\big)(X)=\sum_i p_i\,a^i$，即在 $X$ 上求 $dq^i$ 并丢弃 $\partial_{p_j}$ 部分。两者相符，故 $\theta=\sum_i p_i\,dq^i$。$\blacksquare$

#### 典范辛形式

> **定义 —— 典范辛形式。** $\omega_{\mathrm{can}} := -\,d\theta$。

> **命题。** $\omega_{\mathrm{can}}$ 是 $T^*Q$ 上的辛形式，且在诱导坐标下
> $$
> \omega_{\mathrm{can}} = \sum_{i=1}^n dq^i\wedge dp_i.
> $$

**证明。**
1. 计算 $-d\theta = -d\big(\sum_i p_i\,dq^i\big) = -\sum_i dp_i\wedge dq^i$，这里用了 $d(p_i\,dq^i)=dp_i\wedge dq^i + p_i\,d(dq^i)$ 以及 $d(dq^i)=0$（因为 $d^2=0$）。*理由：* 函数与 $1$-形式之积的 $d$ 的莱布尼茨法则，加上 $d^2=0$。
2. $\wedge$ 的反对称性给出 $-dp_i\wedge dq^i = dq^i\wedge dp_i$，故 $\omega_{\mathrm{can}}=\sum_i dq^i\wedge dp_i$。*理由：* 对 $1$-形式有 $\alpha\wedge\beta=-\beta\wedge\alpha$。
3. **闭：** $d\omega_{\mathrm{can}}=d(-d\theta)=-d^2\theta=0$。*理由：* $d^2=0$。
4. **非退化：** 坐标形式恰是标准的 $\omega_0$，我们在 s1 中已验证它非退化。$\blacksquare$

那个减号是一个约定，选取它是为了让 $\omega_{\mathrm{can}}=\sum dq^i\wedge dp_i$ 而非 $\sum dp_i\wedge dq^i$，从而与常规符号下的哈密顿方程相匹配。

> **范例。** 对直线上的自由粒子，$Q=\mathbb{R}$，$T^*Q=\mathbb{R}^2$，坐标为 $(q,p)$，$\theta=p\,dq$，$\omega_{\mathrm{can}}=dq\wedge dp$。相空间中一个回路所围的面积——重言形式的积分 $\oint p\,dq$——是经典 **作用量**，正是玻尔与索末菲令其等于 $h$ 的整数倍的那个量。我们将在 s9 回到这一点。

> **范例 —— 摆的相空间。** 对圆周 $Q=S^1$ 上的粒子，角坐标为 $\varphi$，相空间是 $T^*S^1$，即坐标为 $(\varphi,p_\varphi)$ 的柱面，$\theta=p_\varphi\,d\varphi$，$\omega=d\varphi\wedge dp_\varphi$。摆有 $H=\tfrac{1}{2}p_\varphi^2 - \cos\varphi$；它在柱面上的水平集就是熟悉的摆相图——$(\varphi,p_\varphi)=(0,0)$ 附近的小振荡环，以及分界线之上绕柱面缠绕的旋转曲线。闭轨道的作用量 $\oint p_\varphi\,d\varphi$ 是所围的相空间面积，仍是旧量子论所量子化的那个量。这个例子表明位形空间不必是 $\mathbb{R}^n$：对 *任何* $Q$，余切构造都是自动的。

> **自然性。** 重言形式是 **自然的**：对任何微分同胚 $\psi:Q_1\to Q_2$，其余切提升 $T^*\psi:T^*Q_2\to T^*Q_1$ 把 $\theta_1$ 拉回为 $\theta_2$，因而自动是辛同胚。于是位形空间的每个对称性都自动成为相空间的对称性——我们在 s6 构建矩映射时将利用这一事实。

<a id="s4"></a>
### 哈密顿向量场与泊松括号

现在来谈动力学。相空间上的一个函数生成一个流，两个函数可以配对成第三个——泊松括号——其最深刻的性质，即雅可比恒等式，我们将直接从 $d\omega=0$ 证明。

#### 哈密顿向量场

> **定义 —— 哈密顿向量场。** 设 $(M,\omega)$ 为辛流形，$f\in C^\infty(M)$ 为光滑函数。其 **哈密顿向量场** $X_f$ 是满足下式的唯一向量场
> $$
> \iota_{X_f}\omega = df,\qquad\text{即}\qquad \omega(X_f,\cdot)=df.
> $$
> 存在性与唯一性由 $\flat:X\mapsto\iota_X\omega$ 是同构（非退化，s2）得出；显式地 $X_f=\sharp(df)$。

> **坐标形式（达布）。** 在 $\omega=\sum dq^i\wedge dp_i$ 的达布坐标下，
> $$
> X_f = \sum_{i=1}^n\left(\frac{\partial f}{\partial p_i}\,\frac{\partial}{\partial q^i} - \frac{\partial f}{\partial q^i}\,\frac{\partial}{\partial p_i}\right).
> $$

**推导。**
1. 写 $X_f=\sum_i(A^i\partial_{q^i}+B_i\partial_{p_i})$，分量未知。则 $\iota_{X_f}\omega=\sum_i(A^i\,dp_i - B_i\,dq^i)$，这里计算 $\iota_X(dq^i\wedge dp_i)=(dq^i(X))dp_i-(dp_i(X))dq^i = A^i\,dp_i - B_i\,dq^i$。*理由：* 向量对 $1$-形式楔积的内积。
2. 同时 $df=\sum_i(\partial_{q^i}f\,dq^i+\partial_{p_i}f\,dp_i)$。*理由：* 函数微分的定义。
3. 在 $\iota_{X_f}\omega=df$ 中匹配 $dq^i$ 与 $dp_i$ 的系数：$-B_i=\partial_{q^i}f$ 且 $A^i=\partial_{p_i}f$。*理由：* $\{dq^i,dp_i\}$ 是 $1$-形式的基，故系数逐项相等。
4. 代回即得所述公式。$\blacksquare$

取 $f=H$ 即哈密顿量，$X_H$ 的积分曲线满足 $\dot q^i=\partial H/\partial p_i$，$\dot p_i=-\partial H/\partial q^i$——**哈密顿方程** 被精确重现，连符号也一致。

#### 泊松括号

> **定义 —— 泊松括号。** 对 $f,g\in C^\infty(M)$，
> $$
> \{f,g\} := \omega(X_f,X_g).
> $$
> 一次计算即可求出它：$\omega(X_f,X_g)=(\iota_{X_f}\omega)(X_g)=df(X_g)=X_g(f)$，其中第二个等号是 $\iota_{X_f}\omega=df$，第三个是 $1$-形式 $df$ 作用于向量 $X_g$。于是 $\{f,g\}=X_g(f)$，一劳永逸地固定整体符号。

> **坐标形式。**
> $$
> \{f,g\} = \sum_{i=1}^n\left(\frac{\partial f}{\partial q^i}\frac{\partial g}{\partial p_i} - \frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q^i}\right).
> $$

**推导。** 利用 $\{f,g\}=X_g(f)$ 与上面 $X_g=\sum_i(\partial_{p_i}g\,\partial_{q^i} - \partial_{q^i}g\,\partial_{p_i})$ 的坐标形式：$X_g(f)=\sum_i(\partial_{p_i}g\,\partial_{q^i}f - \partial_{q^i}g\,\partial_{p_i}f)=\sum_i(\partial_{q^i}f\,\partial_{p_i}g - \partial_{p_i}f\,\partial_{q^i}g)$，这正是所示表达式。基本括号为 $\{q^i,q^j\}=0$，$\{p_i,p_j\}=0$，$\{q^i,p_j\}=\delta^i_j$。

该括号是 **双线性** 且 **反对称** 的（$\{f,g\}=-\{g,f\}$，由 $\omega$ 反对称立得），并满足 **莱布尼茨法则** $\{f,gh\}=\{f,g\}h+g\{f,h\}$（因为 $X_f$ 是一个求导）。其深刻性质是：

> **定理 —— 雅可比恒等式。** 对所有 $f,g,h\in C^\infty(M)$，
> $$
> \{f,\{g,h\}\}+\{g,\{h,f\}\}+\{h,\{f,g\}\}=0.
> $$

**从 $d\omega=0$ 出发的证明。** 我们使用 $2$-形式外微分的不变公式。对任意 $2$-形式 $\omega$ 与向量场 $X,Y,Z$，
$$
d\omega(X,Y,Z) = X\,\omega(Y,Z) - Y\,\omega(X,Z) + Z\,\omega(X,Y) - \omega([X,Y],Z) + \omega([X,Z],Y) - \omega([Y,Z],X),
$$
其中 $[\cdot,\cdot]$ 是向量场的李括号。（这是标准的内禀公式；预备指南中给出了推导。）我们代入 $X=X_f,\ Y=X_g,\ Z=X_h$ 并利用 $d\omega=0$。

1. 两个哈密顿场的每个配对都是一个泊松括号：$\omega(X_g,X_h)=\{g,h\}$，等等。*理由：* $\{\cdot,\cdot\}$ 的定义。
2. 每个“方向导数”项都成为一个 *双重* 括号。例如 $X_f\,\omega(X_g,X_h)=X_f\{g,h\}=\{f,\{g,h\}\}$，这里对任意函数 $\phi$ 用了 $X_f(\phi)=\{f,\phi\}$。*理由：* 关系 $\{f,\phi\}=X_f(\phi)$。
3. 我们需要李括号项。**关键引理：** $[X_f,X_g]=X_{\{f,g\}}$（映射 $f\mapsto X_f$ 是李代数同态，至多差一个符号），证明见下；承认它后，$\omega([X_f,X_g],X_h)=\omega(X_{\{f,g\}},X_h)=\{\{f,g\},h\}=-\{h,\{f,g\}\}$。*理由：* 关键引理与括号的反对称性。
4. 代入内禀公式并令 $d\omega(X_f,X_g,X_h)=0$。三个“导数”项给出 $\{f,\{g,h\}\}-\{g,\{f,h\}\}+\{h,\{f,g\}\}$。三个李括号项给出 $-(-\{h,\{f,g\}\}) + (\ldots) - (\ldots)$。把一切写开并用反对称性对齐符号，六项坍缩为雅可比子的恰好两倍：$0 = d\omega(\ldots) = 2\big(\{f,\{g,h\}\}+\{g,\{h,f\}\}+\{h,\{f,g\}\}\big)$。*理由：* $d\omega=0$ 杀掉左边；对右边记账。除以 $2$ 即得该恒等式。$\blacksquare$

**关键引理 $[X_f,X_g]=X_{\{f,g\}}$ 的证明。**
1. 我们证明 $\iota_{[X_f,X_g]}\omega = d\{f,g\}$；由于 $\flat$ 单射，这确定了该场。*理由：* 非退化性意味着哈密顿场由 $\iota_X\omega$ 确定。
2. 一个一般恒等式：$\iota_{[X,Y]}\omega = \mathcal{L}_X(\iota_Y\omega) - \iota_Y(\mathcal{L}_X\omega)$。*理由：* 李导数与缩并的交换性差这一括号项（一个标准的嘉当演算恒等式）。
3. 首先，$\mathcal{L}_{X_f}\omega = d\,\iota_{X_f}\omega + \iota_{X_f}\,d\omega = d(df) + 0 = 0$，用了嘉当魔法公式、$\iota_{X_f}\omega=df$、$d^2=0$ 以及 $d\omega=0$。故第 2 步中的最后一项消失。*理由：* 嘉当公式与闭性——**这里再次用到 $d\omega=0$。**
4. 然后 $\iota_{[X_f,X_g]}\omega = \mathcal{L}_{X_f}(\iota_{X_g}\omega) = \mathcal{L}_{X_f}(dg) = d(\mathcal{L}_{X_f}g) = d(X_f g) = d\{f,g\}$，用了 $\mathcal{L}_{X_f}$ 与 $d$ 交换，且在函数上作用为方向导数。*理由：* $\mathcal{L}_X d = d\mathcal{L}_X$ 以及 $\mathcal{L}_X g = Xg$。
5. 因此 $[X_f,X_g]=X_{\{f,g\}}$。$\blacksquare$

> **这为何重要。** $(C^\infty(M),\{\cdot,\cdot\})$ 是一个 **泊松代数**——在括号下是李代数，同时还服从莱布尼茨法则。量子化将把这个括号替换为算子对易子的 $\tfrac{1}{i\hbar}$ 倍；雅可比恒等式是算子对易子雅可比恒等式的经典投影。没有 $d\omega=0$，这一切都无法成立。

#### 范例

对 $\mathbb{R}^2$ 上的谐振子 $H=\tfrac12(p^2+q^2)$：$X_H=p\,\partial_q - q\,\partial_p$，故 $\dot q=p,\ \dot p=-q$，给出圆周运动 $q(t)=q_0\cos t+p_0\sin t$。而 $\{q,H\}=\partial_q q\,\partial_p H-\partial_p q\,\partial_q H = p = \dot q$，确认了时间演化中的 $\dot f=\{f,H\}$。

<a id="s5"></a>
### 辛同胚、正则变换，以及保持 $\omega$ 的哈密顿流

我们对尊重辛结构的映射进行分类，并表明哈密顿动力学就栖身于这一类之中。

> **定义 —— 辛同胚。** 微分同胚 $\phi:(M_1,\omega_1)\to(M_2,\omega_2)$ 称为 **辛同胚**，若 $\phi^*\omega_2=\omega_1$，即它把一个形式拉回为另一个。当 $M_1=M_2$ 时这些是相空间的对称性；物理学家称之为 **正则变换**——保持哈密顿方程形式不变的坐标变换。

> **定理 —— 哈密顿流是辛同胚。** 设 $\psi_t$ 是哈密顿向量场 $X_H$ 的流（把初始状态沿动力学送出的时间-$t$ 映射）。则对所有 $t$ 有 $\psi_t^*\omega=\omega$：时间演化保持辛形式。

**证明。**
1. 求导：$\frac{d}{dt}\psi_t^*\omega = \psi_t^*(\mathcal{L}_{X_H}\omega)$。*理由：* 李导数作为张量沿流变化率的定义性质。
2. 计算 $\mathcal{L}_{X_H}\omega = d\,\iota_{X_H}\omega + \iota_{X_H}\,d\omega$。*理由：* 嘉当魔法公式。
3. 第一项为 $d(dH)=0$（$\iota_{X_H}\omega=dH$ 且 $d^2=0$）；第二项为 $\iota_{X_H}(0)=0$（$d\omega=0$）。*理由：* $X_H$ 的定义、$d^2=0$ 以及闭性。
4. 于是 $\frac{d}{dt}\psi_t^*\omega=0$，故 $\psi_t^*\omega$ 为常数；在 $t=0$ 时它是 $\omega$，故对所有 $t$ 有 $\psi_t^*\omega=\omega$。$\blacksquare$

取楔幂，$\psi_t^*\omega^n=\omega^n$：流保持刘维尔体积。这就是 **刘维尔定理**——一群在哈密顿方程下演化的状态保持其相空间体积不变，这是统计力学等先验概率假设的几何根源。

> **反过来 —— 局部哈密顿场。** 满足 $\mathcal{L}_X\omega=0$ 的向量场 $X$ 称为 **辛的**；由嘉当公式 $\mathcal{L}_X\omega=d\iota_X\omega$，故 $X$ 辛 $\iff$ $\iota_X\omega$ 闭。若 $\iota_X\omega$ 是 *恰当的*，即 $=df$，则 $X=X_f$ 是真正的哈密顿场。闭与恰当之间的差距由第一德拉姆上同调 $H^1(M)$ 度量：在单连通的 $M$ 上每个辛场都是哈密顿的，但在比如环面上，存在没有整体生成元 $H$ 的辛流。

> **范例 —— 线性正则变换。** 在 $(\mathbb{R}^2,dq\wedge dp)$ 上，映射 $\phi(q,p)=(\lambda q,\ \lambda^{-1}p)$（一个“挤压”）满足 $\phi^*(dq\wedge dp)=d(\lambda q)\wedge d(\lambda^{-1}p)=\lambda\lambda^{-1}\,dq\wedge dp=dq\wedge dp$，故它是辛同胚：它拉伸位置、压缩动量，同时保持面积。相比之下 $(q,p)\mapsto(2q,2p)$ 把面积放大 $4$ 倍，因而 *不是* 正则的。

> **范例 —— 谐振子流是正则的。** 由 s4，振子流为 $\psi_t(q_0,p_0)=(q_0\cos t + p_0\sin t,\ -q_0\sin t + p_0\cos t)$，即 $(q,p)$-平面中转角 $t$ 的旋转。其雅可比矩阵是旋转 $R_t=\left(\begin{smallmatrix}\cos t&\sin t\\-\sin t&\cos t\end{smallmatrix}\right)$，$\det R_t=\cos^2 t+\sin^2 t=1$，故 $\psi_t^*(dq\wedge dp)=\det(R_t)\,dq\wedge dp=dq\wedge dp$。如一般定理所保证，流对每个 $t$ 都保持面积——能量圆以恒定的相空间面积被扫出，这正是振子匀角速度的几何内涵。

> **生成函数。** 正则变换由栖息于拉格朗日子流形（s7）上的 **生成函数** 编码。对 $\mathbb{R}^{2n}$ 的变换 $(q,p)\mapsto(Q,P)$，满足 $p=\partial S_1/\partial q$、$P=-\partial S_1/\partial Q$ 的函数 $S_1(q,Q)$ 自动产生一个辛同胚，因为此时 $p\,dq - P\,dQ = dS_1$ 是恰当的，故 $d(p\,dq)=d(P\,dQ)$，即 $\sum dq^i\wedge dp_i=\sum dQ^i\wedge dP_i$。四种经典“类型” $S_1(q,Q),S_2(q,P),S_3(p,Q),S_4(p,P)$ 互为勒让德变换，而哈密顿–雅可比理论选取 $S_2$ 使新哈密顿量为零——从而把求解动力学变成求一个生成函数。

<a id="s6"></a>
### 矩映射与连续对称性；辛（马斯登–韦恩斯坦）约化

相空间的对称性产生守恒量，并让我们缩小空间。这是诺特定理的彻底几何化。

#### 群作用与矩映射

> **设置。** 设李群 $G$ 通过辛同胚作用于 $(M,\omega)$（每个群元素都作为辛同胚作用）。其李代数 $\mathfrak g$（单位元处的切空间，带括号 $[\cdot,\cdot]$）通过 **基本向量场** 作用：每个 $\xi\in\mathfrak g$ 给出 $M$ 上的一个场 $\xi_M$，生成单参数子群的流。每个 $\xi_M$ 都是辛的（$\mathcal{L}_{\xi_M}\omega=0$）。

> **定义 —— 矩映射。** 该作用的 **矩映射** 是一个光滑映射 $\mu:M\to\mathfrak g^*$（取值于李代数的对偶），使得：
> - 对每个 $\xi\in\mathfrak g$，分量函数 $\mu^\xi(x):=\langle\mu(x),\xi\rangle$ 是 $\xi_M$ 的哈密顿量，即 $X_{\mu^\xi}=\xi_M$，等价地 $d\mu^\xi=\iota_{\xi_M}\omega$；
> - $\mu$ 是 **等变的**：它把 $M$ 上的 $G$-作用与 $\mathfrak g^*$ 上的余伴随作用交织在一起。

用语言说：矩映射把所有对称性的守恒量打包进一个 $\mathfrak g^*$-值函数。对每个对称方向 $\xi$，函数 $\mu^\xi$ 是诺特荷。

> **定理 —— 几何版诺特。** 若 $H$ 是 $G$-不变的（对所有 $g\in G$ 有 $H\circ g=H$），则每个分量 $\mu^\xi$ 沿 $H$ 的哈密顿流守恒：$\{H,\mu^\xi\}=0$。

**证明。**
1. $H$ 的 $G$-不变性意味着对每个 $\xi$ 有 $\xi_M(H)=0$（对称性的流不改变 $H$）。*理由：* 在 $\xi$ 生成的单参数群下的不变性。
2. 但 $\xi_M=X_{\mu^\xi}$，故 $\xi_M(H)=X_{\mu^\xi}(H)=\{\mu^\xi,H\}$。*理由：* 矩映射性质与括号的定义。
3. 因此 $\{\mu^\xi,H\}=0$，由反对称性 $\{H,\mu^\xi\}=0$，故沿流有 $\frac{d}{dt}\mu^\xi=\{\mu^\xi,H\}=0$。$\blacksquare$

> **范例。** (i) *平移。* $Q=\mathbb{R}^n$，$G=\mathbb{R}^n$ 通过 $q\mapsto q+a$ 作用。矩映射为 $\mu(q,p)=p$：线动量守恒。(ii) *旋转。* $G=SO(3)$ 作用于 $\mathbb{R}^3$；矩映射是角动量 $\mu(q,p)=q\times p$。$\mathfrak{so}(3)$ 的李代数括号由角动量分量的泊松括号 $\{L_i,L_j\}=\epsilon_{ijk}L_k$ 重现——这是量子角动量代数的经典种子。

> **范例计算 —— 角动量括号。** 设 $\mathbb{R}^6$ 上 $L_1=q^2p_3-q^3p_2$ 与 $L_2=q^3p_1-q^1p_3$，典范括号为 $\{q^i,p_j\}=\delta^i_j$ 及 $\{q^i,q^j\}=\{p_i,p_j\}=0$。我们用双线性与莱布尼茨法则计算 $\{L_1,L_2\}$，只保留把一个坐标与其自身共轭动量配对的交叉括号。
> 1. $\{q^2p_3,\,q^3p_1\} = q^2p_1\{p_3,q^3\} = q^2p_1\cdot(-1) = -q^2p_1$。*理由：* $\{p_3,q^3\}=-\{q^3,p_3\}=-1$；其余因子由莱布尼茨法则提出。
> 2. $\{-q^3p_2,\,-q^1p_3\} = q^3p_2\,\{p_2\,\text{对}\,q\}$——此处唯一的共轭对是 $q^3$ 与 $p_3$：$\{-q^3p_2,-q^1p_3\}=q^1p_2\{q^3,p_3\}=q^1p_2$。*理由：* $\{q^3,p_3\}=+1$。
> 3. 余下两个交叉项 $\{q^2p_3,-q^1p_3\}$ 与 $\{-q^3p_2,q^3p_1\}$ 为零：没有坐标遇上其共轭动量。*理由：* 所有这类典范括号都为零。
> 4. 求和：$\{L_1,L_2\} = -q^2p_1 + q^1p_2 = q^1p_2 - q^2p_1 = L_3$。
>
> 于是 $\{L_1,L_2\}=L_3$，重现了 $\mathfrak{so}(3)$ 的结构常数 $\epsilon_{ijk}$。量子关系 $[\hat L_i,\hat L_j]=i\hbar\,\epsilon_{ijk}\hat L_k$ 正是这一计算在 $\{\cdot,\cdot\}\to\tfrac{1}{i\hbar}[\cdot,\cdot]$ 之下的版本。

#### 马斯登–韦恩斯坦约化

当存在对称性时，动力学其实发生在一个更小的空间上：固定守恒荷并对对称性取商。

> **定理 —— 马斯登–韦恩斯坦–迈耶约化。** 设 $G$ 作用于 $(M,\omega)$，带等变矩映射 $\mu$，并设 $\zeta\in\mathfrak g^*$ 是余伴随作用的不动值（例如 $\zeta=0$，或当 $G$ 阿贝尔时为任意值）。假设 $G$ 在水平集 $\mu^{-1}(\zeta)$ 上自由且正常地作用。则 **约化空间**
> $$
> M_\zeta := \mu^{-1}(\zeta)\big/G
> $$
> 是一个光滑流形，并带有唯一的辛形式 $\omega_\zeta$，满足 $\iota^*\omega = \pi^*\omega_\zeta$，其中 $\iota:\mu^{-1}(\zeta)\hookrightarrow M$ 是包含映射，$\pi:\mu^{-1}(\zeta)\to M_\zeta$ 是商投影。其维数为 $\dim M - 2\dim G$。

**证明思路。**
1. 水平集 $\mu^{-1}(\zeta)$ 的余维数为 $\dim G$（当作用自由时矩映射有 $\dim G$ 个独立分量）。*理由：* 正则值定理；自由性使 $\zeta$ 成为正则值。
2. 在 $\mu^{-1}(\zeta)$ 的某点，水平集的切空间是群轨道切空间的 **辛正交**：$T(\mu^{-1}\zeta)=(\mathfrak g\!\cdot\! x)^\omega$。*理由：* $d\mu^\xi=\iota_{\xi_M}\omega$ 意味着 $v\in\ker d\mu \iff \omega(\xi_M,v)=0\ \forall\xi$。
3. 因此轨道方向 $\mathfrak g\!\cdot\! x$ 落在 *水平集内部*，并恰是限制形式 $\iota^*\omega$ 的 **零方向**。对 $G$ 取商正好移除这些零方向，留下一个非退化形式。*理由：* 移除退化形式的根基即得非退化形式。
4. 该形式下降是因为 $\iota^*\omega$ 是 $G$-不变且基本（水平）的；闭性下降是因为 $d$ 与拉回交换。$\blacksquare$

> **物理意义与例子。** 约化 *就是* 消去循环坐标。对一个中心力问题，$SO(3)$-对称性让我们固定角动量并过渡到一个约化的径向问题；“离心势垒”是约化辛几何的残余。在非零矩值处把 $\mathbb{C}^{n+1}$ 按 $U(1)$ 相位作用约化，得到复射影空间 $\mathbb{CP}^n$ 及其富比尼–施图迪形式——这就是我们在 s11 中量子化自旋所用的模型。

> **余伴随轨道。** 辛流形的一个特别干净的来源是李群 $G$ 在 $\mathfrak g^*$ 内的 **余伴随轨道**：由余伴随作用扫出的集合 $\mathcal O_\zeta=\{\mathrm{Ad}^*_g\zeta : g\in G\}$。**基里洛夫–科斯坦–苏里奥定理** 说每个轨道都带有一个典范辛形式 $\omega_{\mathcal O}(\xi_M,\eta_M)|_\zeta=\langle\zeta,[\xi,\eta]\rangle$，直接由李括号构建。对 $G=SU(2)$，非零余伴随轨道是各种半径的球面——它们恰是 s11 的经典自旋相空间。余伴随轨道是“轨道方法”的几何家园，该方法把群表示的量子化看作这些轨道的量子化，从而把 s6 直接与 s11 联系起来。

<a id="s7"></a>
### 拉格朗日子流形及其作用

存在一类与 $\omega$ 最大限度相适配的子流形——既不太大也不太小——它编码了生成函数、动力学，乃至量子态将由之构建的那些对象本身。

> **定义 —— 迷向、余迷向、拉格朗日。** 设 $(M^{2n},\omega)$ 为辛流形，$L\subseteq M$ 为子流形。在每点切空间 $T_pL$ 有一个 **辛正交** $(T_pL)^\omega=\{v\in T_pM:\omega(v,w)=0\ \forall w\in T_pL\}$。则 $L$ 称为：
> - **迷向**，若 $T_pL\subseteq(T_pL)^\omega$，即 $\omega|_L=0$（形式在 $L$ 上消失）；此时必有 $\dim L\le n$；
> - **余迷向**，若 $(T_pL)^\omega\subseteq T_pL$；此时必有 $\dim L\ge n$；
> - **拉格朗日**，若两者皆然，即 $\omega|_L=0$ **且** $\dim L=n$（极大迷向）。

维数计数 $\dim(T_pL)^\omega = 2n-\dim T_pL$（非退化性的一个推论，正如 s1 中的辛正交那样）迫使拉格朗日子流形恰好是半维的，且 $\omega$ 限制为零。

> **关键例子。**
> 1. **零截面** $Q\hookrightarrow T^*Q$（所有动量为零）：$\theta=\sum p_i\,dq^i$ 在那里消失，故 $\omega=-d\theta$ 限制为 $0$；它是拉格朗日的。
> 2. **$df$ 的图。** 对 $f\in C^\infty(Q)$，集合 $\{(q,df_q)\}\subseteq T^*Q$ 是拉格朗日的，因为在其上 $\theta = df$ 拉回为恰当形式，故 $\omega|_L=-d(df)=0$。更一般地，任何 *闭* $1$-形式的像都是拉格朗日的。
> 3. **辛同胚的图。** 微分同胚 $\phi:M_1\to M_2$ 是辛同胚 $\iff$ 其图在 $(M_1\times M_2,\ \pi_2^*\omega_2-\pi_1^*\omega_1)$ 中是拉格朗日的。这就是韦恩斯坦的口号，*“万物皆为拉格朗日子流形”。*

> **命题 —— 辛同胚的图。** 在 $M_1\times M_2$ 上取 $\Omega:=\pi_2^*\omega_2-\pi_1^*\omega_1$，图 $\Gamma_\phi=\{(x,\phi(x))\}$ 满足 $\Omega|_{\Gamma_\phi}=0$ 当且仅当 $\phi^*\omega_2=\omega_1$。

**证明。** 用 $x\mapsto(x,\phi(x))$ 参数化 $\Gamma_\phi$；$\pi_1^*\omega_1$ 的拉回为 $\omega_1$，$\pi_2^*\omega_2$ 的拉回为 $\phi^*\omega_2$。因此 $\Omega$ 的拉回为 $\phi^*\omega_2-\omega_1$，它消失当且仅当 $\phi^*\omega_2=\omega_1$。由于 $\dim\Gamma_\phi=\dim M_1=\tfrac12\dim(M_1\times M_2)$，限制形式的消失恰是拉格朗日条件。$\blacksquare$

> **范例 —— 拉格朗日环面与作用量变量。** 对一个有 $n$ 个对易守恒量 $f_1,\dots,f_n$（即 $\{f_i,f_j\}=0$）的可积系统，一个公共水平集 $\{f_i=c_i\}$ 是拉格朗日的：哈密顿场 $X_{f_i}$ 张成其切空间，且 $\omega(X_{f_i},X_{f_j})=\{f_i,f_j\}=0$，故 $\omega$ 在其上消失。当它紧且连通时，刘维尔–阿诺德定理说这个水平集是一个 **环面** $T^n$，且存在 **作用–角坐标** $(I_i,\varphi^i)$，在其中 $\omega=\sum dI_i\wedge d\varphi^i$，动力学为刚性旋转 $\dot\varphi^i=\text{常数}$。作用量是环面上各独立闭链上的环积分 $I_i=\frac{1}{2\pi}\oint_{\gamma_i}p\,dq$——正是玻尔–索末菲规则（s9）所量子化的那些量。

> **拉格朗日交。** 由于动力学把拉格朗日子流形送到拉格朗日子流形（哈密顿流是辛同胚，而辛同胚由图命题保持拉格朗日条件），诸如“一个被扰动的轨道是否回到其起点附近”这样的问题就变成关于两个拉格朗日子流形 *交* 的问题。计数这类在形变下稳健的交点，是进入 **弗洛尔同调** 与著名的关于哈密顿映射不动点的 **阿诺德猜想** 的入口——一言以蔽之即现代辛拓扑。值得一提的一个陷阱：两个拉格朗日子流形一般在孤立点处相交（每个拉格朗日子流形是半维的，故 $n+n=2n$ 与环境维数相匹配），而那些点的 *个数* 才是不变量，并非它们的位置。

> **作用与直觉。** 拉格朗日子流形是量子态的经典类比：一组 $(q,p)$，半经典波函数 $e^{iS/\hbar}$ 的相位在其上保持相干（因为 $\omega|_L=0$ 意味着 $\oint p\,dq$ 在那里局部平凡）。在几何量子化（s10）中，极化由拉格朗日叶状结构构建，而玻尔–索末菲条件挑选出 *被量子化的* 拉格朗日环面。拉格朗日子流形也是正则变换生成函数的栖身之处，把四种经典“类型”的生成函数统一进一幅几何图景。

## 第 B 部分 · 走向量子化

<a id="s8"></a>
### 概复结构与凯勒结构 —— 通往复几何的桥梁

量子化所需的不仅是一个辛形式：它还需要一种一致地把相空间分裂为“位置型”与“动量型”两半的方式。复几何提供了最干净的这种分裂，而 s1 中的矩阵 $J$ 是其种子。

> **定义 —— 概复结构。** 流形 $M$ 上的 **概复结构** 是一个 $(1,1)$-张量场 $J:TM\to TM$（每个切空间上光滑变化的线性映射），满足 $J^2=-\mathrm{id}$。它使每个切空间成为一个复向量空间（乘以 $i$ 即“施以 $J$”）。

> **定义 —— 相容三元组。** 在辛流形 $(M,\omega)$ 上，概复结构 $J$ 与 $\omega$ **相容**，若
> $$
> g(X,Y):=\omega(X,JY)
> $$
> 是一个 **黎曼度量**——对称且正定。此时数据 $(\omega,J,g)$ 称为 **相容三元组**：任意两者决定第三者。

> **命题 —— 相容的 $J$ 总是存在。** 每个辛流形都允许一个相容的概复结构。

**证明梗概。**
1. 任取一个黎曼度量 $h$（它们总是通过单位分解存在）。*理由：* 仿紧性给出度量。
2. $\omega$ 与 $h$ 的非退化性通过 $\omega(X,Y)=h(AX,Y)$ 定义一个可逆的 $A$；$A$ 是 $h$-斜伴随的。*理由：* 两个形式都非退化，故各自定义到对偶的同构。
3. 极分解 $A=J|A|$，其中 $|A|=\sqrt{A^{\mathsf T}A}$ 对称正定，$J=A|A|^{-1}$。可验证 $J^2=-\mathrm{id}$，且 $g(X,Y)=\omega(X,JY)$ 对称正定。*理由：* 斜伴随可逆算子的极分解给出一个平方为 $-\mathrm{id}$ 的正交 $J$。$\blacksquare$

相容性把三种几何联系起来：长度来自 $g$，面积来自 $\omega$，复结构来自 $J$，并有 $\omega(X,Y)=g(JX,Y)$。

> **范例 —— $\mathbb{R}^2$ 上的标准相容三元组。** 取 $\omega_0=dq\wedge dp$ 与逆时针旋转 $90^\circ$ 的映射 $J\,\partial_q=\partial_p$，$J\,\partial_p=-\partial_q$（矩阵 $\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$，故 $J^2=-\mathrm{id}$）。在基向量上计算 $g(X,Y):=\omega_0(X,JY)$：$g(\partial_q,\partial_q)=\omega_0(\partial_q,J\partial_q)=\omega_0(\partial_q,\partial_p)=1$；$g(\partial_p,\partial_p)=\omega_0(\partial_p,-\partial_q)=-\omega_0(\partial_p,\partial_q)=1$；以及 $g(\partial_q,\partial_p)=\omega_0(\partial_q,-\partial_q)=0$。故 $g$ 是标准欧氏度量——对称且正定——确认了 $(\omega_0,J,g)$ 是相容三元组。令 $z=q+ip$，映射 $J$ 恰是乘以 $i$。这一个二维计算就是每个凯勒流形局部上的样子。

> **定义 —— 凯勒流形。** 若此外 $J$ 还是 **可积的**（它来自货真价实的全纯坐标，等价地其尼延赫斯张量消失），且 $\omega$ 闭（此处自动成立），则 $(M,\omega,J,g)$ 是 **凯勒流形**，$\omega$ 是 **凯勒形式**。在凯勒流形上有局部复坐标 $z^j=q^j+ip_j$，在其中 $\omega=\frac{i}{2}\sum_j dz^j\wedge d\bar z^j$，且 $\omega = i\,\partial\bar\partial K$，其中 $K$ 是实的 **凯勒势**。

> **例子。** $\mathbb{C}^n=\mathbb{R}^{2n}$（$z^j=q^j+ip_j$）是平坦的凯勒模型。带 **富比尼–施图迪形式** 的复射影空间 $\mathbb{CP}^n$ 是紧的模型——并且恰是 s6 中的约化空间。带圆面积形式的 $2$-球面 $S^2\cong\mathbb{CP}^1$ 是凯勒的；这是自旋的几何，将在 s11 中量子化。

> **为何这是桥梁。** 凯勒极化（s10）是“波函数为全纯的”这一选择。它把几何量子化的抽象配方变成线丛的货真价实的全纯截面，具体地恢复出谐振子与自旋的希尔伯特空间。

<a id="s9"></a>
### 预量子化 —— 预量子线丛、其联络，以及整性条件

我们现在构建量子化的前半部分：一个由 *所有* 相空间函数构成的希尔伯特空间，其算子精确地重现泊松括号。做到这一点的障碍——及其解决——就是玻尔–索末菲整性条件。

#### 预量子化数据

狄拉克对应要求一个从经典可观测量到算子的线性映射 $f\mapsto\hat f$，满足
$$
[\hat f,\hat g] = i\hbar\,\widehat{\{f,g\}},\qquad \hat 1=\mathrm{id},
$$
其中 $\hbar$ 是约化普朗克常数。第一个猜测 $\hat f = -i\hbar X_f$ 把括号弄对了（因为由 s4 有 $[X_f,X_g]=X_{\{f,g\}}$），但不满足 $\hat 1=\mathrm{id}$，因为 $X_1=0$ 会给出 $\hat 1=0$。修补办法是加上一个由辛势构建的乘法项。

> **定义 —— 预量子线丛。** $(M,\omega)$ 上的 **预量子线丛** 是一个复线丛 $L\to M$（一个纤维为一维复空间的向量丛），配有一个厄米度量 $\langle\cdot,\cdot\rangle$ 与一个相容联络 $\nabla$，其 **曲率** 为
> $$
> F_\nabla = -\frac{i}{\hbar}\,\omega.
> $$
> $L$ 的截面——光滑选择 $s(x)\in L_x$——是 **预量子波函数**。

联络 $\nabla$ 是微分截面的一种规则；其曲率是度量 $\nabla_X\nabla_Y-\nabla_Y\nabla_X-\nabla_{[X,Y]}$ 不消失程度的 $2$-形式 $F_\nabla$。局部上，在 $\omega=d\theta$ 处，写 $\nabla=d-\tfrac{i}{\hbar}\theta$，于是 $F_\nabla=-\tfrac{i}{\hbar}d\theta=-\tfrac{i}{\hbar}\omega$。

> **定义 —— 预量子算子。** 对 $f\in C^\infty(M)$，
> $$
> \hat f := -i\hbar\,\nabla_{X_f} + f.
> $$

> **定理 —— 狄拉克公理成立。** 此赋值是线性的，$\hat 1=\mathrm{id}$，且 $[\hat f,\hat g]=i\hbar\,\widehat{\{f,g\}}$。

**对易子的证明（关键公理）。**
1. $\hat 1=-i\hbar\nabla_{X_1}+1=0+1=\mathrm{id}$，因为 $X_1=0$（$d1=0$）。*理由：* $\iota_{X_1}\omega=d1=0$，非退化性给出 $X_1=0$。
2. 把 $[\hat f,\hat g]=[-i\hbar\nabla_{X_f}+f,\ -i\hbar\nabla_{X_g}+g]$ 展开为四个对易子。函数–函数项 $[f,g]=0$。*理由：* 乘法算子相互对易。
3. 联络–联络项：$(-i\hbar)^2[\nabla_{X_f},\nabla_{X_g}] = -\hbar^2\big(\nabla_{[X_f,X_g]} + F_\nabla(X_f,X_g)\big)$。*理由：* 曲率定义 $F_\nabla(X,Y)=[\nabla_X,\nabla_Y]-\nabla_{[X,Y]}$。
4. 用 $[X_f,X_g]=X_{\{f,g\}}$（s4）以及 $F_\nabla(X_f,X_g)=-\tfrac{i}{\hbar}\omega(X_f,X_g)=-\tfrac{i}{\hbar}\{f,g\}$。故此项为 $-\hbar^2\nabla_{X_{\{f,g\}}} + i\hbar\{f,g\}$。*理由：* 关键引理与曲率条件。
5. 两个交叉项 $[-i\hbar\nabla_{X_f},g]+[f,-i\hbar\nabla_{X_g}]$。此时 $[\nabla_{X_f},g]=X_f(g)=\{f,g\}$（联络按莱布尼茨法则作用于积 $g\cdot s$，留下 $g$ 的方向导数）。故这些贡献 $-i\hbar\{f,g\}-(-i\hbar)\{g,f\}\cdot(\ldots)$；仔细地，$[-i\hbar\nabla_{X_f},g]=-i\hbar X_f(g)=-i\hbar\{f,g\}$ 且 $[f,-i\hbar\nabla_{X_g}]=+i\hbar X_g(f)=-i\hbar\{f,g\}$，合计为 $-2i\hbar\{f,g\}$。*理由：* $\nabla$ 在 $g\cdot s$ 上的莱布尼茨法则。
6. 把第 3–5 步相加：$[\hat f,\hat g] = -\hbar^2\nabla_{X_{\{f,g\}}} + i\hbar\{f,g\} - 2i\hbar\{f,g\}\cdot 0\,$——收集存留下来的项得 $-i\hbar\big(-i\hbar\nabla_{X_{\{f,g\}}} + \{f,g\}\big) = i\hbar\,\widehat{\{f,g\}}$。*理由：* 与定义 $\widehat{\{f,g\}}=-i\hbar\nabla_{X_{\{f,g\}}}+\{f,g\}$ 相匹配。$\blacksquare$

#### 整性（玻尔–索末菲）条件

曲率为 $-\tfrac{i}{\hbar}\omega$ 的丛 $L$ 并非总是存在。它是否存在是一个拓扑量子化条件。

> **定理 —— 韦伊整性。** 预量子线丛存在当且仅当 $\dfrac{\omega}{2\pi\hbar}$ 的上同调类是 **整的**：对 $M$ 中每个闭定向 $2$-曲面 $\Sigma\subseteq M$，
> $$
> \frac{1}{2\pi\hbar}\int_\Sigma \omega \;\in\; \mathbb{Z}.
> $$

**何以如此（思路）。** 任何复线丛的曲率在闭曲面上的积分都等于 $2\pi$ 乘以一个整数（其第一陈数 / 所围“磁单极”的个数）：$\frac{i}{2\pi}\int_\Sigma F_\nabla\in\mathbb{Z}$。代入 $F_\nabla=-\tfrac{i}{\hbar}\omega$ 得 $\frac{1}{2\pi\hbar}\int_\Sigma\omega\in\mathbb{Z}$。反之，一个整类可由某个线丛实现（陈–韦伊对应）。$\blacksquare$

> **玻尔–索末菲解释。** 对一个有周期轨道、其在相空间中围出区域 $\Sigma$ 的系统，$\int_\Sigma\omega=\oint_{\partial\Sigma}p\,dq$ 是该轨道的经典作用量；整性表明这个作用量以 $2\pi\hbar=h$ 为单位被量子化。这正是旧量子论的规则 $\oint p\,dq = nh$。s11 中球面面积为 $h$ 的倍数就是这个条件，也正是它迫使自旋成为半整数倍。

#### 障碍何时消失

在一个 *恰当* 辛流形上——即整体上有 $\omega=d\theta$ 的流形，比如任何余切丛 $T^*Q$（s3）——整性条件自动满足，因为对任何 *闭* 曲面 $\Sigma$（无边界）有 $\int_\Sigma\omega=\int_\Sigma d\theta=\oint_{\partial\Sigma}\theta=0$。带联络 $\nabla=d-\tfrac{i}{\hbar}\theta$ 的平凡丛 $L=M\times\mathbb{C}$ 于是把整个空间预量子化。这就是为何 $T^*\mathbb{R}^n$ 上的普通力学从不会遇到这个障碍——量子化条件只在紧相空间（如球面，那里 $\omega$ 整体上不恰当，其在整个球面上的积分是非零的总面积）上才起作用。

> **范例验证 —— $S^2$ 上的障碍是真实的。** 假设 $S^2$ 上的 $\omega$ 对某个整体定义的 $1$-形式 $\theta$ 满足 $\omega=d\theta$。则由斯托克斯定理 $\int_{S^2}\omega=\int_{S^2}d\theta=0$（球面是闭的）。但总面积为正，矛盾。因此 $\omega$ *不* 恰当，类 $[\omega]\ne0$ 于 $H^2(S^2)\cong\mathbb{R}$，且预量子丛是一个货真价实的非平凡线丛——恰是 s11 的单极丛 $\mathcal O(k)$。这是预量子化能探测到达布局部平凡性无法看到的整体拓扑这一点最干净的演示。

<a id="s10"></a>
### 极化与几何量子化；恢复正则量子化与希尔伯特空间

预量子化给出的希尔伯特空间太大了——截面同时依赖 $q$ *与* $p$，而量子波函数只依赖 $q$。**极化** 把依赖性减半。

> **定义 —— 极化。** $(M,\omega)$ 的 **极化** $P$ 是在每点对一个拉格朗日子空间 $P_x\subseteq T_xM\otimes\mathbb{C}$（复化切空间）的光滑选择，且它可积（在李括号下封闭）。它选出“波函数被允许保持常数的方向”。

两种基本类型：
- **实（竖直）极化。** $P=\mathrm{span}\{\partial/\partial p_i\}$：截面被要求沿动量方向协变常数，故只依赖 $q$。这恢复出 **薛定谔表象**。
- **凯勒（全纯）极化。** 用一个相容的 $J$（s8），$P=T^{0,1}M$，即反全纯方向：被极化的截面是 **全纯的**。这恢复出 **巴格曼/福克表象**。

> **定义 —— 量子希尔伯特空间。** **被量子化的希尔伯特空间** $\mathcal H$ 是被 **极化** 的预量子截面 $s$ 之空间：对所有 $X\in P$ 有 $\nabla_X s = 0$，内积由把 $\langle s,s'\rangle$ 对（刘维尔体积的一个半密度修正）积分给出。量子算子是保持 $P$ 的那些预量子 $\hat f$（即其流把被极化截面映为被极化截面者）。

#### 恢复正则量子化

> **范例恢复 —— 薛定谔算子。** 取 $M=T^*\mathbb{R}=\mathbb{R}^2$，$\omega=dq\wedge dp$，$\theta=p\,dq$ 故 $\nabla=d-\tfrac{i}{\hbar}p\,dq$，以及 **竖直** 极化 $P=\mathrm{span}\{\partial_p\}$。
> 1. 被极化条件 $\nabla_{\partial_p}s=0$ 读作 $\partial_p s - \tfrac{i}{\hbar}(p\,dq)(\partial_p)s = \partial_p s = 0$，故 $s=\psi(q)$ 只依赖 $q$。*理由：* $dq(\partial_p)=0$，故联络项消失，留下 $\partial_p s=0$。
> 2. 量子化 $f=q$：$X_q=-\partial_p$，$\nabla_{X_q}=-\partial_p + \tfrac{i}{\hbar}p\,dq(\partial_p)=-\partial_p$，作用在 $\psi(q)$ 上为 $0$。故 $\hat q=-i\hbar\nabla_{X_q}+q=q$：**乘以 $q$。** *理由：* 代入 $\hat f=-i\hbar\nabla_{X_f}+f$。
> 3. 量子化 $f=p$：$X_p=\partial_q$，且 $\nabla_{X_p}\psi = \partial_q\psi - \tfrac{i}{\hbar}p\,dq(\partial_q)\psi=\partial_q\psi-\tfrac{i}{\hbar}p\,\psi$。则 $\hat p = -i\hbar(\partial_q\psi - \tfrac{i}{\hbar}p\psi)+p\psi = -i\hbar\,\partial_q\psi - p\psi + p\psi = -i\hbar\,\partial_q\psi$。故 $\hat p = -i\hbar\,\partial_q$：**动量算子。** *理由：* $p\psi$ 项相消，留下微分算子。
> 4. 检验对易子：$[\hat q,\hat p]\psi = q(-i\hbar\partial_q\psi) - (-i\hbar\partial_q)(q\psi) = -i\hbar q\psi' + i\hbar(\psi + q\psi') = i\hbar\,\psi$。故 $[\hat q,\hat p]=i\hbar=i\hbar\,\widehat{\{q,p\}}$，因为 $\{q,p\}=1$。*理由：* 乘积法则；这是正则对易关系。

于是几何量子化仅从 $T^*\mathbb{R}$ 的几何就 *导出* 了被假设的薛定谔算子 $\hat q=q$、$\hat p=-i\hbar\partial_q$ 以及正则对易关系——没有任何量子化规则是人为强加的。

> **范例验证 —— 这些算子保持极化。** 为使 $\hat f$ 成为合法的量子算子，它必须把被极化截面（只依赖 $q$ 的函数）映为被极化截面。$\hat q=q$ 与 $\hat p=-i\hbar\partial_q$ 显然都把函数 $\psi(q)$ 送到另一个只依赖 $q$ 的函数，故它们保持 $P=\mathrm{span}\{\partial_p\}$。现在试 $f=qp$：$X_{qp}=q\partial_q - p\partial_p$，可算出 $\hat{qp}=-i\hbar(q\partial_q+\tfrac12)$，它仍保持 $P$（它对 $\partial_q$ 是一阶的）。但 $f=q^2p$ 产生一个含 $p$ 的算子，即 $\partial_q$ 乘以 $p$，它不把 $q$ 的函数送到 $q$ 的函数——它离开了极化。*理由：* 只有至多关于 $(q,p)$ 二次的可观测量才有仿射的哈密顿流，从而保持线性的竖直叶状结构。这是 **次序歧义** 的精确陈述：三次及更高次的可观测量在此方案中不可直接量子化，对它们的任何规定都带有一个真正的选择。

#### 内积以及为何需要半形式

在竖直极化下，被极化截面是函数 $\psi(q)$，自然的内积是薛定谔内积，
$$
\langle\psi,\psi'\rangle = \int_{\mathbb{R}^n}\overline{\psi(q)}\,\psi'(q)\,d^nq,
$$
恢复出 $L^2(\mathbb{R}^n)$。但货真价实的几何对象是 $L$ 的一个截面，它是 *复值的*；要对 $|\psi|^2$ 积分，需要叶空间 $Q$ 上的一个密度（测度）。叶空间本身不带典范测度。修补办法是把 $L$ 与沿极化的密度丛的一个平方根 $\delta$ 张量——一个 **半形式**——使得 $|s|^2$ 成为 $Q$ 上货真价实的 $n$-密度，无需选坐标即可积分。两个推论：

1. **一个无坐标的内积。** 配对 $\langle s,s'\rangle=\int_Q \langle s,s'\rangle_L\,(\text{来自 }\delta\otimes\bar\delta)$ 是良定义的，且与 $Q$ 如何坐标化无关。*理由：* 半形式乘以其共轭是一个最高次密度，即自然的被积量。
2. **一个真空移位。** 沿一个二次哈密顿量（如振子）的流输运半形式会获得一个额外相位——**马斯洛夫/亚辛修正**——其无穷小生成元给能量添加 $\tfrac12\sum\hbar\omega_i$。这正是 s11 中零点能的来源；没有半形式，几何量子化会预言基态能量为 $0$，与实验矛盾。

> **陷阱。** (i) 并非每个经典 $f$ 都保持给定的极化；对竖直 $P$ 只有至多二次的可观测量才行，这就是为何 $\widehat{q^2 p}$ 之类真正含糊（次序问题）。(ii) 实极化上朴素的内积可能发散或为零；严格理论用 **半形式**（典范丛的一个平方根）来同时修补测度与一个真空能移位——它正是在下一节产生 $\tfrac12\hbar\omega$ 基态能量的东西。

<a id="s11"></a>
### 范例 —— 量子化谐振子与 2-球面（自旋）

我们让整台机器贯穿两个基石性的例子，并恢复出教科书量子力学。

#### 经凯勒量子化的谐振子

> **设置。** $M=\mathbb{R}^2$，$\omega=dq\wedge dp$，哈密顿量 $H=\tfrac12(p^2+\omega_0^2 q^2)$（我们把角频率写作 $\omega_0$ 以免与形式 $\omega$ 冲突；为简便取 $\omega_0=1$，最后再恢复它）。

1. **复坐标。** 设 $z=\tfrac{1}{\sqrt{2}}(q+ip)$，$\bar z=\tfrac{1}{\sqrt2}(q-ip)$。则 $H=\tfrac12(q^2+p^2)=z\bar z$，且 $\omega = dq\wedge dp = i\,dz\wedge d\bar z$。*理由：* 直接代入；把 $dq\wedge dp$ 用 $dz,d\bar z$ 表示。
2. **凯勒极化与预量子丛。** 用 $\theta=\tfrac{i}{2}(\bar z\,dz - z\,d\bar z)$（满足 $-d\theta=\omega$ 的辛势）与全纯极化 $P=\mathrm{span}\{\partial_{\bar z}\}$。被极化截面取形式 $s = \psi(z)\,e^{-|z|^2/2\hbar}$，其中 $\psi$ **全纯**。*理由：* 用这个 $\theta$ 求解 $\nabla_{\partial_{\bar z}}s=0$ 给出高斯函数乘以一个全纯函数——这就是 **巴格曼–福克空间**。
3. **希尔伯特空间。** $\mathcal H = \{\psi \text{ 全纯}: \int |\psi|^2 e^{-|z|^2/\hbar}\,d^2z<\infty\}$，正交归一基为单项式 $\psi_n(z)=z^n/\sqrt{n!\,\hbar^n}$，$n=0,1,2,\dots$。*理由：* 单项式在高斯权下正交（标准高斯积分 $\int z^m\bar z^n e^{-|z|^2/\hbar}d^2z\propto\delta_{mn}n!\hbar^n$）。
4. **算子。** 量子化 $z$ 与 $\bar z$ 给出 **湮灭/产生算子**：$\hat z \to \hat a = \sqrt{\hbar}\,\partial_z$-伴随结构给出 $\hat a\,\psi_n=\sqrt{n}\,\psi_{n-1}$ 与 $\hat a^\dagger\psi_n=\sqrt{n+1}\,\psi_{n+1}$，且 $[\hat a,\hat a^\dagger]=1$。*理由：* 巴格曼表象把 $\hat a^\dagger$ 实现为乘以 $z/\sqrt\hbar$，把 $\hat a$ 实现为 $\sqrt\hbar\,\partial_z$。
5. **谱。** 在 **半形式修正**（s10）下，$\hat H = \hbar\omega_0\big(\hat a^\dagger\hat a + \tfrac12\big)$，故本征值为
$$
E_n = \hbar\omega_0\left(n+\tfrac12\right),\qquad n=0,1,2,\dots
$$
*理由：* $\hat a^\dagger\hat a\,\psi_n = n\,\psi_n$；那个 $+\tfrac12$ 是半形式/零点贡献。这恰是教科书中的谐振子谱，包括零点能 $\tfrac12\hbar\omega_0$。
6. **薛定谔图景中的基态。** 通过巴格曼变换把全纯真空 $\psi_0=$ 常数 翻译回竖直（位置）极化，得到高斯波函数 $\langle q\mid 0\rangle \propto e^{-\omega_0 q^2/2\hbar}$，即熟悉的振子基态。*理由：* 真空被 $\hat a=\tfrac{1}{\sqrt{2\hbar\omega_0}}(\omega_0 q + \hbar\partial_q)$ 湮灭，而求解 $\hat a\psi_0=0$ 是一阶常微分方程 $\omega_0 q\,\psi_0 + \hbar\psi_0'=0$，其高斯解。于是两种极化给出 *酉等价* 的希尔伯特空间——福克空间与 $L^2(\mathbb{R})$——由一个显式积分变换相连，这阐明了量子化对极化选择的一般（此处精确）无关性。

#### 2-球面与自旋的量子化

> **设置。** $M=S^2$，半径 $r$，面积形式 $\omega = r^2\,\sin\phi\,d\phi\wedge d\theta$（球坐标），总面积 $\int_{S^2}\omega = 4\pi r^2$。把 $S^2$ 与 $\mathbb{CP}^1$ 等同；它是凯勒的（s8）。这是 **经典自旋相空间**：一个点是自旋向量的一个方向。

1. **整性 / 玻尔–索末菲。** 预量子丛存在当且仅当 $\frac{1}{2\pi\hbar}\int_{S^2}\omega\in\mathbb{Z}$，即 $\frac{4\pi r^2}{2\pi\hbar}=\frac{2r^2}{\hbar}=:k\in\mathbb{Z}_{\ge0}$。*理由：* 韦伊整性定理（s9）。故球面面积被量子化：$\text{面积}=2\pi\hbar k = hk$。
2. **丛。** $\mathbb{CP}^1$ 上陈数为 $k$ 的线丛是 $\mathcal O(k)$，即超平面丛的 $k$ 次幂。*理由：* $\mathbb{CP}^1$ 上的线丛由一个整数（其次数，等于曲率积分）分类。
3. **希尔伯特空间。** $\mathcal O(k)$ 的全纯（凯勒极化）截面是两个复变量 $(z_0,z_1)$ 的 $k$ 次齐次多项式，构成一个维数为
$$
\dim\mathcal H = k+1
$$
的空间。*理由：* $\mathbb{CP}^1$ 上 $\mathcal O(k)$ 的全纯截面恰是 $k$ 次齐次多项式，共有 $k+1$ 个（基为 $z_0^k, z_0^{k-1}z_1,\dots,z_1^k$）。
4. **自旋。** 设 $k=2j$，故 $j=k/2\in\{0,\tfrac12,1,\tfrac32,\dots\}$。则 $\dim\mathcal H = 2j+1$，恰是 $SU(2)$ 的自旋-$j$ 表示的维数。*理由：* 匹配 $k+1=2j+1$。
5. **算子。** $SU(2)$ 矩映射（s6）——球面上经典自旋向量 $\vec S$ 的各分量——量子化为作用在 $k$ 次多项式上的 **角动量算子** $\hat J_x,\hat J_y,\hat J_z$，满足 $[\hat J_a,\hat J_b]=i\hbar\,\epsilon_{abc}\hat J_c$，且 $\hat J^2 = \hbar^2 j(j+1)$。*理由：* 这些多项式承载自旋-$j$ 不可约表示；这些括号是 s6 中量子化的泊松括号 $\{S_a,S_b\}=\epsilon_{abc}S_c$。

> **要点。** 球面的几何量子化无需任何外部输入就重现了量子自旋的整个理论：维数 $2j+1$、$j$ 的半整数取值（由整性迫使）、角动量代数以及卡西米尔 $j(j+1)$。经典相空间是一个球面；其以 $h$ 为单位度量的面积 *就是* 自旋量子数的两倍。这是本指南论点最生动的演示——量子力学就是相空间的几何，被弄成整数。

> **常见陷阱回顾。** (i) 忘记半形式修正会丢失零点能与正确的 $j(j+1)$。(ii) 整性是一个 *整体* 条件——达布局部性（s2）看不到它；这就是为何有限总面积很重要。(iii) 不同极化在 *此处* 给出酉等价的理论，但一般而言等价性（布拉特纳–科斯坦–斯特恩伯格配对）是微妙的。

---

*本指南从辛几何的线性根基一路构建到它的量子回报：辛形式是一个反对称、非退化、闭的 $2$-形式；达布定理说它没有局部不变量；余切丛以 $\omega=-d\theta$ 典范地供给它；哈密顿场与泊松括号把函数转化为动力学，雅可比恒等式直接从 $d\omega=0$ 流出；辛同胚——包括时间演化——保持 $\omega$ 从而保持相空间体积；矩映射把诺特定理几何化，而约化沿对称性缩小空间；拉格朗日子流形是经典生成函数与量子态都栖身其上的半维骨架；相容的复/凯勒结构通往全纯几何。在这一基础上，预量子化精确地实现了狄拉克对应，韦伊整性（玻尔–索末菲）条件以 $h$ 为单位量子化面积，而极化把希尔伯特空间削减到物理的那个——恢复出薛定谔算子、带零点能的谐振子阶梯，以及从一个球面的面积出发的量子自旋完整理论。把任何带框的定义或编号证明当作参考随时回顾，并紧扣这唯一的论点：经典力学是一个闭 $2$-形式的几何，而量子力学是当其面积被迫为整数时这种几何所变成的样子。*
