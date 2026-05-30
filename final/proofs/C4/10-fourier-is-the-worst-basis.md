# 10 — The Fourier basis is the "worst" basis: $H(O)=\log d$

**Claim.** Let $\rho=\sum_i\lambda_i|\psi_i\rangle\langle\psi_i|$ (eigenbasis $\{|\psi_i\rangle\}$). Measuring in the **Fourier basis**
$$|\phi_k\rangle=\frac{1}{\sqrt d}\sum_{i=1}^{d} e^{2\pi i\,ik/d}\,|\psi_i\rangle$$
gives $|\langle\phi_k|\psi_i\rangle|^2=\frac1d$ for all $i,k$, hence a uniform outcome distribution and the **maximal** entropy $H(O)=\log d$.

---

### 1. In plain words
The eigenbasis of $\rho$ is the basis in which $\rho$ is "most ordered" (diagonal). The Fourier basis is its polar opposite — *maximally tilted* relative to the eigenbasis: every Fourier vector has the same tiny overlap $1/d$ with every eigenvector. Measuring in such a basis throws away all structure: the outcomes come out perfectly uniform, so the entropy is as large as it can possibly be, $\log d$. This is the "worst basis" — it maximizes your uncertainty about the result.

### 2. Toolbox
- The Fourier vectors $\{|\phi_k\rangle\}$ are an **orthonormal basis** (discrete Fourier transform is unitary).
- $v_k=\langle\phi_k|\rho|\phi_k\rangle=\sum_i\lambda_i|\langle\phi_k|\psi_i\rangle|^2$ (expand $\rho$ in its eigenbasis).
- Shannon entropy of $d$ outcomes is maximized by the uniform distribution, value $\log d$ (see [17](17-entropy-zero-and-maximal.md)).
- For distinct eigenvalues of $O$, $H(O)=-\sum_k v_k\log v_k$ ([09](09-distinct-eigenvalues-entropy-independent.md)).

### 3. The proof
1. Compute the overlap of a Fourier vector with an eigenvector:
$$\langle\phi_k|\psi_j\rangle=\frac{1}{\sqrt d}\sum_i e^{-2\pi i\,ik/d}\langle\psi_i|\psi_j\rangle=\frac{1}{\sqrt d}e^{-2\pi i\,jk/d},$$
using orthonormality $\langle\psi_i|\psi_j\rangle=\delta_{ij}$ (only $i=j$ survives).
2. Therefore $|\langle\phi_k|\psi_j\rangle|^2=\dfrac{1}{d}$ — the modulus-squared kills the phase, leaving $1/d$ for **every** $j,k$.
3. The outcome probabilities:
$$v_k=\langle\phi_k|\rho|\phi_k\rangle=\sum_i\lambda_i|\langle\phi_k|\psi_i\rangle|^2=\sum_i\lambda_i\cdot\tfrac1d=\tfrac1d\underbrace{\sum_i\lambda_i}_{=1}=\tfrac1d.$$
(Used $\sum_i\lambda_i=\text{Tr}\,\rho=1$.) So the distribution is **uniform**, regardless of what $\rho$ was!
4. Hence $H(O)=-\sum_{k=1}^d\frac1d\log\frac1d=\log d$, the maximum value for $d$ outcomes. ∎

### 4. Where the magic happens
**The overlaps $|\langle\phi_k|\psi_i\rangle|^2$ are all equal to $1/d$ — the Fourier basis is "mutually unbiased" with the eigenbasis.** When you average $\rho$'s eigenvalues against a flat weight $1/d$, the eigenvalues completely wash out ($\frac1d\sum_i\lambda_i=\frac1d$), so you learn *nothing* about $\rho$ and the entropy maxes out. This is the worst-case companion to [11](11-von-neumann-entropy-is-the-minimum.md)'s best case.

### 5. If he pushes back
- *"Why is $\log d$ the maximum?"* Among all probability vectors on $d$ outcomes, uniform maximizes Shannon entropy; proof via $\log d - H(v)=D_{\mathrm{KL}}(v\,\|\,\text{uniform})\ge0$ (see [17](17-entropy-zero-and-maximal.md)).
- *"Is the Fourier basis literally the unique worst basis?"* Any basis *mutually unbiased* to the eigenbasis (all overlaps $1/d$) achieves $H=\log d$; Fourier is the standard explicit construction. They're all equally "worst."
- *"Connection to uncertainty relations?"* The eigenbasis and a Fourier/MUB basis are **complementary** observables — exactly the case where the Maassen–Uffink bound is maximal ([16](16-maassen-uffink-zero-and-maximal.md)).
- *"What if $O$'s eigenvalues are degenerate?"* Then outcomes merge and the entropy can only drop below $\log d$; the clean statement assumes a genuine basis measurement (distinct eigenvalues, [09](09-distinct-eigenvalues-entropy-independent.md)).
