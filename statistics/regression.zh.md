[English](regression.md) · **中文**

# 回归，*最佳直线及其超越。*

从穿过一团点云的一条直线，到线性模型的全套机器——作为微积分的最小二乘、投影的矩阵几何、诚实的推断，以及那些驱动现代数据科学的推广（逻辑回归、广义线性模型、岭回归与套索）。每个核心结果都被**演示**，并把通向微积分、概率论和线性代数的脉络明确呈现。

[← 返回全部指南](../README.zh.md)

## A 部分 · 简单线性回归

<a id="s0"></a>
### 全局图景：对关系建模

回归回答了一个相关性只能暗示的问题：既然两个（或多个）变量一起变动，我们能否写出一个*函数*，由其他变量预测某一个变量——并量化这个预测有多好？它是应用统计学的主力，也是通向机器学习的门户。

- **信号 + 噪声** —— 我们假设响应 $y$ 是预测变量的一个系统性函数加上随机误差：$y=f(\mathbf{x})+\varepsilon$。
- **估计** —— 通过最小化一个损失（通常是平方误差）来拟合未知函数（这里是一条直线/平面）。
- **推断与预测** —— 给拟合系数和未来预测附上不确定性。

> **原理 —— 回归模型把数据分解为结构与噪声**
>
> 每个回归都写成 $ \text{观测值} = \text{模型} + \text{残差} $。其艺术在于选择一个足够丰富以捕捉结构、却又足够简单以不去拟合噪声的模型。**线性模型**——响应是（预测变量的函数的）线性组合——是基础，因为它可解释、有闭式解，并支撑几乎所有更高级的方法。

**一般的监督学习框架**

$$y_i = f(\mathbf{x}_i) + \varepsilon_i,\qquad E[\varepsilon_i]=0,\qquad i=1,\dots,n$$

*线性模型取 $f(\mathbf{x})=\boldsymbol{\beta}^\top\mathbf{x}$。广义线性模型让 $E[y]$ 的一个已知函数为线性。非参数方法让 $f$ 灵活。同样的"损失—拟合"逻辑贯穿它们全部。*

#### 整篇指南浓缩为一行

> 最佳直线 → 作为微积分的最小二乘 → 矩阵形式与投影 → 推断与方差分析 → 逻辑回归与广义线性模型 → 正则化及其超越

> **联系 —— 接续《统计学》指南停下之处**
>
> 入门《统计学》伴读结束于**相关与最小二乘直线**（其第 13 节）。本指南恰好从那里出发，并对它进行推导、推广和压力测试。请把它的核心思想牢记于心——**z 分数**以及那个问题"距期望有多远，以多少个标准差计？"——因为这里的每个 t 比和 F 比都是同一个想法。

<a id="s1"></a>
### 简单线性回归与最小二乘

*一个预测变量、一个响应、一条直线——通过最小化竖直距离的平方和来拟合。*

**简单线性回归模型**

$$y_i = \beta_0 + \beta_1 x_i + \varepsilon_i,\qquad \varepsilon_i \stackrel{\text{iid}}{\sim}(0,\sigma^2)$$

*$\beta_0$（截距）和 $\beta_1$（斜率）是未知**参数**；$\varepsilon_i$ 是均值为 0、方差恒定为 $\sigma^2$ 的随机噪声。拟合直线为 $\hat y = \hat\beta_0 + \hat\beta_1 x$，第 $i$ 个**残差**为 $e_i = y_i - \hat y_i$。*

> **概念 —— 为什么用平方（而非绝对值）误差？**
>
> 我们用**残差平方和** $\sum e_i^2$ 度量失拟。平方是光滑的（处处可微，故微积分适用）、对大的偏离重重惩罚，并且——关键地——在正态误差下，最小二乘拟合也是**极大似然**拟合。绝对误差给出类似中位数的 $L_1$ 拟合（稳健，但无闭式解）。

**演示 —— 通过最小化平方和导出斜率与截距**

1. 目标是两个未知量的函数：

   $$S(\beta_0,\beta_1)=\sum_{i=1}^{n}\big(y_i-\beta_0-\beta_1 x_i\big)^2.$$
2. 这是一个无约束优化——把两个偏导数都置零（微积分的一阶条件）：

   $$\frac{\partial S}{\partial \beta_0}=-2\sum\big(y_i-\beta_0-\beta_1 x_i\big)=0,\qquad \frac{\partial S}{\partial \beta_1}=-2\sum x_i\big(y_i-\beta_0-\beta_1 x_i\big)=0.$$
3. 第一个方程给出正规方程的一部分 $\sum y_i = n\beta_0 + \beta_1\sum x_i$；除以 $n$，

   $$\hat\beta_0 = \bar y - \hat\beta_1 \bar x.$$
4. 代回第二个方程并利用 $\sum(x_i-\bar x)=0$ 化简：

   $$\hat\beta_1=\frac{\sum (x_i-\bar x)(y_i-\bar y)}{\sum (x_i-\bar x)^2}=\frac{S_{xy}}{S_{xx}}.$$
5. $S$ 的二阶导数（Hessian）是正定的，故这个驻点是唯一的全局极小值。

*因为 $\hat\beta_0=\bar y-\hat\beta_1\bar x$，拟合直线总是穿过质心 $(\bar x,\bar y)$。*

**相关形式的斜率**

$$\hat\beta_1 = r\,\frac{s_y}{s_x},\qquad r=\frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}$$

*其中 $s_x,s_y$ 是样本标准差，$r$ 是相关系数。斜率是按散布之比重新缩放的相关系数——回归和相关是同一个量的两个面。*

**演示 —— $\hat\beta_1 = r\,s_y/s_x$**

