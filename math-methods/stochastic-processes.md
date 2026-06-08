**English** · [中文](stochastic-processes.zh.md)

# Stochastic Processes & Path Integrals, *the mathematics of randomness in motion.*

*A self-contained first course in the mathematics of randomness evolving in time — from the jittering of a pollen grain to Feynman's sum over all possible histories. We build stochastic processes from probability, walk through Markov chains and the Poisson process, construct Brownian motion and the Itô calculus that tames it, solve stochastic differential equations, and cross the bridge from random paths to the partial differential equations of diffusion and quantum mechanics via the Fokker–Planck, Feynman–Kac, and path-integral formulas. Every term is defined on first use, every formula is motivated, and every derivation is a numbered, gap-free chain of reasons. Built on basic algebra, single-variable calculus, and the companion Probability Theory guide.*

[← Back to all guides](../README.md)

## Part A · From probability to processes

<a id="s0"></a>
### Motivation: Brownian motion, noise, diffusion, and Feynman's sum over histories

#### What this guide is about, in one breath

Ordinary calculus describes things that move *predictably*: give me the forces and the starting point and I will tell you exactly where the object is at every later instant. But much of nature is not predictable in that sense. A speck of dust in still air trembles and wanders; the price of a stock zig-zags; a radioactive sample clicks at random instants; heat spreads from hot to cold without anyone steering it. The mathematics that captures "a quantity that evolves while being buffeted by chance" is the theory of **stochastic processes** (from the Greek *stokhastikos*, "able to guess"). This guide builds that theory from the ground up and then reveals its deepest surprise: the very same mathematics of summing over all random paths, when rotated by a factor of $i$, becomes Feynman's formulation of quantum mechanics.

#### Four motivating pictures

- **Brownian motion.** In 1827 the botanist Robert Brown watched pollen grains suspended in water jiggle ceaselessly under his microscope. In 1905 Einstein explained it: the grain is kicked from all sides by water molecules, and the imbalance of kicks at each instant nudges it on a random walk. The mathematical idealization of that jiggle — a continuous path that is random at every scale — is called **Brownian motion** or the **Wiener process**, and it is the central object of this guide (§s4).

- **Noise.** Any signal — a voltage on a wire, a measurement from an instrument — carries an unwanted random component called **noise**. Modeling noise means modeling a random function of time, which is exactly a stochastic process.

- **Diffusion.** Drop ink into water and it spreads. The concentration obeys a deterministic partial differential equation (the **diffusion** or **heat equation**), yet each individual ink molecule performs an erratic random walk. One of the triumphs of this subject is to show that these two descriptions — a smooth equation for the *crowd* and a random path for the *individual* — are two faces of one coin (§s8).

- **Feynman's sum over histories.** A classical particle takes one path from $A$ to $B$. Richard Feynman's 1948 reformulation of quantum mechanics says a quantum particle takes *all* paths at once, each contributing a complex number $e^{iS/\hbar}$ where $S$ is the classical action, and the observed amplitude is the sum over every conceivable history. This **path integral** (§s11) looks formally identical to the average over Brownian paths (§s10) — the bridge between them is the theme of Part E.

#### The whole guide on one line

> processes → Markov chains → Poisson → Brownian motion → martingales → Itô calculus → SDEs → Fokker–Planck → Feynman–Kac → Wiener path integral → Feynman path integral → Euclidean partition function

#### The one prerequisite, restated

We rely on the companion **Probability Theory** guide. The single facts we lean on most, restated in one line each so this guide stands alone: a **random variable** $X$ is a number whose value is governed by chance; its **expectation** (mean) is $\mathbb{E}[X]$, the long-run average; its **variance** is $\mathrm{Var}(X)=\mathbb{E}[(X-\mathbb{E}[X])^2]$, the average squared spread; and a **normal (Gaussian)** random variable with mean $\mu$ and variance $\sigma^2$, written $X\sim\mathcal{N}(\mu,\sigma^2)$, has probability density
$$
p(x)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right).
$$
Two random variables are **independent** when knowing one tells you nothing about the other, so probabilities and expectations of products factor.

#### Common pitfalls

- "Random" does not mean "lawless." A stochastic process has perfectly definite *probabilistic* laws; what is uncertain is the particular outcome, not its statistics.
- The path of Brownian motion is continuous but, as we will prove in spirit (§s4), *nowhere differentiable*: it has no velocity at any instant. Intuition trained on smooth curves fails here, and the Itô calculus (§s6) exists precisely to replace it.

<a id="s1"></a>
### Stochastic processes: definition, finite-dimensional distributions, stationarity, sample paths

#### What & why

To do mathematics with "a random quantity changing in time" we must say exactly what object we are studying. The definition is short but each word carries weight, so we unpack all of them.

#### Every term, defined from zero

- An **index set** $T$ is the set of "times" at which we observe the quantity. If $T=\{0,1,2,\dots\}$ we have **discrete time** (snapshots); if $T=[0,\infty)$ we have **continuous time** (a movie).
- A **state space** $S$ is the set of values the quantity may take (e.g. the integers, or all real numbers $\mathbb{R}$).
- Underlying everything is a **probability space** $(\Omega,\mathcal{F},\mathbb{P})$: a set $\Omega$ of all possible *outcomes* $\omega$ (think "which random world we landed in"), a collection $\mathcal{F}$ of **events** (subsets of $\Omega$ to which we assign probability), and a **probability measure** $\mathbb{P}$ assigning each event a number in $[0,1]$ with $\mathbb{P}(\Omega)=1$.

> **Definition — stochastic process**
>
> A **stochastic process** is a collection of random variables $\{X_t\}_{t\in T}$ indexed by $T$, all defined on one probability space $(\Omega,\mathcal{F},\mathbb{P})$ and taking values in $S$. Equivalently it is a function of *two* arguments, $X:T\times\Omega\to S$, written $X_t(\omega)$.

The two-argument view explains two complementary readings:

- Fix the time $t$ and let the outcome $\omega$ vary: $X_t(\cdot)$ is an ordinary random variable — "where is the particle at time $t$, over all random worlds?"
- Fix the outcome $\omega$ and let time $t$ vary: $t\mapsto X_t(\omega)$ is a single function of time, called a **sample path** or **realization** — "one actual movie of the particle's journey."

#### Finite-dimensional distributions

We can never observe the whole continuum of times at once. What we *can* pin down is, for any finite list of times $t_1<t_2<\dots<t_n$, the joint probability law of the snapshot vector $(X_{t_1},\dots,X_{t_n})$. These joint laws, for every finite list, are the **finite-dimensional distributions** (fdds). The Kolmogorov extension theorem (which we take on trust from probability theory) says: *a consistent family of finite-dimensional distributions determines a stochastic process.* In words — to specify a process it is enough to say how every finite collection of snapshots is jointly distributed.

#### Stationarity

- A process is **(strictly) stationary** if shifting all times by the same amount leaves every fdd unchanged: for every shift $h$ and times $t_1,\dots,t_n$, the law of $(X_{t_1+h},\dots,X_{t_n+h})$ equals that of $(X_{t_1},\dots,X_{t_n})$. Intuition: the statistics "look the same whenever you start watching."
- A weaker, more usable notion is **wide-sense (or weak) stationarity**: the mean $\mathbb{E}[X_t]=\mu$ is constant in time, and the **autocovariance** $\mathrm{Cov}(X_s,X_t)=\mathbb{E}[(X_s-\mu)(X_t-\mu)]$ depends only on the lag $t-s$, not on $s$ and $t$ separately.

#### A first worked example — the simple random walk

Let $\xi_1,\xi_2,\dots$ be independent steps, each equal to $+1$ or $-1$ with probability $\tfrac12$. Define the **simple symmetric random walk** by $X_0=0$ and $X_n=\xi_1+\dots+\xi_n$. Here $T=\{0,1,2,\dots\}$ and $S=\mathbb{Z}$ (the integers). Its mean and variance:

1. $\mathbb{E}[\xi_k]=(+1)\cdot\tfrac12+(-1)\cdot\tfrac12=0$ by the definition of expectation, so $\mathbb{E}[X_n]=\sum_{k=1}^n\mathbb{E}[\xi_k]=0$ by linearity of expectation.
2. $\mathrm{Var}(\xi_k)=\mathbb{E}[\xi_k^2]-(\mathbb{E}[\xi_k])^2=1-0=1$, since $\xi_k^2=1$ always.
3. Because the $\xi_k$ are independent, variances add: $\mathrm{Var}(X_n)=\sum_{k=1}^n\mathrm{Var}(\xi_k)=n$.

So the walk drifts nowhere on average but spreads with standard deviation $\sqrt{n}$. That $\sqrt{n}$ growth is the seed of everything: rescaled correctly, this walk converges to Brownian motion (§s4).

