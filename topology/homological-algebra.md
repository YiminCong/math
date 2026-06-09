**English** · [中文](homological-algebra.zh.md)

# Homological Algebra & Spectral Sequences, *the machinery behind (co)homology.*

*A from-scratch course in the algebra that powers every (co)homology theory: exact sequences and diagram chasing, chain complexes, resolutions, the derived functors* $\mathrm{Tor}$ *and* $\mathrm{Ext}$*, the universal-coefficient and Künneth theorems, and finally spectral sequences — the bookkeeping device that organizes computations no single long exact sequence can reach. Every algebraic word is defined the first time it appears, and every theorem is demonstrated with no gaps.*

[← Back to all guides](../README.md)

> **How to read this guide.** Two earlier guides are useful but not strictly required. From the *Group Theory* guide we borrow the words *group*, *abelian group*, *homomorphism*, *kernel*, *image*, *quotient*, and *exact sequence*; each is restated in one line where first used. From the *Algebraic Topology* guide we borrow the idea that a space gives rise to a *chain complex* whose homology is a topological invariant — §s10 returns to that picture. We assume only ordinary arithmetic and a little single-variable calculus. Nothing is "left to the reader": every claim is proved.

---

## Part A — The algebra of exactness

<a id="s0"></a>
### Motivation: derived functors and spectral sequences as the organizing machinery of all (co)homology

Homology and cohomology theories appear all over mathematics — the homology of a topological space, the cohomology of a group, the cohomology of a sheaf, the Tor and Ext of modules. They look different on the surface, yet they share one engine. This guide builds that engine.

The engine has two halves.

- **Derived functors.** Many natural operations on algebraic objects are *almost* exact — they preserve *some* of the structure of an exact sequence but break it at one spot. A **derived functor** is a systematic gadget that measures exactly how much is broken, in every degree. The two prototypes are $\mathrm{Tor}$ (which measures the failure of the tensor product to be exact) and $\mathrm{Ext}$ (which measures the failure of $\mathrm{Hom}$ to be exact). Singular homology with coefficients, the universal-coefficient theorem, and the Künneth formula are all statements about these two functors.

- **Spectral sequences.** When an object is built in *two* directions at once — a space filtered by subspaces, a complex of complexes, a fibration with base and fiber — the homology cannot usually be read off in one step. A **spectral sequence** is a "movie" of successive approximations: a sequence of pages $E_1, E_2, E_3,\dots$, each computed from the previous one by taking homology, that in good cases *converges* to the answer. It is the master tool that contains long exact sequences, the Künneth formula, and the Leray–Serre computation of fibrations as special cases.

> **The thread of the whole guide.** Build the language of exactness (§s1–s2), learn to resolve objects into simple pieces (§s3), turn that into derived functors (§s4), cash it out in topology (§s5), abstract the pattern into category theory (§s6), and finally assemble the two-dimensional bookkeeping of double complexes and filtrations into spectral sequences (§s7–s11).

> **A preview in one example.** Consider the simplest non-exactness: tensoring the exact sequence $0\to\mathbb{Z}\xrightarrow{\times2}\mathbb{Z}\to\mathbb{Z}/2\to0$ with $\mathbb{Z}/2$ breaks injectivity (§s4). The single number that measures the break is $\mathrm{Tor}_1^{\mathbb{Z}}(\mathbb{Z}/2,\mathbb{Z}/2)=\mathbb{Z}/2$. That same $\mathrm{Tor}$ is what makes $H_2(\mathbb{RP}^2;\mathbb{Z}/2)$ nonzero (§s5), and the same circle of ideas, run in two dimensions, computes the homology of the Hopf fibration (§s10) and the cohomology of a group from that of a normal subgroup and quotient (§s11). One mechanism, many faces.

Throughout, the central object is the **module**, the common generalization of "abelian group" and "vector space." We start there.

<a id="s1"></a>
### Modules, exact sequences, and diagram chasing — the snake lemma and the five lemma

**What & why.** To do algebra uniformly we need a single kind of object flexible enough to include abelian groups, vector spaces, and "vector spaces over the integers." That object is a *module over a ring*. Then "exactness" — the precise statement that one map's image is the next map's kernel — becomes the grammar of the whole subject, and *diagram chasing* is how we prove things in that grammar.

> **Definition — ring.**
> A **ring** $R$ is a set with two operations, addition $+$ and multiplication $\cdot$, such that $(R,+)$ is an abelian group (addition is associative and commutative, has a zero $0$, and every element has a negative), multiplication is associative and has a unit $1$, and multiplication distributes over addition: $a(b+c)=ab+ac$ and $(a+b)c=ac+bc$. If $ab=ba$ always, the ring is **commutative**. *Example:* the integers $\mathbb{Z}$, and any field such as the rationals $\mathbb{Q}$ or the reals $\mathbb{R}$.

> **Definition — module.**
> A **left module** over a ring $R$ (an "$R$-module") is an abelian group $(M,+)$ together with a scalar multiplication $R\times M\to M$, written $(r,m)\mapsto rm$, satisfying for all $r,s\in R$ and $m,n\in M$:
>
> $$
> r(m+n)=rm+rn,\quad (r+s)m=rm+sm,\quad (rs)m=r(sm),\quad 1\,m=m.
> $$
>
> *Examples:* a $\mathbb{Z}$-module is *exactly* an abelian group (scalar multiplication by $n$ is "add $m$ to itself $n$ times"); a module over a field $k$ is *exactly* a vector space over $k$. So "module" is the common parent of both.

> **Definition — module homomorphism (= $R$-linear map).**
> A map $f:M\to N$ of $R$-modules is a **homomorphism** if it respects both operations: $f(m+m')=f(m)+f(m')$ and $f(rm)=rf(m)$. Its **kernel** is $\ker f=\{m:f(m)=0\}$ and its **image** is $\mathrm{im}f=\{f(m):m\in M\}$; both are submodules. $f$ is **injective** (one-to-one) iff $\ker f=0$, and **surjective** (onto) iff $\mathrm{im}f=N$. A bijective homomorphism is an **isomorphism**, written $\cong$.

> **Definition — quotient module.**
> If $K\subseteq M$ is a submodule, the **quotient** $M/K$ has elements the cosets $m+K=\{m+k:k\in K\}$, with $(m+K)+(m'+K)=(m+m')+K$ and $r(m+K)=rm+K$. The map $\pi:M\to M/K$, $\pi(m)=m+K$, is a surjective homomorphism with kernel $K$. *(First isomorphism theorem, used below: any homomorphism $f:M\to N$ induces $M/\ker f\cong \mathrm{im} f$.)*

> **Definition — exact sequence.**
> A sequence of $R$-modules and homomorphisms $\cdots\to A\xrightarrow{\,f\,}B\xrightarrow{\,g\,}C\to\cdots$ is **exact at $B$** if $\mathrm{im}f=\ker g$. It is **exact** if it is exact at every interior module. A **short exact sequence (SES)** is an exact sequence
>
> $$
> 0\to A\xrightarrow{\,f\,}B\xrightarrow{\,g\,}C\to 0,
> $$
>
> which unpacks to: $f$ is injective (exactness at $A$: $\mathrm{im}(0\to A)=0=\ker f$), $g$ is surjective (exactness at $C$: $\mathrm{im}g=\ker(C\to0)=C$), and $\mathrm{im}f=\ker g$, so by the first isomorphism theorem $C\cong B/\mathrm{im}f$.

*Worked example.* $0\to \mathbb{Z}\xrightarrow{\,\times 2\,}\mathbb{Z}\xrightarrow{\bmod 2}\mathbb{Z}/2\to 0$ is a short exact sequence of $\mathbb{Z}$-modules: multiplication by $2$ is injective, reduction mod $2$ is surjective, and the image of "$\times 2$" is the even integers, which is exactly the kernel of "mod $2$." We will use this exact sequence repeatedly.

*A second worked example (checking exactness by hand).* Consider $\mathbb{Z}\xrightarrow{\,f\,}\mathbb{Z}\xrightarrow{\,g\,}\mathbb{Z}/6$ with $f=\times3$ and $g=\bmod 6$. Is it exact at the middle $\mathbb{Z}$? Compute $\mathrm{im}f=3\mathbb{Z}=\{\dots,-3,0,3,6,\dots\}$ and $\ker g=6\mathbb{Z}$. Since $3\mathbb{Z}\neq6\mathbb{Z}$ (e.g. $3\in\mathrm{im}f$ but $g(3)=3\neq0$ so $3\notin\ker g$), the sequence is **not** exact at the middle. Replace $f$ by $\times6$: now $\mathrm{im}f=6\mathbb{Z}=\ker g$, and it is exact. This is the kind of explicit kernel-versus-image bookkeeping every later proof reduces to.

#### Diagram chasing

A **commutative diagram** is a picture of modules and arrows in which any two directed paths with the same start and end give equal composite maps. **Diagram chasing** proves statements by tracking a single element through such a diagram, justifying each move by exactness or commutativity. The two foundational results are the snake lemma and the five lemma.

> **Snake Lemma.** Given a commutative diagram with exact rows
>
> $$
> \begin{array}{ccccccccc}
> & & A & \xrightarrow{\,f\,} & B & \xrightarrow{\,g\,} & C & \to & 0\\
> & & \downarrow{\scriptstyle a} & & \downarrow{\scriptstyle b} & & \downarrow{\scriptstyle c} & & \\
> 0 & \to & A' & \xrightarrow{\,f'\,} & B' & \xrightarrow{\,g'\,} & C' & &
> \end{array}
> $$
>
> there is an exact sequence
>
> $$
> \ker a\to\ker b\to\ker c\xrightarrow{\;\partial\;}\mathrm{coker}a\to\mathrm{coker}b\to\mathrm{coker}c,
> $$
>
> where $\mathrm{coker}a=A'/\mathrm{im}a$ is the **cokernel**, and $\partial$ is the **connecting homomorphism**. If $f$ is injective the sequence may be capped with $0\to\ker a$ on the left; if $g'$ is surjective, with $\mathrm{coker}c\to 0$ on the right.

**Proof (complete diagram chase).**

