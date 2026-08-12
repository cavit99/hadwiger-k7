# Internal audit: complementary response families at a six-cut

**Verdict:** GREEN for Theorems 2.1 and 3.1 and for their stated scope.
The constructions give actual common separators with nonempty open shores,
proper exterior colourings, rejected boundary partitions, and disjoint
partition families.  This is a separate internal mathematical audit, not
external peer review.

## 1. Exact revision

The audited source is
[`hc7_k7minus_six_cut_complementary_cube_lift.md`](hc7_k7minus_six_cut_complementary_cube_lift.md),
with SHA-256

```text
007ee9ce7aaced1564fae9ada9b0e33dd65ef29cf12f0adc396d278653189f74
```

Relative to the revision first checked, this hash changes only the source
status, line wrapping and same-directory dependency links; the theorem
statements and proofs are unchanged.

Its input is the separately audited six-coordinate induced-forest
reduction.  Thus `X=G-F` has a six-cut `S` with exactly two full components
`C,D`, the selected restorer edges cross between them, and every nonempty
subset of `F` occurs as the exact monochromatic-edge signature of a proper
six-colouring of `X`.

## 2. Matching rows

Every edge of `G` between `C` and `D` is a deleted forest edge, because
`C,D` are components of `X-S`.  In the matching case the selected endpoint
set contains exactly one end of each crossing edge.  It is disjoint from
`S` and has order `q`, so the displayed boundary has order `6+q` and meets
every cross-shore edge.

The two parts `E_C,E_D` are nonempty.  The `C`-end of every edge in `E_C`
is left in `C'`, and the `D`-end of every edge in `E_D` is left in `D'`.
Hence both open shores are nonempty.  They are anticomplete because every
crossing edge meets the boundary.  The displayed partition therefore gives
an actual proper two-sided separator.

For nonempty `J subseteq E_C`, the only monochromatic edges after restoring
`F` are the members of `J`, and every such edge has an end in `C'`.
Deleting `C'` makes the restriction proper on all of `G-C'`.  If its
partition on the whole boundary `T` extended through `C'`, a permutation
of colour names would align the two colourings pointwise on `T`; the
colourings would then glue to a six-colouring of `G`.  Thus the partition
is rejected.  The symmetric argument for `E_D` is identical.

If a partition occurred in both families, use the `E_C` colouring on
`D' union T` and the `E_D` colouring on `C' union T`, after aligning colour
names on `T`.  Both restrictions are proper and the open shores are
anticomplete.  This again six-colours `G`, proving that the two families
are disjoint.  The argument compares realised partitions, not their cube
indices, and therefore does not assume that different indices give
different partitions.

## 3. Induced-path row

In the path case, `r` meets both path restorers and lies in `C`, while the
two leaves lie in `D`.  The boundary contains `S`, `r`, and the `D`-end of
each crossing edge of `M_0`.  These vertices are distinct, so its order is
`7+k`, at most eleven.

The hypothesis `C!={r}` makes `C'=C-{r}` nonempty.  Both path leaves remain
in `D'`, because `M_0` is disjoint from the path, so `D'` is nonempty.
The boundary meets the path restorers at `r` and every crossing matching
edge at its selected `D`-end.  Thus the open shores are anticomplete.

For a nonempty signature inside `E_0`, each monochromatic edge has its
other end in `C'`, and deletion of `C'` makes the exterior restriction
proper.  For a nonempty signature inside `{rx,ry}`, each monochromatic
edge has its leaf end in `D'`, and deletion of `D'` makes that restriction
proper.  The same extension-rejection and common-partition gluing arguments
used in the matching row apply without alteration.

The omitted case `C={r}` is exactly the separately audited degree-eight
singleton outcome, and the source states only conclusions already proved
there.

## 4. Trust boundary

The theorem supplies disjoint nonempty *families* of boundary partitions.
It neither proves that all cube indices give different partitions nor
prevents the two families from being disjoint.  The matching boundaries
can have orders nine through twelve and the induced-path boundaries orders
eight through eleven; the selected boundary vertices need not be full to
the residual shores.  Existing order-eight or exact-full-boundary results
therefore do not automatically close these rows.  The stated
complementary-cube synchronisation target is the exact remaining
unsupported implication.
