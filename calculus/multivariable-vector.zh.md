[English](multivariable-vector.md) · **中文**

# 多元微积分，*环环相扣*

完整的第三学期课程——空间的几何、其上函数的微积分、在区域与曲面上的积分，以及那些伟大的向量微积分定理——由基础到进阶铺陈开来。每一个核心结论都经过**演示**，而把梯度、格林、斯托克斯与高斯串联在一起的那条主线也被明确点出。

[← 返回全部指南](../README.zh.md)

## 第 A 部分 · 空间、向量与函数

<a id="s0"></a>
### 全局图景：从一元到多元

一元微积分研究的是直线上的函数 $y=f(x)$。多元微积分做同样的三件事——极限、导数、积分——但输入与输出如今住在空间里。仅仅“多于一个变量”这一处改变，就重新组织了整门学科。

- **求导** — 导数变成一整个*梯度向量*（后来还是一个矩阵），一次性编码了在*每一个*方向上的变化率。
- **积分** — 积分变成在一片 2D 区域、一个 3D 立体、一条曲线或一张曲面上的求和。
- **连接** — 一族定理（格林、斯托克斯、高斯）把区域*内部*的某个导数与其*边界*上的值联系起来，恰如微积分基本定理在一个区间上所做的那样。

> **原理 — 组织全局的核心思想**
>
> 每个对象都按**有几个数进去**和**有几个数出来**来分类。一个**标量场** $f:\mathbb R^n\to\mathbb R$（温度）有梯度。一个**向量场** $\mathbf F:\mathbb R^n\to\mathbb R^n$（流动、力）有旋度和散度。一个**参数化** $\mathbb R\to\mathbb R^3$ 或 $\mathbb R^2\to\mathbb R^3$ 描出一条曲线或一张曲面。知道了类型，就知道该用哪个算子、哪种积分。

> **联系 — 一个你早已掌握的思想**
>
> 整门学科就是微积分基本定理 $\int_a^b f'\,dx=f(b)-f(a)$ 的推广：一个导数在区域上的积分，等于函数在该区域边界上取值的结果。记住这句话；第 27 节将证明四大定理全都是它的特例。

#### 整门课浓缩成一行

> 向量与空间 → 多元函数 → 偏导数与梯度 → 最优化 → 多重积分 → 向量场 → 格林／斯托克斯／高斯

<a id="s1"></a>
### 向量、点积与叉积

*向量带有大小和方向。两种乘积把向量变成关于角度、投影、面积和体积的语言。*

> **概念 — 点、向量与两种乘积**
>
> 点是一个位置；**向量** $\mathbf v=\langle v_1,v_2,v_3\rangle$ 是一个位移。**点积**返回一个标量，度量对齐程度（从而度量角度与投影）；**叉积**返回一个与两者都垂直的向量，其长度等于它们张成的平行四边形的面积。点积关乎角度；叉积关乎面积与定向。

**大小、点积、角度**

$$|\mathbf v|=\sqrt{v_1^2+v_2^2+v_3^2},\qquad \mathbf a\cdot\mathbf b=\sum_i a_ib_i=|\mathbf a||\mathbf b|\cos\theta$$

*$\mathbf a\cdot\mathbf b=0\iff$ 垂直。$\mathbf a$ 在 $\mathbf b$ 上的标量投影是 $\dfrac{\mathbf a\cdot\mathbf b}{|\mathbf b|}$。*

**叉积（在 $\mathbb R^3$ 中）**

$$\mathbf a\times\mathbf b=\begin{vmatrix}\mathbf i&\mathbf j&\mathbf k\\ a_1&a_2&a_3\\ b_1&b_2&b_3\end{vmatrix},\qquad |\mathbf a\times\mathbf b|=|\mathbf a||\mathbf b|\sin\theta$$

*$\mathbf a\times\mathbf b$ 与两者都垂直，方向由右手定则给出；其长度是平行四边形的面积。$\mathbf a\times\mathbf b=-\,\mathbf b\times\mathbf a$。*

**标量三重积 → 体积**

$$V=\big|\,\mathbf a\cdot(\mathbf b\times\mathbf c)\,\big|=\left|\det\!\begin{pmatrix}a_1&a_2&a_3\\ b_1&b_2&b_3\\ c_1&c_2&c_3\end{pmatrix}\right|$$

*平行六面体的有符号体积。它为零 $\iff$ 三个向量共面。*

**演示 — 点积给出角度**

1. 把 $\mathbf a,\mathbf b$ 尾对尾放置；三角形的第三条边是 $\mathbf a-\mathbf b$。余弦定理说

   $$|\mathbf a-\mathbf b|^2=|\mathbf a|^2+|\mathbf b|^2-2|\mathbf a||\mathbf b|\cos\theta.$$
2. 用点积把左边代数地展开：

   $$|\mathbf a-\mathbf b|^2=(\mathbf a-\mathbf b)\cdot(\mathbf a-\mathbf b)=|\mathbf a|^2-2\,\mathbf a\cdot\mathbf b+|\mathbf b|^2.$$
3. 令两个表达式相等；平方长度项相消，留下

   $$\mathbf a\cdot\mathbf b=|\mathbf a||\mathbf b|\cos\theta.$$

*几何（角度）与代数（分量之和）是同一个运算的两副面孔。*

<a id="s2"></a>
### 直线、平面与二次曲面

*有了向量之后，空间中那些基本对象就有了简洁的方程：一条直线需要一个点和一个方向；一个平面需要一个点和一个法向量。*

**过 $P_0$ 且方向为 $\mathbf v$ 的直线**

$$\mathbf r(t)=\mathbf r_0+t\mathbf v,\qquad \frac{x-x_0}{v_1}=\frac{y-y_0}{v_2}=\frac{z-z_0}{v_3}$$

*向量形式（左）与对称形式（右）。一条直线是一个点加上一个方向的所有标量倍。*

**过 $P_0$ 且法向量为 $\mathbf n$ 的平面**

$$\mathbf n\cdot(\mathbf r-\mathbf r_0)=0\ \Longleftrightarrow\ a(x-x_0)+b(y-y_0)+c(z-z_0)=0$$

