# Topology, *nearness without distance.*

A full first course in point-set topology — from open sets to compactness, connectedness, and the great metrization theorems. Built basics → expert. Core definitions are stated cleanly and the central theorems are **proved**, with every thread back to analysis and forward to algebraic topology made explicit.

[← Back to all guides](../README.md)

## Part A · Foundations

<a id="s0"></a>
### The big picture: what topology is

*Topology is the study of those properties of space that survive continuous deformation — "rubber-sheet geometry." It is the language of nearness, stripped of distance, area, and angle.*

In a metric space we know *how far apart* two points are. Topology asks the bolder question: what can we say if we throw away the numbers and keep only the notion of which points are **close to** which sets? The astonishing answer is that almost everything analysts care about — continuity, convergence, compactness, connectedness — can be phrased using nothing but a distinguished family of "open sets."

> **Principle — the central abstraction**
>
> A **topology** on a set $X$ is a choice of which subsets count as **open**. From that single choice flow all the topological concepts: a continuous function is one whose preimages of open sets are open; convergence, closure, and compactness are all defined through open sets. Geometry is replaced by a calculus of open sets.

#### The whole course on one line

> Metric spaces → Open sets & topologies → Continuity & constructions → Connectedness & compactness → Separation & metrization → Nets, completeness, Baire

> **Connection — why it matters**
>
> Topology is the foundation beneath real analysis, functional analysis, differential geometry, and algebraic topology. The same axioms describe $\mathbb R^n$, the space of continuous functions, the Zariski topology of algebraic geometry, and the profinite groups of number theory. Learn the abstraction once; reuse it everywhere.

<a id="s1"></a>
### Set-theory toolkit: functions, relations, cardinality, Zorn's lemma

*Topology is set theory with a chosen structure. We collect the language we will lean on constantly.*

**Sets, images & preimages**

$$f^{-1}(B)=\{x\in X: f(x)\in B\},\qquad f(A)=\{f(x): x\in A\}$$

*Preimage respects all set operations: $f^{-1}(\bigcup_\alpha B_\alpha)=\bigcup_\alpha f^{-1}(B_\alpha)$, $f^{-1}(\bigcap_\alpha B_\alpha)=\bigcap_\alpha f^{-1}(B_\alpha)$, and $f^{-1}(B^c)=\big(f^{-1}(B)\big)^c$. This is exactly why topology is built on preimages, not images.*

**De Morgan's laws (the workhorse)**

$$\Big(\bigcup_{\alpha} A_\alpha\Big)^c=\bigcap_\alpha A_\alpha^c,\qquad \Big(\bigcap_\alpha A_\alpha\Big)^c=\bigcup_\alpha A_\alpha^c$$

*These convert statements about open sets (closed under arbitrary unions) into statements about closed sets (closed under arbitrary intersections).*

> **Concept — relations, equivalences, partitions**
>
> An **equivalence relation** $\sim$ on $X$ (reflexive, symmetric, transitive) partitions $X$ into disjoint **equivalence classes** $[x]=\{y: y\sim x\}$. The set of classes is the **quotient** $X/\!\sim$. This is the engine behind the quotient topology of Section 9.

**Cardinality**

