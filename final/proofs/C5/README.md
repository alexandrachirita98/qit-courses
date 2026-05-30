# C5 — Quantum Channels: Proof Pack (oral exam prep)

Same 5-part format as the [C4 pack](../C4/README.md). Generating prompt: [PROMPT.md](PROMPT.md).

## Core results
| # | File | Result |
|---|------|--------|
| 01 | [01-channel-is-linear-and-extends-uniquely.md](01-channel-is-linear-and-extends-uniquely.md) | $\mathcal E$ linear on states, unique linear extension to $\mathcal B(\mathbb C^d)$ |
| 02 | [02-channels-are-cptp.md](02-channels-are-cptp.md) | Channels are trace-preserving & completely positive |
| 03 | [03-kraus-implies-cp.md](03-kraus-implies-cp.md) | Kraus form ⇒ completely positive |
| 04 | [04-d-positive-implies-choi-psd.md](04-d-positive-implies-choi-psd.md) | $d$-positive ⇒ Choi matrix $\ge0$ |
| 05 | [05-choi-psd-implies-kraus.md](05-choi-psd-implies-kraus.md) | Choi $\ge0$ ⇒ Kraus representation |
| 06 | [06-chois-theorem.md](06-chois-theorem.md) | Choi's theorem (all equivalences) + unitary ⇔ rank $J=1$ |
| 07 | [07-kraus-theorem-trace-preserving.md](07-kraus-theorem-trace-preserving.md) | TP ⇔ complete Kraus ⇔ $\mathrm{Tr}_{d'}J=I_d/d$ |
| 08 | [08-bistochastic-iff-unital.md](08-bistochastic-iff-unital.md) | Bistochastic ⇔ unital channel (via the adjoint) |
| 09 | [09-stinespring-dilation.md](09-stinespring-dilation.md) | Every channel = ancilla + unitary + partial trace |
| 10 | [10-povm-basics.md](10-povm-basics.md) | POVM $=\{F_i\ge0,\sum F_i=I\}$; outcome prob $\mathrm{Tr}(\rho F_i)$ |
| 11 | [11-naimark-dilation.md](11-naimark-dilation.md) | Every POVM = gate + projective measurement |
| 12 | [12-pncp-separability-criterion.md](12-pncp-separability-criterion.md) | Positive maps detect entanglement; witnesses |
| 13 | [13-ppt-criterion.md](13-ppt-criterion.md) | PPT / Peres–Horodecki criterion |

## Derived / "trap"
| # | File | Result |
|---|------|--------|
| 14 | [14-depolarizing-kraus-and-choi.md](14-depolarizing-kraus-and-choi.md) | Worked example: Choi matrix & Kraus ops of $\Delta_\epsilon$ |
| 15 | [15-basic-channels-kraus-operators.md](15-basic-channels-kraus-operators.md) | Ancilla / partial trace / measurement as channels |

## Study order
01 → 02 (what a channel *is*), then the structure theorems 03 → 04 → 05 → **06 (Choi)** → 07 (Kraus). Then 09 (Stinespring), 08 (bistochastic). Then the measurement side 10 → 11 (POVM/Naimark), and the entanglement side 12 → 13 (PnCP/PPT). Use 14–15 as concrete anchors.

> Notation: $\mathcal E:\mathcal B(\mathbb C^d)\to\mathcal B(\mathbb C^{d'})$ a linear map; $|\beta_{00}\rangle=\frac1{\sqrt d}\sum_i|i\rangle|i\rangle$; Choi matrix $J_{\mathcal E}=I_d\otimes\mathcal E(|\beta_{00}\rangle\langle\beta_{00}|)$; Kraus $\mathcal E(\rho)=\sum_k K_k\rho K_k^\dagger$; adjoint $\mathcal E^\dagger$ defined by $\mathrm{Tr}(\mathcal E^\dagger(A)^\dagger B)=\mathrm{Tr}(A^\dagger\mathcal E(B))$.