*一个点恰好落在平面上，当且仅当它相对 $P_0$ 的位移垂直于 $\mathbf n=\langle a,b,c\rangle$。法向量可直接从系数读出。*

**点到平面的距离**

$$D=\frac{|a x_1+b y_1+c z_1+d|}{\sqrt{a^2+b^2+c^2}}$$

*它是 $\overrightarrow{P_0P_1}$ 在单位法向量上投影的长度——一个点积除以 $|\mathbf n|$。*

> **概念 — 用截痕认识二次曲面**
>
> 那些二次曲面——**椭球面** $\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}=1$、**抛物面** $z=x^2+y^2$、**圆锥面** $z^2=x^2+y^2$、**双曲面**、**鞍面** $z=x^2-y^2$——最好通过它们的*截痕*来理解：用坐标平面去切所得到的曲线。把某个变量取作常数，读出由此得到的圆锥曲线即可。

<a id="s3"></a>
### 多元函数；等值线与等值面

*一个函数 $z=f(x,y)$ 给平面上每一点赋予一个高度——一片地貌。把这片地貌平铺着读出来，最干净的办法是等高线图。*

> **概念 — 图像与等值集之别**
>
> $f(x,y)$ 的**图像**是 $\mathbb R^3$ 中的一张曲面。一条**等值线** $f(x,y)=k$ 收集所有给出相同输出 $k$ 的输入——一条等高线，就像地形图上那样。对于 $f(x,y,z)$，$f=k$ 是一张**等值面**。等高线密集意味着地势陡峭；梯度（第 7 节）将正好垂直地横穿它们。

**定义域、值域、等值集**

$$f:D\subseteq\mathbb R^n\to\mathbb R,\qquad \text{level set}=\{\,\mathbf x: f(\mathbf x)=k\,\}$$

*总是先确定定义域：$\sqrt{}$ 需要非负的自变量，$\ln$ 需要正数，分母必须非零。*

> **联系 — 回到一元**
>
> 一条等值线是“解 $f(x)=k$”在多元情形下的表亲。通过等值集——而非图像——来读一个函数，是让梯度、拉格朗日乘数和隐函数求导显得自然的那种视觉习惯。

<a id="s4"></a>
### 多元的极限与连续性

*极限的定义看上去一模一样，但有一个特征是真正新的：在平面上你可以从无穷多个方向趋近一点，而极限必须沿所有这些方向一致。*

**极限与连续性**

$$\lim_{(x,y)\to(a,b)}f(x,y)=L:\ \forall\varepsilon>0\ \exists\delta>0,\ 0<|(x,y)-(a,b)|<\delta\Rightarrow|f-L|<\varepsilon$$

$$f \text{ continuous at }(a,b)\iff \lim_{(x,y)\to(a,b)}f(x,y)=f(a,b)$$

> **原理 — 双路径检验法**
>
> 如果 $f$ 沿两条不同路径趋近 $(a,b)$ 时趋向*不同*的值，那么极限**不存在**。这是标准工具：试 $y=0$，再试 $x=0$，再试 $y=mx$，再试 $y=x^2$。一次不一致就能下结论。

**演示 — 一个通不过路径检验的极限**

1. 考察 $f(x,y)=\dfrac{xy}{x^2+y^2}$ 当 $(x,y)\to(0,0)$ 时的行为。沿 $x$ 轴（$y=0$）：

   $$f(x,0)=\frac{0}{x^2}=0.$$
2. 沿直线 $y=x$：

   $$f(x,x)=\frac{x\cdot x}{x^2+x^2}=\frac{x^2}{2x^2}=\frac12.$$
3. 两条路径给出 $0$ 和 $\tfrac12$。既然它们不一致，极限便不存在——尽管每一个单变量切片都温顺得很。

*从一个方向趋近永远不够；极限必须从所有方向一致地成立。*

## 第 B 部分 · 多元微分学

<a id="s5"></a>
### 偏导数

*要对一个多元函数求导，把除一个之外的所有变量冻住，再像往常那样求导。每个变量都有自己的斜率。*

**偏导数的定义**

$$f_x(a,b)=\frac{\partial f}{\partial x}=\lim_{h\to0}\frac{f(a+h,b)-f(a,b)}{h}$$

*$f_x$ 是曲面在 $x$ 方向的斜率——把 $y$ 保持为常数的单变量切片 $g(x)=f(x,b)$ 的普通导数。*

> **概念 — “把其余变量保持为常数”**
>
> 计算 $\partial f/\partial x$ 时，其余每个变量都是常数。所以 $\partial_x(x^2y^3)=2xy^3$，而 $\partial_y(x^2y^3)=3x^2y^2$。所有单变量法则（乘积、商、链式）原封不动地适用；改变的只是你对“什么是常数”的看法。

> **联系 — 斜率汇聚成梯度**
>
> 一个 $n$ 元函数有 $n$ 个一阶偏导数。把它们收进一个向量 $\nabla f=\langle f_x,f_y,\dots\rangle$，就成了**梯度**（第 7 节）——这个单一对象扮演着一元情形里导数 $f'(x)$ 所扮演的角色。

<a id="s6"></a>
### 多元链式法则

*当变量依赖于其他变量时，贡献沿每一条路径流动并累加起来。链式法则变成对各条路径的求和。*

**链式法则——两种主要情形**

$$\frac{df}{dt}=\frac{\partial f}{\partial x}\frac{dx}{dt}+\frac{\partial f}{\partial y}\frac{dy}{dt}\qquad\big(x=x(t),\,y=y(t)\big)$$

$$\frac{\partial f}{\partial s}=\frac{\partial f}{\partial x}\frac{\partial x}{\partial s}+\frac{\partial f}{\partial y}\frac{\partial y}{\partial s}\qquad\big(x=x(s,t),\,y=y(s,t)\big)$$

*画一棵树：对从输出到你要求导的那个变量的每一条路径求和，沿每条路径相乘。*

> **联系 — 它是梯度与速度的点积**
>
> 第一种情形恰好是 $\dfrac{df}{dt}=\nabla f\cdot \mathbf r'(t)$，即梯度与路径速度的点积。这一个恒等式将作为方向导数（第 7 节）以及线积分基本定理的被积函数（第 20 节）再次出现。

