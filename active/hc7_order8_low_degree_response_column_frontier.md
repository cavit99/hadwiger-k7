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

## 4. The low-degree branch has two different response modes

The seven labels of `J` consist of the target `t`, the five response sources
`c_0,...,c_4`, and one remaining nonresponse label `q`.

### 4.1 Exposed source--target noncontact

If

\[
                         tc_i\notin E(J)               \tag{4.1}
\]

for some `i`, the corresponding same-`(e,c)` path has the correct endpoint
labels.  A subpath from `c_i` to `t` whose interior avoids both roots and all
seven columns can be absorbed into one endpoint column, preserving every
old contact and adding `tc_i`.  This is the audited clean first-hit
augmentation.

If no such clean subpath exists, the first obstruction met by the path may
be a root or another column.  The missing step is a connected reassignment
that preserves both roots, all seven labels, all five prescribed first
neighbours and all old column contacts, or instead returns a terminal
minor, a common boundary partition or a strict literal-shore descent.

### 4.2 Source-saturated target

It is possible that

\[
                         tc_i\in E(J)
                         \quad(0\le i\le4).             \tag{4.2}
\]

Then none of the five named paths is aimed at a missing column contact.  A
low-degree source can already be adjacent to `t`, and all five response
paths can avoid the low-degree part of the system.

This is not repaired by the proposed lexicographic normalization.  At the
abstract contact-graph level, let

\[
                       H=K_2\vee\overline {K_4},
                       \qquad J=K_1\vee H,
\]

and let the outer universal vertex be `t`.  The graph `H` is a six-vertex
2-tree and `J` is edge-maximal `K_5`-minor-free.  Four vertices have degree
three, while `t` contacts all five chosen source labels.  The named paths
may already be single contact edges.  Contact count and coverage are then
maximal and the path-intersection count and path lengths are minimal.

The audited
[seven-column planar shadow](../barriers/hc7_seven_column_k2_planar_shadow.md)
realizes the same obstruction at host level in a seven-connected
`K_7`-minor-free graph.  That graph is six-colourable and has actual
order-seven exits, so it does not refute the full terminal disjunction.  It
does prove that the universal proper-minor rejection data or an equivalent
critical-host consequence must be used.

### 4.3 The low-degree label can be chosen as a source

The computer-assisted, audited
[six-vertex rooted `K_4` lemma](../results/hc7_six_vertex_source_rooted_k4.md)
gives a useful finite normalization in the source-saturated case.  If every
source had degree at least four, then after deleting `t` the five sources
would have degree at least three and the auxiliary vertex would have degree
at most three.  The lemma gives a `K_4` model whose four bags each contain a
source.  Adjoining `t` gives a `K_5` model in `J`, a contradiction.

Consequently (4.2) forces at least one response source `c_i` to have contact
degree at most three.  This is not response exposure: `c_i` is adjacent to
`t`, so its named path need not add a contact.

### 4.4 A noncontacting prescribed incident pair

The audited
[incident-source fork](../results/hc7_order8_low_degree_incident_source_fork.md)
spends that low degree without introducing a critical-triangle case.  Since
`c_i` already contacts `t`, it is nonadjacent to at least two other response
sources; choose one, `c_j`.  Their prescribed vertices `v_i,v_j` are
nonadjacent, and the incident edges `vv_i,vv_j` come from the original fixed
`(e,c)` response.

Simultaneously contracting those two incident edges gives one exact
colouring in which either one edge is bichromatically linked for all five
alternate colours, or there is a three-colour `v_i`--`v_j` bypass avoiding
`v` together with two coupled one-edge responses.  The original colouring
and the three contraction colourings give a common operation table on
`G-{e,vv_i,vv_j}`.  A clean bypass adds the missing column contact, so in a
contact-maximal system the bypass first meets a root or a third column.

The contraction colouring need not induce the original boundary partition.
The two surviving objects are therefore a universally bichromatically
saturated incident edge or a dirty root/column bypass, not a terminal
outcome.

## 5. Spanning and lexicographic normalizations

### 5.1 A maximum system spans the host

**Status:** written proof in this frontier; not separately audited.

Fix the initial two root seeds and roles and the seven column seeds,
including every prescribed vertex and label.  Allow any of the nine
connected sets to be enlarged while they remain pairwise disjoint, the
roots remain adjacent and each root remains adjacent to every column.  First
maximize the number of column contacts and then maximize the total number
of vertices in the nine sets.

