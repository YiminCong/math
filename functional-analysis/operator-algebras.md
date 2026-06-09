**English** · [中文](operator-algebras.zh.md)

# Operator Algebras & Algebraic QFT, *quantum theory as algebra.*

*A rigorous first course in operator algebras built around a single change of viewpoint: instead of fixing a Hilbert space and reading observables off it, we take the **algebra of observables** as the primary object and let Hilbert spaces appear as representations. We climb from Banach algebras and the C\*-identity, through the Gelfand theory that turns commutative C\*-algebras into spaces, the GNS construction that rebuilds a Hilbert space from a state, von Neumann algebras and the double commutant theorem, the Murray–von Neumann classification of factors, modular theory, and finally to the canonical commutation relations and the Haag–Kastler axioms of algebraic quantum field theory. Every term is defined the first time it appears, and every theorem is proved or proved in its key steps with each step's justification named.*

[← Back to all guides](../README.md)

> **How to read this guide.** We assume the **Functional Analysis & Hilbert Spaces** guide (Banach spaces, Hilbert spaces, bounded operators, adjoints, the spectrum of a bounded operator, the spectral theorem). When we use a fact from it we restate it in one line. Everything specific to operator algebras — *Banach algebra*, *C\*-algebra*, *spectrum in an algebra*, *Gelfand transform*, *state*, *GNS representation*, *von Neumann algebra*, *factor*, *trace*, *modular automorphism*, *CCR/CAR*, *net of local observables* — is defined where it first appears, with a worked numerical example. Nothing is "left to the reader." Where the physics illuminates the mathematics we point it out, but this is a **math** guide: claims are proved.

---

## Part A — Algebras of observables

<a id="s0"></a>
### Why algebras: observables before states

In ordinary quantum mechanics one fixes a Hilbert space $\mathcal H$ — for a single particle, $L^2(\mathbb R)$ — and declares that **states** are unit vectors $\psi\in\mathcal H$ (up to phase) and **observables** are self-adjoint operators on $\mathcal H$. This is the *Hilbert-space-first* picture, and it works beautifully for one particle.

But it has a hidden assumption: that there is one God-given Hilbert space, the same for everyone. In quantum statistical mechanics (infinitely many particles, thermal equilibrium) and in quantum field theory (infinitely many degrees of freedom, one per point of space), this assumption fails. There are inequivalent ways to represent the same physical observables on Hilbert spaces — *inequivalent representations* — and choosing one prematurely throws away physics. **Haag's theorem**, which we reach in s11, says bluntly that the interaction picture of field theory cannot live on the free-field Hilbert space at all.

The **algebraic approach to quantum theory**, due to von Neumann, Segal, Haag, and Kastler, repairs this by reversing the order of construction. We take as primary the collection of observables together with the operations we can perform on them:

- we can add two observables and scale them (linear structure);
- we can multiply them (an algebra — composition of operations, or products of measurements made compatible);
- we can form the adjoint $A^*$ (the abstract version of "complex conjugate transpose," encoding that a real measurement is self-adjoint, $A=A^*$);
- and we have a norm $\|A\|$ measuring the largest possible value the observable can take.

The structure that packages all four — and exactly the right compatibility between them, the **C\*-identity** $\|A^*A\|=\|A\|^2$ — is a **C\*-algebra**. The slogan of the whole guide is:

> A quantum system is a C\*-algebra $\mathcal A$ of observables. A **state** is not a vector but a normalized positive linear functional $\omega:\mathcal A\to\mathbb C$ assigning to each observable its expectation value $\omega(A)=\langle A\rangle$. Hilbert spaces are *derived*: each state $\omega$ builds its own representation by the **GNS construction**.

This is not merely a generalization; it is a reorganization that makes the right things primary. Expectation values $\langle A\rangle$ are what experiments measure, so a state-as-functional is closer to the physics than a state-as-vector. And because many inequivalent Hilbert-space representations can carry the same algebra, the algebra is the invariant, observer-independent object.

> **The physical hook.** In the Hilbert-space picture you ask "what is the wavefunction?" In the algebraic picture you ask "what is the expectation value of each observable?" — and the wavefunction, when one exists, is reconstructed from those numbers. The latter question always has an answer; the former sometimes does not.

The plan: define Banach algebras and C\*-algebras (s1), understand the spectrum inside an abstract algebra (s2), prove that commutative C\*-algebras are *exactly* algebras of functions on a space (s3, Gelfand), build the Hilbert space from a state (s4, GNS), study representations (s5), then enrich to von Neumann algebras (s6), classify them (s7), add traces and modular theory (s8), realize the canonical commutation relations algebraically (s9), and assemble the axioms of algebraic QFT (s10–s11).

<a id="s1"></a>
### Banach algebras and C\*-algebras

**What and why.** We want a set whose elements can be added, scaled, multiplied, and measured in size, with everything fitting together continuously so that limits behave. That is a Banach algebra. Adding an adjoint and one identity that links the adjoint to the norm gives a C\*-algebra — the abstract distillation of "operators on a Hilbert space."

We recall from the Functional Analysis guide: a **normed vector space** is a vector space $V$ over $\mathbb C$ with a function $\|\cdot\|:V\to[0,\infty)$ satisfying $\|v\|=0\iff v=0$, $\|\lambda v\|=|\lambda|\,\|v\|$, and the triangle inequality $\|v+w\|\le\|v\|+\|w\|$; it is a **Banach space** if it is complete (every Cauchy sequence converges).

> **Definition — algebra.** An (associative, unital, complex) **algebra** is a complex vector space $\mathcal A$ together with a multiplication $\mathcal A\times\mathcal A\to\mathcal A$, written $(a,b)\mapsto ab$, that is associative ($(ab)c=a(bc)$), bilinear (linear in each argument), and has a **unit** $1\in\mathcal A$ with $1a=a1=a$ for all $a$. The algebra is **commutative** if $ab=ba$ for all $a,b$.

> **Definition — Banach algebra.** A **Banach algebra** is an algebra $\mathcal A$ that is also a Banach space, whose norm is **submultiplicative**:
> $$
> \|ab\|\le\|a\|\,\|b\|\qquad\text{for all }a,b\in\mathcal A,
> $$
> and (for the unital case we use throughout) $\|1\|=1$.

Submultiplicativity is exactly what makes multiplication continuous: if $a_n\to a$ and $b_n\to b$ then $a_nb_n\to ab$, because $\|a_nb_n-ab\|\le\|a_n\|\,\|b_n-b\|+\|a_n-a\|\,\|b\|\to0$ (triangle inequality, submultiplicativity, and boundedness of the convergent sequence $\|a_n\|$).

> **Definition — involution and \*-algebra.** An **involution** on an algebra $\mathcal A$ is a map $a\mapsto a^*$ that is conjugate-linear ($(\lambda a+b)^*=\overline\lambda\,a^*+b^*$), reverses products ($(ab)^*=b^*a^*$), and is its own inverse ($(a^*)^*=a$). An algebra with an involution is a **\*-algebra**. The element $a^*$ is the **adjoint** of $a$. An element is **self-adjoint** if $a=a^*$, **normal** if $a^*a=aa^*$, and (in a unital algebra) **unitary** if $a^*a=aa^*=1$.

> **Definition — C\*-algebra.** A **C\*-algebra** is a Banach \*-algebra $\mathcal A$ in which the norm satisfies the **C\*-identity**:
> $$
> \|a^*a\|=\|a\|^2\qquad\text{for all }a\in\mathcal A.
> $$

The C\*-identity looks innocent but is extraordinarily rigid: it pins down the norm uniquely from the algebraic structure (we will see in s2 that the norm equals a spectral radius), so a C\*-algebra has *at most one* C\*-norm. This is why the abstract algebra, not any particular norm chosen by hand, is the invariant object.

A first consequence we will use constantly: the involution is **isometric**. Indeed, by the C\*-identity and submultiplicativity,
$$
\|a\|^2=\|a^*a\|\le\|a^*\|\,\|a\|,
$$
so dividing by $\|a\|$ (for $a\ne0$) gives $\|a\|\le\|a^*\|$. Replacing $a$ by $a^*$ and using $(a^*)^*=a$ gives $\|a^*\|\le\|a\|$. Hence $\|a^*\|=\|a\|$. *(C\*-identity; submultiplicativity; involution is an involution.)*

> **Definition — examples to keep in mind.**
> 1. **Matrices** $M_n(\mathbb C)$, the $n\times n$ complex matrices, with matrix multiplication, adjoint $a^*=\overline{a}^{\,\mathsf T}$ (conjugate transpose), and operator norm $\|a\|=\sup_{\|x\|=1}\|ax\|$. This is a noncommutative C\*-algebra (for $n\ge2$).
> 2. **Continuous functions** $C(X)$ on a compact Hausdorff space $X$, with pointwise operations, involution $f^*=\overline f$ (complex conjugate), and supremum norm $\|f\|=\sup_{x\in X}|f(x)|$. This is a *commutative* C\*-algebra. (A space $X$ is **compact Hausdorff** if every open cover has a finite subcover and distinct points have disjoint neighborhoods.)
> 3. **Bounded operators** $B(\mathcal H)$ on a Hilbert space $\mathcal H$, with composition, Hilbert-space adjoint, and operator norm. This is the mother of all C\*-algebras.

**Verifying the C\*-identity for $M_n(\mathbb C)$ — worked example.** Take $n=1$ first, trivially: a $1\times1$ matrix is a number $z$, $z^*=\overline z$, $\|z\|=|z|$, and $\|z^*z\|=|\,\overline z z\,|=|z|^2=\|z\|^2$. For general $n$, let $a\in M_n(\mathbb C)$. The operator norm satisfies $\|a\|^2=\sup_{\|x\|=1}\|ax\|^2=\sup_{\|x\|=1}\langle ax,ax\rangle=\sup_{\|x\|=1}\langle a^*ax,x\rangle$ (definition of adjoint). The matrix $a^*a$ is self-adjoint and positive, so by the finite-dimensional spectral theorem it has an orthonormal eigenbasis with nonnegative eigenvalues; the supremum of $\langle a^*ax,x\rangle$ over unit $x$ is its largest eigenvalue $\lambda_{\max}$. But $\lambda_{\max}$ is also $\|a^*a\|$, the operator norm of the self-adjoint operator $a^*a$ (its norm equals its spectral radius, the largest $|\lambda|$). Hence $\|a\|^2=\lambda_{\max}=\|a^*a\|$. *(Definition of operator norm; definition of adjoint; spectral theorem for the positive self-adjoint matrix $a^*a$.)*

