[English](algebraic-topology.md) · **中文**

# 拓扑学，*化为代数。*

一门完整的代数拓扑入门课程——如何把群、环与正合列附加到空间上，使得连续映射变成同态、"形状"变得可计算。每个核心定理都被**演示**，并将贯穿其中、把它们全部捆在一起的函子性脉络明确点出。

[← 返回全部指南](../README.zh.md)

## 第 A 部分 · 同伦与基本群

<a id="s0"></a>
### 宏观图景：把空间变成代数

拓扑学研究空间中那些在连续形变下保持的性质——在*同胚*下不变的性质。但要直接证明两个空间*不*同胚是困难的：你得排除每一种可能的映射。代数拓扑提供了一条出路。

- **附加** 一个代数对象（一个群、一个环、一列群）到每个空间上。
- **函子性** —— 每个连续映射诱导一个同态，且尊重复合与恒等。
- **不变性** —— 同胚的（实际上是同伦等价的）空间得到同构的代数，故不同的代数证明不同的空间。

> **原理 — 中心策略**
>
> 一个**不变量**是从空间与连续映射到群与同态的函子 $F$。由于 $F(f\circ g)=F(f)\circ F(g)$ 且 $F(\mathrm{id})=\mathrm{id}$，同胚 $X\cong Y$ 迫使同构 $F(X)\cong F(Y)$。逆否命题：若 $F(X)\not\cong F(Y)$，则 $X$ 与 $Y$ *不*同胚。我们用一个棘手的拓扑问题换取一个可处理的代数问题。

> **联系 — 为何"函子"是承重的词**
>
> 每一章都是一个函子：$\pi_1$（一个群）、$\pi_n$（阿贝尔群）、$H_n$（同调，阿贝尔群）、$H^n$（上同调，一个分次环）。证明各不相同；逻辑——诱导映射、不变性、计算——却始终如一。

#### 整门课程浓缩成一行

> 同伦 → $\pi_1$ → $\pi_1(S^1)\cong\mathbb{Z}$ → van Kampen → 覆叠空间 → 同调 → 上同调与对偶

<a id="s1"></a>
### 映射的同伦与同伦等价

*把"相等"放松为"可连续形变"是使一切变得可计算的关键一步。多数不变量只看见同伦型，而非同胚型。*

> **定义 — 同伦**
>
> 两个连续映射 $f,g:X\to Y$ 称为**同伦**，记作 $f\simeq g$，若存在连续的 $H:X\times[0,1]\to Y$ 满足 $H(x,0)=f(x)$ 与 $H(x,1)=g(x)$。把 $H$ 想成一部影片：在每个时刻 $t$，$H(-,t)$ 是一个映射，从 $f$ 连续地滑向 $g$。对道路我们通常要求**端点固定**（相对于 $\{0,1\}$ 的同伦）。

**演示 — 同伦是一个等价关系**

1. 自反：$f\simeq f$，通过常值同伦 $H(x,t)=f(x)$，它作为连续映射的复合而连续。
2. 对称：若 $H$ 是同伦 $f\simeq g$，则 $\overline H(x,t)=H(x,1-t)$ 连续（与 $t\mapsto 1-t$ 复合）且给出 $g\simeq f$。
3. 传递：给定 $H:f\simeq g$ 与 $K:g\simeq h$，把它们拼接：在 $t=\tfrac12$ 两片都等于 $g(x)$，故由粘贴引理（在两个相交处一致的闭集上连续）$L$ 连续。

   $$L(x,t)=\begin{cases} H(x,2t), & 0\le t\le \tfrac12,\$$2pt] K(x,2t-1), & \tfrac12\le t\le 1.\end{cases}$$

*等价类 $[f]$ 是良定义的；这是每个同伦不变量的原材料。*

> **定义 — 同伦等价与可缩性**
>
> 映射 $f:X\to Y$ 称为**同伦等价**，若存在 $g:Y\to X$ 使 $g\circ f\simeq \mathrm{id}_X$ 且 $f\circ g\simeq \mathrm{id}_Y$；此时 $X\simeq Y$ 称为**同伦等价**。与一点同伦等价的空间称为**可缩**。$X$ 到子空间 $A$ 的一个**形变收缩**是从 $\mathrm{id}_X$ 到一个固定 $A$ 的收缩 $r:X\to A$ 的同伦；它把 $A\hookrightarrow X$ 展现为同伦等价。

**牢记于心的例子**

*$\mathbb{R}^n$ 可缩（把一切滑向原点：$H(x,t)=(1-t)x$）。挖去一点的平面 $\mathbb{R}^2\setminus\{0\}$ 经由 $H(x,t)=(1-t)x+t\,x/|x|$ 形变收缩到 $S^1$。圆环、Möbius 带与 $S^1$ 全都同伦等价，尽管两两不同胚——同伦确实更粗糙。*

> **联系 — 通向一般拓扑**
>
> 同胚 $\Rightarrow$ 同伦等价，反之绝不成立。代数拓扑不变量被设计成*同伦*不变量，所以它们自动是拓扑不变量——但按其构造方式，它们无法区分圆盘与一点。

<a id="s2"></a>
### 基本群 $\pi_1$

*第一个也是最直观的函子：基点处的环路，至多差一个同伦，以连接为运算。它探测一维的洞。*

> **定义 — 环路、连接、群**
>
> 固定 $x_0\in X$。$x_0$ 处的一条**环路**是道路 $\gamma:[0,1]\to X$ 满足 $\gamma(0)=\gamma(1)=x_0$。**基本群** $\pi_1(X,x_0)$ 是环路的同伦类（相对端点）的集合，其乘积为 $[\,\alpha\,][\,\beta\,]=[\alpha\cdot\beta]$，其中 $$ (\alpha\cdot\beta)(s)=\begin{cases}\alpha(2s),&0\le s\le\tfrac12,\\ \beta(2s-1),&\tfrac12\le s\le1.\end{cases} $$

