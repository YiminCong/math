# Multivariable, *connected.*

A full third-semester course — the geometry of space, the calculus of functions on it, integration over regions and surfaces, and the great vector-calculus theorems — laid out basics → advanced. Every core result is **demonstrated**, and the single thread linking gradient, Green, Stokes and Gauss is made explicit.

[← Back to all guides](../README.md)

## Part A · Space, vectors & functions

<a id="s0"></a>
### The big picture: from one variable to many

Single-variable calculus studied functions $y=f(x)$ on a line. Multivariable calculus does the same three things — limits, derivatives, integrals — but the inputs and outputs now live in space. That one change, "more than one variable," reorganizes the entire subject.

- **Differentiate** — the derivative becomes a whole *gradient vector* (and later a matrix), encoding the rate of change in *every* direction at once.
- **Integrate** — the integral becomes a sum over a 2D region, a 3D solid, a curve, or a surface.
- **Connect** — a family of theorems (Green, Stokes, Gauss) tie a derivative *inside* a region to values on its *boundary*, exactly as the Fundamental Theorem of Calculus did on an interval.

> **Principle — the organizing idea**
>
> Every object splits by **how many numbers go in** and **how many come out**. A **scalar field** $f:\mathbb R^n\to\mathbb R$ (temperature) has a gradient. A **vector field** $\mathbf F:\mathbb R^n\to\mathbb R^n$ (flow, force) has curl and divergence. A **parametrization** $\mathbb R\to\mathbb R^3$ or $\mathbb R^2\to\mathbb R^3$ traces a curve or surface. Knowing the type tells you which operator and which integral apply.

> **Connection — one idea you already own**
>
> The whole subject is the Fundamental Theorem of Calculus, $\int_a^b f'\,dx=f(b)-f(a)$, generalized: a derivative integrated over a region equals the function evaluated on the region's boundary. Hold that sentence; Section 27 shows all four big theorems are special cases of it.

#### The whole course on one line

> Vectors & space → functions of several variables → partial derivatives & the gradient → optimization → multiple integrals → vector fields → Green / Stokes / Gauss

<a id="s1"></a>
### Vectors, dot product & cross product

*A vector carries magnitude and direction. Two products turn vectors into the language of angles, projections, areas and volumes.*

> **Concept — points, vectors, and the two products**
>
> A point is a location; a **vector** $\mathbf v=\langle v_1,v_2,v_3\rangle$ is a displacement. The **dot product** returns a scalar that measures alignment (and hence angle and projection); the **cross product** returns a vector perpendicular to both, whose length is the area of the parallelogram they span. Dot is about angle; cross is about area and orientation.

**Magnitude, dot product, angle**

$$|\mathbf v|=\sqrt{v_1^2+v_2^2+v_3^2},\qquad \mathbf a\cdot\mathbf b=\sum_i a_ib_i=|\mathbf a||\mathbf b|\cos\theta$$

*$\mathbf a\cdot\mathbf b=0\iff$ perpendicular. The scalar projection of $\mathbf a$ onto $\mathbf b$ is $\dfrac{\mathbf a\cdot\mathbf b}{|\mathbf b|}$.*

**Cross product (in $\mathbb R^3$)**

$$\mathbf a\times\mathbf b=\begin{vmatrix}\mathbf i&\mathbf j&\mathbf k\\ a_1&a_2&a_3\\ b_1&b_2&b_3\end{vmatrix},\qquad |\mathbf a\times\mathbf b|=|\mathbf a||\mathbf b|\sin\theta$$

*$\mathbf a\times\mathbf b$ is perpendicular to both, direction by the right-hand rule; its length is the parallelogram area. $\mathbf a\times\mathbf b=-\,\mathbf b\times\mathbf a$.*

**Scalar triple product → volume**

$$V=\big|\,\mathbf a\cdot(\mathbf b\times\mathbf c)\,\big|=\left|\det\!\begin{pmatrix}a_1&a_2&a_3\\ b_1&b_2&b_3\\ c_1&c_2&c_3\end{pmatrix}\right|$$

*The signed volume of the parallelepiped. Zero $\iff$ the three vectors are coplanar.*

**Demonstration — the dot product gives the angle**

1. Place $\mathbf a,\mathbf b$ tail to tail; the third side of the triangle is $\mathbf a-\mathbf b$. The Law of Cosines says

   $$|\mathbf a-\mathbf b|^2=|\mathbf a|^2+|\mathbf b|^2-2|\mathbf a||\mathbf b|\cos\theta.$$
2. Expand the left side algebraically with the dot product:

   $$|\mathbf a-\mathbf b|^2=(\mathbf a-\mathbf b)\cdot(\mathbf a-\mathbf b)=|\mathbf a|^2-2\,\mathbf a\cdot\mathbf b+|\mathbf b|^2.$$
3. Match the two expressions; the squared-length terms cancel, leaving

   $$\mathbf a\cdot\mathbf b=|\mathbf a||\mathbf b|\cos\theta.$$

*Geometry (angle) and algebra (component sum) are two faces of one operation.*

<a id="s2"></a>
### Lines, planes & quadric surfaces

*With vectors in hand, the basic objects of space get clean equations: a line needs a point and a direction; a plane needs a point and a normal.*

**Line through $P_0$ with direction $\mathbf v$**

$$\mathbf r(t)=\mathbf r_0+t\mathbf v,\qquad \frac{x-x_0}{v_1}=\frac{y-y_0}{v_2}=\frac{z-z_0}{v_3}$$

*Vector form (left) and symmetric form (right). A line is a point plus all scalar multiples of one direction.*

**Plane through $P_0$ with normal $\mathbf n$**

