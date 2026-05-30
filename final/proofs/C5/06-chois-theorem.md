# 06 — Choi's theorem (the equivalences) + unitary ⇔ rank $J=1$

**Claim.** For a linear map $\mathcal E:\mathcal B(\mathbb C^d)\to\mathcal B(\mathbb C^{d'})$, the following are equivalent:
1. $\mathcal E$ has a Kraus representation $\mathcal E(\rho)=\sum_{k=0}^{m-1}K_k\rho K_k^\dagger$;
2. $\mathcal E$ is completely positive;
3. $\mathcal E$ is $d$-positive;
4. $J_{\mathcal E}=I_d\otimes\mathcal E(|\beta_{00}\rangle\langle\beta_{00}|)\ge0$;
5. $\mathcal E$ has a Kraus representation with exactly $\text{rank}\,J_{\mathcal E}$ operators.

**Corollary.** $\mathcal E:\mathcal B(\mathbb C^d)\to\mathcal B(\mathbb C^d)$ is **unitary** ($\mathcal E(\rho)=U\rho U^\dagger$) $\iff\text{rank}\,J_{\mathcal E}=1$.

---

### 1. In plain words
This is the master theorem of the lecture. It says four different-looking statements about a map are all the same: "is a physical (sandwich-sum) map," "stays positive even on entangled halves," "stays positive on $d\times d$ halves," and "has a PSD Choi matrix." The practical upshot: to test if a map is a legal quantum operation, just compute one matrix ($J_{\mathcal E}$) and check it's PSD. The corollary says a channel is a pure unitary gate exactly when its Choi matrix has rank 1.

### 2. Toolbox (the pieces, already proved)
- **(1 ⇒ 2):** Kraus ⇒ CP — [03](03-kraus-implies-cp.md).
- **(2 ⇒ 3):** CP ⇒ $d$-positive — trivial (CP means $n$-positive for *all* $n$, in particular $n=d$).
- **(3 ⇒ 4):** $d$-positive ⇒ $J_{\mathcal E}\ge0$ — [04](04-d-positive-implies-choi-psd.md).
- **(4 ⇒ 5):** $J_{\mathcal E}\ge0$ ⇒ Kraus rep with $\text{rank}\,J_{\mathcal E}$ operators — [05](05-choi-psd-implies-kraus.md).
- **(5 ⇒ 1):** trivial (a rank-$J$ Kraus rep *is* a Kraus rep).

### 3. The proof
**The cycle.** Chain the implications above:
$$1\xrightarrow{[03]}2\xrightarrow{\text{trivial}}3\xrightarrow{[04]}4\xrightarrow{[05]}5\xrightarrow{\text{trivial}}1.$$
Every statement implies the next around the loop, so all five are equivalent. ∎

**Minimal Kraus number.** Any Kraus rep $\mathcal E=\sum_{k=0}^{m-1}K_k\rho K_k^\dagger$ has $m\ge\text{rank}\,J_{\mathcal E}$: from the rep, $J_{\mathcal E}=\sum_k(I_d\otimes K_k)|\beta_{00}\rangle\langle\beta_{00}|(I_d\otimes K_k)^\dagger$ is a sum of $m$ rank-$\le1$ terms, so its rank is $\le m$. Step [05] achieves $m=\text{rank}\,J_{\mathcal E}$, so that's the minimum.

**Corollary (unitary ⇔ rank 1).**
- **(⇒)** If $\mathcal E(\rho)=U\rho U^\dagger$ then
$$J_{\mathcal E}=(I_d\otimes U)|\beta_{00}\rangle\langle\beta_{00}|(I_d\otimes U^\dagger)=|\psi\rangle\langle\psi|,\quad |\psi\rangle=(I_d\otimes U)|\beta_{00}\rangle,$$
a pure-state projector, so $\text{rank}\,J_{\mathcal E}=1$.
- **(⇐)** If $\text{rank}\,J_{\mathcal E}=1$, then by [05] there is a single Kraus operator: $\mathcal E(\rho)=K\rho K^\dagger$. Trace-preservation gives
$$\delta_{ij}=\text{Tr}|i\rangle\langle j|=\text{Tr}\,\mathcal E(|i\rangle\langle j|)=\text{Tr}(K|i\rangle\langle j|K^\dagger)=\langle j|K^\dagger K|i\rangle,$$
so $K^\dagger K=I$ — $K$ is a square isometry, hence unitary. ∎

### 4. Where the magic happens
**The whole theorem is one implication cycle stitched from the four lemmas.** The deep content is "$d$-positive already forces complete positivity" (you never need to test $n>d$), proved by the single entangled test state $|\beta_{00}\rangle$. The rank corollary is just "one Kraus operator + trace preservation = unitary."

### 5. If he pushes back
- *"Sketch the full loop on the board."* Write the five boxes and label each arrow with its lemma — examiners love seeing you cite [03]/[04]/[05] precisely.
- *"Why is $\text{rank}\,J$ the number of 'noise sources'?"* Each Kraus operator is one way the environment can act; rank 1 = no environment = unitary; higher rank = more decoherence channels.
- *"Worked Choi matrix?"* See the depolarizing channel in [14](14-depolarizing-kraus-and-choi.md): $\text{rank}\,J_{\Delta_1}=d^2$ (maximally noisy).
- *"Where's trace preservation in Choi's theorem?"* It's *not* — Choi's theorem is about CP only. TP is the separate Kraus theorem [07](07-kraus-theorem-trace-preserving.md).
