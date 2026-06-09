[English](inference.md) · **中文**

# 推断，*从数据到真相。*

一门严谨的数理统计课程——讲述如何把一个随机样本转化为对未知参数的估计、区间、检验与后验信念。每条原理都以精确的定义给出，每个关键定理都被**演示**，并明确揭示其与概率论和微积分的脉络联系。这一扩展版假设读者**没有任何先修数学背景**：每个符号在首次出现时都以文字定义，每个推导都是一个编号列表，其中每一步都说明*做了什么*以及*为什么允许这样做*，每个结论之后都跟有一个完整演算的数值例子。

[← 返回全部指南](../README.zh.md)

## A 部分 · 基础

<a id="s0"></a>
### 全局图景：从数据到结论

*概率论描述一个已知的机制如何产生随机数据。推断则把箭头反转过来：给定数据，机制是什么？*

#### 这一节讲的是什么，用大白话说

设想一家冲压硬币的工厂。你不知道这些硬币是否均匀。你把一枚硬币抛 100 次，看到 58 次正面。“这枚硬币正面朝上的真实概率是多少？”这一问题就是一个**统计推断**问题：你有*数据*（100 次中有 58 次正面），你想恢复一个*关于机制的事实*（正面朝上的真实概率）。概率论会朝相反方向走——它会从“硬币以概率 0.5 落为正面”出发，预测你大概会看到多少次正面。推断把这一推理反过来运行。

#### 定义我们将要用到的每一个术语

- **数据。** 我们实际观测到的数字。记作 $x_1, x_2, \dots, x_n$ ，其中 $n$ 是**样本量**（我们有多少个观测）。小写字母表示我们看到的具体数字。
- **随机变量。** 在我们查看之前，其取值由一个随机实验决定的量。我们用大写字母记随机变量： $X_1, X_2, \dots, X_n$ 。一旦实验完成， $X_i$ 就“变成”观测到的数字 $x_i$ 。
- **参数。** 描述机制的一个未知的固定数（或一组数）。我们记作 $\theta$ （希腊字母“theta”）。在硬币例子中， $\theta$ 是正面朝上的真实概率。
- **参数空间。** $\theta$ 被允许取的所有值组成的集合，记作 $\Theta$ （大写 theta）。对一个硬币概率， $\Theta = [0,1]$ ，即从 $0$ 到 $1$ 的数构成的区间。
- **概率密度（或质量）函数。** 一个函数 $f(x \mid \theta)$ ，它说明当参数等于 $\theta$ 时每个数据值 $x$ 的可能性有多大。竖线“ $\mid$ ”读作“给定”。对于离散数据（计数）它直接给出概率；对于连续数据它给出一个密度，其面积给出概率。（密度与质量的区分见概率论指南；这里我们对两者都笼统地称为“密度”。）
- **统计模型。** 候选分布的整个族，记作 $\{f(x\mid\theta): \theta\in\Theta\}$ 。花括号表示“……的集合”，冒号读作“使得”。所以这是“使 $\theta$ 取遍 $\Theta$ 的所有分布 $f(x\mid\theta)$ 构成的集合”。

在**数理统计**中我们假定这样一个统计模型。我们观测到从该族中某一（未知）成员抽取的数据 $X_1,\dots,X_n$ ，而我们的任务是说出 $\theta$ 是什么。有三类经典的交付物。

- **点估计** —— 对 $\theta$ 的单个最佳猜测 $\hat\theta$ （B 部分）。符号上方的“帽子” $\hat{\,}$ 永远表示“……的一个估计”。
- **区间估计与检验** —— 对 $\theta$ 给出一个带有声明置信度的取值范围，或对某一论断做出是/否的判定（C 部分）。
- **预测 / 信念更新** —— 而且在贝叶斯观点下，给出关于 $\theta$ 的一个完整概率分布，描述我们剩余的不确定性（D 部分）。

> **原理 —— 推断的反演**
>
> 概率论运行的是**参数 $\to$ 数据**：固定 $\theta$ ， $f(x\mid\theta)$ 告诉你数据如何表现。推断运行的是**数据 $\to$ 参数**：固定数据，问哪个 $\theta$ 是可信的。*似然函数*（第 3 节）正是从这一反方向去读的 $f(x\mid\theta)$ ，它是整个学科的枢纽。

#### 一个固定思路的微型演算例子

设模型为“每次抛掷以未知概率 $\theta$ 为正面”。我们抛 $n=3$ 次，观测到正面、反面、正面，即数据 $x_1=1, x_2=0, x_3=1$ （把正面编码为 $1$ ，反面编码为 $0$ ）。若真实值为 $\theta$ ，模型赋予这一确切序列的概率为

$$f(x_1,x_2,x_3\mid\theta)=\theta\cdot(1-\theta)\cdot\theta=\theta^2(1-\theta).$$

把它当作 $\theta$ 的函数来读（数据固定）就是推断的反方向。若 $\theta=0.5$ ，它给出 $0.125$ ；若 $\theta=0.7$ ，给出 $0.147$ ；若 $\theta=0.9$ ，给出 $0.081$ 。值 $\theta=0.7$ 使观测数据比 $0.5$ 或 $0.9$ 更可能，这已经暗示“最可能的” $\theta$ 落在三分之二附近——正是我们看到的正面比例。第 5 节将把这一点精确化。

#### 整门课程浓缩成一行

> 模型与似然 → 充分性 → 点估计量（矩法、MLE）→ 评价它们（偏差、MSE、Cramér–Rao、MVUE）→ 区间与检验（枢轴量、Neyman–Pearson、LRT）→ 贝叶斯与自助法

> **联系 —— 建立在入门统计指南之上**
>
> 入门指南从操作层面引入了 $\bar x$ 、 $s^2$ 、置信区间和 p 值。本指南提供其中的*为什么*：为什么除以 $n-1$ ，为什么会出现 $t$ ，为什么 $\bar X\pm 1.96\,\sigma/\sqrt n$ 是正确的，以及是什么使一个估计量“好”。它是配方背后的理论。

#### 常见误区

- 参数 $\theta$ 是**固定但未知的**，而非随机的（直到 D 部分，贝叶斯观点才刻意把它当作随机以编码信念）。A–C 部分中的随机性存在于*数据*中。
- 像 $\hat\theta=0.58$ 这样的“估计”是一个数字；而产生它的*规则*（第 1 节）才是我们真正研究的对象。

<a id="s1"></a>
### 总体、样本与抽样分布

*统计量是随机数据的函数，所以它本身也是一个随机变量。它的分布是每一项推断赖以建立的对象。*

#### 大白话定位

我们很少测量整个**总体**（工厂将造出的每一枚硬币）。相反，我们取一个**样本**——少数几个观测——并从中计算一个汇总数字，例如平均值。因为样本是随机的，这个汇总数字也是随机的：不同的样本会给出不同的平均值。这个汇总值在所有可能样本上取到的取值模式，就是它的**抽样分布**，理解这一模式正是使我们能为结论附上误差棒和置信度的东西。

#### 定义

- **总体。** 所有可能观测的完整集合，由真实分布 $F$ （或密度 $f$ ）描述。
- **样本。** 我们实际收集到的观测， $X_1,\dots,X_n$ 。
- **独立。** 两个随机变量独立，是指知道其中一个不会告诉你关于另一个的任何信息；形式上它们的联合密度可分解为各自密度的乘积。
- **同分布。** 所有 $X_i$ 都服从相同的分布 $f(x\mid\theta)$ 。

**随机样本（i.i.d.）**

$$X_1,\dots,X_n \ \text{i.i.d.}\ \sim f(x\mid\theta),\qquad \text{joint density } f(\mathbf x\mid\theta)=\prod_{i=1}^n f(x_i\mid\theta)$$

这里“ $\sim$ ”读作“服从……分布”。粗体 $\mathbf x=(x_1,\dots,x_n)$ 是整列数据。符号 $\prod_{i=1}^n$ 是对 $i=1,2,\dots,n$ 取**乘积**——它是求和号 $\sum$ 的乘法类比。所以 $\prod_{i=1}^n f(x_i\mid\theta)=f(x_1\mid\theta)\times f(x_2\mid\theta)\times\cdots\times f(x_n\mid\theta)$ 。

*“i.i.d.” = 独立同分布。独立性正是把联合密度变成单个乘积的东西——这一结构性事实驱动了似然、充分性以及中心极限定理。*

**为什么独立性给出乘积？** 根据独立性的定义，独立变量的联合密度等于它们各自密度的乘积。由于它们又是同分布的，每个个体密度都是*同一个*函数 $f(\cdot\mid\theta)$ ，只是在不同数据点处取值而已。把它们相乘就得到 $\prod_{i=1}^n f(x_i\mid\theta)$ 。

> **概念 —— 统计量 vs 估计量 vs 估计**
>
> **统计量** $T=T(X_1,\dots,X_n)$ 是样本的任意函数，且不依赖于未知的 $\theta$ （你必须能仅凭数据算出它）。**估计量**是用来猜测参数的统计量，例如 $\hat\theta=\bar X$ ；它是随机的。它在观测数据上的实现值，如 $\hat\theta=4.2$ ，是一个**估计**。估计量在所有可能样本上的分布是它的**抽样分布**。

这里 $\bar X$ （读作“X-bar”）表示**样本均值**，定义为 $\bar X = \frac1n\sum_{i=1}^n X_i$ ——把所有观测加起来再除以观测个数。

**样本均值的期望与方差**

$$E[\bar X]=\mu,\qquad \mathrm{Var}(\bar X)=\frac{\sigma^2}{n},\qquad \text{SE}(\bar X)=\frac{\sigma}{\sqrt n}$$

新符号： $E[\,\cdot\,]$ 是**期望值**（一个随机量的长期平均）； $\mu$ （希腊字母“mu”）是总体均值 $E[X]$ ； $\mathrm{Var}$ 是**方差**（到均值的平方距离的平均，衡量离散程度）； $\sigma^2$ （sigma 平方）是总体方差 $\mathrm{Var}(X)$ ； $\sigma$ 是**标准差**（方差的平方根）；SE 是**标准误**，即*估计量*的标准差。

**演示 —— $\bar X$ 的期望与方差，每一步都有依据**

1. 由定义 $\bar X=\frac1n\sum_{i=1}^n X_i$ 。
2. 应用**期望的线性性质**（和的期望等于期望的和，且常数因子可以提出）： $E[\bar X]=\frac1n\sum_{i=1}^n E[X_i]$ 。
3. 每个 $X_i$ 同分布，均值为 $\mu$ ，故对每个 $i$ 有 $E[X_i]=\mu$ 。把 $n$ 份 $\mu$ 加起来得 $\frac1n\cdot n\mu=\mu$ 。因此 $E[\bar X]=\mu$ 。
4. 对于方差，使用这条规则：对**独立**变量，和的方差等于方差之和，且常数因子 $c$ 以平方形式提出： $\mathrm{Var}(cY)=c^2\mathrm{Var}(Y)$ 。取 $c=\frac1n$ ，

   $$\mathrm{Var}(\bar X)=\mathrm{Var}\!\Big(\tfrac1n\sum_{i=1}^n X_i\Big)=\tfrac{1}{n^2}\sum_{i=1}^n \mathrm{Var}(X_i).$$
5. 每个 $\mathrm{Var}(X_i)=\sigma^2$ ，把 $n$ 份相加得 $\frac{1}{n^2}\cdot n\sigma^2=\frac{\sigma^2}{n}$ 。取平方根得到标准误 $\sigma/\sqrt n$ 。

*估计量 $\bar X$ 以真值为中心（ $E[\bar X]=\mu$ ），并随 $n$ 增大而变得更集中（方差以 $1/n$ 缩小）——这是相合性（第 6 节）的种子。*

**数值演算例子。** 设某总体均值 $\mu=10$ ，标准差 $\sigma=4$ 。取样本量 $n=16$ 。则 $E[\bar X]=10$ 且 $\mathrm{Var}(\bar X)=\frac{4^2}{16}=\frac{16}{16}=1$ ，故 $\text{SE}(\bar X)=\sqrt 1=1$ 。把样本量翻两番至 $n=64$ 将给出 $\text{SE}=4/\sqrt{64}=4/8=0.5$ ——要把误差减半，你必须把数据翻两番。

**演示 —— 正态样本下 $\bar X$ 的抽样分布**

1. 设 $X_i\ \text{i.i.d.}\ \sim N(\mu,\sigma^2)$ 。记号 $N(\mu,\sigma^2)$ 表示均值为 $\mu$ 、方差为 $\sigma^2$ 的**正态**（钟形曲线）分布。概率论中的一个标准事实是：独立正态变量的任意线性组合仍是正态的。由于 $\bar X$ 是一个线性组合（ $\frac1n$ 乘以一个和）， $\bar X$ 是正态的。
2. 它的均值与方差已在上面算出： $E[\bar X]=\mu$ ， $\mathrm{Var}(\bar X)=\sigma^2/n$ 。一个正态分布完全由其均值与方差决定，所以

   $$\bar X\sim N\!\left(\mu,\ \frac{\sigma^2}{n}\right),\qquad Z=\frac{\bar X-\mu}{\sigma/\sqrt n}\sim N(0,1).$$
3. 第 2 步中的变换，即减去均值再除以标准差，称为**标准化**；它把任意正态变为**标准正态** $N(0,1)$ （均值 $0$ ，方差 $1$ ）。我们验证： $E[Z]=\frac{E[\bar X]-\mu}{\sigma/\sqrt n}=0$ 且 $\mathrm{Var}(Z)=\frac{\mathrm{Var}(\bar X)}{\sigma^2/n}=1$ 。
4. 对于非正态总体，**中心极限定理（CLT）**给出相同的极限形式：当 $n\to\infty$ 时 $Z\xrightarrow{d}N(0,1)$ 。箭头 $\xrightarrow{d}$ 表示“依分布收敛”——对大 $n$ ，无论总体形状如何， $Z$ 的分布都近似为标准正态。

