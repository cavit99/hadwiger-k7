# Density frontier for the `K_7^-` six-colour route

**Status:** live conditional refinement; not a proof of the `K_7^-`
six-colour conjecture or of `HC_7`.  The entrance reduction, equality
reduction, equality exclusion, and seven-cut theorem are written proofs with
separate internal audits GREEN for their current revisions.  The displayed
finishing targets below remain conjectural.

This frontier supersedes the five-exceptional-vertices target as the main
laboratory for this side route.  It does not replace the primary all-degree
`HC_7` target in [`INDEX.md`](INDEX.md).

## 1. Proved entrance reduction

Let `G` be a hypothetical minor-minimal non-six-colourable graph with no
`K_7^-` minor.  The updated
[density and low-degree rigidity theorem](../results/hc7_k7minus_five_exceptional_vertices_reduction.md)
first proves

\[
 |E(G)|\ge4|V(G)|-5,
 \qquad
 |V(G)|\ge19.                                           \tag{1}
\]

The
[Kempe-component equality-exclusion theorem](../results/hc7_k7minus_equality_kempe_exclusion.md)
rules out the case `|E(G)|=4|V(G)|-5`.  Hence the current proved entrance is

\[
 |E(G)|\ge4|V(G)|-4,
 \qquad
 |V(G)|\ge19.                                           \tag{2}
\]

If `n_i` counts the degree-`i` vertices and

\[
 s=\sum_{i\ge9}(i-8)n_i,
 \qquad
 \varepsilon=10-n_7+s,
\]

then

\[
 2|E(G)|=(8|V(G)|-10)+\varepsilon,
 \qquad
 2\le\varepsilon\le |V(G)|-15,                         \tag{3}
\]

with `epsilon` even.  The former value `epsilon=0` forced `n_7=10` and two
disjoint literal `K_5`s covering those ten vertices.  Section 3 records why
that entire critical-host equality layer is now impossible.

The first possible order now has only two degree patterns:

\[
 7^6 8^{13},
 \qquad
 7^7 8^{11}9^1.                                        \tag{4}
\]

In the second pattern, the two literal `K_5`s meet in one degree-seven
vertex and one vertex of degree eight or nine; their six exclusive vertices
all have degree seven.  This is a structural test case, not a finite
reduction of the unbounded problem.

The entrance proof is computation-free.  For every nonedge in a
degree-seven neighbourhood, a star contraction, one fixed six-colouring,
Kempe-chain connectivity, and Kriesell--Mohr Theorem 7 give a rooted `K_5`
on the other five neighbours.  This forces the neighbourhood complement to
be `K_{3,4}` or `K_{3,3} dotcup K_1`.  The former anti-neighbourhood
129-graph residual and aligned near-`K_7` theorem remain valid elsewhere in
the repository but are not dependencies of this density or equality chain.

## 2. Current density-only sufficient extremal target

The following statement is sufficient for the `K_7^-` six-colour
conjecture:

> **Extremal target.** Every seven-connected `n`-vertex graph with at least
> `4n-4` edges contains a `K_7^-` minor.

Equivalently, every seven-connected `K_7^-`-minor-free graph should satisfy

\[
                              m\le4n-5.                 \tag{5}
\]

This target is not proved.  It is nevertheless the right global statement
to attack: it uses only seven-connectivity and density, while any
minor-minimal colouring counterexample automatically satisfies its
hypotheses.

