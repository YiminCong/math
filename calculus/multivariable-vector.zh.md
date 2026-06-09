[English](multivariable-vector.md) · **中文**

# 多元，*互相连接。*

一门完整的第三学期课程——空间的几何、其上函数的微积分、在区域与曲面上的积分，以及伟大的向量微积分定理——按照从基础到进阶的顺序铺陈。每一个核心结论都从最底层**演示**出来，每一个符号在第一次出现时都给出定义，并把贯穿梯度、Green、Stokes 与 Gauss 的那条主线讲清楚。

本扩充版假设你**初次接触向量与多元函数**。请慢慢读；每一步都既说明*做了什么*，也说明*为什么这样做是允许的*。

[← 返回全部指南](../README.zh.md)

## A 部分 · 空间、向量与函数

<a id="s0"></a>
### 全局图景：从一元到多元

**本节讲什么、为什么重要。** 在你第一门微积分课程中，你研究的是*一元函数*，写作 $y=f(x)$。**函数**一词指的是一条规则：它接收一个输入数 $x$ 并恰好返回一个输出数 $y$。允许的输入构成的集合叫**定义域**；输出构成的集合叫**值域**。你学过对这类函数的三种运算：**极限**（当 $x$ 趋向某点时 $f(x)$ 所趋向的值）、**导数**（瞬时变化率，即图像的斜率）以及**积分**（累积总量，即图像下的面积）。多元微积分做的还是这同样的三件事，只不过现在输入可以同时是若干个数，输出也可以是若干个数。仅此一个改变，就重组了整门学科。

**新名词的定义。**

- **实数**就是数轴上普通的数；所有实数的集合记作 $\mathbb R$。
- $\mathbb R^n$（读作“R-n”）表示所有*由 $n$ 个实数构成的有序数组*的集合。于是 $\mathbb R^2$ 是平面（数组 $(x,y)$），$\mathbb R^3$ 是空间（数组 $(x,y,z)$）。$\mathbb R^n$ 中的一个元素称为一个**点**。
- **标量**是单个实数（与数组相对）。
- **标量场**是一个函数 $f:\mathbb R^n\to\mathbb R$：它吃掉空间中的一个点，返回一个数。例如：房间中各处的温度 $f(x,y,z)$。
- **向量场**是一个函数 $\mathbf F:\mathbb R^n\to\mathbb R^n$：它吃掉一个点，返回一整个箭头（在 §s1 中定义）。例如：各处空气的速度。
- **参数化**是描出一条曲线或一张曲面的函数；例如一条规则 $\mathbb R\to\mathbb R^3$ 把时间 $t$ 送到一个位置，从而画出一条路径。

这三种运算的升级版：

- **求导**——导数变成一整个*梯度向量*（一列斜率，每个输入变量一个；§s7），后来还会变成矩阵。它一次性编码了在*每一个*方向上的变化率。
- **积分**——积分变成在二维区域、三维实体、曲线或曲面上的求和。
- **连接**——一族定理（Green、Stokes、Gauss）把区域*内部*的导数与其*边界*上的值联系起来，恰如微积分基本定理在区间上所做的那样。

> **原理 — 组织全局的想法**
>
> 每个对象都按**有几个数进去**和**有几个数出来**来分类。**标量场** $f:\mathbb R^n\to\mathbb R$（温度）有梯度。**向量场** $\mathbf F:\mathbb R^n\to\mathbb R^n$（流、力）有旋度和散度。**参数化** $\mathbb R\to\mathbb R^3$ 或 $\mathbb R^2\to\mathbb R^3$ 描出一条曲线或一张曲面。知道类型就能知道该用哪个算子、哪种积分。

> **联系 — 你早已掌握的一个想法**
>
> 整门学科就是微积分基本定理 $\int_a^b f'\,dx=f(b)-f(a)$ 的推广：把一个导数在区域上积分，等于函数在该区域边界上的取值。记住这句话；第 27 节将说明四大定理都是它的特例。

#### 微积分基本定理说了什么（你会不断用到它）

因为本指南的一切都依赖它，这里用平实的语言给出陈述，并定义其中的术语。若 $F$ 是一个其导数为 $f$ 的函数（我们称 $F$ 是 $f$ 的一个**原函数**），那么 $f$ 从 $x=a$ 到 $x=b$ 所累积的面积，就只是 $F$ 的改变量：

$$\int_a^b f(x)\,dx=F(b)-F(a),\qquad\text{where } F'(x)=f(x).$$

符号 $\int_a^b$ 表示“在从 $a$ 到 $b$ 的区间上累加”；$dx$ 标明 $x$ 是被累加的变量。这条教益——*要累加一个变化率，你只需端点处的值*——正是后面每一个“大定理”的种子。

#### 整门课程浓缩为一行

> 向量与空间 → 多元函数 → 偏导数与梯度 → 优化 → 多重积分 → 向量场 → Green / Stokes / Gauss

<a id="s1"></a>
### 向量、点积与叉积

*向量带有大小与方向。两种乘积把向量变成描述角度、投影、面积与体积的语言。*

**本节讲什么、为什么重要。** 在空间中做微积分之前，我们需要空间的代数。**向量**是“某个大小、某个方向的推力”这一概念的数学对象。两种特殊的乘法——点积与叉积——让我们用纯算术计算角度、投影、面积和体积。后面几乎每一个公式（梯度、法向量、通量）都由这两种乘积搭建而成，所以我们要仔细定义它们并证明其关键性质。

> **概念 — 点、向量与两种乘积**
>
> 点是一个位置；**向量** $\mathbf v=\langle v_1,v_2,v_3\rangle$ 是一个位移。**点积**返回一个标量，度量对齐程度（从而度量角度与投影）；**叉积**返回一个与两者都垂直的向量，其长度等于二者张成的平行四边形的面积。点积关乎角度；叉积关乎面积与定向。

**定义 — 每个符号都讲清楚。**

- $\mathbb R^3$ 中的一个**向量**是三个数的有序数组 $\mathbf v=\langle v_1,v_2,v_3\rangle$，称为它的**分量**。我们用粗体印刷向量，并用尖括号。从几何上看它是一支箭头：$v_1$ 是它沿 $x$ 方向指出的远近，$v_2$ 沿 $y$，$v_3$ 沿 $z$。长度与方向相同的两支箭头是*同一个*向量，无论你画在何处。
- $\mathbf v$ 的**大小**（或**长度**、**范数**），记作 $|\mathbf v|$，是这支箭头的长短。
- 向量**相加**是分量相加：$\langle a_1,a_2,a_3\rangle+\langle b_1,b_2,b_3\rangle=\langle a_1+b_1,a_2+b_2,a_3+b_3\rangle$（首尾相接的箭头）。用一个数 $c$ **数乘**则是每个分量都乘以它：$c\langle a_1,a_2,a_3\rangle=\langle ca_1,ca_2,ca_3\rangle$（把箭头拉伸，若 $c<0$ 则反向）。
- 两个向量之间的夹角 $\theta$ 是把两支箭头的尾巴并在一起时所量出的角，取值范围 $[0,\pi]$。

**大小、点积、夹角**

$$|\mathbf v|=\sqrt{v_1^2+v_2^2+v_3^2},\qquad \mathbf a\cdot\mathbf b=\sum_i a_ib_i=|\mathbf a||\mathbf b|\cos\theta$$

*$\mathbf a\cdot\mathbf b=0\iff$ 垂直。$\mathbf a$ 在 $\mathbf b$ 上的标量投影是 $\dfrac{\mathbf a\cdot\mathbf b}{|\mathbf b|}$。*

这里**点积** $\mathbf a\cdot\mathbf b$ 由中间那个表达式 $\sum_i a_ib_i = a_1b_1+a_2b_2+a_3b_3$ 定义——对应分量相乘再相加。它输出单个数（一个标量）。符号 $\theta$ 是两支箭头之间的夹角；$\cos\theta$ 是该角的余弦。大小公式不过是三维中的勾股定理：边长为 $|v_1|,|v_2|,|v_3|$ 的长方体的对角线。

**叉积（在 $\mathbb R^3$ 中）**

$$\mathbf a\times\mathbf b=\begin{vmatrix}\mathbf i&\mathbf j&\mathbf k\\ a_1&a_2&a_3\\ b_1&b_2&b_3\end{vmatrix},\qquad |\mathbf a\times\mathbf b|=|\mathbf a||\mathbf b|\sin\theta$$

*$\mathbf a\times\mathbf b$ 与两者都垂直，方向由右手定则给出；其长度是平行四边形面积。$\mathbf a\times\mathbf b=-\,\mathbf b\times\mathbf a$。*

本块中的定义：$\mathbf i=\langle1,0,0\rangle$、$\mathbf j=\langle0,1,0\rangle$、$\mathbf k=\langle0,0,1\rangle$ 是**标准基向量**（沿三条坐标轴的单位箭头）。竖直高条 $\begin{vmatrix}\cdots\end{vmatrix}$ 表示**行列式**，是一套特定的算术配方；把这个 $3\times3$ 行列式展开，得到显式公式

$$\mathbf a\times\mathbf b=\langle a_2b_3-a_3b_2,\; a_3b_1-a_1b_3,\; a_1b_2-a_2b_1\rangle.$$

**右手定则**：让右手的手指沿 $\mathbf a$ 指出，再朝 $\mathbf b$ 卷曲；大拇指便指向 $\mathbf a\times\mathbf b$。

**标量三重积 → 体积**

$$V=\big|\,\mathbf a\cdot(\mathbf b\times\mathbf c)\,\big|=\left|\det\!\begin{pmatrix}a_1&a_2&a_3\\ b_1&b_2&b_3\\ c_1&c_2&c_3\end{pmatrix}\right|$$

*平行六面体的有符号体积。等于零 $\iff$ 三个向量共面。*

**平行六面体**是平行四边形的三维类比：从一个角出发以 $\mathbf a,\mathbf b,\mathbf c$ 为棱的斜长方体。**共面**意味着三支箭头都落在同一个平面内（这时该盒子被压扁，体积为零）。

**演示 — 点积给出夹角**

我们证明几何恒等式 $\mathbf a\cdot\mathbf b=|\mathbf a||\mathbf b|\cos\theta$，即分量公式等于夹角公式。

1. 把 $\mathbf a,\mathbf b$ 尾对尾摆放。从 $\mathbf b$ 的尖端指向 $\mathbf a$ 尖端的箭头是向量 $\mathbf a-\mathbf b$（上面定义的向量减法），于是这三个向量构成一个三角形，三边为 $|\mathbf a|$、$|\mathbf b|$、$|\mathbf a-\mathbf b|$，前两边之间的夹角为 $\theta$。**余弦定理**（平面几何的一个标准事实，推广了勾股定理）给出

   $$|\mathbf a-\mathbf b|^2=|\mathbf a|^2+|\mathbf b|^2-2|\mathbf a||\mathbf b|\cos\theta.$$
2. 用点积的*分量*定义展开左边。首先注意两个由 $\mathbf u\cdot\mathbf u=\sum u_i^2=|\mathbf u|^2$ 及求和 $\sum$ 的分配律直接得到的事实：

   $$|\mathbf a-\mathbf b|^2=(\mathbf a-\mathbf b)\cdot(\mathbf a-\mathbf b)=\mathbf a\cdot\mathbf a-2\,\mathbf a\cdot\mathbf b+\mathbf b\cdot\mathbf b=|\mathbf a|^2-2\,\mathbf a\cdot\mathbf b+|\mathbf b|^2.$$

   （中间这一步用到点积对加法满足分配律——因为它是逐分量乘积之和，故为真——以及 $\mathbf a\cdot\mathbf b=\mathbf b\cdot\mathbf a$，这又是因为数的乘法可交换。）
3. 第 1 步与第 2 步的左边是同一个量，于是令右边相等。$|\mathbf a|^2$ 与 $|\mathbf b|^2$ 两项在两边都出现，相消，剩下 $-2\,\mathbf a\cdot\mathbf b=-2|\mathbf a||\mathbf b|\cos\theta$。两边除以 $-2$：

   $$\mathbf a\cdot\mathbf b=|\mathbf a||\mathbf b|\cos\theta.\qquad\blacksquare$$

*几何（角度）与代数（分量之和）是同一个运算的两面。* 特别地，由于对非零向量有 $|\mathbf a||\mathbf b|>0$，$\mathbf a\cdot\mathbf b=0$ 就迫使 $\cos\theta=0$，即 $\theta=90^\circ$——这正是点积为零意味着垂直的原因。

**习题示例（点积、夹角、投影）。** 设 $\mathbf a=\langle 1,2,2\rangle$ 与 $\mathbf b=\langle 2,0,-1\rangle$。

- 大小：$|\mathbf a|=\sqrt{1^2+2^2+2^2}=\sqrt9=3$ 且 $|\mathbf b|=\sqrt{2^2+0^2+(-1)^2}=\sqrt5$。
- 点积：$\mathbf a\cdot\mathbf b=(1)(2)+(2)(0)+(2)(-1)=2+0-2=0$。因为它等于 $0$，所以 $\mathbf a$ 与 $\mathbf b$ **垂直**（$\theta=90^\circ$），且标量投影 $\frac{\mathbf a\cdot\mathbf b}{|\mathbf b|}=\frac{0}{\sqrt5}=0$。

**习题示例（叉积与面积）。** 仍取 $\mathbf a=\langle1,2,2\rangle$、$\mathbf b=\langle2,0,-1\rangle$，显式公式给出

$$\mathbf a\times\mathbf b=\langle (2)(-1)-(2)(0),\ (2)(2)-(1)(-1),\ (1)(0)-(2)(2)\rangle=\langle -2,\ 5,\ -4\rangle.$$

