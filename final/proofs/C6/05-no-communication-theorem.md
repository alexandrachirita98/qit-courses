# 05 — The no-communication theorem

**Claim.** For any channel $\mathcal E$ acting on Bob's system and any bipartite state $\rho_{AB}$,
$$\text{Tr}_B\big((I_A\otimes\mathcal E)\rho_{AB}\big)=\text{Tr}_B(\rho_{AB})=\rho_A.$$
So whatever Bob does to his subsystem (gate, measurement, entangling an ancilla), Alice's reduced state — hence all her local statistics — is unchanged. No faster-than-light signalling.

---

### 1. In plain words
Bob can fiddle with his half all he likes; Alice, measuring only her half, cannot detect that anything happened until Bob physically sends her something. Mathematically: tracing out Bob's system *after* he applies a channel gives the same $\rho_A$ as before. The channel's trace-preservation is exactly what makes Bob's meddling invisible.

### 2. Toolbox
- It suffices to check on basis blocks $|i_A\rangle\langle j_A|\otimes|i'_B\rangle\langle j'_B|$ (linearity).
- Kraus form $\mathcal E(\cdot)=\sum_k K_k(\cdot)K_k^\dagger$ with completeness $\sum_k K_k^\dagger K_k=I$ (TP, [C5/07](../C5/07-kraus-theorem-trace-preserving.md)).
- Cyclic trace: $\text{Tr}(K_kXK_k^\dagger)=\text{Tr}(K_k^\dagger K_kX)$.

### 3. The proof
Check on a basis block (general $\rho_{AB}$ follows by linearity):
1. $\text{Tr}_B\Big((I_A\otimes\mathcal E)\big(|i_A\rangle\langle j_A|\otimes|i'_B\rangle\langle j'_B|\big)\Big)=|i_A\rangle\langle j_A|\;\text{Tr}_B\Big(\mathcal E(|i'_B\rangle\langle j'_B|)\Big).$
2. $\text{Tr}_B\,\mathcal E(|i'_B\rangle\langle j'_B|)=\sum_k\text{Tr}\big(K_k|i'_B\rangle\langle j'_B|K_k^\dagger\big)=\langle j'_B|\Big(\sum_k K_k^\dagger K_k\Big)|i'_B\rangle$ — cyclicity.
3. $=\langle j'_B|I|i'_B\rangle=\delta_{i'_B,j'_B}$ — **completeness** (trace preservation).
4. So the block maps to $|i_A\rangle\langle j_A|\,\delta_{i'_B j'_B}=\text{Tr}_B\big(|i_A\rangle\langle j_A|\otimes|i'_B\rangle\langle j'_B|\big)$.
5. By linearity, $\text{Tr}_B((I_A\otimes\mathcal E)\rho_{AB})=\text{Tr}_B\rho_{AB}$ for all $\rho_{AB}$. ∎

(Dual statement: $\text{Tr}_A((I_A\otimes\mathcal E)\rho)=\mathcal E(\text{Tr}_A\rho)$ — Bob, conversely, can't tell whether he holds his half of $\rho$ or just $\text{Tr}_A\rho$.)

### 4. Where the magic happens
**Trace preservation $\sum_k K_k^\dagger K_k=I$ is precisely what kills Bob's action under $\text{Tr}_B$:** the channel folds back to the identity inside the trace. A non-trace-preserving "operation" *could* signal — which is why only genuine (TP) channels are physical.

### 5. If he pushes back
- *"What if Bob measures and keeps the outcome?"* Still a channel (a quantum instrument, [CHSH/04](../CHSH/04-observable-as-quantum-instrument.md)); the theorem applies, so Alice's marginal is unchanged. Bob learns something, but Alice can't tell.
- *"Doesn't entanglement let them communicate?"* No — entanglement gives *correlations*, not signalling. Exploiting them (superdense coding, teleportation) always requires a classical message.
- *"Where's this used?"* It underlies the equivalent QKD picture in [13](13-bb84-security.md): Eve acting on the channel can't be detected by the marginal alone, so security must come from uncertainty relations.