**Pitfall.** Submultiplicativity $\|ab\|\le\|a\|\|b\|$ is generally *strict*: with $a=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}$ one has $a^2=0$ so $\|a^2\|=0<\|a\|^2$. The C\*-identity is special precisely because it forces *equality* on the combination $a^*a$.

<a id="s2"></a>
### The spectrum, spectral radius, and Gelfand–Mazur

**What and why.** In a single matrix, eigenvalues are the numbers $\lambda$ for which $a-\lambda 1$ fails to be invertible. The same definition works in any Banach algebra, with no reference to vectors or eigenvectors — it is purely about invertibility. This "spectrum in an algebra" is the bridge from algebra to numbers and underlies everything that follows.

> **Definition — invertible, spectrum, resolvent.** Let $\mathcal A$ be a unital Banach algebra and $a\in\mathcal A$. We call $a$ **invertible** if there is $b\in\mathcal A$ with $ab=ba=1$. The **spectrum** of $a$ is
> $$
> \sigma(a)=\{\lambda\in\mathbb C:\ a-\lambda 1\ \text{is not invertible in }\mathcal A\}.
> $$
> Its complement $\rho(a)=\mathbb C\setminus\sigma(a)$ is the **resolvent set**, and for $\lambda\in\rho(a)$ the element $(a-\lambda1)^{-1}$ is the **resolvent**.

> **Lemma — Neumann series (invertibility near 1).** If $\|x\|<1$ then $1-x$ is invertible, with $(1-x)^{-1}=\sum_{k=0}^\infty x^k$.

**Proof.**
1. The partial sums $s_n=\sum_{k=0}^n x^k$ form a Cauchy sequence: for $m>n$, $\|s_m-s_n\|\le\sum_{k=n+1}^m\|x\|^k\le\sum_{k=n+1}^\infty\|x\|^k=\dfrac{\|x\|^{n+1}}{1-\|x\|}\to0$. *(triangle inequality; submultiplicativity gives $\|x^k\|\le\|x\|^k$; geometric series, valid as $\|x\|<1$.)*
2. Since $\mathcal A$ is complete, $s_n\to s:=\sum_{k\ge0}x^k$ exists. *(Banach space completeness.)*
3. Compute $(1-x)s_n=s_n(1-x)=1-x^{n+1}$ by telescoping. Let $n\to\infty$: $\|x^{n+1}\|\le\|x\|^{n+1}\to0$, and multiplication is continuous, so $(1-x)s=s(1-x)=1$. *(telescoping; continuity of multiplication.)*
4. Thus $s$ is a two-sided inverse of $1-x$. $\blacksquare$

> **Theorem — the spectrum is nonempty, compact, and bounded by the norm.** For any $a$ in a unital Banach algebra, $\sigma(a)$ is a nonempty compact subset of $\mathbb C$ contained in the disk $\{|\lambda|\le\|a\|\}$.

**Proof (key steps).**
1. *Boundedness.* If $|\lambda|>\|a\|$ then $a-\lambda1=-\lambda(1-\lambda^{-1}a)$ and $\|\lambda^{-1}a\|=\|a\|/|\lambda|<1$, so $1-\lambda^{-1}a$ is invertible by the Neumann series; hence $a-\lambda1$ is invertible and $\lambda\notin\sigma(a)$. So $\sigma(a)\subseteq\{|\lambda|\le\|a\|\}$. *(Neumann lemma.)*
2. *Closedness.* The set of invertible elements is open (if $b$ is invertible and $\|c-b\|<1/\|b^{-1}\|$ then $c=b(1-b^{-1}(b-c))$ is invertible by the Neumann series), and $\lambda\mapsto a-\lambda1$ is continuous, so $\rho(a)$ is open and $\sigma(a)$ is closed. Closed and bounded in $\mathbb C$ means compact. *(openness of invertibles; preimage of open set under continuous map is open.)*
3. *Nonemptiness.* The resolvent $R(\lambda)=(a-\lambda1)^{-1}$ is an analytic $\mathcal A$-valued function on $\rho(a)$ (its derivative is $R(\lambda)^2$, from the resolvent identity). If $\sigma(a)$ were empty, $R$ would be entire, and for $|\lambda|\to\infty$, $\|R(\lambda)\|\to0$: from $R(\lambda)=-\lambda^{-1}(1-\lambda^{-1}a)^{-1}$ the Neumann series gives $\|R(\lambda)\|\le|\lambda|^{-1}/(1-\|a\|/|\lambda|)\to0$. By a Banach-space valued **Liouville theorem** (apply any bounded linear functional $\phi$: $\phi(R(\lambda))$ is a bounded entire scalar function, hence constant; as it vanishes at infinity it is $0$; true for all $\phi$, so $R\equiv0$ by Hahn–Banach), $R\equiv0$ — impossible since $R(\lambda)$ is invertible. Contradiction. $\blacksquare$

> **Definition — spectral radius.** The **spectral radius** of $a$ is $r(a)=\sup\{|\lambda|:\lambda\in\sigma(a)\}$ (well-defined since $\sigma(a)$ is nonempty and bounded).

> **Theorem — Gelfand's spectral radius formula.** $\displaystyle r(a)=\lim_{n\to\infty}\|a^n\|^{1/n}=\inf_{n\ge1}\|a^n\|^{1/n}.$

The proof uses that $R(\lambda)$ has a Laurent expansion $\sum_{n\ge0}\lambda^{-n-1}a^n$ convergent for $|\lambda|>r(a)$, whose radius of convergence is governed by $\limsup\|a^n\|^{1/n}$; matching radii gives the formula. We state it; the consequence we need is below.

> **Corollary — the C\*-norm is a spectral radius.** In a C\*-algebra, for self-adjoint $a$, $\|a\|=r(a)$.

**Proof.**
1. For self-adjoint $a$, the C\*-identity gives $\|a^2\|=\|a^*a\|=\|a\|^2$. *(C\*-identity with $a^*=a$.)*
2. Iterating, $\|a^{2^k}\|=\|a\|^{2^k}$ by induction: assuming $\|a^{2^k}\|=\|a\|^{2^k}$, note $a^{2^k}$ is self-adjoint, so $\|a^{2^{k+1}}\|=\|(a^{2^k})^2\|=\|a^{2^k}\|^2=\|a\|^{2^{k+1}}$. *(step 1 applied to the self-adjoint $a^{2^k}$.)*
3. Then $\|a^{2^k}\|^{1/2^k}=\|a\|$ for all $k$, so the limit in the spectral radius formula equals $\|a\|$: $r(a)=\|a\|$. *(spectral radius formula along the subsequence $n=2^k$.)* $\blacksquare$

This is the promised rigidity: the norm of a self-adjoint element is determined by the spectrum, hence by the algebra. Since $\|a\|^2=\|a^*a\|=r(a^*a)$ for *every* $a$ (because $a^*a$ is self-adjoint), the entire norm is algebraically determined.

> **Theorem — Gelfand–Mazur.** A unital Banach algebra in which every nonzero element is invertible (a **division algebra**) is isometrically isomorphic to $\mathbb C$.

**Proof.**
1. Take any $a\in\mathcal A$. By the nonemptiness theorem, $\sigma(a)\ne\emptyset$; pick $\lambda\in\sigma(a)$. *(spectrum nonempty.)*
2. Then $a-\lambda1$ is not invertible. By hypothesis the only non-invertible element is $0$, so $a-\lambda1=0$, i.e. $a=\lambda1$. *(division algebra hypothesis.)*
3. Thus every element is a scalar multiple of $1$; the map $\lambda1\mapsto\lambda$ is an isometric algebra isomorphism onto $\mathbb C$. $\blacksquare$

**Worked example.** In $M_2(\mathbb C)$ take $a=\begin{psmallmatrix}2&0\\0&3\end{psmallmatrix}$. Then $a-\lambda1$ is non-invertible exactly when $\det\begin{psmallmatrix}2-\lambda&0\\0&3-\lambda\end{psmallmatrix}=(2-\lambda)(3-\lambda)=0$, so $\sigma(a)=\{2,3\}$, $r(a)=3=\|a\|$ (consistent with the corollary, since $a$ is self-adjoint), confirming spectrum-in-an-algebra reproduces ordinary eigenvalues.

**Worked example — spectral radius can be smaller than the norm.** Take the nilpotent $a=\begin{psmallmatrix}0&5\\0&0\end{psmallmatrix}$. Then $a^2=0$, so by the radius formula $r(a)=\lim\|a^n\|^{1/n}=0$: the spectrum is $\sigma(a)=\{0\}$. Yet $\|a\|=5\ne0$. This does *not* contradict the s2 corollary because $a$ is **not** self-adjoint ($a^*=\begin{psmallmatrix}0&0\\5&0\end{psmallmatrix}\ne a$); the equality $\|a\|=r(a)$ is a privilege of normal elements. The lesson, important throughout: for a general element the norm sees more than the spectrum, and only the C\*-identity (acting on the *self-adjoint* combination $a^*a$, for which $r(a^*a)=\|a^*a\|=\|a\|^2=25$) recovers the norm.

**Pitfall — the spectrum depends on the ambient algebra (or does it?).** A priori $\sigma(a)$ could shrink if we enlarge the algebra (more elements available to be an inverse). For Banach algebras the spectrum can indeed change under embedding. A pleasant theorem special to C\*-algebras is **spectral permanence**: if $\mathcal B\subseteq\mathcal A$ is a C\*-subalgebra containing the unit, then $\sigma_{\mathcal B}(a)=\sigma_{\mathcal A}(a)$ for every $a\in\mathcal B$. The spectrum is intrinsic — it does not matter which C\*-algebra we compute it in. This is what lets us speak of "the spectrum of an observable" without naming a representation.