其长度 $|\mathbf a\times\mathbf b|=\sqrt{(-2)^2+5^2+(-4)^2}=\sqrt{4+25+16}=\sqrt{45}=3\sqrt5$ 就是 $\mathbf a,\mathbf b$ 张成的平行四边形的面积。用 $|\mathbf a||\mathbf b|\sin\theta$ 核对：因为 $\theta=90^\circ$，$\sin\theta=1$，且 $|\mathbf a||\mathbf b|=3\sqrt5$——二者一致。还有 $\mathbf a\cdot(\mathbf a\times\mathbf b)=(1)(-2)+(2)(5)+(2)(-4)=-2+10-8=0$，确认叉积如所言与 $\mathbf a$ 垂直。

**常见陷阱。** 点积产生一个*数*；叉积产生一个*向量*——千万别混淆。叉积*不*满足交换律：$\mathbf a\times\mathbf b=-\mathbf b\times\mathbf a$（交换行列式的两行会翻转其符号）。叉积只在 $\mathbb R^3$ 中有定义。

<a id="s2"></a>
### 直线、平面与二次曲面

*有了向量在手，空间中的基本对象就得到了简洁的方程：一条直线需要一个点和一个方向；一个平面需要一个点和一个法向量。*

**本节讲什么、为什么重要。** 直线与平面是空间中最简单的、不带弯曲的形状，我们会处处遇到它们——曲线的切线、曲面的切平面（§s8）。关键洞见在于：向量可以各用一个简短的方程来描述它们。我们将定义**方向向量**与**法向量**，推导这些方程，并证明点到平面的距离公式。

**过 $P_0$、方向为 $\mathbf v$ 的直线**

$$\mathbf r(t)=\mathbf r_0+t\mathbf v,\qquad \frac{x-x_0}{v_1}=\frac{y-y_0}{v_2}=\frac{z-z_0}{v_3}$$

*向量形式（左）与对称形式（右）。一条直线就是一个点加上某一方向的所有数乘。*

定义：$P_0=(x_0,y_0,z_0)$ 是直线上一个已知点，$\mathbf r_0=\langle x_0,y_0,z_0\rangle$ 是它的**位置向量**（从原点指向 $P_0$ 的箭头）。**方向向量** $\mathbf v=\langle v_1,v_2,v_3\rangle$ 沿直线指出。**参数** $t$ 是一个实数旋钮：当 $t$ 取遍所有实数时，$\mathbf r(t)=\mathbf r_0+t\mathbf v$ 扫过直线上的每一个点，因为加上 $t\mathbf v$ 会把 $P_0$ 沿该方向向前（或向后）滑动。把每个分量方程 $x=x_0+tv_1$ 等解出 $t$ 再令其相等，便得右边的对称形式。

**过 $P_0$、法向量为 $\mathbf n$ 的平面**

$$\mathbf n\cdot(\mathbf r-\mathbf r_0)=0\ \Longleftrightarrow\ a(x-x_0)+b(y-y_0)+c(z-z_0)=0$$

*一个点落在平面上当且仅当它相对于 $P_0$ 的位移垂直于 $\mathbf n=\langle a,b,c\rangle$。法向量可直接从系数读出。*

**法向量** $\mathbf n=\langle a,b,c\rangle$ 是一个垂直于该平面的向量。推理：点 $P=(x,y,z)$ 落在平面内当且仅当位移 $\mathbf r-\mathbf r_0=\langle x-x_0,y-y_0,z-z_0\rangle$ 留在平面内，即垂直于 $\mathbf n$。根据 §s1 的点积判据（$\mathbf a\cdot\mathbf b=0\iff$ 垂直），这恰好就是 $\mathbf n\cdot(\mathbf r-\mathbf r_0)=0$。用分量展开点积便得右边的方程。若把它乘开为 $ax+by+cz+d=0$ 的形式，则 $d=-(ax_0+by_0+cz_0)$。

**点到平面的距离**

$$D=\frac{|a x_1+b y_1+c z_1+d|}{\sqrt{a^2+b^2+c^2}}$$

*它是 $\overrightarrow{P_0P_1}$ 在单位法向量上投影的长度——一个点积除以 $|\mathbf n|$。*

**演示 — 距离公式。** 我们想求点 $P_1=(x_1,y_1,z_1)$ 到平面 $ax+by+cz+d=0$ 的最短距离 $D$。

1. 在平面上任取一点 $P_0=(x_0,y_0,z_0)$，于是它满足 $ax_0+by_0+cz_0+d=0$，即 $d=-(ax_0+by_0+cz_0)$。从 $P_0$ 到 $P_1$ 的向量是 $\overrightarrow{P_0P_1}=\langle x_1-x_0,\,y_1-y_0,\,z_1-z_0\rangle$。
2. 距离 $D$ 是 $\overrightarrow{P_0P_1}$ 在法向量 $\mathbf n=\langle a,b,c\rangle$ 上*投影*的长度，因为从一点到平面的最短路径正好沿法线方向。标量投影（来自 §s1）的绝对值为

   $$D=\frac{|\,\mathbf n\cdot\overrightarrow{P_0P_1}\,|}{|\mathbf n|}.$$
3. 计算分子：$\mathbf n\cdot\overrightarrow{P_0P_1}=a(x_1-x_0)+b(y_1-y_0)+c(z_1-z_0)=ax_1+by_1+cz_1-(ax_0+by_0+cz_0)$。代入第 1 步的 $-(ax_0+by_0+cz_0)=d$：分子变成 $ax_1+by_1+cz_1+d$。
4. 由于 $|\mathbf n|=\sqrt{a^2+b^2+c^2}$，把第 2、3 步合起来便得方框中的公式。$\blacksquare$

**习题示例。** 平面 $2x-y+2z=6$（于是 $a=2,b=-1,c=2,d=-6$），点 $P_1=(3,0,0)$。则 $|2\cdot3-1\cdot0+2\cdot0-6|=|0|=0$——该点*在*平面上（核对：$2\cdot3=6$）。改取 $P_1=(0,0,0)$：距离 $=\frac{|0+0+0-6|}{\sqrt{4+1+4}}=\frac{6}{3}=2$。所以原点离该平面 2 个单位。

> **概念 — 用截痕认识二次曲面**
>
> 这些二次曲面——**椭球面** $\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}=1$、**抛物面** $z=x^2+y^2$、**圆锥面** $z^2=x^2+y^2$、**双曲面**、**鞍面** $z=x^2-y^2$——最好通过它们的*截痕*来理解：用坐标平面去切所得到的曲线。把某个变量取为常数，读出由此产生的圆锥曲线即可。

**二次曲面**是 $x,y,z$ 的二次方程的图像。**截痕**是与诸如 $z=k$ 这样的平面的交线（令 $z$ 等于一个常数 $k$，看剩下的关于 $x,y$ 的方程）。对于抛物面 $z=x^2+y^2$，在高度 $z=k$ 处的截痕是 $x^2+y^2=k$，当 $k>0$ 时它是半径为 $\sqrt k$ 的圆——所以该曲面是一摞越来越大的圆，呈碗状。在 $x=0$ 处截取得到 $z=y^2$，一条抛物线；它的名字便由此而来。

<a id="s3"></a>
### 多元函数；等值线与等值面

*函数 $z=f(x,y)$ 给平面上每个点赋一个高度——一片地貌。把这片地貌平铺着读出来，最清爽的方式是等高线图。*

**本节讲什么、为什么重要。** 现在我们遇到核心主角：一个输入是*点*、输出是*数*的函数。把它可视化是第一道坎，而两件工具——图像（一张曲面）与等值集（一张等高线图）——会训练你在梯度、优化与积分中要用到的直觉。

> **概念 — 图像 vs. 等值集**
>
> $f(x,y)$ 的**图像**是 $\mathbb R^3$ 中的一张曲面。**等值线** $f(x,y)=k$ 收集所有给出相同输出 $k$ 的输入——一条等高线，就像地形图上那样。对于 $f(x,y,z)$，$f=k$ 是一张**等值面**。等高线密集意味着地势陡峭；梯度（第 7 节）将横切它们而指。

**定义。** **二元函数** $z=f(x,y)$ 给每一对输入 $(x,y)$ 赋一个输出数 $z$。它的**图像**是空间中点 $(x,y,f(x,y))$ 构成的集合——通常是悬于 $xy$ 平面之上的一张曲面，以 $f(x,y)$ 为高度。在水平 $k$ 处的**等值线**是高度等于固定值 $k$ 的输入点之集合：$\{(x,y):f(x,y)=k\}$。在平坦的 $xy$ 平面上画出若干条等值线，恰好就是一张地形/等高线图。

**定义域、值域、等值集**

$$f:D\subseteq\mathbb R^n\to\mathbb R,\qquad \text{level set}=\{\,\mathbf x: f(\mathbf x)=k\,\}$$

*务必先确定定义域：$\sqrt{}$ 要求自变量非负，$\ln$ 要求为正，分母必须非零。*

这里 $D\subseteq\mathbb R^n$ 是**定义域**（符号 $\subseteq$ 表示“是……的子集”，即 $D$ 是 $\mathbb R^n$ 的一部分）：使规则有意义的那些输入之集合。箭头 $\to\mathbb R$ 表示输出是单个实数。$\mathbf x$ 代表输入点 $(x_1,\dots,x_n)$。

**习题示例（定义域与等值线）。** 设 $f(x,y)=\sqrt{9-x^2-y^2}$。

- **定义域。** 平方根要求自变量非负：$9-x^2-y^2\ge0$，即 $x^2+y^2\le9$。定义域是以原点为心、半径为 $3$ 的闭圆盘。
- **图像。** 令 $z=\sqrt{9-x^2-y^2}\ge0$ 并平方得 $x^2+y^2+z^2=9$ 且 $z\ge0$——即半径为 $3$ 的球面的上半部分。
- **等值线。** 解 $f=k$：$\sqrt{9-x^2-y^2}=k\Rightarrow x^2+y^2=9-k^2$。对每个介于 $0$ 与 $3$ 之间的高度 $k$，这是半径为 $\sqrt{9-k^2}$ 的圆。当 $k$ 升向 $3$ 时，这些圆缩成穹顶顶部的一个点——边缘附近紧密排布的等高线说明那里坡度陡峭。

> **联系 — 回到一元情形**
>
> 等值线是“解 $f(x)=k$”的多元表亲。通过等值集——而非图像——来读一个函数，是让梯度、Lagrange 乘子与隐函数求导显得自然的视觉习惯。

<a id="s4"></a>
### 多元的极限与连续性

*极限的定义看起来一样，但有一个特征是真正新的：在平面上你可以从无穷多个方向逼近一个点，而极限必须沿所有这些方向都一致。*

**本节讲什么、为什么重要。** **极限**刻画当输入悄悄爬向目标时函数所趋向的值。一元情形只有两条进路（从左、从右）。在平面上有无穷多条通向一个点的路径，而真正的极限必须沿所有这些路径给出*同一个*答案。这是最常见的“极限不存在”论证的来源，也是**连续性**（没有跳跃）含义的根基，而我们在求导之前需要它。

**极限与连续性**

$$\lim_{(x,y)\to(a,b)}f(x,y)=L:\ \forall\varepsilon>0\ \exists\delta>0,\ 0<|(x,y)-(a,b)|<\delta\Rightarrow|f-L|<\varepsilon$$

$$f \text{ continuous at }(a,b)\iff \lim_{(x,y)\to(a,b)}f(x,y)=f(a,b)$$

**读懂这些符号。** $\lim$ 表示“所趋向的值”。符号 $\forall$ 表示“对每一个”，$\exists$ 表示“存在”。$\varepsilon$（epsilon）与 $\delta$（delta）是很小的正距离。这句话说的是：*无论你在目标输出 $L$ 周围要求多紧的容差 $\varepsilon$，都存在输入点 $(a,b)$ 周围一个足够小的半径 $\delta$，使得每一个距离在 $\delta$ 之内（但不是该点本身，故 $0<$）的输入都落在 $L$ 的 $\varepsilon$ 之内。* 距离 $|(x,y)-(a,b)|=\sqrt{(x-a)^2+(y-b)^2}$ 就是普通的平面距离。在某点**连续**意味着极限存在*并且*等于实际取值 $f(a,b)$——图像在那里没有洞、也没有跳跃。

> **原理 — 两路径判别法**
>
> 若 $f$ 沿两条通向 $(a,b)$ 的不同路径趋向*不同*的值，则极限**不存在**。这是标准工具：试 $y=0$，再试 $x=0$，再试 $y=mx$，再试 $y=x^2$。只要有一处不一致便可定论。

为何这个判别法成立：定义要求存在一个对*所有*邻近输入同时奏效的单一的 $L$。任何一条特定路径都是这些输入的子集，所以若极限 $L$ 存在，则每条路径都必须趋向同一个 $L$。因此两条极限不同的路径使这样的 $L$ 不可能存在。

**演示 — 一个通不过路径判别法的极限**

1. 考虑 $f(x,y)=\dfrac{xy}{x^2+y^2}$ 当 $(x,y)\to(0,0)$。沿 $x$ 轴逼近，即令 $y=0$ 并让 $x\to0$：

   $$f(x,0)=\frac{x\cdot0}{x^2+0^2}=\frac{0}{x^2}=0\quad\Rightarrow\quad\text{limit along this path }=0.$$
2. 现在沿对角线 $y=x$ 逼近，并让 $x\to0$：

   $$f(x,x)=\frac{x\cdot x}{x^2+x^2}=\frac{x^2}{2x^2}=\frac12\quad\Rightarrow\quad\text{limit along this path }=\tfrac12.$$
3. 两条路径给出 $0$ 与 $\tfrac12$。由于不一致，按两路径原理，极限**不存在**——尽管每个单变量切片都温顺得很。$\blacksquare$

*只从一个方向逼近永远不够；极限必须从所有方向一致地成立。*

