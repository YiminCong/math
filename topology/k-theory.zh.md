[English](k-theory.md) · **中文**

# 拓扑 K 理论，*作为广义上同调的向量丛。*

*一门自洽、严谨的拓扑 K 理论入门课程。其思想简单得令人意外：我们不再对空间作三角剖分并数胞腔，而是去观察居于该空间之上的向量空间族——即**向量丛**——并把它们打包成一个代数不变量。事实证明，这个不变量几乎服从普通上同调的全部法则，却额外拥有一种非凡的新对称性——Bott 周期性——这是普通上同调所缺乏的。每个术语在首次出现时都给出定义，每条定理在陈述之前都用平实的语言加以说明，每个论断都加以论证而非断言。*

[← 返回全部指南](../README.zh.md)

> **如何阅读本指南。** 我们假定读者已熟悉**代数拓扑**指南（映射的同伦、同伦等价、上同调群 $H^n(X;G)$、杯积、悬挂 $\Sigma X$、对的长正合列，以及通过 Eilenberg–Steenrod 公理给出的广义上同调理论概念）以及**微分拓扑**指南（光滑流形、向量丛、切丛、示性类、Chern 类 $c_i$ 与 Thom 同构）。我们还会用到一点线性代数（向量空间、直和、张量积、对偶）与群论（阿贝尔群、环）。每当我们倚重其中某项时，都会用一行话重述所需的确切事实。本课程不预设任何 K 理论基础；每个新词——*Grothendieck 群*、*约化 K 理论*、*Bott 周期性*、*Chern 特征标*、*Clifford 代数*——都在首次出现时给出定义。

---

## 第 A 部分 · 从向量丛到一个群

<a id="s0"></a>
### 动机 —— 对向量丛分类，以及由它们构造的一个上同调理论

拓扑空间 $X$ 上的一个**向量丛**，非正式地说，是一族连续变化的向量空间——给每个点 $x\in X$ 附上一个向量空间 $E_x$（即**纤维**），并将它们黏合起来，使得局部上看起来像一个乘积 $U\times\mathbb{C}^n$。（精确定义见 §s1。）最简单的例子是**平凡丛** $X\times\mathbb{C}^n$，其中每根纤维都是同一份 $\mathbb{C}^n$ 的拷贝，以及光滑流形的**切丛**，其在 $x$ 处的纤维是切空间 $T_xM$。

两个基本问题驱动着整个学科：

- **分类。** 给定 $X$，它至多在同构意义下承载多少个秩为 $n$ 的向量丛？在可缩空间上答案是“只有平凡丛”，但在球面 $S^2$ 上却有无穷多个线丛，由一个整数（次数）来标记。对向量丛分类之所以困难，是因为同构类的集合只是一个带有加法（直和）的集合，而这个加法没有逆元。

- **由向量丛得到一个不变量。** 普通上同调 $H^*(X)$ 是从所选的组合骨架（胞腔、单形）构造出来的。我们能否转而*直接*从 $X$ 上的向量丛构造出一个函子性的不变量——一个给每个空间赋以一个环、给每个连续映射赋以一个环同态、并且我们真的能计算的东西？

第二个问题的答案就是 **K 理论**，由 Atiyah 与 Hirzebruch 发明（遵循 Grothendieck 的代数构造）。其配方有两步：

1. **补全缺失的逆元。** 向量丛在 $\oplus$ 下的同构类构成一个交换幺半群（一个带零元但无减法的结合加法）。**Grothendieck 群**构造（§s2）形式地添加逆元，把这个幺半群变成一个阿贝尔群 $K^0(X)$。向量丛的张量积使它成为一个环。

2. **构造高阶群并发现周期性。** 利用悬挂 $\Sigma X$，我们对所有 $n\ge 0$ 定义群 $K^{-n}(X)$（§s4），而 **Bott 周期性定理**（§s5）将这架无穷长的梯子坍缩为仅有两个群 $K^0$ 与 $K^{-1}$，以周期 $2$ 重复。这种周期性在普通上同调中没有类比，正是它这一特征使 K 理论既刚性又可计算。

其回报是一个**广义上同调理论**（§s6）：K 理论满足除维数公理外的每一条 Eilenberg–Steenrod 公理（维数公理说点的上同调集中在次数 $0$）。把“点的上同调”替换为“点的 K 理论，它在*每个偶次数*都是 $\mathbb{Z}$”恰恰就是 Bott 周期性。由这一处改动流出了 Chern 特征标（§s7）、Thom 同构与前推（§s8）、具有八重周期性的实 K 理论（§s9），以及与分析和物理的深刻联系（§s10–s11）。

> **原理 —— K 理论的策略。**
> 不要逐个地对向量丛分类。而要把它们统统扔进一个代数对象，这个对象只记录在添加平凡丛之下保持稳定的信息，然后利用由此产生的周期性。“稳定”是关键词：$K$ 理论只在添加平凡直和项的意义下看一个向量丛，而这种稳定化恰恰使该理论刚性到足以计算、丰富到足以探测指标理论与 D 膜荷。

**路线图。** 第 A 部分（§s1–s3）由向量丛构造 $K^0(X)$，并对点和球面计算它。第 B 部分（§s4–s6）搭建上同调理论：高阶群、Bott 周期性、公理。第 C 部分（§s7–s8）通过 Chern 特征标把 K 理论与普通上同调联系起来，并发展指标理论所需的前推。第 D 部分（§s9–s11）综述实理论、解析 K 理论，以及 K 理论在物理中的出现。赶时间的读者可以读 §s0、§s2、§s5 和 §s7，仍能看到整条弧线。

<a id="s1"></a>
### 向量丛回顾；运算；拉回与同伦不变性

除非另有说明，我们在复数上工作；“向量空间”意指“有限维复向量空间”，而 $X$ 记一个**紧 Hausdorff 空间**（紧：每个开覆盖都有有限子覆盖；Hausdorff：相异点有不交的邻域）。在第 A–B 部分中始终假定紧性，因为它保证了关键的有限性事实（每个向量丛都是某个平凡丛的直和项，§s2）。

> **定义 —— 向量丛。**
> $X$ 上的一个（复的、秩为 $n$ 的）**向量丛**是一个拓扑空间 $E$ 连同一个连续满射 $\pi:E\to X$，使得：
> (i) 每根**纤维** $E_x:=\pi^{-1}(x)$ 都带有 $n$ 维复向量空间的结构；
> (ii) **局部平凡性**：$X$ 的每个点都有一个开邻域 $U$ 和一个同胚 $\varphi:\pi^{-1}(U)\to U\times\mathbb{C}^n$（一个**局部平凡化**），满足 $\varphi(E_x)=\{x\}\times\mathbb{C}^n$，且 $\varphi$ 在每根纤维上限制为一个*线性*同构 $E_x\cong\mathbb{C}^n$。
> 数 $n$ 是**秩**。秩为 $1$ 的丛是**线丛**。空间 $E$ 是**全空间**，$X$ 是**底空间**，$\pi$ 是**投影**。

在两个平凡化 $\varphi_\alpha,\varphi_\beta$ 重叠之处，复合 $\varphi_\alpha\varphi_\beta^{-1}$ 在 $(U_\alpha\cap U_\beta)\times\mathbb{C}^n$ 上具有形式 $(x,v)\mapsto(x,g_{\alpha\beta}(x)v)$，其中 $g_{\alpha\beta}:U_\alpha\cap U_\beta\to GL_n(\mathbb{C})$ 是一个连续映射，即**转移函数**。它们满足**上链条件** $g_{\alpha\beta}g_{\beta\gamma}=g_{\alpha\gamma}$，反之任何满足该条件的映射系统都可通过黏合构造一个向量丛。这是我们在例子中所用的具体把手。

**例题 —— 通过转移函数得到 Möbius 丛。** 用两段弧 $U=\{0<\theta<\pi+\epsilon\}$ 和 $V=\{\pi-\epsilon<\theta<2\pi+\epsilon\}$ 覆盖 $S^1$（角度 $\theta\in[0,2\pi)$）。它们的重叠有两个连通分支，分别在 $\theta=0$ 附近和 $\theta=\pi$ 附近。在 $\theta=\pi$ 附近的分支上取转移函数 $g_{UV}=+1$，在 $\theta=0$ 附近的分支上取 $g_{UV}=-1$，由此定义一个实线丛。这单个符号翻转意味着一个标架绕一圈传输回来后被取负：这就是 **Möbius 带**，$S^1$ 上非平凡的实线丛。若处处取 $g_{UV}\equiv+1$，则得到平凡的柱面。上链条件是平凡满足的（只有两张图卡），所以唯一的不变量就是符号的集合（在改变局部标架的等价关系下）——恰好是 $\mathbb{Z}/2=\{\text{柱面},\text{Möbius}\}$，与 §s3 的黏合计数 $\pi_0(GL_1(\mathbb{R}))$ 相符。（$S^1$ 上的复线丛没有类比，因为 $\mathbb{C}^\times$ 是连通的——没有可翻转的符号——故 $\tilde K^0(S^1)=0$。）

> **定义 —— 截面、态射、同构。**
> $\pi:E\to X$ 的一个**截面**是连续映射 $s:X\to E$ 满足 $\pi\circ s=\mathrm{id}_X$（它在每根纤维中挑选一个向量 $s(x)\in E_x$）。一个**丛态射** $f:E\to F$（在同一底空间上）是满足 $\pi_F\circ f=\pi_E$ 且在每根纤维上线性的连续映射；若它有逆态射则称为**同构**。我们用 $\mathrm{Vect}_n(X)$ 记秩为 $n$ 的丛的同构类集合，并记 $\mathrm{Vect}(X)=\bigsqcup_n\mathrm{Vect}_n(X)$。

**这些运算。** 向量空间上每个函子性的运算都逐纤维地延拓到向量丛上，因为它可以作用于转移函数，并且上链条件得以保持。

> **定义 —— 直和、张量积、对偶。**
> 给定 $X$ 上的丛 $E,F$：
> - **Whitney 和**（直和）$E\oplus F$ 的纤维为 $(E\oplus F)_x=E_x\oplus F_x$，秩为 $\mathrm{rk}\,E+\mathrm{rk}\,F$，转移函数为块对角的 $g^E_{\alpha\beta}\oplus g^F_{\alpha\beta}$。
> - **张量积** $E\otimes F$ 的纤维为 $E_x\otimes F_x$，秩为 $(\mathrm{rk}\,E)(\mathrm{rk}\,F)$，转移函数为 $g^E_{\alpha\beta}\otimes g^F_{\alpha\beta}$。
> - **对偶** $E^*$ 的纤维为 $(E_x)^*=\mathrm{Hom}(E_x,\mathbb{C})$，转移函数为 $(g^E_{\alpha\beta})^{-\top}$（逆转置）。

这些逐纤维地服从向量空间的通常代数律：$\oplus$ 可交换、可结合，以秩为 $0$ 的丛为单位元；$\otimes$ 可交换、可结合，以平凡线丛 $\underline{\mathbb{C}}:=X\times\mathbb{C}$ 为单位元；且 $\otimes$ 对 $\oplus$ 满足分配律。我们用 $\underline{\mathbb{C}}^n=X\times\mathbb{C}^n$ 记秩为 $n$ 的平凡丛。

