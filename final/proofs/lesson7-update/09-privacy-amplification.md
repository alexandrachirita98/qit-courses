# 09 — Privacy amplification

**Claim.** After a QKD protocol, Alice and Bob share a **raw key** $X$ about which an eavesdropper $E$ holds quantum side information with conditional min-entropy $H_{\min}(X|E)$. Applying a random two-universal hash $f$ to compress $X$ down to $l$ bits produces a key $Z=f(X)$ that is $\Delta$-close to uniform and independent of $E$, with
$$\Delta=\tfrac12\sqrt{2^{\,l-H_{\min}(X|E)}}\quad(\text{up to smoothing }+\epsilon),$$
which is negligible whenever $l\ll H_{\min}(X|E)$.

---

### 1. In plain words
The raw key after error correction is only *partially* secret: Eve has intercepted some information (and error correction leaked a bit more). Privacy amplification is the final QKD step — squeeze the raw key through a public random hash to a shorter key that Eve knows essentially nothing about. The Quantum Leftover Hashing Lemma guarantees this works: as long as you output fewer bits than Eve's *uncertainty* $H_{\min}(X|E)$, the result is indistinguishable from a fresh uniform key, even to a quantum Eve.

### 2. Toolbox
- Quantum Leftover Hashing Lemma ([08](08-quantum-leftover-hashing.md)): $\Delta=\tfrac12\sqrt{2^{l-H_{\min}(X|E)}}$.
- "$\Delta$-close to uniform given $E$": $\tfrac12\|\rho_{ZE}-\omega_Z\otimes\sigma_E\|_{\text{Tr}}\le\Delta$ with $\omega_Z=I/2^l$.
- $H_{\min}(K|E)\approx0$ ⇒ Eve can guess $K$; $\rho_{KE}\approx\omega_Z\otimes\rho_E$ ⇒ secret.
- Finite-key estimate of $H_{\min}^\epsilon(X|E)$ from measured error rate ([../C6/13-bb84-security.md](../C6/13-bb84-security.md)).

### 3. The argument
1. **Set up the joint state.** After error correction, model the situation as $\rho_{XE}$: classical raw key $X$ plus Eve's quantum memory $E$. Eve's knowledge is quantified by $H_{\min}(X|E)$ — small if she intercepted a lot, large if she's ignorant.
2. **Apply a random two-universal hash** $f:X\mapsto Z\in\{0,1\}^l$ (the hash choice can be public). By the **Quantum Leftover Hashing Lemma** ([08](08-quantum-leftover-hashing.md)),
$$\tfrac12\big\|\rho_{ZE}-\omega_Z\otimes\sigma_E\big\|_{\text{Tr}}\le\tfrac12\sqrt{2^{\,l-H_{\min}(X|E)}}=\Delta.$$
3. **Choose the output length.** Pick $l\le H_{\min}^\epsilon(X|E)-2\log\tfrac1{\Delta'}$ so $\Delta$ (plus smoothing $\epsilon$) is below the target security level. Then $\rho_{ZE}\approx\omega_Z\otimes\sigma_E$ — the final key $Z$ is uniform **and** uncorrelated with Eve.
4. **Security meaning.** By the operational meaning of trace distance ([../C7/01-helstrom-bound.md](../C7/01-helstrom-bound.md)), Eve cannot distinguish the real key from an ideal uniform secret key with advantage exceeding $\Delta$ — a *composable* security guarantee (a $\Delta$-secret key, cf. the $\Delta$-secret scenario of standard Lecture 7). ∎

### 4. Where the magic happens
**Privacy amplification = randomness extraction with Eve as the side information $E$.** The Quantum Leftover Hashing Lemma converts "Eve's uncertainty $H_{\min}(X|E)$" directly into "secret bits you can safely output ($l<H_{\min}(X|E)$)." You trade key length for secrecy, and the exponential $2^{l-H_{\min}(X|E)}$ makes the leftover correlation vanish fast.

### 5. If he pushes back
- *"Why hash instead of just dropping bits?"* Eve's information might be spread across many bits unpredictably; a random hash mixes all of $X$, removing any structured partial knowledge — dropping fixed bits would not.
- *"Is the public hash a problem?"* No — the lemma holds *on average over a public $f$*; revealing $f$ doesn't help Eve.
- *"Concrete numbers?"* From [../C6/13-bb84-security.md](../C6/13-bb84-security.md): at $1\%$ error, after sending parity checks Eve's chance to share a 256-bit key is $\sim10^{-23}$ — that smallness *is* $\Delta$.
- *"What guarantees $H_{\min}(X|E)$ is large?"* The uncertainty relations of [../C6](../C6/13-bb84-security.md): low measured error ⇒ Eve's uncertainty high ⇒ $H_{\min}(X|E)$ large.
