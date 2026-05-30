# 10 — Unentangled (separable) states can't beat the classical bound 2

**Claim.** If the shared state is separable, $\rho=\sum_i p_i\,\rho_A^{(i)}\otimes\rho_B^{(i)}$, then $|\langle S\rangle_\rho|\le 2$ — no Bell violation.

---

### 1. In plain words
Entanglement is *necessary* to violate CHSH. On a product state, Alice's and Bob's measurements become independent random $\pm1$ values with fixed local averages — which is exactly a (local) hidden-variable model. And we already proved those obey $|S|\le2$. Mixing several product states (a separable state) only averages such legal values, so it stays $\le2$.

### 2. Toolbox
- On a product state, $\langle A_a\otimes B_b\rangle_{\rho_A\otimes\rho_B}=\langle A_a\rangle_{\rho_A}\langle B_b\rangle_{\rho_B}$ ([01](01-expected-value-Tr-rho-O.md)).
- Local averages live in $[-1,1]$: $\alpha_a:=\langle A_a\rangle\in[-1,1]$, $\beta_b:=\langle B_b\rangle\in[-1,1]$ (averages of $\pm1$).
- $\langle S\rangle$ is linear in $\rho$ ([01](01-expected-value-Tr-rho-O.md)), so it's a convex average over the components $p_i$.

### 3. The proof

**Step 1 — a single product state behaves classically.** On $\rho_A\otimes\rho_B$,
1. $\langle S\rangle=\alpha_0\beta_0+\alpha_0\beta_1+\alpha_1\beta_0-\alpha_1\beta_1=\alpha_0(\beta_0+\beta_1)+\alpha_1(\beta_0-\beta_1)$, with $\alpha_a,\beta_b\in[-1,1]$.
2. Since $|\alpha_a|\le1$:
$$|\langle S\rangle|\le|\beta_0+\beta_1|+|\beta_0-\beta_1|.$$
3. For real numbers, $|\beta_0+\beta_1|+|\beta_0-\beta_1|=2\max(|\beta_0|,|\beta_1|)\le2$ (since $|\beta_b|\le1$). Hence $|\langle S\rangle|\le2$ on any product state. ✓

**Step 2 — separable = convex mixture of product states.** With $\rho=\sum_i p_i\rho_A^{(i)}\otimes\rho_B^{(i)}$,
4. $\langle S\rangle_\rho=\sum_i p_i\langle S\rangle_{\rho_A^{(i)}\otimes\rho_B^{(i)}}$ — linearity of $\langle S\rangle$ in $\rho$.
5. $|\langle S\rangle_\rho|\le\sum_i p_i\,|\langle S\rangle_{\rho^{(i)}}|\le\sum_i p_i\cdot2=2$ — triangle inequality + Step 1. ∎

### 4. Where the magic happens
**On a product state the quantum correlator factorizes, $\langle A\otimes B\rangle=\langle A\rangle\langle B\rangle$, which is precisely a local hidden-variable model** (the "hidden variable" being which product component you're in). The same $|b_0+b_1|+|b_0-b_1|\le2$ identity from the classical proof ([08](08-classical-chsh-bound.md)) reappears, now for the *expectations* $\beta_b$.

### 5. If he pushes back
- *"So entanglement is necessary AND sufficient for violation?"* Necessary always (this proof). Sufficient for *pure* states (every entangled pure state violates some CHSH — Gisin's theorem); for mixed entangled states not always (some are local).
- *"Why does factorization kill the violation?"* Because then there *is* a joint assignment of outcome-statistics, i.e. a local model — and KTL's commutator correction effectively vanishes at the level of correlators.
- *"Contrast with the maximal case?"* [07](07-tsirelson-sharpness.md): reaching $2\sqrt2$ needs a maximally entangled state. Separable ⇒ $\le2$; maximally entangled + anticommuting settings ⇒ $2\sqrt2$.