*对正态精确，一般情形下渐近成立——这一单个分布支撑起 C 部分的 $z$ 区间与 $t$ 区间。*

> **联系 —— 概率论指南（CLT 与 MGF）**
>
> 对正态数据 $\bar X$ 是正态的，否则渐近正态——这正是那里用矩母函数（MGF）证明的 CLT。抽样分布无非是随机变量的变换；概率论中 $E$ 、 $\mathrm{Var}$ 与 MGF 的代数运算就是工具箱。

#### 常见误区

- 标准*差* $\sigma$ 衡量总体中的离散程度；标准*误* $\sigma/\sqrt n$ 衡量估计量的离散程度。两者相差一个因子 $\sqrt n$ 。
- “ $\bar X$ 是正态的”只对正态数据*精确*成立；对其他总体它是一个近似，且随 $n$ 改善。

<a id="s2"></a>
### 统计量、充分性与因子分解定理

*某些统计量把数据中关于 $\theta$ 的每一滴信息都榨取出来。这些充分统计量让我们能在不损失任何信息的前提下压缩样本。*

#### 大白话定位

如果你抛一枚硬币 100 次，要估计硬币的偏向，你真的需要正反面的确切顺序吗？凭直觉是不需要的——只有正面的*总数*重要。**充分统计量**是这一直觉的精确版本：它是数据的一个汇总，保留了关于 $\theta$ 的全部信息，所以一旦你知道了它，数据中剩下的细节就是无关的噪声。

#### 定义

- **条件分布。** 在另一个量被固定时某一量的分布。“给定 $T=t$ 时数据的分布”描述了一旦被告知汇总值等于 $t$ 之后哪些数据模式仍然可能。
- 统计量 $T$ *不*依赖 $\theta$ ，所以仅凭数据即可算出（回顾第 1 节）。

> **概念 —— 充分性**
>
> 若给定 $T$ 时数据的条件分布不依赖于 $\theta$ ，则统计量 $T$ 对 $\theta$ 是**充分的**。直觉上：一旦你知道了 $T$ ，样本中其余部分就是不携带关于 $\theta$ 任何进一步信息的“噪声”。对正态样本， $(\sum X_i,\sum X_i^2)$ 是充分的——数据各点的具体顺序无关紧要。

**Fisher–Neyman 因子分解定理**

$$T \text{ is sufficient for }\theta \iff f(\mathbf x\mid\theta)=g\big(T(\mathbf x),\theta\big)\,h(\mathbf x)$$

符号“ $\iff$ ”表示“当且仅当”（两边的陈述等价）。定理说： $T$ 充分当且仅当联合密度恰好分裂为两个因子之积——一个因子 $g$ 涉及 $\theta$ ，但仅通过汇总量 $T(\mathbf x)$ 触及数据，乘以一个因子 $h(\mathbf x)$ ，后者涉及数据但完全不涉及 $\theta$ 。

*要找充分统计量，写出联合密度并分离出 $\theta$ 与数据相遇之处； $\theta$ 所“对话”的那个数据的函数就是充分统计量 $T$ 。*

**为什么因子分解蕴含充分性（带依据的直觉）。** 若密度可分解为 $g(T,\theta)h(\mathbf x)$ ，则对于具有*相同*$T$ 值的两个数据集，对 $\theta$ 的依赖（因子 $g$ ）是相同的；它们只通过 $h$ 不同，而 $h$ 不携带 $\theta$ 。用联合密度除以 $T$ 的密度以构造条件分布时，带 $\theta$ 的因子相消，留下不含 $\theta$ 的东西——这正是充分性的定义。

**演示 —— 通过因子分解得到伯努利 $p$ 的充分统计量**

一个 **伯努利($p$)** 随机变量以概率 $p$ 取 $1$ （“成功”），以概率 $1-p$ 取 $0$ （“失败”）。它的质量函数可紧凑地写成 $f(x\mid p)=p^x(1-p)^{1-x}$ ，其中 $x\in\{0,1\}$ ：代入 $x=1$ 得 $p$ ，代入 $x=0$ 得 $1-p$ 。

1. 对 $X_i\ \text{i.i.d.}\ \sim\text{Bernoulli}(p)$ ，把各个质量函数相乘（独立性，第 1 节）：

   $$f(\mathbf x\mid p)=\prod_{i=1}^n p^{x_i}(1-p)^{1-x_i}.$$
2. 用指数法则 $a^{b}a^{c}=a^{b+c}$ 合并幂次： $p$ 的因子给出 $p^{\sum x_i}$ ， $(1-p)$ 的因子给出 $(1-p)^{\sum(1-x_i)}=(1-p)^{n-\sum x_i}$ （因为 $\sum_{i=1}^n 1 = n$ ）。于是

   $$f(\mathbf x\mid p)=p^{\sum x_i}(1-p)^{\,n-\sum x_i}.$$
3. 这只通过 $T=\sum_{i=1}^n x_i$ （成功的总数）依赖于数据。令 $g(T,p)=p^{T}(1-p)^{n-T}$ 且 $h(\mathbf x)=1$ 。
4. 由因子分解定理， $T=\sum X_i$ （等价地 $\bar X=T/n$ ）对 $p$ 是充分的。

*知道成功的总数与知道 $0$ 和 $1$ 的完整序列一样好。*

**数值演算例子。** 当 $n=5$ 次抛掷且数据为 $1,0,1,1,0$ 时， $T=\sum x_i=3$ 。因子分解告诉我们：*任何*其他含三次正面的序列——比如 $1,1,1,0,0$ ——携带关于 $p$ 的完全相同的信息。两者都给出密度 $p^3(1-p)^2$ 。

> **原理 —— 极小充分性与完备性**
>
> **极小**充分统计量是最粗的充分汇总——它是每个其他充分统计量的函数，因此在不损失信息的前提下尽可能多地压缩。若使 $E_\theta[\varphi(T)]=0$ 对所有 $\theta$ 成立的唯一函数 $\varphi$ 是处处为零的函数，则统计量 $T$ 是**完备的**。完备性是使 Rao–Blackwell 估计量（第 8 节）成为*唯一*最优者的技术要素：它禁止存在两个不同的、 $T$ 的无偏函数。

> **联系 —— 指数族**
>
> 许多分布（正态、伯努利、泊松、指数、伽马）属于**指数族** $f(x\mid\theta)=h(x)\exp\{\eta(\theta)T(x)-A(\theta)\}$ ，其中 $\exp\{\cdot\}$ 是指数函数 $e^{(\cdot)}$ 。这时因子分解是立即可得的（ $\exp\{\eta(\theta)\sum T(x_i)\}$ 那块是 $g$ ， $\prod h(x_i)$ 是 $h$ ），而 $\sum T(X_i)$ 自动是一个完备充分统计量——这是贯穿估计理论的一条统一脉络。

#### 常见误区

- 充分统计量是*针对某个特定模型*而言的充分。总和 $\sum X_i$ 对伯努利 $p$ 充分，但对于一个结果顺序重要的模型，它就不会捕获到全部信息。

<a id="s3"></a>
### 似然函数

*把联合密度反过来：把数据当作固定，把 $\theta$ 当作变量。这一重新解读就是似然，而几乎一切都由它推出。*

#### 大白话定位

在我们收集数据之前，联合密度 $f(\mathbf x\mid\theta)$ 是数据在已知 $\theta$ 下如何表现的配方。在我们收集数据之后，数字 $\mathbf x$ 被冻结，只有 $\theta$ 未知。**似然**就是这同一个公式，现在被看作 $\theta$ 的函数。它回答：“对于每个候选 $\theta$ ，它对我实际看到的数据解释得有多好？”

**似然与对数似然**

$$L(\theta)=f(\mathbf x\mid\theta)=\prod_{i=1}^n f(x_i\mid\theta),\qquad \ell(\theta)=\log L(\theta)=\sum_{i=1}^n \log f(x_i\mid\theta)$$

新符号： $L(\theta)$ 是**似然**； $\ell(\theta)$ （花体 ell）是**对数似然**，即 $L$ 的自然对数。自然对数 $\log$ （底为 $e\approx 2.718$ ）是指数函数的逆。我们使用关键的对数律 $\log(ab)=\log a+\log b$ ：乘积的对数是对数之和。正是这条律使 $L$ 中的乘积在 $\ell$ 中变为*和*，从而远更易于求导。

*$L(\theta)$ **不是**关于 $\theta$ 的概率分布；它不必积分为一。它只是按各 $\theta$ 值对观测数据解释得有多好来*排序*它们。*

> **原理 —— 似然原理**
>
> 数据携带的关于 $\theta$ 的全部信息都包含在似然函数中。两个产生成比例似然（其一是另一的常数倍）的实验，应当导致关于 $\theta$ 的相同推断。取对数把乘积变为和，这就是为什么**得分函数** $\ell'(\theta)$ 与 Fisher 信息（第 7 节）在独立观测上是可加的。

**得分函数**

$$U(\theta)=\frac{\partial}{\partial\theta}\ell(\theta)=\sum_{i=1}^n \frac{\partial}{\partial\theta}\log f(x_i\mid\theta),\qquad E_\theta[U(\theta)]=0$$

新符号： $\frac{\partial}{\partial\theta}$ 是关于 $\theta$ 的**偏导数**——函数随 $\theta$ 变化的变化率（当只有一个变量时它就是普通导数）。 $U(\theta)$ 是**得分**：对数似然的斜率。 $E_\theta$ 上的下标提醒我们这个平均是假设 $\theta$ 为真值时取的。

*在真值 $\theta$ 处得分的均值为零。把得分置零就定位了似然的一个峰——纯粹的微积分优化。*

**演示 —— 得分的期望为零**

1. 从密度积分为一这一事实出发：对**每个** $\theta$ 有 $\int f(x\mid\theta)\,dx=1$ 。（积分号 $\int\cdots dx$ 表示“曲线下的总面积”，对一个概率密度它总是 $1$ 。）
2. 对 $\theta$ 求两边的导数。右边是常数 $1$ ，其导数为 $0$ 。在左边，一个**正则性条件**（ $f$ 的光滑性，它允许我们交换求导与积分的次序）允许把导数移到积分号内：

   $$\int \frac{\partial}{\partial\theta} f(x\mid\theta)\,dx=0.$$
3. 使用**对数导数恒等式** $\frac{\partial}{\partial\theta}\log f = \frac{1}{f}\frac{\partial}{\partial\theta} f$ ，它由 $\log$ 的链式法则得出。整理后它表明 $\frac{\partial}{\partial\theta} f = f\cdot\frac{\partial}{\partial\theta}\log f$ 。代入第 2 步：

   $$\int \Big(\frac{\partial}{\partial\theta}\log f(x\mid\theta)\Big) f(x\mid\theta)\,dx=0.$$
4. 由期望的定义， $\int g(x) f(x\mid\theta)\,dx = E_\theta[g(X)]$ 。取 $g=\frac{\partial}{\partial\theta}\log f$ ，左边正好是 $E_\theta\!\big[\frac{\partial}{\partial\theta}\log f(X\mid\theta)\big]=E_\theta[U(\theta)]$ 。因此 $E_\theta[U(\theta)]=0$ 。

*这条小引理是 MLE 相合性与 Cramér–Rao 界两者背后的主力。*

**数值演算例子（伯努利得分）。** 对单个伯努利观测， $\log f(x\mid p)=x\log p+(1-x)\log(1-p)$ 。对 $p$ 求导得到得分 $\frac{\partial}{\partial p}\log f=\frac{x}{p}-\frac{1-x}{1-p}$ 。通过对 $X$ 取平均来验证均值为零的断言（ $X$ 以概率 $p$ 为 $1$ ，以概率 $1-p$ 为 $0$ ）：

$$E_p\Big[\tfrac{X}{p}-\tfrac{1-X}{1-p}\Big]=\frac{p}{p}-\frac{1-p}{1-p}=1-1=0.\ \checkmark$$

> **联系 —— 微积分：优化就是把得分置零**
>
> 最大化 $\ell(\theta)$ 是微积分问题“找临界点”：解 $\ell'(\theta)=0$ 并检验二阶导数为负， $\ell''(\theta)\lt 0$ ，确认是峰而非谷。负的二阶导数 $-\ell''$ 衡量似然峰有多陡——而这个曲率*就是*观测到的 Fisher 信息（第 7 节）。

## B 部分 · 点估计

<a id="s4"></a>
### 矩法

*最古老的估计量配方：把模型的理论矩与数据的经验矩相匹配，然后求解。*

#### 大白话定位

**矩**是数据某个幂的平均。一阶矩就是均值；二阶矩是平方的平均；以此类推。模型把这些平均预测为关于 $\theta$ 的公式。**矩法**简单地说：把模型预测的平均设为你实际测得的平均，然后解出 $\theta$ 。它是可以想象到的最直接的估计量。

#### 定义

- **理论（总体） $k$ 阶矩：** $\mu_k(\theta)=E_\theta[X^k]$ ，即第 $k$ 个幂的期望值，由模型算出。
- **经验（样本） $k$ 阶矩：** $m_k=\frac1n\sum_{i=1}^n X_i^k$ ，即数据第 $k$ 个幂的平均。

**矩法（MoM）**

$$\text{set } \mu_k(\theta)=E_\theta[X^k] \ \text{equal to}\ m_k=\frac1n\sum_{i=1}^n X_i^k,\quad k=1,2,\dots$$

*用与未知参数个数相同数目的矩方程，然后解出 $\theta$ 。简单、随时可用，但极少最优。*

**演示 —— 泊松、伯努利与正态的矩法估计量**