$$\mathbf n\cdot(\mathbf r-\mathbf r_0)=0\ \Longleftrightarrow\ a(x-x_0)+b(y-y_0)+c(z-z_0)=0$$

*A point lies on the plane exactly when its displacement from $P_0$ is perpendicular to $\mathbf n=\langle a,b,c\rangle$. The normal is read straight off the coefficients.*

**Distance from a point to a plane**

$$D=\frac{|a x_1+b y_1+c z_1+d|}{\sqrt{a^2+b^2+c^2}}$$

*It is the length of the projection of $\overrightarrow{P_0P_1}$ onto the unit normal — a dot product divided by $|\mathbf n|$.*

> **Concept — quadric surfaces by their traces**
>
> The level-two surfaces — **ellipsoid** $\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}=1$, **paraboloid** $z=x^2+y^2$, **cone** $z^2=x^2+y^2$, **hyperboloids**, **saddle** $z=x^2-y^2$ — are best understood by their *traces*: the curves you get by slicing with coordinate planes. Set one variable constant and read off the conic that results.

<a id="s3"></a>
### Functions of several variables; level curves & surfaces

*A function $z=f(x,y)$ assigns a height to each point of the plane — a landscape. The cleanest way to read that landscape flat is the contour map.*

> **Concept — graph vs. level set**
>
> The **graph** of $f(x,y)$ is a surface in $\mathbb R^3$. A **level curve** $f(x,y)=k$ collects all inputs that give the same output $k$ — a contour line, like on a topographic map. For $f(x,y,z)$, $f=k$ is a **level surface**. Tight contours mean steep terrain; the gradient (Section 7) will point straight across them.

**Domain, range, level set**

$$f:D\subseteq\mathbb R^n\to\mathbb R,\qquad \text{level set}=\{\,\mathbf x: f(\mathbf x)=k\,\}$$

*Always pin down the domain first: $\sqrt{}$ needs nonnegative arguments, $\ln$ needs positive, denominators must be nonzero.*

> **Connection — back to one variable**
>
> A level curve is the multivariable cousin of "solve $f(x)=k$." Reading a function through its level sets — rather than its graph — is the visual habit that makes the gradient, Lagrange multipliers, and implicit differentiation feel natural.

<a id="s4"></a>
### Limits & continuity in several variables

*The definition of a limit looks the same, but one feature is genuinely new: in the plane you can approach a point from infinitely many directions, and the limit must agree along all of them.*

**Limit and continuity**

$$\lim_{(x,y)\to(a,b)}f(x,y)=L:\ \forall\varepsilon>0\ \exists\delta>0,\ 0<|(x,y)-(a,b)|<\delta\Rightarrow|f-L|<\varepsilon$$

$$f \text{ continuous at }(a,b)\iff \lim_{(x,y)\to(a,b)}f(x,y)=f(a,b)$$

> **Principle — the two-path test**
>
> If $f$ approaches *different* values along two different paths into $(a,b)$, the limit **does not exist**. This is the standard tool: try $y=0$, then $x=0$, then $y=mx$, then $y=x^2$. One disagreement settles it.

**Demonstration — a limit that fails the path test**

1. Consider $f(x,y)=\dfrac{xy}{x^2+y^2}$ as $(x,y)\to(0,0)$. Along the $x$-axis ($y=0$):

   $$f(x,0)=\frac{0}{x^2}=0.$$
2. Along the line $y=x$:

   $$f(x,x)=\frac{x\cdot x}{x^2+x^2}=\frac{x^2}{2x^2}=\frac12.$$
3. The two paths give $0$ and $\tfrac12$. Since they disagree, the limit does not exist — even though each single-variable slice is perfectly tame.

*Approaching from one direction is never enough; the limit must hold uniformly from all of them.*

## Part B · Differential calculus of several variables

<a id="s5"></a>
### Partial derivatives

*To differentiate a function of many variables, freeze all but one and differentiate as usual. Each variable gets its own slope.*

**Definition of the partial derivative**

$$f_x(a,b)=\frac{\partial f}{\partial x}=\lim_{h\to0}\frac{f(a+h,b)-f(a,b)}{h}$$

*$f_x$ is the slope of the surface in the $x$-direction — the ordinary derivative of the single-variable slice $g(x)=f(x,b)$ with $y$ held constant.*

> **Concept — "hold the others constant"**
>
> Computing $\partial f/\partial x$, every other variable is a constant. So $\partial_x(x^2y^3)=2xy^3$ and $\partial_y(x^2y^3)=3x^2y^2$. All single-variable rules (product, quotient, chain) apply unchanged; only your view of "what is constant" shifts.

> **Connection — slopes assemble into the gradient**
>
> A function of $n$ variables has $n$ first partials. Collected into a vector $\nabla f=\langle f_x,f_y,\dots\rangle$ they become the **gradient** (Section 7) — the single object that plays the role the derivative $f'(x)$ played in one variable.

<a id="s6"></a>
### The multivariable chain rule

*When variables depend on other variables, contributions flow along every path and add up. The chain rule becomes a sum over routes.*

**Chain rule — the two main cases**

$$\frac{df}{dt}=\frac{\partial f}{\partial x}\frac{dx}{dt}+\frac{\partial f}{\partial y}\frac{dy}{dt}\qquad\big(x=x(t),\,y=y(t)\big)$$

$$\frac{\partial f}{\partial s}=\frac{\partial f}{\partial x}\frac{\partial x}{\partial s}+\frac{\partial f}{\partial y}\frac{\partial y}{\partial s}\qquad\big(x=x(s,t),\,y=y(s,t)\big)$$

*Draw a tree: sum over every path from the output to the variable you are differentiating with respect to, multiplying along each path.*

