# Auxiliary five-connected extremal laboratory

**Status:** current structural laboratory for the seven-connected `4n-2`
target.  The auxiliary theorem below is conjectural.  The reductions listed
here have written proofs and separate internal audits; those audits are not
external peer review.

## 1. Auxiliary target

Write `K_7^-` for `K_7` with one edge deleted.  The auxiliary statement is

> **(E5).** Every five-connected graph `G` with
> \[
> |E(G)|\ge 4|V(G)|-7
> \]
> contains a `K_7^-` minor.

This is deliberately stronger than the sole primary target: `(E5)` would
imply the seven-connected `4n-2` theorem, but it is not needed in its full
generality to settle Norin--Totschnig Conjecture 21.  No counterexample to
`(E5)` is known here, and `(E5)` is not proved.

## 2. Proved minimum-enemy reduction

Assume `(E5)` false and choose a counterexample first with minimum order and
then with minimum size.  The following chain is now proved.

1. [Positive surplus is impossible](hc7_k7minus_e5_strict_surplus_elimination.md),
   so the minimum enemy has exactly
   \[
   |E(G)|=4|V(G)|-7.
   \]
2. It has [connectivity exactly five](hc7_k7minus_e5_exact_connectivity_reduction.md).
   The two local inputs are the computation-free
   [degree-six common-neighbour bound](hc7_k7minus_degree6_common_neighbour_bound.md)
   and the computer-assisted, unbounded
   [saturated degree-seven exclusion](hc7_k7minus_degree7_common_neighbour_exclusion.md).
3. For every five-cut `S`, each component of `G-S` is adjacent to all five
   vertices of `S`.  Dense boundaries are excluded by the
   [five-separator reductions](hc7_k7minus_e5_k5minus_cut_elimination.md),
   and [four complementary components are impossible](hc7_k7minus_e5_independent_four_component_elimination.md).
   Thus every five-cut has two or three complementary components.
4. An eight-edge boundary transfers the required high excess to a
   [strictly smaller component behind a cut with at most seven boundary
   edges](hc7_k7minus_e5_eight_edge_cut_descent.md).  The complete
   [seven-edge reduction](hc7_k7minus_e5_seven_edge_cut_reduction.md), its
   [disjoint-star-and-edge completion](hc7_k7minus_e5_star_edge_cut_elimination.md),
   and the [`K_{2,3}` equality-row theorem](hc7_k7minus_e5_k23_331_elimination.md)
   eliminate the remaining seven-edge rows.
5. In the three-component case the boundary is triangle-free.  The
   [sparse three-component theorem](hc7_k7minus_e5_three_component_sparse_elimination.md)
   eliminates every row in which all three lobe excesses are at most three,
   as well as every star-boundary row.  The
   [concentration theorem](hc7_k7minus_e5_three_component_concentration.md)
   then proves that the high lobe has excess at least five.  When the
   boundary has at least two edges, each low lobe has excess at most one;
   if both are singletons, the high closed shore has exactly `4|V|-9`
   edges.  Thus the remaining density is sharply concentrated in one lobe
   over a non-star triangle-free boundary.
6. In the two-component case, the
   [rooted cross-shore and contraction reductions](hc7_k7minus_e5_two_component_rooted_reduction.md)
   close several complete families.  They reduce the unresolved case to a
   low-excess lobe and an opposite lobe which must retain five prescribed
   roots and one additional branch set.
7. In the exact three-component residue with two singleton lobes, the
   [singleton-contraction uncrossing theorem](hc7_k7minus_e5_singleton_contraction_uncrossing.md)
   produces five overlapping rooted three-cuts in the dense shore.  If
   none yields a strict high-excess descent, their small sides have order
   at most two and consist entirely of boundary roots.  Boundary
   classification and Yuan's fragment theorem then leave only
   `G[S]=P_3` disjoint union `K_2`, with at least three of its four
   degree-one roots having degree five in `G`.  Their two-vertex neighbour
   sets in the dense component have distinct representatives, and every
   resulting leaf--neighbour edge belongs to a further exact five-cut.
   The audited
   [anchored four-root reduction](hc7_k7minus_e5_anchored_four_root_reduction.md)
   strengthens the dense-component order bound to eight.  Deleting any
   degree-five leaf leaves an internally four-connected four-root graph
   with exactly `4|V|-8` edges.  It has separately a rooted `K_4` model
   and a rooted `K^*_{4,2}` supply whose augmented helper meets the leaf
   and one of its two dense neighbours.  Every three--two partition of
   the five boundary roots also has disjoint connected carriers.
