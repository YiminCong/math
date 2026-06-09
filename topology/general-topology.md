**English** · [中文](general-topology.zh.md)

# Topology, *nearness without distance.*

A full first course in point-set topology — from open sets to compactness, connectedness, and the great metrization theorems. Built basics → expert. This edition is written for a reader who has *never* seen set theory or metric spaces: every symbol is defined in words the first time it appears, every theorem is proved as a numbered list where each step states both *what* is done and *why* it is allowed, and every idea is illustrated with a concrete worked example.

[← Back to all guides](../README.md)

## Part A · Foundations

<a id="s0"></a>
### The big picture: what topology is

*Topology is the study of those properties of space that survive continuous deformation — "rubber-sheet geometry." It is the language of nearness, stripped of distance, area, and angle.*

#### What this section is for

Before we define anything precisely, let us agree on the *shape* of the subject so that every later definition has a home. The single idea of topology is this: **we want to talk about which points are "near" which sets, without ever measuring how near.** Imagine a rubber sheet with shapes drawn on it. If you stretch and bend the sheet (but never tear it or glue parts together), distances change, angles change, areas change — yet some features stubbornly survive. A loop stays a loop. A connected blob stays connected. A figure-eight keeps its crossing point. Topology is the precise study of exactly those surviving features.

#### Terms defined from scratch

Because we assume no background, here are the words we will use immediately, each in plain language.

- A **set** is just a collection of objects, called its **elements** or **points**. We write $x\in X$ to mean "$x$ is an element of the set $X$" and read it "$x$ in $X$." We write $x\notin X$ for "$x$ is not an element of $X$."
- A **subset** of $X$ is a set all of whose elements are also in $X$; we write $A\subseteq X$. For example, the set of even numbers is a subset of the set of whole numbers.
- The **empty set**, written $\varnothing$, is the set with no elements at all. It is a subset of every set (vacuously: it has no element that could fail to belong to $X$).
- A **family** (or **collection**) of sets is simply a set whose elements are themselves sets. We use the word "family" only to keep our language clear when sets contain sets.

#### The one definition everything rests on

> **Principle — the central abstraction**
>
> A **topology** on a set $X$ is a choice of which subsets count as **open**. From that single choice flow all the topological concepts: a continuous function is one whose preimages of open sets are open; convergence, closure, and compactness are all defined through open sets. Geometry is replaced by a calculus of open sets.

You should not yet know what "open" precisely means — that is the content of §s3. For now, hold this mental picture: an **open set** is a region with no edge of its own, a region where every point has a little breathing room of nearby points still inside the region. The open interval of numbers strictly between $0$ and $1$ is open: any number inside it, say $0.999$, has slightly larger and slightly smaller numbers still inside. The *closed* interval including the endpoints $0$ and $1$ is not open, because the endpoint $1$ has no breathing room to its right.

#### The whole course on one line

> Metric spaces → Open sets & topologies → Continuity & constructions → Connectedness & compactness → Separation & metrization → Nets, completeness, Baire

Read that line as a story. We start (§s2) with **metric spaces**, where distance is available and "open" can be defined concretely. We then *forget the distance* and keep only the open sets (§s3), discovering that continuity (§s7) needs nothing more. We learn four machines for building new spaces from old (§s6, §s8, §s9). We isolate the two great "shape" properties, connectedness (§s10–§s11) and compactness (§s12–§s15). We grade spaces by how well open sets separate things (§s16–§s17), and ask when an abstract space secretly came from a distance after all (§s18–§s19). Finally we repair convergence in wild spaces and return to analysis (§s20–§s22).

> **Connection — why it matters**
>
> Topology is the foundation beneath real analysis, functional analysis, differential geometry, and algebraic topology. The same axioms describe $\mathbb R^n$, the space of continuous functions, the Zariski topology of algebraic geometry, and the profinite groups of number theory. Learn the abstraction once; reuse it everywhere.

##### Common pitfall

Do not expect "open" to mean "without boundary points drawn in heavy ink." It is a *relative* and *axiomatic* notion: a set is open because the chosen topology says so. The same subset can be open under one topology and not under another. We make this precise in §s3 and §s6.

<a id="s1"></a>
### Set-theory toolkit: functions, relations, cardinality, Zorn's lemma

*Topology is set theory with a chosen structure. We collect the language we will lean on constantly.*

#### Why we need this section

Every later definition is phrased in the language of sets, functions, and a couple of logical operations. If even one of these symbols is unfamiliar, the proofs will look like noise. So we spell out each tool, prove the facts we will actually reuse, and work a small numerical example for each.

#### Functions, and the all-important preimage

A **function** $f:X\to Y$ is a rule that assigns to each element $x$ of the set $X$ (the **domain**) exactly one element $f(x)$ of the set $Y$ (the **codomain**). The element $f(x)$ is the **image** of $x$.

We will constantly push whole *sets* through $f$ in two directions.

**Sets, images & preimages**

$$f^{-1}(B)=\{x\in X: f(x)\in B\},\qquad f(A)=\{f(x): x\in A\}$$

In words: the **image** $f(A)$ of a subset $A\subseteq X$ is the set of all outputs you get by feeding in elements of $A$. The **preimage** (or **inverse image**) $f^{-1}(B)$ of a subset $B\subseteq Y$ is the set of all inputs whose output lands in $B$. The notation $f^{-1}$ here does **not** require $f$ to be invertible; $f^{-1}(B)$ is defined for any $f$ and any $B$.

> Worked example. Let $f:\mathbb R\to\mathbb R$ be $f(x)=x^2$ (here $\mathbb R$ is the set of all real numbers — every decimal, positive, negative, or zero). Take $B=[0,4]$, the set of real numbers from $0$ to $4$ inclusive. Then $f^{-1}(B)=\{x:0\le x^2\le 4\}=[-2,2]$, because squaring a number between $-2$ and $2$ lands in $[0,4]$, and no other number does. Take $A=[1,3]$; then $f(A)=[1,9]$.

*Preimage respects all set operations:*

$$f^{-1}\Big(\bigcup_\alpha B_\alpha\Big)=\bigcup_\alpha f^{-1}(B_\alpha),\qquad f^{-1}\Big(\bigcap_\alpha B_\alpha\Big)=\bigcap_\alpha f^{-1}(B_\alpha),\qquad f^{-1}(B^c)=\big(f^{-1}(B)\big)^c.$$

Here $\bigcup_\alpha$ means "the union over all indices $\alpha$": the union of a family of sets is the set of points lying in **at least one** member. The intersection $\bigcap_\alpha$ is the set of points lying in **every** member. The **complement** $B^c$ of $B\subseteq Y$ is $\{y\in Y: y\notin B\}$, everything *not* in $B$.

**Demonstration — preimage commutes with complement**

We prove $f^{-1}(B^c)=\big(f^{-1}(B)\big)^c$; the union and intersection laws are similar and we prove the union law afterward.

1. Take any $x\in X$. By definition of preimage, $x\in f^{-1}(B^c)$ means $f(x)\in B^c$.
2. By definition of complement, $f(x)\in B^c$ means $f(x)\notin B$.
3. By definition of preimage again, $f(x)\notin B$ means $x\notin f^{-1}(B)$.
4. By definition of complement, $x\notin f^{-1}(B)$ means $x\in\big(f^{-1}(B)\big)^c$.
5. Steps 1–4 show $x\in f^{-1}(B^c)$ exactly when $x\in\big(f^{-1}(B)\big)^c$. Two sets with exactly the same elements are equal, so $f^{-1}(B^c)=\big(f^{-1}(B)\big)^c$.

**Demonstration — preimage commutes with union**

1. Suppose $x\in f^{-1}\big(\bigcup_\alpha B_\alpha\big)$. By definition this means $f(x)\in\bigcup_\alpha B_\alpha$, i.e. $f(x)\in B_{\alpha_0}$ for at least one index $\alpha_0$ (definition of union).
2. Then $x\in f^{-1}(B_{\alpha_0})$ (definition of preimage), so $x\in\bigcup_\alpha f^{-1}(B_\alpha)$ (definition of union). This proves the left side is contained in the right.
3. Conversely suppose $x\in\bigcup_\alpha f^{-1}(B_\alpha)$. Then $x\in f^{-1}(B_{\alpha_0})$ for some $\alpha_0$, so $f(x)\in B_{\alpha_0}\subseteq\bigcup_\alpha B_\alpha$, hence $x\in f^{-1}\big(\bigcup_\alpha B_\alpha\big)$. This proves the right side is contained in the left.
4. Each side contains the other, so they are equal.

*This perfect compatibility is exactly why topology is built on preimages, not images.* (Images are worse behaved: in the example above, $f(A\cap A')$ can be smaller than $f(A)\cap f(A')$.)

#### De Morgan's laws (the workhorse)

$$\Big(\bigcup_{\alpha} A_\alpha\Big)^c=\bigcap_\alpha A_\alpha^c,\qquad \Big(\bigcap_\alpha A_\alpha\Big)^c=\bigcup_\alpha A_\alpha^c$$

In words: the complement of a union is the intersection of the complements, and vice versa.

**Demonstration — the first De Morgan law**

1. Take $x$ in the ambient set. By definition of complement, $x\in\big(\bigcup_\alpha A_\alpha\big)^c$ means $x\notin\bigcup_\alpha A_\alpha$.
2. By definition of union, $x\notin\bigcup_\alpha A_\alpha$ means $x$ is in **no** $A_\alpha$; that is, for every index $\alpha$, $x\notin A_\alpha$.
3. By definition of complement, "for every $\alpha$, $x\notin A_\alpha$" means "for every $\alpha$, $x\in A_\alpha^c$."
4. By definition of intersection, that is exactly $x\in\bigcap_\alpha A_\alpha^c$.
5. Steps 1–4 give the same membership condition on both sides, so the sets are equal. The second law follows by applying the first to the sets $A_\alpha^c$ and using $(A^c)^c=A$.

> Worked example. Inside $\mathbb R$, let $A_1=(-\infty,0)$ and $A_2=(1,\infty)$. Then $A_1\cup A_2$ is everything except $[0,1]$, so $(A_1\cup A_2)^c=[0,1]$. On the other side, $A_1^c=[0,\infty)$ and $A_2^c=(-\infty,1]$, and their intersection is $[0,1]$. The two answers agree, as De Morgan promises.

*These convert statements about open sets (closed under arbitrary unions) into statements about closed sets (closed under arbitrary intersections) — we use this conversion in §s3 and §s12.*

#### Relations, equivalences, partitions

> **Concept — relations, equivalences, partitions**
>
> An **equivalence relation** $\sim$ on $X$ (reflexive, symmetric, transitive) partitions $X$ into disjoint **equivalence classes** $[x]=\{y: y\sim x\}$. The set of classes is the **quotient** $X/\!\sim$. This is the engine behind the quotient topology of §s9.

Unpacking the three properties: a **relation** $\sim$ is just a rule that, for each ordered pair $(x,y)$, declares whether "$x\sim y$" holds. It is **reflexive** if $x\sim x$ always; **symmetric** if $x\sim y$ forces $y\sim x$; **transitive** if $x\sim y$ and $y\sim z$ force $x\sim z$. A **partition** of $X$ is a way of cutting $X$ into nonempty, non-overlapping pieces whose union is all of $X$.

**Demonstration — equivalence classes partition $X$**

1. Every $x$ lies in its own class because $x\sim x$ (reflexivity), so the classes cover $X$.
2. Suppose two classes $[x]$ and $[y]$ share a point $z$, so $z\sim x$ and $z\sim y$. By symmetry $x\sim z$, and with $z\sim y$ transitivity gives $x\sim y$.
3. Then for any $w\in[x]$ we have $w\sim x\sim y$, so $w\in[y]$; thus $[x]\subseteq[y]$, and symmetrically $[y]\subseteq[x]$, so $[x]=[y]$.
4. Hence two classes are either identical or disjoint, and together with step 1 this is exactly a partition.

> Worked example. On the integers let $m\sim n$ mean "$m-n$ is even." This is reflexive ($m-m=0$ is even), symmetric, and transitive (sum of two even numbers is even). The two classes are the even integers and the odd integers — a partition of $\mathbb Z$ into "remainders mod $2$."

#### Cardinality

*A set is **countable** if it injects into $\mathbb N$ (finite or countably infinite).* Here $\mathbb N=\{0,1,2,\dots\}$ is the set of natural numbers, and a function is an **injection** (or is **injective**, or **one-to-one**) if different inputs always give different outputs: $f(a)=f(b)$ forces $a=b$. So "countable" means you can label the elements with natural numbers without repeats — you can list them in a (possibly endless) sequence.