**演示 — $\pi_1(X,x_0)$ 是一个群**

1. 良定义：若 $\alpha\simeq\alpha'$ 且 $\beta\simeq\beta'$ 相对端点，则并排同伦 $H\cdot K$ 表明 $\alpha\cdot\beta\simeq\alpha'\cdot\beta'$。故类上的乘积无歧义。
2. 结合律：$(\alpha\cdot\beta)\cdot\gamma$ 与 $\alpha\cdot(\beta\cdot\gamma)$ 仅在三个环路被遍历的速度上不同。一个重新参数化 $\varphi:[0,1]\to[0,1]$（时间轴的同伦）把一个变为另一个，故两类相等。
3. 恒等元：常值环路 $c_{x_0}$ 满足 $[c]\,[\alpha]=[\alpha]=[\alpha]\,[c]$：环路"先等待再走"被重新参数化为"走"，同样由 $[0,1]$ 的一个同伦实现。
4. 逆元：令 $\bar\alpha(s)=\alpha(1-s)$。把往返 $\alpha\cdot\bar\alpha$ 拉回 $x_0$ 的同伦 $H(s,t)=\alpha\big(\text{shrink}\big)$ 表明 $[\alpha][\bar\alpha]=[c]$。

*四条公理都在端点固定的同伦意义下成立——这正是我们对它取商的原因。*

**演示 — 道路连通空间上基点无关**

1. 设 $h:[0,1]\to X$ 是从 $x_0$ 到 $x_1$ 的道路。定义换基点映射

   $$\beta_h:\pi_1(X,x_1)\to\pi_1(X,x_0),\qquad \beta_h[\gamma]=[\,h\cdot\gamma\cdot\bar h\,].$$
2. 它是同态：$\beta_h[\gamma\cdot\delta]=[h\cdot\gamma\cdot\delta\cdot\bar h]=[h\cdot\gamma\cdot\bar h]\,[h\cdot\delta\cdot\bar h]$，插入 $\bar h\cdot h\simeq c$。
3. 它可逆，逆为 $\beta_{\bar h}$，因为 $\beta_h\beta_{\bar h}=\beta_{h\cdot\bar h}=\beta_c=\mathrm{id}$。

*故 $\pi_1(X,x_0)\cong\pi_1(X,x_1)$：在道路连通空间上我们可在同构意义下写 $\pi_1(X)$。（该同构只在内自同构意义下是典范的。）*

**函子性与诱导同态**

$$f:X\to Y,\ f(x_0)=y_0 \ \Longrightarrow\ f_*:\pi_1(X,x_0)\to\pi_1(Y,y_0),\quad f_*[\gamma]=[f\circ\gamma]$$

$$(g\circ f)_*=g_*\circ f_*,\qquad (\mathrm{id}_X)_*=\mathrm{id},\qquad f\simeq g\ (\text{rel }x_0)\Rightarrow f_*=g_*$$

*这三行使 $\pi_1$ 成为函子并证明同伦不变性：$X\simeq Y$ 给出 $\pi_1(X)\cong\pi_1(Y)$。*

> **定义 — 单连通**
>
> $X$ 称为**单连通**，若它道路连通且 $\pi_1(X)=0$（每条环路都可收缩）。例子：$\mathbb{R}^n$、任何凸集，以及 $n\ge 2$ 的 $S^n$。

> **联系 — 通向群论**
>
> $\pi_1$ 一般是*非阿贝尔*的（例如曲面、圆周的楔），所以自由群、表现 $\langle\text{gens}\mid\text{rels}\rangle$ 与正规子群的整套机器都登场了。这是通向组合群论的桥梁。

<a id="s3"></a>
### 圆周：$\pi_1(S^1)\cong\mathbb{Z}$ 与卷绕数

*奠基性的计算。一旦掌握了 $\pi_1(S^1)\cong\mathbb{Z}$，那些伟大的应用几乎不费吹灰之力便随之而出。*

**定理**

$$\pi_1(S^1,\,1)\ \cong\ \mathbb{Z},\qquad [\gamma]\ \longmapsto\ \deg(\gamma)=\text{winding number}.$$

*生成元是环路 $\omega(s)=e^{2\pi i s}$；那个整数是一条环路净缠绕的次数。*

> **概念 — 指数覆叠**
>
> 关键工具是 $p:\mathbb{R}\to S^1,\ p(t)=e^{2\pi i t}$。它把直线缠绕在圆周上，每个点有一个离散纤维 $p^{-1}(1)=\mathbb{Z}$。$\mathbb{R}$ 可缩，故下方的环路在上方变成货真价实的位移——一个数。

**演示 — 覆叠空间证明**

1. 道路提升。每条道路 $\gamma:[0,1]\to S^1$（$\gamma(0)=1$）都有唯一的提升 $\tilde\gamma:[0,1]\to\mathbb{R}$，满足 $\tilde\gamma(0)=0$ 且 $p\circ\tilde\gamma=\gamma$。（用均匀覆叠的弧覆盖 $S^1$；用 $p$ 的局部逆分段提升；唯一性是因为两个提升相差一个局部常值——因而常值——的整数。）
2. 同伦提升。道路的同伦 $\gamma_t$ 提升为同伦 $\tilde\gamma_t$，$\tilde\gamma_t(0)=0$；由唯一性，端点 $\tilde\gamma_t(1)$ 在离散集 $\mathbb{Z}$ 中连续变化，故为常值。
3. 度数映射。定义 $\Phi[\gamma]=\tilde\gamma(1)\in\mathbb{Z}$。第 2 步表明它只依赖于同伦类；它良定义。
4. 同态。要从 $0$ 出发提升 $\alpha\cdot\beta$：把 $\alpha$ 提升为终于 $m$ 的 $\tilde\alpha$，再把 $\beta$ 从 $m$ 出发提升——该提升是 $m+\tilde\beta$，终于 $m+n$。故 $\Phi[\alpha\cdot\beta]=m+n=\Phi[\alpha]+\Phi[\beta]$。
5. 满射：$\omega_n(s)=e^{2\pi i n s}$ 提升为 $t\mapsto nt$，故 $\Phi[\omega_n]=n$。
6. 单射：若 $\Phi[\gamma]=0$ 则 $\tilde\gamma$ 是可缩空间 $\mathbb{R}$ 中的环路，故 $\tilde\gamma\simeq 0$ 相对端点；由 $p$ 推下去给出 $\gamma\simeq c$。故 $[\gamma]=1$。

