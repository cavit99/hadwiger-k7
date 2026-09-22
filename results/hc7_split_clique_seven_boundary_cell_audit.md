# Audit: four path contacts and a seven-vertex boundary

**Verdict: GREEN** for the stated intermediate family theorem. This separate
internal audit is an independent proof reconstruction, not external
peer review. No unsupported inference was found in the pinned proof.

Audited source: [the cell theorem](hc7_split_clique_seven_boundary_cell.md).

- Audit date: 2026-09-22.
- Current SHA-256: `3566ff81ee491ecaf13ab4ce2ee89583922666b96df2b9be968bec3bb7195cd9`.
- Method: direct reconstruction of the separator and minor-model arguments;
  no finite search or computational certificate is used.

The independently reconstructed source originally had SHA-256
`b66251018f085068bed196b8adeeeb982dba0199ef0b10527e8f08f77d83b1ed`.
After promotion to `results/`, only its opening status paragraph changed
to link this audit. Reversing exactly that paragraph reproduces the
original hash; the mathematical text is unchanged. The GREEN verdict
therefore applies to the current pin above.

## Statement and quantifiers checked

The graph is finite, simple and seven-connected. The five vertices of
`K` form a literal clique. The nonempty connected set `X` avoids `K`,
and its entire external neighbourhood is exactly the seven distinct
vertices `S=T dotunion {f1,f2,f3,f4}`, with `|T|=3`. The path `F` avoids
`X union T`, contains the four contacts in the stated order, and has
exactly one vertex `q` in `K`. No vertex of `X` sees both extreme
contacts. The neighbourhood independence inequality is assumed for
every original vertex of `X`.

The first conclusion assumes `d_S(x)>=5` for every `x in X`. The second
replaces this assumption by triangle-freeness of `G[X]`; all preceding
hypotheses remain in force. The proof permits `T intersect K` and permits
`q` to be one of the path contacts. It neither assumes that the boundary
avoids `K` nor passes the independence inequality to a quotient.

## Exterior five-root linkage

Fix either pair of selected path contacts and let `U` consist of that
pair and `T`. If the five disjoint `U`--`K` paths fail in `G-X`, set
Menger supplies a set `W` of at most four vertices separating the two
sets. This version allows separator vertices in either terminal set
and trivial paths at their intersection. In particular, every vertex
of `U intersect K` must belong to `W` under this failure assumption.

The nonempty set `K-W` lies in one component `A` because `K` is a
clique. No vertex of `U-W` lies there. For the two omitted contacts
`Z=S-U`, a vertex of `A-Z` consequently has no neighbour in `X`:
such a neighbour would put that vertex in `S`, whereas `A` avoids
`U` and the vertices of `Z` have been removed. Every other external
neighbour of `A-Z` lies in `W union Z`. This set has at most six
vertices and avoids `X`. If `A-Z` were nonempty, it would separate
that nonempty set from the nonempty set `X`, contradicting
seven-connectivity. Thus `K-W subseteq A subseteq Z subseteq V(F)`.

Since `K intersect V(F)={q}`, this forces `K-W={q}` and
`W=K-{q}`. The whole path `F` avoids this separator. Its two selected
contacts also avoid the separator, and the path connects them to `q`.
This contradicts the separation even when some other roots lie in `K`.

Truncating the resulting five disjoint paths at their first vertices
of `K` preserves their five distinct prescribed roots. Their distinct
ends exhaust `K`, whose literal edges supply every interbag contact.
Every bag avoids `X`. Omitted boundary contacts may lie in these bags;
the later construction never reserves them as additional bags.

## The two preliminary model constructions

For an edge `xy` disjoint from `K`, deleting its ends leaves a
five-connected graph. If the edge has five common neighbours, choose
five of them and link them disjointly to `K` in that graph. Intersections
of the chosen roots with `K` are harmless, as above. The resulting five
bags each see both singleton bags `x,y`; the edge `xy` joins those two
singletons. This proves the common-neighbour bound under the temporary
assumption that `G` has no `K7` minor.

For a boundary-covering edge `B` in `X` with `X-B` nonempty, take a
component `C` of `G[X-B]`. In the five-connected graph `G-B`, a
five-fan from a vertex of `C` to `K` exists. Each suffix strictly after
the last vertex of `C` is nonempty, since its end lies in `K`, disjoint
from `X`. The suffixes avoid `C` and are mutually disjoint: the fan's
only shared vertex lies in `C` and has been discarded.

Each first suffix vertex has an edge to `C` and belongs to
`N_G(C)-B subseteq S`. Boundary coverage therefore gives it an edge
to `B` as well. The five distinct ends in the literal clique give all
suffix-to-suffix contacts. Finally, `C` has an edge to `B` because
`X` is connected and `C` is a component after deleting `B`. Thus the
seven specified bags are connected, nonempty, disjoint and pairwise
adjacent. Suffixes may pass through other components of `X-B`; no later
bag in this construction owns those components.

## Normalization and final two helpers

The cases `|X|=1,2` are correctly excluded. A singleton sees all of `S`;
for two vertices, minimum degree seven gives at least six boundary
neighbours at each end of their edge, hence at least five common
neighbours. Once `|X|>=3`, every edge in `X` leaves a nonempty remainder.

If a vertex has at least six boundary neighbours, an incident edge
has boundary-neighbourhood union of size at least `6+5-4=7`, so it
covers `S` and invokes the preceding model. Otherwise every vertex
has exactly five boundary neighbours. On each edge their intersection
must have size exactly four: size five violates the common-neighbour
bound, while size at most three covers all seven boundary vertices.
Those four common boundary neighbours leave no room for a common
neighbour in `X`. Thus `G[X]` is triangle-free.

The sets `A=N_X(f1)` and `B=N_X(f4)` are nonempty and disjoint. If a
vertex `x` of `A` had no neighbour in `A`, then `N_X(x) union {f1}`
would be an independent subset of its neighbourhood of size
`d_X(x)+1`. The assumed bound is `d_G(x)-5=d_X(x)`, a contradiction.
Thus `A` contains an edge, and so does `B`. The ends of an edge in
`A` have distinct two-element missing sets in `S`, both containing
`f4`; their only common omission is therefore `f4`. That edge sees
all of `S-{f4}`. The corresponding edge in `B` sees all of `S-{f1}`.

A shortest path between these disjoint edges has no internal vertex
on either edge. Assigning its internal vertices to the first edge
gives two disjoint connected adjacent bags in `X`, each still seeing
every vertex of `T union {f2,f3}`. Combining them with the exterior
model supplies all seven bags and all twenty-one required adjacencies
in the original graph.

Under the alternative triangle-free hypothesis, `N_X(x)` itself is
independent. The assumed inequality immediately yields `d_S(x)>=5`,
so the same construction applies. Conversely, at a vertex with
`d_S(x)<=4`, that inequality forces `N_X(x)` to contain an edge;
the vertex lies in a triangle of `G[X]`. The final description of the
remaining cells is therefore justified.

## Scope and dependencies

The proof uses the standard set and fan forms of vertex Menger's
theorem, connectivity after deletion, and explicit branch sets. It is
a direct construction, with no induction class, quotient-criticality
claim or finite-order restriction. The abstract theorem takes the
neighbourhood bound as a hypothesis; obtaining it from contraction
criticality, and obtaining the cell and reserved path in the wider
programme, are application obligations outside this audit.

No mathematical gap remains in this pinned family theorem. It does
not close cells with a low-boundary-degree vertex on a triangle,
cells with additional reserved contacts, the entire split-clique
neighbourhood case, or `HC_7`.
