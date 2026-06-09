[English](tensor-analysis.md) · **中文**

# 高级张量分析，*在坐标系中对弯曲空间作微积分。*

*本文是一份关于张量微积分的实用手册，内容正是相对论与连续介质物理中实际使用的那套工具。如果说配套指南是在概念层面建立几何，那么本文则要卷起袖子动手干：我们摆弄指标、衡量张量密度、用度量升降指标、作协变微分、用 $\sqrt{-g}$ 积分，并直接从纸面上读出麦克斯韦方程组、能量–动量守恒以及狄拉克算子。每一个恒等式都被推导出来；每一个指标都有交代。*

[← 返回全部指南](../README.zh.md)

**前置知识。** 本指南是**微分几何与张量**指南在应用与计算层面的配套。我们从中取用以下事实，并在用到时各用一行重述：**张量**是一个多重线性对象，其分量在坐标变换下携带变换律 $T'^{\mu}{}_{\nu}=\frac{\partial x'^\mu}{\partial x^\alpha}\frac{\partial x^\beta}{\partial x'^\nu}T^{\alpha}{}_{\beta}$；**度量** $g_{\mu\nu}$ 是一个对称的非退化 $(0,2)$ 张量；**协变导数** $\nabla$ 用**克里斯托费尔符号** $\Gamma^\lambda{}_{\mu\nu}=\tfrac12 g^{\lambda\sigma}(\partial_\mu g_{\sigma\nu}+\partial_\nu g_{\sigma\mu}-\partial_\sigma g_{\mu\nu})$ 来修正普通偏导数。我们**不**重新证明这些事实；我们直接拿来用。全文采用重复指标求和约定（爱因斯坦约定），希腊指标 $\mu,\nu,\dots$ 遍历 $n$ 个时空坐标，并记 $\partial_\mu\equiv\partial/\partial x^\mu$。

## A 部分 · 指标的代数

<a id="s0"></a>
### 动机 — 以坐标显式的张量微积分作为物理学的工作语言

配套指南宣扬的是坐标无关性：张量*本身*是一个几何对象，分量只是它在所选图卡中的投影。这是*理解*理论的正确方式。然而，这并不是任何人在*计算*测地线、电磁场或写在纸上的某个度量的爱因斯坦张量时所采用的方式。要做这些计算，你需要一项对偶的技能：对指标、密度以及度量因子 $\sqrt{-g}$ 进行流畅、可靠的操作。

#### 我们要解决什么问题？

一位物理学家递给你一个度量——比如施瓦茨希尔德线元——并要你算出某个流的散度、电磁波辐射的能量，或某条轨道的守恒量。每个答案都是一个*数*或一个*场*，通过一串确定的指标运算提取出来。危险在于，诸如 $\partial_\mu V^\nu$ 或列维-奇维塔*符号* $\epsilon_{\mu\nu\rho\sigma}$ 这样的中间量看起来像张量，但**并不是**：它们的变换方式不对，把它们当作张量来用会产生错误的、依赖于坐标的答案。本指南的任务就是教你哪些对象是真正的张量，哪些是**密度**（被雅可比行列式的某个幂加权的张量），以及究竟哪些组合能恢复张量性。

#### 计划

A 部分是纯代数：**商定理**（判定张量的逆向检验）、对称/反对称分解、缩并，然后是**张量密度**、**列维-奇维塔符号与张量之辨**，以及 $\sqrt{-g}$ 的角色（s1–s2）。B 部分讲实践中的度量以及任意张量的**协变微分**、散度、拉普拉斯算子，以及关键的简化 $\nabla_\mu(\sqrt{-g}\,V^\mu)=\partial_\mu(\sqrt{-g}\,V^\mu)$（s3–s4）。C 部分是形式的微积分——**霍奇星算子**、**余微分**、用不变体积形式作**积分**，以及**散度定理**（s5–s6）。D 部分是把物理做对：**电磁学**（s7）、**应力–能量张量**及其守恒（s8）、借助李导数与基灵矢量得到的**对称性**与守恒荷（s9），以及对弯曲空间上**旋量**与**狄拉克算子**的首次具体审视（s10）。

> **直觉。** 变换律是一份契约。真正的张量遵守它；密度遵守一份带有额外雅可比因子的*修改后的*契约。指标操弄中几乎每一个"悖论"——为什么 $\partial_\mu V^\mu$ 不是散度，为什么 $d^nx$ 不是不变量，为什么 $\epsilon_{\mu\nu\rho\sigma}$ 不是张量——都是同一份契约被悄悄破坏、再通过插入 $\sqrt{-g}$ 来修补的结果。

<a id="s1"></a>
### 分量形式的张量代数：商定理、对称性与缩并

我们汇集那些把张量变成新张量的代数运算，并在每种情形下证明变换契约都被保持。

#### 重述变换契约

> **定义 — 张量分量。** 在坐标变换 $x\mapsto x'$ 下，将雅可比矩阵及其逆记为
> $$
> J^{\mu'}{}_{\alpha}=\frac{\partial x'^{\mu}}{\partial x^{\alpha}},\qquad (J^{-1})^{\alpha}{}_{\mu'}=\frac{\partial x^{\alpha}}{\partial x'^{\mu}}.
> $$
> 一个 $(p,q)$ **张量**的分量为每个上指标携带一个 $J$ 因子、为每个下指标携带一个 $J^{-1}$ 因子：
> $$
> T'^{\mu_1\dots\mu_p}{}_{\nu_1\dots\nu_q}=\frac{\partial x'^{\mu_1}}{\partial x^{\alpha_1}}\cdots\frac{\partial x^{\beta_1}}{\partial x'^{\nu_1}}\cdots\,T^{\alpha_1\dots\alpha_p}{}_{\beta_1\dots\beta_q}.
> $$

由链式法则 $\frac{\partial x'^\mu}{\partial x^\alpha}\frac{\partial x^\alpha}{\partial x'^\nu}=\frac{\partial x'^\mu}{\partial x'^\nu}=\delta^\mu_\nu$，这些雅可比量满足 $J^{\mu'}{}_\alpha (J^{-1})^{\alpha}{}_{\nu'}=\delta^{\mu'}{}_{\nu'}$。下面所有工作都仰仗这一个关系。

#### 缩并把阶数降低 $(1,1)$

> **定理（缩并）。** 若 $T^{\mu}{}_{\nu}$ 是一个 $(1,1)$ 张量的分量，则单个数 $S=T^{\mu}{}_{\mu}$（已求和）是一个标量——一个 $(0,0)$ 张量。更一般地，把一个 $(p,q)$ 张量的一个上指标与一个下指标求和，得到一个 $(p-1,q-1)$ 张量。

*证明。*
1. 写出被缩并指标对的变换律：由 $(1,1)$ 张量的定义，将两个自由指标取作相同并求和，得 $T'^{\mu}{}_{\mu}=\dfrac{\partial x'^\mu}{\partial x^\alpha}\dfrac{\partial x^\beta}{\partial x'^\mu}\,T^{\alpha}{}_{\beta}$。
2. 把共享被求和指标 $\mu$ 的两个雅可比因子归到一起：它们构成 $\dfrac{\partial x^\beta}{\partial x'^\mu}\dfrac{\partial x'^\mu}{\partial x^\alpha}$。
3. 由链式法则，这等于 $\dfrac{\partial x^\beta}{\partial x^\alpha}=\delta^\beta_\alpha$（坐标 $x^\alpha$ 彼此独立，故 $\partial x^\beta/\partial x^\alpha$ 是克罗内克 delta）。
4. 因此 $T'^{\mu}{}_{\mu}=\delta^\beta_\alpha T^{\alpha}{}_{\beta}=T^{\alpha}{}_{\alpha}$。该数在坐标变换下不变，这恰恰说明它是标量。$\blacksquare$
5. 一般情形完全相同：被缩并的指标对像第 3 步那样贡献一个 $\delta$，而余下的 $p-1$ 个上指标与 $q-1$ 个下指标保留各自的雅可比因子，从而给出 $(p-1,q-1)$ 变换律。

> **例。** 在 4 维中取 $T^{\mu}{}_{\nu}=\mathrm{diag}(2,3,5,7)$。则 $T^{\mu}{}_{\mu}=2+3+5+7=17$。这个 $17$ 就是**迹**，它在每一个坐标系中都相同——一个真正的不变量——而各个对角元本身则不是。

#### 对称部分与反对称部分

> **定义。** 对一个 $(0,2)$ 张量 $T_{\mu\nu}$，定义
> $$
> T_{(\mu\nu)}=\tfrac12\bigl(T_{\mu\nu}+T_{\nu\mu}\bigr)\quad\text{(symmetric part)},\qquad
> T_{[\mu\nu]}=\tfrac12\bigl(T_{\mu\nu}-T_{\nu\mu}\bigr)\quad\text{(antisymmetric part)}.
> $$
> 对 $k$ 个指标，圆括号表示对全部 $k!$ 个置换取平均，方括号表示同样的平均但按每个置换的**符号**（即宇称，偶置换为 $+1$，奇置换为 $-1$）加权。

> **定理。** $T_{(\mu\nu)}$ 与 $T_{[\mu\nu]}$ 本身都是 $(0,2)$ 张量，且每个 $(0,2)$ 张量都唯一地分解为 $T_{\mu\nu}=T_{(\mu\nu)}+T_{[\mu\nu]}$。

*证明。*
1. 变换律 $T'_{\mu\nu}=\dfrac{\partial x^\alpha}{\partial x'^\mu}\dfrac{\partial x^\beta}{\partial x'^\nu}T_{\alpha\beta}$ 关于分量 $T_{\alpha\beta}$ 是**线性**的，故分量的任意固定线性组合都以同样的方式变换。
2. 交换后的对象 $T_{\nu\mu}$ 变换为 $T'_{\nu\mu}=\dfrac{\partial x^\alpha}{\partial x'^\nu}\dfrac{\partial x^\beta}{\partial x'^\mu}T_{\alpha\beta}$；重新标记哑指标 $\alpha\leftrightarrow\beta$ 表明这等于 $\dfrac{\partial x^\alpha}{\partial x'^\mu}\dfrac{\partial x^\beta}{\partial x'^\nu}T_{\beta\alpha}$，即交换作用在分量上，而非作用在雅可比因子上。
3. 于是 $\tfrac12(T'_{\mu\nu}\pm T'_{\nu\mu})=\dfrac{\partial x^\alpha}{\partial x'^\mu}\dfrac{\partial x^\beta}{\partial x'^\nu}\cdot\tfrac12(T_{\alpha\beta}\pm T_{\beta\alpha})$——每一部分都携带正确的两个 $J^{-1}$ 因子，故每一部分都是 $(0,2)$ 张量。
4. 两部分相加即还原 $T_{\mu\nu}$；分解是唯一的，因为若 $S+A=0$ 且 $S$ 对称、$A$ 反对称，则交换指标给出 $S-A=0$，故 $S=A=0$。$\blacksquare$

> **陷阱 — 对称性只有小心处理才能在指标升降中保持。** 若 $T_{\mu\nu}$ 对称，则 $T^{\mu\nu}=g^{\mu\alpha}g^{\nu\beta}T_{\alpha\beta}$ 也对称，但一个*混合*对象 $T^\mu{}_\nu$ 没有任何对称性，因为它的两个指标处在不同的高度。一个常见错误是把 $T^\mu{}_\nu$ 当作矩阵那样"转置"；该操作不是坐标协变的。

> **有用的恒等式。** 一个对称张量 $S^{\mu\nu}$ 与一个反对称张量 $A_{\mu\nu}$ 的缩并为零：$S^{\mu\nu}A_{\mu\nu}=0$。

*证明。* 重命名哑指标 $\mu\leftrightarrow\nu$：$S^{\mu\nu}A_{\mu\nu}=S^{\nu\mu}A_{\nu\mu}$。现用 $S^{\nu\mu}=S^{\mu\nu}$（对称性）与 $A_{\nu\mu}=-A_{\mu\nu}$（反对称性）：右边为 $-S^{\mu\nu}A_{\mu\nu}$。一个等于自身相反数的量必为零。$\blacksquare$

#### 商定理 — 一种逆向检验

通常，验证某个对象的*某个缩并*是张量，要比直接检验该对象本身更容易。商定理说这就足够了。

> **定理（商定理）。** 设 $K(\mu,\nu)$ 是在每个坐标系中都给定的一个双指标数组。假设对**每一个**矢量（即 $(1,0)$ 张量）$V^\nu$，量 $W_\mu=K(\mu,\nu)V^\nu$ 都是某个 $(0,1)$ 张量（即余矢量）的分量数组。则 $K(\mu,\nu)$ 是某个 $(0,2)$ 张量 $K_{\mu\nu}$ 的分量。

*证明。*
1. 由假设，$W_\mu=K(\mu,\nu)V^\nu$ 对每个输入矢量都按余矢量变换：$W'_{\mu}=\dfrac{\partial x^\alpha}{\partial x'^\mu}W_\alpha$。
2. 把两边按分量展开。左边：由 $K'$ 在带撇标架中的定义，$W'_\mu=K'(\mu,\nu)V'^{\nu}$。右边：$\dfrac{\partial x^\alpha}{\partial x'^\mu}K(\alpha,\beta)V^\beta$。
3. 在带撇标架中表示输入：由于 $V$ 是矢量，$V^\beta=\dfrac{\partial x^\beta}{\partial x'^\nu}V'^{\nu}$。代入右边：$\dfrac{\partial x^\alpha}{\partial x'^\mu}\dfrac{\partial x^\beta}{\partial x'^\nu}K(\alpha,\beta)\,V'^{\nu}$。
4. 令 $W'_\mu$ 的两个表达式相等：对**一切** $V'^\nu$，$\Bigl[K'(\mu,\nu)-\dfrac{\partial x^\alpha}{\partial x'^\mu}\dfrac{\partial x^\beta}{\partial x'^\nu}K(\alpha,\beta)\Bigr]V'^{\nu}=0$。
5. 一个在每个矢量上都为零的线性型其系数必为零（依次取 $V'^\nu$ 为各个基矢量）。故方括号为零：
$$
K'(\mu,\nu)=\frac{\partial x^\alpha}{\partial x'^\mu}\frac{\partial x^\beta}{\partial x'^\nu}K(\alpha,\beta),
$$
这正是 $(0,2)$ 张量的变换律。$\blacksquare$

> **例 — 度量通过检验。** 线元 $ds^2=g_{\mu\nu}\,dx^\mu dx^\nu$ 是标量（一个不变的长度）。将它写为 $g_{\mu\nu}V^\mu W^\nu$，其中 $V,W$ 是任意切矢量，则对一切输入结果都是标量；对商定理用两次即表明 $g_{\mu\nu}$ 是一个真正的 $(0,2)$ 张量。我们从未需要直接检查它的变换律。

<a id="s2"></a>
### 张量密度、列维-奇维塔符号与张量之辨，以及 $\sqrt{-g}$

若干不可或缺的对象——体积元、置换符号、度量行列式——都**不是**张量。它们是**密度**，而理解它们的权重正是不变积分的关键。

#### 密度的定义

> **定义 — 权重为 $w$ 的张量密度。** 一个**权重为 $w$ 的张量密度**像张量那样变换，但带有一个额外因子，即雅可比行列式的 $w$ 次幂：
> $$
> \tilde T'^{\mu\dots}{}_{\nu\dots}=\left(\det\frac{\partial x}{\partial x'}\right)^{w}\frac{\partial x'^\mu}{\partial x^\alpha}\cdots\frac{\partial x^\beta}{\partial x'^\nu}\cdots\,\tilde T^{\alpha\dots}{}_{\beta\dots}.
> $$
> 这里 $\det\frac{\partial x}{\partial x'}=\det(J^{-1})$ 是逆雅可比矩阵的行列式。权重为 $0$ 的密度就是普通张量。

#### 列维-奇维塔符号是权重为 $\pm1$ 的密度，而非张量

> **定义 — 列维-奇维塔符号。** 在 $n$ 维中，$\epsilon_{\mu_1\dots\mu_n}$ 是**固定**数组：当 $(\mu_1,\dots,\mu_n)$ 是 $(1,\dots,n)$ 的偶置换时等于 $+1$，奇置换时等于 $-1$，任意指标重复时等于 $0$。同一组数值在每个坐标系中都被声明使用——正是这一点使它成为一个符号，而非张量。

> **定理。** 在所有标架中都取这些固定值的列维-奇维塔符号 $\epsilon_{\mu_1\dots\mu_n}$ 是一个**权重为 $-1$** 的张量密度。上指标符号 $\epsilon^{\mu_1\dots\mu_n}$（同样的值）是权重为 $+1$ 的密度。

*证明。*
1. 回忆行列式展开：对任意 $n\times n$ 矩阵 $A^\mu{}_\nu$，$\det A\,\epsilon_{\nu_1\dots\nu_n}=\epsilon_{\mu_1\dots\mu_n}A^{\mu_1}{}_{\nu_1}\cdots A^{\mu_n}{}_{\nu_n}$。这是行列式的余子式/莱布尼茨公式，恒等成立。
2. 取 $A^\mu{}_\nu=\dfrac{\partial x^\mu}{\partial x'^\nu}=(J^{-1})^\mu{}_\nu$，其行列式为 $\det(J^{-1})$：
$$
\det(J^{-1})\,\epsilon_{\nu_1\dots\nu_n}=\frac{\partial x^{\mu_1}}{\partial x'^{\nu_1}}\cdots\frac{\partial x^{\mu_n}}{\partial x'^{\nu_n}}\,\epsilon_{\mu_1\dots\mu_n}.
$$
3. 把它读作一条变换律。右边恰是"$\epsilon$ 的张量变换"；左边是"$\det(J^{-1})$ 乘以新标架中的（同一个）符号"。求解得知，新标架中的符号等于 $(\det(J^{-1}))^{-1}$ 乘以张量变换后的符号——但我们*声明*符号不变，故这一差异 $(\det(J^{-1}))^{+1}$ 通过赋予权重 $w=-1$ 而被吸收。对照 $w=-1$ 的定义即确认无误。$\blacksquare$

#### 度量行列式携带权重 $-2$

> **定理。** 设 $g=\det(g_{\mu\nu})$。在坐标变换下，$g'=(\det J^{-1})^{2}\,g$。故 $g$ 是权重为 $-2$ 的标量密度，而 $\sqrt{|g|}$ 是权重为 $-1$ 的标量密度。

*证明。*
1. 度量按 $g'_{\mu\nu}=\dfrac{\partial x^\alpha}{\partial x'^\mu}\dfrac{\partial x^\beta}{\partial x'^\nu}g_{\alpha\beta}$ 变换，即用矩阵形式写 $g'=(J^{-1})^{\mathsf T} g\,(J^{-1})$。
2. 取行列式：利用 $\det(AB)=\det A\det B$ 与 $\det A^{\mathsf T}=\det A$，得 $\det g'=\det((J^{-1})^{\mathsf T})\det g\,\det(J^{-1})=(\det J^{-1})^2\det g$。
3. 故 $g'=(\det J^{-1})^2 g$（权重 $-2$），取平方根得 $\sqrt{|g'|}=|\det J^{-1}|\sqrt{|g|}$（权重 $-1$，至多差一个由定向追踪的符号）。在洛伦兹号差下 $g<0$，故我们写 $\sqrt{-g}$。$\blacksquare$

#### 列维-奇维塔*张量*：把符号乘以 $\sqrt{-g}$

> **定义 — 列维-奇维塔张量。** 定义 $\varepsilon_{\mu_1\dots\mu_n}=\sqrt{-g}\;\epsilon_{\mu_1\dots\mu_n}$。

> **定理。** $\varepsilon_{\mu_1\dots\mu_n}$ 是一个真正的 $(0,n)$ 张量，且升指标版本在洛伦兹号差下满足 $\varepsilon^{\mu_1\dots\mu_n}=\dfrac{\mathrm{sgn}(g)}{\sqrt{-g}}\,\epsilon^{\mu_1\dots\mu_n}=-\dfrac{1}{\sqrt{-g}}\,\epsilon^{\mu_1\dots\mu_n}$。

*证明。*
1. 我们断言乘积 $\sqrt{-g}\,\epsilon_{\mu_1\dots\mu_n}$ 像真正的 $(0,n)$ 张量那样变换：密度因子 $\sqrt{-g}$（权重 $-1$）恰好抵消符号的反常雅可比因子，只留下普通的张量变换律。以下第 2–4 步将直接予以验证。
2. 把两条变换律结合起来。张量候选者变换为
$$
\varepsilon'_{\nu_1\dots\nu_n}=\sqrt{-g'}\;\epsilon_{\nu_1\dots\nu_n}=|\det J^{-1}|\sqrt{-g}\;\epsilon_{\nu_1\dots\nu_n}.
$$
3. 由符号的行列式恒等式（上一证明的第 2 步），$\sqrt{-g}\,\epsilon_{\nu_1\dots\nu_n}=\dfrac{1}{\det J^{-1}}\,\dfrac{\partial x^{\mu_1}}{\partial x'^{\nu_1}}\cdots\dfrac{\partial x^{\mu_n}}{\partial x'^{\nu_n}}\bigl(\sqrt{-g}\,\epsilon_{\mu_1\dots\mu_n}\bigr)$。代入得
$$
\varepsilon'_{\nu_1\dots\nu_n}=\frac{|\det J^{-1}|}{\det J^{-1}}\frac{\partial x^{\mu_1}}{\partial x'^{\nu_1}}\cdots\frac{\partial x^{\mu_n}}{\partial x'^{\nu_n}}\,\varepsilon_{\mu_1\dots\mu_n}.
$$
4. 对保定向的变换 $\det J^{-1}>0$，比值为 $+1$，这恰是 $(0,n)$ 张量变换律。$\blacksquare$

> **例 — 球面体积。** 在 $\mathbb{R}^3$ 中取球坐标下的平直度量，$g=\mathrm{diag}(1,r^2,r^2\sin^2\theta)$，故 $\sqrt{g}=r^2\sin\theta$。不变体积元 $\sqrt{g}\,dr\,d\theta\,d\phi=r^2\sin\theta\,dr\,d\theta\,d\phi$ 正是熟悉的雅可比因子——而它作为密度 $\sqrt{g}$ 自动出现，无需任何临时凑出来的计算。光秃秃的符号乘积 $dr\,d\theta\,d\phi$ 会给出错误的、依赖坐标的体积。

## B 部分 · 度量与协变微分

<a id="s3"></a>
### 实践中的度量：升降指标与标准正交标架

度量是矢量与余矢量之间的转换装置，也是通过标准正交标架通向平直空间直觉的桥梁。

#### 升指标与降指标

> **定义。** **逆度量** $g^{\mu\nu}$ 由 $g^{\mu\alpha}g_{\alpha\nu}=\delta^\mu_\nu$ 定义。降指标即与 $g_{\mu\nu}$ 缩并，升指标即与 $g^{\mu\nu}$ 缩并：
> $$
> V_\mu=g_{\mu\nu}V^\nu,\qquad V^\mu=g^{\mu\nu}V_\nu.
> $$

> **定理（指标操弄的相容性）。** 对同一指标先降后升即还原原来的张量。

*证明。* 先降后升：利用逆关系与 $\delta$ 的定义，$g^{\rho\mu}V_\mu=g^{\rho\mu}g_{\mu\nu}V^\nu=\delta^\rho_\nu V^\nu=V^\rho$。$\blacksquare$

> **例 — 闵可夫斯基。** 取 $\eta_{\mu\nu}=\mathrm{diag}(-1,+1,+1,+1)$，矢量 $V^\mu=(V^0,V^1,V^2,V^3)$ 降指标得 $V_\mu=(-V^0,V^1,V^2,V^3)$。范数 $V^\mu V_\mu=-(V^0)^2+(V^1)^2+(V^2)^2+(V^3)^2$ 是闵可夫斯基间隔的平方——对类时矢量为负，正是这一符号约定把时间与空间区分开来。

#### 标准正交标架：维尔拜因与四标架

一般的度量是杂乱的，但在每一个点上我们都能选取一个基，使度量看起来恰如平直的闵可夫斯基度量。完成这件事的基变换矩阵就是**维尔拜因**。

> **定义 — 维尔拜因 / 四标架。** **维尔拜因**（德语"多条腿"；在 4 维中称**四标架**或**标架场**）是一组 $n$ 个余矢量场 $e^a{}_\mu$，由一个**标架指标** $a$（拉丁字母）标记，满足
> $$
> g_{\mu\nu}=e^a{}_\mu e^b{}_\nu\,\eta_{ab},
> $$
> 其中 $\eta_{ab}=\mathrm{diag}(-1,+1,\dots,+1)$ 是常值**标架度量**。逆维尔拜因 $e_a{}^\mu$ 满足 $e^a{}_\mu e_a{}^\nu=\delta^\nu_\mu$ 与 $e^a{}_\mu e_b{}^\mu=\delta^a_b$。

直觉如下：$e^a{}_\mu$ 把一个坐标基（弯曲的、"世界"）指标 $\mu$ 转换成一个标准正交标架（平直的、"洛伦兹"）指标 $a$。在该标架中，所有几何在局部都是闵可夫斯基的；维尔拜因记录了局部平直标架是如何粘贴到坐标网格上的。

> **定理。** 维尔拜因分解 $g_{\mu\nu}=e^a{}_\mu e^b{}_\nu\eta_{ab}$ 重现行列式关系 $\sqrt{-g}=|\det e^a{}_\mu|\equiv e$。

*证明。*
1. 把定义读作矩阵方程 $g=e^{\mathsf T}\eta\,e$（略去指标，$e$ 即矩阵 $e^a{}_\mu$）。
2. 取行列式：由乘法性与 $\det e^{\mathsf T}=\det e$，$\det g=(\det e)^2\det\eta$。
3. 由于在洛伦兹号差下 $\det\eta=-1$，故 $\det g=-(\det e)^2$，于是 $-g=(\det e)^2$ 且 $\sqrt{-g}=|\det e|$。$\blacksquare$

> **陷阱 — 两套指标字母表。** 标架指标 $a,b$ 用**常值** $\eta_{ab}$ 升降；世界指标 $\mu,\nu$ 用 $g_{\mu\nu}$ 升降。把它们混用——例如用度量去降一个标架指标——是无意义的。维尔拜因是在这两套字母表之间互换的*唯一*合法途径。

> **为何重要。** 旋量（s10）根本无法用世界指标定义；它们生活在局部洛伦兹群的表示中，而该群作用于标架指标。因此四标架不是一种便利，而是在弯曲空间上处理费米子的必需品。

<a id="s4"></a>
### 协变微分、散度、拉普拉斯算子，以及 $\nabla_\mu(\sqrt{-g}\,V^\mu)=\partial_\mu(\sqrt{-g}\,V^\mu)$

张量分量的普通偏导数不是张量；协变导数用克里斯托费尔修正项修复这一点，每个指标一项。

#### 一般规则

> **定义 — $(p,q)$ 张量的协变导数。** 每个上指标得到一个 $+\Gamma$ 项，每个下指标得到一个 $-\Gamma$ 项：
> $$
> \nabla_\lambda T^{\mu_1\dots}{}_{\nu_1\dots}=\partial_\lambda T^{\mu_1\dots}{}_{\nu_1\dots}+\Gamma^{\mu_1}{}_{\lambda\sigma}T^{\sigma\dots}{}_{\nu_1\dots}+\cdots-\Gamma^{\sigma}{}_{\lambda\nu_1}T^{\mu_1\dots}{}_{\sigma\dots}-\cdots
> $$
> 按所示模式每个指标对应一个修正项。

对标量 $\nabla_\lambda f=\partial_\lambda f$；对矢量 $\nabla_\lambda V^\mu=\partial_\lambda V^\mu+\Gamma^\mu{}_{\lambda\sigma}V^\sigma$；对余矢量 $\nabla_\lambda\omega_\mu=\partial_\lambda\omega_\mu-\Gamma^\sigma{}_{\lambda\mu}\omega_\sigma$。度量是协变常值的，$\nabla_\lambda g_{\mu\nu}=0$（度量相容性，已在配套指南中证明），正因如此升降指标与 $\nabla$ 可交换。

#### 克里斯托费尔符号的一个关键缩并

> **引理。** $\Gamma^\mu{}_{\mu\lambda}=\partial_\lambda\ln\sqrt{-g}=\dfrac{1}{\sqrt{-g}}\partial_\lambda\sqrt{-g}$。

*证明。*
1. 把克里斯托费尔定义在其上指标与一个下指标上缩并：$\Gamma^\mu{}_{\mu\lambda}=\tfrac12 g^{\mu\sigma}(\partial_\mu g_{\sigma\lambda}+\partial_\lambda g_{\sigma\mu}-\partial_\sigma g_{\mu\lambda})$。
2. 第一项与第三项相消：在第三项中重新标记 $\mu\leftrightarrow\sigma$，$g^{\mu\sigma}\partial_\sigma g_{\mu\lambda}=g^{\sigma\mu}\partial_\mu g_{\sigma\lambda}$，因 $g^{\mu\sigma}$ 对称故与第一项相同。于是 $\Gamma^\mu{}_{\mu\lambda}=\tfrac12 g^{\mu\sigma}\partial_\lambda g_{\sigma\mu}$。
3. 用**雅可比公式**求行列式的导数：$\partial_\lambda\det g=\det g\cdot g^{\mu\sigma}\partial_\lambda g_{\sigma\mu}$（逆乘以导数之迹）。故 $g^{\mu\sigma}\partial_\lambda g_{\sigma\mu}=\dfrac{1}{g}\partial_\lambda g=\partial_\lambda\ln|g|$。
4. 因此 $\Gamma^\mu{}_{\mu\lambda}=\tfrac12\partial_\lambda\ln|g|=\partial_\lambda\ln\sqrt{|g|}=\partial_\lambda\ln\sqrt{-g}$（洛伦兹情形）。$\blacksquare$

#### 协变散度的简化

> **定理。** 对任意矢量场 $V^\mu$，
> $$
> \nabla_\mu V^\mu=\frac{1}{\sqrt{-g}}\,\partial_\mu\bigl(\sqrt{-g}\,V^\mu\bigr),
> $$
> 等价地 $\sqrt{-g}\,\nabla_\mu V^\mu=\partial_\mu(\sqrt{-g}\,V^\mu)$——克里斯托费尔符号从散度中消失了。

*证明。*
1. 展开定义：$\nabla_\mu V^\mu=\partial_\mu V^\mu+\Gamma^\mu{}_{\mu\lambda}V^\lambda$。
2. 代入引理 $\Gamma^\mu{}_{\mu\lambda}=\dfrac{1}{\sqrt{-g}}\partial_\lambda\sqrt{-g}$：$\nabla_\mu V^\mu=\partial_\mu V^\mu+\dfrac{1}{\sqrt{-g}}(\partial_\lambda\sqrt{-g})V^\lambda$。
3. 把右边识别为一次乘积法则展开。计算 $\dfrac{1}{\sqrt{-g}}\partial_\mu(\sqrt{-g}\,V^\mu)=\dfrac{1}{\sqrt{-g}}\bigl[(\partial_\mu\sqrt{-g})V^\mu+\sqrt{-g}\,\partial_\mu V^\mu\bigr]=\dfrac{(\partial_\mu\sqrt{-g})V^\mu}{\sqrt{-g}}+\partial_\mu V^\mu$。
4. 两个表达式逐项相符（在重新标记哑指标 $\lambda\to\mu$ 之后）。$\blacksquare$

这是本学科中使用最多的恒等式：它让你计算散度、写出守恒律，而无需求出任何一个克里斯托费尔符号。

#### 张量拉普拉斯算子（拉普拉斯–贝尔特拉米算子）

> **定义。** 标量 $f$ 的**拉普拉斯算子**为 $\Box f=\nabla_\mu\nabla^\mu f=g^{\mu\nu}\nabla_\mu\nabla_\nu f$。

> **定理。** $\Box f=\dfrac{1}{\sqrt{-g}}\partial_\mu\bigl(\sqrt{-g}\,g^{\mu\nu}\partial_\nu f\bigr)$。

*证明。*
1. 由于 $f$ 是标量，$\nabla_\nu f=\partial_\nu f$，故"梯度矢量"为 $V^\mu=g^{\mu\nu}\partial_\nu f$。
2. 拉普拉斯算子是该矢量的散度：$\Box f=\nabla_\mu V^\mu$。
3. 应用前一个框中的散度定理：$\Box f=\dfrac{1}{\sqrt{-g}}\partial_\mu(\sqrt{-g}\,V^\mu)=\dfrac{1}{\sqrt{-g}}\partial_\mu(\sqrt{-g}\,g^{\mu\nu}\partial_\nu f)$。$\blacksquare$

> **例 — 重现平直空间的拉普拉斯算子。** 在球坐标中，$\sqrt{g}=r^2\sin\theta$ 且 $g^{rr}=1$，径向部分为 $\dfrac{1}{r^2\sin\theta}\partial_r(r^2\sin\theta\cdot 1\cdot\partial_r f)=\dfrac{1}{r^2}\partial_r(r^2\partial_r f)$，即教科书上的径向拉普拉斯算子——由主公式一行推出，无需背任何矢量微积分恒等式。

## C 部分 · 形式、星算子与积分

<a id="s5"></a>
### 霍奇星算子与余微分

霍奇星算子把一个 $k$-形式变成它的互补 $(n-k)$-形式，是电磁学中对偶性背后的引擎，也是定义伴随导数的基础。

> **定义 — 霍奇星算子。** 在带度量的 $n$ 维流形上，**霍奇星算子** $\star$ 把分量为 $\alpha_{\mu_1\dots\mu_k}$ 的 $k$-形式 $\alpha$ 映为 $(n-k)$-形式
> $$
> (\star\alpha)_{\nu_1\dots\nu_{n-k}}=\frac{1}{k!}\,\varepsilon_{\nu_1\dots\nu_{n-k}}{}^{\mu_1\dots\mu_k}\,\alpha_{\mu_1\dots\mu_k},
> $$
> 其中 $\varepsilon$ 是列维-奇维塔**张量**（s2），上指标由 $g^{\mu\nu}$ 升起。

> **定理。** 在一个 $k$-形式上两次作用星算子给出 $\star\star\alpha=s\,(-1)^{k(n-k)}\alpha$，其中 $s=\mathrm{sgn}(g)$（洛伦兹号差时 $s=-1$，黎曼号差时 $s=+1$）。

*证明梗概及其关键步骤。*
1. 复合两次星算子会缩并两个列维-奇维塔张量。基本缩并恒等式为 $\varepsilon^{\mu_1\dots\mu_k\,\lambda_1\dots\lambda_{n-k}}\varepsilon_{\nu_1\dots\nu_k\,\lambda_1\dots\lambda_{n-k}}=s\,(n-k)!\,k!\,\delta^{[\mu_1}_{\nu_1}\cdots\delta^{\mu_k]}_{\nu_k}$，即广义反对称化克罗内克 delta。因子 $s$ 之所以出现，是因为把 $\varepsilon$ 的全部 $n$ 个指标升起会抽出 $\det(g^{\mu\nu})=1/g$，而 $\sqrt{-g}\cdot 1/\sqrt{-g}$ 留下 $g$ 的符号。
2. 符号 $(-1)^{k(n-k)}$ 数的是把 $n-k$ 个被缩并指标移到 $k$ 个自由指标之外、以便对齐 delta 所需的对换次数。
3. 把这些数值因子与两个星算子中的 $1/k!$ 归一化合在一起，便得 $s(-1)^{k(n-k)}$。$\blacksquare$

#### 余微分

> **定义 — 余微分。** **余微分** $\delta$ 是外微分 $d$ 的（形式）伴随。在 $n$ 维、洛伦兹符号为 $s$ 的 $k$-形式上，
> $$
> \delta=s\,(-1)^{n(k+1)+1}\,\star\,d\,\star.
> $$
> 它把形式次数降低一：$\delta:\Omega^k\to\Omega^{k-1}$。

> **定理。** 在一个 $1$-形式 $\omega$ 上，余微分是散度的相反数：$\delta\omega=-\nabla^\mu\omega_\mu$（黎曼号差；对洛伦兹号差整体差一个符号）。

*证明。*
1. $\star\omega$ 是一个 $(n-1)$-形式；$d\star\omega$ 是最高次 $n$-形式 $(\nabla^\mu\omega_\mu)\,\varepsilon$，因为对偶的外微分恰好产生协变散度（这是 s4 中散度恒等式的形式语言重述）。
2. 对该最高次形式作用最后的 $\star$，返回一个标量，即 $\nabla^\mu\omega_\mu$，至多差定义中的号差因子。
3. 取 $k=1$，把前因子 $s(-1)^{n(k+1)+1}$ 收拢便给出所述符号。$\blacksquare$

> **为何关心。** 算子 $\delta d+d\delta=\Box$ 是作用在形式上的**霍奇拉普拉斯算子**；$\delta$ 是"$\nabla_\mu F^{\mu\nu}$"在形式语言中的写法，我们将在 s7 看到它给出麦克斯韦两个方程之一。

<a id="s6"></a>
### 流形上的积分：体积形式与散度定理

在一个区域上对标量积分需要一个不变测度；密度 $\sqrt{-g}$ 提供了它。

> **定义 — 不变体积形式。** **体积形式**是最高次 $n$-形式
> $$
> \mathrm{vol}=\sqrt{-g}\;dx^1\wedge\cdots\wedge dx^n,
> $$
> 而标量场 $f$ 在区域 $\Omega$ 上的积分为 $\displaystyle\int_\Omega f\,\mathrm{vol}=\int_\Omega f\,\sqrt{-g}\,d^nx$。

> **定理（不变性）。** $\displaystyle\int_\Omega f\,\sqrt{-g}\,d^nx$ 与坐标无关。

*证明。*
1. 在 $x\to x'$ 下，坐标测度按雅可比绝对值变化：由多元微积分的换元定理，$d^nx=\bigl|\det\tfrac{\partial x}{\partial x'}\bigr|\,d^nx'=|\det J^{-1}|\,d^nx'$。
2. 密度按（s2）变换为 $\sqrt{-g}=\dfrac{1}{|\det J^{-1}|}\sqrt{-g'}$，因为 $\sqrt{-g'}=|\det J^{-1}|\sqrt{-g}$。
3. 标量不变，$f=f'$。把三个因子相乘：$f\sqrt{-g}\,d^nx=f'\cdot\dfrac{\sqrt{-g'}}{|\det J^{-1}|}\cdot|\det J^{-1}|\,d^nx'=f'\sqrt{-g'}\,d^nx'$。两个雅可比因子恰好相消。$\blacksquare$

> **定理（张量形式的散度定理）。** 对带边界 $\partial\Omega$ 的区域 $\Omega$ 上的矢量场 $V^\mu$，
> $$
> \int_\Omega \nabla_\mu V^\mu\,\sqrt{-g}\,d^nx=\oint_{\partial\Omega} V^\mu\,n_\mu\,\sqrt{|h|}\,d^{n-1}y,
> $$
> 其中 $n_\mu$ 是向外的单位法余矢量，$h$ 是诱导边界度量的行列式。

*证明。*
1. 由散度恒等式（s4），$\sqrt{-g}\,\nabla_\mu V^\mu=\partial_\mu(\sqrt{-g}\,V^\mu)$。故左边被积函数是矢量密度 $\sqrt{-g}\,V^\mu$ 的普通坐标散度。
2. 对密度 $\sqrt{-g}\,V^\mu$ 应用多元微积分的**普通**（平直）散度定理：$\int_\Omega\partial_\mu(\sqrt{-g}\,V^\mu)\,d^nx=\oint_{\partial\Omega}\sqrt{-g}\,V^\mu\,d\Sigma_\mu$，其中 $d\Sigma_\mu$ 是坐标面元。
3. 识别边界测度 $\sqrt{-g}\,d\Sigma_\mu=n_\mu\sqrt{|h|}\,d^{n-1}y$，即带其法向的不变面元，这是把体密度约化到 $\partial\Omega$ 上诱导度量的标准约化。代入即得结果。$\blacksquare$

> **例 — 高斯定律。** 取 $V^\mu$ 为平直三维空间中的电场矢量，这约化为 $\int(\nabla\cdot\mathbf E)\,dV=\oint\mathbf E\cdot d\mathbf A$——即熟悉的高斯定理，现在被看作"矢量的散度积分等于其边界通量"这一与度量无关的陈述。

## D 部分 · 张量形式的物理

<a id="s7"></a>
### 电磁场张量与麦克斯韦方程组

电磁学是整套机器最干净利落的演示：六个场分量装配成一个反对称张量，四个矢量方程坍缩为两个张量方程。

> **定义 — 场强张量。** 给定电磁四势 $A_\mu=(-\phi,\mathbf A)$（其中 $\phi$ 是标势，$\mathbf A$ 是矢势），定义反对称**场强**
> $$
> F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu.
> $$

> **定理。** $F_{\mu\nu}$ 是一个真正的反对称 $(0,2)$ 张量，且 $\partial_\mu A_\nu-\partial_\nu A_\mu=\nabla_\mu A_\nu-\nabla_\nu A_\mu$——偏导数可以免费地升级为协变导数。

*证明。*
1. 反对称性 $F_{\nu\mu}=-F_{\mu\nu}$ 由定义立即可见。
2. $\nabla_\mu A_\nu=\partial_\mu A_\nu-\Gamma^\sigma{}_{\mu\nu}A_\sigma$ 中的克里斯托费尔修正项关于 $\mu\nu$ **对称**，因为 $\Gamma^\sigma{}_{\mu\nu}=\Gamma^\sigma{}_{\nu\mu}$（联络无挠）。
3. 反对称化把它消去：$\nabla_\mu A_\nu-\nabla_\nu A_\mu=(\partial_\mu A_\nu-\partial_\nu A_\mu)-(\Gamma^\sigma{}_{\mu\nu}-\Gamma^\sigma{}_{\nu\mu})A_\sigma=\partial_\mu A_\nu-\partial_\nu A_\mu$。由于右边现在显然是一个张量（一个反对称化的协变导数），故 $F$ 也是张量。$\blacksquare$

#### 辨认分量

> 取 $\eta=\mathrm{diag}(-1,1,1,1)$ 且 $i,j\in\{1,2,3\}$：$F_{0i}=\partial_0 A_i-\partial_i A_0=-\partial_t A_i-\partial_i\phi$……对照 $\mathbf E=-\nabla\phi-\partial_t\mathbf A$ 与 $\mathbf B=\nabla\times\mathbf A$，得到 $F_{0i}=E_i$ 与 $F_{ij}=\epsilon_{ijk}B^k$。于是 $F_{\mu\nu}$ 把电场打包在其时-空分量中，把磁场打包在其空-空分量中。

#### 两个协变的麦克斯韦方程

> **定理（齐次方程——比安基/法拉第）。** $\partial_{[\lambda}F_{\mu\nu]}=0$，等价地 $\partial_\lambda F_{\mu\nu}+\partial_\mu F_{\nu\lambda}+\partial_\nu F_{\lambda\mu}=0$。

*证明。*
1. 把 $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$ 代入循环和：
$$
(\partial_\lambda\partial_\mu A_\nu-\partial_\lambda\partial_\nu A_\mu)+(\partial_\mu\partial_\nu A_\lambda-\partial_\mu\partial_\lambda A_\nu)+(\partial_\nu\partial_\lambda A_\mu-\partial_\nu\partial_\mu A_\lambda).
$$
2. 偏导数可交换，$\partial_\lambda\partial_\mu=\partial_\mu\partial_\lambda$（混合偏导相等，对光滑场成立）。六项成对相消：$\partial_\lambda\partial_\mu A_\nu$ 与 $-\partial_\mu\partial_\lambda A_\nu$ 相消，等等。
3. 协变版本完全相同，因为对称的克里斯托费尔项在反对称化中相消，恰如上一证明那样。该方程编码了 $\nabla\cdot\mathbf B=0$ 与法拉第定律 $\nabla\times\mathbf E=-\partial_t\mathbf B$。$\blacksquare$

> **定理（非齐次方程——高斯/安培）。** 取四流 $J^\mu=(\rho,\mathbf J)$ 及高斯制风格单位，
> $$
> \nabla_\mu F^{\mu\nu}=\mu_0 J^\nu,\qquad\text{equivalently}\qquad \frac{1}{\sqrt{-g}}\partial_\mu(\sqrt{-g}\,F^{\mu\nu})=\mu_0 J^\nu.
> $$

*简化形式的证明。*
1. $F^{\mu\nu}$ 反对称。其协变散度为 $\nabla_\mu F^{\mu\nu}=\partial_\mu F^{\mu\nu}+\Gamma^\mu{}_{\mu\lambda}F^{\lambda\nu}+\Gamma^\nu{}_{\mu\lambda}F^{\mu\lambda}$。
2. 末项为零：$\Gamma^\nu{}_{\mu\lambda}$ 关于 $\mu\lambda$ 对称，$F^{\mu\lambda}$ 反对称，对称乘反对称缩并为零（s1）。
3. 中间项用引理 $\Gamma^\mu{}_{\mu\lambda}=\frac{1}{\sqrt{-g}}\partial_\lambda\sqrt{-g}$，故由乘积法则 $\nabla_\mu F^{\mu\nu}=\partial_\mu F^{\mu\nu}+\frac{1}{\sqrt{-g}}(\partial_\lambda\sqrt{-g})F^{\lambda\nu}=\frac{1}{\sqrt{-g}}\partial_\mu(\sqrt{-g}\,F^{\mu\nu})$（与 s4 散度定理相同的代数，反对称的额外项已被丢弃）。
4. 令其等于 $\mu_0 J^\nu$ 即重现高斯定律（$\nu=0$）与安培–麦克斯韦定律（$\nu=i$）。$\blacksquare$

> **推论 — 电荷守恒自动成立。** 对非齐次方程取 $\nabla_\nu$：$\mu_0\nabla_\nu J^\nu=\nabla_\nu\nabla_\mu F^{\mu\nu}$。右边是对称的导数算子 $\nabla_\nu\nabla_\mu$ 与反对称的 $F^{\mu\nu}$ 缩并，故为零。（具体地，$\nabla_\nu\nabla_\mu F^{\mu\nu}=\tfrac12[\nabla_\nu,\nabla_\mu]F^{\mu\nu}$ 产生关于 $(\mu,\nu)$ 对称的里奇型曲率项，故它们与反对称的 $F^{\mu\nu}$ 缩并时同样为零。）于是 $\nabla_\mu J^\mu=0$：电荷自动守恒，这是 $F$ 反对称性的结构性后果。

<a id="s8"></a>
### 应力–能量张量与 $\nabla_\mu T^{\mu\nu}=0$

应力–能量张量既是引力的源，也是能量与动量流动的记账员。

> **定义。** 对称的 $(2,0)$ **应力–能量张量** $T^{\mu\nu}$ 有如下诠释：$T^{00}$ 是能量密度，$T^{0i}$ 是能量通量 / $i$-动量密度，$T^{ij}$ 是 $i$-动量在 $j$ 方向上的通量（应力）。对一个具有静能量密度 $\rho$、压强 $p$、四速 $u^\mu$（归一化 $u^\mu u_\mu=-1$）的**理想流体**，
> $$
> T^{\mu\nu}=(\rho+p)\,u^\mu u^\nu+p\,g^{\mu\nu}.
> $$

> **定理（局部守恒）。** 在无外力的情况下，$\nabla_\mu T^{\mu\nu}=0$。这是 $n$ 个方程，表达能量守恒（$\nu=0$）与动量守恒（$\nu=i$）。

*针对理想流体的推导，表明它给出相对论性欧拉方程。*
1. 计算 $\nabla_\mu T^{\mu\nu}=\nabla_\mu[(\rho+p)u^\mu u^\nu]+\nabla_\mu(p\,g^{\mu\nu})$。利用 $\nabla_\mu g^{\mu\nu}=0$（度量相容性），故末项为 $g^{\mu\nu}\nabla_\mu p=\nabla^\nu p$。
2. 对第一项用莱布尼茨法则：$u^\nu\nabla_\mu[(\rho+p)u^\mu]+(\rho+p)u^\mu\nabla_\mu u^\nu$。
3. 与 $u_\nu$ 缩并以沿流投影（用 $u_\nu u^\nu=-1$ 与 $u_\nu\nabla_\mu u^\nu=0$，后者由对归一化 $u^\nu u_\nu=-1$ 求导得到）：这给出**能量/连续性方程** $\nabla_\mu(\rho u^\mu)+p\,\nabla_\mu u^\mu=0$。
4. 用投影算子 $h^\alpha{}_\nu=\delta^\alpha_\nu+u^\alpha u_\nu$ 投影到与流正交的方向：这给出**欧拉方程** $(\rho+p)u^\mu\nabla_\mu u^\alpha=-h^{\alpha\mu}\nabla_\mu p$——（投影到与运动垂直方向上的）压强梯度使流体加速。$\blacksquare$

> **为何在广义相对论中守恒自动成立。** 爱因斯坦方程为 $G^{\mu\nu}=8\pi G\,T^{\mu\nu}$，其中 $G^{\mu\nu}=R^{\mu\nu}-\tfrac12 R g^{\mu\nu}$ 是爱因斯坦张量。**缩并比安基恒等式** $\nabla_\mu G^{\mu\nu}=0$ 作为一条几何恒等式成立（已在配套指南中证明），故场方程*强制* $\nabla_\mu T^{\mu\nu}=0$。能量–动量守恒不是一个额外假设；它内置于几何之中。

> **例 — 尘埃。** 对无压强物质（"尘埃"）$p=0$，守恒给出 $\nabla_\mu(\rho u^\mu)=0$（连续性）与 $u^\mu\nabla_\mu u^\nu=0$（测地线方程）。尘埃粒子沿测地线自由下落——引力仅凭几何就让物质运动。

<a id="s9"></a>
### 对称性：李导数、基灵矢量与守恒量

度量的连续对称性沿测地线产生守恒量——这是诺特定理的几何面貌。

> **定义 — 分量形式的李导数。** 张量沿矢量场 $\xi$ 的**李导数**度量它在沿 $\xi$ 的流被拖动时的变化。在一个矢量和一个 $(0,2)$ 张量上，
> $$
> (\mathcal L_\xi V)^\mu=\xi^\nu\partial_\nu V^\mu-V^\nu\partial_\nu\xi^\mu,\qquad
> (\mathcal L_\xi T)_{\mu\nu}=\xi^\lambda\partial_\lambda T_{\mu\nu}+T_{\lambda\nu}\partial_\mu\xi^\lambda+T_{\mu\lambda}\partial_\nu\xi^\lambda.
> $$

> **定理。** 李导数可用协变导数代替偏导数来写：$(\mathcal L_\xi T)_{\mu\nu}=\xi^\lambda\nabla_\lambda T_{\mu\nu}+T_{\lambda\nu}\nabla_\mu\xi^\lambda+T_{\mu\lambda}\nabla_\nu\xi^\lambda$。

*证明。* 把每个 $\partial$ 换成 $\nabla$；这会引入克里斯托费尔项。把它们归拢：来自输运项 $\xi^\lambda\nabla_\lambda T_{\mu\nu}$ 的 $\Gamma$ 与来自 $T_{\lambda\nu}\nabla_\mu\xi^\lambda$ 和 $T_{\mu\lambda}\nabla_\nu\xi^\lambda$ 的 $\Gamma$ 两两配对，由于联络无挠（$\Gamma^\lambda{}_{\mu\nu}=\Gamma^\lambda{}_{\nu\mu}$），每一对都带有相等而相反的系数，故所有克里斯托费尔项相消。因此李导数与联络无关。$\blacksquare$

> **定义 — 基灵矢量。** 矢量场 $\xi$ 是**基灵矢量**，如果沿它拖动度量什么也不改变：$\mathcal L_\xi g_{\mu\nu}=0$。用协变形式并代入 $\nabla_\lambda g_{\mu\nu}=0$，这就是**基灵方程**：
> $$
> \nabla_\mu\xi_\nu+\nabla_\nu\xi_\mu=0,\qquad\text{i.e.}\qquad \nabla_{(\mu}\xi_{\nu)}=0.
> $$

> **定理（守恒动量）。** 若 $\xi$ 是基灵矢量，且 $x^\mu(\lambda)$ 是切矢为 $u^\mu$ 的测地线，则 $\xi_\mu u^\mu$ 沿测地线为常数。

*证明。*
1. $\dfrac{d}{d\lambda}(\xi_\mu u^\mu)=u^\nu\nabla_\nu(\xi_\mu u^\mu)$，因为该标量沿曲线的变化率就是方向协变导数。
2. 莱布尼茨：$=u^\nu u^\mu\nabla_\nu\xi_\mu+\xi_\mu(u^\nu\nabla_\nu u^\mu)$。
3. 第二项由**测地线方程** $u^\nu\nabla_\nu u^\mu=0$ 为零。
4. 第一项把**对称的** $u^\nu u^\mu$ 与 $\nabla_\nu\xi_\mu$ 缩并；只有对称部分 $\nabla_{(\nu}\xi_{\mu)}$ 存留，而它由**基灵方程**为零。$\blacksquare$

> **定义 — 基灵张量。** 对称张量 $K_{\mu\nu}$ 是**基灵张量**，如果 $\nabla_{(\lambda}K_{\mu\nu)}=0$。则 $K_{\mu\nu}u^\mu u^\nu$ 沿测地线守恒，论证相同：$u^\mu u^\nu$ 对称，而对称化的导数为零。

> **例 — 克尔的隐藏常数。** 在旋转黑洞（克尔）时空中，显然的基灵矢量 $\partial_t$ 与 $\partial_\phi$ 给出守恒的能量与角动量。但克尔时空还容许一个非平凡的**基灵张量**，其守恒量是**卡特常数**——这个额外的运动积分使克尔时空中的测地线完全可解。基灵张量产生的守恒律没有与之相伴的度量时空对称性，这是初等诺特推理所看不见的现象。

<a id="s10"></a>
### 旋量与四标架形式 — 克利福德代数与狄拉克算子

旋量是构成电子的对象，而它们无法用世界指标书写。下面是建立在 s3 的四标架之上的具体机制。

> **定义 — 克利福德 / 伽马代数。** 平直空间的**伽马矩阵** $\gamma^a$（$a$ 为标架指标）满足**克利福德关系**
> $$
> \{\gamma^a,\gamma^b\}=\gamma^a\gamma^b+\gamma^b\gamma^a=2\,\eta^{ab}\,\mathbb 1,
> $$
> 其中 $\eta^{ab}$ 是常值标架度量。在 4 维中它们是常值的 $4\times4$ 矩阵；编码几何的是反对易子，而非乘积。

要点在于其平方根结构：$(\gamma^a\partial_a)^2$ 重现拉普拉斯/达朗贝尔算子。验证如下：利用克利福德关系与 $\partial_a\partial_b$ 的对称性把 $\gamma^a\gamma^b$ 换成其对称部分，$(\gamma^a\partial_a)(\gamma^b\partial_b)=\tfrac12\{\gamma^a,\gamma^b\}\partial_a\partial_b=\eta^{ab}\partial_a\partial_b=\Box$。于是狄拉克算子是波动算子的一个*平方根*。

#### 使伽马矩阵弯曲

> **定义 — 弯曲伽马矩阵。** 用逆四标架把标架指标转换为世界指标：$\gamma^\mu(x)=e_a{}^\mu(x)\,\gamma^a$。则 $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$。

*证明。* $\{\gamma^\mu,\gamma^\nu\}=e_a{}^\mu e_b{}^\nu\{\gamma^a,\gamma^b\}=e_a{}^\mu e_b{}^\nu\,2\eta^{ab}=2g^{\mu\nu}$，其中最后一步是度量关系 $g^{\mu\nu}=e_a{}^\mu e_b{}^\nu\eta^{ab}$（s3）的逆维尔拜因形式。$\blacksquare$

#### 自旋联络与狄拉克算子

旋量 $\psi$ 携带一个隐藏的标架结构，故对它求导需要一个作用于标架指标的联络——**自旋联络** $\omega_\mu{}^{ab}$，即克里斯托费尔符号在洛伦兹标架中的类比物。

> **定义 — 旋量协变导数。**
> $$
> D_\mu\psi=\partial_\mu\psi+\tfrac14\,\omega_\mu{}^{ab}\,\gamma_a\gamma_b\,\psi,
> $$
> 其中自旋联络由要求四标架协变常值（"四标架假设"）$\nabla_\mu e^a{}_\nu+\omega_\mu{}^a{}_b e^b{}_\nu=0$ 所确定，其解为
> $$
> \omega_\mu{}^{ab}=e^a{}_\nu\bigl(\partial_\mu e^{b\nu}+\Gamma^\nu{}_{\mu\lambda}e^{b\lambda}\bigr).
> $$

> **定义 — 弯曲空间上的狄拉克算子。** 弯曲空间的**狄拉克算子**为
> $$
> \slashed D=\gamma^\mu D_\mu=e_a{}^\mu\gamma^a\bigl(\partial_\mu+\tfrac14\omega_\mu{}^{bc}\gamma_b\gamma_c\bigr),
> $$
> 质量为 $m$ 的粒子的**狄拉克方程**为 $(i\slashed D-m)\psi=0$。

> **为何每一块都必不可少。** 单独的 $\partial_\mu$ 在旋量上不是洛伦兹协变的；$\tfrac14\omega_\mu{}^{ab}\gamma_a\gamma_b$ 项旋转旋量标架以作补偿，恰如 $\Gamma$ 为移动张量标架作补偿。四标架 $e_a{}^\mu$ 是唯一能把带标架指标的伽马矩阵接到带世界指标的导数上的对象。没有四标架，弯曲空间上就没有狄拉克方程——这正是为什么 s3 的标架形式对张量是可选的，对费米子却是必需的。

> **例 — 平直空间的合理性检验。** 在闵可夫斯基坐标中，四标架是平凡的，$e_a{}^\mu=\delta_a^\mu$，故 $\omega_\mu{}^{ab}=0$ 且 $\slashed D=\gamma^\mu\partial_\mu$。狄拉克方程约化为熟悉的 $(i\gamma^\mu\partial_\mu-m)\psi=0$，对它平方给出 $(\Box+m^2)\psi=0$，即克莱因–戈尔登方程——确认狄拉克算子是波动算子的旋量平方根，现在是在任意弯曲背景上。

---

*本指南把张量微积分当作一门手艺来处理：我们学会了哪些数组是张量（商定理）、哪些是密度以及 $\sqrt{-g}$ 如何把它们改造好、如何升降指标与作协变微分，以及单一恒等式 $\nabla_\mu(\sqrt{-g}\,V^\mu)=\partial_\mu(\sqrt{-g}\,V^\mu)$ 如何驯服散度、拉普拉斯算子乃至麦克斯韦方程组。从那里出发，物理几乎机械地涌现出来——电磁场张量、能量–动量守恒、基灵对称性及其守恒荷，以及四标架承载的狄拉克算子。请把它当作案头参考：当某个指标计算卡住时，解决办法几乎总是去问，被遵守的究竟是哪一份契约——张量、密度还是标架——然后插入恢复它所需的 $\sqrt{-g}$ 或维尔拜因。*
