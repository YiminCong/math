[English](derived-from-scratch.md) · **中文**

# 微积分，*从头推导*

不只是公式的罗列——下面每一条核心公式都经过**演示**：一步一步地展示它从何而来。顺序由基础到进阶，每一块内容都建立在前一块之上。

[← 返回全部指南](../README.zh.md)

<a id="s0"></a>
## 在任何符号之前的全局图景

*在脑中记住一张地图。*

整个微积分是关于变化的两个问题，外加一个发现：它们互为反操作。

- **导数**问：*此刻它变化得有多快？*（一个斜率、一个速度、一个变化率）
- **积分**问：*总共累积了多少？*（一片面积、一段距离、一个求和）

两者都是从某个简单的东西出发——两点之间的斜率、一个矩形的面积——再把它推向**极限**，让一个间隙缩小到零。所以极限要先讲。

### 整门课浓缩成一行

> 极限 → 导数 → 积分 ↔（由微积分基本定理连接）→ 级数 → 多元

> **要追随的主线**
>
> **微积分基本定理**（第 7 节）说微分与积分互相抵消。正因如此，第 8–9 节中每一条积分公式都是第 3–4 节中某条微分公式倒着读的结果——我们也将真的这样去推导它们。

<a id="s1"></a>
## 极限与连续性

*极限回答：当输入趋近某个值时，函数走向何处——即便它永远到不了那里？*

**直观的极限**

$$\lim_{x \to a} f(x) = L$$

*当 $x$ 任意地接近 $a$ 时，$f(x)$ 任意地接近 $L$。*

**形式化（ε–δ）定义**

$$\forall\, \varepsilon>0,\; \exists\, \delta>0 \;:\; 0<|x-a|<\delta \implies |f(x)-L|<\varepsilon$$

*随便指定一个围绕 L 的容差 ε；我都能找到一个围绕 a 的窗口 δ，使我保持在容差之内。*

**单侧极限与存在性**

$$\lim_{x\to a^-}f(x)=\lim_{x\to a^+}f(x)=L \iff \lim_{x\to a}f(x)=L$$

*只有当左趋近与右趋近一致时，双侧极限才存在。*

**无穷远处的极限／无穷极限**

$$\lim_{x\to\infty}\frac{1}{x}=0, \qquad \lim_{x\to 0^+}\frac{1}{x}=+\infty$$

### 极限运算法则（极限如何组合）

若 $\lim f = L$ 且 $\lim g = M$：

$$\lim (f \pm g)=L\pm M,\quad \lim (fg)=LM,\quad \lim \tfrac{f}{g}=\tfrac{L}{M}\,(M\neq0),\quad \lim cf=cL$$

**夹逼（夹挤）定理**

$$g(x)\le f(x)\le h(x)\ \text{and}\ \lim g=\lim h=L \implies \lim f=L$$

### 那几个特殊极限——以及它们的来历

**要记住的三个极限**

$$\lim_{x\to0}\frac{\sin x}{x}=1,\qquad \lim_{x\to0}\frac{1-\cos x}{x}=0,\qquad \lim_{x\to0}\frac{e^{x}-1}{x}=1$$

**演示 — 为什么 $ \lim_{x\to0}\frac{\sin x}{x}=1 $**

1. 对一个小角 $x$（弧度制，$0

   $$\sin x < x < \tan x.$$
2. 把每一部分都除以 $\sin x>0$：

   $$1 < \frac{x}{\sin x} < \frac{1}{\cos x}.$$
3. 把三者全部取倒数（不等号方向反转）：

   $$\cos x < \frac{\sin x}{x} < 1.$$
4. 当 $x\to0$ 时，$\cos x\to1$。这个分式被夹在两个都趋向 1 的量之间，所以由夹逼定理它也 $\to1$。

*正是这一个极限让第 4 节中的 $(\sin x)'=\cos x$ 成立。*

**在一点处的连续性**

$$f \text{ continuous at } a \iff \lim_{x\to a} f(x)=f(a)$$

*极限存在、函数值存在、二者相等——没有孔、没有跳跃、没有断裂。*

**介值定理**

$$f \text{ continuous on } [a,b],\ N \text{ between } f(a),f(b) \implies \exists\, c\in(a,b):\ f(c)=N$$

