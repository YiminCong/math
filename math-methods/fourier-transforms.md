**English** · [中文](fourier-transforms.zh.md)

# Fourier Analysis & Integral Transforms, *decomposing the world into waves.*

*This guide builds Fourier analysis from the ground up: starting with the simple idea that any reasonable signal is a sum of pure waves, it develops Fourier series, the Fourier transform, the Dirac delta, convolution, the Laplace transform, and Green's functions — every formula stated precisely, every key result proved step by step, and every idea tied back to the physics of position, momentum, time, and frequency.*

[← Back to all guides](../README.md)

## Part A — From periodic signals to spectra

<a id="s0"></a>
### Motivation — decomposing the world into frequencies

**What & why.** Strike a piano string and you hear a definite pitch; shine white light through a prism and it splits into colours; tap a wineglass and it rings at its natural frequency. In each case a complicated thing — a vibration, a beam of light, a sound — is revealed to be a *superposition* of simple pure tones, each with its own frequency. Fourier analysis is the mathematics of that decomposition. It says: take a function (a signal, a wave, a quantum state) and rewrite it as a combination of the simplest oscillating building blocks, $\sin$, $\cos$, or the complex exponential $e^{i\omega t}$.

Why is this so powerful? Because the building blocks are *eigenfunctions* of the operations physics cares about. Differentiation turns $e^{i\omega t}$ into $i\omega \cdot e^{i\omega t}$ — it just multiplies by a number. A linear, time-invariant physical system (a filter, a resonant circuit, a vibrating membrane) responds to a pure tone by producing the *same* tone with a changed amplitude and phase. So if we know the response to each pure frequency, linearity gives us the response to anything. Solving a hard differential equation becomes solving an algebra problem, one frequency at a time.

**Position versus momentum space.** The single deepest physical reason to care lives in quantum mechanics. A particle's state can be described by a wavefunction $\psi(x)$ telling us *where* it is likely to be (position space), or by a function $\tilde\psi(p)$ telling us *what momentum* it is likely to have (momentum space). These two descriptions contain exactly the same information, and the dictionary that translates between them is the Fourier transform: a sharply localized "spike" in position is a broad spread in momentum, and vice versa. This trade-off is the mathematical heart of the Heisenberg uncertainty principle, and it is a theorem about Fourier transforms before it is a statement about physics.

**Two settings.** We will meet two flavours of the same idea:

- **Periodic functions** (a signal that repeats every $L$ seconds) decompose into a *discrete* set of frequencies — a **Fourier series**, an infinite sum.
- **Non-periodic functions** (a single pulse, a localized wavepacket) decompose into a *continuum* of frequencies — a **Fourier transform**, an integral.

The series is the warm-up; the transform is the goal. We treat the series first because it is concrete and finite-flavoured, then take a limiting "let the period go to infinity" view to reach the transform.

**Why "eigenfunction" is the magic word.** A linear operator $\mathcal D$ (such as $d/dx$, or "convolve with a fixed kernel") acts on functions. An **eigenfunction** is a function $e$ that $\mathcal D$ merely scales: $\mathcal D e=\lambda e$ for some number $\lambda$ (the eigenvalue). If we can write any input as a combination of eigenfunctions, then $\mathcal D$ acts on each piece by simple multiplication, and a hard operator-equation collapses into independent one-number equations. The exponentials $e^{ikx}$ are simultaneous eigenfunctions of differentiation *and* of every shift, which is exactly why Fourier methods turn calculus and shift-invariant physics into arithmetic. This is the same philosophy as diagonalizing a matrix in linear algebra: change to the basis where the operator is diagonal, do the easy thing, change back.