1. 从 $\hat\beta_1=S_{xy}/S_{xx}$ 出发，回忆 $r=S_{xy}/\sqrt{S_{xx}S_{yy}}$，故 $S_{xy}=r\sqrt{S_{xx}S_{yy}}$。
2. 代入：

   $$\hat\beta_1=\frac{r\sqrt{S_{xx}S_{yy}}}{S_{xx}}=r\,\sqrt{\frac{S_{yy}}{S_{xx}}}.$$
3. 由于 $s_y=\sqrt{S_{yy}/(n-1)}$ 且 $s_x=\sqrt{S_{xx}/(n-1)}$，$(n-1)$ 抵消：

   $$\hat\beta_1=r\,\frac{s_y}{s_x}.$$

*如果 $x$ 和 $y$ 被标准化（$s_x=s_y=1$），斜率*就是*相关系数——而"向均值回归"现象出现，因为 $|r|\le 1$。*

> **联系 —— 这就是你已经知道的微积分优化**
>
> 通过把偏导数置零来最小化 $S(\beta_0,\beta_1)$，恰好是微积分课程中的多元优化，应用于数据。正定的 Hessian 是保证极小值的二阶导数检验。回归是装上了统计学解释的微积分优化。

<a id="s2"></a>
### Gauss–Markov 定理与估计量的性质

*为什么最小二乘特殊：在所有线性无偏估计量中，它方差最小。*

**斜率的无偏性**

$$E[\hat\beta_1]=\beta_1,\qquad E[\hat\beta_0]=\beta_0$$

$$\operatorname{Var}(\hat\beta_1)=\frac{\sigma^2}{S_{xx}},\qquad \operatorname{Var}(\hat\beta_0)=\sigma^2\!\left(\frac1n+\frac{\bar x^2}{S_{xx}}\right)$$

*$x$ 的散布越大（$S_{xx}$ 越大）意味着斜率被钉得越紧。这就是为什么好的实验设计要把预测变量的取值铺开。*

**演示 —— $\hat\beta_1$ 无偏并求其方差**

1. 把斜率写成响应的线性组合：$\hat\beta_1=\sum c_i y_i$，权重 $c_i=(x_i-\bar x)/S_{xx}$。注意 $\sum c_i=0$ 且 $\sum c_i x_i=1$。
2. 取期望，利用 $E[y_i]=\beta_0+\beta_1 x_i$：

   $$E[\hat\beta_1]=\sum c_i(\beta_0+\beta_1 x_i)=\beta_0\underbrace{\textstyle\sum c_i}_{0}+\beta_1\underbrace{\textstyle\sum c_i x_i}_{1}=\beta_1.$$
3. 对方差，$y_i$ 相互独立，方差为 $\sigma^2$：

   $$\operatorname{Var}(\hat\beta_1)=\sum c_i^2\,\sigma^2=\frac{\sigma^2}{S_{xx}^2}\sum(x_i-\bar x)^2=\frac{\sigma^2}{S_{xx}}.$$

*这里不需要正态性假设——只需 $E[\varepsilon]=0$、方差恒定和独立性。*

> **原理 —— Gauss–Markov：普通最小二乘是最优线性无偏估计**
>
> 在线性、零均值误差、**同方差性**（方差恒定）以及误差不相关的假设下，普通最小二乘估计量是**最优线性无偏估计量**：在所有既线性于 $\mathbf{y}$ 又无偏的估计量中，普通最小二乘方差最小。这里"最优"指方差最小，而非可能误差最小。

**演示 —— 普通最小二乘为何是最优线性无偏估计的概要**

1. 考虑任意其他线性无偏估计量 $\tilde\beta_1=\sum d_i y_i$。无偏性强制 $\sum d_i=0$ 且 $\sum d_i x_i=1$，与普通最小二乘权重 $c_i$ 满足的约束相同。
2. 写 $d_i = c_i + \delta_i$。约束蕴含 $\sum \delta_i = 0$ 且 $\sum \delta_i x_i = 0$，由此 $\sum c_i \delta_i = 0$（交叉项消失）。
3. 于是方差干净地拆开：

   $$\operatorname{Var}(\tilde\beta_1)=\sigma^2\sum d_i^2=\sigma^2\Big(\sum c_i^2 + \sum \delta_i^2\Big)=\operatorname{Var}(\hat\beta_1)+\sigma^2\sum\delta_i^2.$$
4. 由于 $\sum\delta_i^2\ge 0$，任何对普通最小二乘权重的偏离只会增大方差。

*在线性无偏的竞争者中，普通最小二乘坐落在方差碗的底部——Gauss–Markov 最优。*

**估计误差方差**

$$\hat\sigma^2 = s^2 = \frac{1}{n-2}\sum_{i=1}^n e_i^2 = \frac{\text{SSE}}{n-2}$$

*除以 $n-2$，而非 $n$：估计了两个参数（$\beta_0,\beta_1$），耗费了两个**自由度**。这使 $s^2$ 成为 $\sigma^2$ 的无偏估计——与入门指南中 Bessel 的 $n-1$ 同样的逻辑，加以推广。*

<a id="s3"></a>
### 斜率与截距的推断；置信区间与预测区间

*从点估计到诚实的不确定性：检验一个斜率是否真实，并夹住未来的结果。*

**系数的 t 统计量**

$$t = \frac{\hat\beta_1 - \beta_1^{(0)}}{\operatorname{SE}(\hat\beta_1)},\qquad \operatorname{SE}(\hat\beta_1)=\frac{s}{\sqrt{S_{xx}}}$$