<a id="s3"></a>
### Commutative C\*-algebras and the Gelfand transform

**What and why.** The example $C(X)$ — continuous functions on a compact Hausdorff space — is commutative. Gelfand's great theorem says the converse: *every* commutative unital C\*-algebra is $C(X)$ for some compact Hausdorff $X$, and $X$ is recovered as the space of "evaluation maps." This is a perfect dictionary between algebra and geometry, and it is the abstract engine behind the spectral theorem.

> **Definition — character.** A **character** (or multiplicative linear functional) of a commutative unital Banach algebra $\mathcal A$ is a nonzero algebra homomorphism $\chi:\mathcal A\to\mathbb C$: it is linear, $\chi(ab)=\chi(a)\chi(b)$, and $\chi(1)=1$. The set of all characters is the **spectrum** (or **maximal ideal space**) $\widehat{\mathcal A}$, also called the **Gelfand spectrum**.

> **Lemma — characters are automatically bounded, with $\|\chi\|=1$, and $\chi(a)\in\sigma(a)$.**

**Proof.**
1. For $a$ with $\|a\|<1$, $1-a$ is invertible (Neumann series), and a homomorphism sends invertibles to invertibles (nonzero scalars), so $\chi(1-a)=1-\chi(a)\ne0$; this rules out $|\chi(a)|\ge1$ when $\|a\|<1$. Scaling, $|\chi(a)|\le\|a\|$, so $\chi$ is bounded with $\|\chi\|\le1$; and $\chi(1)=1$ gives $\|\chi\|=1$. *(Neumann; homomorphisms preserve invertibility.)*
2. The element $a-\chi(a)1$ satisfies $\chi(a-\chi(a)1)=0$, so it lies in the kernel of $\chi$, a proper ideal, hence is non-invertible; thus $\chi(a)\in\sigma(a)$. *(kernel of a character is a maximal ideal, which contains no invertibles.)* $\blacksquare$

> **Definition — weak\* topology and the Gelfand transform.** Equip $\widehat{\mathcal A}$ with the **weak\* topology**: the weakest topology making every evaluation $\chi\mapsto\chi(a)$ continuous. The **Gelfand transform** sends $a\in\mathcal A$ to the function $\widehat a:\widehat{\mathcal A}\to\mathbb C$, $\widehat a(\chi)=\chi(a)$.

By the lemma, $\widehat{\mathcal A}$ sits inside the closed unit ball of the dual $\mathcal A^*$, which is **weak\*-compact** by the **Banach–Alaoglu theorem** (a fact from the Functional Analysis guide: the closed unit ball of a dual space is weak\*-compact). One checks $\widehat{\mathcal A}$ is weak\*-closed, hence compact Hausdorff. So $\widehat a\in C(\widehat{\mathcal A})$ always.

> **Theorem — Gelfand–Naimark (commutative case).** Let $\mathcal A$ be a commutative unital C\*-algebra. The Gelfand transform $a\mapsto\widehat a$ is an isometric \*-isomorphism
> $$
> \mathcal A\ \xrightarrow{\ \cong\ }\ C(\widehat{\mathcal A}).
> $$
> That is: it is linear, multiplicative, sends $a^*$ to $\overline{\widehat a}$, preserves the norm, and is a bijection onto all of $C(\widehat{\mathcal A})$.

**Proof (key steps).**
1. *Homomorphism.* $\widehat{ab}(\chi)=\chi(ab)=\chi(a)\chi(b)=\widehat a(\chi)\widehat b(\chi)$ and linearity is immediate; so $a\mapsto\widehat a$ is an algebra homomorphism. *(definition of character.)*
2. *Range of $\widehat a$ is the spectrum.* In the commutative case, $\lambda\in\sigma(a)$ iff $\lambda=\chi(a)$ for some character $\chi$ (every maximal ideal is the kernel of a unique character). Hence $\widehat a(\widehat{\mathcal A})=\sigma(a)$. *(correspondence of characters and maximal ideals, special to commutative Banach algebras.)*
3. *Isometry.* For self-adjoint $a$, $\|\widehat a\|_\infty=\sup_\chi|\chi(a)|=\sup\{|\lambda|:\lambda\in\sigma(a)\}=r(a)=\|a\|$ by the s2 corollary. For general $a$, $\|\widehat a\|_\infty^2=\|\,\overline{\widehat a}\,\widehat a\,\|_\infty=\|\widehat{a^*a}\|_\infty=\|a^*a\|=\|a\|^2$ using the self-adjoint case on $a^*a$ and the C\*-identity. So the map is isometric, hence injective. *(s2 corollary; C\*-identity.)*
4. *\*-preserving.* For self-adjoint $a$, $\sigma(a)\subseteq\mathbb R$ (the spectrum of a self-adjoint element is real — proved in s4 via states, or directly via $\|e^{ita}\|=1$), so $\widehat a$ is real-valued, and one deduces $\widehat{a^*}=\overline{\widehat a}$ on general elements by splitting into real and imaginary parts $a=\frac{a+a^*}2+i\frac{a-a^*}{2i}$. *(reality of spectrum of self-adjoint elements.)*
5. *Surjectivity.* The image is a \*-subalgebra of $C(\widehat{\mathcal A})$ that contains the constants, separates points (if $\chi_1\ne\chi_2$ they differ on some $a$, so $\widehat a$ separates them), and is closed (isometric image of a complete space). The **Stone–Weierstrass theorem** (a self-adjoint, point-separating, unital subalgebra of $C(X)$ is dense) forces the image to be all of $C(\widehat{\mathcal A})$. $\blacksquare$

This is a true *duality*: commutative unital C\*-algebras and compact Hausdorff spaces are the same data viewed two ways. "Noncommutative geometry" is the program of treating a general (noncommutative) C\*-algebra as the algebra of functions on a "quantum space" that has no underlying point set.

> **Corollary — continuous functional calculus.** If $a$ is a normal element of a C\*-algebra, then the C\*-subalgebra it generates is $\cong C(\sigma(a))$, under which $a\leftrightarrow(\text{the identity function }z\mapsto z)$. Consequently for any continuous $f:\sigma(a)\to\mathbb C$ there is a well-defined element $f(a)$, with $\|f(a)\|=\sup_{z\in\sigma(a)}|f(z)|$.

**Worked example.** Let $\mathcal A=C[0,1]$, the continuous functions on $[0,1]$. Its characters are *exactly* the point evaluations $\chi_t(f)=f(t)$ for $t\in[0,1]$: any character is determined by its value on the coordinate function $g(x)=x$, namely $\chi(g)=t\in\sigma(g)=[0,1]$, and then $\chi(f)=f(t)$ for polynomials $f$, hence for all $f$ by density. So $\widehat{\mathcal A}\cong[0,1]$ and the Gelfand transform is the identity $C[0,1]\to C[0,1]$. The space we started with is exactly the space Gelfand reconstructs.

**Worked example — recovering eigenvalues as the Gelfand spectrum.** Let $a=\begin{psmallmatrix}2&0\\0&3\end{psmallmatrix}\in M_2(\mathbb C)$ and let $\mathcal A$ be the commutative C\*-subalgebra it generates together with $1$ — that is, all polynomials in $a$, which here is just the diagonal matrices $\{\mathrm{diag}(\alpha,\beta)\}\cong\mathbb C^2$. A character must send the projection $p=\begin{psmallmatrix}1&0\\0&0\end{psmallmatrix}$ to a number $\chi(p)$ with $\chi(p)^2=\chi(p^2)=\chi(p)$, so $\chi(p)\in\{0,1\}$; the two choices give the two evaluations "read entry $1$" and "read entry $2$." Hence $\widehat{\mathcal A}$ is a two-point space, and the Gelfand transform sends $a$ to the function $\{1,2\}\to\mathbb C$ taking values $2$ and $3$. The function's range $\{2,3\}$ is exactly $\sigma(a)$: Gelfand turns the matrix into the *list of its eigenvalues regarded as a function on the spectrum*. This is precisely the continuous functional calculus in action — $f(a)$ is the matrix $\mathrm{diag}(f(2),f(3))$.

**Intuition.** Gelfand duality is the statement that "a commutative algebra of observables is the same as a classical phase space." A *classical* system is described by functions (observables) on a space (states); Gelfand says any commutative C\*-algebra **is** such an algebra of functions, with the space $\widehat{\mathcal A}$ reconstructed from the algebra. Quantum mechanics is then exactly what happens when the algebra of observables is allowed to be *noncommutative* — there is no underlying point space, only the algebra. This single sentence is the conceptual seed of noncommutative geometry.

## Part B — States, representations, and the GNS construction

<a id="s4"></a>
### Positive elements, states, and the GNS construction

**What and why.** We can now make precise what a "state" is purely algebraically (a normalized positive functional, an assignment of expectation values), and then perform the central miracle of the subject: from a single state we reconstruct a Hilbert space and a representation in which the state becomes $\langle\Omega,\cdot\,\Omega\rangle$ for a vector $\Omega$. This is the **GNS construction** (Gelfand–Naimark–Segal), the bridge back from algebra to Hilbert space.

> **Definition — positive element.** In a C\*-algebra $\mathcal A$, an element $a$ is **positive**, written $a\ge0$, if $a$ is self-adjoint and $\sigma(a)\subseteq[0,\infty)$. Equivalently (a theorem) $a=b^*b$ for some $b\in\mathcal A$.

The equivalence "positive $\iff a=b^*b$" is the algebraic backbone. One direction: if $a\ge0$ then by functional calculus $b=\sqrt a$ (using $f(z)=\sqrt z$ on $\sigma(a)\subseteq[0,\infty)$) is self-adjoint with $b^*b=b^2=a$. The converse — that $b^*b\ge0$ for every $b$ — is the nontrivial half *(stated without proof — a deep result)*; it rests on the C\*-identity and ensures the positive elements form a cone closed under addition.

