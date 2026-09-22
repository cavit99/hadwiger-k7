# Three web views of the extremal prism

**Status:** written proof, with a [separate internal audit](hc7_two_triangle_web_path_cells_audit.md).
The theorem below closes the branch in which a web cell contains an internal
vertex of a surviving prism path. The branch in which all three web views
have only cells contained in `E` remains open. No closure of the whole
six-chromatic two-triangle case or of HC7 is claimed.

## Hypotheses and conclusion

Let `J` have the partition from the
[extremal prism theorem](hc7_two_triangle_extremal_prism.md):
`J-E` is an induced prism subdivision with disjoint paths
`R_i=p_i...q_i`, each with nonempty interior `I_i`; its literal end
triangles are `P={p_1,p_2,p_3}` and `Q={q_1,q_2,q_3}`. The set `E` is
nonempty and connected. Put `T=P union Q`. Assume:

- `J` has no `T`-meeting `K5` model;
- every nonempty subset of `V(J)-T` has at least six actual neighbours;
- each root has at least two neighbours in `E`, and each internal path
  vertex has at least four neighbours in `E`.

**Theorem.** In the web descriptions specified next, if any cell
contains an internal vertex of a surviving path, then `J-z` is planar
for some `z in E`. In particular `chi(J)<=5`.