**演示 — 由链式法则得到隐函数求导**

1. 设 $F(x,y)=0$ 把 $y$ 定义为 $x$ 的函数。对两边关于 $x$ 求导，把 $y=y(x)$ 看待：

   $$\frac{\partial F}{\partial x}\frac{dx}{dx}+\frac{\partial F}{\partial y}\frac{dy}{dx}=0.$$
2. 由于 $dx/dx=1$，解出斜率：

   $$\frac{dy}{dx}=-\frac{F_x}{F_y}\qquad(F_y\neq0).$$

*微积分一里那条神秘的隐函数求导法则，不过是把链式法则应用到一条等值线上。*

<a id="s7"></a>
### 方向导数与梯度

偏导数给出沿坐标轴的斜率。方向导数给出沿*任意*方向的斜率——而梯度把它们全部打包。

**梯度与方向导数**

$$\nabla f=\Big\langle \frac{\partial f}{\partial x},\frac{\partial f}{\partial y},\frac{\partial f}{\partial z}\Big\rangle,\qquad D_{\mathbf u}f=\nabla f\cdot\mathbf u\quad(|\mathbf u|=1)$$

*当你沿单位方向 $\mathbf u$ 迈一步时 $f$ 的变化率，就是梯度在 $\mathbf u$ 上的投影。*

> **概念 — 让梯度不可或缺的三个事实**
>
> (1) $\nabla f$ 指向**最陡上升**的方向；(2) 它的大小 $|\nabla f|$ 就是那个最陡的斜率；(3) $\nabla f$ **垂直于**过该点的等值集。这些合起来把一列偏导数变成一支几何箭头。

**演示 — 梯度是最陡上升的方向**

1. 沿单位方向 $\mathbf u$ 的斜率是 $D_{\mathbf u}f=\nabla f\cdot\mathbf u$。
2. 用 $\nabla f$ 与 $\mathbf u$ 之间的夹角 $\theta$ 写出这个点积：

   $$D_{\mathbf u}f=|\nabla f|\,|\mathbf u|\cos\theta=|\nabla f|\cos\theta.$$
3. 当 $\cos\theta=1$，即 $\theta=0$ 时它取最大值：$\mathbf u$ 与 $\nabla f$ 指向同一方向。最大值是 $|\nabla f|$；最小值 $-|\nabla f|$ 在相反方向（最陡下降）；$\theta=90^\circ$ 给出 $0$。

*因此梯度以最快的速率指向上坡，陡度为 $|\nabla f|$——而零变化率的方向恰好沿着等值集，这证明了 $\nabla f\perp$ 等值集。*

> **联系 — 垂直于等值集**
>
> 沿一条等值线 $f$ 不变，所以对与之相切的 $\mathbf u$ 有 $D_{\mathbf u}f=0$，这迫使 $\nabla f\perp\mathbf u$。这正是为什么 $\nabla F$ 是曲面 $F=k$ 的法向量（第 8 节），也是为什么在约束最优点处梯度会对齐（拉格朗日，第 11 节）。

<a id="s8"></a>
### 切平面、线性近似与微分

*放大一张光滑曲面，它看上去是平的。那个平的近似就是切平面——切线的多元版本。*

**$z=f(x,y)$ 的切平面与线性化**

$$z=f(a,b)+f_x(a,b)(x-a)+f_y(a,b)(y-b)$$

$$L(x,y)=f(a,b)+\nabla f(a,b)\cdot\langle x-a,\,y-b\rangle$$

*与 $y=f(a)+f'(a)(x-a)$ 同样的形态：函数值加斜率乘位移，如今由梯度在两个方向上提供斜率。*

**到等值面 $F(x,y,z)=k$ 的切平面**

$$\nabla F(P)\cdot\langle x-x_0,\,y-y_0,\,z-z_0\rangle=0$$

*由于 $\nabla F$ 是曲面法向量（第 7 节），切平面就是“点 + 垂直于梯度的平面”。*

**全微分**

$$df=f_x\,dx+f_y\,dy+f_z\,dz$$

*对于微小的输入扰动，输出如何变化的一阶估计——误差传播的主力工具。*

> **联系 — 可微不只是偏导数存在**
>
> 一个函数在某点**可微**，是指切平面确实近似它（误差比距离消失得更快）。两个偏导数都存在*并不*足够；但若偏导数在该点附近*连续*，则可微性有保证——这是你几乎总会用到的实用判据。

<a id="s9"></a>
### 高阶偏导数与克莱罗定理

*求两次导，次序可能要紧——然而了不起的是，它通常无关紧要。只要混合偏导数连续，它们就相等。*

**二阶偏导数与克莱罗定理**

$$f_{xx}=\partial_x\partial_x f,\quad f_{xy}=\partial_y\partial_x f,\quad f_{yx}=\partial_x\partial_y f$$

$$\text{If }f_{xy},f_{yx}\text{ are continuous near }(a,b),\ \text{then } f_{xy}(a,b)=f_{yx}(a,b).$$

**演示 — 为什么 $f_{xy}=f_{yx}$**

1. 构造混合了两个方向的二阶差商：

   $$\Delta=\frac{f(a+h,b+k)-f(a+h,b)-f(a,b+k)+f(a,b)}{hk}.$$
2. 先按 $x$ 上的差来分组：令 $g(x)=f(x,b+k)-f(x,b)$。则分子是 $g(a+h)-g(a)$。由中值定理，它等于 $h\,g'(\xi)=h\big(f_x(\xi,b+k)-f_x(\xi,b)\big)$，其中 $\xi$ 在 $a$ 与 $a+h$ 之间。
3. 再对 $f_x(\xi,\cdot)$ 在 $y$ 上用一次中值定理：方括号等于 $k\,f_{xy}(\xi,\eta)$。于是 $\Delta=f_{xy}(\xi,\eta)$。对称地，先按 $y$ 分组得到 $\Delta=f_{yx}(\xi',\eta')$。
4. 令 $h,k\to0$：$(\xi,\eta)$ 和 $(\xi',\eta')$ 都 $\to(a,b)$，由连续性

   $$f_{xy}(a,b)=\lim\Delta=f_{yx}(a,b).$$

