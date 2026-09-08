# Three-connectivity after removing the degree-eight vertex and its cycle

**Status:** written proof; the adjacent audits record their separate internal
verdicts at the exact source hash. This closes a separator case inside the
cycle-and-triangle configuration, not that whole configuration or Conjecture 19.

All graphs are finite and simple. Let `Q=K_7-2K_2`, with the two deleted
edges independent. Suppose `G` is seven-connected, has minimum degree at
least eight, and has no `Q` minor. Let `v` have degree eight, with
`N_G(v)=C union A`, where `C` is a five-cycle and `A` a disjoint triangle,
and at most one edge joins `C` to `A`. Put `B=G-N[v]` and
`J=G-v-C=B union A`.

**Theorem.** The graph `J` is three-connected.

We use the following written proofs with adjacent internal audits:

- [Cycle exterior theorem](../results/hc7_degree8_cycle_exterior.md),
  SHA-256 `6c5196ea71f77a1426d8bc24ef040e7fe85805ac0cb784d2d62d152a67303eb3`:
  `B` is nonempty and connected, and every vertex of `B` has at most two
  neighbours on `C`, consecutive when there are two.
- [Designated five-root almost-clique theorem](../results/hc7_five_root_almost_clique.md),
  SHA-256 `de183e350c412739c05a744e811304454ba90856efee9e097813c70617bba9cd`:
  five roots containing a designated triangle, nonroot degree at least
  seven and every nonempty nonroot-set boundary at least five give five
  rooted bags with only one possible missing contact, incident with any
  designated triangle root and one of the two other roots.

## 1. The exact two-cut sides

Deleting six vertices from `G` shows that `J` is connected. If `x` were
a cutvertex, the triangle makes `A-{x}` lie in one component of `J-x`.
Any other component `X` contains no `A` vertex and has original boundary
in `C union {x}`, of order at most six. The vertex `v` survives outside
that boundary, contradicting seven-connectivity. Thus `J` is two-connected.

Suppose that `T={t_1,t_2}` is a two-cut of `J`. The nonempty set `A-T`
lies in a single component `K` of `J-T`. Every other component `L` is a
subset of `B`, with original neighbourhood contained in `C union T`.
Seven-connectivity makes this neighbourhood exactly `C union T`.
These seven vertices form a cut of `G`, whose component containing `v`
is `K union {v}`. Every component of `G-(C union T)` contacts every
vertex of the cut: a missed vertex would reduce its actual boundary
to at most six while another component survives.

There is exactly one component other than `K`. Otherwise choose two,
`L_1,L_2`. The three disjoint connected bags

```text
L_1 union {t_1},   L_2 union {t_2},   K union {v}
```

are pairwise adjacent and each contacts all of `C`. Contract one cycle
edge; the three bags and the four resulting cycle bags give
`K_3 join C_4=Q`. Hence write `L` for the sole other component.

## 2. A simultaneous allocation on the triangle side

We claim there are pairwise disjoint connected subsets of `K` consisting of:

- a set `D` containing one vertex of `A-T` and contacting two distinct
  vertices of `C`;
- for each `t in T-A`, a set `U_t` containing a different vertex of
  `A-T` and a neighbour of `t`.

In particular, all the used triangle roots are distinct.

Put `k=|T-A|`, so `k` is zero, one or two and `|A-T|=k+1`.
Work in `G[K union C union (T-A)]`, with sink-terminal set
`S=C union (T-A)`. Give each vertex of `A-T` capacity two and every
other vertex capacity one. Add a source adjacent to `A-T` and a sink
adjacent to `S`; terminal vertices may only be path endpoints. The usual
vertex-splitting network implements these capacities.

There is an integral flow of value `2k+2`. Indeed, a vertex separator
of weighted cost at most `2k+1` leaves a source root, since removing all
`k+1` costs `2k+2`. Its reachable side `X` contains that root and no
terminal. All original neighbours of `X` lie in the separator together
with `{v} union (T cap A)`. Their actual number is at most

```text
(2k+1) + 1 + (2-k) = k+4 <= 6.
```

The component `L` survives outside this boundary, contradicting
seven-connectivity. Removing all source roots costs `2k+2`, giving the
matching upper bound.

