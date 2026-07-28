# Density frontier for the `K_7^-` six-colour route

**Status:** live conditional refinement; not a proof of the `K_7^-`
six-colour conjecture or of `HC_7`.  The entrance reduction and the
seven-cut theorem are written proofs with separate internal audits GREEN
for their current revisions.  The displayed finishing targets below remain
conjectural.

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
`n_7=10`, two disjoint
literal `K_5`s covering those ten vertices, and order at least twenty-one.

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

There is a useful proved reduction.  Put `H=G-L`.  Seven-connectivity gives
that `H` is two-connected.  If `{x,y}` were a two-vertex cut of `H`, then
every component of `H-{x,y}` would meet all five triangles: a missed
triangle would make its neighbourhood in `G` have order at most six.  Any
two components would therefore be the two required connected transversals.
Consequently a counterexample to the two-transversal target must have `H`
three-connected.

More generally, if `H-Z` is disconnected, then every component `C` of
`H-Z` satisfies

\[
 |N_H(C)|+
 |\{i:C\cap T_i\ne\varnothing\}|\ge7.                  \tag{6}
\]

The unresolved task is to turn (6), three-connectivity, and the critical
colouring responses into two disjoint connected transversals.

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
 \kappa(G[S])\le6-r.                                   \tag{7}
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
> reducing the density surplus, or an order-seven fragment satisfying (7)
> yields an explicit `K_7^-` model.

This target is open.  In particular, the seven-cut theorem does not itself
show that an arbitrary component contraction preserves seven-connectivity.

## 5. Research discipline for this route

The next useful work is one of:

1. prove the two-transversal target from (6);
2. prove the fragment target by analyzing the small-connectivity boundary
   graphs in (7); or
3. upgrade a normalized Norin--Totschnig near-`K_7` model using the three
   edges of surplus over `4n-8`.

Further enumeration below order nineteen is obsolete.  Enumeration at
order nineteen is useful only if it exposes a lemma that survives at
unbounded order.  Neither random tests nor finite host elimination may be
promoted as a proof of (4).

The earlier
[external-review packet](hc7_k7minus_external_review_packet.md) remains a
frozen record of the preceding five-exceptional-vertices route.  Its open
target has not been proved; this frontier records the stronger current
reduction.
