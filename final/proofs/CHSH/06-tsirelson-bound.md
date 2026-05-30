# 06 — Tsirelson's bound: $|\langle S\rangle|\le 2\sqrt2$

**Claim.** For any quantum state and any $\pm1$ observables, the CHSH value satisfies
$$|\langle S\rangle|=|\text{Tr}(\rho S)|\le 2\sqrt2.$$

---

### 1. In plain words
Quantum mechanics *can* beat the classical CHSH bound of 2 — but not by an unlimited amount. The ceiling is $2\sqrt2\approx2.83$. The proof is short once you have the KTL identity: bound the operator $S^2$ from above by $8I$, conclude $\|S\|\le\sqrt8=2\sqrt2$, and note any expectation of a Hermitian operator is squeezed between its smallest and largest eigenvalues.

### 2. Toolbox
- KTL identity $S^2=4I-[A_0,A_1]\otimes[B_0,B_1]$ ([05](05-khalfin-tsirelson-landau-identity.md)).
- $\|[A_0,A_1]\|\le2$, $\|[B_0,B_1]\|\le2$ ([09](09-commutator-norm-bound.md)); $\|X\otimes Y\|=\|X\|\,\|Y\|$.
- $S$ is Hermitian, so $\langle S\rangle=\text{Tr}(\rho S)$ is an average of $S$'s (real) eigenvalues; hence $|\langle S\rangle|\le\|S\|=\sqrt{\|S^2\|}$.

### 3. The proof
1. From KTL, the "correction" term has norm
$$\big\|[A_0,A_1]\otimes[B_0,B_1]\big\|=\|[A_0,A_1]\|\cdot\|[B_0,B_1]\|\le2\cdot2=4.$$
2. So as operators, $S^2=4I-(\text{something of norm}\le4)\ \preceq\ 4I+4I=8I$. (For a Hermitian $M$ with $\|M\|\le4$, $-M\preceq4I$.)
3. Therefore $\|S^2\|\le8$, and since $\|S\|^2=\|S^2\|$ (Hermitian), $\|S\|\le\sqrt8=2\sqrt2$.
4. $S$ Hermitian ⇒ $\langle S\rangle=\text{Tr}(\rho S)=\sum_i s_i\,\langle e_i|\rho|e_i\rangle$ over $S$'s eigenvalues $s_i$, a probability-weighted average, so $|\langle S\rangle|\le\max_i|s_i|=\|S\|\le2\sqrt2$. ∎

### 4. Where the magic happens
**KTL turns the four-term CHSH operator into "$4I$ minus a bounded correction," instantly capping $S^2$ at $8I$.** Then the generic fact "an expectation never exceeds the top eigenvalue" finishes it. No optimization over states needed — the bound is built into the operator algebra.

### 5. If he pushes back
- *"Is $2\sqrt2$ achievable?"* Yes — when both commutators saturate (anticommuting observables) and you pick the right entangled state; see [07](07-tsirelson-sharpness.md).
- *"Why is the classical bound only 2?"* Classically $[A_0,A_1]=0$ (commuting hidden-variable functions), so $S^2=4I$ and $\|S\|\le2$ ([08](08-classical-chsh-bound.md)).
- *"Step 2 looks like a sign trick — justify it."* For Hermitian $M=[A_0,A_1]\otimes[B_0,B_1]$... careful: this $M$ is not Hermitian, but $S^2$ *is* Hermitian and equals $4I-M$. Bound via $\|S^2-4I\|=\|M\|\le4$, so every eigenvalue of $S^2$ lies in $[4-4,4+4]=[0,8]$, giving $\|S^2\|\le8$. (Cleaner phrasing.)
- *"Does it depend on dimension?"* No — holds for qubits or any dimension; the algebra only used $A^2=B^2=I$.