8. The audited
   [leaf-cut quotient classification](hc7_k7minus_e5_leaf_cut_quotient_nonclosure.md)
   proves that each further exact five-cut has one high component and
   exactly one low component of order at most two.  Contracting both
   components gives a seven-vertex quotient with at most eighteen edges,
   so its `K_7^-`-minor-freeness is automatic and supplies no synchronising
   information.  Keeping the high component uncontracted gives exact
   crossing identities and a strict intersection inside `A`.
9. The audited
   [singleton-neighbour boundary-collapse theorem](hc7_k7minus_e5_singleton_neighbour_boundary_collapse.md)
   eliminates the crossing singleton orientation in which four roots lie
   in the further cut.  Replacing one root of the original cut by the
   selected dense neighbour leaves the four-vertex component
   `{x,y,t,q_t}` with excess one; the universal five-cut lemma therefore
   forces strict high-excess descent inside `A-{p,q_t}`.  The surviving
   `q_t`-singleton rows have at most three roots in the further cut and
   natural boundary orders `9-s` equal to six, seven or eight.  The
   two-vertex low orientation still yields a density-preserving minor whose
   five-connectivity is unproved.
10. The audited
    [atomic six-boundary reduction](hc7_k7minus_e5_six_boundary_atomic_reduction.md)
    treats the first surviving row `s=3`.  It reduces failure of the
    four-root model to either a lifted order-three atom `{p}` or `{p,b}`, or
    one excess-two helper edge `{b,c}` behind an order-four separation.  A
    second density-safe contraction then gives the
    [companion-cut elimination](hc7_k7minus_e5_s3_companion_cut_elimination.md):
    after refining the minimum-lobe choice by maximum excess, the helper-edge
    branch produces a same-order lobe of excess nine, whereas the selected
    lobe has excess eight.  That branch is impossible.  The `s=3` row is
    therefore confined to the two order-three atoms, and deleting either
    leaves at least `4|V|-7` edges in the residual graph.
11. The audited
    [three-separator edge-atom elimination](hc7_k7minus_e5_s3_edge_atom_elimination.md)
    shows that the two-vertex outcome is not terminal.  If its excess is
    one, the degree-five vertex `p` itself defines another exact five-cut
    with singleton low side.  If its excess is two, a density-safe
    contraction and a rooted six-bag model in the returned high shore give
    an explicit `K_7^-` model.  Thus the sole remaining order-three
    obstruction in the `s=3` singleton row is the singleton `{p}`.
12. The audited
    [singleton-triangle contraction](hc7_k7minus_e5_s3_triangle_contraction_reduction.md)
    absorbs both exact singleton cuts at once.  Contracting the triangle
    `{p,t,q_t}` loses at most six edges and gives a proper target-free graph
    `J` with

    ```text
    kappa(J)=4,                    |E(J)|>=4|V(J)|-5.
    ```
    Every four-cut of `J` contains the contracted vertex.  Lifting it gives
    a genuinely new order-six cut in `G`; each complementary component is
    adjacent to the other three cut vertices and meets the triangle in
    aggregate.  Norin--Totschnig's theorem gives a `K_7^vee` minor in `J`,
    but does not prescribe how its contracted-vertex bag splits over the
    triangle.
13. The
    [lifted triangle-cut refinement](hc7_k7minus_e5_s3_triangle_cut_refinement.md)
    uses five-connectivity and the three exact exterior neighbours of each
    triangle vertex.  Every complementary component meets at least two
    triangle vertices, and there are at most four components.  A component
    missing one triangle vertex either has order at most two, or has order
    exactly `|A|` and is accompanied by one singleton.  If no such high
    component occurs, some component is adjacent to all six cut vertices.
    For a high component missing `p` or `q`, the cut differs from the
    corresponding singleton adhesion by exactly one exchanged vertex and
    yields a two-vertex low component of excess one or two.  A high
    component missing `t` either exactly reorients the original
    two-singleton residue, with the same order and excess, or leaves the
    singleton `u_t` and an explicit boundary edge-count normal form.
