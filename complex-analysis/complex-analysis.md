**English** · [中文](complex-analysis.zh.md)

# Complex Analysis, *where calculus becomes magical.*

*A first rigorous course in the calculus of functions of a complex variable. We start from the algebra of $i$ and build, step by step, to the residue theorem and the spectacular rigidity of holomorphic functions — where knowing a function on a tiny disk determines it everywhere, and a single contour integral collects an entire function's hidden arithmetic.*

[← Back to all guides](../README.md)

## Part A · The complex plane

<a id="s0"></a>
### Complex numbers: algebra, the plane, modulus, argument, polar form, and Euler's formula

Complex analysis begins with one act of invention: we declare that there is a number whose square is $-1$. From that single declaration grows a structure so rich that it makes calculus *simpler*, not harder. This section builds the complex numbers from scratch and proves Euler's formula, the identity that ties exponentials to rotation.

#### What problem are we solving?

The equation $x^2+1=0$ has no real solution, because the square of any real number is $\ge 0$. Rather than accept defeat, we *enlarge* the number system by adjoining a new symbol $i$ obeying the single rule $i^2=-1$. Everything else follows by insisting the ordinary laws of algebra (commutativity, associativity, distributivity) continue to hold.

#### Definition and arithmetic

> **Definition — complex numbers**
>
> A **complex number** is an expression $z = x + iy$ where $x,y$ are real numbers and $i$ is a symbol satisfying $i^2=-1$. We call $x = \mathrm{Re} z$ the **real part** and $y = \mathrm{Im} z$ the **imaginary part** (note: $\mathrm{Im} z$ is the *real number* $y$, not $iy$). The set of all complex numbers is denoted $\mathbb{C}$.

Two complex numbers are **equal** exactly when their real parts agree and their imaginary parts agree. Addition and multiplication are defined by treating $i$ as an ordinary quantity and reducing $i^2$ to $-1$:

$$
(x_1+iy_1)+(x_2+iy_2) = (x_1+x_2) + i(y_1+y_2),
$$

$$
(x_1+iy_1)(x_2+iy_2) = (x_1x_2 - y_1y_2) + i(x_1y_2 + x_2y_1).
$$

The multiplication formula is just distribution: $x_1x_2 + ix_1y_2 + iy_1x_2 + i^2 y_1 y_2$, and $i^2 y_1y_2 = -y_1y_2$ moves into the real part.

> **Worked example — arithmetic**
>
> Let $z_1 = 2+3i$, $z_2 = 1-4i$. Then $z_1+z_2 = 3 - i$. For the product: $(2+3i)(1-4i) = 2\cdot 1 + 2\cdot(-4i) + 3i\cdot 1 + 3i\cdot(-4i) = 2 - 8i + 3i - 12i^2 = 2 - 5i + 12 = 14 - 5i$, using $i^2=-1$ at the last step.

#### The conjugate and modulus

> **Definition — conjugate and modulus**
>
> The **complex conjugate** of $z = x+iy$ is $\bar z = x - iy$. The **modulus** (or absolute value) is $|z| = \sqrt{x^2+y^2}$, a nonnegative real number.

The conjugate is the workhorse of complex arithmetic because it linearizes the modulus:

$$
z\bar z = (x+iy)(x-iy) = x^2 - (iy)^2 = x^2 + y^2 = |z|^2.
$$

This single identity gives division. To divide by $z\ne 0$, multiply numerator and denominator by $\bar z$:

$$
\frac{1}{z} = \frac{\bar z}{z\bar z} = \frac{\bar z}{|z|^2} = \frac{x - iy}{x^2+y^2}.
$$

This is well-defined because $z\ne 0$ means $x^2+y^2 > 0$. With division available, $\mathbb{C}$ is a **field**: every nonzero element has a multiplicative inverse.

> **Worked example — division**
>
> $\dfrac{1}{2+3i} = \dfrac{2-3i}{2^2+3^2} = \dfrac{2-3i}{13} = \dfrac{2}{13} - \dfrac{3}{13}i.$ Check: $(2+3i)\left(\tfrac{2}{13}-\tfrac{3}{13}i\right) = \tfrac{1}{13}(2+3i)(2-3i) = \tfrac{1}{13}(4+9) = 1$. ✓

Two conjugation rules we will reuse, each proved by direct computation: $\overline{z_1+z_2} = \bar z_1 + \bar z_2$ and $\overline{z_1 z_2} = \bar z_1\,\bar z_2$. Also $\mathrm{Re} z = \tfrac12(z+\bar z)$ and $\mathrm{Im} z = \tfrac{1}{2i}(z-\bar z)$.

#### The complex plane

A complex number $z=x+iy$ carries exactly two real numbers, so it corresponds to the point $(x,y)$ in the plane $\mathbb{R}^2$. This picture — the **complex plane** or **Argand plane** — is not decoration; it is the geometric content of the whole subject. Addition is vector addition. The modulus $|z|$ is the distance from $z$ to the origin, and $|z_1 - z_2|$ is the distance between the two points. Conjugation is reflection across the real axis.

The **triangle inequality** holds exactly as in $\mathbb{R}^2$: $|z_1+z_2| \le |z_1|+|z_2|$, geometrically "one side of a triangle is no longer than the sum of the other two." A consequence we will lean on: $\bigl||z_1|-|z_2|\bigr| \le |z_1 - z_2|$.

#### Polar form, argument, and Euler's formula

A point in the plane is also described by its distance $r$ from the origin and the angle $\theta$ its radius makes with the positive real axis.

> **Definition — modulus and argument**
>
> For $z\ne 0$, write $r = |z| = \sqrt{x^2+y^2}$ and let $\theta$ be an angle with $x = r\cos\theta$, $y = r\sin\theta$. Then $z = r(\cos\theta + i\sin\theta)$ is the **polar form**, $r$ is the modulus and $\theta$ is an **argument** of $z$, written $\arg z$. Because $\cos$ and $\sin$ have period $2\pi$, the argument is determined only up to adding integer multiples of $2\pi$; the unique value in $(-\pi,\pi]$ is the **principal argument** $\mathrm{Arg} z$.

Now we derive **Euler's formula**, the identity $e^{i\theta} = \cos\theta + i\sin\theta$. We take as known the real Taylor (Maclaurin) series, which converge for all real arguments (a prerequisite from calculus):

$$
e^{t} = \sum_{n=0}^{\infty}\frac{t^n}{n!}, \qquad \cos t = \sum_{n=0}^{\infty}\frac{(-1)^n t^{2n}}{(2n)!}, \qquad \sin t = \sum_{n=0}^{\infty}\frac{(-1)^n t^{2n+1}}{(2n+1)!}.
$$

**Derivation — Euler's formula via power series**

1. *Define* $e^{i\theta}$ for real $\theta$ by substituting $t = i\theta$ into the exponential series: $e^{i\theta} = \sum_{n=0}^{\infty}\dfrac{(i\theta)^n}{n!}$. This is a definition; we are extending $\exp$ to imaginary inputs. (That the series converges absolutely for every complex input is proved in §s9, so rearranging its terms below is legitimate by the rearrangement theorem for absolutely convergent series.)
2. Compute the powers of $i$: $i^0=1,\ i^1=i,\ i^2=-1,\ i^3=-i,\ i^4=1$, and the cycle of length $4$ repeats. So $i^{2k} = (i^2)^k = (-1)^k$ and $i^{2k+1} = i\cdot(-1)^k$.
3. Split the sum into even index $n=2k$ and odd index $n=2k+1$ (allowed because the series is absolutely convergent, so we may reorder and regroup freely):
$$
e^{i\theta} = \sum_{k=0}^{\infty}\frac{(i\theta)^{2k}}{(2k)!} + \sum_{k=0}^{\infty}\frac{(i\theta)^{2k+1}}{(2k+1)!}.
$$
4. Substitute the power values from step 2: $(i\theta)^{2k} = (-1)^k\theta^{2k}$ and $(i\theta)^{2k+1} = i(-1)^k\theta^{2k+1}$. Thus
$$
e^{i\theta} = \sum_{k=0}^{\infty}\frac{(-1)^k\theta^{2k}}{(2k)!} + i\sum_{k=0}^{\infty}\frac{(-1)^k\theta^{2k+1}}{(2k+1)!}.
$$
5. The first sum is the Maclaurin series for $\cos\theta$ and the second is the series for $\sin\theta$. Therefore $e^{i\theta} = \cos\theta + i\sin\theta$. $\blacksquare$

So **polar form is exponential form**: $z = re^{i\theta}$. Multiplication becomes effortless: $r_1 e^{i\theta_1}\cdot r_2 e^{i\theta_2} = r_1 r_2\, e^{i(\theta_1+\theta_2)}$ — *moduli multiply, arguments add*. This proves **De Moivre's theorem** $(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$ by induction on $n$, since $\left(e^{i\theta}\right)^n = e^{in\theta}$. Setting $\theta = \pi$ gives the famous $e^{i\pi} + 1 = 0$.

> **Worked example — roots of unity**
>
> Solve $z^3 = 1$. Write $1 = e^{i\cdot 0}$, but remember the argument is multivalued: $1 = e^{i\cdot 2\pi k}$ for any integer $k$. Then $z = e^{i 2\pi k/3}$ for $k=0,1,2$ gives the three distinct cube roots: $z_0 = 1$, $z_1 = e^{2\pi i/3} = -\tfrac12 + \tfrac{\sqrt3}{2}i$, $z_2 = e^{4\pi i/3} = -\tfrac12 - \tfrac{\sqrt3}{2}i$. They sit at the corners of an equilateral triangle on the unit circle. This multivaluedness of roots and angles is the seed of branch cuts in §s4.