> **Definition — state.** A **state** on a unital C\*-algebra $\mathcal A$ is a linear functional $\omega:\mathcal A\to\mathbb C$ that is
> - **positive**: $\omega(a^*a)\ge0$ for all $a$ (expectation of any "$|b|^2$" is nonnegative), and
> - **normalized**: $\omega(1)=1$.

A positive functional is automatically bounded with $\|\omega\|=\omega(1)$, so a state has $\|\omega\|=1$. We read $\omega(a)$ as the expectation value $\langle a\rangle_\omega$ of the observable $a$ in the state $\omega$.

> **Lemma — the GNS sesquilinear form and Cauchy–Schwarz.** For a state $\omega$, the form $\langle a,b\rangle_\omega:=\omega(a^*b)$ on $\mathcal A$ is sesquilinear and positive semidefinite, and satisfies the **Cauchy–Schwarz inequality** $|\omega(a^*b)|^2\le\omega(a^*a)\,\omega(b^*b)$.

**Proof.**
1. Sesquilinearity is inherited from linearity of $\omega$ and the involution: $\langle a,b\rangle_\omega=\omega(a^*b)$ is conjugate-linear in $a$, linear in $b$. *(linearity of $\omega$; $(\lambda a)^*=\overline\lambda a^*$.)*
2. Positivity: $\langle a,a\rangle_\omega=\omega(a^*a)\ge0$ by the state axiom. *(positivity of $\omega$.)*
3. Cauchy–Schwarz for any positive semidefinite sesquilinear form follows from $0\le\langle a+\lambda b,a+\lambda b\rangle_\omega$ for all $\lambda\in\mathbb C$; choosing $\lambda$ to minimize gives the inequality, exactly as for inner products. *(standard positive-form argument from the Functional Analysis guide.)* $\blacksquare$

> **Definition — representation.** A **representation** of a C\*-algebra $\mathcal A$ is a pair $(\pi,\mathcal H)$ with $\mathcal H$ a Hilbert space and $\pi:\mathcal A\to B(\mathcal H)$ a \*-homomorphism (linear, multiplicative, $\pi(a^*)=\pi(a)^*$, $\pi(1)=\mathrm{id}$). A vector $\Omega\in\mathcal H$ is **cyclic** if $\{\pi(a)\Omega:a\in\mathcal A\}$ is dense in $\mathcal H$.

> **Theorem — GNS construction.** Let $\omega$ be a state on a unital C\*-algebra $\mathcal A$. Then there exist a Hilbert space $\mathcal H_\omega$, a representation $\pi_\omega:\mathcal A\to B(\mathcal H_\omega)$, and a unit cyclic vector $\Omega_\omega\in\mathcal H_\omega$ such that
> $$
> \omega(a)=\langle\Omega_\omega,\ \pi_\omega(a)\,\Omega_\omega\rangle\qquad\text{for all }a\in\mathcal A.
> $$
> The triple is unique up to unitary equivalence.