#### Common pitfalls

- A process is *not* its average. $\mathbb{E}[X_t]$ may be constant while every sample path wanders wildly.
- Wide-sense stationarity is about the first two moments only; a process can be wide-sense stationary yet not strictly stationary.

<a id="s2"></a>
### Discrete-time Markov chains: transition matrices, Chapman–Kolmogorov, stationary distributions

#### What & why

Most processes have memory tangled across all past times, which is unmanageable. The **Markov property** is the great simplification: *the future depends on the past only through the present*. Knowing where you are now, the route you took to get here is irrelevant for predicting the next step. A huge fraction of applied stochastic modeling lives inside this assumption.

#### Definitions

- A **Markov chain** (discrete time, discrete state space) is a process $X_0,X_1,X_2,\dots$ with states in a finite or countable set $S$ such that for all times $n$ and states $i_0,\dots,i_{n+1}$,
$$
\mathbb{P}(X_{n+1}=j \mid X_n=i,\,X_{n-1}=i_{n-1},\dots,X_0=i_0)=\mathbb{P}(X_{n+1}=j\mid X_n=i).
$$
The left side is a **conditional probability** ("probability of $X_{n+1}=j$ given the listed history"); the equation says only the present $X_n=i$ matters.
- The chain is **time-homogeneous** if this probability does not depend on $n$. We then write the **transition probability** $P_{ij}=\mathbb{P}(X_{n+1}=j\mid X_n=i)$ and collect them into the **transition matrix** $P=(P_{ij})$. Each row is a probability distribution: $P_{ij}\ge 0$ and $\sum_j P_{ij}=1$ (a matrix with these two properties is called **stochastic**).

#### Multi-step transitions and the Chapman–Kolmogorov equation

Write $P^{(n)}_{ij}=\mathbb{P}(X_n=j\mid X_0=i)$ for the probability of going from $i$ to $j$ in exactly $n$ steps. The central computational fact:

> **Theorem — Chapman–Kolmogorov.** For all $m,n\ge 0$, $\;P^{(m+n)}_{ij}=\sum_{k\in S}P^{(m)}_{ik}\,P^{(n)}_{kj}$. In matrix form $P^{(m+n)}=P^{(m)}P^{(n)}$, hence $P^{(n)}=P^n$ (the $n$-th matrix power).

*Derivation, gap-free.*

1. Start from the **law of total probability**: to go from $i$ to $j$ in $m+n$ steps, the chain must be in *some* state $k$ after $m$ steps, and these intermediate states are mutually exclusive and exhaustive. Therefore
$$
\mathbb{P}(X_{m+n}=j\mid X_0=i)=\sum_{k\in S}\mathbb{P}(X_{m+n}=j,\,X_m=k\mid X_0=i).
$$
2. Factor each term with the definition of conditional probability $\mathbb{P}(A,B\mid C)=\mathbb{P}(A\mid B,C)\,\mathbb{P}(B\mid C)$:
$$
=\sum_{k}\mathbb{P}(X_{m+n}=j\mid X_m=k,\,X_0=i)\,\mathbb{P}(X_m=k\mid X_0=i).
$$
3. Apply the **Markov property**: given $X_m=k$, the earlier value $X_0=i$ is irrelevant, so $\mathbb{P}(X_{m+n}=j\mid X_m=k,X_0=i)=\mathbb{P}(X_{m+n}=j\mid X_m=k)=P^{(n)}_{kj}$ (using time-homogeneity to shift the start of the clock).
4. The remaining factor is $P^{(m)}_{ik}$ by definition. Substituting gives $P^{(m+n)}_{ij}=\sum_k P^{(m)}_{ik}P^{(n)}_{kj}$, which is exactly the $(i,j)$ entry of the matrix product $P^{(m)}P^{(n)}$. Setting $m=n=1$ and iterating yields $P^{(n)}=P^n$. $\blacksquare$

#### Stationary distributions

A row vector $\pi=(\pi_i)$ with $\pi_i\ge0$ and $\sum_i\pi_i=1$ is a **stationary distribution** if $\pi P=\pi$, i.e. $\sum_i\pi_i P_{ij}=\pi_j$ for all $j$. Meaning: if the chain's state is distributed according to $\pi$ now, it is *still* distributed according to $\pi$ after one step — an equilibrium of the dynamics. For an **irreducible** (every state reachable from every other) and **aperiodic** chain, the distribution $P^{(n)}_{ij}$ converges to a unique $\pi_j$ as $n\to\infty$, independent of the start $i$ (the **fundamental limit theorem for Markov chains**).

#### Worked example — a two-state weather chain

States $S=\{\text{Sunny},\text{Rainy}\}=\{1,2\}$. Say a sunny day is followed by sun with probability $0.8$, and a rainy day is followed by rain with probability $0.6$:
$$
P=\begin{pmatrix}0.8 & 0.2\\[2pt] 0.4 & 0.6\end{pmatrix}.
$$
Find the long-run fraction of sunny days. We solve $\pi P=\pi$ with $\pi=(\pi_1,\pi_2)$ and $\pi_1+\pi_2=1$.

1. First component of $\pi P=\pi$: $0.8\,\pi_1+0.4\,\pi_2=\pi_1$, i.e. $0.4\,\pi_2=0.2\,\pi_1$, so $\pi_1=2\pi_2$.
2. Substitute into the normalization $\pi_1+\pi_2=1$: $2\pi_2+\pi_2=1$, giving $\pi_2=\tfrac13$ and $\pi_1=\tfrac23$.
3. Check the second component: $0.2\,\pi_1+0.6\,\pi_2=0.2\cdot\tfrac23+0.6\cdot\tfrac13=\tfrac{0.4}{3}+\tfrac{0.6}{3}=\tfrac13=\pi_2$. Consistent.

So in the long run it is sunny $2/3$ of the time, regardless of today's weather. To see the convergence, $P^2=\begin{pmatrix}0.72&0.28\\0.56&0.44\end{pmatrix}$ and higher powers march each row toward $(\tfrac23,\tfrac13)=(0.667,0.333)$.

#### Common pitfalls

- A stationary distribution always solves $\pi P=\pi$, but the chain only *converges* to it under irreducibility and aperiodicity. A periodic chain (e.g. one that strictly alternates states) has a stationary $\pi$ yet $P^{(n)}$ never settles.
- $\pi P=\pi$ makes $\pi$ a **left** eigenvector of $P$ with eigenvalue $1$. Confusing left and right eigenvectors is a frequent error.

<a id="s3"></a>
### The Poisson process and continuous-time Markov chains

#### What & why

Many things happen at random *instants*: clicks of a Geiger counter, arrivals at a queue, photons hitting a detector. The **Poisson process** is the canonical model of "completely random points in time," and it is the simplest continuous-time Markov chain — the bridge from discrete steps to genuine continuous-time dynamics.

#### Building the Poisson process

We want a counting process $N_t$ = "number of events up to time $t$," starting at $N_0=0$, with three properties:

1. **Independent increments:** the counts over disjoint time intervals are independent random variables.
2. **Stationary increments:** the law of $N_{t+s}-N_s$ depends only on the length $t$, not on $s$.
3. **No simultaneity:** events arrive one at a time; the chance of two in an infinitesimal interval is negligible.

We make property 3 precise with a **rate** $\lambda>0$ (mean events per unit time): over a tiny interval of length $h$,
$$
\mathbb{P}(\text{one event in }h)=\lambda h+o(h),\qquad \mathbb{P}(\text{two or more in }h)=o(h),
$$
where $o(h)$ ("little-o of $h$") denotes any quantity that vanishes faster than $h$, i.e. $o(h)/h\to0$ as $h\to0$.

#### Deriving the Poisson distribution of $N_t$

Let $p_n(t)=\mathbb{P}(N_t=n)$. We derive a differential equation for it.