> **Common pitfalls**
>
> - $\mathrm{Im} z$ is a real number ($y$), not $iy$. - The argument is not a function until you fix a range; $\arg(1) = 0$ and $\arg(1)=2\pi$ are both "true." - There is **no ordering** on $\mathbb{C}$ compatible with arithmetic: "$z_1 < z_2$" is meaningless for non-real complex numbers. Only $|z|$ can be compared.

<a id="s1"></a>
### Functions of a complex variable: limits and continuity in the plane

Once $\mathbb{C}$ is a plane, a function $f:\mathbb{C}\to\mathbb{C}$ is a rule sending each point to another point — secretly a map of the plane to itself. Limits and continuity are defined exactly as in single-variable calculus, but with $|\cdot|$ now meaning *distance in the plane*.

#### What a complex function is

> **Definition — complex function**
>
> Let $D\subseteq\mathbb{C}$. A **function of a complex variable** is a rule $f:D\to\mathbb{C}$ assigning to each $z\in D$ a single value $w=f(z)$. Writing $z = x+iy$ and $f = u+iv$, the single complex equation $w=f(z)$ packages **two** real functions of two real variables: $u(x,y) = \mathrm{Re} f$ and $v(x,y) = \mathrm{Im} f$.

For example $f(z) = z^2 = (x+iy)^2 = (x^2-y^2) + i(2xy)$, so $u = x^2 - y^2$ and $v = 2xy$.

Because the output is also a plane, we cannot draw a graph in the usual sense (that would need four real dimensions). Instead we visualize $f$ as a **transformation**: it deforms regions of the $z$-plane into regions of the $w$-plane.

#### Open sets, neighborhoods, and limits

To speak of limits we need the language of nearness in the plane.

> **Definition — disk, open set, neighborhood**
>
> The **open disk** of radius $\varepsilon>0$ about $z_0$ is $D(z_0,\varepsilon) = \{z : |z-z_0| < \varepsilon\}$. A set $U$ is **open** if every point of $U$ has some disk around it lying entirely in $U$. A **neighborhood** of $z_0$ is any open set containing $z_0$. A **deleted** (punctured) neighborhood removes the center point itself.

> **Definition — limit**
>
> Let $f$ be defined on a deleted neighborhood of $z_0$. We say $\lim_{z\to z_0} f(z) = L$ if: for every $\varepsilon>0$ there exists $\delta>0$ such that $0 < |z - z_0| < \delta \implies |f(z) - L| < \varepsilon$.

The form is identical to the real definition; the crucial difference is that "$z\to z_0$" allows approach from **every direction in the plane** — along any path, straight or spiraling. The limit exists only if all these approaches agree. This is a far stronger demand than the real two-sided limit and is the source of complex analysis's rigidity.

> **Definition — continuity**
>
> $f$ is **continuous at $z_0$** if $z_0$ is in the domain and $\lim_{z\to z_0} f(z) = f(z_0)$. It is continuous on a set if continuous at each of its points.

**Proposition — limit splits into real and imaginary parts.** With $f=u+iv$, $z_0 = x_0+iy_0$, $L = a+ib$: $\lim_{z\to z_0}f(z) = L$ if and only if $\lim_{(x,y)\to(x_0,y_0)} u(x,y) = a$ and $\lim_{(x,y)\to(x_0,y_0)} v(x,y) = b$ (limits of real functions of two variables).

**Proof.**
1. Suppose the complex limit holds. Since $|u - a| \le |f - L|$ and $|v - b| \le |f - L|$ (a real and imaginary part is never larger in absolute value than the whole), any $\delta$ that forces $|f-L|<\varepsilon$ forces both $|u-a|<\varepsilon$ and $|v-b|<\varepsilon$. So both real limits hold.
2. Conversely, suppose both real limits hold. Given $\varepsilon>0$, choose $\delta_1$ for $|u-a|<\varepsilon/2$ and $\delta_2$ for $|v-b|<\varepsilon/2$, and set $\delta=\min(\delta_1,\delta_2)$. By the triangle inequality $|f-L| = |(u-a)+i(v-b)| \le |u-a| + |v-b| < \varepsilon$. So the complex limit holds. $\blacksquare$

This proposition lets us import the algebra-of-limits theorems for free: sums, products, quotients (nonzero denominator) and compositions of continuous complex functions are continuous, exactly as in real calculus, because they hold componentwise.

> **Worked example**
>
> $f(z) = z^2$ is continuous everywhere: $u = x^2-y^2$ and $v = 2xy$ are polynomials in $x,y$, hence continuous, so by the proposition $f$ is continuous. More directly, every polynomial in $z$ and every rational function (away from zeros of the denominator) is continuous.

> **Common pitfall**
>
> A complex limit demands agreement over **all** directions of approach. The function $f(z) = \bar z/z$ (for $z\ne 0$) has no limit at $0$: along the real axis $\bar z/z = 1$, but along the imaginary axis $z=iy$ gives $\bar z/z = -iy/(iy) = -1$. Different directions, different values — no limit.

## Part B · Differentiation and holomorphy

<a id="s2"></a>
### Complex differentiability and the Cauchy–Riemann equations; holomorphic functions

Here is where complex analysis departs dramatically from real calculus. The definition of the derivative looks identical — but because the limit must hold for approach from *every direction*, it secretly imposes a pair of partial differential equations. A complex-differentiable function is a vastly more special object than a real-differentiable one.

#### The definition

> **Definition — complex derivative**
>
> $f$ is **differentiable at $z_0$** if the limit
>
> $$
> f'(z_0) = \lim_{h\to 0}\frac{f(z_0+h) - f(z_0)}{h}
> $$
>
> exists, where $h$ ranges over **complex** numbers approaching $0$. If $f$ is differentiable at every point of an open set $U$, it is called **holomorphic** (or **analytic**, or **regular**) on $U$. A function holomorphic on all of $\mathbb{C}$ is **entire**.

The quotient is a ratio of two complex numbers, and $h$ may approach $0$ along the real axis, the imaginary axis, or any spiral. For the limit to exist, *all* these must give the same answer. We now extract the consequence.

#### Deriving the Cauchy–Riemann equations

> **Theorem — Cauchy–Riemann (necessary conditions)**
>
> If $f = u+iv$ is differentiable at $z_0 = x_0+iy_0$, then the partial derivatives of $u,v$ exist at $(x_0,y_0)$ and satisfy
> $$
> \frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \qquad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}.
> $$
> Moreover $f'(z_0) = u_x + i v_x = v_y - i u_y$.

**Proof.**
1. By hypothesis the limit $f'(z_0) = \lim_{h\to 0}\frac{f(z_0+h)-f(z_0)}{h}$ exists and equals the same value no matter how $h\to 0$. We exploit this by computing the limit along two specific directions and equating the results.
2. **Approach along the real axis.** Let $h = \Delta x$ be real, $\Delta x\to 0$. Then $z_0+h = (x_0+\Delta x) + iy_0$, and
$$
\frac{f(z_0+h)-f(z_0)}{h} = \frac{[u(x_0+\Delta x,y_0)-u(x_0,y_0)] + i[v(x_0+\Delta x,y_0)-v(x_0,y_0)]}{\Delta x}.
$$
As $\Delta x\to 0$ the real and imaginary pieces converge to the *partial* derivatives in $x$ (this is exactly the definition of a partial derivative). So this direction gives $f'(z_0) = u_x(x_0,y_0) + i\,v_x(x_0,y_0)$.
3. **Approach along the imaginary axis.** Let $h = i\,\Delta y$ with $\Delta y$ real, $\Delta y\to 0$. Then $z_0+h = x_0 + i(y_0+\Delta y)$, and dividing by $h = i\Delta y$ (and using $1/i = -i$),
$$
\frac{f(z_0+h)-f(z_0)}{i\Delta y} = \frac{[u(x_0,y_0+\Delta y)-u] + i[v(x_0,y_0+\Delta y)-v]}{i\,\Delta y}.
$$
Multiply numerator and denominator by $-i$: the limit is $\tfrac{1}{i}(u_y + i v_y) = -i\,u_y + v_y$. So this direction gives $f'(z_0) = v_y(x_0,y_0) - i\,u_y(x_0,y_0)$.
4. Since the derivative is a single number, the two expressions must be equal:
$$
u_x + i v_x = v_y - i u_y.
$$
Equate real parts: $u_x = v_y$. Equate imaginary parts: $v_x = -u_y$, i.e. $u_y = -v_x$. These are the Cauchy–Riemann equations. The two formulas for $f'$ follow from steps 2 and 3. $\blacksquare$

The Cauchy–Riemann (CR) equations are necessary but, by themselves, not quite sufficient. The clean sufficient condition is:

> **Theorem — Cauchy–Riemann (sufficient conditions)**
>
> If $u,v$ have **continuous** first partial derivatives in a neighborhood of $(x_0,y_0)$ and satisfy the CR equations there, then $f=u+iv$ is differentiable at $z_0$, with $f'(z_0) = u_x + i v_x$.