*一条连续曲线不能跳过某个值——它必须经过中间的每一个高度。（这正是求根法奏效的原因。）*

> **为什么接下来这很重要**
>
> 可微要求连续，而导数本身就是*被定义为*一个极限。第 2 节就是把上面这一切小心地应用一次。

<a id="s2"></a>
## 导数的定义

*取两点之间的斜率，然后把它们滑到一起。*

**定义（差商的极限）**

$$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$$

*$\frac{f(x+h)-f(x)}{h}$ 是过两个邻近点的割线的斜率；$h\to0$ 把它倾斜成切线。*

**在一点处的等价形式**

$$f'(a)=\lim_{x\to a}\frac{f(x)-f(a)}{x-a}$$

`$f'(x)$ — 拉格朗日记号` · `$\dfrac{dy}{dx}$ — 莱布尼茨记号` · `$\dot y$ — 牛顿记号` · `$D_xf$ — 算子记号`

**演示 — 从定义求 $f(x)=x^2$ 的导数**

1. 代入定义：

   $$f'(x)=\lim_{h\to0}\frac{(x+h)^2-x^2}{h}.$$
2. 展开分子：

   $$(x+h)^2-x^2 = x^2+2xh+h^2-x^2 = 2xh+h^2.$$
3. 除以 $h$（在极限内 $h\neq0$，故允许）：

   $$\frac{2xh+h^2}{h}=2x+h.$$
4. 令 $h\to0$：

   $$f'(x)=2x.$$

*与幂法则 $nx^{n-1}$ 吻合。接下来我们一般性地证明该法则。*

<a id="s3"></a>
## 求导法则——逐条证明

*下面每一条法则都由极限定义推出。一旦证明，你再也不必触碰定义。*

**常数法则与基本法则**

$$\frac{d}{dx}[c]=0,\quad \frac{d}{dx}[cf]=cf',\quad (f\pm g)'=f'\pm g'$$

*它们直接从第 1 节的极限运算法则中得出（和的极限等于极限之和）。*

**幂法则**

$$\frac{d}{dx}\big[x^{n}\big]=n\,x^{\,n-1}$$

**演示 — 幂法则（借助二项式定理）**

1. 定义：

   $$f'(x)=\lim_{h\to0}\frac{(x+h)^n-x^n}{h}.$$
2. 二项式展开：

   $$(x+h)^n = x^n + n x^{n-1}h + \tfrac{n(n-1)}{2}x^{n-2}h^2+\cdots+h^n.$$
3. 减去 $x^n$；每一个剩下的项都至少含一个因子 $h$：

   $$(x+h)^n-x^n = n x^{n-1}h + \tfrac{n(n-1)}{2}x^{n-2}h^2+\cdots$$
4. 除以 $h$：

   $$n x^{n-1} + \tfrac{n(n-1)}{2}x^{n-2}h + \cdots$$
5. 令 $h\to0$：每一个仍带 $h$ 的项都消失，留下

   $$f'(x)=n x^{n-1}.$$

**★ 你最常用到的那些著名的日常导数**

$$\frac{d}{dx}\,e^{x}=e^{x} \qquad \frac{d}{dx}\sqrt{x}=\frac{1}{2\sqrt{x}} \qquad \frac{d}{dx}\,\frac{1}{x}=-\frac{1}{x^{2}}$$

*$e^x$ 是数学中最著名的导数——唯一一个（在相差常数倍的意义下）等于自身导数的函数，这正是它支配增长、衰减和复利的原因。另外两个是幂法则中不断出现的日常特例。*

**演示 — 那两个日常特例不过是幂法则**

1. 平方根：写成 $\sqrt{x}=x^{1/2}$，应用 $nx^{n-1}$：

   $$\frac{d}{dx}x^{1/2}=\tfrac{1}{2}x^{-1/2}=\frac{1}{2\sqrt{x}}.$$
2. 倒数：写成 $\dfrac{1}{x}=x^{-1}$，应用同一法则：

   $$\frac{d}{dx}x^{-1}=-1\cdot x^{-2}=-\frac{1}{x^{2}}.$$

*幂法则对任意指数都成立——分数或负数皆可——而不只是整数。*

**乘积法则**

$$(fg)' = f'g + fg'$$

