# 11 — Von Neumann entropy is the minimum measurement entropy (eigenbasis is best)

**Claim.** For any density matrix $\rho$ and any basis measurement $O=\{|\phi_k\rangle\}$ (distinct eigenvalues),
$$\log d\ \ge\ H(O)\ \ge\ H(\rho):=-\text{Tr}\,\rho\log\rho=-\sum_i\lambda_i\log\lambda_i,$$
with the lower bound **achieved when $\{|\phi_k\rangle\}$ is the eigenbasis of $\rho$**. So the von Neumann entropy $H(\rho)$ is the smallest possible measurement entropy, and the eigenbasis is the "best" (most informative) basis.

---

### 1. In plain words
Measuring $\rho$ in some basis gives an outcome distribution with some Shannon entropy $H(O)$. Different bases give different entropies. The claim: you can never get below $H(\rho)$, the entropy of $\rho$'s eigenvalues, and you *hit* that minimum exactly by measuring in $\rho$'s own eigenbasis (where the outcome distribution **is** the eigenvalue distribution). Any other basis "blurs" the eigenvalue distribution through a doubly-stochastic matrix, which can only raise entropy ([15](15-doubly-stochastic-never-decreases-entropy.md)). The worst you can do is the Fourier basis, $\log d$ ([10](10-fourier-is-the-worst-basis.md)).

### 2. Toolbox
- Eigen-decomposition $\rho=\sum_i\lambda_i|\psi_i\rangle\langle\psi_i|$; eigenvalue vector $p=(\lambda_i)$ is a probability vector ([05](05-every-density-matrix-is-realized.md)).
- Outcome probabilities $v_k=\langle\phi_k|\rho|\phi_k\rangle$, and (distinct eigenvalues) $H(O)=-\sum_k v_k\log v_k=H(v)$ ([09](09-distinct-eigenvalues-entropy-independent.md)).
- **Doubly-stochastic ⇒ entropy can't decrease:** $v=Dp\Rightarrow H(v)\ge H(p)$ ([15](15-doubly-stochastic-never-decreases-entropy.md)).
- Completeness $\sum_k|\phi_k\rangle\langle\phi_k|=\sum_i|\psi_i\rangle\langle\psi_i|=I$.

### 3. The proof

**Express the outcome distribution as a doubly-stochastic image of the eigenvalues.**
1. Expand $\rho$ in its eigenbasis inside $v_k$:
$$v_k=\langle\phi_k|\rho|\phi_k\rangle=\sum_i\lambda_i\,|\langle\phi_k|\psi_i\rangle|^2=\sum_i \underbrace{|\langle\phi_k|\psi_i\rangle|^2}_{=:D_{k,i}}\,\lambda_i,$$
i.e. $v=Dp$ with $D_{k,i}=|\langle\phi_k|\psi_i\rangle|^2$.

2. **$D$ is doubly stochastic.** Entries $\ge0$ obviously. Column sums:
$$\sum_k D_{k,i}=\sum_k|\langle\phi_k|\psi_i\rangle|^2=\langle\psi_i|\Big(\sum_k|\phi_k\rangle\langle\phi_k|\Big)|\psi_i\rangle=\langle\psi_i|I|\psi_i\rangle=1.$$
Row sums: identically, $\sum_i D_{k,i}=\langle\phi_k|(\sum_i|\psi_i\rangle\langle\psi_i|)|\phi_k\rangle=1$. So both sum to 1. ✓

**Lower bound.**
3. By [15](15-doubly-stochastic-never-decreases-entropy.md), $v=Dp$ with $D$ doubly stochastic gives $H(v)\ge H(p)$. Hence
$$H(O)=H(v)\ge H(p)=-\sum_i\lambda_i\log\lambda_i=H(\rho).$$

**Equality / the best basis.**
4. If $\{|\phi_k\rangle\}=\{|\psi_i\rangle\}$ (the eigenbasis), then $D_{k,i}=|\langle\psi_k|\psi_i\rangle|^2=\delta_{ki}$, so $D=I$, $v=p$, and $H(O)=H(\rho)$. The minimum is attained.

**Upper bound.**
5. $H(v)\le\log d$ always (max entropy of $d$ outcomes, [17](17-entropy-zero-and-maximal.md)), with equality for $v$ uniform — e.g. the Fourier basis ([10](10-fourier-is-the-worst-basis.md)). ∎

### 4. Where the magic happens
**The matrix of squared overlaps $D_{k,i}=|\langle\phi_k|\psi_i\rangle|^2$ is automatically doubly stochastic** (each row/column is the expansion of a unit vector in an orthonormal basis, which sums to 1). So *every* basis measurement is a doubly-stochastic blur of the eigenvalue distribution, and blurring only raises entropy. The eigenbasis is the one basis that doesn't blur ($D=I$). Memorize: **measurement entropy = $H(D\cdot\lambda)\ge H(\lambda)=H(\rho)$.**

### 5. If he pushes back
- *"Why is $-\text{Tr}\,\rho\log\rho=-\sum_i\lambda_i\log\lambda_i$?"* In the eigenbasis $\rho$ is diagonal with entries $\lambda_i$, so $\rho\log\rho$ is diagonal with entries $\lambda_i\log\lambda_i$, and the trace sums them.
- *"Is the minimizing basis unique?"* Up to degeneracy: if $\rho$ has distinct eigenvalues, the eigenbasis is essentially unique; with repeated eigenvalues you may rotate within an eigenspace and still hit $H(\rho)$.
- *"State the takeaway in one line."* The von Neumann entropy is the *intrinsic* uncertainty of $\rho$ — the floor over all measurement bases — and it equals the Shannon entropy of $\rho$'s eigenvalues.
- *"How does this connect to data processing / mixing?"* Same principle as [18](18-depolarizing-increases-entropy.md): doubly-stochastic operations (here, change of measurement basis) never reduce entropy.
