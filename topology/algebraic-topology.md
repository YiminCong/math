**English** · [中文](algebraic-topology.zh.md)

# Topology, *turned into algebra.*

A full first course in algebraic topology — how to attach groups, rings, and exact sequences to spaces so that continuous maps become homomorphisms and "shape" becomes computable. Every core theorem is **demonstrated** from the ground up, every algebraic word is defined the first time it appears, and the functorial thread that ties them all together is made explicit.

[← Back to all guides](../README.md)

> **How to read this guide.** We assume you have read the *General Topology* guide, so you know what a *topological space*, an *open set*, a *continuous map*, a *homeomorphism*, *path-connected*, and *compact* mean. We assume **no** algebra beyond ordinary arithmetic. Every algebraic notion — group, subgroup, homomorphism, kernel, normal subgroup, quotient group, free group, free product, abelian, exact sequence — is defined in plain words the first time it is used, with a small numerical example. Nothing is "left to the reader."

---

#### A pocket dictionary of the algebra we will build (read once, refer back)

We collect the algebraic vocabulary here so you can return to it. Each item is re-defined in context when first used; this is just the map.

> **Definition — group.**
> A **group** is a set $G$ together with a way to combine two elements into a third — a *binary operation* written $a\cdot b$ (or just $ab$) — satisfying three rules:
> 1. **Associativity:** $(ab)c=a(bc)$ for all $a,b,c$. (Grouping does not matter.)
> 2. **Identity:** there is a special element $e$ with $ea=ae=a$ for all $a$. (Doing nothing.)
> 3. **Inverses:** every $a$ has some $a^{-1}$ with $a a^{-1}=a^{-1}a=e$. (Every move can be undone.)
>
> *Example with numbers:* the integers $\mathbb{Z}=\{\dots,-2,-1,0,1,2,\dots\}$ under addition form a group: $a\cdot b$ means $a+b$, the identity is $0$ (since $0+a=a$), and the inverse of $a$ is $-a$ (since $a+(-a)=0$). Associativity is the familiar $(a+b)+c=a+(b+c)$.

> **Definition — abelian group.**
> A group is **abelian** (commutative) if also $ab=ba$ for all $a,b$. *Example:* $(\mathbb{Z},+)$ is abelian since $a+b=b+a$. A group can fail this — we will meet non-abelian groups, where the *order* of moves matters.

> **Definition — subgroup.**
> A **subgroup** $H$ of $G$ is a subset that is itself a group with the same operation: it contains $e$, and is closed under the operation and under inverses ($a,b\in H\Rightarrow ab\in H$ and $a^{-1}\in H$). We write $H\le G$. *Example:* the even integers $2\mathbb{Z}=\{\dots,-2,0,2,4,\dots\}$ form a subgroup of $(\mathbb{Z},+)$.

> **Definition — homomorphism, kernel, image, isomorphism.**
> A **homomorphism** is a map $\varphi:G\to H$ between groups that respects the operations: $\varphi(ab)=\varphi(a)\varphi(b)$. It automatically sends identity to identity and inverses to inverses. Its **kernel** is $\ker\varphi=\{g\in G:\varphi(g)=e_H\}$ (what gets crushed to the identity); its **image** is $\operatorname{im}\varphi=\{\varphi(g):g\in G\}$. An **isomorphism** is a homomorphism that is also a bijection (one-to-one and onto); then $G$ and $H$ are "the same group with relabelled elements," written $G\cong H$. *Example:* $\varphi:\mathbb{Z}\to\mathbb{Z}$, $\varphi(n)=2n$ is a homomorphism with kernel $\{0\}$ and image $2\mathbb{Z}$.

> **Definition — normal subgroup and quotient group.**
> A subgroup $N\le G$ is **normal**, written $N\trianglelefteq G$, if $gNg^{-1}=N$ for every $g\in G$ (conjugating $N$ by anything lands back in $N$). When $N$ is normal we can form the **quotient group** $G/N$: its elements are the *cosets* $gN=\{gn:n\in N\}$, with multiplication $(gN)(hN)=(gh)N$. Normality is exactly the condition that makes this multiplication well defined. *Example:* in $(\mathbb{Z},+)$ every subgroup is normal (the group is abelian); $\mathbb{Z}/2\mathbb{Z}$ has two elements, "even" $=0+2\mathbb{Z}$ and "odd" $=1+2\mathbb{Z}$, with $\text{odd}+\text{odd}=\text{even}$ — this is parity arithmetic.

> **Definition — free group and presentation.**
> The **free group** $F_n$ on symbols $g_1,\dots,g_n$ consists of all finite "words" in the symbols and their inverses (like $g_1 g_2^{-1} g_1$), where the only simplifications allowed are cancelling an adjacent $g_i g_i^{-1}$ or $g_i^{-1}g_i$. There are *no other relations*: it is as "unconstrained" as possible. Multiplication is concatenation of words. A **presentation** $\langle g_1,\dots,g_n\mid r_1,\dots,r_m\rangle$ means "the free group on the $g_i$, then forced to also obey $r_1=\dots=r_m=e$" (formally, quotient by the smallest normal subgroup containing the $r_j$). *Example:* $\langle a\mid a^2\rangle$ is the free group on one symbol $a$ with the extra rule $a^2=e$; it has two elements $\{e,a\}$, i.e. $\mathbb{Z}/2$.

> **Definition — free product and amalgamated free product.**
> The **free product** $G*H$ consists of all alternating words mixing elements of $G$ and $H$, with no relations between the two except their own internal ones. The **amalgamated free product** $G*_K H$ further glues a common subgroup $K$ that maps into both, by adding the relations $i(k)=j(k)$ for $k\in K$. These are the group-theory versions of "gluing." *Example:* $\mathbb{Z}*\mathbb{Z}=F_2$, the free group on two generators.

> **Definition — exact sequence.**
> A chain of groups and homomorphisms $\cdots\to A\xrightarrow{f}B\xrightarrow{g}C\to\cdots$ is **exact at $B$** if $\operatorname{im}f=\ker g$ — the things coming out of $A$ are exactly the things crushed on the way to $C$. A **short exact sequence** $0\to A\xrightarrow{f}B\xrightarrow{g}C\to 0$ packages "$f$ is injective, $g$ is surjective, and $A$ is precisely the kernel of $g$," so $C\cong B/A$. (Here $0$ denotes the trivial one-element group.) This is the central bookkeeping device of the whole subject.

---

## Part A · Homotopy & the fundamental group

<a id="s0"></a>
### The big picture: turning spaces into algebra

Topology studies properties of spaces preserved by continuous deformation — properties invariant under *homeomorphism* (a continuous bijection with continuous inverse; recall this from the General Topology guide). But proving two spaces are *not* homeomorphic is hard *directly*: you would have to rule out **every** possible continuous bijection between them, and there are infinitely many maps to consider. Algebraic topology offers a systematic way out.

The strategy has three moves:

- **Attach** an algebraic object (a group, later a ring or a whole sequence of groups) to every space.
- **Functoriality:** every continuous map between spaces is forced to produce a homomorphism between the attached groups, in a way that respects composing maps and the identity map.
- **Invariance:** homeomorphic — indeed merely *homotopy-equivalent* (§s1) — spaces receive isomorphic algebra. So if the algebra differs, the spaces cannot be the same.

> **Principle — the central strategy.**
>
> An **invariant** is a *functor* $F$ from "spaces and continuous maps" to "groups and homomorphisms." The word *functor* simply names a rule $F$ that (i) sends each space $X$ to a group $F(X)$, (ii) sends each continuous $f:X\to Y$ to a homomorphism $F(f):F(X)\to F(Y)$, and (iii) obeys the two compatibility laws
> $$F(f\circ g)=F(f)\circ F(g),\qquad F(\mathrm{id}_X)=\mathrm{id}_{F(X)}.$$

**Demonstration — why a functor turns homeomorphic spaces into isomorphic groups.** This is the load-bearing logical step of the entire subject, so we prove it with no gaps.

1. Suppose $h:X\to Y$ is a homeomorphism. By definition that means there is a continuous inverse $h^{-1}:Y\to X$ with $h^{-1}\circ h=\mathrm{id}_X$ and $h\circ h^{-1}=\mathrm{id}_Y$. *(definition of homeomorphism, from General Topology)*
2. Apply $F$ to the first equation. Using law (i), $F(h^{-1}\circ h)=F(h^{-1})\circ F(h)$. Using law (iii), $F(\mathrm{id}_X)=\mathrm{id}_{F(X)}$. Since $h^{-1}\circ h=\mathrm{id}_X$, the two left-hand sides are equal, so $F(h^{-1})\circ F(h)=\mathrm{id}_{F(X)}$. *(apply $F$, then the two functor laws)*
3. Apply $F$ to the second equation the same way: $F(h)\circ F(h^{-1})=\mathrm{id}_{F(Y)}$. *(same reasoning)*
4. Steps 2–3 say $F(h):F(X)\to F(Y)$ has a two-sided inverse, namely $F(h^{-1})$. A homomorphism with a two-sided inverse is a bijection, hence an isomorphism. Therefore $F(X)\cong F(Y)$. $\;\blacksquare$

**Worked logical example.** Suppose someone hands us a functor with $F(X)=\mathbb{Z}$ and $F(Y)=\mathbb{Z}/2$ (the two-element group). Could $X$ and $Y$ be homeomorphic? No: by the demonstration a homeomorphism would force $\mathbb{Z}\cong\mathbb{Z}/2$, but $\mathbb{Z}$ is infinite and $\mathbb{Z}/2$ has two elements, so no bijection exists. We have *proved* $X\not\cong Y$ without ever examining a single map between them. This is the whole game, in miniature.

> **Connection — why "functor" is the load-bearing word.**
>
> Every chapter is one functor: $\pi_1$ (a possibly non-abelian group, §s2), $\pi_n$ (abelian groups, §s14), $H_n$ (homology, abelian groups, §s10), $H^n$ (cohomology, a graded *ring*, §s13). The proofs differ; the logic — induced maps, then the argument above, then computation — never does.

#### The whole course on one line

> Homotopy → $\pi_1$ → $\pi_1(S^1)\cong\mathbb{Z}$ → van Kampen → covering spaces → homology → cohomology & duality

<a id="s1"></a>
### Homotopy of maps & homotopy equivalence

*The slackening of "equal" to "continuously deformable" is the move that makes everything compute. Most invariants see only homotopy type, not homeomorphism type.* The intuition: we will treat two maps as "the same" if one can be slid into the other without tearing. This is weaker than being literally equal, and that very weakness is what makes the invariants computable.