Norin and Totschnig prove that a four-connected graph at the nearby
`4n-8` threshold contains the graph obtained from `K_7` by deleting two
edges with a common end, apart from their explicit small exception.  Thus a
graph at the target threshold has four edges of surplus over that benchmark;
one possible proof is to use this surplus to recover one of the two missing
adjacencies.  Their paper explicitly identifies a `K_7^-` strengthening as
the missing extremal input for the six-colour conjecture:
[Norin--Totschnig, Theorem 6 and Conjecture 21](https://arxiv.org/abs/2507.03244).

The former `4n-5` target is a stronger open statement: it would force the
minor one edge earlier.  It is no longer the current sufficient obligation,
because the critical equality layer at that density has been excluded.

## 3. Excluded critical-host equality layer: Kempe-component allocation

Suppose equality held in the original density inequality (1), and let

\[
                         L=\{v_1,\ldots,v_5\}
\]

be one of the two all-degree-seven literal `K_5`s.  The proved local
classification gives five pairwise disjoint private triangles

\[
                         T_i=N(v_i)-V(L),               \tag{6}
\]

where `T_i` is anticomplete to `L-{v_i}`.  The
[equality connectivity and overlap theorem](../results/hc7_k7minus_equality_connectivity_reduction.md)
supplies the exact host for the Kempe argument.  Put `H=G-L`.  Then

\[
 \kappa(H)\ge5,
 \qquad |E(H)|=4|V(H)|-10.                             \tag{7}
\]

Let `A,B` be the two degree-seven `K_5`s, put
`R=G-(A\cup B)`, and let `k=|E(A,B)|`.  The same theorem proves

\[
 \kappa(R)\ge3,
 \qquad |E(R)|=4|V(R)|-15+k,
 \qquad k\le3,                                         \tag{8}
\]

and, before the final exclusion, gives

\[
 |V(R)|\ge19,
 \qquad
 |V(G)|\ge29.                                          \tag{9}
\]

It also proves an exact Hall and edge-critical Kempe fork.  In every
six-colouring of `H`, either four triangles use one common three-colour set,
or at least two colours occur on all five triangles.  For every edge
`v_ix`, with `x\in T_i`, a six-colouring of the edge-deleted graph forces
three two-colour components rooted at `x`; in the rigid branch, each meets
the same four specified triangles.

The new
[Kempe-component allocation theorem](../results/hc7_k7minus_equality_kempe_exclusion.md)
applies the argument symmetrically to the colour absent from `L`.  In the
rigid branch, a `p`-component and a disjoint `q`-component meet the same four
triangles, and one can absorb a path from the fifth.  In the all-five-colour
branch, a three-colour count selects two `p`-components whose connected
union meets all five triangles and a disjoint `q`-component meeting at least
four.  In either case these two connected sets and the five singleton
vertices of `L` form an explicit `K_7^-`-minor model, with at most the one
permitted owner adjacency missing.  This contradiction excludes equality
and proves (2).

The proof does **not** establish the stronger standalone two-transversal
statement, nor the equivalent assertion that `H` has a bond meeting all five
private triangles.  One of the two connected sets may miss the fifth
triangle.  The critical equality host is nevertheless eliminated because a
`K_7^-` model permits exactly that one missing branch-set adjacency.  The old
two-transversal target is therefore retired as a live obligation, not
promoted as a proved theorem.

## 4. Exact seven-cut obstruction

The proved
[seven-cut component-contraction theorem](../results/hc7_k7minus_seven_cut_contraction.md)
gives a second route into the extremal target.  If `S` is an order-seven cut
and `G-S` has `r` components, then

\[
 2\le r\le5,
 \qquad
 N(C)=S\text{ for every component `C`},
 \qquad
 \kappa(G[S])\le6-r.                                  \tag{10}
\]

For `r=2`, the boundary is `K_5`-minor-free; for `r=3`, it has at most nine
edges; for `r=4`, it is a matching plus isolated vertices; and for `r=5`,
it is edgeless.
The theorem isolates the exact failure of naive contraction: contracting
all components gives `I_r\vee G[S]`, and that minor would contain `K_7^-`
whenever it remained seven-connected.

The next structural step is therefore a genuine fragment theorem, not a
density recount:

> **Fragment target.** In a smallest counterexample to (5), either a
> contraction preserving seven-connectivity reduces the order without
> reducing the density surplus, or an order-seven fragment satisfying (10)
> yields an explicit `K_7^-` model.

This target is open.  In particular, the seven-cut theorem does not itself
show that an arbitrary component contraction preserves seven-connectivity.

## 5. Research discipline for this route

The next useful work is one of:

1. analyze the new tight critical-host layer `epsilon=2`, where
   `n_7=8+s`, for structure that survives at unbounded order;
2. prove the fragment target by analyzing the small-connectivity boundary
   graphs in (10); or
3. upgrade a normalized Norin--Totschnig near-`K_7` model using the four
   edges of surplus over `4n-8`.

Further enumeration below order nineteen is obsolete globally, and the
former critical-host equality layer is empty.  Enumeration is useful only
if it exposes a lemma that survives at unbounded order.  Neither random
tests nor finite host elimination may be promoted as a proof of (5).

The [current external-review dossier](hc7_k7minus_external_review_dossier.md)
packages this computation-free density/equality spine for specialist
checking.  The earlier
[global-count packet](hc7_k7minus_external_review_packet.md) remains a
frozen record of the preceding five-exceptional-vertices route; its open
target has not been proved.
