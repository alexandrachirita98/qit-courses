# 04 — An observable as a quantum instrument: Kraus operators $\{E_\lambda(O)\otimes|\lambda\rangle\}$

**Claim.** To model measuring $O$ *and recording the outcome* $\lambda$ in a fresh register, use the channel
$$\mathcal{E}_O(\rho)=\sum_\lambda \big(E_\lambda(O)\otimes|\lambda\rangle\big)\,\rho\,\big(E_\lambda(O)\otimes\langle\lambda|\big)=\sum_\lambda E_\lambda(O)\,\rho\,E_\lambda(O)\otimes|\lambda\rangle\langle\lambda|.$$
Its Kraus operators are $\{E_\lambda(O)\otimes|\lambda\rangle\}$. Measuring $O$ on subsystem $B$ of a bipartite state is $I_A\otimes\mathcal{E}_O$, with Kraus operators $\{I_A\otimes E_\lambda(O)\otimes|\lambda\rangle\}$ — i.e. as if you measured $I_A\otimes O$.

---

### 1. In plain words
The non-selective map ([03](03-non-selective-measurement-channel.md)) throws the outcome away. A real measurement device should *output the result too*. So we attach a "pointer" register $\mathcal{H}$ and write the outcome $\lambda$ into it as $|\lambda\rangle$. The result is a classical-quantum state: post-measurement system, tagged by a classical label. The output register is diagonal (classical) in the $|\lambda\rangle$ basis — exactly a recorded outcome.

### 2. Toolbox
- Non-selective measurement formula $\sum_\lambda E_\lambda\rho E_\lambda$ ([03](03-non-selective-measurement-channel.md)).
- A Kraus map $\mathcal{E}(\rho)=\sum_k K_k\rho K_k^\dagger$ is a channel iff $\sum_k K_k^\dagger K_k=I$ (C5).
- Projector identities $E_\lambda^\dagger=E_\lambda$, $E_\lambda E_{\lambda'}=\delta_{\lambda\lambda'}E_\lambda$, $\sum_\lambda E_\lambda=I$.

### 3. The proof

**The instrument and its action.** Define $K_\lambda:=E_\lambda(O)\otimes|\lambda\rangle$ (maps the system into system⊗pointer).
1. $\mathcal{E}_O(\rho)=\sum_\lambda K_\lambda\rho K_\lambda^\dagger=\sum_\lambda(E_\lambda\otimes|\lambda\rangle)\rho(E_\lambda\otimes\langle\lambda|)=\sum_\lambda E_\lambda\rho E_\lambda\otimes|\lambda\rangle\langle\lambda|$ — the pointer ket·bra gives $|\lambda\rangle\langle\lambda|$.
2. The system marginal $\text{Tr}_{\text{pointer}}\mathcal E_O(\rho)=\sum_\lambda E_\lambda\rho E_\lambda$ recovers the non-selective map; the pointer is diagonal, holding a *classical* outcome distribution $\Pr[\lambda]=\text{Tr}(E_\lambda\rho)$.

**It's a valid channel (complete Kraus set).**
3. $\sum_\lambda K_\lambda^\dagger K_\lambda=\sum_\lambda(E_\lambda\otimes\langle\lambda|)(E_\lambda\otimes|\lambda\rangle)=\sum_\lambda E_\lambda^2\otimes\langle\lambda|\lambda\rangle=\sum_\lambda E_\lambda=I$. ✓ (Used $E_\lambda^2=E_\lambda$ and $\langle\lambda|\lambda\rangle=1$.)

**Measuring a subsystem.**
4. Acting only on $B$, the Kraus operators become $I_A\otimes E_\lambda(O)\otimes|\lambda\rangle$, so the channel is $I_A\otimes\mathcal{E}_O$. Since the projectors $I_A\otimes E_\lambda$ are exactly the spectral projectors of the global observable $I_A\otimes O$, recording $O$ on $B$ is identical to recording $I_A\otimes O$ on the whole system. ∎

### 4. Where the magic happens
**Tensoring each branch with its label $|\lambda\rangle$ turns "collapse" into a single linear channel** — the orthogonality $\langle\lambda|\lambda'\rangle=\delta_{\lambda\lambda'}$ keeps the branches from interfering, so the pointer stays classical. And $I_A\otimes E_\lambda$ being the projectors of $I_A\otimes O$ is why "measure B locally" = "measure $I_A\otimes O$ globally."

### 5. If he pushes back
- *"Why does the pointer have $\dim\mathcal{H}=$ #distinct eigenvalues?"* One orthonormal $|\lambda\rangle$ per outcome; that's all you need to record the result.
- *"How does this connect to CHSH?"* Alice's and Bob's local measurements are instruments on their halves; because $A_a$ acts as $A_a\otimes I$ and $B_b$ as $I\otimes B_b$, they commute and can be applied in either order — the basis for the locality structure of $S$.
- *"Is this the same as Stinespring/Naimark?"* It's the measurement special case; the general dilation theorems are C5.
