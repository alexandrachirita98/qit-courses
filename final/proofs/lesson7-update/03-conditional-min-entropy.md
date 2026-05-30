# 03 — Conditional min-entropy (classical and quantum)

**Claim.**
- **Classical:** $H_{\min}(X|Y)=-\log\sum_y P(y)\max_x P(x|y)$ = $-\log$ of the best guessing probability for $X$ given $Y$.
- **Quantum:** $H_{\min}(A|B)_\rho=\max_{\sigma_B\in\mathcal S(\mathcal H_B)}\sup\{\lambda\in\mathbb R:\rho_{AB}\le2^{-\lambda}I_A\otimes\sigma_B\}$, and $H_{\min}(A|B)\le H_{\min}(A)$.

---

### 1. In plain words
This generalizes min-entropy to "how guessable is $X$ when the adversary *also* holds side information?" Classically, given $Y=y$ the attacker guesses the most likely $x$; averaging over $y$ gives the overall guess probability, and min-entropy is its $-\log$. Quantumly the side info $B$ is a quantum system, and we can't talk about $\max_x P(x|y)$ directly — instead we ask how far below "$I_A\otimes\sigma_B$" the state $\rho_{AB}$ can be squeezed. The bigger we can make $\lambda$, the more uniform/unguessable $A$ is given $B$.

### 2. Toolbox
- Joint $P(x,y)$, marginal $P(y)=\sum_x P(x,y)$, conditional $P(x|y)=P(x,y)/P(y)$.
- Optimal guessing given $Y$: guess $\arg\max_x P(x|y)$; $p_{\text{guess}}(X|Y)=\sum_y P(y)\max_x P(x|y)=\sum_y\max_x P(x,y)$.
- Quantum: $\mathcal S(\mathcal H_B)$ = normalized states; the operator inequality $\rho_{AB}\le2^{-\lambda}I_A\otimes\sigma_B$.

### 3. The proof / derivation

**Classical guessing form.**
1. Given $Y=y$, the best guess succeeds with prob $\max_x P(x|y)$. Averaging over $y$,
$$p_{\text{guess}}(X|Y)=\sum_y P(y)\max_x P(x|y)=\sum_y\max_x P(x,y).$$
2. Define $H_{\min}(X|Y)=-\log p_{\text{guess}}(X|Y)=-\log\sum_y P(y)\max_x P(x|y)$. ∎

**Worked example.** $P(0,0)=0.2,P(0,1)=0.3,P(1,0)=0.1,P(1,1)=0.4$.
- $P(Y{=}0)=0.3,\ P(Y{=}1)=0.7$.
- $\max_x P(x|0)=\max(\tfrac{0.2}{0.3},\tfrac{0.1}{0.3})=\tfrac23$; $\max_x P(x|1)=\max(\tfrac{0.3}{0.7},\tfrac{0.4}{0.7})=\tfrac47$.
- $\sum_y P(y)\max_x P(x|y)=0.3\cdot\tfrac23+0.7\cdot\tfrac47=0.2+0.4=0.6$.
- $H_{\min}(X|Y)=-\log0.6\approx0.737$ bits. (Equivalently $\sum_y\max_x P(x,y)=0.2+0.4=0.6$.)

**Quantum definition & the bound $H_{\min}(A|B)\le H_{\min}(A)$.**
3. The quantum conditional min-entropy is the largest $\lambda$ (optimized over a reference $\sigma_B$) with $\rho_{AB}\le2^{-\lambda}I_A\otimes\sigma_B$ — "how much smaller than a maximally-uncertain-$A$ product state can $\rho_{AB}$ be made."
4. Restricting the inequality to $A$ alone (take $B$ trivial / trace out $B$): $\rho_A\le2^{-\lambda}I_A$ gives $\sup\{\lambda:\rho_A\le2^{-\lambda}I_A\}=H_{\min}(A)$. Since adding the side system $B$ only enlarges the feasible set of $\lambda$ (more $\sigma_B$ to optimize), $H_{\min}(A|B)_\rho\le H_{\min}(A)_\rho$ — **side information never hurts the adversary**. ∎

### 4. Where the magic happens
**Conditional min-entropy = $-\log$(guessing probability with side info).** Classically it's an explicit max-then-average; quantumly the "max guess" is replaced by the operator-inequality optimization $\rho_{AB}\le2^{-\lambda}I_A\otimes\sigma_B$, which still measures "how close to uniform $A$ looks from $B$'s viewpoint." More side info ⇒ smaller conditional min-entropy.

### 5. If he pushes back
- *"Why the operator inequality and not $\max_x P(x|\rho_B)$?"* Quantum side info has no fixed measurement; the semidefinite form is measurement-independent and reduces to the classical guess probability when everything is diagonal.
- *"Operational meaning of the quantum one?"* $2^{-H_{\min}(A|B)}$ = optimal probability to guess $A$ by measuring $B$ (the guessing-probability theorem, König–Renner–Schaffner).
- *"Why does it appear in QKD?"* It directly bounds Eve's guessing probability of the key given her quantum memory $E$; smoothing it ([05](05-smooth-min-entropy.md)) makes it robust, and the LHL ([08](08-quantum-leftover-hashing.md)) turns it into a secrecy guarantee.