**习题示例（一个确实存在的极限）。** 考虑 $g(x,y)=\dfrac{x^2y}{x^2+y^2}$ 在 $(0,0)$ 处。这里分子“强”了一个次数。利用 $|x|\le\sqrt{x^2+y^2}$、$|y|\le\sqrt{x^2+y^2}$ 以及 $\frac{x^2}{x^2+y^2}\le1$：

$$\left|\frac{x^2y}{x^2+y^2}\right|=\frac{x^2}{x^2+y^2}\,|y|\le 1\cdot|y|\le\sqrt{x^2+y^2}.$$

当 $(x,y)\to(0,0)$ 时右边 $\to0$，所以 $g$ 沿*每一条*路径都趋向 $0$。因此极限是 $0$。（这就是夹逼/比较的想法：把 $|g|$ 夹在 $0$ 与某个趋于零的量之间。）

**常见陷阱。** 沿 $x$ 轴与 $y$ 轴一致*并不*能证明极限存在——上面的反例沿两条轴都一致（$0$），却没有极限。你必须检验足够多的路径，或者更好地，像习题示例那样找一个界。

## B 部分 · 多元微分学

<a id="s5"></a>
### 偏导数

*要对多元函数求导，就把除一个之外的所有变量冻结，然后照常求导。每个变量都有自己的斜率。*

**本节讲什么、为什么重要。** 一元函数 $f(x)$ 的导数是它的斜率，$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$——纵增比横增在横增 $h$ 收缩时的极限。有多个输入时不存在单一的斜率；取而代之的是每个输入方向各有一个斜率，即**偏导数**。它们是梯度、链式法则、优化以及后面每一个微分算子的原材料。

**偏导数的定义**

$$f_x(a,b)=\frac{\partial f}{\partial x}=\lim_{h\to0}\frac{f(a+h,b)-f(a,b)}{h}$$

*$f_x$ 是曲面在 $x$ 方向上的斜率——把 $y$ 当常数固定后所得单变量切片 $g(x)=f(x,b)$ 的普通导数。*

记号：$f_x$ 与 $\frac{\partial f}{\partial x}$ 都表示“$f$ 关于 $x$ 的偏导数”。圆头的 $\partial$（读作“偏 dee”）把它与普通的 $d$ 区分开来，提醒我们其他变量被固定住了。在极限中，$h$ 只微动第一个输入；第二个保持在 $b$。所以 $f_x$ 实际上就是冻结 $y=b$ 后所得函数 $g(x)=f(x,b)$ 的普通导数。

> **概念 — “把其余的当常数”**
>
> 计算 $\partial f/\partial x$ 时，其他每个变量都是常数。于是 $\partial_x(x^2y^3)=2xy^3$ 而 $\partial_y(x^2y^3)=3x^2y^2$。所有单变量法则（乘积、商、链式）都原封不动地适用；只有你对“什么是常数”的看法发生了切换。

**习题示例（全部一阶偏导）。** 设 $f(x,y)=x^2y^3+\sin(xy)+e^{x}$。

- $f_x$：把 $y$ 当常数。$x^2y^3$ 的导数是 $2xy^3$（对 $x$ 用幂法则，$y^3$ 是常数乘子）。$\sin(xy)$ 的导数是 $\cos(xy)\cdot y$（链式法则：内层 $xy$ 关于 $x$ 的导数是 $y$）。$e^x$ 的导数是 $e^x$。所以 $f_x=2xy^3+y\cos(xy)+e^x$。
- $f_y$：把 $x$ 当常数。$x^2y^3$ 的导数是 $x^2\cdot3y^2=3x^2y^2$。$\sin(xy)$ 的导数是 $\cos(xy)\cdot x$。$e^x$ 的导数是 $0$（不含 $y$）。所以 $f_y=3x^2y^2+x\cos(xy)$。

**习题示例（数值斜率）。** 对 $f(x,y)=x^2y^3$ 在点 $(a,b)=(2,1)$ 处：$f_x=2xy^3=2(2)(1)^3=4$，$f_y=3x^2y^2=3(4)(1)=12$。所以沿 $+x$ 方向移动时，曲面每走一个单位约升高 $4$ 个单位，沿 $+y$ 约升高 $12$——在此处它在 $y$ 方向更陡。

> **联系 — 斜率拼装成梯度**
>
> $n$ 元函数有 $n$ 个一阶偏导。把它们收进一个向量 $\nabla f=\langle f_x,f_y,\dots\rangle$，就成了**梯度**（第 7 节）——这个单一对象扮演着导数 $f'(x)$ 在一元情形中所扮演的角色。

<a id="s6"></a>
### 多元链式法则

*当变量依赖于别的变量时，贡献沿每一条路径流动并相加。链式法则变成对各条路径的求和。*

**本节讲什么、为什么重要。** 一元链式法则说 $\frac{d}{dt}f(g(t))=f'(g(t))g'(t)$——要对复合函数求导，把外层变化率乘以内层变化率。当输出依赖若干个中间变量、而每个中间变量又依赖底层变量时，变化量相加：你沿每条路径相乘，再对各路径求和。这条法则驱动着方向导数、保守场理论，以及线积分基本定理的证明。

**链式法则 — 两种主要情形**

$$\frac{df}{dt}=\frac{\partial f}{\partial x}\frac{dx}{dt}+\frac{\partial f}{\partial y}\frac{dy}{dt}\qquad\big(x=x(t),\,y=y(t)\big)$$

$$\frac{\partial f}{\partial s}=\frac{\partial f}{\partial x}\frac{\partial x}{\partial s}+\frac{\partial f}{\partial y}\frac{\partial y}{\partial s}\qquad\big(x=x(s,t),\,y=y(s,t)\big)$$

*画一棵树：对从输出到你要求导的那个变量的每一条路径求和，沿每条路径相乘。*

这里 $f$ 依赖 $x$ 与 $y$，而它们又依赖 $t$（第一种情形）或依赖 $s,t$（第二种情形）。项 $\frac{\partial f}{\partial x}\frac{dx}{dt}$ 是 $t$ *通过* $x$ 作用引起的 $f$ 的变化；另一项是*通过* $y$ 的变化；总变化是它们之和，因为到一阶为止，相互独立的贡献是相加的。

**它为何成立（带定义的概述）。** 一个小变化 $\Delta t$ 产生小变化 $\Delta x\approx\frac{dx}{dt}\Delta t$ 与 $\Delta y\approx\frac{dy}{dt}\Delta t$。对可微的 $f$，由此产生的变化是 $\Delta f\approx f_x\,\Delta x+f_y\,\Delta y$（这个线性估计就是 §s8 的全微分）。代入并除以 $\Delta t$，再令 $\Delta t\to0$，即得所示公式。

**习题示例。** 设 $f(x,y)=x^2y$，其中 $x=\cos t$，$y=\sin t$。则 $f_x=2xy$，$f_y=x^2$，$\frac{dx}{dt}=-\sin t$，$\frac{dy}{dt}=\cos t$。于是

$$\frac{df}{dt}=2xy(-\sin t)+x^2(\cos t)=2\cos t\sin t(-\sin t)+\cos^2t\cos t=-2\sin^2t\cos t+\cos^3t.$$

先代入再核对：$f=\cos^2t\sin t$，乘积法则给出 $\frac{df}{dt}=2\cos t(-\sin t)\sin t+\cos^2t\cos t=-2\cos t\sin^2t+\cos^3t$——同样的答案，验证了链式法则。

> **联系 — 它是梯度点乘速度**
>
> 第一种情形恰好是 $\dfrac{df}{dt}=\nabla f\cdot \mathbf r'(t)$，即梯度点乘路径的速度。这个单一恒等式将以方向导数（第 7 节）的身份、以及线积分基本定理被积函数（第 20 节）的身份再度出现。

**演示 — 由链式法则得到隐函数求导**

1. 设方程 $F(x,y)=0$ 暗中把 $y$ 定义为 $x$ 的函数（一条**等值线**，§s3）。两边关于 $x$ 求导，把 $y=y(x)$ 看待并用链式法则（直接通过 $x$ 的路径，加上通过 $y$ 的路径）：

   $$\frac{\partial F}{\partial x}\frac{dx}{dx}+\frac{\partial F}{\partial y}\frac{dy}{dx}=\frac{d}{dx}(0)=0.$$
2. 由于 $\frac{dx}{dx}=1$，这就是 $F_x+F_y\frac{dy}{dx}=0$。解出斜率（当 $F_y\neq0$ 时允许，因为这时要除以它）：

   $$\frac{dy}{dx}=-\frac{F_x}{F_y}\qquad(F_y\neq0).\qquad\blacksquare$$

**习题示例。** 圆 $x^2+y^2-25=0$ 有 $F_x=2x$，$F_y=2y$，所以 $\frac{dy}{dx}=-\frac{2x}{2y}=-\frac{x}{y}$。在 $(3,4)$ 处斜率是 $-\frac34$——与圆的切线垂直于半径相符。

*微积分 I 里那条神秘的隐函数求导法则，不过是把链式法则用到一条等值线上。*

<a id="s7"></a>
### 方向导数与梯度

偏导给出沿坐标轴的斜率。方向导数给出沿*任意*方向的斜率——而梯度把它们全部打包。

**本节讲什么、为什么重要。** 偏导数只告诉你沿 $x$ 或沿 $y$ 的斜率。但你可以朝任意方向走。**方向导数**是沿任意一个方向的斜率，而引人注目的是，它只需与**梯度**——所有偏导构成的向量——做一次点积即可算出。然后会发现梯度指向上坡最快的方向，并且垂直于等值集，这两个事实组织起优化、切平面与 Lagrange 乘子。

**梯度与方向导数**

$$\nabla f=\Big\langle \frac{\partial f}{\partial x},\frac{\partial f}{\partial y},\frac{\partial f}{\partial z}\Big\rangle,\qquad D_{\mathbf u}f=\nabla f\cdot\mathbf u\quad(|\mathbf u|=1)$$

*你沿单位方向 $\mathbf u$ 迈步时 $f$ 的变化率，就是梯度投影到 $\mathbf u$ 上的结果。*

定义：**梯度** $\nabla f$（读作“del f”或“grad f”）是以各偏导数为分量的向量。**单位向量** $\mathbf u$ 是长度为 $1$ 的向量（$|\mathbf u|=1$）；它指定一个纯方向。**方向导数** $D_{\mathbf u}f$ 是当你从该点以单位速率沿方向 $\mathbf u$ 移动时 $f$ 的瞬时变化率。公式 $D_{\mathbf u}f=\nabla f\cdot\mathbf u$ 直接来自 §s6 的链式法则：若 $\mathbf r(t)$ 以速度 $\mathbf u$ 经过该点，则 $\frac{d}{dt}f(\mathbf r(t))=\nabla f\cdot\mathbf u$。

> **概念 — 让梯度不可或缺的三个事实**
>
> (1) $\nabla f$ 指向**最速上升**方向；(2) 它的大小 $|\nabla f|$ 就是那个最陡的斜率；(3) $\nabla f$ **垂直于过该点的等值集**。这三者一起把一列偏导变成一支几何箭头。

**演示 — 梯度是最速上升的方向**

1. 沿单位方向 $\mathbf u$ 的斜率是 $D_{\mathbf u}f=\nabla f\cdot\mathbf u$（上面的定义）。
2. 用 $\nabla f$ 与 $\mathbf u$ 的夹角 $\theta$ 写出点积，利用点积的夹角形式（§s1）及 $|\mathbf u|=1$：

   $$D_{\mathbf u}f=|\nabla f|\,|\mathbf u|\cos\theta=|\nabla f|\cos\theta.$$
3. 当 $\mathbf u$ 变化时，只有 $\cos\theta$ 变化，而 $\cos\theta$ 取遍 $[-1,1]$。它在 $\cos\theta=1$ 时最大，恰好当 $\theta=0$——即 $\mathbf u$ 与 $\nabla f$ 同向。这时 $D_{\mathbf u}f=|\nabla f|$，是最速上升。最小值 $\cos\theta=-1$ 在 $\theta=180^\circ$ 处，给出 $-|\nabla f|$（最速下降），而 $\theta=90^\circ$ 给出 $0$。$\blacksquare$

*因此梯度指向上坡最快的方向，陡度为 $|\nabla f|$——而零变化率的方向恰好沿等值集，这证明了 $\nabla f\perp$ 等值集。*

**习题示例。** 设 $f(x,y)=x^2+y^2$ 在点 $(3,4)$ 处。则 $\nabla f=\langle 2x,2y\rangle=\langle 6,8\rangle$，$|\nabla f|=\sqrt{36+64}=10$。最速上升方向是 $\frac{1}{10}\langle6,8\rangle=\langle0.6,0.8\rangle$，最陡斜率是 $10$。朝比如说 $\mathbf u=\langle1,0\rangle$（$+x$ 方向）的方向导数是 $\nabla f\cdot\mathbf u=6$。注意 $\nabla f=\langle6,8\rangle$ 沿径向向外指——垂直于过 $(3,4)$ 的等值圆 $x^2+y^2=25$，正如垂直性论断所预言。

> **联系 — 垂直于等值集**
>
> 沿一条等值线 $f$ 不变，所以对与之相切的 $\mathbf u$ 有 $D_{\mathbf u}f=0$，迫使 $\nabla f\perp\mathbf u$。这正是 $\nabla F$ 为曲面 $F=k$ 的法向量的原因（第 8 节），也是约束最优点处梯度对齐的原因（Lagrange，第 11 节）。

<a id="s8"></a>
### 切平面、线性逼近与微分

*放大一张光滑曲面，它看起来是平的。那个平的逼近就是切平面——切线的多元版本。*

**本节讲什么、为什么重要。** 在一元情形中，在某点附近曲线可由它的切线很好地逼近，$L(x)=f(a)+f'(a)(x-a)$。在二元情形中，曲线变成曲面，切*线*变成切*平面*。这个线性逼近是我们估计函数值、传播测量误差，以及在更高维定义“可微”应有含义的方式。

**$z=f(x,y)$ 的切平面与线性化**

