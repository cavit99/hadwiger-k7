# A low-codegree edge at every degree-eight vertex in a six-connected graph

**Status:** written proof with one deterministic finite lemma;
[two separate internal audits are GREEN](hc7_k7minus_sixconnected_degree_eight_low_codegree_audit.md).
These are internal mathematical audits, not external peer review.  The verifier is
[`hc7_k7minus_sixconnected_degree_eight_low_codegree_verify.py`](hc7_k7minus_sixconnected_degree_eight_low_codegree_verify.py).
This theorem removes the generic degree-eight row from the six-connected
`4n` extremal programme.  It does not close the returned order-six cut and
therefore does not by itself prove that programme, Conjecture 21, or `HC_7`.

Write `K_t^-` for the graph obtained from `K_t` by deleting one edge.  The
**codegree** of an edge `xy` is

\[
                         c(xy)=|N(x)\cap N(y)|.
\]

## Lemma 1 (the eight-vertex exterior quotient)

Let `J` be a graph on eight vertices with minimum degree at least four and
with no `K_6^-` minor.  Add two nonadjacent vertices `v,c`, make `v`
complete to `J`, and make `c` adjacent to a set `A subseteq V(J)` of order
at least six.  If the resulting graph `Q(J,A)` has no `K_7^-` minor, then,
up to isomorphism, the pair `(J,V(J)-A)` is one of the following four
labelled profiles:

| graph6 code for `J` | the missed pair | degree sequence of `J` |
|---|---|---|
| `GLNM^_` | `5,6` | `4,4,4,4,4,4,4,4` |
| `Gfwhmk` | `0,1` | `4,4,4,4,4,4,5,5` |
| `Gfwhm{` | `0,1` | `4,4,4,4,4,5,5,6` |
| `GxNg~k` | `0,1` | `4,4,4,4,4,6,6,6` |

In particular:

1. `|A|=6`;
2. for each fixed graph `J` in the table, the displayed missed pair is the
   unique two-set whose augmentation is target-free; and
3. the missed pair is an edge of `J`, and both its ends have degree four in
   `J`.

### Finite verification

Every graph on eight vertices occurs by adjoining one vertex in all possible
ways to one of the `1,044` unlabelled order-seven graphs in NetworkX's graph
atlas.  The verifier generates those extensions and retains one member of
each isomorphism class.  The exact counts are

```text
minimum-degree-four extensions             4,443
minimum-degree-four isomorphism classes      424
classes with no K_6^- minor                   55
exterior attachment profiles               2,035
profiles with a certified K_7^- minor       2,031
target-free profiles                            4
```

The `2,035` profiles are the `55` local graphs times all
`1+8+28=37` missed sets of order zero, one, or two.  The four negative
profiles are exactly the four rows above.  For each of the other `2,031`
profiles the verifier returns a branch-set certificate; their sorted digest
is

```text
8b9b31cae19b10a9e958a51dd2c8ef12193b655ec7ab2163b67b638dfc646501
```

The minor search is exact.  It begins with singleton bags and recursively
performs either deletion of a bag or merger of two touching bags.  Every
state therefore consists of disjoint connected bags.  Conversely, every
minor model can be obtained by contracting a spanning tree in each of its
bags and deleting unused vertices.  At six or seven bags the verifier tests
all interbag adjacencies and accepts precisely when at most one pair is
missing.  It separately checks that the missed pair in each negative profile
is unique, is an edge, and has two degree-four ends.  This proves the lemma
within the displayed finite trust boundary.  \(\square\)

## Theorem 2 (six-connected degree-eight low-codegree theorem)

Let `G` be a six-connected graph with no `K_7^-` minor.  If `v` has degree
eight, then some edge `vx` satisfies

\[
                              c(vx)\le3.              \tag{1}
\]

### Proof

Put `J=G[N(v)]`.  Suppose for a contradiction that every edge incident
with `v` has codegree at least four.  For `x in N(v)`,

\[
                         d_J(x)=c(vx),
\]