**Proof.**
1. Continuity of the partials lets us use the **increment formula** from multivariable calculus: for small real increments $\Delta x,\Delta y$,
$$
\Delta u = u_x\,\Delta x + u_y\,\Delta y + \varepsilon_1, \qquad \Delta v = v_x\,\Delta x + v_y\,\Delta y + \varepsilon_2,
$$
where the error terms satisfy $\varepsilon_j/|h|\to 0$ as $h = \Delta x + i\Delta y\to 0$. (This differentiability-from-continuous-partials fact is the prerequisite we restate here.)
2. Combine: $\Delta f = \Delta u + i\Delta v = (u_x\Delta x + u_y\Delta y) + i(v_x\Delta x + v_y\Delta y) + (\varepsilon_1 + i\varepsilon_2)$.
3. Now use the CR equations to replace $u_y = -v_x$ and $v_y = u_x$. Group the terms:
$$
\Delta f = (u_x\Delta x - v_x\Delta y) + i(v_x\Delta x + u_x\Delta y) + (\varepsilon_1+i\varepsilon_2).
$$
4. The main part factors. Observe $(u_x + i v_x)(\Delta x + i\Delta y) = (u_x\Delta x - v_x\Delta y) + i(v_x\Delta x + u_x\Delta y)$ — exactly the grouped terms. So $\Delta f = (u_x + i v_x)\,h + (\varepsilon_1+i\varepsilon_2)$ where $h = \Delta x + i\Delta y$.
5. Divide by $h$ and let $h\to 0$: $\frac{\Delta f}{h} = (u_x + i v_x) + \frac{\varepsilon_1+i\varepsilon_2}{h}$. The error term has modulus $\le (|\varepsilon_1|+|\varepsilon_2|)/|h|\to 0$ by step 1. Hence the limit exists and equals $u_x + i v_x$. $\blacksquare$

> **Worked example**
>
> $f(z) = z^2$: $u = x^2-y^2$, $v=2xy$. Then $u_x = 2x = v_y$ ✓ and $u_y = -2y = -v_x$ ✓ everywhere, with continuous partials, so $f$ is entire and $f'(z) = u_x + iv_x = 2x + i\,2y = 2(x+iy) = 2z$ — the expected power rule. Contrast $g(z) = \bar z$: $u=x,\ v=-y$, so $u_x = 1$ but $v_y = -1$; the CR equations fail everywhere, and $\bar z$ is **nowhere** differentiable despite being perfectly smooth as a real map.

> **Intuition and the $\bar z$ test**
>
> Define $\partial/\partial\bar z = \tfrac12(\partial_x + i\partial_y)$. A short computation shows the CR equations are equivalent to $\partial f/\partial\bar z = 0$. The slogan: *holomorphic functions are those that depend on $z$ only, not on $\bar z$.* Any honest appearance of $\bar z$, $|z|$, $\mathrm{Re} z$, or $\mathrm{Im} z$ in a formula is a warning that the function is probably not holomorphic.

<a id="s3"></a>
### Harmonic functions, the link to holomorphy, and the conformal property

Holomorphy has two beautiful geometric shadows: its real and imaginary parts are **harmonic** (they solve Laplace's equation, the master equation of steady-state physics), and the map it defines **preserves angles**. Both follow from the Cauchy–Riemann equations.

#### Harmonic functions

> **Definition — harmonic**
>
> A real function $\phi(x,y)$ with continuous second partial derivatives is **harmonic** on an open set if it satisfies **Laplace's equation** $\phi_{xx} + \phi_{yy} = 0$. The operator $\Delta = \partial_{xx} + \partial_{yy}$ is the **Laplacian**.

Laplace's equation governs steady-state temperature, electrostatic potential in charge-free regions, and incompressible irrotational fluid flow — which is precisely why complex analysis is a physicist's tool.

> **Theorem — real and imaginary parts of a holomorphic function are harmonic**
>
> If $f = u+iv$ is holomorphic and $u,v$ have continuous second partials (proved automatic in §s7), then $u$ and $v$ are harmonic.

**Proof.**
1. Start from the CR equations $u_x = v_y$ and $u_y = -v_x$.
2. Differentiate the first with respect to $x$: $u_{xx} = v_{yx}$ (differentiating $v_y$ in $x$).
3. Differentiate the second with respect to $y$: $u_{yy} = -v_{xy}$.
4. Add steps 2 and 3: $u_{xx} + u_{yy} = v_{yx} - v_{xy}$.
5. By **Clairaut's theorem** (equality of mixed partials when they are continuous), $v_{yx} = v_{xy}$. Hence $u_{xx}+u_{yy} = 0$; $u$ is harmonic.
6. The same argument applied symmetrically (differentiate $u_x=v_y$ in $y$, and $u_y=-v_x$ in $x$, then subtract) gives $v_{xx}+v_{yy}=0$; $v$ is harmonic. $\blacksquare$

We call $v$ a **harmonic conjugate** of $u$. Given a harmonic $u$ on a simply connected region, one can *construct* a conjugate $v$ by integrating the CR equations, recovering a holomorphic $f$.

> **Worked example — constructing a conjugate**
>
> Let $u = x^2 - y^2$. Check harmonic: $u_{xx} = 2$, $u_{yy} = -2$, sum $0$ ✓. Find $v$: CR says $v_y = u_x = 2x$, so integrating in $y$, $v = 2xy + g(x)$. Then $v_x = 2y + g'(x)$, and CR says $v_x = -u_y = 2y$, forcing $g'(x)=0$, so $g$ is constant. Thus $v = 2xy + C$ and $f = (x^2-y^2) + i\,2xy = z^2$, as expected.

#### The conformal property

> **Definition — conformal**
>
> A map is **conformal** at a point if it preserves the angle between any two smooth curves crossing there, including the sense (orientation) of the angle.

> **Theorem — holomorphic maps are conformal where $f'\ne 0$**
>
> If $f$ is holomorphic at $z_0$ and $f'(z_0)\ne 0$, then $f$ preserves angles at $z_0$.

**Proof.**
1. Let a smooth curve through $z_0$ be $z(t)$ with $z(0)=z_0$ and tangent (velocity) $z'(0)\ne 0$. Its image is $w(t) = f(z(t))$, with tangent, by the chain rule (valid for holomorphic $f$, proved like the real chain rule), $w'(0) = f'(z_0)\,z'(0)$.
2. A complex number's **argument** is the angle its vector makes. So the direction of the image tangent is $\arg w'(0) = \arg f'(z_0) + \arg z'(0)$, using "arguments add under multiplication" (§s0). The image tangent is the original tangent **rotated by the fixed angle $\arg f'(z_0)$** (and scaled by $|f'(z_0)|$).
3. Take two curves through $z_0$ with tangents $z_1'(0), z_2'(0)$. The angle between them is $\arg z_2'(0) - \arg z_1'(0)$. After the map, the tangents are each rotated by the *same* angle $\arg f'(z_0)$, so the difference of arguments is unchanged: $\arg w_2'(0) - \arg w_1'(0) = \arg z_2'(0) - \arg z_1'(0)$.
4. The angle between the images equals the angle between the originals, with the same orientation. The map is conformal. $\blacksquare$

The condition $f'(z_0)\ne 0$ is essential: at $f(z)=z^2$ near $0$, where $f'(0)=0$, angles are **doubled**, not preserved. We return to conformal mapping as a design tool in §s14.

<a id="s4"></a>
### Elementary functions: exp, log, complex powers, trig and hyperbolic; multivaluedness and branch cuts

We now extend the familiar functions to $\mathbb{C}$. The exponential leads the way; everything else is built from it. The new phenomenon is **multivaluedness**: the logarithm and powers naturally take several values at once, and taming them requires cutting the plane.

#### The complex exponential

> **Definition — complex exponential**
>
> For $z = x+iy$, define $e^z = e^x(\cos y + i\sin y)$, i.e. $e^z = e^x e^{iy}$ using Euler's formula (§s0).

This is the unique entire function agreeing with $e^x$ on the real axis and satisfying $(e^z)' = e^z$. Two key properties:
- **Additivity:** $e^{z_1+z_2} = e^{z_1}e^{z_2}$, from the real exponential law plus "arguments add."
- **Periodicity:** $e^{z+2\pi i} = e^z$, because $e^{iy}$ has period $2\pi$ in $y$. This is brand new — the real exponential is never periodic. It is the deep reason the logarithm is multivalued.

The exponential is never zero: $|e^z| = e^x > 0$. Its range is all of $\mathbb{C}\setminus\{0\}$.

#### The logarithm — a multivalued function

To invert $e^w = z$, write $z = re^{i\theta}$ and $w = u+iv$. Then $e^u e^{iv} = re^{i\theta}$ forces $e^u = r$ (so $u = \ln r$, the *real* natural log of the positive number $r$) and $v = \theta + 2\pi k$ for any integer $k$.

> **Definition — complex logarithm**
>
> For $z\ne 0$, the **(multivalued) logarithm** is $\log z = \ln|z| + i\arg z$, where $\arg z$ ranges over all its values, differing by multiples of $2\pi$. The **principal logarithm** picks the principal argument: $\mathrm{Log} z = \ln|z| + i\mathrm{Arg} z$, with $\mathrm{Arg} z\in(-\pi,\pi]$.

> **Worked example**
>
> $\log(-1)$: here $|-1| = 1$ so $\ln|z| = 0$, and $\arg(-1) = \pi + 2\pi k$. So $\log(-1) = i(\pi + 2\pi k) = i\pi, 3i\pi, -i\pi,\dots$. The principal value is $\mathrm{Log}(-1) = i\pi$ — a clean meaning for "the log of a negative number," impossible over $\mathbb{R}$.

#### Branch cuts

A **branch** of a multivalued function is a choice making it single-valued and continuous on a region. The principal logarithm is continuous everywhere except along the negative real axis, where $\mathrm{Arg}$ jumps from near $\pi$ to near $-\pi$. We exclude this ray:

> **Definition — branch cut**
>
> A **branch cut** is a curve removed from the plane to render a multivalued function single-valued and continuous. The standard **principal branch** of $\mathrm{Log}$ uses the cut along $(-\infty, 0]$. On the cut plane $\mathbb{C}\setminus(-\infty,0]$, $\mathrm{Log}$ is holomorphic with $(\mathrm{Log} z)' = 1/z$. A point you cannot encircle without forcing a jump (here $z=0$) is a **branch point**.

#### Complex powers, trig, and hyperbolic functions

