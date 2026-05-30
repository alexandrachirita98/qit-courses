# 04 — $d$-positive ⇒ the Choi matrix is PSD

**Claim.** For a linear map $\mathcal E:\mathcal B(\mathbb C^d)\to\mathcal B(\mathbb C^{d'})$, define the **Choi matrix**
$$J_{\mathcal E}=I_d\otimes\mathcal E\big(|\beta_{00}\rangle\langle\beta_{00}|\big)=\frac1d\sum_{i,j=0}^{d-1}|i\rangle\langle j|\otimes\mathcal E(|i\rangle\langle j|),\qquad |\beta_{00}\rangle=\frac1{\sqrt d}\sum_{i}|i\rangle|i\rangle.$$
If $\mathcal E$ is **$d$-positive** (i.e. $I_d\otimes\mathcal E$ preserves PSD), then $J_{\mathcal E}\ge0$.

---

### 1. In plain words
Feed the map one specific test input — the maximally entangled state $|\beta_{00}\rangle$ — through "do nothing on half, $\mathcal E$ on the other half." The output is a matrix called the Choi matrix. If $\mathcal E$ is at least $d$-positive, then this particular output must be a valid PSD matrix. So "$d$-positive" instantly gives "$J_{\mathcal E}\ge0$." This single test state turns out to carry *all* the information about $\mathcal E$ (the Jamiołkowski isomorphism).

### 2. Toolbox
- $|\beta_{00}\rangle\langle\beta_{00}|$ is a pure state, hence PSD.
- $d$-positivity: $I_d\otimes\mathcal E(A)\ge0$ for all $A\ge0$ (the "$n=d$" case of complete positivity).
- Expanding the Bell projector: $|\beta_{00}\rangle\langle\beta_{00}|=\frac1d\sum_{i,j}|i\rangle\langle j|\otimes|i\rangle\langle j|$.

### 3. The proof
1. Compute the Choi matrix by pushing $I_d\otimes\mathcal E$ through the (expanded) Bell projector:
$$J_{\mathcal E}=I_d\otimes\mathcal E\Big(\tfrac1d\sum_{i,j}|i\rangle\langle j|\otimes|i\rangle\langle j|\Big)=\tfrac1d\sum_{i,j}|i\rangle\langle j|\otimes\mathcal E(|i\rangle\langle j|),$$
using linearity and that $I_d$ leaves the first tensor factor alone. As a block matrix, $J_{\mathcal E}=\frac1d\big(\mathcal E(|i\rangle\langle j|)\big)_{ij}$.
2. The input $|\beta_{00}\rangle\langle\beta_{00}|$ is PSD (a pure-state projector).
3. **$d$-positivity** says $I_d\otimes\mathcal E$ maps this PSD input to a PSD output. Therefore $J_{\mathcal E}=I_d\otimes\mathcal E(|\beta_{00}\rangle\langle\beta_{00}|)\ge0$. ∎

### 4. Where the magic happens
**One maximally entangled test state is enough.** Because $|\beta_{00}\rangle$ "contains" every $|i\rangle\langle j|$ in superposition, its image records $\mathcal E(|i\rangle\langle j|)$ for *all* $i,j$ at once — the whole linear map, packaged as one matrix. Positivity of that one output (guaranteed by $d$-positivity) is the seed for "CP ⇔ $J\ge0$."

### 5. If he pushes back
- *"Why $d$-positive and not just positive?"* The test state lives on $\mathbb C^d\otimes\mathbb C^d$, so we need $I_d\otimes\mathcal E$ to preserve positivity — exactly $d$-positivity. (Positivity of $\mathcal E$ alone is too weak; the transpose is positive but $J_T\not\ge0$, [13](13-ppt-criterion.md).)
- *"Is the map $\mathcal E\mapsto J_{\mathcal E}$ invertible?"* Yes — $\mathcal E(|i\rangle\langle j|)=d(\langle i|\otimes I)J_{\mathcal E}(|j\rangle\otimes I)$, so you recover $\mathcal E$ from $J_{\mathcal E}$. That's the converse [05](05-choi-psd-implies-kraus.md).
- *"Does $d$-positive imply completely positive?"* Yes for finite $d$ — that's the surprising punch of Choi's theorem ([06](06-chois-theorem.md)): you never need $n>d$.
