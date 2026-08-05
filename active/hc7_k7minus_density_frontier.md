# Density frontier for the `K_7^-` six-colour route

**Status:** sole active research frontier; not a proof of the `K_7^-`
six-colour conjecture or of `HC_7`.  The `4n-2` extremal theorem below is
the sole active target.  Its computation-free critical-host entrance,
seven-cut reduction, safe degree-seven contraction, strict-surplus
minimal-enemy structure, and essential-edge six-separation theorem have
written proofs with separate GREEN internal audits.  The exceptional-centre
and direct `HC_7` programmes remain frozen conditional refinements.

## 1. Proved entrance reduction

Let `G` be a hypothetical minor-minimal non-six-colourable graph with no
`K_7^-` minor.  The new
[two-literal-`K_5` theorem](../results/hc7_k7minus_two_literal_k5_exclusion.md)
proves, more generally, that every six-connected graph with two distinct
literal `K_5` subgraphs contains a `K_7^-` minor.  Thus `G` has at most one
literal `K_5`.

Every degree-seven vertex lies in that clique, if it exists, and the
audited
[private-triangle theorem](../results/hc7_k7minus_all_degree7_k5_exclusion.md)
excludes five degree-seven vertices in one clique.  Therefore

\[
 n_7\le4,
 \qquad
 |E(G)|\ge4|V(G)|-2.                                   \tag{1}
\]

If `b` is the number of exceptional degree-eight vertices and

\[
                  \tau=\sum_{i\ge10}(i-9)n_i,
\]

then all degree-seven and nonexceptional degree-eight vertices fit in the
unique possible clique:

\[
                         n_7+(n_8-b)\le5.                \tag{2}
\]

Combining (2) with the audited Jakobsen defect gives

\[
                         b\ge20-n_7+\tau.                \tag{3}
\]

If `n_7<=3`, parity strengthens the edge bound to `m>=4n-1` and (3) gives
`b>=17+tau`.  If `n_7=4`, contracting the unique mixed `K_5` gives a
simple five-connected target-free minor outside the Jakobsen cockade
family; hence

\[
 n\ge37,
 \qquad n_8\ge33+\tau,
 \qquad b\ge32+\tau.                                   \tag{4}
\]

Consequently every hypothetical host satisfies

\[
                         \boxed{b\ge17+\tau}.            \tag{5}
\]

The exceptional-vertex subgraph is `K_5`-free.  The separately written
[exceptional-neighbourhood theorem](../results/hc7_k7minus_exceptional_neighbourhood_completion.md)
also proves that every exceptional neighbourhood has independence number
exactly three and identifies the terminal exterior-component allocation
condition.

Exceptional anti-neighbourhood connectivity is now proved whenever
`n_7>0`: degree-seven incidence supplies a literal `K_5`, while the audited
two-component exceptional-centre theorem would exclude all literal `K_5`s.
The disconnected case is therefore confined to `n_7=0`; there the same
two-component theorem forces at least `25+tau` exceptional vertices.

The entrance proof is computation-free.  The exact degree-seven
neighbourhood theorem uses a star contraction, one fixed six-colouring,
Kempe-chain connectivity, and Kriesell--Mohr Theorem 7.  The new
two-clique theorem then uses only Menger linkage and explicit branch-set
splitting; it removes the former two-clique tight layers entirely.

## 2. Primary extremal target

The following statement is sufficient for the `K_7^-` six-colour
conjecture:

> **Extremal target.** Every seven-connected `n`-vertex graph with at least
> `4n-2` edges contains a `K_7^-` minor.

Equivalently, every seven-connected `K_7^-`-minor-free graph should satisfy

\[
                              m\le4n-3.                 \tag{6}
\]

This target is not proved.  It remains the clean global statement to
attack: it uses only seven-connectivity and density, while any
minor-minimal colouring counterexample automatically satisfies its
hypotheses.

