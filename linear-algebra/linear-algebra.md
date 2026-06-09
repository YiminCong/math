**English** · [中文](linear-algebra.zh.md)

# Linear Algebra, *the language of quantum mechanics.*

*A full first course in linear algebra, built from the ground up and aimed at the place it is spoken most fluently — quantum mechanics, where a physical state is a vector and every measurable quantity is an operator. Every definition is given in plain words, every symbol is named the first time it appears, and every theorem is proved with no gaps.*

[← Back to all guides](../README.md)

> **How to read this guide.** We assume only ordinary algebra (manipulating sums and products, solving simple equations) and a little single-variable calculus (derivatives and integrals appear only in examples). Everything specific to linear algebra — *vector space*, *basis*, *linear map*, *eigenvalue*, *inner product*, *adjoint*, *spectral theorem* — is defined the first time it is used, with a worked numerical example. Nothing is "left to the reader." Where the physics is illuminating we point it out, but this is a **math** guide: claims are proved.

---

## Part A — The skeleton: vector spaces and linear maps

<a id="s0"></a>
### Why linear algebra: states as vectors, observables as operators

Linear algebra is the study of two things and the relationship between them: **vectors**, which we will think of as "things you can add together and scale," and **linear maps**, which are the transformations that respect adding and scaling. That sounds abstract, so here is the physical hook that organizes this whole guide.

In quantum mechanics the complete state of a physical system — say a single electron's spin — is encoded not by a list of numbers in the everyday sense but by a **vector** in a complex vector space. Two states can be *superposed* (added), and a state can be *rescaled* by a complex number without changing the physics it describes. Adding and scaling: those are exactly the operations a vector space provides. A **measurable quantity** ("observable") such as energy, position, or spin-along-an-axis is represented by a **linear operator** — a linear map from the space of states to itself. The possible measured values are the operator's **eigenvalues**, and the special states that return a definite value are its **eigenvectors**. The requirement that measured values be real numbers forces these operators to be *Hermitian* (self-adjoint), and the guarantee that you can always find a full set of definite-value states is the *spectral theorem*. Composite systems (two particles) are described by *tensor products*. Every italicized word in that paragraph is a precise linear-algebra concept, and we will build each one.

So the plan is honest: develop the mathematics rigorously, and at each milestone note the quantum-mechanical reading. Let us begin with the object everything rests on.

> **Why "linear."** A rule $f$ is **linear** when it commutes with the two basic operations: $f(\text{sum}) = \text{sum of } f$ and $f(\text{scaled}) = \text{scaled } f$. Linearity is the mathematical fingerprint of *superposition*, the principle that quantum states combine additively. Nature is full of linear structure precisely because superposition is everywhere; that is why this one subject reappears across physics, statistics, and computation.

<a id="s1"></a>
### Vector spaces: the axioms over $\mathbb{R}$ and $\mathbb{C}$

**What and why.** We want to capture, abstractly, exactly the properties of "arrows you can add and stretch" so that the *same* theorems apply to arrows, lists of numbers, polynomials, and quantum states all at once. A **field** is the system of numbers we are allowed to scale by. For us a field $\mathbb{F}$ will be either the **real numbers** $\mathbb{R}$ (ordinary decimals) or the **complex numbers** $\mathbb{C}$ (numbers $a+bi$ with $i^2=-1$, where $a,b\in\mathbb{R}$). Both support addition, subtraction, multiplication, and division by nonzero elements, obeying the usual algebra rules; that is all we use.

> **Definition — vector space.**
> A **vector space over a field $\mathbb{F}$** is a set $V$ (whose elements are called **vectors**) equipped with two operations:
> - **addition** $+ : V\times V\to V$, written $u+v$, and
> - **scalar multiplication** $\cdot : \mathbb{F}\times V\to V$, written $\lambda v$ (here $\lambda\in\mathbb{F}$ is a **scalar**),
>
> such that for all $u,v,w\in V$ and all $\lambda,\mu\in\mathbb{F}$ the following **axioms** hold:
> 1. **(Additive associativity)** $(u+v)+w = u+(v+w)$.
> 2. **(Additive commutativity)** $u+v = v+u$.
> 3. **(Zero vector)** there is an element $0\in V$ with $v+0=v$ for all $v$.
> 4. **(Additive inverse)** for each $v$ there is $-v\in V$ with $v+(-v)=0$.
> 5. **(Scalar associativity)** $\lambda(\mu v)=(\lambda\mu)v$.
> 6. **(Scalar identity)** $1\,v=v$, where $1$ is the multiplicative identity of $\mathbb{F}$.
> 7. **(Distributivity over vector sums)** $\lambda(u+v)=\lambda u+\lambda v$.
> 8. **(Distributivity over scalar sums)** $(\lambda+\mu)v=\lambda v+\mu v$.
>
> When $\mathbb{F}=\mathbb{R}$ we call $V$ a **real** vector space; when $\mathbb{F}=\mathbb{C}$, a **complex** vector space.

These eight rules look like a lot, but they are just the algebra you already do with arrows, written so it applies to anything. From them we can already prove small facts that the axioms do not *state* but do *force*.

> **Lemma — basic consequences.** In any vector space: (a) the zero vector is unique; (b) $0\cdot v = 0$ for every $v$ (scalar zero times any vector is the zero vector); (c) $(-1)v=-v$.

**Proof.**
1. *(Uniqueness of $0$.)* Suppose $0$ and $0'$ both satisfy axiom 3. Then $0 = 0+0'$ (since $0'$ is a zero, axiom 3) $= 0'+0$ (commutativity, axiom 2) $= 0'$ (since $0$ is a zero, axiom 3). Hence $0=0'$. *(uses axioms 2 and 3 only)*
2. *(Claim $0\cdot v=0$.)* Write the scalar $0\in\mathbb{F}$. Then $0\cdot v = (0+0)v$ (because $0+0=0$ in the field) $= 0\cdot v + 0\cdot v$ (distributivity over scalar sums, axiom 8). *(rewrote $0$ as $0+0$ then expanded)*
3. Add $-(0\cdot v)$ (which exists by axiom 4) to both sides: $0\cdot v + (-(0\cdot v)) = (0\cdot v + 0\cdot v) + (-(0\cdot v))$. The left side is $0$ by axiom 4. The right side regroups (axiom 1) to $0\cdot v + (0\cdot v + (-(0\cdot v))) = 0\cdot v + 0 = 0\cdot v$ (axioms 4 then 3). So $0 = 0\cdot v$, proving (b). *(cancellation using the additive inverse)*
4. *(Claim $(-1)v=-v$.)* Compute $v + (-1)v = 1\,v + (-1)v$ (scalar identity, axiom 6) $= (1+(-1))v$ (distributivity over scalar sums, axiom 8) $= 0\cdot v$ (since $1+(-1)=0$ in the field) $= 0$ (by part (b)). Thus $(-1)v$ added to $v$ gives $0$, so by uniqueness of the additive inverse $(-1)v=-v$, proving (c). $\blacksquare$

**Worked examples.** Each of the following is a vector space; verifying the axioms is routine because each operation is defined coordinatewise or pointwise.

- **$\mathbb{R}^n$**, the set of ordered lists $(x_1,\dots,x_n)$ of real numbers, with $(x_1,\dots,x_n)+(y_1,\dots,y_n)=(x_1+y_1,\dots,x_n+y_n)$ and $\lambda(x_1,\dots,x_n)=(\lambda x_1,\dots,\lambda x_n)$. The zero vector is $(0,\dots,0)$. This is the model of ordinary geometric space; $\mathbb{R}^2$ is the plane, $\mathbb{R}^3$ is physical space.
- **$\mathbb{C}^n$**, the same but with complex entries and complex scalars. This is the arena of quantum mechanics for finite systems: the spin state of an electron lives in $\mathbb{C}^2$.
- **$\mathbb{F}[x]$ (polynomials)**, all polynomials $a_0+a_1x+\dots+a_kx^k$ with coefficients in $\mathbb{F}$, added and scaled term by term. Its subspace $P_n$ of polynomials of degree $\le n$ is also a vector space.
- **Function spaces.** The set of all functions $f:S\to\mathbb{F}$ from any fixed set $S$, with $(f+g)(s)=f(s)+g(s)$ and $(\lambda f)(s)=\lambda f(s)$. Continuous functions $C[a,b]$ and square-integrable wavefunctions $L^2$ are examples — these are the *infinite-dimensional* spaces of quantum field theory and wave mechanics.

> **Definition — subspace.** A subset $W\subseteq V$ is a **subspace** if it is itself a vector space under the inherited operations. Equivalently (and this is what we check in practice) $W$ is a subspace iff it is nonempty and **closed** under the two operations: $u,v\in W \Rightarrow u+v\in W$, and $\lambda\in\mathbb{F}, v\in W \Rightarrow \lambda v\in W$. (Closure under both forces $0=0\cdot v\in W$ and $-v=(-1)v\in W$, so the other axioms are inherited automatically.)

**Pitfall.** A common confusion is to think any subset that "contains arrows" is a subspace. It must contain $0$ and be closed: the line $y=x+1$ in $\mathbb{R}^2$ is *not* a subspace because it misses the origin, and adding two of its points lands off the line. To see the failure concretely, $(0,1)$ and $(1,2)$ both lie on $y=x+1$, but their sum $(1,3)$ has $3\ne 1+1$, so it is off the line. The line $y=x$ (through the origin) *is* a subspace.

> **Definition — real vs. complex matters.** The same set of vectors can be a real space or a complex space depending on the allowed scalars, and the answer is not cosmetic. As a *complex* space $\mathbb{C}$ is one-dimensional (basis $\{1\}$, since any $z\in\mathbb{C}$ is $z\cdot 1$). As a *real* space $\mathbb{C}$ is two-dimensional (basis $\{1,i\}$, since $z=a\cdot 1+b\cdot i$ needs two real coefficients). Quantum mechanics insists on complex scalars precisely because phases $e^{i\theta}$ — complex unit multiples — carry physical meaning through interference.

**A second worked example — the space of $2\times2$ real matrices.** Let $V=M_2(\mathbb{R})$, all $2\times2$ matrices with real entries, added and scaled entrywise. This is a vector space; a basis is the four matrices $\begin{psmallmatrix}1&0\\0&0\end{psmallmatrix},\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix},\begin{psmallmatrix}0&0\\1&0\end{psmallmatrix},\begin{psmallmatrix}0&0\\0&1\end{psmallmatrix}$, so $\dim V=4$. The symmetric matrices ($A=A^{\mathsf T}$) form a $3$-dimensional subspace; the trace-zero matrices form another $3$-dimensional subspace. Recognizing familiar objects (matrices, polynomials, functions) as vectors is the whole power of the abstract definition: one theorem proved once applies everywhere.

