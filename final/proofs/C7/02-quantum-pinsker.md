# 02 — The quantum Pinsker inequality

**Claim.** For any states $\rho,\sigma$,
$$\|\rho-\sigma\|_{\text{Tr}}\le\sqrt{2\ln2\,D(\rho\|\sigma)}.$$
Small relative entropy ⇒ small trace distance ⇒ hard to distinguish.

---

### 1. In plain words
Two entropic/operational measures of "closeness" are linked: the trace distance (how distinguishable, [01](01-helstrom-bound.md)) and the Umegaki divergence (relative entropy). Pinsker says the divergence upper-bounds the squared trace distance. The trick: build a channel that performs the Helstrom measurement and records its $\pm$ result in a qubit. This channel (a) can only *decrease* divergence (data processing) and (b) *preserves* the trace distance. So the quantum problem reduces to the **classical** Pinsker inequality on two-point distributions.

### 2. Toolbox
- **Classical Pinsker:** $\|p-q\|_1\le\sqrt{2\ln2\,D_{\text{KL}}(p\|q)}$ (borrowed from classical info theory).
- **Data processing** for $D$: $D(\mathcal E(\rho)\|\mathcal E(\sigma))\le D(\rho\|\sigma)$ ([../C6/02](../C6/02-data-processing-inequality.md)).
- Trace distance of **diagonal** (classical) states = $\ell_1$ distance of their diagonals.
- The Helstrom channel diagonalizes $\rho-\sigma$.

### 3. The proof
Let $\rho-\sigma=\sum_i\lambda_i|\psi_i\rangle\langle\psi_i|$ and define the channel that records the sign of each eigencomponent in a qubit:
$$\mathcal E(M)=\sum_{\lambda_i>0}|0\rangle\langle\psi_i|M|\psi_i\rangle\langle0|+\sum_{\lambda_i<0}|1\rangle\langle\psi_i|M|\psi_i\rangle\langle1|.$$
1. **$\mathcal E$ preserves the trace distance.** $\mathcal E(\rho)$ and $\mathcal E(\sigma)$ are diagonal qubit states, and $\mathcal E(\rho-\sigma)$ has diagonal $(\sum_{\lambda_i>0}\lambda_i,\ \sum_{\lambda_i<0}\lambda_i)$, whose $\ell_1$ norm is $\sum_i|\lambda_i|=\|\rho-\sigma\|_{\text{Tr}}$. So $\|\mathcal E(\rho)-\mathcal E(\sigma)\|_{\text{Tr}}=\|\rho-\sigma\|_{\text{Tr}}$.
2. **$\mathcal E$ lowers divergence** (it's a channel): $D(\mathcal E(\rho)\|\mathcal E(\sigma))\le D(\rho\|\sigma)$.
3. **Apply classical Pinsker** to the diagonal vectors $p,q$ of $\mathcal E(\rho),\mathcal E(\sigma)$ (for diagonal states, $D=D_{\text{KL}}(p\|q)$):
$$\|\rho-\sigma\|_{\text{Tr}}\overset{(1)}{=}\|p-q\|_1\overset{\text{Pinsker}}{\le}\sqrt{2\ln2\,D_{\text{KL}}(p\|q)}=\sqrt{2\ln2\,D(\mathcal E(\rho)\|\mathcal E(\sigma))}\overset{(2)}{\le}\sqrt{2\ln2\,D(\rho\|\sigma)}.$$ ∎

### 4. Where the magic happens
**The Helstrom channel is simultaneously trace-distance-preserving and divergence-decreasing.** That lets you "downgrade" the quantum states to two classical coins *without losing trace distance but only shrinking divergence* — so the classical Pinsker bound, applied to the coins, transfers to the quantum states (in the safe direction).

### 5. If he pushes back
- *"Why does $\mathcal E$ preserve trace distance exactly?"* Because it measures in the eigenbasis of $\rho-\sigma$, where the trace norm is just the sum of $|\lambda_i|$ — and that's exactly the $\ell_1$ distance of the recorded distributions.
- *"Direction of the inequalities — why does it still work?"* Trace distance is *kept equal*, divergence is *only decreased*; both push the chain the right way to bound $\|\rho-\sigma\|_{\text{Tr}}$ by $\sqrt{2\ln2\,D(\rho\|\sigma)}$.
- *"What's it good for?"* It says relative entropy controls distinguishability — used in QKD to turn a min-entropy/divergence bound into a trace-distance ("$\Delta$-secret") guarantee ([../lesson7-update/09-privacy-amplification.md](../lesson7-update/09-privacy-amplification.md)).
