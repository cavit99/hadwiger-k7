# Internal audit: independent five-cut with four components

**Verdict:** GREEN.

**Audited source:**
[`hc7_k7minus_e5_independent_four_component_elimination.md`](hc7_k7minus_e5_independent_four_component_elimination.md)

**Source SHA-256:**
`ed72324ab14b310522ac579b4207f1a0c3391b9061d9c1de09cf40b6ec0cfa5d`

The theorem is an unbounded, computation-free elimination of the
four-component case in a minimum enemy to `(E5)`.  It does not prove `(E5)`
or the seven-connected `4n-2` target.

## 1. The completed shore is five-connected

For a component `C` of `G-S`, put

```text
H=G[S union C],              H*=H+E(K_5[S]).
```

If at most four vertices are deleted from `H*`, at least one member of the
boundary clique remains.  Any component not containing the remaining
boundary lies in `C` and has all its neighbours in the deleted set.  This
contradicts the five-connectivity consequence

```text
|N_G(Y)|>=5                  for nonempty Y subseteq C.
```

Thus `H*` is five-connected.

## 2. Every boundary-clique edge is critical

For `xy subseteq S`, the edge set of `K_5-xy` is covered by the three
vertices `S-{x,y}`.  Assigning those vertices to the other three full
components and absorbing one connected subtree per assigned component
realises every edge of `K_5-xy`.  The assigned subtrees are disjoint, and
unwanted edges can be deleted, so `H*-xy` is literally a proper minor of
`G`, not merely an abstract augmentation.

Its exact size is

```text
|E(H*-xy)|=4|C|+delta(C)+9 >= 4(|C|+5)-7.
```

It inherits `K_7^-`-minor-freeness.  Were it five-connected, it would be a
smaller `(E5)` enemy.  Hence every edge of the boundary `K_5` is critical
for five-connectivity in `H*`.

Mader's critical-cycle theorem applies exactly: in a `k`-connected
undirected graph, every cycle of critical edges contains a vertex of degree
`k`.  A cycle in `H*[S]` therefore contains `x` with `d_{H*}(x)=5`.
The four other boundary vertices already account for four neighbours, and
fullness supplies a neighbour in `C`; consequently `x` has exactly one
neighbour in `C`.

The cited source is Wolfgang Mader, *Ecken vom Grad n in minimalen n-fach
zusammenhängenden Graphen*, Archiv der Mathematik 23 (1972), 219--224,
Theorem 1.  The statement and the definition of a critical edge were also
matched against the verbatim formulation in Zeev Nutov, *The
k-Connected Subgraph Problem*, Theorem 2.3.

## 3. Root avoidance and the planar bound

Let `Z=S-{x}`.  The completion lemma requires its rooted model in `H-x`;
this avoids the overlap that would occur if the fifth boundary vertex were
allowed inside a rooted branch set.  The revised proof handles this
correctly.

Since `d_H(x)=1`, any `Z`-rooted `K_4` model in `H` can be made disjoint
from `x`: a branch set containing the non-root `x` also contains its unique
neighbour, so `x` is a removable leaf of that branch set.  Therefore the
absence of the required model in `H-x` is equivalent to its absence in
`H`.

Fabila-Monroy--Wood Theorem 15 then places `H` in a spanning rooted
obstruction.  All four nominated roots lie in its planar skeleton.  If a
vertex of `C` lay in an added clique behind a facial triangle `T`, a
component `Y` of the `C`-vertices of that clique would satisfy

```text
N_G(Y)=N_H(Y) subseteq T union {x},
```

contradicting `|N_G(Y)|>=5`.  Thus `H-x` is a spanning subgraph of a planar
skeleton and is planar.  Since `x` is a leaf, for `c=|C|>=4`,

```text
|E(H)| <= 3(c+4)-6+1 = 3c+7,
delta(C) <= 7-c <= 3.
```

This contradicts `delta(C)>=4`.  The use of Fabila-Monroy--Wood is within
the exact scope of their Theorem 15; no finite obstruction class is being
promoted to an unbounded conclusion.

## 4. Small lobes and terminal model

For `c=1,2`, the independent boundary and the unique neighbour of `x`
give excess at most two.  For `c=3`, excess at least four forces all
sixteen allowable edges: `C` is a triangle and every member of `Z` is
complete to `C`.  Three root--triangle pairs and the fourth root singleton
are an explicit `Z`-rooted `K_4` model in `H-x`.

Finally, with three other components `D_1,D_2,D_3`, the seven branch sets

```text
R_1,R_2,R_3,R_4, {x} union D_1, D_2, D_3
```

are disjoint and connected.  Every pair is adjacent except possibly
`D_2,D_3`, so they form a `K_7^-` model.  The root-avoidance condition is
what makes this final list valid.

The global excess identity gives a component with `delta(C)>=4`, because
four integer excesses sum to at least thirteen.  The preceding argument
therefore eliminates the entire four-component case.

## 5. Trust boundary and scope

The proof depends only on the two cited written theorems of Mader and
Fabila-Monroy--Wood.  The former four-vertex enumeration is not a logical
dependency of this revision and should not be cited as one.