**Proof (full construction).**
1. *Pre-inner product.* On the vector space $\mathcal A$ define $\langle a,b\rangle:=\omega(a^*b)$, positive semidefinite by the lemma. It may be **degenerate**: some nonzero $a$ have $\langle a,a\rangle=0$. *(GNS form.)*
2. *Null space is a left ideal.* Let $N=\{a:\omega(a^*a)=0\}$. By Cauchy–Schwarz, $a\in N$ iff $\omega(b^*a)=0$ for all $b$; this makes $N$ a closed subspace. Moreover $N$ is a **left ideal**: if $a\in N$ and $c\in\mathcal A$ then $\omega((ca)^*(ca))=\omega(a^*c^*ca)\le\|c^*c\|\,\omega(a^*a)=0$ (using $\omega(a^*xa)\le\|x\|\,\omega(a^*a)$ for $x=c^*c\ge0$, since $\|x\|1-x\ge0$). So $ca\in N$. *(positivity and the bound $x\le\|x\|1$ for self-adjoint $x$.)*
3. *Quotient and completion.* Form the quotient vector space $\mathcal A/N$, write $[a]$ for the class of $a$. The form descends to a genuine inner product on $\mathcal A/N$: $\langle[a],[b]\rangle:=\omega(a^*b)$ is well-defined (independent of representatives, since $N$ is exactly the null directions) and now positive *definite*. Let $\mathcal H_\omega$ be the completion of $\mathcal A/N$ to a Hilbert space. *(quotient by the null space of a semi-inner product; completion of an inner product space, from the Functional Analysis guide.)*
4. *The representation.* For $c\in\mathcal A$ define $\pi_\omega(c)[a]:=[ca]$. This is well-defined because $N$ is a left ideal (if $a\in N$ then $ca\in N$, so the formula respects classes). It is bounded: $\|\pi_\omega(c)[a]\|^2=\omega(a^*c^*ca)\le\|c\|^2\,\omega(a^*a)=\|c\|^2\|[a]\|^2$, hence $\pi_\omega(c)$ extends to a bounded operator on $\mathcal H_\omega$ with $\|\pi_\omega(c)\|\le\|c\|$. *(left-ideal property; the bound $c^*c\le\|c\|^2 1$.)*
5. *It is a \*-homomorphism.* Linearity and $\pi_\omega(cd)=\pi_\omega(c)\pi_\omega(d)$ are read off from $[cda]=c\cdot[da]$ (associativity). For the adjoint, $\langle[a],\pi_\omega(c)[b]\rangle=\omega(a^*cb)=\omega((c^*a)^*b)=\langle\pi_\omega(c^*)[a],[b]\rangle$, so $\pi_\omega(c)^*=\pi_\omega(c^*)$. *(associativity of $\mathcal A$; definition of the inner product.)*
6. *The cyclic vector.* Set $\Omega_\omega:=[1]$. Then $\pi_\omega(a)\Omega_\omega=[a]$, so the orbit $\{[a]:a\in\mathcal A\}=\mathcal A/N$ is dense in $\mathcal H_\omega$ by construction — $\Omega_\omega$ is cyclic. And $\langle\Omega_\omega,\pi_\omega(a)\Omega_\omega\rangle=\langle[1],[a]\rangle=\omega(1^*a)=\omega(a)$; with $a=1$, $\|\Omega_\omega\|^2=\omega(1)=1$. *(definitions.)*
7. *Uniqueness.* If $(\pi',\mathcal H',\Omega')$ is another such triple, the map $\pi_\omega(a)\Omega_\omega\mapsto\pi'(a)\Omega'$ is well-defined and isometric (both inner products equal $\omega(a^*b)$) on the dense cyclic orbits, hence extends to a unitary $U$ intertwining the representations and sending $\Omega_\omega$ to $\Omega'$. $\blacksquare$

> **Corollary — Gelfand–Naimark (general).** Every C\*-algebra is isometrically \*-isomorphic to a norm-closed \*-subalgebra of $B(\mathcal H)$ for some Hilbert space $\mathcal H$.

**Proof idea.** Take the **universal representation** $\pi=\bigoplus_\omega\pi_\omega$, the direct sum of all GNS representations over all states $\omega$. Enough states exist (for each self-adjoint $a$ there is a state with $|\omega(a)|=\|a\|$, by a Hahn–Banach extension of a character on the commutative subalgebra generated by $a$) to make $\pi$ isometric. So the abstract axioms of a C\*-algebra capture *exactly* the closed \*-subalgebras of bounded operators — no more, no less.

**Worked example.** Let $\mathcal A=M_2(\mathbb C)$ and $\omega(a)=\langle e_1,ae_1\rangle=a_{11}$ (the $(1,1)$ entry), the "spin-up" vector state. Its null space is $N=\{a:\omega(a^*a)=0\}=\{a:\text{column }1\text{ of }a\text{ is }0\}$, a $2$-dimensional left ideal. Then $\mathcal A/N$ is $2$-dimensional, spanned by $[E_{11}],[E_{21}]$ (matrix units), and $\pi_\omega(a)$ acts as left multiplication — which on the first column is just $a$ acting on $\mathbb C^2$. So GNS rebuilds the ordinary $\mathbb C^2$ representation with $\Omega_\omega=e_1$, exactly recovering the textbook spin-$\tfrac12$ Hilbert space from the expectation functional.

**Worked example — a mixed state gives a reducible GNS rep.** On the same $\mathcal A=M_2(\mathbb C)$ take the *tracial* state $\tau(a)=\tfrac12\mathrm{Tr}(a)=\tfrac12(a_{11}+a_{22})$. Now the form $\langle a,b\rangle_\tau=\tfrac12\mathrm{Tr}(a^*b)$ is *faithful*: $\tau(a^*a)=\tfrac12\mathrm{Tr}(a^*a)=\tfrac12\sum_{ij}|a_{ij}|^2=0$ forces $a=0$. So the null space is $N=\{0\}$, the quotient is all of $M_2(\mathbb C)$, and the GNS Hilbert space is the $4$-dimensional space of matrices with inner product $\tfrac12\mathrm{Tr}(a^*b)$ (the normalized Hilbert–Schmidt inner product). The representation $\pi_\tau(c)x=cx$ is left multiplication, which decomposes as two copies of the defining $\mathbb C^2$ representation (one per column), hence is **reducible** — matching the fact (s5) that $\tau$ is a mixed, non-pure state. The cyclic vector is $\Omega_\tau=1$ (the identity matrix), and indeed $\langle 1,c\,1\rangle_\tau=\tfrac12\mathrm{Tr}(c)=\tau(c)$. Contrast this with the pure state above, whose GNS space was only $2$-dimensional and irreducible: *the purer the state, the smaller and more irreducible its GNS world.*

<a id="s5"></a>
### Representations, irreducibility, and pure states

**What and why.** Different states give different GNS Hilbert spaces; the indecomposable building blocks correspond to **pure states** and **irreducible representations**. This is where the algebraic picture explains *superselection* — when two states cannot be coherently superposed, their representations are inequivalent.

> **Definition — subrepresentation, irreducible.** A closed subspace $\mathcal K\subseteq\mathcal H$ is **invariant** for a representation $\pi$ if $\pi(a)\mathcal K\subseteq\mathcal K$ for all $a$. The representation is **irreducible** if the only invariant closed subspaces are $\{0\}$ and $\mathcal H$.

> **Lemma — Schur's lemma (C\*-version).** $\pi$ is irreducible iff the only bounded operators commuting with every $\pi(a)$ are the scalar multiples of the identity, $\{\pi(\mathcal A)\}'=\mathbb C\,\mathrm{id}$. (Here $S'=\{T\in B(\mathcal H):TS=ST\ \forall S\in\mathcal S\}$ is the **commutant**.)

**Proof.**
1. ($\Leftarrow$) Suppose the commutant is $\mathbb C\,\mathrm{id}$ and let $\mathcal K$ be invariant. Since $\pi$ is a \*-representation, the orthogonal projection $P$ onto $\mathcal K$ commutes with all $\pi(a)$: invariance of $\mathcal K$ and (by taking adjoints, using $\pi(a^*)=\pi(a)^*$) invariance of $\mathcal K^\perp$ give $P\pi(a)=\pi(a)P$. So $P\in\{\pi(\mathcal A)\}'=\mathbb C\,\mathrm{id}$, forcing $P=0$ or $P=\mathrm{id}$, i.e. $\mathcal K=\{0\}$ or $\mathcal H$. *(a projection is in the commutant iff its range is invariant for a \*-closed set.)*
2. ($\Rightarrow$) Conversely if some self-adjoint $T$ in the commutant is not scalar, its spectral projections (functional calculus) are non-trivial commutant projections, giving a proper invariant subspace. A general commutant element splits into self-adjoint parts, both in the commutant. $\blacksquare$

> **Definition — pure state.** A state $\omega$ is **pure** if it is an extreme point of the convex set of all states: whenever $\omega=t\,\omega_1+(1-t)\omega_2$ with $0<t<1$ and $\omega_i$ states, then $\omega_1=\omega_2=\omega$. A non-pure state is **mixed**.

> **Theorem — purity $\iff$ irreducibility.** A state $\omega$ is pure if and only if its GNS representation $\pi_\omega$ is irreducible.

**Proof (key steps).**
1. There is a bijection between (i) positive functionals $\le\omega$ and (ii) positive operators in the commutant $\{\pi_\omega(\mathcal A)\}'$ bounded by $\mathrm{id}$: a functional $\omega'\le\omega$ corresponds to $\omega'(a)=\langle\Omega_\omega,\pi_\omega(a)T\Omega_\omega\rangle$ for a unique $0\le T\le\mathrm{id}$ in the commutant. *(Radon–Nikodym-type lemma for states, using cyclicity of $\Omega_\omega$.)*
2. $\omega$ is pure iff the only such $T$ are $0$ and $\mathrm{id}$ (no nontrivial splitting), iff the commutant contains no nontrivial positive contraction, iff $\{\pi_\omega(\mathcal A)\}'=\mathbb C\,\mathrm{id}$, iff (Schur) $\pi_\omega$ is irreducible. $\blacksquare$

**Worked example.** On $M_2(\mathbb C)$ the vector state $\omega(a)=\langle\psi,a\psi\rangle$ for a unit vector $\psi$ is pure (its GNS rep is the irreducible $\mathbb C^2$). The "maximally mixed" state $\tau(a)=\tfrac12\mathrm{Tr}(a)=\tfrac12(a_{11}+a_{22})$ is *not* pure: $\tau=\tfrac12\omega_{e_1}+\tfrac12\omega_{e_2}$, a proper convex combination. Its GNS representation is the $4$-dimensional left-regular representation $M_2(\mathbb C)$ acting on itself, which is reducible (it is $2$ copies of $\mathbb C^2$).

## Part C — Von Neumann algebras

<a id="s6"></a>
### Von Neumann algebras and the double commutant theorem

**What and why.** C\*-algebras are closed in the norm topology. If instead we close in a *weaker* topology — the one in which limits of operators are taken matrix-element by matrix-element — we get **von Neumann algebras**, which carry far more structure (projections in abundance, a rich type theory). The astonishing **double commutant theorem** says this analytic closure coincides exactly with the purely algebraic condition $\mathcal M=\mathcal M''$.

> **Definition — weak and strong operator topologies.** On $B(\mathcal H)$:
> - $T_n\to T$ **strongly** (SOT) if $T_n\xi\to T\xi$ in norm for every $\xi\in\mathcal H$;
> - $T_n\to T$ **weakly** (WOT) if $\langle\eta,T_n\xi\rangle\to\langle\eta,T\xi\rangle$ for all $\xi,\eta\in\mathcal H$.
> Both are weaker than norm convergence $\|T_n-T\|\to0$.

> **Definition — von Neumann algebra.** A **von Neumann algebra** $\mathcal M\subseteq B(\mathcal H)$ is a unital \*-subalgebra that is closed in the weak operator topology. (Equivalently, closed in the strong operator topology — the two give the same closed \*-algebras.)

> **Definition — commutant.** For $\mathcal S\subseteq B(\mathcal H)$, the **commutant** is $\mathcal S'=\{T\in B(\mathcal H):TS=ST\ \forall S\in\mathcal S\}$. The **double commutant** is $\mathcal S''=(\mathcal S')'$.

The commutant of any set is always a von Neumann algebra: it is a \*-algebra (if $\mathcal S$ is \*-closed) and WOT-closed (commuting is a closed condition).

> **Theorem — von Neumann's double commutant theorem.** Let $\mathcal M\subseteq B(\mathcal H)$ be a unital \*-subalgebra. The following are equivalent:
> 1. $\mathcal M$ is closed in the weak operator topology (it is a von Neumann algebra);
> 2. $\mathcal M$ is closed in the strong operator topology;
> 3. $\mathcal M=\mathcal M''$.

**Proof (the substantial implication $\mathcal M''\subseteq\overline{\mathcal M}^{\,SOT}$).**
1. Let $T\in\mathcal M''$, fix $\xi_1,\dots,\xi_n\in\mathcal H$ and $\varepsilon>0$; we find $A\in\mathcal M$ with $\|(T-A)\xi_i\|<\varepsilon$ for all $i$ (this is a basic SOT-neighborhood). *(definition of SOT closure.)*
2. *Single vector ($n=1$).* Let $\mathcal K=\overline{\mathcal M\xi}$ (closure of the orbit) and $P$ the projection onto $\mathcal K$. Since $\mathcal M\mathcal K\subseteq\mathcal K$ and $\mathcal M$ is \*-closed, $P\in\mathcal M'$. As $T\in\mathcal M''$, $T$ commutes with $P$, so $T\mathcal K\subseteq\mathcal K$. Now $\xi=1\cdot\xi\in\mathcal K$ (using $1\in\mathcal M$), hence $T\xi\in\mathcal K=\overline{\mathcal M\xi}$, so some $A\in\mathcal M$ has $\|T\xi-A\xi\|<\varepsilon$. *(invariant subspace gives commutant projection; $T$ in double commutant commutes with it.)*
3. *Many vectors.* Apply the $n=1$ argument to the **amplification**: $\mathcal H^{(n)}=\mathcal H\oplus\cdots\oplus\mathcal H$, with $\mathcal M$ acting diagonally as $A^{(n)}=A\oplus\cdots\oplus A$. One checks $(\mathcal M^{(n)})''=(\mathcal M'')^{(n)}$, so $T^{(n)}\in(\mathcal M^{(n)})''$, and the single-vector result applied to $\xi=(\xi_1,\dots,\xi_n)\in\mathcal H^{(n)}$ yields $A$ with $\sum_i\|(T-A)\xi_i\|^2<\varepsilon^2$. *(amplification trick reduces the general case to $n=1$.)*
4. Hence $T\in\overline{\mathcal M}^{\,SOT}$. Combined with the trivial inclusions $\mathcal M\subseteq\mathcal M''$ and (closure facts) $\overline{\mathcal M}^{\,WOT}\subseteq\mathcal M''$ since $\mathcal M''$ is WOT-closed, all three conditions coincide. $\blacksquare$

**Meaning.** The theorem is a bridge between analysis (closure in a topology) and algebra (commuting relations). It says: the operators you can *approximate* using $\mathcal M$ are precisely those that are *forced* to lie in $\mathcal M$ by every symmetry that $\mathcal M$ respects. Physically, $\mathcal M'$ is the algebra of operators commuting with all observables in $\mathcal M$ — the "symmetries" — and $\mathcal M=\mathcal M''$ says the observables are exactly what commutes with the symmetries.

> **Definition — center.** The **center** of a von Neumann algebra $\mathcal M$ is $Z(\mathcal M)=\mathcal M\cap\mathcal M'$, the elements commuting with everything in $\mathcal M$. It always contains $\mathbb C\,\mathrm{id}$.

**Worked example.** Let $\mathcal M\subseteq B(\mathbb C^2)$ be the diagonal matrices $\{\mathrm{diag}(\alpha,\beta)\}$. Its commutant $\mathcal M'$ is also the diagonal matrices (a matrix commuting with $\mathrm{diag}(1,2)$ must be diagonal). Then $\mathcal M''=(\mathcal M')'=$ diagonal again $=\mathcal M$ — confirming $\mathcal M=\mathcal M''$. Here $\mathcal M$ is commutative, $\mathcal M=\mathcal M'$, and the center is all of $\mathcal M$.

**Worked example — a factor and its commutant by amplification.** Let $\mathcal M=M_2(\mathbb C)\otimes 1_3$ acting on $\mathcal H=\mathbb C^2\otimes\mathbb C^3=\mathbb C^6$, i.e. block-scalar operators $a\otimes 1$ that apply a fixed $2\times2$ matrix to the first factor and do nothing to the second. A direct computation (or the **commutation theorem** for tensor products) gives $\mathcal M'=1_2\otimes M_3(\mathbb C)$, the operators acting only on the second factor. Then $\mathcal M''=(1_2\otimes M_3)'=M_2(\mathbb C)\otimes1_3=\mathcal M$, again verifying the double commutant theorem. The center is $Z(\mathcal M)=\mathcal M\cap\mathcal M'=(M_2\otimes1)\cap(1\otimes M_3)=\mathbb C\,1_6$ — trivial — so $\mathcal M$ is a **factor** (of type I$_2$, foreshadowing s7). This is the simplest illustration that a factor on a tensor-product Hilbert space "owns" one tensor factor and hands the other to its commutant — the algebraic skeleton of a bipartite quantum system, observer versus environment.