*“第一个的导数乘第二个，加上第一个乘第二个的导数。”不是 $f'g'$。*

**演示 — 乘积法则（加减项技巧）**

1. 定义：

   $$(fg)'=\lim_{h\to0}\frac{f(x+h)g(x+h)-f(x)g(x)}{h}.$$
2. 在分子中加上又减去 $f(x+h)g(x)$（它相互抵消为零，故毫无改变）：

   $$f(x+h)g(x+h)-f(x+h)g(x)+f(x+h)g(x)-f(x)g(x).$$
3. 分组并提取因子：

   $$f(x+h)\big[g(x+h)-g(x)\big]+g(x)\big[f(x+h)-f(x)\big].$$
4. 除以 $h$ 并拆分极限：

   $$\lim f(x+h)\frac{g(x+h)-g(x)}{h}+\lim g(x)\frac{f(x+h)-f(x)}{h}.$$
5. 当 $h\to0$：$f(x+h)\to f(x)$，而两个商分别变为 $g'$ 与 $f'$：

   $$(fg)'=f g' + g f'.$$

**商法则**

$$\left(\frac{f}{g}\right)'=\frac{f'g-fg'}{g^{2}}$$

*“低乘高的导减去高乘低的导，再除以低的平方。”*

**演示 — 商法则（直接由乘积法则得出）**

1. 令 $Q=\dfrac{f}{g}$，于是 $f = Q\,g$。
2. 对两边用乘积法则求导：

   $$f' = Q'g + Q g'.$$
3. 解出 $Q'$：

   $$Q' = \frac{f'-Qg'}{g}.$$
4. 把 $Q$ 换回 $f/g$，并通分化简：

   $$Q'=\frac{f'-\frac{f}{g}g'}{g}=\frac{f'g-fg'}{g^2}.$$

*注意商法则并非另一套魔法——它就是乘积法则重新整理的结果。*

**链式法则（函数套函数）**

$$\frac{d}{dx}\,f\big(g(x)\big)=f'\big(g(x)\big)\cdot g'(x) \qquad\Big(\tfrac{dy}{dx}=\tfrac{dy}{du}\cdot\tfrac{du}{dx}\Big)$$

**演示 — 链式法则（让它显而易见的直观）**

1. 把由 $x$ 的变化所引起的 $y$ 的变化写成比值之积（分子分母同乘 $\Delta u$）：

   $$\frac{\Delta y}{\Delta x}=\frac{\Delta y}{\Delta u}\cdot\frac{\Delta u}{\Delta x}.$$
2. 当 $\Delta x\to0$ 时，内层的变化 $\Delta u\to0$ 也成立（因为 $g$ 连续）。
3. 在极限下每个比值都变成一个导数：

   $$\frac{dy}{dx}=\frac{dy}{du}\cdot\frac{du}{dx}=f'(g(x))\,g'(x).$$

*对外层求导，保持内层不变，再乘以内层的导数。*

> **向前的链接（记住这两条）**
>
> 倒着读，**乘积法则变成分部积分**，而**链式法则变成 u 代换**——它们是第 9 节里两大主要积分技巧。我们将由这两条法则推出它们。

<a id="s4"></a>
## 每一个标准函数的导数

*有了上面的法则再加上几个关键极限，下面每一个都能被演示出来。*

**三角函数**

$$(\sin x)'=\cos x,\quad (\cos x)'=-\sin x,\quad (\tan x)'=\sec^2 x$$

$$(\cot x)'=-\csc^2 x,\quad (\sec x)'=\sec x\tan x,\quad (\csc x)'=-\csc x\cot x$$

**演示 — $(\sin x)'=\cos x$**

1. 定义：

   $$(\sin x)'=\lim_{h\to0}\frac{\sin(x+h)-\sin x}{h}.$$
2. 使用和角公式 $\sin(x+h)=\sin x\cos h+\cos x\sin h$：

   $$=\lim_{h\to0}\frac{\sin x\cos h+\cos x\sin h-\sin x}{h}.$$
3. 把含 $\sin x$ 的项分组并拆开：

   $$=\sin x\lim_{h\to0}\frac{\cos h-1}{h}+\cos x\lim_{h\to0}\frac{\sin h}{h}.$$