*混合偏导数相等，恰好是恰当微分与保守场（第 20 节）背后的条件。*

<a id="s10"></a>
### 局部极值与二阶导数判别法

*山丘与山谷出现在曲面平坦之处——即梯度消失之处。一个二阶导数判别法把山峰与山口区分开。*

**临界点与二阶导数判别法**

$$\nabla f=\mathbf 0\ \Rightarrow\ \text{critical point};\qquad D=f_{xx}f_{yy}-f_{xy}^{\,2}$$

*$D>0,\ f_{xx}>0\Rightarrow$ 局部极小；$D>0,\ f_{xx}<0\Rightarrow$ 局部极大；$D<0\Rightarrow$ 鞍点；$D=0\Rightarrow$ 无法判定。*

> **概念 — 为什么 $D$ 是一个行列式**
>
> $D$ 是**黑塞矩阵** $\begin{pmatrix}f_{xx}&f_{xy}\\ f_{xy}&f_{yy}\end{pmatrix}$ 的行列式。在临界点附近 $f$ 看起来像一个二次型；黑塞矩阵的特征值给出沿主轴方向的曲率。两者皆正 → 碗形（极小）；两者皆负 → 穹顶（极大）；异号 → 鞍点。$D$ 的符号（特征值之积）与 $f_{xx}$ 的符号恰好还原出这些情形。

> **联系 — 升级版的微积分一**
>
> 在一元情形：$f'=0$ 然后检查 $f''$。这里 $\nabla f=\mathbf 0$ 代替了 $f'=0$，黑塞矩阵的行列式代替了单个 $f''$。其逻辑——先找平坦处，再探测曲率——是完全相同的。

<a id="s11"></a>
### 拉格朗日乘数法（约束最优化）

*要在约束 $g=c$ 之下最优化 $f$，你不能仅仅令 $\nabla f=\mathbf 0$。约束把你钉在一条曲线或一张曲面上——而答案就在梯度对齐之处。*

**拉格朗日条件**

$$\nabla f=\lambda\,\nabla g,\qquad g(x,y,\dots)=c$$

*对该方程组求解出各变量与乘数 $\lambda$。有两个约束时：$\nabla f=\lambda\nabla g+\mu\nabla h$。*

**演示 — 为什么梯度必须平行**

1. 约束 $g=c$ 把你限制在它的等值集上。参数化一条位于该集合中、在 $t_0$ 处经过某个约束极值的路径 $\mathbf r(t)$。
2. 沿这条路径，$f(\mathbf r(t))$ 在 $t_0$ 处有一个普通极值，故其导数在那里消失：

   $$\frac{d}{dt}f(\mathbf r(t))\Big|_{t_0}=\nabla f\cdot\mathbf r'(t_0)=0.$$
3. 于是对约束集中的每一条路径都有 $\nabla f\perp\mathbf r'(t_0)$——即 $\nabla f\perp$ 约束曲面。但 $\nabla g$ 也 $\perp$ 该曲面（第 7 节）。
4. 两个垂直于同一曲面的向量是平行的：

   $$\nabla f=\lambda\,\nabla g.$$

*在约束最优点处，$f$ 的等值线与约束相切——它们相吻，共享一条法线。乘数 $\lambda$ 度量最优值对约束水平 $c$ 的敏感度。*

## 第 C 部分 · 多重积分

<a id="s12"></a>
### 矩形与一般区域上的二重积分

*二重积分把一个函数在一片 2D 区域上加总起来——曲面之下的体积。富比尼定理让你一次一个变量地去计算它。*

**定义与富比尼定理**

$$\iint_R f\,dA=\lim_{\|P\|\to0}\sum_{i,j} f(x_i^*,y_j^*)\,\Delta A=\int_a^b\!\!\int_c^d f(x,y)\,dy\,dx$$

*在一个矩形上，积分次序可以自由选取。二重积分是小盒子 $f\cdot\Delta A$ 的黎曼和的极限。*

**一般区域（I 型／II 型）**

$$\iint_D f\,dA=\int_a^b\!\!\int_{g_1(x)}^{g_2(x)} f\,dy\,dx=\int_c^d\!\!\int_{h_1(y)}^{h_2(y)} f\,dx\,dy$$

*内层的限描述区域（是函数）；外层的限是常数。先把区域画出来——它决定了上下限，也常常决定哪种次序可行。*

> **原理 — 交换积分次序**
>
> 一个累次积分在某种次序下无从下手，换成另一种次序却可能初等可解。技巧是：从上下限重构出*区域*，然后用交换后的变量重新描述它。区域是不变量；上下限只是切分它的一种方式而已。

> **联系 — 把单重积分迭代起来**
>
> 二重积分不过是一个被积函数本身又是一个定积分的定积分。你所知道的关于 $\int$ 的一切都照搬过来；唯一的新技能是把一片 2D 区域翻译成嵌套的上下限。

<a id="s13"></a>
### 极坐标下的二重积分

*圆与圆盘在 $x,y$ 下是噩梦，在 $r,\theta$ 下却轻而易举。唯一的关窍——也是问题的核心——是面积元会多出一个因子 $r$。*

**极坐标二重积分**

$$x=r\cos\theta,\quad y=r\sin\theta,\qquad \iint_D f\,dA=\iint_D f(r\cos\theta,r\sin\theta)\,\underbrace{r\,dr\,d\theta}_{dA}$$

*那个 $r$ 不是可有可无的——忘掉它是经典错误。它是极坐标映射的雅可比行列式（第 16 节）。*

**演示 — 为什么 $dA=r\,dr\,d\theta$**

1. 用射线 $\theta=\text{const}$ 和圆 $r=\text{const}$ 分割区域。一个典型的“极坐标矩形”在半径 $r$ 处跨越角度 $\Delta\theta$ 和半径 $\Delta r$。
2. 它的两条弯曲边是圆弧。外弧长度为 $r\,\Delta\theta$；径向边长度为 $\Delta r$。对于微小的增量，这块面片近似一个矩形：

   $$\Delta A\approx(\text{arc length})\times(\text{radial width})=(r\,\Delta\theta)(\Delta r).$$