> **Definition — complex power**
>
> For $z\ne0$ and any complex $\alpha$, define $z^\alpha = e^{\alpha\log z}$. With the multivalued $\log$ this is generally multivalued; using $\mathrm{Log}$ gives the principal value.

> **Worked example**
>
> $i^i = e^{i\log i}$. Now $\log i = \ln 1 + i(\pi/2 + 2\pi k) = i(\pi/2 + 2\pi k)$, so $i^i = e^{i\cdot i(\pi/2+2\pi k)} = e^{-(\pi/2 + 2\pi k)}$ — a set of **real** numbers. The principal value is $e^{-\pi/2}\approx 0.2079$.

Trig and hyperbolic functions come from Euler's formula. Adding and subtracting $e^{i\theta} = \cos\theta + i\sin\theta$ and $e^{-i\theta} = \cos\theta - i\sin\theta$ gives the real identities $\cos\theta = \tfrac12(e^{i\theta}+e^{-i\theta})$ and $\sin\theta = \tfrac1{2i}(e^{i\theta}-e^{-i\theta})$. We *define* the complex versions by the same formulas:

$$
\cos z = \frac{e^{iz}+e^{-iz}}{2}, \qquad \sin z = \frac{e^{iz}-e^{-iz}}{2i}, \qquad \cosh z = \frac{e^{z}+e^{-z}}{2}, \qquad \sinh z = \frac{e^{z}-e^{-z}}{2}.
$$

These are entire (built from $e^z$), satisfy the usual derivative rules, and reveal a hidden unity: $\cos(iz) = \cosh z$ and $\sin(iz) = i\sinh z$. A surprise: complex $\cos$ and $\sin$ are **unbounded**, since $|\cos(iy)| = \cosh y\to\infty$. The familiar bound $|\cos|\le 1$ is purely a real-axis phenomenon.

> **Common pitfall**
>
> Do not assume $\log(z_1z_2) = \log z_1 + \log z_2$ as principal values; it can be off by $2\pi i$. Identities valid over $\mathbb{R}$ often hold only "up to a multiple of $2\pi i$" or only on a chosen branch.

## Part C · Integration

<a id="s5"></a>
### Contour integrals: parametrization and the ML inequality

Integration in $\mathbb{C}$ is integration along a path. The single most important quantity in the subject — and the one that drives everything in Parts C and D — is the integral of a function over a curve in the plane.

#### Contours

> **Definition — contour**
>
> A **smooth arc** is a curve $z(t) = x(t) + iy(t)$, $t\in[a,b]$, with continuous nonzero derivative $z'(t)$. A **contour** (piecewise smooth curve) is a finite chain of smooth arcs joined end to end. It is **closed** if $z(a)=z(b)$, and **simple** if it does not cross itself.

> **Definition — contour integral**
>
> For $f$ continuous on a contour $\gamma$ given by $z(t)$, $t\in[a,b]$,
> $$
> \int_\gamma f(z)\,dz = \int_a^b f(z(t))\,z'(t)\,dt,
> $$
> where the right side is an ordinary integral of a complex-valued function of the real variable $t$ (integrate real and imaginary parts separately).

The definition is independent of the parametrization (any orientation-preserving reparametrization gives the same value, by the change-of-variables formula). Reversing orientation flips the sign.

> **Worked example — the master integral**
>
> Integrate $f(z) = z^n$ ($n$ an integer) once counterclockwise around the unit circle $z(t) = e^{it}$, $t\in[0,2\pi]$. Here $z'(t) = ie^{it}$, so
> $$
> \int_\gamma z^n\,dz = \int_0^{2\pi} e^{int}\,ie^{it}\,dt = i\int_0^{2\pi} e^{i(n+1)t}\,dt.
> $$
> If $n\ne -1$, the integrand $e^{i(n+1)t}$ integrates to $\frac{e^{i(n+1)t}}{i(n+1)}$, which is periodic with period dividing $2\pi$, so it returns to its start and the integral is $0$. If $n = -1$, the integrand is $i\int_0^{2\pi} 1\,dt = 2\pi i$. Thus
> $$
> \oint_{|z|=1} z^n\,dz = \begin{cases} 2\pi i, & n=-1,\\ 0, & n\ne -1.\end{cases}
> $$
> Memorize this: the case $n=-1$ giving $2\pi i$ is the seed of the entire residue theorem (§s11).

#### The ML inequality

We constantly need to *bound* a contour integral without evaluating it.

> **Theorem — ML (estimation) inequality**
>
> If $|f(z)|\le M$ for all $z$ on a contour $\gamma$ of length $L$, then
> $$
> \left|\int_\gamma f(z)\,dz\right| \le ML.
> $$

**Proof.**
1. First, for any complex-valued $g(t)$ on $[a,b]$, $\left|\int_a^b g\,dt\right| \le \int_a^b |g|\,dt$. To see this, write $\int_a^b g\,dt = Re^{i\phi}$ in polar form ($R\ge 0$). Then $R = e^{-i\phi}\int_a^b g\,dt = \int_a^b e^{-i\phi}g\,dt$. Since $R$ is real, it equals the real part: $R = \int_a^b \mathrm{Re}(e^{-i\phi}g)\,dt \le \int_a^b |e^{-i\phi}g|\,dt = \int_a^b |g|\,dt$ (because the real part of a complex number never exceeds its modulus, and $|e^{-i\phi}|=1$).
2. Apply step 1 to $g(t) = f(z(t))z'(t)$:
$$
\left|\int_\gamma f\,dz\right| = \left|\int_a^b f(z(t))z'(t)\,dt\right| \le \int_a^b |f(z(t))|\,|z'(t)|\,dt.
$$
3. Bound $|f(z(t))|\le M$ on the curve:
$$
\le M\int_a^b |z'(t)|\,dt = M\cdot L,
$$
since $\int_a^b|z'(t)|\,dt$ is exactly the arc length $L$ of $\gamma$. $\blacksquare$

> **Worked example**
>
> Bound $\left|\int_\gamma \frac{1}{z}\,dz\right|$ where $\gamma$ is the upper semicircle $|z|=2$. On it $|1/z| = 1/2 =: M$, and the length is $L = \pi\cdot 2 = 2\pi$, so the integral is at most $\tfrac12\cdot 2\pi = \pi$ in modulus. The ML inequality is the chief tool for showing "arc contributions vanish" in Jordan's lemma (§s12).

<a id="s6"></a>
### The Cauchy–Goursat theorem

This is the cornerstone. It says the integral of a holomorphic function around any closed contour (in a region without holes) is **zero**. Everything magical downstream — path independence, the integral formula, residues — rests on it.

> **Theorem — Cauchy–Goursat**
>
> If $f$ is holomorphic on an open set containing a closed contour $\gamma$ and its interior, then $\oint_\gamma f(z)\,dz = 0$. More generally this holds whenever $\gamma$ lies in a **simply connected** (hole-free) region on which $f$ is holomorphic.

The brilliance of Goursat's version is that it assumes only differentiability — not continuity of $f'$. We prove the central case: a triangle.

**Proof — for a triangle $T$ (Goursat).**
1. Let $\Delta$ be a solid triangle with boundary $T$, and let $I = \oint_T f\,dz$. **Subdivide** $\Delta$ into four congruent sub-triangles by joining the midpoints of its sides. Orient all boundaries counterclockwise.
2. The integrals over the three interior edges introduced by subdivision each occur **twice with opposite orientation** (each shared edge is traversed once by each of two adjacent sub-triangles in opposite directions), so they cancel when summed. Hence $I = \sum_{j=1}^4 \oint_{T_j} f\,dz$, the sum over the four sub-triangle boundaries.
3. By the triangle inequality, at least one sub-triangle, call it $\Delta^{(1)}$ with boundary $T_1$, satisfies $\left|\oint_{T_1} f\,dz\right| \ge \tfrac14|I|$. (If all four were smaller, the sum could not reach $|I|$.)
4. Repeat the subdivision on $\Delta^{(1)}$, getting $\Delta^{(2)}$ with $\left|\oint_{T_2}f\right| \ge \tfrac14\left|\oint_{T_1}f\right| \ge \tfrac1{4^2}|I|$, and so on. This yields a nested sequence $\Delta\supset\Delta^{(1)}\supset\Delta^{(2)}\supset\cdots$ with
$$
\left|\oint_{T_n} f\,dz\right| \ge \frac{|I|}{4^n}.
$$
5. The diameters $d_n$ and perimeters $L_n$ halve each step: $d_n = d/2^n$, $L_n = L/2^n$, where $d,L$ are the diameter and perimeter of $\Delta$. By the **nested closed sets** property (the diameters shrink to $0$ and each $\Delta^{(n)}$ is closed), the intersection is a single point $z_0\in\Delta$.
6. **Use differentiability at $z_0$.** Since $f'(z_0)$ exists, write $f(z) = f(z_0) + f'(z_0)(z-z_0) + \eta(z)(z-z_0)$, where the error $\eta(z)\to 0$ as $z\to z_0$. Given $\varepsilon>0$, there is $\delta>0$ with $|\eta(z)| < \varepsilon$ whenever $|z-z_0|<\delta$.
7. The functions $f(z_0)$ and $f'(z_0)(z-z_0)$ are a constant and a linear function; each has an explicit antiderivative ($f(z_0)z$ and $f'(z_0)(z-z_0)^2/2$), so their integrals around the *closed* contour $T_n$ are $0$ (an antiderivative makes a closed-loop integral vanish — fundamental theorem of contour integrals). Therefore
$$
\oint_{T_n} f\,dz = \oint_{T_n} \eta(z)(z-z_0)\,dz.
$$
8. For $n$ large enough that $\Delta^{(n)}\subset D(z_0,\delta)$ (possible since diameters shrink to $0$), apply the ML inequality (§s5): on $T_n$, $|\eta(z)| < \varepsilon$ and $|z-z_0|\le d_n = d/2^n$, and the length is $L_n = L/2^n$. So
$$
\left|\oint_{T_n}f\,dz\right| \le \varepsilon\cdot\frac{d}{2^n}\cdot\frac{L}{2^n} = \frac{\varepsilon\,dL}{4^n}.
$$
9. Combine with step 4: $\dfrac{|I|}{4^n} \le \dfrac{\varepsilon\,dL}{4^n}$, hence $|I|\le \varepsilon\,dL$. Since $\varepsilon>0$ was arbitrary and $dL$ is fixed, $|I| = 0$, so $I=0$. $\blacksquare$