> **定义 —— 拉回。**
> 设 $f:Y\to X$ 连续，$\pi:E\to X$ 是一个丛。**拉回** $f^*E$ 是 $Y$ 上的丛，其全空间为 $f^*E=\{(y,e)\in Y\times E:f(y)=\pi(e)\}$，投影为 $(y,e)\mapsto y$；其在 $y$ 上的纤维为 $E_{f(y)}$。若 $E$ 在 $\{U_\alpha\}$ 上有转移函数 $g_{\alpha\beta}$，则 $f^*E$ 在 $\{f^{-1}(U_\alpha)\}$ 上有转移函数 $g_{\alpha\beta}\circ f$。

拉回是函子性的：$(\mathrm{id})^*E\cong E$ 且 $(g\circ f)^*E\cong f^*(g^*E)$，并且它与 $\oplus,\otimes,(-)^*$ 交换。向量丛对 K 理论而言最重要的单条性质是：拉回只依赖于映射的同伦类。

> **定理（拉回的同伦不变性）。** 设 $X$ 仿紧（紧 Hausdorff 即足够），$E\to X$ 是一个向量丛。若 $f_0,f_1:Y\to X$ 是同伦的连续映射，则 $f_0^*E\cong f_1^*E$。

*平实语言的想法。* 一个同伦是 $Y\times[0,1]$ 上的一个丛；我们证明这样的丛在同构意义下沿 $[0,1]$ 方向是常值的，故其两端一致。我们先证明引擎，再推出定理。

**演示 —— $Y\times[0,1]$ 上的丛是从 $Y$ 拉回的。**

1. 设 $H:Y\times[0,1]\to X$ 是从 $f_0$ 到 $f_1$ 的同伦，置 $E_H:=H^*E$，这是 $Y\times[0,1]$ 上的一个丛。只需证明 $E_H\cong p^*(E_H|_{Y\times\{0\}})$，其中 $p:Y\times[0,1]\to Y\times\{0\}$ 是投影，因为这样限制到两端就给出 $f_1^*E=E_H|_{Y\times\{1\}}\cong E_H|_{Y\times\{0\}}=f_0^*E$。*（拉回与限制的定义）*
2. **局部陈述。** 在一点 $y_0\in Y$ 之上，$E_H$ 限制到 $\{y_0\}\times[0,1]$ 是区间上的一个丛，因而平凡（区间可缩；可缩仿紧底空间上的任何丛都平凡——见 §s3 经黏合/延拓的证明，或将其当作标准事实：$[0,1]$ 上的丛通过从 $\{0\}$ 延拓得到一个处处非零标架）。于是存在 $y_0$ 的邻域 $U$，可能缩小后，$E_H$ 在 $U\times[0,1]$ 上平凡化；在 $t$ 方向延拓一个平凡化的障碍是区间上一个连续线性延拓问题的解，总是可解的。*（局部平凡性；区间上的平凡性）*
3. **拼接。** 用这样的邻域 $U_i$ 覆盖 $Y$，在其上 $E_H\cong p^*(E_H|_{U_i\times\{0\}})$。取从属于 $\{U_i\}$ 的单位分解 $\{\rho_i\}$（由仿紧性存在）。用每个 $U_i$ 上的同构，通过 $\{\rho_i\}$ 加权对局部平凡化标架作**单位分解插值**，从而构造一个整体丛同构；黏合的线性性与参数 $t$ 的凸性使该插值良定义且可逆。*（单位分解黏合局部同构；凸组合经同伦提升论证保持在 $GL$ 中）*
4. 其结果是一个整体同构 $E_H\cong p^*(E_H|_{Y\times\{0\}})$，证毕。*（第 1–3 步）*

**推论（计算引擎）。** 向量丛是一个同伦不变的函子：$\mathrm{Vect}(X)$ 只依赖于 $X$ 的同伦型。特别地，**可缩**空间上的每个丛都平凡（取 $Y=X$，$f_0=\mathrm{id}$，$f_1=$ 常值；则 $E\cong f_0^*E\cong f_1^*E=$ 平凡）。

**陷阱。** 同伦不变性需要仿紧性（使单位分解存在）。在野性的底空间上它可能失效。对我们而言 $X$ 总是紧 Hausdorff 的，故无需担心。

<a id="s2"></a>
### Grothendieck 群构造；作为环的 $K^0(X)$；约化群 $\tilde K^0(X)$

集合 $\mathrm{Vect}(X)$ 连同 $\oplus$ 是一个**交换幺半群**：一个可结合、可交换、有单位元（秩为 $0$ 的丛）但一般无逆元的加法——你不能“减去”一个丛。K 理论的开端是借助一个泛代数手段强行造出逆元。

> **定义 —— 交换幺半群的 Grothendieck 群。**
> 设 $(M,+,0)$ 是一个交换幺半群。它的 **Grothendieck 群** $\mathcal G(M)$ 是按如下方式定义的阿贝尔群。在集合 $M\times M$（把 $(a,b)$ 想成形式差“$a-b$”）上赋予等价关系
> $$
> (a,b)\sim(c,d)\iff \exists\,k\in M:\ a+d+k=c+b+k.
> $$
> 置 $\mathcal G(M)=(M\times M)/\!\sim$，加法为 $[(a,b)]+[(c,d)]=[(a+c,b+d)]$。$(a,0)$ 的类记为 $[a]$，且 $[(a,b)]=[a]-[b]$。

额外的“$+k$”是必不可少的：没有它，当 $M$ 不具消去性时 $\sim$ 未必传递。让我们验证 $\mathcal G(M)$ 确实是一个群且具有泛性质。

**演示 —— $\mathcal G(M)$ 是阿贝尔群，且在到群的幺半群同态中是泛的。**

1. **$\sim$ 是等价关系。** 自反性与对称性由对称形式 $a+d+k=c+b+k$ 立得。传递性：若 $a+d+k=c+b+k$ 且 $c+f+l=e+d+l$，把它们相加并借见证项消去：$a+f+(d+k+c+l)=e+b+(d+k+c+l)$，故 $(a,b)\sim(e,f)$，见证项为 $d+k+c+l$。*（$M$ 中 $+$ 的交换性与结合性）*
2. **加法良定义且阿贝尔**，因为它由 $M$ 上阿贝尔的 $+$ 逐坐标计算且尊重 $\sim$（把两个见证项相加）。单位元是 $[(0,0)]=[0]$。*（逐坐标继承）*
3. **逆元存在：** $[(a,b)]+[(b,a)]=[(a+b,a+b)]=[0]$，因为 $(a+b,a+b)\sim(0,0)$，见证项为 $0$。故 $-[a]=[(0,a)]$。*（$\sim$ 的定义）*
4. **泛性质。** 映射 $\iota:M\to\mathcal G(M)$，$a\mapsto[a]$，是幺半群同态；并且对任何阿贝尔群 $A$ 和幺半群同态 $\phi:M\to A$，存在*唯一*的群同态 $\bar\phi:\mathcal G(M)\to A$ 满足 $\bar\phi\circ\iota=\phi$，即 $\bar\phi([a]-[b])=\phi(a)-\phi(b)$（良定义，因为 $\phi$ 尊重 $\sim$：在群 $A$ 中见证项 $k$ 可消去）。*（群完备化的泛性质）*

> **定义 —— $K^0(X)$。**
> $K^0(X):=\mathcal G(\mathrm{Vect}(X))$，即 $X$ 上复向量丛在 $\oplus$ 下的同构类的 Grothendieck 群。它的元素，**虚丛**，是形式差 $[E]-[F]$。

**经稳定化的更干净描述。** 在紧底空间上，每个类都是一个真正的丛与一个*平凡*丛之差。

> **引理（可补性）。** 对紧 Hausdorff 空间 $X$ 上的任何向量丛 $E$，存在一个丛 $E'$ 使得对某个 $N$ 有 $E\oplus E'\cong\underline{\mathbb{C}}^N$。

*证明。* 用有限多个平凡化开集 $U_1,\dots,U_m$ 覆盖 $X$（由紧性可取有限）；取单位分解 $\{\rho_i\}$。映射 $\rho_i\cdot(\text{平凡化}_i):E\to\mathbb{C}^{n}$ 组装成一个逐纤维单射的丛映射 $E\hookrightarrow\underline{\mathbb{C}}^{mn}=:\underline{\mathbb{C}}^N$（单射是因为在每点至少有一个 $\rho_i>0$ 且该分量为单射）。在 $\underline{\mathbb{C}}^N$ 上放一个 Hermite 度量（用 $\{\rho_i\}$ 对局部度量求平均）；则 $E'=E^\perp$ 是一个丛，满足 $E\oplus E'\cong\underline{\mathbb{C}}^N$。$\square$

> **推论 —— 稳定形式。** $K^0(X)$ 的每个元素都等于某个丛 $E$ 与某个整数 $n$ 的 $[E]-[\underline{\mathbb{C}}^n]$。两个丛在 $K^0(X)$ 中满足 $[E]=[F]$，当且仅当它们**稳定同构**：对某个 $k$ 有 $E\oplus\underline{\mathbb{C}}^k\cong F\oplus\underline{\mathbb{C}}^k$（这就是关系 $\sim$，可补性引理把见证项变成了一个平凡丛）。

> **定义 —— 环结构。**
> 张量积使 $K^0(X)$ 成为一个**交换环**：定义 $([E]-[F])\cdot([E']-[F'])=[E\otimes E']+[F\otimes F']-[E\otimes F']-[F\otimes E']$。乘法单位元是 $[\underline{\mathbb{C}}]$（平凡线丛）。对 $+$ 的分配律来自 $\otimes$ 逐纤维对 $\oplus$ 的分配律。

这是良定义的（不依赖代表元），由泛性质应用两次得到，所用的是 $\otimes$ 对 $\oplus$ 的双加性。

**例题 —— 在 $K^0(S^2)$ 中作乘法。** 用基 $\{1,\beta\}$，其中 $\beta=H-1$，配合关系 $\beta^2=0$（§s3）：两个一般元素之积为
$$
(a+b\beta)(c+d\beta)=ac+(ad+bc)\beta+bd\,\beta^2=ac+(ad+bc)\beta.
$$
故 $\tilde K^0(S^2)=\mathbb{Z}\beta$ 是一个平方为零的理想——乘法上平凡的约化 K 理论。这种幂零性在球面上是普遍的：$\tilde K^0(S^n)$ 的乘积总是消失（任何两个正次数类之积落在 $\tilde K^0(S^{n}\wedge S^{n})$-次数 $>n$ 中，被迫为零），故球面的环信息完全在于加法群加上单位元。有意思的乘法结构出现在像 $\mathbb{CP}^n$ 这样的空间上，那里 $x^n\ne0$。

**函子性。** 连续映射 $f:Y\to X$ 诱导出 $f^*:K^0(X)\to K^0(Y)$，一个*环同态*，定义为 $f^*([E]-[F])=[f^*E]-[f^*F]$（拉回尊重 $\oplus,\otimes$）。由同伦不变性（§s1），同伦的映射诱导相等的同态；于是 $K^0$ 是从紧空间到交换环的一个同伦不变的逆变函子——第一条类上同调性质。

