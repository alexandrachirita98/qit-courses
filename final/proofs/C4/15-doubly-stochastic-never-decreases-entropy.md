# 15 — A doubly-stochastic map never decreases Shannon entropy

**Claim.** Let $D$ be a **doubly-stochastic** matrix (entries $\ge0$; every row sums to 1; every column sums to 1) and let $p$ be a probability vector. Then $v:=Dp$ is a probability vector with
$$H(v)\ge H(p),$$
where $H$ is the Shannon entropy. Equivalently: mixing/averaging can only *increase* uncertainty.

---

### 1. In plain words
A doubly-stochastic matrix takes a probability distribution and "smears it out" — it's an average of permutations (Birkhoff's theorem), so it can only make things *more* uniform, never sharper. More uniform = more uncertain = higher entropy. This single lemma is the engine behind two big C4 facts: the von Neumann entropy is the *minimum* measurement entropy ([11](11-von-neumann-entropy-is-the-minimum.md)), and the depolarizing channel can't lower entropy ([18](18-depolarizing-increases-entropy.md)).

### 2. Toolbox
- $\eta(x):=-x\log x$ is **concave** on $[0,1]$ (since $\eta''(x)=-\frac{1}{x\ln 2}<0$). Note $H(p)=\sum_i\eta(p_i)$.
- **Jensen's inequality** for a concave $\eta$ and weights $w_i\ge0$ with $\sum_i w_i=1$:
$$\eta\Big(\sum_i w_i x_i\Big)\ge\sum_i w_i\,\eta(x_i).$$
- Row-stochastic: $\sum_i D_{ki}=1$. Column-stochastic: $\sum_k D_{ki}=1$.

### 3. The proof
Write $v_k=\sum_i D_{ki}\,p_i$.

1. **Each $v_k$ is a weighted average of the $p_i$.** The weights are the $k$-th row $(D_{ki})_i$, which are $\ge0$ and sum to $1$ (**row-stochastic**). So Jensen applies to the concave $\eta$:
$$\eta(v_k)=\eta\Big(\sum_i D_{ki}p_i\Big)\ \ge\ \sum_i D_{ki}\,\eta(p_i).$$
2. **Sum over $k$:**
$$H(v)=\sum_k\eta(v_k)\ \ge\ \sum_k\sum_i D_{ki}\,\eta(p_i)=\sum_i\Big(\underbrace{\sum_k D_{ki}}_{=\,1}\Big)\eta(p_i),$$
where the inner sum is $1$ by **column-stochasticity**.
3. Therefore $H(v)\ge\sum_i \eta(p_i)=H(p)$. ∎

(That $v$ is itself a probability vector: $v_k\ge0$ and $\sum_k v_k=\sum_k\sum_i D_{ki}p_i=\sum_i p_i\cdot\sum_k D_{ki}=\sum_i p_i=1$.)

### 4. Where the magic happens
**The proof uses *both* stochasticity conditions, each once.** Row sums $=1$ make each $v_k$ a genuine average so Jensen fires (concavity ⇒ averaging raises $\eta$). Column sums $=1$ are exactly what's needed to resum $\sum_k D_{ki}=1$ and recover $H(p)$ cleanly. Drop either condition and the inequality can fail. Memorize: **"row sums for Jensen, column sums for the resummation."**

### 5. If he pushes back
- *"Where's majorization in this?"* Equivalent route: $D$ doubly stochastic $\iff$ $v=Dp$ is majorized by $p$ ($v\prec p$), and $H$ is Schur-concave, so $H(v)\ge H(p)$. The Jensen proof above is the self-contained version.
- *"Why must $D$ be doubly stochastic, not just stochastic?"* A merely column-stochastic (classical channel) $D$ can *decrease* entropy — e.g. a deterministic map collapsing everything to one outcome gives $H(v)=0$. Preserving the uniform distribution (the extra "row" condition) is what forbids sharpening.
- *"Equality conditions?"* Jensen is tight when, for each $k$, the $p_i$ with $D_{ki}>0$ are equal — i.e. $D$ just permutes (relabels) $p$. Then $H(v)=H(p)$.
- *"Why does C4 care?"* Because measurement probabilities relate to eigenvalue probabilities by exactly such a $D$ (the matrix of squared overlaps $|\langle\phi_k|\psi_i\rangle|^2$ is doubly stochastic) — that's [11](11-von-neumann-entropy-is-the-minimum.md).
