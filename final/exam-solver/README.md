# QIT Final Exam — Part II solver

A parameterized solver for the *Quantum Information Theory* final (Part II). Every paper
variant shares one template; only the numbers change.

## Files
- **[qit_exam_solver.ipynb](qit_exam_solver.ipynb)** — the notebook. Edit the **Inputs** cell
  (vectors `|φ⟩,|ψ⟩`, mixture weights for `|v⟩`, observable `O`, bonus error rates), run all,
  and read off the answers (with auto-matched A/B/C/D if you paste the options).
- [solver.py](solver.py) — the same logic as a plain script; `python3 solver.py` runs all four
  2025 variants and prints the chosen letters.
- [PROMPT.md](PROMPT.md) — the spec prompt used to generate this (for regenerating elsewhere).
- [build_notebook.py](build_notebook.py) — rebuilds the `.ipynb` from `solver.py`.

## What each question computes (theory in `../proofs/`)
| Q | Quantity | Formula |
|---|----------|---------|
| 1 | entanglement entropy of `\|ψ⟩` | `H(ρ_A)`, `ρ_A=MM†`, `M=ψ.reshape(2,2)` |
| 2 | is `\|v⟩` entangled / witnessed by `O` | PPT of `ρ_v` + `O` block-positive + `Tr(Oρ_v)<0` |
| 3 | min qubits to encode `\|v⟩` | `H(ρ_v)` (Schumacher) |
| 4 | entropic uncertainty of `O` | `−Σ p_λ log₂ p_λ`, `p_λ=Tr(E_λ ρ_v)` |
| 5 | collision prob, two `O`-measurements | `Σ_λ p_λ²` |
| 6 | max-basis collision (two samples) | `Tr(ρ_v²)` |
| 7 | min Kraus operators of `ℰ` | `rank(Choi(ℰ))` |
| 8 | fidelity `\|w⟩` to `\|v⟩` | `(Tr√(√ρ_v ρ_w √ρ_v))²` |
| 9 | entanglement fidelity of `ℰ` | `Σ_k\|Tr(K_k ρ_v)\|²` |
| 10 | entropy exchange of `ℰ` | `H(W)`, `W_{kl}=Tr(K_k ρ_v K_l†)` |
| Bonus | Eve's key-guess prob | `p≤½(1+√(ln2·(h(δ_bit)+h(δ_phase))))`, `p^256` |

Here `ρ_v = w₀\|φ⟩⟨φ\| + w₁\|ψ⟩⟨ψ\|`, the channel `ℰ(ρ)=½ρ+½Σ_λ E_λρE_λ` (observe `O` and
forget, w.p. 50%), and `ρ_w=ℰ(ρ_v)`. Conventions: bits (`log₂`), fidelity **squared**.

## Validation
`solver.py` reproduces the official answer key for all four 2025 papers (3109, 3992, 6572,
6223) with numerical gaps `< 5×10⁻⁷`:

| Paper | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 |
|-------|----|----|----|----|----|----|----|----|----|-----|
| 3109 | B | D | A | D | A | B | B | D | C | A |
| 3992 | D | D | D | B | B | D | D | B | D | A |
| 6572 | D | C | D | A | A | A | C | B | D | C |
| 6223 | B | D | A | A | D | A | D | A | D | C |
