[English](README.md) · **中文**

# 数学指南

一个图文并茂、自成体系的数学库 —— 完整的 **微积分**、**拓扑学** 与 **统计学**
课程，外加一套完整的 **理论物理数学** 工具箱（线性代数、复分析、微分几何、
群论、泛函分析,以及数学物理方法),每一科都从基础一路讲到研究生级别的严格理论。
每份指南都是 **Markdown** 文件,可直接在 GitHub 上阅读（数学公式使用
[KaTeX](https://katex.org/) 风格的 LaTeX）,并提供 **英文** 与 **简体中文** 两种语言。

## 开始阅读

每份指南都有 **英文** 与 **简体中文** 两个版本 —— 用每个文件顶部的
`English · 中文` 切换链接即可。可从下方的学习路径与主题表格直接进入相应章节。

> 英文索引请见 **[README.md](README.md)**。术语表本身即为英↔中双语，两种语言通用。

## 微积分学习路径

| 步骤 | 主题 | 位置 |
| --- | --- | --- |
| 0 · 基础 | 函数、直线、三角 | [`complete-guide.zh.md#s1`](calculus/complete-guide.zh.md#s1) |
| 1 · 微积分一 | 极限与连续 | [`complete-guide.zh.md#s3`](calculus/complete-guide.zh.md#s3) |
| 2 · 微积分一 | 导数及其应用 | [`complete-guide.zh.md#s6`](calculus/complete-guide.zh.md#s6) |
| 3 · 微积分二 | 积分及其应用 | [`complete-guide.zh.md#s14`](calculus/complete-guide.zh.md#s14) |
| 4 · 微积分二 | 数列与级数 | [`complete-guide.zh.md#s23`](calculus/complete-guide.zh.md#s23) |
| 5 · 微积分二 | 参数、极坐标与复数 | [`complete-guide.zh.md#s26`](calculus/complete-guide.zh.md#s26) |
| 6 · 微积分三 | 多元与向量微积分 | [`multivariable-vector.zh.md`](calculus/multivariable-vector.zh.md) |
| 7 · 进阶 | 微分方程 | [`differential-equations.zh.md`](calculus/differential-equations.zh.md) |
| 8 · 精通 | 分析基础（严格化） | [`analysis-foundations.zh.md`](calculus/analysis-foundations.zh.md) |

## 拓扑学学习路径

| 步骤 | 主题 | 位置 |
| --- | --- | --- |
| 0 · 基础 | 集合、函数与度量空间 | [`general-topology.zh.md#s1`](topology/general-topology.zh.md#s1) |
| 1 · 点集 | 拓扑空间、基、闭包 | [`general-topology.zh.md#s3`](topology/general-topology.zh.md#s3) |
| 2 · 点集 | 连续与构造 | [`general-topology.zh.md#s7`](topology/general-topology.zh.md#s7) |
| 3 · 点集 | 连通性与紧性 | [`general-topology.zh.md#s10`](topology/general-topology.zh.md#s10) |
| 4 · 点集 | 分离、可数性与度量化 | [`general-topology.zh.md#s16`](topology/general-topology.zh.md#s16) |
| 5 · 点集 | 收敛与完备性（网、滤子、Baire） | [`general-topology.zh.md#s20`](topology/general-topology.zh.md#s20) |
| 6 · 代数 | 同伦与基本群 | [`algebraic-topology.zh.md#s0`](topology/algebraic-topology.zh.md#s0) |
| 7 · 代数 | 覆叠空间 | [`algebraic-topology.zh.md#s6`](topology/algebraic-topology.zh.md#s6) |
| 8 · 精通 | 同调与上同调 | [`algebraic-topology.zh.md#s9`](topology/algebraic-topology.zh.md#s9) |

## 目录

### 微积分 — [`calculus/`](calculus/)

**核心课程**

| 指南 | 文件 | 内容 |
| --- | --- | --- |
| 完整教程 | [`complete-guide.zh.md`](calculus/complete-guide.zh.md) | 单变量完整课程（微积分一、二），30 节，参照 Banner《Calculus Lifesaver》 |
| 多元与向量微积分 | [`multivariable-vector.zh.md`](calculus/multivariable-vector.zh.md) | 微积分三：偏导数、梯度、拉格朗日乘子、重积分、格林/斯托克斯/散度定理 |
| 微分方程 | [`differential-equations.zh.md`](calculus/differential-equations.zh.md) | 一阶/二阶常微分方程、方程组、拉普拉斯变换、级数与数值方法 |
| 分析基础 | [`analysis-foundations.zh.md`](calculus/analysis-foundations.zh.md) | 严格理论：完备性、ε–δ、一致收敛、黎曼积分（含证明） |

**伴读与参考**

| 指南 | 文件 | 适合 |
| --- | --- | --- |
| 从零推导 | [`derived-from-scratch.zh.md`](calculus/derived-from-scratch.zh.md) | 单变量微积分的"证明优先"伴读 |
| 直观全景 | [`connected-map.zh.md`](calculus/connected-map.zh.md) | 快速把握各概念如何相互关联 |
| 术语表（英↔中） | [`glossary.md`](calculus/glossary.md) | 可搜索的英文↔简体中文术语对照（双语） |

### 拓扑学 — [`topology/`](topology/)

| 指南 | 文件 | 内容 |
| --- | --- | --- |
| 一般拓扑 | [`general-topology.zh.md`](topology/general-topology.zh.md) | 点集：度量与拓扑空间、连续、连通与紧、分离公理、度量化、网/滤子、Baire（23 节） |
| 代数拓扑 | [`algebraic-topology.zh.md`](topology/algebraic-topology.zh.md) | 同伦与基本群、覆叠空间、奇异/单纯同调与上同调（15 节） |
| 术语表（英↔中） | [`glossary.md`](topology/glossary.md) | 双语拓扑术语对照 |

## 统计学学习路径

| 步骤 | 主题 | 位置 |
| --- | --- | --- |
| 0 · 入门课程 | 描述数据 | [`complete-guide.zh.md#s1`](statistics/complete-guide.zh.md#s1) |
| 1 · 入门课程 | 概率基础 | [`complete-guide.zh.md#s4`](statistics/complete-guide.zh.md#s4) |
| 2 · 入门课程 | 分布与中心极限定理 | [`complete-guide.zh.md#s7`](statistics/complete-guide.zh.md#s7) |
| 3 · 入门课程 | 推断：区间与检验 | [`complete-guide.zh.md#s9`](statistics/complete-guide.zh.md#s9) |
| 4 · 概率 | 概率论 | [`probability.zh.md#s0`](statistics/probability.zh.md#s0) |
| 5 · 概率 | 极限定理（大数定律与 CLT） | [`probability.zh.md#s14`](statistics/probability.zh.md#s14) |
| 6 · 推断 | 数理统计推断 | [`inference.zh.md#s0`](statistics/inference.zh.md#s0) |
| 7 · 回归 | 回归与线性模型 | [`regression.zh.md#s0`](statistics/regression.zh.md#s0) |
| 8 · 精通 | 贝叶斯推断及更多 | [`inference.zh.md#s13`](statistics/inference.zh.md#s13) |

### 统计学 — [`statistics/`](statistics/)

| 指南 | 文件 | 内容 |
| --- | --- | --- |
| 完整教程 | [`complete-guide.zh.md`](statistics/complete-guide.zh.md) | 入门课程：描述数据、概率与推断（15 节） |
| 概率论 | [`probability.zh.md`](statistics/probability.zh.md) | 公理、随机变量、矩与矩母函数、联合分布、大数定律与 CLT（19 节） |
| 统计推断 | [`inference.zh.md`](statistics/inference.zh.md) | 数理统计：似然、MLE、Cramér–Rao、Neyman–Pearson、贝叶斯与非参数（17 节） |
| 回归与线性模型 | [`regression.zh.md`](statistics/regression.zh.md) | 矩阵形式最小二乘、方差分析、逻辑回归、GLM、正则化（14 节） |
| 术语表（英↔中） | [`glossary.md`](statistics/glossary.md) | 双语统计术语对照 |

## 理论物理数学学习路径

支撑经典力学、电动力学、量子力学、统计力学、广义相对论与场论的数学工具 ——
每一份都达到与上述课程相同的「零基础、完整证明」标准。

| 步骤 | 主题 | 位置 |
| --- | --- | --- |
| 0 · 基础 | 线性代数（向量 → 谱定理） | [`linear-algebra.zh.md#s1`](linear-algebra/linear-algebra.zh.md#s1) |
| 1 · 方法 | 复分析 | [`complex-analysis.zh.md#s0`](complex-analysis/complex-analysis.zh.md#s0) |
| 2 · 方法 | 傅里叶分析与积分变换 | [`fourier-transforms.zh.md#s0`](math-methods/fourier-transforms.zh.md#s0) |
| 3 · 方法 | 偏微分方程 | [`partial-differential-equations.zh.md#s0`](math-methods/partial-differential-equations.zh.md#s0) |
| 4 · 方法 | 特殊函数 | [`special-functions.zh.md#s0`](math-methods/special-functions.zh.md#s0) |
| 5 · 力学 | 变分法与最小作用量 | [`calculus-of-variations.zh.md#s0`](math-methods/calculus-of-variations.zh.md#s0) |
| 6 · 相对论 | 微分几何与张量 | [`differential-geometry.zh.md#s0`](differential-geometry/differential-geometry.zh.md#s0) |
| 7 · 对称性 | 群论与表示论 | [`group-theory.zh.md#s0`](group-theory/group-theory.zh.md#s0) |
| 8 · 量子 | 泛函分析与希尔伯特空间 | [`functional-analysis.zh.md#s0`](functional-analysis/functional-analysis.zh.md#s0) |

### 理论物理数学

| 工具 | 文件 | 支撑 |
| --- | --- | --- |
| 线性代数 | [`linear-algebra.zh.md`](linear-algebra/linear-algebra.zh.md) | 向量空间 → 本征值、内积、谱定理、张量积、狄拉克左右矢 —— 量子力学的语言（15 节） |
| 复分析 | [`complex-analysis.zh.md`](complex-analysis/complex-analysis.zh.md) | 全纯性与柯西–黎曼、围道积分、留数、洛朗级数、共形与莫比乌斯映射、解析延拓（16 节） |
| 傅里叶分析与积分变换 | [`fourier-transforms.zh.md`](math-methods/fourier-transforms.zh.md) | 傅里叶级数与变换、狄拉克 δ、卷积、拉普拉斯变换、格林函数（13 节） |
| 偏微分方程 | [`partial-differential-equations.zh.md`](math-methods/partial-differential-equations.zh.md) | 波动/热传导/拉普拉斯/薛定谔、特征线、分离变量、施图姆–刘维尔、格林函数（14 节） |
| 特殊函数 | [`special-functions.zh.md`](math-methods/special-functions.zh.md) | Γ 与 B 函数、勒让德与球谐、贝塞尔、厄米、拉盖尔、生成函数（11 节） |
| 变分法 | [`calculus-of-variations.zh.md`](math-methods/calculus-of-variations.zh.md) | 欧拉–拉格朗日、哈密顿原理、诺特定理、哈密顿形式、场（11 节） |
| 微分几何与张量 | [`differential-geometry.zh.md`](differential-geometry/differential-geometry.zh.md) | 流形、张量与度规、微分形式、联络、曲率、爱因斯坦方程 —— 广义相对论的语言（14 节） |
| 群论与表示论 | [`group-theory.zh.md`](group-theory/group-theory.zh.md) | 群、特征标、李群与李代数、su(2)/SU(3)、克莱布什–戈尔丹 —— 对称性与粒子物理（14 节） |
| 泛函分析与希尔伯特空间 | [`functional-analysis.zh.md`](functional-analysis/functional-analysis.zh.md) | 巴拿赫/希尔伯特空间、算符与伴随、谱、谱定理、分布 —— 严格的量子力学（13 节） |

### 进阶专题

| 工具 | 文件 | 支撑 |
| --- | --- | --- |
| 纤维丛与规范场论 | [`fiber-bundles-gauge.zh.md`](differential-geometry/fiber-bundles-gauge.zh.md) | 纤维丛、联络与曲率、Wilson 圈、Yang–Mills、陈类、磁单极与 Aharonov–Bohm —— 力的几何（12 节） |
| 进阶张量分析 | [`tensor-analysis.zh.md`](differential-geometry/tensor-analysis.zh.md) | 张量密度、Hodge 星、协变积分、电磁与能动张量、标架、旋量（11 节） |
| 随机过程与路径积分 | [`stochastic-processes.zh.md`](math-methods/stochastic-processes.zh.md) | 马尔可夫链、布朗运动、Itô 微积分与 SDE、Fokker–Planck、Feynman–Kac、费曼路径积分（13 节） |
| 李代数表示论 | [`lie-representations.zh.md`](group-theory/lie-representations.zh.md) | 基灵型、根系与 Dynkin 图、最高权、Weyl 特征标公式、su(3) 多重态、杨表、Casimir（12 节） |

*（之后可以按同样的方式继续加入更多学科。）*