4. 代入第 1 节的特殊极限 $\big(\frac{\cos h-1}{h}\to0,\ \frac{\sin h}{h}\to1\big)$：

   $$=\sin x\cdot 0 + \cos x\cdot 1 = \cos x.$$

*$\tan,\sec,\csc,\cot$ 随后由对 $\sin/\cos$ 应用商法则而得。*

**指数函数与对数函数**

$$(e^{x})'=e^{x},\quad (a^{x})'=a^{x}\ln a,\quad (\ln x)'=\frac{1}{x},\quad (\log_a x)'=\frac{1}{x\ln a}$$

**演示 — $(e^x)'=e^x$**

1. 定义：

   $$(e^x)'=\lim_{h\to0}\frac{e^{x+h}-e^{x}}{h}.$$
2. 提出 $e^{x}$（它与 $h$ 无关）：

   $$=e^{x}\lim_{h\to0}\frac{e^{h}-1}{h}.$$
3. 剩下的那个极限等于 $1$（第 1 节的一个特殊极限——事实上这正是定义 $e$ 的性质）：

   $$=e^{x}\cdot 1 = e^{x}.$$

*$e^x$ 是唯一一个等于自身导数的函数。*

**演示 — $(\ln x)'=\tfrac1x$（借助反函数）**

1. 令 $y=\ln x$。按定义这意味着

   $$e^{y}=x.$$
2. 对两边关于 $x$ 求导，左边用链式法则：

   $$e^{y}\cdot\frac{dy}{dx}=1.$$
3. 解出 $dy/dx$，并回想 $e^{y}=x$：

   $$\frac{dy}{dx}=\frac{1}{e^{y}}=\frac{1}{x}.$$

**反三角函数**

$$(\arcsin x)'=\frac{1}{\sqrt{1-x^2}},\quad (\arccos x)'=-\frac{1}{\sqrt{1-x^2}},\quad (\arctan x)'=\frac{1}{1+x^2}$$

**演示 — $(\arctan x)'=\tfrac{1}{1+x^2}$**

1. 令 $y=\arctan x$，于是

   $$\tan y = x.$$
2. 对两边求导：

   $$\sec^2 y\cdot\frac{dy}{dx}=1 \;\Rightarrow\; \frac{dy}{dx}=\frac{1}{\sec^2 y}.$$
3. 利用恒等式 $\sec^2 y = 1+\tan^2 y$ 以及 $\tan y = x$：

   $$\frac{dy}{dx}=\frac{1}{1+\tan^2 y}=\frac{1}{1+x^2}.$$

**双曲函数**

$$\sinh x=\frac{e^x-e^{-x}}{2},\quad \cosh x=\frac{e^x+e^{-x}}{2}$$

$$(\sinh x)'=\cosh x,\quad (\cosh x)'=\sinh x,\quad (\tanh x)'=\operatorname{sech}^2 x$$

*由 $e^x$ 定义；它们的导数从 $(e^x)'=e^x$ 一行就能得出。注意 $(\cosh)'=+\sinh$，与三角函数那个负号不同。*

> **一种静默的对称**
>
> 对 $\sin$ 求导四次又回到 $\sin$。正是这个循环使得正弦和余弦能描述一切振荡的现象——它还会在第 11 节它们的泰勒级数中再次出现。

<a id="s5"></a>
## 隐函数、对数与高阶导数

*用于 y 纠缠不清、指数杂乱、或者要求导不止一次的情形。*

**隐函数求导**

$$\frac{d}{dx}[y]=\frac{dy}{dx},\qquad \frac{d}{dx}\big[y^{2}\big]=2y\frac{dy}{dx}$$

**演示 — 圆 $x^2+y^2=25$ 上的斜率**

1. 对两边求导，把 $y$ 视为 $x$ 的函数（所以 $y^2$ 需要链式法则）：

   $$2x+2y\frac{dy}{dx}=0.$$
2. 解出斜率：

   $$\frac{dy}{dx}=-\frac{x}{y}.$$

*每一个含 $y$ 的项都会带上一个 $dy/dx$——这正是第 3 节的链式法则在起作用。*

**对数求导法**