14. The audited
    [high-misser elimination](hc7_k7minus_e5_s3_high_misser_elimination.md)
    replaces the former maximum-excess secondary choice by maximising
    `Phi(Q,C)=delta_Q(C)+|E(G[Q])|` and then minimising the number of other
    components.  This replays the companion- and edge-atom eliminations.
    It excludes the `p`-, `q`-, and adjacent-`t` high missers by a strict
    potential improvement.  The nonadjacent `t` reorientation has another
    five-cut with a high-excess component of order below `|A|`, so it too
    is impossible.  Every lifted cut therefore has a six-full component.
15. The audited
    [six-full contraction reduction](hc7_k7minus_e5_s3_six_full_contraction_reduction.md)
    first excludes four complementary components.  If `C` is six-full,
    `D` is another component, `u` is a triangle vertex met by `D`, and
    `v in C` is adjacent to `u`, then `uv` has at most three common
    neighbours.  Contracting `uv` is density-safe and produces a
    four-connected but not five-connected proper minor.  Every four-cut
    contains the contracted vertex and lifts to an exact five-cut through
    `u,v` in `G`.  A non-six-full component misses a unique triangle
    vertex, has order at most two, and lies behind the companion five-cut
    obtained by deleting that vertex from the six-cut.  Such a component
    exists whenever there are three complementary components.  Finally,
    every returned five-cut has exactly two components: one singleton
    whose neighbourhood is the cut, and one high-excess component of
    order `|A|+1`.  The degree-five triangle count and the central
    five-cut eliminate every order-`|A|` alternative.
16. The audited
    [second-contraction kernel reduction](hc7_k7minus_e5_s3_second_contraction_kernel_reduction.md)
    starts from the returned singleton.  Contracting it to the common
    anchor loses at most four edges.  If this drops four-connectivity, an
    adjacent returned singleton gives an exact labelled `K_2` kernel behind
    a six-set.  If four-connectivity survives and a nontrivial four-cut has
    a side missing an original contraction endpoint, the selected-lobe
    potential gives a labelled `P_3` or `K_3` kernel.  The promoted
    computer-assisted
    [six-boundary screen](../results/hc7_k7minus_e5_six_boundary_kernel_screen.md)
    has 11,914 independently checked certificates and sharp thresholds for
    all six five-full and six-full cases.  Combined with the exact excess
    identities, it eliminates every kernel configuration with one connected
    non-six-full opposite component.  In a split opposite shore, every
    non-six-full component is a full singleton or full edge of order at most
    two.  This does not bound the six-full components.

Consequently one may choose with minimum order a component `C` behind a
five-cut `S` such that

\[
 \delta_S(C)=|E(G[C])|+|E_G(C,S)|-4|C|\ge4.
\]

Its boundary has at most six edges.  Indeed, the eight-edge theorem descends
to a smaller high-excess component, and every seven-edge two-component row
is closed by the four complement-type theorems; a triangle-free
three-component boundary has at most six edges.  This minimum high-excess
lobe is the strongest coherent endpoint of the present reduction.

For the two-singleton three-component branch, the stronger endpoints in
items 7--16 supersede the generic description: the remaining local
object is three or four degree-five leaf roots with distinct representatives
in the dense component.  Each has one neighbour in `G[S]` and exactly two
neighbours in the dense component, and its three neighbours in the closed
shore form a separator.  The `P_5` and `C_5` possibilities force a strict
high-excess descent; the other discarded boundary types contradict the
exact small-side structure and five-connectivity.

The shared [degree-six cut-capacity and exact-excess theorem](hc7_k7minus_degree6_cut_capacity_excess.md)
supplies the rooted models and density identities used in several of these
steps.

## 3. Exact remaining lemma

The common unresolved statement is the following rooted theorem.

> **Five-root reserve-or-descent target.** Let `G` be a minimum `E5` enemy,
> and let `C` be a minimum-order component behind a five-cut `S` satisfying
> `\delta_S(C)\ge4`.  Then either
>
> 1. `G[C\cup S]` has a `K_6`-minor model with five distinct bags containing the
>    five members of `S` and a sixth bag disjoint from `S`; or
> 2. `G` has a strictly smaller component `C'` behind a five-cut `S'` with
>    `\delta_{S'}(C')\ge4`.

