# CHSH / Tsirelson — Proof Pack (oral exam prep)

Same 5-part format as the [C4 pack](../C4/README.md): plain words → toolbox → numbered steps → key trick → likely follow-ups.

The AI prompt that generated this pack: [PROMPT.md](PROMPT.md).

## Core results
| # | File | Result |
|---|------|--------|
| 01 | [01-expected-value-Tr-rho-O.md](01-expected-value-Tr-rho-O.md) | `⟨O⟩_ρ = Tr(ρO)`, linear; average commutes with expectation |
| 02 | [02-pm1-observables-square-to-identity.md](02-pm1-observables-square-to-identity.md) | `±1` eigenvalues ⇒ `A²=I`, `‖A‖=1`, Hermitian *and* unitary |
| 03 | [03-non-selective-measurement-channel.md](03-non-selective-measurement-channel.md) | Forgetting the outcome: `ρ ↦ Σ_λ E_λ ρ E_λ` |
| 04 | [04-observable-as-quantum-instrument.md](04-observable-as-quantum-instrument.md) | Kraus operators `{E_λ ⊗ |λ⟩}`; subsystem measurement `I_A ⊗ E_O` |
| 05 | [05-khalfin-tsirelson-landau-identity.md](05-khalfin-tsirelson-landau-identity.md) | `S² = 4I − [A_0,A_1]⊗[B_0,B_1]` |
| 06 | [06-tsirelson-bound.md](06-tsirelson-bound.md) | `|⟨S⟩| ≤ 2√2` |
| 07 | [07-tsirelson-sharpness.md](07-tsirelson-sharpness.md) | Anticommuting pairs reach `2√2`; explicit `Z,X` construction |
| 08 | [08-classical-chsh-bound.md](08-classical-chsh-bound.md) | Local hidden variable ⇒ `|S| ≤ 2` |

## Derived / "trap" results
| # | File | Result |
|---|------|--------|
| 09 | [09-commutator-norm-bound.md](09-commutator-norm-bound.md) | `‖[A_0,A_1]‖ ≤ 2`, equality iff anticommuting |
| 10 | [10-separable-states-obey-classical-bound.md](10-separable-states-obey-classical-bound.md) | Unentangled states can't beat `2` |

## Study order
02 → 09 → 05 → 06 (the Tsirelson chain), then 08 → 10 (classical side), then 01/03/04 (measurement formalism). The headline pair the examiner loves: **05 (KTL identity) → 06 (Tsirelson bound)**.

> Notation: `A_a, B_b` are `±1`-valued observables (eigenvalues `±1`); `S = A_0⊗B_0 + A_0⊗B_1 + A_1⊗B_0 − A_1⊗B_1`; `[A,B]=AB−BA`; `⟨S⟩ = Tr(ρS)`. The CHSH value is `|S| := |⟨S⟩|`.