1. To have $N_{t+h}=n$, either there were $n$ events by time $t$ and none in $(t,t+h]$, or $n-1$ by time $t$ and exactly one in $(t,t+h]$ (two or more is $o(h)$). By independent and stationary increments,
$$
p_n(t+h)=p_n(t)\,(1-\lambda h)+p_{n-1}(t)\,\lambda h+o(h).
$$
2. Rearrange: $\dfrac{p_n(t+h)-p_n(t)}{h}=-\lambda p_n(t)+\lambda p_{n-1}(t)+\dfrac{o(h)}{h}$.
3. Let $h\to0$; the last term vanishes by the definition of $o(h)$, giving the system
$$
p_n'(t)=-\lambda p_n(t)+\lambda p_{n-1}(t),\qquad p_0'(t)=-\lambda p_0(t),
$$
with $p_n(0)=\mathbf 1\{n=0\}$ (initial certainty of zero events).
4. Solve $p_0'=-\lambda p_0$, $p_0(0)=1$: this is the standard exponential-decay ODE, $p_0(t)=e^{-\lambda t}$.
5. Claim $p_n(t)=\dfrac{(\lambda t)^n}{n!}e^{-\lambda t}$. Verify by induction. It holds for $n=0$. Assume it for $n-1$ and substitute into step 3:
$$
p_n'(t)+\lambda p_n(t)=\lambda\,\frac{(\lambda t)^{n-1}}{(n-1)!}e^{-\lambda t}.
$$
Multiply through by the integrating factor $e^{\lambda t}$: the left side becomes $\frac{d}{dt}\!\big(e^{\lambda t}p_n(t)\big)$ by the product rule, and the right side is $\lambda^n t^{n-1}/(n-1)!$. Integrate from $0$ to $t$ (with $p_n(0)=0$ for $n\ge1$): $e^{\lambda t}p_n(t)=\lambda^n t^n/n!$, so $p_n(t)=\frac{(\lambda t)^n}{n!}e^{-\lambda t}$. $\blacksquare$

So $N_t$ has a **Poisson distribution** with parameter $\lambda t$: $\mathbb{P}(N_t=n)=e^{-\lambda t}(\lambda t)^n/n!$, with $\mathbb{E}[N_t]=\lambda t$ and $\mathrm{Var}(N_t)=\lambda t$.

#### Interarrival times are exponential

The waiting time $\tau$ to the first event satisfies $\mathbb{P}(\tau>t)=\mathbb{P}(N_t=0)=e^{-\lambda t}$. Hence $\tau$ has the **exponential distribution** with density $\lambda e^{-\lambda t}$ and mean $1/\lambda$. By stationary independent increments, all interarrival times are independent exponentials — this is the **memoryless property**: $\mathbb{P}(\tau>s+t\mid\tau>s)=\mathbb{P}(\tau>t)$, the continuous-time echo of the Markov property.

#### Worked example

A call center receives calls at rate $\lambda=3$ per minute. The probability of exactly $2$ calls in a given minute is $p_2(1)=e^{-3}\,3^2/2!=e^{-3}\cdot4.5\approx0.0498\cdot4.5\approx0.224$. The expected wait for the first call is $1/\lambda=1/3$ minute $=20$ seconds.

#### Continuous-time Markov chains in general

A **continuous-time Markov chain** generalizes this: the process sits in a state for an exponentially distributed holding time, then jumps. Its dynamics are encoded in a **generator matrix** $Q=(q_{ij})$ with off-diagonal $q_{ij}\ge0$ (jump rate $i\to j$) and diagonal $q_{ii}=-\sum_{j\ne i}q_{ij}$ (so rows sum to $0$). The transition probabilities $P(t)=(\mathbb{P}(X_t=j\mid X_0=i))$ solve the **Kolmogorov forward equation** $P'(t)=P(t)Q$ with $P(0)=I$, whose solution is the **matrix exponential** $P(t)=e^{tQ}=\sum_{k\ge0}(tQ)^k/k!$. The Poisson process is the special case with states $0,1,2,\dots$ and $q_{i,i+1}=\lambda$.

#### Common pitfalls

- "Poisson process" (random points in time) and "Poisson distribution" (a probability law on counts) are related but distinct; the former *has* the latter as the law of its counts.
- The memoryless property is special to the exponential distribution — no other continuous waiting-time law has it.

## Part B · Brownian motion and stochastic calculus

<a id="s4"></a>
### Brownian motion / the Wiener process: defining properties, and why paths are continuous but nowhere differentiable

#### What & why

Brownian motion $W_t$ is the continuous-time, continuous-state limit of the random walk and the single most important stochastic process. Norbert Wiener proved in 1923 that it exists as a rigorous mathematical object, so it is also called the **Wiener process**.

#### Definition

> **Definition — standard Brownian motion.** A process $\{W_t\}_{t\ge0}$ is a **standard Brownian motion** if:
> 1. $W_0=0$.
> 2. **Independent increments:** for $0\le t_1<t_2<\dots<t_n$, the increments $W_{t_2}-W_{t_1},\dots,W_{t_n}-W_{t_{n-1}}$ are independent.
> 3. **Gaussian increments:** for $s<t$, $\;W_t-W_s\sim\mathcal{N}(0,\,t-s)$ — normal with mean $0$ and variance equal to the elapsed time $t-s$.
> 4. **Continuous paths:** with probability $1$, the map $t\mapsto W_t$ is continuous.

From this we read off the mean and **covariance**: $\mathbb{E}[W_t]=0$, and for $s\le t$,
$$
\mathrm{Cov}(W_s,W_t)=\mathbb{E}[W_s W_t]=\min(s,t).
$$
*Derivation.* Write $W_t=W_s+(W_t-W_s)$. Then $\mathbb{E}[W_sW_t]=\mathbb{E}[W_s^2]+\mathbb{E}[W_s(W_t-W_s)]$. The first term is $\mathrm{Var}(W_s)=s$. In the second, $W_s=W_s-W_0$ and $W_t-W_s$ are increments over disjoint intervals, hence independent (property 2), so the expectation of their product factors into $\mathbb{E}[W_s]\,\mathbb{E}[W_t-W_s]=0\cdot0=0$. Thus $\mathbb{E}[W_sW_t]=s=\min(s,t)$. $\blacksquare$

#### From random walk to Brownian motion (why variance $=$ time)

Take the simple random walk (§s1) but make steps small and frequent. In time $t$ take $n=t/\Delta t$ steps, each of size $\pm\sqrt{\Delta t}$. The position is $W^{(n)}_t=\sqrt{\Delta t}\,(\xi_1+\dots+\xi_n)$.

1. Mean $\mathbb{E}[W^{(n)}_t]=\sqrt{\Delta t}\cdot 0=0$.
2. Variance $\mathrm{Var}(W^{(n)}_t)=\Delta t\cdot\mathrm{Var}(\xi_1+\dots+\xi_n)=\Delta t\cdot n=\Delta t\cdot(t/\Delta t)=t$.
3. By the **central limit theorem** (a normalized sum of many independent identical steps becomes Gaussian), as $\Delta t\to0$ the distribution of $W^{(n)}_t$ tends to $\mathcal{N}(0,t)$.

The choice of step size $\sqrt{\Delta t}$ — not $\Delta t$ — is forced: it is the only scaling that gives a finite, nonzero variance in the limit. That single fact, "displacement scales like the square root of time," is the fingerprint of diffusion and the source of the rule $(dW)^2=dt$ (§s6).

#### Why the paths are continuous but nowhere differentiable

Continuity holds by property 4. The shocking part is non-differentiability. Heuristic but honest argument:

1. The derivative at $t$, if it existed, would be the limit of the difference quotient $\dfrac{W_{t+h}-W_t}{h}$.
2. The numerator $W_{t+h}-W_t\sim\mathcal{N}(0,h)$, so its typical size is its standard deviation $\sqrt{h}$.
3. Therefore the quotient has typical size $\sqrt{h}/h=1/\sqrt{h}$, which **blows up** to $\infty$ as $h\to0$. The difference quotient does not settle to a finite limit; it oscillates with ever-larger amplitude.
4. Made rigorous (Paley–Wiener–Zygmund, 1933), this shows that with probability $1$ the path is differentiable at *no* point.

Intuition: the walk reverses direction on every time scale, so it never has a well-defined instantaneous velocity. This is exactly why ordinary calculus cannot integrate against $dW$ — we need the Itô calculus (§s6).

#### Quadratic variation — the precise statement of $(dW)^2=dt$

Partition $[0,t]$ into $n$ equal pieces of length $\Delta t=t/n$. The **quadratic variation** is the limit of the sum of squared increments:
$$
\sum_{k=1}^{n}\big(W_{t_k}-W_{t_{k-1}}\big)^2 \xrightarrow[n\to\infty]{} t.
$$
*Why.* Each squared increment has mean $\mathbb{E}[(\Delta W)^2]=\mathrm{Var}(\Delta W)=\Delta t$, so the sum of $n$ of them has mean $n\Delta t=t$. Its variance shrinks like $1/n$ (the increments are independent and the variance of a sum of $n$ independent terms each of size $\sim(\Delta t)^2$ is $\sim n(\Delta t)^2=t^2/n\to0$). A random quantity whose mean is $t$ and whose variance vanishes must converge to the constant $t$. This is the rigorous content of the symbolic rule $(dW)^2=dt$: over any interval the *squared* fluctuations add up not to zero (as for a smooth curve) but to the elapsed time.

#### Common pitfalls

