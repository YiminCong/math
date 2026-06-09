**English** · [中文](complete-guide.zh.md)

# Statistics, *connected.*

A full first course — describing data, the probability that underlies it, and the inference it powers — laid out basics → advanced. Every core formula is **demonstrated** from the ground up, with every symbol defined the first time it appears and every algebraic step justified. Nothing is left "to the reader."

[← Back to all guides](../README.md)

#### How to read this guide

You do not need any prior mathematics. Whenever a new symbol appears, it is defined in plain words. Whenever a formula is stated, it is followed by a numbered derivation in which **every line says both what we do and why we are allowed to do it**, and then by a fully worked example with real numbers. If a later section uses an earlier result, that result is restated in one line and pointed to (for example, "recall from §s3"). Read once straight through for the shape of the subject; afterwards, return to any single box as a standalone reference.

A few notations used everywhere:

- $\sum_{i=1}^{n} a_i$ means "add up the quantities $a_1, a_2, \dots, a_n$." The symbol $\sum$ is a capital Greek "S" (for "sum"); $i$ is the **index** that counts from the bottom number to the top number.
- $\int_a^b g(x)\,dx$ means "the area under the curve $y=g(x)$ between $x=a$ and $x=b$." It is the continuous analogue of a sum.
- A bar over a letter, like $\bar x$, means "the average of those values."
- A hat over a letter, like $\hat p$, means "an estimate of that quantity computed from data."

## Part A · Describing data

<a id="s0"></a>
### The big picture

Statistics is the science of learning from data *in the presence of variability*. "Variability" simply means: if you measure the same kind of thing twice — two people's heights, two coin tosses, two days of sales — you generally get different numbers. Statistics is the set of tools for drawing reliable conclusions even though the numbers wobble.

The subject has three movements, and the whole course is the bridge between them.

- **Describe** — summarize the data you actually have: where it is centered, how spread out it is, what shape it has.
- **Model** — use *probability* (the mathematics of chance) to describe the random process that could have generated such data.
- **Infer** — reason backwards from the limited data you saw to a statement about the larger world, while being honest about how uncertain that statement is.

> **Principle — the core problem**
>
> We almost never see the whole **population** (the entire collection of individuals or items we care about); we see only a **sample** (a smaller subset we actually measured). Statistics quantifies how much a sample can tell us about the population, and how confident we may be. **Probability** runs "population → sample" (given the whole, predict the part); **inference** runs "sample → population" (given the part, deduce the whole). They are inverses of each other.

#### A first concrete picture

Imagine a city of 1,000,000 voters (the **population**). You cannot phone all of them, so you phone 1,000 chosen at random (the **sample**). 540 say they support a measure. The true city-wide support rate is some fixed but unknown number; your job in this course is to learn how to say something trustworthy about that unknown number — and to attach a margin of error — using only the 1,000 answers. Every technique in Parts C and D is, ultimately, an answer to this single question.

#### The whole course on one line

> Describe data → Probability → Random variables & the Normal → Sampling distributions → Confidence intervals & tests → Regression

Keep this line in mind: each arrow is a section, and each section feeds the next. By the end you will see that one idea — the **z-score**, "how far is this value from what we expected, measured in standard deviations?" — threads through every box.

<a id="s1"></a>
### Data & variables

*Before any formula: know what kind of thing you are measuring. The type of variable dictates every method that follows — which summary, which graph, which test.*

> **Concept — population vs sample, parameter vs statistic**
>
> A **population** is everyone or everything of interest. A **sample** is the subset you actually observe. A number that describes the population is a **parameter** — it is fixed (it has one true value) but usually unknown, and we write it with Greek letters: $\mu$ (mu, the population mean), $\sigma$ (sigma, the population standard deviation), $p$ (a population proportion). The same kind of number *computed from your sample* is a **statistic** — it is observed (you can write it down) but random (a different sample would give a different value); we write these with ordinary letters and hats or bars: $\bar x$ (sample mean), $s$ (sample standard deviation), $\hat p$ (sample proportion). **All of inference is the act of using a statistic to estimate a parameter.**

**Definitions of the key terms used above**

- **Mean / average**: add the values, divide by how many there are.
- **Standard deviation**: a measure of typical spread; made precise in §s2.
- **Proportion**: a fraction between 0 and 1, e.g. "0.54 of voters."

**Types of variables**

A **variable** is any characteristic that can differ from individual to individual. There are two broad families.

- **Categorical** (also called *qualitative*) variables put each individual into a labelled group.
  - *Nominal*: labels with **no natural order**, e.g. eye color (blue, brown, green).
  - *Ordinal*: labels with a **natural order** but no fixed numeric spacing, e.g. a rating (poor, fair, good, excellent).
- **Numerical** (also called *quantitative*) variables record an actual number.
  - *Discrete*: values you can count, usually whole numbers, e.g. the number of children in a family (0, 1, 2, …).
  - *Continuous*: values from measuring on a scale, which can in principle take any value in a range, e.g. height (172.3 cm).

Why this matters: a categorical variable is summarized by **counts and proportions** and is analysed with tools like the chi-square test (§s12); a numerical variable is summarized by a **mean and standard deviation** and is analysed with z-, t-, or F-tests (§s12). Choosing the wrong family is the most common beginner mistake.

> **Principle — random sampling is what makes inference valid**
>
> A **simple random sample (SRS)** is a sample drawn so that every member of the population has an equal chance of being selected, independently of the others. This is not a bureaucratic formality: it is the precise assumption that lets the probability theory of Part B apply to real data. **Bias** means a *systematic* error — a tilt in one direction — caused by how the data was collected (for example, polling only people who answer landlines). Bias **cannot be removed by collecting more data**; a bigger biased sample is just a bigger biased sample. Only a better sampling method removes bias.

**Worked example — spotting variable types and bias**

A coffee shop records, for each customer: drink size (small/medium/large), number of items bought, and the exact amount spent in dollars.

1. Drink size is **categorical, ordinal** (sizes have an order, but "large minus medium" is not a fixed number of ounces unless specified).
2. Number of items is **numerical, discrete** (a count: 1, 2, 3, …).
3. Amount spent is **numerical, continuous** (a measured quantity like \$7.45).
4. If the shop only surveys customers who come in before 9 a.m., any conclusion about "all customers" is **biased**, because morning customers may buy differently from afternoon ones — and surveying *more* mornings would not fix it.

<a id="s2"></a>
### Describing center & spread

*Two questions summarize any dataset: where is it centered, and how spread out is it? This section answers both, and proves the one formula beginners always find mysterious — why sample variance divides by $n-1$.*

**Measures of center**

> **What it says and why we care.** The **mean** is the balance point of the data: add everything up and share it equally. It is the single number that best summarizes "the typical size" when the data is not badly lopsided.

We write the sample mean as $\bar x$ and the population mean as $\mu$:

$$
\bar x=\frac1n\sum_{i=1}^n x_i,\qquad \mu=\frac1N\sum_{i=1}^N x_i
$$

Here $x_i$ is the $i$-th data value, $n$ is the number of values **in the sample**, and $N$ is the number of values **in the whole population**. The symbol $\sum_{i=1}^{n} x_i$ means $x_1+x_2+\cdots+x_n$. So $\bar x$ is "the sum of all the values, divided by how many there are."

- **Median**: line the values up from smallest to largest; the median is the middle one (or the average of the two middle ones if $n$ is even). It is **robust to outliers** — meaning a single huge value does not drag it much.
- **Mode**: the value that occurs most often.

The mean is *pulled toward a skew* (toward a long tail of extreme values); the median *resists* it. That contrast is itself a useful diagnostic (see §s3).

**Worked example — center**

Data: $2, 4, 4, 5, 100$ (here $n=5$).

1. Mean: $\bar x=\frac{2+4+4+5+100}{5}=\frac{115}{5}=23$.
2. Median: sorted, the middle (3rd) value is $4$.
3. Mode: $4$ (it appears twice).

