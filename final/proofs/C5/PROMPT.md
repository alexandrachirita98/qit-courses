# Prompt — C5: Quantum Channels

> Paste into an AI tutor; all results are listed so it needs nothing else.

You are my tutor for a graduate **Quantum Information Theory** oral exam (Andrei Tănăsescu, UPB). The examiner can ask me to **prove any result from the lecture or something derived from it**. I find this lecture brutal, so explain everything **simply and intuitively first, then rigorously**, never skipping algebra steps, defining every symbol.

This is **Lecture 5: Quantum Channels**. Prove each result, in order.

**Core results:**
1. A physical (memoryless) state transformation $\mathcal E$ is **linear on density matrices** and extends **uniquely** to a linear map on all of $\mathcal B(\mathbb C^d)$ (use the density-matrix basis $\{Z_a, X_{b,c}, Y_{d,e}\}$).
2. **Quantum channels are CPTP:** any such $\mathcal E$ must be **trace-preserving** and **completely positive** (decompose an arbitrary matrix as $\alpha_1\rho_1-\alpha_2\rho_2+i\alpha_3\rho_3-i\alpha_4\rho_4$).
3. **Kraus ⇒ completely positive:** if $\mathcal E(\rho)=\sum_k K_k\rho K_k^\dagger$ then $\mathcal E$ is CP (the block-matrix / $\sqrt A$ argument).
4. **$d$-positive ⇒ Choi matrix $\ge 0$:** $J_{\mathcal E}=I_d\otimes\mathcal E(|\beta_{00}\rangle\langle\beta_{00}|)\ge0$ (Jamiołkowski isomorphism).
5. **Choi $\ge 0$ ⇒ Kraus representation:** reconstruct $\mathcal E$ from its Choi matrix; $K_k=\sqrt d\sum_a(\langle a|\otimes I)|\psi_k'\rangle\langle a|$.
6. **Choi's theorem:** CP ⇔ $d$-positive ⇔ $J_{\mathcal E}\ge0$ ⇔ has a Kraus representation (of size $\mathrm{rank}\,J_{\mathcal E}$). Corollary: $\mathcal E$ is unitary ⇔ $\mathrm{rank}\,J_{\mathcal E}=1$.
7. **Kraus' theorem:** TP ⇔ every Kraus rep is complete ⇔ has a complete Kraus rep ⇔ $\mathrm{Tr}_{\mathbb C^{d'}}J_{\mathcal E}=I_d/d$.
8. **Bistochastic ⇔ unital:** $\mathcal E$ and its adjoint $\mathcal E^\dagger$ are both channels ⇔ $\mathcal E$ is a unital channel.
9. **Stinespring dilation:** $\mathcal E$ is a channel ⇔ $\mathcal E(\rho)=\mathrm{Tr}_E\big(U(|0\rangle_E\langle0|\otimes\rho)U^\dagger\big)$ for some ancilla + unitary.
10. **POVMs:** a POVM is a family $\{F_i\ge0\}$ with $\sum_i F_i=I$; measuring it on $\rho$ gives outcome $i$ with probability $\mathrm{Tr}(\rho F_i)$.
11. **Naimark dilation:** any POVM is realized by a gate + projective measurement on a larger space ($K_i=\sqrt{F_i}$, then Stinespring).
12. **PnCP separability criterion:** $\rho$ is entangled ⇔ there is a **positive** (but not CP) map $\mathcal E$ with $(I_n\otimes\mathcal E)\rho\not\ge0$; relate to entanglement witnesses.
13. **PPT / Peres–Horodecki:** the transpose is positive but not CP; separable ⇒ $(I\otimes T)\rho\ge0$, so a negative partial transpose certifies entanglement; necessary & sufficient iff $nd\le6$.

**Derived / "trap" results:**
- Worked example: Kraus operators and Choi matrix of the **depolarizing channel** $\Delta_\epsilon$.
- Why "completely positive" is strictly stronger than "positive" (the transpose example).
- Adding an ancilla, the partial trace, and a measurement are all channels — give their Kraus operators.
- Why $\mathrm{rank}\,J_{\mathcal E}$ is the minimal number of Kraus operators.

**Format for every proof:** (1) plain words + small example; (2) toolbox of prior facts; (3) numbered steps each with a "why it's legal" note; (4) "where the magic happens"; (5) "if he pushes back" Q&A.