*$\Phi$ 是双射同态，故 $\pi_1(S^1)\cong\mathbb{Z}$。$\;\blacksquare$*

> **联系 — 卷绕数 = 一个围道积分**
>
> 对 $\mathbb{C}\setminus\{0\}$ 中的环路，同一个整数是 $\dfrac{1}{2\pi i}\displaystyle\oint \dfrac{dz}{z}$。拓扑度数与复分析卷绕数实实在在是同一个不变量——代数拓扑与复分析之间的接缝。

<a id="s4"></a>
### Seifert–van Kampen 定理

*一个"分而治之"的定理：它由各片的 $\pi_1$ 及其交叠来计算并集的 $\pi_1$——正是把几何变成群表现的工具。*

**定理（Seifert–van Kampen）**

$$\pi_1(X)\ \cong\ \pi_1(U)\ *_{\pi_1(U\cap V)}\ \pi_1(V),$$

*即自由积 $\pi_1(U)*\pi_1(V)$ 对关系 $i_*(w)=j_*(w)$（对每个 $w\in\pi_1(U\cap V)$）取模，其中 $i,j$ 是两个包含映射。*

**演示 — $n$ 个圆周之楔的 $\pi_1$ 是自由的**

1. 取 $X=S^1\vee\cdots\vee S^1$（$n$ 个圆周粘在一点）。把每个圆周加厚为开集 $U_k\simeq S^1$，使任何交叠 $U_j\cap U_k$ 形变收缩到楔点，因而可缩：$\pi_1(U_j\cap U_k)=0$。
2. 由于合并群平凡，推出就是单纯的自由积。迭代 van Kampen，得到 $n$ 个生成元上的自由群，每个圆周一个生成元。

   $$\pi_1\Big(\bigvee_{k=1}^n S^1\Big)\cong\underbrace{\mathbb{Z}*\cdots*\mathbb{Z}}_{n}=F_n,$$

*对 $n\ge 2$ 这是非阿贝尔的：$ab\ne ba$，反映出两个环路无法彼此滑过。*

**演示 — 可定向亏格 $g$ 曲面的 $\pi_1$**

1. 把 $\Sigma_g$ 构造为一个 $4g$ 边形，其边按词 $a_1b_1a_1^{-1}b_1^{-1}\cdots a_gb_ga_g^{-1}b_g^{-1}$ 粘合。令 $U$ 为开多边形（一个圆盘，可缩），$V$ 为其边界 1-骨架的邻域（$2g$ 个圆周之楔），$U\cap V$ 是圆环 $\simeq S^1$。
2. $\pi_1(U)=1$，$\pi_1(V)=F_{2g}=\langle a_1,b_1,\dots,a_g,b_g\rangle$。$\pi_1(U\cap V)$ 的生成元在 $V$ 中映到边界词，在 $U$ 中映到 $1$。
3. 因此推出施加一条关系——边界词等于 $1$：

   $$\pi_1(\Sigma_g)=\big\langle\, a_1,b_1,\dots,a_g,b_g \ \big|\ \textstyle\prod_{i=1}^g [a_i,b_i]=1 \,\big\rangle.$$

*对环面（$g=1$）这是 $\langle a,b\mid aba^{-1}b^{-1}=1\rangle\cong\mathbb{Z}^2$。阿贝尔化给出 $\mathbb{Z}^{2g}$，恢复出 $H_1$。*

> **联系 — 推出与表现**
>
> van Kampen 表明 $\pi_1$ 把空间的粘合（拓扑中的推出）送到合并自由积（群中的推出）。于是每个 CW 复形都产生其 $\pi_1$ 的一个*表现*：生成元来自 1-胞腔，关系来自 2-胞腔。

<a id="s5"></a>
### 应用：Brouwer（二维）、代数基本定理、无收缩

*单单一个计算 $\pi_1(S^1)\cong\mathbb{Z}$ 现在就能干真活。每个证明都是同一招：一个假想的映射会诱导一个不可能的同态。*

**演示 — 不存在收缩 $r:D^2\to S^1$**

1. 设存在收缩：$r:D^2\to S^1$ 连续，$r\circ\iota=\mathrm{id}_{S^1}$，其中 $\iota:S^1\hookrightarrow D^2$ 是边界的包含映射。
2. 应用函子 $\pi_1$：

   $$r_*\circ \iota_*=(\,r\circ\iota\,)_*=(\mathrm{id}_{S^1})_*=\mathrm{id}_{\mathbb{Z}}.$$
3. 但 $\iota_*:\pi_1(S^1)\to\pi_1(D^2)$ 是 $\mathbb{Z}\to 0$（圆盘可缩），故 $r_*\circ\iota_*$ 通过平凡群分解，必为零映射——它不可能是 $\mathrm{id}_{\mathbb{Z}}$。

*矛盾：不存在这样的收缩。$\;\blacksquare$*

**演示 — 二维 Brouwer 不动点定理**

1. 设 $f:D^2\to D^2$ 连续且无不动点，故对一切 $x$ 有 $f(x)\ne x$。
2. 定义 $r(x)$ = 从 $f(x)$ 经过 $x$ 的射线与 $S^1$ 的交点。由于 $f(x)\ne x$，该射线良定义且 $r$ 连续。
3. 若 $x\in S^1$，射线已在边界 $x$ 处起始，故 $r(x)=x$：于是 $r$ 是收缩 $D^2\to S^1$——由前一演示，不可能。