1. *The induced maps on kernels.* If $x\in\ker a\subseteq A$, then $b(f(x))=f'(a(x))=f'(0)=0$ by commutativity of the left square, so $f$ restricts to $\ker a\to\ker b$. Likewise $g$ restricts to $\ker b\to\ker c$. *(commutativity of the squares)*
2. *The induced maps on cokernels.* If $y\in A'$, then $f'$ sends $\mathrm{im}a$ into $\mathrm{im}b$ (because $f'(a(x))=b(f(x))\in\mathrm{im}b$), so $f'$ descends to $\bar f':\mathrm{coker}a\to\mathrm{coker}b$, $\bar f'(y+\mathrm{im}a)=f'(y)+\mathrm{im}b$. Likewise $g'$ descends to $\bar g'$. *(commutativity again, plus the universal property of quotients)*
3. *Defining the connecting map $\partial:\ker c\to\mathrm{coker}a$.* Take $z\in\ker c\subseteq C$. Since $g$ is surjective (top row exact at $C$), choose $b_0\in B$ with $g(b_0)=z$. Then $g'(b(b_0))=c(g(b_0))=c(z)=0$, so $b(b_0)\in\ker g'=\mathrm{im}f'$ (bottom row exact at $B'$). Choose the unique $a_0\in A'$ with $f'(a_0)=b(b_0)$ (unique because $f'$ is injective). Set $\partial(z)=a_0+\mathrm{im}a\in\mathrm{coker}a$. *(surjectivity of $g$; commutativity; exactness at $B'$; injectivity of $f'$)*
4. *$\partial$ is well defined.* Suppose $b_1$ is another lift, $g(b_1)=z$. Then $g(b_0-b_1)=0$, so $b_0-b_1=f(w)$ for some $w\in A$ (exactness at $B$). Then $b(b_0)-b(b_1)=b(f(w))=f'(a(w))$. The corresponding $a_0$ values therefore differ by $a(w)\in\mathrm{im}a$, so they agree in $\mathrm{coker}a$. Independence of the choice of $a_0$ is automatic since $f'$ is injective. Hence $\partial$ is a well-defined homomorphism (linearity follows by making all choices additively). *(exactness at $B$; commutativity; definition of coker)*
5. *Exactness at $\ker b$.* If $x\in\ker a$, then $g(f(x))=0$ (top row exact at $B$), so $\mathrm{im}(\ker a\to\ker b)\subseteq\ker(\ker b\to\ker c)$. Conversely if $u\in\ker b$ and $g(u)=0$, then $u=f(x)$ for some $x\in A$ (exactness at $B$); and $f'(a(x))=b(f(x))=b(u)=0$, so $a(x)=0$ ($f'$ injective), i.e. $x\in\ker a$. Thus $u$ is in the image. *(exactness at $B$; injectivity of $f'$)*
6. *Exactness at $\ker c$.* If $u\in\ker b$, trace $\partial(g(u))$: a lift of $g(u)$ is $u$ itself, $b(u)=0=f'(0)$, so $\partial(g(u))=0$. Conversely if $z\in\ker c$ has $\partial(z)=0$, then in the construction $a_0\in\mathrm{im}a$, say $a_0=a(w)$; then $b(b_0)=f'(a_0)=f'(a(w))=b(f(w))$, so $b_0-f(w)\in\ker b$ and $g(b_0-f(w))=g(b_0)=z$, exhibiting $z$ in the image of $\ker b\to\ker c$. *(definitions; commutativity; exactness at $B$)*
7. *Exactness at $\mathrm{coker}a$.* For $z\in\ker c$ with $\partial(z)=a_0+\mathrm{im}a$, we have $\bar f'(\partial(z))=f'(a_0)+\mathrm{im}b=b(b_0)+\mathrm{im}b=0$, so $\bar f'\circ\partial=0$. Conversely if $a_0+\mathrm{im}a\in\ker\bar f'$, then $f'(a_0)=b(b_0)$ for some $b_0\in B$; put $z=g(b_0)$, then $c(z)=c(g(b_0))=g'(b(b_0))=g'(f'(a_0))=0$ (bottom row exact at $B'$), so $z\in\ker c$ and by construction $\partial(z)=a_0+\mathrm{im}a$. *(commutativity; exactness at $B'$)*
8. *Exactness at $\mathrm{coker}b$.* Mirror of step 5, dualized to cokernels: $\bar g'\circ\bar f'=0$ since $g'f'=0$, and a class killed by $\bar g'$ comes from $\mathrm{coker}a$ by surjectivity of $g$ and exactness of the bottom row. The argument is the formal dual of step 5 (reverse all arrows and swap kernels for cokernels). *(exactness at $B'$ and at $C$)* $\;\blacksquare$

> **Five Lemma.** In a commutative diagram with exact rows
>
> $$
> \begin{array}{ccccccccc}
> A_1 & \to & A_2 & \to & A_3 & \to & A_4 & \to & A_5\\
> \downarrow{\scriptstyle f_1} & & \downarrow{\scriptstyle f_2} & & \downarrow{\scriptstyle f_3} & & \downarrow{\scriptstyle f_4} & & \downarrow{\scriptstyle f_5}\\
> B_1 & \to & B_2 & \to & B_3 & \to & B_4 & \to & B_5
> \end{array}
> $$
>
> if $f_1$ is surjective, $f_5$ is injective, and $f_2,f_4$ are isomorphisms, then $f_3$ is an isomorphism.

**Proof.** Label the horizontal maps $\alpha_i:A_i\to A_{i+1}$ and $\beta_i:B_i\to B_{i+1}$.

1. *($f_3$ injective.)* Let $x\in\ker f_3$. Then $f_4(\alpha_3(x))=\beta_3(f_3(x))=0$, and $f_4$ injective gives $\alpha_3(x)=0$, so $x\in\ker\alpha_3=\mathrm{im}\alpha_2$ (top exact at $A_3$); write $x=\alpha_2(w)$. Then $\beta_2(f_2(w))=f_3(\alpha_2(w))=f_3(x)=0$, so $f_2(w)\in\ker\beta_2=\mathrm{im}\beta_1$; write $f_2(w)=\beta_1(v)$. Since $f_1$ is surjective, $v=f_1(u)$; then $\beta_1(f_1(u))=f_2(\alpha_1(u))$, so $f_2(w)=f_2(\alpha_1(u))$, and $f_2$ injective gives $w=\alpha_1(u)$. Hence $x=\alpha_2(w)=\alpha_2(\alpha_1(u))=0$ (top exact at $A_2$). So $\ker f_3=0$. *(injectivity of $f_4,f_2$; exactness; surjectivity of $f_1$)*
2. *($f_3$ surjective.)* Let $y\in B_3$. Then $\beta_3(y)\in B_4$; since $f_4$ is surjective, $\beta_3(y)=f_4(t)$ for some $t\in A_4$. Now $f_5(\alpha_4(t))=\beta_4(f_4(t))=\beta_4(\beta_3(y))=0$ (bottom exact at $B_4$), and $f_5$ injective gives $\alpha_4(t)=0$, so $t\in\ker\alpha_4=\mathrm{im}\alpha_3$; write $t=\alpha_3(s)$. Consider $y-f_3(s)$: $\beta_3(y-f_3(s))=f_4(t)-\beta_3(f_3(s))=f_4(t)-f_4(\alpha_3(s))=f_4(t)-f_4(t)=0$, so $y-f_3(s)\in\ker\beta_3=\mathrm{im}\beta_2$; write $y-f_3(s)=\beta_2(p)$. Since $f_2$ is surjective, $p=f_2(q)$, and $\beta_2(f_2(q))=f_3(\alpha_2(q))$, so $y-f_3(s)=f_3(\alpha_2(q))$, giving $y=f_3(s+\alpha_2(q))\in\mathrm{im}f_3$. *(surjectivity/injectivity of $f_4,f_5,f_2$; exactness)* $\;\blacksquare$

> **Worked example — the snake lemma yields $0\to\mathbb{Z}/2\to\mathbb{Z}/4\to\mathbb{Z}/2\to0$ analysis.** Apply the snake lemma to the diagram with rows $0\to\mathbb{Z}\xrightarrow{\times2}\mathbb{Z}\to\mathbb{Z}/2\to0$ (top) and the same row (bottom), with vertical maps $a=b=\times2$ on the two $\mathbb{Z}$'s and $c$ the induced map on $\mathbb{Z}/2$ (which is $0$, since $2\equiv0$). Then $\ker a=\ker b=0$, $\ker c=\mathbb{Z}/2$, $\mathrm{coker}a=\mathrm{coker}b=\mathbb{Z}/2$, $\mathrm{coker}c=\mathbb{Z}/2$. The snake sequence reads
>
> $$
> 0\to0\to\mathbb{Z}/2\xrightarrow{\partial}\mathbb{Z}/2\to\mathbb{Z}/2\to\mathbb{Z}/2\to0,
> $$
>
> and exactness forces $\partial$ to be injective. Tracing the construction of $\partial$ in step 3: lift the generator of $\ker c=\mathbb{Z}/2$ to $1\in\mathbb{Z}$ (top), apply $b=\times2$ to get $2\in\mathbb{Z}$ (bottom), pull back along $f'=\times2$ to get $1\in\mathbb{Z}$, project to $1\in\mathrm{coker}a=\mathbb{Z}/2$ — so $\partial$ sends the generator to the generator, an isomorphism. The connecting map is exactly the Bockstein homomorphism that detects $\mathbb{Z}/4$ versus $\mathbb{Z}/2\oplus\mathbb{Z}/2$.

**Pitfall.** Diagram chasing uses *elements*, which is legitimate for modules but not for an arbitrary abstract setting; §s6 explains how the same lemmas survive in any abelian category by a more careful argument. Also, the snake lemma's connecting map $\partial$ is canonical *despite* the choices made in step 3 — the well-definedness check is not a formality, it is the heart of the lemma.

<a id="s2"></a>
### Chain complexes, homology, and chain homotopy

**What & why.** A single exact sequence has no "holes." The point of homology is to study sequences that *fail* to be exact and to measure that failure. The carrier of this idea is the chain complex.

> **Definition — chain complex.**
> A **chain complex** $C_\bullet$ of $R$-modules is a family $(C_n)_{n\in\mathbb{Z}}$ together with **boundary maps** $\partial_n:C_n\to C_{n-1}$ satisfying $\partial_{n-1}\circ\partial_n=0$ for all $n$. The condition $\partial\partial=0$ says $\mathrm{im}\partial_{n+1}\subseteq\ker\partial_n$. Elements of $\ker\partial_n$ are **cycles** $Z_n$; elements of $\mathrm{im}\partial_{n+1}$ are **boundaries** $B_n$.

> **Definition — homology.**
> The **$n$-th homology** is the quotient module
>
> $$
> H_n(C_\bullet)=\ker\partial_n/\mathrm{im}\partial_{n+1}=Z_n/B_n.
> $$
>
> It measures "cycles that are not boundaries." The complex is exact at $C_n$ iff $H_n=0$; thus **homology is the precise measure of non-exactness.** A **cochain complex** is the same with arrows raised, $d^n:C^n\to C^{n+1}$, $d^{n+1}d^n=0$; its **cohomology** is $H^n=\ker d^n/\mathrm{im}d^{n-1}$.

*Worked example.* Let $C_1=\mathbb{Z}\xrightarrow{\times 2}C_0=\mathbb{Z}$, all other $C_n=0$. Then $\partial_1=\times2$, and $\partial_0=0$. Cycles in degree $0$: all of $\mathbb{Z}$ (since $\partial_0=0$). Boundaries in degree $0$: $\mathrm{im}(\times2)=2\mathbb{Z}$. So $H_0=\mathbb{Z}/2\mathbb{Z}$. In degree $1$: cycles $=\ker(\times2)=0$, so $H_1=0$. The complex "sees" the torsion $\mathbb{Z}/2$.

> **Definition — chain map.**
> A **chain map** $f_\bullet:C_\bullet\to D_\bullet$ is a family $f_n:C_n\to D_n$ commuting with boundaries: $\partial^D_n f_n=f_{n-1}\partial^C_n$. A chain map sends cycles to cycles and boundaries to boundaries, hence induces $f_*:H_n(C)\to H_n(D)$ on homology.

**Demonstration — $f_*$ is well defined.**
1. If $z\in Z_n(C)$ then $\partial^D f(z)=f(\partial^C z)=f(0)=0$, so $f(z)\in Z_n(D)$. *(chain-map condition)*
2. If $z=\partial^C w\in B_n(C)$ then $f(z)=f(\partial^C w)=\partial^D f(w)\in B_n(D)$. *(chain-map condition)*
3. Therefore $f$ maps $Z_n$ to $Z_n$ and $B_n$ to $B_n$, so the formula $f_*(z+B_n)=f(z)+B_n$ is independent of the representative — a well-defined homomorphism on $H_n$. *(quotient universal property)* $\;\blacksquare$