> **定义 —— 秩同态与约化 K 理论。**
> 设 $X$ 连通（使秩在每个丛上是良定义的整数）。**秩** $\mathrm{rk}:K^0(X)\to\mathbb{Z}$，$[E]-[F]\mapsto\mathrm{rk}\,E-\mathrm{rk}\,F$，是一个满的环同态。它的核是**约化 K 理论**
> $$
> \tilde K^0(X):=\ker\big(\mathrm{rk}:K^0(X)\to\mathbb{Z}\big).
> $$
> 等价地，选一个基点 $x_0\in X$，含入映射 $i:\{x_0\}\hookrightarrow X$，则 $\tilde K^0(X)=\ker\big(i^*:K^0(X)\to K^0(\mathrm{pt})=\mathbb{Z}\big)$，并存在一个典范分裂
> $$
> K^0(X)\cong\tilde K^0(X)\oplus\mathbb{Z}.
> $$

这个分裂成立，是因为常值映射 $X\to\{x_0\}$ 给出一个环映射 $\mathbb{Z}=K^0(\mathrm{pt})\to K^0(X)$，它是 $i^*$ 的一个截面；其像是平凡丛，而 $\tilde K^0$ 度量“非平凡部分”。在 $\tilde K^0(X)$ 中，一个虚丛只在添加任意秩的平凡丛的意义下被记录——这是*稳定*现象的形式归宿。

> **直观。** $K^0(X)$ 回答“在减法与稳定化意义下，所有的丛是什么？”整数部分 $\mathbb{Z}$ 是无趣的秩；$\tilde K^0(X)$ 才是拓扑所在之处。对 $X=S^2$ 我们将发现 $\tilde K^0(S^2)\cong\mathbb{Z}$，由 Hopf 线丛与平凡丛之差 $[H]-[\underline{\mathbb{C}}]$ 生成（§s3）。

**例题 —— $\mathbb{N}$ 的 Grothendieck 群，带数字。** 取 $M=(\mathbb{N},+,0)$，原型幺半群（它就是 $\mathrm{Vect}(\mathrm{pt})$）。一对 $(a,b)$ 意指“$a-b$”。则 $(3,1)\sim(5,3)$，因为 $3+3+0=5+1+0$，即二者都代表 $2$。$(0,1)$ 的类是 $\mathbb{N}$ 所缺乏的新元素 $-1$。映射 $[a]-[b]\mapsto a-b$ 是同构 $\mathcal G(\mathbb{N})\cong\mathbb{Z}$。见证项“$+k$”在此不可见，因为 $\mathbb{N}$ 具消去性；而对像 $\mathrm{Vect}(X)$ 这样的幺半群它就变得必不可少了——在那种空间上 $E\oplus G\cong F\oplus G$ *并不*强制 $E\cong F$（只有稳定同构），故见证项 $k$ 编码了“$\oplus$ 一个平凡丛”。这正是为什么 $K^0$ 只在稳定化意义下记住向量丛。

**陷阱 —— 映射 $\mathrm{Vect}(X)\to K^0(X)$ 未必是单射。** 相异的丛在 $K^0$ 中可以变得相等：若 $E\oplus\underline{\mathbb{C}}^k\cong F\oplus\underline{\mathbb{C}}^k$ 但 $E\not\cong F$，则 $[E]=[F]$。这样非同构却*稳定同构*的丛是存在的（例如在高维球面上，$S^n$ 的切丛稳定平凡——$TS^n\oplus\underline{\mathbb{R}}\cong\underline{\mathbb{R}}^{n+1}$——然而除非 $n\in\{1,3,7\}$，$TS^n$ 是非平凡的）。K 理论有意忘掉这一区别；正是这种忘却换来了可计算性。

<a id="s3"></a>
### 例题 —— $K^0(\mathrm{point})$、$K^0(S^2)$，以及线丛的作用

**例 1 —— 点。** 在 $X=\{*\}$ 上，一个向量丛就是一个有限维向量空间，至多在同构意义下由其维数分类。故 $\mathrm{Vect}(\mathrm{pt})\cong(\mathbb{N},+)$，且
$$
K^0(\mathrm{pt})=\mathcal G(\mathbb{N})=\mathbb{Z},\qquad \tilde K^0(\mathrm{pt})=0,
$$
环结构即 $\mathbb{Z}$ 的环结构（向量空间的张量积使维数相乘）。这是 $H^0(\mathrm{pt})=\mathbb{Z}$ 的类比；与普通上同调的区别在于，点的 $K$ 理论在*所有偶次数*都非零（§s5）。

**线丛与黏合。** 为计算 $K^0(S^2)$，我们需要知道球面上的丛。工具是*黏合*：在两个半球上分别平凡化，沿赤道黏合，由此在 $S^n$ 上构造一个丛。

> **构造 —— $S^n$ 上的黏合。** 把 $S^n=D_+^n\cup_{S^{n-1}}D_-^n$ 写成两个沿边界赤道 $S^{n-1}$ 黏合的闭圆盘。在每个圆盘上平凡的丛，至多在同构意义下，由一个连续的**黏合函数** $g:S^{n-1}\to GL_n(\mathbb{C})$ 决定，它指明两个平凡丛在赤道上如何被等同。同伦的黏合函数给出同构的丛，而 $\oplus$ 对应块和 $g\mapsto g\oplus g'$。于是
> $$
> \mathrm{Vect}_n(S^k)\cong[S^{k-1},GL_n(\mathbb{C})]=\pi_{k-1}(GL_n(\mathbb{C})),
> $$
> 即从赤道到 $GL_n(\mathbb{C})$ 的映射的同伦类集合（因 $GL_n$ 是拓扑群，经 $\pi_{k-1}$ 成为一个群）。

*为何同伦的黏合函数给出同构的丛：* 一个同伦 $g_t$ 是 $S^k\times[0,1]$ 上某个丛的黏合函数，其两端是那两个丛；柱面上丛的同伦不变性（§s1）将它们等同。

**$S^2$ 上的线丛。** 此处 $n=1$，$k=2$：黏合函数是映射 $g:S^1\to GL_1(\mathbb{C})=\mathbb{C}^\times$。由于 $\mathbb{C}^\times\simeq S^1$ 形变收缩到单位圆上，$\pi_1(\mathbb{C}^\times)=\mathbb{Z}$，即 $g$ 的**缠绕数**（次数）。因此 $S^2$ 上的线丛由一个整数分类：
$$
\mathrm{Vect}_1(S^2)\cong\pi_1(\mathbb{C}^\times)=\mathbb{Z}.
$$
生成元（缠绕数 $1$）是 **Hopf 线丛** $H$，即 $\mathbb{CP}^1=S^2$ 的重言线丛，其在直线 $\ell\subset\mathbb{C}^2$ 上的纤维就是 $\ell$ 本身。线丛的张量积使缠绕数相加：$H^{\otimes m}$ 的缠绕数为 $m$，故 $\mathrm{Vect}_1(S^2)\cong\mathbb{Z}$ 在 $\otimes$ 下是一个*群*（**Picard 群**），$H$ 为生成元，$H^{-1}=H^*$。

> **一条关键关系 —— 基本乘积关系。** 在 $K^0(S^2)$ 中，
> $$
> (\,[H]-1\,)^2=0,\qquad\text{等价地}\qquad [H]^2=2[H]-1,
> $$
> 其中 $1=[\underline{\mathbb{C}}]$。

**该关系的演示。** $(H-1)^2=H^2-2H+1=H\otimes H-2H+1$。作为丛，$H\otimes H\oplus\underline{\mathbb{C}}\cong H\oplus H$：二者都是 $S^2$ 上秩为 $2$ 的丛，黏合函数在 $\otimes$ 下相乘、在 $\oplus$ 下（块）相加，故 $H\otimes H$ 的黏合为 $z\mapsto z^2$，而 $H\oplus H$ 的黏合为 $z\mapsto\mathrm{diag}(z,z)$；矩阵 $\mathrm{diag}(z^2,1)$ 与 $\mathrm{diag}(z,z)$ 在 $GL_2(\mathbb{C})$ 中同伦（二者行列式缠绕数都为 $2$，且 $GL_2(\mathbb{C})$ 连通、其 $\pi_1=\mathbb{Z}$ 由行列式探测）。因此作为丛 $H^2+1\cong 2H$，在 $K^0(S^2)$ 中给出 $H^2-2H+1=0$。$\square$

> **定理（$K^0(S^2)$ 的计算）。** 作为环，
> $$
> K^0(S^2)\cong\mathbb{Z}[H]/\big((H-1)^2\big),\qquad \tilde K^0(S^2)\cong\mathbb{Z}\ \text{由 }(H-1)\text{ 生成}.
> $$

*证明梗概（完整论证经 Bott 见 §s5）。* 关系 $(H-1)^2=0$ 表明由 $H$ 生成的子环是 $\mathbb{Z}[H]/((H-1)^2)$，在 $\mathbb{Z}$ 上自由、秩为 $2$，以 $\{1,H-1\}$ 为基。这些就是 $K^0(S^2)$ 的*全部*——即 $\tilde K^0(S^2)=\mathbb{Z}\langle H-1\rangle$ 而不更大——这恰是 Bott 周期性的秩为 $2$ 的陈述（§s5），我们在那里证明它。约化生成元 $\beta:=H-1$ 是 **Bott 类**；乘以 $\beta$ 实现周期性同构。$\square$

**与上同调的自洽性检验。** $H^*(S^2;\mathbb{Z})=\mathbb{Z}$ 在次数 $0$ 和 $2$ 处，总秩 $2$——与 $\mathrm{rank}_\mathbb{Z}K^0(S^2)=2$ 相符。Chern 特征标（§s7）将在与 $\mathbb{Q}$ 张量化后使这一相符成为同构，把 $H-1$ 送到 $H^2(S^2;\mathbb{Q})$ 的生成元。

**例 4 —— $S^2$ 上的每个丛，不只是线丛。** $S^2$ 上更高秩的丛由 $\mathrm{Vect}_n(S^2)=\pi_1(GL_n(\mathbb{C}))=\mathbb{Z}$ 对每个 $n\ge1$ 分类，那个整数仍由黏合函数行列式的缠绕读出（行列式映射 $GL_n(\mathbb{C})\to\mathbb{C}^\times$ 在 $\pi_1$ 上诱导同构，因为 $SL_n(\mathbb{C})$ 单连通）。故 $S^2$ 上一个秩为 $n$ 的丛 $E$ 至多在同构意义下由 $(n,c_1)$ 决定，其中 $c_1\in\mathbb{Z}$，且 $E\cong H^{\otimes c_1}\oplus\underline{\mathbb{C}}^{n-1}$。这是**稳定范围**的一个干净例证：一旦秩超过维数的一半，丛就分裂出平凡直和项，只有“稳定”数据 $(n,c_1)$——恰好是 $K^0$ 所记录的——保留下来。这就是为什么 $K^0(S^2)=\mathbb{Z}\{1\}\oplus\mathbb{Z}\{H-1\}$ 捕捉了*全部*的丛，而非一个近似。

