# 03 — A Kraus representation implies complete positivity

**Claim.** If $\mathcal E(\rho)=\sum_{k=0}^{m-1}K_k\rho K_k^\dagger$ for some matrices $K_k$, then $\mathcal E$ is **completely positive**: $I_n\otimes\mathcal E(A)\ge0$ for every PSD $A$ and every $n$.

---

### 1. In plain words
The Kraus form is "sandwich $\rho$ between $K_k$ and $K_k^\dagger$, then sum." Each sandwich $K\rho K^\dagger$ preserves positivity (it's a congruence), and so does the extended version $I\otimes K$. Summing positive things stays positive. The only real work is bookkeeping the tensor/block structure, which we handle with the factorization $A=\sqrt A\sqrt A^\dagger$.

### 2. Toolbox
- $A\ge0\iff A=BB^\dagger$ for some $B$ (take $B=\sqrt A$).
- A congruence $MAM^\dagger$ is PSD whenever $A$ is: $\langle v|MAM^\dagger|v\rangle=\langle M^\dagger v|A|M^\dagger v\rangle\ge0$.
- $I_n\otimes\mathcal E$ acts block-wise: on $A=(A_{ij})_{i,j}$, $(I_n\otimes\mathcal E)(A)=(\mathcal E(A_{ij}))_{ij}$.
- $(I_n\otimes K_k)$ applied to the block matrix $A$ pulls $K_k$ into every block.

### 3. The proof
Let $A=(A_{ij})$ be a PSD block matrix (an $nd\times nd$ matrix viewed as $n\times n$ blocks of size $d\times d$).

1. Apply $I_n\otimes\mathcal E$ block-wise and substitute the Kraus form in each block:
$$(I_n\otimes\mathcal E)(A)=\big(\mathcal E(A_{ij})\big)_{ij}=\Big(\textstyle\sum_k K_kA_{ij}K_k^\dagger\Big)_{ij}=\sum_k\big(K_kA_{ij}K_k^\dagger\big)_{ij}.$$
2. Recognize the $k$-th term as a single congruence by $I_n\otimes K_k$:
$$\big(K_kA_{ij}K_k^\dagger\big)_{ij}=(I_n\otimes K_k)\,A\,(I_n\otimes K_k)^\dagger.$$
(Multiplying the block matrix $A$ on the left by $\text{diag}(K_k,\dots,K_k)=I_n\otimes K_k$ and on the right by its dagger does exactly this.)
3. So $(I_n\otimes\mathcal E)(A)=\sum_k (I_n\otimes K_k)\,A\,(I_n\otimes K_k)^\dagger$.
4. Write $A=\sqrt A\sqrt A^\dagger$ (PSD). Then each term is
$$(I_n\otimes K_k)\sqrt A\,\big[(I_n\otimes K_k)\sqrt A\big]^\dagger=B_kB_k^\dagger\ge0,\qquad B_k:=(I_n\otimes K_k)\sqrt A.$$
5. A sum of PSD matrices is PSD, so $(I_n\otimes\mathcal E)(A)\ge0$. This holds for all $n$, hence $\mathcal E$ is CP. ∎

### 4. Where the magic happens
**$I_n\otimes\mathcal E$ is itself a sum of congruences $(I_n\otimes K_k)A(I_n\otimes K_k)^\dagger$, and a congruence of a PSD matrix is PSD** ($MAM^\dagger=(M\sqrt A)(M\sqrt A)^\dagger$). The tensor factor $I_n$ rides along harmlessly — that's why positivity survives even on entangled inputs (the whole point of "complete").

### 5. If he pushes back
- *"Where did entanglement of the input matter?"* It didn't need to — the argument works for *any* PSD $A$, entangled or not. That robustness is exactly complete positivity.
- *"Is the converse true (CP ⇒ Kraus)?"* Yes — via the Choi matrix: [04](04-d-positive-implies-choi-psd.md) + [05](05-choi-psd-implies-kraus.md), assembled in [06](06-chois-theorem.md).
- *"Do the $K_k$ need any condition?"* For CP, none. For *trace-preserving* (a genuine channel) you also need $\sum_k K_k^\dagger K_k=I$ — that's [07](07-kraus-theorem-trace-preserving.md).
