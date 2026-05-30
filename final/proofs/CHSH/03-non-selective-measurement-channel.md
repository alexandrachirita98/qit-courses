# 03 — Non-selective measurement maps $\rho\mapsto\sum_\lambda E_\lambda\,\rho\,E_\lambda$

**Claim.** Measuring observable $O=\sum_\lambda\lambda E_\lambda$ on $\rho$ and **discarding** the outcome leaves the state
$$\rho'=\sum_\lambda E_\lambda(O)\,\rho\,E_\lambda(O),$$
where $E_\lambda(O)$ is the projector onto the $\lambda$-eigenspace.

---

### 1. In plain words
If you measure but don't look at (or forget) the result, the state becomes a *probabilistic mixture* of all the possible collapsed states, weighted by how likely each was. Miraculously, the probabilities and the normalization constants cancel exactly, leaving the clean "sandwich each projector around $\rho$ and add" formula. This is the prototype of a quantum channel.

### 2. Toolbox
- Collapse rule (postulate 5): on outcome $\lambda$ from $|\xi_k\rangle$, the state becomes $|v'\rangle\propto E_\lambda|\xi_k\rangle$, normalized.
- Outcome $\lambda$ from $|\xi_k\rangle$ has probability $\|E_\lambda|\xi_k\rangle\|^2=\langle\xi_k|E_\lambda|\xi_k\rangle$ (projectors satisfy $E_\lambda^\dagger E_\lambda=E_\lambda^2=E_\lambda$).
- $\rho=\sum_k p_k|\xi_k\rangle\langle\xi_k|$.

### 3. The proof
Suppose $\rho=\sum_k p_k|\xi_k\rangle\langle\xi_k|$. Track the joint randomness over (which $|\xi_k\rangle$ we had) and (which $\lambda$ we got).

1. Outcome $\lambda$ from $|\xi_k\rangle$ has joint probability $q_{k,\lambda}=p_k\,\langle\xi_k|E_\lambda|\xi_k\rangle$.
2. The resulting normalized state is $|v'\rangle=\dfrac{E_\lambda|\xi_k\rangle}{\|E_\lambda|\xi_k\rangle\|}$, so its projector is
$$|v'\rangle\langle v'|=\frac{E_\lambda|\xi_k\rangle\langle\xi_k|E_\lambda}{\langle\xi_k|E_\lambda|\xi_k\rangle}.$$
(Used $\|E_\lambda|\xi_k\rangle\|^2=\langle\xi_k|E_\lambda|\xi_k\rangle$.)
3. Average over all branches:
$$\rho'=\sum_{k,\lambda}q_{k,\lambda}\,|v'\rangle\langle v'|=\sum_{k,\lambda}p_k\,\langle\xi_k|E_\lambda|\xi_k\rangle\cdot\frac{E_\lambda|\xi_k\rangle\langle\xi_k|E_\lambda}{\langle\xi_k|E_\lambda|\xi_k\rangle}.$$
4. **The normalization cancels** the probability factor:
$$\rho'=\sum_{k,\lambda}p_k\,E_\lambda|\xi_k\rangle\langle\xi_k|E_\lambda=\sum_\lambda E_\lambda\Big(\sum_k p_k|\xi_k\rangle\langle\xi_k|\Big)E_\lambda=\sum_\lambda E_\lambda\,\rho\,E_\lambda.\qquad\blacksquare$$

### 4. Where the magic happens
**The Born probability $\langle\xi_k|E_\lambda|\xi_k\rangle$ in the numerator is exactly the denominator that normalizes the collapsed state — they cancel.** What's left is basis-free ($\sum_k p_k|\xi_k\rangle\langle\xi_k|=\rho$ reassembles), so the map depends only on $\rho$ and the projectors $E_\lambda$.

### 5. If he pushes back
- *"Is this a valid quantum channel?"* Yes — it's a Kraus map with operators $\{E_\lambda\}$, and $\sum_\lambda E_\lambda^\dagger E_\lambda=\sum_\lambda E_\lambda=I$ (complete), so it's CPTP. The instrument version that *keeps* $\lambda$ is [04](04-observable-as-quantum-instrument.md).
- *"What if eigenvalues are degenerate?"* $E_\lambda$ projects onto a multi-dimensional eigenspace; the formula is unchanged. Post-measurement superpositions survive *within* each eigenspace (a partial measurement, cf. [C4/09](../C4/09-distinct-eigenvalues-entropy-independent.md)).
- *"Difference from selective measurement?"* Selective keeps one branch $E_\lambda\rho E_\lambda/\Pr[\lambda]$; non-selective averages all branches. This map is sometimes written $\Delta_O(\rho)$, a dephasing in $O$'s eigenbasis.
