# Internal audit: two literal `K_5` subgraphs force `K_7^-`

**Verdict:** GREEN.

**Audited theorem SHA-256:**
`421544721b5084fe5dff280cd2299f0e4cb214ba39bc2b2fde5648fc393bcd83`.

This is a separate internal mathematical audit, not external peer review.
No computation is used.

## Linked-clique lemma

Set-Menger supplies `r` disjoint paths between the two disjoint `K_r`
subgraphs; their distinct ends exhaust both cliques.  The usable-cross-path
split covers every endpoint case.  A rail vertex can lie in an `A`-prefix
unless it is the `B`-end and can lie in a `B`-suffix unless it is the
`A`-end.  Thus opposite placements fail exactly when the two cross-path
ends are both `A`-ends or both `B`-ends.

After splitting two rails, the four pieces have both same-side clique
adjacencies, both original-rail adjacencies, and one cross-adjacency from
the added path.  Only the other cross-pair may be nonadjacent.  Every
unsplit rail is adjacent to all four pieces through its two clique ends.
The displayed branch sets are connected and pairwise disjoint.

If there is no usable cross-path, a component outside the rails that meets
two rails can attach only to one endpoint clique and therefore has at most
`r` neighbours, contradicting `(r+1)`-connectivity.  Every outside
component consequently belongs to one rail.  The interior of that rail
together with all its outside components has boundary contained in its two
ends; it must be empty.  The remaining graph would be two `K_r` subgraphs
joined by a perfect matching, whose minimum degree is `r`, again contrary
to `(r+1)`-connectivity.  The complements used in both separator arguments
are nonempty because `r>=2`.

## Intersecting five-cliques

For intersection order `s<=3`, deleting the intersection from a
six-connected graph preserves connectivity at least `6-s`.  The exclusive
parts are disjoint `K_{5-s}` subgraphs and `6-s=(5-s)+1`, so the lemma
applies.  Every constructed branch set retains an exclusive clique
endpoint.  Each deleted
intersection vertex is therefore universal to the model, and the
intersection vertices are pairwise adjacent.  Adding them gives exactly
seven branch sets with at most one missing adjacency.

For intersection order four, the union contains `K_6^-`.  A six-connected
graph has a vertex outside that union.  Any component of the complement
has all six union vertices in its neighbourhood; otherwise its
neighbourhood is a cut of order at most five.  Contracting that component
supplies the seventh branch set.  The cases are exhaustive.

## Critical-host arithmetic

At most one literal `K_5`, together with the audited degree-seven incidence
and all-degree-seven-clique exclusion, gives `n_7<=4`.  Degree summation
then gives `2m>=8n-4`.  All degree-seven and nonexceptional degree-eight
vertices lie in the one possible clique, so
`n_7+(n_8-b)<=5`.  Combining this with

\[
                         25\le2n_7+n_8-\tau
\]

gives `b>=20-n_7+tau>=16+tau`.  The directions and integrality are correct.

## The `n_7=4` amplification

Uniqueness excludes the two-clique degree-seven neighbourhood type.  The
four degree-seven owners therefore have pairwise disjoint private external
triangles, each anticomplete to the other four vertices of the unique
`K_5`.  The component-incidence count after deleting that clique proves
four-connectivity: each owner can meet at most one component, while the
fifth clique vertex can meet all of them, giving
`q(7-|S|)<=4+q`, impossible for `q>=2` and `|S|<=3`.

Contracting the clique loses exactly four vertices and ten edges and
creates no parallel-edge loss.  A separator of order at most four in the
contracted graph either lifts to `G` or, if it contains the contracted
vertex, reduces to deleting at most three vertices from the four-connected
complement.  The contracted graph is therefore five-connected.  Its order
is at least thirteen, excluding both base cockades, and five-connectivity
excludes a nontrivial clique-sum over four vertices.  Jakobsen's strict
alternative and integrality give `2m<=9n-41`.  The deductions

\[
 n\ge37,\qquad n_8\ge33+\tau,\qquad b\ge32+\tau
\]

then follow exactly as stated.

Splitting on `n_7<=3` or `n_7=4` is exhaustive.  In the first case the
baseline defect inequality gives `b>=17+tau`, and parity sharpens
`2m>=8n-3` to `m>=4n-1`.  The second case has the stronger bounds just
audited.  Thus the global conclusion `b>=17+tau` is valid.

If `n_7>0`, degree-seven clique incidence supplies a literal `K_5`.
The audited degree-eight exterior theorem leaves at most two components in
an exceptional anti-neighbourhood, while the audited two-component theorem
would exclude every literal `K_5`.  These statements are incompatible, so
the claimed connectivity follows.  This argument does not address the
`n_7=0` branch.

## Scope

The unconditional theorem concerns literal `K_5` subgraphs, not arbitrary
`K_5` minor models.  The numerical corollaries require the full critical
host hypotheses and their cited audited inputs.  The result supplies no
upper bound on exceptional vertices and proves neither the `K_7^-`
six-colour conjecture nor `HC_7`.  Conventional specialist review remains
appropriate before publication.
