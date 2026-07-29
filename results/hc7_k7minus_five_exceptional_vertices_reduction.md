# Density and low-degree rigidity under `K_7^-` exclusion

**Status:** written proof; separate internal audit GREEN for this revision.
This result concerns the proposed `K_7^-` six-colour conjecture.  It proves
neither that conjecture nor `HC_7`.

Here `K_7^-` is `K_7` with one edge deleted.  Throughout, let `G` be a
seven-connected graph satisfying

\[
 \chi(G)=7,
 \qquad
 \text{every proper minor of `G` is six-colourable},
 \qquad
 K_7^-\npreccurlyeq G.                                  \tag{H}
\]

Write `n=|V(G)|`, `m=|E(G)|`, and let `n_i` be the number of
degree-`i` vertices.  Call a degree-eight vertex **exceptional** if it lies
in no literal `K_5`; equivalently, its neighbourhood contains no literal
`K_4`.

## Lemma 1 (exact degree-seven neighbourhood types)

If `v` has degree seven, then `G[N(v)]` is one of

\[
 K_4\mathbin{\dot\cup}K_3,
 \qquad
 K_1\vee(K_3\mathbin{\dot\cup}K_3).                    \tag{1}
\]

In the first case `v` lies in exactly one literal `K_5`, say `L`, and the
three vertices of `N(v)-V(L)` form a triangle anticomplete to
`V(L)-{v}`.

In the second case `v` lies in exactly two literal `K_5`s.  They intersect
in `{v,w}`, where `w` is the universal vertex of `G[N(v)]`.  Relative to
either clique, the three outside neighbours form a triangle adjacent to
`w` and anticomplete to the other three clique vertices.

### Proof

The separately audited
[exact degree-seven neighbourhood theorem](hc7_k7minus_degree7_clique_incidence.md)
gives (1) directly.  The literal `K_4`s in the first graph consist only of
its four-vertex component.  In the second they are the universal vertex
joined to either one of the two triangles.  Adjoining `v` gives exactly the
asserted literal `K_5`s and attachment patterns.
\(\square\)

## Lemma 2 (private-triangle capacity)

Let `L` be a literal `K_5` in `G`.

1. If all five vertices of `L` have degree seven, then `n>=20`.
2. If four vertices have degree seven and each lies in no literal `K_5`
   other than `L`, while the fifth vertex has degree `d>=8`, then

   \[
                              n\ge d+13\ge21.            \tag{2}
   \]

### Proof

First suppose that all five vertices of `L` have degree seven.  No one of
them lies in a second literal `K_5`.  Indeed, Lemma 1 would make that second
clique meet `L` in exactly two vertices, both of degree seven.  Its union
with `L` has order eight; the two shared vertices have no neighbours outside
the union, and the two three-vertex exclusive parts are anticomplete.  If
there is a vertex outside the union, those six exclusive vertices form a
cut, contrary to seven-connectivity.  If there is none, seven-connectivity
forces the eight-vertex graph to be complete, also impossible under (H).

For each `v in V(L)`, Lemma 1 now gives a private triangle
`T_v=N(v)-V(L)`, anticomplete to `L-{v}`.  These five triangles are pairwise
disjoint: if `x in T_v cap T_w`, then `x` is adjacent to `v`, while the
attachment rule for `T_w` says that it is nonadjacent to `v`.  They occupy
fifteen vertices outside `L`, proving `n>=20`.

For the second assertion, the four private triangles similarly occupy
twelve vertices outside `L`.  Every one is anticomplete to the fifth clique
vertex `z`.  The vertex `z` has `d-4` neighbours outside `L`, all outside
those twelve vertices.  Therefore

\[
                 |V(G)-V(L)|\ge12+(d-4),
\]

which is (2).  \(\square\)

## Theorem 3 (density, minimum order, and the first residue)

Every graph satisfying (H) has

\[
                              m\ge4n-5                  \tag{3}
\]

and

\[
                              n\ge19.                   \tag{4}
\]

More exactly, put

\[
 s=\sum_{i\ge9}(i-8)n_i,
 \qquad
 q=n_7-s,
 \qquad
 \varepsilon=10-q.
\]

Then

\[
 2m=8n-q=(8n-10)+\varepsilon,
 \qquad
 0\le\varepsilon\le n-15,                              \tag{5}
\]

and `epsilon` is even.

If `n=19`, the degree sequence is one of

