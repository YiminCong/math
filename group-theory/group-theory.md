**English** · [中文](group-theory.zh.md)

# Group Theory & Representations, *the mathematics of symmetry.*

*A full first course in group theory and its representations, built from the axioms and aimed squarely at the place symmetry rules physics — conservation laws, particle multiplets, spin, and the quark model. Every term is defined the first time it appears, every theorem is stated precisely and proved with no gaps, and every abstract idea is anchored by a worked numerical example.*

[← Back to all guides](../README.md)

> **How to read this guide.** We assume only ordinary algebra (manipulating sums, products, and matrices) and a little single-variable calculus (derivatives, the exponential function, Taylor series). Everything specific to group theory — *group*, *subgroup*, *coset*, *homomorphism*, *representation*, *character*, *Lie algebra*, *root*, *weight* — is defined where it is first used and illustrated with real numbers. Nothing is "left to the reader." Where the physics is illuminating we say so, but this is a **math** guide: every claim is proved.

---

## Part A — Groups

<a id="s0"></a>
### Symmetry in physics: why groups are the language of conservation laws and particle classification

A **symmetry** of a system is a transformation you can perform that leaves something essential unchanged. Rotate a perfect sphere about its center: it looks identical afterwards. Shift a uniform crystal by one lattice spacing: identical. Reflect the laws of electromagnetism in a mirror: identical. The deep observation that organizes modern physics is that the *collection of all symmetries of a system has an algebraic structure of its own*, and that structure is a **group**.

Why does this matter? Two reasons drive the entire guide.

First, **conservation laws**. Emmy Noether proved in 1918 that every continuous symmetry of a physical system corresponds to a conserved quantity: invariance under time translation gives conservation of energy, invariance under spatial translation gives conservation of momentum, and invariance under rotation gives conservation of angular momentum. The mathematical object encoding "continuous symmetry" is a **Lie group** (Part C), and the conserved quantity arises from its **Lie algebra** of infinitesimal generators. So the bookkeeping of what stays constant in nature is group theory.

Second, **classification of particles**. In quantum mechanics a state is a vector and a symmetry acts on states by a linear operator. A symmetry group therefore acts on the space of states by a **representation** — a way of realizing abstract group elements as concrete matrices (Part B). States that transform into one another under the symmetry form a **multiplet**, and the possible multiplets are exactly the **irreducible representations** of the group. The proton and neutron form a doublet of an $SU(2)$ symmetry; the lightest mesons and baryons fall into multiplets of $SU(3)$ that exposed the quark substructure of matter. Predicting *which* particles can exist, and how they combine, is representation theory.

So the plan is honest: build the mathematics of groups rigorously, then build the theory of their representations, then specialize to the continuous groups physics actually uses and read the structure back as spin and the quark model. We begin with the single definition everything rests on.

> **Why "group."** A group abstracts exactly the features shared by "things you can do and undo, in sequence": composing two symmetries gives a symmetry, doing nothing is a symmetry, and every symmetry can be reversed. Strip those features to their bare bones and you get four axioms. That those four axioms are enough to force a rich theory is the surprise this guide unfolds.

<a id="s1"></a>
### Groups: the axioms and first examples

**What and why.** We want to capture, abstractly, the algebra of "compose symmetries and undo them," so that one set of theorems applies to integers, rotations, permutations, and matrices all at once.

> **Definition — group.**
> A **group** is a set $G$ together with a **binary operation** $\ast : G\times G \to G$ (a rule that takes two elements $a,b\in G$ and returns an element $a\ast b\in G$) such that the following **axioms** hold:
> 1. **(Closure)** for all $a,b\in G$, the result $a\ast b$ is again in $G$. (This is built into "$\ast: G\times G\to G$.")
> 2. **(Associativity)** for all $a,b,c\in G$, $(a\ast b)\ast c = a\ast(b\ast c)$.
> 3. **(Identity)** there is an element $e\in G$ with $e\ast a = a\ast e = a$ for every $a\in G$.
> 4. **(Inverses)** for each $a\in G$ there is an element $a^{-1}\in G$ with $a\ast a^{-1} = a^{-1}\ast a = e$.
>
> If in addition $a\ast b = b\ast a$ for all $a,b$, the group is **abelian** (commutative). The number of elements $|G|$ is the **order** of the group; if it is finite, $G$ is a **finite group**.

We usually drop the symbol $\ast$ and write $ab$ for $a\ast b$, calling the operation "multiplication"; for abelian groups one often writes it additively as $a+b$ with identity $0$ and inverse $-a$. From the four axioms two basic facts follow that the axioms do not *state* but do *force*.

> **Lemma — uniqueness of identity and inverses.** In any group: (a) the identity $e$ is unique; (b) each element's inverse is unique; (c) $(ab)^{-1} = b^{-1}a^{-1}$.

**Proof.**
1. *(Identity is unique.)* Suppose $e$ and $e'$ both satisfy axiom 3. Then $e = e\ast e'$ (because $e'$ is an identity, so multiplying $e$ by $e'$ returns $e$) $= e'$ (because $e$ is an identity, so multiplying $e'$ by $e$ returns $e'$). Hence $e=e'$. *(uses axiom 3 twice)*
2. *(Inverses are unique.)* Suppose $b$ and $c$ are both inverses of $a$, so $ab=ba=e$ and $ac=ca=e$ (axiom 4). Then $b = b\ast e$ (axiom 3) $= b\ast(a\ast c)$ (since $ac=e$) $= (b\ast a)\ast c$ (associativity, axiom 2) $= e\ast c$ (since $ba=e$) $= c$ (axiom 3). So $b=c$. *(this is why we may write "$a^{-1}$" unambiguously)*
3. *(Socks-and-shoes.)* Compute $(ab)(b^{-1}a^{-1}) = a(bb^{-1})a^{-1}$ (associativity) $= a\,e\,a^{-1}$ (axiom 4) $= aa^{-1}$ (axiom 3) $= e$ (axiom 4). The same computation in the other order gives $(b^{-1}a^{-1})(ab)=e$. By the uniqueness just proved, $b^{-1}a^{-1}$ is the inverse of $ab$. $\blacksquare$

> **Lemma — cancellation.** In any group, $ax=ay$ implies $x=y$, and $xa=ya$ implies $x=y$.

**Proof.** From $ax=ay$, multiply both sides on the left by $a^{-1}$: $a^{-1}(ax)=a^{-1}(ay)$, so $(a^{-1}a)x=(a^{-1}a)y$ (associativity), so $ex=ey$ (inverse), so $x=y$ (identity). The right-hand version is symmetric. $\blacksquare$

**Worked examples.** Each verifies the axioms directly.

- **The integers $(\mathbb{Z},+)$.** Operation is addition; identity is $0$; inverse of $n$ is $-n$; associativity is ordinary arithmetic. Abelian, infinite order.
- **The cyclic group $\mathbb{Z}_n$.** Take the set $\{0,1,\dots,n-1\}$ with operation **addition modulo $n$**: $a+b$ is the remainder of the ordinary sum after dividing by $n$. For $n=4$: $2+3 = 5 = 1 \pmod 4$. Identity $0$; the inverse of $a$ is $n-a$ (and $0^{-1}=0$). Abelian, order $n$. This models the symmetries of an oriented regular $n$-gon under rotation.
- **The symmetric group $S_n$.** The set of all **permutations** of $\{1,2,\dots,n\}$ — bijections (one-to-one and onto maps) from the set to itself — with operation **composition** $(\sigma\tau)(i)=\sigma(\tau(i))$. Identity is the map fixing every point; the inverse is the inverse function. Associativity holds because function composition is always associative. Order $n!$. For $n\ge 3$ it is **non-abelian**: with $\sigma=(1\,2)$ (swap 1 and 2, fix 3) and $\tau=(2\,3)$, compute on the point $1$: $\tau=(2\,3)$ fixes $1$, so $\tau(1)=1$ and $\sigma(1)=2$, giving $(\sigma\tau)(1)=\sigma(\tau(1))=\sigma(1)=2$; whereas $(\tau\sigma)(1)=\tau(\sigma(1))=\tau(2)=3$. Since $2\ne3$, $\sigma\tau\ne\tau\sigma$.
- **The dihedral group $D_n$.** The full symmetry group of a regular $n$-gon, consisting of $n$ rotations and $n$ reflections, order $2n$. Write $r$ for rotation by $2\pi/n$ and $s$ for a fixed reflection. Then every element is $r^k$ or $r^k s$ ($0\le k<n$), and the relations $r^n=e$, $s^2=e$, $srs=r^{-1}$ determine the whole group. It is non-abelian for $n\ge3$, since $sr=r^{-1}s\ne rs$.
- **Matrix groups.** The set $GL_n(\mathbb{R})$ of **invertible** $n\times n$ real matrices under matrix multiplication is a group: closure holds because the product of invertibles is invertible (its inverse is the product of inverses in reverse order), associativity is associativity of matrix multiplication, identity is the matrix $I$, and inverses exist by definition of "invertible." It is non-abelian for $n\ge2$.

> **Pitfall.** Associativity is *not* optional decoration: it is what lets us write products like $abc$ without parentheses and is used in nearly every proof above (uniqueness of inverses, socks-and-shoes, cancellation). A set with a closed operation that fails associativity is not a group, and the theory collapses.