**例 5 —— $K^0(S^1)$ 与 $GL$ 连通性的作用。** 对圆周，黏合用到 $\pi_0(GL_n(\mathbb{C}))$：$S^1=D^1\cup_{S^0}D^1$ 上的一个丛沿两个点由 $GL_n(\mathbb{C})$ 的一个元素黏合，而这种黏合的同伦类是 $\pi_0(GL_n(\mathbb{C}))=\{*\}$，因为 $GL_n(\mathbb{C})$ 道路连通。因此 $S^1$ 上的每个丛都平凡，$\tilde K^0(S^1)=0$，$K^0(S^1)=\mathbb{Z}$。（对照实情形：$GL_n(\mathbb{R})$ 有两个连通分支，故 $S^1$ 上的实线丛构成 $\mathbb{Z}/2$——Möbius 带是非平凡的那个。这是 $KO$ 不同于 $K$ 的第一个暗示。）

---

## 第 B 部分 · 作为上同调理论的 K 理论

<a id="s4"></a>
### 经悬挂得到的高阶 K 群 $K^{-n}(X)$；相对 K 理论

普通上同调在每个次数都有群 $H^n$。迄今我们只有 $K^0$。我们用**悬挂**制造出高阶（负次数）群，恰如人们用取环路定义高阶同伦群那样。

> **定义 —— 约化悬挂与基点。** 对带基点 $x_0$ 的空间 $X$，**约化悬挂**为 $\Sigma X=(X\times[0,1])/\big(X\times\{0\}\cup X\times\{1\}\cup\{x_0\}\times[0,1]\big)$——把顶、底以及基点线坍缩成单个点。于是 $\Sigma S^n=S^{n+1}$。此处所有空间都是**带基点**的紧 Hausdorff 空间，映射保持基点。

> **定义 —— 负 K 群。** 对 $n\ge 0$，
> $$
> \tilde K^{-n}(X):=\tilde K^0(\Sigma^n X),\qquad K^{-n}(X):=\tilde K^{-n}(X_+),
> $$
> 其中 $\Sigma^n$ 是 $n$ 重约化悬挂，$X_+=X\sqcup\{*\}$ 是给 $X$ 添加一个不相交基点（这个技巧使无基点/相对的公式可以统一地表述；注意 $\tilde K^0(X_+)=K^0(X)$）。

这之所以是*正确*的定义，是因为对普通约化上同调有**悬挂同构** $\tilde H^{n}(X)\cong\tilde H^{n+1}(\Sigma X)$；定义 $\tilde K^{-n}(X)=\tilde K^0(\Sigma^n X)$ 是把这种悬挂行为人为地内建进 K 理论，故所得的分次对象将自动满足悬挂公理（§s6）。

> **定义 —— 相对 K 理论。** 对紧对 $(X,A)$（$A\subseteq X$ 闭），定义**商** $X/A$（把 $A$ 坍缩成一点，即基点），并置
> $$
> K^0(X,A):=\tilde K^0(X/A),\qquad K^{-n}(X,A):=\tilde K^{-n}(X/A)=\tilde K^0(\Sigma^n(X/A)).
> $$
> 当 $A=\varnothing$ 时，$X/\varnothing=X_+$，我们恢复 $K^{-n}(X)$。相对类是 $X$ 上在 $A$ 上被平凡化的虚丛，模去尊重该平凡化的等价关系。

> **相对类的具体模型（差丛）。** $K^0(X,A)$ 的一个元素由三元组 $(E,F,\alpha)$ 表示，其中 $E,F$ 是 $X$ 上的丛，连同 $A$ 上的一个同构 $\alpha:E|_A\cong F|_A$；该类是“$[E]-[F]$ 配以 $A$ 上选定的平凡化”。两个三元组等价，若它们在稳定化和 $\alpha$ 的同伦后一致。这是指标定理（§s10）中所用的实用描述。

**例题 —— $K^0(D^2,S^1)$。** 圆盘 $D^2$ 可缩且 $D^2/S^1\cong S^2$，故 $K^0(D^2,S^1)=\tilde K^0(S^2)=\mathbb{Z}$。在差丛图景中，一个生成元是三元组 $(\underline{\mathbb{C}},\underline{\mathbb{C}},\alpha)$，其中 $\alpha:S^1\to GL_1(\mathbb{C})=\mathbb{C}^\times$ 是缠绕数为 $1$ 的恒等映射 $z\mapsto z$：圆盘上两个平凡线丛沿边界由一个一次扭转黏合。坍缩 $S^1$ 后这恰是 Hopf 丛的黏合数据，恢复了 Bott 生成元。$\alpha$ 的缠绕数是那个整数不变量——椭圆算子“符号类”（§s10）的雏形版本，后者恰是切空间上、在零截面之外被平凡化的这样一个差丛。

**例题 —— $K^{-n}(\mathrm{pt})$。** 此处 $X=\mathrm{pt}$，故 $\Sigma^n(\mathrm{pt}_+)=\Sigma^n S^0=S^n$。于是
$$
K^{-n}(\mathrm{pt})=\tilde K^0(S^n).
$$
我们已求得 $\tilde K^0(S^0)=\mathbb{Z}$（两个点：$K^0(S^0)=\mathbb{Z}\oplus\mathbb{Z}$，而约化部分——限制到基点的核——是剩下的那个 $\mathbb{Z}$；见下文）以及 $\tilde K^0(S^2)=\mathbb{Z}$。完整模式 $\tilde K^0(S^n)=\mathbb{Z}$（$n$ 偶）、$0$（$n$ 奇）正是 Bott 周期性的内容，我们现在转向它。具体地它给出
$$
K^{-n}(\mathrm{pt})=\begin{cases}\mathbb{Z}&n\text{ 偶}\\ 0&n\text{ 奇.}\end{cases}
$$

（$\tilde K^0(S^0)$ 的仔细取值：两个点上的丛是一对向量空间；$S^0$ 的约化 K 理论，以其中一点为基点，是 $\mathbb{Z}$——即非基点上丛的秩。悬挂一次，$\tilde K^0(S^1)=\pi_0(GL(\mathbb{C}))=0$，因为 $GL_n(\mathbb{C})$ 连通。这两者锚定了周期性。）

<a id="s5"></a>
### Bott 周期性（陈述，附证明思路）及其推论

K 理论的根本奇迹。

> **定理（Bott 周期性，复情形）。** 对每个紧的带基点空间 $X$，存在一个自然同构
> $$
> \beta:\tilde K^0(X)\xrightarrow{\ \cong\ }\tilde K^0(\Sigma^2 X)=\tilde K^{-2}(X),
> $$
> 由乘以 **Bott 类** $b\in\tilde K^0(S^2)$，$b=[H]-1$，给出。等价地对所有 $n$ 有 $\tilde K^{-n}(X)\cong\tilde K^{-n-2}(X)$，特别地
> $$
> \tilde K^0(S^n)=\begin{cases}\mathbb{Z}&n\text{ 偶}\\0&n\text{ 奇.}\end{cases}
> $$

这里“乘以 $b$”指**外积** $\tilde K^0(X)\otimes\tilde K^0(S^2)\to\tilde K^0(X\wedge S^2)=\tilde K^0(\Sigma^2 X)$，其中 $X\wedge S^2=\Sigma^2 X$ 是**碎积**（两根轴都被坍缩的乘积）。外积 $[E]\cdot[F]=[E\boxtimes F]$ 用到 $X\times Y$ 上纤维为 $E_x\otimes F_y$ 的丛 $E\boxtimes F$。

**证明的思路。** 有若干证明；概念上最干净的是 Atiyah 的，经由**黏合以及 $\Sigma^2 X = $ 双重悬挂上丛的结构**，把问题归结为用 $X$ 上的丛来理解 $X\times S^2$ 上的丛。

1. 由黏合（§s3），$X\times S^2$ 上在 $X\times D_\pm$ 上平凡化的丛由黏合函数 $X\times S^1\to GL(E_X)$ 给出——即 $X$ 上某个丛的自同构的一条环路，亦即环路空间数据的一个元素。故 $\tilde K^0(\Sigma^2 X)$ 受这种黏合函数的同伦类支配。
2. 技术核心是**线性化 / Laurent 多项式**论证：任何黏合函数（连续环路 $S^1\to GL$）都同伦于一条 **Laurent 多项式**环路 $\sum_{k=-N}^{N}A_k z^k$，再通过添加平凡直和项化为一条**线性**环路 $A+Bz$（一条“线性黏合函数”），最终化为形如 $z\mapsto z\cdot p+(1-p)$ 的环路，其中 $p$ 是一个*投影*。*（在环路变量中的 Stone–Weierstrass 逼近；稳定化吸收多项式次数。）*
3. 这种投影值数据恰是 $X$ 上的一个向量丛（$p$ 的像）。这产生出乘以 $b$ 的显式逆，证明该映射是同构。*（投影 $p$ 定义一个子丛，恢复出 $\tilde K^0(X)$ 中的一个类。）*

关键的分析输入仅是 Stone–Weierstrass 定理（三角多项式在连续环路中稠密），加上一项记账：稳定化（添加平凡丛）让我们用线性环路换取高次环路。不需要任何示性类机器；周期性归根结底是关于 $GL(\mathbb{C})$ 与 Laurent 多项式的陈述。

**梗概 —— 降次技巧的思路。** 第 2 步的核心在于：一条单项式型的黏合环路可以降一次，代价是把丛扩大一个平凡直和项。具体地，对 $S^1$ 上的环路 $z\mapsto z\cdot\mathrm{id}_{\mathbb{C}^n}$：

1. 构造秩为 $2n$ 的环路 $z\mapsto\begin{pmatrix}z\,\mathrm{id}&0\\0&\mathrm{id}\end{pmatrix}$，即原环路 $\oplus$ 一条平凡（次数 $0$）环路。*（直和对应添加一个平凡丛）*
2. 在 $GL_{2n}(\mathbb{C})$ 内用对角块为恒等、左下块为 $(1-z)\,\mathrm{id}$ 的初等环路（及其伙伴）作共轭/同伦；一个简短的矩阵计算把环路改写为 $z\mapsto z\,p+(1-p)$，其中投影 $p=\mathrm{diag}(\mathrm{id}_n,0)$，再加上一个同伦于恒等的常值可逆因子。*（行变换是 $GL$ 中的道路；$GL_{2n}(\mathbb{C})$ 道路连通，故常值可逆因子可忽略）*
3. 投影 $p$ 现在是*常值*的，但在 $X$ 上的族版本中它变成依赖 $X$ 的投影 $p(x)$，其像是一个子丛 $\mathrm{im}\,p\subseteq\underline{\mathbb{C}}^{2n}$——$X$ 上一个真正的向量丛，即 $\tilde K^0(X)$ 中的输出类。*（一族连续的投影定义一个子丛）*