3. （精确地说：半径 $r$ 与 $r+\Delta r$ 之间、跨角 $\Delta\theta$ 的面积是 $\tfrac12\big((r+\Delta r)^2-r^2\big)\Delta\theta=\big(r+\tfrac12\Delta r\big)\Delta r\,\Delta\theta\to r\,\Delta r\,\Delta\theta$。）
4. 取极限，$dA=r\,dr\,d\theta$。

*离原点越远的面片，对同样的 $\Delta\theta$ 就越宽；因子 $r$ 正是为这种向外铺开而计的。*

> **联系 — 高斯积分**
>
> 极坐标攻克了 $\int_{-\infty}^{\infty}e^{-x^2}dx=\sqrt\pi$：把它平方成平面上的一个二重积分，转成极坐标，那个顽固的 $e^{-r^2}\,r\,dr$ 便由初等代换积出——来自 $dA$ 的那个 $r$ 正是让它奏效的关键。

<a id="s14"></a>
### 三重积分

*再多一维：在一个立体上积分。图像与记账方式都从二重积分直接延伸过来。*

**三重积分与体积**

$$\iiint_E f\,dV=\int\!\!\int\!\!\int f(x,y,z)\,dz\,dy\,dx,\qquad \text{Vol}(E)=\iiint_E 1\,dV$$

*最内层的限可以依赖另外两个外层变量；中间层依赖最外层；最外层是常数。*

> **原理 — 用投影加切片来建立**
>
> 把立体描述为：在某个坐标平面上的一片 2D **投影** $D$，其中 $z$ 在下曲面 $z=u_1(x,y)$ 与上曲面 $z=u_2(x,y)$ 之间变化。先对 $z$ 积分（对每个 $(x,y)$ 是一个单重积分），再把 $D$ 当作一个二重积分处理——也许用极坐标。

> **联系 — 同样的技能，更多的限**
>
> 三重积分是一个单重积分的二重积分。掌握它完全在于把一个 3D 立体翻译成嵌套的上下限——其中的微积分就是你早已会做的初等积分。

<a id="s15"></a>
### 柱坐标与球坐标

*具有轴对称或中心对称的立体，呼唤尊重那种对称性的坐标。每一种都带来它自己的体积元。*

**柱坐标**

$$x=r\cos\theta,\ y=r\sin\theta,\ z=z,\qquad dV=r\,dz\,dr\,d\theta$$

*在 $xy$ 平面上用极坐标，上面叠加普通的 $z$。最适合圆柱、圆锥、抛物面。*

**球坐标**

$$x=\rho\sin\phi\cos\theta,\ y=\rho\sin\phi\sin\theta,\ z=\rho\cos\phi,\qquad dV=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$$

*$\rho\ge0$ 是到原点的距离，$\phi\in[0,\pi]$ 是与 $+z$ 轴的夹角，$\theta\in[0,2\pi)$ 是经度。最适合球和锥。*

**演示 — 球坐标体积元 $\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$**

1. 把 $\rho$ 增加 $d\rho$：径向边长度为 $d\rho$。
2. 把 $\phi$ 增加 $d\phi$：该点在一个半径为 $\rho$ 的圆（一条经线）上扫出一段弧，长度为 $\rho\,d\phi$。
3. 把 $\theta$ 增加 $d\theta$：该点扫出一条纬度圆，其半径为 $\rho\sin\phi$（到 $z$ 轴的距离），给出弧长 $\rho\sin\phi\,d\theta$。
4. 这三条边两两垂直，故盒子的体积是它们之积：

   $$dV=(d\rho)(\rho\,d\phi)(\rho\sin\phi\,d\theta)=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta.$$

*$\rho^2$ 是球面表面积的增长；$\sin\phi$ 是纬度圆向两极的收缩。两者都直接从雅可比行列式（第 16 节）得出。*

<a id="s16"></a>
### 变量代换与雅可比行列式

*极坐标、柱坐标和球坐标都是同一条原理的特例：用一个光滑映射来换坐标，体积元便按其导数的行列式来缩放。*

**变量代换与雅可比行列式**

$$\iint_R f\,dx\,dy=\iint_S f\big(x(u,v),y(u,v)\big)\,\Big|\frac{\partial(x,y)}{\partial(u,v)}\Big|\,du\,dv$$

$$\frac{\partial(x,y)}{\partial(u,v)}=\det\!\begin{pmatrix} x_u & x_v\\ y_u & y_v\end{pmatrix}$$

*雅可比行列式是该变换的局部面积拉伸因子。在 $n$ 维中它是一个 $n\times n$ 行列式。*

**演示 — 极坐标雅可比行列式还原出那个 $r$**

1. 在 $x=r\cos\theta,\ y=r\sin\theta$ 下，计算偏导数：

   $$x_r=\cos\theta,\ x_\theta=-r\sin\theta,\ y_r=\sin\theta,\ y_\theta=r\cos\theta.$$
2. 构造雅可比行列式：

   $$\frac{\partial(x,y)}{\partial(r,\theta)}=\det\!\begin{pmatrix}\cos\theta & -r\sin\theta\\ \sin\theta & r\cos\theta\end{pmatrix}=r\cos^2\theta+r\sin^2\theta=r.$$
3. 因此 $dx\,dy=|r|\,dr\,d\theta=r\,dr\,d\theta$，正是第 13 节的极坐标元。

*这一部分中每一个特殊体积元都是一个行列式。同样的计算在球坐标下给出 $\rho^2\sin\phi$。*

> **概念 — 为什么是行列式？**
>
> 坐标映射的导数是一个矩阵（雅可比矩阵）；它把一个微小的坐标盒子送成一个微小的平行六面体。**行列式**正是一个线性映射缩放体积的那个因子（第 1 节的三重积）。所以雅可比行列式的绝对值就是局部的体积换算率。

<a id="s17"></a>
### 应用：质量、矩与质心

*多重积分从密度计算物理总量。模式始终是：对密度积分得到整体，对密度乘位置积分找到它的平衡之处。*

**质量、矩、形心**

