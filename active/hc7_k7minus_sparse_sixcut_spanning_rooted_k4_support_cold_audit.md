# Cold audit: spanning rooted-`K_4` support and exact-six portals

**Audit status:** GREEN.

**Source audited:**
[`hc7_k7minus_sparse_sixcut_spanning_rooted_k4_support.md`](hc7_k7minus_sparse_sixcut_spanning_rooted_k4_support.md),
SHA-256

```text
ce3dca735b31b20e210ec3c88c7a5ab194968f3405ebaabb5664d246489088ab
```

This audit checks only Lemmas 1--3 and the stated limitation.  It does not
infer a density bound from the two-bag support conclusion.

## 1. Spanning normalisation

Because `G` is six-connected and `S` is a six-cut, every component of
`G-S`, including `C`, has all of `S` as its neighbourhood.  Thus the neighbour
used in the initially degenerate case exists.  Once the model meets `C`, every
component of `C-(M intersect C)` has an edge to `M intersect C`: otherwise
connectedness of `G[C]` would fail.  Absorbing an entire such component into a
bag it meets preserves connectedness, disjointness, its old root, and all old
inter-bag adjacencies.  Lemma 1 follows.

## 2. Omitted-root support

The four old bags form a clique quotient.  If `p` meets at least three of
them, its singleton bag is nonadjacent to at most one old bag, so the five bags
form a `K_5^-` model rooted at `Z union {p}` and confined away from `q`.
The symmetric argument applies to `q`.  No fan or internally disjoint paths
are required.  Lemma 2 is correct.

## 3. Portal calculation

Fix a component `L` of `R-{p}`.  An edge from `L` to another vertex of
`C-(M union R)` would put that vertex in the same component of `J-M` as `p`.
An edge to another component of `R-{p}` would merge those two components.
All four vertices of `Z` lie in `M`, `q` is the only boundary vertex omitted
from `J`, and `C` has no edge to another component of `G-S`.  Consequently

```text
N_G(L) subseteq A_R union {p,q}.
```

There is another component of `G-S`, giving a vertex outside the closed shore
of `L`; hence six-connectivity applies.  The displayed right-hand side has at
most six vertices, so equality is forced.  In particular `|A_R|=4`, and every
component `L` sees every portal and both omitted roots.  This verifies all
three assertions of Lemma 3, including the fact that the portals are actual
neighbours of each individual component, not merely of their union.

Finally, the connected set `R` is a fifth bag rooted at `p`.  If its four
portals occupied three or four old bags, it would meet at least three of the
four clique bags and invoke Lemma 2's decoder.  Therefore, under punctured
model exclusion, all four portals occupy at most two old bags.

## 4. Scope verdict

The lemmas rigorously reduce a four-portal return to an exact order-six
fragment.  As the source stresses, they do not bound the size or excess of the
one or two supporting branch bags, so no packet or coefficient-four theorem
follows without an additional argument.
