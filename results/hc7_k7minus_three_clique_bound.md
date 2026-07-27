# Three literal `K_5` subgraphs under `K_7^-` exclusion

**Status:** written proof; separate internal audit GREEN.  This is a global
clique-family theorem.  It does not prove the `K_7^-` intermediate
conjecture or `HC_7`.

## Theorem 1

Every seven-connected, non-two-apex graph with no `K_7^-` minor contains at
most two distinct literal `K_5` subgraphs.

## Proof

Suppose that `G` contains three distinct literal `K_5` subgraphs.  First,
two of them cannot intersect in four vertices.  If `L_1,L_2` did, then
their six-vertex union `X` would contain `K_6^-`: every pair is adjacent
except possibly the pair of vertices unique to the two cliques.

Seven-connectivity makes `G-X` nonempty and connected.  Every vertex of
`X` has a neighbour in `G-X`, because it has degree at least seven and at
most five neighbours in `X`.  Contract `G-X` to one connected branch set
and retain the six singleton vertices of `X`.  The resulting seven branch
sets form a `K_7^-`-minor model, a contradiction.

Consequently, any three distinct literal `K_5` subgraphs
`L_1,L_2,L_3` satisfy

\[
                          |L_i\cap L_j|\le3\qquad(i\ne j). \tag{1}
\]

Theorem 1.10 of Niu and Zhang says that a `(k+2)`-connected,
non-`(k-3)`-apex graph containing three literal `k`-cliques whose pairwise
intersections have order at most `k-2` contains a `K_{k+2}` minor.  Apply
it with `k=5`.  Seven-connectivity, non-two-apexness and (1) give a `K_7`
minor, and therefore a `K_7^-` minor, again a contradiction.  \(\square\)

## Published input and exact scope

The external input is Theorem 1.10 of Jianbing Niu and Cun-Quan Zhang,
*Cliques, minors and apex graphs*, Discrete Mathematics 309 (2009),
4095--4107, DOI
[`10.1016/j.disc.2008.12.009`](https://doi.org/10.1016/j.disc.2008.12.009).
The theorem and its exact `k=5` specialization are also recorded in the
separately audited
[global literal-`K_5` transversal theorem](hc7_global_literal_k5_transversal.md).

The overlap-four branch establishes only a `K_7^-` minor; it does not in
general establish a `K_7` minor.  In the application to a seven-chromatic
graph, non-two-apexness is automatic: a planar graph obtained by deleting
two vertices could be four-coloured, and two fresh colours on the deleted
vertices would six-colour the original graph.
