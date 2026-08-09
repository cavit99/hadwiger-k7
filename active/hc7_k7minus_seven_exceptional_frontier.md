# Exceptional degree-eight vertices: live technical frontier

**Status:** active primary technical frontier for Norin--Totschnig
Conjecture 21.  The lower bound and the local neighbourhood,
exterior-completion, and two-component reductions in Sections 1--2 are
written and separately audited GREEN; the finite boundary claims have
retained independently checked verifiers.  The four-centre theorem and its
operation-coupled, tri-separation, trace-preserving, and generalized-wheel
leaf refinements in Section 4 are also separately audited GREEN.  The
accompanying scoped
barriers are separately audited GREEN, while the list-core calculation in
Section 3 remains a written live derivation without a separate audit.  The
upper bound is open.  This file is not a second status ledger.

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

   A fixed deletion of an internal edge of an attained-duty gate was also
   tested.  Its five bichromatic bypasses are labelled by the new edge
   response, whereas the three duties are labelled by the original
   proper-minor response.  No proved transition aligns those partitions;
   treating the bypass colours as duty labels is the first unsupported
   inference.  This does not refute a dynamic split.  The smallest repair
   is a two-operation trace-alignment theorem producing a complete detached
   support, a common boundary partition, `K_7^-`, or `N_G(z)` with a smaller
   exceptional anti-neighbourhood component.

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

**Status of the four-centre reduction:** written proof; separate internal
audit GREEN in the
[promoted theorem](../results/hc7_k7minus_four_centre_web_cut_lattice.md).
The theorem forcing either the required rooted minor or a strict
trace-preserving exact-cut descent remains open.

Since `R(4,5)=25` and `G` has no literal `K_5`, its exceptional vertices
contain an independent four-set `U`.  Put `H=G-U`.  Then `H` is
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

The second outcome cannot occur when `G` is eight-connected.  When
`kappa(G)=7`, the exact lift-order function on separations of `H` is symmetric
and submodular.  For fixed opposite anchors, its minimum separations form an
exact meet/join lattice.  If three cuts have all eight sign regions nonempty,
each centre has exactly one neighbour in every region; four cuts cannot have
all sixteen sign regions nonempty.

This reduces the global obstruction to one dynamic step.  In the rooted
outcome, use the unused centres to extend the rooted `K_5` model to an
explicit `K_7^-`-minor model or force the web outcome.  In the web outcome,
combine the retained one-sided trace and the centre-supported Kempe linkage
across the exact-cut lattice to obtain the same partition into colour
classes on both closed sides, an explicit `K_7^-`-minor model, or a strictly
smaller cut.  The exact static two-shore quotient is insufficient: even
maximum centre-to-boundary incidence and two full components admit a
target-free mechanism.

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

Here is the precise remaining web-side theorem.  Let `Pi` be the partition
of `S=U\dot\cup T` into colour classes under the fixed proper colouring of
the selected closed side.  Let `Q` be a largest clique whose vertices are
singleton blocks of `Pi`, and list the other blocks as `B_1,...,B_k`.
Prove one of the following:

1. there are pairwise disjoint nonempty connected subgraphs
   `P_1,...,P_k` of `C` such that every `P_i\cup B_i` is connected, these
   unions are pairwise adjacent, and each is adjacent to every vertex of
   `Q`;
2. a nontrivial tri-separation below the reduced cut splits `C`; or
3. `G` contains a `K_7^-` minor.

The audited
[boundary-colouring reflection theorem](../results/hc7_exact7_selected_response_preservation.md)
makes the first outcome a six-colouring of `G`; trace minimality excludes
the second.  This leaves a direct minor construction as the only outcome in
a hypothetical counterexample.

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

## 5. Recommended next attack

Pursue one global exceptional-centre terminal theorem.

1. In the rooted-model outcome, use the three unused centres to extend the
   rooted `K_5` model by two additional disjoint branch sets, or use the
   first unavoidable support conflict to force the rooted-web outcome.
2. In the rooted-web outcome, minimize the trace-admissible selected
   component.  Boundary replacement and any tri-separation below the reduced
   cut that splits it already give strict descent.  In the canonical branch
   the selected component is tri-inseparable.  In the generalized-wheel
   branch it is one leaf, `H[T]` contains an edge, and neither component
   contains two disjoint connected subgraphs adjacent to the whole boundary.
3. For the fixed boundary colour classes, construct the disjoint connected
   subgraphs specified above or, using the forced boundary edge, construct
   the prescribed six-terminal `K_6^-` minor in the actual selected side.
   Use the named Kempe component and the three unused centres: the two new
   barriers rule out arguments based only on tri-inseparability or internal
   connectivity.  A returned strict cut is terminal only if it retains `U`,
   the named vertices and the same one-sided colouring trace.

The earlier one-centre operation and rooted-allocation lemmas remain tools
only when they feed this global argument.  Further graph-code filters,
isolated boundary classifications, or another nonterminal separation are not
accepted progress.  The bottleneck is simultaneous label and support
allocation across the family of exceptional centres.
