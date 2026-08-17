# Second independent cold audit: returned type-VII elimination

**Verdict:** GREEN.  This is an internal mathematical audit, not external
peer review.

The audited revisions are

```text
results/hc7_k7minus_returned_type_vii_elimination.md
SHA-256 253f7020aa42ed8de4fe28fb6c1134e0954b76f81963cda606446b31e1ee65d8

results/hc7_k7minus_returned_type_vii_elimination_verify.py
SHA-256 6bf239425a4acee9070de98303d602c28698ff8b61b96e2eaeec8161552fe93e
```

No source edit is required, and there is no unresolved assumption within the
stated scope.

The promoted theorem differs only in its status paragraph and verifier
command path.  Its SHA-256 is
`c7be590f7006ab65289eb020141edd6a30bb73d8aff17df51ffcbfb7f0e9caa1`,
and its mathematical statement and proof are unchanged.

## 1. The strengthened four-root bound

The proof of Lemma 2 was checked directly against Norin--Totschnig,
Theorem 8 and the proof of Lemma 9.  The rooted-model outcome is excluded
by hypothesis and a separation outcome contradicts internal
four-connectivity.  In the trisection outcome, the two noncentral parts are
single roots.  A central part of order at most four would give a graph of
order at most six; in the remaining branch the calculation in Lemma 9 is
exactly

```text
|E(H)| <= 3|V(H)|-9.
```

In the planar outcome, internal four-connectivity makes `H` connected.
Four distinct roots on an outer facial walk of length at most five force at
least three distinct root--root edges.  This remains true when the facial
walk repeats a vertex or a bridge: with five positions, either one position
is unmarked and the four roots form a block with three distinct intervening
edges, or every position is a root and visiting four distinct roots uses at
least three distinct edges.  Hence at most two root edges force outer length
at least six.  Euler's formula then gives

```text
|E(H)| <= 3|V(H)|-3-lambda <= 3|V(H)|-9.
```

Thus the strengthened bound is valid without assuming that the outer facial
walk is a cycle.

## 2. Application to a full component

For each of the root sets `S-{0,5}` and `S-{3,4}`, a rooted separation of
order at most three lifts, after restoring the omitted pair, to a cut of
`G` of order at most five.  A rooted `K_4` model combines with the other two
full components and the appropriate cubic singleton (`0` or `4`) to form a
`K_7^-` model.  The singleton sees three literal roots and may miss only the
fourth.

Each root graph has exactly two edges.  Lemma 2 consequently gives

```text
e+P-a_0-a_5 <= 3c+1,
e+P-a_3-a_4 <= 3c+1.
```

Adding these inequalities and subtracting the degree sum over the component
gives `a_1+a_2<=2`.  Fullness makes both terms one whenever the component
has order at least three; simplicity gives the same conclusion for a
singleton.  The proof does not apply Lemma 2 at order two, so an order-two
edge is correctly retained as the sole possible source of a doubled
attachment at `1` or `2`.

Vertices `1` and `2` each have boundary degree two.  Minimum degree six and
three full components force a doubled attachment for each.  The relevant
components are therefore order-two edges.  Every end of such an edge has
its mate as its only internal neighbour, so it has at least five boundary
neighbours.  If one edge is doubled at both roots, the first finite class is
obtained; otherwise two distinct edges give the second class.  Contracting
the remaining full components creates exactly the stated quotient and every
quotient model lifts.

## 3. Completeness of the finite result

For one retained edge, each boundary vertex has the three exhaustive
incidence choices `first only`, `second only`, or `both`.  The endpoint
degree constraints give `21` patterns doubled at both `1,2`.  They give
`10` patterns doubled only at `1` and `10` doubled only at `2`, hence `100`
ordered split pairs.  No quotient is lost to a symmetry reduction.

The frozen verifier was rerun and returned all `121` target certificates
with digest

```text
88bef0aaee0914ff2b71cc4e00d7b55e8d4a42c274294d8418d37da646805fe6.
```

As an independent oracle, the graph-state checker

```text
results/hc7_k7minus_returned_type_vii_elimination_audit_verify.py
SHA-256 7b78c174433b079ff2a8c25202365f246f1b7b11f74fbd25184a3f8894cc6451
```

reconstructs all quotients and explores graph deletion and contraction
states rather than reusing the stored branch-set certificates.  It returned

```text
GREEN independent type-VII graph-state audit
quotients_checked=121
search_states=3129
```

A third exact branch-set search using the separately retained degree-eight
minor engine also accepted all `21+100` quotients.

## 4. Scope

The theorem is unbounded in the component orders and uses no density
hypothesis.  It eliminates exactly the type-VII seven-edge boundary for a
six-connected target-free graph with three full components.  It does not
address boundaries with at most six edges or the returned two-component
case.