*在正态误差和 $H_0:\beta_1=\beta_1^{(0)}$ 下，这服从自由度为 $n-2$ 的 $t$ 分布。检验 $\beta_1^{(0)}=0$ 问的是"究竟有没有任何线性关系？"*

> **概念 —— 为什么用 $t$，以及为什么是 $n-2$ 个自由度**
>
> 如果我们知道 $\sigma$，标准化的斜率将恰好是正态的。但我们用 $s$ 估计它，注入了额外的不确定性——更肥的尾部——正如在单样本 t 检验中那样。自由度降到 $n-2$，因为拟合两个系数用掉了两条信息。

**斜率的置信区间**

$$\hat\beta_1 \pm t^{*}_{n-2}\;\frac{s}{\sqrt{S_{xx}}}$$

*"估计 ± 临界值 × 标准误"——通用的置信区间模板，现在用于一个回归系数。*

> **原理 —— 置信区间 vs 预测区间**
>
> 在一个新的 $x_0$ 处有两个非常不同的问题。**对均值响应的置信区间**夹住 $E[y\mid x_0]$ ——在 $x_0$ 处 $y$ 的平均值。**预测区间**夹住单个未来观测 $y_0$，故它必须加上一个新点的不可约噪声 $\sigma^2$。预测区间总是更宽，并且即使 $n\to\infty$ 仍保持宽。

**在 $x_0$ 处的置信 vs 预测区间**

$$\hat y_0 \pm t^{*}_{n-2}\,s\sqrt{\frac1n+\frac{(x_0-\bar x)^2}{S_{xx}}}\quad\text{(mean response)}$$

$$\hat y_0 \pm t^{*}_{n-2}\,s\sqrt{1+\frac1n+\frac{(x_0-\bar x)^2}{S_{xx}}}\quad\text{(new observation)}$$

*根号下那个孤零零多出来的 $1$ 是新的 $\varepsilon_0$ 的方差。两个区间都随 $x_0$ 远离 $\bar x$ 而向外张开——外推是危险的。*

**演示 —— 为什么两个区间都在远离 $\bar x$ 时变宽**

1. 在 $x_0$ 处的拟合均值为 $\hat y_0=\hat\beta_0+\hat\beta_1 x_0=\bar y+\hat\beta_1(x_0-\bar x)$。
2. 它的方差结合了 $\bar y$ 与斜率中的不确定性：

   $$\operatorname{Var}(\hat y_0)=\frac{\sigma^2}{n}+(x_0-\bar x)^2\operatorname{Var}(\hat\beta_1)=\sigma^2\!\left(\frac1n+\frac{(x_0-\bar x)^2}{S_{xx}}\right).$$
3. $(x_0-\bar x)^2$ 项随你离开数据中心而二次增长——区间向外弯成一条双曲线。
4. 对一个新观测，加上新鲜的噪声 $\operatorname{Var}(\varepsilon_0)=\sigma^2$，产生那个额外的 $+1$。

*预测在观测到的 $x$ 范围核心附近最可信。*

> **联系 —— 通向《推断》（t/F 分布、极大似然）**
>
> 这里的 $t$ 比在精神上与《推断》指南的单样本 $t$ 检验完全相同。在正态误差下，最小二乘估计与**极大似然**估计重合，而 $t$ 与（稍后的）$F$ 抽样分布恰好是那门课程从正态导出的那些。

<a id="s4"></a>
### 评估拟合：R²、残差与诊断

*一条拟合直线不会自动就是好直线。两件工具：一个单一的拟合优度数字，以及对残余之物的仔细审视。*

**平方和分解**

$$\underbrace{\sum(y_i-\bar y)^2}_{\text{SST}} = \underbrace{\sum(\hat y_i-\bar y)^2}_{\text{SSR}} + \underbrace{\sum(y_i-\hat y_i)^2}_{\text{SSE}}$$

*总变异 = 模型（回归）解释的变异 + 仍未解释的变异（误差/残差）。*

**演示 —— 为什么 SST = SSR + SSE（交叉项消失）**

1. 拆分每个中心化的响应：$y_i-\bar y = (\hat y_i-\bar y)+(y_i-\hat y_i)$，然后平方并求和：

   $$\text{SST}=\text{SSR}+\text{SSE}+2\sum(\hat y_i-\bar y)(y_i-\hat y_i).$$
2. 正规方程给出 $\sum e_i=0$ 和 $\sum x_i e_i = 0$；由于 $\hat y_i-\bar y=\hat\beta_1(x_i-\bar x)$ 是 $x_i$ 的线性函数，交叉项是 $\sum e_i$ 与 $\sum x_i e_i$ 的组合。
3. 两者都为零，故交叉项消失：

   $$\sum(\hat y_i-\bar y)(y_i-\hat y_i)=0.$$

*几何上：残差向量正交于拟合值方向——$n$ 维空间中的勾股定理（为第 6 节的帽子矩阵作铺垫）。*

**判定系数**

$$R^2 = \frac{\text{SSR}}{\text{SST}} = 1 - \frac{\text{SSE}}{\text{SST}}$$

*$y$ 中被模型解释的方差比例。在简单回归中 $R^2=r^2$ 精确成立。$R^2=0.7$ 意味着该直线解释了 70% 的变异性。*

> **概念 —— R² 必要但不充分**
>
> 高 $R^2$ 不能证明模型正确：它可以被加入垃圾预测变量而虚高，并且它对线性形式、方差恒定或独立性假设是否成立只字不提。Anscombe 四重奏——四个 $R^2$ 相同但形状迥异的数据集——是经典的警示。永远要查看**残差图**。

**残差诊断 —— 画什么，揭示什么**