<a id="s2"></a>
### Linear independence, span, basis, dimension

**What and why.** We want a small list of vectors from which *every* vector can be built by adding and scaling, with no redundancy. That minimal-and-complete list is a **basis**, and its length will turn out to be an intrinsic number, the **dimension**. This is the single most important structural fact in the subject, so we build it carefully.

> **Definition — linear combination and span.** A **linear combination** of vectors $v_1,\dots,v_k$ is any vector $\lambda_1 v_1+\dots+\lambda_k v_k$ with scalars $\lambda_i\in\mathbb{F}$. The **span** $\operatorname{span}(v_1,\dots,v_k)$ is the set of *all* such combinations. The span is always a subspace (it is closed under addition and scaling, since a sum/scaling of combinations is again a combination). We say the $v_i$ **span** $V$ if their span is all of $V$.

> **Definition — linear independence.** Vectors $v_1,\dots,v_k$ are **linearly independent** if the only way to combine them into the zero vector is the trivial way: $\lambda_1 v_1+\dots+\lambda_k v_k=0$ forces $\lambda_1=\dots=\lambda_k=0$. Otherwise they are **linearly dependent**, meaning some nontrivial combination vanishes — equivalently, one of them is a combination of the others (a redundancy).

> **Definition — basis and dimension.** A **basis** of $V$ is a list of vectors that is both linearly independent and spans $V$. The **dimension** $\dim V$ is the number of vectors in a basis. (We must prove this number is well defined — that any two bases have the same length — which is the theorem below.)

**Worked example.** In $\mathbb{R}^3$ the **standard basis** is $e_1=(1,0,0),\ e_2=(0,1,0),\ e_3=(0,0,1)$. It spans because $(x,y,z)=x e_1+y e_2+z e_3$, and it is independent because $x e_1+y e_2+z e_3=(x,y,z)=(0,0,0)$ forces $x=y=z=0$. So $\dim\mathbb{R}^3=3$. The vectors $(1,1,0)$ and $(2,2,0)$ are dependent: $2(1,1,0)-1(2,2,0)=0$ nontrivially.

The crux is that "dimension" does not depend on which basis you pick. We prove it via a workhorse lemma.

> **Theorem (Steinitz exchange / Replacement Lemma).** If $v_1,\dots,v_m$ span $V$ and $w_1,\dots,w_n$ are linearly independent in $V$, then $n\le m$.

**Proof (by exchanging $w$'s into the spanning list, one at a time).**
1. Since the $v_i$ span $V$, we can write $w_1$ as a combination $w_1=\sum_{i=1}^m a_i v_i$. *(definition of span)*
2. Not all $a_i$ are zero, because if they were, $w_1=0$ would be a nontrivial dependency among the $w$'s (the coefficient $1$ on $w_1$), contradicting independence. Reorder so $a_1\ne 0$. *(independence of the $w$'s rules out $w_1=0$)*
3. Solve for $v_1$: $v_1=\tfrac{1}{a_1}\big(w_1-\sum_{i\ge2}a_i v_i\big)$, allowed because $a_1\ne0$ so we may divide in the field. Hence $v_1\in\operatorname{span}(w_1,v_2,\dots,v_m)$, and therefore the list $w_1,v_2,\dots,v_m$ still spans $V$ (anything expressible using $v_1$ is now expressible using $w_1$ instead). *(field division; substitution into spans)*
4. Repeat: assume after $k$ steps the list $w_1,\dots,w_k,v_{k+1},\dots,v_m$ spans $V$ (with $k\le n$ and $k\le m$ so far). Write $w_{k+1}=\sum_{j\le k}b_j w_j+\sum_{i>k}c_i v_i$ using this spanning list. *(definition of span)*
5. Some $c_i\ne0$: otherwise $w_{k+1}=\sum_{j\le k}b_j w_j$, a nontrivial dependency among $w_1,\dots,w_{k+1}$, contradicting independence of the $w$'s. In particular this forces that there *is* a $v$ still left to replace, i.e. $k<m$. Reorder the remaining $v$'s so $c_{k+1}\ne0$, and as in step 3 swap $v_{k+1}$ out for $w_{k+1}$, keeping a spanning list. *(independence forbids $c_i$ all zero, which also forces $m>k$)*
6. We can keep exchanging as long as there are $w$'s left. Step 5 shows that each new $w$ requires an unused $v$ to replace it, so the number of $w$'s cannot exceed the number of $v$'s: $n\le m$. $\blacksquare$

> **Corollary — dimension is well defined.** Any two finite bases of $V$ have the same number of elements.

**Proof.** Let $B=(v_1,\dots,v_m)$ and $B'=(w_1,\dots,w_n)$ both be bases.
1. $B$ spans and $B'$ is independent, so by the Replacement Lemma $n\le m$. *(apply the theorem one way)*
2. $B'$ spans and $B$ is independent, so by the Replacement Lemma $m\le n$. *(apply the theorem the other way)*
3. Therefore $m=n$. $\blacksquare$

> **Physics note.** A quantum bit ("qubit") is a state in $\mathbb{C}^2$, with basis $\{|0\rangle,|1\rangle\}$ — dimension $2$. The dimension is the number of *independent classical alternatives* superposed. Two qubits live in a $4$-dimensional space (we will see why under tensor products, §s13).

**Second worked example — a polynomial basis.** In $P_2$, polynomials of degree $\le2$, the natural basis is $\{1,x,x^2\}$, so $\dim P_2=3$. But $\{1,\,x-1,\,(x-1)^2\}$ is also a basis: it spans because any quadratic can be rewritten as a Taylor expansion about $x=1$, and it is independent because $a\cdot1+b(x-1)+c(x-1)^2=0$ as a polynomial forces $c=0$ (top degree), then $b=0$, then $a=0$. Changing the basis here is exactly the algebra of expanding about a different center — the same data, relabeled.

**Pitfall — "spanning" and "independent" pull in opposite directions.** Adding vectors makes spanning easier but independence harder; removing them does the reverse. A basis is the exact balance point: just enough vectors to span, few enough to stay independent. The Replacement Lemma is the precise statement that you cannot have an independent set larger than a spanning set, which is why this balance point has a well-defined size.

> **Lemma — extension and reduction to a basis.** In a finite-dimensional space, every linearly independent set can be *extended* to a basis, and every spanning set can be *reduced* to a basis.
**Proof.** *(Extension.)* If the independent set does not yet span, pick a vector outside its span; adjoining it keeps independence (a new dependency would express the new vector inside the old span, a contradiction). Repeat; this stops because each step raises the size and independent sets are capped at $\dim V$ by the Replacement Lemma. *(Reduction.)* If a spanning set is dependent, some vector is a combination of the others; delete it — the span is unchanged. Repeat until independent. $\blacksquare$

<a id="s3"></a>
### Linear maps; kernel and image; the rank–nullity theorem

**What and why.** A **linear map** is a function between vector spaces that respects addition and scaling — the transformations under which superposition is preserved. Two subspaces measure its behavior: the **kernel** (what it crushes to zero) and the **image** (what it can produce). The rank–nullity theorem says these two sizes add up to the dimension of the source — a conservation law for dimension.

> **Definition — linear map.** A function $T:V\to W$ between vector spaces over the same field $\mathbb{F}$ is a **linear map** (or **linear transformation**) if for all $u,v\in V$, $\lambda\in\mathbb{F}$:
>
> $$
> T(u+v)=T(u)+T(v) \qquad\text{and}\qquad T(\lambda v)=\lambda\,T(v).
> $$
>
> A linear map from $V$ to itself is called a **linear operator**. (Note $T(0)=T(0\cdot 0)=0\cdot T(0)=0$: linear maps fix the zero vector.)

> **Definition — kernel and image.** The **kernel** is $\ker T=\{v\in V : T(v)=0\}$ (everything sent to zero). The **image** is $\operatorname{im}T=\{T(v):v\in V\}$ (everything actually hit). Both are subspaces: the kernel because $T(u)=T(v)=0\Rightarrow T(u+\lambda v)=0$; the image because $T(u)+\lambda T(v)=T(u+\lambda v)$. The dimension of the kernel is the **nullity**; the dimension of the image is the **rank**.

> **Lemma — injective iff trivial kernel.** A linear map $T$ is **injective** (one-to-one) if and only if $\ker T=\{0\}$.
**Proof.** If $T$ is injective and $T(v)=0=T(0)$ then $v=0$, so the kernel is trivial. Conversely if $\ker T=\{0\}$ and $T(u)=T(v)$, then $T(u-v)=T(u)-T(v)=0$ (linearity), so $u-v\in\ker T=\{0\}$, giving $u=v$. $\blacksquare$

> **Theorem — Rank–Nullity.** If $V$ is finite-dimensional and $T:V\to W$ is linear, then
>
> $$
> \dim(\ker T)+\dim(\operatorname{im}T)=\dim V.
> $$

**Proof (extend a kernel basis and track where it goes).**
1. Let $\dim V=n$ and let $u_1,\dots,u_k$ be a basis of $\ker T$, so $\dim(\ker T)=k$. *(every finite-dimensional space has a basis)*
2. A linearly independent set can be extended to a basis of the whole space (add vectors not in the current span until you span $V$; this terminates because dimension is finite). Extend to a basis $u_1,\dots,u_k,w_1,\dots,w_{n-k}$ of $V$. *(basis extension)*
3. **Claim:** $T(w_1),\dots,T(w_{n-k})$ is a basis of $\operatorname{im}T$. If we prove this, then $\dim(\operatorname{im}T)=n-k$, so $k+(n-k)=n=\dim V$, as desired.
4. *(They span the image.)* Any element of $\operatorname{im}T$ is $T(v)$ for some $v\in V$. Write $v=\sum a_i u_i+\sum b_j w_j$ in the basis. Apply $T$: $T(v)=\sum a_i T(u_i)+\sum b_j T(w_j)=\sum b_j T(w_j)$, since each $u_i\in\ker T$ makes $T(u_i)=0$. So every image element is a combination of the $T(w_j)$. *(linearity; $u_i$ in kernel)*
5. *(They are independent.)* Suppose $\sum b_j T(w_j)=0$. By linearity $T\!\left(\sum b_j w_j\right)=0$, so $\sum b_j w_j\in\ker T$, hence equals some combination $\sum a_i u_i$ of the kernel basis. Then $\sum b_j w_j-\sum a_i u_i=0$. But $u_1,\dots,u_k,w_1,\dots,w_{n-k}$ are independent (a basis), so all coefficients vanish; in particular every $b_j=0$. *(membership in kernel; independence of the full basis)*
6. By steps 4–5 the $T(w_j)$ form a basis of the image, proving the claim and the theorem. $\blacksquare$