Notice the single outlier $100$ pushed the mean up to $23$, far above the bulk of the data, while the median stayed at $4$. This is exactly why we report both.

**Measures of spread**

> **What it says and why we care.** Center alone is not enough: the datasets $\{50,50,50\}$ and $\{0,50,100\}$ have the same mean but feel completely different. **Spread** measures how far the values typically sit from the center.

$$
\sigma^2=\frac1N\sum_{i=1}^{N}(x_i-\mu)^2,\qquad s^2=\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar x)^2
$$

$$
\text{SD}=\sqrt{\text{variance}},\qquad \text{IQR}=Q_3-Q_1,\qquad \text{range}=\max-\min
$$

Definitions of the new symbols:

- $\sigma^2$ ("sigma squared") is the **population variance**; $s^2$ is the **sample variance**.
- $x_i-\mu$ is the **deviation** of value $i$ from the mean: how far above (positive) or below (negative) the center it lies.
- **SD** is the **standard deviation**, the square root of the variance; it returns the spread to the original units (dollars, cm, …).
- $Q_1$ and $Q_3$ are the **first and third quartiles**: the values below which 25% and 75% of the data fall. The **IQR** (interquartile range) is the spread of the middle half.
- $\max$ and $\min$ are the largest and smallest values; their difference is the **range**.

> **Concept — why variance squares the deviations**
>
> The deviations $x_i-\bar x$ always sum to zero (we prove this just below), so simply averaging them would always give $0$ and tell us nothing. **Squaring** does two jobs: it makes every term positive (so they cannot cancel) and it punishes large misses much more heavily than small ones. Taking the square root at the very end (the **standard deviation**) returns to the original units, so the final number reads as a "typical distance from the mean."

**Demonstration — the deviations always sum to zero**

This fact is used repeatedly, so we prove it once.

1. Start from the sum of deviations and split the sum (a sum of a difference is the difference of the sums — a basic property of $\sum$):
   $$
   \sum_{i=1}^{n}(x_i-\bar x)=\sum_{i=1}^{n}x_i-\sum_{i=1}^{n}\bar x.
   $$
2. The term $\bar x$ does not depend on $i$, so adding it $n$ times gives $n\bar x$ (definition of multiplication as repeated addition):
   $$
   =\sum_{i=1}^{n}x_i-n\bar x.
   $$
3. By the definition of the mean, $\bar x=\frac1n\sum x_i$, so $\sum x_i=n\bar x$. Substitute (replacing $\sum x_i$ by the equal quantity $n\bar x$):
   $$
   =n\bar x-n\bar x=0.
   $$

So the raw deviations carry no information about size — which is exactly why we must square them.