这就是 $\times b$ 的显式逆：从一条环路（$\tilde K^0(\Sigma^2 X)$ 中的一个类）它制造出一个投影，从而得到 $X$ 上的一个丛。验证它是乘以 Bott 类的双侧逆即完成证明；所用唯一非平凡的分析事实是 Laurent 多项式的稠密性，其余皆为投影的线性代数。$\square$

**推论。**

- **只有两个群。** 双分次理论坍缩：$\tilde K^{-n}$ 只依赖于 $n\bmod 2$。定义 $\tilde K^{-1}(X):=\tilde K^0(\Sigma X)$，并通过 $\tilde K^{n}:=\tilde K^{n\bmod 2}$ 扩展到所有整数 $n$，使 K 理论成为一个 **$\mathbb{Z}/2$ 分次**（$2$ 周期）的上同调理论。
- **$K^0(S^2)$ 得到确认。** $\tilde K^0(S^2)=\tilde K^0(\Sigma^2 S^0)\cong\tilde K^0(S^0)=\mathbb{Z}$，由 $b=H-1$ 生成，严谨地完成了 §s3 的计算。
- **理论的系数。** $K^{-n}(\mathrm{pt})=\mathbb{Z}$（$n$ 偶）、$0$（$n$ 奇）：K 理论在每个偶次数都是 $\mathbb{Z}$。分次环 $K^*(\mathrm{pt})=\mathbb{Z}[b,b^{-1}]$，其中 $b$ 处于次数 $-2$，是**系数环**；反转 $b$ 是周期性的代数影子。

> **陷阱。** 周期性对*复* K 理论是周期 $2$；*实*理论 $KO$ 是周期 $8$（§s9）。混淆二者是最常见的错误。周期 $2$ 的陈述还需要复 Bott 类 $b\in\tilde K^0(S^2)$；类比的实生成元居于 $\tilde{KO}^0(S^8)$。

**例题 —— 对所有 $n$ 的 $K^*(S^n)$。** 结合定义 $\tilde K^{-i}(S^n)=\tilde K^0(\Sigma^i S^n)=\tilde K^0(S^{n+i})$ 与 Bott：
$$
\tilde K^0(S^n)=\begin{cases}\mathbb{Z}&n\text{ 偶}\\0&n\text{ 奇,}\end{cases}\qquad
\tilde K^1(S^n)=\tilde K^0(S^{n+1})=\begin{cases}0&n\text{ 偶}\\\mathbb{Z}&n\text{ 奇.}\end{cases}
$$
故奇维球面只在次数 $1$ 携带 K 理论，偶维球面只在次数 $0$ 携带——K 理论集中在与维数奇偶相反之处。非约化情形：$K^0(S^{2k})=\mathbb{Z}^2$，$K^1(S^{2k})=0$；$K^0(S^{2k+1})=\mathbb{Z}$，$K^1(S^{2k+1})=\mathbb{Z}$。对比普通上同调，它把 $\mathbb{Z}$ 铺展在次数 $0$ 和 $n$ 上；K 理论把同样的总秩挤进单一奇偶性中，这是 $2$ 周期理论的标志。

**例题 —— $K^0(\mathbb{CP}^n)$。** 设 $L$ 为复射影空间 $\mathbb{CP}^n$ 上的重言线丛（在直线 $\ell$ 上的纤维是 $\ell$）。置 $x=[L]-1\in\tilde K^0(\mathbb{CP}^n)$。其定义关系推广了 $S^2=\mathbb{CP}^1$ 的计算：$L$ 满足 $(L-1)^{n+1}=0$，因为 $\mathbb{CP}^n$ 上的 Koszul/Euler 序列关系杀掉第 $(n+1)$ 次幂。因此
$$
K^0(\mathbb{CP}^n)\cong\mathbb{Z}[x]/(x^{n+1}),
$$
一个秩为 $n+1$ 的自由 $\mathbb{Z}$ 模，以 $1,x,\dots,x^n$ 为基，且 $K^1(\mathbb{CP}^n)=0$。这与 $\sum_k\mathrm{rank}\,H^{2k}(\mathbb{CP}^n)=n+1$ 相符，Chern 特征标将证实这一点（§s7）。截断多项式环是上同调环 $H^*(\mathbb{CP}^n)=\mathbb{Z}[t]/(t^{n+1})$ 的 K 理论影子，其中 $x\leftrightarrow$ 一个单位乘以 $t$ 再加上高阶修正。

<a id="s6"></a>
### 长正合列；作为广义上同调理论的 K 理论

我们现在验证 $\{\tilde K^{-n}\}$ 服从 Eilenberg–Steenrod 公理减去维数公理——即（约化）**广义上同调理论**的定义。

> **定义 —— 约化广义上同调理论。** 一列从带基点紧空间到阿贝尔群的逆变同伦函子 $\tilde h^n$（$n\in\mathbb{Z}$），带有自然的**悬挂同构** $\sigma:\tilde h^n(X)\cong\tilde h^{n+1}(\Sigma X)$，使得对每个带基点的对（上纤维化 $A\hookrightarrow X$），序列
> $$
> \tilde h^n(X/A)\to\tilde h^n(X)\to\tilde h^n(A)
> $$
> 正合，且满足**楔公理** $\tilde h^n(\bigvee_\alpha X_\alpha)\cong\prod_\alpha\tilde h^n(X_\alpha)$。舍弃*维数公理*（对 $n\ne 0$ 有 $\tilde h^n(S^0)=0$）正是使它“广义”之所在。

**对的正合列。** 基础的正合性是对 $K^0$ 与一个上纤维化而言的。

> **命题（正合性）。** 对紧对 $(X,A)$，含入 $i:A\hookrightarrow X$ 与坍缩 $q:X\to X/A$ 给出正合列
> $$
> \tilde K^0(X/A)\xrightarrow{q^*}\tilde K^0(X)\xrightarrow{i^*}\tilde K^0(A).
> $$

**演示（在 $\tilde K^0(X)$ 处的正合性）。**

1. **$i^*q^*=0$。** 复合 $A\xrightarrow{i}X\xrightarrow{q}X/A$ 把 $A$ 送到基点，故它零伦；因此在约化 K 理论上 $i^*q^*=(q i)^*=0$。*（同伦不变性；点的约化 K 理论为 $0$）*
2. **$\ker i^*\subseteq\mathrm{im}\,q^*$。** 取 $[E]-[\underline{\mathbb{C}}^n]\in\ker i^*$，故 $E|_A\oplus\underline{\mathbb{C}}^k\cong\underline{\mathbb{C}}^{n+k}|_A$——即 $E$（稳定化后）经某个同构 $\alpha$ *在 $A$ 上平凡*。$A$ 上的一个平凡化让我们能坍缩 $A$：丛 $E\oplus\underline{\mathbb{C}}^k$ 下降为 $X/A$ 上的一个丛 $\bar E$（用 $\alpha$ 把 $A$ 上平凡化后的纤维黏到基点上那单根纤维），且 $q^*\bar E\cong E\oplus\underline{\mathbb{C}}^k$。于是 $[E]-[\underline{\mathbb{C}}^n]=q^*([\bar E]-[\underline{\mathbb{C}}^{n+k}])$。*（在 $A$ 上被平凡化的丛是从商拉回的——§s4 的差丛描述）*
3. 第 1–2 步给出 $\mathrm{im}\,q^*=\ker i^*$，即正合性。$\square$

**扩展为长正合列。** 经 **Puppe/上纤维序列** $A\to X\to X/A\to\Sigma A\to\Sigma X\to\cdots$ 拼接进悬挂，并对每一项施加 $\tilde K^0$，配合等同 $\tilde K^0(\Sigma^k Y)=\tilde K^{-k}(Y)$，得到**对的长正合列**：
$$
\cdots\to K^{-1}(A)\xrightarrow{\partial}K^0(X,A)\to K^0(X)\to K^0(A)\xrightarrow{\partial}K^1(X,A)\to\cdots
$$
由 Bott 周期性（$K^{-2}\cong K^0$，$K^{-1}\cong K^1$），它卷成一个**六项循环正合列**：
$$
\begin{array}{ccccc}
K^0(X,A)&\to&K^0(X)&\to&K^0(A)\\
\uparrow&&&&\downarrow\\
K^1(A)&\leftarrow&K^1(X)&\leftarrow&K^1(X,A)
\end{array}
$$
这个六项序列——在普通 $\mathbb{Z}$ 分次上同调中不可能出现——是 K 理论的计算主力，也是它在算子代数中出现的形态（§s10）。

> **公理的验证（小结）。**
> *函子性 + 同伦不变性：* §s1–s2。*悬挂同构：* 内建于定义 $\tilde K^{-n}(X)=\tilde K^0(\Sigma^n X)$。*正合性：* 上述命题，再用 Puppe 拼接。*楔公理：* 楔 $\bigvee X_\alpha$ 上的丛相容地限制到每个直和项，反之也可黏合，给出 $\tilde K^0(\bigvee X_\alpha)\cong\prod\tilde K^0(X_\alpha)$。除维数公理外所有 Eilenberg–Steenrod 公理都成立，而维数公理失效恰恰是因为 $K^{-2n}(\mathrm{pt})=\mathbb{Z}\ne 0$。

**例题 —— 由六项序列得到 Mayer–Vietoris。** 对 $X=U\cup V$（闭、良态），相对序列组合成
$$
\cdots\to K^0(X)\to K^0(U)\oplus K^0(V)\to K^0(U\cap V)\xrightarrow{\partial}K^1(X)\to\cdots,
$$
它重新算出 $K^0(S^2)=\mathbb{Z}^2$：取 $U,V$ 为两个半球（各可缩，$K^0=\mathbb{Z}$），$U\cap V\simeq S^1$（$\tilde K^0(S^1)=0$，$K^1(S^1)=\mathbb{Z}$）。序列迫使 $\tilde K^0(S^2)\cong\tilde K^1(S^1)\cong K^{-1}(\mathrm{pt})$-移位 $=\mathbb{Z}$，与 Bott 一致。

**例题 —— 由六项序列逐步算出 $K^*(S^1)$。** 把 $S^1=U\cup V$ 写成两段重叠的弧，各可缩，$U\cap V\simeq\{2\text{ 个点}\}=S^0$。K 理论中的约化 Mayer–Vietoris 为
$$
\cdots\to\tilde K^0(S^1)\to\tilde K^0(U)\oplus\tilde K^0(V)\to\tilde K^0(S^0)\xrightarrow{\partial}\tilde K^1(S^1)\to\tilde K^1(U)\oplus\tilde K^1(V)\to\cdots
$$
现在 $\tilde K^*(U)=\tilde K^*(V)=0$（可缩）。序列坍缩为 $0\to\tilde K^0(S^1)\to0$ 与 $0\to\tilde K^0(S^0)\xrightarrow{\partial}\tilde K^1(S^1)\to0$。第一个给出 $\tilde K^0(S^1)=0$。第二个给出 $\tilde K^1(S^1)\cong\tilde K^0(S^0)=\mathbb{Z}$。故 $K^0(S^1)=\mathbb{Z}$，$K^1(S^1)=\mathbb{Z}$——每一步都由正合性以及约化 K 理论在可缩片段上的消失所证成，无需诉诸 Bott。这里的连接映射 $\partial$ 是 $K^1(S^1)$ 次数 $1$ 生成元的几何起源：重叠上的单位 $z\mapsto z$，正是构造 Möbius/Hopf 黏合数据的那个缠绕。

