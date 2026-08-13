# Linear seven-removable matchings in the critical host

**Status:** written proof.  A separate internal audit is adjacent in
[`hc7_k7minus_linear_removable_matching_audit.md`](hc7_k7minus_linear_removable_matching_audit.md).
This theorem does not prove the `K_7^-` six-colour conjecture or `HC_7`.

The result combines the critical-host degree defect with the audited
five-edge removable-matching theorem.  Its main point is global: a
hypothetical counterexample has a linearly large matching whose simultaneous
deletion preserves seven-connectivity, and all nonempty equality signatures
on that matching occur on one common graph.

## 1. Setting

Let `G` be a minor-minimal non-six-colourable graph with no `K_7^-` minor.
Write

\[
 n=|V(G)|,\qquad m=|E(G)|,
\]

and, for `i>=8`, let `n_i` denote the number of vertices of degree `i`.  Put

\[
             \tau=\sum_{i\ge10}(i-9)n_i.              \tag{1.1}
\]

The audited critical-host theorem gives

\[
 \chi(G)=7,\qquad \kappa(G)\ge7,\qquad \delta(G)\ge8,
 \qquad K_5\not\subseteq G,
 \qquad n_8\ge25+\tau.                                \tag{1.2}
\]

Consequently

\[
\begin{aligned}
 2m
   &=8n_8+9n_9+\sum_{i\ge10}i n_i\\
   &=9n-n_8+\tau\\
   &\le9n-25.                                         \tag{1.3}
\end{aligned}
\]

We use two audited inputs.

1. `G` has a matching of order five whose deletion leaves a
   seven-connected graph.
2. Mader's critical-cycle theorem: if every edge of a cycle in a
   `k`-connected graph is critical for `k`-connectivity, then the cycle
   contains a vertex of degree `k`.

## 2. Feedback vertex sets are linearly large

### Lemma 2.1 (five-chromatic `K_5`-free graphs have at least sixteen edges)

Let `J` be a `K_5`-free graph with `chi(J)>=5`.  Then

\[
                         |E(J)|\ge16.                 \tag{2.1}
\]

#### Proof

Choose an induced subgraph of `J` which is vertex-minimal subject to having
chromatic number at least five, and continue to denote it by `J`.  Put
`s=|V(J)|`.  Then

\[
                         \chi(J)=5,\qquad \delta(J)\ge4. \tag{2.2}
\]

The graph has at least seven vertices.  For `s=5` it would be `K_5`.  For
`s=6`, (2.2) makes the complement a matching.  At most one complementary
edge leaves a literal `K_5`, while two complementary edges and the two
remaining singleton vertices give a four-colouring.

If `s>=8`, (2.2) gives `|E(J)|>=2s`.  Equality would make `J` a connected
four-regular five-chromatic graph, contrary to Brooks' theorem.  Hence
`|E(J)|>=2s+1>=17`.

It remains that `s=7`.  The degree bound gives at least fourteen edges.
Equality again contradicts Brooks' theorem.  If there are fifteen edges,
the degree sequence is either

\[
 (6,4,4,4,4,4,4)
 \quad\hbox{or}\quad
 (5,5,4,4,4,4,4).                                    \tag{2.3}
\]

In the first case, deleting the universal vertex leaves a cubic
four-chromatic graph.  Brooks' theorem gives a `K_4` component, which
together with the universal vertex is a `K_5`.

In the second case, the complement has degree sequence
`(1,1,2,2,2,2,2)`.  It is one of

\[
 P_7,\qquad P_2\mathbin{\dot\cup}C_5,\qquad
 P_3\mathbin{\dot\cup}C_4,\qquad
 P_4\mathbin{\dot\cup}C_3.
\]

Each has a matching of order three.  The corresponding three nonedges of
`J`, together with the remaining singleton, give a four-colouring.  Thus
fifteen edges are also impossible, proving (2.1). `\square`

### Theorem 2.2 (linear feedback-vertex lower bound)

Every feedback vertex set `T` of `G` satisfies

