**English** · [中文](multivariable-vector.zh.md)

# Multivariable, *connected.*

A full third-semester course — the geometry of space, the calculus of functions on it, integration over regions and surfaces, and the great vector-calculus theorems — laid out basics → advanced. Every core result is **demonstrated** from the ground up, every symbol is defined the first time it appears, and the single thread linking gradient, Green, Stokes and Gauss is made explicit.

This expanded edition assumes you are **new to vectors and to functions of several variables**. Read slowly; every step says both *what* is done and *why* it is allowed.

[← Back to all guides](../README.md)

## Part A · Space, vectors & functions

<a id="s0"></a>
### The big picture: from one variable to many

**What this section says and why we care.** In your first calculus course you studied a *function of one variable*, written $y=f(x)$. The word **function** means a rule that takes an input number $x$ and returns exactly one output number $y$. The set of allowed inputs is the **domain**; the set of outputs is the **range**. You learned three operations on such functions: the **limit** (the value $f(x)$ heads toward as $x$ heads toward some point), the **derivative** (the instantaneous rate of change, the slope of the graph), and the **integral** (the accumulated total, the area under the graph). Multivariable calculus does these same three things, but now the input can be several numbers at once and the output can be several numbers too. That single change reorganizes the whole subject.

**Definitions of the new words.**

- A **real number** is an ordinary number on the number line; the collection of all of them is written $\mathbb R$.
- $\mathbb R^n$ ("R-n") means the collection of all *ordered lists of $n$ real numbers*. So $\mathbb R^2$ is the plane (lists $(x,y)$), and $\mathbb R^3$ is space (lists $(x,y,z)$). An element of $\mathbb R^n$ is called a **point**.
- A **scalar** is a single real number (as opposed to a list).
- A **scalar field** is a function $f:\mathbb R^n\to\mathbb R$: it eats a point of space and returns one number. Example: the temperature $f(x,y,z)$ at each location in a room.
- A **vector field** is a function $\mathbf F:\mathbb R^n\to\mathbb R^n$: it eats a point and returns a whole arrow (defined in §s1). Example: the velocity of the air at each location.
- A **parametrization** is a function that traces out a curve or surface; e.g. a rule $\mathbb R\to\mathbb R^3$ sending a time $t$ to a position draws a path.

The three operations, upgraded:

- **Differentiate** — the derivative becomes a whole *gradient vector* (a list of slopes, one per input variable; §s7), and later a matrix. It encodes the rate of change in *every* direction at once.
- **Integrate** — the integral becomes a sum over a 2-dimensional region, a 3-dimensional solid, a curve, or a surface.
- **Connect** — a family of theorems (Green, Stokes, Gauss) tie a derivative *inside* a region to values on its *boundary*, exactly as the Fundamental Theorem of Calculus did on an interval.

> **Principle — the organizing idea**
>
> Every object splits by **how many numbers go in** and **how many come out**. A **scalar field** $f:\mathbb R^n\to\mathbb R$ (temperature) has a gradient. A **vector field** $\mathbf F:\mathbb R^n\to\mathbb R^n$ (flow, force) has curl and divergence. A **parametrization** $\mathbb R\to\mathbb R^3$ or $\mathbb R^2\to\mathbb R^3$ traces a curve or surface. Knowing the type tells you which operator and which integral apply.

> **Connection — one idea you already own**
>
> The whole subject is the Fundamental Theorem of Calculus, $\int_a^b f'\,dx=f(b)-f(a)$, generalized: a derivative integrated over a region equals the function evaluated on the region's boundary. Hold that sentence; Section 27 shows all four big theorems are special cases of it.

#### What the Fundamental Theorem of Calculus says (you will need it constantly)

Because everything in this guide leans on it, here is the statement in plain words, with its terms defined. If $F$ is a function whose derivative is $f$ (we call $F$ an **antiderivative** of $f$), then the accumulated area under $f$ from $x=a$ to $x=b$ is just the change in $F$:

$$\int_a^b f(x)\,dx=F(b)-F(a),\qquad\text{where } F'(x)=f(x).$$

The symbol $\int_a^b$ means "add up over the interval from $a$ to $b$"; the $dx$ marks $x$ as the variable being summed over. The lesson — *to add up a rate of change you only need the endpoint values* — is the seed of every "big theorem" later.

#### The whole course on one line

> Vectors & space → functions of several variables → partial derivatives & the gradient → optimization → multiple integrals → vector fields → Green / Stokes / Gauss

<a id="s1"></a>
### Vectors, dot product & cross product

*A vector carries magnitude and direction. Two products turn vectors into the language of angles, projections, areas and volumes.*

**What this section says and why we care.** Before we can do calculus in space we need the algebra of space. A **vector** is the mathematical object for "a push of a certain size in a certain direction." Two special multiplications — the dot product and the cross product — let us compute angles, projections, areas, and volumes with pure arithmetic. Almost every later formula (gradients, normals, flux) is built from these two products, so we define them carefully and prove their key properties.

> **Concept — points, vectors, and the two products**
>
> A point is a location; a **vector** $\mathbf v=\langle v_1,v_2,v_3\rangle$ is a displacement. The **dot product** returns a scalar that measures alignment (and hence angle and projection); the **cross product** returns a vector perpendicular to both, whose length is the area of the parallelogram they span. Dot is about angle; cross is about area and orientation.

**Definitions — every symbol spelled out.**

- A **vector** in $\mathbb R^3$ is an ordered list of three numbers $\mathbf v=\langle v_1,v_2,v_3\rangle$, called its **components**. We print vectors in bold and use angle brackets. Geometrically it is an arrow: $v_1$ is how far it points along the $x$-direction, $v_2$ along $y$, $v_3$ along $z$. Two arrows with the same length and direction are the *same* vector regardless of where you draw them.
- The **magnitude** (or **length**, or **norm**) of $\mathbf v$, written $|\mathbf v|$, is how long the arrow is.
- **Adding** vectors adds components: $\langle a_1,a_2,a_3\rangle+\langle b_1,b_2,b_3\rangle=\langle a_1+b_1,a_2+b_2,a_3+b_3\rangle$ (tip-to-tail arrows). **Scaling** by a number $c$ multiplies each component: $c\langle a_1,a_2,a_3\rangle=\langle ca_1,ca_2,ca_3\rangle$ (stretches the arrow, reversing it if $c<0$).
- The angle $\theta$ between two vectors is the angle you would measure between the two arrows when their tails are placed together, taken in $[0,\pi]$.

**Magnitude, dot product, angle**

$$|\mathbf v|=\sqrt{v_1^2+v_2^2+v_3^2},\qquad \mathbf a\cdot\mathbf b=\sum_i a_ib_i=|\mathbf a||\mathbf b|\cos\theta$$

*$\mathbf a\cdot\mathbf b=0\iff$ perpendicular. The scalar projection of $\mathbf a$ onto $\mathbf b$ is $\dfrac{\mathbf a\cdot\mathbf b}{|\mathbf b|}$.*

Here the **dot product** $\mathbf a\cdot\mathbf b$ is defined by the middle expression $\sum_i a_ib_i = a_1b_1+a_2b_2+a_3b_3$ — multiply matching components and add. It outputs a single number (a scalar). The symbol $\theta$ is the angle between the two arrows; $\cos\theta$ is the cosine of that angle. The magnitude formula is just the Pythagorean theorem in 3D: the diagonal of a box with side lengths $|v_1|,|v_2|,|v_3|$.

**Cross product (in $\mathbb R^3$)**

$$\mathbf a\times\mathbf b=\begin{vmatrix}\mathbf i&\mathbf j&\mathbf k\\ a_1&a_2&a_3\\ b_1&b_2&b_3\end{vmatrix},\qquad |\mathbf a\times\mathbf b|=|\mathbf a||\mathbf b|\sin\theta$$

*$\mathbf a\times\mathbf b$ is perpendicular to both, direction by the right-hand rule; its length is the parallelogram area. $\mathbf a\times\mathbf b=-\,\mathbf b\times\mathbf a$.*

Definitions for this block: $\mathbf i=\langle1,0,0\rangle$, $\mathbf j=\langle0,1,0\rangle$, $\mathbf k=\langle0,0,1\rangle$ are the **standard basis vectors** (unit arrows along the three axes). The tall bars $\begin{vmatrix}\cdots\end{vmatrix}$ denote a **determinant**, a specific arithmetic recipe; expanding the $3\times3$ determinant gives the explicit formula

$$\mathbf a\times\mathbf b=\langle a_2b_3-a_3b_2,\; a_3b_1-a_1b_3,\; a_1b_2-a_2b_1\rangle.$$

The **right-hand rule**: point your right hand's fingers along $\mathbf a$, curl them toward $\mathbf b$; your thumb points along $\mathbf a\times\mathbf b$.

**Scalar triple product → volume**

$$V=\big|\,\mathbf a\cdot(\mathbf b\times\mathbf c)\,\big|=\left|\det\!\begin{pmatrix}a_1&a_2&a_3\\ b_1&b_2&b_3\\ c_1&c_2&c_3\end{pmatrix}\right|$$

*The signed volume of the parallelepiped. Zero $\iff$ the three vectors are coplanar.*

A **parallelepiped** is the 3D analogue of a parallelogram: the slanted box whose edges from one corner are $\mathbf a,\mathbf b,\mathbf c$. **Coplanar** means all three arrows lie in one common plane (then the box is flat and has zero volume).

**Demonstration — the dot product gives the angle**

We prove the geometric identity $\mathbf a\cdot\mathbf b=|\mathbf a||\mathbf b|\cos\theta$, i.e. that the component formula equals the angle formula.

1. Place $\mathbf a,\mathbf b$ tail to tail. The arrow from the tip of $\mathbf b$ to the tip of $\mathbf a$ is the vector $\mathbf a-\mathbf b$ (vector subtraction, defined above), so the three vectors form a triangle with sides $|\mathbf a|$, $|\mathbf b|$, $|\mathbf a-\mathbf b|$ and included angle $\theta$ between the first two. The **Law of Cosines** (a standard fact of plane geometry, generalizing Pythagoras) gives

   $$|\mathbf a-\mathbf b|^2=|\mathbf a|^2+|\mathbf b|^2-2|\mathbf a||\mathbf b|\cos\theta.$$
2. Expand the left side using the *component* definition of the dot product. First note two facts that follow straight from $\mathbf u\cdot\mathbf u=\sum u_i^2=|\mathbf u|^2$ and the distributive property of the sum $\sum$:

   $$|\mathbf a-\mathbf b|^2=(\mathbf a-\mathbf b)\cdot(\mathbf a-\mathbf b)=\mathbf a\cdot\mathbf a-2\,\mathbf a\cdot\mathbf b+\mathbf b\cdot\mathbf b=|\mathbf a|^2-2\,\mathbf a\cdot\mathbf b+|\mathbf b|^2.$$

   (The middle step uses that the dot product distributes over addition — true because it is a sum of products component by component — and that $\mathbf a\cdot\mathbf b=\mathbf b\cdot\mathbf a$, again because multiplication of numbers commutes.)
3. The left sides of steps 1 and 2 are the same quantity, so set the right sides equal. The terms $|\mathbf a|^2$ and $|\mathbf b|^2$ appear on both sides and cancel, leaving $-2\,\mathbf a\cdot\mathbf b=-2|\mathbf a||\mathbf b|\cos\theta$. Divide by $-2$:

   $$\mathbf a\cdot\mathbf b=|\mathbf a||\mathbf b|\cos\theta.\qquad\blacksquare$$

*Geometry (angle) and algebra (component sum) are two faces of one operation.* In particular, since $|\mathbf a||\mathbf b|>0$ for nonzero vectors, $\mathbf a\cdot\mathbf b=0$ forces $\cos\theta=0$, i.e. $\theta=90^\circ$ — that is why a zero dot product means perpendicular.

**Worked example (dot product, angle, projection).** Let $\mathbf a=\langle 1,2,2\rangle$ and $\mathbf b=\langle 2,0,-1\rangle$.

- Magnitudes: $|\mathbf a|=\sqrt{1^2+2^2+2^2}=\sqrt9=3$ and $|\mathbf b|=\sqrt{2^2+0^2+(-1)^2}=\sqrt5$.
- Dot product: $\mathbf a\cdot\mathbf b=(1)(2)+(2)(0)+(2)(-1)=2+0-2=0$. Because it is $0$, $\mathbf a$ and $\mathbf b$ are **perpendicular** ($\theta=90^\circ$), and the scalar projection $\frac{\mathbf a\cdot\mathbf b}{|\mathbf b|}=\frac{0}{\sqrt5}=0$.

**Worked example (cross product and area).** With the same $\mathbf a=\langle1,2,2\rangle$, $\mathbf b=\langle2,0,-1\rangle$, the explicit formula gives

$$\mathbf a\times\mathbf b=\langle (2)(-1)-(2)(0),\ (2)(2)-(1)(-1),\ (1)(0)-(2)(2)\rangle=\langle -2,\ 5,\ -4\rangle.$$

