# Triangle-poor edges at every degree-eight vertex

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_degree_eight_triangle_poor_edge_packing_audit.md)
for this revision.
The proofs are computation-free.  The retained
[finite verifier](hc7_k7minus_degree_eight_triangle_poor_edge_packing_verify.py)
is an independent cross-check of the order-eight lemmas and includes a
sharp negative calibration.

Here `K_t^-` denotes `K_t` with one edge deleted.  The number of triangles
containing an edge `xy` is `|N(x)\cap N(y)|`.

## Lemma 1 (the eight-vertex complement lemma)

Every graph `J` on eight vertices with minimum degree at least five contains
`K_6^-` as a minor.

### Proof

Put `H=\overline J`, so `\Delta(H)<=2`, and add edges to `H` until it is
edge-maximal subject to having maximum degree at most two.  Call the resulting
graph `H'`.  A graph of maximum degree two is a disjoint union of paths and
cycles.  In `H'`, every path of order at least three is already closed into a
cycle, and vertices of degree less than two cannot lie in two distinct
components, since an edge could then be added between them.  Thus, up to
isomorphism, `H'` is one of

\[
 C_8,\quad C_5\mathbin\dot\cup C_3,\quad
 C_4\mathbin\dot\cup C_4,\quad C_7\mathbin\dot\cup K_1,\quad
 C_4\mathbin\dot\cup C_3\mathbin\dot\cup K_1,\quad
 C_6\mathbin\dot\cup K_2,\quad
 C_3\mathbin\dot\cup C_3\mathbin\dot\cup K_2.        \tag{1}
\]

Indeed, if every component is a cycle, its orders partition eight into parts
of size at least three.  Otherwise the unique component containing deficient
vertices is `K_1` or `K_2`, and the remaining components are cycles.  This
gives exactly the seven graphs in (1).

Since `H` is a subgraph of `H'`, the graph `J'=\overline{H'}` is a spanning
subgraph of `J`.  It remains only to exhibit a `K_6^-` model in `J'`.  Label
each cycle consecutively, using the vertex sets indicated in the first
column.  The following row gives six branch sets; direct inspection shows
that every displayed nonsingleton is connected in `J'` and that at most the
pair stated in the last column is nonadjacent.

\[
\begin{array}{c|c|c}
H'&\text{branch sets in }\overline{H'}&\text{only missing pair}\\
\hline
C_8\ (0,\ldots,7)
 &03,15,2,4,6,7&6\!:\!7\\
C_5(0,\ldots,4)\dot\cup C_3(5,6,7)
 &05,1,26,3,4,7&3\!:\!4\\
C_4(0,\ldots,3)\dot\cup C_4(4,\ldots,7)
 &04,1,25,3,6,7&6\!:\!7\\
C_7(0,\ldots,6)\dot\cup K_1(7)
 &024,1,3,5,6,7&5\!:\!6\\
C_4(0,\ldots,3)\dot\cup C_3(4,5,6)\dot\cup K_1(7)
 &024,1,3,5,6,7&5\!:\!6\\
C_6(0,\ldots,5)\dot\cup K_2(6,7)
 &024,1,3,5,6,7&6\!:\!7\\
C_3(0,1,2)\dot\cup C_3(3,4,5)\dot\cup K_2(6,7)
 &03,14,2,5,6,7&6\!:\!7
\end{array}                                             \tag{2}
\]

For example, `03` denotes the branch set `{0,3}`.  Hence `J'`, and therefore
`J`, contains `K_6^-` as a minor.  \(\square\)

## Theorem 2 (one triangle-poor edge at every degree-eight vertex)

Let `G` be a `K_7^-`-minor-free graph and let `v` have degree eight.  Then
`v` has a neighbour `x` such that

\[
             |N_G(v)\cap N_G(x)|\le4.                 \tag{3}
\]

Equivalently, some edge incident with `v` lies in at most four triangles.

### Proof

Suppose instead that every `x in N_G(v)` has at least five neighbours in
`N_G(v)`.  Then the eight-vertex graph `J=G[N_G(v)]` has minimum degree at
least five.  Lemma 1 supplies six disjoint connected branch sets in `J`
whose quotient contains `K_6^-`.  Adding the singleton branch set `{v}`,
which is adjacent to every one of those six sets, gives a `K_7^-` minor in
`G`, a contradiction.  \(\square\)

## Corollary 3 (simultaneous edge packing)

Let `B` be the set of degree-eight vertices of a `K_7^-`-minor-free graph
`G`.  There is a set `R` of at least `ceil(|B|/2)` distinct edges such that

1. every vertex in `B` is incident with an edge of `R`; and
2. every edge in `R` lies in at most four triangles.

### Proof