Every vertex of `T-A` can be required as an endpoint. For `k=2`,
two-connectivity of `J` supplies two vertex-disjoint `A`--`T` paths
with distinct endpoints. Stop them at their first `T` vertices and
retain their suffixes after the last `A` vertices; the interiors lie
in `K-A`. For `k=1`, the component `K union {v}` contacts the sole
`t in T-A`, and `v` does not contact `t in B`. Connectedness of `K`
therefore gives a path from `A-T` to `t`, again starting at its last
source root. For `k=0` there is no prescribed terminal.

Initialize the flow with these `k` paths, and augment to value `2k+2`.
A simple residual source--sink augmenting path never uses a reverse
terminal--sink arc, since it stops on reaching the sink. Thus the
prescribed terminal arcs stay saturated. This preserves the endpoints,
not necessarily the initial paths themselves.

Decompose the final integral flow into `2k+2` paths. They end at distinct
vertices of `S`, including all of `T-A`. Exactly two start at each source
root: all source capacities are saturated, so no path uses another source
root internally. Apart from their source roots, the paths are disjoint.
If the `k` prescribed-terminal paths start at different source roots,
one remaining source starts two `C` paths. The terminal paths with their
`T-A` endpoints removed give the `U_t`; the two `C` paths with their
endpoints removed give `D`. This always applies for `k=0,1`.

The only remaining case has `k=2` and both `T` paths starting at `a_1`.
Let `X` be their union with `a_1` removed. Let `Y` be the union of the four
paths from `a_2,a_3`,
with their `C` endpoints removed. Both sets lie in `J-a_1`. This graph
is connected, so there is an `X`--`Y` path `R` whose interior avoids both
sets. The interior of `R` consequently avoids all six chosen paths.
It cannot enter a different component of `J-T`: to do so from `K`
or to return would meet `T subseteq X` internally. Thus `R` lies in
`K union T`.

Suppose its `Y` endpoint lies on a path from `a_2`. Follow that path
from `a_2` to the endpoint, then `R`, then the suffix of the `T` path
containing the other endpoint. This is a new `a_2`--`T` path. Retain the
other `a_1`--`T` path and the two `a_3`--`C` paths. They are disjoint
except for the shared endpoint `a_3` of the last pair: the old six paths
were disjoint outside their source roots and `R` avoids all their interiors.
Their portions in `K` give `U_{t_1},U_{t_2},D`. The case of an endpoint
in the `a_3` family is identical with those two labels exchanged.

## 3. Completing the minor on the opposite side

Choose two disjoint edges of `C` whose contraction leaves the two selected
`D` contacts in different cycle bags. This is always possible on a
five-cycle: nonadjacent vertices cannot merge under a matching, and if
the selected pair is adjacent choose a matching avoiding their edge.
The three resulting cycle roots form a triangle. Designate one of the
two roots contacted by `D` as `z`.

Apply these two contractions in `G[L union C union T]`. Its five roots
are the three cycle roots and the two `T` roots. Every nonempty subset
of `L` had its full original boundary, at least seven, so after the
two contractions it still has boundary at least five. Every vertex of
`L` had its original degree, at least eight. It loses at most one
neighbour: its at most two cycle neighbours are consecutive, so they can
merge in at most one of the two disjoint cycle edges. Thus every nonroot
has degree at least seven.

The designated almost-clique theorem supplies the five rooted bags with
only a possible missing pair `z--t_i`. Lift the three cycle roots through
the two fixed disjoint edges. For each `t in T-A`, adjoin `U_t` to its
root bag through the selected neighbour of `t`. These sets lie in `K`
and are disjoint from the entire model on `L union C union T` and from
`D`; the two `T` roots remain distinct.

Every `T` bag now contains an `A` vertex. The unused bag `D` contains a
different `A` vertex, so it contacts both `T` bags by the literal triangle.
It contacts at least two cycle bags, including `z`. The singleton `{v}`
contacts all five root bags and `D`. Hence the only possibly absent
contacts among these seven connected disjoint bags are `z--t_i` and
`D--h`, where `h` is the possible cycle root missed by `D`. Since `h!=z`,
these two pairs are independent. This is a `Q` minor, a contradiction.

All two-cuts are excluded. Since `J` is two-connected and has at least four
vertices, it is three-connected. Every reduction above uses specified
disjoint contraction preimages in the fixed host. There is no induction
on a quotient, and no claim that such a quotient preserves chromatic
criticality or seven-connectivity. QED

The remaining cycle-case obligation is still global: the two helpers
obtained after a cycle-edge contraction must simultaneously contact all
four cycle bags and place triangle vertices on both sides. Three-connectivity
of `J` does not yet prove that partition exists.