\[
             |T|\ge
             \left\lceil\frac{5n+59}{14}\right\rceil. \tag{2.4}
\]

More precisely, suppose that `R=G-T` is nonempty.  Put

\[
 t=|T|,\quad r=|R|,\quad
 c=\text{the number of components of }R,\quad
 e_T=|E(G[T])|,
\]

and

\[
             D_R=\sum_{x\in R}(d_G(x)-8)\ge0.         \tag{2.5}
\]

Then

\[
             5r+2e_T+2c+2D_R\le9t-25.                \tag{2.6}
\]

#### Proof

If `R` is empty, then `t=n`, and (2.4) follows from `n>=25`.  Assume that
`R` is nonempty.  Since `R` is a forest,

\[
                         |E(R)|=r-c.                  \tag{2.7}
\]

Colouring `G[T]` and the forest `R` with disjoint palettes gives

\[
                         \chi(G[T])\ge5.              \tag{2.8}
\]

The graph `G[T]` is `K_5`-free by (1.2), so Lemma 2.1 gives

\[
                         e_T\ge16.                    \tag{2.9}
\]

Degree summation over `R`, using (2.5) and (2.7), gives

\[
 |E(T,R)|
   =8r+D_R-2(r-c)
   =6r+2c+D_R.                                        \tag{2.10}
\]

Consequently

\[
                         m=e_T+7r+c+D_R.              \tag{2.11}
\]

Substitute (2.11) into (1.3), with `n=t+r`.  This gives (2.6).  Since
`c>=1`, equations (2.6) and (2.9) imply

\[
                         5r+34\le9t-25.
\]

Using `r=n-t` yields

\[
                         5n+59\le14t,
\]

which is (2.4). `\square`

### Remark 2.3 (a sharper internal-edge estimate)

In the notation of Theorem 2.2 one also has

\[
                         e_T\ge\max\{16,34-r\}.       \tag{2.12}
\]

Indeed, every degree-eight vertex of `T` has at least two neighbours in
`T`.  Otherwise it has at least seven neighbours in the forest `R`, which
contain an independent four-set.  Contracting the four-edge star from the
vertex to that set and expanding a six-colouring gives a missing colour at
the centre and hence a six-colouring of `G`.

Let `J` be the critical subgraph used in Lemma 2.1, of order `s`.  At most
`n-n_8<=n-25` vertices of `G` have degree different from eight.  Hence at
least

\[
                         \max\{0,25-r-s\}
\]

vertices of `T-V(J)` have degree eight.  Their degree sum in `G[T]` is at
least twice their number, so they contribute at least that many edges not
internal to `J`.  Combining this with the bounds in Lemma 2.1 gives
(2.12).

The sharper estimate is not needed for (2.4), but records the exact
strength left by the degree-eight count.

## 3. A linearly large seven-removable matching

Call a matching `M` **seven-removable** when `G-M` is seven-connected.

### Theorem 3.1 (linear removable matching)

The graph `G` has a seven-removable matching `M` satisfying

\[
              |M|\ge
              \left\lceil\frac{5n+59}{28}\right\rceil. \tag{3.1}
\]

It may be chosen so that `V(M)` is a feedback vertex set.  In particular,

\[
                              |M|\ge7.                 \tag{3.2}
\]

#### Proof

The audited removable-matching theorem supplies a seven-removable matching
of order five.  Starting from it, choose an inclusion-maximal
seven-removable matching `M`, and put

\[
                              X=G-M.                   \tag{3.3}
\]

Suppose that `G-V(M)` contains a cycle `C`.  Every vertex of `C` is
disjoint from the matching, so no edge of `M` is incident with it.  Hence

\[
                              d_X(x)=d_G(x)\ge8
                              \qquad(x\in V(C)).        \tag{3.4}
\]

