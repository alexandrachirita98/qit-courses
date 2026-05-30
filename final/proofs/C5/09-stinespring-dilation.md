# 09 — Stinespring dilation: every channel = ancilla + unitary + partial trace

**Claim.** $\mathcal E$ is a quantum channel $\iff$ there is an ancilla $E$, a unitary $U$, and a fixed ancilla state $|0\rangle_E$ with
$$\mathcal E(\rho)=\text{Tr}_E\Big(U\big(|0\rangle_E\langle0|\otimes\rho\big)U^\dagger\Big).$$

---

### 1. In plain words
Every noisy channel is secretly *unitary on a bigger system*. Attach a clean ancilla, let everything evolve together by one big reversible gate $U$, then ignore (trace out) the ancilla. The "noise" is just the information that leaked into the part you threw away. This is the physical picture behind Kraus operators: the index $k$ is which ancilla state you'd see if you measured it.

### 2. Toolbox
- A channel has a complete Kraus rep $\mathcal E(\rho)=\sum_{k=0}^{m-1}K_k\rho K_k^\dagger$ with $\sum_k K_k^\dagger K_k=I$ ([06](06-chois-theorem.md), [07](07-kraus-theorem-trace-preserving.md)).
- An **isometry** $V$ satisfies $V^\dagger V=I$ (orthonormal columns); it extends to a unitary by Gram–Schmidt.
- Partial trace $\text{Tr}_E(\cdot)=\sum_k(\langle k|_E\otimes I)\,\cdot\,(|k\rangle_E\otimes I)$.

### 3. The proof

**(⇐) The construction is a channel.** Adding an ancilla, applying a unitary, and partial-tracing are each CP and TP, and compositions of CPTP maps are CPTP. So the right-hand side is a channel. (Spelled out in [15](15-basic-channels-kraus-operators.md).)

**(⇒) Build the dilation from Kraus operators.**
1. Define $V=\sum_{k=0}^{m-1}|k\rangle_E\otimes K_k$, a map $\mathbb C^d\to\mathbb C^m\otimes\mathbb C^{d'}$. Check it's an isometry:
$$V^\dagger V=\sum_{k,k'}(\langle k|\otimes K_k^\dagger)(|k'\rangle\otimes K_{k'})=\sum_{k}K_k^\dagger K_k=I_d,$$
using $\langle k|k'\rangle=\delta_{kk'}$ and completeness.
2. **Extend $V$ to a unitary $U$** by Gram–Schmidt (orthonormal columns of $V$ extend to an orthonormal basis = columns of $U$). Then $U(|0\rangle_E\otimes|\psi\rangle)=V|\psi\rangle$ for all $|\psi\rangle$.
3. **Trace out the ancilla.** For a pure input $|\psi\rangle$:
$$\text{Tr}_E\big(V|\psi\rangle\langle\psi|V^\dagger\big)=\sum_{k'}(\langle k'|\otimes I)\Big(\sum_{k}|k\rangle\otimes K_k|\psi\rangle\Big)\Big(\sum_{k''}\langle k''|\otimes\langle\psi|K_{k''}^\dagger\Big)(|k'\rangle\otimes I).$$
The $\langle k'|k\rangle$, $\langle k''|k'\rangle$ factors force $k=k''=k'$, leaving
$$=\sum_{k}K_k|\psi\rangle\langle\psi|K_k^\dagger=\mathcal E(|\psi\rangle\langle\psi|).$$
4. By linearity this extends to all $\rho$: $\text{Tr}_E\big(U(|0\rangle_E\langle0|\otimes\rho)U^\dagger\big)=\mathcal E(\rho)$. ∎

**Bonus (measurement picture).** Measuring the ancilla in the $|k\rangle$ basis after $U$ yields $k$ with probability $\text{Tr}(K_k\rho K_k^\dagger)$, post-state $K_k\rho K_k^\dagger/p_k$ — recovering the selective measurement; averaging over $k$ gives $\mathcal E$.

### 4. Where the magic happens
**Stack the Kraus operators into the columns of one tall isometry $V=\sum_k|k\rangle\otimes K_k$.** Completeness $\sum_k K_k^\dagger K_k=I$ is *exactly* the statement $V^\dagger V=I$ (isometry). Extend to a unitary, trace out the stacking register $E$, and the $\langle k|k'\rangle=\delta_{kk'}$ orthogonality reassembles the Kraus sum.

### 5. If he pushes back
- *"How big must the ancilla be?"* Dimension $m=\text{rank}\,J_{\mathcal E}$ suffices (the minimal number of Kraus operators); the lecture takes $m\le dd'$ to be safe.
- *"Is $U$ unique?"* No — different completions of $V$, and different Kraus reps, give different dilations (all related by an ancilla isometry). The reduced action $\mathcal E$ is unique.
- *"Relation to Naimark?"* Naimark ([11](11-naimark-dilation.md)) is Stinespring specialized to measurement channels: dilate the POVM's $K_i=\sqrt{F_i}$ and projectively measure the ancilla.