*故圆盘的每个连续自映射都有不动点。$\;\blacksquare$*

**演示 — 代数基本定理**

1. 设 $p(z)=z^n+a_{n-1}z^{n-1}+\cdots+a_0$，$n\ge 1$，并设 $p$ 在 $\mathbb{C}$ 中无根。
2. 对每个半径 $R\ge0$，环路 $\gamma_R(s)=\dfrac{p(Re^{2\pi i s})/p(R)}{|p(Re^{2\pi i s})/p(R)|}$ 落在 $S^1$ 中。当 $R$ 变化时它们全都同伦（无根意味着分母从不为零），故卷绕数 $\deg(\gamma_R)$ 关于 $R$ 为常值；在 $R=0$ 处它是 $0$。
3. 对很大的 $R$，$z^n$ 占主导，故 $p(Re^{2\pi i s})$ 像 $(Re^{2\pi i s})^n$ 一样缠绕：$\deg(\gamma_R)=n$。
4. 常值性迫使 $n=0$，与 $n\ge1$ 矛盾。

*故 $p$ 必有根：$\mathbb{C}$ 代数闭——用卷绕数证明。$\;\blacksquare$*

> **联系 — 一个模板，多个定理**
>
> 每个证明都从一个假想映射造出一个不可能的同态，借助 $\pi_1(S^1)\cong\mathbb{Z}\ne 0$。所有维数的 Brouwer、Borsuk–Ulam 定理与毛球定理都用更高的不变量（$H_n$、度数）遵循同一模式。

## 第 B 部分 · 覆叠空间

<a id="s6"></a>
### 覆叠空间与提升定理

*覆叠空间是 $\pi_1$ 子群的几何化身。提升是已经驱动了圆周计算的引擎。*

> **定义 — 覆叠空间**
>
> 连续满射 $p:\tilde X\to X$ 称为**覆叠映射**，若每个 $x\in X$ 都有一个*被均匀覆叠*的开邻域 $U$：$p^{-1}(U)=\bigsqcup_\alpha V_\alpha$，是诸开集的无交并，每个被 $p$ 同胚地映到 $U$。纤维 $p^{-1}(x)$ 是离散的；它们共同的基数是**叶**数。例子：$\mathbb{R}\to S^1$（无穷多叶）、$S^1\xrightarrow{z\mapsto z^n}S^1$（$n$ 叶）、$S^n\to\mathbb{RP}^n$（2 叶）。

**提升定理**

$$f_*\big(\pi_1(Y,y_0)\big)\ \subseteq\ p_*\big(\pi_1(\tilde X,\tilde x_0)\big),$$

*且当它存在时，它是唯一的。*

**演示 — $p_*$ 是单射；叶数计数指数**

1. $p_*$ 的单射性。若 $\tilde\gamma$ 是 $\tilde X$ 中的环路且 $p\circ\tilde\gamma\simeq c$ 在 $X$ 中，则用同伦提升性质把那个零伦提升上去；唯一性使该提升成为 $\tilde\gamma$ 的零伦。故 $\ker p_*=1$ 且 $p_*\pi_1(\tilde X)\hookrightarrow\pi_1(X)$ 是子群。
2. 纤维 = 陪集。对连通的 $\tilde X$，把环路类 $[\gamma]\in\pi_1(X,x_0)$ 送到它从 $\tilde x_0$ 出发的提升的端点。这给出与该子群右陪集的一个双射。

   $$p^{-1}(x_0)\ \longleftrightarrow\ p_*\pi_1(\tilde X,\tilde x_0)\ \backslash\ \pi_1(X,x_0),$$

*叶数 $=$ 指数 $[\pi_1(X):p_*\pi_1(\tilde X)]$。覆叠是显形的子群。*

> **联系 — 局部到整体**
>
> "被均匀覆叠"是纯局部条件，却迫使整体的提升性质。这种局部到整体的过渡与层论以及 van Kampen 中的粘合是同一精神。

<a id="s7"></a>
### Galois 对应：覆叠的分类与覆叠变换

*一个良好空间 $X$ 的覆叠空间由 $\pi_1(X)$ 的子群分类——这部词典与 Galois 理论中域扩张与子群之间的对应在形式上完全一致。*

**定理（覆叠的 Galois 对应）**

$$\left\{\begin{array}{c}\text{connected covers}\\ p:(\tilde X,\tilde x_0)\to(X,x_0)\end{array}\right\}\ \longleftrightarrow\ \left\{\begin{array}{c}\text{subgroups}\\ H\le\pi_1(X,x_0)\end{array}\right\},\qquad p\mapsto p_*\pi_1(\tilde X,\tilde x_0).$$

*忘掉基点后，覆叠的同构类 $\leftrightarrow$ 子群的共轭类。更小的子群 $=$ 更大的覆叠；平凡子群 $=$ 万有覆叠。*

> **定义 — 覆叠变换与正规性**
>
> $p:\tilde X\to X$ 的一个**覆叠变换**是满足 $p\circ\varphi=p$ 的同胚 $\varphi:\tilde X\to\tilde X$；它们构成群 $\mathrm{Deck}(\tilde X/X)$。覆叠称为**正规（正则/Galois）**，当 $H=p_*\pi_1(\tilde X)$ 是正规子群时——等价地，当覆叠变换在每个纤维上传递地作用时。

**演示 — $\mathrm{Deck}\cong N(H)/H$**

1. 一个覆叠变换是 $p$ 沿 $p$ 的自提升；由提升判据，这样的提升对应于把 $H$ 共轭到自身的 $\pi_1(X)$ 元素，即对应于正规化子 $N(H)$。
2. 两个这样的元素给出同一个覆叠变换当且仅当它们相差一个 $H$ 中的元素（它提升为一个环路，即恒等覆叠映射）。故

   $$\mathrm{Deck}(\tilde X/X)\ \cong\ N(H)/H.$$