Its length $|\mathbf a\times\mathbf b|=\sqrt{(-2)^2+5^2+(-4)^2}=\sqrt{4+25+16}=\sqrt{45}=3\sqrt5$ is the area of the parallelogram spanned by $\mathbf a,\mathbf b$. Check against $|\mathbf a||\mathbf b|\sin\theta$: since $\theta=90^\circ$, $\sin\theta=1$, and $|\mathbf a||\mathbf b|=3\sqrt5$ — they agree. Also $\mathbf a\cdot(\mathbf a\times\mathbf b)=(1)(-2)+(2)(5)+(2)(-4)=-2+10-8=0$, confirming the cross product is perpendicular to $\mathbf a$ as claimed.

**Common pitfalls.** The dot product makes a *number*; the cross product makes a *vector* — never mix them up. The cross product is *not* commutative: $\mathbf a\times\mathbf b=-\mathbf b\times\mathbf a$ (swapping rows of the determinant flips its sign). The cross product is only defined in $\mathbb R^3$.

<a id="s2"></a>
### Lines, planes & quadric surfaces

*With vectors in hand, the basic objects of space get clean equations: a line needs a point and a direction; a plane needs a point and a normal.*

**What this section says and why we care.** A line and a plane are the simplest curved-free shapes in space, and we will meet them everywhere — tangent lines to curves, tangent planes to surfaces (§s8). The key insight is that vectors describe them with one short equation each. We define **direction vector** and **normal vector**, derive the equations, and prove the point-to-plane distance formula.

**Line through $P_0$ with direction $\mathbf v$**

$$\mathbf r(t)=\mathbf r_0+t\mathbf v,\qquad \frac{x-x_0}{v_1}=\frac{y-y_0}{v_2}=\frac{z-z_0}{v_3}$$

*Vector form (left) and symmetric form (right). A line is a point plus all scalar multiples of one direction.*

Definitions: $P_0=(x_0,y_0,z_0)$ is a known point on the line and $\mathbf r_0=\langle x_0,y_0,z_0\rangle$ is its **position vector** (the arrow from the origin to $P_0$). The **direction vector** $\mathbf v=\langle v_1,v_2,v_3\rangle$ points along the line. The **parameter** $t$ is a real number knob: as $t$ ranges over all reals, $\mathbf r(t)=\mathbf r_0+t\mathbf v$ sweeps out every point on the line, because adding $t\mathbf v$ slides $P_0$ forward (or backward) along the direction. Solving each component equation $x=x_0+tv_1$ etc. for $t$ and equating gives the symmetric form on the right.

**Plane through $P_0$ with normal $\mathbf n$**

$$\mathbf n\cdot(\mathbf r-\mathbf r_0)=0\ \Longleftrightarrow\ a(x-x_0)+b(y-y_0)+c(z-z_0)=0$$

*A point lies on the plane exactly when its displacement from $P_0$ is perpendicular to $\mathbf n=\langle a,b,c\rangle$. The normal is read straight off the coefficients.*

A **normal vector** $\mathbf n=\langle a,b,c\rangle$ is one perpendicular to the plane. The reasoning: a point $P=(x,y,z)$ lies in the plane exactly when the displacement $\mathbf r-\mathbf r_0=\langle x-x_0,y-y_0,z-z_0\rangle$ stays inside the plane, i.e. is perpendicular to $\mathbf n$. By the dot-product test of §s1 ($\mathbf a\cdot\mathbf b=0\iff$ perpendicular), that is exactly $\mathbf n\cdot(\mathbf r-\mathbf r_0)=0$. Expanding the dot product with components gives the right-hand equation. If you multiply it out to the form $ax+by+cz+d=0$, then $d=-(ax_0+by_0+cz_0)$.

**Distance from a point to a plane**

$$D=\frac{|a x_1+b y_1+c z_1+d|}{\sqrt{a^2+b^2+c^2}}$$

*It is the length of the projection of $\overrightarrow{P_0P_1}$ onto the unit normal — a dot product divided by $|\mathbf n|$.*

**Demonstration — the distance formula.** We want the shortest distance $D$ from a point $P_1=(x_1,y_1,z_1)$ to the plane $ax+by+cz+d=0$.

1. Pick any point $P_0=(x_0,y_0,z_0)$ on the plane, so it satisfies $ax_0+by_0+cz_0+d=0$, i.e. $d=-(ax_0+by_0+cz_0)$. The vector from $P_0$ to $P_1$ is $\overrightarrow{P_0P_1}=\langle x_1-x_0,\,y_1-y_0,\,z_1-z_0\rangle$.
2. The distance $D$ is the length of the *projection* of $\overrightarrow{P_0P_1}$ onto the normal $\mathbf n=\langle a,b,c\rangle$, because the shortest path from a point to a plane runs straight along the normal direction. The scalar projection (from §s1) has absolute value

   $$D=\frac{|\,\mathbf n\cdot\overrightarrow{P_0P_1}\,|}{|\mathbf n|}.$$
3. Compute the numerator: $\mathbf n\cdot\overrightarrow{P_0P_1}=a(x_1-x_0)+b(y_1-y_0)+c(z_1-z_0)=ax_1+by_1+cz_1-(ax_0+by_0+cz_0)$. Substitute $-(ax_0+by_0+cz_0)=d$ from step 1: the numerator becomes $ax_1+by_1+cz_1+d$.
4. Since $|\mathbf n|=\sqrt{a^2+b^2+c^2}$, putting steps 2–3 together yields the boxed formula. $\blacksquare$

**Worked example.** Plane $2x-y+2z=6$ (so $a=2,b=-1,c=2,d=-6$), point $P_1=(3,0,0)$. Then $|2\cdot3-1\cdot0+2\cdot0-6|=|0|=0$ — the point lies *on* the plane (check: $2\cdot3=6$). Take instead $P_1=(0,0,0)$: distance $=\frac{|0+0+0-6|}{\sqrt{4+1+4}}=\frac{6}{3}=2$. So the origin is 2 units from the plane.

> **Concept — quadric surfaces by their traces**
>
> The level-two surfaces — **ellipsoid** $\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}=1$, **paraboloid** $z=x^2+y^2$, **cone** $z^2=x^2+y^2$, **hyperboloids**, **saddle** $z=x^2-y^2$ — are best understood by their *traces*: the curves you get by slicing with coordinate planes. Set one variable constant and read off the conic that results.

A **quadric surface** is the graph of a degree-2 equation in $x,y,z$. A **trace** is the intersection curve with a plane like $z=k$ (set $z$ equal to a constant $k$ and see what equation in $x,y$ remains). For the paraboloid $z=x^2+y^2$, the trace at height $z=k$ is $x^2+y^2=k$, a circle of radius $\sqrt k$ when $k>0$ — so the surface is a stack of growing circles, a bowl. Tracing in $x=0$ gives $z=y^2$, a parabola; hence the name.

<a id="s3"></a>
### Functions of several variables; level curves & surfaces

*A function $z=f(x,y)$ assigns a height to each point of the plane — a landscape. The cleanest way to read that landscape flat is the contour map.*

**What this section says and why we care.** Now we meet the central character: a function whose input is a *point* and whose output is a *number*. Visualizing it is the first hurdle, and the two tools — the graph (a surface) and the level set (a contour map) — train the intuition you will use for gradients, optimization, and integration.

> **Concept — graph vs. level set**
>
> The **graph** of $f(x,y)$ is a surface in $\mathbb R^3$. A **level curve** $f(x,y)=k$ collects all inputs that give the same output $k$ — a contour line, like on a topographic map. For $f(x,y,z)$, $f=k$ is a **level surface**. Tight contours mean steep terrain; the gradient (Section 7) will point straight across them.

**Definitions.** A **function of two variables** $z=f(x,y)$ assigns to each input pair $(x,y)$ a single output number $z$. Its **graph** is the set of points $(x,y,f(x,y))$ in space — usually a surface sitting above the $xy$-plane, with $f(x,y)$ as the height. A **level curve** at level $k$ is the set of input points where the height equals the fixed value $k$: $\{(x,y):f(x,y)=k\}$. Plotting several level curves on the flat $xy$-plane is exactly a topographic/contour map.

**Domain, range, level set**

$$f:D\subseteq\mathbb R^n\to\mathbb R,\qquad \text{level set}=\{\,\mathbf x: f(\mathbf x)=k\,\}$$

*Always pin down the domain first: $\sqrt{}$ needs nonnegative arguments, $\ln$ needs positive, denominators must be nonzero.*

Here $D\subseteq\mathbb R^n$ is the **domain** (the symbol $\subseteq$ means "is a subset of," i.e. $D$ is part of $\mathbb R^n$): the set of inputs for which the rule makes sense. The arrow $\to\mathbb R$ says the output is a single real number. $\mathbf x$ stands for the input point $(x_1,\dots,x_n)$.

**Worked example (domain and level curves).** Let $f(x,y)=\sqrt{9-x^2-y^2}$.

- **Domain.** The square root needs a nonnegative argument: $9-x^2-y^2\ge0$, i.e. $x^2+y^2\le9$. The domain is the closed disk of radius $3$ centered at the origin.
- **Graph.** Setting $z=\sqrt{9-x^2-y^2}\ge0$ and squaring gives $x^2+y^2+z^2=9$ with $z\ge0$ — the upper half of a sphere of radius $3$.
- **Level curves.** Solve $f=k$: $\sqrt{9-x^2-y^2}=k\Rightarrow x^2+y^2=9-k^2$. For each height $k$ between $0$ and $3$ this is a circle of radius $\sqrt{9-k^2}$. As $k$ rises toward $3$ the circles shrink to a point at the top of the dome — closely spaced contours near the rim signal steep slope there.

> **Connection — back to one variable**
>
> A level curve is the multivariable cousin of "solve $f(x)=k$." Reading a function through its level sets — rather than its graph — is the visual habit that makes the gradient, Lagrange multipliers, and implicit differentiation feel natural.

<a id="s4"></a>
### Limits & continuity in several variables

*The definition of a limit looks the same, but one feature is genuinely new: in the plane you can approach a point from infinitely many directions, and the limit must agree along all of them.*

**What this section says and why we care.** A **limit** captures the value a function approaches as the input creeps toward a target. In one variable there are only two ways in (from the left, from the right). In the plane there are infinitely many paths to a point, and a genuine limit must give the *same* answer along all of them. This is the source of the most common "the limit does not exist" arguments, and it underlies the meaning of **continuity** (no jumps), which we need before differentiating.

**Limit and continuity**

$$\lim_{(x,y)\to(a,b)}f(x,y)=L:\ \forall\varepsilon>0\ \exists\delta>0,\ 0<|(x,y)-(a,b)|<\delta\Rightarrow|f-L|<\varepsilon$$

$$f \text{ continuous at }(a,b)\iff \lim_{(x,y)\to(a,b)}f(x,y)=f(a,b)$$

**Reading the symbols.** $\lim$ means "the value approached." The symbol $\forall$ means "for every" and $\exists$ means "there exists." $\varepsilon$ (epsilon) and $\delta$ (delta) are small positive distances. The phrase says: *no matter how tight a tolerance $\varepsilon$ you demand around the target output $L$, there is a small enough radius $\delta$ around the input point $(a,b)$ such that every input within distance $\delta$ (but not the point itself, hence $0<$) lands within $\varepsilon$ of $L$.* The distance $|(x,y)-(a,b)|=\sqrt{(x-a)^2+(y-b)^2}$ is the ordinary plane distance. **Continuous** at a point means the limit exists *and* equals the actual value $f(a,b)$ — the graph has no hole or jump there.

> **Principle — the two-path test**
>
> If $f$ approaches *different* values along two different paths into $(a,b)$, the limit **does not exist**. This is the standard tool: try $y=0$, then $x=0$, then $y=mx$, then $y=x^2$. One disagreement settles it.

Why the test is valid: the definition demands a single $L$ that works for *all* nearby inputs at once. Any particular path is a subset of those inputs, so if a limit $L$ existed, every path would have to approach that same $L$. Hence two paths with different limits make $L$ impossible.

**Demonstration — a limit that fails the path test**

1. Consider $f(x,y)=\dfrac{xy}{x^2+y^2}$ as $(x,y)\to(0,0)$. Approach along the $x$-axis, i.e. set $y=0$ and let $x\to0$:

   $$f(x,0)=\frac{x\cdot0}{x^2+0^2}=\frac{0}{x^2}=0\quad\Rightarrow\quad\text{limit along this path }=0.$$
2. Now approach along the diagonal line $y=x$ and let $x\to0$:

   $$f(x,x)=\frac{x\cdot x}{x^2+x^2}=\frac{x^2}{2x^2}=\frac12\quad\Rightarrow\quad\text{limit along this path }=\tfrac12.$$
3. The two paths give $0$ and $\tfrac12$. Since they disagree, by the two-path principle the limit **does not exist** — even though each single-variable slice is perfectly tame. $\blacksquare$

*Approaching from one direction is never enough; the limit must hold uniformly from all of them.*

**Worked example (a limit that does exist).** Consider $g(x,y)=\dfrac{x^2y}{x^2+y^2}$ at $(0,0)$. Here the numerator is one degree "stronger." Using $|x|\le\sqrt{x^2+y^2}$ and $|y|\le\sqrt{x^2+y^2}$ and $\frac{x^2}{x^2+y^2}\le1$:

