[English](general-relativity.md) · **中文**

# 广义相对论与洛伦兹几何，*作为弯曲时空的引力。*

*一次严谨、自足的旅程，从等效原理出发，走向爱因斯坦场方程乃至更远。我们把时空视为洛伦兹流形，细致地构建其因果与曲率结构，从作用量导出场方程，进而严格获得那些经典成果——牛顿极限、引力波、施瓦西与克尔黑洞、膨胀的宇宙以及奇点定理——每一步都给出充分的论证。这是一份始终把物理放在视野之内的数学指南：每一个公式都有定义，每一处推导都没有缺口，每一个符号在使用之前都先被引入。*

[← 返回全部指南](../README.zh.md)

**预备知识。** 本指南直接建立在 **微分几何与张量** 指南及其应用篇 **高级张量分析** 之上。我们从中取用以下内容，并在用到时用一句话各自重述：一个 **光滑流形** $M$ 是一个借助坐标卡在局部上看起来像 $\mathbb{R}^n$ 的空间； $p\in M$ 处的一个 **切向量** 是作用在函数上的方向导数算子 $V=V^\mu\partial_\mu$ ；一个 **张量** 是一个多重线性对象，其分量按 $T'^{\mu}{}_{\nu}=\frac{\partial x'^\mu}{\partial x^\alpha}\frac{\partial x^\beta}{\partial x'^\nu}T^{\alpha}{}_{\beta}$ 变换；**度量** $g_{\mu\nu}$ 是一个对称非退化的 $(0,2)$ 张量；**协变导数** $\nabla$ 用 **克里斯托费尔符号** $\Gamma^\lambda{}_{\mu\nu}=\tfrac12 g^{\lambda\sigma}(\partial_\mu g_{\sigma\nu}+\partial_\nu g_{\sigma\mu}-\partial_\sigma g_{\mu\nu})$ 来修正偏导数；而 **不变体积元** 是 $\sqrt{-g}\,d^nx$ ，其中 $g=\det(g_{\mu\nu})$ 。我们不再重新证明这些；我们在洛伦兹号差下把它们投入使用。全文中，重复指标求和（爱因斯坦约定），希腊指标 $\mu,\nu,\dots\in\{0,1,2,3\}$ 标记时空坐标，其中 $x^0$ 为时间坐标，拉丁空间指标 $i,j,\dots\in\{1,2,3\}$ ， $\partial_\mu\equiv\partial/\partial x^\mu$ ，并且我们令光速 $c=1$ ，除非恢复它有助于阐明某个极限。

## A 部分 · 舞台：洛伦兹几何与因果性

<a id="s0"></a>
### 动机——等效原理，以及为何引力就是时空的几何

牛顿引力是一种力：质量 $M$ 产生场 $\vec{g}=-\nabla\Phi$ ，而一个检验粒子的加速度为 $\ddot{\vec{x}}=-\nabla\Phi$ 。这幅图景里隐藏着一个静默的奇迹。感受场的"引力质量" $m_g$ （力 $=m_g\,\vec{g}$ ）与抵抗加速的"惯性质量" $m_i$ （力 $=m_i\,\ddot{\vec{x}}$ ），就任何实验所能分辨而言，*是同一个数*。厄缶型实验确认 $m_g/m_i$ 恒定到优于 $10^{13}$ 分之一。在牛顿理论中这一相等是一个无法解释的巧合；在爱因斯坦理论中它是奠基之石。

#### 我们要解决什么问题？

我们想要一个引力理论，它能够 (i) 解释为何所有物体不论成分都以相同方式下落，(ii) 与狭义相对论相容（没有瞬时的超距作用；信号速度有限），并 (iii) 在适当的极限下化归为牛顿的成功理论。其解答是激进的：**引力不是作用在固定舞台上的力；它就是舞台本身的形状。** 自由下落的物体沿着穿过弯曲时空的最直可能路径——测地线——运动，而物质告诉时空如何弯曲。

#### 等效原理的审慎陈述

> **弱等效原理（WEP）。** 一个自由下落检验体的轨迹只依赖于它的初始位置与速度，而不依赖于它的内部成分。等价地，对每个物体都有 $m_g=m_i$ 。

> **爱因斯坦等效原理（EEP）。** 在时空中一个充分小的区域内，任何局域非引力实验的结果都与（自由下落的）实验室的速度和位置无关。在局部，自由下落与无引力情形下的惯性运动无法区分；匀加速与匀强引力场无法区分。

那些著名的思想实验让 EEP 变得生动。一个身处无窗电梯中的观察者，无法借助局域实验分辨电梯究竟是在深空中以 $9.8\,\text{m/s}^2$ 加速、还是静止地坐落在地球表面；也无法分辨它究竟是在朝地球自由下落、还是漂浮在深空之中。*局域* 一词至关重要：真实的引力场逐点变化，因此在一个大区域内并排释放的两个检验质量会 *彼此* 漂近（两者都朝地心下落）。这些残余的相对加速度——**潮汐效应**——正是无法被变换消去的部分，它们恰是时空 **曲率**（s5）的标志。

#### 从原理到几何

把 EEP 转化为几何的逻辑如下。

1. EEP 表明，在每一个事件处都存在 **局域惯性坐标**，在其中自由粒子以恒定速度沿直线运动，且狭义相对论的定律在一阶近似下成立。这等价于说存在一个度量，其值可以在一点处被化为闵可夫斯基形式 $\eta_{\mu\nu}=\mathrm{diag}(-1,1,1,1)$ ，且在那里一阶导数为零。
2. 由一个标准的流形事实（法坐标的存在性，已在微分几何指南中证明），这正是一个（伪）黎曼流形在一点附近所呈现的情形：人们总可以选取坐标使得 $g_{\mu\nu}(p)=\eta_{\mu\nu}$ 且 $\partial_\alpha g_{\mu\nu}(p)=0$ ，但一般而言 *二阶* 导数——曲率——无法被化为零。
3. 那些不可消去的二阶导数就是潮汐场。因此引力场被编码在一个洛伦兹号差度量的曲率之中，而自由下落就是该度量的测地运动。

> **直观。** "质量告诉时空如何弯曲；弯曲的时空告诉质量如何运动。" 前半句是爱因斯坦场方程（s6）；后半句是测地线方程（s3）。本指南其余的一切，都是对这两句话的细致展开。

本指南余下部分按五个部分组织。A 部分（s0–s2）搭建洛伦兹舞台及其因果结构。B 部分（s3–s5）发展测地线与曲率，即引力的运动学。C 部分（s6–s7）是动力学：场方程、它们的牛顿极限以及引力波。D 部分（s8–s9）研究最重要的解，黑洞。E 部分（s10–s11）涵盖宇宙学以及关于奇点的整体定理。

<a id="s1"></a>
### 洛伦兹流形；度量号差；类时/类光/类空向量；光锥；固有时

我们现在把"弯曲时空"精确化。

> **定义——洛伦兹度量与流形。** 光滑 $n$ 维流形 $M$ 上的一个 **洛伦兹度量** 是对每一点 $p$ 光滑地指派一个非退化对称双线性形式 $g_p:T_pM\times T_pM\to\mathbb{R}$ ，使得在每个 $p$ 处都存在一组基，在其中 $g_p=\mathrm{diag}(-1,+1,\dots,+1)$ 。二元组 $(M,g)$ 称为一个 **洛伦兹流形**；物理的 **时空** 是 $n=4$ 的情形。我们用分量记 $g(V,W)=g_{\mu\nu}V^\mu W^\nu$ ，并记 **线元** $ds^2=g_{\mu\nu}\,dx^\mu dx^\nu$ 。

正负号的模式称为 **号差**。它是良定义的——与用来对角化 $g$ 的基无关——这就是 **西尔维斯特惯性定律**。

> **定理（西尔维斯特惯性定律）。** 对于实向量空间上一个非退化对称双线性形式，通过对角化得到的正对角元个数 $p_+$ 与负对角元个数 $p_-$ ，对每一组对角化基都相同。二元组 $(p_-,p_+)$ ——或仅是那个孤立负号的符号，记作 $(-,+,+,+)$ ——即号差。

*证明。*
1. 设 $\{e_i\}$ 与 $\{f_j\}$ 是对角化 $g$ 的两组基，分别有 $p_+$ 与 $q_+$ 个正对角元。令 $P=$ 那些满足 $g(e_i,e_i)>0$ 的 $e_i$ 的张成（维数 $p_+$ ）， $N=$ 那些满足 $g(f_j,f_j)\le 0$ 的 $f_j$ 的张成（维数 $n-q_+$ ）。
2. 在 $P\setminus\{0\}$ 上该形式严格为正（ $g(v,v)>0$ ）；在 $N$ 上它非正（ $g(v,v)\le 0$ ）。因此 $P\cap N=\{0\}$ ，因为一个非零向量不能使 $g(v,v)$ 同时既为正又 $\le 0$ 。
3. 于是 $\dim P+\dim N\le n$ （两个仅交于 $0$ 的子空间之和的维数），即 $p_+ +(n-q_+)\le n$ ，给出 $p_+\le q_+$ 。
4. 交换两组基的角色给出 $q_+\le p_+$ 。因此 $p_+=q_+$ ，类似地负的个数也一致。 $\blacksquare$

所以"号差 $(-,+,+,+)$"是一个真正的不变量，而非坐标的产物。（有些教材采用 $(+,-,-,-)$ ；物理是相同的，只是缩并的符号翻转。我们固定为 $(-,+,+,+)$ 。）

#### 三种因果类型

负号按 $g(V,V)$ 的符号把切向量分成三类。

> **定义——因果性质。** 一个非零切向量 $V$ 称为 **类时** 若 $g(V,V)<0$ ，**类光**（或 **光样**）若 $g(V,V)=0$ ，**类空** 若 $g(V,V)>0$ 。零向量按惯例视为类空。一条曲线称为类时/类光/类空，若其切向量在每一点都具有该性质。

在闵可夫斯基空间 $\eta_{\mu\nu}=\mathrm{diag}(-1,1,1,1)$ 中，以 $V=(V^0,\vec V)$ ，我们有 $g(V,V)=-(V^0)^2+|\vec V|^2$ 。于是类时意味着 $|V^0|>|\vec V|$ （速度低于光速），类光意味着 $|V^0|=|\vec V|$ （速度恰为光速），类空意味着 $|V^0|<|\vec V|$ （快于光速——任何有质量粒子都不可能）。

> **定义——光锥。** 在每个事件 $p$ 处， $T_pM$ 中类光向量的集合构成一个双锥，即 $p$ 处的 **光锥**。其内部（类时向量）有两个连通分支；在整个 $M$ 上连续地选取其中一个分支为"未来"即给出一个 **时间定向**。位于未来分支中的向量称为 **未来指向** 的。我们全文假设 $M$ 是时间定向的。

> **算例——闵可夫斯基空间中的光锥。** 取 $\eta=\mathrm{diag}(-1,1,1,1)$ ，以及向量 $V=(2,1,1,1)$ 。则 $g(V,V)=-4+1+1+1=-1<0$ ：类时。向量 $W=(\sqrt3,1,1,1)$ 有 $g(W,W)=-3+3=0$ ：类光。向量 $U=(1,1,1,1)$ 有 $g(U,U)=-1+3=+2>0$ ：类空——它将描述快于光速的运动，对物质是被禁止的。

#### 固有时

对于一条类时世界线——一个有质量粒子的历史——其自然参量是它自己时钟所读出的时间。

> **定义——固有时。** 沿一条切向量为 $u^\mu=dx^\mu/d\lambda$ （故 $g(u,u)<0$ ）的类时曲线 $x^\mu(\lambda)$ ，在参量值 $\lambda_1,\lambda_2$ 之间流逝的 **固有时** 为
>
> $$
> \tau=\int_{\lambda_1}^{\lambda_2}\sqrt{-g_{\mu\nu}\frac{dx^\mu}{d\lambda}\frac{dx^\nu}{d\lambda}}\;d\lambda.
> $$
>
> 等价地沿世界线 $d\tau^2=-ds^2=-g_{\mu\nu}\,dx^\mu dx^\nu$ 。

平方根内的负号恰恰是因为类时向量满足 $g(V,V)<0$ ，故 $-g(V,V)>0$ 且根式为实。用 $\tau$ 本身参数化世界线给出 **四速度** $u^\mu=dx^\mu/d\tau$ ，它自动是单位类时的：
$$
g_{\mu\nu}u^\mu u^\nu=g_{\mu\nu}\frac{dx^\mu}{d\tau}\frac{dx^\nu}{d\tau}=\frac{g_{\mu\nu}dx^\mu dx^\nu}{d\tau^2}=\frac{-d\tau^2}{d\tau^2}=-1.
$$

> **算例——时间膨胀。** 在闵可夫斯基空间中令一个粒子沿 $x$ 以恒定速度 $v$ 运动： $x^\mu(t)=(t,vt,0,0)$ 。则 $d\tau^2=-(-dt^2+dx^2)=dt^2-v^2dt^2=(1-v^2)\,dt^2$ ，故 $d\tau=\sqrt{1-v^2}\,dt$ 。运动的时钟相对于坐标时按洛伦兹因子 $1/\sqrt{1-v^2}$ 变慢——狭义相对论的时间膨胀，直接从度量读出。

> **陷阱。** 固有时仅沿 *类时* 曲线有定义；对类光曲线 $d\tau=0$ （光不经历固有时），对类空曲线被积函数为虚——那里转而使用 **固有长度** $\int\sqrt{g_{\mu\nu}\dot x^\mu\dot x^\nu}\,d\lambda$ 。在选择根号下的符号之前，务必先检查因果性质。

<a id="s2"></a>
### 因果结构——按时序与因果的未来/过去；柯西面与整体双曲性（概述）

每一点处的光锥编织成一个整体的 **因果结构**，它说明哪些事件能够影响哪些事件。由于没有信号快于光速传播，影响只沿类时或类光的未来指向曲线传播。

> **定义——因果与按时序关系。** 对事件 $p,q\in M$ ：
> - $p\ll q$ （ $q$ 在 $p$ 的 **按时序未来** 中）若存在一条从 $p$ 到 $q$ 的光滑未来指向 **类时** 曲线。
> - $p\prec q$ （ $q$ 在 $p$ 的 **因果未来** 中）若 $p=q$ 或存在一条从 $p$ 到 $q$ 的未来指向 **因果**（类时或类光）曲线。
>
> $p$ 的 **按时序未来** 是 $I^+(p)=\{q:p\ll q\}$ ，**因果未来** 是 $J^+(p)=\{q:p\prec q\}$ 。过去 $I^-(p),J^-(p)$ 用过去指向曲线定义。对一个集合 $S$ ， $I^\pm(S)=\bigcup_{p\in S}I^\pm(p)$ ， $J^\pm$ 类似。

基本事实（用光锥的局部结构证明）： $I^+(p)$ 总是 **开** 的； $J^+(p)$ 包含 $I^+(p)$ ，且其边界 $\dot J^+(p)$ 由类光测地线生成。因果曲线的拼接给出传递性：若 $p\prec q$ 且 $q\prec r$ 则 $p\prec r$ ；并且若两段之一是类时的，则 $p\ll r$ （一段类时的腿在拼接时可被"推动"以保持类时）。这些正是"你只能影响你的未来，并且只在你的光锥之内"的精确版本。

> **定义——因果性条件。** 一个时空称为 **因果的** 若它不含闭因果曲线（仅平凡环路才有 $p\prec p$ ），称为 **强因果的** 若任何离开某事件小邻域的因果曲线都无法任意接近地回到它附近。这些排除了时间旅行：一条闭类时曲线会让一个事件处于它自己的过去之中。

#### 柯西面与整体双曲性

最深刻的因果概念是：一个"空间快照"上的初始数据是否决定整个历史——即把物理作为初值问题的适定性。

> **定义——柯西面。** 子集 $\Sigma\subset M$ 称为一个 **柯西面**，若 $M$ 中每一条不可延拓的（极大延拓的）因果曲线都恰好与 $\Sigma$ 相交一次。直观上， $\Sigma$ 是一个完整的"时间瞬间"，每个粒子和每条光线都必须且仅须穿越它一次。

> **定义——整体双曲性。** 一个时空称为 **整体双曲的**，若它是因果的，并且对每一对 $p\prec q$ ，"因果钻石" $J^+(p)\cap J^-(q)$ 是紧的（其中没有事件能逃到无穷或撞上奇点）。Geroch 的一条定理表明这等价于柯西面的存在，并且在那种情形下 $M$ 微分同胚于 $\mathbb{R}\times\Sigma$ ——时空在整体上分裂为时间 $\times$ 空间。

> **为何这很重要。** 整体双曲性是这样一个几何陈述：爱因斯坦方程（s6）容许一个适定的初值问题——在一张柯西面 $\Sigma$ 上指定度量及其变化率，则整个未来时空被确定。这是 ADM 表述（s11）以及数值相对论的基础。

> **算例——闵可夫斯基空间。** $\mathbb{R}^{1,3}$ 是整体双曲的；任何切片 $\{t=\text{const}\}$ 都是柯西面，因为每条不可延拓的因果曲线逐点满足 $|dx^0|\ge|d\vec x|$ ，故其时间坐标在两个方向上都无界增长，从而恰好穿越每个常数 $t$ 切片一次。相反，从闵可夫斯基空间中移除单独一点会破坏整体双曲性：因果曲线可以通过冲入那个洞而变得不可延拓，于是它们便错过了远侧的切片。

> **陷阱。** 并非每个物理上合理的时空都是整体双曲的。极大延拓的克尔与莱斯纳–诺德斯特罗姆黑洞含有 **柯西视界**，越过它预测便失效。我们在此给出概述；奇点定理（s11）以 *整体双曲性加上能量与因果性条件* 换取 *测地不完备的不可避免性*。

## B 部分 · 运动学：测地线与曲率

<a id="s3"></a>
### 列维-奇维塔联络与洛伦兹号差下的测地线；作为自由下落的测地线方程

为了比较不同点处的向量并定义"最直"曲线，我们需要一个联络。度量挑选出唯一一个自然的联络。

> **定理（（伪）黎曼几何基本定理）。** 在任何洛伦兹流形上都存在唯一一个联络 $\nabla$ ，它 (i) **与度量相容**， $\nabla_\lambda g_{\mu\nu}=0$ ，并且 (ii) **无挠**， $\Gamma^\lambda{}_{\mu\nu}=\Gamma^\lambda{}_{\nu\mu}$ 。它就是 **列维-奇维塔联络**，其分量为克里斯托费尔符号
>
> $$
> \Gamma^\lambda{}_{\mu\nu}=\tfrac12 g^{\lambda\sigma}\big(\partial_\mu g_{\sigma\nu}+\partial_\nu g_{\sigma\mu}-\partial_\sigma g_{\mu\nu}\big).
> $$

*证明（存在性与唯一性合并——Koszul 技巧）。*
1. 假设这样的 $\nabla$ 存在，系数为 $\Gamma^\lambda{}_{\mu\nu}$ ，则由与度量相容有 $\nabla_\mu g_{\nu\rho}=\partial_\mu g_{\nu\rho}-\Gamma^\sigma{}_{\mu\nu}g_{\sigma\rho}-\Gamma^\sigma{}_{\mu\rho}g_{\nu\sigma}=0$ （这只是把协变导数公式作用于 $g$ ）。
2. 把同一方程作指标循环置换写出：
   $\partial_\mu g_{\nu\rho}=\Gamma^\sigma{}_{\mu\nu}g_{\sigma\rho}+\Gamma^\sigma{}_{\mu\rho}g_{\nu\sigma}$ (A)，
   $\partial_\nu g_{\rho\mu}=\Gamma^\sigma{}_{\nu\rho}g_{\sigma\mu}+\Gamma^\sigma{}_{\nu\mu}g_{\rho\sigma}$ (B)，
   $\partial_\rho g_{\mu\nu}=\Gamma^\sigma{}_{\rho\mu}g_{\sigma\nu}+\Gamma^\sigma{}_{\rho\nu}g_{\mu\sigma}$ (C)。
3. 计算 (A)+(B)−(C)。利用对称性 $\Gamma^\sigma{}_{\mu\nu}=\Gamma^\sigma{}_{\nu\mu}$ （无挠）以及 $g$ 的对称性，各项成对相消，只剩下两份相等的 $\Gamma^\sigma{}_{\mu\nu}g_{\sigma\rho}$ ：
   $\partial_\mu g_{\nu\rho}+\partial_\nu g_{\rho\mu}-\partial_\rho g_{\mu\nu}=2\,\Gamma^\sigma{}_{\mu\nu}g_{\sigma\rho}$ 。
4. 两边与 $\tfrac12 g^{\rho\lambda}$ 缩并（因 $g$ 非退化，故 $g^{\rho\lambda}$ 存在且 $g^{\rho\lambda}g_{\sigma\rho}=\delta^\lambda_\sigma$ ）：这分离出 $\Gamma^\lambda{}_{\mu\nu}=\tfrac12 g^{\lambda\sigma}(\partial_\mu g_{\sigma\nu}+\partial_\nu g_{\sigma\mu}-\partial_\sigma g_{\mu\nu})$ 。
5. 第 4 步表明，*若* 一个与度量相容的无挠联络存在，则它被迫具有这些系数——唯一性。反之，用此公式定义 $\Gamma$ 并逆转上述代数运算，便验证 $\nabla g=0$ 及对称性，给出存在性。该构造处处都未用到号差的符号，因此在洛伦兹号差下逐字成立。 $\blacksquare$

> **定义——测地线。** 一条曲线 $x^\mu(\lambda)$ 称为 **测地线**，若其切向量沿自身被平行移动： $\nabla_{\dot x}\dot x=0$ 。用分量，以 $\dot x^\mu=dx^\mu/d\lambda$ ，
>
> $$
> \frac{d^2x^\lambda}{d\lambda^2}+\Gamma^\lambda{}_{\mu\nu}\frac{dx^\mu}{d\lambda}\frac{dx^\nu}{d\lambda}=0.
> $$
>
> 使该式成立的参量（右端不出现额外项 $f(\lambda)\dot x^\lambda$ ）称为 **仿射** 参量；固有时 $\tau$ 是类时测地线的仿射参量。

这就是 **测地线方程**。我们现在证明它 *既* 是"最直"曲线（协变加速度为零），*又* 是"固有时极值"曲线，并且它是自由下落的方程。

#### 测地线使固有时取极值

> **断言。** 类时测地线使固有时泛函 $\tau[x]=\int\sqrt{-g_{\mu\nu}\dot x^\mu\dot x^\nu}\,d\lambda$ 取极值。

*证明。*
1. 对能量型泛函 $S=\tfrac12\int g_{\mu\nu}\dot x^\mu\dot x^\nu\,d\lambda$ 取极值更为简洁，其临界点（取仿射参量）与 $\tau$ 的临界点一致；我们使用 $S$ ，之后再指出仿射性。
2. $L=\tfrac12 g_{\mu\nu}\dot x^\mu\dot x^\nu$ 的欧拉–拉格朗日方程是 $\frac{d}{d\lambda}\frac{\partial L}{\partial\dot x^\lambda}-\frac{\partial L}{\partial x^\lambda}=0$ （来自单变量变分法的标准变分恒等式）。
3. 计算 $\frac{\partial L}{\partial\dot x^\lambda}=g_{\lambda\nu}\dot x^\nu$ 和 $\frac{\partial L}{\partial x^\lambda}=\tfrac12\partial_\lambda g_{\mu\nu}\dot x^\mu\dot x^\nu$ 。
4. 则由乘积法则与链式法则有 $\frac{d}{d\lambda}(g_{\lambda\nu}\dot x^\nu)=g_{\lambda\nu}\ddot x^\nu+\partial_\mu g_{\lambda\nu}\dot x^\mu\dot x^\nu$ 。
5. 相减： $g_{\lambda\nu}\ddot x^\nu+\partial_\mu g_{\lambda\nu}\dot x^\mu\dot x^\nu-\tfrac12\partial_\lambda g_{\mu\nu}\dot x^\mu\dot x^\nu=0$ 。把中间项在 $\mu\nu$ 上对称化（因 $\dot x^\mu\dot x^\nu$ 对称，故允许）： $\partial_\mu g_{\lambda\nu}\dot x^\mu\dot x^\nu=\tfrac12(\partial_\mu g_{\lambda\nu}+\partial_\nu g_{\lambda\mu})\dot x^\mu\dot x^\nu$ 。
6. 括号变成 $\tfrac12(\partial_\mu g_{\lambda\nu}+\partial_\nu g_{\lambda\mu}-\partial_\lambda g_{\mu\nu})\dot x^\mu\dot x^\nu$ ，由克里斯托费尔公式这恰是 $g_{\lambda\sigma}\Gamma^\sigma{}_{\mu\nu}\dot x^\mu\dot x^\nu$ 。
7. 于是 $g_{\lambda\nu}\ddot x^\nu+g_{\lambda\sigma}\Gamma^\sigma{}_{\mu\nu}\dot x^\mu\dot x^\nu=0$ 。与 $g^{\rho\lambda}$ 缩并得 $\ddot x^\rho+\Gamma^\rho{}_{\mu\nu}\dot x^\mu\dot x^\nu=0$ ——测地线方程。 $\blacksquare$

#### 测地线 = 自由下落

由 EEP（s0），一个自由下落的粒子是局域惯性的：在 $p$ 处的局域惯性坐标中我们有 $\Gamma^\lambda{}_{\mu\nu}(p)=0$ ，故测地线方程化为 $\ddot x^\lambda=0$ ——匀速直线运动，恰是牛顿第一定律对无力物体的陈述。方程 $\nabla_{\dot x}\dot x=0$ 是"无力"的坐标无关陈述，而 $\Gamma$ 项是仅因坐标非惯性而出现的表观"引力"。自由下落就是测地运动。

> **算例——以球面上的测地线作为合理性检验。** 虽属黎曼情形，圆 2 维球面让这套机器具体起来。以 $ds^2=d\theta^2+\sin^2\theta\,d\phi^2$ ，非零克里斯托费尔符号为 $\Gamma^\theta{}_{\phi\phi}=-\sin\theta\cos\theta$ 与 $\Gamma^\phi{}_{\theta\phi}=\cot\theta$ 。测地线方程由大圆求解，例如赤道 $\theta=\pi/2$ （此时 $\Gamma^\theta{}_{\phi\phi}=0$ 且 $\ddot\phi=0$ ）。这确认测地线是度量所允许的"最直"曲线。

<a id="s4"></a>
### 曲率——黎曼、里奇、标量与外尔张量；缩并的比安基恒等式（推导）

曲率度量协变导数不可交换的程度——等价地，平行移动的路径依赖性，即 s0 的潮汐场。

> **定义——黎曼曲率张量。** 对向量场，定义 $R(X,Y)Z=\nabla_X\nabla_Y Z-\nabla_Y\nabla_X Z-\nabla_{[X,Y]}Z$ 。在坐标基中（其中 $[\partial_\mu,\partial_\nu]=0$ ）其分量为
>
> $$
> R^\rho{}_{\sigma\mu\nu}=\partial_\mu\Gamma^\rho{}_{\nu\sigma}-\partial_\nu\Gamma^\rho{}_{\mu\sigma}+\Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}-\Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}.
> $$