- $W_t$ is continuous everywhere yet differentiable nowhere — a genuinely counterintuitive combination that does not occur among "ordinary" functions.
- The ordinary first-order variation $\sum|W_{t_k}-W_{t_{k-1}}|$ is *infinite*; it is the *quadratic* variation that is finite. This is why Stieltjes-style integration against $dW$ fails and Itô's construction is needed.

<a id="s5"></a>
### Martingales, filtrations, and stopping times; the optional stopping theorem

#### What & why

A **martingale** is the mathematical model of a fair game: your expected future fortune, given everything you know now, equals your present fortune. This single idea underpins the Itô integral, no-arbitrage pricing in finance, and many elegant computations. To state it we first need to formalize "everything you know now."

#### Filtrations and conditional expectation

- A **filtration** $\{\mathcal{F}_t\}_{t\ge0}$ is an increasing family of event-collections, $\mathcal{F}_s\subseteq\mathcal{F}_t$ for $s\le t$. Read $\mathcal{F}_t$ as "all information observable up to time $t$." Increasing means information is never forgotten.
- A process $X_t$ is **adapted** to $\{\mathcal{F}_t\}$ if $X_t$ is known once $\mathcal{F}_t$ is known (its value depends only on information up to $t$).
- The **conditional expectation** $\mathbb{E}[X\mid\mathcal{F}_t]$ is the best forecast of $X$ given the information $\mathcal{F}_t$; it is itself a random variable. Two properties we use: the **tower property** $\mathbb{E}[\mathbb{E}[X\mid\mathcal{F}_t]\mid\mathcal{F}_s]=\mathbb{E}[X\mid\mathcal{F}_s]$ for $s\le t$ (forecasting your forecast just gives the earlier forecast), and **taking out what is known**, $\mathbb{E}[YX\mid\mathcal{F}_t]=Y\,\mathbb{E}[X\mid\mathcal{F}_t]$ when $Y$ is $\mathcal{F}_t$-measurable (known by time $t$).

#### Martingales

> **Definition — martingale.** An adapted process $\{M_t\}$ with $\mathbb{E}|M_t|<\infty$ is a **martingale** with respect to $\{\mathcal{F}_t\}$ if for all $s\le t$,
> $$
> \mathbb{E}[M_t\mid\mathcal{F}_s]=M_s.
> $$
> If "$=$" is replaced by "$\ge$" it is a **submartingale** (favorable game); by "$\le$", a **supermartingale** (unfavorable).

*Example: Brownian motion is a martingale.* For $s\le t$, $\mathbb{E}[W_t\mid\mathcal{F}_s]=\mathbb{E}[W_s+(W_t-W_s)\mid\mathcal{F}_s]=W_s+\mathbb{E}[W_t-W_s\mid\mathcal{F}_s]$. The increment $W_t-W_s$ is independent of $\mathcal{F}_s$ (the past), so its conditional expectation equals its plain expectation $0$. Hence $\mathbb{E}[W_t\mid\mathcal{F}_s]=W_s$. Similarly $W_t^2-t$ is a martingale (this is the martingale form of $(dW)^2=dt$).

#### Stopping times

A **stopping time** $\tau$ is a random time such that the event $\{\tau\le t\}$ is decidable from $\mathcal{F}_t$ — you can tell whether you have stopped using only information available by time $t$, with no peeking into the future. "Stop the first time the walk hits $+5$" is a stopping time; "stop one step before the maximum" is not.

#### The optional stopping theorem

> **Theorem — optional stopping.** If $\{M_t\}$ is a martingale and $\tau$ a stopping time that is bounded (or satisfies suitable integrability/finiteness conditions), then $\mathbb{E}[M_\tau]=\mathbb{E}[M_0]$.

In words: *you cannot beat a fair game by any non-anticipating stopping strategy* — your expected fortune at the moment you choose to quit equals your starting fortune.

#### Worked gambling example — gambler's ruin

A gambler starts with $\$a$ and bets $\$1$ on fair coin flips, quitting when broke ($0$) or reaching a target $\$N$ (so $0<a<N$). What is the probability $q$ of reaching $N$ before $0$?

1. Model the fortune as the random walk $X_n=a+\xi_1+\dots+\xi_n$ (steps $\pm1$, fair). Then $X_n$ is a martingale: $\mathbb{E}[X_{n+1}\mid\mathcal{F}_n]=X_n+\mathbb{E}[\xi_{n+1}]=X_n+0=X_n$.
2. Let $\tau$ be the first time the fortune hits $0$ or $N$ — a stopping time. One shows $\tau$ is finite with probability $1$ and the conditions for optional stopping hold.
3. Apply optional stopping: $\mathbb{E}[X_\tau]=\mathbb{E}[X_0]=a$.
4. At time $\tau$ the fortune is either $0$ (probability $1-q$) or $N$ (probability $q$). So $\mathbb{E}[X_\tau]=0\cdot(1-q)+N\cdot q=Nq$.
5. Equate: $Nq=a$, hence $q=a/N$.

Concretely, starting with $\$30$ aiming for $\$100$, you reach the target before ruin with probability $30/100=0.3$. Notice how a one-line equation, $\mathbb{E}[M_\tau]=\mathbb{E}[M_0]$, dissolved a problem that would otherwise need a difference equation.

#### Common pitfalls

- Optional stopping can *fail* without an integrability/boundedness condition. The classic counterexample: in a fair game, "bet until you are $\$1$ ahead, then quit." This stopping time is finite with probability $1$ and yields $\$1$ surely — seemingly beating a fair game — but it is not bounded and requires unbounded capital, so the theorem does not apply.
- A stopping rule may not look into the future. This non-anticipation is the whole content of the definition.

<a id="s6"></a>
### The Itô integral and Itô's lemma

#### What & why

We want to give meaning to integrals like $\int_0^t f(s)\,dW_s$ and to differentiate functions of Brownian motion. Because $W$ has infinite ordinary variation (§s4), the classical Riemann–Stieltjes integral does not exist. Itô's insight: define the integral as a *limit in mean square* using **left-endpoint** sample points, which keeps the integral a martingale and makes everything computable through the single new rule $(dW)^2=dt$.

#### Constructing the Itô integral

For a process $f_t$ adapted to the filtration, partition $[0,t]$ as $0=t_0<\dots<t_n=t$ and form the **Itô sum** using the value of $f$ at the *left* endpoint of each subinterval:
$$
\int_0^t f_s\,dW_s := \lim_{n\to\infty}\sum_{k=0}^{n-1} f_{t_k}\,\big(W_{t_{k+1}}-W_{t_k}\big),
$$
the limit taken in **mean square** (i.e. the expected squared difference between the sum and the limit goes to $0$). The left-endpoint choice is essential: because $f_{t_k}$ is known at time $t_k$ and the increment $W_{t_{k+1}}-W_{t_k}$ lies entirely in the future, each term has conditional mean zero, so the integral is a **martingale**. (A right-endpoint or midpoint rule gives a different value — the Stratonovich integral — because the integrand and the increment would then be correlated.)

Two key properties follow:
- **Zero mean:** $\mathbb{E}\!\left[\int_0^t f_s\,dW_s\right]=0$.
- **Itô isometry:** $\;\mathbb{E}\!\left[\left(\int_0^t f_s\,dW_s\right)^2\right]=\int_0^t\mathbb{E}[f_s^2]\,ds$. *Why:* expand the square of the sum; cross terms $f_{t_j}f_{t_k}\Delta W_j\Delta W_k$ ($j\ne k$) vanish in expectation because the later increment is independent of everything earlier and has mean $0$; the diagonal terms give $\mathbb{E}[f_{t_k}^2]\,\mathbb{E}[(\Delta W_k)^2]=\mathbb{E}[f_{t_k}^2]\,\Delta t_k$, whose sum tends to the stated integral.

#### Itô's lemma — the chain rule of stochastic calculus

> **Theorem — Itô's lemma (one dimension).** Let $X_t$ satisfy $dX_t=a_t\,dt+b_t\,dW_t$ (shorthand for an Itô process with **drift** $a_t$ and **diffusion** $b_t$), and let $f(t,x)$ be twice continuously differentiable. Then
> $$
> df(t,X_t)=\left(\frac{\partial f}{\partial t}+a_t\frac{\partial f}{\partial x}+\tfrac12 b_t^2\frac{\partial^2 f}{\partial x^2}\right)dt+b_t\frac{\partial f}{\partial x}\,dW_t.
> $$

The extra term $\tfrac12 b_t^2\,\partial_{xx}f$, absent from ordinary calculus, is the entire novelty; it comes from $(dW)^2=dt$.

*Full derivation.*

