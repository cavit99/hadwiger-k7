# Separate internal audit: the matching response square

**Verdict:** GREEN for Theorems 2.1, 2.2, 2.4 and 2.6, Lemma 2.3,
Corollary 2.5, Theorems 3.1 and 3.2, and Proposition 4.1.  Section 5
correctly records an unresolved model-allocation problem; it is not a
claim that the matching branch or `HC_7` has been closed.  This is a
separate internal mathematical audit, not external peer review.

## Exact revision

The audited source is
[`hc7_k7minus_matching_square_common_state.md`](hc7_k7minus_matching_square_common_state.md),
with SHA-256

```text
ca291c23674c11832159301af0c9d1bd7bfd5302495359bbfe81b4f8a5f55e14
```

The promoted source differs from the initially audited revision
`0133c86db86594c43738ea207665a6cc5c8bdedbd3b95f52d112580aa7705d2a`
only in its status header and the directory-relative link to the finite
diagnostic.  Its mathematical content is unchanged.

The audit checks the displayed abstract hypotheses.  The live matching-row
application additionally depends on the separately audited six-coordinate
forest and six-cut localisation results for the two opposite coordinates
and the two seven-connected restorations.

## 1. Common deletion and double contraction

The spanning six-connected subgraph `X` makes `H=G-{e,f}` six-connected.
Minor-minimality makes `H` at most six-chromatic.  A five-colouring would
be repaired by giving the nonadjacent open-shore vertices `u,v` one fresh
colour, so `chi(H)=6`.

Colourings of `G/e`, `G/f` and `G/e/f` expand to the three nonempty
signatures on `H`.  The all-proper signature would colour `G` after both
edges were restored.  The same fresh-colour argument rules out a
five-colouring of `G/e/f`.  Thus `HC_6` supplies one `K_6` model in the
double contraction; making it spanning and lifting it co-bags both named
endpoint pairs in the same model.  No assertion that all four endpoints
belong to one bag is made.

The rooted-`K_4` conclusion in Theorem 2.1(5) follows from the standard
two-linked/rooted-`K_4` implication for six-connected graphs.  The claim is
valid, but the source should acquire an exact primary citation before
publication.  It is not used in Theorems 2.2--2.6 or 3.1--4.1.

## 2. Connectivity and response separations

For a cut of `G/e/f`, replacing either contraction vertex in the cut by
its two preimages increases its order by at most two.  Seven-connectivity
therefore gives connectivity at least five.  Every order-five cut must
contain both contraction vertices and lifts exactly to an order-seven cut
of `G`.  Fullness and the rejected-partition response then follow from
seven-connectivity and a colouring of one deleted boundary edge.  This
checks Theorem 2.2.

Lemma 2.3 uses fullness only to obtain internally shore-confined connector
paths.  It correctly does **not** replace those paths by the unsupported
edges `uq,vp`, and correctly declines to contract the resulting arbitrary
cycle.

For Theorem 2.4, an order-six cut of `H` leaves exactly two components:
either one-edge restoration can join all components only in that case, and
both restored edges must cross the same split.  The two edges are
vertex-disjoint, so either mixed choice of endpoints leaves a vertex on
each side and gives an actual order-eight separation in `G`.  Taking a
component behind it produces an actual separator of order seven or eight
and the stated proper-minor response.  Consequently, after those responses
are excluded, `H` is seven-connected.  Its `4|V(H)|-2` density then permits
the stated application of Norin--Totschnig Theorem 6; the order hypothesis
excludes the small exception, and target exclusion makes the spanning
`K_7^vee` model exact.  This checks Corollary 2.5.

## 3. Spending the forbidden signature

In Theorem 2.6, switching an unlocked bichromatic component at one end of
the equal coordinate must make the other coordinate monochromatic; an
all-proper result is forbidden.  Repeating from the original colouring at
the other end gives two crossed bichromatic components, each containing
one end of each coordinate.  A nondominating component supplies an actual
separator of order at least seven and two opposite responses which agree
literally on its exterior.

If both components dominated, the only edges between them would be the two
deleted coordinates.  Domination forces each component to consist of its
two coordinate endpoints, hence the four endpoints induce a cycle.
Contracting that cycle gives an exactly six-chromatic proper minor.  A
spanning `K_6` model in the contraction lifts so that the two dominating
components and the five foreign bags form an explicit `K_7` model.  This
contradicts the hypotheses.  The resulting conclusion is exact: after all
such response separators are excluded, every singleton response locks its
equal pair in all five alternate palettes.

The returned separator has no proved upper bound.  In particular,
Theorem 2.6 is not by itself an order-seven or order-eight descent theorem.

## 4. Fans, locks and model splitting

For Theorem 3.1, simultaneous repair of both shores with the fixed
double-contraction partition would glue to a six-colouring of `G`.  On a
nonrepairable shore, each alternate-colour component at the open endpoint
must reach the boundary.  The Menger obstruction to retaining the five
prescribed first edges has order at most six:

```text
{u,p} union D union Z,
|D|+|Z|+2 <= h+(5-h-1)+2=6.
```

The nonempty opposite shore makes this a forbidden cut.  The resulting
five paths, together with the selected edge, are therefore a genuine
shore-confined six-fan with distinct boundary ends.

Theorem 3.2 is the standard component-switch calculation over `F_2`.  For
equal root colours, every alternate palette locks at least one coordinate,
giving three locks on one.  For distinct root colours, two unlocked
palettes on the two coordinates must coincide; including their mutual
palette gives four locks on one coordinate.  The proof claims no
disjointness among the lock paths.

For Proposition 4.1, a spanning tree of the co-bagged branch set can be
chosen to contain the restored coordinate.  Removing that edge gives two
connected split sets.  Four foreign bags meeting both, together with the
fifth bag meeting at least one, give seven connected bags with at most one
missing adjacency.  This is exactly a `K_7^-` model.

## 5. Unresolved point and trust boundary

The proof does not assign the fan ends or the five palette-lock paths to
the five foreign bags of the common `K_6` model.  A lock path may pass from
one one-sided bag to another without making either bag adjacent to both
sides of the root split.  Nor is it proved that both shores reject the
fixed double-contraction partition.

The live matching residue is therefore still:

```text
all five alternate palettes locked
plus one common co-bagged K6 model
plus a one- or two-shore response fan
```

without the four foreign double contacts, a common boundary partition, or
an order-at-most-eight labelled response.  Large response separators also
remain unterminalised.  No theorem in the source proves the matching row,
the six-coordinate forest branch, the `K_7^-` six-colour conjecture, or
`HC_7`.

The external inputs are `HC_6`, Norin--Totschnig Theorem 6, Menger's
theorem, the six-connected two-linked theorem, and the rooted-`K_4`
characterisation.  The proof itself is unbounded and uses no finite
enumeration.
