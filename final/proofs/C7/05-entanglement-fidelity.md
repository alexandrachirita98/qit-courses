# 05 — Entanglement fidelity and the pure-state formula

**Claim.**
- For a pure target $\sigma=|\phi\rangle\langle\phi|$, the fidelity is the collapse probability $F(\rho,|\phi\rangle\langle\phi|)=\langle\phi|\rho|\phi\rangle$.
- To measure how well a channel $\mathcal E$ preserves $\rho$ *even against an entangled reference*, use the **entanglement fidelity**
$$F(\rho,\mathcal E)=F\big((I_{\text{Bob}}\otimes\mathcal E_{\text{Alice}})|\psi_\rho\rangle\langle\psi_\rho|,\ |\psi_\rho\rangle\langle\psi_\rho|\big)=\langle\psi_\rho|(I\otimes\mathcal E)(|\psi_\rho\rangle\langle\psi_\rho|)|\psi_\rho\rangle,$$
independent of which purification $|\psi_\rho\rangle$ of $\rho$ is chosen.

---

### 1. In plain words
Compression is good if Alice can't tell her states were squeezed and unsqueezed — *even using entanglement with a helper to test*. Ordinary fidelity $F(\rho,\mathcal E(\rho))$ isn't enough because it would let Bob re-optimize his half. Entanglement fidelity fixes a purification $|\psi_\rho\rangle$, runs only Alice's half through $\mathcal E$, and measures the overlap with the original. The pure-target formula $F(\rho,|\phi\rangle\langle\phi|)=\langle\phi|\rho|\phi\rangle$ makes it a single number: the probability $\rho$ would pass the "are you still $|\phi\rangle$?" test.

### 2. Toolbox
- Uhlmann formula $F(\rho,\sigma)=(\text{Tr}|\sqrt\rho\sqrt\sigma|)^2$ ([04](04-uhlmann-theorem.md)).
- For pure $\sigma=|\phi\rangle\langle\phi|$, $\sqrt\sigma=|\phi\rangle\langle\phi|$.
- A purification $|\psi_\rho\rangle$ with $\text{Tr}_{\text{Bob}}|\psi_\rho\rangle\langle\psi_\rho|=\rho$; all purifications related by a unitary on Bob.

### 3. The proof

**Pure-target fidelity.**
1. With $\sigma=|\phi\rangle\langle\phi|$ (so $\sqrt\sigma=|\phi\rangle\langle\phi|$):
$$\text{Tr}|\sqrt\rho\sqrt\sigma|=\text{Tr}\sqrt{\sqrt\sigma\,\rho\,\sqrt\sigma}=\text{Tr}\sqrt{|\phi\rangle\langle\phi|\rho|\phi\rangle\langle\phi|}=\text{Tr}\sqrt{\langle\phi|\rho|\phi\rangle\,|\phi\rangle\langle\phi|}=\sqrt{\langle\phi|\rho|\phi\rangle}.$$
(Used $|\phi\rangle\langle\phi|\rho|\phi\rangle\langle\phi|=\langle\phi|\rho|\phi\rangle\,|\phi\rangle\langle\phi|$, a scalar times a projector.)
2. Square it: $F(\rho,|\phi\rangle\langle\phi|)=\langle\phi|\rho|\phi\rangle$ — exactly the probability that $\rho$ collapses onto $|\phi\rangle$. ∎

**Entanglement fidelity is purification-independent.**
3. The target $|\psi_\rho\rangle\langle\psi_\rho|$ is pure, so by step 1,
$$F(\rho,\mathcal E)=\langle\psi_\rho|\,(I\otimes\mathcal E)(|\psi_\rho\rangle\langle\psi_\rho|)\,|\psi_\rho\rangle.$$
4. Any two purifications differ by a unitary $V$ on Bob: $|\psi'_\rho\rangle=(V\otimes I)|\psi_\rho\rangle$. Since $V$ acts on Bob and $\mathcal E$ on Alice, $V$ commutes through $(I\otimes\mathcal E)$ and cancels in the symmetric expression $\langle\psi_\rho|(I\otimes\mathcal E)(\cdot)|\psi_\rho\rangle$. Hence the value is the same for all purifications. ∎

### 4. Where the magic happens
**Against a pure target, Uhlmann collapses to $\langle\phi|\rho|\phi\rangle$** — fidelity = collapse probability. And fixing a purification while letting only Alice's half evolve is exactly the "Alice can't tell, even with a helper" criterion; Bob's unitary freedom cancels, so it's well-defined.

### 5. If he pushes back
- *"Why not just use $F(\rho,\mathcal E(\rho))$?"* That allows re-optimizing Bob's reference, hiding correlated errors; entanglement fidelity tests $\mathcal E$ on a *fixed* entangled input, the stricter requirement for QoS-preserving compression.
- *"Kraus formula?"* $F(\rho,\mathcal E)=\sum_k|\text{Tr}(K_k\rho)|^2$ for $\mathcal E=\sum_kK_k\cdot K_k^\dagger$ — drops out of the same expression.
- *"How is it measured?"* Measure the POVM $\{|\psi_\rho\rangle\langle\psi_\rho|,\,I-|\psi_\rho\rangle\langle\psi_\rho|\}$ on $(I\otimes\mathcal E)|\psi_\rho\rangle\langle\psi_\rho|$ — feeds straight into the Fano bound [06](06-quantum-fano.md).
