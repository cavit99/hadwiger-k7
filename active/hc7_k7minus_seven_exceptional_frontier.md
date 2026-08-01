# Exceptional degree-eight vertices: live technical frontier

**Status:** active conditional frontier.  The lower bound and the local
neighbourhood, exterior-completion, and two-component reductions in Sections
1--2 are written and separately audited GREEN; the finite boundary claims
have retained independently checked verifiers.  The accompanying scoped
barriers are also separately audited GREEN.  The list-core calculation in
Section 3 is a written live derivation without a separate audit.  The upper
bound is open.  This file is not a second status ledger.

## 1. Exact finishing target

Let `G` satisfy

\[
 \kappa(G)\ge7,
 \qquad \chi(G)=7,
 \qquad \text{every proper minor of `G` is six-colourable},
 \qquad K_7^-\npreccurlyeq G.                              \tag{H}
\]

Call a degree-eight vertex exceptional when its neighbourhood is
`K_4`-free.  The proved
[two-literal-`K_5` exclusion and sharpened defect theorem](../results/hc7_k7minus_two_literal_k5_exclusion.md)
gives

\[
 b\ge17+\sum_{i\ge10}(i-9)n_i,                          \tag{1}
\]

where `b` is the number of exceptional vertices; write `tau` for the
displayed sum.  Therefore the theorem

> every graph satisfying (H) has at most sixteen exceptional vertices

would prove that every `K_7^-`-minor-free graph is six-colourable.  It is a
headline-equivalent finishing theorem, not a routine intermediate lemma.

The same theorem proves `n_7<=4`, `m>=4n-2`, and at most one literal
`K_5`.  If `n_7=4`, the host has order at least 37 and at least
`32+tau` exceptional vertices.  Thus the former exact `b=7` layer and all
two-clique tight layers are now excluded.

## 2. What the present attack proved

The new
[exceptional-neighbourhood and exterior-completion theorem](../results/hc7_k7minus_exceptional_neighbourhood_completion.md)
proves two facts.

1. Every exceptional vertex `u` has `alpha(G[N(u)])=3`.  Thus every one of
   the at least seventeen centres has an independent triple; the former
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

The focused two-component attack now has a global consequence.  The
[two-component literal-clique exclusion](../results/hc7_k7minus_one_nonfull_k5_and_nested_cut.md)
proves that if even one exceptional centre `u` has two exterior components,
then the whole graph contains no literal `K_5`.  The proof links any
hypothetical clique to five of the at least six neighbourhood vertices met
by both components and completes those five branch sets with `\{u\}` and
the opposite component.  Consequently

\[
 n_7=0,\qquad \delta(G)\ge8,\qquad |E(G)|\ge4|V(G)|,
 \qquad n_8\ge25+\sum_{i\ge10}(i-9)n_i.                \tag{2}
\]

Every degree-eight vertex is then exceptional and `|V(G)|\ge25`.  Thus a
surviving critical host obeys a sharp dichotomy: either every exceptional
centre has connected exterior, or the host is globally literal-`K_5`-free
and has at least 25 exceptional centres.

The sharpened clique theorem closes the positive-degree-seven side of this
dichotomy completely.  If `n_7>0`, degree-seven incidence supplies a
literal `K_5`, so every exceptional anti-neighbourhood is connected.  The
remaining connectivity target lies entirely in the `n_7=0`,
literal-`K_5`-free branch described by (2).

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
types.  Every surviving exterior component has `X`-full connected-subgraph
packing number one, so the full packing vector outside `X` is exactly
`(1,1,1)` for `\{u\},E,F`.  For the reserve types with six or seven
missing root adjacencies, every fixed star-contraction colouring still
supports at least two demands through each side; concentrating all but one
demand in one side would already give a rooted `K_5^-` and hence a
`K_7^-` model.  The
[scoped static barriers](../barriers/hc7_k7minus_shore_allocation_barrier.md)
show that boundary counting, fullness, and independent-triple rotation do
not by themselves force that concentration.

### Current operation-coupled connectivity attack

The proposed theorem that `G-N[u]` is connected for every exceptional
degree-eight vertex is proved when `n_7>0` and remains open only when
`n_7=0`.  Within that literal-`K_5`-free branch, the current attack gives
four unbounded reductions; none is an isolated graph-code elimination.

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
   structure.  The open residues are label-preserving augmentation of the
   unrooted near model and the wide cutvertex-block case.
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
it shows that one static colouring state cannot close the theorem.

There is, however, genuine adaptive information.  For each `x\in B`, a
six-colouring of the proper minor `G-x` restricts to a colouring of `G-B`
for which `H-x` is list-colourable but `H` is not.  Consequently every
minimal core for that response contains `x`.  The seven anchored cores may
differ; synchronizing them is the exact multi-centre colouring target.

## 4. Exact remaining obstruction

The most concrete current gate is the following allocation statement.

> **Rooted exterior-allocation target.** Among the at least seventeen exceptional
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

## 5. Recommended next attack

Attack the remaining operation-coupled obligations in this order.

1. **Add a second critical response in the adjacent-miss case.**  The
   point-rooted `K_4`, even with the full operated fans, does not by itself
   preserve whole path labels or return an order-seven cut.  Split according
   as the residual `G-{u,x,y}` is five- or six-chromatic and couple the fixed
   `G-xy` colouring to a second proper-minor colouring across the two
   overlapping critical order-seven separations.
2. **Use the same absorption/uncrossing mechanism in the one-nonfull and
   both-full cases.**  It must align operation colours with rooted bags or
   preserve them through an exact seven-separation.  More graph-code filters
   or static shore-demand counts are not progress on this gate.
3. **Then synchronize the seven anchored list cores.**  Use the changing
   deletion responses to eliminate saturated singleton and tight odd-cycle
   cores; the static `C_7\vee C_6` witness does not couple those operations.

Further finite enumeration is useful only when attached to one of these
unbounded lifts.  The present bottleneck is label-preserving synchronization,
not an incomplete boundary census.
