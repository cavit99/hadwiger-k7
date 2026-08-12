# Internal audit: seven-removable matching reduction

**Verdict:** GREEN for Theorems 2.1, 3.1 and 4.1, Lemma 2.2 and
Corollary 4.2.  Two independent cold readings reached the same verdict.
This is an internal mathematical audit, not external peer review.

## 1. Exact revision and dependencies

The audited source is
[`hc7_k7minus_seven_removable_matching_reduction.md`](hc7_k7minus_seven_removable_matching_reduction.md),
with SHA-256

```text
d62491aad7d9a5474a6eeed355f4a6f31977c7bd1ce9a05bc1231d00a0a23e13
```

The repository inputs used in the proof were checked at these audited
source revisions:

```text
61fa3c094c34d06590efcef8a6903356f36bc8aadcdec75f834aa7e5cfd82936  hc7_contracted_edge_k6_model_normalization.md
4845f5375581971aca7397bbac0e3eb930dd2943c9dca71f6264a24e2fa31c6e  hc7_k7minus_exact_k7vee_separator_dichotomy.md
c81a3f7d656a4ef02a69ab88b311acc3601d9103aedbf6b6380c54cee350a3c3  hc7_k7minus_dense_branch_rotation_visibility.md
```

The external inputs were checked against their stated sources.  Theorem 1.3
of Chu's preprint gives a `k`-removable matching of order `m` when
`delta(G)>=max{k+1,2m-2}`, apart from `K_{2m-1}` and an irrelevant cycle
case.  At `(k,m)=(7,5)` the threshold is eight and the order hypothesis
excludes `K_9`.  Theorem 6 of Norin and Totschnig applies to a
four-connected graph with at least `4n-8` edges, apart from
`K_{2,2,2,2}`.  Here the common host is seven-connected, has at least
`4n-5` edges and has order at least 25.

Chu's paper was a recent preprint at the time of this audit.  Verifying its
stated theorem and its use here is not an independent audit of Chu's proof.

## 2. Matching signatures and singleton operations

For every nonempty `J subseteq M`, a six-colouring of `G/J` expands to the
common graph `H=G-M`.  Every edge of `J` has equal-coloured ends, while
every edge of `M-J` remains literal because `M` is a matching and is
therefore bichromatic.  This proves the exact signature `J`.  An empty
signature would remain proper after restoring `M` and would six-colour
`G`.

For one edge `e`, both `G-e` and `G/e` are proper minors.  A five-colouring
of either graph can be expanded and one end recoloured with a fresh sixth
colour to colour `G`; hence both graphs are exactly six-chromatic.  The
audited contraction-bag normalization therefore supplies the connected
one-end side and its actual separator.  Seven-connectivity supplies the
order-seven lower bound.

Lemma 2.2 correctly works for every nonempty proper set meeting `V(M)`.
A singleton-signature colouring has just one restored monochromatic edge,
and deleting the set removes one of its ends.  Any interior colouring with
the same boundary equality partition can be palette-permuted to agree
literally on the boundary, then glued to colour `G`.  Thus the claimed
rejected trace is partition-specific as well as literal.

## 3. Exact near-clique model and endpoint support

Norin--Totschnig Theorem 6 supplies a `K_7^vee` model in `H`, and absorbing
unused components makes it spanning.  If restoring the matching supplied
either nominally missing adjacency, the displayed seven bags would give a
`K_7^-` model.  Target exclusion therefore makes the partition an exact
spanning model in `G`, so the audited exact-model dichotomy applies.

The two-portal proof was checked by rerunning that dichotomy with the two
prescribed matching endpoints.  Every separator branch captures one of
them; the alternative is the explicit target model.  The matching endpoint
then supplies a direct trace by Lemma 2.2.  Since all neighbours of the
deficient bag lie in the four universal bags and its neighbourhood is an
actual separator, the four unit bounds and seven-connectivity give at least
three unsupported neighbours exactly as stated.

The hybrid support corollary is also valid.  The earlier centre-star theorem
supplies traces on its response-support set, while Lemma 2.2 supplies them
on `V(M)`.  The same selected-portal rerun and count apply to their union.

## 4. Trust boundary

No proof gap or hidden finite assumption was found.  The result does not
establish any of the following stronger statements:

- the removable matching has one end at each exceptional centre;
- `chi(G/J)=6` for matching sets `J` of order greater than one;
- one common `K_6` model co-bags all five matching pairs;
- the returned separator has order seven or a compatible interior boundary
  partition; or
- the support-sparse exact model is impossible.

The terminalization target in Section 5 remains open.  Consequently this
reduction proves neither the `K_7^-` six-colour conjecture nor `HC_7`.