$$m=\iint_D \rho\,dA,\qquad M_y=\iint_D x\,\rho\,dA,\quad M_x=\iint_D y\,\rho\,dA$$

$$\bar x=\frac{M_y}{m},\qquad \bar y=\frac{M_x}{m}$$

*三维版本是在一个立体上以 $dV$ 积分。在密度为常数时，质心是纯几何的**形心**。*

**转动惯量**

$$I_x=\iint_D y^2\rho\,dA,\quad I_y=\iint_D x^2\rho\,dA,\quad I_0=\iint_D (x^2+y^2)\rho\,dA$$

*惯量以到轴距离的*平方*来给质量加权——这正是为什么远离轴的质量如此强烈地抗拒转动。*

> **联系 — 反复出现的模板**
>
> 总量 = $\int(\text{密度})$；平均位置 = $\frac{\int(\text{位置})(\text{密度})}{\int(\text{密度})}$。同一个模板给出概率（密度积分为 1，均值 = $\int x f\,dx$）——通向统计学姊妹篇的桥梁。

## 第 D 部分 · 向量微积分

<a id="s18"></a>
### 向量场

*一个向量场给空间中每一点都系上一支箭头——风速、一个力、一个电场。在这些场上做微积分是整门课的高潮。*

**向量场与梯度场**

$$\mathbf F(x,y,z)=\langle P,\,Q,\,R\rangle,\qquad \mathbf F=\nabla f\ \Rightarrow\ \mathbf F \text{ is a gradient (conservative) field}$$

*这时 $f$ 是 $\mathbf F$ 的一个**势**。引力和静电学是梯度场。*

> **概念 — 通过流动来读一个场**
>
> 把场想象成一团流体的速度。两个问题组织起接下来的一切：沿一条曲线，流动*推动你*多少（环流量、线积分）；穿过一条边界，有多少流动*通过*（通量、面积分）。旋度度量局部旋转；散度度量局部源/汇。

<a id="s19"></a>
### 线积分（标量与向量）；功

*沿一条曲线积分。对标量，你把一个量按弧长加权求和；对场，你把它沿路径的分量求和——它所做的功。*

**标量与向量线积分**

$$\int_C f\,ds=\int_a^b f(\mathbf r(t))\,|\mathbf r'(t)|\,dt$$

$$\int_C \mathbf F\cdot d\mathbf r=\int_a^b \mathbf F(\mathbf r(t))\cdot\mathbf r'(t)\,dt=\int_C P\,dx+Q\,dy+R\,dz$$

*$ds=|\mathbf r'|\,dt$ 是弧长；$d\mathbf r=\mathbf r'\,dt$ 是有向的一步。向量积分是 $\mathbf F$ 沿 $C$ 所做的功。*

> **概念 — 标量线积分与向量线积分之别**
>
> **标量**积分 $\int_C f\,ds$ 与方向无关（它按长度加权——想想一根金属丝的质量）。**向量**积分 $\int_C\mathbf F\cdot d\mathbf r$ 在你反转曲线时变号，因为它度量的是有向的推动。功与环流量都是向量线积分。

> **联系 — 投影到切向上**
>
> $\mathbf F\cdot d\mathbf r=(\mathbf F\cdot\mathbf T)\,ds$：功积分是切向分量 $\mathbf F\cdot\mathbf T$ 的标量积分。这个切向视角将成为格林定理和斯托克斯定理的左端（环流量）。

<a id="s20"></a>
### 线积分基本定理与保守场

*对一个梯度场，线积分只依赖于端点——而非路径。这就是微积分基本定理本身，被提升到空间中的曲线上。*

**线积分基本定理**

$$\int_C \nabla f\cdot d\mathbf r=f(\mathbf r(b))-f(\mathbf r(a))$$

*与路径无关；沿一条闭合回路它是 $0$。这样的 $\mathbf F=\nabla f$ 是**保守的**。*

**保守场的判据（单连通域）**

$$\mathbf F=\langle P,Q\rangle \text{ conservative}\iff \frac{\partial P}{\partial y}=\frac{\partial Q}{\partial x}\quad\big(\text{in 3D: }\nabla\times\mathbf F=\mathbf 0\big)$$

*交叉偏导数判据是克莱罗定理（第 9 节）的乔装：若 $\mathbf F=\nabla f$，则 $P_y=f_{xy}=f_{yx}=Q_x$。*

**演示 — 证明线积分基本定理**

1. 设 $\mathbf F=\nabla f$，用 $\mathbf r(t),\ a\le t\le b$ 参数化 $C$。则

   $$\int_C\nabla f\cdot d\mathbf r=\int_a^b\nabla f(\mathbf r(t))\cdot\mathbf r'(t)\,dt.$$
2. 由多元链式法则（第 6 节），被积函数是一个全导数：

   $$\nabla f(\mathbf r(t))\cdot\mathbf r'(t)=\frac{d}{dt}\,f(\mathbf r(t)).$$
3. 现在它是一个普通的单变量积分；应用经典的微积分基本定理：

   $$\int_a^b\frac{d}{dt}f(\mathbf r(t))\,dt=f(\mathbf r(b))-f(\mathbf r(a)).$$

*梯度是多元导数；对它积分便在边界点上还原出函数——第 27 节边界原理的第一个实例。*

<a id="s21"></a>
### 格林定理

*伟大定理中的第一个：一个场绕一条闭合平面曲线的环流量，等于其（标量）旋度在所围区域上的积分。*

**格林定理（环流量形式）**

$$\oint_C P\,dx+Q\,dy=\iint_D\Big(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\Big)\,dA$$

*$C$ 是区域 $D$ 的正向（逆时针）边界。右端的被积函数是 2D 标量旋度。*

**两个推论**

$$\text{Area}(D)=\oint_C x\,dy=-\oint_C y\,dx=\tfrac12\oint_C x\,dy-y\,dx$$

$$\text{Flux form: }\ \oint_C \mathbf F\cdot\mathbf n\,ds=\iint_D \Big(\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}\Big)\,dA$$

*环流量形式是 2D 的斯托克斯定理；通量形式是 2D 的散度定理。同一个定理，两种读法。*

