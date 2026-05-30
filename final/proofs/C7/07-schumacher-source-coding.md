# 07 — Schumacher's source coding theorem: $\min R=H(\rho)$

**Claim.** To compress $n$ i.i.d. copies of a source with density matrix $\rho$ into $m=nR+o(n)$ qubits and decompress with vanishing error ($\pi_n\to0$), the minimal achievable rate is
$$\min R=H(\rho)\quad(\text{von Neumann entropy}).$$

---

### 1. In plain words
The quantum analogue of Shannon's source coding theorem. A stream of identical quantum states can be squeezed to $H(\rho)$ qubits per state — no fewer (else you'd beat the Holevo bound), no more needed. The achievability uses a **typical subspace**: although $\rho^{\otimes n}$ lives in a huge $d^n$-dimensional space, almost all of its weight sits in a subspace of dimension $\approx 2^{nH(\rho)}$. Project onto that subspace and map it isometrically into $nH(\rho)$ qubits.

### 2. Toolbox
- Compression scheme $(\mathcal E,\mathcal D)$ with $\mathcal E:\mathcal B(\mathcal H^{\otimes n})\to\mathcal B((\mathbb C^2)^{\otimes m})$, $\mathcal D$ the reverse; success $F(\rho^{\otimes n},\mathcal D\circ\mathcal E)\ge1-\pi$.
- $\rho=\sum_i p_i|\psi_i\rangle\langle\psi_i|$ ⇒ $\rho^{\otimes n}=\sum_{i_1,\dots,i_n}p_{i_1}\cdots p_{i_n}|\psi_{i_1}\rangle\langle\psi_{i_1}|\otimes\cdots$.
- **Typical set** $I$ of index strings $(i_1,\dots,i_n)$: those with empirical frequencies near $p$; by the AEP, $\text{Tr}(P\rho^{\otimes n})\ge1-\pi$ where $P=\sum_{i\in I}|\psi_{i_1}\rangle\langle\psi_{i_1}|\otimes\cdots$, and $|I|\le 2^{n(H(\rho)+C\epsilon)}$.
- Holevo bound ([../C6/08](../C6/08-holevo-theorem.md)) for the converse.

### 3. The proof

**Achievability ($R=H(\rho)$ works).**
1. Diagonalize: $\rho^{\otimes n}$ has eigenvectors $|\psi_{i_1}\rangle\otimes\cdots\otimes|\psi_{i_n}\rangle$ with eigenvalues $p_{i_1}\cdots p_{i_n}$ — a classical i.i.d. distribution over index strings.
2. Let $I$ be the set of $\epsilon$-typical index strings and $P=\sum_{i\in I}|\psi_{i_1}\cdots\psi_{i_n}\rangle\langle\cdots|$ the typical-subspace projector. By the classical AEP (Shannon), $\text{Tr}(P\rho^{\otimes n})\ge1-\pi$ and $\dim(\text{typical subspace})=|I|\le 2^{n(H(\rho)+C\epsilon)}$.
3. **Encoder:** an isometry mapping the typical subspace into $m=n(H(\rho)+C\epsilon)$ qubits (enough room since $2^m\ge|I|$); discard the rest. **Decoder:** the reverse isometry.
4. Because almost all of $\rho^{\otimes n}$'s weight is inside the typical subspace, the entanglement fidelity satisfies $F(\rho^{\otimes n},\mathcal D\circ\mathcal E)\ge1-\pi$. So $R=H(\rho)+C\epsilon$ is achievable; let $\epsilon\to0$. ∎ (achievability)

**Converse ($R<H(\rho)$ impossible).**
5. Suppose $R<H(\rho)$, i.e. $m<nH(\rho)$ qubits. The compressed system can carry at most $m$ qubits of quantum information; decompressing to high fidelity would let one transmit $\approx nH(\rho)$ qubits' worth of distinguishable signals through an $m<nH(\rho)$-qubit channel, **violating the Holevo bound** (accessible info $\le m<nH(\rho)$). Contradiction. So $\min R\ge H(\rho)$. ∎ (converse)

Combining, $\min R=H(\rho)$.

### 4. Where the magic happens
**The typical subspace:** $\rho^{\otimes n}$ concentrates onto $\sim2^{nH(\rho)}$ dimensions out of $d^n$, just as a typical bit-string set has size $2^{nH}$ classically. Compressing = an isometry onto that subspace. The converse is "you can't fit $nH(\rho)$ qubits of information into fewer qubits" — Holevo.

### 5. If he pushes back
- *"Why $H(\rho)$ and not the Shannon entropy of $p$?"* Because the *eigenbasis* realization minimizes entropy ([../C4/11](../C4/11-von-neumann-entropy-is-the-minimum.md)); compression uses $\rho$'s eigenvectors, giving the eigenvalue entropy $H(\rho)$.
- *"What if the $|\psi_i\rangle$ aren't orthogonal?"* Schumacher still compresses to $H(\rho)$ (the eigenvalue entropy), which is $\le$ the Shannon entropy of the (non-orthogonal) ensemble — you can do *better* than naive classical labeling.
- *"Role of entanglement fidelity?"* It's the right success criterion (preserve states even against a reference); the Fano inequality ([06](06-quantum-fano.md)) makes the converse quantitative.
- *"Analogy to Shannon?"* Exact mirror: typical set ↔ typical subspace, $H(X)$ bits ↔ $H(\rho)$ qubits.
