# Prompt — Lesson 7 (updated): Quantum Leftover Hashing Lemma

> Paste into an AI tutor; all results listed. This is the reworked Lesson 7 (by Alexandra Mușat) that front-loads the entropy zoo and hashing before the compression material.

You are my tutor for a graduate **Quantum Information Theory** oral exam (UPB). The examiner can ask me to **prove any lecture result or a derived one**. Explain **simply and intuitively first, then rigorously**, never skipping steps, defining each symbol.

This lecture covers the **entropy zoo, universal hashing, the Leftover Hashing Lemma, and privacy amplification** (the second half — state discrimination, Pinsker, fidelity, Uhlmann, Fano, Schumacher — is the same as standard Lecture 7). Prove each:

**Core results:**
1. **Rényi entropy & collision entropy ($\alpha=2$):** $H_\alpha(X)=\frac1{1-\alpha}\log\sum_i p_i^\alpha$, and $H_2(X)=-\log\sum_i p_i^2=-\log\Pr[X=X']$ (collision probability).
2. **Min-entropy ($\alpha\to\infty$):** $H_\infty(X)=-\log\max_i p_i$, equal to $-\log$ of the optimal guessing probability.
3. **Conditional min-entropy:** classical $H_{\min}(X|Y)=-\log\sum_y P(y)\max_x P(x|y)$; quantum $H_{\min}(A|B)_\rho=\max_{\sigma_B}\sup\{\lambda:\rho_{AB}\le2^{-\lambda}I_A\otimes\sigma_B\}$, and $H_{\min}(A|B)\le H_{\min}(A)$.
4. **Trace distance & purified distance:** $D(\rho,\sigma)=\tfrac12\text{Tr}|\rho-\sigma|$ is a metric; (generalized) fidelity $F$; purified distance $P(\rho,\sigma)=\sqrt{1-F(\rho,\sigma)^2}$.
5. **Smooth min-entropy:** $H_{\min}^\epsilon(A|B)_\rho=\max_{\tilde\rho\in B^\epsilon(\rho)}H_{\min}(A|B)_{\tilde\rho}$ over the $\epsilon$-ball in purified distance.
6. **Two-universal hashing:** definition ($\Pr_f[f(x)=f(x')]\le1/|Z|$ for $x\ne x'$); the $\mathbb Z_5$ linear example is two-universal.
7. **Randomness extraction & classical Leftover Hashing Lemma:** a $(k,\varepsilon)$-extractor; LHL: $Z=f(X)$ is $\Delta$-close to uniform given $E$ with $\Delta=\tfrac12\sqrt{2^{\,l-H_{\min}(X|E)}}$.
8. **Quantum Leftover Hashing Lemma:** the same with quantum side information $E$, and the two-universal ($\delta\le2^{-l}$) simplification.
9. **Privacy amplification:** how QKD turns a partially-secret raw key into a (near-)uniform secret key using a 2-universal hash, justified by the QLHL.

**Format:** (1) plain words + small example; (2) toolbox; (3) numbered steps with "why legal"; (4) "where the magic happens"; (5) "if he pushes back".