$$z=f(a,b)+f_x(a,b)(x-a)+f_y(a,b)(y-b)$$

$$L(x,y)=f(a,b)+\nabla f(a,b)\cdot\langle x-a,\,y-b\rangle$$

*与 $y=f(a)+f'(a)(x-a)$ 形式相同：值加上斜率乘位移，只是现在由梯度在两个方向上提供斜率。*

推理：平面必须过 $(a,b,f(a,b))$ 并具有正确的斜率。固定 $y=b$，切片在 $x$ 方向上必须有斜率 $f_x(a,b)$；固定 $x=a$，在 $y$ 方向上斜率为 $f_y(a,b)$。满足这些条件的唯一平面就是所示的那个。两个所示形式是相同的，因为点积 $\nabla f\cdot\langle x-a,y-b\rangle=f_x(x-a)+f_y(y-b)$。

**等值面 $F(x,y,z)=k$ 的切平面**

$$\nabla F(P)\cdot\langle x-x_0,\,y-y_0,\,z-z_0\rangle=0$$

*因为 $\nabla F$ 是曲面法向量（第 7 节），所以切平面就是“点 + 垂直于梯度的平面”。*

这不过是 §s2 中以 $\mathbf n=\nabla F(P)$ 为法向量的平面方程，用到了梯度垂直于等值面（§s7）。

**全微分**

$$df=f_x\,dx+f_y\,dy+f_z\,dz$$

*对输入做小幅微动时输出如何变化的一阶估计——误差传播的主力工具。*

**微分** $dx,dy,dz$ 代表输入的小变化；$df$ 是由此估计出的输出变化。这个公式只是说每个输入的变化贡献它的斜率乘以它的大小，再把这些加起来——与切平面相同的线性想法。

**习题示例（线性逼近）。** 估计 $\sqrt{(3.02)^2+(3.97)^2}$。设 $f(x,y)=\sqrt{x^2+y^2}$ 在 $(a,b)=(3,4)$ 处，那里 $f=5$。则 $f_x=\frac{x}{\sqrt{x^2+y^2}}=\frac{3}{5}$，$f_y=\frac{y}{\sqrt{x^2+y^2}}=\frac{4}{5}$。取 $\Delta x=0.02$，$\Delta y=-0.03$：

$$f\approx 5+\tfrac35(0.02)+\tfrac45(-0.03)=5+0.012-0.024=4.988.$$

精确值是 $\sqrt{9.1204+15.7609}=\sqrt{24.8813}\approx4.98812$——线性估计精确到四位小数。

> **联系 — 可微不止是偏导存在**
>
> 一个函数在某点**可微**，如果切平面确实逼近它（误差比距离更快地趋于零）。两个偏导都存在*并不*够；但若偏导在该点附近*连续*，则可微性得到保证——这是你几乎总会用到的实用判据。

<a id="s9"></a>
### 高阶偏导与 Clairaut 定理

*求两次导，次序可能要紧——但引人注目的是，通常并不要紧。只要混合偏导连续，它们就相等。*

**本节讲什么、为什么重要。** 你可以再对一个偏导求导，产生**二阶偏导**。令人惊讶且极其有用的事实（**Clairaut 定理**）是：两个**混合**偏导——先对 $x$ 后对 $y$，对比先 $y$ 后 $x$——只要连续就相等。这一个对称性是恰当微分、保守场（§s20）以及旋度消失恒等式（§s22）背后隐藏的原因。

**二阶偏导与 Clairaut 定理**

$$f_{xx}=\partial_x\partial_x f,\quad f_{xy}=\partial_y\partial_x f,\quad f_{yx}=\partial_x\partial_y f$$

$$\text{If }f_{xy},f_{yx}\text{ are continuous near }(a,b),\ \text{then } f_{xy}(a,b)=f_{yx}(a,b).$$

记号说明：$f_{xy}$ 表示“先 $\partial_x$，再 $\partial_y$”，下标从左到右读（算子记号 $\partial_y\partial_x$ 则从右往左作用，因而是同一回事）。下面用到的**中值定理（MVT）**是一元事实：对可微的 $g$，改变量 $g(p)-g(q)$ 等于 $g'(c)(p-q)$，其中 $c$ 是 $q$ 与 $p$ 之间严格内部的某点——平均变化率在内部某处被作为瞬时变化率取到。

**演示 — 为何 $f_{xy}=f_{yx}$**

1. 作出同时微动两个变量、增量为 $h,k$ 的**二阶差分**：

   $$\Delta=\frac{f(a+h,b+k)-f(a+h,b)-f(a,b+k)+f(a,b)}{hk}.$$
2. 把分子先按 $x$ 上的差分分组。定义 $g(x)=f(x,b+k)-f(x,b)$；则分子是 $g(a+h)-g(a)$。由 MVT，存在 $a$ 与 $a+h$ 之间的 $\xi$ 使 $g(a+h)-g(a)=h\,g'(\xi)=h\big(f_x(\xi,b+k)-f_x(\xi,b)\big)$。
3. 再次用 MVT，这次在 $y$ 上，作用于函数 $y\mapsto f_x(\xi,y)$ 在 $b$ 与 $b+k$ 之间：存在 $\eta$ 使 $f_x(\xi,b+k)-f_x(\xi,b)=k\,f_{xy}(\xi,\eta)$。代入第 2 步并除以 $hk$ 得 $\Delta=f_{xy}(\xi,\eta)$。
4. 由对称性——把分子先按 $y$ 上的差分分组并重复——我们也得到 $\Delta=f_{yx}(\xi',\eta')$，其中 $(\xi',\eta')$ 在 $(a,b)$ 附近。
5. 令 $h,k\to0$。则 $(\xi,\eta)\to(a,b)$ 且 $(\xi',\eta')\to(a,b)$（它们被夹在各角之间）。利用 $f_{xy}$ 与 $f_{yx}$ *连续*（所以它们在移动点处的值趋于它们在 $(a,b)$ 处的值）：

   $$f_{xy}(a,b)=\lim_{h,k\to0}\Delta=f_{yx}(a,b).\qquad\blacksquare$$

**习题示例。** 设 $f(x,y)=x^3y^2+\sin x$。则 $f_x=3x^2y^2+\cos x$，所以 $f_{xy}=\partial_y(3x^2y^2+\cos x)=6x^2y$。换一条路，$f_y=2x^3y$，所以 $f_{yx}=\partial_x(2x^3y)=6x^2y$。它们相符，正如 Clairaut 所保证。

*混合偏导相等正是恰当微分与保守场背后的条件（第 20 节）。*

<a id="s10"></a>
### 局部极值与二阶导数判别法

*山丘与山谷出现在曲面平坦之处——即梯度消失之处。一个二阶导数判别法把山峰与山口区分开来。*

**本节讲什么、为什么重要。** 要找一张曲面的最高或最低点，先定位平坦之处（梯度为零——$f'=0$ 的多元类比）。但平坦之处可能是山峰、山谷，或一个**鞍点**（一个方向上是上、另一个方向上是下）。**二阶导数判别法**用一个由二阶偏导搭成的数 $D$ 来分类它们。

**临界点与二阶导数判别法**

$$\nabla f=\mathbf 0\ \Rightarrow\ \text{critical point};\qquad D=f_{xx}f_{yy}-f_{xy}^{\,2}$$

*$D>0,\ f_{xx}>0\Rightarrow$ 局部极小；$D>0,\ f_{xx}<0\Rightarrow$ 局部极大；$D<0\Rightarrow$ 鞍点；$D=0\Rightarrow$ 无法判定。*

定义：**临界点**是所有一阶偏导都消失的输入，即 $\nabla f=\mathbf 0=\langle0,0\rangle$；曲面在那里局部平坦。**局部极小**（相应地**极大**）是比所有邻近点都低（高）的点。**鞍点**是一个既非极小也非极大的临界点——它沿一个方向是极小、沿另一个方向是极大，像一座山口。判别式 $D$ 是上面定义的那个数；规则按 $D$ 与 $f_{xx}$ 的符号对临界点分类。

> **概念 — 为何 $D$ 是一个行列式**
>
> $D$ 是 **Hessian 矩阵** $\begin{pmatrix}f_{xx}&f_{xy}\\ f_{xy}&f_{yy}\end{pmatrix}$ 的行列式。在临界点附近 $f$ 看起来像一个二次型；Hessian 的特征值给出沿主轴的曲率。两者皆正 → 碗形（极小）；两者皆负 → 穹形（极大）；异号 → 鞍点。$D$（特征值之积）的符号与 $f_{xx}$ 的符号恰好恢复出这些情形。

**Hessian** 是二阶偏导构成的矩阵；**行列式**是 §s1 中那个面积配方（对 $2\times2$ 矩阵为 $ad-bc$）；**特征值**是沿曲面自然轴向的曲率（这里你只需用规则，无需计算它们）。它们的乘积等于行列式 $D$：两个同号曲率给出 $D>0$（碗或穹），异号给出 $D<0$（鞍）。

**习题示例。** 对 $f(x,y)=x^3-3x+y^2$ 的临界点分类。

1. 偏导：$f_x=3x^2-3$，$f_y=2y$。令两者为零：$3x^2-3=0\Rightarrow x=\pm1$；$2y=0\Rightarrow y=0$。临界点：$(1,0)$ 与 $(-1,0)$。
2. 二阶偏导：$f_{xx}=6x$，$f_{yy}=2$，$f_{xy}=0$。所以 $D=f_{xx}f_{yy}-f_{xy}^2=(6x)(2)-0=12x$。
3. 在 $(1,0)$：$D=12>0$ 且 $f_{xx}=6>0$ → **局部极小**。在 $(-1,0)$：$D=-12<0$ → **鞍点**。

> **联系 — 微积分 I 的升级**
>
> 在一元情形中：$f'=0$ 然后检查 $f''$。这里 $\nabla f=\mathbf 0$ 取代 $f'=0$，Hessian 行列式取代单个的 $f''$。逻辑——找平坦之处，再探测曲率——完全相同。

<a id="s11"></a>
### Lagrange 乘子（约束优化）

*要在约束 $g=c$ 下优化 $f$，不能简单地令 $\nabla f=\mathbf 0$。约束把你钉在一条曲线或一张曲面上——而答案出现在梯度对齐之处。*

**本节讲什么、为什么重要。** 你常常想要 $f$ 的最大或最小值，但你不能自由漫游——你必须待在一个约束上，比如固定预算或一条曲线。令 $\nabla f=\mathbf0$ 是错的，因为无约束的山峰可能在禁区之外。**Lagrange 乘子**法说：约束最优点出现在 $f$ 的梯度与约束的梯度平行之处。

**Lagrange 条件**

$$\nabla f=\lambda\,\nabla g,\qquad g(x,y,\dots)=c$$

*对变量与乘子 $\lambda$ 解这个方程组。有两个约束时：$\nabla f=\lambda\nabla g+\mu\nabla h$。*

定义：**约束**是一个方程 $g(x,y,\dots)=c$，把输入限制在 $g$ 的一个等值集上（§s3）。数 $\lambda$（lambda）是 **Lagrange 乘子**，一个未知标量。该条件说 $\nabla f$ 是 $\nabla g$ 的一个数乘，即两支箭头平行。

**演示 — 为何梯度必须平行**

1. 约束 $g=c$ 把你限制在它的等值集上（二维中是一条曲线，三维中是一张曲面）。取任意一条完全落在该集合内、并在时刻 $t_0$ 经过一个约束极值的光滑路径 $\mathbf r(t)$。
2. 沿该路径，值 $f(\mathbf r(t))$ 构成一个普通的一元函数，在 $t_0$ 处有极值；因此它的导数在那里消失。由链式法则（§s6，作为梯度点乘速度）：

   $$\frac{d}{dt}f(\mathbf r(t))\Big|_{t_0}=\nabla f\cdot\mathbf r'(t_0)=0.$$
3. 所以 $\nabla f\perp\mathbf r'(t_0)$。这对约束集中通过该点的*每一条*路径都成立，而这些速度 $\mathbf r'(t_0)$ 扫过该集合的所有切方向。因此 $\nabla f$ 垂直于整个约束集。但 $\nabla g$ 也垂直于该集合，因为它是 $g$ 的一个等值集而梯度垂直于其等值集（§s7）。
4. 两个都垂直于同一条曲线/曲面的向量沿同一条直线，因而平行；平行意味着一个是另一个的数乘：

   $$\nabla f=\lambda\,\nabla g.\qquad\blacksquare$$

**习题示例。** 在约束 $g(x,y)=x^2+y^2=8$ 下最大化 $f(x,y)=xy$。

1. $\nabla f=\langle y,x\rangle$，$\nabla g=\langle2x,2y\rangle$。条件 $\nabla f=\lambda\nabla g$ 给出 $y=2\lambda x$ 与 $x=2\lambda y$。
2. 把第一个代入第二个：$x=2\lambda(2\lambda x)=4\lambda^2 x$。若 $x\neq0$，则 $4\lambda^2=1$，所以 $\lambda=\pm\tfrac12$。于是 $y=2\lambda x=\pm x$。
3. 在 $y=\pm x$ 下使用约束 $x^2+y^2=8$：$2x^2=8\Rightarrow x^2=4\Rightarrow x=\pm2$，$y=\pm2$。候选点是 $(\pm2,\pm2)$。
4. 计算 $f=xy$：在 $(2,2)$ 与 $(-2,-2)$ 处为 $+4$，在 $(2,-2)$ 与 $(-2,2)$ 处为 $-4$。所以 $xy$ 在该圆上的最大值是 $\boxed{4}$（而最小值是 $-4$）。

*在约束最优点处，$f$ 的等值线与约束相切——它们相吻，共用一个法向量。乘子 $\lambda$ 度量最优值对约束水平 $c$ 的敏感性。*

## C 部分 · 多重积分

<a id="s12"></a>
### 矩形与一般区域上的二重积分