***残差对拟合值：**弯曲的带状暗示非线性；漏斗形暗示异方差。**残差的 Q–Q 图：**偏离对角线标示出非正态误差。**残差对次序/时间：**模式标示出自相关。**杠杆与 Cook 距离：**识别那些凭一己之力操纵拟合的高影响点。*

> **原理 —— 四条假设，助记词"LINE"**
>
> 均值的**线性（L**inearity），误差的**独立性（I**ndependence），误差的**正态性（N**ormality，精确的 $t$/$F$ 推断需要它，无偏性不需要），以及**等方差（E**qual variance，同方差性）。诊断就是你检查每一条的方式。违反并不总是使拟合失效，但它们会改变哪些推断值得信赖。

> **联系 —— 通向《统计学》指南的相关**
>
> 恒等式 $R^2=r^2$ 把本节直接系回入门指南：你在那里算出的相关系数*就是*这里被解释方差的平方根。回归把相关从"它们一起变动吗？"提升为"变动多少，以及多可靠？"

## B 部分 · 多元线性回归

<a id="s5"></a>
### 矩阵形式的多元回归模型

*预测变量一多，标量代数就变得笨拙。线性代数使整套理论紧凑而精确。*

**堆叠成矩阵的模型**

$$\mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon},\qquad E[\boldsymbol{\varepsilon}]=\mathbf{0},\quad \operatorname{Cov}(\boldsymbol{\varepsilon})=\sigma^2\mathbf{I}$$

$$\mathbf{y}\in\mathbb{R}^{n},\quad \mathbf{X}\in\mathbb{R}^{n\times p},\quad \boldsymbol{\beta}\in\mathbb{R}^{p}$$

*$\mathbf{X}$ 的每一行是一个观测的预测变量；第一列通常全为 1 以承载截距。$\boldsymbol{\beta}$ 收集所有系数。单个方程 $\mathbf{y}=\mathbf{X}\boldsymbol{\beta}+\boldsymbol{\varepsilon}$ 对每一行同时成立。*

> **概念 —— 设计矩阵 $\mathbf{X}$**
>
> 矩阵 $\mathbf{X}$ 被称为**设计矩阵**，因为在一个实验中你确实是在设计它。它的列可以是原始预测变量、变换（$x^2,\log x$）、类别的虚拟变量，或交互项——任何*关于系数线性*的东西。"线性模型"意味着关于 $\boldsymbol{\beta}$ 线性，而非关于 $x$：$y=\beta_0+\beta_1 x+\beta_2 x^2$ 是一个完全线性的模型。

**解释一个系数**

*$\beta_j$ 是在**保持所有其他预测变量固定**时，$x_j$ 增加一个单位所对应的 $y$ 的期望变化。这条"其他一切相等"的条款正是把多元回归与一堆简单回归区分开的东西——它针对其他变量校正了每个预测变量。*

> **联系 —— 通向线性代数**
>
> 从此往后，回归*就是*线性代数：拟合是解一个线性系统，拟合值是一个正交投影，方差住在 $(\mathbf{X}^\top\mathbf{X})^{-1}$ 中，而共线性是近奇异。$\mathbf{X}^\top\mathbf{X}$ 的特征值支配稳定性。一切都归结为向量、矩阵和子空间的几何。

<a id="s6"></a>
### 通过线性代数的最小二乘：正规方程与帽子矩阵

*本学科中最重要的单个计算——以及它作为投影的优美几何意义。*

**正规方程与普通最小二乘估计量**

$$\mathbf{X}^\top\mathbf{X}\,\hat{\boldsymbol{\beta}} = \mathbf{X}^\top\mathbf{y}\quad\Longrightarrow\quad \hat{\boldsymbol{\beta}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$$

*只要 $\mathbf{X}$ 列满秩（无精确共线性），$\mathbf{X}^\top\mathbf{X}$ 可逆，它就有效。*

**演示 —— 通过矩阵微积分导出正规方程**

1. 把损失写成平方范数：

   $$S(\boldsymbol{\beta})=\|\mathbf{y}-\mathbf{X}\boldsymbol{\beta}\|^2=(\mathbf{y}-\mathbf{X}\boldsymbol{\beta})^\top(\mathbf{y}-\mathbf{X}\boldsymbol{\beta}).$$
2. 展开：

   $$S=\mathbf{y}^\top\mathbf{y}-2\boldsymbol{\beta}^\top\mathbf{X}^\top\mathbf{y}+\boldsymbol{\beta}^\top\mathbf{X}^\top\mathbf{X}\boldsymbol{\beta}.$$
3. 关于 $\boldsymbol{\beta}$ 取梯度并置零：

   $$\nabla_{\boldsymbol\beta}S=-2\mathbf{X}^\top\mathbf{y}+2\mathbf{X}^\top\mathbf{X}\boldsymbol{\beta}=\mathbf{0}.$$
4. 整理成正规方程并求解：

   $$\mathbf{X}^\top\mathbf{X}\,\hat{\boldsymbol\beta}=\mathbf{X}^\top\mathbf{y}\;\Rightarrow\;\hat{\boldsymbol\beta}=(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}.$$
5. Hessian $2\mathbf{X}^\top\mathbf{X}$ 是半正定的（满秩时正定），故这是全局极小值。

*与第 1 节相同的"把导数置零"手法——现在是向量形式，同时解出每个系数。*

**帽子矩阵**

$$\hat{\mathbf{y}}=\mathbf{X}\hat{\boldsymbol\beta}=\underbrace{\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top}_{\mathbf{H}}\,\mathbf{y}=\mathbf{H}\mathbf{y}$$

*$\mathbf{H}$ "给 $\mathbf{y}$ 戴上帽子"。它的对角元 $h_{ii}$ 是**杠杆值**——每个观测把自己的拟合值拉动多少。残差为 $\mathbf{e}=(\mathbf{I}-\mathbf{H})\mathbf{y}$。*

**演示 —— $\mathbf{H}$ 是一个投影（对称且幂等）**

1. 对称：由于 $(\mathbf{X}^\top\mathbf{X})^{-1}$ 对称，

   $$\mathbf{H}^\top=\big(\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\big)^\top=\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top=\mathbf{H}.$$
2. 幂等：内部的 $\mathbf{X}^\top\mathbf{X}$ 与其逆抵消，

   $$\mathbf{H}^2=\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\underbrace{\mathbf{X}^\top\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}}_{=\,\mathbf{I}}\mathbf{X}^\top=\mathbf{H}.$$
