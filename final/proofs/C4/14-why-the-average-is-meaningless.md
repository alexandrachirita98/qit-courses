# 14 — Why the average of non-numeric outcomes carries no physics

**Claim.** When an observable's eigenvalues $\lambda_k$ are arbitrary labels for *qualitatively distinct* outcomes (horse A, B, C, …), the mean $\langle O\rangle=\sum_k\lambda_k v_k$ and the variance $\Delta O^2$ are **not physical**: they change if you relabel the outcomes, even though the experiment is identical. The physically meaningful content is the outcome distribution $\{v_k\}$ itself (and label-invariant functions of it, such as the Shannon entropy).

---

### 1. In plain words
"What's the average winning horse?" is a nonsense question: it depends on whether you numbered the horses A=1,B=2,… or A=10,B=−3,…. The quantum formalism *forces* you to attach real numbers (eigenvalues) to outcomes, but for non-numeric outcomes those numbers are a free choice — a gauge. Any quantity that moves when you change the gauge is an artifact, not physics. The probabilities $v_k=\langle\phi_k|\rho|\phi_k\rangle$ don't move (they're fixed by the state and the basis), so *they* — and the entropy built from them — are the real content.

### 2. Toolbox
- Outcome probabilities $v_k=\langle\phi_k|\rho|\phi_k\rangle$ depend on $\rho$ and the basis $\{|\phi_k\rangle\}$ **only** — not on the eigenvalues ([19](19-two-trace-identities.md)).
- Mean $\langle O\rangle=\sum_k\lambda_k v_k$, variance $\Delta O^2=\sum_k\lambda_k^2v_k-\langle O\rangle^2$ ([08](08-mean-and-variance-depend-on-eigenvalues.md)).
- A "relabeling" replaces the distinct values $\lambda_k$ by any other distinct values $\lambda_k'$, **keeping the eigenvectors fixed**.
- Shannon entropy $H(O)=-\sum_k v_k\log v_k$ uses only $\{v_k\}$ ([09](09-distinct-eigenvalues-entropy-independent.md)).

### 3. The proof

**The mean is gauge-dependent.**
1. Fix the state and the measurement basis, so the probabilities $\{v_k\}$ are fixed.
2. Relabel: choose new distinct eigenvalues $\lambda_k'$ (same eigenvectors). The new mean is $\langle O'\rangle=\sum_k\lambda_k'v_k$.
3. In general $\sum_k\lambda_k'v_k\neq\sum_k\lambda_k v_k$ — e.g. shift all labels by a constant $c$: $\lambda_k'=\lambda_k+c$ gives $\langle O'\rangle=\langle O\rangle+c$, which differs for any $c\ne0$. So the mean is **not** determined by the physics; it tracks the arbitrary labels.
4. Same for the variance: scaling $\lambda_k'=s\lambda_k$ gives $\Delta O'^2=s^2\Delta O^2$ — rescalable to anything. (The $d=3$ example in [08](08-mean-and-variance-depend-on-eigenvalues.md) even makes its $\epsilon$-monotonicity an artifact.)

**The distribution and its entropy are gauge-invariant.**
5. Under relabeling, $\{v_k\}$ is unchanged (Step 1), so any function of $\{v_k\}$ alone is unchanged. In particular $H(O)=-\sum_k v_k\log v_k$ is invariant.
6. Therefore the honest "amount of randomness" in the experiment is carried by $\{v_k\}$ / $H(O)$, not by $\langle O\rangle$ or $\Delta O^2$. ∎

### 4. Where the magic happens
**Separate what the experiment fixes (the probabilities $v_k$) from what you chose by hand (the labels $\lambda_k$).** Mean and variance mix the two, so they inherit the arbitrariness of the labels. Entropy depends only on the fixed part, so it's the physically meaningful uncertainty measure. Slogan: *probabilities are physics; eigenvalues are bookkeeping.*

### 5. If he pushes back
- *"So variance is always meaningless?"* No — only when eigenvalues are arbitrary labels. For a genuine physical observable (energy, position, spin-$z$), the eigenvalues are nature-given, the labels aren't free, and variance is meaningful (Heisenberg).
- *"Why does QM even let me pick the eigenvalues?"* Postulate 2 only requires an observable to be Hermitian; you're free to identify outcomes with any real numbers. For sampling a categorical distribution ([01](01-sampling-with-an-observable.md)) the values are pure convention.
- *"Is the entropy the *only* invariant?"* Any symmetric function of the probabilities is invariant (e.g. Rényi entropies, collision probability). Entropy is the chosen uncertainty measure because of its operational meaning (compression, uncertainty relations).
