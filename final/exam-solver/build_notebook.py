"""Generate qit_exam_solver.ipynb from the validated solver."""
import nbformat as nbf
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

nb = new_notebook()
cells = []

cells.append(new_markdown_cell(
"""# QIT Final Exam — Part II solver

Computes all 10 multiple-choice answers + the bonus for the *Quantum Information Theory*
final (Part II). Every paper variant shares the **same structure** — only the numbers
change — so just edit the **Inputs** cell and re-run.

**Theory map** (see `final/proofs/`):
| Q | Quantity | Result |
|---|----------|--------|
| 1 | entanglement entropy of \\|ψ⟩ | C6 Schmidt decomposition |
| 2 | is \\|v⟩ entangled / does O witness it | C5 PnCP + PPT, entanglement witnesses |
| 3 | min qubits to encode \\|v⟩ | C7 Schumacher (`minR=H(ρ)`) |
| 4 | entropic uncertainty of measuring O | C4 measurement entropy |
| 5 | collision prob of two O-measurements | C4 collision probability |
| 6 | max-basis collision (two samples) | C4 majorization → `Tr ρ²` |
| 7 | min Kraus operators of ℰ | C5 Choi rank |
| 8 | fidelity of \\|w⟩ to \\|v⟩ | C7 Uhlmann |
| 9 | entanglement fidelity of ℰ | C7 entanglement fidelity |
| 10 | entropy exchange of ℰ | C7 / quantum Fano |
| Bonus | Eve's key-guess probability | C6 Berta uncertainty / BB84 |

**Conventions:** entropies in **bits** (`log2`); two-qubit ordering `|00>,|01>,|10>,|11>`;
amplitude matrix `M = v.reshape(2,2)` with row = qubit A, col = qubit B, so `ρ_A = M M†`;
**fidelity is squared** `F=(Tr√(√ρ σ √ρ))²` (course/Uhlmann convention)."""))

cells.append(new_markdown_cell("## 1. Library functions (run once)"))

with open("solver.py") as f:
    src = f.read()
# strip the __main__ block and VARIANTS dict for the functions cell
core = src.split("# ----------------------------- variants -----------------------------")[0]
core = core.replace('"""QIT Final Exam Part II — solver (validation script).\n\n'
                    'Implements the 10 questions + bonus, parameterized by the exam inputs.\n'
                    'Theory references: course lectures C4-C7 (see final/proofs/).\n"""\n', "")
cells.append(new_code_cell(core.strip()))

cells.append(new_markdown_cell(
"""## 2. Inputs — edit this cell for your exam paper

`v_weights` are the two probabilities under the `(|φ⟩ |ψ⟩ ; p₀ p₁)` row in the problem.
`O_prefactor` is the scalar in front of the matrix (the papers show `1/1 = 1`)."""))

cells.append(new_code_cell(
"""inputs = dict(
    phi_raw=[13, 6, 6, 22], phi_norm=725,
    psi_raw=[-27, 16, 16, -3], psi_norm=1250,
    v_weights=(203/703, 500/703),
    O_prefactor=1,
    O_matrix=[[7, 0, 0, 6],
              [0, 25, 0, 0],
              [0, 0, 25, 0],
              [6, 0, 0, 23]],
    # bonus:
    delta_bit=0.08, delta_phase=0.02, eps_target=1e-6, key_length=256,
)

# OPTIONAL: paste the four printed choices per question to auto-pick the letter.
options = {
    "Q1": dict(A=0.867117, B=0.141441, C=1.742312, D=1.441988),
    "Q3": dict(A=0.831474, B=1.878090, C=0.576334, D=0.867117),
    "Q4": dict(A=0.622528, B=0.540508, C=0.780658, D=0.940744),
    "Q5": dict(A=0.540508, B=0.940744, C=0.780658, D=0.622528),
    "Q6": dict(A=0.589243, B=0.612188, C=0.285043, D=0.500000),
    "Q7": dict(A=1, B=2, C=3, D=4),
    "Q8": dict(A=0.770254, B=0.901849, C=0.877641, D=0.813331),
    "Q9": dict(A=0.813331, B=0.901849, C=0.770254, D=0.877641),
    "Q10": dict(A=0.762480, B=0.970372, C=1.427005, D=0.595530),
}"""))

cells.append(new_markdown_cell("## 3. Solve & report"))

