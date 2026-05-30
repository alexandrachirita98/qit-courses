# 09 — With distinct eigenvalues, measurement entropy ignores the eigenvalues

**Claim.** If $O=\sum_{k=1}^d\lambda_k|\phi_k\rangle\langle\phi_k|$ has **distinct** eigenvalues, then
$$H(O)=-\sum_{k=1}^d \langle\phi_k|\rho|\phi_k\rangle\,\log\langle\phi_k|\rho|\phi_k\rangle$$
depends only on the **basis** $\{|\phi_k\rangle\}$, not on the values $\lambda_k$. (It does still depend on the basis.)

---

### 1. In plain words
Shannon entropy measures *how spread out* the outcome probabilities are — not *what the outcomes are called*. The mean and variance ([08](08-mean-and-variance-depend-on-eigenvalues.md)) care about the labels $\lambda_k$; entropy does not. The only role the eigenvalues play in a measurement is to decide *which outcomes are lumped together*: equal eigenvalues merge into one outcome. If all eigenvalues are distinct, nothing merges, each eigenvector is its own outcome with probability $\langle\phi_k|\rho|\phi_k\rangle$, and the entropy is a function of those probabilities alone.

### 2. Toolbox
- Outcome $\lambda$ has projector $E_\lambda=\sum_{k:\lambda_k=\lambda}|\phi_k\rangle\langle\phi_k|$ and probability $\Pr[\lambda]=\text{Tr}(\rho E_\lambda)=\sum_{k:\lambda_k=\lambda}\langle\phi_k|\rho|\phi_k\rangle$.
- Shannon entropy is indexed by **distinct** outcome values: $H(O)=-\sum_\lambda\Pr[\lambda]\log\Pr[\lambda]$.
- Write $v_k:=\langle\phi_k|\rho|\phi_k\rangle\ge0$, $\sum_k v_k=1$ ([19](19-two-trace-identities.md), [04](04-density-matrix-properties.md)).

### 3. The proof
1. By definition $H(O)=-\sum_\lambda\Pr[\lambda]\log\Pr[\lambda]$, the sum running over **distinct eigenvalues** $\lambda$.
2. **Distinct eigenvalues** means each $\lambda$ is hit by exactly one index $k$, so $E_\lambda=|\phi_k\rangle\langle\phi_k|$ and $\Pr[\lambda]=\langle\phi_k|\rho|\phi_k\rangle=v_k$.
3. The map $\lambda\mapsto k$ is then a bijection, so the sum over $\lambda$ is just a sum over $k$:
$$H(O)=-\sum_{k=1}^d v_k\log v_k.$$
4. The right-hand side contains only the probabilities $v_k=\langle\phi_k|\rho|\phi_k\rangle$ — **no $\lambda_k$ appears**. Replace $\lambda_k$ by any other distinct values and $H(O)$ is unchanged. ∎

**Why "distinct" matters (degenerate case).** If, say, $\lambda_1=\lambda_2$, those two eigenvectors share one outcome with probability $v_1+v_2$, and
$$H=-(v_1+v_2)\log(v_1+v_2)-\sum_{k\ge3}v_k\log v_k\ \ne\ -\sum_k v_k\log v_k$$
in general. Merging outcomes *lowers* the entropy (grouping is a coarse-graining). This is the difference between a **basis (von Neumann) measurement** (distinct eigenvalues, full information) and a **partial measurement** (repeated eigenvalues), which leaves post-measurement superpositions.

### 4. Where the magic happens
**Eigenvalues only decide the bucketing of outcomes; with distinct eigenvalues every eigenvector is its own bucket, so $H(O)$ is a function of the probabilities $\langle\phi_k|\rho|\phi_k\rangle$ alone.** That's why entropy is the *honest* uncertainty measure for non-numeric outcomes, while mean/variance are not.

### 5. If he pushes back
- *"But $H(O)$ still depends on the basis $\{|\phi_k\rangle\}$, right?"* Yes — different bases give different $v_k$, hence different entropy. The eigenvalue-independence is only about the *labels*, not the *directions*. The basis dependence is what the next results explore: worst basis = Fourier ([10](10-fourier-is-the-worst-basis.md)), best basis = eigenbasis of $\rho$ ([11](11-von-neumann-entropy-is-the-minimum.md)).
- *"Does merging outcomes always reduce entropy?"* Yes: grouping $\{p,q\}$ into $p+q$ satisfies $-(p+q)\log(p+q)\le -p\log p-q\log q$ (entropy is subadditive under merging). A partial measurement extracts less information.
- *"Give the cleanest one-line statement."* For a von Neumann (distinct-eigenvalue) measurement, $H(O)=H\big(\langle\phi_k|\rho|\phi_k\rangle\big)$ — the Shannon entropy of the diagonal of $\rho$ in the $\{|\phi_k\rangle\}$ basis.
