# Separate internal audit: operation-provenance exchange

**Verdict:** **GREEN.**  The operation-changing singleton normalisation,
the exact old-model persistence criterion, the two-edge signature
classification, the boundary localisation and gluing alternative, and the
disjoint-edge chromatic argument are correct at the pinned revision.  The
result records an exact operation/model quantifier mismatch and does not
terminalise the eight-coordinate branch.

This is a separate internal mathematical audit, not external peer review.

## Exact revision

The audited source is
[`hc7_k7minus_operation_provenance_exchange.md`](hc7_k7minus_operation_provenance_exchange.md),
with SHA-256

```text
d485f6735b11414170bd1eee9d3cb5a84b196e34c501078dd321b8f56f40bef8
```

An earlier cold audit checked mathematical revision

```text
6b6e42e40698b85255c780afc6f5ec9dc23c0ed1c6612292057fcd6ea6db5b14
```

After that cold audit, revision

```text
e503a9b67cf9bce40caf864fdfe66f874c397f943cf7e42efa2da4544cf8afb7
```

added the status link to this audit and explicitly clarified that the
unchanged exact model in Theorem 2.1 anchors the singleton in `G`;
persistence of that model after both edge deletions is the separate question
answered by Proposition 2.2.  The current revision additionally defines an
operation-changing model-anchored response side as the same geometry with
an arbitrary selected edge and its rejected edge-deletion response.  It
reserves explicit wording for claims which retain an `F_8` coordinate.
This removes a terminology ambiguity and changes no proof hypothesis or
conclusion checked below.

## 1. Singleton normalisation

If the starting side is not a singleton, choose a spanning tree of its
connected subgraph, rooted at an endpoint of an edge to the connected
branch-set complement.  Deleting a non-root leaf leaves that tree connected.
Together with a spanning tree of the complement and the root--complement
edge, this proves that the containing branch set remains connected after
the leaf is removed.  The singleton case is immediate.  Thus the selected
vertex `u` satisfies the geometric requirement `R-u` connected.

For any incident edge `uv`, minor-criticality gives a proper six-colouring
of `G-uv`.  Its ends must have equal colours, or it would colour `G` after
the edge was restored.  Removing `u` removes the sole possible improper
edge.  An intact extension inducing the same boundary partition would
align by a permutation of the six colour names and glue to a six-colouring
of `G`.  The named far branch set is anticomplete to `u`, so the boundary
is actual.  This proves the singleton response while retaining the same
geometric exact model in `G`.

The neighbourhood of `u` is not complete: minimum degree gives at least
eight neighbours, while four pairwise adjacent neighbours together with
`u` would form the excluded literal `K_5`.  Hence two nonadjacent neighbours
exist.  Their two incident edges form an induced path, so the audited
singleton two-edge theorem applies exactly as invoked.

## 2. Exact persistence of the original labels

Both deleted edges are incident with `u in R`.  No other branch set can
lose an internal edge, and no required inter-branch-set adjacency not
incident with `R` can be lost.  Since `R-u` remains connected, `Q[R]` is
connected precisely when at least one edge from `u` to `R-u` survives;
this is condition (2.3).  Each required `R`--foreign adjacency survives
precisely when an edge other than the two selected edges still witnesses
it; this is condition (2.4).

These conditions are independently necessary and jointly sufficient.
Deletion creates no optional adjacency, so exactness is preserved whenever
the model survives.  The separately obtained density model in the common
deletion carries no identification with the original labels.  Proposition
2.2 records that distinction correctly.

## 3. Exact signature languages

Let `e` be the fixed forest edge and `g` the appendage--core attachment
edge.  They are distinct because the appendage contains no forest endpoint.

- The singleton-signature colouring of `G-e` is proper on `g`, giving
  `EP`.
- A proper six-colouring of `G-g` makes the ends of `g` equal and is proper
  on the present edge `e`, giving `PE`.
- `PP` would remain proper after both edges were restored and is therefore
  impossible.

If the edges are disjoint, contracting both pairs and expanding gives
`EE`; no other edge collapses.  If they form an induced path, contracting
the whole path and expanding likewise gives `EE`; the absent outer chord is
essential here.  If the outer chord is present, equality on both incident
edges would give equal colours to its adjacent ends, so `EE` is impossible.
These observations prove exactly the three languages stated in Theorem
3.1.

