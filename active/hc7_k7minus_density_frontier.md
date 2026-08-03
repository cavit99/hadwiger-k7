# Density frontier for the `K_7^-` six-colour route

**Status:** live conditional refinement; not a proof of the `K_7^-`
six-colour conjecture or of `HC_7`.  The six-connected two-clique theorem,
critical-host degree and exceptional-vertex consequences, private-triangle
allocation, and seven-boundary connected-subgraph, critical-host capacity,
three-component exclusion, and contraction theorems are written proofs with
separate internal audits
GREEN for their current revisions.  The local-completion theorem,
two-component nonfull and both-full reductions, and distinct
nonadjacent-miss fan-tree elimination are also written and separately
audited GREEN; their finite boundary claims have retained independently
checked verifiers.  The live list-core derivation is not separately
audited.  Both displayed finishing targets below remain conjectural.

This frontier supersedes the five-exceptional-vertices target as the main
laboratory for this side route.  It does not replace the primary all-degree
`HC_7` target in [`INDEX.md`](INDEX.md).

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

## 2. Two sufficient finishing targets

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
edges with a common end, apart from their explicit small exception.  Thus a
graph at the target threshold has six edges of surplus over that benchmark;
one possible proof is to use this surplus to recover one of the two missing
adjacencies.  Their paper explicitly identifies a `K_7^-` strengthening as
the missing extremal input for the six-colour conjecture:
[Norin--Totschnig, Theorem 6 and Conjecture 21](https://arxiv.org/abs/2507.03244).

The critical-host count supplies a second, less general but more structured
finishing theorem:

> **Exceptional-count target.** Every seven-connected, seven-chromatic,
> `K_7^-`-minor-free graph whose every proper minor is six-colourable has at
> most sixteen exceptional degree-eight vertices.

This is also unproved.  It would contradict (5) directly and therefore
settle the same six-colour conjecture while retaining all proper-minor
colouring responses.  Its exact reductions, barriers, and next allocation
gate are in the
[seven-exceptional technical frontier](hc7_k7minus_seven_exceptional_frontier.md).

The former `4n-4` and `4n-5` targets are stronger open statements.  They
are no longer the exact sufficient obligations because the critical-host
density entrance has moved to `4n-2`.

## 3. Private-triangle Kempe allocation and the excluded `4n-5` layer

Suppose equality held in the original density inequality (1), and let

\[
                         L=\{v_1,\ldots,v_5\}
\]

be one of the two all-degree-seven literal `K_5`s.  The proved local
classification gives five pairwise disjoint private triangles

\[
                         T_i=N(v_i)-V(L),               \tag{7}
\]

where `T_i` is anticomplete to `L-{v_i}`.  The
[equality connectivity and overlap theorem](../results/hc7_k7minus_equality_connectivity_reduction.md)
supplies the exact host for the Kempe argument.  Put `H=G-L`.  Then

\[
 \kappa(H)\ge5,
 \qquad |E(H)|=4|V(H)|-10.                             \tag{8}
\]

Let `A,B` be the two degree-seven `K_5`s, put
`R=G-(A\cup B)`, and let `k=|E(A,B)|`.  The same theorem proves

\[
 \kappa(R)\ge3,
 \qquad |E(R)|=4|V(R)|-15+k,
 \qquad k\le3,                                         \tag{9}
\]

and, before the final exclusion, gives

\[
 |V(R)|\ge19,
 \qquad
 |V(G)|\ge29.                                          \tag{10}
\]

It also proves an exact Hall and edge-critical Kempe fork.  In every
six-colouring of `H`, either four triangles use one common three-colour set,
or at least two colours occur on all five triangles.  For every edge
`v_ix`, with `x\in T_i`, a six-colouring of the edge-deleted graph forces
three two-colour components rooted at `x`; in the rigid branch, each meets
the same four specified triangles.

The earlier equality-case
[Kempe-component allocation and exclusion](../results/hc7_k7minus_equality_kempe_exclusion.md)
applies the argument symmetrically to the colour absent from `L`.  In the
rigid branch, a `p`-component and a disjoint `q`-component meet the same four
triangles, and one can absorb a path from the fifth.  In the all-five-colour
branch, a three-colour count selects two `p`-components whose connected
union meets all five triangles and a disjoint `q`-component meeting at least
four.  In either case these two connected sets and the five singleton
vertices of `L` form an explicit `K_7^-`-minor model, with at most the one
permitted owner adjacency missing.  This contradiction excludes equality
and proves the strict `4n-4` critical-host density bound.

The new
[private-triangle Kempe allocation theorem](../results/hc7_k7minus_all_degree7_k5_exclusion.md)
reconstructs this argument using only a literal `K_5`, five pairwise
disjoint private external triangles, connectedness after deleting the
clique, and a proper-minor six-colouring.  Seven-connectivity and the exact
degree-seven neighbourhood theorem supply those hypotheses for any
all-degree-seven literal `K_5`.  Thus the allocation is no longer confined
to density equality and gives the stronger entrance and tight-layer
structure in Section 1.

The proof does **not** establish the stronger standalone two-transversal
statement, nor the equivalent assertion that `H` has a bond meeting all five
private triangles.  One of the two connected sets may miss the fifth
triangle.  The critical equality host is nevertheless eliminated because a
`K_7^-` model permits exactly that one missing branch-set adjacency.  The old
two-transversal target is therefore retired as a live obligation, not
promoted as a proved theorem.

## 4. Boundary-full connected subgraphs and exact contraction obstruction

The proved
[connected-subgraph capacity and component-contraction theorem](../results/hc7_k7minus_seven_boundary_component_descent.md)
strictly sharpens the earlier seven-cut result.  Let `S` be an order-seven
cut, let `G-S` have `r` components, and let `\pi_S(G)` be the maximum number
of pairwise vertex-disjoint connected subgraphs of `G-S` each adjacent to
all of `S`.  Then

\[
 2\le r\le\pi_S(G)\le4,
 \qquad
 N(C)=S\text{ for every component `C`},
 \qquad
 \kappa(G[S])\le6-\pi_S(G).                           \tag{11}
\]

For `r=2`, the boundary is `K_5`-minor-free; for `r=3`, it has at most nine
edges; and for `r=4`, it is a matching plus isolated vertices.  The former
five-component case is impossible: five disjoint connected subgraphs outside
the boundary, each adjacent to every boundary vertex, give an explicit
`K_7^-` model.  In the four-component case, every component is either a
singleton or is two-connected.

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
 q=|E(G)|-(4|V(G)|-4).                                \tag{12}
\]

