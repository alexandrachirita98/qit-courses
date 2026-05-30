# 03 — Entanglement-assisted discrimination & the fidelity

**Claim.** If Alice's state is $\rho$ or $\sigma$ (equal priors) but she holds purifications $|\phi_\rho\rangle,|\psi_\sigma\rangle$ (e.g. shared with Bob), the best discrimination success is
$$P_{\text{succ}}=\frac12\Big(1+\sqrt{1-|\langle\phi_\rho|\psi_\sigma\rangle|^2}\Big).$$
The **maximal** overlap $|\langle\phi_\rho|\psi_\sigma\rangle|^2$ over all purifications is the **fidelity** $F(\rho,\sigma)$ — the *hardest-to-distinguish* case.

---

### 1. In plain words
Distinguishing two *pure* states is governed by their overlap: orthogonal = perfectly distinguishable, parallel = impossible. Apply the Helstrom bound to the two purifications and you get a success probability set entirely by their overlap. Now, purifications aren't unique — different "padding" gives different overlaps. The *largest* achievable overlap is defined to be the fidelity, corresponding to the purifications that are as similar as possible, i.e. the case where discrimination is hardest.

### 2. Toolbox
- Helstrom bound for two states, equal priors: $P_{\text{succ}}=\tfrac12+\tfrac14\|\,|\phi_\rho\rangle\langle\phi_\rho|-|\psi_\sigma\rangle\langle\psi_\sigma|\,\|_{\text{Tr}}$ ([01](01-helstrom-bound.md)).
- Two unit vectors span a 2-D space; write $|\phi_\rho\rangle=\cos\theta\,|\psi_\sigma\rangle+\sin\theta\,|\xi\rangle$ with $|\xi\rangle\perp|\psi_\sigma\rangle$.
- Trace norm of a $2\times2$ traceless-ish difference = $2|\sin\theta|$.

### 3. The proof
1. In the 2-D span of $\{|\psi_\sigma\rangle,|\xi\rangle\}$, the difference of projectors is
$$|\phi_\rho\rangle\langle\phi_\rho|-|\psi_\sigma\rangle\langle\psi_\sigma|=\begin{pmatrix}\cos^2\theta-1 & \cos\theta\sin\theta\\ \cos\theta\sin\theta & \sin^2\theta\end{pmatrix}.$$
2. Its eigenvalues are $\pm|\sin\theta|$ (compute: trace $=0$, determinant $=-\cos^2\theta\sin^2\theta-(1-\cos^2\theta)\cdots=-\sin^2\theta$, so eigenvalues $\pm\sin\theta$). Hence trace norm $=2|\sin\theta|$.
3. Helstrom: $P_{\text{succ}}=\tfrac12+\tfrac14\cdot2|\sin\theta|=\tfrac12(1+|\sin\theta|)=\tfrac12\big(1+\sqrt{1-\cos^2\theta}\big)=\tfrac12\big(1+\sqrt{1-|\langle\phi_\rho|\psi_\sigma\rangle|^2}\big).$
4. $P_{\text{succ}}$ is *decreasing* in the overlap $|\langle\phi_\rho|\psi_\sigma\rangle|^2$. So the **minimal** distinguishability ↔ **maximal** overlap over all purifications, which is *defined* as the fidelity
$$F(\rho,\sigma):=\max\big\{|\langle\phi_\rho|\psi_\sigma\rangle|^2:\ \text{Tr}_B|\phi_\rho\rangle\langle\phi_\rho|=\rho,\ \text{Tr}_B|\psi_\sigma\rangle\langle\psi_\sigma|=\sigma\big\}.\qquad\blacksquare$$

### 4. Where the magic happens
**Two states live in a 2-D plane, so their projector difference has eigenvalues $\pm\sin\theta$**, making discrimination a pure function of the overlap $\cos\theta$. Optimizing the (non-unique) purifications to *maximize* overlap defines fidelity as "best-case similarity" — exactly the quantity Uhlmann computes in closed form ([04](04-uhlmann-theorem.md)).

### 5. If he pushes back
- *"Why maximize overlap and not minimize?"* Maximal overlap = the most pessimistic (hardest) discrimination, the meaningful worst case for tasks like compression quality.
- *"Is $F\in[0,1]$?"* Yes: $F=1$ iff $\rho=\sigma$, $F=0$ iff orthogonal supports.
- *"Relation to trace distance?"* They sandwich each other: $1-\sqrt F\le\tfrac12\|\rho-\sigma\|_{\text{Tr}}\le\sqrt{1-F}$ (Fuchs–van de Graaf), so both measure closeness.
