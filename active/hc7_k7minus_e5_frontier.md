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

## 4. Recorded nonclosures

Two tempting continuations are exhausted and must not be repeated.

- [Ordinary two--three linkage](hc7_k7minus_e5_two_component_rooted_reduction.md#the-two--three-linkage-route-is-sharp-at-lobe-excess-one)
  closes the relevant row when the low lobe has excess at least two, but is
  sharp at excess one.  Its path example is diagnostic and does not satisfy
  the full minimum-enemy hypotheses.
- [Rooted-model overlap and critical-cycle descent](hc7_k7minus_e5_three_component_root_overlap_nonclosure.md)
  can return a smaller component, but neither construction preserves the
  high-excess inequality.  It therefore does not give a well-founded
  descent.

These findings do not refute the five-root reserve-or-descent target.  They
show that its proof must couple the low interface to the opposite dense
lobe or establish a sharp equality structure.  Further isolated boundary
codes or unrooted minor models are not accepted terminal outcomes.

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