**Pitfall — norm closure is not enough.** A C\*-algebra (norm-closed) need not be a von Neumann algebra (WOT-closed). Example: the compact operators $K(\mathcal H)$ on infinite-dimensional $\mathcal H$ form a C\*-algebra but are *not* WOT-closed — finite-rank projections onto larger and larger subspaces converge strongly to $1$, which is not compact. Its WOT closure (equivalently its double commutant) is all of $B(\mathcal H)$. So $K(\mathcal H)''=B(\mathcal H)\ne K(\mathcal H)$, and the double commutant theorem correctly reports that $K(\mathcal H)$ is not a von Neumann algebra.

<a id="s7"></a>
### Factors and the Murray–von Neumann classification

**What and why.** A von Neumann algebra with the smallest possible center — just the scalars — cannot be split into independent pieces; it is a **factor**, the irreducible building block. Murray and von Neumann discovered the shocking fact that factors come in distinct **types** distinguished by how "big" their projections can be, measured by a dimension function that need not take integer or even discrete values.

> **Definition — factor.** A von Neumann algebra $\mathcal M$ is a **factor** if its center is trivial: $Z(\mathcal M)=\mathcal M\cap\mathcal M'=\mathbb C\,\mathrm{id}$. (Every von Neumann algebra is a "direct integral" of factors, so factors are the atoms.)

> **Definition — projections and equivalence.** A **projection** is $p\in\mathcal M$ with $p=p^*=p^2$. Two projections $p,q$ are **(Murray–von Neumann) equivalent**, $p\sim q$, if there is a **partial isometry** $v\in\mathcal M$ with $v^*v=p$ and $vv^*=q$ (so $v$ maps the range of $p$ isometrically onto the range of $q$). We write $p\preceq q$ if $p\sim q'\le q$ for some subprojection $q'$.

This $\preceq$ totally orders the projections of a factor (a theorem) and so behaves like a "size." A projection $p$ is **finite** if it is not equivalent to a proper subprojection of itself ($p\sim q\le p\Rightarrow q=p$); otherwise **infinite**. This is the operator-algebra version of Dedekind's distinction between finite and infinite sets (a set is infinite iff it bijects with a proper subset).

> **Theorem — Murray–von Neumann classification.** Every factor falls into exactly one of the following types, characterized by the range of a normalized **dimension function** $d(p)$ on its projections:
> - **Type I$_n$** ($n\in\{1,2,\dots\}$): $d$ takes values in $\{0,1,2,\dots,n\}$; the factor is $\cong B(\mathbb C^n)=M_n(\mathbb C)$. **Type I$_\infty$**: values $\{0,1,2,\dots,\infty\}$; the factor is $\cong B(\mathcal H)$ for separable infinite-dimensional $\mathcal H$.
> - **Type II$_1$**: $d$ takes *all* values in the continuum $[0,1]$, and the identity is finite. There is a continuum of inequivalent projection sizes but no minimal (atomic) projection.
> - **Type II$_\infty$**: values $[0,\infty]$; the identity is infinite, but the factor has a finite subprojection.
> - **Type III**: the only values are $\{0,\infty\}$ — every nonzero projection is infinite and equivalent to the identity; there is *no* trace at all.

**Proof structure (what the classification rests on).**
1. *Comparison theorem.* In a factor, for any two projections $p,q$, either $p\preceq q$ or $q\preceq p$. *(uses triviality of the center: the central projection that would obstruct comparison is $0$ or $1$.)*
2. *Dimension function.* On the equivalence classes of projections, $\preceq$ is a total order and there is an essentially unique additive function $d$ (additive on orthogonal projections, $d(p)+d(q)=d(p+q)$ when $pq=0$), normalized by $d(1)=1$ in the finite case. *(additivity from partial isometries; uniqueness up to scale.)*
3. *Range dichotomy* *(stated without proof — a deep result)*. The possible ranges of $d$ are exactly the five listed sets; which one occurs is the type. The deep content is that the *continuous* range $[0,1]$ (type II$_1$) and the *degenerate* range $\{0,\infty\}$ (type III) actually occur — von Neumann constructed type II$_1$ from the group-measure-space and infinite-tensor-product constructions. $\blacksquare$

**Meaning and physics.** Type I is ordinary quantum mechanics — observables on a fixed Hilbert space, with minimal projections (rank-one, "pure states exist as vectors"). Type II and III have *no minimal projections*: you can keep halving a projection forever. Type III factors are the generic case in **quantum field theory** — the local algebra of observables in any bounded region of spacetime is a type III$_1$ factor (a theorem of Buchholz–Fredenhagen and others). This is why field theory has no normalizable "smallest excitation localized in a region" and why local states are highly entangled.

**Worked example (the hyperfinite II$_1$ factor).** Take the infinite tensor product of $2\times2$ matrix algebras with the trace state, $\mathcal R=\overline{\bigotimes_{k=1}^\infty M_2(\mathbb C)}$ (weak closure in the GNS representation of the product trace $\tau=\bigotimes\frac12\mathrm{Tr}$). A projection of "trace $1/2^k$" exists for every $k$, and by combining them one realizes every dyadic rational, then by closure every real value in $[0,1]$ — so $d$ has continuous range and $\mathcal R$ is a II$_1$ factor with no minimal projection.

**Worked example — finiteness as Dedekind-finiteness, concretely.** In $\mathcal M=B(\mathcal H)$ with $\mathcal H=\ell^2(\mathbb N)$ (type I$_\infty$), the identity $1$ is an *infinite* projection: the unilateral shift $v(e_n)=e_{n+1}$ is a partial isometry with $v^*v=1$ but $vv^*=1-p_0$, the projection killing the first basis vector. So $1\sim 1-p_0\lneq1$ — the identity is equivalent to a proper subprojection of itself, exactly Dedekind's "infinite set bijects with a proper subset." In a II$_1$ factor this is impossible: the trace would give $\tau(1)=\tau(1-p_0)=\tau(1)-\tau(p_0)$, forcing $\tau(p_0)=0$ and hence $p_0=0$ (faithfulness). The *existence of a faithful finite trace* is precisely what makes the identity finite, separating type II$_1$ from the infinite types. Type III is the extreme opposite: $1$ is infinite and *every* nonzero projection is equivalent to $1$, so the only conceivable trace values are $0$ and $\infty$ — no finite trace can exist at all.

**Intuition — why physics meets type III.** A local algebra in QFT contains, for every region nested inside it, observables of arbitrarily fine localization, and the vacuum entangles all scales. There is no "smallest indivisible excitation" one could call a minimal projection, and the entanglement is so strong that any local projection can be rotated into any other by the algebra — the hallmark of type III$_1$. The absence of a trace is the mathematical face of the physical fact that *energy and entanglement entropy in a region are not normalizable*; this is why naive "number of states in a box" counting diverges and must be regulated.

<a id="s8"></a>
### Traces and a first look at Tomita–Takesaki modular theory

**What and why.** A **trace** is a state insensitive to the order of multiplication, $\tau(ab)=\tau(ba)$ — the abstract version of the matrix trace, and exactly what type II$_1$ factors possess and type III factors lack. When no trace exists, a state still carries dynamical information: **Tomita–Takesaki theory** shows that *every* faithful state on a von Neumann algebra generates a canonical one-parameter group of automorphisms, the **modular flow** — an intrinsic notion of time built from the algebra and the state alone.

> **Definition — trace.** A **tracial state** on a von Neumann algebra $\mathcal M$ is a state $\tau$ with the **trace property** $\tau(ab)=\tau(ba)$ for all $a,b\in\mathcal M$. It is **faithful** if $\tau(a^*a)=0\Rightarrow a=0$.

> **Proposition — a II$_1$ factor has a unique faithful tracial state.** The dimension function $d$ extends to the unique trace: $\tau(p)=d(p)$ on projections, extended by linearity and continuity.

**Proof sketch.**
1. *Existence.* Define $\tau(p)=d(p)$ for projections; extend to self-adjoint elements via the spectral decomposition (functional calculus writes $a=\int\lambda\,dp_\lambda$) and then to all of $\mathcal M$ by linearity. The trace property $\tau(ab)=\tau(ba)$ holds first for partial isometries (since $v^*v\sim vv^*$ have equal $d$) and extends by linearity/density. *(dimension function additivity and equivalence of $v^*v,vv^*$.)*
2. *Uniqueness.* Any two traces agree on projections because $d$ is the unique normalized additive function on projection-classes in a factor (s7), hence agree everywhere by density. $\blacksquare$

> **Theorem — Tomita–Takesaki (statement).** Let $\mathcal M\subseteq B(\mathcal H)$ be a von Neumann algebra with a **cyclic and separating** vector $\Omega$ (cyclic: $\mathcal M\Omega$ dense; separating: $a\Omega=0\Rightarrow a=0$). Define the antilinear operator $S$ by
> $$
> S\,a\Omega=a^*\Omega\qquad(a\in\mathcal M),
> $$
> and let $S=J\Delta^{1/2}$ be its **polar decomposition**, with $J$ antiunitary (the **modular conjugation**) and $\Delta=S^*S>0$ (the **modular operator**). Then:
> 1. $J\mathcal M J=\mathcal M'$ — conjugation by $J$ swaps the algebra with its commutant;
> 2. $\Delta^{it}\mathcal M\Delta^{-it}=\mathcal M$ for all $t\in\mathbb R$ — the **modular automorphism group** $\sigma_t(a)=\Delta^{it}a\Delta^{-it}$ preserves $\mathcal M$.