> **Cycle notation, once and for all.** A permutation in $S_n$ is written as a product of **cycles**: $(\,i_1\,i_2\,\cdots\,i_k\,)$ denotes the map sending $i_1\mapsto i_2$, $i_2\mapsto i_3$, …, $i_k\mapsto i_1$, and fixing everything not listed. Disjoint cycles (sharing no entries) commute, because they move separate elements. A **transposition** is a $2$-cycle $(\,i\,j\,)$. Every permutation is a product of disjoint cycles in essentially one way, and every cycle is a product of transpositions, e.g. $(\,1\,2\,3\,)=(\,1\,2\,)(\,2\,3\,)$ — read right to left: $(\,2\,3\,)$ first sends $2\mapsto3$, then $(\,1\,2\,)$ leaves $3$ alone, net $2\mapsto3$; tracing all three points confirms the $3$-cycle. We use this notation throughout.

**A non-example, to sharpen the definition.** The nonzero integers under multiplication, $(\mathbb{Z}\setminus\{0\},\times)$, are *not* a group: closure, associativity, and the identity $1$ all hold, but $2$ has no integer multiplicative inverse ($\tfrac12\notin\mathbb{Z}$). Enlarging to the nonzero **rationals** $(\mathbb{Q}\setminus\{0\},\times)$ repairs this — now $2^{-1}=\tfrac12$ exists — giving a genuine abelian group. The lesson: every one of the four axioms must be checked; dropping the inverse axiom alone is the difference between a group and a mere **monoid**.

<a id="s2"></a>
### Subgroups, cosets, and Lagrange's theorem

**What and why.** Inside a group there are often smaller self-contained groups — the rotations sitting inside all symmetries of a polygon, the even integers inside all integers. Understanding a group often means understanding its subgroups, and the first great theorem says their sizes are tightly constrained.

> **Definition — subgroup.** A subset $H\subseteq G$ is a **subgroup**, written $H\le G$, if $H$ is itself a group under the operation of $G$. Concretely $H$ must satisfy: (i) $e\in H$; (ii) if $a,b\in H$ then $ab\in H$ (closure); (iii) if $a\in H$ then $a^{-1}\in H$.

> **Subgroup test.** A nonempty subset $H\subseteq G$ is a subgroup if and only if $ab^{-1}\in H$ whenever $a,b\in H$.

**Proof.** ($\Rightarrow$) If $H$ is a subgroup and $a,b\in H$, then $b^{-1}\in H$ (property iii) and so $ab^{-1}\in H$ (property ii). ($\Leftarrow$) Suppose $H$ is nonempty and closed under $ab^{-1}$. Pick any $a\in H$ (possible since nonempty). Then $aa^{-1}=e\in H$ (apply the test with $b=a$), giving (i). For any $b\in H$, applying the test to the pair $(e,b)$ gives $eb^{-1}=b^{-1}\in H$, giving (iii). Finally for $a,b\in H$ we have $b^{-1}\in H$, so applying the test to $(a,b^{-1})$ gives $a(b^{-1})^{-1}=ab\in H$, giving (ii). $\blacksquare$

**Example.** In $(\mathbb{Z},+)$ the even integers $2\mathbb{Z}=\{\dots,-2,0,2,4,\dots\}$ form a subgroup: the difference of two even numbers is even. In $D_4$ (order 8) the four rotations $\{e,r,r^2,r^3\}$ form a subgroup isomorphic to $\mathbb{Z}_4$.

> **Definition — coset.** Let $H\le G$ and $g\in G$. The **left coset** of $H$ by $g$ is the set $gH=\{gh : h\in H\}$. The **right coset** is $Hg=\{hg:h\in H\}$.

A coset is $H$ "shifted" by $g$. The key technical fact is that distinct cosets do not overlap at all.

> **Lemma — cosets partition $G$.** For $H\le G$: (a) every element lies in some left coset (namely $g\in gH$); (b) two left cosets are either identical or disjoint; (c) every left coset has exactly $|H|$ elements.

**Proof.**
1. *(a)* Since $e\in H$, we have $g=ge\in gH$. So $g$ belongs to its own coset, and the cosets cover all of $G$.
2. *(b)* Suppose two cosets $aH$ and $bH$ share an element $x$. Then $x=ah_1=bh_2$ for some $h_1,h_2\in H$. Solve: $a = b h_2 h_1^{-1}$. Now take any element $ah\in aH$; substitute to get $ah = b(h_2h_1^{-1}h)$, and $h_2h_1^{-1}h\in H$ because $H$ is closed under products and inverses. Hence $ah\in bH$, proving $aH\subseteq bH$. By the symmetric argument $bH\subseteq aH$, so $aH=bH$. Thus if they share even one element they are equal; otherwise they are disjoint. *(uses subgroup closure)*
3. *(c)* Define the map $\varphi:H\to gH$ by $\varphi(h)=gh$. It is **onto** by definition of $gH$. It is **one-to-one**: if $gh_1=gh_2$ then $h_1=h_2$ by left cancellation. A bijection between finite sets means equal size, so $|gH|=|H|$. $\blacksquare$

> **Definition — index.** The number of distinct left cosets of $H$ in $G$ is the **index** $[G:H]$.

> **Theorem — Lagrange.** If $G$ is a finite group and $H\le G$, then $|H|$ divides $|G|$, and precisely $|G| = [G:H]\,|H|$.

**Proof.**
1. By the Lemma, the distinct left cosets of $H$ form a **partition** of $G$: every element of $G$ lies in exactly one of them (part (a) gives coverage; part (b) gives non-overlap). Let there be $k=[G:H]$ distinct cosets, call them $g_1H,\dots,g_kH$.
2. Since these $k$ sets are disjoint and cover $G$, the total count is the sum of their sizes: $|G| = |g_1H| + \cdots + |g_kH|$. *(counting a partition)*
3. Each coset has exactly $|H|$ elements by part (c). So $|G| = k\,|H| = [G:H]\,|H|$.
4. Therefore $|H|$ divides $|G|$. $\blacksquare$

> **Corollary — order of an element divides $|G|$.** The **order** of an element $a$ is the smallest positive integer $m$ with $a^m=e$. The set $\langle a\rangle=\{e,a,a^2,\dots,a^{m-1}\}$ is a subgroup of size $m$ (the **cyclic subgroup generated by $a$**), so by Lagrange $m$ divides $|G|$. In particular $a^{|G|}=e$ for every $a$.

**Worked example.** In $S_3$ (order $6$) Lagrange forbids any subgroup of order $4$ or $5$, since neither divides $6$. The allowed subgroup orders are $1,2,3,6$, and indeed $S_3$ has the trivial subgroup, three subgroups of order $2$ (generated by each transposition), one of order $3$ (the rotations $\{e,(1\,2\,3),(1\,3\,2)\}$), and itself.

> **Corollary — groups of prime order are cyclic.** If $|G|=p$ is prime, take any $a\ne e$. The order of $a$ divides $p$ and exceeds $1$, so it equals $p$; hence $\langle a\rangle$ has $p$ elements and must be all of $G$. So $G\cong\mathbb{Z}_p$. Prime-order groups have no nontrivial subgroups at all — they are the indivisible "atoms" among finite groups.

**Worked example — Fermat's little theorem from Lagrange.** Take $G=(\mathbb{Z}_p^\times,\times)$, the nonzero residues mod a prime $p$ under multiplication; this is a group of order $p-1$. By the corollary "$a^{|G|}=e$," every nonzero residue satisfies $a^{p-1}\equiv 1\pmod p$. For $p=7$ and $a=3$: $3^6=729=7\cdot104+1\equiv1\pmod7$. A purely number-theoretic fact falls straight out of a counting theorem about cosets — a first taste of why group theory unifies so much.

> **Pitfall.** Lagrange is a *one-way* statement: $|H|$ divides $|G|$. The converse fails — a divisor of $|G|$ need not be the order of any subgroup. The smallest counterexample is the alternating group $A_4$ (order $12$), which has *no* subgroup of order $6$.

<a id="s3"></a>
### Normal subgroups, quotient groups, homomorphisms, and the first isomorphism theorem

**What and why.** We want to build a *new, smaller* group whose elements are the cosets of $H$. For the multiplication of cosets to even make sense, $H$ must be special — **normal**. The payoff is the single most useful theorem in elementary group theory: every homomorphism is, up to relabeling, a quotient.

> **Definition — normal subgroup.** $N\le G$ is **normal**, written $N\trianglelefteq G$, if $gNg^{-1}=N$ for every $g\in G$ — equivalently, the left and right cosets coincide, $gN=Ng$ for all $g$. (In an abelian group every subgroup is normal.)

> **Definition — homomorphism.** A map $\phi:G\to G'$ between groups is a **homomorphism** if it respects the operation: $\phi(ab)=\phi(a)\phi(b)$ for all $a,b\in G$. Its **kernel** is $\ker\phi=\{g\in G:\phi(g)=e'\}$ and its **image** is $\mathrm{im}\phi=\{\phi(g):g\in G\}$. A bijective homomorphism is an **isomorphism**, written $G\cong G'$; isomorphic groups are "the same group with relabeled elements."

> **Lemma — homomorphisms preserve structure.** For a homomorphism $\phi:G\to G'$: (a) $\phi(e)=e'$; (b) $\phi(a^{-1})=\phi(a)^{-1}$; (c) $\ker\phi$ is a normal subgroup of $G$; (d) $\phi$ is one-to-one if and only if $\ker\phi=\{e\}$.

