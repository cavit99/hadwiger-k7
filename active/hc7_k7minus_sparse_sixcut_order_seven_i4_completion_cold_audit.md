# Cold audit: terminal order-seven `i=4` Hall return

**Verdict:** **GREEN** at the pinned revisions below.  This is an independent
internal audit, not external peer review.

## Pinned artefacts

```text
e5ad8fef32d6581234d5873317c77592757b1cd809c2a95c6bbbc2b710fec78c
  active/hc7_k7minus_sparse_sixcut_order_seven_i4_completion.md
08d284ea78a8a1d97ce3506166f005815507dbdcd852f6a73896f3148eca58e7
  active/experiments/sparse_sixcut_order_seven_i4_completion/verify.py
```

This theorem source differs from the revision first audited, whose SHA-256
was `6d0a3a0240bd385c75b64d5755677624c98b9485a4a549dc673feafcbb1e5147`,
only in the status text: `independent cold audit pending` was replaced by
`independently cold-audited`.  The theorem statement, proofs, fourteen-row
table and reproduction instructions are unchanged.

The Hall-profile input used by the terminal composition was checked at

```text
a81cb9476890fe0d373ecdc8aecebf5a40996d7d44ba15f16faf076dd5b581d8
  active/hc7_k7minus_ordinary_k5minus_rooting_contraction_gate.md
```

## 1. The overlapping deletion reduction

For every chosen `u in U`, inclusion-minimal Hall deficiency matches
`U-{u}` bijectively to `R`, while the complementary Hall calculation matches
`W` bijectively to `T`.  The two root sets are disjoint and together have
order six.  Hence all six vertices of `C-u` have distinct matched roots.

If `C-u` had an ordinary five-bag `K_5^-` model, choose one matched vertex
from each branch bag and adjoin its root.  This preserves connectivity,
disjointness and every quotient contact, and uses five distinct roots.
Thus it gives precisely the excluded punctured rooted model.  Lemma 1.1 has
no hidden assumption that an individual member of `U` dominates `W`.

## 2. The six-vertex extremal lemma

The edge count in Lemma 1.2 is correct.  At thirteen or more edges, deletion
of a minimum-degree vertex leaves at least nine edges.  At twelve edges the
same conclusion holds unless every degree is four; the unique exceptional
graph is `K_{2,2,2}`, and contracting an edge between two parts leaves only
the nonedge inside the third part.

At eleven edges, target exclusion makes every original degree at least
three.  The four-edge complement therefore has maximum degree at most two,
and its component decomposition is exactly

```text
C_4+2K_1,  C_3+K_2+K_1,  P_5+K_1,  P_4+K_2,  P_3+P_3.
```

I checked each stated contraction in the last four cases.  The contracted
pair is an edge of the original graph, its bag contacts every remaining
singleton except in at most one case, and the remaining singletons have at
most one noncontact in total.  For complement `C_4+2K_1`, a five-singleton
model leaves at least two cycle-complement edges.  A spanning five-bag model
has one two-vertex bag: if it uses a universal vertex, at least two
cycle-complement edges remain; otherwise it joins opposite cycle vertices
and misses both other cycle vertices.  Hence `K_2 join 2K_2` is genuinely
minor-free.

As a separate exhaustive check, independently written code tested every
graph on six labelled vertices by all connected five-bag partitions.  It
found

```text
maximum edges in a K_5^--minor-free graph       11
labelled equality graphs                         45
equality degree sequence                 5,5,3,3,3,3
```

The `45=15*3` equality graphs are exactly the choices of the universal
`K_2` and a matching on the remaining four vertices, so they form the one
claimed isomorphism class.

## 3. The internal edge ceiling

Lemma 1.1 gives `e(C)-d_C(u)<=11` for each `u in U`.  Since a shore vertex
has at most six neighbours in `C`, equality `e(C)=17` would force every
member of `U` to be universal, already supplying all six edges of `U` and
all twelve `U`--`W` edges.

For `e(C)=16`, write `a=e(U)`, `b=e(U,W)` and `c=e(W)`.  Connectivity of the
three-vertex branch bag gives `c>=2`, and every `u in U` has degree at least
five.  Therefore

```text
20 <= 2a+b = a+16-c <= 6+16-2 = 20.
```

Thus `U=K_4`, `c=2`, and every member of `U` has degree five.  Deleting one
member gives an eleven-edge graph in which each other member of `U` has
degree four, contradicting the equality degree sequence above.  This proves
the stated sharp ceiling `e(C)<=15`; the source does not claim a
classification of equality at fifteen.

## 4. The fourteen incidence cases

I reconstructed the incidence search without importing the frozen verifier.
For a `K_4`, validity means that all three `W` columns are nonempty and at
most one `U` row is empty.  For `K_4-01`, every row and column is nonempty.
The exact counts are

```text
                         valid masks   minimal masks   path orbits
K_4                             3221              60             3
K_4-01                          2161              48            11
```

Canonicalisation under all `U` permutations in the first case, under the
permutations preserving `{0,1}` in the second, and under path reversal gave
exactly the fourteen neighbourhood strings printed in the theorem.  The
orbits are disjoint and cover every inclusion-minimal valid mask.  Every
valid mask contains a minimal one, so restoring deleted incidence edges
cannot lose a displayed model.

I also performed a methodologically separate direct rooted search over all
`5382` valid masks.  For each mask it chose the unmatched `U` vertex, chose
one of the six matched vertices whose root is omitted, and assigned the two
remaining internal vertices either to one of the five anchored bags or to
no bag.  It then tested bag connectivity and all ten quotient contacts.
This search used neither the fourteen representatives nor the verifier's
containment test and found zero failures.

Finally, I checked every displayed row individually.  Each part is
connected, the five parts are disjoint, each contains its claimed matched
anchor, and at least nine of the ten pairs contact.  If `o` is a `W` vertex,
the three `U-{u}` roots and the other two `W` roots are used.  If `o` lies
in `U-{u}`, two `U` roots and all three `W` roots are used.  Thus every row
uses exactly five distinct roots and omits the sixth; placing an omitted or
unmatched internal vertex inside another anchored bag causes no root
collision.

The pinned verifier was rerun with assertions enabled and reproduced

```text
K4: valid=3221 minimal=60 orbits=3
K4-minus-edge: valid=2161 minimal=48 orbits=11
order-seven i=4 completion table: PASS
```

## 5. Terminal composition and scope

For `i=4`, the four deficient bags are singleton vertices and the fifth bag
is the connected three-vertex set `W`.  Collective domination
`N_C(U)=C-U` says that every vertex of `W`, not every individual member of
`U`, has a cross-neighbour.  The ordinary five-bag quotient says exactly
that

```text
(missing edges in U) + (members of U with no neighbour in W) <= 1.
```

Deleting an edge of a triangular `W` if necessary gives the spanning path
used by Lemma 2.1.  The two Hall matchings then meet its root convention, so
the fourteen-case lemma returns the punctured rooted `K_5^-` model.  No
excess, relative-connectivity or packet assumption is used after the Hall
profile has been obtained.

No reduction, extremal, orbit-coverage, root-accounting or composition gap
was found.  The result closes the `i=4` order-seven Hall case; it does not by
itself close the `i=2` or `i=3` cases or the full sparse-six-cut programme.