Norin and Totschnig prove that a four-connected graph at the
`4n-8` threshold contains the graph obtained from `K_7` by deleting two
edges with a common end, apart from their explicit small exception.  The
six-edge numerical difference at the present threshold is global
accounting, not a canonical set of six edges near the deficient branch
set.  No localisation principle of that kind is claimed here.  Their paper
identifies a `K_7^-` strengthening as the missing extremal input for the
six-colour conjecture:
[Norin--Totschnig, Theorem 6 and Conjecture 21](https://arxiv.org/abs/2507.03244).

The critical-host count also leaves the following sufficient statement:

> **Exceptional-count target.** Every seven-connected, seven-chromatic,
> `K_7^-`-minor-free graph whose every proper minor is six-colourable has at
> most sixteen exceptional degree-eight vertices.

This is unproved and is no longer a parallel active target.  It is retained
as a conditional refinement because it would contradict (5) while keeping
the proper-minor colouring responses.  Its exact reductions and barriers
are in the
[seven-exceptional technical frontier](hc7_k7minus_seven_exceptional_frontier.md).

The former `4n-4` and `4n-5` targets are stronger open statements.  They
are no longer the exact sufficient obligations because the critical-host
density entrance has moved to `4n-2`.

## 3. Critical-host entrance and superseded tight layer

The audited
[private-triangle Kempe allocation theorem](../results/hc7_k7minus_all_degree7_k5_exclusion.md)
excludes a literal `K_5` whose five vertices all have degree seven.  Together
with the two-clique theorem, this gives the critical-host inequalities in
Section 1 and makes the former `4n-5` equality programme obsolete.

The allocation constructs two disjoint connected sets, one meeting all five
private triangles and the other meeting at least four.  This is exactly
enough for a `K_7^-` model, but it does **not** prove the stronger
two-transversal or bond statement.  The full superseded equality analysis is
preserved in the [archived ledger](../archive/RESEARCH_LEDGER_2026-08-02.md)
and its promoted theorem files.

## 4. Boundary-full connected subgraphs and exact contraction obstruction

The proved
[connected-subgraph capacity and component-contraction theorem](../results/hc7_k7minus_seven_boundary_component_descent.md)
gives the underlying packing bound.  Let `S` be an order-seven
cut, let `G-S` have `r` components, and let `\pi_S(G)` be the maximum number
of pairwise vertex-disjoint connected subgraphs of `G-S` each adjacent to
all of `S`.  Then

\[
 2\le r\le\pi_S(G)\le4,
 \qquad
 N(C)=S\text{ for every component `C`},
 \qquad
 \kappa(G[S])\le6-\pi_S(G).                           \tag{7}
\]

For `r=2`, the boundary is `K_5`-minor-free; for `r=3`, it has at most nine
edges; and the older packing argument allowed `r=4` only with a matching
plus isolated vertices on the boundary.  The new audited
[three-component theorem](../results/hc7_k7minus_seven_cut_three_component_bound.md)
eliminates that last case without a density or colouring hypothesis:

\[
                         2\le r\le3,
\]

and `r=3` forces `Delta(G[S])<=3`.

The separately audited
[critical seven-cut capacity theorem](../results/hc7_k7minus_critical_seven_cut_capacity.md)
adds the proper-minor six-colouring hypothesis of the hypothetical critical
host and obtains the strict bound

\[
                         2\le r\le\pi_S(G)\le3.
\]

The separately audited
[three-component `3,2,2` cut theorem](../results/hc7_k7minus_three_component_seven_cut_exclusion.md)
uses that exact partition, two crossless-shore web completions, and planar
precolouring extension to eliminate the three-component case.  Hence every
order-seven cut in the critical host has exactly two components.  One
component has packing number one, the two packing numbers sum to at most
three, and `G[S]` has an edge.  These conclusions depend essentially on
proper-minor six-colourability and do not apply to an arbitrary dense
seven-connected graph.

For a component `C_i`, put

\[
 n_i=|V(C_i)|,\quad
 e_i=|E(C_i)|+|E(C_i,S)|,\quad
 \delta_i=e_i-4n_i,\quad
 q=|E(G)|-(4|V(G)|-4).                                \tag{8}
\]

For a nonempty component set `X`, contracting every `C_i`, `i\in X`, gives
`H_X` with exact surplus

\[
 |E(H_X)|-(4|V(H_X)|-4)
   =q+\sum_{i\in X}(3-\delta_i).                      \tag{9}
\]

The theorem also gives an exact, not merely sufficient, connectivity test:
`H_X` is seven-connected precisely when deleting any nonempty subfamily
`D\subseteq X` together with any external set `Z` satisfying
`|D|+|Z|\le6` leaves the corresponding graph connected.  Consequently a
descent-minimal graph has a concrete failure certificate whenever a
nonsingleton component is density-eligible.  In particular,

\[
 |V(C_i)|\ge2,\quad \delta_i\le3+q
 \quad\Longrightarrow\quad
 G-V(C_i)-Z\text{ is disconnected for some }|Z|\le5. \tag{10}
\]

The former stronger cut-reduction target was:

> **Seven-cut reduction target.** Let `G` be seven-connected with
> `|E(G)|>=4|V(G)|-4`, and let `S` be a vertex cut of order seven.  Then
> either `G` contains a `K_7^-` minor, or `G` has a proper minor `H` that is
> seven-connected and satisfies `|E(H)|>=4|V(H)|-4`.

This target remains open and frozen.  It is equivalent in strength to the former bare global
`4n-4` extremal statement, which is strictly stronger than the current
`4n-2` sufficient target in Section 2; it is not an ordinary preliminary
lemma.  The global `4n-4` statement trivially gives the first outcome.
Conversely, choose a proper-minor-minimal counterexample to that same-threshold
statement.  If it were eight-connected,
then `G-e` would be seven-connected for every edge `e`, while minimum degree
eight would give `|E(G-e)|>=4|V(G)|-1`; hence `G-e` would be a smaller
counterexample.  Thus the chosen graph has an order-seven cut, and either
outcome of the target is contradictory.  The proved theorems do not close
this stronger dichotomy.  The new three-component theorem removes `r=4`
in every seven-connected target-free host, but it does not preserve the
density under a shore contraction.

## 5. Minimal-enemy reduction and exact next theorem

Assume the `4n-2` target false.  Choose a target-free counterexample `G`
first with minimum order and then with minimum size, and write

\[
                      q(G)=|E(G)|-(4|V(G)|-2).
\]

Jakobsen's theorem already gives `|V(G)|>=21`: for `n<=20`, the inequality
`4n-2>=9n/2-12` reaches his `K_7^-` threshold, and seven-connectivity
excludes the clique-sum exceptions.  The exact published input is recorded
in the audited
[degree-defect theorem](../results/hc7_k7minus_five_exceptional_vertices_reduction.md#theorem-4-five-exceptional-degree-eight-vertices).
At the first possible orders, its strict inequality leaves only

\[
 (n,m)=(21,82),\quad(22,86),
 \qquad n=23:\ m\in\{90,91\}.                         \tag{11}
\]

A recorded, separately checked preliminary falsification screen excludes
the principal natural extremal
families.  Every seven-connected complete multipartite graph has a `K_7`
minor: take one singleton branch set from each part and complete the seven
bags with disjoint cross-part edges; seven-connectivity gives the matching
inequalities.  Nontrivial clique sums and the Jakobsen and Jørgensen
cockades either retain a cut of order at most six or, after enough universal
vertices are added to raise connectivity, contain a `K_7` minor.
Universal planar multi-apex constructions similarly contain `K_7^-` by the
rooted-diamond theorem.  Thus the unexcluded constructional zone begins
with a genuinely rewired near-cockade or a noncomplete adhesion of order
seven, not a blow-up, cone, or ordinary clique sum.  This screen is not an
exhaustive or separately promoted theorem.

The audited
[degree-seven safe-contraction theorem](../results/hc7_k7minus_degree7_safe_contraction.md)
gives a degree-seven vertex `v` and an incident edge `vs` with

\[
 |N(v)\cap N(s)|\le3,
 \qquad q(G/vs)\ge q(G).
\]

The quotient cannot remain seven-connected.  Pulling back a minimum cut
returns an exact order-seven cut containing `v,s`, with at most three
complementary components.  In the two-exterior case every incident edge is
density-preserving, and Yuan's fragment theorem yields the exact nested
root-swap residue recorded in Theorem 3 of that result.

If `q(G)>0`, minimality also makes `G` minimally seven-connected.  The
audited
[strict-surplus theorem](../results/hc7_k7minus_strict_surplus_minimal_enemy.md)
then combines Mader's forest structure with Schmidt's exact count.  More
than half the vertices have degree seven, the remaining induced graph is a
forest, and at least `ceil(n_7/2)` distinct density-preserving
noncontractible edges cover all degree-seven vertices.  Each is certified
by an exact order-seven cut.  Moreover, those edges contain either an edge
joining two degree-seven vertices or a two-edge star whose two leaves have
degree seven.

The audited
[essential-edge theorem](../results/hc7_k7minus_essential_edge_six_separation.md)
gives a second exact view.  Deleting any essential edge leaves a
six-connected graph with two boundary-full shores behind an order-six cut;
the deleted edge is the sole cross-edge.  If

\[
 \delta_X=|E(G[X])|+|E_G(X,S)|-4|X|,
\]

then each shore contraction has exact surplus

\[
                         q(G/X)=q(G)+2-\delta_X.
\]

The audited
[`K_4`-reserve inequality](../results/hc7_k7minus_six_cut_k4_reserve_inequality.md)
now adds a direct boundary restriction.  If the six-boundary contains a
literal clique `Z` of order four and `S-Z=\{r,s\}`, then

\[
                 d_G(r)+d_G(s)
                 \ge15+q(G)+\mathbf1_{rs\in E(G)}.    \tag{12}
\]

Thus the two vertices outside a boundary `K_4` cannot both have degree
seven.  This is an unbounded theorem on the primary proof spine; it does
not prove that every relevant boundary contains such a clique.

The next theorem must therefore prove one of the following:

1. one safe degree-seven edge is seven-contractible;
2. the family of exact seven-cuts uncrosses to an explicit `K_7^-` model;
3. an essential-edge shore is both density-eligible and contractible while
   retaining seven-connectivity.

The immediate campaign is the strict-surplus `K_4`-reserve aggregation
problem.  Combine (12) with the audited safe-edge cover and the exact
essential-edge cuts to force either a boundary `K_4` with two degree-seven
complementary vertices, an explicit `K_7^-` model from crossing cuts, or
the shore contraction in outcome 3.  Success would eliminate `q(G)>0` and
reduce the target to its exact-density layer.

The live obstruction is precise.  A trace-one fragment may support a
nested root swap rather than collapse to a singleton.  At an essential-edge
six-separation, the rooted-diamond construction supplies only six of the
seven required branch sets.  Kawarabayashi's odd-connectivity
contractible-edge argument is a relevant architecture, but its
`K_4^-`-free hypothesis supplies a triangle-free edge and hence a lower
bound on both shores behind every failed contraction.  A density-safe edge
here can have three common neighbours.  Its cut can therefore end in the
nested root-swap residue, and neither the safe star nor the global forest
count forces a strictly smaller safe shore.  This is the first unsupported
inference in that attempted adaptation.

The robust `K_6`-model transversal has also been tested and frozen as a
principal mechanism.  If `F` is a minimum edge set meeting every `K_6`
model, each `e\in F` restores a one-edge witness in `G-F+e`; splitting the
branch set containing `e` leaves at least two missing incidences to the
other five bags.  Witnesses for different edges need not share labels or
branch sets, and deleting `F` loses seven-connectivity.  The smallest
repair would itself be a new saturation theorem forcing two compatible
critical extensions in the common host.  This does not refute the
transversal statement.

The two-root dominating-`K_5` augmentation route stops at a parallel exact
point.  A normalised model has final induced cycle `C`; closure would follow
from a `C`-touching rooted `K_5^-` model after deleting its first two,
possibly large, bags.  Failure of that rooted model is not known to return
a cut of order at most six—existing absorption gives a weighted separator
of order at least seven.  In a critical host this proposed dichotomy would
already settle the whole conjecture, so it is not being treated as a
smaller fallback lemma.

Further isolated boundary classifications, small graph-code
eliminations, or exceptional-count increments are frozen unless they
resolve one of the three displayed outcomes.

The positive-surplus atom route gives an additional, independently audited
reduction.  The
[generalised safe-atom theorem](hc7_k7minus_generalised_safe_atom_reduction.md)
leaves only singleton, edge, three-vertex path and triangle atoms behind
two-sided order-seven cuts.  The
[low-endpoint refinement](hc7_k7minus_low_endpoint_safe_atom_reduction.md)
isolates a five-rooted `K_6` problem, and the computer-assisted
[four-distinct-miss path theorem](hc7_k7minus_p3_atom_yuan_draft.md)
eliminates one complete path case.  These statements require `q(G)>0` and
do not address the exact-surplus layer.

## 6. Auxiliary five-connected laboratory

The current bounded laboratory is the stronger auxiliary statement

\[
 \kappa(G)\ge5,\qquad |E(G)|\ge4|V(G)|-7
 \quad\Longrightarrow\quad K_7^-\preccurlyeq G.
\]

It is not proved and is not a second primary target.  Its value is that a
minimum enemy is now reduced to exact density, connectivity five, and one
five-root reserve-or-high-excess-descent lemma.  The full audited chain,
recorded nonclosures, and exact survivor are in the
[auxiliary five-connected frontier](hc7_k7minus_e5_frontier.md).

The decisive E5 gate found neither a proof nor a counterexample.  It did
produce the direct inequality (12) and an audited
[protected rooted-equality peel](../results/hc7_protected_rooted_k42_equality_peel.md).
The latter preserves labels inside an exact rooted pair but has no proved
host-reinsertion theorem.  Further E5-specific boundary enumeration is
therefore frozen; only an unbounded transferable theorem or a genuine E5
counterexample reopens it.

## 7. Frozen prior laboratories

The previous exceptional-centre and direct `HC_7` programmes are preserved
in the [archived ledger](../archive/RESEARCH_LEDGER_2026-08-02.md), the
[exceptional-centre frontier](hc7_k7minus_seven_exceptional_frontier.md),
and the [bounded-interface frontier](hc7_bounded_interface_synchronization_frontier.md).
They remain sources of audited tools but are not parallel active targets.
The universal seven-cut theorem above supersedes the former four-component
residue; in an arbitrary extremal enemy only the two- and three-component
cases remain, while every critical-host order-seven cut has exactly two
components.  No frozen boundary census or operation-coupled local residue
is being presented as progress on the unconditional target.
