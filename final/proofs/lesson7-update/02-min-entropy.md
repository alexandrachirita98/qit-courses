# 02 — Min-entropy $H_\infty(X)=-\log\max_i p_i$ = $-\log$ guessing probability

**Claim.** As $\alpha\to\infty$, the Rényi entropy tends to the **min-entropy**
$$H_\infty(X)=\min_i(-\log p_i)=-\log\max_i p_i,$$
which equals $-\log$ of the probability that an adversary who knows the distribution guesses $X$ correctly in one try.

---

### 1. In plain words
Min-entropy is the *most pessimistic* entropy: it cares only about the single most likely outcome. If one value of $X$ is very probable, $X$ is easy to guess and min-entropy is low. It's the right measure for security: it directly answers "what's the best chance an attacker has of guessing the secret?" — namely $p_{\text{guess}}=\max_i p_i=2^{-H_\infty}$.

### 2. Toolbox
- $H_\alpha(X)=\frac1{1-\alpha}\log\sum_i p_i^\alpha$.
- For large $\alpha$, the sum $\sum_i p_i^\alpha$ is dominated by the largest term $(\max_i p_i)^\alpha$.
- Optimal single-guess strategy: output the most probable value.

### 3. The proof
1. **Limit.** Factor out the largest probability $p_{\max}=\max_i p_i$:
$$\sum_i p_i^\alpha=p_{\max}^\alpha\sum_i\Big(\frac{p_i}{p_{\max}}\Big)^\alpha=p_{\max}^\alpha\big(1+o(1)\big)\quad(\alpha\to\infty),$$
since every ratio $p_i/p_{\max}\le1$ and those $<1$ vanish. Then
$$H_\infty(X)=\lim_{\alpha\to\infty}\frac{1}{1-\alpha}\log\big(p_{\max}^\alpha(1+o(1))\big)=\lim_{\alpha\to\infty}\frac{\alpha\log p_{\max}}{1-\alpha}=-\log p_{\max}.$$
2. **Guessing interpretation.** An adversary maximizes $\Pr[\text{guess}=X]$ by guessing the most likely value, giving $p_{\text{guess}}=\max_i p_i$. Hence $H_\infty(X)=-\log p_{\text{guess}}$. ∎

### 4. Where the magic happens
**For large $\alpha$, the biggest probability swamps the sum, so Rényi entropy zooms in on $\max_i p_i$ alone.** That single number *is* the adversary's optimal guessing probability — which is why min-entropy, not Shannon entropy, is the currency of cryptographic security.

### 5. If he pushes back
- *"Why not Shannon entropy for security?"* Shannon is an *average* surprise; a key could have high Shannon entropy yet one dominant value an attacker exploits. Min-entropy bounds the *worst case* (best guess).
- *"High vs low?"* Low guessing probability ⇒ high min-entropy (secure); high guessing probability ⇒ low min-entropy (insecure).
- *"Conditional version?"* With side information $Y$ (or quantum $E$), $H_{\min}(X|Y)$ measures guessing probability *given* the side info — the quantity that actually matters in QKD ([03](03-conditional-min-entropy.md)).
