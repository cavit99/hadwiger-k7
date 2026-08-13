# Exceptional degree-eight vertices: live technical frontier

**Status:** active primary technical frontier for Norin--Totschnig
Conjecture 21.  The lower bound and the local neighbourhood,
exterior-completion, and two-component reductions in Sections 1--2 are
written and separately audited GREEN; the finite boundary claims have
retained independently checked verifiers.  The four-centre theorem and its
operation-coupled, tri-separation, trace-preserving, and generalized-wheel
leaf refinements in Section 4 are also separately audited GREEN.  The
Boolean minimum-separator linkage, the cyclic four-region elimination, and
the exact one-coordinate response language in Section 4 are separately
audited GREEN.  The removable-matching, replacement-abundance,
six-coordinate induced-forest, growth-or-feedback, bounded-feedback degree
elimination, six-centre feedback and portal-cycle threshold reductions are
separately audited GREEN.  The
matching common-state, large-boundary lock reduction, order-nine transition
projection and induced-path common-model theorems are separately audited
GREEN.  The selected-edge root-bag response theorem and the all-lock
branch-set transfer note with its precisely scoped route nonclosure are
separately audited GREEN.  The five-centre
two-cut response reduction and its terminal
order-five, order-six, and order-seven component cases are separately
audited GREEN.  The order-six case has independently checked DRAT
certificates; the order-seven case has an exact 149-orbit Z3 search and a
separate cold full rerun, with the absence of DRAT stated in its trust
boundary.  The universal four-boundary rooted-`K_4` theorem and the
unique-owner critical-completion minor-or-separator reduction are also
separately audited GREEN.  The boundary-first donor-gate theorem and its
scoped route nonclosure are separately audited GREEN.  The five-edge
common-host theorem, its signed four-crossing and omitted-coordinate
reductions, the two-shore rooted-minor theorem, the dense-branch visibility
theorem, and the palette-intersection barrier are separately audited GREEN,
while the list-core calculation in Section 3 remains a written live
derivation without a separate audit.  The upper bound is open.  This file
is not a second status ledger.

## 1. Primary target and exact finishing reduction

The primary target is:

> **Norin--Totschnig Conjecture 21.** Every graph with no `K_7^-` minor is
> six-colourable.

This is open and does not imply `HC_7`.

Let `G` satisfy

\[
 \kappa(G)\ge7,
 \qquad \chi(G)=7,
 \qquad \text{every proper minor of `G` is six-colourable},
 \qquad K_7^-\npreccurlyeq G.                              \tag{H}
\]

Call a degree-eight vertex exceptional when its neighbourhood is
`K_4`-free.  The audited
[degree-seven rooted-helper closure](../results/hc7_k7minus_degree7_rooted_helper_closure.md)
now gives

\[
 n_7=0,\qquad G\text{ contains no literal }K_5,
 \qquad b=n_8\ge25+\sum_{i\ge10}(i-9)n_i.               \tag{1}
\]

where `b` is the number of exceptional vertices; write `tau` for the
displayed sum.  Therefore the theorem

> every graph satisfying (H) has at most 24 exceptional vertices

would prove Conjecture 21.  It is a headline-equivalent finishing theorem,
not a routine intermediate lemma.

The audited rooted-helper closure also proves `delta(G)>=8` and `m>=4n`.
Thus the former positive-degree-seven and literal-clique branches, the exact
`b=7` layer, and all two-clique tight layers are excluded.

The audited
[independence-four elimination](../results/hc7_k7minus_alpha4_regular_ramsey_elimination.md)
adds a terminal global branch closure.  A 505-case incidence enumeration,
reduced to 40 symmetry classes, and independently checked DRAT
refutations prove that no 25-vertex 8-regular graph has independence number
four and clique number at most four.  The accompanying written reduction
shows that `alpha(G[B])=4` would force the entire host to be such a graph.
Since `R(4,5)=25`, (1) and the absence of a literal `K_5` now give

\[
             \alpha(G[B])\ge5.                         \tag{1.1}
\]

Thus five independent exceptional centres are available simultaneously.

## 2. What the present attack proved

The new
[exceptional-neighbourhood and exterior-completion theorem](../results/hc7_k7minus_exceptional_neighbourhood_completion.md)
proves two facts.

1. Every exceptional vertex `u` has `alpha(G[N(u)])=3`.  Thus every one of
   the at least 25 centres has an independent triple; the former
   independence-number-two branch is absent.
2. For an independent triple `I\subseteq N(u)` and
   `R=N(u)-I`, any `R`-rooted `K_5` model in `G-({u}\cup I)` that avoids an
   exterior component completes immediately to a `K_7^-` model.

The audited
[low-degree exterior-component theorem](../results/hc7_low_degree_exterior_component_bounds.md)
gives at most two components of `G-N[u]`.
Consequently every surviving rooted model is bilateral when there are two
components.  In the one-component case every residual connected subgraph
outside the rooted bags either has no neighbour in `I` or contacts at most
three of the five bags.

These are positive host-level reductions.  They do not yet coordinate six
or seven different centres.

The earlier focused two-component attack has a compatible local
consequence.  The
[two-component literal-clique exclusion](../results/hc7_k7minus_one_nonfull_k5_and_nested_cut.md)
proves that if even one exceptional centre `u` has two exterior components,
then the whole graph contains no literal `K_5`.  The proof links any
hypothetical clique to five of the at least six neighbourhood vertices met
by both components and completes those five branch sets with `\{u\}` and
the opposite component.  The rooted-helper closure now supplies its former
conclusion globally, whether the exterior is connected or not:

\[
 n_7=0,\qquad \delta(G)\ge8,\qquad |E(G)|\ge4|V(G)|,
 \qquad n_8\ge25+\sum_{i\ge10}(i-9)n_i.                \tag{2}
\]

Every degree-eight vertex is therefore exceptional and `|V(G)|\ge25`.
There is no longer a positive-degree-seven side of the dichotomy.  The
remaining connectivity target lies entirely in the branch described by
(2), with at least 25 exceptional centres available simultaneously.

The earlier
[nonfull-attachment theorem](../results/hc7_k7minus_nonfull_attachment_reduction.md)
proves that two exterior components cannot miss the same neighbour of `u`.
If exactly one component is nonfull, deleting its unique missed neighbour
from `X=N(u)` gives an order-seven cut with connected-subgraph packing
vector exactly `(1,2)`.  Its boundary has independence number three, at
most nine edges, connectivity at most three, no `K_5` minor, no vertex
deletion with a `K_4^-` minor, and no robust independent triple.  The
audited uniform defect-two connected-subgraph reflection theorem forces the
missed vertex to have at most four neighbours on that boundary and at least
two neighbours entering the full exterior component.  A retained exact
census leaves 28 possible seven-vertex boundary types.

The new theorem goes further in this one-nonfull case.  It forces a six-fan
from the missed vertex to the seven-vertex boundary, and every such fan
meets every boundary-full connected subgraph of the full exterior
component.  For any fixed full connected subgraph, a tight failed
allocation produces two overlapping order-seven cuts; the remaining cases
are the non-tight attachment inequality `|A|+|B|\ge7` and the exact nested
packing-`(1,1)` or packing-`(1,2)` cuts.  The
[two-entrance barrier](../barriers/hc7_k7minus_nonfull_two_entrance_allocation_barrier.md)
shows why the two known entrance vertices alone cannot split off the third
connected subgraph; its witness contains an explicit `K_7`-minor model and
is only five-chromatic, so it does not refute the critical-host conclusion.

When the two components have distinct nonadjacent misses, the
[contracted-star and fan-tree theorem](../results/hc7_k7minus_distinct_miss_fan_tree_elimination.md)
now eliminates the complete branch.  A star-contraction colouring and one
Kempe response force the common six-set to have independence number at most
two, dynamically excluding the exact `3K_2` parity obstruction and every
other independence-three boundary.  The common boundary is then two
disjoint triangles, with at most one joining edge.  Six-fans in `G-u`
produce marked trees inside the two arbitrary exterior components, and the
retained finite completion constructs an explicit `K_7^-` model for every
portal-mask and labelled-tree configuration.  The earlier parity-language
barrier remains a valid warning about static trace coverage, but is no
longer a live obstruction.

In the both-full case, the
[boundary reduction](../results/hc7_k7minus_both_full_shore_reduction.md)
starts with all 2,076 exceptional order-eight neighbourhoods.  An
unbounded diamond-deletion lift leaves 15 boundary types; the audited
three-full-component theorem removes eight, leaving seven exact graph6
types.  No surviving exterior component contains two vertex-disjoint
connected subgraphs that are each adjacent to every vertex of `X`; this
holds for all three components `\{u\},E,F`.  For the reserve types with six or seven
missing root adjacencies, every fixed star-contraction colouring still
supports at least two demands through each side; concentrating all but one
demand in one side would already give a rooted `K_5^-` and hence a
`K_7^-` model.  The
[scoped static barriers](../barriers/hc7_k7minus_shore_allocation_barrier.md)
show that boundary counting, fullness, and independent-triple rotation do
not by themselves force that concentration.

Two census claims must not be confused with this promoted reduction.  A
[deterministic Rolek--Song matching-augmentation screen](hc7_k7minus_degree8_rolek_matching_nonclosure_verify.py)
closes 773 of the 2,076 exceptional boundaries but leaves 1,303, including
all seven promoted both-full types.  The published disjoint-path input and
the branch-set lift are sound; the first unsupported inference was treating
these 1,303 matching failures as the seven output by the independent
diamond-deletion and clique-odd-cycle-transversal filters.  This is a
computer-assisted finite route nonclosure, not an unbounded theorem.  A
separate provisional list of “197 one-full survivors” has no retained
defining predicate, digest, verifier, audit, or manifest entry and is not
part of the proof spine.

### Current operation-coupled connectivity attack

The proposed theorem that `G-N[u]` is connected for every exceptional
degree-eight vertex remains open.  The critical host is now unconditionally
in the `n_7=0`, literal-`K_5`-free branch.  Within that branch, the current
attack gives several unbounded reductions; none is an isolated graph-code
elimination.

