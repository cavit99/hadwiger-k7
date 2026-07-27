# Internal audit: three literal `K_5` subgraphs under `K_7^-` exclusion

**Verdict:** GREEN.

**Audited theorem SHA-256:**
`5b5e399122b996186e861f5075e7808c8e6fe4353082256ee12d5074499d2574`.

This is a separate internal mathematical audit, not external peer review.

## Overlap-four branch

Two distinct five-cliques meeting in four vertices have a six-vertex union
containing every edge except possibly the edge between their two unique
vertices.  Seven-connectivity makes the complement of this six-set
nonempty and connected.  Minimum degree at least seven ensures that every
vertex of the six-set contacts that complement.  Contracting it therefore
gives a seven-bag `K_7^-` model.

The proof correctly does **not** claim a `K_7` in this branch.

## Published theorem branch

If no pair meets in four vertices, any three distinct literal `K_5`
subgraphs have pairwise intersections of order at most three.  Theorem 1.10
of Niu and Zhang, *Cliques, minors and apex graphs*, specializes at `k=5`
to exactly:

- a seven-connected graph;
- not two-apex; and
- three literal `K_5` subgraphs with pairwise intersections at most three.

Its conclusion is a `K_7` minor.  This same specialization was previously
checked in the audited global literal-`K_5` transversal theorem, at source
SHA-256
`96c5cd399141ecc593d3f1b8a91717433f711c677f481135ee178e6745aa2996`.

The two branches are exhaustive and both contradict `K_7^-` exclusion.

## Trust boundary

This theorem is unexpectedly short relative to earlier clique-family
arguments and should receive conventional specialist review before any
publication claim.  The internal audit found no graph-order, disjointness,
apex-definition or hypothesis mismatch.  It concerns literal `K_5`
subgraphs, not arbitrary `K_5` minor models.
