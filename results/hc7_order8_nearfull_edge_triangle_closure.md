# An order-eight near-full edge component with two additional full components

**Status:** written reductions together with the computer-assisted finite
Lemma 4.1; separate internal audit **GREEN** in
[`hc7_order8_nearfull_edge_triangle_closure_audit.md`](hc7_order8_nearfull_edge_triangle_closure_audit.md).
This result closes one exact three-component subcase and does not prove
`HC_7`.

## 1. Setting and notation

For a graph `H`, let `tau_odd(H)` be the minimum order of a vertex set whose
deletion makes `H` bipartite.  If `r,s` are distinct vertices of `H`, write
`H+rs` for the graph obtained by adding the edge `rs` when it is absent.

A connected subgraph disjoint from a vertex set `S` is **`S`-full** when it
has a neighbour at every vertex of `S`.

## 2. The exact orientation obstruction

### Lemma 2.1 (rooted odd-cycle transversal)

Let `H` be a graph and let `r,s` be distinct vertices.  The following are
equivalent.

1. There are a set `Z` of order at most two and a bipartition

   \[
                    V(H)-Z=P\mathbin{\dot\cup}Q
   \]

   such that `r` does not belong to `P` and `s` does not belong to `Q`.
   A root in `Z` imposes no condition.
2. `tau_odd(H+rs)<=2`.

#### Proof

Suppose first that item 1 holds.  If both roots survive, then `r` belongs
to `Q` and `s` belongs to `P`, so the added edge `rs` runs between the two
bipartition classes.  If either root was deleted, that edge is absent from
`(H+rs)-Z`.  Thus `(H+rs)-Z` is bipartite.

Conversely, let `Z` of order at most two make `(H+rs)-Z` bipartite.  If both
roots survive, the edge `rs` puts them on opposite sides; name the sides so
that `r` belongs to `Q` and `s` belongs to `P`.  If exactly one root
survives, reverse the bipartite component containing it when necessary to
put it on the required side.  If neither survives, there is no condition.
The remaining bipartite components may be oriented arbitrarily.  This gives
item 1. \(\square\)

### Lemma 2.2 (oriented contraction obstruction)

Let `G` satisfy

\[
 \chi(G)=7,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G. \tag{2.1}
\]

Let `(A,B)` be a separation with boundary `S`, where

\[
                    V(A-B)=\{v,a\},\qquad va\in E(G). \tag{2.2}
\]

Assume `|S|>=3`.

There do not exist `Z subseteq S`, `|Z|<=2`, and a partition

\[
                    S-Z=P\mathbin{\dot\cup}Q            \tag{2.3}
\]

such that `P,Q` are independent, `P subseteq N_G(v)`, and
`Q subseteq N_G(a)`.

#### Proof

Contract spanning trees of the two disjoint connected sets

\[
                       \{v\}\cup P,\qquad \{a\}\cup Q.
\]

At least one contraction is nontrivial because `|S-Z|>=1`.  Six-colour the
resulting proper minor.  The edge `va`
forces the two contraction images to have distinct colours.  Expanding
those colours over `P,Q` gives a proper six-colouring of `B` in which `S`
uses at most `2+|Z|<=4` colours.  Give `v,a` two distinct colours absent
from `S`.  Since their other neighbours lie in `S`, this six-colours `G`,
contrary to (2.1). \(\square\)

In particular, suppose `v` misses exactly `r` in `S` and `a` misses exactly
`s`, where `r!=s`.  Lemma 2.1 and Lemma 2.2 give

\[
                       \tau_{\rm odd}(G[S]+rs)\ge3.     \tag{2.4}
\]

## 3. The `K_4`-minor-free full-endpoint case needs no computation

### Lemma 3.1

Every `K_4`-minor-free graph on eight vertices has an odd-cycle transversal
of order at most two.

#### Proof

A `K_4`-minor-free graph has treewidth at most two, and hence is
two-degenerate and three-colourable.  In a proper three-colouring of eight
vertices, a smallest colour class has order at most two.  Delete that class;
the union of the other two colour classes is bipartite. \(\square\)

Consequently Lemma 2.2 excludes the `K_4`-minor-free case in which both ends
of the edge are `S`-full.  It also excludes the `K_4`-minor-free case in
which exactly one end has a unique missed boundary vertex: orient the
bipartite component containing that vertex toward the other endpoint.

## 4. Finite rooted triangle alternative

### Lemma 4.1 (computer-assisted)

Let `H` be a graph on eight vertices such that

\[
 \alpha(H)\le3,
 \qquad K_4\not\preccurlyeq H-Z
       \text{ for every two-set }Z\subseteq V(H).       \tag{4.1}
\]

For each endpoint mark choose either `FULL` or one vertex missed by that
endpoint; two vertex marks must be distinct.  Then at least one of the
following holds:

1. there are `Z subseteq V(H)`, `|Z|<=2`, and a bipartition

   \[
                  V(H)-Z=P\mathbin{\dot\cup}Q
   \]

   such that `P` avoids the first endpoint's mark and `Q` avoids the second
   endpoint's mark, with `FULL` imposing no condition;
2. both endpoints have distinct vertex marks `r,s`, and `H-{r,s}` contains
   a triangle.

The deterministic certificate generator
[`hc7_order8_rooted_oct_triangle_certificate.py`](hc7_order8_rooted_oct_triangle_certificate.py)
and independent checker
[`hc7_order8_rooted_oct_triangle_check.py`](hc7_order8_rooted_oct_triangle_check.py)
verify this statement over the complete nauty catalogue.  The exact census
is

\[
\begin{array}{lr}
\text{unlabelled graphs satisfying (4.1)}&185,\\
\text{endpoint-mark profiles}&13,505,\\
\text{profiles with a compatible bipartition}&13,247,\\
\text{remaining profiles with a triangle witness}&258.
\end{array}
\]

