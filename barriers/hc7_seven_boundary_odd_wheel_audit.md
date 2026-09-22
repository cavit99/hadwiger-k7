# Audit: seven-boundary odd-wheel barrier

**Status:** separate internal audit; **GREEN** for the explicit structural
counterexample and its six-choice helper strengthening. This is not a
counterexample to `HC_7` or to the planar-cell colouring theorem.

- Audit date: 2026-09-22.
- [Source](hc7_seven_boundary_odd_wheel.md) SHA-256:
  `4f8dd41fe16b1eb13f6fb2dd4417de126f294fde2085f8c4b7d6c06b1af92716`.
- [Verifier](hc7_seven_boundary_odd_wheel_verify.py) SHA-256:
  `5d207898fb0ed54dd0edb4338faf152c9ce77148bc99502eadebbf43fbdce2d4`.

The original structural counterexample was reconstructed independently.
The added density paragraph and matching verifier assertions were then
written and checked during this audit at the parent's request; they were
not supplied by an independent third auditor.

## Direct reconstruction

The stated 12-vertex base has 30 edges. Its two pentagonal rings and
the edges `bi-ai,bi-a(i+1)` triangulate an annulus; the two cap fans
give a planar embedding. Each base neighbourhood is a five-cycle.
Adding the adjacent universal pair gives 14 vertices and 55 edges.
The finite check of all base cuts of order at most four, together with
the universal pair, proves seven-connectivity; a base vertex has degree
seven, giving the matching upper bound. The five-cycle neighbourhoods
give independence number two at base vertices. The displayed matching
of six edges covers the base and verifies the claimed bound at either
universal vertex.

The exact boundary of the wheel `X` is the universal pair and all five
`a` vertices. The labelled `T`, induced four-vertex path, five-clique
and their intersections agree with the source. The neighbour sets in
`X` of the two extreme path vertices are disjoint. The completed side
is the join of the universal pair with the wheel plus `a4`, where
`a4` is adjacent to the consecutive rim pair `b3,b4`. This latter
graph is two-connected. The displayed four-cut then proves that the
completed side has connectivity exactly four.

In any purported seven-bag complete model, at least five bags avoid
both universal vertices. Those bags are connected and pairwise adjacent
inside the planar base, giving an impossible `K5` minor. This proves
minor exclusion independently of the verifier. The displayed six colour
classes partition the vertices and are independent; the verifier checks
that witness explicitly.

## All six rooted sides

The wheel contributes ten internal edges. The two universal gates
contribute twelve cell edges, and `a4` contributes two more. Each path
contact contributes two cell edges. Thus all six choices of two contacts
give rooted four-density `10+14+4-4*6=4`.

Every nonempty subset of `X` has at least seven external neighbours
in the original graph: otherwise deleting at most six vertices separates
it from `p`, which is outside `X` and anticomplete to it. Forming the
five-rooted side removes only the two omitted contacts from this
neighbourhood. Its internal five-connectivity, hence 4-lightness, follows.
The updated verifier checks all 63 nonempty subsets for each of the six
root choices as well as the edge counts.

A full-contact H2 upgrade on any one of these sides could be glued
to the exterior rooted clique supplied by the audited seven-boundary
linkage construction. The root bags intersect across the two sides
only at their prescribed roots, while both helpers stay in `X`.
The resulting seven bags would contradict the direct minor exclusion.
This verifies the strengthened barrier without asserting that the
existing one-missing-contact H2 theorem fails.

## Verification and limits

The standard-library verifier was read and run through
`uv run python3 barriers/hc7_seven_boundary_odd_wheel_verify.py`.
All assertions passed, including the added density and internal
connectivity checks. Its finite enumeration covers this one labelled
graph; planarity and minor exclusion rest on the direct arguments above.

The graph is six-colourable and is not asserted to realise a minimum
reserved state of a seven-contraction-critical host. The barrier refutes
the stated unconditional minor conclusion and full-contact upgrade only.
Index checks are left to the parent's integration pass as requested.
