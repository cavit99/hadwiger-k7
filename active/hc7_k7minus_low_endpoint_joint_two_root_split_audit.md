# Author-side audit: low-endpoint joint two-root split

**Verdict:** **GREEN** for the theorem at SHA-256

```text
f0e129b30bb9f1c0d8cf8257b39bb70cbc573d15e7231de90c52de62aa33ad79.
```

This is an adversarial self-audit, not an independent or external review.

## Chromatic and density entrance

The critical-host minimum degree makes the second endpoint have degree
eight or nine.  Since deleting two vertices lowers chromatic number by at
most two and gives a proper subgraph, `5<=chi(H)<=6` is exact.

The exclusion of a five-colouring is valid.  For a fixed colour with no
common pole neighbour, the colour-class neighbours of `v` can all be
recoloured with a new sixth colour: they are independent, and none is
adjacent to `x`.  Assigning the old colour to `v` and the new colour to `x`
restores a proper colouring of the edge `vx`.  Thus every one of five
colours would require a distinct common neighbour, contradicting codegree
three.  No global double-critical assumption is used.

The edge count after deleting the adjacent pair is

```text
|E(H)|=|E(G)|-8-d_G(x)+1>=4|V(H)|-8.
```

Seven-connectivity leaves five-connectivity.  The audited count
`n_8>=26+tau` gives `|V(H)|>=24`, excluding the eight-vertex exception in
Norin--Totschnig Theorem 6.  A `K_7^vee` model therefore exists, and
absorbing its deficient branch set into any universal branch set really
does give a `K_6` model.  Connectedness justifies spanning enlargement.

The six-chromatic two-vertex deletion and the standing critical hypotheses
match the frozen palette-permutation theorem exactly.  In particular, the
source is entitled to use one edge-deletion colouring which supplies all
five non-pole colours at each end.

## Joint contact bound

For any spanning `K_6` model, `{v,x}` is a connected set disjoint from all
six branch sets.  If its union of contacts had order six, it and the model
would give `K_7`; if it had order five, they would give `K_7^-`.  Hence the
new target-sensitive bound is exactly

```text
|C_v union C_x|<=4.
```

This is stronger than the ordinary `K_7`-minor contact bound and is used
at the correct point in the proof.

## Existence of a splittable common branch set

The three common-neighbour vertices belong to the spanning branch-set
partition.  If two share a branch set, assigning one to each pole gives
the required distinct roots even though each vertex is itself adjacent to
both poles.

Otherwise they occupy three distinct common-contact branch sets.  Assume
adversarially that no common branch set has distinct pole neighbours.  In
any such branch set, choosing arbitrary neighbours of the two poles shows
that both nonempty neighbourhoods must be the same singleton.  Therefore
the three displayed branch sets are the only common ones and their portals
are exactly the three common-neighbour vertices.

Those three vertices use at most three colours; no distinctness of their
colours is assumed.  Choose one of the five saturated colours absent from
them.  Its selected neighbours at the two poles cannot coincide and cannot
lie in one branch set, since either event would create a further common
portal or a common branch set with distinct pole neighbours.  Their branch
sets are consequently distinct and exclusive.  The joint contact union
then has order at least `3+2=5`, contradicting the target-sensitive bound.
This proves the splittable branch set for every spanning model.

## Rooted split and separator

Deleting an edge of a spanning tree on the path between the two selected
roots partitions the branch set into two nonempty connected adjacent
parts.  After adjoining the appropriate pole, the two new bags are
connected, disjoint and adjacent through `vx`.  The other five branch sets
remain pairwise adjacent.  Thus the only possibly absent pairs among the
seven bags are their ten pole-piece--foreign-set contacts.

Target exclusion forces at least two such pairs to be absent; one absent
pair would still be a `K_7^-` model.  Any absent pair says that the
corresponding unaugmented piece is anticomplete to a nonempty foreign
branch set.  Its complete external neighbourhood is therefore an actual
separator, not merely a model-relative portal set.

Seven-connectivity gives the lower bound seven.  At equality, the proof of
fullness is sound because deletion of that exact boundary has at least two
components: the connected split piece and a component containing the
missed foreign branch set.  A component missing one boundary vertex would
have a separating neighbourhood of order at most six.

## Exact scope

No upper bound on the returned separator has been proved.  The theorem
therefore advances every low-endpoint model into an actual separation but
does not call a separator of order greater than seven terminal.  The
four-connected static quotient and the high-codegree two-apex icosahedral
example fail the theorem's hypotheses and are described only as scope
checks.

The pinned mathematical dependencies were checked at the hashes displayed
in the source.  No proof defect was found.  A separate cold audit is still
required before promotion.
