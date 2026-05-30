# Prompt — Python notebook to solve the QIT final exam (Part II)

> Paste into an AI coding assistant. It builds a Jupyter notebook that takes the exam's inputs and computes all 10 answers + the bonus. The underlying theory is the Quantum Information Theory course (lectures C4–C7); the per-result references below point at the relevant theorems.

You are to implement a **single, well-documented Jupyter notebook** (`qit_exam_solver.ipynb`) using only `numpy` and `scipy`. It must take the inputs of a "Quantum Information Theory — Final Exam, Part II" problem and compute the numerical answer to each of the 10 multiple-choice questions and the bonus. Every exam variant has the **same structure** (only the numbers change), so write it parameterized.

## Inputs (per exam variant)
```python
phi_raw   = [...]          # length-4 real vector (two-qubit, unnormalized)
phi_norm  = 725            # |phi> = phi_raw / sqrt(phi_norm)
psi_raw   = [...]          # length-4 real vector
psi_norm  = 1250           # |psi> = psi_raw / sqrt(psi_norm)
v_weights = (203/703, 500/703)   # |v> is the RANDOM state: |phi> w.p. w0, |psi> w.p. w1
O_matrix  = [[...],...]     # 4x4 Hermitian observable (integer entries)
O_prefactor = 1            # actual observable is O = O_prefactor * O_matrix  (often 1/1 = 1)
# Bonus:
delta_bit   = 0.08         # Z-basis (bit) error rate
delta_phase = 0.02         # X-basis (phase) error rate
eps_target  = 1e-6         # target expected error after parity cross-checks
key_length  = 256
```

## Conventions (use exactly these — they match the course)
- **All entropies are in bits → use `log2`.** `xlog2x(0)=0`.
- **Two-qubit ordering:** basis `|00>,|01>,|10>,|11>`; a state vector `v` reshapes to the amplitude matrix `M = v.reshape(2,2)` with row index = **first** qubit (A), column index = **second** qubit (B). Reduced state of A is `rho_A = M @ M.conj().T`.
- **von Neumann entropy** `H(rho) = -sum λ_i log2 λ_i` over eigenvalues `λ_i>0` (use `scipy.linalg.eigh`, clip tiny negatives).
- **Fidelity convention (course C7/Uhlmann):** `F(rho,sigma) = ( Tr | sqrt(rho) sqrt(sigma) | )^2 = ( Tr sqrt( sqrt(rho) sigma sqrt(rho) ) )^2` — i.e. **squared**. Use `scipy.linalg.sqrtm`, take real part, clip.
- Numerical tolerances: treat eigenvalues `< 1e-9` as zero; group "equal" eigenvalues of `O` with tolerance `1e-6` (degeneracies matter!).

## Derived objects (build once)
- `phi`, `psi` = normalized state vectors. `O = O_prefactor * O_matrix`.
- **Mixed state** `rho_v = w0 |phi><phi| + w1 |psi><psi|`.
- **Spectral projectors of `O`:** eigendecompose `O`; group eigenvectors by **distinct** eigenvalue; `E_lambda` = projector onto each eigenspace (sum of `|e><e|`). Verify `sum E_lambda = I`.
- **Pinching / non-selective measurement** of `O`: `Delta_O(rho) = sum_lambda E_lambda @ rho @ E_lambda`.
- **The channel** `E`: "with prob 50% we observe `O` and forget the result, else do nothing":
  `E(rho) = 0.5*rho + 0.5*Delta_O(rho)`.
  Its **Kraus operators** are `{ sqrt(0.5)*I } ∪ { sqrt(0.5)*E_lambda for each distinct λ }` (check `sum K†K = I`).
- `rho_w = E(rho_v)`.
- **Purification** `|Omega_v>` of `rho_v` on a doubled space (for entanglement-fidelity / entropy-exchange cross-checks), e.g. `sum_i sqrt(μ_i) |i>_A ⊗ |i>_R` from the eigendecomposition `rho_v = sum μ_i |i><i|`.

## The 10 questions — exact computation + theory reference

**Q1. Entropy of entanglement of `|ψ⟩`.** (C6 — Schmidt decomposition / entanglement entropy.)
`M = psi.reshape(2,2); rho_A = M@M.conj().T; answer = H(rho_A)`. (≤ 1 bit; options > 1 are distractors.)

**Q2. Is `|v⟩` entangled / does `O` witness it?** (C5 — PnCP & PPT criteria, entanglement witnesses.) Compute:
1. `entangled = (min eigenvalue of the partial transpose of rho_v on qubit B) < -tol`  (PPT / Peres–Horodecki).
2. `O_is_valid_witness`: `O` Hermitian **and** `O` not PSD (has a negative eigenvalue) **and** block-positive, i.e. `min over product states |a>⊗|b> of <a,b|O|a,b> >= -tol` (numerically minimize over two Bloch-sphere angle pairs, many restarts).
3. `detects = Tr(O @ rho_v) < -tol`.
Decision: `D` if not `entangled`; else if `O_is_valid_witness and detects` → `A` (witnessed by O); else if `O_is_valid_witness and not detects` → `B` (entangled, not witnessed by O); else (`not O_is_valid_witness`) → `C` (entangled but O is not a witness). Print the booleans and `Tr(O rho_v)`.

**Q3. Minimal average qubits for lossless encoding of `|v⟩`.** (C7 — Schumacher source coding: `min R = H(rho)`.)
`answer = H(rho_v)` (von Neumann entropy of the mixed state). (≤ 1 bit here.)

**Q4. Entropic uncertainty of measuring `O` on `|v⟩`.** (C4 — measurement entropy.)
Distinct-eigenvalue probabilities `p_lambda = Tr(E_lambda @ rho_v)`; `answer = -sum p_lambda log2 p_lambda`. (O is degenerate → few outcomes; this is effectively a binary entropy.)

