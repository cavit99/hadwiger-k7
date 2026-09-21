# A rooted dart from nonroot minimum degree five

**Status:** written proof with a separate hash-pinned internal audit,
using an explicitly identified construction from an external proof. This
is a local structural lemma, not Conjecture 21, HC7, or a result claimed
comparable in significance to Norin–Totschnig. No finite search result is used.

All graphs are finite and simple. For a graph `F` and four-set `Z`, internal
four-connectivity means that every nonempty `W subseteq V(F)-Z` has at least
four external neighbours. This is equivalent to the absence of a proper
root separation of order at most three, since `|Z|=4`.

A **Z-rooted dart** has four disjoint connected bags containing the four
individual roots, and a fifth disjoint nonempty connected bag adjacent to
all four. Among the root bags, two contacts form a three-vertex path; the
remaining root is isolated in the target. Additional contacts may be
deleted. The choice of the three roots and their order is unrestricted.

## Exact external construction

We use the final construction in the proof of Dvořák–Norin–Rahman,
[Lemma 3.1, arXiv:2609.17760v1](https://arxiv.org/html/2609.17760v1#S3),
with the following precise hypotheses. Its primary proof was inspected
on 21 September 2026.

Let the four roots be independent. Suppose there is a tree `T` whose
leaves are exactly the roots. Its branching vertices are either two
vertices `v1,v2` of degree three or one vertex `v1=v2` of degree four.
Let `P` be their joining path, trivial in the latter case. Choose `T`
so that `|E(P)|` is minimum among all such trees. If `F-{v1,v2}` contains
a path joining the parts of every partition of the roots into two pairs,
then `F` contains a rooted dart.

This is the terminal part of the cited proof, after its two-separator
case. The two auxiliary paths there avoid `P` by the minimum-spine choice.
Their interiors are allocated to one root bag, giving two root contacts;
`P` is the helper and the four root branches supply its four contacts.
No density, degree or induction hypothesis is used in that construction.
We import this construction, not the positive-density statement of
Lemma 3.1 under different hypotheses.

## Degree-five lemma

**Theorem.** Let `(F,Z)` be internally four-connected, with `|Z|=4` and
`|V(F)-Z|>=2`. If every vertex outside `Z` has degree at least five in
`F`, then `F` has a `Z`-rooted dart.

**Proof.** We induct on `|V(F)|`. Delete all edges between roots; this
changes neither nonroot degrees nor the external neighbourhood of any
root-free set. A model in the resulting graph is also a model in `F`,
so assume the roots are independent.

First, every partition `Z=Z1 dotcup Z2` into two pairs has two
vertex-disjoint `Z1`–`Z2` paths. Otherwise Menger's theorem gives a
separation `(B1,B2)` of order at most one with `Zi subseteq Bi`.
Put `K=B1 intersect B2` and

```text
Wi = Bi - (Zi union K).
```

Each `Wi` is root-free, and its external neighbours belong to `Zi union K`,
which has at most three vertices. Internal four-connectivity forces both
`Wi` to be empty. Consequently every nonroot lies in `K`, contradicting
that there are at least two nonroots. This also rules out a separation
with separator `{v}` and two roots in each open side, for any nonroot `v`.

Every component of `F-Z` is adjacent to all four roots: its boundary
is a subset of `Z` and has order at least four. A tree inside any such
component, with one attachment to each root, contains a subtree whose
leaves are exactly `Z`. We may therefore choose a minimum-spine tree
`T` as in the external construction, with spine ends `v1,v2` outside `Z`.

If there is no separation `(B1,B2)` with separator exactly `{v1,v2}`
and two roots in each open side, the external construction applies.
Indeed, a failed path connection in `F-{v1,v2}` for a two-pair partition
would partition its components into such a separation. This also covers
`v1=v2`; in that case the separation was already excluded above.

It remains that `v1!=v2` and such a separation exists. Set

```text
K={v1,v2},  Zi=(Z intersect Bi) union K,
Fi=F[Bi],  Wi=Bi-Zi.
```

Here `|Zi|=4`, consisting of two original roots and the two spine ends.
If both `Wi` are empty, the only nonroots of `F` are `v1,v2`.
Their degrees are at least five in this six-vertex graph, so they are
adjacent to each other and to all four roots. Keep `{v1}` as helper,
absorb `v2` into any one root bag and keep the other roots singleton.
The root bags then have a three-edge star, which contains the required
three-vertex path, and the helper contacts all four. This is a dart.

Otherwise choose `i` with `Wi` nonempty. In fact `|Wi|>=2`: if `Wi={w}`,
then all neighbours of `w` belong to the four-set `Zi`, contradicting
its degree at least five.

The induction hypotheses hold for `(Fi,Zi)`. Every vertex of `Wi` keeps
all its neighbours because an edge cannot join the two open sides of a
separation. Thus its degree in `Fi` is still at least five. Likewise,
for every nonempty `Y subseteq Wi`,

```text
N_Fi(Y)=N_F(Y),
```

so this boundary has at least four vertices. This proves internal
four-connectivity. Finally `Bi` omits the two original roots on the
opposite open side, so `|V(Fi)|<=|V(F)|-2`. The induction genuinely
decreases order and supplies a `Zi`-rooted dart in `Fi`.

We now lift it without reusing a root or a helper vertex. The two disjoint
paths established above, between `Z intersect Bi` and the opposite pair
of original roots, must cross `K` at different vertices. On each path,
retain the segment after its **last** visit to `K`. These two segments
start at `v1,v2`, end at the two opposite original roots in some order,
and have all their remaining vertices outside `Bi`: a return to the
chosen open side would require another visit to `K`.

Append these segments to the two dart root bags containing `v1,v2`.
Each enlarged bag is connected. The segments are disjoint and avoid all
other local model bags, including the helper. The original two roots
in `Bi` remain in their own bags; the two opposite roots become the
prescribed roots of the enlarged bags. All model contacts are retained.
This is a `Z`-rooted dart in `F`, completing the induction. QED

## Scope

The only external mathematical input beyond Menger's theorem is the
explicitly isolated terminal construction above. No graph is assumed to
remain globally four-connected after passing to an induced side; the
required rooted connectivity is proved directly. The degree-four variant
is not asserted. Applying this lemma to a five-root minimal counterexample
requires a separate selection of the root separator and a proof that its
interior has at least two vertices.