3. 一个对称幂等矩阵恰好是一个正交投影——这里投影到 $\mathbf{X}$ 的列空间上。故 $\hat{\mathbf{y}}$ 是该子空间中最接近 $\mathbf{y}$ 的点。
4. 残差 $\mathbf{e}=(\mathbf{I}-\mathbf{H})\mathbf{y}$ 正交于列空间：$\mathbf{X}^\top\mathbf{e}=\mathbf{0}$ ——恰好是正规方程的重新表述。

*最小二乘 = 从 $\mathbf{y}$ 向预测变量张成的空间作垂线。SST=SSR+SSE 是这个直角三角形的勾股定理。*

**估计量的协方差**

$$\operatorname{Cov}(\hat{\boldsymbol\beta})=\sigma^2(\mathbf{X}^\top\mathbf{X})^{-1}$$

*标准误是它对角线的平方根。几何意义：$\mathbf{X}$ 携带很少变异的那些方向（$\mathbf{X}^\top\mathbf{X}$ 的小特征值）给出大的系数方差——多重共线性的萌芽。*

> **联系 —— 来自线性代数的投影与特征值**
>
> $\mathbf{H}$ 是投影矩阵；$\operatorname{trace}(\mathbf{H})=p$ 等于模型自由度（它计数列空间的维数）。$\mathbf{X}^\top\mathbf{X}$ 的特征值同时决定逆的稳定性和 $\hat{\boldsymbol\beta}$ 的方差——正是线性代数里的特征值/条件数思想。

<a id="s7"></a>
### 推断、多重共线性与模型选择

*检验个别系数，诊断预测变量何时彼此打架，并选择保留哪些。*

**单个系数的 t 检验**

$$t_j = \frac{\hat\beta_j}{\operatorname{SE}(\hat\beta_j)},\qquad \operatorname{SE}(\hat\beta_j)=s\sqrt{[(\mathbf{X}^\top\mathbf{X})^{-1}]_{jj}}$$

*在 $H_0:\beta_j=0$ 下分布为 $t_{n-p}$。它检验 $x_j$ 的贡献*在所有其他预测变量都在模型中的前提下*——是偏效应，而非边际效应。*

> **概念 —— 多重共线性**
>
> 当预测变量高度相关时，$\mathbf{X}^\top\mathbf{X}$ 近乎奇异（特征值微小），故 $(\mathbf{X}^\top\mathbf{X})^{-1}$ 有巨大的元素，系数标准误爆炸。症状：整体 $F$ 显著但没有显著的个别 $t$；系数带有"错误"的符号，并在加入或删除一个预测变量时剧烈摇摆。它损害的是*解释和稳定性*，不一定是预测。

**方差膨胀因子**

$$\operatorname{VIF}_j=\frac{1}{1-R_j^2}$$

*其中 $R_j^2$ 来自把 $x_j$ 对所有其他预测变量回归。$\operatorname{VIF}_j>5$–$10$ 标示出有问题的共线性：$\hat\beta_j$ 的方差相比正交设计被膨胀了那个因子。*

| 准则 | 公式 / 思想 | 它奖励什么 |
| --- | --- | --- |
| 调整 $R^2$ | $1-\dfrac{\text{SSE}/(n-p)}{\text{SST}/(n-1)}$ | 拟合，对额外参数加以惩罚 |
| AIC | $2p-2\ln\hat L$ | 预测拟合，轻惩罚 |
| BIC | $p\ln n-2\ln\hat L$ | 简约，更重的惩罚（随 $n$ 增长） |
| Mallows $C_p$ | $\dfrac{\text{SSE}_p}{\hat\sigma^2}-n+2p$ | 用少量预测变量得到低偏差 |
| 交叉验证 | 留出的预测误差 | 诚实的样本外精度 |

> **原理 —— 选择是偏差–方差的折中**
>
> 加入预测变量总是降低训练 SSE，但最终会因拟合噪声而抬高*测试*误差。上面每个准则都在拟合与复杂度之间权衡；它们的区别在于惩罚有多陡。逐步选择虽方便却乐观（它使通常的 p 值失效）；交叉验证和正则化（第 12 节）是现代默认做法。

> **联系 —— 通向极大似然与信息准则**
>
> AIC 和 BIC 由极大化的**对数似然** $\ln\hat L$ 建立——与《推断》指南相同的极大似然机制。在正态误差下，极大化似然就是最小化 SSE，故最小二乘和极大似然一致，而这些准则只是给对数似然加上一笔复杂度税。

<a id="s8"></a>
### 方差分析与 F 检验

*对整个模型的一个检验：这一组预测变量合在一起，是否比什么都不用更好？*

**整体 F 检验**

$$F=\frac{\text{SSR}/(p-1)}{\text{SSE}/(n-p)}=\frac{\text{MSR}}{\text{MSE}}$$

