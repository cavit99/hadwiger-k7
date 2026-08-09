# Descent from the generalized-wheel branch

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_four_centre_wheel_leaf_descent_audit.md`](hc7_k7minus_four_centre_wheel_leaf_descent_audit.md).

This note treats the generalized-wheel outcome of the canonical
tri-separation theorem.  It gives a strict trace-preserving descent unless
the selected component lies wholly inside one leaf of the canonical
decomposition.  In that exception, expanding the leaf recovers the original
cut.

## 1. Setting

Use the setting and notation of the audited
[trace-preserving descent theorem](hc7_k7minus_four_centre_trace_descent.md).
Choose a trace-admissible cut

\[
 H-T=C\mathbin{\dot\cup}D,
 \qquad N_G(C)=N_G(D)=U\mathbin{\dot\cup}T             \tag{1.1}
\]

with `|C|` minimum.  Fix `x_j in D` and
`gamma=phi(x_j)`.  Every vertex of `T` has at least two neighbours in `C`.
Thus, if `q` is the Carmesin and Kurkofka reduction of

\[
                         (C\cup T,D\cup T),             \tag{1.2}
\]

then its selected side is literally `C union T`.  Its selected open side is

\[
                         C\mathbin{\dot\cup}T_D,        \tag{1.3}
\]

where `T_D` consists of the vertices reduced from the `D`-side, equivalently
`T_D={t in T:d_{H[D union T]}(t)=1}`.

Assume that `q` heavily interlaces the canonical splitting star `sigma`.
Let `W` be its expanded torso.  The Carmesin and Kurkofka torso theorem
says that `W` is a generalized wheel.

## 2. The minimum wheel-side cut

### Theorem 2.1 (the selected component is one canonical leaf)

The set `C` is disjoint from `V(W)` and is the open side of one leaf
separation of `sigma` after that mixed separation is converted to an
ordinary three-separation.  The resulting ordinary separation is (1.2),
so this expansion gives no descent.

#### Proof

The proof of the generalized-wheel outcome constructs a 2-connected apex
decomposition of `H`.  Its centre is a vertex `v`, its central torso is a
cycle `O`, and its tri-star is `sigma`.  The reduced separation `q` cuts
`O` at two rim elements and has `v` as its third separator element.  The
expanded torso is a concrete generalized wheel: besides `v` and the rim
vertices, it may have a degree-three vertex adjacent to `v` and to the two
ends of a rim edge.

Suppose for a contradiction that `C cap V(W)` is nonempty, and choose `w`
in this intersection.  The vertex `w` is not the centre `v`.  If
`d_W(w)=3`, put
`z=w`, so `z in C`.  Otherwise `w` is a rim vertex incident with one of the
added degree-three vertices; choose that vertex as `z`.  The
apex-decomposition places `z` in the same open side of `q` as `w`.  In this
case `z` is not a rim vertex and hence cannot be an endpoint in `T_D` of a
separator edge of `q`, so again `z in C`.  Consequently

\[
                         z\in C\cap V(W),
                         \qquad d_W(z)=3.              \tag{2.1}
\]

The graph `H[V(W)]` is a subgraph of `W`.  Since `delta(H)>=4`, the vertex
`z` has a neighbour `y` outside `V(W)`.  Every member of `T` lies in
`V(W)`: the unreduced vertices are separator vertices of `q`, while a
reduced member of `T_D` is an endpoint of a rim-edge element of its mixed
separator.  The components `C,D` are anticomplete, so `y in C`.

The vertex `y` lies in the open side of a unique leaf separation
`s in sigma`.  Convert `s` to an ordinary three-separation by choosing,
for every edge element of its mixed separator, the endpoint on the leaf
side as the new boundary vertex.  In the expanded-torso construction all
these chosen endpoints, and all vertex elements of the separator, belong to
`V(W)`.  The open leaf side `L` is therefore disjoint from `V(W)` and still
contains `y`.

The separation `q` interlaces `sigma`.  Since `y in C`, orient `s` below
the selected side of `q`.  Equations (1.3) and `L cap V(W)=emptyset` give

\[
                         \varnothing\ne L\subseteq C.  \tag{2.2}
\]

The vertex `z` belongs to `C-L`, so the inclusion is strict.  The converted
leaf separation is a proper ordinary three-separation of `H`.  Every member
of `U` crosses it, and it lifts to an exact cut with boundary
`U dotcup T'` for some three-set `T'`.  The two-component theorem makes
`L` connected.  Its opposite open side contains `x_j`, while its selected
closed side lies in `C union T`.  The fixed colouring therefore restricts
to the new selected side, and assigning colour `gamma` to `r` remains
proper.  The ordered vertices and named bichromatic component are
unchanged.  This contradicts the minimum choice of `C`.

It follows that `C cap V(W)` is empty.  The open leaf sides of `sigma`
are pairwise disjoint and anticomplete outside `V(W)`.  Since `C` is
connected, it lies in one such open leaf side.  Interlacing orients that
leaf below the selected side of `q`.  By (1.3), every selected-side vertex
outside `V(W)` belongs to `C`, so the open leaf side is exactly `C`.

Convert this leaf separation to an ordinary three-separation as above.
Its open side is `C`, and its boundary has order three.  But
`N_H(C)=T`, so its boundary is `T`; the ordinary separation is exactly
(1.2).  \(\square\)

The unresolved generalized-wheel case is therefore confined to one
canonical leaf whose open side is exactly `C`.

### Corollary 2.2 (boundary edge and disjoint connected subgraphs)

The graph `H[T]` has an edge.  Moreover, neither `C` nor `D` contains two
vertex-disjoint connected subgraphs that are each adjacent to every vertex
of `U dotcup T`.

#### Proof

Let `s in sigma` be the leaf tri-separation used at the end of the proof of
Theorem 2.1.  Suppose that `T` is independent.  In the conversion of `s` to
the ordinary separation (1.2), every edge element of the mixed separator is
replaced by its endpoint on the leaf side.  Each such endpoint lies in `T`
and has at least two neighbours in `C`, by the minimum choice of `C`.  It is
therefore not reduced from the selected side.  The separator edges of `s`
form a matching, so the chosen endpoint has just one neighbour in `D`.
Independence of `T` makes this its only neighbour in the opposite closed
side.  Reduction consequently restores the original separator edge.

Every vertex element of the separator of `s` already has at least two
neighbours on both sides, since `s` is a tri-separation.  It remains a vertex
element under reduction.  Thus reducing (1.2) returns `s`.  But its reduction
is `q`, so `q=s`.  This is impossible: `q` interlaces `sigma`, whereas
`s in sigma` does not interlace that star.  Hence `H[T]` has an edge.

The audited theorem on disjoint connected subgraphs adjacent to the whole
boundary says that, up to exchanging `C` and `D`, either neither component
contains two such subgraphs or only `D` does; in the latter case `T` is
independent.  The latter case has just been excluded.  \(\square\)

The canonical decomposition does not by itself synchronize the two boundary
colourings or augment the rooted minor model when the selected component is
one leaf and neither component contains two disjoint connected subgraphs
adjacent to every boundary vertex.

## Dependencies

- [Trace-preserving four-centre descent](hc7_k7minus_four_centre_trace_descent.md).
- [Canonical tri-separation form of the rooted-web cut](hc7_k7minus_four_centre_tri_separation_reduction.md).
- [Operation-coupled four-centre reduction](hc7_k7minus_four_centre_operation_cut_reduction.md), Theorem 4.1.
- [Two-component normal form for seven-vertex cuts](hc7_k7minus_three_component_seven_cut_exclusion.md), Corollary 2.
- Johannes Carmesin and Jan Kurkofka, *Canonical Decompositions of
  3-Connected Graphs*, Advances in Combinatorics 2025:7,
  <https://doi.org/10.19086/aic.2025.7>, especially Lemma 1.8.5,
  Section 2.2.3, Lemma 2.5.5, Lemma 2.5.11 and Theorem 2.2.8(ii).
