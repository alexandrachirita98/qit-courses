# 03 — Random states are indistinguishable ⇔ they have the same density matrix

**Claim.** Two random quantum states $|v\rangle\sim\{|\psi_i\rangle,p_i\}$ and $|v'\rangle\sim\{|\psi'_j\rangle,p'_j\}$ produce identical measurement statistics for **every** observable if and only if
$$\rho:=\sum_i p_i|\psi_i\rangle\langle\psi_i|=\sum_j p'_j|\psi'_j\rangle\langle\psi'_j|=:\rho'.$$

---

### 1. In plain words
For a *pure* state, "all the physics" lives in the projector $|\psi\rangle\langle\psi|$ ([02](02-indiscernible-pure-states.md)). For a *random* state — a probabilistic mixture of pure states — "all the physics" lives in the **average** of those projectors, the density matrix $\rho$. Two recipes that produce the same $\rho$ are physically the same gas of states: no measurement, ever, can tell them apart. The reason is that every measurement probability turns out to be a linear readout of $\rho$ (namely $\text{Tr}(\rho E_\lambda)$), so it only ever "sees" $\rho$.

### 2. Toolbox
- Probability that a random state collapses onto $|\phi_k\rangle$ is the *average over the mixture* of the pure-state collapse probabilities.
- $\sum_i p_i|\langle\psi_i|\phi_k\rangle|^2=\langle\phi_k|\big(\sum_i p_i|\psi_i\rangle\langle\psi_i|\big)|\phi_k\rangle=\text{Tr}(\rho\,|\phi_k\rangle\langle\phi_k|)$, via [19](19-two-trace-identities.md).
- A nonzero **Hermitian** matrix has a nonzero eigenvalue (spectral theorem).

### 3. The proof

**Step 0: every measurement probability is $\text{Tr}(\rho E_\lambda)$.**
For an observable $O=\sum_\lambda\lambda E_\lambda$, the probability of outcome $\lambda$ on the random state is
1. $\Pr[\lambda]=\mathbb{E}_i\big[\langle\psi_i|E_\lambda|\psi_i\rangle\big]=\sum_i p_i\langle\psi_i|E_\lambda|\psi_i\rangle$ — average the Born probability over which $|\psi_i\rangle$ we hold.
2. $=\text{Tr}\Big(E_\lambda\sum_i p_i|\psi_i\rangle\langle\psi_i|\Big)=\text{Tr}(E_\lambda\rho)$ — push the sum into a trace ([19](19-two-trace-identities.md)).

So **all** statistics depend on the state only through $\rho$.

**(⇐) Same $\rho$ ⇒ indistinguishable.**
3. If $\rho=\rho'$, then $\text{Tr}(E_\lambda\rho)=\text{Tr}(E_\lambda\rho')$ for every observable and outcome. Identical statistics everywhere. ✓

**(⇒) Indistinguishable ⇒ same $\rho$.** (Prove the contrapositive.)
4. Suppose $\rho\ne\rho'$. Then $\Delta:=\rho-\rho'$ is a **nonzero Hermitian** matrix (difference of Hermitians), so it has an eigenvector $|\chi\rangle$ with eigenvalue $\mu\ne0$.
5. Measure the projective observable whose eigenbasis includes $|\chi\rangle$, outcome "$|\chi\rangle$" with projector $|\chi\rangle\langle\chi|$:
$$\Pr[\,|\chi\rangle\,]_\rho-\Pr[\,|\chi\rangle\,]_{\rho'}=\langle\chi|\rho|\chi\rangle-\langle\chi|\rho'|\chi\rangle=\langle\chi|\Delta|\chi\rangle=\mu\neq0.$$
6. The two states give different probabilities for this outcome ⇒ **distinguishable**. Contrapositive: indistinguishable ⇒ $\rho=\rho'$. ∎

### 4. Where the magic happens
**Born's rule is linear in the state's projector, so averaging it over a mixture replaces "projector" by "average projector" $=\rho$.** That single linearity collapses an entire ensemble down to one matrix — and the converse uses the cheap fact that a *nonzero* Hermitian matrix always has an eigenvector you can measure to expose the difference.

### 5. If he pushes back
- *"Why does the difference $\rho-\rho'$ have to be Hermitian?"* Both $\rho,\rho'$ are Hermitian ([04](04-density-matrix-properties.md)); the difference of Hermitians is Hermitian, hence diagonalizable with real eigenvalues.
- *"Couldn't a fancier measurement (POVM) distinguish them even when $\rho=\rho'$?"* No. Any POVM outcome probability is also $\text{Tr}(\rho F_i)$, still a function of $\rho$ alone. (POVMs are C5 material; the same linearity argument covers them.)
- *"So is the map (random state) → $\rho$ many-to-one?"* Yes — that's exactly [05](05-every-density-matrix-is-realized.md)'s non-uniqueness. Many ensembles, one $\rho$, one physics.
- *"Pure-state version?"* Set the mixtures to single states: this reduces to [02](02-indiscernible-pure-states.md), where "same $\rho$" becomes "same projector" = "equal up to global phase."