*在 $H_0:\beta_1=\cdots=\beta_{p-1}=0$（所有斜率为零）下，$F\sim F_{p-1,\,n-p}$。一个大的 $F$ 说明模型每个参数解释的方差远多于剩余的噪声——至少有一个预测变量要紧。*

| 来源 | 平方和 | 自由度 | 均方 | F |
| --- | --- | --- | --- | --- |
| 回归 | $\text{SSR}=\sum(\hat y_i-\bar y)^2$ | $p-1$ | $\text{MSR}=\text{SSR}/(p-1)$ | $\text{MSR}/\text{MSE}$ |
| 误差 | $\text{SSE}=\sum(y_i-\hat y_i)^2$ | $n-p$ | $\text{MSE}=\text{SSE}/(n-p)$ |   |
| 总计 | $\text{SST}=\sum(y_i-\bar y)^2$ | $n-1$ |   |   |

**演示 —— 构建 F 比**

1. 划分变异：$\text{SST}=\text{SSR}+\text{SSE}$，并相应地划分自由度：$(n-1)=(p-1)+(n-p)$。
2. 在 $H_0$ 下，每个平方和除以 $\sigma^2$ 是一个独立的卡方：$\text{SSR}/\sigma^2\sim\chi^2_{p-1}$ 且 $\text{SSE}/\sigma^2\sim\chi^2_{n-p}$（它们的独立性源自 $\mathbf{H}$ 与 $\mathbf{I}-\mathbf{H}$ 的正交性）。
3. 一个 $F$ 随机变量是两个独立卡方各除以其自由度之比：

   $$F=\frac{(\text{SSR}/\sigma^2)/(p-1)}{(\text{SSE}/\sigma^2)/(n-p)}=\frac{\text{MSR}}{\text{MSE}}\sim F_{p-1,\,n-p}.$$
4. $\sigma^2$ 抵消——所以我们从不需要知道它。在 $H_0$ 下，$E[\text{MSR}]=E[\text{MSE}]=\sigma^2$，故 $F\approx 1$；一个真实信号把 $\text{MSR}$ 推到 $\text{MSE}$ 之上。

*在简单回归中整体 $F$ 等于单个斜率的 $t^2$ ——两个检验重合。*

> **概念 —— 偏（嵌套）F 检验**
>
> 要检验系数的一个*子集*，把全模型与一个简化模型比较：$F=\dfrac{(\text{SSE}_{\text{red}}-\text{SSE}_{\text{full}})/q}{\text{SSE}_{\text{full}}/(n-p)}$，其中删去了 $q$ 个系数。这个"额外平方和"$F$ 是比较嵌套模型背后的发动机，也是带多个水平的类别变量如何作为一整块被检验的方式。

> **联系 —— 同样的方差分析，同样的 F，与《统计学》指南相同**
>
> 入门指南的单因素方差分析（"组间方差比组内方差"）是这个回归方差分析的一个特例，以组成员身份虚拟变量作为预测变量。同样的 $F$ 分布，同样来自《概率论》和《推断》指南的卡方比值逻辑。

<a id="s9"></a>
### 类别预测变量、交互与变换

*如何把类别、曲率和条件效应喂进一个仍然"线性"的模型。*

**虚拟（指示）编码**

$$x_{\text{group B}}=\begin{cases}1 & \text{if obs is in group B}\\ 0 & \text{otherwise}\end{cases}$$

*一个 $k$ 水平的类别需要 $k-1$ 个虚拟变量；被省略的水平是**基准**。把全部 $k$ 个加上截距一并放入会使 $\mathbf{X}$ 秩亏——即"虚拟变量陷阱"（与截距列完全共线）。*

> **概念 —— 一个虚拟变量系数意味着什么**
>
> 在 $y=\beta_0+\beta_1 D$ 中，系数 $\beta_1$ 是该组与基准之间平均 $y$ 的差。当同时有一个数值预测变量时，一个虚拟变量平移**截距**（平行直线，不同高度）。要让*斜率*随组而异，你需要一个交互项。

**交互项**

$$y=\beta_0+\beta_1 x+\beta_2 D+\beta_3\,(x\cdot D)+\varepsilon$$

*当 $D=0$ 时 $x$ 的斜率是 $\beta_1$；当 $D=1$ 时它是 $\beta_1+\beta_3$。交互项 $\beta_3$ 度量 $x$ 的效应如何**取决于** $D$ ——非平行直线。两个数值预测变量之间的交互以同样方式运作：$\beta_3\,x_1 x_2$。*

## C 部分 · 广义模型及其超越

<a id="s10"></a>
### 逻辑回归

*当响应是一个是/否结果时，一条直线就崩溃了。logit 联系把它修好。*

> **概念 —— 为什么不直接对 0/1 数据拟合一条直线？**
>
> 对二元 $y$ 作线性回归可能预测出低于 0 或高于 1 的概率，而它的误差既非正态也非同方差。我们转而对**概率** $p=P(y=1\mid\mathbf{x})$ 建模，并让它通过一个把整条实轴映射到 $(0,1)$ 的函数——逻辑（sigmoid）曲线。

**逻辑模型与 logit 联系**

$$p(\mathbf{x})=\frac{1}{1+e^{-\boldsymbol{\beta}^\top\mathbf{x}}},\qquad \operatorname{logit}(p)=\ln\frac{p}{1-p}=\boldsymbol{\beta}^\top\mathbf{x}$$

*这些**对数优势**关于预测变量是线性的。所以 $e^{\beta_j}$ 是一个**优势比**：$x_j$ 每增加一个单位，$y=1$ 的优势的乘性变化。*

**演示 —— 对数似然及其得分方程**