**Worked example.** Let $T:\mathbb{R}^3\to\mathbb{R}^2$, $T(x,y,z)=(x+y,\ y+z)$. The kernel solves $x+y=0,\ y+z=0$, i.e. $y=-x,\ z=-y=x$, so $\ker T=\{(x,-x,x)\}=\operatorname{span}\big((1,-1,1)\big)$, nullity $1$. The image contains $T(e_1)=(1,0)$ and $T(e_2)=(1,1)$, which are independent and span $\mathbb{R}^2$, so rank $2$. Check: $1+2=3=\dim\mathbb{R}^3$. 

**Second worked example — differentiation as a linear map.** On $P_3$ (polynomials of degree $\le3$, dimension $4$), the derivative $D(p)=p'$ is linear because $(p+q)'=p'+q'$ and $(\lambda p)'=\lambda p'$ — the familiar calculus rules *are* the linearity axioms. Its kernel is the constants $\{a\}$, nullity $1$; its image is $P_2$ (every quadratic is the derivative of some cubic), rank $3$. Rank–nullity: $1+3=4=\dim P_3$. Notice $D$ is *not* injective (constants vanish) yet *is* surjective onto $P_2$ — exactly what a non-zero nullity forces.

> **Corollary — for operators on a finite-dimensional space, injective $\Leftrightarrow$ surjective.** If $T:V\to V$ with $\dim V<\infty$, then $T$ injective $\iff$ $\ker T=\{0\}$ $\iff$ $\dim(\operatorname{im}T)=\dim V$ (by rank–nullity) $\iff$ $\operatorname{im}T=V$ $\iff$ $T$ surjective. So a square system either has a unique solution for every right-hand side, or fails both ways. (This collapses in infinite dimensions: the shift operator on sequences is injective but not surjective — a fact at the heart of functional analysis.)

**Pitfall.** Rank–nullity is about *dimensions*, not the subspaces themselves. The kernel and image can even live in different spaces (when $V\ne W$), and there is in general no natural way to "add" them back into $V$; what is conserved is only the count of dimensions.

<a id="s4"></a>
### Matrices as linear maps; multiplication as composition; change of basis

**What and why.** Once you fix bases, every linear map becomes a rectangular grid of numbers — a **matrix** — and the abstract operation "compose two maps" becomes the concrete recipe "multiply two matrices." Choosing a different basis re-expresses the same map; the bookkeeping for that is **change of basis**, central in physics where one freely switches between coordinate frames or measurement bases.

> **Definition — matrix of a linear map.** Fix a basis $(v_1,\dots,v_n)$ of $V$ and $(w_1,\dots,w_m)$ of $W$. For each $j$, expand $T(v_j)=\sum_{i=1}^m A_{ij}\,w_i$. The numbers $A_{ij}\in\mathbb{F}$ form the **matrix** $A=[A_{ij}]$ of $T$ (size $m\times n$: $m$ rows, $n$ columns). **The $j$-th column of $A$ is the coordinate list of $T(v_j)$.** This single sentence is the whole meaning of a matrix.

Why does the matrix determine $T$? Because a linear map is *completely determined by what it does to a basis*: if $v=\sum_j x_j v_j$ then linearity gives $T(v)=\sum_j x_j T(v_j)=\sum_j x_j \sum_i A_{ij}w_i=\sum_i\big(\sum_j A_{ij}x_j\big)w_i$. So the coordinates $y_i$ of $T(v)$ are $y_i=\sum_j A_{ij}x_j$ — which is exactly the rule for **matrix times column vector**.

> **Definition — matrix multiplication.** For $A$ of size $m\times n$ and $B$ of size $n\times p$, their product $AB$ is the $m\times p$ matrix with entries
>
> $$
> (AB)_{ik}=\sum_{j=1}^n A_{ij}B_{jk}.
> $$

> **Theorem — multiplication is composition.** If $S:U\to V$ has matrix $B$ and $T:V\to W$ has matrix $A$ (in compatible bases), then $T\circ S$ has matrix $AB$.

**Proof.**
1. Let $(u_k)$, $(v_j)$, $(w_i)$ be the chosen bases of $U,V,W$, with $S(u_k)=\sum_j B_{jk}v_j$ and $T(v_j)=\sum_i A_{ij}w_i$. *(definition of the matrices)*
2. Compute $(T\circ S)(u_k)=T\big(\sum_j B_{jk}v_j\big)=\sum_j B_{jk}\,T(v_j)$, by linearity of $T$. *(linearity)*
3. Substitute $T(v_j)=\sum_i A_{ij}w_i$: this becomes $\sum_j B_{jk}\sum_i A_{ij}w_i=\sum_i\big(\sum_j A_{ij}B_{jk}\big)w_i$. *(substitution; reorder finite sums)*
4. The coefficient of $w_i$ is $\sum_j A_{ij}B_{jk}=(AB)_{ik}$ by definition of the product. So the matrix of $T\circ S$ is exactly $AB$. $\blacksquare$

This is *why* matrix multiplication has its peculiar row-times-column formula: it is forced by the demand that it model composition of maps. It also explains why matrix multiplication is associative ($(AB)C=A(BC)$, because composing functions is associative) but generally **not commutative** ($AB\ne BA$, because doing transformations in the opposite order gives a different result). Non-commutativity is the mathematical root of the Heisenberg uncertainty principle.

**Worked example (non-commutativity).** With $A=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}$ and $B=\begin{psmallmatrix}0&0\\1&0\end{psmallmatrix}$: $AB=\begin{psmallmatrix}1&0\\0&0\end{psmallmatrix}$ but $BA=\begin{psmallmatrix}0&0\\0&1\end{psmallmatrix}$, so $AB\ne BA$.

> **Definition — change of basis.** Suppose $(v_j)$ and $(v'_j)$ are two bases of $V$, related by $v'_j=\sum_i P_{ij}v_i$. The invertible matrix $P=[P_{ij}]$ (its columns are the new basis vectors in old coordinates) is the **change-of-basis matrix**. A coordinate vector transforms as $[v]_{\text{old}}=P[v]_{\text{new}}$.

> **Theorem — how a matrix changes basis.** If a linear operator $T:V\to V$ has matrix $A$ in the old basis and $A'$ in the new basis, then $A'=P^{-1}AP$.

**Proof.**
1. Let $x'=[v]_{\text{new}}$ and $x=[v]_{\text{old}}=Px'$. Then $T(v)$ has old coordinates $Ax$ and new coordinates $A'x'$, with old$=$new converted: $Ax=P(A'x')$. *(definition of the matrix of $T$ and of $P$)*
2. Substitute $x=Px'$: $A(Px')=P(A'x')$, i.e. $APx'=PA'x'$ for all coordinate vectors $x'$. *(substitution)*
3. Since this holds for every $x'$, the matrices are equal: $AP=PA'$. Multiply on the left by $P^{-1}$ (it exists because a change-of-basis matrix is invertible): $A'=P^{-1}AP$. $\blacksquare$

Matrices related by $A'=P^{-1}AP$ are called **similar** (§s8). They are the same operator wearing different coordinate clothes.

**Worked example — change of basis in action.** Let $T$ on $\mathbb{R}^2$ be reflection across the line $y=x$. In the standard basis $T(e_1)=(0,1)=e_2$ and $T(e_2)=e_1$, so $A=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}$. Switch to the basis $v'_1=(1,1)$ (along the mirror) and $v'_2=(1,-1)$ (perpendicular). Reflection fixes $v'_1$ and negates $v'_2$, so in the new basis the matrix is the diagonal $A'=\begin{psmallmatrix}1&0\\0&-1\end{psmallmatrix}$. Concretely $P=\begin{psmallmatrix}1&1\\1&-1\end{psmallmatrix}$, $P^{-1}=\tfrac12\begin{psmallmatrix}1&1\\1&-1\end{psmallmatrix}$, and one checks $P^{-1}AP=\begin{psmallmatrix}1&0\\0&-1\end{psmallmatrix}$. The geometry — a reflection — is clearest in the basis adapted to it; finding such a basis is what *diagonalization* (§s8) automates.

**Pitfall — row vs. column conventions.** Whether you write $A\mathbf x$ (column vectors on the right) or $\mathbf x A$ (row vectors on the left) flips the order of products and transposes the change-of-basis formula. This guide uses column vectors throughout, so maps compose right-to-left exactly as functions do: $(T\circ S)(x)=T(S(x))$ matches $AB\mathbf x=A(B\mathbf x)$.

<a id="s5"></a>
### Systems of linear equations; Gaussian elimination; rank

**What and why.** A system of linear equations $A\mathbf{x}=\mathbf{b}$ asks: which input vectors $\mathbf{x}$ does the map $A$ send to a given target $\mathbf{b}$? **Gaussian elimination** is the systematic algorithm to answer this, and it simultaneously computes the **rank** — the true number of independent constraints.

> **Definition — the three elementary row operations.** On the augmented matrix $[A\,|\,\mathbf{b}]$ we may (R1) swap two rows; (R2) multiply a row by a nonzero scalar; (R3) add a scalar multiple of one row to another. **Each operation preserves the solution set**, because it corresponds to a reversible recombination of equations — and any operation you can undo cannot lose or gain solutions.

> **Definition — row echelon form (REF).** A matrix is in **echelon form** if every nonzero row begins with a leading nonzero entry (a **pivot**) lying strictly to the right of the pivot above it, and all-zero rows sit at the bottom. **Gaussian elimination** uses R1–R3 to bring any matrix to echelon form; continuing to clear entries above pivots and scaling pivots to $1$ gives the unique **reduced** row echelon form (RREF).

> **Definition — rank.** The **rank** of $A$ is the number of pivots in its echelon form — equivalently (and this needs proof) the dimension of the image, i.e. the number of independent columns.

