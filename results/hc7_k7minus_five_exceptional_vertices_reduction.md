# Five exceptional degree-eight vertices under `K_7^-` exclusion

**Status:** written proof; separate internal audit GREEN.  This reduction is
conditional on the two adjacent audited results.  The resulting
five-exceptional-vertices theorem remains open, so this proves neither the
`K_7^-` conjecture nor `HC_7`.

Call a degree-eight vertex `bad` if it belongs to no literal `K_5`;
equivalently, its neighbourhood contains no literal `K_4`.

## Theorem 1 (global count reduction)

Let `G` be seven-connected, with `chi(G)=7`, every proper minor
six-colourable, and no `K_7^-` minor.  Then `G` contains at least five bad
degree-eight vertices.  In particular, it contains two nonadjacent bad
degree-eight vertices.

## Proof

Let `n_i` denote the number of vertices of degree `i`.  Jakobsen's extremal
theorem, in the form quoted as Theorem 2 by Albar, says that an `n`-vertex
graph with at least

\[
                              \frac92n-12
\]

edges has a `K_7^-` minor or is a
`(K_{2,2,2,2},K_6,4)`-cockade.  A nontrivial such cockade has a separator of
order four, while either base graph has chromatic number at most six.
Hence the present seven-connected seven-chromatic graph is not a cockade,
and

\[
                              2|E(G)|\le9|V(G)|-25.       \tag{1}
\]

Since seven-connectivity gives minimum degree at least seven, (1) yields

\[
 \begin{aligned}
  25
   &\le 9|V(G)|-2|E(G)|\\
   &=2n_7+n_8-\sum_{i\ge10}(i-9)n_i
   \le2n_7+n_8.                                         \tag{2}
 \end{aligned}
\]

By the audited degree-seven clique-incidence theorem, every degree-seven
vertex lies in a literal `K_5`.  By the audited three-clique bound, `G` has
at most two distinct literal `K_5` subgraphs: the graph is non-two-apex
because it is seven-chromatic.  Their union has at most ten vertices.

Let `b` be the number of bad degree-eight vertices.  Every degree-seven
vertex and every nonbad degree-eight vertex belongs to that union, so

\[
                              n_7+(n_8-b)\le10.           \tag{3}
\]

In particular `n_7<=10`.  Combining (2) and (3),

\[
                     b\ge n_7+n_8-10\ge15-n_7\ge5.      \tag{4}
\]

Five bad vertices cannot be pairwise adjacent, since they would themselves
form a literal `K_5`.  Thus two of them are nonadjacent.  \(\square\)

## Corollary 2 (exact sufficient finishing theorem)

The following statement would prove that every `K_7^-`-minor-free graph is
six-colourable:

> **Five-exceptional-vertices theorem.** A seven-connected graph with
> `chi(G)=7`, every proper minor six-colourable, and no `K_7^-` minor has at
> most four degree-eight vertices whose neighbourhoods are `K_4`-free.

Indeed, Theorem 1 gives at least five such vertices in any minor-minimal
counterexample.

## A stronger possible pair route

The following statements would also suffice, but are stronger than the
five-exceptional-vertices theorem:

1. no two nonadjacent bad degree-eight vertices occur under the same host
   hypotheses;
2. for every nonadjacent bad degree-eight pair `u,v`, the graph
   `G-\{u,v\}` contains five pairwise adjacent connected branch sets, each
   meeting both `N(u)` and `N(v)`.

In the second outcome, the five bags together with `\{u\},\{v\}` form a
`K_7^-` model whose only permitted missing adjacency is `uv`.  Neither pair
statement is equivalent to the exact finishing theorem: a bad pair might be
eliminated by another minor construction, a colouring contradiction or a
critical separation, and a proof may need all five exceptional vertices
simultaneously.

Seven internally disjoint `u`--`v` paths and the two local neighbourhood
types do not force the paired-rooted model; the adjacent barrier gives an
explicit counterexample to that weaker inference.

## Published input

The density input is Jakobsen's theorem as quoted in Boris Albar,
*Coloration of `K_7^-`-minor free graphs*, arXiv:1402.2806, Theorem 2 and
Corollary 4.  The two new inputs are:

- [degree-seven clique incidence under `K_7^-` exclusion](hc7_k7minus_degree7_clique_incidence.md);
- [the three-clique bound under `K_7^-` exclusion](hc7_k7minus_three_clique_bound.md).