For each `v in B`, choose one edge supplied by Theorem 2, and let `R` be the
set of distinct chosen edges.  It covers `B`.  A single edge can be chosen
by at most its two ends, so `|R|>=ceil(|B|/2)`.  \(\square\)

## Corollary 4 (thirteen triangle-poor edges in the global host)

Let `G` be a seven-connected `K_7^-`-minor-free graph with minimum degree at
least eight.  For `i>=8`, let `n_i` be the number of degree-`i` vertices and
put

\[
                    \tau=\sum_{i\ge10}(i-9)n_i.
\]

Then

\[
             n_8\ge25+\tau,                            \tag{4}
\]

and `G` has at least

\[
             \left\lceil\frac{25+\tau}{2}\right\rceil \tag{5}
\]

distinct edges lying in at most four triangles.  These edges may be chosen
to cover every degree-eight vertex.  In particular, there are at least
thirteen such edges.

### Proof

Jakobsen's extremal theorem says that an `n`-vertex graph with at least
`9n/2-12` edges contains `K_7^-` as a minor or is a
`(K_{2,2,2,2},K_6,4)`-cockade.  Neither base graph is seven-connected, and
every nontrivial such cockade has a separator of order four.  Consequently
`G` is not an exceptional cockade.  Strictness and integrality give

\[
                         2|E(G)|\le9|V(G)|-25.          \tag{6}
\]

On the other hand, minimum degree eight gives the exact degree identity

\[
 2|E(G)|=8n_8+9n_9+\sum_{i\ge10}i n_i
         =9|V(G)|-n_8+\tau.                            \tag{7}
\]

Combining (6) and (7) proves (4).  Corollary 3 now gives at least
`ceil(n_8/2)`, and hence at least the number in (5), distinct triangle-poor
edges covering all degree-eight vertices.  \(\square\)

## Lemma 5 (rooted deletion in an exceptional neighbourhood)

Let `J` be a graph on eight vertices such that

\[
             \delta(J)\ge4,\qquad K_4\not\subseteq J,
             \qquad \alpha(J)=3.                       \tag{8}
\]

Call a vertex `r` **good** when `J-r` contains `K_5^-` as a minor.  Every
vertex of `J` has a good neighbour.

### Proof

We first show that `J` is three-connected.  A component has order at least
five, and a component behind a cutvertex has order at least four, so neither
a disconnection nor a cutvertex is possible on eight vertices.  If a
two-cut `S` existed, the six remaining vertices would split into two
three-vertex components.  Minimum degree four would make each component a
triangle complete to `S`.  If `S` contained an edge, this would give a
literal `K_4`; if not, the resulting graph would have independence number
two.  Both alternatives contradict (8).

Suppose first that `J` is four-connected.  Fix `r`.  Then `J-r` is
three-connected.  Wood and Woodall's classification says that a
three-connected `K_5^-`-minor-free graph is a wheel, the triangular prism,
or `K_{3,3}`.  If `r` is not good, order seven forces `J-r` to be a wheel
with a six-vertex rim.  Every rim vertex has degree three in `J-r`, so it is
adjacent to `r`.  The hub is not adjacent to `r`, since otherwise the hub,
`r`, and the ends of a rim edge would form a `K_4`.  Hence

\[
                         J=\overline{K_2}\vee C_6.       \tag{9}
\]

In (9), every rim vertex is good.  Indeed, with apices `p,q` and cyclic rim
`v_0,\ldots,v_5`, after deleting `v_2` the five sets

\[
             \{p,v_0\},\ \{q,v_1\},\ \{v_3\},\
             \{v_4\},\ \{v_5\}                       \tag{10}
\]

form a `K_5^-` model; the only missing pair is
`\{v_3\}:\{v_5\}`.  Cyclic symmetry handles every rim vertex.  The six rim
vertices totally dominate (9).  Thus either every vertex is good, or (9)
holds and the good rim vertices still meet the neighbourhood of every
vertex.

It remains to consider `\kappa(J)=3`.  Let `S` be a three-cut.  Every
component of `J-S` has order at least two, so there are exactly two, of
orders two and three.  Write the former as `A=\{a,a'\}` and the latter as
`B`.  Minimum degree four makes `aa'` an edge and makes both vertices of
`A` complete to `S`.  The set `S` is independent, since an edge of `J[S]`
together with `A` would be a `K_4`.  Every vertex of `B` has a neighbour in
`B`, so `J[B]` is either a three-vertex path or a triangle.

In the branch-set displays (11)--(15), juxtaposition denotes the set of the
displayed vertices; singleton branch sets are written as single letters.