1. In the one-nonfull case, the
   [shore-localized edge response](hc7_k7minus_one_nonfull_nondouble_palette.md)
   proves, conditional on the established computer-assisted bound
   `|N_S(x)|<=4`, that `ux` is non-double-critical.  One fixed colouring of
   `G-ux` supplies all five two-colour `u`--`x` paths inside the joined
   shore.  In the five-core alternative, `K_7^-` exclusion forces two
   adjacent model branch sets wholly into that shore.  What is missing is a
   label-preserving way to make those sets boundary-full, or an actual
   order-seven separation when that enlargement fails.
2. For distinct adjacent misses `x,y`, the
   [fixed-response path and descent theorem](hc7_k7minus_adjacent_miss_operation_descent.md)
   proves that `xy` is non-double-critical.  One colouring of `G-xy`
   yields four internally disjoint operated `x`--`y` paths, together with
   `xuy`, and full six-fans on both shores retaining the four operated first
   edges.  The residual graph `G-{u,x,y}` is four-connected and nonplanar,
   so any four nominated path hits root a `K_4` model.  The point-rooted
   model may meet foreign operated paths; a set-rooted absorption theorem,
   or an exact operation-labelled seven-separation when absorption fails,
   is still required.
3. In the both-full case, the
   [rooted-diamond alternative](hc7_k7minus_both_full_diamond_or_exact7.md)
   converts two disjoint near-full connected supports into an explicit
   `K_7^-` model or a strict actual order-seven separation in the opposite
   shore.  Independently, the
   [whole-component contraction dichotomy](hc7_k7minus_both_full_component_contraction_dichotomy.md)
   puts one proper contraction above `4n-6`; it either yields a
   `K_7^\vee` model by Norin--Totschnig or has an exact cutvertex-block
   structure.  The open residues are the construction of a rooted
   `K_7^-`-minor model from the unrooted near model while retaining the
   named roots, and the wide cutvertex-block case.
4. Globally, choose a smallest component `E` among all disconnected
   exceptional anti-neighbourhoods.  The audited
   [full-side vertex exclusion](../results/hc7_k7minus_one_nonfull_full_vertex_exclusion.md)
   proves that every degree-eight vertex of `E` has connected
   anti-neighbourhood.  Indeed, the only possible recentering would make
   that vertex adjacent to all seven common boundary vertices inside the
   full exterior component.  The one-nonfull nested-cut theorem then gives
   simultaneously at most four and at least five boundary contacts; its
   defect-two reflection supplies a six-colouring.  This eliminates the
   complete exact order-seven/eight matching-core rotation, not merely one
   boundary graph.  It still does not eliminate the originally selected
   disconnected centre `u`, since `E` may contain no degree-eight vertex or
   only degree-eight vertices with connected anti-neighbourhoods.
5. The
   [degree-eight pair-deletion reduction](hc7_k7minus_pair_deletion_k7vee_reduction.md)
   uses the full density jump rather than one local attachment pattern.  For
   any two degree-eight vertices `a,b`, the graph `G-{a,b}` is
   five-connected and lies at or above the Norin--Totschnig `4n-8`
   threshold, so it has a spanning `K_7^\vee` model.  Target exclusion
   sharply restricts how the two retained roots meet its seven branch sets,
   and absorbing the deficient branch set gives a spanning `K_6` model with
   at most four contacts per root.  For a globally minimum surplus donor
   over all root-contact-maximal spanning `K_6` models, every donor--target
   portal belongs to every connected core retaining the root and four
   protected adjacencies; all but at most four such portals are donor
   cutvertices.  One fixed edge deletion gives
   five colour-indexed Kempe paths, but their colours have not been aligned
   with the target and owner branch-set labels.  Closing the residue still
   requires that operation-to-recipient allocation, or a returned separation
   whose boundary is literally the neighbourhood of a named exceptional
   degree-eight vertex.  In the exact `2+2` root-removal split, the thick
   two-owner side now collapses to one literal portal vertex.  The remaining
   vertices on that side and the complementary labelled side are connected,
   anticomplete, and both adjacent to the same two nonadjacent boundary
   vertices.  Two proper-minor colourings therefore glue across that
   boundary and six-colour `G`.  This eliminates the entire `2+2`
   root-removal residue.  In the connected two-loss case, the same
   two-owner argument eliminates every nonconcentrated residue by a two-cut
   contradiction or a two-boundary six-colouring; only the atomic bag
   `R={r,s}` with a `2+2` split of the universal adjacencies can survive.

   More generally, the audited
   [exact spanning-`K_7^\vee` separator dichotomy](../results/hc7_k7minus_exact_k7vee_separator_dichotomy.md)
   bypasses the remaining root-removal forms at the model level.  The fixed
   two-edge response either gives an explicit `K_7^-` model or preserves
   its named colouring on an actual nested separator `N_G(Y)` of order at
   least seven, where `Y` is a nonempty proper connected part of one
   universal bag and its complement in that bag remains connected.  This
   is nonterminal: the separator may have order greater than seven, the two
   deleted endpoints need not lie on opposite open shores, and the boundary
   need not be `N_G(z)` for a named exceptional vertex.
6. In the exact packing-`(1,2)` branch, the
   [three-full-subgraph completion theorem](../results/hc7_k7minus_exact7_three_full_subgraph_completion.md)
   exactly characterizes the `K_7^-` models visible after contracting the
   three full connected subgraphs.  The new
   [multiple-missing-adjacency dichotomy](../results/hc7_k7minus_multiple_missing_adjacencies_separator_dichotomy.md)
   removes the remaining contact count in the `2+1+1+3` response: every
   complete operated `x`--`y` support disjoint from the two rich full
   subgraphs gives either an explicit `K_7^-` model or an actual nested
   separator, even when it meets none of the retained boundary triangle.
   In the `3+1+1+2` response the same conclusion holds when either operated
   support meets both ends of the retained boundary edge.  The crossed
   one-miss-at-each orientation remains open.

   This is an unbounded structural reduction, but its separator is not a
   terminal: its boundary may have order greater than seven, need not equal
   `N_G(z)` for an exceptional vertex, and need not carry a legal trace of
   the fixed colouring.  The direct-entry case can also put every complete
   support through one of the retained full subgraphs.  Thus the surviving
   problem is operation-labelled support detachment and separator
   terminalization, not a missing boundary-contact estimate.

   Deleting an internal edge of a connected subgraph realizing the original
   boundary partition was also tested.  Its five bichromatic bypasses are
   labelled by the new edge response, whereas the three required connected
   subgraphs are labelled by the original proper-minor response.  No proved
   transition aligns those partitions; identifying the bypass colours with
   the old boundary blocks is the first unsupported inference.  This does
   not refute a dynamic split.  The smallest repair is a two-operation
   trace-alignment theorem producing a complete detached support, a common
   boundary partition, `K_7^-`, or `N_G(z)` with a smaller exceptional
   anti-neighbourhood component.

The same note gives a global one-root strengthening.  For every exceptional
`r`, the bounds `m>=4n` and `b>=25` put the six-connected graph `G-r`
strictly above the same extremal threshold.  Thus `G-r` has an exact
spanning `K_7^\vee` model, and the optimized forced-interface theorem
applies at every exceptional centre.  Spanning contact-maximal `K_6` models
in `G-r` already occur in the archive; the extra near-clique labels and
their compatibility with the optimized model remain unspent.

## 3. Seven-root list reduction

**Status:** written live derivation; not separately audited or promoted to
`results/`.

Choose any seven exceptional vertices and call their set `B`.  Six-colour
`G-B` with a colouring `phi`.  Put `H=G[B]`; the degree-defect theorem gives
that `H` is `K_5`-free.  For each `v\in B`, let

\[
 \begin{aligned}
 E_v&=N(v)-B,\\
 \rho(v)&=|E_v|-|\phi(E_v)|,\\
 L(v)&=[6]-\phi(E_v).
 \end{aligned}                                           \tag{3}
\]

Then `G[B]` is not `L`-colourable; otherwise the colouring extends to all
of `G`.  Since `|E_v|=8-d_H(v)`, the exact list identity is

\[
                         |L(v)|=d_H(v)+\rho(v)-2.         \tag{4}
\]

Let `C\subseteq B` be inclusion-minimal such that `G[C]` is not colourable
from the restricted lists.  It is connected, since otherwise minimality
colours each component separately.  Colouring `C-v` and then attempting to
extend at `v` also gives `d_{H[C]}(v)>=|L(v)|`.  For `v\in C`, define

\[
 c(v)=|N_H(v)-C|,
 \qquad
 \varepsilon(v)=d_{H[C]}(v)-|L(v)|.                     \tag{5}
\]

Minimality gives `\varepsilon(v)>=0`, and substitution in (4) gives the
exact budget

\[
                  \boxed{c(v)+\rho(v)+\varepsilon(v)=2}
                  \qquad(v\in C).                        \tag{6}
\]

Thus each core vertex has exactly two units divided among contacts with the
other exceptional vertices, repeated exterior colours, and list-degree
excess.  For the tight set

\[
                         T=\{v\in C:\varepsilon(v)=0\},
\]

the graph `H[T]` is a Gallai forest.  Indeed, after colouring outside a
block `Q`, each vertex of `Q` retains at least `d_Q(v)` colours.  The
Borodin--Erdos--Rubin--Taylor degree-choosability theorem forces `Q` to be a
complete graph or an odd cycle; `K_5`-freeness bounds the complete blocks by
`K_4`.  This is the same audited argument as Theorem 2.1(4) of
[`hc7_boundary_list_critical_transfer.md`](../results/hc7_boundary_list_critical_transfer.md).

It does not finish.  The explicit
[`C_7\vee C_6` mechanism barrier](../barriers/hc7_k7minus_seven_root_list_count_barrier.md)
has seven exceptional degree-eight vertices and is eight-connected.  One
colouring of the `C_6` produces empty lists and singleton cores; another
produces the tight odd-cycle core `C=B=C_7` with common list `\{1,2\}`.
The witness is only five-chromatic and is not a counterexample to (H), but
it shows that one fixed boundary colouring cannot close the theorem.

There is, however, genuine adaptive information.  For each `x\in B`, a
six-colouring of the proper minor `G-x` restricts to a colouring of `G-B`
for which `H-x` is list-colourable but `H` is not.  Consequently every
minimal core for that response contains `x`.  The seven anchored cores may
differ; synchronizing them is the exact multi-centre colouring target.

## 4. Current global finishing obstruction

