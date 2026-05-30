# 10 — Schmidt decomposition & entropy of entanglement

**Claim.** Every pure bipartite state $|\psi\rangle\in\mathbb C^d\otimes\mathbb C^{d'}$ can be written
$$|\psi\rangle=\sum_{k=0}^{r-1}s_k\,|\phi_k\rangle\otimes|\xi_k\rangle,\qquad s_k>0,\ \{|\phi_k\rangle\},\{|\xi_k\rangle\}\text{ orthonormal},$$
where $r=$ Schmidt rank. The reduced states $\rho_A=\sum_k s_k^2|\phi_k\rangle\langle\phi_k|$ and $\rho_B=\sum_k s_k^2|\xi_k\rangle\langle\xi_k|$ share the **same** nonzero eigenvalues $s_k^2$, so $H(\rho_A)=H(\rho_B)=:$ the **entropy of entanglement**.

---

### 1. In plain words
Any pure state of two systems can be lined up so that Alice's basis vector $|\phi_k\rangle$ is perfectly paired with Bob's $|\xi_k\rangle$, with a single positive weight $s_k$ each. This is just the singular value decomposition (SVD) of the coefficient matrix. The immediate payoff: both halves of a pure entangled state have *identical* entropy spectra, so their entropy is a basis-independent measure of how entangled $|\psi\rangle$ is.

### 2. Toolbox
- **SVD:** any matrix $M=USV^\dagger=\sum_k|u_k\rangle s_k\langle v_k|$ with orthonormal $\{|u_k\rangle\},\{|v_k\rangle\}$ and $s_k\ge0$.
- Coefficient matrix: $|\psi\rangle=\sum_{i,j}\alpha_{ij}|i\rangle|j\rangle$, $M=(\alpha_{ij})$.
- Reduced state $\rho_A=\text{Tr}_B|\psi\rangle\langle\psi|$.

### 3. The proof
1. Collect coefficients into the matrix $M$ with $\alpha_{ij}=\langle i|M|j\rangle$, and take its SVD: $M=\sum_k|\phi_k\rangle s_k\langle\xi_k|$ (writing the singular vectors as $|\phi_k\rangle\in\mathbb C^d$, $|\xi_k\rangle\in\mathbb C^{d'}$).
2. Then $\alpha_{ij}=\sum_k\langle i|\phi_k\rangle s_k\langle\xi_k|j\rangle$, so
$$|\psi\rangle=\sum_{i,j}\alpha_{ij}|i\rangle|j\rangle=\sum_k s_k\Big(\sum_i\langle i|\phi_k\rangle|i\rangle\Big)\otimes\Big(\sum_j\langle\xi_k|j\rangle^*|j\rangle\Big)... =\sum_k s_k|\phi_k\rangle\otimes|\xi_k\rangle.$$
(The singular vectors regroup into the kets $|\phi_k\rangle,|\xi_k\rangle$; this is the Schmidt form.)
3. **Reduced states.** Trace out $B$ (orthonormality $\langle\xi_k|\xi_l\rangle=\delta_{kl}$):
$$\rho_A=\text{Tr}_B|\psi\rangle\langle\psi|=\sum_{k,l}s_ks_l|\phi_k\rangle\langle\phi_l|\,\langle\xi_l|\xi_k\rangle=\sum_k s_k^2|\phi_k\rangle\langle\phi_k|.$$
Symmetrically $\rho_B=\sum_k s_k^2|\xi_k\rangle\langle\xi_k|$.
4. Both have eigenvalues $\{s_k^2\}$, so $H(\rho_A)=-\sum_k s_k^2\log s_k^2=H(\rho_B)$. ∎

### 4. Where the magic happens
**The Schmidt decomposition is just the SVD of the coefficient matrix**, and SVD gives the *same* singular values $s_k$ to both sides. Since $\rho_A$ and $\rho_B$ get eigenvalues $s_k^2$ from the same SVD, their entropies must coincide — a pure state is "equally entangled from both ends."

### 5. If he pushes back
- *"Schmidt rank = 1 means?"* Product (separable) state, $|\psi\rangle=|\phi\rangle|\xi\rangle$, entanglement entropy 0. Rank $>1$ ⇒ entangled.
- *"Connect to conditional entropy."* For pure $|\psi\rangle$: $H(\rho_{AB})=0$, so $H(A|B)=-H(\rho_B)=-H(\rho_A)\le0$ — zero iff separable, negative otherwise ([09](09-conditional-von-neumann-entropy.md)).
- *"Maximally entangled state?"* All $s_k^2=1/d$ ⇒ $\rho_A=\rho_B=I/d$, entanglement entropy $\log d$ (the max).
- *"Is the decomposition unique?"* The $s_k$ are unique (singular values); the vectors are unique up to phases/degeneracy.
