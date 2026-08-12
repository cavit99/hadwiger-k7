# Separate internal audit: fixed-coordinate response core reduction

**Verdict:** **GREEN.**  Lemma 2.1, Theorem 3.1 and Corollary 3.2 are
correct at the pinned revision.  In particular, passing to a critical core
preserves an actual separation and makes the newly induced boundary lists
smaller, not larger.  Section 4 records the resulting route nonclosure
accurately and does not claim boundary compression.

This is a separate internal mathematical audit, not external peer review.

## Exact revision

The mathematical source audited was
[`hc7_k7minus_fixed_coordinate_response_core_reduction.md`](hc7_k7minus_fixed_coordinate_response_core_reduction.md),
with SHA-256

```text
fcd24078aa939f40d02f661c3e1cccf2e28d34f6e42672b83b1dab53590b0dbd
```

After this audit, its status line alone was updated to link this audit.  The
current source SHA-256 is

```text
0473dc5826585e87935d3acf04c9c9579f8ecf52d92f076a9a44e7907c8b2da1
```

No mathematical statement or proof text changed.

The proof is computation-free.  Its positive statements use only that `G`
is not six-colourable, that `c` is a proper six-colouring of `G-e`, and that
the chosen connected side meets an end of `e`.  Seven-connectivity is used
only for the lower bound on the order of an actual separator.

## 1. Inheritance and actuality

Let `R=V(G)-N_G[Y]`.  Since `R` is nonempty and anticomplete to `Y`, every
nonempty `K subseteq Y` is disjoint and anticomplete to `R`.  Consequently
`R` is disjoint from `K union N_G(K)`, so deleting `N_G(K)` leaves the two
nonempty sets `K` and `R` separated.  Thus the actual-separator assertion in
Lemma 2.1 survives passage to every connected rooted subset; no fullness or
minimality hypothesis is being used implicitly.

The colouring `c` can fail on `G` only at `e=uv`, because it is proper on
`G-e`, and its ends have the same colour.  Removing a set meeting `{u,v}`
therefore makes its exterior restriction proper.  If the induced boundary
equality partition extended through the closed `K`-side, a permutation of
the at most six colour names would make that extension agree with `c` on
the boundary.  Gluing would then six-colour `G`.  This proves the rejected
trace exactly as stated.  If `G` is seven-connected, the actual separator
has order at least seven.

## 2. The list-critical core

An `L_Y`-colouring of `G[Y]` would combine directly with `c|G-Y`, since
each list omits every colour used by an exterior boundary neighbour.  It
would therefore six-colour `G`, proving that the list obstruction exists.
A vertex-minimal non-list-colourable induced subgraph is connected: if it
had two or more components, minimality would colour every component and
their colourings would combine.

The endpoint-retention argument is also exact.

- If only `u` lies in `Y`, then `v` lies in the boundary.  Apart from the
  incidence `uv`, every internal or boundary edge is proper under `c`.
  Hence `c` list-colours every induced subgraph of `G[Y-u]`, forcing the
  obstruction to contain `u`.
- If both ends lie in `Y`, all boundary incidences are proper under `c`,
  and omitting either end removes the sole potentially improper internal
  edge.  Thus the obstruction contains both ends.

The connected critical core consequently satisfies every hypothesis of
Lemma 2.1 and retains the same edge, exterior colouring and rejected
boundary partition.

## 3. Direction of the list comparison in Corollary 3.2

This is the delicate point, and the direction in the source is correct.
For a chosen core `K subseteq Y` and a vertex `x in K`, every old boundary
neighbour of `x` remains a new boundary neighbour:

\[
 N_G(x)\cap N_G(Y)\ \subseteq\ N_G(x)\cap N_G(K).
\]

The new boundary can additionally contain neighbours of `x` in `Y-K`.
It therefore displays a superset of the old boundary colours, and hence

\[
 L_K(x)=[6]-c(N_G(x)\cap N_G(K))
       \ \subseteq\
       [6]-c(N_G(x)\cap N_G(Y))=L_Y(x).
\]

Since `G[K]` is not colourable from `L_Y|K`, it is certainly not colourable
from the smaller lists `L_K`.  The construction can therefore be repeated
on the new actual side.  The appropriate end or ends of `e` remain in every
iterate, and every proper replacement strictly decreases the positive
integer side order.  At termination the whole current side is
vertex-minimal noncolourable from its own newly induced boundary lists,
which proves Corollary 3.2.

## 4. Exact scope and nonclosure

For `K subsetneq Y`, every neighbour of `K` outside `Y` lies in the old
boundary, while neighbours in `Y-K` form the possible new contribution.
Thus the disjoint decomposition in (4.1) is exhaustive.  It gives no upper
bound on `|N_G(K)|`; the side-order descent is not a boundary-order descent.

The cited rooted-compression barrier indeed permits a singleton response
side with unbounded boundary, while containing the forbidden target.  The
generic large-boundary reduction may choose a fresh endpoint and colouring,
so it does not repair this fixed-coordinate quantifier mismatch.  These are
properly stated as limitations of the mechanism, not as counterexamples to
a target-free host theorem.

There are no unresolved assumptions in the proved inheritance or
side-reduction statements.  The source does **not** prove an order-seven or
order-eight boundary retaining the coordinate, a compatible shore
partition, the eight-coordinate terminalisation theorem, or the
`K_7^-` six-colour conjecture.
