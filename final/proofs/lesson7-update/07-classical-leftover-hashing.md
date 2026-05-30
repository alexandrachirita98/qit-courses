# 07 — Randomness extraction & the classical Leftover Hashing Lemma

**Claim.**
- A function $\text{Ext}:\{0,1\}^n\times\{0,1\}^d\to\{0,1\}^m$ is a **$(k,\varepsilon)$-extractor** if, for every source $X$ with $H_{\min}(X)\ge k$ and an independent uniform seed $U_d$, the output is $\varepsilon$-close to uniform: $\tfrac12\|\text{Ext}(X,U_d)-U_m\|_1\le\varepsilon$.
- **Leftover Hashing Lemma:** if $\mathcal F$ is a two-universal family $X\to\{0,1\}^l$, then on average over $f\in\mathcal F$, $Z=f(X)$ is $\Delta$-close to uniform conditioned on side info $E$, with
$$\Delta=\tfrac12\sqrt{2^{\,l-H_{\min}(X|E)}}.$$

---

### 1. In plain words
A weak random source (only guaranteed min-entropy $k$, possibly with weird correlations and known to an eavesdropper $E$) can be turned into almost-perfect uniform bits by hashing with a *random* two-universal hash and outputting fewer bits than the available min-entropy. The LHL gives the exact trade-off: output $l$ bits and you're off-uniform by $\Delta=\tfrac12\sqrt{2^{l-H_{\min}(X|E)}}$, which is tiny as long as $l$ is comfortably below $H_{\min}(X|E)$.

### 2. Toolbox
- Two-universality: $\Pr_f[f(x)=f(x')]\le2^{-l}$ ([06](06-two-universal-hashing.md)).
- Min-entropy $\Leftrightarrow$ collision: $\sum_x P(x)^2\le\max_x P(x)=2^{-H_{\min}(X)}$ ([01](01-renyi-and-collision-entropy.md), [02](02-min-entropy.md)).
- $\ell_1$–$\ell_2$ bound: for a distribution on $N=2^l$ points, $\|q-u\|_1\le\sqrt{N}\,\|q-u\|_2$ and $\|q-u\|_2^2=\sum_z q_z^2-\tfrac1N$.

### 3. The proof (collision-probability argument, no side info $E$ for clarity)
1. **Output collision probability.** The chance two independent draws of $(f,Z)$ collide in *both* the seed and the output is
$$\Pr[Z=Z']=\Pr[f\text{ same}]\big(\Pr[X=X']+\Pr[f(X)=f(X')\mid X\ne X']\big).$$
Using two-universality $\Pr[f(X)=f(X')\mid X\ne X']\le2^{-l}$ and $\Pr[X=X']=\sum_x P(x)^2\le2^{-H_{\min}(X)}$:
$$\Pr[Z=Z'\mid f]\le2^{-H_{\min}(X)}+2^{-l}.$$
2. **Collision ⇒ distance to uniform.** For the output distribution $q$ on $2^l$ points, $\|q-u\|_2^2=\Pr[Z=Z']-2^{-l}\le2^{-H_{\min}(X)}$.
3. **$\ell_2\to\ell_1$:** $\|q-u\|_1\le\sqrt{2^l}\,\|q-u\|_2\le\sqrt{2^l\cdot2^{-H_{\min}(X)}}=\sqrt{2^{\,l-H_{\min}(X)}}$.
4. So the distance to uniform $\Delta=\tfrac12\|q-u\|_1\le\tfrac12\sqrt{2^{\,l-H_{\min}(X)}}$. With side information $E$, the identical argument with conditional collision probability replaces $H_{\min}(X)$ by $H_{\min}(X|E)$:
$$\Delta=\tfrac12\sqrt{2^{\,l-H_{\min}(X|E)}}.\qquad\blacksquare$$

### 4. Where the magic happens
**Two-universality bounds the *output* collision probability by $2^{-H_{\min}}+2^{-l}$, and collision probability controls the $\ell_2$ (hence $\ell_1$) distance to uniform.** So "few collisions" ⇒ "looks uniform." The exponent $l-H_{\min}(X|E)$ is the gap between bits you take and bits of true (adversary-conditioned) randomness available — keep it negative and $\Delta$ is exponentially small.

### 5. If he pushes back
- *"Why output fewer than $H_{\min}$ bits?"* If $l\approx H_{\min}(X|E)$ then $\Delta\approx\tfrac12$ (useless); you must leave a security gap so $2^{l-H_{\min}}$ is tiny. This gap is the "entropy you sacrifice."
- *"Where does the seed go?"* It's the random choice of $f$; the lemma is "on average over $f$," and the seed can even be public.
- *"Quantum side info?"* The bound survives with $E$ quantum — that's the Quantum Leftover Hashing Lemma ([08](08-quantum-leftover-hashing.md)).