For a nonempty component set `X`, contracting every `C_i`, `i\in X`, gives
`H_X` with exact surplus

\[
 |E(H_X)|-(4|V(H_X)|-4)
   =q+\sum_{i\in X}(3-\delta_i).                      \tag{13}
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
 G-V(C_i)-Z\text{ is disconnected for some }|Z|\le5. \tag{14}
\]

The main structural step is therefore the following positive cut-reduction
theorem, not a density recount:

> **Seven-cut reduction target.** Let `G` be seven-connected with
> `|E(G)|>=4|V(G)|-4`, and let `S` be a vertex cut of order seven.  Then
> either `G` contains a `K_7^-` minor, or `G` has a proper minor `H` that is
> seven-connected and satisfies `|E(H)|>=4|V(H)|-4`.

This target is open.  It is equivalent in strength to the former bare global
`4n-4` extremal statement, which is strictly stronger than the current
`4n-2` sufficient target in Section 2; it is not an ordinary preliminary
lemma.  The global `4n-4` statement trivially gives the first outcome.
Conversely, choose a proper-minor-minimal counterexample to that same-threshold
statement.  If it were eight-connected,
then `G-e` would be seven-connected for every edge `e`, while minimum degree
eight would give `|E(G-e)|>=4|V(G)|-1`; hence `G-e` would be a smaller
counterexample.  Thus the chosen graph has an order-seven cut, and either
outcome of the target is contradictory.  The proved theorems do not close
this dichotomy.  The critical-host theorem eliminates `r=4` by a colouring
argument, while the contraction theorem identifies exactly what a successful
whole-component contraction in an arbitrary extremal graph must satisfy and
what separator certificate exists when it fails.

## 5. Ordered next attacks and research discipline

The all-degree-seven extraction is complete.  The general separator attack
removed `r=5`, strengthened the boundary statement to the maximum boundary-
full connected-subgraph packing number, proved two-connectivity of every
nonsingleton component when `r=4`, and replaced informal contraction
language by the exact surplus and connectivity criteria above.  The
critical-host reflection and planar-extension attack has now removed
`r=3,4` altogether.  Every critical order-seven cut is a two-shore cut with
packing vector `(1,1)`, `(1,2)`, or `(2,1)`.  The deficient-`P` attack first
eliminates the split remainder by a two-boundary colouring argument.  In a
connected remainder with exactly two lost universal adjacencies, every
nonconcentrated case is eliminated by a two-cut contradiction or a
two-boundary six-colouring; only the atomic bag `R={r,s}` with a `2+2`
support split survives.

