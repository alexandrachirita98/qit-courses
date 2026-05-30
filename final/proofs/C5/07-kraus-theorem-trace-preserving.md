# 07 — Kraus' theorem: trace-preserving ⇔ complete Kraus ⇔ $\text{Tr}_{d'}J_{\mathcal E}=I_d/d$

**Claim.** For a completely positive $\mathcal E(\rho)=\sum_k K_k\rho K_k^\dagger$, the following are equivalent:
1. **every** Kraus representation is complete ($\sum_k K_k^\dagger K_k=I_d$);
2. **some** Kraus representation is complete;
3. $\mathcal E$ is **trace preserving**;
4. $\text{Tr}_{\mathbb C^{d'}}J_{\mathcal E}=\dfrac{I_d}{d}$.

---

### 1. In plain words
Complete positivity (Choi's theorem) makes a map *physical-ish*, but a true channel must also conserve total probability — be trace preserving. Kraus' theorem says that's equivalent to the simple operator condition $\sum_k K_k^\dagger K_k=I$ ("the Kraus operators form a resolution of the identity"), and to a partial-trace condition on the Choi matrix. So checking "is it a channel?" = "is $J_{\mathcal E}\ge0$ **and** $\text{Tr}_{d'}J_{\mathcal E}=I/d$?"

### 2. Toolbox
- $\text{Tr}\,\mathcal E(|i\rangle\langle j|)=\text{Tr}\big(\sum_k K_k|i\rangle\langle j|K_k^\dagger\big)=\langle j|\big(\sum_k K_k^\dagger K_k\big)|i\rangle$ (cyclic trace).
- $\text{Tr}\,\mathcal E(\rho)=\sum_{i,j}\rho_{ij}\,\text{Tr}\,\mathcal E(|i\rangle\langle j|)$ (linearity).
- Recovery: $\mathcal E(|i\rangle\langle j|)=d(\langle i|\otimes I)J_{\mathcal E}(|j\rangle\otimes I)$ ([05](05-choi-psd-implies-kraus.md)).

### 3. The proof

**Compute the trace of $\mathcal E(|i\rangle\langle j|)$.**
1. $\text{Tr}\,\mathcal E(|i\rangle\langle j|)=\text{Tr}\sum_k K_k|i\rangle\langle j|K_k^\dagger=\langle j|\Big(\sum_k K_k^\dagger K_k\Big)|i\rangle$ — cyclicity moves $K_k^\dagger$ to the front.

**(1 ⇔ 2): completeness is a property of $\mathcal E$, not of the chosen $K_k$.**
2. Step 1 shows $\text{Tr}\,\mathcal E(|i\rangle\langle j|)=\big(\sum_k K_k^\dagger K_k\big)_{ji}$, which equals $\delta_{ij}$ iff $\sum_k K_k^\dagger K_k=I$. The left side $\text{Tr}\,\mathcal E(|i\rangle\langle j|)$ doesn't reference a particular Kraus rep, so if *one* rep is complete, $\text{Tr}\,\mathcal E(|i\rangle\langle j|)=\delta_{ij}$, and then *every* rep must also satisfy $\sum_k K_k^\dagger K_k=I$. Hence 1 ⇔ 2.

**(2 ⇔ 3): completeness ⇔ trace preserving.**
3. $\text{Tr}\,\mathcal E(\rho)=\sum_{i,j}\rho_{ij}\text{Tr}\,\mathcal E(|i\rangle\langle j|)$. This equals $\sum_{i,j}\rho_{ij}\delta_{ij}=\sum_i\rho_{ii}=\text{Tr}\,\rho$ for all $\rho$ **iff** $\text{Tr}\,\mathcal E(|i\rangle\langle j|)=\delta_{ij}$ **iff** $\sum_k K_k^\dagger K_k=I$. So TP ⇔ complete.

**(3 ⇔ 4): the Choi partial-trace condition.**
4. Using recovery, $\text{Tr}\,\mathcal E(|i\rangle\langle j|)=d\,\text{Tr}_{d'}\big[(\langle i|\otimes I)J_{\mathcal E}(|j\rangle\otimes I)\big]=d\,(\langle i|\,\text{Tr}_{d'}J_{\mathcal E}\,|j\rangle)$. TP means this equals $\delta_{ij}$, i.e. $\langle i|\text{Tr}_{d'}J_{\mathcal E}|j\rangle=\frac1d\delta_{ij}$, i.e. $\text{Tr}_{d'}J_{\mathcal E}=\frac{I_d}{d}$. ∎

### 4. Where the magic happens
**Trace-preservation collapses to a single operator equation $\sum_k K_k^\dagger K_k=I$**, because $\text{Tr}\,\mathcal E(|i\rangle\langle j|)=\langle j|(\sum_kK_k^\dagger K_k)|i\rangle$ probes exactly that operator. And since the *left* side is rep-independent, completeness can't depend on which Kraus operators you picked.

### 5. If he pushes back
- *"So the full 'is it a channel?' test is…"* $J_{\mathcal E}\ge0$ (CP, Choi [06](06-chois-theorem.md)) **and** $\text{Tr}_{d'}J_{\mathcal E}=I_d/d$ (TP, here).
- *"Contrast with classical stochastic matrices."* Complete Kraus ($\sum K_k^\dagger K_k=I$) is the quantum analogue of "columns sum to 1." Unitality ($\sum K_kK_k^\dagger=I$) is "rows sum to 1" — the two together are bistochastic ([08](08-bistochastic-iff-unital.md)).
- *"Why does $J_{\mathcal E}$ have trace 1 for a channel?"* $\text{Tr}\,J_{\mathcal E}=\text{Tr}(\text{Tr}_{d'}J_{\mathcal E})=\text{Tr}(I_d/d)=1$ — the Choi matrix of a channel is itself a density matrix (Jamiołkowski: channels ↔ states).