cells.append(new_code_cell(
"""ans = solve(inputs)

labels = {
    "Q1": "entanglement entropy of |psi>",
    "Q2": "is |v> entangled / witnessed by O",
    "Q3": "min qubits to encode |v>  (Schumacher H(rho_v))",
    "Q4": "entropic uncertainty of measuring O",
    "Q5": "P[same result], two O-measurements",
    "Q6": "max-basis collision prob (Tr rho^2)",
    "Q7": "min # Kraus operators of E (Choi rank)",
    "Q8": "fidelity F(|v>,|w>)  [squared]",
    "Q9": "entanglement fidelity of E",
    "Q10": "entropy exchange of E",
}
print(f"{'Q':<4}{'value':<26}{'pick':<6}{'gap':<12}description")
print("-" * 90)
for q in [f"Q{i}" for i in range(1, 11)]:
    val = ans[q]
    if q in options:
        letter, gap = closest(val, options[q])
        flag = "" if (gap is not None and gap < 1e-3) else "  <-- CHECK convention"
        print(f"{q:<4}{str(round(val,6) if isinstance(val,float) else val):<26}"
              f"{letter:<6}{gap:<12.2e}{labels[q]}{flag}")
    else:
        print(f"{q:<4}{str(val):<26}{'':<6}{'':<12}{labels[q]}")

print()
print("Q8 fidelity — SQUARED   (course/Uhlmann, Tr^2|VrhoVsigma|):", round(ans["Q8"], 6))
print("Q8 fidelity — UNSQUARED (Nielsen-Chuang, Tr|VrhoVsigma|)  :", round(ans["Q8_unsquared"], 6))
print("   (the exam lists BOTH as options; the course convention is the SQUARED one = Q8)")
print()
print("Q2 detail:", ans["_Q2"])
print(f"Q9 cross-check (purification): {ans['_Q9_check']:.6f}  (should equal Q9)")
print(f"Q10 cross-check (purification): {ans['_Q10_check']:.6f}  (should equal Q10)")"""))

cells.append(new_markdown_cell(
"""## 4. Bonus — Eve's probability to guess the key (Berta / BB84)

From the Berta et al. memory-assisted uncertainty relation (`H(X|B)+H(Z|E)≥1`, and the
`Z↔X` partner), averaging gives `h(p) ≥ 1 − ½h(δ_bit) − ½h(δ_phase)`, hence the per-bit
guessing probability `p ≤ ½(1+√(ln2·(h(δ_bit)+h(δ_phase))))`. `p_key = p^256` is the naive
per-key bound; the parity cross-checks (forcing expected error ≤ `eps_target`) refine it as
in the C6 BB84 derivation."""))

cells.append(new_code_cell(
"""b = ans["_bonus"]
print(f"per-bit guess prob  p   = {b['p_per_bit']:.6f}")
print(f"lower bound on h(p)     = {b['h_p_lower']:.6f}")
print(f"naive per-key bound p^{inputs['key_length']} = {b['p_key']:.3e}")"""))

cells.append(new_markdown_cell(
"""## 5. Validation — all four 2025 papers

Runs the solver on every known variant and prints the chosen letters. All gaps should be
~1e-7, confirming the formulas and conventions match the official answer key."""))

# embed VARIANTS dict + runner
variants_src = src.split("# ----------------------------- variants -----------------------------")[1]
variants_src = variants_src.split('if __name__ == "__main__":')[0]
runner = variants_src.strip() + """

print(f"{'paper':<8}" + "".join(f"Q{i:<5}" for i in range(1, 11)))
print("-" * 70)
for vid, inp in VARIANTS.items():
    a = solve(inp)
    row = []
    for q in [f"Q{i}" for i in range(1, 11)]:
        if q == "Q2":
            row.append(a[q].split()[0])  # letter
        elif q == "Q7":
            l, _ = closest(a[q], inp["options"].get(q, {"A":1,"B":2,"C":3,"D":4}))
            row.append(l)
        elif q in inp["options"]:
            l, g = closest(a[q], inp["options"][q])
            row.append(l + ("!" if g > 1e-3 else ""))
        else:
            row.append("?")
    print(f"{vid:<8}" + "".join(f"{r:<6}" for r in row))
"""
cells.append(new_code_cell(runner))

nb["cells"] = cells
nb["metadata"] = {
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python", "version": "3"},
}
with open("qit_exam_solver.ipynb", "w") as f:
    nbf.write(nb, f)
print("wrote qit_exam_solver.ipynb with", len(cells), "cells")