> **Connection — it is a gradient dotted with a velocity**
>
> The first case is exactly $\dfrac{df}{dt}=\nabla f\cdot \mathbf r'(t)$, the gradient dotted with the velocity of the path. This single identity reappears as the directional derivative (Section 7) and as the integrand of the Fundamental Theorem for line integrals (Section 20).

**Demonstration — implicit differentiation from the chain rule**

1. Suppose $F(x,y)=0$ defines $y$ as a function of $x$. Differentiate both sides with respect to $x$, treating $y=y(x)$:

   $$\frac{\partial F}{\partial x}\frac{dx}{dx}+\frac{\partial F}{\partial y}\frac{dy}{dx}=0.$$
2. Since $dx/dx=1$, solve for the slope:

   $$\frac{dy}{dx}=-\frac{F_x}{F_y}\qquad(F_y\neq0).$$

*The mysterious implicit-differentiation rule of Calc I is just the chain rule applied to a level curve.*

<a id="s7"></a>
### Directional derivatives & the gradient

Partials give slopes along the axes. The directional derivative gives the slope along *any* direction — and the gradient packages them all.

**Gradient & directional derivative**

$$\nabla f=\Big\langle \frac{\partial f}{\partial x},\frac{\partial f}{\partial y},\frac{\partial f}{\partial z}\Big\rangle,\qquad D_{\mathbf u}f=\nabla f\cdot\mathbf u\quad(|\mathbf u|=1)$$

*The rate of change of $f$ as you step in unit direction $\mathbf u$ is the gradient projected onto $\mathbf u$.*

> **Concept — three facts that make the gradient indispensable**
>
> (1) $\nabla f$ points in the direction of **steepest ascent**; (2) its magnitude $|\nabla f|$ is that steepest slope; (3) $\nabla f$ is **perpendicular to the level set** through the point. Together these turn a list of partials into a geometric arrow.

**Demonstration — the gradient is the direction of steepest ascent**

1. The slope in unit direction $\mathbf u$ is $D_{\mathbf u}f=\nabla f\cdot\mathbf u$.
2. Write the dot product with the angle $\theta$ between $\nabla f$ and $\mathbf u$:

   $$D_{\mathbf u}f=|\nabla f|\,|\mathbf u|\cos\theta=|\nabla f|\cos\theta.$$
3. This is maximized when $\cos\theta=1$, i.e. $\theta=0$: $\mathbf u$ points the same way as $\nabla f$. The maximum value is $|\nabla f|$; the minimum, $-|\nabla f|$, is the opposite direction (steepest descent); $\theta=90^\circ$ gives $0$.

*Hence the gradient points uphill fastest, with steepness $|\nabla f|$ — and the zero-rate directions are exactly along the level set, proving $\nabla f\perp$ level set.*

> **Connection — perpendicular to the level set**
>
> Along a level curve $f$ does not change, so $D_{\mathbf u}f=0$ for $\mathbf u$ tangent to it, forcing $\nabla f\perp\mathbf u$. This is why $\nabla F$ is the normal to a surface $F=k$ (Section 8) and why gradients align at a constrained optimum (Lagrange, Section 11).

<a id="s8"></a>
### Tangent planes, linear approximation & differentials

*Zoom into a smooth surface and it looks flat. That flat approximation is the tangent plane — the multivariable version of the tangent line.*

**Tangent plane & linearization of $z=f(x,y)$**

$$z=f(a,b)+f_x(a,b)(x-a)+f_y(a,b)(y-b)$$

$$L(x,y)=f(a,b)+\nabla f(a,b)\cdot\langle x-a,\,y-b\rangle$$

*Same shape as $y=f(a)+f'(a)(x-a)$: value plus slope times displacement, now with the gradient supplying the slope in both directions.*

**Tangent plane to a level surface $F(x,y,z)=k$**

$$\nabla F(P)\cdot\langle x-x_0,\,y-y_0,\,z-z_0\rangle=0$$

*Because $\nabla F$ is the surface normal (Section 7), the tangent plane is "point + plane perpendicular to the gradient."*

**Total differential**

$$df=f_x\,dx+f_y\,dy+f_z\,dz$$

*A first-order estimate of how the output changes for small input nudges — the workhorse for error propagation.*

> **Connection — differentiability is more than partials existing**
>
> A function is **differentiable** at a point if the tangent plane genuinely approximates it (the error vanishes faster than the distance). Having both partials is *not* enough; but if the partials are *continuous* near the point, differentiability is guaranteed — the practical test you will almost always use.

<a id="s9"></a>
### Higher-order partials & Clairaut's theorem

*Differentiate twice and the order can matter — except, remarkably, it usually doesn't. The mixed partials are equal whenever they are continuous.*

**Second partials & Clairaut's theorem**

$$f_{xx}=\partial_x\partial_x f,\quad f_{xy}=\partial_y\partial_x f,\quad f_{yx}=\partial_x\partial_y f$$

$$\text{If }f_{xy},f_{yx}\text{ are continuous near }(a,b),\ \text{then } f_{xy}(a,b)=f_{yx}(a,b).$$

**Demonstration — why $f_{xy}=f_{yx}$**

1. Form the second difference quotient that mixes both directions:

   $$\Delta=\frac{f(a+h,b+k)-f(a+h,b)-f(a,b+k)+f(a,b)}{hk}.$$
2. Group as a difference in $x$ first: let $g(x)=f(x,b+k)-f(x,b)$. Then the numerator is $g(a+h)-g(a)$. By the Mean Value Theorem it equals $h\,g'(\xi)=h\big(f_x(\xi,b+k)-f_x(\xi,b)\big)$ for some $\xi$ between $a$ and $a+h$.
3. Apply the MVT again in $y$ to $f_x(\xi,\cdot)$: the bracket equals $k\,f_{xy}(\xi,\eta)$. So $\Delta=f_{xy}(\xi,\eta)$. Symmetrically, grouping in $y$ first gives $\Delta=f_{yx}(\xi',\eta')$.
4. Let $h,k\to0$: both $(\xi,\eta)$ and $(\xi',\eta')\to(a,b)$, and by continuity

   $$f_{xy}(a,b)=\lim\Delta=f_{yx}(a,b).$$

