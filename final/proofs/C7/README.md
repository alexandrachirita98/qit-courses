# C7 — Quantum Compression: Proof Pack (oral exam prep)

Same 5-part format as the [C4 pack](../C4/README.md). Generating prompt: [PROMPT.md](PROMPT.md).

> The reworked **lesson-7 update** (min-entropy, universal hashing, leftover hashing, privacy amplification) has its own pack: [../lesson7-update/](../lesson7-update/README.md). The discrimination → Pinsker → fidelity → Schumacher results below are shared by both lectures.

## Core results
| # | File | Result |
|---|------|--------|
| 01 | [01-helstrom-bound.md](01-helstrom-bound.md) | Optimal state discrimination; success $=\tfrac12+\tfrac12\|p\rho-(1-p)\sigma\|_{\text{Tr}}$ |
| 02 | [02-quantum-pinsker.md](02-quantum-pinsker.md) | $\|\rho-\sigma\|_{\text{Tr}}\le\sqrt{2\ln2\,D(\rho\|\sigma)}$ |
| 03 | [03-fidelity-and-discrimination.md](03-fidelity-and-discrimination.md) | Entanglement-assisted discrimination; fidelity = max purification overlap |
| 04 | [04-uhlmann-theorem.md](04-uhlmann-theorem.md) | $F(\rho,\sigma)=(\text{Tr}|\sqrt\rho\sqrt\sigma|)^2$ |
| 05 | [05-entanglement-fidelity.md](05-entanglement-fidelity.md) | Entanglement fidelity; $F(\rho,|\phi\rangle\langle\phi|)=\langle\phi|\rho|\phi\rangle$ |
| 06 | [06-quantum-fano.md](06-quantum-fano.md) | Quantum Fano inequality |
| 07 | [07-schumacher-source-coding.md](07-schumacher-source-coding.md) | $\min R=H(\rho)$ |

## Study order
01 → 02 (discrimination + Pinsker: distinguishability ↔ entropy). Then the fidelity arc 03 → 04 → 05 → 06, then **07 (Schumacher)** as the headline compression theorem. Examiner favorites: **01 (Helstrom)**, **04 (Uhlmann)**, **07 (Schumacher)**.

> Notation: $\|A\|_{\text{Tr}}=\text{Tr}|A|=\text{Tr}\sqrt{A^\dagger A}$ trace norm; $D(\rho\|\sigma)$ Umegaki divergence ([../C6/01](../C6/01-umegaki-divergence-nonnegative.md)); $F(\rho,\sigma)$ fidelity; $h(\cdot)$ binary entropy; $H(\rho)$ von Neumann entropy.
