# Cold audit: ordinary-`K_5^-` rooting contraction gate

**Audit status:** GREEN.

**Source audited:**
[`hc7_k7minus_ordinary_k5minus_rooting_contraction_gate.md`](hc7_k7minus_ordinary_k5minus_rooting_contraction_gate.md),
SHA-256

```text
0e078226085a494413fac157ca4de6cc4ebcb0fb5eb855a2f8738d141b59776a
```

The audit reconstructs the small-order Hall argument, the arbitrary-order
literal-core linkage, both directions of the contraction obstruction, all
lifting assertions, and the order-seven deficiency profile.  It does not
certify a transfer of two packets across a derived boundary or elimination
of the exact fragments.

## 1. The order-at-most-six row

For every nonempty `X subseteq C`, the elementary bound

```text
|N_C(X)|<=|C|-|X|<=6-|X|
```

and relative six-connectivity give `|N_S(X)|>=|X|`.  These are exactly
Hall's inequalities for a matching saturating `C`.  Selecting one vertex in
each of the five ordinary branch bags gives five distinct matched roots.
Adjoining a root along its matching edge preserves disjointness,
connectedness, and every old quotient adjacency.  The unused sixth root is
not in a branch bag, so the model is genuinely punctured.  The proof does
not assume that a five-vertex model spans a six-vertex shore.

## 2. The arbitrary-order literal core

Let `W` be the five vertices of a literal `K_5^-`.  Any vertex separator of
order at most four leaves a vertex of both `S` and `W`.  If it separated the
two surviving sets, the component containing a surviving vertex of `W` but
no root would be a nonempty subset of `C` with external neighbourhood of
order at most four, contrary to relative six-connectivity.  The set form of
Menger therefore gives five vertex-disjoint `S`--`W` paths.  Their endpoints
are distinct and, because `|W|=5`, exhaust `W`.

On each path, begin at its last root and stop at the first later vertex of
`W`.  These subpaths remain disjoint, meet `S` and `W` only in their ends,
and still exhaust `W`.  Taking them as five branch bags therefore retains
the nine literal near-clique edges, uses five distinct roots, and omits the
sixth root entirely.  This verifies Theorem 2.2 at arbitrary shore order;
no Hall condition on all of `C` is being smuggled into the argument.

## 3. Contraction quantifiers

Let `w` be the contraction of `uv`.  If a test set contains `w`, replacing
`w` by both ends of the edge leaves its external vertex-neighbourhood
unchanged.  If it avoids `w`, its boundary can change only by identifying
`u` and `v`; it drops by one precisely when both are old boundary vertices.
Because every old boundary has order at least six, a contracted boundary has
order at most five exactly when the old boundary has order six and contains
both `u,v`.

The connected-witness normalisation is valid.  For any component `X_0` of a
possibly disconnected witness `X`,

```text
N_H(X_0) subseteq N_H(X),
```

whilst relative six-connectivity gives `|N_H(X_0)|>=6` and the witness has
`|N_H(X)|=6`.  Hence the two sets are equal, so both `u,v` remain boundary
vertices of `X_0`.  This proves the stated if and only if with a nonempty
connected witness; no minimality or hidden inducedness assumption is used.

## 4. Lifting and minimality

Contracting an edge internal to one ordinary branch bag retains that model.
Conversely, replacing `w` by the connected edge `uv` in the unique rooted
bag or packet that uses it restores every edge represented after
contraction.  At most one member of a disjoint two-packet family can use
`w`, so disjointness also lifts.  The six roots are never identified.

Thus, if such a contraction preserved relative six-connectivity in a
minimum-order counterexample, the smaller instance would return one of the
two desired outcomes and that outcome would lift.  Lemma 3.1 therefore
forces the exact fragment on every edge internal to the chosen ordinary
model.  The order lower bound follows independently from the small-order
row.

## 5. The order-seven Hall profile

Absorbing each component outside an ordinary model into any branch bag it
meets produces a spanning five-bag partition without deleting a quotient
edge.  Let `I` be an inclusion-minimal deficient family, `i=|I|`, and let
`U` be the union of its bags.  Hall deficiency and relative connectivity
give the equality chain

```text
6 <= |N_C(U)|+|N_S(U)|
  <= (7-|U|)+(i-1)
  <= 6.
```

Consequently `|U|=i`, `|N_S(U)|=i-1`, and
`N_C(U)=C-U`.  In particular every bag of `I` is a singleton and every such
vertex is adjacent to all of `C-U`.  Inclusion-minimal deficiency supplies a
matching of `i-1` of these bags to all `i-1` roots in `N_S(U)`.

For nonempty `Y subseteq C-U`, applying relative connectivity to `U union Y`
and subtracting the already counted root set gives

```text
|N_S(Y)-N_S(U)|>=|Y|.
```

This is Hall's condition from `C-U` to `S-N_S(U)`; both sets have order
`7-i`, so the matching is perfect.  The five model bags contain seven shore
vertices, hence the complementary `5-i` bags contain exactly two vertices
beyond one representative per bag.  Combining the two matchings roots four
of the five branch bags, leaves exactly one universal singleton bag
unassigned, and distinctly matches the two surplus complementary vertices.

Here “unrooted” is correctly read relative to this assembled matching: it
does not assert that the singleton has no boundary neighbours.  With that
standard meaning, the final profile follows exactly as written.  Moving a
surplus matched vertex while preserving its old branch-bag quotient contacts
is indeed an additional, unproved operation, as the source states.

## 6. Scope verdict

All stated implications are sound under the explicit stable-boundary and
relative-six-connectivity hypotheses.  The result identifies a genuine
exact-six obstruction but does not make the two-packet outcome hereditary;
the source labels that remaining obstruction accurately.
