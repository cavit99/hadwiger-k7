# Separate internal audit: eight-coordinate endpoint visibility

**Verdict:** **GREEN.**  Lemma 2.1, the endpoint-visibility transfer,
preservation of exactness, strict increase of the visibility score, the
maximum-model argument, and the numerical boundary compression are correct
at the revision below.  The resulting order-seven, order-eight or
order-nine response interface is not terminal.

This is a separate internal mathematical audit, not external peer review.

## Exact revision

The audited source is
[`hc7_k7minus_eight_coordinate_endpoint_visibility.md`](hc7_k7minus_eight_coordinate_endpoint_visibility.md),
with SHA-256

```text
8ad949ac4d3cb831e9cffa26115f955e98feaca9cef4a238d240eaa113e4f11d
```

The promoted source differs from the initially audited revision
`a8209ea878d3ff7b52c41153f56d3aa7f4df839a1795134fce69858a26b9619b`
only in its status paragraph and audit link.  Its mathematical content is
unchanged.

## 1. Singleton-coordinate traces

Fix an endpoint in a nonempty proper set `Y` and its incident coordinate
edge `e`.  A signature-`{e}` colouring of `G-F_8` has `e` as its only
monochromatic edge after all eight coordinates are restored.  Deleting
`Y` removes one end of `e`, so its restriction properly colours `G-Y`.
An intact extension inducing the same boundary partition would align by a
permutation of the six colour names and glue to a six-colouring of `G`.
This verifies Lemma 2.1.  It does not assert that traces supplied by
different coordinates are distinct.

## 2. The endpoint transfer

Let `v` be an endpoint in a universal bag `U`, not adjacent to the
deficient bag `P`, and choose a `P`-neighbour `q` in `U`.  A fixed
`q`--`v` path extends to a spanning tree of `G[U]`.  Deleting the edge
`xv` of that path incident with `v` gives connected nonempty sets

```text
A containing q and x,     W containing v.
```

If `W` has lost a foreign adjacency, it is anticomplete to the
corresponding nonempty foreign branch set.  Thus `N_G(W)` is an actual
separator; seven-connectivity supplies its lower bound and Lemma 2.1
attaches the original coordinate response.

Otherwise `W` retains all five foreign adjacencies.  Replacing

```text
P,U  by  P union A,W
```

preserves connectedness: a `P`--`q` edge connects the enlarged deficient
bag, while `xv` connects the two new bags.  The other three universal
adjacencies of `P` survive through the old subset `P`, and every adjacency
among the six foreign bags survives because `W` retains its five.

If `A` meets either deficient twin `B` or `C`, the seven new bags miss at
most the other deficient adjacency and form an explicit `K_7^-` model.  If
it meets neither twin, both `P` and `A` are anticomplete to `B,C` in the
literal graph `G`.  The transferred spanning model is therefore still
exact after restoration of `F_8`, rather than merely being a model in the
deletion host.

If `A` contains a coordinate endpoint, the enlarged deficient bag itself
has an actual boundary with a coordinate trace.  In the remaining case
`A` contains no coordinate endpoint.  No endpoint already counted by

\[
             s(P)=|(P\cup N_G(P))\cap V(F_8)|
\]

is lost: endpoints in `P` remain in the enlarged bag, and exterior
endpoints adjacent to `P` remain adjacent to the subset `P`.  The endpoint
`v` was not previously counted but becomes adjacent to the enlarged bag
through `xv`.  Hence the score increases strictly.  This verifies every
outcome of Theorem 3.1 and explains why counting only exterior portals
would not be monotone.

## 3. Capture and the maximum-model argument

The exact-`K_7^vee` separator dichotomy may be rerun with any two nominated
`P`-neighbours in one universal bag.  In its retaining-core outcome the
returned component contains the avoided nominated vertex; in its opposite-
gate outcome the two gates contain the nominated vertices separately.
Thus every separator returned by this labelled rerun contains a coordinate
endpoint, while its alternative is the explicit target model.  Lemma 2.1
then attaches the coordinate trace.  This verifies Theorem 4.1.

Choose an exact spanning model maximising `s(P)`.  A coordinate endpoint
in `P`, `B` or `C` immediately gives an actual response separator, using
one of the two anticomplete deficient bags as a far side.  Otherwise every
endpoint lies in a universal bag.  Theorem 3.1 and maximality force each of
those endpoints to be adjacent to `P`, unless the target or a response
separator has already occurred.

The eight-edge forest has sixteen distinct endpoints in the matching case
and fifteen in the induced-`P_3` case.  Four universal bags therefore put
two endpoint portals in one bag.  Theorem 4.1 completes the disjunction in
Theorem 5.1.  The argument is finite only in its maximisation of a bounded
integer score; it imposes no bound on the order of the returned separator.

## 4. Numerical boundary compression

If the original-coordinate response boundary from Theorem 5.1 has order at
most nine, it already proves Corollary 5.2 with all coordinate provenance
retained.  If its order is at least ten, the audited large actual-boundary
singleton descent applies in this seven-connected critical host.  Each
application returns an actual singleton-side response with strictly smaller
boundary order.  Iteration therefore terminates at order seven, eight or
nine.

The source records the price exactly.  After the first descent, the
operation may be a fresh edge deletion at an unrelated singleton.  The
bounded response need not retain the selected member of `F_8`, the forest,
the exact-model labels or the original boundary partition.  Corollary 5.2
does not claim order at most eight or a label-preserving recursion.

## 5. Exact remaining obstruction

The theorem terminalises neither the original-coordinate separator nor the
bounded response.  A rejected one-sided trace does not supply an intact
extension with the same partition from the other side.  At order nine it is
also not an exact order-seven/eight descent.  The remaining alternatives
are therefore genuinely:

1. terminalise a generic order-seven, order-eight or order-nine response
   interface; or
2. compress the original-coordinate separator while retaining enough of
   its operation and model labels to obtain a colouring, the target minor,
   or a strict labelled descent.

Neither spanningness of the exact model nor the punctured signature cube
bounds the number of literal neighbours of a returned connected set.

## Dependencies and trust boundary

The proof uses the audited forced eight-coordinate host, the audited exact
`K_7^vee` separator dichotomy, and the audited large-boundary singleton
descent.  Their relevant current source hashes are

```text
c49b8b736475c9a71410fb9e4a79dad0de862ed6304d2e71b472a07b791c7422  results/hc7_k7minus_six_coordinate_growth_or_feedback.md
15c765ab83c396410fab88c57d855f7a594c99f26f7b462a7461bc028fc368f1  results/hc7_k7minus_bounded_feedback_degree_elimination.md
4845f5375581971aca7397bbac0e3eb930dd2943c9dca71f6264a24e2fa31c6e  results/hc7_k7minus_exact_k7vee_separator_dichotomy.md
d95c459737f7d94e8c212e8f3d90e2b5fbf762f46567d70e6e6d9dfb386dd244  results/hc7_k7minus_matching_lock_boundary_reduction.md
```

The result is unbounded and computation-free.  It closes the endpoint-to-
portal placement problem by forcing an original-coordinate separator, but
does not prove the eight-coordinate branch, the six-coordinate
terminalisation theorem, Conjecture 21 or `HC_7`.
