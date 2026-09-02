# Independent internal audit: three-support bonds and the exact three-cut reduction

**Verdict: GREEN.**  At the exact revision identified below, the direct
three-support minor construction, the universal bond bound, the
four-connected bond theorem, the three-pair bond lemma, and the reduction
to two-component three-cuts are correct under their stated hypotheses.
This is a separate internal mathematical audit, not external peer review.

**Audited source:**
[`hc7_k44_three_support_bond_and_threecut_reduction.md`](hc7_k44_three_support_bond_and_threecut_reduction.md)

**Audited source SHA-256:**
`4007a05f71be45b16df65637806bffd241fd3da3cb9905b0764e73b818ecb9db`

**Audited finite verifier:**
[`hc7_k44_three_support_bond_completion_verify.py`](hc7_k44_three_support_bond_completion_verify.py)

**Verifier SHA-256:**
`9aa04512b78656c59e67a3e425f025cfeab6121f1babf00863175efc2d8ce200`

## 1. Accepted inputs

The audit accepts the following adjacent GREEN results at the displayed
source revisions.

| input | source SHA-256 |
|---|---|
| [`hc7_k44_tight_boundary_and_minimum_blocker.md`](hc7_k44_tight_boundary_and_minimum_blocker.md) | `384150b962a3e86848622e78cd711fac3d27b1bfcedbc22a1ce8adb2d7127b90` |
| [`hc7_k44_five_support_bond_reduction.md`](hc7_k44_five_support_bond_reduction.md) | `687034d01f4b1a9784585aa9596def4439939f17efc6ecd0d0530c2c95aa7773` |
| [`hc7_k44_spanning_two_helper_split_count.md`](hc7_k44_spanning_two_helper_split_count.md) | `9e139106b9f5c47d1c12b7b24436f1890b6f50aa31c293689b2cb1fb3945da54` |

The first result supplies the actual seven-vertex boundary, its seven
disjoint boundary-rooted bags with distinct literal-core representatives,
boundary fullness, support multiplicity, three-connectivity, minimum degree
four, the specified vertex `p`, and the exact three-cut profiles.  The
second supplies the six-boundary inequality, the minimum support-full-side
classification, the parity-bond theorem in the form used here, and the
off-face support lemma.  The third supplies the oriented two-helper
completion used in the first case of Corollary 2.2.

## 2. Direct three-support completion

The three types in (6) are exhaustive.  With `a` fixed on one shore and
`b` on the other, if `r,c,e` have the meanings in the proof, then
`r+c+e=3`.  Its six solutions pair under simultaneous interchange of
`a,b` and the two shores and reduce exactly to `T_1,T_2,T_3`.  In
`T_1,T_3`, the two unselected representatives have the same colour, so
the mixed assignment can be normalized by interchanging their names.  In
`T_2` they have opposite colours, and the table treats both mixed
assignments in its middle row.

Every union displayed in (7) is connected.  A union of two core-rooted
bags uses an edge of the literal `K_{4,4}` between opposite-shore
representatives; a union of a helper and a rooted bag uses one of the
assumed support edges.  The original rooted bags are mutually disjoint,
the unused core vertex belongs to none of them, and `A,Z` are disjoint from
the bags and the core.  Hence each row consists of seven pairwise disjoint
connected branch sets.

A direct contact check of all six rows gives exactly the conclusion stated
in the last column: the first five rows can miss only the displayed pair,
and the final row is complete.  Thus every row has at least twenty of the
twenty-one possible contacts and is a valid `K_7^-` minor model.  The proof
does not rely on an incorrect claim that the six retained boundary roots
alone form a `K_6^-`; the necessary contacts come from the explicit
five-root, two-helper branch-set mergers in (7).

The application to the minimum blocker is legitimate.  Each boundary-rooted
bag lies outside `X`, contains its boundary root, and has one distinct core
representative.  If a shore of a bond meets `R_d`, its edge to `d` makes it
adjacent to the `d`-rooted bag.  The two bond shores are disjoint from all
rooted bags and the literal core, and they are adjacent because they form a
partition of the connected graph `X` into two nonempty connected sets.

For Corollary 2.2, orient the bond so that `A` meets `R_a`.  When `Z` meets
`R_b`, the audited split-count theorem applies with three split
`K`-supports.  Otherwise `A` meets `R_b`; choose any three split supports
as `j_1,j_2,j_3`.  Each of the remaining two nonempty supports meets at
least one bond shore, so all hypotheses of Lemma 2.1 hold.  Consequently a
target-free minimum blocker satisfies `s(A,Z)<=2` for every bond, with no
orientation exception.

## 3. The four-connected and three-pair bond theorems

For Theorem 3.1, the bond `(Y-p,{p})` makes the family of admissible
support-full shores nonempty: four-connectivity makes `Y-p` connected, and
support order at least two makes it meet all five supports.  The audited
minimum-side theorem may be applied with both distinguished supports equal
to `{p}`.  A closing bond in that auxiliary instance would split at least
three supports, so the contrary assumption excludes one.  The bounds
`2<=|M|<=s<=2` leave only the triangle-free path outcome and give the
support placement in (11)--(12).

