# 12 — The Maassen–Uffink uncertainty relation (the big one)

**Claim.** For two basis observables $O=\{|\phi_k\rangle\}$ and $O'=\{|\xi_k\rangle\}$ (distinct eigenvalues) and **any** state $\rho$,
$$\boxed{\,H(O)+H(O')\ \ge\ -\log\max_{k,j}|\langle\phi_k|\xi_j\rangle|^2\,}$$
The right side ("$-\log$ of the maximal overlap $c^2$") is the uncertainty lower bound: you cannot be certain about two sufficiently different observables at once.

---

### 1. In plain words
If two measurements are "incompatible" (their bases are tilted relative to each other), you can't predict both sharply. Maassen–Uffink makes this quantitative: the *sum* of the two measurement entropies is bounded below by a number that grows as the bases become more unlike each other. The proof is a clever detour: instead of attacking Shannon entropy directly, we prove the inequality for a whole family of **Rényi entropies** $H_\alpha$, using one analysis tool (the **Riesz–Thorin interpolation theorem**) to bound how a unitary stretches vector norms, then take the limit $\alpha\to1$ to land back on Shannon entropy.

### 2. Setup and toolbox
- The two bases are related by a unitary: $|\xi_k\rangle=U|\phi_k\rangle$. Define the overlap matrix $U_{k,j}=\langle\xi_k|\phi_j\rangle$ and $c:=\max_{k,j}|U_{k,j}|=\max_{k,j}|\langle\phi_k|\xi_j\rangle|$.
- Measuring a **pure** $|\psi\rangle$: amplitudes $x_k=\langle\phi_k|\psi\rangle$ (probabilities $|x_k|^2$) and $y_k=\langle\xi_k|\psi\rangle$ (probabilities $|y_k|^2$). Key link: $y_k=\sum_j U_{k,j}x_j$, i.e. $y=Ux$.
- **Rényi entropy** $H_\alpha(p)=\frac{1}{1-\alpha}\log\sum_k p_k^\alpha$; as $\alpha\to1$, $H_\alpha\to H$ (Shannon). For measurement probabilities $p_k=|x_k|^2$:
$$H_\alpha(O)=\frac{1}{1-\alpha}\log\sum_k|x_k|^{2\alpha}=\frac{2\alpha}{1-\alpha}\log\|x\|_{2\alpha},$$
where $\|x\|_p=(\sum_k|x_k|^p)^{1/p}$.
- **$p$-norms**, the relation $\frac{1}{2\alpha}+\frac{1}{2\beta}=1$ (i.e. $\frac1\alpha+\frac1\beta=2$; "harmonic conjugates").
- **Riesz–Thorin (black box):** if a linear map $U$ sends $\ell^{p_0}\!\to\ell^{q_0}$ with norm $M_0$ and $\ell^{p_1}\!\to\ell^{q_1}$ with norm $M_1$, then for the interpolated exponents ($\frac1{p_\theta}=\frac{1-\theta}{p_0}+\frac{\theta}{p_1}$, similarly $q_\theta$) the norm satisfies $\|U\|_{p_\theta\to q_\theta}\le M_0^{1-\theta}M_1^{\theta}$.
- Shannon entropy $H$ is **concave** (to lift from pure to mixed states).

### 3. The proof

**Step 1 — entropies as norms.** As above,
$$H_\alpha(O)=\frac{2\alpha}{1-\alpha}\log\|x\|_{2\alpha},\qquad H_\beta(O')=\frac{2\beta}{1-\beta}\log\|y\|_{2\beta}=\frac{2\beta}{1-\beta}\log\|Ux\|_{2\beta}.$$
So everything reduces to comparing $\|Ux\|_{2\beta}$ with $\|x\|_{2\alpha}$.

**Step 2 — bound $U$ at two extreme exponent pairs.**
- At $p_0=q_0=2$: $U$ is **unitary**, so $\|Ux\|_2=\|x\|_2$ ⇒ operator norm $M_0=1$.
- At $p_1=1,\ q_1=\infty$: $\|Ux\|_\infty=\max_k|\sum_j U_{k,j}x_j|\le\max_{k,j}|U_{k,j}|\sum_j|x_j|=c\,\|x\|_1$ ⇒ operator norm $M_1\le c$.

**Step 3 — interpolate (Riesz–Thorin).** Choose $\theta=1-\frac1\beta$. Then the interpolated exponents are
$$\frac{1}{q_\theta}=\frac{1-\theta}{2}=\frac{1}{2\beta}\ \Rightarrow\ q_\theta=2\beta,\qquad \frac{1}{p_\theta}=\frac{1-\theta}{2}+\theta=\frac{1+\theta}{2}=\frac{1}{2\alpha}\ \Rightarrow\ p_\theta=2\alpha,$$
where the last equality used $\frac1\alpha=1+\theta=2-\frac1\beta$, i.e. exactly the harmonic-conjugate condition. Riesz–Thorin gives
$$\|U\|_{2\alpha\to2\beta}\le M_0^{1-\theta}M_1^{\theta}\le 1^{\,1-\theta}c^{\theta}=c^{\,1-1/\beta},$$
so
$$\|Ux\|_{2\beta}\ \le\ c^{\,1-1/\beta}\,\|x\|_{2\alpha}.$$

**Step 4 — turn the norm bound back into entropies.** Take $\log$:
$$\log\|Ux\|_{2\beta}\le\Big(1-\tfrac1\beta\Big)\log c+\log\|x\|_{2\alpha}.$$
Substitute $\log\|x\|_{2\alpha}=\frac{1-\alpha}{2\alpha}H_\alpha(O)$ and $\log\|Ux\|_{2\beta}=\frac{1-\beta}{2\beta}H_\beta(O')$:
$$\frac{1-\beta}{2\beta}H_\beta(O')\le\Big(1-\tfrac1\beta\Big)\log c+\frac{1-\alpha}{2\alpha}H_\alpha(O).$$

**Step 5 — the coefficients magically match.** Using $\frac{1}{2\alpha}=1-\frac{1}{2\beta}$:
$$\frac{1-\alpha}{2\alpha}=\frac{1}{2\alpha}-\frac12=\frac12-\frac{1}{2\beta}=:A,\qquad -\frac{1-\beta}{2\beta}=\frac12-\frac{1}{2\beta}=A,\qquad 1-\tfrac1\beta=2A.$$
Rearranging Step 4 with these:
$$A\,H_\alpha(O)+A\,H_\beta(O')\ \ge\ -2A\log c.$$
Since $A=\frac12-\frac1{2\beta}>0$ for $\beta>1$, divide by $A$:
$$H_\alpha(O)+H_\beta(O')\ \ge\ -2\log c=-\log c^2=-\log\max_{k,j}|\langle\phi_k|\xi_j\rangle|^2.$$

**Step 6 — limit to Shannon.** Let $\alpha,\beta\to1$ (allowed: $\frac1\alpha+\frac1\beta=2$ is satisfied in the limit). Then $H_\alpha\to H$, giving
$$H(O)+H(O')\ \ge\ -\log\max_{k,j}|\langle\phi_k|\xi_j\rangle|^2\qquad\text{for every pure }|\psi\rangle.$$

**Step 7 — extend to mixed $\rho=\sum_i p_i|\psi_i\rangle\langle\psi_i|$.** The measurement distribution of $\rho$ is the mixture of the pure ones, and $H$ is **concave**, so $H(O)_\rho\ge\sum_i p_iH(O)_{|\psi_i\rangle}$ and likewise for $O'$. Summing the per-state bound:
$$H(O)_\rho+H(O')_\rho\ \ge\ \sum_i p_i\big[H(O)_i+H(O')_i\big]\ \ge\ \sum_i p_i\big(-\log c^2\big)=-\log c^2.\qquad\blacksquare$$

### 4. Where the magic happens
**Riesz–Thorin interpolation between two facts about $U$:** it's *norm-preserving* at $p=2$ (unitarity) and *entrywise bounded* at $p=1\!\to\!\infty$ (max overlap $c$). Interpolating these trades off into the exact $2\alpha\!\to\!2\beta$ bound $c^{1-1/\beta}$. The second piece of magic is **Step 5**: the harmonic-conjugate condition $\frac1\alpha+\frac1\beta=2$ forces the two entropy coefficients to be *equal*, so after dividing you get the clean symmetric sum $H_\alpha+H_\beta$. Memorize those two beats — "interpolate unitary vs. max-overlap" and "conjugacy equalizes the coefficients."

### 5. If he pushes back
- *"Why Rényi and not Shannon directly?"* Shannon entropy isn't a norm; Rényi entropy *is* (a log of a $p$-norm), so the interpolation machinery applies. Shannon is recovered as the $\alpha\to1$ limit.
- *"When is the bound zero / maximal?"* Zero iff the bases share an eigenvector (max overlap $=1$); maximal ($\log d$) iff the bases are complementary/MUB (every overlap $=1/d$). Proof in [16](16-maassen-uffink-zero-and-maximal.md).
- *"Why does concavity (not convexity) extend it to mixed states?"* Mixing states *increases* entropy, $H(\text{mixture})\ge\text{mixture of }H$, so the mixed-state LHS is *at least* the average of pure-state LHSs, each already $\ge -\log c^2$.
- *"Relation to Heisenberg's $\Delta x\,\Delta p$?"* This is the *entropic* uncertainty relation — it uses entropy instead of variance, so it's free of the label/variance pathologies ([08](08-mean-and-variance-depend-on-eigenvalues.md)) and is the form used in QKD security proofs.
- *"What's $c$ for $Z$ and $X$ on a qubit?"* $|\langle 0|+\rangle|^2=\tfrac12$, so $-\log\tfrac12=1$ bit: $H(Z)+H(X)\ge1$.
