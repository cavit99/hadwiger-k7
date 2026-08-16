# Every exceptional centre has a remote removable edge and an exact operation cube

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_remote_removable_edge_operation_cube_audit.md).
The first
theorem is a general consequence of Chu's prescribed-set removable-edge
theorem.  The critical-host application is computation-free and produces a
new exact common object at every exceptional degree-eight vertex.  It does
not prove the `K_7^-` six-colour conjecture or `HC_7`.

An edge `f` of a `k`-connected graph is **`k`-removable** if `G-f` remains
`k`-connected.

## 1. A general remote-edge theorem

### Theorem 1.1 (remote removable edge at a low-degree vertex)

Let `k\ge2`, let `G` be a `k`-connected graph with minimum degree at least
`k+1`, and let `z` be a vertex of degree `k+1`.  Put

\[
                         W=N_G(z),
              \qquad U=V(G)-W.                       \tag{1.1}
\]

Suppose that

\[
 |U|\ge k,
 \qquad K_k\npreccurlyeq G,
 \qquad \chi(G)>\chi(G[W])+2.                        \tag{1.2}
\]

Then `G-N_G[z]` contains a `k`-removable edge of `G`.

#### Proof

First, `G[U]` has an edge.  Otherwise every vertex of `U` has all its at
least `k+1` neighbours in the `(k+1)`-set `W`, and hence `G` contains a
complete bipartite subgraph with parts `U` and `W`.  Choose `k` vertices
on each side.  Contracting a perfect matching between them gives `k`
pairwise adjacent connected branch sets, a `K_k` minor, contrary to
(1.2).

Apply Theorem 2.2 of Chu's prescribed-set removable-edge theorem with this
set `W`.  Here `|W|=k+1`, and every vertex of `U` has degree at least

\[
                         \max\{k+1,|W|\}=k+1.         \tag{1.3}
\]

It gives a `k`-removable edge in `G[U]` unless `G[U]` is a forest.  In the
exceptional case, colour `G[W]` and the forest `G[U]` with disjoint
palettes.  This gives a proper colouring of `G` with at most
`\chi(G[W])+2` colours, contrary to (1.2).

Thus a `k`-removable edge `f` lies in `G[U]`.  The vertex `z` is isolated
in `G[U]`, because all its neighbours belong to `W`.  Hence neither end of
`f` is in `N_G[z]`, as required. `\square`

The conclusion is stronger than an edge merely avoiding `z`: both ends are
nonadjacent to `z`, while deleting the edge preserves the full original
connectivity.

## 2. Application at every exceptional centre

Assume from now on that `G` is a hypothetical critical host:

\[
 \begin{gathered}
  \chi(G)=7,
  \qquad \chi(J)\le6\text{ for every proper minor }J\text{ of }G,\\
  \kappa(G)\ge7,
  \qquad \delta(G)\ge8,
  \qquad |E(G)|\ge4|V(G)|,
  \qquad |V(G)|\ge25,
  \qquad K_7^-\npreccurlyeq G.                       \tag{2.1}
 \end{gathered}
\]

A degree-eight vertex `z` is **exceptional** when `G[N(z)]` contains no
`K_4` subgraph.  The audited exceptional-neighbourhood theorem gives

\[
                         \alpha(G[N(z)])=3.           \tag{2.2}
\]

### Lemma 2.1 (the exceptional neighbourhood is four-colourable)

For every exceptional vertex `z`,

\[
                         \chi(G[N(z)])\le4.           \tag{2.3}
\]

#### Proof

Choose an independent triple `I\subseteq N(z)` using (2.2).  The graph on
the other five vertices is `K_4`-free and is therefore three-colourable.
For completeness, a hypothetical four-critical subgraph has minimum degree
at least three.  If it has at most four vertices it is `K_4`.  If it has
five, its complement has maximum degree at most one.  Avoiding a `K_4`
forces that complement to contain two disjoint edges, and the resulting
graph `K_5-2K_2` is three-colourable by giving the ends of each missing edge
one common colour and the remaining vertex a third colour.  This is a
contradiction.

Give `I` one new colour in addition to that three-colouring. `\square`

### Corollary 2.2 (a remote seven-removable edge at every centre)

For every exceptional degree-eight vertex `z`, there is an edge

\[
                      f=uv\in E(G-N[z])              \tag{2.4}
\]

such that `G-f` is seven-connected.

#### Proof

