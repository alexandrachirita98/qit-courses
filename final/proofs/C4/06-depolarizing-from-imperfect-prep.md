# 06 — Imperfect preparation of $|+\rangle$ averages to the depolarizing channel

**Claim.** Suppose we *try* to prepare $|+\rangle$ but the gate is faulty and we actually get
$$|\psi\rangle_{X,Y}=\sqrt{1-X}\,|+\rangle+\sqrt{X}\,e^{2\pi i Y}\,|-\rangle,\qquad X\sim\mathcal U[0,\epsilon],\ Y\sim\mathcal U[0,1].$$
Then the resulting mixed state is
$$\rho=\mathbb{E}\big[\,|\psi_{X,Y}\rangle\langle\psi_{X,Y}|\,\big]=\Big(1-\tfrac\epsilon2\Big)|+\rangle\langle+|+\tfrac\epsilon2|-\rangle\langle-|=\Delta_\epsilon\big(|+\rangle\langle+|\big),$$
where $\Delta_\epsilon(\rho)=(1-\epsilon)\rho+\epsilon\,\frac{I}{d}$ is the **depolarizing channel** ($d=2$).

---

### 1. In plain words
Real hardware is noisy. We aim for the pure state $|+\rangle$ but leak a random amount $X$ of amplitude into the orthogonal $|-\rangle$, with a random phase $Y$. Averaging over this randomness gives a *mixed* state. Two things happen in the average: (1) the random phase $Y$ averages the off-diagonal "coherence" terms to **zero**, and (2) the small leak $X$ moves a little probability ($\epsilon/2$ on average) from $|+\rangle$ to $|-\rangle$. The result is exactly "$|+\rangle$ with a dash of maximally-mixed noise" — the depolarizing channel.

### 2. Toolbox
- Density matrix of a random pure state is the average of its projector ([04](04-density-matrix-properties.md)).
- A projector in the $\{|+\rangle,|-\rangle\}$ basis: $|\psi\rangle\langle\psi|$ has entries $\psi_a\bar\psi_b$.
- Phase averaging: $\displaystyle\int_0^1 e^{\pm2\pi i y}\,dy=0$.
- Mean of a uniform variable: $\mathbb{E}[X]=\epsilon/2$ for $X\sim\mathcal U[0,\epsilon]$.
- $|+\rangle\langle+|+|-\rangle\langle-|=I$ (completeness).

### 3. The proof

Work in the orthonormal basis $\{|+\rangle,|-\rangle\}$. Write $a=\sqrt{1-X}$, $b=\sqrt{X}\,e^{2\pi i Y}$.

1. The projector is
$$|\psi_{X,Y}\rangle\langle\psi_{X,Y}|=\begin{pmatrix}|a|^2 & a\bar b\\ \bar a b & |b|^2\end{pmatrix}=\begin{pmatrix}1-X & \sqrt{X(1-X)}\,e^{-2\pi i Y}\\ \sqrt{X(1-X)}\,e^{2\pi i Y} & X\end{pmatrix}.$$
(Just multiplied out $\psi_a\bar\psi_b$; the $\sqrt{1-X}$ is real.)

2. **Average the off-diagonals over $Y$:** they carry a factor $e^{\pm2\pi i Y}$, and
$$\mathbb{E}_Y\big[e^{\pm2\pi i Y}\big]=\int_0^1 e^{\pm2\pi i y}\,dy=0.$$
So both off-diagonal entries average to $0$ — *the random phase destroys the coherences.*

3. **Average the diagonals over $X$:** with $\mathbb{E}[X]=\epsilon/2$,
$$\mathbb{E}[1-X]=1-\tfrac\epsilon2,\qquad \mathbb{E}[X]=\tfrac\epsilon2.$$

4. Assemble:
$$\rho=\begin{pmatrix}1-\frac\epsilon2 & 0\\ 0 & \frac\epsilon2\end{pmatrix}_{\{|+\rangle,|-\rangle\}}=\Big(1-\tfrac\epsilon2\Big)|+\rangle\langle+|+\tfrac\epsilon2|-\rangle\langle-|.$$

5. **Recognize the depolarizing channel.** Expand the target:
$$\Delta_\epsilon(|+\rangle\langle+|)=(1-\epsilon)|+\rangle\langle+|+\epsilon\tfrac{I}{2}=(1-\epsilon)|+\rangle\langle+|+\tfrac\epsilon2\big(|+\rangle\langle+|+|-\rangle\langle-|\big)$$
$$=\Big(1-\epsilon+\tfrac\epsilon2\Big)|+\rangle\langle+|+\tfrac\epsilon2|-\rangle\langle-|=\Big(1-\tfrac\epsilon2\Big)|+\rangle\langle+|+\tfrac\epsilon2|-\rangle\langle-|=\rho.\quad\blacksquare$$

### 4. Where the magic happens
**A uniformly random phase averages every coherence to zero** ($\int_0^1 e^{2\pi i y}dy=0$). That's what converts a random *pure* state into a genuinely *mixed* one (off-diagonals gone). The leak $X$ then just relabels how much probability sits on $|-\rangle$, giving the clean "signal + $\frac\epsilon2$ noise" form.

### 5. If he pushes back
- *"What if $Y$ were fixed, not random?"* Then the off-diagonals survive and $\rho$ stays **pure** (a rotated $|+\rangle$); you'd get a coherent error, not depolarizing noise. Randomness of the phase is what mixes.
- *"Why call it 'depolarizing'?"* $\Delta_\epsilon$ shrinks the Bloch vector toward the center (maximally mixed $I/2$) by a factor $(1-\epsilon)$; full depolarization $\epsilon=1$ gives $I/2$, total loss of polarization.
- *"Is $\Delta_\epsilon$ really a channel?"* Yes — it's a convex mixture "do nothing with prob $1-\epsilon$, replace by $I/d$ with prob $\epsilon$," which is completely positive and trace preserving (proved properly in C5).
- *"What does this noise do to entropy?"* It can only increase the von Neumann entropy — see [18](18-depolarizing-increases-entropy.md).
