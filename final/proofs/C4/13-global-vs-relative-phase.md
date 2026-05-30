# 13 — Global phase is invisible; relative phase is measurable

**Claim.**
- A **global** phase is undetectable: $e^{i\theta}|\psi\rangle$ gives the same statistics as $|\psi\rangle$ for every observable.
- A **relative** phase is detectable: $|\psi_\varphi\rangle=\frac{1}{\sqrt2}(|0\rangle+e^{i\varphi}|1\rangle)$ has measurement statistics that depend on $\varphi$.

---

### 1. In plain words
Multiplying the *whole* state by a phase $e^{i\theta}$ changes nothing physical — it cancels in every prediction. But a phase sitting on *one part* of a superposition relative to another (a "relative phase") tilts the state and **is** observable: you just have to measure in the right basis (here, the $X$ basis). This is why $|+\rangle$ and $|-\rangle$ — which differ only by a relative sign — are perfectly distinguishable, while $|\psi\rangle$ and $-|\psi\rangle$ are the same state.

### 2. Toolbox
- Statistics depend on the state only through the projector $|\psi\rangle\langle\psi|$ ([02](02-indiscernible-pure-states.md), [19](19-two-trace-identities.md)).
- Expectation of an observable: $\langle X\rangle=\langle\psi|X|\psi\rangle$ ([08](08-mean-and-variance-depend-on-eigenvalues.md)).
- Pauli $X=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, with eigenstates $|\pm\rangle=\frac1{\sqrt2}(|0\rangle\pm|1\rangle)$.

### 3. The proof

**Global phase is invisible.**
1. $\big(e^{i\theta}|\psi\rangle\big)\big(e^{i\theta}|\psi\rangle\big)^\dagger=e^{i\theta}e^{-i\theta}|\psi\rangle\langle\psi|=|\psi\rangle\langle\psi|$ — same projector.
2. Every outcome probability is $\text{Tr}(E_\lambda|\psi\rangle\langle\psi|)$, a function of the projector alone, so it's unchanged. The two states are indiscernible. ∎

**Relative phase is visible.** Take $|\psi_\varphi\rangle=\frac1{\sqrt2}(|0\rangle+e^{i\varphi}|1\rangle)$.
3. Its projector has off-diagonal entries that *carry $\varphi$*:
$$|\psi_\varphi\rangle\langle\psi_\varphi|=\frac12\begin{pmatrix}1 & e^{-i\varphi}\\ e^{i\varphi} & 1\end{pmatrix}.$$
4. Measure $X$. Its expectation:
$$\langle X\rangle_\varphi=\langle\psi_\varphi|X|\psi_\varphi\rangle=\text{Tr}\Big(X\,|\psi_\varphi\rangle\langle\psi_\varphi|\Big)=\frac12\,\text{Tr}\begin{pmatrix}e^{i\varphi}&1\\1&e^{-i\varphi}\end{pmatrix}=\frac{e^{i\varphi}+e^{-i\varphi}}{2}=\cos\varphi.$$
5. $\langle X\rangle_\varphi=\cos\varphi$ depends on $\varphi$ — e.g. $\varphi=0$ gives $\langle X\rangle=+1$ (state $|+\rangle$, always outcome $+1$), while $\varphi=\pi$ gives $\langle X\rangle=-1$ (state $|-\rangle$, always outcome $-1$). Perfectly distinguishable. ∎

### 4. Where the magic happens
**A global phase cancels in $|\psi\rangle\langle\psi|$ (it appears as $e^{i\theta}e^{-i\theta}$); a relative phase survives in the *off-diagonal* of the projector** and so shows up in any measurement sensitive to coherences (like $X$). "Phase is invisible" is true only for the *overall* phase — the redundant gauge degree of freedom counted in [01](01-sampling-with-an-observable.md).

### 5. If he pushes back
- *"Isn't a relative phase just a global phase of the $|1\rangle$ component?"* Yes, but it's *relative* to the $|0\rangle$ component — only a phase common to **all** components is global. The difference of two phases is physical.
- *"Which basis exposes a relative phase between $|0\rangle$ and $|1\rangle$?"* Any basis not diagonal in $\{|0\rangle,|1\rangle\}$; $X$ (or $Y$) is the natural choice. Measuring $Z$ would *miss* it ($\Pr[0]=\Pr[1]=\frac12$ regardless of $\varphi$).
- *"Tie-in to the uncertainty relation?"* The $Z$ measurement is blind to $\varphi$ while the $X$ measurement sees it perfectly — $Z$ and $X$ are complementary, the maximal-overlap case of Maassen–Uffink ([16](16-maassen-uffink-zero-and-maximal.md)).