为看出这是协变导数的对易子，在一个向量 $V^\rho$ 上计算：
$$
(\nabla_\mu\nabla_\nu-\nabla_\nu\nabla_\mu)V^\rho=R^\rho{}_{\sigma\mu\nu}V^\sigma.
$$
这个恒等式—— $V$ 的二阶协变导数相差一个张量乘 $V$ ——是最简洁的定义：曲率是交换 $\nabla$ 们的障碍。

#### 黎曼张量的对称性

降下第一个指标， $R_{\rho\sigma\mu\nu}=g_{\rho\lambda}R^\lambda{}_{\sigma\mu\nu}$ ，列维-奇维塔黎曼张量满足：
- **后一对反对称：** $R_{\rho\sigma\mu\nu}=-R_{\rho\sigma\nu\mu}$ （由定义显然）。
- **前一对反对称：** $R_{\rho\sigma\mu\nu}=-R_{\sigma\rho\mu\nu}$ （来自与度量相容）。
- **对换对称：** $R_{\rho\sigma\mu\nu}=R_{\mu\nu\rho\sigma}$ 。
- **第一（代数）比安基恒等式：** $R_{\rho[\sigma\mu\nu]}=0$ ，即 $R_{\rho\sigma\mu\nu}+R_{\rho\mu\nu\sigma}+R_{\rho\nu\sigma\mu}=0$ 。

