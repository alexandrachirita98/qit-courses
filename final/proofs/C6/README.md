# C6 — Quantum Data Processing: Proof Pack (oral exam prep)

Same 5-part format as the [C4 pack](../C4/README.md). Generating prompt: [PROMPT.md](PROMPT.md).

## Core results
| # | File | Result |
|---|------|--------|
| 01 | [01-umegaki-divergence-nonnegative.md](01-umegaki-divergence-nonnegative.md) | $D(\rho\|\sigma)\ge0$, $=0$ iff $\rho=\sigma$; $=\infty$ on support mismatch |
| 02 | [02-data-processing-inequality.md](02-data-processing-inequality.md) | $D(\mathcal E\rho\|\mathcal E\sigma)\le D(\rho\|\sigma)$ |
| 03 | [03-bistochastic-cant-decrease-entropy.md](03-bistochastic-cant-decrease-entropy.md) | Unital channel ⇒ $H(\mathcal E\rho)\ge H(\rho)$ |
| 04 | [04-reduced-states-marginals.md](04-reduced-states-marginals.md) | Measuring a half = $\mathcal E_A(\text{Tr}_B\rho)$; reduced states as marginals |
| 05 | [05-no-communication-theorem.md](05-no-communication-theorem.md) | $\text{Tr}_B((I_A\otimes\mathcal E)\rho)=\text{Tr}_B\rho$ |
| 06 | [06-quantum-mutual-information.md](06-quantum-mutual-information.md) | $I(A{:}B)=H(A)+H(B)-H(AB)$ |
| 07 | [07-quantum-classical-mutual-info.md](07-quantum-classical-mutual-info.md) | QC state: $I(A{:}B)=$ Holevo $\chi$ |
| 08 | [08-holevo-theorem.md](08-holevo-theorem.md) | Monotonicity of mutual info ⇒ Holevo bound |
| 09 | [09-conditional-von-neumann-entropy.md](09-conditional-von-neumann-entropy.md) | $H(A|B)$, its monotonicities, $\ge0$ for separable |
| 10 | [10-schmidt-decomposition.md](10-schmidt-decomposition.md) | Schmidt decomposition; equal reduced-state entropies |
| 11 | [11-uncertainty-with-quantum-memory.md](11-uncertainty-with-quantum-memory.md) | Berta et al. memory-assisted uncertainty |
| 12 | [12-tripartite-uncertainty.md](12-tripartite-uncertainty.md) | Tripartite uncertainty relation |
| 13 | [13-bb84-security.md](13-bb84-security.md) | BB84 security from uncertainty relations |

## Study order
01 → 02 (divergence + DPI: the engine) → 03 (entropy & unital). Then the bipartite story 04 → 05 → 06 → 07 → 08. Then 09 (conditional entropy) → 10 (Schmidt) → 11 → 12 (memory/tripartite uncertainty) → 13 (BB84). The examiner's favorites: **02 (DPI)**, **06**, **09**.

> Notation: $D(\rho\|\sigma)=-\text{Tr}(\rho(\log\sigma-\log\rho))$ Umegaki divergence; $H(\rho)=-\text{Tr}\rho\log\rho$; $H(AB)=H(\rho_{AB})$; $I(A{:}B)$ mutual information; $H(A|B)=H(AB)-H(B)$ conditional entropy; $\mathcal E$ a channel; $\Delta_1$ the completely depolarizing channel.
