# 08 — Mean and variance of a measurement, and why they're label-dependent

**Claim.** For $\rho$ and observable $O=\sum_k\lambda_k|\phi_k\rangle\langle\phi_k|$,
$$\langle O\rangle_\rho=\text{Tr}(\rho O)=\sum_k\lambda_k\langle\phi_k|\rho|\phi_k\rangle,\qquad \Delta O^2_\rho=\text{Tr}(\rho O^2)-\big(\text{Tr}(\rho O)\big)^2=\sum_k\lambda_k^2\langle\phi_k|\rho|\phi_k\rangle-\langle O\rangle_\rho^2.$$
Both depend on the **choice of eigenvalues** $\lambda_k$. In particular the variance need not even be monotone in a noise parameter, unlike the entropy.

---

### 1. In plain words
The mean and variance of a measurement are just the ordinary statistics of the outcome values $\lambda_k$, weighted by their quantum probabilities $\langle\phi_k|\rho|\phi_k\rangle$. The catch: when outcomes are *qualitative* (horse A, B, C…), the numbers $\lambda_k$ we attach to them are arbitrary. Change the labels and the mean/variance change — so these statistics are not intrinsic to the physics. We'll prove the formulas and then show, with a $d=3$ example, that the variance can rise *and then fall* as noise increases — a "bad monotony artifact" of bad labels.

### 2. Toolbox
- $\langle O\rangle_\rho:=\mathbb E[\text{outcome}]=\sum_\lambda\lambda\Pr[\lambda]$ and $\Pr[\lambda]=\text{Tr}(\rho E_\lambda)$ ([19](19-two-trace-identities.md), [03](03-indistinguishable-iff-same-density-matrix.md)).
- $O=\sum_k\lambda_k|\phi_k\rangle\langle\phi_k| \Rightarrow O^2=\sum_k\lambda_k^2|\phi_k\rangle\langle\phi_k|$ (orthonormal eigenbasis).
- Variance $=\mathbb E[\text{outcome}^2]-(\mathbb E[\text{outcome}])^2$.

### 3. The proof

**Mean.**
1. $\langle O\rangle_\rho=\sum_\lambda\lambda\,\text{Tr}(\rho E_\lambda)=\text{Tr}\big(\rho\sum_\lambda\lambda E_\lambda\big)=\text{Tr}(\rho O)$ — linearity of trace; $\sum_\lambda\lambda E_\lambda=O$ by definition. Note this is **linear in $O$**.
2. In the eigenbasis, $\text{Tr}(\rho O)=\sum_k\lambda_k\,\text{Tr}(\rho|\phi_k\rangle\langle\phi_k|)=\sum_k\lambda_k\langle\phi_k|\rho|\phi_k\rangle$. ✓

**Variance.**
3. $\langle O^2\rangle_\rho=\text{Tr}(\rho O^2)=\sum_k\lambda_k^2\langle\phi_k|\rho|\phi_k\rangle$ — same computation with $O^2$.
4. $\Delta O^2_\rho=\langle O^2\rangle_\rho-\langle O\rangle_\rho^2=\sum_k\lambda_k^2\langle\phi_k|\rho|\phi_k\rangle-\Big(\sum_k\lambda_k\langle\phi_k|\rho|\phi_k\rangle\Big)^2$. ✓

Both formulas are explicit polynomials in the labels $\lambda_k$ — relabel the outcomes and the numbers change.

### 4. The $d=3$ example (non-monotone variance)
Take $\rho=(1-\epsilon)|\psi\rangle\langle\psi|+\epsilon\frac I3$ measured in a basis containing $|\psi\rangle$, with labels $\lambda_1=1,\lambda_2=2,\lambda_3=3$. From [07](07-measurement-uncertainty-grows-with-epsilon.md) the probabilities are $\Pr[\lambda_1]=1-\frac23\epsilon$ and $\Pr[\lambda_2]=\Pr[\lambda_3]=\frac\epsilon3$.

5. $\langle O\rangle=1\cdot\big(1-\tfrac23\epsilon\big)+(2+3)\tfrac\epsilon3=1-\tfrac23\epsilon+\tfrac{5\epsilon}{3}=1+\epsilon.$
6. $\langle O^2\rangle=1\cdot\big(1-\tfrac23\epsilon\big)+(4+9)\tfrac\epsilon3=1-\tfrac23\epsilon+\tfrac{13\epsilon}{3}=1+\tfrac{11\epsilon}{3}.$
7. $\Delta O^2=\big(1+\tfrac{11\epsilon}{3}\big)-(1+\epsilon)^2=1+\tfrac{11\epsilon}{3}-1-2\epsilon-\epsilon^2=\tfrac{5\epsilon}{3}-\epsilon^2.$
8. Complete the square: $\tfrac{5\epsilon}{3}-\epsilon^2=\big(\tfrac56\big)^2-\big(\epsilon-\tfrac56\big)^2.$

This **increases until $\epsilon=\frac56$, then decreases** — non-monotone in the noise. Compare with the entropy of the *same* experiment ([07](07-measurement-uncertainty-grows-with-epsilon.md)), which increases monotonically all the way to $\epsilon=1$. The difference is entirely due to the arbitrary labels $1,2,3$.

### 5. Where the magic happens
**$\langle O\rangle=\text{Tr}(\rho O)$ is linear in $O$** — that one identity gives both the mean (use $O$) and, via $O^2$, the second moment. But linearity in $O$ is exactly what makes these statistics *sensitive to relabeling*: rescale or shift the $\lambda_k$ and $\text{Tr}(\rho O)$ moves with them. Entropy avoids this because it's built from the probabilities only, not the values.

### 6. If he pushes back
- *"Why is the mean physically meaningless for horse races?"* Because "horse A = 1, B = 2" is an arbitrary numbering; renumber and the 'average horse' changes. See [14](14-why-the-average-is-meaningless.md).
- *"When ARE mean/variance meaningful?"* When the eigenvalues are genuine physical quantities (energy, spin projection) — then the labels aren't arbitrary and Heisenberg-type variance relations make sense.
- *"Can you make the variance monotone by relabeling?"* Yes — that's the point: monotonicity here is an artifact of the labels, not of the state. Choose other $\lambda_k$ and you get a different curve.
- *"What's the label-independent uncertainty measure?"* The Shannon entropy $H(O)$ of the outcome distribution; with distinct eigenvalues it doesn't see the labels at all ([09](09-distinct-eigenvalues-entropy-independent.md)).