**Status of the four-centre reduction:** the promoted theorem and the
refinements cited in this section have separate GREEN internal audits.  The
theorem forcing either the required rooted minor or a strict
trace-preserving exact-cut descent remains open.

Choose five independent exceptional vertices `Z`.  For any four-set
`U subset Z`, put `H=G-U`.  Then `H` is
three-connected, nonplanar and exactly six-chromatic.  Fix `r in U`, a
six-colouring of `G-r`, and four colours occurring once on `N(r)`, with
literal representatives `x_1,x_2,x_3,x_4 in H`.  The promoted theorem gives
exactly one of two outcomes:

1. `H` contains an `\{x_1,x_2,x_3,x_4\}`-rooted `K_4` model.  Together
   with `r` this is a fixed-colouring-anchored `K_5` model avoiding the
   other three centres.
2. `H` is contained in a rooted web and returns a three-set `T` and two full
   components `C,D` of `G-(U dotcup T)`.  Thus `U dotcup T` is an actual
   order-seven cut.  The set `T` is not a literal triangle.  One closed
   shore retains a proper six-colouring after restoring `r`, and an
   alternating linkage forced by the web uses another named centre in
   `U-r`.

The fifth centre also gives a separate reduction before choosing a
four-set.  Put `F=G-Z`.  The audited
[five-centre two-cut theorem](../results/hc7_k7minus_five_centre_two_cut_reduction.md)
proves that any two-cut `{p,q}` of `F` lifts to the exact boundary

\[
                         S=Z\mathbin{\dot\cup}\{p,q\}
\]

with exactly two full complementary components and with `pq` absent but a
centre--pole edge present.  Their permitted boundary responses are opposite
singletons.  Orient the components so that `C` accepts only `p=q` and `D`
only `p!=q`.  Then

\[
 \chi(G[C])\ge4,\qquad \chi(G[D])\ge5,\qquad
 \mu_S(C)=1,
\]

the rooted graph `(G[C union S],Z,p,q)` is infeasible, and

\[
 e(G[C])+e_G(C,S)\le6|C|+1,\qquad
 e(G[C])\ge2|C|-1,\qquad |C|\ge8.
\]

The equality side contains four colour-distinguished `p`--`q` paths arising
from a critical edge, while every permitted colouring of the distinct side
contains a bichromatic `p`--`q` path.  The separately audited
[order-five component theorem](../results/hc7_k7minus_order_seven_k5minus_component_elimination.md)
is terminal: if `|C|=5`, the degree bound forces `G[C]=K_5^-` and an
explicit `K_7^-` model.  The separately audited
[order-six finite incidence theorem](../results/hc7_k7minus_order_six_equality_shore_elimination.md)
constructs the same forbidden minor for `|C|=6`; its ten complement-orbit
formulas have independently checked DRAT refutations.  The separately
audited
[order-seven allocation theorem](../results/hc7_k7minus_order_seven_equality_shore_elimination.md)
contracts one core edge and assigns six distinct boundary vertices so that
the resulting six bags miss at most one adjacency.  Its exact 149-orbit
search and cold full rerun close `|C|=7`.  Thus only equality shores of order
at least eight remain in the two-cut branch.

The audited unbounded attack on those larger shores has the following exact
hierarchy.

1. If a centre has one contact on a shore, the
   [singleton shift](hc7_k7minus_five_centre_singleton_shift.md) produces six
   equality-shore arms.  A `K_5^-` minor in their contact graph completes an
   explicit `K_7^-` model by the audited
   [six-arm criterion](hc7_k7minus_five_centre_singleton_six_arm_completion.md).
   The current scalar inequalities do not force that contact minor.
2. With no singleton contact, a minimal bad-root set of order three is
   eliminated by
   [contraction-colouring gluing](hc7_k7minus_five_centre_t3_palette_gluing.md).
   Order four has the audited
   [atom/exchange trichotomy](hc7_k7minus_five_centre_t4_atom_exchange.md):
   high contacts on `C`, the unbounded density threshold
   `e(C)>=3|C|-2`, or a forced induced-path contact table.  None of the
   three outcomes is terminal yet.
3. At order five, the
   [global palette theorem](hc7_k7minus_five_centre_t5_global_palette.md)
   and the audited
   [critical-completion elimination](hc7_k7minus_five_centre_critical_completion_nested_cut.md)
   force all five `D`-contact sets to be rainbow triangles in one fixed
   colouring.  The audited
   [atom-slack theorem](hc7_k7minus_five_centre_t5_atom_slack.md) gives
   `|C|>=15`; the audited
   [crossed-overlap theorem](hc7_k7minus_five_centre_t5_atom_overlap_budget.md)
   can expose an exact order-seven cut, but the general all-rainbow row
   remains open.  In its `b=2` subcase, the
   common-hole and rooted-model reductions localize the missing composition
   to a split inside a concentrated model bag.

The supporting audited chain is also part of this laboratory.  In the
all-rainbow row it consists of the
[common-triangle reduction](hc7_k7minus_five_centre_common_rainbow_triangle_elimination.md),
the [synchronized-path theorem](hc7_k7minus_five_centre_distance_one_paths.md),
the [common-component simultaneity barrier](../barriers/hc7_all_rainbow_common_components_multiroot_barrier.md),
the [rooted `K_{1,1,3}` scheme reduction](hc7_k7minus_five_centre_rolek_scheme_reduction.md)
and its exact
[second-triangle reservation barrier](../barriers/hc7_k113_second_triangle_reservation_barrier.md),
the [shore-confined rooted-`K_5` theorem](hc7_k7minus_five_centre_rainbow_triangle_rooted_k5.md),
and the [private-contact theorem](hc7_k7minus_five_centre_two_private_contacts.md).
For `b=2`, the live chain is the
[Hall-rectangle reduction](hc7_k7minus_five_centre_b2_rectangle_locks.md),
[common-hole transition](hc7_k7minus_five_centre_b2_common_hole_transition.md),
[four-colour projection](hc7_k7minus_five_centre_b2_four_colour_projection.md),
[pairwise Kempe-contact theorem](hc7_k7minus_five_centre_b2_pairwise_kempe_touch.md),
[stable-bag concentration](hc7_k7minus_five_centre_b2_stable_bag_concentration.md),
and the [terminal bag-split criterion](hc7_k7minus_five_centre_b2_model_bag_split.md).

An independent completion argument gives a second unbounded reduction.
Contract `D union Z` to `x` and add the absent edge `pq`.  The resulting
proper completion is seven-chromatic.  The audited
[model lift](hc7_k7minus_five_centre_completion_model_lift.md) makes every
distinct-pole placement terminal and reduces the same-bag placement to a
spanning model

\[
                         B,\{x\},R_1,\ldots,R_5,
\]

where `B` contains both poles, the sole model nonedge is `R_aR_b`, and
\(N_G(R_i)\cap Z=\{z_i\}\) after relabelling.  Splitting `B-pq` gives exactly
three pole-incidence codes and at least three opposite-side-deficient
owners.

The promoted
[four-boundary rooted-`K_4` theorem](../results/hc7_k7minus_five_centre_universal_boundary_rooted_k4.md)
holds simultaneously at the level of existence: every four-set in
\(S=Z\mathbin{\dot\cup}\{p,q\}\) roots a `K_4` on the closed `D`-shore.
Using the roots `p,q,z_a,z_b` repairs the artificial pole edge and the owner
nonedge in one spanning seven-bag model.  The audited
[near-clique donor reduction](hc7_k7minus_five_centre_owner_nonedge_connector.md)
then removes every pole-incidence and deficiency-pattern exception: either
`G` contains a `K_7^-` minor, or some nonempty proper connected set `Y` has
connected complement in its model bag and `N_G(Y)` is an actual separator
of order at least seven.

In a target-free host only the separator outcome survives.  It is not yet
a legal descent.  Its order has no upper bound, it need not contain the five
centres, and no equality/distinct boundary response is retained.  Indeed,
if `Y` lies in an ordinary owner bag \(R_i\cup\{z_i\}\), then unique ownership
gives \(N_G(Y)\cap Z\subseteq\{z_i\}\).  The original `pq` completion also
cannot instantiate the existing partition-reflection theorem: it supplies a
response on the original boundary `S`, not an opposite-shore proper
operation realizing the same labelled partition on the new literal
separator.  This quantifier mismatch is the exact nonclosure, not a missing
quotient case.

The exact-order-seven subcase has one further consequence.  If
`T=N_G(Y)` has order seven, every component of `G-T` is `T`-full and
`G[T]` has no `K_5` minor: a `K_5` model in `T`, together with any two
components of `G-T`, would be a `K_7^-` model.  Hence `G[T]` is
four-colourable.  Contracting a full component together with any prescribed
nonempty independent set in `T` shows that each of the two grouped shore
languages meets every exact-block cylinder.  The audited
[split-boundary synchronization theorem](../results/hc7_split_boundary_synchronization.md)
therefore forces every surviving such `G[T]` to be nonsplit.  This is still
nonterminal: nonsplit boundaries admit the sharp abstract parity separation
of the two response languages.

The separately audited
[boundary-first donor-gate theorem](hc7_k7minus_five_centre_minimal_donor_gate.md)
now makes the limit of ordinary-donor relocation exact.  A vertex-minimal
fixed-trace core either fills the whole donor or exposes a smaller
donor-eligible set.  In a comparison class closed under that replacement,
the smaller set has strictly larger open neighbourhood and may lose the
trace; without closure there is no lexicographic comparison.  Replacing
the donor by a co-connected singleton does not repair this: its degree can
exceed the old separator order, so it is worse in the first lexicographic
coordinate.

If the comparison class is broadened from labelled gate donors to all
geometric model donors, the ordinary bags
`U_i=R_i union {z_i}` do supply the singleton candidates `{z_i}`.  The
minimum boundary is then seven or eight; in the order-eight case the second
coordinate forces a degree-eight singleton.  This recovers the familiar
separator `N_G(v)`, but not the model trace: its singleton shore uses at
most five boundary colours, whereas every six-colouring of `G-v` uses all
six on `N_G(v)`.  Restricting the class retains the labelled model and
operation data but loses the bound; broadening it recovers the bound but
does not preserve those data as an invariant.  This quantifier fork is the
decisive nonclosure of the proposed gate.