---

## 第 C 部分 · 通往上同调与指标理论的桥梁

<a id="s7"></a>
### Chern 特征标与有理同构

K 理论与普通上同调在整数意义上是不同的（K 理论 $2$ 周期；$H^*$ 不是），然而在与 $\mathbb{Q}$ 张量化后它们变得*相同*。比较映射是 **Chern 特征标**，由 Chern 类构造。

> **回顾（来自微分拓扑）。** $X$ 上的复向量丛 $E$ 有 **Chern 类** $c_i(E)\in H^{2i}(X;\mathbb{Z})$，总类为 $c(E)=1+c_1(E)+c_2(E)+\cdots$，满足 **Whitney 和公式** $c(E\oplus F)=c(E)\,c(F)$（杯积）与自然性 $c(f^*E)=f^*c(E)$。对线丛 $L$，$c(L)=1+c_1(L)$。

Chern 特征标是唯一既加性*又*乘性的环映射 $K^0\to H^{\mathrm{even}}(\,\cdot\,;\mathbb{Q})$；定义它的技巧是**分裂原理**加上 Chern 根的指数。

> **定义 —— Chern 特征标。** 设（分裂原理）$E$ 形式地分裂为线丛之和，$c(E)=\prod_{j=1}^n(1+x_j)$，其中 **Chern 根** $x_j\in H^2$ 是形式的；$x_j$ 的第 $i$ 个初等对称多项式是 $c_i(E)$。定义
> $$
> \mathrm{ch}(E)=\sum_{j=1}^n e^{x_j}=\sum_{j=1}^n\Big(1+x_j+\tfrac{x_j^2}{2!}+\cdots\Big)\in H^{\mathrm{even}}(X;\mathbb{Q}).
> $$
> 由于 $\sum_j e^{x_j}$ 在 $x_j$ 中对称，它是 $c_i(E)$ 的多项式，故 $\mathrm{ch}(E)$ 良定义，不依赖于形式分裂。低阶项：
> $$
> \mathrm{ch}(E)=\mathrm{rk}(E)+c_1(E)+\tfrac12\big(c_1(E)^2-2c_2(E)\big)+\cdots
> $$

**演示 —— $\mathrm{ch}$ 低阶项的推导。** 展开 $\sum_j e^{x_j}=\sum_j(1+x_j+\tfrac{x_j^2}{2}+\cdots)$，并用初等对称多项式 $e_k=c_k$ 按上同调次数归集（Newton 恒等式把幂和 $p_k=\sum_j x_j^k$ 与 $e_k$ 联系起来）：

1. **次数 $0$：** $\sum_j 1=n=\mathrm{rk}(E)$。*（有 $n$ 个 Chern 根）*
2. **次数 $2$：** $\sum_j x_j=p_1=e_1=c_1(E)$。*（Newton：$p_1=e_1$）*
3. **次数 $4$：** $\tfrac12\sum_j x_j^2=\tfrac12 p_2$。Newton 恒等式 $p_2=e_1^2-2e_2$ 给出 $\tfrac12 p_2=\tfrac12(c_1^2-2c_2)=\tfrac12 c_1^2-c_2$。*（Newton：$p_2=e_1^2-2e_2$）*

故 $\mathrm{ch}(E)=n+c_1+(\tfrac12 c_1^2-c_2)+\cdots$，即上面所引的公式，现已是推导而非断言。半整数系数 $\tfrac12$ 是 Chern 特征标不保持整数格、仅在 $\otimes\mathbb{Q}$ 之后才成为同构的结构性原因。

> **定理（Chern 特征标是环同态）。** $\mathrm{ch}:K^0(X)\to H^{\mathrm{even}}(X;\mathbb{Q})$ 是一个良定义的环同态：$\mathrm{ch}(E\oplus F)=\mathrm{ch}(E)+\mathrm{ch}(F)$ 且 $\mathrm{ch}(E\otimes F)=\mathrm{ch}(E)\,\mathrm{ch}(F)$。

**加性与乘性的演示。**

1. **加性。** $E\oplus F$ 的 Chern 根是 $E$ 与 $F$ 的 Chern 根之并（Whitney 公式 $c(E\oplus F)=c(E)c(F)$ 把因子 $\prod(1+x_j)$ 相乘）。因此 $\mathrm{ch}(E\oplus F)=\sum_{j}e^{x_j}+\sum_k e^{y_k}=\mathrm{ch}(E)+\mathrm{ch}(F)$。由于 $\mathrm{ch}$ 对 $\oplus$ 加性，它经 $\mathrm{ch}([E]-[F])=\mathrm{ch}(E)-\mathrm{ch}(F)$ 扩展为 Grothendieck 群 $K^0$ 上的同态。*（$\mathcal G$ 的泛性质，§s2）*
2. **乘性。** 一个线丛有 Chern 根 $x_j$；线丛之张量 $L\otimes M$ 的第一 Chern 类是 $c_1(L)+c_1(M)$（线丛的 Chern 类在 $\otimes$ 下相加），故其 Chern 根是 $x_j+y_k$。于是 $E\otimes F$ 的 Chern 根是所有和 $x_j+y_k$，且
> $$
> \mathrm{ch}(E\otimes F)=\sum_{j,k}e^{x_j+y_k}=\Big(\sum_j e^{x_j}\Big)\Big(\sum_k e^{y_k}\Big)=\mathrm{ch}(E)\,\mathrm{ch}(F),
> $$
> 用到 $e^{a+b}=e^ae^b$。*（指数律；$\otimes$ 对 $\oplus$ 的双线性性）* $\square$

> **定理（有理同构 / Chern 特征标同构）。** 对有限 CW 复形 $X$，Chern 特征标诱导出 $\mathbb{Z}/2$ 分次环的同构
> $$
> \mathrm{ch}:K^*(X)\otimes_{\mathbb{Z}}\mathbb{Q}\ \xrightarrow{\ \cong\ }\ H^{\mathrm{even}}(X;\mathbb{Q})\oplus H^{\mathrm{odd}}(X;\mathbb{Q})=H^*(X;\mathbb{Q}),
> $$
> 其中 $K^0\otimes\mathbb{Q}\cong H^{\mathrm{even}}$ 且 $K^1\otimes\mathbb{Q}\cong H^{\mathrm{odd}}$。

*证明思路。* 两边都是广义上同调理论（右边经 $H^{\mathrm{even/odd}}$ 用 $\mathbb{Q}$ 系数做成 $2$ 周期），$\mathrm{ch}$ 是它们之间的自然变换，且它在点上是同构（$K^0(\mathrm{pt})\otimes\mathbb{Q}=\mathbb{Q}=H^0(\mathrm{pt};\mathbb{Q})$，所有更高项为 $0$）。上同调理论间在点上为同构的自然变换，在所有有限复形上都是同构——这是**比较定理**，用五引理和长正合列对胞腔作归纳证明。$\square$

**例题 —— $S^2$。** $\mathrm{ch}(H-1)=\mathrm{ch}(H)-1=e^{c_1(H)}-1=c_1(H)+\tfrac12 c_1(H)^2+\cdots$。在 $S^2$ 上，$c_1(H)$ 生成 $H^2(S^2;\mathbb{Z})=\mathbb{Z}$，而 $c_1(H)^2\in H^4(S^2)=0$。故 $\mathrm{ch}(H-1)=c_1(H)$，即 $H^2$ 的生成元。于是 $\mathrm{ch}$ 把 $\tilde K^0(S^2)=\mathbb{Z}$ 的 Bott 生成元 $H-1$ 送到 $H^2(S^2;\mathbb{Z})$ 的生成元，此处甚至在 $\mathbb{Z}$ 上已是同构。整数格一般是不同的（例如在 $\mathbb{CP}^n$ 上 $\mathrm{ch}$ 的像并非整个 $H^{\mathrm{even}}(\mathbb{Z})$），这正是干净陈述需要 $\otimes\mathbb{Q}$ 的原因。

**例题 —— $\mathbb{CP}^2$ 上的 $\mathrm{ch}$，带实数。** 设 $t=c_1(L^{-1})\in H^2(\mathbb{CP}^2;\mathbb{Z})$ 为标准生成元，故 $H^*(\mathbb{CP}^2)=\mathbb{Z}[t]/(t^3)$，其中 $t,t^2$ 生成 $H^2,H^4$。对偶线丛的 Chern 根是 $-t$……改取 $L^*$，满足 $c_1(L^*)=t$。则
$$
\mathrm{ch}(L^*)=e^{t}=1+t+\tfrac{t^2}{2},\qquad \mathrm{ch}((L^*)^{\otimes 2})=e^{2t}=1+2t+2t^2,
$$
因为 $t^3=0$。作为乘性的检验，$\mathrm{ch}(L^*)^2=(1+t+\tfrac{t^2}{2})^2=1+2t+(1+1)t^2+\cdots=1+2t+2t^2$（舍去 $t^3,t^4$），与 $\mathrm{ch}((L^*)^2)$ 相符。$K^0(\mathbb{CP}^2)$ 的基 $\{1,\ L^*-1,\ (L^*-1)^2\}$ 在 $\mathrm{ch}$ 下映到 $\{1,\ t+\tfrac{t^2}{2},\ t^2\}$（计算 $(L^*-1)^2$：$\mathrm{ch}=(t+\tfrac{t^2}2)^2=t^2$），它是 $H^{\mathrm{even}}(\mathbb{CP}^2;\mathbb{Q})=\mathbb{Q}\{1,t,t^2\}$ 的一组 $\mathbb{Q}$ 基——通过在基元上展示该同构来证实有理同构。注意像 $\{1, t+\tfrac{t^2}2, t^2\}$ *不是*整数格 $\{1,t,t^2\}$（中间那个向量有半整数的 $t^2$ 系数），这是 $\mathrm{ch}$ 仅在 $\otimes\mathbb{Q}$ 后才是同构的具体原因。

> **陷阱。** $\mathrm{ch}$ 仅在 $\otimes\mathbb{Q}$ 后才是同构。在整数意义上，K 理论比 $H^*$ 携带*更多*信息：挠现象与整数格是真正不同的，这恰恰是为什么 K 理论能探测到上同调遗漏的东西（如某些 D 膜荷，§s11）。

<a id="s8"></a>
### Thom 同构、K 定向与前推

为在 K 理论中作*积分*——为定义沿流形映射的 Gysin 映射 / 前推，即微分形式积分在 K 理论中的类比——我们需要 K 理论的 Thom 同构以及 K 定向的概念。

> **定义 —— Thom 空间。** 对带 Hermite 度量的秩为 $n$ 的复向量丛 $\pi:V\to X$，**Thom 空间**为 $X^V:=D(V)/S(V)$，即把单位球面丛坍缩后的单位圆盘丛。对平凡丛 $X^{\underline{\mathbb{C}}^n}=\Sigma^{2n}(X_+)$。