If `X-f` failed to be seven-connected for every edge `f` of `C`, all edges
of `C` would be critical for seven-connectivity in the seven-connected
graph `X`.  Mader's critical-cycle theorem would then give a vertex of
`C` of degree seven in `X`, contrary to (3.4).  Thus some edge `f` of
`C` satisfies that `X-f` is seven-connected.  The edge `f` is disjoint
from every edge of `M`, so `M\cup\{f\}` is a larger seven-removable
matching, a contradiction.

Therefore `G-V(M)` is a forest, and `V(M)` is a feedback vertex set.
Theorem 2.2 gives

\[
                         2|M|=|V(M)|
                            \ge\left\lceil\frac{5n+59}{14}\right\rceil.
\]

Since `|M|` is an integer, this implies (3.1).  Finally `n>=25`, so the
right side of (3.1) is at least seven. `\square`

### Theorem 3.2 (complete punctured response cube)

Let `M` be any nonempty matching in `G`.  If `G-M` is considered as the
common deletion graph, then

\[
 \{\Sigma_M(c):c\text{ is a proper six-colouring of }G-M\}
                         =2^M-\{\varnothing\},         \tag{3.5}
\]

where

\[
                 \Sigma_M(c)=\{xy\in M:c(x)=c(y)\}.   \tag{3.6}
\]

In particular, (3.5) holds for the matching in Theorem 3.1.

#### Proof

Fix a nonempty subset `J` of `M`.  Contract every edge in `J` and
six-colour the resulting proper minor.  Expand every contraction class and
restrict the colouring to `G-M`.  The ends of every edge in `J` have equal
colours.

Every edge of `M-J` remains between two distinct contraction classes
because `M` is a matching.  Every edge of `G-M` also remains between
distinct classes: the only two vertices in one contraction class are the
ends of one matching edge, and the graph is simple.  Thus the expanded
colouring is proper on `G-M` and has signature exactly `J`.

An empty signature would remain proper after every edge of `M` was
restored and would six-colour `G`.  Hence it does not occur. `\square`

## 4. Seven-coordinate exact-model consequences

Choose any seven-edge submatching `N` of the matching in Theorem 3.1 and
put

\[
                              H=G-N.                   \tag{4.1}
\]

### Corollary 4.1 (one global seven-coordinate host)

The graph `H` is seven-connected and satisfies

\[
 |E(H)|\ge4|V(H)|-7,                                  \tag{4.2}
\]

while its matching signatures are exactly

\[
                              2^N-\{\varnothing\}.      \tag{4.3}
\]

Moreover, `H` has a spanning exact `K_7^\vee`-minor model: it may be
labelled

\[
                         P,B,C,U_1,U_2,U_3,U_4,        \tag{4.4}
\]

where the only absent branch-set adjacencies are `PB` and `PC`, and both
pairs remain anticomplete after all seven matching edges are restored.

#### Proof

The graph `H` contains the seven-connected spanning graph `G-M`, so it is
seven-connected.  The density bound follows from `|E(G)|>=4|V(G)|`.
Equation (4.3) is Theorem 3.2.

Norin--Totschnig's density theorem applies to (4.2), and its small
exception is excluded by `n>=25`.  Absorb unused components into adjacent
branch sets to make the model spanning.  If either nominally absent pair
became adjacent after the matching edges were restored, the seven branch
sets would contain a `K_7^-` model.  Target exclusion therefore makes
(4.4) exact in `G`. `\square`

### Theorem 4.2 (target or an original-coordinate response separator)

Let `N` be any submatching of the matching in Theorem 3.1 with

\[
                              5\le |N|\le8.             \tag{4.5}
\]

Then either `G` contains a `K_7^-` minor, or there are an edge
`e\in N` and a nonempty proper connected set `Y` meeting an end of `e`
such that

\[
                         N_G(Y)
\]

is an actual separator of order at least seven.  The singleton-signature
colouring for `e` is proper on `G-Y`, and its equality partition on
`N_G(Y)` is rejected by the intact closed `Y`-side.

#### Proof

Put `H_N=G-N`.  It is seven-connected because it contains `G-M`, and

\[
                    |E(H_N)|\ge4|V(G)|-|N|
                              \ge4|V(G)|-8.            \tag{4.6}
\]