*Equal mixed partials is exactly the condition behind exact differentials and conservative fields (Section 20).*

<a id="s10"></a>
### Local extrema & the second-derivative test

*Hills and valleys occur where the surface is level — where the gradient vanishes. A second-derivative test sorts peaks from passes.*

**Critical points & the second-derivative test**

$$\nabla f=\mathbf 0\ \Rightarrow\ \text{critical point};\qquad D=f_{xx}f_{yy}-f_{xy}^{\,2}$$

*$D>0,\ f_{xx}>0\Rightarrow$ local min; $D>0,\ f_{xx}<0\Rightarrow$ local max; $D<0\Rightarrow$ saddle; $D=0\Rightarrow$ inconclusive.*

> **Concept — why $D$ is a determinant**
>
> $D$ is the determinant of the **Hessian** $\begin{pmatrix}f_{xx}&f_{xy}\\ f_{xy}&f_{yy}\end{pmatrix}$. Near a critical point $f$ looks like a quadratic form; the Hessian's eigenvalues give the curvatures along the principal axes. Both positive → bowl (min); both negative → dome (max); opposite signs → saddle. The sign of $D$ (product of eigenvalues) and of $f_{xx}$ recover exactly those cases.

> **Connection — Calc I, upgraded**
>
> In one variable: $f'=0$ then check $f''$. Here $\nabla f=\mathbf 0$ replaces $f'=0$, and the Hessian determinant replaces the single $f''$. The logic — find flat spots, then probe curvature — is identical.

<a id="s11"></a>
### Lagrange multipliers (constrained optimization)

*To optimize $f$ subject to a constraint $g=c$, you cannot just set $\nabla f=\mathbf 0$. The constraint pins you to a curve or surface — and the answer is where the gradients line up.*

**Lagrange condition**

$$\nabla f=\lambda\,\nabla g,\qquad g(x,y,\dots)=c$$

*Solve this system for the variables and the multiplier $\lambda$. With two constraints: $\nabla f=\lambda\nabla g+\mu\nabla h$.*

**Demonstration — why the gradients must be parallel**

1. The constraint $g=c$ confines you to its level set. Parametrize a path $\mathbf r(t)$ lying in that set, passing through a constrained extremum at $t_0$.
2. Along the path $f(\mathbf r(t))$ has an ordinary extremum at $t_0$, so its derivative vanishes there:

   $$\frac{d}{dt}f(\mathbf r(t))\Big|_{t_0}=\nabla f\cdot\mathbf r'(t_0)=0.$$
3. Thus $\nabla f\perp\mathbf r'(t_0)$ for every path in the constraint set — i.e. $\nabla f\perp$ the constraint surface. But $\nabla g$ is also $\perp$ that surface (Section 7).
4. Two vectors perpendicular to the same surface are parallel:

   $$\nabla f=\lambda\,\nabla g.$$

*At a constrained optimum the level curves of $f$ are tangent to the constraint — they kiss, sharing a normal. The multiplier $\lambda$ measures the sensitivity of the optimum to the constraint level $c$.*

## Part C · Multiple integrals

<a id="s12"></a>
### Double integrals over rectangles & general regions

*A double integral adds up a function over a 2D region — the volume under a surface. Fubini's theorem lets you compute it one variable at a time.*

**Definition & Fubini's theorem**

$$\iint_R f\,dA=\lim_{\|P\|\to0}\sum_{i,j} f(x_i^*,y_j^*)\,\Delta A=\int_a^b\!\!\int_c^d f(x,y)\,dy\,dx$$

*Over a rectangle the order of integration is free. The double integral is a limit of Riemann sums of little boxes $f\cdot\Delta A$.*

**General (Type I / Type II) regions**

$$\iint_D f\,dA=\int_a^b\!\!\int_{g_1(x)}^{g_2(x)} f\,dy\,dx=\int_c^d\!\!\int_{h_1(y)}^{h_2(y)} f\,dx\,dy$$

*The inner limits describe the region (functions); the outer limits are constants. Sketch the region first — it dictates the bounds and often which order is tractable.*

> **Principle — reversing the order of integration**
>
> An iterated integral that is impossible in one order can be elementary in the other. The technique: from the bounds, reconstruct the *region*, then re-describe it with the variables swapped. The region is the invariant; the bounds are just one way of slicing it.

> **Connection — iterating single integrals**
>
> A double integral is just a definite integral whose integrand is itself a definite integral. Everything you know about $\int$ carries over; the only new skill is translating a 2D region into nested limits.

<a id="s13"></a>
### Double integrals in polar coordinates

*Circles and disks are nightmares in $x,y$ but trivial in $r,\theta$. The only catch — and it is the heart of the matter — is the area element gains a factor of $r$.*

**Polar double integral**

$$x=r\cos\theta,\quad y=r\sin\theta,\qquad \iint_D f\,dA=\iint_D f(r\cos\theta,r\sin\theta)\,\underbrace{r\,dr\,d\theta}_{dA}$$

*The $r$ is not optional — forgetting it is the classic error. It is the Jacobian of the polar map (Section 16).*

**Demonstration — why $dA=r\,dr\,d\theta$**

