# A full exterior has a relative six-contraction-critical quotient

**Status:** written elementary deduction from the computer-assisted adjacent
two-block exterior theorem; adjacent independent cold audit GREEN.  The
exact separator conclusion is unbounded, but it holds in a contracted
quotient of the critical host.  No coefficient-four density retention is
claimed.

Write `K_7^-` for `K_7` with one edge deleted.

## Theorem 1 (terminal full-exterior quotient)

Let `G` be a seven-connected graph with no `K_7^-` minor.  Let `v` have
degree eight, put `J=G[N_G(v)]`, and suppose

```text
delta(J)>=3,
G-N_G[v] is one connected component C,
N_G(C)=V(J).
```

If `|C|>=2`, then contracting edges with both ends in the current image of
`C` produces a minor `H` with the following properties.  With `R` denoting
the image of `C` in `H`,

1. `H` is exactly six-connected and has no `K_7^-` minor;
2. `R` is connected, `N_H(R)=V(J)`, and `|R|>=3`;
3. for every edge `ab` of `H[R]`, the graph `H/ab` is exactly
   five-connected; and
4. for every such edge `ab`, there is an order-six separator `S_ab` of
   `H` which contains `a,b` and for which every component `D` of
   `H-S_ab` satisfies

   ```text
   N_H(D)=S_ab.
   ```

In particular, every component of `H-S_ab` has a neighbour at each of
`a` and `b`.

The same conclusion is obtained after any choice of the first exterior
edge and any maximal continuation which preserves six-connectivity.

### Proof

We first record the elementary contraction fact used twice below.  If `F`
is `k`-connected and `xy` is an edge, then `F/xy` is
`(k-1)`-connected, provided the quotient has at least `k` vertices.  Let
`z` be the contracted vertex.  Indeed, a cut `X` of `F/xy` of order at
most `k-2` would lift as follows.  If `z` is not in `X`, then contracting
`xy` in the connected graph `F-X` cannot disconnect it.  If `z` is in
`X`, then

```text
(X-{z}) union {x,y}
```

has order at most `k-1`, and deleting it from `F` gives exactly the same
graph as deleting `X` from `F/xy`.  Both alternatives contradict
`k`-connectivity of `F`.

First, `|C|` cannot equal two.  In that case its two singleton vertices
would themselves be an adjacent connected two-block partition of `C`, and
the associated quotient would be `G`, which is seven-connected and hence
six-connected.  This contradicts Corollary 2 of
[`hc7_k7minus_adjacent_exterior_pair_elimination.md`](hc7_k7minus_adjacent_exterior_pair_elimination.md).

Choose any edge of `G[C]` and contract it.  Seven-connectivity and the
preceding fact show that the resulting graph is six-connected.  If this
first contraction leaves exactly two exterior vertices, its two branch
sets give another adjacent connected two-block partition forbidden by that
corollary; therefore this case cannot occur.  Continue contracting edges
within the current image of `C` whenever the resulting
graph remains six-connected, and stop when no such edge remains.  This
process terminates.  At every stage, the exterior vertices correspond to
a partition of the original `C` into connected branch sets.  Its image is
connected and full to `J`, while `v` remains complete to `J` and
anticomplete to the exterior image.

More generally, no later contraction can first produce a six-connected
stage with exactly two exterior vertices.  Such a stage would be obtained
from a partition

```text
C=X dot_union Y
```

into two nonempty connected sets with an `X-Y` edge, contrary to
Corollary 2 of
[`hc7_k7minus_adjacent_exterior_pair_elimination.md`](hc7_k7minus_adjacent_exterior_pair_elimination.md).
Nor can the process reach one exterior vertex, because immediately before
the last contraction it would have a forbidden six-connected two-vertex
exterior.  Thus the terminal image `R` has at least three vertices.

Let `H` be the terminal quotient.  It is at least six-connected and remains
`K_7^-`-minor-free because it is a minor of `G`.  If it were
seven-connected, the elementary contraction fact would make the
contraction of any edge of the connected graph `H[R]` six-connected.
This contradicts maximality.  Hence `H` is exactly six-connected.

Fix `ab in E(H[R])`.  Maximality says that `H/ab` is not
six-connected, while the elementary contraction fact says that it is
five-connected.  Therefore its connectivity is exactly five.  Let `z`
be the contracted vertex and let `X` be an order-five separator of
`H/ab`.

We must have `z in X`.  Otherwise `H-X` is connected by
six-connectivity, and contracting `ab` in `H-X` would show that
`(H/ab)-X` is connected.  Now put

```text
S_ab=(X-{z}) union {a,b}.
```

This set has order six, and `H-S_ab` is identical to `(H/ab)-X`.
Consequently it is disconnected, so `S_ab` is an exact order-six
separator of `H`.

