# Nonfull attachments at an exceptional degree-eight vertex

**Status:** written host reductions and computer-assisted finite boundary
classification; separate internal mathematical and computational audits
GREEN for this revision.  The retained verifier is
[`hc7_k7minus_nonfull_attachment_reduction_verify.py`](hc7_k7minus_nonfull_attachment_reduction_verify.py).
This result narrows the two-component exterior allocation problem.  It
does not prove
the `K_7^-` six-colour conjecture or `HC_7`.

Throughout, let `G` satisfy

\[
 \kappa(G)\ge7,
 \qquad \chi(G)=7,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G,
 \qquad K_7^-\npreccurlyeq G.                         \tag{H}
\]

Let `u` be exceptional of degree eight, put `X=N_G(u)`, and suppose
`G-N_G[u]` has exactly two components `E,F`.  The established exceptional-
neighbourhood theorem gives

\[
 \alpha(G[X])=3,
 \qquad K_4\not\subseteq G[X].                         \tag{1}
\]

Seven-connectivity makes each exterior component adjacent to at least seven
vertices of `X`; a nonfull component therefore misses exactly one.

## 1. A connected-rich seven-cut excludes boundary diamonds

For a seven-vertex cut `S`, call a connected subgraph of `G-S` **`S`-full**
when it is adjacent to every literal vertex of `S`.

### Lemma 1 (connected-rich diamond deletion)

Let `G` have no `K_7^-` minor and let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

where `L,R` are nonempty and anticomplete and `G[R]` is connected.  Suppose
`L` contains one connected `S`-full subgraph `Q`, while `R` contains two
vertex-disjoint connected `S`-full subgraphs `P_1,P_2`.  Then

\[
                         K_4^-\npreccurlyeq G[S]-z
                         \qquad(z\in S).                \tag{2}
\]

#### Proof

Join `P_1` to `P_2` by a shortest path in `G[R]`.  Its open interior avoids
both subgraphs.  Absorb the path except its endpoint in `P_2` into `P_1`.
This gives disjoint, connected, adjacent, `S`-full subgraphs `P'_1,P_2`.

If `B_1,\ldots,B_4` were the bags of a `K_4^-` model in `G[S]-z`, then

\[
 Q\cup\{z\},\qquad P'_1,\qquad P_2,
 \qquad B_1,\ldots,B_4                              \tag{3}
\]

would be seven disjoint connected branch sets.  The first three are
pairwise adjacent, each is adjacent to all four boundary bags, and at most
one adjacency is absent among the boundary bags.  Thus (3) is a `K_7^-`
model, a contradiction. \(\square\)

## 2. The two exterior components cannot miss the same vertex

### Theorem 2 (same-miss exclusion)

The components `E,F` do not have the same missed vertex of `X`.

#### Proof

Suppose both miss `x`, and put `S=X-\{x\}`.  The components of `G-S` are
exactly

\[
                         E,\qquad F,\qquad \{u,x\}.     \tag{4}
\]

They are all `S`-full.  The critical seven-cut capacity theorem says that
each component in a three-component cut has `S`-full packing number one.

The vertex `x` has no exterior neighbour.  Since `\delta(G)\ge7`, it is
adjacent to six or seven vertices of `S`.  If it sees all seven, the
singletons `\{u\}` and `\{x\}` are two disjoint `S`-full subgraphs inside
`\{u,x\}`, contrary to its packing number.

If `x` sees six vertices of `S`, then `d_G(x)=7`.  The vertex `u` is
universal in `G[N_G(x)]`.  The exact degree-seven neighbourhood theorem
therefore gives

\[
                         G[N_G(x)]\cong
                         K_1\vee(K_3\mathbin{\dot\cup}K_3),     \tag{5}
\]

with `u` as the universal vertex.  The six neighbours of `x` in `S` hence
contain a triangle.  That triangle together with `x` is a literal `K_4` in
`G[X]`, contradicting (1). \(\square\)

## 3. Exactly one nonfull component

### Theorem 3 (one-nonfull reduction)

Suppose `E` misses `x` and `F` is `X`-full.  Put `S=X-\{x\}` and
`H=G[S]`.  Then:

1. `G-S` has the two components `E` and `F\cup\{u,x\}`;
2. their `S`-full packing vector is exactly `(1,2)`, with `E` the
   packing-one component;