**Demonstration — why the sample variance divides by $n-1$ (Bessel's correction)**

> **Goal.** Explain, step by step, why $s^2$ uses $n-1$ in the denominator rather than $n$, and why this makes $s^2$ an **unbiased** estimate of $\sigma^2$ (meaning: on average over many samples it lands on the true value, $E[s^2]=\sigma^2$; the symbol $E[\cdot]$ is the long-run average, defined fully in §s6).

1. We want to measure spread around the *true* center $\mu$, but $\mu$ is unknown, so we substitute the *sample* center $\bar x$. This is the only honest choice — but it has a side effect.
2. The sample mean $\bar x$ is, by its definition in this section, the value that makes $\sum(x_i-\bar x)^2$ **as small as possible** among all constants. (Reason: the derivative of $\sum(x_i-c)^2$ with respect to $c$ is $-2\sum(x_i-c)$, which is zero exactly when $c=\bar x$ — the same minimization idea used for regression in §s13.) Therefore using $\bar x$ in place of the true $\mu$ makes the sum of squares **systematically too small**.
3. Quantify the shrinkage. Add and subtract $\bar x$ inside the deviation from $\mu$ (a legal step: we add $0$ written as $-\bar x+\bar x$):
   $$
   \sum_{i=1}^{n}(x_i-\mu)^2=\sum_{i=1}^{n}\big((x_i-\bar x)+(\bar x-\mu)\big)^2.
   $$
4. Expand the square using $(a+b)^2=a^2+2ab+b^2$ and split the sum:
   $$
   =\sum (x_i-\bar x)^2+2(\bar x-\mu)\sum(x_i-\bar x)+n(\bar x-\mu)^2.
   $$
   (The factor $(\bar x-\mu)$ is constant in $i$, so it comes outside its sum; the last term is $(\bar x-\mu)^2$ added $n$ times.)
5. By the previous demonstration, $\sum(x_i-\bar x)=0$, so the middle term vanishes:
   $$
   \sum (x_i-\mu)^2=\sum(x_i-\bar x)^2+n(\bar x-\mu)^2.
   $$
6. Rearranging, $\sum(x_i-\bar x)^2=\sum(x_i-\mu)^2-n(\bar x-\mu)^2$. The second piece is positive, confirming step 2: the deviations from $\bar x$ are smaller than those from $\mu$.
7. Take expectations (long-run averages). The average of $\sum(x_i-\mu)^2$ is $n\sigma^2$ (each term averages to $\sigma^2$, by the definition of $\sigma^2$). The average of $n(\bar x-\mu)^2$ is $n\cdot\mathrm{Var}(\bar x)=n\cdot\frac{\sigma^2}{n}=\sigma^2$ (using the standard-error result proved in §s9). Therefore:
   $$
   E\!\left[\sum(x_i-\bar x)^2\right]=n\sigma^2-\sigma^2=(n-1)\sigma^2.
   $$
8. Divide by $(n-1)$ so the average comes out to exactly $\sigma^2$:
   $$
   E\!\left[\frac{1}{n-1}\sum(x_i-\bar x)^2\right]=\sigma^2,\qquad\text{i.e. } E[s^2]=\sigma^2.
   $$

That is the whole reason for the $n-1$: it exactly cancels the one unit of "shrinkage" caused by estimating the center from the same data. We say one **degree of freedom** was "spent" estimating $\bar x$; only $n-1$ deviations are then free to vary, since they must sum to $0$. If the population mean $\mu$ were genuinely known, you would not spend that degree of freedom, and you would divide by $n$.

**Worked example — variance and SD**

Data $\{2,4,6\}$ as a sample, so $n=3$.

1. Mean: $\bar x=\frac{2+4+6}{3}=4$.
2. Deviations: $2-4=-2$, $4-4=0$, $6-4=2$. (Check they sum to $0$: yes.)
3. Squared deviations: $4, 0, 4$; their sum is $8$.
4. Sample variance: $s^2=\frac{8}{n-1}=\frac{8}{2}=4$.
5. Sample standard deviation: $s=\sqrt{4}=2$. So a "typical" value sits about $2$ units from the mean of $4$ — which matches the data.

**Common pitfall.** Do not confuse $\sigma$ (population, divide by $N$) with $s$ (sample, divide by $n-1$). Calculators usually offer both; using the wrong one slightly mis-scales every later interval and test.

<a id="s3"></a>
### Distributions & visualizing data

*Center and spread do not capture **shape** — and shape changes everything about which method is appropriate.*

> **Concept — shape & skew**
>
> A **distribution** is the pattern of how often each value (or range of values) occurs. A distribution can be **symmetric** (the left half mirrors the right), **right-skewed** (a long tail stretching toward large values; this pulls the mean *above* the median), or **left-skewed** (a long tail toward small values; mean *below* median). The relationship "mean vs median" is therefore a quick read on skew. A **histogram** is a bar chart of how many values fall in each range — it reveals shape. A **boxplot** draws the **five-number summary**: minimum, $Q_1$, median, $Q_3$, maximum.

**Why mean-vs-median detects skew (short justification).** A long right tail contains a few very large values. From §s2 we saw the mean is sensitive to such extremes while the median is not. So a right tail drags the mean upward past the unmoved median; hence "mean > median" signals right skew. The symmetric mirror argument gives the left-skew case.

**Percentiles, z-scores & outliers**

A **percentile** is the value below which a given percent of the data lies (the 90th percentile is the value beating 90% of the data). The **z-score** rescales any value into "number of standard deviations from the mean":

$$
z=\frac{x-\mu}{\sigma}\qquad(\text{how many SDs the value } x \text{ lies from the mean})
$$

A common rule flags a point as an **outlier** (an unusually extreme value worth investigating) when it falls far outside the middle half:

$$
x < Q_1-1.5\,\text{IQR}\quad\text{or}\quad x > Q_3+1.5\,\text{IQR}
$$

**Worked example — z-score and the outlier rule**

A test has mean $\mu=70$ and SD $\sigma=8$.

1. A score of $x=86$ has $z=\frac{86-70}{8}=\frac{16}{8}=2$: it is **2 standard deviations above average**. By the empirical rule of §s8, only about 2.5% of scores are that high or higher.
2. Suppose a dataset has $Q_1=40$, $Q_3=60$, so $\text{IQR}=60-40=20$ and $1.5\,\text{IQR}=30$. The fences are $40-30=10$ and $60+30=90$. A value of $95$ exceeds the upper fence ($95>90$), so it is flagged as an outlier; a value of $88$ is not.

> **Connection — the z-score is the thread of the whole course**
>
> The z-score strips away units and scale: it converts any value into "distance from center, measured in standard deviations." This single idea returns as the **standard Normal** (§s8), the **test statistic** (§s11), and the basis of **correlation** (§s13). Whenever you see a fraction with "(thing) − (its center)" on top and "(a standard deviation)" on the bottom, you are looking at a z-score in disguise.

## Part B · Probability

<a id="s4"></a>
### Probability basics

*Probability is the mathematics of chance — the engine that, run in reverse, lets a sample speak about a population.*

> **Concept — sample space & events**
>
> The **sample space** $S$ is the set of *all* possible outcomes of a random experiment. An **event** is any subset of $S$ — a collection of outcomes we might care about. The **probability** $P(A)$ of event $A$ is a number measuring how likely $A$ is, on a scale from $0$ (impossible) to $1$ (certain). For a fair six-sided die, $S=\{1,2,3,4,5,6\}$, and "roll an even number" is the event $A=\{2,4,6\}$.

**The axioms & basic rules**

The whole theory rests on three simple rules (the **axioms**), plus two consequences we will prove.

$$
0\le P(A)\le 1,\qquad P(S)=1,\qquad P(A^c)=1-P(A)
$$

$$
P(A\cup B)=P(A)+P(B)-P(A\cap B)
$$

Definitions of the new symbols:

- $A^c$ is the **complement** of $A$: "$A$ does not happen" (all outcomes not in $A$).
- $A\cup B$ ("$A$ union $B$") means "$A$ or $B$ (or both) happens."
- $A\cap B$ ("$A$ intersect $B$") means "$A$ and $B$ both happen."

**Demonstration — the complement rule $P(A^c)=1-P(A)$**

1. Every outcome is either in $A$ or not in $A$, and never both. So $A$ and $A^c$ together make up all of $S$ with no overlap: $A\cup A^c=S$ and $A\cap A^c=\varnothing$ (the empty set).
2. For two events with no overlap, probabilities add (this is the third axiom in its "mutually exclusive" form): $P(A\cup A^c)=P(A)+P(A^c)$.
3. But $A\cup A^c=S$, and $P(S)=1$ by the second axiom. So $P(A)+P(A^c)=1$.
4. Subtract $P(A)$ from both sides: $P(A^c)=1-P(A)$.

**Demonstration — the addition rule (why we subtract the overlap)**

1. Suppose we try to compute $P(A\cup B)$ by simply adding $P(A)+P(B)$.
2. Any outcome that is in **both** $A$ and $B$ (that is, in $A\cap B$) has then been counted **twice** — once inside $P(A)$ and once inside $P(B)$.
3. To fix the double-count, subtract the overlap exactly once:
   $$
   P(A\cup B)=P(A)+P(B)-P(A\cap B).
   $$
4. **Special case — mutually exclusive events.** If $A$ and $B$ cannot happen together, then $A\cap B=\varnothing$ and $P(A\cap B)=0$, so the rule simplifies to $P(A\cup B)=P(A)+P(B)$.

**Worked example — addition rule with a deck of cards**

Draw one card from a standard 52-card deck. Let $A$ = "the card is a heart" and $B$ = "the card is a King."

1. $P(A)=\frac{13}{52}$ (13 hearts), $P(B)=\frac{4}{52}$ (4 Kings).
2. The overlap $A\cap B$ is "the King of Hearts," a single card: $P(A\cap B)=\frac{1}{52}$.
3. By the addition rule, $P(\text{heart or King})=\frac{13}{52}+\frac{4}{52}-\frac{1}{52}=\frac{16}{52}=\frac{4}{13}\approx0.308$.
4. **Pitfall check.** Naively adding $\frac{13}{52}+\frac{4}{52}=\frac{17}{52}$ would wrongly count the King of Hearts twice — that is exactly what the subtraction prevents.

<a id="s5"></a>
### Conditional probability & Bayes' theorem

*How knowing one thing changes the probability of another — and how to flip the direction of conditioning around.*

**Conditional probability, multiplication, independence**

> **What it says and why we care.** Often we learn partial information and want to update a probability. The **conditional probability** $P(A\mid B)$ ("probability of $A$ **given** $B$") is the chance of $A$ once we already know $B$ happened.

$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)},\qquad P(A\cap B)=P(A\mid B)\,P(B)
$$

$$
A,B \text{ independent} \iff P(A\cap B)=P(A)\,P(B)
$$

- $P(A\mid B)$ is read "the probability of $A$ given $B$."
- **Independent** means knowing $B$ tells you nothing about $A$ (and vice versa); the symbol $\iff$ means "if and only if" (the two statements are equivalent).

**Why the conditional formula makes sense (justification).** Once we know $B$ happened, the world shrinks: only outcomes inside $B$ are still possible, so $B$ becomes our new "sample space." Among those, the ones where $A$ also happens form $A\cap B$. The conditional probability is therefore the fraction of $B$'s probability that also lies in $A$ — which is precisely $\frac{P(A\cap B)}{P(B)}$. Multiplying both sides by $P(B)$ gives the **multiplication rule** $P(A\cap B)=P(A\mid B)P(B)$.

**Why independence reads as multiplication (justification).** If $A$ and $B$ are independent, then learning $B$ does not change the chance of $A$: $P(A\mid B)=P(A)$. Substitute that into the multiplication rule: $P(A\cap B)=P(A\mid B)P(B)=P(A)P(B)$.

**Bayes' theorem**

$$
P(A\mid B)=\frac{P(B\mid A)\,P(A)}{P(B)},\qquad P(B)=\sum_i P(B\mid A_i)P(A_i)
$$

The second formula is the **law of total probability**: it builds up $P(B)$ by splitting the world into mutually exclusive causes $A_1, A_2, \dots$ (which together cover everything) and adding the chance of $B$ through each.

**Demonstration — Bayes' theorem in two lines**

1. Write the joint probability $P(A\cap B)$ in **both** orders using the multiplication rule from above (the order of "and" does not matter, so both equal the same joint probability):
   $$
   P(A\cap B)=P(A\mid B)\,P(B)=P(B\mid A)\,P(A).
   $$
2. Take the right-hand equality, $P(A\mid B)P(B)=P(B\mid A)P(A)$, and divide both sides by $P(B)$ (allowed because $P(B)>0$):
   $$
   P(A\mid B)=\frac{P(B\mid A)\,P(A)}{P(B)}.
   $$

