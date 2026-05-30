# 18 — The depolarizing channel never decreases von Neumann entropy

**Claim.** For the depolarizing channel $\Delta_\epsilon(\rho)=(1-\epsilon)\rho+\epsilon\,\dfrac{I}{d}$ with $\epsilon\in[0,1]$,
$$H\big(\Delta_\epsilon(\rho)\big)\ \ge\ H(\rho).$$
Adding white noise can only raise (or keep) the entropy.

---

### 1. In plain words
$\Delta_\epsilon$ pushes any state a fraction $\epsilon$ of the way toward the maximally mixed state $I/d$ (total ignorance). Moving toward "total ignorance" can't make you more certain, so the entropy can't go down. We can prove this cleanly and self-contained: in $\rho$'s own eigenbasis, $\Delta_\epsilon$ acts on the eigenvalue vector as a **doubly-stochastic** matrix (mix-with-uniform), and doubly-stochastic maps never decrease Shannon entropy ([15](15-doubly-stochastic-never-decreases-entropy.md)).

### 2. Toolbox
- $H(\rho)=H(\lambda)$, the Shannon entropy of $\rho$'s eigenvalues ([11](11-von-neumann-entropy-is-the-minimum.md)).
- A doubly-stochastic matrix $D$ with $v=D\lambda$ gives $H(v)\ge H(\lambda)$ ([15](15-doubly-stochastic-never-decreases-entropy.md)).
- $J$ = the all-ones $d\times d$ matrix; $J\lambda=(\sum_i\lambda_i)\mathbf{1}=\mathbf{1}$ when $\lambda$ is a probability vector.
- $\rho$ and $I/d$ are **simultaneously diagonalizable** (the identity is diagonal in *every* basis).

### 3. The proof

1. Diagonalize $\rho=\sum_i\lambda_i|\psi_i\rangle\langle\psi_i|$. In this eigenbasis $I/d$ is also diagonal (entries $1/d$), so $\Delta_\epsilon(\rho)$ is diagonal too, with eigenvalues
$$\mu_i=(1-\epsilon)\lambda_i+\epsilon\tfrac1d.$$
Hence $H\big(\Delta_\epsilon(\rho)\big)=H(\mu)$, the Shannon entropy of the vector $\mu=(\mu_i)$.

2. Write $\mu$ as a matrix acting on $\lambda$. With $D:=(1-\epsilon)I+\dfrac{\epsilon}{d}J$,
$$D\lambda=(1-\epsilon)\lambda+\tfrac{\epsilon}{d}J\lambda=(1-\epsilon)\lambda+\tfrac{\epsilon}{d}\mathbf{1}=\mu.$$
(Used $J\lambda=\mathbf 1$ since $\sum_i\lambda_i=1$, and $\frac1d\mathbf1$ has all entries $\frac1d$.)

3. **$D$ is doubly stochastic:**
 - entries $\ge0$ for $\epsilon\in[0,1]$ (diagonal $1-\epsilon+\frac\epsilon d\ge0$, off-diagonal $\frac\epsilon d\ge0$);
 - each row sums to $(1-\epsilon)\cdot1+\frac\epsilon d\cdot d=1-\epsilon+\epsilon=1$; by symmetry each column too.

4. Apply [15](15-doubly-stochastic-never-decreases-entropy.md): $\mu=D\lambda$ with $D$ doubly stochastic $\Rightarrow H(\mu)\ge H(\lambda)$. Therefore
$$H\big(\Delta_\epsilon(\rho)\big)=H(\mu)\ge H(\lambda)=H(\rho).\qquad\blacksquare$$

### 4. Where the magic happens
**Because $I/d$ is diagonal in every basis, $\Delta_\epsilon$ is purely classical on $\rho$'s eigenvalues** — it's the doubly-stochastic "blend with uniform" matrix $D=(1-\epsilon)I+\frac\epsilon d J$. No operator-concavity machinery needed; the quantum problem collapses to the classical lemma [15](15-doubly-stochastic-never-decreases-entropy.md). The whole content is "mixing with uniform = a doubly-stochastic blur."

### 5. If he pushes back
- *"Can't you just say von Neumann entropy is concave?"* Yes: $H\big((1-\epsilon)\rho+\epsilon\frac Id\big)\ge(1-\epsilon)H(\rho)+\epsilon\log d\ge H(\rho)$ since $\log d\ge H(\rho)$ ([17](17-entropy-zero-and-maximal.md)). But concavity of $H$ is itself a theorem; the doubly-stochastic route proves it from scratch for this channel.
- *"Is $\Delta_\epsilon$ entropy-increasing because it's *bistochastic*?"* Exactly — $\Delta_\epsilon$ is a unital channel ($\Delta_\epsilon(I)=I$), and unital/bistochastic channels never decrease von Neumann entropy. C6 proves the general statement; this is the concrete C4 instance.
- *"When is the entropy unchanged?"* At $\epsilon=0$ (no noise), or if $\rho=I/d$ already (then $\mu=\lambda$). Strictly increasing otherwise for $\epsilon\in(0,1)$ unless $\rho$ is already maximally mixed.
- *"Does this contradict the variance being non-monotone ([08](08-mean-and-variance-depend-on-eigenvalues.md))?"* No — entropy is the well-behaved (monotone) measure; variance depends on arbitrary labels and need not be monotone.