The first outcome combines with the opposite whole lobe to give seven
branch sets with at most one missing adjacency.  The second is a genuine
well-founded descent.  An unrooted `K_6` model, a smaller arbitrary side,
or a separation which loses the high excess is insufficient.

The ordinary extremal theorem for an unrooted `K_6` does not control which
bags meet the five prescribed roots.  That distinction, rather than the
existence of some `K_6` minor, is the unresolved content.

In the exact two-singleton branch this target has narrowed further.  Fix a
degree-five leaf root `t`, put `Z=S-{t}`, and choose `p` among the two
dense-component neighbours of `t`.  It is enough to prove the **anchored
four-root `K_5`-or-descent target**: for some such `t,p`, either `H-t`
has four pairwise adjacent bags rooted at `Z` and a disjoint fifth bag
containing `p` and adjacent to all four, or there is a component of order
below `|A|` behind a five-cut which retains excess at least four.  In the
first outcome

```text
{x,t}, {y}, the four Z-root bags, the p-bag
```

is an explicit `K_7^-` model; the second is the required well-founded
descent.  The audited anchored reduction supplies the two relevant rooted
models and all three--two carriers separately, but does not synchronise
them.

Within the crossing `q_t`-singleton route, items 9--16 remove the four-root
row and the only internally four-connected obstruction in the next row
`s=3`.  They also eliminate or reclassify its two-vertex order-three atom.
In the exact residue put `F=G-{x,y,t,q_t}` and `Z=S-{t}`.  After changing
the adhesion when necessary, the remaining low component is the singleton
`{p}` and has

```text
N_F(p)=T,                         |T|=3,
T union {t,q_t} is an exact five-cut,
N_G(p)=T union {t,q_t}.
```

It has excess one and `F-p` has exactly `4|V(F-p)|-7` edges.  Contracting
`pt` alone is an audited nonclosure: it returns the inherited image of
`N(q_t)`.  The stronger singleton-triangle contraction absorbs both known
singleton cuts.  It gives a four-connected graph `J` of density at least
`4|V(J)|-5`, an unrooted `K_7^vee` minor, and a new exact four-cut through
the contracted vertex whose lift is an order-six separation in `G`.

The lifted cut is now sharper.  Every component meets at least two triangle
vertices.  The boundary-complement selection and the central five-cut
exclude every high triangle-missing component, so some component is
six-full; the original singleton twins then exclude four complementary
components.  There are exactly two or three.

For every other component and each triangle vertex which it meets, an edge
from that triangle vertex into a chosen six-full component is density-safe.
Its contraction gives a four-connected proper minor and each returned
four-cut lifts to an exact five-cut through the two ends.  Every returned
cut has a singleton and a high-excess component of order `|A|+1`; an
equal-order high component is impossible.

The returned singleton permits one further contraction.  Connectivity
failure gives the labelled `K_2` kernel; an endpoint-missing nontrivial cut
in the four-connected quotient gives the labelled `P_3` or `K_3` kernel.
The sharp finite screen and the exact excess identities eliminate every
connected opposite component missing one of the six new boundary vertices.
In a split opposite shore, each component missing a boundary vertex is a
full singleton or full edge of order at most two.

The exact surviving alternatives are now: the second quotient repeats the
anchored singleton-cut normal form; every eligible nontrivial cut is met on
both sides by both original contraction endpoints; or the kernel's opposite
shore has several bounded non-six-full components, one or more large
six-full components, or both.  The genuine two-six-full case remains a
density-sensitive labelled split.  Aggregate contact alone is not enough.

## 4. Recorded nonclosures

The following continuations are exhausted or require hypotheses stronger
than their tempting formulations.  They must not be repeated without a new
ingredient.

