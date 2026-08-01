# Pair deletion at degree-eight centres and a spanning `K_7^\vee` model

**Status:** written nonterminal reduction; separately internally audited in
[`hc7_k7minus_pair_deletion_k7vee_reduction_audit.md`](hc7_k7minus_pair_deletion_k7vee_reduction_audit.md).
This note records a reusable consequence of the disconnected
exceptional-centre branch.  It does not construct a `K_7^-` minor, produce
a six-colouring, or prove exceptional anti-neighbourhood connectivity.

## 1. Setting

Let `G` satisfy

\[
 \kappa(G)\ge7,
 \qquad \chi(G)=7,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G,
 \qquad K_7^-\npreccurlyeq G.                         \tag{H}
\]

Assume that some exceptional degree-eight vertex has disconnected
anti-neighbourhood.  The audited two-component theorem then gives

\[
 \delta(G)\ge8,
 \qquad |E(G)|\ge4|V(G)|,
 \qquad n_8\ge25+\tau,                               \tag{1}
\]

where

\[
                  \tau=\sum_{i\ge10}(i-9)n_i.
\]

In this branch `G` contains no literal `K_5`, and every degree-eight vertex
is exceptional.

## 2. The pair-deletion reduction

### Theorem 1 (a spanning near-clique model after deleting two centres)

Let `a,b` be any two degree-eight vertices of `G`, and put
`H=G-{a,b}`.  Then `H` is five-connected and contains a spanning
`K_7^\vee`-minor model.  Label its branch sets

\[
                         P,B,C,U_1,U_2,U_3,U_4,        \tag{2}
\]

so that the two missing adjacencies of `K_7^\vee` are `PB` and `PC`.
For each retained root `r\in\{a,b\}`:

1. `r` is adjacent to at most four of the six branch sets
   `B,C,U_1,U_2,U_3,U_4`;
2. if `r` is adjacent to `P`, then it is adjacent to neither `B` nor `C`;
3. `a` and `b` cannot both be adjacent to all five branch sets
   `P,U_1,U_2,U_3,U_4`.

Here a vertex is adjacent to a branch set when it has a neighbour in that
set.

#### Proof

Deleting two vertices from a seven-connected graph leaves a
five-connected graph.  Writing `n=|V(G)|` and `m=|E(G)|`, exact edge
accounting gives

\[
 \begin{aligned}
 |E(H)|
   &=m-d_G(a)-d_G(b)+\mathbf 1_{ab\in E(G)}\\
   &=m-16+\mathbf 1_{ab\in E(G)}\\
   &\ge4n-16+\mathbf 1_{ab\in E(G)}\\
   &=4|V(H)|-8+\mathbf 1_{ab\in E(G)}.                \tag{3}
 \end{aligned}
\]

Norin--Totschnig's extremal theorem therefore gives a `K_7^\vee` minor in
`H`, unless `H\cong K_{2,2,2,2}`.  Equation (1) gives `n\ge25`, whereas
`|V(H)|=n-2\ge23` and `K_{2,2,2,2}` has eight vertices, so the exception
is impossible.

Enlarge the seven branch sets to a partition of `V(H)` by assigning every
component outside their union to an adjacent branch set.  This preserves
connectedness and all required model adjacencies.  Since `G` has no
`K_7^-` minor, the pairs `PB` and `PC` remain nonadjacent: either additional
adjacency would make the seven branch sets contain a `K_7^-` model.

The six branch sets

\[
                         B,C,U_1,U_2,U_3,U_4           \tag{4}
\]

are pairwise adjacent.  If `r` met at least five of them, these six sets
together with the singleton branch set `\{r\}` would have at most one
missing adjacency, giving a `K_7^-` model.  This proves item 1.

Suppose next that `r` meets both `P` and `B`.  Absorb `r` into `P`.  The
enlarged branch set is connected and now adjacent to `B`; among the seven
sets in (2), only its adjacency to `C` may be absent.  This is again a
`K_7^-` model.  The same argument with `B,C` interchanged proves item 2.

Finally assume that both roots meet `P,U_1,U_2,U_3,U_4`.  Then

\[
             \{a\},\{b\},P,U_1,U_2,U_3,U_4            \tag{5}
\]

are seven pairwise adjacent branch sets except possibly for the single
pair `\{a\},\{b\}`.  They contain a `K_7^-` model, proving item 3.
\(\square\)

## 3. Exact limit of the reduction

The theorem does not control how the eight neighbours of a retained root
are distributed *inside* a contacted branch set.  In particular, its
conclusions do not exclude the following contact pattern:

\[
 N_G(a)\cap V(H),N_G(b)\cap V(H)
     \subseteq U_1\cup U_2\cup U_3\cup U_4,
 \qquad
 \{a,b\}\text{ anticomplete to }P\cup B\cup C.        \tag{6}
\]

This is a surviving abstract contact pattern, not a claimed example
satisfying (H).  Seven-connectivity supplies paths from the roots but does
not by itself split one of the four contacted branch sets while preserving
its five other model adjacencies.

The global count has the same localization limit.  For `D\subseteq V(G)`,
write `n_8(D)=|\{v\in D:d_G(v)=8\}|`.  For a disconnected exceptional
centre `u` with exterior components `E,F`, the nine vertices of `N[u]` and
(1) give only

\[
                         n_8(E)+n_8(F)\ge16+\tau.       \tag{7}
\]

There is no positive lower bound on either summand separately.  Thus the
count does not place a degree-eight centre in a selected minimum exterior
component or in an operation-returned side.

The reusable open step exposed by (6) is a label-preserving branch-set
transfer: move a root-neighbour piece into an uncontacted member of (4)
while retaining the other required branch-set adjacencies, or return an
actual separation whose boundary is literally the neighbourhood of a
named exceptional degree-eight vertex.  An arbitrary smaller separation
does not certify exceptional anti-neighbourhood descent.

## Inputs and scope

- [two-component literal-clique exclusion and density jump](../results/hc7_k7minus_one_nonfull_k5_and_nested_cut.md);
- [Norin--Totschnig](https://arxiv.org/abs/2507.03244), *Every graph with
  no `K_7^\vee`-minor is 6-colorable*, Theorem 6;
- seven-connectivity from contraction-criticality.

The theorem may be cited for the spanning `K_7^\vee` model and the three
displayed root-contact restrictions.  It may not be cited as a
label-preserving branch-set split, a same-host exceptional
anti-neighbourhood descent, or an elimination of any remaining attachment
regime.