*二重积分把一个函数在二维区域上累加起来——即曲面下的体积。Fubini 定理让你一次处理一个变量来计算它。*

**本节讲什么、为什么重要。** 单重积分 $\int_a^b f\,dx$ 把 $f$ 在一个区间上累积（曲线下的面积）。**二重积分** $\iint_R f\,dA$ 把 $f$ 在一片平坦区域上累积（曲面下的体积）。实用的引擎是 **Fubini 定理**：你把二重积分算成两个嵌套的普通积分——一次处理一个变量。

**定义与 Fubini 定理**

$$\iint_R f\,dA=\lim_{\|P\|\to0}\sum_{i,j} f(x_i^*,y_j^*)\,\Delta A=\int_a^b\!\!\int_c^d f(x,y)\,dy\,dx$$

*在矩形上，当 $f$ 在其上连续（更一般地可积）时，积分次序可以随意。二重积分是小盒子 $f\cdot\Delta A$ 的 Riemann 和的极限。*

定义：$R$ 是积分区域；$dA$ 是**面积元**（一小块面积）。一个**分割** $P$ 把 $R$ 切成面积为 $\Delta A$ 的小矩形；$(x_i^*,y_j^*)$ 是第 $(i,j)$ 个矩形中的取样点；$\|P\|$ 是最大那块的尺寸。中间那个表达式是一个 **Riemann 和**——把高乘面积 $f\cdot\Delta A$ 在所有块上加起来——而积分是它在块收缩时的极限。**Fubini 定理**说这个二维极限等于右边的累次单重积分：先对 $y$ 积分（内层），再对 $x$ 积分（外层）。

**一般（I 型 / II 型）区域**

$$\iint_D f\,dA=\int_a^b\!\!\int_{g_1(x)}^{g_2(x)} f\,dy\,dx=\int_c^d\!\!\int_{h_1(y)}^{h_2(y)} f\,dx\,dy$$

*内层上下限描述区域（是函数）；外层上下限是常数。先画出区域——它决定积分限，也常常决定哪个次序好处理。*

**I 型区域**夹在两条曲线 $y=g_1(x)$（下）与 $y=g_2(x)$（上）之间，跨一个 $x$ 区间 $[a,b]$；**II 型区域**夹在 $x=h_1(y)$ 与 $x=h_2(y)$ 之间，跨一个 $y$ 区间 $[c,d]$。内层积分的上下限是函数（它们描述移动的边界）；外层上下限是常数。

**习题示例。** 计算 $\iint_D x\,dA$，其中 $D$ 是顶点为 $(0,0),(1,0),(1,1)$ 的三角形。

1. 把 $D$ 描述为 I 型：$x$ 从 $0$ 跑到 $1$；对固定的 $x$，$y$ 从下边 $y=0$ 跑到直线 $y=x$。所以 $\iint_D x\,dA=\int_0^1\!\int_0^{x} x\,dy\,dx$。
2. 内层积分（把 $x$ 当常数）：$\int_0^x x\,dy=x\,[y]_0^x=x\cdot x=x^2$。
3. 外层积分：$\int_0^1 x^2\,dx=\big[\tfrac{x^3}{3}\big]_0^1=\tfrac13$。

所以 $\iint_D x\,dA=\tfrac13$。

> **原理 — 交换积分次序**
>
> 一个累次积分在某一次序下无法计算，在另一次序下却可能是初等的。技巧：从积分限重构出*区域*，再用交换了的变量重新描述它。区域是不变量；积分限只是切割它的一种方式。

**习题示例（次序交换）。** 考虑 $\int_0^1\!\int_x^1 e^{y^2}\,dy\,dx$。内层 $\int e^{y^2}dy$ 没有初等原函数——卡住了。重构区域：$0\le x\le1$ 且 $x\le y\le1$，即三角形 $0\le x\le y\le1$。改以 $y$ 为外层重新切割：$0\le y\le1$ 且 $0\le x\le y$：

$$\int_0^1\!\int_0^{y} e^{y^2}\,dx\,dy=\int_0^1 e^{y^2}\,[x]_0^{y}\,dy=\int_0^1 y\,e^{y^2}\,dy.$$

现在代换 $u=y^2$，$du=2y\,dy$：$=\tfrac12\int_0^1 e^u\,du=\tfrac12(e-1)$。这次交换把一个无法计算的积分变成了一个初等的。

> **联系 — 把单重积分迭代起来**
>
> 二重积分不过是一个被积函数本身是定积分的定积分。你所知道的关于 $\int$ 的一切都搬得过来；唯一的新技能是把一个二维区域翻译成嵌套的积分限。

<a id="s13"></a>
### 极坐标中的二重积分

*圆与圆盘在 $x,y$ 中是噩梦，但在 $r,\theta$ 中却平凡。唯一的关窍——也是问题的核心——是面积元多出一个因子 $r$。*

**本节讲什么、为什么重要。** **极坐标**用点到原点的距离 $r$ 和它与正 $x$ 轴所成的角 $\theta$ 来描述一个点。圆形区域在 $r,\theta$ 中变成简单的矩形。关键的微妙之处在于面积元是 $r\,dr\,d\theta$，*而不是* $dr\,d\theta$——这个多出来的 $r$ 是本学科中最常被遗忘的因子，所以我们要把它推导出来。

**极坐标二重积分**

$$x=r\cos\theta,\quad y=r\sin\theta,\qquad \iint_D f\,dA=\iint_D f(r\cos\theta,r\sin\theta)\,\underbrace{r\,dr\,d\theta}_{dA}$$

*这个 $r$ 不是可选的——忘掉它是经典的错误。它是极坐标映射的 Jacobian（第 16 节）。*

定义：$r\ge0$ 是到原点的距离，$\theta$ 是与 $+x$ 轴所成的角。转换 $x=r\cos\theta,\,y=r\sin\theta$ 来自直角三角形三角学。要积分时，把这些代入 $f$，并把 $dA$ 换成 $r\,dr\,d\theta$。

**演示 — 为何 $dA=r\,dr\,d\theta$**

1. 用射线 $\theta=\text{常数}$ 和圆 $r=\text{常数}$ 来分割区域。一个典型的“极坐标矩形”张开一个小角 $\Delta\theta$、有一个小的径向厚度 $\Delta r$，位于半径 $r$ 处。
2. 它的两条弯曲边是圆弧。弧长等于半径乘以角，所以外弧长为 $r\,\Delta\theta$；径向边（一段直的）长为 $\Delta r$。对于小增量，这块斑近似是以这两个边长为边的矩形：

   $$\Delta A\approx(\text{arc length})\times(\text{radial width})=(r\,\Delta\theta)(\Delta r).$$
3. 精确地说：这块斑是半径介于 $r$ 与 $r+\Delta r$ 之间、张角为 $\Delta\theta$ 的区域。半径为 $\rho$、角为 $\Delta\theta$ 的圆扇形面积是 $\tfrac12\rho^2\Delta\theta$，所以这片圆环切片的面积为

   $$\Delta A=\tfrac12\big((r+\Delta r)^2-r^2\big)\Delta\theta=\tfrac12\big(2r\,\Delta r+(\Delta r)^2\big)\Delta\theta=\big(r+\tfrac12\Delta r\big)\Delta r\,\Delta\theta.$$
4. 令 $\Delta r,\Delta\theta\to0$；那项 $\tfrac12\Delta r$ 消失，留下面积元 $dA=r\,dr\,d\theta$。$\blacksquare$

*对于同样的 $\Delta\theta$，离原点越远的斑越宽；因子 $r$ 说明了这种向外扇开的效应。*

**习题示例。** 在圆盘 $D:\,x^2+y^2\le4$ 上计算 $\iint_D (x^2+y^2)\,dA$。在极坐标下，$x^2+y^2=r^2$，圆盘是 $0\le r\le2$，$0\le\theta\le2\pi$，且 $dA=r\,dr\,d\theta$：

$$\int_0^{2\pi}\!\int_0^2 r^2\cdot r\,dr\,d\theta=\int_0^{2\pi}\!\int_0^2 r^3\,dr\,d\theta=\int_0^{2\pi}\Big[\tfrac{r^4}{4}\Big]_0^2 d\theta=\int_0^{2\pi}4\,d\theta=8\pi.$$

忘掉那个多出的 $r$ 会得到内层 $\int_0^2 r^2\,dr=\tfrac83$ 以及一个错误的最终答案——正是那个方框所警示的陷阱。

> **联系 — 高斯积分**
>
> 极坐标攻克 $\int_{-\infty}^{\infty}e^{-x^2}dx=\sqrt\pi$：把它平方成在平面上的二重积分，转到极坐标，于是顽固的 $e^{-r^2}\,r\,dr$ 由初等代换便可积出——来自 $dA$ 的那个 $r$ 正是让它成功的关键。

<a id="s14"></a>
### 三重积分

*再加一维：在一个实体上积分。图景与记账法都直接从二重积分延伸过来。*

**本节讲什么、为什么重要。** **三重积分** $\iiint_E f\,dV$ 把 $f$ 在一个三维实体 $E$ 上累积。当 $f=1$ 时它计算该实体的体积；当 $f$ 是密度时它计算质量。相比二重积分，唯一真正新的技能是用三层嵌套的积分限来描述一个实体。

**三重积分与体积**

$$\iiint_E f\,dV=\int\!\!\int\!\!\int f(x,y,z)\,dz\,dy\,dx,\qquad \text{Vol}(E)=\iiint_E 1\,dV$$

*最内层的积分限可依赖于两个外层变量；中间层依赖于最外层；最外层是常数。*

这里 $dV$ 是**体积元**（一个小体积盒子），$E$ 是实体。与 §s12 中的 Fubini 一样，三重积分被算成三层嵌套的普通积分。

> **原理 — 用投影与切片来设定**
>
> 把实体描述为：在某个坐标平面上的一片二维**影子** $D$，其中 $z$ 在下曲面 $z=u_1(x,y)$ 与上曲面 $z=u_2(x,y)$ 之间跑动。先对 $z$ 积分（对每个 $(x,y)$ 是一个单重积分），然后把 $D$ 当作一个二重积分处理——可能在极坐标下。

**习题示例（体积）。** 求实体 $E$ 的体积，它位于平面 $z=x+y$ 之下、$z=0$ 之上，覆盖单位正方形 $0\le x\le1,\,0\le y\le1$。

1. 对正方形中每个 $(x,y)$，$z$ 从 $0$ 跑到 $x+y$。所以 $\text{Vol}=\int_0^1\!\int_0^1\!\int_0^{x+y}1\,dz\,dy\,dx$。
2. 最内层：$\int_0^{x+y}dz=x+y$。
3. 中间层（对 $y$）：$\int_0^1 (x+y)\,dy=\big[xy+\tfrac{y^2}{2}\big]_0^1=x+\tfrac12$。
4. 外层（对 $x$）：$\int_0^1\big(x+\tfrac12\big)dx=\big[\tfrac{x^2}{2}+\tfrac{x}{2}\big]_0^1=\tfrac12+\tfrac12=1$。

体积是 $1$。

> **联系 — 同样的技能，更多的限**
>
> 三重积分是单重积分的二重积分。掌握它完全在于把一个三维实体翻译成嵌套的积分限——其中的微积分是你早已会做的初等积分。

<a id="s15"></a>
### 柱坐标与球坐标

*具有轴对称或中心对称的实体呼唤着尊重那种对称的坐标。每种坐标都带来自己的体积元。*

**本节讲什么、为什么重要。** 正如极坐标简化平面中的圆形区域，**柱坐标**与**球坐标**简化空间中的实体。柱坐标 = 底面的极坐标加上普通的高度；球坐标 = 到原点的距离加上两个角。每种都带着自己的体积元，我们将把它推导出来。

**柱坐标**

$$x=r\cos\theta,\ y=r\sin\theta,\ z=z,\qquad dV=r\,dz\,dr\,d\theta$$

*$xy$ 平面上是极坐标，上面是普通的 $z$。适合柱体、圆锥、抛物面。*

它们对底面复用极坐标 $(r,\theta)$，并保留 $z$ 作高度。体积元从 §s13 继承极坐标的 $r$（$z$ 方向贡献一个朴素的 $dz$）：$dV=(r\,dr\,d\theta)\,dz$。

**球坐标**

$$x=\rho\sin\phi\cos\theta,\ y=\rho\sin\phi\sin\theta,\ z=\rho\cos\phi,\qquad dV=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$$

*$\rho\ge0$ 是到原点的距离，$\phi\in[0,\pi]$ 是与 $+z$ 轴所成的角，$\theta\in[0,2\pi)$ 是经度。适合球与圆锥。*

定义：$\rho$（rho）是到原点的直线距离；$\phi$（phi）是从北极（$+z$ 轴）向下量起的**极角**；$\theta$ 是 $xy$ 平面中的**方位角**（经度）。

**演示 — 球坐标体积元 $\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$**

1. 固定角度、把 $\rho$ 增加 $d\rho$：点笔直向外移动，描出一条长为 $d\rho$ 的径向边。
2. 固定 $\rho,\theta$、把 $\phi$ 增加 $d\phi$：点沿一个半径为 $\rho$ 的圆（一条过两极的子午线）移动，所以描出一段长为（半径 × 角）$=\rho\,d\phi$ 的弧。
3. 固定 $\rho,\phi$、把 $\theta$ 增加 $d\theta$：点沿一个纬度圆移动。它的半径是到 $z$ 轴的距离，即 $\rho\sin\phi$（以 $\rho$ 为斜边、与竖直方向成角 $\phi$ 的直角三角形的水平直角边）。所以这段弧长为 $\rho\sin\phi\,d\theta$。
4. 这三条边相互垂直（径向、沿子午线、沿纬度），所以这个小盒子的体积是三个长度之积：

   $$dV=(d\rho)(\rho\,d\phi)(\rho\sin\phi\,d\theta)=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta.\qquad\blacksquare$$