这些把 $n=4$ 时的 $n^4=256$ 个分量削减到 $20$ 个独立分量。

> **定义——里奇张量、标量曲率、爱因斯坦张量。** 把黎曼张量在其第一与第三指标上缩并：
>
> $$
> R_{\mu\nu}=R^\lambda{}_{\mu\lambda\nu},\qquad R=g^{\mu\nu}R_{\mu\nu},\qquad G_{\mu\nu}=R_{\mu\nu}-\tfrac12 R\,g_{\mu\nu}.
> $$
>
> $R_{\mu\nu}$ 是 **里奇张量**（对称， $R_{\mu\nu}=R_{\nu\mu}$ ，来自对换对称）， $R$ 是 **标量曲率**， $G_{\mu\nu}$ 是 **爱因斯坦张量**。

> **定义——外尔张量。** **外尔张量** $C_{\rho\sigma\mu\nu}$ 是黎曼张量的完全无迹部分：它是唯一的组合
>
> $$
> C_{\rho\sigma\mu\nu}=R_{\rho\sigma\mu\nu}-\big(g_{\rho[\mu}R_{\nu]\sigma}-g_{\sigma[\mu}R_{\nu]\rho}\big)+\tfrac13 R\,g_{\rho[\mu}g_{\nu]\sigma}
> $$
>
> （在 $n=4$ 时）且其所有单次缩并均为零。黎曼张量分裂为 **里奇部分（通过 s6 由物质设定）加上外尔部分（自由引力场——潮汐畸变、引力波）。**

