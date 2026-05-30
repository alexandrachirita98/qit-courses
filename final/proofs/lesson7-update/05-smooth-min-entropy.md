# 05 — Smooth min-entropy

**Claim.** The $\epsilon$-**smooth** conditional min-entropy maximizes the min-entropy over an $\epsilon$-ball of nearby states:
$$H_{\min}^\epsilon(A|B)_\rho=\max_{\tilde\rho_{AB}\in B^\epsilon(\rho_{AB})}H_{\min}(A|B)_{\tilde\rho},\qquad B^\epsilon(\rho)=\{\tilde\rho\ \text{(sub-normalized)}:\ P(\rho,\tilde\rho)\le\epsilon\}.$$
It satisfies $H_{\min}^\epsilon(A|B)_\rho\ge H_{\min}(A|B)_\rho$.

---

### 1. In plain words
Raw min-entropy is brittle: one tiny "bad" eigenvalue (a rare high-probability spike) can crater it, even if the state is *almost* perfectly uniform. Smoothing fixes this — we're allowed to nudge the state by up to $\epsilon$ (in purified distance) to the *most favorable* nearby state, then take its min-entropy. This ignores negligible-probability pathologies and gives the quantity that actually governs how many secret bits you can extract.

### 2. Toolbox
- Conditional min-entropy $H_{\min}(A|B)$ ([03](03-conditional-min-entropy.md)).
- Purified distance $P$ and its $\epsilon$-ball $B^\epsilon(\rho)$ ([04](04-trace-and-purified-distance.md)).
- "max over a set containing $\rho$" $\ge$ "value at $\rho$".

### 3. The proof
1. The $\epsilon$-ball $B^\epsilon(\rho)$ contains $\rho$ itself (since $P(\rho,\rho)=0\le\epsilon$).
2. $H_{\min}^\epsilon(A|B)_\rho$ is defined as the **maximum** of $H_{\min}(A|B)_{\tilde\rho}$ over $\tilde\rho\in B^\epsilon(\rho)$. A maximum over a set containing $\rho$ is at least the value at $\rho$:
$$H_{\min}^\epsilon(A|B)_\rho\ge H_{\min}(A|B)_\rho.$$
3. Larger $\epsilon$ ⇒ bigger ball ⇒ larger (or equal) smooth min-entropy: it's non-decreasing in $\epsilon$. ∎

### 4. Where the magic happens
**Optimizing over an $\epsilon$-ball discards measure-$\le\epsilon$ "bad parts" of the state.** A single near-deterministic component would otherwise force $H_{\min}$ down to $\approx0$; smoothing lets you delete it (at cost $\epsilon$ in distance) and recover the true extractable randomness. This is *the* entropy that appears in finite-size QKD bounds.

### 5. If he pushes back
- *"Why does QKD use $H_{\min}^\epsilon$ not $H_{\min}$?"* Because real protocols accept a small failure probability $\epsilon$; smoothing builds that tolerance in and gives much better (larger) entropy estimates with experimental estimators.
- *"What's the price of smoothing?"* The final security parameter picks up an additive $\epsilon$ (e.g. $\Delta\le\epsilon+\tfrac12\sqrt{\cdots}$ in the LHL, [08](08-quantum-leftover-hashing.md)).
- *"Is the max attained?"* Yes — $B^\epsilon(\rho)$ is compact (closed, bounded set of sub-normalized states) and $H_{\min}$ is continuous, so the maximum exists.