- [Ordinary two--three linkage](hc7_k7minus_e5_two_component_rooted_reduction.md#the-two--three-linkage-route-is-sharp-at-lobe-excess-one)
  closes the relevant row when the low lobe has excess at least two, but is
  sharp at excess one.  Its path example is diagnostic and does not satisfy
  the full minimum-enemy hypotheses.
- [Rooted-model overlap and critical-cycle descent](hc7_k7minus_e5_three_component_root_overlap_nonclosure.md)
  can return a smaller component, but neither construction preserves the
  high-excess inequality.  It therefore does not give a well-founded
  descent.
- [Singleton-contraction fragment uncrossing](hc7_k7minus_e5_singleton_contraction_uncrossing.md)
  gives pairwise disjoint boundary traces, not pairwise disjoint fragments.
  In the sole surviving `P_3` disjoint union `K_2` row, Hall's condition
  gives distinct dense-component representatives, but the corresponding
  exact five-cuts do not give simultaneous disjoint extensions or all ten
  adjacencies of an `S`-rooted `K_5` model.
- [All three--two terminal splits may have disjoint carriers](../barriers/hc7_three_two_carriers_do_not_force_rooted_k5.md)
  without a rooted `K_5`, even in a four-connected graph.  The octahedral
  example is three edges below the live closed-shore density and therefore
  refutes only direct carrier synchronisation, not the density-sensitive
  anchored target.
- [Fully contracted leaf-cut quotients](hc7_k7minus_e5_leaf_cut_quotient_nonclosure.md)
  have too few edges for target-freeness to impose any restriction.  In
  the crossing singleton orientation, the four-root row collapses by
  strict descent and the internally four-connected branch of the `s=3`
  row collapses by a same-order, higher-excess companion cut.  The
  alternative two-vertex orientation still needs a near-universal
  edge-completion lemma preserving five-connectivity or returning the same
  strict descent.
- Retaining a [six-vertex boundary contact quotient](../barriers/hc7_e5_six_boundary_quotient_barrier.md)
  also does not force the target.  A dependency-free finite verifier gives
  a ten-vertex, 27-edge quotient respecting the selected component's
  nonadjacency to `t`, yet every seven-bag model has at least two missing
  adjacencies.  The host-level `s=4` theorem bypasses this barrier by using
  the high-excess conclusion erased by contraction.  Thus the construction
  remains a valid contact-only barrier, not an obstruction to the now
  closed host row; it is not an `E5` enemy and does not encode the internal
  high-side structure or simultaneous exact-cut family.
- [Atomic portal concentration](hc7_k7minus_e5_six_boundary_atomic_reduction.md)
  is a real obstruction for a generic residual rooted model: the finite
  verifier finds minimum defect two for both surviving order-three atoms.
  It is not a host counterexample.  The host companion cut eliminates the
  order-four atom, and a further host argument eliminates or reclassifies
  the two-vertex order-three atom.  For the sole singleton atom,
  contraction of `pt` returns the already known four-cut and only the
  published unrooted `K_7^vee` conclusion.  Repeating that contraction is
  therefore exhausted.  Contracting the whole singleton triangle instead
  produces a new exact six-separation.  Five-connectivity upgrades its
  components to two-of-three triangle contact.  The later potential
  argument eliminates every high misser, and the twin path excludes four
  components, leaving two or three and at least one six-full component.
  Safe triangle-to-full contractions then force returned cuts with one
  singleton side and an order-`|A|+1` high side; all equal-order returned
  sides are eliminated.  The later second-contraction theorem converts a
  connectivity drop or an endpoint-missing nontrivial cut into one of three
  sharp labelled kernels and closes the connected non-six-full opposite
  shore.  It does not justify iteration through a larger contracted anchor,
  handle a cut met on both sides by both original endpoints, or localise
  density across several opposite components.  Only each individual
  non-six-full component has bounded labelled structure.
  The
  [contact barrier](../barriers/hc7_e5_triangle_lift_contact_barrier.md)
  shows that even two components complete to all six boundary vertices do
  not force `K_7^-` in the contracted abstraction.  A labelled split or a
  density-sensitive descent at the refined cut remains necessary.  The
  stronger
  [five-connected local barrier](../barriers/hc7_e5_six_full_local_structure_barrier.md)
  retains the exact triangle degrees and one six-full component, but lies
  four edges below the `E5` threshold.  Thus even local five-connectivity
  does not replace the missing density argument.
- **Bare relative connectivity and excess do not force the reserve.**  Let
  `H=K_{4,2,2}`.  Take as the five roots the four vertices in the part of
  order four and one vertex in a part of order two.  The three nonroots
  induce `P_3`, completing the roots makes `H` isomorphic to
  `K_8-2K_2`, and the open-side excess is

  ```text
  2+14-4(3)=4.
  ```

  Thus the rooted pair is internally five-connected and has exactly the
  coarse excess used in the laboratory.  It nevertheless has no `K_6`
  model with the five roots in distinct bags and a root-free sixth bag.
  The sixth bag consumes one of the three nonroots; at least three of the
  remaining nonroots would be needed to make the four mutually
  nonadjacent roots pairwise adjacent as rooted bags.

  Adding one vertex adjacent precisely to the five roots gives the
  five-connected target-free graph `K_{4,2,3}-e`, of order nine and size
  25.  It lies below the `E5` threshold 29.  Target-freeness follows
  already for `K_{4,2,3}`: among seven bags with at most one missing
  adjacency, at most four bags can lie wholly in individual multipartite
  parts, so at least three bags must meet two parts and hence require at
  least ten vertices in total.  This construction therefore refutes only
  the coarse local reserve inference, not `(E5)` or the minimum-enemy
  reserve-or-descent target.
- **A reserve-only conclusion is also wrong at near-Mader density.**  Let
  `H=K_{3,2,1,1,1}` and take the parts of orders three and two as the five
  roots.  Then

  ```text
  |E(H)|=24=4|V(H)|-8,
  ```

  and completing the roots gives `K_8`.  A root-free sixth bag leaves only
  two of the three singleton-part vertices for the root bags.  Two are
  needed to repair the three mutually nonadjacent roots, and a third is
  needed to repair the two mutually nonadjacent roots, so the requested
  reserve does not exist.  On the other hand `H` itself contains the
  explicit `K_7^-` model

  ```text
  {a_1,b_1}, {a_2}, {a_3}, {b_2}, {c_1}, {c_2}, {c_3},
  ```

  whose only missing adjacency is `{a_2}{a_3}`.  Hence an abstract lobe
  theorem must allow an explicit target outcome; the target-free
  minimum-enemy hypothesis is doing real work in the live statement.
- **Wollan's coefficient-four minimal-pair machinery does not apply.**  A
  minimum high-excess lobe suggests a `4`-massed pair, but Theorem 2.2 of
  Wollan's *Extremal functions for rooted minors* assumes
  `alpha>=|V(F)|`.  With `F=K_5` this requires `alpha>=5`, whereas the
  present excess supplies only the coefficient four.  The degree-eight
  vertex and four-common-neighbour conclusions from that theorem therefore
  cannot be imported here.  See
  <https://doi.org/10.1002/jgt.20301>.
- **An unrooted `K_6` cannot simply be rerooted.**  Mader's ordinary
  threshold supplies six unlabelled branch sets.  A five-fan from the
  prescribed roots to their union need not first meet five distinct bags.
  Splitting a repeatedly hit bag can destroy its connectivity or one of
  its five model adjacencies.  No current transfer theorem preserves all
  five root labels, so this first-hit step remains an unsupported
  inference rather than a standard consequence of five-connectivity.

These findings do not refute the five-root reserve-or-descent target under
the full minimum-enemy hypotheses.  They show that its proof must use
target-freeness and the opposite lobe, or establish a sharp equality
structure with a genuine high-excess descent.  Further isolated boundary
codes, unrooted minor models, or coefficient-four appeals to Wollan's
minimal-pair theorem are not accepted terminal outcomes.

## 5. Relation to the direct `4n-2` route

The direct positive-surplus route has also advanced.  Mader's generalised
atom theory reduces it to singleton, edge, path, and triangle atoms in
[the density-safe atom theorem](hc7_k7minus_generalised_safe_atom_reduction.md).
The [low-endpoint refinement](hc7_k7minus_low_endpoint_safe_atom_reduction.md)
isolates the same five-root reserve problem, and the computer-assisted
[four-distinct-miss path theorem](hc7_k7minus_p3_atom_yuan_draft.md)
eliminates one complete path case.  These results require positive
`4n-2` surplus and do not address the exact-surplus layer.

Thus the two programmes now meet at one mathematical issue: turn a dense,
internally five-connected lobe with five prescribed boundary roots into a
rooted six-bag model, or preserve enough density under a strict descent.