\[
 7^6 8^{13},
 \qquad
 7^7 8^{11}9^1.                                        \tag{6}
\]

In the second case the two literal `K_5`s covering the degree-seven
vertices meet in exactly two vertices: one has degree seven, the other has
degree eight or nine, and all six vertices exclusive to the two cliques
have degree seven.

Finally, if `n_7=10`, then `n>=21`.  In particular the equality layer
`m=4n-5` starts only at order at least twenty-one.

### Proof

The audited
[degree-seven clique-incidence theorem](hc7_k7minus_degree7_clique_incidence.md)
says that every degree-seven vertex lies in a literal `K_5`.  The audited
[three-clique bound](hc7_k7minus_three_clique_bound.md) says that `G` has at
most two literal `K_5`s: the graph is not two-apex because it is
seven-chromatic.  Consequently

\[
                              n_7\le10.                 \tag{7}
\]

Minimum degree is at least seven, so degree summation gives the exact
identity

\[
 2m=7n_7+8(n-n_7)+s=8n-n_7+s=8n-q.                    \tag{8}
\]

Equations (7) and (8) imply (3) and the lower inequality in (5).

Jakobsen's extremal theorem, in the form quoted as Theorem 2 by Albar,
says that an `n`-vertex graph with at least `9n/2-12` edges contains a
`K_7^-` minor or is a `(K_{2,2,2,2},K_6,4)`-cockade.  A nontrivial such
cockade has a separator of order four, while either base graph has chromatic
number at most six.  Thus `G` is not a cockade, and integrality gives

\[
                              2m\le9n-25.               \tag{9}
\]

Combining (8) and (9) yields

\[
 q\ge25-n,
 \qquad
 \varepsilon=10-q\le n-15.
\]

The number `epsilon=2m-(8n-10)` is even.

We next record three consequences of Lemmas 1 and 2:

\[
 n_7=10\Longrightarrow n\ge21,
 \qquad
 n_7=9\Longrightarrow n\ge20,
 \qquad
 n_7=8\Longrightarrow n\ge20.                          \tag{10}
\]

For `n_7=10`, the two literal `K_5`s covering the degree-seven vertices are
disjoint and all their vertices have degree seven.  Lemma 2 first gives
`n>=20`; the improvement to twenty-one is proved below.

For `n_7=9`, the two covering cliques have intersection of order at most
one.  A shared degree-seven vertex would instead force intersection order
two by Lemma 1.  If the cliques meet in one vertex, that vertex has degree
at least eight, leaving room for only eight degree-seven vertices in their
union.  Hence the cliques are disjoint, one contains five degree-seven
vertices, and Lemma 2 gives `n>=20`.

Suppose `n_7=8`.  Let `A,B` be the two covering cliques and put
`r=|A cap B|`.  Since their union contains eight degree-seven vertices,
`r<=2`.

If `r=0`, either one clique contains five degree-seven vertices, or each
contains four.  The first case has order at least twenty by Lemma 2.  In the
second, the four degree-seven vertices of either clique are private and its
fifth vertex has degree at least eight, so Lemma 2 gives order at least
twenty-one.

If `r=1`, the shared vertex is not degree seven by Lemma 1.  Thus each
clique has four private degree-seven vertices, and Lemma 2 again gives
order at least twenty-one.

If `r=2`, all eight vertices in `A union B` have degree seven.  Each shared
vertex is adjacent to the other seven union vertices and hence has no
neighbour outside the union.  Lemma 1 also makes the two three-vertex
exclusive parts anticomplete.  Deleting those six exclusive vertices
separates the shared pair from the nonempty remainder, contrary to
seven-connectivity.  The remainder is nonempty because a seven-connected
graph on eight vertices is `K_8`, forbidden by (H).  This proves (10).

If `n<=18`, then (5) gives `epsilon<=3`.  Since `epsilon` is even,
`epsilon<=2`, and its definition forces `n_7>=8`.  This contradicts (10),
proving (4).

Now let `n=19`.  Equations (5) and parity give
`epsilon in {0,2,4}`.  The first two values force `n_7>=8` and are excluded
by (10).  Thus `epsilon=4`, or

\[
                              n_7-s=6.                  \tag{11}
\]

If `n_7>=8`, (10) again gives a contradiction.  If `n_7<=5`, (11) is
impossible.  Hence either `n_7=6,s=0`, or `n_7=7,s=1`, giving exactly the
two degree sequences in (6).

