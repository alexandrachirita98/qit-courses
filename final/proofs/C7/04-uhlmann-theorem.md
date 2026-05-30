# 04 — Uhlmann's theorem: $F(\rho,\sigma)=(\text{Tr}|\sqrt\rho\sqrt\sigma|)^2$

**Claim.** The fidelity — the maximal squared overlap over purifications — has the closed form
$$F(\rho,\sigma)=\max_{\text{purifications}}|\langle\phi_\rho|\psi_\sigma\rangle|^2=\Big(\text{Tr}\big|\sqrt\rho\sqrt\sigma\big|\Big)^2=\Big(\text{Tr}\sqrt{\sqrt\sigma\,\rho\,\sqrt\sigma}\Big)^2.$$

---

### 1. In plain words
Fidelity was *defined* by an optimization over purifications ([03](03-fidelity-and-discrimination.md)) — hard to compute directly. Uhlmann's theorem turns it into a formula you can evaluate from $\rho$ and $\sigma$ alone. The proof writes a general purification overlap as a trace involving a free unitary $U$, then uses the triangle inequality $|\text{Tr}(AU)|\le\text{Tr}|A|$ — tight for the right $U$ — to do the maximization in one stroke.

### 2. Toolbox
- Purifications $|\phi_\rho\rangle=\sum_i\sqrt{p_i}|a_i\rangle\otimes|x_i\rangle$, $|\psi_\sigma\rangle=\sum_j\sqrt{q_j}|b_j\rangle\otimes|y_j\rangle$ (eigen-decompositions $\rho=\sum_i p_i|a_i\rangle\langle a_i|$, $\sigma=\sum_j q_j|b_j\rangle\langle b_j|$).
- Freedom in a purification = a unitary $U$ on the purifying system.
- **Key inequality:** $|\text{Tr}(AU)|\le\text{Tr}|A|$ for any unitary $U$, with equality for a suitable $U$ (polar decomposition).

### 3. The proof
1. Compute a general overlap:
$$\langle\phi_\rho|\psi_\sigma\rangle=\sum_{i,j}\sqrt{p_iq_j}\,\langle a_i|b_j\rangle\,\langle x_i|y_j\rangle.$$
The factors $\langle x_i|y_j\rangle$ are entries of a free unitary $U$ (the purification freedom).
2. Repackage as a trace. Recognizing $\sum_i\sqrt{p_i}|a_i\rangle\langle a_i|=\sqrt\rho$ and $\sum_j\sqrt{q_j}|b_j\rangle\langle b_j|=\sqrt\sigma$, the sum becomes
$$\langle\phi_\rho|\psi_\sigma\rangle=\text{Tr}\big(\sqrt\rho\,\sqrt\sigma\,U\big)$$
for the unitary $U$ encoding the $\langle x_i|y_j\rangle$ overlaps.
3. **Bound and optimize.** By the key inequality,
$$|\langle\phi_\rho|\psi_\sigma\rangle|=|\text{Tr}(\sqrt\rho\sqrt\sigma\,U)|\le\text{Tr}\big|\sqrt\rho\sqrt\sigma\big|,$$
with equality achievable by choosing $U$ from the polar decomposition of $\sqrt\rho\sqrt\sigma$ (e.g. taking $|x_i\rangle=|y_i\rangle$).
4. Therefore the maximal overlap is $\text{Tr}|\sqrt\rho\sqrt\sigma|$, and squaring,
$$F(\rho,\sigma)=\Big(\text{Tr}|\sqrt\rho\sqrt\sigma|\Big)^2=\Big(\text{Tr}\sqrt{\sqrt\sigma\rho\sqrt\sigma}\Big)^2.\qquad\blacksquare$$
(The last equality uses $|\sqrt\rho\sqrt\sigma|=\sqrt{\sqrt\sigma\rho\sqrt\sigma}$ up to a unitary, same trace.)

### 4. Where the magic happens
**The purification freedom is exactly a free unitary $U$ inside $\text{Tr}(\sqrt\rho\sqrt\sigma\,U)$, and $\max_U|\text{Tr}(AU)|=\text{Tr}|A|$.** So optimizing over all purifications = optimizing over $U$ = applying one matrix inequality. The abstract "max over purifications" becomes a single trace-norm.

### 5. If he pushes back
- *"Prove $|\text{Tr}(AU)|\le\text{Tr}|A|$."* Polar-decompose $A=|A|W$ ($W$ unitary). Then $\text{Tr}(AU)=\text{Tr}(|A|WU)=\text{Tr}(|A|V)$ with $V=WU$ unitary; $|\text{Tr}(|A|V)|\le\sum_k s_k|V_{kk}|\le\sum_k s_k=\text{Tr}|A|$ (singular values $s_k\ge0$, $|V_{kk}|\le1$). Equality at $V=I$.
- *"Pure-state special case?"* If $\sigma=|\phi\rangle\langle\phi|$ then $F(\rho,\sigma)=\langle\phi|\rho|\phi\rangle$ — see [05](05-entanglement-fidelity.md).
- *"Symmetric in $\rho,\sigma$?"* Yes — $\text{Tr}|\sqrt\rho\sqrt\sigma|=\text{Tr}|\sqrt\sigma\sqrt\rho|$.
