# 09 — Conditional von Neumann entropy and its monotonicities

**Claim.** Define $H(A|B)_\rho=H(\rho_{AB})-H(\rho_B)$. Then
$$H(A|B)=\log d_A-D\big(\rho_{AB}\,\big\|\,\tfrac{I_A}{d_A}\otimes\rho_B\big),$$
and consequently:
1. $H(A|\mathcal E(B))\ge H(A|B)$ for any channel $\mathcal E$ on $B$;
2. $H(\mathcal E(A)|B)\ge H(A|B)$ for any **bistochastic** $\mathcal E$ on $A$;
3. $H(A|B)\ge0$ for every **separable** state (so $H(A|B)<0\Rightarrow$ entanglement).

---

### 1. In plain words
Classically, conditioning never increases entropy and is always $\ge0$. Quantumly it's stranger: $H(A|B)$ can be **negative** when $A,B$ are entangled — Bob can "know more than everything" about $A$. Writing $H(A|B)$ as "$\log d_A$ minus a divergence" lets the data processing inequality instantly deliver three monotonicity facts, and pins down that *negative* conditional entropy is a signature of entanglement.

### 2. Toolbox
- $H(A|B)=H(\rho_{AB})-H(\rho_B)$.
- $D(\rho_{AB}\|I_A/d_A\otimes\rho_B)=\log d_A-H(A|B)$ (derived in step 1).
- DPI ([02](02-data-processing-inequality.md)); joint convexity of $D$ ([01](01-umegaki-divergence-nonnegative.md)).
- $D\ge0$ ([01](01-umegaki-divergence-nonnegative.md)).

### 3. The proof

**The divergence form.**
1. $D(\rho_{AB}\|\tfrac{I_A}{d_A}\otimes\rho_B)=-\text{Tr}\rho_{AB}\log(\tfrac{I_A}{d_A}\otimes\rho_B)+\text{Tr}\rho_{AB}\log\rho_{AB}.$ The first term: $\log(\tfrac{I_A}{d_A}\otimes\rho_B)=-\log d_A\,I+I_A\otimes\log\rho_B$, so it equals $\log d_A+\text{Tr}\rho_B\log\rho_B\cdot(-1)$... carefully,
$$-\text{Tr}\rho_{AB}\log(\tfrac{I_A}{d_A}\otimes\rho_B)=\log d_A-\text{Tr}(\rho_B\log\rho_B)=\log d_A+H(\rho_B).$$
With the second term $=-H(\rho_{AB})$:
$$D(\rho_{AB}\|\tfrac{I_A}{d_A}\otimes\rho_B)=\log d_A+H(\rho_B)-H(\rho_{AB})=\log d_A-H(A|B).\quad\checkmark$$

**Property 1 (process Bob).** Apply DPI to $\rho_{AB}$ and $\tfrac{I_A}{d_A}\otimes\rho_B$ under $I_A\otimes\mathcal E$:
2. $D\big((I\otimes\mathcal E)\rho_{AB}\,\|\,\tfrac{I_A}{d_A}\otimes\mathcal E(\rho_B)\big)\le D(\rho_{AB}\|\tfrac{I_A}{d_A}\otimes\rho_B)$. Translating via step 1 ($\log d_A-H$): $\log d_A-H(A|\mathcal E(B))\le\log d_A-H(A|B)$, i.e. $H(A|\mathcal E(B))\ge H(A|B)$. ∎

**Property 2 (bistochastic on Alice).** A bistochastic $\mathcal E$ fixes $I_A/d_A$; apply DPI under $\mathcal E\otimes I_B$ similarly (the reference $\tfrac{I_A}{d_A}\otimes\rho_B$ is invariant), giving $H(\mathcal E(A)|B)\ge H(A|B)$. ∎

**Property 3 (separable ⇒ nonnegative).** For $\rho=\sum_i p_i|\phi_i\rangle\langle\phi_i|\otimes|\psi_i\rangle\langle\psi_i|$:
3. $H(A|B)=\log d_A-D\big(\sum_i p_i|\phi_i\rangle\langle\phi_i|\otimes|\psi_i\rangle\langle\psi_i|\,\big\|\,\sum_i p_i\tfrac{I_A}{d_A}\otimes|\psi_i\rangle\langle\psi_i|\big)$.
4. By **joint convexity**, $D\le\sum_i p_iD\big(|\phi_i\rangle\langle\phi_i|\otimes|\psi_i\rangle\langle\psi_i|\,\|\,\tfrac{I_A}{d_A}\otimes|\psi_i\rangle\langle\psi_i|\big)=\sum_i p_iD\big(|\phi_i\rangle\langle\phi_i|\|\tfrac{I_A}{d_A}\big)=\sum_i p_i\log d_A=\log d_A.$
5. Hence $H(A|B)\ge\log d_A-\log d_A=0$. ∎ So $H(A|B)<0$ forces entanglement.

### 4. Where the magic happens
**$H(A|B)=\log d_A-D(\rho_{AB}\|I_A/d_A\otimes\rho_B)$ turns conditional entropy into a divergence**, so DPI/joint-convexity (the C6 engine) immediately yield the monotonicities and the separability bound. Negativity = "the joint state is more ordered than Bob's marginal," only possible with entanglement.

### 5. If he pushes back
- *"Compute $H(A|B)$ for a Bell state."* For $|\beta_{00}\rangle$: $H(\rho_{AB})=0$ (pure), $H(\rho_B)=\log d$ (maximally mixed), so $H(A|B)=-\log d$ — maximally negative. (See [10](10-schmidt-decomposition.md).)
- *"Intuition for negativity?"* It quantifies pre-shared entanglement usable for, e.g., superdense coding / state merging (it's the qubit cost, which can be negative = you gain entanglement).
- *"Is conditioning-reduces-entropy still true?"* $H(A|B)\le H(A)$ holds (from $I(A{:}B)\ge0$), but unlike classical, $H(A|B)$ itself can dip below 0.
