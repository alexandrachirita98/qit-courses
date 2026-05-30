# 08 — The Quantum Leftover Hashing Lemma

**Claim.** Let $X$ be a classical random variable, $E$ a **quantum** system (side information), and $\mathcal F$ a $\delta$-almost two-universal family of hash functions $X\to\{0,1\}^l$. Then, on average over $f\in\mathcal F$, the output $Z=f(X)$ is $\Delta$-close to uniform conditioned on $E$:
$$\Delta=\inf_{\epsilon>0}\ \frac12\sqrt{(2^l\delta-1)+2^{\,l-H_{\min}^\epsilon(X|E)+\log(\frac{2}{\epsilon^2}+1)}}\ +\ \epsilon.$$
If $\mathcal F$ is genuinely two-universal ($\delta\le2^{-l}$), this simplifies to
$$\Delta=\frac12\sqrt{2^{\,l-H_{\min}(X|E)}}.$$

---

### 1. In plain words
The classical Leftover Hashing Lemma ([07](07-classical-leftover-hashing.md)) survives when the eavesdropper holds *quantum* side information $E$ — you just replace the classical conditional min-entropy by the (smooth) quantum conditional min-entropy. The smoothing parameter $\epsilon$ and the $\delta$-almost slack appear as correction terms, but in the clean two-universal case the bound is the same elegant $\tfrac12\sqrt{2^{l-H_{\min}(X|E)}}$. This is the theorem that makes privacy amplification provably secure against a quantum adversary.

### 2. Toolbox
- $\Delta$-close to uniform given $E$ means $\tfrac12\|\rho_{ZE}-\omega_Z\otimes\sigma_E\|_{\text{Tr}}\le\Delta$ for some $\sigma_E$, with $\omega_Z=I_Z/2^l$ ([04](04-trace-and-purified-distance.md)).
- Quantum conditional (smooth) min-entropy $H_{\min}(X|E)$, $H_{\min}^\epsilon(X|E)$ ([03](03-conditional-min-entropy.md), [05](05-smooth-min-entropy.md)).
- $\delta$-almost two-universality ([06](06-two-universal-hashing.md)).
- A quantum collision/$\ell_2$ estimate (the quantum analogue of [07](07-classical-leftover-hashing.md)'s step 2).

### 3. The proof (structure)
The proof mirrors the classical one ([07](07-classical-leftover-hashing.md)) with quantum collision quantities; here is the skeleton.
1. **Quantum $\ell_2$ (collision) bound.** Define the conditional "collision operator" and bound it using $\delta$-almost two-universality:
$$\text{(quantum collision)}\ \le\ \delta+2^{-H_{\min}(X|E)}\quad(\text{cf. }2^{-l}+2^{-H_{\min}}\text{ classically}).$$
2. **$\ell_2\to\ell_1$ (trace norm).** Convert the collision/$\ell_2$ bound on $\rho_{ZE}-\omega_Z\otimes\sigma_E$ into a trace-distance bound, picking up the $\sqrt{2^l}$ dimension factor:
$$\tfrac12\|\rho_{ZE}-\omega_Z\otimes\sigma_E\|_{\text{Tr}}\le\tfrac12\sqrt{(2^l\delta-1)+2^{\,l-H_{\min}(X|E)}}.$$
3. **Smoothing.** Replace $H_{\min}$ by the smooth $H_{\min}^\epsilon$ (optimize over the $\epsilon$-ball, [05](05-smooth-min-entropy.md)); this is only valid up to an additive $+\epsilon$ in trace distance and contributes the $\log(\tfrac2{\epsilon^2}+1)$ correction. Taking $\inf_{\epsilon>0}$ gives the stated $\Delta$.
4. **Two-universal simplification.** If $\delta\le2^{-l}$ then $2^l\delta-1\le0$, the correction term drops, and (without needing to smooth) $\Delta=\tfrac12\sqrt{2^{\,l-H_{\min}(X|E)}}$. ∎

### 4. Where the magic happens
**Quantum side information changes essentially nothing structurally: collision probability still controls trace distance, and the only new quantity is the quantum conditional min-entropy $H_{\min}(X|E)$.** Two-universality kills the $2^l\delta-1$ term, recovering the clean classical-looking bound — now provably secure even if Eve is a quantum computer.

### 5. If he pushes back
- *"Why is the quantum case harder than classical?"* The "distance to uniform" is now a trace norm on operators, and you need the quantum $\ell_2$/collision estimate plus smoothing; conceptually it's the same collision-bounds-uniformity idea.
- *"What does $\Delta$ mean operationally?"* By Helstrom/trace distance ([../C7/01-helstrom-bound.md](../C7/01-helstrom-bound.md)), even Eve's *optimal* test cannot distinguish the real key+side-info from ideal (uniform key ⊗ her state) with advantage more than $\Delta$.
- *"How is $H_{\min}^\epsilon(X|E)$ obtained in practice?"* From the measured error rate via an estimator (the BB84 finite-key bound, [../C6/13-bb84-security.md](../C6/13-bb84-security.md)).
