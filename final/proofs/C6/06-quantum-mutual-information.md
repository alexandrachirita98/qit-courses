# 06 — Quantum mutual information $I(A{:}B)=H(A)+H(B)-H(AB)$

**Claim.** Defining $I(A{:}B)_\rho=D(\rho_{AB}\|\rho_A\otimes\rho_B)$, one has
$$I(A{:}B)=H(\rho_A)+H(\rho_B)-H(\rho_{AB}),$$
exactly as in the classical case. In particular $I(A{:}B)\ge0$ (it's a divergence).

---

### 1. In plain words
Mutual information measures how far the joint state is from being a product of its marginals — i.e. how correlated $A$ and $B$ are. Defining it as the divergence between $\rho_{AB}$ and $\rho_A\otimes\rho_B$ automatically makes it $\ge0$ ([01](01-umegaki-divergence-nonnegative.md)). Expanding that divergence and using that $\log$ of a tensor product is a sum, it collapses to the familiar entropy combination $H(A)+H(B)-H(AB)$.

### 2. Toolbox
- $\log(\rho_A\otimes\rho_B)=\log\rho_A\otimes I_B+I_A\otimes\log\rho_B$ (log of a tensor product).
- **Partial-trace identity:** $\text{Tr}_B\big(\rho_{AB}(\log\rho_A\otimes I_B)\big)=\rho_A\log\rho_A$ (proved below).
- $\text{Tr}\rho_A\log\rho_A=-H(\rho_A)$; $D\ge0$ ([01](01-umegaki-divergence-nonnegative.md)).

### 3. The proof
1. $I(A{:}B)=D(\rho_{AB}\|\rho_A\otimes\rho_B)=-\text{Tr}\big(\rho_{AB}\log(\rho_A\otimes\rho_B)\big)+\text{Tr}(\rho_{AB}\log\rho_{AB}).$
2. Second term $=-H(\rho_{AB})$.
3. First term: split the log,
$$-\text{Tr}\big(\rho_{AB}(\log\rho_A\otimes I_B)\big)-\text{Tr}\big(\rho_{AB}(I_A\otimes\log\rho_B)\big).$$
4. Reduce each via partial trace: $\text{Tr}\big(\rho_{AB}(\log\rho_A\otimes I_B)\big)=\text{Tr}_A\big[(\text{Tr}_B\rho_{AB})\log\rho_A\big]=\text{Tr}(\rho_A\log\rho_A)=-H(\rho_A)$, and likewise $=-H(\rho_B)$.
5. Combine: $I(A{:}B)=\big(H(\rho_A)+H(\rho_B)\big)-H(\rho_{AB})$. ∎ Nonnegativity is inherited from $D\ge0$.

**The partial-trace identity (step used above).**
6. Write $\rho_{AB}=\sum_{i,i',j,j'}(\rho)_{ii',jj'}|i\rangle\langle j|_A\otimes|i'\rangle\langle j'|_B$. Then
$$\text{Tr}_B\big(\rho_{AB}(\log\rho_A\otimes I_B)\big)=\sum_{i,i',j}(\rho)_{ii',ji'}\,|i\rangle\langle j|\log\rho_A=\sum_{i,j}\langle i|\rho_A|j\rangle\,|i\rangle\langle j|\log\rho_A=\rho_A\log\rho_A,$$
using $\sum_{i'}(\rho)_{ii',ji'}=\langle i|\rho_A|j\rangle$ (definition of the reduced state) and $\sum_{i,j}\langle i|\rho_A|j\rangle|i\rangle\langle j|=\rho_A$. ∎

### 4. Where the magic happens
**$\log(\rho_A\otimes\rho_B)$ splits into a sum, and partial-tracing each piece against $\rho_{AB}$ produces the marginal entropies.** That single algebraic fact turns the divergence definition into the entropy formula — and hands you nonnegativity for free.

### 5. If he pushes back
- *"Why define it as a divergence rather than the entropy sum?"* The divergence form makes $I\ge0$ immediate and connects to the DPI (monotonicity, [08](08-holevo-theorem.md)). The entropy form is for computing.
- *"Can $I(A{:}B)$ exceed the classical max?"* Yes — for entangled (esp. pure) states it can reach $2\min(\log d_A,\log d_B)$, double the classical bound, because $H(AB)$ can be smaller than each marginal.
- *"Subadditivity?"* $I\ge0$ is exactly subadditivity of entropy: $H(AB)\le H(A)+H(B)$.
