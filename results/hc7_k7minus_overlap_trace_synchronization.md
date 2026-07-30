# Synchronizing the common six-set in the distinct-miss residue

**Status:** written proof; [separate internal audit GREEN](hc7_k7minus_overlap_trace_synchronization_audit.md).  The six-vertex census in Corollary 4 is a computer-assisted finite result with retained verifier
[`hc7_k7minus_overlap_trace_synchronization_verify.py`](hc7_k7minus_overlap_trace_synchronization_verify.py).
This result strictly reduces, but does not close, the pair of overlapping
cuts whose two connected-subgraph packing numbers are `(1,1)`.

## 1. Setting and trace gluing

Assume

\[
 \kappa(G)\ge 7,\qquad \chi(G)=7,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G,
 \qquad K_7^-\npreccurlyeq G.                         \tag{1}
\]

Let `u` have degree eight, put `X=N_G(u)`, and suppose that
`G-N_G[u]` has two components `E,F`.  In the distinct nonadjacent-miss
case, write

\[
 N_X(E)=X-\{x\},\qquad N_X(F)=X-\{y\},\qquad
 x\ne y,\quad xy\notin E(G),\quad Z=X-\{x,y\}.       \tag{2}
\]

For a colouring of a graph containing `Z`, its **`Z`-trace** is the
equality partition induced on the literal vertices of `Z`.

### Lemma 1 (common-trace gluing)

If a six-colouring of `G-F` and a six-colouring of `G-E` have the same
`Z`-trace, then `G` is six-colourable.

#### Proof

Call the two colourings `c_E` and `c_F`, according to the exterior
component they retain.  The vertex `u` is adjacent to every vertex of
`Z`, so its colour is absent from `Z` in both colourings.  Equality of the
two `Z`-traces gives a bijection between the colours of their corresponding
blocks.  Extend that bijection by sending `c_F(u)` to `c_E(u)`, and then
extend it arbitrarily to a permutation of all six colours.  After applying
the permutation to `c_F`, the two colourings agree on `Z\cup\{u\}`.

Define a colouring of `G` by taking `c_E` on `E\cup\{y\}`, taking `c_F`
on `F\cup\{x\}`, and using their common values on `Z\cup\{u\}`.  The
only edges not wholly certified by one of the two original colourings
could run between the two selected pieces.  There are none: `E` is
anticomplete to `F\cup\{u,x\}`, `F` is anticomplete to `E\cup\{u,y\}`,
and `xy` is a nonedge.  The combined colouring is proper, contrary to
`chi(G)=7`. \(\square\)

Thus, in a counterexample, the two proper-minor `Z`-trace languages are
disjoint.  This conclusion uses the two distinct misses and the nonedge
`xy`; it does not use the packing-`(1,1)` conclusion.

## 2. Exact forcing by connected `Z`-full subgraphs

Call a connected subgraph of `E` or `F` **`Z`-full** when it is adjacent
to every literal vertex of `Z`.  Let `nu_Z(E)` and `nu_Z(F)` be the
maximum orders of vertex-disjoint families of such subgraphs.

For a partition `Pi` of `Z` into independent blocks, let

\[
 d_Z(\Pi)=|\Pi|-\omega\bigl(G[\operatorname{sing}(\Pi)]\bigr), \tag{3}
\]

where `sing(Pi)` is the set of vertices occurring as singleton blocks.

### Lemma 2 (common-boundary reflection)

Let `Pi` be a proper equality partition of `Z` with at most five blocks.
If

\[
 d_Z(\Pi)\le \min\{\nu_Z(E),\nu_Z(F)\},               \tag{4}
\]

then `G` is six-colourable.

#### Proof

Choose a maximum clique `U` among the singleton blocks of `Pi`, and let
`B_1,...,B_m` be all remaining blocks.  Thus `m=d_Z(Pi)`.  Inside `F`,
choose disjoint connected `Z`-full subgraphs `P_1,...,P_m`.  Contract a
spanning tree of each connected set `P_i\cup B_i`.  The resulting minor is
proper because `m>=1` in the present `K_4`-minor-free setting.

The contracted representatives together with the literal vertices of
`U` form a clique: fullness supplies all adjacencies involving a
representative, and `U` is a clique.  A six-colouring of this proper minor
therefore pulls back on `G-F` to an exact `Z`-trace `Pi`.  Only the
independent boundary blocks are expanded; no vertex of a contracted
subgraph in `F` is expanded.

Repeating the same construction with `E` gives a six-colouring of `G-E`
with the same exact trace.  Lemma 1 glues the two colourings. \(\square\)

Call (3) the **reflection demand** of `Pi`, and let

\[
 \delta_Z=\min_\Pi d_Z(\Pi).                           \tag{5}
\]