*Key facts: a countable union of countable sets is countable; $\mathbb Q$ is countable; $\mathbb R$ is uncountable (Cantor's diagonal argument). Countability governs the second-countable, separable, and Lindelöf properties of §s16.*

**Demonstration — $\mathbb R$ is uncountable (Cantor's diagonal argument)**

1. It is enough to show the interval $(0,1)$ is uncountable, since $(0,1)\subseteq\mathbb R$. Suppose, for contradiction, that $(0,1)$ were countable, so we could list every number in it as $r_1,r_2,r_3,\dots$.
2. Write each $r_n$ as an infinite decimal $0.d_{n1}d_{n2}d_{n3}\dots$ (choosing the form not ending in all $9$s, so each number has one chosen representation).
3. Build a new decimal $s=0.s_1s_2s_3\dots$ by the diagonal rule: let $s_n=5$ if the digit $d_{nn}$ is not $5$, and $s_n=4$ if $d_{nn}=5$. Then $s_n\ne d_{nn}$ for every $n$, and $s$ uses only the digits $4$ and $5$, so it is a genuine number in $(0,1)$ not ending in $9$s.
4. For each $n$, $s$ differs from $r_n$ in the $n$-th decimal place, so $s\ne r_n$. Thus $s$ is in $(0,1)$ but not in the list — contradicting that the list contained *every* number of $(0,1)$.
5. The assumption "$(0,1)$ is countable" is impossible, so $\mathbb R$ is uncountable.

> Worked example of a countable set: $\mathbb Q$, the rationals (fractions $p/q$). List fractions by the size of $|p|+|q|$, breaking ties by some fixed order, skipping repeats; this is an explicit injection into $\mathbb N$, so $\mathbb Q$ is countable even though it is infinite and dense.

#### Partial orders & Zorn's lemma

$$\textbf{Zorn's lemma: } \text{if every chain in a poset has an upper bound, the poset has a maximal element.}$$

*A **partial order** $\leq$ is reflexive, antisymmetric, transitive. A **chain** is a totally ordered subset; an **upper bound** of a subset $S$ is an element $\geq$ everything in $S$; a **maximal element** has nothing strictly above it.*

Term by term: a **partial order** is a relation $\le$ that is reflexive ($a\le a$), **antisymmetric** ($a\le b$ and $b\le a$ force $a=b$), and transitive. A set with a partial order is a **poset** (partially ordered set). It is "partial" because two elements may be **incomparable** — neither $a\le b$ nor $b\le a$. A **chain** is a subset in which every two elements *are* comparable. A **maximal element** $m$ is one with no element strictly larger: there is no $x$ with $m\le x$ and $m\ne x$. (Maximal is weaker than "largest": a maximal element need not dominate everything, it just has nothing above it.)

> Worked example of a poset. Let the poset be all subsets of $\{1,2,3\}$ ordered by $\subseteq$. The chain $\varnothing\subseteq\{1\}\subseteq\{1,2\}\subseteq\{1,2,3\}$ has upper bound $\{1,2,3\}$. The unique maximal element is $\{1,2,3\}$. By contrast, the poset of *proper* subsets (everything except $\{1,2,3\}$) has three maximal elements $\{1,2\},\{1,3\},\{2,3\}$ and no largest element — illustrating why "maximal" is not "largest."

> **Principle — choice in disguise**
>
> Zorn's lemma is equivalent to the **Axiom of Choice** and to the **Well-Ordering Theorem**. In topology it is the hidden engine behind Tychonoff's theorem (§s14), the existence of maximal ideals, and the ultrafilter lemma for nets and filters (§s20).

The **Axiom of Choice** says: given any family of nonempty sets, there is a function picking one element from each. We use Zorn's lemma rather than proving it; it is taken as a foundational assumption.

<a id="s2"></a>
### Metric spaces: open balls, convergence, the prototype

*Metric spaces are the concrete ancestor of topology. Every intuition you have about openness, continuity, and limits comes from here.*

#### Why start here

The eventual definition of "topology" (§s3) will look strange and unmotivated unless you first see it in the setting where it was born: spaces with a notion of distance. So here we define distance abstractly, build open sets out of it, and prove the small fact (open balls are open) that the whole later theory imitates.

**Definition — metric space**

$$d:X\times X\to[0,\infty),\quad d(x,y)=0\iff x=y,\quad d(x,y)=d(y,x),\quad d(x,z)\leq d(x,y)+d(y,z).$$

Reading the symbols: $X\times X$ is the set of all ordered pairs $(x,y)$ with $x,y\in X$ (the **Cartesian product** of $X$ with itself). The notation $d:X\times X\to[0,\infty)$ means $d$ is a function taking each pair to a number in $[0,\infty)$, the non-negative real numbers. The symbol $\iff$ means "if and only if" — the two sides are equivalent. So a **metric** (or **distance function**) is a rule $d$ assigning a non-negative number $d(x,y)$ to each pair of points, such that:

- **(Identity of indiscernibles)** $d(x,y)=0$ exactly when $x=y$: distinct points are a positive distance apart, and a point is distance $0$ from itself.
- **(Symmetry)** $d(x,y)=d(y,x)$: distance does not care about direction.
- **(Triangle inequality)** $d(x,z)\le d(x,y)+d(y,z)$: a detour through $y$ is never shorter than the direct trip.

A set $X$ together with such a $d$ is a **metric space**.

*Example metrics on $\mathbb R^n$ (the set of $n$-tuples of real numbers):* Euclidean $d_2(x,y)=\sqrt{\sum_i (x_i-y_i)^2}$ (straight-line distance), taxicab $d_1(x,y)=\sum_i|x_i-y_i|$ (city-block distance), and the max metric $d_\infty(x,y)=\max_i|x_i-y_i|$. All three satisfy the three axioms.

> Worked example. On $\mathbb R^2$, take $x=(0,0)$ and $y=(3,4)$. Then $d_2(x,y)=\sqrt{3^2+4^2}=5$, while $d_1(x,y)=3+4=7$ and $d_\infty(x,y)=\max(3,4)=4$. The three distances differ, yet (as §s4 will show) they all generate the *same* open sets.

**Definition — open ball & open set**

$$B(x,r)=\{y\in X: d(x,y)\lt r\}$$

The **open ball** $B(x,r)$ of **center** $x$ and **radius** $r>0$ is the set of all points strictly closer to $x$ than $r$. ("Strictly" because we use $<$, not $\le$; the boundary shell is excluded.)

*A set $U\subseteq X$ is **open** if every point of it has some ball entirely inside $U$: for all $x\in U$ there is $r\gt 0$ with $B(x,r)\subseteq U$.* Intuitively, "open" means every point has breathing room.

> Worked example. In $\mathbb R$ with $d(x,y)=|x-y|$, the ball $B(0,1)$ is the open interval $(-1,1)$. The set $(0,1)$ is open: a point like $0.9$ has the ball $B(0.9,0.05)=(0.85,0.95)\subseteq(0,1)$. The set $[0,1]$ is not open, because the point $1$ admits no ball $B(1,r)=(1-r,1+r)$ that stays inside $[0,1]$ — every such ball pokes out past $1$.

**Demonstration — open balls are open**

We must show $B(x,r)$ satisfies the definition of "open": every one of its points has a smaller ball inside it.

1. Take any $y\in B(x,r)$, so by definition $d(x,y)\lt r$. Set $s=r-d(x,y)$; since $d(x,y)<r$, we have $s\gt 0$, so $s$ is a legitimate radius.
2. Take any $z\in B(y,s)$, meaning $d(y,z)\lt s$. The triangle inequality (third metric axiom) applied to the points $x,y,z$ gives

   $$d(x,z)\leq d(x,y)+d(y,z)\lt d(x,y)+s=d(x,y)+\big(r-d(x,y)\big)=r.$$
3. So $d(x,z)\lt r$, which by definition of the ball means $z\in B(x,r)$. Since $z$ was an arbitrary point of $B(y,s)$, we conclude $B(y,s)\subseteq B(x,r)$.
4. Thus every point $y$ of $B(x,r)$ has a ball $B(y,s)$ inside $B(x,r)$. By the definition of open, $B(x,r)$ is open.

*The triangle inequality is precisely what makes the open-set definition consistent — without it, step 2 fails and balls need not be open.*

**Definition — convergence & continuity (metric form)**

$$x_n\to x \iff \forall\varepsilon\gt 0\ \exists N\ \forall n\geq N:\ d(x_n,x)\lt\varepsilon$$

A **sequence** $(x_n)$ is an infinite list $x_1,x_2,x_3,\dots$ of points (a function from $\mathbb N$ to $X$). The symbols read: "for every $\varepsilon>0$ there exists an index $N$ such that for all $n\ge N$, the distance $d(x_n,x)$ is less than $\varepsilon$." Plainly: **$x_n\to x$** ("$x_n$ converges to $x$") means that however small a target tolerance $\varepsilon$ you name, eventually (from some index $N$ on) all the terms are within $\varepsilon$ of $x$.

$$f \text{ continuous at } x \iff \forall\varepsilon\gt 0\ \exists\delta\gt 0:\ d(x,y)\lt\delta\Rightarrow d'\big(f(x),f(y)\big)\lt\varepsilon$$

Here $f:X\to Y$ maps one metric space to another, with $d$ the distance in $X$ and $d'$ the distance in $Y$. The symbol $\Rightarrow$ means "implies." In words: $f$ is **continuous at $x$** if, for every output tolerance $\varepsilon$, there is an input tolerance $\delta$ so that staying within $\delta$ of $x$ guarantees the output stays within $\varepsilon$ of $f(x)$. Small input changes cause small output changes.

> Worked example. On $\mathbb R$, the sequence $x_n=1/n$ converges to $0$: given $\varepsilon>0$, choose $N$ larger than $1/\varepsilon$; then for $n\ge N$, $d(x_n,0)=1/n\le 1/N<\varepsilon$. And $f(x)=2x$ is continuous: given $\varepsilon$, take $\delta=\varepsilon/2$; then $|x-y|<\delta$ gives $|2x-2y|=2|x-y|<2\delta=\varepsilon$.

> **Connection — the leap to topology**
>
> Both definitions can be re-read using only open sets: $x_n\to x$ means every open set containing $x$ eventually contains all $x_n$; $f$ is continuous iff preimages of open sets are open. Topology keeps these reformulations and *discards the metric*. §s3 and §s7 make this precise.

##### Common pitfall

The same set $X$ can carry many different metrics. As the example above hinted, $d_1,d_2,d_\infty$ on $\mathbb R^n$ are different functions but give the *same* open sets, hence the same topology. So the metric is extra information; topology will keep only the part of it that survives as the open-set structure.

## Part B · Topological spaces

<a id="s3"></a>
### Topological spaces & open sets

*The central definition of the subject. Three axioms abstract everything we learned about open sets in metric spaces.*

#### The idea behind the axioms

In §s2 we *defined* open sets from a distance. Now we throw the distance away and simply *declare* a family of sets to be open, demanding only the three properties that metric open sets always had (we verified them implicitly there and verify them explicitly below). Anything satisfying these three properties deserves to be called a topology, whether or not a distance is anywhere in sight.

**Definition — topology**

A **topology** on a set $X$ is a family $\tau$ of subsets of $X$ (the **open sets**) satisfying:

$$\text{(T1)}\ \ \varnothing\in\tau,\ X\in\tau;$$

$$\text{(T2)}\ \ U_\alpha\in\tau\ \Rightarrow\ \bigcup_\alpha U_\alpha\in\tau\quad(\text{arbitrary unions});$$

$$\text{(T3)}\ \ U_1,\dots,U_n\in\tau\ \Rightarrow\ \bigcap_{i=1}^n U_i\in\tau\quad(\text{finite intersections}).$$

In words: (T1) the empty set and the whole space are open; (T2) a union of *any* number of open sets (even infinitely many) is open; (T3) an intersection of *finitely many* open sets is open. The Greek letter $\tau$ (tau) is the traditional name for the topology.

*The pair $(X,\tau)$ is a **topological space**. A set is **closed** if its complement is open.* Beware: "closed" is **not** the opposite of "open." A set can be both (e.g. $\varnothing$ and $X$ are both open and closed), neither, or just one.

**Demonstration — the metric open sets satisfy the three axioms**

Let $X$ be a metric space and let $\tau$ be the family of all metric-open sets from §s2. We check (T1)–(T3).

1. **(T1)** The empty set $\varnothing$ is open *vacuously*: the requirement "every point of $\varnothing$ has a ball inside" is satisfied because $\varnothing$ has no points to check. And $X$ is open because for any $x\in X$ and any radius $r$, the ball $B(x,r)$ consists of points of $X$, so $B(x,r)\subseteq X$.
2. **(T2)** Let each $U_\alpha$ be open and take $x\in\bigcup_\alpha U_\alpha$. By definition of union, $x\in U_{\alpha_0}$ for some particular $\alpha_0$. Since $U_{\alpha_0}$ is open, there is a ball $B(x,r)\subseteq U_{\alpha_0}$. But $U_{\alpha_0}\subseteq\bigcup_\alpha U_\alpha$, so $B(x,r)\subseteq\bigcup_\alpha U_\alpha$. Hence every point of the union has a ball inside it: the union is open.
3. **(T3)** Let $U_1,\dots,U_n$ be open and take $x\in\bigcap_{i=1}^n U_i$. For each $i$, openness gives a radius $r_i>0$ with $B(x,r_i)\subseteq U_i$. Let $r=\min(r_1,\dots,r_n)$. Because there are *finitely many* $r_i$, this minimum is itself a positive number (an infinite collection of positive numbers can have infimum $0$ — this is exactly where finiteness is needed). Then $B(x,r)\subseteq B(x,r_i)\subseteq U_i$ for every $i$, so $B(x,r)\subseteq\bigcap_i U_i$. The finite intersection is open.

*Infinite intersections fail:* the sets $(-\tfrac1n,\tfrac1n)$ are each open in $\mathbb R$, but

$$\bigcap_{n=1}^\infty\Big(-\tfrac1n,\tfrac1n\Big)=\{0\}$$

is **not** open — the point $0$ has no ball $(-r,r)$ contained in $\{0\}$. That is exactly why (T3) is restricted to finite intersections.

**A zoo of topologies on a set $X$**

- **Discrete topology:** *every* subset is open, $\tau=\mathcal P(X)$ (here $\mathcal P(X)$, the **power set**, is the family of all subsets of $X$). Maximally many open sets.
- **Indiscrete / trivial topology:** only $\varnothing$ and $X$ are open. Minimally many.
- **Cofinite topology:** the open sets are $\varnothing$ together with every set whose complement is finite.
- **Standard topology on $\mathbb R$:** the open sets are arbitrary unions of open intervals $(a,b)$.
- **Lower-limit topology $\mathbb R_\ell$:** generated by half-open intervals $[a,b)$.

**Demonstration — the cofinite topology is a topology**

1. **(T1)** $\varnothing$ is declared open. $X$ is open because its complement $\varnothing$ is finite (it has zero elements).
2. **(T2)** Let $\{U_\alpha\}$ be open, each $U_\alpha=\varnothing$ or with finite complement. If all are empty the union is empty (open). Otherwise some $U_{\alpha_0}$ has finite complement; by De Morgan (§s1), $\big(\bigcup_\alpha U_\alpha\big)^c=\bigcap_\alpha U_\alpha^c\subseteq U_{\alpha_0}^c$, a subset of a finite set, hence finite. So the union has finite complement: open.
3. **(T3)** For finitely many nonempty open $U_1,\dots,U_n$, De Morgan gives $\big(\bigcap_i U_i\big)^c=\bigcup_i U_i^c$, a finite union of finite sets, hence finite. So the finite intersection has finite complement: open. (If any $U_i=\varnothing$ the intersection is $\varnothing$, open.)

> **Concept — finer vs coarser**
>
> If $\tau_1\subseteq\tau_2$ we say $\tau_2$ is **finer** (more open sets, more "resolution") and $\tau_1$ is **coarser**. The discrete topology is the finest possible; the indiscrete the coarsest. A finer topology makes more functions *out of* the space continuous and fewer *into* it.

> **Connection — the cofinite topology as a teacher**
>
> On an infinite set the cofinite topology is the simplest example where points are closed but the space is not Hausdorff: any two nonempty open sets intersect. It recurs as a counterexample throughout Part C.

We can already prove that last claim. If $U,V$ are nonempty cofinite-open sets, then $U^c,V^c$ are finite, so $(U\cap V)^c=U^c\cup V^c$ (De Morgan) is finite; on an infinite $X$ a set with finite complement cannot be empty, so $U\cap V\ne\varnothing$. Two nonempty open sets always meet — the opposite of the "Hausdorff" condition of §s17.

<a id="s4"></a>
### Basis & subbasis for a topology

*Listing every open set is hopeless. A basis is a small "alphabet" of open sets from which all others are spelled by union.*

#### Motivation

The standard topology on $\mathbb R$ has uncountably many open sets — you cannot list them. But every one of them is a union of open intervals. So the intervals form a compact "alphabet" that *generates* the whole topology. A basis abstracts this.

**Definition — basis**

A **basis** is a family $\mathcal B$ of subsets of $X$ satisfying:

$$\text{(B1)}\ \ \bigcup_{B\in\mathcal B}B=X;\qquad \text{(B2)}\ \ x\in B_1\cap B_2\ \Rightarrow\ \exists B_3\in\mathcal B,\ x\in B_3\subseteq B_1\cap B_2.$$

In words: (B1) the basis sets cover $X$ (every point is in at least one); (B2) wherever two basis sets overlap, a third basis set fits inside the overlap around any given point.

*The **topology generated by $\mathcal B$** is: $U$ is open iff for every $x\in U$ there is $B\in\mathcal B$ with $x\in B\subseteq U$. Equivalently, open sets are exactly arbitrary unions of basis elements.*

**Demonstration — the generated collection is a topology**

Let $\tau$ be the family of sets $U$ such that every $x\in U$ has a basis element $B$ with $x\in B\subseteq U$.

1. **(T1)** $\varnothing\in\tau$ vacuously (no points to check). $X\in\tau$ because by (B1) every $x\in X$ lies in some $B\in\mathcal B$, and $B\subseteq X$.
2. **(T2)** Let each $U_\alpha\in\tau$ and take $x\in\bigcup_\alpha U_\alpha$. Then $x\in U_{\alpha_0}$ for some $\alpha_0$, and by definition of $\tau$ there is $B\in\mathcal B$ with $x\in B\subseteq U_{\alpha_0}\subseteq\bigcup_\alpha U_\alpha$. So the union is in $\tau$.
3. **(T3)** It suffices to handle two sets $U_1,U_2\in\tau$ (then induct). Take $x\in U_1\cap U_2$. Get $B_1\subseteq U_1$ and $B_2\subseteq U_2$ from $\tau$, each containing $x$. Then $x\in B_1\cap B_2$, so by (B2) there is $B_3\in\mathcal B$ with $x\in B_3\subseteq B_1\cap B_2\subseteq U_1\cap U_2$. Hence $U_1\cap U_2\in\tau$.

*(B2) is exactly the condition that makes finite intersections work — without it step 3 collapses.*

> Worked example. The open intervals $\mathcal B=\{(a,b):a<b\}$ form a basis for $\mathbb R$. (B1): every real $x$ lies in, say, $(x-1,x+1)$. (B2): the intersection of two open intervals is again an open interval (or empty), so it directly contains a basis interval around any of its points. The generated topology is the standard topology.

**Definition — subbasis**

*A **subbasis** $\mathcal S$ is any collection covering $X$.* The topology it generates is built in two steps: first form $\mathcal B$, the family of all **finite intersections** of members of $\mathcal S$ (including $X$ itself as the empty intersection); this $\mathcal B$ is a basis, and the topology is then the unions of members of $\mathcal B$. Subbases let us specify a topology by naming just a few "must be open" sets — the product topology of §s8 is defined this way.

> Worked example. On $\mathbb R$, the rays $\mathcal S=\{(a,\infty):a\in\mathbb R\}\cup\{(-\infty,b):b\in\mathbb R\}$ form a subbasis. A finite intersection $(a,\infty)\cap(-\infty,b)=(a,b)$ recovers the open intervals, so the generated topology is again standard.

> **Connection — open balls are a basis**
>
> In a metric space the open balls $\{B(x,r)\}$ form a basis (we proved (B2) implicitly when showing balls are open in §s2), and the topology they generate is exactly the metric topology of §s2. The rays $(a,\infty)$ and $(-\infty,b)$ form a subbasis for the standard topology on $\mathbb R$. Bases are how almost every concrete topology is presented.

<a id="s5"></a>
### Closure, interior, boundary & limit points

*Given any set, topology produces three canonical relatives: the largest open set inside it, the smallest closed set around it, and the rim between.*

**Definition — interior, closure, boundary**

$$\mathrm{int}A=\bigcup\{U\subseteq A: U\text{ open}\},\qquad \overline{A}=\bigcap\{C\supseteq A: C\text{ closed}\}$$

$$\partial A=\overline{A}\setminus\mathrm{int}A=\overline A\cap\overline{A^c}$$

In words: the **interior** $\mathrm{int}A$ is the union of all open sets contained in $A$ — it is open (a union of open sets, by T2) and it is the *largest* open set inside $A$. The **closure** $\overline A$ is the intersection of all closed sets containing $A$ — it is closed (an intersection of closed sets is closed, proved below) and the *smallest* closed set around $A$. The **boundary** $\partial A$ is what is left of the closure after removing the interior: the "rim." The symbol $A\setminus B$ (set difference) means $\{x\in A:x\notin B\}$.

*So always $\mathrm{int}A\subseteq A\subseteq\overline A$.*

**Demonstration — an arbitrary intersection of closed sets is closed (so $\overline A$ is closed)**

1. Let $\{C_\beta\}$ be closed, so each complement $C_\beta^c$ is open (definition of closed, §s3).
2. By De Morgan (§s1), $\big(\bigcap_\beta C_\beta\big)^c=\bigcup_\beta C_\beta^c$.
3. The right side is a union of open sets, hence open by (T2).
4. So $\bigcap_\beta C_\beta$ has open complement, i.e. it is closed. In particular $\overline A$, an intersection of closed sets, is closed.

**Definition — limit point & the closure characterization**

A point $x$ is a **limit point** of $A$ if every open set containing $x$ also contains a point of $A$ *other than $x$ itself*. The set of limit points is denoted $A'$.

$$\overline{A}=A\cup A'=\{x: \text{every open } U\ni x \text{ has } U\cap A\neq\varnothing\}.$$

*A point of $\overline A$ that is not a limit point is an **isolated point** of $A$. $A$ is **dense** if $\overline A=X$* — its closure fills the whole space.

**Demonstration — the membership form of closure: $x\in\overline A$ iff every open $U\ni x$ meets $A$**

1. ($\Rightarrow$) Suppose some open $U\ni x$ misses $A$, i.e. $U\cap A=\varnothing$, so $A\subseteq U^c$. Now $U^c$ is closed (complement of open) and contains $A$, so by definition of closure $\overline A\subseteq U^c$. Since $x\in U$, $x\notin U^c$, hence $x\notin\overline A$. Contrapositive: if $x\in\overline A$ then every open $U\ni x$ meets $A$.
2. ($\Leftarrow$) Suppose $x\notin\overline A$. Then $x$ is outside the closed set $\overline A$, so $x\in(\overline A)^c$, which is open and contains $x$ but misses $A$ (since $A\subseteq\overline A$). So there *is* an open set around $x$ missing $A$. Contrapositive: if every open $U\ni x$ meets $A$, then $x\in\overline A$.

> Worked example. In $\mathbb R$ with $A=(0,1)$: $\mathrm{int}A=(0,1)$ (already open), $\overline A=[0,1]$ (the endpoints are limit points: every interval around $0$ contains points of $(0,1)$), and $\partial A=\{0,1\}$. For $A=\mathbb Q$: $\mathrm{int}\mathbb Q=\varnothing$ (no interval is all-rational), $\overline{\mathbb Q}=\mathbb R$ (every interval contains a rational), so $\partial\mathbb Q=\mathbb R$.

**Demonstration — a set is open iff it equals its interior**

1. ($\Leftarrow$) Suppose $A=\mathrm{int}A$. By definition $\mathrm{int}A$ is a union of open sets, hence open (T2); so $A$ is open.
2. ($\Rightarrow$) Suppose $A$ is open. Then $A$ is itself one of the open sets $U\subseteq A$ appearing in the union defining $\mathrm{int}A$, so $A\subseteq\mathrm{int}A$.
3. The reverse $\mathrm{int}A\subseteq A$ always holds, since every $U$ in the union is a subset of $A$. Combining steps 2 and 3, $\mathrm{int}A=A$.

*Dually, $A$ is closed $\iff A=\overline A\iff A'\subseteq A$ (a set is closed exactly when it already contains all its limit points).*

**Demonstration — the Kuratowski closure axioms**

These four properties characterize closure (the first item below bundles two of them, $\overline{\varnothing}=\varnothing$ and $A\subseteq\overline A$); we prove them from our definition.

1. **Grounding and extensiveness:** $\overline{\varnothing}=\varnothing$ because $\varnothing$ is itself closed and contains $\varnothing$, so it is the smallest such set; and $A\subseteq\overline A$ directly from the definition (every $C$ in the intersection contains $A$).
2. **Idempotence:** $\overline{\overline A}=\overline A$. We proved $\overline A$ is closed; the closure of any closed set is itself, since that set is the smallest closed set containing itself.
3. **Finite additivity:** $\overline{A\cup B}=\overline A\cup\overline B$.
   - ($\supseteq$) $\overline A\cup\overline B$ is a union of two closed sets. A finite union of closed sets is closed: its complement $\overline A^c\cap\overline B^c$ is a finite intersection of open sets, open by (T3). And $\overline A\cup\overline B\supseteq A\cup B$. Being a closed set containing $A\cup B$, it contains the *smallest* such, $\overline{A\cup B}$; hence $\overline{A\cup B}\subseteq\overline A\cup\overline B$.
   - ($\subseteq$) Closure is **monotone**: if $S\subseteq T$ then $\overline S\subseteq\overline T$, because every closed set containing $T$ contains $S$, so the intersection defining $\overline T$ is over a subfamily of that defining... more directly, $\overline T$ is a closed set containing $S$, hence $\overline S\subseteq\overline T$. Applying monotonicity to $A\subseteq A\cup B$ and $B\subseteq A\cup B$ gives $\overline A\subseteq\overline{A\cup B}$ and $\overline B\subseteq\overline{A\cup B}$, so $\overline A\cup\overline B\subseteq\overline{A\cup B}$.
   - Both inclusions give equality.

*These four properties can **replace** the open-set axioms: a closure operator defines a topology (the closed sets are the fixed sets $A=\overline A$). A beautiful instance of equivalent foundations.*

> **Connection — $\mathbb Q$ is dense in $\mathbb R$**
>
> Every interval contains a rational, so $\overline{\mathbb Q}=\mathbb R$. Density is the topological skeleton of approximation in analysis, and a countable dense set is exactly separability (§s16).

<a id="s6"></a>
### The subspace topology

*Any subset of a space becomes a space in its own right by intersecting open sets with it. This is the first of our four constructions.*

**Definition — subspace (relative) topology**

Given $(X,\tau)$ and a subset $A\subseteq X$, the **subspace topology** on $A$ is

$$\tau_A=\{U\cap A: U\in\tau\}$$

i.e. its open sets are exactly the **traces** of $X$-open sets on $A$.

**Demonstration — $\tau_A$ is a topology on $A$**

1. **(T1)** $\varnothing=\varnothing\cap A$ and $A=X\cap A$, and $\varnothing,X\in\tau$, so both are in $\tau_A$.
2. **(T2)** A union of traces is the trace of the union: $\bigcup_\alpha(U_\alpha\cap A)=\big(\bigcup_\alpha U_\alpha\big)\cap A$, because intersection distributes over union. Since $\bigcup_\alpha U_\alpha\in\tau$ (T2 in $X$), this is in $\tau_A$.
3. **(T3)** A finite intersection of traces is the trace of the intersection: $\bigcap_{i=1}^n(U_i\cap A)=\big(\bigcap_{i=1}^n U_i\big)\cap A$, again by distributivity. Since $\bigcap_i U_i\in\tau$ (T3 in $X$), this is in $\tau_A$.

> **Concept — "open in $A$" is relative**
>
> A set can be open in $A$ without being open in $X$. Example: $[0,\tfrac12)$ is open in $A=[0,1]$ (it equals $(-\tfrac12,\tfrac12)\cap A$) but not open in $\mathbb R$. Openness and closedness are always *relative to a chosen ambient space*.

Let us verify that example carefully. In $\mathbb R$, the set $U=(-\tfrac12,\tfrac12)$ is open. Its trace on $A=[0,1]$ is $U\cap A=[0,\tfrac12)$ (the negative part is chopped off by $A$). So $[0,\tfrac12)$ is open in the subspace $A$. But in $\mathbb R$ it is not open, because the point $0$ has no open interval $(-r,r)$ contained in $[0,\tfrac12)$.

**Demonstration — closed-in-subspace are traces of closed sets**

1. $F$ is closed in $A$ iff its complement $A\setminus F$ is open in $A$, i.e. $A\setminus F=U\cap A$ for some open $U$ of $X$ (definition of $\tau_A$).
2. Taking complements inside $A$: $F=A\setminus(U\cap A)=A\cap U^c$. Since $U$ is open in $X$, $U^c$ is closed in $X$. So $F$ is the trace of a closed set.
3. Conversely, for any closed $C\subseteq X$, its trace $A\cap C$ has complement (in $A$) equal to $A\cap C^c=A\cap(\text{open})$, a trace of an open set, hence open in $A$. So $A\cap C$ is closed in $A$.

*So "closed in the subspace" = "trace of a closed set," perfectly dual to the open case.*

> **Connection — heredity**
>
> Some properties pass to every subspace ("hereditary": Hausdorff, second countable, metrizable); others only to closed or open subspaces (compactness passes to closed subspaces; local compactness to open ones). Track this carefully — it returns in §s12, §s15, and §s17.

<a id="s7"></a>
### Continuous functions & homeomorphisms

*Continuity is the morphism of topology. Remarkably, it is captured entirely by preimages of open sets — no $\varepsilon$, no $\delta$.*

**Definition — continuous map**

A map $f:X\to Y$ between topological spaces is **continuous** if $f^{-1}(V)$ is open in $X$ for every open $V\subseteq Y$. (Recall from §s1 that $f^{-1}(V)=\{x:f(x)\in V\}$.) *It suffices to check this on a basis (or subbasis) of $Y$*, because preimage commutes with unions and finite intersections (§s1), so if it holds on the alphabet it holds on every spelled-out open set.

**Demonstration — it suffices to check continuity on a basis**

1. Suppose $f^{-1}(B)$ is open for every basis element $B$ of $Y$. Let $V\subseteq Y$ be any open set.
2. Write $V=\bigcup_\alpha B_\alpha$ as a union of basis elements (§s4).
3. Then $f^{-1}(V)=f^{-1}\big(\bigcup_\alpha B_\alpha\big)=\bigcup_\alpha f^{-1}(B_\alpha)$, using the preimage–union law (§s1).
4. This is a union of open sets, hence open by (T2). So $f$ is continuous.

**Demonstration — metric continuity $\iff$ preimages of open sets are open**

1. ($\Rightarrow$) Assume the $\varepsilon$-$\delta$ condition of §s2 holds at every point. Let $V$ be open in $Y$ and take $x\in f^{-1}(V)$, so $f(x)\in V$. Since $V$ is open, some ball $B(f(x),\varepsilon)\subseteq V$. By continuity at $x$ there is $\delta>0$ with $d(x,y)<\delta\Rightarrow d'(f(x),f(y))<\varepsilon$, i.e. $f\big(B(x,\delta)\big)\subseteq B(f(x),\varepsilon)\subseteq V$, so $B(x,\delta)\subseteq f^{-1}(V)$. Hence every point of $f^{-1}(V)$ has a ball inside it: $f^{-1}(V)$ is open.
2. ($\Leftarrow$) Assume preimages of open sets are open. Fix any $x$ and any $\varepsilon>0$. The ball $V=B(f(x),\varepsilon)$ is open (§s2), so $f^{-1}(V)$ is open and contains $x$. By openness pick $\delta>0$ with $B(x,\delta)\subseteq f^{-1}(V)$.
3. Then $d(x,y)<\delta$ gives $y\in B(x,\delta)\subseteq f^{-1}(V)$, so $f(y)\in V=B(f(x),\varepsilon)$, i.e. $d'(f(x),f(y))<\varepsilon$. That is precisely continuity at $x$ in the $\varepsilon$-$\delta$ sense.

*The topological definition recovers — and generalizes — the analyst's. Preimage, not image, because preimage commutes with unions, intersections, and complements (§s1).*

> Worked example. Let $f:\mathbb R\to\mathbb R$, $f(x)=x^2$, with the standard topology. Take an open interval $(a,b)$. If $a\ge 0$, $f^{-1}((a,b))=(-\sqrt b,-\sqrt a)\cup(\sqrt a,\sqrt b)$, a union of two open intervals, hence open. If $a<0<b$, $f^{-1}((a,b))=(-\sqrt b,\sqrt b)$, open. If $b\le 0$, the preimage is $\varnothing$, open. So $f^{-1}$ of every basis interval is open, and by the basis criterion $f$ is continuous.

**Equivalent characterizations of continuity**

*For $f:X\to Y$ the following are equivalent: (i) preimages of open sets are open; (ii) preimages of closed sets are closed; (iii) $f(\overline A)\subseteq\overline{f(A)}$ for all $A$; (iv) for each $x$ and each open $V\ni f(x)$, some open $U\ni x$ has $f(U)\subseteq V$.*

**Demonstration — (i) $\iff$ (ii)**

1. Assume (i). Let $C\subseteq Y$ be closed, so $C^c$ is open, so $f^{-1}(C^c)$ is open by (i). But $f^{-1}(C^c)=\big(f^{-1}(C)\big)^c$ (preimage–complement law, §s1). So $\big(f^{-1}(C)\big)^c$ is open, meaning $f^{-1}(C)$ is closed. That is (ii).
2. Assume (ii). Let $V\subseteq Y$ be open, so $V^c$ is closed, so $f^{-1}(V^c)=\big(f^{-1}(V)\big)^c$ is closed, meaning $f^{-1}(V)$ is open. That is (i).

**Definition — homeomorphism**

A **homeomorphism** is a continuous bijection $f$ whose inverse $f^{-1}$ is *also* continuous. (A **bijection** is a function that is both injective — distinct inputs give distinct outputs — and **surjective** — every element of the codomain is hit; such an $f$ has a genuine inverse function $f^{-1}$.) Spaces related by a homeomorphism are **homeomorphic** — "topologically the same."

*A continuous bijection need not be a homeomorphism.* Example: $f:[0,1)\to S^1$, $f(t)=e^{2\pi i t}$ (wrapping the half-open interval around the circle $S^1$). It is a continuous bijection, but its inverse is discontinuous at the point $1\in S^1$ where the two ends almost meet.

> **Concept — topological invariants**
>
> A property preserved by homeomorphism is a **topological invariant**: connectedness, compactness, Hausdorffness, the countability axioms. To prove two spaces are *not* homeomorphic, exhibit an invariant they differ on. ($\mathbb R$ and $\mathbb R^2$ differ because removing a point disconnects only the former — see §s10.)

> **Connection — composition & the gluing lemma**
>
> Compositions of continuous maps are continuous: if $g\circ f$ then $(g\circ f)^{-1}(W)=f^{-1}(g^{-1}(W))$, a preimage of a preimage, open by applying continuity twice. The **pasting lemma**: if $X=A\cup B$ with $A,B$ both closed (or both open) and $f$ is continuous on each and they agree on $A\cap B$, then $f$ is continuous on $X$. This is how piecewise-defined maps stay continuous.

<a id="s8"></a>
### The product topology

*How to topologize a product of spaces. The "obvious" choice is wrong for infinite products; the right one is engineered to make projections continuous.*

**Definition — product topology**

Given spaces $X_\alpha$ indexed by $\alpha$, their **product** $\prod_\alpha X_\alpha$ is the set of all "tuples" choosing one point $x_\alpha\in X_\alpha$ from each factor. The **projection** $\pi_\beta$ sends a tuple to its $\beta$-th coordinate, $\pi_\beta\big((x_\alpha)_\alpha\big)=x_\beta$.

The **product topology** on $\prod_\alpha X_\alpha$ is generated by the subbasis of "cylinders" $\pi_\beta^{-1}(U_\beta)$, where $U_\beta\subseteq X_\beta$ is open. *Equivalently a basic open set is $\prod_\alpha U_\alpha$ with each $U_\alpha$ open and $U_\alpha=X_\alpha$ for all but **finitely many** $\alpha$* (because a basis element is a finite intersection of subbasic cylinders, and each cylinder constrains only one coordinate).

> **Concept — why "finitely many" restrictions**
>
> The product topology is the **coarsest** topology making every projection $\pi_\alpha$ continuous. The finer "box topology" (allow all $U_\alpha$ to vary freely) destroys good theorems: with it, the diagonal map can fail to be continuous and Tychonoff's theorem (§s14) fails. We almost always mean the product topology.

**Universal property**

*A map $f:Z\to\prod_\alpha X_\alpha$ is continuous **iff** each component $\pi_\alpha\circ f:Z\to X_\alpha$ is continuous.* This characterizes the product topology completely and is its reason for existence.

**Demonstration — the universal property**

1. ($\Rightarrow$) If $f$ is continuous, then each $\pi_\alpha\circ f$ is a composition of continuous maps ($\pi_\alpha$ is continuous, shown next), hence continuous.
2. ($\Leftarrow$) Suppose every $\pi_\alpha\circ f$ is continuous. It suffices (basis criterion, §s7) to check $f^{-1}$ of each subbasic cylinder $\pi_\beta^{-1}(U_\beta)$ is open. Compute $f^{-1}\big(\pi_\beta^{-1}(U_\beta)\big)=(\pi_\beta\circ f)^{-1}(U_\beta)$, which is open because $\pi_\beta\circ f$ is continuous and $U_\beta$ is open. So $f$ is continuous.

**Demonstration — projections are continuous and open**

1. **Continuous:** for open $U\subseteq X_\beta$, the preimage $\pi_\beta^{-1}(U)$ is by definition a subbasic open set of the product, hence open. So $\pi_\beta$ is continuous.
2. **Open:** take a basic open box $\prod_\alpha U_\alpha$ (nonempty). Its image under $\pi_\beta$ is $U_\beta$ (the $\beta$-coordinate ranges over exactly $U_\beta$ as the tuple ranges over the box), which is open. So $\pi_\beta$ sends basic open sets to open sets.
3. A general open set is a union of basic boxes, and the image of a union is the union of the images: $\pi_\beta\big(\bigcup_\gamma\text{box}_\gamma\big)=\bigcup_\gamma\pi_\beta(\text{box}_\gamma)$, a union of open sets, open. So $\pi_\beta$ is an open map.

*Projections are continuous, surjective, and open — but generally not closed.* (The image of a closed set can fail to be closed: e.g. the hyperbola $\{xy=1\}$ is closed in $\mathbb R^2$ but its projection to the $x$-axis is $(-\infty,0)\cup(0,\infty)$ omitting $0$ — yet $0$ is a limit, so the projection is not closed.)

> **Connection — the Euclidean plane**
>
> The product topology on $\mathbb R\times\mathbb R$ is exactly the standard topology on $\mathbb R^2$: open rectangles form a basis, equivalent to open disks. Products are how all the higher-dimensional and function spaces are built. Tychonoff (§s14) is the deep theorem about infinite products.

<a id="s9"></a>
### The quotient topology

*Gluing points together. This construction builds circles from intervals, tori from squares, and the projective plane from a disk.*

**Definition — quotient topology**

Let $q:X\to Y$ be a **surjection** (every point of $Y$ is hit). The **quotient topology** on $Y$ declares $V\subseteq Y$ open iff $q^{-1}(V)$ is open in $X$. *It is the **finest** topology making $q$ continuous.* When $Y=X/\!\sim$ for an equivalence relation (§s1) and $q$ sends each point to its class, this glues equivalent points into one.

**Demonstration — the quotient topology is a topology**

1. **(T1)** $q^{-1}(\varnothing)=\varnothing$ and $q^{-1}(Y)=X$, both open in $X$, so $\varnothing,Y$ are open in $Y$.
2. **(T2)** If each $q^{-1}(V_\alpha)$ is open, then $q^{-1}\big(\bigcup_\alpha V_\alpha\big)=\bigcup_\alpha q^{-1}(V_\alpha)$ (preimage–union, §s1) is open. So $\bigcup_\alpha V_\alpha$ is open in $Y$.
3. **(T3)** Likewise $q^{-1}\big(\bigcap_{i=1}^n V_i\big)=\bigcap_{i=1}^n q^{-1}(V_i)$ is a finite intersection of open sets, open. So $\bigcap_i V_i$ is open in $Y$.

**Universal property**

*A map $g:Y\to Z$ out of a quotient is continuous **iff** $g\circ q:X\to Z$ is continuous.* So to define a continuous map on $X/\!\sim$ it suffices to define a continuous map on $X$ that is constant on each equivalence class.

**Demonstration — the universal property**

1. ($\Rightarrow$) If $g$ is continuous then $g\circ q$ is a composition of continuous maps, hence continuous.
2. ($\Leftarrow$) Suppose $g\circ q$ is continuous. Let $W\subseteq Z$ be open. Then $(g\circ q)^{-1}(W)=q^{-1}\big(g^{-1}(W)\big)$ is open in $X$. By the *definition* of the quotient topology, that says exactly that $g^{-1}(W)$ is open in $Y$. So $g$ is continuous.

**Demonstration — gluing $[0,1]$ endpoints gives the circle**

1. On $[0,1]$ define $\sim$ by $0\sim 1$ (and every other point only equivalent to itself). Define $f:[0,1]\to S^1$ by $f(t)=e^{2\pi i t}=(\cos 2\pi t,\sin 2\pi t)$. It is continuous, and $f(0)=f(1)=(1,0)$, so $f$ is constant on each class.
2. By the universal property, $f$ factors through the quotient: there is a continuous map $\bar f:[0,1]/\!\sim\,\to S^1$ with $\bar f\circ q=f$. It is a bijection: $f$ is onto $S^1$, and $f(s)=f(t)$ with $s\ne t$ only when $\{s,t\}=\{0,1\}$, which are identified in the quotient, so $\bar f$ is injective.
3. $[0,1]/\!\sim$ is compact, being the continuous image $q([0,1])$ of the compact set $[0,1]$ (§s12, §s13), and $S^1$ is Hausdorff (a metric space, §s17). A continuous bijection from a compact space to a Hausdorff space is a homeomorphism (§s12). Therefore $[0,1]/(0\sim 1)\cong S^1$.

*Gluing opposite sides of a square similarly yields the torus.*

> **Connection — duality of the four constructions**
>
> Subspace and product are **initial** constructions (coarsest topology making maps *in* continuous); quotient and disjoint-union are **final** (finest making maps *out* continuous). This duality is the categorical heart of point-set topology and the gateway to algebraic topology, where quotients build the fundamental spaces.

## Part C · Properties of spaces

<a id="s10"></a>
### Connectedness

*A space is connected if it cannot be split into two separate open pieces — the topological notion of being "all one piece."*

**Definition — connected space**

$X$ is **disconnected** if it can be written $X=U\cup V$ with $U,V$ open, both nonempty, and disjoint ($U\cap V=\varnothing$); such a pair is a **separation**. $X$ is **connected** if no separation exists. *Equivalently, the only sets that are both open and closed ("clopen") are $\varnothing$ and $X$* — because if $U$ were clopen and nontrivial, then $U$ and $V=U^c$ would form a separation.

The symbol $\sqcup$ below denotes a union that is *disjoint*.

**Demonstration — $[0,1]$ (indeed any real interval) is connected**

1. Suppose, for contradiction, $[0,1]=A\sqcup B$ is a separation, with both $A,B$ open in $[0,1]$, disjoint, nonempty. Say $0\in A$. Let $c=\sup\{x\in[0,1]:[0,x]\subseteq A\}$, the supremum (least upper bound) of all $x$ such that the whole initial segment up to $x$ lies in $A$. This set is nonempty (contains $0$) and bounded by $1$, so $c$ exists by the least-upper-bound property of $\mathbb R$.
2. $A$ is also *closed* in $[0,1]$ (its complement $B$ is open). The point $c$ is a limit of points of $A$ (points just below $c$ that are in initial segments inside $A$), so $c\in\overline A=A$ (closure, §s5). Thus $c\in A$.
3. Since $A$ is open in $[0,1]$ and $c\in A$, there is some $\delta>0$ with $[0,1]\cap(c-\delta,c+\delta)\subseteq A$. If $c<1$, then $[0,c+\tfrac\delta2]\subseteq A$, making $c+\tfrac\delta2$ a larger element of the set in step 1 — contradicting that $c$ is its supremum. So $c=1$.
4. Then $1=c\in A$, and $[0,1]\subseteq A$, forcing $B=\varnothing$ — contradicting that $B$ is nonempty. Hence no separation exists and $[0,1]$ is connected.

*The least-upper-bound property of $\mathbb R$ is exactly what powers connectedness of intervals.*

**Demonstration — continuous images of connected spaces are connected**

1. Let $f:X\to Y$ be continuous and surjective with $X$ connected. Suppose, for contradiction, $Y=U\sqcup V$ is a separation.
2. By continuity (§s7), $f^{-1}(U)$ and $f^{-1}(V)$ are open in $X$. They are disjoint because $U,V$ are, and they cover $X$ because $U,V$ cover $Y$ (preimage laws, §s1). They are nonempty because $f$ is surjective so hits both $U$ and $V$.
3. Thus $X=f^{-1}(U)\sqcup f^{-1}(V)$ is a separation of $X$ — contradicting that $X$ is connected. So $Y$ has no separation; $Y$ is connected.

*Corollary — the **Intermediate Value Theorem**.* A continuous $f:[a,b]\to\mathbb R$ has image $f([a,b])$ which is connected (continuous image of the connected $[a,b]$). The connected subsets of $\mathbb R$ are exactly the intervals (a set missing a middle value $c$ splits at $c$ into a separation), so the image is an interval, hence contains every value between $f(a)$ and $f(b)$.

> Worked example. Why $\mathbb R\not\cong\mathbb R^2$. If a homeomorphism $h:\mathbb R\to\mathbb R^2$ existed, it would restrict to a homeomorphism $\mathbb R\setminus\{0\}\to\mathbb R^2\setminus\{h(0)\}$. But $\mathbb R\setminus\{0\}=(-\infty,0)\sqcup(0,\infty)$ is disconnected, while $\mathbb R^2$ minus a point is connected (any two points can be joined avoiding the hole). Connectedness is a topological invariant (§s7), so no such $h$ exists.

> **Connection — building bigger connected sets**
>
> If $\{A_\alpha\}$ are connected with a common point, their union is connected. The closure of a connected set is connected. Products of connected spaces are connected. These let us assemble $\mathbb R^n$ and spheres as connected from intervals.

<a id="s11"></a>
### Path-connectedness & components

*A stronger, more geometric cousin of connectedness: you can walk from any point to any other along a continuous path.*

**Definition — path-connected**

A **path** from $a$ to $b$ in $X$ is a continuous map $\gamma:[0,1]\to X$ with $\gamma(0)=a$ and $\gamma(1)=b$. ($\gamma$ is the route; the parameter $t\in[0,1]$ is "time," $\gamma(0)$ the start, $\gamma(1)$ the finish.) $X$ is **path-connected** if any two of its points are joined by some path.

**Theorem — path-connected $\Rightarrow$ connected**

**Demonstration**

1. Suppose $X$ is path-connected but, for contradiction, disconnected: $X=U\sqcup V$ a separation. Pick $a\in U$, $b\in V$, and a path $\gamma:[0,1]\to X$ from $a$ to $b$.
2. The image $\gamma([0,1])$ is connected (continuous image of the connected $[0,1]$, §s10).
3. But $U\cap\gamma([0,1])$ and $V\cap\gamma([0,1])$ are open in the image, disjoint, cover it, and are nonempty ($a$ in the first, $b$ in the second). That is a separation of a connected set — impossible. So $X$ is connected.

*The converse fails*, as the next example shows.

**Demonstration — the topologist's sine curve: connected but not path-connected**

1. Let $S=\{(x,\sin\tfrac1x):0\lt x\leq 1\}$ (the wildly oscillating curve as $x\to 0$) and $T=\{0\}\times[-1,1]$ (a vertical segment on the $y$-axis). One computes the closure $\overline S=S\cup T$, because as $x\to 0^+$ the values $\sin\tfrac1x$ sweep through all of $[-1,1]$ infinitely often, so every point of $T$ is a limit point of $S$ (§s5).
2. $S$ is connected, being the continuous image of the connected interval $(0,1]$ under $x\mapsto(x,\sin\tfrac1x)$ (§s10). The closure of a connected set is connected (stated in §s10), so $\overline S=S\cup T$ is connected.
3. Yet there is no path from a point of $T$ to a point of $S$ inside $\overline S$. Suppose $\gamma:[0,1]\to\overline S$ were such a path with $\gamma(0)\in T$. Near $t=0$ the path would have to stay near $T$ by continuity, but to reach $S$ it must have $x$-coordinate becoming positive, forcing the $y$-coordinate $\sin\tfrac1x$ to oscillate between $-1$ and $1$ without settling — so $\gamma$ cannot be continuous at the instant it leaves $T$. Hence no path exists, and $\overline S$ is not path-connected.

*Connectedness and path-connectedness genuinely differ. They **agree** for open subsets of $\mathbb R^n$ and for locally path-connected spaces.*

> **Concept — components**
>
> The **connected components** are the maximal connected subsets; they partition $X$ and are always closed. **Path components** partition $X$ by the "joined by a path" equivalence relation. Each path component lies inside a single component. A space is **totally disconnected** (e.g. $\mathbb Q$, the Cantor set) if every component is a single point.

To see $\mathbb Q$ is totally disconnected: given two rationals $p<q$, pick an irrational $r$ between them; then $(-\infty,r)\cap\mathbb Q$ and $(r,\infty)\cap\mathbb Q$ separate any subset containing both $p$ and $q$. So no connected subset has more than one point.

> **Connection — to algebraic topology**
>
> Path components are $\pi_0(X)$, the zeroth homotopy set. Refining "is there a path?" to "are two paths deformable into each other?" gives the fundamental group $\pi_1$. Point-set connectedness is the entryway to homotopy theory.

<a id="s12"></a>
### Compactness

*The single most important property in topology — a finiteness condition that makes continuous functions tame and limits behave.*

**Definition — compact space**

An **open cover** of $X$ is a family $\{U_\alpha\}$ of open sets whose union is all of $X$ (every point lies in at least one $U_\alpha$). A **subcover** is a subfamily that still covers. $X$ is **compact** if *every* open cover has a *finite* subcover. (For a subset $K\subseteq X$, "compact" means compact in the subspace topology, equivalently: any family of $X$-open sets covering $K$ has a finite subfamily still covering $K$.)

The slogan: compactness lets you replace "infinitely many open sets cover me" with "finitely many already do."

**Demonstration — continuous images of compact spaces are compact**

1. Let $f:X\to Y$ be continuous, $X$ compact, and let $\{V_\alpha\}$ be an open cover of $f(X)$.
2. By continuity each $f^{-1}(V_\alpha)$ is open (§s7), and these cover $X$: any $x\in X$ has $f(x)\in V_\alpha$ for some $\alpha$, so $x\in f^{-1}(V_\alpha)$.
3. Compactness of $X$ yields a finite subcover $f^{-1}(V_{\alpha_1}),\dots,f^{-1}(V_{\alpha_n})$ of $X$.
4. Then $V_{\alpha_1},\dots,V_{\alpha_n}$ cover $f(X)$: for $y=f(x)\in f(X)$, $x$ lies in some $f^{-1}(V_{\alpha_i})$, so $y\in V_{\alpha_i}$. A finite subcover exists, so $f(X)$ is compact.

*Corollary — the **Extreme Value Theorem**.* A continuous $f:X\to\mathbb R$ on a compact $X$ has compact image $f(X)$, which (by Heine–Borel, §s13) is closed and bounded, hence contains its supremum and infimum. So $f$ attains a maximum and a minimum.

**Demonstration — in a Hausdorff space, compact $\Rightarrow$ closed**

(A space is **Hausdorff** if any two distinct points can be enclosed in disjoint open sets — formal definition in §s17; we use just that property.)

1. Let $K\subseteq X$ be compact, $X$ Hausdorff, and fix any $x\notin K$. For each $y\in K$, since $x\ne y$, Hausdorffness gives disjoint open sets $U_y\ni x$ and $V_y\ni y$.
2. The family $\{V_y:y\in K\}$ is an open cover of $K$; compactness gives a finite subcover $V_{y_1},\dots,V_{y_n}$. Let $U=\bigcap_{i=1}^n U_{y_i}$, a finite intersection of open sets, hence open (T3), and containing $x$.
3. $U$ is disjoint from each $V_{y_i}$ (since $U\subseteq U_{y_i}$ and $U_{y_i}\cap V_{y_i}=\varnothing$), hence disjoint from their union $\supseteq K$. So $U\cap K=\varnothing$: $U$ is a neighborhood of $x$ missing $K$.
4. Every $x\notin K$ thus has an open neighborhood inside $K^c$, so $K^c$ is open and $K$ is closed.

*Hausdorffness is essential:* in the cofinite topology on an infinite set (§s3) every subset is compact (any open cover has one member with finite complement, and finitely many more sets mop up that finite remainder), but not every subset is closed.

**Demonstration — the finite intersection property (FIP) characterization**

A family of sets has the **FIP** if every *finite* subfamily has nonempty intersection. Claim: $X$ is compact iff every family of *closed* sets with the FIP has nonempty total intersection.

1. Start from a family of closed sets $\{C_\alpha\}$ and pass to complements $\{C_\alpha^c\}$, which are open.
2. By De Morgan (§s1): $\bigcap_\alpha C_\alpha=\varnothing$ exactly when $\bigcup_\alpha C_\alpha^c=X$, i.e. the open sets $C_\alpha^c$ cover $X$.
3. Likewise a *finite* subfamily $C_{\alpha_1}\cap\dots\cap C_{\alpha_n}=\varnothing$ exactly when $C_{\alpha_1}^c\cup\dots\cup C_{\alpha_n}^c=X$, i.e. those finitely many open sets cover $X$.
4. So "the closed family has the FIP (no finite subfamily has empty intersection)" translates to "no finite subfamily of the open cover covers $X$," and "the total intersection is empty" translates to "the open family covers $X$."
5. Therefore: *compact* ("every open cover has a finite subcover") is equivalent to its contrapositive ("if no finite subfamily covers, the whole family does not cover"), which by steps 2–4 is exactly "every closed family with the FIP has nonempty intersection."

*The FIP form is the workhorse for Tychonoff's theorem (§s14) and for proving nested-set theorems like Cantor's.*

**Corollary — continuous bijection from compact to Hausdorff is a homeomorphism**

*If $f:X\to Y$ is a continuous bijection, $X$ compact and $Y$ Hausdorff, then $f$ is a homeomorphism.*

**Demonstration**

1. To show $f^{-1}$ is continuous, by characterization (ii) of §s7 it suffices to show $f$ maps closed sets to closed sets (a **closed map**), since for $g=f^{-1}$ we have $g^{-1}(C)=f(C)$.
2. Let $C\subseteq X$ be closed. A closed subset of a compact space is compact: any open cover of $C$, together with the open set $C^c$, covers $X$; a finite subcover, minus $C^c$, covers $C$.
3. So $C$ is compact, hence $f(C)$ is compact (continuous image, proved above), hence closed in the Hausdorff space $Y$ (compact $\Rightarrow$ closed, proved above).
4. Thus $f$ is a closed map, so $f^{-1}$ is continuous, so $f$ is a homeomorphism.

<a id="s13"></a>
### Compactness in metric spaces: sequential compactness & Heine–Borel

*In metric spaces three a-priori-different notions of compactness coincide, giving the most usable theorem in analysis.*

**Three notions of compactness**

- **Compact:** every open cover has a finite subcover (§s12).
- **Sequentially compact:** every sequence has a subsequence converging to a point of the space. (A **subsequence** keeps an infinite, increasingly-indexed selection of the original terms.)
- **Limit point compact:** every infinite subset has a limit point (§s5) in the space.

**Theorem — equivalence in metric spaces**

*For a metric space $X$, the following are equivalent: (i) compact; (ii) sequentially compact; (iii) limit point compact; (iv) complete **and** totally bounded.* (Here **totally bounded** means: for every $\varepsilon>0$, finitely many balls of radius $\varepsilon$ cover $X$; **complete** is defined in §s21.) In general topological spaces these notions can differ; the metric structure is what fuses them.

**Theorem — Heine–Borel**

$$K\subseteq\mathbb R^n \text{ is compact} \iff K \text{ is closed and bounded.}$$

(**Bounded** means $K$ fits inside some ball of finite radius.) This is what makes $[a,b]$ and closed balls compact, and underlies the Extreme Value and uniform-continuity theorems.

**Demonstration — $[0,1]$ is compact (bisection)**

1. Suppose, for contradiction, an open cover $\mathcal U$ of $[0,1]$ has no finite subcover. Bisect $[0,1]$ into $[0,\tfrac12]$ and $[\tfrac12,1]$. If *both* halves had finite subcovers, their union would be a finite subcover of $[0,1]$ — contradiction. So at least one half, call it $I_1$, has no finite subcover.
2. Repeat the bisection on $I_1$, getting $I_2\subseteq I_1$ with no finite subcover, and so on. This yields nested closed intervals $I_1\supseteq I_2\supseteq\cdots$ with lengths $|I_n|=2^{-n}\to 0$, each lacking a finite subcover.
3. By completeness of $\mathbb R$ (the nested interval property), the intersection $\bigcap_n I_n$ is a single point $x$. Since $\mathcal U$ covers $[0,1]$, some $U\in\mathcal U$ contains $x$; $U$ being open contains an interval $(x-\varepsilon,x+\varepsilon)$.
4. For $n$ large enough that $2^{-n}<\varepsilon$, we have $I_n\subseteq(x-\varepsilon,x+\varepsilon)\subseteq U$ (as $x\in I_n$ and $I_n$ has length $<\varepsilon$). So the single set $U$ covers $I_n$ — contradicting "no finite subcover." Hence the assumption fails and $[0,1]$ is compact.

*Bisection + completeness = compactness.* The general Heine–Borel follows: a closed bounded $K\subseteq\mathbb R^n$ sits inside a box $[-M,M]^n$, which is compact as a finite product of compact intervals (Tychonoff for finite products, §s14), and a closed subset of a compact space is compact (§s12). Conversely a compact subset of $\mathbb R^n$ is closed (Hausdorff, §s12) and bounded (else the cover by balls $B(0,m)$ has no finite subcover).

> **Connection — why infinite dimensions break Heine–Borel**
>
> In an infinite-dimensional normed space the closed unit ball is closed and bounded but **not** compact (Riesz's lemma builds a sequence with no convergent subsequence). This failure is the reason functional analysis needs weak topologies — and why Tychonoff's theorem becomes indispensable.

<a id="s14"></a>
### Tychonoff's theorem

*The deepest theorem of point-set topology: an arbitrary product of compact spaces is compact. Its proof needs the Axiom of Choice.*

**Theorem — Tychonoff**

$$\text{If each } X_\alpha \text{ is compact, then } \prod_{\alpha} X_\alpha \text{ (product topology) is compact.}$$

*Strikingly, the statement for arbitrary products is **equivalent** to the Axiom of Choice (Kelley). For Hausdorff factors it is weaker, equivalent to the ultrafilter lemma.*

> **Concept — proof strategy via the FIP / ultrafilters**
>
> The cleanest proof uses the FIP characterization (§s12). Take a family of closed sets in the product with the FIP; extend it (using Zorn's lemma, §s1) to a *maximal* family of subsets that still has the FIP. Maximality forces this family to be "decisive": for each subset, it contains either it or its complement, and it is closed under finite intersections and supersets. Project to each compact factor $X_\alpha$; by compactness (FIP form) the projected family has a common limit point $p_\alpha$. Assemble $p=(p_\alpha)_\alpha$. One checks every basic neighborhood of $p$ meets every member of the original family, so $p$ lies in the closure of each, hence in the total intersection — which is therefore nonempty. By the FIP characterization the product is compact. The ultrafilter version (§s20): every ultrafilter on a product converges iff each coordinate ultrafilter converges, which holds by compactness of factors.

> **Connection — what Tychonoff buys**
>
> It produces the Hilbert cube $[0,1]^{\mathbb N}$ as a compact space (basis for Urysohn metrization, §s19), the Stone–Čech compactification, and compactness of spaces of probability measures and of $\{0,1\}^X$ (Stone duality, compactness in logic). Almost every "big" compact space is built by Tychonoff.

> Worked example (finite case, fully concrete). The square $[0,1]\times[0,1]$ is compact. Given an open cover, for each fixed $x$ the slice $\{x\}\times[0,1]$ is compact (homeomorphic to $[0,1]$, §s13), so finitely many cover sets handle a tube $(x-\delta_x,x+\delta_x)\times[0,1]$ around it (the "tube lemma"). The intervals $(x-\delta_x,x+\delta_x)$ cover the compact $[0,1]$; take finitely many; the corresponding finitely many tubes, each finitely covered, give a finite subcover of the square. This is Tychonoff for two factors, made explicit.

<a id="s15"></a>
### Local compactness & the one-point compactification

*Many important spaces (like $\mathbb R^n$) are not compact but are compact "near each point." Such spaces can be made compact by adding a single point at infinity.*

**Definition — locally compact**

$X$ is **locally compact** if every point has a compact **neighborhood** (a set containing an open set around the point). For Hausdorff $X$ this is equivalent to: every point has a neighborhood basis of compact sets (arbitrarily small compact neighborhoods). Examples: $\mathbb R^n$ (each point sits in a closed ball, compact by Heine–Borel §s13), discrete spaces (each point $\{x\}$ is a compact neighborhood), all compact spaces. Non-example: $\mathbb Q$ (no neighborhood of a rational is compact, because it fails to be complete/closed in the needed way).

**Theorem — Alexandroff one-point compactification**

$$(\mathbb R^n)^+\cong S^n,\qquad \mathbb R^+\cong S^1,\qquad \mathbb C^+\cong S^2 \ (\text{the Riemann sphere}).$$

*For locally compact Hausdorff $X$, form $X^+=X\cup\{\infty\}$ by adjoining one new point $\infty$. Declare $V\subseteq X^+$ open iff either $V$ is open in $X$, or $V=\{\infty\}\cup(X\setminus K)$ for some compact $K\subseteq X$. Then $X^+$ is compact Hausdorff and $X$ is dense in it.*

**Demonstration — the declared family is a topology, and $X^+$ is compact**

First, that we have a topology:
1. $\varnothing$ is open (it is open in $X$); $X^+=\{\infty\}\cup(X\setminus\varnothing)$ with $\varnothing$ compact, so $X^+$ is open.
2. Unions and finite intersections of the two types of open set are again of one of the two types, using that finite unions of compact sets are compact and (in the Hausdorff case) compact sets are closed so $X\setminus K$ is open. (We omit the routine case-checking, which only uses §s12.)

Now compactness:
1. Let $\mathcal U$ be an open cover of $X^+$. Some member $U_0\in\mathcal U$ must contain $\infty$, so by the definition of open sets $U_0=\{\infty\}\cup(X\setminus K)$ for some compact $K\subseteq X$.
2. The remaining sets of $\mathcal U$, intersected with $X$, are open in $X$ and cover $K$ (they cover everything except possibly points of $K$, which $U_0$ misses). Since $K$ is compact, extract a finite subcover $U_1,\dots,U_n$ of $K$.
3. Then $U_0,U_1,\dots,U_n$ cover all of $X^+$: $U_0$ handles $\infty$ and all of $X\setminus K$, while $U_1,\dots,U_n$ handle $K$. A finite subcover exists, so $X^+$ is compact.

*The point at infinity "swallows" everything outside a compact set, converting local compactness into global compactness.*

> Worked example. $\mathbb R^+\cong S^1$. Map $S^1$ minus its north pole to $\mathbb R$ by stereographic projection (a homeomorphism); the north pole becomes the single point $\infty$. Open sets of $S^1$ around the north pole correspond exactly to sets $\{\infty\}\cup(\mathbb R\setminus K)$ with $K$ compact (the complements of large closed intervals), matching the one-point topology. So the circle *is* the line with one point added at infinity.

<a id="s16"></a>
### Countability axioms: first/second countable, separable, Lindelöf

*Smallness conditions that control how "big" a topology can be. They decide whether sequences suffice and whether covers can be thinned.*

**The four countability axioms**

A **neighborhood basis** at a point $x$ is a family of open sets containing $x$ such that every open set around $x$ contains a member of the family.

- **First countable:** every point has a *countable* neighborhood basis.
- **Second countable:** the whole topology has a *countable* basis (§s4).
- **Separable:** there is a *countable* dense subset (§s5).
- **Lindelöf:** every open cover has a *countable* subcover. (Like compactness, §s12, but with "countable" in place of "finite.")

**Implications**

$$\text{second countable}\ \Rightarrow\ \text{first countable},\ \text{separable, and Lindelöf}.$$

*In **metric** spaces, separable $\iff$ second countable $\iff$ Lindelöf. In general they diverge:* the lower-limit line $\mathbb R_\ell$ (§s3) is separable, first countable, and Lindelöf but **not** second countable.

**Demonstration — second countable $\Rightarrow$ first countable**

1. Let $\mathcal B=\{B_n\}$ be a countable basis. Fix a point $x$.
2. Let $\mathcal B_x=\{B_n\in\mathcal B: x\in B_n\}$, a subfamily of the countable $\mathcal B$, hence countable.
3. For any open $U\ni x$, the basis property (§s4) gives a basis element $B$ with $x\in B\subseteq U$; this $B$ is in $\mathcal B_x$. So $\mathcal B_x$ is a countable neighborhood basis at $x$, proving first countability.

**Demonstration — second countable $\Rightarrow$ separable**

1. Let $\{B_n\}$ be a countable basis; discard any empty $B_n$, and from each nonempty $B_n$ pick one point $x_n\in B_n$ (a countable use of the Axiom of Choice, §s1).
2. Let $D=\{x_n\}$, a countable set. For any nonempty open $U$, the basis property gives some nonempty $B_n\subseteq U$, so $x_n\in B_n\subseteq U$, i.e. $x_n\in U\cap D$.
3. Thus every nonempty open set meets $D$; by the membership form of closure (§s5), $\overline D=X$. So $D$ is countable and dense: $X$ is separable.

**Demonstration — second countable $\Rightarrow$ Lindelöf**

1. Let $\{B_n\}$ be a countable basis and $\{U_\alpha\}$ an open cover.
2. For each point $x$, pick $U_{\alpha(x)}\ni x$ and then a basis element $B_{n(x)}$ with $x\in B_{n(x)}\subseteq U_{\alpha(x)}$. Let $\mathcal N=\{B_n:\text{some }U_\alpha\supseteq B_n\}$; this is a subfamily of the countable basis, hence countable, and it covers $X$.
3. For each $B_n\in\mathcal N$ choose one $U_{\alpha_n}\supseteq B_n$. The countably many $\{U_{\alpha_n}\}$ cover $X$ (since the $B_n$ do), giving a countable subcover. So $X$ is Lindelöf.

*$\mathbb R^n$ is second countable* — the balls with rational center and rational radius form a countable basis — *hence separable ($\mathbb Q^n$ is dense) and Lindelöf.*

> **Connection — why first countable saves sequences**
>
> In a first-countable space sequences detect everything: $x\in\overline A$ iff some sequence in $A$ converges to $x$, and continuity equals sequential continuity. In spaces that are *not* first countable (e.g. $\mathbb R^{\mathbb R}$), sequences fail and you must use nets or filters (§s20).

<a id="s17"></a>
### Separation axioms: T0–T4, Hausdorff, regular, normal

*A hierarchy measuring how well open sets can tell points and closed sets apart. The higher you go, the more like a metric space you become.*

| Axiom | Name | Says: can separate… |
| --- | --- | --- |
| T0 | Kolmogorov | two distinct points by some open set containing exactly one |
| T1 | Fréchet | each of two points by an open set excluding the other ($\iff$ points are closed) |
| T2 | Hausdorff | two distinct points by *disjoint* open sets |
| T3 | Regular (+T1) | a point and a closed set not containing it, by disjoint opens |
| T3½ | Tychonoff / completely regular | a point and a closed set by a continuous $[0,1]$-function |
| T4 | Normal (+T1) | two disjoint closed sets by disjoint open sets |

"Separate by disjoint open sets" means: put each thing inside its own open set, with the two open sets not overlapping.

**Demonstration — T1 is equivalent to "all singletons are closed"**

1. ($\Rightarrow$) Assume T1. Fix a point $p$. For each $x\ne p$, T1 gives an open set $U_x\ni x$ with $p\notin U_x$. Then $X\setminus\{p\}=\bigcup_{x\ne p}U_x$ is a union of open sets, hence open; so $\{p\}$ is closed.
2. ($\Leftarrow$) Assume every singleton is closed. Given $x\ne y$, the set $X\setminus\{y\}$ is open, contains $x$, and excludes $y$; symmetrically $X\setminus\{x\}$ works the other way. That is exactly T1.

> **Concept — the staircase**
>
> Roughly $T4\Rightarrow T3\tfrac12\Rightarrow T3\Rightarrow T2\Rightarrow T1\Rightarrow T0$ (with the convention that $T3,T4$ include $T1$). Each step is strictly stronger; standard counterexamples separate consecutive levels. The cofinite topology on an infinite set (§s3) is $T1$ (singletons are finite, hence closed) but not $T2$ (any two nonempty open sets intersect, proved in §s3).

**Demonstration — every metric space is normal (T4)**

1. Let $A,B$ be disjoint closed sets in a metric space. Define the **distance to a set** $d(x,A)=\inf_{a\in A}d(x,a)$. This function is continuous (indeed $|d(x,A)-d(y,A)|\le d(x,y)$ by the triangle inequality) and satisfies $d(x,A)=0$ iff $x\in\overline A=A$ (since $A$ is closed).
2. Define $U=\{x: d(x,A)<d(x,B)\}$ and $V=\{x:d(x,B)<d(x,A)\}$. Each is open as the set where one continuous function is strictly less than another (it is the preimage of $(0,\infty)$ under the continuous map $x\mapsto d(x,B)-d(x,A)$, resp. its negative). They are disjoint, since the strict inequalities $d(x,A)<d(x,B)$ and $d(x,B)<d(x,A)$ cannot both hold.
3. If $a\in A$: then $d(a,A)=0$, and $d(a,B)>0$ because $a\notin B$ and $B$ is closed (so $d(a,B)=0$ would force $a\in B$). Thus $d(a,A)=0<d(a,B)$, so $a\in U$; hence $A\subseteq U$. Symmetrically $B\subseteq V$. So $A,B$ are separated by the disjoint open sets $U,V$: the space is normal.

*Metric spaces sit at the top of the staircase — they are even perfectly normal. This is why metrizability (§s19) is so strong.*

> **Connection — Hausdorff is the workhorse**
>
> Hausdorffness guarantees *limits are unique* (a sequence/net cannot converge to two points separated by disjoint open sets) and that compact sets are closed (§s12). Almost every space in analysis and geometry is assumed Hausdorff. Compact Hausdorff spaces are automatically normal — the hypothesis behind Urysohn and Tietze next.

<a id="s18"></a>
### Urysohn's lemma & the Tietze extension theorem

*In a normal space, abstract separation by open sets upgrades to separation by an honest continuous function — the bridge from topology back to analysis.*

**Theorem — Urysohn's lemma**

In a normal space $X$, for any two disjoint closed sets $A,B$ there is a continuous function

$$f:X\to[0,1]\quad\text{with}\quad f|_A=0\ \text{ and }\ f|_B=1.$$

(The notation $f|_A=0$ means $f$ takes the value $0$ at every point of $A$.) *Such an $f$ need not be $0$ only on $A$; the lemma asserts existence, not exact level sets.*

> **Concept — how the function is built**
>
> Normality lets us insert, for every **dyadic rational** $r\in(0,1)$ (a fraction with denominator a power of $2$, like $\tfrac12,\tfrac14,\tfrac34$), an open set $U_r$ with $A\subseteq U_0$, $U_1=X\setminus B$, and crucially $\overline{U_r}\subseteq U_s$ whenever $r<s$ (each "shell" sits strictly inside the next). This nesting is arranged step by step using normality to slip a new set between $\overline{U_r}$ and $U_s$. Define $f(x)=\inf\{r: x\in U_r\}$ (and $f(x)=1$ if $x$ is in no $U_r$). The dense nesting of the $U_r$ makes $f$ continuous, and by construction $f=0$ on $A$ and $f=1$ on $B$. The "topological interpolation" by dyadics is the whole trick.

**Demonstration — why $f$ is continuous (sketch made rigorous on subbasic sets)**

1. The intervals $[0,a)$ and $(a,1]$ form a subbasis of $[0,1]$, so by §s7 it suffices to show $f^{-1}([0,a))$ and $f^{-1}((a,1])$ are open.
2. $f(x)<a$ means $x\in U_r$ for some dyadic $r<a$ (by definition of infimum), so $f^{-1}([0,a))=\bigcup_{r<a}U_r$, a union of open sets, hence open.
3. $f(x)>a$ means $x\notin\overline{U_r}$ for some dyadic $r>a$; using the nesting $\overline{U_r}\subseteq U_s$, one gets $f^{-1}((a,1])=\bigcup_{r>a}\big(X\setminus\overline{U_r}\big)$, again a union of open sets, hence open.
4. Preimages of subbasic open sets are open, so $f$ is continuous.

**Theorem — Tietze extension**

*Let $X$ be normal and $A\subseteq X$ closed. Every continuous $f:A\to[a,b]$ (or $A\to\mathbb R$) extends to a continuous $F:X\to[a,b]$ (resp. $\mathbb R$) with $F|_A=f$.* (To **extend** means $F$ agrees with $f$ on $A$ but is defined on all of $X$.) *Conversely, this extension property characterizes normality.*

> **Connection — Urysohn powers Tietze, and metrization**
>
> Tietze is proved by repeatedly applying Urysohn's lemma to build the extension as a uniformly convergent series of "correction" functions, each shaving off a fixed fraction of the remaining error. Urysohn's lemma is also the key ingredient in the metrization theorem of §s19 — it supplies the continuous functions needed to embed the space.

<a id="s19"></a>
### The Urysohn metrization theorem

*When does an abstract topology secretly come from a metric? Urysohn gives a clean sufficient condition.*

**Theorem — Urysohn metrization**

*Every **second-countable** (§s16) **regular** (T3, §s17) space is **metrizable** — there exists a metric whose induced open sets are exactly the given topology.* (Such a space is automatically normal, so Urysohn's lemma §s18 applies.)

**Demonstration — embedding into the Hilbert cube**

1. Using second countability together with normality, construct a countable family of Urysohn functions $f_n:X\to[0,1]$ that *separates points from closed sets*: for any point $x$ and closed set $C$ with $x\notin C$, some $f_n$ has $f_n(x)=0$ and $f_n=1$ on $C$. (Take pairs of basis elements $B_i\subseteq\overline{B_i}\subseteq B_j$ and apply Urysohn's lemma §s18 to $\overline{B_i}$ and $X\setminus B_j$; there are countably many such pairs.)
2. Combine them into one map $F:X\to[0,1]^{\mathbb N}$, $F(x)=(f_1(x),f_2(x),\dots)$. Each coordinate $\pi_n\circ F=f_n$ is continuous, so by the universal property of products (§s8) $F$ is continuous. The separating property of step 1 makes $F$ **injective** and an **embedding** (a homeomorphism onto its image $F(X)$ with the subspace topology): distinct points get distinct coordinate-patterns, and $F$ carries open sets to relatively open sets.
3. The **Hilbert cube** $[0,1]^{\mathbb N}$ (the product of countably many copies of $[0,1]$) is metrizable by

   $$d(x,y)=\sum_{n=1}^\infty 2^{-n}\,|x_n-y_n|.$$

   This series converges (each term is at most $2^{-n}$, and $\sum 2^{-n}=1$), and one checks it satisfies the three metric axioms (§s2), inducing the product topology. A subspace of a metric space is again a metric space (use the same $d$, §s6). Since $X\cong F(X)\subseteq[0,1]^{\mathbb N}$, the space $X$ is metrizable.

*Metrizability becomes "embeddable in a known metric space." The deep general answer is the Nagata–Smirnov theorem (metrizable iff regular with a $\sigma$-locally-finite basis).*

> **Connection — closing the loop with Part A**
>
> We started from metric spaces (§s2), abstracted away the metric (§s3), and now recover exactly which abstract spaces were metric all along. The countability and separation axioms turn out to be precisely the fingerprints a metric leaves on a topology.

## Part D · Convergence & completeness

<a id="s20"></a>
### Nets & filters: convergence in general spaces

*Sequences are too short to see all of topology. Nets and filters are the two equivalent fixes that make convergence work in any space.*

> **Concept — why sequences fail**
>
> In a non-first-countable space (§s16) a point can lie in $\overline A$ with *no* sequence in $A$ reaching it, and a discontinuous function can be sequentially continuous. The fix: index the "sequence" by an arbitrary directed set instead of by $\mathbb N$, so it can be long enough to probe every neighborhood.

**Definition — directed set & net**

A **directed set** $(D,\leq)$ is a set with a relation that is reflexive and transitive (a **preorder**) in which any two elements have a common upper bound: for $d_1,d_2\in D$ there is $d_3$ with $d_1\le d_3$ and $d_2\le d_3$. A **net** is a function $x:D\to X$, written $(x_d)_{d\in D}$. It **converges** to $p$ if for every open $U\ni p$ there is an index $d_0$ such that $x_d\in U$ for all $d\geq d_0$ (the net is *eventually* in $U$).

A sequence is the special case $D=\mathbb N$; nets allow far richer index sets (for instance, the open neighborhoods of a point, ordered by reverse inclusion).

**Definition — filter & ultrafilter**

A **filter** $\mathcal F$ on $X$ is a nonempty family of nonempty subsets of $X$ that is closed under taking supersets (if $F\in\mathcal F$ and $F\subseteq G$ then $G\in\mathcal F$) and under finite intersections (if $F_1,F_2\in\mathcal F$ then $F_1\cap F_2\in\mathcal F$). It **converges** to $p$ if every neighborhood of $p$ belongs to $\mathcal F$. A maximal filter (one not contained in a strictly larger filter) is an **ultrafilter**; equivalently, for every set $S\subseteq X$, an ultrafilter contains $S$ or its complement $S^c$.

**Theorem — nets/filters characterize everything**

*$x\in\overline A$ iff some net in $A$ converges to $x$. $f$ is continuous iff it preserves convergence of all nets. **$X$ is compact iff every net has a convergent subnet, iff every ultrafilter converges.** $X$ is Hausdorff iff every net has at most one limit.*

**Demonstration — $x\in\overline A$ iff some net in $A$ converges to $x$**

1. ($\Leftarrow$) Suppose a net $(x_d)$ in $A$ converges to $x$. For any open $U\ni x$, the net is eventually in $U$, so in particular $U$ contains some $x_d\in A$, i.e. $U\cap A\ne\varnothing$. By the membership form of closure (§s5), $x\in\overline A$.
2. ($\Rightarrow$) Suppose $x\in\overline A$. Let $D$ be the set of open neighborhoods of $x$, ordered by *reverse* inclusion ($U\le V$ iff $V\subseteq U$); this is directed because $U_1\cap U_2$ is a common (smaller, hence "larger" in this order) neighborhood. For each $U\in D$, $x\in\overline A$ guarantees $U\cap A\ne\varnothing$, so choose $x_U\in U\cap A$. The net $(x_U)_{U\in D}$ lies in $A$ and converges to $x$: given any open $V\ni x$, for all $U\le V$ (i.e. $U\subseteq V$) we have $x_U\in U\subseteq V$. So the net is eventually in $V$.

> **Connection — the slick Tychonoff proof**
>
> The ultrafilter criterion gives Tychonoff (§s14) in three lines: take an ultrafilter on the product; project it to each factor, where compactness yields a limit $p_\alpha$; the product point $p=(p_\alpha)$ is the limit of the original ultrafilter (a basic neighborhood of $p$ constrains finitely many coordinates, each of which the projected ultrafilter handles). Filters convert hard covering arguments into clean convergence statements.

<a id="s21"></a>
### Complete metric spaces & completion

*Completeness — every Cauchy sequence converges — is a metric (not purely topological) property, yet it underwrites all of analysis.*

**Definition — Cauchy & complete**

A sequence $(x_n)$ in a metric space is **Cauchy** if its terms eventually get arbitrarily close *to each other*:

$$\forall\varepsilon\gt 0\ \exists N\ \forall m,n\geq N:\ d(x_m,x_n)\lt\varepsilon.$$

A metric space is **complete** if every Cauchy sequence converges to a point *of the space*. $\mathbb R^n$ is complete; $\mathbb Q$ is not.

**Demonstration — every convergent sequence is Cauchy (but not conversely)**

1. Suppose $x_n\to x$. Given $\varepsilon>0$, by convergence there is $N$ with $d(x_n,x)<\varepsilon/2$ for all $n\ge N$.
2. Then for $m,n\ge N$, the triangle inequality gives $d(x_m,x_n)\le d(x_m,x)+d(x,x_n)<\varepsilon/2+\varepsilon/2=\varepsilon$. So $(x_n)$ is Cauchy.
3. The converse fails *in $\mathbb Q$*: the sequence $3,\,3.1,\,3.14,\,3.141,\dots$ of decimal truncations of $\pi$ is Cauchy (consecutive terms differ by at most $10^{-n}$), yet it has no limit in $\mathbb Q$ because $\pi$ is irrational. So $\mathbb Q$ is not complete.

> **Concept — completeness is not topological**
>
> $(0,1)$ and $\mathbb R$ are homeomorphic (e.g. via $x\mapsto\tan(\pi(x-\tfrac12))$), yet $\mathbb R$ is complete and $(0,1)$ is not (the sequence $1/n$ is Cauchy in $(0,1)$ but its limit $0$ is missing). Completeness depends on the *metric*, not just the open sets. The topological shadow of completeness is "complete metrizability," and Baire's theorem (§s22) is what survives.

**Theorem — completion**

*Every metric space $X$ embeds isometrically as a dense subset of a complete metric space $\widehat X$, unique up to isometry.* (An **isometry** is a distance-preserving map.) **Construction:** $\widehat X$ is the set of equivalence classes of Cauchy sequences in $X$, where $(x_n)\sim(y_n)$ iff $d(x_n,y_n)\to 0$, with distance

$$\widehat d\big(\langle x_n\rangle,\langle y_n\rangle\big)=\lim_n d(x_n,y_n).$$

For example $\widehat{\mathbb Q}=\mathbb R$ — the real numbers *are* the completion of the rationals.

> **Connection — fixed points & analysis**
>
> Completeness makes the **Banach fixed-point theorem** work (a contraction on a complete space has a unique fixed point), which proves existence/uniqueness for ODEs and implicit functions. Completeness of function spaces $C[a,b]$ and $L^p$ is the foundation of functional analysis.

<a id="s22"></a>
### The Baire category theorem

*A deep statement that complete spaces cannot be "small": they are not a countable union of negligible pieces. It powers many existence theorems by pure topology.*

**Definitions — nowhere dense, meager**

A set is **nowhere dense** if its closure has empty interior ($\mathrm{int}\overline A=\varnothing$, §s5) — intuitively, it is so thin that even after filling in limit points it contains no little open patch. A set is **meager** (or **first category**) if it is a countable union of nowhere dense sets; otherwise it is **nonmeager** (**second category**).

> Worked example. In $\mathbb R$, a single point $\{p\}$ is nowhere dense (its closure is itself, with empty interior). Any countable set, like $\mathbb Q$, is meager, being a countable union of points. The Baire theorem below will show $\mathbb R$ itself is *not* meager, which is why $\mathbb R\ne\mathbb Q$ in a strong sense.

**Theorem — Baire category**

*In a **complete metric space** (or a locally compact Hausdorff space), the intersection of countably many dense open sets is dense. Equivalently, such a space is **not** meager in itself.*

**Demonstration — proof of the Baire category theorem**

1. Let $\{U_n\}_{n\ge1}$ be dense open sets in a complete metric space $X$, and let $W$ be any nonempty open set. We will produce a point in $W\cap\bigcap_n U_n$, proving that intersection is dense.
2. Since $U_1$ is dense, $W\cap U_1$ is nonempty (a dense set meets every nonempty open set, §s5) and open. Choose a point and a small radius to get a closed ball $\overline{B_1}=\overline{B(x_1,r_1)}\subseteq W\cap U_1$ with $r_1<1$. (We can fit a *closed* ball because $W\cap U_1$ is open, so it contains an open ball, and a slightly smaller closed ball.)
3. Inductively, having $\overline{B_n}$, use that $U_{n+1}$ is dense and open: $B_n\cap U_{n+1}$ is nonempty open, so choose a closed ball $\overline{B_{n+1}}\subseteq B_n\cap U_{n+1}$ with $r_{n+1}<r_n/2$. The radii shrink: $r_n<2^{-(n-1)}\to 0$.
4. The centers $(x_n)$ form a Cauchy sequence: for $m\ge n$, $x_m\in B_m\subseteq B_n$, so $d(x_m,x_n)<r_n\to 0$. By completeness $x_n\to x$ for some $x\in X$.
5. For each fixed $n$, all later centers $x_m$ ($m\ge n$) lie in the closed set $\overline{B_n}$, so the limit does too: $x\in\overline{B_n}$. By construction $\overline{B_n}\subseteq U_n$ for $n\ge1$ and $\overline{B_1}\subseteq W$. Hence $x\in W$ and $x\in U_n$ for every $n$, i.e. $x\in W\cap\bigcap_n U_n\ne\varnothing$.
6. Since $W$ was an arbitrary nonempty open set, $\bigcap_n U_n$ meets every one, so it is dense. The "not meager" form follows by taking complements: if $X=\bigcup_n A_n$ with each $A_n$ nowhere dense, then the open dense sets $U_n=X\setminus\overline{A_n}$ would have empty intersection, contradicting density.

*Completeness (Cauchy sequences converge) + nested shrinking closed balls = the theorem. The locally compact case replaces shrinking balls with nested compact sets and the FIP (§s12).*

> **Connection — what Baire proves**
>
> Baire shows $\mathbb R$ is uncountable (each point is nowhere dense, and a complete space cannot be a countable union of nowhere dense sets, so $\mathbb R$ is not the countable union of its points); it yields the existence of continuous nowhere-differentiable functions, and underpins the three pillars of functional analysis — the **uniform boundedness**, **open mapping**, and **closed graph** theorems. Topology, with no extra analysis, forces these existence results.

---

*A first course in general (point-set) topology — definitions stated precisely, the central theorems proved, and every thread back to metric-space analysis and forward to algebraic and functional analysis made explicit. Read once for the architecture: metric spaces motivate open sets; open sets define continuity; the four constructions build new spaces; connectedness and compactness are the load-bearing invariants; separation and countability decide metrizability; and completeness with Baire returns us to analysis. Return to any box as a reference.*