1. Partition the region with rays $\theta=\text{const}$ and circles $r=\text{const}$. A typical "polar rectangle" spans angle $\Delta\theta$ and radius $\Delta r$, at radius $r$.
2. Its two curved sides are circular arcs. The outer arc has length $r\,\Delta\theta$; the radial side has length $\Delta r$. For small increments the patch is nearly a rectangle:

   $$\Delta A\approx(\text{arc length})\times(\text{radial width})=(r\,\Delta\theta)(\Delta r).$$
3. (Exactly: the area between radii $r$ and $r+\Delta r$ over angle $\Delta\theta$ is $\tfrac12\big((r+\Delta r)^2-r^2\big)\Delta\theta=\big(r+\tfrac12\Delta r\big)\Delta r\,\Delta\theta\to r\,\Delta r\,\Delta\theta$.)
4. Taking the limit, $dA=r\,dr\,d\theta$.

*Patches far from the origin are wider for the same $\Delta\theta$; the factor $r$ accounts for that fanning out.*

> **Connection — the Gaussian integral**
>
> Polar coordinates crack $\int_{-\infty}^{\infty}e^{-x^2}dx=\sqrt\pi$: square it into a double integral over the plane, convert to polar, and the stubborn $e^{-r^2}\,r\,dr$ integrates by elementary substitution — the $r$ from $dA$ is exactly what makes it work.

<a id="s14"></a>
### Triple integrals

*One more dimension: integrate over a solid. The picture and the bookkeeping extend directly from double integrals.*

**Triple integral & volume**

$$\iiint_E f\,dV=\int\!\!\int\!\!\int f(x,y,z)\,dz\,dy\,dx,\qquad \text{Vol}(E)=\iiint_E 1\,dV$$

*Innermost limits may depend on the two outer variables; the middle on the outermost; the outermost are constants.*

> **Principle — set up by projecting and slicing**
>
> Describe the solid as: a 2D **shadow** $D$ in one coordinate plane, with $z$ running between a lower surface $z=u_1(x,y)$ and an upper surface $z=u_2(x,y)$. Integrate $z$ first (a single integral for each $(x,y)$), then handle $D$ as a double integral — possibly in polar.

> **Connection — same skill, more limits**
>
> A triple integral is a double integral of a single integral. Mastery is entirely about translating a 3D solid into nested bounds — the calculus is the elementary integration you already do.

<a id="s15"></a>
### Cylindrical & spherical coordinates

*Solids with axial or central symmetry beg for coordinates that respect that symmetry. Each brings its own volume element.*

**Cylindrical coordinates**

$$x=r\cos\theta,\ y=r\sin\theta,\ z=z,\qquad dV=r\,dz\,dr\,d\theta$$

*Polar in the $xy$-plane, ordinary $z$ on top. Ideal for cylinders, cones, paraboloids.*

**Spherical coordinates**

$$x=\rho\sin\phi\cos\theta,\ y=\rho\sin\phi\sin\theta,\ z=\rho\cos\phi,\qquad dV=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$$

*$\rho\ge0$ is distance from origin, $\phi\in[0,\pi]$ the angle from the $+z$-axis, $\theta\in[0,2\pi)$ the longitude. Ideal for spheres and cones.*

**Demonstration — the spherical volume element $\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$**

1. Increase $\rho$ by $d\rho$: the radial edge has length $d\rho$.
2. Increase $\phi$ by $d\phi$: the point sweeps an arc on a circle of radius $\rho$ (a meridian), of length $\rho\,d\phi$.
3. Increase $\theta$ by $d\theta$: the point sweeps a circle of latitude whose radius is $\rho\sin\phi$ (distance from the $z$-axis), giving arc length $\rho\sin\phi\,d\theta$.
4. The three edges are mutually perpendicular, so the box volume is their product:

   $$dV=(d\rho)(\rho\,d\phi)(\rho\sin\phi\,d\theta)=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta.$$

*The $\rho^2$ is the surface-area growth of spheres; the $\sin\phi$ is the shrinking of latitude circles toward the poles. Both fall straight out of the Jacobian (Section 16).*

<a id="s16"></a>
### Change of variables & the Jacobian

*Polar, cylindrical and spherical are special cases of one principle: change coordinates with a smooth map, and the volume element scales by the determinant of its derivative.*

**Change of variables & the Jacobian**

$$\iint_R f\,dx\,dy=\iint_S f\big(x(u,v),y(u,v)\big)\,\Big|\frac{\partial(x,y)}{\partial(u,v)}\Big|\,du\,dv$$

$$\frac{\partial(x,y)}{\partial(u,v)}=\det\!\begin{pmatrix} x_u & x_v\\ y_u & y_v\end{pmatrix}$$

*The Jacobian determinant is the local area-stretch factor of the transformation. In $n$ dimensions it is an $n\times n$ determinant.*

**Demonstration — the polar Jacobian recovers the $r$**

1. With $x=r\cos\theta,\ y=r\sin\theta$, compute the partials:

   $$x_r=\cos\theta,\ x_\theta=-r\sin\theta,\ y_r=\sin\theta,\ y_\theta=r\cos\theta.$$
2. Form the Jacobian determinant:

   $$\frac{\partial(x,y)}{\partial(r,\theta)}=\det\!\begin{pmatrix}\cos\theta & -r\sin\theta\\ \sin\theta & r\cos\theta\end{pmatrix}=r\cos^2\theta+r\sin^2\theta=r.$$
3. Therefore $dx\,dy=|r|\,dr\,d\theta=r\,dr\,d\theta$, exactly the polar element of Section 13.

*Every special volume element in this part is one determinant. The same computation in spherical yields $\rho^2\sin\phi$.*