#### 第二（微分）比安基恒等式及其缩并

> **定理（第二比安基恒等式）。** $\nabla_{[\lambda}R_{\rho\sigma]\mu\nu}=0$ ，即 $\nabla_\lambda R_{\rho\sigma\mu\nu}+\nabla_\rho R_{\sigma\lambda\mu\nu}+\nabla_\sigma R_{\lambda\rho\mu\nu}=0$ 。

*证明。*
1. 在一点 $p$ 处的局域惯性（法）坐标中工作，那里 $\Gamma^\lambda{}_{\mu\nu}(p)=0$ （这种坐标的存在由微分几何指南给出）。在那里 $\nabla=\partial$ *在 $p$ 处*，且黎曼张量中的二次 $\Gamma\Gamma$ 项消失，余下 $R^\rho{}_{\sigma\mu\nu}=\partial_\mu\Gamma^\rho{}_{\nu\sigma}-\partial_\nu\Gamma^\rho{}_{\mu\sigma}$ 。
2. 求导： $\nabla_\lambda R^\rho{}_{\sigma\mu\nu}(p)=\partial_\lambda R^\rho{}_{\sigma\mu\nu}(p)=\partial_\lambda\partial_\mu\Gamma^\rho{}_{\nu\sigma}-\partial_\lambda\partial_\nu\Gamma^\rho{}_{\mu\sigma}$ （ $\partial\Gamma$ 项在一次求导后存留； $\Gamma\partial\Gamma$ 项因 $\Gamma(p)=0$ 而消失）。
3. 在 $[\lambda\mu\nu]$ 上反对称化。每一项都是 $\Gamma$ 的一个二阶偏导数；由于偏导数可交换，对求导所在的三个指标位反对称化便使该和为零： $\partial_{[\lambda}\partial_\mu\Gamma^\rho{}_{\nu]\sigma}=0$ 。
4. 因此在 $p$ 处 $\nabla_{[\lambda}R^\rho{}_{|\sigma|\mu\nu]}=0$ 。两边都是张量且 $p$ 是任意的，故该恒等式处处成立。（一个张量方程若在某一坐标系下于一点成立，则在所有坐标系下成立。） $\blacksquare$

现在到了用于寻找场方程的关键收获。

> **定理（缩并的比安基恒等式）。** $\nabla^\mu G_{\mu\nu}=0$ ，其中 $G_{\mu\nu}=R_{\mu\nu}-\tfrac12 R g_{\mu\nu}$ 。

*证明。*
1. 从第二比安基恒等式的形式 $\nabla_\lambda R_{\rho\sigma\mu\nu}+\nabla_\mu R_{\rho\sigma\nu\lambda}+\nabla_\nu R_{\rho\sigma\lambda\mu}=0$ 出发（利用后一对反对称对反对称化陈述的重标记）。
2. 与 $g^{\rho\mu}$ 缩并。由于 $\nabla g=0$ ， $g^{\rho\mu}$ 可穿过 $\nabla$ ，而升起第一个指标只是 $g^{\rho\mu}R_{\rho\sigma\nu\lambda}=R^\mu{}_{\sigma\nu\lambda}$ 。把它应用于全部三项：
   - 第一项： $g^{\rho\mu}R_{\rho\sigma\mu\nu}=R^\mu{}_{\sigma\mu\nu}=R_{\sigma\nu}$ （里奇，第一与第三指标缩并）。
   - 第二项： $g^{\rho\mu}R_{\rho\sigma\nu\lambda}=R^\mu{}_{\sigma\nu\lambda}$ （保留自由指标 $\mu$ ）。
   - 第三项： $g^{\rho\mu}R_{\rho\sigma\lambda\mu}=R^\mu{}_{\sigma\lambda\mu}=-R^\mu{}_{\sigma\mu\lambda}=-R_{\sigma\lambda}$ ，用到后一对反对称性 $R_{\rho\sigma\lambda\mu}=-R_{\rho\sigma\mu\lambda}$ 。

   这给出 $\nabla_\lambda R_{\sigma\nu}+\nabla_\mu R^\mu{}_{\sigma\nu\lambda}-\nabla_\nu R_{\sigma\lambda}=0$ 。
3. 再次与 $g^{\sigma\nu}$ 缩并。利用 $g^{\sigma\nu}R_{\sigma\nu}=R$ ； $g^{\sigma\nu}\nabla_\nu R_{\sigma\lambda}=\nabla^\sigma R_{\sigma\lambda}=\nabla^\mu R_{\mu\lambda}$ ；以及 $g^{\sigma\nu}R^\mu{}_{\sigma\nu\lambda}=-R^\mu{}_\lambda$ （黎曼的第二与第三指标缩并给出负的里奇，由第一对反对称性 $R_{\mu\sigma\nu\lambda}=-R_{\sigma\mu\nu\lambda}$ ）：
   $\nabla_\lambda R-\nabla_\mu R^\mu{}_\lambda-\nabla^\mu R_{\mu\lambda}=0$ ，即相等的中间项与末项合并给出 $\nabla_\lambda R-2\nabla^\mu R_{\mu\lambda}=0$ 。
4. 改写： $\nabla^\mu R_{\mu\lambda}=\tfrac12\nabla_\lambda R=\tfrac12\nabla^\mu(g_{\mu\lambda}R)$ （利用 $\nabla g=0$ 把 $g$ 拉入内部）。
5. 因此 $\nabla^\mu\big(R_{\mu\lambda}-\tfrac12 g_{\mu\lambda}R\big)=\nabla^\mu G_{\mu\lambda}=0$ 。 $\blacksquare$

> **为何这是关键支点。** 爱因斯坦张量 *恒等地* 无散——这是一个几何恒等式，而非运动方程。在 s6 中我们令 $G_{\mu\nu}\propto T_{\mu\nu}$ ；恒等式 $\nabla^\mu G_{\mu\nu}=0$ 于是 *迫使* $\nabla^\mu T_{\mu\nu}=0$ ，即能量与动量的局域守恒。几何免费地把守恒内建其中。

> **算例——一个常曲率空间。** 对半径为 $a$ 的圆 2 维球面， $R_{\theta\phi\theta\phi}=a^2\sin^2\theta$ 给出里奇 $R_{\mu\nu}=\tfrac{1}{a^2}g_{\mu\nu}$ 以及标量 $R=2/a^2>0$ 。正曲率：邻近的测地线相互收敛，与地球仪上经线在赤道处的收敛相符。

<a id="s5"></a>
### 测地偏离、潮汐力与雅可比场

我们现在把 s0 的断言精确化：潮汐效应——引力中无法被变换消去的那部分——*就是* 曲率。

> **设置。** 考虑一族光滑的单参数测地线 $x^\mu(\tau,s)$ ：对每个固定的 $s$ ， $\tau\mapsto x^\mu(\tau,s)$ 是一条测地线。令 $u^\mu=\partial x^\mu/\partial\tau$ 为切向量（四速度）， $\xi^\mu=\partial x^\mu/\partial s$ 为连接相邻测地线的 **偏离向量**。 $\xi$ 度量两个无穷接近的自由下落者之间的间隔。

> **定理（测地偏离 / 雅可比方程）。** 偏离向量服从
>
> $$
> \frac{D^2\xi^\mu}{d\tau^2}=-R^\mu{}_{\nu\rho\sigma}\,u^\nu\xi^\rho u^\sigma,
> $$
>
> 其中 $\tfrac{D}{d\tau}=\nabla_u$ 是沿测地线的协变导数。解 $\xi$ 称为 **雅可比场**。

*证明。*
1. 由于 $\tau$ 与 $s$ 是该族上的坐标，坐标向量场对易： $[u,\xi]=0$ ，故 $\nabla_u\xi=\nabla_\xi u$ （无挠联络： $\nabla_u\xi-\nabla_\xi u=[u,\xi]=0$ ）。
2. 由第 1 步计算 $\frac{D^2\xi}{d\tau^2}=\nabla_u\nabla_u\xi=\nabla_u\nabla_\xi u$ 。
3. 用曲率定义 $\nabla_u\nabla_\xi u-\nabla_\xi\nabla_u u=R(u,\xi)u+\nabla_{[u,\xi]}u$ 。由于 $[u,\xi]=0$ ，最后一项消失： $\nabla_u\nabla_\xi u=\nabla_\xi\nabla_u u+R(u,\xi)u$ 。
4. 但每条曲线都是测地线，故 $\nabla_u u=0$ ；因此 $\nabla_\xi\nabla_u u=0$ 。
5. 于是 $\frac{D^2\xi}{d\tau^2}=R(u,\xi)u$ 。按我们的约定， $R(X,Y)Z$ 的 $\mu$ 分量为 $R^\mu{}_{\nu\rho\sigma}Z^\nu X^\rho Y^\sigma$ ，故取 $X=u$ 、 $Y=\xi$ 、 $Z=u$ 得 $[R(u,\xi)u]^\mu=R^\mu{}_{\nu\rho\sigma}u^\nu u^\rho\xi^\sigma$ 。现用后一对反对称性 $R^\mu{}_{\nu\rho\sigma}=-R^\mu{}_{\nu\sigma\rho}$ 并交换哑指标 $\rho\leftrightarrow\sigma$ ： $R^\mu{}_{\nu\rho\sigma}u^\nu u^\rho\xi^\sigma=-R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma$ 。因此 $\frac{D^2\xi^\mu}{d\tau^2}=-R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma$ ，即带负号的方框形式。 $\blacksquare$

#### 潮汐力

右端是相对论性的 **潮汐力**。两个自由下落的粒子，各自 *不受任何力*，却仍以由黎曼张量设定的速率彼此相对加速。这是引力的不变内容：在 *单个* 自由下落参考系中你感觉失重（你可以在你所在处令 $\Gamma=0$ ），但你 *无法* 令二阶导数 $R$ 为零，故你仍能探测到你的邻居被"拉面条"化。

