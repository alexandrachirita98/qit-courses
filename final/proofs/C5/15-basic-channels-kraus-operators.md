# 15 — Basic operations are channels: gate, ancilla, partial trace, measurement

**Claim.** Each of the following is a quantum channel (CPTP), with the stated Kraus operators:
| operation | action | Kraus operators |
|---|---|---|
| gate $U$ | $\rho\mapsto U\rho U^\dagger$ | $\{U\}$ |
| add ancilla | $\rho\mapsto\rho\otimes|0\rangle\langle0|$ | $\{I\otimes|0\rangle\}$ |
| partial trace | $\rho_{AB}\mapsto\text{Tr}_B\rho_{AB}$ | $\{I\otimes\langle i|\}_i$ |
| measure $O$ & record | $\rho\mapsto\sum_\lambda E_\lambda\rho E_\lambda\otimes|\lambda\rangle\langle\lambda|$ | $\{E_\lambda(O)\otimes|\lambda\rangle\}_\lambda$ |

These are the building blocks Stinespring assembles ([09](09-stinespring-dilation.md)).

---

### 1. In plain words
Everything you physically do to a quantum system — apply a gate, bring in a fresh qubit, discard a subsystem, measure and write down the result — is a channel. We just exhibit Kraus operators for each and check the completeness relation $\sum_k K_k^\dagger K_k=I$ that makes it trace-preserving ([07](07-kraus-theorem-trace-preserving.md)). CP is automatic from the Kraus form ([03](03-kraus-implies-cp.md)).

### 2. Toolbox
- A map is a channel iff it has a complete Kraus rep: CP ([03](03-kraus-implies-cp.md)) + $\sum_k K_k^\dagger K_k=I$ ([07](07-kraus-theorem-trace-preserving.md)).
- $\{|i\rangle\}$ orthonormal basis of the traced-out system; $\sum_i|i\rangle\langle i|=I$.
- Projectors $E_\lambda$ satisfy $E_\lambda^\dagger E_\lambda=E_\lambda$, $\sum_\lambda E_\lambda=I$.

### 3. The proof — check each

**Gate $U$.** Single Kraus operator $K=U$. Completeness: $U^\dagger U=I$ (unitary). CP + TP. ✓ (And $\text{rank}\,J=1$, the unitary corollary [06](06-chois-theorem.md).)

**Adding an ancilla.** $\rho\mapsto\rho\otimes|0\rangle\langle0|=(I\otimes|0\rangle)\,\rho\,(I\otimes\langle0|)$, single Kraus operator $K=I\otimes|0\rangle$ (maps $\mathcal H\to\mathcal H\otimes\mathcal H_E$).
1. Completeness: $K^\dagger K=(I\otimes\langle0|)(I\otimes|0\rangle)=I\otimes\langle0|0\rangle=I$. ✓

**Partial trace.** $\text{Tr}_B\rho_{AB}=\sum_i(I_A\otimes\langle i|)\rho_{AB}(I_A\otimes|i\rangle)$, Kraus operators $K_i=I_A\otimes\langle i|$.
2. Completeness: $\sum_i K_i^\dagger K_i=\sum_i(I\otimes|i\rangle)(I\otimes\langle i|)=I\otimes\sum_i|i\rangle\langle i|=I\otimes I=I$. ✓

**Measure $O$ and record (quantum instrument).** Kraus operators $K_\lambda=E_\lambda(O)\otimes|\lambda\rangle$ (see [CHSH/04](../CHSH/04-observable-as-quantum-instrument.md)).
3. Completeness: $\sum_\lambda K_\lambda^\dagger K_\lambda=\sum_\lambda(E_\lambda\otimes\langle\lambda|)(E_\lambda\otimes|\lambda\rangle)=\sum_\lambda E_\lambda^2\otimes\langle\lambda|\lambda\rangle=\sum_\lambda E_\lambda=I$. ✓

All four have complete Kraus representations ⇒ all are CPTP channels. ∎

### 4. Where the magic happens
**Each elementary operation is "one or a few Kraus operators," and the completeness relation $\sum_kK_k^\dagger K_k=I$ is just a resolution of identity** — unitarity ($U^\dagger U=I$), normalization ($\langle0|0\rangle=1$), basis completeness ($\sum_i|i\rangle\langle i|=I$), or projector completeness ($\sum_\lambda E_\lambda=I$). Composing them (Stinespring) shows every channel is built from these.

### 5. If he pushes back
- *"Compose them to get Stinespring."* Add ancilla → apply joint unitary → partial trace = a general channel ([09](09-stinespring-dilation.md)). These three rows are exactly its ingredients.
- *"Is partial trace really CP?"* Yes — it has the Kraus form above; it's the adjoint of "tensoring with $I$," and it maps states to states.
- *"Which of these are unital?"* The gate (always), partial trace (yes, $\text{Tr}_B(I_{AB})=d_B I_A$, unital up to the dimension factor in normalized form); adding an ancilla is *not* unital ($I\mapsto I\otimes|0\rangle\langle0|\ne I$). See [08](08-bistochastic-iff-unital.md).