*$\rho^2$ 是球面面积的增长；$\sin\phi$ 是纬度圆向两极收缩。两者都直接出自 Jacobian（第 16 节）。*

**习题示例（球的体积）。** 半径为 $a$ 的球是 $0\le\rho\le a$，$0\le\phi\le\pi$，$0\le\theta\le2\pi$：

$$\text{Vol}=\int_0^{2\pi}\!\int_0^{\pi}\!\int_0^{a}\rho^2\sin\phi\,d\rho\,d\phi\,d\theta=\Big(\int_0^a\rho^2d\rho\Big)\Big(\int_0^\pi\sin\phi\,d\phi\Big)\Big(\int_0^{2\pi}d\theta\Big).$$

各因子：$\int_0^a\rho^2d\rho=\tfrac{a^3}{3}$；$\int_0^\pi\sin\phi\,d\phi=[-\cos\phi]_0^\pi=2$；$\int_0^{2\pi}d\theta=2\pi$。相乘：$\tfrac{a^3}{3}\cdot2\cdot2\pi=\tfrac{4}{3}\pi a^3$——熟悉的球体积，验证了 $\rho^2\sin\phi$ 这个体积元。

<a id="s16"></a>
### 换元法与 Jacobian

*极坐标、柱坐标与球坐标都是一个原理的特例：用一个光滑映射换坐标，体积元就按其导数的行列式缩放。*

**本节讲什么、为什么重要。** 所有那些特殊的面积/体积元（$r$、$r$、$\rho^2\sin\phi$）都是同一条主法则的实例。当你通过某个映射用新变量 $(u,v)$ 代替 $(x,y)$ 时，面积被一个局部因子拉伸——即 **Jacobian 行列式**的绝对值。这是多元换元法，推广了微积分 I 中的 $u$ 代换。

**换元法与 Jacobian**

$$\iint_R f\,dx\,dy=\iint_S f\big(x(u,v),y(u,v)\big)\,\Big|\frac{\partial(x,y)}{\partial(u,v)}\Big|\,du\,dv$$

$$\frac{\partial(x,y)}{\partial(u,v)}=\det\!\begin{pmatrix} x_u & x_v\\ y_u & y_v\end{pmatrix}$$

*Jacobian 行列式是变换的局部面积拉伸因子。在 $n$ 维中它是一个 $n\times n$ 行列式。*

定义：一个**换元**（或**坐标映射**）把旧坐标表示为新坐标的函数，$x=x(u,v)$，$y=y(u,v)$。$R$ 是 $xy$ 中的区域；$S$ 是 $uv$ 中对应的区域。**Jacobian 矩阵** $\begin{pmatrix}x_u&x_v\\y_u&y_v\end{pmatrix}$ 收集该映射的偏导；它的**行列式** $\frac{\partial(x,y)}{\partial(u,v)}=x_uy_v-x_vy_u$ 度量该映射如何缩放微小面积。我们取它的绝对值，因为面积为正。

**演示 — 极坐标 Jacobian 恢复出 $r$**

1. 用 $x=r\cos\theta,\ y=r\sin\theta$（所以 $(u,v)=(r,\theta)$），计算四个偏导。对 $x$ 求导：$x_r=\cos\theta$，$x_\theta=-r\sin\theta$。对 $y$ 求导：$y_r=\sin\theta$，$y_\theta=r\cos\theta$。
2. 作出 Jacobian 行列式 $x_r y_\theta-x_\theta y_r$：

   $$\frac{\partial(x,y)}{\partial(r,\theta)}=\det\!\begin{pmatrix}\cos\theta & -r\sin\theta\\ \sin\theta & r\cos\theta\end{pmatrix}=(\cos\theta)(r\cos\theta)-(-r\sin\theta)(\sin\theta)=r\cos^2\theta+r\sin^2\theta.$$
3. 用恒等式 $\cos^2\theta+\sin^2\theta=1$：行列式是 $r$。由于 $r\ge0$，它的绝对值是 $r$，所以 $dx\,dy=r\,dr\,d\theta$——恰好是 §s13 的极坐标元。$\blacksquare$

*本部分中每一个特殊体积元都是一个行列式。同样的计算在球坐标中给出 $\rho^2\sin\phi$。*

**习题示例（线性换元）。** 计算 $\iint_R (x+y)\,dx\,dy$，其中 $R$ 是单位正方形 $S:\,0\le u\le1,\,0\le v\le1$ 在映射 $x=u+v$，$y=u-v$ 下的像所成的平行四边形（其顶点为 $(0,0),(1,1),(2,0),(1,-1)$）。Jacobian：$x_u=1,x_v=1,y_u=1,y_v=-1$，所以 $\frac{\partial(x,y)}{\partial(u,v)}=(1)(-1)-(1)(1)=-2$，绝对值为 $2$。又 $x+y=(u+v)+(u-v)=2u$。于是积分变为

$$\iint_S 2u\cdot2\,du\,dv=\int_0^1\!\int_0^1 4u\,du\,dv=\Big(\int_0^1 4u\,du\Big)\Big(\int_0^1 dv\Big)=\big[2u^2\big]_0^1\cdot 1=2.$$

新变量把一个倾斜的平行四边形变成了一个容易的矩形，得到 $\iint_R(x+y)\,dx\,dy=2$。

> **概念 — 为何是行列式？**
>
> 坐标映射的导数是一个矩阵（Jacobian 矩阵）；它把一个微小坐标盒子送成一个微小平行六面体。**行列式**恰好是线性映射缩放体积的那个因子（第 1 节的三重积）。所以 Jacobian 行列式的绝对值就是局部的体积换算率。

<a id="s17"></a>
### 应用：质量、矩与质心

*多重积分从密度计算物理总量。模式始终是：把密度积分得到总体，把密度乘位置积分以找到它的平衡之处。*

**本节讲什么、为什么重要。** 给定物质如何分布（它的**密度**），积分可恢复物理总量：总质量、平衡点（**质心**），以及对旋转的阻抗（**转动惯量**）。这个反复出现的模板——总量 $=\int(\text{密度})$，平均位置 $=\frac{\int(\text{位置})(\text{密度})}{\int(\text{密度})}$——也是概率与统计的基础。

**质量、矩、形心**

$$m=\iint_D \rho\,dA,\qquad M_y=\iint_D x\,\rho\,dA,\quad M_x=\iint_D y\,\rho\,dA$$

$$\bar x=\frac{M_y}{m},\qquad \bar y=\frac{M_x}{m}$$

*三维版本在一个实体上用 $dV$ 积分。当密度为常数时，质心就是纯几何的**形心**。*

定义：$\rho(x,y)$（rho）是**密度**——每点处单位面积的质量。**质量** $m$ 把密度在区域上加起来。**矩** $M_y=\iint x\rho\,dA$ 用每一小份质量到 $y$ 轴的 $x$ 距离对其加权（对称地，$M_x$ 用 $y$）；下标命名所取之矩绕的那条轴。**质心** $(\bar x,\bar y)$ 是平衡点；用矩除以质量便得到以质量为权的平均位置。**形心**是密度为常数时的质心——一个纯几何的中心。

**转动惯量**

$$I_x=\iint_D y^2\rho\,dA,\quad I_y=\iint_D x^2\rho\,dA,\quad I_0=\iint_D (x^2+y^2)\rho\,dA$$

*惯量用到轴的距离的平方对质量加权——这就是为何远离轴的质量如此强烈地抗拒转动。*

**转动惯量** $I$ 绕某轴用每一小份质量到该轴距离的*平方*对其加权；$I_0$（绕原点/$z$ 轴）用 $x^2+y^2$，即到原点距离的平方。

**习题示例。** 一块薄板覆盖正方形 $0\le x\le1,\,0\le y\le1$，密度为 $\rho(x,y)=x$（越靠右越重）。

- 质量：$m=\int_0^1\!\int_0^1 x\,dy\,dx=\int_0^1 x\,dx=\tfrac12$。
- 绕 $y$ 轴的矩：$M_y=\int_0^1\!\int_0^1 x\cdot x\,dy\,dx=\int_0^1 x^2\,dx=\tfrac13$。
- 所以 $\bar x=\frac{M_y}{m}=\frac{1/3}{1/2}=\tfrac23$。平衡点坐落在中心偏右处（$\tfrac23>\tfrac12$），正如预期，因为质量集中在 $x=1$ 一侧。
- 由于在 $y$ 上的对称性（密度不依赖 $y$）：$M_x=\int_0^1\!\int_0^1 y\cdot x\,dy\,dx=\big(\int_0^1 x\,dx\big)\big(\int_0^1 y\,dy\big)=\tfrac12\cdot\tfrac12=\tfrac14$，所以 $\bar y=\frac{1/4}{1/2}=\tfrac12$（竖直方向居中）。质心：$(\tfrac23,\tfrac12)$。

> **联系 — 反复出现的模板**
>
> 总量 = $\int(\text{密度})$；平均位置 = $\frac{\int(\text{位置})(\text{密度})}{\int(\text{密度})}$。同样的模板给出概率（密度积分为 1，均值 = $\int x f\,dx$）——这是通往统计学姊妹篇的桥梁。

## D 部分 · 向量微积分

<a id="s18"></a>
### 向量场

*向量场给空间中每一点贴上一支箭头——风速、一个力、一个电场。在这些场上做微积分是本课程的高潮。*

**本节讲什么、为什么重要。** 至此为止，函数返回的都是数（标量场）。**向量场**在每一点返回一支箭头——是流与力的自然模型。课程余下部分研究如何沿曲线（功）和穿过曲面（通量）对这类场积分，以及场为某势函数的梯度这一特殊而美妙的情形。

**向量场与梯度场**

$$\mathbf F(x,y,z)=\langle P,\,Q,\,R\rangle,\qquad \mathbf F=\nabla f\ \Rightarrow\ \mathbf F \text{ is a gradient (conservative) field}$$

*这时 $f$ 是 $\mathbf F$ 的一个**势**。引力和静电学都是梯度场。*

定义：**向量场** $\mathbf F$ 给每一点 $(x,y,z)$ 赋予向量 $\langle P,Q,R\rangle$，其中 $P,Q,R$ 是位置的普通标量函数（即分量）。一个场是**梯度场**（也叫**保守场**），如果存在一个标量函数 $f$，称为**势**，使 $\mathbf F=\nabla f$——即 $P=f_x$，$Q=f_y$，$R=f_z$。

**习题示例。** 场 $\mathbf F=\langle 2xy,\,x^2\rangle$ 是保守的，势为 $f(x,y)=x^2y$，因为 $f_x=2xy=P$ 且 $f_y=x^2=Q$。（我们将在 §s20 学习判据以及如何求出 $f$。）

> **概念 — 通过流来读一个场**
>
> 把这个场想象成一种流体的速度。两个问题组织起接下来的一切：沿一条曲线，流*推你*多少（环量、线积分）；穿过一条边界，多少流*通过*（通量、曲面积分）。旋度度量局部旋转；散度度量局部源/汇。

<a id="s19"></a>
### 线积分（标量与向量）；功

*沿一条曲线积分。对标量，你把一个量按弧长加权来累加；对场，你累加它沿路径的分量——即它所做的功。*

**本节讲什么、为什么重要。** **线积分**沿一条曲线累积，而不是在一个区间上。它有两种风味：**标量**线积分按弧长对一个量加权（比方一根金属丝的质量），而**向量**线积分累加场沿路径的分量——物理上是一个力所做的**功**。功与环量是 Green 与 Stokes 定理的左边。

**标量与向量线积分**

$$\int_C f\,ds=\int_a^b f(\mathbf r(t))\,|\mathbf r'(t)|\,dt$$

$$\int_C \mathbf F\cdot d\mathbf r=\int_a^b \mathbf F(\mathbf r(t))\cdot\mathbf r'(t)\,dt=\int_C P\,dx+Q\,dy+R\,dz$$

*$ds=|\mathbf r'|\,dt$ 是弧长；$d\mathbf r=\mathbf r'\,dt$ 是有向步长。向量积分是 $\mathbf F$ 沿 $C$ 所做的功。*

定义：曲线 $C$ 由一个**参数化** $\mathbf r(t)=\langle x(t),y(t),z(t)\rangle$，$a\le t\le b$ 描述——一个移动的点。它的**速度**是 $\mathbf r'(t)=\langle x'(t),y'(t),z'(t)\rangle$，**速率**是 $|\mathbf r'(t)|$。**弧长元** $ds=|\mathbf r'(t)|\,dt$ 是在时间 $dt$ 内扫过的微小长度（距离 = 速率 × 时间）。**有向步长** $d\mathbf r=\mathbf r'(t)\,dt$ 是微小位移向量。标量积分累加按长度加权的 $f$；向量积分累加场与有向步长的点积。

**习题示例（标量）。** 沿线段 $\mathbf r(t)=\langle t,t\rangle$，$0\le t\le1$，密度为 $f(x,y)=x+y$ 的金属丝的质量。这里 $\mathbf r'=\langle1,1\rangle$，$|\mathbf r'|=\sqrt2$，且 $f(\mathbf r(t))=t+t=2t$。所以 $\int_C f\,ds=\int_0^1 2t\cdot\sqrt2\,dt=2\sqrt2\cdot\tfrac12=\sqrt2$。

**习题示例（功）。** $\mathbf F=\langle y,x\rangle$ 沿同一线段 $\mathbf r(t)=\langle t,t\rangle$ 所做的功。则 $\mathbf F(\mathbf r(t))=\langle t,t\rangle$，$\mathbf r'=\langle1,1\rangle$，所以 $\mathbf F\cdot\mathbf r'=t+t=2t$，且 $\int_C\mathbf F\cdot d\mathbf r=\int_0^1 2t\,dt=1$。

