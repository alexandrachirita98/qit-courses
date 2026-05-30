# 02 — A $\pm1$ observable satisfies $A^2=I$ (and is both Hermitian and unitary)

**Claim.** If $A$ is a Hermitian observable whose only eigenvalues are $\pm1$, then
$$A^2=I,\qquad \|A\|=1,\qquad A=A^\dagger=A^{-1}.$$

---

### 1. In plain words
A "$\pm1$ observable" is a yes/no-style measurement whose outcomes are labelled $+1$ and $-1$ (e.g. a Pauli $X$, $Y$, $Z$). Squaring it gives the identity because $(\pm1)^2=1$ on every eigenvector. This tiny fact is the lubricant for the whole CHSH computation: wherever $A_a^2$ or $B_b^2$ appears, you replace it by $I$.

### 2. Toolbox
- Spectral decomposition: $A=(+1)P_+ +(-1)P_-$, where $P_\pm$ project onto the $\pm1$ eigenspaces, $P_++P_-=I$, $P_+P_-=0$, $P_\pm^2=P_\pm$.
- Operator norm $\|A\|=\max|\text{eigenvalue}|$ for Hermitian $A$.

### 3. The proof
1. Write $A=P_+-P_-$ (spectral form with eigenvalues $\pm1$).
2. Square it: $A^2=(P_+-P_-)^2=P_+^2-P_+P_--P_-P_++P_-^2$.
3. Use $P_\pm^2=P_\pm$ and $P_+P_-=P_-P_+=0$ (orthogonal eigenspaces): $A^2=P_++P_-=I$. ∎
4. $\|A\|=\max\{|+1|,|-1|\}=1$ — Hermitian norm is the largest absolute eigenvalue.
5. $A^2=I$ together with $A=A^\dagger$ gives $A^\dagger A=A^2=I$, so $A$ is also **unitary** and $A^{-1}=A$. ∎

### 4. Where the magic happens
**$(\pm1)^2=1$ on each eigenvector ⇒ $A^2=I$.** Being simultaneously Hermitian (it's an observable) and unitary ($A^2=I$) is exactly why $\pm1$ observables behave like reflections and make the Tsirelson algebra collapse so neatly.

### 5. If he pushes back
- *"Where is $A^2=I$ used in CHSH?"* In the KTL identity ([05](05-khalfin-tsirelson-landau-identity.md)): $(B_0\pm B_1)^2=2I\pm(B_0B_1+B_1B_0)$ uses $B_0^2=B_1^2=I$.
- *"Why $\|A\|=1$ matters?"* It bounds the commutator norm $\|[A_0,A_1]\|\le2$ ([09](09-commutator-norm-bound.md)), which gives Tsirelson's $2\sqrt2$.
- *"Is every $\pm1$ observable a Pauli?"* No — any reflection $A=UZU^\dagger$ works; Paulis are the canonical examples.
