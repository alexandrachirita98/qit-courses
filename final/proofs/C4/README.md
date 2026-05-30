# C4 — Quantum Random Variables: Proof Pack (oral exam prep)

Each proof is in its own file, explained **plainly first, then rigorously**, in this format:

1. **In plain words** — what we prove and why it's true intuitively (often with a qubit example).
2. **Toolbox** — the definitions / prior results we're allowed to use.
3. **The proof** — every algebra step numbered, with a plain-English note on *why* it's legal.
4. **Where the magic happens** — the one trick to memorize so you can rebuild it under pressure.
5. **If he pushes back** — likely follow-up questions + short answers.

## Core results (from the lecture)

| # | File | Result |
|---|------|--------|
| 01 | [01-sampling-with-an-observable.md](01-sampling-with-an-observable.md) | Measuring `W` on `\|ψ⟩=Σαᵢ\|ϕᵢ⟩` gives `λ_k` w.p. `\|α_k\|²`; infinitely many `\|ψ⟩` match a distribution |
| 02 | [02-indiscernible-pure-states.md](02-indiscernible-pure-states.md) | `\|ψ⟩≡\|ξ⟩ ⇔ \|ψ⟩=e^{iθ}\|ξ⟩ ⇔ \|ψ⟩⟨ψ\|=\|ξ⟩⟨ξ\|` |
| 03 | [03-indistinguishable-iff-same-density-matrix.md](03-indistinguishable-iff-same-density-matrix.md) | Random states are indistinguishable ⇔ same density matrix |
| 04 | [04-density-matrix-properties.md](04-density-matrix-properties.md) | `ρ` is Hermitian, PSD, unit-trace |
| 05 | [05-every-density-matrix-is-realized.md](05-every-density-matrix-is-realized.md) | Every density matrix comes from a random state (spectral); non-unique |
| 06 | [06-depolarizing-from-imperfect-prep.md](06-depolarizing-from-imperfect-prep.md) | Imperfect `\|+⟩` preparation averages to the depolarizing channel |
| 07 | [07-measurement-uncertainty-grows-with-epsilon.md](07-measurement-uncertainty-grows-with-epsilon.md) | Outcome distribution & entropy of `ρ=(1-ε)\|ψ⟩⟨ψ\|+εI/d`; H grows with ε |
| 08 | [08-mean-and-variance-depend-on-eigenvalues.md](08-mean-and-variance-depend-on-eigenvalues.md) | `⟨O⟩`, `ΔO²` formulas; why they're label-dependent (d=3 example) |
| 09 | [09-distinct-eigenvalues-entropy-independent.md](09-distinct-eigenvalues-entropy-independent.md) | Distinct eigenvalues ⇒ `H(O)` independent of the eigenvalues |
| 10 | [10-fourier-is-the-worst-basis.md](10-fourier-is-the-worst-basis.md) | Fourier basis gives `H(O)=log d` (maximal) |
| 11 | [11-von-neumann-entropy-is-the-minimum.md](11-von-neumann-entropy-is-the-minimum.md) | `H(O) ≥ H(ρ)`, eigenbasis is best (majorization) |
| 12 | [12-maassen-uffink.md](12-maassen-uffink.md) | `H(O)+H(O') ≥ -log max\|⟨ϕ_k\|ξ_j⟩\|²` (the big one) |

## Derived / "trap" results (could be asked at the oral)

| # | File | Result |
|---|------|--------|
| 13 | [13-global-vs-relative-phase.md](13-global-vs-relative-phase.md) | Global phase is invisible; relative phase is measurable |
| 14 | [14-why-the-average-is-meaningless.md](14-why-the-average-is-meaningless.md) | Why the mean of non-numeric outcomes carries no physics |
| 15 | [15-doubly-stochastic-never-decreases-entropy.md](15-doubly-stochastic-never-decreases-entropy.md) | `D` doubly stochastic, `v=Dp` ⇒ `H(v) ≥ H(p)` |
| 16 | [16-maassen-uffink-zero-and-maximal.md](16-maassen-uffink-zero-and-maximal.md) | When the MU bound is 0 (shared eigenvector) vs maximal (complementary) |
| 17 | [17-entropy-zero-and-maximal.md](17-entropy-zero-and-maximal.md) | `H(ρ)=0 ⇔ pure`; `H(ρ)=log d ⇔ ρ=I/d` |
| 18 | [18-depolarizing-increases-entropy.md](18-depolarizing-increases-entropy.md) | `Δ_ε` never decreases von Neumann entropy |
| 19 | [19-two-trace-identities.md](19-two-trace-identities.md) | `Tr(ρ\|ϕ⟩⟨ϕ\|)=⟨ϕ\|ρ\|ϕ⟩` and `Σ_k⟨ϕ_k\|ρ\|ϕ_k⟩=1` |

## Suggested study order
Start with the **tiny tools** 19 → 04 → 05 (they're used everywhere), then 01–03, then the entropy chain 17 → 15 → 09 → 10 → 11, then **12 (Maassen–Uffink)** and its corollary 16. Leave 06/07/08/18 for the depolarizing-channel cluster, and 13/14 are quick conceptual ones.

> Notation: `|ψ⟩` a pure state (column vector), `ρ` a density matrix, `H(ρ)=-Tr ρ log ρ` the von Neumann entropy, `H(O)` the Shannon entropy of the outcomes of measuring observable `O`. Logs are base 2 (entropy in bits) unless noted.
