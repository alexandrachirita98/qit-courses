# QIT Oral Exam — Cheat Sheet (formulas & notions)

Fast reference distilled from the proof packs in this folder ([C4](C4/README.md) · [CHSH](CHSH/README.md) · [C5](C5/README.md) · [C6](C6/README.md) · [C7](C7/README.md) · [lesson7-update](lesson7-update/README.md)). No proofs — just the statement, the formula, and the one idea to remember. Logs are **base 2**. Drill-down links go to the full proof.

---

## 0. Core toolbox (used everywhere)

| Fact | Formula |
|---|---|
| Born rule (mixed) | $\Pr[\lambda]=\text{Tr}(\rho E_\lambda)$, $E_\lambda$ = eigen-projector |
| Trace ↔ sandwich | $\text{Tr}(\rho\,\|\phi\rangle\langle\phi\|)=\langle\phi\|\rho\|\phi\rangle$ · [C4/19](C4/19-two-trace-identities.md) |
| Probabilities sum | $\sum_k\langle\phi_k\|\rho\|\phi_k\rangle=\text{Tr}\,\rho=1$ |
| Expectation | $\langle O\rangle_\rho=\text{Tr}(\rho O)$ (linear in $O$) · [CHSH/01](CHSH/01-expected-value-Tr-rho-O.md) |
| von Neumann entropy | $H(\rho)=-\text{Tr}\,\rho\log\rho=-\sum_i\lambda_i\log\lambda_i$ |
| Shannon entropy | $H(p)=-\sum_i p_i\log p_i$ |
| Binary entropy | $h(x)=-x\log x-(1-x)\log(1-x)$ |
| Density matrix | $\rho=\rho^\dagger$, $\rho\ge0$, $\text{Tr}\,\rho=1$ · [C4/04](C4/04-density-matrix-properties.md) |
| Purity | $\text{Tr}(\rho^2)=\sum_i\lambda_i^2\in[\tfrac1d,1]$; $=1\Leftrightarrow$ pure |
| Spectral / Schmidt / SVD | diagonalize Hermitians; reshape bipartite vectors via SVD |

**Two-qubit reshape:** $|\psi\rangle=\sum_{ij}M_{ij}|i\rangle_A|j\rangle_B$, $M=$ `psi.reshape(2,2)`, $\rho_A=MM^\dagger$.

---

## 1. Headline theorems (most likely at the board)

Each: the formula, **what it means in plain words**, and *the trick* to reconstruct the proof.

