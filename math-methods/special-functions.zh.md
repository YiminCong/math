[English](special-functions.md) · **中文**

# 特殊函数，*物理学反复求索的那些解。*

*这是一门关于数学物理中特殊函数的、自成体系的入门课程——Gamma 函数与 Beta 函数，正交多项式的几大家族（Legendre、Hermite、Laguerre），球谐函数，以及 Bessel 函数——还有把它们统一起来的那套机制：权函数、生成函数、递推关系，以及将它们串联在一起的超几何级数。每一个术语都用文字定义，每一个公式都给出动机，每一段推导都是一条编了号、无缝衔接的理由链。课程建立在基础代数与单变量微积分之上；通往量子力学与波动方程的桥梁都被明确地铺设出来。*

[← 返回全部指南](../README.zh.md)

## A 部分 · 特殊函数为何存在

<a id="s0"></a>
### 动机：一再出现的同一批方程

#### 用一句话说清本指南讲什么

翻开任何一本讲热流、振动膜、静电学或量子力学的书，你都会一再遇到*同样的那一小撮函数*：Legendre 多项式、Bessel 函数、Hermite 与 Laguerre 多项式、球谐函数。它们并非随意而来。一旦把物理学的基本偏微分方程（PDE）——**Laplace 方程**、**波动方程**、**热方程**、**Schrödinger 方程**——写在适合问题几何形状的坐标中，它们便是这些方程天然的"振动模式"。本指南从零开始构造这些函数，证明它们的定义性质，并说明为什么物理学总是恰好需要它们。

#### 它们从何而来：分离变量法

物理学的核心 PDE 都是线性的，形如（Laplace 算子）$=$（某个东西）。在具有球对称性的区域（一个原子、一颗行星的场）我们使用球坐标 $(r,\theta,\phi)$；在具有柱对称性的区域（一根导线、一面鼓、一根管道）我们使用柱坐标 $(\rho,\phi,z)$。标准的求解技术是**分离变量法**：猜测解可以分解为若干单变量函数的乘积，例如

$$
u(r,\theta,\phi)=R(r)\,\Theta(\theta)\,\Phi(\phi),
$$

代入 PDE，再把整式除开。由于此时每个变量都出现在自己的项里，每一项必须各自等于一个常数（一个*分离常数*）。这个含三个变量的单一 PDE 便分解为三个**常微分方程**（ODE），每个坐标一个。特殊函数恰好就是这些 ODE 的解：

- 球坐标中的极角方程是 **Legendre 方程**；它行为良好的解是 **Legendre 多项式** $P_\ell$，以及（带一个方位角指标的）**连带 Legendre 函数** $P_\ell^m$，后者与 $e^{im\phi}$ 组合成**球谐函数** $Y_\ell^m$（§s4、§s5）。
- 柱坐标中的径向方程是 **Bessel 方程**；它的解是 **Bessel 函数** $J_\nu$（§s6）。
- 抛物势阱中粒子的 Schrödinger 方程给出 **Hermite 方程**，其解是 **Hermite 多项式** $H_n$（§s7）。
- 氢原子的径向 Schrödinger 方程给出**连带 Laguerre** 方程，其解是 **Laguerre 多项式** $L_n^{(\alpha)}$（§s8）。

#### 四个方程，集中在一处

作为参考，驱动整个学科的 PDE 是（其中 $\nabla^2$ 为 Laplace 算子，$c$ 为波速，$k$ 为扩散常数，$\hbar,m,V$ 为量子量）：