> **定理（K 理论中的 Thom 同构）。** 设 $V\to X$ 为秩 $n$ 的复向量丛。存在一个 **Thom 类** $\lambda_V\in\tilde K^0(X^V)$，使得乘以它是一个同构
> $$
> \Phi:K^0(X)\xrightarrow{\ \cong\ }\tilde K^0(X^V),\qquad \Phi(a)=\pi^*a\cdot\lambda_V.
> $$

**Thom 类的构造（K 理论的 Koszul/外类）。** 在 $V$ 的全空间上，构造**外代数复形**
$$
0\to\Lambda^0 V\xrightarrow{\,\wedge v\,}\Lambda^1 V\xrightarrow{\,\wedge v\,}\Lambda^2 V\to\cdots\to\Lambda^n V\to 0,
$$
其中在点 $v\in V_x$ 处映射是与向量 $v$ 的外乘。在零截面之外（$v\ne 0$）该复形是**正合**的（非零向量的 Koszul 复形是无圈的——与 $v/|v|^2$ 缩并得到一个到零的链同伦）。一个在某紧集之外正合的丛复形（此处是在圆盘内部之外，在限制到 $D(V)$ 并注意到在 $S(V)$ 上正合之后）定义一个支撑在 $X^V$ 上的差类：
$$
\lambda_V=\Big[\textstyle\sum_{i\ \mathrm{even}}\Lambda^i V\Big]-\Big[\textstyle\sum_{i\ \mathrm{odd}}\Lambda^i V\Big]\in\tilde K^0(X^V),
$$
即交错和 $\sum_i(-1)^i[\Lambda^i V]$，经 Koszul 同伦在 $S(V)$ 上被平凡化（§s4 的差丛描述）。$\Phi$ 是同构，经黏合与 Bott 周期性，归结为 $V=\underline{\mathbb{C}}^n$ 的情形，那里 $\tilde K^0(\Sigma^{2n}X_+)=\tilde K^{-2n}(X_+)\cong K^0(X)$ 恰是周期性。$\square$

> **定义 —— K 定向；复丛是 K 可定向的。** 一个实向量丛（或经其稳定法/切丛得到的流形映射）称为 **K 可定向**，若其 Thom 空间携带一个使 $\Phi$ 成为同构的 Thom 类。上述构造表明**每个复向量丛都典范地 K 可定向**。更一般地，一个实丛 K 可定向当且仅当它容许一个 $\mathrm{Spin}^c$ 结构——可定向性的 K 理论加细。*（对普通上同调，可定向性 $\leftrightarrow$ $w_1=0$；K 可定向性 $\leftrightarrow$ $\mathrm{Spin}^c$，即 $W_3=0$。）*

> **定义 —— 前推（Gysin 映射）。** 设 $f:X\to Y$ 是闭流形间的光滑映射且 K 定向（例如带复法丛的嵌入，或 $\mathrm{Spin}^c$ 流形间的任何映射）。则存在一个**前推**（逆向 / Gysin 映射）
> $$
> f_!:K^*(X)\to K^{*+d}(Y),\qquad d=\dim Y-\dim X,
> $$
> 构造如下：(i) 把 $X\hookrightarrow Y\times\mathbb{R}^N$ 嵌入；(ii) 在管状邻域上施加 Thom 同构（其法丛 K 定向）；(iii) 用零延拓并借 Bott 周期性下降悬挂。它满足函子性 $(g\circ f)_!=g_!f_!$ 与**投影公式** $f_!(f^*b\cdot a)=b\cdot f_!(a)$。

**例题 —— 点上线丛的 Thom 类。** 取 $X=\mathrm{pt}$ 和 $V=\mathbb{C}$（点上秩为 $1$ 的丛）。Thom 空间为 $\mathrm{pt}^{\mathbb{C}}=D^2/S^1=S^2$。外代数复形为 $0\to\Lambda^0\mathbb{C}=\mathbb{C}\xrightarrow{\wedge v}\Lambda^1\mathbb{C}=\mathbb{C}\to0$，即乘以标量 $v$，对 $v\ne0$ 是同构。Thom 类是 $\lambda_V=[\Lambda^0]-[\Lambda^1]$，在 $0$ 之外平凡化，它在 $\tilde K^0(S^2)$ 中至多差一个符号恰是 $-(H-1)$——即 Bott 生成元。故 K 理论的 Thom 同构 $K^0(\mathrm{pt})=\mathbb{Z}\xrightarrow{\cong}\tilde K^0(S^2)=\mathbb{Z}$，$1\mapsto\lambda_V$，*就是*伪装的 Bott 周期性。这是看清“为何 $\underline{\mathbb{C}}^n$ 的 Thom 类生成 $\tilde K^0(S^{2n})$”以及“为何复丛之 K 可定向建立在同一周期性之上”的最干净方式。

**例题 —— 向点的前推与指标。** 对闭 $\mathrm{Spin}^c$ 流形 $X$ 与 $f:X\to\mathrm{pt}$，前推
$$
f_!:K^0(X)\to K^0(\mathrm{pt})=\mathbb{Z}
$$
是 **K 理论积分 / 拓扑指标**。Atiyah–Singer 指标定理（§s10）把 $f_!([E])$ 等同于一个扭化 Dirac 算子的解析指标，而 **Riemann–Roch–Grothendieck** 相容性
$$
\mathrm{ch}(f_!a)=f_*\big(\mathrm{ch}(a)\cdot\mathrm{Td}(X)\big)
$$
（其中 $f_*$ 是普通的上同调积分，$\mathrm{Td}$ 是 Todd 类）正是“K 理论前推与上同调积分在差一个 Todd 修正下一致”的精确陈述——即指标定理中 $\hat A$ 亏格与 Todd 亏格公式的来源。

---

## 第 D 部分 · 变体、分析与物理

<a id="s9"></a>
### Clifford 代数与实 K 理论（$KO$）；八重周期性

把复丛换成**实**向量丛得到**实 K 理论** $KO^*(X)$，即实丛在 $\oplus$ 下的 Grothendieck 群。其结构受 **Clifford 代数**支配，周期是 $8$ 而非 $2$。

> **定义 —— Clifford 代数。** 对带标准负定形式的 $\mathbb{R}^n$，**Clifford 代数** $\mathrm{Cl}_n$ 是由 $e_1,\dots,e_n$ 生成、服从 $e_ie_j+e_je_i=-2\delta_{ij}$ 的结合实代数。（故 $e_i^2=-1$ 且相异生成元反交换。）其表示论是 $8$ 周期的：$\mathrm{Cl}_{n+8}\cong\mathrm{Cl}_n\otimes\mathbb{R}(16)$（矩阵代数），此事实归因于实可除代数 $\mathbb{R},\mathbb{C},\mathbb{H}$。

> **定理（实 Bott 周期性）。** $\tilde{KO}^{-n}(\mathrm{pt})=\tilde{KO}^0(S^n)$ 关于 $n$ 是 $8$ 周期的，取值为
> $$
> \begin{array}{c|cccccccc}
> n\bmod 8 & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7\\\hline
> KO^{-n}(\mathrm{pt}) & \mathbb{Z} & \mathbb{Z}/2 & \mathbb{Z}/2 & 0 & \mathbb{Z} & 0 & 0 & 0
> \end{array}
> $$
> 且 $KO^{-n-8}(\mathrm{pt})\cong KO^{-n}(\mathrm{pt})$。

与 Clifford 代数的联系（Atiyah–Bott–Shapiro）：差 $KO^{-n}(\mathrm{pt})\cong M_n/i^*M_{n+1}$，其中 $M_n$ 是 $\mathrm{Cl}_n$ 模的 Grothendieck 群，$i^*$ 沿 $\mathrm{Cl}_n\hookrightarrow\mathrm{Cl}_{n+1}$ 作限制——Clifford 代数的表示论*计算*同伦群，而 Clifford 模的 $8$ 重周期性就是实 Bott 周期性。$\mathbb{Z}/2$ 出现在次数 $1,2$ 处，是真正的挠，任何有理不变量都看不见——这是带 $\mathbb{Q}$ 系数的普通上同调无法察觉的现象。

> **概览 —— 周期性时钟。** 复 K 理论：周期 $2$，系数 $\mathbb{Z},0,\mathbb{Z},0,\dots$（由 $\mathbb{C}$ 驱动，一步可除代数）。实 K 理论：周期 $8$，系数如上（由 $\mathbb{R}\to\mathbb{C}\to\mathbb{H}$ 塔驱动）。还有一个“四元数 / 辛”理论 $KSp$，以及把它们联系起来的复化 $KO^*\to K^*$ 与实化 $K^*\to KO^*$。这八重模式与自由费米子拓扑相的分类（§s11）中出现的是同一个——“十重道路”。

**例题 —— 小 Clifford 代数与表的开头。** 由 $e_ie_j+e_je_i=-2\delta_{ij}$ 计算前几个 $\mathrm{Cl}_n$：
$$
\mathrm{Cl}_0=\mathbb{R},\quad \mathrm{Cl}_1=\mathbb{C}\ (e_1^2=-1),\quad \mathrm{Cl}_2=\mathbb{H}\ (e_1,e_2,e_1e_2\text{ 表现得像 }i,j,k),\quad \mathrm{Cl}_3=\mathbb{H}\oplus\mathbb{H}.
$$
实可除代数 $\mathbb{R},\mathbb{C},\mathbb{H}$ 出现在前三步，八步之后到达一个 $16\times16$ 的实矩阵代数 $\mathrm{Cl}_8\cong\mathbb{R}(16)$，其模理论 Morita 等价于 $\mathbb{R}=\mathrm{Cl}_0$——这个 Morita 等价*就是*八重周期性。$\mathbb{Z}/2$ 项 $KO^{-1},KO^{-2}$ 追溯到 $\mathrm{Cl}_1=\mathbb{C}$ 与 $\mathrm{Cl}_2=\mathbb{H}$ 具有受限的模维数集合，从而在余核 $M_n/i^*M_{n+1}$ 中产生挠。

**例题 —— 具体地 $\tilde{KO}^0(S^1)=\mathbb{Z}/2$。** $S^1$ 上的实线丛由 $\pi_0(GL_1(\mathbb{R}))=\pi_0(\mathbb{R}^\times)=\{\pm\}=\mathbb{Z}/2$ 黏合：平凡柱面（$+$）与 Möbius 带（$-$）。在 $\tilde{KO}^0(S^1)$ 中 Möbius 类 $\mu$ 满足 $2\mu=0$，因为 $\mu\oplus\mu$（黏合 $\mathrm{diag}(-1,-1)\in GL_2(\mathbb{R})$，落在恒等连通分支中）是平凡的。这与表中条目 $KO^{-1}(\mathrm{pt})=\tilde{KO}^0(S^1)=\mathbb{Z}/2$ 相符——一个任何有理或复不变量都看不见的挠类，也是 $\mathbb{Z}_2$ 拓扑绝缘体不变量（§s11）的原型。

<a id="s10"></a>
### 算子/解析 K 理论与 K 同调；与指标理论的联系

K 理论有一个纯解析的化身，适用于（非交换）代数，与算子理论相统一。