Every subpath of `U` is a bond shore because every component left in
`U-P` attaches to the connected set `V`.  Formula (13) then counts all
five supports exactly.  Applying it to an end-subpath at each path edge
shows that no two of the three internal support hulls use the same edge.
Their union is a nonempty forest, so the symmetric difference of their
endpoint pairs is its nonempty odd-degree set.  The Chen--Ding--Yu--Zang
parity-bond dichotomy therefore applies.

The second application of that dichotomy correctly excludes the facial
alternative.  The off-face support lemma supplies a replacement pair
containing a vertex outside the first facial cycle `C`, while the other two
endpoint pairs retain at least three distinct vertices of `C`: two
positive-length edge-disjoint subpaths can share at most one endpoint.
The replacement triple remains acyclic because the selected off-cycle
vertex occurs in exactly one pair.  Whitney uniqueness identifies the two
plane representations up to a spherical homeomorphism.  In a
three-connected plane graph, two distinct facial cycles intersect in the
empty set, one vertex, or one edge.  Hence a second facial cycle containing
at least three vertices of `C` must equal `C`, contradicting its selected
off-cycle vertex.  This verifies the revised facial-cycle sentence at the
audited hash.

Lemma 3.2 is correct.  Deleting one vertex of a three-connected graph leaves
a two-connected graph.  Set-Menger therefore gives, in each component
`W_i`, two disjoint paths from the selected pair to the two retained cut
vertices, saturating both endpoint sets.  After trimming, their interiors
cannot leave `W_i`, because the third cut vertex has been deleted.  The
three paths ending at each retained cut vertex form two disjoint connected
sets and place opposite members of every selected pair in opposite sets.  A
shortest path makes the two sets adjacent if necessary.  Every component of
the unused graph attaches to their connected union and may be assigned
wholly to a side it meets.  This produces a spanning bond without moving a
selected vertex and therefore preserves all three separations.

## 4. The exact three-cut reduction

In Theorem 4.1, the universal bound `s<=2` and the minimum-side theorem
again force the plain induced-path case, now without needing an incidence
orientation for `R_b`.  Formula (13), pairwise edge-disjoint positive
support hulls, `m>=4`, and `rho(u)<=2` follow as stated.  The singleton case
of the six-boundary inequality then gives (16), including the stated
endpoint and internal attachment bounds.

A bipolar order exists because `X` is three-connected.  Every proper
prefix and suffix is a bond shore, so `s<=2` is exactly the depth-two
condition for the five half-open support intervals.  Interval graphs are
chordal and intervals have the Helly property; depth two therefore makes
their intersection graph a forest.  Counting the supports missed by a
prefix or suffix in the six-boundary inequality gives (19).

If `X` were four-connected, Theorem 3.1 would contradict `s<=2`; hence its
known three-connectivity is exact and it has a three-cut.  For any such cut,
a component disjoint from `U-T` would meet at most the two endpoint
supports, contradicting `q>=6`.  The asserted lower bound on `|T cap U|`
in the three-component case then follows by deleting vertices from the
path `U`.

Both three-component profiles from the tight-boundary theorem are properly
eliminated.  In the exceptional profile, its distinguished component and
connected complement form a bond splitting the three
non-component-exclusive supports.  In the other profile, each of three
distinct supports has its whole vertex set in one distinct component.
Support multiplicity supplies two distinct vertices of each such support,
so Lemma 3.2 gives a bond splitting all three supports.  Either profile
contradicts the universal bound `s<=2`.  The prior three-component bound and
the definition of a cut then imply that every three-cut leaves exactly two
components.  The earlier argument that every component meets `U-T` remains
valid for each such cut.

## 5. Finite check, trust boundary, and remaining scope

The verifier compiles and runs successfully, with output

```text
PASS cases=160 minimum_optimum=20
PASS optimum_distribution=20:136,21:24
PASS certificate_sha256=a21f18a19ad4618c1cf4569f05cbd2b25201f924de140a5f78eb04aa9a3c4b17
NOTE bounded corroboration only; the unbounded lemma uses its written proof
```

It enumerates all forty proper `3`-by-`4` placements with `a,b` opposite
and all four minimal assignments of the two remaining supports.  Its
deletion-and-contraction recursion exhausts seven connected branch sets in
each ten-vertex quotient and independently validates every returned model.
This corroborates only the finite case table in Lemma 2.1.  It does not
establish the existence of the rooted bags, Corollary 2.2, Theorem 3.1,
Lemma 3.2, or Theorem 4.1; those are covered by the written proofs audited
above.  No unbounded conclusion is inferred from the enumeration.

The result eliminates four-connected nonsingleton minimum blockers and
every three-component three-cut.  Every three-cut in a surviving
nonsingleton blocker has exactly two components, each meeting the chosen
minimum support-full path; no complete support profile across those two
components is yet proved.  Eliminating this sole nonsingleton possibility is
precisely the open two-component three-cut completion lemma in Section 5.
The singleton-blocker branch remains separate.  Accordingly, this result
does not by itself prove the literal `K_{4,4}` case of T44, T44,
Conjecture 21, or `HC_7`.