This system spans `G`.  Indeed, let `Z` be a component outside the nine
sets and let `A` be the set of columns met by `Z`.  If `A` contains two
nonadjacent labels, a path through `Z` between the corresponding columns can
be absorbed into one of them.  It preserves all old data and adds a column
contact.  Its new contact graph remains `K_5`-minor-free, since otherwise
the two roots would lift it to a `K_7` minor.  This contradicts the first
maximization.

Hence `A` is a clique.  If `A` is nonempty, absorb all of `Z` into one
column in `A`; every other newly met column was already adjacent to it.  If
`A` is empty, connectedness of `G` makes `Z` adjacent to a root, and it can
be absorbed into that root.  Either operation preserves all required
contacts and increases total coverage, a contradiction.

Consequently a low-degree column is separated from its nonneighbour columns
by the union of the two roots and at most three neighbouring columns.  This
is a genuine host separation, but its boundary is a set of literal vertices
inside those connected subgraphs and can have unbounded order.  The
normalization therefore does not supply an exact-seven response or a strict
operated-shore descent.

### 5.2 What a lexicographic rank can and cannot do

For one fixed `e,c` and one fixed set of literal labels, an admissible column
system may be chosen lexicographically to

\[
 \left(
   |E(J)|,
   \left|\bigcup_sV(L_s)\right|,
   -d_{\rm old}(P),
   -|P|
 \right),                                                   \tag{5.1}
\]

where `d_old(P)` counts root or old-column occurrences on a selected
source--target path.  Finiteness of `G` makes this a valid normalization.

The rank does not create an exchange.  Maximizing contacts among realizable
same-operation systems is weaker than making `J` abstractly edge-maximal,
and (4.2) can leave no selected path to a missing contact.  Every claimed
rank improvement must therefore include a literal no-contact-loss
reassignment proof.

There is one useful conditional compression.  If `J` is abstractly
edge-maximal `K_5`-minor-free and (4.2) holds, then the two roots and columns
contain a `K_7` with one edge missing.  If `tq` is present, `J-t` is an
edge-maximal `K_4`-minor-free graph, hence a 2-tree containing `K_4` with one
edge missing.  If `tq` is absent, a `K_5` model in `J+tq` yields a `K_4`
model in `J-t`.  This model must use `q`, since otherwise adjoining the
target already gives a `K_5` model in `J`.  Its bag containing `q` must be
the singleton `{q}`: if it also contained a source vertex, that vertex would
restore the target contact and again give a `K_5` model in `J`.  In either
case `t` and four column bags form a `K_5` with at most one edge missing;
when `tq` is absent, that possible missing edge is incident with `q`.  The
roots complete a `K_7` with one edge missing.

The audited
[one-defect two-root completion/separation theorem](../results/hc7_one_defect_two_root_k5_separator.md)
then gives a `K_7` minor or a genuine full-neighbourhood separation, but the
separation can have unbounded order and need not preserve the selected
response.  This conditional compression is a written proof in this
frontier, not a separately audited or terminal result.

## 6. Exact open theorem

### Low-degree response-column composition theorem

In the setting of Sections 1--3, choose a free-root system satisfying
(3.1).  Prove at least one of:

1. an explicit `K_7`-minor model in `G`;
2. one complete equality partition of `S` extending through both closed
   shores;
3. an actual order-seven selected-response interface on a nonempty proper
   connected subset of `C` or `D`;
4. a strict order-eight response-side descent on a proper connected subset
   of the operated shore; or
5. for the same edge `e`, colouring `c`, root seeds and roles, seven labels,
   five first neighbours and target, a no-contact-loss reassignment which
   strictly improves a declared finite rank.

The proof has two separate obligations:

- **incident-source composition:** in the source-saturated configuration
  (4.2), close either the universally saturated incident edge or the dirty
  root/column bypass from Section 4.4 while retaining the common three-edge
  operation table and the fixed column labels;
- **first-obstruction exchange:** when (4.1) holds, handle both a first root
  encounter and a first old-column encounter without losing operation
  provenance.

An order-seven output is recursive only with the stated proper literal
shore decrease and named crossing-edge response.  A fresh response, an
unbounded separator or a new quotient contact system without a proved rank
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
- [generic exact-seven response restart](../results/hc7_generic_exact7_response_restart.md)
- [one-defect two-root completion or separation](../results/hc7_one_defect_two_root_k5_separator.md)
- [a local path need not split an intermediate column](../barriers/hc7_degree8_dirty_path_local_uncrossing_barrier.md)
- [seven-connected planar column shadow](../barriers/hc7_seven_column_k2_planar_shadow.md)
- [contact maximization need not provide an improving transfer](hc7_pb_max_contact_nine_four_colour.md)