From triangles one extends to any polygon (triangulate it) and then to convex regions and simply connected regions by approximating contours with polygons. A direct corollary:

> **Corollary — path independence and antiderivatives**
>
> On a simply connected region where $f$ is holomorphic, $\int_\gamma f\,dz$ depends only on the endpoints of $\gamma$, and $f$ has an antiderivative $F$ with $F' = f$. Consequently $\int_\gamma f\,dz = F(z_{\text{end}}) - F(z_{\text{start}})$, exactly like the fundamental theorem of calculus.

This is why $\oint z^n\,dz = 0$ for $n\ge 0$ (those are entire, with antiderivative $z^{n+1}/(n+1)$), while $n=-1$ escapes — $1/z$ has no single-valued antiderivative around $0$ because $\log z$ is multivalued.

<a id="s7"></a>
### The Cauchy integral formula and the formula for derivatives

Now the payoff. A holomorphic function's values inside a contour are completely determined by its values *on* the contour. This is unheard of in real calculus and is the source of complex analysis's rigidity.

> **Theorem — Cauchy integral formula**
>
> Let $f$ be holomorphic on and inside a positively (counterclockwise) oriented simple closed contour $\gamma$, and let $z_0$ be a point *inside* $\gamma$. Then
> $$
> f(z_0) = \frac{1}{2\pi i}\oint_\gamma \frac{f(z)}{z - z_0}\,dz.
> $$

**Proof.**
1. The function $g(z) = \dfrac{f(z)}{z-z_0}$ is holomorphic everywhere inside $\gamma$ *except* at $z_0$. By a deformation consequence of Cauchy–Goursat (the integral over $\gamma$ equals the integral over a small circle around $z_0$, because the region between them is hole-free for $g$), we may replace $\gamma$ by a small circle $C_\rho$ of radius $\rho$ centered at $z_0$:
$$
\oint_\gamma \frac{f(z)}{z-z_0}\,dz = \oint_{C_\rho}\frac{f(z)}{z-z_0}\,dz.
$$
2. Split the right side using $f(z) = f(z_0) + [f(z)-f(z_0)]$:
$$
\oint_{C_\rho}\frac{f(z)}{z-z_0}\,dz = f(z_0)\oint_{C_\rho}\frac{dz}{z-z_0} + \oint_{C_\rho}\frac{f(z)-f(z_0)}{z-z_0}\,dz.
$$
3. The first integral is the master integral of §s5 with center $z_0$: parametrize $z = z_0 + \rho e^{it}$, then $\oint_{C_\rho}\frac{dz}{z-z_0} = \int_0^{2\pi}\frac{i\rho e^{it}}{\rho e^{it}}\,dt = \int_0^{2\pi} i\,dt = 2\pi i$. So the first term is $2\pi i\,f(z_0)$.
4. The second integral vanishes as $\rho\to 0$. Since $f$ is continuous at $z_0$, given $\varepsilon>0$ choose $\rho$ small enough that $|f(z)-f(z_0)|<\varepsilon$ on $C_\rho$. On $C_\rho$, $|z-z_0| = \rho$, so the integrand has modulus $< \varepsilon/\rho$, and the contour length is $2\pi\rho$. By the ML inequality the second integral has modulus $< (\varepsilon/\rho)(2\pi\rho) = 2\pi\varepsilon$.
5. The left side of step 2 does **not** depend on $\rho$ (it equals the fixed $\oint_\gamma$ from step 1). So the second integral equals a constant; but step 4 shows that constant has modulus $< 2\pi\varepsilon$ for every $\varepsilon>0$, forcing it to be $0$.
6. Therefore $\oint_\gamma \frac{f(z)}{z-z_0}\,dz = 2\pi i\,f(z_0)$. Divide by $2\pi i$. $\blacksquare$

#### The formula for derivatives

Differentiating the integral formula with respect to the *parameter* $z_0$ — under the integral sign — produces formulas for every derivative.

> **Theorem — Cauchy's formula for derivatives**
>
> Under the same hypotheses, $f$ has derivatives of **all** orders inside $\gamma$, and
> $$
> f^{(n)}(z_0) = \frac{n!}{2\pi i}\oint_\gamma \frac{f(z)}{(z-z_0)^{n+1}}\,dz, \qquad n = 0,1,2,\dots
> $$

**Proof (sketch of the induction with full first step).**
1. For $n=1$, form the difference quotient using the integral formula at $z_0+h$ and $z_0$:
$$
\frac{f(z_0+h)-f(z_0)}{h} = \frac{1}{2\pi i}\oint_\gamma f(z)\cdot\frac{1}{h}\left(\frac{1}{z-z_0-h} - \frac{1}{z-z_0}\right)dz.
$$
2. Combine the fractions: $\frac{1}{h}\cdot\frac{(z-z_0)-(z-z_0-h)}{(z-z_0-h)(z-z_0)} = \frac{1}{(z-z_0-h)(z-z_0)}$. So the quotient is $\frac{1}{2\pi i}\oint_\gamma \frac{f(z)}{(z-z_0-h)(z-z_0)}\,dz$.
3. Let $h\to 0$. The integrand converges to $\frac{f(z)}{(z-z_0)^2}$ uniformly on $\gamma$ (because $z$ stays a fixed positive distance from $z_0$ as $z$ ranges over $\gamma$, so the denominators are bounded away from $0$). Uniform convergence permits passing the limit inside the integral. This gives $f'(z_0) = \frac{1!}{2\pi i}\oint_\gamma \frac{f(z)}{(z-z_0)^2}\,dz$.
4. The same difference-quotient argument applied to $f^{(n)}$ (using the formula for $n$ to get $n+1$) advances the induction; the factor $n!$ accumulates from differentiating $(z-z_0)^{-(n+1)}$ each step. $\blacksquare$

> **Stunning consequence**
>
> A function differentiable *once* on an open set is automatically differentiable *infinitely many times* there. This is utterly false over $\mathbb{R}$ (where $f(x)=x|x|$ is differentiable once but not twice). It also retroactively justifies §s3's assumption that $u,v$ have continuous second partials.

> **Worked example**
>
> Evaluate $\oint_{|z|=1}\frac{e^z}{z^2}\,dz$. Here $f(z)=e^z$ is entire, $z_0=0$, and the integrand matches $\frac{f(z)}{z^{1+1}}$ with $n=1$. So the integral equals $\frac{2\pi i}{1!}f'(0) = 2\pi i\,e^0 = 2\pi i$.

<a id="s8"></a>
### Consequences: Liouville's theorem, the fundamental theorem of algebra, and the maximum-modulus principle

The integral formulas are not just for computing — they imply sweeping structural theorems. Three classics follow with short proofs.

#### Cauchy's estimate and Liouville

> **Lemma — Cauchy's estimate**
>
> If $f$ is holomorphic on and inside the circle $C_R$ of radius $R$ about $z_0$, and $|f|\le M$ on $C_R$, then $|f^{(n)}(z_0)| \le \dfrac{n!\,M}{R^n}$.

**Proof.** Apply ML to the derivative formula (§s7): on $C_R$ the integrand $\frac{f(z)}{(z-z_0)^{n+1}}$ has modulus $\le \frac{M}{R^{n+1}}$, and the length is $2\pi R$. So $|f^{(n)}(z_0)|\le \frac{n!}{2\pi}\cdot\frac{M}{R^{n+1}}\cdot 2\pi R = \frac{n!M}{R^n}$. $\blacksquare$

> **Theorem — Liouville**
>
> A bounded entire function is constant.

**Proof.**
1. Suppose $f$ is entire and $|f|\le M$ everywhere. Fix any $z_0$. Apply Cauchy's estimate with $n=1$ on a circle of radius $R$: $|f'(z_0)|\le M/R$.
2. Since $f$ is entire, this holds for *every* $R>0$. Let $R\to\infty$: $|f'(z_0)|\le M/R\to 0$, so $f'(z_0)=0$.
3. As $z_0$ was arbitrary, $f'\equiv 0$ on the connected set $\mathbb{C}$, so $f$ is constant (a function with zero derivative on a connected open set is constant). $\blacksquare$

#### The fundamental theorem of algebra

> **Theorem — fundamental theorem of algebra**
>
> Every non-constant polynomial $p(z)$ with complex coefficients has at least one root in $\mathbb{C}$.

**Proof.**
1. Suppose $p$ has no root, so $p(z)\ne 0$ for all $z$. Then $g(z) = 1/p(z)$ is entire (a quotient of holomorphic functions with nonvanishing denominator).
2. As $|z|\to\infty$, $|p(z)|\to\infty$ (the leading term $a_n z^n$ dominates): writing $p(z)=a_n z^n+\dots+a_0$ with $a_n\ne 0$, the reverse triangle inequality gives $|p(z)|\ge |a_n||z|^n\Bigl(1 - \frac{|a_{n-1}|/|a_n|}{|z|} - \cdots - \frac{|a_0|/|a_n|}{|z|^n}\Bigr)\to\infty$, since the bracket $\to 1$. Hence $|g(z)| = 1/|p(z)|\to 0$. Hence $g$ is bounded outside some large disk, and being continuous it is bounded on the closed disk too — so $g$ is bounded on all of $\mathbb{C}$.
3. By Liouville, $g$ is constant, so $p$ is constant — contradicting "non-constant." Therefore $p$ has a root. $\blacksquare$

