# Seven-cut component contraction under `K_7^-` exclusion

**Status:** written proof; separate internal audit GREEN.  This is a
structural theorem for seven-connected `K_7^-`-minor-free graphs.  It does
not prove the current extremal `4n-4` target, the stronger `4n-5` benchmark,
the `K_7^-` six-colour conjecture, or `HC_7`.

## Theorem 1

Let `G` be a seven-connected graph with no `K_7^-` minor.  Let `S` be a
vertex cut of order seven, and let

\[
                         C_1,\ldots,C_r
\]

be the components of `G-S`.  Then

\[
 N_G(C_i)=S\quad(1\le i\le r),
 \qquad
 2\le r\le5,                                            \tag{1}
\]

and

\[
                         \kappa(G[S])\le6-r.             \tag{2}
\]

There are four sharper conclusions:

1. if `r=2`, then `G[S]` has no `K_5` minor;
2. if `r=3`, then `G[S]` has at most nine edges;
3. if `r=4`, then `G[S]` has maximum degree at most one;
4. if `r=5`, then `G[S]` is edgeless.

## Proof

Since \(N_G(C_i)\subseteq S\) and another component lies outside `C_i`, a
proper subset of `S` containing `N_G(C_i)` would be a vertex cut of order at
most six.  Thus every component is adjacent to all of `S`, proving the
first part of (1).

Contract each `C_i` to one vertex `c_i`.  The resulting minor is

\[
                    J=I_r\vee G[S],                     \tag{3}
\]

where `I_r={c_1,...,c_r}` is an independent set.  We first prove a finite
claim.

### Claim 2

Let `R` be a graph on seven vertices and `r>=2`.  If \(I_r\vee R\) is
seven-connected, then it contains a `K_7^-` minor.

### Proof of Claim 2

Write the vertices of `I_r` as **apices** only within this proof.

If `r=2`, seven-connectivity forces `R` to be five-connected.  Hence
`|E(R)|>=18`.  Mader's sharp `K_5`-minor bound permits at most
`3|V(R)|-6=15` edges in a `K_5`-minor-free graph.  A `K_5` model in `R`,
together with the two singleton apices, is a `K_7^-` model whose only
missing adjacency is between those two singletons.

Let `r=3`.  Now `R` is four-connected, so `|E(R)|>=14`.  A `K_5` model
again finishes immediately with two singleton apices.  Otherwise Mader's
bound gives `|E(R)|<=15`.

If `|E(R)|=14`, then `R` is four-regular.  Its complement is either `C_7`
or `C_3 dotcup C_4`.  In the first case label the complement cycle
cyclically by `0,...,6`; in the second label the triangle by `0,1,2` and
the four-cycle cyclically by `3,4,5,6`.  In either case

\[
       \{0,3\},\quad \{1,5\},\quad \{2\},\quad
       \{4\},\quad \{6\}                               \tag{4}
\]

are five pairwise adjacent connected branch sets in `R`, a `K_5` model.

It remains that `|E(R)|=15`.  Summing `|E(R-{x,y})|` over the 21 unordered
pairs `{x,y}` counts each edge ten times, for a total of 150.  Some pair
therefore leaves at least eight edges.  Mader's sharp `K_4`-minor bound is
`2|V|-3=7` on five vertices, so `R-{x,y}` has a `K_4` model.  If the three
apices are `a,b,c`, then

\[
                 \{a\},\quad \{b,x\},\quad \{c,y\}
\]

together with those four branch sets form a `K_7` model.

Let `r=4`.  The graph `R` is three-connected and has minimum degree at
least three.  It has a cycle of length at most five: otherwise a
breadth-first count from an edge in a graph of girth at least six would
require at least

\[
                              2+4+8=14
\]

vertices.  Choose distinct vertices `x,y` outside a shortest such cycle.
Contract the cycle to three pairwise adjacent branch sets.  Use two
singleton apices, and merge the other two apices with `x` and `y`.  These
are seven branch sets with every required adjacency except possibly the
one between the two singleton apices.

Let `r=5`.  The graph `R` is two-connected, so choose an edge `xy` and
three further vertices `z_1,z_2,z_3`.  Use two singleton apices, merge the
other three apices respectively with the `z_i`, and retain `{x}` and `{y}`.
Again only the pair of singleton apices may be nonadjacent.

Finally, if `r>=6`, choose six apices and five boundary vertices.  Keep two
apices as singletons, merge four with four of the boundary vertices, and
retain the fifth boundary vertex as a singleton.  This construction is a
`K_7^-` model regardless of the edges of `R`.  This proves Claim 2.
\(\square\)

### Claim 3

Every graph on seven vertices with at least ten edges contains, as a not
necessarily induced subgraph, `K_4^-`, the house graph, or `K_{2,3}`.
Here the house graph is obtained from a four-cycle by adjoining one vertex
adjacent to the ends of one cycle edge.

### Proof of Claim 3

Suppose that `Q` contains none of the three graphs.  Choose a vertex `v` of
maximum degree `d`, and put

\[
                  A=N_Q(v),\qquad B=V(Q)-N_Q[v].
\]

The graph `Q[A]` is a matching: if one vertex of `A` had two neighbours in
`A`, those three vertices together with `v` would contain `K_4^-`.
Moreover, every vertex of `B` has at most two neighbours in `A`; three such
neighbours together with `v` would give `K_{2,3}`.

If `d>=5`, these observations give

\[
 |E(Q)|
 \le d+\left\lfloor\frac d2\right\rfloor
       +2(6-d)+\binom{6-d}{2}
 \le9.                                                  \tag{5}
\]

