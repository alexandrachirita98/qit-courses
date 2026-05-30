# 01 — Expected value of an observable is $\langle O\rangle_\rho=\text{Tr}(\rho O)$

**Claim.** Measuring observable $O=\sum_\lambda\lambda E_\lambda$ on a state $\rho$ gives expected outcome
$$\langle O\rangle_\rho=\mathbb{E}[\text{outcome}]=\text{Tr}(\rho O),$$
which is **linear in $O$**. Consequently, for a *random* observable $O_o\sim\{O_1,\dots,O_m;\ f_1,\dots,f_m\}$,
$$\mathbb{E}[\langle O_o\rangle]=\Big\langle \sum_o f_o O_o\Big\rangle,$$
i.e. "average of the expectations = expectation of the average observable."

---

### 1. In plain words
The average reading of a measurement is computed two ways that agree: weigh each outcome $\lambda$ by its probability, *or* just trace $\rho$ against the matrix $O$. The second form is a clean linear functional of $O$, which makes the CHSH algebra (sums of products of observables) painless — you can push expectations through sums and tensor products freely.

### 2. Toolbox
- Outcome probability $\Pr[\lambda]=\text{Tr}(\rho E_\lambda)$ (Born's rule for mixed states; see [C4/19](../C4/19-two-trace-identities.md), [C4/03](../C4/03-indistinguishable-iff-same-density-matrix.md)).
- Spectral form $O=\sum_\lambda\lambda E_\lambda$ with $\sum_\lambda E_\lambda=I$.
- Trace is linear: $\text{Tr}(\sum_k c_k M_k)=\sum_k c_k\text{Tr}(M_k)$.

### 3. The proof

**The formula.**
1. $\langle O\rangle_\rho=\sum_\lambda\lambda\Pr[\lambda]=\sum_\lambda\lambda\,\text{Tr}(\rho E_\lambda)$ — definition of expectation + Born's rule.
2. $=\text{Tr}\Big(\rho\sum_\lambda\lambda E_\lambda\Big)=\text{Tr}(\rho O)$ — pull the sum inside the trace (linearity), recognize $O$. ∎

**Linearity in $O$.** $\text{Tr}(\rho(aO+bO'))=a\,\text{Tr}(\rho O)+b\,\text{Tr}(\rho O')$ — immediate from trace linearity.

**Random observable.** Let $O_o$ equal $O_i$ with probability $f_i$.
3. $\mathbb{E}[\langle O_o\rangle]=\sum_o f_o\langle O_o\rangle=\sum_o f_o\,\text{Tr}(\rho O_o)$ — average over which observable.
4. $=\text{Tr}\Big(\rho\sum_o f_o O_o\Big)=\Big\langle\sum_o f_o O_o\Big\rangle$ — linearity again; the two expectations commute. ∎

For a **pure** state $\rho=|\psi\rangle\langle\psi|$: $\langle O\rangle=\text{Tr}(|\psi\rangle\langle\psi|O)=\langle\psi|O|\psi\rangle$ (cyclic trace) — the familiar sandwich.

### 4. Where the magic happens
**$\langle O\rangle=\text{Tr}(\rho O)$ is linear in $O$.** Every CHSH manipulation — expanding $S$, taking expectations of sums and tensor products — is just this one linearity used repeatedly.

### 5. If he pushes back
- *"Why is the average label even meaningful here?"* For `±1` observables the eigenvalues are genuine numbers (outcomes $\pm1$), so unlike the horse example ([C4/14](../C4/14-why-the-average-is-meaningless.md)) the mean *is* physical.
- *"Does $\langle A\otimes B\rangle$ factor?"* Only on product states $\rho=\rho_A\otimes\rho_B$: then $\text{Tr}((\rho_A\otimes\rho_B)(A\otimes B))=\text{Tr}(\rho_A A)\text{Tr}(\rho_B B)$. Entanglement breaks the factorization — that's what lets $S$ exceed 2.
