# Internal audit: generalized-wheel leaf descent

**Verdict:** **GREEN** for the exact revision below.

**Audited source:**
[`hc7_k7minus_four_centre_wheel_leaf_descent.md`](hc7_k7minus_four_centre_wheel_leaf_descent.md)

**Audited source SHA-256:**

```text
c04236752495ec7ff6e57b54cc498423be1b621c5ba3547739cec72b045db176
```

**Originally audited source SHA-256:**

```text
3ea68eff59f8cc2d3f08f15c8b076cde012609862117491cd642c4e55d31421b
```

**Previous promoted source SHA-256:**

```text
8d61c7a9dac744c151b44cb1e15822a1ea75f603e86a21952940ef9546405263
```

The previous promoted source differs from the originally audited source only
by changing the opening audit status from
`pending` to `GREEN` and replacing the undefined phrase `final thin-leaf
case` with the equivalent explicit description `when the selected component
is one leaf and both component packing numbers are one`.  Reversing exactly
those two edits reproduces the originally audited hash shown above.  Neither
edit changes a hypothesis, conclusion or proof step, so the GREEN verdict
applies to both revisions.

The current source differs from the previous promoted source only in three
terminology edits.  The Corollary 2.2 heading, its final proof paragraph and
the closing scope sentence replace the project-specific language of
full-subgraph packing numbers by the exact standard-language conclusion:
neither component contains two vertex-disjoint connected subgraphs that are
each adjacent to every boundary vertex.

This replacement is logically equivalent in the present setting.  The
operation-cut note defines `nu_X` as the maximum number of pairwise
vertex-disjoint connected subgraphs of `G[X]` adjacent to every vertex of
`S=U dotcup T`.  Each of `C,D` is connected and has neighbourhood exactly
`S`, so the component itself is one such subgraph.  Consequently `nu_X=1`
if and only if `X` contains no two such subgraphs.  The pinned operation-cut
Theorem 4.1 leaves, up to exchanging `C,D`, only `(nu_C,nu_D)=(1,1)` or
`(1,2)`, and the latter forces `T` to be independent.  Corollary 2.2 has
already excluded that case.  Thus the three edits change neither the
corollary's conclusion nor any proof step, and the GREEN verdict applies to
the current hash.

This is a separate internal mathematical audit, not external peer review.
The proof was checked against the published Carmesin--Kurkofka paper and
the exact local dependencies listed below.  No unresolved inference was
found within the theorem's stated scope.

## Apex decomposition and the degree-three witness

The proof of Carmesin--Kurkofka Theorem 2.2.8(ii) starts from the heavily
interlacing tri-separation `q`, chooses a crossing strong nontrivial
tri-separation, and applies Lemma 1.8.5.  The resulting 2-connected apex
decomposition has centre `v`, central torso-cycle `O`, and tri-star equal
to the given splitting star `sigma` by Lemmas 2.5.10 and 2.2.5.  The
Crossing Lemma and Lemma 2.5.5 put `v` in the separator of `q` and put its
other two separator elements on the rim.  Lemma 2.5.11 identifies the
expanded torso `W` as a concrete generalized wheel.

Every non-centre vertex of a concrete generalized wheel is either a rim
vertex or an added degree-three vertex.  A rim vertex of degree greater
than three is incident with an added degree-three vertex.  If
`w in C cap V(W)` has degree three, the proof takes `z=w`; otherwise it
takes such an added vertex.  In the latter case, the associated bold rim
edge belongs to one leaf of the apex decomposition.  Since `q` interlaces
the tri-star and `w` is in its selected open side, that leaf, and hence
`z`, is on the same side.  The added vertex is not a rim vertex, while the
members of `T_D` are rim endpoints of separator-edge elements of `q`.
Thus in both cases

```text
z in C cap V(W)  and  d_W(z)=3.
```

The expanded torso contains every original edge induced by its vertex
set, possibly together with added torso edges.  Hence `H[V(W)]` is a
subgraph of `W`.  Since `delta(H)>=4`, the vertex `z` has an actual
neighbour outside `V(W)`.

All three vertices of `T` lie in `V(W)`.  A member not reduced from the
`D`-side is a vertex element of the separator of `q`, hence is `v` or a
rim vertex.  A member of

```text
T_D={t in T : d_{H[D union T]}(t)=1}
```

is an endpoint of one of the two rim-edge elements of that separator.
The outside neighbour of `z` therefore lies neither in `T` nor in `D`,
which is anticomplete to `C`; it lies in `C` as claimed.

## Leaf conversion and strict trace preservation