**演示 — 在 I 型／II 型区域上的格林定理**

1. 先证 $P$ 这一部分。对一个 I 型区域 $D=\{a\le x\le b,\ g_1(x)\le y\le g_2(x)\}$，把旋度项在 $D$ 上积分：

   $$\iint_D \!-\frac{\partial P}{\partial y}\,dA=-\int_a^b\!\!\int_{g_1}^{g_2}\frac{\partial P}{\partial y}\,dy\,dx.$$
2. 用微积分基本定理做内层积分：

   $$=-\int_a^b\big[P(x,g_2(x))-P(x,g_1(x))\big]\,dx.$$
3. 现在直接计算 $\oint_C P\,dx$。顶部边界（右→左）贡献 $-\int_a^b P(x,g_2)\,dx$；底部（左→右）贡献 $+\int_a^b P(x,g_1)\,dx$；竖直边上 $dx=0$。相加后与第 2 步吻合：

   $$\oint_C P\,dx=\iint_D\!-\frac{\partial P}{\partial y}\,dA.$$
4. 对称地，把 $D$ 看作 II 型给出 $\oint_C Q\,dy=\iint_D \frac{\partial Q}{\partial x}\,dA$。把两者相加。

*一个一般区域是由这样的块拼接而成；内部边界成对相消，只剩外围曲线。这种相消是第 D 部分每一个定理背后的引擎。*

<a id="s22"></a>
### 旋度与散度

*向量场上的两个求导算子。旋度度量微观的旋转；散度度量净流出。它们是斯托克斯定理和高斯定理的被积函数。*

**借助 $\nabla$ 的旋度与散度**

$$\nabla\times\mathbf F=\begin{vmatrix}\mathbf i&\mathbf j&\mathbf k\\ \partial_x&\partial_y&\partial_z\\ P&Q&R\end{vmatrix},\qquad \nabla\cdot\mathbf F=\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}$$

*旋度返回一个向量（旋转的轴）；散度返回一个标量（源的强度）。*

**两个组织起一切的恒等式**

$$\nabla\times(\nabla f)=\mathbf 0,\qquad \nabla\cdot(\nabla\times\mathbf F)=0$$

*“梯度的旋度为零”（梯度场是无旋的）；“旋度的散度为零”（旋度场是无源的）。两者都是穿着向量外衣的克莱罗定理。*

> **概念 — 物理意义**
>
> 在流动中放一个微小的桨轮：它绕轴 $\nabla\times\mathbf F$ 旋转，速率由 $|\nabla\times\mathbf F|$ 决定。包住一个微小的球：$\nabla\cdot\mathbf F$ 是每单位体积的净流出通量——在源处为正，在汇处为负。这些局部的读数在积分后便成为全局的定理。

**演示 — 梯度的旋度消失**

1. 取 $\mathbf F=\nabla f=\langle f_x,f_y,f_z\rangle$。$\nabla\times\mathbf F$ 的 $\mathbf k$ 分量是

   $$\partial_x(f_y)-\partial_y(f_x)=f_{yx}-f_{xy}.$$
2. 由克莱罗定理（第 9 节），$f_{xy}=f_{yx}$，所以这个分量是 $0$；同样的相消也消掉了 $\mathbf i$ 和 $\mathbf j$ 分量。

*因此保守 $\Rightarrow$ 无旋——这是第 20 节 $P_y=Q_x$ 判据的 3D 版本。*

<a id="s23"></a>
### 参数曲面与曲面面积

*正如一条曲线是一个参数，一张曲面是两个参数。两个切向量的叉积给出法向量——以及面积元。*

**参数化、法向量、曲面面积**

$$\mathbf r(u,v)=\langle x,y,z\rangle,\qquad \mathbf r_u\times\mathbf r_v=\text{normal},\qquad dS=|\mathbf r_u\times\mathbf r_v|\,du\,dv$$

$$A(S)=\iint_D |\mathbf r_u\times\mathbf r_v|\,dA$$

*对一个图像 $z=g(x,y)$：$dS=\sqrt{1+g_x^2+g_y^2}\,dA$。*

**演示 — 曲面面积元 $dS=|\mathbf r_u\times\mathbf r_v|\,du\,dv$**

1. 一个小参数矩形 $[u,u+du]\times[v,v+dv]$ 映射到 $S$ 上的一块弯曲面片。它的两条边近似是缩放后的切向量：$\mathbf r_u\,du$ 与 $\mathbf r_v\,dv$。
2. 这块面片近似是由这两条边张成的平行四边形。它的面积是它们叉积的大小（第 1 节）：

   $$dS=|\mathbf r_u\,du\times\mathbf r_v\,dv|=|\mathbf r_u\times\mathbf r_v|\,du\,dv.$$

*叉积身兼两职：它的方向是曲面法向量（通量所需），它的大小是面积尺度。*

<a id="s24"></a>
### 面积分与通量

*在一张曲面上积分。对标量，按面积加权；对场，把穿过曲面的分量求和——即通量。*

**标量面积分与通量**

$$\iint_S f\,dS=\iint_D f(\mathbf r(u,v))\,|\mathbf r_u\times\mathbf r_v|\,dA$$

$$\iint_S \mathbf F\cdot d\mathbf S=\iint_S \mathbf F\cdot\mathbf n\,dS=\iint_D \mathbf F\cdot(\mathbf r_u\times\mathbf r_v)\,dA$$

*$d\mathbf S=\mathbf n\,dS=(\mathbf r_u\times\mathbf r_v)\,dA$。通量度量每单位时间有多少 $\mathbf F$ 穿过 $S$。*

> **概念 — 定向要紧**
>
> 一个通量积分需要选定一侧：一个**定向**，由一个连续的单位法向量 $\mathbf n$ 给出。翻转 $\mathbf n$ 就翻转符号。对一张闭合曲面，约定取*向外*的法向量。（莫比乌斯带是不可定向的——不存在一致的选择。）

> **联系 — 与线积分的对应**
>
> 标量面积分 ↔ 标量线积分（按测度加权）；通量 $\iint\mathbf F\cdot\mathbf n\,dS$ ↔ 环流量 $\int\mathbf F\cdot\mathbf T\,ds$。曲线用切向量；曲面用法向量。斯托克斯（第 25 节）和高斯（第 26 节）把这些联系到一起。

