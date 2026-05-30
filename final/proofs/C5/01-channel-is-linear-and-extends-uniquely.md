# 01 — A channel is linear on states and extends uniquely to all matrices

**Claim.** A memoryless state transformation $\mathcal E$ acts **linearly** on density matrices,
$$\mathcal E(p\rho+(1-p)\rho')=p\,\mathcal E(\rho)+(1-p)\,\mathcal E(\rho'),$$
and this restriction extends **uniquely** to a linear map on all of $\mathcal B(\mathbb C^d)$, because the density matrices span $\mathcal B(\mathbb C^d)$.

---

### 1. In plain words
A channel processes one input state at a time, with no memory. If you feed it a *random* state — $\rho$ with probability $p$, else $\rho'$ — the output is the same random mixture of outputs. That's linearity (well, affine/convex-linearity) on states. Since every matrix can be written as a combination of density matrices, there's exactly one linear map on the whole matrix space agreeing with $\mathcal E$ on states. So "channel = linear map" is forced, not assumed.

### 2. Toolbox
- A convex mixture of states is a state; feeding it = mixing the outputs (memorylessness).
- The density matrices contain a **basis** of $\mathcal B(\mathbb C^d)$: $Z_a=|a\rangle\langle a|$, $X_{b,c}=\frac{|b\rangle+|c\rangle}{\sqrt2}\frac{\langle b|+\langle c|}{\sqrt2}$, $Y_{d,e}=\frac{|d\rangle+i|e\rangle}{\sqrt2}\frac{\langle d|-i\langle e|}{\sqrt2}$.
- A linear map is determined by its values on a basis.

### 3. The proof

**Convex-linearity on states.**
1. Preparing "$\rho$ w.p. $p$, $\rho'$ w.p. $1-p$" *is* the state $p\rho+(1-p)\rho'$ ([C4/03](../C4/03-indistinguishable-iff-same-density-matrix.md)). Memorylessness means the output is the corresponding mixture of outputs:
$$\mathcal E(p\rho+(1-p)\rho')=p\,\mathcal E(\rho)+(1-p)\,\mathcal E(\rho').$$

**Every matrix is a combination of density matrices.**
2. Any $A=\sum_{i,j}a_{ij}|i\rangle\langle j|$ can be rewritten in the basis $\{Z_a,X_{b,c},Y_{d,e}\}$ — diagonal parts via $Z_a$, real off-diagonal via $X_{b,c}$ (minus diagonal corrections), imaginary off-diagonal via $Y_{d,e}$:
$$A=\sum_i a_{ii}Z_i+\sum_{i<j}(a_{ij}+a_{ji})\Big(X_{i,j}-\tfrac{Z_i+Z_j}{2}\Big)+i\sum_{i<j}(a_{ij}-a_{ji})\Big(Y_{i,j}-\tfrac{Z_i+Z_j}{2}\Big).$$
So the density matrices **span** $\mathcal B(\mathbb C^d)$.

**Unique linear extension.**
3. Define $\mathcal E$ on each basis element (a density matrix, where it's already specified), then extend by linearity. Step 2 guarantees every $A$ is reached, so $\mathcal E(A)$ is well-defined.
4. Uniqueness: two linear maps agreeing on a spanning set agree everywhere. ∎

### 4. Where the magic happens
**Density matrices aren't a small corner of matrix space — they linearly span all of it.** So "behaves linearly on states" upgrades for free to "is a genuine linear operator on $\mathcal B(\mathbb C^d)$," letting us study channels with full linear algebra (Choi matrices, Kraus operators, etc.).

### 5. If he pushes back
- *"Convex-linear isn't the same as linear."* Right — but combined with trace-preservation you get full linearity on the real span (Hermitian matrices), and complexifying gives all of $\mathcal B(\mathbb C^d)$. The basis argument makes the extension unique.
- *"Why insist on memorylessness?"* Without it, the map could depend on history and need not be linear in the single-state input. Channels model the memoryless (Markovian) case.
- *"What pins down the rest of the definition?"* Physicality forces trace-preservation and complete positivity — that's [02](02-channels-are-cptp.md).