> **算例——重新得到牛顿潮汐。** 对一个弱静态场，其度量为 $g_{00}=-(1+2\Phi)$ （s7），相关的曲率分量为 $R^i{}_{0j0}=\partial_i\partial_j\Phi$ 。偏离方程变成 $\frac{d^2\xi^i}{dt^2}=-\partial_i\partial_j\Phi\,\xi^j$ ——恰是牛顿潮汐方程，其中潮汐张量是势的黑塞矩阵。对一个点质量 $\Phi=-GM/r$ ，这给出沿 $r$ 的熟悉拉伸以及横向于它的挤压。曲率 *就是* 潮汐张量。

> **陷阱。** "自由下落抵消引力"仅在逐点且到一阶时为真。在任何有限区域内潮汐项都存留，这正是为何电梯思想实验（s0）被限制在一个 *小* 实验室内。雅可比场还探测 **共轭点**（在那里一个非平凡的雅可比场在两点处为零），它是奇点定理（s11）背后聚焦论证的核心。

## C 部分 · 动力学：场方程及其首批推论

<a id="s6"></a>
### 爱因斯坦场方程——由爱因斯坦–希尔伯特作用量导出（完整变分），以及 $T_{\mu\nu}$ 的角色

我们现在写下确定几何的定律。最简洁的途径是变分的：假设最简单的广义协变作用量并使其取极值。

> **定义——爱因斯坦–希尔伯特作用量。** 以物质拉格朗日密度 $\mathcal{L}_m$ ，
>
> $$
> S=\frac{1}{2\kappa}\int R\,\sqrt{-g}\;d^4x+\int \mathcal{L}_m\,\sqrt{-g}\;d^4x,\qquad \kappa=8\pi G,
> $$
>
> 其中 $R$ 是标量曲率， $\sqrt{-g}\,d^4x$ 是不变体积（高级张量分析）。我们关于逆度量 $g^{\mu\nu}$ 变分 $S$ 并要求 $\delta S=0$ 。

我们需要三个变分引理。全程中， $\delta$ 表示对场 $g$ 的变分。

> **引理 1（ $\sqrt{-g}$ 的变分）。** $\delta\sqrt{-g}=-\tfrac12\sqrt{-g}\,g_{\mu\nu}\,\delta g^{\mu\nu}$ 。

*证明。* 雅可比公式给出 $\delta g=\delta\det(g_{\mu\nu})=g\,g^{\mu\nu}\delta g_{\mu\nu}$ 。由 $g_{\mu\nu}g^{\nu\rho}=\delta_\mu^\rho$ ，变分给出 $g^{\mu\nu}\delta g_{\mu\nu}=-g_{\mu\nu}\delta g^{\mu\nu}$ 。于是 $\delta\sqrt{-g}=\frac{-1}{2\sqrt{-g}}\delta g=\frac{-1}{2\sqrt{-g}}\,g\,g^{\mu\nu}\delta g_{\mu\nu}=\tfrac12\sqrt{-g}\,g^{\mu\nu}\delta g_{\mu\nu}=-\tfrac12\sqrt{-g}\,g_{\mu\nu}\delta g^{\mu\nu}$ ，其中用到 $g/\sqrt{-g}=-\sqrt{-g}$ 。 $\blacksquare$

> **引理 2（里奇张量的变分——帕拉蒂尼恒等式）。** $\delta R_{\mu\nu}=\nabla_\lambda(\delta\Gamma^\lambda{}_{\mu\nu})-\nabla_\nu(\delta\Gamma^\lambda{}_{\lambda\mu})$ 。

*证明。*
1. 尽管 $\Gamma$ 不是张量，两个联络之 *差* $\delta\Gamma^\lambda{}_{\mu\nu}$ 是张量（变换律中非张量性的非齐次部分在作差时相消）。
2. 变分 $R^\rho{}_{\mu\lambda\nu}=\partial_\lambda\Gamma^\rho{}_{\nu\mu}-\partial_\nu\Gamma^\rho{}_{\lambda\mu}+\Gamma\Gamma-\Gamma\Gamma$ 。在一点处的法坐标中（那里 $\Gamma=0$ ， $\nabla=\partial$ ） $\Gamma\Gamma$ 的变分消失，且 $\delta R^\rho{}_{\mu\lambda\nu}=\partial_\lambda\delta\Gamma^\rho{}_{\nu\mu}-\partial_\nu\delta\Gamma^\rho{}_{\lambda\mu}=\nabla_\lambda\delta\Gamma^\rho{}_{\nu\mu}-\nabla_\nu\delta\Gamma^\rho{}_{\lambda\mu}$ 。
3. 两边都是张量，故在所有参考系中成立。缩并 $\rho=\lambda$ 得 $\delta R_{\mu\nu}=\nabla_\lambda\delta\Gamma^\lambda{}_{\nu\mu}-\nabla_\nu\delta\Gamma^\lambda{}_{\lambda\mu}$ 。 $\blacksquare$

> **引理 3（里奇变分项是一个全散度）。** 对某个向量 $v^\lambda$ 有 $g^{\mu\nu}\delta R_{\mu\nu}=\nabla_\lambda v^\lambda$ ，故积分为一个边界项。

*证明。* 由引理 2， $g^{\mu\nu}\delta R_{\mu\nu}=g^{\mu\nu}\nabla_\lambda\delta\Gamma^\lambda{}_{\mu\nu}-g^{\mu\nu}\nabla_\nu\delta\Gamma^\lambda{}_{\lambda\mu}$ 。由于 $\nabla g=0$ ，把 $g^{\mu\nu}$ 拉入内部： $=\nabla_\lambda(g^{\mu\nu}\delta\Gamma^\lambda{}_{\mu\nu})-\nabla_\nu(g^{\mu\nu}\delta\Gamma^\lambda{}_{\lambda\mu})=\nabla_\lambda v^\lambda$ ，其中 $v^\lambda=g^{\mu\nu}\delta\Gamma^\lambda{}_{\mu\nu}-g^{\lambda\nu}\delta\Gamma^\mu{}_{\mu\nu}$ 。由协变散度定理， $\int\nabla_\lambda v^\lambda\sqrt{-g}\,d^4x$ 是一个边界积分，对紧支集的变分它为零。 $\blacksquare$

#### 完整变分

1. 把引力部分写为 $S_g=\frac{1}{2\kappa}\int g^{\mu\nu}R_{\mu\nu}\sqrt{-g}\,d^4x$ 。对三个因子 $g^{\mu\nu}$ 、 $R_{\mu\nu}$ 、 $\sqrt{-g}$ 用乘积法则变分：
   $$
   \delta S_g=\frac{1}{2\kappa}\int\Big(R_{\mu\nu}\sqrt{-g}\,\delta g^{\mu\nu}+g^{\mu\nu}\sqrt{-g}\,\delta R_{\mu\nu}+R\,\delta\sqrt{-g}\Big)d^4x.
   $$
2. 中间项由引理 3 消失（边界项，对紧支集变分舍去）。
3. 末项由引理 1 为 $R\,\delta\sqrt{-g}=-\tfrac12 R\,g_{\mu\nu}\sqrt{-g}\,\delta g^{\mu\nu}$ 。
4. 合并存留项：
   $$
   \delta S_g=\frac{1}{2\kappa}\int\Big(R_{\mu\nu}-\tfrac12 R\,g_{\mu\nu}\Big)\sqrt{-g}\,\delta g^{\mu\nu}\,d^4x=\frac{1}{2\kappa}\int G_{\mu\nu}\sqrt{-g}\,\delta g^{\mu\nu}\,d^4x.
   $$
5. 物质部分通过 $\mathcal{L}_m$ 的变分定义 **能量–动量张量**：
   $$
   T_{\mu\nu}\equiv-\frac{2}{\sqrt{-g}}\frac{\delta(\sqrt{-g}\,\mathcal{L}_m)}{\delta g^{\mu\nu}},\qquad\text{所以}\qquad \delta S_m=-\tfrac12\int T_{\mu\nu}\sqrt{-g}\,\delta g^{\mu\nu}\,d^4x.
   $$
6. 对 *任意* $\delta g^{\mu\nu}$ 令 $\delta S=\delta S_g+\delta S_m=0$ 迫使被积函数为零（变分法基本引理）：
   $$
   \frac{1}{2\kappa}G_{\mu\nu}-\tfrac12 T_{\mu\nu}=0\;\Longrightarrow\; G_{\mu\nu}=\kappa\,T_{\mu\nu}.
   $$

> **爱因斯坦场方程。** 以 $\kappa=8\pi G$ （恢复 $c$ 后， $\kappa=8\pi G/c^4$ ）：
>
> $$
> G_{\mu\nu}=R_{\mu\nu}-\tfrac12 R\,g_{\mu\nu}=8\pi G\,T_{\mu\nu}.
> $$
>
> 向拉格朗日量添加一个常数 $\Lambda$ （ $R\to R-2\Lambda$ ）给出带 **宇宙学常数** 的版本： $G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G\,T_{\mu\nu}$ 。

#### $T_{\mu\nu}$ 的角色与内建的守恒

$T_{\mu\nu}$ 是源： $T_{00}$ 是能量密度， $T_{0i}$ 是动量密度（能流）， $T_{ij}$ 是应力（对角线上为压强）。对一个静止能量密度为 $\rho$ 、压强为 $p$ 、四速度为 $u^\mu$ 的 **理想流体**：
$$
T_{\mu\nu}=(\rho+p)u_\mu u_\nu+p\,g_{\mu\nu}.
$$
把缩并的比安基恒等式 $\nabla^\mu G_{\mu\nu}=0$ （s4）作用于场方程便得到
$$
\nabla^\mu T_{\mu\nu}=0,
$$
即能量–动量的局域守恒——它是几何的 *推论*，而非一个额外的假设。这正是作用量途径正确的深层原因： $S$ 的微分同胚不变性同时蕴含比安基恒等式与守恒律。

> **算例——方程计数。** $G_{\mu\nu}=8\pi G\,T_{\mu\nu}$ 是一个对称的 $4\times4$ 方程组：10 个方程。4 个缩并的比安基恒等式把独立的动力学方程减到 6 个，恰与固定 4 个坐标（规范）自由度后剩下的 6 个度量分量相匹配。正是这种平衡使初值问题适定（s11）。