> **概念 — 标量 vs. 向量线积分**
>
> **标量**积分 $\int_C f\,ds$ 与方向无关（它按长度加权——想想一根金属丝的质量）。**向量**积分 $\int_C\mathbf F\cdot d\mathbf r$ 在你反转曲线时改变符号，因为它度量的是有向的推力。功与环量都是向量线积分。

> **联系 — 投影到切向**
>
> $\mathbf F\cdot d\mathbf r=(\mathbf F\cdot\mathbf T)\,ds$：功积分是切向分量 $\mathbf F\cdot\mathbf T$ 的标量积分。这个切向视角成为 Green 与 Stokes 定理的左边（环量）。（这里 $\mathbf T=\mathbf r'/|\mathbf r'|$ 是**单位切向量**，即行进方向。）

<a id="s20"></a>
### 线积分基本定理与保守场

*对一个梯度场，线积分只依赖于端点——而非路径。这就是 FTC 本身，被提升到空间中的曲线上。*

**本节讲什么、为什么重要。** 当一个场是梯度 $\nabla f$ 时，它的功积分坍缩为端点处势值之差——中间的路径无关紧要。这是微积分基本定理被原封不动地搬到空间中的曲线上，也是“大定理”里最简单的一个。它还给出判断一个场是否保守的快捷判据。

**线积分基本定理**

$$\int_C \nabla f\cdot d\mathbf r=f(\mathbf r(b))-f(\mathbf r(a))$$

*与路径无关；绕一个闭合回路它是 $0$。这样的 $\mathbf F=\nabla f$ 是**保守的**。*

**闭合回路**是一条回到起点的曲线，$\mathbf r(b)=\mathbf r(a)$；这时右边是 $0$。**与路径无关**意味着积分只依赖端点，而非路线。

**保守场判据（单连通域）**

$$\mathbf F=\langle P,Q\rangle \text{ conservative}\iff \frac{\partial P}{\partial y}=\frac{\partial Q}{\partial x}\quad\big(\text{in 3D: }\nabla\times\mathbf F=\mathbf 0\big)$$

*这个交叉偏导判据是 Clairaut 定理（第 9 节）的化装：若 $\mathbf F=\nabla f$ 则 $P_y=f_{xy}=f_{yx}=Q_x$。*

一个域是**单连通**的，如果它没有洞（任何回路都能在其内部收缩成一点）。在这样的域上，交叉偏导相等既必要又充分。为何必要：若 $\mathbf F=\nabla f$ 则 $P=f_x,Q=f_y$，所以 $P_y=f_{xy}$，$Q_x=f_{yx}$，由 Clairaut（§s9）相等。

**演示 — 证明线积分基本定理**

1. 设 $\mathbf F=\nabla f$ 并把 $C$ 用 $\mathbf r(t),\ a\le t\le b$ 参数化。由向量线积分的定义（§s19）：

   $$\int_C\nabla f\cdot d\mathbf r=\int_a^b\nabla f(\mathbf r(t))\cdot\mathbf r'(t)\,dt.$$
2. 由多元链式法则（§s6，梯度点乘速度的形式），被积函数就是 $f$ 沿路径关于 $t$ 的全导数：

   $$\nabla f(\mathbf r(t))\cdot\mathbf r'(t)=\frac{d}{dt}\,f(\mathbf r(t)).$$
3. 现在它是一个普通的单变量导数积分；应用经典 FTC（§s0）：

   $$\int_a^b\frac{d}{dt}f(\mathbf r(t))\,dt=f(\mathbf r(b))-f(\mathbf r(a)).\qquad\blacksquare$$

**习题示例。** 对 $\mathbf F=\langle 2xy,x^2\rangle=\nabla f$，$f=x^2y$（来自 §s18），沿*任意*一条从 $(0,0)$ 到 $(1,3)$ 的路径所做的功是 $f(1,3)-f(0,0)=1^2\cdot3-0=3$——无需参数化。（判据确认其保守：$P_y=\partial_y(2xy)=2x$ 且 $Q_x=\partial_x(x^2)=2x$，相等。）

*梯度是多元导数；把它积分便在边界点处恢复出函数——这是第 27 节边界原理的首个实例。*

<a id="s21"></a>
### Green 定理

*伟大定理中的第一个：一个场绕闭合平面曲线的环量，等于它的（标量）旋度在所围区域上的积分。*

**本节讲什么、为什么重要。** **Green 定理**是平面中第一个完整的“边界 = 内部”定理。它把一个场绕闭合曲线的**环量**（边界上的线积分）与场的**标量旋度**在内部区域上的二重积分等同起来。它打包了两种物理读法——环量与通量——并且是 Stokes 与 Gauss 的平面原型。

**Green 定理（环量形式）**

$$\oint_C P\,dx+Q\,dy=\iint_D\Big(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\Big)\,dA$$

*$C$ 是区域 $D$ 的正向（逆时针）边界。右边的被积函数是二维标量旋度。*

定义：$\oint_C$ 是绕一条*闭合*曲线 $C$ 的线积分。**正向**（逆时针）意味着当你沿 $C$ 行走时，区域 $D$ 在你左手边。**环量**是绕该回路的功积分。**标量旋度** $Q_x-P_y$ 度量场在某点旋转的倾向。

**两个推论**

$$\text{Area}(D)=\oint_C x\,dy=-\oint_C y\,dx=\tfrac12\oint_C x\,dy-y\,dx$$

$$\text{Flux form: }\ \oint_C \mathbf F\cdot\mathbf n\,ds=\iint_D \Big(\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}\Big)\,dA$$

*环量形式是二维的 Stokes 定理；通量形式是二维的散度定理。一个定理，两种读法。*

面积公式由选取 $P,Q$ 使 $Q_x-P_y=1$ 而来（例如 $P=0,Q=x$ 给出 $\iint 1\,dA=\text{面积}$，等于 $\oint x\,dy$）。这里 $\mathbf n$ 是 $C$ 的**外单位法向量**，通量形式度量穿过 $C$ 的总外流。

**演示 — I 型/II 型区域上的 Green 定理**

1. 在一个 I 型区域 $D=\{a\le x\le b,\ g_1(x)\le y\le g_2(x)\}$（§s12）上证明 $P$ 部分。用 Fubini 把 $-P_y$ 项在 $D$ 上积分，先做 $y$：

   $$\iint_D \!-\frac{\partial P}{\partial y}\,dA=-\int_a^b\!\!\int_{g_1(x)}^{g_2(x)}\frac{\partial P}{\partial y}\,dy\,dx.$$
2. 内层积分是对一个 $y$ 导数的积分，所以由 FTC（§s0）它在 $y$ 限处取值：

   $$-\int_a^b\big[P(x,g_2(x))-P(x,g_1(x))\big]\,dx=\int_a^b P(x,g_1(x))\,dx-\int_a^b P(x,g_2(x))\,dx.$$
3. 现在直接逆时针沿边界行走来计算 $\oint_C P\,dx$。在下边 $y=g_1(x)$（$x$：$a\to b$）上它贡献 $+\int_a^b P(x,g_1)\,dx$；在上边 $y=g_2(x)$（$x$：$b\to a$，反向）上它贡献 $-\int_a^b P(x,g_2)\,dx$；在竖直边上 $x$ 是常数所以 $dx=0$，它们什么也不贡献。这个和等于第 2 步：

   $$\oint_C P\,dx=\iint_D\!-\frac{\partial P}{\partial y}\,dA.$$
4. 对称地，把 $D$ 视为 II 型并先做 $x$，得到 $\oint_C Q\,dy=\iint_D \frac{\partial Q}{\partial x}\,dA$。把两个结果相加便得 Green 定理。$\blacksquare$

*一般区域由这样的小块拼接而成；内部边界成对相消，只留下外曲线。这个相消正是 D 部分中每一个定理背后的引擎。*

**习题示例。** 逆时针绕单位圆 $C$ 计算 $\oint_C(-y\,dx+x\,dy)$。这里 $P=-y$，$Q=x$，所以 $Q_x-P_y=1-(-1)=2$。由 Green 定理，该线积分等于 $\iint_D 2\,dA=2\cdot\text{Area}(D)=2\cdot\pi(1)^2=2\pi$。（用 $\mathbf r(t)=\langle\cos t,\sin t\rangle$ 直接核对也给出 $2\pi$。）

<a id="s22"></a>
### 旋度与散度

*作用在向量场上的两个微分算子。旋度度量微观旋转；散度度量净外流。它们是 Stokes 与 Gauss 的被积函数。*

**本节讲什么、为什么重要。** 两个算子把一个向量场变成新的场，捕捉它的局部行为：**旋度**（一个度量局部旋转的向量）与**散度**（一个度量局部源/汇的标量）。它们恰恰是出现在 Stokes 与 Gauss 定理内部一侧的“导数”对象。两个简洁的恒等式——梯度的旋度为零、旋度的散度为零——组织起整个理论。

**用 $\nabla$ 表示的旋度与散度**

$$\nabla\times\mathbf F=\begin{vmatrix}\mathbf i&\mathbf j&\mathbf k\\ \partial_x&\partial_y&\partial_z\\ P&Q&R\end{vmatrix},\qquad \nabla\cdot\mathbf F=\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}$$

*旋度返回一个向量（旋转轴）；散度返回一个标量（源强度）。*

这里 $\nabla=\langle\partial_x,\partial_y,\partial_z\rangle$ 是 **del 算子**——一个由偏导指令构成的符号向量。**旋度** $\nabla\times\mathbf F$ 像叉积（§s1）那样计算，第二行是这些导数算子；展开后它是 $\langle R_y-Q_z,\;P_z-R_x,\;Q_x-P_y\rangle$。**散度** $\nabla\cdot\mathbf F$ 像点积那样计算，把“对角线”的偏导加起来。

**组织一切的两个恒等式**

$$\nabla\times(\nabla f)=\mathbf 0,\qquad \nabla\cdot(\nabla\times\mathbf F)=0$$

*“梯度的旋度为零”（梯度场无旋）；“旋度的散度为零”（旋度场无源）。两者都是穿了向量外衣的 Clairaut 定理。*

**演示 — 梯度的旋度消失**

1. 取 $\mathbf F=\nabla f=\langle f_x,f_y,f_z\rangle$，所以 $P=f_x,Q=f_y,R=f_z$。$\nabla\times\mathbf F$ 的 $\mathbf k$ 分量是 $Q_x-P_y$（来自上面展开的旋度）：

   $$\partial_x(f_y)-\partial_y(f_x)=f_{yx}-f_{xy}.$$
2. 由 Clairaut 定理（§s9），连续的混合偏导相等，$f_{xy}=f_{yx}$，所以这个分量是 $f_{yx}-f_{xy}=0$。同样的相消，配上其他几对（$f_{zy}=f_{yz}$ 与 $f_{xz}=f_{zx}$），消掉了 $\mathbf i$ 与 $\mathbf j$ 分量。因此 $\nabla\times(\nabla f)=\mathbf 0$。$\blacksquare$

**习题示例（散度与旋度）。** 对 $\mathbf F=\langle xy,\,yz,\,zx\rangle$：散度 $\nabla\cdot\mathbf F=\partial_x(xy)+\partial_y(yz)+\partial_z(zx)=y+z+x$。旋度：$\nabla\times\mathbf F=\langle R_y-Q_z,\,P_z-R_x,\,Q_x-P_y\rangle=\langle 0-y,\,0-z,\,0-x\rangle=\langle -y,-z,-x\rangle$。

> **概念 — 物理含义**
>
> 把一个微小的桨轮丢进流里：它绕轴 $\nabla\times\mathbf F$ 旋转，速率由 $|\nabla\times\mathbf F|$ 决定。围一个微小的球：$\nabla\cdot\mathbf F$ 是每单位体积的净外流——在源处为正，在汇处为负。这些局部读数一经积分就成为全局定理。

*因此保守 $\Rightarrow$ 无旋——这是第 20 节 $P_y=Q_x$ 判据的三维版本。*

<a id="s23"></a>
### 参数曲面与曲面面积

*正如一条曲线对应一个参数，一张曲面对应两个。两个切向量的叉积给出法向量——以及面积元。*

**本节讲什么、为什么重要。** 一条曲线需要一个参数；一张**曲面**需要两个。把曲面写作 $\mathbf r(u,v)$，两个偏速度向量 $\mathbf r_u,\mathbf r_v$ 张成切平面，而它们的叉积同时是曲面的**法向量**（方向）与**面积缩放**（大小）。这单一对象驱动着曲面面积、曲面积分与通量。

**参数化、法向量、曲面面积**

$$\mathbf r(u,v)=\langle x,y,z\rangle,\qquad \mathbf r_u\times\mathbf r_v=\text{normal},\qquad dS=|\mathbf r_u\times\mathbf r_v|\,du\,dv$$

$$A(S)=\iint_D |\mathbf r_u\times\mathbf r_v|\,dA$$

*对图像 $z=g(x,y)$：$dS=\sqrt{1+g_x^2+g_y^2}\,dA$。*

定义：**参数曲面**由带两个参数的 $\mathbf r(u,v)$ 给出；当 $(u,v)$ 取遍区域 $D$ 时，$\mathbf r$ 的尖端描出曲面 $S$。**切向量** $\mathbf r_u=\partial\mathbf r/\partial u$ 与 $\mathbf r_v=\partial\mathbf r/\partial v$ 沿曲面指出；它们的叉积与曲面垂直。$dS$ 是**曲面面积元**。

**演示 — 曲面面积元 $dS=|\mathbf r_u\times\mathbf r_v|\,du\,dv$**

1. 取一个小的参数矩形 $[u,u+du]\times[v,v+dv]$；它映成 $S$ 上的一小块弯曲斑。固定 $v$ 并把 $u$ 增加 $du$ 使你大约移动 $\mathbf r_u\,du$（变化率乘以步长）；类似地另一条边约为 $\mathbf r_v\,dv$。
2. 对于小步长，这块斑近似是这两个边向量张成的平行四边形。由 §s1，两个向量张成的平行四边形面积是它们叉积的大小：

   $$dS=|\,\mathbf r_u\,du\times\mathbf r_v\,dv\,|=|\mathbf r_u\times\mathbf r_v|\,du\,dv,$$

   这里用到把每个因子乘以正数 $du,dv$ 会使叉积的长度缩放 $du\,dv$ 倍。$\blacksquare$