so `delta(J)>=4`.  The graph `J` has no `K_6^-` minor, since adjoining the
singleton bag `{v}` to such a model would give a `K_7^-` minor in `G`.

First suppose `G-N[v]` is empty.  Six-connectivity gives `delta(G)>=6`,
and hence `delta(J)>=5`.  The eight-vertex complement lemma from the
[degree-eight triangle-poor-edge theorem](hc7_k7minus_degree_eight_triangle_poor_edge_packing.md#lemma-1-the-eight-vertex-complement-lemma)
then gives a `K_6^-` minor in `J`, a contradiction.

Thus `G-N[v]` is nonempty.  Let `C` be any one of its components.  Its
neighbourhood is contained in `N(v)` and separates `C` from `v`, so
six-connectivity gives

\[
                           |N_G(C)|\ge6.              \tag{2}
\]

Contract the connected set `C` to a vertex `c`, delete every other exterior
component, and retain `J` and `v`.  The resulting minor is exactly
`Q(J,N_G(C))` from Lemma 1: the vertices `v,c` are nonadjacent, `v` is
complete to `J`, and `c` has precisely the boundary neighbours of `C`.
Target exclusion and (2) therefore put this quotient in one of the four
rows of Lemma 1.

Fix the unique missed pair `{a,b}` belonging to the resulting graph `J`.
The preceding argument applies to **every** component of `G-N[v]`.  Since
the target-free missed pair is unique for this fixed labelled `J`, every
such component misses both `a` and `b`.  Hence neither vertex has a
neighbour outside `N[v]`.  Lemma 1 gives `d_J(a)=d_J(b)=4`, and consequently

\[
                         d_G(a)=d_G(b)=1+4=5,
\]

contrary to six-connectivity.  This proves (1).  \(\square\)

## Corollary 3 (a universal contraction edge at density `4n`)

Every six-connected `K_7^-`-minor-free graph `G` with

\[
                            |E(G)|\ge4|V(G)|          \tag{3}
\]

has an edge of codegree at most three.

### Proof

Jakobsen's extremal theorem and six-connectivity exclude every four-sum
cockade exception; the two base graphs do not satisfy (3).  Hence a
target-free graph satisfying (3) has average degree less than nine and has
a vertex of degree six, seven, or eight.

If every edge had codegree at least four, the established
[degree-six disk bound](../active/hc7_k7minus_degree6_common_neighbour_bound.md)
would contradict (3) in the degree-six case, whilst the
[saturated degree-seven exclusion](../active/hc7_k7minus_degree7_common_neighbour_exclusion.md)
would exclude the degree-seven case.  Theorem 2 excludes the degree-eight
case.  Thus some edge has codegree at most three.  \(\square\)

## Corollary 4 (a connectivity defect ladder)

Let `G` be an `r`-connected `K_7^-`-minor-free graph with
`r>=6` and `|E(G)|>=4|V(G)|`.  Its Jakobsen defect

\[
                         D(G)=9|V(G)|-2|E(G)|
\]

satisfies

\[
                              D(G)\ge20+r.             \tag{4}
\]

In particular, a six-connected graph has defect at least twenty-six and a
seven-connected graph has defect at least twenty-seven.

### Proof

We first treat `r=6`.  Corollary 3 supplies an edge `e` of codegree at most
three.  The graph `G/e` is at least five-connected, target-free, and still has at
least four times as many edges as vertices.  It is not a nontrivial
Jakobsen cockade, since those have a four-cut, and the two base graphs do
not meet this density.  Jakobsen's strict bound therefore gives

\[
                             D(G/e)\ge25.
\]

If `c=c(e)`, exact contraction accounting gives

\[
                          D(G/e)=D(G)-7+2c.           \tag{5}
\]

Since `c<=3`, this proves `D(G)>=26`.

For `r>=7`, contract the edge supplied by Corollary 3.  The result is
`(r-1)`-connected and retains the coefficient-four density.  Induction and
(5) give

\[
                     D(G)\ge D(G/e)+1
                          \ge20+(r-1)+1=20+r.
\]

This proves (4).  \(\square\)

### Critical-host consequence

In the audited hypothetical minor-minimal non-six-colourable target-free
host, put

\[
 b=n_8,\qquad \tau=\sum_{i\ge10}(i-9)n_i.
\]

The existing minimum-degree and density package gives seven-connectivity,
minimum degree eight, `|E(G)|>=4|V(G)|`, and the degree identity

\[
                              D(G)=b-\tau.
\]

Corollary 4 therefore strengthens the current exceptional-vertex count to

\[
                              b\ge27+\tau.             \tag{6}
\]

This is a necessary condition on a hypothetical critical host, not a
colouring theorem.

## Corollary 5 (the exact returned-cut gate)

Suppose the statement

> every six-connected graph `G` with `|E(G)|>=4|V(G)|` contains a
> `K_7^-` minor

is false, and choose an enemy `G` of minimum order.  Put

\[
                   s=|E(G)|-4|V(G)|\ge0.
\]

There is an edge `uv` of codegree at most three such that `G/uv` is exactly
five-connected and

\[
             |E(G/uv)|\ge4|V(G/uv)|+s.               \tag{7}
\]

Every five-cut of `G/uv` contains the contraction vertex and lifts to an
order-six cut `S` of `G`.  If `D_1,...,D_r` are the components of `G-S` and

\[
 \eta_i=|E(G[D_i])|+|E_G(D_i,S)|-4|D_i|,
\]

then every component is full to `S`, `r in {2,3}`, and

\[
                   |E(G[S])|+\sum_i\eta_i=24+s.      \tag{8}
\]

The only returned rows are

\[
\begin{array}{c|c|c}
r&G[S]&\text{component excess}\\
\hline
2&|E(G[S])|\le11&\eta_1+\eta_2\ge13+s,\\
3&\Delta(G[S])\le3,\ |E(G[S])|\le8&
   \eta_1+\eta_2+\eta_3\ge16+s.
\end{array}                                           \tag{9}
\]

### Proof

Choose the edge from Corollary 3.  Its contraction deletes the edge itself
and at most three duplicates, proving (7).  Edge contraction lowers vertex
connectivity by at most one, so `G/uv` is five-connected.  If it were
six-connected, it would be a smaller enemy.  Hence it is exactly
five-connected.  A five-cut avoiding the contraction vertex would already
be a five-cut in `G`, contradicting six-connectivity.  Thus every five-cut
contains the contraction vertex, and replacing that vertex by `u,v` lifts
the cut to an order-six cut `S`.

The [exact six-cut localisation theorem](hc7_k7minus_exact_six_cut_localisation.md)
gives fullness, the component count and the boundary bounds in (9).
Partitioning the edges over `S` and its components gives (8).  Equivalently,
in the notation of that theorem,

\[
 q_G=|E(G)|-(4|V(G)|-2)=s+2,
\]

so its identity `q_G=|E(G[S])|+sum_i eta_i-22` becomes (8).
The two inequalities in the last column of (9) now follow.  \(\square\)

## Exact scope

Theorem 2 is global and unbounded: the host outside one neighbourhood is
represented only by contracting an arbitrary whole component.  The finite
calculation concerns the resulting ten-vertex quotient, not bounded-order
hosts.

Corollary 3 removes the last local-degree obstruction to a density-preserving
contraction at the `4n` threshold.  Corollary 5 shows precisely why this is
not yet a proof of the broad extremal statement: the contraction can return
a five-cut, and the two high-excess rows in (9) remain open.  Any completion
must compose across that lifted cut or prove that one of its shore
contractions preserves six-connectivity and coefficient-four density.

## Published input

I. T. Jakobsen, *On a certain homomorphism properties of graphs II*,
Mathematica Scandinavica **52** (1983), 229--261,
doi:`10.7146/math.scand.a-12004`.
