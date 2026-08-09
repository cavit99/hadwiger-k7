# Internal audit: trace-preserving descent from a four-centre exact cut

Audited file:
`results/hc7_k7minus_four_centre_trace_descent.md`.

Audited mathematical revision SHA-256:

```text
41fabe3036e1b3fa2d479e7b87d9fd767d55b3dbb245fa74de2a67455d920029
```

Previously promoted source SHA-256:

```text
f3bc2374c410631a39a98a63f05db8eab52a7271f58be70bb313241c7f8a7e71
```

Previous promoted source SHA-256:

```text
cbbefe62836e889f44bae6e41ac52ac0ffe54e05dbe86e2fc200c8f9f2d918ab
```

Current promoted source SHA-256:

```text
04d4585b25ce9fbd8f3392b715eb28caa7e4b008e45072ede2b08cbbf0bfecff
```

The previously promoted source differs from the audited mathematical
revision only in the opening status label, where
`pending` was replaced by `GREEN`.  Its mathematical content is unchanged.
The next source differs from that previously promoted source only by
deleting the redundant dependency-list bullet for the two-component normal
form.  That input remains pinned below.  No theorem statement or proof was
changed.

The current source differs from it only in the final scope sentence, where
the undefined phrase `rooted augmentation` is replaced by the precise
non-result: an explicit `K_7^-`-minor model extending the rooted branch
sets.  The accompanying line reflow is mechanical.  This clarifies the
intended terminal output and changes no proved assertion.

**Verdict:** **GREEN** for all four revisions above.

This is a separate internal mathematical audit, not external peer review.
The proof was reconstructed from the definitions of mixed-separation
reduction and lifted order; no computation is used.

## One-vertex descent and the minimum selected side

In Theorem 2.1, the selected component cannot be the singleton `{c}`:
then all neighbours of `c` would lie in the seven-vertex boundary, contrary
to minimum degree eight.  After exchanging `t` for its unique neighbour `c`,
the remaining vertices split as `C-c` and `D+t`.  These sets are nonempty
and anticomplete, and `D+t` is connected.  Hence the new seven-set is a
genuine cut.  The audited two-component theorem makes `C-c` connected and
shows that these are exactly the two components; seven-connectivity makes
both components full at the new boundary.

The identity

```text
(C-c) union U union ((T-t)+c) = C union U union (T-t)
```

puts the new selected closed side inside the old one.  Its colouring is
therefore a restriction of the accepted colouring, and the fixed colour
`gamma` remains available at `r`.  All four selected terminals still avoid
the smaller component, while `x_j` remains in the opposite component.  The
new cut is consequently trace-admissible and has selected component of
order `|C|-1`.

A minimum trace-admissible selected component exists because the graph is
finite and the original rooted-web cut is admissible.  Boundary fullness
gives every `t in T` a neighbour in `C`; uniqueness would invoke Theorem 2.1
and contradict minimality.  Thus every boundary vertex has at least two
neighbours in `C`.  In Carmesin--Kurkofka reduction no boundary vertex can
then be deleted from the selected side, so that side remains exactly
`C union T`, as asserted in Corollary 2.2.

## Anchored meet descent

Let `q=rho(p_0)`.  Since its selected side is literally `C union T`, the
relation `a=(P,Q)<=q` puts `P` inside `C union T` and puts all of `D` in
`Q-P`.  Hence the chosen vertices `c_0 in C cap (P-Q)` and `x_j in D` are
opposite open-side anchors, and they are nonadjacent because `C,D` are
anticomplete.

For the nontrivial tri-separation `a`, Carmesin--Kurkofka Lemma 1.3.3 makes
its separator-edge elements a matching.  Replacing every such edge by one
endpoint therefore produces an ordinary three-separation.  Choosing the
other endpoint on an edge incident with `c_0` or `x_j` leaves each named
vertex in its original open side.  The instructions cannot conflict: the
separator edges form a matching and `c_0x_j` is absent.  The resulting
ordinary separation is proper and still has `c_0,x_j` as opposite anchors.

The original order-seven cut and seven-connectivity give `kappa(G)=7`.
Corollary 3.3 of the audited four-centre cut-lattice theorem then makes all
four vertices of `U` cross both ordinary three-separations, each of lifted
order seven.  Its fixed-anchor uncrossing theorem applies to their meet.
The meet is proper, has lifted order seven, and is crossed by every member
of `U`; its ordinary separator therefore has order `7-4=3`, and adjoining
`U` gives an exact order-seven cut in `G`.

The meet's selected open side is exactly

```text
C cap (bar P-bar Q).
```

It contains `c_0`.  The vertex `z in C cap (Q-P)` remains either in the
opposite open side or becomes a boundary vertex when the mixed separator is
converted, so it is absent from the meet's selected open side.  The descent
is therefore nonempty and strict.  The two-component theorem makes both new
open sides connected, the opposite side contains `x_j`, and
seven-connectivity makes both components boundary-full.

The meet's selected closed side is contained in `C union T`.  Restricting
the old accepted colouring preserves the extension at `r`; the smaller
component still avoids every `x_i`.  The graph, fixed colouring, selected
vertices and named bichromatic component have not been altered.  Reducing
the new ordinary separation supplies the claimed new mixed separator and
its boundary-provenance map.  Thus every assertion of Theorem 3.1, including
connectivity, strictness and label preservation, follows.

## Totally nested residue

If `q` is totally nested, every nontrivial tri-separation is nested with it.
The side of `q` opposite `C union T` contains no vertex of `C`.  A nested
tri-separation that split `C` could not contain `q` in either orientation,
as that would put all of `C` on one side; it can therefore be oriented below
`q`.  Theorem 3.1 would then give a smaller trace-admissible selected
component, contradicting minimality.  Corollary 3.2 is correct.

## Pinned dependencies and scope

The local inputs used above are present at their separately audited
revisions:

```text
four-centre rooted-web and fixed-anchor cut lattice
e7fcf00c9bdbd2fcbab78bb13d4244a659f4f7db0ae45a97cfbd9a8d599a0ee3

canonical tri-separation reduction and boundary map
b5b0ff71e8942d4b16674a25362c9459523c4c7460f15176892d4ded8a82b682

two-component normal form for seven-vertex cuts
1041988a33b749bef5802dd21d3cd9419b5afc754735a20174bf5a13c0a56c96
```

The unresolved canonical-adhesion case is a minimum trace-admissible cut
whose reduction is a canonical adhesion: every boundary vertex has at least two
neighbours in its selected component, the selected side survives reduction
literally, and no nontrivial tri-separation splits that component.  The note
does not obtain a common boundary colouring or an explicit `K_7^-`-minor
model extending the named rooted branch sets in this
case.  It therefore does not eliminate the rooted-web outcome, prove the
`K_7^-` six-colour conjecture, or settle Hadwiger's conjecture for `t=7`.