1. Taylor-expand $f$ around $(t,X_t)$ to second order, since first order will turn out to be insufficient:
$$
df=\frac{\partial f}{\partial t}\,dt+\frac{\partial f}{\partial x}\,dX+\tfrac12\frac{\partial^2 f}{\partial x^2}\,(dX)^2+\tfrac12\frac{\partial^2 f}{\partial t^2}(dt)^2+\frac{\partial^2 f}{\partial t\,\partial x}\,dt\,dX+\cdots
$$
2. Substitute $dX=a\,dt+b\,dW$ and compute $(dX)^2=(a\,dt+b\,dW)^2=a^2(dt)^2+2ab\,dt\,dW+b^2(dW)^2$.
3. Now apply the **multiplication table** of Itô calculus, each entry justified by the orders established in §s4:
$$
(dW)^2=dt,\qquad dt\,dW=0,\qquad (dt)^2=0.
$$
- $(dW)^2=dt$ is the quadratic-variation result (§s4): squared Brownian increments accumulate at rate $1$ per unit time.
- $(dt)^2=0$ and $dt\,dW=0$ because $dt$ is of order the step size while these products are of higher order (e.g. $dt\,dW\sim\Delta t\cdot\sqrt{\Delta t}=(\Delta t)^{3/2}$), which vanish faster than $dt$ when summed and so contribute nothing in the mean-square limit.
4. Therefore $(dX)^2=b^2\,dt$, all other second-order terms vanish, and the $\partial_{tt}$ and mixed terms drop out. Collecting the surviving pieces:
$$
df=\frac{\partial f}{\partial t}\,dt+\frac{\partial f}{\partial x}(a\,dt+b\,dW)+\tfrac12\frac{\partial^2 f}{\partial x^2}\,b^2\,dt,
$$
which on grouping the $dt$ terms is exactly the stated formula. $\blacksquare$

#### Worked example — $f(W_t)=W_t^2$

Here $X_t=W_t$ so $a=0$, $b=1$, and $f(x)=x^2$ with $f_x=2x$, $f_{xx}=2$. Itô's lemma gives
$$
d(W_t^2)=\big(0+0+\tfrac12\cdot1\cdot2\big)dt+1\cdot2W_t\,dW_t=dt+2W_t\,dW_t.
$$
Integrate from $0$ to $t$: $\;W_t^2=t+2\int_0^t W_s\,dW_s$. Rearranged, $\int_0^t W_s\,dW_s=\tfrac12 W_t^2-\tfrac12 t$. The "$-\tfrac12 t$" is the Itô correction; naive calculus would have written $\int_0^t W\,dW=\tfrac12 W_t^2$, which is *wrong*. This single example shows the new calculus in action and confirms (taking expectations, $\mathbb{E}[W_t^2]=t$) that $\mathbb{E}[\int_0^t W\,dW]=0$, consistent with the martingale property.

#### Common pitfalls

- Always evaluate the integrand at the *left* endpoint. Forgetting this conflates Itô with Stratonovich and changes the answer.
- Never drop the $\tfrac12 b^2 f_{xx}$ term; it is the heart of stochastic calculus, not an optional refinement.

## Part C · Stochastic differential equations and their PDEs

<a id="s7"></a>
### Stochastic differential equations: geometric Brownian motion and the Ornstein–Uhlenbeck process

#### What & why

A **stochastic differential equation** (SDE) is the random analogue of an ordinary differential equation: it prescribes how a quantity changes per instant as a deterministic push plus a random kick. The general form is
$$
dX_t=\mu(t,X_t)\,dt+\sigma(t,X_t)\,dW_t,
$$
where $\mu$ is the **drift coefficient** (average rate of change) and $\sigma$ is the **diffusion coefficient** (size of the random kicks). This is shorthand for the integral equation $X_t=X_0+\int_0^t\mu\,ds+\int_0^t\sigma\,dW_s$, the last term being an Itô integral (§s6). We solve the two most important examples completely.

#### Geometric Brownian motion (the model of stock prices)

The SDE is $dX_t=\mu X_t\,dt+\sigma X_t\,dW_t$ with constants $\mu,\sigma$ and $X_0>0$: percentage changes, not absolute changes, are random, which keeps prices positive.

1. Guess that $\log X_t$ is simpler, motivated by the multiplicative structure. Apply Itô's lemma to $f(x)=\log x$, with $f_x=1/x$, $f_{xx}=-1/x^2$, and (from the SDE) $a=\mu X$, $b=\sigma X$:
$$
d(\log X_t)=\Big(\mu X\cdot\tfrac1X+\tfrac12(\sigma X)^2\cdot(-\tfrac1{X^2})\Big)dt+\sigma X\cdot\tfrac1X\,dW_t.
$$
2. Simplify each piece: the $dt$ coefficient is $\mu-\tfrac12\sigma^2$ (the cancellation of $X$ is the point of the substitution), and the $dW$ coefficient is $\sigma$. So
$$
d(\log X_t)=\big(\mu-\tfrac12\sigma^2\big)dt+\sigma\,dW_t.
$$
3. The right side has *constant* coefficients, so integrate directly from $0$ to $t$: $\log X_t-\log X_0=(\mu-\tfrac12\sigma^2)t+\sigma W_t$.
4. Exponentiate:
$$
X_t=X_0\exp\!\Big(\big(\mu-\tfrac12\sigma^2\big)t+\sigma W_t\Big).
$$

Because $\sigma W_t\sim\mathcal{N}(0,\sigma^2 t)$, $X_t$ is **log-normally** distributed. The drift seen by the *logarithm* is $\mu-\tfrac12\sigma^2$, not $\mu$ — the famous "volatility drag," a direct consequence of the Itô correction. Concretely, with $X_0=100$, $\mu=0.1$, $\sigma=0.2$, the median price after one year is $100\exp((0.1-0.02)\cdot1)=100e^{0.08}\approx108.3$.

#### The Ornstein–Uhlenbeck process (mean-reverting noise)

The SDE is $dX_t=-\theta X_t\,dt+\sigma\,dW_t$ with $\theta>0$: a restoring drift pulls $X$ back toward $0$ (a noisy spring; the velocity of a Brownian particle with friction).

1. The drift is *not* constant, so we use an **integrating factor**, exactly as for the linear ODE $x'=-\theta x$. Apply Itô's lemma to $Y_t=e^{\theta t}X_t$, i.e. $f(t,x)=e^{\theta t}x$, with $f_t=\theta e^{\theta t}x$, $f_x=e^{\theta t}$, $f_{xx}=0$, and $a=-\theta X$, $b=\sigma$:
$$
dY_t=\big(\theta e^{\theta t}X_t+e^{\theta t}(-\theta X_t)+0\big)dt+e^{\theta t}\sigma\,dW_t.
$$
2. The $dt$ terms cancel exactly (the design of the integrating factor), leaving $dY_t=\sigma e^{\theta t}\,dW_t$.
3. Integrate: $Y_t-Y_0=\sigma\int_0^t e^{\theta s}\,dW_s$, and since $Y_0=X_0$,
$$
X_t=e^{-\theta t}X_0+\sigma\int_0^t e^{-\theta(t-s)}\,dW_s.
$$
4. Read off the statistics. The mean is $\mathbb{E}[X_t]=e^{-\theta t}X_0$ (the Itô integral has mean $0$), decaying toward $0$. The variance, by the **Itô isometry** (§s6),
$$
\mathrm{Var}(X_t)=\sigma^2\int_0^t e^{-2\theta(t-s)}\,ds=\frac{\sigma^2}{2\theta}\big(1-e^{-2\theta t}\big)\xrightarrow[t\to\infty]{}\frac{\sigma^2}{2\theta}.
$$

