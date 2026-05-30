# 04 — Trace distance (a metric) and the purified distance

**Claim.**
- The **trace distance** $D(\rho,\sigma)=\tfrac12\text{Tr}|\rho-\sigma|$ is a metric: $D\ge0$ with $D=0\iff\rho=\sigma$, symmetric, and satisfies the triangle inequality.
- With (generalized) fidelity $F(\rho,\sigma)=\text{Tr}|\sqrt\rho\sqrt\sigma|+\sqrt{(1-\text{Tr}\rho)(1-\text{Tr}\sigma)}$ (for sub-normalized states), the **purified distance** is $P(\rho,\sigma)=\sqrt{1-F(\rho,\sigma)^2}$, also a metric.

---

### 1. In plain words
To "smooth" entropies (next file) we need a notion of "states within $\epsilon$ of each other." Two natural choices: trace distance (operational — half the trace norm of the difference, directly the bias in distinguishing them) and purified distance (built from fidelity, behaves well under purification and partial trace). Both are genuine metrics, so $\epsilon$-balls make sense.

### 2. Toolbox
- $|A|=\sqrt{A^\dagger A}$; trace norm $\text{Tr}|A|=\sum_k s_k$ (singular values).
- Helstrom: $D(\rho,\sigma)$ = optimal bias in distinguishing $\rho,\sigma$ (equal priors) ([../C7/01-helstrom-bound.md](../C7/01-helstrom-bound.md)).
- Fidelity $F\in[0,1]$, $F=1\iff\rho=\sigma$ ([../C7/04-uhlmann-theorem.md](../C7/04-uhlmann-theorem.md)).

### 3. The proof

**Trace distance is a metric.**
1. **Nonneg & definite.** $\text{Tr}|\rho-\sigma|\ge0$, $=0\iff\rho-\sigma=0\iff\rho=\sigma$ (a matrix with zero trace norm is zero).
2. **Symmetry.** $|\rho-\sigma|=|\sigma-\rho|$, so $D(\rho,\sigma)=D(\sigma,\rho)$.
3. **Triangle inequality.** The trace norm is a norm, so $\|\rho-\tau\|_{\text{Tr}}\le\|\rho-\sigma\|_{\text{Tr}}+\|\sigma-\tau\|_{\text{Tr}}$; divide by 2:
$$D(\rho,\tau)\le D(\rho,\sigma)+D(\sigma,\tau).\qquad\checkmark$$

**Purified distance.**
4. Define $P(\rho,\sigma)=\sqrt{1-F(\rho,\sigma)^2}$. Since $F\in[0,1]$, $P\in[0,1]$, and $P=0\iff F=1\iff\rho=\sigma$; symmetric because $F$ is.
5. The triangle inequality for $P$ follows from the fact that $P$ equals the trace distance between *purifications* minimized appropriately (hence the name) — it inherits metric structure from the trace distance on the larger space. ∎

### 4. Where the magic happens
**Trace distance = distinguishing bias (operational), purified distance = "sine of the fidelity angle" (geometric).** $P=\sqrt{1-F^2}$ is literally $\sin\theta$ where $\cos\theta=F$ in the purification picture of [../C7/03-fidelity-and-discrimination.md](../C7/03-fidelity-and-discrimination.md). Either one gives a legitimate $\epsilon$-ball for smoothing.

### 5. If he pushes back
- *"Why two distances?"* Trace distance is operationally transparent; purified distance is *monotone under trace-preserving maps and stable under purification*, which makes the smooth-entropy calculus clean.
- *"How do they relate?"* Fuchs–van de Graaf: $1-F\le D\le\sqrt{1-F^2}=P$. So they're equivalent up to these bounds.
- *"Why 'generalized' fidelity?"* The extra $\sqrt{(1-\text{Tr}\rho)(1-\text{Tr}\sigma)}$ term handles **sub-normalized** states (trace $\le1$), which appear when smoothing.
