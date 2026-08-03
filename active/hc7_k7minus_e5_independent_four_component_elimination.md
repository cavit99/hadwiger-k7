# Independent five-cuts with four exterior components

**Status:** written computation-free unbounded theorem; separate internal
audit.  The theorem eliminates the complete four-component residue in
`(E5)`; it does not prove `(E5)`.

Write `K_7^-` for `K_7` with one edge deleted.  Recall that a minimum
`E5` enemy is a five-connected, `K_7^-`-minor-free graph `G` with

```text
|E(G)| >= 4|V(G)|-7,
```

chosen first with minimum order and then with minimum size.  Let `S` be a
cut of order five and let `C_1,...,C_r` be the components of `G-S`.  Put

```text
delta(C_i)=|E(G[C_i])|+|E_G(C_i,S)|-4|C_i|.
```

Every `C_i` is full to `S`.  Moreover, for every nonempty `X subseteq C_i`,

```text
|N_G(X)| >= 5.                                      (1)
```

## Lemma 1 (rooted `K_4` completion)

Suppose that `r>=4` and `G[S]` is edgeless.  If, for some component `C_0`
and some `x in S`, the graph

```text
G[(S-{x}) union C_0]
```

contains a `K_4` minor rooted at the four vertices of `S-{x}`, then `G`
contains a `K_7^-` minor.

### Proof

Let `R_1,...,R_4` be the four rooted branch sets.  Take three other
components `D_1,D_2,D_3`.  The set

```text
X={x} union D_1
```

is connected.  It is adjacent to every `R_i`: the component `D_1` is full
to `S`, and the corresponding root belongs to `R_i`.  Each of `D_2,D_3`
is adjacent to all four rooted bags and to `X` through `x`.  Thus

```text
R_1,R_2,R_3,R_4,X,D_2,D_3
```

are pairwise adjacent except possibly for `D_2,D_3`.  They form a
`K_7^-` model.  \(\square\)

## Lemma 2 (a critical boundary leaf)

Suppose that `r=4`, `G[S]` is edgeless, and `C` is a component of `G-S`
with `delta(C)>=4`.  Put

```text
H=G[S union C],              H*=H+E(K_5[S]).
```

Then some `x in S` has exactly one neighbour in `C`.

### Proof

The graph `H*` is five-connected.  Indeed, after deleting at most four
vertices, some member of the clique `S` remains.  A component not containing
the remaining part of `S` would be a nonempty set `Y subseteq C` with
`|N_G(Y)|<=4`, contrary to (1).

Fix an edge `xy` of the added boundary clique.  The graph `K_5-xy` has the
three-vertex cover `S-{x,y}`.  Assign its three vertices injectively to the
three components of `G-S` other than `C`, and assign every edge of `K_5-xy`
to a cover end.  Inside the component assigned to `a`, take a connected
subgraph meeting a neighbour of `a` and a neighbour of every other end of
an edge assigned to `a`, and contract that subgraph into `a`.  Deleting
unused vertices and edges gives `H*-xy` as a proper minor of `G`.

This minor is target-free and has

```text
|E(H*-xy)|=4|C|+delta(C)+9
            >=4(|C|+5)-7.
```

If it were five-connected, it would be a smaller `E5` enemy.  Therefore
every edge of the boundary `K_5` is critical for five-connectivity in
`H*`.

Mader's critical-cycle theorem says that a cycle of critical edges in a
`k`-connected graph contains a vertex of degree `k`.  Apply it to any
Hamilton cycle of `H*[S]`.  Some `x in S` has `d_{H*}(x)=5`.  Four of its
neighbours are the other boundary vertices, and fullness gives at least one
neighbour in `C`.  Hence it has exactly one neighbour in `C`.  \(\square\)

## Lemma 3 (the high-excess lobe is terminal)

Under the hypotheses of Lemma 2, `G` contains a `K_7^-` minor.

### Proof

Take `x` from Lemma 2, put `Z=S-{x}`, and retain the notation
`H=G[S union C]`.  Suppose first that `H-x` has a `Z`-rooted `K_4` model.
Lemma 1 gives the target minor, so assume otherwise.

Since `x` has degree one in `H`, any `Z`-rooted `K_4` model in `H` can be
made disjoint from `x`: if a branch set contains `x`, deleting that
non-root leaf preserves the model.  Hence `H` itself has no such rooted
model.

By Fabila-Monroy and Wood, Theorem 15, `H` is a spanning subgraph of one
of their six rooted-`K_4` obstructions.  Such an obstruction is obtained
from a planar skeleton by adding, at triangles `T`, cliques `X_T` complete
to `T`; the four nominated roots lie in the skeleton.

No vertex of `C` belongs to an added clique.  Otherwise take a component
`Y` of the graph induced by the members of `C` in one such clique.  The
only possible boundary vertex in that clique is `x`, and `C` is a component
of `G-S`, so

```text
N_G(Y)=N_H(Y) subseteq T union {x}.
```

This contradicts (1).  It follows that `H-x` is planar, whether `x` lies
in the planar skeleton or in an added clique.  As `d_H(x)=1`, for
`c=|C|>=4` we obtain

```text
|E(H)| <= 3(c+4)-6+1 = 3c+7,
```

and therefore `delta(C)<=7-c<=3`, contrary to the choice of `C`.

It remains to consider `c<=3`.  For `c=1` and `c=2`, the independent
boundary and `d_H(x)=1` give at most five and ten edges, respectively, so
`delta(C)<=2`.  If `c=3` and `delta(C)>=4`, all sixteen possible edges
consistent with `d_H(x)=1` must be present: `C` is a triangle and every
vertex of `Z` is adjacent to every vertex of `C`.  Match three vertices of
`C` to three roots in `Z` and retain the fourth root as a singleton.  These
are four connected, pairwise-adjacent rooted bags in `H-x`, contradicting
the first paragraph.  \(\square\)

## Theorem 4 (four-component elimination)

Let `G` be a minimum `E5` enemy and let `S` be a cut of order five.  Then
`G-S` does not have four components.

### Proof

The existing four-component reduction shows that `G[S]` is edgeless.  If
`q=|E(G)|-(4|V(G)|-7)`, direct edge accounting gives

```text
sum_i delta(C_i)=q+13>=13.
```

Thus some component has excess at least four.  Lemma 3 gives a `K_7^-`
minor, a contradiction.  \(\square\)

## External inputs

- Wolfgang Mader, *Ecken vom Grad n in minimalen n-fach zusammenhängenden
  Graphen*, Archiv der Mathematik 23 (1972), 219--224, Theorem 1.
- Ruy Fabila-Monroy and David R. Wood, *Rooted `K_4`-Minors*, Electronic
  Journal of Combinatorics 20(2) (2013), P64, Theorem 15,
  <https://doi.org/10.37236/3476>.