So Bayes' theorem is nothing more than the multiplication rule written twice and rearranged. It **reverses the direction of conditioning** — turning "probability of the evidence given the cause," $P(B\mid A)$, into "probability of the cause given the evidence," $P(A\mid B)$.

**Worked example — the medical-test surprise (full numbers)**

A disease affects 1% of people. A test is 99% accurate in both directions: if you have the disease it is positive 99% of the time; if you do not, it is negative 99% of the time. You test positive. What is the chance you actually have the disease?

Let $A$ = "has disease," $B$ = "tests positive."

1. Given numbers: $P(A)=0.01$ (the **base rate**), $P(A^c)=0.99$, $P(B\mid A)=0.99$, $P(B\mid A^c)=0.01$ (a false positive).
2. Total probability of a positive test (split over the two causes, "sick" and "healthy"):
   $$
   P(B)=P(B\mid A)P(A)+P(B\mid A^c)P(A^c)=0.99\times0.01+0.01\times0.99=0.0099+0.0099=0.0198.
   $$
3. Apply Bayes:
   $$
   P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}=\frac{0.99\times0.01}{0.0198}=\frac{0.0099}{0.0198}=0.5.
   $$
4. So even after a positive result on a 99%-accurate test, there is only a **50%** chance the disease is present.

> **Principle — why Bayes surprises people**
>
> For a rare condition, even a very accurate test produces many false positives, because the small number of true cases is swamped by the enormous healthy population (in the example, the 0.99% true positives are matched by 0.99% false positives). Bayes forces you to weight the test result by the **base rate** $P(A)$ — the lesson at the heart of medical screening, spam filters, and fraud detection alike. **Common pitfall:** confusing $P(B\mid A)$ ("positive given sick," which is high) with $P(A\mid B)$ ("sick given positive," which can be low). They are not the same number, and Bayes is the bridge between them.

<a id="s6"></a>
### Random variables & expectation

*A **random variable** attaches a number to each outcome of a random experiment; **expectation** is its long-run average value.*

A random variable is usually written with a capital letter like $X$. Example: toss a coin; let $X=1$ for heads and $X=0$ for tails. $X$ turns outcomes into numbers we can do arithmetic on.

**Expectation & variance**

> **What it says and why we care.** The **expectation** $E[X]$ (also called the **mean** of $X$) is the average value of $X$ you would get if you repeated the experiment forever. It is a weighted average: each possible value is weighted by its probability.

$$
E[X]=\sum_x x\,P(x)\quad\text{(discrete)},\qquad E[X]=\int x\,f(x)\,dx\quad\text{(continuous)}
$$

$$
\mathrm{Var}(X)=E\big[(X-\mu)^2\big]=E[X^2]-\big(E[X]\big)^2
$$

Definitions:

- For a **discrete** variable, $P(x)$ is the probability that $X$ equals the value $x$, and we sum over all possible values.
- For a **continuous** variable, $f(x)$ is the **probability density function** — a curve whose height represents relative likelihood — and the integral $\int$ is the continuous version of the sum.
- $\mathrm{Var}(X)$ is the **variance** of $X$: the expected squared distance from its mean $\mu=E[X]$. Its square root is the standard deviation of $X$.
- More generally, the expectation of *any function* of $X$ is found by the same weighted average: $E[g(X)]=\sum_x g(x)\,P(x)$ (discrete) or $\int g(x)f(x)\,dx$ (continuous). In particular $E[X^2]=\sum_x x^2\,P(x)$ — used in the variance shortcut and the die example below.

> **Connection — this is where calculus enters**
>
> For continuous variables, the density $f(x)$ plays the role of a function, and **probability is area under it**: the chance that $X$ lands between $a$ and $b$ is the area below the curve over that interval,
> $$
> P(a\le X\le b)=\int_a^b f(x)\,dx.
> $$
> Expectation becomes an integral, not a sum. The Normal curve (§s8), percentiles (§s3), and p-values (§s11) are *all* areas under a density — the integral calculus made concrete.

**Linearity & sums**

$$
E[aX+b]=a\,E[X]+b,\qquad E[X+Y]=E[X]+E[Y]
$$

$$
\mathrm{Var}(aX+b)=a^2\mathrm{Var}(X),\qquad \mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)\ \text{(if independent)}
$$

Here $a$ and $b$ are fixed constants, and $Y$ is another random variable. "Linearity of expectation" — the rule $E[X+Y]=E[X]+E[Y]$ — is remarkable because it holds **even when $X$ and $Y$ are not independent**. Variance only adds for *independent* variables.

**Demonstration — linearity $E[aX+b]=aE[X]+b$ (discrete case)**

1. Start from the definition with $aX+b$ in place of the value:
   $$
   E[aX+b]=\sum_x (a x+b)\,P(x).
   $$
2. Distribute the multiplication and split the sum (both are basic algebra/$\sum$ rules):
   $$
   =a\sum_x x\,P(x)+b\sum_x P(x).
   $$
3. The first sum is $E[X]$ by definition; the second sum is $\sum_x P(x)=1$ because the probabilities of all outcomes add to $1$. Hence:
   $$
   =a\,E[X]+b\cdot 1=a\,E[X]+b.
   $$

**Demonstration — the variance shortcut $\mathrm{Var}(X)=E[X^2]-(E[X])^2$**

1. Begin from the definition of variance and expand the square inside, using $(X-\mu)^2=X^2-2\mu X+\mu^2$:
   $$
   \mathrm{Var}(X)=E\big[(X-\mu)^2\big]=E\big[X^2-2\mu X+\mu^2\big].
   $$
2. Apply linearity of expectation (the rule just proved) to break the expectation across the three terms; note $\mu$ is a constant so it pulls outside:
   $$
   =E[X^2]-2\mu\,E[X]+\mu^2.
   $$
3. Substitute $E[X]=\mu$ (the definition of $\mu$ as the mean of $X$):
   $$
   =E[X^2]-2\mu\cdot\mu+\mu^2=E[X^2]-2\mu^2+\mu^2=E[X^2]-\mu^2.
   $$
4. Writing $\mu=E[X]$ back gives the headline form, the handy "mean of the square minus the square of the mean":
   $$
   \mathrm{Var}(X)=E[X^2]-\big(E[X]\big)^2.
   $$

**Worked example — expectation and variance of a die**

Roll a fair six-sided die; $X$ is the number shown, each value with probability $\frac16$.

1. $E[X]=\sum_{x=1}^{6} x\cdot\frac16=\frac{1+2+3+4+5+6}{6}=\frac{21}{6}=3.5$.
2. $E[X^2]=\frac{1^2+2^2+3^2+4^2+5^2+6^2}{6}=\frac{1+4+9+16+25+36}{6}=\frac{91}{6}\approx15.17$.
3. By the shortcut, $\mathrm{Var}(X)=E[X^2]-(E[X])^2=\frac{91}{6}-(3.5)^2=15.1\overline{6}-12.25=2.91\overline{6}$.
4. Standard deviation: $\sqrt{2.9167}\approx1.71$. So a single roll typically lands about $1.7$ away from the average of $3.5$ — sensible for values spread over $1$ to $6$.

<a id="s7"></a>
### Common distributions

*A handful of named distributions model most real situations. Know each one's "story," its mean, and its variance, and you can recognize them in the wild.*

| Distribution | Models | Mean | Variance |
| --- | --- | --- | --- |
| Bernoulli($p$) | one yes/no trial | $p$ | $p(1-p)$ |
| Binomial($n,p$) | $\#$ successes in $n$ independent trials | $np$ | $np(1-p)$ |
| Geometric($p$) | trials until the first success | $1/p$ | $(1-p)/p^2$ |
| Poisson($\lambda$) | rare events per fixed interval | $\lambda$ | $\lambda$ |
| Uniform($a,b$) | equally likely anywhere on $[a,b]$ | $(a+b)/2$ | $(b-a)^2/12$ |
| Normal($\mu,\sigma^2$) | sums of many small effects | $\mu$ | $\sigma^2$ |
| Exponential($\lambda$) | waiting time between events | $1/\lambda$ | $1/\lambda^2$ |