$$
\nabla^2 u=0\ \ (\text{Laplace}),\quad \nabla^2 u=\frac{1}{c^2}\partial_t^2 u\ \ (\text{wave}),\quad \nabla^2 u=\frac{1}{k}\partial_t u\ \ (\text{heat}),\quad -\frac{\hbar^2}{2m}\nabla^2\psi+V\psi=i\hbar\,\partial_t\psi\ \ (\text{Schr\"odinger}).
$$

每一个都是线性的，且都由 Laplace 算子构造而成，因此每一个都可用分离变量法处理；几何形状（$\nabla^2$ 在所选坐标中的形式）决定哪些特殊函数登场。球面给出 Legendre 与球谐函数；柱面给出 Bessel；抛物势给出 Hermite；Coulomb 势给出 Laguerre。物理学惊人的节俭之处在于：这四个方程，在两三种标准坐标系中，便囊括了经典与量子现象中极大的一部分——而它们只需要本指南所构造的这一小撮函数。

#### 共同的线索

所有这些函数都共享一种深层结构：它们关于某个权函数是**正交的**（§s3），它们服从**三项递推关系**与 **Rodrigues 公式**（§s3、§s9），它们由**生成函数**打包（§s9），而且——最令人惊讶的是——它们几乎全是同一个对象的特例，那就是**超几何函数**（§s10）。Gamma 函数（§s1），即阶乘的连续推广，是其中的连接组织：它出现在归一化常数中、级数系数中，以及超几何级数的定义本身之中。

为什么偏偏是正交性成为反复出现的那条性质？因为每个分离方程背后的物理算子（角向 Laplace 算子、径向算子、振子 Hamilton 量）都是**自伴的**——在相应的内积下它等于自己的"转置"。线性代数的一条基本定理，搬到函数上，便是：自伴算子属于不同特征值的特征向量是正交的。特殊函数恰好就是这些特征向量，而它们各自不同的特征值正是量子化了的 $\ell(\ell+1)$、$2n$、能级，等等。所以"这些函数是正交的"乃是"对称矩阵的特征向量相互垂直"在无穷维中的回响，而权函数 $w$ 不过是那个算子恰好在其下对称的内积。把这个类比记在心里，会让整个学科感觉像线性代数，而不是一堆公式的标本馆。

#### 本指南的路线图

> Gamma 与 Beta（那些常数）→ 正交多项式（一般理论）→ Legendre → 球谐函数 → Bessel → Hermite → Laguerre → 生成函数与递推关系（那套机制）→ 超几何函数（宏大的统一）。

#### 常见陷阱

- "特殊"并不意味着"罕见"。这些函数的*特殊*在于*有名有姓、被列入表册*；它们在物理学中和 $\sin$、$\cos$ 一样常见（而 $\sin$、$\cos$ 本身就是特殊函数——$y''+y=0$ 的解）。
- 每个 ODE 通常都还有第二个解，但它在某个奇点（原点，或球的两极）处发散。物理学以**正则性**为由舍弃它——波函数或势必须保持有限。我们会在每处发生此事时予以标记。

## B 部分 · 两个基本函数

<a id="s1"></a>
### Gamma 函数：阶乘的延拓

#### 是什么 & 为什么

阶乘 $n!=1\cdot 2\cdots n$ 计数 $n$ 个对象的排列数，并出现在每一个 Taylor 级数中。但它只对非负整数有定义。许多公式——在概率论中、在 $n$ 维球的体积中、在特殊函数的系数中——要求对一个*分数*乃至复数取阶乘。**Gamma 函数** $\Gamma(z)$ 是唯一一个自然地填补这些空缺的函数：一条恰好穿过各阶乘值的光滑曲线。

#### 定义

> **定义 —— Gamma 函数（Euler 积分）。** 对实部为正的复数 $z$，即 $\mathrm{Re}(z)>0$，
> $$
> \Gamma(z)=\int_0^\infty t^{\,z-1}e^{-t}\,dt .
> $$

这里 $t$ 是实积分变量，$e^{-t}$ 是使积分在 $t\to\infty$ 处收敛的指数衰减，而 $t^{z-1}=e^{(z-1)\ln t}$ 是一个幂。条件 $\mathrm{Re}(z)>0$ 是必需的，以保证被积函数 $t^{z-1}$ 在 $t=0$ 附近可积：在原点附近，$\int_0 t^{z-1}\,dt$ 恰好在 $\mathrm{Re}(z-1)>-1$ 时收敛，即 $\mathrm{Re}(z)>0$。

#### 递推关系 $\Gamma(z+1)=z\,\Gamma(z)$ —— 证明

这条单一的恒等式是整个学科的引擎：它是"阶乘性质" $n!=n\cdot(n-1)!$ 的连续形式。

> **定理。** 对所有满足 $\mathrm{Re}(z)>0$ 的 $z$，$\ \Gamma(z+1)=z\,\Gamma(z)$。

**证明（分部积分）。**

1. 从定义出发，把 $z+1$ 代入相应位置：$\displaystyle\Gamma(z+1)=\int_0^\infty t^{\,z}e^{-t}\,dt$。*（理由：在 Euler 积分中作替换 $z\mapsto z+1$；指数 $z-1$ 变成 $z$。）*
2. 应用**分部积分** $\int u\,dv = uv-\int v\,du$，取 $u=t^{z}$、$dv=e^{-t}\,dt$。于是 $du=z\,t^{z-1}\,dt$（幂法则），$v=-e^{-t}$（$e^{-t}$ 的原函数）。*（理由：对 $(0,\infty)$ 上这些连续可微的因子而言，分部积分成立。）*
3. 这给出 $\displaystyle\Gamma(z+1)=\Big[-t^{z}e^{-t}\Big]_0^\infty+\int_0^\infty z\,t^{z-1}e^{-t}\,dt$。
4. 计算边界项 $\big[-t^{z}e^{-t}\big]_0^\infty$。当 $t\to\infty$ 时，$e^{-t}$ 的衰减快于任何幂 $t^{z}$ 的增长，故乘积 $\to 0$。当 $t\to 0^+$ 时，因 $\mathrm{Re}(z)>0$ 有 $t^{z}\to 0$，故乘积 $\to 0$。因此边界项为 $0$。*（理由：在无穷远处指数胜过多项式；在零点处正实部指数把幂压为零。）*
5. 剩下的积分由 $\Gamma(z)$ 的定义即为 $z\int_0^\infty t^{z-1}e^{-t}\,dt=z\,\Gamma(z)$。*（理由：把常数 $z$ 提出积分；认出这是 Euler 积分。）*
6. 因此 $\Gamma(z+1)=z\,\Gamma(z)$。$\blacksquare$

#### 推广阶乘

> **推论。** 对每个非负整数 $n$，$\ \Gamma(n+1)=n!$。

**证明（归纳法）。**
1. *基础情形。* $\displaystyle\Gamma(1)=\int_0^\infty e^{-t}\,dt=\big[-e^{-t}\big]_0^\infty=0-(-1)=1=0!$。*（理由：直接求值；按约定 $0!=1$。）*
2. *归纳步骤。* 假设 $\Gamma(n+1)=n!$。由 $z=n+1$ 时的递推关系，$\Gamma(n+2)=(n+1)\Gamma(n+1)=(n+1)\cdot n!=(n+1)!$。*（理由：刚证明的递推关系，再用归纳假设。）*
3. 由归纳法，命题对一切 $n\ge 0$ 成立。$\blacksquare$

所以 $\Gamma$ 把阶乘平移了一位：$\Gamma(z+1)$"就是"$z!$。这一平移是 Euler 定义的历史偶然，也是本学科中差一错误最常见的单一来源。

#### 关键取值与延拓

递推关系还让我们能把 $\Gamma$ *延拓*到负宗量：把它改写为 $\Gamma(z)=\Gamma(z+1)/z$。只要 $\mathrm{Re}(z)>-1$（且 $z\ne0$），右边就有意义，从而在那里定义了 $\Gamma$；反复使用此技巧便覆盖整个平面，唯独除去非正整数 $0,-1,-2,\dots$，在那里 $1/z$ 型的因子发散。于是 $\Gamma$ 在 $z=0,-1,-2,\dots$ 处有**简单极点**，而在其他每一处都有限且光滑。

有一个取值很著名，值得记录。**半整数**取值是

$$
\Gamma\!\left(\tfrac12\right)=\sqrt{\pi}.
$$

**证明。**
1. 由定义，$\Gamma(\tfrac12)=\int_0^\infty t^{-1/2}e^{-t}\,dt$。
2. 作替换 $t=x^2$，于是 $dt=2x\,dx$，$t^{-1/2}=1/x$（对 $x>0$）。积分限仍为 $0$ 与 $\infty$。*（理由：一个光滑、单调的变量替换。）*
3. 积分变为 $\int_0^\infty \frac1x\,e^{-x^2}\,2x\,dx=2\int_0^\infty e^{-x^2}\,dx$。
4. **Gauss 积分** $\int_0^\infty e^{-x^2}\,dx=\tfrac{\sqrt\pi}{2}$（标准结果；通过平方并换到极坐标来证明）。*（理由：引用微积分中的预备知识。）*
5. 因此 $\Gamma(\tfrac12)=2\cdot\tfrac{\sqrt\pi}{2}=\sqrt\pi$。$\blacksquare$

结合递推关系：$\Gamma(\tfrac32)=\tfrac12\Gamma(\tfrac12)=\tfrac{\sqrt\pi}{2}$，以及 $\Gamma(\tfrac52)=\tfrac32\cdot\tfrac12\sqrt\pi=\tfrac{3\sqrt\pi}{4}$。

#### 反射公式

第二条恒等式把 $\Gamma$ 与正弦联系起来，是许多化简的来源：

$$
\Gamma(z)\,\Gamma(1-z)=\frac{\pi}{\sin(\pi z)},\qquad z\notin\mathbb Z.
$$

我们不会从头重证它（它依赖于 $\sin$ 的无穷乘积表示），但有两个推论值得一看。令 $z=\tfrac12$ 便复得 $\Gamma(\tfrac12)^2=\pi/\sin(\pi/2)=\pi$，即 $\Gamma(\tfrac12)=\sqrt\pi$，与上面的积分证明一致。又因为 $\sin(\pi z)$ 在每个整数处有零点，右边在那里发散，这确认了 $\Gamma$ 在非正整数处的极点，并表明 $\Gamma$ *没有*零点（一个等于有限非零数的乘积，除非另一个因子为无穷，否则不可能有一个因子为零）。

#### Stirling 近似，及其重要性

对大宗量，Gamma 函数（从而阶乘）以一种可被精确控制的方式增长：

$$
\Gamma(z+1)=z!\;\sim\;\sqrt{2\pi z}\;\Big(\frac{z}{e}\Big)^{z}\qquad(z\to\infty).
$$

其背后的思想是 **Laplace 方法**：在 $\Gamma(z+1)=\int_0^\infty t^{z}e^{-t}\,dt=\int_0^\infty e^{z\ln t-t}\,dt$ 中，指数 $f(t)=z\ln t-t$ 在 $f'(t)=z/t-1=0$ 处取最大，即在 $t=z$ 处。把 $f$ 在其峰值附近展开到二阶（$f''(z)=-z/t^2|_{t=z}=-1/z$）会把积分变成一个 Gauss 积分 $\int e^{f(z)-\frac{1}{2z}(t-z)^2}dt$，其值 $e^{f(z)}\sqrt{2\pi z}=z^z e^{-z}\sqrt{2\pi z}$ 恰好就是 Stirling 公式。*（理由：一个尖锐峰起的被积函数被其最大值处的 Gauss 鼓包所主导。）* 这就是为什么热力学（$\ln N!\approx N\ln N-N$）和中心极限定理都倚赖 $\Gamma$。

#### 例题

计算 $\Gamma(6)$ 与 $\Gamma(\tfrac72)$。由推论 $\Gamma(6)=5!=120$。由递推关系，$\Gamma(\tfrac72)=\tfrac52\Gamma(\tfrac52)=\tfrac52\cdot\tfrac34\sqrt\pi=\tfrac{15}{8}\sqrt\pi\approx 3.32$。作为 Stirling 检验，$\Gamma(6)=5!=120$ 对比 $\sqrt{10\pi}\,(5/e)^5$：这里 $(5/e)^5\approx 21.06$ 且 $\sqrt{10\pi}\approx 5.605$，故乘积 $\approx 118.0$，与 $120$ 相差在 $2\%$ 之内——在 $z=5$ 时已经相当好了。

#### 一个几何应用：$n$ 维球的体积

$n$ 维单位球的体积是 $V_n=\dfrac{\pi^{n/2}}{\Gamma(\tfrac n2+1)}$。Gamma 函数在此不可回避，因为 $n$ 可以是奇数，那时半整数阶乘值 $\Gamma(\tfrac32),\Gamma(\tfrac52),\dots$ 就会出现。对 $n=3$：$V_3=\pi^{3/2}/\Gamma(\tfrac52)=\pi^{3/2}/(\tfrac34\sqrt\pi)=\tfrac43\pi$，即在 $r=1$ 时熟悉的 $\tfrac43\pi r^3$。半整数 Gamma 值并非奇珍异玩；它们就是"球的体积"的字面内容。

#### 应用：归一化 Gamma 分布

Gamma 函数实际上就是某个概率分布的归一化常数。**Gamma 分布**在 $t>0$ 上有密度 $p(t)=\dfrac{1}{\Gamma(\alpha)\beta^\alpha}\,t^{\alpha-1}e^{-t/\beta}$。它积分为 $1$ 不过是 Euler 积分的乔装：作替换 $u=t/\beta$ 得到 $\int_0^\infty t^{\alpha-1}e^{-t/\beta}dt=\beta^\alpha\int_0^\infty u^{\alpha-1}e^{-u}du=\beta^\alpha\Gamma(\alpha)$，恰好抵消前置因子。期望值通过 $\int_0^\infty t\cdot t^{\alpha-1}e^{-t/\beta}dt=\beta^{\alpha+1}\Gamma(\alpha+1)=\alpha\beta\cdot\beta^\alpha\Gamma(\alpha)$ 算出为 $\alpha\beta$，这里又一次用到递推关系 $\Gamma(\alpha+1)=\alpha\Gamma(\alpha)$。连续阶乘就这样被直接编织进了统计学。

#### 直觉与陷阱

- 把 $\Gamma$ 想成穿过诸点 $(1,1),(2,1),(3,2),(4,6),\dots$ 的最光滑曲线（Bohr–Mollerup 定理通过对数凸性使"最光滑"变得精确）。
- 记住那个平移：$\Gamma(n)=(n-1)!$，**而不是** $n!$。
- $\Gamma$ *从不为零*；反之，$1/\Gamma$ 是一个整函数，其零点恰在非正整数处。

<a id="s2"></a>
### Beta 函数及其与 Gamma 的联系

#### 是什么 & 为什么

许多在*有限*区间 $[0,1]$ 上的积分——Beta 分布变量的概率、Jacobi 多项式的归一化、体积——都具有 $\int_0^1 x^{a-1}(1-x)^{b-1}\,dx$ 的形状。**Beta 函数**恰好把这种形状打包起来，而一条优美的恒等式通过 Gamma 来表达它，从而把有限区间上的积分变成阶乘之比。

#### 定义

> **定义 —— Beta 函数。** 对 $\mathrm{Re}(p)>0$ 与 $\mathrm{Re}(q)>0$，
> $$
> B(p,q)=\int_0^1 x^{\,p-1}(1-x)^{\,q-1}\,dx .
> $$

两个因子 $x^{p-1}$ 与 $(1-x)^{q-1}$ 关于中点对称，这已经暗示了 $B(p,q)=B(q,p)$（作替换 $x\mapsto 1-x$）。

#### 关系式 $B(p,q)=\dfrac{\Gamma(p)\,\Gamma(q)}{\Gamma(p+q)}$ —— 证明

> **定理。** 对 $\mathrm{Re}(p)>0,\mathrm{Re}(q)>0$，$\ B(p,q)=\dfrac{\Gamma(p)\Gamma(q)}{\Gamma(p+q)}$。

**证明。**
1. 写出乘积 $\Gamma(p)\Gamma(q)=\Big(\int_0^\infty s^{p-1}e^{-s}ds\Big)\Big(\int_0^\infty t^{q-1}e^{-t}dt\Big)=\iint_{s,t>0} s^{p-1}t^{q-1}e^{-(s+t)}\,ds\,dt$。*（理由：两个独立变量的积分之乘积就是在第一象限上的二重积分——Fubini 定理，因被积函数为正而成立。）*
2. 换元到 $s=u\,x$、$t=u(1-x)$，其中 $u=s+t\in(0,\infty)$ 是总量，$x=s/(s+t)\in(0,1)$ 是占比。*（理由：这把第一象限双射地映到条带 $u>0,\ 0<x<1$ 上。）*
3. 计算 $(s,t)\mapsto(u,x)$ 的 **Jacobi 行列式**。由 $s=ux,\ t=u(1-x)$：$\partial(s,t)/\partial(u,x)=\det\begin{pmatrix} x & u\\ 1-x & -u\end{pmatrix}=x(-u)-u(1-x)=-u$，故 $ds\,dt=|{-u}|\,du\,dx=u\,du\,dx$。*（理由：换元公式；取 Jacobi 行列式的绝对值。）*
4. 又有 $s+t=u$ 及 $s^{p-1}t^{q-1}=(ux)^{p-1}\big(u(1-x)\big)^{q-1}=u^{p+q-2}x^{p-1}(1-x)^{q-1}$。
5. 代入：$\Gamma(p)\Gamma(q)=\int_0^\infty\!\!\int_0^1 u^{p+q-2}x^{p-1}(1-x)^{q-1}e^{-u}\,u\,dx\,du$。
6. 分离现已独立的积分：$=\Big(\int_0^\infty u^{p+q-1}e^{-u}\,du\Big)\Big(\int_0^1 x^{p-1}(1-x)^{q-1}\,dx\Big)=\Gamma(p+q)\,B(p,q)$。*（理由：$u$-积分是 $\Gamma(p+q)$ 的 Euler 积分；$x$-积分按定义为 $B(p,q)$。）*
7. 除以 $\Gamma(p+q)$（非零）得到 $B(p,q)=\Gamma(p)\Gamma(q)/\Gamma(p+q)$。$\blacksquare$

#### 例题

计算 $\int_0^{\pi/2}\sin^4\theta\,d\theta$。作替换 $x=\sin^2\theta$ 把三角幂变成一个 Beta 积分；标准结果是

$$
\int_0^{\pi/2}\sin^{2a-1}\theta\,\cos^{2b-1}\theta\,d\theta=\tfrac12 B(a,b).
$$

对 $\sin^4\theta$ 取 $2a-1=4\Rightarrow a=\tfrac52$ 及 $2b-1=0\Rightarrow b=\tfrac12$。于是 $\tfrac12 B(\tfrac52,\tfrac12)=\tfrac12\dfrac{\Gamma(5/2)\Gamma(1/2)}{\Gamma(3)}=\tfrac12\cdot\dfrac{\frac{3}{4}\sqrt\pi\cdot\sqrt\pi}{2}=\tfrac12\cdot\dfrac{3\pi/4}{2}=\dfrac{3\pi}{16}$，与课本值吻合。

上面的三角形式并非魔法；这里给出它的一行推导。从 $B(a,b)=\int_0^1 x^{a-1}(1-x)^{b-1}dx$ 出发，作替换 $x=\sin^2\theta$，于是 $dx=2\sin\theta\cos\theta\,d\theta$，$1-x=\cos^2\theta$，且当 $x:0\to1$ 时 $\theta:0\to\tfrac\pi2$。则 $x^{a-1}=\sin^{2a-2}\theta$，$(1-x)^{b-1}=\cos^{2b-2}\theta$，而 $B(a,b)=\int_0^{\pi/2}\sin^{2a-2}\theta\cos^{2b-2}\theta\cdot2\sin\theta\cos\theta\,d\theta=2\int_0^{\pi/2}\sin^{2a-1}\theta\cos^{2b-1}\theta\,d\theta$。*（理由：变量替换贡献了一个额外的 $\sin\theta\cos\theta$，把两个指数各抬高一。）* 除以 $2$ 即得上面所用的公式。

#### 倍量公式

一个漂亮的副产品是 **Legendre 倍量公式** $\Gamma(z)\Gamma(z+\tfrac12)=2^{1-2z}\sqrt\pi\,\Gamma(2z)$，Beta 函数能干净利落地把它交付出来。梗概：用两种方式求 $B(z,z)=\Gamma(z)^2/\Gamma(2z)$——一次直接求，一次在对称替换 $x=\tfrac{1+u}{2}$ 之后求，该替换把 $[0,1]$ 上的积分变成 $(1-u^2)^{z-1}$ 在 $[-1,1]$ 上的积分，而后者本身就是一个 Beta 值 $\tfrac12 B(\tfrac12,z)=\tfrac12\Gamma(\tfrac12)\Gamma(z)/\Gamma(z+\tfrac12)$。令 $B(z,z)$ 的两个表达式相等，再用 $\Gamma(\tfrac12)=\sqrt\pi$ 化简，便得到所述恒等式。*（理由：同一个积分，两种合法的替换，必须给出同一个答案。）* 这条公式正是半整数 Gamma 值在归一化常数中总与整数值并肩出现的原因。

#### 第二个例题：一个半直线上的积分

计算 $\int_0^\infty \dfrac{x^{p-1}}{(1+x)^{p+q}}\,dx$，这是统计学中出现的形式（Beta 素分布）。作替换 $x=\dfrac{u}{1-u}$，于是 $1+x=\dfrac{1}{1-u}$，$dx=\dfrac{du}{(1-u)^2}$，且当 $x:0\to\infty$ 时 $u:0\to1$。被积函数变成 $\Big(\dfrac{u}{1-u}\Big)^{p-1}(1-u)^{p+q}\dfrac{du}{(1-u)^2}=u^{p-1}(1-u)^{q-1}\,du$。*（理由：一个单调的变量替换，把半直线搬到 $[0,1]$ 上。）* 因此该积分等于 $B(p,q)=\Gamma(p)\Gamma(q)/\Gamma(p+q)$——同一个 Beta 值，如今却跨越整条半直线。

#### 陷阱

- Beta 积分是在 $[0,1]$ 上的；如果你的积分跑在 $[0,\infty)$ 或 $[-1,1]$ 上，先换元（如刚才所演示的）。
- 把对称性 $B(p,q)=B(q,p)$ 当作一个理智检验，它在对称的 Gamma 公式中清晰可见。

## C 部分 · 正交多项式

<a id="s3"></a>
### 正交多项式：一般理论

#### 是什么 & 为什么

有一条单一的线索贯穿 Legendre、Hermite 与 Laguerre 多项式，那就是**正交性**的思想——垂直向量在多项式中的类比。正如空间中任何向量都能写在一组相互垂直的单位向量基下，任何合理的函数都能在一组正交多项式的基下展开。本节一次性搭好一般机制，于是每个具名家族随后都成为一个快速的特例。

#### 带权内积

> **定义 —— 带权内积。** 固定一个区间 $[a,b]$（可以无穷）和其上的一个**权函数** $w(x)\ge 0$。对函数 $f,g$ 定义
> $$
> \langle f,g\rangle=\int_a^b f(x)\,g(x)\,w(x)\,dx .
> $$
> 若 $\langle f,g\rangle=0$，则两个函数（关于 $w$）**正交**。**范数**为 $\|f\|=\sqrt{\langle f,f\rangle}$。

权 $w$ 告诉我们在区间上"吻合在何处算数"。不同的物理问题供给不同的权：$[-1,1]$ 上的 $w=1$（Legendre，来自球面），$\mathbb R$ 上的 $w=e^{-x^2}$（Hermite，来自振子的 Gauss 基态），$[0,\infty)$ 上的 $w=x^\alpha e^{-x}$（Laguerre，来自氢的径向测度）。

> **定义 —— 正交多项式族。** 一个满足 $\deg p_n=n$ 的序列 $p_0,p_1,p_2,\dots$，若当 $m\ne n$ 时总有 $\langle p_m,p_n\rangle=0$，则它对权 $w$ 是**正交的**。若此外对所有 $n$ 都有 $\|p_n\|=1$，则该族是**正交规范的**。

给定一个权，这样的族在每个 $p_n$ 的归一化意义下是唯一的（你总能对 $1,x,x^2,\dots$ 作 Gram–Schmidt 来产生一个）。

#### 例题：用 Gram–Schmidt 构造 Legendre

取 $[-1,1]$ 上的 $w=1$，对 $1,x,x^2$ 作正交化，以具体看清这套机制。
1. $p_0=1$。其范数平方为 $\langle1,1\rangle=\int_{-1}^1 1\,dx=2$。
2. $p_1=x-\dfrac{\langle x,1\rangle}{\langle1,1\rangle}\cdot1$。现在 $\langle x,1\rangle=\int_{-1}^1 x\,dx=0$（奇被积函数在对称区间上），故 $p_1=x$。*（理由：减去到 $p_0$ 上的投影；该投影因对称性而消失。）*
3. $p_2=x^2-\dfrac{\langle x^2,1\rangle}{\langle1,1\rangle}\cdot1-\dfrac{\langle x^2,x\rangle}{\langle x,x\rangle}\cdot x$。计算 $\langle x^2,1\rangle=\int_{-1}^1 x^2dx=\tfrac23$ 及 $\langle x^2,x\rangle=\int_{-1}^1 x^3dx=0$。故 $p_2=x^2-\tfrac{2/3}{2}=x^2-\tfrac13$。
4. 重新缩放至 Legendre 归一化 $P_2(1)=1$：$x^2-\tfrac13$ 在 $x=1$ 处等于 $\tfrac23$，故 $P_2=\tfrac32(x^2-\tfrac13)=\tfrac12(3x^2-1)$，正是 §s4 的 $P_2$。

这表明正交族是被权*强制*出来的；唯一的自由是最后的标量归一化。

#### 为什么正交族是一组基：展开系数

设 $f=\sum_{k} c_k p_k$。与 $p_n$ 作内积：

$$
\langle f,p_n\rangle=\sum_k c_k\langle p_k,p_n\rangle=c_n\langle p_n,p_n\rangle,
$$

因为每个 $k\ne n$ 的交叉项都因正交性而消失。因此系数可由一个积分读出，

$$
c_n=\frac{\langle f,p_n\rangle}{\langle p_n,p_n\rangle}.
$$

这正是 Fourier 系数的工作方式，只是把 $\sin,\cos$ 换成了 $p_n$。*每一个*（关于 $w$）平方可积的函数都能这样被捕获——完备性——这是分析中一条更深的定理；这里我们把它当作组织原则来用。

有一条很有回报的恒等式，即 **Parseval 关系**：若 $f=\sum_n c_n p_n$，则 $\langle f,f\rangle=\sum_n c_n^2\langle p_n,p_n\rangle$，因为所有交叉项都因正交性而消失。用言语来说，$f$ 的"能量"（其范数平方）是其各分量能量之和——不同模式之间没有干涉。在量子力学中这表明不同测量结果的概率相加：若在某正交规范的能量基下 $\psi=\sum_n c_n\phi_n$，则 $\sum_n|c_n|^2=1$，且 $|c_n|^2$ 是测得第 $n$ 个能量的概率。因此特殊函数的正交性绝非技术上的细枝末节；它是"各模式互不交谈"的数学形式。

#### 三项递推关系

> **定理（三项递推）。** 任何正交多项式族都满足如下形式的关系
> $$
> p_{n+1}(x)=(A_n x+B_n)\,p_n(x)-C_n\,p_{n-1}(x)
> $$
> 其中常数 $A_n,B_n,C_n$ 依赖于该族。

**带完整理由的证明梗概。**
1. 多项式 $p_0,\dots,p_{n+1}$ 是所有次数 $\le n+1$ 的多项式的一组基，因为它们的次数是 $0,1,\dots,n+1$（这是由 $1,x,\dots,x^{n+1}$ 作出的三角的、因而可逆的变换）。
2. 考虑 $x\,p_n(x)$：它的次数为 $n+1$，故可写成 $x p_n=\sum_{k=0}^{n+1}\alpha_k p_k$。*（理由：第 1 步，在基下展开。）*
3. 对每个 $k$，$\alpha_k\|p_k\|^2=\langle x p_n,p_k\rangle=\langle p_n,x p_k\rangle$（变量 $x$ 在对称内积中可自由移动）。*（理由：$x$ 为实数，故 $\langle xf,g\rangle=\langle f,xg\rangle$。）*
4. 若 $k\le n-2$，则 $x p_k$ 的次数 $\le n-1<n$，而 $p_n$ 与*所有*次数 $<n$ 的多项式正交（因为这样的多项式是 $p_0,\dots,p_{n-1}$ 的组合，而它们各自都与 $p_n$ 正交）。因此对 $k\le n-2$ 有 $\alpha_k=0$。*（理由：与较低次数的正交性。）*
5. 只有 $k=n-1,n,n+1$ 留存，给出 $x p_n=\alpha_{n+1}p_{n+1}+\alpha_n p_n+\alpha_{n-1}p_{n-1}$。解出 $p_{n+1}$ 便给出所述形式，其中 $A_n=1/\alpha_{n+1}$，等等。$\blacksquare$

正是这个递推关系使得这些多项式计算起来很廉价：从 $p_0,p_1$ 出发，靠乘法与减法便能逐个磨出其余，从不必碰高次公式。

#### Rodrigues 型公式

每个经典家族也都有一个 **Rodrigues 公式**，它把 $p_n$ 紧凑地表达为一个简单函数的 $n$ 阶导数再除以权：

$$
p_n(x)=\frac{1}{e_n\,w(x)}\frac{d^n}{dx^n}\Big[w(x)\,s(x)^n\Big],
$$

其中 $s(x)$ 是一个固定的、次数 $\le 2$ 的多项式（正是其根为区间端点的那一个），而 $e_n$ 是一个归一化常数。我们将看到具体版本：Legendre 用 $w=1,\ s=x^2-1$；Hermite 用 $w=e^{-x^2},\ s=1$；Laguerre 用 $w=x^\alpha e^{-x},\ s=x$。这三个权连同它们的 $s$，恰好是 **Sturm–Liouville 特征值问题**的解，这就是正交性根本得以出现的抽象原因。

#### 正交性的 Sturm–Liouville 源头

每个经典家族所解的方程都可写成**自伴（Sturm–Liouville）形式**：

$$
\frac{d}{dx}\!\left[r(x)\,\frac{dy}{dx}\right]+\lambda\,w(x)\,y=0,
$$

其中 $r(x)$ 在区间端点处为零。这里 $\lambda$ 是特征值（例如 Legendre 的 $\ell(\ell+1)$，Hermite 的 $2n$），而 $w$ 是正交权。这条一般定理——我们将在每个具体情形中*重新证明*而非引用它——是：

> **Sturm–Liouville 正交性。** 属于*不同*特征值 $\lambda_m\ne\lambda_n$ 的特征函数 $y_m,y_n$ 满足 $\int y_m y_n\,w\,dx=0$。

证明总是我们在 §s4 中用过的同样三步：把每个方程乘以另一个特征函数，相减，认出一个完全导数 $\frac{d}{dx}[r(y_m y_n'-y_n y_m')]$，积分，然后看着边界项因 $r$ 在端点处为零而消亡。正交积分中的权 $w$ 被*强制*为方程中乘 $\lambda$ 的那同一个 $w$。这就是为什么每个家族的权不是一个自由的选择：它由它所解的物理方程所支配。

#### 陷阱

- 正交性是*相对于一个权*而言的。同一个 $n$ 次多项式对象只有在 $[-1,1]$ 上取权 $1$ 时才是"Legendre 多项式"；换一个权，你就得到一个不同的家族。

<a id="s4"></a>
### Legendre 多项式

#### 是什么 & 为什么

当你在球坐标中求解 Laplace 方程 $\nabla^2 V=0$ 并分离变量时，极角（$\theta$）部分在替换 $x=\cos\theta$ 之后变成 **Legendre 方程**。它的多项式解 $P_\ell(x)$ 是静电学与引力**多极展开**的基本构件。它们是 $[-1,1]$ 上权 $w=1$ 的正交族。

#### Legendre 方程

> **定义 —— Legendre 方程。** 对整数 $\ell\ge 0$，
> $$
> \frac{d}{dx}\!\left[(1-x^2)\frac{dP}{dx}\right]+\ell(\ell+1)\,P=0,\qquad -1\le x\le 1.
> $$

表达式 $\ell(\ell+1)$ 是**分离常数**；要求解在两极 $x=\pm1$ 处保持有限，便迫使它取那个特定值且 $\ell$ 为非负整数，而此时正则解便是一个次数为 $\ell$ 的多项式 $P_\ell(x)$，并由 $P_\ell(1)=1$ 归一化。

#### 为什么方程长这样——以及为什么 $\ell$ 必须是整数

球坐标中的 Laplace 算子，作用在一个无 $\phi$ 依赖的分离解 $u=R(r)\Theta(\theta)$ 上，给出一个角向部分 $\frac{1}{\sin\theta}\frac{d}{d\theta}\big(\sin\theta\,\Theta'\big)+\lambda\,\Theta=0$。作替换 $x=\cos\theta$（于是 $dx=-\sin\theta\,d\theta$ 且 $\sin^2\theta=1-x^2$）把 $\frac{1}{\sin\theta}\frac{d}{d\theta}\big(\sin\theta\,\frac{d}{d\theta}\big)$ 变成 $\frac{d}{dx}\big[(1-x^2)\frac{d}{dx}\big]$，产生带 $\lambda=\ell(\ell+1)$ 的 Legendre 方程。*（理由：变量替换的链式法则；那些 $\sin\theta$ 因子折进了 $(1-x^2)$ 中。）* 若试一个幂级数解 $\Theta=\sum a_k x^k$，系数之间的两项递推表明该级数在 $x=\pm1$（两极 $\theta=0,\pi$）处*发散*，除非它终止；终止恰好发生在 $\lambda=\ell(\ell+1)$ 且 $\ell$ 为非负整数时。所以量子化"$\ell$ 是整数"是换取一个在两极不发散的解所付的代价——这是贯穿本指南的一个反复出现的主题。

最初几个是

$$
P_0=1,\quad P_1=x,\quad P_2=\tfrac12(3x^2-1),\quad P_3=\tfrac12(5x^3-3x).
$$

#### 生成函数

> **定理（生成函数）。** 对 $|x|\le1$ 与 $|t|<1$，
> $$
> \frac{1}{\sqrt{1-2xt+t^2}}=\sum_{\ell=0}^\infty P_\ell(x)\,t^{\ell}.
> $$

这个紧凑的函数绝非偶然：当 $x=\cos\gamma$ 是 $\mathbf r$ 与 $\mathbf r'$ 之间夹角的余弦、$t=r_</r_>$ 是较小半径与较大半径之比时，$\frac{1}{\sqrt{1-2xt+t^2}}=\frac{1}{|\mathbf r-\mathbf r'|}\cdot r_>$ 恰好就是 **Coulomb/Newton 核** $1/|\mathbf r-\mathbf r'|$。所以 Legendre 多项式是从反平方距律中*诞生*出来的（§s9 由这个生成函数导出递推关系）。

#### Rodrigues 公式

> **定理（Rodrigues）。** $\displaystyle P_\ell(x)=\frac{1}{2^\ell\,\ell!}\frac{d^\ell}{dx^\ell}\big(x^2-1\big)^{\ell}$。

这是一般 Rodrigues 模板在 $w=1,\ s=x^2-1$ 时的实例，其中 $e_\ell=2^\ell\ell!$。在 $\ell=2$ 处作检验：$\frac{d^2}{dx^2}(x^2-1)^2=\frac{d^2}{dx^2}(x^4-2x^2+1)=12x^2-4$，除以 $2^2\cdot 2!=8$ 得 $\tfrac{12x^2-4}{8}=\tfrac12(3x^2-1)=P_2$。正确。

#### 正交性 —— 完整证明

> **定理（正交性）。** $\displaystyle\int_{-1}^{1}P_m(x)P_\ell(x)\,dx=\frac{2}{2\ell+1}\,\delta_{m\ell}$，其中 $\delta_{m\ell}=1$ 当 $m=\ell$，否则为 $0$。

**正交部分（$m\ne\ell$）的证明。**
1. 把 Legendre 方程对 $P_\ell$ 与对 $P_m$ 写成自伴形式：
$$
\big[(1-x^2)P_\ell'\big]'+\ell(\ell+1)P_\ell=0,\qquad \big[(1-x^2)P_m'\big]'+m(m+1)P_m=0.
$$
2. 把第一个乘以 $P_m$、第二个乘以 $P_\ell$，然后相减：
$$
P_m\big[(1-x^2)P_\ell'\big]'-P_\ell\big[(1-x^2)P_m'\big]'+\big[\ell(\ell+1)-m(m+1)\big]P_mP_\ell=0.
$$
*（理由：两个成立的方程的线性组合也成立。）*
3. 前两项合并成一个单一导数。用乘积法则检验：
$$
\frac{d}{dx}\Big[(1-x^2)\big(P_m P_\ell'-P_\ell P_m'\big)\Big]=P_m\big[(1-x^2)P_\ell'\big]'-P_\ell\big[(1-x^2)P_m'\big]',
$$
因为交叉项 $(1-x^2)(P_m'P_\ell'-P_\ell'P_m')$ 相消。*（理由：乘积法则，再消去相等的项。）*
4. 把整个方程在 $[-1,1]$ 上积分。全导数项积分为边界值 $\big[(1-x^2)(P_mP_\ell'-P_\ell P_m')\big]_{-1}^{1}$，它为 $0$，因为因子 $(1-x^2)$ 在 $x=\pm1$ 处为零。*（理由：微积分基本定理；端点把边界项压为零。）*
5. 剩下的是 $\big[\ell(\ell+1)-m(m+1)\big]\displaystyle\int_{-1}^1 P_m P_\ell\,dx=0$。
6. 由于 $m\ne\ell$（非负整数），$\ell(\ell+1)\ne m(m+1)$，故方括号非零；把它除去便迫使 $\int_{-1}^1 P_mP_\ell\,dx=0$。$\blacksquare$

**归一化 $\int_{-1}^1 P_\ell^2\,dx=\tfrac{2}{2\ell+1}$** 由生成函数得出：把它平方，在 $[-1,1]$ 上积分，用刚证明的正交性消去交叉项，再把 $t$ 的各次幂与 $\int_{-1}^1\frac{dx}{1-2xt+t^2}=\frac1t\ln\frac{1+t}{1-t}=\sum_\ell \frac{2}{2\ell+1}t^{2\ell}$ 相匹配。

#### 物理用途：多极展开

电荷分布 $\rho(\mathbf r')$ 产生势 $V(\mathbf r)=\frac{1}{4\pi\epsilon_0}\int\frac{\rho(\mathbf r')}{|\mathbf r-\mathbf r'|}d^3r'$。对于比源更靠外的场点（$r>r'$），用生成函数展开核（$t=r'/r,\ x=\cos\gamma$）：

$$
V(\mathbf r)=\frac{1}{4\pi\epsilon_0}\sum_{\ell=0}^\infty \frac{1}{r^{\ell+1}}\int \rho(\mathbf r')\,r'^{\ell}P_\ell(\cos\gamma)\,d^3r'.
$$

$\ell=0$ 项是**单极**（总电荷，按 $1/r$ 衰减），$\ell=1$ 是**偶极**（$1/r^2$），$\ell=2$ 是**四极**（$1/r^3$），以此类推。Legendre 多项式按各部分衰减的快慢把场分门别类——这就是远离源处静电学的组织方案。

#### 例题：把一个函数用 Legendre 多项式展开

把 $f(x)=x^2$ 在 $[-1,1]$ 上展开为 $\sum c_\ell P_\ell$。由于 $\deg f=2$，只有 $\ell=0,1,2$ 能有贡献。用 $c_\ell=\frac{2\ell+1}{2}\int_{-1}^1 f P_\ell\,dx$（§s3 的系数公式配上 §s4 的范数）：
- $c_0=\tfrac12\int_{-1}^1 x^2\,dx=\tfrac12\cdot\tfrac23=\tfrac13$。
- $c_1=\tfrac32\int_{-1}^1 x^2\cdot x\,dx=0$（奇被积函数）。
- $c_2=\tfrac52\int_{-1}^1 x^2\cdot\tfrac12(3x^2-1)\,dx=\tfrac54\int_{-1}^1(3x^4-x^2)\,dx=\tfrac54\big(3\cdot\tfrac25-\tfrac23\big)$。这里 $3\cdot\tfrac25=\tfrac65$ 且 $\tfrac65-\tfrac23=\tfrac{18-10}{15}=\tfrac{8}{15}$，故 $c_2=\tfrac54\cdot\tfrac{8}{15}=\tfrac{2}{3}$。

检验：$\tfrac13 P_0+\tfrac23 P_2=\tfrac13+\tfrac23\cdot\tfrac12(3x^2-1)=\tfrac13+x^2-\tfrac13=x^2$。展开精确地重现了 $f$，对于一个多项式来说本应如此。

#### 陷阱

- $P_\ell$ 是由 $P_\ell(1)=1$ 归一化的，**而不是**由单位范数归一化。它的范数平方是 $\tfrac{2}{2\ell+1}$；忘掉这个因子会败坏每一个展开系数。

<a id="s5"></a>
### 连带 Legendre 函数与球谐函数

#### 是什么 & 为什么

球面上完整的角向依赖需要两个指标：$\ell$ 用于极向形状，$m$ 用于方位角的扭转。极向部分是**连带 Legendre 函数** $P_\ell^m$，与 $e^{im\phi}$ 组合便构成**球谐函数** $Y_\ell^m(\theta,\phi)$。它们是球面的振动模式，在量子力学中则是角动量的特征函数。

#### 定义

> **定义 —— 连带 Legendre 函数。** 对整数 $0\le m\le\ell$，
> $$
> P_\ell^m(x)=(-1)^m(1-x^2)^{m/2}\frac{d^m}{dx^m}P_\ell(x),\qquad x=\cos\theta.
> $$

它们解**连带 Legendre 方程**，即当方位角分离常数为 $m^2$ 时出现的极向 ODE：

$$
\frac{d}{dx}\!\left[(1-x^2)\frac{dP}{dx}\right]+\left[\ell(\ell+1)-\frac{m^2}{1-x^2}\right]P=0.
$$

对 $m=0$ 这退化为 Legendre 方程，故 $P_\ell^0=P_\ell$。

#### 球谐函数与正交规范性

> **定义 —— 球谐函数。**
> $$
> Y_\ell^m(\theta,\phi)=\sqrt{\frac{2\ell+1}{4\pi}\,\frac{(\ell-m)!}{(\ell+m)!}}\;P_\ell^m(\cos\theta)\,e^{im\phi},\qquad -\ell\le m\le\ell.
> $$

那个笨拙的平方根常数恰好就是使它们在球面上正交规范的因子：

> **定理（球面上的正交规范性）。** 以立体角元 $d\Omega=\sin\theta\,d\theta\,d\phi$，
> $$
> \int_0^{2\pi}\!\!\int_0^{\pi} Y_\ell^m(\theta,\phi)\,\overline{Y_{\ell'}^{m'}(\theta,\phi)}\,\sin\theta\,d\theta\,d\phi=\delta_{\ell\ell'}\,\delta_{mm'}.
> $$

其机制分裂为两个独立的检验。方位角积分 $\int_0^{2\pi}e^{i(m-m')\phi}d\phi=2\pi\delta_{mm'}$ 处理 $m$ 指标（复指数的正交性）。极向积分 $\int_{-1}^1 P_\ell^m P_{\ell'}^m\,dx=\frac{2}{2\ell+1}\frac{(\ell+m)!}{(\ell-m)!}\delta_{\ell\ell'}$——其证明与 §s4 完全相同，只是方程中多了那个 $m$ 项——处理 $\ell$ 指标，而归一化常数把两个额外因子都抵消，只留下 $1$。

由于 $Y_\ell^m$ 既正交规范*又*完备，球面上**任何**函数都展开为 $f(\theta,\phi)=\sum_{\ell=0}^\infty\sum_{m=-\ell}^{\ell}c_{\ell m}Y_\ell^m$，其中 $c_{\ell m}=\int f\,\overline{Y_\ell^m}\,d\Omega$——这是 Fourier 级数在球面上的类比。它是辐射方向图、宇宙微波背景功率谱以及原子轨道之多极语言的基础。

#### 加法定理

一条单一的恒等式把球谐函数与 §s4 的 Legendre 多项式联系起来，并解释了多极展开的角向因子：

$$
P_\ell(\cos\gamma)=\frac{4\pi}{2\ell+1}\sum_{m=-\ell}^{\ell}Y_\ell^m(\theta_1,\phi_1)\,\overline{Y_\ell^m(\theta_2,\phi_2)},
$$

其中 $\gamma$ 是两个方向 $(\theta_1,\phi_1)$ 与 $(\theta_2,\phi_2)$ 之间的夹角。用言语来说：反平方距生成函数所产生的简单的 $P_\ell(\cos\gamma)$（其中 $\gamma$ 是源点与场点之间的夹角）分解为对参照于固定轴的各 $m$ 模式之和。这正是那座桥梁，它让 §s4 的多极展开能够用源的内禀多极矩 $\int\rho\,r'^\ell\,\overline{Y_\ell^m}\,d^3r'$ 重写——即电动力学中的标准形式。

#### 量子力学中的角动量

在量子力学中，轨道角动量算子是 $(\theta,\phi)$ 上的微分算子。球谐函数是它们共同的**特征函数**：

$$
\hat L^2\,Y_\ell^m=\hbar^2\,\ell(\ell+1)\,Y_\ell^m,\qquad \hat L_z\,Y_\ell^m=\hbar\,m\,Y_\ell^m.
$$

于是 $\ell$ 确定角动量的*大小*（$\sqrt{\ell(\ell+1)}\,\hbar$），而 $m$ 确定它在 $z$ 轴上的*投影*（$m\hbar$）。人们熟悉的原子轨道形状——$s$（$\ell=0$）、$p$（$\ell=1$）、$d$（$\ell=2$）——就是 $|Y_\ell^m|^2$ 的图像。角动量的整数量子化，归根结底就是这样一句话：只有整数 $\ell$ 才给出在两极都有限的极向解。

#### 例题

$Y_0^0=\frac{1}{\sqrt{4\pi}}$（常数，$s$ 轨道）。$Y_1^0=\sqrt{\frac{3}{4\pi}}\cos\theta$，其平方 $\propto\cos^2\theta$ 是沿 $z$ 指向的哑铃状 $p_z$ 轨道。检验 $Y_1^0$ 的归一化：$\int|Y_1^0|^2 d\Omega=\frac{3}{4\pi}\cdot 2\pi\int_0^\pi\cos^2\theta\sin\theta\,d\theta=\frac{3}{2}\cdot\frac{2}{3}=1$。正确。

#### 例题：把球面上的一个函数展开

把 $f(\theta,\phi)=\cos^2\theta$ 用球谐函数展开。因为 $f$ 没有 $\phi$ 依赖，只有 $m=0$ 项留存；又因为 $\cos^2\theta$ 是 $\cos\theta$ 的二次多项式，只有 $\ell=0,2$ 有贡献。用 $\cos^2\theta=\tfrac13+\tfrac23 P_2(\cos\theta)$——正是 §s4 中找到的 $x^2$ 的 Legendre 展开，其中 $x=\cos\theta$。把 $P_\ell$ 转换为归一化的 $Y_\ell^0=\sqrt{\tfrac{2\ell+1}{4\pi}}P_\ell$：
$$
\cos^2\theta=\tfrac13\cdot1+\tfrac23 P_2=\sqrt{\tfrac{4\pi}{1}}\cdot\tfrac13\,Y_0^0+\sqrt{\tfrac{4\pi}{5}}\cdot\tfrac23\,Y_2^0.
$$
于是系数为 $c_{0,0}=\tfrac{2\sqrt\pi}{3}$ 与 $c_{2,0}=\tfrac{2}{3}\sqrt{\tfrac{4\pi}{5}}$，其余皆消失。$\ell=0$ 部分是 $\cos^2\theta$ 在球面上的*平均值*（$\tfrac13$），而 $\ell=2$ 部分是它的四极形状——这恰是用来描述比如行星扁率或辐射各向异性的语言。

#### 陷阱

- 符号因子 $(-1)^m$（Condon–Shortley 相位）是一种约定；各书不同，它会传播进选择定则的符号中。挑定一种约定并坚持使用。

<a id="s6"></a>
### Bessel 函数

#### 是什么 & 为什么

从球面切换到**柱面**——一面鼓、一根同轴电缆、一个圆波导——波动方程或 Laplace 方程的径向部分便变成 **Bessel 方程**。它的解，**Bessel 函数** $J_\nu(x)$，描述波的幅度如何随到轴的距离变化。它们是"柱几何的三角函数"，但幅度缓慢衰减，零点不等间隔。

#### Bessel 方程

> **定义 —— $\nu$ 阶 Bessel 方程。**
> $$
> x^2\frac{d^2y}{dx^2}+x\frac{dy}{dx}+(x^2-\nu^2)\,y=0.
> $$

数 $\nu\ge0$ 是**阶**，通常是一个来自方位角分离（$e^{in\phi}$）的整数 $n$。点 $x=0$ 是一个**正则奇点**，所以我们用级数（Frobenius 方法）而非朴素的 Taylor 级数来求解。

#### 级数解 —— 完整推导

> **定理。** 一个在原点正则的解是
> $$
> J_\nu(x)=\sum_{k=0}^{\infty}\frac{(-1)^k}{k!\,\Gamma(k+\nu+1)}\left(\frac{x}{2}\right)^{2k+\nu}.
> $$

**推导。**
1. 假设一个 **Frobenius 级数** $y=\sum_{k\ge0}a_k x^{k+s}$，其中 $a_0\ne0$，$s$ 是未知指数。*（理由：正则奇点处的标准拟设。）*
2. 逐项求导：$y'=\sum a_k(k+s)x^{k+s-1}$，$y''=\sum a_k(k+s)(k+s-1)x^{k+s-2}$。
3. 代入方程并收集 $x^{k+s}$ 的系数。各项 $x^2y'',xy',-\nu^2 y$ 贡献 $a_k\big[(k+s)(k+s-1)+(k+s)-\nu^2\big]=a_k\big[(k+s)^2-\nu^2\big]$，而 $x^2y$ 项贡献 $a_{k-2}$。于是递推为
$$
a_k\big[(k+s)^2-\nu^2\big]+a_{k-2}=0.
$$
*（理由：匹配 $x$ 的相等幂次；每个幂次必须各自消失。）*
4. $k=0$ 项（$a_0\ne0$）迫使**指标方程** $s^2-\nu^2=0$，故 $s=\pm\nu$。取 $s=\nu$ 作为正则解。*（理由：最低幂确定指数。）*
5. $k=1$ 项给出 $a_1[(1+\nu)^2-\nu^2]=0\Rightarrow a_1=0$，于是每个奇系数都消失。*（理由：方括号 $(1+2\nu)\ne0$。）*
6. 对偶数 $k=2j$，递推变为 $a_{2j}=-\dfrac{a_{2j-2}}{(2j+2\nu)(2j)}=-\dfrac{a_{2j-2}}{4j(j+\nu)}$。*（理由：因式 $(2j+\nu)^2-\nu^2=2j(2j+2\nu)$。）*
7. 从 $a_0$ 迭代：$a_{2j}=\dfrac{(-1)^j a_0}{4^j\,j!\,(\nu+1)(\nu+2)\cdots(\nu+j)}=\dfrac{(-1)^j a_0\,\Gamma(\nu+1)}{4^j\,j!\,\Gamma(\nu+j+1)}$，用 $\Gamma$ 来压缩这个上升乘积（这正是 Gamma 函数大显身手之处）。*（理由：把递推叠缩；$\Gamma(z+1)=z\Gamma(z)$ 把乘积塌缩。）*
8. 选取标准归一化 $a_0=\dfrac{1}{2^\nu\,\Gamma(\nu+1)}$。则 $a_{2j}=\dfrac{(-1)^j}{2^{2j+\nu}j!\,\Gamma(\nu+j+1)}$，且 $y=\sum_j a_{2j}x^{2j+\nu}=J_\nu(x)$，正如所述。$\blacksquare$

选取 $s=-\nu$ 给出第二个、一般是奇异的解；对整数阶这两个解相关，于是出现一个真正独立的解 $Y_\nu$（**第二类 Bessel 函数**），但它在原点像 $\ln x$ 那样发散，对于在轴上正则的问题被舍弃。

#### 例题：$J_0$ 的级数

在级数中令 $\nu=0$ 给出 $J_0(x)=\sum_{k\ge0}\dfrac{(-1)^k}{(k!)^2}\big(\tfrac x2\big)^{2k}=1-\dfrac{x^2}{4}+\dfrac{x^4}{64}-\dfrac{x^6}{2304}+\cdots$，因为 $\Gamma(k+1)=k!$ 使分母为 $(k!)^2$。在 $x=1$ 处求值：$1-0.25+0.015625-0.000434+\cdots\approx0.7652$，即表中的 $J_0(1)=0.7652$。这交替的、迅速缩小的各项既说明了为什么该级数处处收敛（$(k!)^2$ 分母碾压分子），也说明了为什么 $J_0$ 起始于 $1$ 并立即向下弯——这是它向 $x\approx2.405$ 处的零点缓缓第一次振荡的开端。

#### 性质与零点

- **原点处的行为：** $J_0(0)=1$，而对 $\nu>0$ 有 $J_\nu(0)=0$（首项的幂为 $x^\nu$）。
- **大 $x$ 的渐近：** $J_\nu(x)\approx\sqrt{\frac{2}{\pi x}}\cos\!\big(x-\tfrac{\nu\pi}{2}-\tfrac\pi4\big)$——一个衰减的余弦，解释了"类三角而幅度收缩"的图景。
- **零点：** $J_\nu$ 有无穷多个正零点 $\alpha_{\nu,1}<\alpha_{\nu,2}<\cdots$；对 $J_0$ 这些是 $\approx 2.405,\,5.520,\,8.654,\dots$。它们*不是* $\pi$ 的倍数，这是与 $\sin$ 的关键区别。
- **圆盘上的正交性：** 对固定阶 $\nu$ 与零点 $\alpha_{\nu,k}$，当 $j\ne k$ 时 $\int_0^1 J_\nu(\alpha_{\nu,j}\rho)J_\nu(\alpha_{\nu,k}\rho)\,\rho\,d\rho=0$——权为 $\rho$（圆盘的面积元）。这使得 **Fourier–Bessel 级数**成为圆内的天然展开。

#### 圆盘正交性为何成立 —— 标度技巧

圆盘正交性值得一个证明，因为所涉及的两个函数解的是 Bessel 方程的*标度*版本。设 $u(\rho)=J_\nu(\alpha\rho)$ 与 $v(\rho)=J_\nu(\beta\rho)$，其中 $\alpha,\beta$ 是两个不同的零点（故 $u(1)=v(1)=0$）。各自满足一个 Sturm–Liouville 方程 $\big(\rho\,u'\big)'+\big(\alpha^2\rho-\tfrac{\nu^2}{\rho}\big)u=0$，对 $v$ 则带 $\beta^2$ 类似。把 $u$-方程乘以 $v$，$v$-方程乘以 $u$，相减，并在 $[0,1]$ 上积分：
$$
(\alpha^2-\beta^2)\int_0^1 \rho\,u v\,d\rho=\Big[\rho\big(u v'-v u'\big)\Big]_0^1.
$$
*（理由：相减时 $\tfrac{\nu^2}{\rho}$ 项相消，剩余的导数项塌缩成一个边界表达式，恰如 §s4。）* 在 $\rho=0$ 处因子 $\rho$ 把该项杀死；在 $\rho=1$ 处 $u(1)=v(1)=0$，故边界项完全消失。由于 $\alpha^2\ne\beta^2$，积分 $\int_0^1\rho\,J_\nu(\alpha\rho)J_\nu(\beta\rho)\,d\rho=0$。权 $\rho$ 由 Sturm–Liouville 形式强制而来（它是乘 $u'$ 的那个 $r(\rho)$），印证了 §s3 的教训：权来自方程，而非来自选择。

#### 递推与导数关系

Bessel 函数也满足三项递推，可直接由级数导出：

$$
J_{\nu-1}(x)+J_{\nu+1}(x)=\frac{2\nu}{x}J_\nu(x),\qquad J_{\nu-1}(x)-J_{\nu+1}(x)=2J_\nu'(x).
$$

把这两个相加与相减给出紧凑的阶梯形式 $J_\nu'=J_{\nu-1}-\frac{\nu}{x}J_\nu$ 与 $J_\nu'=\frac{\nu}{x}J_\nu-J_{\nu+1}$。作为第一个关系的快速检验，把不含生成函数的 $J_0$ 级数逐项求导：$J_0'(x)=\sum_{k\ge1}\frac{(-1)^k(2k)}{(k!)^2}\frac{x^{2k-1}}{2^{2k}}=-\sum_{j\ge0}\frac{(-1)^j}{j!(j+1)!}\frac{x^{2j+1}}{2^{2j+1}}=-J_1(x)$，与 $\nu=0$ 处的关系吻合（此时 $J_{-1}=-J_1$）。*（理由：在收敛半径内对幂级数逐项求导。）*

#### 一个积分表示

对整数阶 $n$ 有一个干净的积分形式，

$$
J_n(x)=\frac{1}{\pi}\int_0^\pi \cos\big(n\theta-x\sin\theta\big)\,d\theta,
$$

它来自 **Jacobi–Anger 展开** $e^{ix\sin\theta}=\sum_{n=-\infty}^{\infty}J_n(x)e^{in\theta}$——这本身不过是左边那个波关于 $\theta$ 的 Fourier 级数，以 $J_n$ 为 Fourier 系数。这种表示正是 Bessel 在研究行星运动（平近点角与偏近点角之间的关系）时最初遇见这些函数的方式，它使 $J_n$ 有界、振荡的特征显而易见：被积函数是一个余弦，故 $|J_n(x)|\le1$。

#### 物理用途：振动的鼓

半径为 $a$ 的圆形鼓面服从波动方程；分离变量给出径向因子 $J_n(k\rho)$ 与角向因子 $\cos n\phi$。被夹紧的边缘 $\rho=a$ 要求 $J_n(ka)=0$，故 $k=\alpha_{n,k}/a$。因此允许的振动频率为 $f_{n,k}=\frac{c}{2\pi}\frac{\alpha_{n,k}}{a}$。由于这些 $\alpha$ 不规则地间隔，鼓的泛音*不是*基频的谐波倍数——这正是为什么鼓听起来与弦不同。同样的函数描述光纤与微波腔的模式。

#### 例题：最低的鼓模式

对最简单的、轴对称的模式取 $n=0$。基频用第一个零点 $\alpha_{0,1}\approx2.405$；下一个轴对称泛音用 $\alpha_{0,2}\approx5.520$。频率比为 $\alpha_{0,2}/\alpha_{0,1}\approx5.520/2.405\approx2.295$——既不是弦的八度那干净的 $2$，也不是下一个的 $3$，而是一个看似无理的数。这一个计算就解释了鼓面那种特有的*无确定音高*的音色：它的泛音不会叠成谐波系列。对比一根弦，其模式用 $\sin(n\pi x/L)$，零点等间隔地落在 $n\pi$ 处，给出精确的整数频率比 $1:2:3:\dots$ 与一个确定的乐音音高。小提琴的音与定音鼓的咚声之间的区别，归根结底就是 $\sin$ 的零点与 $J_0$ 的零点之间的区别。

#### 陷阱

- 不要把阶 $\nu$（一个来自几何的固定指标）与零点的指标 $k$ 混淆。并且记住径向正交性中的权 $\rho$——没有它积分就不为零。

<a id="s7"></a>
### Hermite 多项式

#### 是什么 & 为什么

**量子谐振子**——抛物势 $V=\tfrac12 m\omega^2x^2$ 中的一个粒子——是物理学中最重要的可解模型（它近似*任何*势在极小值附近的行为，且是量子场论的基础）。求解它的 Schrödinger 方程产生 **Hermite 多项式** $H_n$，即全直线上 Gauss 权 $e^{-x^2}$ 的正交族。

#### Hermite 方程

> **定义 —— Hermite 方程。** 对整数 $n\ge0$，
> $$
> \frac{d^2 H}{dx^2}-2x\frac{dH}{dx}+2n\,H=0.
> $$

它的多项式解（即唯一那些增长不会快到 Gauss 函数也压不住的解）是 $H_n$，归一化使首项为 $(2x)^n$：

$$
H_0=1,\quad H_1=2x,\quad H_2=4x^2-2,\quad H_3=8x^3-12x.
$$

#### 生成函数与 Rodrigues 公式

> **生成函数。** $\displaystyle e^{\,2xt-t^2}=\sum_{n=0}^\infty H_n(x)\,\frac{t^n}{n!}$。
>
> **Rodrigues 公式。** $\displaystyle H_n(x)=(-1)^n e^{x^2}\frac{d^n}{dx^n}e^{-x^2}$。

Rodrigues 公式是一般模板在 $w=e^{-x^2},\,s=1$ 时的实例。检验 $n=2$：$\frac{d^2}{dx^2}e^{-x^2}=\frac{d}{dx}(-2xe^{-x^2})=(-2+4x^2)e^{-x^2}$，故 $(-1)^2e^{x^2}\cdot(-2+4x^2)e^{-x^2}=4x^2-2=H_2$。正确。

这两种打包方式是等价的，证明它是对这套机制的一次干净练习。生成函数 $e^{2xt-t^2}$ 可通过配方重写：$2xt-t^2=x^2-(x-t)^2$，故 $e^{2xt-t^2}=e^{x^2}e^{-(x-t)^2}$。现在把 $e^{-(x-t)^2}$ 在 $t=0$ 附近展开成关于 $t$ 的 Taylor 级数。由链式法则，$\frac{\partial^n}{\partial t^n}e^{-(x-t)^2}\big|_{t=0}=(-1)^n\frac{d^n}{dx^n}e^{-x^2}$（作用在 $x-t$ 的函数上时，每个 $t$-导数等于负的一个 $x$-导数）。因此
$$
e^{2xt-t^2}=e^{x^2}\sum_{n=0}^\infty \frac{t^n}{n!}(-1)^n\frac{d^n}{dx^n}e^{-x^2}=\sum_{n=0}^\infty\frac{t^n}{n!}\Big[(-1)^n e^{x^2}\frac{d^n}{dx^n}e^{-x^2}\Big].
$$
把 $t^n/n!$ 的系数与生成函数定义 $\sum H_n t^n/n!$ 相匹配，表明那个方括号*就是* $H_n$——恰好是 Rodrigues 公式。*（理由：两个关于 $t$ 的幂级数相等当且仅当它们的系数相等。）* 因此生成函数与 Rodrigues 公式是同一个陈述，通过配方相联系。

#### 带 Gauss 权的正交性 —— 关键步骤的证明

> **定理。** $\displaystyle\int_{-\infty}^{\infty}H_m(x)H_n(x)\,e^{-x^2}\,dx=2^n\,n!\,\sqrt{\pi}\;\delta_{mn}$。

**正交性（$m\ne n$）的证明。**
1. 把 Hermite 方程乘以 $e^{-x^2}$ 化为自伴（Sturm–Liouville）形式：$\big(e^{-x^2}H_n'\big)'+2n\,e^{-x^2}H_n=0$，因为 $\frac{d}{dx}(e^{-x^2}H_n')=e^{-x^2}(H_n''-2xH_n')$。*（理由：乘积法则重现了方程的前两项。）*
2. 对 $H_m$ 写出同样的式子，把 $H_n$-方程乘以 $H_m$ 反之亦然，相减：
$$
H_m(e^{-x^2}H_n')'-H_n(e^{-x^2}H_m')'+2(n-m)e^{-x^2}H_mH_n=0.
$$
3. 前两项等于 $\dfrac{d}{dx}\big[e^{-x^2}(H_mH_n'-H_nH_m')\big]$（乘积法则，交叉项相消）。*（理由：与 Legendre 证明相同的代数。）*
4. 在 $(-\infty,\infty)$ 上积分。全导数项给出 $\pm\infty$ 处的边界值，它们消失，因为 $e^{-x^2}$ 在那里把任何多项式都杀死。*（理由：Gauss 衰减主导多项式增长。）*
5. 剩下 $2(n-m)\int_{-\infty}^\infty e^{-x^2}H_mH_n\,dx=0$；由于 $n\ne m$，该积分为 $0$。$\blacksquare$

范数 $2^n n!\sqrt\pi$ 来自把生成函数平方并对 $e^{-x^2}$ 积分：$\int e^{2xt-t^2}e^{2xs-s^2}e^{-x^2}dx=\sqrt\pi\,e^{2st}=\sqrt\pi\sum_n \frac{(2st)^n}{n!}$；匹配 $t^ms^n$ 系数只留下 $m=n$ 且其值为 $2^n n!\sqrt\pi$。

#### 物理用途：量子谐振子

定态 Schrödinger 方程 $-\frac{\hbar^2}{2m}\psi''+\tfrac12 m\omega^2x^2\psi=E\psi$，在重新标度 $\xi=\sqrt{m\omega/\hbar}\,x$ 并提出 Gauss 因子 $e^{-\xi^2/2}$（唯一能驯服 $x^2$ 势的衰减）之后，恰好化为 Hermite 方程。归一化的本征态是

$$
\psi_n(\xi)=\Big(\tfrac{1}{2^n n!\sqrt\pi}\Big)^{1/2}H_n(\xi)\,e^{-\xi^2/2},\qquad E_n=\hbar\omega\Big(n+\tfrac12\Big).
$$

来自"$n$ 次 Hermite 多项式"的整数 $n$ *就是*那个量子数，而 $\psi_n$ 的正交规范性（Gauss 权 $\to$ 在两个因子之间分摊的 $e^{-\xi^2/2}$）就是能量本征态的正交性。基态能量 $\tfrac12\hbar\omega\ne0$ 是著名的零点能。

#### 升降算子与递推关系，并列对照

量子力学提供了一条算子路径，它与 Hermite 递推关系恰好相映成趣。定义 $a=\tfrac{1}{\sqrt2}(\xi+\partial_\xi)$（降）与 $a^\dagger=\tfrac{1}{\sqrt2}(\xi-\partial_\xi)$（升）。作用在本征态上，$a\,\psi_n=\sqrt n\,\psi_{n-1}$ 与 $a^\dagger\psi_n=\sqrt{n+1}\,\psi_{n+1}$。从 $\psi_n$ 剥去 Gauss 因子 $e^{-\xi^2/2}$，这些便直接变成 Hermite 关系：$a^\dagger\psi_n=\sqrt{n+1}\,\psi_{n+1}$ 展开为 $\big(2\xi-\tfrac{d}{d\xi}\big)$ 型的组合，重现 §s9 的 $H_{n+1}=2\xi H_n-2nH_{n-1}$ 与 $H_n'=2nH_{n-1}$。*（理由：$\partial_\xi$ 作用在 $H_n e^{-\xi^2/2}$ 上既产生一个 $H_n'$ 项又产生一个 $-\xi H_n$ 项，重新组合成相邻多项式。）* 所以抽象的"把能量升降 $\hbar\omega$"与"把 Hermite 指标上下移一步"是同一个陈述——物理与特殊函数的递推是同一结构的两副面孔。数算子 $a^\dagger a$ 的特征值为 $n$，这就是为什么 $E_n=\hbar\omega(n+\tfrac12)$。

#### 陷阱

- 存在两种约定："物理学家的" $H_n$（权 $e^{-x^2}$，此处所用）与"概率学家的" $He_n$（权 $e^{-x^2/2}$）。它们相差一个标度；混用会使范数被 $2$ 的幂败坏。

<a id="s8"></a>
### Laguerre 与连带 Laguerre 多项式

#### 是什么 & 为什么

**氢原子**是量子力学最高荣耀的可解问题。它的径向 Schrödinger 方程，在剥去指数衰减与离心幂之后，变成**连带 Laguerre 方程**。它的解，Laguerre 多项式 $L_n^{(\alpha)}$，是 $[0,\infty)$ 上权 $x^\alpha e^{-x}$ 的正交族——半直线上的天然权。

#### 定义

> **定义 —— Laguerre 方程。** $\displaystyle x\,y''+(1-x)\,y'+n\,y=0$，其多项式解为 $L_n(x)$。
>
> **连带 Laguerre。** $\displaystyle x\,y''+(\alpha+1-x)\,y'+n\,y=0$，其解为 $L_n^{(\alpha)}(x)$。

普通 Laguerre 是 $\alpha=0$。Rodrigues 公式（即 $w=x^\alpha e^{-x},\,s=x$ 模板）为

$$
L_n^{(\alpha)}(x)=\frac{x^{-\alpha}e^{x}}{n!}\frac{d^n}{dx^n}\big(x^{n+\alpha}e^{-x}\big).
$$

最初几个普通的：$L_0=1,\ L_1=1-x,\ L_2=1-2x+\tfrac12 x^2$。

#### 正交性

> **定理。** $\displaystyle\int_0^\infty L_m^{(\alpha)}(x)L_n^{(\alpha)}(x)\,x^\alpha e^{-x}\,dx=\frac{\Gamma(n+\alpha+1)}{n!}\,\delta_{mn}$。

其证明与 §s4 和 §s7 是同样的 Sturm–Liouville 论证：自伴形式为 $\big(x^{\alpha+1}e^{-x}y'\big)'+n\,x^\alpha e^{-x}y=0$，而边界项在 $x=0$ 处（因子 $x^{\alpha+1}$，正幂）与在 $x=\infty$ 处（因子 $e^{-x}$，指数衰减）都消失。具体地说：把 $L_m$ 的方程乘以 $L_n$ 反之亦然，相减，认出 $\frac{d}{dx}\big[x^{\alpha+1}e^{-x}(L_m L_n'-L_n L_m')\big]$，在 $[0,\infty)$ 上积分，边界项在两端都为 $0$——剩下 $(n-m)\int_0^\infty L_m L_n\,x^\alpha e^{-x}dx=0$，故 $m\ne n$ 时正交。范数通过 Rodrigues 公式与 Gamma 积分求得，为 $\Gamma(n+\alpha+1)/n!$——注意 Gamma 函数又一次供给了归一化。

在 $\alpha=0,\ n=0,1$ 处作一个快速的数值理智检验：$L_0=1,\ L_1=1-x$，$[0,\infty)$ 上权 $e^{-x}$。则 $\int_0^\infty 1\cdot(1-x)e^{-x}dx=\int_0^\infty e^{-x}dx-\int_0^\infty x e^{-x}dx=1-1=0$，确认了 $L_0\perp L_1$。两个 Gamma 积分 $\int_0^\infty e^{-x}dx=\Gamma(1)=1$ 与 $\int_0^\infty xe^{-x}dx=\Gamma(2)=1$ 恰好相消，这是正交性最初等的体现。

#### 物理用途：氢的径向波函数

对 Coulomb 势 $V=-\frac{e^2}{4\pi\epsilon_0 r}$，在球坐标中分离 Schrödinger 方程给出角向因子 $Y_\ell^m$（§s5）与一个径向方程。写 $\rho=2r/(na_0)$（$a_0$ 为 Bohr 半径，$n$ 为主量子数）并提出束缚态衰减 $e^{-\rho/2}$ 与小 $r$ 幂 $\rho^{\ell}$，余下部分的方程恰好是带 $\alpha=2\ell+1$、次数为 $n-\ell-1$ 的连带 Laguerre 方程。归一化的径向函数是

$$
R_{n\ell}(r)=N_{n\ell}\;e^{-\rho/2}\,\rho^{\ell}\,L_{\,n-\ell-1}^{(2\ell+1)}(\rho),
$$

其中 $N_{n\ell}$ 由上面的 Laguerre 范数确定。径向函数对不同 $n$（同一 $\ell$）的正交性，正是带权 $x^{2\ell+1}e^{-x}$ 的 Laguerre 正交性。整数次数 $n-\ell-1\ge0$ 迫使 $\ell\le n-1$——即在能级 $n$ 上可用的 $s,p,d,\dots$ 支壳止于 $\ell=n-1$ 这条规则。

#### 能级与量子数

产生 Laguerre 方程的那同一个分离过程也确定了**能级**。要求径向函数可归一化（在无穷远处衰减）便迫使 Laguerre 次数 $n-\ell-1$ 为非负整数，而追踪那些常数便给出 Bohr 谱

$$
E_n=-\frac{m e^4}{2(4\pi\epsilon_0)^2\hbar^2}\,\frac{1}{n^2}=-\frac{13.6\ \text{eV}}{n^2}.
$$

三个整数带着清晰的意义涌现：$n$（主量子数，来自 Laguerre 可归一化性）确定能量；$\ell$（角量子数，来自 Legendre/球谐部分，$0\le\ell\le n-1$）确定轨道形状；$m$（磁量子数，$-\ell\le m\le\ell$，来自 $e^{im\phi}$ 因子）确定取向。能级 $n$ 上的态数为 $\sum_{\ell=0}^{n-1}(2\ell+1)=n^2$——这是与自旋一起构建出元素周期表的简并度。这些量子数中的每一个都是整数，原因*相同*：一个非整数会使某个特殊函数在某个奇点（原点或极点）处发散，违反波函数必须保持有限且可归一化的物理要求。

#### 例题

对基态 $n=1,\ell=0$：次数 $n-\ell-1=0$，故 $L_0^{(1)}=1$，且 $R_{10}\propto e^{-\rho/2}=e^{-r/a_0}$——$1s$ 轨道那简单的衰减指数，无径向节点（次数 $0\Rightarrow$ 无零点），与观测一致。对 $n=2,\ell=0$：次数 $1$，$L_1^{(1)}(\rho)=2-\rho$，故 $R_{20}\propto(2-\rho)e^{-\rho/2}$ 在 $\rho=2$ 处恰好有一个节点——$2s$ 轨道的那个单一径向节点。径向节点数就是 Laguerre 次数 $n-\ell-1$，这是你可以从多项式上直接读出的事实。

#### 陷阱

- $L_n^{(\alpha)}$ 的指标约定各异（有些作者平移 $n$ 或按 $n!$ 标度）；在信任一个公式之前，总要对照 $L_0=1$ 与微分方程加以核实。

## D 部分 · 统一的机制

<a id="s9"></a>
### 生成函数与递推关系

#### 是什么 & 为什么

**生成函数**是一个单一的闭式函数，其幂级数系数是一整个特殊函数家族。它是一个"压缩包"：一个表达式，按一个辅助变量 $t$ 的幂展开时，一举给出所有的 $P_\ell$、$H_n$ 或 $L_n$。对生成函数关于 $t$ 或 $x$ 求导，几乎机械地产生**递推关系**（每个函数用它的相邻者表示）与微分方程。本节展示这套机制运转的样子，让那些关系不再显得像魔法。

#### 推导示范 1：由生成函数得 Legendre 递推

设 $g(x,t)=(1-2xt+t^2)^{-1/2}=\sum_{\ell\ge0}P_\ell(x)t^\ell$。

1. 对 $g$ 关于 $t$ 求导。由链式法则，$\dfrac{\partial g}{\partial t}=-\tfrac12(1-2xt+t^2)^{-3/2}\cdot(-2x+2t)=\dfrac{x-t}{(1-2xt+t^2)^{3/2}}$。*（理由：对 $-1/2$ 次幂用链式法则。）*
2. 注意 $\dfrac{\partial g}{\partial t}=\dfrac{x-t}{1-2xt+t^2}\,g$，故 $(1-2xt+t^2)\dfrac{\partial g}{\partial t}=(x-t)\,g$。*（理由：代数重排，把一个幂的方括号并入 $g$。）*
3. 代入级数 $g=\sum P_\ell t^\ell$ 与 $\dfrac{\partial g}{\partial t}=\sum \ell P_\ell t^{\ell-1}$：
$$
(1-2xt+t^2)\sum_\ell \ell P_\ell t^{\ell-1}=(x-t)\sum_\ell P_\ell t^\ell.
$$
4. 展开两边并收集 $t^\ell$ 的系数。左边：$(\ell+1)P_{\ell+1}-2x\ell P_\ell+(\ell-1)P_{\ell-1}$。右边：$xP_\ell-P_{\ell-1}$。*（理由：移动指标使每一项都带 $t^\ell$；匹配系数，因为一个幂级数为零当且仅当所有系数消失。）*
5. 令两边相等并化简：
$$
(\ell+1)P_{\ell+1}(x)=(2\ell+1)\,x\,P_\ell(x)-\ell\,P_{\ell-1}(x).
$$
这就是 Legendre 三项递推（§s3 模板配上显式常数）。$\blacksquare$

**检验：** $\ell=1$ 给出 $2P_2=3xP_1-P_0=3x^2-1$，故 $P_2=\tfrac12(3x^2-1)$。与 §s4 吻合。

#### 推导示范 2：一个 Hermite 递推

对 $g(x,t)=e^{2xt-t^2}=\sum_n H_n\frac{t^n}{n!}$ 关于 $t$ 求导：$\partial_t g=(2x-2t)g$。
1. 左：$\sum_n H_n\frac{n t^{n-1}}{n!}=\sum_n H_n\frac{t^{n-1}}{(n-1)!}$。右：$(2x-2t)\sum_n H_n\frac{t^n}{n!}$。
2. 匹配 $\frac{t^n}{n!}$ 的系数：左给出 $H_{n+1}$，右给出 $2xH_n-2nH_{n-1}$。*（理由：对齐幂次；因子 $2t$ 降低一个指标并带下一个 $n$。）*
3. 因此 $H_{n+1}(x)=2x\,H_n(x)-2n\,H_{n-1}(x)$。检验 $n=1$：$H_2=2x\cdot2x-2\cdot1=4x^2-2$。正确。

改为关于 $x$ 求导给出 $\partial_x g=2t\,g$，它产生**导数关系** $H_n'(x)=2n\,H_{n-1}(x)$。两者合起来，一个递推与一条导数规则便让你能重建整个家族，甚至通过消去相邻者重新导出 Hermite 微分方程。

#### 推导示范 3：由这些关系重构 Hermite 方程

两个关系 $H_n'=2nH_{n-1}$ 与 $H_{n+1}=2xH_n-2nH_{n-1}$ 已经包含了那个微分方程：
1. 由第一个关系，$H_{n-1}=\tfrac{1}{2n}H_n'$，故递推变为 $H_{n+1}=2xH_n-H_n'$。
2. 再次对第一个关系求导并移动指标：$H_{n+1}'=2(n+1)H_n$，故 $H_n=\tfrac{1}{2(n+1)}H_{n+1}'$。对 $H_{n+1}=2xH_n-H_n'$ 求导得 $H_{n+1}'=2H_n+2xH_n'-H_n''$。
3. 把 $H_{n+1}'=2(n+1)H_n$ 代入第 2 步的最后一个方程：$2(n+1)H_n=2H_n+2xH_n'-H_n''$，即 $H_n''-2xH_n'+2nH_n=0$。*（理由：纯粹代入；指标的记账闭合了这个回路。）* 这就是 Hermite 方程——纯粹从递推机制中得到，从未触及原来的 Schrödinger 问题。

#### Laguerre 生成函数

为完整起见，连带 Laguerre 家族由下式打包

$$
\frac{1}{(1-t)^{\alpha+1}}\exp\!\Big(\frac{-xt}{1-t}\Big)=\sum_{n=0}^{\infty}L_n^{(\alpha)}(x)\,t^{n},\qquad |t|<1.
$$

对它关于 $t$ 求导并匹配幂次（与 Legendre 和 Hermite 相同的两步套路）便给出 Laguerre 三项递推 $(n+1)L_{n+1}^{(\alpha)}=(2n+\alpha+1-x)L_n^{(\alpha)}-(n+\alpha)L_{n-1}^{(\alpha)}$。要点正是这种一致性：*一套套路，三个家族。*

#### 统一的图景

每个经典家族都符合同一个模式：一个生成函数 $\Rightarrow$ 一次 $t$-求导给出三项递推，一次 $x$-求导给出一条阶梯（"导数 = 移位"）关系，而把两者结合便重构出那个二阶 ODE。这些递推也是数值库实际所计算的，因为攀爬一个稳定的递推远比对一个高次显式多项式求和更廉价、更精确。

为把"一套套路"这一论断彻底落到实处，这里给出通用配方，对任何带生成函数 $g(x,t)=\sum_n c_n(x)\,t^n$ 的家族都成立（其中 $c_n$ 是该家族，至多差一个已知的阶乘因子）：（1）求出 $\partial_t g$ 的闭式，并注意它等于 $g$ 乘以一个关于 $t$ 的有理函数；（2）清去分母使两边都是关于 $t$ 的多项式乘以级数；（3）代入 $g$ 与 $\partial_t g$ 的级数；（4）读出每边 $t^n$ 的系数并令其相等。第 1 步总能奏效，因为经典生成函数都是初等的（一个幂、一个指数或一个比值），所以它们的 $t$-导数是同一类对象乘以一个有理因子。第 4 步的输出总是一个三项递推，因为那个有理因子关于 $t$ 至多 $2$ 次，把每个 $c_n$ 至多耦合到两个相邻者——这就是抽象的 §s3 三项定理，如今从生成函数那一侧看到。同一个递推的两个独立证明（§s3 中的 Sturm–Liouville 结构与这里的生成函数代数）是一个好兆头，说明这结构是真实的，而非某一种方法的人为产物。

#### 陷阱

- 递推在某一方向上可能是数值*不稳定*的。对 Bessel 函数，按阶*向上*递推会放大误差；人们向下递推并重新归一化（Miller 算法）。知道这个关系并不等于知道该往哪个方向运行它。

<a id="s10"></a>
### 超几何函数：（几乎）一统天下的一个函数

#### 是什么 & 为什么

令人惊叹的是，Legendre、Hermite、Laguerre 与 Bessel 函数全都共享正交性、递推关系与 Rodrigues 公式。其深层原因在于它们几乎全是**单个函数的特例**：**超几何函数** $\,_2F_1$（及其合流表亲 $\,_1F_1$）。理解这一个对象便一举解释了它们的家族相似性。

#### Pochhammer 符号与级数

> **定义 —— 上升阶乘（Pochhammer 符号）。** 对 $k\ge1$，$(a)_k=a(a+1)(a+2)\cdots(a+k-1)$，且 $(a)_0=1$。等价地 $(a)_k=\Gamma(a+k)/\Gamma(a)$——又是 Gamma，把乘积打包。

> **定义 —— Gauss 超几何函数。**
> $$
> {}_2F_1(a,b;c;x)=\sum_{k=0}^{\infty}\frac{(a)_k\,(b)_k}{(c)_k}\,\frac{x^k}{k!}.
> $$

"超几何"这个名称意味着相继两项之比是 *$k$ 的有理函数*：$\dfrac{u_{k+1}}{u_k}=\dfrac{(a+k)(b+k)}{(c+k)(1+k)}\,x$。这一条单独的性质——把 Pochhammer 比值写出来一行即可核验——正是本指南中每一个特殊函数级数暗中所满足的。**合流**超几何函数 ${}_1F_1(a;c;x)=\sum_k\frac{(a)_k}{(c)_k}\frac{x^k}{k!}$ 是其中一个参数被送往无穷时的极限。

#### 这些家族如何作为特例出现

每个具名函数都是带特定参数与特定宗量的 ${}_2F_1$ 或 ${}_1F_1$：

- **Legendre：** $\displaystyle P_\ell(x)={}_2F_1\!\Big(-\ell,\,\ell+1;\,1;\,\tfrac{1-x}{2}\Big)$。第一个参数 $-\ell$ 为负整数，把级数截断成一个 $\ell$ 次多项式——这就是 $P_\ell$ *为什么*是多项式。
- **Laguerre：** $\displaystyle L_n^{(\alpha)}(x)=\binom{n+\alpha}{n}\,{}_1F_1(-n;\,\alpha+1;\,x)$。同样 $-n$ 截断了合流级数。
- **Hermite：** $\displaystyle H_{2m}(x)=(-1)^m\frac{(2m)!}{m!}\,{}_1F_1\!\big(-m;\tfrac12;x^2\big)$，奇次有类似公式。
- **Bessel：** $\displaystyle J_\nu(x)=\frac{(x/2)^\nu}{\Gamma(\nu+1)}\,{}_0F_1\!\big(;\nu+1;-\tfrac{x^2}{4}\big)$，是更进一步的合流极限 ${}_0F_1$。

机制是一致的：**一个负整数的分子参数使无穷级数终止**，把超越的 ${}_2F_1/{}_1F_1$ 变成多项式家族；否则（Bessel）便得到一个超越的整函数。

#### 例题：为什么 $-\ell$ 截断级数

取 Legendre 情形 ${}_2F_1(-\ell,\ell+1;1;u)$，令 $\ell=2$。Pochhammer 因子 $(-2)_k=(-2)(-1)(0)(1)\cdots$ 在 $k=2$ 处碰上一个**零**，因为 $(-2)_2=(-2)(-1)=2$ 但 $(-2)_3=(-2)(-1)(0)=0$，而后续每一项都带着那个零因子。*（理由：当 $a=-2$ 时，一旦 $k\ge3$，$(a)_k$ 就包含因子 $a+2=0$。）* 所以求和在 $k=0,1,2$ 之后停止：三项，一个关于 $u=\tfrac{1-x}{2}$ 的二次多项式，因而关于 $x$ 也是二次。写出来，${}_2F_1(-2,3;1;u)=1+\frac{(-2)(3)}{1}\,u+\frac{(-2)(-1)(3)(4)}{1\cdot2}\frac{u^2}{2!}=1-6u+6u^2$；代入 $u=\tfrac{1-x}{2}$ 得 $1-3(1-x)+\tfrac32(1-x)^2=\tfrac12(3x^2-1)=P_2(x)$。一般教训：多项式的*次数*等于那个负整数的大小，而它恰好就是特殊函数的指标 $\ell$（或 $n$）。

#### 为什么这是恰当的普遍性层次

超几何方程
$$
x(1-x)\,y''+\big[c-(a+b+1)x\big]\,y'-ab\,y=0
$$
是恰好有三个**正则奇点**（在 $0,1,\infty$）的最一般的二阶线性 ODE。本指南中的每个方程——Legendre、Hermite、Laguerre、Bessel——都是由它经过移动、合并或把奇点送往无穷（一个称为*合流*的过程）而得到的。

合流的故事值得详述，因为它正是这些家族在何种精确意义上"是同一个方程"。一个二阶线性 ODE 在很大程度上由其奇点*位于何处*以及它们*有多坏*所钉死：
- **Legendre** 是把超几何方程的三个正则奇点放在 $\pm1$ 与 $\infty$（对 $0,1,\infty$ 的一个 Möbius 重标）。没有合并；这就是为什么 $P_\ell$ 是一个普通的 ${}_2F_1$。
- **Laguerre / 合流超几何**出现于三个奇点中有两个*相撞*之时。把 $1$ 处的奇点推往无穷使它与已在那里的那个合并，留下一个正则奇点（在 $0$）与一个**非正则**奇点（在 $\infty$）。无穷处那个合并后强度更大的奇点正是产生 Laguerre 权中 $e^{-x}$ 因子的根源。
- **Hermite** 是合流方程的进一步改造（代入 $x\to x^2$ 并吸收因子），继承了无穷处同一个单一的非正则点，因而有 Gauss 因子 $e^{-x^2}$。
- **Bessel** 来自一个更深的合流（${}_0F_1$），那里无穷处的非正则点"更强"——这就是为什么 $J_\nu$ 振荡并像 $x^{-1/2}$ 那样衰减，而不是终止或保持多项式。

所以这些家族之间的差异——多项式还是振荡、哪个权、哪个区间——都是*奇点去了哪里、如何合并*的记账。所有这些函数共享正交性、递推关系与 Rodrigues 公式的那个"巧合"根本不是巧合：它们是*从不同视角看到的同一个方程*。这就是本学科最终的统一陈述——也是为什么一位掌握了一个特殊函数的物理学家，在某种精确意义上，已经把它们全都见过了。

#### 整个学科浓缩在一张卡片上

把所有家族都对照共同结构排开来看会有帮助。每一个都是某区间上某权 $w$ 的正交族，解一个 Sturm–Liouville 方程，有一个 Rodrigues 公式 $\frac{1}{e_n w}\frac{d^n}{dx^n}(w s^n)$、一个生成函数，以及在超几何体系中的一个位置：

- **Legendre** $P_\ell$：区间 $[-1,1]$，权 $1$，$s=x^2-1$；来自球面的极角；${}_2F_1$ 多项式。
- **连带 Legendre / 球谐函数** $P_\ell^m,Y_\ell^m$：同一区间但带 $\tfrac{m^2}{1-x^2}$ 项；来自整个球面；角动量的特征函数。
- **Bessel** $J_\nu$：区间 $[0,1]$（径向），权 $\rho$，来自柱面；${}_0F_1$，振荡且不终止。
- **Hermite** $H_n$：区间 $\mathbb R$，权 $e^{-x^2}$，$s=1$；来自抛物势阱；${}_1F_1$ 多项式。
- **Laguerre** $L_n^{(\alpha)}$：区间 $[0,\infty)$，权 $x^\alpha e^{-x}$，$s=x$；来自 Coulomb 径向问题；${}_1F_1$ 多项式。

沿任一列往下读，同一套机制反复出现；横跨任一行去读，你看到的是同一个物理问题。Gamma 函数（§s1）坐落在这一切之下，供给级数系数中的阶乘、归一化常数，以及超几何级数的 Pochhammer 符号。这就是整个学科的架构：四个 PDE、两个坐标系、一族方程，以及一个把那些常数维系在一起的连续阶乘。

#### 陷阱

- 级数 ${}_2F_1$ 对 $|x|<1$ 收敛；在该圆盘之外，该函数由解析延拓定义，而连接公式（联系在 $0$、$1$、$\infty$ 处的行为）才是真正微妙之处所在。多项式情形回避了这一点，因为一个终止的级数处处收敛。

---

*本指南从根源处构建了物理学的特殊函数：作为连续阶乘的 Gamma 函数及其 Beta 伴侣；正交多项式的一般理论——权、三项递推、Rodrigues 公式——然后是它在 Legendre 多项式与球谐函数（球面）、Bessel 函数（柱面）、Hermite 多项式（振子）与 Laguerre 多项式（氢原子）中的具体化身；驱动它们全体的生成函数与递推机制；最后是揭示它们乔装成一个家族的超几何函数。每一个正交性都从 Sturm–Liouville 结构证明，每一个级数都逐项导出，每一个公式都回溯到要求它的物理方程。自然的下一步是自伴算子的谱理论（它把"特征函数的正交基"变成一条定理）、这些函数在大宗量下的渐近分析，以及它们在求解电磁学与量子力学的偏微分方程中的日常使用。*
