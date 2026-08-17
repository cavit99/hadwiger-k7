# Cold audit: ordinary-`K_5^-` rooting contraction gate

**Audit status:** GREEN after correction of the order-seven contact profile.

**Source audited:**
[`hc7_k7minus_ordinary_k5minus_rooting_contraction_gate.md`](hc7_k7minus_ordinary_k5minus_rooting_contraction_gate.md),
SHA-256

```text
a81cb9476890fe0d373ecdc8aecebf5a40996d7d44ba15f16faf076dd5b581d8
```

The audit reconstructs the small-order Hall argument, the arbitrary-order
literal-core linkage, both directions of the contraction obstruction, all
lifting assertions, and the corrected order-seven deficiency profile.  An
earlier revision incorrectly promoted collective domination by a deficient
family to individual universality of each singleton bag.  The argument below
does not make that inference.  The audit does not certify a transfer of two
packets across a derived boundary or elimination of the exact fragments.

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
`N_C(U)=C-U`.  In particular every bag of `I` is a singleton and their union
dominates `C-U`.  This equality does not say that each singleton is adjacent
to every vertex of `C-U` when `i>1`.  Inclusion-minimal deficiency supplies a
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
of the five branch bags, leaves exactly one singleton bag unmatched, and
distinctly matches the two surplus complementary vertices.  If `i=1`, the
unmatched singleton alone dominates `C-U` and has no root neighbour, so it is
individually universal in `C` and has total degree six.  If `i>1`, neither an
individual universal singleton nor a quotient-preserving surplus transfer is
forced.  The corrected source records that distribution problem as open.

## 6. Scope verdict

All corrected implications are sound under the explicit stable-boundary and
relative-six-connectivity hypotheses.  The result identifies a genuine
exact-six obstruction but does not make the two-packet outcome hereditary or
resolve the `i>1` order-seven contact distribution; the source labels both
remaining obstructions accurately.