**Proof.**
1. *(a)* $\phi(e)=\phi(ee)=\phi(e)\phi(e)$ (homomorphism). Cancel one $\phi(e)$ (left-multiply by its inverse in $G'$): $e'=\phi(e)$.
2. *(b)* $\phi(a)\phi(a^{-1})=\phi(aa^{-1})=\phi(e)=e'$, and likewise on the other side; by uniqueness of inverses $\phi(a^{-1})=\phi(a)^{-1}$.
3. *(c, subgroup)* If $a,b\in\ker\phi$ then $\phi(ab^{-1})=\phi(a)\phi(b)^{-1}=e'(e')^{-1}=e'$, so $ab^{-1}\in\ker\phi$; by the subgroup test $\ker\phi\le G$. *(normal)* For $g\in G$ and $n\in\ker\phi$: $\phi(gng^{-1})=\phi(g)\phi(n)\phi(g)^{-1}=\phi(g)\,e'\,\phi(g)^{-1}=e'$, so $gng^{-1}\in\ker\phi$. Hence $g(\ker\phi)g^{-1}\subseteq\ker\phi$ for all $g$, which gives equality (apply also to $g^{-1}$), so $\ker\phi\trianglelefteq G$.
4. *(d)* If $\phi$ is one-to-one, only $e$ can map to $e'=\phi(e)$, so $\ker\phi=\{e\}$. Conversely if $\ker\phi=\{e\}$ and $\phi(a)=\phi(b)$, then $\phi(ab^{-1})=\phi(a)\phi(b)^{-1}=e'$, so $ab^{-1}\in\ker\phi=\{e\}$, giving $ab^{-1}=e$, i.e. $a=b$. $\blacksquare$

> **Definition and theorem — quotient group.** If $N\trianglelefteq G$, the set of cosets $G/N=\{gN:g\in G\}$ becomes a group under the operation $(aN)(bN)=(ab)N$, called the **quotient group**.

**Proof that the operation is well defined and gives a group.**
1. *(Well defined.)* The trouble is that a coset has many names: $aN=a'N$ when $a'=an$ for some $n\in N$. We must check the product does not depend on the chosen names. Suppose $aN=a'N$ and $bN=b'N$, so $a'=an_1$, $b'=bn_2$ with $n_1,n_2\in N$. Then $a'b' = a n_1 b n_2$. Insert $b^{-1}b=e$: $a'b' = a b\,(b^{-1}n_1 b)\,n_2$. Now $b^{-1}n_1 b\in N$ because $N$ is normal ($b^{-1}Nb=N$). So $a'b' = ab\,(\text{element of }N)$, which means $(a'b')N=(ab)N$. The product of cosets is therefore unambiguous. *(this is exactly where normality is needed)*
2. *(Group axioms.)* Associativity: $((aN)(bN))(cN)=(ab)N\cdot cN=((ab)c)N=(a(bc))N=(aN)((bN)(cN))$, using associativity in $G$. Identity: $eN=N$ satisfies $(N)(aN)=aN=(aN)(N)$. Inverse: $(aN)^{-1}=a^{-1}N$, since $(aN)(a^{-1}N)=(aa^{-1})N=eN$. All axioms hold. $\blacksquare$

> **Theorem — First Isomorphism Theorem.** Let $\phi:G\to G'$ be a homomorphism. Then $\mathrm{im}\phi$ is a subgroup of $G'$, $\ker\phi\trianglelefteq G$, and
>
> $$
> G/\ker\phi \;\cong\; \mathrm{im}\phi .
> $$

**Proof.** Write $K=\ker\phi$, which is normal by the Lemma, so $G/K$ is a group.
1. Define $\Phi:G/K\to\mathrm{im}\phi$ by $\Phi(gK)=\phi(g)$.
2. *(Well defined.)* If $gK=g'K$ then $g'=gk$ for some $k\in K$, so $\phi(g')=\phi(g)\phi(k)=\phi(g)e'=\phi(g)$. The value does not depend on the representative.
3. *(Homomorphism.)* $\Phi((gK)(hK))=\Phi((gh)K)=\phi(gh)=\phi(g)\phi(h)=\Phi(gK)\Phi(hK)$.
4. *(Onto.)* Every element of $\mathrm{im}\phi$ is $\phi(g)=\Phi(gK)$ for some $g$, so $\Phi$ is onto.
5. *(One-to-one.)* Suppose $\Phi(gK)=e'$, i.e. $\phi(g)=e'$. Then $g\in K$, so $gK=K$, the identity coset. Thus the kernel of $\Phi$ is trivial, and by part (d) of the Lemma $\Phi$ is injective.
6. A bijective homomorphism is an isomorphism, so $G/K\cong\mathrm{im}\phi$. $\blacksquare$

**Worked example.** Let $\phi:\mathbb{Z}\to\mathbb{Z}_n$ send an integer to its remainder mod $n$. This is a homomorphism: the remainder of a sum is the sum of remainders mod $n$. It is onto, and its kernel is the multiples of $n$, $n\mathbb{Z}$. The theorem gives $\mathbb{Z}/n\mathbb{Z}\cong\mathbb{Z}_n$ — the clock arithmetic group is literally the integers with multiples of $n$ collapsed to zero. A second example: the **sign** homomorphism $\mathrm{sgn}:S_n\to\{+1,-1\}$ (multiplicative group of two elements) sends a permutation to $+1$ if it is a product of an even number of transpositions and $-1$ otherwise; its kernel is the **alternating group** $A_n$, and $S_n/A_n\cong\{\pm1\}$, so $A_n$ has index $2$ and thus $|A_n|=n!/2$.

<a id="s4"></a>
### Group actions, orbits and stabilizers, and the orbit–stabilizer theorem

**What and why.** Groups become powerful when they *act* on a set — when each group element moves the points of some space around. Symmetries of a molecule act on its atoms; rotations act on points of a sphere; a symmetry group acts on quantum states. Counting orbits and stabilizers is how we extract numerical information from symmetry.

> **Definition — group action.** A (left) **action** of a group $G$ on a set $X$ is a map $G\times X\to X$, written $g\cdot x$, such that: (i) $e\cdot x = x$ for all $x$; (ii) $g\cdot(h\cdot x) = (gh)\cdot x$ for all $g,h\in G$, $x\in X$.

> **Definition — orbit and stabilizer.** For $x\in X$, the **orbit** is $\mathrm{Orb}(x)=\{g\cdot x : g\in G\}$ — everywhere $x$ can be sent. The **stabilizer** is $\mathrm{Stab}(x)=\{g\in G : g\cdot x = x\}$ — the elements that fix $x$.

> **Lemma.** $\mathrm{Stab}(x)$ is a subgroup of $G$.

**Proof.** $e\in\mathrm{Stab}(x)$ by (i). If $g,h$ fix $x$ then $(gh)\cdot x = g\cdot(h\cdot x)=g\cdot x = x$, so $gh$ fixes $x$. If $g\cdot x=x$, apply $g^{-1}$: $g^{-1}\cdot(g\cdot x)=g^{-1}\cdot x$, and the left side is $(g^{-1}g)\cdot x = e\cdot x = x$, so $g^{-1}\cdot x = x$. All three subgroup conditions hold. $\blacksquare$

> **Theorem — Orbit–Stabilizer.** For a group $G$ acting on $X$ and any $x\in X$, there is a bijection between the orbit $\mathrm{Orb}(x)$ and the set of left cosets of $\mathrm{Stab}(x)$. Hence for finite $G$,
>
> $$
> |\mathrm{Orb}(x)| = [\,G : \mathrm{Stab}(x)\,] = \frac{|G|}{|\mathrm{Stab}(x)|}.
> $$

**Proof.** Write $S=\mathrm{Stab}(x)$.
1. Define $\psi: G/S \to \mathrm{Orb}(x)$ by $\psi(gS)=g\cdot x$.
2. *(Well defined.)* If $gS=g'S$ then $g'=gs$ for some $s\in S$, so $g'\cdot x = (gs)\cdot x = g\cdot(s\cdot x)=g\cdot x$. The value depends only on the coset.
3. *(One-to-one.)* If $g\cdot x = g'\cdot x$, apply $g^{-1}$ on the left: $x = (g^{-1}g')\cdot x$, so $g^{-1}g'\in S$, which means $g'\in gS$, i.e. $gS=g'S$. Distinct cosets give distinct points.
4. *(Onto.)* Any point of the orbit is $g\cdot x=\psi(gS)$ for some $g$.
5. So $\psi$ is a bijection, giving $|\mathrm{Orb}(x)|=[G:S]$, and by Lagrange this equals $|G|/|S|$ when $G$ is finite. $\blacksquare$

**Worked example.** Let $G=D_4$ (order $8$) act on the four vertices of a square, $X=\{1,2,3,4\}$. The orbit of vertex $1$ is all four vertices (any vertex can be rotated to any other), so $|\mathrm{Orb}(1)|=4$. The stabilizer of vertex $1$ consists of the identity and the reflection through the diagonal containing vertex $1$ — two elements. Check the theorem: $|\mathrm{Orb}(1)|\cdot|\mathrm{Stab}(1)| = 4\cdot 2 = 8 = |G|$. Knowing only that the action is *transitive* (one orbit of size $4$) and that $|G|=8$, we deduce the stabilizer has order $2$ without listing it.

**Worked counting application — colorings of a triangle.** How many genuinely different ways are there to color the $3$ vertices of an equilateral triangle with $2$ colors, where rotations of the triangle count as the same? The rotation group is $\mathbb{Z}_3=\{e,r,r^2\}$ acting on the $2^3=8$ colorings. **Burnside's lemma** (a consequence of orbit–stabilizer: the number of orbits equals the average number of fixed points, $\frac{1}{|G|}\sum_g|\text{Fix}(g)|$) gives the count. The identity fixes all $8$ colorings; each nontrivial rotation $r,r^2$ fixes only the $2$ monochromatic colorings (all vertices must match). So the number of distinct colorings is $\frac{1}{3}(8+2+2)=4$. Listing them confirms it: all-color-A, all-color-B, two-A-one-B, two-B-one-A. Symmetry counting reduces a fiddly combinatorial question to one average.