> **Definition — homotopy.**
>
> Let $X,Y$ be spaces and $[0,1]$ the unit interval. Two continuous maps $f,g:X\to Y$ are **homotopic**, written $f\simeq g$, if there is a continuous map $H:X\times[0,1]\to Y$ with
> $$H(x,0)=f(x)\quad\text{and}\quad H(x,1)=g(x)\quad\text{for all }x\in X.$$
> Think of the second coordinate $t\in[0,1]$ as *time*: at each frozen time $t$, the rule $x\mapsto H(x,t)$ is a continuous map $X\to Y$, and as $t$ runs $0\to 1$ this map slides continuously from $f$ to $g$. $H$ is a "movie" of maps. For **paths** (maps from $[0,1]$) we additionally demand the two endpoints never move during the movie — this is called homotopy **rel $\{0,1\}$** (read "relative to the endpoints").

**Demonstration — homotopy is an equivalence relation.** We must check the three defining properties of an equivalence relation (reflexive, symmetric, transitive). We use only the definition above and the *pasting lemma* from General Topology (a map defined piecewise on two closed pieces that agree on the overlap is continuous).

1. **Reflexive ($f\simeq f$).** Define $H(x,t)=f(x)$, ignoring $t$. This is continuous because it is $f$ composed with the projection $X\times[0,1]\to X$, both continuous. At $t=0$ and $t=1$ it equals $f$. *(definition of homotopy with the constant movie)*
2. **Symmetric (if $f\simeq g$ then $g\simeq f$).** Let $H$ witness $f\simeq g$. Define $\overline H(x,t)=H(x,1-t)$. It is continuous as the composite of $H$ with the continuous map $t\mapsto 1-t$. At $t=0$ it is $H(x,1)=g(x)$; at $t=1$ it is $H(x,0)=f(x)$. So $\overline H$ runs $g\simeq f$. *(definition + composition of continuous maps)*
3. **Transitive (if $f\simeq g$ and $g\simeq h$ then $f\simeq h$).** Let $H:f\simeq g$ and $K:g\simeq h$. Splice the two movies, running the first at double speed on $[0,\tfrac12]$ and the second at double speed on $[\tfrac12,1]$:
   $$L(x,t)=\begin{cases} H(x,2t), & 0\le t\le \tfrac12,\\ K(x,2t-1), & \tfrac12\le t\le 1.\end{cases}$$
   At the seam $t=\tfrac12$ the top piece gives $H(x,1)=g(x)$ and the bottom piece gives $K(x,0)=g(x)$; they agree. The two pieces are continuous on the closed sets $X\times[0,\tfrac12]$ and $X\times[\tfrac12,1]$, which cover $X\times[0,1]$ and overlap exactly where the formulas agree, so by the pasting lemma $L$ is continuous. It runs $f\simeq h$. $\;\blacksquare$ *(pasting lemma + definition of homotopy)*

Because $\simeq$ is an equivalence relation, the maps $X\to Y$ split into disjoint **homotopy classes**; we write $[f]$ for the class of $f$. These classes are the raw material of every homotopy invariant.

> **Definition — homotopy equivalence, contractible, deformation retraction.**
>
> A map $f:X\to Y$ is a **homotopy equivalence** if there exists $g:Y\to X$ with $g\circ f\simeq \mathrm{id}_X$ and $f\circ g\simeq \mathrm{id}_Y$ (the round trips are merely *homotopic* to doing nothing, not literally equal). Then $X$ and $Y$ are **homotopy equivalent**, written $X\simeq Y$. A space homotopy equivalent to a single point is **contractible** (it can be continuously shrunk to a point). A **deformation retraction** of $X$ onto a subspace $A\subseteq X$ is a homotopy $H:X\times[0,1]\to X$ with $H(x,0)=x$, $H(x,1)\in A$, and $H(a,t)=a$ for all $a\in A$ (points already in $A$ never move). It exhibits the inclusion $A\hookrightarrow X$ as a homotopy equivalence.

**Worked example — $\mathbb{R}^n$ is contractible.** Define $H:\mathbb{R}^n\times[0,1]\to\mathbb{R}^n$ by $H(x,t)=(1-t)x$. It is continuous (scalar multiplication and subtraction are continuous). At $t=0$, $H(x,0)=x=\mathrm{id}(x)$; at $t=1$, $H(x,1)=0$, the constant map at the origin. So $\mathrm{id}_{\mathbb{R}^n}\simeq(\text{constant})$, which is exactly the statement that $\mathbb{R}^n$ is homotopy equivalent to the one-point space $\{0\}$. Concretely, every point glides straight to the origin at uniform speed. $\;\blacksquare$

**Worked example — the punctured plane retracts onto the circle.** Let $X=\mathbb{R}^2\setminus\{0\}$ and $A=S^1=\{x:|x|=1\}$. Define
$$H(x,t)=(1-t)\,x+t\,\frac{x}{|x|}.$$
This is continuous on $X$ (we never divide by zero, since $x\ne 0$). At $t=0$ it is $x$; at $t=1$ it is $x/|x|$, which has length $1$, so it lands in $S^1$. If $|x|=1$ already, then $x/|x|=x$ and $H(x,t)=(1-t)x+tx=x$ for all $t$: points on the circle stay put. Hence $H$ is a deformation retraction of the punctured plane onto $S^1$. *Pitfall:* you must check the path $H(x,t)$ never passes through $0$; here $(1-t)+t/|x|>0$ times $x\ne 0$, so it does not. $\;\blacksquare$

An annulus, a Möbius band, and $S^1$ are all homotopy equivalent (each deformation-retracts onto a core circle) though no two are homeomorphic — homotopy is genuinely *coarser* than homeomorphism.

> **Connection — to general topology.**
>
> Homeomorphism $\Rightarrow$ homotopy equivalence (a homeomorphism is in particular a homotopy equivalence, taking $g=f^{-1}$), but never the reverse, as the disk-vs-point example shows. Our invariants are designed to be *homotopy* invariants, so they are automatically *topological* invariants too — but by construction they cannot distinguish a disk from a point.

<a id="s2"></a>
### The fundamental group $\pi_1$

*The first and most intuitive functor: loops at a basepoint, considered up to homotopy, with "do one loop then the other" as the group operation. It detects one-dimensional holes — places a loop can get stuck around.*

> **Definition — loops, concatenation, the fundamental group.**
>
> Fix a point $x_0\in X$ called the **basepoint**. A **loop** at $x_0$ is a path $\gamma:[0,1]\to X$ (continuous) with $\gamma(0)=\gamma(1)=x_0$ (it starts and ends at the basepoint). The **fundamental group** $\pi_1(X,x_0)$ is the set of homotopy classes (rel endpoints, §s1) of loops at $x_0$, equipped with the product $[\alpha][\beta]=[\alpha\cdot\beta]$, where the **concatenation** $\alpha\cdot\beta$ runs $\alpha$ at double speed on $[0,\tfrac12]$ then $\beta$ at double speed on $[\tfrac12,1]$:
> $$(\alpha\cdot\beta)(s)=\begin{cases}\alpha(2s),&0\le s\le\tfrac12,\\ \beta(2s-1),&\tfrac12\le s\le1.\end{cases}$$
> (This is continuous by the pasting lemma: at $s=\tfrac12$ both pieces give $x_0$.)

**Demonstration — $\pi_1(X,x_0)$ is a group.** We verify the four requirements: well-definedness of the product, associativity, an identity, and inverses. Throughout, "$\simeq$" means homotopy rel endpoints, and we freely reparametrize the time axis $[0,1]$ — a continuous, endpoint-fixing change of speed $\varphi:[0,1]\to[0,1]$ gives $\gamma\simeq\gamma\circ\varphi$ via the straight-line homotopy $H(s,t)=\gamma\big((1-t)s+t\,\varphi(s)\big)$, which fixes endpoints because $\varphi(0)=0,\varphi(1)=1$.

1. **Well defined.** We must show the product of *classes* does not depend on representatives. Suppose $\alpha\simeq\alpha'$ via a homotopy $H$ (rel endpoints) and $\beta\simeq\beta'$ via $K$. Build the "side-by-side" homotopy that runs $H$ on the first half of $s$ and $K$ on the second half:
   $$(H\cdot K)(s,t)=\begin{cases}H(2s,t),&0\le s\le\tfrac12,\\ K(2s-1,t),&\tfrac12\le s\le1.\end{cases}$$
   At the seam $s=\tfrac12$ both equal $\gamma$-value $x_0$ for all $t$ (endpoints are fixed), so by the pasting lemma it is continuous; it runs $\alpha\cdot\beta\simeq\alpha'\cdot\beta'$. Hence $[\alpha][\beta]=[\alpha'][\beta']$. *(pasting lemma + definition of the product on classes)*
2. **Associativity.** Compare $(\alpha\cdot\beta)\cdot\gamma$ and $\alpha\cdot(\beta\cdot\gamma)$. Both traverse $\alpha,\beta,\gamma$ in order; they differ only in the time intervals allotted (quarter/quarter/half versus half/quarter/quarter). A single reparametrization $\varphi$ that linearly stretches/compresses these intervals carries one to the other, and by the reparametrization fact above this is a homotopy rel endpoints. So $([\alpha][\beta])[\gamma]=[\alpha]([\beta][\gamma])$. *(reparametrization homotopy)*
3. **Identity.** Let $c$ be the constant loop $c(s)=x_0$. Then $c\cdot\alpha$ is "wait at $x_0$ for half the time, then do $\alpha$ at double speed." The reparametrization that deletes the waiting gives $c\cdot\alpha\simeq\alpha$; similarly $\alpha\cdot c\simeq\alpha$. Hence $[c]$ is a two-sided identity. *(reparametrization homotopy)*
4. **Inverses.** Let $\bar\alpha(s)=\alpha(1-s)$ be $\alpha$ run backwards. Consider $\alpha\cdot\bar\alpha$: go out along $\alpha$, come straight back. Shrink the "turnaround time" toward $s=0$:
   $$H(s,t)=\begin{cases}\alpha(2s),&0\le s\le\tfrac{1-t}{2},\\ \alpha(1-t),&\tfrac{1-t}{2}\le s\le\tfrac{1+t}{2},\\ \alpha(2-2s),&\tfrac{1+t}{2}\le s\le 1.\end{cases}$$
   At $t=0$ this is $\alpha\cdot\bar\alpha$; at $t=1$ it is the constant loop $c$ (the middle "pause at the start" swallows everything). It fixes endpoints at $x_0$. So $[\alpha][\bar\alpha]=[c]$, and likewise $[\bar\alpha][\alpha]=[c]$. Thus $[\alpha]^{-1}=[\bar\alpha]$. $\;\blacksquare$ *(pasting lemma + definition of homotopy)*

All four axioms hold only *up to* endpoint-fixing homotopy — which is exactly why we quotiented by it. (Recall *group* from the pocket dictionary: a set with an associative operation, an identity, and inverses.)

