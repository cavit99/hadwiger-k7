# Internal audit: pairwise-Kempe relative-connectivity barrier

**Verdict:** **GREEN** for Propositions 3.1 and 4.1 and for the exact
counterexample scope.  This is a separate internal mathematical audit,
not external peer review.

## 1. Exact revision checked

The audited barrier source
`hc7_b2_pairwise_kempe_relative_connectivity_barrier.md` has SHA-256

```text
521aafe954b1288f8673a30d3be9f8f50bfa27e9ae9cb358ec4b405e697adb8e
```

The nine-vertex core is imported from the separately audited
paired-colourful planar-core barrier at source SHA-256

```text
25d436688ed47f624fafc465249165ac889c43839e1c3a83d4930a90f1118630
```

whose GREEN audit has SHA-256

```text
43d1a0f23aeadbe31cff338070393524dbfb06adf7e67d5b8836fd63d0466c8f
```

## 2. Colouring and common components

The displayed colouring of the core has classes `012,34,56,78`.  The
four added vertices `9,10,11,12` receive the four ordinary colours and
are properly coloured against their respective neighbours `3,0,0,0`.
The new vertex `h` receives the fifth colour `r` and is adjacent to all
eight members of `S union T`.  Thus `S` and `T` each contain one vertex
of every ordinary colour, and for each ordinary colour the corresponding
two contacts lie with `h` in one `r`--ordinary-colour component.  All four
components therefore intersect at `h`.

Deleting `h` leaves the four-chromatic core with four pendant vertices,
so the remaining graph is exactly four-chromatic under the displayed
extension.  Every four-colouring restricts to a four-colouring of the core,
where `S` is colourful by the audited core theorem.

## 3. No four disjoint paired connected sets

A family of four disjoint connected sets meeting both order-four sets
would use every member of `S` and `T` exactly once.  A set containing `9`
but not `h` must contain `3`; a set containing one of `10,11,12` but not
`h` must contain `0`.  Disjointness permits at most one set of each type to
avoid `h`.  At least two of the four sets would therefore contain `h`, a
contradiction.  This already excludes the connected branch sets required
by a paired-rooted `K_4` model, without needing to test their mutual
adjacencies.

## 4. Relative boundary inequality

Every nonempty `X` meets all five universal boundary neighbourhoods, and
the two remaining boundary vertices occur exactly when `X` meets `S` or
`T`.  Hence the boundary identity (4.2) is exact.

The constructed graph `C` is two-connected: deleting `h` leaves the
connected core with four pendant vertices, while deleting any other vertex
leaves the four-connected core minus at most one vertex connected and `h`
provides an alternative attachment for every affected new vertex.
Consequently a proper `X` meeting both root sets has at least one internal
boundary vertex, and one meeting exactly one root set has at least two;
the missed four-set guarantees vertices beyond any proposed unique
neighbour.  Both cases give total boundary at least eight.

If `X` meets neither root set and contains `h`, all eight root vertices are
in `N_C(X)`.  If it avoids `h`, then it is a nonempty subset of
`V(R)-S`; four-connectivity of `R`, with all four vertices of `S` outside
`X`, gives at least four neighbours in `R`.  These cases give totals at
least thirteen and nine, respectively.  For `X=V(C)`, the internal
boundary is empty and all seven external boundary vertices occur, so the
total is exactly seven.

## 5. Scope

The construction is not a five-centre host and is not claimed to satisfy
seven-connectivity, minor-criticality, or the degree-eight incidence
profiles.  It refutes only the local implication from pairwise-touching
common-hole components plus the relative boundary inequality to a paired
rooted model or strict equality separation.  No unresolved gap remains in
that stated barrier claim.
