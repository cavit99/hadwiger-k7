# Density frontier for the `K_7^-` six-colour route

**Status:** live conditional refinement; not a proof of the `K_7^-`
six-colour conjecture or of `HC_7`.  The entrance reduction, equality
reduction, and seven-cut theorem are written proofs with separate internal
audits GREEN for their current revisions.  The displayed finishing targets
below remain conjectural.

This frontier supersedes the five-exceptional-vertices target as the main
laboratory for this side route.  It does not replace the primary all-degree
`HC_7` target in [`INDEX.md`](INDEX.md).

## 1. Proved entrance reduction

Let `G` be a hypothetical minor-minimal non-six-colourable graph with no
`K_7^-` minor.  The updated
[density and low-degree rigidity theorem](../results/hc7_k7minus_five_exceptional_vertices_reduction.md)
proves

\[
 |E(G)|\ge4|V(G)|-5,
 \qquad
 |V(G)|\ge19.                                           \tag{1}
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
 0\le\varepsilon\le |V(G)|-15,                         \tag{2}
\]

with `epsilon` even.  Equality in the density inequality in (1) forces
`n_7=10` and two disjoint literal `K_5`s covering those ten vertices.  The
equality refinement in Section 3 improves its order bound to twenty-nine.

The first possible order now has only two degree patterns:

\[
 7^6 8^{13},
 \qquad
 7^7 8^{11}9^1.                                        \tag{3}
\]

In the second pattern, the two literal `K_5`s meet in one degree-seven
vertex and one vertex of degree eight or nine; their six exclusive vertices
all have degree seven.  This is a structural test case, not a finite
reduction of the unbounded problem.

## 2. Exact sufficient extremal theorem

The following statement is sufficient for the `K_7^-` six-colour
conjecture:

> **Extremal target.** Every seven-connected `n`-vertex graph with at least
> `4n-5` edges contains a `K_7^-` minor.

Equivalently, every seven-connected `K_7^-`-minor-free graph should satisfy

\[
                              m\le4n-6.                 \tag{4}
\]

This target is not proved.  It is nevertheless the right global statement
to attack: it uses only seven-connectivity and density, while any
minor-minimal colouring counterexample automatically satisfies its
hypotheses.

Norin and Totschnig prove that a four-connected graph at the nearby
`4n-8` threshold contains the graph obtained from `K_7` by deleting two
edges with a common end, apart from their explicit small exception.  Thus a
graph in the range (1) already has this two-defect near-`K_7` minor; one
possible proof of the extremal target is to recover one of its two missing
adjacencies.  Their paper explicitly identifies a `K_7^-` strengthening as
the missing extremal input for the six-colour conjecture:
[Norin--Totschnig, Theorem 6 and Conjecture 21](https://arxiv.org/abs/2507.03244).

## 3. Tight-density rooted-minor target

Suppose equality holds in the density inequality in (1), and let

\[
                         L=\{v_1,\ldots,v_5\}
\]

be one of the two all-degree-seven literal `K_5`s.  The proved local
classification gives five pairwise disjoint triangles

\[
                         T_i=N(v_i)-V(L),               \tag{5}
\]

where `T_i` is anticomplete to `L-{v_i}`.

Two vertex-disjoint connected subgraphs of `G-L`, each meeting every
`T_i`, together with the five singleton vertices of `L`, form a
`K_7^-`-minor model.  The only permitted missing adjacency is between the
two connected subgraphs.  In rooted-minor language, this is an
`L`-rooted `K_{2,5}` model.

This gives the sharper finishing statement for the equality layer:

> **Two-transversal target.** Under the full critical-host hypotheses, the
> five private triangles in (5) admit two vertex-disjoint connected
> transversals in `G-L`.

The new
[equality connectivity and overlap theorem](../results/hc7_k7minus_equality_connectivity_reduction.md)
gives a substantially stronger reduction.  Put `H=G-L`.  Then

\[
 \kappa(H)\ge5,
 \qquad |E(H)|=4|V(H)|-10.                             \tag{6}
\]

Indeed, if a set `Z` of at most four vertices separated `H`,
seven-connectivity would force each component to meet at least
`7-|Z|` of the five triangles.  The surviving part of a triangle is a
clique and lies in only one component, making two components impossible.

Let `A,B` be the two degree-seven `K_5`s, put
`R=G-(A\cup B)`, and let `k=|E(A,B)|`.  The same theorem proves

\[
 \kappa(R)\ge3,
 \qquad |E(R)|=4|V(R)|-15+k,
 \qquad k\le3.                                         \tag{7}
\]

It also gives the sharp current order information

\[
 |V(R)|\ge19,
 \qquad
 |V(G)|\ge29.                                          \tag{8}
\]

These bounds are written deductions from nonseparating-vertex and degree
counts, not finite enumeration.

More generally, if `H-Z` is disconnected, then every component `C` of
`H-Z` satisfies

\[
 |N_H(C)|+
 |\{i:C\cap T_i\ne\varnothing\}|\ge7.                  \tag{9}
\]

The target is equivalently a bond of `H` meeting every triangle.  Fournier's
cyclability theorem and five-connectivity give a cycle of `H` through all
fifteen triangle vertices, but a terminal-spanning cycle alone is
insufficient: five triangles joined cyclically by one edge per consecutive
pair give an explicit two-connected obstruction.  The missing positive
argument must use the at-least-five attachments of the off-cycle bridges.

Critical colouring supplies a second exact constraint.  In every
six-colouring of `H`, either four triangles use one common three-colour set,
or at least two colours occur on all five triangles.  This is the complete
Hall obstruction to extending the colouring across `L`.  Edge-criticality
sharpens it: for every edge `v_ix` with `x\in T_i`, a six-colouring of the
edge-deleted graph forces three two-colour components rooted at `x`, each
meeting its prescribed triangle.  In the rigid four-triangle-palette branch,
each component meets all four specified triangles.  They share the same
four root-coloured triangle vertices, so the remaining task is to split or
reroute this common spine into two disjoint connected transversals.

Wollan's exact rooted-`K_{2,t}` theorem is the closest general input, but at
`t=5` its edge threshold is `5|V(H)|-14`, far above the present density and
it does not close this specialization.  See
[Wollan, Theorem 1.3](https://doi.org/10.1002/jgt.20301).

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

> **Fragment target.** In a smallest counterexample to (4), either a
> contraction preserving seven-connectivity reduces the order without
> reducing the density surplus, or an order-seven fragment satisfying (10)
> yields an explicit `K_7^-` model.

This target is open.  In particular, the seven-cut theorem does not itself
show that an arbitrary component contraction preserves seven-connectivity.

## 5. Research discipline for this route

The next useful work is one of:

1. prove the bond target from (6)--(9), by splitting or rerouting the shared
   four-triangle Kempe spine;
2. prove the fragment target by analyzing the small-connectivity boundary
   graphs in (10); or
3. upgrade a normalized Norin--Totschnig near-`K_7` model using the three
   edges of surplus over `4n-8`.

Further enumeration below order nineteen is obsolete globally, and below
order twenty-nine in the equality layer.  Enumeration is useful only if it
exposes a lemma that survives at unbounded order.  Neither random tests nor
finite host elimination may be promoted as a proof of (4).

The earlier
[external-review packet](hc7_k7minus_external_review_packet.md) remains a
frozen record of the preceding five-exceptional-vertices route.  Its open
target has not been proved; this frontier records the stronger current
reduction.