**Demonstration — the group does not depend on the basepoint (on a path-connected space).** "Path-connected" (from General Topology) means any two points are joined by a path.

1. Let $h:[0,1]\to X$ be a path from $x_0$ to $x_1$, with reverse $\bar h$. Define the **change-of-basepoint map**
   $$\beta_h:\pi_1(X,x_1)\to\pi_1(X,x_0),\qquad \beta_h[\gamma]=[\,h\cdot\gamma\cdot\bar h\,].$$
   (Go from $x_0$ to $x_1$ along $h$, do the loop $\gamma$ at $x_1$, return along $\bar h$ — net a loop at $x_0$.) It is well defined by the well-definedness of concatenation (step 1 above).
2. **It is a homomorphism** (recall: respects the product). Compute, inserting the constant loop $\bar h\cdot h\simeq c$ in the middle:
   $$\beta_h([\gamma][\delta])=[h\cdot\gamma\cdot\delta\cdot\bar h]=[h\cdot\gamma\cdot\bar h\cdot h\cdot\delta\cdot\bar h]=\beta_h[\gamma]\,\beta_h[\delta].$$
   *(group axioms in $\pi_1(X,x_0)$: insert $[\bar h][h]=[c]$, the identity)*
3. **It is invertible**, with inverse $\beta_{\bar h}$, because $\beta_h\circ\beta_{\bar h}=\beta_{h\cdot\bar h}=\beta_c=\mathrm{id}$ (composing two changes of basepoint concatenates the connecting paths). $\;\blacksquare$

So $\pi_1(X,x_0)\cong\pi_1(X,x_1)$: on a path-connected space we may drop the basepoint and write $\pi_1(X)$ up to isomorphism. (Caveat: the isomorphism depends on $h$ — different paths can differ by an inner automorphism — so it is canonical only when $\pi_1$ is abelian.)

**Functoriality & the induced homomorphism.** A based continuous map is a map $f:X\to Y$ with $f(x_0)=y_0$. It induces
$$f_*:\pi_1(X,x_0)\to\pi_1(Y,y_0),\qquad f_*[\gamma]=[f\circ\gamma].$$

**Demonstration — $f_*$ is a well-defined homomorphism and $\pi_1$ is a functor.**

1. **Well defined.** If $\gamma\simeq\gamma'$ via $H$ (rel endpoints), then $f\circ H$ is a homotopy $f\circ\gamma\simeq f\circ\gamma'$ rel endpoints (compose continuous maps; endpoints map to $y_0$). So $f_*$ is independent of representative. *(composition of continuous maps)*
2. **Homomorphism.** $f\circ(\alpha\cdot\beta)=(f\circ\alpha)\cdot(f\circ\beta)$ because applying $f$ commutes with the piecewise definition of concatenation. Hence $f_*([\alpha][\beta])=f_*[\alpha]\,f_*[\beta]$. *(definition of concatenation)*
3. **Functor laws.** $(g\circ f)\circ\gamma=g\circ(f\circ\gamma)$ gives $(g\circ f)_*=g_*\circ f_*$, and $\mathrm{id}\circ\gamma=\gamma$ gives $(\mathrm{id}_X)_*=\mathrm{id}$. *(associativity of composition)*
4. **Homotopy invariance.** If $f\simeq g$ rel $x_0$ then $f_*=g_*$: the homotopy of maps applied to a loop is a homotopy of the image loops. Combined with §s0's demonstration, $X\simeq Y\Rightarrow\pi_1(X)\cong\pi_1(Y)$. $\;\blacksquare$

These facts make $\pi_1$ a functor (compare §s0) and prove homotopy invariance.

> **Definition — simply connected.**
>
> $X$ is **simply connected** if it is path-connected and $\pi_1(X)=0$ (the trivial group — every loop is homotopic to the constant loop, i.e. every loop can be contracted to a point). Examples we will justify: $\mathbb{R}^n$ and any convex set (contractible, so $\pi_1=0$ by homotopy invariance), and $S^n$ for $n\ge 2$ (§s11/§s12 compute its homology; here we just record it).

**Worked example — $\pi_1(\mathbb{R}^n)=0$.** By §s1, $\mathbb{R}^n$ is contractible, hence homotopy equivalent to a point. A point has exactly one loop (the constant one) and one homotopy class, so $\pi_1(\text{point})=0$. By homotopy invariance (step 4 above), $\pi_1(\mathbb{R}^n)\cong\pi_1(\text{point})=0$. $\;\blacksquare$

> **Connection — to group theory.**
>
> $\pi_1$ is in general **non-abelian** (e.g. the wedge of two circles, §s4, has $\pi_1=F_2$ where $ab\ne ba$). So the full machinery of free groups, presentations $\langle\text{generators}\mid\text{relations}\rangle$, and normal subgroups (all in the pocket dictionary) enters topology. This is the bridge into combinatorial group theory.

<a id="s3"></a>
### The circle: $\pi_1(S^1)\cong\mathbb{Z}$ and the winding number

*The foundational computation. Once $\pi_1(S^1)\cong\mathbb{Z}$ is in hand, the great applications (§s5) fall out almost for free.* The intuition: a loop on a circle has a well-defined *net number of times it wraps around*, an integer that adds when you do one loop after another — exactly the group $(\mathbb{Z},+)$.

**Theorem.**
$$\pi_1(S^1,\,1)\ \cong\ \mathbb{Z},\qquad [\gamma]\ \longmapsto\ \deg(\gamma)=\text{winding number}.$$
Here we view $S^1=\{z\in\mathbb{C}:|z|=1\}$ with basepoint $1$. The generator is the once-around loop $\omega(s)=e^{2\pi i s}$, and the integer assigned to a loop is its net number of wraps.

> **Concept — the exponential covering.**
>
> The key tool is the map $p:\mathbb{R}\to S^1,\ p(t)=e^{2\pi i t}$. It wraps the real line around the circle infinitely, like winding string around a spool; each circle point $z$ has the discrete *fiber* $p^{-1}(z)=\{t:e^{2\pi i t}=z\}$, and $p^{-1}(1)=\mathbb{Z}$. Crucially $\mathbb{R}$ is contractible, so a *loop downstairs* on $S^1$ unrolls to a *genuine displacement upstairs* on $\mathbb{R}$ — and a displacement on the line is just a number.

**Demonstration — the covering-space proof.** We use two lifting facts (proved in general in §s6), here stated for $p$.

1. **Path lifting.** Every path $\gamma:[0,1]\to S^1$ with $\gamma(0)=1$ has a *unique* lift $\tilde\gamma:[0,1]\to\mathbb{R}$ with $\tilde\gamma(0)=0$ and $p\circ\tilde\gamma=\gamma$. *Reason:* cover $S^1$ by two open arcs on which $p$ has continuous local inverses; subdivide $[0,1]$ finely (using compactness) so each subinterval lands in one arc; lift piecewise using the local inverse and glue. Uniqueness: two lifts differ by a continuous integer-valued function (their difference lands in $p^{-1}(1)=\mathbb{Z}$), which on a connected interval is constant; matching at $0$ forces it to be $0$.
2. **Homotopy lifting.** A homotopy of paths $\gamma_t$ (rel endpoints) lifts to a homotopy $\tilde\gamma_t$ with $\tilde\gamma_t(0)=0$. By uniqueness the endpoints $\tilde\gamma_t(1)$ form a *continuous* function of $t$ valued in the discrete set $\mathbb{Z}$, hence are *constant* in $t$.
3. **The degree map.** Define $\Phi[\gamma]=\tilde\gamma(1)\in\mathbb{Z}$. By step 2 it depends only on the homotopy class of $\gamma$, so $\Phi:\pi_1(S^1,1)\to\mathbb{Z}$ is well defined.
4. **Homomorphism.** To lift $\alpha\cdot\beta$ starting at $0$: first lift $\alpha$ to $\tilde\alpha$ ending at some integer $m$; then lift $\beta$, but starting at $m$ — the lift is $m+\tilde\beta$ (translation by $m$ is also a lift, by uniqueness), ending at $m+n$ where $n=\Phi[\beta]$. So $\Phi[\alpha\cdot\beta]=m+n=\Phi[\alpha]+\Phi[\beta]$. *(uniqueness of lifts + translation invariance of $p$)*
5. **Surjective.** The loop $\omega_n(s)=e^{2\pi i n s}$ lifts to the straight path $t\mapsto ns$ (check $p(ns)=e^{2\pi i n s}=\omega_n$), ending at $n$. So $\Phi[\omega_n]=n$, hitting every integer.
6. **Injective.** Suppose $\Phi[\gamma]=0$, i.e. $\tilde\gamma$ is a *loop* (ends where it began, at $0$) in $\mathbb{R}$. Since $\mathbb{R}$ is convex, the straight-line homotopy $\tilde H(s,t)=(1-t)\tilde\gamma(s)$ contracts $\tilde\gamma$ to the constant $0$ rel endpoints. Pushing down by $p$, the homotopy $p\circ\tilde H$ contracts $\gamma$ to the constant loop. So $[\gamma]$ is the identity. Thus $\ker\Phi$ is trivial, and a homomorphism with trivial kernel is injective.

Steps 3–6 make $\Phi$ a bijective homomorphism, i.e. an isomorphism: $\pi_1(S^1)\cong\mathbb{Z}$. $\;\blacksquare$

**Worked example — reading off a winding number.** Take the concatenation $\gamma(s)=e^{2\pi i\,(4s)}$ on $[0,\tfrac12]$ (two forward wraps) followed by $\gamma(s)=e^{2\pi i\,(2-2(2s-1))}$ on $[\tfrac12,1]$ (one backward wrap) — concretely, wind around twice forwards then once backwards. Its lift to $\mathbb{R}$ is $\tilde\gamma(s)=4s$ on $[0,\tfrac12]$ and $\tilde\gamma(s)=2-2(2s-1)$ on $[\tfrac12,1]$: it starts at $0$, climbs to $2$, then descends to $1$, ending at $1$. So $\Phi[\gamma]=1$: the net winding is $+1$, even though the loop physically went around three times. The cancellation of one forward and one backward wrap is exactly the group operation $2+(-1)=1$ in $\mathbb{Z}$. $\;\blacksquare$

> **Connection — winding number = a contour integral.**
>
> For a loop in $\mathbb{C}\setminus\{0\}$ the same integer is $\dfrac{1}{2\pi i}\displaystyle\oint\dfrac{dz}{z}$. The topological degree and the complex-analytic winding number are literally the same invariant — the seam between algebraic topology and complex analysis.

<a id="s4"></a>
### The Seifert–van Kampen theorem

*A "divide and conquer" theorem: it computes $\pi_1$ of a union from the $\pi_1$ of the pieces and their overlap. This is the tool that turns a picture (a polygon with edges glued) into a group presentation.*

