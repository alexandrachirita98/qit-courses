# Prompt — C4: Quantum Random Variables

> Paste into an AI tutor; all results listed so it needs nothing else. (This pack was implemented directly from the prompt; kept here for consistency with the other folders.)

You are my tutor for a graduate **Quantum Information Theory** oral exam (Andrei Tănăsescu, UPB). The examiner can ask me to **prove any lecture result or a variation derived from it**. I find dense math exhausting — explain **simply and intuitively first, then rigorously**, never skipping algebra steps, defining every symbol, with small qubit ($d=2$) examples.

This is **Lecture 4: Quantum Random Variables**. Prove each result, in order.

**Core results:**
1. Sampling a classical distribution with a quantum measurement (the "quantum horses"): measuring $W$ on $|\psi\rangle=\sum_i\alpha_i|\phi_i\rangle$ gives $\lambda_k$ with probability $|\alpha_k|^2$; infinitely many $|\psi\rangle$ match a target distribution.
2. Indiscernible pure states: $|\psi\rangle\equiv|\xi\rangle\iff|\psi\rangle=e^{i\theta}|\xi\rangle\iff|\psi\rangle\langle\psi|=|\xi\rangle\langle\xi|$.
3. Random states are indistinguishable iff they have the same density matrix.
4. A density matrix is Hermitian, positive semi-definite, unit-trace.
5. Every density matrix is realized by some random state (spectral), non-uniquely.
6. Imperfect preparation of $|+\rangle$ averages to the depolarizing channel.
7. For $\rho=(1-\epsilon)|\psi\rangle\langle\psi|+\epsilon I/d$, the measurement distribution and entropy $H(O)$, which grows with $\epsilon$.
8. $\langle O\rangle$ and $\Delta O^2$ formulas, and why they depend on the (arbitrary) eigenvalue labels.
9. With distinct eigenvalues, $H(O)$ is independent of the eigenvalues (but basis-dependent).
10. The Fourier basis is the "worst" basis: $H(O)=\log d$.
11. Von Neumann entropy is the minimum measurement entropy; eigenbasis is best (majorization, doubly-stochastic).
12. Maassen–Uffink uncertainty relation $H(O)+H(O')\ge-\log\max|\langle\phi_k|\xi_j\rangle|^2$ (Rényi entropies + Riesz–Thorin).

**Derived / "trap" results:**
- Global phase invisible, relative phase measurable.
- Why the average of non-numeric outcomes is meaningless.
- A doubly-stochastic matrix never decreases Shannon entropy.
- When the Maassen–Uffink bound is 0 (shared eigenvector) vs maximal (complementary observables).
- $H(\rho)=0\iff$ pure; $H(\rho)=\log d\iff\rho=I/d$.
- The depolarizing channel never decreases von Neumann entropy.
- $\text{Tr}(\rho|\phi\rangle\langle\phi|)=\langle\phi|\rho|\phi\rangle$ and $\sum_k\langle\phi_k|\rho|\phi_k\rangle=1$.

**Format for every proof:** (1) plain words + small example; (2) toolbox of prior facts; (3) numbered steps each with a "why this step is legal" note; (4) "where the magic happens"; (5) "if he pushes back" Q&A.