All full/full profiles and all `2,960` one-miss profiles have a compatible
bipartition.  The `258` triangle outcomes occur among the `10,360` ordered
distinct two-miss profiles.

This is a finite computer-assisted result.  Catalogue completeness is
delegated to nauty; the checker independently decodes the graphs, recognizes
the `185` graphs satisfying (4.1), verifies every bipartition or triangle
witness, and checks that every endpoint-mark profile occurs exactly once.

## 5. Explicit minor construction from the triangle

### Lemma 5.1

Let `S` have order eight and put `H=G[S]`.  Suppose `G-S` contains three
distinct components

\[
                         E=\{v,a\},\qquad C_1,\qquad C_2,
\]

where `va` is an edge, `C_1,C_2` are `S`-full, and

\[
        N_G(v)\cap S=S-\{r\},\qquad
        N_G(a)\cap S=S-\{s\},\qquad r\ne s.             \tag{5.1}
\]

If `H-{r,s}` contains a triangle, then `G` contains a `K_7` minor.

#### Proof

Let the triangle be `T={t_1,t_2,t_3}`.  Choose distinct

\[
                  x,y\in S-\{r,s,t_1,t_2,t_3\};
\]

three vertices are available.  The following seven sets are branch sets:

\[
 \{v\},\quad \{a\},\quad C_1\cup\{x\},\quad C_2\cup\{y\},
 \quad \{t_1\},\quad\{t_2\},\quad\{t_3\}.              \tag{5.2}
\]

They are disjoint and connected.  The triangle supplies its three internal
adjacencies.  Fullness makes each enlarged component adjacent to every
triangle singleton and makes the two enlarged components adjacent through,
for example, an edge from `C_1` to `y`.  Both `v` and `a` see
`x,y,t_1,t_2,t_3`, since these five vertices avoid `r,s`; and `va` is an
edge.  Thus all 21 required adjacencies in (5.2) hold. \(\square\)

## 6. Three-component near-full edge closure

### Theorem 6.1

Let `G` satisfy (2.1) and contain no `K_7` minor.  Let `S` have order eight,
and suppose `G-S` has three distinct components

\[
                         E=\{v,a\},\qquad C_1,\qquad C_2
\]

such that:

1. `va` is an edge and `E` is `S`-full;
2. `C_1,C_2` are `S`-full;
3. each of `v,a` misses at most one vertex of `S`; and
4. writing `H=G[S]`,

   \[
    \alpha(H)\le3,
    \qquad K_4\not\preccurlyeq H-Z
          \text{ for every two-set }Z\subseteq S.       \tag{6.1}
   \]

Then this configuration is impossible.

#### Proof

Because `E` is `S`-full, if both endpoints have a miss then the two missed
vertices are distinct.  Apply Lemma 4.1 with `FULL` for a full endpoint and
its unique missed vertex otherwise.

In the first outcome, the two independent sides lie respectively in the
boundary neighbourhoods of `v,a`.  Lemma 2.2 applies to the separation with
open shore `E`, a contradiction.  The second outcome gives two distinct
misses `r,s` and a triangle in `G[S]-{r,s}`.  Lemma 5.1 then gives a `K_7`
minor, again a contradiction. \(\square\)

### Corollary 6.2 (aligned degree-eight application)

Retain the aligned degree-eight setup inside a hypothetical minor-minimal
seven-chromatic graph with no `K_7` minor.  Thus `S=N_G(u)` and
`G-N_G[u]` has exactly two `S`-full components `E,F`.  If one of `E,F` is
a two-vertex edge component whose endpoints each miss at most one boundary
vertex, then the configuration is impossible.

#### Proof

The components of `G-S` include `E`, `F`, and the singleton `{u}`.  The
opposite one of `E,F` and `{u}` are `S`-full, so they supply `C_1,C_2` in
Theorem 6.1.  The low-degree independence bound gives `alpha(G[S])<=3`.
For a two-set `Z={z_1,z_2}`, a `K_4` model in `G[S]-Z`, together with

\[
                       \{u\},\qquad E\cup\{z_1\},
                       \qquad F\cup\{z_2\},
\]

would be an explicit `K_7`-minor model: fullness supplies all contacts and
the two anchors connect the three added branch sets.  Hence (6.1) holds,
and Theorem 6.1 applies. \(\square\)

## 7. Exact gain and limitation

The theorem supersedes the narrower `520`-configuration diagnostic for this
literal aligned three-component host.  It tests the actual `185`-type
compact boundary class and closes every full/full, one-miss, and
distinct-one-miss endpoint profile.  Lemma 3.1 separately replaces the
former computer-assisted proof of the full/full `K_4`-minor-free
consequence.

It does not prove that either aligned component has order two.  When an
aligned full component is an edge, seven-connectivity bounds each endpoint
defect by two and fullness makes the two missed sets disjoint; the theorem
leaves exactly the profiles in which at least one endpoint has defect two.
It does not apply to the primary minimum-boundary case with exactly two full
components: there is only one other component available to supply the two
enlarged branch sets in (5.2).  No operation provenance is used or
preserved, and neither `HC_7` nor the general bounded-interface composition
theorem follows.

## Inputs

- [low-degree boundary and neighbourhood independence bound](hc7_low_degree_adjacent_pair_alignment.md)
- [aligned degree-eight bilateral response cycle](hc7_degree8_aligned_pair_bilateral_cycle.md)
- [four-portal reduction](hc7_degree8_four_portal_reduction.md)
- [active two-vertex-shore contraction laboratory](../active/hc7_two_vertex_shore_bipartite_contraction.md)
- [active near-full diagnostic census](../active/hc7_p2_nearfull_bipartition_census.md)