**Theorem (Seifert–van Kampen).** Let $X=U\cup V$ with $U,V$ open, and $U,V,U\cap V$ path-connected and containing the basepoint. Then
$$\pi_1(X)\ \cong\ \pi_1(U)\ *_{\pi_1(U\cap V)}\ \pi_1(V),$$
the **amalgamated free product** (pocket dictionary): the free product $\pi_1(U)*\pi_1(V)$ modulo the relations $i_*(w)=j_*(w)$ for every $w\in\pi_1(U\cap V)$, where $i:U\cap V\hookrightarrow U$ and $j:U\cap V\hookrightarrow V$ are the inclusions. In words: take all loops from both pieces, allow them to be combined freely, but force a loop living in the overlap to be counted the *same* whether you view it inside $U$ or inside $V$.

**Demonstration — $\pi_1$ of a wedge of $n$ circles is the free group $F_n$.** A **wedge** $S^1\vee\cdots\vee S^1$ is $n$ circles all glued at one common point.

1. Thicken each circle to an open set $U_k$ that deformation-retracts onto that circle (so $\pi_1(U_k)\cong\mathbb{Z}$ by §s3), arranged so that any overlap $U_j\cap U_k$ ($j\ne k$) deformation-retracts onto the single wedge point. A point is contractible, so $\pi_1(U_j\cap U_k)=0$, the trivial group. *(deformation retraction + §s3)*
2. With trivial amalgamating group, "force the overlap loops to agree" forces nothing (there are no nontrivial overlap loops), so the amalgamated free product is just the plain free product. Applying van Kampen and inducting over the $n$ circles:
   $$\pi_1\Big(\bigvee_{k=1}^n S^1\Big)\cong\underbrace{\mathbb{Z}*\cdots*\mathbb{Z}}_{n}=F_n,$$
   one free generator per circle. $\;\blacksquare$

For $n\ge 2$ this group is **non-abelian**: the word $ab$ (loop $a$ then loop $b$) is a different reduced word from $ba$, and there is no relation to make them equal. Geometrically the two loops cannot be slid past each other.

**Demonstration — $\pi_1$ of the orientable genus-$g$ surface $\Sigma_g$.** $\Sigma_g$ is the sphere with $g$ handles (a torus has $g=1$); it is built from a $4g$-sided polygon by identifying edges in the pattern $a_1b_1a_1^{-1}b_1^{-1}\cdots a_gb_ga_g^{-1}b_g^{-1}$.

1. Let $U$ be the open interior of the polygon — a disk, hence contractible, so $\pi_1(U)=0$. Let $V$ be a neighborhood of the glued boundary, which deformation-retracts onto the boundary's 1-skeleton: after the identifications, the $4g$ edges become $2g$ circles all sharing one vertex, i.e. a wedge of $2g$ circles, so $\pi_1(V)=F_{2g}=\langle a_1,b_1,\dots,a_g,b_g\rangle$. The overlap $U\cap V$ is an annulus, which deformation-retracts onto a circle, so $\pi_1(U\cap V)\cong\mathbb{Z}$.
2. The generator of $\pi_1(U\cap V)\cong\mathbb{Z}$ (the loop going once around near the boundary) maps, under $j_*$ into $V$, to the boundary word $w=\prod_{i=1}^g a_ib_ia_i^{-1}b_i^{-1}$; under $i_*$ into the disk $U$ it maps to the trivial loop (it bounds the disk).
3. Van Kampen's amalgamation says: set these two images equal, i.e. impose $w=1$. Starting from $\pi_1(U)*\pi_1(V)=0*F_{2g}=F_{2g}$, adding the single relation $w=1$ gives
   $$\pi_1(\Sigma_g)=\big\langle\, a_1,b_1,\dots,a_g,b_g \ \big|\ \textstyle\prod_{i=1}^g a_ib_ia_i^{-1}b_i^{-1}=1 \,\big\rangle.$$
   Here $a_ib_ia_i^{-1}b_i^{-1}$ is the **commutator** $[a_i,b_i]$, which measures how far $a_i$ and $b_i$ fail to commute. $\;\blacksquare$

**Worked example — the torus, $g=1$.** The presentation is $\langle a,b\mid aba^{-1}b^{-1}=1\rangle$. The single relation says $ab=ba$: the two generators commute. A free group on two generators that is then forced to be commutative is exactly $\mathbb{Z}\times\mathbb{Z}=\mathbb{Z}^2$ (pairs of integers $(m,n)$ under componentwise addition, $a=(1,0)$, $b=(0,1)$). So $\pi_1(T^2)\cong\mathbb{Z}^2$. This matches intuition: a loop on a torus is classified by how many times it goes around the tube and how many times through the hole — two independent integers. $\;\blacksquare$

> **Connection — pushouts & presentations.**
>
> Van Kampen says $\pi_1$ converts *gluing of spaces* into *amalgamated free products of groups*. Consequently every CW complex (§s9) yields a **presentation** of its $\pi_1$: one generator per 1-cell (edge loop), one relation per 2-cell (its attaching word).

<a id="s5"></a>
### Applications: Brouwer (2D), the fundamental theorem of algebra, no retraction

*A single computation, $\pi_1(S^1)\cong\mathbb{Z}$ (§s3), now does real work. Each proof is the same move: a hypothetical map would induce an impossible homomorphism.*

**Demonstration — there is no retraction $r:D^2\to S^1$.** Here $D^2$ is the closed disk and $S^1$ its boundary circle. A **retraction** is a continuous $r:D^2\to S^1$ that fixes the boundary, i.e. $r\circ\iota=\mathrm{id}_{S^1}$ where $\iota:S^1\hookrightarrow D^2$ is inclusion.

1. Suppose such an $r$ exists. *(hypothesis for contradiction)*
2. Apply the functor $\pi_1$ (§s2) and its laws $(f\circ g)_*=f_*\circ g_*$, $(\mathrm{id})_*=\mathrm{id}$:
   $$r_*\circ \iota_*=(r\circ\iota)_*=(\mathrm{id}_{S^1})_*=\mathrm{id}_{\pi_1(S^1)}=\mathrm{id}_{\mathbb{Z}}.$$
   *(functor laws + §s3)*
3. But $\iota_*:\pi_1(S^1)\to\pi_1(D^2)$ is a homomorphism $\mathbb{Z}\to 0$, because $D^2$ is convex, hence contractible, so $\pi_1(D^2)=0$ (§s2 worked example). Any homomorphism into the trivial group is the zero map; then $r_*\circ\iota_*$ also factors through $0$ and is the zero map $\mathbb{Z}\to\mathbb{Z}$.
4. Step 2 says this composite is $\mathrm{id}_\mathbb{Z}$ (which sends $1\mapsto 1$), while step 3 says it is $0$ (which sends $1\mapsto 0$). Since $1\ne 0$ in $\mathbb{Z}$, this is a contradiction. $\;\blacksquare$

**Demonstration — Brouwer fixed-point theorem in 2D.** Every continuous $f:D^2\to D^2$ has a fixed point.

1. Suppose not: $f(x)\ne x$ for all $x\in D^2$. *(hypothesis for contradiction)*
2. Since $f(x)\ne x$, there is a well-defined ray *starting at $f(x)$ and passing through $x$*. Let $r(x)$ be the point where this ray exits the disk, hitting $S^1$. As $f$ is continuous and $f(x)\ne x$ keeps the ray's direction continuous, $r:D^2\to S^1$ is continuous. *(elementary geometry; continuity from the formula)*
3. If $x\in S^1$, the ray from $f(x)$ through $x$ leaves the disk exactly at $x$, so $r(x)=x$. Thus $r$ is a retraction $D^2\to S^1$.
4. But the previous demonstration proved no such retraction exists — contradiction. $\;\blacksquare$

**Demonstration — the fundamental theorem of algebra.** Every nonconstant polynomial over $\mathbb{C}$ has a root.

1. Let $p(z)=z^n+a_{n-1}z^{n-1}+\cdots+a_0$ with $n\ge1$, and suppose $p(z)\ne 0$ for all $z\in\mathbb{C}$. *(hypothesis for contradiction)*
2. For each radius $R\ge 0$ define the loop in $S^1$
   $$\gamma_R(s)=\frac{p(Re^{2\pi i s})/p(R)}{\big|\,p(Re^{2\pi i s})/p(R)\,\big|}.$$
   This is defined because $p$ never vanishes (denominator never $0$). As $R$ varies continuously, the $\gamma_R$ form a homotopy, so by §s3 the winding number $\deg(\gamma_R)\in\mathbb{Z}$ is *constant* in $R$. At $R=0$ the loop is constant, so $\deg(\gamma_0)=0$; hence $\deg(\gamma_R)=0$ for all $R$. *(homotopy invariance of degree, §s3)*
3. For $R$ very large, the top-degree term $z^n$ dominates the rest (since $|z^n|=R^n$ grows faster than the lower terms), so $p(Re^{2\pi i s})$ winds the same number of times as $(Re^{2\pi i s})^n=R^n e^{2\pi i n s}$, namely $n$ times. So $\deg(\gamma_R)=n$ for large $R$. *(domination estimate + §s3 with $\omega_n$)*
4. Steps 2 and 3 give $0=\deg(\gamma_R)=n$, contradicting $n\ge1$. $\;\blacksquare$

**Worked example — a quadratic must have a root.** Take $p(z)=z^2+1$. For large $R$ the loop $\gamma_R$ winds $n=2$ times (it tracks $z^2$); if $p$ had no root the winding would have to stay $0$. The contradiction $0=2$ forces a root — indeed $z=\pm i$. The topology *predicts existence* before any formula is found. $\;\blacksquare$

> **Connection — one template, many theorems.**
>
> Each proof builds an *impossible homomorphism* out of a hypothetical map, leveraging $\pi_1(S^1)\cong\mathbb{Z}\ne 0$. Brouwer in all dimensions, Borsuk–Ulam, and the hairy-ball theorem follow the same pattern using the higher invariants $H_n$ and degree (§s12).

## Part B · Covering spaces

<a id="s6"></a>
### Covering spaces & the lifting theorems

*Covering spaces are the geometric incarnation of subgroups of $\pi_1$. The "lifting" technique that already powered the circle computation (§s3) is now stated in general.*

> **Definition — covering space.**
>
> A continuous surjection $p:\tilde X\to X$ is a **covering map** if every point $x\in X$ has an open neighborhood $U$ that is **evenly covered**: the preimage $p^{-1}(U)$ is a disjoint union $\bigsqcup_\alpha V_\alpha$ of open sets, each mapped *homeomorphically* onto $U$ by $p$. Picture $U$ with several identical copies ("sheets") stacked above it. The fibers $p^{-1}(x)$ are discrete, and on a connected $X$ they all have the same size — the number of **sheets**. Examples: $\mathbb{R}\to S^1$ (infinitely many sheets, §s3), $S^1\xrightarrow{z\mapsto z^n}S^1$ ($n$ sheets), $S^n\to\mathbb{RP}^n$ (2 sheets, identifying antipodes).

