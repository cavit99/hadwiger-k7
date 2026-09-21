# Internal audit: a rooted dart from nonroot minimum degree five

**Verdict: GREEN.** This is a separate internal mathematical audit, not
external peer review. The result is unbounded and uses no finite census.

Audited [source](rooted_dart_nonroot_degree_five.md), SHA-256:

```text
37dcf256f64fca7c49a1bd4ec66021371fba9a7863bf9523597ba4b898ecfad2
```

The mathematical body is unchanged from the separately inspected draft
at SHA-256
`e793ecb1aba7957296dafc8de9e5a564a269d14d8386b61c896604731326220b`.
Only the promotion status and its line wrapping changed.

## Exact external dependency

The terminal construction in Dvořák--Norin--Rahman,
[arXiv:2609.17760v1, proof of Lemma 3.1](https://arxiv.org/html/2609.17760v1#S3),
was inspected directly. After the case of a separator consisting of the
two branching vertices, it uses a tree with exactly the four prescribed
leaves and a shortest path between its branching vertices. The absence
of the indicated two-versus-two root separation supplies its two cross
paths. Minimum length of the branching path gives the disjointness used
in its final five bags. No density or induction hypothesis is used in
that terminal construction.

The present proof imports precisely that construction under the same
tree and path hypotheses. It does not apply the positive-density
statement of Lemma 3.1 to a graph without positive density. This external
construction, and Menger's theorem, remain accepted inputs; this audit
does not claim an independent proof of the entire external paper.

## Induction hypotheses and terminal case

Deleting root--root edges preserves all nonroot degrees and boundaries.
If a partition of the roots into pairs lacked two disjoint paths, a
separator of order at most one would put each remaining nonroot on a
side whose boundary has order at most three. Internal four-connectivity
would leave at most the separator vertex as a nonroot, contradicting
the explicit assumption of at least two nonroots. This establishes the
linkage needed later even when the small separator contains a root.

Each nonroot component is adjacent to all four roots. Taking a tree in
one such component and one attachment to each root gives a tree whose
leaves are exactly the prescribed roots. Its branching vertices are
nonroots, and choosing a shortest branching path is legitimate in a
finite graph. If the specified two-vertex separation is absent, a failed
cross path would partition components after deleting those vertices
into exactly that separation. Thus the external terminal construction
applies. The coincident-branching-vertex case is covered by the preceding
one-vertex-separator exclusion.

## Smaller side and lift

In the remaining two-vertex separation, each induced side has two old
roots and both branching vertices as its four prescribed roots. If
neither side has another vertex, there are exactly two nonroots in the
six-vertex graph; degree five makes both universal. The displayed
absorption of one into a root bag gives a root star containing the
required three-vertex path, while the other is a full helper.

Otherwise a nonempty side interior has at least two vertices: a singleton
could only see its four boundary vertices. Every interior vertex keeps
all its neighbours and degree at least five. Every subset of that
interior also keeps its full external neighbourhood, proving the exact
rooted-connectivity hypothesis for the side. The side omits the two
opposite original roots, so its order decreases by at least two. The
induction class and decreasing parameter are therefore valid.

The two disjoint original root-pair paths cross the separator at distinct
vertices. Their segments after the last separator visits lie entirely
outside the chosen side except for their initial vertices. Appending
these segments to the corresponding two root bags preserves connectivity,
all contacts and disjointness from the helper and other root bags. The
opposite original roots become the roots of these enlarged bags; the
two roots already in the side stay in their original bags. Thus the
inductive dart lifts with all four prescribed roots retained.

No unresolved inference was found in the stated degree-five theorem.
The assumption of at least two nonroots and the nonroot degree bound
are used explicitly. The degree-four variant, the stronger helper
theorem, C21 and HC7 are not certified by this audit.