Reading the table: $p$ is a success probability, $n$ a number of trials, $\lambda$ ("lambda") an average rate, and $[a,b]$ a range. A **Bernoulli** trial is a single yes/no experiment (a coin flip). A **Binomial** counts the successes in $n$ such flips.

**The binomial probability**

> **What it says and why we care.** The Binomial answers: in $n$ independent yes/no trials, each succeeding with probability $p$, what is the chance of getting **exactly** $k$ successes?

$$
P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}
$$

Definition of the new symbol: $\binom{n}{k}$ ("$n$ choose $k$") is the **number of ways** to choose which $k$ of the $n$ trials are the successes. It equals $\dfrac{n!}{k!\,(n-k)!}$, where $n!$ ("$n$ factorial") means $n\times(n-1)\times\cdots\times1$.

**Why the formula has this shape (justification).** Fix one specific pattern of $k$ successes and $n-k$ failures (say SS…SFF…F). Because the trials are independent, the probability of *that one* pattern is $p$ multiplied $k$ times and $(1-p)$ multiplied $n-k$ times — i.e. $p^k(1-p)^{n-k}$ (multiplication rule for independent events, §s5). Every arrangement of the same $k$ successes has the same probability, and there are $\binom{n}{k}$ such arrangements. Adding these equally-likely, mutually exclusive arrangements (addition rule, §s4) multiplies that probability by $\binom{n}{k}$, giving the formula.

**Demonstration — why the binomial mean is $np$ and variance is $np(1-p)$**

1. A Binomial is just a sum of $n$ independent Bernoulli trials: $X=X_1+X_2+\cdots+X_n$, where each $X_i$ is $1$ (success) with probability $p$ and $0$ (failure) with probability $1-p$.
2. Find the mean of one Bernoulli trial from the definition of expectation (§s6): $E[X_i]=1\cdot p+0\cdot(1-p)=p$.
3. By **linearity of expectation** (§s6), which needs no independence, add the $n$ identical pieces:
   $$
   E[X]=E[X_1]+\cdots+E[X_n]=\underbrace{p+\cdots+p}_{n\text{ terms}}=np.
   $$
4. Find the variance of one trial via the shortcut $\mathrm{Var}(X_i)=E[X_i^2]-(E[X_i])^2$ (§s6). Since $X_i$ is $0$ or $1$, $X_i^2=X_i$, so $E[X_i^2]=p$, giving $\mathrm{Var}(X_i)=p-p^2=p(1-p)$.
5. Because the trials are **independent**, variances add (§s6):
   $$
   \mathrm{Var}(X)=\sum_{i=1}^{n}\mathrm{Var}(X_i)=np(1-p).
   $$

The recurring move of probability is on display: **decompose a complicated variable into simple independent pieces, handle one piece, then sum.**

**Worked example — Binomial with numbers**

Flip a fair coin $n=5$ times ($p=0.5$). What is the probability of exactly $k=2$ heads, and what is the expected number of heads?

1. $\binom{5}{2}=\frac{5!}{2!\,3!}=\frac{120}{2\times6}=10$ ways to place the 2 heads.
2. Each such pattern has probability $0.5^2\times0.5^3=0.5^5=\frac{1}{32}$.
3. So $P(X=2)=10\times\frac{1}{32}=\frac{10}{32}=0.3125$.
4. Expected number of heads: $E[X]=np=5\times0.5=2.5$; variance $np(1-p)=5\times0.5\times0.5=1.25$.

<a id="s8"></a>
### The Normal distribution & the Central Limit Theorem

*The bell curve, and the theorem that explains why it appears almost everywhere in nature and in statistics.*

**The Normal density & standardizing**

> **What it says and why we care.** The **Normal distribution** is the famous symmetric "bell curve." Its full shape is fixed by just two numbers: the mean $\mu$ (where the peak sits) and the standard deviation $\sigma$ (how wide the bell is). It models any quantity built up from many small, independent contributions (heights, measurement errors, sample means).

$$
f(x)=\frac{1}{\sigma\sqrt{2\pi}}\,e^{-\frac{(x-\mu)^2}{2\sigma^2}},\qquad Z=\frac{X-\mu}{\sigma}\sim N(0,1)
$$

Definitions: $f(x)$ is the density (height of the curve) at value $x$; $e\approx2.718$ is the base of natural logarithms; $\pi\approx3.14159$; $N(0,1)$ is the **standard Normal** — a Normal with mean $0$ and SD $1$; the symbol $\sim$ means "is distributed as." The transformation $Z=\frac{X-\mu}{\sigma}$ is exactly the **z-score** of §s3.

**Why standardizing works (justification).** Subtracting $\mu$ shifts the curve so its center sits at $0$; dividing by $\sigma$ rescales the horizontal axis so one unit equals one standard deviation. Because the bell's shape is identical for every $\mu,\sigma$ once recentered and rescaled, **any** Normal problem reduces to one standard Normal — which is why a single table (or a single software function) answers them all.

> **Principle — the empirical (68–95–99.7) rule**
>
> For *any* Normal distribution, about **68%** of the values lie within $1$ SD of the mean, about **95%** within $2$ SD, and about **99.7%** within $3$ SD. These percentages are fixed areas under the bell. This is the reason that, later, "about $2$ standard errors" becomes a "$95\%$ confidence interval" (§s10).

**Worked example — using standardizing and the empirical rule**

Adult heights are roughly Normal with $\mu=170$ cm and $\sigma=10$ cm.

1. What fraction are between $160$ and $180$ cm? Those bounds are $\mu\pm1\sigma$ (since $160=170-10$ and $180=170+10$), so by the empirical rule about **68%**.
2. How unusual is $190$ cm? Standardize: $z=\frac{190-170}{10}=2$. That is $2$ SD above the mean; by the rule, only about $\frac{100\%-95\%}{2}=2.5\%$ of people are that tall or taller.

> **Principle — the Central Limit Theorem (CLT)**
>
> Take repeated samples of size $n$ from *any* population whatsoever, with mean $\mu$ and SD $\sigma$. As $n$ grows, the distribution of the **sample mean** $\bar X$ becomes approximately Normal — **regardless of the original population's shape** — centered at $\mu$ with standard deviation $\sigma/\sqrt n$:
> $$
> \bar X \approx N\!\left(\mu,\ \frac{\sigma^2}{n}\right)\quad\text{for large }n.
> $$
> This is the single most important result in the subject. It is *why* Normal-based methods work on skewed, lumpy, real-world data: even if individual values are not Normal, their average is.

**Why the CLT's center and spread are what they are (partial justification).** We do not prove the full bell-curve conclusion here (it requires advanced tools), but we *can* prove the two numbers. The center $\mu$ follows from linearity of expectation (§s6): $E[\bar X]=E\big[\frac1n\sum X_i\big]=\frac1n\sum E[X_i]=\frac1n\cdot n\mu=\mu$. The spread $\sigma/\sqrt n$ is derived in full in §s9. So the CLT's claim is "this average is approximately Normal, with the mean and SD we can already compute."

**Worked example — the CLT in action**

A population of single dice rolls is *flat*, not bell-shaped (each face equally likely, mean $3.5$, SD $\approx1.71$ from §s6). Take samples of $n=36$ rolls and average them.

1. By the CLT, the sample mean $\bar X$ is approximately Normal even though one roll is not.
2. Its center is still $\mu=3.5$.
3. Its SD shrinks to $\sigma/\sqrt n=1.71/\sqrt{36}=1.71/6\approx0.285$. So averages of 36 rolls cluster tightly around $3.5$, in a bell shape — the flat distribution has been "Normalized" by averaging.

