# 05 — Choi matrix PSD ⇒ a Kraus representation exists

**Claim.** If $J_{\mathcal E}\ge0$, then $\mathcal E$ has a Kraus representation $\mathcal E(\rho)=\sum_{k}K_k\rho K_k^\dagger$. Explicitly, with the spectral decomposition $J_{\mathcal E}=\sum_k\lambda_k|\psi_k\rangle\langle\psi_k|$ and $|\psi_k'\rangle:=\sqrt{\lambda_k}\,|\psi_k\rangle$,
$$K_k=\sqrt d\sum_{a=0}^{d-1}\big(\langle a|\otimes I_{d'}\big)|\psi_k'\rangle\,\langle a|.$$

---

### 1. In plain words
The Choi matrix stores the whole map. If it's PSD, diagonalize it; each (scaled) eigenvector becomes a Kraus operator. Reshaping a vector in $\mathbb C^d\otimes\mathbb C^{d'}$ into a $d'\times d$ matrix is the standard "vectorization" trick. Once we have Kraus operators, [03](03-kraus-implies-cp.md) tells us $\mathcal E$ is automatically CP — closing the loop.

### 2. Toolbox
- **Recovery formula:** $\mathcal E(|i\rangle\langle j|)=d\,(\langle i|\otimes I_{d'})\,J_{\mathcal E}\,(|j\rangle\otimes I_{d'})$ (invert the Choi definition; see [04](04-d-positive-implies-choi-psd.md)).
- $J_{\mathcal E}\ge0\Rightarrow J_{\mathcal E}=\sum_k|\psi_k'\rangle\langle\psi_k'|$ with $|\psi_k'\rangle=\sqrt{\lambda_k}|\psi_k\rangle$ (absorb eigenvalues; $\lambda_k\ge0$).
- $\mathcal E(\rho)=\sum_{i,j}\langle i|\rho|j\rangle\,\mathcal E(|i\rangle\langle j|)$ (linearity in the input).

### 3. The proof
1. **PSD ⇒ sum of rank-ones.** $J_{\mathcal E}=\sum_k\lambda_k|\psi_k\rangle\langle\psi_k|=\sum_k|\psi_k'\rangle\langle\psi_k'|$ with $|\psi_k'\rangle=\sqrt{\lambda_k}|\psi_k\rangle$ (uses $\lambda_k\ge0$).
2. **Apply the recovery formula** and substitute:
$$\mathcal E(|i\rangle\langle j|)=d(\langle i|\otimes I)J_{\mathcal E}(|j\rangle\otimes I)=\sum_k\underbrace{\sqrt d(\langle i|\otimes I)|\psi_k'\rangle}_{=:K_k|i\rangle}\ \underbrace{\big(\sqrt d(\langle j|\otimes I)|\psi_k'\rangle\big)^\dagger}_{=\langle j|K_k^\dagger}.$$
3. **Read off the Kraus operator.** Define $K_k=\sqrt d\sum_a(\langle a|\otimes I)|\psi_k'\rangle\langle a|$, a $d'\times d$ matrix. Then $K_k|i\rangle=\sqrt d(\langle i|\otimes I)|\psi_k'\rangle$, matching step 2:
$$\mathcal E(|i\rangle\langle j|)=\sum_k K_k|i\rangle\langle j|K_k^\dagger.$$
4. **Extend by linearity** to all $\rho$:
$$\mathcal E(\rho)=\sum_{i,j}\langle i|\rho|j\rangle\,\mathcal E(|i\rangle\langle j|)=\sum_k K_k\Big(\sum_{i,j}\langle i|\rho|j\rangle\,|i\rangle\langle j|\Big)K_k^\dagger=\sum_k K_k\rho K_k^\dagger.$$
5. By [03](03-kraus-implies-cp.md), a map of this form is completely positive. ∎

### 4. Where the magic happens
**Diagonalizing the (PSD) Choi matrix turns each eigenvector into a Kraus operator** via vectorization: a vector $|\psi_k'\rangle\in\mathbb C^d\otimes\mathbb C^{d'}$ is "unstacked" into the matrix $K_k$. The number of Kraus operators = number of nonzero eigenvalues = $\text{rank}\,J_{\mathcal E}$ (the minimum possible).

### 5. If he pushes back
- *"Why is the recovery formula true?"* From $J_{\mathcal E}=\frac1d\sum_{i,j}|i\rangle\langle j|\otimes\mathcal E(|i\rangle\langle j|)$, sandwich with $\langle i|\otimes I$ and $|j\rangle\otimes I$: only the $(i,j)$ block survives, leaving $\frac1d\mathcal E(|i\rangle\langle j|)$; multiply by $d$.
- *"Is the Kraus rep unique?"* No — eigenbasis choice and any isometry mixing the $K_k$ give other valid reps. The *minimal* size $\text{rank}\,J_{\mathcal E}$ is invariant.
- *"What if I want a trace-preserving channel?"* Then additionally $\sum_k K_k^\dagger K_k=I$, equivalent to $\text{Tr}_{d'}J_{\mathcal E}=I_d/d$ — see [07](07-kraus-theorem-trace-preserving.md).
