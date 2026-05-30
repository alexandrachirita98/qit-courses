# Measurement Uncertainty — mean, variance, and "bad monotony"

> Explains the C4 slide *"Measurement Uncertainty"* (mean & variance of a noisy measurement, and the $d=3$ example where the variance rises then falls). Full proofs: [C4/08](../proofs/C4/08-mean-and-variance-depend-on-eigenvalues.md), [C4/07](../proofs/C4/07-measurement-uncertainty-grows-with-epsilon.md).

## The big picture (plain words)
We take a clean state $|\psi\rangle$, add a fraction $\epsilon$ of white noise (the maximally mixed state $I/d$), and measure an observable $O$. The slide computes two statistics of the outcome — the **average** $\langle O\rangle$ and the **variance** $\Delta O^2$ — and then makes a warning point: **these two numbers depend on the arbitrary labels $\lambda_k$ you stuck on the outcomes**, so they can behave weirdly (the variance goes *up then down* as noise increases). Entropy doesn't have this problem; that's why entropy is the "honest" uncertainty measure.

## Setup: where the numbers come from
The state is
$$\rho=(1-\epsilon)\,|\psi\rangle\langle\psi|+\epsilon\,\tfrac{I}{d},$$
and we measure $O=\sum_k\lambda_k|\phi_k\rangle\langle\phi_k|$ in a basis that **contains** $|\psi\rangle$ (say $|\phi_1\rangle=|\psi\rangle$). From [C4/07](../proofs/C4/07-measurement-uncertainty-grows-with-epsilon.md) the outcome probabilities are:
$$\Pr[\lambda_1]=1-\tfrac{d-1}{d}\epsilon,\qquad \Pr[\lambda_k]=\tfrac{\epsilon}{d}\ \ (k\ge2).$$
(Intuition: with probability $1-\epsilon$ you land on $|\psi\rangle$ for sure; the noise $\epsilon$ spreads a little weight $\epsilon/d$ onto each of the other $d-1$ outcomes.)

## The mean
The average outcome is just "value × probability, summed":
$$\boxed{\ \langle O\rangle_\rho=\mathbb E[O]=\Big(1-\tfrac{d-1}{d}\epsilon\Big)\lambda_1+\tfrac{\epsilon}{d}\sum_{k=2}^d\lambda_k\ }$$
- First term: the likely outcome $\lambda_1$ times its probability.
- Second term: each of the noisy outcomes $\lambda_k$ ($k\ge2$) times $\epsilon/d$.

## The variance
Variance = "average of the square minus square of the average", $\Delta O^2=\langle O^2\rangle-\langle O\rangle^2$. Since $O^2$ has the same eigenvectors but eigenvalues $\lambda_k^2$:
$$\boxed{\ \Delta O^2_\rho=\Big(1-\tfrac{d-1}{d}\epsilon\Big)\lambda_1^2+\tfrac{\epsilon}{d}\sum_{k=2}^d\lambda_k^2-\langle O\rangle_\rho^2\ }$$

**The point:** both boxed formulas are built out of the labels $\lambda_k$. If you renamed the outcomes (e.g. used $10,20,30$ instead of $1,2,3$), these numbers would change completely — even though the *experiment* is identical. That's the warning the slide is making.

## The $d=3$ worked example (step by step)
Take $d=3$ and labels $\lambda_1=1,\ \lambda_2=2,\ \lambda_3=3$. Then:
$$\Pr[\lambda_1]=1-\tfrac{2}{3}\epsilon,\qquad \Pr[\lambda_2]=\Pr[\lambda_3]=\tfrac{\epsilon}{3}.$$

**Step 1 — mean.** Using $\lambda_2+\lambda_3=2+3=5$:
$$\langle O\rangle=\Big(1-\tfrac{2}{3}\epsilon\Big)\cdot1+\tfrac{\epsilon}{3}\cdot5=1-\tfrac{2}{3}\epsilon+\tfrac{5}{3}\epsilon=1+\epsilon.$$

**Step 2 — second moment.** Using $\lambda_2^2+\lambda_3^2=4+9=13$:
$$\langle O^2\rangle=\Big(1-\tfrac{2}{3}\epsilon\Big)\cdot1+\tfrac{\epsilon}{3}\cdot13=1-\tfrac{2}{3}\epsilon+\tfrac{13}{3}\epsilon=1+\tfrac{11}{3}\epsilon.$$

**Step 3 — variance.**
$$\Delta O^2=\langle O^2\rangle-\langle O\rangle^2=\Big(1+\tfrac{11}{3}\epsilon\Big)-(1+\epsilon)^2.$$
Expand $(1+\epsilon)^2=1+2\epsilon+\epsilon^2$:
$$\Delta O^2=1+\tfrac{11}{3}\epsilon-1-2\epsilon-\epsilon^2=\tfrac{11}{3}\epsilon-\tfrac{6}{3}\epsilon-\epsilon^2=\tfrac{5}{3}\epsilon-\epsilon^2.$$

**Step 4 — complete the square** (to see the shape):
$$\Delta O^2=\tfrac{5}{3}\epsilon-\epsilon^2=\Big(\tfrac{5}{6}\Big)^2-\Big(\epsilon-\tfrac{5}{6}\Big)^2.$$
(Check: $(\tfrac56)^2-(\epsilon-\tfrac56)^2=\tfrac{25}{36}-\epsilon^2+\tfrac{5}{3}\epsilon-\tfrac{25}{36}=\tfrac{5}{3}\epsilon-\epsilon^2$ ✓.)

## Reading the result: "bad monotony"
$\Delta O^2(\epsilon)=(\tfrac56)^2-(\epsilon-\tfrac56)^2$ is a **downward parabola** in $\epsilon$ with its peak at $\epsilon=\tfrac56$:
- for $\epsilon<\tfrac56$ the variance **increases** (more noise → more spread),
- at $\epsilon=\tfrac56$ it's **maximal**,
- for $\epsilon>\tfrac56$ it **decreases** again.

So as you crank up the noise, the variance goes **up then down** — it is *not* monotone in $\epsilon$. The slide calls this **"bad monotony… an artifact of badly chosen eigenvalues."**

## Why this is a warning, not physics
Compare with the **entropy** of the very same experiment ([C4/07](../proofs/C4/07-measurement-uncertainty-grows-with-epsilon.md)): $H(O)=h(q)+q\log(d-1)$ with $q=\tfrac{d-1}{d}\epsilon$ — this **increases monotonically** all the way to $\epsilon=1$. More noise always means more entropy.

The difference:
- **Entropy** is built from the *probabilities only* — it ignores what you named the outcomes. So it tracks the genuine "amount of randomness".
- **Mean and variance** are built from the *numeric labels* $\lambda_k$. Those labels are arbitrary for non-numeric outcomes (think "horse A, B, C"), so any quantity that depends on them — including the non-monotone variance — carries no physical meaning. Relabel the outcomes and you get a different curve.

**Takeaway for the exam:** when an observable's eigenvalues are just arbitrary tags, trust the **entropy** as the uncertainty measure (monotone, label-free), and treat the mean/variance as gauge-dependent. This is exactly why the entropic uncertainty (exam **Q4**) is the meaningful quantity, not the variance. See also [C4/14](../proofs/C4/14-why-the-average-is-meaningless.md) (why the average is meaningless) and [C4/09](../proofs/C4/09-distinct-eigenvalues-entropy-independent.md) (entropy ignores the labels).
