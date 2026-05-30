# 08 — Bistochastic ⇔ unital channel (via the adjoint)

**Claim.** For $\mathcal E(\rho)=\sum_k K_k\rho K_k^\dagger$, the adjoint channel is $\mathcal E^\dagger(\rho)=\sum_k K_k^\dagger\rho K_k$. Then:
- $\mathcal E$ is CP $\iff\mathcal E^\dagger$ is CP;
- $\mathcal E$ is trace-preserving $\iff\mathcal E^\dagger$ is **unital** ($\mathcal E^\dagger(I)=I$);
- $\mathcal E$ is **bistochastic** (both $\mathcal E$ and $\mathcal E^\dagger$ are channels) $\iff\mathcal E$ is a **unital channel**.

---

### 1. In plain words
Classically, a stochastic matrix has columns summing to 1; a *doubly*-stochastic (bistochastic) one also has rows summing to 1. The quantum analogue: a channel is trace-preserving (the "columns" condition); it's *also* a channel in reverse (its adjoint is a channel) exactly when it's **unital** — it fixes the identity $I$ (the "rows" condition). Unital channels are the ones that can't decrease entropy (the C6 story).

### 2. Toolbox
- Adjoint defined by $\text{Tr}(\mathcal E^\dagger(A)^\dagger B)=\text{Tr}(A^\dagger\mathcal E(B))$.
- TP ⇔ $\sum_k K_k^\dagger K_k=I$ ([07](07-kraus-theorem-trace-preserving.md)).
- Unital means $\mathcal E(I)=I$.

### 3. The proof

**The adjoint is the dagger-flipped Kraus map.**
1. $\text{Tr}\big(A^\dagger\mathcal E(B)\big)=\text{Tr}\big(A^\dagger\sum_k K_kBK_k^\dagger\big)=\text{Tr}\big(\sum_k K_k^\dagger A^\dagger K_k\,B\big)=\text{Tr}\big((\sum_k K_k^\dagger A K_k)^\dagger B\big)$ — cyclicity moves $K_k^\dagger,K_k$ around $A^\dagger$. Matching the definition, $\mathcal E^\dagger(A)=\sum_k K_k^\dagger A K_k$.

**CP is symmetric.**
2. $\mathcal E^\dagger$ has Kraus operators $\{K_k^\dagger\}$ — also a Kraus form — so it's CP by [03](03-kraus-implies-cp.md). Thus $\mathcal E$ CP $\iff\mathcal E^\dagger$ CP.

**TP of $\mathcal E$ ⇔ unitality of $\mathcal E^\dagger$.**
3. $\mathcal E^\dagger(I)=\sum_k K_k^\dagger I K_k=\sum_k K_k^\dagger K_k$. By [07](07-kraus-theorem-trace-preserving.md), $\mathcal E$ is TP $\iff\sum_k K_k^\dagger K_k=I\iff\mathcal E^\dagger(I)=I\iff\mathcal E^\dagger$ unital.

**Bistochastic ⇔ unital channel.**
4. "$\mathcal E$ bistochastic" means *both* $\mathcal E$ and $\mathcal E^\dagger$ are channels (CP + TP).
 - $\mathcal E$ is a channel: CP + TP.
 - $\mathcal E^\dagger$ is a channel: CP (automatic, step 2) + TP. By step 3 applied to $\mathcal E^\dagger$ (whose adjoint is $\mathcal E$), "$\mathcal E^\dagger$ TP" $\iff$ "$\mathcal E$ unital."
5. Combining: $\mathcal E$ bistochastic $\iff$ ($\mathcal E$ CP + TP) and ($\mathcal E$ unital) $\iff\mathcal E$ is a **unital channel**. ∎

### 4. Where the magic happens
**Daggering the Kraus operators swaps the two normalization conditions:** $\sum_k K_k^\dagger K_k=I$ (trace-preserving) for $\mathcal E$ becomes $\sum_k K_k K_k^\dagger=I$ (unital) for $\mathcal E$. Requiring *both* = bistochastic = doubly-stochastic in the quantum sense.

### 5. If he pushes back
- *"Give the classical mirror."* Stochastic $D$ ($\mathbb 1^TD=\mathbb 1^T$, columns sum to 1) ↔ TP; $D\mathbb 1=\mathbb 1$ (rows sum to 1) ↔ unital; both ↔ doubly stochastic. (See [C4/15](../C4/15-doubly-stochastic-never-decreases-entropy.md).)
- *"Why care about unital?"* Unital channels never decrease von Neumann entropy — the depolarizing channel ([14](14-depolarizing-kraus-and-choi.md), [C4/18](../C4/18-depolarizing-increases-entropy.md)) is the canonical example.
- *"Is the adjoint always TP?"* No — only when $\mathcal E$ is unital. TP and unital are independent conditions; bistochastic demands both.