1. **泊松($\lambda$)。** 泊松分布对稀有事件计数，并具有性质 $E[X]=\lambda$ （它唯一的参数也是其均值）。把第一理论矩 $\lambda$ 与第一经验矩 $\bar X$ 相匹配给出一个方程 $\lambda=\bar X$ ，故 $\hat\lambda_{\text{MoM}}=\bar X$ 。
2. **伯努利($p$)。** 此处 $E[X]=p$ 。与 $\bar X$ 匹配给出 $\hat p_{\text{MoM}}=\bar X$ ——成功的样本比例。
3. **正态($\mu,\sigma^2$)。** 两个未知量，所以我们需要两个方程。第一矩 $E[X]=\mu$ 与 $\bar X$ 匹配给出 $\hat\mu=\bar X$ 。第二矩是 $E[X^2]=\mathrm{Var}(X)+(E[X])^2=\sigma^2+\mu^2$ （使用恒等式 $\mathrm{Var}(X)=E[X^2]-(E[X])^2$ 整理而得）。把它与 $\frac1n\sum X_i^2$ 匹配：

   $$\sigma^2+\mu^2=\frac1n\sum_{i=1}^n X_i^2 \ \Rightarrow\ \hat\sigma^2_{\text{MoM}}=\frac1n\sum_{i=1}^n X_i^2-\hat\mu^2=\frac1n\sum_{i=1}^n X_i^2-\bar X^2.$$
4. 最后，代数恒等式 $\frac1n\sum X_i^2-\bar X^2=\frac1n\sum (X_i-\bar X)^2$ （展开右边即可证明： $\frac1n\sum(X_i^2-2X_i\bar X+\bar X^2)=\frac1n\sum X_i^2-2\bar X\cdot\bar X+\bar X^2=\frac1n\sum X_i^2-\bar X^2$ ）让我们可以写成

   $$\hat\sigma^2_{\text{MoM}}=\frac1n\sum_{i=1}^n (X_i-\bar X)^2.$$

*注意除数是 $n$ ，而非 $n-1$ ：矩法方差向下偏（见第 6 节）。*

**数值演算例子（泊松）。** 一个呼叫中心记录 $n=5$ 个一分钟内各自的呼叫数： $2, 4, 3, 5, 6$ 。则 $\bar X=(2+4+3+5+6)/5=20/5=4$ ，故 $\hat\lambda_{\text{MoM}}=4$ 次每分钟。

**数值演算例子（正态方差）。** 对数据 $2,4,6$ ，均值为 $\bar X=4$ 。平方偏差： $(2-4)^2=4$ ， $(4-4)^2=0$ ， $(6-4)^2=4$ ，相加得 $8$ 。则 $\hat\sigma^2_{\text{MoM}}=8/3\approx 2.667$ （除以 $n=3$ ），而无偏版本会除以 $n-1=2$ ，给出 $4$ 。

> **原理 —— 何时求助于 MoM**
>
> 当似然难以最大化时，或作为迭代式 MLE 的起始值时，MoM 大放异彩。在温和条件下它是相合的（随 $n$ 增大其估计趋近真值），但通常比 MLE 效率低：它忽略了似然的完整形状，只用到少数几个矩。

<a id="s5"></a>
### 极大似然估计

*选取使观测数据最可能的参数值。MLE 是现代统计学中占主导地位的估计量。*

#### 大白话定位

在 $\theta$ 的所有候选值中，**极大似然估计**是使我们所看到的数据最可能出现的那个值。它是“最好地解释”观测的单个 $\theta$ 。由于似然是乘积（难以求导）而对数似然是和（易于求导），我们最大化对数；又因 $\log$ 只会单调增加，无论哪种方式峰的位置都相同。

**极大似然估计量**

$$\hat\theta_{\text{MLE}}=\arg\max_{\theta\in\Theta} L(\theta)=\arg\max_{\theta\in\Theta} \ell(\theta),\qquad \text{solve } U(\theta)=\ell'(\theta)=0$$

算子 $\arg\max_{\theta} $ 表示“使后面表达式最大的那个 $\theta$ 值”（与 $\max$ 不同，后者是最大值本身）。

*最大化 $\ell$ 与最大化 $L$ 是等价的（因为 $\log$ 是增函数，所以它保持最大值的位置），但把乘积变成了和。用 $\ell''(\hat\theta)\lt 0$ 确认是极大值。*

**为什么最大化 $\ell$ 与 $L$ 给出相同答案。** 若 $\log$ 严格递增，则 $L(\theta_1)>L(\theta_2)$ 当且仅当 $\log L(\theta_1)>\log L(\theta_2)$ 。所以按 $L$ 对 $\theta$ 值排序与按 $\ell$ 排序完全相同，特别地，排名最高的 $\theta$ 是同一个。

**演示 —— 伯努利 $p$ 的 MLE**

1. 由第 2 节， $L(p)=p^{\sum x_i}(1-p)^{n-\sum x_i}$ 。用 $\log(ab)=\log a+\log b$ 与 $\log(a^c)=c\log a$ 取对数：

   $$\ell(p)=\Big(\sum x_i\Big)\log p+\Big(n-\sum x_i\Big)\log(1-p).$$
2. 逐项求导。回顾 $\frac{d}{dp}\log p=\frac1p$ ，并由链式法则 $\frac{d}{dp}\log(1-p)=\frac{-1}{1-p}$ 。把得分置零：

   $$\ell'(p)=\frac{\sum x_i}{p}-\frac{n-\sum x_i}{1-p}=0.$$
3. 两边乘以 $p(1-p)$ （因 $0<p<1$ 使其非零，故允许）： $(1-p)\sum x_i-p(n-\sum x_i)=0$ 。展开： $\sum x_i - p\sum x_i - pn + p\sum x_i=0$ ，即 $\sum x_i - pn=0$ 。求解：

   $$\hat p_{\text{MLE}}=\frac{1}{n}\sum_{i=1}^n x_i=\bar X.$$
4. 检验它是极大值： $\ell''(p)=-\frac{\sum x_i}{p^2}-\frac{n-\sum x_i}{(1-p)^2}<0$ 处处成立，所以该临界点是峰。

*这里 MLE 与 MoM 重合；一般情形下它们不同。*

**数值演算例子。** 抛一枚硬币 $n=10$ 次，观测到 $7$ 次正面。则 $\hat p_{\text{MLE}}=7/10=0.7$ 。在正面概率为 $0.7$ 的硬币下数据最可能。

**演示 —— 正态 $(\mu,\sigma^2)$ 的 MLE**

1. 正态密度为 $f(x\mid\mu,\sigma^2)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\!\big(-\frac{(x-\mu)^2}{2\sigma^2}\big)$ 。对 $i$ 的乘积取对数（并用 $\log\exp(u)=u$ ），

   $$\ell(\mu,\sigma^2)=-\frac n2\log(2\pi)-\frac n2\log\sigma^2-\frac{1}{2\sigma^2}\sum_{i=1}^n(x_i-\mu)^2.$$
2. 对 $\mu$ 求偏导（只有最后一项依赖 $\mu$ ；对平方用链式法则）： $\partial\ell/\partial\mu=\frac{1}{\sigma^2}\sum(x_i-\mu)$ 。置零： $\sum(x_i-\mu)=0\Rightarrow \sum x_i = n\mu\Rightarrow \hat\mu=\bar X$ 。
3. 对 $\sigma^2$ 求偏导（把 $\sigma^2$ 当作单个变量 $v$ ； $\frac{d}{dv}\log v=\frac1v$ 且 $\frac{d}{dv}(1/v)=-1/v^2$ ）： $\partial\ell/\partial\sigma^2=-\frac{n}{2\sigma^2}+\frac{1}{2\sigma^4}\sum(x_i-\mu)^2$ 。置零并代入 $\mu=\hat\mu=\bar X$ ：

   $$\frac{1}{2\sigma^4}\sum(x_i-\bar X)^2=\frac{n}{2\sigma^2}\ \Rightarrow\ \hat\sigma^2_{\text{MLE}}=\frac1n\sum_{i=1}^n (x_i-\bar X)^2.$$
4. **确认它是最大值点。** 当 $\mu\to\pm\infty$ ，或 $\sigma^2\to 0^+$ ，或 $\sigma^2\to\infty$ 时，项 $-\frac n2\log\sigma^2-\frac1{2\sigma^2}\sum(x_i-\mu)^2$ 使 $\ell\to-\infty$ ；由于 $\ell$ 在开区域 $\{\sigma^2>0\}$ 上光滑且在每个边界都趋于 $-\infty$ ，其内部的临界点——既然唯一——必是全局最大值（严格地说，那里的海森矩阵负定，例如 $\partial^2\ell/\partial\mu^2=-n/\sigma^2<0$ ）。

*除数又是 $n$ 。方差的 MLE 是有偏的——下一节将量化它。*

**数值演算例子。** 对数据 $2,4,6$ ： $\hat\mu=\bar X=4$ ，且（由第 4 节的例子） $\hat\sigma^2_{\text{MLE}}=8/3\approx 2.667$ 。

> **原理 —— 为什么 MLE 如此受推崇**
>
> 在正则性条件下，MLE 是**相合的**（逼近真实 $\theta$ ）、**渐近正态的**（其抽样分布趋于钟形曲线），并且是**渐近有效的**——它在极限下达到 Cramér–Rao 界（第 7 节）。它还具有**不变性**：任意函数 $g(\theta)$ 的 MLE 就是 $g(\hat\theta_{\text{MLE}})$ 。它唯一的弱点是有限样本偏差。

**MLE 的渐近正态性**

$$\sqrt n\,(\hat\theta_{\text{MLE}}-\theta)\ \xrightarrow{d}\ N\!\Big(0,\ \frac{1}{I_1(\theta)}\Big)$$

*$I_1(\theta)$ 是单个观测中的 Fisher 信息（第 7 节）。这一陈述是 Wald 区间与检验的引擎：对大 $n$ ， $\hat\theta_{\text{MLE}}$ 近似为 $N(\theta,\,1/(nI_1(\theta)))$ 。*

> **联系 —— 微积分优化，应用于数据**
>
> 求 $\hat\theta_{\text{MLE}}$ 就是微积分里“把导数置零、检验二阶导数”那套常规，现在应用于 $\ell(\theta)$ 。当不存在闭式时，数值方法（Newton–Raphson，它用到 $\ell''$ ）接管——而 $\ell''$ 又是信息。

<a id="s6"></a>
### 评价估计量：偏差、方差、MSE 与相合性

*估计量是一个随机变量；我们以它的中心位置、它的散布程度，以及它是否随数据积累而逼近真值来评判它。*

#### 大白话定位

两位飞镖选手：一位的投掷紧密成团但全部偏在靶心左侧（散布小，但有系统性偏移），另一位的投掷以靶心为中心但散得很开（无偏移，但散布大）。**偏差**衡量系统性偏移；**方差**衡量散布；**均方误差（MSE）**把两者合并为一个分数。好的估计量让总和保持很小。

**偏差、方差与均方误差**

$$\mathrm{Bias}(\hat\theta)=E[\hat\theta]-\theta,\qquad \mathrm{MSE}(\hat\theta)=E\big[(\hat\theta-\theta)^2\big]$$

$$\mathrm{MSE}(\hat\theta)=\mathrm{Var}(\hat\theta)+\big[\mathrm{Bias}(\hat\theta)\big]^2$$

用文字说：偏差是估计量的平均落点离真值有多远；MSE 是平均的平方偏差；而 MSE 恰好分裂为散布加偏移平方。

*当 $E[\hat\theta]=\theta$ （零偏差）时估计量是**无偏的**。MSE 在散布与系统性偏移之间作权衡——有时一点偏差能换来少很多的方差。*

**演示 —— MSE 的偏差–方差分解**

1. 在误差内部加上又减去估计量自身的均值 $E[\hat\theta]$ ： $(\hat\theta-\theta)=(\hat\theta-E[\hat\theta])+(E[\hat\theta]-\theta)$ 。这是合法的，因为我们加上又减去同一个量，净变化为零。
2. 用 $(a+b)^2=a^2+2ab+b^2$ 把两边平方，然后取期望（第 1 节的 $E$ 的线性性）：

   $$E[(\hat\theta-\theta)^2]=E[(\hat\theta-E\hat\theta)^2]+2(E\hat\theta-\theta)\,E[\hat\theta-E\hat\theta]+(E\hat\theta-\theta)^2.$$

   这里 $(E\hat\theta-\theta)$ 是常数，所以它在交叉项中可以从期望里提出。
3. 交叉项消失，因为 $E[\hat\theta-E\hat\theta]=E[\hat\theta]-E[\hat\theta]=0$ （对均值的偏离的均值为零）。
4. 剩下的是 $E[(\hat\theta-E\hat\theta)^2]$ ，这是**方差的定义** $\mathrm{Var}(\hat\theta)$ ，加上 $(E\hat\theta-\theta)^2$ ，即 $\mathrm{Bias}(\hat\theta)^2$ 。因此 $\mathrm{MSE}=\mathrm{Var}+\mathrm{Bias}^2$ 。

*同样的“加上又减去均值”手法也是恒等式 $\mathrm{Var}(X)=E[X^2]-(E[X])^2$ 的基础。*

**演示 —— 正态方差的 MLE 是有偏的，及其 MSE**

