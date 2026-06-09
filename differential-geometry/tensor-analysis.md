**English** · [中文](tensor-analysis.zh.md)

# Advanced Tensor Analysis, *calculus on curved space, in coordinates.*

*A working manual for tensor calculus as it is actually used in relativity and continuum physics. Where the companion guide built the geometry conceptually, this one rolls up its sleeves: we manipulate indices, weigh tensor densities, raise and lower with the metric, differentiate covariantly, integrate with $\sqrt{-g}$, and read Maxwell's equations, the conservation of energy–momentum, and the Dirac operator straight off the page. Every identity is derived; every index is accounted for.*

[← Back to all guides](../README.md)

**Prerequisite.** This guide is the applied, computational companion to the **Differential Geometry & Tensors** guide. From it we take, and restate in one line each as we use them: a **tensor** is a multilinear object whose components carry the transformation law $T'^{\mu}{}_{\nu}=\frac{\partial x'^\mu}{\partial x^\alpha}\frac{\partial x^\beta}{\partial x'^\nu}T^{\alpha}{}_{\beta}$ under a change of coordinates; the **metric** $g_{\mu\nu}$ is a symmetric non-degenerate $(0,2)$ tensor; and the **covariant derivative** $\nabla$ corrects ordinary partials with the **Christoffel symbols** $\Gamma^\lambda{}_{\mu\nu}=\tfrac12 g^{\lambda\sigma}(\partial_\mu g_{\sigma\nu}+\partial_\nu g_{\sigma\mu}-\partial_\sigma g_{\mu\nu})$. We do **not** re-prove those facts; we put them to work. Throughout, repeated indices are summed (Einstein convention), Greek indices $\mu,\nu,\dots$ run over the $n$ spacetime coordinates, and we write $\partial_\mu\equiv\partial/\partial x^\mu$.

## Part A · The algebra of indices

<a id="s0"></a>
### Motivation — coordinate-explicit tensor calculus as the working language of physics

The companion guide preaches coordinate-freedom: a tensor *is* a geometric object, and the components are just its shadow in a chosen chart. That is the right way to *understand* the theory. It is not, however, how anyone *computes* a geodesic, an electromagnetic field, or the Einstein tensor of a metric written on paper. For that you need the dual skill: fluent, reliable manipulation of indices, densities, and the metric factor $\sqrt{-g}$.

#### What problem are we solving?

A physicist hands you a metric — say the Schwarzschild line element — and asks for the divergence of a current, the energy radiated by an electromagnetic wave, or the conserved quantities of an orbit. Each answer is a *number* or a *field*, extracted by a definite sequence of index operations. The danger is that intermediate quantities such as $\partial_\mu V^\nu$, or the Levi-Civita *symbol* $\epsilon_{\mu\nu\rho\sigma}$, look like tensors but are **not**: they fail to transform correctly, and using them as if they were tensors produces wrong, coordinate-dependent answers. This guide's job is to teach which objects are genuine tensors, which are **densities** (tensors weighted by a power of the Jacobian determinant), and exactly which combinations restore tensorial behavior.

#### The plan

Part A is pure algebra: the **quotient theorem** (a converse test for tensors), symmetric/antisymmetric decomposition, contraction, and then **tensor densities**, the **Levi-Civita symbol versus tensor**, and the role of $\sqrt{-g}$ (s1–s2). Part B is the metric in practice and **covariant differentiation** of arbitrary tensors, the divergence, the Laplacian, and the crucial simplification $\nabla_\mu(\sqrt{-g}\,V^\mu)=\partial_\mu(\sqrt{-g}\,V^\mu)$ (s3–s4). Part C is calculus of forms — the **Hodge star**, the **codifferential**, **integration** with the invariant volume form, and the **divergence theorem** (s5–s6). Part D is physics done right: **electromagnetism** (s7), the **stress–energy tensor** and its conservation (s8), **symmetries** and conserved charges via the Lie derivative and Killing vectors (s9), and a first concrete look at **spinors** and the **Dirac operator** on curved space (s10).

> **Intuition.** The transformation law is a contract. A genuine tensor honours it; a density honours a *modified* contract with an extra Jacobian factor. Almost every "paradox" in index gymnastics — why $\partial_\mu V^\mu$ is not the divergence, why $d^nx$ is not an invariant, why $\epsilon_{\mu\nu\rho\sigma}$ is not a tensor — is the same contract being silently broken and then repaired by inserting $\sqrt{-g}$.

<a id="s1"></a>
### Tensor algebra in components: the quotient theorem, symmetry, and contraction

We collect the algebraic operations that turn tensors into new tensors, proving in each case that the transformation contract is preserved.

#### The transformation contract, restated

> **Definition — tensor components.** Under a coordinate change $x\mapsto x'$, write the Jacobian and its inverse as
>
> $$
> J^{\mu'}{}_{\alpha}=\frac{\partial x'^{\mu}}{\partial x^{\alpha}},\qquad (J^{-1})^{\alpha}{}_{\mu'}=\frac{\partial x^{\alpha}}{\partial x'^{\mu}}.
> $$
>
> A $(p,q)$ **tensor** has components carrying one factor of $J$ per upper index and one factor of $J^{-1}$ per lower index:
>
> $$
> T'^{\mu_1\dots\mu_p}{}_{\nu_1\dots\nu_q}=\frac{\partial x'^{\mu_1}}{\partial x^{\alpha_1}}\cdots\frac{\partial x^{\beta_1}}{\partial x'^{\nu_1}}\cdots\,T^{\alpha_1\dots\alpha_p}{}_{\beta_1\dots\beta_q}.
> $$

These Jacobians satisfy $J^{\mu'}{}_\alpha (J^{-1})^{\alpha}{}_{\nu'}=\delta^{\mu'}{}_{\nu'}$ by the chain rule $\frac{\partial x'^\mu}{\partial x^\alpha}\frac{\partial x^\alpha}{\partial x'^\nu}=\frac{\partial x'^\mu}{\partial x'^\nu}=\delta^\mu_\nu$. This single relation does all the work below.

#### Contraction lowers rank by $(1,1)$

> **Theorem (contraction).** If $T^{\mu}{}_{\nu}$ are the components of a $(1,1)$ tensor, then the single number $S=T^{\mu}{}_{\mu}$ (summed) is a scalar — a $(0,0)$ tensor. More generally, summing one upper against one lower index of a $(p,q)$ tensor yields a $(p-1,q-1)$ tensor.

*Proof.*
1. Write the transformation law for the contracted pair: $T'^{\mu}{}_{\mu}=\dfrac{\partial x'^\mu}{\partial x^\alpha}\dfrac{\partial x^\beta}{\partial x'^\mu}\,T^{\alpha}{}_{\beta}$, by the definition of a $(1,1)$ tensor with the two free indices identified and summed.
2. Group the two Jacobian factors that share the summed index $\mu$: they form $\dfrac{\partial x^\beta}{\partial x'^\mu}\dfrac{\partial x'^\mu}{\partial x^\alpha}$.
3. By the chain rule this equals $\dfrac{\partial x^\beta}{\partial x^\alpha}=\delta^\beta_\alpha$ (the coordinates $x^\alpha$ are independent, so $\partial x^\beta/\partial x^\alpha$ is the Kronecker delta).
4. Therefore $T'^{\mu}{}_{\mu}=\delta^\beta_\alpha T^{\alpha}{}_{\beta}=T^{\alpha}{}_{\alpha}$. The number is unchanged by the coordinate change, which is exactly the statement that it is a scalar. $\blacksquare$
5. The general case is identical: the contracted index pair contributes a $\delta$ exactly as in step 3, while the remaining $p-1$ upper and $q-1$ lower indices keep their Jacobian factors, giving the $(p-1,q-1)$ law.

> **Worked example.** Take $T^{\mu}{}_{\nu}=\mathrm{diag}(2,3,5,7)$ in 4 dimensions. Then $T^{\mu}{}_{\mu}=2+3+5+7=17$. This $17$ is the **trace**, and it is the same in every coordinate system — a genuine invariant — whereas the individual diagonal entries are not.

#### Symmetric and antisymmetric parts

> **Definition.** For a $(0,2)$ tensor $T_{\mu\nu}$ define
>
> $$
> T_{(\mu\nu)}=\tfrac12\bigl(T_{\mu\nu}+T_{\nu\mu}\bigr)\quad\text{(symmetric part)},\qquad
> T_{[\mu\nu]}=\tfrac12\bigl(T_{\mu\nu}-T_{\nu\mu}\bigr)\quad\text{(antisymmetric part)}.
> $$
>
> For $k$ indices, parentheses mean the average over all $k!$ permutations, brackets the same average weighted by the **sign** of each permutation (the parity, $+1$ for even, $-1$ for odd).

> **Theorem.** $T_{(\mu\nu)}$ and $T_{[\mu\nu]}$ are themselves $(0,2)$ tensors, and every $(0,2)$ tensor decomposes uniquely as $T_{\mu\nu}=T_{(\mu\nu)}+T_{[\mu\nu]}$.

*Proof.*
1. The transformation law $T'_{\mu\nu}=\dfrac{\partial x^\alpha}{\partial x'^\mu}\dfrac{\partial x^\beta}{\partial x'^\nu}T_{\alpha\beta}$ is **linear** in the components $T_{\alpha\beta}$, so any fixed linear combination of components transforms the same way.
2. The swapped object $T_{\nu\mu}$ transforms as $T'_{\nu\mu}=\dfrac{\partial x^\alpha}{\partial x'^\nu}\dfrac{\partial x^\beta}{\partial x'^\mu}T_{\alpha\beta}$; relabelling the dummy indices $\alpha\leftrightarrow\beta$ shows this equals $\dfrac{\partial x^\alpha}{\partial x'^\mu}\dfrac{\partial x^\beta}{\partial x'^\nu}T_{\beta\alpha}$, i.e. the swap acts on the components, not the Jacobians.
3. Hence $\tfrac12(T'_{\mu\nu}\pm T'_{\nu\mu})=\dfrac{\partial x^\alpha}{\partial x'^\mu}\dfrac{\partial x^\beta}{\partial x'^\nu}\cdot\tfrac12(T_{\alpha\beta}\pm T_{\beta\alpha})$ — each part carries the correct two factors of $J^{-1}$, so each is a $(0,2)$ tensor.
4. Adding the two parts returns $T_{\mu\nu}$; the decomposition is unique because if $S+A=0$ with $S$ symmetric and $A$ antisymmetric, then swapping indices gives $S-A=0$, so $S=A=0$. $\blacksquare$

> **Pitfall — symmetry survives index moves only with care.** If $T_{\mu\nu}$ is symmetric, so is $T^{\mu\nu}=g^{\mu\alpha}g^{\nu\beta}T_{\alpha\beta}$, but a *mixed* object $T^\mu{}_\nu$ has no symmetry property because its two indices live at different heights. A frequent error is to "transpose" $T^\mu{}_\nu$ as if it were a matrix; that operation is not coordinate-covariant.

> **Useful identity.** The contraction of a symmetric tensor $S^{\mu\nu}$ with an antisymmetric tensor $A_{\mu\nu}$ vanishes: $S^{\mu\nu}A_{\mu\nu}=0$.

*Proof.* Rename dummies $\mu\leftrightarrow\nu$: $S^{\mu\nu}A_{\mu\nu}=S^{\nu\mu}A_{\nu\mu}$. Now use $S^{\nu\mu}=S^{\mu\nu}$ (symmetry) and $A_{\nu\mu}=-A_{\mu\nu}$ (antisymmetry): the right side is $-S^{\mu\nu}A_{\mu\nu}$. A quantity equal to its own negative is zero. $\blacksquare$

#### The quotient theorem — a converse test

It is often easier to verify that *some contraction* of an object is a tensor than to check the object directly. The quotient theorem says that is enough.

> **Theorem (quotient theorem).** Let $K(\mu,\nu)$ be a doubly-indexed array of numbers in every coordinate system. Suppose that for **every** vector (i.e. $(1,0)$ tensor) $V^\nu$, the quantity $W_\mu=K(\mu,\nu)V^\nu$ is the component array of a $(0,1)$ tensor (a covector). Then $K(\mu,\nu)$ are the components of a $(0,2)$ tensor $K_{\mu\nu}$.

*Proof.*
1. By hypothesis $W_\mu=K(\mu,\nu)V^\nu$ transforms as a covector: $W'_{\mu}=\dfrac{\partial x^\alpha}{\partial x'^\mu}W_\alpha$, for every input vector.
2. Expand both sides in components. Left: $W'_\mu=K'(\mu,\nu)V'^{\nu}$ by definition of $K'$ in the primed frame. Right: $\dfrac{\partial x^\alpha}{\partial x'^\mu}K(\alpha,\beta)V^\beta$.
3. Express the input in the primed frame: since $V$ is a vector, $V^\beta=\dfrac{\partial x^\beta}{\partial x'^\nu}V'^{\nu}$. Substitute into the right side: $\dfrac{\partial x^\alpha}{\partial x'^\mu}\dfrac{\partial x^\beta}{\partial x'^\nu}K(\alpha,\beta)\,V'^{\nu}$.
4. Equate the two expressions for $W'_\mu$: $\Bigl[K'(\mu,\nu)-\dfrac{\partial x^\alpha}{\partial x'^\mu}\dfrac{\partial x^\beta}{\partial x'^\nu}K(\alpha,\beta)\Bigr]V'^{\nu}=0$ for **all** $V'^\nu$.
5. A linear form that vanishes on every vector has zero coefficients (choose $V'^\nu$ to be each basis vector in turn). Hence the bracket vanishes:
$$
K'(\mu,\nu)=\frac{\partial x^\alpha}{\partial x'^\mu}\frac{\partial x^\beta}{\partial x'^\nu}K(\alpha,\beta),
$$
which is precisely the $(0,2)$ tensor transformation law. $\blacksquare$

> **Worked example — the metric passes the test.** The line element $ds^2=g_{\mu\nu}\,dx^\mu dx^\nu$ is a scalar (an invariant length). Writing it as $g_{\mu\nu}V^\mu W^\nu$ for arbitrary tangent vectors $V,W$, the result is a scalar for all inputs; applying the quotient theorem twice shows $g_{\mu\nu}$ is a genuine $(0,2)$ tensor. We never had to inspect its transformation law directly.

<a id="s2"></a>
### Tensor densities, the Levi-Civita symbol versus tensor, and $\sqrt{-g}$

Several indispensable objects — the volume element, the permutation symbol, the metric determinant — are **not** tensors. They are **densities**, and understanding their weight is the key to invariant integration.

#### Definition of a density

> **Definition — tensor density of weight $w$.** A **tensor density of weight $w$** transforms like a tensor but with an extra factor of the Jacobian determinant raised to the power $w$:
>
> $$
> \tilde T'^{\mu\dots}{}_{\nu\dots}=\left(\det\frac{\partial x}{\partial x'}\right)^{w}\frac{\partial x'^\mu}{\partial x^\alpha}\cdots\frac{\partial x^\beta}{\partial x'^\nu}\cdots\,\tilde T^{\alpha\dots}{}_{\beta\dots}.
> $$
>
> Here $\det\frac{\partial x}{\partial x'}=\det(J^{-1})$ is the determinant of the inverse Jacobian. A weight-$0$ density is an ordinary tensor.

#### The Levi-Civita symbol is a density of weight $\pm1$, not a tensor

> **Definition — Levi-Civita symbol.** In $n$ dimensions, $\epsilon_{\mu_1\dots\mu_n}$ is the **fixed** array equal to $+1$ if $(\mu_1,\dots,\mu_n)$ is an even permutation of $(1,\dots,n)$, $-1$ if odd, and $0$ if any index repeats. The same numerical array is declared in every coordinate system — this is what makes it a symbol, not a tensor.

> **Theorem.** The Levi-Civita symbol $\epsilon_{\mu_1\dots\mu_n}$, taken with these fixed values in all frames, is a tensor **density of weight $-1$**. The upper-index symbol $\epsilon^{\mu_1\dots\mu_n}$ (same values) is a density of weight $+1$.

*Proof.*
1. Recall the determinant expansion: for any $n\times n$ matrix $A^\mu{}_\nu$, $\det A\,\epsilon_{\nu_1\dots\nu_n}=\epsilon_{\mu_1\dots\mu_n}A^{\mu_1}{}_{\nu_1}\cdots A^{\mu_n}{}_{\nu_n}$. This is the cofactor/Leibniz formula for the determinant, and it holds identically.
2. Apply it with $A^\mu{}_\nu=\dfrac{\partial x^\mu}{\partial x'^\nu}=(J^{-1})^\mu{}_\nu$, whose determinant is $\det(J^{-1})$:
$$
\det(J^{-1})\,\epsilon_{\nu_1\dots\nu_n}=\frac{\partial x^{\mu_1}}{\partial x'^{\nu_1}}\cdots\frac{\partial x^{\mu_n}}{\partial x'^{\nu_n}}\,\epsilon_{\mu_1\dots\mu_n}.
$$
3. Read this as a transformation law. The right side is exactly "tensor transformation of $\epsilon$"; the left side is "$\det(J^{-1})$ times the (same) symbol in the new frame." Solving, the symbol in the new frame equals $(\det(J^{-1}))^{-1}$ times the tensor-transformed symbol — but we *declare* the symbol unchanged, so the discrepancy $(\det(J^{-1}))^{+1}$ is absorbed by assigning weight $w=-1$. Matching to the definition with $w=-1$ confirms it. $\blacksquare$

#### The metric determinant carries weight $-2$

> **Theorem.** Let $g=\det(g_{\mu\nu})$. Under a coordinate change, $g'=(\det J^{-1})^{2}\,g$. Thus $g$ is a scalar density of weight $-2$, and $\sqrt{|g|}$ is a scalar density of weight $-1$.

*Proof.*
1. The metric transforms as $g'_{\mu\nu}=\dfrac{\partial x^\alpha}{\partial x'^\mu}\dfrac{\partial x^\beta}{\partial x'^\nu}g_{\alpha\beta}$, i.e. in matrix form $g'=(J^{-1})^{\mathsf T} g\,(J^{-1})$.
2. Take determinants: $\det g'=\det((J^{-1})^{\mathsf T})\det g\,\det(J^{-1})=(\det J^{-1})^2\det g$, using $\det(AB)=\det A\det B$ and $\det A^{\mathsf T}=\det A$.
3. Hence $g'=(\det J^{-1})^2 g$ (weight $-2$), and taking the square root, $\sqrt{|g'|}=|\det J^{-1}|\sqrt{|g|}$ (weight $-1$, up to the sign that orientation tracks). In Lorentzian signature $g<0$, so we write $\sqrt{-g}$. $\blacksquare$

#### The Levi-Civita *tensor*: multiply the symbol by $\sqrt{-g}$

> **Definition — Levi-Civita tensor.** Define $\varepsilon_{\mu_1\dots\mu_n}=\sqrt{-g}\;\epsilon_{\mu_1\dots\mu_n}$.

> **Theorem.** $\varepsilon_{\mu_1\dots\mu_n}$ is a genuine $(0,n)$ tensor, and the raised version satisfies $\varepsilon^{\mu_1\dots\mu_n}=\dfrac{\mathrm{sgn}(g)}{\sqrt{-g}}\,\epsilon^{\mu_1\dots\mu_n}=-\dfrac{1}{\sqrt{-g}}\,\epsilon^{\mu_1\dots\mu_n}$ in Lorentzian signature.

*Proof.*
1. We claim the product $\sqrt{-g}\,\epsilon_{\mu_1\dots\mu_n}$ transforms as a genuine $(0,n)$ tensor: the density factor $\sqrt{-g}$ (weight $-1$) exactly cancels the symbol's anomalous Jacobian factor, leaving the ordinary tensor law. Steps 2–4 verify this directly.
2. Combine the two transformation laws. The tensor candidate transforms as
$$
\varepsilon'_{\nu_1\dots\nu_n}=\sqrt{-g'}\;\epsilon_{\nu_1\dots\nu_n}=|\det J^{-1}|\sqrt{-g}\;\epsilon_{\nu_1\dots\nu_n}.
$$
3. From the symbol's determinant identity (step 2 of the previous proof), $\sqrt{-g}\,\epsilon_{\nu_1\dots\nu_n}=\dfrac{1}{\det J^{-1}}\,\dfrac{\partial x^{\mu_1}}{\partial x'^{\nu_1}}\cdots\dfrac{\partial x^{\mu_n}}{\partial x'^{\nu_n}}\bigl(\sqrt{-g}\,\epsilon_{\mu_1\dots\mu_n}\bigr)$. Substituting,
$$
\varepsilon'_{\nu_1\dots\nu_n}=\frac{|\det J^{-1}|}{\det J^{-1}}\frac{\partial x^{\mu_1}}{\partial x'^{\nu_1}}\cdots\frac{\partial x^{\mu_n}}{\partial x'^{\nu_n}}\,\varepsilon_{\mu_1\dots\mu_n}.
$$
4. For orientation-preserving changes $\det J^{-1}>0$, the ratio is $+1$ and this is exactly the $(0,n)$ tensor law. $\blacksquare$

> **Worked example — spherical volume.** In $\mathbb{R}^3$ with the flat metric in spherical coordinates, $g=\mathrm{diag}(1,r^2,r^2\sin^2\theta)$ so $\sqrt{g}=r^2\sin\theta$. The invariant volume element $\sqrt{g}\,dr\,d\theta\,d\phi=r^2\sin\theta\,dr\,d\theta\,d\phi$ is the familiar Jacobian factor — and it arose automatically as the density $\sqrt{g}$, with no ad-hoc computation. The bare symbol product $dr\,d\theta\,d\phi$ would have given the wrong, coordinate-dependent volume.

## Part B · The metric and covariant differentiation

<a id="s3"></a>
### The metric in practice: raising/lowering and orthonormal frames

The metric is the conversion device between vectors and covectors, and the bridge to flat-space intuition through orthonormal frames.

#### Raising and lowering

> **Definition.** The **inverse metric** $g^{\mu\nu}$ is defined by $g^{\mu\alpha}g_{\alpha\nu}=\delta^\mu_\nu$. Lowering an index means contracting with $g_{\mu\nu}$, raising means contracting with $g^{\mu\nu}$:
>
> $$
> V_\mu=g_{\mu\nu}V^\nu,\qquad V^\mu=g^{\mu\nu}V_\nu.
> $$

> **Theorem (consistency of index gymnastics).** Lowering then raising the same index returns the original tensor.

*Proof.* Lower then raise: $g^{\rho\mu}V_\mu=g^{\rho\mu}g_{\mu\nu}V^\nu=\delta^\rho_\nu V^\nu=V^\rho$, using the inverse relation and the definition of $\delta$. $\blacksquare$

> **Worked example — Minkowski.** With $\eta_{\mu\nu}=\mathrm{diag}(-1,+1,+1,+1)$ a vector $V^\mu=(V^0,V^1,V^2,V^3)$ lowers to $V_\mu=(-V^0,V^1,V^2,V^3)$. The norm $V^\mu V_\mu=-(V^0)^2+(V^1)^2+(V^2)^2+(V^3)^2$ is the squared Minkowski interval — negative for timelike vectors, the sign convention that distinguishes time from space.

#### Orthonormal frames: vielbeins and tetrads

A general metric is messy, but at every single point we can choose a basis in which it looks exactly like flat Minkowski. The change-of-basis matrices that do this are the **vielbeins**.

> **Definition — vielbein / tetrad.** A **vielbein** (German "many legs"; in 4D, **tetrad** or **frame field**) is a set of $n$ covector fields $e^a{}_\mu$, labelled by a **frame index** $a$ (Latin), such that
>
> $$
> g_{\mu\nu}=e^a{}_\mu e^b{}_\nu\,\eta_{ab},
> $$
>
> where $\eta_{ab}=\mathrm{diag}(-1,+1,\dots,+1)$ is the constant **frame metric**. The inverse vielbein $e_a{}^\mu$ satisfies $e^a{}_\mu e_a{}^\nu=\delta^\nu_\mu$ and $e^a{}_\mu e_b{}^\mu=\delta^a_b$.

The intuition: $e^a{}_\mu$ converts a coordinate-basis (curved, "world") index $\mu$ into an orthonormal-frame (flat, "Lorentz") index $a$. In the frame, all geometry is locally Minkowski; the vielbein records how the local flat frame is glued to the coordinate grid.

> **Theorem.** The vielbein decomposition $g_{\mu\nu}=e^a{}_\mu e^b{}_\nu\eta_{ab}$ reproduces the determinant relation $\sqrt{-g}=|\det e^a{}_\mu|\equiv e$.

*Proof.*
1. Read the definition as a matrix equation $g=e^{\mathsf T}\eta\,e$ (suppressing indices, with $e$ the matrix $e^a{}_\mu$).
2. Take determinants: $\det g=(\det e)^2\det\eta$, by multiplicativity and $\det e^{\mathsf T}=\det e$.
3. Since $\det\eta=-1$ in Lorentzian signature, $\det g=-(\det e)^2$, so $-g=(\det e)^2$ and $\sqrt{-g}=|\det e|$. $\blacksquare$

> **Pitfall — two index alphabets.** Frame indices $a,b$ are raised and lowered with the **constant** $\eta_{ab}$; world indices $\mu,\nu$ with $g_{\mu\nu}$. Mixing them — e.g. lowering a frame index with the metric — is meaningless. The vielbein is the *only* legal way to swap between the two alphabets.

> **Why this matters.** Spinors (s10) cannot be defined with world indices at all; they live in representations of the local Lorentz group, which acts on frame indices. The tetrad is therefore not a convenience but a necessity for fermions on curved space.

<a id="s4"></a>
### Covariant differentiation, the divergence, the Laplacian, and $\nabla_\mu(\sqrt{-g}\,V^\mu)=\partial_\mu(\sqrt{-g}\,V^\mu)$

Ordinary partial derivatives of tensor components are not tensors; the covariant derivative repairs this with Christoffel corrections, one per index.

#### The general rule

> **Definition — covariant derivative of a $(p,q)$ tensor.** Each upper index gets a $+\Gamma$ term, each lower index a $-\Gamma$ term:
>
> $$
> \nabla_\lambda T^{\mu_1\dots}{}_{\nu_1\dots}=\partial_\lambda T^{\mu_1\dots}{}_{\nu_1\dots}+\Gamma^{\mu_1}{}_{\lambda\sigma}T^{\sigma\dots}{}_{\nu_1\dots}+\cdots-\Gamma^{\sigma}{}_{\lambda\nu_1}T^{\mu_1\dots}{}_{\sigma\dots}-\cdots
> $$
>
> with one correction term per index in the indicated pattern.

For a scalar $\nabla_\lambda f=\partial_\lambda f$; for a vector $\nabla_\lambda V^\mu=\partial_\lambda V^\mu+\Gamma^\mu{}_{\lambda\sigma}V^\sigma$; for a covector $\nabla_\lambda\omega_\mu=\partial_\lambda\omega_\mu-\Gamma^\sigma{}_{\lambda\mu}\omega_\sigma$. The metric is covariantly constant, $\nabla_\lambda g_{\mu\nu}=0$ (metric compatibility, proved in the companion guide), which is why raising/lowering commutes with $\nabla$.

#### A key contraction of the Christoffel symbol

> **Lemma.** $\Gamma^\mu{}_{\mu\lambda}=\partial_\lambda\ln\sqrt{-g}=\dfrac{1}{\sqrt{-g}}\partial_\lambda\sqrt{-g}$.

*Proof.*
1. Contract the Christoffel definition on its upper index with one lower: $\Gamma^\mu{}_{\mu\lambda}=\tfrac12 g^{\mu\sigma}(\partial_\mu g_{\sigma\lambda}+\partial_\lambda g_{\sigma\mu}-\partial_\sigma g_{\mu\lambda})$.
2. The first and third terms cancel: relabel $\mu\leftrightarrow\sigma$ in the third term, $g^{\mu\sigma}\partial_\sigma g_{\mu\lambda}=g^{\sigma\mu}\partial_\mu g_{\sigma\lambda}$, identical to the first since $g^{\mu\sigma}$ is symmetric. So $\Gamma^\mu{}_{\mu\lambda}=\tfrac12 g^{\mu\sigma}\partial_\lambda g_{\sigma\mu}$.
3. Use **Jacobi's formula** for the derivative of a determinant: $\partial_\lambda\det g=\det g\cdot g^{\mu\sigma}\partial_\lambda g_{\sigma\mu}$ (the trace of inverse-times-derivative). Hence $g^{\mu\sigma}\partial_\lambda g_{\sigma\mu}=\dfrac{1}{g}\partial_\lambda g=\partial_\lambda\ln|g|$.
4. Therefore $\Gamma^\mu{}_{\mu\lambda}=\tfrac12\partial_\lambda\ln|g|=\partial_\lambda\ln\sqrt{|g|}=\partial_\lambda\ln\sqrt{-g}$ (Lorentzian). $\blacksquare$

#### The covariant divergence simplifies

> **Theorem.** For any vector field $V^\mu$,
>
> $$
> \nabla_\mu V^\mu=\frac{1}{\sqrt{-g}}\,\partial_\mu\bigl(\sqrt{-g}\,V^\mu\bigr),
> $$
>
> equivalently $\sqrt{-g}\,\nabla_\mu V^\mu=\partial_\mu(\sqrt{-g}\,V^\mu)$ — the Christoffel symbols disappear from the divergence.

*Proof.*
1. Expand the definition: $\nabla_\mu V^\mu=\partial_\mu V^\mu+\Gamma^\mu{}_{\mu\lambda}V^\lambda$.
2. Substitute the Lemma $\Gamma^\mu{}_{\mu\lambda}=\dfrac{1}{\sqrt{-g}}\partial_\lambda\sqrt{-g}$: $\nabla_\mu V^\mu=\partial_\mu V^\mu+\dfrac{1}{\sqrt{-g}}(\partial_\lambda\sqrt{-g})V^\lambda$.
3. Recognise the right side as a product-rule expansion. Compute $\dfrac{1}{\sqrt{-g}}\partial_\mu(\sqrt{-g}\,V^\mu)=\dfrac{1}{\sqrt{-g}}\bigl[(\partial_\mu\sqrt{-g})V^\mu+\sqrt{-g}\,\partial_\mu V^\mu\bigr]=\dfrac{(\partial_\mu\sqrt{-g})V^\mu}{\sqrt{-g}}+\partial_\mu V^\mu$.
4. The two expressions agree term by term (after relabelling the dummy $\lambda\to\mu$). $\blacksquare$

This is the most-used identity in the subject: it lets you compute divergences and write conservation laws without ever evaluating a Christoffel symbol.

#### The tensor Laplacian (Laplace–Beltrami operator)

> **Definition.** The **Laplacian** of a scalar $f$ is $\Box f=\nabla_\mu\nabla^\mu f=g^{\mu\nu}\nabla_\mu\nabla_\nu f$.

> **Theorem.** $\Box f=\dfrac{1}{\sqrt{-g}}\partial_\mu\bigl(\sqrt{-g}\,g^{\mu\nu}\partial_\nu f\bigr)$.

*Proof.*
1. Since $f$ is a scalar, $\nabla_\nu f=\partial_\nu f$, so the "gradient vector" is $V^\mu=g^{\mu\nu}\partial_\nu f$.
2. The Laplacian is the divergence of this vector: $\Box f=\nabla_\mu V^\mu$.
3. Apply the divergence theorem of the previous box: $\Box f=\dfrac{1}{\sqrt{-g}}\partial_\mu(\sqrt{-g}\,V^\mu)=\dfrac{1}{\sqrt{-g}}\partial_\mu(\sqrt{-g}\,g^{\mu\nu}\partial_\nu f)$. $\blacksquare$

> **Worked example — flat-space Laplacian recovered.** In spherical coordinates with $\sqrt{g}=r^2\sin\theta$ and $g^{rr}=1$, the radial part is $\dfrac{1}{r^2\sin\theta}\partial_r(r^2\sin\theta\cdot 1\cdot\partial_r f)=\dfrac{1}{r^2}\partial_r(r^2\partial_r f)$, the textbook radial Laplacian — derived in one line from the master formula, no vector-calculus identities memorised.

## Part C · Forms, the star, and integration

<a id="s5"></a>
### The Hodge star operator and the codifferential

The Hodge star turns a $k$-form into its complementary $(n-k)$-form, and is the engine behind duality in electromagnetism and the definition of adjoint derivatives.

> **Definition — Hodge star.** On an $n$-dimensional manifold with metric, the **Hodge star** $\star$ maps a $k$-form $\alpha$ with components $\alpha_{\mu_1\dots\mu_k}$ to the $(n-k)$-form
>
> $$
> (\star\alpha)_{\nu_1\dots\nu_{n-k}}=\frac{1}{k!}\,\varepsilon_{\nu_1\dots\nu_{n-k}}{}^{\mu_1\dots\mu_k}\,\alpha_{\mu_1\dots\mu_k},
> $$
>
> where $\varepsilon$ is the Levi-Civita **tensor** (s2) and the upper indices were raised with $g^{\mu\nu}$.

> **Theorem.** Applying the star twice gives $\star\star\alpha=s\,(-1)^{k(n-k)}\alpha$ on a $k$-form, where $s=\mathrm{sgn}(g)$ ($s=-1$ for Lorentzian signature, $+1$ for Riemannian).

*Proof sketch with the load-bearing step.*
1. Composing two stars contracts two Levi-Civita tensors. The fundamental contraction identity is $\varepsilon^{\mu_1\dots\mu_k\,\lambda_1\dots\lambda_{n-k}}\varepsilon_{\nu_1\dots\nu_k\,\lambda_1\dots\lambda_{n-k}}=s\,(n-k)!\,k!\,\delta^{[\mu_1}_{\nu_1}\cdots\delta^{\mu_k]}_{\nu_k}$, the generalized antisymmetrized Kronecker delta. The factor $s$ enters because raising all $n$ indices of $\varepsilon$ pulls out $\det(g^{\mu\nu})=1/g$, and $\sqrt{-g}\cdot 1/\sqrt{-g}$ leaves the sign of $g$.
2. The sign $(-1)^{k(n-k)}$ counts the transpositions needed to move the $n-k$ contracted indices past the $k$ free ones to line up the deltas.
3. Combining the numerical factors with the $1/k!$ normalizations in the two stars yields $s(-1)^{k(n-k)}$. $\blacksquare$

#### The codifferential

> **Definition — codifferential.** The **codifferential** $\delta$ is the (formal) adjoint of the exterior derivative $d$. On a $k$-form in $n$ dimensions with Lorentzian sign $s$,
>
> $$
> \delta=s\,(-1)^{n(k+1)+1}\,\star\,d\,\star.
> $$
>
> It lowers form-degree by one: $\delta:\Omega^k\to\Omega^{k-1}$.

> **Theorem.** On a $1$-form $\omega$, the codifferential is minus the divergence: $\delta\omega=-\nabla^\mu\omega_\mu$ (Riemannian signature; an overall sign flips for Lorentzian).

*Proof.*
1. $\star\omega$ is an $(n-1)$-form; $d\star\omega$ is the top $n$-form $(\nabla^\mu\omega_\mu)\,\varepsilon$, because exterior differentiation of the dual produces exactly the covariant divergence (this is the form-language restatement of the divergence identity in s4).
2. Applying the final $\star$ to the top form returns a scalar, namely $\nabla^\mu\omega_\mu$ up to the signature factor in the definition.
3. Collecting the prefactor $s(-1)^{n(k+1)+1}$ with $k=1$ gives the stated sign. $\blacksquare$

> **Why we care.** The operator $\delta d+d\delta=\Box$ is the **Hodge Laplacian** on forms; $\delta$ is how "$\nabla_\mu F^{\mu\nu}$" is written in form language, and we will see it produce one of Maxwell's two equations in s7.

<a id="s6"></a>
### Integration on a manifold: the volume form and the divergence theorem

Integration of a scalar over a region requires an invariant measure; the density $\sqrt{-g}$ supplies it.

> **Definition — invariant volume form.** The **volume form** is the top-degree $n$-form
>
> $$
> \mathrm{vol}=\sqrt{-g}\;dx^1\wedge\cdots\wedge dx^n,
> $$
>
> and the integral of a scalar field $f$ over a region $\Omega$ is $\displaystyle\int_\Omega f\,\mathrm{vol}=\int_\Omega f\,\sqrt{-g}\,d^nx$.

> **Theorem (invariance).** $\displaystyle\int_\Omega f\,\sqrt{-g}\,d^nx$ is independent of coordinates.

*Proof.*
1. Under $x\to x'$ the coordinate measure changes by the absolute Jacobian: $d^nx=\bigl|\det\tfrac{\partial x}{\partial x'}\bigr|\,d^nx'=|\det J^{-1}|\,d^nx'$, by the change-of-variables theorem of multivariable calculus.
2. The density transforms (s2) as $\sqrt{-g}=\dfrac{1}{|\det J^{-1}|}\sqrt{-g'}$, since $\sqrt{-g'}=|\det J^{-1}|\sqrt{-g}$.
3. The scalar is unchanged, $f=f'$. Multiply the three factors: $f\sqrt{-g}\,d^nx=f'\cdot\dfrac{\sqrt{-g'}}{|\det J^{-1}|}\cdot|\det J^{-1}|\,d^nx'=f'\sqrt{-g'}\,d^nx'$. The two Jacobian factors cancel exactly. $\blacksquare$

> **Theorem (divergence theorem in tensor form).** For a vector field $V^\mu$ on a region $\Omega$ with boundary $\partial\Omega$,
>
> $$
> \int_\Omega \nabla_\mu V^\mu\,\sqrt{-g}\,d^nx=\oint_{\partial\Omega} V^\mu\,n_\mu\,\sqrt{|h|}\,d^{n-1}y,
> $$
>
> where $n_\mu$ is the outward unit normal covector and $h$ the determinant of the induced boundary metric.

*Proof.*
1. By the divergence identity (s4), $\sqrt{-g}\,\nabla_\mu V^\mu=\partial_\mu(\sqrt{-g}\,V^\mu)$. So the left integrand is an ordinary coordinate divergence of the vector density $\sqrt{-g}\,V^\mu$.
2. Apply the **ordinary** (flat) divergence theorem of multivariable calculus to the density $\sqrt{-g}\,V^\mu$: $\int_\Omega\partial_\mu(\sqrt{-g}\,V^\mu)\,d^nx=\oint_{\partial\Omega}\sqrt{-g}\,V^\mu\,d\Sigma_\mu$, where $d\Sigma_\mu$ is the coordinate surface element.
3. Identify the boundary measure $\sqrt{-g}\,d\Sigma_\mu=n_\mu\sqrt{|h|}\,d^{n-1}y$, the invariant area element with its normal, a standard reduction of the bulk density to the induced metric on $\partial\Omega$. Substituting gives the result. $\blacksquare$

> **Worked example — Gauss's law.** Taking $V^\mu$ the electric field vector in flat 3-space, this reduces to $\int(\nabla\cdot\mathbf E)\,dV=\oint\mathbf E\cdot d\mathbf A$ — the familiar Gauss theorem, now seen as the metric-independent statement that the divergence of a vector integrates to its boundary flux.

## Part D · Physics in tensor form

<a id="s7"></a>
### The electromagnetic field tensor and Maxwell's equations

Electromagnetism is the cleanest demonstration of the whole machinery: six field components assemble into one antisymmetric tensor, and four vector equations collapse to two tensor equations.

> **Definition — field strength tensor.** Given the electromagnetic four-potential $A_\mu=(-\phi,\mathbf A)$ (with $\phi$ the scalar and $\mathbf A$ the vector potential), define the antisymmetric **field strength**
>
> $$
> F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu.
> $$

> **Theorem.** $F_{\mu\nu}$ is a genuine antisymmetric $(0,2)$ tensor, and $\partial_\mu A_\nu-\partial_\nu A_\mu=\nabla_\mu A_\nu-\nabla_\nu A_\mu$ — the partials may be promoted to covariant derivatives for free.

*Proof.*
1. Antisymmetry $F_{\nu\mu}=-F_{\mu\nu}$ is immediate from the definition.
2. The Christoffel correction in $\nabla_\mu A_\nu=\partial_\mu A_\nu-\Gamma^\sigma{}_{\mu\nu}A_\sigma$ is **symmetric** in $\mu\nu$ because $\Gamma^\sigma{}_{\mu\nu}=\Gamma^\sigma{}_{\nu\mu}$ (the connection is torsion-free).
3. Antisymmetrizing kills it: $\nabla_\mu A_\nu-\nabla_\nu A_\mu=(\partial_\mu A_\nu-\partial_\nu A_\mu)-(\Gamma^\sigma{}_{\mu\nu}-\Gamma^\sigma{}_{\nu\mu})A_\sigma=\partial_\mu A_\nu-\partial_\nu A_\mu$. Since the right side is now manifestly a tensor (an antisymmetrized covariant derivative), so is $F$. $\blacksquare$

#### Identifying the components

> With $\eta=\mathrm{diag}(-1,1,1,1)$ and $i,j\in\{1,2,3\}$: $F_{0i}=\partial_0 A_i-\partial_i A_0=-\partial_t A_i-\partial_i\phi$... read against $\mathbf E=-\nabla\phi-\partial_t\mathbf A$ and $\mathbf B=\nabla\times\mathbf A$, this gives $F_{0i}=E_i$ and $F_{ij}=\epsilon_{ijk}B^k$. So $F_{\mu\nu}$ packages the electric field in its time-space components and the magnetic field in its space-space components.

#### The two covariant Maxwell equations

> **Theorem (homogeneous equations — Bianchi/Faraday).** $\partial_{[\lambda}F_{\mu\nu]}=0$, equivalently $\partial_\lambda F_{\mu\nu}+\partial_\mu F_{\nu\lambda}+\partial_\nu F_{\lambda\mu}=0$.

*Proof.*
1. Substitute $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$ into the cyclic sum:
$$
(\partial_\lambda\partial_\mu A_\nu-\partial_\lambda\partial_\nu A_\mu)+(\partial_\mu\partial_\nu A_\lambda-\partial_\mu\partial_\lambda A_\nu)+(\partial_\nu\partial_\lambda A_\mu-\partial_\nu\partial_\mu A_\lambda).
$$
2. Partial derivatives commute, $\partial_\lambda\partial_\mu=\partial_\mu\partial_\lambda$ (equality of mixed partials, valid for smooth fields). The six terms cancel in pairs: $\partial_\lambda\partial_\mu A_\nu$ cancels $-\partial_\mu\partial_\lambda A_\nu$, and so on.
3. The covariant version is identical because the symmetric Christoffel terms cancel in the antisymmetrization, exactly as in the previous proof. This equation encodes $\nabla\cdot\mathbf B=0$ and Faraday's law $\nabla\times\mathbf E=-\partial_t\mathbf B$. $\blacksquare$

> **Theorem (inhomogeneous equations — Gauss/Ampère).** With four-current $J^\mu=(\rho,\mathbf J)$ and Gaussian-style units,
>
> $$
> \nabla_\mu F^{\mu\nu}=\mu_0 J^\nu,\qquad\text{equivalently}\qquad \frac{1}{\sqrt{-g}}\partial_\mu(\sqrt{-g}\,F^{\mu\nu})=\mu_0 J^\nu.
> $$

*Proof of the simplified form.*
1. $F^{\mu\nu}$ is antisymmetric. Its covariant divergence is $\nabla_\mu F^{\mu\nu}=\partial_\mu F^{\mu\nu}+\Gamma^\mu{}_{\mu\lambda}F^{\lambda\nu}+\Gamma^\nu{}_{\mu\lambda}F^{\mu\lambda}$.
2. The last term vanishes: $\Gamma^\nu{}_{\mu\lambda}$ is symmetric in $\mu\lambda$, $F^{\mu\lambda}$ antisymmetric, and symmetric-times-antisymmetric contracts to zero (s1).
3. The middle term uses the Lemma $\Gamma^\mu{}_{\mu\lambda}=\frac{1}{\sqrt{-g}}\partial_\lambda\sqrt{-g}$, so $\nabla_\mu F^{\mu\nu}=\partial_\mu F^{\mu\nu}+\frac{1}{\sqrt{-g}}(\partial_\lambda\sqrt{-g})F^{\lambda\nu}=\frac{1}{\sqrt{-g}}\partial_\mu(\sqrt{-g}\,F^{\mu\nu})$ by the product rule (same algebra as the divergence theorem in s4, with the antisymmetric extra term already dropped).
4. Setting this equal to $\mu_0 J^\nu$ reproduces Gauss's law ($\nu=0$) and Ampère–Maxwell ($\nu=i$). $\blacksquare$

> **Corollary — charge conservation for free.** Take $\nabla_\nu$ of the inhomogeneous equation: $\mu_0\nabla_\nu J^\nu=\nabla_\nu\nabla_\mu F^{\mu\nu}$. The right side is a symmetric derivative operator $\nabla_\nu\nabla_\mu$ contracted with the antisymmetric $F^{\mu\nu}$, hence zero. (Concretely, $\nabla_\nu\nabla_\mu F^{\mu\nu}=\tfrac12[\nabla_\nu,\nabla_\mu]F^{\mu\nu}$ produces Ricci-type curvature terms that are symmetric in $(\mu,\nu)$, so they too vanish when contracted with the antisymmetric $F^{\mu\nu}$.) So $\nabla_\mu J^\mu=0$: charge is conserved automatically, as a structural consequence of $F$'s antisymmetry.

<a id="s8"></a>
### The stress–energy tensor and $\nabla_\mu T^{\mu\nu}=0$

The stress–energy tensor is the source of gravity and the bookkeeper of energy and momentum flow.

> **Definition.** The symmetric $(2,0)$ **stress–energy tensor** $T^{\mu\nu}$ has the interpretation: $T^{00}$ is energy density, $T^{0i}$ is the flux of energy / density of $i$-momentum, and $T^{ij}$ is the flux of $i$-momentum in the $j$-direction (stress). For a **perfect fluid** with rest energy density $\rho$, pressure $p$, and four-velocity $u^\mu$ (normalized $u^\mu u_\mu=-1$),
>
> $$
> T^{\mu\nu}=(\rho+p)\,u^\mu u^\nu+p\,g^{\mu\nu}.
> $$

> **Theorem (local conservation).** In the absence of external forces, $\nabla_\mu T^{\mu\nu}=0$. These are $n$ equations expressing conservation of energy ($\nu=0$) and momentum ($\nu=i$).

*Derivation for the perfect fluid, showing it yields the relativistic Euler equations.*
1. Compute $\nabla_\mu T^{\mu\nu}=\nabla_\mu[(\rho+p)u^\mu u^\nu]+\nabla_\mu(p\,g^{\mu\nu})$. Use $\nabla_\mu g^{\mu\nu}=0$ (metric compatibility), so the last term is $g^{\mu\nu}\nabla_\mu p=\nabla^\nu p$.
2. Leibniz on the first term: $u^\nu\nabla_\mu[(\rho+p)u^\mu]+(\rho+p)u^\mu\nabla_\mu u^\nu$.
3. Project along the flow by contracting with $u_\nu$ (using $u_\nu u^\nu=-1$ and $u_\nu\nabla_\mu u^\nu=0$, the latter from differentiating the normalization $u^\nu u_\nu=-1$): this gives the **energy/continuity equation** $\nabla_\mu(\rho u^\mu)+p\,\nabla_\mu u^\mu=0$.
4. Project orthogonal to the flow with the projector $h^\alpha{}_\nu=\delta^\alpha_\nu+u^\alpha u_\nu$: this gives the **Euler equation** $(\rho+p)u^\mu\nabla_\mu u^\alpha=-h^{\alpha\mu}\nabla_\mu p$ — pressure gradients (projected perpendicular to the motion) accelerate the fluid. $\blacksquare$

> **Why conservation is automatic in GR.** The Einstein equations read $G^{\mu\nu}=8\pi G\,T^{\mu\nu}$, where $G^{\mu\nu}=R^{\mu\nu}-\tfrac12 R g^{\mu\nu}$ is the Einstein tensor. The **contracted Bianchi identity** $\nabla_\mu G^{\mu\nu}=0$ holds as a geometric identity (proved in the companion guide), so the field equations *force* $\nabla_\mu T^{\mu\nu}=0$. Energy–momentum conservation is not an extra assumption; it is built into the geometry.

> **Worked example — dust.** For pressureless matter ("dust") $p=0$, conservation gives $\nabla_\mu(\rho u^\mu)=0$ (continuity) and $u^\mu\nabla_\mu u^\nu=0$ (the geodesic equation). Dust particles free-fall along geodesics — gravity moves matter by geometry alone.

<a id="s9"></a>
### Symmetries: the Lie derivative, Killing vectors, and conserved quantities

Continuous symmetries of the metric produce conserved quantities along geodesics — the geometric face of Noether's theorem.

> **Definition — Lie derivative in components.** The **Lie derivative** of a tensor along a vector field $\xi$ measures its change as it is dragged along the flow of $\xi$. On a vector and a $(0,2)$ tensor,
>
> $$
> (\mathcal L_\xi V)^\mu=\xi^\nu\partial_\nu V^\mu-V^\nu\partial_\nu\xi^\mu,\qquad
> (\mathcal L_\xi T)_{\mu\nu}=\xi^\lambda\partial_\lambda T_{\mu\nu}+T_{\lambda\nu}\partial_\mu\xi^\lambda+T_{\mu\lambda}\partial_\nu\xi^\lambda.
> $$

> **Theorem.** The Lie derivative may be written with covariant derivatives in place of partials: $(\mathcal L_\xi T)_{\mu\nu}=\xi^\lambda\nabla_\lambda T_{\mu\nu}+T_{\lambda\nu}\nabla_\mu\xi^\lambda+T_{\mu\lambda}\nabla_\nu\xi^\lambda$.

*Proof.* Replace every $\partial$ by $\nabla$; this introduces Christoffel terms. Collect them: the $\Gamma$ from the transport term $\xi^\lambda\nabla_\lambda T_{\mu\nu}$ pairs against those from $T_{\lambda\nu}\nabla_\mu\xi^\lambda$ and $T_{\mu\lambda}\nabla_\nu\xi^\lambda$, and because the connection is torsion-free ($\Gamma^\lambda{}_{\mu\nu}=\Gamma^\lambda{}_{\nu\mu}$) each such pair carries equal and opposite coefficients, so all Christoffel terms cancel. The Lie derivative is therefore connection-independent. $\blacksquare$

> **Definition — Killing vector.** A vector field $\xi$ is a **Killing vector** if dragging the metric along it changes nothing: $\mathcal L_\xi g_{\mu\nu}=0$. Using the covariant form with $\nabla_\lambda g_{\mu\nu}=0$, this is **Killing's equation**:
>
> $$
> \nabla_\mu\xi_\nu+\nabla_\nu\xi_\mu=0,\qquad\text{i.e.}\qquad \nabla_{(\mu}\xi_{\nu)}=0.
> $$

> **Theorem (conserved momentum).** If $\xi$ is Killing and $x^\mu(\lambda)$ is a geodesic with tangent $u^\mu$, then $\xi_\mu u^\mu$ is constant along the geodesic.

*Proof.*
1. $\dfrac{d}{d\lambda}(\xi_\mu u^\mu)=u^\nu\nabla_\nu(\xi_\mu u^\mu)$, since this scalar's rate of change along the curve is the directional covariant derivative.
2. Leibniz: $=u^\nu u^\mu\nabla_\nu\xi_\mu+\xi_\mu(u^\nu\nabla_\nu u^\mu)$.
3. The second term is zero by the **geodesic equation** $u^\nu\nabla_\nu u^\mu=0$.
4. The first term contracts the **symmetric** $u^\nu u^\mu$ with $\nabla_\nu\xi_\mu$; only the symmetric part $\nabla_{(\nu}\xi_{\mu)}$ survives, and that is zero by **Killing's equation**. $\blacksquare$

> **Definition — Killing tensor.** A symmetric tensor $K_{\mu\nu}$ is a **Killing tensor** if $\nabla_{(\lambda}K_{\mu\nu)}=0$. Then $K_{\mu\nu}u^\mu u^\nu$ is conserved along geodesics, by the same argument with $u^\mu u^\nu$ symmetric and the symmetrized derivative vanishing.

> **Worked example — Kerr's hidden constant.** In the rotating-black-hole (Kerr) spacetime, the obvious Killing vectors $\partial_t$ and $\partial_\phi$ give conserved energy and angular momentum. But Kerr also admits a non-trivial **Killing tensor**, whose conserved quantity is the **Carter constant** — the extra integral of motion that makes geodesics in Kerr completely solvable. Killing tensors generate conservation laws with no associated spacetime symmetry of the metric, a phenomenon invisible to elementary Noether reasoning.

<a id="s10"></a>
### Spinors and the tetrad formalism — Clifford algebra and the Dirac operator

Spinors are the objects electrons are made of, and they cannot be written with world indices. Here is the concrete machinery, built on the tetrads of s3.

> **Definition — Clifford / gamma algebra.** The flat-space **gamma matrices** $\gamma^a$ ($a$ a frame index) satisfy the **Clifford relation**
>
> $$
> \{\gamma^a,\gamma^b\}=\gamma^a\gamma^b+\gamma^b\gamma^a=2\,\eta^{ab}\,\mathbb 1,
> $$
>
> with $\eta^{ab}$ the constant frame metric. They are constant $4\times4$ matrices in 4D; the anticommutator, not the product, encodes the geometry.

The square-root structure is the point: $(\gamma^a\partial_a)^2$ recovers the Laplacian/d'Alembertian. To verify, $(\gamma^a\partial_a)(\gamma^b\partial_b)=\tfrac12\{\gamma^a,\gamma^b\}\partial_a\partial_b=\eta^{ab}\partial_a\partial_b=\Box$, using the Clifford relation and the symmetry of $\partial_a\partial_b$ to replace $\gamma^a\gamma^b$ by its symmetric part. The Dirac operator is thus a *square root* of the wave operator.

#### Curving the gamma matrices

> **Definition — curved gammas.** Use the inverse tetrad to convert the frame index to a world index: $\gamma^\mu(x)=e_a{}^\mu(x)\,\gamma^a$. Then $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$.

*Proof.* $\{\gamma^\mu,\gamma^\nu\}=e_a{}^\mu e_b{}^\nu\{\gamma^a,\gamma^b\}=e_a{}^\mu e_b{}^\nu\,2\eta^{ab}=2g^{\mu\nu}$, where the last step is the inverse-vielbein form of the metric relation $g^{\mu\nu}=e_a{}^\mu e_b{}^\nu\eta^{ab}$ (s3). $\blacksquare$

#### The spin connection and the Dirac operator

A spinor $\psi$ carries a hidden frame structure, so differentiating it requires a connection that acts on frame indices — the **spin connection** $\omega_\mu{}^{ab}$, the Lorentz-frame analogue of the Christoffel symbol.

> **Definition — spinor covariant derivative.**
>
> $$
> D_\mu\psi=\partial_\mu\psi+\tfrac14\,\omega_\mu{}^{ab}\,\gamma_a\gamma_b\,\psi,
> $$
>
> where the spin connection is fixed by requiring the tetrad to be covariantly constant ("tetrad postulate"), $\nabla_\mu e^a{}_\nu+\omega_\mu{}^a{}_b e^b{}_\nu=0$, which solves to
>
> $$
> \omega_\mu{}^{ab}=e^a{}_\nu\bigl(\partial_\mu e^{b\nu}+\Gamma^\nu{}_{\mu\lambda}e^{b\lambda}\bigr).
> $$

> **Definition — Dirac operator on curved space.** The curved-space **Dirac operator** is
>
> $$
> {D\!\!\!/}=\gamma^\mu D_\mu=e_a{}^\mu\gamma^a\bigl(\partial_\mu+\tfrac14\omega_\mu{}^{bc}\gamma_b\gamma_c\bigr),
> $$
>
> and the **Dirac equation** for a particle of mass $m$ is $(i{D\!\!\!/}-m)\psi=0$.

> **Why every piece is necessary.** The $\partial_\mu$ alone is not Lorentz-covariant on spinors; the $\tfrac14\omega_\mu{}^{ab}\gamma_a\gamma_b$ term rotates the spinor frame to compensate, exactly as $\Gamma$ compensates for moving tensor frames. The tetrad $e_a{}^\mu$ is the only object that can attach the frame-indexed gammas to world-indexed derivatives. Without tetrads there is no Dirac equation on curved space — which is why s3's frame formalism, optional for tensors, is mandatory for fermions.

> **Worked example — flat-space sanity check.** In Minkowski coordinates the tetrad is trivial, $e_a{}^\mu=\delta_a^\mu$, so $\omega_\mu{}^{ab}=0$ and ${D\!\!\!/}=\gamma^\mu\partial_\mu$. The Dirac equation reduces to the familiar $(i\gamma^\mu\partial_\mu-m)\psi=0$, and squaring it gives $(\Box+m^2)\psi=0$, the Klein–Gordon equation — confirming that the Dirac operator is the spinorial square root of the wave operator, now on arbitrary curved backgrounds.

---

*This guide treated tensor calculus as a craft: we learned which arrays are tensors (the quotient theorem), which are densities and how $\sqrt{-g}$ rehabilitates them, how to raise, lower, and differentiate covariantly, and how the single identity $\nabla_\mu(\sqrt{-g}\,V^\mu)=\partial_\mu(\sqrt{-g}\,V^\mu)$ tames divergences, Laplacians, and Maxwell's equations alike. From there the physics fell out almost mechanically — the electromagnetic field tensor, the conservation of energy–momentum, Killing symmetries and their conserved charges, and the tetrad-borne Dirac operator. Keep this as a desk reference: when an index computation stalls, the fix is almost always to ask which contract — tensor, density, or frame — is being honoured, and to insert the $\sqrt{-g}$ or vielbein that restores it.*
