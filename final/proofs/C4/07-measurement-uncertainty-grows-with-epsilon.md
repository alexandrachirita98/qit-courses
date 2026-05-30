# 07 — Outcome distribution and entropy of a noisy state; entropy grows with $\epsilon$

**Claim.** Let $\rho=(1-\epsilon)|\psi\rangle\langle\psi|+\epsilon\frac{I}{d}$ and measure a basis observable $O=\sum_k\lambda_k|\phi_k\rangle\langle\phi_k|$ with $|\phi_1\rangle=|\psi\rangle$ (so the basis "contains" $|\psi\rangle$). Then the outcomes are distributed as
$$O\sim\begin{pmatrix}\lambda_1 & \lambda_2 & \cdots & \lambda_d\\[2pt] 1-\frac{d-1}{d}\epsilon & \frac\epsilon d & \cdots & \frac\epsilon d\end{pmatrix},$$
and the Shannon entropy
$$H(O)=h\!\Big(\tfrac{d-1}{d}\epsilon\Big)+\tfrac{d-1}{d}\epsilon\,\log(d-1)$$
**increases** with the error $\epsilon\in[0,1]$. (Here $h(x)=-x\log x-(1-x)\log(1-x)$ is the binary entropy.)

---

### 1. In plain words
Take a clean state $|\psi\rangle$ and contaminate it with a fraction $\epsilon$ of "white noise" $I/d$. Now measure in a basis that includes $|\psi\rangle$. With no noise you'd always land on $|\psi\rangle$ (zero uncertainty). The noise bleeds a little probability $\epsilon/d$ onto each of the other $d-1$ outcomes, so the result becomes less predictable. We compute the exact probabilities, plug into Shannon's entropy, and check that more noise ⇒ more uncertainty, monotonically, until at $\epsilon=1$ everything is uniform (maximal uncertainty).

### 2. Toolbox
- Outcome probability $=\langle\phi_k|\rho|\phi_k\rangle=\text{Tr}(\rho|\phi_k\rangle\langle\phi_k|)$ ([19](19-two-trace-identities.md)).
- $\langle\phi_k|\,\frac Id\,|\phi_k\rangle=\frac1d$; and $|\langle\psi|\phi_k\rangle|^2=\delta_{1k}$ (orthonormal basis with $|\phi_1\rangle=|\psi\rangle$).
- Linearity: $\langle\phi_k|\rho|\phi_k\rangle=(1-\epsilon)|\langle\psi|\phi_k\rangle|^2+\epsilon\frac1d$.

### 3. The proof

**The distribution.**
1. For the "correct" outcome ($k=1$):
$$\Pr[\lambda_1]=\langle\psi|\rho|\psi\rangle=(1-\epsilon)\underbrace{|\langle\psi|\psi\rangle|^2}_{1}+\epsilon\tfrac1d=1-\epsilon+\tfrac\epsilon d=1-\tfrac{d-1}{d}\epsilon.$$
2. For the other outcomes ($k\ge2$, orthogonal to $|\psi\rangle$):
$$\Pr[\lambda_k]=\langle\phi_k|\rho|\phi_k\rangle=(1-\epsilon)\underbrace{|\langle\psi|\phi_k\rangle|^2}_{0}+\epsilon\tfrac1d=\tfrac\epsilon d.$$
3. Sanity check: $\big(1-\frac{d-1}{d}\epsilon\big)+(d-1)\frac\epsilon d=1$. ✓

**The entropy.** Let $q:=\frac{d-1}{d}\epsilon$, so $\Pr[\lambda_1]=1-q$ and each of the $d-1$ small ones is $\frac\epsilon d=\frac{q}{d-1}$.
4. $\displaystyle H(O)=-(1-q)\log(1-q)-\sum_{k=2}^{d}\frac{q}{d-1}\log\frac{q}{d-1}$ — Shannon entropy definition.
5. The sum has $d-1$ equal terms: $-(d-1)\cdot\frac{q}{d-1}\log\frac{q}{d-1}=-q\log\frac{q}{d-1}=-q\log q+q\log(d-1)$.
6. So
$$H(O)=\underbrace{-(1-q)\log(1-q)-q\log q}_{=\,h(q)}+\,q\log(d-1)=h(q)+q\log(d-1).$$
Substituting $q=\frac{d-1}{d}\epsilon$ gives the claimed formula. ∎

**Monotone increasing in $\epsilon$.** Since $q$ is a positive multiple of $\epsilon$, monotonicity in $\epsilon$ = monotonicity in $q$.
7. $\dfrac{dH}{dq}=h'(q)+\log(d-1)=\log\dfrac{1-q}{q}+\log(d-1)=\log\dfrac{(d-1)(1-q)}{q}$, using $h'(q)=\log\frac{1-q}{q}$.
8. This is $\ge0$ exactly when $(d-1)(1-q)\ge q$, i.e. $q\le\frac{d-1}{d}$. But $\epsilon\in[0,1]$ means $q=\frac{d-1}{d}\epsilon\in[0,\frac{d-1}{d}]$ — *precisely* the range where the derivative is $\ge0$.
9. Hence $H(O)$ increases throughout $\epsilon\in[0,1]$, hitting its max $\log d$ at $\epsilon=1$ (where $1-q=\frac1d$ and the distribution is uniform). ∎

### 4. Where the magic happens
**Substitute $q=\frac{d-1}{d}\epsilon$ and the messy distribution collapses into "$(1-q)$ on one outcome, $q$ split evenly among $d-1$ others."** That's literally binary entropy $h(q)$ (clean vs. noise) plus $q\log(d-1)$ (which of the $d-1$ noisy slots). And the physical range $\epsilon\le1$ is exactly the range where this is increasing — noise never accidentally sharpens the distribution here.

### 5. If he pushes back
- *"Contrast with the variance — does that also increase monotonically?"* No! The **variance depends on the eigenvalue labels** and can be non-monotone in $\epsilon$ (see the $d=3$ example in [08](08-mean-and-variance-depend-on-eigenvalues.md)). Entropy is the well-behaved uncertainty measure because it ignores the labels ([09](09-distinct-eigenvalues-entropy-independent.md)).
- *"Why measure in a basis containing $|\psi\rangle$?"* It's the most favorable basis (it would be perfect at $\epsilon=0$), isolating the pure effect of the noise. Any other basis only adds more uncertainty.
- *"What is $H(O)$ at $\epsilon=0$ and $\epsilon=1$?"* $0$ (certain outcome $\lambda_1$) and $\log d$ (uniform), respectively.
- *"Is this $H(O)$ the von Neumann entropy of $\rho$?"* Only here, because this basis happens to be the eigenbasis of $\rho$ (it's $|\psi\rangle$ plus orthogonal complement). In general $H(O)\ge H(\rho)$, see [11](11-von-neumann-entropy-is-the-minimum.md).