**Lifting theorems.** For a covering $p:(\tilde X,\tilde x_0)\to(X,x_0)$ the following hold (these generalize §s3 steps 1–2):
- **Unique path lifting:** every path in $X$ from $x_0$ has a unique lift to $\tilde X$ from $\tilde x_0$.
- **Homotopy lifting:** every homotopy of paths lifts uniquely.
- **Lifting criterion:** a map $f:(Y,y_0)\to(X,x_0)$ from a path-connected, locally path-connected $Y$ lifts to $\tilde X$ iff
$$f_*\big(\pi_1(Y,y_0)\big)\ \subseteq\ p_*\big(\pi_1(\tilde X,\tilde x_0)\big),$$
and when a lift exists it is unique once $\tilde x_0$ is chosen.

**Demonstration — $p_*$ is injective, and the number of sheets equals an index.**

1. **Injectivity of $p_*$.** Recall a homomorphism is injective iff its kernel is trivial. Suppose $[\tilde\gamma]\in\ker p_*$, i.e. $\tilde\gamma$ is a loop in $\tilde X$ with $p\circ\tilde\gamma\simeq c$ (the constant loop) in $X$. Lift that nullhomotopy using homotopy lifting; by uniqueness the lifted homotopy is a nullhomotopy of $\tilde\gamma$ itself, so $[\tilde\gamma]=1$. Hence $\ker p_*=1$ and $p_*$ embeds $\pi_1(\tilde X,\tilde x_0)$ as a subgroup $H=p_*\pi_1(\tilde X)\le\pi_1(X,x_0)$. *(homotopy lifting + uniqueness)*
2. **Fiber $\leftrightarrow$ cosets.** Assume $\tilde X$ connected. Given a loop class $[\gamma]\in\pi_1(X,x_0)$, lift $\gamma$ from $\tilde x_0$ and record the endpoint $\tilde\gamma(1)\in p^{-1}(x_0)$. This is well defined on classes (homotopy lifting) and surjective onto the fiber (path-connectedness of $\tilde X$). Two classes give the same endpoint iff they differ by an element of $H$ (the difference lifts to a loop). This produces a bijection
   $$p^{-1}(x_0)\ \longleftrightarrow\ H\,\backslash\,\pi_1(X,x_0)\quad(\text{the right cosets of }H).$$
   So the **number of sheets** equals the **index** $[\pi_1(X):H]$ — the number of cosets. $\;\blacksquare$

**Worked example — the $n$-fold cover of the circle.** For $p:S^1\to S^1$, $p(z)=z^n$, the map $p_*:\mathbb{Z}\to\mathbb{Z}$ sends the generator (one loop upstairs) to $n$ loops downstairs, so $p_*(\mathbb{Z})=n\mathbb{Z}$. The fiber over $1$ is the $n$-th roots of unity — $n$ points. And indeed the index $[\mathbb{Z}:n\mathbb{Z}]=n$, the number of cosets $\{0+n\mathbb{Z},\dots,(n-1)+n\mathbb{Z}\}$. Sheets $=$ index, confirmed. $\;\blacksquare$

> **Connection — local-to-global.**
>
> "Evenly covered" is a purely *local* condition, yet it forces the *global* lifting properties. This local-to-global passage is the same spirit as sheaf theory and as the gluing in van Kampen (§s4).

<a id="s7"></a>
### The Galois correspondence: classifying covers & deck transformations

*Connected covering spaces of a nice space $X$ are classified by subgroups of $\pi_1(X)$ — a dictionary formally identical to Galois theory's correspondence between field extensions and subgroups of a Galois group.*