3. `|E(H)|\le9`, `\kappa(H)\le3`, `H` is `K_4`-free and `K_5`-minor-free,
   and `\alpha(H)=3`;
4. `H-z` has no `K_4^-` minor for every `z\in S`;
5. `H` has no independent triple whose four-vertex complement contains a
   triangle; and
6. the missed vertex `x` has at most four neighbours in `S` and at least
   two neighbours in `F`.

#### Proof

The component `F\cup\{u,x\}` is connected.  It contains the disjoint
`S`-full subgraphs `F` and `\{u\}`, while `E` itself is `S`-full.  The
critical seven-cut capacity theorem gives packing sum at most three with
one side of packing number one, proving items 1--2.  Its boundary
consequences give the edge and connectivity bounds in item 3; literal
`K_4`-freeness and `\alpha(H)\le3` follow from (1).  For completeness,
if `H` had a `K_5` model, any two of the three disjoint `S`-full subgraphs
`E,F,\{u\}` together with its five bags would form a `K_7^-` model, with
only the two exterior bags possibly nonadjacent.

If `\alpha(H)\le2`, then `\overline H` is triangle-free.  Mantel's theorem
and `|E(H)|\le9` force

\[
 |E(\overline H)|=12,
 \qquad \overline H\cong K_{3,4},
 \qquad H\cong K_3\mathbin{\dot\cup}K_4,
\]

contradicting `K_4`-freeness.  Thus `\alpha(H)=3`.

Apply Lemma 1 with thin subgraph `E` and rich subgraphs `F,\{u\}` inside
the connected side `F\cup\{u,x\}`.  This proves item 4.  Finally, an
independent triple with a triangle in its complement is the robust
independent-block outcome of the audited adaptive `(1,2)` reflection
theorem.  That theorem gives a `K_7` minor or a six-colouring of `G`, both
contrary to (H).  This proves item 5.

Items 3 and 5 show that `H` has no robust independent block from the
audited adaptive `(1,2)` reduction: its independence number is three, and
the only possible order-three block would have a triangular complement.
Item 4 also implies that `H-\{a,b\}` is `K_4`-minor-free for every pair
`a,b`, since a `K_4` minor there would be a `K_4^-` minor in `H-a`.
Hence `H` belongs to the frozen 129-boundary residual.

If `x` had at least five neighbours in `S`, apply the audited uniform
defect-two carrier theorem to the separation with rich shore
`F\cup\{u,x\}` and opposite shore `E`.  The rich shore contains the
pairwise disjoint connected subgraphs `F`, `\{u\}`, and `\{x\}`; the
first two are `S`-full and the third misses at most two vertices of `S`.
The opposite component `E` is `S`-full.  That theorem would six-colour
`G`, contrary to (H).  Thus `|N(x)\cap S|\le4`.  Since
`\delta(G)\ge7`, while `x` sees `u` and has no neighbour in `E`, it has
at least two neighbours in `F`.  This proves item 6. \(\square\)

### Corollary 3.1 (computer-assisted one-nonfull boundary census)

Up to isomorphism, exactly 28 graphs of order seven satisfy all boundary
conditions in items 3--5 of Theorem 3.  Their edge and connectivity
distributions are

\[
 \#\{|E(H)|=5,6,7,8,9\}=1,4,10,11,2,
 \qquad
 \#\{\kappa(H)=0,1,2\}=9,15,4.
\]

All 28 graphs are three-chromatic.  Twenty-one become bipartite after
deleting one vertex, four require deleting a two-vertex clique, and three
have no clique odd-cycle transversal.  Their graph6 codes are

