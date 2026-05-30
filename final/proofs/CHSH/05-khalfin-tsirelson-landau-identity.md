# 05 — The Khalfin–Tsirelson–Landau identity: $S^2=4I-[A_0,A_1]\otimes[B_0,B_1]$

**Claim.** For $\pm1$ observables $A_0,A_1$ (on Alice) and $B_0,B_1$ (on Bob), the CHSH operator
$$S=A_0\otimes B_0+A_0\otimes B_1+A_1\otimes B_0-A_1\otimes B_1$$
satisfies
$$S^2=4I-[A_0,A_1]\otimes[B_0,B_1],\qquad [X,Y]:=XY-YX.$$

---

### 1. In plain words
We square the CHSH operator. The "diagonal" terms collapse to a clean $4I$ (thanks to $A^2=B^2=I$), and all the cross terms bundle into a single commutator-times-commutator. The point: $S^2$ deviates from $4I$ only by how badly Alice's two observables fail to commute, *times* how badly Bob's do. If either party's observables commute, $S^2=4I$ and you're stuck at the classical bound. This identity is the entire content of Tsirelson's theorem.

### 2. Toolbox
- $A_0^2=A_1^2=I$ and $B_0^2=B_1^2=I$ ([02](02-pm1-observables-square-to-identity.md)).
- $(X\otimes Y)(X'\otimes Y')=(XX')\otimes(YY')$ (tensor product multiplication).
- $[X,Y]=XY-YX$; note $YX-XY=-[X,Y]$.

### 3. The proof

**Group the sum.**
1. $S=A_0\otimes(B_0+B_1)+A_1\otimes(B_0-B_1)$ — factor Alice's operators out.

**Square it** (four terms):
2. $S^2=A_0^2\otimes(B_0+B_1)^2+A_1^2\otimes(B_0-B_1)^2+A_0A_1\otimes(B_0+B_1)(B_0-B_1)+A_1A_0\otimes(B_0-B_1)(B_0+B_1).$

**Diagonal terms → $4I$.** Using $A_0^2=A_1^2=I$ and $B_0^2=B_1^2=I$:
3. $(B_0+B_1)^2=2I+(B_0B_1+B_1B_0)$ and $(B_0-B_1)^2=2I-(B_0B_1+B_1B_0)$.
4. Their sum: $I\otimes\big[(2I+\cdots)+(2I-\cdots)\big]=I\otimes 4I=4I$ — the anticommutator $B_0B_1+B_1B_0$ cancels.

**Cross terms → one commutator product.**
5. $(B_0+B_1)(B_0-B_1)=B_0^2-B_0B_1+B_1B_0-B_1^2=B_1B_0-B_0B_1=-[B_0,B_1]$ (the $\pm I$ from the squares cancel).
6. $(B_0-B_1)(B_0+B_1)=B_0B_1-B_1B_0=+[B_0,B_1]$.
7. So the cross terms are $A_0A_1\otimes(-[B_0,B_1])+A_1A_0\otimes[B_0,B_1]=(A_1A_0-A_0A_1)\otimes[B_0,B_1]=-[A_0,A_1]\otimes[B_0,B_1].$

**Assemble.**
8. $S^2=4I-[A_0,A_1]\otimes[B_0,B_1]$. ∎

### 4. Where the magic happens
**The squares ($A^2=B^2=I$) kill the diagonal down to $4I$, and the cross terms collapse the anticommutators, leaving only commutators.** Non-commutativity is the *only* way $S^2$ can exceed $4I$ — and it must be non-commutativity on **both** sides (a tensor product of two commutators).

### 5. If he pushes back
- *"Why does this immediately bound $S$?"* Because $\|[A_0,A_1]\|\le2$ and $\|[B_0,B_1]\|\le2$ ([09](09-commutator-norm-bound.md)), so $S^2\le 4I+4I=8I$, giving $\|S\|\le2\sqrt2$ ([06](06-tsirelson-bound.md)).
- *"What if $[A_0,A_1]=0$?"* Then $S^2=4I$, so $\|S\|\le2$ — commuting (classical-like) observables can't beat the Bell bound.
- *"Is the identity exact, no inequalities?"* Yes, it's an operator identity. The inequalities only enter when we bound the commutator norms.
