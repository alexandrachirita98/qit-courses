# What each exam question asks (Q1–Q10 + Bonus)

A plain-language walkthrough of every question the notebook ([qit_exam_solver.ipynb](qit_exam_solver.ipynb)) solves. For each: what it *really* asks, the formula, how it's computed, and the traps. Theory links go to the [proof packs](../proofs/).

## The setup (shared by all questions)
- `|φ⟩`, `|ψ⟩` — two **pure** two-qubit states (4-vectors, normalized).
- `|v⟩` — a **random/mixed** state: it's `|φ⟩` with prob `w₀`, `|ψ⟩` with prob `w₁`. Its density matrix is
  $$\rho_v = w_0\,|\phi\rangle\langle\phi| + w_1\,|\psi\rangle\langle\psi|.$$
- `O` — a 4×4 Hermitian **observable** (used both as a measurement and as a candidate entanglement witness).
- `ℰ` — the **channel** "with prob 50% measure `O` and forget the result, else do nothing":
  $$\mathcal E(\rho)=\tfrac12\rho+\tfrac12\sum_\lambda E_\lambda\,\rho\,E_\lambda,$$
  where `E_λ` projects onto the eigenspace of distinct eigenvalue `λ`. Kraus operators: `{√½ I} ∪ {√½ E_λ}`.
- `|w⟩` — the state after the channel: `ρ_w = ℰ(ρ_v)`.

> Key distinction the exam tests constantly: **Q1 is about the pure state `|ψ⟩`**, while **Q3/Q4/Q5/Q6/Q8/Q9/Q10 are about the mixed state `ρ_v`** (or `ρ_w`).

