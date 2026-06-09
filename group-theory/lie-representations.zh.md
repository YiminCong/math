[English](lie-representations.md) · **中文**

# 李代数表示论，*对称性的分类。*

*这是一门承接群论指南中引入的李代数、并一路推进到单李代数及其不可约表示分类的第二门课程——根系、Dynkin 图、最高权、Weyl 特征标公式——其中每个定义都被写清楚，每条定理都被证明或仔细论证，并且始终把粒子多重态的物理放在视野之内。要牢记的唯一收获：对表示进行分类，就是对自然界所能构造的态多重态进行分类。*

[← 返回全部指南](../README.zh.md)

> **如何阅读本指南。** 唯一的前置要求是 **群论与表示** 指南（[`group-theory.md`](group-theory.md)），它建立了群、*表示*（同态 $\rho:G\to GL(V)$，把群元实现为矩阵）、*李群*（同时也是光滑流形的群，如旋转群）、*李代数*（它们由无穷小生成元构成的切空间），以及对 $\mathfrak{su}(2)$（自旋）的阶梯分析。每当我们用到其中某个事实时，都会用一行字重新陈述，使本指南可以独立阅读。我们假定读者掌握普通代数和一点单变量微积分；一切专门概念——*理想*、*Killing 形式*、*Cartan 子代数*、*根*、*权*、*Dynkin 图*、*Verma 模*、*Weyl 群*、*Casimir*——都会在首次出现时给出定义并用真实数字加以说明。没有任何东西留给读者自行补全；凡是用到外部的硬性输入（李第三定理、Weyl 的酉技巧）我们都会明确指出并解释其内容。凡是物理能带来启发之处我们都会说明，但这是一份**数学**指南：论断都要被证明。

---

## A 部分 — 李代数的结构

<a id="s0"></a>
### 动机：为什么对表示分类就是对可能的粒子多重态分类

**是什么以及为什么。** 在量子力学中，一个物理态是复向量空间中的一个向量 $|\psi\rangle$，而系统的一个连续对称性——旋转、同位旋变换、$SU(3)$ 味对称性——通过一个线性算子作用于态。这些算子的集合构成李群 $G$ 的一个**表示**：一个光滑同态 $\rho:G\to GL(V)$，把每个对称性 $g$ 赋予态空间 $V$ 上的一个可逆矩阵 $\rho(g)$，满足 $\rho(gh)=\rho(g)\rho(h)$。被对称性彼此混合、且无法被拆分成更小这类族的那些态，构成一个**多重态**，在数学上即一个**不可约表示**（没有被每个 $\rho(g)$ 映入自身的真非零子空间的表示）。

在前置指南中确立的两个事实奠定了这里的一切。

第一，使哈密顿量保持不变的对称性，迫使同一多重态中的态**简并**（能量相等）：若 $\rho(g)$ 对所有 $g$ 都与能量算子 $H$ 对易，那么 $H$ 在每个不可约块上以单个标量作用（由 Schur 引理——与不可约表示对易的同态是恒等映射的标量倍）。所以观察到的简并模式*就是*态空间分解为不可约表示的方式。质子—中子的近简并是一个同位旋二重态；八个轻重子是一个 $SU(3)$ 八重态。

第二，在单位元附近，李群由其**李代数** $\mathfrak{g}$ 支配，后者是带括号 $[\,\cdot\,,\cdot\,]$ 的无穷小生成元向量空间，而群的表示微分得到代数的表示（对于单连通群，反过来也成立）。于是看似分析性的问题"哪些矩阵能实现这一对称性？"就变成了纯代数的问题"这个李代数有哪些表示？"那个代数问题有一个*完整而有限的答案*：半单李代数的不可约表示由它们的**最高权**编目，最高权是某个格上的点，而代数本身落入一份短名单（$A_n,B_n,C_n,D_n$ 族和五个例外型）。

所以本指南的口号是精确的，而非诗意的：**对 $\mathfrak{g}$ 的表示分类，就是对一个具有 $\mathfrak{g}$ 对称性的理论所能包含的态多重态分类。** 当 Gell-Mann 把强子排列成八重态和十重态时，他就是在读取 $\mathfrak{su}(3)$ 的不可约表示；重子十重态中那个空着的角落是一个尚未找到粒子的表示位置，而 $\Omega^-$ 填补了它。我们将构建使这类预言成为必然的机制。

> **计划。** A 部分敲定结构理论：哪些李代数是"半单的"（好的那些），以及检测它们的 Killing 形式。B 部分是几何核心：Cartan 子代数、根、Dynkin 图与分类定理。C 部分才是真正的表示论：权、最高权理论、Verma 模、Weyl 特征标公式。D 部分把 $\mathfrak{su}(2)$ 和 $\mathfrak{su}(3)$ 做到底，处理张量积与分支，并以在实验室中标记态的 Casimir 算子收尾。

<a id="s1"></a>
### 再访李代数：结构常数、理想、伴随表示

**是什么以及为什么。** 我们重述前置指南中李代数的定义，并立即发展下文处处要用的三个工具：基展开（*结构常数*）、可以"除掉"的子结构（*理想*），以及一个代数对自身最重要的那个表示（*伴随表示*）。

