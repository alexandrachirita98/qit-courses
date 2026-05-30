# 07 — Mutual information of a quantum–classical state = Holevo $\chi$

**Claim.** For a classical–quantum state $\rho_{AB}=\sum_i p_i\,|i\rangle\langle i|_A\otimes\rho_B^i$,
$$I(A{:}B)=H\Big(\sum_i p_i\rho_i\Big)-\sum_i p_iH(\rho_i)=:\chi(\{p_i,\rho_i\}),$$
the **Holevo quantity**.

---

### 1. In plain words
Imagine Alice picks a classical label $i$ with probability $p_i$ and hands Bob the quantum state $\rho_i$. How correlated are her label and his quantum system? The answer is the Holevo $\chi$: the entropy of the *average* state minus the average of the entropies. It measures how much Bob's ensemble "spreads out" depending on Alice's choice — the maximum classical information his quantum system could reveal about $i$.

### 2. Toolbox
- $I(A{:}B)=H(A)+H(B)-H(AB)$ ([06](06-quantum-mutual-information.md)).
- For a block-diagonal (cq) state, $\log\rho_{AB}=\sum_i|i\rangle\langle i|\otimes\log(p_i\rho_i)$ (orthogonal $A$-blocks).
- $H(p)=-\sum_i p_i\log p_i$, and reduced states $\rho_A=\sum_ip_i|i\rangle\langle i|$, $\rho_B=\sum_ip_i\rho_i$.

### 3. The proof
1. **Joint entropy.** Because the $A$-blocks are orthogonal,
$$\log\rho_{AB}=\sum_i|i\rangle\langle i|\otimes\big(\log p_i\,I+\log\rho_i\big),$$
so
$$\rho_{AB}\log\rho_{AB}=\sum_i p_i\log p_i\,|i\rangle\langle i|\otimes\rho_i+\sum_i p_i|i\rangle\langle i|\otimes\rho_i\log\rho_i.$$
2. Take $-\text{Tr}$:
$$H(\rho_{AB})=-\sum_i p_i\log p_i\,\underbrace{\text{Tr}\rho_i}_{1}-\sum_i p_i\,\text{Tr}(\rho_i\log\rho_i)=H(p)+\sum_i p_iH(\rho_i).$$
3. **Marginals.** $H(\rho_A)=H(p)$ (since $\rho_A=\sum_i p_i|i\rangle\langle i|$ is "classical"), and $H(\rho_B)=H(\sum_i p_i\rho_i)$.
4. **Combine** via [06](06-quantum-mutual-information.md):
$$I(A{:}B)=H(\rho_A)+H(\rho_B)-H(\rho_{AB})=H(p)+H\big(\textstyle\sum_i p_i\rho_i\big)-\big(H(p)+\textstyle\sum_i p_iH(\rho_i)\big),$$
$$=H\Big(\sum_i p_i\rho_i\Big)-\sum_i p_iH(\rho_i)=\chi.\qquad\blacksquare$$

### 4. Where the magic happens
**The classical register $H(p)$ appears in both $H(A)$ and $H(AB)$ and cancels**, leaving the purely quantum "spread" $H(\bar\rho)-\overline{H(\rho_i)}$. That cancellation is what isolates the Holevo quantity from the mutual information.

### 5. If he pushes back
- *"Why is $\chi\ge0$?"* It's a mutual information, so $\ge0$ ([06](06-quantum-mutual-information.md)); equivalently, entropy is concave so $H(\sum p_i\rho_i)\ge\sum p_iH(\rho_i)$.
- *"When is $\chi=0$?"* When all $\rho_i$ are equal (Bob's state independent of Alice's label) — no correlation.
- *"Why is this *the* bound Bob faces?"* Because any measurement Bob makes is a channel on $B$, and mutual information only decreases under it ([08](08-holevo-theorem.md)) — so $\chi$ caps the information he can extract.