<a id="s25"></a>
### 斯托克斯定理

*把格林定理从平面上抬起来。一张曲面边界曲线上的环流量，等于旋度穿过该曲面的通量。*

**斯托克斯定理**

$$\oint_{\partial S} \mathbf F\cdot d\mathbf r=\iint_S (\nabla\times\mathbf F)\cdot d\mathbf S$$

*$\partial S$ 是 $S$ 的边界曲线，相对 $\mathbf n$ 按右手定则定向。任意以相同边界为界的曲面都给出相同的答案。*

> **概念 — 把微观的旋转加起来**
>
> 旋度是每单位面积的局部环流量。用许多微小的回路铺满曲面；在每个回路上，环流量 $\approx(\nabla\times\mathbf F)\cdot\mathbf n\,dS$。相邻回路共享被以*相反*方向遍历的边，所以所有内部贡献相消——只有外围边界存活。那种相消就是格林定理的证明（第 21 节），如今在曲面上。

> **联系 — 格林是平坦的斯托克斯**
>
> 取 $S$ 为 $xy$ 平面中的一片区域，$\mathbf n=\mathbf k$。则 $(\nabla\times\mathbf F)\cdot\mathbf k=Q_x-P_y$，斯托克斯定理变成 $\oint P\,dx+Q\,dy=\iint(Q_x-P_y)\,dA$——正是格林定理。

<a id="s26"></a>
### 散度（高斯）定理

*一个场向外穿过一张闭合曲面的通量，等于其散度在内部立体上的积分。内部的源解释了净流出。*

**散度定理**

$$\oiint_{\partial E} \mathbf F\cdot d\mathbf S=\iiint_E (\nabla\cdot\mathbf F)\,dV$$

*$\partial E$ 是立体 $E$ 的闭合边界曲面，取向外的法向量。总流出 = 内部的总源强度。*

> **概念 — 把通量逐层抵消**
>
> 散度是每单位体积的净流出。把 $E$ 切成许多微小的盒子；每个贡献 $(\nabla\cdot\mathbf F)\,dV$ 的流出。两个盒子相接之处，从一个流出的通量就是流*入*另一个的通量——大小相等、方向相反，故相消。只剩外围曲面。与格林和斯托克斯相同的相消原理。

> **联系 — 格林的通量形式是平坦的高斯**
>
> 在平面上，散度定理读作 $\oint_C\mathbf F\cdot\mathbf n\,ds=\iint_D(P_x+Q_y)\,dA$——正是格林定理的通量形式（第 21 节）。高斯定理是它的 3D 升级。

## 第 E 部分 · 综合

<a id="s27"></a>
### 统一的图景：一个定理统辖全部

*五个定理——微积分基本定理、线积分基本定理、格林、斯托克斯、高斯——是同一个陈述从不同维度看到的样子：一个导数在区域上的积分，等于函数在其边界上的积分。*

> **原理 — 广义斯托克斯定理**
>
> 用微分形式的语言，五者全都坍缩成一行：**$d\omega$ 在区域 $M$ 上的积分，等于 $\omega$ 在边界 $\partial M$ 上的积分**。这里 $d$ 是外微分（它特殊化为梯度、旋度、散度），而 $\partial$ 是“取边界”。每一个经典定理都是它在特定维度和特定算子下的样子。

**主陈述**

$$\int_{M} d\omega=\int_{\partial M}\omega$$

*“先求导再在内部积分 = 把原物在边界上积分。”下面每一个定理都是它的一个实例。*

| 定理 | 区域 $M$ | 边界 $\partial M$ | 导数 $d$ |
| --- | --- | --- | --- |
| 微积分基本定理（微积分一） | 区间 $[a,b]$ | 两个端点 | $f'$ |
| 线积分基本定理 | 曲线 $C$ | 两个端点 | 梯度 $\nabla f$ |
| 格林 | 平面区域 $D$ | 曲线 $\partial D$ | 标量旋度 $Q_x-P_y$ |
| 斯托克斯 | 曲面 $S$ | 曲线 $\partial S$ | 旋度 $\nabla\times\mathbf F$ |
| 散度 | 立体 $E$ | 曲面 $\partial E$ | 散度 $\nabla\cdot\mathbf F$ |

**演示 — 从主陈述读出每一个经典定理**

1. 微积分基本定理：$M=[a,b]$，$d\omega=f'\,dx$，且 $\int_{\partial M}\omega=f(b)-f(a)$（带符号 $+,-$ 的两个端点）。一个 0 维集合的边界“积分”不过是取值。
2. 线积分基本定理：$M=C$，$\omega=f$，$d\omega=\nabla f\cdot d\mathbf r$；边界是两个端点——第 20 节。
3. 格林／斯托克斯：$M$ 是 2 维的，$d$ 产生旋度，$\partial M$ 是界定它的曲线——环流量 = 旋度通量。
4. 散度：$M$ 是 3 维的，$d$ 产生散度，$\partial M$ 是界定它的曲面——流出 = 源的总量。

*每一次反复出现的证明手法都相同：把区域铺成小块，注意内部边界成对相消，只有 $\partial M$ 存活。*

#### 整个向量微积分浓缩成一行

> 内部的导数 = 边界上的值 · $ \displaystyle\int_M d\omega=\int_{\partial M}\omega $

> **要保持的习惯**
>
> 每当你遇到一个新的积分恒等式，就问本课程的那两个问题：*区域是什么，它的边界是什么？*在偏导数、多重积分、通量与环流量的背后，坐着同一个思想——一个导数在内部加总起来，就是在边缘读出的那个函数——这是微积分基本定理，一路向上贯穿到底。

---

*一门多元与向量微积分的第三学期课程——概念、原理、公式，以及它们背后的演示——作为统计学与微积分指南的姊妹篇而建。先通读一遍把握形状；随时回到任一方框当作参考。记住：这里每一个伟大定理都在说同一件事——在一片区域上积分一个导数，你便在它的边界上把函数取了回来。*
