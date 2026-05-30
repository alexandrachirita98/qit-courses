# 06 — Two-universal hash families (and the $\mathbb Z_5$ example)

**Claim.** A family $\mathcal F$ of functions $X\to Z$ is **two-universal** if for every pair $x\ne x'$, a uniformly random $f\in\mathcal F$ collides with probability at most $1/|Z|$:
$$\Pr_{f}[f(x)=f(x')]\le\frac{1}{|Z|}.$$
The linear family $f_a(x_1,x_2)=a_1x_1+a_2x_2\bmod5$ over $\mathbb Z_5$ (seed $a\in\mathbb Z_5^2$) is two-universal.

---

### 1. In plain words
A hash function squashes long inputs to short outputs; collisions (two inputs hashing equal) are inevitable. "Two-universal" means: for any fixed pair of distinct inputs, a *randomly chosen* hash from the family collides them no more often than blind chance ($1/|Z|$). This randomness over the seed $a$ is what makes hashing extract near-uniform bits even when the attacker knows the family — the crux of the Leftover Hashing Lemma.

### 2. Toolbox
- $\mathbb Z_5=\{0,1,2,3,4\}$ is a field (5 prime), so nonzero elements are invertible.
- Family $\{f_a:a\in\mathbb Z_5^2\}$, $|{\mathcal F}|=25$, output space $Z=\mathbb Z_5$, $|Z|=5$.
- Collision condition: $f_a(x)=f_a(x')\iff a\cdot(x-x')=0\bmod5$.

### 3. The proof (the $\mathbb Z_5$ family is two-universal)
1. Fix $x=(x_1,x_2)\ne x'=(x_1',x_2')$ and let $d=x-x'\ne0\bmod5$. A collision means
$$f_a(x)-f_a(x')=a\cdot d=a_1d_1+a_2d_2=0\bmod5.$$
2. **Count the seeds $a$ satisfying $a\cdot d=0$.** Since $d\ne0$, WLOG $d_1\ne0$ (invertible in the field $\mathbb Z_5$). Then for *each* of the 5 choices of $a_2$, the equation $a_1d_1=-a_2d_2$ has a **unique** solution $a_1=-a_2d_2d_1^{-1}$. So exactly $5$ seeds collide.
3. **Collision probability:** $\Pr_a[f_a(x)=f_a(x')]=\dfrac{\#\{a:a\cdot d=0\}}{|\mathcal F|}=\dfrac{5}{25}=\dfrac15=\dfrac{1}{|Z|}.$
4. This meets the two-universal bound (with equality). ∎

**Concrete collision.** $a=(2,3)$: $f_{(2,3)}(1,1)=2+3=5\equiv0$ and $f_{(2,3)}(4,4)=8+12=20\equiv0$, so $(1,1)$ and $(4,4)$ collide under this particular seed — but only $1/5$ of seeds collide any fixed pair.

**Generalization.** $\mathcal F$ is **$\delta$-almost two-universal** if $\Pr_f[f(x)=f(x')]\le\delta$ for all $x\ne x'$; two-universal is the case $\delta=1/|Z|$.

### 4. Where the magic happens
**Over a field, the linear equation $a\cdot d=0$ (for fixed $d\ne0$) has exactly $|Z|^{(\text{seed dim}-1)}$ solutions** — a hyperplane through the origin — so the collision fraction is exactly $1/|Z|$. Field invertibility ($d_1^{-1}$ exists) is what pins the count; that's why the modulus is prime.

### 5. If he pushes back
- *"Why does universality need randomness over $f$?"* For any single fixed hash, an adversary could pick inputs that always collide; averaging over a random seed defeats that, giving the $1/|Z|$ guarantee.
- *"What if $|Z|=2^l$?"* Use linear maps over $\mathbb F_2$ (matrix–vector products mod 2); same argument, collision prob $2^{-l}$.
- *"Where is two-universality used?"* It directly bounds the output collision probability in the Leftover Hashing Lemma ([07](07-classical-leftover-hashing.md), [08](08-quantum-leftover-hashing.md)).
