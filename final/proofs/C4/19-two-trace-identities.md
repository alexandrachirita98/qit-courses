# 19 — Two trace identities used everywhere

**Claim.** For any density matrix $\rho$, any unit vector $|\phi\rangle$, and any orthonormal basis $\{|\phi_k\rangle\}$:

$$\text{(a)}\quad \text{Tr}\big(\rho\,|\phi\rangle\langle\phi|\big)=\langle\phi|\rho|\phi\rangle, \qquad\qquad \text{(b)}\quad \sum_k \langle\phi_k|\rho|\phi_k\rangle = 1.$$

---

### 1. In plain words
These are the two "plumbing" facts the whole lecture runs on.

- **(a)** says: the *probability* of a measurement landing in state $|\phi\rangle$ — which Born's rule writes as the trace $\text{Tr}(\rho\,|\phi\rangle\langle\phi|)$ — is just the simple number $\langle\phi|\rho|\phi\rangle$ (the "diagonal entry" of $\rho$ in the direction $|\phi\rangle$). It lets you swap between a trace and a sandwich whenever convenient.
- **(b)** says: if you add up the probabilities of all $d$ outcomes of a basis measurement, you get $1$. Of course you do — *something* has to happen. This is just normalization in disguise.

### 2. Toolbox
- **Trace** $\text{Tr}(A)=\sum_k \langle k|A|k\rangle$ in any orthonormal basis (basis-independent).
- **Trace is cyclic:** $\text{Tr}(ABC)=\text{Tr}(CAB)$.
- **Completeness of a basis:** $\sum_k |\phi_k\rangle\langle\phi_k| = I$.
- $\text{Tr}\,\rho = 1$ (unit trace, see [04](04-density-matrix-properties.md)).

### 3. The proof

**(a)** $\langle\phi|\rho|\phi\rangle$ is a single number ($1\times1$), and the trace of a number is itself. Using cyclicity:

1. $\text{Tr}\big(\rho|\phi\rangle\langle\phi|\big)=\text{Tr}\big(\langle\phi|\rho|\phi\rangle\big)$ — moved the bra $\langle\phi|$ from the back to the front (cyclic property).
2. $=\langle\phi|\rho|\phi\rangle$ — the trace of a scalar is the scalar. ∎

*Index version, if you don't trust cyclicity:* with $A=\rho|\phi\rangle\langle\phi|$,
$$\text{Tr}(A)=\sum_k\langle k|\rho|\phi\rangle\langle\phi|k\rangle=\langle\phi|\Big(\sum_k|k\rangle\langle k|\Big)\rho|\phi\rangle=\langle\phi|I\rho|\phi\rangle=\langle\phi|\rho|\phi\rangle.$$
(We pulled the scalars $\langle\phi|k\rangle$ next to $\langle k|$ and used completeness.)

**(b)**
1. $\displaystyle\sum_k \langle\phi_k|\rho|\phi_k\rangle = \sum_k \text{Tr}\big(\rho|\phi_k\rangle\langle\phi_k|\big)$ — each term rewritten by part (a).
2. $\displaystyle= \text{Tr}\Big(\rho\sum_k|\phi_k\rangle\langle\phi_k|\Big)$ — trace is linear, pull the sum inside.
3. $= \text{Tr}(\rho\, I)=\text{Tr}\,\rho$ — completeness of the basis.
4. $=1$ — unit trace. ∎

### 4. Where the magic happens
**A projector $|\phi\rangle\langle\phi|$ inside a trace turns into a sandwich $\langle\phi|\cdot|\phi\rangle$.** And **summing projectors over a full basis = the identity.** Those two moves convert almost every "probability" expression in C4 into something you can compute by hand.

### 5. If he pushes back
- *"Why is $\langle\phi|\rho|\phi\rangle\ge 0$?"* Because $\rho$ is positive semi-definite ([04](04-density-matrix-properties.md)); it's a genuine probability.
- *"Does (b) need $\rho$ to be a state?"* Only the final "$=1$" does (unit trace). The step $\sum_k\langle\phi_k|A|\phi_k\rangle=\text{Tr}\,A$ holds for **any** matrix $A$.
- *"What if the basis isn't orthonormal?"* Completeness $\sum_k|\phi_k\rangle\langle\phi_k|=I$ fails, so (b) breaks. Orthonormality is essential.
