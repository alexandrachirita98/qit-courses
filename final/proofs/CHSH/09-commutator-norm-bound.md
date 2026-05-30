# 09 — For $\pm1$ observables, $\|[A_0,A_1]\|\le 2$ (equality iff anticommuting)

**Claim.** If $A_0,A_1$ are $\pm1$ observables then $\|[A_0,A_1]\|=\|A_0A_1-A_1A_0\|\le 2$, with equality exactly when $A_0A_1=-A_1A_0$ (they anticommute).

---

### 1. In plain words
Each $\pm1$ observable has operator norm 1 (it's a reflection). A commutator of two norm-1 operators can't be longer than $1+1=2$ by the triangle inequality. The maximum, 2, is reached precisely when the two reflections are "as incompatible as possible" — when swapping their order flips the sign (anticommutation), like $Z$ and $X$. This is the quantity that, squared and tensored, produces Tsirelson's $2\sqrt2$.

### 2. Toolbox
- $\|A_0\|=\|A_1\|=1$ ([02](02-pm1-observables-square-to-identity.md)).
- Submultiplicativity & triangle inequality of the operator norm: $\|XY\|\le\|X\|\|Y\|$, $\|X+Y\|\le\|X\|+\|Y\|$.
- Anticommuting case: $A_0A_1=-A_1A_0\Rightarrow[A_0,A_1]=2A_0A_1$; and $A_0A_1$ is unitary (product of unitaries) so $\|A_0A_1\|=1$.

### 3. The proof

**Upper bound.**
1. $\|[A_0,A_1]\|=\|A_0A_1-A_1A_0\|\le\|A_0A_1\|+\|A_1A_0\|$ — triangle inequality.
2. $\le\|A_0\|\|A_1\|+\|A_1\|\|A_0\|=1\cdot1+1\cdot1=2$ — submultiplicativity + norm 1. ∎

**Equality (anticommuting).**
3. If $A_0A_1=-A_1A_0$ then $[A_0,A_1]=A_0A_1-A_1A_0=2A_0A_1$.
4. $A_0A_1$ is a product of two unitaries ([02](02-pm1-observables-square-to-identity.md)), hence unitary, so $\|A_0A_1\|=1$ and $\|[A_0,A_1]\|=2\|A_0A_1\|=2$. ∎

(Conversely, equality in the triangle inequality forces $A_0A_1$ and $-A_1A_0$ to be "aligned," which for these reflections means anticommutation; the explicit construction in [07](07-tsirelson-sharpness.md) realizes it.)

### 4. Where the magic happens
**Norm-1 reflections ⇒ commutator $\le 2$ by the triangle inequality; anticommutation makes the two pieces add coherently to hit 2.** Plugging $\|[A_0,A_1]\|=\|[B_0,B_1]\|=2$ into the KTL identity ([05](05-khalfin-tsirelson-landau-identity.md)) is what saturates Tsirelson.

### 5. If he pushes back
- *"Concretely for $Z,X$?"* $[Z,X]=ZX-XZ=2iY$, and $\|2iY\|=2\|Y\|=2$. Saturated.
- *"Why does this give $S^2\le 8I$?"* $\|[A_0,A_1]\otimes[B_0,B_1]\|=\|[A_0,A_1]\|\,\|[B_0,B_1]\|\le4$, so $S^2=4I-(\text{op of norm}\le4)\preceq 8I$.
- *"Is $[A_0,A_1]$ Hermitian?"* No — it's anti-Hermitian ($[A_0,A_1]^\dagger=-[A_0,A_1]$). That's fine; we only need its norm. (E.g. $2iY$.)