> **定义 — 李代数。** 域 $\mathbb{F}$ 上的一个**李代数**（我们取 $\mathbb{F}=\mathbb{R}$ 或 $\mathbb{C}$）是一个向量空间 $\mathfrak{g}$，配备一个双线性映射 $[\,\cdot\,,\cdot\,]:\mathfrak{g}\times\mathfrak{g}\to\mathfrak{g}$，即**括号**，对所有 $X,Y,Z\in\mathfrak{g}$ 满足：
> 1. **（反对称性）** $[X,Y]=-[Y,X]$（故 $[X,X]=0$）；
> 2. **（Jacobi 恒等式）** $[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0$。
>
> **子代数**是在括号下封闭的子空间。$\mathfrak{g}$ 的**维数**是它作为向量空间的维数。

激发动机的模型：对矩阵而言，$[X,Y]=XY-YX$（**对易子**）。这显然是双线性且反对称的，而 Jacobi 恒等式是一个直接的展开（每个乘积 $XYZ$ 恰带 $+$ 出现一次、带 $-$ 出现一次，三个一组相消——我们在习题例中验证这一点）。矩阵李群的无穷小生成元构成这样的代数；例如 $\mathfrak{su}(2)$ 是对易子下的无迹反 Hermite $2\times2$ 矩阵。

> **定义 — 结构常数。** 固定 $\mathfrak{g}$ 的一组基 $\{T_a\}_{a=1}^{n}$（$n=\dim\mathfrak{g}$）。由于每个括号 $[T_a,T_b]$ 仍在 $\mathfrak{g}$ 中，它在基中唯一展开：
>
> $$
> [T_a,T_b]=\sum_{c=1}^{n} f_{ab}{}^{c}\,T_c .
> $$
>
> 这些数 $f_{ab}{}^{c}\in\mathbb{F}$ 是**结构常数**。它们编码了整个括号：反对称性迫使 $f_{ab}{}^{c}=-f_{ba}{}^{c}$，而 Jacobi 恒等式变成二次关系 $\sum_e\big(f_{ab}{}^{e}f_{ec}{}^{d}+f_{bc}{}^{e}f_{ea}{}^{d}+f_{ca}{}^{e}f_{eb}{}^{d}\big)=0$，对所有 $a,b,c,d$ 成立。

> **定义 — 理想。** 子空间 $\mathfrak{a}\subseteq\mathfrak{g}$ 是一个**理想**，如果 $[\mathfrak{g},\mathfrak{a}]\subseteq\mathfrak{a}$，即对每个 $X\in\mathfrak{g}$ 和 $A\in\mathfrak{a}$ 有 $[X,A]\in\mathfrak{a}$。（对照前置指南中的*正规子群*：理想恰是你可以"对其取商"的子结构，因为括号下降到商空间 $\mathfrak{g}/\mathfrak{a}$。）

理想是正规子群在李代数中的类比。整个代数 $\mathfrak{g}$ 和零子空间 $\{0\}$ 总是理想（**平凡**理想）。没有其他理想的代数（且 $\dim\mathfrak{g}>1$，括号非零）称为**单**代数——这些就是我们要分类的不可分原子。

> **定义 — 伴随表示。** 对 $X\in\mathfrak{g}$ 定义线性映射 $\mathrm{ad}_X:\mathfrak{g}\to\mathfrak{g}$ 为 $\mathrm{ad}_X(Y)=[X,Y]$。指派 $X\mapsto\mathrm{ad}_X$ 称为**伴随表示**，$\mathrm{ad}:\mathfrak{g}\to\mathfrak{gl}(\mathfrak{g})$，其中 $\mathfrak{gl}(\mathfrak{g})$ 是 $\mathfrak{g}$ 上所有线性映射在对易子下构成的代数。

> **引理 — 伴随表示是李代数同态。** 对所有 $X,Y\in\mathfrak{g}$，$\mathrm{ad}_{[X,Y]}=[\mathrm{ad}_X,\mathrm{ad}_Y]$，其中右边的括号是算子的对易子。

**证明。**
1. 把两边作用于任意 $Z\in\mathfrak{g}$；只需证明它们在每个 $Z$ 上相等（线性映射由其取值确定，依*线性性*）。
2. 左边：$\mathrm{ad}_{[X,Y]}(Z)=[[X,Y],Z]$，依 $\mathrm{ad}$ 的*定义*。
3. 右边：$[\mathrm{ad}_X,\mathrm{ad}_Y](Z)=\mathrm{ad}_X\mathrm{ad}_Y(Z)-\mathrm{ad}_Y\mathrm{ad}_X(Z)=[X,[Y,Z]]-[Y,[X,Z]]$，依*算子对易子的定义*和 $\mathrm{ad}$ 的定义。
4. 把 Jacobi 恒等式写成 $[[X,Y],Z]=[X,[Y,Z]]-[Y,[X,Z]]$（用*反对称性*对最后一项整理三个循环项），便表明第 2 步与第 3 步相等。$\blacksquare$

这个引理表明伴随表示确实是一个表示：它把括号送到对易子，正是李代数同态的定义性质。伴随表示是*根*将要栖身之处（s3）。

**习题例 — $\mathfrak{su}(2)$ 的结构常数与伴随表示。** 取标准生成元 $J_1,J_2,J_3$，满足 $[J_a,J_b]=\sum_c \varepsilon_{abc}J_c$，其中 $\varepsilon_{abc}$ 是全反对称符号（$\varepsilon_{123}=+1$）。故结构常数是 $f_{ab}{}^{c}=\varepsilon_{abc}$。在基 $(J_1,J_2,J_3)$ 中计算 $\mathrm{ad}_{J_3}$：
$$
\mathrm{ad}_{J_3}(J_1)=[J_3,J_1]=J_2,\quad \mathrm{ad}_{J_3}(J_2)=[J_3,J_2]=-J_1,\quad \mathrm{ad}_{J_3}(J_3)=0 .
$$
作为矩阵（列 = $J_1,J_2,J_3$ 的像）：
$$
\mathrm{ad}_{J_3}=\begin{pmatrix}0&-1&0\\ 1&0&0\\ 0&0&0\end{pmatrix}.
$$
这是绕 $3$ 轴旋转的生成元作用在一个 $3$ 维向量上——$\mathfrak{su}(2)$ 的伴随表示就是向量（自旋 $1$）表示，从纯代数恢复了前置指南中的一个事实。我们也来*数值地验证 Jacobi*，在 $(J_1,J_2,J_3)$ 上：$[J_1,[J_2,J_3]]+[J_2,[J_3,J_1]]+[J_3,[J_1,J_2]] = [J_1,J_1]+[J_2,J_2]+[J_3,J_3]=0+0+0=0$。很好。

> **易错点。** 结构常数依赖于所选的基；关于代数的论断（如"$\mathfrak{g}$ 是单的"）绝不可暗中依赖于基。补救之道是构造*不依赖于基*的对象——其中第一个，Killing 形式，就在下面。

<a id="s2"></a>
### 可解、幂零与半单李代数；Killing 形式；Cartan 判据

**是什么以及为什么。** 正如整数分解为素数，李代数分解为构件。一个极端是"完全非单"的代数，它们只由反复求括号、最终归零的运算构成——即**可解**与**幂零**的代数，相当于阿贝尔/三角的类比。另一极端是**半单**代数，它们是单块之和，拥有优美的表示论。我们需要一个可计算的判别法来辨别孰是孰非：**Killing 形式**与 **Cartan 判据**。

> **定义 — 导出列与下中心列。** 令 $\mathfrak{g}^{(0)}=\mathfrak{g}$、$\mathfrak{g}^{(k+1)}=[\mathfrak{g}^{(k)},\mathfrak{g}^{(k)}]$（来自 $\mathfrak{g}^{(k)}$ 中各对元素的所有括号的张成）；这是**导出列**。令 $\mathfrak{g}^{[0]}=\mathfrak{g}$、$\mathfrak{g}^{[k+1]}=[\mathfrak{g},\mathfrak{g}^{[k]}]$；这是**下中心列**。每一项都是理想（与 $\mathfrak{g}$ 中任何元素的括号都留在其内）。

> **定义 — 可解、幂零。** $\mathfrak{g}$ 是**可解的**，若对某个 $k$ 有 $\mathfrak{g}^{(k)}=\{0\}$（反复对导出部分求括号最终把一切归零）。$\mathfrak{g}$ 是**幂零的**，若对某个 $k$ 有 $\mathfrak{g}^{[k]}=\{0\}$。幂零 $\Rightarrow$ 可解，因为对所有 $k$ 有 $\mathfrak{g}^{(k)}\subseteq\mathfrak{g}^{[k]}$（一个简单的归纳：$\mathfrak{g}^{(k+1)}=[\mathfrak{g}^{(k)},\mathfrak{g}^{(k)}]\subseteq[\mathfrak{g},\mathfrak{g}^{[k]}]=\mathfrak{g}^{[k+1]}$）。

**例子。** 每个**阿贝尔**代数（所有括号为零）都是幂零的：已有 $\mathfrak{g}^{(1)}=\{0\}$。严格上三角 $n\times n$ 矩阵（对角线及其下方为零）的代数是幂零的——每次对易都把非零带推得离对角线更远一步，直到掉出去。*所有*上三角矩阵的代数是可解的但不是幂零的。

> **定义 — 根与半单。** 每个有限维李代数都有唯一的极大可解理想，即**根** $\mathrm{rad}\mathfrak{g}$（所有可解理想之和仍可解，故存在一个最大者）。$\mathfrak{g}$ 是**半单的**，若 $\mathrm{rad}\mathfrak{g}=\{0\}$——根本没有非零的可解理想。等价地（我们要用的一条定理，归功于 Cartan），半单代数是单代数的直和。

半单是最佳位置："尽可能远离可解"。我们现在来构建检测器。

> **定义 — Killing 形式。** **Killing 形式**是对称双线性形式 $\kappa:\mathfrak{g}\times\mathfrak{g}\to\mathbb{F}$，
>
> $$
> \kappa(X,Y)=\mathrm{tr}\big(\mathrm{ad}_X\,\mathrm{ad}_Y\big),
> $$
>
> 即两个伴随算子复合的迹。它是对称的，因为 $\mathrm{tr}(AB)=\mathrm{tr}(BA)$；它还是**不变的**：$\kappa([X,Y],Z)=\kappa(X,[Y,Z])$。

**不变性的证明。**
1. 由 s1 的引理，$\mathrm{ad}_{[X,Y]}=\mathrm{ad}_X\mathrm{ad}_Y-\mathrm{ad}_Y\mathrm{ad}_X$。记 $A=\mathrm{ad}_X,B=\mathrm{ad}_Y,C=\mathrm{ad}_Z$。
2. 那么 $\kappa([X,Y],Z)=\mathrm{tr}((AB-BA)C)=\mathrm{tr}(ABC)-\mathrm{tr}(BAC)$，依*迹的线性性*与第 1 步。
3. 同样地 $\kappa(X,[Y,Z])=\mathrm{tr}(A(BC-CB))=\mathrm{tr}(ABC)-\mathrm{tr}(ACB)$。
4. 由*迹的循环性*，$\mathrm{tr}(BAC)=\mathrm{tr}(ACB)$。因此第 2 步与第 3 步相等。$\blacksquare$

Killing 形式不依赖于基（它是一个迹）——正是我们在 s1 中想要的不变对象。它的关键特征是**非退化性**：$\kappa$ 非退化，若使得 $\kappa(X,Y)=0$ 对所有 $Y$ 成立的唯一 $X$ 是 $X=0$。

> **定理 — Cartan 半单性判据。** 一个有限维李代数 $\mathfrak{g}$ 是半单的**当且仅当**它的 Killing 形式 $\kappa$ 非退化。

我们把它当作一个工作工具来用；它的证明依赖于*可解性*的 Cartan 判据（一个代数可解，当且仅当它的 Killing 形式在 $[\mathfrak{g},\mathfrak{g}]$ 上为零，这通过幂零算子的结构来证明），以及根恰是 $\kappa$ 的**核**（退化子空间）这一事实。我们给出支撑我们例子的那个方向。

**证明：非零阿贝尔理想迫使退化（故非退化 $\Rightarrow$ 半单）。**
1. 设 $\mathfrak{a}\ne\{0\}$ 是一个阿贝尔理想（$[\mathfrak{a},\mathfrak{a}]=0$）。取 $A\in\mathfrak{a}$、$X\in\mathfrak{g}$；我们来证明 $\kappa(A,X)=0$，于是每个 $A\in\mathfrak{a}$ 都落在退化子空间中，使得 $\kappa$ 退化。
2. 考虑算子 $T=\mathrm{ad}_A\mathrm{ad}_X$。映射 $\mathrm{ad}_X$ 把 $\mathfrak{g}$ 映入 $\mathfrak{g}$，而因为 $\mathfrak{a}$ 是理想，$\mathrm{ad}_A$ 把 $\mathfrak{g}$ 映*入* $\mathfrak{a}$（因为 $[A,\,\cdot\,]\in\mathfrak{a}$，由于 $\mathfrak{a}$ 是理想）。所以 $\mathrm{ad}_A\mathfrak{g}\subseteq\mathfrak{a}$。
3. 那么 $T(\mathfrak{g})=\mathrm{ad}_A(\mathrm{ad}_X\mathfrak{g})\subseteq\mathrm{ad}_A\mathfrak{g}\subseteq\mathfrak{a}$，且 $T(\mathfrak{a})=\mathrm{ad}_A\mathrm{ad}_X\mathfrak{a}\subseteq\mathrm{ad}_A\mathfrak{g}\subseteq\mathfrak{a}$；此外 $T^2(\mathfrak{g})\subseteq\mathrm{ad}_A\mathrm{ad}_X\mathfrak{a}\subseteq\mathrm{ad}_A\mathfrak{a}=[A,\mathfrak{a}]\subseteq[\mathfrak{a},\mathfrak{a}]=0$，这里用到 $\mathfrak{a}$ 是*阿贝尔的*。所以 $T$ 是**幂零的**（$T^2=0$）。
4. 幂零算子的所有特征值都是 $0$，因此迹为 $0$：$\kappa(A,X)=\mathrm{tr}T=0$。由于 $X$ 任意，$A$ 在退化子空间中。$\blacksquare$

**习题例 — $\mathfrak{su}(2)$ 的 $\kappa$。** 用 $f_{ab}{}^c=\varepsilon_{abc}$，$\mathrm{ad}_{T_a}$ 的矩阵元是 $(\mathrm{ad}_{T_a})_{cb}=\varepsilon_{acb}$。那么
$$
\kappa(T_a,T_b)=\mathrm{tr}(\mathrm{ad}_{T_a}\mathrm{ad}_{T_b})=\sum_{c,d}\varepsilon_{acd}\varepsilon_{bdc}=-\sum_{c,d}\varepsilon_{acd}\varepsilon_{bcd}=-2\,\delta_{ab},
$$
这里用到恒等式 $\sum_{c,d}\varepsilon_{acd}\varepsilon_{bcd}=2\delta_{ab}$。所以 $\kappa=-2\,I$，它是非退化的（$\det=-8\ne0$）：由 Cartan 判据 $\mathfrak{su}(2)$ 是半单的，实际上是单的。这个形式是负定的——这是**紧**代数的标志，正因如此 $\mathfrak{su}(2)$ 积分成紧群 $SU(2)$。

> **易错点。** "半单"*不是*"没有阿贝尔子代数"——每个代数都有大量阿贝尔子代数。它指的是没有阿贝尔（更一般地，可解）*理想*。Cartan 子代数（s3）是阿贝尔的，但不是理想，所以它不违反半单性。

## B 部分 — 根与分类

<a id="s3"></a>
### Cartan 子代数与根空间分解（贯穿例 $\mathfrak{su}(3)$）

**是什么以及为什么。** 在前置指南中为分析 $\mathfrak{su}(2)$，我们挑出唯一对易的生成元 $J_3$，把它对角化，并观察升降算子 $J_\pm$ 把它的特征值平移 $\pm1$。一般理论照搬这一做法：挑出一组*极大*的相互对易的生成元（**Cartan 子代数**），把它们在 $\mathfrak{g}$ 上的伴随作用同时对角化，于是出现的非零平移向量就是**根**。这把整个代数分解为一个对易核心加上若干根空间——本学科的母图。

我们从现在起在 $\mathbb{C}$ 上工作（把代数复化；例如 $\mathfrak{su}(2)$ 复化成 $\mathfrak{sl}(2,\mathbb{C})$，由下面的 $H,E,F$ 张成）。在 $\mathbb{C}$ 上算子可对角化，而分析正需要这一点。

> **定义 — Cartan 子代数（CSA）。** **Cartan 子代数** $\mathfrak{h}\subseteq\mathfrak{g}$ 是一个极大阿贝尔子代数，其所有元素在 $\mathrm{ad}$ 下都可对角化作用（这类元素称为**半单的**）。它的维数是 $\mathfrak{g}$ 的**秩** $r$。对半单的 $\mathfrak{g}$，所有 Cartan 子代数有相同的维数，故秩定义良好。

因为 $\mathfrak{h}$ 的元素彼此对易，它们的伴随算子 $\{\mathrm{ad}_H:H\in\mathfrak{h}\}$ 也对易，而对易的可对角化算子是**可同时对角化的**（一个标准的线性代数事实：存在公共特征基）。所以 $\mathfrak{g}$ 分裂为联合特征空间。

> **定义 — 根空间分解。** 对线性泛函 $\alpha\in\mathfrak{h}^{*}$（线性映射 $\mathfrak{h}\to\mathbb{C}$）定义**根空间**
>
> $$
> \mathfrak{g}_\alpha=\{\,X\in\mathfrak{g} : [H,X]=\alpha(H)\,X \text{ for all } H\in\mathfrak{h}\,\}.
> $$
>
> 使得 $\mathfrak{g}_\alpha\ne\{0\}$ 的非零 $\alpha$ 是**根**；根的集合是 $\Phi$。零泛函对应的空间就是 $\mathfrak{g}_0=\mathfrak{h}$ 本身（对半单 $\mathfrak{g}$，CSA 是它自己的中心化子）。整个代数是直和
>
> $$
> \mathfrak{g}=\mathfrak{h}\ \oplus\ \bigoplus_{\alpha\in\Phi}\mathfrak{g}_\alpha .
> $$

根 $\alpha$ 是生成元 $X\in\mathfrak{g}_\alpha$ 在 CSA 的特征值上所产生的那些"平移"构成的向量——正是"$J_\pm$ 把 $J_3$ 平移 $\pm1$"的多维版本。

> **命题 — 根的基本性质。** 对半单的 $\mathfrak{g}$：
> 1. $[\mathfrak{g}_\alpha,\mathfrak{g}_\beta]\subseteq\mathfrak{g}_{\alpha+\beta}$（括号使根相加）。
> 2. 每个根空间都是**一维**的：$\dim\mathfrak{g}_\alpha=1$。
> 3. 若 $\alpha\in\Phi$ 则 $-\alpha\in\Phi$，且 $\alpha$ 的倍数中只有 $\pm\alpha$ 是根。
> 4. 对 $\alpha\in\Phi$，三元组 $\{E_\alpha\in\mathfrak{g}_\alpha,\ E_{-\alpha}\in\mathfrak{g}_{-\alpha},\ H_\alpha=[E_\alpha,E_{-\alpha}]\}$ 张成一个同构于 $\mathfrak{sl}(2,\mathbb{C})$ 的子代数。

**(1) 的证明。** 设 $X\in\mathfrak{g}_\alpha,Y\in\mathfrak{g}_\beta,H\in\mathfrak{h}$。那么
$$
[H,[X,Y]]=[[H,X],Y]+[X,[H,Y]]
$$
依 *Jacobi 恒等式*（以 $\mathrm{ad}_H$ 是导子的形式）。第一项是 $[\alpha(H)X,Y]=\alpha(H)[X,Y]$，第二项是 $\beta(H)[X,Y]$，依*根空间的定义*与*双线性性*。相加得 $[H,[X,Y]]=(\alpha+\beta)(H)\,[X,Y]$，所以 $[X,Y]\in\mathfrak{g}_{\alpha+\beta}$。$\blacksquare$

性质 (4) 是整个理论的引擎：**每个根都给出一份 $\mathfrak{su}(2)$ 阶梯的副本**。因为我们已经完全知道 $\mathfrak{su}(2)$ 的表示（$H$ 的特征值是整数，关于 $0$ 对称），我们可以把那个知识转移过来，约束根与权彼此之间如何排布（s4、s6）。

> **每个根内部的 $\mathfrak{sl}(2)$。** 归一化使得 $H_\alpha,E_\alpha,E_{-\alpha}$ 满足 $[H_\alpha,E_\alpha]=2E_\alpha$、$[H_\alpha,E_{-\alpha}]=-2E_{-\alpha}$、$[E_\alpha,E_{-\alpha}]=H_\alpha$。这*恰是* $\mathfrak{sl}(2,\mathbb{C})$ 的关系，对应 $H\leftrightarrow H_\alpha$。元素 $H_\alpha\in\mathfrak{h}$ 是 $\alpha$ 的**余根**。

**习题例 — $\mathfrak{su}(3)$ 根系。** 复化成 $\mathfrak{sl}(3,\mathbb{C})$，即无迹 $3\times3$ 复矩阵，维数 $8$。CSA $\mathfrak{h}$ 是对角无迹矩阵，秩 $2$。设 $E_{ij}$（$i\ne j$）是在第 $i$ 行、第 $j$ 列处单独一个 $1$ 的矩阵。对对角阵 $H=\mathrm{diag}(h_1,h_2,h_3)$（满足 $h_1+h_2+h_3=0$），
$$
[H,E_{ij}]=(h_i-h_j)\,E_{ij},
$$
因为 $HE_{ij}$ 按第 $i$ 个对角元缩放，而 $E_{ij}H$ 按第 $j$ 个缩放。所以 $E_{ij}$ 是根向量，其根 $\alpha=L_i-L_j$，其中 $L_i(H)=h_i$ 读取第 $i$ 个对角元。六个根是 $\pm(L_1-L_2),\ \pm(L_2-L_3),\ \pm(L_1-L_3)$。把它们画在平面 $h_1+h_2+h_3=0$ 上（用 Killing 形式给出的内积），得到**六个等长向量，以 $60^\circ$ 间隔排列——一个正六边形。** 这个六边形是 $A_2$ 根系，它正是八重法的几何 DNA。

> **易错点。** CSA 作为*集合*不唯一（任何共轭都行），但它的维数——即秩——以及由此得到的根系是内禀的。选择 CSA 就像选择坐标轴；物理（多重态的形状）与坐标轴无关。

<a id="s4"></a>
### 根系：单根、Cartan 矩阵与 Dynkin 图

**是什么以及为什么。** 根的集合 $\Phi$ 不是任意一堆向量；来自每个根的 $\mathfrak{sl}(2)$ 结构（s3）强加了尖锐的几何约束。把这些约束抽象出来，就得到**根系**的概念，即在某些反射下封闭的有限向量集合。值得注意的是，一个根系由极少量的数据决定——少数几个**单根**，打包进一个 **Cartan 矩阵**并画成一张 **Dynkin 图**——而正是这份数据被分类（s5）所枚举。

> **定义 — 根系。** 欧氏空间 $E$（带内积 $(\cdot,\cdot)$）中非零向量的有限集合 $\Phi$ 是一个**根系**，如果：
> 1. $\Phi$ 张成 $E$，且对每个 $\alpha\in\Phi$，$\Phi$ 中 $\alpha$ 的倍数只有 $\pm\alpha$；
> 2. 对每个 $\alpha$，**反射** $s_\alpha(v)=v-\dfrac{2(v,\alpha)}{(\alpha,\alpha)}\alpha$（关于垂直于 $\alpha$ 的超平面的反射）把 $\Phi$ 映到自身；
> 3. （**整性**）对所有 $\alpha,\beta\in\Phi$，整数 $\langle\beta,\alpha\rangle:=\dfrac{2(\beta,\alpha)}{(\alpha,\alpha)}\in\mathbb{Z}$。

(3) 中的整性不是我们凭喜好强加的假设——它是被每个根的 $\mathfrak{sl}(2)$ 作用于根空间所*强制*的，因为（s3 性质 4 加上 s6）任何 $H_\alpha$ 的特征值都是整数。这个单一事实极其严苛。

> **定理 — 两根之间的夹角被量子化。** 对夹角为 $\theta$ 的相异根 $\alpha,\beta$，乘积 $\langle\beta,\alpha\rangle\langle\alpha,\beta\rangle = \dfrac{4(\alpha,\beta)^2}{(\alpha,\alpha)(\beta,\beta)}=4\cos^2\theta$ 是一个 $\le 4$ 的非负整数，故 $\in\{0,1,2,3,4\}$。排除平行情形（$\theta=0,\pi$，给出 $4$），唯一的可能是 $4\cos^2\theta\in\{0,1,2,3\}$，即 $\theta\in\{90^\circ,120^\circ,135^\circ,150^\circ\}$（以及补角 $60^\circ,45^\circ,30^\circ$）。

**证明。**
1. $\langle\beta,\alpha\rangle$ 和 $\langle\alpha,\beta\rangle$ 都是整数，由整性（公理 3）。
2. 它们的乘积是 $\dfrac{2(\beta,\alpha)}{(\alpha,\alpha)}\cdot\dfrac{2(\alpha,\beta)}{(\beta,\beta)}=\dfrac{4(\alpha,\beta)^2}{(\alpha,\alpha)(\beta,\beta)}$，由*代入*。
3. 由 *Cauchy–Schwarz 定义* $\cos\theta=\dfrac{(\alpha,\beta)}{\|\alpha\|\,\|\beta\|}$，这个乘积等于 $4\cos^2\theta$，一个在 $[0,4]$ 中的实数。
4. 作为 $[0,4]$ 中整数的乘积，它落在 $\{0,1,2,3,4\}$ 中。解 $4\cos^2\theta=k$ 给出所列的夹角。$\blacksquare$

一个连续量（夹角）被钉死在四个离散值上，这正是为什么只有有限多个根系。我们现在把数据进一步约简。

> **定义 — 正根与单根。** 在 $E$ 上选一个在每个根上都非零的线性泛函（一个"通用方向"）。一个根是**正的**（$\alpha>0$）若其值为正，否则为**负的**；$\Phi=\Phi^{+}\sqcup\Phi^{-}$，其中 $\Phi^{-}=-\Phi^{+}$。一个正根是**单的**若它*不是*两个正根之和。单根的集合 $\Delta=\{\alpha_1,\dots,\alpha_r\}$ 是 $E$ 的一组**基**（$r=\mathrm{rank}$），且每个正根都是单根的*非负整数组合*。

> **定义 — Cartan 矩阵。** 取单根 $\alpha_1,\dots,\alpha_r$，**Cartan 矩阵**是 $r\times r$ 整数矩阵
>
> $$
> A_{ij}=\langle\alpha_i,\alpha_j\rangle=\frac{2(\alpha_i,\alpha_j)}{(\alpha_j,\alpha_j)} .
> $$
>
> 它的对角元是 $A_{ii}=2$；非对角元在 $\{0,-1,-2,-3\}$ 中（由夹角量子化，因为相异单根成钝角，故 $(\alpha_i,\alpha_j)\le0$）。

> **定义 — Dynkin 图。** 每个单根画一个节点。把相异节点 $i\ne j$ 用 $A_{ij}A_{ji}\in\{0,1,2,3\}$ 条边连起来。当两个根长度不同（双键或三键）时，画一个从较长根指向较短根的箭头。这幅图编码了整个 Cartan 矩阵，因而（可以通过从 $\Delta$ 重构 $\Phi$ 来证明）编码了整个代数。

**习题例 — $A_2=\mathfrak{su}(3)$。** 由 s3，正根可取为 $\alpha_1=L_1-L_2$、$\alpha_2=L_2-L_3$，第三个正根是 $\alpha_1+\alpha_2=L_1-L_3$（所以它*不是*单的——它是正根之和）。所有根等长；$\alpha_1$ 与 $\alpha_2$ 之间的夹角是 $120^\circ$。那么
$$
A=\begin{pmatrix}2 & -1\\ -1 & 2\end{pmatrix},
$$
因为 $A_{12}=2\cos120^\circ\cdot\frac{\|\alpha_1\|}{\|\alpha_2\|}=2(-\tfrac12)(1)=-1$。Dynkin 图是用单条边连起来的两个节点：$\circ\!-\!\circ$。这是最简单的非平凡图，它*就是* $\mathfrak{su}(3)$。

> **易错点。** Cartan 整数 $\langle\alpha_i,\alpha_j\rangle$ 一般**不对称**（当根长度不同时 $A_{ij}\ne A_{ji}$）；图只记录它们的乘积。忘掉箭头就丢失了 $B_n$ 与 $C_n$ 的区别。

<a id="s5"></a>
### 单李代数的分类（$A_n,B_n,C_n,D_n$ 与例外型）

**是什么以及为什么。** 这里是顶峰。根系上的夹角/长度约束如此之紧，以至于连通的 Dynkin 图可以被完全列出——而每一个都恰好对应于 $\mathbb{C}$ 上的一个单李代数。这就是 **Cartan–Killing 分类**，数学中的伟大定理之一。我们陈述它并解释使名单有限的逻辑。

> **定理 — 单李代数的分类。** 在 $\mathbb{C}$ 上，每个有限维单李代数恰好对应一张连通 Dynkin 图，完整名单是：
> - 四个无穷的**经典**族：
>   - $A_n\ (n\ge1)$：$\mathfrak{sl}(n+1,\mathbb{C})$，无迹矩阵——紧实形式 $\mathfrak{su}(n+1)$；
>   - $B_n\ (n\ge2)$：$\mathfrak{so}(2n+1,\mathbb{C})$，奇正交；
>   - $C_n\ (n\ge3)$：$\mathfrak{sp}(2n,\mathbb{C})$，辛；
>   - $D_n\ (n\ge4)$：$\mathfrak{so}(2n,\mathbb{C})$，偶正交；
> - 五个**例外**代数：$G_2,F_4,E_6,E_7,E_8$（维数 $14,52,78,133,248$）。

这些图：$A_n$ 是 $n$ 个节点的单键链；$B_n$ 与 $C_n$ 是以双键收尾的链（用箭头区分）；$D_n$ 是一端分叉成两个节点的链；$G_2$ 是用三键相连的两个节点；$F_4$ 是带中央双键的四个节点；$E$ 系列是带一条短分支的分叉图。

**界定名单的逻辑（带关键步骤的概要）。**
1. 一张连通 Dynkin 图来自一组单位向量或缩放向量，其两两夹角在 $\{90^\circ,120^\circ,135^\circ,150^\circ\}$ 中且成对钝角（s4）。称这样的配置为**容许的**。
2. **无圈。** 若图中含有一个圈，把圈中的单根相加并对长度平方，利用每条键贡献 $2(\alpha_i,\alpha_j)\le-(\alpha_i,\alpha_i)$，得到一个非零向量的非正范数——与内积的正定性矛盾。所以图是**树**。
3. **分支有界。** 一个节点最多有三条键（计入重数）：若节点 $\beta$ 与邻居 $\gamma_1,\dots,\gamma_k$ 相连（两两正交，因为不相邻的单根正交），那么 $\sum_i \cos^2(\beta,\gamma_i)<1$，因为 $\beta$ 有一个落在它们张成空间之外的分量；每条键对该和贡献 $\ge\tfrac14$，迫使键数 $\le 3$。这除掉了所列形状之外的一切：至多一条双键/三键，至多一个度为三的分支节点。
4. **特征值检验。** 还剩有限多棵候选树；对相伴的对称矩阵做行列式/特征值计算（它必须正定）排除其余，恰好留下 $A_n,B_n,C_n,D_n,G_2,F_4,E_6,E_7,E_8$。
5. **存在性。** 反过来，每张幸存的图都被*实现*：经典型由显式的矩阵代数实现，例外型由直接（尽管繁复）的构造实现。所以对应关系 图 $\leftrightarrow$ 代数 是一个双射。$\blacksquare$（关于界限部分；存在性引用文献）

**习题例 — 从 $A_n$ 读出维数。** 对 $A_n=\mathfrak{su}(n+1)$：秩 $n$，根是 $n+1$ 个指标中 $i\ne j$ 的 $L_i-L_j$，给出 $n(n+1)$ 个根，再加上秩为 $n$ 的 CSA：总维数 $\dim=n(n+1)+n=n(n+2)$。验证 $n=1$：$\dim=3$（$\mathfrak{su}(2)$，正确）；$n=2$：$\dim=8$（$\mathfrak{su}(3)$，正确，与八个 Gell-Mann 矩阵相符）。

> **为什么物理与例外型相遇。** 大统一理论曾提出 $SU(5)$（$A_4$）、$SO(10)$（$D_5$）和 $E_6$ 作为规范群，正是因为它们的表示能把一代夸克和轻子打包进单个多重态。因此这份分类是自然界对称性候选者的一份有限菜单。

> **易错点 — 低秩巧合。** 那些范围（$B_n$ 从 $n\ge2$ 起，等等）避免重复计入偶然同构：$A_1=B_1=C_1$（$\mathfrak{su}(2)\cong\mathfrak{so}(3)\cong\mathfrak{sp}(2)$）、$B_2\cong C_2$、$D_2\cong A_1\times A_1$、$D_3\cong A_3$。这些是真正的同构，不是错误，在你识别一个物理对称性时很重要。

## C 部分 — 表示论

<a id="s6"></a>
### 权、权格与最高权定理

**是什么以及为什么。** 有了代数的骨架（根）在手，我们转向它的表示。CSA 在一个表示上的特征值就是**权**——即 $J_3$ 特征值 $m$ 的推广。正如一个自旋 $j$ 的表示被它最高的特征值 $m=j$ 钉死，半单代数的每个不可约表示都被单个**最高权**钉死。这是整个学科的核心分类定理。

> **定义 — 表示的权。** 设 $\rho:\mathfrak{g}\to\mathfrak{gl}(V)$ 是一个表示。由于 $\mathfrak{h}$ 是阿贝尔的，且（在半单代数的有限维表示中）作用可对角化，$V$ 分裂为联合特征空间：
>
> $$
> V=\bigoplus_{\mu} V_\mu,\qquad V_\mu=\{v\in V:\rho(H)v=\mu(H)\,v\ \forall H\in\mathfrak{h}\}.
> $$
>
> 每个使 $V_\mu\ne0$ 的 $\mu\in\mathfrak{h}^{*}$ 是一个**权**；$\dim V_\mu$ 是它的**重数**。（根是*伴随*表示的权，s3。）

> **根向量如何移动权。** 若 $v\in V_\mu$ 且 $E_\alpha\in\mathfrak{g}_\alpha$，那么 $\rho(E_\alpha)v\in V_{\mu+\alpha}$。证明：对 $H\in\mathfrak{h}$，$\rho(H)\rho(E_\alpha)v=\rho(E_\alpha)\rho(H)v+\rho([H,E_\alpha])v=\mu(H)\rho(E_\alpha)v+\alpha(H)\rho(E_\alpha)v=(\mu+\alpha)(H)\rho(E_\alpha)v$，用到 $\rho$ 是*同态*（$\rho([H,E_\alpha])=[\rho(H),\rho(E_\alpha)]$）以及 $[H,E_\alpha]=\alpha(H)E_\alpha$。所以 $\rho(E_\alpha)$ 是一个升降算子，把权平移根 $\alpha$。

> **定义 — 整权与权格。** 把每个根的 $\mathfrak{sl}(2)$（s3）作用于一个权，迫使对每个根 $\alpha$ 有 $\langle\mu,\alpha\rangle=\dfrac{2(\mu,\alpha)}{(\alpha,\alpha)}\in\mathbb{Z}$——因为 $\mu(H_\alpha)$ 是某个 $\mathfrak{sl}(2)$ 表示中 $H_\alpha$ 的一个特征值，因此是整数。这样的 $\mu$ 是**整权**；它们构成一个格 $P$，即**权格**。$P$ 中与单余根**对偶**的基是**基本权**的集合 $\{\omega_1,\dots,\omega_r\}$，由 $\langle\omega_i,\alpha_j\rangle=\delta_{ij}$ 定义。

> **定义 — 支配权、最高权。** 固定正根（s4）。一个权 $\mu$ 是**支配的**，若对所有单根 $\alpha_i$ 有 $\langle\mu,\alpha_i\rangle\ge0$（等价地 $\mu=\sum_i m_i\omega_i$，其中整数 $m_i\ge0$，即 **Dynkin 标号**）。在一个不可约表示中存在唯一的权 $\lambda$，即**最高权**，使得对任何正根 $\alpha$，$\lambda+\alpha$ *都不是*权（没有升算子能逃出它）；它的权空间是一维的。

> **定理 — 最高权定理（Cartan–Weyl）。** 设 $\mathfrak{g}$ 是半单李代数。映射
>
> $$
> \big\{\text{irreducible finite-dim representations}\big\}/\!\cong\ \ \xrightarrow{\ \sim\ }\ \big\{\text{dominant integral weights }\lambda\big\}
> $$
>
> 把每个不可约表示送到它的最高权，是一个**双射**。每个支配整权都是恰好一个不可约表示 $V(\lambda)$ 的最高权，且同构的表示有相等的最高权。

**唯一性/单射性的证明（我们在这里能干净利落完成的部分）。**
1. *（最高权存在。）* $V$ 有限维，故在它有限多个权中挑一个对序"$\mu\preceq\mu'$ 当且仅当 $\mu'-\mu$ 是正根之和"为极大的权 $\lambda$。那么对任何正根 $\alpha$，$\lambda+\alpha$ 都不是权，因为它会超过 $\lambda$。所以最高权存在。
2. *（它的权空间一维且生成全空间。）* 设 $0\ne v_\lambda\in V_\lambda$。反复施加降算子 $\rho(E_{-\alpha})$；由权平移规则，每次都落入更低的权空间，而所有这些像的张成 $W$ 是 $\mathfrak{g}$ 不变的（施加于一串降算子之上的升算子，可借助对易关系重写为更低阶的串——即 s7 的 **PBW** 重排）。由于 $V$ 不可约且 $W\ne0$，故 $W=V$。所以 $V$ 由单个向量 $v_\lambda$ 生成。
3. *（最高权决定表示。）* 若 $V,V'$ 不可约且有相同的最高权 $\lambda$，构造 $V\oplus V'$ 及其对角最高权向量 $(v_\lambda,v'_\lambda)$；它生成的子表示是不可约的，且非平凡地投影到每个因子上，故由 Schur 引理这些投影是同构，给出 $V\cong V'$。因此映射是单射。$\blacksquare$（满射性——即*每个*支配 $\lambda$ 都出现——是 s7 的 Verma 模构造的内容。）

**习题例 — $\mathfrak{su}(3)$ 的基本权。** 秩 $2$，单根 $\alpha_1,\alpha_2$ 成 $120^\circ$，等长 $\sqrt2$（故 $(\alpha_i,\alpha_i)=2$）。解 $\langle\omega_i,\alpha_j\rangle=\delta_{ij}$ 得到 $\omega_1,\omega_2$ 为六边形的两个"外"方向。定义表示 $\mathbf 3$ 有最高权 $\omega_1$（Dynkin 标号 $(1,0)$）；它的共轭 $\overline{\mathbf3}$ 有 $\omega_2=(0,1)$；伴随八重态 $\mathbf 8$ 有 $\omega_1+\omega_2=(1,1)$。每个 $SU(3)$ 多重态都由一对非负整数 $(p,q)=(m_1,m_2)$ 标记，即 Dynkin 标号。

> **易错点。** "最高"依赖于所选的正系统/通用方向。不同的选择把权按 Weyl 群（s8）置换，所以*表示*不变，尽管被标记为"最高"的向量会移动。务必固定一个正系统并坚持使用。

<a id="s7"></a>
### 从最高权构造不可约表示（Verma 模）

**是什么以及为什么。** 最高权定理说每个支配 $\lambda$ 标记一个不可约表示，但我们想*构造*它并计算它的权。干净的构造是 **Verma 模**：通过形式地施加所有降算子，构建"尽可能自由"的最高权表示，然后把应当消失的部分商掉。这既证明了存在性（s6 的满射性），又给出了权图的算法。

> **定义 — 泛包络代数与 PBW。** **泛包络代数** $U(\mathfrak{g})$ 是由 $\mathfrak{g}$ 生成、仅服从 $XY-YX=[X,Y]$ 的结合代数。$\mathfrak{g}$ 的表示与 $U(\mathfrak{g})$ 模是同一回事。**Poincaré–Birkhoff–Witt（PBW）定理**指出，固定 $\mathfrak{g}$ 的一组有序基，分成（降 $E_{-\alpha}$）$\,\cdot\,$（Cartan $H$）$\,\cdot\,$（升 $E_\alpha$），那么有序单项式构成 $U(\mathfrak{g})$ 的一组基——任何乘积都可用对易关系重排成这个正规形式。

> **定义 — Verma 模。** 对一个权 $\lambda$，**Verma 模** $M(\lambda)$ 由单个向量 $v_\lambda$ 生成，规则是：$\rho(H)v_\lambda=\lambda(H)v_\lambda$（它有权 $\lambda$）以及对每个正根 $\alpha$ 有 $\rho(E_\alpha)v_\lambda=0$（它是"最高的"），*没有其他关系*。由 PBW，$M(\lambda)$ 的一组基是
>
> $$
> \big\{\,\rho(E_{-\beta_1})^{k_1}\cdots\rho(E_{-\beta_N})^{k_N}\,v_\lambda\ :\ k_i\ge0\,\big\},
> $$
>
> 其中 $\beta_1,\dots,\beta_N$ 取遍正根。指数为 $k_i$ 的单项式有权 $\lambda-\sum_i k_i\beta_i$。

$M(\lambda)$ 是*无穷维*的——我们无限制地施加了降算子。它含有唯一的极大真子模 $N(\lambda)$（所有避开 $v_\lambda$ 的子模之和）。

> **定理 — 不可约表示的构造。** 商 $V(\lambda)=M(\lambda)/N(\lambda)$ 是最高权为 $\lambda$ 的不可约表示。若 $\lambda$ 是**支配整权**，则 $V(\lambda)$ 是**有限维的**，完成了 s6 的最高权双射。

**为什么支配性给出有限维（机制）。**
1. 对每个单根 $\alpha_i$，三元组 $H_i,E_i,E_{-i}$ 是一个 $\mathfrak{sl}(2)$（s3）。向量 $v_\lambda$ 的 $H_i$ 特征值是 $m_i=\langle\lambda,\alpha_i\rangle\ge0$，一个整数（支配整权）。
2. 在 $\mathfrak{sl}(2)$ 表示论中（前置指南），最高权 $m_i\ge0$ 迫使 $E_{-i}^{\,m_i+1}v_\lambda$ 成为一个权为 $\lambda-(m_i+1)\alpha_i$ 的*新*最高权向量，而相容性要求它在不可约商中消失。
3. 这些消失关系（每个单根一条）把无穷的 Verma 模砍成有限多个幸存的权——恰是熬过所有 $\mathfrak{sl}(2)$ 截断的那些 $\le\lambda$ 的权。幸存集合是有限的且 Weyl 对称（s8）。$\blacksquare$（机制；完整证明经由 Weyl 完全可约性定理）

**习题例 — 从 $\lambda=\omega_1=(1,0)$ 构造 $\mathfrak{su}(3)$ 的 $\mathbf3$。**
1. 从权为 $\omega_1$ 的 $v_\lambda$ 出发。它的 Dynkin 标号是 $(1,0)$：$\langle\lambda,\alpha_1\rangle=1$、$\langle\lambda,\alpha_2\rangle=0$。
2. 由于 $\langle\lambda,\alpha_2\rangle=0$，从 $v_\lambda$ 出发的 $\alpha_2$ 串长度为 $1$：施加 $E_{-\alpha_2}$ 得到 $0$。施加 $E_{-\alpha_1}$（标号 $1$）得到一个权为 $\omega_1-\alpha_1$ 的新态。
3. 从那个态出发，它的 $\alpha_2$ 标号现在是 $1$，所以施加 $E_{-\alpha_2}$ 得到第三个态，权为 $\omega_1-\alpha_1-\alpha_2$。再施加任何降算子都得到 $0$。
4. 三个态，权构成一个三角形：这就是前置指南中的夸克三角 $u,d,s$。维数 $3$，确认无误。

> **易错点。** Verma 模是无穷维且可约的；*物理*多重态是那个有限的商。跳过取商（忘掉关系 $E_{-i}^{m_i+1}v_\lambda=0$）会产生在自然界中无处安放的虚假"态"。

<a id="s8"></a>
### Weyl 群、Weyl 特征标公式与 Weyl 维数公式

**是什么以及为什么。** 任何表示的权图都有一个隐藏的对称性：它在由根生成的反射群即 **Weyl 群**之下不变。利用这一对称性，Weyl 导出了**特征标**（记录每个权及其重数的记账函数）的闭式公式，并作为推论，得到了 $V(\lambda)$ **维数**的一行公式。这些把权的计数从手工搜索变成了算术。

> **定义 — Weyl 群。** **Weyl 群** $W$ 是由单根上的反射 $s_{\alpha_i}$ 生成的群，按 $s_\alpha(\mu)=\mu-\langle\mu,\alpha\rangle\,\alpha$ 作用于权空间。它是有限的，置换诸根，并在正系统的各种可能选择上单可迁地作用。对 $\mathfrak{su}(2)$，$W=\mathbb{Z}_2$（$\mu\mapsto-\mu$）；对 $\mathfrak{su}(3)=A_2$，$W$ 是六边形的对称群，即 $6$ 阶二面体群 $S_3$。

> **定义 — 特征标。** 表示 $V$ 的**特征标**是关于权的形式和 $\mathrm{ch} V=\sum_\mu (\dim V_\mu)\,e^{\mu}$，其中 $e^\mu$ 是形式指数，满足 $e^\mu e^\nu=e^{\mu+\nu}$。它一次性记录所有权和重数，且 $\mathrm{ch}V|_{\text{set }e^\mu\to1}=\dim V$。

> **定义 — Weyl 向量与符号。** 令 $\rho=\tfrac12\sum_{\alpha>0}\alpha$ 为 **Weyl 向量**（正根之和的一半；等于 $\sum_i\omega_i$）。对 $w\in W$ 令 $\det(w)=(-1)^{\ell(w)}$，其中 $\ell(w)$ 是写出 $w$ 所需的反射个数（$w$ 的**符号**）。

> **定理 — Weyl 特征标公式。** 对最高权 $\lambda$ 为支配整权的不可约表示 $V(\lambda)$，
>
> $$
> \mathrm{ch}V(\lambda)\ =\ \frac{\displaystyle\sum_{w\in W}\det(w)\,e^{\,w(\lambda+\rho)}}{\displaystyle\sum_{w\in W}\det(w)\,e^{\,w(\rho)}} .
> $$
>
> 分母等于 **Weyl 分母** $\displaystyle\prod_{\alpha>0}\big(e^{\alpha/2}-e^{-\alpha/2}\big)$。

证明的思路（完整证明引自 Weyl）：分子与分母在 $W$ 之下各自*反对称*（符号随每次反射翻转），所以比值像真正的特征标那样 $W$ 对称，再把它与最高权 $\lambda$ 加上重数记账相匹配，便唯一地钉死它。我们完整地提取实用的推论。

> **推论 — Weyl 维数公式。**
>
> $$
> \dim V(\lambda)\ =\ \prod_{\alpha>0}\frac{(\lambda+\rho,\alpha)}{(\rho,\alpha)} ,
> $$
>
> 一个对正根的乘积。

**从特征标公式导出维数公式。**
1. $\dim V(\lambda)$ 是把每个 $e^\mu$ 设为 $1$ 的特征标。但令 $e^\mu\to1$ 会使 Weyl 特征标公式的分子和分母都消失（每个都是在"原点"取 $0$ 的交错和），是一个不定式 $0/0$。
2. 用标准的取极限技巧解决它：把 $e^\mu\to e^{t(\mu,\rho)}$ 换入一个实参数 $t$ 并令 $t\to0$（这相当于对交错和求导；合法是因为两者都关于 $t$ 解析）。
3. 分母变成 $\prod_{\alpha>0}\big(e^{t(\alpha,\rho)/2}-e^{-t(\alpha,\rho)/2}\big)\sim\prod_{\alpha>0} t(\alpha,\rho)$，当 $t\to0$，因为每个因子 $e^{x}-e^{-x}=2\sinh x\sim 2x$（到主导阶），此处 $x=t(\alpha,\rho)/2$，故 $\sim t(\alpha,\rho)$。
4. 分子，由同样的展开但以 $\lambda+\rho$ 代替 $\rho$，变成 $\sim\prod_{\alpha>0}t(\alpha,\lambda+\rho)$。
5. 取比值，$t$ 的幂次相消（各有 $|\Phi^+|$ 个因子），得
$$
\dim V(\lambda)=\prod_{\alpha>0}\frac{(\lambda+\rho,\alpha)}{(\rho,\alpha)} . \qquad\blacksquare
$$

**习题例 — $\mathfrak{su}(3)$ 多重态的维数。** 三个正根是 $\alpha_1,\alpha_2,\alpha_1+\alpha_2$，且 $\rho=\omega_1+\omega_2$。对 $\lambda=(p,q)=p\,\omega_1+q\,\omega_2$，计算这些乘积（在此归一化下用 $(\omega_i,\alpha_j)=\tfrac12(\alpha_j,\alpha_j)\delta_{ij}=\delta_{ij}$）给出著名的闭式
$$
\dim V(p,q)=\tfrac12(p+1)(q+1)(p+q+2).
$$
验证：$(p,q)=(1,0)\Rightarrow\tfrac12\cdot2\cdot1\cdot3=3$（即 $\mathbf3$）；$(1,1)\Rightarrow\tfrac12\cdot2\cdot2\cdot4=8$（八重态 $\mathbf8$）；$(3,0)\Rightarrow\tfrac12\cdot4\cdot1\cdot5=10$（重子十重态 $\mathbf{10}$）。这套算术精确地复现了八重法的多重态大小。

> **易错点。** 维数公式用的是 $\lambda+\rho$，不是 $\lambda$；忘掉 Weyl 向量 $\rho$ 是最常见的错误，会给出无意义（常常是零）的维数。

## D 部分 — 理论习题与物理

<a id="s9"></a>
### 完整做透 $\mathfrak{su}(2)$ 与 $\mathfrak{su}(3)$：多重态与八重法

**是什么以及为什么。** 我们现在为物理用得最多的两个代数组装起一切，端到端地计算它们的不可约表示，使抽象的机制成为具体的数字与图像。

**$\mathfrak{su}(2)$ 完整版。** 秩 $1$；复化成 $\mathfrak{sl}(2,\mathbb{C})$，满足 $[H,E]=2E,[H,F]=-2F,[E,F]=H$（这里 $E=J_+,F=J_-,H=2J_3$）。一个单根 $\alpha$，一个基本权 $\omega=\tfrac12\alpha$，Weyl 群 $\{1,-1\}$。
- 支配整权是 $\lambda=n\,\omega$，$n=0,1,2,\dots$（Dynkin 标号 $n$）；物理上 $n=2j$，故自旋 $j=n/2$。
- 表示 $V(n\omega)$ 有权 $n,n-2,\dots,-n+2,-n$（以 $H$ 特征值计），每个重数为 $1$。
- 由 Weyl 算维数：一个正根 $\alpha$，$\rho=\omega$，$\dim=\dfrac{(\lambda+\rho,\alpha)}{(\rho,\alpha)}=\dfrac{(n+1)\omega\cdot\alpha}{\omega\cdot\alpha}=n+1=2j+1$。这就是磁子态 $m=-j,\dots,j$ 的熟悉计数。

所以 $\mathfrak{su}(2)$ 的不可约表示恰是自旋 $j$ 多重态，从一般理论中得以恢复。

**$\mathfrak{su}(3)$ 完整版。** 秩 $2$；六个根构成一个六边形（s3）；正根 $\alpha_1,\alpha_2,\alpha_1+\alpha_2$；Weyl 群 $S_3$（$6$ 阶）；基本权 $\omega_1,\omega_2$。
- 多重态由 $(p,q)$ 标记，维数 $\tfrac12(p+1)(q+1)(p+q+2)$（s8）。
- $V(p,q)$ 的权图是一个六边形（当 $p$ 或 $q=0$ 时是三角形），外边界的边长为 $p$ 和 $q$，且**内部重数**随你向内跨过每一圈而增加 $1$，直到环变成三角形，然后保持不变。对八重态 $(1,1)$：一个由六个外权构成的六边形加上重数为 $2$ 的中心（$6+2=8$）。

**八重法，导出。** 把 $\mathbf 3=(1,0)$ 的三个态等同于权（同位旋 $t_3$，超荷 $y$）处的夸克 $u,d,s$：
$$
u:(\tfrac12,\tfrac13),\quad d:(-\tfrac12,\tfrac13),\quad s:(0,-\tfrac23).
$$
那么：
- **介子** $q\bar q$：$\mathbf3\otimes\overline{\mathbf3}=\mathbf8\oplus\mathbf1$（维数 $3\times3=9=8+1$）。八重态是赝标介子 $\pi^{\pm,0},K^{\pm},K^0,\bar K^0,\eta$；它们的权由把一个夸克权加上一个反夸克权得到，填出一个中心被双重占据的六边形。
- **重子** $qqq$：$\mathbf3\otimes\mathbf3\otimes\mathbf3=\mathbf{10}\oplus\mathbf8\oplus\mathbf8\oplus\mathbf1$（维数 $27=10+8+8+1$）。十重态 $\mathbf{10}=(3,0)$ 是一个三角形；它最底端尖角的位置，权 $(0,-1)$ 处带三个 $s$ 夸克，就是 **$\Omega^-$**，由这个三角形所预言，并于 1964 年被发现。

Gell-Mann–Nishijima 关系 $Q=t_3+\tfrac12 y$ 把每个权转换为电荷；对 $u$，$Q=\tfrac12+\tfrac12\cdot\tfrac13=\tfrac23$，即正确的分数夸克电荷。**强子的多重态结构，字面上就是 $\mathfrak{su}(3)$ 的不可约表示论。**

> **易错点。** 味 $SU(3)$ 只是近似的（$s$ 夸克更重），所以多重态在质量上有分裂；那个*分组*是精确的表示论，那个*简并*被破坏对称性的项打破。不要期待质量相等，只能期待相等的量子数模式。

<a id="s10"></a>
### 张量积、分支规则与 $\mathfrak{su}(n)$ 的 Young 表

**是什么以及为什么。** 把系统组合起来（两个夸克，夸克 + 反夸克）意味着对表示取张量积；结果是可约的，而分解它就是"多重态的相加"。对 $\mathfrak{su}(n)$ 有一套优美的组合记账法——**Young 表**——它通过画方块来完成这些分解。

> **定义 — 表示的张量积。** 给定 $\rho:\mathfrak{g}\to\mathfrak{gl}(V)$ 和 $\sigma:\mathfrak{g}\to\mathfrak{gl}(W)$，**张量积**按生成元的**和**作用于 $V\otimes W$（维数 $\dim V\cdot\dim W$）：$(\rho\otimes\sigma)(X)=\rho(X)\otimes I+I\otimes\sigma(X)$。因此权*相加*：$V\otimes W$ 的权是 $\{\mu+\nu:\mu\in\mathrm{wt}V,\nu\in\mathrm{wt}W\}$，重数相乘。

> **方法 — 按权分解。** 要分解 $V\otimes W=\bigoplus_i V(\lambda_i)$：列出所有相加得到的权，找到最高的那个，剥离以该最高权为最高权的不可约表示（减去它已知的权图），然后重复。这是 $\mathfrak{su}(2)$ Clebsch–Gordan 算法的多维版本。

**习题例 — $\mathfrak{su}(3)$ 的 $\mathbf 3\otimes\mathbf3$。** $9$ 个相加得到的权，其最高权为 $\omega_1+\omega_1=2\omega_1=(2,0)$，给出对称六重态 $\mathbf6$（$\dim=\tfrac12\cdot3\cdot1\cdot4=6$）。剩下的 $3$ 个权，最高权为 $\omega_2=(0,1)$，即反对称的 $\overline{\mathbf3}$。所以
$$
\mathbf3\otimes\mathbf3=\mathbf6\oplus\overline{\mathbf3},\qquad 9=6+3.
$$

> **定义 — Young 图与 Young 表。** **Young 图**是一个左对齐的方块阵列，行长 $\lambda_1\ge\lambda_2\ge\cdots\ge0$。对 $\mathfrak{su}(n)$，至多 $n-1$ 行的图标记一个不可约表示（长度为 $n$ 的列可以删去）。Dynkin 标号从行长之差恢复：$m_i=\lambda_i-\lambda_{i+1}$。

> **规则 — 经由钩长—内容公式求维数（对 $\mathfrak{su}(n)$）。** $\dim=\prod_{\text{boxes}}\dfrac{n+c(\text{box})}{h(\text{box})}$，其中 $c=(\text{column}-\text{row})$ 是**内容**，$h$ 是**钩长**（右侧加下方加自身的方块数）。**Littlewood–Richardson 规则**通过组合地把一个图的方块放入另一个图来分解张量积。

**习题例 — 用方块做 $\mathfrak{su}(3)$。** 单个方块 $\square$ 是 $\mathbf3$。那么 $\square\otimes\square$ =（一行两个方块）$\oplus$（一列两个方块）：行是对称的 $\mathbf6$，列是 $\overline{\mathbf3}$（在 $\mathfrak{su}(3)$ 中高度为 $2$ 的列），复现 $\mathbf3\otimes\mathbf3=\mathbf6\oplus\overline{\mathbf3}$。对三个方块，$\mathbf3\otimes\mathbf3\otimes\mathbf3$ 给出一行三个（$\mathbf{10}$）、两个 L 形 Young 表（$\mathbf8\oplus\mathbf8$）以及一列三个（一整列，$=\mathbf1$）：$\mathbf{10}\oplus\mathbf8\oplus\mathbf8\oplus\mathbf1$，恰是 s9 的重子分解。

> **定义 — 分支规则。** **分支规则**告诉你 $\mathfrak{g}$ 的一个不可约表示在限制到子代数 $\mathfrak{g}'\subset\mathfrak{g}$ 时如何分解（你只需读出 $\mathfrak{g}$ 的权包含哪些 $\mathfrak{g}'$ 的权）。例：把 $\mathfrak{su}(3)\to\mathfrak{su}(2)\times\mathfrak{u}(1)$（同位旋 $\times$ 超荷）限制，八重态分支为 $\mathbf8\to\mathbf3_0\oplus\mathbf2_{+1}\oplus\mathbf2_{-1}\oplus\mathbf1_0$——可辨认为重子八重态的 $\Sigma$/$\Lambda$、核子、$\Xi$ 与单态的内容。

> **易错点。** 生成元相加（$X\otimes I+I\otimes X$），但*群元*相乘（$\rho(g)\otimes\sigma(g)$）；在代数层面用乘法规则就是经典的角动量相加错误。

<a id="s11"></a>
### Casimir 算子、它们的特征值及物理应用（标记态）

**是什么以及为什么。** 一个多重态需要标号。CSA 在多重态*内部*给出 $r$ 个对易的标号（权）。要标记多重态*本身*——要说"这是八重态，那是十重态"——我们需要在每个不可约表示上为常数的算子。这些就是 **Casimir 算子**，由代数构建并与一切对易；由 Schur 引理它们在每个不可约表示上以标量作用，而那些标量恰是物理学家引用的多重态标号。

> **定义 — 二次 Casimir。** 取一组基 $\{T_a\}$，令 $g^{ab}$ 为 Killing 形式矩阵 $g_{ab}=\kappa(T_a,T_b)$ 的逆。**二次 Casimir** 是 $U(\mathfrak{g})$ 中的元素
>
> $$
> C_2=\sum_{a,b} g^{ab}\,T_a T_b .
> $$
>
> 它是**中心的**：对所有 $X\in\mathfrak{g}$ 有 $[C_2,X]=0$。

**$C_2$ 为中心的证明。**
1. 计算 $[C_2,T_c]=\sum_{a,b}g^{ab}\big([T_a,T_c]T_b+T_a[T_b,T_c]\big)$，依对易子与乘积的 *Leibniz 规则*。
2. 代入 $[T_a,T_c]=\sum_d f_{ac}{}^{d}T_d$，另一项同理，得到一些 $f$ 与 $g^{ab}$ 及两个 $T$ 的缩并之和。
3. 定义 $f_{abc}=\sum_d g_{cd} f_{ab}{}^{d}$。*Killing 形式的不变性*（s2），$\kappa([T_a,T_c],T_b)=\kappa(T_a,[T_c,T_b])$，恰好说明 $f_{abc}$ 在其三个指标上是**全反对称的**。
4. 第 2 步的两项，在用 $g^{ab}$ 升指标后，变成*对称*张量 $T_aT_b$ 之和与*反对称*的 $f_{abc}$ 的缩并（带重新标号），它消失。因此对所有 $c$ 有 $[C_2,T_c]=0$。$\blacksquare$

> **定理 — Casimir 特征值（Freudenthal–Weyl）。** 在不可约表示 $V(\lambda)$ 上，二次 Casimir 以标量作用
>
> $$
> C_2\big|_{V(\lambda)}=(\lambda,\lambda+2\rho)=(\lambda+\rho,\lambda+\rho)-(\rho,\rho),
> $$
>
> 其中 $\rho$ 是 Weyl 向量，$(\cdot,\cdot)$ 是由 Killing 形式诱导的内积。

**证明。**
1. 由 Schur 引理（与不可约表示对易的算子是标量），$C_2$ 在 $V(\lambda)$ 上以一个数作用；在最高权向量 $v_\lambda$ 上计算它。
2. 把 $C_2$ 分成 Cartan 部分与根部分：$C_2=\sum_{i,j}g^{ij}H_iH_j+\sum_{\alpha>0}(E_\alpha E_{-\alpha}+E_{-\alpha}E_\alpha)$，利用根空间分解重新组织。
3. 在 $v_\lambda$ 上：升算子 $E_\alpha$（$\alpha>0$）将它湮灭（最高权，s6），所以只有 $E_\alpha E_{-\alpha}$ 经由对易子 $E_\alpha E_{-\alpha}=E_{-\alpha}E_\alpha+[E_\alpha,E_{-\alpha}]=E_{-\alpha}E_\alpha+H_\alpha$ 留存，而 $E_{-\alpha}E_\alpha v_\lambda=0$。
4. 汇总：$C_2 v_\lambda=\big((\lambda,\lambda)+\sum_{\alpha>0}(\lambda,\alpha)\big)v_\lambda=(\lambda,\lambda+2\rho)v_\lambda$，用到由 *Weyl 向量的定义* 得到的 $2\rho=\sum_{\alpha>0}\alpha$。$\blacksquare$

**习题例 — $\mathfrak{su}(2)$ 的 Casimir。** 这里 $C_2$ 是（至多差一个归一化）$J^2=J_1^2+J_2^2+J_3^2$。对自旋 $j$，$\lambda=2j\,\omega$，公式给出特征值 $\propto j(j+1)$——著名的 $J^2|j,m\rangle=j(j+1)|j,m\rangle$，现在被看作 $(\lambda,\lambda+2\rho)$ 的一个特例。对多重态中每个 $m$ 它是*同一个数*：一个多重态标号。

**习题例 — $\mathfrak{su}(3)$ 的 Casimir。** 取 $\lambda=(p,q)$，公式算得
$$
C_2(p,q)=\tfrac13\big(p^2+q^2+pq+3p+3q\big),
$$
所以 $\mathbf3=(1,0)\Rightarrow C_2=\tfrac43$，八重态 $(1,1)\Rightarrow C_2=3$，十重态 $(3,0)\Rightarrow C_2=6$。不同的多重态得到不同的 Casimir 值——恰是完整命名一个态（在同位旋和超荷之外）所需的第二个标号。

> **态在实验室中如何被标记。** 一个强子的量子数是：命名其 $SU(3)$ 多重态（哪个八重态/十重态）的 **Casimir**，然后是定位它在多重态中位置的**权** $(t_3,y)$，再然后是用于自旋的另一个 $\mathfrak{su}(2)$ Casimir $j(j+1)$ 和权 $m$。独立 Casimir 的个数等于**秩** $r$（对 $\mathfrak{su}(3)$ 有两个：二次和三次），它们与那 $r$ 个权标号一起，完全标定每个态。这就是整个分类的操作含义：*标记粒子的守恒量子数，就是表示的 Casimir 算子的特征值与权。*

> **易错点。** 更高秩的代数需要*不止一个* Casimir 来分开所有不可约表示（$\mathfrak{su}(3)$ 还需要三次 Casimir——单凭二次无法区分所有 $(p,q)$ 与 $(q,p)$ 对）。这个个数恰好是秩。

---

*我们从一个承诺出发：对表示分类就是对自然界所允许的多重态分类。我们兑现了它。结构理论（Killing 形式、半单性）隔离出好的代数；根系与 Dynkin 图把每个代数约简为几个整数，并给出有限的 Cartan–Killing 名单；最高权定理与 Verma 构造把每个支配权变成一个具体的多重态；Weyl 公式以闭式数出维数与权；而 Casimir 算子交还了实验者列表的那些量子数本身。$\mathfrak{su}(3)$ 的六边形不是八重法的隐喻——它就是权图，而 $\Omega^-$ 一直在格的一个空角落里等待，直到这套数学被相信。先读一遍，把握从 Killing 形式到 Casimir 特征值的脉络；当你需要这台机器时再回到任一加框定理。被分类的对称性，就是关于什么能存在的目录。*
