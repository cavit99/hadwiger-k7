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
   crossing identities, but currently leaves either a boundary of order
   six or a density-preserving minor whose five-connectivity is unproved.

Consequently one may choose, with minimum order, a component `C` behind a
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
items 7 and 8 supersede the generic description: the remaining local
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
  the crossing singleton orientation, the smallest open repair is a
  boundary-collapse lemma which turns a strict high-potential intersection
  behind at most six vertices into an order-five high-excess component,
  unless the anchored model already exists.  The alternative two-vertex
  orientation needs a near-universal edge-completion lemma preserving
  five-connectivity or returning the same strict descent.
- Retaining a [six-vertex boundary contact quotient](../barriers/hc7_e5_six_boundary_quotient_barrier.md)
  also does not force the target.  A dependency-free finite verifier gives
  a ten-vertex, 27-edge quotient in which the selected component sees the
  anchor and all five roots, yet every seven-bag model has at least two
  missing adjacencies.  This refutes only the quotient abstraction: it is
  not an `E5` enemy and does not encode the internal high-side structure or
  simultaneous exact-cut family.
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
