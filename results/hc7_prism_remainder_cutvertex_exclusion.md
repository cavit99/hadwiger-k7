# The extremal prism remainder has no cutvertex

**Status:** written proof, with a [separate internal audit](hc7_prism_remainder_cutvertex_exclusion_audit.md).
Under the hypotheses below, this rules out every
cutvertex of the connected remainder `E`. It does not rule out a
two-separator of `E` or by itself close the entire two-triangle case.

## Hypotheses and conclusion

Retain the partition in the
[extremal prism theorem](hc7_two_triangle_extremal_prism.md):
`J-E` is the induced prism subdivision with rails `R_i=p_i...q_i`,
each having a nonempty interior `I_i`, and literal end triangles
`P={p_1,p_2,p_3}` and `Q={q_1,q_2,q_3}`. Set `T=P union Q`.
Assume that:

* `J` is five-connected and `J-z` is nonplanar for every `z in E`;
* `E` is nonempty and connected;
* `J` has no `T`-meeting `K5` model;
* every nonempty subset of `V(J)-T` has at least six actual neighbours;
* each root has at least two neighbours in `E`, and each internal rail
  vertex has at least four neighbours in `E`.

**Theorem.** The graph `J[E]` has no cutvertex.

For each `i`, let `H_i=J-V(R_i)`. Fix the three ordered web completions
from the [path-cell theorem](hc7_two_triangle_web_path_cells.md).
A rooted `K4` in `H_i` would extend by the actual fifth bag `R_i` to
a `T`-meeting `K5`. In particular, two vertex-disjoint paths joining
opposite pairs of the four roots on the surviving-rail cycle are
forbidden. Every edge used in such a linkage below is actual.

The path-cell theorem and the nonplanarity of every `J-z` imply that
all three fixed webs are clean: their whole cell interiors are subsets
of `E`, and all surviving rail vertices lie in the planar skeleton. Whole cell
interiors from distinct views are disjoint, by the theorem's
cross-view restriction. No compatibility of the three embeddings
is assumed.

## A consequence for arbitrary shores containing a rail interior

We first make explicit the following consequence of the written
path-cell proof. It is used below for a newly constructed shore,
not for an original web cell.

**Shore consequence.** If a nonempty connected root-free set
`X subseteq V(H_i)` meets a surviving rail interior and has
`|N_{H_i}(X)|<=3`, then `J-z` is planar for some `z in E`.
Consequently no such `X` exists under the present hypotheses.

Here is why the earlier proof applies with exactly this premise.
Its section “Actual shores and their path ownership” starts with an
arbitrary connected root-free set with at most three actual gates.
It proves that `X=W union I_j`, with `N_E(W)={z}`, that `W` owns
all `E`-neighbours of both endpoints of `R_j`, and that `W` misses
the third rail `R_k`. Each component of `W` meets `I_j`.

The section “At most one view has a cell meeting a path” constructs
the complementary shore containing `I_k` with gates `{p_k,q_k,z}`.
That construction only uses the just-proved properties of `X`.
The duplicate-ownership and mutual-ownership arguments then force
the two other fixed web completions to be clean; they do not
require `X` itself to have been a cell. Finally the planar gluing
section uses those two clean completions and the complementary
actual shores to construct all of `J-z`. These are precisely the
inputs already obtained here. This contradicts the assumed
nonplanarity of `J-z`.

Thus this consequence follows from the existing argument with no
containment claim about `X` inside a web cell and no new completion
or criticality assumption.

## No component at a cutvertex can contact only one rail

Suppose `z` is a cutvertex of `E`, and let `W` be a component of
`E-z` whose prism contacts all lie on one rail `R_i`. Set `A=E-W`.
Then `A` is connected and contains `z`, and `N_E(W)={z}`.
The six-neighbour bound ensures that `W` has at least five distinct
neighbours on `R_i`. Let `a,b` be the first and last such neighbours
in its order from `p_i` to `q_i`.

All of `W` lies in the skeleton of each alternate view `H_j`,
`j!=i`. Indeed, if a whole cell `C` met `W`, then the nonempty
root-free set `C intersection W` would have actual `J`-boundary
contained in

    N_{H_j}(C) union {z}.

There are no contacts to the deleted rail `R_j`, because `W`
contacts only `R_i`. This boundary has at most four vertices,
contradicting the six-neighbour bound. Cross-view disjointness of
whole cells also ensures that `z` is visible in at least one of
these two alternate skeletons. Choose such a view `H_j`; write
`R_k` for its other surviving rail.

We describe precisely the auxiliary drawing used in this skeleton.
Project an actual path in `E` by replacing every maximal portion
inside a cell with the corresponding face edge between its two
actual `E`-gate endpoints. A portion with equal endpoints may be
discarded. Since `E` is connected and has visible vertices, every
actual component of `E` inside a cell has an `E` gate. These
projections yield a connected planar auxiliary graph on all visible
`E` vertices, using only actual skeleton edges and triangular-face
edges between `E` gates. It is disjoint from the actual cycle

    D=R_i union R_k union {p_i p_k,q_i q_k}.

Therefore the whole auxiliary graph lies on one side of `D`.
Regard that side as a disk. Every used auxiliary edge between
`E` vertices lies in that disk as well.

The same projection restricted to paths of connected `A` gives a
connected auxiliary subgraph on its visible vertices, containing
`z` and disjoint from `W`. To check this restriction, every actual
component of `A` inside a cell has an `A` gate: a path in `A` to
the visible vertex `z` must first exit the cell at such a gate.
Moreover a hidden `A` vertex has no neighbour in `W`, since every
edge from `W` to `A` ends at the visible vertex `z`.

