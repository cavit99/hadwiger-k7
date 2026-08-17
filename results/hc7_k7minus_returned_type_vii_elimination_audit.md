# Cold audit of the returned type-VII elimination

**Verdict:** GREEN.

This audit checks the fixed revisions

```text
results/hc7_k7minus_returned_type_vii_elimination.md
SHA-256 253f7020aa42ed8de4fe28fb6c1134e0954b76f81963cda606446b31e1ee65d8

results/hc7_k7minus_returned_type_vii_elimination_verify.py
SHA-256 6bf239425a4acee9070de98303d602c28698ff8b61b96e2eaeec8161552fe93e
```

The rooted bound, its two applications, the order-two reduction, the exact
quotient lifting and all 121 finite cases are correct at these hashes.  No
source edit was made.

After promotion, only the status paragraph and verifier command path were
updated.  The promoted theorem has SHA-256
`c7be590f7006ab65289eb020141edd6a30bb73d8aff17df51ffcbfb7f0e9caa1`;
its mathematical statement and proof are unchanged.

## 1. Imported rooted result

The exact external dependency is Norin--Totschnig, *Every graph with no
`K_7^\vee`-minor is 6-colorable*, arXiv:2507.03244v1, Theorem 8 and the
proof of Lemma 9.  The cited proof was checked against the primary source.

Lemma 2 is a valid sharpening in the stated order range.  The rooted-model
and rooted-separation outcomes of Theorem 8 are excluded by the hypotheses.
In the trisection outcome, the proof of Lemma 9 reduces the two noncentral
parts to one root each.  A central part of order at most four would give a
graph of order at most six; otherwise the inductive calculation is exactly
the bound `3|V(H)|-9` used here.

In the planar outcome, internal four-connectivity first ensures that `H` is
connected.  Four distinct roots on an outer facial walk of length at most
five force at least three distinct consecutive root pairs, and hence at
least three root edges.  Thus at most two root edges force outer length at
least six.  Standard face counting then gives

```text
|E(H)| <= 3|V(H)|-3-lambda <= 3|V(H)|-9.
```

This argument does not assume that the outer facial walk is a cycle.  If a
vertex or edge is repeated on the walk, four distinct marked roots still
force three distinct root--root edges in the prohibited short case.

## 2. Component inequalities

For `Z=S-{0,5}`, a rooted separation of order at most three lifts after
adding `0,5` to a cut of `G` of order at most five.  A rooted `K_4` model
would combine with

```text
D union {5}, E, {0}
```

to form seven branch sets with only the contact from `0` to the root at `4`
possibly absent.  The analogous construction for `Z=S-{3,4}` uses the cubic
vertex `4`.  Both exclusions are exact.

Including the two literal root edges in each four-root graph, Lemma 2 gives

```text
e+P-a_0-a_5 <= 3c+1,
e+P-a_3-a_4 <= 3c+1.
```

Adding these and comparing with the degree sum over `C` gives

```text
a_1+a_2 <= 2.
```

Fullness gives `a_1,a_2>=1`, so both equal one for every component of order
at least three.  The same conclusion for a singleton follows from
simplicity.  The proof deliberately does not apply Lemma 2 at order two;
instead it correctly identifies order two as the only possible source of a
doubled attachment at `1` or `2`.

## 3. Forced order-two components and quotient lift

Vertices `1` and `2` each have two neighbours inside the displayed boundary.
Minimum degree six therefore supplies at least four incident component
edges at each.  Three full components supply only three baseline incidences,
so each root is doubled in some component.  By the preceding conclusion,
each such component has order two and, being connected, is an edge.

Every end of a retained order-two component has only its mate inside the
component.  Minimum degree six therefore makes it adjacent to at least five
boundary vertices.  Contracting any other full component to one vertex
produces exactly the quotient used in Lemma 3: the contracted vertex is
adjacent to all six boundary vertices, while distinct components create no
additional intercomponent edge.  Any branch-set model in the quotient lifts
through those component contractions.

If one edge is doubled at both roots, the first finite class applies.  If
not, the two doubled roots occur in distinct edges, and neither edge is
doubled at the other root; this is exactly the second finite class.  Thus
the same/split alternatives are exhaustive.

## 4. Finite verification

For one retained edge, fullness gives three labelled incidence choices at
each boundary vertex.  Requiring each end to miss at most one boundary
vertex gives 21 profiles when both `1` and `2` are doubled.  When exactly
one of them is doubled and the other is not, there are five profiles for
each orientation of the nondoubled incidence, hence ten.  The split case
therefore has `10 x 10=100` ordered profile pairs.  These counts include all
endpoint labellings; no symmetry reduction is assumed.

The source verifier was rerun and reproduced all 121 validated branch-set
certificates and digest

```text
88bef0aaee0914ff2b71cc4e00d7b55e8d4a42c274294d8418d37da646805fe6.
```

Its oracle is exact: deleting unused vertices and contracting a spanning
tree in each connected branch set reaches every seven-bag minor model, and
at seven bags at least 20 contacts are precisely a `K_7^-` subgraph or a
`K_7` subgraph.

As a cold cross-check, the adjacent audit verifier reconstructs the cases
and searches graph states directly by every edge contraction and vertex
deletion, rather than carrying branch-set masks.  It independently reports

```text
GREEN independent type-VII graph-state audit
quotients_checked=121
search_states=3129
```

## 5. Scope and residual assumptions

There is no unresolved proof assumption.  The theorem uses simplicity,
six-connectivity, exactly three components, fullness of each component and
the exact seven-edge boundary.  It does not use a density hypothesis.  It
does not address returned boundaries with at most six edges or the returned
two-component case.
