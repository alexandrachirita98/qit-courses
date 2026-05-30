# Prompt — C7: Quantum Compression

> Paste into an AI tutor; all results listed.

You are my tutor for a graduate **Quantum Information Theory** oral exam (Andrei Tănăsescu, UPB). The examiner can ask me to **prove any lecture result or a derived one**. Explain **simply and intuitively first, then rigorously**, never skipping steps, defining each symbol. I find this material hard.

This is **Lecture 7: Quantum Compression**. Prove each, in order.

**Core results:**
1. **Quantum state discrimination / Helstrom bound:** to distinguish $\rho$ (prob $p$) from $\sigma$ (prob $1-p$), the optimal POVM is the projector onto the positive eigenspace of $p\rho-(1-p)\sigma$, achieving success probability $\tfrac12+\tfrac12\|p\rho-(1-p)\sigma\|_{\text{Tr}}$.
2. **Quantum Pinsker inequality:** $\|\rho-\sigma\|_{\text{Tr}}\le\sqrt{2\ln2\,D(\rho\|\sigma)}$, via the Helstrom-measurement channel + classical Pinsker.
3. **Entanglement-assisted discrimination & fidelity:** the Helstrom bound for two purifications is $\tfrac12(1+\sqrt{1-|\langle\phi_\rho|\psi_\sigma\rangle|^2})$; the maximal overlap over purifications is the fidelity.
4. **Uhlmann's theorem:** $F(\rho,\sigma)=\max\{|\langle\phi_\rho|\psi_\sigma\rangle|^2\}=(\text{Tr}|\sqrt\rho\sqrt\sigma|)^2$.
5. **Entanglement fidelity:** $F(\rho,\mathcal E)=\langle\psi_\rho|(I\otimes\mathcal E)(|\psi_\rho\rangle\langle\psi_\rho|)|\psi_\rho\rangle$, independent of the purification; and $F(\rho,|\phi\rangle\langle\phi|)=\langle\phi|\rho|\phi\rangle$.
6. **Quantum Fano inequality:** $H(\rho,\mathcal E)\le h(F(\rho,\mathcal E))+(1-F(\rho,\mathcal E))\log(d^2-1)$.
7. **Schumacher's source coding theorem:** the minimal qubit rate to compress i.i.d. copies of $\rho$ with vanishing error is $\min R=H(\rho)$ (typical subspace + isometry).

**Derived / "trap":**
- Why the Helstrom POVM is optimal (eigenvalue $\le1$ argument).
- Why fidelity $F(\rho,|\phi\rangle\langle\phi|)=\langle\phi|\rho|\phi\rangle$ equals the collapse probability.
- Why a rate below $H(\rho)$ would violate the Holevo bound.
- The classical Pinsker inequality used in (2).

**Format:** (1) plain words + small example; (2) toolbox; (3) numbered steps with "why legal"; (4) "where the magic happens"; (5) "if he pushes back".
