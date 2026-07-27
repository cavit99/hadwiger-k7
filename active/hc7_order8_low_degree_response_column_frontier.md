# Low-degree response-column frontier at an order-eight boundary

**Status:** conjectural target assembled from separately audited inputs.  The
simultaneous dual-root pentagonal-bipyramid alternative is eliminated by a
written proof with an adjacent GREEN cold audit.  The low-degree
response-column theorem in Section 6 is open.

This file concerns only the minimum order-eight interface with exactly two
boundary-full components.  It is a conditional laboratory beneath the
all-degree bounded-interface composition theorem, not a proof of `HC_7`.

## 1. Exact host setting

Let `G` be seven-connected and satisfy

\[
  \chi(G)=7,
  \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G,
  \qquad K_7\not\preccurlyeq G.
\]

Let `S` have order eight and suppose that `G-S` has exactly two connected
components `C,D`, each adjacent to every literal vertex of `S`.  The audited
[two-shore boundary-absorption theorem](../results/hc7_two_full_shore_boundary_absorption.md)
gives

\[
                         \chi(G[S])\le4.
\]

Four-colourability of the boundary does not give a boundary partition that
extends through both closed shores.

## 2. One fixed operation and its labelled columns

Fix `v in C`, an edge

\[
                    e=vx,\qquad x\in(C-v)\cup S,
\]

and one six-colouring `c` of `G-e`.  The audited
[arbitrary-edge response-star theorem](../results/hc7_order8_arbitrary_edge_response_star.md)
and its
[dual-free-root refinement](../results/hc7_order8_dual_free_root_response_star.md)
return one of:

1. an actual order-seven full-neighbourhood separation on a nonempty proper
   connected subset of `C` or `D`;
2. a strict order-eight response-side descent on a nonempty proper connected
   subset of `C`; or
3. eight latent connected columns with labels

   \[
                \{t,c_0,c_1,c_2,c_3,c_4,a,b\}.
   \]

Here `t` is the target label containing `x`; `c_0,...,c_4` contain the five
prescribed first neighbours `v_0,...,v_4` belonging to the five
`c`-bichromatic paths of `e`, so `vv_i` is the corresponding first edge;
and `a,b` are the two nonresponse labels.  For every consumed label `r`, the
construction gives two adjacent connected roots and the seven other
columns, with each root adjacent to every column.  For each `i`, the same
edge `e` and the same colouring `c` give a literal path from column `c_i`
to column `t`.

The order-eight descent can belong to one of the seven prescribed first
edges rather than to `e`.  It is nevertheless a strict response-side
descent on the declared literal shore-size parameter.

In the order-seven outcome, choose any edge crossing from the returned
connected set to its full neighbourhood and six-colour its deletion.  The
boundary partition extends through the opposite closed shore but cannot
extend through the intact returned shore, since otherwise the two
extensions would glue.  Thus the output is a
[generic exact-seven response interface](../results/hc7_generic_exact7_response_restart.md)
on a proper literal shore, as required by the recursive alternative below.

## 3. The simultaneous pentagonal-bipyramid alternative is eliminated

For a consumed label `r`, let `K-r` be the contact graph of the seven
surviving columns.  A `K_5` minor in `K-r`, together with the two roots,
lifts to an explicit `K_7`-minor model in `G`.

The audited
[seven-column contact theorem](../results/hc7_seven_column_contact_structure.md)
says that a surviving `K-r` either has a vertex of degree at most three or
is a pentagonal bipyramid.  The written
[dual-root overlap closure](../results/hc7_order8_dual_root_contact_overlap_closure.md)
proves that `K-a` and `K-b` cannot both be pentagonal bipyramids: their
overlap already contains a `K_5` minor after another latent column is
consumed.  Consequently one of the two free-root choices has a contact
graph `J` with

\[
                         \delta(J)\le3.                \tag{3.1}
\]

Thus no pentagonal-bipyramid path-splitting theorem is required in this
dual-root construction.

## 4. One noncontacting incident-pair normal form

The seven labels of `J` consist of the target `t`, the five response sources
`c_0,...,c_4`, and one remaining nonresponse label `q`.  The written
[unified incident-pair theorem](../results/hc7_order8_unified_incident_pair_normal_form.md)
removes the former split between an exposed source--target pair and a
source-saturated target.

If some source `c_i` does not contact `t`, choose the incident edges

\[
                              vx,\quad vv_i.             \tag{4.1}
\]

If every source contacts `t`, the audited six-vertex rooted-`K_4` lemma
forces a source `c_i` of contact degree at most three.  It misses at least
two other sources; choose one `c_j` and the incident pair

\[
                              vv_i,\quad vv_j.           \tag{4.2}
\]

In both cases the outer endpoints are nonadjacent because their columns do
not contact.  On the common two-edge deletion there are exactly the three
positive equality signatures

\[
                         (=,\ne),\quad(\ne,=),\quad(=,=), \tag{4.3}
\]

and no all-proper signature.  The common contraction colouring has exact
monochromatic neighbourhood trace consisting of the two outer endpoints.
It gives either:

1. one selected incident edge bichromatically linked for all five alternate
   colours; or
2. a bypass between the two noncontacting endpoint columns, avoiding `v`,
   with two named component switches giving the opposite one-edge responses.

A clean bypass adds the missing contact.  A dirty bypass and universal
saturation remain nonterminal.  In the saturation branch, either one named
component switch already gives an opposite one-edge response, or all five
bichromatic components contain the whole endpoint triad.  In the latter
case five colour-distinct first edges together with the selected pair give
a prescribed seven-edge all-boundary fan, unless an order-seven separation
or strict order-eight descent occurs.  The fan preserves first edges, not
the five complete bichromatic paths.

The simultaneous-contraction colouring need not induce the boundary
partition of the original fixed colouring `c`.  The common data are the
literal operation, column labels, incident edges, contraction colouring and
named switches—not a common boundary trace.

### 4.1 Conflict-component normal form for every bypass

The separately audited
[incident-bypass conflict theorem](../results/hc7_order8_incident_bypass_conflict_split.md)
removes the distinction between disjoint and intersecting named bichromatic
components.  From their one fixed common-deletion colouring and two named
switches it obtains a nonempty bipartite edge set `F` with:

1. one colouring in which exactly all edges of `F` are monochromatic;
2. for every `f in F`, a minor-critical colouring in which exactly `f` is
   monochromatic;
3. no colouring in which every edge of `F` is proper; and
4. all five alternate-colour Kempe locks at every unit edge in its own unit
   colouring;
5. one induced conflict component which, in the first colouring, splits
   into two adjacent connected sides each seeing all five alternate palette
   colours outside the full conflict set.

Thus every dirty bypass now has an exact same-operation conflict object and
a complete all-edge/unit/no-empty response table.  Unit edges on opposite
open shores orient their boundary responses in opposite directions, so a
shared boundary partition would already glue; neither shore occurrence nor
a partition collision is forced.  The theorem still does not assign
the five palette colours to five distinct latent columns.  This distinction
is essential: the audited paired-colourful-set barriers already show that
two connected full-palette sets do not statically force the labelled rooted
minor required here.

The accompanying
[conflict-compression barrier](../barriers/hc7_incident_bypass_conflict_compression_barrier.md)
realizes every prescribed nonempty bipartite conflict graph with the central
response table and rigid central Kempe class.  Its seven-connected instance
contains an explicit `K_7`-minor model and is not minor-critical.  It does
not refute the target, but proves that shortestness or Kempe normalization
alone cannot simplify `F`; a proof must use `K_7`-minor exclusion, the unit
responses or the literal column labels.

## 5. Eight-latent-column and rank normalizations

The separately written
[latent-column spanning normalization](../results/hc7_order8_latent_column_spanning_normalization.md)
keeps both fan centres and all eight original fan-tail cores fixed.  Among
pairwise disjoint connected enlargements of those eight columns, maximize
the eight-column contact graph and then total coverage.  Seven-connectivity
and elementary absorption prove

\[
                    V(G)=\{v,w\}\mathbin{\dot\cup}
                          \bigcup_{s\in S}\widehat K_s. \tag{5.1}
\]

Thus a selected bypass avoiding `v` has no unclassified exterior interior:
after leaving its endpoint column it meets either `w` or another latent
column.  If its first old-object encounter lies in a root away from `w`,
changing which nonresponse label is consumed turns that encounter into a
latent-column encounter.  With enlarged columns the column encounter can
occur earlier.  The selected endpoint columns and incident edges survive,
but the low-degree property of the new seven-column deletion need not.

The written
[common-deletion connectivity theorem](../results/hc7_order8_incident_pair_common_deletion_connectivity.md)
adds a host-level alternative.  The graph obtained by deleting the selected
incident pair is six-connected, unless `v` has degree exactly seven and its
singleton shore is already a strict generic exact-seven response restart.
Thus every nonrecursive dirty bypass now lives in one six-connected common
deletion.  For its named bypass, every root-first encounter can be changed
to a latent-column encounter unless the bypass itself uses the fixed opposite
centre `w`.  In that exceptional case six-connectivity supplies a path
avoiding both centres, but does not preserve the two named bichromatic
component switches.  Thus the exact remaining path residues are a first
already-contacting latent column and a fixed-centre provenance bottleneck.

A decorated finite rank must live on all eight latent labels, not one
seven-column deletion.  A useful order is

\[
 \left(
   |E(K)|,
   \left|\bigcup_sV(K_s)\right|,
   -d_{\rm old}(P),
   -|P|
 \right),                                                   \tag{5.2}
\]

maximizing the first two coordinates and minimizing the last two.  Contact-
neutral rotations are permitted only when they preserve the fixed operation,
the endpoint seeds, all eight labels and dual-root realizability, and improve
a later coordinate without reducing an earlier one.  The rank makes a
proved exchange terminate; it does not create that exchange.

