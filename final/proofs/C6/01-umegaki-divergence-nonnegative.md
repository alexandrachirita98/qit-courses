# 01 — Umegaki divergence is $\ge0$, $=0$ iff $\rho=\sigma$ (Klein's inequality)

**Claim.** The quantum relative entropy $D(\rho\|\sigma)=-\text{Tr}\big(\rho(\log\sigma-\log\rho)\big)$ satisfies $D(\rho\|\sigma)\ge0$, with equality iff $\rho=\sigma$. If $\text{supp}\,\rho\not\subseteq\text{supp}\,\sigma$ (some eigenvector of $\rho$ lives where $\sigma$ has a zero eigenvalue), then $D(\rho\|\sigma)=+\infty$.

---

### 1. In plain words
The Umegaki divergence is the quantum version of KL divergence — a "distance-like" measure of how distinguishable $\rho$ is from $\sigma$. It's never negative, and it's zero only when the two states are identical. The proof reduces the quantum statement to the *classical* KL inequality by a clever use of Jensen: replace a sum involving $\sigma$'s eigenvalues by a single logarithm. The infinite case is the quantum "you assigned probability 0 to something that happens" pathology.

### 2. Toolbox
- Eigendecompositions $\rho=\sum_i p_i|\psi_i\rangle\langle\psi_i|$, $\sigma=\sum_j q_j|\phi_j\rangle\langle\phi_j|$.
- $\log$ is concave; **Jensen**: $\sum_j w_j\log q_j\le\log\sum_j w_j q_j$ for weights $w_j\ge0$, $\sum_j w_j=1$.
- Classical **Gibbs/KL inequality**: $D_{\mathrm{KL}}(p\|r)=\sum_i p_i\log\frac{p_i}{r_i}\ge0$, $=0$ iff $p=r$.
- $|\langle\psi_i|\phi_j\rangle|^2$ are doubly-stochastic weights (rows/columns sum to 1).

### 3. The proof
Assume supports are compatible (else see below). Expand in eigenbases:
1. $\langle\psi_i|\log\sigma|\psi_i\rangle=\sum_j|\langle\psi_i|\phi_j\rangle|^2\log q_j$ — $\log\sigma=\sum_j\log q_j\,|\phi_j\rangle\langle\phi_j|$.
2. $D(\rho\|\sigma)=\sum_i p_i\big(\log p_i-\langle\psi_i|\log\sigma|\psi_i\rangle\big)=\sum_i p_i\Big(\log p_i-\sum_j|\langle\psi_i|\phi_j\rangle|^2\log q_j\Big).$
3. **Jensen** on the inner sum (weights $w_j=|\langle\psi_i|\phi_j\rangle|^2$ summing to 1):
$$\sum_j|\langle\psi_i|\phi_j\rangle|^2\log q_j\le\log\sum_j|\langle\psi_i|\phi_j\rangle|^2 q_j=:\log r_i.$$
4. Therefore $D(\rho\|\sigma)\ge\sum_i p_i(\log p_i-\log r_i)=D_{\mathrm{KL}}(p\|r)\ge0$, where $r_i=\sum_j|\langle\psi_i|\phi_j\rangle|^2q_j$ is a probability vector ($\sum_i r_i=\sum_j q_j=1$). ∎

**Equality.** Need *both* Jensen tight and $D_{\mathrm{KL}}(p\|r)=0$:
5. Jensen is tight iff all $q_j$ with $|\langle\psi_i|\phi_j\rangle|^2>0$ are equal — forcing $|\langle\psi_i|\phi_j\rangle|^2\in\{0,1\}$, i.e. the eigenbases coincide (a permutation $\tau$ with $|\psi_i\rangle=|\phi_{\tau(i)}\rangle$, $r_i=q_{\tau(i)}$).
6. $D_{\mathrm{KL}}(p\|r)=0$ iff $p=r$. Together: same eigenvectors *and* same eigenvalues ⇒ $\rho=\sigma$. ∎

**Infinite case.** If $|\psi_0\rangle\in\ker\sigma$ but $\langle\psi_0|\rho|\psi_0\rangle=p_0>0$, then $\langle\psi_0|\log\sigma|\psi_0\rangle=\log0=-\infty$, so $-p_0\langle\psi_0|\log\sigma|\psi_0\rangle=+\infty$; the divergence is defined as $+\infty$. (You can never confuse $\rho$ for $\sigma$ if $\rho$ can produce an outcome $\sigma$ forbids.)

### 4. Where the magic happens
**Jensen converts the quantum cross term $\sum_j|\langle\psi_i|\phi_j\rangle|^2\log q_j$ into a single $\log r_i$, reducing the quantum inequality to the classical KL inequality.** The squared overlaps $|\langle\psi_i|\phi_j\rangle|^2$ are doubly stochastic, exactly as in [C4/11](../C4/11-von-neumann-entropy-is-the-minimum.md) — the recurring "measurement blurs eigenvalues" structure.

### 5. If he pushes back
- *"Is $D$ a metric?"* No — not symmetric ($D(\rho\|\sigma)\ne D(\sigma\|\rho)$) and no triangle inequality. It's a divergence (premetric).
- *"Why does $D=\infty$ matter?"* It captures perfect distinguishability when supports differ; crucial for the support conditions in min-entropy/QKD (C7).
- *"Where is this used next?"* Everywhere: the DPI ([02](02-data-processing-inequality.md)), mutual information ([06](06-quantum-mutual-information.md)), conditional entropy ([09](09-conditional-von-neumann-entropy.md)) are all built on $D$.