> **定义 —— C\*-代数的 K 理论。** 对带单位的 C\*-代数 $A$（一个满足 $\|a^*a\|=\|a\|^2$ 的复 Banach $*$-代数，例如 $A=C(X)$，紧 $X$ 上的连续函数），把 $K_0(A)$ 定义为矩阵代数 $M_\infty(A)$ 中**投影** $p=p^*=p^2$ 在（Murray–von Neumann）等价与稳定化意义下的 Grothendieck 群，把 $K_1(A)$ 经 $M_\infty(A)$ 中酉元的同伦类定义。**Serre–Swan / Gelfand：** 对 $A=C(X)$，有限生成投射 $A$ 模对应于 $X$ 上的向量丛，给出
> $$
> K_0(C(X))\cong K^0(X),\qquad K_1(C(X))\cong K^1(X).
> $$
> 于是拓扑 K 理论是算子 K 理论的交换情形；后者把理论扩展到*非交换空间*。

六项正合列（§s6）在此对一个理想 $0\to I\to A\to A/I\to 0$ 出现，是算子代数中计算的基石。

**例题 —— Toeplitz 扩张与 Toeplitz 算子的指标。** 一个基础性的算子-K 计算：Toeplitz C\*-代数 $\mathcal T$（由 $\ell^2(\mathbb{N})$ 上的单边移位 $S$ 生成）位于一个短正合列中
$$
0\to\mathcal K\to\mathcal T\xrightarrow{\sigma}C(S^1)\to0,
$$
其中 $\mathcal K$ 是紧算子，$\sigma$ 是符号映射。带有 $K_0(\mathcal K)=\mathbb{Z}$、$K_1(\mathcal K)=0$、$K_0(C(S^1))=\mathbb{Z}$、$K_1(C(S^1))=\mathbb{Z}$ 的六项序列，其连接映射 $\partial:K_1(C(S^1))=\mathbb{Z}\to K_0(\mathcal K)=\mathbb{Z}$ 等于**缠绕数的相反数**：对可逆符号 $f:S^1\to\mathbb{C}^\times$，Toeplitz 算子 $T_f$ 是 Fredholm 的，且 $\mathrm{ind}(T_f)=-\mathrm{wind}(f)$。这是最简单的指标定理，并且它*由 K 理论的边界映射计算*——§s3 的缠绕数作为解析指标重现。它是 Atiyah–Singer 的 $1$ 维原型。

> **定义 —— K 同调。** 对偶理论 $K_*(X)$（**K 同调**）由 **Fredholm 模** / 抽象椭圆算子表示：一个类（粗略地）是一个带有 $C(X)$ 表示的 Hilbert 空间，连同一个几乎与该表示交换的自伴 Fredholm 算子 $F$。具体地，流形 $X$ 上的一个**椭圆微分算子** $D$（例如 Dirac 算子）定义一个 K 同调类 $[D]\in K_*(X)$。

> **定理（Atiyah–Singer 指标定理，K 理论形式）。** 对闭流形 $X$ 上的椭圆算子 $D$，**解析指标** $\mathrm{ind}(D)=\dim\ker D-\dim\mathrm{coker}\,D\in\mathbb{Z}$ 等于**拓扑指标**：符号类 $[\sigma_D]\in K^0(TX)$ 与基本类的配对，经前推到点来计算，
> $$
> \mathrm{ind}(D)=p_!\,[\sigma_D]\in K^0(\mathrm{pt})=\mathbb{Z}.
> $$
> 经 Chern 特征标与 Riemann–Roch 公式（§s8），这变为上同调指标公式 $\mathrm{ind}(D)=\int_X\mathrm{ch}(\sigma_D)\,\mathrm{Td}(TX\otimes\mathbb{C})$。

**例题 —— 环面上的指标定理与最简单的 Gauss–Bonnet 检验。** 对闭定向曲面 $\Sigma$ 上的 de Rham / Euler 算子 $D=d+d^*$，解析指标是 $\dim\ker-\dim\mathrm{coker}=\sum_k(-1)^k b_k=\chi(\Sigma)$，即 Euler 示性数。拓扑一侧计算 $\int_\Sigma e(T\Sigma)$，即 Euler 类的积分。在环面 $T^2$ 上，$\chi=0$，确实 $\int_{T^2}e=0$（环面可平行化，Euler 类为零）；在 $S^2$ 上，$\chi=2=\int_{S^2}e$。K 理论的陈述把 $d+d^*$ 的符号打包成 $K^0(T\Sigma)$ 中的一个类并把它推到 $\mathbb{Z}$，返回 $\chi$——以三种方式（代数拓扑的交错和、解析指标、曲率积分）得到同一个数，现在被看成单个 K 理论前推。这是指标定理特殊化到经典 Gauss–Bonnet 定理的情形，而 K 理论作为记账使得向*任何*椭圆算子的推广自动成立。

*为何 K 理论是自然的语言。* 指标是**稳定**的（添加可逆算子、形变 $D$、稳定化向量丛都不改变它）——恰是 K 理论所施加的等价关系。指标映射就是 §s8 的 K 理论前推 $p_!$；Bott 周期性使*非紧* $TX$ 上的符号类良定义、前推可计算。K 理论（丛/符号）与 K 同调（算子）之间的配对 $K^*(X)\times K_*(X)\to\mathbb{Z}$ *就是*指标，而指标定理说该配对的解析计算与拓扑计算相吻合。这是指标理论最现代、最灵活的陈述，也是通往 Baum–Connes 猜想与非交换几何的门户。

<a id="s11"></a>
### 物理 —— D 膜荷与物质拓扑相的 K 理论分类

K 理论不仅仅是数学家的组织原则；它是两个物理分类问题的正确归宿。

**弦论中的 D 膜荷（概览）。** 在 II 型弦论中，**D 膜**是开弦所终结其上的延展对象，在其世界体上携带一个规范场（一个 Chan–Paton 丛）。朴素地说，缠绕一个闭链的 D 膜携带普通上同调中的一个荷（该闭链的同调类配以规范丛的 Chern 特征标）。其加细，归功于 Minasian–Moore 与 Witten：

> **原理 —— D 膜荷居于 K 理论中。** 时空 $X$ 中一个 D 膜组态的守恒荷由 $K^0(X)$（IIB 型）或 $K^1(X)$（IIA 型）分类，而不仅仅由 $H^{\mathrm{even/odd}}(X;\mathbb{Z})$ 分类。

其物理原因精确地映射到 K 理论结构上：(i) **膜–反膜湮灭**恰是 Grothendieck 关系 $[E]-[E]=0$——带丛 $E$ 的膜与带丛 $E$ 的反膜相消，故只有虚差才要紧；(ii) **快子凝聚**在带快子场 $T:E\to F$ 的膜–反膜对 $(E,F)$ 上，经差丛/Koszul 构造，恰好产生支撑在 $T$ 不可逆处的 K 理论类 $[E]-[F]$——这就是 §s8 的 Atiyah–Bott–Shapiro / Thom 类构造；(iii) **Freed–Witten 反常**说一个膜只能缠绕一个 $\mathrm{Spin}^c$ 闭链——恰是 §s8 的 K 可定向性条件。微妙之处（H 通量）把分类推向**扭化 K 理论**。

**物质的拓扑相（概览）。** 一个有能隙量子系统的**拓扑相**是哈密顿量在保持能隙开放的连续形变下的等价类。对带给定对称性（时间反演 $T$、粒子–空穴 $C$、手征 $S$）的自由费米子，**十重道路**（Altland–Zirnbauer）把系统组织进十个对称类，并且：

> **原理 —— 拓扑相由 K 理论分类。** 在给定对称类下、空间维数 $d$ 中的自由费米子拓扑相之集合是一个 K 理论群；十个类对应十个实/复 K 理论函子，而对 $d$ 的依赖遵循 Bott 周期性时钟——$8$ 重实周期性（§s9）就是**拓扑绝缘体与超导体的周期表**（Kitaev）。

具体地，有能隙的哈密顿量经其占据态丛（到负能态的投影）定义出 Brillouin 区环面 / 动量空间的 $K^0$ 或 $KO^j$ 中的一个类；像 Chern 数（整数量子霍尔）这样的拓扑不变量是这个类的 $\mathrm{ch}$（§s7），而 $\mathbb{Z}/2$ 不变量（量子自旋霍尔 / $\mathbb{Z}_2$ 拓扑绝缘体）恰是 $KO$ 表中的挠项 $\mathbb{Z}/2$（§s9）——任何上同调/Chern 数不变量都看不见，只有 K 理论才能探测。当人们改变维数或对称类时该表的八重移位，是 Bott 周期性的物理化身：计算 $KO^*(\mathrm{pt})$ 的同一套 Clifford 模代数预言了哪些相存在。

**例题 —— 作为 Chern 数的整数量子霍尔效应。** 磁场中充填了 $\nu$ 个 Landau 能级的二维电子气，其动量空间是 Brillouin 环面 $T^2$。占据带组装成一个秩为 $\nu$ 的复丛 $E\to T^2$，定义出一个类 $[E]\in K^0(T^2)$。其拓扑内容是第一 Chern 数
$$
c_1(E)=\frac{1}{2\pi}\int_{T^2}F\in\mathbb{Z},
$$
即 Berry 曲率 $F$ 的积分——等于 $\mathrm{ch}_1(E)$，Chern 特征标的次数 $2$ 部分（§s7）。TKNN 公式把霍尔电导等同为 $\sigma_{xy}=c_1(E)\cdot e^2/h$：量子化平台字面上就是带丛的整数 K 理论不变量。这里 $K^0$，复（无反酉对称性），十重道路的 A 类，处于 $d=2$——而该表预言 $K^0(\mathrm{pt})$-型不变量 $\mathbb{Z}$，恰是观测到的整数量子化。$S^2$ 上的同一个丛（单个 Dirac 单极子，$c_1=1$）就是 §s3 的 Hopf 丛 $H$：整数量子霍尔效应的生成元与 Bott 生成元是同一个对象。

> **统一的图景。** 一束基态丛 $\to$ 一个 K 理论类 $\to$ 经 Chern 特征标（整数不变量）与 $KO$ 的挠（$\mathbb{Z}/2$ 不变量）得到不变量，并由 Bott 周期性支配跨维数的模式。为分类向量丛而建立的数学，竟能计数 D 膜荷并列出物质的状态——使 K 理论可计算的那同一份稳定性与周期性，也使它在物理上不可避免。

---

*一门拓扑 K 理论的入门课程——从向量丛与 Grothendieck 群，经 Bott 周期性与广义上同调公理，到 Chern 特征标、Thom 同构与前推，再到该理论的解析与物理化身。先读一遍以把握其架构：向量丛变成一个环，那个环变成一个 $2$ 周期的上同调理论，而那个周期性——关于 $GL(\mathbb{C})$ 与 Laurent 多项式的一个事实——正是让 K 理论得以计算椭圆算子的指标、计数 D 膜的荷、列出物质拓扑相的东西。把任何方框中的定义或演示当作参考随时回看，并把这句口号放在眼前：K 理论只在稳定化意义下记住一个丛，而那种忘却恰恰使它刚性、周期且强大。*