Because `G[Z]` is `K_4`-minor-free in the present residue, it is
three-colourable.  Hence a minimum-demand partition may be chosen with at
most three blocks.  Lemma 2 gives the unbounded host conclusion

\[
 \boxed{\min\{\nu_Z(E),\nu_Z(F)\}<\delta_Z.}          \tag{6}
\]

This is stronger than merely observing that the two seven-boundary full
packing numbers are one: it also controls connected subgraphs required to
meet only the shared six-set.

## 3. The demand-one type is impossible

The previous nonfull-attachment reduction gives

\[
 \alpha(G[Z])\le3,\qquad K_4\npreccurlyeq G[Z],\qquad
 K_4^-\npreccurlyeq G[Z-z]\quad(z\in Z).               \tag{7}
\]

### Lemma 3 (unique demand-one boundary)

Under (7), `delta_Z<=1` holds if and only if `G[Z]` is the net:
a triangle with one pendant vertex at each triangle vertex.

#### Proof

By the clique-deletion demand identity, demand at most one gives a clique `U` such
that `I=Z-U` is independent.  The independence bound gives `|I|<=3`,
while `K_4`-minor-freeness gives `|U|<=3`.  Since `|Z|=6`, both sets have
order three and `U` is a triangle.

Every vertex of `U` has a neighbour in `I`, since otherwise that vertex
together with `I` would be an independent four-set.  Every vertex of `I`
has at most one neighbour in `U`: two such neighbours together with the
triangle `U` give a `K_4^-` after deleting a different vertex of `I`,
and three give a literal `K_4`.  There are therefore exactly three
`U-I` edges, and they form a perfect matching.  This is the net.

Conversely, deleting the triangle from the net leaves an independent set,
so its demand is one. \(\square\)

By (6), the net cannot occur: both connected exterior components are
themselves `Z`-full, so the left side of (6) is at least one.

## 4. A triangle forces common-six packing one

### Lemma 4 (triangle packing lift)

If `G[Z]` contains a triangle, then

\[
                         \nu_Z(E)=\nu_Z(F)=1.           \tag{8}
\]

#### Proof

Suppose `E` contains two disjoint connected `Z`-full subgraphs `P,Q`.
Because `E` is connected, a shortest `P-Q` path can be absorbed, except
for its last endpoint, into `P`; the enlarged `P` and `Q` are then
connected, disjoint, adjacent, and still `Z`-full.

Let `T` be a triangle in `Z`, and choose distinct
`z,w in Z-T`.  The seven connected branch sets

\[
 P\cup\{z\},\quad Q\cup\{w\},\quad F\cup\{x\},
 \quad\{u\},\quad(\{t\}:t\in T)                       \tag{9}
\]

are pairwise adjacent.  The first two are adjacent by construction; their
anchors `z,w` join them to `F\cup\{x\}` and to `u`; the edge `ux` joins
the latter two bags; and `Z`-fullness supplies every adjacency to the
triangle.  Thus (9) is an explicit `K_7`-minor model, contrary to (1).
The argument for `F` is symmetric.  Each component is itself `Z`-full,
so both packing numbers equal one. \(\square\)

### Corollary 4 (exact six-vertex residue)

Up to isomorphism, exactly 28 graphs on six vertices satisfy (7).  Their
reflection-demand distribution is

\[
 \#\{\delta_Z=1,2,3\}=1,26,1.                         \tag{10}
\]

The unique demand-one graph is the net and is eliminated by Lemma 3 and
(6).  The unique demand-three graph is `K_3 dotcup K_3`.  Sixteen of the
28 graphs contain a triangle; after eliminating the net, the 15 triangular
survivors satisfy (8).  The other 12 are triangle-free, all have demand
two, and (6) says that at least one of `E,F` has `Z`-full packing number
one.

The adjacent deterministic verifier enumerates all 156 unlabelled
six-vertex graphs with nauty `geng`, checks the two minor exclusions by
exact deletion/contraction recursion, and checks independence, triangles,
and reflection demand directly.  This finite classification does not replace
the unbounded proofs in Lemmas 1--4.

## 5. Exact stopping point

The conclusion is not synchronization of every remaining pair of trace
languages.  The explicit
[three-matching parity-language barrier](../barriers/hc7_k7minus_overlap_trace_language_barrier.md)
shows that, even after retaining all independent-block contractions and
the central colouring constraint, two abstract response languages may be
disjoint.  Closing the remaining 27 common boundaries therefore requires
compatibility between operation-related colourings or additional topology
inside an exterior component whose `Z`-full packing number is one.

## Dependencies

- [nonfull-attachment reduction](hc7_k7minus_nonfull_attachment_reduction.md);
- [critical seven-cut capacity](hc7_k7minus_critical_seven_cut_capacity.md);
- [clique-deletion demand identity](hc7_exact7_packet_demand_identity.md).
