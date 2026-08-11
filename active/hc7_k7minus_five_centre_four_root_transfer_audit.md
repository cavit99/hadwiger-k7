# Internal audit of the four-root palette transfer

Audited file:
`active/hc7_k7minus_five_centre_four_root_transfer.md`

Audited SHA-256:

```text
06c60e0a56ded0a1fc273149a76e51cff1e22c0f956a016e91bcd1056d86f647
```

**Verdict:** **GREEN** for the stated theorems and exact scope of this
revision.

This is a hash-pinned internal mathematical audit, not external peer review.
Relative to the theorem revision originally checked, the source changes
only its audit-status metadata; no theorem or proof text changed, so the
GREEN verdict is retained.  Its theorems eliminate only the
specified rows of the five-centre two-cut analysis.

## 1. Standing hypotheses

The audit checked that every use of contraction colourability follows from
the explicit assumption that every proper minor of `G` is six-colourable.
Both contractions delete vertices of a nonempty shore and are therefore
proper.  The two full components `C,D`, the independence of `Z`, the absent
edge `pq`, and the two permitted response colourings are all stated before
they are used.

The degree identity

\[
                         c_z+d_z+\rho_z=8
\]

is exact because the five centres are independent and `C,D` are the only
components outside `S=Z\mathbin{\dot\cup}\{p,q\}`.

## 2. Equal-response transfer

For `A=Z-\{z\}`, feasibility is defined in the graph
`G[C\cup A\cup\{p,q\}]`.  Thus the omitted centre `z` is not a vertex of
the witness path `P`; this is essential when `z` is retained after the
contractions.

Let `K` be the component after deleting `P` that contains `A`.  If `z` had
a neighbour in `K`, adjoining the literal vertex `z` to `K` would put all
five roots in one component after deleting the same path, contradicting
five-root infeasibility.  Hence every `C`-neighbour of `z` lies on `P` or
in another component of the graph minus `P`.

The union `W` of `P` with every such component containing a `z`-neighbour
is connected: each component of the connected rooted graph minus `P` has
a neighbour on `P`.  The sets `K,W` are disjoint, connected and adjacent;
`W` contains both poles and a `z`-neighbour.  Contracting them therefore
forces different colours on their images and forces `z` to avoid the pole
image's colour.

On pullback, the vertices of `A` are expanded from the `K`-image and
`p,q` from the `W`-image.  These expansions are proper because `A` is
independent and `pq` is absent.  Every edge from an expanded boundary
vertex to `D` is represented by an edge incident with the appropriate
contraction image.  The retained vertex `z` and all its `D`-edges are
literal.  This proves all three asserted colour conditions.

No centre--pole edge at `z` is used.  The fact that `C` is full at `z`
ensures that `W` contains a neighbour of `z`.

## 3. Distinct-response transfer

Again the omitted centre `z` is absent from the feasible rooted graph and
hence from `P,K`.  A component `R` of `K\cap D` exists because four
independent roots cannot form a connected subgraph after the pole path is
deleted without using a vertex of `D`.

No vertex of `C` is adjacent to `R`, and no different component of `D-P`
is adjacent to `R`.  Therefore

\[
                         N_G(R)\subseteq Z\cup V(P).
\]

This neighbourhood separates nonempty `R` from nonempty `C`.  Since at
most five of its vertices lie in `Z`, seven-connectivity gives at least two
distinct contacts on `P`.  Splitting `P` across an edge between two
ordered contacts makes the `p`-subpath, the `q`-subpath, and `K` pairwise
adjacent.  Their three contraction images form a triangle and so receive
three distinct colours.

Expanding `A,p,q` is proper for the same independence reasons as above,
and every edge from an expanded vertex to the untouched `C`-side is
represented.  The retained omitted centre causes no pullback issue.

## 4. Palette arguments

In Theorem 3.1 the two shore colourings agree on the literal boundary
`A\cup\{p,q\}` after a colour permutation.  The only edges between the two
open sides are the `c_z` edges from `z` to `C`.  Their `C`-ends avoid the
root colour `alpha`.  The transferred colour of `z` avoids the pole colour
`beta`.  If it is not `alpha`, it is one of exactly four freely permutable
colours.  With `c_z\le3`, one of those four colours is absent from
`N_C(z)`, which proves the gluing step.

For Corollary 3.2, `N_C(z)` and `N_D(z)` are anticomplete.  A `K_4`-free
set of order at least four is not a clique, so its independence number is
at least two.  Since the full exceptional neighbourhood has independence
number three, `N_D(z)` has independence number one and is a clique; its
order is at most three by `K_4`-freeness.

In Theorem 4.1, adjacency from `z` to both poles forces the transferred
colour of `z` to avoid both fixed pole colours.  Its `D`-neighbours avoid
the root colour in the fixed distinct-response colouring.  Unless `z`
already has the root colour, it uses one of exactly three freely permutable
colours.  At most two `D`-contacts cannot occupy all three, so the two
colourings glue.  Corollary 4.2 is then the exhaustive split
`c_z+d_z=6` when `rho_z=2`.

## 5. Scope and unresolved cases

The audit found no inference that eliminates a minimal infeasible root set
of order four.  Nor does Theorem 3.1 eliminate the order-five row once all
`c_z\ge4`, or Theorem 4.1 eliminate the three-contact palette obstruction.
Section 5 states these limitations accurately.

The proof does not establish that the distinct-side four-root witness can
be chosen with overlapping attachment intervals, synchronize different
transferred colourings, or construct a `K_7^-` model in the remaining
rows.  No such conclusion should be cited from this note.