> **Concept — why a determinant?**
>
> The derivative of the coordinate map is a matrix (the Jacobian matrix); it sends a tiny coordinate box to a tiny parallelepiped. The **determinant** is precisely the factor by which a linear map scales volume (Section 1's triple product). So the absolute Jacobian determinant is the local volume-conversion rate.

<a id="s17"></a>
### Applications: mass, moments & center of mass

*Multiple integrals compute physical totals from a density. The pattern is always: integrate the density to get the whole, integrate density-times-position to find where it balances.*

**Mass, moments, centroid**

$$m=\iint_D \rho\,dA,\qquad M_y=\iint_D x\,\rho\,dA,\quad M_x=\iint_D y\,\rho\,dA$$

$$\bar x=\frac{M_y}{m},\qquad \bar y=\frac{M_x}{m}$$

*The 3D versions integrate over a solid with $dV$. With constant density the center of mass is the purely geometric **centroid**.*

**Moment of inertia**

$$I_x=\iint_D y^2\rho\,dA,\quad I_y=\iint_D x^2\rho\,dA,\quad I_0=\iint_D (x^2+y^2)\rho\,dA$$

*Inertia weights mass by the *square* of distance from the axis — why mass far from the axis resists rotation so strongly.*

> **Connection — the recurring template**
>
> Total = $\int(\text{density})$; average position = $\frac{\int(\text{position})(\text{density})}{\int(\text{density})}$. The same template gives probability (density integrates to 1, mean = $\int x f\,dx$) — the bridge to the statistics companion.

## Part D · Vector calculus

<a id="s18"></a>
### Vector fields

*A vector field attaches an arrow to every point of space — wind velocity, a force, an electric field. Calculus on these fields is the climax of the course.*

**Vector field & gradient field**

$$\mathbf F(x,y,z)=\langle P,\,Q,\,R\rangle,\qquad \mathbf F=\nabla f\ \Rightarrow\ \mathbf F \text{ is a gradient (conservative) field}$$

*$f$ is then a **potential** for $\mathbf F$. Gravity and electrostatics are gradient fields.*

> **Concept — read a field by its flow**
>
> Imagine the field as the velocity of a fluid. Two questions organize everything that follows: along a curve, how much does the flow *push you* (circulation, line integrals); across a boundary, how much flow *passes through* (flux, surface integrals). Curl measures local spin; divergence measures local source/sink.

<a id="s19"></a>
### Line integrals (scalar & vector); work

*Integrate along a curve. For a scalar, you sum a quantity weighted by arc length; for a field, you sum its component along the path — the work it does.*

**Scalar & vector line integrals**

$$\int_C f\,ds=\int_a^b f(\mathbf r(t))\,|\mathbf r'(t)|\,dt$$

$$\int_C \mathbf F\cdot d\mathbf r=\int_a^b \mathbf F(\mathbf r(t))\cdot\mathbf r'(t)\,dt=\int_C P\,dx+Q\,dy+R\,dz$$

*$ds=|\mathbf r'|\,dt$ is arc length; $d\mathbf r=\mathbf r'\,dt$ is the directed step. The vector integral is the work done by $\mathbf F$ along $C$.*

> **Concept — scalar vs. vector line integral**
>
> The **scalar** integral $\int_C f\,ds$ is independent of direction (it weights by length — think mass of a wire). The **vector** integral $\int_C\mathbf F\cdot d\mathbf r$ reverses sign if you reverse the curve, because it measures directed push. Work and circulation are vector line integrals.

> **Connection — projecting onto the tangent**
>
> $\mathbf F\cdot d\mathbf r=(\mathbf F\cdot\mathbf T)\,ds$: the work integral is the scalar integral of the tangential component $\mathbf F\cdot\mathbf T$. This tangential view becomes the left side of Green's and Stokes' theorems (circulation).

<a id="s20"></a>
### The Fundamental Theorem for line integrals & conservative fields

*For a gradient field, a line integral depends only on the endpoints — not the path. This is the FTC itself, lifted to curves in space.*

**Fundamental Theorem for line integrals**

$$\int_C \nabla f\cdot d\mathbf r=f(\mathbf r(b))-f(\mathbf r(a))$$

*Path-independent; around a closed loop it is $0$. Such $\mathbf F=\nabla f$ is **conservative**.*

**Test for conservative fields (simply connected domain)**

$$\mathbf F=\langle P,Q\rangle \text{ conservative}\iff \frac{\partial P}{\partial y}=\frac{\partial Q}{\partial x}\quad\big(\text{in 3D: }\nabla\times\mathbf F=\mathbf 0\big)$$

*The cross-partial test is Clairaut's theorem (Section 9) in disguise: if $\mathbf F=\nabla f$ then $P_y=f_{xy}=f_{yx}=Q_x$.*

**Demonstration — proving the FTC for line integrals**

1. Let $\mathbf F=\nabla f$ and parametrize $C$ by $\mathbf r(t),\ a\le t\le b$. Then

   $$\int_C\nabla f\cdot d\mathbf r=\int_a^b\nabla f(\mathbf r(t))\cdot\mathbf r'(t)\,dt.$$
2. By the multivariable chain rule (Section 6), the integrand is a total derivative:

   $$\nabla f(\mathbf r(t))\cdot\mathbf r'(t)=\frac{d}{dt}\,f(\mathbf r(t)).$$
3. Now it is an ordinary single-variable integral; apply the classical FTC:

   $$\int_a^b\frac{d}{dt}f(\mathbf r(t))\,dt=f(\mathbf r(b))-f(\mathbf r(a)).$$

*The gradient is the multivariable derivative; integrating it recovers the function at the boundary points — the first instance of the boundary principle of Section 27.*

<a id="s21"></a>
### Green's theorem

*The first of the great theorems: circulation of a field around a closed plane curve equals the integral of its (scalar) curl over the enclosed region.*

**Green's theorem (circulation form)**

$$\oint_C P\,dx+Q\,dy=\iint_D\Big(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\Big)\,dA$$

*$C$ is the positively oriented (counterclockwise) boundary of region $D$. The integrand on the right is the 2D scalar curl.*

**Two consequences**

$$\text{Area}(D)=\oint_C x\,dy=-\oint_C y\,dx=\tfrac12\oint_C x\,dy-y\,dx$$

$$\text{Flux form: }\ \oint_C \mathbf F\cdot\mathbf n\,ds=\iint_D \Big(\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}\Big)\,dA$$