> **Proposition — pivots count independent columns.** The number of pivots equals $\dim(\operatorname{im}A)$, the column rank.
**Proof.**
1. Row operations are left-multiplications by invertible matrices, so they do not change *linear relations among columns*: if $\sum c_j a_j=0$ for columns of $A$, the same coefficients give $\sum c_j a'_j=0$ after any row operation, and conversely. *(invertible left-multiply preserves $A\mathbf c=0$)*
2. In echelon form, the **pivot columns** are independent (each pivot sits in a row where the others are zero, so no nontrivial combination of pivot columns can cancel), while each **non-pivot column** is a combination of the pivot columns to its left (back-substitution expresses it). *(structure of echelon form)*
3. Hence the pivot columns form a basis of the column space, so their count — the number of pivots — equals $\dim(\operatorname{im}A)$. By step 1 this is the same for $A$. $\blacksquare$

> **Existence/uniqueness of solutions.** The system $A\mathbf x=\mathbf b$ is **consistent** (has a solution) iff $\mathbf b$ lies in $\operatorname{im}A$, detected as: no echelon row of the form $[0\,\cdots\,0\,|\,c]$ with $c\ne0$. When consistent, the solution is **unique** iff every column is a pivot column (no free variables); otherwise the free variables parametrize an affine family of solutions. This is rank–nullity (§s3) in disguise: $\#\text{free variables}=\dim(\ker A)=n-\operatorname{rank}A$.

**Worked example.** Solve $\begin{cases}x+2y+z=4\\ 2x+y-z=1\\ x-y-2z=-3\end{cases}$.
Augmented matrix and elimination:
$$
\left[\begin{array}{ccc|c}1&2&1&4\\2&1&-1&1\\1&-1&-2&-3\end{array}\right]
\xrightarrow[R3-R1]{R2-2R1}
\left[\begin{array}{ccc|c}1&2&1&4\\0&-3&-3&-7\\0&-3&-3&-7\end{array}\right]
\xrightarrow{R3-R2}
\left[\begin{array}{ccc|c}1&2&1&4\\0&-3&-3&-7\\0&0&0&0\end{array}\right].
$$
Two pivots (columns $1,2$), so rank $2$; the zero bottom row is consistent. With $z=t$ free, the middle row gives $-3y-3t=-7\Rightarrow y=\tfrac{7}{3}-t$, and the top row gives $x=4-2y-t=4-2(\tfrac73-t)-t=-\tfrac23+t$. Solution family: $(x,y,z)=(-\tfrac23,\tfrac73,0)+t(1,-1,1)$. The direction $(1,-1,1)$ is exactly the kernel from the §s3 example — same matrix structure.

## Part B — Spectra: determinants, eigenvalues, diagonalization

<a id="s6"></a>
### Determinants: definition, properties, volume meaning, multiplicativity

**What and why.** The **determinant** of a square matrix is a single number that tells you whether the map is invertible (nonzero determinant $\Leftrightarrow$ invertible) and by how much it scales volume. It is the key to eigenvalues via the characteristic polynomial.

> **Definition — determinant.** For an $n\times n$ matrix $A=[A_{ij}]$,
>
> $$
> \det A=\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)\,A_{1\sigma(1)}A_{2\sigma(2)}\cdots A_{n\sigma(n)},
> $$
> where the sum runs over all **permutations** $\sigma$ of $\{1,\dots,n\}$ (rearrangements), and $\operatorname{sgn}(\sigma)=\pm1$ is $+1$ if $\sigma$ is built from an even number of swaps and $-1$ if odd. For $2\times2$: $\det\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}=ad-bc$. For $3\times3$ this is the familiar six-term rule.

The defining formula is unwieldy; what we actually use are its **characterizing properties**, which we now state and which uniquely pin down the determinant.

> **Theorem — the determinant is the unique function that is (i) multilinear and alternating in the columns and (ii) equals $1$ on the identity.** Concretely: (a) scaling one column by $\lambda$ scales $\det$ by $\lambda$; (b) adding a multiple of one column to another leaves $\det$ unchanged; (c) swapping two columns flips the sign; (d) $\det I=1$.

**Proof sketch that properties (a)–(d) follow from the definition, then determine it.**
1. *(Multilinearity, a.)* Each product term contains exactly one factor from each column, so each term is linear in any single column; summing keeps linearity. *(each term linear $\Rightarrow$ sum linear)*
2. *(Alternating, c.)* Swapping columns $p,q$ relabels each permutation $\sigma\mapsto\sigma\circ(p\,q)$, which multiplies $\operatorname{sgn}$ by $-1$; reindexing the sum shows $\det$ negates. *(sign of a transposition is $-1$)*
3. *(b follows.)* If two columns are equal, swapping them both negates the determinant (by c) and leaves it unchanged (same matrix), so $\det=-\det$, giving $\det=0$. Adding $\lambda(\text{col }q)$ to col $p$ adds $\lambda\det(\text{matrix with col }q\text{ in two slots})=0$. *(alternating $\Rightarrow$ repeated column gives }0)*
4. *(Uniqueness.)* Any multilinear alternating function with $\det I=1$, expanded over columns written in the standard basis, collapses by (a)–(c) to exactly the permutation sum — so the formula is forced. $\blacksquare$

> **Theorem — multiplicativity.** $\det(AB)=\det(A)\det(B)$.

**Proof.**
1. Fix $A$ and view $D(B):=\det(AB)$ as a function of the *columns* of $B$. Since the $k$-th column of $AB$ is $A$ times the $k$-th column of $B$, and matrix-times-vector is linear, $D$ is multilinear and alternating in $B$'s columns. *(linearity of $A(\cdot)$; alternation inherited)*
2. By the uniqueness theorem, any multilinear alternating function equals $\det(B)$ times its value on the identity. So $D(B)=\det(B)\cdot D(I)$. *(uniqueness up to the value at $I$)*
3. But $D(I)=\det(AI)=\det A$. Therefore $\det(AB)=\det(A)\det(B)$. $\blacksquare$

> **Corollary.** $A$ is invertible iff $\det A\ne0$, and then $\det(A^{-1})=1/\det A$ (from $\det A\det A^{-1}=\det I=1$). Also $\det A=0$ exactly when the columns are dependent (the map collapses dimension).

**Geometric meaning.** $|\det A|$ is the factor by which $A$ scales $n$-dimensional volume: the unit cube (spanned by $e_1,\dots,e_n$) is sent to the parallelepiped spanned by the columns of $A$, whose volume is $|\det A|$. The sign of $\det A$ records whether orientation is preserved ($+$) or flipped ($-$). Volume scaling **multiplies** under composition — which is precisely why determinants multiply.

**Worked example.** $A=\begin{psmallmatrix}2&1\\1&3\end{psmallmatrix}$ has $\det A=2\cdot3-1\cdot1=5\ne0$, so $A$ is invertible and stretches areas by $5$. Indeed $A^{-1}=\tfrac15\begin{psmallmatrix}3&-1\\-1&2\end{psmallmatrix}$, with $\det A^{-1}=\tfrac15$.

**Second worked example — cofactor expansion of a $3\times3$.** Expanding along the first row,
$$
\det\begin{pmatrix}1&2&0\\3&-1&4\\2&0&1\end{pmatrix}
=1\det\begin{psmallmatrix}-1&4\\0&1\end{psmallmatrix}-2\det\begin{psmallmatrix}3&4\\2&1\end{psmallmatrix}+0
=1(-1)-2(3-8)=-1+10=9.
$$
Since $9\ne0$ the three rows are linearly independent and the matrix is invertible; geometrically it scales volume by $9$. The cofactor expansion is just the permutation sum regrouped by which entry of the first row appears — a practical computation that the defining formula justifies.

**Pitfall — the determinant is multilinear, not linear.** It is linear in *each column separately* but **not** in the matrix as a whole: $\det(A+B)\ne\det A+\det B$ in general (try $A=B=I$ in $2\times2$: $\det(2I)=4$ but $\det I+\det I=2$). Likewise $\det(\lambda A)=\lambda^n\det A$ for an $n\times n$ matrix, because all $n$ columns scale at once.

<a id="s7"></a>
### Eigenvalues and eigenvectors; the characteristic polynomial

**What and why.** An **eigenvector** of an operator is a nonzero vector whose direction the operator leaves unchanged, merely scaling it by an **eigenvalue**. In quantum mechanics eigenvectors are the *states of definite measurement* and eigenvalues are the *possible measured values* — this is the bridge §s14 makes explicit.

> **Definition — eigenvalue, eigenvector.** For a linear operator $T:V\to V$, a scalar $\lambda\in\mathbb{F}$ is an **eigenvalue** if there is a **nonzero** vector $v$ (the **eigenvector**) with $T(v)=\lambda v$. The set of all $v$ (including $0$) with $T(v)=\lambda v$ is the **eigenspace** $E_\lambda=\ker(T-\lambda I)$, a subspace.

> **Theorem — eigenvalues are roots of the characteristic polynomial.** $\lambda$ is an eigenvalue of the matrix $A$ iff $\det(A-\lambda I)=0$. The polynomial $p(\lambda)=\det(A-\lambda I)$ is the **characteristic polynomial**.

**Proof.**
1. $\lambda$ is an eigenvalue $\iff$ there is $v\ne0$ with $Av=\lambda v$ $\iff$ $(A-\lambda I)v=0$ has a nonzero solution. *(rearrange the eigenvalue equation)*
2. A homogeneous system $(A-\lambda I)v=0$ has a nonzero solution $\iff$ the matrix $A-\lambda I$ is **not** invertible (an invertible matrix has only $v=0$ in its kernel). *(invertible $\Leftrightarrow$ trivial kernel)*
3. By the determinant corollary (§s6), $A-\lambda I$ is non-invertible $\iff \det(A-\lambda I)=0$. Chaining the equivalences gives the claim. $\blacksquare$

Because $\det(A-\lambda I)$ is a degree-$n$ polynomial in $\lambda$, over $\mathbb{C}$ it always has $n$ roots counted with multiplicity (the Fundamental Theorem of Algebra: every nonconstant complex polynomial factors completely). **This is one reason quantum mechanics is built over $\mathbb{C}$**: operators are guaranteed eigenvalues. Over $\mathbb{R}$ a rotation may have *no* real eigenvalue.

> **Definitions — multiplicities.** The **algebraic multiplicity** of $\lambda$ is its multiplicity as a root of $p$. The **geometric multiplicity** is $\dim E_\lambda$. Always $1\le\text{geometric}\le\text{algebraic}$.

**Worked example.** $A=\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}$. Then $p(\lambda)=\det\begin{psmallmatrix}2-\lambda&1\\1&2-\lambda\end{psmallmatrix}=(2-\lambda)^2-1=\lambda^2-4\lambda+3=(\lambda-1)(\lambda-3)$. Eigenvalues $1,3$. For $\lambda=3$: solve $(A-3I)v=0$, i.e. $\begin{psmallmatrix}-1&1\\1&-1\end{psmallmatrix}v=0\Rightarrow v=(1,1)$. For $\lambda=1$: $v=(1,-1)$. The eigenvectors are orthogonal — no accident, since $A$ is symmetric (foreshadowing §s11).