1. 回顾第 5 节， $\hat\sigma^2_{\text{MLE}}=\frac1n\sum(X_i-\bar X)^2$ 。定义**无偏样本方差** $S^2=\frac{1}{n-1}\sum(X_i-\bar X)^2$ 。比较两者， $\hat\sigma^2_{\text{MLE}}=\frac{n-1}{n}S^2$ （因为 $\frac{1}{n}=\frac{n-1}{n}\cdot\frac{1}{n-1}$ ）。
2. 正态数据的一个关键抽样事实（在概率论指南中证明）： $\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}$ ，其中 $\chi^2_{n-1}$ 是**自由度为 $n-1$ 的卡方分布**—— $n-1$ 个独立标准正态的平方和的分布，其均值为 $n-1$ ，方差为 $2(n-1)$ 。由此 $E[S^2]=\sigma^2$ （所以 $S^2$ 无偏）且 $\mathrm{Var}(S^2)=\frac{2\sigma^4}{n-1}$ （重标度： $\mathrm{Var}(S^2)=(\frac{\sigma^2}{n-1})^2\mathrm{Var}(\chi^2_{n-1})=\frac{\sigma^4}{(n-1)^2}\cdot 2(n-1)=\frac{2\sigma^4}{n-1}$ ）。
3. 对第 1 步取期望： $E[\hat\sigma^2_{\text{MLE}}]=\frac{n-1}{n}E[S^2]=\frac{n-1}{n}\sigma^2$ 。因此

   $$\mathrm{Bias}=\frac{n-1}{n}\sigma^2-\sigma^2=-\frac{\sigma^2}{n}.$$

   偏差为负：MLE 平均而言*低*估了方差。
4. 方差： $\mathrm{Var}(\hat\sigma^2_{\text{MLE}})=\big(\tfrac{n-1}{n}\big)^2\mathrm{Var}(S^2)=\big(\tfrac{n-1}{n}\big)^2\frac{2\sigma^4}{n-1}=\frac{2(n-1)\sigma^4}{n^2}$ 。加上偏差平方 $\big(\frac{\sigma^2}{n}\big)^2=\frac{\sigma^4}{n^2}$ ：

   $$\mathrm{MSE}(\hat\sigma^2_{\text{MLE}})=\frac{2(n-1)\sigma^4}{n^2}+\frac{\sigma^4}{n^2}=\frac{(2n-1)\,\sigma^4}{n^2}.$$

*引人注目的是， $\hat\sigma^2_{\text{MLE}}$ 的 MSE 比无偏的 $S^2$ （其 MSE 即其方差 $2\sigma^4/(n-1)$ ）**更小**：这是接受一点偏差以降低总误差的教科书案例。*

**数值演算例子。** 设 $\sigma^2=1$ 且 $n=5$ 。则 $\mathrm{MSE}(S^2)=\frac{2}{4}=0.5$ ，而 $\mathrm{MSE}(\hat\sigma^2_{\text{MLE}})=\frac{2\cdot5-1}{25}=\frac{9}{25}=0.36$ 。这里有偏的 MLE 在 MSE 上胜出。

> **原理 —— 相合性**
>
> 若当 $n\to\infty$ 时 $\hat\theta_n\xrightarrow{p}\theta$ （箭头 $\xrightarrow{p}$ 表示“依概率收敛”：对任意微小容差，偏离 $\theta$ 超过该容差的概率趋于 $0$ ），则估计量是**相合的**。一个充分条件是 $\mathrm{MSE}(\hat\theta_n)\to 0$ （均方相合），它通过**切比雪夫不等式** $P(|\hat\theta-\theta|\ge\varepsilon)\le \mathrm{MSE}/\varepsilon^2$ 强制依概率收敛。有偏与无偏的方差估计量都是相合的，因为它们的偏差（ $\sim 1/n$ ）与方差（ $\sim 1/n$ ）都趋于零——偏差在小样本中要紧，在极限下不要紧。

> **联系 —— 入门指南中的 $n-1$ 终于得到解释**
>
> 入门指南只是断言“除以 $n-1$ 使得 $E[S^2]=\sigma^2$ ”。这里我们看到确切的原因：MLE 的除数 $n$ 产生 $-\sigma^2/n$ 的偏差，而 $n-1$ （Bessel）修正消除了它。那“损失的自由度”就是上面 $\chi^2_{n-1}$ 中的 $n-1$ ——从相同数据中估计 $\bar X$ 用掉了一个自由度。

<a id="s7"></a>
### Fisher 信息与 Cramér–Rao 下界

*任何无偏估计量能有多精确，都有一个硬性下限。Fisher 信息衡量一个样本告诉你多少关于 $\theta$ 的信息；它的倒数就是那个下限。*

#### 大白话定位

某些实验比其他实验更具信息量。如果似然有一个尖锐而狭窄的峰，数据就把 $\theta$ 钉得很紧；如果它宽而平坦，那么许多 $\theta$ 值几乎同样好地解释数据。**Fisher 信息**量化了这种尖锐程度。随后了不起的 **Cramér–Rao 界**说：没有无偏估计量的方差能小于信息的倒数——精度有一个根本的速度极限。

**Fisher 信息**

$$I(\theta)=E\!\left[\Big(\frac{\partial}{\partial\theta}\log f(X\mid\theta)\Big)^2\right]=-\,E\!\left[\frac{\partial^2}{\partial\theta^2}\log f(X\mid\theta)\right]$$

$$I_n(\theta)=n\,I_1(\theta)\quad\text{(information adds over i.i.d. observations)}$$

第一个表达式是**得分的方差**（其平方的平均，因为由第 3 节得分均值为零）。第二个，在正则性下与之相等，是对数似然的**期望负曲率**——二阶导数衡量斜率如何变化，即曲线弯曲得多厉害。下标区分单个观测中的信息（ $I_1$ ）与整个样本中的信息（ $I_n$ ）。

**为什么信息可加。** 因为 $\ell(\theta)=\sum_i \log f(x_i\mid\theta)$ 是一个和（第 3 节），它的二阶导数是各单观测二阶导数之和。对每个 i.i.d. 项取 $-E[\cdot]$ 给出相同的 $I_1(\theta)$ ，把 $n$ 个相加得 $I_n(\theta)=nI_1(\theta)$ 。

**演示 —— $I(\theta)$ 的两个公式一致**

1. 从第 3 节的均值为零恒等式出发，写成 $\int (\partial_\theta\log f)\,f\,dx=0$ （缩写 $\partial_\theta=\frac{\partial}{\partial\theta}$ ）。
2. 对 $\theta$ 求此式的导数（由正则性把导数移入），对 $(\partial_\theta\log f)\cdot f$ 用乘积法则：

   $$\int \big(\partial_\theta^2\log f\big) f\,dx + \int (\partial_\theta\log f)\,(\partial_\theta f)\,dx=0.$$
3. 在第二个积分中代入 $\partial_\theta f = f\,\partial_\theta\log f$ （第 3 节的对数导数恒等式），给出 $\int (\partial_\theta\log f)^2 f\,dx$ 。
4. 于是 $E[\partial_\theta^2\log f]+E[(\partial_\theta\log f)^2]=0$ ，即 $E[(\partial_\theta\log f)^2]=-E[\partial_\theta^2\log f]$ ，这正是所断言的相等。

*信息是得分的方差，等价地是对数似然的期望曲率。尖锐的似然峰意味着高信息，意味着精确的估计。*

**演示 —— 伯努利 $p$ 的 Fisher 信息**

1. 单个观测： $\log f(x\mid p)=x\log p+(1-x)\log(1-p)$ 。
2. 得分（一阶导数，来自第 3 节）： $\frac{\partial}{\partial p}\log f=\frac{x}{p}-\frac{1-x}{1-p}$ 。二阶导数（用 $\frac{d}{dp}(1/p)=-1/p^2$ 与链式法则）： $\frac{\partial^2}{\partial p^2}\log f=-\frac{x}{p^2}-\frac{1-x}{(1-p)^2}$ 。
3. 取 $-E[\cdot]$ ，用 $E[X]=p$ 故 $E[1-X]=1-p$ ：

   $$I_1(p)=\frac{E[X]}{p^2}+\frac{E[1-X]}{(1-p)^2}=\frac{p}{p^2}+\frac{1-p}{(1-p)^2}=\frac1p+\frac1{1-p}=\frac{1}{p(1-p)}.$$

   最后一步把分数通分到公分母 $p(1-p)$ ： $\frac{1}{p}+\frac{1}{1-p}=\frac{(1-p)+p}{p(1-p)}=\frac{1}{p(1-p)}$ 。

*所以 $I_n(p)=n/[p(1-p)]$ —— $p$ 越极端（接近 $0$ 或 $1$ ），每次试验的信息越大。*

**Cramér–Rao 下界（CRLB）**

$$\text{for any unbiased }\hat\theta:\qquad \mathrm{Var}(\hat\theta)\ \ge\ \frac{1}{I_n(\theta)}=\frac{1}{n\,I_1(\theta)}$$

*没有无偏估计量能击败这一方差。达到它的估计量是**有效的**；其**相对效率**是界与其实际方差之比（一个介于 $0$ 与 $1$ 之间的数， $1$ 表示完全有效）。*

**演示 —— Cramér–Rao 界**

1. 设 $\hat\theta$ 无偏，并设 $U=U(\theta)$ 为得分，有 $E[U]=0$ （第 3 节）且 $\mathrm{Var}(U)=I_n(\theta)$ （信息作为得分方差的定义）。
2. 我们证明 $\mathrm{Cov}(\hat\theta,U)=1$ 。从无偏性 $E[\hat\theta]=\int \hat\theta(\mathbf x) f(\mathbf x\mid\theta)\,d\mathbf x=\theta$ 出发。对 $\theta$ 求导（正则性允许移入）： $\int \hat\theta\,\partial_\theta f\,d\mathbf x=1$ 。代入 $\partial_\theta f=f\,U$ （对数导数恒等式）： $\int \hat\theta\,U\,f\,d\mathbf x = E[\hat\theta U]=1$ 。由于 $E[U]=0$ ，协方差为 $\mathrm{Cov}(\hat\theta,U)=E[\hat\theta U]-E[\hat\theta]E[U]=1-0=1$ 。
3. 对协方差应用 **Cauchy–Schwarz 不等式** $\mathrm{Cov}(A,B)^2\le\mathrm{Var}(A)\mathrm{Var}(B)$ （协方差永不超过散布之积）。取 $A=\hat\theta$ ， $B=U$ ：

   $$1=\mathrm{Cov}(\hat\theta,U)^2\le \mathrm{Var}(\hat\theta)\,\mathrm{Var}(U)=\mathrm{Var}(\hat\theta)\,I_n(\theta).$$
4. 两边除以 $I_n(\theta)>0$ ：

   $$\mathrm{Var}(\hat\theta)\ge\frac{1}{I_n(\theta)}.$$

*示例：对伯努利， $\hat p=\bar X$ 有 $\mathrm{Var}(\bar X)=\frac{p(1-p)}{n}$ （第 1 节，因为对伯努利 $\mathrm{Var}(X)=p(1-p)$ ）。界是 $\frac{1}{I_n(p)}=\frac{p(1-p)}{n}$ ——两者相等，所以 $\bar X$ 达到下限，是**有效的**。*

**数值演算例子。** 当 $p=0.5$ 且 $n=100$ 时， $I_n=\frac{100}{0.5\cdot0.5}=400$ ，所以 CRLB 是 $1/400=0.0025$ ，而确实 $\mathrm{Var}(\bar X)=\frac{0.25}{100}=0.0025$ 。标准误是 $\sqrt{0.0025}=0.05$ 。

> **联系 —— 曲率、微积分与 MLE**
>
> 形式 $I=-E[\ell'']$ 字面上就是期望二阶导数——对数似然在其峰处弯曲程度的微积分度量。这就是为什么 MLE 的渐近方差（第 5 节）是 $1/I_n(\theta)$ ：更弯曲的似然把 $\theta$ 钉得更紧。

<a id="s8"></a>
### Rao–Blackwell 与最小方差无偏估计量

*给定任何无偏估计量，对充分统计量取条件只会改进它。加上完备性，这就产生唯一的最优无偏估计量。*

#### 大白话定位

假设你有一个粗糙的、只用到部分数据的无偏猜测。第 2 节告诉我们充分统计量持有关于 $\theta$ 的*全部*信息。**Rao–Blackwell 定理**说：把你的粗糙猜测在无关细节上取平均（即对充分统计量取条件），你就得到一个新的估计量，它仍然无偏但方差*不会更大*——通常严格更小。加上**完备性**，这个改进后的估计量可被证明是唯一的最优无偏估计量。

#### 定义

- **条件期望** $E[\tilde\theta\mid T]$ ：在给定 $T$ 取某一值的所有数据集中 $\tilde\theta$ 的平均值。它本身是 $T$ 的函数，因此是一个有效统计量。
- **MVUE：** **最小方差无偏估计量**——方差尽可能小的无偏估计量。

**Rao–Blackwell 定理**

$$\text{if } E[\tilde\theta]=\theta \text{ and } T \text{ is sufficient, then } \hat\theta=E[\tilde\theta\mid T] \text{ satisfies } E[\hat\theta]=\theta,\quad \mathrm{Var}(\hat\theta)\le \mathrm{Var}(\tilde\theta)$$

**演示 —— 为什么 Rao–Blackwell 有效**

1. **无偏性被保持。** **全期望律**说 $E\big[E[\tilde\theta\mid T]\big]=E[\tilde\theta]$ 。由于 $\hat\theta=E[\tilde\theta\mid T]$ ，这给出 $E[\hat\theta]=E[\tilde\theta]=\theta$ 。
2. **方差不增加。** **全方差律**陈述 $\mathrm{Var}(\tilde\theta)=\mathrm{Var}\big(E[\tilde\theta\mid T]\big)+E\big[\mathrm{Var}(\tilde\theta\mid T)\big]$ 。第一项是 $\mathrm{Var}(\hat\theta)$ ；第二项是方差的平均，因此 $\ge 0$ 。去掉一个非负项， $\mathrm{Var}(\tilde\theta)\ge\mathrm{Var}(\hat\theta)$ 。
3. **为什么 $T$ 必须充分。** 若 $T$ 不充分， $E[\tilde\theta\mid T]$ 仍可能（通过条件分布）依赖于未知的 $\theta$ ，使它不可计算且不是有效统计量。充分性保证条件分布不含 $\theta$ ，所以 $\hat\theta$ 是一个真正的估计量。

