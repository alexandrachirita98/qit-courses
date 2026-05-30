# 01 — The Helstrom bound for quantum state discrimination

**Claim.** Given $\rho$ with prior probability $p$ and $\sigma$ with prior $1-p$, the best two-outcome POVM $\{F,I-F\}$ achieves success probability
$$P_{\text{succ}}=\frac12+\frac12\,\|p\rho-(1-p)\sigma\|_{\text{Tr}},$$
maximized by taking $F$ = the projector onto the **positive** eigenspace of $M:=p\rho-(1-p)\sigma$ (the **Helstrom measurement**).

---

### 1. In plain words
Someone hands you one of two known states and you must guess which. Your "test" is a POVM element $F$ (guess "$\rho$") and $I-F$ (guess "$\sigma$"). The math shows your success only depends on $F$ through the operator $M=p\rho-(1-p)\sigma$: you want $F$ to "catch" all of $M$'s positive part and none of its negative part. So the optimal $F$ projects onto where $M>0$. The resulting success rate is $\tfrac12$ (random guessing) plus half the trace-norm of $M$ — the more $\rho,\sigma$ differ, the better you do.

### 2. Toolbox
- POVM outcome probabilities $\text{Tr}(\rho F)$, $\text{Tr}(\sigma(I-F))$ ([../C5/10](../C5/10-povm-basics.md)).
- Any $0\le F\le I$ has eigenvalues in $[0,1]$.
- Spectral form $M=\sum_i\lambda_i|\psi_i\rangle\langle\psi_i|$, $\text{Tr}\,M=p-(1-p)=2p-1$, $\|M\|_{\text{Tr}}=\sum_i|\lambda_i|$.

### 3. The proof
1. **Success probability.**
$$P_{\text{succ}}=p\,\text{Tr}(\rho F)+(1-p)\text{Tr}(\sigma(I-F))=(1-p)+\text{Tr}\big(F(p\rho-(1-p)\sigma)\big)=(1-p)+\text{Tr}(FM).$$
(Expanded $(1-p)\text{Tr}(\sigma(I-F))=(1-p)-(1-p)\text{Tr}(\sigma F)$ and combined the $F$-terms.)
2. **Maximize $\text{Tr}(FM)$ over $0\le F\le I$.** Diagonalize $M=\sum_i\lambda_i|\psi_i\rangle\langle\psi_i|$. Then $\text{Tr}(FM)=\sum_i\lambda_i\langle\psi_i|F|\psi_i\rangle$, and since $0\le\langle\psi_i|F|\psi_i\rangle\le1$, the sum is maximized by setting $\langle\psi_i|F|\psi_i\rangle=1$ when $\lambda_i>0$ and $=0$ when $\lambda_i<0$ — i.e. $F=\sum_{\lambda_i>0}|\psi_i\rangle\langle\psi_i|$, the **positive-part projector**. Maximum: $\text{Tr}(FM)=\sum_{\lambda_i>0}\lambda_i$.
3. **Evaluate.** With $\sum_i\lambda_i=\text{Tr}\,M=2p-1$ and $\sum_i|\lambda_i|=\|M\|_{\text{Tr}}$:
$$\sum_{\lambda_i>0}\lambda_i=\frac{\|M\|_{\text{Tr}}+(2p-1)}{2}.$$
4. Plug into step 1:
$$P_{\text{succ}}=(1-p)+\frac{\|M\|_{\text{Tr}}+2p-1}{2}=\frac12+\frac12\|M\|_{\text{Tr}}.\qquad\blacksquare$$

**Symmetric case $p=\tfrac12$:** $M=\tfrac12(\rho-\sigma)$, so $P_{\text{succ}}=\tfrac12+\tfrac14\|\rho-\sigma\|_{\text{Tr}}$.

### 4. Where the magic happens
**Everything funnels through $M=p\rho-(1-p)\sigma$, and $\text{Tr}(FM)$ is maximized by keeping $M$'s positive eigenvalues and dropping its negative ones** (because $F$'s eigenvalues are capped at 1). The leftover $\tfrac12+\tfrac12\|M\|_{\text{Tr}}$ ties "how well you can distinguish" directly to the trace distance.

### 5. If he pushes back
- *"Why is the trace norm the right distance?"* Because $P_{\text{succ}}$ — the operational distinguishability — equals $\tfrac12+\tfrac12\|M\|_{\text{Tr}}$; trace distance *is* distinguishability.
- *"Could a fancier (more-outcome) POVM do better?"* No — two hypotheses need only a binary test; the Helstrom projector is globally optimal.
- *"What's the link to entropy?"* The Pinsker inequality ([02](02-quantum-pinsker.md)) bounds this trace distance by the divergence, connecting distinguishability to relative entropy.