There is one useful conditional finite compression.  If the target contacts
all five sources, a designated low-degree source has degree at most three,
and `J` is **abstractly** edge-maximal `K_5`-minor-free, the finite
[edge-maximal source-contact theorem](../results/hc7_order8_edge_maximal_source_contact.md)
gives a spanning `K_4` model in `J-c_i` met by `c_i` in exactly three bags.
The two roots, `c_i`, and those four bags form a labelled `K_7` with one
missing adjacency, incident with `c_i`.

The audited
[one-defect two-root completion/separation theorem](../results/hc7_one_defect_two_root_k5_separator.md)
then gives a `K_7` minor or a genuine full-neighbourhood separation.  The
separation can have unbounded order and need not preserve the selected
response.  More importantly, maximality under realizable exchanges in
(5.2) is strictly weaker than abstract edge-maximality.  This finite result
is therefore a conditional endpoint for the dirty exchange, not a proof of
that exchange.

## 6. Exact open theorem

### Coupled dirty-bypass and saturation composition theorem

In the setting of Sections 1--4, choose the incident pair and common
contraction colouring from Section 4 and an eight-latent-column system
maximal under (5.2).  Prove at least one of:

1. an explicit `K_7`-minor model in `G`;
2. one complete equality partition of `S` extending through both closed
   shores;
3. an actual order-seven selected-response interface on a nonempty proper
   connected subset of `C` or `D`;
4. a strict order-eight response-side descent on a proper connected subset
   of the operated shore; or
5. for the same edge `e`, colouring `c`, eight latent labels, five first
   neighbours, target and dual-root roles, a connected reassignment or
   controlled contact rotation which strictly improves (5.2).

The proof has two precise obligations:

- **conflict-component label alignment:** use the all-edge/unit/no-empty
  response table from Section 4.1 and the bilateral palette contacts to
  construct the required labelled `K_5` model from the latent columns, or
  return an explicit `K_7`-minor model, a common boundary partition, a
  strict exact-seven response, or a proper
  nested same-form order-eight interface which preserves the selected
  response and strictly decreases the literal operated shore.  A first
  old-column encounter, a hit on `w`, another colouring or an unranked contact rotation is not a
  final outcome;
- **joint triad saturation:** compose the named one-edge response or the
  prescribed seven-edge fan from the universal-saturation branch with the
  same latent columns.  Palette-indexed fan arms cannot be read as column
  labels without proof.

An order-seven or nested order-eight output is recursive only with the
stated proper literal shore decrease and named crossing-edge response.  A
fresh response, an unbounded separator or a new quotient contact system without a proved rank
increase is not a terminal conclusion.

## 7. Secondary two-shore structure

The audited
[two-shore Kempe/list dichotomy](../results/hc7_two_shore_kempe_list_dichotomy.md)
and
[two-shore incidence-cycle theorem](../results/hc7_two_shore_kempe_incidence_cycle.md)
remain relevant structural inputs.  They are not direct inputs to Section
6: their selected transition or alternating cycle need not arise from the
same edge `e`, colouring `c`, colour pair or labelled column system.  They
should enter this branch only after an explicit provenance-alignment lemma.

## Direct inputs and nearest barriers

- [arbitrary-edge response star](../results/hc7_order8_arbitrary_edge_response_star.md)
- [two free root choices](../results/hc7_order8_dual_free_root_response_star.md)
- [two-full-shore boundary absorption](../results/hc7_two_full_shore_boundary_absorption.md)
- [seven-column contact structure](../results/hc7_seven_column_contact_structure.md)
- [dual-root pentagonal-bipyramid overlap closure](../results/hc7_order8_dual_root_contact_overlap_closure.md)
- [six-vertex source-rooted `K_4` lemma](../results/hc7_six_vertex_source_rooted_k4.md)
- [noncontacting incident-source fork](../results/hc7_order8_low_degree_incident_source_fork.md)
- [unified noncontacting incident-pair response](../results/hc7_order8_unified_incident_pair_normal_form.md)
- [exact conflict component and all-edge/unit response table](../results/hc7_order8_incident_bypass_conflict_split.md)
- [eight-latent-column spanning normalization](../results/hc7_order8_latent_column_spanning_normalization.md)
- [six-connected common deletion or strict exact-seven restart](../results/hc7_order8_incident_pair_common_deletion_connectivity.md)
- [conditional edge-maximal source-contact theorem](../results/hc7_order8_edge_maximal_source_contact.md)
- [generic exact-seven response restart](../results/hc7_generic_exact7_response_restart.md)
- [one-defect two-root completion or separation](../results/hc7_one_defect_two_root_k5_separator.md)
- [a local path need not split an intermediate column](../barriers/hc7_degree8_dirty_path_local_uncrossing_barrier.md)
- [six-connectivity and a centre-free path still do not split a singleton column](../barriers/hc7_pentagonal_bipyramid_target_star_shadow.md)
- [central Kempe normalization permits an arbitrary bipartite conflict graph](../barriers/hc7_incident_bypass_conflict_compression_barrier.md)
- [seven-connected planar column shadow](../barriers/hc7_seven_column_k2_planar_shadow.md)
- [contact maximization need not provide an improving transfer](hc7_pb_max_contact_nine_four_colour.md)