*A set is **countable** if it injects into $\mathbb N$ (finite or countably infinite). Key facts: a countable union of countable sets is countable; $\mathbb Q$ is countable; $\mathbb R$ is uncountable (Cantor's diagonal argument). Countability governs the second-countable, separable, and Lindelöf properties of Section 16.*

**Partial orders & Zorn's lemma**

$$\textbf{Zorn's lemma: } \text{if every chain in a poset has an upper bound, the poset has a maximal element.}$$

*A **partial order** $\leq$ is reflexive, antisymmetric, transitive. A **chain** is a totally ordered subset; an **upper bound** of a subset $S$ is an element $\geq$ everything in $S$; a **maximal element** has nothing strictly above it.*

> **Principle — choice in disguise**
>
> Zorn's lemma is equivalent to the **Axiom of Choice** and to the **Well-Ordering Theorem**. In topology it is the hidden engine behind Tychonoff's theorem (Section 14), the existence of maximal ideals, and the ultrafilter lemma for nets and filters (Section 20).

<a id="s2"></a>
### Metric spaces: open balls, convergence, the prototype

*Metric spaces are the concrete ancestor of topology. Every intuition you have about openness, continuity, and limits comes from here.*

**Definition — metric space**

$$d:X\times X\to[0,\infty),\quad d(x,y)=0\iff x=y,\quad d(x,y)=d(y,x),\quad d(x,z)\leq d(x,y)+d(y,z).$$

*The last is the **triangle inequality**. Example metrics on $\mathbb R^n$: Euclidean $d_2$, taxicab $d_1$, and the max metric $d_\infty$.*

**Definition — open ball & open set**

$$B(x,r)=\{y\in X: d(x,y)\lt r\}$$

*A set $U\subseteq X$ is **open** if every point of it has some ball entirely inside $U$: for all $x\in U$ there is $r\gt 0$ with $B(x,r)\subseteq U$.*

**Demonstration — open balls are open**

1. Take $y\in B(x,r)$, so $d(x,y)\lt r$. Let $s=r-d(x,y)\gt 0$.
2. For any $z\in B(y,s)$, the triangle inequality gives

   $$d(x,z)\leq d(x,y)+d(y,z)\lt d(x,y)+s=r.$$
3. Hence $z\in B(x,r)$, so $B(y,s)\subseteq B(x,r)$. Every point of the ball has a ball inside it.

*The triangle inequality is precisely what makes the open-set definition consistent.*

**Definition — convergence & continuity (metric form)**

$$x_n\to x \iff \forall\varepsilon\gt 0\ \exists N\ \forall n\geq N:\ d(x_n,x)\lt\varepsilon$$

$$f \text{ continuous at } x \iff \forall\varepsilon\gt 0\ \exists\delta\gt 0:\ d(x,y)\lt\delta\Rightarrow d'\big(f(x),f(y)\big)\lt\varepsilon$$

> **Connection — the leap to topology**
>
> Both definitions can be re-read using only open sets: $x_n\to x$ means every open set containing $x$ eventually contains all $x_n$; $f$ is continuous iff preimages of open sets are open. Topology keeps these reformulations and *discards the metric*. Sections 3 and 7 make this precise.

## Part B · Topological spaces

<a id="s3"></a>
### Topological spaces & open sets

*The central definition of the subject. Three axioms abstract everything we learned about open sets in metric spaces.*

**Definition — topology**

$$\text{(T1)}\ \ \varnothing\in\tau,\ X\in\tau;$$

$$\text{(T2)}\ \ U_\alpha\in\tau\ \Rightarrow\ \bigcup_\alpha U_\alpha\in\tau\quad(\text{arbitrary unions});$$

$$\text{(T3)}\ \ U_1,\dots,U_n\in\tau\ \Rightarrow\ \bigcap_{i=1}^n U_i\in\tau\quad(\text{finite intersections}).$$

*The pair $(X,\tau)$ is a **topological space**. A set is **closed** if its complement is open.*

**Demonstration — the metric open sets satisfy the three axioms**

1. (T1) $\varnothing$ is vacuously open; $X$ is open since any ball lies in $X$.
2. (T2) If $x\in\bigcup_\alpha U_\alpha$, then $x\in U_{\alpha_0}$ for some $\alpha_0$; a ball about $x$ lies in $U_{\alpha_0}\subseteq\bigcup_\alpha U_\alpha$.
3. (T3) If $x\in\bigcap_{i=1}^n U_i$, pick $r_i$ with $B(x,r_i)\subseteq U_i$; then $r=\min_i r_i\gt 0$ and $B(x,r)\subseteq\bigcap U_i$. The minimum needs finiteness.

*Infinite intersections fail: $\bigcap_{n}(-\tfrac1n,\tfrac1n)=\{0\}$ is not open. That is why (T3) is only finite.*

**A zoo of topologies on a set $X$**

***Discrete:** every subset is open ($\tau=\mathcal P(X)$). **Indiscrete/trivial:** only $\varnothing$ and $X$. **Cofinite:** open sets are $\varnothing$ and the complements of finite sets. **Standard on $\mathbb R$:** generated by open intervals. **Lower-limit $\mathbb R_\ell$:** generated by half-open intervals $[a,b)$.*

> **Concept — finer vs coarser**
>
> If $\tau_1\subseteq\tau_2$ we say $\tau_2$ is **finer** (more open sets, more "resolution") and $\tau_1$ is **coarser**. The discrete topology is the finest possible; the indiscrete the coarsest. A finer topology makes more functions *out of* the space continuous and fewer *into* it.

> **Connection — the cofinite topology as a teacher**
>
> On an infinite set the cofinite topology is the simplest example where points are closed but the space is not Hausdorff: any two nonempty open sets intersect. It recurs as a counterexample throughout Part C.

<a id="s4"></a>
### Basis & subbasis for a topology

*Listing every open set is hopeless. A basis is a small "alphabet" of open sets from which all others are spelled by union.*

**Definition — basis**

$$\text{(B1)}\ \ \bigcup_{B\in\mathcal B}B=X;\qquad \text{(B2)}\ \ x\in B_1\cap B_2\ \Rightarrow\ \exists B_3\in\mathcal B,\ x\in B_3\subseteq B_1\cap B_2.$$

*The **topology generated by $\mathcal B$** is: $U$ is open iff for every $x\in U$ there is $B\in\mathcal B$ with $x\in B\subseteq U$. Equivalently, open sets are exactly arbitrary unions of basis elements.*

**Demonstration — the generated collection is a topology**

1. $\varnothing$ is open vacuously; $X$ is open by (B1).
2. Unions: if each $U_\alpha$ is a union of basis elements, so is $\bigcup_\alpha U_\alpha$. Closed under arbitrary unions.
3. Finite intersections: for $x\in U_1\cap U_2$ take basis sets $B_1,B_2$ with $x\in B_i\subseteq U_i$; by (B2) some $B_3\subseteq B_1\cap B_2\subseteq U_1\cap U_2$ contains $x$. So the intersection is open.

*(B2) is exactly the condition that makes finite intersections work.*

**Definition — subbasis**

*A **subbasis** $\mathcal S$ is any collection covering $X$. The topology it generates has as a basis all *finite intersections* of members of $\mathcal S$; open sets are arbitrary unions of those. Subbases let us specify a topology by naming just a few "must be open" sets — the product topology of Section 8 is defined this way.*

> **Connection — open balls are a basis**
>
> In a metric space the open balls $\{B(x,r)\}$ form a basis, and the topology they generate is exactly the metric topology of Section 2. The rays $(a,\infty)$ and $(-\infty,b)$ form a subbasis for the standard topology on $\mathbb R$. Bases are how almost every concrete topology is presented.

<a id="s5"></a>
### Closure, interior, boundary & limit points

*Given any set, topology produces three canonical relatives: the largest open set inside it, the smallest closed set around it, and the rim between.*

**Definition — interior, closure, boundary**

$$\operatorname{int}A=\bigcup\{U\subseteq A: U\text{ open}\},\qquad \overline{A}=\bigcap\{C\supseteq A: C\text{ closed}\}$$

$$\partial A=\overline{A}\setminus\operatorname{int}A=\overline A\cap\overline{A^c}$$

*So $\operatorname{int}A$ is the largest open subset of $A$; $\overline A$ is the smallest closed superset of $A$; always $\operatorname{int}A\subseteq A\subseteq\overline A$.*

**Definition — limit point & the closure characterization**

$$\overline{A}=A\cup A'=\{x: \text{every open } U\ni x \text{ has } U\cap A\neq\varnothing\}.$$

*A point of $\overline A$ that is not a limit point is an **isolated point**. $A$ is **dense** if $\overline A=X$.*

**Demonstration — a set is open iff it equals its interior**

1. ($\Leftarrow$) If $A=\operatorname{int}A$, then $A$ is a union of open sets, hence open.
2. ($\Rightarrow$) Suppose $A$ is open. Then $A$ is itself one of the open sets $U\subseteq A$ in the union defining $\operatorname{int}A$, so $A\subseteq\operatorname{int}A$.
3. Always $\operatorname{int}A\subseteq A$. Combining, $\operatorname{int}A=A$.

*Dually, $A$ is closed $\iff A=\overline A\iff A'\subseteq A$.*

**Demonstration — the Kuratowski closure axioms**

1. $\overline{\varnothing}=\varnothing$ and $A\subseteq\overline A$: immediate from the definition.
2. Idempotence: $\overline{\overline A}=\overline A$ since $\overline A$ is already closed.
3. Finite additivity: $\overline{A\cup B}=\overline A\cup\overline B$. The right side is closed and contains $A\cup B$, so $\overline{A\cup B}\subseteq\overline A\cup\overline B$; the reverse holds since closure is monotone.

*These four properties can *replace* the open-set axioms: a closure operator defines a topology. A beautiful instance of equivalent foundations.*

> **Connection — $\mathbb Q$ is dense in $\mathbb R$**
>
> Every interval contains a rational, so $\overline{\mathbb Q}=\mathbb R$. Density is the topological skeleton of approximation in analysis, and a countable dense set is exactly separability (Section 16).

<a id="s6"></a>
### The subspace topology

*Any subset of a space becomes a space in its own right by intersecting open sets with it. This is the first of our four constructions.*

**Definition — subspace (relative) topology**

$$\tau_A=\{U\cap A: U\in\tau\}$$

*The open sets of $A$ are exactly the traces of open sets of $X$. One checks (T1)–(T3) hold because intersection distributes over unions and finite intersections.*

> **Concept — "open in $A$" is relative**
>
> A set can be open in $A$ without being open in $X$. Example: $[0,\tfrac12)$ is open in $A=[0,1]$ (it equals $(-\tfrac12,\tfrac12)\cap A$) but not open in $\mathbb R$. Openness and closedness are always *relative to a chosen ambient space*.

**Demonstration — closed-in-subspace are traces of closed sets**

1. $F$ is closed in $A$ iff $A\setminus F=U\cap A$ for some open $U$ of $X$.
2. Then $F=A\setminus(U\cap A)=A\cap U^c$, and $U^c$ is closed in $X$.
3. Conversely the trace $A\cap C$ of any closed $C$ has open complement $A\cap C^c$ in $A$.

*So "closed in the subspace" = "trace of a closed set," perfectly dual to the open case.*

> **Connection — heredity**
>
> Some properties pass to every subspace ("hereditary": Hausdorff, second countable, metrizable); others only to closed or open subspaces (compactness passes to closed subspaces; local compactness to open ones). Track this carefully — the summary table in Section 17/the preservation table flags it.

<a id="s7"></a>
### Continuous functions & homeomorphisms

*Continuity is the morphism of topology. Remarkably, it is captured entirely by preimages of open sets — no $\varepsilon$, no $\delta$.*

**Definition — continuous map**

*$f:X\to Y$ is **continuous** if $f^{-1}(V)$ is open in $X$ for every open $V\subseteq Y$. It suffices to check this on a basis (or subbasis) of $Y$.*

**Demonstration — metric continuity $\iff$ preimages of open sets are open**

1. ($\Rightarrow$) Assume the $\varepsilon$-$\delta$ condition. Let $V$ be open in $Y$ and $x\in f^{-1}(V)$. Since $f(x)\in V$, some ball $B(f(x),\varepsilon)\subseteq V$. By continuity at $x$ there is $\delta$ with $f(B(x,\delta))\subseteq B(f(x),\varepsilon)\subseteq V$, so $B(x,\delta)\subseteq f^{-1}(V)$. Thus $f^{-1}(V)$ is open.
2. ($\Leftarrow$) Assume preimages of opens are open. Fix $x$ and $\varepsilon\gt 0$. The set $V=B(f(x),\varepsilon)$ is open, so $f^{-1}(V)$ is open and contains $x$; pick $\delta$ with $B(x,\delta)\subseteq f^{-1}(V)$.
3. Then $d(x,y)\lt\delta\Rightarrow f(y)\in V\Rightarrow d'(f(x),f(y))\lt\varepsilon$. That is exactly continuity at $x$.

*The topological definition recovers — and generalizes — the analyst's. Preimage, not image, because preimage commutes with unions, intersections, and complements.*

**Equivalent characterizations of continuity**

*For $f:X\to Y$ the following are equivalent: (i) preimages of open sets are open; (ii) preimages of closed sets are closed; (iii) $f(\overline A)\subseteq\overline{f(A)}$ for all $A$; (iv) for each $x$ and each open $V\ni f(x)$, some open $U\ni x$ has $f(U)\subseteq V$.*

**Definition — homeomorphism**

*A **homeomorphism** is a continuous bijection $f$ whose inverse $f^{-1}$ is also continuous. Spaces related by one are **homeomorphic** — "topologically the same." A continuous bijection need *not* be a homeomorphism (e.g. $[0,1)\to S^1,\ t\mapsto e^{2\pi i t}$).*

> **Concept — topological invariants**
>
> A property preserved by homeomorphism is a **topological invariant**: connectedness, compactness, Hausdorffness, the countability axioms. To prove two spaces are *not* homeomorphic, exhibit an invariant they differ on. ($\mathbb R$ and $\mathbb R^2$ differ because removing a point disconnects only the former.)

> **Connection — composition & the gluing lemma**
>
> Compositions of continuous maps are continuous (preimage of preimage). The **pasting lemma**: if $X=A\cup B$ with $A,B$ both closed (or both open) and $f$ is continuous on each agreeing on $A\cap B$, then $f$ is continuous on $X$. This is how piecewise-defined maps stay continuous.

<a id="s8"></a>
### The product topology

*How to topologize a product of spaces. The "obvious" choice is wrong for infinite products; the right one is engineered to make projections continuous.*

**Definition — product topology**

*On $\prod_{\alpha} X_\alpha$ the **product topology** is generated by the subbasis of "cylinders" $\pi_\beta^{-1}(U_\beta)$, where $\pi_\beta$ is the projection to coordinate $\beta$ and $U_\beta\subseteq X_\beta$ is open. Equivalently a basic open set is $\prod_\alpha U_\alpha$ with $U_\alpha$ open and $U_\alpha=X_\alpha$ for all but **finitely many** $\alpha$.*

> **Concept — why "finitely many" restrictions**
>
> The product topology is the **coarsest** topology making every projection $\pi_\alpha$ continuous. The finer "box topology" (allow all $U_\alpha$ to vary) destroys good theorems: with it, the diagonal map can fail to be continuous and Tychonoff's theorem fails. We almost always mean the product topology.

**Universal property**

*A map $f:Z\to\prod_\alpha X_\alpha$ is continuous **iff** each component $\pi_\alpha\circ f:Z\to X_\alpha$ is continuous. This characterizes the product topology completely and is its reason for existence.*

**Demonstration — projections are continuous and open**

1. For open $U\subseteq X_\beta$, $\pi_\beta^{-1}(U)$ is a subbasic open set by definition, so $\pi_\beta$ is continuous.
2. For a basic open box $\prod U_\alpha$, $\pi_\beta(\prod U_\alpha)=U_\beta$ (assuming nonempty), which is open — so $\pi_\beta$ is an open map.
3. A general open set is a union of boxes, and $\pi_\beta$ of a union is the union of the images, again open.

*Projections are continuous, surjective, and open — but generally not closed.*

> **Connection — the Euclidean plane**
>
> The product topology on $\mathbb R\times\mathbb R$ is exactly the standard topology on $\mathbb R^2$: open rectangles form a basis, equivalent to open disks. Products are how all the higher-dimensional and function spaces are built. Tychonoff (Section 14) is the deep theorem about infinite products.

<a id="s9"></a>
### The quotient topology

*Gluing points together. This construction builds circles from intervals, tori from squares, and the projective plane from a disk.*

**Definition — quotient topology**

*Let $q:X\to Y$ be a surjection. The **quotient topology** on $Y$ declares $V\subseteq Y$ open iff $q^{-1}(V)$ is open in $X$. It is the **finest** topology making $q$ continuous. When $Y=X/\!\sim$ and $q$ sends each point to its class, this glues equivalent points.*

**Universal property**

*A map $g:Y\to Z$ out of a quotient is continuous **iff** $g\circ q:X\to Z$ is continuous. So to define a continuous map on $X/\!\sim$ it suffices to define a continuous map on $X$ that is constant on each equivalence class.*

**Demonstration — gluing $[0,1]$ endpoints gives the circle**

1. On $[0,1]$ set $0\sim 1$ (all other points distinct). Define $f:[0,1]\to S^1$ by $f(t)=e^{2\pi i t}$; it is continuous and constant on classes.
2. By the universal property $f$ factors as a continuous bijection $\bar f:[0,1]/\!\sim\,\to S^1$.
3. $[0,1]/\!\sim$ is compact (quotient of a compact space) and $S^1$ is Hausdorff; a continuous bijection from compact to Hausdorff is a homeomorphism (Section 12).

*So $[0,1]/(0\sim 1)\cong S^1$. Gluing opposite sides of a square similarly yields the torus.*

> **Connection — duality of the four constructions**
>
> Subspace and product are **initial** constructions (coarsest topology making maps *in* continuous); quotient and disjoint-union are **final** (finest making maps *out* continuous). This duality is the categorical heart of point-set topology and the gateway to algebraic topology, where quotients build the fundamental spaces.

## Part C · Properties of spaces

<a id="s10"></a>
### Connectedness

*A space is connected if it cannot be split into two separate open pieces — the topological notion of being "all one piece."*

**Definition — connected space**

*$X$ is **disconnected** if $X=U\cup V$ with $U,V$ open, nonempty, and disjoint (a **separation**). $X$ is **connected** if no separation exists — equivalently, the only sets both open and closed ("clopen") are $\varnothing$ and $X$.*

**Demonstration — $[0,1]$ (indeed any real interval) is connected**

1. Suppose $[0,1]=A\sqcup B$ is a separation with $0\in A$. Let $c=\sup\{x:[0,x]\subseteq A\}$.
2. Since $A$ is closed in $[0,1]$, $c\in A$. Since $A$ is open, some $[0,c+\delta)\subseteq A$ unless $c=1$; that would force $c$ not to be the supremum.
3. Hence $c=1$, so $1\in A$ and $B=\varnothing$ — contradicting that $B$ is nonempty.

*The least-upper-bound property of $\mathbb R$ is exactly what powers connectedness of intervals.*

**Demonstration — continuous images of connected spaces are connected**

1. Let $f:X\to Y$ be continuous and surjective with $X$ connected. Suppose $Y=U\sqcup V$ is a separation.
2. Then $f^{-1}(U)$ and $f^{-1}(V)$ are open, disjoint, nonempty (surjectivity), and cover $X$.
3. That is a separation of $X$ — contradiction. So $Y$ has no separation; $Y$ is connected.

*Corollary — the **Intermediate Value Theorem**: a continuous $f:[a,b]\to\mathbb R$ has connected image, hence an interval, hence hits every value between $f(a)$ and $f(b)$.*

> **Connection — building bigger connected sets**
>
> If $\{A_\alpha\}$ are connected with a common point, their union is connected. The closure of a connected set is connected. Products of connected spaces are connected. These let us assemble $\mathbb R^n$ and spheres as connected from intervals.

<a id="s11"></a>
### Path-connectedness & components

*A stronger, more geometric cousin of connectedness: you can walk from any point to any other along a continuous path.*

**Definition — path-connected**

*A **path** from $a$ to $b$ is a continuous $\gamma:[0,1]\to X$ with $\gamma(0)=a,\ \gamma(1)=b$. $X$ is **path-connected** if any two points are joined by a path.*

**Theorem — path-connected $\Rightarrow$ connected**

*If $X$ were separated as $U\sqcup V$, a path from a point of $U$ to a point of $V$ would have connected image $\gamma([0,1])$ split by $U,V$ — impossible. The converse fails.*

**Demonstration — the topologist's sine curve: connected but not path-connected**

1. Let $S=\{(x,\sin\tfrac1x):0\lt x\leq 1\}$ and $T=\{0\}\times[-1,1]$. The closure of $S$ is $\overline S=S\cup T$.
2. $S$ is connected (continuous image of $(0,1]$); its closure $\overline S$ is therefore connected.
3. But no path can reach $T$ from $S$: as $x\to 0$ the curve oscillates forever, so a continuous path would have to be discontinuous at the moment it lands on $T$.

*Connectedness and path-connectedness genuinely differ. They *agree* for open subsets of $\mathbb R^n$ and for locally path-connected spaces.*

> **Concept — components**
>
> The **connected components** are the maximal connected subsets; they partition $X$ and are always closed. **Path components** partition $X$ by the "joined by a path" equivalence relation. Each path component lies inside a single component. A space is **totally disconnected** (e.g. $\mathbb Q$, the Cantor set) if every component is a single point.

> **Connection — to algebraic topology**
>
> Path components are $\pi_0(X)$, the zeroth homotopy set. Refining "is there a path?" to "are two paths deformable into each other?" gives the fundamental group $\pi_1$. Point-set connectedness is the entryway to homotopy theory.

<a id="s12"></a>
### Compactness

*The single most important property in topology — a finiteness condition that makes continuous functions tame and limits behave.*

**Definition — compact space**

*An **open cover** of $X$ is a family of open sets whose union is $X$. $X$ is **compact** if every open cover has a **finite subcover**. (For a subset, use the subspace topology, i.e. cover by sets open in $X$ and extract finitely many.)*

**Demonstration — continuous images of compact spaces are compact**

1. Let $f:X\to Y$ be continuous, $X$ compact, and $\{V_\alpha\}$ an open cover of $f(X)$.
2. Then $\{f^{-1}(V_\alpha)\}$ is an open cover of $X$; compactness gives a finite subcover $f^{-1}(V_{\alpha_1}),\dots,f^{-1}(V_{\alpha_n})$.
3. Then $V_{\alpha_1},\dots,V_{\alpha_n}$ cover $f(X)$. A finite subcover exists, so $f(X)$ is compact.

*Corollary — the **Extreme Value Theorem**: a continuous $f:X\to\mathbb R$ on compact $X$ has compact, hence closed and bounded, image, so it attains a maximum and minimum.*

**Demonstration — in a Hausdorff space, compact $\Rightarrow$ closed**

1. Let $K\subseteq X$ be compact, $X$ Hausdorff, and fix $x\notin K$. For each $y\in K$ choose disjoint open $U_y\ni x,\ V_y\ni y$.
2. The $\{V_y\}$ cover $K$; take a finite subcover $V_{y_1},\dots,V_{y_n}$. Let $U=\bigcap_{i}U_{y_i}$, a finite intersection, hence open, containing $x$.
3. $U$ is disjoint from each $V_{y_i}$, so $U\cap K=\varnothing$. Thus $x$ has a neighborhood missing $K$: $K^c$ is open, $K$ closed.

*Hausdorffness is essential: in the cofinite topology on an infinite set every subset is compact, but not all are closed.*

**Demonstration — the finite intersection property (FIP) characterization**

1. A family of sets has the FIP if every finite subfamily has nonempty intersection. Claim: $X$ is compact iff every family of closed sets with the FIP has nonempty total intersection.
2. Take complements. Closed sets $\{C_\alpha\}$ with empty intersection $\Leftrightarrow$ open sets $\{C_\alpha^c\}$ cover $X$ (De Morgan).
3. Compactness = "every cover has a finite subcover" = "if no finite subfamily of $\{C_\alpha^c\}$ covers, the whole cannot either" = "if every finite intersection of $\{C_\alpha\}$ is nonempty, the whole intersection is nonempty."

*The FIP form is the workhorse for Tychonoff's theorem and for proving nested-set theorems like Cantor's.*

**Corollary — continuous bijection from compact to Hausdorff**

*If $f:X\to Y$ is a continuous bijection, $X$ compact and $Y$ Hausdorff, then $f$ is a **homeomorphism**. Reason: $f$ maps closed (hence compact) sets to compact (hence closed) sets, so $f$ is a closed map, so $f^{-1}$ is continuous.*

<a id="s13"></a>
### Compactness in metric spaces: sequential compactness & Heine–Borel

*In metric spaces three a-priori-different notions of compactness coincide, giving the most usable theorem in analysis.*

**Three notions of compactness**

***Compact:** every open cover has a finite subcover. **Sequentially compact:** every sequence has a convergent subsequence. **Limit point compact:** every infinite subset has a limit point.*

**Theorem — equivalence in metric spaces**

*For a metric space $X$, the following are equivalent: (i) compact; (ii) sequentially compact; (iii) limit point compact; (iv) complete **and** totally bounded. (In general topological spaces these can differ.)*

**Theorem — Heine–Borel**

$$K\subseteq\mathbb R^n \text{ is compact} \iff K \text{ is closed and bounded.}$$

*This is what makes $[a,b]$ and closed balls compact, and it underlies Extreme Value and uniform-continuity theorems.*

**Demonstration — $[0,1]$ is compact (bisection)**

1. Suppose an open cover $\mathcal U$ has no finite subcover. Bisect $[0,1]$; at least one half has no finite subcover. Repeat, getting nested $I_n$ of length $2^{-n}$, each with no finite subcover.
2. By completeness the $I_n$ shrink to a single point $x=\bigcap_n I_n$. Some $U\in\mathcal U$ contains $x$, and being open it contains $(x-\varepsilon,x+\varepsilon)$.
3. For large $n$, $I_n\subseteq(x-\varepsilon,x+\varepsilon)\subseteq U$ — so $I_n$ is covered by the single set $U$, contradicting "no finite subcover."

*Bisection + completeness = compactness. The general Heine–Borel follows by taking products and closed subsets.*

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
> The cleanest proof uses the FIP characterization (Section 12). Take a family of closed sets with the FIP; extend it (using Zorn's lemma) to a maximal family still having the FIP. Maximality forces it to be "decisive" coordinatewise — its projections to each compact $X_\alpha$ have a common limit point. Assembling these coordinates produces a point in the total intersection, so the product is compact. The ultrafilter version: every ultrafilter on a product converges iff each coordinate ultrafilter converges, which holds by compactness of factors.

> **Connection — what Tychonoff buys**
>
> It produces the Hilbert cube $[0,1]^{\mathbb N}$ as a compact space (basis for Urysohn metrization, Section 19), the Stone–Čech compactification, and compactness of spaces of probability measures and of $\{0,1\}^X$ (Stone duality, compactness in logic). Almost every "big" compact space is built by Tychonoff.

<a id="s15"></a>
### Local compactness & the one-point compactification

*Many important spaces (like $\mathbb R^n$) are not compact but are compact "near each point." Such spaces can be made compact by adding a single point at infinity.*

**Definition — locally compact**

*$X$ is **locally compact** if every point has a compact neighborhood. For Hausdorff $X$ this is equivalent to: every point has a neighborhood basis of compact sets. Examples: $\mathbb R^n$, discrete spaces, all compact spaces. Non-example: $\mathbb Q$.*

**Theorem — Alexandroff one-point compactification**

$$(\mathbb R^n)^+\cong S^n,\qquad \mathbb R^+\cong S^1,\qquad \mathbb C^+\cong S^2 \ (\text{the Riemann sphere}).$$

*For locally compact Hausdorff $X$, form $X^+=X\cup\{\infty\}$. Declare $V\subseteq X^+$ open iff either $V$ is open in $X$, or $V=\{\infty\}\cup(X\setminus K)$ for some compact $K\subseteq X$. Then $X^+$ is compact Hausdorff and $X$ is dense in it.*

**Demonstration — $X^+$ is compact**

1. Let $\mathcal U$ be an open cover of $X^+$. Some $U_0\in\mathcal U$ contains $\infty$, so $U_0=\{\infty\}\cup(X\setminus K)$ with $K$ compact.
2. The remaining sets of $\mathcal U$, restricted to $X$, cover the compact set $K$; extract a finite subcover $U_1,\dots,U_n$.
3. Then $U_0,U_1,\dots,U_n$ cover all of $X^+$: $U_0$ handles $\infty$ and $X\setminus K$; the rest handle $K$.

*The point at infinity "swallows" everything outside a compact set, converting local compactness into global compactness.*

<a id="s16"></a>
### Countability axioms: first/second countable, separable, Lindelöf

*Smallness conditions that control how "big" a topology can be. They decide whether sequences suffice and whether covers can be thinned.*

**The four countability axioms**

***First countable:** every point has a countable neighborhood basis. **Second countable:** the whole topology has a countable basis. **Separable:** there is a countable dense subset. **Lindelöf:** every open cover has a countable subcover.*

**Implications**

$$\text{second countable}\ \Rightarrow\ \text{first countable},\ \text{separable, and Lindelöf}.$$

*In *metric* spaces, separable $\iff$ second countable $\iff$ Lindelöf. In general they diverge: $\mathbb R_\ell$ (lower-limit) is separable, first countable, and Lindelöf but **not** second countable.*

**Demonstration — second countable $\Rightarrow$ separable**

1. Let $\{B_n\}$ be a countable basis; discard any empty $B_n$ and pick one point $x_n\in B_n$ (countable choice).
2. Let $D=\{x_n\}$. For any nonempty open $U$, some basis element $B_n\subseteq U$ is nonempty, so $x_n\in U\cap D$.
3. Thus every open set meets $D$: $D$ is dense and countable, so $X$ is separable.

*$\mathbb R^n$ is second countable (balls with rational center and radius), hence separable ($\mathbb Q^n$ is dense) and Lindelöf.*

> **Connection — why first countable saves sequences**
>
> In a first-countable space sequences detect everything: $x\in\overline A$ iff some sequence in $A$ converges to $x$, and continuity equals sequential continuity. In spaces that are *not* first countable (e.g. $\mathbb R^{\mathbb R}$), sequences fail and you must use nets or filters (Section 20).

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

> **Concept — the staircase**
>
> Roughly $T4\Rightarrow T3\tfrac12\Rightarrow T3\Rightarrow T2\Rightarrow T1\Rightarrow T0$ (with the convention that $T3,T4$ include $T1$). Each step is strictly stronger; standard counterexamples separate consecutive levels. The cofinite topology on an infinite set is $T1$ but not $T2$.

**Demonstration — every metric space is normal (T4)**

1. Let $A,B$ be disjoint closed sets. The function $x\mapsto d(x,A)=\inf_{a\in A}d(x,a)$ is continuous and vanishes exactly on $A$.
2. Define $U=\{x: d(x,A)\lt d(x,B)\}$ and $V=\{x: d(x,B)\lt d(x,A)\}$. Both are open (continuity) and disjoint.
3. If $a\in A$ then $d(a,A)=0\lt d(a,B)$ (as $a\notin B$ closed), so $A\subseteq U$; symmetrically $B\subseteq V$.

*Metric spaces sit at the top of the staircase — they are even perfectly normal. This is why metrizability (Section 19) is so strong.*

> **Connection — Hausdorff is the workhorse**
>
> Hausdorffness guarantees *limits are unique* and that compact sets are closed (Section 12). Almost every space in analysis and geometry is assumed Hausdorff. Compact Hausdorff spaces are automatically normal — the hypothesis behind Urysohn and Tietze next.

<a id="s18"></a>
### Urysohn's lemma & the Tietze extension theorem

*In a normal space, abstract separation by open sets upgrades to separation by an honest continuous function — the bridge from topology back to analysis.*

**Theorem — Urysohn's lemma**

$$f:X\to[0,1]\quad\text{with}\quad f|_A=0\ \text{ and }\ f|_B=1.$$

*(Such an $f$ need not be $0$ only on $A$; the lemma asserts existence, not exact level sets.)*

> **Concept — how the function is built**
>
> Normality lets us insert, for every dyadic rational $r\in(0,1)$, an open set $U_r$ with $A\subseteq U_0$ and $\overline{U_r}\subseteq U_s$ whenever $r\lt s$, and $U_1=X\setminus B$. Define $f(x)=\inf\{r: x\in U_r\}$. The nested family makes $f$ continuous; it is $0$ on $A$ and $1$ on $B$. The "topological interpolation" by dyadics is the whole trick.

**Theorem — Tietze extension**

*Let $X$ be normal and $A\subseteq X$ closed. Every continuous $f:A\to[a,b]$ (or $A\to\mathbb R$) extends to a continuous $F:X\to[a,b]$ (resp. $\mathbb R$) with $F|_A=f$. Conversely, this extension property characterizes normality.*

> **Connection — Urysohn powers Tietze, and metrization**
>
> Tietze is proved by repeatedly applying Urysohn's lemma to build the extension as a uniformly convergent series of "correction" functions. Urysohn's lemma is also the key ingredient in the metrization theorem of Section 19 — it supplies the continuous functions needed to embed the space.

<a id="s19"></a>
### The Urysohn metrization theorem

*When does an abstract topology secretly come from a metric? Urysohn gives a clean sufficient condition.*

**Theorem — Urysohn metrization**

*Every **second-countable** **regular** (T3) space is **metrizable** — there exists a metric inducing its topology. (Such a space is automatically normal.)*

**Demonstration — embedding into the Hilbert cube**

1. Using second countability + normality, build a countable family of Urysohn functions $f_n:X\to[0,1]$ that separates points from closed sets.
2. Combine them into $F:X\to[0,1]^{\mathbb N}$, $F(x)=(f_1(x),f_2(x),\dots)$. Each coordinate is continuous, so $F$ is continuous; the separating property makes $F$ an embedding (homeomorphism onto its image).
3. The Hilbert cube $[0,1]^{\mathbb N}$ is metrizable (e.g. $d(x,y)=\sum_n 2^{-n}|x_n-y_n|$). A subspace of a metric space is metric, so $X$ is metrizable.

*Metrizability becomes "embeddable in a known metric space." The deep general answer is the Nagata–Smirnov theorem (metrizable iff regular with a $\sigma$-locally-finite basis).*

> **Connection — closing the loop with Part A**
>
> We started from metric spaces (Section 2), abstracted away the metric, and now recover exactly which abstract spaces were metric all along. The countability and separation axioms turn out to be precisely the fingerprints a metric leaves on a topology.

## Part D · Convergence & completeness

<a id="s20"></a>
### Nets & filters: convergence in general spaces

*Sequences are too short to see all of topology. Nets and filters are the two equivalent fixes that make convergence work in any space.*

> **Concept — why sequences fail**
>
> In a non-first-countable space a point can lie in $\overline A$ with *no* sequence in $A$ reaching it, and a discontinuous function can be sequentially continuous. The fix: index by an arbitrary directed set instead of $\mathbb N$.

**Definition — directed set & net**

*A **directed set** $(D,\leq)$ is a preorder where any two elements have an upper bound. A **net** is a function $x:D\to X$. It **converges** to $p$ if for every open $U\ni p$ there is $d_0$ with $x_d\in U$ for all $d\geq d_0$ (eventually in $U$).*

**Definition — filter & ultrafilter**

*A **filter** $\mathcal F$ is a nonempty family of nonempty sets, closed under supersets and finite intersections. It **converges** to $p$ if every neighborhood of $p$ belongs to $\mathcal F$. A maximal filter is an **ultrafilter**; for every set $S$, an ultrafilter contains $S$ or $S^c$.*

**Theorem — nets/filters characterize everything**

*$x\in\overline A$ iff some net in $A$ converges to $x$. $f$ is continuous iff it preserves convergence of all nets. **$X$ is compact iff every net has a convergent subnet, iff every ultrafilter converges.** $X$ is Hausdorff iff every net has at most one limit.*

> **Connection — the slick Tychonoff proof**
>
> The ultrafilter criterion gives Tychonoff (Section 14) in three lines: project an ultrafilter on the product to each factor, where compactness yields a limit; the product point assembled from these limits is the limit of the original ultrafilter. Filters convert hard covering arguments into clean convergence statements.

<a id="s21"></a>
### Complete metric spaces & completion

*Completeness — every Cauchy sequence converges — is a metric (not purely topological) property, yet it underwrites all of analysis.*

**Definition — Cauchy & complete**

*A sequence is **Cauchy** if $\forall\varepsilon\gt 0\ \exists N\ \forall m,n\geq N:\ d(x_m,x_n)\lt\varepsilon$. A metric space is **complete** if every Cauchy sequence converges in it. $\mathbb R^n$ is complete; $\mathbb Q$ is not.*

> **Concept — completeness is not topological**
>
> $(0,1)$ and $\mathbb R$ are homeomorphic, yet $\mathbb R$ is complete and $(0,1)$ is not. Completeness depends on the *metric*, not just the open sets. The topological shadow of completeness is "complete metrizability," and Baire's theorem (Section 22) is what survives.

**Theorem — completion**

*Every metric space $X$ embeds isometrically as a dense subset of a complete metric space $\widehat X$, unique up to isometry. Construction: $\widehat X$ = equivalence classes of Cauchy sequences, with $d(\langle x_n\rangle,\langle y_n\rangle)=\lim_n d(x_n,y_n)$. E.g. $\widehat{\mathbb Q}=\mathbb R$.*

> **Connection — fixed points & analysis**
>
> Completeness makes the **Banach fixed-point theorem** work (a contraction on a complete space has a unique fixed point), which proves existence/uniqueness for ODEs and implicit functions. Completeness of function spaces $C[a,b]$ and $L^p$ is the foundation of functional analysis.

<a id="s22"></a>
### The Baire category theorem

*A deep statement that complete spaces cannot be "small": they are not a countable union of negligible pieces. It powers many existence theorems by pure topology.*

**Definitions — nowhere dense, meager**

*A set is **nowhere dense** if its closure has empty interior. A set is **meager** (first category) if it is a countable union of nowhere dense sets; otherwise **nonmeager** (second category).*

**Theorem — Baire category**

*In a **complete metric space** (or a locally compact Hausdorff space), the intersection of countably many dense open sets is dense. Equivalently, such a space is **not** meager in itself: it is not a countable union of nowhere dense sets.*

**Demonstration — proof of the Baire category theorem**

1. Let $\{U_n\}$ be dense open in a complete metric space $X$; take any nonempty open $W$. We show $W\cap\bigcap_n U_n\neq\varnothing$.
2. Since $U_1$ is dense, $W\cap U_1\neq\varnothing$ and open: choose a closed ball $\overline{B_1}=\overline{B(x_1,r_1)}\subseteq W\cap U_1$ with $r_1\lt 1$.
3. Inductively, $U_{n+1}$ dense gives a closed ball $\overline{B_{n+1}}\subseteq B_n\cap U_{n+1}$ with $r_{n+1}\lt r_n/2$. The centers $x_n$ are Cauchy (nested shrinking balls).
4. By completeness $x_n\to x$. Each $x\in\overline{B_n}\subseteq U_n$ and $x\in\overline{B_1}\subseteq W$; hence $x\in W\cap\bigcap_n U_n$.

*Completeness (Cauchy sequences converge) + nested closed balls = the theorem. The locally compact case replaces shrinking balls with nested compact sets and the FIP.*

> **Connection — what Baire proves**
>
> Baire shows $\mathbb R$ is uncountable (points are nowhere dense, a countable union can't be all of $\mathbb R$); it yields the existence of continuous nowhere-differentiable functions, and underpins the three pillars of functional analysis — the **uniform boundedness**, **open mapping**, and **closed graph** theorems. Topology, with no extra analysis, forces these existence results.

---

*A first course in general (point-set) topology — definitions stated precisely, the central theorems proved, and every thread back to metric-space analysis and forward to algebraic and functional analysis made explicit. Read once for the architecture: metric spaces motivate open sets; open sets define continuity; the four constructions build new spaces; connectedness and compactness are the load-bearing invariants; separation and countability decide metrizability; and completeness with Baire returns us to analysis. Return to any box as a reference.*