1. 每个 $y_i$ 是成功概率为 $p_i=p(\mathbf{x}_i)$ 的伯努利变量，故似然为

   $$L(\boldsymbol\beta)=\prod_{i=1}^n p_i^{\,y_i}(1-p_i)^{1-y_i}.$$
2. 取对数得到对数似然：

   $$\ell(\boldsymbol\beta)=\sum_{i=1}^n\Big[y_i\ln p_i+(1-y_i)\ln(1-p_i)\Big].$$
3. 代入 $\operatorname{logit}(p_i)=\boldsymbol\beta^\top\mathbf{x}_i$ 并求导，得到优雅的得分方程：

   $$\frac{\partial\ell}{\partial\boldsymbol\beta}=\sum_{i=1}^n\big(y_i-p_i\big)\mathbf{x}_i=\mathbf{X}^\top(\mathbf{y}-\mathbf{p})=\mathbf{0}.$$
4. 这些关于 $\boldsymbol\beta$ 是非线性的（因为 $p_i$ 依赖于 $\boldsymbol\beta$）——无闭式解。用 Newton–Raphson 迭代求解，又称迭代重加权最小二乘（IRLS）。

*注意残差 $(y_i-p_i)$ 正交于预测变量——与普通最小二乘相同的正交性，现在用于似然。*

> **原理 —— 用优势比与偏差作解释**
>
> 系数住在对数优势尺度上，故把 $e^{\beta_j}$ 报告为一个优势比。拟合优度使用**偏差** $-2\ell$（广义线性模型中 SSE 的类比）；嵌套模型用**似然比检验** $\Delta\text{deviance}\sim\chi^2$ 比较。分类质量用 ROC 曲线 / AUC 评判，而非 $R^2$。

> **联系 —— 通向极大似然与伯努利**
>
> 逻辑回归是《概率论》指南中伯努利分布的极大似然，其参数由一个线性预测器掌舵。似然比检验复用《推断》指南的渐近 $\chi^2$ 理论。线性回归是正态的极大似然；这里是伯努利的极大似然——同样的原理，不同的分布。

<a id="s11"></a>
### 广义线性模型（GLM）

*线性回归和逻辑回归是同一个家族的两个成员。广义线性模型为这个模式命名。*

> **概念 —— 广义线性模型的三种成分**
>
> 每个广义线性模型都有 (1) 一个**随机成分** —— 来自指数族的响应分布（正态、伯努利、泊松、伽马……）；(2) 一个**系统成分** —— 一个线性预测器 $\eta=\boldsymbol\beta^\top\mathbf{x}$；以及 (3) 一个**联系函数** $g$，通过 $g(E[y])=\eta$ 把它们连起来。选定分布和联系就挑出了模型。

**广义线性模型模板**

$$g\big(E[y\mid\mathbf{x}]\big)=\boldsymbol\beta^\top\mathbf{x},\qquad y\mid\mathbf{x}\sim \text{exponential family}$$

*线性回归是带正态响应和恒等联系的广义线性模型；逻辑回归是带 logit 联系的伯努利；泊松回归是带对数联系的计数。*

| 模型 | 响应分布 | 联系 $g(\mu)$ | 逆（均值） |
| --- | --- | --- | --- |
| 线性回归 | 正态 | 恒等：$\mu$ | $\eta$ |
| 逻辑回归 | 伯努利 / 二项 | logit：$\ln\frac{\mu}{1-\mu}$ | $\frac{1}{1+e^{-\eta}}$ |
| Probit 回归 | 伯努利 | probit：$\Phi^{-1}(\mu)$ | $\Phi(\eta)$ |
| 泊松回归 | 泊松 | 对数：$\ln\mu$ | $e^{\eta}$ |
| 伽马回归 | 伽马 | 倒数：$1/\mu$ | $1/\eta$ |

> **原理 —— 典范联系与统一拟合**
>
> 每个指数族分布都有一个自然的**典范联系**（伯努利的 logit、泊松的对数、正态的恒等），它使数学最干净，且使得分方程取形式 $\mathbf{X}^\top(\mathbf{y}-\boldsymbol\mu)=\mathbf{0}$。所有广义线性模型都由同一个算法——**IRLS**——拟合，并用偏差和似然比检验比较。一个框架，多种响应类型。

> **联系 —— 指数族把《概率论》绑到一起**
>
> 《概率论》指南的正态、伯努利、泊松和伽马都是指数族成员；广义线性模型是处理每一个的单一回归框架。联系函数推广了第 10 节的 logit，而恒等联系恢复 A/B 部分的普通最小二乘。

<a id="s12"></a>
### 正则化：岭回归、套索与偏差–方差权衡

*当预测变量众多或共线时，朴素的普通最小二乘会过拟合。收缩系数以一点点偏差换取少得多的方差。*

**岭回归（L2 惩罚）**

$$\hat{\boldsymbol\beta}_{\text{ridge}}=\arg\min_{\boldsymbol\beta}\;\|\mathbf{y}-\mathbf{X}\boldsymbol\beta\|^2+\lambda\|\boldsymbol\beta\|_2^2$$

$$\hat{\boldsymbol\beta}_{\text{ridge}}=(\mathbf{X}^\top\mathbf{X}+\lambda\mathbf{I})^{-1}\mathbf{X}^\top\mathbf{y}$$

*惩罚 $\lambda\ge 0$ 把系数向零收缩。它有闭式解——而且带有一个优美的副作用。*

**演示 —— 岭回归的闭式解，及它为何总能求逆**

