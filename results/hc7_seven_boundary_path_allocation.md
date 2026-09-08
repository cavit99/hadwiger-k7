# A central-root path on a seven-vertex boundary

**Status:** written normalization; a separate exact-source internal audit is adjacent. The
simultaneous allocation described at the end remains unproved. This is
not a closure of the two-triangle case or Conjecture 19.

Graphs are finite and simple; set neighbourhoods are external. Write
`Q=K_7` minus two independent edges. A rooted model has disjoint connected
bags containing their respective roots.
The inputs are [the four-root packet, Lemma 1](hc7_two_triangle_exterior_helpers.md),
SHA-256 `b3fe07ea52e0e553c61edb59cd5b7da3719ae834d8803f21afb9bde90fc410a8`,
and, only for the actual-host application,
[contraction closure, Corollary 3](../active/hc7_companion_contraction_closure.md),
SHA-256 `ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`.
Both inputs have adjacent audits. No new literature input is used.

## 1. Hypotheses and conclusion

Let `F` have vertex partition `D dotcup C dotcup P`, where `D` is
nonempty, `C={r} dotcup B` has four vertices, and `P={p1,p2,p3}` has
three. Suppose that, for every nonempty `X subseteq D` and every `d in D`,

`|N_F(X)|>=7`, `d_F(d)>=8`, and `|N_F(d) intersect C|<=2`.

The normalization does not require edges within `C`. In the application,
`B` is a literal triangle. Write `F_c=F-(C-{c})` for `c in C`.
Each `F_c` satisfies the four-root packet at `P union {c}`: deleting
three roots loses at most three boundary vertices and at most two
neighbours of any nonroot. Thus all four rooted `K_4` responses exist.

**Theorem.** Among all these responses, maximize the number of vertices
in the three P bags, then minimize the central bag's order. After
permuting the names of the P roots and bags, a maximizing response has
connected, pairwise adjacent P bags `M1,M2,M3` and central bag

`R={z0,z1,...,zk}`, where `z0=c in C`.

They partition `D union P union {c}`, retain the four prescribed roots,
and have these properties:

1. If `k=0`, the singleton `c` contacts all three P bags.
2. If `k>=1`, `F[R]` is the induced path `z0...zk`. Put `q=zk`.
   The vertex `q` gives the only R contacts to `M2,M3`; every internal
   path vertex contacts `M1` and neither `M2` nor `M3`.
3. Every `zj` with `j>=2` has no neighbour in `C`. If `k=1`, `q` has
   at least six actual neighbours in `M1 union M2 union M3`.
   If `k>=2`, `z1` has at least five actual neighbours in `M1`, each
   internal `zj` with `j>=2` has at least six in `M1`, and `q` has at
   least seven in the union of the P bags.

The central root is selected from `C`; the theorem does not prescribe it.

## 2. Path and unused-component normalization

Take the stated extremal response. Inside `R`, choose a minimal tree
containing `c` and a contact to each P bag. Central-bag minimality makes
this tree span `R`. A nonroot leaf must be the sole R contact to at
least two P bags. Otherwise it can be donated to the unique bag whose
contact would be lost (or to any contacted bag if none would be lost):
the remaining R tree is connected, its old leaf edge restores the
donated contact, and all other contacts survive. This increases the
P union. A leaf with no P contact could instead be deleted.

Two nonroot leaves would require four distinct sole-contact labels.
Hence a nonsingleton tree is a path with `c` at one end and `q` at the
other. Name two of q's exclusive labels `M2,M3`. All earlier vertices
can contact only `M1`. A chord bypassing a nonempty internal segment
either permits donating that segment to `M1`, if it has an M1 contact,
or permits deleting it from R. The old path edge from a retained end
to a donated segment preserves the central M1 contact. These moves
contradict the two extremal choices, so the path is induced.

Let `U` be a component of unused vertices in `F_c`. It lies in `D`
and has no P-bag neighbour, since otherwise all of U could be absorbed
there. Its boundary is therefore on R. In particular `k=0` or `k=1`
permits no such component, by the boundary-at-least-four condition.

For `k>=2`, mark the endpoints `c,q` and every internal path vertex
with an M1 contact. If U has path neighbours strictly before and after
an internal marked vertex, reroute R between the extreme attachment
positions through a path in U. Donate the entire bypassed segment to
M1. That segment is connected and has an M1 contact; the retained old
path edge restores the R--M1 contact. The root and q remain in R,
so R--M2 and R--M3 survive. This strictly increases the P union,
regardless of whether the reroute uses every vertex of U.

Consequently each unused component's attachment interval lies in one
closed gap between consecutive marks. For any gap, take its internal
path vertices together with all unused components whose intervals lie
in that gap. This set has boundary contained in the two endpoints:
its path vertices have no P contact, the path is induced, and any
component meeting its interior must have its interval in this gap.
A nonempty such set contradicts boundary at least four. Components
with just one attachment position already violate that bound directly.
All gaps are therefore empty. There are no unused vertices, and every
internal path vertex contacts M1. This proves (1) and (2).

## 3. Switching the central root and counting actual neighbours

Suppose `j>=2` and `zj` sees `c' in C-{c}`. Use `c',zj,...,q` as
the new central path and donate `z1,...,z(j-1)` to M1. The donated
prefix contains an internal path vertex with an M1 contact. Its last
old path edge gives the new central M1 contact, including when `zj=q`;
q retains its exclusive M2 and M3 contacts. All P roots and their
mutual contacts remain untouched. This is a valid response in `F_c'`,
with the old central root now excluded and a strictly larger P union.
Thus no such edge exists. The induced path also excludes `c--zj`.

If `k=1`, q has at most two C neighbours and all its other neighbours
are in P bags, giving at least six there. If `k>=2`, z1 has its two
path neighbours and at most one additional C neighbour; its other
neighbours are all in M1, giving at least five. Later internal vertices
have no C neighbours, exactly two path neighbours, and all other
neighbours in M1, giving at least six. Finally q has no C neighbour
and only one path neighbour, giving at least seven P-bag neighbours.
These are vertex counts in the original F, not counts of adjacent bags.

## 4. Application and the unclosed allocation

In the actual seven-connected, minimum-degree-eight, Q-free host, let
`N(v)=A dotcup B dotcup {x,y}`, where A,B are three-vertex triangles
and xy is an edge; extra edges are allowed.
Put `W=G-N[v]`. If nonempty `D subseteq W` has boundary `{r} union P`
in `G-v-B`, with `r in A` and `P subseteq W` of order three, then
`N_G(D)=B union {r} union P`. Seven-connectivity forces equality,
since v survives outside that closed side. The induced closed side
satisfies the displayed boundary and degree conditions. Beside the
four-clique `{v} union B`, contraction closure gives every D vertex
at most two B neighbours; a vertex seeing r has at most one B neighbour.
Thus every D vertex sees at most two vertices of `C={r} union B`.
No chromatic-criticality assumption is used in this application.

The theorem does not place B contacts in different P bags. In particular,
donating q to M2 can destroy the sole central M3 contact. Rerouting through
M1 would have to retain a connected p1 bag and its other clique contacts;
the actual-neighbour counts do not establish such a transfer. One useful
further target is an r-centred response whose P bags have a perfect
matching of contacts to B in that same model. No such matching, compatible
extra helper, or simultaneous choice among the four responses is proved.
