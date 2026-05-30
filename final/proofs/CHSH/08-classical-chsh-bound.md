# 08 — Classical CHSH: a local hidden variable gives $|S|\le 2$

**Claim.** If the outcomes come from a shared classical (hidden) variable $\omega$, with $A_a(\omega),B_b(\omega)\in\{\pm1\}$ and
$$\mathbb{E}[A_a\otimes B_b]=\int A_a(\omega)B_b(\omega)\,p(\omega)\,d\omega,$$
then $|S|=|\mathbb{E}[A_0B_0]+\mathbb{E}[A_0B_1]+\mathbb{E}[A_1B_0]-\mathbb{E}[A_1B_1]|\le 2.$

---

### 1. In plain words
If Alice's and Bob's answers are just deterministic functions of some shared random seed $\omega$ (no quantum weirdness), then **for every fixed $\omega$** the CHSH combination of their $\pm1$ answers equals $\pm2$ — never more. Averaging over $\omega$ can't push an average of $\pm2$ values past 2. That's the whole Bell inequality. (The lecture gives Bell's slicker integral derivation "backwards"; the pointwise version below is the easiest to remember.)

### 2. Toolbox
- All values are $\pm1$: $A_a(\omega),B_b(\omega)\in\{\pm1\}$.
- $p(\omega)\ge0$, $\int p(\omega)d\omega=1$ (a probability density).
- $|\mathbb{E}[f]|\le\max_\omega|f(\omega)|$ for any random variable $f$.

### 3. The proof (pointwise — the easy way)

Fix $\omega$ and write $a_i=A_i(\omega),\ b_j=B_j(\omega)\in\{\pm1\}$. Consider the integrand
$$s(\omega)=a_0b_0+a_0b_1+a_1b_0-a_1b_1=a_0(b_0+b_1)+a_1(b_0-b_1).$$
1. Since $b_0,b_1\in\{\pm1\}$, **exactly one** of $(b_0+b_1)$ and $(b_0-b_1)$ is $0$ and the other is $\pm2$:
 - if $b_0=b_1$: $b_0+b_1=\pm2$, $b_0-b_1=0$;
 - if $b_0\ne b_1$: $b_0+b_1=0$, $b_0-b_1=\pm2$.
2. So $s(\omega)=a_i\cdot(\pm2)=\pm2$ (one term vanishes, the other is $\pm1\cdot\pm2$). Hence $|s(\omega)|=2$ for every $\omega$.
3. Average: $S=\int s(\omega)p(\omega)d\omega$, so $|S|\le\int|s(\omega)|p(\omega)d\omega=\int 2\,p(\omega)d\omega=2.$ ∎

### 4. Bell's derivation (the lecture's "backwards" version)
Split $S=x+y$ with $x=\mathbb{E}[A_0B_0]+\mathbb{E}[A_0B_1]$, $y=\mathbb{E}[A_1B_0]-\mathbb{E}[A_1B_1]$. The aim is $|x|+|y|\le2$, which follows from proving $|y|\le2\pm x$. The trick: insert $\pm A_0B_0A_1B_1$ (which equals $\pm1$) to factor,
$$y=\int A_1B_0\,(1\pm A_0B_1)\,p\,d\omega-\int A_1B_1\,(1\pm A_0B_0)\,p\,d\omega.$$
Each $|A_1B_0|\le1$, $|A_1B_1|\le1$, and the factors $(1\pm A_0B_1),(1\pm A_0B_0)\ge0$, so
$$|y|\le\int(1\pm A_0B_1)p\,d\omega+\int(1\pm A_0B_0)p\,d\omega=2\pm x.$$
Hence $|S|=|x+y|\le|x|+|y|\le2$. ∎

### 5. Where the magic happens
**For $\pm1$ values, $b_0+b_1$ and $b_0-b_1$ can't both be nonzero** — one is always 0. That forces the pointwise combination to be exactly $\pm2$, and an average of $\pm2$'s lives in $[-2,2]$. The quantum world escapes this because Alice's and Bob's outcomes don't simultaneously exist as fixed $\pm1$ numbers before measurement (no joint $A_a(\omega),B_b(\omega)$).

### 5b. If he pushes back
- *"Where exactly does locality enter?"* In assuming a *single* $\omega$ determines both $A_a(\omega)$ and $B_b(\omega)$ independently of the other's setting — outcomes are pre-assigned and local. Quantum correlations have no such joint assignment.
- *"Why can quantum reach $2\sqrt2>2$?"* Because $S^2=4I-[A_0,A_1]\otimes[B_0,B_1]$ ([05](05-khalfin-tsirelson-landau-identity.md)) and non-commuting observables make the correction positive; classically the commutators vanish.
- *"Is $2\sqrt2/2=\sqrt2$ significant?"* Yes — it's the maximal quantum-over-classical advantage for CHSH.