**Second worked example — no real eigenvalues.** The rotation by $90^\circ$, $R=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}$, has $p(\lambda)=\lambda^2+1$, whose roots are $\pm i$ — *not real*. Over $\mathbb{R}$ this matrix has **no** eigenvectors, which matches the geometry: a $90^\circ$ rotation leaves no direction unmoved. Over $\mathbb{C}$ it has eigenvalues $\pm i$ with eigenvectors $(1,\mp i)$. This is the cleanest illustration of why the field matters and why complex scalars guarantee a spectrum.

> **Trace and determinant from eigenvalues.** Expanding $p(\lambda)=\det(A-\lambda I)=(-1)^n\big(\lambda^n-(\operatorname{tr}A)\lambda^{n-1}+\dots+(-1)^n\det A\big)$ and comparing with $\prod(\lambda-\lambda_k)$ shows the sum of eigenvalues equals the **trace** (sum of diagonal entries) and their product equals the **determinant**. For the example $A=\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}$: eigenvalues $1+3=4=\operatorname{tr}A$ and $1\cdot3=3=\det A$. These two checks catch most arithmetic errors instantly.

**Pitfall.** An eigenvector is by definition nonzero; the equation $T(0)=\lambda 0$ holds for *every* $\lambda$, so allowing $v=0$ would make every scalar an "eigenvalue." The zero vector lives in every eigenspace but is never an eigenvector.

<a id="s8"></a>
### Diagonalization and similarity; when is a matrix diagonalizable

**What and why.** A **diagonal** matrix acts independently on each coordinate — the simplest possible operator. **Diagonalizing** means finding a basis (of eigenvectors) in which the operator is diagonal; then powers, exponentials, and dynamics become trivial to compute. In quantum mechanics, diagonalizing the energy operator (Hamiltonian) solves the dynamics.

> **Definition — diagonalizable.** An operator $A$ is **diagonalizable** if there is an invertible $P$ with $P^{-1}AP=D$ diagonal — equivalently (recall similarity, §s4) if $A$ has a basis of eigenvectors.

> **Theorem — eigenvector basis $\Leftrightarrow$ diagonalizable.** $A$ is diagonalizable iff $V$ has a basis consisting of eigenvectors of $A$; and then the columns of $P$ are those eigenvectors while the diagonal entries of $D$ are the corresponding eigenvalues.

**Proof.**
1. Suppose $v_1,\dots,v_n$ are eigenvectors forming a basis, $Av_j=\lambda_j v_j$. Let $P$ have these as columns. Then $AP$ has $j$-th column $Av_j=\lambda_j v_j$, while $PD$ (with $D=\operatorname{diag}(\lambda_j)$) has $j$-th column $\lambda_j v_j$ too. So $AP=PD$, hence $P^{-1}AP=D$. *(column-by-column matrix identity; $P$ invertible since its columns are a basis)*
2. Conversely if $P^{-1}AP=D$ is diagonal, reverse the computation: $AP=PD$ says $A(\text{col}_j P)=\lambda_j(\text{col}_j P)$, so the columns of $P$ are eigenvectors, and being columns of an invertible matrix they form a basis. $\blacksquare$

> **Theorem — eigenvectors for distinct eigenvalues are independent.** Hence an $n\times n$ matrix with $n$ distinct eigenvalues is diagonalizable.

**Proof (by induction on the number of eigenvalues).**
1. One eigenvector is independent (it is nonzero). *(base case)*
2. Suppose $v_1,\dots,v_k$ (distinct eigenvalues $\lambda_1,\dots,\lambda_k$) are independent and consider $v_{k+1}$ with eigenvalue $\lambda_{k+1}\ne\lambda_i$. Assume a dependence $v_{k+1}=\sum_{i\le k}c_i v_i$. *(suppose dependence to derive contradiction)*
3. Apply $A$: $\lambda_{k+1}v_{k+1}=\sum c_i\lambda_i v_i$. Also multiply the dependence by $\lambda_{k+1}$: $\lambda_{k+1}v_{k+1}=\sum c_i\lambda_{k+1}v_i$. Subtract: $0=\sum c_i(\lambda_i-\lambda_{k+1})v_i$. *(two expressions for the same vector)*
4. By independence of $v_1,\dots,v_k$, each $c_i(\lambda_i-\lambda_{k+1})=0$; since $\lambda_i\ne\lambda_{k+1}$, every $c_i=0$, so $v_{k+1}=0$ — contradicting that it is an eigenvector. Hence $v_1,\dots,v_{k+1}$ are independent. $\blacksquare$

> **Criterion — when diagonalizable.** $A$ is diagonalizable iff for **every** eigenvalue the geometric multiplicity equals the algebraic multiplicity (the eigenspaces are "big enough" and together span $V$). When some eigenspace is too small, the matrix is **defective** and cannot be diagonalized.

**Worked example (diagonalizable).** Reusing $A=\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}$ with eigenpairs $(3,(1,1)),(1,(1,-1))$: set $P=\begin{psmallmatrix}1&1\\1&-1\end{psmallmatrix}$, $D=\begin{psmallmatrix}3&0\\0&1\end{psmallmatrix}$. Then $P^{-1}AP=D$, and $A^n=PD^nP^{-1}$ is instant to compute.

**Worked example (defective).** $N=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}$ has characteristic polynomial $\lambda^2$, so $\lambda=0$ with algebraic multiplicity $2$, but $\ker N=\operatorname{span}((1,0))$ has dimension $1$. Geometric $<$ algebraic, so $N$ is **not** diagonalizable. (Such a matrix is the smallest **Jordan block**; the Jordan form is the systematic "best possible" near-diagonalization for defective matrices, but Hermitian operators — the ones quantum mechanics cares about — are never defective, as §s11 proves.)

**Why diagonalization is useful — computing $A^{100}$.** If $A=PDP^{-1}$ then $A^k=PD^kP^{-1}$, because the inner $P^{-1}P$ pairs telescope: $A^2=PDP^{-1}PDP^{-1}=PD^2P^{-1}$, and induction continues. Raising a *diagonal* matrix to a power just raises each diagonal entry. So for $A=\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}$, $A^{100}=P\begin{psmallmatrix}3^{100}&0\\0&1\end{psmallmatrix}P^{-1}$ — a closed form, no repeated multiplication. The same trick defines the **matrix exponential** $e^{A}=Pe^{D}P^{-1}$, which solves linear differential equations $\dot x=Ax$ and, with $A=-iHt/\hbar$, generates quantum time evolution (§s14).

**Pitfall — similarity preserves the spectrum, not the eigenvectors' coordinates.** Similar matrices share characteristic polynomial, eigenvalues, trace, determinant, and rank, because $\det(P^{-1}AP-\lambda I)=\det(P^{-1}(A-\lambda I)P)=\det(A-\lambda I)$. But the eigenvectors are expressed in different bases, so their coordinate lists differ. "Same operator, different coordinates" is the right mental model.

## Part C — Geometry: inner products, adjoints, the spectral theorem

<a id="s9"></a>
### Inner product spaces; norms, orthogonality, Cauchy–Schwarz, Gram–Schmidt

**What and why.** To do geometry — lengths, angles, perpendicularity — a vector space needs an **inner product**. The complex (Hermitian) version is the structure of quantum state space, where $\langle\psi|\phi\rangle$ encodes probability amplitudes.

> **Definition — inner product.** An **inner product** on a vector space $V$ over $\mathbb{F}\in\{\mathbb{R},\mathbb{C}\}$ is a map $\langle\cdot,\cdot\rangle:V\times V\to\mathbb{F}$ with, for all $u,v,w$ and $\lambda$:
> 1. **(Conjugate symmetry)** $\langle u,v\rangle=\overline{\langle v,u\rangle}$ (the bar is complex conjugation; over $\mathbb{R}$ this is plain symmetry).
> 2. **(Linearity in the first slot)** $\langle\lambda u+w,v\rangle=\lambda\langle u,v\rangle+\langle w,v\rangle$. (Then it is *conjugate*-linear in the second slot.)
> 3. **(Positive-definiteness)** $\langle v,v\rangle\ge0$, with equality iff $v=0$.
>
> The **norm** is $\|v\|=\sqrt{\langle v,v\rangle}$ (a real length). Vectors are **orthogonal** if $\langle u,v\rangle=0$.

The standard examples: on $\mathbb{R}^n$, $\langle x,y\rangle=\sum x_iy_i$ (dot product); on $\mathbb{C}^n$, $\langle x,y\rangle=\sum x_i\overline{y_i}$ (the conjugate makes $\langle v,v\rangle=\sum|v_i|^2$ real and positive); on functions, $\langle f,g\rangle=\int f\overline{g}$.

> **Theorem — Cauchy–Schwarz inequality.** $|\langle u,v\rangle|\le\|u\|\,\|v\|$, with equality iff $u,v$ are linearly dependent.

**Proof.**
1. If $v=0$ both sides are $0$; done. So assume $v\ne0$, hence $\|v\|^2=\langle v,v\rangle>0$. *(handle the trivial case)*
2. Let $\lambda=\dfrac{\langle u,v\rangle}{\langle v,v\rangle}$ and consider $w=u-\lambda v$ (the part of $u$ "perpendicular to $v$"). *(orthogonal projection)*
3. Compute $\langle w,v\rangle=\langle u,v\rangle-\lambda\langle v,v\rangle=\langle u,v\rangle-\langle u,v\rangle=0$: $w\perp v$. *(plug in $\lambda$)*
4. By positive-definiteness $0\le\langle w,w\rangle=\langle u-\lambda v,\,u-\lambda v\rangle=\langle u,u\rangle-\overline{\lambda}\langle u,v\rangle$ (the cross terms with $v$ vanish since $w\perp v$, more directly: expand and use $\langle w,v\rangle=0$). Substituting $\lambda$ gives $0\le\|u\|^2-\dfrac{|\langle u,v\rangle|^2}{\|v\|^2}$. *(positivity of the norm of $w$)*
5. Rearrange: $|\langle u,v\rangle|^2\le\|u\|^2\|v\|^2$; take square roots. Equality holds iff $w=0$, i.e. $u=\lambda v$ — linear dependence. $\blacksquare$