> **Connection — the spine of all inference**
>
> Normal density (area = probability, §s6) → z-scores standardize any Normal (§s3) → the CLT makes the sample mean $\bar X$ Normal (this section) → therefore the confidence intervals and z/t-tests of Part C are all just statements about **areas under one bell curve**. Master this chain and the rest of the course is bookkeeping.

## Part C · Statistical inference

<a id="s9"></a>
### Sampling distributions & the standard error

*A statistic computed from a random sample is itself random — compute it from a different sample and you get a different number. The distribution of those numbers is the key to all inference.*

> **Concept — the sampling distribution**
>
> Imagine taking *every possible* sample of size $n$ from the population and computing the sample mean $\bar x$ for each. The collection of all those $\bar x$ values forms the **sampling distribution of the mean**. Its spread — called the **standard error (SE)** — measures how much an estimate bounces around from one sample to the next. Crucially, the standard error is **not** the spread of the raw data; it is the spread of the *estimate*.

**Standard error of the mean & proportion**

$$
\text{SE}(\bar X)=\frac{\sigma}{\sqrt n},\qquad \text{SE}(\hat p)=\sqrt{\frac{p(1-p)}{n}}
$$

Here $\hat p$ is the sample proportion (the fraction of "successes" in the sample), and $p$ is the true population proportion. Both formulas say the same thing: more data ($n$ larger) means a smaller standard error, hence a more precise estimate.

**Demonstration — why the standard error has a $\sqrt n$**

1. Write the sample mean as a scaled sum (just the definition of the mean):
   $$
   \bar X=\frac1n\big(X_1+X_2+\cdots+X_n\big),
   $$
   where the $X_i$ are independent draws, each with variance $\sigma^2$.
2. Use the scaling rule for variance, $\mathrm{Var}(aX)=a^2\mathrm{Var}(X)$ (§s6), with $a=\frac1n$, together with the rule that independent variances add (§s6):
   $$
   \mathrm{Var}(\bar X)=\frac{1}{n^2}\mathrm{Var}(X_1+\cdots+X_n)=\frac{1}{n^2}\sum_{i=1}^{n}\mathrm{Var}(X_i).
   $$
3. Each of the $n$ terms equals $\sigma^2$, so the sum is $n\sigma^2$:
   $$
   \mathrm{Var}(\bar X)=\frac{1}{n^2}\,(n\sigma^2)=\frac{\sigma^2}{n}.
   $$
4. The standard error is the standard deviation of $\bar X$, i.e. the square root of its variance:
   $$
   \text{SE}(\bar X)=\sqrt{\mathrm{Var}(\bar X)}=\sqrt{\frac{\sigma^2}{n}}=\frac{\sigma}{\sqrt n}.
   $$

The $\sqrt n$ on the bottom has a famous consequence: to **halve** your uncertainty you must **quadruple** the sample size (because $\sqrt{4}=2$). This is the law of diminishing returns that governs every poll and experiment.

**Worked example — standard error**

A population has SD $\sigma=20$. You take a sample of $n=100$.

1. $\text{SE}(\bar X)=\frac{20}{\sqrt{100}}=\frac{20}{10}=2$. So sample means typically land within about $2$ of the true mean.
2. To shrink the SE to $1$ (half as big), solve $\frac{20}{\sqrt n}=1$, giving $\sqrt n=20$, so $n=400$ — four times as much data, exactly as the $\sqrt n$ rule predicts.

<a id="s10"></a>
### Confidence intervals

*An estimate is more honest reported as a range than as a single number. A **confidence interval** is that range, together with a statement of how often the method succeeds.*

**The general form**

$$
\text{estimate}\ \pm\ (\text{critical value})\times\text{SE}
$$

$$
\bar x \pm z^{*}\frac{\sigma}{\sqrt n}\quad(\sigma\text{ known}),\qquad \bar x \pm t^{*}\frac{s}{\sqrt n}\quad(\sigma\text{ unknown})
$$

$$
\hat p \pm z^{*}\sqrt{\tfrac{\hat p(1-\hat p)}{n}}
$$

Definitions: the **critical value** ($z^{*}$ or $t^{*}$) is the number of standard errors you reach out on each side to capture the desired percentage of the sampling distribution; for $95\%$ confidence with large $n$, $z^{*}\approx1.96$. The $\pm$ part is the **margin of error**. The symbols $s$ and $t^{*}$ are explained in the connection box below.

Note on the proportion interval: the true standard error is $\sqrt{p(1-p)/n}$, which depends on the unknown $p$; we substitute the estimate $\hat p$ for $p$ inside the square root. This **plug-in approximation** is accurate for large $n$ (where $\hat p\approx p$).

**Why this form works (justification).** From §s9 the estimate $\bar x$ is centered on the true $\mu$ with spread $\text{SE}$, and from the CLT (§s8) it is approximately Normal. The empirical rule (§s8) says about $95\%$ of Normal values fall within (just under) $2$ SE of the center. So reaching out $z^{*}\approx1.96$ standard errors on each side traps the true value in $95\%$ of samples. That is exactly what the formula does.

> **Concept — what "95% confident" actually means**
>
> It does **not** mean "there is a 95% chance the true value lies in *this particular* interval." The true parameter is a fixed number, not random — it is either in your interval or it is not. What "95% confident" means is: the **procedure** generates intervals that capture the true value $95\%$ of the time across many repeated samples. You trust the *method*, not the single interval. For a $95\%$ interval with large $n$, $z^{*}\approx1.96$ — the "$2$ SD" of the empirical rule, made exact.

> **Connection — why the t-distribution appears**
>
> When $\sigma$ is unknown (the usual case) we estimate it with the sample SD $s$ from §s2. Plugging in an *estimated* spread injects extra uncertainty, especially for small $n$. The **t-distribution** is a bell curve like the Normal but with slightly **fatter tails**, which widens the interval to honestly account for that extra uncertainty. We then use a critical value $t^{*}$ (a bit larger than $z^{*}$) read off the t-distribution. As $n\to\infty$, $s\to\sigma$ and the t-distribution converges back to the Normal, so $t^{*}\to z^{*}$.

**Worked example — a 95% confidence interval for a mean ($\sigma$ known)**

A sample of $n=100$ has mean $\bar x=50$; the population SD is known to be $\sigma=20$.

1. Standard error (§s9): $\text{SE}=\frac{20}{\sqrt{100}}=2$.
2. Critical value for 95% confidence: $z^{*}=1.96$.
3. Margin of error: $1.96\times2=3.92$.
4. Interval: $50\pm3.92$, i.e. from $46.08$ to $53.92$. We are "95% confident" — in the procedure sense above — that the true mean lies in this range.

**Worked example — a confidence interval for a proportion**

A poll of $n=1000$ finds $\hat p=0.54$ support.

1. $\text{SE}(\hat p)=\sqrt{\frac{0.54\times0.46}{1000}}=\sqrt{\frac{0.2484}{1000}}=\sqrt{0.0002484}\approx0.01576$.
2. Margin of error at 95%: $1.96\times0.01576\approx0.0309$, i.e. about $\pm3.1$ percentage points.
3. Interval: $0.54\pm0.031$, roughly $0.509$ to $0.571$. Since the whole interval is above $0.5$, the data suggests genuine majority support.

<a id="s11"></a>
### Hypothesis testing

*A formal way to ask: is what I observed surprising enough to rule out mere chance?*

> **Concept — the logic of a test**
>
> We assume a **null hypothesis** $H_0$ — the skeptical default that "nothing special is going on" (e.g. "the coin is fair," "the new drug has no effect"). We then ask: *if $H_0$ were true*, how likely is data at least as extreme as what we actually saw? That probability is the **p-value**. If the p-value is very small, our data would be a near-miracle under $H_0$, so we **reject** $H_0$ in favour of the **alternative hypothesis** $H_a$ ("something is going on"). It is proof by (probabilistic) contradiction: assume nothing happened, show the data is then absurdly unlikely, conclude something happened.