**Q5. Probability that two `O`-measurements of `|v⟩` give the same result.** (C4 / collision probability.)
`answer = sum_lambda p_lambda**2` (same `p_lambda` as Q4).

**Q6. Max over orthonormal (rank-1 projective) bases of the collision probability for two samples of `|v⟩`.** (C4 — majorization; max at the eigenbasis.)
`answer = Tr(rho_v @ rho_v) = sum μ_i**2` (purity), where `μ_i` are eigenvalues of `rho_v`.

**Q7. Minimal number of Kraus operators of `E`.** (C5 — Choi's theorem: minimal Kraus = rank of the Choi matrix.)
Build the Choi matrix `J_E = (I ⊗ E)(|Ω><Ω|)` with `|Ω> = sum_i |i>|i>` (unnormalized maximally entangled, dimension 4), apply `E` to the second factor block-wise; `answer = number of eigenvalues of J_E above tol` (an integer in {1,2,3,4}).

**Q8. Quantum fidelity of `|w⟩` to `|v⟩`.** (C7 — Uhlmann's theorem.)
`answer = F(rho_v, rho_w)` using the squared convention above.

**Q9. Entanglement fidelity of `E` applied to `|v⟩`.** (C7 — entanglement fidelity.)
`answer = sum_k |Tr(K_k @ rho_v)|**2` over the Kraus operators of `E` (representation-independent). Cross-check via `<Omega_v|(I⊗E)(|Omega_v><Omega_v|)|Omega_v>`.

**Q10. Entropy exchanged when `E` is applied to `|v⟩`.** (C7 — entropy exchange / quantum Fano.)
Form the matrix `W` with `W[k,l] = Tr(K_k @ rho_v @ K_l.conj().T)` over the Kraus operators (this is a density matrix on the Kraus index); `answer = H(W)` (von Neumann entropy of `W`). Cross-check: equals `H((I⊗E)(|Omega_v><Omega_v|))`.

**BONUS. BB84 / Berta et al. — Eve's probability to guess a 256-bit key.** (C6 — uncertainty with quantum memory; BB84 security.)
With binary entropy `h(x) = -x log2 x - (1-x) log2(1-x)`:
1. From the tripartite/Berta uncertainty relation `H(X|B)+H(Z|E) ≥ 1` and `H(Z|B)+H(X|E) ≥ 1`, averaging gives `h(p) ≥ 1 - ½h(delta_bit) - ½h(delta_phase)`, so Eve's per-bit guess probability
   `p ≤ ½ ( 1 + sqrt( ln(2) * ( h(delta_bit) + h(delta_phase) ) ) )`.
2. Report `p` (per-bit) and the per-key bound `p**key_length`.
3. Follow the lecture's parity-cross-check refinement: to force the expected mismatch `≤ eps_target` over a 256-bit key, account for the leaked parity bits (Eve gains information per round); recompute the refined `h(p)` and `p`, and report the refined probability that Eve shares the whole key. Document the steps and cite C6's BB84 derivation; print intermediate quantities.

## Output & validation
- Wrap everything in `solve_exam(inputs: dict) -> dict` returning every answer, and a pretty printer that lists `Q1..Q10` with the computed value.
- Accept an optional `options` dict mapping each question to its 4 choices `{'A':..,'B':..,'C':..,'D':..}`; print the **closest** option and the absolute gap, so I can read off the letter.
- Include **all four 2025 variants below as test cases** in the final cells, run `solve_exam` on each, and display a table of chosen letters. Add `assert`-style sanity checks (probabilities in `[0,1]`, entropies ≥ 0, Q1 & Q3 ≤ 1 bit, Q7 ∈ {1,2,3,4}, fidelities in `[0,1]`).
- Markdown cells must briefly explain each formula and link it to the course result (Schmidt/Schumacher/Uhlmann/Choi/entropy-exchange/Berta), so the notebook doubles as revision.

### Test variants (paper IDs)
```python
# 3109
phi_raw=[13,6,6,22]; phi_norm=725;  psi_raw=[-27,16,16,-3]; psi_norm=1250
v_weights=(203/703,500/703); O_prefactor=1
O_matrix=[[7,0,0,6],[0,25,0,0],[0,0,25,0],[6,0,0,23]]
delta_bit=0.08; delta_phase=0.02; eps_target=1e-6
# 3992
phi_raw=[7,4,4,13]; phi_norm=250;  psi_raw=[-14,22,22,19]; psi_norm=1525
v_weights=(100/161,61/161); O_prefactor=1
O_matrix=[[125,-48,14,-20],[-48,51,-48,-96],[14,-48,29,28],[-20,-96,28,95]]
delta_bit=0.03; delta_phase=0.10; eps_target=1e-3
# 6572
phi_raw=[21,-8,-8,9]; phi_norm=650;  psi_raw=[-1,2,2,2]; psi_norm=13
v_weights=(5/17,12/17); O_prefactor=1
O_matrix=[[77,0,-20,32],[0,9,0,0],[-20,0,17,-20],[32,0,-20,77]]
delta_bit=0.02; delta_phase=0.05; eps_target=1e-6
# 6223
phi_raw=[9,8,8,21]; phi_norm=650;  psi_raw=[-21,28,28,21]; psi_norm=2450
v_weights=(13/18,5/18); O_prefactor=1
O_matrix=[[191,-12,-80,2],[-12,93,-24,-12],[-80,-24,113,-80],[2,-12,-80,191]]
delta_bit=0.09; delta_phase=0.07; eps_target=1e-5
```
The chosen letters should match the printed exam options; if any computed value sits between two options, surface it so I can flag a convention issue (especially the fidelity squared-vs-not convention and the bonus refinement).
```
```
