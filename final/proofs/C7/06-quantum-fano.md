# 06 — The quantum Fano inequality

**Claim.** Let $\rho$ pass through a channel $\mathcal E$ (on $\mathbb C^d$), with entanglement fidelity $F=F(\rho,\mathcal E)$. The **entropy exchange** $H(\rho,\mathcal E)$ satisfies
$$H(\rho,\mathcal E)\le h(F)+(1-F)\log(d^2-1),$$
where $h$ is the binary entropy.

---

### 1. In plain words
Classical Fano bounds the entropy of an error in terms of the error probability. Here the "error probability" is $1-F$ (the chance the channel disturbed the state, measured by entanglement fidelity), and the "entropy of the error" is the entropy exchange $H(\rho,\mathcal E)$ — how much the environment learned. High fidelity ⇒ small entropy exchange ⇒ little leaked to the environment. The proof measures a 2-outcome POVM ("survived?" vs "disturbed?") and applies the data-processing/max-entropy bound.

### 2. Toolbox
- Entropy exchange $H(\rho,\mathcal E)=H(\rho')-H(|\psi_\rho\rangle\langle\psi_\rho|)$ where $\rho'=(I\otimes\mathcal E)|\psi_\rho\rangle\langle\psi_\rho|$, and $H(\text{pure})=0$.
- $F(\rho,\mathcal E)=\langle\psi_\rho|\rho'|\psi_\rho\rangle$ ([05](05-entanglement-fidelity.md)).
- $H(\rho')=\log d^2-D(\rho'\|I/d^2)$, and $D$ decreases under the measuring channel (data processing, [../C6/02](../C6/02-data-processing-inequality.md)).
- Max entropy on $d^2$ outcomes is $\log d^2$.

### 3. The proof
1. The reference+system space has dimension $d^2$, and the input $|\psi_\rho\rangle$ is pure, so $H(\rho,\mathcal E)=H(\rho')-0=H(\rho')$.
2. Rewrite via divergence from maximally mixed: $H(\rho')=\log d^2-D(\rho'\|I/d^2)$.
3. **Coarse-grain with the survival POVM** $\{|\psi_\rho\rangle\langle\psi_\rho|,\ I-|\psi_\rho\rangle\langle\psi_\rho|\}$, recording the outcome in a qubit $\rho''$. This is a channel, so it lowers divergence:
$$D(\rho'\|I/d^2)\ge D\big(\rho''\ \big\|\ \tfrac1{d^2}|0\rangle\langle0|+\tfrac{d^2-1}{d^2}|1\rangle\langle1|\big).$$
The reference state's "survive" probability is $1/d^2$ (overlap of $I/d^2$ with the pure $|\psi_\rho\rangle$), and $\rho''$ has survive-probability $F$.
4. Substitute back:
$$H(\rho')=\log d^2-D(\rho'\|I/d^2)\le\log d^2-D\big(\rho''\|\cdots\big).$$
Computing the right-hand side (a 2-point relative entropy with the survive/disturb split) gives exactly
$$\le h(F)+(1-F)\log(d^2-1).$$
5. Hence $H(\rho,\mathcal E)=H(\rho')\le h(F)+(1-F)\log(d^2-1)$. ∎

### 4. Where the magic happens
**Coarse-graining to a single yes/no question ("did the state survive?") via the data processing inequality** turns the $d^2$-dimensional entropy into a binary-entropy bound: $h(F)$ for the survive/disturb coin, plus $(1-F)\log(d^2-1)$ for "which of the $d^2-1$ ways it could have been disturbed." It's the quantum mirror of classical Fano.

### 5. If he pushes back
- *"What is entropy exchange physically?"* The entropy dumped into the environment when $\rho$ goes through $\mathcal E$ (equivalently $H$ of the environment's state in a Stinespring dilation). Small ⇒ reversible-ish.
- *"Why $d^2-1$?"* The reference+system lives in dimension $d^2$; conditioned on "disturbed," there are $d^2-1$ orthogonal directions to spread over.
- *"Used where?"* It certifies compression: high $F$ ⇒ low entropy exchange ⇒ faithful recovery, the engine behind Schumacher's converse ([07](07-schumacher-source-coding.md)).