**演示 —— 对一个粗糙的泊松估计量做 Rao–Blackwell 化**

1. 设 $X_1,\dots,X_n\ \text{i.i.d.}\ \sim\text{Poisson}(\lambda)$ ；我们想估计 $g(\lambda)=e^{-\lambda}$ ，它等于 $P(X=0)$ （零事件的概率）。
2. 一个粗糙的无偏估计量只用第一个观测： $\tilde g=\mathbf{1}\{X_1=0\}$ ，即 $X_1=0$ 时为 $1$ 、否则为 $0$ 的示性函数。它的期望是 $E[\tilde g]=P(X_1=0)=e^{-\lambda}$ ，所以它无偏——但很浪费，忽略了 $X_2,\dots,X_n$ 。
3. 总和 $T=\sum X_i$ 对 $\lambda$ 充分且完备（它是指数族统计量，第 2 节）。通过取条件做 Rao–Blackwell 化： $\hat g=E[\mathbf 1\{X_1=0\}\mid T]=P(X_1=0\mid T)$ 。
4. 一个标准事实：给定总和 $T=t$ ，计数 $X_1$ 服从 $\text{Binomial}(t,1/n)$ （ $t$ 个事件中每个以概率 $1/n$ 落入第 $1$ 个槽位）。第 $1$ 个槽位中为零的概率是 $\big(1-\frac1n\big)^t$ 。因此

   $$\hat g=P(X_1=0\mid T=t)=\Big(1-\tfrac1n\Big)^{t}=\Big(\tfrac{n-1}{n}\Big)^{\sum X_i}.$$

*这个改进的估计量是无偏的（由 Rao–Blackwell）且方差更小——并且，由完备性，它是 $e^{-\lambda}$ 的唯一 MVUE。*

**数值演算例子。** 当 $n=4$ 且观测总和 $T=2$ 时，只用 $X_1$ 的粗糙估计量会给出 $0$ 或 $1$ ；Rao–Blackwell 化后的估计是光滑的 $\big(\frac{3}{4}\big)^2=\frac{9}{16}\approx 0.5625$ ，是对 $e^{-\lambda}$ 远更合理的猜测。

**Lehmann–Scheffé 定理（MVUE）**

$$T \text{ complete \& sufficient},\ \ E[\,\varphi(T)\,]=\theta \ \Longrightarrow\ \varphi(T) \text{ is the unique MVUE of }\theta$$

*若存在完备充分统计量的一个无偏函数，则它就是**那个**最小方差无偏估计量。完备性保证唯一性。*

**为什么唯一性由完备性得出。** 假设 $\varphi_1(T)$ 与 $\varphi_2(T)$ 是完备充分 $T$ 的两个无偏函数。它们的差 $d(T)=\varphi_1(T)-\varphi_2(T)$ 对所有 $\theta$ 有 $E[d(T)]=\theta-\theta=0$ 。由**完备性**的定义（第 2 节），唯一这样的函数恒为零，所以 $\varphi_1=\varphi_2$ 。因此 $T$ 的无偏函数是唯一的，而 Rao–Blackwell 表明它胜过任何其他无偏估计量。

> **原理 —— 通往最优无偏估计量之路**
>
> （1）找一个完备充分统计量 $T$ （常通过指数族）。（2）找任意一个无偏估计量。（3）对 $T$ 取条件，或直接找一个具有正确均值的 $T$ 的函数。结果就是 MVUE。对正态样本， $\bar X$ 是 $\mu$ 的 MVUE， $S^2$ 是 $\sigma^2$ 的 MVUE。

> **联系 —— 充分性的回报**
>
> 第 2 节承诺充分性会让我们“免费”改进估计量。Rao–Blackwell 就是回报：保信息的压缩 $T$ 正是我们用来取条件以甩掉无关方差的对象。

## C 部分 · 区间估计与检验

<a id="s9"></a>
### 通过枢轴量构造置信区间

*置信区间由枢轴量构造：一个数据与参数的函数，其分布是固定且已知的。反转其已知分位数即可框住 $\theta$ 。*

#### 大白话定位

单个最佳猜测 $\hat\theta$ 永远不会恰好正确。**置信区间**转而报告一个可信值的*范围*，连同一个像 95% 这样的置信水平。构造它的诀窍是**枢轴量**：一个数据与未知 $\theta$ 的巧妙组合，其概率分布完全已知且不涉及 $\theta$ 。因为我们知道枢轴量的分布，我们就知道它有 95% 的时间落在哪两个临界值之间；把那一陈述重排以孤立出 $\theta$ ，就得到区间。

#### 定义

- **分位数。** 一个分布有给定比例落在其下方的截断点。对标准正态， $z_{\alpha/2}$ 是右侧面积为 $\alpha/2$ 的点。
- **$\alpha$ （alpha）。** 容许的错误率；置信水平为 $1-\alpha$ 。对 95% 置信， $\alpha=0.05$ 。

**枢轴量**

$$Q(\mathbf X,\theta)\ \text{is a pivot if its distribution does not depend on }\theta.$$

*从 $P(a\le Q\le b)=1-\alpha$ ，代数地孤立出 $\theta$ ，得到一个以概率 $1-\alpha$ 覆盖 $\theta$ 的随机区间。*

**演示 —— 正态均值的 CI， $\sigma$ 已知**

1. 枢轴量：由第 1 节， $Z=\dfrac{\bar X-\mu}{\sigma/\sqrt n}\sim N(0,1)$ 。它的分布（标准正态）不涉及 $\mu$ ，所以它是一个有效枢轴量。
2. 用对称的标准正态临界值 $\pm z_{\alpha/2}$ 框住它：由这些分位数的定义， $P\big(-z_{\alpha/2}\le Z\le z_{\alpha/2}\big)=1-\alpha$ 。
3. 代入 $Z$ 并对 $\mu$ 解这一双重不等式。从 $-z_{\alpha/2}\le \frac{\bar X-\mu}{\sigma/\sqrt n}\le z_{\alpha/2}$ 出发。三部分同乘 $\sigma/\sqrt n>0$ （保持不等号方向）： $-z_{\alpha/2}\frac{\sigma}{\sqrt n}\le \bar X-\mu\le z_{\alpha/2}\frac{\sigma}{\sqrt n}$ 。减去 $\bar X$ 并乘以 $-1$ （这会**反转**不等号），给出

   $$\bar X-z_{\alpha/2}\frac{\sigma}{\sqrt n}\ \le\ \mu\ \le\ \bar X+z_{\alpha/2}\frac{\sigma}{\sqrt n}.$$

*对 $\alpha=0.05$ ， $z_{\alpha/2}=z_{0.025}=1.96$ ——经验法则中的“两个标准误”。*

**数值演算例子。** 设 $\sigma=10$ ， $n=25$ ， $\bar X=50$ 。标准误是 $\sigma/\sqrt n=10/5=2$ 。95% 区间是 $50\pm 1.96\times 2 = 50\pm 3.92$ ，即 $[46.08,\ 53.92]$ 。

**演示 —— 正态均值的 CI， $\sigma$ 未知（ $t$ 枢轴量）**

1. 实际中 $\sigma$ 未知，所以用样本标准差 $S=\sqrt{S^2}$ 替换它。候选枢轴量是 $T=\dfrac{\bar X-\mu}{S/\sqrt n}$ 。它不再是标准正态，因为分母现在是随机的。
2. 重写 $T=\dfrac{(\bar X-\mu)/(\sigma/\sqrt n)}{S/\sigma}$ 。分子是 $N(0,1)$ （第 1 节）。对于分母，回顾第 6 节 $\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}$ ，所以 $S/\sigma=\sqrt{\chi^2_{n-1}/(n-1)}$ ，并且（对正态数据）它与分子*独立*。
3. 由**学生氏 $t$ 的定义**（一个标准正态除以一个独立的卡方除以其自由度后的平方根；见第 12 节）， $T\sim t_{n-1}$ ，即自由度为 $n-1$ 的 $t$ 分布——而关键在于这一分布既不涉及 $\mu$ 也不涉及 $\sigma$ ，所以 $T$ 是有效枢轴量。
4. 用 $t$ 临界值 $t_{n-1,\alpha/2}$ 完全照前面那样反转：

   $$\bar X\ \pm\ t_{n-1,\,\alpha/2}\,\frac{S}{\sqrt n}.$$

*更肥的 $t$ 尾部（更大的临界值）是估计 $\sigma$ 的代价；当 $n\to\infty$ 时 $t_{n-1}\to N(0,1)$ ，两个区间合并。*

**数值演算例子。** 当 $n=10$ （ $9$ 个自由度）， $\bar X=50$ ， $S=10$ ， $t_{9,0.025}=2.262$ 时：标准误是 $10/\sqrt{10}\approx 3.162$ ，所以区间是 $50\pm 2.262\times 3.162=50\pm 7.15$ ，即 $[42.85,\ 57.15]$ ——比 $\sigma$ 已知的情形更宽，反映了额外的不确定性。

> **原理 —— 置信意味着什么**
>
> 置信是**程序**的性质，而非某一个区间的性质。“95% 置信”意味着：在反复抽样中，随机区间有 $95\%$ 的时间覆盖固定的 $\theta$ 。一旦算出，某个特定区间如 $[46.08, 53.92]$ 要么包含 $\theta$ 要么不包含——再无概率可言。

> **联系 —— 枢轴量统一了入门指南中的区间**
>
> 入门指南中的每一个 CI——对均值、对比例、对方差（用 $\chi^2$ 枢轴量）——都是反转某个枢轴量。配方“估计 $\pm$ 临界值 $\times$ SE”是枢轴量近似为 $N(0,1)$ 的特例。

<a id="s10"></a>
### 假设检验：错误、功效与 Neyman–Pearson 引理

*检验把数据空间分割为“拒绝”和“不拒绝”。在所有水平 $\alpha$ 的检验中，哪个功效最大？对简单假设，Neyman–Pearson 给出确切的答案。*

#### 大白话定位

**假设检验**是对关于 $\theta$ 的某一论断的法庭。**原假设** $H_0$ 是默认（“硬币是均匀的”）；**备择假设** $H_1$ 是对手（“硬币有偏”）。我们设计一条规则，它查看数据并要么拒绝 $H_0$ 要么不拒绝。两种错误都可能发生：冤枉无辜（拒绝一个为真的 $H_0$ ）与放走有罪（未能拒绝一个为假的 $H_0$ ）。我们把第一种错误率封顶在 $\alpha$ ，然后让第二种尽可能小。

#### 定义

- **第一类错误：** 当 $H_0$ 实际为真时拒绝它。其概率是 $\alpha$ 。
- **第二类错误：** 当 $H_1$ 为真时未能拒绝 $H_0$ 。其概率是 $\beta$ 。
- **功效：** 正确拒绝一个为假的 $H_0$ 的概率，等于 $1-\beta$ 。
- **简单假设：** 把 $\theta$ 固定到单个值的假设（例如 $\theta=\theta_0$ ），与**复合**假设（例如 $\theta>\theta_0$ ）相对。

**错误、水平与功效**

$$\alpha=P_{\theta_0}(\text{reject }H_0)\ \text{(Type I)},\qquad \beta=P_{\theta_1}(\text{fail to reject }H_0)\ \text{(Type II)}$$

$$\text{power}=1-\beta=P_{\theta_1}(\text{reject }H_0)$$

*检验有一个**水平** $\alpha$ （其最大第一类错误率）和一个**功效函数** $\beta(\theta)=P_\theta(\text{reject})$ ，给出在每个 $\theta$ 处的拒绝概率。我们固定 $\alpha$ 并最大化功效。*

**Neyman–Pearson 引理**

$$\text{For }H_0:\theta=\theta_0 \text{ vs } H_1:\theta=\theta_1,\ \text{the most powerful size-}\alpha\text{ test rejects when } \frac{L(\theta_1)}{L(\theta_0)}\ge k.$$

*似然比是两个简单假设的最优检验统计量；选取阈值 $k$ 使水平等于 $\alpha$ 。*

**演示 —— Neyman–Pearson 最优性**

一个**检验**由函数 $\phi(\mathbf x)\in\{0,1\}$ 描述，它在拒绝处等于 $1$ 、在不拒绝处等于 $0$ 。它的水平是 $E_{\theta_0}[\phi]$ ，功效是 $E_{\theta_1}[\phi]$ 。

1. 设 $\phi^*$ 是似然比（LR）检验，恰好在 $L(\theta_1)\ge k\,L(\theta_0)$ 处拒绝（即 $\phi^*=1$ ）， $k$ 的选取使其水平恰为 $\alpha$ 。设 $\phi$ 是任意水平 $\le\alpha$ 的竞争检验。
2. 考虑在每个数据点处的乘积 $(\phi^*-\phi)\big(L(\theta_1)-kL(\theta_0)\big)$ 。在 $\phi^*=1$ 处：由规则， $L(\theta_1)-kL(\theta_0)\ge0$ ，且 $\phi^*-\phi=1-\phi\ge0$ ，所以乘积 $\ge0$ 。在 $\phi^*=0$ 处：规则给出 $L(\theta_1)-kL(\theta_0)<0$ ，且 $\phi^*-\phi=-\phi\le0$ ，所以乘积又 $\ge0$ （负数乘以非正数）。因此逐点乘积 $\ge 0$ ，所以它的积分也是：

   $$\int (\phi^*-\phi)\big(L(\theta_1)-kL(\theta_0)\big)\,d\mathbf x\ \ge\ 0.$$