```text
FCOc_ FCOe_ FCOf_ FCOeo FCOfo FCOfw FCQ`_ FCQaO FCQe_ FCQb_
FCQeO FCQbO FCQfO FCQeo FCQbo FCQQO FCQUO FCQRO FCQVO FCR`o
FCQrO FCQrW FCp`_ FCpd_ FCpb_ FCXe_ FCdb? FCdeG
```

and the SHA-256 digest of the sorted newline-separated code list is

```text
a045e1d21098d0789ea1c549ed00f380ab97df9120335ff24127f9c8a039eacd
```

The deterministic verifier enumerates all 1,044 unlabelled order-seven
graphs with nauty `geng`.  It tests independence number, literal cliques,
edge count and connectivity directly, and tests `K_5` and `K_4^-` minor
containment by exact deletion/contraction recursion.  It then checks every
vertex deletion and every independent triple.  This census classifies only
the literal boundary; the reduction from the unbounded host is the written
proof of Theorem 3.

## 4. Two distinct missed vertices

### Theorem 4 (overlapping-cut reduction)

Suppose `E` misses `x`, `F` misses `y`, and `x\ne y`.

1. If `xy\in E(G)`, both cuts `X-\{x\}` and `X-\{y\}` have connected-rich
   packing vector `(1,2)` and satisfy boundary conclusions 3--5 of Theorem
   3 on their respective seven-vertex boundaries.
2. If `xy\notin E(G)`, each joined side has packing number one.  Each
   opposite exterior component has packing number one or two; a packing-two
   side again produces a connected-rich `(1,2)` cut.  Unless at least one
   overlapping cut is `(1,2)`, both are `(1,1)`; this pair of overlapping
   `(1,1)` cuts is the only new packet cell.
3. In the nonadjacent case, with `Z=X-\{x,y\}`,

   \[
                    K_4\npreccurlyeq G[Z],
       \qquad       K_4^-\npreccurlyeq G[Z-z]\quad(z\in Z).      \tag{6}
   \]

#### Proof

Consider `S_x=X-\{x\}`.  Its two components are `E` and
`F\cup\{u,x\}`.  If `xy` is an edge, `F\cup\{x\}` and `\{u\}` are two
disjoint `S_x`-full subgraphs in the connected joined side.  The critical
seven-cut theorem makes the vector exactly `(1,2)`.  Repeat the proof of
Theorem 3 using `F\cup\{x\}` and `\{u\}` as the two rich packets; this
gives boundary conclusions 3--5.  The argument for `S_y` is symmetric,
using `E\cup\{y\}` and `\{u\}`, and proves item 1.

If `xy` is a nonedge, every `S_x`-full connected subgraph of the joined
side contains `u`: both `F` and `x` miss the boundary vertex `y`.  Thus that
side has packing number one.  The critical capacity bound leaves packing
number one or two on `E`.  The symmetric statement holds at `S_y`, proving
item 2.

For item 3, a `K_4` model in `G[Z]`, together with

\[
                   E\cup\{y\},\qquad F\cup\{x\},\qquad \{u\},   \tag{7}
\]

would be a `K_7^-` model: only the first two displayed bags might be
nonadjacent.  If instead `G[Z-z]` contained a `K_4^-` model, use

\[
                E\cup\{y,z\},\qquad F\cup\{x\},\qquad \{u\}.   \tag{8}
\]

The three bags in (8) are pairwise adjacent because `F` sees `z`, and the
only possible missing adjacency is now inside the boundary model.  Both
constructions contradict (H), proving (6). \(\square\)

## 5. Exact stopping point

The remaining `(1,1)` cell is not a hidden demand-one reflection.  For its
seven-vertex boundary `H`, both `\omega(H)` and `\alpha(H)` are at most
three.  The packet-demand identity says that demand at most one would
require a clique `U` for which `H-U` is independent.  This would give

\[
                         |V(H)|\le\omega(H)+\alpha(H)\le6,
\]

contrary to `|V(H)|=7`.  Thus every equality partition has packet demand at
least two, beyond one packet on either side.

Theorems 2--4 eliminate the same-miss case and replace every other nonfull
attachment by a named `(1,2)` boundary residue or two overlapping `(1,1)`
cuts with the minor exclusions (6).  Current cut reflection controls whole
`S`-full subgraphs; it does not divide a packet-one exterior component into
five partially attached rooted bags.  No shore-allocation theorem is
claimed.

## Inputs

- [critical seven-cut capacity](hc7_k7minus_critical_seven_cut_capacity.md)
- [degree-seven neighbourhood classification](hc7_k7minus_degree7_clique_incidence.md)
- [adaptive `(1,2)` boundary closure](hc7_exact7_adaptive_12_boundary_closure.md)
- [packet-demand identity](hc7_exact7_packet_demand_identity.md)
- [uniform defect-two carrier reflection](hc7_exact7_all_residual_defect2_carrier.md)
- [exceptional-neighbourhood completion](hc7_k7minus_exceptional_neighbourhood_completion.md)