> **陷阱。** 迹反转形式常更顺手：对 $G_{\mu\nu}=8\pi G\,T_{\mu\nu}$ 取迹给出 $-R=8\pi G\,T$ （其中 $T=g^{\mu\nu}T_{\mu\nu}$ ，用到 $g^{\mu\nu}g_{\mu\nu}=4$ ），故 $R_{\mu\nu}=8\pi G(T_{\mu\nu}-\tfrac12 T g_{\mu\nu})$ 。**在真空中**（ $T_{\mu\nu}=0$ ）这读作 $R_{\mu\nu}=0$ ——*而非* $R_{\rho\sigma\mu\nu}=0$ 。真空时空是里奇平坦的，但一般而言是弯曲的（其外尔张量，s4，携带引力场）。忘记这一点是最常见的广义相对论错误。

<a id="s7"></a>
### 牛顿极限与线性化引力；引力波（推导波动方程）

一个正确的引力理论在场弱且运动慢时必须重现牛顿理论，而当场并非完全静态时它预言一个新现象——几何中的涟漪。

#### 牛顿极限

> **假设。** (i) 弱场： $g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu}$ ，其中 $|h_{\mu\nu}|\ll1$ ，只保留 $h$ 的一阶。(ii) 慢运动：粒子速度 $\ll1$ ，故 $dx^i/d\tau\ll dx^0/d\tau\approx1$ 。(iii) 静态场： $\partial_0 h_{\mu\nu}=0$ 。

1. 测地线方程 $\ddot x^\mu+\Gamma^\mu{}_{\alpha\beta}\dot x^\alpha\dot x^\beta=0$ 。在慢运动下，求和中只有 $\alpha=\beta=0$ 存留： $\ddot x^i\approx-\Gamma^i{}_{00}(\dot x^0)^2$ 。
2. 到一阶， $\Gamma^i{}_{00}=\tfrac12 g^{i\sigma}(2\partial_0 g_{\sigma0}-\partial_\sigma g_{00})=-\tfrac12\partial_i h_{00}$ （用到静态场 $\partial_0=0$ 以及 $g^{i\sigma}\approx\delta^{i\sigma}$ ）。
3. 故 $\ddot x^i\approx\tfrac12\partial_i h_{00}\,(\dot x^0)^2$ 。以 $\dot x^0\approx1$ 并把坐标时与 $\tau$ 等同，得 $\frac{d^2x^i}{dt^2}=\tfrac12\partial_i h_{00}$ 。
4. 牛顿说 $\frac{d^2x^i}{dt^2}=-\partial_i\Phi$ 。匹配： $h_{00}=-2\Phi$ ，即 $g_{00}=-(1+2\Phi)$ 。
5. 迹反转形式的场方程 $R_{00}=8\pi G(T_{00}-\tfrac12 T\eta_{00})$ ，对非相对论性物质（ $T_{00}=\rho$ ， $T\approx-\rho$ ）给出 $R_{00}=4\pi G\rho$ 。到一阶计算 $R_{00}\approx-\tfrac12\nabla^2 h_{00}=\nabla^2\Phi$ ，我们得到 $\nabla^2\Phi=4\pi G\rho$ ——**泊松方程**。牛顿引力是爱因斯坦引力的静态弱场极限。作用量中的因子 $8\pi G$ 正是为了让这一结果正确而选取的。

#### 线性化引力与波动方程

舍去静态假设但保留 $g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu}$ ，对 $h$ 线性。指标现在用 $\eta$ 升降。

1. 定义 **迹反转扰动** $\bar h_{\mu\nu}=h_{\mu\nu}-\tfrac12\eta_{\mu\nu}h$ ，其中 $h=\eta^{\mu\nu}h_{\mu\nu}$ 。
2. 线性化的爱因斯坦张量为（把 $R_{\mu\nu}$ 展开到一阶的标准但冗长的运算）
   $$
   G_{\mu\nu}^{(1)}=-\tfrac12\Big(\Box\bar h_{\mu\nu}+\eta_{\mu\nu}\partial^\alpha\partial^\beta\bar h_{\alpha\beta}-\partial^\alpha\partial_\nu\bar h_{\mu\alpha}-\partial^\alpha\partial_\mu\bar h_{\nu\alpha}\Big),
   $$
   其中 $\Box=\eta^{\alpha\beta}\partial_\alpha\partial_\beta=-\partial_t^2+\nabla^2$ 是平直的达朗贝尔算子。
3. **规范自由度。** 一个无穷小坐标变换 $x^\mu\to x^\mu+\xi^\mu$ 使 $h_{\mu\nu}\to h_{\mu\nu}-\partial_\mu\xi_\nu-\partial_\nu\xi_\mu$ （线性化的微分同胚）。这正是一个自旋-2 场的规范自由度。选取 $\xi^\mu$ 以施加 **洛伦兹（调和）规范** $\partial^\mu\bar h_{\mu\nu}=0$ ；这总是可能的，因为所需的 $\xi$ 求解 $\Box\xi_\nu=\partial^\mu\bar h_{\mu\nu}$ ，一个可解的波动方程。
4. 在洛伦兹规范中第 2 步里 $\bar h$ 的三个导数项消失，余下 $G^{(1)}_{\mu\nu}=-\tfrac12\Box\bar h_{\mu\nu}$ 。场方程 $G^{(1)}_{\mu\nu}=8\pi G\,T_{\mu\nu}$ 变成
   $$
   \boxed{\;\Box\bar h_{\mu\nu}=-16\pi G\,T_{\mu\nu}\;}
   $$
5. **在真空中**（ $T_{\mu\nu}=0$ ）： $\Box\bar h_{\mu\nu}=0$ ——波动方程。引力以光速 $c$ 作为波传播（因 $\Box$ 的特征速度为 $1$ ）。

> **引力波偏振。** 残余的规范自由度（满足 $\Box\xi=0$ 的变换）让我们进一步施加 **横向无迹（TT）规范**： $\bar h=0$ ， $\bar h_{0\mu}=0$ ， $\partial^j\bar h_{ij}=0$ 。一个沿 $z$ 传播的波于是只有两个独立分量，
>
> $$
> h_{ij}^{TT}=\begin{pmatrix}h_+ & h_\times & 0\\ h_\times & -h_+ & 0\\ 0&0&0\end{pmatrix}\cos\big(\omega(t-z)\big),
> $$
>
> 即 **加** 偏振与 **叉** 偏振。一圈自由检验质量沿正交轴交替被拉伸与挤压——恰是激光干涉仪探测器所测量的。

> **算例——由测地偏离得到两种偏振。** 把 $h^{TT}_{ij}$ 代入偏离方程 $\ddot\xi^i=\tfrac12\ddot h^{TT}_{ij}\xi^j$ 。对单独的 $h_+$ ，位于 $(\xi^x,0)$ 的质量在 $x$ 方向振荡，而位于 $(0,\xi^y)$ 的质量以相反相位在 $y$ 方向振荡：一圈质量变成一个在"高瘦"与"宽扁"之间振荡的椭圆。 $h_\times$ 模式做相同的事，但旋转了 $45^\circ$ 。这是可观测的标志；关于波的其余一切都是纯规范。

## D 部分 · 解：黑洞

<a id="s8"></a>
### 施瓦西解——推导；视界；轨道与近日点进动；光线偏折

第一个也是最重要的精确解是一个静态球对称质量外部的场。

> **拟设。** 静态、球对称、真空。最一般的此类度量可写为
>
> $$
> ds^2=-e^{2\alpha(r)}dt^2+e^{2\beta(r)}dr^2+r^2(d\theta^2+\sin^2\theta\,d\phi^2),
> $$
>
> 带两个未知函数 $\alpha(r),\beta(r)$ （球面上的 $r^2$ 是按面积选取径向坐标：在 $r$ 处的球面面积为 $4\pi r^2$ ）。

*解的推导。*
1. 对此度量计算克里斯托费尔符号，然后计算 $R_{\mu\nu}$ （s3–s4 的一个直接但冗长的应用）。独立的真空方程 $R_{\mu\nu}=0$ 化为：
   $R_{tt}$ 与 $R_{rr}$ 一起给出 $\alpha'+\beta'=0$ ，故 $\alpha+\beta=\text{const}$ ；重标度 $t$ 把该常数设为零，因此 $\beta=-\alpha$ 。
