# Lesson 7 (updated) — Leftover Hashing Lemma: Proof Pack

The reworked Lesson 7 (by Alexandra Mușat): the **entropy zoo → universal hashing → leftover hashing → privacy amplification** front end. Same 5-part format as the [C4 pack](../C4/README.md). Generating prompt: [PROMPT.md](PROMPT.md).

> The second half of this lecture (state discrimination, Pinsker, fidelity, Uhlmann, entanglement fidelity, Fano, Schumacher) is identical to standard Lecture 7 — see the [C7 pack](../C7/README.md). Not duplicated here.

## Core results
| # | File | Result |
|---|------|--------|
| 01 | [01-renyi-and-collision-entropy.md](01-renyi-and-collision-entropy.md) | Rényi entropy; $H_2=-\log\Pr[X=X']$ |
| 02 | [02-min-entropy.md](02-min-entropy.md) | $H_\infty=-\log\max_i p_i=-\log p_{\text{guess}}$ |
| 03 | [03-conditional-min-entropy.md](03-conditional-min-entropy.md) | Conditional min-entropy (classical + quantum) |
| 04 | [04-trace-and-purified-distance.md](04-trace-and-purified-distance.md) | Trace distance metric; purified distance $P=\sqrt{1-F^2}$ |
| 05 | [05-smooth-min-entropy.md](05-smooth-min-entropy.md) | Smooth min-entropy ($\epsilon$-ball) |
| 06 | [06-two-universal-hashing.md](06-two-universal-hashing.md) | Two-universal families; the $\mathbb Z_5$ example |
| 07 | [07-classical-leftover-hashing.md](07-classical-leftover-hashing.md) | Extractors & classical Leftover Hashing Lemma |
| 08 | [08-quantum-leftover-hashing.md](08-quantum-leftover-hashing.md) | Quantum Leftover Hashing Lemma |
| 09 | [09-privacy-amplification.md](09-privacy-amplification.md) | Privacy amplification in QKD |

## Study order
01 → 02 → 03 (entropy zoo, ending at conditional min-entropy — the key quantity). Then 04 → 05 (the smoothing metric). Then 06 → 07 → 08 (hashing → leftover hashing), capped by 09 (privacy amplification). The headline: **08 (Quantum LHL)** and its use in **09**.

> Notation: $H_\alpha$ Rényi entropy, $H_\infty/H_{\min}$ min-entropy, $H_{\min}^\epsilon$ smooth min-entropy; $D(\rho,\sigma)=\tfrac12\text{Tr}|\rho-\sigma|$ trace distance; $P$ purified distance; $\Delta$ = trace-distance-to-uniform-given-$E$. Logs base 2.