As in Corollary 4.1, choose a spanning exact model

\[
                         P,B,C,U_1,U_2,U_3,U_4.        \tag{4.7}
\]

For a model of this form define

\[
             s(P)=|(P\cup N_G(P))\cap V(N)|.          \tag{4.8}
\]

Choose the model to maximise `s(P)`.

Every nonempty proper set meeting an endpoint of `N` carries the rejected
singleton-coordinate trace: use the colouring with precisely that matching
edge monochromatic.  If one of `P,B,C` meets `V(N)`, that branch set is the
required `Y`, since it is anticomplete to one of the other named branch
sets.  We may therefore assume that every endpoint lies in a universal bag.

Fix an endpoint `v\in U_i` which is not adjacent to `P`.  Choose
`q\in U_i\cap N_G(P)` and a spanning tree of `G[U_i]` containing a
`q`--`v` path.  Delete the edge of this path incident with `v`.  Let `A`
be the resulting connected side containing `q`, and put `W=U_i-A`; thus
`W` is connected and contains `v`.

If `W` is anticomplete to a foreign branch set of `U_i`, then
`N_G(W)` is an actual separator and `W` is the required response side.
Otherwise move `A` from `U_i` into `P`.  The new sets are connected,
`W` retains every required foreign adjacency, and the edge between `A`
and `W` supplies the new `P`--`U_i` adjacency.  If `A` is adjacent to
`B` or `C`, the seven branch sets miss at most one adjacency and give
`K_7^-`.  Otherwise they form another exact model.

If `A` contains an endpoint of `N`, then `P\cup A` is a response side
with an actual separator, using `B` or `C` as a far branch set.  If it
contains no endpoint, every endpoint counted by the old score remains
counted and `v` becomes a new endpoint in the neighbourhood of the
deficient branch set.  This strictly increases (4.8), contrary to its
choice.

Thus every matching endpoint in a universal bag is adjacent to `P`.
There are at least ten endpoints distributed among four universal bags,
so one universal bag contains two distinct endpoint portals.  Apply the
audited exact-`K_7^\vee` separator dichotomy to those two selected
neighbours of `P`.  It gives `K_7^-`, or a nonempty proper connected set
inside that universal bag, containing one selected endpoint, whose open
neighbourhood is an actual separator.  The singleton-coordinate colouring
again supplies the rejected trace. `\square`

### Corollary 4.3 (linear abundance of operation-labelled separations)

Unless `G` already contains `K_7^-`, it has at least

\[
   \left\lfloor
      \frac{1}{5}
      \left\lceil\frac{5n+59}{28}\right\rceil
   \right\rfloor                                      \tag{4.9}
\]

distinct matching edges, each of which is retained by an actual
response-bearing separation as in Theorem 4.2.

#### Proof

Partition a matching from Theorem 3.1 into disjoint five-edge submatchings,
discarding at most four edges.  Apply Theorem 4.2 to each block.  The
selected coordinate edges are distinct because the blocks are disjoint.
`\square`

## 5. Scope

Theorem 3.1 replaces the former bounded coordinate supply by a linear one.
In particular, every hypothetical counterexample has one seven-connected
common deletion graph carrying seven matching coordinates, all `127`
nonempty signatures, and an exact spanning `K_7^\vee` model.  There is no
six-connectivity branch and no induced-path alternative at this entrance.

The theorem does not synchronize the boundary partitions of the response
separations in Corollary 4.3, bound their orders above seven, or prove that
two of the exact models can be chosen compatibly.  Those are the remaining
global uses of the new abundance.

## Dependencies

- the audited critical-host degree and exceptional-vertex theorem;
- the audited five-edge seven-removable matching theorem, based on Chu's
  sharp removable-matching theorem;
- Mader's critical-cycle theorem, in the same form already used in the
  coordinate-growth theorem;
- Norin--Totschnig's density theorem for `K_7^\vee`; and
- the audited exact-`K_7^\vee` separator dichotomy.