**Interpretation.**
1. The vector state $\omega(a)=\langle\Omega,a\Omega\rangle$ defines, through $\Delta$ alone, a canonical dynamics $\sigma_t$ on the algebra. There is no clock chosen by hand: the *state itself* tells the observables how to evolve. This is the famous slogan "the state contains the time" (Connes–Rovelli **thermal time hypothesis**).
2. When $\tau$ is a trace, $S$ is essentially $J$ alone and $\Delta=1$, so the modular flow is trivial ($\sigma_t=\mathrm{id}$). Nontrivial modular flow is exactly the symptom of a *non-tracial* state — the generic situation in type III, hence in field theory.
3. The relation $\sigma_t(a)=\Delta^{it}a\Delta^{-it}$ together with the KMS condition (s11) identifies $\omega$ as a thermal equilibrium state for the dynamics $\sigma_t$ at inverse temperature $\beta=-1$. Equilibrium and modular flow are the same phenomenon.

**Worked example.** Let $\mathcal M=M_n(\mathbb C)$ acting on $\mathcal H=M_n(\mathbb C)$ (Hilbert–Schmidt inner product $\langle x,y\rangle=\mathrm{Tr}(x^*y)$) by left multiplication, with cyclic-separating vector $\Omega=\rho^{1/2}$ where $\rho>0$ is a density matrix ($\rho>0$, $\mathrm{Tr}\,\rho=1$), giving the state $\omega(a)=\mathrm{Tr}(\rho a)$. Then $S(a\rho^{1/2})=a^*\rho^{1/2}$ unwinds to $\Delta(x)=\rho x\rho^{-1}$ and the modular flow is $\sigma_t(a)=\rho^{it}a\rho^{-it}$ — exactly Heisenberg evolution generated by the "Hamiltonian" $-\log\rho$. So $\omega$ is the **Gibbs state** $\rho=e^{-H}/\mathrm{Tr}\,e^{-H}$ at $\beta=1$, and modular flow is thermal time. When $\rho=\frac1n 1$ (the trace), $\Delta=1$ and the flow is trivial — matching point (2).

## Part D — Algebraic quantum field theory

<a id="s9"></a>
### The canonical (anti)commutation relations: Weyl, CCR, CAR

**What and why.** Quantizing a field means making the classical Poisson brackets into commutators: $[\,\widehat q,\widehat p\,]=i\hbar$. But unbounded operators are awkward to put in a C\*-algebra (they have no norm). The fix is to exponentiate to bounded unitaries — the **Weyl operators** — whose commutation relations are an algebraic identity. For fermions one uses *anticommutators*, giving the bounded **CAR algebra** directly.

> **Definition — Heisenberg CCR (unbounded form).** The **canonical commutation relation** for one degree of freedom is the relation, on a suitable domain,
> $$
> [\,\widehat q,\widehat p\,]=\widehat q\widehat p-\widehat p\widehat q=i\hbar\,1.
> $$
> No bounded operators can satisfy this: if they did, taking the trace (in finite dimensions) of both sides gives $0=i\hbar n$, impossible; in infinite dimensions $\|\,[\widehat q,\widehat p]\,\|$ would have to bound $|\hbar|$ times unbounded powers (Wintner's theorem). Hence $\widehat q,\widehat p$ are necessarily unbounded.

> **Definition — Weyl operators and the CCR algebra.** Introduce the bounded unitaries $W(s,t)=e^{i(s\widehat q+t\widehat p)}$ for $(s,t)\in\mathbb R^2$. The Baker–Campbell–Hausdorff formula turns the CCR into the **Weyl relations**:
> $$
> W(s_1,t_1)\,W(s_2,t_2)=e^{-\tfrac{i\hbar}{2}(s_1 t_2-s_2 t_1)}\,W(s_1+s_2,\ t_1+t_2).
> $$
> The C\*-algebra generated by symbols $W(f)$ for $f$ in a symplectic space $(V,\sigma)$, with $W(f)W(g)=e^{-\frac i2\sigma(f,g)}W(f+g)$ and $W(f)^*=W(-f)$, is the **Weyl (CCR) algebra** $\mathrm{CCR}(V,\sigma)$.

> **Theorem — Stone–von Neumann.** For finitely many degrees of freedom, every irreducible representation of the Weyl relations by strongly continuous unitaries is unitarily equivalent to the standard Schrödinger representation on $L^2(\mathbb R^n)$.

This is *uniqueness* of quantization in finite dimensions — and its **failure in infinite dimensions** (infinitely many degrees of freedom, i.e. fields) is precisely why QFT has inequivalent representations, the technical root of Haag's theorem (s11).

> **Definition — CAR algebra.** For fermions, given a Hilbert space $\mathfrak h$ (the "one-particle space"), the **canonical anticommutation relations** are, for **creation/annihilation operators** $a(f),a^*(f)$ ($f\in\mathfrak h$),
> $$
> \{a(f),a^*(g)\}=a(f)a^*(g)+a^*(g)a(f)=\langle f,g\rangle\,1,\qquad \{a(f),a(g)\}=0.
> $$
> Because $\|a(f)\|=\|f\|$ (a consequence of the C\*-identity applied to these relations — proved below), these *are* bounded, so the **CAR algebra** $\mathrm{CAR}(\mathfrak h)$ is a genuine C\*-algebra with no need to exponentiate.

**Proof that $\|a(f)\|=\|f\|$.**
1. From the CAR, $a(f)^*a(f)+a(f)a(f)^*=\langle f,f\rangle1=\|f\|^2 1$, and $a(f)^2=0$ (set $g=f$ in the second relation). *(CAR relations.)*
2. Let $x=a(f)^*a(f)\ge0$. Then $x^2=a(f)^*a(f)a(f)^*a(f)=a(f)^*(\|f\|^21-a(f)^*a(f))a(f)=\|f\|^2 x-a(f)^*a(f)^{*}a(f)a(f)$, and the last term vanishes because $a(f)^2=0$ gives $a(f)a(f)=0$. So $x^2=\|f\|^2x$. *(substitute the anticommutator; use $a(f)^2=0$.)*
3. Thus $\sigma(x)\subseteq\{0,\|f\|^2\}$, so $\|x\|=\|f\|^2$ (it is nonzero for $f\ne0$). By the C\*-identity $\|a(f)\|^2=\|a(f)^*a(f)\|=\|x\|=\|f\|^2$, hence $\|a(f)\|=\|f\|$. *(spectrum from $x^2=\|f\|^2x$; C\*-identity.)* $\blacksquare$

**Worked example (one fermionic mode).** With $\dim\mathfrak h=1$, write $a=a(f)$ for unit $f$. Then $\{a,a^*\}=1$, $a^2=0$. Represent on $\mathbb C^2$ by $a=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}$: indeed $a^2=0$, $a^*a=\begin{psmallmatrix}0&0\\0&1\end{psmallmatrix}$, $aa^*=\begin{psmallmatrix}1&0\\0&0\end{psmallmatrix}$, and $a^*a+aa^*=1$. The number operator $a^*a$ has eigenvalues $0$ (empty) and $1$ (occupied) — the Pauli exclusion principle, $a^2=0$ meaning "no two fermions in one mode," falls straight out of the algebra. And $\|a\|=1=\|f\|$, matching the theorem.

<a id="s10"></a>
### Algebraic quantum field theory: Haag–Kastler axioms

**What and why.** Algebraic QFT (AQFT) makes the slogan "observables before states" into the foundation of relativistic quantum field theory. The primary object is not a field operator at a point (a singular object) but the assignment, to each region of spacetime, of the C\*-algebra of observables measurable *in that region*. A QFT *is* such an assignment — a **net of local algebras** — satisfying axioms encoding locality and relativistic covariance.

> **Definition — net of local observables.** Let $\mathcal O\mapsto\mathfrak A(\mathcal O)$ assign to each bounded open region $\mathcal O$ of Minkowski spacetime $\mathbb R^{1,3}$ a C\*-algebra $\mathfrak A(\mathcal O)\subseteq\mathfrak A$ of observables localized in $\mathcal O$, all inside one global C\*-algebra $\mathfrak A=\overline{\bigcup_{\mathcal O}\mathfrak A(\mathcal O)}$. This assignment is a **net**.

> **Definition — Haag–Kastler axioms.** A net $\mathcal O\mapsto\mathfrak A(\mathcal O)$ is a (Haag–Kastler) **QFT** if:
> 1. **Isotony** (monotonicity): $\mathcal O_1\subseteq\mathcal O_2\Rightarrow\mathfrak A(\mathcal O_1)\subseteq\mathfrak A(\mathcal O_2)$. More measurements are possible in a larger region.
> 2. **Microcausality / locality**: if $\mathcal O_1$ and $\mathcal O_2$ are **spacelike separated** (no signal at speed $\le c$ connects them), then their algebras commute elementwise: $[\mathfrak A(\mathcal O_1),\mathfrak A(\mathcal O_2)]=\{0\}$. Spacelike-separated measurements do not disturb each other — the algebraic form of Einstein causality.
> 3. **Poincaré covariance**: the Poincaré group (Lorentz transformations and spacetime translations) acts by automorphisms $\alpha_g:\mathfrak A\to\mathfrak A$ with $\alpha_g(\mathfrak A(\mathcal O))=\mathfrak A(g\mathcal O)$. The physics is relativistically invariant.
> 4. **Spectrum condition** (positivity of energy): in the vacuum representation, the generator of time translations (the Hamiltonian) has nonnegative spectrum, and the energy–momentum lies in the forward light cone.
> 5. **Vacuum**: there is a Poincaré-invariant state $\omega_0$ (the **vacuum**), whose GNS representation contains a unique invariant vector $\Omega_0$.

**Why this is the right packaging.**
1. The axioms refer only to algebras and regions, never to a specific Hilbert space or field. Two theories with the same net are physically identical; the net is the invariant. *(observables-first principle of s0.)*
2. Microcausality is the *only* place the spacetime causal structure enters — the entire content of "relativity" is "spacelike algebras commute." This makes causality manifestly an algebraic property.
3. **Haag duality** (often an additional requirement) states $\mathfrak A(\mathcal O)'=\mathfrak A(\mathcal O')$, where $\mathcal O'$ is the spacelike complement: the commutant of a local algebra is the algebra of the causally disconnected region. This is the AQFT incarnation of the double commutant theorem (s6) and ties directly to Tomita–Takesaki: the modular flow of the vacuum on a wedge region is the Lorentz boost (the **Bisognano–Wichmann theorem**), and the associated KMS temperature is the **Unruh temperature** felt by an accelerated observer.