$$\left|\frac{x^2y}{x^2+y^2}\right|=\frac{x^2}{x^2+y^2}\,|y|\le 1\cdot|y|\le\sqrt{x^2+y^2}.$$

As $(x,y)\to(0,0)$ the right side $\to0$, so $g\to0$ along *every* path. Hence the limit is $0$. (This is the squeeze/comparison idea: trap $|g|$ between $0$ and something that vanishes.)

**Common pitfall.** Agreement along the $x$-axis and $y$-axis does *not* prove a limit exists — the failing example above agrees ($0$) along both axes yet has no limit. You must check enough paths, or better, find a bound as in the worked example.

## Part B · Differential calculus of several variables

<a id="s5"></a>
### Partial derivatives

*To differentiate a function of many variables, freeze all but one and differentiate as usual. Each variable gets its own slope.*

**What this section says and why we care.** The derivative of a one-variable function $f(x)$ is its slope, $f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$ — the limit of the rise-over-run as the run $h$ shrinks. With several inputs there is no single slope; instead we get one slope per input direction, the **partial derivatives**. They are the raw material for the gradient, the chain rule, optimization, and every later differential operator.

**Definition of the partial derivative**

$$f_x(a,b)=\frac{\partial f}{\partial x}=\lim_{h\to0}\frac{f(a+h,b)-f(a,b)}{h}$$

*$f_x$ is the slope of the surface in the $x$-direction — the ordinary derivative of the single-variable slice $g(x)=f(x,b)$ with $y$ held constant.*

The notation: $f_x$ and $\frac{\partial f}{\partial x}$ both mean "the partial derivative of $f$ with respect to $x$." The rounded $\partial$ ("partial dee") distinguishes it from the ordinary $d$, reminding us other variables are held fixed. In the limit, $h$ nudges only the first input; the second stays at $b$. So $f_x$ is literally the ordinary derivative of the function $g(x)=f(x,b)$ obtained by freezing $y=b$.

> **Concept — "hold the others constant"**
>
> Computing $\partial f/\partial x$, every other variable is a constant. So $\partial_x(x^2y^3)=2xy^3$ and $\partial_y(x^2y^3)=3x^2y^2$. All single-variable rules (product, quotient, chain) apply unchanged; only your view of "what is constant" shifts.

**Worked example (all first partials).** Let $f(x,y)=x^2y^3+\sin(xy)+e^{x}$.

- $f_x$: treat $y$ as a constant. The derivative of $x^2y^3$ is $2xy^3$ (power rule on $x$, $y^3$ is a constant multiplier). The derivative of $\sin(xy)$ is $\cos(xy)\cdot y$ (chain rule: inside $xy$ has $x$-derivative $y$). The derivative of $e^x$ is $e^x$. So $f_x=2xy^3+y\cos(xy)+e^x$.
- $f_y$: treat $x$ as a constant. The derivative of $x^2y^3$ is $x^2\cdot3y^2=3x^2y^2$. The derivative of $\sin(xy)$ is $\cos(xy)\cdot x$. The derivative of $e^x$ is $0$ (no $y$). So $f_y=3x^2y^2+x\cos(xy)$.

**Worked example (numeric slope).** For $f(x,y)=x^2y^3$ at the point $(a,b)=(2,1)$: $f_x=2xy^3=2(2)(1)^3=4$ and $f_y=3x^2y^2=3(4)(1)=12$. So moving in the $+x$ direction the surface rises about $4$ units per unit step, and in $+y$ about $12$ — it is steeper in $y$ here.

> **Connection — slopes assemble into the gradient**
>
> A function of $n$ variables has $n$ first partials. Collected into a vector $\nabla f=\langle f_x,f_y,\dots\rangle$ they become the **gradient** (Section 7) — the single object that plays the role the derivative $f'(x)$ played in one variable.

<a id="s6"></a>
### The multivariable chain rule

*When variables depend on other variables, contributions flow along every path and add up. The chain rule becomes a sum over routes.*

**What this section says and why we care.** The one-variable chain rule says $\frac{d}{dt}f(g(t))=f'(g(t))g'(t)$ — to differentiate a composition, multiply the outer rate by the inner rate. When the output depends on several intermediate variables, each of which depends on the underlying variable, the changes add: you multiply along each route and sum over routes. This rule powers the directional derivative, conservative-field theory, and the proof of the Fundamental Theorem for line integrals.

**Chain rule — the two main cases**

$$\frac{df}{dt}=\frac{\partial f}{\partial x}\frac{dx}{dt}+\frac{\partial f}{\partial y}\frac{dy}{dt}\qquad\big(x=x(t),\,y=y(t)\big)$$

$$\frac{\partial f}{\partial s}=\frac{\partial f}{\partial x}\frac{\partial x}{\partial s}+\frac{\partial f}{\partial y}\frac{\partial y}{\partial s}\qquad\big(x=x(s,t),\,y=y(s,t)\big)$$

*Draw a tree: sum over every path from the output to the variable you are differentiating with respect to, multiplying along each path.*

Here $f$ depends on $x$ and $y$, and these in turn depend on $t$ (first case) or on $s,t$ (second). The term $\frac{\partial f}{\partial x}\frac{dx}{dt}$ is the change in $f$ caused by $t$ acting *through* $x$; the other term is the change *through* $y$; the total change is their sum because, to first order, independent contributions add.

**Why it holds (sketch with definitions).** A small change $\Delta t$ produces small changes $\Delta x\approx\frac{dx}{dt}\Delta t$ and $\Delta y\approx\frac{dy}{dt}\Delta t$. For a differentiable $f$ the resulting change is $\Delta f\approx f_x\,\Delta x+f_y\,\Delta y$ (this linear estimate is the total differential of §s8). Substitute and divide by $\Delta t$, then let $\Delta t\to0$ to get the displayed formula.

**Worked example.** Let $f(x,y)=x^2y$ with $x=\cos t$, $y=\sin t$. Then $f_x=2xy$, $f_y=x^2$, $\frac{dx}{dt}=-\sin t$, $\frac{dy}{dt}=\cos t$. So

$$\frac{df}{dt}=2xy(-\sin t)+x^2(\cos t)=2\cos t\sin t(-\sin t)+\cos^2t\cos t=-2\sin^2t\cos t+\cos^3t.$$

Check by substituting first: $f=\cos^2t\sin t$, and the product rule gives $\frac{df}{dt}=2\cos t(-\sin t)\sin t+\cos^2t\cos t=-2\cos t\sin^2t+\cos^3t$ — the same answer, confirming the chain rule.

> **Connection — it is a gradient dotted with a velocity**
>
> The first case is exactly $\dfrac{df}{dt}=\nabla f\cdot \mathbf r'(t)$, the gradient dotted with the velocity of the path. This single identity reappears as the directional derivative (Section 7) and as the integrand of the Fundamental Theorem for line integrals (Section 20).

**Demonstration — implicit differentiation from the chain rule**

1. Suppose an equation $F(x,y)=0$ secretly defines $y$ as a function of $x$ (a **level curve**, §s3). Differentiate both sides with respect to $x$, treating $y=y(x)$ and using the chain rule (the path through $x$ directly plus the path through $y$):

   $$\frac{\partial F}{\partial x}\frac{dx}{dx}+\frac{\partial F}{\partial y}\frac{dy}{dx}=\frac{d}{dx}(0)=0.$$
2. Since $\frac{dx}{dx}=1$, this is $F_x+F_y\frac{dy}{dx}=0$. Solve for the slope (allowed when $F_y\neq0$, since we then divide by it):

   $$\frac{dy}{dx}=-\frac{F_x}{F_y}\qquad(F_y\neq0).\qquad\blacksquare$$

**Worked example.** The circle $x^2+y^2-25=0$ has $F_x=2x$, $F_y=2y$, so $\frac{dy}{dx}=-\frac{2x}{2y}=-\frac{x}{y}$. At $(3,4)$ the slope is $-\frac34$ — matching the tangent to a circle being perpendicular to the radius.

*The mysterious implicit-differentiation rule of Calc I is just the chain rule applied to a level curve.*

<a id="s7"></a>
### Directional derivatives & the gradient

Partials give slopes along the axes. The directional derivative gives the slope along *any* direction — and the gradient packages them all.

**What this section says and why we care.** A partial derivative only tells you the slope along $x$ or along $y$. But you can walk in any direction. The **directional derivative** is the slope along an arbitrary direction, and remarkably it is computed by a single dot product with the **gradient** — the vector of all partials. The gradient then turns out to point uphill fastest and to be perpendicular to level sets, two facts that organize optimization, tangent planes, and Lagrange multipliers.

**Gradient & directional derivative**

$$\nabla f=\Big\langle \frac{\partial f}{\partial x},\frac{\partial f}{\partial y},\frac{\partial f}{\partial z}\Big\rangle,\qquad D_{\mathbf u}f=\nabla f\cdot\mathbf u\quad(|\mathbf u|=1)$$

*The rate of change of $f$ as you step in unit direction $\mathbf u$ is the gradient projected onto $\mathbf u$.*

Definitions: the **gradient** $\nabla f$ (read "del f" or "grad f") is the vector whose components are the partial derivatives. A **unit vector** $\mathbf u$ is a vector of length $1$ ($|\mathbf u|=1$); it specifies a pure direction. The **directional derivative** $D_{\mathbf u}f$ is the instantaneous rate of change of $f$ as you move from the point in the direction $\mathbf u$ at unit speed. The formula $D_{\mathbf u}f=\nabla f\cdot\mathbf u$ comes directly from the chain rule of §s6: if $\mathbf r(t)$ moves through the point with velocity $\mathbf u$, then $\frac{d}{dt}f(\mathbf r(t))=\nabla f\cdot\mathbf u$.

> **Concept — three facts that make the gradient indispensable**
>
> (1) $\nabla f$ points in the direction of **steepest ascent**; (2) its magnitude $|\nabla f|$ is that steepest slope; (3) $\nabla f$ is **perpendicular to the level set** through the point. Together these turn a list of partials into a geometric arrow.

**Demonstration — the gradient is the direction of steepest ascent**

1. The slope in unit direction $\mathbf u$ is $D_{\mathbf u}f=\nabla f\cdot\mathbf u$ (definition above).
2. Write the dot product with the angle $\theta$ between $\nabla f$ and $\mathbf u$, using the angle form of the dot product (§s1) and $|\mathbf u|=1$:

   $$D_{\mathbf u}f=|\nabla f|\,|\mathbf u|\cos\theta=|\nabla f|\cos\theta.$$
3. As $\mathbf u$ varies, only $\cos\theta$ changes, and $\cos\theta$ ranges over $[-1,1]$. It is largest, $\cos\theta=1$, exactly when $\theta=0$ — i.e. $\mathbf u$ points the same way as $\nabla f$. Then $D_{\mathbf u}f=|\nabla f|$, the steepest ascent. The smallest, $\cos\theta=-1$ at $\theta=180^\circ$, gives $-|\nabla f|$ (steepest descent), and $\theta=90^\circ$ gives $0$. $\blacksquare$

*Hence the gradient points uphill fastest, with steepness $|\nabla f|$ — and the zero-rate directions are exactly along the level set, proving $\nabla f\perp$ level set.*

**Worked example.** Let $f(x,y)=x^2+y^2$ at the point $(3,4)$. Then $\nabla f=\langle 2x,2y\rangle=\langle 6,8\rangle$, with $|\nabla f|=\sqrt{36+64}=10$. The direction of steepest ascent is $\frac{1}{10}\langle6,8\rangle=\langle0.6,0.8\rangle$, and the steepest slope is $10$. The directional derivative toward, say, $\mathbf u=\langle1,0\rangle$ (the $+x$ direction) is $\nabla f\cdot\mathbf u=6$. Note $\nabla f=\langle6,8\rangle$ points radially outward — perpendicular to the level circle $x^2+y^2=25$ through $(3,4)$, as the perpendicularity claim predicts.

> **Connection — perpendicular to the level set**
>
> Along a level curve $f$ does not change, so $D_{\mathbf u}f=0$ for $\mathbf u$ tangent to it, forcing $\nabla f\perp\mathbf u$. This is why $\nabla F$ is the normal to a surface $F=k$ (Section 8) and why gradients align at a constrained optimum (Lagrange, Section 11).

<a id="s8"></a>
### Tangent planes, linear approximation & differentials

*Zoom into a smooth surface and it looks flat. That flat approximation is the tangent plane — the multivariable version of the tangent line.*

**What this section says and why we care.** In one variable, near a point the curve is well approximated by its tangent line, $L(x)=f(a)+f'(a)(x-a)$. In two variables the curve becomes a surface and the tangent *line* becomes a tangent *plane*. This linear approximation is how we estimate function values, propagate measurement errors, and define what "differentiable" should mean in higher dimensions.

**Tangent plane & linearization of $z=f(x,y)$**

$$z=f(a,b)+f_x(a,b)(x-a)+f_y(a,b)(y-b)$$

$$L(x,y)=f(a,b)+\nabla f(a,b)\cdot\langle x-a,\,y-b\rangle$$

