# Internal audit: multiple missing centre adjacencies

**Verdict:** GREEN for Theorem 1 and Corollary 2.  Two independent cold
checks found no branch-set, separator, or fixed-operation error.  The result
is nonterminal because its separator is not identified as an exceptional
anti-neighbourhood.

**Audited source:**
[`hc7_k7minus_multiple_missing_adjacencies_separator_dichotomy.md`](hc7_k7minus_multiple_missing_adjacencies_separator_dichotomy.md)

**SHA-256:**

```text
b9c02238a4142647005745b96b7d94377fb897c3d589081388dca0a6718edad2
```

This is a separate internal mathematical audit, not external peer review.
No finite computation is used.

## 1. Duplicate donor contact

Because the model spans `G`, a branch set missed by `X` is a far side of
`N_G(X)`.  Seven-connectivity therefore gives at least seven literal
neighbours of `X`.  At least two of the six branch sets are missed, so
those neighbours occupy at most four contacted branch sets.  One contacted
set contains two distinct neighbour vertices.  Distinct donor vertices,
not merely two edges with a common donor endpoint, are what the proof uses.

## 2. Avoidable retaining core

If a retaining core `T` through the first donor portal avoids the second,
the component `Y` of the donor minus `T` containing the second portal is
connected.  Its donor complement is connected because it contains `T` and
every other component of the deletion attaches to `T`.  That complement
retains all five donor--foreign adjacencies.

Absorbing `Y` into `X` therefore gives the seven displayed branch sets.
The cut edge gives the new centre--donor adjacency, the retained core gives
all donor--foreign adjacencies, and `Y` repairs all but at most one missing
centre adjacency.  This is an explicit `K_7^-` model.  Otherwise a missed
foreign branch set anticomplete to `Y` is a literal far side of `N_G(Y)`.

## 3. Unavoidable opposite cores

The two canonical opposite sets are connected, have connected donor
complements, and are disjoint.  Each has a nonempty monopoly set: an empty
one would make its connected complement a retaining core avoiding the
opposite marked vertex.

Choose a foreign portal set wholly contained in one opposite set.  Since
the other opposite set is disjoint, it has no edge to that foreign branch
set.  The latter is therefore a far side of the other set's open
neighbourhood.  This directly supplies the separator outcome; no monopoly
cardinality argument or multi-target linkage is needed.

## 4. Fixed-operation scope

Corollary 2 correctly assumes rather than infers survival of the labelled
model and two distinct donor portals in the edge-star deletion.  The proof
then uses only surviving edges.  Restoring an edge-star centred in `X` can
add the centre to the selected donor piece's neighbourhood, but cannot add
an edge from that piece to its foreign far side.  Thus the separator remains
actual in `G`, and the named colouring is unchanged.

The corollary must not be applied to an arbitrary deleted edge or directly
to a contraction quotient without checking model survival and pullback.

## 5. Exact limitation

The theorem returns neither a common boundary partition nor a boundary of
the form `N_G(z)` for a named exceptional degree-eight vertex.  The
separator can have order greater than seven, and the retained colouring
need not be proper on either new closed shore.  The result therefore does
not prove exceptional-centre connectivity, Conjecture 21, or `HC_7`.