The stronger model-level result applies before those cases.  In any exact
spanning `K_7^\vee` frame in a seven-connected host, either there is an
explicit `K_7^-` model or a nonempty proper connected part `Y` of one
universal bag has connected complement in that bag and `N_G(Y)` is an
actual separator of order at least seven.  The fixed two-edge response
retains at least five portals across the four universal bags, so this
dichotomy preserves the same named six-colouring.  It therefore bypasses
generic root-removal compatibility.  Globally minimizing boundary order now
gives either an exact two-shore seven-cut, or an order-eight boundary with
exactly two or three full complementary components and the
strengthened residual-boundary profile: the boundary is `K_5`-minor-free
and four-colourable, and its small vertex deletions satisfy the sharper
colouring and `K_t^-` exclusions in Proposition 11.
The minimum boundary order is `kappa(G)`.  In the order-eight branch,
`kappa(G)=delta(G)=8`, `n_7=0`, `|E(G)|>=4|V(G)|`,
`n_8>=25+tau`, and `b>=20+tau`.  Every degree-eight neighbourhood is a
minimum cut, so a disconnected exceptional anti-neighbourhood has exactly
two nonsingleton components, both full to the neighbourhood.  The fixed
double-star response also yields a persistent single-edge-deletion
colouring with exactly the same trace away from its root.  Eight-connectivity
forces every crossing-edge order-eight response into its clean-fan branch;
on a smallest two-shore side, the paired seven-column response has a
contact graph of minimum degree at most three.  If the fixed exceptional
root has connected anti-neighbourhood, the persistent single-edge response
forces that paired-column system directly at `N(r)`: the operation,
colouring trace, and surviving labelled near-clique model are all retained,
although the near-clique and column labels are not identified.
The global minimizer need not retain the nested labels or align the deleted
endpoints with its shores.  The immediate exceptional-centre attack is
therefore operation-labelled separator terminalization: force a common
boundary partition, an explicit `K_7^-` model, or a smaller component of
`G-N[z]` for a named exceptional `z`.  An arbitrary global minimum
separator is not an exceptional neighbourhood boundary.

For the bare extremal theorem, `r=4` remains open because an arbitrary
seven-connected graph at the density threshold has no proper-minor
six-colouring responses to reflect.  That separate route may use the surplus
identity and contraction-failure certificates, and must still handle the
sparse four-component boundary before reaching the weaker general
three-component restrictions.  No simultaneous chromatic-critical and
density-descent minimality reduction has been proved here.

Boundary arithmetic alone cannot finish this: the restrictions permit formal
excess patterns in which every whole-component contraction loses too much
density.  These are arithmetic patterns, not asserted graph examples.
Internal component structure is therefore the load-bearing next input.
The normalized Norin--Totschnig near-`K_7` upgrade remains a higher-risk
fallback because six global surplus edges need not occur at the deficient
branch set.

In parallel, the exceptional-centre route has completed its first
two-component attack.  The
[nonfull-attachment reduction](../results/hc7_k7minus_nonfull_attachment_reduction.md)
eliminates a common missed neighbour and reduces every other nonfull
configuration to connected-rich `(1,2)` seven-cuts or two overlapping
`(1,1)` cuts with explicit boundary-minor exclusions.  In the
one-nonfull cell, uniform defect-two reflection also forces the missed
vertex to have at most four boundary neighbours and at least two neighbours
in the full exterior component; an exact retained census leaves 28 possible
boundary types.  The new
[full-side vertex exclusion](../results/hc7_k7minus_one_nonfull_full_vertex_exclusion.md)
shows that no vertex of the full component can see all seven common boundary
vertices.  Consequently, in a smallest component among disconnected
exceptional anti-neighbourhoods, every degree-eight vertex has connected
anti-neighbourhood: the only exact recentering would violate that exclusion
and hence return a six-colouring.  This closes the complete order-seven/eight
matching-core rotation but not the general one-nonfull case.  The
[contracted-star and fan-tree theorem](../results/hc7_k7minus_distinct_miss_fan_tree_elimination.md)
now eliminates the complete distinct nonadjacent-miss cell: a reusable
Kempe response removes the `3K_2` parity obstruction and every other
independence-three boundary, while paired shore-confined fan trees produce
an explicit `K_7^-` for the two remaining common-six graphs.  Distinct
adjacent misses remain connected-rich `(1,2)` cuts.  In the both-full case,
the
[finite boundary and packet reduction](../results/hc7_k7minus_both_full_shore_reduction.md)
leaves seven exact boundary types and forces both exterior full-subgraph
packing numbers to equal one.  A fixed star-contraction colouring on the
six- and seven-demand reserve types must support at least two demands
through each shore.  This is a strict narrowing, not shore allocation:
the next theorem must synchronize changing critical colourings or extract
an additional residual contact inside a packet-one shore.  Static boundary
labels are ruled out by the
[balanced-label and mechanism barriers](../barriers/hc7_k7minus_shore_allocation_barrier.md).
The complementary multi-centre attack still seeks to synchronize the seven
anchored list cores arising from colourings of `G-x`; one static list census
is blocked by the explicit `C_7\vee C_6` mechanism witness.

Further enumeration below order nineteen is obsolete globally, and the
former critical-host equality layer is empty.  Enumeration is useful only
if it exposes a lemma that survives at unbounded order.  Neither random
tests nor finite host elimination may be promoted as a proof of (6).
Likewise, a smallest-counterexample assumption is a standard engine for a
positive universal proof; constructing counterexamples to intermediate
lemmas is only a falsification check.  A new barrier is a stop or pivot
signal, not the success criterion for this route.

The [external-review dossier](hc7_k7minus_external_review_dossier.md)
records the reviewed computation-free density spine preceding the new
two-clique theorem.  The earlier
[global-count review record](hc7_k7minus_external_review_packet.md) remains a
frozen record of the preceding five-exceptional-vertices route; its open
target has not been proved.
