# 04 — Reduced states are the quantum marginals

**Claim.** If Alice measures her half of $\rho_{AB}$ in basis $\{|\xi_k\rangle\}$ and records the index, the channel factors as $\mathcal E(\rho)=\mathcal E_A(\text{Tr}_B\,\rho)$, where
$$\mathcal E_A(\rho_A)=\sum_k|k\rangle_R\langle\xi_k|_A\,\rho_A\,|\xi_k\rangle_A\langle k|_R,\qquad \text{Tr}_B(\rho_{AB})=\sum_b(I_A\otimes\langle b|_B)\rho_{AB}(I_A\otimes|b\rangle_B).$$
Hence, with no communication from Bob, Alice's statistics depend only on the **reduced state** $\rho_A=\text{Tr}_B\rho_{AB}$.

---

### 1. In plain words
Whatever Alice does locally, she only ever "sees" her reduced density matrix $\rho_A$ — the quantum analogue of a classical marginal distribution. The full bipartite operation "measure A, record the result" splits cleanly into "throw away B (partial trace)" followed by "measure A." So Alice literally cannot distinguish holding her half of an entangled $\rho_{AB}$ from holding an isolated $\rho_A$.

### 2. Toolbox
- Partial trace $\text{Tr}_B(\rho_{AB})=\sum_b(I_A\otimes\langle b|)\rho_{AB}(I_A\otimes|b\rangle)$ ([C5/15](../C5/15-basic-channels-kraus-operators.md)).
- Recording a measurement is a channel with Kraus operators acting on $A$ only.
- Born's rule on the reduced state: outcome probabilities $\text{Tr}(\rho_A E_k)$.

### 3. The proof
1. **Write the full channel.** Measuring $A$ in $\{|\xi_k\rangle\}$ and storing $k$ in register $R$, while not touching $B$:
$$\mathcal E(\rho_{AB})=\sum_{k,b}\big(|k\rangle_R\langle\xi_k|_A\otimes\langle b|_B\big)\,\rho_{AB}\,\big(|\xi_k\rangle_A\langle k|_R\otimes|b\rangle_B\big).$$
2. **The $B$-sum is exactly a partial trace.** Group it:
$$\mathcal E(\rho_{AB})=\sum_k|k\rangle_R\langle\xi_k|_A\Big(\underbrace{\sum_b(I_A\otimes\langle b|_B)\rho_{AB}(I_A\otimes|b\rangle_B)}_{=\,\text{Tr}_B\rho_{AB}\,=\,\rho_A}\Big)|\xi_k\rangle_A\langle k|_R.$$
3. **Recognize the composition.** The remaining $A$-operation is $\mathcal E_A$:
$$\mathcal E(\rho_{AB})=\sum_k|k\rangle_R\langle\xi_k|\,\rho_A\,|\xi_k\rangle\langle k|_R=\mathcal E_A(\rho_A)=\mathcal E_A(\text{Tr}_B\rho_{AB}).$$
4. The output register holds $k$ with probability $\langle\xi_k|\rho_A|\xi_k\rangle=\text{Tr}(\rho_A\,|\xi_k\rangle\langle\xi_k|)$ — a function of $\rho_A$ alone. ∎

### 4. Where the magic happens
**Summing over Bob's basis $\sum_b(I\otimes\langle b|)\cdots(I\otimes|b\rangle)$ *is* the partial trace.** So "measure A, ignore B" automatically computes $\rho_A$ first. Reduced states are the right notion of "Alice's local state," playing the role of marginals.

### 5. If he pushes back
- *"Does this depend on which purification/global state?"* No — only on $\rho_A=\text{Tr}_B\rho_{AB}$. Many global states share the same $\rho_A$ and are locally indistinguishable to Alice.
- *"Isn't that just the no-communication theorem?"* It's the Alice-side half: her statistics = function of $\rho_A$. The full no-signalling statement (Bob's actions don't change $\rho_A$) is [05](05-no-communication-theorem.md).
- *"Why 'marginal'?"* For a classical joint distribution $p(a,b)$, Alice sees $\sum_b p(a,b)$; partial trace is the exact quantum analogue.
