# 03 — A channel can't decrease entropy iff it is bistochastic (unital)

**Claim.** For a channel $\mathcal E$ on $\mathbb C^d$, $H(\mathcal E(\rho))\ge H(\rho)$ for all $\rho$ **iff** $\mathcal E$ is unital ($\mathcal E(I)=I$), i.e. bistochastic.

---

### 1. In plain words
This is the quantum second-law flavored statement, and it's a one-line corollary of the data processing inequality. Compare any state $\rho$ to the maximally mixed state $I/d$ using the divergence; the DPI says processing shrinks that divergence. When the channel is unital it fixes $I/d$, and the algebra turns "divergence shrinks" into "entropy grows." It's the operator version of "doubly-stochastic maps raise Shannon entropy" ([C4/15](../C4/15-doubly-stochastic-never-decreases-entropy.md)).

### 2. Toolbox
- DPI: $D(\mathcal E(\rho)\|\mathcal E(\sigma))\le D(\rho\|\sigma)$ ([02](02-data-processing-inequality.md)).
- Key identity: $D(\rho\|I/d)=\log d-H(\rho)$.
- Unital: $\mathcal E(I/d)=I/d$.

### 3. The proof

**The identity.**
1. $D(\rho\|I/d)=-\text{Tr}\big(\rho(\log\tfrac Id-\log\rho)\big)=-\text{Tr}\big(\rho(-\log d\cdot I-\log\rho)\big)=\log d\,\underbrace{\text{Tr}\rho}_{1}+\underbrace{\text{Tr}\rho\log\rho}_{-H(\rho)}=\log d-H(\rho).$

**Unital ⇒ entropy non-decreasing.** Take $\sigma=I/d$ in the DPI; unital gives $\mathcal E(I/d)=I/d$:
2. $D(\mathcal E(\rho)\|I/d)\le D(\rho\|I/d)$.
3. Apply the identity to both sides: $\log d-H(\mathcal E(\rho))\le\log d-H(\rho)$, hence $H(\mathcal E(\rho))\ge H(\rho)$. ∎

**Converse (entropy non-decreasing ⇒ unital).** Expanding the DPI gap for general $\sigma=I/d$:
4. $0\le D(\rho\|I/d)-D(\mathcal E(\rho)\|\mathcal E(I/d))=H(\mathcal E(\rho))-H(\rho)+\big(1-\text{Tr}(\mathcal E(\rho)\log\mathcal E(I))\big)\log d.$
5. If $H(\mathcal E(\rho))\ge H(\rho)$ is to hold for *all* $\rho$ with no extra slack, one needs $\mathcal E(I)=I$ (the correction term vanishes only when $\mathcal E(I/d)=I/d$). So entropy-non-decreasing forces unitality. ∎

### 4. Where the magic happens
**$D(\rho\|I/d)=\log d-H(\rho)$:** divergence-from-maximally-mixed is just "entropy deficit." So the DPI ("divergence shrinks") *is* "entropy grows," provided the channel pins the reference state $I/d$ — which is exactly unitality.

### 5. If he pushes back
- *"Relation to the classical statement?"* Identical structure to [C4/15](../C4/15-doubly-stochastic-never-decreases-entropy.md): bistochastic = doubly-stochastic; both preserve the uniform/maximally-mixed state and so can't sharpen.
- *"Example?"* The depolarizing channel is unital ⇒ raises entropy ([C4/18](../C4/18-depolarizing-increases-entropy.md)). A non-unital channel (e.g. amplitude damping toward $|0\rangle$) *can* decrease entropy (it can purify toward $|0\rangle$).
- *"Why does the converse need 'for all $\rho$'?"* A single $\rho$ might accidentally gain entropy; the *iff* is about the property holding universally.