In the latter case, the two covering cliques cannot cover the seven
degree-seven vertices without a shared degree-seven vertex: otherwise one
clique has at least four private degree-seven vertices and Lemma 2 gives
`n>=21` (or it has five degree-seven vertices and gives `n>=20`).  Lemma 1
then makes their intersection a two-set.  Both shared vertices cannot have
degree seven, because the same six-vertex-cut argument used above would
apply.  Thus exactly one is degree seven; the other six degree-seven
vertices are exclusive to the two cliques.  This proves the description of
the second residue.

It remains to prove the first implication in (10) sharply.  Suppose
`n_7=10` and `n=20`, and call the two disjoint all-degree-seven cliques

\[
 A=\{a_1,\ldots,a_5\},
 \qquad
 B=\{b_1,\ldots,b_5\}.
\]

For `a in A`, the five private triangles from Lemma 2 partition the fifteen
vertices outside `A`.  Hence every vertex outside `A` has exactly one
neighbour in `A`.  The analogous statement holds for `B`, so the edges
between `A` and `B` form a perfect matching; relabel so that they are
`a_i b_i`.

Put `C=V(G)-(A union B)`.  Write

\[
                         T_{a_i}=\{b_i,x_i,y_i\}.
\]

This set is a triangle.  The degree-seven vertex `b_i` therefore has
external neighbourhood exactly `{a_i,x_i,y_i}`, and the five edges
`x_i y_i` form a perfect matching of the ten-vertex graph `G[C]`.  Every
vertex of `C` has exactly two neighbours in `A union B`, so minimum degree
seven gives degree at least five in `G[C]`.  If `G[C]` were disconnected,
every component would have order at least six, impossible on ten vertices.
Thus `G[C]` is connected.

The five singleton branch sets `{a_i}`, together with the connected sets
`B` and `C`, form a `K_7`-minor model: `A` is a clique, the matching joins
every `{a_i}` to `B`, the vertices `x_i,y_i` join every `{a_i}` to `C`, and
`b_i x_i` joins `B` to `C`.  This contradicts (H), and proves
`n>=21` when `n_7=10`.  Equality in (3) forces
`10-n_7+s=0`, hence `n_7=10`, proving the final sentence.  \(\square\)

## Theorem 4 (five exceptional degree-eight vertices)

The graph `G` contains at least five exceptional degree-eight vertices.  In
particular, two of them are nonadjacent.

### Proof

Let `b` be the number of exceptional degree-eight vertices.  From (9),

\[
 25
 \le 9n-2m
 =2n_7+n_8-\sum_{i\ge10}(i-9)n_i
 \le2n_7+n_8.                                          \tag{12}
\]

Every degree-seven vertex and every nonexceptional degree-eight vertex lies
in the union of the at most two literal `K_5`s.  Hence

\[
                         n_7+(n_8-b)\le10.              \tag{13}
\]

Combining (12), (13), and `n_7<=10` gives

\[
                         b\ge n_7+n_8-10
                           \ge15-n_7
                           \ge5.
\]

Five exceptional vertices cannot be pairwise adjacent, since they would
themselves form a literal `K_5`.  \(\square\)

## Corollary 5 (two sufficient finishing theorems)

Either of the following statements would prove that every `K_7^-`-minor-free
graph is six-colourable.

1. Every seven-connected graph with `m>=4n-5` contains a `K_7^-` minor.
2. A graph satisfying (H) has at most four exceptional degree-eight
   vertices.

### Proof

Choose a minor-minimal non-six-colourable `K_7^-`-minor-free graph.  Mader's
contraction-critical connectivity theorem gives (H).  Theorem 3 contradicts
statement 1, while Theorem 4 contradicts statement 2.  \(\square\)

## Published inputs and trust boundary

The density input is Jakobsen's theorem as quoted in Boris Albar,
[*Coloration of `K_7^-`-minor free graphs*](https://arxiv.org/abs/1402.2806),
Theorem 2 and Corollary 4.  The local classification uses the separately
audited computation-free degree-seven neighbourhood theorem cited in
Lemma 1.

Theorem 3 is a reduction to the extremal statement in Corollary 5, not a
proof of that statement.  The order-nineteen description is a structural
laboratory, not a finite reduction of the unbounded conjecture.  No finite
enumeration is used in these proofs.
