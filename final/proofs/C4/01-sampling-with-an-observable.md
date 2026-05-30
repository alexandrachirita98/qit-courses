# 01 — Sampling a classical distribution with a quantum measurement

**Claim.** Let $W=\sum_{k=1}^d \lambda_k|\phi_k\rangle\langle\phi_k|$ be an observable with orthonormal eigenvectors $\{|\phi_k\rangle\}$ and **distinct** eigenvalues. Measuring $W$ on
$$|\psi\rangle=\sum_i \alpha_i|\phi_i\rangle$$
yields outcome $\lambda_k$ with probability $|\langle\psi|\phi_k\rangle|^2=|\alpha_k|^2$. Consequently, to reproduce a target distribution $(w_1,\dots,w_d)$ there are **infinitely many** states $|\psi\rangle$ that work.

---

### 1. In plain words
We want a quantum gadget that spits out outcome $k$ with a prescribed probability $w_k$ (the "quantum horses": horse $k$ wins with probability $w_k$). Recipe: pick an observable whose eigenvectors $|\phi_k\rangle$ label the outcomes, and prepare a state whose component along $|\phi_k\rangle$ has squared length $w_k$. Born's rule then makes outcome $k$ appear with probability $w_k$. The neat twist: the *phases* of those components don't affect the probabilities at all, so you can dial them however you like — hence infinitely many valid states.

### 2. Toolbox
- **Born's rule (postulate 4):** outcome $\lambda_k$ has probability $\langle\psi|E_{\lambda_k}|\psi\rangle$, where $E_{\lambda_k}=|\phi_k\rangle\langle\phi_k|$ is the projector onto the $\lambda_k$-eigenspace (distinct eigenvalues ⇒ one eigenvector each).
- Orthonormality: $\langle\phi_k|\phi_i\rangle=\delta_{ki}$.
- A state has $\langle\psi|\psi\rangle=1$, i.e. $\sum_k|\alpha_k|^2=1$.

### 3. The proof

**The probability.**
1. $\Pr[\lambda_k]=\langle\psi|\,|\phi_k\rangle\langle\phi_k|\,|\psi\rangle=|\langle\phi_k|\psi\rangle|^2$ — Born's rule with projector $|\phi_k\rangle\langle\phi_k|$; the middle is a number times its conjugate.
2. $\langle\phi_k|\psi\rangle=\langle\phi_k|\sum_i\alpha_i|\phi_i\rangle=\sum_i\alpha_i\langle\phi_k|\phi_i\rangle=\alpha_k$ — expand $|\psi\rangle$, then orthonormality kills all terms but $i=k$.
3. Therefore $\Pr[\lambda_k]=|\alpha_k|^2$. ∎

**Matching a target distribution.** To get $\Pr[\lambda_k]=w_k$, choose
$$\alpha_k=\sqrt{w_k}\,e^{i\theta_k}\quad\text{for any phases }\theta_k.$$
4. Then $|\alpha_k|^2=w_k$ as required, and normalization is automatic: $\sum_k|\alpha_k|^2=\sum_k w_k=1$.
5. The phases $\theta_1,\dots,\theta_d$ are **completely free**, so there is a continuum of solutions. ∎

**Counting the freedom (the slide's "11 vs 6").** A state $|\psi\rangle\in\mathbb{C}^d$ has $2d$ real parameters (real + imaginary parts). Subtract 1 for normalization and 1 for the physically-irrelevant global phase ([13](13-global-vs-relative-phase.md)): $2d-2$ genuine real degrees of freedom. The target imposes only $d-1$ independent constraints (the $d$ numbers $w_k$ sum to 1). For $d\ge2$,
$$2d-2 \;>\; d-1,$$
so the solution set is a positive-dimensional family — infinitely many states. (For $d=6$: $11$ free reals after normalization vs. $6$ constraints, matching the lecture's count.)

### 4. Where the magic happens
**Probabilities see only $|\alpha_k|^2$, never the phase of $\alpha_k$.** So once the magnitudes are pinned by the target distribution, the relative phases are a free gauge — that's the entire source of non-uniqueness. (And it's *relative* phase that's free here, the same freedom that makes [03](03-indistinguishable-iff-same-density-matrix.md) and density matrices necessary.)

### 5. If he pushes back
- *"Why did you need distinct eigenvalues?"* So each outcome $\lambda_k$ corresponds to a single eigenvector and $E_{\lambda_k}=|\phi_k\rangle\langle\phi_k|$. With repeated eigenvalues several $|\phi_k\rangle$ merge into one outcome (a *partial* measurement, see [09](09-distinct-eigenvalues-entropy-independent.md)).
- *"Is the average outcome $\sum_k\lambda_k w_k$ meaningful?"* No — the $\lambda_k$ are arbitrary labels for non-numeric outcomes (horse names), so the mean is gauge-dependent; see [14](14-why-the-average-is-meaningless.md).
- *"What if I only have qubits, not a $d$-level system?"* Round up to $2^{\lceil\log_2 d\rceil}$ dimensions and either leave some outcomes at probability 0 or pack multiple races; the minimal-dimension choice $d$ just gives the simplest formulas.
- *"Could two of your solutions be physically the same?"* If they differ only by a *global* phase, yes (same state). Differing *relative* phases give genuinely different states that merely happen to share this one measurement's statistics.
