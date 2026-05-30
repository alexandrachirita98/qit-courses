# 07 — Tsirelson is sharp: anticommuting observables reach $2\sqrt2$

**Claim.** The bound $|\langle S\rangle|=2\sqrt2$ is achieved. It requires both pairs to **anticommute** ($A_0A_1=-A_1A_0$, $B_0B_1=-B_1B_0$). An explicit qubit construction: $A_0=Z$, $A_1=X$, $B_0=UZU^\dagger$, $B_1=UXU^\dagger$, on a suitable entangled state.

---

### 1. In plain words
To max out CHSH you need the most incompatible local measurements possible — pairs that anticommute, like $Z$ and $X$. Then both commutators in the KTL identity hit their max norm 2, $S^2$ reaches $8I$, and choosing the state to be the top eigenvector of $S$ gives $\langle S\rangle=2\sqrt2$. The construction shows you can always manufacture a second anticommuting pair by conjugating $\{Z,X\}$ with any unitary $U$.

### 2. Toolbox
- $S^2\preceq8I$, with equality on the top eigenspace requiring $\|[A_0,A_1]\|=\|[B_0,B_1]\|=2$ ([06](06-tsirelson-bound.md), [09](09-commutator-norm-bound.md)).
- Anticommutation gives max commutator norm ([09](09-commutator-norm-bound.md)).
- $ZX-XZ=2iY$; conjugation preserves algebra: $(UZU^\dagger)(UXU^\dagger)=U(ZX)U^\dagger$.
- $\langle S\rangle=2\sqrt2$ iff $\rho$ is supported on the top eigenspace of $S$ (eigenvalue $2\sqrt2$).

### 3. The proof

**Why anticommutation is needed.** To reach $\|S\|=2\sqrt2$ we need $\|S^2\|=8$, i.e. the correction $[A_0,A_1]\otimes[B_0,B_1]$ must have norm 4, i.e. each commutator must have norm 2 — which ([09](09-commutator-norm-bound.md)) means each pair anticommutes.

**Build a second anticommuting pair.**
1. $\{Z,X\}$ anticommute: $ZX=-XZ$ (since $ZX-XZ=2iY$ and $ZX+XZ=0$).
2. For any unitary $U$, set $B_0=UZU^\dagger$, $B_1=UXU^\dagger$. Then
$$B_0B_1=UZU^\dagger UXU^\dagger=U(ZX)U^\dagger=-U(XZ)U^\dagger=-B_1B_0,$$
so $\{B_0,B_1\}$ also anticommute, and $[B_0,B_1]=U(2iY)U^\dagger$ has norm 2. ✓

**Achieve the value.** Take $A_0=Z,A_1=X,B_0=UZU^\dagger,B_1=UXU^\dagger$.
3. The slide computes $S=(I\otimes U)(Z\otimes Z+Z\otimes X+X\otimes Z-X\otimes X)(I\otimes U^\dagger)$, and the middle $4\times4$ matrix has eigenvalues $\pm2\sqrt2$ (its top eigenvector is a Bell-like state $|\phi_+\rangle$).
4. Concretely with $U=I$ and shared state $|\phi_+\rangle$ (top eigenvector of $Z\otimes Z+Z\otimes X+X\otimes Z-X\otimes X$), $\langle S\rangle=2\sqrt2$. ∎

### 4. Where the magic happens
**Conjugating an anticommuting pair by any unitary keeps it anticommuting** ($U(\cdot)U^\dagger$ preserves products), so anticommuting "measurement settings" are plentiful. Saturating both commutators at norm 2 and sitting on $S$'s top eigenvector is what turns the $\preceq 8I$ bound into an equality.

### 5. If he pushes back
- *"Which entangled state?"* The eigenvector of $S$ with eigenvalue $+2\sqrt2$; for the standard settings it's a maximally entangled (Bell) state. Maximal violation needs maximal entanglement here.
- *"Can a product (unentangled) state reach $2\sqrt2$?"* No — it can't even pass 2 ([10](10-separable-states-obey-classical-bound.md)). You need entanglement.
- *"Real angle settings?"* The famous choice: Alice measures at $0°,45°$ and Bob at $22.5°,67.5°$ on the Bloch sphere — exactly anticommuting-friendly directions giving $2\sqrt2$.