First let `B=b_1b_2b_3` be a path.  Its ends are complete to `S`, and the
middle vertex sees at least two vertices of `S`.  Choose distinct
`s_1,s_2,s_3 in S`, with `b_2s_3` present.  After deleting `a`, the sets

\[
       b_1s_1,\quad b_3s_2,\quad b_2,\quad a',\quad s_3  \tag{11}
\]

form a `K_5^-` model, missing only `b_2:a'`.  Hence both vertices of `A`
are good.  Deleting an end, say `b_1`, gives the same conclusion from

\[
       as_1,\quad b_3s_2,\quad b_2,\quad a',\quad s_3,   \tag{12}
\]

where `s_1,s_3` are chosen among the at least two neighbours of `b_2` in
`S`.  Finally, after deleting `b_2`, the sets

\[
       as_1,\quad b_1s_2,\quad b_3,\quad a',\quad s_3   \tag{13}
\]

again miss only `b_3:a'`.  Thus every vertex of `A\cup B` is good.

Now let `B` be a triangle.  Every vertex of `B` sees at least two vertices
of `S`.  No vertex of `S` sees all of `B`, since that would make a `K_4`.
The missing incidences between `B` and `S` consequently form a perfect
matching; label them `b_is_i` for `i=1,2,3`.  After deleting `a`, the sets

\[
       s_1b_2,\quad s_2a',\quad b_1,\quad s_3,\quad b_3 \tag{14}
\]

form a `K_5^-` model, missing only `s_3:b_3`.  After deleting `b_1`, use

\[
       s_1b_2b_3,\quad s_2,\quad s_3,\quad a,\quad a',  \tag{15}
\]

whose only missing pair is `s_2:s_3`.  Symmetry again shows that every
vertex of `A\cup B` is good.

In either three-cut case, a vertex of `A` has the other good vertex of `A`
as a neighbour, every vertex of `B` has a good neighbour in `B`, and every
vertex of `S` is adjacent to both good vertices of `A`.  The good vertices
therefore totally dominate `J`.  \(\square\)

## Theorem 6 (one almost-full exterior component is terminal)

Let `J` satisfy (8).  Add a vertex `z` adjacent to every vertex of `J` and
a further vertex `c` adjacent to at least seven vertices of `J`.  No
adjacency between `z` and `c` is required.  The resulting graph contains
`K_7^-` as a minor.

### Proof

If `c` misses a vertex of `J`, call it `x`; otherwise choose `x` arbitrarily.
By Lemma 5, `x` has a good neighbour `r`.  In particular, `cr` is an edge.
Let `M_1,\ldots,M_5` be a `K_5^-` model in `J-r`.

Use the seven branch sets

\[
                       \{z\},\quad \{c,r\},\quad
                       M_1,\ldots,M_5.                  \tag{16}
\]

The first two are adjacent through `zr`.  The vertex `z` sees every
`M_i`.  The set `\{c,r\}` also sees every `M_i`: the only possible failure
of a `c`-edge is when `M_i=\{x\}`, and then the edge `rx` is present.  The
five remaining sets have at most one missing pair.  Thus (16) is a
`K_7^-` model.  \(\square\)

## Corollary 7 (a three-triangle edge at an exceptional centre)

Let `G` be seven-connected and `K_7^-`-minor-free.  Suppose that `v` has
degree eight and

\[
              K_4\not\subseteq G[N(v)],\qquad
              \alpha(G[N(v)])=3.                       \tag{17}
\]

Then `v` has a neighbour `x` such that

\[
                    |N_G(v)\cap N_G(x)|\le3.            \tag{18}
\]

### Proof

Put `J=G[N(v)]` and suppose that `\delta(J)\ge4`.  If
`G-N[v]` is empty, seven-connectivity gives `\delta(J)\ge6`; Lemma 1 then
gives a `K_6^-` minor in `J`, which `v` completes to `K_7^-`.

Otherwise choose a component `C` of `G-N[v]`.  Its neighbourhood is a
separator contained in `N(v)`, so seven-connectivity gives
`|N_G(C)|\ge7`.  Contract `C` to `c` and delete all other exterior vertices.
The retained minor consists of `J`, the vertex `v` complete to `J`, and a
vertex `c` adjacent to at least seven vertices of `J`.  Theorem 6 gives a
`K_7^-` minor, a contradiction.  Hence `\delta(J)\le3`.  Since

\[
              |N_G(v)\cap N_G(x)|=d_J(x)
              \qquad(x\in N_G(v)),
\]

(18) follows.  \(\square\)

## Corollary 8 (the Jakobsen defect is at least twenty-six)

Let `G` be a seven-connected `K_7^-`-minor-free graph with minimum degree
at least eight.  Suppose every degree-eight vertex satisfies (17).  Put

