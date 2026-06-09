[English](calculus-of-variations.md) · **中文**

# 变分法，*物理定律背后的原理。*

*一门自洽的变分法入门课程——从"哪条曲线使某个量最小？"这一问题出发，直到欧拉–拉格朗日方程、哈密顿原理、诺特定理与场论。每个术语都用文字定义，每条公式都给出动机，每步推导都是一条编号、无缝隙的推理链。本课程建立在基础代数与单变量微积分之上；与力学、微分几何之间的桥梁都被明确指出。*

[← 返回全部指南](../README.zh.md)

## A 部分 · 背景设定

<a id="s0"></a>
### 动机：最小作用量、最速降线、测地线

#### 一口气说清本指南讲什么

普通微积分问的是：在所有*数* $x$ 中，哪一个使函数 $f(x)$ 最小？你通过令 $f'(x)=0$ 来回答。变分法问的是一个更丰富的问题：在所有连接两点的*曲线*（或函数）中，哪一条使某个总量——长度、时间或能量——最小？物理学令人惊叹的发现是：自然本身正是在回答这样的问题——一大批物理定律都可以写成"真实的路径是使某个积分取驻值的那一条"。本指南建立使这一陈述精确化的数学，随后展示它如何生成牛顿定律、守恒律与场方程。

#### 三个引出动机的问题

- **最小作用量原理。** 在重力作用下运动的质点、绕太阳公转的行星、穿过玻璃而弯折的一束光——每一个都沿着使某个称为**作用量**的量取驻值（往往是极小值）的路径运动。我们不再用力一步一步地推动质点，而是一次性把整段旅程交给它，问哪一段旅程是"最优的"。这是物理学中最深刻的组织性思想，而它是一个变分问题。

- **最速降线**（希腊语："最短时间"）。由约翰·伯努利于 1696 年提出：一颗珠子在无摩擦的情形下沿一根钢丝从点 $A$ 滑到一个并不在其正下方的较低点 $B$。在所有可能的钢丝形状中，哪一种使珠子从 $A$ 到 $B$ 所用*时间最短*？直线并不是答案；答案是一段**摆线**（滚动的轮子上一点所描出的曲线）的弧。我们在 §s3 中完整求解此问题。

- **测地线。** 两点之间最短的路径是什么？在平坦的平面上它是一条直线；在球面上它是一段大圆弧（这就是为何飞越太平洋的飞机看起来会向北偏）。**测地线**是曲面上"尽可能笔直"的曲线，求它依旧是一个使总长度最小化的问题。我们在 §s6 中处理此问题。

#### 它们的共同之处

在每一情形中，未知的都是一个**函数**——曲线的形状 $y(x)$——而要最小化的量是**由这整个函数沿曲线积分计算出的一个数**：一个时间、一个长度、一个能量。一条吃进一个函数并返回单个数的法则称为**泛函**。变分法就是泛函的微积分：它给出泛函版本的"令导数为零"，而这个版本就是**欧拉–拉格朗日方程**（§s2）。

#### 一句话概括整本指南

> 泛函 → 一阶变分 → 欧拉–拉格朗日方程 → 求解曲线实例 → 场与约束 → 测地线 → 力学（哈密顿）→ 诺特 → 哈密顿形式 → 经典场

#### 常见陷阱

- "驻值"与"极小值"不是一回事。令一阶变分为零找到的是*驻*点；它们可能是极小、极大或鞍点状的。我们在 §s2 中讨论这一点。
- 未知的是*整个函数*，而非它在某一点的值。你无法通过优化珠子在某个单独 $x$ 处的高度来求解最速降线；曲线在每一点的值都通过斜率 $y'$ 与其邻点耦合在一起。

<a id="s1"></a>
### 泛函与变分；泛函导数

#### 是什么以及为什么

为模仿普通微积分，我们需要三种要素：一个待优化的对象（这里是泛函）、一个"移动一点点"的概念（这里是函数的*变分*），以及一个"变化率"的概念（这里是*一阶变分*，即导数的泛函类比）。本节小心地定义这三者，使得 §s2 中的推导没有任何缝隙。

#### 从零定义每个术语