> **Definition — chain homotopy.**
> Two chain maps $f_\bullet,g_\bullet:C_\bullet\to D_\bullet$ are **chain homotopic** if there is a family $h_n:C_n\to D_{n+1}$ (no commutation required) with
>
> $$
> f_n-g_n=\partial^D_{n+1}h_n+h_{n-1}\partial^C_n.
> $$
>
> We write $f\simeq g$ and call $h$ a **chain homotopy**.

> **Theorem (homotopy invariance).** If $f\simeq g$ then $f_*=g_*$ on homology.

**Proof.**
1. Let $z\in Z_n(C)$, so $\partial^C z=0$. Apply the homotopy identity: $f(z)-g(z)=\partial^D h(z)+h(\partial^C z)=\partial^D h(z)+h(0)=\partial^D h(z)$. *(homotopy identity; $z$ is a cycle)*
2. Thus $f(z)-g(z)\in B_n(D)$, so $f(z)$ and $g(z)$ represent the *same* class in $H_n(D)$. *(definition of boundary and of homology class)*
3. Hence $f_*(z+B)=g_*(z+B)$ for every cycle $z$, i.e. $f_*=g_*$. $\;\blacksquare$

> **Theorem (long exact sequence of homology).** A short exact sequence of chain complexes $0\to A_\bullet\xrightarrow{f}B_\bullet\xrightarrow{g}C_\bullet\to 0$ (exact in each degree) induces a long exact sequence
>
> $$
> \cdots\to H_n(A)\xrightarrow{f_*}H_n(B)\xrightarrow{g_*}H_n(C)\xrightarrow{\partial_*}H_{n-1}(A)\to\cdots
> $$

**Proof.** Apply the snake lemma (§s1) to the commutative diagram whose two rows are the $\partial$-maps of the SES of complexes in adjacent degrees; the snake's connecting map *is* $\partial_*$, and splicing the resulting six-term exact sequences over all $n$ produces the long exact sequence. Concretely: in each degree $0\to A_n\to B_n\to C_n\to 0$ is exact, $\partial$ commutes with $f,g$, and the snake lemma yields exactness at each $H_n$ together with $\partial_*$; the verification that consecutive six-term pieces splice is the matching of the snake's $\ker\to\mathrm{coker}$ map across degrees. $\;\blacksquare$

> **Worked example — the long exact sequence in action (the pair $(D^2,S^1)$).** In algebraic topology the disk $D^2$ has the homology of a point ($H_0=\mathbb{Z}$, all higher $0$) and the circle $S^1$ has $H_0=H_1=\mathbb{Z}$. The relative chains fit into a SES of complexes $0\to C_\bullet(S^1)\to C_\bullet(D^2)\to C_\bullet(D^2,S^1)\to0$, giving the long exact sequence
>
> $$
> \cdots\to H_2(D^2,S^1)\xrightarrow{\partial_*}H_1(S^1)\xrightarrow{i_*}H_1(D^2)\to H_1(D^2,S^1)\to H_0(S^1)\to\cdots
> $$
>
> Substituting $H_1(D^2)=0$, exactness forces $\partial_*:H_2(D^2,S^1)\to H_1(S^1)=\mathbb{Z}$ to be surjective; combined with $H_2(D^2)=0$ on its left it is also injective, so $H_2(D^2,S^1)\cong\mathbb{Z}$. The connecting map "$\partial_*$" — the snake's $\partial$ — is precisely the boundary operator that detects the circle as the rim of the disk. This is the homological algebra of "the boundary of a $2$-cell is its bounding circle."

**Intuition.** Homology turns "the failure to be exact" into a computable invariant; chain homotopy is the algebraic shadow of "continuous deformation," which is why homotopy-equivalent spaces have equal homology. The long exact sequence is the workhorse: it converts a known relationship between three complexes into a single infinite exact ladder relating all their homology groups, and the connecting map carries the geometric content.

## Part B — Resolutions and derived functors

<a id="s3"></a>
### Projective and injective resolutions (existence)

**What & why.** To "derive" a functor we must first replace a module by a complex of especially simple modules that the functor handles cleanly. The simple modules are *projective* (for right-exact functors like $\otimes$) and *injective* (for left-exact functors like $\mathrm{Hom}$). This section defines them and proves resolutions always exist.

> **Definition — free module.**
> An $R$-module $F$ is **free** if it has a basis: $F\cong\bigoplus_{i\in I}R$, a direct sum of copies of $R$. Every module is a quotient of a free module: send a free module on generators of $M$ onto $M$.

> **Definition — projective module.**
> $P$ is **projective** if for every surjection $g:B\twoheadrightarrow C$ and every map $f:P\to C$ there is a **lift** $\tilde f:P\to B$ with $g\tilde f=f$. Equivalently, every surjection $B\twoheadrightarrow P$ **splits** (has a right inverse).

> **Lemma.** Every free module is projective.

**Proof.** Let $F$ have basis $(e_i)$, $g:B\twoheadrightarrow C$ surjective, $f:F\to C$. For each $i$ choose $b_i\in B$ with $g(b_i)=f(e_i)$ (possible since $g$ is surjective). Define $\tilde f(\sum r_i e_i)=\sum r_i b_i$; this is $R$-linear because $(e_i)$ is a basis, and $g\tilde f(e_i)=g(b_i)=f(e_i)$, so $g\tilde f=f$ on a basis, hence everywhere. *(surjectivity of $g$; universal property of a basis)* $\;\blacksquare$

> **Definition — injective module.**
> $E$ is **injective** if for every injection $j:A\hookrightarrow B$ and every map $f:A\to E$ there is an **extension** $\tilde f:B\to E$ with $\tilde f j=f$. (This is the projective property with all arrows reversed.)

> **Definition — resolution.**
> A **projective resolution** of $M$ is an exact sequence
>
> $$
> \cdots\to P_2\xrightarrow{d_2}P_1\xrightarrow{d_1}P_0\xrightarrow{\varepsilon}M\to 0
> $$
>
> with every $P_n$ projective. An **injective resolution** is an exact sequence $0\to M\xrightarrow{\eta}E^0\xrightarrow{d^0}E^1\to\cdots$ with every $E^n$ injective.

> **Theorem (existence of projective resolutions).** Every $R$-module $M$ has a projective (indeed free) resolution.

**Proof (explicit construction).**
1. Choose a free module $P_0$ surjecting onto $M$ via $\varepsilon:P_0\twoheadrightarrow M$ — take $P_0$ free on a generating set of $M$. By the lemma $P_0$ is projective. *(every module is a quotient of a free module)*
2. Let $K_0=\ker\varepsilon$. Choose a free module $P_1$ surjecting onto $K_0$; compose with the inclusion $K_0\hookrightarrow P_0$ to get $d_1:P_1\to P_0$ with $\mathrm{im}d_1=K_0=\ker\varepsilon$, giving exactness at $P_0$. *(same fact, applied to $K_0$)*
3. Inductively, given $d_n:P_n\to P_{n-1}$, set $K_{n}=\ker d_n$ and choose free $P_{n+1}\twoheadrightarrow K_n$; let $d_{n+1}$ be the composite $P_{n+1}\twoheadrightarrow K_n\hookrightarrow P_n$. Then $\mathrm{im}d_{n+1}=K_n=\ker d_n$, exactness at $P_n$, and $d_n d_{n+1}=0$. *(induction; every module is a quotient of a free module)*
4. The resulting complex is a free, hence projective, resolution. $\;\blacksquare$

For injective resolutions over $\mathbb{Z}$ (and any ring) the dual existence theorem holds; the key input is that *every abelian group embeds in a divisible group*, and divisible abelian groups are exactly the injective $\mathbb{Z}$-modules.

> **Theorem (injective resolutions exist over $\mathbb{Z}$).** Every abelian group $M$ embeds in an injective abelian group, hence has an injective resolution.

**Proof sketch with the load-bearing step proved.**
1. *(Baer's criterion, used as a tool.)* An abelian group $E$ is injective iff every map from an ideal $n\mathbb{Z}$ into $E$ extends to $\mathbb{Z}$; one checks this is equivalent to $E$ being **divisible** (for every $e\in E$ and $0\neq n$ there is $e'$ with $ne'=e$). *(Baer's criterion specialized to $\mathbb{Z}$)*
2. *Embedding.* Write $M$ as a quotient of a free group $\bigoplus\mathbb{Z}$; the free group embeds in $\bigoplus\mathbb{Q}$, which is divisible. A quotient of a divisible group is divisible, and a careful pushout (or the explicit $\mathrm{Hom}(\mathbb{Z},\mathbb{Q}/\mathbb{Z})$ construction) embeds $M$ into a divisible, hence injective, group $E^0$. *(divisibility is preserved under quotients; step 1)*
3. Iterate on $E^0/M$ to build $E^1,E^2,\dots$, producing the injective resolution. $\;\blacksquare$

> **Worked example — a free resolution of $\mathbb{Z}/6$ over $\mathbb{Z}$.** Follow the construction. $P_0=\mathbb{Z}$ with $\varepsilon:\mathbb{Z}\twoheadrightarrow\mathbb{Z}/6$ the reduction map; $K_0=\ker\varepsilon=6\mathbb{Z}\cong\mathbb{Z}$. Take $P_1=\mathbb{Z}$ surjecting onto $6\mathbb{Z}$ by $1\mapsto6$, so $d_1=\times6:\mathbb{Z}\to\mathbb{Z}$. Now $\ker d_1=0$, so the resolution terminates:
>
> $$
> 0\to\mathbb{Z}\xrightarrow{\times6}\mathbb{Z}\xrightarrow{\bmod6}\mathbb{Z}/6\to0.
> $$
>
> It has length $1$ — the general phenomenon that finitely generated abelian groups have free resolutions of length $\leq1$, which is why $\mathrm{Tor}_n$ and $\mathrm{Ext}^n$ vanish over $\mathbb{Z}$ for $n\geq2$ (§s4).

**Pitfall.** Projective is *not* the same as free for general rings (e.g. over $\mathbb{Z}/6\cong\mathbb{Z}/2\times\mathbb{Z}/3$ the factor $\mathbb{Z}/2$ is projective but not free); over $\mathbb{Z}$, however — and more generally over any PID — *every* projective module is free, so the two notions coincide for everything we use here. The choice of resolution is wildly non-unique (different generators, different free covers), which is exactly why the independence theorem of §s4 is indispensable: it guarantees the derived functors do not see the choice.

<a id="s4"></a>
### Derived functors — Tor and Ext, their definition and independence of the resolution

**What & why.** A functor $F$ that is only *right exact* (preserves cokernels but maybe not kernels) loses information at the left end of a SES. The **left derived functors** $L_nF$ recover that lost information. Applying this to $-\otimes_R N$ gives $\mathrm{Tor}$; dually, the **right derived functors** $R^nF$ of the left-exact $\mathrm{Hom}_R(-,N)$ give $\mathrm{Ext}$. The word "derive" is literal: we take the functor's behaviour on a *resolution* of $M$ — a complex of simple modules built in §s3 — and read off the homology of the resulting complex degree by degree. Degree $0$ returns the original functor; the higher degrees are the new information.