$$y=f(x)^{g(x)} \Rightarrow \ln y=g\ln f \Rightarrow \frac{y'}{y}=\big(g\ln f\big)'$$

*先取 $\ln$，把别扭的幂变成乘积。对于 $x^{x}$ 这类东西必不可少。*

**高阶导数**

$$f''(x)=\frac{d}{dx}f'(x),\qquad f^{(n)}(x)=\frac{d^{\,n}y}{dx^{\,n}}$$

*若 $s(t)$ 是位置：$s'$ 是速度，$s''$ 是加速度。二阶导数还控制凹凸性（第 6 节）。*

<a id="s6"></a>
## 让导数发挥作用

*切线、曲线形状、最优化，以及看似无解的极限。*

**在 $x=a$ 处的切线**

$$y-f(a)=f'(a)(x-a)$$

### 从导数读出一条曲线

- $f'>0$：递增   $f'<0$：递减
- **临界点**：$f'(x)=0$ 或无定义之处——极大/极小的候选点
- $f''>0$：上凹（杯形）   $f''<0$：下凹（帽形）
- **拐点**：$f''$ 变号之处

**一阶与二阶导数判别法**

$$f'(c)=0:\quad f''(c)>0 \Rightarrow \text{local min},\qquad f''(c)<0 \Rightarrow \text{local max}$$

**中值定理（及罗尔定理这一特例）**

$$\exists\,c\in(a,b):\ f'(c)=\frac{f(b)-f(a)}{b-a}$$

*在某处，瞬时斜率等于平均斜率。罗尔定理是 $f(a)=f(b)$ 的特例，给出 $f'(c)=0$。*

**洛必达法则（用于 $0/0$ 或 $\infty/\infty$）**

$$\lim_{x\to a}\frac{f(x)}{g(x)}=\lim_{x\to a}\frac{f'(x)}{g'(x)}$$

**演示 — 它为何成立（局部线性的图景）**

1. 在 $x=a$ 附近且 $f(a)=g(a)=0$ 时，把每个函数换成它的切线（第 6 节）：

   $$f(x)\approx f'(a)(x-a),\qquad g(x)\approx g'(a)(x-a).$$
2. 作比值；公共因子 $(x-a)$ 约掉：

   $$\frac{f(x)}{g(x)}\approx\frac{f'(a)(x-a)}{g'(a)(x-a)}=\frac{f'(a)}{g'(a)}.$$

*一个不定型的比值由斜率之比所支配。漂亮地回到了第 1 节。*

**线性近似与微分**

$$f(x)\approx f(a)+f'(a)(x-a),\qquad dy=f'(x)\,dx$$

*在一点附近，每条光滑曲线看起来都像它的切线。把它推广到无穷多阶导数，便成为第 11 节的泰勒级数。*

<a id="s7"></a>
## 原函数与微积分基本定理

*整门学科的枢纽：导数与积分被揭示为互为反操作。*

**不定积分（原函数）**

$$\int f(x)\,dx=F(x)+C \quad\text{where}\quad F'(x)=f(x)$$

*“什么函数以‘它’为导数？”出现 $+C$ 是因为常数在求导时会消失。*

**作为黎曼和极限的定积分**

$$\int_{a}^{b} f(x)\,dx=\lim_{n\to\infty}\sum_{i=1}^{n} f(x_i^{*})\,\Delta x,\qquad \Delta x=\frac{b-a}{n}$$

*把面积切成 n 个细矩形，加起来，再让切片消失。积分“就是”一个无穷和——与构造导数时同样的“推向极限”。*

### 微积分基本定理

**第一部分 — 微分抵消积分**

$$\frac{d}{dx}\int_{a}^{x} f(t)\,dt=f(x)$$

**第二部分 — 用原函数来计算积分**

$$\int_{a}^{b} f(x)\,dx=F(b)-F(a),\quad F'=f$$

**演示 — 为什么第一部分成立（细条论证）**

1. 定义累积面积函数

   $$A(x)=\int_a^x f(t)\,dt.$$
2. 把 $x$ 增加一个微小的 $h$，会添上一条宽 $h$、高约 $f(x)$ 的细条：

   $$A(x+h)-A(x)\approx f(x)\cdot h.$$
3. 除以 $h$：

   $$\frac{A(x+h)-A(x)}{h}\approx f(x).$$
4. 令 $h\to0$。左边恰好是 $A'(x)$ 的定义：

   $$A'(x)=f(x).$$

*所以面积函数的导数就是原来的函数——累积与变化率是互逆的运算。第二部分随之成立，因为任意两个原函数只相差一个常数。*

> **回报**
>
> 要求一片面积（一个无穷和），你并不去做加法——你找一个原函数，再相减两个值。这正是为什么第 8 节的整张积分表不过是第 3–4 节的导数表倒着读。

<a id="s8"></a>
## 基本积分表

*每一行都是某条求导法则的逆转——对右端求导即可验证其中任意一行。*

**积分的幂法则**

$$\int x^{n}\,dx=\frac{x^{\,n+1}}{n+1}+C \quad(n\neq-1)$$

*验证：对 $\frac{x^{n+1}}{n+1}$ 求导，幂法则便还原出 $x^n$。*

**$n=-1$ 这一例外**

$$\int \frac{1}{x}\,dx=\ln|x|+C$$

| 积分 | 结果 | 是谁的逆… |
| --- | --- | --- |
| $\int e^{x}\,dx$ | $e^{x}+C$ | $(e^x)'=e^x$ |
| $\int a^{x}\,dx$ | $\dfrac{a^{x}}{\ln a}+C$ | $(a^x)'=a^x\ln a$ |
| $\int \cos x\,dx$ | $\sin x+C$ | $(\sin x)'=\cos x$ |
| $\int \sin x\,dx$ | $-\cos x+C$ | $(\cos x)'=-\sin x$ |
| $\int \sec^{2}x\,dx$ | $\tan x+C$ | $(\tan x)'=\sec^2 x$ |
| $\int \sec x\tan x\,dx$ | $\sec x+C$ | $(\sec x)'=\sec x\tan x$ |
| $\int \dfrac{1}{1+x^{2}}\,dx$ | $\arctan x+C$ | $(\arctan x)'=\frac{1}{1+x^2}$ |
| $\int \dfrac{1}{\sqrt{1-x^{2}}}\,dx$ | $\arcsin x+C$ | $(\arcsin x)'=\frac{1}{\sqrt{1-x^2}}$ |
| $\int \sinh x\,dx$ | $\cosh x+C$ | $(\cosh x)'=\sinh x$ |

### 三个需要一点小技巧的积分

| 积分 | 结果 | 怎么做 |
| --- | --- | --- |
| $\int \tan x\,dx$ | $\ln\vert \sec x\vert +C$ | 用 $u=\cos x$ 作 u 代换 |
| $\int \ln x\,dx$ | $x\ln x-x+C$ | 分部积分（见 §9） |
| $\int \sec x\,dx$ | $\ln\vert \sec x+\tan x\vert +C$ | 乘以一个巧妙的 1 |

> 如何使用本节
>
> 不要把这张表单独去背。如果你掌握了第 3–4 节的导数表，你就已经掌握了这张表——只需把箭头反过来。这就是微积分基本定理在起作用。

<a id="s9"></a>
## 积分技巧——逐条证明

*当一个积分对不上这张表时，就把它重塑到对得上为止。其中两条是求导法则的逆转，我们也将这样去推导它们。*

**u 代换**

$$\int f\big(g(x)\big)g'(x)\,dx=\int f(u)\,du,\qquad u=g(x)$$

**演示 — u 代换就是链式法则的逆转**

1. 令 $F$ 是 $f$ 的一个原函数，即 $F'=f$。由链式法则：

   $$\frac{d}{dx}F\big(g(x)\big)=F'\big(g(x)\big)g'(x)=f\big(g(x)\big)g'(x).$$
2. 对两边积分（积分抵消导数）：

   $$\int f\big(g(x)\big)g'(x)\,dx=F\big(g(x)\big)+C.$$
3. 这个右端恰好是带 $u=g(x)$ 的 $\int f(u)\,du$。

**分部积分**

$$\int u\,dv=uv-\int v\,du$$

**演示 — 分部积分就是乘积法则的逆转**

1. 从乘积法则出发：

   $$(uv)'=u'v+uv'.$$
2. 对两边关于 $x$ 积分：

   $$uv=\int u'v\,dx+\int uv'\,dx.$$
3. 解出其中一个积分：即 $\displaystyle\int u\,dv=uv-\int v\,du.$

   $$\int uv'\,dx=uv-\int u'v\,dx,$$

*用它处理诸如 $\int x e^{x}\,dx$ 或 $\int \ln x\,dx$（取 $u=\ln x,\ dv=dx$）这样的乘积。*

**三角代换**

$$\sqrt{a^2-x^2}\!: x=a\sin\theta,\quad \sqrt{a^2+x^2}\!: x=a\tan\theta,\quad \sqrt{x^2-a^2}\!: x=a\sec\theta$$

*用一个干净的三角恒等式换掉一个别扭的平方根。*

**部分分式**

$$\frac{P(x)}{(x-r_1)(x-r_2)}=\frac{A}{x-r_1}+\frac{B}{x-r_2}$$

*把一个有理函数拆成若干简单块，每块积分都得到一个对数或反正切。*

**反常积分**

$$\int_{a}^{\infty} f(x)\,dx=\lim_{t\to\infty}\int_{a}^{t} f(x)\,dx$$

*无穷限（或竖直渐近线）作为极限来处理；若该极限有限，积分便“收敛”。*

### 定积分的性质

$$\int_a^b f=-\int_b^a f,\qquad \int_a^a f=0,\qquad \int_a^b f=\int_a^c f+\int_c^b f$$

> **把这面镜子摆明**
>
> 链式法则 ⟷ u 代换。乘积法则 ⟷ 分部积分。微分有总是奏效的干净法则；积分是反向的搜寻，所以它需要巧妙的招数。同样的关系，更难的方向。

<a id="s10"></a>
## 让积分发挥作用

*任何累积起来的东西——面积、体积、长度、平均——都是一个积分。*

**两曲线之间的面积**

$$A=\int_a^b\big[f(x)-g(x)\big]\,dx$$

**旋转体体积——圆盘法**

$$V=\pi\int_a^b\big[f(x)\big]^2\,dx$$

**旋转体体积——壳层法**

$$V=2\pi\int_a^b x\,f(x)\,dx$$

**弧长**

$$L=\int_a^b\sqrt{1+\big[f'(x)\big]^2}\;dx$$

**函数的平均值**

$$\bar f=\frac{1}{b-a}\int_a^b f(x)\,dx$$

**演示 — 弧长公式从何而来**

1. 用许多微小的直线段去逼近曲线。每段有水平跨度 $dx$ 和竖直升高 $dy$。
2. 由勾股定理，线段长度是

   $$ds=\sqrt{dx^2+dy^2}.$$
3. 从根号中提出 $dx$，并使用 $\frac{dy}{dx}=f'(x)$：

   $$ds=\sqrt{1+\big(\tfrac{dy}{dx}\big)^2}\,dx=\sqrt{1+[f'(x)]^2}\,dx.$$
4. 把从 $a$ 到 $b$ 的所有微小长度积分（加总）起来：

   $$L=\int_a^b\sqrt{1+[f'(x)]^2}\,dx.$$

*这里每一条公式都用同一套配方：写出一个微小切片，再积分以求无穷多个之和——这就是第 7 节的黎曼思想。*

<a id="s11"></a>
## 数列与级数

*加起无穷多项——当总和有限时，我们能从函数的导数把函数重建出来。*

**几何级数**

$$\sum_{n=0}^{\infty} a r^{n}=\frac{a}{1-r}\quad(|r|<1)$$

**演示 — 几何求和公式**

1. 写出部分和：

   $$S_n=a+ar+ar^2+\cdots+ar^{n-1}.$$
2. 乘以 $r$：

   $$rS_n=ar+ar^2+\cdots+ar^{n}.$$
3. 相减——几乎所有项都消去：

   $$S_n-rS_n=a-ar^{n}\;\Rightarrow\; S_n=\frac{a(1-r^{n})}{1-r}.$$
4. 若 $|r|<1$，则当 $n\to\infty$ 时 $r^{n}\to0$：

   $$S=\frac{a}{1-r}.$$

**p-级数**

$$\sum_{n=1}^{\infty}\frac{1}{n^{p}}\ \text{converges} \iff p>1$$

### 收敛判别法的完整工具箱

| 判别法 | 表述 |
| --- | --- |
| 第 n 项（发散）判别法 | 若 $\lim a_n\neq 0$，级数发散 |
| 比值判别法 | $\lim\left\vert \frac{a_{n+1}}{a_n}\right\vert =L$；$L<1$ 收敛，$L>1$ 发散 |
| 根值判别法 | $\lim \vert a_n\vert ^{1/n}=L$；$L<1$ 收敛 |
| 比较判别法 | 用一个已知的收敛/发散级数从上/下界住 $a_n$ |
| 极限比较判别法 | 若 $\lim \frac{a_n}{b_n}$ 有限且为正，二者表现相同 |
| 积分判别法 | $\sum a_n$ 与 $\int_1^\infty f\,dx$ 同收敛或同发散 |
| 交错级数判别法 | 若 $b_n$ 递减趋于 $0$，则 $\sum(-1)^n b_n$ 收敛 |

**泰勒级数——由函数的导数重建函数**

$$f(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^{n}$$

*麦克劳林级数是 $a=0$ 的特例。它是线性近似（第 6 节）延续到无穷多阶导数。*

**演示 — 为什么系数是 $f^{(n)}(a)/n!$**

1. 设 $f(x)=c_0+c_1(x-a)+c_2(x-a)^2+\cdots$。令 $x=a$：除第一项外每项都消失，故 $c_0=f(a)$。
2. 求导一次，再令 $x=a$：只剩线性项存活，得 $c_1=f'(a)$。
3. 求导 $n$ 次：$(x-a)^n$ 项变成常数 $n!\,c_n$，其余在 $x=a$ 处全部消失：

   $$f^{(n)}(a)=n!\,c_n \;\Rightarrow\; c_n=\frac{f^{(n)}(a)}{n!}.$$

### 那些著名的展开

$$e^{x}=\sum_{n=0}^{\infty}\frac{x^{n}}{n!}=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots$$

$$\sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots,\qquad \cos x=1-\frac{x^2}{2!}+\frac{x^4}{4!}-\cdots$$

$$\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}-\cdots,\qquad \frac{1}{1-x}=\sum_{n=0}^{\infty}x^n\ (|x|<1)$$

> **统一性的一瞥**
>
> 把 $x=i\theta$ 代入 $e^x$ 级数，并用 $\sin$ 与 $\cos$ 级数重新分组：你会落在欧拉公式 $e^{i\theta}=\cos\theta+i\sin\theta$ 上。由导数构造出的级数，悄然把指数与振荡联系在一起。

<a id="s12"></a>
## 多元微积分的一瞥

*同样的两个思想——斜率与累积——在多于一维的情形里。*

**偏导数**

$$\frac{\partial f}{\partial x}=\lim_{h\to0}\frac{f(x+h,\,y)-f(x,\,y)}{h}$$

*对一个变量求导而保持其余变量不变——就是第 2 节的定义，只是把 $y$ 冻结了。*

**梯度（所有偏导数构成的向量）**

$$\nabla f=\left\langle \frac{\partial f}{\partial x},\ \frac{\partial f}{\partial y},\ \frac{\partial f}{\partial z}\right\rangle$$

*指向最陡上升的方向——导数在多元情形下的表亲。*

**多元链式法则**

$$\frac{df}{dt}=\frac{\partial f}{\partial x}\frac{dx}{dt}+\frac{\partial f}{\partial y}\frac{dy}{dt}$$

**二重积分（在一片区域上累积）**

$$\iint_{R} f(x,y)\,dA=\int_{c}^{d}\!\int_{a}^{b} f(x,y)\,dx\,dy$$

*一个曲面之下的体积——又是黎曼思想，只不过堆叠的是微小的盒子而非矩形。*

> **这一切通向何方**
>
> 从这里，路径通向那些伟大的积分定理（格林、斯托克斯、散度）——每一个都是更高维度的微积分基本定理，再次诉说着：边界上的行为由内部的行为所支配。

---

*先通读一遍把握形状，然后随时回到任一方框当作参考。让微积分豁然开朗的习惯：每当遇到一条新公式，就问它暗地里是哪条更早公式的一个版本——并试着凭记忆复现它的演示。这里几乎所有内容都由极限、乘积法则和链式法则构造而成。*