**The test statistic & p-value**

$$
z=\frac{\bar x-\mu_0}{\sigma/\sqrt n},\qquad t=\frac{\bar x-\mu_0}{s/\sqrt n}
$$

Definitions: $\mu_0$ is the value of the mean *claimed by the null hypothesis*. The denominator is the standard error (§s9). So the test statistic is, once again, a **z-score** (§s3): it measures **how many standard errors the observed estimate sits away from the null value**. The **p-value** is the tail area of the bell beyond that statistic. We **reject $H_0$ when the p-value is below a pre-chosen threshold $\alpha$** (the **significance level**, typically $\alpha=0.05$).

**Why the test statistic is a z-score (justification).** Under $H_0$, the CLT (§s8) says $\bar x$ is approximately Normal centered at $\mu_0$ with spread $\sigma/\sqrt n$. Standardizing it — subtract the center, divide by the spread, exactly as in §s3 — produces a standard-Normal quantity. A large $|z|$ means the data sits far out in the tail, an unlikely place if $H_0$ holds; the area past it is the p-value.

**The two errors & power**

$$
\text{Type I }(\alpha):\text{ reject a true }H_0,\qquad \text{Type II }(\beta):\text{ fail to reject a false }H_0
$$

$$
\text{Power}=1-\beta=\text{the chance of detecting a real effect}
$$

A **Type I error** is a false alarm (crying "effect!" when there is none); its probability is exactly the threshold $\alpha$ we chose. A **Type II error** ($\beta$, "beta") is a miss (failing to notice a real effect). **Power** is the complement of a miss: the probability of correctly detecting a true effect.

> **Principle — the trade-off you can't escape**
>
> Lowering $\alpha$ (fewer false alarms) raises $\beta$ (more missed real effects), and vice versa — for a fixed sample, you cannot reduce both. The *only* way to shrink both at once is a **larger sample**, because (from §s9) that shrinks the standard error, sharpening the whole picture. **Common pitfall:** a non-significant result means "not enough evidence to reject $H_0$," **not** "$H_0$ is proven true." Absence of evidence is not evidence of absence.

**Worked example — a one-sample z-test**

A machine is supposed to fill bottles to $\mu_0=500$ ml. You sample $n=25$ bottles, find mean $\bar x=495$, and know $\sigma=10$.

1. Standard error: $\frac{\sigma}{\sqrt n}=\frac{10}{\sqrt{25}}=\frac{10}{5}=2$.
2. Test statistic: $z=\frac{495-500}{2}=\frac{-5}{2}=-2.5$. The sample mean sits $2.5$ standard errors *below* the claimed fill.
3. For a two-sided test, the p-value is the area beyond $\pm2.5$, which is about $0.0124$ (roughly $1.24\%$).
4. Since $0.0124<\alpha=0.05$, we **reject** $H_0$: there is significant evidence the machine is under-filling.

> **Connection — intervals and tests are the same coin**
>
> A two-sided test at level $\alpha$ rejects $H_0:\mu=\mu_0$ **exactly when** $\mu_0$ falls *outside* the $(1-\alpha)$ confidence interval (§s10). Reason: both are built from the same statistic $\frac{\bar x-\mu_0}{\text{SE}}$ and the same critical value; "$\mu_0$ more than $z^{*}$ SEs away" is simultaneously "reject" and "outside the interval." In the bottle example, the 95% interval is $495\pm1.96\times2=495\pm3.92=(491.08,\ 498.92)$, which does *not* contain $500$ — the same conclusion as the test.

<a id="s12"></a>
### The common tests

*Which test to run is decided by two questions: what **type** are your variables (§s1), and how many **groups** are you comparing?*

| Test | Use when… | Statistic |
| --- | --- | --- |
| z-test | one mean/proportion, $\sigma$ known or large $n$ | $z=\frac{\bar x-\mu_0}{\sigma/\sqrt n}$ |
| One-sample t | one mean, $\sigma$ unknown | $t=\frac{\bar x-\mu_0}{s/\sqrt n}$ |
| Two-sample t | compare two group means | $t=\frac{\bar x_1-\bar x_2}{\text{SE}}$ |
| Paired t | before/after on the same subjects | $t$ on the within-pair differences |
| Chi-square $\chi^2$ | categorical data: goodness-of-fit or independence | $\chi^2=\sum\frac{(O-E)^2}{E}$ |
| ANOVA (F-test) | compare 3+ group means | $F=\frac{\text{between-group variance}}{\text{within-group variance}}$ |

Every entry in the "Statistic" column is a comparison of a signal to a measure of noise — that is the unifying idea.

> **Concept — what chi-square and F are really doing**
>
> **Chi-square** ($\chi^2$) compares the **observed** counts $O$ in each category to the counts $E$ we would **expect** if the null were true; squaring the gaps and dividing by $E$ accumulates the discrepancies into one number that grows large when observed and expected disagree. **ANOVA** ("Analysis of Variance," summarized by the **F-statistic**) asks whether the spread *between* the group means is large compared with the natural spread *within* the groups: if the groups differ by more than random noise alone would produce, at least one group mean is genuinely different.

**Demonstration — why each $\chi^2$ term is divided by $E$**

1. The raw gap between a category's observed and expected count is $O-E$. We square it, $(O-E)^2$, so over- and under-counts cannot cancel (same reasoning as squaring deviations in §s2).
2. But a gap of, say, $10$ means very different things when $E=10$ versus $E=1000$. We must judge each gap **relative to how big it was expected to be**.
3. Dividing by $E$ does exactly this rescaling, so $\frac{(O-E)^2}{E}$ measures the gap in units of "expected size." Summing over all categories combines them into the total statistic $\chi^2=\sum\frac{(O-E)^2}{E}$. A large total means the observed pattern is far from what the null predicts.

**Worked example — a chi-square goodness-of-fit test**

Roll a die $60$ times; under "the die is fair," each face is expected $E=10$ times. Suppose you observe counts $8,9,10,11,13,9$ for faces $1$–$6$.

1. Expected count for each face: $E=\frac{60}{6}=10$.
2. Terms $\frac{(O-E)^2}{E}$: $\frac{(8-10)^2}{10}=0.4$, $\frac{(9-10)^2}{10}=0.1$, $\frac{0^2}{10}=0$, $\frac{1^2}{10}=0.1$, $\frac{3^2}{10}=0.9$, $\frac{1^2}{10}=0.1$.
3. Sum: $\chi^2=0.4+0.1+0+0.1+0.9+0.1=1.6$.
4. With $6-1=5$ degrees of freedom, a $\chi^2$ of $1.6$ is small (the p-value is large, about $0.9$), so we do **not** reject fairness — these counts are well within ordinary random variation.

<a id="s13"></a>
### Correlation & regression

*From the question "are two variables related?" to the action "draw the best line through them."*

**Covariance & the correlation coefficient**

> **What it says and why we care.** **Covariance** measures whether two variables tend to move together (both above their means at once) or in opposite directions. **Correlation** $r$ is covariance rescaled to a clean, unit-free number between $-1$ and $1$ that you can compare across any datasets.

$$
\mathrm{Cov}(X,Y)=E[XY]-E[X]\,E[Y],\qquad r=\frac{\mathrm{Cov}(X,Y)}{\sigma_X\,\sigma_Y}
$$

Definitions: $\sigma_X$ and $\sigma_Y$ are the standard deviations of $X$ and $Y$; $E[XY]$ is the average of the product. A positive covariance means "when $X$ is high, $Y$ tends to be high"; a negative one means the opposite.

