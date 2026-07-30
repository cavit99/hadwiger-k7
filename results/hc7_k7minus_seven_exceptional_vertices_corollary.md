# Seven exceptional degree-eight vertices in a critical `K_7^-` host

**Status:** written proof; separate internal audit GREEN for this revision.
This is a structural theorem about a hypothetical counterexample.  It does
not prove the `K_7^-` six-colour conjecture or `HC_7`.

Here `K_7^-` denotes `K_7` with one edge deleted.  Let `G` be a finite
simple graph satisfying

\[
 \kappa(G)\ge7,
 \qquad \chi(G)=7,
 \qquad \text{every proper minor of `G` is six-colourable},
 \qquad K_7^-\npreccurlyeq G.                              \tag{H}
\]

For each integer `i`, let `n_i` be the number of degree-`i` vertices of
`G`.  Call a degree-eight vertex **exceptional** if it lies in no literal
`K_5`.  Equivalently, its neighbourhood contains no literal `K_4`.

## Theorem 1 (seven exceptional vertices and the degree defect)

Let `b` be the number of exceptional vertices and put

\[
                  \tau=\sum_{i\ge10}(i-9)n_i.               \tag{1}
\]

Then

\[
                  b\ge15-n_7+\tau\ge7+\tau.                 \tag{2}
\]

In particular, `G` has at least seven exceptional degree-eight vertices.
The subgraph induced by all exceptional vertices is `K_5`-free, and every
set of seven exceptional vertices contains at least three nonedges.

### Proof

The audited
[density and low-degree rigidity theorem](hc7_k7minus_five_exceptional_vertices_reduction.md)
proves, under (H),

\[
 25\le 9|V(G)|-2|E(G)|
    =2n_7+n_8-\sum_{i\ge10}(i-9)n_i.                         \tag{3}
\]

Every degree-seven vertex lies in a literal `K_5`, by the audited exact
degree-seven neighbourhood theorem used there.  Every nonexceptional
degree-eight vertex also lies in a literal `K_5`, by definition.  The
audited three-clique theorem says that `G` has at most two literal `K_5`s,
so these vertices lie in their union and hence

\[
                         n_7+(n_8-b)\le10.                   \tag{4}
\]

Combining (1), (3), and (4) gives

\[
 25\le 2n_7+n_8-\tau
    =\bigl(n_7+n_8-b\bigr)+n_7+b-\tau
    \le10+n_7+b-\tau,
\]

and therefore

\[
                         b\ge15-n_7+\tau.                    \tag{5}
\]

The separately audited
[all-degree-seven clique exclusion](hc7_k7minus_all_degree7_k5_exclusion.md)
proves `n_7\le8` under exactly (H).  Substitution in (5) proves (2).

No five exceptional vertices form a clique, because each vertex of such a
clique would lie in that literal `K_5`.  Thus the exceptional-vertex
subgraph is `K_5`-free.  Turan's theorem gives at most eighteen edges in a
`K_5`-free graph on seven vertices, whereas seven vertices have twenty-one
pairs.  At least three pairs are consequently nonedges.  \(\square\)

## Theorem 2 (rigidity at exactly seven exceptional vertices)

If `b=7`, then

\[
 n_7=8,\qquad n_8=9,\qquad n_i=0\quad(i\ge10),             \tag{6}
\]

and every remaining vertex has degree nine.  Moreover,

\[
                  2|E(G)|=9|V(G)|-25,                     \tag{7}
\]

so `|V(G)|` is odd.  There are exactly two literal `K_5`s.  They are
vertex-disjoint, and each consists of four degree-seven vertices and one
nonexceptional degree-eight vertex.  In particular, `|V(G)|\ge21`.

### Proof

Equality `b=7` in (2) forces `n_7=8` and `tau=0`; hence there is no vertex
of degree at least ten.  Inequality (3) now gives `n_8>=9`, while (4) gives

\[
                         8+(n_8-7)\le10,
\]

and hence `n_8<=9`.  Thus `n_8=9`, and every other vertex has degree nine.
Summing degrees gives

\[
 2|E(G)|=7\cdot8+8\cdot9+9\bigl(|V(G)|-17\bigr)
         =9|V(G)|-25,
\]

which also proves the parity assertion.

The eight degree-seven vertices and the two nonexceptional degree-eight
vertices all lie in the union of at most two literal `K_5`s.  Ten distinct
vertices cannot be covered by fewer than two five-vertex cliques, so there
are exactly two and they are disjoint.  The audited all-degree-seven clique
exclusion says that each contains a degree-eight vertex.  There are exactly
two nonexceptional degree-eight vertices in their union, so each clique
contains one of them and four degree-seven vertices.  The four degree-seven
vertices of either clique lie in no other literal `K_5`, because the two
literal `K_5`s are the only ones and are disjoint.  Lemma 2(2) of the
[density and low-degree rigidity theorem](hc7_k7minus_five_exceptional_vertices_reduction.md)
therefore applies with fifth-vertex degree eight and gives
`|V(G)|\ge8+13=21`.  \(\square\)

## Corollary 3 (sufficient exceptional-vertex finishing theorem)

The following statement would prove that every `K_7^-`-minor-free graph is
six-colourable:

> Every graph satisfying (H) has at most six exceptional degree-eight
> vertices.

### Proof

If the six-colour statement were false, choose a minor-minimal
non-six-colourable `K_7^-`-minor-free graph `G`.  Vertex minimality gives
`\chi(G)=7`, proper-minor minimality gives the third condition in (H), and
`G` is noncomplete, since the only complete seven-chromatic graph is
`K_7`, which contains `K_7^-`.  Mader's connectivity theorem for
noncomplete contraction-critical graphs therefore gives
`\kappa(G)\ge7`.  Hence `G` satisfies (H).  The proposed upper bound would
give `b\le6`, contradicting Theorem 1.  \(\square\)

## Dependencies and scope

Theorem 1 is the direct synthesis of two previously audited results.  The
first supplies the sharper inequality `b\ge15-n_7+\tau`; the second supplies
the independent improvement `n_7\le8`.  No density-equality assumption and
no finite enumeration are used.

The lower bound does not supply an upper bound on the number of exceptional
vertices.  Seven-connectivity alone gives paths between selected vertices,
but the recorded
[seven-path counterexample](../barriers/hc7_k7minus_bad_pair_seven_paths_barrier.md)
shows that one nonadjacent pair and ordinary Menger linkage do not by
themselves force a `K_7^-` minor.  Any proof of the finishing statement must
use additional simultaneous structure or the proper-minor colouring
responses in (H).