> **Theorem (Reeh–Schlieder, statement).** In a Haag–Kastler net with the spectrum condition, the vacuum $\Omega_0$ is **cyclic and separating** for every local algebra $\mathfrak A(\mathcal O)$ of a region with nonempty causal complement.

**Meaning.** From a single bounded region one can, by acting with local observables on the vacuum, approximate *any* state of the global theory — even states describing particles on the far side of the universe. This is a sharp statement of vacuum entanglement, and (via s8) it is exactly the cyclic-separating hypothesis that powers modular theory: every local algebra $\mathfrak A(\mathcal O)$ carries a canonical modular flow built from the vacuum.

**Worked example (free scalar field, schematically).** For the free Klein–Gordon field one builds $\mathfrak A(\mathcal O)$ as the Weyl (CCR) algebra over the space of real test functions supported in $\mathcal O$, with symplectic form given by the commutator distribution $\sigma(f,g)=\int(f\,\partial_0 g-g\,\partial_0 f)$. Isotony holds because larger support sets contain smaller ones; microcausality holds because the commutator distribution vanishes for spacelike-separated supports (the field's causal propagator is supported in the light cone); Poincaré covariance is inherited from the action on test functions. The local algebras turn out to be type III$_1$ factors (s7) — the generic AQFT situation.

<a id="s11"></a>
### The KMS condition, thermal states, and Haag's theorem

**What and why.** How does one say "thermal equilibrium" without a trace (impossible in type III)? The answer is the **KMS condition** — an analyticity condition relating $\omega(a\,\sigma_t(b))$ to $\omega(\sigma_t(b)\,a)$ across a strip in the complex time plane. It captures the Gibbs state in finite systems and *generalizes* it to systems where $e^{-\beta H}/\mathrm{Tr}\,e^{-\beta H}$ makes no sense. And it ties directly back to modular theory and to the obstruction Haag identified for interacting fields.

> **Definition — dynamics on a C\*-algebra.** A **(C\*-)dynamical system** is a C\*-algebra $\mathfrak A$ with a strongly continuous one-parameter group of automorphisms $t\mapsto\sigma_t$ (the time evolution), $\sigma_{s+t}=\sigma_s\sigma_t$, $\sigma_t(a^*)=\sigma_t(a)^*$.

> **Definition — KMS condition.** A state $\omega$ on $(\mathfrak A,\sigma)$ satisfies the **KMS condition at inverse temperature $\beta>0$** (Kubo–Martin–Schwinger) if for all $a,b$ in a dense set there is a function $F_{a,b}$, bounded and continuous on the strip $\{z:0\le\mathrm{Im}\,z\le\beta\}$ and analytic in its interior, with boundary values
> $$
> F_{a,b}(t)=\omega\!\big(a\,\sigma_t(b)\big),\qquad F_{a,b}(t+i\beta)=\omega\!\big(\sigma_t(b)\,a\big).
> $$

> **Proposition — finite systems: KMS $\iff$ Gibbs.** For $\mathfrak A=M_n(\mathbb C)$ with $\sigma_t(a)=e^{itH}ae^{-itH}$, the unique $\beta$-KMS state is the **Gibbs state** $\omega_\beta(a)=\dfrac{\mathrm{Tr}(e^{-\beta H}a)}{\mathrm{Tr}(e^{-\beta H})}$.

**Proof.**
1. Take $\omega_\beta$ as defined and set $F_{a,b}(z)=\dfrac{1}{\mathrm{Tr}(e^{-\beta H})}\mathrm{Tr}\big(e^{-\beta H}a\,e^{izH}be^{-izH}\big)$. This entire function is analytic in $z$ (matrix exponentials are entire), bounded on the strip (finite dimensions). *(finite-dimensional analyticity.)*
2. At $z=t$ real, $F_{a,b}(t)=\omega_\beta(a\sigma_t(b))$ by definition. *(definition of $\sigma_t$.)*
3. At $z=t+i\beta$: write the analytic continuation of the conjugation explicitly, $\sigma_{t+i\beta}(b)=e^{i(t+i\beta)H}\,b\,e^{-i(t+i\beta)H}$, and use $e^{i(t+i\beta)H}=e^{itH}e^{-\beta H}$, so $F_{a,b}(t+i\beta)=\frac{1}{Z}\mathrm{Tr}(e^{-\beta H}a\,e^{itH}e^{-\beta H}be^{\beta H}e^{-itH})$; using cyclicity of the trace to move $e^{-\beta H}$ around and $\sigma_t(b)=e^{itH}be^{-itH}$, this equals $\omega_\beta(\sigma_t(b)\,a)$. *(cyclicity of the matrix trace; $Z=\mathrm{Tr}\,e^{-\beta H}$.)*
4. So $\omega_\beta$ is KMS. Uniqueness: the KMS boundary condition forces the two-point functions to match those of the Gibbs state, which determine the state. $\blacksquare$

> **Theorem — KMS $\iff$ modular (the bridge to s8).** A faithful state $\omega$ is $\beta$-KMS for the dynamics $\sigma_t$ if and only if (after rescaling time) $\sigma_t$ is the **modular automorphism group** of $\omega$, i.e. $\sigma_{-t/\beta}=\sigma_t^\omega=\Delta^{it}\cdot\Delta^{-it}$ from Tomita–Takesaki.

This is the punchline uniting the whole guide: equilibrium (KMS), intrinsic time (modular flow), and the structure of type III algebras are *the same mathematics*. Thermal states exist and are characterized by KMS even where no density matrix and no trace exist — exactly the regime of quantum field theory and quantum statistical mechanics in the thermodynamic limit.

> **Theorem — Haag's theorem (statement).** In a relativistic QFT satisfying the Wightman/Haag–Kastler axioms, if an interacting field at a fixed time is unitarily equivalent to a free field at that time (as the **interaction picture** of textbook perturbation theory assumes), then the interacting theory is in fact free — its $S$-matrix is trivial.

**Meaning, and how it closes the loop.**
1. The interaction picture presupposes one Hilbert space carrying both the free and the interacting field, related by a unitary. Haag's theorem says this is impossible for a genuinely interacting relativistic theory: the free and interacting **vacuum representations are unitarily inequivalent**.
2. The root cause is the failure of Stone–von Neumann in infinitely many degrees of freedom (s9): with infinitely many modes the Weyl relations admit a continuum of inequivalent irreducible representations, and the free and interacting fields sit in different ones.
3. This is the strongest vindication of the algebraic viewpoint of s0: one must take the **abstract algebra of observables** as primary, because *no single Hilbert space* is adequate. Representations — vacuum, thermal at each temperature, charged superselection sectors — are derived, state-by-state, by GNS. The algebra is the theory; the Hilbert spaces are its shadows.

**Worked example (a finite caricature of inequivalence).** Consider the infinite tensor product $\bigotimes_{k=1}^\infty\mathbb C^2$ with two product states: $\omega=\bigotimes\langle\uparrow,\cdot\,\uparrow\rangle$ (all spins up) and $\omega'=\bigotimes\langle\theta,\cdot\,\theta\rangle$ with each spin tilted by a fixed small angle $\theta$. Each defines a GNS representation. Because $\prod_k|\langle\uparrow,\theta\rangle|=\prod_k\cos(\theta/2)=0$ for $\theta\ne0$ (an infinite product of numbers $<1$), the two states are **disjoint**: there is no unitary intertwining their GNS representations. Two locally indistinguishable, globally inequivalent worlds on the same algebra — the same mechanism (infinitely many degrees of freedom) that makes Haag's theorem true.

**Worked example — KMS at $\beta\to0$ and $\beta\to\infty$.** Return to $\mathfrak A=M_2(\mathbb C)$ with Hamiltonian $H=\mathrm{diag}(0,E)$ ($E>0$) and dynamics $\sigma_t(a)=e^{itH}ae^{-itH}$. The $\beta$-KMS (Gibbs) state is
$$
\omega_\beta(a)=\frac{a_{11}+e^{-\beta E}a_{22}}{1+e^{-\beta E}}.
$$
As $\beta\to\infty$ (zero temperature) this tends to $\omega_\infty(a)=a_{11}$, the ground state — a *pure* state, the unique lowest-energy vector. As $\beta\to0$ (infinite temperature) it tends to $\omega_0(a)=\tfrac12(a_{11}+a_{22})$, the maximally mixed trace state, for which the modular flow is trivial (s8). So the KMS family interpolates between the pure ground state and the tracial chaos of infinite temperature, and the modular operator $\Delta=e^{-\beta H}\cdot\,e^{\beta H}$ deforms continuously with $\beta$ — a single algebraic object encoding the entire thermodynamics of the system. This finite example is the seed of the general theorem: KMS states are the equilibrium states, modular flow is their built-in dynamics, and in the thermodynamic or field-theoretic limit (type III) this is *the only* way equilibrium can be defined, since no Gibbs formula survives.

---

*We began by demoting the Hilbert space and promoting the algebra of observables, and the mathematics rewarded the choice at every turn: the C\*-identity made the norm a spectral invariant (s1–s2); Gelfand turned commutative algebras into spaces and gave the functional calculus (s3); GNS rebuilt Hilbert spaces from states (s4–s5); von Neumann's double commutant tied analysis to algebra and opened the type theory of factors (s6–s7); traces and modular flow revealed that a state secretly carries a dynamics, with KMS identifying equilibrium intrinsically (s8, s11); and the CCR/CAR algebras and Haag–Kastler axioms assembled all of it into relativistic quantum field theory, where Haag's theorem proves the algebraic standpoint was not a luxury but a necessity. The quantum world, read this way, is an algebra of what can be measured — and every Hilbert space is one of its many faithful retellings.*