**Why $r$ is the average product of z-scores (justification).** From §s3, the z-score of $X$ is $z_X=\frac{X-\mu_X}{\sigma_X}$, and similarly $z_Y$. Their average product is $E[z_X z_Y]=E\!\left[\frac{(X-\mu_X)(Y-\mu_Y)}{\sigma_X\sigma_Y}\right]=\frac{E[(X-\mu_X)(Y-\mu_Y)]}{\sigma_X\sigma_Y}=\frac{\mathrm{Cov}(X,Y)}{\sigma_X\sigma_Y}=r$. So **correlation is literally the average product of the two variables' z-scores** — large and positive when both variables are simultaneously above (or below) average. Because z-scores are unit-free, $r$ is too, and it can be shown to stay within $[-1,1]$: $r=\pm1$ means a perfect straight-line relationship; $r=0$ means no *linear* relationship.

**The least-squares regression line**

$$
\hat y=b_0+b_1x,\qquad b_1=r\,\frac{s_y}{s_x},\qquad b_0=\bar y-b_1\bar x
$$

$$
R^2=r^2=\text{the fraction of the variation in }y\text{ explained by }x
$$

Definitions: $\hat y$ ("y-hat") is the line's **predicted** value of $y$ for a given $x$; $b_0$ is the **intercept** (the predicted $y$ when $x=0$); $b_1$ is the **slope** (how much $\hat y$ changes per one-unit increase in $x$); $s_x, s_y$ are the sample SDs of $x$ and $y$.

**Demonstration — deriving the slope by minimizing squared error (calculus)**

1. We want the line that fits best in the **least-squares** sense: choose $b_0,b_1$ to minimize the total squared vertical gap between data points and line. Define
   $$
   S(b_0,b_1)=\sum_{i=1}^{n}\big(y_i-b_0-b_1 x_i\big)^2.
   $$
   Each term $\big(y_i-(b_0+b_1x_i)\big)^2$ is the squared **residual**: the squared distance from the actual $y_i$ to the line's prediction.
2. To minimize a function, set its derivatives to zero (the same optimization idea used in §s2 to show $\bar x$ minimizes squared deviations). Take the partial derivative with respect to $b_0$ (treating $b_1$ as constant), using the chain rule, and set it to $0$:
   $$
   \frac{\partial S}{\partial b_0}=\sum 2\big(y_i-b_0-b_1x_i\big)(-1)=0\ \Longrightarrow\ \sum\big(y_i-b_0-b_1x_i\big)=0.
   $$
3. Take the partial derivative with respect to $b_1$ and set it to $0$:
   $$
   \frac{\partial S}{\partial b_1}=\sum 2\big(y_i-b_0-b_1x_i\big)(-x_i)=0\ \Longrightarrow\ \sum x_i\big(y_i-b_0-b_1x_i\big)=0.
   $$
   These two equations are the **normal equations**.
4. From the first normal equation, divide by $n$: $\bar y-b_0-b_1\bar x=0$, which rearranges to
   $$
   b_0=\bar y-b_1\bar x.
   $$
   (This already shows the line passes through the point $(\bar x,\bar y)$, since setting $x=\bar x$ gives $\hat y=b_0+b_1\bar x=\bar y$.)
5. Substitute $b_0=\bar y-b_1\bar x$ into the second normal equation and simplify (algebra: expand, collect the $b_1$ terms, and use the deviation forms). The result is the slope in terms of sums of cross-deviations and squared deviations:
   $$
   b_1=\frac{\sum (x_i-\bar x)(y_i-\bar y)}{\sum (x_i-\bar x)^2}.
   $$
6. Recognize the pieces: the numerator divided by $n$ is the covariance and the denominator divided by $n$ is $s_x^2$, so $b_1=\frac{\mathrm{Cov}(x,y)}{s_x^2}=\frac{\mathrm{Cov}(x,y)}{s_x s_y}\cdot\frac{s_y}{s_x}=r\,\frac{s_y}{s_x}$, matching the boxed formula.

This is the calculus optimization of the companion guide — "set the derivative to zero" — applied to data.

**Worked example — fitting a line to four points**

Data: $(1,2),(2,2),(3,4),(4,5)$.

1. Means: $\bar x=\frac{1+2+3+4}{4}=2.5$, $\bar y=\frac{2+2+4+5}{4}=3.25$.
2. Deviations $(x_i-\bar x)$: $-1.5,-0.5,0.5,1.5$; deviations $(y_i-\bar y)$: $-1.25,-1.25,0.75,1.75$.
3. Cross-products $(x_i-\bar x)(y_i-\bar y)$: $1.875,0.625,0.375,2.625$; sum $=5.5$.
4. Squared $x$-deviations: $2.25,0.25,0.25,2.25$; sum $=5.0$.
5. Slope: $b_1=\frac{5.5}{5.0}=1.1$. Intercept: $b_0=\bar y-b_1\bar x=3.25-1.1\times2.5=3.25-2.75=0.5$.
6. Best-fit line: $\hat y=0.5+1.1x$. Check it passes through $(\bar x,\bar y)=(2.5,3.25)$: $0.5+1.1\times2.5=3.25$. Correct.

> **Principle — correlation is not causation**
>
> A large $|r|$ means two variables move together; it does **not** mean one causes the other. A hidden **confounding variable** — a third factor influencing both — can manufacture a strong correlation with no causal link (ice-cream sales and drowning both rise in summer). Only a **randomized experiment**, where the researcher actively assigns the treatment, can establish causation; regression on merely observed data cannot.

## Part E · Perspective

<a id="s14"></a>
### Pitfalls & the bigger picture

*Knowing the formulas is half the battle; using them honestly is the other half.*

> **Principle — the common traps**
>
> - **p-hacking / multiple comparisons:** if you test enough things, something will look "significant" by pure luck (test 20 useless ideas at $\alpha=0.05$ and on average one "passes"). Guard against it by **pre-registering** your hypotheses and **adjusting** the threshold when you run many tests.
> - **Significant ≠ important:** with a huge sample, the standard error (§s9) becomes tiny, so even a trivial, useless effect can be "statistically significant." Always report an **effect size** (how big the effect is, in real units), not just a p-value (whether it is non-zero).
> - **Sampling bias beats sample size:** a biased million-person poll is worse than a clean thousand-person one. Recall from §s1 that bias is a systematic tilt that more data cannot cure.

**Worked example — multiple comparisons by the numbers**

Suppose $20$ independent useless hypotheses are each tested at $\alpha=0.05$ (each has a $5\%$ false-alarm rate, all genuinely null).

1. Chance one specific test does *not* falsely fire: $1-0.05=0.95$.
2. Chance *all* $20$ stay quiet (independent, so multiply, §s5): $0.95^{20}\approx0.358$.
3. Chance at least one false alarm: $1-0.358\approx0.642$ — about a **64%** chance of a spurious "discovery." This is why naïve multiple testing is so dangerous, and why thresholds must be tightened.

**Two philosophies of inference**

- **Frequentist** (this guide's default): parameters are fixed unknown constants; probability describes the long-run frequency with which *procedures* succeed. p-values and confidence intervals (§s10–§s11) are frequentist tools — they make statements about the method over repeated sampling.
- **Bayesian**: parameters themselves are treated as having probability distributions. You start from a **prior** belief, observe data, and update to a **posterior** belief using Bayes' theorem (§s5): $\text{posterior}\propto\text{likelihood}\times\text{prior}$. This directly answers "given my data, how probable is the hypothesis?" — the question frequentist p-values do *not* answer.

These are two valid lenses on the same uncertainty, suited to different questions; neither is universally "correct."

> **The habit to keep**
>
> Trace every inference back to its source of randomness. Behind every confidence interval and p-value sits one engine — the **sampling distribution**, made approximately Normal by the **CLT** (§s8) — and behind the whole subject sits one idea, the **z-score** (§s3): *how far is what we observed from what we'd expect, measured in standard deviations?* If you can answer that question, you understand statistics.

---

*A first course in statistics and probability — concepts, principles, formulas, and the full demonstrations behind them — built as a companion to the Complete Calculus guide. Read once for the shape; return to any single box as a self-contained reference. Remember the two directions: probability runs population → sample; inference runs sample → population.*
