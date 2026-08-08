# Internal audit: false-twin triangle closure

**Verdict:** GREEN.

**Audited source:**
[`hc7_k7minus_false_twin_triangle_closure.md`](hc7_k7minus_false_twin_triangle_closure.md)

**Audited SHA-256:**
`55c70b8922f75bdbcbae96fadfa60bb72cccc232db386d3065d95e323a1417fd`

This is an internal mathematical audit, not external peer review.  The
proof is computation-free.

## 1. Rooted input and density

The invoked contrapositive of Norin--Totschnig, Lemma 12, has the exact
threshold `4|V(F)|-9`.  In Theorem 1, deleting the degree-six false twin
removes exactly six edges and gives

\[
 |E(F)|\ge4n-13=4|V(F)|-9.
\]

Six-connectivity of `G` makes `F=G-y` five-connected, which is stronger
than the rooted internal four-connectivity required by the cited theorem.
The four roots induce a literal `K_4`: the three boundary vertices form the
assumed triangle and the false twin is adjacent to all of them.

## 2. Maximal-helper normalisation

The optimisation is over finitely many branch-set models.  In each root
bag, the leaf exchange correctly reduces all helper contacts to one portal.
If the two helper contact sets have union of order at least two, they admit
distinct representatives; a minimal tree through the prescribed root and
the representatives has a non-root representative as a leaf.  Moving that
leaf preserves both altered bags' connectivity and both root--helper
adjacencies.  Otherwise the contact sets are the same singleton.

An unused component meeting a helper can be absorbed whole, so the helper
union has at most four external neighbours.  If any vertex lay outside the
helper union and those portals, deleting at most four vertices would leave
two nonempty open sides, contrary to five-connectivity.  Therefore all four
root bags are their single portal vertices.  No unstated spanning-model
assumption is used.

## 3. Final branch sets

The singleton root `x` has no neighbour outside the other three roots and
`S-\{a,b,c\}`.  Since each helper is adjacent to the `x`-bag, each helper
contains a member of that three-set.  The reinserted false twin `y` is
therefore adjacent to both helpers and to the three triangle roots.  The
six rooted-model bags are mutually adjacent, and `y` misses only `x`.
This is literally a seven-bag `K_7^-` model.

For Corollary 2, deleting a degree-seven false twin from a seven-connected
graph leaves a six-connected graph and density `4|V(F)|-5`, safely above
the same rooted threshold.  The proof otherwise applies verbatim.

## 4. Scope

The theorem excludes a triangle in the common boundary.  It does not
exclude a triangle-free boundary and, in particular, does not handle the
degree-seven returned-cut subcase in which the two boundary neighbours of
the selected vertex are nonadjacent.