*Same shape as $y=f(a)+f'(a)(x-a)$: value plus slope times displacement, now with the gradient supplying the slope in both directions.*

Reasoning: the plane must pass through $(a,b,f(a,b))$ and have the right slopes. Holding $y=b$, the slice must have slope $f_x(a,b)$ in $x$; holding $x=a$, slope $f_y(a,b)$ in $y$. The unique plane meeting these conditions is the displayed one. The two displayed forms are identical because the dot product $\nabla f\cdot\langle x-a,y-b\rangle=f_x(x-a)+f_y(y-b)$.

**Tangent plane to a level surface $F(x,y,z)=k$**

$$\nabla F(P)\cdot\langle x-x_0,\,y-y_0,\,z-z_0\rangle=0$$

*Because $\nabla F$ is the surface normal (Section 7), the tangent plane is "point + plane perpendicular to the gradient."*

This is just the plane equation of §s2 with normal $\mathbf n=\nabla F(P)$, using that the gradient is perpendicular to the level surface (§s7).

**Total differential**

$$df=f_x\,dx+f_y\,dy+f_z\,dz$$

*A first-order estimate of how the output changes for small input nudges — the workhorse for error propagation.*

The **differentials** $dx,dy,dz$ stand for small changes in the inputs; $df$ is the resulting estimated change in the output. The formula simply says each input's change contributes its slope times its size, and these add — the same linear idea as the tangent plane.

**Worked example (linear approximation).** Estimate $\sqrt{(3.02)^2+(3.97)^2}$. Let $f(x,y)=\sqrt{x^2+y^2}$ at $(a,b)=(3,4)$, where $f=5$. Then $f_x=\frac{x}{\sqrt{x^2+y^2}}=\frac{3}{5}$ and $f_y=\frac{y}{\sqrt{x^2+y^2}}=\frac{4}{5}$. With $\Delta x=0.02$, $\Delta y=-0.03$:

$$f\approx 5+\tfrac35(0.02)+\tfrac45(-0.03)=5+0.012-0.024=4.988.$$

The exact value is $\sqrt{9.1204+15.7609}=\sqrt{24.8813}\approx4.98812$ — the linear estimate is accurate to four decimals.

> **Connection — differentiability is more than partials existing**
>
> A function is **differentiable** at a point if the tangent plane genuinely approximates it (the error vanishes faster than the distance). Having both partials is *not* enough; but if the partials are *continuous* near the point, differentiability is guaranteed — the practical test you will almost always use.

<a id="s9"></a>
### Higher-order partials & Clairaut's theorem

*Differentiate twice and the order can matter — except, remarkably, it usually doesn't. The mixed partials are equal whenever they are continuous.*