3. 把积分展开成两块，识别 $\int \phi^* L(\theta_1)=\text{power}(\phi^*)$ 等等：

   $$\big[\text{power}(\phi^*)-\text{power}(\phi)\big]-k\big[\text{size}(\phi^*)-\text{size}(\phi)\big]\ge0.$$
4. 由于 $k\ge0$ 且 $\text{size}(\phi)\le\alpha=\text{size}(\phi^*)$ ，括号 $\text{size}(\phi^*)-\text{size}(\phi)\ge0$ ，所以被减项 $-k[\cdots]\le 0$ 。把它移过去， $\text{power}(\phi^*)-\text{power}(\phi)\ge k[\text{size}(\phi^*)-\text{size}(\phi)]\ge0$ 。因此 $\text{power}(\phi^*)\ge\text{power}(\phi)$ ：LR 检验功效最大。

*似然比的最优性是下一节每个检验的种子。*

**演示 —— 正态均值的最大功效检验**

1. $X_i\sim N(\mu,\sigma^2)$ ， $\sigma$ 已知， $H_0:\mu=\mu_0$ vs $H_1:\mu=\mu_1$ ，其中 $\mu_1>\mu_0$ 。
2. 计算似然比的对数。每个似然是 $\prod \frac{1}{\sqrt{2\pi}\sigma}\exp(-\frac{(x_i-\mu)^2}{2\sigma^2})$ ，常数在比值中相消。指数之差是 $-\frac{1}{2\sigma^2}\sum[(x_i-\mu_1)^2-(x_i-\mu_0)^2]$ 。展开平方： $(x_i-\mu_1)^2-(x_i-\mu_0)^2 = -2x_i(\mu_1-\mu_0)+(\mu_1^2-\mu_0^2)$ 。求和，

   $$\log\frac{L(\mu_1)}{L(\mu_0)}=\frac{(\mu_1-\mu_0)}{\sigma^2}\sum x_i+\text{const}=\frac{n(\mu_1-\mu_0)}{\sigma^2}\bar X+\text{const}.$$
3. 由于 $\mu_1-\mu_0>0$ ，LR 是 $\bar X$ 的*增*函数。所以“对大 LR 拒绝”与“对大 $\bar X$ 拒绝”是同一条规则：当 $\bar X\ge c$ 时拒绝。
4. 选取 $c$ 使水平为 $\alpha$ 。在 $H_0$ 下， $\frac{\bar X-\mu_0}{\sigma/\sqrt n}\sim N(0,1)$ ，所以 $P_{\mu_0}(\bar X\ge c)=\alpha$ 意味着 $\frac{c-\mu_0}{\sigma/\sqrt n}=z_\alpha$ ，给出 $c=\mu_0+z_\alpha\,\sigma/\sqrt n$ 。等价地，当 $Z=\frac{\bar X-\mu_0}{\sigma/\sqrt n}\ge z_\alpha$ 时拒绝。

*熟悉的单侧 $z$ 检验就是 Neyman–Pearson 最优检验——并且由于拒绝规则不依赖于具体的 $\mu_1$ （只依赖 $\mu_1>\mu_0$ ），它对所有 $\mu>\mu_0$ 是**一致最大功效的**。*

**数值演算例子。** 检验 $H_0:\mu=100$ vs $H_1:\mu>100$ ， $\sigma=15$ ， $n=9$ ， $\alpha=0.05$ （故 $z_{0.05}=1.645$ ）。截断点是 $c=100+1.645\times 15/3=100+8.225=108.225$ 。若观测到 $\bar X=110$ ，则 $110>108.225$ ，所以我们拒绝 $H_0$ 。等价地 $Z=(110-100)/5=2.0>1.645$ 。

> **联系 —— 检验与区间互为对偶**
>
> $H_0:\theta=\theta_0$ 的水平 $\alpha$ 双侧检验恰好在 $\theta_0$ 落在 $1-\alpha$ 置信区间之外时拒绝。检验的接受域反转之后*就是*一个置信集——这正是入门指南所暗示的对偶，现在被精确化了。

<a id="s11"></a>
### 似然比、Wald 与得分检验

*对复合假设与多参数，三种渐近等价的检验占主导——全部由似然构造，全部近似 $\chi^2$ 。*

#### 大白话定位

Neyman–Pearson 引理是完美的，但只针对两个单一值。真实问题更丰富：“ $\mu$ 等于 $100$ 吗，对抗*任何*其他值？”三种通用检验处理这一点，全部由似然导出，全部对大样本产生一个服从卡方分布的统计量。它们从三个角度看对数似然的同一个峰——它的高度、它的位置、它的斜率。

**广义似然比统计量**

$$\Lambda=\frac{\sup_{\theta\in\Theta_0} L(\theta)}{\sup_{\theta\in\Theta} L(\theta)},\qquad -2\log\Lambda\ \xrightarrow{d}\ \chi^2_{r}$$

新符号： $\sup$ （“上确界”）表示可达到的最大值； $\Theta_0$ 是 $H_0$ 下允许的受限参数集， $\Theta$ 是全集。所以 $\Lambda$ 把 $H_0$ 下的最佳拟合与总体的最佳拟合作比较；它总是介于 $0$ 与 $1$ 之间，小的 $\Lambda$ 反对 $H_0$ 。

*$r$ 是 $H_0$ 所施加的约束数（ $H_0$ 移除了多少个自由参数）。对大的 $-2\log\Lambda$ 拒绝。这一极限卡方就是 **Wilks 定理**。*

**演示 —— 一个 LRT 及其 $\chi^2_1$ 极限（Wilks）**

1. 正态样本， $\sigma$ 已知；检验 $H_0:\mu=\mu_0$ vs $H_1:\mu\ne\mu_0$ 。分子在唯一允许的值 $\mu_0$ 上最大化 $L$ （别无选择）；分母在所有 $\mu$ 上最大化，在 MLE $\hat\mu=\bar X$ 处达到（第 5 节）。
2. 代入正态对数似然并构造 $-2\log\Lambda = -2[\ell(\mu_0)-\ell(\bar X)]$ 。只有平方和那一项依赖 $\mu$ ：

   $$-2\log\Lambda=\frac{1}{\sigma^2}\Big[\sum(x_i-\mu_0)^2-\sum(x_i-\bar X)^2\Big].$$

   用恒等式 $\sum(x_i-\mu_0)^2=\sum(x_i-\bar X)^2+n(\bar X-\mu_0)^2$ 展开（一种勾股式分裂，通过在平方内加上又减去 $\bar X$ 并注意交叉项求和为零来验证）。 $\sum(x_i-\bar X)^2$ 相消，留下

   $$-2\log\Lambda=\frac{n(\bar X-\mu_0)^2}{\sigma^2}.$$
3. 在 $H_0$ 下， $\frac{\sqrt n(\bar X-\mu_0)}{\sigma}\sim N(0,1)$ （第 1 节），而一个标准正态的平方按定义是 $\chi^2_1$ （第 12 节）。因此

   $$-2\log\Lambda=\Big(\tfrac{\bar X-\mu_0}{\sigma/\sqrt n}\Big)^2=Z^2\sim\chi^2_1.$$

*这里 Wilks 的 $\chi^2_1$ 是精确的（一个约束， $r=1$ ）；一般情形下它在 $n\to\infty$ 时渐近成立。*

**数值演算例子。** 当 $\mu_0=100$ ， $\sigma=15$ ， $n=9$ ， $\bar X=110$ 时： $-2\log\Lambda=\frac{9(110-100)^2}{225}=\frac{900}{225}=4.0$ 。 $\chi^2_1$ 的 5% 截断点是 $3.84$ 。由于 $4.0>3.84$ ，拒绝 $H_0$ （与给出 $Z=2.0$ 的 $z$ 检验一致，且 $2.0^2=4.0$ ）。

**Wald 与得分（Rao）检验**

$$W=\frac{(\hat\theta-\theta_0)^2}{\widehat{\mathrm{Var}}(\hat\theta)}=I_n(\hat\theta)\,(\hat\theta-\theta_0)^2,\qquad R=\frac{U(\theta_0)^2}{I_n(\theta_0)}$$

*两个统计量都 $\xrightarrow{d}\chi^2_r$ 。**Wald** 检验使用 MLE $\hat\theta$ 及那里的曲率（ $\widehat{\mathrm{Var}}(\hat\theta)=1/I_n(\hat\theta)$ ，来自第 7 节）；**得分**检验使用 $\ell$ 在 $\theta_0$ 处的斜率 $U(\theta_0)$ ，根本不需要 MLE。LRT、Wald 与得分渐近一致。*

**数值演算例子（Wald，伯努利）。** 从 $n=100$ 次抛掷得 $40$ 次正面检验 $H_0:p=0.5$ ，所以 $\hat p=0.4$ 。MLE 处的信息是 $I_n(\hat p)=\frac{n}{\hat p(1-\hat p)}=\frac{100}{0.4\cdot0.6}=416.67$ 。则 $W=416.67\times(0.4-0.5)^2=416.67\times0.01=4.17>3.84$ ，所以在 5% 水平拒绝。

> **原理 —— 一个峰的三种视角**
>
> 想象对数似然曲线在其最大值附近。**LRT** 衡量 $\ell$ 从 $\hat\theta$ 下降到 $\theta_0$ 的垂直落差；**Wald** 检验衡量水平距离 $\hat\theta-\theta_0$ （按曲率缩放）；**得分**检验衡量 $\ell$ 在 $\theta_0$ 处的斜率。对一个二次（正态）对数似然，三者完全重合；一般情形下它们只在有限样本中有差异。

> **联系 —— Cramér–Rao 投入运用**
>
> Wald 方差 $1/I_n(\hat\theta)$ 是在 MLE 处求值的 Cramér–Rao 界（第 7 节）——那一节的下限作为分母中的标准误回归。得分检验直接使用 $U(\theta_0)$ 与 $I_n(\theta_0)$ ：正是第 3 节与第 7 节定义的那些量。

<a id="s12"></a>
### 标准检验及其抽样分布（t、χ²、F）

*三个分布，全部由从正态总体抽样产生，提供了经典统计学的精确检验。*

#### 大白话定位

你遇到的几乎每个“具名”检验—— $t$ 检验、卡方检验、方差分析的 F 检验——都由三个分布之一构造。这三个全部*构造*自标准正态：把若干正态平方就得到卡方；把一个正态除以一个缩放的卡方就得到 $t$ ；取两个卡方之比就得到 F。了解这些构造就揭穿了整套经典工具的神秘面纱。

**这三者如何由正态样本产生**

$$Z=\frac{\bar X-\mu}{\sigma/\sqrt n}\sim N(0,1),\qquad \frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}$$

$$t_k=\frac{Z}{\sqrt{\chi^2_k/k}},\qquad F_{d_1,d_2}=\frac{\chi^2_{d_1}/d_1}{\chi^2_{d_2}/d_2}$$

文字定义： $\chi^2_k$ （自由度为 $k$ 的卡方）是 $Z_1^2+\cdots+Z_k^2$ 的分布，即 $k$ 个独立标准正态平方之和。 $t_k$ 是一个标准正态除以一个*独立*的 $\chi^2_k$ 按其自由度缩放后的平方根。 $F_{d_1,d_2}$ 是两个独立卡方之比，每个各除以其自身的自由度。

*对正态样本 $\bar X\perp S^2$ （符号 $\perp$ 表示“独立于”；对正态数据样本均值与样本方差独立）——正是这一独立性使 $t$ 比值的分子与分母独立，正如 $t_k$ 的定义所要求。*

**演示 —— 借助 Helmert 变换证明 $(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$ 与 $\bar X\perp S^2$**

*这两个事实——在上文以及第 6 节中被默默使用——是正态样本理论的基石。下面对 $X_1,\dots,X_n\ \text{i.i.d.}\ \sim N(\mu,\sigma^2)$ 给出它们的证明。*

1. **标准化。** 令 $Z_i=(X_i-\mu)/\sigma$ 。则 $Z_1,\dots,Z_n\ \text{i.i.d.}\ \sim N(0,1)$ ，于是随机向量 $\mathbf Z=(Z_1,\dots,Z_n)^\top$ 具有**球对称**的联合密度 $\propto\exp\!\big(-\tfrac12\sum_i z_i^2\big)=\exp\!\big(-\tfrac12\|\mathbf z\|^2\big)$ 。它对 $\mathbf z$ 的依赖只通过其长度 $\|\mathbf z\|^2=\sum z_i^2$ 。
2. **施加一个正交（Helmert）变换。** 设 $A$ 是一个 $n\times n$ **正交矩阵**（ $A^\top A=I$ ，即其各行是两两垂直的单位向量），其**第一行**是常向量 $\big(\tfrac{1}{\sqrt n},\dots,\tfrac{1}{\sqrt n}\big)$ ；其余 $n-1$ 行是补全一组标准正交基的任意单位向量（经典的 **Helmert 矩阵**是一种显式选择）。定义 $\mathbf Y=A\mathbf Z$ ，即 $Y_j=\sum_i A_{ji}Z_i$ 。
3. **变换后的向量仍是 i.i.d. 标准正态。** 正交映射保持长度， $\|\mathbf Y\|^2=\mathbf Z^\top A^\top A\,\mathbf Z=\|\mathbf Z\|^2$ ，且雅可比行列式为 $\pm1$ ，所以 $\mathbf Y$ 的密度 $\propto\exp\!\big(-\tfrac12\|\mathbf y\|^2\big)$ ——*同样*的球对称形式。该密度分解为 $\prod_j\exp(-\tfrac12 y_j^2)$ ，所以 $Y_1,\dots,Y_n\ \text{i.i.d.}\ \sim N(0,1)$ 。（等价地：独立正态的线性组合是正态，而正交性使各 $Y_j$ 不相关，因此——由于联合正态——相互独立。）
4. **辨认第一个坐标。** $Y_1=\sum_i\tfrac{1}{\sqrt n}Z_i=\sqrt n\,\bar Z$ ，其中 $\bar Z=\frac1n\sum Z_i=(\bar X-\mu)/\sigma$ 。因此 $Y_1=\sqrt n\,(\bar X-\mu)/\sigma$ 只是 $\bar X$ 的函数。
5. **辨认其余坐标即 $S^2$ 。** 由于 $A$ 保持长度， $\sum_{j=1}^n Y_j^2=\sum_{i=1}^n Z_i^2$ 。减去第一个坐标：由第 4 步的代数以及恒等式 $\sum_i(Z_i-\bar Z)^2=\sum_i Z_i^2-n\bar Z^2$ ，
   $$\sum_{j=2}^n Y_j^2=\sum_{i=1}^n Z_i^2-Y_1^2=\sum_{i=1}^n Z_i^2-n\bar Z^2=\sum_{i=1}^n(Z_i-\bar Z)^2=\frac{1}{\sigma^2}\sum_{i=1}^n(X_i-\bar X)^2=\frac{(n-1)S^2}{\sigma^2}.$$
6. **读出两个结论。** 右端 $\sum_{j=2}^n Y_j^2$ 是 $n-1$ 个独立标准正态平方之和，按定义即 $\chi^2_{n-1}$ ；因此 $\dfrac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}$ 。此外 $\bar X$ 只是 $Y_1$ 的函数（第 4 步），而 $S^2$ 只是 $Y_2,\dots,Y_n$ 的函数（第 5 步），且这两组 $Y_j$ 相互独立（第 3 步）；所以 $\bar X\perp S^2$ 。