\[
 b=n_8,\qquad \tau=\sum_{i\ge10}(i-9)n_i,
 \qquad D=b-\tau=9|V(G)|-2|E(G)|.                      \tag{19}
\]

Then

\[
                         D\ge26,\qquad b\ge26+\tau.    \tag{20}
\]

Moreover, `G` has a set `R` of at least

\[
                         \left\lceil\frac{26+\tau}{2}\right\rceil
                                                                  \tag{21}
\]

distinct edges covering all degree-eight vertices, each lying in at most
three triangles.

### Proof

The degree identity in (19) is immediate from `\delta(G)\ge8`.  Applying
Jakobsen's theorem to `G` first gives `D\ge25`; seven-connectivity excludes
both base cockades and every nontrivial four-sum.  Hence
`b=D+\tau\ge25+\tau`, so degree-eight vertices exist and `|V(G)|\ge25`.

For an edge `e=xy`, put `c(e)=|N(x)\cap N(y)|`.  The contraction `G/e` is
six-connected: a cut of order at most five would lift to a cut of order at
most six in `G`, replacing the contracted vertex by `x,y` when necessary.
It remains target-free, has order at least twenty-four, and is not a
Jakobsen cockade.  Since

\[
             |E(G/e)|=|E(G)|-1-c(e),
\]

Jakobsen's strict bound for `G/e` gives

\[
 2\bigl(|E(G)|-1-c(e)\bigr)
       \le9\bigl(|V(G)|-1\bigr)-25.
\]

Using (19) and rearranging yields

\[
                              D+2c(e)\ge32.             \tag{22}
\]

Choose a degree-eight vertex `v`.  Corollary 7 gives an incident edge `e`
with `c(e)\le3`; (22) proves `D\ge26` and hence (20).

Finally choose one edge given by Corollary 7 at every degree-eight vertex
and retain the distinct choices.  One edge covers at most two such vertices,
so the resulting set has order at least `ceil(b/2)`.  Equations (20) and
(21) follow.  \(\square\)

The audited critical-host reductions used elsewhere in this repository
give exactly the hypotheses of Corollary 8: minimum degree eight, no literal
`K_5`, and independence number three in every degree-eight neighbourhood.
Thus a hypothetical minor-minimal non-six-colourable target-free graph has
Jakobsen defect at least twenty-six; the former equality case `D=25` is
eliminated.

## Sharpness and scope

The constant four in Theorem 2 cannot be lowered without an additional
hypothesis.  Let `J=C_8^2`, the graph on `Z_8` in which two vertices are
adjacent when their cyclic distance is one or two, and let `G_0=K_1\vee J`
with apex `v`.  The graph `J` is the planar square-antiprism graph and is
four-regular.  Hence `d_{G_0}(v)=8`, and every edge `vx` lies in exactly four
triangles.

The graph `G_0` has no `K_7^-` minor.  A model avoiding `v` would lie in the
planar graph `J`.  If `v` belongs to one branch set, deleting that branch set
would leave a `K_6` or `K_6^-` minor in `J`, according as the unique missing
edge of the target is or is not incident with the deleted branch set.  Both
possibilities contradict planarity.  This example has connectivity five,
so it establishes sharpness of Theorem 2, not of its seven-connected
specialisation.

The minimum-degree-four hypothesis in Lemma 5 and Theorem 6 is sharp for
that quotient statement.  The verifier records the cubic graph with graph6
code ``GMs`KK``; it is `K_4`-free with independence number three, yet adjoining
two nonadjacent vertices both complete to it produces no `K_7^-` minor.
Thus the same one-component quotient cannot by itself force an edge in at
most two triangles.

Corollary 8 eliminates the full Jakobsen-defect equality layer `D=25` and
gives a simultaneous packing of edges in at most three triangles.  It does
not prove the `4n-2` extremal target, Conjecture 21, the `K_7^-`
six-colour conjecture, or `HC_7`.  It remains below the Norin--Totschnig
benchmark: this is a global structural and extremal reduction, not a
colouring theorem or a complete extremal classification.

## Published input

I. T. Jakobsen, *On a certain homomorphism properties of graphs II*,
Mathematica Scandinavica **52** (1983), 229--261,
doi:`10.7146/math.scand.a-12004`.  The exact threshold and cockade exception
are also quoted as Theorem 2 in B. Albar, *Coloration of
`K_7^-`-minor free graphs*, arXiv:1402.2806.

R. G. Wood and D. R. Woodall, *Defective Choosability of Graphs without
Small Minors*, Electronic Journal of Combinatorics **16** (2009), R92,
Lemma 4.2.1, doi:`10.37236/181`.  That lemma states exactly that every
three-connected `K_5^-`-minor-free graph is a wheel, the triangular prism,
or `K_{3,3}`.