> **Intuition.** The orbit measures how far $x$ can move; the stabilizer measures how much of the group "wastes its effort" leaving $x$ fixed. Their sizes multiply to $|G|$ because each point in the orbit is reached by exactly $|\mathrm{Stab}(x)|$ group elements (a full coset).

<a id="s5"></a>
### Conjugacy classes

**What and why.** Within a group, some elements are "the same kind of operation seen from a different viewpoint" — for instance all reflections of a square are conjugate. Sorting elements into **conjugacy classes** is the bridge to characters and the eventual reading of representations.

> **Definition — conjugacy.** Elements $a,b\in G$ are **conjugate** if $b = gag^{-1}$ for some $g\in G$. This is an equivalence relation (reflexive via $g=e$; symmetric via $g^{-1}$; transitive by composing the conjugators), so it partitions $G$ into disjoint **conjugacy classes**. The class of $a$ is $\mathrm{Cl}(a)=\{gag^{-1}:g\in G\}$.

Conjugation by $g$ is itself the action $g\cdot a = gag^{-1}$ of $G$ on itself (one checks (i) and (ii)), so the conjugacy class is exactly an orbit. The stabilizer of $a$ under this action is the **centralizer** $C_G(a)=\{g:ga=ag\}$. Orbit–stabilizer then gives a class-size formula for free:
$$
|\mathrm{Cl}(a)| = \frac{|G|}{|C_G(a)|},
$$
so every class size divides $|G|$.

**Worked example in $S_3$.** Permutations are conjugate in $S_n$ exactly when they have the same **cycle type** (the same pattern of cycle lengths), because conjugating $(\,i\,j\,k\,\cdots)$ by $g$ just relabels the entries to $(\,g(i)\,g(j)\,g(k)\,\cdots)$. So we read off the classes of $S_3$ by cycle type:
- $\{e\}$ — the identity, cycle type "three fixed points." Size $1$.
- $\{(1\,2),(1\,3),(2\,3)\}$ — the transpositions, cycle type "one 2-cycle." Size $3$.
- $\{(1\,2\,3),(1\,3\,2)\}$ — the 3-cycles. Size $2$.

Check: $1+3+2 = 6 = |S_3|$, and each size ($1,3,2$) divides $6$, consistent with the class-size formula. The number of conjugacy classes here is $3$; we will see in s8 that this equals the number of irreducible representations.

**Worked verification of the relabeling rule.** Conjugate $(1\,2\,3)$ by $g=(1\,2)$ in $S_3$. The rule says $g(1\,2\,3)g^{-1}=(g(1)\,g(2)\,g(3))=(2\,1\,3)=(1\,3\,2)$. Check directly: $g^{-1}=(1\,2)$, and we evaluate $g(1\,2\,3)g^{-1}$ on the point $2$ — read right to left: $g^{-1}$ sends $2\mapsto1$, then $(1\,2\,3)$ sends $1\mapsto2$, then $g$ sends $2\mapsto1$, net $2\mapsto1$. And $(1\,3\,2)$ indeed sends $2\mapsto1$. Tracing the other points confirms $g(1\,2\,3)g^{-1}=(1\,3\,2)$, exactly the predicted relabeling. So the two $3$-cycles are genuinely conjugate, as the class structure claimed.

> **The class equation.** Splitting $G$ into conjugacy classes and counting gives $|G|=\sum_i |\mathrm{Cl}(a_i)| = |Z(G)| + \sum_{\text{nontrivial classes}} \frac{|G|}{|C_G(a_i)|}$, where the **center** $Z(G)=\{z : zg=gz\ \forall g\}$ collects the singleton classes. For $S_3$: $6 = 1 + 3 + 2$, with center $\{e\}$ only (size $1$). This equation is the lever behind many structural theorems — for instance, it forces every group of prime-power order to have a nontrivial center.

> **Pitfall.** Conjugate elements are *not* generally equal, and the relation depends on the whole group: two elements conjugate in a larger group may fail to be conjugate in a subgroup. Cycle type characterizes conjugacy in $S_n$ specifically, not in arbitrary groups.

## Part B — Representations

<a id="s6"></a>
### Representations: definition, equivalence, reducibility, unitarity

**What and why.** A representation realizes the abstract elements of a group as concrete matrices acting on a vector space — turning group theory into linear algebra, where eigenvalues and bases are available. In quantum mechanics the symmetry group acts on states exactly this way, so representations *are* the multiplets of physics.

> **Definition — representation.** A **representation** of a group $G$ on a finite-dimensional complex vector space $V$ is a homomorphism $\rho: G\to GL(V)$, where $GL(V)$ is the group of invertible linear maps $V\to V$. Equivalently, after choosing a basis, $\rho$ assigns to each $g$ an invertible $d\times d$ matrix $\rho(g)$ with $\rho(gh)=\rho(g)\rho(h)$. The number $d=\dim V$ is the **dimension** (or **degree**) of the representation. The **trivial representation** sends every $g$ to the number $1$ (degree $1$).

The homomorphism property forces $\rho(e)=I$ and $\rho(g^{-1})=\rho(g)^{-1}$ (s3 Lemma applied to $\rho$).

> **Definition — equivalence.** Two representations $\rho,\rho'$ on spaces $V,V'$ of the same dimension are **equivalent** if there is an invertible linear map $T:V\to V'$ with $T\rho(g)=\rho'(g)T$ for all $g$, i.e. $\rho'(g)=T\rho(g)T^{-1}$. Equivalent representations are the same representation in different coordinates.

> **Definition — invariant subspace and reducibility.** A subspace $W\subseteq V$ is **invariant** if $\rho(g)W\subseteq W$ for every $g$ (the group never pushes a vector of $W$ out of $W$). A representation is **reducible** if it has an invariant subspace other than $\{0\}$ and $V$; otherwise it is **irreducible**. If $V$ splits as a direct sum $V=W_1\oplus W_2$ of two invariant subspaces, the representation is **completely reducible** (decomposable) into the pieces it induces on $W_1$ and $W_2$.

> **Definition — unitary representation.** A representation is **unitary** if every $\rho(g)$ is a **unitary matrix**, meaning $\rho(g)^\dagger\rho(g)=I$ where $\rho(g)^\dagger$ is the conjugate transpose. Unitary maps preserve the inner product $\langle u,v\rangle$, hence preserve length and angle — physically, they preserve total probability.

**Worked example.** The cyclic group $\mathbb{Z}_n=\{0,1,\dots,n-1\}$ has, for each integer $k$ with $0\le k<n$, a one-dimensional representation $\rho_k(m)=e^{2\pi i\,km/n}$. Check the homomorphism property: $\rho_k(m+m')=e^{2\pi i k(m+m')/n}=e^{2\pi i km/n}e^{2\pi i km'/n}=\rho_k(m)\rho_k(m')$, and addition is mod $n$ but $e^{2\pi i k n/n}=1$ so the mod-$n$ wrap does not matter. Each $\rho_k(m)$ is a unit-modulus complex number, hence unitary. These $n$ representations are the complete list of irreducibles of $\mathbb{Z}_n$.

**A second worked example — the regular representation of $\mathbb{Z}_3$.** Let $\mathbb{Z}_3=\{0,1,2\}$ act on $V=\mathbb{C}^3$ by *permuting the coordinates cyclically*: the generator $1$ acts by the matrix that sends $(x_0,x_1,x_2)\mapsto(x_2,x_0,x_1)$,
$$
P=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}.
$$
This is a $3$-dimensional representation (the **regular representation**). It is *reducible*: the all-ones vector $(1,1,1)$ spans a $1$-dimensional invariant subspace (it is fixed by $P$). The orthogonal complement, spanned by vectors summing to zero, is also invariant and splits further over $\mathbb{C}$ into the two remaining one-dimensional irreducibles $\rho_1,\rho_2$ of s6's first example. So $\rho_{\text{reg}}\cong\rho_0\oplus\rho_1\oplus\rho_2$, each appearing once — a preview of the general fact that the regular representation contains every irreducible exactly $\dim(\rho_i)$ times.

> **Intuition.** "Irreducible" means "cannot be broken into smaller invariant pieces" — the atoms of representation theory. The whole subject is: find all irreducibles, then write any representation as a sum of them. Section 7 guarantees this is always possible for finite groups.

<a id="s7"></a>
### Schur's lemma and Maschke's theorem

**What and why.** Two structural theorems make finite-group representation theory clean. **Maschke** says every representation breaks into irreducible pieces (no leftover "indecomposable but reducible" mess). **Schur** pins down the maps between irreducibles so tightly that it forces the orthogonality relations of the next section.

> **Theorem — Maschke.** Every finite-dimensional representation of a finite group $G$ over $\mathbb{C}$ is completely reducible: it is a direct sum of irreducible representations.