Apply Theorem 1.1 with `k=7`.  The set `U=V(G)-N(z)` has order
`|V(G)|-8\ge17`, `G` has no `K_7` minor because it has no `K_7^-` minor,
and Lemma 2.1 gives

\[
                       7=\chi(G)>4+2.
\]

All hypotheses hold. `\square`

## 3. The centred four-edge operation cube

Fix an exceptional `z`, choose an independent triple

\[
                         I=\{x_1,x_2,x_3\}
                            \subseteq N(z),           \tag{3.1}
\]

and let `f=uv` be supplied by Corollary 2.2.  Put

\[
 T=\{zx_1,zx_2,zx_3,f\}
          \cong K_{1,3}\mathbin{\dot\cup}K_2.        \tag{3.2}
\]

The two components in (3.2) are vertex-disjoint and induced on their own
vertex sets: `I` is independent and both ends of `f` lie outside `N[z]`.

For disjoint sets `C,D\subseteq T`, let `G/C-D` denote the minor obtained
by contracting the edges in `C` and deleting the edges in `D`; every edge
of `T-(C\cup D)` is kept.

For a proper colouring `c` of `G-T`, write

\[
                  \Sigma_T(c)=\{xy\in T:c(x)=c(y)\}. \tag{3.2A}
\]

### Theorem 3.1 (full mixed-operation exact-six cube)

For every pair of disjoint sets `C,D\subseteq T` with
`C\cup D\ne\varnothing`,

\[
                          \chi(G/C-D)=6.              \tag{3.3}
\]

Thus the four labelled edges support all

\[
                              3^4-1=80                \tag{3.4}
\]

nontrivial keep/delete/contract patterns as exact six-chromatic proper
minors of the same graph.

#### Proof

Every graph in (3.3) is a proper minor, so it is at most six-colourable by
(2.1).  Suppose some `M=G/C-D` had a proper five-colouring.  Expand the
contracted forest components, initially retaining the contraction colours.

If at least one of the three star edges belongs to `C\cup D`, recolour `z`
with a fresh sixth colour.  If `f\in C\cup D`, recolour one fixed end `u`
of `f` with that same fresh colour.  The vertices `z,u` are nonadjacent by
(2.4).  Every other neighbour of either recoloured vertex still uses one of
the original five colours.  The independent set `I` prevents a collapsed
edge among the star leaves, and componentwise inducedness ensures that the
expansion creates no other collapsed edge.  Every operated edge is now
proper, while every kept edge was represented in `M` and remains proper.

This is a proper six-colouring of `G`, contrary to (2.1).  Hence every
minor in (3.3) is exactly six-chromatic. `\square`

### Corollary 3.2 (exact connectivity and all deletion signatures)

Let `H=G-T`.  Then:

1. `H` is exactly five-connected, has at least `4|V(G)|-4` edges and is
   exactly six-chromatic.
2. Its equality signatures on `T` are exactly

   \[
      \{\Sigma_T(c):c\in\operatorname{Col}_6(H)\}
                              =2^T-\{\varnothing\}.   \tag{3.5}
   \]

3. `H` has a spanning `K_7^\vee` model which is exact even after all four
   edges of `T` are restored in `G`.
4. `G/T` is exactly six-chromatic and has a spanning `K_6` model.  On
   expansion in `G`, one branch set contains the whole star
   `G[\{z\}\cup I]`, and a branch set, possibly the same one, contains
   both ends of `f`.

#### Proof

The exact chromatic statements for `H` and `G/T` are the all-delete and
all-contract instances of Theorem 3.1.

Put `J=G-f`, which is seven-connected.  The degree of `z` in `H` is five,
so `\kappa(H)\le5`.  Suppose a set `S` of order at most four disconnects
`H`.  If `z\in S`, then `H-S=J-S` is connected.  Otherwise let `A` be the
component of `H-S` containing `z` and let `B` be another component.  Since
`d_H(z)=5>|S|`, the set `A-\{z\}` is nonempty.  The only edges of `J-H`
are the three displayed edges incident with `z`, so `S\cup\{z\}` separates
`A-\{z\}` from `B` in `J`.  Its order is at most five, contradicting the
seven-connectivity of `J`.  Thus `\kappa(H)=5`.

For nonempty `Q\subseteq T`, expand a six-colouring of `G/Q`.  Forestness
and componentwise inducedness give signature exactly `Q` on `H`.  An empty
signature would six-colour `G`, proving (3.5).

