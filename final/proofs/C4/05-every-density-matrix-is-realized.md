# 05 — Every density matrix is realized by some random state (and not uniquely)

**Claim.** If $\rho$ is Hermitian, PSD and unit-trace, then its eigenvalues $\lambda_i$ form a probability vector, so $\rho$ is the density matrix of the random state
$$|v\rangle\sim\begin{pmatrix}|\psi_1\rangle & |\psi_2\rangle & \cdots & |\psi_d\rangle\\ \lambda_1 & \lambda_2 & \cdots & \lambda_d\end{pmatrix},$$
where $\rho=\sum_i\lambda_i|\psi_i\rangle\langle\psi_i|$ is the spectral decomposition. Moreover the realization is **not unique**.

---

### 1. In plain words
[04](04-density-matrix-properties.md) showed every random state *gives* a density matrix. This is the converse: every density matrix *comes from* a random state. The trick is the **spectral theorem** — any Hermitian matrix is diagonal in some orthonormal eigenbasis. Reading off the diagonal, the entries are nonnegative (PSD) and sum to 1 (unit trace), i.e. exactly a probability distribution. So "$\rho$" literally *is* "pick eigenvector $|\psi_i\rangle$ with probability $\lambda_i$." Non-uniqueness: different recipes (different mixtures) can stir to the same $\rho$ — e.g. an unpolarized qubit is "half $|0\rangle$, half $|1\rangle$" *or* "half $|+\rangle$, half $|-\rangle$."

### 2. Toolbox
- **Spectral theorem:** a Hermitian $\rho$ can be written $\rho=\sum_i\lambda_i|\psi_i\rangle\langle\psi_i|$ with real $\lambda_i$ and orthonormal $\{|\psi_i\rangle\}$.
- $\rho\ge0 \Rightarrow$ eigenvalues $\ge 0$, because $\lambda_i=\langle\psi_i|\rho|\psi_i\rangle$.
- $\text{Tr}\,\rho=\sum_i\lambda_i$ (trace = sum of eigenvalues).

### 3. The proof

1. By the spectral theorem, $\rho=\sum_{i=1}^d \lambda_i|\psi_i\rangle\langle\psi_i|$ with $\{|\psi_i\rangle\}$ orthonormal and $\lambda_i\in\mathbb{R}$. (Hermitian ⇒ real eigenvalues, orthonormal eigenvectors.)
2. $\lambda_i=\langle\psi_i|\rho|\psi_i\rangle\ge0$ — apply $\rho\ge0$ (PSD) to the unit vector $|\psi_i\rangle$.
3. $\sum_i\lambda_i=\text{Tr}\,\rho=1$ — trace equals sum of eigenvalues, and $\rho$ is unit-trace.
4. Steps 2–3 say $(\lambda_1,\dots,\lambda_d)$ is a probability vector. So define the random state that takes value $|\psi_i\rangle$ with probability $\lambda_i$.
5. Its density matrix ([04](04-density-matrix-properties.md)) is $\sum_i\lambda_i|\psi_i\rangle\langle\psi_i|=\rho$. So $\rho$ is realized. ∎

**Non-uniqueness (worked example).** The maximally mixed qubit:
$$\tfrac12|0\rangle\langle0|+\tfrac12|1\rangle\langle1|=\tfrac12 I,\qquad \tfrac12|+\rangle\langle+|+\tfrac12|-\rangle\langle-|=\tfrac12\big(|+\rangle\langle+|+|-\rangle\langle-|\big)=\tfrac12 I.$$
Both equal $\tfrac12 I$ because $\{|0\rangle,|1\rangle\}$ and $\{|+\rangle,|-\rangle\}$ are each complete orthonormal bases ($\sum|\phi_k\rangle\langle\phi_k|=I$). So two physically different preparations (a coin-flip of computational states vs. a coin-flip of Hadamard states) have the **same** density matrix — and by [03](03-indistinguishable-iff-same-density-matrix.md) are physically indistinguishable.

### 4. Where the magic happens
**Spectral theorem turns "$\rho$ is a density matrix" into "the eigenvalues are a probability distribution."** Diagonalize, read the diagonal, done. The eigenbasis is the *canonical* random-state realization — but any decomposition $\rho=\sum_j q_j|\chi_j\rangle\langle\chi_j|$ (the $|\chi_j\rangle$ need not be orthogonal) works too, which is the source of non-uniqueness.

### 5. If he pushes back
- *"When is the realization unique?"* Essentially never for mixed states: as soon as $\rho$ has a repeated eigenvalue (e.g. $I/2$) you can rotate within that eigenspace; and you can also use non-orthogonal ensembles. (Pure states $\rho=|\psi\rangle\langle\psi|$ are "unique up to global phase.")
- *"How are two ensembles for the same $\rho$ related?"* By the **unitary freedom / HJW theorem**: $\{\sqrt{p_i}|\psi_i\rangle\}$ and $\{\sqrt{q_j}|\chi_j\rangle\}$ give the same $\rho$ iff related by an isometry. (Mention only if asked.)
- *"Does the eigen-realization minimize anything?"* Yes — it minimizes the measurement entropy; that's [11](11-von-neumann-entropy-is-the-minimum.md): the von Neumann entropy is $H(\lambda)$, the entropy of the eigenvalues.