**Proof.** The engine is **averaging over the group**, which only works because $G$ is finite (we divide by $|G|$).
1. *(Make it unitary.)* Start with any inner product $\langle\,,\rangle_0$ on $V$ and average it over the group:
$$
\langle u,v\rangle \;=\; \frac{1}{|G|}\sum_{g\in G}\langle \rho(g)u,\;\rho(g)v\rangle_0 .
$$
This is again a valid inner product (a sum of inner products is positive-definite and conjugate-symmetric). It is **$G$-invariant**: for any $h$,
$$
\langle \rho(h)u,\rho(h)v\rangle = \frac{1}{|G|}\sum_{g}\langle \rho(g)\rho(h)u,\rho(g)\rho(h)v\rangle_0 = \frac{1}{|G|}\sum_{g'}\langle \rho(g')u,\rho(g')v\rangle_0 = \langle u,v\rangle,
$$
where we substituted $g'=gh$; as $g$ runs over $G$ so does $g'$ (this is the **rearrangement** valid because right-multiplication by $h$ permutes $G$). Invariance means each $\rho(h)$ preserves $\langle\,,\rangle$, i.e. $\rho$ is **unitary** with respect to this inner product.
2. *(Split off any invariant subspace.)* Suppose $W\subseteq V$ is invariant and proper. Let $W^\perp=\{v:\langle v,w\rangle=0\ \forall w\in W\}$ be its orthogonal complement, so $V=W\oplus W^\perp$ (a basic fact of inner-product spaces). Claim $W^\perp$ is also invariant. Take $v\in W^\perp$, $w\in W$, and any $g$. Then
$$
\langle \rho(g)v,\,w\rangle = \langle v,\,\rho(g)^{-1}w\rangle,
$$
using that $\rho(g)$ is unitary so its adjoint is $\rho(g)^{-1}$. Since $W$ is invariant, $\rho(g)^{-1}w=\rho(g^{-1})w\in W$, and $v\perp W$, so this inner product is $0$. As $w$ was arbitrary, $\rho(g)v\in W^\perp$. Hence $W^\perp$ is invariant.
3. *(Induct.)* If $V$ is irreducible we are done. Otherwise it has a proper invariant $W$, and by step 2, $V=W\oplus W^\perp$ with both pieces invariant. Each piece has smaller dimension, so by induction on $\dim V$ each decomposes into irreducibles, and so does $V$. $\blacksquare$

> **Theorem — Schur's Lemma.** Let $\rho:G\to GL(V)$ and $\sigma:G\to GL(W)$ be irreducible representations, and let $T:V\to W$ be a linear map that **intertwines** them, meaning $T\rho(g)=\sigma(g)T$ for all $g$. Then:
> (a) either $T=0$ or $T$ is an isomorphism;
> (b) if $V=W$ and $\sigma=\rho$ (over $\mathbb{C}$), then $T=\lambda I$ for some scalar $\lambda$.

**Proof.**
1. *(a, kernel.)* $\ker T$ is invariant under $\rho$: if $v\in\ker T$ then $T(\rho(g)v)=\sigma(g)Tv=\sigma(g)0=0$, so $\rho(g)v\in\ker T$. Since $\rho$ is irreducible, $\ker T$ is $\{0\}$ or all of $V$. If $\ker T=V$ then $T=0$.
2. *(a, image.)* $\mathrm{im}T$ is invariant under $\sigma$: any element is $Tv$, and $\sigma(g)(Tv)=T(\rho(g)v)\in\mathrm{im}T$. Since $\sigma$ is irreducible, $\mathrm{im}T$ is $\{0\}$ or all of $W$. If $T\ne0$, then $\ker T=\{0\}$ (injective) and $\mathrm{im}T=W$ (onto), so $T$ is an isomorphism.
3. *(b.)* Now $V=W$ over $\mathbb{C}$. Since $\mathbb{C}$ is algebraically closed and $V$ is finite-dimensional, $T$ has an eigenvalue $\lambda$ (a root of its characteristic polynomial). Consider $T-\lambda I$. It also intertwines $\rho$ with itself, because $(T-\lambda I)\rho(g)=T\rho(g)-\lambda\rho(g)=\rho(g)T-\lambda\rho(g)=\rho(g)(T-\lambda I)$. But $T-\lambda I$ has nontrivial kernel (the $\lambda$-eigenspace is nonzero), so by part (a) it cannot be an isomorphism; hence $T-\lambda I=0$, i.e. $T=\lambda I$. $\blacksquare$

**Worked consequence — irreducible representations of abelian groups are 1-dimensional.** Let $G$ be abelian and $\rho$ an irreducible representation over $\mathbb{C}$. Fix any $h\in G$; the matrix $\rho(h)$ commutes with every $\rho(g)$ because $\rho(h)\rho(g)=\rho(hg)=\rho(gh)=\rho(g)\rho(h)$ (using that $G$ is abelian). By Schur (b), $\rho(h)=\lambda_h I$ for a scalar. But then *every* one-dimensional subspace is invariant (a scalar matrix preserves all lines), so irreducibility forces $\dim V=1$. This is why $\mathbb{Z}_n$ had only the $n$ one-dimensional irreducibles of s6, and why the harmonics $e^{2\pi i km/n}$ are the complete story for abelian symmetry — Fourier analysis is exactly the representation theory of abelian groups.

> **Why this matters.** Schur (b) says the only matrices commuting with *all* of an irreducible representation are scalars — the representation is "as non-degenerate as possible." This rigidity is precisely what makes the matrix entries of irreducibles orthogonal, which is the content of the next section and the engine of character tables.

<a id="s8"></a>
### Characters and orthogonality; building a character table

**What and why.** Carrying around whole matrices is unwieldy. The **character** — the trace of each representation matrix — distills a representation to one number per conjugacy class, yet retains enough information to identify it completely. Orthogonality relations turn "decompose into irreducibles" into simple arithmetic.

> **Definition — character.** The **character** of a representation $\rho$ is the function $\chi_\rho(g)=\mathrm{tr}\rho(g)$ (the trace, the sum of diagonal entries). Key facts, all from properties of the trace: (i) $\chi_\rho(e)=\dim V$ (trace of $I$); (ii) $\chi_\rho$ is **constant on conjugacy classes** (a **class function**), because $\mathrm{tr}(\rho(g)\rho(a)\rho(g)^{-1})=\mathrm{tr}\rho(a)$ by the cyclic property of trace; (iii) equivalent representations have equal characters (trace is basis-independent).

Define the **inner product of class functions** by
$$
\langle \chi,\psi\rangle = \frac{1}{|G|}\sum_{g\in G}\overline{\chi(g)}\,\psi(g).
$$

> **Theorem — orthogonality of irreducible characters.** If $\chi$ and $\psi$ are the characters of irreducible representations of a finite group $G$ over $\mathbb{C}$, then
>
> $$
> \langle \chi,\psi\rangle = \begin{cases} 1 & \text{if the two representations are equivalent},\\ 0 & \text{otherwise}.\end{cases}
> $$

**Proof (sketch with the load-bearing steps complete).**
1. For representations $\rho$ (on $V$) and $\sigma$ (on $W$) and *any* linear map $A:V\to W$, form the averaged map $\tilde A=\frac{1}{|G|}\sum_g \sigma(g)A\rho(g)^{-1}$. A substitution $g\mapsto hg$ shows $\sigma(h)\tilde A=\tilde A\rho(h)$, so $\tilde A$ intertwines.
2. By Schur's Lemma: if $\rho\not\cong\sigma$ then $\tilde A=0$ for every choice of $A$; if $\rho=\sigma$ then $\tilde A=\lambda I$ with $\lambda=\frac{\mathrm{tr}A}{\dim V}$ (take traces of both sides of $\tilde A=\lambda I$, using that averaging preserves trace).
3. Choosing $A$ to be the elementary matrices (a single $1$ entry) and reading off components gives the **Grand Orthogonality relations** among matrix entries; summing the diagonal entries (taking traces) collapses these to the character statement above. The non-equivalent case yields $0$; the equal case yields $\frac{1}{|G|}\sum_g|\chi(g)|^2 = 1$. $\blacksquare$

Two corollaries make characters a complete bookkeeping tool:

> **Corollary — decomposition and counting.** Any representation decomposes as $\rho\cong\bigoplus_i m_i\,\rho_i$ over the distinct irreducibles $\rho_i$, and the multiplicities are recovered by $m_i=\langle\chi_{\rho_i},\chi_\rho\rangle$. A representation is irreducible if and only if $\langle\chi_\rho,\chi_\rho\rangle=1$. Moreover **the number of inequivalent irreducible representations equals the number of conjugacy classes**, and the dimensions $d_i$ satisfy $\sum_i d_i^2 = |G|$.

**Worked example — the character table of $S_3$.** From s5, $S_3$ has $3$ conjugacy classes: $\{e\}$ (size $1$), the transpositions $\{(1\,2),(1\,3),(2\,3)\}$ (size $3$), and the 3-cycles $\{(1\,2\,3),(1\,3\,2)\}$ (size $2$). So there are exactly $3$ irreducibles. Their dimensions satisfy $d_1^2+d_2^2+d_3^2=6$; the only positive-integer solution is $1+1+4$, i.e. dimensions $1,1,2$.
- The **trivial** representation: $\chi(g)=1$ for all $g$.
- The **sign** representation: $\chi(g)=\mathrm{sgn}(g)$, which is $+1$ on $e$, $-1$ on transpositions, $+1$ on 3-cycles.
- The **2-dimensional standard** representation $\rho_{\text{std}}$: realize $S_3$ as the symmetries of an equilateral triangle acting on the plane. Then $\rho(e)=I$ has trace $2$; a reflection (transposition) has trace $0$ (it has eigenvalues $+1,-1$); a $120^\circ$ rotation (3-cycle) has trace $2\cos120^\circ=-1$.

Assemble the table (columns headed by a class representative, with the class size above):

| | $e$ (1) | $(1\,2)$ (3) | $(1\,2\,3)$ (2) |
|---|---|---|---|
| trivial | $1$ | $1$ | $1$ |
| sign | $1$ | $-1$ | $1$ |
| standard | $2$ | $0$ | $-1$ |

Check orthogonality of "standard" with itself, weighting each class by its size: $\langle\chi,\chi\rangle=\frac{1}{6}\big(1\cdot2^2 + 3\cdot0^2 + 2\cdot(-1)^2\big)=\frac{1}{6}(4+0+2)=1$, confirming it is irreducible. Check "trivial" against "sign": $\frac{1}{6}(1\cdot1\cdot1 + 3\cdot1\cdot(-1) + 2\cdot1\cdot1)=\frac{1}{6}(1-3+2)=0$, confirming they are inequivalent. The table is consistent and complete.

**Decomposing a representation with characters.** Suppose we hand $S_3$ the $6$-dimensional regular representation $\rho_{\text{reg}}$ (permuting the group's own elements). Its character is easy: $\chi_{\text{reg}}(g)$ counts the elements fixed by left-multiplication by $g$, which is $|G|=6$ if $g=e$ and $0$ otherwise (no non-identity element fixes anything under left multiplication). So $\chi_{\text{reg}}=(6,0,0)$ on the classes $(e,\text{transposition},\text{3-cycle})$. The multiplicities are
$$
m_i=\langle\chi_{\rho_i},\chi_{\text{reg}}\rangle=\frac{1}{6}\big(\,\overline{\chi_{\rho_i}(e)}\cdot 6\,\big)=\chi_{\rho_i}(e)=d_i,
$$
since only the identity class contributes. Reading dimensions off the table: $m_{\text{triv}}=1$, $m_{\text{sign}}=1$, $m_{\text{std}}=2$. So $\rho_{\text{reg}}\cong\text{triv}\oplus\text{sign}\oplus 2\cdot\text{std}$, and a dimension check gives $1+1+2\cdot2=6$. This confirms the general theorem that each irreducible appears in the regular representation exactly $d_i$ times, and re-derives $\sum d_i^2=|G|$.

> **Pitfall.** Orthogonality sums must weight each conjugacy class by its size (or equivalently sum over all group elements, not over classes). Forgetting the class sizes is the most common arithmetic error in building a character table.

## Part C — Continuous groups and physics

<a id="s9"></a>
### Continuous (Lie) groups: the key matrix groups

**What and why.** Rotations, Lorentz boosts, and gauge transformations form *continuous* families — you can rotate by any angle, not just discrete amounts. Such groups are **Lie groups**: groups that are also smooth manifolds, so calculus applies. The ones physics lives on are all groups of matrices.

> **Definition — Lie group (working version).** A **matrix Lie group** is a subgroup $G\subseteq GL_n(\mathbb{C})$ that is **closed** under taking limits of sequences that stay invertible — concretely a group of matrices defined by smooth (differentiable) constraints, so that near the identity it looks like a piece of $\mathbb{R}^k$. The number $k$ is the **dimension** of the group: the number of independent real parameters needed to specify an element.

The fundamental examples, with the constraint that defines each:

- **$GL_n(\mathbb{R})$, $GL_n(\mathbb{C})$** — the **general linear groups**: all invertible $n\times n$ real (resp. complex) matrices. The constraint is just $\det\ne0$. Dimension $n^2$ (real) or $2n^2$ (real dimension, complex case).
- **$O(n)$** — the **orthogonal group**: real matrices with $A^{\mathsf T}A=I$. The condition $A^{\mathsf T}A=I$ says $A$ preserves the dot product, hence lengths and angles; these are the rigid motions of $\mathbb{R}^n$ fixing the origin (rotations and reflections). Taking $\det$ of $A^{\mathsf T}A=I$ gives $(\det A)^2=1$, so $\det A=\pm1$.
- **$SO(n)$** — the **special orthogonal group**: $A\in O(n)$ with $\det A=+1$. These are the pure **rotations** (reflections excluded). $SO(3)$ is the rotation group of physical space.
- **$U(n)$** — the **unitary group**: complex matrices with $U^\dagger U=I$ ($\dagger$ = conjugate transpose). They preserve the complex inner product $\langle u,v\rangle=\sum \bar u_i v_i$, hence preserve quantum probabilities. Taking $\det$ gives $|\det U|=1$, so $\det U=e^{i\theta}$.
- **$SU(n)$** — the **special unitary group**: $U\in U(n)$ with $\det U=+1$. $SU(2)$ governs spin; $SU(3)$ governs the strong interaction's color and the light-quark flavor symmetry.

**Worked example — $SO(2)$.** Every element is a rotation $R(\theta)=\begin{pmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{pmatrix}$. One checks $R(\theta)^{\mathsf T}R(\theta)=I$ and $\det R(\theta)=\cos^2\theta+\sin^2\theta=1$, and $R(\theta)R(\phi)=R(\theta+\phi)$ (angle addition formulas), so $SO(2)$ is a one-parameter abelian group, geometrically a circle. Its dimension is $1$.

> **Counting dimensions.** $SU(2)$: a $2\times2$ unitary matrix has $4$ complex = $8$ real parameters; $U^\dagger U=I$ imposes $4$ real conditions and $\det=1$ imposes $1$ more, leaving $8-4-1=3$. So $SU(2)$ is $3$-dimensional — matching the $3$ rotation axes of space, a coincidence we explain in s11.

**Worked example — every $SU(2)$ element explicitly.** Solving the constraints shows every element of $SU(2)$ has the form
$$
U=\begin{pmatrix} \alpha & -\bar\beta \\ \beta & \bar\alpha \end{pmatrix},\qquad |\alpha|^2+|\beta|^2=1,
$$
with $\alpha,\beta\in\mathbb{C}$. Writing $\alpha=a_0+ia_3$, $\beta=a_2+ia_1$ with real $a_\mu$, the constraint becomes $a_0^2+a_1^2+a_2^2+a_3^2=1$ — the unit sphere $S^3$ in four dimensions. So $SU(2)$ is geometrically a $3$-sphere: connected and "simply connected" (no holes), which is the precise reason it is the universal cover of $SO(3)$ and why spin-$\tfrac12$ exists. The three independent parameters are visible as the three angles needed to locate a point on $S^3$.

> **Containment relations.** These groups nest: $SU(n)\subset U(n)\subset GL_n(\mathbb{C})$ and $SO(n)\subset O(n)\subset GL_n(\mathbb{R})\subset GL_n(\mathbb{C})$. The "$S$" (special) groups are the **connected** pieces containing the identity, obtained by dropping the orientation-reversing reflections (which sit in the $\det=-1$ component, disconnected from the identity). This is why $SO(n)$, not $O(n)$, is the proper home of continuous rotation: you cannot continuously deform a reflection into the identity without passing through a non-orthogonal matrix.

<a id="s10"></a>
### Lie algebras, generators, the exponential map, and structure constants

**What and why.** A Lie group is curved and hard to handle directly, but its behavior *near the identity* is a flat vector space — the **Lie algebra** — that captures almost everything. Physicists call its basis vectors **generators**; the exponential map rebuilds the group from them. This linearization is why infinitesimal symmetries (and Noether's conserved currents) are computable.

> **Definition — Lie algebra of a matrix group.** For a matrix Lie group $G$, its **Lie algebra** $\mathfrak{g}$ is the set of matrices $X$ such that $e^{tX}\in G$ for all real $t$, where the **matrix exponential** is the convergent series
>
> $$
> e^{X} = \sum_{k=0}^{\infty}\frac{X^k}{k!} = I + X + \tfrac{1}{2}X^2 + \cdots .
> $$
>
> Elements of $\mathfrak{g}$ are the **infinitesimal generators**: $X=\frac{d}{dt}\big|_{t=0}e^{tX}$ is the velocity through the identity along the curve $t\mapsto e^{tX}$.

> **Theorem — the algebra is closed under the commutator.** If $X,Y\in\mathfrak g$ then the **commutator** $[X,Y]=XY-YX$ is also in $\mathfrak g$. Thus $\mathfrak g$ is a real vector space closed under the bracket $[\,,]$; this is the abstract structure called a **Lie algebra**.

**Worked derivation of the defining conditions.** The conditions on $X$ come from differentiating the group's defining equation at $t=0$.
1. *(Orthogonal/$SO(n)$.)* The condition is $A^{\mathsf T}A=I$. Put $A=e^{tX}$, note $(e^{tX})^{\mathsf T}=e^{tX^{\mathsf T}}$, so $e^{tX^{\mathsf T}}e^{tX}=I$. Differentiate at $t=0$ using $\frac{d}{dt}e^{tX}\big|_0=X$ and the product rule: $X^{\mathsf T}+X=0$. So $\mathfrak{so}(n)$ is the **antisymmetric** matrices ($X^{\mathsf T}=-X$). The $\det=1$ condition adds nothing infinitesimally because $\det e^{tX}=e^{t\mathrm{tr}X}$ and antisymmetric matrices already have zero trace.
2. *(Unitary/$SU(n)$.)* The condition $U^\dagger U=I$ with $U=e^{tX}$ and $(e^{tX})^\dagger=e^{tX^\dagger}$ differentiates to $X^\dagger+X=0$: $\mathfrak{u}(n)$ is the **anti-Hermitian** matrices. The extra $\det=1$ gives, from $\det e^{tX}=e^{t\mathrm{tr}X}=1$, the **traceless** condition $\mathrm{tr}X=0$. So $\mathfrak{su}(n)$ = traceless anti-Hermitian matrices.

**Proof that $[X,Y]\in\mathfrak g$.** Consider the smooth curve $\gamma(t)=e^{\sqrt t\,X}e^{\sqrt t\,Y}e^{-\sqrt t\,X}e^{-\sqrt t\,Y}$ in $G$ (a product of group elements, hence in $G$). Expanding each exponential to second order in $\sqrt t$ and multiplying out, the zeroth and first-order terms cancel and one finds $\gamma(t)=I+t[X,Y]+O(t^{3/2})$. Hence $\frac{d}{dt}\gamma(t)\big|_{t=0^+}=[X,Y]$ is a tangent vector to $G$ at the identity, i.e. lies in $\mathfrak g$. $\blacksquare$

> **Definition — structure constants.** Fix a basis $T_1,\dots,T_k$ of $\mathfrak g$ (the **generators**). Since $\mathfrak g$ is closed under the bracket, each $[T_a,T_b]$ is a combination of the $T_c$:
>
> $$
> [T_a,T_b] = \sum_c f_{ab}{}^{c}\,T_c .
> $$
>
> The numbers $f_{ab}{}^c$ are the **structure constants**; they encode the entire local structure of the group. They are **antisymmetric** in $a,b$ (since $[T_a,T_b]=-[T_b,T_a]$) and satisfy a quadratic identity coming from the **Jacobi identity** $[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0$ (which holds for commutators by direct expansion).

**Worked example — the exponential is rotation.** Take the single generator $X=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ of $\mathfrak{so}(2)$ (antisymmetric, as the theory demands). Compute its powers: $X^2=-I$, $X^3=-X$, $X^4=I$, repeating with period $4$. Summing the exponential series and grouping even and odd powers,
$$
e^{\theta X}=\sum_k\frac{\theta^k X^k}{k!} = \Big(1-\tfrac{\theta^2}{2!}+\cdots\Big)I + \Big(\theta-\tfrac{\theta^3}{3!}+\cdots\Big)X = \cos\theta\,I + \sin\theta\,X = \begin{pmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{pmatrix}.
$$
We recover exactly $R(\theta)\in SO(2)$ from s9. So the single antisymmetric generator, exponentiated, sweeps out the whole rotation group — a concrete instance of the algebra rebuilding the group.

> **Why the exponential rebuilds the group.** For each connected matrix Lie group, every element near the identity is $e^{X}$ for some $X\in\mathfrak g$, and products of such exponentials reach the whole connected group. So knowing the finitely many structure constants determines the group's local — and for connected, simply connected groups, global — multiplication. This is the sense in which the algebra is a faithful shadow of the group.

> **Pitfall.** $e^{X}e^{Y}\ne e^{X+Y}$ unless $X$ and $Y$ commute; the correct relation is the **Baker–Campbell–Hausdorff formula** $e^Xe^Y=e^{X+Y+\frac12[X,Y]+\cdots}$, whose higher terms are built entirely from nested commutators — i.e. from the structure constants. This non-commutativity of exponentials is the algebraic shadow of the group being non-abelian, and it is why the commutator, not the sum, is the fundamental operation of a Lie algebra.

<a id="s11"></a>
### $\mathfrak{su}(2)$ and $\mathfrak{so}(3)$: spin and the irreducible representations of angular momentum

**What and why.** This is where the abstract machinery becomes physics. The rotation group $SO(3)$ and the spin group $SU(2)$ share one Lie algebra, and *its* irreducible representations are exactly the allowed values of angular momentum and spin. We will derive the spectrum $j=0,\tfrac12,1,\tfrac32,\dots$ from the algebra alone.

**The generators.** A basis for $\mathfrak{su}(2)$ (traceless anti-Hermitian $2\times2$) is $-\tfrac{i}{2}\sigma_a$ where the **Pauli matrices** are
$$
\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad \sigma_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad \sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$
Physicists prefer the Hermitian generators $J_a=\tfrac12\sigma_a$ (so that $\rho(g)=e^{-i\theta_a J_a}$ with real angles). A direct computation of the products gives the **commutation relations**
$$
[J_a,J_b]=i\sum_c \epsilon_{abc}\,J_c,
$$
where $\epsilon_{abc}$ is the totally antisymmetric symbol ($\epsilon_{123}=1$). The structure constants are $f_{ab}{}^c=\epsilon_{abc}$.

**Same algebra as $\mathfrak{so}(3)$.** The generators of $SO(3)$ are the antisymmetric matrices $(L_a)_{bc}=-\epsilon_{abc}$ (infinitesimal rotations about each axis), and one computes their commutators are *also* $[L_a,L_b]=\sum_c\epsilon_{abc}L_c$ (same structure constants up to the $i$ convention). So $\mathfrak{su}(2)\cong\mathfrak{so}(3)$ as Lie algebras. Yet the *groups* differ: there is a 2-to-1 homomorphism $SU(2)\to SO(3)$ ($+U$ and $-U$ give the same rotation), which is exactly why a spin-$\tfrac12$ state changes sign under a $360^\circ$ rotation — a measurable physical fact.

> **Theorem — irreducible representations of $\mathfrak{su}(2)$.** The finite-dimensional irreducible representations are labeled by a single number $j\in\{0,\tfrac12,1,\tfrac32,2,\dots\}$. Representation $j$ has dimension $2j+1$, with a basis of states $|j,m\rangle$ for $m=-j,-j+1,\dots,j-1,j$, on which the generators act by
>
> $$
> J_3|j,m\rangle = m\,|j,m\rangle,\qquad J_\pm|j,m\rangle = \sqrt{j(j+1)-m(m\pm1)}\;|j,m\pm1\rangle,
> $$
>
> where $J_\pm=J_1\pm iJ_2$ are the **raising/lowering operators**.

**Proof (the highest-weight construction).**
1. *(Commutators of the ladder operators.)* From $[J_a,J_b]=i\epsilon_{abc}J_c$ one computes $[J_3,J_\pm]=\pm J_\pm$ and $[J_+,J_-]=2J_3$. The first relation says $J_\pm$ shifts the $J_3$-eigenvalue by $\pm1$: if $J_3|m\rangle=m|m\rangle$ then $J_3(J_\pm|m\rangle)=(J_\pm J_3 + [J_3,J_\pm])|m\rangle=(m\pm1)J_\pm|m\rangle$. *(this is why they are "ladder" operators)*
2. *(The Casimir.)* The operator $J^2=J_1^2+J_2^2+J_3^2$ commutes with every $J_a$ (direct check using the relations), so by Schur's Lemma (s7) it acts as a single scalar on an irreducible representation; call that scalar $j(j+1)$ (any nonnegative scalar can be written this way for a unique $j\ge0$).
3. *(Finite-dimensional forces a top rung.)* In a finite-dimensional representation the eigenvalues $m$ of the Hermitian operator $J_3$ are bounded. Let $|j,j\rangle$ be a **highest-weight** state with the largest $m$, so $J_+|j,j\rangle=0$ (there is no higher rung). Using $J_-J_+=J^2-J_3^2-J_3$, apply to $|j,j\rangle$: $0=(j(j+1)-m^2-m)|j,j\rangle$ at the top, forcing the top value $m=j$ (taking the nonnegative root), which is why we named it $j$.
4. *(Build the rest by lowering.)* Apply $J_-$ repeatedly to get states with $m=j,j-1,j-2,\dots$. The norm computation $\|J_-|j,m\rangle\|^2 = \langle j,m|J_+J_-|j,m\rangle = j(j+1)-m(m-1)$ (using $J_+J_-=J^2-J_3^2+J_3$) gives exactly the coefficient quoted, and it must stay $\ge0$.
5. *(Termination quantizes $j$.)* The ladder must stop at some bottom rung $m=-j'$, where $J_-|j,-j'\rangle=0$ forces (by the analogous bottom computation) $j'=j$. The number of steps from $+j$ down to $-j$ must be a nonnegative integer, so $2j\in\{0,1,2,\dots\}$, i.e. $j\in\{0,\tfrac12,1,\tfrac32,\dots\}$. The dimension is the number of rungs, $2j+1$. $\blacksquare$

**Worked example — spin $\tfrac12$.** Here $j=\tfrac12$, dimension $2$, states $|{\uparrow}\rangle=|\tfrac12,\tfrac12\rangle$ and $|{\downarrow}\rangle=|\tfrac12,-\tfrac12\rangle$. Then $J_3=\tfrac12\mathrm{diag}(1,-1)$, $J_+|{\downarrow}\rangle=\sqrt{\tfrac12\cdot\tfrac32-(-\tfrac12)(\tfrac12)}\,|{\uparrow}\rangle=|{\uparrow}\rangle$, recovering exactly $J_a=\tfrac12\sigma_a$. This is the electron's spin. The next case $j=1$ (dimension $3$) is the spin-1 / vector representation, realized by ordinary $3$-vectors under $SO(3)$.

<a id="s12"></a>
### $SU(3)$, roots and weights, and the quark model

**What and why.** $SU(3)$ is the symmetry that organized the "particle zoo" of the 1960s into neat geometric patterns and revealed that protons and neutrons are made of quarks. The mathematics is a higher-rank version of the $\mathfrak{su}(2)$ ladder: instead of one $J_3$ there are two simultaneously diagonalizable generators, so states live on a $2$-dimensional lattice.

**The algebra.** $\mathfrak{su}(3)$ is the traceless anti-Hermitian $3\times3$ matrices, dimension $8$ (count: $9$ complex entries = $18$ real, minus $9$ for anti-Hermiticity, minus $1$ for traceless = $8$). A standard basis is the **Gell-Mann matrices** $\lambda_1,\dots,\lambda_8$, with Hermitian generators $T_a=\tfrac12\lambda_a$ satisfying $[T_a,T_b]=i\sum_c f_{abc}T_c$.

> **Definition — Cartan subalgebra, weights, roots.** The **Cartan subalgebra** $\mathfrak h$ is a maximal set of generators that mutually commute; its dimension is the **rank**. For $\mathfrak{su}(3)$ the rank is $2$: $T_3=\tfrac12\lambda_3$ and $T_8=\tfrac1{2\sqrt3}\lambda_8$ commute. In any representation these are simultaneously diagonalizable; the pair of eigenvalues $(t_3,y)$ of a common eigenstate is its **weight**, a point in the $2$-dimensional **weight plane**. (Physically $t_3$ is the third component of **isospin** and $y$ is the **hypercharge**.) The **roots** are the weights of the **adjoint representation** — the action of the algebra on itself by the bracket — and they are the analogues of the $\pm1$ shifts of the $\mathfrak{su}(2)$ ladder operators, now arranged as six vectors forming a regular hexagon.

> **The ladder structure.** Just as $J_\pm$ moved states between $J_3$-eigenvalues, $\mathfrak{su}(3)$ has six "stepping" operators (one per root) that move a state from one weight to a neighboring weight in the plane. A representation is built from a **highest-weight** state by applying lowering operators, exactly as in s11, but now in two directions; the resulting set of weights forms a symmetric polygon.

**Worked concretely — the fundamental and its conjugate.** The defining $3$-dimensional representation $\mathbf{3}$ (matrices acting on $\mathbb{C}^3$) has three weights forming a triangle; identify the three basis states with the lightest **quarks**:
$$
u:\ (t_3,y)=(\tfrac12,\tfrac13),\qquad d:\ (-\tfrac12,\tfrac13),\qquad s:\ (0,-\tfrac23).
$$
The conjugate representation $\overline{\mathbf 3}$ has the negated weights and describes the **antiquarks** $\bar u,\bar d,\bar s$. Larger multiplets are built by tensoring (s13): combining a quark and an antiquark gives the meson octet, $\mathbf3\otimes\overline{\mathbf3}=\mathbf8\oplus\mathbf1$; combining three quarks gives the baryon multiplets, $\mathbf3\otimes\mathbf3\otimes\mathbf3=\mathbf{10}\oplus\mathbf8\oplus\mathbf8\oplus\mathbf1$. The decuplet $\mathbf{10}$ is the famous triangular pattern whose missing corner — predicted by the math before it was found — was the $\Omega^-$ baryon, discovered in 1964. The Gell-Mann–Nishijima relation $Q=t_3+\tfrac12 y$ recovers each particle's electric charge from its weight; for the $u$ quark, $Q=\tfrac12+\tfrac12\cdot\tfrac13=\tfrac23$, the correct fractional charge.

**Worked example — the meson octet weights.** Combine a quark weight with an antiquark weight by *adding* the weight vectors (s13). For example $u\bar s$ has weight $(\tfrac12,\tfrac13)+(0,\tfrac23)=(\tfrac12,1)$ — this is the $K^+$ meson, with charge $Q=t_3+\tfrac12 y=\tfrac12+\tfrac12=1$, correct. Running through all nine $q\bar q$ pairs and plotting their summed weights produces a hexagon with two states at the center, exactly the spin-zero pseudoscalar meson octet (the $\pi$, $K$, and $\eta$ mesons), plus one extra central state forming the singlet — matching $\mathbf3\otimes\overline{\mathbf3}=\mathbf8\oplus\mathbf1$. The geometry is not analogy; it is the literal weight diagram.

> **Rank and the number of good quantum numbers.** A rank-$r$ group has $r$ mutually commuting generators, hence $r$ simultaneously measurable conserved quantum numbers labeling states within a multiplet. For $\mathfrak{su}(2)$ ($r=1$) that is the single $m=J_3$ of s11; for $\mathfrak{su}(3)$ ($r=2$) it is the pair (isospin $t_3$, hypercharge $y$). This is why a spin state needs one label but a hadron in an $SU(3)$ multiplet needs two — the rank of the symmetry group dictates how many "addresses" a state carries.

> **Intuition.** The lesson of $SU(3)$ is that *geometry in the weight plane is physics*: each point is a particle, each multiplet is a polygon, and the requirement that polygons close up under the root-vector steps quantizes which multiplets — which families of particles — can exist. The quark model is, at heart, the statement that observed hadrons fill out the irreducible representations of $SU(3)$.

<a id="s13"></a>
### Tensor products and Clebsch–Gordan decomposition

**What and why.** Combining two systems — two spins, a quark and an antiquark — corresponds to the **tensor product** of their representations. The combined representation is reducible, and decomposing it into irreducibles is exactly "addition of angular momentum." This is the operation that built every multiplet in s12.

> **Definition — tensor product of representations.** Given representations $\rho:G\to GL(V)$ and $\sigma:G\to GL(W)$, the **tensor product** acts on the space $V\otimes W$ (spanned by symbols $v\otimes w$, of dimension $\dim V\cdot\dim W$) by $(\rho\otimes\sigma)(g)\,(v\otimes w)=\rho(g)v\otimes\sigma(g)w$. For Lie algebra generators this becomes the **sum** $J_a^{\text{tot}}=J_a\otimes I + I\otimes J_a$ — which is precisely why physicists "add" angular momenta.

> **Character of a tensor product.** Taking the trace of $(\rho\otimes\sigma)(g)$ factorizes: $\chi_{\rho\otimes\sigma}(g)=\chi_\rho(g)\,\chi_\sigma(g)$. Combined with the multiplicity formula $m_i=\langle\chi_{\rho_i},\chi_{\rho\otimes\sigma}\rangle$ from s8, this reduces *any* decomposition to multiplying and integrating characters.

> **Theorem — Clebsch–Gordan series for $\mathfrak{su}(2)$.** The tensor product of the spin-$j_1$ and spin-$j_2$ representations decomposes as
>
> $$
> j_1\otimes j_2 \;=\; (j_1+j_2)\ \oplus\ (j_1+j_2-1)\ \oplus\ \cdots\ \oplus\ |j_1-j_2| ,
> $$
>
> each total spin $J$ from $|j_1-j_2|$ up to $j_1+j_2$ appearing exactly once.

**Proof.**
1. *(Weights add.)* Since $J_3^{\text{tot}}=J_3\otimes I + I\otimes J_3$, the product basis $|j_1,m_1\rangle\otimes|j_2,m_2\rangle$ is a $J_3^{\text{tot}}$-eigenbasis with eigenvalue $m=m_1+m_2$. Count how many product states have each total $m$: it is the number of pairs $(m_1,m_2)$ with $m_1+m_2=m$, which (for $j_1\ge j_2$) equals $j_1+j_2-|m|+1$ on the falling edge $j_1-j_2\le|m|\le j_1+j_2$. So the multiplicities of $m$ run $1,2,3,\dots$ up to $2j_2+1$, then plateau, decreasing symmetrically at the ends.
2. *(Subtract off ladders.)* An irreducible spin-$J$ block contributes exactly one state at each $m=-J,\dots,J$. The largest total $m$ available is $j_1+j_2$, appearing once, so there is exactly one spin-$(j_1+j_2)$ block. Removing its contribution lowers each multiplicity; the new top is $m=j_1+j_2-1$, again with one leftover state, giving one spin-$(j_1+j_2-1)$ block. Iterating peels off one block per integer step.
3. *(Where it stops.)* The process exhausts all states when the running top reaches $|j_1-j_2|$; below that the multiplicities have all been accounted for. A dimension check confirms completeness: $\sum_{J=|j_1-j_2|}^{j_1+j_2}(2J+1) = (2j_1+1)(2j_2+1) = \dim(V_{j_1}\otimes V_{j_2})$. $\blacksquare$

**Worked example — two spin-$\tfrac12$ particles.** Take $j_1=j_2=\tfrac12$. The formula gives $\tfrac12\otimes\tfrac12 = 1\oplus 0$: a spin-$1$ **triplet** (dimension $3$) and a spin-$0$ **singlet** (dimension $1$), total $3+1=4=2\times2$. Explicitly, the triplet is the symmetric combination
$$
|{\uparrow\uparrow}\rangle,\quad \tfrac{1}{\sqrt2}\big(|{\uparrow\downarrow}\rangle+|{\downarrow\uparrow}\rangle\big),\quad |{\downarrow\downarrow}\rangle,
$$
and the singlet is the antisymmetric $\tfrac1{\sqrt2}(|{\uparrow\downarrow}\rangle-|{\downarrow\uparrow}\rangle)$. The numerical coefficients ($\pm\tfrac1{\sqrt2}$, etc.) are the **Clebsch–Gordan coefficients**, computed by starting from the highest state $|{\uparrow\uparrow}\rangle=|1,1\rangle$ and applying the total lowering operator $J_-^{\text{tot}}=J_-\otimes I + I\otimes J_-$ from s11. This decomposition is exactly why two electrons can be in a spin-symmetric triplet or a spin-antisymmetric singlet — the foundation of the chemical bond and of the periodic table's structure.

> **Pitfall.** The total generators are *sums* $J_a\otimes I + I\otimes J_a$, not products; the multiplicative rule applies to the group elements ($\rho(g)\otimes\sigma(g)$) and to characters, but the algebra (infinitesimal) version is additive. Confusing the two is the classic error in addition of angular momentum.

---

*From four axioms we reached the conserved quantities of physics, the multiplets of particles, and the quark model. The throughline is a single idea seen at ever greater depth: a symmetry group acts, that action is a representation, representations decompose into irreducible atoms, and those atoms — labeled by $j$ for spin, by weights for $SU(3)$ — are exactly the families of states nature allows. Read once for the architecture; return to any boxed theorem or numbered proof when you need the machinery. Symmetry was the organizing principle all along.*