The density bound and five-connectivity let us apply Norin--Totschnig,
Theorem 6; the exceptional graph `K_{2,2,2,2}` is excluded by
`|V(G)|\ge25`.  Hence `H` has a `K_7^\vee` model, which can be made
spanning.  If either nominally missing bag pair were adjacent in `G`,
whether already in `H` or through an edge restored from `T`, the same bags
would form a `K_7^-` model in `G`.  Target exclusion therefore makes the
model exact in `G`.

Finally, the established case `HC_6` supplies a `K_6` model in the exactly
six-chromatic connected minor `G/T`; unused vertices may be absorbed.
Expanding the two contraction images gives the stated co-bagged model in
`G`. `\square`

### Corollary 3.3 (a six-connected path-plus-remote-edge host)

For distinct `x_i,x_j\in I`, put

\[
                      T_3=\{zx_i,zx_j,f\},
             \qquad H_3=G-T_3.                       \tag{3.6}
\]

Then `H_3` is exactly six-connected and exactly six-chromatic, has all
seven nonempty signatures on the componentwise-induced forest
`P_3\dot\cup K_2`, and has a spanning exact `K_7^\vee` model.  Every one
of its `3^3-1=26` nontrivial mixed keep/delete/contract patterns is exactly
six-chromatic.

For any neighbour `x` of `z`, the two-edge host
`G-\{zx,f\}` is at least six-connected, exactly six-chromatic, has the
three nonempty equality signatures, and has a spanning exact
`K_7^\vee` model.  The quotient `G/zx/f` is exactly six-chromatic and its
spanning `K_6` model co-bags both endpoint pairs on expansion, possibly in
the same branch set.

#### Proof

The chromatic, signature and model assertions repeat Theorem 3.1 and
Corollary 3.2 on the indicated subforests.  Their deletion hosts have at
least `4|V(G)|-3` and `4|V(G)|-2` edges, respectively, so the same density
theorem applies.

For exact connectivity of `H_3`, work again in the seven-connected graph
`J=G-f`.  Now `d_{H_3}(z)=6`, giving the upper bound.  If a set `S` of
order at most five disconnected `H_3`, deletion of `z` handles the case
`z\in S`.  When `z\notin S`, the component containing `z` also contains a
second vertex because `d_{H_3}(z)>|S|`; then `S\cup\{z\}`, of order at
most six, disconnects `J`, a contradiction.  Thus `\kappa(H_3)=6`.

For `G-\{zx,f\}`, deleting one edge from the seven-connected graph `G-f`
lowers connectivity by at most one.  The fresh-sixth-colour argument in
Theorem 3.1 works for the componentwise-induced forest `\{zx,f\}` even
when `x\notin I`, proving all remaining assertions. `\square`

### Corollary 3.4 (a bounded opposite-shore response interface at every centre)

Let `C` be the component of `G-N[z]` containing the remote edge `f`, and
put

\[
                              Q=N_G(C).               \tag{3.7}
\]

Then

\[
                Q\subseteq N(z),
              \qquad 7\le |Q|\le8,                  \tag{3.8}
\]

and

\[
 V(G)=C\mathbin{\dot\cup}Q\mathbin{\dot\cup}
          (V(G)-(C\cup Q))                           \tag{3.9}
\]

is an actual separation.  On this one boundary the following opposite
response families coexist.

1. For every nonempty `J\subseteq\{zx_1,zx_2,zx_3\}`, a signature-`J`
   colouring of `G-T`, with `f` proper, restricts to a proper colouring of
   `G[C\cup Q]`.  Its equality partition on `Q` is rejected by the intact
   opposite closed shore.
2. A signature-`\{f\}` colouring of `G-T` restricts to a proper colouring
   of `G-C`.  Its equality partition on `Q` is rejected by the intact
   `C`-shore.
3. The partition in item 2 is different from every one of the seven
   partitions in item 1.

Thus every exceptional centre supplies an actual order-seven or order-eight
separation carrying a full punctured three-coordinate centre-star response
family in one orientation and a seven-removable remote-edge response in the
other.

#### Proof

The vertex `z` has no neighbour in `G-N[z]`, so every neighbour of `C`
belongs to `N(z)`.  Hence `Q\subseteq N(z)` and `|Q|\le8`.  The set `Q`
separates the nonempty component `C` from the vertex `z`; seven-connectivity
gives `|Q|\ge7`.  The vertex `z` belongs to the opposite open shore, so the
separation is actual.