> The inline **Example (6223)** boxes below all use paper 6223: $|\phi\rangle=\tfrac1{\sqrt{650}}[9,8,8,21]$, $|\psi\rangle=\tfrac1{\sqrt{2450}}[-21,28,28,21]$, $w_0=\tfrac{13}{18}=0.7222$, $w_1=\tfrac{5}{18}=0.2778$; eigenvalues of $\rho_v$ are $\{0,0,0.1667,0.8333\}$; $O$ has eigenvalues $\{21,105,189,273\}$. A consolidated table is at the [end](#worked-example--paper-6223-real-numbers).

---

## Q1 — Entropy of entanglement of `|ψ⟩`
**Asks:** how entangled is the *pure* state `|ψ⟩` (between qubit A and qubit B)?

**Concept.** For a pure bipartite state, "amount of entanglement" = the von Neumann entropy of *either* reduced state (they're equal). 0 = product/separable, 1 bit = maximally entangled (two qubits).

**Formula.**
$$\text{reshape } |\psi\rangle\to M\ (2\times2),\quad \rho_A=MM^\dagger,\quad E(|\psi\rangle)=H(\rho_A)=-\sum_i s_i\log_2 s_i$$
where `s_i` are the eigenvalues of `ρ_A` (= squared Schmidt coefficients).

**Example (6223).** Step by step:
1. Reshape $|\psi\rangle=\tfrac1{\sqrt{2450}}[-21,28,28,21]$ into $M=\tfrac1{\sqrt{2450}}\begin{pmatrix}-21&28\\28&21\end{pmatrix}$.
2. $\rho_A=MM^\dagger$ → eigenvalues $\{0.5,\ 0.5\}$ (maximally entangled).
3. $H=-0.5\log_2 0.5-0.5\log_2 0.5=0.5\cdot1+0.5\cdot1=$ **1.000000** → **B**.

**Steps.** (1) `M = ψ.reshape(2,2)`; (2) `ρ_A = M @ M†`; (3) entropy of its eigenvalues.

**Watch out.** ≤ 1 bit always → any option > 1 (e.g. 1.74, 1.44) is a **distractor**. Don't use `ρ_v` here — this is the pure `|ψ⟩` only.

**Theory:** [C6/10 Schmidt decomposition](../proofs/C6/10-schmidt-decomposition.md). Notebook: `ans["Q1"]`.

---

## Q2 — Is `|v⟩` entangled / does `O` witness it?
**Asks:** decide between A (entanglement witnessed by `O`), B (not witnessed by `O`), C (entangled but `O` isn't a valid witness), D (separable).

**Concept.** An **entanglement witness** is a Hermitian `O` that gives `Tr(O·σ) ≥ 0` on every separable state but `Tr(O·ρ) < 0` on some entangled `ρ` — a negative expectation is a *certificate* of entanglement.

**Checklist (run all):**
1. **`ρ_v` entangled?** PPT test: the partial transpose `(I⊗T)ρ_v` has a **negative eigenvalue** (necessary & sufficient for 2×2).
2. **`O` a valid witness?** `O` Hermitian, **not** PSD (has a negative eigenvalue), and **block-positive**: `⟨a,b|O|a,b⟩ ≥ 0` for all product states `|a⟩⊗|b⟩`.
3. **Does it fire?** `Tr(O·ρ_v) < 0`.

**Decision tree.**
- not entangled → **D**
- entangled + valid witness + `Tr(Oρ_v)<0` → **A**
- entangled + valid witness + `Tr(Oρ_v)≥0` → **B**
- entangled + `O` not block-positive → **C**

**Example (6223).** Step by step:
1. Build $\rho_v=w_0|\phi\rangle\langle\phi|+w_1|\psi\rangle\langle\psi|$ with $w_0=0.7222,\ w_1=0.2778$.
2. Partial transpose $(I\otimes T)\rho_v$ → eigenvalues $\{0,\ 0,\ 0.1667,\ 0.8333\}$.
3. Minimum eigenvalue $=0$ (not $<0$) ⇒ $\rho_v$ **separable** → **D**. (Side note: $\text{Tr}(O\rho_v)=+106.73>0$, so `O` wouldn't fire anyway.)

**Watch out.** "Entangled" ≠ "witnessed": a state can be entangled while *this* `O` fails to detect it (B or C). In your 4 variants: 3109/3992/6223 → **D** (separable), 6572 → **C**.

**Theory:** [C5/12 PnCP](../proofs/C5/12-pncp-separability-criterion.md), [C5/13 PPT](../proofs/C5/13-ppt-criterion.md). Notebook: `ans["Q2"]` (+ `ans["_Q2"]` detail).

---

## Q3 — Minimal average qubits for lossless encoding of `|v⟩`
**Asks:** how many qubits per copy to compress a stream of `ρ_v`'s without loss (asymptotically)?

**Concept.** Schumacher's source coding theorem: the answer is the **von Neumann entropy** of the source.

**Formula.** $\min R = H(\rho_v) = -\sum_i \lambda_i\log_2\lambda_i$ (eigenvalues of `ρ_v`).

**Example (6223).** Step by step:
1. $\rho_v$ eigenvalues (the two nonzero ones): $\lambda=\{0.1667,\ 0.8333\}$.
2. $H=-0.1667\log_2 0.1667-0.8333\log_2 0.8333$.
3. $=0.1667\cdot 2.585+0.8333\cdot 0.263=0.4309+0.2192=$ **0.650022** → **A**.

**Watch out.** This is `ρ_v` (the **mixed** state), *not* `|ψ⟩` (that's Q1). Since `ρ_v` is a mix of 2 states, rank ≤ 2 → ≤ 1 bit.

**Theory:** [C7/07 Schumacher](../proofs/C7/07-schumacher-source-coding.md). Notebook: `ans["Q3"]`.

---

## Q4 — Entropic uncertainty of measuring `O` on `|v⟩`
**Asks:** how unpredictable is the *outcome* when you measure `O` on `ρ_v`?

**Concept.** Group outcomes by **distinct eigenvalue** of `O` (degenerate ones merge), get a probability per outcome, take Shannon entropy.

**Formula.**
$$p_\lambda=\text{Tr}(E_\lambda\,\rho_v),\qquad H(O)=-\sum_\lambda p_\lambda\log_2 p_\lambda.$$

**Example (6223).** Step by step:
1. $O$ has **4 distinct** eigenvalues $\{21,105,189,273\}$ → 4 outcomes.
2. $p_\lambda=\text{Tr}(E_\lambda\rho_v)=\{0.5771,\ 0.0340,\ 0.1800,\ 0.2089\}$.
3. $H=-\sum_\lambda p_\lambda\log_2 p_\lambda=0.4577+0.1659+0.4453+0.4719=$ **1.540656** → **A**. (4 distinct outcomes ⇒ $H$ can exceed 1.)

**Watch out.** `O` here is degenerate (e.g. eigenvalue 25 repeated) → often just **2 distinct outcomes** → `H ≤ 1` effectively a binary entropy. Use eigen*spaces*, not individual eigenvectors.

**Theory:** [C4/09 distinct-eigenvalue entropy](../proofs/C4/09-distinct-eigenvalues-entropy-independent.md). Notebook: `ans["Q4"]`.

---

## Q5 — Probability two `O`-measurements give the same result
**Asks:** measure `O` on two independent copies of `ρ_v`; chance both give the same outcome?

**Concept.** Collision probability of the outcome distribution from Q4.

**Formula.** $\sum_\lambda p_\lambda^2$ (same `p_λ` as Q4).

**Example (6223).** Same $p_\lambda=\{0.5771,0.0340,0.1800,0.2089\}$ as Q4:
$$\sum_\lambda p_\lambda^2=0.5771^2+0.0340^2+0.1800^2+0.2089^2=0.3330+0.0012+0.0324+0.0436=\textbf{0.410282}\ \to\ \textbf{D}.$$

**Watch out.** Q4 and Q5 share the same number set in the options (one is the entropy `−Σp log p`, the other is `Σp²`) — don't mix them up.

**Theory:** [lesson7-update/01 collision entropy](../proofs/lesson7-update/01-renyi-and-collision-entropy.md). Notebook: `ans["Q5"]`.

---

## Q6 — Max-over-bases collision for two samples of `|v⟩`
**Asks:** if you could measure two copies of `ρ_v` in *any* orthonormal basis, the **largest** probability of the same result?

**Concept.** Collision probability `Σ_k ⟨b_k|ρ_v|b_k⟩²` is maximized in the **eigenbasis** of `ρ_v` (majorization), where it equals the purity.

**Formula.** $\max = \text{Tr}(\rho_v^2) = \sum_i \lambda_i^2$.

**Example (6223).** $\rho_v$ eigenvalues $\{0.1667,0.8333\}$:
$$\text{Tr}(\rho_v^2)=0.1667^2+0.8333^2=0.0278+0.6944=\textbf{0.722222}\ \to\ \textbf{A}.$$
(Distractor $w_0^2+w_1^2=0.7222^2+0.2778^2=0.598765$, option D — only correct if $|\phi\rangle\perp|\psi\rangle$.)

**Watch out.** Distractors: `0.5` (the maximally-mixed value) and `w₀²+w₁²` (what you'd get only if `|φ⟩⊥|ψ⟩`, which they usually aren't — the real answer is a bit larger because of the overlap term).

**Theory:** [C4/11 majorization / best basis](../proofs/C4/11-von-neumann-entropy-is-the-minimum.md). Notebook: `ans["Q6"]`.

---

## Q7 — Minimal number of Kraus operators of `ℰ`
**Asks:** the fewest Kraus operators needed to write `ℰ(ρ)=Σ_k K_k ρ K_k†`?

**Concept.** Choi's theorem: minimal #Kraus = **rank of the Choi matrix** `J_ℰ`.

**Formula.** Build `J_ℰ = (I⊗ℰ)(|Ω⟩⟨Ω|)`, count eigenvalues `> tol`. Answer is an integer in **{1,2,3,4}**.

**Example (6223).** Build $J_{\mathcal E}$ (16×16) and take its eigenvalues: $\{0,\dots,0,\ 0.5,\ 0.5,\ 0.5,\ 2.5\}$ → **4** nonzero → rank **4** → **D**. (Intuition: `O` has 4 distinct eigenvalues, so the dephasing part needs 4 independent operators.)

**Watch out.** Rank 1 ⇔ `ℰ` is a unitary (it isn't here, because of the measurement part). The explicit Kraus set `{√½ I}∪{√½ E_λ}` may be *linearly dependent*, so its size overcounts — the true minimum is the Choi rank.

**Theory:** [C5/06 Choi's theorem](../proofs/C5/06-chois-theorem.md). Notebook: `ans["Q7"]`.

---

## Q8 — Quantum fidelity of `|w⟩` to `|v⟩`
**Asks:** how similar are `ρ_w = ℰ(ρ_v)` and `ρ_v`? (1 = identical, 0 = orthogonal)

**Formula (course convention — SQUARED).**
$$F(\rho_v,\rho_w)=\Big(\text{Tr}\sqrt{\sqrt{\rho_v}\,\rho_w\,\sqrt{\rho_v}}\Big)^2.$$

**Example (6223).** Step by step:
1. $M=\sqrt{\rho_v}\,\sqrt{\rho_w}$.
2. singular values of $M$: $\{0.7332,\ 0.1694,\ 0,\ 0\}$.
3. $\text{Tr}|M|=0.7332+0.1694=0.902552$.
4. $F=(\text{Tr}|M|)^2=0.902552^2=$ **0.814600** → **A**. (Trap: stopping at step 3 gives $0.902552$ = option B, the *unsquared* fidelity.)

**⚠ Biggest trap on the exam.** Every variant lists both the **squared** value and its **square root** (the Nielsen–Chuang *unsquared* fidelity) as options. The course uses **squared** ($F=\text{Tr}^2(\sqrt\rho\sqrt\sigma)$, and `F(ρ,|φ⟩⟨φ|)=⟨φ|ρ|φ⟩` only holds squared). Pick the squared one. (6223: A=0.8146 squared ✓, B=0.9026=√A is the unsquared trap.)

**Theory:** [C7/04 Uhlmann](../proofs/C7/04-uhlmann-theorem.md). Notebook: `ans["Q8"]`.

---

## Q9 — Entanglement fidelity of `ℰ` applied to `|v⟩`
**Asks:** how well does `ℰ` preserve `ρ_v`, tested against an entangled reference (the strict "quality of service" measure)?

**Formula.** $F(\rho_v,\mathcal E)=\sum_k |\text{Tr}(K_k\,\rho_v)|^2$ (representation-independent). For *this* channel it simplifies to $\tfrac12+\tfrac12\sum_\lambda p_\lambda^2 = \tfrac12+\tfrac12\,(\text{Q5})$.

**Example (6223).** 5 Kraus operators $\{\sqrt{\tfrac12}I,\ \sqrt{\tfrac12}E_{21},\ \sqrt{\tfrac12}E_{105},\ \sqrt{\tfrac12}E_{189},\ \sqrt{\tfrac12}E_{273}\}$ ⇒ $\text{Tr}(K_k\rho_v)=\{0.7071,\ 0.4081,\ 0.0240,\ 0.1273,\ 0.1477\}$.
$$F=\sum_k|\text{Tr}(K_k\rho_v)|^2=0.5+0.1666+0.0006+0.0162+0.0218=\textbf{0.705141}\ \to\ \textbf{D}.$$
(Check: $=\tfrac12+\tfrac12\cdot\text{Q5}=\tfrac12+\tfrac12\cdot0.410282$.)

**Watch out.** Different from Q8: Q8 compares two *states*; Q9 grades the *channel* against an entangled input. It's already a "squared-type" probability — no extra square root.

**Theory:** [C7/05 entanglement fidelity](../proofs/C7/05-entanglement-fidelity.md). Notebook: `ans["Q9"]` (cross-checked via purification).

---

## Q10 — Entropy exchanged when `ℰ` is applied to `|v⟩`
**Asks:** how much entropy leaks into the environment when `ρ_v` passes through `ℰ`?

**Formula.** Build the matrix `W_{kl}=Tr(K_k ρ_v K_l†)` over the Kraus operators (it's a density matrix on the Kraus index); the entropy exchange is
$$H(\rho_v,\mathcal E)=H(W)=-\sum_i \mu_i\log_2\mu_i\quad(\mu_i=\text{eigenvalues of }W).$$
Equivalently `H((I⊗ℰ)(|Ω_v⟩⟨Ω_v|))` for a purification `|Ω_v⟩`.

**Example (6223).** Step by step:
1. Form $W$ (5×5), $W_{kl}=\text{Tr}(K_k\rho_v K_l^\dagger)$.
2. Its eigenvalues: $\{0,\ 0.0207,\ 0.0961,\ 0.1606,\ 0.7227\}$.
3. $H(W)=-\sum_i\mu_i\log_2\mu_i=$ **1.202687** → **C**.

**Watch out.** Can exceed 1 (it lives on the Kraus/environment space, dimension = #Kraus). Pairs with Q9 in the quantum Fano inequality (high fidelity ⇒ low entropy exchange).

**Theory:** [C7/06 quantum Fano](../proofs/C7/06-quantum-fano.md). Notebook: `ans["Q10"]` (cross-checked via purification).

---

## Bonus — Eve's probability to guess a 256-bit key (BB84 / Berta)
**Asks:** given the measured bit-error rate `δ_bit` (Z basis) and phase-error rate `δ_phase` (X basis), bound how well an eavesdropper Eve can guess the key.

**Concept.** Recast BB84 as an entangled-pair protocol; the Berta tripartite uncertainty relation says Eve and Bob can't both know the `X` and `Z` results. Low measured error ⇒ Bob knows a lot ⇒ Eve must be ignorant.

**Formula.** With binary entropy `h(·)`:
$$h(p)\ge 1-\tfrac12 h(\delta_{\text{bit}})-\tfrac12 h(\delta_{\text{phase}})\ \Rightarrow\ p\le \tfrac12\Big(1+\sqrt{\ln 2\,(h(\delta_{\text{bit}})+h(\delta_{\text{phase}}))}\Big),$$
then the naive per-key bound is `p^256`.

**Example (6223).** $\delta_{\text{bit}}=0.09,\ \delta_{\text{phase}}=0.07$ → $h(0.09)=0.4365,\ h(0.07)=0.3659$ →
$$p\le\tfrac12\big(1+\sqrt{\ln2\,(0.4365+0.3659)}\big)=\tfrac12(1+\sqrt{0.5563})=\tfrac12(1+0.7458)=\textbf{0.8729}\ \text{per bit}\ \to\ p^{256}\approx 7.68\times10^{-16}.$$

**Watch out.** No multiple-choice key for the bonus. The `p^256` is the simple bound; the parity cross-checks (forcing expected error ≤ `eps_target`) refine it as in the lecture's worked example.

**Theory:** [C6/11 memory uncertainty](../proofs/C6/11-uncertainty-with-quantum-memory.md), [C6/13 BB84](../proofs/C6/13-bb84-security.md). Notebook: `ans["_bonus"]`.

---

## Worked example — paper 6223 (real numbers)

Inputs: $|\phi\rangle=\tfrac1{\sqrt{650}}[9,8,8,21]$, $|\psi\rangle=\tfrac1{\sqrt{2450}}[-21,28,28,21]$, weights $w_0=\tfrac{13}{18}=0.7222$, $w_1=\tfrac{5}{18}=0.2778$, and
$$O=\begin{pmatrix}191&-12&-80&2\\-12&93&-24&-12\\-80&-24&113&-80\\2&-12&-80&191\end{pmatrix}.$$
First build $\rho_v=w_0|\phi\rangle\langle\phi|+w_1|\psi\rangle\langle\psi|$ → eigenvalues $\{0,\,0,\,0.1667,\,0.8333\}$ (rank 2, as expected for a mix of 2 states). $O$ has eigenvalues $\{21,105,189,273\}$ (4 distinct).

| Q | Plug in the numbers | Result | Pick |
|---|---|---|---|
| **1** | $\rho_A=MM^\dagger$ of $|\psi\rangle$ has eigenvalues $\{0.5,0.5\}$; $H=-0.5\log_2 0.5-0.5\log_2 0.5$ | **1.000000** | **B** |
| **2** | PPT eigenvalues $\{0,0,0.1667,0.8333\}$, min $=0$ (not $<0$) ⇒ **not entangled** | **separable** | **D** |
| **3** | $H(\rho_v)=-0.1667\log_2 0.1667-0.8333\log_2 0.8333$ | **0.650022** | **A** |
| **4** | distinct eigenvalues $\{21,105,189,273\}$; $p=\{0.5771,0.0340,0.1800,0.2089\}$; $H=-\sum p\log_2 p$ | **1.540656** | **A** |
| **5** | $\sum_\lambda p_\lambda^2=0.5771^2+0.0340^2+0.1800^2+0.2089^2$ | **0.410282** | **D** |
| **6** | $\text{Tr}(\rho_v^2)=0.1667^2+0.8333^2$ (distractor $w_0^2+w_1^2=0.598765$=D) | **0.722222** | **A** |
| **7** | $\text{rank}\,J_{\mathcal E}$ — Choi eigenvalues $\{0,\dots,0.5,0.5,0.5,2.5\}$, 4 nonzero | **4** | **D** |
| **8** | $\big(\text{Tr}|\sqrt{\rho_v}\sqrt{\rho_w}|\big)^2=0.902552^2$ (trap: $0.902552$=B, unsquared) | **0.814600** | **A** |
| **9** | $\sum_k|\text{Tr}(K_k\rho_v)|^2=\tfrac12+\tfrac12(0.410282)$ | **0.705141** | **D** |
| **10** | $H(W)$, $W$ eigenvalues $\{0,0.0207,0.0961,0.1606,0.7227\}$ | **1.202687** | **C** |

**Q2 detail:** the partial transpose of $\rho_v$ has no negative eigenvalue (min $=0$) ⇒ $\rho_v$ is separable, so the answer is **D** regardless of `O`. (Here also $\text{Tr}(O\rho_v)=+106.73>0$, so `O` wouldn't fire anyway.)

**Bonus:** $\delta_{\text{bit}}=0.09,\ \delta_{\text{phase}}=0.07$. $h(0.09)=0.4365$, $h(0.07)=0.3659$.
$$p\le\tfrac12\Big(1+\sqrt{\ln2\,(0.4365+0.3659)}\Big)=0.8729,\qquad p^{256}\approx7.68\times10^{-16}.$$

**Final answer row (6223):** Q1–Q10 = **B, D, A, A, D, A, D, A, D, C**.

---

## Quick relationships (sanity checks)
- **Q9 = ½ + ½·Q5** (for this specific channel).
- **Q5 ≤ 1** and **Q6 = Tr ρ²**; Q5 (coarse `O`-measurement) can be *larger* than Q6 (best rank-1 basis) — different measurements.
- **Q1 ≤ 1** and **Q3 ≤ 1** (two-qubit pure / rank-2 mixed); options above 1 are distractors.
- **Q8 squared, Q9 squared-type** — internally consistent; if Q8 "looks like √(an option)", you forgot to square.
