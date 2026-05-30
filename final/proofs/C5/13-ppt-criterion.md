# 13 — The PPT (Peres–Horodecki) criterion

**Claim.** The transpose $T(\rho)=\rho^{\mathsf T}$ is **positive but not completely positive**. Consequently the **partial transpose** $I_n\otimes T$ satisfies: every separable $\rho$ has $(I_n\otimes T)\rho\ge0$, so
$$(I_n\otimes T)\rho\not\ge0\ \Rightarrow\ \rho\text{ is entangled.}$$
This **PPT criterion** is necessary *and sufficient* iff $nd\le6$ (qubit–qubit and qubit–qutrit).

---

### 1. In plain words
Transposing a density matrix keeps it a valid state (same eigenvalues). But transposing only *half* of an entangled state can produce negative eigenvalues — a red flag that the state was entangled. This gives the most-used practical entanglement test: take the partial transpose and look for a negative eigenvalue. For the smallest systems ($2\times2$, $2\times3$) it catches *all* entanglement; in larger systems some entangled states sneak past (PPT but still entangled).

### 2. Toolbox
- Transpose preserves eigenvalues (and trace, Hermiticity), so $T$ is positive: $\rho\ge0\Rightarrow\rho^{\mathsf T}\ge0$.
- Partial transpose on blocks: $(I_n\otimes T)\big(|a\rangle\langle b|\otimes|i\rangle\langle j|\big)=|a\rangle\langle b|\otimes|j\rangle\langle i|$, i.e. transpose each $d\times d$ block.
- $T$ is a positive map, so the general PnCP criterion ([12](12-pncp-separability-criterion.md)) applies.

### 3. The proof

**$T$ is positive.**
1. $\rho^{\mathsf T}$ has the same eigenvalues as $\rho$ (transpose preserves the characteristic polynomial), so $\rho\ge0\Rightarrow\rho^{\mathsf T}\ge0$. ✓

**$T$ is not completely positive.** Test on the Bell state.
2. $(I_d\otimes T)|\beta_{00}\rangle\langle\beta_{00}|=\frac1d\sum_{i,j}|i\rangle\langle j|\otimes(|i\rangle\langle j|)^{\mathsf T}=\frac1d\sum_{i,j}|i\rangle\langle j|\otimes|j\rangle\langle i|$ — this is $\frac1d$ times the **swap** operator.
3. The swap has eigenvalue $-1$ on antisymmetric vectors, e.g. $(|01\rangle-|10\rangle)$: $(I\otimes T)|\beta_{00}\rangle\langle\beta_{00}|\,(|01\rangle-|10\rangle)=-\frac1d(|01\rangle-|10\rangle)$. A negative eigenvalue ⇒ $(I_d\otimes T)|\beta_{00}\rangle\langle\beta_{00}|\not\ge0$ ⇒ $T$ is **not** CP. ∎

**Separable ⇒ PPT.** By [12](12-pncp-separability-criterion.md) (positive map preserves separable states), or directly:
4. $(I_n\otimes T)\big(\sum_i p_i|\phi_i\rangle\langle\phi_i|\otimes|\psi_i\rangle\langle\psi_i|\big)=\sum_i p_i|\phi_i\rangle\langle\phi_i|\otimes(|\psi_i\rangle\langle\psi_i|)^{\mathsf T}\ge0$, since each transposed projector is still PSD.
5. Contrapositive: $(I_n\otimes T)\rho\not\ge0\Rightarrow\rho$ entangled. ∎

**Sufficiency for $nd\le6$.** For $2\times2$ and $2\times3$, every positive map decomposes as $\mathcal E_1+\mathcal E_2\circ T$ with $\mathcal E_1,\mathcal E_2$ CP (Størmer–Woronowicz). Hence the transpose is the *only* positive map you need, so PPT is also sufficient there. (Stated; the decomposition theorem is beyond the lecture.)

### 4. Where the magic happens
**Transposing one half of $|\beta_{00}\rangle$ turns the Bell projector into (a multiple of) the swap operator, which has a $-1$ eigenvalue.** That single negative eigenvalue is simultaneously the proof that $T$ is not CP *and* the prototype of every PPT entanglement detection.

### 5. If he pushes back
- *"How do I run the test?"* Compute $\rho^{T_B}$ (transpose the second subsystem's blocks); if any eigenvalue is $<0$, entangled. For $2\times2$ that's the whole story.
- *"PPT but entangled — example?"* Bound-entangled states in $3\times3$ or $2\times4$; they have positive partial transpose yet no distillable entanglement. This is why the criterion fails sufficiency for $nd>6$.
- *"Why exactly $nd\le6$?"* That's the regime where the Størmer–Woronowicz decomposition of positive maps holds, making transpose-detection complete.
- *"Relation to entanglement witnesses?"* $I_n\otimes T$ is the canonical witness-generating positive map; its Choi matrix is a witness ([12](12-pncp-separability-criterion.md)).