> **Corollary — triangle inequality.** $\|u+v\|\le\|u\|+\|v\|$.
**Proof.** $\|u+v\|^2=\|u\|^2+2\operatorname{Re}\langle u,v\rangle+\|v\|^2\le\|u\|^2+2\|u\|\|v\|+\|v\|^2=(\|u\|+\|v\|)^2$, using $\operatorname{Re}\langle u,v\rangle\le|\langle u,v\rangle|\le\|u\|\|v\|$ (Cauchy–Schwarz). Take roots. $\blacksquare$

> **Definition — orthonormal basis.** A basis $(e_1,\dots,e_n)$ is **orthonormal** if $\langle e_i,e_j\rangle=\delta_{ij}$ (equal to $1$ if $i=j$, else $0$). In such a basis coordinates are just inner products: $v=\sum_i\langle v,e_i\rangle e_i$.

> **Theorem — Gram–Schmidt.** Any list of independent vectors $v_1,\dots,v_k$ can be converted into an orthonormal list $e_1,\dots,e_k$ with the same span.

**Proof (constructive algorithm).**
1. Set $u_1=v_1$ and $e_1=u_1/\|u_1\|$ (allowed: $v_1\ne0$ since independent). *(normalize the first)*
2. Having $e_1,\dots,e_{j-1}$ orthonormal, subtract from $v_j$ its components along them: $u_j=v_j-\sum_{i<j}\langle v_j,e_i\rangle e_i$. *(project out the previous directions)*
3. Then $u_j\ne0$: if it were $0$, $v_j$ would lie in $\operatorname{span}(e_1,\dots,e_{j-1})=\operatorname{span}(v_1,\dots,v_{j-1})$, contradicting independence. Set $e_j=u_j/\|u_j\|$. *(independence keeps $u_j$ nonzero)*
4. Check orthogonality: for $i<j$, $\langle u_j,e_i\rangle=\langle v_j,e_i\rangle-\langle v_j,e_i\rangle\langle e_i,e_i\rangle=\langle v_j,e_i\rangle-\langle v_j,e_i\rangle=0$ (other terms drop by orthonormality of earlier $e$'s). So each new $e_j$ is orthogonal to all previous, and the spans match at every stage. $\blacksquare$

**Worked example.** Orthonormalize $v_1=(1,1,0),v_2=(1,0,1)$ in $\mathbb{R}^3$. $e_1=\tfrac1{\sqrt2}(1,1,0)$. Then $\langle v_2,e_1\rangle=\tfrac1{\sqrt2}$, so $u_2=(1,0,1)-\tfrac1{\sqrt2}\cdot\tfrac1{\sqrt2}(1,1,0)=(1,0,1)-(\tfrac12,\tfrac12,0)=(\tfrac12,-\tfrac12,1)$, and $\|u_2\|=\sqrt{\tfrac14+\tfrac14+1}=\sqrt{\tfrac32}$, giving $e_2=\sqrt{\tfrac23}(\tfrac12,-\tfrac12,1)$. One checks $\langle e_1,e_2\rangle=0$.

> **The angle interpretation.** Cauchy–Schwarz lets us *define* the angle $\theta$ between real vectors by $\cos\theta=\dfrac{\langle u,v\rangle}{\|u\|\,\|v\|}$, which lies in $[-1,1]$ exactly because $|\langle u,v\rangle|\le\|u\|\|v\|$. Orthogonality ($\langle u,v\rangle=0$) is the case $\theta=90^\circ$. In the complex/quantum setting $|\langle\psi,\phi\rangle|^2$ is the probability that a system prepared in state $\phi$ is found in state $\psi$, and Cauchy–Schwarz guarantees this probability never exceeds $1$.

**Pitfall — the conjugate cannot be dropped in the complex case.** For $v=(1,i)\in\mathbb{C}^2$, the "naive" form $\sum v_iv_i=1+i^2=0$ would make a nonzero vector have zero length. The correct Hermitian form $\sum v_i\overline{v_i}=|1|^2+|i|^2=2>0$ restores positive-definiteness. The conjugate in the second slot is not decoration; it is what makes lengths real and positive.

> **Pythagoras and the parallelogram law.** If $u\perp v$ then $\|u+v\|^2=\|u\|^2+\|v\|^2$ (expand the inner product; the cross terms $\langle u,v\rangle$ vanish). More generally the parallelogram law $\|u+v\|^2+\|u-v\|^2=2\|u\|^2+2\|v\|^2$ holds, and it characterizes which norms come from an inner product — a fact that opens the door to the *functional analysis* guide.

<a id="s10"></a>
### Adjoints; self-adjoint (Hermitian), unitary, and normal operators

**What and why.** The **adjoint** $T^*$ of an operator is its "mirror with respect to the inner product." The three classes that govern quantum mechanics are defined by how an operator relates to its adjoint: **Hermitian** ($T=T^*$, observables), **unitary** ($T^*T=I$, time evolution and symmetries), and **normal** ($TT^*=T^*T$, the class the spectral theorem covers).

> **Definition — adjoint.** Given an operator $T$ on an inner product space, its **adjoint** $T^*$ is the unique operator satisfying $\langle Tu,v\rangle=\langle u,T^*v\rangle$ for all $u,v$. In an orthonormal basis, $T^*$ is the **conjugate transpose** of $T$'s matrix: $(T^*)_{ij}=\overline{T_{ji}}$.

**Why the matrix is the conjugate transpose.** With orthonormal $(e_i)$, $T_{ij}=\langle Te_j,e_i\rangle$. Then $(T^*)_{ij}=\langle T^*e_j,e_i\rangle=\overline{\langle e_i,T^*e_j\rangle}=\overline{\langle Te_i,e_j\rangle}=\overline{T_{ji}}$, using conjugate symmetry and the defining property. *(each step names the rule: orthonormal coordinates, conjugate symmetry, adjoint definition)*

> **Definitions — the three classes.**
> - **Self-adjoint / Hermitian:** $T^*=T$. Matrix: $\overline{T_{ji}}=T_{ij}$.
> - **Unitary:** $T^*T=TT^*=I$, i.e. $T^{-1}=T^*$. Equivalent to **preserving the inner product**: $\langle Tu,Tv\rangle=\langle u,v\rangle$.
> - **Normal:** $T^*T=TT^*$ (commutes with its own adjoint). Both Hermitian and unitary operators are normal.

> **Proposition — unitary $\Leftrightarrow$ inner-product-preserving.**
**Proof.** If $T^*T=I$ then $\langle Tu,Tv\rangle=\langle u,T^*Tv\rangle=\langle u,v\rangle$. Conversely if $\langle Tu,Tv\rangle=\langle u,v\rangle$ for all $u,v$, then $\langle u,(T^*T-I)v\rangle=0$ for all $u$; taking $u=(T^*T-I)v$ forces $(T^*T-I)v=0$ for all $v$, so $T^*T=I$. $\blacksquare$

> **Proposition — Hermitian operators have real diagonal inner products.** If $T=T^*$ then $\langle Tv,v\rangle$ is real for all $v$.
**Proof.** $\langle Tv,v\rangle=\langle v,T^*v\rangle=\langle v,Tv\rangle=\overline{\langle Tv,v\rangle}$ (conjugate symmetry), and a number equal to its own conjugate is real. $\blacksquare$ This is the seed of "Hermitian $\Rightarrow$ real eigenvalues" (§s11), the reason observables are Hermitian.

**Worked example.** $T=\begin{psmallmatrix}2&i\\-i&3\end{psmallmatrix}$ is Hermitian: its conjugate transpose swaps the off-diagonals and conjugates, $\overline{i}=-i$ goes to position $(2,1)$ — and indeed $(2,1)$ entry is $-i$. The matrix $U=\tfrac1{\sqrt2}\begin{psmallmatrix}1&1\\1&-1\end{psmallmatrix}$ (the Hadamard gate) is unitary: $U^*U=I$.

**Second worked example — a normal but non-Hermitian, non-unitary operator.** $N=\begin{psmallmatrix}1&1\\-1&1\end{psmallmatrix}$ has $N^*=\begin{psmallmatrix}1&-1\\1&1\end{psmallmatrix}$. Compute $N^*N=\begin{psmallmatrix}2&0\\0&2\end{psmallmatrix}=NN^*$, so $N$ is normal. It is not Hermitian ($N\ne N^*$) and not unitary ($N^*N=2I\ne I$). Normality is the genuinely larger class the spectral theorem needs, and this example shows it contains operators outside the other two.

> **The Pauli matrices — the algebra of spin.** The three Hermitian matrices $\sigma_x=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix},\ \sigma_y=\begin{psmallmatrix}0&-i\\i&0\end{psmallmatrix},\ \sigma_z=\begin{psmallmatrix}1&0\\0&-1\end{psmallmatrix}$ represent spin-measurement along the three axes. Each is Hermitian (observable) *and* unitary (so also a quantum gate), with eigenvalues $\pm1$. They famously fail to commute, e.g. $\sigma_x\sigma_y-\sigma_y\sigma_x=2i\sigma_z$, and this non-commutativity is precisely why spin components cannot be measured simultaneously — the uncertainty principle wearing a matrix mask.

**Pitfall — "adjoint" vs. "transpose."** Over $\mathbb{R}$ the adjoint is just the transpose $A^{\mathsf T}$; over $\mathbb{C}$ it is the *conjugate* transpose $A^*=\overline{A^{\mathsf T}}$. Forgetting the conjugate makes a true Hermitian matrix look non-symmetric and breaks the real-eigenvalue theorem. Always conjugate in the complex case.

<a id="s11"></a>
### The spectral theorem for Hermitian / normal operators

**What and why.** The **spectral theorem** is the crown jewel: every normal operator (in particular every Hermitian one) has an **orthonormal basis of eigenvectors**, and Hermitian operators have **real eigenvalues**. Physically: every observable can be measured in some orthonormal basis of definite-value states, with real measured values, and those states are mutually exclusive (orthogonal).

> **Theorem — Spectral Theorem (complex, finite-dimensional).** Let $T$ be an operator on a finite-dimensional complex inner product space. Then $T$ is **normal** iff there is an **orthonormal basis of eigenvectors** of $T$. If $T$ is **Hermitian**, all eigenvalues are **real**; if **unitary**, all eigenvalues have modulus $1$.

We build the proof from two lemmas.

> **Lemma A — real eigenvalues.** Every eigenvalue of a Hermitian $T$ is real.
**Proof.** Let $Tv=\lambda v$ with $v\ne0$. Then $\lambda\langle v,v\rangle=\langle Tv,v\rangle$, which is real (previous section), and $\langle v,v\rangle>0$ is real and positive, so $\lambda=\langle Tv,v\rangle/\langle v,v\rangle$ is real. $\blacksquare$