**Theorem (Galois correspondence for covers).** For $X$ path-connected, locally path-connected, and semilocally simply connected,
$$\left\{\begin{array}{c}\text{connected covers}\\ p:(\tilde X,\tilde x_0)\to(X,x_0)\end{array}\right\}\ \longleftrightarrow\ \left\{\begin{array}{c}\text{subgroups}\\ H\le\pi_1(X,x_0)\end{array}\right\},\qquad p\longmapsto p_*\pi_1(\tilde X,\tilde x_0).$$
This is a bijection. Forgetting basepoints, isomorphism classes of covers correspond to *conjugacy classes* of subgroups. The pattern: a **smaller** subgroup gives a **bigger** cover (more sheets, by §s6's index count); the trivial subgroup gives the largest cover, the **universal cover** (§s8).

> **Definition — deck transformation, normal/regular cover.**
>
> A **deck transformation** of $p:\tilde X\to X$ is a homeomorphism $\varphi:\tilde X\to\tilde X$ with $p\circ\varphi=p$ (it shuffles the sheets while staying above each point). These form a group $\mathrm{Deck}(\tilde X/X)$ under composition. A cover is **normal** (also called **regular** or **Galois**) when its subgroup $H=p_*\pi_1(\tilde X)$ is a *normal* subgroup of $\pi_1(X)$ (pocket dictionary: $gHg^{-1}=H$); equivalently, when the deck group acts *transitively* on each fiber (it can move any sheet to any other).

**Demonstration — $\mathrm{Deck}(\tilde X/X)\cong N(H)/H$**, where $N(H)=\{g\in\pi_1(X):gHg^{-1}=H\}$ is the **normalizer** of $H$ (the largest subgroup in which $H$ is normal).

1. A deck transformation is exactly a lift of the covering map $p$ along itself with a prescribed image of $\tilde x_0$. By the lifting criterion (§s6) such a lift exists, sending $\tilde x_0$ to another fiber point indexed by a coset $Hg$, precisely when conjugating $H$ by $g$ returns $H$, i.e. when $g\in N(H)$. So deck transformations are parametrized by elements $g\in N(H)$. *(lifting criterion, §s6)*
2. Two elements $g,g'\in N(H)$ give the *same* deck transformation iff they send $\tilde x_0$ to the same point, iff $Hg=Hg'$, iff $g'g^{-1}\in H$. So the parametrization descends to a bijection from the cosets $N(H)/H$, and one checks it respects composition, giving a group isomorphism
   $$\mathrm{Deck}(\tilde X/X)\ \cong\ N(H)/H.$$
   (The quotient $N(H)/H$ is a group precisely because $H$ is normal in $N(H)$ by definition of the normalizer — pocket dictionary on quotient groups.) $\;\blacksquare$
3. **Special cases.** If the cover is normal, $N(H)=\pi_1(X)$, so $\mathrm{Deck}\cong\pi_1(X)/H$. For the universal cover $H=1$, so $\mathrm{Deck}\cong\pi_1(X)$ itself.

**Worked example.** For $\mathbb{R}\to S^1$ (universal cover, §s3), $H=1$ and $\mathrm{Deck}\cong\pi_1(S^1)=\mathbb{Z}$: the deck transformations are the integer translations $t\mapsto t+n$ of the line, which indeed satisfy $p(t+n)=e^{2\pi i(t+n)}=e^{2\pi it}=p(t)$. For the $n$-fold cover $z\mapsto z^n$, $H=n\mathbb{Z}$ is normal in the abelian $\mathbb{Z}$, and $\mathrm{Deck}\cong\mathbb{Z}/n\mathbb{Z}$: the deck maps are rotations by $n$-th roots of unity. $\;\blacksquare$

> **Connection — to field theory.**
>
> Replace "cover" by "field extension," "subgroup of $\pi_1$" by "subgroup of the Galois group," "deck group" by "Galois group," "universal cover" by "separable closure." Both are instances of one categorical pattern: a fundamental group acting, with subgroups indexing intermediate objects.

<a id="s8"></a>
### The universal cover

*The biggest connected cover: simply connected (§s2), sitting above all the others. It is where $\pi_1$ materializes literally as a group of symmetries (deck transformations).*

**Theorem — existence & universal property.** If $X$ is path-connected, locally path-connected, and **semilocally simply connected** (every point has a neighborhood in which loops are nullhomotopic *in $X$*), then $X$ has a **universal cover** $\tilde X$ with $\pi_1(\tilde X)=1$. It is *universal*: for any connected cover $Y\to X$ there is a covering map $\tilde X\to Y$ over $X$. It is unique up to isomorphism, and
$$X\ \cong\ \tilde X/\pi_1(X),\qquad \mathrm{Deck}(\tilde X/X)\cong\pi_1(X).$$

**Demonstration — construction by homotopy classes of paths.**

1. Fix $x_0$. Define $\tilde X=\{\,[\gamma]:\gamma\text{ a path in }X\text{ starting at }x_0\,\}$, where $[\gamma]$ is the homotopy class rel endpoints. Define $p[\gamma]=\gamma(1)$ (the endpoint). *(definition of the candidate space)*
2. Topologize $\tilde X$: a basic open set is indexed by an evenly-covered neighborhood $U$ of $\gamma(1)$ together with a class $[\gamma]$, consisting of all $[\gamma\cdot\eta]$ for paths $\eta$ inside $U$. Semilocal simple connectivity guarantees this is consistent (small loops in $U$ are nullhomotopic in $X$, so concatenating them does not change the class). One checks $p$ is then a covering map. *(definition + semilocal simple connectivity)*
3. **$\tilde X$ is path-connected:** given $[\gamma]$, the path $t\mapsto[\gamma_t]$, where $\gamma_t$ is $\gamma$ restricted to $[0,t]$, runs from the basepoint class $[c_{x_0}]$ to $[\gamma]$. **$\tilde X$ is simply connected:** a loop in $\tilde X$ based at $[c_{x_0}]$ is itself a homotopy of $\gamma$ in $X$, so its endpoint class equals its start class — the loop is trivial. Hence $\pi_1(\tilde X)=1$. *(definitions of path-connected and simply connected, §s1–s2)*
4. **$\pi_1(X)$ acts as deck transformations:** define $[\alpha]\cdot[\gamma]=[\alpha\cdot\gamma]$ for $[\alpha]\in\pi_1(X,x_0)$. This is a homeomorphism of $\tilde X$ commuting with $p$ (since $(\alpha\cdot\gamma)(1)=\gamma(1)$), it is **free** (no nontrivial $[\alpha]$ fixes a class) and **properly discontinuous**, and its orbit space is $X$. By §s7 this realizes $\mathrm{Deck}(\tilde X/X)\cong\pi_1(X)$ and $X\cong\tilde X/\pi_1(X)$. $\;\blacksquare$

**Worked example — the torus.** The universal cover of $T^2$ is the plane $\mathbb{R}^2$, with covering map $(s,t)\mapsto(e^{2\pi is},e^{2\pi it})$. The deck group is $\mathbb{Z}^2$ acting by integer translations $(s,t)\mapsto(s+m,t+n)$, and the orbit space $\mathbb{R}^2/\mathbb{Z}^2$ is the torus. By the theorem $\pi_1(T^2)\cong\mathrm{Deck}=\mathbb{Z}^2$, confirming the van Kampen computation of §s4. Other examples: $\widetilde{S^1}=\mathbb{R}$ (deck group $\mathbb{Z}$); $\widetilde{\mathbb{RP}^n}=S^n$ (deck group $\mathbb{Z}/2$, the antipodal map). $\;\blacksquare$

> **Connection — geometry & group actions.**
>
> A free, properly discontinuous action of a group $G$ on a simply connected $\tilde X$ produces a space $\tilde X/G$ with $\pi_1(\tilde X/G)\cong G$. This is how flat tori, hyperbolic surfaces, and lens spaces are manufactured — geometry arising from group actions on a universal cover.

## Part C · Homology & beyond

<a id="s9"></a>
### Simplicial & CW complexes

*To compute, we need spaces built from standard bricks. Simplices and cells turn homology into a problem in linear algebra over the integers.*

> **Definition — simplices & $\Delta$-complexes.**
>
> The **standard $n$-simplex** is
> $$\Delta^n=\Big\{(t_0,\dots,t_n)\in\mathbb{R}^{n+1}:t_i\ge0,\ \textstyle\sum_i t_i=1\Big\}.$$
> For $n=0,1,2,3$ this is a point, a segment, a filled triangle, a solid tetrahedron. Its **faces** are obtained by setting one coordinate to $0$ (deleting a vertex). A **$\Delta$-complex** is a space assembled from simplices glued along faces by affine maps, with a chosen ordering of vertices fixing orientations.

> **Definition — CW complex.**
>
> A **CW complex** is built up by dimension ("skeleton by skeleton"): start with a discrete set of **$0$-cells** (points); having built the $(n-1)$-skeleton $X^{(n-1)}$, attach **$n$-cells** $e^n$ (copies of the open disk's interior) via continuous **attaching maps** $\varphi:\partial D^n=S^{n-1}\to X^{(n-1)}$ that glue each cell's boundary to what is already there. ("C" = closure-finite: each cell meets finitely many others; "W" = weak topology.) Spheres, projective spaces, surfaces, and Grassmannians all have small explicit CW structures.

**The boundary operator on simplices.** Orient an $n$-simplex by ordering its vertices $[v_0,\dots,v_n]$. Its **boundary** is the alternating sum of its $(n{-}1)$-dimensional faces:
$$\partial_n[v_0,\dots,v_n]=\sum_{i=0}^{n}(-1)^i\,[v_0,\dots,\widehat{v_i},\dots,v_n],$$
where the hat $\widehat{v_i}$ means "omit vertex $v_i$." The sign $(-1)^i$ records orientation. Intuitively the boundary of a triangle is its three edges, with signs so that they form a consistent loop.

**Demonstration — the fundamental identity $\partial^2=0$** (the boundary of a boundary is empty).

1. Apply $\partial$ twice and expand:
   $$\partial_{n-1}\partial_n[v_0,\dots,v_n]=\sum_{i=0}^{n}(-1)^i\,\partial_{n-1}[v_0,\dots,\widehat{v_i},\dots,v_n].$$
   Each inner boundary is itself an alternating sum over the *remaining* vertices. *(definition of $\partial$ applied twice)*
2. After both deletions we obtain faces missing two vertices $v_i$ and $v_j$ with $i<j$. Such a face arises in exactly two ways: (a) remove $v_i$ first, then $v_j$ — but once $v_i$ is gone, $v_j$ sits in position $j-1$, contributing sign $(-1)^i(-1)^{j-1}$; (b) remove $v_j$ first, then $v_i$ — here $v_i$ keeps position $i$, contributing sign $(-1)^j(-1)^i$. *(careful index bookkeeping)*
3. Add the two signs: since $(-1)^{i+j-1}=-(-1)^{i+j}$, the two terms $(-1)^{i+j-1}$ and $(-1)^{i+j}$ are negatives of each other and cancel. Since every doubly-removed face cancels in a pair, the whole sum is $0$: $\partial_{n-1}\circ\partial_n=0$. $\;\blacksquare$

**Worked example — boundary of a triangle, twice.** Let $[v_0,v_1,v_2]$ be a triangle. Then
$$\partial_2[v_0,v_1,v_2]=[v_1,v_2]-[v_0,v_2]+[v_0,v_1].$$
Apply $\partial_1$ (recall $\partial_1[a,b]=[b]-[a]$):
$$\partial_1\big([v_1,v_2]-[v_0,v_2]+[v_0,v_1]\big)=([v_2]-[v_1])-([v_2]-[v_0])+([v_1]-[v_0])=0.$$
Every vertex appears once with each sign and cancels. This is $\partial^2=0$ in the smallest concrete case. $\;\blacksquare$

The identity $\partial^2=0$ is the algebraic heart of homology: it guarantees $\operatorname{im}\partial_{n+1}\subseteq\ker\partial_n$, so the quotient $\ker\partial_n/\operatorname{im}\partial_{n+1}$ makes sense.

> **Connection — to linear algebra.**
>
> Fix a coefficient ring, usually $\mathbb{Z}$. The **$n$-chains** $C_n$ form the free abelian group on the $n$-cells (formal integer combinations of cells), and each $\partial_n$ is an integer matrix. Homology is then $\ker/\operatorname{im}$ of integer matrices — computable by reducing to *Smith normal form*.

<a id="s10"></a>
### Singular homology

*A definition that works for **every** space with no triangulation required — at the cost of enormous chain groups, redeemed by the powerful theorems of §s11.*

> **Definition — singular simplex, chains, the boundary, homology.**
>
> A **singular $n$-simplex** in $X$ is *any* continuous map $\sigma:\Delta^n\to X$ (the simplex need not be embedded — it can fold or collapse). The **chain group** $C_n(X)$ is the free abelian group on all singular $n$-simplices: its elements are finite formal sums $\sum_i n_i\sigma_i$ with $n_i\in\mathbb{Z}$. The **boundary** $\partial_n:C_n(X)\to C_{n-1}(X)$ uses the same alternating-face formula as §s9, with $\sigma$ restricted to each face. By the §s9 computation $\partial^2=0$, giving a **chain complex**
> $$\cdots\xrightarrow{\ \partial_{n+1}\ }C_n(X)\xrightarrow{\ \partial_n\ }C_{n-1}(X)\xrightarrow{\ \partial_{n-1}\ }\cdots\xrightarrow{\ \partial_1\ }C_0(X)\to 0.$$
> The **$n$-th homology group** is
> $$H_n(X)=\frac{\ker\partial_n}{\operatorname{im}\partial_{n+1}}=\frac{\text{cycles }Z_n}{\text{boundaries }B_n}.$$
> (This quotient is legal because $B_n=\operatorname{im}\partial_{n+1}\subseteq\ker\partial_n=Z_n$, and all groups here are abelian so every subgroup is normal — pocket dictionary.)

> **Concept — what $H_n$ measures.**
>
> A **cycle** is a chain with zero boundary (a "closed" loop, surface, …); a **boundary** is a chain that *is* the boundary of something one dimension up (it "bounds," i.e. is filled in). $H_n$ records the cycles that are **not** filled — the $n$-dimensional holes. Concretely: $H_0$ counts path-components, $H_1$ is the abelianization of $\pi_1$ (below), and higher $H_n$ detect higher-dimensional voids.

**Demonstration — $H_0(X)\cong\mathbb{Z}^{(\#\text{path-components})}$.**

1. Since $\partial_0=0$ (the target is the zero group), every $0$-chain is a cycle: $Z_0=C_0(X)$, the free abelian group on the points of $X$.
2. A singular $1$-simplex is a path $\sigma:[0,1]\to X$ with $\partial_1\sigma=\sigma(1)-\sigma(0)$. So $B_0=\operatorname{im}\partial_1$ is generated by all differences $q-p$ where $p,q$ are joined by a path.
3. Therefore in $H_0=Z_0/B_0$ two points become equal exactly when a path joins them, i.e. when they lie in the same path-component. Choosing one point per path-component gives a basis, so $H_0$ is free abelian with one $\mathbb{Z}$ per path-component. $\;\blacksquare$ *(definition of $\partial_1$ + quotient by boundaries)*

For path-connected $X$ this gives $H_0(X)\cong\mathbb{Z}$. The **augmentation** map $\sum n_i\sigma_i\mapsto\sum n_i$ makes the isomorphism explicit, sending each point to $1$.

**Hurewicz in degree 1.** For path-connected $X$,
$$H_1(X)\ \cong\ \pi_1(X)^{\mathrm{ab}}=\pi_1(X)/[\pi_1(X),\pi_1(X)],$$
the **abelianization** of $\pi_1$. Here $[\pi_1,\pi_1]$ is the **commutator subgroup** (generated by all $aba^{-1}b^{-1}$); quotienting by it forces all elements to commute, producing the largest abelian quotient. In words: homology is $\pi_1$ with the order of loops forgotten.

**Worked examples of $H_1$.**
- For the circle, $\pi_1(S^1)=\mathbb{Z}$ is already abelian, so $H_1(S^1)\cong\mathbb{Z}$.
- For the genus-$g$ surface, abelianizing $\langle a_i,b_i\mid\prod[a_i,b_i]\rangle$ kills all commutators; the lone relation (a product of commutators) becomes trivial, leaving the free abelian group on $2g$ generators: $H_1(\Sigma_g)\cong\mathbb{Z}^{2g}$.
- For a wedge of $n$ circles, abelianizing $F_n$ gives $\mathbb{Z}^n$, so $H_1(\bigvee_n S^1)\cong\mathbb{Z}^n$. $\;\blacksquare$

<a id="s11"></a>
### Homotopy invariance & the exact sequences

*The three pillars that make homology computable: homotopy invariance, the long exact sequence of a pair, and Mayer–Vietoris.*

**Functoriality & homotopy invariance.** A continuous $f:X\to Y$ induces $f_*:H_n(X)\to H_n(Y)$ (push each singular simplex $\sigma$ to $f\circ\sigma$; this commutes with $\partial$, so it sends cycles to cycles and boundaries to boundaries). The functor laws and homotopy invariance hold:
$$(g\circ f)_*=g_*\circ f_*,\qquad (\mathrm{id})_*=\mathrm{id},\qquad f\simeq g\Rightarrow f_*=g_*.$$
By the §s0 argument, $X\simeq Y\Rightarrow H_n(X)\cong H_n(Y)$. In particular a contractible space has the homology of a point: $H_0=\mathbb{Z}$ and $H_n=0$ for $n>0$.

> **Concept — exact sequences (recall pocket dictionary).**
>
> A sequence $\cdots\to A\xrightarrow{f}B\xrightarrow{g}C\to\cdots$ is **exact at $B$** if $\operatorname{im}f=\ker g$. Exactness lets an unknown group be pinned down by its neighbors. A **short exact sequence** $0\to A\to B\to C\to0$ encodes "$A$ injects into $B$, $B$ surjects onto $C$, and $A=\ker(B\to C)$," so $C\cong B/A$.

**Long exact sequence of a pair $(X,A)$.** For a subspace $A\subseteq X$, the **relative homology** $H_n(X,A)$ measures $X$ "modulo" $A$ (chains in $X$, ignoring those living in $A$). These fit into an infinite exact sequence:
$$\cdots\to H_n(A)\xrightarrow{i_*}H_n(X)\xrightarrow{j_*}H_n(X,A)\xrightarrow{\ \partial\ }H_{n-1}(A)\xrightarrow{i_*}H_{n-1}(X)\to\cdots$$
The **connecting map** $\partial$ takes a relative cycle to the boundary it leaves behind inside $A$. Exactness at each spot lets you solve for one group from its neighbors.

**Mayer–Vietoris.** If $X=U\cup V$ with $U,V$ open (interiors covering $X$), there is an exact sequence
$$\cdots\to H_n(U\cap V)\xrightarrow{(i_*,j_*)}H_n(U)\oplus H_n(V)\xrightarrow{k_*-l_*}H_n(X)\xrightarrow{\ \partial\ }H_{n-1}(U\cap V)\to\cdots$$
This is the homology analogue of van Kampen (§s4): it assembles the homology of the whole from overlapping pieces. (Here $\oplus$ is the **direct sum** — pairs of elements added componentwise.)

**Demonstration — Mayer–Vietoris computes $H_n(S^k)$.** We use *reduced* homology $\tilde H_n$, which subtracts one $\mathbb{Z}$ in degree $0$ so that a point has all $\tilde H_n=0$; this only changes $H_0$.

1. Cover $S^k$ by two open sets $U,V$ slightly larger than the upper and lower closed hemispheres. Each is contractible (a hemisphere deformation-retracts to its pole), so $\tilde H_*(U)=\tilde H_*(V)=0$ in all degrees. Their overlap $U\cap V$ is an equatorial band that deformation-retracts onto the equator $S^{k-1}$, so $\tilde H_*(U\cap V)\cong\tilde H_*(S^{k-1})$.
2. Plug into Mayer–Vietoris. For each $n$, the terms $\tilde H_n(U)\oplus\tilde H_n(V)=0$ and $\tilde H_{n-1}(U)\oplus\tilde H_{n-1}(V)=0$ vanish, so the sequence forces the connecting map to be an isomorphism:
   $$\tilde H_n(S^k)\ \xrightarrow{\ \partial\ \cong\ }\ \tilde H_{n-1}(S^{k-1}).$$
   *(exactness with vanishing neighbors: $0\to\tilde H_n(S^k)\xrightarrow{\partial}\tilde H_{n-1}(S^{k-1})\to0$)*
3. **Base case** $S^0$ (two points): $\tilde H_0(S^0)\cong\mathbb{Z}$ (one $\mathbb{Z}$ less than the two-component $H_0=\mathbb{Z}^2$), and $\tilde H_n(S^0)=0$ for $n\ne0$. Shifting the isomorphism up $k$ times from $S^0$ to $S^k$ moves the lone $\mathbb{Z}$ from degree $0$ to degree $k$:
   $$\tilde H_n(S^k)=\begin{cases}\mathbb{Z},&n=k,\\ 0,&\text{otherwise.}\end{cases}$$
4. Converting back to ordinary homology (add one $\mathbb{Z}$ in degree $0$):
   $$H_n(S^k)=\begin{cases}\mathbb{Z},& n=0\text{ or }n=k,\\ 0,&\text{otherwise}\end{cases}\quad(k\ge1),$$
   with $H_0(S^0)=\mathbb{Z}^2$. $\;\blacksquare$

**Worked example — $H_*(S^2)$.** Setting $k=2$: $H_0=\mathbb{Z}$ (connected), $H_1=0$ (no one-dimensional holes — every loop on the sphere contracts), $H_2=\mathbb{Z}$ (one two-dimensional void, the cavity the sphere encloses), and $H_n=0$ for $n\ge3$. This matches the geometric picture of a hollow ball. $\;\blacksquare$

> **Connection — homological algebra.**
>
> The connecting map $\partial$ and the long exact sequence come from the **snake lemma** applied to a short exact sequence of chain complexes. The same machinery powers $\mathrm{Tor}$, $\mathrm{Ext}$, and derived functors throughout algebra.

<a id="s12"></a>
### Computing homology: degree, Euler characteristic, Betti numbers

*Now we compute on $\Delta$-complexes — far smaller than the singular complex but giving the same answer — and read off the numerical invariants.*

**Demonstration — cellular homology of $S^1$, $S^2$, and the torus.** We use minimal CW (cell) structures; chains are integer combinations of cells, and $\partial$ is the cellular boundary (the attaching map's degree onto each lower cell — equivalently, the abelianized edge word for a $2$-cell), not the §s9 simplicial alternating-face formula.

1. **$S^1$** as one vertex $v$ and one edge $a$ glued into a loop. Then $\partial_1 a=v-v=0$, so every $1$-chain is a cycle: $Z_1=\mathbb{Z}\langle a\rangle$. There are no $2$-cells, so $B_1=0$, giving $H_1(S^1)=\mathbb{Z}$. Also $H_0=\mathbb{Z}$ (connected, §s10). So $H_*(S^1)=(\mathbb{Z},\mathbb{Z},0,\dots)$.
2. **$S^2$** as two triangles glued along their entire common boundary (top and bottom of a "pillowcase"), one vertex, ... after the gluing the two $2$-cells with opposite orientations have boundaries that cancel: $\partial_2(f_{\text{top}}-f_{\text{bot}})=0$, giving a $2$-cycle that bounds nothing, so $H_2=\mathbb{Z}$; meanwhile $H_1=0$ and $H_0=\mathbb{Z}$. So $H_*(S^2)=(\mathbb{Z},0,\mathbb{Z},0,\dots)$, matching §s11.
3. **Torus $T^2$** from the square with edge word $aba^{-1}b^{-1}$: one vertex $v$, two edges $a,b$, one face $f$. Compute boundaries. $\partial_1 a=v-v=0$ and $\partial_1 b=0$, so $Z_1=\mathbb{Z} a\oplus\mathbb{Z} b=\mathbb{Z}^2$. The face boundary follows the edge word: $\partial_2 f=a+b-a-b=0$, so $f$ is a $2$-cycle and $B_1=\operatorname{im}\partial_2=0$. Therefore $H_2=\mathbb{Z}\langle f\rangle=\mathbb{Z}$, $H_1=Z_1/B_1=\mathbb{Z}^2$, $H_0=\mathbb{Z}$.
   $$H_*(T^2)=(\mathbb{Z},\ \mathbb{Z}^2,\ \mathbb{Z},\ 0,\dots).$$
   One component, two independent loops (around the tube and through the hole), one enclosed void. $\;\blacksquare$

**Degree of a map $f:S^n\to S^n$.** Since $H_n(S^n)\cong\mathbb{Z}$, the induced map $f_*$ is multiplication by an integer:
$$f_*:H_n(S^n)=\mathbb{Z}\to H_n(S^n)=\mathbb{Z}\quad\text{is multiplication by }\deg f.$$
Its key properties (all from functoriality, §s11): $\deg(\mathrm{id})=1$, $\deg(\text{constant})=0$, $\deg(g\circ f)=\deg g\cdot\deg f$, and the antipodal map $x\mapsto-x$ has degree $(-1)^{n+1}$. Degree drives the hairy-ball theorem and higher-dimensional Brouwer.

**Worked example — the antipodal map on $S^1$ and $S^2$.** On $S^1$, $x\mapsto-x$ is rotation by $\pi$, homotopic to the identity, so degree $(-1)^{1+1}=1$. On $S^2$, the antipodal map reverses orientation and has degree $(-1)^{2+1}=-1$; since $-1\ne1$ it is *not* homotopic to the identity — which is the crux of the hairy-ball theorem (you cannot comb a sphere). $\;\blacksquare$

**Betti numbers & Euler characteristic.** The **$n$-th Betti number** is the rank (number of independent $\mathbb{Z}$ summands) of $H_n$:
$$b_n=\operatorname{rank}H_n(X)=\dim_{\mathbb{Q}}H_n(X;\mathbb{Q}),\qquad \chi(X)=\sum_{n\ge0}(-1)^n b_n.$$
So $b_0=\#$components, $b_1=\#$independent loops, $b_2=\#$independent voids. **Torsion** (finite pieces like the $\mathbb{Z}/2$ in $\mathbb{RP}^2$) is invisible to $b_n$ and $\chi$.

**Demonstration — Euler characteristic from cells equals Euler characteristic from homology.**

1. For a finite complex let $c_n$ = number of $n$-cells, and within $C_n$ write $z_n=\operatorname{rank}Z_n$ (rank of cycles) and $r_n=\operatorname{rank}B_n=\operatorname{rank}(\operatorname{im}\partial_{n+1})$ (rank of boundaries coming *into* degree $n$). Rank–nullity for $\partial_n:C_n\to C_{n-1}$ says $\operatorname{rank}C_n=\operatorname{rank}\ker\partial_n+\operatorname{rank}\operatorname{im}\partial_n$, i.e.
   $$c_n=z_n+r_{n-1}.$$
   *(rank–nullity theorem from linear algebra; $\operatorname{im}\partial_n$ has rank $r_{n-1}$ because it lands in degree $n-1$)*
2. By definition of homology, $b_n=\operatorname{rank}H_n=z_n-r_n$ (rank of cycles minus rank of boundaries). *(definition of $H_n$, §s10)*
3. Form the alternating sum of step 1:
   $$\sum_n(-1)^n c_n=\sum_n(-1)^n\big(z_n+r_{n-1}\big)=\sum_n(-1)^n z_n+\sum_n(-1)^n r_{n-1}.$$
   In the second sum shift the index ($n\to n+1$): $\sum_n(-1)^n r_{n-1}=-\sum_n(-1)^n r_n$. Hence
   $$\sum_n(-1)^n c_n=\sum_n(-1)^n(z_n-r_n)=\sum_n(-1)^n b_n=\chi(X).$$
   *(re-indexing + step 2)* $\;\blacksquare$

So $\chi$ computed by counting cells equals $\chi$ computed from homology — a topological invariant independent of the chosen cell structure. For surfaces this is the classical $V-E+F=2-2g$.

**Worked example — Euler characteristic of the torus, two ways.** From homology: $b_0=1,b_1=2,b_2=1$, so $\chi=1-2+1=0$. From cells (the §s12 structure): $c_0=1,c_1=2,c_2=1$, so $\chi=1-2+1=0$. They agree, as the demonstration guarantees. $\;\blacksquare$

| Space | $\pi_1$ | $H_0,H_1,H_2,\dots$ | $\chi$ |
| --- | --- | --- | --- |
| Point | $1$ | $\mathbb{Z},0,0,\dots$ | $1$ |
| $S^1$ | $\mathbb{Z}$ | $\mathbb{Z},\mathbb{Z},0,\dots$ | $0$ |
| $S^n\ (n\ge2)$ | $1$ | $\mathbb{Z},0,\dots,\mathbb{Z}\,(\deg n),0,\dots$ | $1+(-1)^n$ |
| Torus $T^2$ | $\mathbb{Z}^2$ | $\mathbb{Z},\mathbb{Z}^2,\mathbb{Z},0,\dots$ | $0$ |
| $\Sigma_g$ (genus $g$) | $\langle a_i,b_i\mid\prod[a_i,b_i]\rangle$ | $\mathbb{Z},\mathbb{Z}^{2g},\mathbb{Z},0,\dots$ | $2-2g$ |
| $\bigvee_n S^1$ | $F_n$ (free) | $\mathbb{Z},\mathbb{Z}^n,0,\dots$ | $1-n$ |
| $\mathbb{RP}^2$ | $\mathbb{Z}/2$ | $\mathbb{Z},\ \mathbb{Z}/2,\ 0,\dots$ | $1$ |
| $\mathbb{RP}^n$ ($n$ odd) | $\mathbb{Z}/2$ | $\mathbb{Z},\mathbb{Z}/2,\dots,\mathbb{Z}$ | $0$ |
| $\mathbb{RP}^n$ ($n$ even) | $\mathbb{Z}/2$ | $\mathbb{Z},\mathbb{Z}/2,\dots,0$ | $1$ |

> **Connection — abstract algebra reappears.**
>
> Over $\mathbb{Z}$ the structure theorem for finitely generated abelian groups gives $H_n\cong\mathbb{Z}^{b_n}\oplus(\text{torsion})$. The Betti number $b_n$ is the free rank; the torsion (like $\mathbb{Z}/2$ for $\mathbb{RP}^2$) records subtler "twisting" invisible to $\chi$.

<a id="s13"></a>
### Cohomology & the cup product

*Dualizing chains gives cohomology — the same Betti numbers, but now carrying a **ring** structure that homology lacks. The extra multiplication separates spaces that homology cannot.*

**The cochain complex & cohomology.** Fix a coefficient ring $R$ (e.g. $\mathbb{Z}$ or a field). The **$n$-cochains** are the homomorphisms from chains to $R$:
$$C^n(X;R)=\operatorname{Hom}(C_n(X),R),\qquad \delta=\partial^{*}:C^n\to C^{n+1},\qquad H^n(X;R)=\frac{\ker\delta}{\operatorname{im}\delta}.$$
The **coboundary** $\delta$ is the transpose (dual) of $\partial$: $(\delta\varphi)(c)=\varphi(\partial c)$. Because $\partial^2=0$ (§s9) we get $\delta^2=0$, so cohomology is well defined. The arrows now point **up** in degree, making cohomology **contravariant**: a map $f:X\to Y$ induces $f^*:H^n(Y)\to H^n(X)$ (note the reversed direction).

**Universal coefficients.** There is a short exact sequence (recall: pocket dictionary)
$$0\to \operatorname{Ext}^1_{\mathbb{Z}}(H_{n-1}(X),R)\to H^n(X;R)\to \operatorname{Hom}(H_n(X),R)\to 0.$$
Over a field $R$, the $\operatorname{Ext}$ term vanishes and $H^n\cong\operatorname{Hom}(H_n,R)$, so cohomology has the *same Betti numbers* as homology. The genuinely new content is therefore not additive but **multiplicative**:

> **Definition — cup product & cohomology ring.**
>
> The **cup product** is a multiplication $\smile:H^p(X;R)\times H^q(X;R)\to H^{p+q}(X;R)$ that makes the direct sum $H^*(X;R)=\bigoplus_n H^n(X;R)$ a graded ring (a ring whose elements carry a degree, with $\deg(\alpha\smile\beta)=\deg\alpha+\deg\beta$). It is **graded-commutative**, $\alpha\smile\beta=(-1)^{pq}\beta\smile\alpha$, and **natural**, $f^*(\alpha\smile\beta)=f^*\alpha\smile f^*\beta$.

**Demonstration — the cup product distinguishes $T^2$ from $S^2\vee S^1\vee S^1$.** These two spaces have *identical* homology and cohomology *groups*, so no additive invariant separates them — but their *ring* structures differ.

1. Both have $H^0=\mathbb{Z}$, $H^1=\mathbb{Z}^2$, $H^2=\mathbb{Z}$. (For the torus, §s12; for the wedge, $H^1$ gets a $\mathbb{Z}$ from each circle and $H^2$ a $\mathbb{Z}$ from the sphere.) Additively they are indistinguishable. *(universal coefficients + §s12)*
2. **Torus.** Write $H^1(T^2)=\langle\alpha,\beta\rangle$ (dual to the two loops). The cup product is *nondegenerate*: $\alpha\smile\beta$ generates $H^2(T^2)\cong\mathbb{Z}$, while $\alpha\smile\alpha=0=\beta\smile\beta$ (graded-commutativity forces $\alpha\smile\alpha=-\alpha\smile\alpha$, so $2(\alpha\smile\alpha)=0$, and over $\mathbb{Z}$ in this degree it is $0$). The ring is the exterior algebra $\Lambda[\alpha,\beta]$.
3. **Wedge.** Any two positive-degree classes from *different* wedge summands cup to $0$, because they are supported near disjoint parts of the space that meet only at the basepoint; naturality with the collapse maps forces the product to vanish. In particular $\alpha\smile\beta=0$, which does *not* generate $H^2$. The ring multiplication is trivial in positive degrees.
4. A homotopy equivalence would induce a *ring* isomorphism on $H^*$ (naturality, plus the §s0 argument applied to the ring-valued functor). But step 2 has $\alpha\smile\beta\ne0$ and step 3 has it $=0$ — no ring isomorphism can match them. Hence $T^2\not\simeq S^2\vee S^1\vee S^1$. $\;\blacksquare$

This distinction is completely invisible to homology alone; the cup product is what sees it.

> **Connection — to differential geometry.**
>
> For smooth manifolds, **de Rham cohomology** (closed differential forms modulo exact ones) computes $H^*(X;\mathbb{R})$, and the cup product becomes the **wedge product** of forms. Topology, calculus on manifolds, and ring theory converge in one object.

<a id="s14"></a>
### A glimpse beyond: higher homotopy groups, manifolds & Poincaré duality

*Where the subject opens up: higher $\pi_n$ (rich but hard), the special structure of manifolds, and the duality that organizes their (co)homology.*

> **Definition — higher homotopy groups $\pi_n$.**
>
> $\pi_n(X,x_0)$ is the set of homotopy classes of based maps $S^n\to X$, with a concatenation-style group operation generalizing §s2. For $n\ge2$ these groups are **abelian**. *(Eckmann–Hilton: there are two ways to combine two such maps — along the first or the second sphere coordinate — and each is a unital operation for which the other is a homomorphism; a short algebra argument then forces the two operations to coincide and to be commutative.)* Unlike homology, $\pi_n$ is brutally hard: even $\pi_k(S^n)$ for $k>n$ is largely mysterious — these are the "stable homotopy groups of spheres."

**Hurewicz theorem (general).** If $X$ is simply connected (or more generally $(n{-}1)$-connected) with $n\ge2$, meaning $\pi_k(X)=0$ for $k<n$, then
$$H_k(X)=0\ \ (0<k<n)\quad\text{and}\quad \pi_n(X)\cong H_n(X).$$
The first nonzero homotopy and homology groups agree. This is the bridge from the computable ($H_*$) back to the elusive ($\pi_*$).

**Worked example — $\pi_n(S^n)\cong\mathbb{Z}$.** The sphere $S^n$ ($n\ge2$) is simply connected, so $\pi_k(S^n)=0$ for $k<n$; Hurewicz then gives $\pi_n(S^n)\cong H_n(S^n)\cong\mathbb{Z}$ (§s11). The generator is the identity map, and the integer is the degree of §s12. So "wrapping the $n$-sphere around itself $d$ times" is detected by an integer, exactly as for the circle. $\;\blacksquare$

**Poincaré duality.** For a **closed** (compact, without boundary) **oriented** $n$-manifold $M$,
$$H_k(M;\mathbb{Z})\ \cong\ H^{n-k}(M;\mathbb{Z}),$$
and consequently the Betti numbers are symmetric:
$$b_k(M)=b_{n-k}(M).$$
The isomorphism is given by *cap product* with the fundamental class $[M]\in H_n(M)$ (the class representing the whole manifold). A corollary: for odd-dimensional closed orientable $M$, pairing $b_k=b_{n-k}$ across the middle forces $\chi(M)=0$.

**Demonstration — duality on the genus-$g$ surface.**

1. $\Sigma_g$ is a closed oriented $2$-manifold with $b_0=1,\ b_1=2g,\ b_2=1$ (§s10/§s12). *(established earlier)*
2. Poincaré duality with $n=2$ predicts $b_0=b_2$ (indeed $1=1$, ✓) and $b_1=b_{2-1}=b_1$ (trivially true). The middle pairing $H^1\times H^1\to H^2\cong\mathbb{Z}$ is the cup product of §s13 — the **intersection form** — and Poincaré duality says it is *nondegenerate*. It is skew-symmetric of rank $2g$. *(Poincaré duality + §s13 cup product)*
3. Concretely, each loop $a_i$ has a *dual* loop $b_i$ that it crosses exactly once, and crosses every other generator zero times; in cohomology $\alpha_i\smile\beta_i$ generates $H^2$ while all other cup products vanish. Holes come in dual pairs. $\;\blacksquare$

> **Connection — the larger landscape.**
>
> From here: fiber bundles and the long exact sequence of a fibration, spectral sequences, characteristic classes (Chern, Stiefel–Whitney), K-theory, and the cobordism/surgery program that classifies manifolds. Every road still begins with one idea — a functor from spaces to algebra, computed via exact sequences.

---

*A first course in algebraic topology — concepts, definitions, theorems, and the demonstrations behind them — built as a companion to the General Topology guide. Read once for the shape; return to any box as a reference. Remember: every chapter is one functor turning continuous maps into homomorphisms, so that different algebra proves different spaces.*
