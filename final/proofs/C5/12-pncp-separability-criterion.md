# 12 — Positive (not completely positive) maps detect entanglement

**Claim.** Let $\rho\in\mathcal B(\mathbb C^n\otimes\mathbb C^d)$.
- **(Easy, useful direction)** If $\mathcal E:\mathcal B(\mathbb C^d)\to\mathcal B(\mathbb C^{d})$ is **positive** and $(I_n\otimes\mathcal E)\rho\not\ge0$, then $\rho$ is **entangled**.
- **(Full criterion)** $\rho$ is entangled $\iff$ there exists a positive map $\mathcal E$ with $(I_n\otimes\mathcal E)\rho\not\ge0$.

This $\mathcal E$ is positive but **not** completely positive.

---

### 1. In plain words
A *positive* map keeps single states positive but may wreck *entangled* states when applied to one half — precisely because it's not completely positive. That failure is a feature: separable states survive any positive map, so if applying $I\otimes\mathcal E$ produces a negative eigenvalue, the input couldn't have been separable. Hence positive-but-not-CP maps are **entanglement detectors**. The converse (every entangled state is caught by *some* positive map) uses a separating-hyperplane / entanglement-witness argument.

### 2. Toolbox
- Separable: $\rho=\sum_i p_i|\phi_i\rangle\langle\phi_i|\otimes|\psi_i\rangle\langle\psi_i|$.
- A positive map preserves positivity of single states: $\mathcal E(|\psi\rangle\langle\psi|)\ge0$.
- **Entanglement witness:** separable states form a closed convex set; an entangled $\rho$ outside it can be separated by a hyperplane = a Hermitian $O$ with $\text{Tr}(O\rho)<0$ but $\text{Tr}\big(O\,|\phi\rangle\langle\phi|\otimes|\psi\rangle\langle\psi|\big)\ge0$ for all product states.
- Witness ↔ map: interpret $O$ as the Choi matrix of a map $\mathcal E$ (so $O=J_{\mathcal E}$).

### 3. The proof

**(Easy direction) Positive maps don't disturb separable states.**
1. Apply $I_n\otimes\mathcal E$ to a separable $\rho$:
$$(I_n\otimes\mathcal E)\Big(\sum_i p_i|\phi_i\rangle\langle\phi_i|\otimes|\psi_i\rangle\langle\psi_i|\Big)=\sum_i p_i\,|\phi_i\rangle\langle\phi_i|\otimes\mathcal E(|\psi_i\rangle\langle\psi_i|).$$
2. Each $\mathcal E(|\psi_i\rangle\langle\psi_i|)\ge0$ (positivity), each $|\phi_i\rangle\langle\phi_i|\ge0$, so every term is PSD, and $p_i\ge0$: the sum is $\ge0$.
3. Contrapositive: if $(I_n\otimes\mathcal E)\rho\not\ge0$ then $\rho$ is **not** separable, i.e. entangled. ∎

**(Converse) Every entangled state is detected.**
4. The separable states form a closed convex set. If $\rho$ is entangled, it lies outside, so a **separating hyperplane** gives a Hermitian $O$ (an *entanglement witness*) with
$$\text{Tr}(O\rho)<0,\qquad \text{Tr}\big(O\,|\phi\rangle\langle\phi|\otimes|\psi\rangle\langle\psi|\big)\ge0\ \ \forall|\phi\rangle,|\psi\rangle.$$
5. Interpret $O=J_{\mathcal E}$ as a Choi matrix of a map $\mathcal E$. The witness condition $\text{Tr}(O\,|\phi\rangle\langle\phi|\otimes|\psi\rangle\langle\psi|)\ge0$ translates (using $J_{\mathcal E}\leftrightarrow\mathcal E$) into $\langle\phi|\mathcal E(|\psi\rangle\langle\psi|)|\phi\rangle\ge0$ for all pure $|\psi\rangle,|\phi\rangle$ — i.e. $\mathcal E(|\psi\rangle\langle\psi|)\ge0$, so $\mathcal E$ is **positive**.
6. And $\text{Tr}(O\rho)<0$ translates into $(I_n\otimes\mathcal E)\rho\not\ge0$. So this positive $\mathcal E$ detects $\rho$. Since $O\not\ge0$ (it has negative expectation on $\rho$), $\mathcal E$ is **not** CP. ∎

### 4. Where the magic happens
**Separable states survive every positive map (apply $\mathcal E$ termwise to the product pieces); entangled states need not.** The converse is convex geometry: an entangled state sits outside the convex set of separable states, so a hyperplane (witness $O$) separates it, and reading $O$ as a Choi matrix turns the witness into the detecting positive map.

### 5. If he pushes back
- *"Concrete positive-not-CP map?"* The transpose $T$ — that's the PPT criterion [13](13-ppt-criterion.md).
- *"Why isn't one map enough for all $\rho$?"* No single positive map detects every entangled state in general; the criterion quantifies over *all* positive maps. (For small dimensions $nd\le6$, the transpose alone suffices.)
- *"What's the witness, intuitively?"* An observable whose expectation is $\ge0$ on all separable states but $<0$ on $\rho$ — a measurable certificate of entanglement.