Finally, let `D` be a component of `H-S_ab`.  Its neighbourhood is a
subset of `S_ab`.  Because there is another component of `H-S_ab`, the set
`N_H(D)` separates `D` from a vertex outside `D union N_H(D)`.  The
six-connectivity of `H` therefore gives `|N_H(D)|>=6`.  Since
`|S_ab|=6`, equality holds and `N_H(D)=S_ab`.  This proves all four
claims. `\square`

## Proposition 2 (exact density and exterior-excess ledger)

Let

```text
G=H_0, H_1, ..., H_q=H
```

be a contraction sequence from Theorem 1.  If the edge contracted in
`H_i` has `t_i` common neighbours in `H_i`, then

```text
|E(H)|-4|V(H)|
  = |E(G)|-4|V(G)| + sum_{i=0}^{q-1}(3-t_i).       (1)
```

Equivalently, for the current exterior image `R_i` define

```text
rho_i=|E(H_i[R_i])|+|E_{H_i}(R_i,J)|-4|R_i|.
```

Then

```text
rho_{i+1}=rho_i+3-t_i,                              (2)
|E(H_i)|-4|V(H_i)|=rho_i+|E(J)|-28.                 (3)
```

For any terminal separator `S_ab` from Theorem 1, if
`D_1,...,D_r` are the components of `H-S_ab` and

```text
eta(D_j)=|E(H[D_j])|+|E_H(D_j,S_ab)|-4|D_j|,
```

then

```text
|E(H)|-4|V(H)|=|E(H[S_ab])|+sum_j eta(D_j)-24.      (4)
```

### Proof

Contracting an edge with `t_i` common neighbours removes the contracted
edge and identifies exactly `t_i` duplicate edge pairs.  It therefore
removes `1+t_i` edges and one vertex, proving (1).  The centre `v` is
anticomplete to every `R_i`, so all common neighbours of an edge in
`H_i[R_i]` lie in `R_i union J`; the same count gives (2).  The vertex
and edge decompositions

```text
V(H_i)={v} dot_union V(J) dot_union R_i,
E(H_i)=E(J) dot_union E(v,J) dot_union E(H_i[R_i])
       dot_union E_{H_i}(R_i,J),
```

with `|J|=|E(v,J)|=8`, give (3).  Finally, no edge joins two different
components of `H-S_ab`.  Splitting all vertices and edges over
`S_ab,D_1,...,D_r` gives (4). `\square`

## What the normal form does and does not retain

Theorem 1 is an unbounded structural normal form: the exterior image can
have arbitrary order, but every one of its edges lies in a minimum
six-vertex cut, and every component behind that cut is full to all six cut
vertices.  Thus the remaining object is *relatively
six-contraction-critical along its exterior edges* in standard
connectivity language.

There are two important limitations.

First, `S_ab` is a separator of the quotient `H`.  Lifting it to `G`
requires replacing any contracted vertex in `S_ab` by its entire branch
set, so it need not give an order-six separator of `G`.

Second, (1) shows that connectivity-preserving contraction does not by
itself preserve coefficient-four density.  Density is retained along a
sequence if its cumulative common-neighbour cost satisfies

```text
sum_i(t_i-3) <= |E(G)|-4|V(G)|,
```

but neither maximality nor the adjacent-pair theorem currently supplies
this inequality.  The same uncontrolled term appears in the exterior
excess through (2).  A target-rich calibration shows why connectivity and
fullness alone cannot control it: take `J=K_8`, make a clique `C=K_r`
complete to `J`, and add `v` complete to `J` and anticomplete to `C`.
The resulting graph is eight-connected, while an edge of `C` has `r+6`
common neighbours.  This construction contains a `K_7` and therefore
does not refute a density-retention theorem using `K_7^-`-minor exclusion;
it only isolates the additional input such a theorem would need.

Equation (4) remains available as an exact separator-excess decomposition
if a future argument controls the loss in (1).  At present, however, the
terminal quotient cannot be fed into a coefficient-four extremal descent
without a new low-common-neighbour contraction theorem or a direct bound
on the cumulative loss.

## Dependency and scope

The only non-elementary input is Corollary 2 of the adjacent-pair exterior
quotient theorem.  That corollary depends on the exhaustive census of
`611,678` six-connected quotients, reproduced in its adjacent independent
GREEN audit.

The singleton exterior `|C|=1` is outside the abstract theorem: it has no
exterior edge to contract.  It is irrelevant in the actual critical-host
application, where the standard order bound gives `|V(G)|>=26` and hence

```text
|C|=|V(G)|-9>=17.
```

This is the critical-host defect bound recorded, for example, in
[`hc7_k7minus_critical_degree_eight_codegree_three_dichotomy.md`](hc7_k7minus_critical_degree_eight_codegree_three_dichotomy.md).
There the full-exterior reduction supplies exactly the hypotheses above
when the exterior is nonempty and all eight edges incident with the
degree-eight centre have codegree at least three.  The note does not
eliminate the terminal normal form and hence does not prove Conjecture 21
or `HC_7`.