*这唯一的技巧——把 i.i.d. 正态向量旋转，使一个新坐标轴指向全 1 方向（均值），而另外 $n-1$ 个轴张成其正交补（偏差）——一举给出两个事实，并清晰地展示了“ $n-1$ 个自由度”从何而来：一个轴被 $\bar X$ 花掉了。*

| 分布 | 定义 | 用于 | 检验统计量 |
| --- | --- | --- | --- |
| $t_k$ | $N(0,1)\big/\sqrt{\chi^2_k/k}$ | 均值， $\sigma$ 未知；回归系数 | $t=\dfrac{\bar X-\mu_0}{S/\sqrt n}$ |
| $\chi^2_k$ | $k$ 个 $N(0,1)$ 平方之和 | 方差；拟合优度；独立性；LRT/Wald/得分极限 | $\dfrac{(n-1)S^2}{\sigma_0^2}$, $\ \sum\dfrac{(O-E)^2}{E}$ |
| $F_{d_1,d_2}$ | 两个缩放 $\chi^2$ 之比 | 比较两个方差；方差分析（3 个及以上均值） | $F=\dfrac{S_1^2}{S_2^2}$, $\ \dfrac{\text{MS}_{\text{between}}}{\text{MS}_{\text{within}}}$ |

**演示 —— 单样本 $t$ 统计量确实是 $t_{n-1}$**

1. 写出统计量，然后把分子分母都除以 $\sigma$ 以标准化： $\dfrac{\bar X-\mu}{S/\sqrt n}=\dfrac{(\bar X-\mu)/(\sigma/\sqrt n)}{S/\sigma}$ 。分子 $(\bar X-\mu)/(\sigma/\sqrt n)$ 正好是 $Z\sim N(0,1)$ （第 1 节）。
2. 分母： $S/\sigma=\sqrt{S^2/\sigma^2}$ 。由 $\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}$ 得 $\frac{S^2}{\sigma^2}=\frac{\chi^2_{n-1}}{n-1}$ ，所以 $S/\sigma=\sqrt{\chi^2_{n-1}/(n-1)}$ 。对正态数据这与分子独立（因为 $\bar X\perp S^2$ ）。
3. 代入后，统计量等于 $\dfrac{N(0,1)}{\sqrt{\chi^2_{n-1}/(n-1)}}$ ，分子分母独立——这正是上面给出的 $t_{n-1}$ 的定义。因此单样本 $t$ 统计量恰好是 $t_{n-1}$ 。

*这里 $t$ 分布不是近似——它是精确的抽样律，也是入门指南“ $\sigma$ 未知时用 $t$ ”正确的原因。*

**数值演算例子（卡方方差检验）。** 从 $n=10$ 件、观测 $S^2=6$ 检验某过程的方差是否为 $\sigma_0^2=4$ 。统计量是 $\frac{(n-1)S^2}{\sigma_0^2}=\frac{9\times 6}{4}=13.5$ ，与 $\chi^2_9$ 比较。 $\chi^2_9$ 的上 5% 截断点是 $16.92$ ，所以 $13.5<16.92$ ，我们在上尾不拒绝——观测到的方差不是显著地大。

> **联系 —— 概率论指南的分布，投入运用**
>
> 概率论指南中抽象定义的 $\chi^2$ 、 $t$ 与 $F$ 正是正态数据统计量的抽样分布。经典推断在很大程度上就是用这三个律记账。

## D 部分 · 贝叶斯与非参数

<a id="s13"></a>
### 贝叶斯推断：先验、后验与共轭性

*把 $\theta$ 本身当作随机。把信念编码进一个先验，通过贝叶斯定理用数据更新，然后读出后验—— $\theta$ 的一个完整分布。*

#### 大白话定位

迄今 $\theta$ 都是一个固定未知量。**贝叶斯**方法做了一个大胆之举：把 $\theta$ 当作随机的，带有一个概率分布描述我们在看到数据*之前*的信念（**先验**）。在观测数据之后，我们用贝叶斯定理把那些信念更新为一个**后验**分布。后验是一个完整的答案——不是单个估计而是 $\theta$ 上整条可信度曲线。

#### 定义

- **先验** $\pi(\theta)$ ：看到数据之前 $\theta$ 的分布（希腊字母 $\pi$ ，“pi”，表示参数上的一个密度）。
- **后验** $\pi(\theta\mid\mathbf x)$ ：看到数据之后 $\theta$ 的分布。
- **证据 / 边缘似然：** 分母 $\int L(\theta)\pi(\theta)\,d\theta$ ，一个使后验积分为 $1$ 的常数。
- **$\propto$ （“正比于”）：** 相差一个不涉及 $\theta$ 的常数因子时相等。

**参数的贝叶斯定理**

$$\pi(\theta\mid\mathbf x)=\frac{L(\theta)\,\pi(\theta)}{\int L(\theta)\,\pi(\theta)\,d\theta}\ \propto\ \underbrace{L(\theta)}_{\text{likelihood}}\ \underbrace{\pi(\theta)}_{\text{prior}}$$

*后验 $\propto$ 似然 $\times$ 先验。分母（边缘/证据）只是确保后验是一个有效分布的归一化常数。*

**为什么这是贝叶斯定理。** 事件的贝叶斯定理说 $P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}$ 。把 $A$ 等同于“ $\theta$ 取某一给定值”（先验 $\pi(\theta)$ ），把 $B$ 等同于“数据 $\mathbf x$ ”（给定 $\theta$ 时其概率是似然 $L(\theta)=f(\mathbf x\mid\theta)$ ）。则 $P(A\mid B)$ 成为后验， $P(B\mid A)$ 成为似然， $P(A)$ 成为先验， $P(B)$ 成为证据——正是上面那个公式，只是用密度替换了事件概率。

> **概念 —— 共轭性**
>
> 若所得后验属于与先验相同的族，则一个先验对一个似然是**共轭的**。共轭对使更新纯粹是代数的——无需积分——并把数据的效应揭示为该族参数的一个简单变化。

| 似然 | 共轭先验 | 后验 |
| --- | --- | --- |
| 伯努利 / 二项($p$) | Beta($\alpha,\beta$) | Beta($\alpha+\sum x_i,\ \beta+n-\sum x_i$) |
| 泊松($\lambda$) | Gamma($\alpha,\beta$) | Gamma($\alpha+\sum x_i,\ \beta+n$) |
| 正态均值（ $\sigma^2$ 已知） | Normal($\mu_0,\tau_0^2$) | 正态（精度加权，见下） |
| 正态精度（ $\mu$ 已知） | Gamma | Gamma |
| 指数($\lambda$) | Gamma($\alpha,\beta$) | Gamma($\alpha+n,\ \beta+\sum x_i$) |
| 多项 | Dirichlet | Dirichlet |

**演示 —— Beta–伯努利更新**

**Beta($\alpha,\beta$)** 分布是 $[0,1]$ 上一条灵活的曲线，其密度正比于 $p^{\alpha-1}(1-p)^{\beta-1}$ ——一个概率的天然先验。

1. 先验 $\pi(p)\propto p^{\alpha-1}(1-p)^{\beta-1}$ ；似然 $L(p)\propto p^{\sum x_i}(1-p)^{n-\sum x_i}$ （来自第 2 节）。
2. 相乘，用规则 $a^b a^c=a^{b+c}$ 合并幂次：

   $$\pi(p\mid\mathbf x)\propto p^{\alpha-1}(1-p)^{\beta-1}\cdot p^{\sum x_i}(1-p)^{n-\sum x_i}=p^{\alpha+\sum x_i-1}(1-p)^{\beta+n-\sum x_i-1}.$$
3. 把指数与 Beta 形式 $p^{a-1}(1-p)^{b-1}$ 相匹配：这是 $\text{Beta}\big(\alpha+\sum x_i,\ \beta+n-\sum x_i\big)$ 的核——同一个族，第一个参数加上成功次数，第二个参数加上失败次数。

*先验参数 $(\alpha,\beta)$ 起到先验成功与失败的“伪计数”的作用。*

**数值演算例子。** 从均匀先验 $\text{Beta}(1,1)$ （所有概率等可能）出发。抛一枚硬币 $n=10$ 次，观测到 $7$ 次正面（ $\sum x_i=7$ ，失败 $=3$ ）。后验是 $\text{Beta}(1+7,\ 1+3)=\text{Beta}(8,4)$ 。它的均值是 $\frac{8}{8+4}=\frac{8}{12}\approx 0.667$ ——被先验的伪计数从原始的 $0.7$ 略微拉低。

> **联系 —— 概率论指南中的贝叶斯定理**
>
> 这正是用于事件的同一个贝叶斯定理，提升到密度： $P(A\mid B)\propto P(B\mid A)P(A)$ 变成 $\pi(\theta\mid x)\propto f(x\mid\theta)\pi(\theta)$ 。频率派与贝叶斯推断共享似然；它们只在 $\theta$ 是否获得一个概率分布上有所不同。

<a id="s14"></a>
### 贝叶斯估计与可信区间

*从后验中提取点估计与区间——而著名的正态–正态更新表明后验均值是先验与数据的精度加权平均。*

#### 大白话定位

后验是一个完整的分布，但我们常想要单个数字或一个范围。**后验均值**是天然的单一汇总；**可信区间**是贝叶斯的范围。与置信区间不同，可信区间让你能诚实地说“ $\theta$ 落在此处的概率是 95%”——因为在贝叶斯世界里 $\theta$ 有一个概率分布。

**后验点估计**

$$\hat\theta_{\text{Bayes}}=E[\theta\mid\mathbf x]\ \text{(posterior mean, min. squared-error loss)},\qquad \hat\theta_{\text{MAP}}=\arg\max_\theta \pi(\theta\mid\mathbf x)$$

新术语：**MAP** 代表**最大后验**——后验密度取峰值（其众数）的那个值。

*后验均值最小化期望平方误差损失；后验中位数最小化绝对损失；MAP（众数）是带先验惩罚的 MLE 的贝叶斯类比。*

**为什么后验均值最小化平方误差损失。** 我们寻找最小化 $E[(\theta-d)^2\mid\mathbf x]$ 的数 $d$ 。展开： $E[\theta^2\mid\mathbf x]-2dE[\theta\mid\mathbf x]+d^2$ 。对 $d$ 求导并置零： $-2E[\theta\mid\mathbf x]+2d=0$ ，故 $d=E[\theta\mid\mathbf x]$ ，即后验均值。二阶导数是 $2>0$ ，确认是极小值。

**演示 —— 正态先验是共轭的；后验均值是精度加权的**

一个正态分布的**精度**是其方差的倒数；大精度意味着紧、有信心的信念。

1. 数据汇总 $\bar X\mid\mu\sim N(\mu,\sigma^2/n)$ （ $\sigma$ 已知），先验 $\mu\sim N(\mu_0,\tau_0^2)$ 。后验正比于两个正态密度之积；在指数中我们把 $\mu$ 的两个二次式相加。
2. $\mu$ 的两个二次式之和本身是一个二次式，所以后验是正态的： $\mu\mid\mathbf x\sim N(\mu_n,\tau_n^2)$ 。在指数中收集 $\mu^2$ 的系数，给出后验精度为先验精度 $1/\tau_0^2$ 与数据精度 $n/\sigma^2$ 之和：

   $$\frac{1}{\tau_n^2}=\frac{1}{\tau_0^2}+\frac{n}{\sigma^2}.$$
3. 收集线性项的系数并相除，给出后验均值为先验均值 $\mu_0$ 与数据均值 $\bar X$ 的精度加权平均：

   $$\mu_n=\frac{\frac{1}{\tau_0^2}\,\mu_0+\frac{n}{\sigma^2}\,\bar X}{\frac{1}{\tau_0^2}+\frac{n}{\sigma^2}}.$$

   每个来源都按其精度加权——越有信心的来源拉得越用力。

*当 $n\to\infty$ 时数据精度 $n/\sigma^2$ 占主导， $\mu_n\to\bar X$ ，先验被冲淡——贝叶斯与频率派估计收敛。*

