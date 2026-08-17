# Cold audit: tripod configuration or exact-six fragment

**Audit status:** GREEN.

**Source audited:**
[`hc7_k7minus_sparse_sixcut_tripod_or_exact_fragment.md`](hc7_k7minus_sparse_sixcut_tripod_or_exact_fragment.md),
SHA-256

```text
dc0d5784eccc26a0e04188b92524f54c71dc5b737cdb22f55c4d26439a14c226
```

The current source SHA-256 is
`0444ca85f21fe12638e183298e612fe2efe9efb6b28fff108ae327cc8248f08d`.
The only post-audit change marks the source as independently audited; the
mathematical text is unchanged.

The audit was performed independently from the derivation.  It checks the
stated source theorem, every separator lift, the coefficient-four identity,
the rooted-model decoder added in Section 3, and the three-vertex guardrail.
It does not certify any stronger packet inequality or density implication.

## 1. Primary-source input

Theorem 1.2 of Hayashi--Kawarabayashi--Yoo was checked against the published
statement and the definitions immediately preceding it.  The four hypotheses
recorded in Section 1 are the hypotheses used there: connected nontrivial
interior, the rooted separation restriction of order at most three, the
two--two separation restriction of order at most two, and exterior degree at
least two at each of the four stable roots.  The three alternatives and their
limited rooting information are represented conservatively.  In particular,
the note does not silently turn a foot into a branch vertex or claim that all
four roots occur as branches of the returned subdivision.

## 2. Separator arithmetic

For a separation of order at most three with all four roots on one side, a
component `X_0` in the nonempty open side has

```text
N_G(X_0) subseteq (A intersect B) union R.
```

The right-hand side has at most five vertices.  At least one of the four roots
lies outside `X_0 union N_G(X_0)`, since the separator has order at most three.
Thus this is a genuine cut contradiction to six-connectivity, including when
some roots lie in the separator.

If the two--two hypothesis fails, the four roots lie in the two open sides,
so the separator `T` is contained in `C`.  Since `|C|>=3>|T|`, one open side
contains a vertex of `C`.  For a component `X` there,

```text
N_G(X) subseteq T union Z_X union R.
```

The opposite two roots give a vertex outside the closed shore.  Hence
six-connectivity forces equality, `|T|=2`, and all six displayed vertices are
actual neighbours of `X`.  This proves both exactness and properness of the
derived six-fragment.

The excess identity is exact.  Edges internal to `X` and edges from `X` to
`T union Z_X union R` form precisely the first summand.  Every remaining
internal edge of `C`, and every remaining edge from `C` to `S`, forms the
second.  No edge from `X` to `Z_Y` exists.  The vertex terms partition `C`, so
no correction term is missing.

Completing `S` to a clique creates no new edge incident with `X`.  Therefore
the quoted six-boundary rerooting corollary applies to the exact fragment with
the claimed punctured confinement.  The source and its independent audit are
pinned in the audited note.

## 3. Rooted-model normalisation and decoders

Lemma 3.1 is correct.  Maximising the union of a rooted `K_4` model absorbs
each component outside the model into a bag it meets, preserving every old
bag adjacency and root.  The resulting bags span `C union Z`.  A singleton
omitted root meeting three bags then leaves at most one missing pair among the
five bags, and the unused sixth root is absent.

Each row of Proposition 3.2 was reconstructed directly:

* splitting the three diamond paths gives a four-bag `K_4^-` quotient;
* splitting the four paths of the `K_{2,3}^+` subdivision gives its five-bag
  quotient with seven edges, and two foot-bag contacts raise this to nine;
* contracting subdivision paths towards branch vertices gives the five bags
  of the `K_5^-` quotient.

The repaired statement explicitly confines every relevant augmentation and
model to `G-s`.  Thus the omitted root cannot be used internally.  In the
second and third rows, “appended” entails disjointness from the existing bags
as well as mutual disjointness, so the added roots remain on distinct branch
bags.  No row claims that the primary subdivision alone supplies those
augmentations.

## 4. Guardrail reconstruction

For the triangle atom, all seven nonempty subsets of `C` meet the relative
six-connectivity inequality, the stated excess is `4`, and every `S`-full
connected set has at least two vertices, giving packet number one.

A five-root model on only three internal vertices must have at least two
singleton boundary bags.  Three singleton boundary bags would already create
three missing pairs, so exactly two are possible; stability then forces both
singleton roots to see all three internal vertices.  Only root `0` does, which
excludes the model.  The displayed spanning rooted `K_4`, diamond paths, and
four `a`--`b` paths for the `K_{2,3}^+` subdivision were also checked edge by
edge.

## 5. Scope verdict

The exact-six peel, hereditary rerooting step, incidence decoder, and sharp
low-excess example are sound.  The source accurately labels the unresolved
step: the inseparable subdivision outcome still needs a density-sensitive
augmentation or a second full packet.
