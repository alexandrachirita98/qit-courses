# 11 — Naimark dilation: every POVM is a gate + projective measurement

**Claim.** Any POVM $\{F_i\ge0\}_{i=0}^{n-1}$ with $\sum_i F_i=I_d$ can be implemented by adjoining an ancilla, applying a unitary, and performing a **projective** measurement on the enlarged system. Outcome $i$ occurs with probability $\text{Tr}(F_i\rho)$, the POVM's prediction.

---

### 1. In plain words
POVMs look more powerful than ordinary projective measurements — but they aren't, if you allow a bigger lab. Naimark's theorem says: turn each POVM element into a "measurement operator" $K_i=\sqrt{F_i}$, build the measurement channel, dilate it à la Stinespring, and then a *plain* projective measurement of the ancilla reproduces the POVM. So POVM = projective measurement viewed through an ancilla.

### 2. Toolbox
- $F_i\ge0$ has a positive square root: $K_i=\sqrt{F_i}$ (or any $K_i$ with $K_i^\dagger K_i=F_i$, e.g. Cholesky), so $F_i=K_i^\dagger K_i$.
- The measurement channel $\mathcal E(\rho)=\sum_i K_i\rho K_i^\dagger$ is CP, and complete since $\sum_i K_i^\dagger K_i=\sum_i F_i=I$ ([07](07-kraus-theorem-trace-preserving.md)).
- Stinespring dilation of a channel ([09](09-stinespring-dilation.md)): isometry $V=\sum_i|i\rangle_E\otimes K_i$, extend to unitary $U$.
- Born's rule: projective measurement of ancilla in $\{|i\rangle_E\}$.

### 3. The proof
1. **Square roots.** Set $K_i=\sqrt{F_i}$, so $F_i=K_i^\dagger K_i$ and $\sum_i K_i^\dagger K_i=\sum_i F_i=I$.
2. **Measurement channel & its dilation.** $\mathcal E(\rho)=\sum_i K_i\rho K_i^\dagger$ is a channel; by Stinespring, $V=\sum_i|i\rangle_E\otimes K_i$ is an isometry ($V^\dagger V=\sum_iK_i^\dagger K_i=I$), extended to a unitary $U$ with $U(|0\rangle_E\otimes|\psi\rangle)=V|\psi\rangle$.
3. **Projectively measure the ancilla** in the orthonormal basis $\{|i\rangle_E\}$ after applying $U$. The probability of outcome $i$ on input $|0\rangle_E\otimes\rho$ is
$$\Pr[i]=\text{Tr}\big[(|i\rangle_E\langle i|\otimes I)\,U(|0\rangle_E\langle0|\otimes\rho)U^\dagger\big]=\text{Tr}\big[(|i\rangle_E\langle i|\otimes I)\,V\rho V^\dagger\big].$$
4. Since $V\rho V^\dagger=\sum_{i',i''}|i'\rangle\langle i''|\otimes K_{i'}\rho K_{i''}^\dagger$, projecting the ancilla onto $|i\rangle$ keeps $i'=i''=i$:
$$\Pr[i]=\text{Tr}(K_i\rho K_i^\dagger)=\text{Tr}(K_i^\dagger K_i\,\rho)=\text{Tr}(F_i\rho).$$
This is exactly the POVM's outcome probability. ∎

5. **Post-measurement state** (on the system): $K_i\rho K_i^\dagger/\text{Tr}(F_i\rho)$. Note it depends on the *choice* of $K_i$ — different roots ($K_i'=W_iK_i$, $W_i$ unitary) give the same probabilities but different collapsed states.

### 4. Where the magic happens
**$F_i=K_i^\dagger K_i$ turns "POVM element" into "Kraus operator," and $\sum_iF_i=I$ becomes the isometry condition $V^\dagger V=I$.** Stinespring then provides the unitary, and a *projective* measurement of the ancilla index $i$ reads off $\text{Tr}(F_i\rho)$. The POVM's extra power is just projective measurement seen on a dilated space.

### 5. If he pushes back
- *"How large an ancilla?"* Dimension $n$ (one basis vector per outcome) suffices; if $n>dd'$ the lecture takes $m=d\lceil n/d\rceil$.
- *"Why $\sqrt{F_i}$ specifically?"* Any factorization $F_i=K_i^\dagger K_i$ works for the *probabilities*; $\sqrt{F_i}$ is the canonical (Hermitian) choice. The post-measurement state is the part that depends on this choice.
- *"Does this make POVMs 'no more powerful'?"* For the *statistics*, yes — they're projective measurements in disguise. Operationally they're often more convenient (e.g. unambiguous state discrimination).
