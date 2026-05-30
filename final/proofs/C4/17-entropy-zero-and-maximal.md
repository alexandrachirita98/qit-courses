# 17 — $H(\rho)=0 \iff$ pure; $H(\rho)=\log d \iff$ maximally mixed

**Claim.** For a density matrix $\rho$ on $\mathbb{C}^d$ with eigenvalues $\lambda_i$, the von Neumann entropy $H(\rho)=-\sum_i\lambda_i\log\lambda_i$ satisfies $0\le H(\rho)\le\log d$, with
- $H(\rho)=0\iff\rho$ is **pure** ($\rho=|\psi\rangle\langle\psi|$);
- $H(\rho)=\log d\iff\rho=\dfrac{I}{d}$ (**maximally mixed**).

---

### 1. In plain words
Von Neumann entropy is just the Shannon entropy of $\rho$'s eigenvalues, which form a probability distribution. Shannon entropy is smallest (zero) when the distribution is a spike — all probability on one eigenvalue — which means $\rho$ is a single pure state with no randomness. It's largest ($\log d$) when the distribution is flat — all eigenvalues equal $1/d$ — which means $\rho=I/d$, total ignorance. So entropy interpolates between "definitely this state" and "no idea, every direction equally likely."

### 2. Toolbox
- $H(\rho)=H(\lambda)=-\sum_i\lambda_i\log\lambda_i$, with $\lambda$ a probability vector ([05](05-every-density-matrix-is-realized.md), [11](11-von-neumann-entropy-is-the-minimum.md)).
- Each term $\eta(\lambda_i)=-\lambda_i\log\lambda_i\ge0$ on $[0,1]$, and $\eta(x)=0\iff x\in\{0,1\}$.
- **Gibbs' inequality:** for probability vectors $\lambda,u$, $D_{\mathrm{KL}}(\lambda\|u)=\sum_i\lambda_i\log\frac{\lambda_i}{u_i}\ge0$, with equality iff $\lambda=u$.
- A pure state has eigenvalues $(1,0,\dots,0)$; $\rho=I/d$ has eigenvalues $(\frac1d,\dots,\frac1d)$.

### 3. The proof

**$H\ge0$, with $H=0\iff$ pure.**
1. Every term $\eta(\lambda_i)=-\lambda_i\log\lambda_i\ge0$ (since $0\le\lambda_i\le1$), so $H(\rho)=\sum_i\eta(\lambda_i)\ge0$.
2. $H(\rho)=0\iff$ every term is $0\iff$ each $\lambda_i\in\{0,1\}$. Combined with $\sum_i\lambda_i=1$, exactly one eigenvalue is $1$ and the rest are $0$.
3. That means $\rho=1\cdot|\psi_1\rangle\langle\psi_1|=|\psi_1\rangle\langle\psi_1|$, a pure state. Conversely a pure state has eigenvalues $(1,0,\dots)$ so $H=0$. ∎

**$H\le\log d$, with $H=\log d\iff$ maximally mixed.** Compare to the uniform vector $u=(\frac1d,\dots,\frac1d)$.
4. $\displaystyle\log d-H(\rho)=\sum_i\lambda_i\log d+\sum_i\lambda_i\log\lambda_i=\sum_i\lambda_i\log\frac{\lambda_i}{1/d}=D_{\mathrm{KL}}(\lambda\|u).$
(Used $\sum_i\lambda_i=1$ so $\log d=\sum_i\lambda_i\log d$.)
5. By Gibbs, $D_{\mathrm{KL}}(\lambda\|u)\ge0$, hence $H(\rho)\le\log d$.
6. Equality $\iff D_{\mathrm{KL}}(\lambda\|u)=0\iff\lambda=u\iff$ all $\lambda_i=\frac1d\iff\rho=\frac1d\sum_i|\psi_i\rangle\langle\psi_i|=\frac1d I$. ∎

### 4. Where the magic happens
**$\log d - H(\rho)$ is *exactly* the KL divergence from $\rho$'s eigenvalues to the uniform distribution.** That one rewrite turns the upper bound into "relative entropy $\ge0$," whose equality case (uniform) instantly identifies the maximally mixed state. For the lower bound, the key is that each $-\lambda\log\lambda$ term is nonnegative and vanishes only at $\lambda\in\{0,1\}$.

### 5. If he pushes back
- *"Give the purity test without entropy."* $\rho$ is pure $\iff\rho^2=\rho$ $\iff\text{Tr}(\rho^2)=1$. (Mixed states have $\text{Tr}(\rho^2)<1$.) Equivalent to $H=0$ at the endpoints but $\text{Tr}\rho^2$ is the "purity," related to the collision/Rényi-2 entropy.
- *"Why is uniform the max-entropy distribution?"* Step 4–5 *is* that statement, specialized; it's the Gibbs inequality / concavity of $\log$.
- *"Does $H(\rho)=\log d$ depend on the basis?"* No — $H(\rho)$ is basis-independent (it's the eigenvalue entropy). It's the *measurement* entropy $H(O)$ that's basis-dependent ([11](11-von-neumann-entropy-is-the-minimum.md)); they coincide at the eigenbasis.
- *"Where is this used?"* It underpins [11](11-von-neumann-entropy-is-the-minimum.md) (upper bound $\log d$) and [18](18-depolarizing-increases-entropy.md) (mixing toward $I/d$ raises entropy).
