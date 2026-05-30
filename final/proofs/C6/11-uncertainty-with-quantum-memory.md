# 11 — Uncertainty in the presence of quantum memory (Berta et al.)

**Claim.** If Bob holds a quantum memory $B$ correlated with Alice's system $A$, then for two basis observables $O=\{|\phi_k\rangle\}$, $O'=\{|\xi_j\rangle\}$,
$$H(O|B)_\rho+H(O'|B)_\rho\ \ge\ -\log\max_{k,j}|\langle\phi_k|\xi_j\rangle|^2\ +\ H(A|B)_\rho.$$
With no memory ($B$ trivial), the conditional terms become classical and this reduces to Maassen–Uffink plus a positive entropy bonus:
$$H(O)+H(O')\ \ge\ -\log\max_{k,j}|\langle\phi_k|\xi_j\rangle|^2+\underbrace{H(\rho)}_{\ge0}.$$

---

### 1. In plain words
Maassen–Uffink ([C4/12](../C4/12-maassen-uffink.md)) bounds how uncertain two incompatible measurements are. Berta et al. sharpen it when a *quantum memory* $B$ is around: a helper holding $B$ can reduce uncertainty about Alice's measurements. The improved bound adds the conditional entropy $H(A|B)$ on the right — which can be **negative** for entangled memory, meaning enough entanglement can beat the original uncertainty floor (the basis of EPR-steering and QKD attacks). When there's no memory, $H(A|B)\to H(\rho)\ge0$ and you recover Maassen–Uffink, strengthened.

### 2. Toolbox
- Conditional entropy as uncertainty: measuring $O$ on $A$ is a bistochastic (dephasing) channel $\mathcal E$, and $H(O|B)_\rho=H(A|B)_{(\mathcal E\otimes I_B)\rho}$.
- Monotonicity $H(\mathcal E(A)|B)\ge H(A|B)$ for bistochastic $\mathcal E$ ([09](09-conditional-von-neumann-entropy.md), property 2).
- The tripartite relation $H(O|B)+H(O'|C)\ge-\log c^2$ for pure $\rho_{ABC}$ ([12](12-tripartite-uncertainty.md)).
- $c^2=\max_{k,j}|\langle\phi_k|\xi_j\rangle|^2$ (max overlap).

### 3. The proof (reduction from the tripartite relation)
The cleanest route uses a **purification** $|\psi\rangle_{ABC}$ of $\rho_{AB}$ (so $\rho_{AB}=\text{Tr}_C|\psi\rangle\langle\psi|$) and the tripartite uncertainty relation [12](12-tripartite-uncertainty.md):
1. For pure $\rho_{ABC}$, [12](12-tripartite-uncertainty.md) gives $H(O|B)+H(O'|C)\ge-\log c^2$.
2. For a *pure* global state, the measured conditional entropies satisfy the duality $H(O'|C)=-H(O'|B)+\text{(correction)}$; carrying the correction through (the slide's chain) converts $H(O'|C)$ into $H(O'|B)-H(A|B)$:
$$H(O'|C)\le -H(A|B)+H(O'|B)\quad\Longrightarrow\quad H(O|B)+H(O'|B)\ge -\log c^2+H(A|B).$$
3. **Average to mixed states.** Any mixed $\rho_{AB}$ is a mixture of pure states; since the left side is concave in the state, the inequality survives the average. ∎

**No-memory limit.** If $B$ is trivial, $H(O|B)=H(O)$ (ordinary Shannon entropy of the measurement) and $H(A|B)=H(\rho)\ge0$:
4. $H(O)+H(O')\ge-\log c^2+H(\rho)$, which is Maassen–Uffink plus the nonnegative bonus $H(\rho)$. ∎

### 4. Where the magic happens
**Conditional entropy is the right "uncertainty given side information," and a quantum memory contributes $H(A|B)$ — possibly negative — to the floor.** The proof is not a new inequality but a *repackaging* of the tripartite relation [12](12-tripartite-uncertainty.md) using a purification: the third party $C$ stands in for "the rest of the world."

### 5. If he pushes back
- *"How can the bound drop below Maassen–Uffink?"* If $A,B$ are maximally entangled, $H(A|B)=-\log d_A$ ([09](09-conditional-von-neumann-entropy.md)), so the right side can be $\le0$ — Bob can predict *both* measurements (the EPR "paradox"/steering).
- *"Why does measuring = a channel?"* Recording $O$ dephases $A$ in the $\{|\phi_k\rangle\}$ basis — a unital (bistochastic) channel; hence the conditional-entropy monotonicity applies ([09](09-conditional-von-neumann-entropy.md)).
- *"Where is this used?"* The QKD/BB84 security proof ([13](13-bb84-security.md)) is exactly this with $B,E$ being Bob's and Eve's memories.