**习题示例（图像公式）。** 对图像 $z=g(x,y)$，参数化 $\mathbf r(x,y)=\langle x,y,g(x,y)\rangle$。则 $\mathbf r_x=\langle1,0,g_x\rangle$，$\mathbf r_y=\langle0,1,g_y\rangle$，叉积为 $\langle -g_x,-g_y,1\rangle$，其长度为 $\sqrt{g_x^2+g_y^2+1}$。因此 $dS=\sqrt{1+g_x^2+g_y^2}\,dA$，与方框中的特例相符。

**习题示例（数值面积）。** 平面片 $z=2x+2y$ 在单位正方形 $0\le x,y\le1$ 上的曲面面积：这里 $g_x=2,g_y=2$，所以 $dS=\sqrt{1+4+4}\,dA=3\,dA$，且 $A=\iint_D 3\,dA=3\cdot1=3$。

*叉积身兼两职：它的方向是曲面法向量（通量所需），它的大小是面积缩放。*

<a id="s24"></a>
### 曲面积分与通量

*在一张曲面上积分。对标量，按面积加权；对场，累加穿过曲面的分量——即通量。*

**本节讲什么、为什么重要。** 与线积分相对应，**曲面积分**也有两种风味。**标量**曲面积分按面积对一个量加权（弯曲薄片的质量）。**通量**积分累加一个向量场*穿过*曲面的分量——每单位时间有多少流体越过。通量是散度定理的边界一侧，也是 Stokes 的内部一侧。

**标量曲面积分与通量**

$$\iint_S f\,dS=\iint_D f(\mathbf r(u,v))\,|\mathbf r_u\times\mathbf r_v|\,dA$$

$$\iint_S \mathbf F\cdot d\mathbf S=\iint_S \mathbf F\cdot\mathbf n\,dS=\iint_D \mathbf F\cdot(\mathbf r_u\times\mathbf r_v)\,dA$$

*$d\mathbf S=\mathbf n\,dS=(\mathbf r_u\times\mathbf r_v)\,dA$。通量度量每单位时间有多少 $\mathbf F$ 穿过 $S$。*

定义：$\mathbf n$ 是曲面的**单位法向量**（所选的“朝外”方向）；$d\mathbf S=\mathbf n\,dS$ 是**向量面积元**，把面积缩放与法向方向结合起来。通量积分把场与这个向量元点乘，只挑出 $\mathbf F$ 中垂直于曲面的那部分（真正越过的那部分）。

**习题示例（通量）。** $\mathbf F=\langle 0,0,z\rangle$ 向上穿过平面 $z=x+y$ 在单位正方形 $0\le x,y\le1$ 上那部分的通量。参数化 $\mathbf r(x,y)=\langle x,y,x+y\rangle$；则 $\mathbf r_x\times\mathbf r_y=\langle -1,-1,1\rangle$（$z$ 分量朝上，正如所愿）。在曲面上 $\mathbf F=\langle0,0,x+y\rangle$，所以 $\mathbf F\cdot(\mathbf r_x\times\mathbf r_y)=x+y$。于是

$$\iint_S\mathbf F\cdot d\mathbf S=\int_0^1\!\int_0^1(x+y)\,dx\,dy=\int_0^1\Big(\tfrac12+y\Big)dy=\tfrac12+\tfrac12=1.$$

> **概念 — 定向要紧**
>
> 通量积分需要选定一侧：一个**定向**，由一个连续的单位法向量 $\mathbf n$ 给出。翻转 $\mathbf n$ 会翻转符号。对闭合曲面，约定取*外*法向量。（Möbius 带是不可定向的——不存在自洽的选择。）

> **联系 — 与线积分的对应**
>
> 标量曲面积分 ↔ 标量线积分（按测度加权）；通量 $\iint\mathbf F\cdot\mathbf n\,dS$ ↔ 环量 $\int\mathbf F\cdot\mathbf T\,ds$。曲线用切向量；曲面用法向量。Stokes（第 25 节）与 Gauss（第 26 节）把它们绑在一起。

<a id="s25"></a>
### Stokes 定理

*Green 定理脱离平面后的样子。绕一张曲面边界曲线的环量，等于旋度穿过该曲面的通量。*

**本节讲什么、为什么重要。** **Stokes 定理**把 Green 定理推广到空间中的弯曲曲面。一个场绕曲面边界曲线的环量，等于场的旋度穿过该曲面的通量。引人注目的是，*任何*具有相同边界的曲面都给出相同答案——边界本身就掌控着环量。

**Stokes 定理**

$$\oint_{\partial S} \mathbf F\cdot d\mathbf r=\iint_S (\nabla\times\mathbf F)\cdot d\mathbf S$$

*$\partial S$ 是 $S$ 的边界曲线，按右手定则相对于 $\mathbf n$ 定向。任何具有相同边界的曲面都给出相同答案。*

定义：$\partial S$（“$S$ 的边界”）是曲面的边缘曲线。**右手定则定向**：若右手大拇指沿 $\mathbf n$ 指出，则卷曲的手指给出绕 $\partial S$ 的正方向。左边是环量；右边是旋度的通量（§s22、§s24）。

> **概念 — 把微观旋转加起来**
>
> 旋度是每单位面积的局部环量。用许多微小回路平铺曲面；在每个回路上，环量 $\approx(\nabla\times\mathbf F)\cdot\mathbf n\,dS$。相邻回路共享沿*相反*方向遍历的边，所以所有内部贡献相消——只有外边界存活下来。那个相消就是 Green 的证明（第 21 节），如今在一张曲面上进行。

**习题示例。** 对 $\mathbf F=\langle -y,x,0\rangle$ 在平面 $z=0$ 中的圆盘 $S:\,x^2+y^2\le1$ 上、取朝上法向量 $\mathbf n=\mathbf k$，验证 Stokes。旋度：$\nabla\times\mathbf F=\langle0,0,\,Q_x-P_y\rangle=\langle0,0,1-(-1)\rangle=\langle0,0,2\rangle$。旋度的通量：$\iint_S\langle0,0,2\rangle\cdot\mathbf k\,dS=\iint_S 2\,dA=2\pi$。绕单位圆的边界环量（来自 §s21 的习题示例，$\oint -y\,dx+x\,dy=2\pi$）也给出 $2\pi$——它们一致。

> **联系 — Green 是平面的 Stokes**
>
> 取 $S$ 为 $xy$ 平面中一片带 $\mathbf n=\mathbf k$ 的区域。则 $(\nabla\times\mathbf F)\cdot\mathbf k=Q_x-P_y$，Stokes 变成 $\oint P\,dx+Q\,dy=\iint(Q_x-P_y)\,dA$——恰好就是 Green 定理。

<a id="s26"></a>
### 散度（Gauss）定理

*一个场穿过闭合曲面向外的通量，等于它的散度在内部实体上的积分。内部的源解释了净外流。*

**本节讲什么、为什么重要。** **散度定理**（Gauss 定理）是三维的高潮：一个场穿过闭合曲面向外的总通量，等于场的散度在所围实体上的积分。用话说，穿过边界的净外流 = 内部的总源强度——流体流动与电磁学的自然守恒律。

**散度定理**

$$\iint_{\partial E} \mathbf F\cdot d\mathbf S=\iiint_E (\nabla\cdot\mathbf F)\,dV$$

*$\partial E$ 是实体 $E$ 的闭合边界曲面，取外法向量。总外流 = 内部总源强度。*

定义：$E$ 是一个实体区域，$\partial E$ 是它的闭合边界曲面（闭合曲面，因为它是实体 $E$ 的边界），按**外**法向量定向。左边是总外流通量；右边把散度（§s22）在内部积分。

> **概念 — 把通量伸缩相消**
>
> 散度是每单位体积的净外流。把 $E$ 切成许多微小盒子；每个贡献 $(\nabla\cdot\mathbf F)\,dV$ 的外流。两个盒子相接处，从一个盒子流出的通量正是流*入*另一个的通量——大小相等、方向相反，故相消。只剩外曲面。与 Green 和 Stokes 相同的相消原理。

**习题示例。** 设 $\mathbf F=\langle x,y,z\rangle$，$E$ 是半径为 $a$ 的球。散度：$\nabla\cdot\mathbf F=1+1+1=3$。所以 $\iiint_E 3\,dV=3\cdot\text{Vol}=3\cdot\tfrac43\pi a^3=4\pi a^3$。直接计算通量：球面上外法向量是 $\mathbf n=\frac{1}{a}\langle x,y,z\rangle$，所以 $\mathbf F\cdot\mathbf n=\frac{1}{a}(x^2+y^2+z^2)=\frac{a^2}{a}=a$（常数），给出通量 $=a\cdot(\text{曲面面积})=a\cdot4\pi a^2=4\pi a^3$。两边一致。

> **联系 — Green 的通量形式是平面的 Gauss**
>
> 在平面中，散度定理读作 $\oint_C\mathbf F\cdot\mathbf n\,ds=\iint_D(P_x+Q_y)\,dA$——恰好就是 Green 定理的通量形式（第 21 节）。Gauss 是它的三维升级。

## E 部分 · 综合

<a id="s27"></a>
### 统一图景：一个定理统辖它们全部

*五个定理——FTC、线积分 FTC、Green、Stokes、Gauss——是从不同维度看到的同一个陈述：一个导数在区域上的积分等于函数在其边界上的积分。*

**本节讲什么、为什么重要。** 你证明过的一切都坍缩成一句话。微积分基本定理、它的线积分版本、Green、Stokes 与 Gauss 全都是不同维度下的*同一个*陈述：把一个导数在区域上积分，你就得到原函数在边界上的求和。认识到这一点是整门课程的回报。

> **原理 — 广义 Stokes 定理**
>
> 用微分形式的语言，这五个全都坍缩成一行：**$d\omega$ 在区域 $M$ 上的积分等于 $\omega$ 在边界 $\partial M$ 上的积分**。这里 $d$ 是外微分（它特殊化为梯度、旋度、散度），$\partial$ 是“取边界”。每个经典定理都是它在某个特定维度与算子下的样子。

定义（从轻而言）：**微分形式** $\omega$ 是你拿来积分的那种对象（一个函数，或一个“$P\,dx+Q\,dy$”表达式，等等）。**外微分** $d$ 是一个单一运算，它在函数上变成梯度、在 1-形式上变成旋度、在 2-形式上变成散度——取决于维度。**边界** $\partial M$ 是区域 $M$ 的边缘（区间的端点、围成曲面的曲线、围成实体的曲面）。

**主陈述**

$$\int_{M} d\omega=\int_{\partial M}\omega$$

*“先求导再在内部积分 = 把原物在边界上积分。”下面每个定理都是它的一个实例。*

| 定理 | 区域 $M$ | 边界 $\partial M$ | 导数 $d$ |
| --- | --- | --- | --- |
| FTC（微积分 I） | 区间 $[a,b]$ | 两个端点 | $f'$ |
| FTC，线积分 | 曲线 $C$ | 两个端点 | 梯度 $\nabla f$ |
| Green | 平面区域 $D$ | 曲线 $\partial D$ | 标量旋度 $Q_x-P_y$ |
| Stokes | 曲面 $S$ | 曲线 $\partial S$ | 旋度 $\nabla\times\mathbf F$ |
| 散度 | 实体 $E$ | 曲面 $\partial E$ | 散度 $\nabla\cdot\mathbf F$ |

**演示 — 从主线读出每个经典定理**

1. **FTC。** 取 $M=[a,b]$，$\omega=f$，$d\omega=f'\,dx$。边界 $\partial M$ 是带符号 $+b,-a$ 的两个端点，所以 $\int_{\partial M}\omega=f(b)-f(a)$。在一个 0 维集合上的“积分”就是取值。主线变成 $\int_a^b f'\,dx=f(b)-f(a)$——§s0。
2. **线积分 FTC。** 取 $M=C$（一条曲线），$\omega=f$，$d\omega=\nabla f\cdot d\mathbf r$；边界是两个端点。主线是 $\int_C\nabla f\cdot d\mathbf r=f(\text{终点})-f(\text{起点})$——§s20。
3. **Green / Stokes。** $M$ 是二维的（一片平面区域或一张曲面）；$d$ 产生（标量或向量）旋度；$\partial M$ 是边界曲线。主线读作 环量 = 旋度通量——§s21、§s25。
4. **散度。** $M$ 是三维实体；$d$ 产生散度；$\partial M$ 是边界曲面。主线读作 外流 = 源总量——§s26。

*这个反复出现的证明动作每次都一样：平铺区域，注意内部边界成对相消，只有 $\partial M$ 存活。* 你在 Green 定理的演示中（§s21）以及 Stokes 与 Gauss 的伸缩相消图景中看到过这个显式的相消。

#### 整个向量微积分浓缩为一行

> 内部的导数 = 边界上的值 · $ \displaystyle\int_M d\omega=\int_{\partial M}\omega $

> **要保持的习惯**
>
> 每当你遇到一个新的积分恒等式，就问本课程的那两个问题：*区域是什么，它的边界是什么？* 在偏导数、多重积分、通量与环量背后，坐着同一个想法——一个导数在内部上的求和就是从边缘读出的函数——一路向上的微积分基本定理。

---

*一门第三学期的多元与向量微积分课程——概念、原理、公式，以及它们背后的演示——作为统计学与微积分指南的姊妹篇而构建。读一遍把握其形貌；遇到任何方框都可回来作参考。记住：这里每一个伟大定理说的都是同一件事——把一个导数在区域上积分，你就在它的边界上重新得到那个函数。*
