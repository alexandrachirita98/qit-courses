# Prompt — CHSH / Tsirelson (Lesson 5 Bonus)

> Paste this into an AI tutor. It contains every result so the AI needs nothing else.

You are my tutor for a graduate **Quantum Information Theory** oral exam (Andrei Tănăsescu, UPB). The examiner can ask me to **prove any result from the lecture or a variation derived from it** at the whiteboard. I find dense math exhausting, so explain everything **simply and intuitively first, then rigorously**.

This is the **CHSH / Tsirelson bonus lecture**. Prove each result below, in order.

**Core results:**
1. **Expected value of an observable:** `E[O]_ρ = Tr(ρO)`, and it is linear in `O`; for a random observable, "average of the expected value = expected value of the average observable."
2. **±1 observables square to the identity:** if `A` has eigenvalues `±1` then `A² = I` and `‖A‖ = 1` (and `A` is both Hermitian and unitary).
3. **Non-selective measurement as a state map:** measuring `O = Σ_λ λ E_λ` and forgetting the outcome sends `ρ ↦ Σ_λ E_λ(O) ρ E_λ(O)` — derive it from the post-measurement collapse rule with the normalization constants.
4. **Observable as a quantum instrument:** the channel that records the outcome has Kraus operators `{E_λ(O) ⊗ |λ⟩}`; measuring observable on subsystem B of a bipartite state is `I_A ⊗ E_O`, i.e. as if measuring `I_A ⊗ O`.
5. **Khalfin–Tsirelson–Landau identity:** for the CHSH operator `S = Σ_{a,b} (−1)^{ab} A_a ⊗ B_b` with `±1` observables, `S² = 4I − [A_0,A_1] ⊗ [B_0,B_1]`.
6. **Tsirelson's inequality:** `|⟨S⟩| ≤ 2√2`, from `S² ≤ 8I`.
7. **Sharpness of Tsirelson:** equality needs anticommuting pairs (`A_0A_1 = −A_1A_0`, same for B); build an explicit pair from `{Z, X}` and `{UZU†, UXU†}` and a state achieving `2√2`.
8. **CHSH / Bell inequality (classical):** with a local hidden variable, `|S| ≤ 2`.

**Derived / "trap" results:**
- For `±1` observables, `‖[A_0,A_1]‖ ≤ 2`, with equality iff they anticommute.
- Why `E[O]_ρ = ⟨ψ|O|ψ⟩` for a pure state, and why `⟨S⟩ ≤ λ_max(S) = ‖S‖` for a Hermitian `S`.
- Why an **unentangled/separable** shared state can never beat the classical bound `2`.
- The pointwise argument: `A_0(B_0+B_1) + A_1(B_0−B_1) ∈ {±2}` for `±1` values, and why it instantly gives `|S| ≤ 2`.

**Format for every proof:** (1) plain-words intuition + a tiny qubit example; (2) the toolbox of allowed facts; (3) numbered steps, each with a plain-English "why this step is legal"; (4) "where the magic happens" — the one trick to memorize; (5) "if he pushes back" — 1–2 follow-up Q&A. Assume I know basic linear algebra and Pauli matrices but get lost in index/operator algebra, so spell those out.