The proposed single-edge
[paired-donor continuation](hc7_k7minus_five_centre_paired_donor_gate.md)
has now been run as well.  If one colouring of `G-e` gives a genuine
accepted-exterior/rejected-interior trace at each of two disjoint donors,
the donors contain the two ends of `e`.  Their traces are therefore
restrictions of one literal colouring, and their joint boundary satisfies

\[
 |N(Y_1\cup Y_2)|=|N(Y_1)|+|N(Y_2)|
  -|N(Y_1)\cap N(Y_2)|-|N(Y_1)\cap Y_2|-|N(Y_2)\cap Y_1|.
\]

With lists kept on that fixed joint boundary, every minimal joint
list-critical core contains both ends of `e`.  A compatible pair supplied
inside the spanning near-clique would give an explicit `K_7^-` minor or an
actual joint separator retaining this one response.

The supply step is absent.  The unique-owner theorem gives one donor; its
two canonical simultaneous pieces lie in one bag and need not be adjacent,
have a connected joint complement, or share a far bag.  An arbitrary
interbag edge need not have ends in donor-eligible pieces retaining the
named duties, and its deletion colouring need not induce the old `pq`
partition.  Joint minimisation does not repair this: a proper
operation-preserving core hull either leaves the fixed comparison class or
creates a new boundary vertex in the discarded part of the same bag which
is anticomplete to the other donor.

The explicit
[paired-overlap barrier](../barriers/hc7_k7minus_paired_donor_overlap_barrier.md)
shows that the hoped-for local overlap inference is false even with two
order-seven rejected traces, overlap of order five, one cross-edge, and
five protected contacts on each smaller donor.  A width-four tree
decomposition excludes `K_7^-`, while both boundaries inflate to order
eight, lose their traces, and leave the joint trace rejected.  The witness
is only three-connected and four-chromatic; it does not refute a full
host-level supply theorem.  It does rule out overlap-weighted minimisation
as the missing engine.

Accordingly both the one-donor gate and its single-edge paired variant are
frozen.  The audited
[two-edge response reduction](hc7_k7minus_five_centre_two_edge_response_reduction.md)
tests the sole natural multi-edge extension.  Under one fixed deletion
colouring, two disjoint sets carry genuine traces exactly when every
monochromatic deleted edge crosses between them; three disjoint sets cannot
all carry such traces.  In the equality completion, contracting either or
both of two suitable edges gives exactly one of three patterns: a singleton
pole-response flip, a genuinely joint double flip, or three stable
seven-chromatic completions containing `K_7^-` models with the corresponding
co-bagging.  The double operation retains the literal boundary partition
`Z|{p}|{q}`, but no theorem supplies the required edge pair or lifts every
stable same-pole-bag model.  The bounded test therefore stops there.

At the exact-seven backup, the remaining issue is likewise literal label
capture: to invoke minimum-side descent one must recover a boundary
`Z union {r,s}` and make the new proper subcomponent the equality-response
side.  Fullness, nonsplitness and further boundary queries do not supply
that orientation.

The second outcome cannot occur when `G` is eight-connected.  When
`kappa(G)=7`, the exact lift-order function on separations of `H` is symmetric
and submodular.  For fixed opposite anchors, its minimum separations form an
exact meet/join lattice.  If three cuts have all eight sign regions nonempty,
each centre has exactly one neighbour in every region; four cuts cannot have
all sixteen sign regions nonempty.

The exhaustive three-connected branch was opened through the audited
[global five-centre rotation
reduction](../results/hc7_k7minus_five_centre_rotation_reduction.md).  The common core
`F=G-Z` is nonplanar and exactly six-chromatic.  Every six-colouring of `F`
saturates at least one centre, and a colouring of `G-r` restricts to a
colouring of `F` whose saturation set is exactly `{r}`.  These five
singleton sets are invariant under colour permutation.

For each ordered pair of distinct centres, the four-centre theorem applies
on `F+z_i`, giving twenty labelled applications.  A web outcome returns a
two-cut immediately or an order-three separation crossed by the four
non-omitted centres.  Two anchor-compatible web separations uncross to an
order-two/order-four pair if their omitted labels cross the same corner,
and otherwise to an order-three/order-three label rotation.  If no
orientation has compatible anchors, an original exact-cut component has
order three or four.

At one fixed root, either two selected shores share the same literal
extension vertex and colour, or the four web cuts have the exact form

\[
 N_G(C_i)=(Z-\{z_i\})\mathbin{\dot\cup}(X-\{x_i\}).
\]

The maximal packet is no longer a three-connected obstruction.  At least
two omitted centres lie in their own selected components, and the meet of
those two exact separations has boundary

\[
                         Z\mathbin{\dot\cup}(X-\{x_i,x_j\}).
\]

It returns a two-cut of `F`.  On one closed shore the same literal colouring
extends over the fixed root with either of the two distinct colours of
`x_i,x_j`.  The corresponding colourings of `G-rx_i` and `G-rx_j` agree
on `G-r` and give opposite singleton signatures.  For
`theta=phi_r|F`, put

\[
 L_z=[6]\setminus\theta(N_G(z))\qquad(z\in Z-\{r\}).
\]

One operation normalizes to the standard distinct response exactly when

\[
 \{\theta(x_i),\theta(x_j)\}\cap\bigcap_{z\ne r}L_z
                         \ne\varnothing.
\]

Hence every fixed-root packet in the three-connected branch has a
rooted-model outcome or two web shores sharing one literal extension vertex
and colour.  The separately audited
[palette-intersection barrier](../barriers/hc7_k7minus_five_rotation_palette_intersection_barrier.md)
shows that the five singleton-saturation rows alone do not force the
displayed common missing colour or its common-partition fallback.  It is a
palette-level barrier, not a critical-host counterexample.

### Six-coordinate induced-forest route: principal structural laboratory (paused)

The audited
[replacement-abundance theorem](../results/hc7_k7minus_removable_matching_rotation_abundance.md)
and [induced-forest reduction](../results/hc7_k7minus_six_coordinate_forest_reduction.md)
consume the removable-matching entrance below.  They force a six-edge
componentwise-induced forest

\[
 F\cong6K_2\quad\hbox{or}\quad4K_2\mathbin{\dot\cup}P_3,
 \qquad X=G-F,                                      \tag{4.F1}
\]

such that `X` is six-connected and both of two distinguished one-edge
restorations are seven-connected.  The proper six-colourings of `X`
realise every nonempty signature on `F`; `X` has a spanning exact
`K_7^vee` model; and one literal cycle of `G` contains all six forest
edges.  The five-edge star from the first replacement fork is absorbed by
the induced `P_3`, using the global exclusion of a literal `K_5`.

If `kappa(X)=6`, every six-cut has exactly two full complementary
components and both distinguished edges cross them.  The audited
[complementary-cube lift](../results/hc7_k7minus_six_cut_complementary_cube_lift.md)
turns every nonsingleton crossing row into an actual separator of order
eight through twelve.  The audited
[coordinate-localisation theorem](../results/hc7_k7minus_six_cut_coordinate_localisation.md)
then sends each selected coordinate to a strict response-bearing separator
or to a full component.  A full fallback has a `K_5`-minor-free,
four-colourable, nonsplit boundary; boundary order at least ten gives a
fresh strict singleton response.  Thus excluding all strict responses
leaves only a boundary `T` of order eight or nine with exactly two or three
full components.  In the three-component case `chi(G[T])` is three or
four.  The explicit
[three-component barrier](../barriers/hc7_k7minus_three_full_component_partition_barrier.md)
shows that fullness and ordinary boundary colouring alone do not force the
adjacent-pair partition needed for four-colour gluing.

The two forest types now admit separate common-host reductions.

For `F=6K_2`, only three matching edges cross and `|T|=9`.  Choose the two
distinguished restorers, which enter opposite open sides.  The audited
[matching common-state theorem](../results/hc7_k7minus_matching_square_common_state.md)
puts all three nonempty two-edge signatures on one common six-chromatic
double deletion, and one spanning `K_6` model co-bags both endpoint pairs.
After responses of order at most eight are excluded, the common deletion is
seven-connected and has an exact spanning `K_7^vee` model.  An unlocked
palette gives two crossed Kempe components and an actual response
separator; the both-dominating alternative gives an explicit `K_7` minor.

The audited
[selected-edge root-bag response theorem](../results/hc7_k7minus_selected_edge_root_bag_response.md)
splits the co-bagged root along the selected equality edge.  It gives
`K_7^-` or an actual separator retaining that edge, the common model split
and the boundary partition rejected by the intact shore.  Its order is at
least seven.  The
[boundary-reduction theorem](../results/hc7_k7minus_matching_lock_boundary_reduction.md)
strictly reduces every actual boundary of order at least ten numerically by
a fresh singleton response and iterates to order seven, eight or nine; the
original matching and model labels need not survive.  At a new
order-nine singleton it either returns order at most eight or the sharp
full-component degree-nine pole.  If every palette is locked, each lock
component either gives one of these endpoints or is connected, dominating
and three-chromatic, with a four- or five-chromatic `K_6`-minor-free
complement.  The
[order-nine projection theorem](../results/hc7_k7minus_order9_crossed_transition_projection.md)
gives a complementary conclusion without losing the old boundary: an
unlocked transition has nonempty support on at most four vertices of `T`
and yields either a boundary colouring rejected by both shores or one
literal boundary Kempe interchange between opposite-shore colourings.  In
the latter case the two supporting components have boundary order seven,
eight or nine and are full to `T` in the final case.

For `F=4K_2 dotcup P_3`, the audited
[induced-path common-model theorem](../results/hc7_k7minus_p3_opposite_coordinate_common_model.md)
puts each leaf response on a seven-connected two-edge host.  Deleting a
crossing matching coordinate and both path edges gives one six-connected
host with the complete punctured three-coordinate cube and one spanning
`K_6` model co-bagging both the matching pair and the entire induced path.
The order-nine host becomes seven-connected after order-seven/eight
responses are excluded.  In the exact order-eight row, all three deleted
edges cross the cut and two complete geometric linkage families share one
shore fan.

