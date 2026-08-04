# Contracting the singleton triangle exposes a new six-separation

**Status:** active computation-free written reduction; separately audited in
the [adjacent audit](hc7_k7minus_e5_s3_triangle_contraction_reduction_audit.md).
This note does not prove `(E5)`.

Use the exact singleton endpoint of the
[three-separator edge-atom elimination](hc7_k7minus_e5_s3_edge_atom_elimination.md).
Thus `G` is a minimum `E5` enemy, the selected degree-five leaf is `t`,
and there are three-sets `T,R_0 union {b}` such that

```text
N_G(p)=T union {t,q},                 |T|=3,
N_G(q)={p,t,b} union R_0,             |R_0|=2,
N_G(t)={p,q,x,y,u_t}.
```

The vertices `p,t,q` induce a triangle.  The cut
`T union {t,q}` has singleton low component `{p}`, while
`{p,t,b} union R_0=N_G(q)` has singleton low component `{q}`.

## Lemma 1 (the two adhesions are not identical)

One has

\[
                             T\ne\{b\}\cup R_0.       \tag{1}
\]

### Proof

If equality held, the connected set `{p,q}` would have open neighbourhood

\[
                             \{t\}\cup T,
\]

of order four: the displayed exact neighbourhoods contain every edge from
`p` or `q` to the rest of `G`.  Deleting that four-set would separate
`{p,q}`, contrary to five-connectivity.  \(\square\)

## Lemma 2 (density of the triangle contraction)

Contract the triangle `{p,t,q}` to a single vertex `z`, and call the
resulting graph `J`.  Then

\[
                         |E(J)|\ge4|V(J)|-5.           \tag{2}
\]

### Proof

There are exactly nine incidences from the triangle to its exterior:

```text
three from p to T,
three from t to {x,y,u_t},
three from q to {b} union R_0.
```

By Lemma 1, the union of `T` and `{b} union R_0` has order at least four.
The vertices `x,y` are distinct from that union, so the exterior
neighbourhood of the triangle has order at least six.  Contracting the
triangle loses its three internal edges and at most `9-6` duplicate
exterior incidences, hence at most six edges.  Since

```text
|E(G)|=4|V(G)|-7,                  |V(J)|=|V(G)|-2,
```

inequality (2) follows.  \(\square\)

## Theorem 3 (new exact four-cut and lifted six-separation)

The graph `J` is four-connected but not five-connected.  Every four-cut
of `J` contains `z`.  Consequently there is a three-set `R` such that

\[
                         \{z\}\cup R                  \tag{3}
\]

is an exact four-cut of `J`, and

\[
                         \{p,t,q\}\cup R              \tag{4}
\]

is an order-six cut of `G`.

Every component behind (3) is adjacent to every member of `R` and to `z`.
Equivalently, every component behind (4) is adjacent to every member of
`R` and has a neighbour in the triangle `{p,t,q}`.

### Proof

First, `J` is three-connected.  A cut of order at most two avoiding `z`
would lift unchanged to `G`; one containing `z` would lift after replacing
`z` by `p,t,q` to a cut of `G` of order at most four.  Both contradict
five-connectivity.

Suppose that `J` has a three-cut.  It must contain `z`, and replacing `z`
by the triangle gives an exact five-cut

\[
                         Q=\{p,t,q\}\cup R',           \tag{5}
\]

where `|R'|=2`.  Every component behind a minimum five-cut is adjacent to
all five cut vertices, in particular to `t`.  But the neighbours of `t`
outside (5) are precisely the surviving members of `{x,y,u_t}`, and all
of them lie in one component:

- if both `x,y` survive, they are joined through any surviving member of
  `S`;
- if exactly one survives, it joins every surviving member of `S`;
- if both are deleted, then `u_t` survives and is the only possible
  neighbour of `t` outside the cut.

At least one of the three vertices survives because `|R'|=2`.  Thus every
component behind (5) contains a vertex of the same connected set, which is
impossible.  Hence `J` is four-connected.

The graph `J` is a proper target-free minor satisfying the `E5` threshold
by (2).  If it were five-connected, it would contradict the minimum choice
of `G`.  It therefore has a four-cut.  Such a cut contains `z`, since one
avoiding `z` would lift unchanged to a four-cut of `G`.  This proves
(3)--(4).  Fullness to the four-cut in the four-connected graph `J` gives
the final assertion.  \(\square\)

## 4. Published near-clique conclusion and its exact limit

Norin--Totschnig, Theorem 6, applies to `J`: it is four-connected and its
density in (2) is strictly above `4|V(J)|-8`.  The exceptional graph
`K_{2,2,2,2}` has exactly `4|V|-8` edges and therefore cannot occur.  Hence

\[
                              K_7^\vee\preccurlyeq J, \tag{6}
\]

where `K_7^vee` is `K_7` with two incident edges deleted.

The theorem is S. Norin and A. Totschnig,
[*Every graph with no `K_7^vee`-minor is 6-colorable*, Theorem 6](https://arxiv.org/abs/2507.03244).

Neither (6) nor the six-separation (4) is by itself a `K_7^-` model.
The published theorem does not prescribe the bag containing `z`, and an
arbitrary bag containing `z` need not split across the three preimages
`p,t,q` while retaining one of the two missing adjacencies.  Likewise, a
component behind (4) is guaranteed to meet the triangle only in aggregate,
not at all three named vertices.

## 5. Exact endpoint

The triangle contraction is strictly stronger than contracting `pt` alone:
both inherited singleton cuts are absorbed, and non-five-connectivity now
returns a genuinely new exact order-six separation.  The sole `s=3`
singleton obstruction has therefore been reduced to a four-connected graph
of density at least `4|V|-5` with

1. a `K_7^vee` minor;
2. an exact four-cut containing the contracted triangle vertex; and
3. a lifted order-six separation whose components meet all three other cut
   vertices and at least one of `p,t,q`.

The smallest repair is a labelled near-clique-or-separation theorem: either
choose the model in (6) so that expanding its `z`-bag restores one missing
adjacency, or use (3) to produce an explicit `K_7^-` model or a strict
lexicographic high-excess descent in `G`.  An unlabelled `K_7^vee` model or
an arbitrary order-six side proves neither conclusion.
