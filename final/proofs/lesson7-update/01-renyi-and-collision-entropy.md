# 01 — Rényi entropy and collision entropy ($\alpha=2$)

**Claim.** The Rényi entropy of order $\alpha$ is
$$H_\alpha(X)=\frac1{1-\alpha}\log\sum_i p_i^\alpha,$$
and at $\alpha=2$ it becomes the **collision entropy** $H_2(X)=-\log\sum_i p_i^2=-\log\Pr[X=X']$, where $X'$ is an independent copy of $X$.

---

### 1. In plain words
Shannon entropy is one member of a whole family (Rényi entropies), indexed by $\alpha$, all measuring "spread" but weighting the probabilities differently. At $\alpha=2$ the quantity $\sum_i p_i^2$ is exactly the **collision probability** — the chance that two independent draws from the distribution come out equal. Spread-out distributions rarely collide (high collision entropy); peaked ones collide often (low collision entropy). Rényi entropies are designed so independent sources add: $H_\alpha(X,Y)=H_\alpha(X)+H_\alpha(Y)$.

### 2. Toolbox
- Probability vector $p=(p_i)$, $p_i\ge0$, $\sum_i p_i=1$.
- Independent copies $X,X'$: $\Pr[X=X']=\sum_i\Pr[X=i]\Pr[X'=i]=\sum_i p_i^2$.
- $\lim_{\alpha\to1}H_\alpha=H$ (Shannon), by L'Hôpital.

### 3. The proof
1. Plug $\alpha=2$ into the definition: $H_2(X)=\frac1{1-2}\log\sum_i p_i^2=-\log\sum_i p_i^2$.
2. Identify the sum as a collision probability: drawing $X$ and an independent $X'$ from the same distribution,
$$\Pr[X=X']=\sum_i\Pr[X=i\text{ and }X'=i]=\sum_i p_i\cdot p_i=\sum_i p_i^2.$$
3. Therefore $H_2(X)=-\log\Pr[X=X']$. ∎

**Interpretation.** Spread-out ⇒ small $\sum p_i^2$ ⇒ large $H_2$ (collisions rare, lots of randomness). Concentrated ⇒ large $\sum p_i^2$ ⇒ small $H_2$.

### 4. Where the magic happens
**$\sum_i p_i^2$ is literally "probability two samples agree."** Rényi's $\frac1{1-\alpha}\log(\cdot)$ wrapper is engineered to keep independent events additive while letting $\alpha$ tune how harshly you weight high-probability outcomes; $\alpha=2$ lands on the operationally meaningful collision probability.

### 5. If he pushes back
- *"How do the orders compare?"* $H_\alpha$ is non-increasing in $\alpha$: $H_0\ge H_1(=\text{Shannon})\ge H_2\ge\cdots\ge H_\infty$. So $H_2\ge H_\infty$ always.
- *"Why does QIT care about $H_2$?"* The Leftover Hashing Lemma's collision-probability proof runs on $H_2$, and $H_2\ge H_{\min}$ lets you convert to the min-entropy bound ([07](07-classical-leftover-hashing.md)).
- *"What's $\alpha\to\infty$?"* The min-entropy $-\log\max_i p_i$ — the most pessimistic order ([02](02-min-entropy.md)).