These theorems remove path existence, unrelated model choice and an
unbounded unlocked separator as the first gaps.  They do not allocate
palette components or transition paths to model bags.  The matching repair
is to make one dominating lock or one projected transition meet both sides
of four foreign bags, or to preserve its labels through a bounded response.
The audited
[all-lock branch-set transfer gate](hc7_k7minus_all_lock_branch_transfer_gate.md)
shows that this cannot be obtained by absorbing an initial segment of one
lock component in one fixed colouring: a proper segment is not a Kempe
component, whereas switching the whole connected lock leaves the selected
edge monochromatic.  Blocked model ownership therefore does not itself
produce an original-labelled response separator or common shore partition.
This is a recorded route nonclosure, not a counterexample to a
response-sensitive split theorem.  A successful matching repair must
compare different realised signatures while retaining one model, or use a
new consequence of target exclusion.
The audited
[cross-signature pivot gate](hc7_k7minus_cross_signature_pivot_gate.md)
performs that comparison as far as the present data permit.  The fixed
foreign-bag deficiency profile is colouring-independent.  At a supplied
common `EE` pivot, the two singleton-producing Kempe components must share
one palette colour and either meet in that colour or have an edge between
their other colour classes; otherwise their switches produce the forbidden
`PP` signature.  The response square does not itself supply one common
`EE` pivot, and the resulting interaction need not meet a deficient model
label.  The audited
[static two-split barrier](../barriers/hc7_k7minus_static_two_split_profile_barrier.md)
shows that target exclusion and `K_5`-free quotient contacts do not repair
this second gap.  The matching route is therefore deferred until a
Kempe-valid model-monotone exchange is available.
The induced-path repair is the corresponding triple split: four foreign
bags must meet all three connected pieces of the path bag, or the failed
allocation must return a labelled order-seven response.  The finite
[opposite-shore diagnostic](experiments/opposite_shore_coordinate_square_gate/)
shows that the three positive signatures, two response fans and a common
co-bagged model do not suffice if the forbidden all-proper signature and
critical connectivity are omitted.

If `kappa(X)>=7`, the audited
[growth-or-feedback theorem](../results/hc7_k7minus_six_coordinate_growth_or_feedback.md)
gives an eight-edge componentwise-induced forest with a seven-connected
exact-model deletion host, or a feedback vertex set `T` satisfying

\[
                       |T|\le14,qquad\chi(G[T])\ge5. \tag{4.F2}
\]

Outcome (4.F2) is now empty.  The audited
[bounded-feedback degree elimination](../results/hc7_k7minus_bounded_feedback_degree_elimination.md)
uses the exact degree defect

\[
                       2|E(G)|\le9|V(G)|-25,
\]

the forest identity for `G-T`, and a sharp edge bound for a `K_5`-free
five-critical subgraph of `G[T]`.  These first force
`|T|=14` and `25<=|V(G)|<=27`.  Counting the degree-eight vertices that
remain inside `T` then strengthens the internal edge bound and contradicts
the same defect inequality.  The proof is unbounded and computation-free.
Consequently `kappa(X)>=7` forces the eight-coordinate exact-model outcome.

The audited
[endpoint-visibility theorem](../results/hc7_k7minus_eight_coordinate_endpoint_visibility.md)
now spends the full punctured eight-cube on that one model.  Choose an
exact model maximising the number of coordinate endpoints in the closed
neighbourhood of its deficient bag.  A connected branch transfer either
constructs `K_7^-`, returns an actual separator retaining a singleton
coordinate response, or strictly increases that score.  The last outcome
is impossible at the maximum.  Pigeonhole over the `15` or `16` endpoints
then puts two endpoint portals in one universal bag, so the exact-model
dichotomy returns the target or such a response separator.  Generic
density descent bounds the latter separator by nine, but can replace the
forest coordinate by a fresh singleton operation.  Thus the former
unlocalised dense fallback has been reduced to one bounded response
synchronisation problem with an exact label-loss alternative.

The
[fixed-coordinate response-core reduction](../results/hc7_k7minus_fixed_coordinate_response_core_reduction.md)
gives a rigorous descent without losing the coordinate.  The
same edge and colouring survive on every connected actual subset containing
a relevant endpoint.  A minimal boundary-list obstruction is connected,
retains the endpoint set, and gives strict side-order descent whenever it is
proper.  The process ends at a fixed-coordinate boundary-list-critical
side, but its boundary need not decrease.

The audited
[model-anchored hull theorem](../results/hc7_k7minus_model_anchored_response_hull.md)
now keeps the exact-model bag, a connected complement within that bag and a
named anticomplete bag throughout the side-order descent.  Global
minimisation over all eight coordinate responses and all ordinary exact
models gives the audited
[appendage-ownership theorem](../results/hc7_k7minus_model_anchored_appendage_ownership.md).
A nonsingleton terminal side consists of a boundary-list-critical core and
at most two coordinate-free appendages.  Each appendage monopolises at
least two foreign model labels, and different appendages have disjoint
monopoly sets.

Every appendage has a fresh attachment-edge response.  The audited
[operation-provenance theorem](../results/hc7_k7minus_operation_provenance_exchange.md)
puts that response and the retained forest response on one deletion host
and determines its equality signatures.  It does not exchange their
provenance: the core retains the forest coordinate but disconnects the
branch-bag complement, while the appendage retains the model geometry but
only for the fresh operation.  The exact static
[appendage quotient screen](experiments/model_anchored_appendage_quotient_gate/README.md)
leaves target-free profiles for every ownership order.  Thus another
uncoloured ownership analysis cannot close this case.

At a singleton, the audited
[coordinate-localisation theorem](../results/hc7_k7minus_singleton_coordinate_localisation.md)
gives an exhaustive fork.  A nonadjacent neighbour supplies one induced
path with all three nonempty equality signatures.  The audited
[common-deletion theorem](../results/hc7_k7minus_singleton_induced_path_common_deletion.md)
then gives a seven-connected common host or an actual order-seven/eight
response retaining the entire square.  The seven-connected outcome is the
same response-sensitive three-piece model-allocation problem already
isolated in the six-cut path case.

In the other singleton outcome, the forest mate dominates the remaining
neighbourhood.  The audited
[dominated common-neighbour theorem](../results/hc7_k7minus_dominated_singleton_twocut_response.md)
finds a vertex cut of order at most two, actual response components on its
two sides, and an exact exclusive switch between the original edge and
each fresh incident edge.  The audited
[low-degree completion](../results/hc7_k7minus_dominated_singleton_low_degree_terminal.md)
uses an exact marked-neighbourhood enumeration to eliminate the only
degree-eight and degree-nine placements which could trap every
model-persistent edge in the cut.  Together with the high-degree count,
the dominated case is aligned at every degree: one common deletion graph
retains the original exact model, the forest colouring, a fresh exclusive
response and an actual response component.

The centre-preserving visibility and bounded-interface theorems now bypass
that unbounded component.  At an original degree-eight centre `u`, the
exterior of `N[u]` is connected and the exact boundary has the form

\[
                    N(u)=Q\mathbin{\dot\cup}\{v\},
\]

where `v` is complete to `Q` and `Q` is `C_5\dot\cup K_2`, a five-cycle
with a pendant two-edge path, or `C_7`.  The graph
`H=G-\{u,v\}` is five-connected.

Protect `Q` and two of the four other independent degree-eight centres in
one terminal-legal contraction of `H`.  The written and audited
[two-protected-centre theorem](hc7_k7minus_dominated_two_protected_centres_kernel.md)
eliminates the complete order-eleven branch, so the common irreducible
kernel has order nine or ten.  The exact order-ten catalogue has 1,153
rooted occurrences; an independent connected-partition checker confirms
that one usable contact from an adaptively selected protected centre to an
adaptively selected `Q`-rooted bag
closes every occurrence.  In the all-terminal order-nine branch, contacts
at both centres close every static survivor.  A corrected computer-assisted
diagnostic shows that,
in 1,901 of 2,252 placements, each named centre admits some closing contact;
in the remaining 351 exactly one centre does.  The
former figures 2,177 and 75 came from a helper which inadvertently added a
hidden second contact and are withdrawn.

The prescribed-representative theorem gives a literal selectable matching
edge at a protected centre but not its rooted-bag location.  Ordinary
root-bag minimisation does not bridge that gap.  The exact faithful suffix
screen deletes every source adjacency owned solely by the moved suffix and
still leaves

\[
                         256,\qquad1022,\qquad256
\]

order-nine placements.  This is a decisive route nonclosure for static
two-owner transfer, not a host counterexample.  The missing positive
statement must use the matching edge's singleton-signature colouring.

The separately audited
[anchored-compression barrier](../barriers/hc7_k7minus_anchored_coordinate_compression_barrier.md)
still has arbitrarily high connectivity and minimum degree and an unbounded
singleton response boundary.  It contains a literal `K_7`, so it does not
refute the live target; it proves that the target must use the exact model,
the second operation and `K_7^-`-minor exclusion.

The audited six-centre feedback theorem, forest-component reduction,
forest-shore extension and four-of-five composition theorem remain valid
proof infrastructure for the now-impossible alternative.  Their full-shore,
`7,6,7` and six-component cases are superseded reductions, not live global
residues.

Finally, the audited
[portal-cycle threshold reduction](../results/hc7_k7minus_portal_edge_cycle_threshold.md)
puts a clean exact-model portal edge and all six edges in (4.F1) on at most
two vertex-disjoint cycles.  The exceptional seven-edge-cut outcome gives a
proper order-seven separation.  Connectivity alone cannot cite the desired
one-cycle upgrade: this is precisely the unresolved Lovasz--Woodall
threshold.  The smallest repair is a two-cycle composition using the exact
seven branch bags and critical colouring responses.

The proposed operation-labelled protected-centre contact-or-split theorem
has now reached a decisive route nonclosure.  In `H-w`, failure of a
six-arm fan from the selected mate to `Q` gives an exact order-seven
separation retaining the selected edge and its singleton-signature
colouring.  If the fan exists, its paths in the original host need not
align with the independently contracted branch sets.  A target-free exact
quotient survives even when the mate has six direct `Q` contacts,
and explicit simultaneous three-arm suffixes still leave faithful-transfer
survivors.  A marked-edge terminal kernel supplies only a contact already
covered by the baseline connected-absorption search.  Thus
five-connectivity, fan incidence and static branch-set ownership do not
imply the desired common two-centre contact or split.

