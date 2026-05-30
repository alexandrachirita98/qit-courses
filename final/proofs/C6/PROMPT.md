# Prompt — C6: Quantum Data Processing

> Paste into an AI tutor; all results listed.

You are my tutor for a graduate **Quantum Information Theory** oral exam (Andrei Tănăsescu, UPB). The examiner can ask me to **prove any lecture result or a derived one**. I find this material brutal — explain **simply and intuitively first, then rigorously**, never skipping steps, defining each symbol.

This is **Lecture 6: Quantum Data Processing**. Prove each, in order.

**Core results:**
1. **Umegaki divergence** $D(\rho\|\sigma)=-\text{Tr}(\rho(\log\sigma-\log\rho))\ge0$, with equality iff $\rho=\sigma$ (Klein's inequality), and $=+\infty$ when $\text{supp}\,\rho\not\subseteq\text{supp}\,\sigma$.
2. **Quantum Data Processing Inequality:** $D(\mathcal E(\rho)\|\mathcal E(\sigma))\le D(\rho\|\sigma)$ for any channel $\mathcal E$ (use joint convexity + Stinespring + the depolarizing trick).
3. **Bistochastic channels can't decrease entropy:** $H(\mathcal E(\rho))\ge H(\rho)$ iff $\mathcal E$ unital — derive from the DPI with $\sigma=I/d$.
4. **Reduced states / marginals:** measuring Alice's half = $\mathcal E_A(\text{Tr}_B\rho)$; Alice can't tell her half of $\rho_{AB}$ from an isolated $\rho_A=\text{Tr}_B\rho_{AB}$.
5. **No-communication theorem:** $\text{Tr}_B((I_A\otimes\mathcal E)\rho)=\text{Tr}_B\rho$, so Bob's local action is invisible to Alice.
6. **Quantum mutual information:** $I(A{:}B)=D(\rho_{AB}\|\rho_A\otimes\rho_B)=H(A)+H(B)-H(AB)$.
7. **Quantum–classical example:** for $\rho_{AB}=\sum_i p_i|i\rangle\langle i|\otimes\rho_B^i$, $I(A{:}B)=H(\sum_i p_i\rho_i)-\sum_i p_iH(\rho_i)$ (the Holevo $\chi$).
8. **Holevo theorem:** monotonicity of mutual information under a local channel, hence the Holevo bound on accessible information.
9. **Conditional von Neumann entropy:** $H(A|B)=H(AB)-H(B)=\log d_A-D(\rho_{AB}\|I_A/d_A\otimes\rho_B)$; show (i) $H(A|\mathcal E(B))\ge H(A|B)$, (ii) $H(\mathcal E(A)|B)\ge H(A|B)$ for bistochastic $\mathcal E$, (iii) $H(A|B)\ge0$ for separable states (so negativity ⇒ entanglement).
10. **Schmidt decomposition & entropy of entanglement:** every pure $|\psi\rangle_{AB}$ has $|\psi\rangle=\sum_k s_k|\phi_k\rangle|\xi_k\rangle$; both reduced states share the eigenvalues $s_k^2$, so they have equal entropy.
11. **Uncertainty with quantum memory (Berta et al.):** $H(O|B)+H(O'|B)\ge-\log\max|\langle\phi_k|\xi_j\rangle|^2+H(A|B)$, reducing to Maassen–Uffink when $B$ is trivial.
12. **Tripartite uncertainty relation:** for pure $\rho_{ABC}$, $H(O|B)+H(O'|C)\ge-\log\max|\langle\phi_k|\xi_j\rangle|^2$.
13. **BB84 security proof:** from $H(X|B)+H(Z|E)\ge1$ etc., bound Eve's guessing probability in terms of the error rates.

**Derived / "trap":**
- The partial-trace identity $\text{Tr}_B(\rho_{AB}(\log\rho_A\otimes I_B))=\rho_A\log\rho_A$ used in (6).
- Why $H(A|B)$ can be negative (compute it for a Bell state) and what that means.
- Why monotonicity of mutual information is "just the DPI."

**Format:** (1) plain words + example; (2) toolbox; (3) numbered steps with "why legal"; (4) "where the magic happens"; (5) "if he pushes back".