> **Lemma B — orthogonal eigenvectors for normal $T$.** For a normal operator, eigenvectors with distinct eigenvalues are orthogonal; moreover $Tv=\lambda v \iff T^*v=\overline\lambda v$.
**Proof.**
1. For normal $T$, $\|Tv\|^2=\langle Tv,Tv\rangle=\langle v,T^*Tv\rangle=\langle v,TT^*v\rangle=\langle T^*v,T^*v\rangle=\|T^*v\|^2$ for all $v$, using $T^*T=TT^*$. So $T$ and $T^*$ have the same "length effect." *(normality)*
2. Apply this to $T-\lambda I$, which is also normal (it commutes with its adjoint $T^*-\overline\lambda I$ — check directly). So $\|(T-\lambda I)v\|=\|(T^*-\overline\lambda I)v\|$, meaning $Tv=\lambda v\iff T^*v=\overline\lambda v$. *(apply step 1 to a shifted normal operator)*
3. Now let $Tv=\lambda v$, $Tw=\mu w$, $\lambda\ne\mu$. Then $\lambda\langle v,w\rangle=\langle Tv,w\rangle=\langle v,T^*w\rangle=\langle v,\overline\mu w\rangle=\mu\langle v,w\rangle$ (step 2 for $w$). So $(\lambda-\mu)\langle v,w\rangle=0$, and since $\lambda\ne\mu$, $\langle v,w\rangle=0$. $\blacksquare$

**Proof of the Spectral Theorem (the normal $\Rightarrow$ orthonormal eigenbasis direction, by induction on dimension).**
1. Over $\mathbb{C}$ the characteristic polynomial has a root, so $T$ has at least one eigenvalue $\lambda_1$ with unit eigenvector $e_1$. *(Fundamental Theorem of Algebra, §s7)*
2. Let $W=e_1^\perp=\{w:\langle w,e_1\rangle=0\}$, the orthogonal complement, of dimension $\dim V-1$. **Claim: $W$ is invariant under $T$** (i.e. $T$ maps $W$ into $W$). For $w\in W$: $\langle Tw,e_1\rangle=\langle w,T^*e_1\rangle=\langle w,\overline{\lambda_1}e_1\rangle=\lambda_1\langle w,e_1\rangle=0$, using Lemma B's fact $T^*e_1=\overline{\lambda_1}e_1$. So $Tw\in W$. *(invariance via the adjoint acting on $e_1$)*
3. The restriction $T|_W$ is again normal on the smaller space $W$ (it inherits commuting with its adjoint, which restricts to $(T^*)|_W$). By the induction hypothesis, $W$ has an orthonormal eigenbasis $e_2,\dots,e_n$ of $T$. *(induction on dimension; base case $\dim=1$ trivial)*
4. Then $e_1,e_2,\dots,e_n$ is an orthonormal eigenbasis of all of $V$ ($e_1\perp W$ by construction, and the rest are orthonormal within $W$). $\blacksquare$

**Converse.** If $T$ has an orthonormal eigenbasis, its matrix in that basis is diagonal $D$; then $T^*$ has matrix $\overline{D}$ (also diagonal), and diagonal matrices commute, so $T^*T=TT^*$ — $T$ is normal. Combined with Lemma A, a Hermitian operator additionally has real eigenvalues. $\blacksquare$

> **Spectral decomposition.** Equivalently, a Hermitian/normal $T$ can be written $T=\sum_k\lambda_k P_k$, where $P_k$ is the orthogonal projection onto the eigenspace $E_{\lambda_k}$. In Dirac notation (§s14), $T=\sum_k\lambda_k|e_k\rangle\langle e_k|$. This *is* the quantum measurement postulate: an observable is its eigenvalues weighted by projectors onto definite-value states.

**Worked example.** $A=\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}$ is real symmetric (Hermitian). Eigenpairs $(3,(1,1)),(1,(1,-1))$ — eigenvalues real, eigenvectors orthogonal. Normalizing: $e_1=\tfrac1{\sqrt2}(1,1),e_2=\tfrac1{\sqrt2}(1,-1)$. With orthogonal $Q=\tfrac1{\sqrt2}\begin{psmallmatrix}1&1\\1&-1\end{psmallmatrix}$, $Q^{*}AQ=\operatorname{diag}(3,1)$ and the spectral decomposition is $A=3\,e_1e_1^{*}+1\,e_2e_2^{*}$.

> **Why this is the deepest theorem in the guide.** Three separate miracles happen at once for a Hermitian operator: (1) eigenvalues are *real* (so they can be physical measured values); (2) eigenvectors can be chosen *orthonormal* (so distinct outcomes are mutually exclusive states); (3) they form a *complete basis* (so every state is a superposition of definite-value states). No special structure beyond $T=T^*$ is needed. The entire measurement framework of quantum mechanics is downstream of these three facts.

**Pitfall — diagonalizable is weaker than spectrally diagonalizable.** A general matrix with distinct eigenvalues is diagonalizable (§s8) but its eigenvectors need not be orthogonal, so the diagonalizing $P$ is invertible but not unitary. The spectral theorem's extra gift is that for normal operators $P$ can be taken *unitary* ($P^{-1}=P^*$), which is exactly what preserves the inner-product geometry — and hence probabilities.

> **Simultaneous diagonalization.** Two Hermitian operators $A,B$ can be diagonalized in the *same* orthonormal basis if and only if they **commute** ($AB=BA$). Physically, two observables are simultaneously measurable precisely when they commute; when they do not — like position and momentum, or two spin components — no common eigenbasis exists and the uncertainty principle results. The "only if" is quick (commuting diagonal matrices), and the "if" follows by restricting $B$ to each eigenspace of $A$ — which is legitimate because $B$ **preserves** each eigenspace: if $Av=\lambda v$ then $A(Bv)=B(Av)=\lambda(Bv)$ (using $AB=BA$), so $Bv\in E_\lambda(A)$, i.e. $B$ maps $E_\lambda(A)$ into itself — where it is again Hermitian and so diagonalizable.

## Part D — Extensions for physics: SVD, tensor products, Dirac notation

<a id="s12"></a>
### Positive-definite operators, quadratic forms, and the SVD

**What and why.** **Positive-definite** operators measure "energy-like" quantities that are always nonnegative; **quadratic forms** are the functions $\langle Tv,v\rangle$ they generate (kinetic energy, variance, potential wells). The **singular value decomposition (SVD)** extends the spectral theorem to *any* matrix, even non-square ones — the most-used factorization in applied mathematics.

> **Definition — positive (semi)definite.** A Hermitian operator $T$ is **positive-definite** if $\langle Tv,v\rangle>0$ for all $v\ne0$ (**positive-semidefinite** if $\ge0$). By the spectral theorem this is equivalent to **all eigenvalues being positive** (resp. nonnegative): writing $v$ in the eigenbasis, $\langle Tv,v\rangle=\sum_k\lambda_k|c_k|^2$, which is positive for all nonzero $v$ iff each $\lambda_k>0$.

> **Definition — quadratic form.** A **quadratic form** is $q(v)=\langle Av,v\rangle=\sum_{i,j}A_{ij}\,\overline{v_i}\,v_j$ for Hermitian $A$. The spectral theorem **diagonalizes** it: in the eigenbasis, $q=\sum_k\lambda_k|c_k|^2$ — a weighted sum of squares (the *principal axes*). This is why the spectral theorem classifies conic sections and stability of equilibria.

> **Theorem — Singular Value Decomposition.** Every $m\times n$ matrix $A$ (over $\mathbb{C}$) factors as $A=U\Sigma V^*$, where $U$ ($m\times m$) and $V$ ($n\times n$) are unitary and $\Sigma$ is $m\times n$ diagonal with real entries $\sigma_1\ge\dots\ge\sigma_r>0$ (the **singular values**) followed by zeros, $r=\operatorname{rank}A$.

**Proof (build it from the spectral theorem applied to $A^*A$).**
1. $A^*A$ is Hermitian ($(A^*A)^*=A^*A$) and positive-semidefinite ($\langle A^*Av,v\rangle=\langle Av,Av\rangle=\|Av\|^2\ge0$). By the spectral theorem it has an orthonormal eigenbasis $v_1,\dots,v_n$ with real eigenvalues $\lambda_i\ge0$. Order them so $\lambda_1\ge\dots\ge\lambda_n\ge0$; let $r$ be the number of positive ones and set $\sigma_i=\sqrt{\lambda_i}$. *(spectral theorem on $A^*A$; eigenvalues nonnegative)*
2. For $i\le r$ define $u_i=\dfrac{1}{\sigma_i}Av_i$. These are orthonormal: $\langle u_i,u_j\rangle=\dfrac{1}{\sigma_i\sigma_j}\langle Av_i,Av_j\rangle=\dfrac{1}{\sigma_i\sigma_j}\langle A^*Av_i,v_j\rangle=\dfrac{\lambda_i}{\sigma_i\sigma_j}\langle v_i,v_j\rangle=\delta_{ij}$. *(definition of $u_i$; $A^*Av_i=\lambda_i v_i$; orthonormality of the $v$'s)*
3. Extend $u_1,\dots,u_r$ to an orthonormal basis $u_1,\dots,u_m$ of $\mathbb{C}^m$ (Gram–Schmidt, §s9). Let $V=[v_1\cdots v_n]$, $U=[u_1\cdots u_m]$ (both unitary, orthonormal columns), and $\Sigma$ diagonal with the $\sigma_i$. *(basis extension; assemble matrices)*
4. Verify $AV=U\Sigma$: for $i\le r$, $Av_i=\sigma_i u_i$ (by definition of $u_i$); for $i>r$, $\lambda_i=0$ so $\|Av_i\|^2=\langle A^*Av_i,v_i\rangle=0$, hence $Av_i=0$, matching the zero columns of $\Sigma$. Thus $AV=U\Sigma$, and right-multiplying by $V^*=V^{-1}$ gives $A=U\Sigma V^*$. $\blacksquare$

The singular values are the semi-axis lengths of the ellipsoid that $A$ maps the unit sphere onto: $A$ rotates ($V^*$), stretches along axes ($\Sigma$), and rotates again ($U$). $\sigma_1$ is the maximum stretch ($=\|A\|$, the operator norm).

**Worked example.** $A=\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}$. Then $A^*A=\begin{psmallmatrix}1&1\\1&2\end{psmallmatrix}$, eigenvalues $\tfrac{3\pm\sqrt5}{2}$, so singular values $\sigma_{1,2}=\sqrt{\tfrac{3\pm\sqrt5}{2}}\approx1.618,\,0.618$ (golden ratio and its reciprocal). Their product $\sigma_1\sigma_2=\sqrt{\det(A^*A)}=\sqrt{\det A^*\det A}=|\det A|=1$, consistent with $A$ preserving area.