3. 对正规覆叠 $N(H)=\pi_1(X)$，故 $\mathrm{Deck}\cong\pi_1(X)/H$。对万有覆叠 $H=1$ 且 $\mathrm{Deck}\cong\pi_1(X)$。

*覆叠群扮演 Galois 群的角色；$\pi_1(X)/H$ 是它"在基上的 Galois 群"。*

> **联系 — 通向域论**
>
> 把"覆叠"换成"域扩张"，"$\pi_1$ 的子群"换成"$\mathrm{Gal}$ 的子群"，"覆叠群"换成"Galois 群"，"万有覆叠"换成"可分闭包"。两者都是同一范畴模式的实例：一个基本群在作用，子群标号中间对象。

<a id="s8"></a>
### 万有覆叠

*最大的连通覆叠：单连通，坐落在所有其他覆叠之上。它是 $\pi_1$ 作为一群对称而显形之处。*

**定理 — 存在性与泛性质**

$$X\ \cong\ \tilde X/\pi_1(X),\qquad \mathrm{Deck}(\tilde X/X)\cong\pi_1(X).$$

*若 $X$ 道路连通、局部道路连通且半局部单连通，则它有一个**万有覆叠** $\tilde X$，满足 $\pi_1(\tilde X)=1$。它是万有的：对任何连通覆叠 $Y\to X$ 都有覆叠映射 $\tilde X\to Y$。它在同构意义下唯一，且*

**演示 — 用道路同伦类构造**

1. 固定 $x_0$。令 $\tilde X=\{\,[\gamma]: \gamma \text{ 是从 } x_0 \text{ 出发的道路，相对端点取类}\,\}$，并令 $p[\gamma]=\gamma(1)$。
2. 用由一个均匀覆叠邻域及进入它的一个道路类标号的基本集来给 $\tilde X$ 赋予拓扑；半局部单连通性使其自洽（小环路在 $X$ 中零伦）。
3. $\tilde X$ 道路连通（用连接在各类之间滑动）且单连通：上方的一条环路是下方 $\gamma$ 的一个同伦，故它的类为常值——它是平凡环路。
4. $\pi_1(X)$ 通过 $[\alpha]\cdot[\gamma]=[\alpha\cdot\gamma]$ 作用于 $\tilde X$，作用自由且真正不连续，商为 $X$。这把 $\pi_1(X)$ 实现为覆叠群。

*例子：$\widetilde{S^1}=\mathbb{R}$，$\widetilde{T^2}=\mathbb{R}^2$ 以 $\mathbb{Z}^2$ 为覆叠群，$\widetilde{\mathbb{RP}^n}=S^n$ 以 $\mathbb{Z}/2$ 为覆叠群。*

> **联系 — 几何与群作用**
>
> 群 $G$ 在单连通的 $\tilde X$ 上的自由、真正不连续作用给出 $\pi_1(\tilde X/G)\cong G$。这正是平坦环面、双曲曲面与透镜空间被构造的方式——几何源自在万有覆叠上的群作用。

## 第 C 部分 · 同调及更远

<a id="s9"></a>
### 单纯复形与 CW 复形

*为了计算，我们需要用标准砖块搭建的空间。单形与胞腔使同调成为线性代数中的问题。*

> **定义 — 单形与 $\Delta$-复形**
>
> **标准 $n$-单形**是 $\Delta^n=\{(t_0,\dots,t_n):t_i\ge0,\ \sum t_i=1\}$：点、线段、三角形、四面体、……它的面通过删去一个顶点获得。一个 **$\Delta$-复形**通过仿射等同沿面把单形粘合起来，并以一个选定的顶点序固定定向。

> **定义 — CW 复形**
>
> **CW 复形**逐骨架地搭建：从离散的 $0$-胞腔开始，然后用映射 $\varphi:\partial D^n=S^{n-1}\to X^{(n-1)}$ 附加 $n$-胞腔 $e^n$。"C" = 闭包有限，"W" = 弱拓扑。球面、射影空间、曲面与 Grassmann 流形全都有小而显式的 CW 结构。

**单形上的边界算子**

$$\partial_n[v_0,\dots,v_n]=\sum_{i=0}^{n}(-1)^i\,[v_0,\dots,\widehat{v_i},\dots,v_n]$$

*依次丢掉每个顶点；符号 $(-1)^i$ 编码定向。$[\,\widehat{v_i}\,]$ 表示"省略 $v_i$"。*

**演示 — 基本恒等式 $\partial^2=0$**

1. 两次应用 $\partial$：$\partial_{n-1}\partial_n[v_0,\dots,v_n]=\sum_i(-1)^i\,\partial_{n-1}[\dots\widehat{v_i}\dots]$，把每个内层边界在剩余顶点上展开。
2. 每个面 $[\dots\widehat{v_i}\dots\widehat{v_j}\dots]$（$i\lt j$）出现两次：一次先去掉 $v_i$ 再去掉 $v_j$（符号 $(-1)^i(-1)^{j-1}$，因为 $v_j$ 左移一位），一次先去掉 $v_j$ 再去掉 $v_i$（符号 $(-1)^j(-1)^i$）。
3. 两个符号相反，故每项都抵消：$\partial_{n-1}\circ\partial_n=0$。

*"边界的边界为零"是同调的代数核心——它使 $\operatorname{im}\partial_{n+1}\subseteq\ker\partial_n$。*

> **联系 — 通向线性代数**
>
> 固定一个环（通常是 $\mathbb{Z}$）：$n$-链 $C_n$ 是 $n$-胞腔上的自由模，而 $\partial_n$ 是一个矩阵。同调于是只是整数矩阵的 $\ker/\operatorname{im}$——可用 Smith 标准形求解。

<a id="s10"></a>
### 奇异同调

一个对*每个*空间都奏效、无须三角剖分的定义——代价是巨大的链群，但由强有力的定理来救赎。

