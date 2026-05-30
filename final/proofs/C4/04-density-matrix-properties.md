# 04 — A density matrix is Hermitian, positive semi-definite, and unit-trace

**Claim.** The matrix representation of a random quantum state
$$\rho=\sum_{|\psi\rangle}\Pr[v=|\psi\rangle]\,|\psi\rangle\langle\psi|$$
satisfies $\rho^\dagger=\rho$ (Hermitian), $\langle\phi|\rho|\phi\rangle\ge0\ \forall|\phi\rangle$ (positive semi-definite, PSD), and $\text{Tr}\,\rho=1$ (unit-trace). These three properties are the **definition** of a density matrix.

---

### 1. In plain words
A "random quantum state" is just: with some probability you hold $|\psi_1\rangle$, with another probability $|\psi_2\rangle$, etc. Its density matrix is the probability-weighted average of the projectors $|\psi_i\rangle\langle\psi_i|$. We want to show this average always lands in a special class of matrices ("density matrices"). The three properties say, intuitively:
- **Hermitian** = it represents a real, physical observable-like object (real measurement statistics).
- **PSD** = every probability it predicts is $\ge 0$ (no negative probabilities).
- **Unit trace** = the probabilities of a complete measurement add to $1$.

### 2. Toolbox
- Each $|\psi\rangle$ is a **unit** vector: $\langle\psi|\psi\rangle=1$.
- A projector satisfies $(|\psi\rangle\langle\psi|)^\dagger=|\psi\rangle\langle\psi|$.
- The weights $p_{|\psi\rangle}:=\Pr[v=|\psi\rangle]$ are **real**, $\ge0$, and **sum to 1**.
- $\text{Tr}\,|\psi\rangle\langle\psi|=\langle\psi|\psi\rangle$ (the scalar-trace move, [19](19-two-trace-identities.md)).
- $(A+B)^\dagger=A^\dagger+B^\dagger$ and $(cA)^\dagger=\bar c\,A^\dagger$.

### 3. The proof

Write $\rho=\sum_i p_i\,|\psi_i\rangle\langle\psi_i|$ with $p_i\ge0$, $\sum_i p_i=1$.

**Hermitian.**
1. $\rho^\dagger=\Big(\sum_i p_i|\psi_i\rangle\langle\psi_i|\Big)^\dagger=\sum_i \bar p_i\,(|\psi_i\rangle\langle\psi_i|)^\dagger$ — dagger distributes over the sum and conjugates the scalar.
2. $=\sum_i p_i\,|\psi_i\rangle\langle\psi_i|=\rho$ — because $p_i$ is real ($\bar p_i=p_i$) and the projector is self-adjoint. ∎

**Positive semi-definite.** Take any vector $|\phi\rangle$:
3. $\langle\phi|\rho|\phi\rangle=\sum_i p_i\,\langle\phi|\psi_i\rangle\langle\psi_i|\phi\rangle=\sum_i p_i\,|\langle\psi_i|\phi\rangle|^2$ — used $\langle\phi|\psi_i\rangle\langle\psi_i|\phi\rangle=|\langle\psi_i|\phi\rangle|^2$.
4. Each term is $(\ge0)\cdot(\ge0)\ge0$, so the sum is $\ge0$. Hence $\rho\ge0$. ∎

**Unit trace.**
5. $\text{Tr}\,\rho=\sum_i p_i\,\text{Tr}|\psi_i\rangle\langle\psi_i|$ — trace is linear.
6. $=\sum_i p_i\,\langle\psi_i|\psi_i\rangle=\sum_i p_i\cdot1=\sum_i p_i$ — scalar-trace move + unit vectors.
7. $=1$ — the probabilities sum to 1. ∎

### 4. Where the magic happens
Each property of $\rho$ is *inherited* from a property of the building blocks:
**real weights → Hermitian**, **probabilities & moduli-squared are nonnegative → PSD**, **probabilities sum to 1 → unit trace**. There's nothing quantum-mysterious; it's "average of projectors with a probability vector."

### 5. If he pushes back
- *"Is the converse true — is every Hermitian/PSD/unit-trace matrix a density matrix of some random state?"* Yes — that's the next result, [05](05-every-density-matrix-is-realized.md), via the spectral decomposition.
- *"Why PSD and not just positive eigenvalues?"* PSD ($\langle\phi|\rho|\phi\rangle\ge0\,\forall\phi$) is *equivalent* to "Hermitian with eigenvalues $\ge0$." The eigenvalues are the realizable probabilities.
- *"Can $\rho$ have an eigenvalue $>1$?"* No: eigenvalues are $\ge0$ and sum (the trace) is $1$, so each is in $[0,1]$.
- *"What's special about pure states here?"* $\rho=|\psi\rangle\langle\psi|$ is the special case of one outcome with probability 1; it also satisfies $\rho^2=\rho$ (it's a projector). Mixed states have $\rho^2\ne\rho$.