This excludes that entire branch of the selected original-host case
`chi(J)=6`. It also contradicts the stronger original-host condition
`chi(J-z)>=5` recorded in
[Section 5 of the construction frontier](../active/hc7_degree7_exceptional_construction_working.md#5-direct-prism-construction-remaining-gap).
No criticality is transferred to a quotient.

For `{i,j,k}={1,2,3}`, put `H_i=J-V(R_i)`. Its cycle consisting of
`R_j,R_k,p_jp_k,q_jq_k` has the root order `p_j,p_k,q_k,q_j`.
A rooted `K4` in `H_i` finishes with the fifth bag `R_i`. Therefore
Fabila-Monroy--Wood, *Rooted K4-Minors*,
[Lemmas 2 and 7](https://arxiv.org/html/1102.3760v1), give an ordered web
completion of `H_i`. Fix one such completion for each `i`.

A web consists of an embedded planar skeleton with the four nominated
roots, in the specified order, on its outer quadrilateral. For each
triangular inner face there is a disjoint cell, whose vertices have no
neighbours outside that cell and the three face vertices. The completion
may add edges. Throughout, an **actual cell component** means a connected
component of the subgraph of `H_i` induced by one cell's vertices. Its
actual boundary `B_X=N_{H_i}(X)` has size at most three and lies in the
skeleton. None of the arguments below treats a completion edge as actual.

## Actual shores and their path ownership

The next statements apply to any nonempty connected root-free set
`X subseteq V(H_i)` with `|N_{H_i}(X)|<=3`, including actual cell
components. Thus they remain applicable to newly constructed shores.

Such an `X` cannot meet both surviving path interiors: a nonempty subset
of either interior has at least two boundary vertices on that path, and
the two paths are disjoint. If `X` meets a surviving path, say `R_j`, it
has the exact form

    X = W union R_j(s,t),        N_{H_i}(X) = {s,t,z},
    W subseteq E,               N_E(W) = {z},

where `R_j(s,t)` is one nonempty open interval and `z in E-W`.
Indeed `W` is nonempty, since every internal path vertex has four actual
`E` neighbours. It is proper: if `E subseteq X`, all four surviving roots
would be boundary vertices. Connectivity of `E` now supplies at least
one `E` boundary vertex. At most two gates remain on `R_j`, forcing a
single interval. Every component of `E[W]` contacts that interval,
because `X` is connected. Also `W` is a union of components of `E-z`;
consequently `A=E-W` is connected and contains `z`.

**Full path ownership.** For this shore, necessarily

    s=p_j,  t=q_j,  X=W union I_j,
    N_E(p_j) union N_E(q_j) subseteq W.

Here is the actual third-view argument. The six-neighbour condition gives
at least three distinct contacts of `X` on deleted path `R_i`; only `W`
can have these contacts. Let `a,b` be their first and last vertices, in
the order from `p_i`.

If `A` contacts `p_j` and has a neighbour `v` on `R_i` strictly after
`a`, there are disjoint paths in `H_k`: one follows `p_i R_i a`, enters
`W`, follows `X` to its `R_j` interval, and then follows `R_j` to `q_j`;
the other goes from `p_j` into connected `A`, reaches `v`, and follows
`R_i` to `q_i`. These are the two forbidden diagonals in the four-root
order. All paths use actual edges; their disjointness follows from
`A disjoint X`, the two surviving paths being disjoint, and `a<v`.
Thus an `A` contact at `p_j` forbids every such `v`. Symmetrically an
`A` contact at `q_j` forbids `A` contacts on `R_i` strictly before `b`.

If either endpoint has an `A` neighbour, the whole open interval
`R_i(a,b)` therefore has no `A` neighbour. Adjoining it to `X` gives a
nonempty root-free set whose actual boundary is contained in
`{s,t,z,a,b}`, a contradiction. Both endpoint neighbour sets consequently
lie in `W`. They are nonempty, so `p_j,q_j` must themselves be the two
path gates `s,t`. This proves full ownership. In particular `W` has no
contact at all with `R_k`, and `N_E(I_j) subseteq W union {z}`.

## Cross-view restrictions

**Cells contained in E are disjoint across views.** More generally, let
nonempty `C,D subseteq E` satisfy `|B_C|,|B_D|<=3`, where
`B_C=N_{H_i}(C)` and `B_D=N_{H_j}(D)`, with `i!=j`. Then `C` and `D`
are disjoint.

For otherwise `N_J(C intersection D) subseteq B_C union B_D`.
The six-neighbour condition forces two disjoint triples, every member
of which actually neighbours the intersection. It follows that
`B_C subseteq D union V(R_j)` and `B_D subseteq C union V(R_i)`:
a gate outside the other shore and its deleted path would belong to
both triples. Thus `N_E(C union D)` is empty. Connectivity gives
`E=C union D`, but neither shore can contact the remaining path `R_k`,
a contradiction.

**The same path cannot be owned from two views.** Suppose shores in
`H_i,H_k` both own `R_j`, with `E` parts `W,W'` and gates `z,z'`.
Their intersection contains `I_j` and has actual boundary contained in
`{p_j,q_j,z,z'}`. The two deleted paths cannot contribute: each is
absent from one shore and is forbidden as the third path by the other.
This contradicts the six-neighbour condition.

**Mutual ownership is impossible.** Suppose a shore in `H_i` owns
`R_j`, with `E` part `W` and gate `z`, and one in `H_j` owns `R_i`,
with `E` part `V` and gate `w`.

If `W intersection V` is nonempty, their union has at most one external
`E` neighbour. To see this, if `z!=w` and `z notin V`, a path inside
`W union {z}` from the intersection to `z` must first leave `V` at `w`,
so `w in W`; the case `z=w` is immediate. Now
`W union V union I_i union I_j` has boundary contained in the four
end roots and that one external `E` neighbour, a contradiction.

If the `E` parts are disjoint, `W` has at least three contacts on `R_i`.
None is an endpoint, whose `E` neighbours are all in `V`. Since every
`E` neighbour of `I_i` lies in `V union {w}`, it follows that `w in W`.
Likewise `z in V`. Their union has no external `E` neighbour, hence is
all of `E`, contradicting the absence of contacts with the third path.

**At most one view has a cell meeting a path.** Suppose `H_i` has the
shore `W union I_j` with gate `z`. In

    J[(E-W-{z}) union I_k]

take the connected component `Y` containing `I_k`. Its actual boundary
in `H_i` is contained in `{p_k,q_k,z}`. Indeed `W` has no `R_k`
contact, its `E` boundary is just `z`, and every neighbour of `R_j`
outside that path lies in `W union {z}`. The shore theorem gives
`Y=V union I_k`, with the same gate `z`, owning both endpoints of
`R_k`. In any other view a cell meeting a path would either duplicate
one of these two owned paths or give mutual ownership. Both are
impossible by the preceding paragraphs. Hence the other two fixed web
completions have every cell contained in `E`.

## Planar gluing in the branch with a path in a cell

Retain the complementary shores just constructed, and write

    E-{z} = W_j disjoint union W_k disjoint union N.

Here `W_j=W` owns `R_j`, `W_k=V` owns `R_k`, and `N` consists of the
remaining components of `E-z`. The parts `W_j,W_k` have no contacts
with `R_k,R_j`, respectively; `N` contacts neither of those paths.
Every component in `W_j` contacts `I_j`, and every component in `W_k`
contacts `I_k`. These facts follow from connectedness of the two shores.
Every component of `E-z` has a neighbour at `z`.

In clean view `H_j`, all vertices of `W_k union N` belong to the planar
skeleton. For if a cell component `C` met this set in a nonempty set
`D`, then

    N_J(D) subseteq N_{H_j}(C) union {z},

because `W_k union N` has no contact with the deleted path `R_j` and
has `E` boundary contained in `{z}`. This gives at most four actual
neighbours. Similarly `W_j union N` lies in the skeleton of `H_k`.
All vertices of the two surviving paths lie in the skeleton in each
clean view. Finally `z` lies in at least one of these two skeletons,
because otherwise it lies in two `E`-only cell components, contradicting
cross-view disjointness. Interchange `j,k` if necessary so that it lies
in the skeleton of `H_j`.

Consider in that skeleton the actual subgraph on

    R_i union R_k union W_k union N union {z}.

The off-path set `K=W_k union N union {z}` is connected and contacts
the interior `I_k`. The outer skeleton quadrilateral is
`p_i,p_k,q_k,q_i`. Its edge `p_iq_i` is a completion edge, since the
original end triangles are anticomplete. The actual induced path `R_i`
is a simple arc between its two outer endpoints with all internal
vertices in the interior of this disk. The arc cuts off a pocket next
to the outer edge `p_iq_i`, containing none of `R_k`. Since `K` is
connected, avoids `R_i`, and contacts `I_k`, it cannot have a vertex in
that pocket. Thus the actual patch has no vertex or edge in the pocket.
Omitting the artificial outer edge exposes the whole `R_i` on its
outer face, while `p_k,q_k` retain their outer order. Delete `z`.

In the skeleton of `H_k`, take the actual subgraph on

    R_i union R_j union W_j.

Every component of its off-path set `W_j` contacts `I_j`, so the same
pocket argument applies to each component separately. It gives a disk
embedding with all of `R_i` on one boundary arc and `p_j,q_j` on the
other outer side in the order inherited from the web.

Glue these two disk drawings along their identical actual path `R_i`,
with their interiors on opposite sides. They otherwise have disjoint
vertex sets and together contain every vertex and edge of `J-z`
except `p_jp_k` and `q_jq_k`: there are no edges between different
components of `E-z`, the forbidden path contacts were proved above,
and the original prism is induced. The inherited outer root orders
allow those last two cap edges to be drawn in the outer endpoint
regions, one at the `p_i` end and the other at the `q_i` end, without
crossing. This constructs a planar embedding of all of `J-z`.

No completion edge is part of this final graph or a minor model.
The Four Colour Theorem now gives `chi(J)<=5`.

## Exact remaining all-clean obstruction

When no view has a cell meeting a surviving path, the cross-view
disjointness above remains available. It does not make the three
skeletons compatible, and it does not by itself make the actual graphs
`H_i` planar. An actual planar cell together with its three gates cannot
automatically be inserted into the original skeleton face: the gates
must be cofacial. Completing the gate triangle can destroy planarity.
This is the first unresolved step of the attempted all-clean extension,
including the proposed extension under two-connectivity of `E`.

There is a short conditional whole-prism test. If all three **actual**
graphs `H_i` were planar, write `e=|E|`, `r_i=|R_i|`, `s=sum r_i`,
`a=|E(J[E])|`, and `d_i=|E_J(E,R_i)|`, with `d=sum d_i`.
The connected off-cycle set `E` lies on one side of each surviving-path
cycle, so that cycle can bound the outside face. Disk Euler gives

    a+d_j+d_k <= 3e+r_j+r_k-3,
    3a+2d <= 9e+2s-9.

But actual degree and contact bounds give `2a+d>=6e` and
`d>=4(s-6)+12=4s-12`, hence `3a+2d>=9e+2s-6`, a contradiction.
The algebra does not establish its missing planarity premise. Nor does
five-colourability of separate `H_i` supply a colouring extension over
the deleted path: its attachments to a cell remain unbounded.
