# 14 — Worked example: Choi matrix & Kraus operators of the depolarizing channel

**Claim.**
- The **completely depolarizing** channel $\Delta_1(\rho)=\frac{I_d}{d}\text{Tr}\,\rho$ has Choi matrix $J_{\Delta_1}=\frac{I_{d^2}}{d^2}\ge0$, rank $d^2$, and a minimal Kraus representation with $d^2$ operators $K_{k_1,k_2}=\frac1{\sqrt d}|k_2\rangle\langle k_1|$.
- The **qubit depolarizing** channel $\Delta_\epsilon(\rho)=(1-\epsilon)\rho+\epsilon\frac{I_2}{2}\text{Tr}\,\rho$ ($d=2$) has rank-4 Choi matrix and Kraus operators $K_0=\tfrac{\sqrt{4-3\epsilon}}2 I,\ K_1=\tfrac{\sqrt\epsilon}2 Z,\ K_2=\sqrt{\tfrac\epsilon2}\,|1\rangle\langle0|,\ K_3=\sqrt{\tfrac\epsilon2}\,|0\rangle\langle1|.$

---

### 1. In plain words
This is the "plug in numbers" exercise that ties Choi's and Kraus' theorems together. The completely depolarizing channel erases everything to the maximally mixed state — maximally noisy — so its Choi matrix is itself maximally mixed and full rank $d^2$ (you need $d^2$ Kraus operators). The qubit $\Delta_\epsilon$ interpolates between identity ($\epsilon=0$) and full noise; diagonalizing its Choi matrix yields four Kraus operators built from $I,Z$ and the two ladder operators.

### 2. Toolbox
- $J_{\mathcal E}=I_d\otimes\mathcal E(|\beta_{00}\rangle\langle\beta_{00}|)$; Kraus from eigenvectors of $J_{\mathcal E}$ ([05](05-choi-psd-implies-kraus.md)).
- $|\beta_{00}\rangle\langle\beta_{00}|=\frac1d\sum_{i,j}|i\rangle\langle j|\otimes|i\rangle\langle j|$.
- Completeness check $\sum_k K_k^\dagger K_k=I$ ([07](07-kraus-theorem-trace-preserving.md)).

### 3. Completely depolarizing $\Delta_1$
1. **Choi matrix.** $J_{\Delta_1}=I_d\otimes\Delta_1(|\beta_{00}\rangle\langle\beta_{00}|)=\frac1d\sum_{i,j}|i\rangle\langle j|\otimes\frac{I_d}{d}\,\text{Tr}|i\rangle\langle j|$. Since $\text{Tr}|i\rangle\langle j|=\delta_{ij}$,
$$J_{\Delta_1}=\frac1{d}\sum_{i}|i\rangle\langle i|\otimes\frac{I_d}{d}=\frac{I_d}{d}\otimes\frac{I_d}{d}=\frac{I_{d^2}}{d^2}\ge0.$$
2. **Rank & eigenvectors.** $J_{\Delta_1}$ is a multiple of the identity ⇒ rank $d^2$, every $|k_1\rangle\otimes|k_2\rangle$ an eigenvector with eigenvalue $1/d^2$. Minimal Kraus count $=d^2$.
3. **Kraus operators** from [05](05-choi-psd-implies-kraus.md): with $|\psi'\rangle=\frac1d|k_1\rangle|k_2\rangle$,
$$K_{k_1,k_2}=\sqrt d\sum_a(\langle a|\otimes I)\big(\tfrac1d|k_1\rangle|k_2\rangle\big)\langle a|=\frac1{\sqrt d}|k_2\rangle\langle k_1|.$$
4. **Check complete:** $\sum_{k_1,k_2}K_{k_1,k_2}^\dagger K_{k_1,k_2}=\frac1d\sum_{k_1,k_2}|k_1\rangle\langle k_2|k_2\rangle\langle k_1|=\frac1d\sum_{k_1,k_2}|k_1\rangle\langle k_1|=\frac1d\cdot d\cdot I=I$. ✓
5. **Sanity:** $\sum_{k_1,k_2}K_{k_1,k_2}\rho K_{k_1,k_2}^\dagger=\frac1d\sum_{k_1,k_2}|k_2\rangle\langle k_1|\rho|k_1\rangle\langle k_2|=\frac1d\sum_{k_2}|k_2\rangle\big(\sum_{k_1}\langle k_1|\rho|k_1\rangle\big)\langle k_2|=\frac{I_d}{d}\text{Tr}\,\rho.$ ✓

(Non-uniqueness: the Pauli/Heisenberg operators $\frac1d Z^{k_2}X^{k_1}$ give another minimal Kraus rep of $\Delta_1$, as on the slide.)

### 4. Qubit $\Delta_\epsilon$ ($d=2$)
6. The Choi matrix $J_{\Delta_\epsilon}=I_2\otimes\Delta_\epsilon(|\beta_{00}\rangle\langle\beta_{00}|)$ has rank 4 with eigen-pairs
$$\lambda_0=\tfrac{4-3\epsilon}4,\ |\psi_0\rangle=|\beta_{00}\rangle;\quad \lambda_{1,2,3}=\tfrac\epsilon4,\ |\psi_1\rangle=|\beta_{10}\rangle,\,|\psi_2\rangle=|01\rangle,\,|\psi_3\rangle=|10\rangle.$$
7. Vectorizing gives $K_0=\tfrac{\sqrt{4-3\epsilon}}2 I,\ K_1=\tfrac{\sqrt\epsilon}2 Z,\ K_2=\sqrt{\tfrac\epsilon2}|1\rangle\langle0|,\ K_3=\sqrt{\tfrac\epsilon2}|0\rangle\langle1|.$
8. Recombine: $\sum_k K_k\rho K_k^\dagger=\tfrac{4-3\epsilon}4\rho+\tfrac\epsilon4 Z\rho Z+\tfrac\epsilon4\big(|1\rangle\langle0|\rho|0\rangle\langle1|+|0\rangle\langle1|\rho|1\rangle\langle0|\big)=(1-\epsilon)\rho+\epsilon\tfrac{I_2}2\text{Tr}\,\rho.$ ✓

### 5. Where the magic happens
**Maximal noise ⇒ maximal-rank (identity) Choi matrix ⇒ the most Kraus operators ($d^2$).** Reading Kraus operators off the Choi eigenvectors is the entire "Choi ⇒ Kraus" machine ([05](05-choi-psd-implies-kraus.md)) made concrete. The $\frac{I_d}{d}\otimes\frac{I_d}{d}$ factorization is the cleanest possible illustration of Jamiołkowski (channel ↔ state).

### 6. If he pushes back
- *"Why rank $d^2$ for $\Delta_1$?"* Because $J_{\Delta_1}\propto I_{d^2}$ — a totally mixed Choi matrix. Maximal decoherence needs the maximal number of "noise operators."
- *"Is $\text{Tr}_{d'}J_{\Delta_1}=I_d/d$?"* $\text{Tr}_{d'}\frac{I_{d^2}}{d^2}=\frac{I_d}{d^2}\cdot d=\frac{I_d}d$. ✓ — confirms TP via Kraus' theorem [07](07-kraus-theorem-trace-preserving.md).
- *"Connection to C4?"* $\Delta_\epsilon$ is exactly the imperfect-preparation noise of [C4/06](../C4/06-depolarizing-from-imperfect-prep.md) and the entropy-increasing channel of [C4/18](../C4/18-depolarizing-increases-entropy.md).