If `d<=2`, then `|E(Q)|<=7`.  It remains to consider `d=3,4`.

Let `d=4`, write `B={p,q}`, and put

\[
 \alpha=|E(Q[A])|,
 \quad x=|E_Q(A,B)|,
 \quad \beta=|E(Q[B])|.
\]

Here `alpha<=2`, `x<=4`, and `beta<=1`.  If `alpha=2`, ten edges force one
of `p,q` to have two neighbours in `A`.  If they are the ends of one
matching edge, there is a `K_4^-`; if they lie on different matching edges,
there is a house.  If `alpha<=1`, ten edges force equality

\[
                    (\alpha,x,\beta)=(1,4,1).
\]

Let `ab` be the unique edge of `Q[A]` and let `c,t` be the two isolated
vertices of `Q[A]`.  A two-element `A`-neighbourhood using `a` or `b`
creates `K_4^-` or a house with `v`.  Thus both `p` and `q` see exactly
`{c,t}`; the edge `pq` then completes a `K_4^-` on `{p,q,c,t}`.

Now let `d=3`.  Maximum degree gives `|E(Q)|<=10`, so equality holds.  With
the same notation,

\[
                       \alpha+x+\beta=7,
 \qquad \alpha\le1.                                    \tag{6}
\]

If `alpha=1`, a vertex of `B` with two `A`-neighbours again creates
`K_4^-` or a house.  Hence `x<=3`, and (6) forces `x=beta=3`.  The graph
`Q[B]` is a triangle.  Its three edges to `A` have distinct ends in `A`,
since a repeated end gives `K_4^-`; the unique edge of `Q[A]`, its two
matched vertices in `B`, and `v` form a house.

It remains that `alpha=0`.  If `beta=3`, degree capacity in the triangle
`Q[B]` gives `x<=3`, contrary to (6).  If `beta=2`, write the path in `B`
as `p-q-r`.  Equation (6) forces cross-degrees `2,1,2`.  Equal
`A`-neighbourhoods of `p,r` give `K_{2,3}`.  If those two-element
neighbourhoods are distinct, the neighbour of `q` is either their common
vertex, giving `K_4^-`, or one of their two distinct vertices, giving a
house.

If `beta=1`, all three vertices of `B` have two neighbours in `A`.
Repeated two-element neighbourhoods give `K_4^-` or `K_{2,3}`, so after
labelling the sole edge of `Q[B]` as `pq` and `A={a,b,c}`, we may write

\[
 N_A(p)=\{a,b\},\quad N_A(q)=\{a,c\},\quad
 N_A(r)=\{b,c\}.
\]

The cycle `a-v-b-p-a` with roof `q` is a house.  Finally, `beta=0` would
force `x=7`, although `x<=6`.  Every case is contradictory, proving the
claim.  \(\square\)

For completeness,

\[
                  \kappa(I_r\vee R)=
                  \min\{7,r+\kappa(R)\}.                \tag{7}
\]

Indeed, a cut of order below seven must delete all `r` independent
vertices and then disconnect `R`; deleting all seven vertices of `R` gives
the other cut.

The graph `J` in (3) has no `K_7^-` minor.  The construction for `r>=6`
therefore gives `r<=5`.  By Claim 2, `J` is not seven-connected.  Equation
(7) now gives `r+\kappa(G[S])<=6`, which is (2).

If `r=2`, a `K_5` model in `G[S]` together with `c_1,c_2` would be a
`K_7^-` model.

If `r=3` and `G[S]` has at least ten edges, Claim 3 supplies one of its
three subgraphs.  A literal `K_4^-` uses four boundary vertices; merge the
three contracted components with the other three boundary vertices, and
retain those four vertices as singletons.  These seven bags form a
`K_7^-` model.

The house and `K_{2,3}` each have a `K_4^-` minor on their five vertices:
contract the square edge opposite the roof in the house, or any edge of
`K_{2,3}`.  Use one contracted component as a singleton, merge the other
two with the two unused boundary vertices, and retain the four
`K_4^-` branch sets.  This again gives `K_7^-`.  Hence
`|E(G[S])|<=9` when `r=3`.

If `r=4` and `G[S]` contains a path `x-y-z`, choose three further boundary
vertices `p,q,t` and write the four contracted component vertices as
`a,b,c,d`.  The seven branch sets

\[
 \{a\},\quad \{b,p\},\quad \{c,q\},\quad \{d,t\},
 \quad \{x\},\quad \{y\},\quad \{z\}
\]

have every pairwise adjacency except possibly `{x}--{z}`.  Thus no such
path exists, and `G[S]` has maximum degree at most one.

If `r=5`, any boundary edge can play the role of `xy` in the explicit
`r=5` construction, so no such edge exists.  These prove the four sharper
conclusions.  \(\square\)

## Published input and scope

The only external input is the `p=4,5` cases of Mader's sharp minor
extremal theorem: a `K_p`-minor-free graph has at most

\[
                    (p-2)n-\binom{p-1}{2}
\]

edges.  The primary source is W. Mader,
*Homomorphiesätze für Graphen*, Mathematische Annalen **178** (1968),
154--168.  Every other minor in the proof is given by explicit branch sets.

The theorem identifies what must fail when components behind an exact
seven-cut are contracted.  It does not show that contracting an arbitrary
connected subgraph preserves seven-connectivity, and it does not provide a
strict recursive descent by itself.  In particular, it proves neither the
current global `4n-4` extremal target nor the stronger `4n-5` benchmark.
