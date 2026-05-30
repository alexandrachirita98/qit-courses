# 08 — Holevo's theorem: monotonicity of mutual information & the Holevo bound

**Claim.** Mutual information is monotone under a local channel: for any channel $\mathcal E$ on $B$,
$$I(A{:}\mathcal E(B))\le I(A{:}B).$$
Consequently, if Alice encodes a classical label $i$ (prob. $p_i$) into states $\rho_i$ and Bob measures, the information he can recover is bounded by the **Holevo bound**
$$I(A{:}\tilde A)\le\chi=H\Big(\sum_i p_i\rho_i\Big)-\sum_i p_iH(\rho_i).$$

---

### 1. In plain words
Bob processing his system can't increase how much it tells him about Alice — that's monotonicity, and it's just the data processing inequality applied to mutual information. The payoff: no matter how cleverly Bob measures, the classical information he extracts about Alice's label is capped by the Holevo quantity $\chi$. This is why $n$ qubits can carry at most $n$ classical bits.

### 2. Toolbox
- $I(A{:}B)=D(\rho_{AB}\|\rho_A\otimes\rho_B)$ ([06](06-quantum-mutual-information.md)).
- DPI: $D$ shrinks under any channel ([02](02-data-processing-inequality.md)).
- A channel on $B$ leaves $A$'s marginal alone: $((I_A\otimes\mathcal E)\rho)_A=\rho_A$ ([05](05-no-communication-theorem.md)), and $((I_A\otimes\mathcal E)\rho)_B=\mathcal E(\rho_B)$.
- For a cq state, $I(A{:}B)=\chi$ ([07](07-quantum-classical-mutual-info.md)).

### 3. The proof

**Monotonicity.**
1. $I(A{:}\mathcal E(B))=I(A{:}B)_{(I_A\otimes\mathcal E)\rho}=D\big((I_A\otimes\mathcal E)\rho\,\big\|\,\rho_A\otimes\mathcal E(\rho_B)\big)$ — using the marginals above.
2. Note $\rho_A\otimes\mathcal E(\rho_B)=(I_A\otimes\mathcal E)(\rho_A\otimes\rho_B)$. So both arguments are the *same channel* $I_A\otimes\mathcal E$ applied to $\rho$ and to $\rho_A\otimes\rho_B$:
$$I(A{:}\mathcal E(B))=D\big((I_A\otimes\mathcal E)\rho\,\big\|\,(I_A\otimes\mathcal E)(\rho_A\otimes\rho_B)\big)\overset{\text{DPI}}{\le}D(\rho\|\rho_A\otimes\rho_B)=I(A{:}B).$$ ∎

**Holevo bound.**
3. Alice prepares the cq state $\rho_{AB}=\sum_i p_i|i\rangle\langle i|_A\otimes\rho_B^i$, with $I(A{:}B)=\chi$ ([07](07-quantum-classical-mutual-info.md)).
4. Bob's measurement (even a POVM) is a channel $\mathcal E$ on $B$ producing a classical guess $\tilde A$: $\rho\mapsto\sum_{i,j}p_i|i\rangle\langle i|_A\otimes d_{j|i}|j\rangle\langle j|_B$.
5. By monotonicity, the information his guess shares with Alice's label is
$$I(A{:}\tilde A)=I(A{:}\mathcal E(B))\le I(A{:}B)=\chi.\qquad\blacksquare$$

### 4. Where the magic happens
**Monotonicity of mutual information is literally the DPI applied to the pair $\big(\rho,\ \rho_A\otimes\rho_B\big)$ under $I_A\otimes\mathcal E$.** Then "Bob measures" = "apply a channel," so his accessible information can't beat the un-processed $I(A{:}B)=\chi$.

### 5. If he pushes back
- *"What are the loopholes?"* Holevo bounds *total* accessible info, not *which* bit — so Bob can choose which bit to read (Quantum Random Access Codes); and with shared entanglement the bound improves to $I(A{:}\tilde A)\le\log d-H(A'|B)$, enabling superdense coding (the conditional entropy can be negative, [09](09-conditional-von-neumann-entropy.md)).
- *"Why does this cap qubits-as-bits?"* For $d=2^n$ with $\chi\le\log d=n$, so one $n$-qubit message conveys $\le n$ classical bits.
- *"Is $\chi$ achievable?"* Asymptotically yes (Holevo–Schumacher–Westmoreland), with block coding.