For nonempty `J\subseteq\{zx_1,zx_2,zx_3\}`, take the signature-`J`
colouring from (3.5).  Its only monochromatic restored edges are incident
with `z`, which does not belong to `C\cup Q`; the edge `f` is proper.  Its
restriction to `G[C\cup Q]` is therefore proper.  Any extension of its
boundary partition through the opposite intact shore would glue to a
six-colouring of `G`, so the partition is rejected there.

For the signature-`\{f\}` colouring, both ends of the sole monochromatic
restored edge lie in `C`.  Its restriction to `G-C` is proper, and the same
gluing argument shows that its boundary partition is rejected by the intact
`C`-shore.

If this last partition equalled one from the first family, the two proper
closed-shore colourings would align on `Q` and glue to a six-colouring of
`G`.  This proves item 3. `\square`

### Corollary 3.5 (visible boundary-response rank)

Use the notation of Corollary 3.4.  For nonempty `A\subseteq I`, choose one
colouring with centre-star signature `\{zx:x\in A\}` and write
`pi_A` for its induced partition of `Q`.  Write `rho` for the partition
induced by the signature-`{f}` colouring.  Then:

1. if `I\subseteq Q`, at least four of the seven partitions `pi_A` are
   distinct, and the family together with `rho` contains at least five
   distinct partitions;
2. if `|I\cap Q|=2`, at least two of the seven partitions `pi_A` are
   distinct, and the family together with `rho` contains at least three
   distinct partitions.

In particular, the first conclusion always holds when `|Q|=8`.  When
`|Q|=7`, the first or second conclusion holds according as the unique
vertex of `N(z)-Q` lies outside or inside `I`.

#### Proof

In the colouring defining `pi_A`, the vertices of `I` having the same
colour as `z` are exactly the vertices in `A`.  Every vertex of `N(z)-I`
has a different colour from `z`, because its edge to `z` is
kept in `G-T`.  Consequently the visible part on `Q` of the colour block
containing `z` is exactly `A\cap Q`, whenever this set is nonempty.

If two centre-star colourings induced the same partition of `Q`, two
nonempty visible `z`-blocks would therefore have to be equal or disjoint:
they are blocks of one and the same partition.  If `I\subseteq Q`, use
the four endpoint sets

\[
                I,\quad I-\{x_1\},\quad I-\{x_2\},
                    \quad I-\{x_3\}.                 \tag{3.10}
\]

Their visible blocks are pairwise intersecting and pairwise unequal, so
their four partitions are distinct.  If `I\cap Q=\{x_i,x_j\}`, the
partitions `pi_{\{x_i\}}` and `pi_{\{x_i,x_j\}}` have intersecting unequal
visible blocks and hence are distinct.  Finally,
Corollary 3.4(3) says that `rho` differs from every centre-star partition.
This proves both bounds. `\square`

## 4. Exact scope

Theorem 3.1 supplies a remote operation at every exceptional centre, not
merely at one selected centre.  Its full deletion host simultaneously has
exact connectivity five, all fifteen nonempty equality signatures and an
exact spanning near-clique model; all eighty mixed minor patterns are
exactly six-chromatic.  Corollary 3.3 also gives a six-connected common
host for an induced two-edge path at the centre and the remote edge.
Corollary 3.4 converts the same object into a literal bounded separation
with operation-labelled response families in both orientations, and
Corollary 3.5 proves that at least five boundary states survive when the
three star leaves are visible, and at least three in the remaining case.

The theorem does not assert that the remote edges chosen for different
centres are distinct, form a matching, or occupy prescribed bags of one
fixed minor model.  It therefore does not replace the remaining
operation-to-model allocation theorem.

## 5. External and internal inputs

- H. Chu,
  [*A sharp extension of Halin's removable-edge theorem to matchings*,
  Theorem 2.2](https://arxiv.org/html/2608.09394#S2.Thmtheorem2.2): the
  prescribed-set removable-edge alternative used in Theorem 1.1.
- [exceptional-neighbourhood theorem](hc7_k7minus_exceptional_neighbourhood_completion.md)
- [critical-host structural conclusions](hc7_k7minus_degree7_rooted_helper_closure.md)
- S. Norin and A. Totschnig,
  [*Every graph with no `K_7^\vee` minor is 6-colourable*, Theorem 6](https://arxiv.org/html/2507.03244#S1.Thmtheorem6)
- the established case `HC_6`