Every actual contact from `A` to a surviving rail can also be
represented in this drawing. A visible `A` endpoint gives its
actual skeleton edge. For a hidden endpoint in a cell, take a path
inside its actual `A` component to an `A` gate `h`; the rail
endpoint `t` is another gate of the same cell. The face edge `ht`
represents the contact. It avoids `W`, and except for its rail
endpoint it stays on the common `E` side of `D`. These edges are
auxiliary drawing edges only, not asserted actual contacts or
minor-model edges.

Every vertex of `R_k` has an `A` neighbour, since `W` has no such
contacts. The projected `A` subgraph consequently reaches `R_k`.
On the other hand, connected `W` supplies a simple actual
`a`--`b` path with all internal vertices in `W`. In the disk on
the `E` side of `D`, this arc and the boundary interval `R_i[a,b]`
bound a pocket not containing `R_k`. The projected connected `A`
subgraph avoids the arc and reaches `R_k`, so lies outside that
pocket. It cannot have a represented contact at a vertex of the
open interval `R_i(a,b)`: such an edge would have to approach from
inside the pocket, or cross the arc. In particular no actual
vertex of `R_i(a,b)` has an `A` neighbour.

The nonempty root-free set

    W union V(R_i(a,b))

now has actual `J`-boundary contained in `{z,a,b}`. Inducedness of
the prism excludes other rail exits, and the extreme choice of
`a,b` contains every `W` contact. This contradicts the
six-neighbour bound. Thus every component of `E-z` contacts at
least two rails. A component contacting no rail is already
excluded by its actual boundary `{z}`.

## Ordering a component against its entire complement

Continue to suppose `z` is a cutvertex. Fix a component `W` of
`E-z` and let `A=E-W`. Both are connected and disjoint. For a rail
`R_h`, write `W_h=N_J(W) intersection V(R_h)` and
`A_h=N_J(A) intersection V(R_h)`. Every rail vertex has an
`E` neighbour, so

    W_h union A_h = V(R_h).

If `W` and `A` both contact distinct rails `R_i,R_j`, the following
opposed inequalities are impossible:

    w_i < a_i on R_i,       a_j < w_j on R_j,
    w_i in W_i, a_i in A_i, a_j in A_j, w_j in W_j.

They give disjoint opposite-corner paths in `H_k`: follow
`p_i R_i w_i`, cross connected `W` to `w_j`, and follow `R_j`
to `q_j`; the other path follows `p_j R_j a_j`, crosses connected
`A` to `a_i`, and follows `R_i` to `q_i`. Strict inequalities
separate the rail portions, while `W` and `A` separate their
internal portions.

On a rail contacted by both parts, at least one strict comparison
exists, since their union is the whole rail and that rail has at
least three vertices. If both directions of strict comparison
occurred on one common rail, neither direction could occur on any
other common rail, by the forbidden pair just proved. That would
force the contact union on the other rail to consist of a single
vertex, a contradiction. Thus, whenever there are at least two
common rails, the contacts on each are separated and have the
same orientation on all common rails:

    every W contact <= every A contact,

or all the reverse inequalities. Equality at their common
boundary vertex is allowed. This conclusion uses `A=E-W`, not
just an individually selected second component of `E-z`.

## Excluding the remaining cutvertex configurations

First suppose a component `W` contacts exactly two rails
`R_i,R_j`, and misses `R_k`. If `A` misses either of those two
rails, say `R_j`, then `W` owns every `E` neighbour of `R_j`.
The actual set `X=W union I_j` is connected and root-free in
`H_i`, with actual boundary contained in `{p_j,q_j,z}`. The
shore consequence above contradicts the nonplanarity of every `J-z`.

Otherwise `W` and `A` both contact `R_i,R_j`, so they have the
consistent order just proved. Suppose `W` precedes `A`; for each
`h in {i,j}` let `b_h` be the last `W` contact on `R_h`. Every
rail vertex strictly before `b_h` has all of its `E` neighbours
in `W`, because every `A` contact is at or after `b_h`. Form

    U = W union V(R_i[p_i,b_i)) union V(R_j[p_j,b_j)).

The actual external boundary is contained in

    {z,b_i,b_j,p_k}.

Indeed `W` has no third-rail contact and only `z` as an external
`E` neighbour; the two prefixes have no `A` contacts and exit
their rails only at `b_i,b_j`; their only remaining cap exits
are to `p_k`. Prefixes of length zero cause no difficulty. The
set `U` is nonempty, and `q_k` is outside both `U` and its displayed
boundary. Deleting at most four vertices therefore separates `J`,
contrary to five-connectivity. If `A` precedes `W`, use suffixes
strictly after the first `W` contacts and the boundary vertex
`q_k` instead. This excludes every component with exactly two
rail types.

Every component of `E-z` consequently contacts all three rails.
Since `z` is a cutvertex, there is another such component; hence
for any chosen `W` its complement `A` contacts all three rails
as well. Their contacts have the same order on all three rails.
If `W` precedes `A`, let `b_h` be the last `W` contact on each
`R_h` and take

    U = W union the three prefixes R_h[p_h,b_h).

Now

    N_J(U) subseteq {z,b_1,b_2,b_3}.

Any end-triangle edge leaving a selected prefix ends at one of
these `b_h` when that other prefix is empty; otherwise it stays
inside `U`. No `q_h` belongs to a strict prefix. A vertex of the
other component of `E-z` is outside `U` and the displayed boundary,
so this again contradicts five-connectivity. Reversing the order
gives the identical argument with three suffixes. Every possible
cutvertex configuration has been excluded, proving the theorem.

No quotient is used, no criticality is inherited, and no completion
edge enters an actual separator or rooted minor model.