- 一个**函数** $y(x)$ 接受一个数 $x$ 并返回一个数 $y$。一个**光滑**函数是指可以按我们需要的任意次数求导的函数（这里至少二阶连续可微）；我们记 $y\in C^2[a,b]$ 表示在闭区间 $[a,b]$ 上二阶连续可微的函数。
- 一个**泛函** $J$ 是一条法则，它把整个函数 $y$ 作为输入并返回单个实数 $J[y]$。我们用方括号 $J[y]$ 来强调输入是一个函数而非一个数。*例：* $y$ 在 $[a,b]$ 上的图像长度就是泛函 $L[y]=\int_a^b\sqrt{1+y'(x)^2}\,dx$（在 §s3 中导出）。

> **定义 — 标准泛函**
>
> 贯穿本指南的核心对象是
>
> $$
> J[y]=\int_a^b L\big(x,\,y(x),\,y'(x)\big)\,dx .
> $$
>
> 这里 $a<b$ 是固定的数，$y$ 取遍 $[a,b]$ 上的光滑函数，而 $L(x,y,y')$ ——**拉格朗日量**（或**被积函数**）——是关于*三个独立位置*的一个给定光滑函数：位置 $x$、值 $y$ 和斜率 $y'$。为计算 $J[y]$，你在每个 $x$ 处把曲线的值和斜率代入 $L$ 并沿区间累加（积分）。

一个关键的微妙之处：当我们对 $L$ 求导时，它被当作三个*独立*变量 $x, y, y'$ 的函数。符号 $\partial L/\partial y$ 与 $\partial L/\partial y'$ 意为"在固定另外两个位置的情况下对 $L$ 求导"。只有在求出这些偏导数*之后*，我们才记起：沿一条真实曲线，$y$ 和 $y'$ 都是 $x$ 的函数。

#### 容许函数与固定端点

我们在**容许函数**上进行优化：即 $[a,b]$ 上经过指定端点的光滑函数，
$$
y(a)=y_a,\qquad y(b)=y_b ,
$$
其中 $y_a,y_b$ 是给定的数。（最速降线的钢丝被钉在 $A$ 和 $B$ 处。）正是这个边界条件使问题确定，而它也恰恰是下面推导中消去某些项的原因。

#### 对函数作变分

为了探查某条特定曲线 $y$ 是否最优，我们对它作微扰。任取一个光滑函数 $\eta(x)$ ——即**变分方向**——它在*端点处取零*：
$$
\eta(a)=0,\qquad \eta(b)=0 .
$$
这最后一项要求保证被微扰的曲线仍然经过同样的端点，因而它保持容许。现在构造一族单参数的竞争曲线
$$
y_\varepsilon(x)=y(x)+\varepsilon\,\eta(x),
$$
其中 $\varepsilon$ 是一个小实数。在 $\varepsilon=0$ 时我们恢复到 $y$；随着 $\varepsilon$ 增大，我们沿方向 $\eta$ 偏离开来。量 $\delta y:=\varepsilon\eta$ 称为 **$y$ 的变分**——*整个函数*的无穷小改变，即普通微积分中小步长 $\Delta x$ 的类比。

#### 一阶变分：把泛函问题化为微积分问题

把这一族代入 $J$，你便得到关于单个数 $\varepsilon$ 的一个普通函数：
$$
\Phi(\varepsilon):=J[y+\varepsilon\eta]=\int_a^b L\big(x,\,y+\varepsilon\eta,\,y'+\varepsilon\eta'\big)\,dx .
$$
这是整个学科的核心技巧：通过沿单一方向 $\eta$ 滑动，我们把一个无穷维问题（在所有函数上优化）坍缩为一个一维问题（在数 $\varepsilon$ 上优化 $\Phi$），后者由普通微积分处理。

> **定义 — 一阶变分**
>
> $J$ 在 $y$ 处沿方向 $\eta$ 的**一阶变分**为
>
> $$
> \delta J[y;\eta]:=\left.\frac{d}{d\varepsilon}\right|_{\varepsilon=0}J[y+\varepsilon\eta]=\Phi'(0).
> $$
>
> 它是泛函的方向导数——当我们开始沿方向 $\eta$ 移动曲线时 $J$ 变化的快慢。

> **定义 — 驻定（极值）函数**
>
> 若对*每一个*容许方向一阶变分都为零，则称函数 $y$ 对 $J$ 是**驻定的**（并称为**极值曲线**）：
>
> $$
> \delta J[y;\eta]=0\quad\text{for all smooth }\eta\text{ with }\eta(a)=\eta(b)=0 .
> $$
>
> 这正是 $f'(x)=0$ 的精确类比：真正的极小或极大必定是驻定的，因为若对某个 $\eta$ 有 $\Phi'(0)\neq0$，那么沿 $+\eta$ 或 $-\eta$ 移动一点点便会严格减小 $J$，于是 $y$ 不可能是最优的。

#### 泛函导数

当我们把一阶变分写成
$$
\delta J[y;\eta]=\int_a^b \frac{\delta J}{\delta y}(x)\,\eta(x)\,dx ,
$$
的形式时，乘在 $\eta$ 上的函数 $\dfrac{\delta J}{\delta y}(x)$ 称为 $J$ 的**泛函导数**。它是梯度的连续类比：普通函数的梯度是一个由偏导数组成的*向量*（每个坐标一个数），而泛函导数是一个*函数*（每个点 $x$ 一个数）。驻定性是说这整个函数为零——而 §s2 表明泛函导数恰好就是欧拉–拉格朗日方程的左边。

#### 求解实例 — 长度泛函的一阶变分

取 $L=\sqrt{1+y'^2}$，于是 $J[y]=\int_a^b\sqrt{1+y'^2}\,dx$（图像长度）。
1. 构造 $\Phi(\varepsilon)=\int_a^b\sqrt{1+(y'+\varepsilon\eta')^2}\,dx$。*理由：* 因 $\frac{d}{dx}(y+\varepsilon\eta)=y'+\varepsilon\eta'$，故把 $y'$ 换成 $y'+\varepsilon\eta'$。
2. 在积分号下求导（之所以允许，是因为被积函数在有限区间上关于 $\varepsilon$ 光滑）：由对 $\sqrt{\,\cdot\,}$ 用链式法则，$\Phi'(\varepsilon)=\int_a^b \frac{(y'+\varepsilon\eta')\,\eta'}{\sqrt{1+(y'+\varepsilon\eta')^2}}\,dx$。
3. 令 $\varepsilon=0$：$\displaystyle \delta J[y;\eta]=\int_a^b \frac{y'\,\eta'}{\sqrt{1+y'^2}}\,dx.$
这就是一阶变分；在 §s3 中我们令它为零并发现直线。

#### 常见陷阱

- $\eta$ 必须在端点处取零；否则竞争曲线离开容许集合，而 §s2 中的边界项就不会消去。
- $\delta J=0$ 检测的是*驻定性*，而非极小性。确认真正的极小需要一个"二阶变分"检验，即 $f''>0$ 的类比，我们仅提及而不展开。

## B 部分 · 基本方程

<a id="s2"></a>
### 欧拉–拉格朗日方程：完整推导

#### 是什么以及为什么

驻定性，即对所有 $\eta$ 都有 $\delta J[y;\eta]=0$，是一个必须对*无穷多个*方向 $\eta$ 成立的方程。这很笨重。欧拉–拉格朗日方程把"对所有 $\eta$ 成立"重新打包成关于 $y$ 本身的单个微分方程——它是整个学科的主力。我们无缝隙地导出它，包括为最后一步提供依据的引理。

#### 第 1 步 — 一般地计算一阶变分

1. 从 $\Phi(\varepsilon)=\displaystyle\int_a^b L\big(x,\,y+\varepsilon\eta,\,y'+\varepsilon\eta'\big)\,dx$ 出发。
2. 在积分号下求导（被积函数关于 $\varepsilon$ 光滑且区间有限，故求导与积分可交换次序）：
   $$
   \Phi'(\varepsilon)=\int_a^b\left[\frac{\partial L}{\partial y}\,\eta+\frac{\partial L}{\partial y'}\,\eta'\right]dx .
   $$
   *理由：* 多元函数的链式法则。当 $\varepsilon$ 改变时，$L$ 的第二个位置以速率 $\eta$ 改变，第三个位置以速率 $\eta'$ 改变；把每一项乘以对应的偏导数并相加。
3. 令 $\varepsilon=0$，于是这些偏导数沿曲线 $y$ 本身求值：
   $$
   \delta J[y;\eta]=\int_a^b\left[\frac{\partial L}{\partial y}\,\eta+\frac{\partial L}{\partial y'}\,\eta'\right]dx .
   $$

#### 第 2 步 — 对那个麻烦的项作分部积分

含 $\eta'$ 的项把 $\eta$ 的自由度藏在一个导数里面；我们把导数从 $\eta$ 上移开并转到系数上。
4. 回顾**分部积分**：$\int_a^b u\,v'\,dx=\big[u v\big]_a^b-\int_a^b u'\,v\,dx$，对 $C^1$ 函数成立（它是乘积法则 $(uv)'=u'v+uv'$ 积分而来）。取 $u=\dfrac{\partial L}{\partial y'}$，$v=\eta$（于是 $v'=\eta'$）：
   $$
   \int_a^b \frac{\partial L}{\partial y'}\,\eta'\,dx=\left[\frac{\partial L}{\partial y'}\,\eta\right]_a^b-\int_a^b \frac{d}{dx}\!\left(\frac{\partial L}{\partial y'}\right)\eta\,dx .
   $$
5. 边界项消失：$\big[\frac{\partial L}{\partial y'}\eta\big]_a^b=\frac{\partial L}{\partial y'}(b)\,\eta(b)-\frac{\partial L}{\partial y'}(a)\,\eta(a)=0$，*这是因为* 由变分的容许性条件有 $\eta(a)=\eta(b)=0$。正是在这里，固定端点的要求发挥了作用。

#### 第 3 步 — 整理并应用基本引理

6. 把第 5 步代回第 3 步：
   $$
   \delta J[y;\eta]=\int_a^b\left[\frac{\partial L}{\partial y}-\frac{d}{dx}\!\left(\frac{\partial L}{\partial y'}\right)\right]\eta\,dx .
   $$
   方括号中不再含 $\eta'$；变分的全部自由度现在都落在单个因子 $\eta$ 上。这个方括号就是 §s1 中所承诺的**泛函导数** $\dfrac{\delta J}{\delta y}$。
7. 驻定性要求这个积分对*每一个*容许的 $\eta$ 都为零。为得出方括号本身必定为零的结论，我们需要：

> **引理 — 变分法基本引理**
>
> 设 $g$ 是 $[a,b]$ 上的连续函数。若对**每一个**满足 $\eta(a)=\eta(b)=0$ 的 $C^1$ 检验函数 $\eta$ 都有 $\displaystyle\int_a^b g(x)\,\eta(x)\,dx=0$，则对一切 $x\in[a,b]$ 有 $g(x)=0$。（只要求 $C^1$ 检验函数使引理更易应用——下面那个显式凸起就是 $C^1$ 的——而这对 $C^2$ 的欧拉–拉格朗日理论已经足够，因为对更小的 $C^1$ 凸起类积分为零就已迫使 $g\equiv0$；从而对一切光滑的 $\eta$ 它也为零。）

*引理的证明（反证法）。*
1. 假设 $g$ 不恒为零。那么存在一点 $c\in(a,b)$ 使 $g(c)\neq0$；设 $g(c)>0$（若 $g(c)<0$ 则把 $g$ 换成 $-g$）。
2. 由于 $g$ 连续，存在一个小区间 $[c-\rho,\,c+\rho]\subset(a,b)$，在其上 $g(x)>\tfrac12 g(c)>0$。*理由：* 连续性意味着 $c$ 附近的值仍接近 $g(c)$；取容差 $\tfrac12 g(c)$ 即可。
3. 构造一个在该区间上为正、在区间外为零的"凸包"检验函数：令
   $$
   \eta(x)=\begin{cases}\big[(x-(c-\rho))(\,(c+\rho)-x)\big]^2,& x\in[c-\rho,c+\rho],\\[2pt]0,&\text{otherwise.}\end{cases}
   $$
   这个 $\eta$ 是 $C^1$ 的（在接合处平方因子及其一阶导数都为零，故 $\eta$ 与 $\eta'$ 都与零的那一段相接；它在该处不是 $C^2$，但 $C^1$ 正是引理现在的假设所要求的全部），满足 $\eta(a)=\eta(b)=0$，处处 $\ge0$，且在开区间 $(c-\rho,c+\rho)$ 上严格 $>0$。
4. 于是 $\int_a^b g\,\eta\,dx=\int_{c-\rho}^{c+\rho} g\,\eta\,dx>0$，因为被积函数在一个正长度集合上是两个正量之积、在别处为零。（一个在某区间上为正的连续函数的积分是正的。）
5. 这与"该积分对*每一个*这样的 $\eta$ 都为零"的假设矛盾。因此不存在这样的 $c$，故 $g\equiv0$。$\blacksquare$

8. 取 $g=\dfrac{\partial L}{\partial y}-\dfrac{d}{dx}\big(\dfrac{\partial L}{\partial y'}\big)$ 应用该引理，得到结果：

> **定理 — 欧拉–拉格朗日方程**
>
> 若 $y$ 是 $J[y]=\int_a^b L(x,y,y')\,dx$ 在固定端点的容许函数上的驻定函数（极值曲线），则 $y$ 满足
>
> $$
> \frac{\partial L}{\partial y}-\frac{d}{dx}\!\left(\frac{\partial L}{\partial y'}\right)=0 .
> $$
>
> 这是关于 $y$ 的一个（通常为二阶的）常微分方程。它的解就是候选的最优者。

#### 仔细解读这些符号

在 $\dfrac{d}{dx}\big(\dfrac{\partial L}{\partial y'}\big)$ 中，内层的 $\partial L/\partial y'$ 是 $x,y,y'$ 的函数；外层的 $d/dx$ 是一个**全**导数，由链式法则它既计入 $x$ 的直接变化，*也*计入通过 $y(x)$ 与 $y'(x)$ 的变化：
$$
\frac{d}{dx}\frac{\partial L}{\partial y'}=\frac{\partial^2 L}{\partial x\,\partial y'}+\frac{\partial^2 L}{\partial y\,\partial y'}\,y'+\frac{\partial^2 L}{\partial y'^2}\,y'' .
$$
$y''$ 的出现表明该方程一般是二阶的。

#### 贝尔特拉米恒等式 —— 当 $L$ 不显含 $x$ 时的一个免费首次积分

若 $L$ 不显含 $x$（即 $\partial L/\partial x=0$），欧拉–拉格朗日方程便有一个即得的首次积分，往往远更易于求解。
1. 计算 $L$ 沿曲线的全导数：$\dfrac{dL}{dx}=\dfrac{\partial L}{\partial x}+\dfrac{\partial L}{\partial y}y'+\dfrac{\partial L}{\partial y'}y''$（链式法则）。
2. 计算 $\dfrac{d}{dx}\!\Big(y'\dfrac{\partial L}{\partial y'}\Big)=y''\dfrac{\partial L}{\partial y'}+y'\dfrac{d}{dx}\dfrac{\partial L}{\partial y'}$（乘积法则）。
3. 相减：$\dfrac{dL}{dx}-\dfrac{d}{dx}\!\Big(y'\dfrac{\partial L}{\partial y'}\Big)=\dfrac{\partial L}{\partial x}+y'\Big[\dfrac{\partial L}{\partial y}-\dfrac{d}{dx}\dfrac{\partial L}{\partial y'}\Big].$
4. 在极值曲线上方括号为零（欧拉–拉格朗日）。若又有 $\partial L/\partial x=0$，则右边为零，于是左边是某个常数的导数：

> **贝尔特拉米恒等式**（当 $\partial L/\partial x=0$ 时成立）：
>
> $$
> L-y'\,\frac{\partial L}{\partial y'}=\text{constant}.
> $$

这是能量守恒（§s8）的变分祖先。

#### 常见陷阱

- $\partial L/\partial y'$ 的意思是把 $y'$ 当作一个独立符号来对 $L$ 求导；只有之后你才对所得结果沿曲线取 $d/dx$。混淆这两种次序是最常见的错误。
- 欧拉–拉格朗日方程对极值而言是*必要*的，但并非*充分*；和 $f'=0$ 一样，它也可能标出鞍点。

## C 部分 · 求解曲线实例

<a id="s3"></a>
### 求解实例：最短路径、最速降线、最小旋转曲面

#### 例 1 — 平面上的最短路径是一条直线

我们严格地证明这一"显然"的事实，以见机器运作。
1. **建立泛函。** 从 $(a,y_a)$ 到 $(b,y_b)$ 的曲线 $y(x)$ 的弧长为 $L[y]=\int_a^b\sqrt{1+y'^2}\,dx$。*理由：* 图像的一个无穷小片段有水平增量 $dx$ 和竖直增量 $dy=y'\,dx$，故由勾股定理其长度为 $\sqrt{dx^2+dy^2}=\sqrt{1+y'^2}\,dx$；积分即把这些片段相加。
2. **辨认 $L$。** 这里 $L=\sqrt{1+y'^2}$ 只依赖于 $y'$，故 $\partial L/\partial y=0$ 且 $\dfrac{\partial L}{\partial y'}=\dfrac{y'}{\sqrt{1+y'^2}}$（对平方根用链式法则）。
3. **欧拉–拉格朗日。** 因 $\partial L/\partial y=0$，方程化为 $\dfrac{d}{dx}\dfrac{y'}{\sqrt{1+y'^2}}=0$，故 $\dfrac{y'}{\sqrt{1+y'^2}}=c$（一个常数）。
4. **解出斜率。** 平方后，$y'^2=c^2(1+y'^2)\Rightarrow y'^2(1-c^2)=c^2\Rightarrow y'=\dfrac{c}{\sqrt{1-c^2}}=:m$，一个常数。
5. **积分。** $y=mx+k$：一条直线。两个常数 $m,k$ 由端点确定。最短路径是这段直线，如今是被*导出*的，而非假设的。

#### 例 2 — 最速降线是一条摆线

1. **建立时间泛函。** 让珠子从 $A=(0,0)$ 落下，$y$ *向下*量度为正，落向 $B$。能量守恒给出下落高度 $y$ 后的速率 $v=\sqrt{2gy}$（动能 $\tfrac12 mv^2$ 等于损失的势能 $mgy$，故 $v=\sqrt{2gy}$）。以速率 $v$ 走过弧长 $ds=\sqrt{1+y'^2}\,dx$ 所需的时间为 $dt=ds/v$，故总下降时间为
   $$
   T[y]=\int_0^{x_B}\frac{\sqrt{1+y'^2}}{\sqrt{2gy}}\,dx .
   $$
2. **辨认 $L$。** $L=\dfrac{\sqrt{1+y'^2}}{\sqrt{2gy}}$ *不显含 $x$*，故**贝尔特拉米恒等式**适用。
3. **应用贝尔特拉米。** 计算 $\dfrac{\partial L}{\partial y'}=\dfrac{1}{\sqrt{2gy}}\cdot\dfrac{y'}{\sqrt{1+y'^2}}$，然后
   $$
   L-y'\frac{\partial L}{\partial y'}=\frac{1}{\sqrt{2gy}}\left[\sqrt{1+y'^2}-\frac{y'^2}{\sqrt{1+y'^2}}\right]=\frac{1}{\sqrt{2gy}}\cdot\frac{1}{\sqrt{1+y'^2}}=\text{const}.
   $$
   *理由：* 通分到公分母 $\sqrt{1+y'^2}$；分子 $\,(1+y'^2)-y'^2=1$。
4. **化为常微分方程。** 平方并吸收常数后，$y\,(1+y'^2)=C$，其中常数 $C=2R$。这是**摆线**的定义微分方程。
5. **用参数求解。** 之所以选代换 $y'=\cot(\theta/2)$，是为了让讨厌的因子 $1+y'^2$ 借毕达哥拉斯恒等式坍缩：$1+y'^2=1+\cot^2(\theta/2)=\csc^2(\theta/2)$，正是它使下面的代数闭合。借此，$y=\dfrac{C}{\csc^2(\theta/2)}=C\sin^2(\theta/2)=\tfrac{C}{2}(1-\cos\theta)=R(1-\cos\theta)$，这里用了半角恒等式 $\sin^2(\theta/2)=\tfrac12(1-\cos\theta)$。现在由 $dx=dy/y'$ 积分来恢复 $x$。对 $y=R(1-\cos\theta)$ 求导得 $dy=R\sin\theta\,d\theta$，于是
   $$
   dx=\frac{dy}{y'}=\frac{R\sin\theta\,d\theta}{\cot(\theta/2)}=R\sin\theta\,\tan(\theta/2)\,d\theta.
   $$
   半角化简 $\sin\theta=2\sin(\theta/2)\cos(\theta/2)$ 把 $\sin\theta\,\tan(\theta/2)=2\sin^2(\theta/2)=1-\cos\theta$，所以 $dx=R(1-\cos\theta)\,d\theta$。积分（取 $\theta=0$ 时 $x=0$）得 $x=R(\theta-\sin\theta)$。
   $$
   x=R(\theta-\sin\theta),\qquad y=R(1-\cos\theta).
   $$
   这恰好是摆线的参数方程——一个半径为 $R$ 的圆沿一条直线滚动时其上一点所描出的曲线。因此最快下降曲线是一段摆线的弧，其中 $R$ 取得使曲线通过 $B$。

#### 例 3 — 最小旋转曲面是一个悬链面

把一条曲线 $y(x)\ge0$ 绕 $x$ 轴旋转；所得曲面（设想两个圆环之间的肥皂膜）的面积为 $S[y]=\int_a^b 2\pi y\sqrt{1+y'^2}\,dx$（每一条带是一个半径为 $y$、斜宽为 $\sqrt{1+y'^2}\,dx$ 的环带）。我们最小化 $S$。
1. **辨认 $L$。** 丢掉常数 $2\pi$：$L=y\sqrt{1+y'^2}$，同样不显含 $x$，故用**贝尔特拉米**。
2. **应用贝尔特拉米。** $\dfrac{\partial L}{\partial y'}=\dfrac{y\,y'}{\sqrt{1+y'^2}}$，且
   $$
   y\sqrt{1+y'^2}-y'\cdot\frac{y\,y'}{\sqrt{1+y'^2}}=\frac{y}{\sqrt{1+y'^2}}=c .
   $$
3. **求解。** 于是 $y=c\sqrt{1+y'^2}$，即 $y'=\sqrt{(y/c)^2-1}$。分离变量，$\displaystyle\int\frac{dy}{\sqrt{(y/c)^2-1}}=\int dx$ 给出 $c\,\mathrm{arccosh}(y/c)=x-x_0$，因此
   $$
   y=c\,\cosh\!\frac{x-x_0}{c}.
   $$
   这是一条**悬链线**，它扫出的曲面是一个**悬链面**——两个同轴圆环之间肥皂膜实际所取的形状。

#### 一个具体的数

对例 1 取 $A=(0,0)$，$B=(3,4)$：第 4 步给出 $m=(4-0)/(3-0)=4/3$，$k=0$，故 $y=\tfrac{4}{3}x$，长度为 $\int_0^3\sqrt{1+16/9}\,dx=\int_0^3\tfrac{5}{3}\,dx=5$ ——即勾股定理斜边 $\sqrt{3^2+4^2}=5$。变分方法重现了初等几何，这是一个合理性检验。

#### 常见陷阱

- 在最速降线中，把 $y$ 向上量度会翻转一个符号并隐藏摆线；选取"向下为正"使 $v=\sqrt{2gy}$ 为实数。
- 当两个圆环离得太远时，最小曲面问题可能没有光滑解（膜会断裂成两个圆盘）；欧拉–拉格朗日方程找到一个候选者，但存在性仍需检验。

## D 部分 · 推广

<a id="s4"></a>
### 多个函数与多个自变量（场）

#### 多个未知函数

一个状态常常同时由一个变量的*多个*函数来描述——例如一个质点的三个坐标 $y_1(x),y_2(x),y_3(x)$ 作为时间 $x$ 的函数。泛函变为
$$
J[y_1,\dots,y_n]=\int_a^b L\big(x,\,y_1,\dots,y_n,\,y_1',\dots,y_n'\big)\,dx .
$$
一次对一个函数 $y_k$ 作变分，使用一个独立的凸包 $\eta_k$（其余保持固定）。每个变分都必须独立地为零，故对每个下标重复一次 §s2 的推导，便得到一个欧拉–拉格朗日方程**组**：
$$
\frac{\partial L}{\partial y_k}-\frac{d}{dx}\!\left(\frac{\partial L}{\partial y_k'}\right)=0,\qquad k=1,\dots,n .
$$
1. 固定所有 $y_j$（$j\neq k$），并令 $y_k\to y_k+\varepsilon\eta_k$，其中 $\eta_k(a)=\eta_k(b)=0$。
2. 沿此方向的一阶变分为 $\int_a^b\big[\partial L/\partial y_k-\frac{d}{dx}(\partial L/\partial y_k')\big]\eta_k\,dx$，与 §s2 中完全一样，因为只有第 $k$ 个位置在变动。
3. 基本引理迫使方括号为零。由于 $k$ 是任意的，故全部 $n$ 个方程成立。*独立处理它们的理由：* 凸包 $\eta_k$ 可以一次取一个，故沿每个方向的驻定性是一个独立的条件。

#### 多个自变量 —— 场

现在让未知量是*多个*输入的函数，$u(x_1,\dots,x_m)$ ——一个**场**，例如一根振动弦在位置 $x$、时间 $t$ 处的高度 $u(x,t)$。积分在一个区域 $\Omega$ 上进行，而被积函数依赖于 $u$ 及其偏导数 $u_{x_i}=\partial u/\partial x_i$：
$$
J[u]=\int_\Omega L\big(x_i,\,u,\,u_{x_1},\dots,u_{x_m}\big)\,dx_1\cdots dx_m .
$$
作变分 $u\to u+\varepsilon\eta$，其中 $\eta$ 在边界 $\partial\Omega$ 上为零。一阶变分为
$$
\delta J=\int_\Omega\left[\frac{\partial L}{\partial u}\,\eta+\sum_{i=1}^m\frac{\partial L}{\partial u_{x_i}}\,\eta_{x_i}\right]dx .
$$
对第二组项作多变量的分部积分：**散度定理**把 $\int_\Omega (\partial L/\partial u_{x_i})\,\eta_{x_i}\,dx$ 化为一个边界积分（它消失，因为 $\eta=0$ 于 $\partial\Omega$ 上）减去 $\int_\Omega \frac{\partial}{\partial x_i}(\partial L/\partial u_{x_i})\,\eta\,dx$。整理并应用多变量基本引理给出：

> **场的欧拉–拉格朗日方程**
>
> $$
> \frac{\partial L}{\partial u}-\sum_{i=1}^m\frac{\partial}{\partial x_i}\!\left(\frac{\partial L}{\partial u_{x_i}}\right)=0 .
> $$

这个单一方程是经典场论（§s10）的引擎。

#### 求解实例 — 振动弦

取 $u(x,t)$ 和 $L=\tfrac12\rho\,u_t^2-\tfrac12\tau\,u_x^2$（动能减去弹性能量密度；$\rho$ = 单位长度质量，$\tau$ = 张力），计算 $\partial L/\partial u=0$，$\partial L/\partial u_t=\rho u_t$，$\partial L/\partial u_x=-\tau u_x$。场方程给出 $0-\big[\partial_t(\rho u_t)+\partial_x(-\tau u_x)\big]=0$，即
$$
\rho\,u_{tt}=\tau\,u_{xx},
$$
即**波动方程**，波速为 $\sqrt{\tau/\rho}$。弦的动力学直接从一个变分原理中掉了出来。

#### 常见陷阱

- 有多个变量时，你必须在*每一个*导数位置作分部积分，并丢弃*每一个*边界项；漏掉一个就会破坏方程。
- 求导时把 $u$ 和每个 $u_{x_i}$ 当作 $L$ 的独立位置，与之前对 $y,y'$ 的处理完全一样。

<a id="s5"></a>
### 约束：拉格朗日乘子与等周问题

#### 是什么以及为什么

实际问题常常在*另一个泛函被固定*的条件下优化一个泛函：在固定体积下最小化面积，在固定长度下最小化能量。所用工具是来自普通多元微积分的同一个**拉格朗日乘子**思想，提升到泛函上。

#### 回顾（一行）

在普通微积分中，要在 $g=$ 常数的约束下使 $f$ 取极值，可对一个数 $\lambda$ 求解 $\nabla f=\lambda\nabla g$：在约束极值处，目标函数的梯度平行于约束的梯度。

#### 变分版本

要在**等周约束** $K[y]=\int_a^b G\,dx=\ell$（一个固定的数）下使 $J[y]=\int_a^b L\,dx$ 取极值，引入一个常数**乘子** $\lambda$ 并自由地使组合泛函 $J-\lambda K$ 取极值：

> **定理。** $J$ 在约束 $K=\ell$ 下的极值曲线满足 $L-\lambda G$ 的欧拉–拉格朗日方程：
>
> $$
> \frac{\partial(L-\lambda G)}{\partial y}-\frac{d}{dx}\frac{\partial(L-\lambda G)}{\partial y'}=0 ,
> $$
>
> 其中 $\lambda$ 为某个常数，它与积分常数一道由端点和约束 $K=\ell$ 共同确定。

*为何这样有效（带理由的概述）。* 容许变分必须使 $K$ 保持一阶固定，即 $\delta K=0$，故 $\eta$ 不再自由——它被限制在与约束相切的方向上。由普通拉格朗日乘子背后那个相同的线性代数事实，条件"对所有满足 $\delta K=0$ 的 $\eta$ 都有 $\delta J=0$"等价于"对某个常数 $\lambda$ 和*所有* $\eta$ 都有 $\delta J=\lambda\,\delta K$"，即 $\delta(J-\lambda K)=0$。于是 §s2 的无约束推导便适用于 $L-\lambda G$。

#### 求解实例 — 悬挂的链条（悬链线）

一条*固定长度* $\ell$ 的均匀柔性链条挂在两根柱子之间；它会安定为**势能最低**的形状。我们来导出这个形状。
1. **目标。** 势能是（质量密度）$\times g\times$（高度）的累加：$J[y]=\int_a^b \rho g\,y\,\sqrt{1+y'^2}\,dx$（因子 $\sqrt{1+y'^2}\,dx$ 是一段的弧长，它携带质量 $\rho\,ds$ 处于高度 $y$）。丢掉常数 $\rho g$。
2. **约束。** 链条的长度固定：$K[y]=\int_a^b\sqrt{1+y'^2}\,dx=\ell$。
3. **组合。** 使 $L-\lambda G$ 取极值，其中 $L-\lambda G=(y-\lambda)\sqrt{1+y'^2}$。不显含 $x$，故用**贝尔特拉米**：
   $$
   (y-\lambda)\sqrt{1+y'^2}-y'\frac{(y-\lambda)y'}{\sqrt{1+y'^2}}=\frac{y-\lambda}{\sqrt{1+y'^2}}=c .
   $$
4. **求解。** 这是 §s3 的悬链面方程平移了 $\lambda$：$y-\lambda=c\cosh\frac{x-x_0}{c}$，即
   $$
   y=\lambda+c\,\cosh\!\frac{x-x_0}{c}.
   $$
   悬挂的链条是一条**悬链线**。常数 $\lambda,c,x_0$ 由两个端点高度和长度约束 $K=\ell$ 确定。

#### 常见陷阱

- 乘子 $\lambda$ 是一个*待求解的未知量*，而非自由选择；约束方程提供求出它所需的额外方程。
- "等周"在历史上意为"相同周长"（经典问题：使固定长度曲线所围面积最大，其答案是圆）；如今这个名字涵盖任何积分约束问题。

<a id="s6"></a>
### 作为变分问题的测地线

#### 是什么以及为什么

**测地线**是曲面上、或更一般地在具有距离概念的空间中局部最短的曲线。测地线把"直线"推广到弯曲空间，是微分几何与广义相对论的核心（在广义相对论中自由下落的物体描出时空的测地线）。

#### 度量与长度泛函（一行的预备知识复述）

在一个曲面上，距离由一个**度量**编码：无穷小长度的平方为 $ds^2=\sum_{i,j} g_{ij}(q)\,dq^i\,dq^j$，其中 $q^i$ 是坐标，$g_{ij}$ 是给定的函数（**度量张量**）。曲线 $q(t)$，$t\in[0,1]$，的长度为
$$
L[q]=\int_0^1\sqrt{\sum_{i,j}g_{ij}(q)\,\dot q^i\dot q^j}\;dt,\qquad \dot q^i=\frac{dq^i}{dt}.
$$
测地线是 $L$ 的极值曲线。

#### 能量泛函技巧

平方根被积函数很别扭。测地线（至多差一个重新参数化）也使**能量** $E[q]=\tfrac12\int_0^1\sum_{i,j}g_{ij}\dot q^i\dot q^j\,dt$ 取极值，它的欧拉–拉格朗日方程更整洁，且它选出了等速参数化。

#### 求解推导 — 测地线方程

取 $L_E=\tfrac12 g_{ij}\dot q^i\dot q^j$（对重复指标隐含求和）。应用多函数欧拉–拉格朗日方程（§s4），其中"$x$"的角色由 $t$ 扮演，"$y_k$"由 $q^k$ 扮演：
1. $\dfrac{\partial L_E}{\partial q^k}=\tfrac12\,\partial_k g_{ij}\,\dot q^i\dot q^j$（度量依赖于位置）。
2. $\dfrac{\partial L_E}{\partial \dot q^k}=g_{kj}\dot q^j$（对二次型求导；因子 $\tfrac12$ 与两个对称项合并）。
3. $\dfrac{d}{dt}\dfrac{\partial L_E}{\partial \dot q^k}=g_{kj}\ddot q^j+\partial_i g_{kj}\,\dot q^i\dot q^j$（乘积法则 + 链式法则）。
4. 欧拉–拉格朗日（$\frac{d}{dt}\partial_{\dot q^k}L_E-\partial_{q^k}L_E=0$）给出 $g_{kj}\ddot q^j+\big(\partial_i g_{kj}-\tfrac12\partial_k g_{ij}\big)\dot q^i\dot q^j=0$。
5. 把中间项对称化并乘以逆度量 $g^{mk}$，便得**测地线方程**
   $$
   \ddot q^m+\Gamma^m_{ij}\,\dot q^i\dot q^j=0,\qquad \Gamma^m_{ij}=\tfrac12 g^{mk}\big(\partial_i g_{kj}+\partial_j g_{ki}-\partial_k g_{ij}\big),
   $$
   其中 $\Gamma^m_{ij}$ 是**克里斯托费尔符号**。这正是"测地线相对于弯曲几何具有零加速度"的精确陈述。

#### 求解实例 — 球面上的大圆

在单位球面上，用坐标 $(\theta,\phi)$（余纬度、经度），$ds^2=d\theta^2+\sin^2\theta\,d\phi^2$，故 $g_{\theta\theta}=1,\ g_{\phi\phi}=\sin^2\theta$。由于 $L_E$ 不显含 $\phi$，$\phi$ 的欧拉–拉格朗日方程给出一个守恒量 $\partial L_E/\partial\dot\phi=\sin^2\theta\,\dot\phi=$ 常数（§s8 的一个实例）。求解 $\theta$ 方程，解恰好是**大圆**——球面与过其球心的平面的交线。这印证了 §s0 的飞机直觉。

#### 常见陷阱

- 长度在重新参数化下不变，故长度泛函的极值曲线只在你沿其行进的方式上被确定；能量泛函通过固定等速消除了这种含糊。
- 测地线是*局部*最短的；一段"绕远路"的大圆弧仍是测地线，但不是全局极小。

## E 部分 · 力学

<a id="s7"></a>
### 哈密顿原理与拉格朗日力学

#### 是什么以及为什么

我们现在兑现这套机器：力学定律是一个变分原理。我们不用牛顿的"力引起加速度"，而是假定单个标量并要求它取驻值；于是牛顿定律便*随之而来*。

#### 作用量与哈密顿原理

对于一个具有坐标 $q(t)$ 的力学系统，定义**拉格朗日量** $L=T-V$，即动能减去势能，以及**作用量**
$$
S[q]=\int_{t_1}^{t_2} L\big(q,\dot q,t\big)\,dt .
$$

> **哈密顿原理。** 在固定的构型 $q(t_1)$ 和 $q(t_2)$ 之间的真实运动 $q(t)$ 是作用量 $S$ 的一个**驻点**。

由 §s2（其中 $x\to t$，$y\to q$），驻定性等价于欧拉–拉格朗日方程，这里称为**运动方程**：
$$
\frac{d}{dt}\frac{\partial L}{\partial \dot q}-\frac{\partial L}{\partial q}=0 .
$$

#### 从拉格朗日量导出牛顿定律

考虑一维中、势 $V(q)$ 作用下质量为 $m$ 的一个质点。
1. **写出拉格朗日量。** 动能 $T=\tfrac12 m\dot q^2$，势 $V(q)$，故 $L=\tfrac12 m\dot q^2-V(q)$。
2. **计算各部分。** $\dfrac{\partial L}{\partial \dot q}=m\dot q$（即**动量** $p$），以及 $\dfrac{\partial L}{\partial q}=-\dfrac{dV}{dq}$（即**力** $F=-V'$，由势的定义）。
3. **欧拉–拉格朗日。** $\dfrac{d}{dt}(m\dot q)-(-V'(q))=0\Rightarrow m\ddot q=-V'(q)=F.$
4. 这恰好是**牛顿第二定律** $F=ma$。变分原理不仅与牛顿一致——它*包含*牛顿。

#### 为什么是 $T-V$ 而不是 $T+V$？

一个自然的疑虑：为何是减号而非加号？符号由要求运动方程得出正确结果而定：只有 $L=T-V$ 才产生 $m\ddot q=-V'$。用 $T+V$（即能量）会得到 $m\ddot q=+V'$，符号错误。作用量*不是*能量；能量是一个不同的组合（§s9）。

#### 求解实例 — 简谐振子

弹簧上的质量有 $V=\tfrac12 k q^2$，故 $L=\tfrac12 m\dot q^2-\tfrac12 k q^2$。则 $\partial L/\partial\dot q=m\dot q$，$\partial L/\partial q=-kq$，运动方程为 $m\ddot q+kq=0$，解为 $q(t)=A\cos(\omega t+\varphi)$，$\omega=\sqrt{k/m}$ ——正弦振荡，从作用量中恢复出来。

#### 收获：广义坐标

拉格朗日力学之所以出色，是因为方程 $\frac{d}{dt}\partial_{\dot q}L=\partial_q L$ 在*任何*坐标 $q$ 下都成立——角度、沿钢丝的距离，凡是适合问题的都行——无需把力分解成分量。选取与几何相匹配的坐标，写下 $T-V$，然后摇动曲柄即可。

#### 常见陷阱

- $L=T-V$ 使用以你所选坐标表示的能量；在非笛卡儿坐标中 $T$ 会带上度量因子（例如极坐标中 $\tfrac12 m(\dot r^2+r^2\dot\theta^2)$）。
- 哈密顿原理要求*构型上的端点固定*，而非速度固定；你指定系统在 $t_1$ 和 $t_2$ 处的位置。

<a id="s8"></a>
### 对称性与诺特定理

#### 是什么以及为什么

本指南中最美的定理：**作用量的每一个连续对称性都产生一个守恒量。** 时间平移对称性给出能量守恒；空间平移对称性给出动量守恒；旋转对称性给出角动量守恒。守恒律不是偶然——它们是对称性的影子。

#### 循环坐标 —— 先看简单情形

若 $L$ 不依赖于某个特定坐标 $q$（仅依赖于 $\dot q$），则该 $q$ 称为**循环的**，欧拉–拉格朗日方程立即给出一个守恒律：$\frac{d}{dt}\frac{\partial L}{\partial\dot q}=\frac{\partial L}{\partial q}=0$，故**共轭动量** $p=\partial L/\partial\dot q$ 是常数。*例：* 若 $L$ 与位置 $x$ 无关，则线动量 $p=m\dot x$ 守恒——平移对称性 $\Rightarrow$ 动量守恒，一行即得。

#### 诺特定理（陈述）

> **定理（诺特）。** 设作用量在一个连续变换族 $q\to q+\varepsilon\,\psi(q,t)$ 下（到一阶）不变，其无穷小生成元为 $\psi$，意指拉格朗日量至多改变一个全时间导数，$\delta L=\frac{d}{dt}F$。则沿运动方程的任意解，量
>
> $$
> Q=\frac{\partial L}{\partial \dot q}\,\psi-F
> $$
>
> 守恒：$\dfrac{dQ}{dt}=0$。

#### 推导

1. 在 $q\to q+\varepsilon\psi$ 下，$\dot q\to\dot q+\varepsilon\dot\psi$。到 $\varepsilon$ 的一阶，$L$ 的改变为 $\delta L=\dfrac{\partial L}{\partial q}\psi+\dfrac{\partial L}{\partial \dot q}\dot\psi$（链式法则）。
2. 在一个解上，$\dfrac{\partial L}{\partial q}=\dfrac{d}{dt}\dfrac{\partial L}{\partial \dot q}$（欧拉–拉格朗日，§s7）。代入：
   $$
   \delta L=\frac{d}{dt}\!\left(\frac{\partial L}{\partial \dot q}\right)\psi+\frac{\partial L}{\partial \dot q}\dot\psi=\frac{d}{dt}\!\left(\frac{\partial L}{\partial \dot q}\,\psi\right),
   $$
   其中最后一个等号是乘积法则的逆用。
3. 由假设 $\delta L=\dfrac{dF}{dt}$。令二者相等：$\dfrac{d}{dt}\big(\frac{\partial L}{\partial\dot q}\psi\big)=\dfrac{dF}{dt}$，故 $\dfrac{d}{dt}\big(\frac{\partial L}{\partial\dot q}\psi-F\big)=0$。因此 $Q$ 守恒。$\blacksquare$

#### 由时间平移对称性得能量

时间对称性需要稍微不同的处理，因为它平移 $t$ 本身，但结论是 §s2 的贝尔特拉米恒等式的化装版本。
1. 设 $L$ 不显含时间，$\partial L/\partial t=0$。
2. 计算全时间导数 $\dfrac{dL}{dt}=\dfrac{\partial L}{\partial q}\dot q+\dfrac{\partial L}{\partial \dot q}\ddot q$（无 $\partial L/\partial t$ 项）。
3. 用欧拉–拉格朗日把 $\partial L/\partial q$ 换成 $\frac{d}{dt}\partial_{\dot q}L$，这等于 $\dfrac{d}{dt}\big(\dot q\,\frac{\partial L}{\partial\dot q}\big)$（乘积法则）。
4. 因此 $\dfrac{d}{dt}\Big(\dot q\,\dfrac{\partial L}{\partial \dot q}-L\Big)=0$。守恒量
   $$
   H=\dot q\,\frac{\partial L}{\partial \dot q}-L
   $$
   就是**能量**（哈密顿量，§s9）。对 $L=\tfrac12 m\dot q^2-V$，$H=m\dot q^2-(\tfrac12 m\dot q^2-V)=\tfrac12 m\dot q^2+V=T+V$ ——恰好是总能量。

#### 求解实例 — 由平移对称性得动量

两个通过仅依赖于其*间距*的势 $V(q_1-q_2)$ 相互作用的质点，有 $L=\tfrac12 m_1\dot q_1^2+\tfrac12 m_2\dot q_2^2-V(q_1-q_2)$。平移 $q_1\to q_1+\varepsilon,\ q_2\to q_2+\varepsilon$ 使 $V$（因而 $L$）不变，故 $\delta L=0$，对每个有 $F=0$，$\psi=1$。诺特的 $Q=\frac{\partial L}{\partial\dot q_1}\cdot1+\frac{\partial L}{\partial\dot q_2}\cdot1=m_1\dot q_1+m_2\dot q_2$ ——即**总线动量**，守恒。平移不变性 $\Rightarrow$ 动量守恒，得证。

#### 常见陷阱

- 对称性必须是*连续的*（一个单参数族）；像反射这样的离散对称性不给出诺特荷。
- $\delta L$ 可能等于一个全导数 $\frac{dF}{dt}$ 而不必字面上为零；那仍然算数，忘记 $-F$ 项会给出错误的（不守恒的）$Q$。

## F 部分 · 哈密顿形式与场

<a id="s9"></a>
### 哈密顿表述、勒让德变换与正则方程

#### 是什么以及为什么

拉格朗日力学使用位置与速度 $(q,\dot q)$ 并给出二阶方程。**哈密顿**表述把速度换成动量 $(q,p)$，并用具有惊人对称性的*两个*一阶方程替换每个二阶方程。这一观点是统计力学、混沌理论以及通往量子力学之路的基础。

#### 勒让德变换（引擎）

我们想把变量 $\dot q$ 换成 $p=\partial L/\partial\dot q$。以这种方式更换变量的干净办法是**勒让德变换**。

> **定义 — 勒让德变换。** 给定 $L(\dot q)$（把 $q,t$ 当作参数），定义 $p=\dfrac{\partial L}{\partial \dot q}$ 和
>
> $$
> H(q,p,t)=p\,\dot q-L(q,\dot q,t),
> $$
>
> 其中右边的 $\dot q$ 通过反解 $p=\partial L/\partial\dot q$ 用 $p$ 表示。$H$ 即**哈密顿量**。

只要 $\partial^2 L/\partial\dot q^2\neq0$，该变换便有良好定义（可逆），这使 $p(\dot q)$ 严格单调以便可以反解。

#### 导出哈密顿正则方程

取 $H=p\dot q-L$ 的微分并比较系数。
1. $dH=\dot q\,dp+p\,d\dot q-\dfrac{\partial L}{\partial q}dq-\dfrac{\partial L}{\partial \dot q}d\dot q-\dfrac{\partial L}{\partial t}dt$（乘积法则 + 链式法则）。
2. 项 $p\,d\dot q$ 与 $-\frac{\partial L}{\partial\dot q}d\dot q$ 相消，*因为* 按定义 $p=\partial L/\partial\dot q$。这种相消正是勒让德变换的全部要点：$H$ 真正依赖于 $p$，而非依赖于 $\dot q$。
3. 故 $dH=\dot q\,dp-\dfrac{\partial L}{\partial q}dq-\dfrac{\partial L}{\partial t}dt$。但由微分的定义又有 $dH=\dfrac{\partial H}{\partial q}dq+\dfrac{\partial H}{\partial p}dp+\dfrac{\partial H}{\partial t}dt$。
4. 匹配独立微分 $dq,dp,dt$ 的系数：
   $$
   \frac{\partial H}{\partial p}=\dot q,\qquad \frac{\partial H}{\partial q}=-\frac{\partial L}{\partial q},\qquad \frac{\partial H}{\partial t}=-\frac{\partial L}{\partial t}.
   $$
5. 由欧拉–拉格朗日，$\dfrac{\partial L}{\partial q}=\dfrac{d}{dt}\dfrac{\partial L}{\partial\dot q}=\dot p$。代入中间的关系给出 $\partial H/\partial q=-\dot p$。汇总：

> **哈密顿正则方程**
>
> $$
> \dot q=\frac{\partial H}{\partial p},\qquad \dot p=-\frac{\partial H}{\partial q}.
> $$

这两个一阶方程等价于单个二阶欧拉–拉格朗日方程，但它们在 $q$ 与 $p$ 之间的对称性是通往更深结构（相空间、泊松括号、量子化）的门户。

#### 能量守恒，再访

由正则方程，$\dfrac{dH}{dt}=\dfrac{\partial H}{\partial q}\dot q+\dfrac{\partial H}{\partial p}\dot p+\dfrac{\partial H}{\partial t}=(-\dot p)\dot q+\dot q\,\dot p+\dfrac{\partial H}{\partial t}=\dfrac{\partial H}{\partial t}$。前两项恒等地相消，故若 $H$ 不显含时间（$\partial H/\partial t=0$），则 $H$ 守恒——能量守恒，又一次，如今几乎是平凡的。

#### 求解实例 — 哈密顿形式的简谐振子

由 $L=\tfrac12 m\dot q^2-\tfrac12 k q^2$：$p=m\dot q\Rightarrow\dot q=p/m$，且 $H=p\dot q-L=\dfrac{p^2}{m}-\big(\tfrac12 m(p/m)^2-\tfrac12 kq^2\big)=\dfrac{p^2}{2m}+\tfrac12 kq^2$ ——动能加势能，即总能量。正则方程：$\dot q=\partial H/\partial p=p/m$ 和 $\dot p=-\partial H/\partial q=-kq$，二者合并得 $m\ddot q=-kq$，与 §s7 中相同的振子。

#### 常见陷阱

- 只有当坐标不显含时间且 $T$ 关于速度是二次的时，$H$ 才等于 $T+V$；一般地 $H=p\dot q-L$ 是定义，而"能量"就是它所给出的任何东西。
- 形成 $H$ 之后你必须把 $\dot q$ 用 $p$ 消去；在 $H$ 内部留下一个游离的 $\dot q$ 是经典的错误。

<a id="s10"></a>
### 场论（简述）：拉格朗日密度与场方程

#### 是什么以及为什么

最后的推广：未知量是一个**场** $\phi(x^\mu)$ ——一个定义在空间与时间每一点上的量，比如电磁势或一个量子场的值。同一个变分原理，配上对时空的积分，便产生所有经典场论的方程。这是从本指南通往电磁学与量子场论的桥梁。

#### 拉格朗日密度与作用量

对一个依赖于时空坐标 $x^\mu=(t,x,y,z)$ 的场 $\phi$，我们没有单个 $L$，而有一个**拉格朗日密度** $\mathcal{L}$ ——*单位体积的*拉格朗日量——它依赖于场及其时空导数 $\partial_\mu\phi=\partial\phi/\partial x^\mu$：
$$
S[\phi]=\int \mathcal{L}\big(\phi,\,\partial_\mu\phi,\,x^\mu\big)\,d^4x ,
$$
其中 $d^4x=dt\,dx\,dy\,dz$，积分在时空的一个区域上进行。作用量依旧是一个数；哈密顿原理依旧要求它取驻值。

#### 场的欧拉–拉格朗日方程

这是 §s4 中 $m=4$ 个自变量、并由场扮演 $u$ 角色的情形。作变分 $\phi\to\phi+\varepsilon\eta$（其中 $\eta=0$ 于边界上）并应用散度定理（时空中的分部积分）给出：

> **场的欧拉–拉格朗日方程**
>
> $$
> \frac{\partial \mathcal{L}}{\partial \phi}-\partial_\mu\!\left(\frac{\partial \mathcal{L}}{\partial(\partial_\mu\phi)}\right)=0 ,
> $$
>
> 对重复指标 $\mu=0,1,2,3$ 求和。

*简要推导，带理由：*
1. 一阶变分：$\delta S=\int\big[\frac{\partial\mathcal{L}}{\partial\phi}\eta+\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi)}\partial_\mu\eta\big]d^4x$（链式法则，如 §s4）。
2. 对第二项作分部积分：$\int\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi)}\partial_\mu\eta\,d^4x=\oint(\cdots)\,dS-\int\partial_\mu\big(\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi)}\big)\eta\,d^4x$（散度定理）。
3. 边界积分消失，因为 $\eta=0$ 于该处。
4. 整理；多变量基本引理迫使方括号为零，给出所述方程。

#### 求解实例 — 克莱因–戈尔登场

取相对论标量密度 $\mathcal{L}=\tfrac12\big(\partial_t\phi\big)^2-\tfrac12|\nabla\phi|^2-\tfrac12 m^2\phi^2$（动能减去梯度减去质量项；采用波速为 $1$ 的单位）。
1. $\dfrac{\partial\mathcal{L}}{\partial\phi}=-m^2\phi$。
2. $\dfrac{\partial\mathcal{L}}{\partial(\partial_t\phi)}=\partial_t\phi$ 且 $\dfrac{\partial\mathcal{L}}{\partial(\partial_i\phi)}=-\partial_i\phi$。
3. 场方程：$-m^2\phi-\big[\partial_t(\partial_t\phi)+\partial_i(-\partial_i\phi)\big]=0$，即
   $$
   \partial_t^2\phi-\nabla^2\phi+m^2\phi=0 ,
   $$
   即**克莱因–戈尔登方程**。令 $m=0$ 恢复波动方程；同一个模板配上正确的 $\mathcal{L}$，便给出麦克斯韦方程和爱因斯坦方程。

#### 常见陷阱

- $\mathcal{L}$ 是一个*密度*；物理的拉格朗日量是它的空间积分 $L=\int\mathcal{L}\,d^3x$。
- 指标 $\mu$ 取遍*全部四个*时空方向；漏掉时间导数项会给出错误的静态方程。

---

*一门完整的变分法入门课程：泛函与一阶变分，从基本引理无缝隙地导出的欧拉–拉格朗日方程，经典曲线（直线、最速降线摆线、悬链面），向多个函数和向场的推广，借助拉格朗日乘子的约束问题，测地线，以及分析力学的完整脉络——哈密顿原理、诺特定理、哈密顿量与勒让德变换，还有经典场论。每个符号都用文字定义，每个论断都被证明。贯穿其中的唯一线索：自然定律就是某个作用量取驻值的条件。*