So unlike Brownian motion (whose variance grows without bound), the OU process reaches a **stationary distribution** $\mathcal{N}(0,\sigma^2/2\theta)$: the restoring drift balances the diffusion. This is the prototype of equilibrium noise (and Einstein's relation linking diffusion, temperature, and friction).

#### Common pitfalls

- In geometric Brownian motion the long-run growth rate of the *typical* path is $\mu-\tfrac12\sigma^2$, which can be negative even when $\mu>0$ if volatility is large — a real effect, not an artifact.
- Apply Itô's lemma, never the ordinary chain rule, to functions of an SDE solution.

<a id="s8"></a>
### The Fokker–Planck (forward Kolmogorov) equation and its link to the diffusion PDE

#### What & why

An SDE tracks one random path. Often we want the *probability density* $p(x,t)$ of finding the particle at position $x$ at time $t$ — the description of the whole ensemble. The **Fokker–Planck equation** (also the **forward Kolmogorov equation**) is the deterministic PDE that this density obeys. It is the precise statement that "the crowd diffuses smoothly even though each individual jitters."

#### The equation

> **Theorem — Fokker–Planck.** If $dX_t=\mu(x)\,dt+\sigma(x)\,dW_t$, then the density $p(x,t)$ of $X_t$ satisfies
> $$
> \frac{\partial p}{\partial t}=-\frac{\partial}{\partial x}\big(\mu(x)\,p\big)+\frac12\frac{\partial^2}{\partial x^2}\big(\sigma(x)^2\,p\big).
> $$

*Derivation via a test function.* Let $\phi(x)$ be any smooth function vanishing at $\pm\infty$ (a **test function**). We compute $\frac{d}{dt}\mathbb{E}[\phi(X_t)]$ two ways.

1. By Itô's lemma applied to $\phi(X_t)$ (with no explicit $t$-dependence, $a=\mu$, $b=\sigma$):
$$
d\phi(X_t)=\big(\mu\,\phi'+\tfrac12\sigma^2\phi''\big)dt+\sigma\phi'\,dW_t.
$$
2. Take expectations. The $dW$ term has mean $0$ (Itô integrals are martingales, §s6), so
$$
\frac{d}{dt}\mathbb{E}[\phi(X_t)]=\mathbb{E}\big[\mu\,\phi'+\tfrac12\sigma^2\phi''\big]=\int\big(\mu(x)\phi'(x)+\tfrac12\sigma(x)^2\phi''(x)\big)p(x,t)\,dx,
$$
using the definition of expectation as an integral against the density $p$.
3. On the other hand, $\mathbb{E}[\phi(X_t)]=\int\phi(x)p(x,t)\,dx$, so $\frac{d}{dt}\mathbb{E}[\phi(X_t)]=\int\phi(x)\,\partial_t p\,dx$.
4. Equate the two expressions and move all derivatives off $\phi$ and onto $p$ by **integration by parts** (boundary terms vanish because $\phi$ and its derivatives die at $\pm\infty$): each $\int\mu\phi' p\,dx=-\int\phi\,\partial_x(\mu p)\,dx$, and $\int\tfrac12\sigma^2\phi'' p\,dx=+\int\tfrac12\phi\,\partial_{xx}(\sigma^2 p)\,dx$ (two integrations by parts).
5. The result is $\int\phi\big[\partial_t p+\partial_x(\mu p)-\tfrac12\partial_{xx}(\sigma^2 p)\big]dx=0$ for *every* test function $\phi$. A continuous quantity whose integral against every test function is zero must itself be zero (the **fundamental lemma of the calculus of variations**). Hence the bracket vanishes, which is the Fokker–Planck equation. $\blacksquare$

#### The link to the diffusion / heat equation

Take pure Brownian motion: $\mu=0$, $\sigma=1$, $X_0=0$. The Fokker–Planck equation collapses to
$$
\frac{\partial p}{\partial t}=\frac12\frac{\partial^2 p}{\partial x^2},
$$
which is exactly the **diffusion (heat) equation** with diffusion constant $D=\tfrac12$ (the Partial Differential Equations guide derives this PDE from conservation of probability and Fick's law). Its solution with a point-mass start is the **Gaussian / heat kernel**
$$
p(x,t)=\frac{1}{\sqrt{2\pi t}}\exp\!\Big(-\frac{x^2}{2t}\Big),
$$
which we verify is the density of $W_t\sim\mathcal{N}(0,t)$ — closing the loop: the random-path definition of Brownian motion (§s4) and the smooth diffusion PDE give the *same* spreading Gaussian. We can check it solves the PDE directly: with $p=\frac{1}{\sqrt{2\pi t}}e^{-x^2/2t}$, a computation of $\partial_t p$ and $\tfrac12\partial_{xx}p$ shows both equal $\frac{1}{\sqrt{2\pi t}}e^{-x^2/2t}\big(\frac{x^2}{2t^2}-\frac{1}{2t}\big)$, so the equation holds.

#### Common pitfalls

- The drift term is $-\partial_x(\mu p)$, *inside* the derivative — for state-dependent $\mu(x)$ you may not pull $\mu$ out. The same applies to $\sigma(x)^2$ inside the second derivative.
- The **backward** Kolmogorov equation (used in Feynman–Kac, §s9) acts on the starting point, not the endpoint, and is a different equation; do not confuse forward and backward.

<a id="s9"></a>
### The Feynman–Kac formula: the bridge between SDEs and PDEs

#### What & why

We have seen densities (forward equation). The Feynman–Kac formula goes the other way: it expresses the solution of a *deterministic* parabolic PDE as an *expectation* over random paths. This is the rigorous prototype of "solve a PDE by averaging over trajectories," and the direct ancestor of the Feynman path integral (§s11).

#### The statement

> **Theorem — Feynman–Kac.** Let $u(x,t)$ solve the backward PDE
> $$
> \frac{\partial u}{\partial t}+\mu(x)\frac{\partial u}{\partial x}+\tfrac12\sigma(x)^2\frac{\partial^2 u}{\partial x^2}-V(x)\,u=0,\qquad u(x,T)=g(x),
> $$
> on $t\le T$, where $V(x)\ge0$ is a "potential" and $g$ a terminal payoff. Then
> $$
> u(x,t)=\mathbb{E}\!\left[\exp\!\Big(-\int_t^T V(X_s)\,ds\Big)\,g(X_T)\;\Big|\;X_t=x\right],
> $$
> where $X_s$ solves $dX_s=\mu\,ds+\sigma\,dW_s$ started at $X_t=x$.

#### Derivation

We show the random-expectation expression solves the PDE.

1. Define the **discount factor** $D_s=\exp\!\big(-\int_t^s V(X_r)\,dr\big)$, so $D_t=1$ and, by the fundamental theorem of calculus, $dD_s=-V(X_s)D_s\,ds$ (this is an ordinary, not stochastic, differential since $D$ has no $dW$ term).
2. Consider the process $M_s=D_s\,u(X_s,s)$ for $t\le s\le T$. Apply the **product rule** (valid here because $D$ is smooth in $s$): $dM_s=u\,dD_s+D_s\,du$.
3. Compute $du=du(X_s,s)$ by **Itô's lemma** (§s6) with drift $\mu$, diffusion $\sigma$:
$$
du=\Big(\partial_s u+\mu\,\partial_x u+\tfrac12\sigma^2\partial_{xx}u\Big)ds+\sigma\,\partial_x u\,dW_s.
$$
4. Substitute steps 1 and 3 into step 2 and group the $ds$ terms:
$$
dM_s=D_s\Big(\underbrace{\partial_s u+\mu\,\partial_x u+\tfrac12\sigma^2\partial_{xx}u-V\,u}_{=\,0\text{ by the PDE}}\Big)ds+D_s\,\sigma\,\partial_x u\,dW_s.
$$
5. The $ds$ bracket is exactly the left-hand side of the backward PDE, which is zero. Hence $dM_s=D_s\sigma\partial_x u\,dW_s$ — a pure Itô integral, therefore a **martingale** (§s6), so $\mathbb{E}[M_s]$ is constant in $s$.
6. Equate the martingale's value at $s=t$ and $s=T$. At $s=t$: $M_t=D_t\,u(X_t,t)=1\cdot u(x,t)=u(x,t)$. At $s=T$: $M_T=D_T\,u(X_T,T)=\exp(-\int_t^T V\,dr)\,g(X_T)$ using the terminal condition $u(\cdot,T)=g$.
7. Therefore $u(x,t)=\mathbb{E}[M_t]=\mathbb{E}[M_T]=\mathbb{E}\big[\exp(-\int_t^T V\,ds)\,g(X_T)\mid X_t=x\big]$, the claimed formula. $\blacksquare$

#### Worked special case — heat equation with no potential

Set $\mu=0$, $\sigma=1$, $V=0$. The PDE is the backward heat equation $\partial_t u+\tfrac12\partial_{xx}u=0$ with $u(x,T)=g(x)$, and Feynman–Kac gives $u(x,t)=\mathbb{E}[g(X_T)\mid X_t=x]$ where $X_T-x\sim\mathcal{N}(0,T-t)$. Explicitly,
$$
u(x,t)=\int_{-\infty}^{\infty} g(y)\,\frac{1}{\sqrt{2\pi(T-t)}}\exp\!\Big(-\frac{(y-x)^2}{2(T-t)}\Big)\,dy,
$$
the solution of the heat equation by convolution with the Gaussian kernel — recovered here purely by averaging over Brownian endpoints. (In finance this same formula, with geometric Brownian motion and a discount, *is* the Black–Scholes option price.)

#### Common pitfalls

- The PDE here is **backward** (a terminal, not initial, condition) and the time derivative carries a $+$ sign; substituting $\tau=T-t$ turns it into a standard forward heat-type equation.
- $V\ge0$ acts as a "killing rate": paths are exponentially discounted at rate $V(X_s)$, as if the particle could be annihilated.

## Part D · Path integrals

<a id="s10"></a>
### The Wiener path integral: discretizing paths and the Gaussian measure

#### What & why

So far we averaged functions of the *endpoint* $X_T$. A path integral averages a functional of the *entire trajectory* $\{X_s\}$. The **Wiener integral** makes precise the idea "integrate over the space of all continuous paths, weighting each by how likely Brownian motion is to follow it." It is the probabilistic template that, analytically continued, becomes the Feynman integral (§s11).

#### Discretizing a Brownian path

Fix endpoints: paths from $x_0=0$ at time $0$ to $x_n=x$ at time $t$. Slice $[0,t]$ into $n$ steps of length $\epsilon=t/n$ at times $t_k=k\epsilon$, and approximate a path by its values $(x_1,\dots,x_{n-1})$ at the interior nodes.

1. By independent Gaussian increments (§s4), each increment $x_k-x_{k-1}\sim\mathcal{N}(0,\epsilon)$ with density $\frac{1}{\sqrt{2\pi\epsilon}}\exp(-\frac{(x_k-x_{k-1})^2}{2\epsilon})$.
2. By independence, the joint density of the increments is the product over $k=1,\dots,n$:
$$
\rho_n(x_1,\dots,x_{n-1})=\prod_{k=1}^{n}\frac{1}{\sqrt{2\pi\epsilon}}\exp\!\Big(-\frac{(x_k-x_{k-1})^2}{2\epsilon}\Big)
=\Big(\frac{1}{2\pi\epsilon}\Big)^{n/2}\exp\!\Big(-\frac{1}{2\epsilon}\sum_{k=1}^{n}(x_k-x_{k-1})^2\Big).
$$
3. Recognize the exponent. Writing $\frac{x_k-x_{k-1}}{\epsilon}$ as a discrete velocity $\dot x$, the sum becomes $\sum_k(x_k-x_{k-1})^2=\epsilon\sum_k\big(\tfrac{x_k-x_{k-1}}{\epsilon}\big)^2\epsilon\to\int_0^t\dot x(s)^2\,ds$ as $\epsilon\to0$. So formally
$$
\rho\,\propto\,\exp\!\Big(-\frac12\int_0^t\dot x(s)^2\,ds\Big).
$$

#### The Wiener measure and Wiener integral

The limit defines the **Wiener measure** $\mathcal{D}W$ on path space, and for a functional $F[x(\cdot)]$ the **Wiener integral** is the formal limit of finite-dimensional integrals:
$$
\mathbb{E}\big[F\big]=\int F[x(\cdot)]\;\mathcal{D}W
=\lim_{n\to\infty}\Big(\frac{1}{2\pi\epsilon}\Big)^{n/2}\!\int F\,\exp\!\Big(-\frac{1}{2\epsilon}\sum_{k=1}^{n}(x_k-x_{k-1})^2\Big)\,dx_1\cdots dx_{n-1}.
$$

Two remarks make this honest:
- The "weight" $\exp(-\tfrac12\int\dot x^2\,ds)$ is *not* a true probability density on path space (there is no infinite-dimensional Lebesgue measure, and $\dot x$ does not even exist, §s4). What is rigorous is the family of finite-dimensional Gaussian integrals together with the normalizing prefactors; the Wiener measure is their well-defined limit.
- **Consistency check (composition).** Integrating the discretized weight over a single interior node $x_k$ reproduces a single Gaussian over the longer interval, because the convolution of two Gaussians of variances $\epsilon$ is a Gaussian of variance $2\epsilon$:
$$
\int_{-\infty}^{\infty}\frac{e^{-(x_{k+1}-y)^2/2\epsilon}}{\sqrt{2\pi\epsilon}}\,\frac{e^{-(y-x_{k-1})^2/2\epsilon}}{\sqrt{2\pi\epsilon}}\,dy=\frac{1}{\sqrt{2\pi(2\epsilon)}}\exp\!\Big(-\frac{(x_{k+1}-x_{k-1})^2}{2(2\epsilon)}\Big).
$$
This is the **Chapman–Kolmogorov** relation (§s2) in continuous form, and it guarantees the discretization converges to one consistent object — the same heat kernel of §s8.

#### Worked check — the free propagator from the slicing

Integrating out *all* interior nodes by repeated Gaussian convolution (the variance simply adds, $\epsilon+\epsilon+\dots=n\epsilon=t$) gives the total transition density from $0$ to $x$ in time $t$:
$$
\int_{x(0)=0}^{x(t)=x}\mathcal{D}W=\frac{1}{\sqrt{2\pi t}}\exp\!\Big(-\frac{x^2}{2t}\Big),
$$
once again the heat kernel of §s8 — the Wiener path integral, summed over all paths, reproduces ordinary diffusion. We have now derived the same Gaussian by three independent routes (random walk limit §s4, Fokker–Planck §s8, path integral §s10).

#### Common pitfalls

- There is no Lebesgue "$dx$ on path space"; only the *normalized* Gaussian limit is meaningful. Always keep the prefactor $(2\pi\epsilon)^{-n/2}$ attached.
- The exponent $\int\dot x^2$ is a heuristic; rigorously one works with increments, never with the (nonexistent) derivative $\dot x$.

<a id="s11"></a>
### The Feynman path integral in quantum mechanics: the free-particle propagator and recovering the Schrödinger equation

#### What & why

Feynman's idea: a quantum particle's amplitude to go from $a$ to $b$ is a sum over **all** paths, each weighted by $e^{iS[x]/\hbar}$, where $S=\int L\,dt$ is the **classical action** (the time-integral of the **Lagrangian** $L=\tfrac12 m\dot x^2-V(x)$; see the Calculus of Variations guide) and $\hbar$ is the reduced Planck constant. Formally it is the Wiener integral (§s10) with the real Gaussian weight replaced by an oscillatory phase — the substitution $\tfrac12\dot x^2\to\tfrac{i}{\hbar}L$.

#### The propagator as a path integral

> **Definition.** The **propagator** $K(x_b,t_b;x_a,t_a)$ is the amplitude for a particle at $x_a$ at time $t_a$ to be found at $x_b$ at time $t_b$. Feynman's prescription:
> $$
> K(x_b,t_b;x_a,t_a)=\int_{x(t_a)=x_a}^{x(t_b)=x_b}\exp\!\Big(\frac{i}{\hbar}S[x(\cdot)]\Big)\,\mathcal{D}x.
> $$

The same time-slicing as §s10 makes this a limit of ordinary (now complex) Gaussian integrals, with each slice contributing $\exp\!\big(\frac{i}{\hbar}\,\frac{m}{2}\frac{(x_k-x_{k-1})^2}{\epsilon}-\frac{i}{\hbar}\epsilon V\big)$ and a normalizing prefactor $\big(\frac{m}{2\pi i\hbar\epsilon}\big)^{1/2}$ per slice.

#### Worked example — the free-particle propagator

Free particle: $V=0$, $L=\tfrac12 m\dot x^2$. Discretize with $n$ slices of length $\epsilon$ and do the Gaussian integrals over interior nodes.

1. The slice weight is $\big(\tfrac{m}{2\pi i\hbar\epsilon}\big)^{1/2}\exp\!\big(\tfrac{im}{2\hbar\epsilon}(x_k-x_{k-1})^2\big)$ — a Gaussian in the increment with *imaginary* variance $\tfrac{i\hbar\epsilon}{m}$.
2. Use the complex Gaussian convolution: combining two adjacent slices integrates out $x_k$ and gives one slice of doubled "time," $\big(\tfrac{m}{2\pi i\hbar(2\epsilon)}\big)^{1/2}\exp\!\big(\tfrac{im}{2\hbar(2\epsilon)}(x_{k+1}-x_{k-1})^2\big)$ — the same convolution rule as §s10 but with $\epsilon\to i\hbar\epsilon/m$.
3. Iterating over all $n$ slices makes the times add to $n\epsilon=t_b-t_a=:T$:
$$
K(x_b,t_b;x_a,t_a)=\sqrt{\frac{m}{2\pi i\hbar T}}\;\exp\!\Big(\frac{im\,(x_b-x_a)^2}{2\hbar T}\Big).
$$
4. Interpret: the exponent is exactly $\frac{i}{\hbar}S_{\text{cl}}$, where $S_{\text{cl}}=\frac{m(x_b-x_a)^2}{2T}$ is the classical action of the straight-line free path (constant velocity $(x_b-x_a)/T$). The quantum amplitude is the *classical action in the phase*, times a Gaussian-fluctuation prefactor.

This is the precise analytic continuation of the Wiener heat kernel of §s10: replace $t\to i\hbar t/m$ and the diffusion Gaussian becomes the free propagator.

#### Recovering the Schrödinger equation

The propagator advances the wavefunction $\psi(x,t)=\int K(x,t;y,t-\epsilon)\,\psi(y,t-\epsilon)\,dy$. We extract the Schrödinger equation by expanding for small $\epsilon$.

1. For one short step with potential $V$, $K(x,t;y,t-\epsilon)=\big(\tfrac{m}{2\pi i\hbar\epsilon}\big)^{1/2}\exp\!\big(\tfrac{im(x-y)^2}{2\hbar\epsilon}-\tfrac{i}{\hbar}\epsilon V(x)\big)$.
2. The Gaussian factor is sharply peaked: it forces $y$ close to $x$, with typical spread $(x-y)^2\sim\hbar\epsilon/m$. Substitute $\eta=y-x$ and Taylor-expand $\psi(y)=\psi(x)+\eta\psi_x+\tfrac12\eta^2\psi_{xx}+\cdots$.
3. Do the resulting Gaussian moment integrals over $\eta$ (with imaginary variance): $\int e^{im\eta^2/2\hbar\epsilon}\,d\eta=(2\pi i\hbar\epsilon/m)^{1/2}$ (normalizes the prefactor to $1$); the odd moment $\int\eta\,(\cdots)\,d\eta=0$; and $\int\eta^2(\cdots)\,d\eta=(2\pi i\hbar\epsilon/m)^{1/2}\cdot\tfrac{i\hbar\epsilon}{m}$.
4. Collecting terms to first order in $\epsilon$, and expanding $e^{-i\epsilon V/\hbar}\approx1-\tfrac{i}{\hbar}\epsilon V$ and the left side $\psi(x,t)\approx\psi(x,t-\epsilon)+\epsilon\,\partial_t\psi$:
$$
\psi+\epsilon\,\partial_t\psi=\psi+\frac{i\hbar\epsilon}{2m}\,\partial_{xx}\psi-\frac{i\epsilon}{\hbar}V\psi+O(\epsilon^2).
$$
5. Cancel $\psi$, divide by $\epsilon$, multiply by $i\hbar$, and let $\epsilon\to0$:
$$
i\hbar\,\frac{\partial\psi}{\partial t}=-\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2}+V(x)\,\psi,
$$
the **Schrödinger equation**. $\blacksquare$

The path integral and the Schrödinger PDE are thus two descriptions of one theory — exactly as Brownian paths and the diffusion PDE were in §s8. The factor $i$ is the only difference.

#### Common pitfalls

- The path-integral "measure" $\mathcal{D}x$ is, even more than the Wiener case, only defined through the time-slicing limit; the prefactor $(m/2\pi i\hbar\epsilon)^{1/2}$ per slice is part of its definition.
- Oscillatory (complex) Gaussians converge only conditionally; rigor usually proceeds by Wick rotation to the Euclidean integral of §s12, where the weight is again a genuine probability.

<a id="s12"></a>
### Euclidean (imaginary-time) path integrals and the connection to the statistical-mechanics partition function

#### What & why

The free propagator (§s11) is a Gaussian with *imaginary* time. Rotating time to be imaginary, $t\to -i\tau$ (a **Wick rotation**), turns the oscillating phase $e^{iS/\hbar}$ into a decaying weight $e^{-S_E/\hbar}$ — a real probability, exactly the Wiener weight of §s10. This is not a trick: it identifies quantum mechanics in imaginary time with classical statistical mechanics, and gives the path integral its firmest mathematical footing.

#### Wick rotation

Set $t=-i\tau$ with $\tau$ real ("Euclidean time"). Then the time integral in the action transforms, and the **Euclidean action** becomes
$$
S_E=\int\Big(\tfrac12 m\big(\tfrac{dx}{d\tau}\big)^2+V(x)\Big)d\tau,
$$
with a crucial sign flip: the Lagrangian $\tfrac12 m\dot x^2-V$ becomes the *energy* $\tfrac12 m x'^2+V$ (kinetic plus potential). The phase factor turns into a real Boltzmann-like weight:
$$
e^{iS/\hbar}\;\longrightarrow\;e^{-S_E/\hbar}.
$$
*Why the sign flips.* With $t=-i\tau$, $dt=-i\,d\tau$ and $\dot x=dx/dt=i\,dx/d\tau$, so the kinetic term $\tfrac12 m\dot x^2\,dt=\tfrac12 m(i x')^2(-i\,d\tau)=\tfrac12 m x'^2\,(i)\,d\tau\cdot(-1)\cdot\!\dots$ — carrying the factors through, $iS/\hbar=-S_E/\hbar$ with $S_E$ the energy integral above. The oscillatory measure has become the genuinely convergent Wiener-type measure of §s10 (with $\hbar$ playing the role that $\epsilon$ played there).

#### The partition function connection

In statistical mechanics, a system in thermal equilibrium at temperature $T$ has **partition function** $Z=\sum_{\text{states}}e^{-E/k_BT}=\mathrm{Tr}\,e^{-\beta H}$, where $H$ is the **Hamiltonian** (energy operator), $\beta=1/k_BT$ is **inverse temperature**, $k_B$ is Boltzmann's constant, and $\mathrm{Tr}$ (trace) sums the diagonal $\langle x|\cdot|x\rangle$ over all configurations.

The bridge: the quantum **time-evolution operator** is $e^{-iHt/\hbar}$, and the Euclidean propagator is $\langle x_b|e^{-H\tau/\hbar}|x_a\rangle$ — the *same* operator with $t=-i\tau$. Comparing with $e^{-\beta H}$ gives the identification
$$
\tau/\hbar \;=\;\beta\;=\;\frac{1}{k_BT}.
$$
So **imaginary time is inverse temperature**. Therefore:

1. The Euclidean path integral over a time interval of "length" $\tau=\hbar\beta$ computes the matrix element $\langle x_b|e^{-\beta H}|x_a\rangle$.
2. Taking the **trace** means setting $x_b=x_a$ and integrating over that common value — i.e. summing over all **periodic** paths $x(0)=x(\hbar\beta)$:
$$
Z=\mathrm{Tr}\,e^{-\beta H}=\oint_{x(0)=x(\hbar\beta)}\exp\!\Big(-\frac{1}{\hbar}\int_0^{\hbar\beta}\Big[\tfrac12 m\,x'^2+V(x)\Big]d\tau\Big)\,\mathcal{D}x.
$$

In words: *the quantum partition function at temperature $T$ is a Wiener-style path integral over closed loops of imaginary-time duration $\hbar\beta$.* The randomness of Brownian motion (§s10) and the thermal fluctuations of statistical mechanics are, after this rotation, the very same Gaussian path measure.

#### Worked check — high-temperature (classical) limit

As $T\to\infty$, $\beta\to0$, so the loop duration $\hbar\beta\to0$: every periodic path is squeezed to a single point and the kinetic term suppresses any motion. Only the constant path survives, the loop integral collapses to $\int e^{-\beta V(x)}\,dx$ (times a kinetic Gaussian giving the **thermal de Broglie** prefactor), and we recover the *classical* partition function $Z_{\text{cl}}\propto\int e^{-\beta V(x)}\,dx$. The path integral correctly reduces to classical Boltzmann statistics in the high-temperature limit — a check that the whole construction is consistent.

#### Common pitfalls

- Wick rotation is an analytic continuation; results computed in Euclidean time must be rotated back ($\tau\to it$) to recover real-time quantum amplitudes, and this back-rotation can be subtle.
- The trace forces *periodic* boundary conditions (closed loops); open propagators use fixed endpoints. Mixing these up changes the answer.

---

*This guide built the mathematics of randomness in motion from the ground up: stochastic processes and their finite-dimensional laws, Markov chains with the Chapman–Kolmogorov equation and stationary distributions, the Poisson process and continuous-time chains, and Brownian motion — continuous yet nowhere differentiable, with quadratic variation $(dW)^2=dt$. On that foundation we erected the Itô calculus, solved the geometric-Brownian-motion and Ornstein–Uhlenbeck SDEs in closed form, and crossed the great bridge to deterministic PDEs through the Fokker–Planck and Feynman–Kac formulas. Finally the Wiener path integral discretized the space of paths into a Gaussian measure, the Feynman path integral carried that idea — with a single factor of $i$ — into quantum mechanics and regenerated the Schrödinger equation, and the Wick rotation revealed imaginary time to be inverse temperature, fusing quantum amplitudes with the statistical-mechanics partition function. The single thread: averaging over all random histories turns the jitter of an individual path into the smooth law of an ensemble, and the same Gaussian sum-over-paths describes diffusion, finance, and the quantum world alike.*