> **Completing the square — diagonalizing a quadratic form by hand.** Consider $q(x,y)=2x^2+2xy+2y^2$, the form of the matrix $A=\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}$. Its eigenvalues $3,1$ are both positive, so $A$ is positive-definite and $q>0$ for $(x,y)\ne(0,0)$ — the level set $q=1$ is an ellipse. In the eigenbasis (rotate by $45^\circ$) the form becomes $3u^2+1v^2$, a sum of squares with the eigenvalues as coefficients. The principal axes of the ellipse point along the eigenvectors, and their lengths scale as $1/\sqrt{\lambda_k}$. This is how the spectral theorem classifies conics and identifies stable vs. unstable equilibria in mechanics (positive-definite Hessian $=$ a minimum).

**Pitfall — singular values are not eigenvalues.** For a non-normal matrix the singular values $\sigma_i$ (always real and nonnegative, defined for *any* matrix, even rectangular) differ from the eigenvalues. They agree in magnitude only when the matrix is normal. The SVD's universality — it works for every matrix — is exactly why it dominates data analysis (principal component analysis, low-rank approximation, pseudo-inverses) where matrices are rarely square or normal.

> **Application — the operator norm and best low-rank approximation.** The largest singular value $\sigma_1=\|A\|$ is the maximum factor by which $A$ can stretch any unit vector. Keeping only the largest $k$ singular values in $U\Sigma V^*$ gives the best rank-$k$ approximation of $A$ in this norm (the Eckart–Young theorem) — the mathematical core of image compression and dimensionality reduction.

<a id="s13"></a>
### Direct sums and tensor products (composite quantum systems)

**What and why.** To combine two systems you need a way to combine their spaces. The **direct sum** stacks spaces side by side (independent degrees of freedom); the **tensor product** is the genuinely quantum combination, where the dimensions *multiply* and entanglement lives.

> **Definition — direct sum.** The **direct sum** $V\oplus W$ is the set of pairs $(v,w)$ with $v\in V,w\in W$, added and scaled componentwise: $(v_1,w_1)+(v_2,w_2)=(v_1+v_2,w_1+w_2)$, $\lambda(v,w)=(\lambda v,\lambda w)$. If $(e_i)$ is a basis of $V$ and $(f_j)$ of $W$, then $(e_i,0)$ and $(0,f_j)$ together form a basis, so $\dim(V\oplus W)=\dim V+\dim W$. **Dimensions add.**

> **Definition — tensor product.** The **tensor product** $V\otimes W$ is the vector space spanned by symbols $v\otimes w$ (called **simple** or **product** tensors), subject to **bilinearity**:
>
> $$
> (\lambda v_1+v_2)\otimes w=\lambda(v_1\otimes w)+v_2\otimes w,\qquad v\otimes(\lambda w_1+w_2)=\lambda(v\otimes w_1)+v\otimes w_2.
> $$
> A basis is $\{e_i\otimes f_j\}$ over all $i,j$, so $\dim(V\otimes W)=\dim V\cdot\dim W$. **Dimensions multiply.**

> **Universal property.** The map $(v,w)\mapsto v\otimes w$ is bilinear, and it is the *most general* such: every bilinear map $V\times W\to Z$ factors **uniquely** through a linear map $V\otimes W\to Z$ (i.e. equals that linear map composed with $\otimes$). This is the defining feature of the tensor product and is what the independence proof below exploits.

> **Proposition — the tensor basis is a basis.** If $(e_i)_{i=1}^m$ and $(f_j)_{j=1}^n$ are bases, the $mn$ products $e_i\otimes f_j$ are independent and span $V\otimes W$.
**Proof (sketch with the defining universal property).**
1. *(Spanning.)* By bilinearity, any $v\otimes w=\big(\sum_i a_i e_i\big)\otimes\big(\sum_j b_j f_j\big)=\sum_{i,j}a_i b_j\,(e_i\otimes f_j)$, and general elements are sums of such, hence in the span of $\{e_i\otimes f_j\}$. *(expand by bilinearity)*
2. *(Independence.)* For each pair $(p,q)$ the bilinear map $(v,w)\mapsto v_p^*\,w_q^*$ (the $p$-th coordinate of $v$ times the $q$-th of $w$, using coordinate functionals) factors through $V\otimes W$ and sends $e_i\otimes f_j\mapsto\delta_{ip}\delta_{jq}$. A dependence $\sum c_{ij}e_i\otimes f_j=0$ evaluated by this map yields $c_{pq}=0$ for every $(p,q)$. *(coordinate functionals separate the basis tensors)* $\blacksquare$

**Physics — entanglement.** Two qubits live in $\mathbb{C}^2\otimes\mathbb{C}^2\cong\mathbb{C}^4$, with basis $|00\rangle,|01\rangle,|10\rangle,|11\rangle$ (shorthand for $e_i\otimes f_j$). A state is **separable** if it is a single product $|\psi\rangle\otimes|\phi\rangle$ and **entangled** otherwise. The Bell state $\tfrac1{\sqrt2}(|00\rangle+|11\rangle)$ is entangled.

**Worked example — proof that the Bell state is entangled.** Suppose $\tfrac1{\sqrt2}(|00\rangle+|11\rangle)=(a|0\rangle+b|1\rangle)\otimes(c|0\rangle+d|1\rangle)=ac|00\rangle+ad|01\rangle+bc|10\rangle+bd|11\rangle$. Matching coefficients: $ac=\tfrac1{\sqrt2}$, $bd=\tfrac1{\sqrt2}$ (both nonzero, so $a,b,c,d\ne0$), yet $ad=0$ and $bc=0$. The latter force one of $a,d$ and one of $b,c$ to vanish — contradicting that all four are nonzero. So no product factorization exists: the state is entangled. This impossibility is a pure linear-algebra fact.

<a id="s14"></a>
### Dirac bra–ket notation, recast as linear algebra

**What and why.** Physicists write quantum linear algebra in **bra–ket** notation. It is not new mathematics — it is exactly the inner-product space machinery of this guide, with suggestive symbols. Translating it back to §s9–s11 is the bridge to quantum mechanics.

> **The dictionary.**
> - A **ket** $|\psi\rangle$ is a vector in a complex inner product space $V$ (a state).
> - A **bra** $\langle\psi|$ is the linear functional $v\mapsto\langle v,\psi\rangle$ — an element of the **dual space** $V^*$. The map $|\psi\rangle\mapsto\langle\psi|$ is the conjugate-linear correspondence between $V$ and $V^*$ guaranteed by the inner product (Riesz representation).
> - The **bracket** $\langle\phi|\psi\rangle$ is the inner product $\langle\psi,\phi\rangle$ (a complex number, a **probability amplitude**). Note the conjugate-linearity: $\langle\phi|$ paired with $|\psi\rangle$.
> - The **outer product** $|\phi\rangle\langle\psi|$ is the operator $v\mapsto\langle v,\psi\rangle\,\phi=\langle\psi|v\rangle\,|\phi\rangle$ — rank-one, the building block of operators.

> **Completeness / resolution of the identity.** For an orthonormal basis $\{|e_k\rangle\}$,
>
> $$
> \sum_k|e_k\rangle\langle e_k|=I.
> $$
**Proof.** Apply the left side to any $v$: $\sum_k|e_k\rangle\langle e_k|v\rangle=\sum_k\langle v,e_k\rangle e_k$, which is the expansion of $v$ in the orthonormal basis (§s9), equal to $v$. Since this holds for all $v$, the operator is $I$. $\blacksquare$ This identity is the workhorse of every quantum computation — you "insert $\sum|e_k\rangle\langle e_k|$" to change basis.

> **Observables and measurement, as the spectral theorem.** An **observable** is a Hermitian operator $A=A^*$. By the spectral theorem (§s11) it has real eigenvalues $\{a_k\}$ (the possible measured values) and an orthonormal eigenbasis $\{|a_k\rangle\}$, giving the **spectral decomposition**
>
> $$
> A=\sum_k a_k\,|a_k\rangle\langle a_k|.
> $$
> For a normalized state $|\psi\rangle$ ($\langle\psi|\psi\rangle=1$), the **Born rule** says measuring $A$ yields value $a_k$ with probability $|\langle a_k|\psi\rangle|^2$. These probabilities sum to $1$ precisely because of completeness: $\sum_k|\langle a_k|\psi\rangle|^2=\langle\psi|\big(\sum_k|a_k\rangle\langle a_k|\big)|\psi\rangle=\langle\psi|\psi\rangle=1$.

> **Time evolution, as unitarity.** Schrödinger evolution sends $|\psi(0)\rangle\mapsto|\psi(t)\rangle=U(t)|\psi(0)\rangle$ with $U(t)=e^{-iHt/\hbar}$ **unitary** (because $H$ is Hermitian, $U^*=e^{+iHt/\hbar}=U^{-1}$). Unitarity preserves inner products (§s10), hence preserves total probability $\langle\psi|\psi\rangle=1$. Conservation of probability is exactly the inner-product-preservation theorem.

**Worked example — spin measurement.** Take spin along $z$ for a qubit: $S_z=\tfrac{\hbar}{2}\begin{psmallmatrix}1&0\\0&-1\end{psmallmatrix}$, Hermitian with eigenpairs $(+\tfrac\hbar2,|0\rangle)$ and $(-\tfrac\hbar2,|1\rangle)$. For the state $|\psi\rangle=\tfrac1{\sqrt2}(|0\rangle+|1\rangle)$, the Born rule gives probability $|\langle0|\psi\rangle|^2=\tfrac12$ for outcome $+\tfrac\hbar2$ and $\tfrac12$ for $-\tfrac\hbar2$. Every symbol here is an object from this guide: a Hermitian matrix, its real eigenvalues, its orthonormal eigenbasis, and inner products giving probabilities.

---

*This guide built linear algebra from the eight vector-space axioms up to the spectral theorem, the SVD, and tensor products, and then read the whole structure back as the language of quantum mechanics: states are vectors, observables are Hermitian operators, measured values are real eigenvalues, definite-value states are an orthonormal eigenbasis, and time evolution is unitary. Return to any boxed definition or numbered proof as a reference — and remember that superposition is just vector addition, and that is why this one subject runs through all of physics.*
