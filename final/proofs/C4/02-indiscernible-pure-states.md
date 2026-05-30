# 02 — Indiscernible pure states differ only by a global phase

**Claim.** For pure states, the following are equivalent:
$$|\psi\rangle\equiv|\xi\rangle \iff |\psi\rangle=e^{i\theta}|\xi\rangle \iff |\psi\rangle\langle\psi|=|\xi\rangle\langle\xi|,$$
where $|\psi\rangle\equiv|\xi\rangle$ means **no observable's measurement statistics can tell them apart**.

---

### 1. In plain words
Two pure states look identical to *every possible experiment* exactly when they differ by an overall phase factor $e^{i\theta}$ — a "global phase." Global phase is invisible because every prediction quantum mechanics makes goes through the projector $|\psi\rangle\langle\psi|$, and the phase cancels there ($e^{i\theta}\cdots e^{-i\theta}=1$). Conversely, if two states are *not* phase-multiples, you can always cook up a measurement that separates them: just measure "am I in state $|\psi\rangle$?".

### 2. Toolbox
- Born's rule: statistics of measuring $O=\sum_\lambda \lambda E_\lambda$ on a pure state depend on it only through $\Pr[\lambda]=\langle\psi|E_\lambda|\psi\rangle=\text{Tr}(E_\lambda|\psi\rangle\langle\psi|)$ ([19](19-two-trace-identities.md)).
- Cauchy–Schwarz: for unit vectors, $|\langle\xi|\psi\rangle|\le1$, with equality iff they're parallel ($|\psi\rangle=c|\xi\rangle$, $|c|=1$).
- Any unit vector extends to an orthonormal basis (Gram–Schmidt).

### 3. The proof
We prove a cycle: (A) $|\psi\rangle=e^{i\theta}|\xi\rangle$ ⇒ (B) equal projectors ⇒ (C) indiscernible ⇒ (A).

**(A) ⇒ (B): phase ⇒ same projector.**
1. $|\psi\rangle\langle\psi|=\big(e^{i\theta}|\xi\rangle\big)\big(e^{i\theta}|\xi\rangle\big)^\dagger=e^{i\theta}e^{-i\theta}|\xi\rangle\langle\xi|=|\xi\rangle\langle\xi|$ — the phase and its conjugate cancel.

**(B) ⇒ (C): same projector ⇒ indiscernible.**
2. For *any* observable, $\Pr[\lambda]=\text{Tr}(E_\lambda|\psi\rangle\langle\psi|)$ depends on the state only through the projector $|\psi\rangle\langle\psi|$.
3. If $|\psi\rangle\langle\psi|=|\xi\rangle\langle\xi|$, then every such probability is identical for the two states. So they're indiscernible. ✓

**(C) ⇒ (A): indiscernible ⇒ phase.** (Contrapositive is cleanest.)
4. Suppose $|\psi\rangle$ and $|\xi\rangle$ are **not** phase-multiples. By Cauchy–Schwarz equality, that means $|\langle\xi|\psi\rangle|^2\ne1$ (strictly less than 1).
5. Build the observable $W$ whose eigenbasis extends $|\psi\rangle$ (Gram–Schmidt), and consider the outcome "collapse onto $|\psi\rangle$", with projector $|\psi\rangle\langle\psi|$.
6. On $|\psi\rangle$ this outcome has probability $\langle\psi|\psi\rangle\langle\psi|\psi\rangle=1$. On $|\xi\rangle$ it has probability $|\langle\psi|\xi\rangle|^2\ne1$.
7. Different probabilities ⇒ the states are **distinguishable**. Contrapositive: indiscernible ⇒ $|\langle\xi|\psi\rangle|^2=1$ ⇒ (Cauchy–Schwarz) $|\psi\rangle=e^{i\theta}|\xi\rangle$. ∎

**Bonus direct check that phase ⇒ indiscernible.** For *any* eigenvectors $\{|\phi_k\rangle\}$,
$$|\langle\xi|\phi_k\rangle|^2=\big|\langle\psi|e^{-i\theta}|\phi_k\rangle\big|^2=|\langle\psi|\phi_k\rangle|^2,$$
so the two states produce the same statistics in every basis — phase truly drops out.

### 4. Where the magic happens
**Everything physical is built from $|\psi\rangle\langle\psi|$, and a global phase cancels in $|\psi\rangle\langle\psi|$.** So "physically equal" = "equal projector" = "equal up to phase." The converse direction's trick is the *projective measurement onto $|\psi\rangle$ itself*: it gives certainty for $|\psi\rangle$, so any deviation shows up immediately.

### 5. If he pushes back
- *"Isn't a relative phase also a phase — why is that detectable?"* Because a relative phase changes the projector. $|+\rangle$ and $|-\rangle$ differ by a relative phase, are orthogonal, and the $X$-measurement separates them perfectly. See [13](13-global-vs-relative-phase.md).
- *"Where did Cauchy–Schwarz equality get used?"* Twice: $|\langle\xi|\psi\rangle|=1$ for unit vectors forces parallelism, which (with unit norm) is exactly $|\psi\rangle=e^{i\theta}|\xi\rangle$.
- *"What's the mixed-state analogue?"* Random states are indistinguishable iff they have the same **density matrix**, not the same projector — that's [03](03-indistinguishable-iff-same-density-matrix.md).
