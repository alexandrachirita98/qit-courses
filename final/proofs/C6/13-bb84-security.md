# 13 — BB84 security from the uncertainty relation

**Claim.** In the entanglement-based BB84 picture, after Eve's intervention the tripartite state $\rho_{ABE}$ satisfies
$$H(X|B)_\rho+H(Z|E)_\rho\ge1,\qquad H(Z|B)_\rho+H(X|E)_\rho\ge1.$$
If Bob's error rates are $\delta_{\text{bit}}$ (in the $X$ basis) and $\delta_{\text{phase}}$ (in the $Z$ basis), then Eve's probability $p$ of guessing the key bit obeys
$$h(p)\ge 1-\tfrac12h(\delta_{\text{bit}})-\tfrac12h(\delta_{\text{phase}}),\qquad p\le\tfrac12\Big(1+\sqrt{\ln 2\,\big(h(\delta_{\text{bit}})+h(\delta_{\text{phase}})\big)}\Big).$$
Low observed error ⇒ provably high uncertainty for Eve.

---

### 1. In plain words
BB84 sends qubits in randomly chosen $X$ or $Z$ bases. Recast it (equivalently) as Alice making a Bell pair, sending one half through Eve to Bob, and everyone measuring. The tripartite uncertainty relation says Eve and Bob can't *both* know Alice's $X$ and $Z$ outcomes. So if Bob's measurements match Alice's well (low error), Eve is forced to be ignorant. Quantify it and you get a bound on Eve's guessing probability purely from the measured error rates — the heart of QKD security.

### 2. Toolbox
- Tripartite uncertainty / memory-assisted relation with complementary $X,Z$: max overlap $|\langle x|z\rangle|^2=1/2$, so $-\log c^2=1$ ([11](11-uncertainty-with-quantum-memory.md), [12](12-tripartite-uncertainty.md)).
- Binary entropy $h(\delta)$; Fano-type bound: $H(X|B)\le h(\delta_{\text{bit}})$ if Bob errs with rate $\delta_{\text{bit}}$.
- Eve guessing $\Leftrightarrow$ low $H(Z|E)$: if she guesses with prob $p$, $H(Z|E)\le h(p)$ (heuristically).
- Pinsker-type relation $p\le\frac12(1+\sqrt{(2\ln2)(1-h(p))})$ (C7 link).

### 3. The proof (sketch following the lecture)
**Equivalent entanglement-based protocol.** A qubit $|\psi\rangle=H^iX^j|0\rangle$ Alice sends could equally be obtained by measuring her half of a Bell pair $|\beta_{00}\rangle_{AB}$. Since that measurement commutes with Eve's channel $\mathcal E$ (acting on the in-flight qubit $B$ + her ancilla $E$), the protocol is equivalent to:
1. Alice makes $|\beta_{00}\rangle_{AB}$, sends $B$ through Eve (who applies $\mathcal E$ entangling $B,E$), Bob receives $B$; all measure in random $X/Z$ bases and keep matching-basis rounds.

**Apply the uncertainty relation.** With $A$'s complementary observables $X,Z$ (overlap $1/2$, bound $1$):
2. $H(X|B)_\rho+H(Z|E)_\rho\ge1$ and $H(Z|B)_\rho+H(X|E)_\rho\ge1$.

**Translate to error rates.**
3. Low bit-error $\delta_{\text{bit}}$ ⇒ Bob predicts Alice's $X$ well ⇒ $H(X|B)\le h(\delta_{\text{bit}})$. Plugged into (2): $H(Z|E)\ge1-h(\delta_{\text{bit}})$, i.e. Eve is uncertain about $Z$. Symmetrically $H(X|E)\ge1-h(\delta_{\text{phase}})$.
4. Averaging the two and writing Eve's guess probability $p$ via $h(p)\ge\frac12(H(X|E)+H(Z|E))\ge1-\frac12h(\delta_{\text{bit}})-\frac12h(\delta_{\text{phase}})$.
5. Converting $h(p)$ to $p$ (concavity / Pinsker, C7): $p\le\frac12\big(1+\sqrt{\ln2\,(h(\delta_{\text{bit}})+h(\delta_{\text{phase}}))}\big)$. ∎

**Numbers.** At a $1\%$ error rate, Eve guesses $<66.6\%$ of bits; with privacy amplification (32 parity sums), her chance to share the final 256-bit key drops to $\sim10^{-23}$.

### 4. Where the magic happens
**Recasting prepare-and-measure BB84 as an entangled-pair protocol makes Eve a *third party* in a tripartite state, so the uncertainty relation forbids her and Bob from both knowing $X$ and $Z$.** Security then follows from *measured* error rates — no assumption about Eve's strategy, because the bound holds for any channel $\mathcal E$.

### 5. If he pushes back
- *"Why is the prepare-and-measure version equivalent?"* Alice's local measurement commutes with Eve's channel on the other systems ([05](05-no-communication-theorem.md) logic), so measuring before or after sending is the same.
- *"Which uncertainty relation exactly?"* The memory-assisted Berta relation ([11](11-uncertainty-with-quantum-memory.md)) with $X,Z$ complementary; the two inequalities use $B$ and $E$ as the two memories ([12](12-tripartite-uncertainty.md)).
- *"What does privacy amplification do?"* Compresses the partially-secret raw key into a shorter, nearly-perfectly-secret key (the Leftover Hashing Lemma, C7 / lesson-7 update).