2. 方程 $R_{\theta\theta}=0$ 变成 $e^{2\alpha}(2r\alpha'+1)=1$ ，即 $\frac{d}{dr}\big(r\,e^{2\alpha}\big)=1$ 。
3. 积分第 2 步： $r\,e^{2\alpha}=r-2GM$ ，积分常数记作 $2GM$ ，故 $e^{2\alpha}=1-\frac{2GM}{r}$ 且 $e^{2\beta}=e^{-2\alpha}=\big(1-\frac{2GM}{r}\big)^{-1}$ 。
4. 常数 $M$ 由把牛顿极限 $g_{tt}=-(1+2\Phi)=-(1-2GM/r)$ 与 $\Phi=-GM/r$ （s7）匹配来确定： $M$ 即质量。 $\blacksquare$

> **施瓦西度量。**
>
> $$
> ds^2=-\Big(1-\frac{2GM}{r}\Big)dt^2+\Big(1-\frac{2GM}{r}\Big)^{-1}dr^2+r^2 d\Omega^2,\qquad d\Omega^2=d\theta^2+\sin^2\theta\,d\phi^2.
> $$

> **伯克霍夫定理（陈述）。** 这是 *唯一* 的球对称真空解——球对称性迫使静态性。一个脉动的球对称恒星不发射引力波，且其外部恰是施瓦西的。

#### 视界

在 $r=2GM\equiv r_s$ （**施瓦西半径**）处度量系数发散： $g_{tt}\to0$ ， $g_{rr}\to\infty$ 。这是一个 **坐标奇点**，而非物理奇点——曲率标量 $R_{\rho\sigma\mu\nu}R^{\rho\sigma\mu\nu}=48G^2M^2/r^6$ 在那里有限。曲面 $r=r_s$ 是 **事件视界**：一个光只能向内穿越的类光曲面。真正的奇点在 $r=0$ ，那里曲率标量发散。我们在 s9 中用更好的坐标使视界的正则性显现出来。

#### 轨道与近日点进动

对赤道面（ $\theta=\pi/2$ ）内一条测地线上的有质量粒子，由时间与转动对称性（基灵向量 $\partial_t,\partial_\phi$ ）得到两个守恒量：单位质量的能量 $E=(1-2GM/r)\dot t$ 与角动量 $L=r^2\dot\phi$ ，其中 $\dot{}=d/d\tau$ 。

1. 归一化 $g_{\mu\nu}\dot x^\mu\dot x^\nu=-1$ 在代入 $E,L$ 后给出：
   $$
   \tfrac12\dot r^2+V_{\rm eff}(r)=\tfrac12 E^2,\qquad V_{\rm eff}=\tfrac12\Big(1-\frac{2GM}{r}\Big)\Big(1+\frac{L^2}{r^2}\Big)-\tfrac12.
   $$
2. 展开： $V_{\rm eff}=-\frac{GM}{r}+\frac{L^2}{2r^2}-\frac{GM L^2}{r^3}$ 。前两项是牛顿的；新的 $-GML^2/r^3$ 项是广义相对论修正。
3. 令 $u=1/r$ 并用 $\phi$ 参数化。对轨道方程求导得到
   $$
   \frac{d^2u}{d\phi^2}+u=\frac{GM}{L^2}+3GM\,u^2.
   $$
   $3GMu^2$ 项是对牛顿开普勒方程 $u''+u=GM/L^2$ （其解为一个闭合椭圆）的相对论修正。
4. 把 $3GMu^2$ 围绕圆轨道值 $u_0=GM/L^2$ 作微扰处理。该修正使轨道并非在 $\Delta\phi=2\pi$ 之后闭合，而是在 $2\pi/\sqrt{1-6GM/p}\approx2\pi(1+3GM/p)$ 之后闭合，其中半正焦弦 $p=L^2/GM$ 。每轨道近日点进动
   $$
   \Delta\phi_{\rm prec}\approx\frac{6\pi GM}{p}=\frac{6\pi GM}{a(1-e^2)}.
   $$

> **算例——水星。** 以 $M=M_\odot$ ，半长轴 $a=5.79\times10^{10}\,$m，偏心率 $e=0.206$ ，以及 $GM_\odot/c^2=1.48\times10^3\,$m（恢复 $c$ ）： $\Delta\phi=6\pi(1.48\times10^3)/[5.79\times10^{10}(1-0.206^2)]\approx5.0\times10^{-7}\,$rad/轨道。乘以 $\approx415$ 轨道/世纪给出每世纪 $\approx43''$ ——水星近日点长期存在的反常，得到精确解释。

#### 光线偏折

对光（类光测地线）归一化为 $g_{\mu\nu}\dot x^\mu\dot x^\nu=0$ ，这去掉了常数项，给出 $u''+u=3GMu^2$ 。围绕直线 $u_0=\sin\phi/b$ （碰撞参量 $b$ ）微扰，掠过一个质量的光线的总偏转为
$$
\Delta\phi=\frac{4GM}{b}\quad(\text{即 }\frac{4GM}{c^2 b}).
$$

> **算例——掠过太阳的光线。** $b=R_\odot=6.96\times10^8\,$m， $GM_\odot/c^2=1.48\times10^3\,$m： $\Delta\phi=4(1.48\times10^3)/6.96\times10^8=8.5\times10^{-6}\,$rad$=1.75''$ 。这是朴素牛顿"光子作为慢粒子"值的 *两倍*——因子 2 来自空间曲率 $g_{rr}$ ——其 1919 年的日食确认使爱因斯坦闻名于世。

> **陷阱。** 坐标 $r$ *不是* 径向距离；固有径向距离是 $\int(1-2GM/r)^{-1/2}dr$ ，它在视界附近相对于 $\Delta r$ 发散。而 $t$ 是一个远处静态观察者的时间，而非下落者的时间——这导致引力红移以及下落物体在视界处表观的"冻结"。

<a id="s9"></a>
### 黑洞——克鲁斯卡尔–塞凯赖什延拓、克尔度量（概述）以及黑洞力学定律

#### 克鲁斯卡尔–塞凯赖什：极大延拓

施瓦西坐标只覆盖 $r>2GM$ （或只覆盖 $r<2GM$ ）且在视界处失效。为看到完整的时空，我们更换坐标使度量在那里正则。

1. 定义 **乌龟坐标** $r_*=r+2GM\ln\big|\frac{r}{2GM}-1\big|$ ，故 $dr_*=(1-2GM/r)^{-1}dr$ 且在视界处 $r_*\to-\infty$ 。
2. 构造类光坐标 $u=t-r_*$ ， $v=t+r_*$ （常数 $u$/$v$ 是径向光线）。度量变成 $ds^2=-(1-2GM/r)\,du\,dv+r^2d\Omega^2$ ，在视界处（ $1-2GM/r\to0$ ）仍退化。
3. 指数化为 **克鲁斯卡尔坐标** $U=-e^{-u/4GM}$ ， $V=e^{v/4GM}$ （在外部）。则
   $$
   ds^2=-\frac{32G^3M^3}{r}e^{-r/2GM}\,dU\,dV+r^2 d\Omega^2,
   $$
   其中 $r$ 由 $UV=-(\frac{r}{2GM}-1)e^{r/2GM}$ 隐式定义。前因子在 $r=2GM$ （ $UV=0$ ）处有限且非零：视界现在完全正则。
4. $(U,V)$ 平面揭示四个区域：我们的外部（I）、未来视界后的黑洞内部（II，含 $UV=1$ 处的 $r=0$ 奇点）、第二个渐近外部（III）以及一个白洞区域（IV）。这就是 **极大延拓** 的施瓦西时空； $r=0$ 处的曲率奇点是区域 II 未来中的一个 *类空* 曲面——一旦进入，撞上它就如同到达明天一样不可避免。

#### 克尔度量（概述）

真实的黑洞自旋。具有质量 $M$ 与角动量 $J=Ma$ 的唯一稳态、轴对称、渐近平直的真空解是 **克尔度量**（玻耶–林奎斯特坐标）：
$$
ds^2=-\Big(1-\frac{2GMr}{\Sigma}\Big)dt^2-\frac{4GMar\sin^2\theta}{\Sigma}dt\,d\phi+\frac{\Sigma}{\Delta}dr^2+\Sigma\,d\theta^2+\Big(r^2+a^2+\frac{2GMa^2r\sin^2\theta}{\Sigma}\Big)\sin^2\theta\,d\phi^2,
$$
其中 $\Sigma=r^2+a^2\cos^2\theta$ ， $\Delta=r^2-2GMr+a^2$ 。关键特征： $\Delta=0$ 处的 **外视界**，即 $r_+=GM+\sqrt{G^2M^2-a^2}$ （要求 $a\le GM$ ——取等时为极端）；视界之外的 **能层**，那里 $g_{tt}>0$ 且没有观察者能保持静止（参考系拖曳是彻底的）；以及可经由彭罗斯过程提取的转动能量。令 $a=0$ 恢复施瓦西解。**无毛定理** 表明稳态黑洞完全由 $(M,J,Q)$ （质量、角动量、电荷）刻画。

#### 黑洞力学四定律

这些热力学的非凡类比把视界的表面引力 $\kappa$ （在视界处把一个粒子保持住所需的、红移到无穷处的加速度）、面积 $A$ 、角速度 $\Omega_H$ 与电荷联系起来。

- **第零定律：** $\kappa$ 在一个稳态黑洞的视界上恒定。（类比：温度在平衡态中均匀。）
- **第一定律：** $dM=\frac{\kappa}{8\pi G}\,dA+\Omega_H\,dJ+\Phi_H\,dQ$ 。（类比： $dE=T\,dS+\dots$ 。）
- **第二定律（霍金面积定理）：** 在任何遵守类光能量条件的经典过程中，总视界面积永不减小， $dA\ge0$ 。（类比： $dS\ge0$ 。）
- **第三定律：** $\kappa=0$ （极端性）无法在有限次操作中达到。

> **热力学的点睛之笔。** 这个类比并非形式上的：霍金的量子计算赋予视界一个真实的温度 $T_H=\frac{\hbar\kappa}{2\pi}$ 与熵 $S=\frac{A}{4G\hbar}$ （贝肯斯坦–霍金熵）。黑洞是真正的热力学对象；面积定律 *就是* 它们的热力学第二定律。

> **算例——太阳质量黑洞。** 对 $M=M_\odot$ ， $r_s=2GM/c^2\approx3\,$km，视界面积 $A=4\pi r_s^2\approx1.1\times10^8\,$m$^2$ ，表面引力 $\kappa=1/(4GM)$ 给出 $T_H\sim6\times10^{-8}\,$K——极其寒冷，因此天体物理黑洞吸收的远多于它辐射的。霍金辐射只对微小（原初）黑洞才重要。

## E 部分 · 宇宙及其边界

<a id="s10"></a>
### 宇宙学——FLRW 度量与弗里德曼方程（推导）

在最大尺度上，观测到宇宙是 **均匀的**（每一点都相同）且 **各向同性的**（每个方向都相同）。这些对称性把度量确定到只差一个函数与一个常数。

> **定义——FLRW 度量。** 弗里德曼–勒梅特–罗伯逊–沃克度量为
>
> $$
> ds^2=-dt^2+a(t)^2\Big[\frac{dr^2}{1-kr^2}+r^2 d\Omega^2\Big],
> $$
>
> 其中 $a(t)$ 是 **标度因子**（空间的相对大小）， $k\in\{-1,0,+1\}$ 设定空间曲率：开放（双曲）、平坦或闭合（球面）。均匀性与各向同性恰好迫使这一形式。

*弗里德曼方程的推导。* 取一个理想流体源 $T_{\mu\nu}=(\rho+p)u_\mu u_\nu+p g_{\mu\nu}$ ，其中 $u^\mu=(1,0,0,0)$ （共动流体）。
1. 计算 FLRW 的非零克里斯托费尔符号：例如 $\Gamma^0{}_{ij}=a\dot a\,\tilde g_{ij}$ ， $\Gamma^i{}_{0j}=\frac{\dot a}{a}\delta^i_j$ ，外加空间的那些，其中 $\tilde g_{ij}$ 是单位标度的空间度量， $\dot{}=d/dt$ 。
2. 由这些，里奇张量的 $00$ 分量是 $R_{00}=-3\frac{\ddot a}{a}$ 。
3. 空间里奇张量给出 $R_{ij}=\big(\frac{\ddot a}{a}+2\frac{\dot a^2}{a^2}+2\frac{k}{a^2}\big)g_{ij}$ ，以及标量曲率 $R=6\big(\frac{\ddot a}{a}+\frac{\dot a^2}{a^2}+\frac{k}{a^2}\big)$ 。
4. $00$ 爱因斯坦方程 $G_{00}=8\pi G\,T_{00}$ ，以 $G_{00}=R_{00}-\tfrac12 R g_{00}=3\big(\frac{\dot a^2}{a^2}+\frac{k}{a^2}\big)$ 与 $T_{00}=\rho$ ，给出 **第一弗里德曼方程**：
   $$
   \Big(\frac{\dot a}{a}\Big)^2=\frac{8\pi G}{3}\rho-\frac{k}{a^2}.
   $$
5. 空间爱因斯坦方程 $G_{ij}=8\pi G T_{ij}$ 与第一个方程结合，消去 $\dot a^2$ ，给出 **第二弗里德曼（加速度）方程**：
   $$
   \frac{\ddot a}{a}=-\frac{4\pi G}{3}(\rho+3p).
   $$
6. 守恒 $\nabla^\mu T_{\mu0}=0$ 给出 **连续性方程** $\dot\rho+3\frac{\dot a}{a}(\rho+p)=0$ （空间膨胀时能量的红移）；它是第一个方程的时间导数与第二个方程的结合，由比安基恒等式保证自洽。 $\blacksquare$

> **解读这些方程。** 哈勃参量是 $H=\dot a/a$ 。第一弗里德曼方程说膨胀率由能量密度与曲率设定。第二个说普通物质（ $\rho>0,p\ge0$ ）*减速* 膨胀，而一个满足 $p<-\rho/3$ 的成分——例如宇宙学常数 $\Lambda$ ，它充当 $\rho_\Lambda=\Lambda/8\pi G$ ， $p_\Lambda=-\rho_\Lambda$ ——*加速* 膨胀。观测到的加速膨胀被归因于这样的"暗能量"。

> **算例——状态方程与标度。** 以 $p=w\rho$ ，连续性方程积分为 $\rho\propto a^{-3(1+w)}$ 。物质（ $w=0$ ）： $\rho\propto a^{-3}$ （按体积稀释）。辐射（ $w=1/3$ ）： $\rho\propto a^{-4}$ （体积加红移）。宇宙学常数（ $w=-1$ ）： $\rho=$ 常数。一个平坦（ $k=0$ ）的物质宇宙于是有 $\dot a^2\propto a^{-1}$ ，解得 $a(t)\propto t^{2/3}$ ——物质主导时期的减速膨胀；一个 $\Lambda$ 主导的平坦宇宙给出 $a\propto e^{Ht}$ ，指数式的德西特膨胀。

> **陷阱。** $a(t)$ 是无量纲的，只有比值才有意义；按惯例令 $a(\text{今天})=1$ 。光的红移是 $1+z=a(\text{现在})/a(\text{发射时})$ ，*而非* 多普勒频移——它是波长被空间本身的膨胀所拉伸。

<a id="s11"></a>
### ADM（初值）表述以及彭罗斯–霍金奇点定理的陈述

#### ADM 分解：作为演化的广义相对论

整体双曲性（s2）让我们把时空切成空间曲面 $\Sigma_t$ ，并把爱因斯坦方程视为时间中的演化——这对广义相对论概念上的"适定性"以及数值相对论都至关重要。

> **定义——ADM（3+1）分解。** 用类空柯西面 $\Sigma_t$ 对 $M$ 进行叶状分层。写
>
> $$
> ds^2=-N^2\,dt^2+\gamma_{ij}\big(dx^i+N^i dt\big)\big(dx^j+N^j dt\big),
> $$
>
> 其中 $\gamma_{ij}$ 是 $\Sigma_t$ 上的 **诱导空间度量**， $N$ 是 **流逝**（法向观察者每单位坐标时的固有时）， $N^i$ 是 **移位**（空间坐标在各切片间如何滑动）。动力学场是 $\gamma_{ij}$ ；其"速度"被编码在 **外曲率** $K_{ij}=\frac{1}{2N}(\dot\gamma_{ij}-D_iN_j-D_jN_i)$ 中，其中 $D$ 是 $\gamma$ 的协变导数。

十个爱因斯坦方程分裂为两组：
- **约束**（不含 $N,N^i$ 的时间导数；它们约束 $\Sigma_t$ 上的初始数据）：
  $$
  \text{哈密顿：}\quad {}^{(3)}R+K^2-K_{ij}K^{ij}=16\pi G\,\rho,\qquad
  \text{动量：}\quad D_j(K^{ij}-\gamma^{ij}K)=8\pi G\,J^i,
  $$
  其中 ${}^{(3)}R$ 是 $\gamma$ 的标量曲率， $K=\gamma^{ij}K_{ij}$ ，而 $\rho,J^i$ 是法向观察者所测量的能量与动量密度。
- **演化方程：** 关于 $\dot\gamma_{ij}$ （ $K$ 的定义）以及 $\dot K_{ij}$ （其余六个爱因斯坦方程）的时间一阶方程。

> **适定的初值问题。** 在 $\Sigma_0$ 上选取满足四个约束的 $(\gamma_{ij},K_{ij})$ ；则流逝与移位是 *自由的规范选择*（它们固定坐标），而演化方程把时空唯一地确定到未来。这就是"几何服从确定性动力学"的严格含义，由 Choquet-Bruhat 定理（真空爱因斯坦方程具有适定的柯西问题）支撑。这四个约束是四个缩并的比安基恒等式（s4）在 3+1 中的投影。

#### 奇点定理

施瓦西与 FLRW 奇点（s8、s10）也许会被当作完美对称性的产物而打发掉。奇点定理表明它们并非如此：在宽泛的、无需对称性的条件下，引力坍缩与宇宙学的过去是 *测地不完备的*——某条测地线无法被延拓到其仿射参量的所有值。

> **关键工具——聚焦与劳赫德胡里方程。** 对一族膨胀率为 $\theta$ （横向体积的分数变化率）的类时测地线，
>
> $$
> \frac{d\theta}{d\tau}=-\tfrac13\theta^2-\sigma_{\mu\nu}\sigma^{\mu\nu}+\omega_{\mu\nu}\omega^{\mu\nu}-R_{\mu\nu}u^\mu u^\nu,
> $$
>
> 带剪切 $\sigma$ 与涡量 $\omega$ 。若引力是吸引的（ $R_{\mu\nu}u^\mu u^\nu\ge0$ ，即 **强能量条件**）且该族无旋（ $\omega=0$ ），则 $\frac{d\theta}{d\tau}\le-\tfrac13\theta^2$ ，这一旦 $\theta$ 为负便迫使 $\theta\to-\infty$ （测地线聚焦到一个焦散/共轭点）于有限固有时内。吸引是无条件的。

> **彭罗斯定理（1965，黑洞）。** 若一个时空是整体双曲的、具有一个非紧的柯西面、满足类光能量条件（对类光 $k$ 有 $R_{\mu\nu}k^\mu k^\nu\ge0$ ）、并含有一个 **陷俘面**——一个闭合 2 维曲面，其向内与向外的类光法向族 *两者* 都在收敛——则该时空是类光测地不完备的：它含有一个奇点。一个陷俘面在坍缩恒星内部形成，故坍缩为奇点是一般性的，而非球对称性的产物。

> **霍金定理（宇宙学）。** 若一个整体双曲的时空满足强能量条件、并在一张柯西面上处处以一个有下界的速率膨胀（ $\theta\ge\theta_0>0$ ），则它是过去类时测地不完备的：在有限固有时之前曾有一个奇点（一次大爆炸）。霍金与彭罗斯把这些合并为单一定理，同时涵盖两种情形。

> **"奇点"意味着什么以及不意味着什么。** 这些定理证明 **测地不完备性**——观察者在有限固有时内耗尽时空——*而非* 某个曲率标量发散（尽管通常确实如此）。它们假设一个 **能量条件**（物质以吸引方式产生引力）与一个 **因果性/整体条件**，并得出不可避免性。它们是存在性定理：它们说一个奇点 *形成*，但不说它的本质。它们深刻的讯息是：经典广义相对论预言了它自身的失效，标志着在它无法描述的奇点处需要一个量子引力理论。

> **算例——当一个能量条件失效时。** 由宇宙学常数驱动的加速宇宙违反强能量条件（ $\rho+3p=\rho-3\rho_\Lambda<0$ ）。这正是为何德西特空间（ $a\propto e^{Ht}$ ，s10）是 *未来* 测地完备的——没有未来奇点——这说明定理的假设是尖锐的：放松吸引，聚焦便可能失效。

---

*本指南把引力从单一的物理原理——所有物体下落方式相同——带到了一个完整的几何理论。等效原理使时空成为一个洛伦兹流形；其因果光锥组织起因与果；列维-奇维塔联络把自由下落化为测地运动；曲率成为不可约的潮汐场；而爱因斯坦–希尔伯特作用量交付了场方程 $G_{\mu\nu}=8\pi G\,T_{\mu\nu}$ ，能量守恒由缩并的比安基恒等式内建其中。从那里出发，经典检验（近日点进动、光线偏折）、引力波、施瓦西与克尔黑洞及其热力学定律、膨胀的 FLRW 宇宙，以及最后的 ADM 演化与奇点定理，全都由诚实的计算随之而来。把这当作一张地图：当一个相对论问题陷入僵局时，回到那两句话——物质弯曲时空，弯曲的时空移动物质——并问情形所诉诸的是哪个张量、哪个对称性或哪个能量条件。*