> **Definition — tensor product (the operation we will derive).**
> For a right $R$-module $M$ and left $R$-module $N$, the **tensor product** $M\otimes_R N$ is the abelian group generated by symbols $m\otimes n$ subject to bilinearity $(m+m')\otimes n=m\otimes n+m'\otimes n$, $m\otimes(n+n')=m\otimes n+m\otimes n'$, and $mr\otimes n=m\otimes rn$. It is **right exact**: applying $-\otimes_R N$ to $A\to B\to C\to0$ yields $A\otimes N\to B\otimes N\to C\otimes N\to 0$ exact, but the leftmost map may fail to be injective.

*Failure example.* Tensor $0\to\mathbb{Z}\xrightarrow{\times2}\mathbb{Z}\to\mathbb{Z}/2\to0$ with $N=\mathbb{Z}/2$. The map $\mathbb{Z}\otimes\mathbb{Z}/2\xrightarrow{\times2}\mathbb{Z}\otimes\mathbb{Z}/2$ becomes $\mathbb{Z}/2\xrightarrow{\times2=0}\mathbb{Z}/2$, the zero map — **not** injective. The "missing kernel" is what $\mathrm{Tor}$ will detect.

> **Definition — derived functor (left).**
> To compute $L_nF(M)$ for a right-exact functor $F$: take a projective resolution $P_\bullet\to M$, delete $M$ to get $\cdots\to P_1\to P_0\to0$, apply $F$ to get the complex $F(P_\bullet)$, and set
>
> $$
> L_nF(M)=H_n\big(F(P_\bullet)\big).
> $$
>
> Define $\mathrm{Tor}_n^R(M,N)=L_n(-\otimes_R N)(M)=H_n(P_\bullet\otimes_R N)$.

> **Definition — derived functor (right) and Ext.**
> Dually, for left-exact $F$, apply $F$ to an injective resolution $M\to E^\bullet$ and set $R^nF(M)=H^n(F(E^\bullet))$. Define $\mathrm{Ext}^n_R(M,N)=R^n\mathrm{Hom}_R(-,N)(M)=H^n(\mathrm{Hom}_R(P_\bullet,N))$, using a projective resolution of $M$ in the first variable (the two recipes agree).

> **Theorem (independence of the resolution).** $L_nF(M)$ does not depend, up to canonical isomorphism, on the chosen projective resolution.

**Proof.** It rests on the *Comparison Theorem*.

1. **Comparison Theorem.** Given projective resolutions $P_\bullet\to M$ and $Q_\bullet\to M'$ and a map $\phi:M\to M'$, there is a chain map $\tilde\phi:P_\bullet\to Q_\bullet$ lifting $\phi$, unique up to chain homotopy. *Proof:* build $\tilde\phi_n$ by induction using projectivity of $P_n$ to lift through the surjection $Q_n\twoheadrightarrow\ker(Q_{n-1}\to Q_{n-2})$; uniqueness up to homotopy is the same lifting applied to the difference of two lifts, which lands in boundaries. *(projectivity lifting property of §s3)*
2. Take $M'=M$, $\phi=\mathrm{id}$, and two resolutions $P_\bullet,Q_\bullet$. Comparison gives chain maps $\tilde\phi:P\to Q$ and $\tilde\psi:Q\to P$ lifting $\mathrm{id}$. Then $\tilde\psi\tilde\phi$ and $\mathrm{id}_P$ both lift $\mathrm{id}_M$, so by uniqueness they are chain homotopic; similarly $\tilde\phi\tilde\psi\simeq\mathrm{id}_Q$. *(comparison theorem)*
3. Apply $F$. A chain homotopy $f-g=\partial h+h\partial$ maps under the additive functor $F$ to $F(f)-F(g)=F(\partial)F(h)+F(h)F(\partial)$ — still a chain homotopy. Hence $F(\tilde\phi)$ and $F(\tilde\psi)$ are mutually inverse on homology (by §s2 homotopy invariance), giving a *canonical* isomorphism $H_n(F(P))\cong H_n(F(Q))$. *(additivity of $F$; §s2 homotopy invariance)* $\;\blacksquare$

> **Computation — $\mathrm{Tor}_1^{\mathbb{Z}}(\mathbb{Z}/2,\mathbb{Z}/2)$.**
> Projective (free) resolution of $\mathbb{Z}/2$: $0\to\mathbb{Z}\xrightarrow{\times2}\mathbb{Z}\to0$ (then $\to\mathbb{Z}/2$). Tensor with $\mathbb{Z}/2$ and delete the augmentation: $0\to\mathbb{Z}/2\xrightarrow{\times2=0}\mathbb{Z}/2\to0$. Homology: $H_0=\mathbb{Z}/2$ (coker of $0$) $=\mathrm{Tor}_0=\mathbb{Z}/2\otimes\mathbb{Z}/2$; $H_1=\ker(0)/\mathrm{im}=\mathbb{Z}/2$. So $\mathrm{Tor}_1^{\mathbb{Z}}(\mathbb{Z}/2,\mathbb{Z}/2)=\mathbb{Z}/2$ — precisely the "missing kernel" from the failure example.

> **Computation — $\mathrm{Ext}^1_{\mathbb{Z}}(\mathbb{Z}/2,\mathbb{Z})$.**
> Apply $\mathrm{Hom}_{\mathbb{Z}}(-,\mathbb{Z})$ to $0\to\mathbb{Z}\xrightarrow{\times2}\mathbb{Z}\to0$: get $0\to\mathbb{Z}\xrightarrow{\times2}\mathbb{Z}\to0$ (since $\mathrm{Hom}(\mathbb{Z},\mathbb{Z})=\mathbb{Z}$ and the dual of $\times2$ is $\times2$). Cohomology: $H^0=\ker(\times2)=0=\mathrm{Ext}^0=\mathrm{Hom}(\mathbb{Z}/2,\mathbb{Z})$; $H^1=\mathbb{Z}/2\mathbb{Z}=\mathrm{Ext}^1$. So $\mathrm{Ext}^1_{\mathbb{Z}}(\mathbb{Z}/2,\mathbb{Z})=\mathbb{Z}/2$.

**Key facts (each provable as above).** $\mathrm{Tor}_0=\otimes$, $\mathrm{Ext}^0=\mathrm{Hom}$; over $\mathbb{Z}$, $\mathrm{Tor}_n=\mathrm{Ext}^n=0$ for $n\geq2$ (because every subgroup of a free abelian group is free, so resolutions have length $1$); a SES in either variable yields a **long exact sequence** of $\mathrm{Tor}$'s or $\mathrm{Ext}$'s (apply §s2's long exact sequence to the resolution complexes).

> **Theorem (long exact sequence of $\mathrm{Tor}$).** A short exact sequence $0\to A'\to A\to A''\to0$ of right $R$-modules and a fixed left module $N$ produce a long exact sequence
>
> $$
> \cdots\to\mathrm{Tor}_1(A',N)\to\mathrm{Tor}_1(A,N)\to\mathrm{Tor}_1(A'',N)\to A'\otimes N\to A\otimes N\to A''\otimes N\to0.
> $$

**Derivation.**
1. Choose projective resolutions $P'_\bullet\to A'$ and $P''_\bullet\to A''$. The **Horseshoe Lemma** (standard; stated without proof) says: given projective resolutions of the two outer terms $A',A''$ of a SES $0\to A'\to A\to A''\to0$, one can assemble a projective resolution $P_\bullet\to A$ of the middle term with $P_n=P'_n\oplus P''_n$, fitting into a degreewise-split SES of complexes $0\to P'_\bullet\to P_\bullet\to P''_\bullet\to0$. *(Horseshoe Lemma; degreewise splitting because $P''_n$ is projective)*
2. Tensor with $N$. Because the SES of complexes splits in each degree, $0\to P'_\bullet\otimes N\to P_\bullet\otimes N\to P''_\bullet\otimes N\to0$ is still short exact. *(a degreewise-split SES survives any additive functor)*
3. Apply the long exact homology sequence of §s2. Its homology groups are by definition the $\mathrm{Tor}_n$, and the right end $\mathrm{Tor}_0=\otimes$ closes with $\to A''\otimes N\to0$ by right-exactness of $\otimes$. *(§s2 long exact sequence; $\mathrm{Tor}_0=\otimes$)* $\;\blacksquare$

> **Theorem (balancing of $\mathrm{Tor}$).** $\mathrm{Tor}_n^R(M,N)$ can be computed by resolving *either* variable: $H_n(P^M_\bullet\otimes N)\cong H_n(M\otimes Q^N_\bullet)$ where $P^M_\bullet\to M$ and $Q^N_\bullet\to N$ are projective resolutions.

**Derivation.** Form the double complex $P^M_\bullet\otimes Q^N_\bullet$ with $C_{p,q}=P^M_p\otimes Q^N_q$ and the two tensored differentials. Run the two double-complex spectral sequences of §s9. Because each $P^M_p$ is projective (flat), tensoring the resolution $Q^N_\bullet\to N$ with $P^M_p$ stays exact, so one spectral sequence collapses to $H_n(P^M_\bullet\otimes N)$; by symmetry the other collapses to $H_n(M\otimes Q^N_\bullet)$. Both converge to $H_n(\mathrm{Tot})$, so the two are isomorphic. *(degenerate double-complex spectral sequence of §s9; flatness of projectives)* $\;\blacksquare$

> **Interpretation — $\mathrm{Ext}^1$ classifies extensions.** An **extension** of $A$ by $B$ is a SES $0\to B\to E\to A\to0$; two are *equivalent* if related by an isomorphism of the middle term fixing $B$ and $A$. The set of equivalence classes is in natural bijection with $\mathrm{Ext}^1_R(A,B)$, with the **split** extension $E=A\oplus B$ corresponding to $0$. *Example:* $\mathrm{Ext}^1_{\mathbb{Z}}(\mathbb{Z}/2,\mathbb{Z})=\mathbb{Z}/2$ has two classes — the split extension $0\to\mathbb{Z}\to\mathbb{Z}\oplus\mathbb{Z}/2\to\mathbb{Z}/2\to0$ (class $0$) and the nonsplit $0\to\mathbb{Z}\xrightarrow{\times2}\mathbb{Z}\to\mathbb{Z}/2\to0$ (the nonzero class). The nonvanishing of $\mathrm{Ext}^1$ is exactly the existence of a genuinely twisted extension.

<a id="s5"></a>
### The universal coefficient theorem and the Künneth formula (derive)

**What & why.** In topology one computes homology with integer coefficients, then wants homology or cohomology with other coefficients, and the homology of a product space. Both answers are governed by $\mathrm{Tor}$ and $\mathrm{Ext}$. We derive both. We work with a chain complex $C_\bullet$ of **free** abelian groups (the case of singular chains), which is what makes the splittings below possible.

> **Universal Coefficient Theorem (homology).** Let $C_\bullet$ be a chain complex of free abelian groups and $G$ an abelian group. There is a short exact sequence, natural in $G$,
>
> $$
> 0\to H_n(C)\otimes G\to H_n(C\otimes G)\to \mathrm{Tor}_1^{\mathbb{Z}}(H_{n-1}(C),G)\to 0,
> $$
>
> and it splits (non-naturally), so $H_n(C\otimes G)\cong (H_n(C)\otimes G)\oplus\mathrm{Tor}_1^{\mathbb{Z}}(H_{n-1}(C),G)$.

**Derivation.**
1. Let $Z_n,B_n\subseteq C_n$ be cycles and boundaries. Since $C_n$ is free abelian and $B_{n-1}\subseteq C_{n-1}$ is a subgroup of a free abelian group, $B_{n-1}$ is free. The SES $0\to Z_n\to C_n\xrightarrow{\partial}B_{n-1}\to0$ therefore **splits** ($B_{n-1}$ free $\Rightarrow$ projective $\Rightarrow$ the surjection splits). *(subgroups of free abelian groups are free; §s3 projectivity)*
2. View $Z_\bullet$ and $B_\bullet$ as chain complexes with **zero** differentials. The split SES of step 1 is a SES of chain complexes $0\to Z_\bullet\to C_\bullet\xrightarrow{\partial} B_{\bullet-1}\to0$, where $B_{\bullet-1}$ is $B$ shifted. *(splitting degreewise)*
3. Tensor with $G$. Because each term is free (hence the SES splits), the tensored sequence $0\to Z_\bullet\otimes G\to C_\bullet\otimes G\to B_{\bullet-1}\otimes G\to0$ is still short exact. *(a split SES stays split, hence exact, after applying any additive functor)*
4. Its long exact homology sequence (§s2) has connecting map equal to the inclusion $B_n\hookrightarrow Z_n$ tensored with $G$, namely $i\otimes\mathrm{id}_G:B_n\otimes G\to Z_n\otimes G$. (This identification is exactly the snake-lemma connecting map of §s1 applied to the split SES of step 3: since $Z_\bullet$ and $B_\bullet$ carry zero differentials, the only surviving differential after tensoring is the inclusion $i:B_n\hookrightarrow Z_n$ of boundaries into cycles, and $\partial_*=i\otimes\mathrm{id}_G$.) Splicing yields, for each $n$,
> $$
> 0\to\mathrm{coker}(i\otimes\mathrm{id})_n\to H_n(C\otimes G)\to\ker(i\otimes\mathrm{id})_{n-1}\to0.
> $$
*(long exact sequence; identifying the connecting map)*
5. Now use the free resolution $0\to B_n\xrightarrow{i}Z_n\to H_n(C)\to0$ of $H_n(C)$ (it is a resolution by free groups because $B_n,Z_n$ are free). Tensoring with $G$ and taking homology: $\mathrm{coker}(i\otimes\mathrm{id})=H_n(C)\otimes G$ and $\ker(i\otimes\mathrm{id})=\mathrm{Tor}_1^{\mathbb{Z}}(H_n(C),G)$, by the very definition of $\mathrm{Tor}$ from this length-one free resolution. *(definition of $\otimes$ as $\mathrm{Tor}_0$ and $\mathrm{Tor}_1$, §s4)*
6. Substituting into step 4 gives the stated SES. **Splitting:** since $Z_n$ is a direct summand of $C_n$ (step 1), choose a retraction $C_n\to Z_n$; it induces $H_n(C\otimes G)\to H_n(C)\otimes G$ splitting the first map. $\;\blacksquare$

> **Universal Coefficient Theorem (cohomology).** With $C_\bullet$ free, there is a split SES
>
> $$
> 0\to\mathrm{Ext}^1_{\mathbb{Z}}(H_{n-1}(C),G)\to H^n(\mathrm{Hom}(C,G))\to\mathrm{Hom}(H_n(C),G)\to0.
> $$
>
> *Derivation:* identical to the above with $\mathrm{Hom}(-,G)$ in place of $\otimes G$; the connecting maps now produce $\mathrm{Hom}=\mathrm{Ext}^0$ and $\mathrm{Ext}^1$ from the same length-one free resolution. *(dualize steps 1–6)*

> **Künneth Formula.** For free chain complexes $C_\bullet,D_\bullet$ of abelian groups there is a split SES
>
> $$
> 0\to\bigoplus_{i+j=n}H_i(C)\otimes H_j(D)\to H_n(C\otimes D)\to\bigoplus_{i+j=n-1}\mathrm{Tor}_1^{\mathbb{Z}}(H_i(C),H_j(D))\to0.
> $$

**Derivation.**
1. As in UCT step 1, split each $0\to Z_i(C)\to C_i\to B_{i-1}(C)\to0$ so $C_\bullet$ decomposes; treat $C_\bullet$ as built from the free complexes $Z_\bullet$ and $B_\bullet$ with zero differential. *(subgroups of free abelian groups are free; splitting)*
2. The SES $0\to Z_\bullet\to C_\bullet\to B_{\bullet-1}\to0$ tensored over $\mathbb{Z}$ with the *complex* $D_\bullet$ stays short exact (terms are free). *(split SES survives $\otimes$)*
3. Take the long exact homology sequence. Using $H_*(Z_\bullet\otimes D)=\bigoplus Z_i(C)\otimes H_j(D)$ and likewise for $B$ (zero differentials make homology the tensor termwise), the connecting map is again $i\otimes\mathrm{id}$, the inclusion $B_i\hookrightarrow Z_i$. *(homology of a zero-differential complex; identification of connecting map)*
4. The cokernel and kernel of $i\otimes\mathrm{id}_{H_j(D)}$ are $H_i(C)\otimes H_j(D)$ and $\mathrm{Tor}_1(H_i(C),H_j(D))$ respectively, by the length-one free resolution $0\to B_i\to Z_i\to H_i(C)\to0$ (§s4). Summing over $i+j=n$ and $i+j=n-1$ gives the formula; the split comes from the retractions as before. $\;\blacksquare$

> **Worked example — homology of $\mathbb{RP}^2$ with coefficients.** Integral homology: $H_0=\mathbb{Z},\ H_1=\mathbb{Z}/2,\ H_2=0$. With $G=\mathbb{Z}/2$: UCT gives $H_2(\mathbb{RP}^2;\mathbb{Z}/2)\cong(H_2\otimes\mathbb{Z}/2)\oplus\mathrm{Tor}_1(H_1,\mathbb{Z}/2)=0\oplus\mathrm{Tor}_1(\mathbb{Z}/2,\mathbb{Z}/2)=\mathbb{Z}/2$. So even though $H_2(\mathbb{RP}^2;\mathbb{Z})=0$, the mod-2 homology in degree $2$ is nonzero — the $\mathrm{Tor}$ term *creates* a class. This is the famous "extra" $\mathbb{Z}/2$ in $H_*(\mathbb{RP}^2;\mathbb{Z}/2)$.

> **Worked example — cohomology of $\mathbb{RP}^2$ over $\mathbb{Z}$ via the Ext term.** The cohomology UCT gives $H^n(\mathbb{RP}^2;\mathbb{Z})\cong\mathrm{Hom}(H_n,\mathbb{Z})\oplus\mathrm{Ext}^1(H_{n-1},\mathbb{Z})$. In degree $2$: $\mathrm{Hom}(H_2,\mathbb{Z})=\mathrm{Hom}(0,\mathbb{Z})=0$ and $\mathrm{Ext}^1(H_1,\mathbb{Z})=\mathrm{Ext}^1(\mathbb{Z}/2,\mathbb{Z})=\mathbb{Z}/2$, so $H^2(\mathbb{RP}^2;\mathbb{Z})=\mathbb{Z}/2$. In degree $1$: $\mathrm{Hom}(\mathbb{Z}/2,\mathbb{Z})=0$ and $\mathrm{Ext}^1(\mathbb{Z},\mathbb{Z})=0$, so $H^1=0$. Cohomology *shifts* the torsion of homology up by one degree — the signature of the $\mathrm{Ext}$ term.

> **The cross product and the Künneth map.** The first map in the Künneth SES, $H_i(C)\otimes H_j(D)\to H_{i+j}(C\otimes D)$, is the **homology cross product** $\alpha\otimes\beta\mapsto\alpha\times\beta$, sending a pair of cycle classes to the class of their tensor. When all groups are free (e.g. coefficients in a field $k$), the $\mathrm{Tor}$ term vanishes and Künneth becomes the clean isomorphism $H_n(C\otimes D)\cong\bigoplus_{i+j=n}H_i(C)\otimes H_j(D)$. *Example over a field:* $H_*(T^2;k)=H_*(S^1;k)\otimes H_*(S^1;k)$, giving Betti numbers $1,2,1$ for the torus — two independent loops and one $2$-cell.

## Part C — Categorical language and double complexes

<a id="s6"></a>
### Categories, functors, natural transformations, and abelian categories (a working introduction)

**What & why.** Everything above used phrases like "naturally" and "functor." Category theory makes these precise and lets the snake/five lemmas and derived functors live in a setting beyond modules (sheaves, complexes themselves). We give just enough to use.

> **Definition — category.**
> A **category** $\mathcal{C}$ consists of a collection of **objects**; for each ordered pair $(X,Y)$ a set of **morphisms** $\mathrm{Hom}(X,Y)$; a composition $\mathrm{Hom}(Y,Z)\times\mathrm{Hom}(X,Y)\to\mathrm{Hom}(X,Z)$, $(g,f)\mapsto g\circ f$, that is associative; and for each $X$ an identity $\mathrm{id}_X$ with $\mathrm{id}_Y\circ f=f=f\circ\mathrm{id}_X$. *Examples:* $\mathbf{Set}$ (sets and functions), $R\text{-}\mathbf{Mod}$ ($R$-modules and homomorphisms), $\mathbf{Top}$ (spaces and continuous maps).

> **Definition — functor.**
> A **functor** $F:\mathcal{C}\to\mathcal{D}$ assigns to each object $X$ an object $F(X)$ and to each morphism $f:X\to Y$ a morphism $F(f):F(X)\to F(Y)$ with $F(g\circ f)=F(g)\circ F(f)$ and $F(\mathrm{id}_X)=\mathrm{id}_{F(X)}$. A **contravariant** functor reverses arrows: $F(f):F(Y)\to F(X)$. *Examples:* homology $H_n:\mathbf{Top}\to\mathbf{Ab}$ is a (covariant) functor; $\mathrm{Hom}_R(-,N)$ is contravariant.

> **Definition — natural transformation.**
> Given functors $F,G:\mathcal{C}\to\mathcal{D}$, a **natural transformation** $\eta:F\Rightarrow G$ assigns to each object $X$ a morphism $\eta_X:F(X)\to G(X)$ such that for every $f:X\to Y$ the square commutes: $G(f)\circ\eta_X=\eta_Y\circ F(f)$. "Natural" in the UCT means exactly this. If each $\eta_X$ is an isomorphism, $\eta$ is a **natural isomorphism**.

*Worked example.* The map $\eta_M:M\to M^{**}=\mathrm{Hom}(\mathrm{Hom}(M,k),k)$, $\eta_M(m)(\phi)=\phi(m)$, is a natural transformation from the identity functor to the double-dual functor on vector spaces; the square commutes because for linear $f:M\to N$, $f^{**}\circ\eta_M=\eta_N\circ f$ by direct substitution. On finite-dimensional spaces it is a natural isomorphism.

> **Definition — abelian category.**
> An **abelian category** is a category where (i) $\mathrm{Hom}$-sets are abelian groups and composition is bilinear, (ii) there is a zero object and all finite direct sums exist, (iii) every morphism has a kernel and cokernel, and (iv) every monomorphism is the kernel of its cokernel and every epimorphism is the cokernel of its kernel. $R\text{-}\mathbf{Mod}$ is the prototype; sheaves of abelian groups form another.

> **Theorem (Freyd–Mitchell embedding, stated).** Every small abelian category embeds, exactly, as a full subcategory of $R\text{-}\mathbf{Mod}$ for some ring $R$.

**Consequence (why diagram chasing is legal in any abelian category).** Because the embedding is exact and full, any statement provable by chasing *elements* in $R\text{-}\mathbf{Mod}$ — the snake lemma, the five lemma, the long exact sequence — holds in every abelian category. We may therefore "pretend objects have elements." *(Freyd–Mitchell)*

> **Definition — adjoint functors.**
> Functors $F:\mathcal{C}\to\mathcal{D}$ and $G:\mathcal{D}\to\mathcal{C}$ are an **adjoint pair** ($F$ left adjoint to $G$) if there is a natural isomorphism
>
> $$
> \mathrm{Hom}_{\mathcal{D}}(F(X),Y)\cong\mathrm{Hom}_{\mathcal{C}}(X,G(Y))
> $$
>
> for all $X,Y$. The prototype is the **tensor–Hom adjunction** $\mathrm{Hom}(M\otimes_R N,\,P)\cong\mathrm{Hom}\big(M,\mathrm{Hom}_R(N,P)\big)$.

> **Why exactness behaviour is forced.** A left adjoint preserves all *colimits* (in particular cokernels), hence is **right exact** — this is precisely why $\otimes$ (a left adjoint) is right exact and needs left-derived functors $\mathrm{Tor}$. A right adjoint preserves all *limits* (kernels), hence is **left exact** — why $\mathrm{Hom}(-,N)$ and $(-)^G$ are left exact and need right-derived functors $\mathrm{Ext}$ and $H^*(G;-)$. The entire $\mathrm{Tor}$/$\mathrm{Ext}$ dichotomy is the shadow of this single adjunction fact. *(adjoints preserve (co)limits)*

**Demonstration — a left adjoint $F$ is right exact.**
1. Right-exactness means: applied to $A\to B\to C\to0$, the result $F(A)\to F(B)\to F(C)\to0$ is exact, i.e. $F(C)$ is the cokernel of $F(A)\to F(B)$. *(definition of right exact)*
2. A cokernel is a colimit (the coequalizer of $A\to B$ and $0$). *(cokernel = colimit)*
3. Left adjoints preserve colimits: $\mathrm{Hom}(F(\mathrm{colim}),Y)\cong\mathrm{Hom}(\mathrm{colim},G(Y))\cong\lim\mathrm{Hom}(-,G(Y))\cong\lim\mathrm{Hom}(F(-),Y)\cong\mathrm{Hom}(\mathrm{colim}F(-),Y)$, and Yoneda then identifies $F(\mathrm{colim})=\mathrm{colim}F(-)$. So $F$ sends the cokernel to a cokernel, which is exactly right-exactness. *(adjunction; the contravariant $\mathrm{Hom}$ turns colimits into limits; Yoneda)* $\;\blacksquare$

**Pitfall.** A morphism can be both mono and epi without being an isomorphism in a general category (e.g. $\mathbb{Z}\hookrightarrow\mathbb{Q}$ in the category of rings); abelian categories are precisely the setting where mono + epi $\Rightarrow$ iso, which is what diagram lemmas silently use.

<a id="s7"></a>
### Double complexes and the total complex

**What & why.** Many constructions are naturally indexed by *two* integers (rows and columns). Packaging them as a double complex and then collapsing to a single **total complex** is the technical bridge to spectral sequences.

> **Definition — double complex.**
> A **double complex** $C_{\bullet\bullet}=(C_{p,q})$ is a grid of modules with horizontal maps $d^h:C_{p,q}\to C_{p-1,q}$ and vertical maps $d^v:C_{p,q}\to C_{p,q-1}$ satisfying
>
> $$
> d^h d^h=0,\qquad d^v d^v=0,\qquad d^h d^v + d^v d^h = 0.
> $$
>
> (The sign convention $d^hd^v+d^vd^h=0$ — anticommuting — is what makes the total differential square to zero; some authors use commuting squares and insert a sign $(-1)^p$ instead.)

> **Definition — total complex.**
> The **total complex** $\mathrm{Tot}(C)_\bullet$ has
>
> $$
> \mathrm{Tot}(C)_n=\bigoplus_{p+q=n}C_{p,q},\qquad D=d^h+d^v.
> $$

> **Lemma.** $D\circ D=0$, so $\mathrm{Tot}(C)$ is a chain complex.

**Proof.**
1. Expand $D^2=(d^h+d^v)(d^h+d^v)=d^hd^h+d^hd^v+d^vd^h+d^vd^v$. *(distributivity)*
2. The first and last terms vanish ($d^hd^h=0$, $d^vd^v=0$). *(double-complex axioms)*
3. The middle two terms are $d^hd^v+d^vd^h=0$ by the anticommutation axiom. *(double-complex axiom)*
4. Hence $D^2=0$. $\;\blacksquare$

*Worked example.* Take the double complex with one nonzero row, $\cdots\to C_{1,0}\to C_{0,0}$. Then $\mathrm{Tot}$ is just that row, and $H_n(\mathrm{Tot})$ is the ordinary homology of the row. More interestingly, a $2\times2$ square $C_{1,1}\to C_{1,0}$, $C_{1,1}\to C_{0,1}$, etc., totalizes to $C_{1,1}\xrightarrow{(d^h,d^v)}C_{1,0}\oplus C_{0,1}\xrightarrow{d^v - d^h}C_{0,0}$, whose middle homology is exactly what a $2$-page spectral sequence will compute in §s9.

> **Worked example — iterated homology can disagree with total homology.** Consider the $2\times2$ first-quadrant double complex (entries at $(0,0),(1,0),(0,1),(1,1)$) all equal to $\mathbb{Z}$, with both nonzero horizontal maps and both nonzero vertical maps the identity, signs arranged so the square anticommutes. Take vertical homology first: each column $\mathbb{Z}\xrightarrow{\mathrm{id}}\mathbb{Z}$ is exact, so $H^v=0$ everywhere, hence "$H^h(H^v)=0$." Now compute $H_*(\mathrm{Tot})$ directly: $\mathrm{Tot}_2=C_{1,1}=\mathbb{Z}$, $\mathrm{Tot}_1=C_{1,0}\oplus C_{0,1}=\mathbb{Z}^2$, $\mathrm{Tot}_0=C_{0,0}=\mathbb{Z}$, with $D_2=(\mathrm{id},\mathrm{id})$ injective and $D_1=(\mathrm{id},-\mathrm{id})$ surjective onto $\mathbb{Z}$ with kernel the anti-diagonal $=\mathrm{im}D_2$. So $H_*(\mathrm{Tot})=0$ too — here they agree because the complex is acyclic. Perturb one map to $\times2$ and the two iterated homologies and the total homology will differ, with the discrepancy recorded by a nonzero $d^2$ on the $E^2$ page (§s9). This is the precise sense in which the spectral sequence "corrects" naive iterated homology.

**Two ways to take homology.** One can first take homology along columns (using $d^v$), then along rows (using the induced $d^h$), or vice versa. The two answers usually differ from each other and from $H_*(\mathrm{Tot})$. The spectral sequence is the precise machine relating these "iterated homologies" to $H_*(\mathrm{Tot})$: each starts from one of the iterated homologies on its $E^2$ page and converges to $H_*(\mathrm{Tot})$, so the differentials measure exactly the gap.

## Part D — Spectral sequences

<a id="s8"></a>
### Spectral sequences — pages, differentials, and convergence (the definition made concrete)

**What & why.** A spectral sequence is a sequence of two-dimensional grids ("pages"), each obtained from the last by taking homology, designed to compute a hard homology in successive approximations. We give the bare definition, then make every word concrete.

> **Definition — (homological) spectral sequence.**
> A **spectral sequence** (of $R$-modules, starting at page $r_0$) is a family
>
> $$
> \big\{E^r_{p,q},\ d^r:E^r_{p,q}\to E^r_{p-r,\,q+r-1}\big\}_{r\geq r_0}
> $$
>
> such that each $d^r$ satisfies $d^r\circ d^r=0$, together with isomorphisms
>
> $$
> E^{r+1}_{p,q}\cong H_{p,q}(E^r)=\frac{\ker\big(d^r:E^r_{p,q}\to E^r_{p-r,q+r-1}\big)}{\mathrm{im}\big(d^r:E^r_{p+r,q-r+1}\to E^r_{p,q}\big)}.
> $$
>
> Thus each page is the homology of the previous page with respect to its differential $d^r$. The bidegree of $d^r$ is $(-r,\,r-1)$: as $r$ grows the differentials get "longer and flatter."

> **Definition — the limit page $E^\infty$.**
> Fix $(p,q)$. As $r$ increases, $E^r_{p,q}$ is a subquotient of the previous one. In the **first-quadrant** case ($E^r_{p,q}=0$ unless $p,q\geq0$), for each fixed $(p,q)$ both the incoming and outgoing differentials eventually point outside the quadrant, so $d^r=0$ in and out of position $(p,q)$ for all large $r$. Then $E^{r}_{p,q}=E^{r+1}_{p,q}=\cdots$ stabilizes; the common value is $E^\infty_{p,q}$.

> **Definition — convergence.**
> The spectral sequence **converges** to a graded module $H_\bullet$ (written $E^r_{p,q}\Rightarrow H_{p+q}$) if $H_n$ carries a filtration $0=F_{-1}\subseteq F_0\subseteq\cdots\subseteq F_n=H_n$ with isomorphisms
>
> $$
> E^\infty_{p,q}\cong F_p H_{p+q}/F_{p-1}H_{p+q}.
> $$
>
> In words: the limit page is the **associated graded** of a filtration on the answer. Recovering $H_n$ from the $E^\infty_{p,q}$ on the anti-diagonal $p+q=n$ is an **extension problem** (one must reassemble the pieces), which can have several solutions.

**Concrete reading guide.**
1. Draw the grid with $p$ horizontal, $q$ vertical. Page $E^2$ usually has an interpretable entry (e.g. $H_p(\text{base};H_q(\text{fiber}))$ in §s10).
2. $d^2$ goes two left, one up: $(p,q)\to(p-2,q+1)$. Take homology to get $E^3$.
3. $d^3$ goes three left, two up; etc. Keep going until differentials die.
4. Read $E^\infty$ along anti-diagonals $p+q=n$; solve the extension problem for $H_n$.

> **Worked example — a two-column spectral sequence collapses to a long exact sequence.** Suppose $E^2_{p,q}=0$ except for columns $p=0$ and $p=1$. Then $d^2:(p,q)\to(p-2,q+1)$ always lands in a zero column, so $d^2=0$ and $E^2=E^\infty$. The filtration on $H_n$ has only two steps, giving SES $0\to E^\infty_{0,n}\to H_n\to E^\infty_{1,n-1}\to0$. Splicing these across all $n$ yields a long exact sequence — showing the LES is the simplest nontrivial spectral sequence.

> **Worked example — solving an extension problem.** Suppose along the anti-diagonal $p+q=2$ the limit page gives $E^\infty_{0,2}=\mathbb{Z}/2$ and $E^\infty_{2,0}=\mathbb{Z}/2$, all other entries on that diagonal zero. Convergence supplies a filtration $0\subseteq F_0H_2\subseteq F_2H_2=H_2$ with $F_0H_2=E^\infty_{0,2}=\mathbb{Z}/2$ and $H_2/F_0H_2=E^\infty_{2,0}=\mathbb{Z}/2$. Thus $H_2$ is an extension $0\to\mathbb{Z}/2\to H_2\to\mathbb{Z}/2\to0$, classified (§s4) by $\mathrm{Ext}^1(\mathbb{Z}/2,\mathbb{Z}/2)=\mathbb{Z}/2$: either $H_2=\mathbb{Z}/2\oplus\mathbb{Z}/2$ or $H_2=\mathbb{Z}/4$. The spectral sequence alone cannot decide; this is the **extension problem**, and resolving it (here, knowing the ring structure or a Bockstein) is the price of the technique.

**Pitfall.** $E^\infty$ gives only the *associated graded* of $H_n$, not $H_n$ itself. If the pieces are e.g. $\mathbb{Z}/2$ and $\mathbb{Z}/2$, the answer might be $\mathbb{Z}/4$ or $\mathbb{Z}/2\oplus\mathbb{Z}/2$; resolving this requires extra input. Also "convergence" needs the filtration to be exhaustive and bounded — automatic in the first-quadrant case, not in general. A second common error is forgetting the bidegree: $d^r$ has bidegree $(-r,r-1)$ in homological indexing but $(r,1-r)$ in cohomological (upper) indexing — the page two cohomology differential $d_2:E_2^{p,q}\to E_2^{p+2,q-1}$ goes two *right*, one *down*, as in the LHS five-term sequence of §s11.

<a id="s9"></a>
### The spectral sequence of a filtered complex and of a double complex (derive)

**What & why.** Spectral sequences are not pulled from thin air — every one comes from a *filtered complex*. We construct it and prove the pages are successive homologies. The double-complex spectral sequence is then the special case where the filtration is by columns.

> **Definition — filtered complex.**
> A **filtration** of a chain complex $(C_\bullet,D)$ is a nested family of subcomplexes $\cdots\subseteq F_{p-1}C\subseteq F_pC\subseteq F_{p+1}C\subseteq\cdots$ with $D(F_pC)\subseteq F_pC$. It is **bounded** if for each $n$ there are $s<t$ with $F_sC_n=0$ and $F_tC_n=C_n$.

> **Theorem (spectral sequence of a filtered complex).** A bounded filtration on $C_\bullet$ determines a spectral sequence with
>
> $$
> E^0_{p,q}=F_pC_{p+q}/F_{p-1}C_{p+q},\qquad E^1_{p,q}=H_{p+q}\big(F_pC/F_{p-1}C\big),
> $$
>
> converging to $H_{p+q}(C)$ with the filtration induced by $F_\bullet$.

**Derivation (the exact-couple construction).**
1. *Set up groups.* For each $p$ the inclusion $F_{p-1}C\hookrightarrow F_pC$ gives a SES of complexes $0\to F_{p-1}C\to F_pC\to F_pC/F_{p-1}C\to0$, hence (by §s2) a long exact sequence in homology. Define
> $$
> A_{p,q}=H_{p+q}(F_pC),\qquad E^1_{p,q}=H_{p+q}(F_pC/F_{p-1}C).
> $$
*(long exact sequence of a SES of complexes, §s2)*
2. *The exact couple.* The long exact sequences assemble into a single diagram of maps $i:A_{p-1}\to A_p$ (induced by inclusion), $j:A_p\to E^1$ (the quotient map), $k:E^1\to A_{p-1}$ (the connecting map), forming an **exact couple**: exact at each of $A,E,A$. *(exactness of each LES)*
3. *Derive the couple.* Define $d^1=j\circ k:E^1\to E^1$. Then $d^1d^1=jk\,jk=j(kj)k=0$ because $kj=0$ by exactness at $A$. Set $E^2=\ker d^1/\mathrm{im}d^1$ and replace $A$ by $iA$; one checks the new triple $(iA,E^2,\dots)$ is again an exact couple — the **derived couple**. *(exactness at $A$ gives $kj=0$)*
4. *Iterate.* The $r$-th derived couple has $E^r$ and differential $d^r=j^{(r)}k^{(r)}$ of bidegree $(-r,r-1)$, and $E^{r+1}=H(E^r,d^r)$ by construction. This is exactly the data of a spectral sequence (§s8). *(induction: derive the couple $r$ times)*
5. *Convergence.* Boundedness makes the filtration on each $H_n(C)$ finite, so $E^r$ stabilizes to $E^\infty$, and tracking the derived couples identifies $E^\infty_{p,q}=F_pH_{p+q}(C)/F_{p-1}H_{p+q}(C)$. *(bounded filtration $\Rightarrow$ stabilization, §s8)* $\;\blacksquare$

> **Corollary (double-complex spectral sequences).** A first-quadrant double complex $C_{\bullet\bullet}$ gives **two** spectral sequences converging to $H_*(\mathrm{Tot}\,C)$:
>
> $$
> {}^{I}\!E^2_{p,q}=H^h_p\big(H^v_q(C)\big)\ \Rightarrow\ H_{p+q}(\mathrm{Tot}\,C),\qquad
> {}^{II}\!E^2_{p,q}=H^v_p\big(H^h_q(C)\big)\ \Rightarrow\ H_{p+q}(\mathrm{Tot}\,C).
> $$

**Derivation.** Filter $\mathrm{Tot}\,C$ by columns: $F_p(\mathrm{Tot}\,C)_n=\bigoplus_{i\leq p}C_{i,n-i}$. This is a bounded filtration (first-quadrant), so the filtered-complex theorem applies. On the $E^0$ page the only surviving differential is the vertical $d^v$ (the horizontal part raises filtration), so $E^1={}H^v(C)$; the induced $d^1$ is the horizontal map, so $E^2=H^h(H^v(C))$ — the first spectral sequence. Filtering by rows instead gives the second. Both converge to $H_*(\mathrm{Tot})$ because both arise from bounded filtrations of the *same* complex. *(filtered-complex theorem; identification of $d^0,d^1$ with $d^v,d^h$)* $\;\blacksquare$

> **Worked example — a degenerate double complex.** If a first-quadrant double complex has exact columns except in row $q=0$, then $H^v_q(C)=0$ for $q>0$, so ${}^IE^2$ is concentrated in row $0$: ${}^IE^2_{p,0}=H^h_p(\text{the row of column-homologies})$, all higher rows zero. Then every $d^r$ ($r\geq2$) is zero (source or target lies in a zero row), so $E^2=E^\infty$ and $H_n(\mathrm{Tot}\,C)\cong H^h_n(H^v_0(C))$. This "collapse at $E^2$" is the workhorse behind many comparison theorems (e.g. that two resolutions compute the same derived functor — the balancing of $\mathrm{Tor}$).

> **Edge maps.** A first-quadrant spectral sequence always has two canonical maps to and from its target, the **edge homomorphisms**. Along the bottom row, the composite $H_n(\mathrm{Tot})\twoheadrightarrow E^\infty_{n,0}\hookrightarrow E^2_{n,0}$ is a natural map $H_n\to E^2_{n,0}$; along the left column, $E^2_{0,n}\twoheadrightarrow E^\infty_{0,n}\hookrightarrow H_n(\mathrm{Tot})$. *Derivation that they are well defined:* $E^\infty_{n,0}$ is a *quotient* of $E^2_{n,0}$ because all incoming differentials $d^r:E^r_{n+r,1-r}\to E^r_{n,0}$ vanish (their source is below the first quadrant), so only outgoing differentials act, leaving $E^\infty_{n,0}$ a subquotient that is in fact a quotient of $E^2_{n,0}$; dually $E^\infty_{0,n}$ is a *sub* of $E^2_{0,n}$. The convergence filtration then puts $E^\infty_{n,0}$ at the top quotient and $E^\infty_{0,n}$ at the bottom subobject of $H_n$. *(first-quadrant vanishing of incoming/outgoing differentials; convergence filtration of §s8)* These edge maps are what specialize, in §s11, to the **inflation** $H^p(Q;M^N)\to H^p(G;M)$ and **restriction** $H^q(G;M)\to H^q(N;M)^Q$ maps.

<a id="s10"></a>
### The Leray–Serre spectral sequence of a fibration — a worked computation

**What & why.** The single most-used spectral sequence in topology computes the homology of the total space of a fibration from the homology of its base and fiber. We state it and run a full computation.

> **Definition — fibration (Serre).** A continuous map $\pi:E\to B$ is a **(Serre) fibration** if it has the homotopy lifting property for cubes: any homotopy of a cube in $B$ lifts, given a lift of its start, to a homotopy in $E$. The **fiber** is $F=\pi^{-1}(b_0)$. *Example:* the Hopf map $S^1\to S^3\xrightarrow{\pi}S^2$ has fiber $S^1$.

> **Theorem (Leray–Serre, homology).** For a fibration $F\to E\xrightarrow{\pi}B$ with $B$ path-connected and acting trivially on $H_*(F)$ (the simply-connected base case), there is a first-quadrant spectral sequence
>
> $$
> E^2_{p,q}=H_p\big(B;\,H_q(F)\big)\ \Rightarrow\ H_{p+q}(E).
> $$
>
> The differentials are $d^r:E^r_{p,q}\to E^r_{p-r,q+r-1}$, and $E^\infty$ is the associated graded of a filtration of $H_*(E)$.

**Worked computation — homology of $S^3$ from the Hopf fibration $S^1\to S^3\to S^2$.** We will *verify* $H_*(S^3)$ and in the process pin down a differential.

1. *The $E^2$ page.* Base $B=S^2$ has $H_p(S^2)=\mathbb{Z}$ for $p=0,2$ and $0$ otherwise. Fiber $F=S^1$ has $H_q(S^1)=\mathbb{Z}$ for $q=0,1$ and $0$ otherwise. With trivial action, $E^2_{p,q}=H_p(S^2)\otimes H_q(S^1)$ (no $\mathrm{Tor}$ since everything is free). Nonzero entries:
> $$
> E^2_{0,0}=\mathbb{Z},\quad E^2_{2,0}=\mathbb{Z},\quad E^2_{0,1}=\mathbb{Z},\quad E^2_{2,1}=\mathbb{Z},
> $$
all others $0$. *(Künneth with free coefficients, §s5; given homologies of $S^1,S^2$)*
2. *Which differentials can be nonzero?* $d^2:E^2_{p,q}\to E^2_{p-2,q+1}$. The only nonzero $d^2$ possible connects $E^2_{2,0}=\mathbb{Z}\to E^2_{0,1}=\mathbb{Z}$ (since other sources/targets are $0$). Call this map $\delta$. All $d^r$ for $r\geq3$ vanish (bidegree pushes out of the four occupied spots). *(bidegree of $d^2$; the grid has only four nonzero entries)*
3. *Determine $\delta$ by knowing the answer at the corners.* The total space is $S^3$: $H_0=\mathbb{Z}$, $H_1=0$, $H_2=0$, $H_3=\mathbb{Z}$. Convergence says $\bigoplus_{p+q=n}E^\infty_{p,q}$ (as associated graded) must match $H_n(S^3)$.
> - $n=1$: only $E^2_{0,1}=\mathbb{Z}$ contributes. For $H_1(S^3)=0$ we need $E^\infty_{0,1}=0$, i.e. $\delta:E^2_{2,0}\to E^2_{0,1}$ must be **onto** $\mathbb{Z}$.
> - $n=2$: only $E^2_{2,0}=\mathbb{Z}$ contributes. For $H_2(S^3)=0$ we need $E^\infty_{2,0}=0$, i.e. $\delta$ must be **injective** ($\ker\delta=0$).
> Together: $\delta:\mathbb{Z}\to\mathbb{Z}$ is an isomorphism, so it is $\pm1$. *(convergence: $E^\infty=$ associated graded of $H_*(S^3)$)*
4. *Check the surviving corners.* After $d^2=\delta$ (an iso), $E^3_{2,0}=E^3_{0,1}=0$, while $E^3_{0,0}=\mathbb{Z}$ and $E^3_{2,1}=\mathbb{Z}$ survive untouched (no differentials hit them). These stabilize: $E^\infty_{0,0}=\mathbb{Z}$ gives $H_0(S^3)=\mathbb{Z}$ ✓, and $E^\infty_{2,1}=\mathbb{Z}$ (with $p+q=3$) gives $H_3(S^3)=\mathbb{Z}$ ✓. *(stabilization; convergence)*
5. *Conclusion.* The spectral sequence reproduces $H_*(S^3)=(\mathbb{Z},0,0,\mathbb{Z})$ and forces the Hopf fibration's transgression $\delta$ to be an isomorphism — the algebraic fingerprint of the nontriviality of the Hopf bundle. $\;\blacksquare$

**Second computation — the loop space homology $H_*(\Omega S^3)$ from the path fibration.** The **path–loop fibration** $\Omega S^3\to PS^3\xrightarrow{\pi}S^3$ has contractible total space $PS^3$ (the path space of based paths), fiber the loop space $\Omega S^3$, and base $S^3$. We use it *backwards*: knowing $E$ is contractible, we deduce $H_*(\Omega S^3)$.

1. *What we know.* $H_*(PS^3)=H_*(\text{point})$: $\mathbb{Z}$ in degree $0$, else $0$. Base $S^3$: $H_p(S^3)=\mathbb{Z}$ for $p=0,3$, else $0$. Let $h_q=H_q(\Omega S^3)$ be the unknowns.
2. *The $E^2$ page.* With simply-connected base, $E^2_{p,q}=H_p(S^3)\otimes h_q$ (free, no $\mathrm{Tor}$ until proven otherwise). The only nonzero columns are $p=0$ and $p=3$: $E^2_{0,q}=h_q$ and $E^2_{3,q}=h_q$. *(Künneth, trivial action)*
3. *The only possible differential.* With two columns three apart, the only differential that can be nonzero is $d^3:E^3_{3,q}\to E^3_{0,q+2}$, i.e. $h_q\to h_{q+2}$. *(bidegree $(-3,2)$ for $d^3$; other $d^r$ land in zero columns)*
4. *Force the answer.* Since $E^\infty$ must be that of a point — zero except $E^\infty_{0,0}=\mathbb{Z}$ — every $d^3$ must be an **isomorphism** $h_q\xrightarrow{\sim}h_{q+2}$ for $q\geq0$ (otherwise a surviving class would give nonzero homology of $PS^3$ in positive degree), except that $E^2_{0,0}=h_0=\mathbb{Z}$ must survive. Starting from $h_0=\mathbb{Z}$ (path-connected loop space) and $h_1$: position $(0,1)$ can only be killed by $d^3$ from $(3,-1)=0$, so $h_1$ must already vanish for $E^\infty_{0,1}=0$; hence $h_1=0$. Then $d^3:h_0\to h_2$ iso gives $h_2=\mathbb{Z}$; $h_3$ must vanish by the same parity argument; $d^3:h_2\to h_4$ gives $h_4=\mathbb{Z}$; inductively $h_{2k}=\mathbb{Z}$ and $h_{2k+1}=0$. *(convergence to a point forces the differentials)*
5. *Conclusion.* $H_q(\Omega S^3)=\mathbb{Z}$ for $q$ even, $0$ for $q$ odd — recovering the known fact that $\Omega S^3$ has the homology of an infinite "divided-power" algebra on one degree-$2$ generator. $\;\blacksquare$

**Intuition.** The $E^2$ page is "base homology with fiber-homology coefficients." Differentials record how the fiber twists as you move around the base; a nonzero $d^r$ means the bundle is genuinely nontrivial. Running a known total space *backwards* (as in the path fibration) computes the fiber — this is the standard route to loop-space homology and ultimately to homotopy groups. **Pitfall:** when $\pi_1(B)$ acts nontrivially on $H_*(F)$ one must use *local* (twisted) coefficients on the $E^2$ page — the trivial-action hypothesis above is essential.

<a id="s11"></a>
### Group cohomology and the Lyndon–Hochschild–Serre spectral sequence (overview)

**What & why.** Replacing "space" by "group" gives **group cohomology**, the derived functor of taking invariants. A short exact sequence of groups then plays the role of a fibration, and its spectral sequence — Lyndon–Hochschild–Serre (LHS) — relates the cohomology of the whole group to that of a normal subgroup and the quotient.

**What & why.** Group cohomology answers questions like "how many extensions of $Q$ by an abelian group are there?" and "which symmetries lift?" It is the derived functor of invariants, and it is computed by exactly the resolution machinery of §s3–s4 applied to the group ring. The spectral sequence at the end of this section is the group-theoretic mirror of the Leray–Serre sequence.

> **Definition — $G$-module.**
> A **$G$-module** $M$ is an abelian group with an action of the group $G$ by automorphisms; equivalently a module over the **group ring** $\mathbb{Z}[G]$ (finite formal sums $\sum n_g\, g$, multiplied using the group law). The **invariants** are $M^G=\{m: gm=m\ \forall g\}$, and $(-)^G=\mathrm{Hom}_{\mathbb{Z}[G]}(\mathbb{Z},-)$ where $\mathbb{Z}$ carries the trivial action.

> **Definition — group cohomology.**
> $H^n(G;M)=\mathrm{Ext}^n_{\mathbb{Z}[G]}(\mathbb{Z},M)=R^n(-)^G(M)$, the right derived functors (§s4) of taking $G$-invariants. So $H^0(G;M)=M^G$, and the higher $H^n$ measure the failure of invariants to be exact. *Example:* $H^1(G;M)$ classifies "crossed homomorphisms modulo principal ones"; for trivial action $H^1(G;M)=\mathrm{Hom}(G,M)$.

> **Full computation — $H^n(\mathbb{Z}/2;\mathbb{Z})$ from a free resolution.** Let $G=\mathbb{Z}/2=\langle t\mid t^2=1\rangle$, so $\mathbb{Z}[G]=\mathbb{Z}[t]/(t^2-1)$. There is a standard **periodic** free resolution of the trivial module $\mathbb{Z}$ over $\mathbb{Z}[G]$:
>
> $$
> \cdots\to\mathbb{Z}[G]\xrightarrow{\,t-1\,}\mathbb{Z}[G]\xrightarrow{\,t+1\,}\mathbb{Z}[G]\xrightarrow{\,t-1\,}\mathbb{Z}[G]\xrightarrow{\,\varepsilon\,}\mathbb{Z}\to0,
> $$
>
> where $\varepsilon(t)=1$ is the augmentation. One checks $(t-1)(t+1)=t^2-1=0$ and $(t+1)(t-1)=0$ in $\mathbb{Z}[G]$, and exactness because $\ker\varepsilon$ is generated by $t-1$, $\ker(t-1)$ by $t+1$, etc. Apply $\mathrm{Hom}_{\mathbb{Z}[G]}(-,\mathbb{Z})$ with $\mathbb{Z}$ trivial; each $\mathrm{Hom}_{\mathbb{Z}[G]}(\mathbb{Z}[G],\mathbb{Z})=\mathbb{Z}$, the dual of $t-1$ becomes multiplication by $\varepsilon(t)-1=0$, and the dual of $t+1$ becomes $\varepsilon(t)+1=2$. The cochain complex is
>
> $$
> \mathbb{Z}\xrightarrow{0}\mathbb{Z}\xrightarrow{2}\mathbb{Z}\xrightarrow{0}\mathbb{Z}\xrightarrow{2}\cdots
> $$
>
> Cohomology: $H^0=\mathbb{Z}$; in odd degrees $H^{2k+1}=\ker(2)/\mathrm{im}(0)=0$; in positive even degrees $H^{2k}=\ker(0)/\mathrm{im}(2)=\mathbb{Z}/2$. So $H^n(\mathbb{Z}/2;\mathbb{Z})=\mathbb{Z},0,\mathbb{Z}/2,0,\mathbb{Z}/2,\dots$ — the same pattern as $H^*(\mathbb{RP}^\infty;\mathbb{Z})$, because $\mathbb{RP}^\infty$ is the classifying space $B(\mathbb{Z}/2)$ and group cohomology *is* the cohomology of the classifying space.

> **Theorem (Lyndon–Hochschild–Serre).** For a short exact sequence of groups $1\to N\to G\to Q\to1$ and a $G$-module $M$, there is a first-quadrant spectral sequence
>
> $$
> E_2^{p,q}=H^p\big(Q;\,H^q(N;M)\big)\ \Rightarrow\ H^{p+q}(G;M).
> $$

**Where it comes from (overview).** The functor "take $G$-invariants" factors as "take $N$-invariants, then take $Q=G/N$-invariants": $M^G=(M^N)^Q$. LHS is the **Grothendieck spectral sequence** of this composite of functors — the general theorem that for a composable pair of functors $F,F'$ with $F$ sending injectives/acyclics to $F'$-acyclics, there is a spectral sequence $R^pF'\big(R^qF(M)\big)\Rightarrow R^{p+q}(F'\circ F)(M)$. Concretely it is the double-complex spectral sequence (§s9) of a suitable double resolution. *(composite-functor / Grothendieck spectral sequence, built from §s9)*

> **Worked use — the five-term exact sequence.** Reading the low-degree corner of LHS exactly as in the two-column example of §s8 gives, for any $1\to N\to G\to Q\to1$,
>
> $$
> 0\to H^1(Q;M^N)\to H^1(G;M)\to H^1(N;M)^Q\xrightarrow{\,d_2\,} H^2(Q;M^N)\to H^2(G;M).
> $$
>
> *Derivation:* the entries $E_2^{p,q}$ with $p+q\leq2$ and the single $d_2:E_2^{0,1}\to E_2^{2,0}$ are all that can be nonzero in low degree; assembling their kernels/cokernels by the convergence filtration (§s8) yields the five terms. This recovers, among other things, the inflation–restriction sequence of Galois cohomology. *(low-degree reading of a first-quadrant spectral sequence, §s8)*

**Intuition.** A normal subgroup $N\trianglelefteq G$ behaves like a "fiber" and $Q=G/N$ like a "base"; LHS is the algebraic Leray–Serre spectral sequence of the fibration $BN\to BG\to BQ$ of classifying spaces. The whole guide closes the loop: the same two-dimensional bookkeeping computes the (co)homology of spaces, of modules, and of groups.

---

*A from-scratch course in homological algebra and spectral sequences: exactness and diagram chasing, chain complexes, resolutions, the derived functors $\mathrm{Tor}$ and $\mathrm{Ext}$, the universal-coefficient and Künneth theorems, the categorical language that makes it portable, and the spectral sequences — filtered, double-complex, Leray–Serre, and Lyndon–Hochschild–Serre — that organize every computation. Read once for the architecture; return to any box for the proof. The single idea underneath: measure the failure of exactness, then bookkeep that measurement in two dimensions.*