Dividing out the root and repeating shows a degree-$n$ polynomial has exactly $n$ roots counted with multiplicity — the "fundamental" factorization $\mathbb{C}$ provides and $\mathbb{R}$ cannot.

#### The maximum-modulus principle

> **Theorem — maximum-modulus principle**
>
> If $f$ is holomorphic and non-constant on a connected open set $U$, then $|f|$ has no local maximum in $U$. If $U$ is bounded and $f$ is continuous up to the boundary, $|f|$ attains its maximum *on the boundary*.

**Proof.**
1. **Mean value property.** Apply the Cauchy integral formula on a circle $z = z_0+\rho e^{it}$: substituting $dz = i\rho e^{it}dt$ gives
$$
f(z_0) = \frac{1}{2\pi}\int_0^{2\pi} f(z_0+\rho e^{it})\,dt.
$$
So $f(z_0)$ is the **average** of its values on any circle around $z_0$.
2. Suppose $|f|$ had a local maximum $M = |f(z_0)|$ at $z_0$. On a small circle, $|f(z_0+\rho e^{it})|\le M$. Taking moduli in step 1, $M = |f(z_0)| \le \frac{1}{2\pi}\int_0^{2\pi}|f(z_0+\rho e^{it})|\,dt \le M$.
3. Equality throughout forces $|f(z_0+\rho e^{it})| = M$ for all $t$ (a continuous function whose average equals its maximum must equal that maximum everywhere). So $|f|\equiv M$ on every small circle, hence on a disk.
4. A holomorphic function of constant modulus on a region is constant (from the CR equations: $|f|^2 = u^2+v^2$ constant, differentiate and combine with CR to force $u,v$ constant). This contradicts non-constancy unless $f$ is constant. So no interior local maximum exists. The boundary statement follows since $|f|$, continuous on the compact closure, attains a max somewhere, and by the above not in the interior. $\blacksquare$

> **Worked example**
>
> On the closed unit disk, where is $|e^z|$ largest? Since $|e^z| = e^{\mathrm{Re} z} = e^x$, and $f=e^z$ is non-constant, the maximum is on the boundary $|z|=1$, at $x=1$, i.e. $z=1$: value $e$. The principle correctly predicts the maximum is on the boundary.

## Part D · Series and residues

<a id="s9"></a>
### Power series and Taylor series; analyticity equals having a power series

We now show the two meanings of "analytic" coincide: being holomorphic is exactly the same as being locally a convergent power series. This ties §s2's local derivative to a global representation.

> **Definition — power series**
>
> A **power series** centered at $z_0$ is $\sum_{n=0}^\infty a_n (z-z_0)^n$ with complex coefficients $a_n$. Its **radius of convergence** is $R = 1/\limsup_n |a_n|^{1/n}$ (with $R=\infty$ if the limsup is $0$).

> **Theorem — convergence of power series**
>
> A power series converges absolutely for $|z-z_0|<R$ and diverges for $|z-z_0|>R$; on every closed sub-disk $|z-z_0|\le r<R$ convergence is uniform.

**Proof.** Apply the root test: $\limsup_n |a_n(z-z_0)^n|^{1/n} = |z-z_0|\limsup_n|a_n|^{1/n} = |z-z_0|/R$. This is $<1$ when $|z-z_0|<R$ (absolute convergence) and $>1$ when $|z-z_0|>R$ (divergence). Uniformity on $|z-z_0|\le r$ follows from the Weierstrass M-test with $M_n = |a_n|r^n$. $\blacksquare$

Within its disk a power series defines a holomorphic function, differentiable term by term (uniform convergence licenses differentiating under the sum). Conversely:

> **Theorem — holomorphic implies Taylor series (Taylor's theorem)**
>
> If $f$ is holomorphic on a disk $D(z_0,R)$, then for all $z$ in that disk
> $$
> f(z) = \sum_{n=0}^\infty \frac{f^{(n)}(z_0)}{n!}(z-z_0)^n,
> $$
> and this series converges on the whole disk.

**Proof.**
1. Take $z$ with $|z-z_0|<r<R$ and apply the Cauchy integral formula on the circle $C_r$ of radius $r$: $f(z) = \frac{1}{2\pi i}\oint_{C_r}\frac{f(w)}{w-z}\,dw$.
2. Expand the kernel as a geometric series. Write $\frac{1}{w-z} = \frac{1}{(w-z_0)-(z-z_0)} = \frac{1}{w-z_0}\cdot\frac{1}{1-\frac{z-z_0}{w-z_0}}$. For $w$ on $C_r$ we have $\left|\frac{z-z_0}{w-z_0}\right| = \frac{|z-z_0|}{r} < 1$, so the geometric series $\sum_{n\ge 0}\left(\frac{z-z_0}{w-z_0}\right)^n$ converges, uniformly in $w$ on $C_r$.
3. Thus $\frac{1}{w-z} = \sum_{n=0}^\infty \frac{(z-z_0)^n}{(w-z_0)^{n+1}}$. Multiply by $f(w)/(2\pi i)$ and integrate term by term over $C_r$ (uniform convergence permits the interchange):
$$
f(z) = \sum_{n=0}^\infty \left(\frac{1}{2\pi i}\oint_{C_r}\frac{f(w)}{(w-z_0)^{n+1}}\,dw\right)(z-z_0)^n.
$$
4. The bracket is exactly $f^{(n)}(z_0)/n!$ by Cauchy's derivative formula (§s7). So the coefficients are $a_n = f^{(n)}(z_0)/n!$, giving the Taylor series. Since $r<R$ was arbitrary, the representation holds on all of $D(z_0,R)$. $\blacksquare$

> **Worked example**
>
> $\frac{1}{1-z} = \sum_{n=0}^\infty z^n$ for $|z|<1$; the radius is $1$, dictated by the singularity at $z=1$. Likewise $e^z = \sum z^n/n!$ has $R=\infty$, confirming the legitimacy of the rearrangements in §s0's Euler derivation.

A profound corollary, the **identity theorem**: if two holomorphic functions agree on a set with a limit point inside a connected region, they agree everywhere on it. (Justification: apply the result to the difference $h=f-g$; the zeros of a nonzero analytic function are **isolated** — at any zero the local power-series form $h(z)=(z-z_0)^m\,[a_m+\cdots]$ with $a_m\ne 0$ is nonzero on a punctured neighborhood — so a zero set with a limit point forces $h\equiv 0$ on the connected region.) Holomorphic functions are rigid — knowing one on a tiny arc pins it down globally.

<a id="s10"></a>
### Laurent series and the classification of singularities

Taylor series handle points where $f$ is holomorphic. Near an *isolated singularity* — a point where $f$ misbehaves — we need negative powers too. The **Laurent series** supplies them and lets us classify exactly how bad a singularity is.

> **Theorem/Definition — Laurent series**
>
> If $f$ is holomorphic on an **annulus** $A = \{r < |z-z_0| < R\}$, then on $A$
> $$
> f(z) = \sum_{n=-\infty}^{\infty} a_n (z-z_0)^n, \qquad a_n = \frac{1}{2\pi i}\oint_{C}\frac{f(w)}{(w-z_0)^{n+1}}\,dw,
> $$
> where $C$ is any circle in the annulus. The terms with $n<0$ form the **principal part**.

**Proof idea.** Apply the Cauchy formula with two circles bounding the annulus (outer $C_R$ traversed counterclockwise, inner $C_r$ clockwise). Expand the outer kernel as a geometric series in $(z-z_0)/(w-z_0)$ (giving nonnegative powers, as in §s9) and the inner kernel as a series in $(w-z_0)/(z-z_0)$ (giving negative powers). Integrating term by term yields both halves of the sum. $\blacksquare$

> **Definition — isolated singularity and its three types**
>
> $z_0$ is an **isolated singularity** of $f$ if $f$ is holomorphic on a punctured disk $0<|z-z_0|<R$ but not (defined as holomorphic) at $z_0$. By the principal part of its Laurent series:
> - **Removable:** no negative-power terms. $f$ extends holomorphically across $z_0$.
> - **Pole of order $m$:** finitely many negative terms, lowest being $a_{-m}(z-z_0)^{-m}$ with $a_{-m}\ne 0$. (Order $1$ = simple pole.)
> - **Essential:** infinitely many negative terms.

> **Worked examples — one of each**
>
> - $\dfrac{\sin z}{z}$ at $0$: $\sin z = z - z^3/6 + \cdots$ so $\frac{\sin z}{z} = 1 - z^2/6 + \cdots$ — no negative powers, **removable** (define the value $1$ at $0$). - $\dfrac{e^z}{z^2}$ at $0$: $= \frac{1}{z^2} + \frac{1}{z} + \frac12 + \cdots$, two negative terms, **pole of order $2$**. - $e^{1/z}$ at $0$: $= \sum_{n\ge 0}\frac{1}{n!\,z^n} = 1 + \frac1z + \frac{1}{2z^2}+\cdots$, infinitely many negative terms, **essential**.

The classification has teeth. Near a removable singularity $f$ stays bounded; near a pole $|f|\to\infty$; near an **essential** singularity the **Casorati–Weierstrass theorem** says $f$ comes arbitrarily close to *every* complex value in every neighborhood — wild behavior, exemplified by $e^{1/z}$ taking all nonzero values infinitely often near $0$.

<a id="s11"></a>
### Residues and the residue theorem

The single coefficient $a_{-1}$ in a Laurent series is special: it is the only term that survives integration around the singularity (recall §s5: only $z^{-1}$ integrates to a nonzero $2\pi i$). Collecting these coefficients gives a master computational tool.

> **Definition — residue**
>
> The **residue** of $f$ at an isolated singularity $z_0$ is the Laurent coefficient $a_{-1}$:
> $$
> \mathrm{Res}(f,z_0) = a_{-1} = \frac{1}{2\pi i}\oint_C f(z)\,dz,
> $$
> for a small circle $C$ around $z_0$.

> **Theorem — residue theorem**
>
> Let $f$ be holomorphic on and inside a positively oriented simple closed contour $\gamma$, except for finitely many isolated singularities $z_1,\dots,z_k$ inside $\gamma$. Then
> $$
> \oint_\gamma f(z)\,dz = 2\pi i\sum_{j=1}^k \mathrm{Res}(f,z_j).
> $$

**Proof.**
1. Around each singularity $z_j$ draw a small circle $C_j$, of radius small enough that the circles are disjoint and lie inside $\gamma$. Consider the region $\Omega$ between $\gamma$ and the union of these circles. On $\Omega$, $f$ is holomorphic (all singularities have been excised).
2. Connect $\gamma$ to each $C_j$ by thin "keyhole" corridors, forming a single closed contour $\Gamma$ that bounds a simply connected region on which $f$ is holomorphic. The two edges of each corridor are traversed in opposite directions and cancel.
3. By Cauchy–Goursat (§s6), $\oint_\Gamma f\,dz = 0$. Removing the cancelling corridor edges, $\Gamma$ consists of $\gamma$ traversed counterclockwise together with each $C_j$ traversed **clockwise**. Therefore
$$
0 = \oint_\gamma f\,dz - \sum_{j=1}^k \oint_{C_j} f\,dz,
$$
where the minus sign converts each clockwise circle to counterclockwise.
4. By the definition of residue (step's box above), $\oint_{C_j} f\,dz = 2\pi i\mathrm{Res}(f,z_j)$. Substitute:
$$
\oint_\gamma f\,dz = \sum_{j=1}^k 2\pi i\,\mathrm{Res}(f,z_j) = 2\pi i\sum_{j=1}^k \mathrm{Res}(f,z_j). \qquad \blacksquare
$$

#### Computing residues

> **Formulas — residues at poles**
>
> - Simple pole: $\mathrm{Res}(f,z_0) = \lim_{z\to z_0}(z-z_0)f(z)$.
> - If $f = p/q$ with $p(z_0)\ne 0$ and $q$ having a simple zero at $z_0$: $\mathrm{Res}(f,z_0) = p(z_0)/q'(z_0)$.
> - Pole of order $m$: $\mathrm{Res}(f,z_0) = \dfrac{1}{(m-1)!}\lim_{z\to z_0}\dfrac{d^{m-1}}{dz^{m-1}}\bigl[(z-z_0)^m f(z)\bigr]$.

The simple-pole formula holds because $(z-z_0)f(z) = a_{-1} + a_0(z-z_0)+\cdots$, whose limit is $a_{-1}$. The order-$m$ formula multiplies away the pole to leave a Taylor series, then differentiates $m-1$ times to isolate $a_{-1}$.

> **Worked example**
>
> $\mathrm{Res}\left(\frac{e^z}{z^2-1}, 1\right)$: simple pole at $z=1$, with $p=e^z$, $q=z^2-1$, $q'=2z$. Residue $= e^1/(2\cdot 1) = e/2$.

<a id="s12"></a>
### Evaluating real definite integrals by residues

The residue theorem's most spectacular application is computing hard *real* integrals — ones that defeat elementary antiderivatives — by closing a contour in the complex plane.

#### Trigonometric integrals over $[0,2\pi]$

For $\int_0^{2\pi} R(\cos\theta,\sin\theta)\,d\theta$, substitute $z = e^{i\theta}$, so $d\theta = dz/(iz)$, $\cos\theta = \tfrac12(z+z^{-1})$, $\sin\theta = \tfrac1{2i}(z-z^{-1})$, converting it to a contour integral around $|z|=1$.

> **Worked example**
>
> $\displaystyle\int_0^{2\pi}\frac{d\theta}{2+\cos\theta}$. Substitute: $\cos\theta = \tfrac12(z+1/z)$, $d\theta = dz/(iz)$, giving $\oint_{|z|=1}\frac{1}{2 + \frac12(z+1/z)}\cdot\frac{dz}{iz} = \oint \frac{2}{i(z^2 + 4z + 1)}\,dz$. The denominator's roots are $z = -2\pm\sqrt3$; only $z_0 = -2+\sqrt3\approx -0.27$ lies inside $|z|=1$. Residue there: $\frac{2}{i}\cdot\frac{1}{2z_0+4} = \frac{2}{i\cdot 2\sqrt3} = \frac{1}{i\sqrt3}$. Multiply by $2\pi i$: integral $= 2\pi i\cdot\frac{1}{i\sqrt3} = \frac{2\pi}{\sqrt3}$.

#### Rational integrals over $(-\infty,\infty)$

For $\int_{-\infty}^\infty \frac{p(x)}{q(x)}\,dx$ with $\deg q\ge \deg p + 2$ and no real zeros of $q$, integrate over a semicircular contour: the real segment $[-R,R]$ plus the upper semicircle $\Gamma_R$ of radius $R$.

> **Worked example**
>
> $\displaystyle\int_{-\infty}^\infty\frac{dx}{1+x^2}$. The function $1/(1+z^2)$ has poles at $\pm i$; only $z=i$ is in the upper half-plane. Residue (simple pole, $q=1+z^2$, $q'=2z$): $1/(2i)$. On $\Gamma_R$, $|1/(1+z^2)|\le 1/(R^2-1)$ and length $\pi R$, so by ML the arc integral is $\le \pi R/(R^2-1)\to 0$. Hence $\int_{-\infty}^\infty = 2\pi i\cdot\frac{1}{2i} = \pi$. (This matches the elementary answer $\arctan x\big|_{-\infty}^\infty = \pi$.)

#### Jordan's lemma and Fourier-type integrals

For integrands like $\frac{p(x)}{q(x)}e^{iax}$ (with $a>0$), the factor $e^{iaz} = e^{iax}e^{-ay}$ decays in the upper half-plane.

> **Lemma — Jordan**
>
> If $a>0$ and $f(z)\to 0$ uniformly as $|z|\to\infty$ in the upper half-plane, then $\int_{\Gamma_R} f(z)e^{iaz}\,dz\to 0$ as $R\to\infty$, where $\Gamma_R$ is the upper semicircle.

The proof refines ML using $\int_0^\pi e^{-aR\sin\theta}\,d\theta \le \pi/(aR)$ (the bound $\sin\theta\ge 2\theta/\pi$ on $[0,\pi/2]$ controls the integral). The exponential's decay beats the contour's growth.

> **Worked example**
>
> $\displaystyle\int_{-\infty}^\infty\frac{\cos x}{1+x^2}\,dx = \mathrm{Re}\int_{-\infty}^\infty\frac{e^{ix}}{1+x^2}\,dx$. Pole at $z=i$ in the upper half-plane; residue of $\frac{e^{iz}}{1+z^2}$ there is $\frac{e^{i\cdot i}}{2i} = \frac{e^{-1}}{2i}$. So the integral $= 2\pi i\cdot\frac{e^{-1}}{2i} = \pi e^{-1} = \pi/e$ (already real, and we take the real part). Result: $\pi/e$.

#### Principal values and poles on the contour

When $q$ has a *simple zero on the real axis*, the integral may exist only as a **Cauchy principal value** $\mathrm{P}\!\int = \lim_{\epsilon\to0}\bigl(\int_{-\infty}^{-\epsilon}+\int_{\epsilon}^{\infty}\bigr)$. We indent the contour with a small semicircle around the pole; a half-circle around a simple pole contributes $\pi i$ (half of $2\pi i$) times the residue.

> **Worked example**
>
> $\displaystyle\int_{-\infty}^\infty \frac{\sin x}{x}\,dx$. Use $\frac{e^{iz}}{z}$, which has a simple pole at $0$ on the axis. Indent **above** the pole with a small semicircle (pushing the contour into the upper half-plane so the pole is left *outside*). The full closed contour then encloses no poles, so its integral is $0$; the small semicircle is traversed **clockwise**, so it contributes $-\pi i\mathrm{Res}(e^{iz}/z,0) = -\pi i\cdot 1$ (minus half of $2\pi i\cdot\text{Res}$); the large arc vanishes by Jordan. Balancing gives $\mathrm{P}\!\int_{-\infty}^\infty \frac{e^{ix}}{x}\,dx = \pi i$. Taking imaginary parts: $\int_{-\infty}^\infty\frac{\sin x}{x}\,dx = \pi$.

<a id="s13"></a>
### The argument principle and Rouché's theorem

Residues can *count* — they tally the zeros and poles of a function inside a contour, leading to powerful tools for locating roots.

> **Theorem — argument principle**
>
> Let $f$ be holomorphic inside and on a positively oriented simple closed contour $\gamma$, except for finitely many poles inside, with no zeros or poles *on* $\gamma$. Then
> $$
> \frac{1}{2\pi i}\oint_\gamma \frac{f'(z)}{f(z)}\,dz = Z - P,
> $$
> where $Z$ is the number of zeros and $P$ the number of poles inside $\gamma$, each counted with multiplicity.

**Proof.**
1. The integrand $f'/f$ is the **logarithmic derivative**; its singularities are exactly the zeros and poles of $f$. We compute its residue at each.
2. Near a zero of order $m$: write $f(z) = (z-z_0)^m g(z)$ with $g(z_0)\ne 0$ holomorphic. Then $\frac{f'}{f} = \frac{m}{z-z_0} + \frac{g'}{g}$. Since $g'/g$ is holomorphic at $z_0$, the residue of $f'/f$ is $m$.
3. Near a pole of order $p$: write $f(z) = (z-z_0)^{-p} h(z)$ with $h(z_0)\ne 0$. Then $\frac{f'}{f} = \frac{-p}{z-z_0} + \frac{h'}{h}$, so the residue is $-p$.
4. By the residue theorem (§s11), $\frac{1}{2\pi i}\oint_\gamma \frac{f'}{f}\,dz = \sum(\text{residues}) = \sum(\text{orders of zeros}) - \sum(\text{orders of poles}) = Z - P$. $\blacksquare$

The name comes from the geometric meaning: the integral equals $\frac{1}{2\pi}$ times the total change in $\arg f(z)$ as $z$ traverses $\gamma$ — the number of times the image curve $f(\gamma)$ winds around the origin.

> **Theorem — Rouché**
>
> If $f,g$ are holomorphic on and inside a simple closed contour $\gamma$, and $|g(z)| < |f(z)|$ for all $z$ on $\gamma$, then $f$ and $f+g$ have the same number of zeros (with multiplicity) inside $\gamma$.

**Proof.**
1. On $\gamma$, $|f| > |g|\ge 0$, so $f\ne 0$ on $\gamma$; and $|f+g|\ge |f|-|g| > 0$, so $f+g\ne 0$ on $\gamma$. Both have the argument principle available with $P=0$ (holomorphic, no poles), so their zero-counts are $Z_f = \frac{1}{2\pi}\Delta_\gamma\arg f$ and $Z_{f+g} = \frac{1}{2\pi}\Delta_\gamma\arg(f+g)$.
2. Write $f+g = f\cdot(1 + g/f)$. Then $\arg(f+g) = \arg f + \arg(1+g/f)$, so $\Delta_\gamma\arg(f+g) = \Delta_\gamma\arg f + \Delta_\gamma\arg(1+g/f)$.
3. On $\gamma$, $|g/f| < 1$, so the point $w = 1 + g/f$ stays in the disk $|w-1|<1$, which lies entirely in the right half-plane and never encircles the origin. Hence $\Delta_\gamma\arg(1+g/f) = 0$.
4. Therefore $\Delta_\gamma\arg(f+g) = \Delta_\gamma\arg f$, so $Z_{f+g} = Z_f$. $\blacksquare$

> **Worked example**
>
> How many roots of $z^4 + 6z + 3$ lie in $|z|<2$? Take $f = z^4$ (which has $4$ zeros at $0$) and $g = 6z+3$. On $|z|=2$: $|f| = 16$, while $|g|\le 6\cdot 2 + 3 = 15 < 16$. By Rouché, $z^4+6z+3$ has the same count as $z^4$: **four** roots in $|z|<2$. (Consistent with the fundamental theorem of algebra, §s8.)

## Part E · Geometry and continuation

<a id="s14"></a>
### Conformal mapping and Möbius transformations

Section s3 showed holomorphic maps preserve angles. Here we use that to *design* maps that carry one region onto another — a technique that solves boundary-value problems in physics by transplanting them to simpler domains.

> **Definition — conformal map**
>
> A **conformal map** between regions is a holomorphic bijection with $f'\ne 0$ throughout (automatic for a holomorphic bijection). It preserves angles (§s3) and its inverse is also conformal.

The most important explicit family:

> **Definition — Möbius transformation**
>
> A **Möbius (linear fractional) transformation** is $T(z) = \dfrac{az+b}{cz+d}$ with complex $a,b,c,d$ and $ad-bc\ne 0$.

The condition $ad-bc\ne 0$ keeps $T$ non-constant: $T'(z) = \frac{ad-bc}{(cz+d)^2}$. Möbius maps form a **group** under composition (composition of two is again Möbius; the inverse $T^{-1}(w) = \frac{dw-b}{-cw+a}$ is Möbius). Treating $\infty$ as a point (the **Riemann sphere** $\mathbb{C}\cup\{\infty\}$) makes each $T$ a bijection of the sphere, sending $z=-d/c$ to $\infty$ and $\infty$ to $a/c$.

> **Theorem — Möbius maps send "clines" to "clines"**
>
> Every Möbius transformation maps the family of lines-and-circles to itself (a line is a "circle through $\infty$").

**Proof sketch.** Any Möbius map is a composition of translations $z\mapsto z+b$, scalings/rotations $z\mapsto az$, and the inversion $z\mapsto 1/z$ (algebraically decompose $\frac{az+b}{cz+d}$). The first two preserve lines and circles (a translation or rotation/scaling carries any line to a line and any circle to a circle); one checks by direct computation that $z\mapsto 1/z$ sends the general cline equation $A|z|^2 + \mathrm{Re}(\bar Bz) + C = 0$ to another of the same form. $\blacksquare$

> **Theorem — three points determine a Möbius map**
>
> Given three distinct points $z_1,z_2,z_3$ and three distinct targets $w_1,w_2,w_3$, there is a unique Möbius transformation sending $z_j\mapsto w_j$.

This is the practical engine: to map a circular region to another, send three boundary points to three boundary points. The construction uses the **cross-ratio** $\frac{(z-z_1)(z_2-z_3)}{(z-z_3)(z_2-z_1)}$, which every Möbius map preserves.

> **Worked example — upper half-plane to unit disk**
>
> The map $T(z) = \dfrac{z-i}{z+i}$ sends the upper half-plane $\{\mathrm{Im} z>0\}$ conformally onto the unit disk $\{|w|<1\}$. Check the boundary: for real $z$, $|z-i| = |z+i| = \sqrt{z^2+1}$, so $|T(z)| = 1$ — the real axis maps to the unit circle. And $T(i) = 0$, an interior point, confirming the upper half-plane maps inside. This is the standard bridge used to transfer disk results to half-plane problems.

> **Why physicists care**
>
> Harmonic functions (§s3) stay harmonic under conformal maps. So a hard Laplace boundary-value problem on a complicated region can be conformally mapped to a disk or half-plane, solved there, and mapped back — the foundation of two-dimensional electrostatics, ideal fluid flow, and heat conduction.

<a id="s15"></a>
### Analytic continuation and a first look at Riemann surfaces

The identity theorem (§s9) said a holomorphic function is determined by its values on any small piece. This rigidity lets us *extend* a function beyond its original domain in essentially one way — and tracking the extension around branch points forces us onto a new geometric object.

> **Definition — analytic continuation**
>
> Let $f_1$ be holomorphic on a region $U_1$ and $f_2$ on $U_2$, with $U_1\cap U_2$ nonempty and connected. If $f_1 = f_2$ on the overlap, $f_2$ is an **analytic continuation** of $f_1$ to $U_2$. By the identity theorem the continuation is **unique** when it exists.

> **Worked example — the geometric series and its continuation**
>
> $f_1(z) = \sum_{n=0}^\infty z^n$ converges only on $|z|<1$. But on that disk it equals $\frac{1}{1-z}$, which is holomorphic on all of $\mathbb{C}\setminus\{1\}$. So $f_2(z) = \frac{1}{1-z}$ is *the* analytic continuation of $f_1$ — the same function, now seen on a far larger domain, with the unit circle no longer a real barrier but an artifact of the series representation.

#### Continuation along paths and monodromy

We can also continue by **chains of overlapping disks**, re-expanding the Taylor series at successive centers (each new series agrees with the old on the overlap, so by uniqueness it continues the function). A subtlety arises: continuing the *same* starting function along *two different paths* to the same endpoint can give *different* values when the paths enclose a **branch point**.

> **Worked example — the logarithm's monodromy**
>
> Start with $\mathrm{Log} z$ near $z=1$ (value $0$). Continue it counterclockwise around the origin. Each step the imaginary part (the argument) increases continuously; after a full loop the value has grown by $2\pi i$ — we return to $z=1$ but with value $2\pi i$, not $0$. The function does not come back to itself. The origin is a branch point; encircling it permanently shifts the branch.

This non-single-valuedness is not a defect to be patched with a branch cut (§s4) but a feature with a natural home.

> **Definition / Idea — Riemann surface**
>
> A **Riemann surface** for a multivalued function is a surface, built by stacking and gluing copies (**sheets**) of the plane along branch cuts, on which the function becomes genuinely single-valued and holomorphic. For $\log z$ the surface is an infinite spiral staircase (infinitely many sheets, each loop around $0$ climbing to the next). For $\sqrt z$ it is two sheets joined into a single surface, so that going around $0$ twice returns you home.

On its Riemann surface, $\log z$ is one honest function; the "$+2\pi i$ per loop" simply means you have climbed one floor. Riemann surfaces turn the awkward multivaluedness of §s4 into clean geometry, and they open the door to the deep interplay of complex analysis, topology, and algebraic geometry — the subject's grand horizon.

> **Common pitfall**
>
> A branch cut is a *choice* (it depends on where you draw the forbidden curve); the branch points are *intrinsic* (forced by the function). Two analysts may cut differently, but they agree on where the genuine obstructions — the branch points — lie.

---

*From a single rule $i^2=-1$ we reached the residue theorem, the rigidity of holomorphic functions, and the spiral staircase of the logarithm. The throughline is one astonishing fact: complex differentiability — the innocent-looking demand that a limit exist from every direction — forces analyticity, power-series representation, infinite smoothness, and the encoding of a function's global behavior in contour integrals. Read once for the architecture; return to any proof box when you need the machinery. The magic was in the definition all along.*