1. 目标是 $S(\boldsymbol\beta)=(\mathbf{y}-\mathbf{X}\boldsymbol\beta)^\top(\mathbf{y}-\mathbf{X}\boldsymbol\beta)+\lambda\boldsymbol\beta^\top\boldsymbol\beta$。
2. 把梯度置零：

   $$\nabla S=-2\mathbf{X}^\top\mathbf{y}+2\mathbf{X}^\top\mathbf{X}\boldsymbol\beta+2\lambda\boldsymbol\beta=\mathbf{0}.$$
3. 归并项并求解：

   $$(\mathbf{X}^\top\mathbf{X}+\lambda\mathbf{I})\,\hat{\boldsymbol\beta}=\mathbf{X}^\top\mathbf{y}\;\Rightarrow\;\hat{\boldsymbol\beta}_{\text{ridge}}=(\mathbf{X}^\top\mathbf{X}+\lambda\mathbf{I})^{-1}\mathbf{X}^\top\mathbf{y}.$$
4. 加上 $\lambda\mathbf{I}$ 把 $\mathbf{X}^\top\mathbf{X}$ 的每个特征值抬高 $\lambda>0$，故矩阵总是可逆的——岭回归甚至在 $p>n$ 或预测变量共线（普通最小二乘彻底失败之处）时也能用。

*岭回归是带有数值稳定、条件数更好的正规方程矩阵的普通最小二乘——共线性的解药。*

**套索（L1 惩罚）**

$$\hat{\boldsymbol\beta}_{\text{lasso}}=\arg\min_{\boldsymbol\beta}\;\|\mathbf{y}-\mathbf{X}\boldsymbol\beta\|^2+\lambda\|\boldsymbol\beta\|_1$$

*L1 范数 $\sum|\beta_j|$ 在各坐标轴上有尖角，故解常常恰好落在 $\beta_j=0$ 处——套索做**自动变量选择**。无闭式解；由坐标下降或 LARS 求解。**弹性网**融合两种惩罚。*

> **原理 —— 偏差–方差权衡**
>
> 期望预测误差分解为 $\text{error}=\text{bias}^2+\text{variance}+\sigma^2_{\text{irreducible}}$。普通最小二乘无偏，但在预测变量众多/共线时方差可能巨大。正则化故意*加入偏差*（收缩系数）以*更多地削减方差*，从而降低总误差。惩罚 $\lambda$ 由交叉验证调节，沿这条曲线拨动位置。

> **联系 —— 特征值、Gauss–Markov 与贝叶斯**
>
> Gauss–Markov 说普通最小二乘是*无偏估计量中*最优的；岭回归通过允许偏差而逃出这一限制，因此能在均方误差上胜过普通最小二乘。$\lambda\mathbf{I}$ 项直接抬高 $\mathbf{X}^\top\mathbf{X}$ 的小特征值——线性代数中的条件数修正。而岭回归恰好是在 $\boldsymbol\beta$ 上用正态先验时的**贝叶斯**后验众数（套索在拉普拉斯先验下）——这是早先指南的贝叶斯/贝叶斯定理线索。

<a id="s13"></a>
### 越界一瞥：混合模型、时间序列与非参数回归

*在普通回归的假设崩溃之处，三大扩展接管。*

**混合效应模型 —— 当独立性失效时**

$$\mathbf{y}=\mathbf{X}\boldsymbol\beta+\mathbf{Z}\mathbf{b}+\boldsymbol\varepsilon,\qquad \mathbf{b}\sim N(\mathbf{0},\mathbf{G})$$

*分组/聚类数据（学校内的学生、对一位患者的重复测量）违反独立性。**随机效应** $\mathbf{b}$ 对组级偏离建模；$\boldsymbol\beta$ 是总体**固定效应**。由 REML/极大似然拟合。*

**时间序列 —— 当误差自相关时**

*当观测按时间排序时，误差是相关的，破坏 Gauss–Markov。诸如 **AR($p$)**、**MA($q$)** 和 **ARIMA** 之类的模型把一个序列对它自己的过去回归；广义最小二乘和 Durbin–Watson 统计量处理自相关残差。预测把"保持其他固定"替换为"外推动态"。*

**非参数回归 —— 当形式未知时**

$$y_i=f(x_i)+\varepsilon_i,\qquad f\ \text{flexible, not a fixed formula}$$

***样条**、**LOESS**、**核平滑**和**广义可加模型（GAM）**让数据自行决定曲线。**回归树**、**随机森林**和**梯度提升**进一步推入机器学习。一个平滑参数在同一条偏差–方差权衡上扮演 $\lambda$ 的角色。*

> **原理 —— 一个"损失—拟合"思想，不断推广**
>
> 本指南中的每个模型都是同一个三步故事：**设定**一个结构（直线、平面、联系、灵活曲线），通过优化一个损失或似然来**拟合**它（把梯度置零——微积分），并用诚实的、样本外的不确定性来**评估**它。这套数学从单条直线一直扩展到深度学习，骨架不变。

> **联系 —— 整条弧线**
>
> 相关（《统计学》）→ 作为微积分优化的最小二乘 → 投影与特征值（线性代数）→ t/F 抽样分布与极大似然（《推断》）→ 指数族上的广义线性模型（《概率论》）→ 作为贝叶斯先验的正则化。回归是每一门早先学科汇聚成一件实用工具之处。

---

*一份完整的回归与线性模型伴读——从穿过散点图的最佳直线到广义线性模型、正则化，以及混合模型与机器学习的前沿。每个核心结果都被演示，并系回微积分（优化）、线性代数（投影、特征值），以及那些使不确定性诚实的概率与推断。读一遍以把握形状；把任何方框当作参考随时回看。记住骨架：设定一个结构，通过最小化一个损失来拟合，用诚实的不确定性来评估。*
