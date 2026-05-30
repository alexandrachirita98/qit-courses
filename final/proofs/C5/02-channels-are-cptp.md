# 02 — Quantum channels are completely positive and trace preserving (CPTP)

**Claim.** A physical channel $\mathcal E$ must be **trace preserving** ($\text{Tr}\,\mathcal E(A)=\text{Tr}\,A$) and **completely positive** ($I_n\otimes\mathcal E$ maps PSD to PSD for every $n$). Equivalently: *quantum channels = CPTP maps.*

---

### 1. In plain words
Two physical demands force the definition. (1) Probabilities must stay normalized: outputs are states, so traces (total probability) are preserved. (2) The channel might act on just *part* of a larger entangled system, and the *whole* system must remain a valid state (no negative probabilities). Demanding positivity even on entangled inputs is "complete" positivity — strictly more than ordinary positivity. Together: CPTP.

### 2. Toolbox
- Any matrix decomposes as $A=\frac{A+A^\dagger}{2}+\frac{A-A^\dagger}{2}$ (Hermitian + anti-Hermitian), and a Hermitian matrix is (PSD) − (PSD). So $A=\alpha_1\rho_1-\alpha_2\rho_2+i\alpha_3\rho_3-i\alpha_4\rho_4$ with $\alpha_k\ge0$, $\rho_k$ states.
- $\mathcal E$ is linear ([01](01-channel-is-linear-and-extends-uniquely.md)) and maps states to states.
- States have trace 1; for a state $\rho$, $\text{Tr}\,\mathcal E(\rho)=1=\text{Tr}\,\rho$.

### 3. The proof

**Trace preserving.** Decompose $A=\alpha_1\rho_1-\alpha_2\rho_2+i\alpha_3\rho_3-i\alpha_4\rho_4$.
1. By linearity, $\text{Tr}\,\mathcal E(A)=\alpha_1\text{Tr}\,\mathcal E(\rho_1)-\alpha_2\text{Tr}\,\mathcal E(\rho_2)+i\alpha_3\text{Tr}\,\mathcal E(\rho_3)-i\alpha_4\text{Tr}\,\mathcal E(\rho_4)$.
2. Each $\mathcal E(\rho_k)$ is a state, so $\text{Tr}\,\mathcal E(\rho_k)=1=\text{Tr}\,\rho_k$. Hence $\text{Tr}\,\mathcal E(A)=\alpha_1-\alpha_2+i\alpha_3-i\alpha_4=\text{Tr}\,A$. ∎

**Completely positive.** We must show $I_n\otimes\mathcal E(A)\ge0$ whenever $A\ge0$, for all $n$.
3. Physically, $\mathcal E$ applied to half of an $n\times d$ system must output a valid (PSD) state, because the input $A$ (a state of the joint system, up to scaling) maps to a state. For a single state-component this is $I_n\otimes\mathcal E(\alpha_1\rho_1)=\alpha_1\,(I_n\otimes\mathcal E)(\rho_1)\ge0$.
4. Since this holds for every $n$ and the action is linear, $I_n\otimes\mathcal E$ preserves the PSD cone — that is exactly complete positivity. ∎

**So the formal definition is: a quantum channel is a CPTP map.** (The non-obvious word is "completely": ordinary positivity is *not* enough — see the transpose in [13](13-ppt-criterion.md).)

### 4. Where the magic happens
**Decompose any matrix into four states** ($A=\alpha_1\rho_1-\alpha_2\rho_2+i\alpha_3\rho_3-i\alpha_4\rho_4$): this reduces "what $\mathcal E$ does to arbitrary $A$" to "what it does to states," where physicality (trace 1, stays PSD) is guaranteed. The leap from positive to *completely* positive is the recognition that $\mathcal E$ may act on a subsystem of an entangled whole.

### 5. If he pushes back
- *"Why isn't positivity enough?"* Because a positive-but-not-CP map (like the transpose) sends some entangled inputs to non-states (negative eigenvalues) — physically impossible for a real device. CP rules those out. This is precisely what makes positive maps useful as *entanglement detectors* ([12](12-pncp-separability-criterion.md)).
- *"Is every CPTP map physically realizable?"* Yes — Stinespring ([09](09-stinespring-dilation.md)) builds it from an ancilla + unitary + partial trace.
- *"How do I check CP in practice?"* Compute the Choi matrix and check $J_{\mathcal E}\ge0$ ([06](06-chois-theorem.md)).
