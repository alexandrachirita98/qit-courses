# 12 — Tripartite uncertainty relation

**Claim.** For a **pure** tripartite state $\rho_{ABC}=|\phi\rangle\langle\phi|$ and two basis observables $O=\{|\phi_k\rangle\}$, $O'=\{|\xi_j\rangle\}$ measured on $A$,
$$H(O|B)_\rho+H(O'|C)_\rho\ \ge\ -\log\max_{k,j}|\langle\phi_k|\xi_j\rangle|^2.$$

---

### 1. In plain words
Split the "helpers" in two: Bob holds $B$, a third party Charlie holds $C$, and together with $A$ everything is one big pure state. The relation says: if Bob can predict Alice's $O$-measurement well (small $H(O|B)$), then Charlie *cannot* also predict her complementary $O'$-measurement well (large $H(O'|C)$) — their combined predictive powers are bounded. Intuitively, measuring $C$ tells you Alice's index, and combined with Alice's result you'd know Bob's post-measurement state, so the uncertainties trade off exactly via the overlap.

### 2. Toolbox
- For pure $\rho_{ABC}$: $H(\rho_{AB})=H(\rho_C)$ and $H(\rho_B)=H(\rho_{AC})$ (a pure state's complementary marginals have equal entropy — from Schmidt, [10](10-schmidt-decomposition.md)).
- $H(A|B)=H(\rho_{AB})-H(\rho_B)$; measuring is a channel $\mathcal E$ giving $H(O|B)=H(A|B)_{(\mathcal E\otimes I_B)\rho}$.
- The pure-state purification lets us relate "measure on $B$" to "measure on $C$."

### 3. The proof (slide's chain)
Let $\mathcal E$ be the channel that measures $O'$ on $A$.
1. **Purity identities.** Since $\rho_{ABC}$ is pure, $H(A|B)_{\rho_{AB}}=H(\rho_{AB})-H(\rho_B)=H(\rho_C)-H(\rho_B)$.
2. **Measure $O'$, track on $C$.** After applying $\mathcal E$ on $A$,
$$H(O'|B)_{\rho_{AB}}=H(A|B)_{(\mathcal E\otimes I_B)\rho_{AB}}=H\big((\mathcal E\otimes I_B)\rho_{AB}\big)-H(\rho_B).$$
3. Using purity again to swap $B\leftrightarrow C$ on the measured state and reorganizing (the slide's algebra),
$$H(O'|B)_{\rho_{AB}}\le H\big((\mathcal E\otimes I_C)\rho_{AC}\big)+H(A|B)=H(O'|C)_{\rho_{AC}}+H(A|B).$$
Intuition for the inequality: knowing Alice's result *and* measuring $C$ would reveal Bob's post-measurement state, so $C$ is at least as informative about $O'$ as $B$ is, up to the $H(A|B)$ deficit.
4. **Combine with Maassen–Uffink** on $A$ alone, $H(O)+H(O')\ge-\log c^2$ (lift the C4 bound through the conditioning): the two helper-conditioned entropies inherit
$$H(O|B)+H(O'|C)\ge-\log c^2=-\log\max_{k,j}|\langle\phi_k|\xi_j\rangle|^2.$$
5. **Mixed states.** Average the (concave) left side over a pure-state decomposition; the bound persists. ∎

### 4. Where the magic happens
**Purity links the three marginals** ($H(\rho_{AB})=H(\rho_C)$ etc.), so "uncertainty Bob has about $O'$" can be rewritten as "uncertainty Charlie has," up to $H(A|B)$. That swap is what splits the single-system Maassen–Uffink bound into a $B$-piece and a $C$-piece. The third system $C$ acts as a stand-in for "the purifying environment."

### 5. If he pushes back
- *"How does this give the bipartite Berta relation?"* Take $C$ to be the purifying system of $\rho_{AB}$; then $H(O'|C)=H(O'|B)-H(A|B)$ recovers [11](11-uncertainty-with-quantum-memory.md).
- *"Why must $\rho_{ABC}$ be pure?"* The marginal-entropy identities ($H(\rho_{AB})=H(\rho_C)$) only hold for pure global states; for mixed $\rho_{ABC}$, purify into a fourth system first.
- *"Operational meaning?"* It forbids two separate parties from each perfectly predicting two complementary observables — the monogamy at the heart of QKD security ([13](13-bb84-security.md)).