*The circulation form is the 2D Stokes' theorem; the flux form is the 2D Divergence theorem. One theorem, two readings.*

**Demonstration — Green's theorem on a Type I/II region**

1. Prove the $P$ piece. For a Type I region $D=\{a\le x\le b,\ g_1(x)\le y\le g_2(x)\}$, integrate the curl term over $D$:

   $$\iint_D \!-\frac{\partial P}{\partial y}\,dA=-\int_a^b\!\!\int_{g_1}^{g_2}\frac{\partial P}{\partial y}\,dy\,dx.$$
2. Do the inner integral by the FTC:

   $$=-\int_a^b\big[P(x,g_2(x))-P(x,g_1(x))\big]\,dx.$$
3. Now compute $\oint_C P\,dx$ directly. The top boundary (right→left) contributes $-\int_a^b P(x,g_2)\,dx$; the bottom (left→right) contributes $+\int_a^b P(x,g_1)\,dx$; the vertical sides have $dx=0$. Summing matches step 2:

   $$\oint_C P\,dx=\iint_D\!-\frac{\partial P}{\partial y}\,dA.$$
4. Symmetrically, viewing $D$ as Type II gives $\oint_C Q\,dy=\iint_D \frac{\partial Q}{\partial x}\,dA$. Add the two.

*A general region is glued from such pieces; the interior boundaries cancel in pairs, leaving only the outer curve. This cancellation is the engine behind every theorem in Part D.*

<a id="s22"></a>
### Curl & divergence

*Two derivative operators on a vector field. Curl measures microscopic rotation; divergence measures net outflow. They are the integrands of Stokes and Gauss.*

**Curl & divergence via $\nabla$**

$$\nabla\times\mathbf F=\begin{vmatrix}\mathbf i&\mathbf j&\mathbf k\\ \partial_x&\partial_y&\partial_z\\ P&Q&R\end{vmatrix},\qquad \nabla\cdot\mathbf F=\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}$$

*Curl returns a vector (axis of spin); divergence returns a scalar (source strength).*

**Two identities that organize everything**

$$\nabla\times(\nabla f)=\mathbf 0,\qquad \nabla\cdot(\nabla\times\mathbf F)=0$$

*"Curl of a gradient is zero" (gradient fields are irrotational); "divergence of a curl is zero" (curl fields are sourceless). Both are Clairaut's theorem in vector dress.*

> **Concept — the physical meaning**
>
> Drop a tiny paddlewheel in the flow: it spins about the axis $\nabla\times\mathbf F$, at a rate set by $|\nabla\times\mathbf F|$. Enclose a tiny ball: $\nabla\cdot\mathbf F$ is the net flux out per unit volume — positive at a source, negative at a sink. These local readings become the global theorems when integrated.

**Demonstration — curl of a gradient vanishes**

1. Take $\mathbf F=\nabla f=\langle f_x,f_y,f_z\rangle$. The $\mathbf k$-component of $\nabla\times\mathbf F$ is

   $$\partial_x(f_y)-\partial_y(f_x)=f_{yx}-f_{xy}.$$
2. By Clairaut (Section 9), $f_{xy}=f_{yx}$, so this component is $0$; the same cancellation kills the $\mathbf i$- and $\mathbf j$-components.

*Hence conservative $\Rightarrow$ irrotational — the 3D version of the $P_y=Q_x$ test of Section 20.*

<a id="s23"></a>
### Parametric surfaces & surface area

*Just as a curve is one parameter, a surface is two. The cross product of the two tangent vectors gives the normal — and the area element.*

**Parametrization, normal, surface area**

$$\mathbf r(u,v)=\langle x,y,z\rangle,\qquad \mathbf r_u\times\mathbf r_v=\text{normal},\qquad dS=|\mathbf r_u\times\mathbf r_v|\,du\,dv$$

$$A(S)=\iint_D |\mathbf r_u\times\mathbf r_v|\,dA$$

*For a graph $z=g(x,y)$: $dS=\sqrt{1+g_x^2+g_y^2}\,dA$.*

**Demonstration — the surface-area element $dS=|\mathbf r_u\times\mathbf r_v|\,du\,dv$**

1. A small parameter rectangle $[u,u+du]\times[v,v+dv]$ maps to a curved patch on $S$. Its two edges are approximately the tangent vectors scaled: $\mathbf r_u\,du$ and $\mathbf r_v\,dv$.
2. The patch is nearly the parallelogram spanned by these edges. Its area is the magnitude of their cross product (Section 1):

   $$dS=|\mathbf r_u\,du\times\mathbf r_v\,dv|=|\mathbf r_u\times\mathbf r_v|\,du\,dv.$$

*The cross product does double duty: its direction is the surface normal (needed for flux), its magnitude is the area scale.*

<a id="s24"></a>
### Surface integrals & flux

*Integrate over a surface. For a scalar, weight by area; for a field, sum the component crossing the surface — the flux.*

**Scalar surface integral & flux**

$$\iint_S f\,dS=\iint_D f(\mathbf r(u,v))\,|\mathbf r_u\times\mathbf r_v|\,dA$$