**What this section says and why we care.** You can differentiate a partial derivative again, producing **second-order partials**. The surprising and deeply useful fact (**Clairaut's theorem**) is that the two **mixed** partials — differentiate by $x$ then $y$, versus $y$ then $x$ — come out equal whenever they are continuous. This single symmetry is the hidden reason behind exact differentials, conservative fields (§s20), and the vanishing-curl identity (§s22).

**Second partials & Clairaut's theorem**

$$f_{xx}=\partial_x\partial_x f,\quad f_{xy}=\partial_y\partial_x f,\quad f_{yx}=\partial_x\partial_y f$$

$$\text{If }f_{xy},f_{yx}\text{ are continuous near }(a,b),\ \text{then } f_{xy}(a,b)=f_{yx}(a,b).$$

Notation note: $f_{xy}$ means "first $\partial_x$, then $\partial_y$" reading the subscripts left to right (the operator notation $\partial_y\partial_x$ applies right to left, hence the same thing). The **Mean Value Theorem (MVT)** used below is the one-variable fact: for a differentiable $g$, the change $g(p)-g(q)$ equals $g'(c)(p-q)$ for some point $c$ strictly between $q$ and $p$ — the average rate is achieved as an instantaneous rate somewhere inside.

**Demonstration — why $f_{xy}=f_{yx}$**

1. Form the **second difference** that nudges both variables, at increments $h,k$:

   $$\Delta=\frac{f(a+h,b+k)-f(a+h,b)-f(a,b+k)+f(a,b)}{hk}.$$
2. Group the numerator as a difference in $x$ first. Define $g(x)=f(x,b+k)-f(x,b)$; then the numerator is $g(a+h)-g(a)$. By the MVT there is $\xi$ between $a$ and $a+h$ with $g(a+h)-g(a)=h\,g'(\xi)=h\big(f_x(\xi,b+k)-f_x(\xi,b)\big)$.
3. Apply the MVT again, now in $y$, to the function $y\mapsto f_x(\xi,y)$ between $b$ and $b+k$: there is $\eta$ with $f_x(\xi,b+k)-f_x(\xi,b)=k\,f_{xy}(\xi,\eta)$. Substituting into step 2 and dividing by $hk$ gives $\Delta=f_{xy}(\xi,\eta)$.
4. By symmetry — grouping the numerator as a difference in $y$ first and repeating — we also get $\Delta=f_{yx}(\xi',\eta')$ for some $(\xi',\eta')$ near $(a,b)$.
5. Let $h,k\to0$. Then $(\xi,\eta)\to(a,b)$ and $(\xi',\eta')\to(a,b)$ (they are trapped between the corners). Using that $f_{xy}$ and $f_{yx}$ are *continuous* (so their values at the moving points approach their values at $(a,b)$):

   $$f_{xy}(a,b)=\lim_{h,k\to0}\Delta=f_{yx}(a,b).\qquad\blacksquare$$

**Worked example.** Let $f(x,y)=x^3y^2+\sin x$. Then $f_x=3x^2y^2+\cos x$, so $f_{xy}=\partial_y(3x^2y^2+\cos x)=6x^2y$. Going the other way, $f_y=2x^3y$, so $f_{yx}=\partial_x(2x^3y)=6x^2y$. They match, as Clairaut guarantees.

*Equal mixed partials is exactly the condition behind exact differentials and conservative fields (Section 20).*

<a id="s10"></a>
### Local extrema & the second-derivative test

*Hills and valleys occur where the surface is level — where the gradient vanishes. A second-derivative test sorts peaks from passes.*

**What this section says and why we care.** To find the highest or lowest points of a surface, first locate the flat spots (where the gradient is zero — the multivariable analogue of $f'=0$). But a flat spot can be a peak, a valley, or a **saddle** (up one way, down another). The **second-derivative test** uses a single number $D$ built from second partials to classify them.

**Critical points & the second-derivative test**

$$\nabla f=\mathbf 0\ \Rightarrow\ \text{critical point};\qquad D=f_{xx}f_{yy}-f_{xy}^{\,2}$$

*$D>0,\ f_{xx}>0\Rightarrow$ local min; $D>0,\ f_{xx}<0\Rightarrow$ local max; $D<0\Rightarrow$ saddle; $D=0\Rightarrow$ inconclusive.*

Definitions: a **critical point** is an input where all first partials vanish, i.e. $\nabla f=\mathbf 0=\langle0,0\rangle$; the surface is locally level there. A **local minimum** (resp. **maximum**) is a point lower (higher) than all nearby points. A **saddle point** is a critical point that is neither — it is a minimum along one direction and a maximum along another, like a mountain pass. The discriminant $D$ is the number defined above; the rules classify the critical point by the signs of $D$ and $f_{xx}$.

> **Concept — why $D$ is a determinant**
>
> $D$ is the determinant of the **Hessian** $\begin{pmatrix}f_{xx}&f_{xy}\\ f_{xy}&f_{yy}\end{pmatrix}$. Near a critical point $f$ looks like a quadratic form; the Hessian's eigenvalues give the curvatures along the principal axes. Both positive → bowl (min); both negative → dome (max); opposite signs → saddle. The sign of $D$ (product of eigenvalues) and of $f_{xx}$ recover exactly those cases.

The **Hessian** is the matrix of second partials; a **determinant** is the same area-recipe from §s1 ($ad-bc$ for a $2\times2$); **eigenvalues** are the curvatures along the surface's natural axes (you need only the rule, not their computation, here). Their product equals the determinant $D$: two same-sign curvatures give $D>0$ (a bowl or dome), opposite signs give $D<0$ (a saddle).

**Worked example.** Classify the critical points of $f(x,y)=x^3-3x+y^2$.

1. Partials: $f_x=3x^2-3$, $f_y=2y$. Set both to zero: $3x^2-3=0\Rightarrow x=\pm1$; $2y=0\Rightarrow y=0$. Critical points: $(1,0)$ and $(-1,0)$.
2. Second partials: $f_{xx}=6x$, $f_{yy}=2$, $f_{xy}=0$. So $D=f_{xx}f_{yy}-f_{xy}^2=(6x)(2)-0=12x$.
3. At $(1,0)$: $D=12>0$ and $f_{xx}=6>0$ → **local minimum**. At $(-1,0)$: $D=-12<0$ → **saddle point**.

> **Connection — Calc I, upgraded**
>
> In one variable: $f'=0$ then check $f''$. Here $\nabla f=\mathbf 0$ replaces $f'=0$, and the Hessian determinant replaces the single $f''$. The logic — find flat spots, then probe curvature — is identical.

<a id="s11"></a>
### Lagrange multipliers (constrained optimization)

*To optimize $f$ subject to a constraint $g=c$, you cannot just set $\nabla f=\mathbf 0$. The constraint pins you to a curve or surface — and the answer is where the gradients line up.*

**What this section says and why we care.** Often you want the largest or smallest value of $f$ but you are not free to roam — you must stay on a constraint, like a fixed budget or a curve. Setting $\nabla f=\mathbf0$ is wrong because the unconstrained peak may be off-limits. The method of **Lagrange multipliers** says the constrained optimum occurs where the gradient of $f$ is parallel to the gradient of the constraint.

**Lagrange condition**

$$\nabla f=\lambda\,\nabla g,\qquad g(x,y,\dots)=c$$

*Solve this system for the variables and the multiplier $\lambda$. With two constraints: $\nabla f=\lambda\nabla g+\mu\nabla h$.*

Definitions: the **constraint** is an equation $g(x,y,\dots)=c$ restricting inputs to a level set of $g$ (§s3). The number $\lambda$ (lambda) is the **Lagrange multiplier**, an unknown scalar. The condition says $\nabla f$ is a scalar multiple of $\nabla g$, i.e. the two arrows are parallel.

**Demonstration — why the gradients must be parallel**

1. The constraint $g=c$ confines you to its level set (a curve in 2D, a surface in 3D). Take any smooth path $\mathbf r(t)$ lying entirely in that set and passing through a constrained extremum at time $t_0$.
2. Along the path, the values $f(\mathbf r(t))$ form an ordinary one-variable function with an extremum at $t_0$; hence its derivative vanishes there. By the chain rule (§s6, as a gradient dotted with velocity):

   $$\frac{d}{dt}f(\mathbf r(t))\Big|_{t_0}=\nabla f\cdot\mathbf r'(t_0)=0.$$
3. So $\nabla f\perp\mathbf r'(t_0)$. This holds for *every* path through the point in the constraint set, and these velocities $\mathbf r'(t_0)$ sweep out all tangent directions to the set. Therefore $\nabla f$ is perpendicular to the whole constraint set. But $\nabla g$ is also perpendicular to that set, because the set is a level set of $g$ and the gradient is normal to its level sets (§s7).
4. Two vectors that are both perpendicular to the same curve/surface point along the same line, hence are parallel; parallel means one is a scalar multiple of the other:

   $$\nabla f=\lambda\,\nabla g.\qquad\blacksquare$$

**Worked example.** Maximize $f(x,y)=xy$ on the constraint $g(x,y)=x^2+y^2=8$.

1. $\nabla f=\langle y,x\rangle$, $\nabla g=\langle2x,2y\rangle$. The condition $\nabla f=\lambda\nabla g$ gives $y=2\lambda x$ and $x=2\lambda y$.
2. Substitute the first into the second: $x=2\lambda(2\lambda x)=4\lambda^2 x$. If $x\neq0$, then $4\lambda^2=1$, so $\lambda=\pm\tfrac12$. Then $y=2\lambda x=\pm x$.
3. Use the constraint $x^2+y^2=8$ with $y=\pm x$: $2x^2=8\Rightarrow x^2=4\Rightarrow x=\pm2$, $y=\pm2$. The candidate points are $(\pm2,\pm2)$.
4. Evaluate $f=xy$: it is $+4$ at $(2,2)$ and $(-2,-2)$, and $-4$ at $(2,-2)$ and $(-2,2)$. So the maximum of $xy$ on the circle is $\boxed{4}$ (and the minimum is $-4$).

*At a constrained optimum the level curves of $f$ are tangent to the constraint — they kiss, sharing a normal. The multiplier $\lambda$ measures the sensitivity of the optimum to the constraint level $c$.*

## Part C · Multiple integrals

<a id="s12"></a>
### Double integrals over rectangles & general regions

*A double integral adds up a function over a 2D region — the volume under a surface. Fubini's theorem lets you compute it one variable at a time.*

**What this section says and why we care.** A single integral $\int_a^b f\,dx$ accumulates $f$ over an interval (the area under a curve). A **double integral** $\iint_R f\,dA$ accumulates $f$ over a flat region (the volume under a surface). The practical engine is **Fubini's theorem**: you compute a double integral as two ordinary integrals nested inside each other — integrate one variable at a time.

**Definition & Fubini's theorem**

$$\iint_R f\,dA=\lim_{\|P\|\to0}\sum_{i,j} f(x_i^*,y_j^*)\,\Delta A=\int_a^b\!\!\int_c^d f(x,y)\,dy\,dx$$

*Over a rectangle, for $f$ continuous (more generally integrable) on it, the order of integration is free. The double integral is a limit of Riemann sums of little boxes $f\cdot\Delta A$.*

Definitions: $R$ is the region of integration; $dA$ is the **area element** (a tiny patch of area). A **partition** $P$ chops $R$ into little rectangles of area $\Delta A$; $(x_i^*,y_j^*)$ is a sample point in the $(i,j)$ rectangle; $\|P\|$ is the size of the largest piece. The middle expression is a **Riemann sum** — add up height-times-area $f\cdot\Delta A$ over all pieces — and the integral is its limit as the pieces shrink. **Fubini's theorem** says this 2D limit equals the iterated single integral on the right: integrate over $y$ first (inner), then over $x$ (outer).

**General (Type I / Type II) regions**

$$\iint_D f\,dA=\int_a^b\!\!\int_{g_1(x)}^{g_2(x)} f\,dy\,dx=\int_c^d\!\!\int_{h_1(y)}^{h_2(y)} f\,dx\,dy$$

*The inner limits describe the region (functions); the outer limits are constants. Sketch the region first — it dictates the bounds and often which order is tractable.*

A **Type I region** sits between two curves $y=g_1(x)$ (bottom) and $y=g_2(x)$ (top) over an $x$-interval $[a,b]$; a **Type II region** sits between $x=h_1(y)$ and $x=h_2(y)$ over a $y$-interval $[c,d]$. The inner integral's limits are functions (they describe the moving edges); the outer limits are constants.

**Worked example.** Compute $\iint_D x\,dA$ where $D$ is the triangle with vertices $(0,0),(1,0),(1,1)$.

1. Describe $D$ as Type I: $x$ runs $0$ to $1$; for fixed $x$, $y$ runs from the bottom edge $y=0$ up to the line $y=x$. So $\iint_D x\,dA=\int_0^1\!\int_0^{x} x\,dy\,dx$.
2. Inner integral (treat $x$ as constant): $\int_0^x x\,dy=x\,[y]_0^x=x\cdot x=x^2$.
3. Outer integral: $\int_0^1 x^2\,dx=\big[\tfrac{x^3}{3}\big]_0^1=\tfrac13$.

So $\iint_D x\,dA=\tfrac13$.

> **Principle — reversing the order of integration**
>
> An iterated integral that is impossible in one order can be elementary in the other. The technique: from the bounds, reconstruct the *region*, then re-describe it with the variables swapped. The region is the invariant; the bounds are just one way of slicing it.

**Worked example (order reversal).** Consider $\int_0^1\!\int_x^1 e^{y^2}\,dy\,dx$. The inner $\int e^{y^2}dy$ has no elementary antiderivative — stuck. Reconstruct the region: $0\le x\le1$ and $x\le y\le1$, i.e. the triangle $0\le x\le y\le1$. Re-slice with $y$ outer: $0\le y\le1$ and $0\le x\le y$:

$$\int_0^1\!\int_0^{y} e^{y^2}\,dx\,dy=\int_0^1 e^{y^2}\,[x]_0^{y}\,dy=\int_0^1 y\,e^{y^2}\,dy.$$

Now substitute $u=y^2$, $du=2y\,dy$: $=\tfrac12\int_0^1 e^u\,du=\tfrac12(e-1)$. The reversal turned an impossible integral into an elementary one.

> **Connection — iterating single integrals**
>
> A double integral is just a definite integral whose integrand is itself a definite integral. Everything you know about $\int$ carries over; the only new skill is translating a 2D region into nested limits.

<a id="s13"></a>
### Double integrals in polar coordinates

*Circles and disks are nightmares in $x,y$ but trivial in $r,\theta$. The only catch — and it is the heart of the matter — is the area element gains a factor of $r$.*

**What this section says and why we care.** **Polar coordinates** describe a point by its distance $r$ from the origin and the angle $\theta$ it makes with the positive $x$-axis. Round regions become simple rectangles in $r,\theta$. The crucial subtlety is that the area element is $r\,dr\,d\theta$, *not* $dr\,d\theta$ — the extra $r$ is the most-forgotten factor in the subject, so we derive it.

**Polar double integral**

$$x=r\cos\theta,\quad y=r\sin\theta,\qquad \iint_D f\,dA=\iint_D f(r\cos\theta,r\sin\theta)\,\underbrace{r\,dr\,d\theta}_{dA}$$

*The $r$ is not optional — forgetting it is the classic error. It is the Jacobian of the polar map (Section 16).*

Definitions: $r\ge0$ is the distance from the origin, $\theta$ the angle from the $+x$-axis. The conversion $x=r\cos\theta,\,y=r\sin\theta$ comes from right-triangle trigonometry. To integrate, substitute these into $f$ and replace $dA$ by $r\,dr\,d\theta$.

**Demonstration — why $dA=r\,dr\,d\theta$**

1. Partition the region with rays $\theta=\text{const}$ and circles $r=\text{const}$. A typical "polar rectangle" spans a small angle $\Delta\theta$ and a small radial thickness $\Delta r$, located at radius $r$.
2. Its two curved sides are circular arcs. Arc length equals radius times angle, so the outer arc has length $r\,\Delta\theta$; the radial side (a straight piece) has length $\Delta r$. For small increments the patch is nearly a rectangle with these two side lengths:

   $$\Delta A\approx(\text{arc length})\times(\text{radial width})=(r\,\Delta\theta)(\Delta r).$$
3. Exactly: the patch is the region between radii $r$ and $r+\Delta r$ subtending angle $\Delta\theta$. The area of a circular sector of radius $\rho$ and angle $\Delta\theta$ is $\tfrac12\rho^2\Delta\theta$, so the ring slice has area

   $$\Delta A=\tfrac12\big((r+\Delta r)^2-r^2\big)\Delta\theta=\tfrac12\big(2r\,\Delta r+(\Delta r)^2\big)\Delta\theta=\big(r+\tfrac12\Delta r\big)\Delta r\,\Delta\theta.$$
4. Let $\Delta r,\Delta\theta\to0$; the $\tfrac12\Delta r$ term vanishes, leaving the area element $dA=r\,dr\,d\theta$. $\blacksquare$

*Patches far from the origin are wider for the same $\Delta\theta$; the factor $r$ accounts for that fanning out.*

**Worked example.** Compute $\iint_D (x^2+y^2)\,dA$ over the disk $D:\,x^2+y^2\le4$. In polar, $x^2+y^2=r^2$, the disk is $0\le r\le2$, $0\le\theta\le2\pi$, and $dA=r\,dr\,d\theta$:

$$\int_0^{2\pi}\!\int_0^2 r^2\cdot r\,dr\,d\theta=\int_0^{2\pi}\!\int_0^2 r^3\,dr\,d\theta=\int_0^{2\pi}\Big[\tfrac{r^4}{4}\Big]_0^2 d\theta=\int_0^{2\pi}4\,d\theta=8\pi.$$

Forgetting the extra $r$ would have given $\int_0^2 r^2\,dr=\tfrac83$ inside and a wrong final answer — the pitfall the box warns about.

> **Connection — the Gaussian integral**
>
> Polar coordinates crack $\int_{-\infty}^{\infty}e^{-x^2}dx=\sqrt\pi$: square it into a double integral over the plane, convert to polar, and the stubborn $e^{-r^2}\,r\,dr$ integrates by elementary substitution — the $r$ from $dA$ is exactly what makes it work.

<a id="s14"></a>
### Triple integrals

*One more dimension: integrate over a solid. The picture and the bookkeeping extend directly from double integrals.*

**What this section says and why we care.** A **triple integral** $\iiint_E f\,dV$ accumulates $f$ over a 3D solid $E$. With $f=1$ it computes the solid's volume; with $f$ a density it computes mass. The only genuinely new skill versus double integrals is describing a solid with three nested limits.

**Triple integral & volume**

$$\iiint_E f\,dV=\int\!\!\int\!\!\int f(x,y,z)\,dz\,dy\,dx,\qquad \text{Vol}(E)=\iiint_E 1\,dV$$

*Innermost limits may depend on the two outer variables; the middle on the outermost; the outermost are constants.*

Here $dV$ is the **volume element** (a tiny box of volume), $E$ the solid. As with Fubini in §s12, the triple integral is computed as three nested ordinary integrals.

> **Principle — set up by projecting and slicing**
>
> Describe the solid as: a 2D **shadow** $D$ in one coordinate plane, with $z$ running between a lower surface $z=u_1(x,y)$ and an upper surface $z=u_2(x,y)$. Integrate $z$ first (a single integral for each $(x,y)$), then handle $D$ as a double integral — possibly in polar.

**Worked example (volume).** Find the volume of the solid $E$ under the plane $z=x+y$, above $z=0$, over the unit square $0\le x\le1,\,0\le y\le1$.

1. For each $(x,y)$ in the square, $z$ runs from $0$ to $x+y$. So $\text{Vol}=\int_0^1\!\int_0^1\!\int_0^{x+y}1\,dz\,dy\,dx$.
2. Innermost: $\int_0^{x+y}dz=x+y$.
3. Middle (over $y$): $\int_0^1 (x+y)\,dy=\big[xy+\tfrac{y^2}{2}\big]_0^1=x+\tfrac12$.
4. Outer (over $x$): $\int_0^1\big(x+\tfrac12\big)dx=\big[\tfrac{x^2}{2}+\tfrac{x}{2}\big]_0^1=\tfrac12+\tfrac12=1$.

The volume is $1$.

> **Connection — same skill, more limits**
>
> A triple integral is a double integral of a single integral. Mastery is entirely about translating a 3D solid into nested bounds — the calculus is the elementary integration you already do.

<a id="s15"></a>
### Cylindrical & spherical coordinates

*Solids with axial or central symmetry beg for coordinates that respect that symmetry. Each brings its own volume element.*

**What this section says and why we care.** Just as polar coordinates simplify round regions in the plane, **cylindrical** and **spherical** coordinates simplify solids in space. Cylindrical = polar in the floor plus ordinary height; spherical = distance-from-origin plus two angles. Each carries its own volume element, which we derive.

**Cylindrical coordinates**

$$x=r\cos\theta,\ y=r\sin\theta,\ z=z,\qquad dV=r\,dz\,dr\,d\theta$$

*Polar in the $xy$-plane, ordinary $z$ on top. Ideal for cylinders, cones, paraboloids.*

These reuse polar $(r,\theta)$ for the floor and keep $z$ as height. The volume element inherits the polar $r$ from §s13 (the $z$ direction contributes a plain $dz$): $dV=(r\,dr\,d\theta)\,dz$.

**Spherical coordinates**

$$x=\rho\sin\phi\cos\theta,\ y=\rho\sin\phi\sin\theta,\ z=\rho\cos\phi,\qquad dV=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$$

*$\rho\ge0$ is distance from origin, $\phi\in[0,\pi]$ the angle from the $+z$-axis, $\theta\in[0,2\pi)$ the longitude. Ideal for spheres and cones.*

Definitions: $\rho$ (rho) is the straight-line distance to the origin; $\phi$ (phi) is the **polar angle** measured down from the north pole ($+z$-axis); $\theta$ is the **azimuth** (longitude) in the $xy$-plane.

**Demonstration — the spherical volume element $\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$**

1. Increase $\rho$ by $d\rho$ with the angles fixed: the point moves straight outward, tracing a radial edge of length $d\rho$.
2. Increase $\phi$ by $d\phi$ with $\rho,\theta$ fixed: the point moves along a circle of radius $\rho$ (a meridian through the poles), so it traces an arc of length (radius × angle) $=\rho\,d\phi$.
3. Increase $\theta$ by $d\theta$ with $\rho,\phi$ fixed: the point moves along a circle of latitude. Its radius is the distance from the $z$-axis, which is $\rho\sin\phi$ (the horizontal leg of the right triangle with hypotenuse $\rho$ and angle $\phi$ from the vertical). So this arc has length $\rho\sin\phi\,d\theta$.
4. The three edges are mutually perpendicular (radial, along-meridian, along-latitude), so the little box's volume is the product of the three lengths:

   $$dV=(d\rho)(\rho\,d\phi)(\rho\sin\phi\,d\theta)=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta.\qquad\blacksquare$$

*The $\rho^2$ is the surface-area growth of spheres; the $\sin\phi$ is the shrinking of latitude circles toward the poles. Both fall straight out of the Jacobian (Section 16).*

**Worked example (volume of a sphere).** The ball of radius $a$ is $0\le\rho\le a$, $0\le\phi\le\pi$, $0\le\theta\le2\pi$:

$$\text{Vol}=\int_0^{2\pi}\!\int_0^{\pi}\!\int_0^{a}\rho^2\sin\phi\,d\rho\,d\phi\,d\theta=\Big(\int_0^a\rho^2d\rho\Big)\Big(\int_0^\pi\sin\phi\,d\phi\Big)\Big(\int_0^{2\pi}d\theta\Big).$$

Each factor: $\int_0^a\rho^2d\rho=\tfrac{a^3}{3}$; $\int_0^\pi\sin\phi\,d\phi=[-\cos\phi]_0^\pi=2$; $\int_0^{2\pi}d\theta=2\pi$. Multiplying: $\tfrac{a^3}{3}\cdot2\cdot2\pi=\tfrac{4}{3}\pi a^3$ — the familiar sphere volume, confirming the $\rho^2\sin\phi$ element.

<a id="s16"></a>
### Change of variables & the Jacobian

*Polar, cylindrical and spherical are special cases of one principle: change coordinates with a smooth map, and the volume element scales by the determinant of its derivative.*

**What this section says and why we care.** All those special area/volume elements ($r$, $r$, $\rho^2\sin\phi$) are instances of one master rule. When you substitute new variables $(u,v)$ for $(x,y)$ via some map, areas get stretched by a local factor — the absolute value of the **Jacobian determinant**. This is the multivariable substitution rule, generalizing $u$-substitution from Calc I.

**Change of variables & the Jacobian**

$$\iint_R f\,dx\,dy=\iint_S f\big(x(u,v),y(u,v)\big)\,\Big|\frac{\partial(x,y)}{\partial(u,v)}\Big|\,du\,dv$$

$$\frac{\partial(x,y)}{\partial(u,v)}=\det\!\begin{pmatrix} x_u & x_v\\ y_u & y_v\end{pmatrix}$$

*The Jacobian determinant is the local area-stretch factor of the transformation. In $n$ dimensions it is an $n\times n$ determinant.*

Definitions: a **change of variables** (or **coordinate map**) expresses old coordinates as functions of new ones, $x=x(u,v)$, $y=y(u,v)$. $R$ is the region in $xy$; $S$ is the corresponding region in $uv$. The **Jacobian matrix** $\begin{pmatrix}x_u&x_v\\y_u&y_v\end{pmatrix}$ collects the partials of the map; its **determinant** $\frac{\partial(x,y)}{\partial(u,v)}=x_uy_v-x_vy_u$ measures how the map scales tiny areas. We take its absolute value because area is positive.

**Demonstration — the polar Jacobian recovers the $r$**

1. With $x=r\cos\theta,\ y=r\sin\theta$ (so $(u,v)=(r,\theta)$), compute the four partials. Differentiating $x$: $x_r=\cos\theta$, $x_\theta=-r\sin\theta$. Differentiating $y$: $y_r=\sin\theta$, $y_\theta=r\cos\theta$.
2. Form the Jacobian determinant $x_r y_\theta-x_\theta y_r$:

   $$\frac{\partial(x,y)}{\partial(r,\theta)}=\det\!\begin{pmatrix}\cos\theta & -r\sin\theta\\ \sin\theta & r\cos\theta\end{pmatrix}=(\cos\theta)(r\cos\theta)-(-r\sin\theta)(\sin\theta)=r\cos^2\theta+r\sin^2\theta.$$
3. Use the identity $\cos^2\theta+\sin^2\theta=1$: the determinant is $r$. Since $r\ge0$, its absolute value is $r$, so $dx\,dy=r\,dr\,d\theta$ — exactly the polar element of §s13. $\blacksquare$

*Every special volume element in this part is one determinant. The same computation in spherical yields $\rho^2\sin\phi$.*

**Worked example (a linear change).** Evaluate $\iint_R (x+y)\,dx\,dy$ where $R$ is the parallelogram that is the image, under the map $x=u+v$, $y=u-v$, of the unit square $S:\,0\le u\le1,\,0\le v\le1$ (its vertices are $(0,0),(1,1),(2,0),(1,-1)$). Jacobian: $x_u=1,x_v=1,y_u=1,y_v=-1$, so $\frac{\partial(x,y)}{\partial(u,v)}=(1)(-1)-(1)(1)=-2$, absolute value $2$. Also $x+y=(u+v)+(u-v)=2u$. So the integral becomes

$$\iint_S 2u\cdot2\,du\,dv=\int_0^1\!\int_0^1 4u\,du\,dv=\Big(\int_0^1 4u\,du\Big)\Big(\int_0^1 dv\Big)=\big[2u^2\big]_0^1\cdot 1=2.$$

The new variables turned a slanted parallelogram into an easy rectangle, giving $\iint_R(x+y)\,dx\,dy=2$.

> **Concept — why a determinant?**
>
> The derivative of the coordinate map is a matrix (the Jacobian matrix); it sends a tiny coordinate box to a tiny parallelepiped. The **determinant** is precisely the factor by which a linear map scales volume (Section 1's triple product). So the absolute Jacobian determinant is the local volume-conversion rate.

<a id="s17"></a>
### Applications: mass, moments & center of mass

*Multiple integrals compute physical totals from a density. The pattern is always: integrate the density to get the whole, integrate density-times-position to find where it balances.*

**What this section says and why we care.** Given how matter is distributed (its **density**), integrals recover physical totals: the total mass, the balance point (**center of mass**), and the resistance to spinning (**moment of inertia**). The recurring template — total $=\int(\text{density})$, average position $=\frac{\int(\text{position})(\text{density})}{\int(\text{density})}$ — also underlies probability and statistics.

**Mass, moments, centroid**

$$m=\iint_D \rho\,dA,\qquad M_y=\iint_D x\,\rho\,dA,\quad M_x=\iint_D y\,\rho\,dA$$

$$\bar x=\frac{M_y}{m},\qquad \bar y=\frac{M_x}{m}$$

*The 3D versions integrate over a solid with $dV$. With constant density the center of mass is the purely geometric **centroid**.*

Definitions: $\rho(x,y)$ (rho) is the **density** — mass per unit area at each point. The **mass** $m$ adds up density over the region. The **moment** $M_y=\iint x\rho\,dA$ weights each bit of mass by its $x$-distance from the $y$-axis (and symmetrically $M_x$ by $y$); the subscript names the axis about which the moment is taken. The **center of mass** $(\bar x,\bar y)$ is the balance point; dividing the moment by the mass gives the mass-weighted average position. The **centroid** is the center of mass when density is constant — a purely geometric center.

**Moment of inertia**

$$I_x=\iint_D y^2\rho\,dA,\quad I_y=\iint_D x^2\rho\,dA,\quad I_0=\iint_D (x^2+y^2)\rho\,dA$$

*Inertia weights mass by the square of distance from the axis — why mass far from the axis resists rotation so strongly.*

The **moment of inertia** $I$ about an axis weights each bit of mass by the *square* of its distance from that axis; $I_0$ (about the origin/$z$-axis) uses $x^2+y^2$, the squared distance from the origin.

**Worked example.** A thin plate covers the square $0\le x\le1,\,0\le y\le1$ with density $\rho(x,y)=x$ (heavier toward the right).

- Mass: $m=\int_0^1\!\int_0^1 x\,dy\,dx=\int_0^1 x\,dx=\tfrac12$.
- Moment about $y$-axis: $M_y=\int_0^1\!\int_0^1 x\cdot x\,dy\,dx=\int_0^1 x^2\,dx=\tfrac13$.
- So $\bar x=\frac{M_y}{m}=\frac{1/3}{1/2}=\tfrac23$. The balance point sits right of center ($\tfrac23>\tfrac12$), as expected since mass is concentrated toward $x=1$.
- By symmetry in $y$ (density does not depend on $y$): $M_x=\int_0^1\!\int_0^1 y\cdot x\,dy\,dx=\big(\int_0^1 x\,dx\big)\big(\int_0^1 y\,dy\big)=\tfrac12\cdot\tfrac12=\tfrac14$, so $\bar y=\frac{1/4}{1/2}=\tfrac12$ (centered vertically). Center of mass: $(\tfrac23,\tfrac12)$.

> **Connection — the recurring template**
>
> Total = $\int(\text{density})$; average position = $\frac{\int(\text{position})(\text{density})}{\int(\text{density})}$. The same template gives probability (density integrates to 1, mean = $\int x f\,dx$) — the bridge to the statistics companion.

## Part D · Vector calculus

<a id="s18"></a>
### Vector fields

*A vector field attaches an arrow to every point of space — wind velocity, a force, an electric field. Calculus on these fields is the climax of the course.*

**What this section says and why we care.** Until now functions returned numbers (scalar fields). A **vector field** returns an arrow at every point — the natural model for flows and forces. The rest of the course studies how to integrate such fields along curves (work) and across surfaces (flux), and the special, beautiful case where the field is the gradient of a potential.

**Vector field & gradient field**

$$\mathbf F(x,y,z)=\langle P,\,Q,\,R\rangle,\qquad \mathbf F=\nabla f\ \Rightarrow\ \mathbf F \text{ is a gradient (conservative) field}$$

*$f$ is then a **potential** for $\mathbf F$. Gravity and electrostatics are gradient fields.*

Definitions: a **vector field** $\mathbf F$ assigns to each point $(x,y,z)$ the vector $\langle P,Q,R\rangle$, where $P,Q,R$ are ordinary scalar functions of position (the components). A field is a **gradient field** (also **conservative**) if there is a scalar function $f$, called a **potential**, with $\mathbf F=\nabla f$ — i.e. $P=f_x$, $Q=f_y$, $R=f_z$.

**Worked example.** The field $\mathbf F=\langle 2xy,\,x^2\rangle$ is conservative with potential $f(x,y)=x^2y$, since $f_x=2xy=P$ and $f_y=x^2=Q$. (We will learn the test and how to find $f$ in §s20.)

> **Concept — read a field by its flow**
>
> Imagine the field as the velocity of a fluid. Two questions organize everything that follows: along a curve, how much does the flow *push you* (circulation, line integrals); across a boundary, how much flow *passes through* (flux, surface integrals). Curl measures local spin; divergence measures local source/sink.

<a id="s19"></a>
### Line integrals (scalar & vector); work

*Integrate along a curve. For a scalar, you sum a quantity weighted by arc length; for a field, you sum its component along the path — the work it does.*

**What this section says and why we care.** A **line integral** accumulates along a curve rather than over an interval. There are two flavors: the **scalar** line integral weights a quantity by arc length (mass of a wire, say), while the **vector** line integral sums the field's component along the path — physically, the **work** done by a force. Work and circulation are the left-hand sides of Green's and Stokes' theorems.

**Scalar & vector line integrals**

$$\int_C f\,ds=\int_a^b f(\mathbf r(t))\,|\mathbf r'(t)|\,dt$$

$$\int_C \mathbf F\cdot d\mathbf r=\int_a^b \mathbf F(\mathbf r(t))\cdot\mathbf r'(t)\,dt=\int_C P\,dx+Q\,dy+R\,dz$$

*$ds=|\mathbf r'|\,dt$ is arc length; $d\mathbf r=\mathbf r'\,dt$ is the directed step. The vector integral is the work done by $\mathbf F$ along $C$.*

Definitions: a curve $C$ is described by a **parametrization** $\mathbf r(t)=\langle x(t),y(t),z(t)\rangle$, $a\le t\le b$ — a moving point. Its **velocity** is $\mathbf r'(t)=\langle x'(t),y'(t),z'(t)\rangle$ and **speed** is $|\mathbf r'(t)|$. The **arc-length element** $ds=|\mathbf r'(t)|\,dt$ is the tiny length swept in time $dt$ (distance = speed × time). The **directed step** $d\mathbf r=\mathbf r'(t)\,dt$ is the tiny displacement vector. The scalar integral adds $f$ weighted by length; the vector integral adds the dot product of the field with the directed step.

**Worked example (scalar).** Mass of a wire along the line segment $\mathbf r(t)=\langle t,t\rangle$, $0\le t\le1$, with density $f(x,y)=x+y$. Here $\mathbf r'=\langle1,1\rangle$, $|\mathbf r'|=\sqrt2$, and $f(\mathbf r(t))=t+t=2t$. So $\int_C f\,ds=\int_0^1 2t\cdot\sqrt2\,dt=2\sqrt2\cdot\tfrac12=\sqrt2$.

**Worked example (work).** Work by $\mathbf F=\langle y,x\rangle$ along the same segment $\mathbf r(t)=\langle t,t\rangle$. Then $\mathbf F(\mathbf r(t))=\langle t,t\rangle$ and $\mathbf r'=\langle1,1\rangle$, so $\mathbf F\cdot\mathbf r'=t+t=2t$ and $\int_C\mathbf F\cdot d\mathbf r=\int_0^1 2t\,dt=1$.

> **Concept — scalar vs. vector line integral**
>
> The **scalar** integral $\int_C f\,ds$ is independent of direction (it weights by length — think mass of a wire). The **vector** integral $\int_C\mathbf F\cdot d\mathbf r$ reverses sign if you reverse the curve, because it measures directed push. Work and circulation are vector line integrals.

> **Connection — projecting onto the tangent**
>
> $\mathbf F\cdot d\mathbf r=(\mathbf F\cdot\mathbf T)\,ds$: the work integral is the scalar integral of the tangential component $\mathbf F\cdot\mathbf T$. This tangential view becomes the left side of Green's and Stokes' theorems (circulation). (Here $\mathbf T=\mathbf r'/|\mathbf r'|$ is the **unit tangent**, the direction of travel.)

<a id="s20"></a>
### The Fundamental Theorem for line integrals & conservative fields

*For a gradient field, a line integral depends only on the endpoints — not the path. This is the FTC itself, lifted to curves in space.*

**What this section says and why we care.** When a field is a gradient $\nabla f$, its work integral collapses to a difference of potential values at the endpoints — the path in between does not matter. This is the literal Fundamental Theorem of Calculus carried up to curves in space, and it is the simplest of the "big theorems." It also gives a quick test for whether a field is conservative.

**Fundamental Theorem for line integrals**

$$\int_C \nabla f\cdot d\mathbf r=f(\mathbf r(b))-f(\mathbf r(a))$$

*Path-independent; around a closed loop it is $0$. Such $\mathbf F=\nabla f$ is **conservative**.*

A **closed loop** is a curve that returns to its start, $\mathbf r(b)=\mathbf r(a)$; then the right side is $0$. **Path-independent** means the integral depends only on the endpoints, not the route.

**Test for conservative fields (simply connected domain)**

$$\mathbf F=\langle P,Q\rangle \text{ conservative}\iff \frac{\partial P}{\partial y}=\frac{\partial Q}{\partial x}\quad\big(\text{in 3D: }\nabla\times\mathbf F=\mathbf 0\big)$$

*The cross-partial test is Clairaut's theorem (Section 9) in disguise: if $\mathbf F=\nabla f$ then $P_y=f_{xy}=f_{yx}=Q_x$.*

A domain is **simply connected** if it has no holes (any loop can shrink to a point inside it). On such a domain the cross-partial equality is both necessary and sufficient. Why necessary: if $\mathbf F=\nabla f$ then $P=f_x,Q=f_y$, so $P_y=f_{xy}$ and $Q_x=f_{yx}$, equal by Clairaut (§s9).

**Demonstration — proving the FTC for line integrals**

1. Let $\mathbf F=\nabla f$ and parametrize $C$ by $\mathbf r(t),\ a\le t\le b$. By the definition of the vector line integral (§s19):

   $$\int_C\nabla f\cdot d\mathbf r=\int_a^b\nabla f(\mathbf r(t))\cdot\mathbf r'(t)\,dt.$$
2. By the multivariable chain rule (§s6, the gradient-dotted-with-velocity form), the integrand is the total $t$-derivative of $f$ along the path:

   $$\nabla f(\mathbf r(t))\cdot\mathbf r'(t)=\frac{d}{dt}\,f(\mathbf r(t)).$$
3. Now it is an ordinary single-variable integral of a derivative; apply the classical FTC (§s0):

   $$\int_a^b\frac{d}{dt}f(\mathbf r(t))\,dt=f(\mathbf r(b))-f(\mathbf r(a)).\qquad\blacksquare$$

**Worked example.** With $\mathbf F=\langle 2xy,x^2\rangle=\nabla f$, $f=x^2y$ (from §s18), the work along *any* path from $(0,0)$ to $(1,3)$ is $f(1,3)-f(0,0)=1^2\cdot3-0=3$ — no parametrization needed. (Test confirms conservative: $P_y=\partial_y(2xy)=2x$ and $Q_x=\partial_x(x^2)=2x$, equal.)

*The gradient is the multivariable derivative; integrating it recovers the function at the boundary points — the first instance of the boundary principle of Section 27.*

<a id="s21"></a>
### Green's theorem

*The first of the great theorems: circulation of a field around a closed plane curve equals the integral of its (scalar) curl over the enclosed region.*

**What this section says and why we care.** **Green's theorem** is the first full "boundary = interior" theorem in the plane. It equates the **circulation** of a field around a closed curve (a line integral on the boundary) with a double integral of the field's **scalar curl** over the region inside. It packages two physical readings — circulation and flux — and is the flat prototype of Stokes and Gauss.

**Green's theorem (circulation form)**

$$\oint_C P\,dx+Q\,dy=\iint_D\Big(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\Big)\,dA$$

*$C$ is the positively oriented (counterclockwise) boundary of region $D$. The integrand on the right is the 2D scalar curl.*

Definitions: $\oint_C$ is a line integral around a *closed* curve $C$. **Positively oriented** (counterclockwise) means as you walk along $C$, the region $D$ is on your left. **Circulation** is the work integral around the loop. The **scalar curl** $Q_x-P_y$ measures the field's tendency to rotate at a point.

**Two consequences**

$$\text{Area}(D)=\oint_C x\,dy=-\oint_C y\,dx=\tfrac12\oint_C x\,dy-y\,dx$$

$$\text{Flux form: }\ \oint_C \mathbf F\cdot\mathbf n\,ds=\iint_D \Big(\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}\Big)\,dA$$

*The circulation form is the 2D Stokes' theorem; the flux form is the 2D Divergence theorem. One theorem, two readings.*

The area formula follows by choosing $P,Q$ so that $Q_x-P_y=1$ (e.g. $P=0,Q=x$ gives $\iint 1\,dA=\text{Area}$, equal to $\oint x\,dy$). Here $\mathbf n$ is the **outward unit normal** to $C$, and the flux form measures total outflow across $C$.

**Demonstration — Green's theorem on a Type I/II region**

1. Prove the $P$ piece on a Type I region $D=\{a\le x\le b,\ g_1(x)\le y\le g_2(x)\}$ (§s12). Integrate the $-P_y$ term over $D$ by Fubini, doing $y$ first:

   $$\iint_D \!-\frac{\partial P}{\partial y}\,dA=-\int_a^b\!\!\int_{g_1(x)}^{g_2(x)}\frac{\partial P}{\partial y}\,dy\,dx.$$
2. The inner integral is of a $y$-derivative, so by the FTC (§s0) it evaluates at the $y$-limits:

   $$-\int_a^b\big[P(x,g_2(x))-P(x,g_1(x))\big]\,dx=\int_a^b P(x,g_1(x))\,dx-\int_a^b P(x,g_2(x))\,dx.$$
3. Now compute $\oint_C P\,dx$ directly by walking the boundary counterclockwise. On the bottom edge $y=g_1(x)$ ($x$: $a\to b$) it contributes $+\int_a^b P(x,g_1)\,dx$; on the top edge $y=g_2(x)$ ($x$: $b\to a$, reversed) it contributes $-\int_a^b P(x,g_2)\,dx$; on the vertical sides $x$ is constant so $dx=0$ and they contribute nothing. The sum equals step 2:

   $$\oint_C P\,dx=\iint_D\!-\frac{\partial P}{\partial y}\,dA.$$
4. Symmetrically, viewing $D$ as Type II and doing $x$ first gives $\oint_C Q\,dy=\iint_D \frac{\partial Q}{\partial x}\,dA$. Add the two results to obtain Green's theorem. $\blacksquare$

*A general region is glued from such pieces; the interior boundaries cancel in pairs, leaving only the outer curve. This cancellation is the engine behind every theorem in Part D.*

**Worked example.** Compute $\oint_C(-y\,dx+x\,dy)$ around the unit circle $C$ counterclockwise. Here $P=-y$, $Q=x$, so $Q_x-P_y=1-(-1)=2$. By Green's theorem the line integral equals $\iint_D 2\,dA=2\cdot\text{Area}(D)=2\cdot\pi(1)^2=2\pi$. (Direct check via $\mathbf r(t)=\langle\cos t,\sin t\rangle$ also gives $2\pi$.)

<a id="s22"></a>
### Curl & divergence

*Two derivative operators on a vector field. Curl measures microscopic rotation; divergence measures net outflow. They are the integrands of Stokes and Gauss.*

**What this section says and why we care.** Two operators turn a vector field into new fields that capture its local behavior: the **curl** (a vector measuring local spin) and the **divergence** (a scalar measuring local source/sink). They are exactly the "derivative" objects appearing on the interior side of Stokes' and Gauss's theorems. Two clean identities — curl of a gradient is zero, divergence of a curl is zero — organize the whole theory.

**Curl & divergence via $\nabla$**

$$\nabla\times\mathbf F=\begin{vmatrix}\mathbf i&\mathbf j&\mathbf k\\ \partial_x&\partial_y&\partial_z\\ P&Q&R\end{vmatrix},\qquad \nabla\cdot\mathbf F=\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}$$

*Curl returns a vector (axis of spin); divergence returns a scalar (source strength).*

Here $\nabla=\langle\partial_x,\partial_y,\partial_z\rangle$ is the **del operator** — a symbolic vector of partial-derivative instructions. The **curl** $\nabla\times\mathbf F$ is computed like a cross product (§s1) with the second row being these derivative operators; expanded it is $\langle R_y-Q_z,\;P_z-R_x,\;Q_x-P_y\rangle$. The **divergence** $\nabla\cdot\mathbf F$ is computed like a dot product, summing the "diagonal" partials.

**Two identities that organize everything**

$$\nabla\times(\nabla f)=\mathbf 0,\qquad \nabla\cdot(\nabla\times\mathbf F)=0$$

*"Curl of a gradient is zero" (gradient fields are irrotational); "divergence of a curl is zero" (curl fields are sourceless). Both are Clairaut's theorem in vector dress.*

**Demonstration — curl of a gradient vanishes**

1. Take $\mathbf F=\nabla f=\langle f_x,f_y,f_z\rangle$, so $P=f_x,Q=f_y,R=f_z$. The $\mathbf k$-component of $\nabla\times\mathbf F$ is $Q_x-P_y$ (from the expanded curl above):

   $$\partial_x(f_y)-\partial_y(f_x)=f_{yx}-f_{xy}.$$
2. By Clairaut's theorem (§s9), continuous mixed partials are equal, $f_{xy}=f_{yx}$, so this component is $f_{yx}-f_{xy}=0$. The same cancellation, with the other pairs ($f_{zy}=f_{yz}$ and $f_{xz}=f_{zx}$), kills the $\mathbf i$- and $\mathbf j$-components. Hence $\nabla\times(\nabla f)=\mathbf 0$. $\blacksquare$

**Worked example (divergence and curl).** For $\mathbf F=\langle xy,\,yz,\,zx\rangle$: divergence $\nabla\cdot\mathbf F=\partial_x(xy)+\partial_y(yz)+\partial_z(zx)=y+z+x$. Curl: $\nabla\times\mathbf F=\langle R_y-Q_z,\,P_z-R_x,\,Q_x-P_y\rangle=\langle 0-y,\,0-z,\,0-x\rangle=\langle -y,-z,-x\rangle$.

> **Concept — the physical meaning**
>
> Drop a tiny paddlewheel in the flow: it spins about the axis $\nabla\times\mathbf F$, at a rate set by $|\nabla\times\mathbf F|$. Enclose a tiny ball: $\nabla\cdot\mathbf F$ is the net flux out per unit volume — positive at a source, negative at a sink. These local readings become the global theorems when integrated.

*Hence conservative $\Rightarrow$ irrotational — the 3D version of the $P_y=Q_x$ test of Section 20.*

<a id="s23"></a>
### Parametric surfaces & surface area

*Just as a curve is one parameter, a surface is two. The cross product of the two tangent vectors gives the normal — and the area element.*

**What this section says and why we care.** A curve needs one parameter; a **surface** needs two. Writing $\mathbf r(u,v)$ for the surface, the two partial-velocity vectors $\mathbf r_u,\mathbf r_v$ span the tangent plane, and their cross product is simultaneously the surface **normal** (direction) and the **area scale** (magnitude). This single object drives surface area, surface integrals, and flux.

**Parametrization, normal, surface area**

$$\mathbf r(u,v)=\langle x,y,z\rangle,\qquad \mathbf r_u\times\mathbf r_v=\text{normal},\qquad dS=|\mathbf r_u\times\mathbf r_v|\,du\,dv$$

$$A(S)=\iint_D |\mathbf r_u\times\mathbf r_v|\,dA$$

*For a graph $z=g(x,y)$: $dS=\sqrt{1+g_x^2+g_y^2}\,dA$.*

Definitions: a **parametric surface** is given by $\mathbf r(u,v)$ with two parameters; as $(u,v)$ ranges over a region $D$, the tip of $\mathbf r$ traces the surface $S$. The **tangent vectors** $\mathbf r_u=\partial\mathbf r/\partial u$ and $\mathbf r_v=\partial\mathbf r/\partial v$ point along the surface; their cross product is normal to it. $dS$ is the **surface-area element**.

**Demonstration — the surface-area element $dS=|\mathbf r_u\times\mathbf r_v|\,du\,dv$**

1. Take a small parameter rectangle $[u,u+du]\times[v,v+dv]$; it maps to a small curved patch on $S$. Holding $v$ fixed and increasing $u$ by $du$ moves you by approximately $\mathbf r_u\,du$ (rate of change times step); similarly the other edge is approximately $\mathbf r_v\,dv$.
2. For small steps the patch is nearly the parallelogram spanned by these two edge vectors. By §s1, the area of a parallelogram spanned by two vectors is the magnitude of their cross product:

   $$dS=|\,\mathbf r_u\,du\times\mathbf r_v\,dv\,|=|\mathbf r_u\times\mathbf r_v|\,du\,dv,$$

   using that scaling each factor by the positive numbers $du,dv$ scales the cross product's length by $du\,dv$. $\blacksquare$

**Worked example (graph formula).** For a graph $z=g(x,y)$, parametrize $\mathbf r(x,y)=\langle x,y,g(x,y)\rangle$. Then $\mathbf r_x=\langle1,0,g_x\rangle$, $\mathbf r_y=\langle0,1,g_y\rangle$, and the cross product is $\langle -g_x,-g_y,1\rangle$, whose length is $\sqrt{g_x^2+g_y^2+1}$. Hence $dS=\sqrt{1+g_x^2+g_y^2}\,dA$, matching the boxed special case.

**Worked example (numeric area).** Surface area of the plane piece $z=2x+2y$ over the unit square $0\le x,y\le1$: here $g_x=2,g_y=2$, so $dS=\sqrt{1+4+4}\,dA=3\,dA$ and $A=\iint_D 3\,dA=3\cdot1=3$.

*The cross product does double duty: its direction is the surface normal (needed for flux), its magnitude is the area scale.*

<a id="s24"></a>
### Surface integrals & flux

*Integrate over a surface. For a scalar, weight by area; for a field, sum the component crossing the surface — the flux.*

**What this section says and why we care.** Mirroring line integrals, **surface integrals** come in two flavors. The **scalar** surface integral weights a quantity by area (mass of a curved sheet). The **flux** integral sums the component of a vector field passing *through* the surface — how much fluid crosses per unit time. Flux is the boundary side of the Divergence theorem and the interior side of Stokes'.

**Scalar surface integral & flux**

$$\iint_S f\,dS=\iint_D f(\mathbf r(u,v))\,|\mathbf r_u\times\mathbf r_v|\,dA$$

$$\iint_S \mathbf F\cdot d\mathbf S=\iint_S \mathbf F\cdot\mathbf n\,dS=\iint_D \mathbf F\cdot(\mathbf r_u\times\mathbf r_v)\,dA$$

*$d\mathbf S=\mathbf n\,dS=(\mathbf r_u\times\mathbf r_v)\,dA$. Flux measures how much of $\mathbf F$ passes through $S$ per unit time.*

Definitions: $\mathbf n$ is the **unit normal** to the surface (the chosen "out" direction); $d\mathbf S=\mathbf n\,dS$ is the **vector area element**, combining the area scale with the normal direction. The flux integral dots the field with this vector element, picking out only the part of $\mathbf F$ perpendicular to the surface (the part that actually crosses).

**Worked example (flux).** Flux of $\mathbf F=\langle 0,0,z\rangle$ upward through the part of the plane $z=x+y$ over the unit square $0\le x,y\le1$. Parametrize $\mathbf r(x,y)=\langle x,y,x+y\rangle$; then $\mathbf r_x\times\mathbf r_y=\langle -1,-1,1\rangle$ (upward $z$-component, as wanted). On the surface $\mathbf F=\langle0,0,x+y\rangle$, so $\mathbf F\cdot(\mathbf r_x\times\mathbf r_y)=x+y$. Thus

$$\iint_S\mathbf F\cdot d\mathbf S=\int_0^1\!\int_0^1(x+y)\,dx\,dy=\int_0^1\Big(\tfrac12+y\Big)dy=\tfrac12+\tfrac12=1.$$

> **Concept — orientation matters**
>
> A flux integral needs a chosen side: an **orientation**, given by a continuous unit normal $\mathbf n$. Flipping $\mathbf n$ flips the sign. For a closed surface the convention is the *outward* normal. (A Möbius band is non-orientable — no consistent choice exists.)

> **Connection — the parallel with line integrals**
>
> Scalar surface integral ↔ scalar line integral (weight by measure); flux $\iint\mathbf F\cdot\mathbf n\,dS$ ↔ circulation $\int\mathbf F\cdot\mathbf T\,ds$. Curves use the tangent; surfaces use the normal. Stokes (Section 25) and Gauss (Section 26) tie these together.

<a id="s25"></a>
### Stokes' theorem

*Green's theorem, lifted off the plane. Circulation around the boundary curve of a surface equals the flux of the curl through the surface.*

**What this section says and why we care.** **Stokes' theorem** generalizes Green's theorem to curved surfaces in space. The circulation of a field around the boundary curve of a surface equals the flux of the field's curl through the surface. Remarkably, *any* surface with the same boundary gives the same answer — the boundary alone controls the circulation.

**Stokes' theorem**

$$\oint_{\partial S} \mathbf F\cdot d\mathbf r=\iint_S (\nabla\times\mathbf F)\cdot d\mathbf S$$

*$\partial S$ is the boundary curve of $S$, oriented by the right-hand rule relative to $\mathbf n$. Any surface with the same boundary gives the same answer.*

Definitions: $\partial S$ ("boundary of $S$") is the edge curve of the surface. The **right-hand rule orientation**: if the thumb of your right hand points along $\mathbf n$, the curled fingers give the positive direction around $\partial S$. The left side is circulation; the right is the flux of the curl (§s22, §s24).

> **Concept — sum the microscopic spins**
>
> Curl is local circulation per unit area. Tile the surface with tiny loops; on each, circulation $\approx(\nabla\times\mathbf F)\cdot\mathbf n\,dS$. Adjacent loops share edges traversed in *opposite* directions, so all interior contributions cancel — only the outer boundary survives. That cancellation is Green's proof (Section 21), now on a surface.

**Worked example.** Verify Stokes for $\mathbf F=\langle -y,x,0\rangle$ on the disk $S:\,x^2+y^2\le1$ in the plane $z=0$ with upward normal $\mathbf n=\mathbf k$. Curl: $\nabla\times\mathbf F=\langle0,0,\,Q_x-P_y\rangle=\langle0,0,1-(-1)\rangle=\langle0,0,2\rangle$. Flux of curl: $\iint_S\langle0,0,2\rangle\cdot\mathbf k\,dS=\iint_S 2\,dA=2\pi$. Boundary circulation around the unit circle (from the worked example of §s21, $\oint -y\,dx+x\,dy=2\pi$) also gives $2\pi$ — they agree.

> **Connection — Green is flat Stokes**
>
> Take $S$ to be a region in the $xy$-plane with $\mathbf n=\mathbf k$. Then $(\nabla\times\mathbf F)\cdot\mathbf k=Q_x-P_y$ and Stokes becomes $\oint P\,dx+Q\,dy=\iint(Q_x-P_y)\,dA$ — Green's theorem exactly.

<a id="s26"></a>
### The Divergence (Gauss) theorem

*The flux of a field out through a closed surface equals the integral of its divergence over the solid inside. Sources inside account for net outflow.*

**What this section says and why we care.** The **Divergence theorem** (Gauss's theorem) is the 3D climax: the total flux of a field outward through a closed surface equals the integral of the field's divergence over the solid enclosed. In words, net outflow across the boundary = total source strength inside — the natural conservation law of fluid flow and electromagnetism.

**Divergence theorem**

$$\iint_{\partial E} \mathbf F\cdot d\mathbf S=\iiint_E (\nabla\cdot\mathbf F)\,dV$$

*$\partial E$ is the closed boundary surface of solid $E$, with outward normal. Total outflow = total source strength inside.*

Definitions: $E$ is a solid region, $\partial E$ its closed bounding surface (closed, since it bounds the solid $E$), oriented with the **outward** normal. The left side is total flux out; the right integrates the divergence (§s22) over the interior.

> **Concept — telescoping the fluxes**
>
> Divergence is net outflow per unit volume. Chop $E$ into tiny boxes; each contributes $(\nabla\cdot\mathbf F)\,dV$ of outflow. Where two boxes touch, the flux out of one is flux *into* the other — equal and opposite, so it cancels. Only the outer surface remains. Same cancellation principle as Green and Stokes.

**Worked example.** Let $\mathbf F=\langle x,y,z\rangle$ and $E$ the ball of radius $a$. Divergence: $\nabla\cdot\mathbf F=1+1+1=3$. So $\iiint_E 3\,dV=3\cdot\text{Vol}=3\cdot\tfrac43\pi a^3=4\pi a^3$. Direct flux: on the sphere the outward normal is $\mathbf n=\frac{1}{a}\langle x,y,z\rangle$, so $\mathbf F\cdot\mathbf n=\frac{1}{a}(x^2+y^2+z^2)=\frac{a^2}{a}=a$ (constant), giving flux $=a\cdot(\text{surface area})=a\cdot4\pi a^2=4\pi a^3$. The two sides agree.

> **Connection — Green's flux form is flat Gauss**
>
> In the plane, the Divergence theorem reads $\oint_C\mathbf F\cdot\mathbf n\,ds=\iint_D(P_x+Q_y)\,dA$ — exactly the flux form of Green's theorem (Section 21). Gauss is its 3D upgrade.

## Part E · Synthesis

<a id="s27"></a>
### The unifying picture: one theorem behind them all

*Five theorems — FTC, FTC for line integrals, Green, Stokes, Gauss — are a single statement seen from different dimensions: the integral of a derivative over a region equals the integral of the function over its boundary.*

**What this section says and why we care.** Everything you proved collapses into one sentence. The Fundamental Theorem of Calculus, its line-integral version, Green, Stokes, and Gauss are all the *same* statement in different dimensions: integrate a derivative over a region and you get the original function summed over the boundary. Recognizing this is the payoff of the whole course.

> **Principle — the generalized Stokes' theorem**
>
> In the language of differential forms, all five collapse to one line: **the integral of $d\omega$ over a region $M$ equals the integral of $\omega$ over the boundary $\partial M$**. Here $d$ is the exterior derivative (which specializes to gradient, curl, divergence) and $\partial$ is "take the boundary." Each classical theorem is this with a particular dimension and operator.

Definitions (lightly): a **differential form** $\omega$ is the kind of object you integrate (a function, or a "$P\,dx+Q\,dy$" expression, etc.). The **exterior derivative** $d$ is a single operation that becomes the gradient on functions, the curl on 1-forms, and the divergence on 2-forms — depending on the dimension. The **boundary** $\partial M$ is the edge of the region $M$ (endpoints of an interval, the curve bounding a surface, the surface bounding a solid).

**The master statement**

$$\int_{M} d\omega=\int_{\partial M}\omega$$

*"Differentiate then integrate over the inside = integrate the original over the boundary." Every theorem below is one instance.*

| Theorem | Region $M$ | Boundary $\partial M$ | Derivative $d$ |
| --- | --- | --- | --- |
| FTC (Calc I) | interval $[a,b]$ | two endpoints | $f'$ |
| FTC, line integrals | curve $C$ | two endpoints | gradient $\nabla f$ |
| Green | plane region $D$ | curve $\partial D$ | scalar curl $Q_x-P_y$ |
| Stokes | surface $S$ | curve $\partial S$ | curl $\nabla\times\mathbf F$ |
| Divergence | solid $E$ | surface $\partial E$ | divergence $\nabla\cdot\mathbf F$ |

**Demonstration — reading each classic off the master line**

1. **FTC.** Take $M=[a,b]$, $\omega=f$, $d\omega=f'\,dx$. The boundary $\partial M$ is the two endpoints with signs $+b,-a$, so $\int_{\partial M}\omega=f(b)-f(a)$. The "integral" over a 0-dimensional set is just evaluation. The master line becomes $\int_a^b f'\,dx=f(b)-f(a)$ — §s0.
2. **Line-integral FTC.** Take $M=C$ (a curve), $\omega=f$, $d\omega=\nabla f\cdot d\mathbf r$; the boundary is the two endpoints. The master line is $\int_C\nabla f\cdot d\mathbf r=f(\text{end})-f(\text{start})$ — §s20.
3. **Green / Stokes.** $M$ is 2-dimensional (a plane region or surface); $d$ produces the (scalar or vector) curl; $\partial M$ is the bounding curve. The master line reads circulation = curl flux — §s21, §s25.
4. **Divergence.** $M$ is the 3-dimensional solid; $d$ produces the divergence; $\partial M$ is the bounding surface. The master line reads outflow = source total — §s26.

*The recurring proof move is the same every time: tile the region, note interior boundaries cancel in pairs, and only $\partial M$ survives.* You saw this explicit cancellation in the Green's-theorem demonstration (§s21) and in the telescoping pictures for Stokes and Gauss.

#### The whole of vector calculus on one line

> derivative inside = values on the boundary · $ \displaystyle\int_M d\omega=\int_{\partial M}\omega $

> **The habit to keep**
>
> Whenever you meet a new integral identity, ask the two questions of this course: *what is the region, and what is its boundary?* Behind partial derivatives, multiple integrals, flux and circulation sits one idea — a derivative summed over the inside is the function read off the edge — the Fundamental Theorem of Calculus, all the way up.

---

*A third-semester course in multivariable and vector calculus — concepts, principles, formulas, and the demonstrations behind them — built as a companion to the Statistics and Calculus guides. Read once for the shape; return to any box as a reference. Remember: every great theorem here says the same thing — integrate a derivative over a region, and you get the function back on its boundary.*