The fresh-sixth-colour expansions correctly rule out five-colourings of
each single contraction, of the common deletion in the incident cases, and
of the induced-path contraction.  The source deliberately makes no such
claim for the double contraction of two disjoint edges, where one fresh
colour need not separate both pairs.

Deleting two edges lowers connectivity by at most two and leaves the
Norin--Totschnig density bound used in the cited singleton theorem.  The
small exceptional graph is excluded by the host order.  A spanning
`K_7^vee` model follows, and target exclusion makes both nominally missing
pairs genuinely anticomplete after restoration of the two edges.

## 4. Boundary localisation

An appendage contains no endpoint of `F_8`.  Therefore an `EP` or `EE`
colouring leaves the monochromatic forest edge wholly in `G-A`, whereas a
`PE` colouring becomes proper there because deleting `A` removes the
appendage end of `g`.  This verifies the precise exterior chamber in item
1 of Theorem 4.1.

The critical core `K` meets `e` and contains the core endpoint of `g`, so
it meets every monochromatic selected edge in every realised chamber.  The
same is true of `Z`.  Their exterior restrictions are proper and rejected
by the usual gluing argument.  The named far branch set makes both
boundaries actual.

On the closed `A`-side, `g` is present between `a in A` and `k in N(A)`,
so `PE` and `EE` are improper.  In an `EP` colouring, `g` is proper and
the sole possible improper edge is `e`.  Because neither end of `e` lies
in `A`, that edge belongs to the closed side exactly when both ends lie in
`N(A)`.  This proves (4.2).

When (4.2) holds, the `EP` closed-side and `PE` exterior languages are both
nonempty.  A common equality partition aligns by a permutation of colour
names and glues to a proper six-colouring of `G`.  In a non-six-colourable
host the two languages must therefore be disjoint.  The `EE` chamber is
improper on both relevant shores and cannot provide the gluing partition.

## 5. The disjoint-edge chromatic argument

Suppose the edges are disjoint, (4.2) holds, and the common deletion has a
five-colouring.  Its signature cannot be `EP` or `PE`: recolouring one end
of the sole equal pair with a fresh sixth colour would permit restoration
of both edges.  Hence its signature is `EE`.

If one endpoint of `e` were nonadjacent to one endpoint of `g`, recolouring
those two vertices with the same fresh sixth colour would separate both
equal pairs without creating a new monochromatic edge.  This would again
six-colour `G`.  Thus all four cross-edges are present.  In particular the
appendage endpoint of `g` is adjacent to both ends of `e`, putting both in
`N(A)` and contradicting (4.2).  Therefore the common deletion is exactly
six-chromatic in the second alternative.  In the triangle geometry, the
two ends of `e` are visibly adjacent to the appendage endpoint, so the
first alternative holds as stated.

## 6. Trust boundary

The source correctly withholds identification of the density model in the
common deletion with the original exact model.  It also withholds an
exchange between the forest-coordinate response on the disconnected-core
side and the fresh attachment-edge response on the appendage.  The proved
outcome is exactly the disjunction in (5.1), not a bounded labelled
separator or a common boundary partition.

There are no unresolved assumptions in the proved statements.  The note
does not prove operation-sensitive branch-set transfer, eight-coordinate
terminalisation, Conjecture 21 or `HC_7`.

## Dependencies checked

The direct local dependencies and their current source hashes are

```text
aefcb5164c4122bfb142b7cbbbc31f4d4154cb5c632fe454510e358a510843d8  results/hc7_k7minus_model_anchored_appendage_ownership.md
90c1a84a934ca2848c35152b3a0d0b089da55f308fa829f2add24addbcba8749  results/hc7_k7minus_singleton_coordinate_localisation.md
7cc1da7567f05e10bb7089c4b6dcd0706e9a0daa406063e7ba986d3d283c9512  results/hc7_k7minus_model_anchored_response_hull.md
8ad949ac4d3cb831e9cffa26115f955e98feaca9cef4a238d240eaa113e4f11d  results/hc7_k7minus_eight_coordinate_endpoint_visibility.md
```

Each has an adjacent GREEN internal audit.  This audit does not elevate
those internal checks to external peer review.

The first three paths were updated when those theorems were promoted from
`active/` to `results/`.  The response-hull audit records that its current
revision differs from the originally checked mathematical text only by its
status link.
