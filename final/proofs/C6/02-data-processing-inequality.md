# 02 — The Quantum Data Processing Inequality

**Claim.** For any quantum channel $\mathcal E$ and any states $\rho,\sigma$,
$$D(\mathcal E(\rho)\|\mathcal E(\sigma))\le D(\rho\|\sigma).$$
Processing through a channel can only make two states **harder** to tell apart.

---

### 1. In plain words
You can't gain distinguishing information by passing states through the same noisy box — at best you keep what you had. This is *the* workhorse inequality of quantum information. The proof has three moves, each leaving $D$ unchanged or decreasing it: adding a clean ancilla (no change), applying a unitary (no change, by invariance), and the only inequality — applying the **completely depolarizing** channel to the environment, which is a *mixture of unitaries* and hence contractive by joint convexity.

### 2. Toolbox
- **Joint convexity** of $D$ (stated; technical): $D(\sum_i p_i\rho_i\|\sum_i p_i\sigma_i)\le\sum_i p_iD(\rho_i\|\sigma_i)$.
- **Unitary invariance:** $D(U\rho U^\dagger\|U\sigma U^\dagger)=D(\rho\|\sigma)$ (logs transform by conjugation, trace is cyclic).
- **Ancilla invariance:** $D(\rho\otimes\tau\|\sigma\otimes\tau)=D(\rho\|\sigma)$ for a fixed state $\tau$.
- **Stinespring** ([C5/09](../C5/09-stinespring-dilation.md)): $\mathcal E(\rho)=\text{Tr}_E(U(\rho\otimes|0\rangle\langle0|_E)U^\dagger)$.
- $\Delta_1$ (completely depolarizing) is a **mixed-unitary** channel: $\Delta_1(X)=\frac1{d^2}\sum_{a,b}Z^aX^b\,X\,(Z^aX^b)^\dagger=\frac{I}{d}\text{Tr}\,X$ ([C5/14](../C5/14-depolarizing-kraus-and-choi.md)).

### 3. The proof

**Mixed-unitary channels are contractive (the one inequality).** For $\mathcal F(\cdot)=\sum_i p_iU_i(\cdot)U_i^\dagger$:
1. $D(\mathcal F(\rho)\|\mathcal F(\sigma))=D(\sum_i p_iU_i\rho U_i^\dagger\|\sum_i p_iU_i\sigma U_i^\dagger)\overset{\text{joint conv.}}{\le}\sum_i p_iD(U_i\rho U_i^\dagger\|U_i\sigma U_i^\dagger)\overset{\text{inv.}}{=}\sum_i p_iD(\rho\|\sigma)=D(\rho\|\sigma).$

**Assemble the channel via Stinespring + depolarize the environment.**
2. $D(\rho\|\sigma)=D(\rho\otimes|0\rangle\langle0|_E\|\sigma\otimes|0\rangle\langle0|_E)$ — ancilla invariance.
3. $=D\big(U(\rho\otimes|0\rangle\langle0|)U^\dagger\big\|U(\sigma\otimes|0\rangle\langle0|)U^\dagger\big)$ — unitary invariance.
4. $\ge D\big((I_A\otimes\Delta_{1,E})U(\rho\otimes|0\rangle\langle0|)U^\dagger\big\|(I_A\otimes\Delta_{1,E})U(\sigma\otimes|0\rangle\langle0|)U^\dagger\big)$ — apply the **mixed-unitary** map $I_A\otimes\Delta_{1,E}$ (unitaries $I_A\otimes Z^aX^b$); contractive by step 1.
5. But $\Delta_{1,E}$ replaces the $E$-part by maximally mixed: $(I_A\otimes\Delta_{1,E})(X_{AE})=\text{Tr}_E(X_{AE})\otimes\frac{I_E}{d_E}$. So step 4's argument is $\mathcal E(\rho)\otimes\frac{I_E}{d_E}$ versus $\mathcal E(\sigma)\otimes\frac{I_E}{d_E}$.
6. $D\big(\mathcal E(\rho)\otimes\tfrac{I_E}{d_E}\big\|\mathcal E(\sigma)\otimes\tfrac{I_E}{d_E}\big)=D(\mathcal E(\rho)\|\mathcal E(\sigma))$ — ancilla invariance again.
7. Chaining 2–6: $D(\rho\|\sigma)\ge D(\mathcal E(\rho)\|\mathcal E(\sigma))$. ∎

### 4. Where the magic happens
**Partial trace = "depolarize the environment," and depolarizing is a mixture of unitaries, so joint convexity makes it contractive.** Everything else (ancilla, unitary) leaves $D$ exactly invariant. The hard analytic fact — joint convexity of Umegaki divergence — is the single technical input (proved in Watrous 5.2.3); the rest is bookkeeping with Stinespring.

### 5. If he pushes back
- *"Why is $\Delta_1$ mixed-unitary?"* The Heisenberg–Weyl operators $\{Z^aX^b\}$ averaged give $\frac{I}{d}\text{Tr}$ ([C5/14](../C5/14-depolarizing-kraus-and-choi.md), slide computation).
- *"Do I have to prove joint convexity?"* Usually cited as a hard lemma; know that it's *the* nontrivial ingredient and everything else is invariance.
- *"Consequences?"* Monotonicity of mutual information ([08](08-holevo-theorem.md)), entropy can't decrease under unital channels ([03](03-bistochastic-cant-decrease-entropy.md)), conditional-entropy monotonicities ([09](09-conditional-von-neumann-entropy.md)).