Unlike the punctured response cube, which is automatic for every
componentwise-induced forest in a minor-critical graph, the connectivity,
common-cycle and model-placement conclusions are genuine structural data.
The complete bounded-feedback alternative is terminally eliminated,
endpoint placement in the forced exact model is terminal, and the
dominated singleton is model-aligned in every degree and its centre-bearing
terminal has a common nine- or ten-vertex rooted kernel.  The underlying
colouring-to-branch-set conversion remains open, but the protected-centre
fan-to-root mechanism is frozen rather than treated as an active theorem
target.  In the nonsingleton outcome, the parallel open problem is
operation-sensitive transfer across at most two model-owning appendages.

### Seven-removable matching entrance

The separately audited
[seven-removable matching reduction](../results/hc7_k7minus_seven_removable_matching_reduction.md)
now gives a shorter common-host reduction.  Apply Theorem 1.3 of
[Chu's recent removable-matching preprint](https://arxiv.org/abs/2608.09394)
with `k=7` and `m=5`.  Since
`delta(G)>=8` and `|V(G)|>=25`, there is a matching `M_R` of order five such
that

\[
                    H_R=G-M_R
\]

is seven-connected.  It also satisfies

\[
 |E(H_R)|\ge4|V(H_R)|-5,\qquad
 \{\Sigma_{M_R}(c):c\in\operatorname{Col}_6(H_R)\}
                    =2^{M_R}-\{\varnothing\}.       \tag{4.R1}
\]

The signature assertion follows by six-colouring `G/J` and expanding the
contracted matching edges, for every nonempty `J subseteq M_R`; the empty
signature would six-colour `G`.  For each singleton `e in M_R`, both `G-e`
and `G/e` are exactly six-chromatic.  The audited contraction-bag
normalization therefore returns a connected set `Y_e` containing exactly
one end of `e`, with `N_G(Y_e)` an actual separator of order at least seven.
A signature-`{e}` colouring gives a boundary precolouring which is proper
outside `Y_e` and does not extend through it.  More generally, every proper
set meeting a matching endpoint carries such a rejected exterior trace.

The seven-connectivity of `H_R` removes every low-connectivity row from
this common host.  Norin--Totschnig's density theorem gives a spanning
`K_7^vee` minor model in `H_R`.  Label its branch sets

\[
                 P,B,C,U_1,U_2,U_3,U_4,
\]

where only `PB` and `PC` may be absent.  Target exclusion makes both pairs
anticomplete even after `M_R` is restored, so this is an exact spanning
model in `G`.  The audited exact-model dichotomy now gives a `K_7^-` minor
or a nonempty proper connected set `Y` in one universal bag, with connected
bag complement and `N_G(Y)` an actual separator.  If `Y` meets `V(M_R)`, it
carries a singleton-signature rejected trace.

There is a sharp support residue.  If two `P`-neighbours in one universal
bag are matching endpoints, the exact-model proof can select them and
returns the target or a separator meeting an endpoint.  Hence a target-free
outcome without a forced trace satisfies

\[
 |N_G(P)\cap U_i\cap V(M_R)|\le1\quad(1\le i\le4),
 \qquad |N_G(P)-V(M_R)|\ge3.                         \tag{4.R2}
\]

The old five-centre response support may be retained simultaneously.  With
`W_Z` from the dense rotation-visibility theorem and

\[
                         W^+=W_Z\cup V(M_R),
\]

the same argument gives (4.R2) with `V(M_R)` replaced by `W^+`.

This entrance is now consumed by the replacement-abundance and
six-coordinate theorems above.  The response-bearing separator and sparse
support in (4.R2) remain valid conditional outputs, but they are no longer
the first proof obligation.

The price of seven-connectivity is loss of the exceptional-centre labels.
The matching `M_R` need not have one end at each centre, so (4.R1) does not
give centre saturation, exact six-chromaticity for every multi-edge
deletion and contraction, or one common `K_6` model co-bagging all five
pairs.  Those stronger conclusions belong to the centre-edge construction
below.  Chu's theorem is also a recent preprint input, not an externally
peer-reviewed result at the time of writing.

### Secondary centre-labelled common host

The audited
[common five-edge response theorem](../results/hc7_k7minus_five_centre_common_matching_reduction.md)
now provides a stronger literal synchronization without that inference.
For every `z in Z`, a star-contraction colouring gives an independent triple
`I_z` and five singleton-colour neighbours `R_z`.  Hall's theorem selects
distinct `x_z in R_z`; hence

\[
 M=\{zx_z:z\in Z\},\qquad H=G-M
\]

with `M` a matching.  The exact matching-signature language on `H` is

\[
                         2^M-\{\varnothing\}.        \tag{4.0}
\]

For every nonempty `J subseteq M`, both `G-J` and `G/J` are exactly
six-chromatic.  Expanding a colouring of `G/J` gives a signature-`J`
colouring whose restriction `theta_J` to `F` satisfies

\[
 \varnothing\ne\operatorname{Sat}(\theta_J)
                 \subseteq\{z:zx_z\in J\}.          \tag{4.0a}
\]

The same two graphs supply spanning `K_6` models: one in `G-J`, and one in
`G` with every pair indexed by `J` in a common branch set.  Applying the
minimal contraction-bag theorem to each singleton coordinate also gives
five actual separators of order at least seven, each carrying its literal
exterior-realised, interior-rejected precolouring.  Their orders and boundary
partitions need not agree.

This one graph gives the following exhaustive connectivity alternatives.

1. If `kappa(H)=2`, every minimum cut has two components joined by all five
   deleted matching edges.  All 32 endpoint transversals are exact
   order-seven cuts with two full sides.  The same pair is a two-cut of
   `F`; every centre has its selected representative as its unique contact
   with one open shore and all seven other neighbours in the opposite
   closed shore.
2. If `kappa(H)=3`, every minimum cut has two components joined by four or
   five matching edges.  Four crossings give 16 exact order-seven cuts.
   Five crossings give 32 proper order-eight cuts; every mixed transversal
   gives an exact order-seven descent or two full order-eight sides.  The
   cut with its centres removed separates `F`; when `kappa(F)>=3`, the cut
   avoids `Z` and is a three-cut of `F`.
3. If `kappa(H)>=4`, density and Norin--Totschnig give a spanning
   `K_7^vee` model.  The exact near-clique dichotomy gives the target or a
   connected, co-connected model-bag piece `Y` with an actual boundary of
   order at least seven.  If `M_Y=\{e in M:e cap Y ne emptyset\}`, then
   every nonempty `J subseteq M_Y` gives an exterior-realised,
   interior-rejected trace on `N_G(Y)`.  These `2^{|M_Y|}-1` traces need not
   induce distinct boundary partitions.

The common-host theorem replaces five unrelated operations by one punctured
five-dimensional Boolean response family.  It does not yet terminalize the
three connectivity rows.  In the two-cut row, the existing singleton-shift
theorem applies to every centre whose singleton lies on the equality shore,
but its scalar identities repeat and do not compose; if at most one does,
four singleton anchors lie on the distinct shore and root unrelated `K_4`
models there.  The 31 signatures give rejected traces, not 31 distinct
boundary partitions.  In the four-connected row, a returned piece disjoint
from all ten matching ends is invisible to the raw signature family; a
piece meeting the matching has traces but still lacks a partition-specific
carrier or terminal descent.

The audited
[two-shore rooted-minor theorem](../results/hc7_k7minus_five_centre_two_shore_rooted_k4.md)
sharpens the first row.  Orient the components as `C` (equal response) and
`D` (distinct response), and put

\[
                         U=\{z\in Z:x_z\in C\}.
\]

For every four-set `Q` of the seven-vertex boundary, `G[D union Q]` has a
`Q`-rooted `K_4` minor.  If `U` is nonempty, one centre has a singleton
contact with `C`; the singleton-shift density bound and the rooted `K_4`
obstruction theorem then give the same universal conclusion in
`G[C union Q]`.  Merging two such models at one common boundary root gives
seven bags, but the remaining `3`-by-`3` cross-shore matrix needs at least
eight adjacencies.  Fullness contacts may all enter the merged bag and do
not force a specified matrix entry.  If `U` is empty, all five selected
neighbours are singleton contacts with `D`, and the equality-shore rooted
model is not yet supplied.

The audited
[signed four-crossing theorem](../results/hc7_k7minus_four_crossing_signed_boolean_reduction.md)
now resolves the connectivity and linkage geometry of the first three-cut
row.  Write its four crossing matching edges as `E`.  For every nonempty
`R subseteq E`, and every endpoint choice on `E-R`, the graph `G-R` has two
full complementary shores at a separator of order `7-|R|`, and

\[
 \kappa(G-R)=7-|R|,
 \qquad
 \Sigma_R(G-R)=2^R-\{\varnothing\}.                \tag{4.0b}
\]

One fixed family of seven disjoint paths contains the four crossing edges
as consecutive edges on four distinct paths.  This is a signed statement:
the centre end of a coordinate may lie on either shore.  For
`1<=|R|<=3`, the dense minor theorem gives a spanning `K_7^vee` model, so
target exclusion returns an actual nested model-bag separator.  A returned
piece meeting `r` deleted coordinates carries all `2^r-1` corresponding
rejected traces.  The first unsupported case is again a piece disjoint from
the coordinate ends, or one whose traces repeat the same boundary
partition.  Thus (4.0b) is not yet a terminal elimination of the
four-crossing row.

For the five-crossing row, either a mixed order-eight transversal exposes an
exact order-seven component, or all thirty mixed transversals have exactly
two full shores.  The audited
[omitted-coordinate linkage theorem](../results/hc7_k7minus_five_crossing_omitted_coordinate_linkage.md)
removes the apparent one-unit slack in the latter case.  For every selected
edge `e_i=z_ix_i`, at least one of the useful alternatives holds:

1. `G-e_i` exposes an exact order-seven response with one end of `e_i` in
   the boundary and the other in the rejected component; or
2. `G-e_i` is seven-connected and has seven disjoint `z_i`--`x_i` paths
   which place the other four matching edges consecutively on four paths
   and the three vertices of the original cut on the other three.

In the second outcome, restoring `e_i` gives eight disjoint paths and the
rooted minor

\[
                  K_2\vee G[N_G(z_i)-\{x_i\}].      \tag{4.0c}
\]

Thus the displayed seven-vertex neighbourhood graph has no `K_5^-` minor.
If the response outcome fails for all five coordinates, all five complete
path packets exist, but only with quantifiers `for every i there exists
P_i`.  The packets lie in different one-edge deletion graphs and may
intersect arbitrarily.  Simultaneous packet composition is now the first
unsupported inference.

The audited
[dense-branch visibility theorem](../results/hc7_k7minus_dense_branch_rotation_visibility.md)
sharpens the four-connected row.  For each centre, let `K_z` be the
intersection of all independent triples in its neighbourhood, and put

\[
                  W=Z\cup\bigcup_{z\in Z}(N_G(z)-K_z).             \tag{4.0d}
\]

Every connected set meeting `W` has a direct rejected trace from a centre
deletion or star contraction.  If one universal bag of the exact
`K_7^vee` model contains two `P`-neighbours in `W`, the near-clique proof
returns the target or a nested separator containing one of them.  Hence a
trace-invisible residue has at most one supported `P`-neighbour in each of
the four universal bags, at least three `P`-neighbours outside `W`, and at
most two vertices in each exceptional neighbourhood.  If the returned
boundary has order seven and its selected piece avoids `Z`, it is already a
labelled two-cut or a four-centre order-three separation of `F` when the
boundary contains respectively five or four centres.

The secondary centre-labelled terminalization problem is therefore to solve
the two-shore `3`-by-`3` allocation or the all-five-on-`D` orientation;
terminalize the signed four-crossing separator or compose the five omitted-
coordinate linkage packets; or eliminate its response-support-sparse dense
model.  These rows remain valid receivers if the seven-removable route
returns an exact labelled separation.  They are no longer the immediate
proof obligation.  The rotation theorem remains available for labelled
three-cut geometry, while direct palette intersection is frozen.

The audited
[operation-coupled reduction](../results/hc7_k7minus_four_centre_operation_cut_reduction.md)
sharpens the web side.  For a selected cross-edge it gives either a
colour-indexed five-spoke packing or a strictly smaller actual order-seven
component retaining a common exact colour block.  The always-available
distinct-ended fan has at least two missing limb contacts.  If one shore
contains two disjoint boundary-full connected subgraphs, then `T` is
independent, every independent four-set in the boundary has independent
complement, and one fixed shore colouring carries all three pairwise `T`
Kempe paths.  Each unused centre also repairs the rooted-web obstruction in
the uncoloured graph.  The smaller cut need not contain `U`, and the paths
need not avoid the rooted bags or the two full subgraphs; neither output is
yet terminal.

The audited
[tri-separation normalization](../results/hc7_k7minus_four_centre_tri_separation_reduction.md)
now identifies the unlabelled geometry of the original four-centre cut.
After deleting `U`, its ordinary three-separation has a unique strong
nontrivial Carmesin--Kurkofka reduction with both open sides connected.
That reduction is either induced by a canonical mixed-tree-decomposition
edge or heavily interlaces a unique splitting star whose compressed torso is
a wheel and whose expanded torso is a generalized wheel.  Two crossing
reductions have a one-vertex centre and four one-element links.

An explicit
[boundary-trace counterexample](../barriers/hc7_k7minus_tri_separation_boundary_trace_loss.md)
shows that the mixed reduction alone does not identify the original endpoint
of a separator edge.  The audited
[trace-preserving descent](../results/hc7_k7minus_four_centre_trace_descent.md)
retains the inverse boundary map, fixed colouring, ordered rooted terminals
and named Kempe contact.  Choose a trace-admissible cut with selected
component `C` of minimum order.  Every vertex of `T` then has at least two
neighbours in `C`, and any nontrivial tri-separation below the reduced cut
that splits `C` yields a strictly smaller trace-admissible exact cut.  In the
canonical-adhesion case, no nontrivial tri-separation splits `C`.

The separately audited
[generalized-wheel leaf descent](../results/hc7_k7minus_four_centre_wheel_leaf_descent.md)
removes the remaining unrestricted rim geometry.  At a minimum cut, `C` is
disjoint from the expanded generalized-wheel torso and is exactly the open
side of one canonical leaf.  The graph `H[T]` has an edge, and each
complementary component lacks two vertex-disjoint connected subgraphs that
are each adjacent to every vertex of `U\dot\cup T`.

This is the limit of the uncoloured decomposition.  The separately audited
[Fano-plane barrier](../barriers/hc7_k7minus_tri_inseparable_full_subgraph_barrier.md)
is seven-connected, `K_5`-free, has minimum degree eight, and has no mixed
separation of order at most three splitting its selected component.  That
component nevertheless has no two disjoint connected subgraphs adjacent to
the whole boundary.  The example contains a `K_7` minor; it refutes only the
attempt to deduce the required subgraphs from tri-inseparability and degree
conditions.  A proof for the critical host must use its proper-minor
six-colourings or the exclusion of a `K_7^-` minor.

The audited
[exact-boundary reduction](../results/hc7_k7minus_four_centre_exact_u_bridge_reduction.md)
now uses the proper-minor colourings on the actual minimum side.  Exact
colourings of its two closed shores put `U` in one colour class.  On `C`, a
paired trace gives three same-end bichromatic paths; otherwise an
all-distinct trace gives one such path for the paired trace accepted on
`D`.  A connected support can be chosen so that all centre-free components
are absorbed.  At most eight components remain, at most two see all four
centres, and at most two have one attachment to the support.

In the paired case, the audited
[clean-fan theorem](../results/hc7_k7minus_four_centre_paired_trace_fan.md)
replaces the uncontrolled intersection of the three Kempe paths by one
`p`--`p'` path and two `p`--`q` paths whose interiors are pairwise disjoint.
The alternative in the fan argument is already a strict trace-admissible
descent.

The audited
[common-colouring theorem](../results/hc7_k7minus_common_colouring_centre_change.md)
controls the opposite side.  Recolouring the four selected classes gives a
single six-colouring of `H` saturated at another centre.  Every exact
four-centre cut obtained there is either the old cut or has a component
`B` with `emptyset != B subsetneq D`.  Inclusion-minimal such components
are disjoint.  Their interaction graph `Gamma` satisfies

\[
             \Delta(\Gamma)\le3,
             \qquad \alpha(\Gamma)\le2,
             \qquad |V(\Gamma)|\le4.                 \tag{4.1}
\]

The order bound follows from explicit `K_7^-` models.  In the equality
case `Gamma` is initially `2K_2`, `P_4`, or `C_4`.  The five resulting exact
components force at least eleven distinct cuts obtained by simultaneously
replacing nonempty sets of uniquely attached centres by their unique
neighbours.  Together with the five original four-centre cuts, this gives
at least sixteen distinct exact order-seven cuts.  For each component, its
replacement cuts form a Boolean sublattice of the separation lattice, and
one six-colouring of the original closed side gives a coherent boundary
partition at every cut.  At least one sublattice contains a four-element
square.  Its cuts do not share one fixed centre set, so the existing
fixed-anchor uncrossing theorem does not compare their boundary partitions.

The audited
[Boolean replacement theorem](../results/hc7_k7minus_boolean_replacement_edge_coupling.md)
supplies the missing graph structure.  Fix one exact component `P`.  In any
seven-path linkage across its replacement family, each edge
`u x_{uP}`, `u in W_P`, is a fixed coordinate edge on a distinct path.
Proper-minor colourings of the graph with these edges deleted realize every
nonempty set of endpoint-equalities, while the all-unequal set is
impossible.  A colouring restricts properly to a closed side exactly when
its equal endpoint pairs lie on the side prescribed by the corresponding
Boolean coordinate.

Deleting one coordinate edge `ux` gives an exact order-six separation in
the six-connected, exactly six-chromatic graph `H=G-ux`.  Its boundary has at most
eleven edges.  If `L,R'` are its open sides and

\[
 \delta_Z=|E(H[Z])|+|E_H(Z,Q)|-4|Z|,
 \qquad \sigma=|E(G)|-4|V(G)|,
\]

then

\[
             \delta_L+\delta_{R'}
              =\sigma+23-|E(G[Q])|\ge\sigma+12.     \tag{4.2}
\]

The coordinate edge is not double-critical.  If colourings of the two
closed shores induce the same partition on `Q`, then they combine unless
the endpoints have the same named boundary colour, or `Q` uses five colours
and both endpoints use the sole missing colour.  In the latter case the
boundary partition has shape `2+1+1+1+1`.

Deleting two coordinate edges gives an exact order-five separation in a
five-connected, exactly six-chromatic graph with a spanning `K_6` model.
The three nonempty endpoint-equality signatures occur, but their colourings
need not be related.  In the four-region case, if `Gamma` is `P_4` or
`C_4`, the two replacement vertices are nonadjacent; an edge between them
would give an explicit `K_7^-` model.  That adjacency argument alone does
not eliminate either interaction graph and gives no conclusion for `2K_2`.

The audited
[cyclic four-region elimination](../results/hc7_k7minus_cyclic_four_region_elimination.md)
uses the full simultaneous-replacement geometry to close one of those
graphs.  Inside a doubly replaced component, internal rooted connectivity
and the rooted-triangle obstruction produce three pairwise adjacent bags
rooted at the two replacement vertices and one remaining centre.  If
`Gamma=C_4`, the four other exact components form a `K_4^-` after the last
centre is absorbed, so the seven bags give an explicit `K_7^-` model.
Thus

\[
                         \Gamma\in\{2K_2,P_4\}.       \tag{4.3}
\]

In the `P_4` case, no Boolean square is based at `C` or at an endpoint
region.  Its two internal regions carry at least five unique-centre
incidences between them; both carry one, and one carries at least three.

The audited
[minimum-separator linkage theorem](../results/hc7_k7minus_boolean_minimum_separator_linkage.md)
now anchors this geometry.  If `P subset D`, every coordinate path crosses
the old minimum boundary at its named centre `u`; its suffix after `u` lies
wholly in `C`.  Truncating one common linkage between the Boolean and old
separators fixes every replaced coordinate as the literal edge
`x_{uP}u`, every unreplaced centre as a trivial path, and bijects `T_P`
with `T`.  The `u`--`C` suffix may be stopped at the interior of the clean
fan's `p`--`p'` path.  Thus the old base-point and path-permutation
ambiguities are gone.  This is path anchoring, not a replacement cut based
at `C`; in particular, it does not prove `u in W_C`.

For one coordinate, the same theorem gives an exact response-language
normal form.  Write `Q` for the six-vertex separator of `G-ux`.  Rejection
at the cut containing `x` already implies rejection at the cut containing
`u`, because the coherent intact-side types of `x,u` are compatible.
Hence “simultaneous rejection” is only one constraint.  Starting from any
six-colouring `kappa` of `G-ux`, for which `kappa(u)=kappa(x)`, recolour
only `u` on the original closed `P`-side.  At most four neighbour colours
are forbidden there.  The resulting coherent colouring agrees with
`kappa` on `Q`, removes the empty-language alternative, and forces one
two-colour lock through each open shore.  The `P`-side lock begins with the
literal edge `ux`.  Concatenating it with the anchored suffix produces one
path whose colour-labelled prefix reaches the clean-fan support through
the named centre; no colour conclusion holds on its `C`-tail.

There is also an exact terminal criterion for separator transport.  If a
proper order-four separation of `H=G-U`, crossed by exactly three centres,
enters and splits `C` while retaining `x_j` in the opposite open side,
fixed-anchor uncrossing with the old cut yields either a strict
trace-admissible exact-`U` descent or an exact one-missing-centre cut
strictly below the old separation.  The present Boolean cuts based in `D`
are nested above the old cut and do not split `C`, so this criterion does
not yet fire.

The first unsupported inference is now fixed-trace synchronization.  The
normalization uses an arbitrary colouring of `G-ux`, whereas the minimum
side and clean fan use one fixed exact-`U` trace.  No proved step makes
these the same witness.  The
[odd-wheel mechanism barrier](../barriers/hc7_k7minus_local_coordinate_synchronization_barrier.md)
has an exact lower-order cut, both adjacent lifted cuts, the common lower-cut
partition, endpoint equality, coherent normalization, two-sided Kempe locks
and a simultaneous literal coordinate linkage, but neither lifted cut has
a partition realized by both shores.  It is not a critical host and has no
fixed minimum-side trace, so it does not refute the desired theorem.  It
does rule out deriving synchronization from the local package alone.

A direct fixed-trace audit exposes a sharper localization failure in that
one-coordinate formulation.  Fix a literal colouring `c` of the old closed
`C`-shore inducing the selected partition `Pi_C`.  For `z in D`, define

\[
              L_e(z)=[6]-c(N_{G-e}(z)\cap(U\cup T)),                \tag{4.4}
\]

where `e=ux_{uP}` and `x=x_{uP}`.  Then `G-e` has a six-colouring inducing
`Pi_C` on the old boundary if and only if `G[D]` is `L_e`-colourable.
Deleting `e` can enlarge only the list at `x`, and it does so only when `x`
has no second neighbour in `U`.

If `G[D]` is not `L_e`-colourable, a vertex-minimal induced rejection
kernel can avoid `x`.  No proved result excludes that possibility.  In
that branch the coordinate edge is absent from the obstruction, and every
separator naturally exposed by the kernel is nested inside `D`, on the
wrong side of the minimum choice of `C`.  Even a kernel containing `x`
does not presently produce a separation which enters `C`.  Thus the
proposed one-coordinate trichotomy does not follow from the current
package: its hypothesis is opposite-side list rejection, while its two
noncolouring exits were required inside `C`.  This is a recorded route
nonclosure, not a counterexample to such a theorem under the full critical-
host hypotheses.

For the four-centre laboratory, the next accepted target is a square-level
fixed-trace kernel localization theorem.  For the two marked list
enlargements of a surviving
`2K_2` square or internal-region `P_4` square, it must force one of:

1. a one- or two-coordinate colouring attaining `Pi_C`, followed by an
   aligned endpoint repair;
2. an explicit `K_7^-`-minor model; or
3. an exact fixed-trace or one-missing-centre separation which enters and
   strictly splits `C`.

In particular, the theorem must handle kernels avoiding one marked endpoint;
merely applying the one-extra-colour critical-kernel trichotomy after
assuming attainment is circular.  The fixed trace remains the common
invariant needed for composition, while the square supplies two marked list
changes rather than one coordinate which may disappear from its own
obstruction.

There is also an exact rooted-minor formulation.  The audited
[boundary-completion theorem](../results/hc7_k7minus_four_centre_completed_side.md)
shows that

\[
                         F=H[C\cup T]+\binom{T}{2}
\]

is four-connected.  For every two-set `P subseteq T`, the actual rooted
pair `(G[C union U union P],U union P)` is internally six-connected.  If it
contains a rooted `K_6^-` minor, the opposite component `D` is a seventh
branch set and gives a `K_7^-` minor in `G`.  In the generalized-wheel
branch, choose `P` as the ends of the forced edge in `H[T]`.

The separately audited
[six-terminal barrier](../barriers/hc7_k7minus_internal_six_rooted_k6minus_barrier.md)
shows the exact limit: internal six-connectivity, the boundary edge and even
a rooted `K_4` do not force the prescribed `K_6^-` minor.  Its natural
boundary extension already has a four-connected completion, but it contains
two disjoint connected subgraphs adjacent to all seven boundary vertices.
Thus any theorem forcing either the prescribed rooted `K_6^-` minor or a
trace-preserving exact-cut descent must use the full generalized-wheel
restriction or the minor-critical colouring responses.

### Secondary sufficient one-centre routes

The earlier one-centre allocation statement remains a sufficient target,
but it is no longer the preferred endpoint:

> **Rooted exterior-allocation target.** Among the at least 25 exceptional
> centres, find `u`, an independent triple `I\subseteq N(u)`, and an
> `(N(u)-I)`-rooted `K_5` model such that either:
>
> 1. the model avoids one component of `G-N[u]`; or
> 2. a connected subgraph disjoint from the star and all five bags is
>    adjacent to the star and to at least four bags.

In the both-full two-component case, a third accepted outcome is an
`(N(u)-I)`-rooted `K_5^-` model confined to one closed side; the unused
full component completes it to `K_7^-`.

Each accepted outcome gives an explicit `K_7^-` model.  With one exterior
component, the residual-contact outcome is necessary: a model avoiding the
whole component would be confined to its five roots and would make them a
literal `K_5`, impossible at an exceptional centre.

For two exterior components, the literal-clique theorem first forces the
global high-density branch (2).  Two nonfull components cannot have the
same miss or distinct nonadjacent misses.  In the adjacent-miss residue, one
fixed operation now supplies the required disjoint paths and a point-rooted
`K_4`; set-rooted absorption is the remaining obstruction.  In the
one-nonfull residue, one fixed operation localizes all five two-colour paths
but does not align them with the near-clique bags.  In the both-full residue,
rooted diamonds and dense component contractions still lack compatible
labels.  The minimum-shore rotation is now eliminated by a six-colouring,
but all three general attachment regimes, and therefore exceptional-centre
connectivity, remain open.

The existing one-pair seven-path argument cannot supply this allocation;
its exact failure is recorded in the
[seven-path barrier](../barriers/hc7_k7minus_bad_pair_seven_paths_barrier.md).

A second exact sufficient target is tailored to the new forced interface.
Choose a minimum-order component `C_0` among `G-N[v]` over all exceptional
vertices `v`.  At its centre, one named edge-deletion colouring must yield
an explicit `K_7^-` model, a six-colouring, or an exceptional
anti-neighbourhood component smaller than `C_0`.  This
[one-operation terminal/descent target](hc7_k7minus_pair_deletion_k7vee_reduction.md#5-one-named-colouring-operation-and-its-exact-limit)
would close the whole critical host.  The new model-level dichotomy returns
an operation-preserving actual separator.  A separate global minimization
reduces the host to an exact two-shore seven-cut or to a minimum order-eight
boundary with two or three full complementary components and a
`K_5`-minor-free four-colourable boundary satisfying a stronger
vertex-deletion profile.  In the order-eight branch,
`kappa(G)=delta(G)=8`, `n_7=0`, `|E(G)|>=4|V(G)|`,
`n_8>=25+tau`, and `b>=20+tau`; every disconnected exceptional
anti-neighbourhood is automatically a two-shore both-full interface.  The
fixed double-star response also has a persistent single-edge-deletion
colouring with the same trace away from its root.  Eight-connectivity forces
the order-eight operation machinery into clean fans and, on a smallest
two-shore side, a paired seven-column system whose contact graph has minimum
degree at most three.  At a fixed exceptional root with connected
anti-neighbourhood, the persistent single-edge response forces the same
system directly on the singleton root side, with boundary trace
`2,2,1,1,1,1` and the original labelled near-clique model still present.
The operation is then aligned, but the near-clique and column labels are
not.  Producing that label transfer, or a terminal when it fails, is the
remaining open step in this secondary route.

## 5. Pause decision and possible restart points

The Conjecture 21 discovery campaign is paused at the protected-centre
fan-to-root nonclosure.  No item below is authorised as an immediate proof
attack.  If the campaign is deliberately resumed after external specialist
review, the remaining mechanisms should be considered in this order.

1. Pause the protected-centre fan-to-root line.  Its exact positive output
   is an order-seven labelled separation when the required fan fails; its
   fan-success case has a verified target-free quotient and the same
   path/model quantifier mismatch as earlier allocation programmes.  Do not
   add further kernel orders, protected centres or static owner transfers.
2. In the seven-connected exact-model row, use the two-cycle portal theorem.
   Either merge the two cycles while retaining the six coordinates and the
   portal edge, or turn the failed rerouting into an order-seven separation
   carrying those labels.  Do not assume the unresolved one-cycle
   Lovasz--Woodall conclusion.
3. If component-to-bag capture does not close, apply one response-sensitive
   allocation theorem to the common induced-path triple split.  Its
   low-connectivity outcome already returns an order-seven/eight response;
   do not open a second path programme with fewer labels.
4. Return to `kappa(X)=6` matching only with new exchange technology.  In the
   matching row, a valid proof must supply one deficiency-aware common
   `EE` pivot or another Kempe-valid model-monotone exchange; the three
   realised signatures, fixed deficiencies and target exclusion do not do
   this statically.

The common co-bagged-`K_6` split proposed for the original removable
matching is not available in the eight-coordinate host and is obstructed at
quotient level.  Static appendage ownership is likewise exhausted.  In the
six-cut matching row where a common model is available, one fixed all-lock
colouring cannot label a branch-set transfer; the full response square has
now been spent up to the exact shared-pivot quantifier and model-incidence
gaps.