**奇异链复形**

$$\cdots\xrightarrow{\ \partial_{n+1}\ }C_n(X)\xrightarrow{\ \partial_n\ }C_{n-1}(X)\xrightarrow{\ \partial_{n-1}\ }\cdots\xrightarrow{\ \partial_1\ }C_0(X)\to 0.$$

$$H_n(X)=\frac{\ker\partial_n}{\operatorname{im}\partial_{n+1}}=\frac{\text{cycles }Z_n}{\text{boundaries }B_n}.$$

*一个**奇异 $n$-单形**是任何连续映射 $\sigma:\Delta^n\to X$。令 $C_n(X)$ 是它们全体上的自由阿贝尔群，$\partial_n$ 由同样的交错面公式定义。则 $\partial^2=0$，给出一个链复形*

> **概念 — $H_n$ 度量什么**
>
> 一个**闭链**是没有边界的链（一个"封闭的环路/曲面"）；一个**边界**是某物的边界。$H_n$ 计数 $n$ 维的洞：那些*没有*被填满的闭链。$H_0$ 计数道路分支；$H_1$ 是 $\pi_1$ 的阿贝尔化；更高的 $H_n$ 看见更高维的空洞。

**演示 — $H_0(X)\cong\mathbb{Z}^{\#\text{path-components}}$**

1. $\partial_0=0$，故 $Z_0=C_0(X)$，即点上的自由群。一个 1-单形（道路）$\sigma$ 有 $\partial_1\sigma=\sigma(1)-\sigma(0)$，故 $B_0$ 由所有被道路相连的点之差生成。
2. 故两点同调当且仅当它们落在同一道路分支中；$H_0=Z_0/B_0$ 是自由阿贝尔群，每个道路分支有一个生成元。

*对道路连通的 $X$，$H_0(X)\cong\mathbb{Z}$。"增广" $\sum n_i\sigma_i\mapsto\sum n_i$ 使这一点精确。*

**Hurewicz（一次）**

$$X\text{ path-connected}\ \Longrightarrow\ H_1(X)\ \cong\ \pi_1(X)^{\mathrm{ab}}=\pi_1(X)/[\pi_1,\pi_1].$$

*同调是阿贝尔化后的 $\pi_1$：它忘掉环路的次序。故 $H_1(\Sigma_g)\cong\mathbb{Z}^{2g}$，$H_1(\bigvee_n S^1)\cong\mathbb{Z}^n$。*

<a id="s11"></a>
### 同伦不变性与正合列

*使同调可计算的三大支柱：不变性、对的长正合列，以及 Mayer–Vietoris。*

**函子性与同伦不变性**

$$f:X\to Y\ \Rightarrow\ f_*:H_n(X)\to H_n(Y),\qquad (g\circ f)_*=g_*f_*,\qquad f\simeq g\Rightarrow f_*=g_*.$$

*因此 $X\simeq Y\Rightarrow H_n(X)\cong H_n(Y)$：同调是同伦不变量，故可缩空间对 $n\gt 0$ 有 $H_n=0$ 而 $H_0=\mathbb{Z}$。*

> **概念 — 正合列**
>
> 序列 $\cdots\to A\xrightarrow{\,f\,}B\xrightarrow{\,g\,}C\to\cdots$ 在 $B$ 处**正合**，若 $\operatorname{im}f=\ker g$。正合性是一种记账手段，让未知的群被其邻居钉死。一个**短正合列** $0\to A\to B\to C\to 0$ 表示 $A\hookrightarrow B$ 且 $B\twoheadrightarrow C$，核为 $A$。

**对 $(X,A)$ 的长正合列**

$$\cdots\to H_n(A)\xrightarrow{i_*}H_n(X)\xrightarrow{j_*}H_n(X,A)\xrightarrow{\ \partial\ }H_{n-1}(A)\xrightarrow{i_*}H_{n-1}(X)\to\cdots$$

*相对同调 $H_n(X,A)$ 度量 $X$ "模" $A$；连接映射 $\partial$ 把一个相对闭链送到它留在 $A$ 中的边界。正合性把三者串联起来。*

**Mayer–Vietoris**

$$\cdots\to H_n(U\cap V)\xrightarrow{(i_*,j_*)}H_n(U)\oplus H_n(V)\xrightarrow{k_*-l_*}H_n(X)\xrightarrow{\ \partial\ }H_{n-1}(U\cap V)\to\cdots$$

*对 $X=U\cup V$（内部覆盖 $X$）。这是 van Kampen 的同调类比：它由交叠的各片计算整体。*

**演示 — Mayer–Vietoris 给出 $H_n(S^k)$**

1. 用两个略微交叠的半球 $U,V$ 覆盖 $S^k$，每个都可缩（故 $H_*(U)=H_*(V)=H_*(\text{pt})$）；交叠 $U\cap V\simeq S^{k-1}$（一条赤道带）。
2. 对 $n\ge 2$，序列左边有 $H_n(U)\oplus H_n(V)=0$，右边有 $H_{n-1}(U)\oplus H_{n-1}(V)=0$，故 $\partial:H_n(S^k)\xrightarrow{\cong}H_{n-1}(S^{k-1})$ 是同构。
3. 从基本情形 $S^0$（两点）归纳：$\tilde H_0(S^0)=\mathbb{Z}$。向上移 $k$ 次给出当 $n=k$ 时 $\tilde H_n(S^k)=\mathbb{Z}$，否则为 $0$。

*$\displaystyle H_n(S^k)=\begin{cases}\mathbb{Z},& n=0 \text{ or } n=k,\\ 0,&\text{otherwise}\end{cases}$（对 $S^0$ 在 $n=0=k$ 处为 $\mathbb{Z}^2$）。$\;\blacksquare$*

> **联系 — 同调代数**
>
> 连接映射 $\partial$ 与长正合列来自对链复形的短正合列应用*蛇引理*。这是贯穿代数始终的同一套机器——用于 $\mathrm{Tor}$、$\mathrm{Ext}$ 与导出函子。

<a id="s12"></a>
### 计算同调：度数、Euler 示性数、Betti 数

*现在我们来计算，并直接从同调读出数值不变量——Betti 数与 Euler 示性数。*

**演示 — $S^1$、$S^2$ 与环面的单纯同调**

1. $S^1$ 用一个顶点 $v$ 与一条边 $a$（一个环路）。则 $\partial_1 a=v-v=0$，故 $Z_1=\mathbb{Z}\langle a\rangle$，$B_1=0$：$H_1=\mathbb{Z}$。且 $H_0=\mathbb{Z}$。故 $H_*(S^1)=(\mathbb{Z},\mathbb{Z},0,\dots)$。
2. $S^2$ 用两个三角面沿公共边界粘合：链群给出 $H_0=\mathbb{Z}$，$H_1=0$，$H_2=\mathbb{Z}$（两个反定向的面之和是一个不界任何物的 2-闭链）。
3. 环面 $T^2$ 由正方形 $aba^{-1}b^{-1}$ 得到：一个顶点、两条边 $a,b$、一个面 $f$。则 $\partial_2 f=a+b-a-b=0$ 故 $H_2=\mathbb{Z}\langle f\rangle$；$\partial_1 a=\partial_1 b=0$ 故 $Z_1=\mathbb{Z}^2$ 且 $B_1=0$，给出 $H_1=\mathbb{Z}^2$；且 $H_0=\mathbb{Z}$。

*$H_*(T^2)=(\mathbb{Z},\ \mathbb{Z}^2,\ \mathbb{Z},\ 0,\dots)$——一个分支、两个独立的环路、一个空洞。$\;\blacksquare$*

**映射 $f:S^n\to S^n$ 的度数**

$$f_*:H_n(S^n)=\mathbb{Z}\to H_n(S^n)=\mathbb{Z}\quad\text{is multiplication by }\deg f.$$

*$\deg(\mathrm{id})=1$，$\deg(\text{constant})=0$，$\deg(g\circ f)=\deg g\cdot\deg f$，且对径映射的度数为 $(-1)^{n+1}$。度数驱动毛球定理与高维 Brouwer。*

**Betti 数与 Euler 示性数**

$$b_n=\operatorname{rank} H_n(X)=\dim_{\mathbb{Q}} H_n(X;\mathbb{Q}),\qquad \chi(X)=\sum_{n\ge0}(-1)^n b_n.$$

*$b_0=$ 分支数，$b_1=$ 独立环路数，$b_2=$ 独立空洞数。挠（例如 $\mathbb{RP}^2$ 中的 $\mathbb{Z}/2$）不影响 $b_n$ 或 $\chi$。*

**演示 — 经由 Betti 数的 Euler 示性数**

1. 对有限复形，令 $c_n$ 为 $n$-胞腔的个数，$z_n=\operatorname{rank}Z_n$，$b_n^{\partial}=\operatorname{rank}B_n$。对 $\partial_n:C_n\to C_{n-1}$ 应用秩—零化度定理给出 $c_n=z_n+b_{n-1}^{\partial}$。
2. 由定义 $b_n=z_n-b_n^{\partial}$（$\ker$ 的秩减去 $\operatorname{im}$ 的秩）。作交错和：

   $$\sum_n(-1)^n c_n=\sum_n(-1)^n\big(z_n+b_{n-1}^{\partial}\big).$$
3. $b^{\partial}$ 项与 $z$ 项相消（望远镜式），剩下

   $$\sum_n(-1)^n c_n=\sum_n(-1)^n b_n=\chi(X).$$

*故从*胞腔*算出的 $\chi$ 等于从*同调*算出的 $\chi$——一个拓扑不变量。对曲面 $V-E+F=2-2g$。$\;\blacksquare$*

| 空间 | $\pi_1$ | $H_0,H_1,H_2,\dots$ | $\chi$ |
| --- | --- | --- | --- |
| 点 | $1$ | $\mathbb{Z},0,0,\dots$ | $1$ |
| $S^1$ | $\mathbb{Z}$ | $\mathbb{Z},\mathbb{Z},0,\dots$ | $0$ |
| $S^n\ (n\ge2)$ | $1$ | $\mathbb{Z},0,\dots,\mathbb{Z}\,(\deg n),0,\dots$ | $1+(-1)^n$ |
| 环面 $T^2$ | $\mathbb{Z}^2$ | $\mathbb{Z},\mathbb{Z}^2,\mathbb{Z},0,\dots$ | $0$ |
| $\Sigma_g$（亏格 $g$） | $\langle a_i,b_i\mid\prod[a_i,b_i]\rangle$ | $\mathbb{Z},\mathbb{Z}^{2g},\mathbb{Z},0,\dots$ | $2-2g$ |
| $\bigvee_n S^1$ | $F_n$（自由） | $\mathbb{Z},\mathbb{Z}^n,0,\dots$ | $1-n$ |
| $\mathbb{RP}^2$ | $\mathbb{Z}/2$ | $\mathbb{Z},\ \mathbb{Z}/2,\ 0,\dots$ | $1$ |
| $\mathbb{RP}^n$（$n$ 奇） | $\mathbb{Z}/2$ | $\mathbb{Z},\mathbb{Z}/2,\dots,\mathbb{Z}$ | $0$ |
| $\mathbb{RP}^n$（$n$ 偶） | $\mathbb{Z}/2$ | $\mathbb{Z},\mathbb{Z}/2,\dots,0$ | $1$ |

> **联系 — 抽象代数重现**
>
> 在 $\mathbb{Z}$ 上，有限生成阿贝尔群的结构定理把 $H_n\cong\mathbb{Z}^{b_n}\oplus(\text{torsion})$ 分裂。Betti 数是自由秩；挠（如 $\mathbb{RP}^n$ 的 $\mathbb{Z}/2$）记录 $\chi$ 看不见的更微妙的"扭转"。

<a id="s13"></a>
### 上同调与杯积

把链对偶化给出上同调——同样的 Betti 数，但现在带有同调所缺乏的*环*结构。这额外的乘法分离了同调无法分离的空间。

**上链复形与上同调**

$$C^n(X;R)=\operatorname{Hom}(C_n(X),R),\qquad \delta=\partial^{*}:C^n\to C^{n+1},\qquad H^n(X;R)=\frac{\ker\delta}{\operatorname{im}\delta}.$$

*上边界 $\delta$ 是 $\partial$ 的转置；$\delta^2=0$，因为 $\partial^2=0$。箭头现在在次数上*向上*指，使上同调反变：$f:X\to Y$ 给出 $f^*:H^n(Y)\to H^n(X)$。*

**万有系数**

$$0\to \operatorname{Ext}^1_{\mathbb{Z}}(H_{n-1}(X),R)\to H^n(X;R)\to \operatorname{Hom}(H_n(X),R)\to 0.$$

*在域上，$\operatorname{Ext}=0$ 且 $H^n\cong\operatorname{Hom}(H_n,\text{field})$：与同调相同的 Betti 数。新意在乘法，而非加法。*

> **定义 — 杯积与上同调环**
>
> **杯积** $\smile:H^p(X;R)\times H^q(X;R)\to H^{p+q}(X;R)$ 使 $H^*(X;R)=\bigoplus_n H^n$ 成为分次环。它是分次交换的：$\alpha\smile\beta=(-1)^{pq}\,\beta\smile\alpha$，且自然：$f^*(\alpha\smile\beta)=f^*\alpha\smile f^*\beta$。

**演示 — 杯积把 $T^2$ 与 $S^2\vee S^1\vee S^1$ 分离**

1. 两个空间有完全相同的同调与上同调群：$H^0=\mathbb{Z}$，$H^1=\mathbb{Z}^2$，$H^2=\mathbb{Z}$。加性不变量无法区分它们。
2. 对环面，$H^1=\langle\alpha,\beta\rangle$，杯积是非退化的：$\alpha\smile\beta$ 生成 $H^2=\mathbb{Z}$（且 $\alpha\smile\alpha=0$）。这个环是外代数 $\Lambda[\alpha,\beta]$。
3. 对楔 $S^2\vee S^1\vee S^1$，来自不同楔加项的两个类的任何乘积都是 $0$（它们只共享基点）：$\alpha\smile\beta=0$。乘积是平凡的。

*不同的环结构 $\Rightarrow$ 这两个空间不同伦等价——一个仅靠同调无法看到的区分。$\;\blacksquare$*

> **联系 — 通向微分几何**
>
> 对光滑流形，**de Rham 上同调**（闭模恰当微分形式）计算 $H^*(X;\mathbb{R})$，而杯积变成形式的*楔积*。拓扑、流形上的微积分与环论在同一个对象中相遇。

<a id="s14"></a>
### 略窥更远：高阶同伦群、流形与 Poincaré 对偶

*学科开阔起来之处：高阶 $\pi_n$（困难但丰富）、流形的特殊结构，以及组织其（上）同调的对偶。*

> **定义 — 高阶同伦群 $\pi_n$**
>
> $\pi_n(X,x_0)$ 是带基点映射 $S^n\to X$ 的同伦类。对 $n\ge2$ 它们是**阿贝尔的**（Eckmann–Hilton 论证：同一集合上两个可交换的带单位元乘积必然重合且交换）。与同调不同，$\pi_n$ 极其难算——即便是 $k\gt n$ 的 $\pi_k(S^n)$ 也大体上神秘莫测（"球面的稳定同伦群"）。

**Hurewicz 定理（一般情形）**

$$\pi_k(X)=0\ \text{for } k\lt n\ (n\ge2)\ \Longrightarrow\ H_k(X)=0\ (0\lt k\lt n)\ \text{and}\ \pi_n(X)\cong H_n(X).$$

*第一个非零的同伦群与同调群一致。这是从可计算者（$H_*$）通向难捉摸者（$\pi_*$）的桥梁。*

**Poincaré 对偶**

$$M\text{ closed oriented }n\text{-manifold}\ \Longrightarrow\ H_k(M;\mathbb{Z})\ \cong\ H^{n-k}(M;\mathbb{Z}).$$

$$\text{In particular}\quad b_k(M)=b_{n-k}(M).$$

*与基本类 $[M]\in H_n(M)$ 的卡积给出该同构。Betti 数是对称的；对奇数维闭可定向 $M$ 这迫使 $\chi(M)=0$。*

**演示 — 亏格 $g$ 曲面上的对偶**

1. $\Sigma_g$ 是闭可定向 $2$-流形，$b_0=1,\ b_1=2g,\ b_2=1$。
2. Poincaré 对偶预言 $b_0=b_2$（$\;1=1\;\checkmark$）与 $b_1=b_1$（显然）。配对 $H^1\times H^1\to H^2\cong\mathbb{Z}$ 是第 13 节的杯积——相交形式，一个秩为 $2g$ 的非退化反对称配对。

*几何上，每个环路 $a_i$ 都有一个恰好与它相交一次的对偶环路 $b_i$：洞成对偶地出现。$\;\blacksquare$*

> **联系 — 更广阔的图景**
>
> 由此而出：纤维丛与纤维化的长正合列、谱序列、示性类（Chern、Stiefel–Whitney）、K-理论，以及分类流形的配边 / 手术纲领。每条路依旧起于同一个想法——一个从空间到代数的函子，经由正合列来计算。

---

*一门代数拓扑的入门课程——概念、定义、定理及其背后的演示——作为《完整统计学指南》与《微积分指南》的伴侣而建。读一遍把握其形状；把任何方框当作参考随时回看。记住：每一章都是一个把连续映射变成同态的函子，使得不同的代数证明不同的空间。*