### Maassen–Uffink — [C4/12](C4/12-maassen-uffink.md)
$$H(O)+H(O')\ge-\log\max_{k,j}|\langle\phi_k|\xi_j\rangle|^2$$
**Plain words:** You can't be sharp about two *incompatible* measurements at once. If measuring $O$ is predictable (low entropy), then $O'$ *must* be fuzzy. The sum of the two uncertainties has a floor set by how "different" the two bases are (their biggest overlap). Share an eigenvector → floor $0$ (compatible); maximally unbiased → floor $\log d$ (most incompatible).
*Trick:* write Rényi entropies as $\log$ of $p$-norms; **Riesz–Thorin** interpolates between "unitary keeps the 2-norm" and "max overlap bounds the $1\!\to\!\infty$ norm"; let $\alpha,\beta\to1$ to recover Shannon.

### von Neumann entropy = minimum measurement entropy — [C4/11](C4/11-von-neumann-entropy-is-the-minimum.md)
$$H(O)\ge H(\rho),\quad\text{equality in }\rho\text{'s eigenbasis}$$
**Plain words:** However you measure $\rho$, the randomness of the outcomes is never below the state's own entropy $H(\rho)$. The *least* random measurement is in $\rho$'s eigenbasis (outcomes = its eigenvalues); any other basis just "smears" those eigenvalues and adds uncertainty.
*Trick:* the matrix of squared overlaps $D_{ki}=|\langle\phi_k|\psi_i\rangle|^2$ is **doubly stochastic**, and doubly-stochastic mixing only raises entropy (majorization).

### KTL identity → Tsirelson — [CHSH/05](CHSH/05-khalfin-tsirelson-landau-identity.md), [CHSH/06](CHSH/06-tsirelson-bound.md)
$$S^2=4I-[A_0,A_1]\otimes[B_0,B_1]\ \Rightarrow\ |\langle S\rangle|\le 2\sqrt2$$
**Plain words:** Quantum mechanics *can* beat the classical CHSH limit of 2 — but only up to $2\sqrt2$. Squaring the CHSH operator gives $4I$ minus a term measuring how much Alice's two observables fail to commute, times Bob's. Each commutator has size $\le2$, so $S^2\preceq 8I$ and $|\langle S\rangle|\le\sqrt8$.
*Trick:* $A^2=B^2=I$ collapses the diagonal to $4I$; the cross-terms bundle into the commutator product.

### Choi's theorem — [C5/06](C5/06-chois-theorem.md)
$$\text{CP}\iff J_{\mathcal E}=I\otimes\mathcal E(|\beta_{00}\rangle\langle\beta_{00}|)\ge0$$
**Plain words:** To check if a map is a legal quantum operation, you don't test infinitely many inputs — you feed it **one** entangled state (the Bell state), get its "Choi matrix", and check it's positive. Bonus: the *minimum number of Kraus operators* you need equals the **rank** of that matrix (= the answer to exam Q7).
*Trick:* the maximally-entangled test state encodes the whole map at once; recover $\mathcal E(|i\rangle\langle j|)=d(\langle i|\otimes I)J(|j\rangle\otimes I)$.

### Kraus / Stinespring — [C5/07](C5/07-kraus-theorem-trace-preserving.md), [C5/09](C5/09-stinespring-dilation.md)
$$\mathcal E(\rho)=\sum_k K_k\rho K_k^\dagger,\ \ \textstyle\sum_k K_k^\dagger K_k=I\ \ \Longleftrightarrow\ \ \mathcal E(\rho)=\text{Tr}_E\big(U(|0\rangle\langle0|\otimes\rho)U^\dagger\big)$$
**Plain words:** Every noisy channel is secretly a *reversible* (unitary) operation on a bigger system: add a clean ancilla, apply one big gate to everything, then throw the ancilla away. The "noise" is just information that leaked into the discarded part. Trace-preservation = the Kraus operators sum to the identity.
*Trick:* stack the Kraus operators into one tall isometry $V=\sum_k|k\rangle\otimes K_k$; the condition $\sum_k K_k^\dagger K_k=I$ is exactly $V^\dagger V=I$.

### Data Processing Inequality — [C6/02](C6/02-data-processing-inequality.md)
$$D(\mathcal E\rho\,\|\,\mathcal E\sigma)\le D(\rho\,\|\,\sigma)$$
**Plain words:** Passing two states through the *same* noisy box can never make them easier to tell apart — processing only loses information, never creates it. This one inequality is the engine behind almost every "monotonicity" result in C6.
*Trick:* adding an ancilla and applying a unitary leave $D$ unchanged; partial trace = "depolarize the environment", which is a mixture of unitaries, so joint convexity makes $D$ shrink.

### Holevo bound — [C6/08](C6/08-holevo-theorem.md)
$$I(A{:}\tilde A)\le\chi=H\Big(\textstyle\sum_i p_i\rho_i\Big)-\sum_i p_iH(\rho_i)$$
**Plain words:** With $n$ qubits you can transmit at most $n$ classical bits. No matter how cleverly Bob measures the state Alice sent, the classical information he extracts about her message is capped by the Holevo quantity $\chi$.
*Trick:* it's just the **DPI** applied to mutual information — Bob's measurement is a channel, and mutual information only decreases under a channel.

### Conditional von Neumann entropy — [C6/09](C6/09-conditional-von-neumann-entropy.md)
$$H(A|B)=H(AB)-H(B)=\log d_A-D\big(\rho_{AB}\,\|\,\tfrac{I_A}{d_A}\otimes\rho_B\big)$$
**Plain words:** The leftover uncertainty about $A$ once you hold $B$. Classically it's always $\ge0$, but quantumly it can be **negative** — and that negativity is itself a signature of entanglement. A Bell state gives the most negative value, $-\log d$.
*Trick:* rewriting it as $\log d_A-D(\cdots)$ turns it into a divergence, so the DPI hands you all its monotonicity properties for free.

### Schmidt decomposition / entanglement entropy — [C6/10](C6/10-schmidt-decomposition.md)
$$|\psi\rangle=\sum_k s_k\,|\phi_k\rangle|\xi_k\rangle,\qquad \rho_A,\rho_B\text{ both have eigenvalues }s_k^2$$
**Plain words:** Any pure state of two systems can be lined up so Alice's $k$-th vector pairs with Bob's $k$-th, weighted by $s_k$. Both halves then carry the **same** entropy — the "amount of entanglement". (This is exam Q1.)
*Trick:* it's literally the **SVD** of the coefficient matrix $M$ ($M_{ij}=\langle ij|\psi\rangle$); the squared singular values are the shared reduced-state eigenvalues.

### Uhlmann's theorem (fidelity) — [C7/04](C7/04-uhlmann-theorem.md)
$$F(\rho,\sigma)=\big(\text{Tr}|\sqrt\rho\sqrt\sigma|\big)^2=\max|\langle\phi_\rho|\psi_\sigma\rangle|^2$$
**Plain words:** Fidelity = how similar two states are (1 = identical, 0 = orthogonal). It's the best overlap between their purifications, and Uhlmann gives a closed formula. **Note the square** — the course convention is *squared* (this is exam Q8; the unsquared $\text{Tr}|\sqrt\rho\sqrt\sigma|$ is the trap option).
*Trick:* the purification freedom is a free unitary $U$ inside $\text{Tr}(\sqrt\rho\sqrt\sigma\,U)$, and $\max_U|\text{Tr}(AU)|=\text{Tr}|A|$.

### Schumacher source coding — [C7/07](C7/07-schumacher-source-coding.md)
$$\min\text{ rate}=H(\rho)\ \text{qubits per symbol}$$
**Plain words:** To compress a stream of identical quantum states, you need exactly $H(\rho)$ qubits each — no fewer, no more. Almost all the weight of $\rho^{\otimes n}$ sits in a "typical subspace" of dimension $\approx 2^{nH(\rho)}$, and you just project onto it. (This is exam Q3.)
*Trick:* the typical subspace; going below $H(\rho)$ would let you beat the Holevo bound.

### Quantum Leftover Hashing — [L7/08](lesson7-update/08-quantum-leftover-hashing.md)
$$\Delta=\tfrac12\sqrt{2^{\,l-H_{\min}(X|E)}}$$
**Plain words:** If an eavesdropper $E$ knows *something* about your raw key, hashing it down to fewer bits than $E$'s uncertainty $H_{\min}(X|E)$ produces a key that's almost perfectly uniform and secret. This is **privacy amplification** — the last step of QKD.
*Trick:* a 2-universal hash makes output collisions rare; low collision probability bounds the $\ell_2$ (then $\ell_1$) distance to a uniform key.

---

## 2. C4 — Quantum Random Variables

| Result | Formula / statement | Idea |
|---|---|---|
| Sampling [01](C4/01-sampling-with-an-observable.md) | measure $W$ on $\sum_i\alpha_i\|\phi_i\rangle$ ⇒ $\Pr[\lambda_k]=\|\alpha_k\|^2$ | phases free ⇒ ∞ many $\|\psi\rangle$ |
| Indiscernible [02](C4/02-indiscernible-pure-states.md) | $\|\psi\rangle\equiv\|\xi\rangle\Leftrightarrow\|\psi\rangle=e^{i\theta}\|\xi\rangle\Leftrightarrow$ same projector | global phase invisible |
| Same stats ⇔ same $\rho$ [03](C4/03-indistinguishable-iff-same-density-matrix.md) | all stats via $\text{Tr}(\rho E_\lambda)$ | mixtures collapse to one matrix |
| Realization [05](C4/05-every-density-matrix-is-realized.md) | $\rho=\sum_i\lambda_i\|\psi_i\rangle\langle\psi_i\|$, $\lambda$=prob. vector | non-unique ensembles |
| Depolarizing [06](C4/06-depolarizing-from-imperfect-prep.md) | $\Delta_\epsilon(\rho)=(1-\epsilon)\rho+\epsilon\frac Id\text{Tr}\rho$ | random phase kills off-diagonals |
| Meas. entropy [07](C4/07-measurement-uncertainty-grows-with-epsilon.md) | $\rho=(1-\epsilon)\|\psi\rangle\langle\psi\|+\epsilon\frac Id$: $H=h(q)+q\log(d{-}1)$, $q=\tfrac{d-1}{d}\epsilon$ | grows with $\epsilon$ |
| Mean/variance [08](C4/08-mean-and-variance-depend-on-eigenvalues.md) | $\langle O\rangle=\sum_k\lambda_k\langle\phi_k\|\rho\|\phi_k\rangle$, $\Delta O^2=\langle O^2\rangle-\langle O\rangle^2$ | **depend on eigenvalue labels** |
| Distinct eigvals [09](C4/09-distinct-eigenvalues-entropy-independent.md) | $H(O)=-\sum_k v_k\log v_k$, $v_k=\langle\phi_k\|\rho\|\phi_k\rangle$ | label-independent, basis-dependent |
| Worst basis [10](C4/10-fourier-is-the-worst-basis.md) | Fourier ⇒ all $\|\langle\phi_k\|\psi_i\rangle\|^2=\tfrac1d$ ⇒ $H(O)=\log d$ | MUB with eigenbasis |
| Doubly-stoch. [15](C4/15-doubly-stochastic-never-decreases-entropy.md) | $v=Dp$, $D$ bistochastic ⇒ $H(v)\ge H(p)$ | rows for Jensen, cols for resum |
| MU bound range [16](C4/16-maassen-uffink-zero-and-maximal.md) | $0\le B\le\log d$; $0$ ⇔ shared eigvec, $\log d$ ⇔ complementary (overlap $\tfrac1d$) | — |
| Entropy extremes [17](C4/17-entropy-zero-and-maximal.md) | $H(\rho)=0\Leftrightarrow$ pure; $=\log d\Leftrightarrow\rho=I/d$ | $\log d-H=D_{\mathrm{KL}}(\lambda\|u)$ |
| Depolarizing ↑ entropy [18](C4/18-depolarizing-increases-entropy.md) | $H(\Delta_\epsilon\rho)\ge H(\rho)$ | mixing with $I/d$ = bistochastic |

---

## 3. CHSH / Tsirelson

$S=A_0{\otimes}B_0+A_0{\otimes}B_1+A_1{\otimes}B_0-A_1{\otimes}B_1$, observables $\pm1$-valued.

| Result | Formula | Idea |
|---|---|---|
| $\pm1$ obs. [02](CHSH/02-pm1-observables-square-to-identity.md) | $A^2=I$, $\|A\|=1$, Hermitian & unitary | $(\pm1)^2=1$ |
| Commutator bound [09](CHSH/09-commutator-norm-bound.md) | $\|[A_0,A_1]\|\le2$, $=2$ ⇔ anticommute | triangle ineq. |
| KTL [05](CHSH/05-khalfin-tsirelson-landau-identity.md) | $S^2=4I-[A_0,A_1]\otimes[B_0,B_1]$ | — |
| Tsirelson [06](CHSH/06-tsirelson-bound.md) | $\|\langle S\rangle\|\le2\sqrt2$ | $S^2\preceq8I$, $\langle S\rangle\le\|S\|$ |
| Sharpness [07](CHSH/07-tsirelson-sharpness.md) | anticommuting $\{Z,X\}$ on Bell state ⇒ $2\sqrt2$ | $ZX-XZ=2iY$ |
| Classical [08](CHSH/08-classical-chsh-bound.md) | local hidden var ⇒ $\|S\|\le2$ | $A_0(b_0{+}b_1)+A_1(b_0{-}b_1)\in\{\pm2\}$ |
| Separable [10](CHSH/10-separable-states-obey-classical-bound.md) | product state ⇒ $\|\langle S\rangle\|\le2$ | factorizes = local model |

---

## 4. C5 — Quantum Channels

Notation: $J_{\mathcal E}=I_d\otimes\mathcal E(\|\beta_{00}\rangle\langle\beta_{00}\|)$, $\mathcal E(\rho)=\sum_k K_k\rho K_k^\dagger$.

| Result | Formula / statement | Idea |
|---|---|---|
| Channel = CPTP [02](C5/02-channels-are-cptp.md) | completely positive + trace preserving | act on half of entangled ⇒ need *complete* positivity |
| Kraus ⇒ CP [03](C5/03-kraus-implies-cp.md) | $I_n\otimes\mathcal E=\sum_k(I\otimes K_k)(\cdot)(I\otimes K_k)^\dagger$ | congruence preserves PSD |
| Choi [06](C5/06-chois-theorem.md) | CP ⇔ $J_{\mathcal E}\ge0$; min #Kraus $=\text{rank}\,J_{\mathcal E}$; unitary ⇔ rank 1 | recover $\mathcal E(\|i\rangle\langle j\|)=d(\langle i\|{\otimes}I)J(\|j\rangle{\otimes}I)$ |
| Kraus (TP) [07](C5/07-kraus-theorem-trace-preserving.md) | TP ⇔ $\sum_k K_k^\dagger K_k=I$ ⇔ $\text{Tr}_{d'}J=\tfrac{I_d}d$ | — |
| Bistochastic [08](C5/08-bistochastic-iff-unital.md) | both $\mathcal E,\mathcal E^\dagger$ channels ⇔ $\mathcal E$ unital ($\mathcal E(I)=I$); $\mathcal E^\dagger(\rho)=\sum K_k^\dagger\rho K_k$ | dagger swaps TP↔unital |
| Stinespring [09](C5/09-stinespring-dilation.md) | $\mathcal E(\rho)=\text{Tr}_E(U(\|0\rangle\langle0\|\otimes\rho)U^\dagger)$ | isometry $V=\sum_k\|k\rangle\otimes K_k$ |
| POVM [10](C5/10-povm-basics.md) | $\{F_i\ge0\}$, $\sum_i F_i=I$; $\Pr[i]=\text{Tr}(\rho F_i)$ | — |
| Naimark [11](C5/11-naimark-dilation.md) | every POVM = gate + projective meas. | $K_i=\sqrt{F_i}$ then Stinespring |
| PnCP [12](C5/12-pncp-separability-criterion.md) | $\rho$ entangled ⇔ ∃ **positive** (not CP) $\mathcal E$ with $(I\otimes\mathcal E)\rho\not\ge0$ | separable survive positive maps |
| PPT [13](C5/13-ppt-criterion.md) | separable ⇒ $(I\otimes T)\rho\ge0$; neg. partial transpose ⇒ entangled (iff $nd\le6$) | transpose positive, not CP |
| Depolarizing [14](C5/14-depolarizing-kraus-and-choi.md) | $\Delta_1$: $J=\tfrac{I_{d^2}}{d^2}$, rank $d^2$, $K_{k_1k_2}=\tfrac1{\sqrt d}\|k_2\rangle\langle k_1\|$ | maximal noise = full rank |

---

## 5. C6 — Quantum Data Processing

| Result | Formula / statement | Idea |
|---|---|---|
| Umegaki [01](C6/01-umegaki-divergence-nonnegative.md) | $D(\rho\|\sigma)=-\text{Tr}(\rho(\log\sigma-\log\rho))\ge0$, $=0$⇔$\rho=\sigma$; $\infty$ on support clash | Jensen ⇒ classical KL |
| DPI [02](C6/02-data-processing-inequality.md) | $D(\mathcal E\rho\|\mathcal E\sigma)\le D(\rho\|\sigma)$ | joint convexity |
| Entropy & unital [03](C6/03-bistochastic-cant-decrease-entropy.md) | unital ⇒ $H(\mathcal E\rho)\ge H(\rho)$ | $D(\rho\|I/d)=\log d-H(\rho)$ |
| No-communication [05](C6/05-no-communication-theorem.md) | $\text{Tr}_B((I_A\otimes\mathcal E)\rho)=\text{Tr}_B\rho$ | $\sum K_k^\dagger K_k=I$ |
| Mutual info [06](C6/06-quantum-mutual-information.md) | $I(A{:}B)=D(\rho_{AB}\|\rho_A\otimes\rho_B)=H(A)+H(B)-H(AB)\ge0$ | $\log$ of tensor = sum |
| Holevo $\chi$ [07](C6/07-quantum-classical-mutual-info.md) | $\chi=H(\sum p_i\rho_i)-\sum p_iH(\rho_i)$ | classical reg. cancels |
| Conditional [09](C6/09-conditional-von-neumann-entropy.md) | $H(A\|B)=H(AB)-H(B)$; $H(A\|\mathcal E B)\ge H(A\|B)$; separable ⇒ $\ge0$ | negative ⇒ entangled |
| Berta (memory) [11](C6/11-uncertainty-with-quantum-memory.md) | $H(O\|B)+H(O'\|B)\ge-\log c^2+H(A\|B)$ | quantum memory lowers floor |
| Tripartite [12](C6/12-tripartite-uncertainty.md) | pure $\rho_{ABC}$: $H(O\|B)+H(O'\|C)\ge-\log c^2$ | purity links marginals |
| BB84 [13](C6/13-bb84-security.md) | $H(X\|B)+H(Z\|E)\ge1$; low error ⇒ Eve ignorant | prepare-measure = entangled picture |

---

## 6. C7 — Quantum Compression

$\|A\|_{\text{Tr}}=\text{Tr}\sqrt{A^\dagger A}$; fidelity **squared** convention.

| Result | Formula | Idea |
|---|---|---|
| Helstrom [01](C7/01-helstrom-bound.md) | $P_{\text{succ}}=\tfrac12+\tfrac12\|p\rho-(1-p)\sigma\|_{\text{Tr}}$ | project on positive part of $p\rho-(1-p)\sigma$ |
| Pinsker [02](C7/02-quantum-pinsker.md) | $\|\rho-\sigma\|_{\text{Tr}}\le\sqrt{2\ln2\,D(\rho\|\sigma)}$ | Helstrom channel keeps trace dist., lowers $D$ |
| Discrimination↔fidelity [03](C7/03-fidelity-and-discrimination.md) | $P_{\text{succ}}=\tfrac12(1+\sqrt{1-\|\langle\phi_\rho\|\psi_\sigma\rangle\|^2})$ | fidelity = max purification overlap |
| Uhlmann [04](C7/04-uhlmann-theorem.md) | $F(\rho,\sigma)=(\text{Tr}\|\sqrt\rho\sqrt\sigma\|)^2$ | free-unitary trick |
| Entanglement fidelity [05](C7/05-entanglement-fidelity.md) | $F(\rho,\mathcal E)=\sum_k\|\text{Tr}(K_k\rho)\|^2$; $F(\rho,\|\phi\rangle\langle\phi\|)=\langle\phi\|\rho\|\phi\rangle$ | rep-independent |
| Quantum Fano [06](C7/06-quantum-fano.md) | $H(\rho,\mathcal E)\le h(F)+(1-F)\log(d^2-1)$ | coarse-grain to survive/disturb |
| Schumacher [07](C7/07-schumacher-source-coding.md) | $\min R=H(\rho)$ | typical subspace |

**Entropy exchange** (Q10): $H(\rho,\mathcal E)=H(W)$, $W_{kl}=\text{Tr}(K_k\rho K_l^\dagger)$.

---

## 7. Lesson-7 update — entropy zoo & hashing

| Result | Formula | Idea |
|---|---|---|
| Rényi / collision [01](lesson7-update/01-renyi-and-collision-entropy.md) | $H_\alpha=\tfrac1{1-\alpha}\log\sum p_i^\alpha$; $H_2=-\log\sum p_i^2=-\log\Pr[X{=}X']$ | collision prob |
| Min-entropy [02](lesson7-update/02-min-entropy.md) | $H_\infty=-\log\max_i p_i=-\log p_{\text{guess}}$ | worst-case / security |
| Cond. min-entropy [03](lesson7-update/03-conditional-min-entropy.md) | $H_{\min}(X\|Y)=-\log\sum_y\max_x P(x,y)$; quantum: $\max_\sigma\sup\{\lambda:\rho_{AB}\le2^{-\lambda}I\otimes\sigma\}$ | guessing prob w/ side info |
| Purified distance [04](lesson7-update/04-trace-and-purified-distance.md) | $D=\tfrac12\text{Tr}\|\rho-\sigma\|$; $P=\sqrt{1-F^2}$ | both metrics |
| Smooth min-entropy [05](lesson7-update/05-smooth-min-entropy.md) | $H_{\min}^\epsilon=\max_{\tilde\rho\in B^\epsilon(\rho)}H_{\min}$ | ignore $\epsilon$-bad parts |
| Two-universal [06](lesson7-update/06-two-universal-hashing.md) | $\Pr_f[f(x)=f(x')]\le\tfrac1{\|Z\|}$ | linear hash over a field |
| Classical LHL [07](lesson7-update/07-classical-leftover-hashing.md) | $\Delta=\tfrac12\sqrt{2^{\,l-H_{\min}(X\|E)}}$ | collision ⇒ uniformity |
| Quantum LHL [08](lesson7-update/08-quantum-leftover-hashing.md) | same with quantum $E$ | privacy amplification basis |

---

## 8. Entanglement-witness checklist (exam Q2)

Given state $\rho$ and Hermitian $O$, decide if $O$ witnesses $\rho$'s entanglement:

1. **Valid state?** $\rho=\rho^\dagger$, $\rho\ge0$, $\text{Tr}\rho=1$.
2. **Valid observable?** $O=O^\dagger$.
3. **$\rho$ entangled?** PPT: partial transpose $(I\otimes T)\rho$ has a **negative** eigenvalue. (necessary & sufficient for $nd\le6$)
4. **Can $O$ witness?** $O\not\ge0$ (has a negative eigenvalue — else trivial).
5. **Is $O$ a *true* witness?** $O$ is **block-positive**: $\langle a,b\|O\|a,b\rangle\ge0$ for all product states (equiv. its Choi map is positive but not CP).
6. **Does it fire?** $\text{Tr}(O\rho)<0$.

**Decision tree (A/B/C/D):**
- not entangled (step 3 fails) → **D** (separable)
- entangled + $O$ valid witness (4&5) + $\text{Tr}(O\rho)<0$ → **A** (witnessed by $O$)
- entangled + $O$ valid witness but $\text{Tr}(O\rho)\ge0$ → **B** (not witnessed by $O$)
- entangled but $O$ not block-positive (5 fails) → **C** (entangled, $O$ not a witness)

---

## 9. Exam Part-II → formula map

$\rho_v=w_0\|\phi\rangle\langle\phi\|+w_1\|\psi\rangle\langle\psi\|$; channel $\mathcal E(\rho)=\tfrac12\rho+\tfrac12\sum_\lambda E_\lambda\rho E_\lambda$; $\rho_w=\mathcal E(\rho_v)$.

| Q | Asks | Compute |
|---|---|---|
| 1 | ent. entropy of $\|\psi\rangle$ | $H(\rho_A)$, $\rho_A=MM^\dagger$, $M=\psi.\text{reshape}(2,2)$ ($\le1$ bit) |
| 2 | is $\|v\rangle$ witnessed by $O$ | witness checklist above |
| 3 | min qubits for $\|v\rangle$ | $H(\rho_v)$ (Schumacher) |
| 4 | entropic uncertainty of $O$ | $-\sum_\lambda p_\lambda\log p_\lambda$, $p_\lambda=\text{Tr}(E_\lambda\rho_v)$ |
| 5 | $P[\text{same}]$, two $O$-meas. | $\sum_\lambda p_\lambda^2$ |
| 6 | max-basis collision | $\text{Tr}(\rho_v^2)$ |
| 7 | min #Kraus of $\mathcal E$ | $\text{rank}\,J_{\mathcal E}$ (1–4) |
| 8 | fidelity $\|w\rangle$ to $\|v\rangle$ | $(\text{Tr}\sqrt{\sqrt{\rho_v}\rho_w\sqrt{\rho_v}})^2$ |
| 9 | entanglement fidelity | $\sum_k\|\text{Tr}(K_k\rho_v)\|^2=\tfrac12+\tfrac12\sum_\lambda p_\lambda^2$ |
| 10 | entropy exchange | $H(W)$, $W_{kl}=\text{Tr}(K_k\rho_v K_l^\dagger)$ |
| Bonus | Eve guesses key | $p\le\tfrac12(1+\sqrt{\ln2\,(h(\delta_{\text{bit}})+h(\delta_{\text{phase}}))})$, then $p^{256}$ |

---

## 10. Memorize these FIRST (highest value)

1. **Core toolbox** §0 — `Tr(ρO)`, `H(ρ)=−Σλlogλ`, density-matrix axioms, purity `Trρ²`.
2. **Choi's theorem** [C5/06](C5/06-chois-theorem.md) — CP ⇔ $J\ge0$, min #Kraus = rank $J$ (covers Q7).
3. **Conditional entropy** [C6/09](C6/09-conditional-von-neumann-entropy.md) — $H(A\|B)=H(AB)-H(B)$, negativity ⇔ entanglement.
4. **Schmidt / entanglement entropy** [C6/10](C6/10-schmidt-decomposition.md) — SVD; $H(\rho_A)=H(\rho_B)$ (covers Q1).
5. **Uhlmann fidelity** [C7/04](C7/04-uhlmann-theorem.md) — $F=(\text{Tr}\|\sqrt\rho\sqrt\sigma\|)^2$ (covers Q8).
6. **Maassen–Uffink + Berta** [C4/12](C4/12-maassen-uffink.md), [C6/11](C6/11-uncertainty-with-quantum-memory.md) — $H(O)+H(O')\ge-\log c^2$ (covers bonus).
7. **DPI** [C6/02](C6/02-data-processing-inequality.md) — everything-monotone engine.
8. **Witness checklist** §8 + **PPT** [C5/13](C5/13-ppt-criterion.md) (covers Q2).