**A map of where we are going.** The journey has a shape worth previewing. Periodic signals give discrete spectra (Fourier *series*, [s1](#s1)–[s3](#s3)). Letting the period grow without bound turns the discrete ladder of frequencies into a continuum (Fourier *transform*, [s4](#s4)–[s8](#s8)). Tilting the integration contour into the complex plane and restricting to $t>0$ gives the *Laplace* transform for initial-value problems ([s9](#s9)–[s10](#s10)). Replacing the continuum by a finite grid of samples gives the *discrete* transform a computer can run ([s11](#s11)). Four transforms, one idea — decompose, solve in the easy basis, reassemble.

**Symbols introduced.** Throughout, $x$ or $t$ denotes the variable in the original domain (space or time); $k$ or $\omega$ denotes the conjugate variable (wavenumber or angular frequency); $i=\sqrt{-1}$; $\int_a^b$ is the definite integral; an overline $\overline{z}$ denotes complex conjugate. We assume only single-variable calculus (derivatives, integrals, the chain rule, integration by parts) and basic complex arithmetic ($e^{i\theta}=\cos\theta+i\sin\theta$, Euler's formula).

**A first taste of "frequency".** A pure wave is $\cos(\omega t)$ or, more usefully, $e^{i\omega t}$. The number $\omega$ is the **angular frequency** (radians per second); the wave repeats every $T=2\pi/\omega$ seconds. For a wave in space, $e^{ikx}$ has **wavenumber** $k$ (radians per metre) and wavelength $2\pi/k$. The single fact that makes the exponential king of the building blocks is
$$
\frac{d}{dt}e^{i\omega t}=i\omega\,e^{i\omega t}:
$$
differentiating an exponential reproduces it, scaled by $i\omega$. Compare with $\frac{d}{dt}\cos(\omega t)=-\omega\sin(\omega t)$, which turns a cosine into a different function (a sine). The exponential is an **eigenfunction** of $d/dt$ — it survives differentiation up to a number — and that is precisely the property that converts differential equations into algebra. Keep this single equation in mind; it is the seed from which the derivative rule ([s5](#s5)), the Laplace method ([s9](#s9)), and the Green's-function calculation ([s10](#s10)) all grow.

<a id="s1"></a>
### Fourier series and the orthogonality of sines and cosines

**What & why.** Suppose $f(x)$ repeats with period $2L$: $f(x+2L)=f(x)$ for all $x$. The claim of Fourier is that we can write

$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty}\left[a_n\cos\!\frac{n\pi x}{L} + b_n\sin\!\frac{n\pi x}{L}\right].
$$

Each term $\cos(n\pi x/L)$ or $\sin(n\pi x/L)$ is a pure wave whose period divides $2L$, so the whole sum repeats every $2L$, as required. The numbers $a_n,b_n$ are the **Fourier coefficients** — they say "how much" of each pure wave is present. Our job: find a formula for them.

**The key tool: orthogonality.** Two functions $g,h$ on an interval are **orthogonal** there if $\int g(x)\overline{h(x)}\,dx = 0$ — the integral of their product vanishes. (The word borrows from vectors: orthogonal means "perpendicular", and the integral plays the role of a dot product.) The miracle that makes Fourier series work is that the sines and cosines above are mutually orthogonal over any interval of length $2L$. We prove this now.

**The geometric picture (why this works at all).** Think of functions on $[-L,L]$ as "vectors" in an infinite-dimensional space, with **inner product** $\langle g,h\rangle=\int_{-L}^{L} g\,\overline h\,dx$ and length $\|g\|=\sqrt{\langle g,g\rangle}$. In ordinary 3D space, to find the components of a vector $\mathbf v$ in an orthogonal basis $\mathbf e_1,\mathbf e_2,\mathbf e_3$ you compute $v_i=\langle\mathbf v,\mathbf e_i\rangle/\langle\mathbf e_i,\mathbf e_i\rangle$ — you project onto each axis. A Fourier series is *exactly the same move*, with the sines and cosines as the axes: the coefficient $a_n$ is the projection of $f$ onto the $\cos(n\pi x/L)$ "axis", normalized by that axis's squared length. The orthogonality theorem below is the statement that these axes really are mutually perpendicular, so the projections do not interfere — the heart of the whole construction. Everything that follows (coefficient formulas, Parseval, the transform) is linear-algebra-in-disguise on this function space.

**Theorem (orthogonality relations).** For integers $m,n\ge 1$, integrating over one full period $[-L,L]$:

$$
\int_{-L}^{L}\cos\!\frac{m\pi x}{L}\cos\!\frac{n\pi x}{L}\,dx = L\,\delta_{mn},\qquad
\int_{-L}^{L}\sin\!\frac{m\pi x}{L}\sin\!\frac{n\pi x}{L}\,dx = L\,\delta_{mn},
$$

$$
\int_{-L}^{L}\sin\!\frac{m\pi x}{L}\cos\!\frac{n\pi x}{L}\,dx = 0\quad(\text{all }m,n),
$$

where $\delta_{mn}$ (the **Kronecker delta**) equals $1$ if $m=n$ and $0$ otherwise.

**Proof.**
1. Recall the product-to-sum identities, which follow from the angle-addition formulas $\cos(A\pm B)=\cos A\cos B \mp \sin A\sin B$ by adding/subtracting:
$$
\cos A\cos B = \tfrac12[\cos(A-B)+\cos(A+B)],\quad
\sin A\sin B = \tfrac12[\cos(A-B)-\cos(A+B)],
$$
$$
\sin A\cos B = \tfrac12[\sin(A+B)+\sin(A-B)].
$$
We use these because they convert a *product* of trig functions (hard to integrate) into a *sum* (each term a single cosine or sine, easy to integrate).
2. Take the first integral with $A=m\pi x/L$, $B=n\pi x/L$. By step 1,
$$
\int_{-L}^{L}\cos\!\frac{m\pi x}{L}\cos\!\frac{n\pi x}{L}\,dx
=\tfrac12\int_{-L}^{L}\cos\!\frac{(m-n)\pi x}{L}\,dx + \tfrac12\int_{-L}^{L}\cos\!\frac{(m+n)\pi x}{L}\,dx.
$$
3. Evaluate each piece. For any nonzero integer $k$, by the fundamental theorem of calculus and $\sin(k\pi)=\sin(-k\pi)=0$,
$$
\int_{-L}^{L}\cos\!\frac{k\pi x}{L}\,dx = \left.\frac{L}{k\pi}\sin\!\frac{k\pi x}{L}\right|_{-L}^{L} = \frac{L}{k\pi}\big[\sin(k\pi)-\sin(-k\pi)\big]=0.
$$
This is *why* whole-number frequencies matter: each completes an integer number of cycles over $[-L,L]$, so its integral cancels.
4. Case $m\ne n$: then $m-n\ne 0$ and $m+n\ne 0$, so both integrals in step 2 vanish by step 3; the result is $0$. This matches $L\delta_{mn}=0$.
5. Case $m=n$: then $m-n=0$, so the first integrand is $\cos 0 = 1$, giving $\tfrac12\int_{-L}^{L}1\,dx=\tfrac12(2L)=L$. The second has $m+n=2m\ne0$, so it vanishes by step 3. Total: $L=L\delta_{mm}$. The two cases together prove the cosine relation.
6. The sine relation is identical, using $\sin A\sin B=\tfrac12[\cos(A-B)-\cos(A+B)]$; when $m=n$ the surviving piece is again $\tfrac12\int_{-L}^{L}1\,dx=L$.
7. The mixed relation: by step 1, $\sin A\cos B=\tfrac12[\sin((m+n)\pi x/L)+\sin((m-n)\pi x/L)]$. For any integer $k$, $\int_{-L}^{L}\sin(k\pi x/L)\,dx=0$ because $\sin(k\pi x/L)$ is an **odd** function (sends $x\mapsto -x$ to its negative) integrated over the symmetric interval $[-L,L]$, and the integral of an odd function over a symmetric interval is zero. Hence the mixed integral is $0$ for all $m,n$. $\blacksquare$

**The coefficient formulas.** Now extract $a_n$ and $b_n$ by exploiting orthogonality.
1. Assume the series converges and may be integrated term by term (justified for the well-behaved functions we treat; we revisit convergence in [s2](#s2)).
2. To find $a_m$ ($m\ge1$), multiply both sides of the series by $\cos(m\pi x/L)$ and integrate over $[-L,L]$:
$$
\int_{-L}^{L} f(x)\cos\!\frac{m\pi x}{L}\,dx
= \frac{a_0}{2}\!\int_{-L}^{L}\!\cos\!\frac{m\pi x}{L}\,dx
+\sum_{n=1}^\infty a_n\!\int_{-L}^{L}\!\cos\!\frac{n\pi x}{L}\cos\!\frac{m\pi x}{L}\,dx
+\sum_{n=1}^\infty b_n\!\int_{-L}^{L}\!\sin\!\frac{n\pi x}{L}\cos\!\frac{m\pi x}{L}\,dx.
$$
3. By the orthogonality theorem: the $a_0$ integral is $0$ (step 3 above with $k=m$); every mixed sine–cosine integral is $0$; and in the cosine sum only the $n=m$ term survives, contributing $a_m\cdot L$. Thus
$$
a_m = \frac{1}{L}\int_{-L}^{L} f(x)\cos\!\frac{m\pi x}{L}\,dx,\qquad m\ge 1.
$$
4. The constant term: integrate the bare series over $[-L,L]$. All sines and cosines integrate to $0$ (step 3), leaving $\int_{-L}^{L} f\,dx = \frac{a_0}{2}\cdot 2L = a_0 L$, so $a_0 = \frac1L\int_{-L}^{L}f\,dx$. Writing the constant as $a_0/2$ makes this the $m=0$ case of the $a_m$ formula — that is the whole reason for the "/2".
5. Identically, multiplying by $\sin(m\pi x/L)$ gives $b_m = \frac1L\int_{-L}^{L} f(x)\sin(m\pi x/L)\,dx$.

**Worked example: the square wave.** Let $f(x)=-1$ on $(-\pi,0)$ and $+1$ on $(0,\pi)$, period $2\pi$ (so $L=\pi$).
1. $f$ is odd, so all $a_m=0$ (an odd function times the even $\cos$ is odd, integral over symmetric interval is $0$).
2. $b_m=\frac1\pi\int_{-\pi}^\pi f(x)\sin(mx)\,dx = \frac2\pi\int_0^\pi \sin(mx)\,dx$ (the integrand $f\sin$ is even, doubling the half-interval).
3. $\int_0^\pi\sin(mx)\,dx = \frac{1-\cos(m\pi)}{m} = \frac{1-(-1)^m}{m}$, which is $0$ for even $m$ and $2/m$ for odd $m$.
4. Hence $b_m = \frac{4}{m\pi}$ for odd $m$, $0$ for even $m$, giving
$$
f(x)=\frac{4}{\pi}\left(\sin x + \frac{\sin 3x}{3} + \frac{\sin 5x}{5}+\cdots\right).
$$
At $x=\pi/2$ this predicts $f=1=\frac4\pi(1-\tfrac13+\tfrac15-\cdots)$, i.e. $1-\tfrac13+\tfrac15-\cdots=\pi/4$ — the Leibniz series for $\pi$, a satisfying sanity check.

**A second worked example: a cosine-only signal.** Let $f(x)=x^2$ on $[-\pi,\pi]$, period $2\pi$. This even, continuous function should have only cosine terms.
1. $b_n=0$ (even function times odd sine integrates to zero over the symmetric interval).
2. $a_0=\frac1\pi\int_{-\pi}^\pi x^2dx=\frac2\pi\cdot\frac{\pi^3}{3}=\frac{2\pi^2}{3}$.
3. $a_n=\frac2\pi\int_0^\pi x^2\cos(nx)\,dx$. Integrate by parts twice: $\int x^2\cos(nx)dx=\frac{x^2\sin nx}{n}+\frac{2x\cos nx}{n^2}-\frac{2\sin nx}{n^3}$. At $x=\pi$ the sine terms vanish and $\cos n\pi=(-1)^n$, giving $a_n=\frac2\pi\cdot\frac{2\pi(-1)^n}{n^2}=\frac{4(-1)^n}{n^2}$.
4. Hence
$$
x^2=\frac{\pi^2}{3}+4\sum_{n=1}^\infty\frac{(-1)^n}{n^2}\cos(nx).
$$
Evaluate at $x=\pi$ (where $f=\pi^2$, and the series converges to $\pi^2$ by continuity of the periodic extension at the seam): $\pi^2=\frac{\pi^2}{3}+4\sum_n\frac{(-1)^n(-1)^n}{n^2}=\frac{\pi^2}{3}+4\sum_n\frac1{n^2}$, so $\sum_n\frac1{n^2}=\frac{\pi^2}{6}$ — the Basel problem, solved by a Fourier series. (Evaluating instead at $x=0$ gives the alternating cousin $\sum\frac{(-1)^{n-1}}{n^2}=\frac{\pi^2}{12}$.)

**Pitfall.** Orthogonality holds over *any* interval of length $2L$, but the integrals must run over exactly one full period; integrating over a partial period destroys the cancellations in step 3.

<a id="s2"></a>
### Convergence, the Gibbs phenomenon, and the complex form

**What & why.** Writing down coefficients is one thing; knowing the series actually *equals* $f$ is another. Here we state when convergence holds, expose the famous "overshoot" near jumps, and recast everything in the cleaner complex-exponential language we use for the rest of the guide.

**Pointwise convergence (Dirichlet).** Suppose $f$ is periodic with period $2L$, and on one period it is piecewise continuous with a piecewise-continuous derivative (it has finitely many jumps and corners). Then at every point $x$ the Fourier series converges to the *average of the left and right limits*:
$$
\frac{a_0}{2}+\sum_{n=1}^\infty\Big[a_n\cos\tfrac{n\pi x}{L}+b_n\sin\tfrac{n\pi x}{L}\Big]=\frac{f(x^-)+f(x^+)}{2}.
$$
At points of continuity $f(x^-)=f(x^+)=f(x)$, so the series equals $f(x)$. At a jump it splits the difference. We state this as the working criterion; its proof uses the Dirichlet kernel and is standard, but the key consequence to internalize is the "midpoint of a jump" rule. For our square wave, at $x=0$ the series gives $\tfrac12(-1+1)=0$, exactly the midpoint, even though $f$ itself was not defined there.

**The Gibbs phenomenon.** Near a jump discontinuity, the partial sums of the series *overshoot* the true value by a fixed percentage that does **not** shrink as you add more terms — only the width of the overshoot shrinks. Concretely, the overshoot settles at about $8.95\%$ of the half-jump (the distance from the midpoint to one side). The numerical fingerprint is the constant
$$
\frac{1}{\pi}\int_0^{\pi}\frac{\sin t}{t}\,dt \approx 0.5895,
$$
so for a unit one-sided step (the true value jumping to $1$) the partial sum peaks at about $1.0895$. Intuition: you are trying to build a vertical cliff out of smooth waves; no finite combination of smooth functions can have a true jump, so the best it can do is ring near the edge. Pitfall: refining the sum does not "fix" the spike — it merely pushes it closer to the jump. This matters in signal processing, where it causes ringing artifacts near sharp edges.

**Where the $8.95\%$ comes from.** Near a unit jump, the partial sum $S_N$ behaves like an integral of the Dirichlet kernel up to the location of its first side lobe; the peak value is governed by the **sine integral** $\mathrm{Si}(\pi)=\int_0^\pi\frac{\sin t}{t}\,dt\approx1.8519$. For a unit one-sided step whose true value rises to $1$, the partial sum reaches about $1.0895$ at its peak — an overshoot of $\approx8.95\%$ of the half-jump. Crucially this number is *independent of $N$*: increasing $N$ moves the overshoot peak closer to the discontinuity (the lobe narrows like $1/N$) but never lowers its height. The practical fix is not "more terms" but **windowing** — multiplying the coefficients by a taper (Fejér, Hann, etc.) that softens the kernel's side lobes at the cost of a slightly blurrier edge.

**The complex exponential form.** Euler's formula $e^{i\theta}=\cos\theta+i\sin\theta$ lets us bundle each $\cos$/$\sin$ pair into a single exponential. We claim
$$
f(x)=\sum_{n=-\infty}^{\infty} c_n\, e^{i n\pi x/L},\qquad c_n=\frac{1}{2L}\int_{-L}^{L} f(x)\,e^{-i n\pi x/L}\,dx.
$$
**Derivation.**
1. From Euler, $\cos\theta=\tfrac12(e^{i\theta}+e^{-i\theta})$ and $\sin\theta=\tfrac1{2i}(e^{i\theta}-e^{-i\theta})$.
2. Substitute into the real series term $a_n\cos\frac{n\pi x}{L}+b_n\sin\frac{n\pi x}{L}$ with $\theta=n\pi x/L$:
$$
a_n\cdot\tfrac12(e^{i\theta}+e^{-i\theta})+b_n\cdot\tfrac1{2i}(e^{i\theta}-e^{-i\theta})
=\tfrac12(a_n-i b_n)e^{i\theta}+\tfrac12(a_n+i b_n)e^{-i\theta},
$$
using $1/i=-i$. So defining $c_n=\tfrac12(a_n-ib_n)$ for $n>0$, $c_{-n}=\tfrac12(a_n+ib_n)$, and $c_0=a_0/2$, the real series becomes the two-sided sum over all integers $n$.
3. The coefficient formula follows by the same orthogonality trick in complex form. The exponentials satisfy $\int_{-L}^{L}e^{i m\pi x/L}\overline{e^{i n\pi x/L}}\,dx=\int_{-L}^{L}e^{i(m-n)\pi x/L}\,dx$, which equals $2L$ when $m=n$ and $0$ otherwise (by the same antiderivative argument as in [s1](#s1), since $e^{ik\pi x/L}$ over a full period integrates to zero for integer $k\ne0$). Multiplying $f=\sum_n c_n e^{in\pi x/L}$ by $e^{-im\pi x/L}$, integrating, and keeping only the surviving $n=m$ term gives $\int_{-L}^L f\,e^{-im\pi x/L}\,dx = c_m\cdot 2L$, hence the boxed $c_m$. $\blacksquare$

The complex form is symmetric, compact, and the natural starting point for the transform.

**Where the convergence claim comes from (the Dirichlet kernel).** It is worth seeing *why* the partial sums approach the midpoint of a jump, rather than taking it on faith. Let $S_N(x)$ be the sum of the first $N$ harmonics. Substituting the integral formulas for the coefficients into $S_N$ and collecting the geometric sum of exponentials gives
$$
S_N(x)=\frac{1}{2L}\int_{-L}^{L} f(x')\,D_N\!\Big(\frac{\pi(x-x')}{L}\Big)\,dx',\qquad D_N(\theta)=\frac{\sin\!\big((N+\tfrac12)\theta\big)}{\sin(\theta/2)}.
$$
1. The function $D_N$ is the **Dirichlet kernel**. It comes from summing $\sum_{n=-N}^{N}e^{in\theta}$, a finite geometric series with ratio $e^{i\theta}$; the closed form $\frac{\sin((N+1/2)\theta)}{\sin(\theta/2)}$ follows by multiplying top and bottom by $e^{-i\theta/2}-e^{i\theta/2}$ and using $e^{i\phi}-e^{-i\phi}=2i\sin\phi$.
2. $D_N$ integrates to $2\pi$ over a period (all terms but $n=0$ vanish), so $S_N$ is a *weighted average* of $f$ with total weight $1$.
3. As $N\to\infty$ the kernel becomes ever more concentrated near $\theta=0$ (its central spike narrows and the side lobes oscillate fast and cancel against any continuous $f$). The mass piles up at $x'=x$, so the weighted average tends to $f(x)$ at points of continuity, and to the midpoint $\tfrac12(f(x^-)+f(x^+))$ at a jump because the kernel is symmetric and splits its weight evenly across the two sides.

This is the engine behind the Dirichlet criterion, and the slowly decaying side lobes of $D_N$ are exactly what produce the Gibbs overshoot.

**A second example: the triangle wave.** Let $f(x)=|x|$ on $[-\pi,\pi]$, extended with period $2\pi$. This $f$ is *continuous* (no jumps), so by Dirichlet the series equals $f$ everywhere and there is no Gibbs overshoot.
1. $f$ is even, so all $b_n=0$.
2. $a_0=\frac1\pi\int_{-\pi}^\pi|x|\,dx=\frac2\pi\int_0^\pi x\,dx=\frac2\pi\cdot\frac{\pi^2}{2}=\pi$.
3. $a_n=\frac2\pi\int_0^\pi x\cos(nx)\,dx$; integrating by parts ($u=x$, $dv=\cos(nx)dx$) gives $\frac2\pi\big[\frac{x\sin nx}{n}+\frac{\cos nx}{n^2}\big]_0^\pi=\frac{2}{\pi n^2}(\cos n\pi-1)=\frac{2((-1)^n-1)}{\pi n^2}$, which is $0$ for even $n$ and $-\frac{4}{\pi n^2}$ for odd $n$.
4. Hence
$$
|x|=\frac{\pi}{2}-\frac{4}{\pi}\Big(\cos x+\frac{\cos 3x}{9}+\frac{\cos 5x}{25}+\cdots\Big).
$$
Setting $x=0$ gives $0=\frac\pi2-\frac4\pi\sum_{k\ge0}\frac1{(2k+1)^2}$, i.e. $\sum_{k\ge0}\frac1{(2k+1)^2}=\frac{\pi^2}{8}$ — the same identity Parseval will produce in [s3](#s3), here from continuity at a single point. Notice the coefficients decay like $1/n^2$ for this continuous function, versus $1/n$ for the discontinuous square wave: **smoother functions have faster-decaying spectra**, a theme that recurs throughout the subject.

<a id="s3"></a>
### Parseval's theorem: energy in the spectrum

**What & why.** The total "energy" of a signal is $\int |f|^2$ (in physics, $|f|^2$ is power, energy density, or probability density). Parseval's theorem says this energy is the *sum of the energies of the individual frequency components* — nothing is lost or double-counted when you switch to the spectral picture. It is the statement that the Fourier decomposition is an *orthonormal* change of basis: it preserves length, like rotating coordinate axes.

**Theorem (Parseval, complex form).** For a $2L$-periodic $f$ with coefficients $c_n$,
$$
\frac{1}{2L}\int_{-L}^{L}|f(x)|^2\,dx=\sum_{n=-\infty}^{\infty}|c_n|^2.
$$

**Proof.**
1. Write $|f|^2=f\,\overline{f}$ and expand one factor as its series: $\overline{f(x)}=\sum_m \overline{c_m}\,e^{-im\pi x/L}$ (conjugating $f=\sum_m c_m e^{im\pi x/L}$ term by term, using $\overline{e^{i\theta}}=e^{-i\theta}$).
2. Then
$$
\int_{-L}^{L}|f|^2\,dx=\int_{-L}^{L}\Big(\sum_n c_n e^{in\pi x/L}\Big)\Big(\sum_m \overline{c_m}\,e^{-im\pi x/L}\Big)dx
=\sum_{n,m}c_n\overline{c_m}\int_{-L}^{L}e^{i(n-m)\pi x/L}\,dx,
$$
interchanging sum and integral (valid for the convergent series we treat).
3. By the complex orthogonality from [s2](#s2), the inner integral is $2L$ if $n=m$ and $0$ otherwise. Only diagonal terms survive: $\sum_n c_n\overline{c_n}\cdot 2L = 2L\sum_n |c_n|^2$.
4. Divide by $2L$. $\blacksquare$

In real-coefficient form, substituting $c_0=a_0/2$ and $|c_n|^2+|c_{-n}|^2=\tfrac12(a_n^2+b_n^2)$ gives
$$
\frac1L\int_{-L}^{L}|f|^2\,dx=\frac{a_0^2}{2}+\sum_{n=1}^\infty(a_n^2+b_n^2).
$$

**The transform version (Plancherel).** The same energy-conservation statement holds for the Fourier transform of [s4](#s4):
$$
\int_{-\infty}^\infty|f(x)|^2\,dx=\frac{1}{2\pi}\int_{-\infty}^\infty|\hat f(k)|^2\,dk.
$$
*Sketch of proof.* Write the left side as $\int f\,\overline f\,dx$, replace one factor by its inverse-transform integral $\overline{f(x)}=\frac1{2\pi}\int\overline{\hat f(k)}e^{-ikx}dk$, swap the order of integration, and recognize $\int f(x)e^{-ikx}dx=\hat f(k)$. The leftover $\frac1{2\pi}\int|\hat f|^2dk$ results. $\blacksquare$ The factor $1/(2\pi)$ is the same bookkeeping constant from our convention; in the symmetric $1/\sqrt{2\pi}$ convention the two sides are literally equal, which is why physicists favour it. Either way, *the transform preserves total energy* — it is an isometry, a rotation of an infinite-dimensional space. In quantum mechanics this is the statement that total probability is the same whether you compute it in position space, $\int|\psi(x)|^2dx$, or momentum space.

**Worked example.** Apply real-form Parseval to the square wave of [s1](#s1) ($L=\pi$, $a_n=0$, $b_n=4/(n\pi)$ for odd $n$). The left side: $\frac1\pi\int_{-\pi}^\pi |{\pm1}|^2dx=\frac1\pi\cdot 2\pi=2$. The right side: $\sum_{n\text{ odd}}\big(\tfrac{4}{n\pi}\big)^2=\frac{16}{\pi^2}\sum_{n\text{ odd}}\frac1{n^2}$. Equate:
$$
2=\frac{16}{\pi^2}\sum_{k=0}^\infty\frac{1}{(2k+1)^2}\;\Longrightarrow\;\sum_{k=0}^\infty\frac{1}{(2k+1)^2}=\frac{\pi^2}{8}.
$$
So Parseval applied to a square wave proves $1+\tfrac19+\tfrac1{25}+\cdots=\pi^2/8$ — and from it one recovers $\sum 1/n^2=\pi^2/6$ (the odd terms are $\pi^2/8$; the even terms are $\tfrac14\sum 1/n^2$, so $S=\pi^2/8+\tfrac14 S$, giving $S=\pi^2/6$). A beautiful payoff for free.

**A second numeric: how much energy in the first few harmonics?** A practical use of Parseval is to ask what fraction of a signal's energy lives in its lowest modes — this is the basis of lossy compression. For the square wave the total energy per period (left side above) is $2$, and the energy in harmonic $n$ is $b_n^2=\big(\tfrac{4}{n\pi}\big)^2=\tfrac{16}{\pi^2 n^2}$ for odd $n$.
- Fundamental ($n=1$): $\tfrac{16}{\pi^2}\approx1.621$, i.e. $\approx81.1\%$ of the total energy.
- Through $n=3$: add $\tfrac{16}{9\pi^2}\approx0.180$, cumulative $\approx90.1\%$.
- Through $n=5$: add $\tfrac{16}{25\pi^2}\approx0.0648$, cumulative $\approx93.4\%$.

So three terms already carry over $90\%$ of the energy — which is why truncating a Fourier series (or a JPEG's discrete-cosine coefficients) discards little perceptible content while shrinking the data dramatically. Parseval is the bookkeeping that makes "keep the big coefficients, drop the small ones" a principled compression strategy.

## Part B — The Fourier transform

<a id="s4"></a>
### The Fourier transform and its inverse

**What & why.** A non-periodic pulse contains *all* frequencies, not a discrete ladder of them. We get there by letting the period $2L\to\infty$ in a Fourier series: the spacing between allowed frequencies $\Delta k=\pi/L$ shrinks to zero, the sum becomes an integral, and the discrete coefficients $c_n$ become a continuous function $\hat f(k)$ — the **spectrum**.

**Heuristic limit.** Write the complex series with $k_n=n\pi/L$ and $\Delta k=\pi/L$:
$$
f(x)=\sum_n c_n e^{ik_n x},\quad c_n=\frac{1}{2L}\int_{-L}^L f(x')e^{-ik_n x'}dx'.
$$
Define $\hat f(k_n):=2L\,c_n=\int_{-L}^L f(x')e^{-ik_n x'}dx'$. Then $c_n=\hat f(k_n)\,\Delta k/(2\pi)$, so $f(x)=\frac1{2\pi}\sum_n \hat f(k_n)e^{ik_n x}\Delta k$. As $L\to\infty$, $\Delta k\to0$ and the Riemann sum becomes an integral. This motivates the definitions.

**Definition (convention used in this guide).** For an absolutely integrable function $f$ (i.e. $\int_{-\infty}^\infty|f|\,dx<\infty$), the **Fourier transform** and its **inverse** are
$$
\hat f(k)=\mathcal F\{f\}(k)=\int_{-\infty}^{\infty} f(x)\,e^{-ikx}\,dx,
\qquad
f(x)=\mathcal F^{-1}\{\hat f\}(x)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\hat f(k)\,e^{ikx}\,dk.
$$
We state the convention explicitly because conventions differ. Ours puts no constant on the forward transform and $1/(2\pi)$ on the inverse, and uses the sign $e^{-ikx}$ forward. (Symmetric physics texts use $1/\sqrt{2\pi}$ on each; signal-processing texts use frequency $\nu$ with $e^{-2\pi i\nu x}$ and no prefactor. All are equivalent up to bookkeeping; mixing them is the most common error in the subject.)

**The inversion theorem.** If $f$ is continuous, absolutely integrable, and $\hat f$ is also absolutely integrable, then $\mathcal F^{-1}\{\mathcal F\{f\}\}=f$. The proof rests on knowing the transform of a Gaussian (computed in [s6](#s6)) used as a convergence factor, or on the delta-function machinery of [s7](#s7); we will in fact *derive* the inversion constant $1/(2\pi)$ in [s7](#s7) from $\int e^{ikx}dk = 2\pi\,\delta(x)$. For now, accept the pair as the dictionary between position $x$ and wavenumber $k$.

**Reading the definition.** $\hat f(k)$ asks: "how much of the pure wave $e^{ikx}$ (wavenumber $k$, i.e. wavelength $2\pi/k$) is contained in $f$?" The forward transform *projects* $f$ onto each wave by integrating against its conjugate $e^{-ikx}$; the inverse *reassembles* $f$ by summing all the waves back, weighted by $\hat f(k)$. The same projection-and-reassembly story as the Fourier series of [s1](#s1), but with a *continuum* of axes $\{e^{ikx}:k\in\mathbb R\}$ instead of a discrete ladder, and an integral $\int dk$ in place of a sum $\sum_n$.

**The discrete-to-continuous dictionary, made explicit.** It pays to line up the series and transform side by side, since each formula on the left becomes its right-hand counterpart as the period $2L\to\infty$:
- discrete frequencies $k_n=n\pi/L$ $\;\to\;$ continuous $k\in\mathbb R$;
- coefficient $c_n$ $\;\to\;$ density $\hat f(k)$, related by $c_n\approx\hat f(k_n)\,\Delta k/(2\pi)$;
- sum $\sum_n(\cdots)$ $\;\to\;$ integral $\frac{1}{2\pi}\int(\cdots)\,dk$;
- orthogonality $\int_{-L}^L e^{i(m-n)\pi x/L}dx=2L\,\delta_{mn}$ $\;\to\;$ completeness $\int_{-\infty}^\infty e^{i(k-k')x}dx=2\pi\,\delta(k-k')$ (the continuous analogue, with the Kronecker delta becoming the Dirac delta of [s7](#s7)).

This last line is the deepest part of the dictionary: the *discrete* orthogonality of harmonics becomes the *continuous* orthogonality of waves, with the Dirac delta playing the role the Kronecker delta played for series. It is the technical engine of every transform identity that follows.

**Existence note / pitfall.** Absolute integrability guarantees the forward integral converges (the integrand is bounded by $|f|$). Many functions we care about — a constant, $\sin x$, the delta — are *not* absolutely integrable, and their transforms exist only as **distributions** ([s7](#s7)). Knowing which regime you are in prevents nonsense.

**A first worked transform.** Take $f(x)=e^{-|x|}$ (a symmetric decaying spike). Then, splitting at $0$,
$$
\hat f(k)=\int_{-\infty}^{0}e^{x}e^{-ikx}dx+\int_{0}^{\infty}e^{-x}e^{-ikx}dx=\frac{1}{1-ik}+\frac{1}{1+ik}=\frac{2}{1+k^2}.
$$
A spike in $x$ with width $\sim1$ became a hump in $k$ with width $\sim1$ — comparable widths because the spike was already moderate. We will see in [s6](#s6) that *narrowing* the spike *broadens* the hump.

**The uncertainty principle, stated.** Define the spreads (standard deviations) of $|f|^2$ and $|\hat f|^2$ about their means as $\Delta x$ and $\Delta k$. A theorem (proved via the Cauchy–Schwarz inequality applied to $xf$ and $f'$) states
$$
\Delta x\,\Delta k\ \ge\ \tfrac12.
$$
The product of the position spread and the wavenumber spread cannot be made smaller than $1/2$; sharpening one blurs the other. In quantum mechanics $p=\hbar k$, so $\Delta x\,\Delta p\ge\hbar/2$ — the Heisenberg uncertainty principle is this Fourier inequality in disguise. Equality holds exactly for the Gaussian ([s6](#s6)), the minimum-uncertainty shape.

<a id="s5"></a>
### Properties: linearity, shift, scaling, derivative, convolution

**What & why.** These five rules turn the transform into a calculus. Each says "a simple operation in $x$-space corresponds to a simple operation in $k$-space." We prove each from the definition. Let $\hat f=\mathcal F\{f\}$, $\hat g=\mathcal F\{g\}$.

**(1) Linearity.** $\mathcal F\{\alpha f+\beta g\}=\alpha\hat f+\beta\hat g$.
*Proof.* $\int(\alpha f+\beta g)e^{-ikx}dx=\alpha\int f e^{-ikx}dx+\beta\int g e^{-ikx}dx$ by linearity of the integral. $\blacksquare$

**(2) Shift (translation).** $\mathcal F\{f(x-a)\}(k)=e^{-ika}\hat f(k)$.
*Proof.* By definition $\mathcal F\{f(x-a)\}=\int f(x-a)e^{-ikx}dx$. Substitute $u=x-a$, $du=dx$, $x=u+a$ (a valid change of variable, linear and onto $\mathbb R$): $=\int f(u)e^{-ik(u+a)}du=e^{-ika}\int f(u)e^{-iku}du=e^{-ika}\hat f(k)$. $\blacksquare$ A shift in position becomes a *phase* in frequency — the magnitude $|\hat f|$ is unchanged, only the phase rotates. (Physically: moving a pulse in time does not change its frequency content, only the phase clocking.)

**(3) Scaling.** For $a\ne0$, $\mathcal F\{f(ax)\}(k)=\frac{1}{|a|}\hat f\!\big(\tfrac{k}{a}\big)$.
*Proof.* $\int f(ax)e^{-ikx}dx$; substitute $u=ax$, $du=a\,dx$. For $a>0$: $=\frac1a\int f(u)e^{-iku/a}du=\frac1a\hat f(k/a)$. For $a<0$ the limits flip, contributing another sign that combines to give $\frac{1}{|a|}$. Combining, $\frac1{|a|}\hat f(k/a)$. $\blacksquare$ This is the *uncertainty trade-off in one line*: squeezing $f$ in $x$ (large $a$) stretches $\hat f$ in $k$ and vice versa. Narrow in position $\Leftrightarrow$ broad in momentum.

**(4) Derivative rule.** If $f$ is differentiable with $f(x)\to0$ as $|x|\to\infty$, then $\mathcal F\{f'\}(k)=ik\,\hat f(k)$.
*Proof.* $\mathcal F\{f'\}=\int_{-\infty}^\infty f'(x)e^{-ikx}dx$. Integrate by parts with $u=e^{-ikx}$, $dv=f'(x)dx$ (so $du=-ik\,e^{-ikx}dx$, $v=f$):
$$
=\Big[f(x)e^{-ikx}\Big]_{-\infty}^{\infty}-\int_{-\infty}^\infty f(x)(-ik)e^{-ikx}dx.
$$
The boundary term vanishes because $f\to0$ and $|e^{-ikx}|=1$. The remaining term is $ik\int f e^{-ikx}dx=ik\hat f(k)$. $\blacksquare$ This is the workhorse: **differentiation becomes multiplication by $ik$.** Iterating, $\mathcal F\{f^{(n)}\}=(ik)^n\hat f$, which turns a constant-coefficient differential equation into a polynomial equation in $k$. (In quantum mechanics this is exactly $\hat p=-i\hbar\,d/dx$ acting as multiplication by $\hbar k=p$ in momentum space.)

**(5) Convolution theorem.** Define the **convolution** $(f*g)(x)=\int_{-\infty}^\infty f(y)g(x-y)\,dy$. Then $\mathcal F\{f*g\}=\hat f\cdot\hat g$.
*Proof.*
1. By definition, $\mathcal F\{f*g\}(k)=\int_{x}\Big(\int_{y}f(y)g(x-y)\,dy\Big)e^{-ikx}\,dx$.
2. Interchange the order of integration (Fubini's theorem, valid since $f,g$ absolutely integrable makes the double integral absolutely convergent): $=\int_y f(y)\Big(\int_x g(x-y)e^{-ikx}dx\Big)dy$.
3. The inner integral is $\mathcal F\{g(x-y)\}(k)=e^{-iky}\hat g(k)$ by the shift rule (2), treating $y$ as the shift.
4. Substitute back: $=\int_y f(y)e^{-iky}\hat g(k)\,dy=\hat g(k)\int_y f(y)e^{-iky}dy=\hat g(k)\hat f(k)$. $\blacksquare$

A *dual* version holds: $\mathcal F\{f\cdot g\}=\frac{1}{2\pi}\,\hat f * \hat g$. The convolution theorem is arguably the single most useful fact in applied Fourier analysis: a tangled smearing operation ($*$) in $x$-space becomes plain multiplication in $k$-space.

**(6) Multiplication by $x$ (the dual of the derivative rule).** $\mathcal F\{x f(x)\}(k)=i\,\dfrac{d}{dk}\hat f(k)$.
*Proof.* Differentiate $\hat f(k)=\int f(x)e^{-ikx}dx$ under the integral sign (justified when $xf$ is absolutely integrable): $\frac{d}{dk}\hat f=\int f(x)(-ix)e^{-ikx}dx=-i\int xf(x)e^{-ikx}dx=-i\,\mathcal F\{xf\}$. Solve for $\mathcal F\{xf\}$. $\blacksquare$ Together with rule (4) this gives a perfect duality: $x\leftrightarrow i\,d/dk$ and $d/dx\leftrightarrow ik$. The roles of position and frequency are mirror images — the structural origin of the position/momentum symmetry of quantum mechanics.

**Worked use of the rules.** Find $\hat f$ for $f(x)=x\,e^{-|x|}$ without integrating from scratch. We know $\mathcal F\{e^{-|x|}\}=\frac{2}{1+k^2}$ ([s4](#s4)). By rule (6),
$$
\mathcal F\{x\,e^{-|x|}\}=i\,\frac{d}{dk}\frac{2}{1+k^2}=i\cdot\frac{-4k}{(1+k^2)^2}=\frac{-4ik}{(1+k^2)^2}.
$$
The answer is purely imaginary and odd in $k$ — correct, since $f$ is a real odd function (real odd $\leftrightarrow$ imaginary odd is a general symmetry of the transform). Building transforms from known ones plus the rules is faster and less error-prone than direct integration.

<a id="s6"></a>
### A table of standard transforms, derived in full

**What & why.** A handful of transforms recur everywhere. We derive each so the table is yours, not memorized. Convention as in [s4](#s4).

**(a) Rectangular pulse.** Let $\Pi_a(x)=1$ for $|x|<a$ and $0$ otherwise.
$$
\hat\Pi_a(k)=\int_{-a}^{a}e^{-ikx}dx=\left.\frac{e^{-ikx}}{-ik}\right|_{-a}^{a}=\frac{e^{-ika}-e^{ika}}{-ik}=\frac{2\sin(ka)}{k},
$$
using $e^{i\theta}-e^{-i\theta}=2i\sin\theta$. So $\hat\Pi_a(k)=2a\,\mathrm{sinc}(ka)$ where $\mathrm{sinc}\,u=\sin u/u$. A sharp box in $x$ gives an oscillating, slowly decaying sinc in $k$ — the origin of diffraction ripples and Gibbs ringing.

**(b) One-sided exponential.** Let $f(x)=e^{-bx}$ for $x>0$, $0$ for $x<0$, with $b>0$.
$$
\hat f(k)=\int_0^\infty e^{-bx}e^{-ikx}dx=\int_0^\infty e^{-(b+ik)x}dx=\left.\frac{e^{-(b+ik)x}}{-(b+ik)}\right|_0^\infty=\frac{1}{b+ik},
$$
the boundary at $\infty$ vanishing since $\mathrm{Re}(b+ik)=b>0$ forces $e^{-(b+ik)x}\to0$.

**(c) Two-sided (symmetric) exponential.** Let $f(x)=e^{-b|x|}$, $b>0$. Split the integral:
$$
\hat f(k)=\int_{-\infty}^0 e^{bx}e^{-ikx}dx+\int_0^\infty e^{-bx}e^{-ikx}dx=\frac{1}{b-ik}+\frac{1}{b+ik}=\frac{2b}{b^2+k^2},
$$
combining over a common denominator. This **Lorentzian** is the spectral lineshape of a damped oscillator; its width in $k$ is set by $b$ (the damping), another uncertainty trade-off.

**(d) Gaussian — the self-dual transform.** Let $f(x)=e^{-x^2/(2\sigma^2)}$.
1. $\hat f(k)=\int_{-\infty}^\infty e^{-x^2/(2\sigma^2)}e^{-ikx}dx$. Complete the square in the exponent: $-\frac{x^2}{2\sigma^2}-ikx=-\frac{1}{2\sigma^2}\big(x^2+2ik\sigma^2 x\big)=-\frac{1}{2\sigma^2}\big((x+ik\sigma^2)^2+k^2\sigma^4\big)$.
2. So $\hat f(k)=e^{-k^2\sigma^2/2}\int_{-\infty}^\infty e^{-(x+ik\sigma^2)^2/(2\sigma^2)}dx$.
3. The remaining integral equals $\int_{-\infty}^\infty e^{-x^2/(2\sigma^2)}dx=\sigma\sqrt{2\pi}$ (the standard Gaussian integral $\int e^{-au^2}du=\sqrt{\pi/a}$ with $a=1/(2\sigma^2)$). Shifting the contour by the imaginary amount $ik\sigma^2$ leaves the value unchanged because $e^{-z^2}$ is entire and decays in the relevant strip — a contour-shift argument from complex analysis, which we invoke as the one external fact here.
4. Therefore
$$
\mathcal F\{e^{-x^2/(2\sigma^2)}\}(k)=\sigma\sqrt{2\pi}\;e^{-\sigma^2 k^2/2}.
$$
A Gaussian transforms into a Gaussian — the *only* shape that does so. Its width in $x$ is $\sigma$; its width in $k$ is $1/\sigma$; their product is fixed at $1$. (Here $\sigma$ and $1/\sigma$ are the $e^{-1/2}$ widths — the half-widths at which the Gaussian falls to $e^{-1/2}$ of its peak — whose product is $1$; these are *not* the rms spreads $\Delta x,\Delta k$ of [s4](#s4), whose product is $\tfrac12$. For a Gaussian the rms spreads are $\Delta x=\sigma/\sqrt2$ and $\Delta k=1/(\sigma\sqrt2)$, giving $\Delta x\,\Delta k=\tfrac12$.) This is the function that *saturates* the uncertainty bound, which is why the ground state of the harmonic oscillator (a Gaussian) is the minimum-uncertainty quantum state.

**Summary table.**

| $f(x)$ | $\hat f(k)=\int f e^{-ikx}dx$ |
| --- | --- |
| Box $\Pi_a$ | $\dfrac{2\sin ka}{k}$ |
| $e^{-bx}\,\theta(x)$, $b>0$ | $\dfrac{1}{b+ik}$ |
| $e^{-b|x|}$, $b>0$ | $\dfrac{2b}{b^2+k^2}$ |
| $e^{-x^2/2\sigma^2}$ | $\sigma\sqrt{2\pi}\,e^{-\sigma^2k^2/2}$ |
| $\delta(x)$ (see [s7](#s7)) | $1$ |
| $1$ | $2\pi\,\delta(k)$ |
| $\cos(k_0 x)$ | $\pi[\delta(k-k_0)+\delta(k+k_0)]$ |

**A transform of a pure wave.** Using $\mathcal F\{1\}=2\pi\delta(k)$ and the shift-in-$k$ dual of the shift rule, $\mathcal F\{e^{ik_0x}\}=2\pi\delta(k-k_0)$ (a single pure wave is one spike in frequency). Then
$$
\mathcal F\{\cos k_0 x\}=\mathcal F\{\tfrac12(e^{ik_0x}+e^{-ik_0x})\}=\pi\big[\delta(k-k_0)+\delta(k+k_0)\big],
$$
two spikes at $\pm k_0$ — a cosine is exactly its two frequencies, no spread. This is the limiting opposite of the delta: the delta is one point in $x$ and flat in $k$; a pure wave is flat in $x$ and one point in $k$. Everything else lives between these extremes.

**Symmetry summary (useful as a check).** From the definition one reads off: $f$ real $\Rightarrow$ $\hat f(-k)=\overline{\hat f(k)}$ (Hermitian symmetry); $f$ even $\Rightarrow$ $\hat f$ even and real-valued (the cosine transform); $f$ odd $\Rightarrow$ $\hat f$ odd and imaginary (the sine transform). Use these to catch algebra errors instantly — every derived transform above obeys them.

<a id="s7"></a>
### The Dirac delta as a distribution

**What & why.** Physics constantly wants an "infinitely tall, infinitely thin spike of unit area" — a point charge, an instantaneous impulse, a perfectly localized particle. No ordinary function does this. The honest object is a **distribution** (generalized function): something defined not by its values but by *what it does when integrated against a smooth test function*.

**Test functions.** A **test function** $\varphi$ is smooth (infinitely differentiable) and zero outside some bounded interval (compact support). A distribution $T$ is a linear map sending each test function to a number, written $\langle T,\varphi\rangle$.

**The delta, defined by its action.** The **Dirac delta** $\delta$ is the distribution
$$
\langle\delta,\varphi\rangle=\varphi(0).
$$
For an ordinary function $g$ we would write $\langle g,\varphi\rangle=\int g\varphi\,dx$; by analogy we *write* $\int\delta(x)\varphi(x)\,dx=\varphi(0)$, but this integral is shorthand for the defining rule, not a Riemann integral. More generally the **sifting property** is
$$
\int_{-\infty}^\infty \delta(x-a)\,\varphi(x)\,dx=\varphi(a):
$$
integrating against $\delta(x-a)$ "sifts out" the value of $\varphi$ at the single point $x=a$. (Proof: substitute $u=x-a$; $\int\delta(u)\varphi(u+a)du=\varphi(0+a)=\varphi(a)$ by the definition.)

**Delta as a limit.** Take any "bump of unit area" and squeeze it. For instance the Gaussian $g_\epsilon(x)=\frac{1}{\epsilon\sqrt{2\pi}}e^{-x^2/(2\epsilon^2)}$ has $\int g_\epsilon=1$ for every $\epsilon$. As $\epsilon\to0$ it grows tall and thin. For any continuous $\varphi$,
$$
\int g_\epsilon(x)\varphi(x)\,dx\xrightarrow{\epsilon\to0}\varphi(0),
$$
because the mass concentrates at $0$ where $\varphi\approx\varphi(0)$ and $\int g_\epsilon=1$. So $g_\epsilon\to\delta$ in the distributional sense. Many families work (boxes, Lorentzians, sincs); what matters is unit area collapsing to a point. Pitfall: "$\delta(0)=\infty$" is meaningless as a value — only integrals against test functions have meaning.

**Fourier transform of the delta.** By the definition with the test function $e^{-ikx}$ (treated formally),
$$
\hat\delta(k)=\int_{-\infty}^\infty\delta(x)e^{-ikx}dx=e^{-ik\cdot0}=1.
$$
The delta contains *every* frequency in equal measure — a perfectly localized spike is maximally spread in $k$. This is the extreme of the uncertainty trade-off.

**Fourier transform of a constant, and the inversion constant.** Run the inverse transform on $\hat\delta=1$:
$$
\delta(x)=\mathcal F^{-1}\{1\}=\frac{1}{2\pi}\int_{-\infty}^\infty e^{ikx}dk\quad\Longrightarrow\quad \int_{-\infty}^\infty e^{ikx}\,dk=2\pi\,\delta(x).
$$
This is the **completeness relation** — the engine behind every inversion proof. Reading it the other way (transform of the constant $1$): $\mathcal F\{1\}(k)=\int e^{-ikx}dx=2\pi\,\delta(k)$. A constant (DC) signal is pure zero-frequency. These two facts close the table in [s6](#s6) and justify the $1/(2\pi)$ in the inverse transform: it is exactly the constant that makes $\int e^{ikx}dk=2\pi\delta(x)$ consistent with $\delta$ sifting out $f(x)$ in the inversion integral $f(x)=\frac1{2\pi}\iint f(x')e^{ik(x-x')}dx'dk$.

**A consistency check via the completeness relation.** The following is *not* an independent proof of inversion — it is circular, since the completeness relation $\int e^{ikx}dk=2\pi\delta(x)$ was itself obtained from inversion above. Read it instead as a consistency check that the $1/(2\pi)$ and the delta hang together. (The genuinely non-circular proof regularizes the divergent inner integral with a Gaussian factor $e^{-\epsilon k^2}$, evaluates it as a true Gaussian for $\epsilon>0$, and lets $\epsilon\to0$ to recover the delta — the route flagged in [s4](#s4) and built from the Gaussian transform of [s6](#s6).)
1. Start from the inverse transform applied to the forward transform: $\mathcal F^{-1}\{\mathcal F\{f\}\}(x)=\frac1{2\pi}\int_k\Big(\int_{x'}f(x')e^{-ikx'}dx'\Big)e^{ikx}\,dk$.
2. Swap the order of integration (Fubini, valid under our integrability hypotheses): $=\int_{x'}f(x')\Big(\frac1{2\pi}\int_k e^{ik(x-x')}\,dk\Big)dx'$.
3. The inner integral is $\frac1{2\pi}\cdot 2\pi\,\delta(x-x')=\delta(x-x')$ by the completeness relation.
4. By the sifting property, $\int_{x'}f(x')\delta(x-x')\,dx'=f(x)$. Hence $\mathcal F^{-1}\mathcal F=\mathrm{id}$, consistently. The $1/(2\pi)$ is not arbitrary — it is forced.

**More properties of the delta.** Each is defined through its action on a test function $\varphi$.
1. **Scaling:** $\delta(ax)=\frac{1}{|a|}\delta(x)$ for $a\ne0$. Proof: substitute $u=ax$ in $\int\delta(ax)\varphi(x)\,dx=\frac{1}{|a|}\int\delta(u)\varphi(u/a)\,du=\frac{1}{|a|}\varphi(0)$, matching $\frac1{|a|}\langle\delta,\varphi\rangle$. The $|a|$ (not $a$) appears because flipping the limits for $a<0$ contributes a compensating sign.
2. **Derivative of the delta:** define $\langle\delta',\varphi\rangle=-\langle\delta,\varphi'\rangle=-\varphi'(0)$, by analogy with integration by parts (the boundary term vanishes since $\varphi$ has compact support). So $\int\delta'(x)\varphi(x)\,dx=-\varphi'(0)$ — $\delta'$ probes the *slope* of $\varphi$ at $0$.
3. **Composition with a function:** if $g$ has simple zeros at points $x_j$ (where $g(x_j)=0$, $g'(x_j)\ne0$), then
$$
\delta(g(x))=\sum_j\frac{\delta(x-x_j)}{|g'(x_j)|}.
$$
Near each zero $g(x)\approx g'(x_j)(x-x_j)$, so locally $\delta(g(x))=\delta(g'(x_j)(x-x_j))=\frac{1}{|g'(x_j)|}\delta(x-x_j)$ by the scaling rule. Worked instance: $\delta(x^2-a^2)=\frac{1}{2|a|}\big[\delta(x-a)+\delta(x+a)\big]$, since $g'(\pm a)=\pm2a$. This rule is everywhere in physics — it converts energy-conserving delta functions into sums over allowed states.

**The Heaviside step and the delta.** Let $\theta(x)=0$ for $x<0$ and $1$ for $x>0$ (the unit step). As distributions, $\theta'=\delta$: the derivative of a jump is a spike. Proof: $\langle\theta',\varphi\rangle=-\langle\theta,\varphi'\rangle=-\int_0^\infty\varphi'(x)\,dx=-[\varphi]_0^\infty=\varphi(0)=\langle\delta,\varphi\rangle$, using compact support to kill the upper boundary. This is why a sudden switch-on produces an impulse in the rate of change — the mathematical content behind "differentiating an edge gives a spike", and the reason edge-detection filters in image processing are essentially derivative operators.

<a id="s8"></a>
### Convolution, filtering, and correlation

**What & why.** Convolution $(f*g)(x)=\int f(y)g(x-y)dy$ is "smearing $f$ with the shape $g$" — replace each point of $f$ by a little copy of $g$ and add them up. It models every linear, shift-invariant process: blurring an image, the response of a circuit, the echo of a room. Filtering and correlation are its two great applications.

**Why convolution is the universal linear response.** A linear shift-invariant system is fully described by its **impulse response** $h$, the output when the input is a delta spike. Let us write the argument out carefully, because it is the conceptual core of the section.
1. **Decompose the input.** Any input is a continuous superposition of shifted spikes: $f(x)=\int f(y)\,\delta(x-y)\,dy$, by the sifting property of [s7](#s7). Read this as "$f$ is built from a spike of strength $f(y)\,dy$ located at each point $y$."
2. **Linearity.** Call the system's action $\mathcal S$. Linearity means $\mathcal S$ of a sum (here an integral) is the sum of $\mathcal S$ of the pieces: $\mathcal S f(x)=\int f(y)\,\mathcal S[\delta(\,\cdot\,-y)](x)\,dy$.
3. **Shift-invariance.** By definition $\mathcal S[\delta]=h$, and shift-invariance says shifting the input merely shifts the output: $\mathcal S[\delta(\,\cdot\,-y)](x)=h(x-y)$.
4. **Assemble.** Substituting, $\mathcal S f(x)=\int f(y)\,h(x-y)\,dy=(f*h)(x)$.

Thus *every* linear shift-invariant system is a convolution with its impulse response — no exceptions. The convolution theorem ([s5](#s5)) then says: in frequency space the system simply multiplies each frequency by $\hat h(k)$, the **transfer function**. Designing a filter = choosing $\hat h(k)$. This is why the Fourier basis is the "right" one for such systems: it is the basis in which they are diagonal.

**Filtering example.** Pass a signal $f$ through a system with $\hat h(k)=1$ for $|k|<k_c$ and $0$ otherwise (an ideal low-pass filter that keeps low frequencies and removes high ones). In $k$-space the output is $\hat f(k)\hat h(k)$ — high frequencies above $k_c$ are deleted, smoothing the signal. In $x$-space, $h=\mathcal F^{-1}\{\hat h\}=\frac{1}{2\pi}\int_{-k_c}^{k_c}e^{ikx}dk=\frac{\sin(k_c x)}{\pi x}$ (a sinc), so the output is $f*\mathrm{sinc}$ — each point smeared by a sinc. This is exactly how blurring removes sharp detail.

**Worked convolution.** Convolve two identical boxes. Let $f=g=\Pi_{1/2}$ (value $1$ on $(-\tfrac12,\tfrac12)$). Then $(f*g)(x)=\int f(y)g(x-y)dy$ is the length of the overlap of a box centered at $0$ with one centered at $x$. The overlap is $1-|x|$ for $|x|<1$ and $0$ otherwise — a **triangle**. Check via transforms: $\hat\Pi_{1/2}(k)=\frac{2\sin(k/2)}{k}$, so $\widehat{f*g}=\big(\frac{2\sin(k/2)}{k}\big)^2=\frac{4\sin^2(k/2)}{k^2}$, and indeed the transform of the triangle is known to be $\mathrm{sinc}^2$, matching. Two boxes convolve to a triangle — smearing a flat top with a flat top rounds it linearly.

**Correlation.** The **cross-correlation** $(f\star g)(x)=\int \overline{f(y)}\,g(y+x)\,dy$ measures how much $g$, shifted by $x$, resembles $f$. It peaks at the shift where the two signals best line up — the basis of pattern matching, radar ranging, and pitch detection. Its transform is $\mathcal F\{f\star g\}=\overline{\hat f}\,\hat g$ (conjugate on the first factor; the sign flip versus convolution comes from the $g(y+x)$ rather than $g(x-y)$). The special case $g=f$ gives the **autocorrelation**, whose transform $|\hat f|^2$ is the **power spectrum** — the Wiener–Khinchin theorem, the bridge from time-domain correlations to the frequency content of noise.

**Worked correlation: finding a delay.** Suppose a radar emits a pulse $g(t)$ and receives a faint, delayed echo $f(t)=A\,g(t-t_0)+\text{noise}$, and we want the delay $t_0$ (which gives the range). Compute the cross-correlation of the sent and received signals:
$$
(g\star f)(x)=\int \overline{g(y)}\,f(y+x)\,dy=A\int\overline{g(y)}\,g(y+x-t_0)\,dy+(\text{noise term}).
$$
The signal part is $A$ times the autocorrelation of $g$ evaluated at $x-t_0$. Autocorrelation always peaks at argument $0$ (a signal resembles itself best when unshifted, by Cauchy–Schwarz), so $(g\star f)$ peaks at $x=t_0$. Reading off the location of the peak gives the delay, and hence the distance, even when the echo is buried in noise — because noise, being uncorrelated with $g$, contributes no peak. The fast way to compute the correlation for all shifts at once is via transforms: $g\star f=\mathcal F^{-1}\{\overline{\hat g}\,\hat f\}$, an FFT-sized computation rather than a shift-by-shift search.

**Smoothing as low-pass filtering, revisited.** Convolving with a normalized Gaussian $g_\sigma$ blurs a signal. In frequency space this multiplies $\hat f$ by $\hat g_\sigma\propto e^{-\sigma^2k^2/2}$ (from [s6](#s6)), which suppresses high $k$ — fine detail — more strongly the larger $\sigma$ is. So "blur radius" in $x$-space and "cutoff frequency" in $k$-space are reciprocal: a wide blur kills a low cutoff. This single statement underlies Gaussian blur in image editors, antialiasing, and the diffusion of heat (whose Green's function is exactly a spreading Gaussian).

**Worked PDE: heat diffusion by transform.** The heat equation $\partial_t u=D\,\partial_x^2 u$ on the infinite line, with initial temperature $u(x,0)=u_0(x)$, succumbs immediately to the Fourier transform in $x$.
1. Transform in $x$: with $\hat u(k,t)=\int u(x,t)e^{-ikx}dx$, the derivative rule turns $\partial_x^2\mapsto(ik)^2=-k^2$, so the PDE becomes an *ordinary* differential equation in $t$ for each fixed $k$: $\partial_t\hat u=-Dk^2\hat u$.
2. Solve it: $\hat u(k,t)=\hat u_0(k)\,e^{-Dk^2 t}$. Each frequency simply decays, and high frequencies (large $k$) decay fastest — sharp features smooth out first, exactly what diffusion does.
3. Invert. The factor $e^{-Dk^2t}$ is the transform of a Gaussian (from [s6](#s6), with width $\propto\sqrt{Dt}$), so by the convolution theorem the solution is $u_0$ convolved with that Gaussian:
$$
u(x,t)=\int_{-\infty}^\infty \frac{1}{\sqrt{4\pi D t}}\,e^{-(x-y)^2/(4Dt)}\,u_0(y)\,dy.
$$
The kernel is the **heat kernel** — the Green's function of diffusion — a Gaussian that spreads with width $\sqrt{2Dt}$. A hard PDE became a one-line ODE per frequency; this transform-the-space-variable technique is the standard attack on linear PDEs on infinite or periodic domains.

## Part C — Transforms in differential equations

<a id="s9"></a>
### The Laplace transform and initial-value problems

**What & why.** The Fourier transform needs the function to decay at $\pm\infty$. Many engineering signals start at $t=0$ and may *grow*. The **Laplace transform** handles these by inserting a decaying factor $e^{-st}$ and integrating only over $t\ge0$, building the initial conditions in automatically.

**Definition.** For $t\ge0$,
$$
F(s)=\mathcal L\{f\}(s)=\int_0^\infty f(t)\,e^{-st}\,dt,\qquad s=\sigma+i\omega\in\mathbb C,
$$
convergent where $\mathrm{Re}(s)=\sigma$ is large enough to beat any growth of $f$ (the *region of convergence*).

**Relation to the Fourier transform.** Set the real part $\sigma$ to a fixed value and let $s=\sigma+i\omega$: then $F(\sigma+i\omega)=\int_0^\infty [f(t)e^{-\sigma t}]e^{-i\omega t}dt$, which is exactly the Fourier transform of the damped, one-sided function $f(t)e^{-\sigma t}\theta(t)$. So Laplace = Fourier of a function multiplied by a real exponential and restricted to $t>0$. The two are the same idea on different contours in the complex plane; the inverse Laplace transform is a contour integral (the Bromwich integral) running vertically at $\mathrm{Re}(s)=\sigma$.

**Why a one-sided transform with a damping factor.** Two design choices distinguish Laplace from Fourier, and each earns its keep. First, integrating only over $t\ge0$ matches the physical setup of "switch the system on at $t=0$ with known state" — the past is irrelevant. Second, the factor $e^{-\sigma t}$ (the real part of $e^{-st}$) is an exponential *guillotine*: even if $f$ grows like $e^{ct}$, choosing $\sigma>c$ makes $f(t)e^{-\sigma t}$ decay, so the integral converges. The set of $s$ with $\mathrm{Re}\,s>c$ is the **region of convergence**; the transform is analytic there, and the threshold $c$ (the **abscissa of convergence**) encodes the fastest growth rate of $f$. Fourier, lacking this factor, simply fails for growing or non-decaying signals — which is exactly the gap Laplace fills.

**The integration rule.** Alongside the derivative rule, $\mathcal L\{\int_0^t f(\tau)d\tau\}=\frac{1}{s}F(s)$: integrating in time divides by $s$, the mirror of differentiating multiplying by $s$. (Proof: let $g(t)=\int_0^t f$, so $g'=f$ and $g(0)=0$; the derivative rule gives $F(s)=sG(s)-0$, hence $G=F/s$.) Together, $d/dt\leftrightarrow\times s$ and $\int dt\leftrightarrow\div s$ turn the calculus of an initial-value problem into the algebra of rational functions of $s$.

**The derivative rule with initial data.** This is the property that solves ODEs.
$$
\mathcal L\{f'\}(s)=sF(s)-f(0).
$$
*Proof.* Integrate by parts: $\int_0^\infty f'(t)e^{-st}dt=[f(t)e^{-st}]_0^\infty+s\int_0^\infty f(t)e^{-st}dt$. The boundary term is $0-f(0)=-f(0)$ (top vanishes for $\sigma$ in the region of convergence). The integral is $sF(s)$. Sum: $sF(s)-f(0)$. $\blacksquare$ Iterating, $\mathcal L\{f''\}=s^2F(s)-sf(0)-f'(0)$. The initial conditions appear as constants — exactly what an initial-value problem needs.

**Worked initial-value problem.** Solve $y''+y=0$ with $y(0)=0$, $y'(0)=1$.
1. Transform both sides: $\mathcal L\{y''\}+\mathcal L\{y\}=0$, i.e. $\big(s^2Y-s\cdot0-1\big)+Y=0$.
2. Solve the *algebraic* equation: $(s^2+1)Y=1$, so $Y(s)=\dfrac{1}{s^2+1}$.
3. Invert using the known pair $\mathcal L\{\sin t\}=\frac{1}{s^2+1}$ (derive: $\int_0^\infty\sin t\,e^{-st}dt=\frac{1}{s^2+1}$ by two integrations by parts). Hence $y(t)=\sin t$.
4. Check: $y(0)=0$, $y'(0)=\cos0=1$, $y''+y=-\sin t+\sin t=0$. Correct. The differential equation became algebra, was solved by inspection, and inverted from a table — the entire Laplace method in four lines.

**Building the table.** A few transforms power most calculations; we derive them so the table is self-contained.
1. $\mathcal L\{1\}=\int_0^\infty e^{-st}dt=\big[-\tfrac1s e^{-st}\big]_0^\infty=\tfrac1s$ (for $\mathrm{Re}\,s>0$).
2. $\mathcal L\{e^{at}\}=\int_0^\infty e^{(a-s)t}dt=\tfrac{1}{s-a}$ (for $\mathrm{Re}\,s>\mathrm{Re}\,a$); the $\mathcal L\{1\}$ result is the case $a=0$.
3. $\mathcal L\{t^n\}=\tfrac{n!}{s^{n+1}}$, by repeated integration by parts (or differentiating $\tfrac1{s-a}$ in $a$).
4. $\mathcal L\{\cos\omega t\}$ and $\mathcal L\{\sin\omega t\}$: write $\cos\omega t=\tfrac12(e^{i\omega t}+e^{-i\omega t})$ and use rule 2 with $a=\pm i\omega$:
$$
\mathcal L\{\cos\omega t\}=\tfrac12\Big(\tfrac1{s-i\omega}+\tfrac1{s+i\omega}\Big)=\frac{s}{s^2+\omega^2},\qquad
\mathcal L\{\sin\omega t\}=\frac{\omega}{s^2+\omega^2}.
$$
5. **Shift in $s$:** $\mathcal L\{e^{at}f(t)\}=F(s-a)$ — multiplying by $e^{at}$ shifts the transform variable. (Proof: $\int_0^\infty e^{at}f(t)e^{-st}dt=\int_0^\infty f(t)e^{-(s-a)t}dt=F(s-a)$.) This instantly gives damped oscillations: $\mathcal L\{e^{-\gamma t}\sin\omega t\}=\frac{\omega}{(s+\gamma)^2+\omega^2}$.

**A damped, driven worked problem.** Solve $y''+3y'+2y=0$ with $y(0)=1$, $y'(0)=0$ (overdamped relaxation).
1. Transform: $(s^2Y-s\cdot1-0)+3(sY-1)+2Y=0$, so $(s^2+3s+2)Y=s+3$.
2. Factor: $s^2+3s+2=(s+1)(s+2)$, giving $Y=\dfrac{s+3}{(s+1)(s+2)}$.
3. Partial fractions: $\dfrac{s+3}{(s+1)(s+2)}=\dfrac{2}{s+1}-\dfrac{1}{s+2}$ (solve $A(s+2)+B(s+1)=s+3$ at $s=-1,-2$ to get $A=2$, $B=-1$).
4. Invert each term with rule 2: $y(t)=2e^{-t}-e^{-2t}$.
5. Check: $y(0)=2-1=1$; $y'(t)=-2e^{-t}+2e^{-2t}$ so $y'(0)=0$. Both initial conditions met, and the solution decays monotonically — the expected overdamped behaviour. Notice how partial fractions plays the role that residues played for the Fourier inversion: it splits the rational transform into table entries.

<a id="s10"></a>
### Green's functions via transforms: the damped oscillator

**What & why.** A **Green's function** $G$ is the response of a linear system to a unit impulse $\delta$ — its impulse response. Once you know it, the response to *any* driving force is a convolution (as in [s8](#s8)): the impulse can be "summed up" to build any force. Transforms compute $G$ almost mechanically.

**The problem.** The driven, damped harmonic oscillator obeys
$$
\ddot x(t)+2\gamma\dot x(t)+\omega_0^2 x(t)=f(t),
$$
where $\gamma>0$ is the damping rate, $\omega_0$ the natural frequency, $f$ the driving force per unit mass. The Green's function solves it with $f(t)=\delta(t)$:
$$
\ddot G+2\gamma\dot G+\omega_0^2 G=\delta(t).
$$

**Derivation by Fourier transform.**
1. Transform in time, $G(t)\mapsto \hat G(\omega)$, using the derivative rule $\mathcal F\{\dot G\}=i\omega\hat G$, $\mathcal F\{\ddot G\}=(i\omega)^2\hat G=-\omega^2\hat G$ (from [s5](#s5)), and $\mathcal F\{\delta\}=1$ (from [s7](#s7)):
$$
(-\omega^2+2i\gamma\omega+\omega_0^2)\,\hat G(\omega)=1.
$$
2. Solve algebraically:
$$
\hat G(\omega)=\frac{1}{\omega_0^2-\omega^2+2i\gamma\omega}.
$$
This is the **frequency response**: its magnitude peaks near $\omega\approx\omega_0$ (resonance), with peak sharpness set by $\gamma$ — the Lorentzian lineshape met in [s6](#s6).
3. Invert: $G(t)=\frac{1}{2\pi}\int_{-\infty}^\infty\frac{e^{i\omega t}}{\omega_0^2-\omega^2+2i\gamma\omega}\,d\omega$. Factor the denominator. The roots of $\omega^2-2i\gamma\omega-\omega_0^2=0$ are $\omega=i\gamma\pm\omega_d$ where $\omega_d=\sqrt{\omega_0^2-\gamma^2}$ (assume underdamping $\omega_0>\gamma$). Both poles sit in the *upper* half-plane (positive imaginary part $\gamma$).
4. Evaluate by contour integration / residues (the one complex-analysis tool used here): for $t>0$, $e^{i\omega t}$ decays as $\mathrm{Im}\,\omega\to+\infty$, so close the contour in the upper half-plane, enclosing both poles. For $t<0$ close below, enclosing nothing, giving $G(t)=0$ — the response cannot precede the impulse (**causality**), a direct consequence of both poles lying above the real axis.
5. The residues at $\omega=i\gamma\pm\omega_d$ sum to give, for $t>0$,
$$
G(t)=\frac{1}{\omega_d}\,e^{-\gamma t}\sin(\omega_d t),\qquad G(t)=0\text{ for }t<0.
$$
6. Check: $G(0)=0$ and $\dot G(0^+)=1$ (a unit impulse imparts a unit kick to the velocity), the oscillation rings at the *damped* frequency $\omega_d$, and the envelope $e^{-\gamma t}$ decays at the damping rate — exactly the physics of a struck, damped bell.

**Using it.** For an arbitrary force, $x(t)=(G*f)(t)=\int_{-\infty}^t \frac{e^{-\gamma(t-\tau)}}{\omega_d}\sin\!\big(\omega_d(t-\tau)\big)f(\tau)\,d\tau$ — the upper limit $t$ enforced by causality ($G=0$ for negative argument). The system "remembers" past kicks with an exponentially fading, oscillating memory.

**Resonance read off the frequency response.** Drive the oscillator with a steady tone $f(t)=\cos\omega t$. By linearity the steady-state response is the input scaled by the frequency response $\hat G(\omega)$ at that one frequency: amplitude $|\hat G(\omega)|$ and phase $\arg\hat G(\omega)$. From step 2,
$$
|\hat G(\omega)|=\frac{1}{\sqrt{(\omega_0^2-\omega^2)^2+4\gamma^2\omega^2}}.
$$
1. This is largest when the radicand is smallest. Differentiating the radicand and setting it to zero gives the resonance peak at $\omega_{\text{res}}=\sqrt{\omega_0^2-2\gamma^2}$ — slightly below the natural frequency, shifted down by damping.
2. At the peak the amplitude scales like $1/\gamma$: light damping gives a tall, sharp resonance; heavy damping a low, broad one. The peak width (the band where the response is within $1/\sqrt2$ of maximum) is $\sim\gamma$, so the dimensionless **quality factor** $Q\approx\omega_0/(2\gamma)$ measures sharpness.
3. The phase $\arg\hat G$ passes through $-\pi/2$ at $\omega=\omega_0$: at resonance the response lags the drive by a quarter cycle, the universal signature of a driven oscillator at resonance — from a pushed swing to an LC circuit to an absorption line.

This is the whole point of the Green's function: one calculation ($\hat G$) simultaneously delivers the impulse response in time, the resonance curve in frequency, and the steady-state response to any tone.

## Part D — Discrete and synthesis

<a id="s11"></a>
### Sampling and the discrete Fourier transform

**What & why.** Computers cannot store a continuous function; they store **samples** $f[n]=f(nT)$ taken every $T$ seconds (sampling rate $1/T$). Two questions arise: when do samples capture the signal faithfully, and how do we Fourier-analyze a finite list of numbers?

**The sampling idea (Nyquist).** Sampling at spacing $T$ in time multiplies the signal by a "comb" of deltas; by the convolution/multiplication duality this *periodizes* the spectrum, making copies of $\hat f$ spaced by $2\pi/T$ in frequency. If $\hat f$ is band-limited (zero above a maximum frequency $\omega_{\max}$) and the copies do not overlap — which requires the sampling rate to exceed twice the highest frequency, $1/T>2\,(\omega_{\max}/2\pi)$ — then the original spectrum can be cut out cleanly and the continuous signal reconstructed exactly. This is the **Nyquist–Shannon sampling theorem**. Sample too slowly and the copies overlap: high frequencies masquerade as low ones (**aliasing**), the reason wagon wheels spin backwards on film and why audio is low-pass filtered before digitizing.

**The discrete Fourier transform (DFT).** For a finite sequence $x_0,\dots,x_{N-1}$ define
$$
X_k=\sum_{n=0}^{N-1}x_n\,e^{-2\pi i kn/N},\qquad k=0,\dots,N-1,
$$
with inverse $x_n=\frac1N\sum_{k=0}^{N-1}X_k e^{2\pi i kn/N}$. This is the exact discrete analogue of the series/transform: the continuous integral becomes a finite sum over the $N$ sampled points, and the frequencies $e^{2\pi i kn/N}$ are the $N$ complex $N$-th roots of unity. The discrete orthogonality $\sum_{n=0}^{N-1}e^{2\pi i(k-k')n/N}=N\delta_{kk'}$ (a finite geometric series, summing to $N$ when $k=k'$ and to $0$ otherwise since $e^{2\pi i(k-k')}=1$) proves the inversion formula by the same multiply-and-sum trick used for series in [s1](#s1).

**A tiny DFT by hand.** Take $N=4$ and the sequence $x=(1,0,1,0)$ — a signal alternating period-2. With $W=e^{-2\pi i/4}=e^{-i\pi/2}=-i$,
$$
X_k=\sum_{n=0}^{3}x_n W^{kn}=x_0+x_2 W^{2k}=1+(-i)^{2k}=1+(-1)^k.
$$
So $X_0=2$, $X_1=0$, $X_2=2$, $X_3=0$. The energy sits entirely in the $k=0$ (constant) and $k=2$ (the highest, Nyquist, frequency) bins — exactly right, since $(1,0,1,0)$ is the average $\tfrac12$ plus a $\tfrac12$-amplitude wave oscillating at the fastest representable rate. The inverse formula reconstructs $x_n=\tfrac14(2+2(-1)^n)=\tfrac12(1+(-1)^n)$, which is $1$ for even $n$ and $0$ for odd $n$ — the original sequence. A clean round trip.

**Aliasing, concretely.** With $N$ samples the only distinguishable frequencies are $k=0,1,\dots,N-1$, and frequency $k$ is *indistinguishable* from $k+N$: $W^{(k+N)n}=W^{kn}W^{Nn}=W^{kn}$ since $W^N=1$. A wave faster than the sampling grid can resolve therefore impersonates a slower one. This is aliasing made precise — and the reason the sampling theorem demands a band limit below half the sample rate before digitizing.

**The FFT, briefly.** Computed naively the DFT costs $N^2$ operations (each of $N$ outputs is a sum of $N$ terms). The **Fast Fourier Transform** factors the sum recursively: split the input into even- and odd-indexed halves, transform each half (size $N/2$), and combine with twiddle factors $W^k$. The recursion $T(N)=2T(N/2)+O(N)$ solves to $T(N)=O(N\log N)$ — the algorithm that made digital signal processing, MP3s, JPEGs, and numerical PDE solvers practical. It is not a different transform, only a fast way to evaluate the same one.

<a id="s12"></a>
### Synthesis: the unifying picture

**What & why.** Step back and the whole subject is one idea wearing different clothes. In every case we expand a function in a basis of pure waves that *diagonalizes* the relevant operator, turn calculus into algebra, solve, and transform back.

**The single template.**
- **Periodic, continuous** $\to$ Fourier *series*: discrete frequencies $n\pi/L$, coefficients $c_n$.
- **Non-periodic, continuous** $\to$ Fourier *transform*: continuous frequencies $k$, spectrum $\hat f(k)$. (Recovered from the series by $L\to\infty$.)
- **One-sided / growing** $\to$ *Laplace* transform: complex frequency $s$, building in initial data.
- **Sampled / finite** $\to$ *DFT/FFT*: $N$ roots of unity, computed fast.

All four obey the same grammar: linearity, a shift $\leftrightarrow$ phase rule, a derivative $\leftrightarrow$ multiplication rule, and a convolution $\leftrightarrow$ product rule. Learn the rules once; the four transforms are dialects.

**The deep threads.**
1. *Diagonalization.* Waves $e^{ikx}$ are eigenfunctions of $d/dx$ (eigenvalue $ik$) and of every shift-invariant operator. Transforming to $k$-space is choosing the basis where these operators become multiplication — the same move as diagonalizing a matrix in linear algebra.
2. *Conjugate variables.* Position $\leftrightarrow$ wavenumber, time $\leftrightarrow$ frequency, $x\leftrightarrow p/\hbar$. The scaling rule ([s5](#s5)) makes the uncertainty trade-off a theorem: narrow in one domain forces broad in the other, the Gaussian ([s6](#s6)) being the optimal compromise.
3. *Energy is preserved.* Parseval/Plancherel ([s3](#s3)) say the transform is a rotation of an infinite-dimensional space — it relabels, never creates or destroys.
4. *Impulse $\to$ response $\to$ everything.* The delta ([s7](#s7)) and the Green's function ([s10](#s10)) say: know the response to a single spike and convolution ([s8](#s8)) gives the response to anything.

**One worked thread tying the guide together.** Trace a single signal through the whole machine. Take a struck, damped oscillator. (i) Its impulse response is the Green's function $G(t)=\frac{1}{\omega_d}e^{-\gamma t}\sin\omega_d t$ ([s10](#s10)), found by *transforming* the differential equation into algebra via the derivative rule ([s5](#s5)) and $\mathcal F\{\delta\}=1$ ([s7](#s7)). (ii) Its response to any force is the *convolution* $G*f$ ([s8](#s8)), because the system is linear and shift-invariant. (iii) Its response to a pure tone is read straight off $|\hat G(\omega)|$, giving the Lorentzian resonance curve ([s6](#s6), [s10](#s10)). (iv) The energy it dissipates is accounted for by *Parseval/Plancherel* ([s3](#s3)). (v) If we sample its ringing for a computer, the *DFT/FFT* ([s11](#s11)) recovers the spectrum, with the sampling theorem telling us how fast to sample. Five sections, one physical object — each tool a different face of the same decomposition into waves.

**A checklist you can carry away.** Faced with a new problem in waves, signals, or linear differential equations, ask in order: *Is it periodic?* (series) *Does it decay?* (Fourier transform) *Is it one-sided or growing, with initial data?* (Laplace) *Is it sampled?* (DFT/FFT). Then apply the universal grammar — linearity, shift $\leftrightarrow$ phase, derivative $\leftrightarrow$ multiply, convolution $\leftrightarrow$ multiply — to move the hard operation into the easy domain, solve there, and transform back. Watch the conjugate-variable trade-off (narrow $\leftrightarrow$ broad) and trust the symmetry checks (real $\leftrightarrow$ Hermitian, even $\leftrightarrow$ real, smooth $\leftrightarrow$ fast-decaying spectrum) to catch errors.

From a plucked string to a quantum wavefunction to the JPEG on your screen, the same decomposition into waves is at work. That is the unity of Fourier analysis: the world, taken apart into frequencies, becomes simple — and then it can be put back together.

*This guide developed Fourier analysis from periodic series through the transform, the delta, convolution, and the Laplace and Green's-function machinery, proving the load-bearing results along the way. The natural next steps are the spectral theory of self-adjoint operators (where these ideas become the spectral theorem), the theory of distributions made fully rigorous, and the application of all of it to partial differential equations and quantum mechanics.*
