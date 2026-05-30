# 16 — When the Maassen–Uffink bound is zero (shared eigenvector) vs. maximal (complementary)

**Claim.** The MU lower bound $B=-\log\max_{k,j}|\langle\phi_k|\xi_j\rangle|^2$ for two bases $\{|\phi_k\rangle\}$, $\{|\xi_j\rangle\}$ of $\mathbb{C}^d$ satisfies $0\le B\le\log d$, and:
- $B=0$ **iff the two bases share a common eigenvector** ($|\phi_k\rangle=e^{i\theta}|\xi_j\rangle$ for some $k,j$).
- $B=\log d$ (maximal) **iff the bases are complementary** — every overlap equals $1/d$ (mutually unbiased bases, MUBs), e.g. eigenbases of distinct Pauli strings like $X\otimes Z\otimes Y$.

---

### 1. In plain words
The MU bound measures *how incompatible* two measurements are.
- If they share even one eigenvector, there's a state ($=$ that shared vector) on which **both** measurements are perfectly certain — no joint uncertainty is forced, so the bound is $0$.
- The most incompatible case is when the two bases are "maximally tilted": each vector of one basis is an equal-weight blend of all vectors of the other (overlap $1/d$ everywhere). Then knowing one perfectly tells you *nothing* about the other, and the bound is as large as possible, $\log d$.

### 2. Toolbox
- $|\langle\phi_k|\xi_j\rangle|\le1$ for unit vectors (Cauchy–Schwarz), $=1$ iff parallel (equal up to phase).
- For each fixed $j$: $\sum_{k}|\langle\phi_k|\xi_j\rangle|^2=\langle\xi_j|\big(\sum_k|\phi_k\rangle\langle\phi_k|\big)|\xi_j\rangle=1$ (completeness).
- $\max\ge\text{average}$: the max of $d$ nonnegative numbers summing to 1 is $\ge\frac1d$, with equality iff all equal $\frac1d$.
- $-\log$ is decreasing: larger overlap ⇒ smaller bound.

### 3. The proof

Let $m:=\max_{k,j}|\langle\phi_k|\xi_j\rangle|^2$, so $B=-\log m$.

**Range $0\le B\le\log d$.**
1. Fix any $j$. The $d$ numbers $|\langle\phi_k|\xi_j\rangle|^2$ are $\ge0$ and sum to $1$, so their max is $\ge\frac1d$. Taking the overall max, $m\ge\frac1d$.
2. Also $m\le1$ (Cauchy–Schwarz). Hence $\frac1d\le m\le1$, and applying the decreasing $-\log$: $0\le-\log m\le\log d$, i.e. $0\le B\le\log d$. ✓

**$B=0$ iff a shared eigenvector.**
3. $B=0\iff m=1\iff$ some $|\langle\phi_k|\xi_j\rangle|^2=1\iff$ (Cauchy–Schwarz equality) $|\phi_k\rangle=e^{i\theta}|\xi_j\rangle$ — a common eigenvector. 
4. *Why the bound is then achievable:* prepare the state $|\psi\rangle=|\phi_k\rangle=e^{i\theta}|\xi_j\rangle$. Measuring $O$ gives outcome $k$ with certainty ($H(O)=0$); measuring $O'$ gives outcome $j$ with certainty ($H(O')=0$). So $H(O)+H(O')=0=B$. No uncertainty is forced. ∎

**$B=\log d$ iff complementary (MUB).**
5. $B=\log d\iff m=\frac1d$. By Step 1, $m=\frac1d$ forces, for **every** $j$, *all* of $|\langle\phi_k|\xi_j\rangle|^2$ to equal $\frac1d$ (the max equals the average only when all terms are equal). That's the definition of **mutually unbiased bases**.
6. Conversely, if all overlaps are $\frac1d$ then $m=\frac1d$ and $B=\log d$. ∎

**Example (qubit, $d=2$).** $Z$-eigenbasis $\{|0\rangle,|1\rangle\}$ and $X$-eigenbasis $\{|+\rangle,|-\rangle\}$: every overlap $|\langle0|+\rangle|^2=\dots=\frac12$, so $B=-\log\frac12=1$ bit, i.e. $H(Z)+H(X)\ge1$. For $n$ qubits, eigenbases of two Pauli strings that differ in every tensor slot (e.g. $X\otimes Z\otimes Y$ vs $Z\otimes X\otimes X$) are MUBs with $m=\frac1{2^n}=\frac1d$, giving $B=\log d=n$ bits.

### 4. Where the magic happens
**"Max overlap $=1$" ⇔ shared vector (Cauchy–Schwarz), and "max overlap $=\frac1d$" ⇔ all overlaps equal (max meets average).** The single fact $\sum_k|\langle\phi_k|\xi_j\rangle|^2=1$ (completeness) pins the overlaps between $\frac1d$ and $1$, and the two extremes are exactly the trivial (commuting) and maximally-complementary cases.

### 5. If he pushes back
- *"Does $B=0$ mean the observables commute?"* They share an eigenvector, so they have a common eigenbasis on at least a 1-D subspace; the certainty state lives there. Fully commuting observables share a *complete* eigenbasis and $B=0$ via that.
- *"Why do complementary observables matter?"* They give the tightest uncertainty (hardest to predict both), which is exactly what you want for **provable QKD security** — the eavesdropper can't know both bases. (This is the C4 → C6 BB84 link.)
- *"Is $B$ tight?"* Maassen–Uffink is not always tight (the Berta et al. version with quantum memory improves it, C6), but the endpoints here ($B=0$ and the MUB case) are achievable.
- *"Connection to the Fourier 'worst basis'?"* The Fourier basis is mutually unbiased with the eigenbasis — same MUB condition, overlaps $1/d$ ([10](10-fourier-is-the-worst-basis.md)).