**数值演算例子。** 先验 $\mu\sim N(\mu_0=0,\ \tau_0^2=1)$ ，故先验精度 $=1$ 。数据： $\sigma^2=4$ ， $n=8$ ， $\bar X=3$ ，故数据精度 $=n/\sigma^2=8/4=2$ 。后验精度 $=1+2=3$ ，所以 $\tau_n^2=1/3\approx 0.333$ 。后验均值 $\mu_n=\frac{1\cdot0+2\cdot3}{3}=\frac{6}{3}=2$ ——介于先验的 $0$ 与数据的 $3$ 之间的折中，因为数据精度是其两倍而向数据倾斜。

**可信区间**

$$P\big(\theta\in C\mid\mathbf x\big)=1-\alpha,\qquad \text{e.g. } [\,q_{\alpha/2},\,q_{1-\alpha/2}\,]\ \text{of the posterior}$$

这里 $q_{\alpha/2}$ 与 $q_{1-\alpha/2}$ 是*后验*分布的下、上分位数。

*与置信区间不同，这**是**给定数据时关于 $\theta$ 的直接概率陈述——人们错误地附加给置信区间的那种解释。*

**数值演算例子。** 接上文，后验是 $N(2,\ 0.333)$ ，标准差 $\sqrt{0.333}\approx 0.577$ 。95% 可信区间是 $2\pm 1.96\times 0.577=2\pm 1.13$ ，即 $[0.87,\ 3.13]$ ，而我们可以合法地说“给定数据与先验， $\theta$ 以概率 0.95 落在 $[0.87, 3.13]$ 中”。

> **原理 —— 可信 vs 置信**
>
> 95% **可信**区间说“给定数据与先验， $\theta$ 以概率 0.95 落在此处”。95% **置信**区间对程序作一个长期频率的断言（第 9 节）。在平先验与对称似然下两者常在数值上重合，但其含义截然不同。

> **联系 —— 正则化是一个先验**
>
> 在 $\mu$ 上用正态先验的 MAP 估计正是把 $\bar X$ 向 $\mu_0$ 作岭式收缩：最大化对数后验是在对数似然上加一个 $-\frac{(\mu-\mu_0)^2}{2\tau_0^2}$ 惩罚。带惩罚的似然方法是伪装的 MAP 估计——贝叶斯先验与估计的优化观点之间的一座桥。

<a id="s15"></a>
### 非参数方法与自助法

*当你不愿假定一个参数模型时，让数据替代总体。经验分布与重抽样承担重活。*

#### 大白话定位

迄今我们总是假定一个模型族（正态、泊松等）。**非参数**方法放弃这一假定，让数据自己说话。关键对象是**经验分布**——字面上就是把数据的直方图当作它*就是*总体。**自助法**则通过反复从数据中重抽样来估计估计量的不确定性，绕开对任何公式的需要。

#### 定义

- **经验分布函数（EDF）** $\hat F_n(x)$ ：数据中 $\le x$ 的比例。
- **示性函数** $\mathbf 1\{A\}$ ：当陈述 $A$ 为真时等于 $1$ ，否则为 $0$ 。
- **重抽样（有放回）：** 从观测值中抽出的一个大小为 $n$ 的新数据集，每次抽取均匀随机且值可以重复。

**经验分布函数**

$$\hat F_n(x)=\frac1n\sum_{i=1}^n \mathbf 1\{X_i\le x\}\ \xrightarrow{\text{a.s.}}\ F(x)\quad(\text{Glivenko–Cantelli, uniformly})$$

箭头 $\xrightarrow{\text{a.s.}}$ 表示“几乎必然”（以概率一）。**Glivenko–Cantelli 定理**保证 $\hat F_n$ 一致收敛到真实的 $F$ ——不只在每个点处，而是处处同时。

*$\hat F_n$ 是 $F$ 的非参数 MLE。插入式估计量用 $\hat F_n$ 替换未知的 $F$ ：样本均值估计总体均值，样本中位数估计总体中位数，以此类推。*

**为什么 $\hat F_n(x)\to F(x)$ 在每个 $x$ 处。** 固定 $x$ 。每个示性函数 $\mathbf 1\{X_i\le x\}$ 是一个伯努利变量，以概率 $F(x)=P(X\le x)$ 等于 $1$ 。所以 $\hat F_n(x)$ 是 $n$ 个 i.i.d. 伯努利($F(x)$) 变量的平均，由**大数定律**（第 6 节相合性，应用于此），这个平均收敛到它的均值 $F(x)$ 。Glivenko–Cantelli 把这一点加强为关于 $x$ 一致地成立。

> **概念 —— 自助法的思想**
>
> 要在没有公式的情况下衡量一个统计量 $\hat\theta=T(\hat F_n)$ 的变异性，把样本当作总体：从中重抽样并观察 $\hat\theta$ 如何变化。**插入原理**——用 $\hat F_n$ 替换 $F$ ——就是全部诀窍。

**演示 —— 用于标准误的非参数自助法**

1. 从观测样本 $\{x_1,\dots,x_n\}$ 有放回地抽出一个大小为 $n$ 的重抽样： $\{x_1^*,\dots,x_n^*\}$ 。（某些原始值出现多次，另一些根本不出现。）
2. 在重抽样上计算统计量， $\hat\theta^{*(b)}=T(x_1^*,\dots,x_n^*)$ （例如样本中位数）。
3. 对 $b=1,\dots,B$ （比如 $B=2000$ ）重复第 1–2 步，得到副本 $\hat\theta^{*(1)},\dots,\hat\theta^{*(B)}$ 。
4. 用自助副本的散布（样本标准差）估计标准误，其中 $\bar{\hat\theta}^{*}=\frac1B\sum_b \hat\theta^{*(b)}$ 是它们的平均：

   $$\widehat{\text{SE}}_{\text{boot}}=\sqrt{\frac{1}{B-1}\sum_{b=1}^B\big(\hat\theta^{*(b)}-\bar{\hat\theta}^{*}\big)^2}.$$
5. 一个简单的 $1-\alpha$ 区间是**百分位区间** $\big[\hat\theta^{*}_{(\alpha/2)},\ \hat\theta^{*}_{(1-\alpha/2)}\big]$ ——副本的经验分位数（例如 95% 取第 2.5 和第 97.5 百分位）。

*没有分布假定，没有 CLT 公式——重抽样仅从数据本身重建抽样分布。*

**数值演算例子（微型，手算）。** 数据 $\{1, 5, 9\}$ ，统计量 = 均值。一个重抽样可能是 $\{5,5,9\}$ ，均值 $19/3\approx 6.33$ ；另一个 $\{1,1,9\}$ ，均值 $11/3\approx 3.67$ ；又一个 $\{1,5,5\}$ ，均值 $11/3\approx 3.67$ 。在许多这样的重抽样中，这些均值的散布估计了 $\text{SE}(\bar X)$ ——这里由于我们知道 $\bar X$ 的公式，它应当接近 $\sqrt{\frac{\text{样本方差}}{3}}$ ，提供了一个自助法无需使用该公式即可重现的合理性检验。

> **联系 —— 为什么自助法有效**
>
> 抽样分布描述当样本从 $F$ 抽取时 $\hat\theta$ 如何变化。自助法用 $\hat F_n$ 替换未知的 $F$ 并从*它*中抽取。Glivenko–Cantelli 保证 $\hat F_n\approx F$ ，所以自助变异性近似真实抽样变异性——插入原理投入运用。

<a id="s16"></a>
### 一瞥之外：决策理论与大样本渐近

*一个统一的框架——把估计与检验视为损失下的决策——以及使 MLE 成为默认工具的渐近机制（delta 方法、有效性）。*

#### 大白话定位

退一步，把估计与检验看作一个思想的特例：在不确定性下作**决策**，其中错误带有**损失**。一条决策规则的质量是它的平均损失，称为**风险**。另外，**delta 方法**让我们把 MLE 已知的近似正态性贯穿任何光滑变换，所以我们能给像比值（odds）和率这样的导出量附上误差棒。

#### 定义

- **决策规则** $\delta$ ：把观测数据映射到一个行动的函数（例如一个估计，或“拒绝/不拒绝”）。
- **损失函数** $\ell(\theta, d)$ ：当真值为 $\theta$ 时采取行动 $d$ 的惩罚（注意：这个 $\ell$ 是损失，而非前面各节的对数似然；这个符号按惯例被重复使用）。
- **风险** $R(\theta,\delta)$ ：期望损失，对数据取平均。

**风险，决策的语言**

$$R(\theta,\delta)=E_\theta\big[\,\ell(\theta,\delta(\mathbf X))\,\big],\qquad \text{e.g. squared-error loss } \ell(\theta,d)=(d-\theta)^2\Rightarrow R=\text{MSE}$$

*决策规则 $\delta$ 把数据映射到行动；它的**风险**是期望损失。在平方误差损失下，风险正是第 6 节的 MSE——所以估计是决策理论的一个特例。*

**为什么平方误差风险等于 MSE。** 取 $\ell(\theta,d)=(d-\theta)^2$ 且 $d=\delta(\mathbf X)=\hat\theta$ ，风险是 $R=E_\theta[(\hat\theta-\theta)^2]$ ，这就是均方误差的定义（第 6 节）。

> **原理 —— 可容许性、极小极大与贝叶斯规则**
>
> 若另一条规则处处风险 $\le$ 且在某处严格更小（它被支配，故永不值得使用），则一条规则是**不可容许的**。**极小极大**规则最小化最坏情形风险 $\max_\theta R(\theta,\delta)$ ；**贝叶斯**规则最小化对一个先验取平均的风险——它是第 14 节后验期望损失的最小化者。引人注目的是，在维数 $\ge3$ 时样本均值是不可容许的（Stein 悖论）：收缩估计量处处胜过它。

**delta 方法**

$$\sqrt n\,(\hat\theta-\theta)\xrightarrow{d}N(0,\sigma^2)\ \Longrightarrow\ \sqrt n\,\big(g(\hat\theta)-g(\theta)\big)\xrightarrow{d}N\!\big(0,\ [g'(\theta)]^2\sigma^2\big)$$

这里 $g$ 是任意光滑变换， $g'(\theta)$ 是它的导数。结论是说：变换后的估计量也近似正态，方差按斜率平方 $[g'(\theta)]^2$ 缩放。

*一阶 Taylor 展开把渐近正态性贯穿一个光滑变换 $g$ ——误差传播的渐近版本，纯粹是微积分。*

**演示 —— delta 方法**

1. 把 $g$ 在 $\theta$ 处**Taylor 展开**到一阶（微积分事实：光滑函数在局部被其切线很好地逼近）： $g(\hat\theta)\approx g(\theta)+g'(\theta)(\hat\theta-\theta)$ 。误差是 $(\hat\theta-\theta)^2$ 阶的，当 $\hat\theta\to\theta$ 时相对于线性项可忽略。
2. 减去 $g(\theta)$ 并乘以 $\sqrt n$ ： $\sqrt n\,(g(\hat\theta)-g(\theta))\approx g'(\theta)\cdot\sqrt n\,(\hat\theta-\theta)$ 。
3. 由假设 $\sqrt n(\hat\theta-\theta)\xrightarrow{d}N(0,\sigma^2)$ 。把一个收敛到 $N(0,\sigma^2)$ 的量乘以常数 $g'(\theta)$ 会把它的方差按 $[g'(\theta)]^2$ 缩放（回顾 $\mathrm{Var}(cY)=c^2\mathrm{Var}(Y)$ ，第 1 节）。由 **Slutsky 定理**（它让我们把一个依分布收敛的序列与常数结合），右边 $\xrightarrow{d}N(0,[g'(\theta)]^2\sigma^2)$ ，左边也如此。

*这就是如何为比值、率以及其他变换参数得到标准误的。*

**数值演算例子。** 设 $\hat p=0.4$ 来自 $n=100$ ，其中 $\mathrm{Var}(\hat p)=\frac{p(1-p)}{n}\approx\frac{0.4\cdot0.6}{100}=0.0024$ 。我们想要**对数比值** $g(p)=\log\frac{p}{1-p}$ 的标准误。它的导数是 $g'(p)=\frac{1}{p(1-p)}=\frac{1}{0.24}\approx 4.167$ 。由 delta 方法， $\mathrm{Var}(g(\hat p))\approx [g'(\hat p)]^2\mathrm{Var}(\hat p)=4.167^2\times 0.0024\approx 0.0417$ ，所以对数比值的标准误是 $\sqrt{0.0417}\approx 0.204$ 。

> **原理 —— MLE 的渐近至上性**
>
> 在正则性下， $\sqrt n(\hat\theta_{\text{MLE}}-\theta)\xrightarrow{d}N(0,1/I_1(\theta))$ ：MLE 是相合的、渐近正态的，并且渐近有效——它在极限下达到 Cramér–Rao 界（第 7 节）。这就是为什么，在没有特殊结构时，极大似然（及其贝叶斯表亲）是统计推断的主力。

> **联系 —— 整部指南，浓缩成一段弧**
>
> 似然（s3）给出得分与信息（s7）；最大化它给出 MLE（s5）；信息为它的方差设界（s7–8）并设定区间的宽度（s9）与检验的尺度（s10–11）；同一个似然乘以一个先验给出后验（s13–14）；而在不假定模型之处，经验分布与自助法（s15）顶上。一个函数——似然——组织起整个学科。

---

*一门数理统计课程——充分性、估计、Cramér–Rao 界、Neyman–Pearson 与似然比检验、贝叶斯更新以及自助法——每条原理都被精确陈述，每个定理都被演示。它是入门统计与概率论指南的同伴。把任意一个框作为参考随时回顾，并记住：在估计、检验与贝叶斯背后，同样矗立着一个单一对象，即似然函数。*
