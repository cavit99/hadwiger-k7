# Closing the two-triangle degree-seven neighbourhood case

**Status:** written proof, with a [separate whole-chain internal audit](hc7_two_triangle_case_closure_audit.md).
The conclusion covers both chromatic branches of this neighbourhood
case. It does not cover the other degree-seven neighbourhoods, degrees
eight and nine, or HC7.

## Structural theorem

Let `J` be a finite simple five-connected graph containing an ordinary
`K5` minor and two vertex-disjoint anticomplete literal triangles `P,Q`.
Put `T=P union Q`. Suppose every nonempty set `X subseteq V(J)-T`
has at least six distinct neighbours outside `X` in `J`.

Then either:

1. `J` has a `K5` model whose five branch sets each meet `T`; or
2. `J-z` is planar for some `z outside T`.

## Proof and exact dependencies

Assume neither conclusion holds. The
[extremal prism theorem](hc7_two_triangle_extremal_prism.md)
applies: four-connectivity follows from five-connectivity, the ordinary
`K5` minor is assumed, and the first alternative is excluded. It gives
the exact partition `V(J)=E dotunion S`, where `E` is connected and
`S=J-E` is an induced prism subdivision with literal caps `P,Q` and
three nontrivial rails `R_i=p_i...q_i`.

Every cap root has at least two neighbours in `E`: its degree in `J`
is at least five and exactly three neighbours lie in the prism. Every
rail-interior vertex has at least four `E` neighbours, by the
six-neighbour hypothesis applied to its singleton. Likewise every
vertex of `E` has degree at least six in `J`. In particular `|E|>=4`.

For each `i`, a `K4` model in `H_i=J-V(R_i)` rooted at the four
surviving cap vertices would extend with fifth bag `R_i` to the first
alternative. The ordered web descriptions and their external input are
therefore applicable exactly as in the
[path-cell proof](hc7_two_triangle_web_path_cells.md).
That proof gives the second alternative if a cell meets a surviving
rail. All three fixed webs are consequently clean, with their whole
cell interiors contained in `E`. The same proof shows that cell
interiors from different views are disjoint.

The [cutvertex exclusion](hc7_prism_remainder_cutvertex_exclusion.md)
now applies: `J-z` is nonplanar for every `z in E` by the excluded
second alternative. It follows that `E` has no cutvertex. Since it is
connected and has at least four vertices, it is two-connected.

The [two-connected cell exclusion](hc7_prism_two_connected_cell_exclusion.md)
then makes every actual cell empty. Thus each actual `H_i` is a planar
subgraph of its skeleton. This dependency has a
[separate internal audit](hc7_prism_two_connected_cell_exclusion_audit.md).

Write `e=|E|`, `s=|S|`, `a=e(J[E])` and `d=e_J(E,S)`. In each `H_i`,
the connected `E` lies on one side of the surviving-rail cycle; the
induced prism supplies no other edges outside it. Take that cycle as
the outer face. Summing the three disk Euler bounds gives

    3a+2d <= 9e+2s-9.

The actual degrees give `2a+d>=6e`. The six cap vertices contribute
at least twelve contacts and the `s-6` rail-interior vertices at least
four each, so `d>=4s-12`. Consequently

    3a+2d = (3/2)(2a+d)+(1/2)d >= 9e+2s-6,

a contradiction. This proves the two stated alternatives.

## Original-host consequence: both chromatic branches

Let `G` be a finite simple seven-connected graph with `chi(G)>=7`.
Suppose a vertex `u` has exactly seven neighbours,

    N_G(u)=P dotunion Q dotunion {r},

where `P,Q` are anticomplete triangles and `r` is adjacent to every
vertex of `P union Q`. Then `G` contains a `K7` minor.

To prove this, suppose otherwise and put `J=G-{u,r}`. It is
five-connected. If `J` were four-colourable, two fresh colours on
`u,r` would six-colour `G`; hence `chi(J)>=5`. Hadwiger's theorem for
`K5` supplies an ordinary `K5` minor, as in the original-host application
of the audited extremal prism theorem.

If `X` is a nonempty subset of `V(J)-T`, then `u` has no neighbour in
`X`. A `J` boundary of order at most five would give a `G` boundary
of order at most six after adding `r`, separating `X` from `u`.
Seven-connectivity excludes this. Thus the structural theorem applies.

Its first alternative supplies five disjoint connected bags in `J`,
each meeting `T`. Adjoin the two singleton bags `{u},{r}`. They are
adjacent to one another and to all five bags, because both vertices are
adjacent to every vertex of `T`. These are seven disjoint connected
bags with all required contacts, a `K7` model.

In the second alternative, `J-z` is planar for `z outside T`. The
Four Colour Theorem colours it with four colours. Give the nonadjacent
vertices `u,z` colour five and `r` colour six. This colours all of `G`,
again a contradiction. No proper-minor colouring or inherited criticality
is needed for this consequence.

In particular, a hypothetical seven-contraction-critical counterexample
to HC7 cannot have this degree-seven neighbourhood. The proof does not
assume `chi(J)=6`; it also excludes the previously separate `chi(J)=5`
branch. No assertion is made about the other neighbourhood configurations.
