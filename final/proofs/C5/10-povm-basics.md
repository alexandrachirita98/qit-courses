# 10 — POVMs: $\{F_i\ge0\}$ with $\sum_i F_i=I$, outcome probability $\text{Tr}(\rho F_i)$

**Claim.** The most general measurement on $\mathbb C^d$ with outcomes $\{1,\dots,n\}$ is a **POVM**: a collection of operators $\{F_i\}$ with $F_i\ge0$ and $\sum_{i=1}^n F_i=I$. Measuring it on $\rho$ produces outcome $i$ with probability $\text{Tr}(\rho F_i)$.

---

### 1. In plain words
Projective (von Neumann) measurements are the textbook kind, but real detectors are more general. A POVM is the minimal data needed for a measurement to give sensible probabilities: a positive operator $F_i$ per outcome, summing to the identity. Positivity makes probabilities nonnegative; summing to $I$ makes them total 1. The outcome rule is the natural generalization of Born's rule, $\Pr[i]=\text{Tr}(\rho F_i)$.

### 2. Toolbox
- A POVM is a map $F:\mathcal F\to\mathcal B(\mathcal H)$ with $F(\Omega)=I$ such that $\mu_{|\psi\rangle}(E)=\langle\psi|F(E)|\psi\rangle$ is a probability measure for every $|\psi\rangle$.
- Finite outcome set $\Omega=\{1,\dots,n\}$: the measure is determined by $F_i:=F(\{i\})$.
- Probability measure axioms: nonnegativity and additivity, total mass 1.

### 3. The proof (deriving the conditions from "must give probabilities")
1. **Nonnegativity ⇒ $F_i\ge0$.** For every $|\psi\rangle$, $\mu_{|\psi\rangle}(\{i\})=\langle\psi|F_i|\psi\rangle\ge0$. Since this holds for all $|\psi\rangle$, $F_i\ge0$.
2. **Additivity.** For a subset $E\subseteq\Omega$, $\mu_{|\psi\rangle}(E)=\sum_{i\in E}\mu_{|\psi\rangle}(\{i\})=\langle\psi|\big(\sum_{i\in E}F_i\big)|\psi\rangle$, so $F(E)=\sum_{i\in E}F_i$.
3. **Total mass 1 ⇒ $\sum_i F_i=I$.** Take $E=\Omega$: $I=F(\Omega)=\sum_{i=1}^n F_i$.
4. **Outcome rule on mixed states.** Write $\rho=\sum_a p_a|\psi_a\rangle\langle\psi_a|$. Then
$$\Pr[i]=\sum_a p_a\langle\psi_a|F_i|\psi_a\rangle=\sum_a p_a\,\text{Tr}(|\psi_a\rangle\langle\psi_a|F_i)=\text{Tr}(\rho F_i),$$
using [C4/19](../C4/19-two-trace-identities.md) and linearity. ∎

Conversely, any $\{F_i\ge0,\sum_i F_i=I\}$ yields valid probabilities $\text{Tr}(\rho F_i)\ge0$ summing to $\text{Tr}(\rho I)=1$.

### 4. Where the magic happens
**"Give a probability measure for every state" forces exactly two conditions:** positivity of each $F_i$ (nonneg probabilities) and $\sum_i F_i=I$ (they sum to 1). No orthogonality or projector property required — that's the freedom over projective measurements. Born's rule generalizes verbatim to $\text{Tr}(\rho F_i)$.

### 5. If he pushes back
- *"How is this more general than projective measurement?"* Projective: $F_i=E_i$ orthogonal projectors, $E_iE_j=\delta_{ij}E_i$, and at most $d$ outcomes. POVM: the $F_i$ needn't be projectors or orthogonal, and you can have $n>d$ outcomes.
- *"Is it really physical?"* Yes — by Naimark ([11](11-naimark-dilation.md)) every POVM is a projective measurement on a larger (dilated) space, so it's implementable with an ancilla + gate + standard measurement.
- *"What's the post-measurement state?"* Not fixed by the POVM alone — it depends on a choice of Kraus operators $K_i$ with $F_i=K_i^\dagger K_i$ (e.g. $K_i=\sqrt{F_i}$); the state becomes $K_i\rho K_i^\dagger/\text{Tr}(F_i\rho)$, see [11](11-naimark-dilation.md).