By the expanded-torso construction in Carmesin--Kurkofka Section 2.2.3,
every vertex outside `V(W)` belongs to the open side of a unique leaf
separation.  For each edge element of that mixed separator, choosing its
leaf-side endpoint as a boundary vertex produces an ordinary
three-separation: separator edges form a matching, every old crossing edge
then meets the new boundary, and the boundary still has order three.  The
chosen endpoints and the original vertex elements all belong to `V(W)`,
so the converted open leaf side is disjoint from `V(W)`.

Interlacing orients the leaf below the selected side of `q`.  Its converted
open side `L` is therefore contained in `C dotcup T_D`; disjointness from
`V(W)` removes `T_D`, so `L subseteq C`.  It contains the outside neighbour
of `z`, while `z` itself lies in `C cap V(W)`, making the containment
nonempty and strict.

The converted separation has `x_j` in its opposite open side.  The audited
four-centre lift theorem makes all four vertices of `U` cross it, so it
lifts to an exact order-seven cut.  The audited two-component theorem makes
`L` connected.  Its selected closed side is contained in `C union T`, so
the accepted colouring restricts unchanged and colour `gamma` remains
available at `r`.  The ordered roots and named bichromatic component are
global data in the unchanged graph.  Thus the new cut is trace-admissible
and contradicts minimum choice whenever `C` meets `V(W)`.

## The single-leaf conclusion and disjoint-subgraph corollary

Once `C cap V(W)` is empty, distinct open leaf sides are disjoint and have
no edge between them outside `V(W)`: such an edge would itself be a mixed
separator edge and would put its endpoints in the expanded torso.  The
connected set `C` consequently lies in one leaf.  Interlacing puts that
leaf below the selected side of `q`, and every selected-side vertex outside
`V(W)` belongs to `C`; hence its converted open side is exactly `C`.
The converted boundary has order three and contains `N_H(C)=T`, so it is
exactly `T`, and the resulting ordinary separation is precisely
`(C union T,D union T)` with the stated orientation.

Corollary 2.2 is also correct.  If `T` were independent, each leaf-side
endpoint chosen for an edge element would have at least two neighbours in
`C` by trace minimality, exactly one neighbour in `D` by the matching
property, and no neighbour in `T`.  Carmesin--Kurkofka reduction would
therefore restore that separator edge.  Vertex elements of the original
tri-separation already have two neighbours on both closed sides and remain
vertices.  The deterministic reduction of the recovered ordinary
separation would be the leaf separation `s`.  It is also `q`, which is
impossible because `q` interlaces `sigma` while a member `s of sigma` does
not.  Thus `H[T]` has an edge.

The exact seven-cut capacity theorem leaves, up to orientation, either no
component containing two vertex-disjoint connected subgraphs adjacent to
the whole boundary or exactly one component containing two.  The audited
operation-cut Theorem 4.1 uses only the exact cut, the independent four-set
`U`, and the adaptive independent-block closure; it therefore applies to
this minimum trace-admissible cut.  The second alternative makes `T`
independent, now excluded.  Consequently neither component contains two
such subgraphs.

There is no stronger contradiction from the equality of the converted
ordinary separation with the original cut.  Without independence of `T`,
a chosen leaf-side endpoint may have a second neighbour in the opposite
closed side through another boundary vertex.  It then remains a vertex
under reduction instead of restoring the mixed separator edge.  This is
the same phenomenon behind Carmesin--Kurkofka Remark 1.8.4.  The surviving
case is therefore genuinely a single canonical leaf with an edge in `H[T]`,
and neither component contains two vertex-disjoint connected subgraphs
adjacent to every boundary vertex.  It remains open to use the critical-host
colouring data to construct the prescribed rooted minor or another strict
trace-preserving cut.

## Pinned local dependencies

```text
trace-preserving four-centre descent
f3bc2374c410631a39a98a63f05db8eab52a7271f58be70bb313241c7f8a7e71

canonical tri-separation reduction
b5b0ff71e8942d4b16674a25362c9459523c4c7460f15176892d4ded8a82b682

operation-coupled four-centre reduction
4d4ca474cb9d9f28632077f0a89d79c0fc36840f3eb2600c745e0ea2150f2f98

two-component normal form for seven-vertex cuts
1041988a33b749bef5802dd21d3cd9419b5afc754735a20174bf5a13c0a56c96
```

The primary external source checked was Johannes Carmesin and Jan
Kurkofka, *Canonical Decompositions of 3-Connected Graphs*, Advances in
Combinatorics 2025:7, <https://doi.org/10.19086/aic.2025.7>, especially
Lemma 1.8.5, Section 2.2.3, Lemma 2.5.5, Lemma 2.5.11, Remark 1.8.4 and
Theorem 2.2.8(ii).