$$\iint_S \mathbf F\cdot d\mathbf S=\iint_S \mathbf F\cdot\mathbf n\,dS=\iint_D \mathbf F\cdot(\mathbf r_u\times\mathbf r_v)\,dA$$

*$d\mathbf S=\mathbf n\,dS=(\mathbf r_u\times\mathbf r_v)\,dA$. Flux measures how much of $\mathbf F$ passes through $S$ per unit time.*

> **Concept — orientation matters**
>
> A flux integral needs a chosen side: an **orientation**, given by a continuous unit normal $\mathbf n$. Flipping $\mathbf n$ flips the sign. For a closed surface the convention is the *outward* normal. (A Möbius band is non-orientable — no consistent choice exists.)

> **Connection — the parallel with line integrals**
>
> Scalar surface integral ↔ scalar line integral (weight by measure); flux $\iint\mathbf F\cdot\mathbf n\,dS$ ↔ circulation $\int\mathbf F\cdot\mathbf T\,ds$. Curves use the tangent; surfaces use the normal. Stokes (Section 25) and Gauss (Section 26) tie these together.

<a id="s25"></a>
### Stokes' theorem

*Green's theorem, lifted off the plane. Circulation around the boundary curve of a surface equals the flux of the curl through the surface.*

**Stokes' theorem**

$$\oint_{\partial S} \mathbf F\cdot d\mathbf r=\iint_S (\nabla\times\mathbf F)\cdot d\mathbf S$$

*$\partial S$ is the boundary curve of $S$, oriented by the right-hand rule relative to $\mathbf n$. Any surface with the same boundary gives the same answer.*

> **Concept — sum the microscopic spins**
>
> Curl is local circulation per unit area. Tile the surface with tiny loops; on each, circulation $\approx(\nabla\times\mathbf F)\cdot\mathbf n\,dS$. Adjacent loops share edges traversed in *opposite* directions, so all interior contributions cancel — only the outer boundary survives. That cancellation is Green's proof (Section 21), now on a surface.

> **Connection — Green is flat Stokes**
>
> Take $S$ to be a region in the $xy$-plane with $\mathbf n=\mathbf k$. Then $(\nabla\times\mathbf F)\cdot\mathbf k=Q_x-P_y$ and Stokes becomes $\oint P\,dx+Q\,dy=\iint(Q_x-P_y)\,dA$ — Green's theorem exactly.

<a id="s26"></a>
### The Divergence (Gauss) theorem

*The flux of a field out through a closed surface equals the integral of its divergence over the solid inside. Sources inside account for net outflow.*

**Divergence theorem**

$$\oiint_{\partial E} \mathbf F\cdot d\mathbf S=\iiint_E (\nabla\cdot\mathbf F)\,dV$$

*$\partial E$ is the closed boundary surface of solid $E$, with outward normal. Total outflow = total source strength inside.*

> **Concept — telescoping the fluxes**
>
> Divergence is net outflow per unit volume. Chop $E$ into tiny boxes; each contributes $(\nabla\cdot\mathbf F)\,dV$ of outflow. Where two boxes touch, the flux out of one is flux *into* the other — equal and opposite, so it cancels. Only the outer surface remains. Same cancellation principle as Green and Stokes.

> **Connection — Green's flux form is flat Gauss**
>
> In the plane, the Divergence theorem reads $\oint_C\mathbf F\cdot\mathbf n\,ds=\iint_D(P_x+Q_y)\,dA$ — exactly the flux form of Green's theorem (Section 21). Gauss is its 3D upgrade.

## Part E · Synthesis

<a id="s27"></a>
### The unifying picture: one theorem behind them all

*Five theorems — FTC, FTC for line integrals, Green, Stokes, Gauss — are a single statement seen from different dimensions: the integral of a derivative over a region equals the integral of the function over its boundary.*

> **Principle — the generalized Stokes' theorem**
>
> In the language of differential forms, all five collapse to one line: **the integral of $d\omega$ over a region $M$ equals the integral of $\omega$ over the boundary $\partial M$**. Here $d$ is the exterior derivative (which specializes to gradient, curl, divergence) and $\partial$ is "take the boundary." Each classical theorem is this with a particular dimension and operator.

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

1. FTC: $M=[a,b]$, $d\omega=f'\,dx$, and $\int_{\partial M}\omega=f(b)-f(a)$ (endpoints with signs $+,-$). The boundary "integral" of a 0-dimensional set is just evaluation.
2. Line-integral FTC: $M=C$, $\omega=f$, $d\omega=\nabla f\cdot d\mathbf r$; boundary is the two endpoints — Section 20.
3. Green / Stokes: $M$ is 2-dimensional, $d$ produces the curl, $\partial M$ is the bounding curve — circulation = curl flux.
4. Divergence: $M$ is 3-dimensional, $d$ produces the divergence, $\partial M$ is the bounding surface — outflow = source total.

*The recurring proof move is the same every time: tile the region, note interior boundaries cancel in pairs, and only $\partial M$ survives.*

#### The whole of vector calculus on one line

> derivative inside = values on the boundary · $ \displaystyle\int_M d\omega=\int_{\partial M}\omega $

> **The habit to keep**
>
> Whenever you meet a new integral identity, ask the two questions of this course: *what is the region, and what is its boundary?* Behind partial derivatives, multiple integrals, flux and circulation sits one idea — a derivative summed over the inside is the function read off the edge — the Fundamental Theorem of Calculus, all the way up.

---

*A third-semester course in multivariable and vector calculus — concepts, principles, formulas, and the demonstrations behind them — built as a companion to the Statistics and Calculus guides. Read once for the shape; return to any box as a reference. Remember: every great theorem here says the same thing — integrate a derivative over a region, and you get the function back on its boundary.*
