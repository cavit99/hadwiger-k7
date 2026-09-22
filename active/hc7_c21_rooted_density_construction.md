# Conjecture 21: completed rooted-density construction

**Status, 21 September 2026:** written proof with two separate hash-pinned
internal audits. Every finite `K7^-`-minor-free graph is six-colourable.
The [research ledger](../RESEARCH_LEDGER.md) gives the current significance
assessment. HC7 remains open; internal audits are not external peer review.

## 1. Changed external input

Dvořák, Norin and Rahman, *Every graph with no K7= minor is 6-colorable*,
[arXiv:2609.17760v1](https://arxiv.org/html/2609.17760v1), submitted
15 September 2026, state:

- Theorem 1.1: every `Q=K7-2K2`-minor-free graph is six-colourable.
- Theorem 1.3: every five-connected graph of order `n>=6` with
  `e>=4n-7` contains Q.
- Theorem 1.6: a minor-minimal non-six-colourable `K7^-`-minor-free graph
  is seven-connected and has `e>=4n-2`.

Their first theorem resolves Conjecture 19. Their density theorem directly
excludes our former remaining host: seven-connectivity implies
five-connectivity, minimum degree eight gives `n>=9` and `e>=4n`.
No neighbourhood or exterior-colouring case remains for that application.
These are external preprint results. The statements and this implication
have been inspected; we have not independently reconstructed their whole
proof. They are not our own completion of the user's objective.

## 2. The completed theorem

The [global proof](../results/hc7_k7minus_bilight_extremal.md),
[first audit](../results/hc7_k7minus_bilight_extremal_audit.md) and
[second audit](../results/hc7_k7minus_bilight_extremal_second_audit.md)
establish that every 4-bilight graph on `n>=3` vertices with `e>=4n-2`
contains `K7^-`. In particular this proves Dvořák–Norin–Rahman Conjecture
1.5 for five-connected graphs. Their Theorem 1.6 then gives C21.

The new construction has two parts.

1. The [rooted helper theorem](../results/five_root_one_missing_contact.md)
   gives five prescribed-root bags and two root-free helpers with at least
   ten of eleven possible contacts involving a helper. It holds at rooted
   four-density two in every 4-light five-rooted graph, without an order
   bound. Its reductions preserve all roots and fixed disjoint preimages;
   padding is used only to select a fragment. This part is computation-free.
2. The global proof eliminates degree-five vertices and all five-cuts of
   a minimum density counterexample. A low-density fragment contains a
   low-triangle edge; consistent orientation makes an inclusion-minimal
   such fragment an unrestricted end. A new local end lemma gives the
   contradiction. The resulting six-connected graph has only high-triangle
   edges, and the degree-six and degree-seven terminal arguments finish.

The degree-seven step uses an
[elementary nine-vertex lemma](../results/hc7_k7minus_degree7_quotient_hand_proof.md),
with a [separate internal audit](../results/hc7_k7minus_degree7_quotient_hand_proof_audit.md),
together with a written reduction from arbitrary host order. Five maximal
complement types and explicit models replace the former 232-case
computational premise; its original proof and verifier remain preserved.
The [earlier helper probes](hc7_c21_helper_search_findings.md) are not proof
inputs. The [working draft](../archive/hc7_c21_global_composition_working_2026-09-21.md)
preserves the superseded routes; it is not the audited final proof.

## 3. Barriers remain valid

- A [boundary-star replacement](../barriers/five_root_star_replacement.md)
  can preserve density and destroy lightness. The final argument proves
  admissibility of its particular operations instead.
- [Density one](../barriers/five_root_helper_completion.md#1-the-density-one-extension-fails)
  does not force the ten-contact rooted model. The global end argument
  excludes those obstructions in a minimum counterexample.
- [Arbitrary density](../barriers/five_root_helper_completion.md#3-arbitrary-density-does-not-force-all-eleven-contacts)
  cannot force all eleven contacts. This blocks a direct strengthening
  of the rooted theorem to complete helpers.
- Independently selected helper models can yield `K_{2,2,2,2}`, without
  `K7^-`; the [working draft](../archive/hc7_c21_global_composition_working_2026-09-21.md)
  records that exact model-composition obstruction. The final proof does
  not rely on arbitrary such composition at six-cuts.

The [former six-cut frontier](hc7_k7minus_sixconnected_4n_sparse_threecut_frontier.md)
is now historical. Its global target follows from the new theorem; its
stronger local placement assertions are not automatically proved.

## 4. What remains towards HC7

C21 guarantees a seven-bag minor with at most one missing adjacency in
every non-six-colourable graph. HC7 requires all 21 adjacencies. Completing
that contact while preserving disjoint connected bags remains unproved.
A density-only version of the new theorem cannot supply the last step:
two universal vertices joined to a five-connected plane triangulation give
seven-connected `K7`-minor-free graphs with `5n-15` edges, as noted in
Dvořák–Norin–Rahman's introduction. Their chromatic structure must matter.

The complete [C21 manuscript](../paper/k7minus-six-colour/main.pdf) now
includes the supporting constructions and exact proof dependencies, with
a [separate internal audit](../paper/k7minus-six-colour/main_audit.md).
External review and historical priority remain outstanding. No author
contact has been authorised, and no particular HC7 construction follows
automatically from this theorem.

The next discovery focus is the actual minor-minimal non-six-colourable
`K7`-minor-free host: combine its proper-minor six-colourings with a changeable
`K7^-` model to obtain a `K7` model or a valid colouring lift. This is an
HC7-level construction obligation, not a proved reduction to a small local
case. The density-only and all-eleven-contact barriers above remain in force.
The old `K7^-`-minor-free critical-host degree, clique and defect restrictions
cannot be transferred to this larger class. The separate `3,2,2`
[seven-cut colouring theorem](../results/hc7_k7minus_three_component_seven_cut_exclusion.md)
can be reused only when its actual connectivity and boundary hypotheses hold.

**Selected checkpoint — conjectural:** every seven-connected graph `G`
with `chi(G)=7`, every proper minor six-colourable, and a degree-seven
vertex contains a `K7` minor. This would exclude an entire unbounded case;
it would not settle HC7. A hypothetical minimal counterexample has a
vertex of degree seven, eight or nine, by Mader's connectivity and edge
bounds; see [Rolek–Song, Theorems 1.8 and 2.1](https://sciences.ucf.edu/math/zxsong/wp-content/uploads/sites/13/2018/04/Coloring-graphs-with-forbidden-minors.pdf).

The [existing degree-seven programme](hc7_degree7_model_separator_frontier.md)
already supplies a connected exterior, proper-minor colourings realising
every single repeated neighbour pair, and rooted five-bag models. Its
global compatibility step is still open. For `S=N(u)`, the construction
must produce either a `K7` model or a six-colouring of `G-u` using at most
five colours on `S`; the latter extends to `u`. Choose the repeated pair,
colouring and rooted bags together. More fixed-model responses or a fresh
enumeration of neighbourhoods do not close this checkpoint.

Use the [actual boundary-aligned edge response](../results/hc7_low_degree_boundary_edge_alignment.md)
as a common-host witness, subject to its precise hypotheses. The
[selected-response barrier](../barriers/hc7_degree7_single_edge_response_alignment_barrier.md)
and [reversible rotations](../barriers/hc7_near_k7_rotation_involution_barrier.md)
exclude the old shortcuts. Keep the original critical host fixed; a
quotient supplies a colouring, not inherited criticality. Any recursive
construction needs a proved decreasing parameter and both colouring and
minor lifts. No such completion mechanism is presently established.

### Current construction and its limits

The [recolouring calculation](hc7_degree7_colour_repair_working.md), with
a separate internal audit, works with all six-colourings of one actual
edge-deletion graph. For an interior edge it identifies every endpoint
connection requiring `u` and gives a coupled interchange that can remove
all such exceptions. A single endpoint repair is precisely the reverse
of the earlier separating-edge move; it is not a decreasing reduction.
Even the strengthened singleton-root incidence does not suffice:
the [ten-vertex selected-layer counterexample](../barriers/hc7_degree7_selected_colour_layers.md)
has a written width-five certificate. It lacks criticality and seven-
connectivity, so the full construction remains possible.

**Working boundary-edge refinement.** For `h=sv`, with `s in S` and
`v in C`, the same interchange argument gives at most one exceptional
connection: the equality colour already occurs at `s`. An exception
forces a repeated pair `{s,t}` with `t in N_F(s)-N_G(v)`, where
`F=overline{G[S]}`. If `d_F(s)=2`, there are at most two companion roots.
Moreover `D=N_C(s)` contains an edge: otherwise `{u} union D` is an
independent subset of `N(s)` of size `|D|+1`, contrary to Dirac's bound
`alpha(G[N(s)])<=d(s)-5=|D|`. Thus the chosen boundary edge can belong
to an actual triangle through `s`. These restrictions do not synchronise
its different edge responses. The missing construction is one collection
of four disjoint connected core bags meeting both endpoint components and
retaining the boundary contacts to `u`. Separate colourful-set models
do not supply that collection; zero exceptional connections is not an exit.

#### Completed case: the two-triangle neighbourhood

The [case-closure theorem](../results/hc7_two_triangle_case_closure.md)
has a fresh separate whole-chain internal audit. If a seven-connected
graph of chromatic number at least seven has a vertex `u` with
`N(u)=P dotunion Q dotunion {r}`, where `P,Q` are anticomplete triangles
and `r` is complete to both, it contains a `K7` minor. Both chromatic
branches of `J=G-{u,r}` are covered. Other degree-seven neighbourhoods
and degrees eight and nine remain open.

The structural theorem is more general. A five-connected graph `J` with
an ordinary `K5` minor, two anticomplete triangles `T=P union Q`, and
at least six neighbours for every nonempty root-free set has either a
`K5` model meeting `T` in every bag or `J-z` planar for `z outside T`.
In the original host, the model extends with `{u},{r}`; a four-colouring
of `J-z` extends by giving `u,z` colour five and `r` colour six.

Its direct construction retains the whole
[extremal prism](../results/hc7_two_triangle_extremal_prism.md).
[Path-containing web cells](../results/hc7_two_triangle_web_path_cells.md)
give the apex outcome. Otherwise
[cutvertex exclusion](../results/hc7_prism_remainder_cutvertex_exclusion.md)
and the [two-connected cell theorem](../results/hc7_prism_two_connected_cell_exclusion.md)
exhaust the remainder: all actual cells are empty. Three disk Euler
bounds contradict the actual degree and rail-contact bounds. The decisive
projection uses a connected complementary region to retain every actual
rail contact, and a separate connected projection only to fix its side
of the surviving cycle. No completion edge becomes a minor contact.

The earlier [three-connected insertion proof](../results/hc7_two_triangle_three_connected_remainder.md)
and the independent [common-graph planarity lemma](../results/three_web_remainder_planarity.md)
remain audited results, but neither is needed in the final chain. The
[isolated-gate precursor](../archive/hc7_prism_isolated_gate_working_2026-09-22.md)
is preserved. The final proof bypasses its cofacial-insertion difficulty
by excluding the cells themselves. The following older response and
allocation gaps are historical route nonclosures, not gaps in this
case-closure theorem.

#### Next attack: the split-clique neighbourhood

**Open construction target:** exclude `G[N(u)]=K3 dotunion K4` in the
original seven-contraction-critical host. Write its triangle as `P`,
its four-clique as `D`, and its exterior as `C=G-N[u]`. For every
`r in D`, the new structural theorem applies to `J_r=G-{u,r}` with
triangles `P,D-{r}`. The apex alternative would six-colour `G`, so a
triangle-meeting `K5` model exists. Its bags need not distribute the
three roots of either triangle into distinct bags.

A concrete sufficient construction is a partition of the common graph
`M=G-({u} union D)=P union C` into connected sets `A,B`, each meeting
`P` and each adjacent to all four vertices of `D`. Since `M` is connected,
these two parts are adjacent. Together with singleton bags `D` and `{u}`,
they give the required `K7`. This partition is not yet proved to exist.
The attack must choose the two parts, root ownership and proper-minor
colourings together; models obtained for different choices of `r` cannot
be combined without a valid ownership argument. All final bags may change.

A [working root-placement strengthening](hc7_split_clique_construction_working.md)
reconstructs the proof with one triangle kept singleton. It gives four
partitions of the same three-connected `M`: in the partition indexed by
`r`, one P-meeting part is adjacent to all of `D` and the other misses
only `r`. This deduction is not separately audited. The explicit joint
construction joins two deficient parts and keeps the P-containing component
of their complement. The unresolved step is retaining all four clique
contacts in that component; no intersection-connectivity assumption or
common spanning tree is available. The [maximal-partition exchanges](hc7_split_clique_exchange_working.md)
give smaller possible shapes for the full helper, but do not resolve
this loss of contacts. These remain working deductions, not a further
completed case.

The [current four-root construction](hc7_split_clique_rooted_construction_working.md)
avoids that unaudited root-placement premise. It reserves two disjoint
connected bags in the actual host; any remaining rooted `K4` would lift
to `K7`. Fabila-Monroy--Wood's full obstruction theorem gives a spanning
web directly, because the four roots have two disjoint actual edges.
Minimising the number of reserved vertices gives explicit decreasing
exchanges, with all root contacts retained. The
[seven-boundary cell theorem](../results/hc7_split_clique_seven_boundary_cell.md),
with a separate internal audit, now excludes every triangle-free cell
with three actual web gates and four contacts on one reserved path.
More generally it excludes the entire family in which every cell vertex
has at least five boundary neighbours. The proof combines two connected
internal helpers with an exterior clique model retaining all three gates
and the two middle contacts. No quotient inherits criticality.

A minimum remaining exact cell has a two-connected interior and a
four-connected graph after completing its three gates to a triangle;
the working construction gives the actual-shore decrease and the cutvertex
exit. The [planar-cell theorem](../results/hc7_planar_seven_boundary_cell.md),
with a separate internal audit, closes the planar completed-side case:
two edge bounds force opposite-port paths, contracting them supplies a
proper-minor colouring with at most two port colours, and a four-colour
extension at the three cofacial gates colours the whole original host.
No arbitrary precolouring extension across a longer cycle is assumed.

Thus the remaining completed side is nonplanar, and its low-boundary-degree
vertices lie in internal triangles. The
[odd-wheel counterexample](../barriers/hc7_seven_boundary_odd_wheel.md)
shows that seven-connectivity, the neighbourhood independence bounds and
this completed-side connectivity do not themselves force the desired
minor, even when every choice of two path contacts gives rooted
four-density four for the helper theorem. The original colouring
obstruction or additional frame information must enter. Cells with extra
reserved contacts and the final whole-host colouring also remain outside
these closures.

Requiring both the gate side and the port side to be nonplanar also
fails: the [explicit 42-vertex barrier](../barriers/hc7_both_nonplanar_cell.md)
retains seven-connectivity, the local Dirac inequalities and the exact
boundary and path data. Its finite hypotheses and six-colouring are
checked by a deterministic verifier; it has not had a separate audit.
Independent helper and linkage models therefore cannot be combined on
these structural premises alone. The original split-clique frame and
non-six-colourability remain available; neither is realised by the example.

The subsequent colouring attempts reach a common lift obstruction.
Contracting full sides supplies actual exterior colourings and common
available colours on the deleted sides, but not their list-colouring
extensions. Likewise, a quotient identifying both port pairs and a gate
edge gives a compatible outside response only: it is not an edge-deletion
colouring of the whole graph until the cell is restored. The four-clique
list-matching formulation reproduces the existing repeated P--D pair
rather than a decreasing exchange. These are route nonclosures, not new
counterexamples. The bipartite matroid proof does not supply this lift:
its contractions combine original colours, and its spanning forests may
consume the vertices reserved for the extra path. The complete case
still requires an original-host colouring or seven compatible bags; a
new approach need not preserve these chosen sides or models.

More specifically, normalising a selected bipartite scheme can absorb
actual neighbours of the fourth D root into another prescribed D bag.
Even a triangle of such neighbours does not itself prevent that loss;
additional original-host edges must enter the rerouting. Marked forest
allocations without this retention step therefore remain conditional.
The [cell-free colouring discussion](hc7_split_clique_rooted_construction_working.md#the-remaining-global-construction)
also records why the present exchanges do not imply a three-colour reserve.

**Working simultaneous-star construction; no case closure.** For
`r in D`, put `Q=D-{r}`, `T=N_C(r)` and `k=|T|`, so `d(r)=k+4`.
Suppose some `q_j in Q` misses an independent set `W subset T` of
order `k-2`. Choose any other `q_i in Q` and any `p in P`. Contract
the disjoint stars `{u,p,q_i}` and `{r,q_j} union W`, then six-colour
the resulting proper minor. Lift to `J=G-{u,r}`, giving the leaves
of each star its contracted colour. This is proper: each identified
leaf set is independent, and every other original J-edge survives
between distinct quotient vertices. The two star colours differ because
`q_i q_j` is an edge.

Each of `P union Q` and `T union Q` now uses at most five colours.
Their nonempty sets of missing colours must be the same singleton
`{gamma}`: distinct representatives would colour u,r and hence G.
Thus both unions use exactly five colours. In the first, the unique
repeated pair is `p q_i`; in the second, `W union {q_j}` is one colour
class and all four other vertices have distinct colours. Give the merged
ur vertex colour gamma. This yields a colouring of `G/ur` in which P
and T each use exactly one Q colour, and those colours differ. It works
for every prescribed choice above. The minor has `k+1` fewer vertices;
this is an explicit colouring lift, not an induction. It does not retain
an earlier colouring or its paths.

The hypothesis holds whenever `d(r)=7`: T is a triangle by Dirac's
bound and u's anticompleteness to T. In any six-colouring of `G/ur`,
the triangles T,Q avoid the merged vertex's colour, so they share a
colour and have a nonedge `t q_j`. Take `W={t}`.
It also holds for the degree-eight and degree-nine instances of the
[common-stem residue](hc7_split_clique_exchange_working.md#where-a-two-p-partition-can-still-resist-the-label-switch).
There the third owned Q label misses T, and T induces a disjoint union
of paths on four or five vertices. Its larger bipartition class has
at least `k-2` vertices, from which W can be chosen. This applies to
that recorded configuration, not to every higher-degree neighbour.

Relabel gamma as six and the Q colours as one, two, three. Then P and T
each have unique vertices `p_i,t_i` of colours `i=4,5`. In J there is
a `p_i`--`t_i` path using only colours `i,6`: otherwise the component
of u in that two-colour graph of `G-ur` can be interchanged and the
edge ur restored properly. These two paths can share colour-six vertices.
If the induced graph `J[4,5,6]` has no
two disjoint paths between the pairs `{p4,p5}` and `{t4,t5}`, Menger gives
a single separating vertex x of colour six. It has a neighbour of each
Q colour: recolouring x with a missing Q colour would destroy the forced
two-colour connection and permit the same interchange. These neighbours
need not be the prescribed Q roots.

There is a joint extraction if the two displayed bichromatic paths A,B
can be chosen disjoint in such a colouring. Let I be the colour-six class
in J. In every five-colouring of `J-I`, each
of `P union Q,T union Q` uses all five colours: otherwise restore I
in colour six and colour u,r with distinct available colours. For each
Q colour i, one of P,T omits i. This forces paths from `q_i` to that
set's colour-four and colour-five vertices in the respective bichromatic
subgraphs of `J-I`; swapping the component
at `q_i` would otherwise remove i from the colourful union. The first
paths avoid B, and the second avoid A. Contract A,B and truncate these
paths at their first contacts. They form a rooted `K_{3,2}` scheme.
The bipartite theorem supplies five compatible bags; lifting retains both
P and T contacts in each helper. The literal Q edges and `p4p5` complete
their clique, and `{u},{r}` complete K7. This is a working conditional
construction, without a separate audit.

The missing step is choosing, within this family of common colourings,
two disjoint paths in their specified two-colour layers.
An arbitrary free-pairing linkage in `J[4,5,6]` need not preserve that
avoidance. For example, a wheel with rim `p4,p5,t4,t5` in that cyclic
order and a centre x of colour six has two disjoint cross-cap edges,
but both prescribed bichromatic paths must use x. Its connected rim
also prevents a four--five Kempe switch from repairing this. This is
an obstruction to that local inference, not a critical-host counterexample.
An attempted rerouting instead uses helpers `{x,p4,t5}` and `{p5,t4}`.
The first still needs paths from Q to x in colours `i,6`; the second
needs paths in colours `i,4,5` avoiding `p4,t5`. Neither is forced by
the current construction. The simultaneous-star freedom has not yet
supplied these missing attachments.

Adding an exterior star contraction does not preserve the colouring
lift automatically: its centre need not admit the common missing colour
when restored. Unlike u,r, its neighbourhood is not one of the two
controlled neighbour sets. No valid iteration has been obtained. Neither
the adjacent-degree-seven case nor the whole split-clique case is closed.

**Audited three-contact closure; the four-contact branch remains.** Choose
`p in P`, six-colour `G/up` with its contracted vertex coloured six,
and let I be the other vertices of that colour. Then I is independent
and anticomplete to p. Put `K=G-({u,p} union I)`, and let X be the
component of `K-D` containing the edge `P-{p}`. That edge together
with D uses all five colours in every five-colouring of K.

The [three-contact theorem](../results/hc7_split_clique_three_contact.md),
with a [separate reconstruction audit](../results/hc7_split_clique_three_contact_audit.md),
proves that if X misses any D vertex, G contains K7. The six paths
in the earlier five-bag extraction combine with three additional
colour-six paths from p to form a fully rooted K3,3 scheme. The two
literal root triangles and u complete K7. No maximality, connectivity
hypothesis or induction is needed for this branch.

Thus in a hypothetical counterexample, X contacts all four D vertices
for **every** p and **every** colouring of `G/up`. The same applies
for every independent `I subset C` anticomplete to p for which
`G-({u,p} union I)` is five-colourable: its colouring extends back to
`G/up`. The [earlier extraction](../archive/hc7_split_clique_asymmetric_extraction_2026-09-22.md)
is frozen; its three-contact allocation gap is resolved.

**Working exchanges in the remaining four-contact branch.** Normalise a
colouring of `G-u` as `P={p_6,a_5,b_4}`, `D={d_4,q_1,q_2,q_3}`.
Swapping any components on colours five and six is valid. Swapping
the one L containing the edge pa makes a the unique colour-six
neighbour of u, and therefore supplies a colouring of `G/ua`.
The new removed class is
`I'=(I-L) union ((V_5 intersection L)-{a})`. Old colour-five vertices
are removed, and old colour-six vertices are restored. The former may
separate X, so the new component need not contain the old one or be
larger. Maximising |X| over all choices supplies no strict exchange
without a retention argument. Universal four-contact retention does
not itself repair this: all four contacts can remain in an unchanged
part of X. Replacing the entire layer on colours four, five and six
by another proper three-colouring is also valid, but supplies no
monotone parameter by itself.

There is a further direct construction if d lies in both the
four--five component containing ab and the four--six component
containing pb. The resulting a--d and p--d paths, together with the
six forced a/p--Q paths, form a fully rooted K2,4 scheme. Its minor,
the literal D clique and edge ap, and singleton u give K7. Criticality
forces the p--Q paths but not p--d: b shares d's colour. Swapping a
component which misses d can move the repeated colour to another P
vertex, but no increasing exchange or complete four-contact
construction has been proved. This conditional construction is working
material, not a further independently audited closure.

**Attempted six-root construction; no valid induction yet.** For every
`r in D`, `J=G-{u,r}` is six-chromatic and therefore contains an ordinary
K6 minor by HC6. The colour repair below with X empty excludes five colours.
A model rooted at all six vertices of `P union Q` would finish
the whole split-clique case by adjoining u. The ordinary model does not
retain those roots automatically; the earlier
[three-helper normalisation gap](hc7_degree7_exceptional_construction_working.md#11-three-helpers-when-the-first-triangle-is-singleton)
remains relevant.

There is a global batch of deletions retaining six-chromaticity.
Let X be an independent subset of C, anticomplete to r, with
`|N_G(X) intersection P|<=1`. Suppose `J-X` had a five-colouring.
Of the two colours absent from Q, choose one whose P vertex, if present,
misses X. Give X, r and that P vertex colour six, and give u the chosen
colour. This would six-colour G, so `chi(J-X)=6`. Alternatively, choose
an adjacent parent in `J-X` for each x and contract the resulting
disjoint stars. A five-colouring of that quotient would lift to `J-X`,
so the quotient is also six-chromatic. All six roots remain distinct,
and rooted models lift through fixed disjoint star preimages. Neither
operation asserts that its hypothesis survives iteration. A minimal
six-critical subgraph can change after deletion; choosing one does not
provide an independent set meeting all such subgraphs.

The colouring lift does not establish the required relative
six-connectivity. A failure after one root-free edge contraction would
have an actual root-free region Y with
`N_J(Y)={x,y} union Z`, `|Z|=4`; contracting xy gives it a five-cut.
Seven-connectivity of G forces Y to meet `N_C(r)`. An ordinary K6 model
in the quotient can lie behind this cut without retaining the six roots.
A six-root allocation across the original boundary, or a colouring
extension through Y, is still needed. Neither follows from the batch
colouring lift, so this does not supply a smaller induction instance.

Two other construction attempts do not close the case. Contracting a
maximal partition's sparse full part B gives one common available colour
on its restored vertices, not degree-sized lists: outside neighbours may
use all five other colours. Small blocks therefore do not justify a
list-colouring extension. A six-path flow in `G-u`, with P capacities
`(2,2,2)` and D capacities `(2,2,1,1)`, gives two valid reserved-pair
webs when its incidence graph is an alternating spanning path. But a
cell in either view may contain a tail from the other reserve, with
only one path gate. Clean cells in a common remainder, a suitable
incidence pattern and a third view are all unproved. The completed
three-web planarity argument cannot be imported under these premises.

The full split-clique frame also excludes a two-apex explanation, even
without chromaticity. If `G-R` were planar for a pair R, it would be
five-connected and contain no K4: in a planar K4 embedding, a face's
three vertices would separate any additional vertex. Thus R meets
`{u} union D` twice and `{u} union P` once, forcing `R={u,d}` with
`d in D`. The planar graph `G-R` has minimum degree at least five and
Euler's inequality forces at least twelve degree-five vertices. Each
must see both deleted vertices to have G-degree at least seven. This
contradicts `d_G(u)=7`. This working deduction does not show that a
K7-minor-free graph must be two-apex; no such structural premise is used.

The attempted two-separator descent has a concrete nonclosure, not a
counterexample or an exhaustive normal form. A separator `Z={z1,z2}`
may leave two components with H0 boundaries `Z union {q1,t}` and
`Z union {q2,t}`, where `T={q1,q2,t}` and neither separator vertex
sees q1 or q2. If both components see all four F contacts, each actual
boundary has order eight. The natural helpers miss different clique
gates; expanding both corresponding exterior bags consumes the two
components. An alternative exterior model rooted at t and all four
ports is not supplied by the linkage argument, which can leave its
surviving clique side at an omitted q1 or q2. Contracting Z does not
repair the proof: it may reduce an original seven-boundary set to six
and does not preserve the degree data. A valid colouring lift or a
different simultaneous allocation remains possible.

The colouring terminal need only be `chi(G-{u,r})<=5`: the
[existing selected-edge argument](hc7_degree7_exceptional_construction_working.md#4-scope-of-the-negative-findings)
would extend it to a six-colouring of G. The construction must therefore
produce a rooted minor or a valid five-colouring of that whole graph,
possibly through an apex description. Separate planarity or colouring
of its pieces is insufficient. The
[six-vertex colouring barrier](../barriers/hc7_split_clique_three_colour_rooted_minor.md)
also excludes a proposed shortcut: two disjoint Kempe components can
have conflicting simultaneous swaps across an edge.

#### Previous attack: use six-chromaticity at the model separator

**Preserved preceding plan and its failed construction; no case closure.** A duplication
check against [the matching-bridge theorem, Theorem 3.5](../results/hc7_degree7_matching_bridge_bundle.md)
and [the connector-or-separator theorem](../results/hc7_exact7_rooted_k5_connector_separator.md)
shows that constructing four rooted bags and then seeking a connector is
already an unresolved repository mechanism. Rebuilding the core is not
the next research task.

Its useful specialised form is as follows. Delete the whole `r`-class
`I0` of a six-colouring of `G-u`. The resulting graph `H` has colourful
`T` in every five-colouring. Delete the repeated-pair class `C` of one
such colouring, containing `p in P,q in Q`. The four remaining roots
`Z=T-{p,q}` are colourful in the four-colourable graph `L=H-C`:
otherwise restoring `C` omits a colour on `T`. Martinsson--Steiner
[Theorem 1.3](https://arxiv.org/html/2209.00594v1#S1), or the bichromatic
`K2,2` scheme and our bipartite theorem, supplies a `Z`-rooted `K4`.

A `p-q` path avoiding these four bags in `J` completes a `T`-meeting
`K5`, hence `K7` with `{u},{r}`. If there is no such path, an actual
inclusion-minimal `p-q` separator inside the four bags has order at
least five, by five-connectivity of `J`. Its two distinguished components
are full to it. Thus one bag contains two separator vertices, but no
valid split follows merely from this fact. The separator can have
arbitrary order. This is the old obstruction, not a new reduction.

The selected case adds `chi(J)=6`. In particular `I0-{r}` is nonempty;
the connector may use these vertices and all other unused colours.
Nonemptiness alone gives no linkage. The next construction must show
how six-chromaticity forces a compatible bag exchange across that actual
separator, or how failure yields a five-colouring of `J` or six-colouring
of `G`. All colourings, repeated pairs and bags may change. A successful
model of this form is sufficient, not compulsory for case closure.

The following restarts still lack an improvement: a Kempe swap can move
cut vertices out of the core colours, but rebuilding the core can move
the separator back; minimising the `r`-class does not synchronise root
and neighbour contacts; contracting a full shore supplies a colouring
without an expansion. None is a new mechanism merely because `I0-{r}`
is nonempty.

Begin with two complementary construction workers and the coordinating
agent: one develops a joint recolouring from actual proper-minor
responses, the other a simultaneous allocation across the full separator.
They must produce an explicit exchange, not more sufficient conditions.
Before scaling, specify its use of `chi(J)=6`, retained roots and contacts,
success and failure outcomes, and a strict improvement or complete lift.
If it applies unchanged to a known weaker barrier, test that example
first. A failure for one frozen colouring or model does not refute an
existential construction.

Only after such an exchange has promise should further workers handle
its separator cases and targeted computational tests, using existing
tools. Recursion requires a preserved class, strict descent and a lift;
none follows from choosing a smaller quotient. If the first construction
cycle returns the same ownership gap, change the proposed operation
before allocating another cycle. Independent reconstruction begins when
an argument appears to close the case or remove a substantial gap. The
whole six-chromatic case remains the success criterion; we do not yet
have a validated new operation that closes it.

**First joint construction cycle.** The
[cap-edge response](hc7_two_triangle_six_chromatic_working.md#a-joint-cap-edge-colouring-response)
first finishes any cap edge with three actual common neighbours in J.
Otherwise one contraction colouring supplies at most two alternating
paths. Their prefixes expand one endpoint, keep the other singleton,
and reserve five distinct common neighbours, including u,r and the third
cap root. This corrects the common-contact deficit simultaneously, but
does not preserve the opposite triangle or the linkage after the expanded
set is deleted. The single-path case gives six-chromatic proper minors;
these do not inherit seven-criticality. The eligible opposite-cap switch
has an inverse and preserves path length. No strict improvement or case
closure was obtained, and no separate audit was commissioned. The
[failed continuations](hc7_two_triangle_six_chromatic_working.md#why-the-joint-response-has-not-closed-the-case)
identify the exact missing lift; repeating a shortest-response argument
without a different operation is not an advance.

**Primary-source recheck, 22 September 2026.** Targeted searches and
version checks found no theorem supplying this joint construction:

- [*Colorful Minors*, v5, 4 September, Theorem 3.1](https://arxiv.org/html/2507.10467v5#S3)
  needs an ordinary `K_k` model with `k>=floor(3qt/2)+t`.
  One annotation for `T` and five target bags require `K12`, not our `K6`.
- [*The Erdős–Pósa Property for Colorful Minors*, 4 September, Corollary 2.3](https://arxiv.org/pdf/2609.04956)
  gives the one-annotation packing–covering property exactly for
  outerplanar targets. It gives no general bounded hitting-set theorem
  for a `T`-meeting `K5`; the critical-host case remains possible.
- [Liu–Luo v2, 9 September](https://arxiv.org/html/2609.06867v2), and
  [Lin, 8 September, Lemma 2.4](https://arxiv.org/html/2609.08713v1),
  give simultaneous star contractions costing at most one colour.
  Neither gives an exact six-colouring lift or the missing bag contacts.
- [Dvořák–Norin–Rahman, v1, 15 September](https://arxiv.org/html/2609.17760v1)
  remains the current version. Its `K7^-`-free critical-host restrictions
  do not apply to the present host, and its colouring theorem does not
  complete the missing adjacency. Its preserved induction class remains
  a useful methodological example.

These checks do not establish an exhaustive literature search. They
support concentrating on the joint construction rather than reopening
the asymptotic or density-only programmes. Its probability of success
cannot presently be quantified responsibly.

#### Existing constructions and exact nonclosures

The [extremal prism reduction](../results/hc7_two_triangle_extremal_prism.md)
now supplies an exact representation if that rooted model is absent.
It applies already in four-connected graphs with an ordinary `K5`
minor and two anticomplete triangles. Maximising one connected helper
forces its complement to be an induced subdivision of the triangular
prism. Every original vertex is retained. In the actual critical graph,
each triangle vertex has at least two neighbours in the helper `E`,
and each path interior vertex has at least four. Moreover `G[E union {r}]`
requires at least four colours. Explicit exchanges confine every non-cut
vertex's prism contacts to one end triangle or a segment of at most two
edges of one path; its degree inside `E` is at least three.

The missing step is extending this exchange through vertices with no
path-interior contact and through separations of `E`, while retaining
the complementary helper's connectivity and all root contacts. A proposed
exclusion of three-connected `E` omitted these vertices and is withdrawn.
No induction or case closure follows from the representation. The
construction keeps the original colouring responses available; it does
not assume that a contracted helper or another extremal choice inherits
them.

The [contraction and colouring attack](hc7_degree7_exceptional_construction_working.md#8-what-the-contraction-attack-establishes)
now forces a triangle around a root with exactly two helper neighbours
and proves exact colouring lifts for a path owning a root. Contracting an induced
three-vertex path retains the prism theorem's premises, but can leave
the owned-root configuration inside the smaller helper. Mandatory Kempe
moves on both triangles, obtained using bipartite contractibility, are
also reversible. The unresolved construction must retain the complementary
connected set's contacts while rerouting or splitting it; neither fewer
quotient vertices nor a change of repeated pair establishes descent.

The subsequent [three-owner construction](hc7_degree7_exceptional_construction_working.md#9-a-construction-for-some-three-owner-patterns)
excludes a common root missing an independent pair of the four-vertex
path, and handles the minimal remaining contact sets when deleting the
root pair leaves a five-chromatic graph. The six-chromatic branch forces
an ordinary `K6` minor. The [two-bag construction](hc7_degree7_exceptional_construction_working.md#10-a-six-clique-model-using-two-remainder-bags)
turns any such model with exactly two bags entering `E` into the required
rooted `K5`, for arbitrary subdivision lengths. The stronger
[two-singleton construction](hc7_two_triangle_six_chromatic_working.md)
now finishes if just two vertices of either triangle are singleton in
the `K6` model. It uses the whole graph after deleting those two vertices,
allows arbitrary remaining bags, and covers every placement of the other
triangle. When all three of its roots lie in one bag, three choices of
helper pair give nested actual cutvertex shores; their incompatible
boundary restrictions force a linkage. It subsumes the previous
[singleton-triangle case](hc7_degree7_exceptional_construction_working.md#11-three-helpers-when-the-first-triangle-is-singleton).
Its four-colour deletion application also finishes if deleting a triangle
edge's ends leaves a four-colourable graph. These are working proofs,
without separate audits, and do not close the whole six-chromatic branch.

**First unresolved step in the extensions.** In a general `K6` model, a
part of a root bag can carry its only contacts to two helpers. Moving it
to one helper loses the other contact. Retaining only one singleton root
leaves routing cuts containing whole helper bags and up to two actual
vertices; the cutvertex nesting above no longer applies. Six disjoint
paths from `T` to chosen model representatives do not fix this: they can
enter other bags first. The stronger actual boundary condition has not
yielded a split preserving every required contact. These are route
nonclosures, not counterexamples to the desired construction.

The colouring attempts retain the same unresolved compatibility issue.
Minimising the size of the `r`-colour class gives five-colourings after
its deletion, with `T` using all five colours. Proper-minor colourings
can use fewer colours on `T`, but their restrictions need not agree with
those five-colourings. Contracting a triangle edge in `G` gives a
six-chromatic proper minor, yet does not make the relevant pair deletion
in `J` four-colourable. Across an actual
seven-cut, a colouring of a contracted shore likewise need not lift
through that shore. A valid joint recolouring or a simultaneous bag
reassignment remains possible; no decreasing transition has been proved.

The [intact-helper barrier](../barriers/hc7_prism_intact_helper_barrier.md)
rules out repairing root ownership solely after contracting two connected
pieces to single vertices. Its four-connected eleven-vertex graph has an
extremal helper and contacts from both pieces to all three paths, but no
`K5` model whose five bags all meet the triangles. It fails the stronger original-host
connectivity and contact bounds. A valid repair must retain those bounds
and the pieces' internal splitting choices.
The new two-bag construction has the additional premise of an explicit
`K6` model; the barrier does not refute this stronger statement.

Deleting the whole `r`-colour class from any six-colouring of `G-u`
gives a five-chromatic graph in which the six roots are colourful in
every five-colouring. The [new marked-minor reduction](../results/hc7_two_triangle_colourful_reduction.md),
with [separate internal reviews](../results/hc7_two_triangle_colourful_reduction_audit.md),
either finishes the model or reduces this pair to four-connectivity.
It covers all separators of order at most three, decreases vertex order,
and preserves the original marks in fixed disjoint preimages. Five
surviving marks finish by the existing rooted-certificate theorem; six
retain two literal triangles, with cross edges allowed.

The four-connected construction remains unproved and is an optional
stronger target, rather than the required next theorem. This reduction
handles both chromatic values of `G-{u,r}` but closes neither branch. Taking a
minimum `r`-colour class does not force a usable connector: the class may
be `{r}`. Paths from different Kempe colourings can reuse a vertex while
representing independent demands, so they do not automatically form a
bipartite scheme. The existing first-hit helper transfer can lose a
required triangle contact. The needed repair remains a simultaneous
choice of all five bags or a valid recolouring of the original host.

Two proposed reductions also remain invalid. Minimising arbitrary
seven-cut shores selects the original singleton `{u}`, without a terminal
construction. Contracting a connected fibre and using its quotient
colouring does not give a colouring lift. Closing an edge fibre under its
equality colour and the colour of `u` can reach another protected root;
if the endpoint connection closes inside the fibre, restoring the edge
creates an odd cycle and defeats the proposed two-colour lift.
A repair must preserve the required boundary partition and prove either
a colour extension or a strictly decreasing, liftable construction.
