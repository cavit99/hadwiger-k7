# Seven-cut component bound in a minor-minimal non-six-colourable graph

**Status:** written proof; separate internal audit GREEN for this revision.

Here `K_7^-` denotes `K_7` with one edge deleted.  A connected subgraph
of `G-S` is called **full at `S`** in this note if it is adjacent to every
literal vertex of `S`.

## Lemma 1 (exact boundary-colouring reflection)

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

where `L` and `R` are nonempty and anticomplete.  Suppose every proper
minor of `G` is six-colourable.  Let `Pi` be a partition of `S` into
independent blocks.  Suppose `G[L]` contains pairwise vertex-disjoint
connected subgraphs

\[
                         P_1,\ldots,P_t
\]

that are each full at `S`.  Suppose also that all blocks of `Pi` except a
set of singleton blocks whose vertices form a clique in `G[S]` can be
assigned injectively to `P_1,\ldots,P_t`, and that at least one block is
assigned.

Then `G[R\cup S]` has a proper six-colouring whose equality partition on
the literal set `S` is exactly `Pi`.

### Proof

Let `U\subseteq S` be the clique of retained singleton-block vertices, and
write the other blocks as `B_1,\ldots,B_m`, assigned to
`P_1,\ldots,P_m`, where `1\le m\le t`.  Each set

\[
                         Z_j=V(P_j)\cup B_j
\]

is connected: `P_j` is connected and has a neighbour at every vertex of
`B_j`.  These sets are pairwise disjoint.  Contract a spanning tree of
each `G[Z_j]`, and call its image `z_j`.  At least one edge between a
connected subgraph and its assigned nonempty boundary block is contracted,
so the resulting minor `M` is proper.

The vertices

\[
                         z_1,\ldots,z_m,\quad U
\]

form a clique in `M`.  For distinct `j,k`, fullness of `P_j` supplies an
edge from `P_j` to a literal vertex of `B_k`; fullness also supplies every
`z_j-U` adjacency, and `U` is a clique by assumption.  These clique
vertices correspond one-to-one with the blocks of `Pi`.

Take a six-colouring of `M`.  Keep it on the untouched set `R\cup U`, and
give every vertex of `B_j` the colour of `z_j`.  This is a proper colouring
of `G[R\cup S]`: each `B_j` is independent, and every edge from `B_j` to
an untouched vertex was represented by an edge at `z_j`.  The displayed
clique gives different colours to different blocks, so the equality
partition on `S` is exactly `Pi`.  \(\square\)

## Lemma 2 (two-versus-two and one-versus-three exclusion)

Retain the setup of Lemma 1, assume that `G` is not six-colourable, and
suppose

\[
                         \Delta(G[S])\le1.               \tag{1}
\]

Neither of the following configurations exists:

1. each of `G[L]` and `G[R]` contains two pairwise vertex-disjoint
   connected subgraphs full at `S`; or
2. `G[L]` contains one connected subgraph full at `S` and `G[R]` contains
   three pairwise vertex-disjoint connected subgraphs full at `S`.

### Proof

Because `G[S]` is a matching together with isolated vertices, there is a
partition

\[
                         S=I_1\mathbin{\dot\cup}I_2
                           \mathbin{\dot\cup}\{q\},      \tag{2}
\]

where `I_1,I_2` are independent sets of order three.  Indeed, choose `q`
to be an isolated vertex, put the two ends of every remaining matching
edge in opposite sets, and distribute the remaining isolated vertices to
make both sets have order three.  Such a `q` exists because a matching on
seven vertices has at most three edges.

In configuration 1, apply Lemma 1 in `L` to the partition

\[
                         I_1\mid I_2\mid\{q\},           \tag{3}
\]

assigning `I_1,I_2` to the two full connected subgraphs and retaining the
singleton `q`.  This gives a six-colouring of `G[R\cup S]` with exact
partition (3).  Apply the same construction in `R` to obtain a six-colouring
of `G[L\cup S]` with the same exact partition.  A permutation of the six
colour names makes the two colourings agree on every vertex of `S`; they
then glue because `L` and `R` are anticomplete.  This contradicts the
assumption that `G` is not six-colourable.

Now consider configuration 2.  Since a seven-vertex graph of maximum
degree one has an independent set `I` of order at least four, choose one of
order four.  Let `Q\subseteq G[L]` be full at `S`.  Contract a spanning
tree of the connected set

\[
                              V(Q)\cup I                 \tag{4}
\]

and six-colour the resulting proper minor.  Pull this colouring back only
to `G[R\cup S]`, assigning every vertex of `I` the colour of the contracted
image.  The pullback is proper because `I` is independent.  Moreover, `I`
is one exact colour class on `S`: fullness of `Q` makes its contracted image
adjacent to each of the three vertices in `S-I`.

Let `Pi` be the complete equality partition on `S` in this colouring.  It
consists of the block `I` and at most three blocks on `S-I`.  If there are
at most two latter blocks, assign all blocks of `Pi` to at most three of the
full connected subgraphs in `R` and apply Lemma 1 with no retained
singleton.  If there are three latter blocks, all three vertices of `S-I`
are singleton blocks; retain any one of them and assign `I` and the other
two singleton blocks to the three full connected subgraphs in `R`.
Lemma 1 again gives a six-colouring of `G[L\cup S]` with exact partition
`Pi`.

The two closed-shore colourings have the same exact boundary partition.
After permuting colour names they glue to a six-colouring of `G`, again a
contradiction.  \(\square\)

## Theorem 3 (critical seven-cut capacity)

Let `G` satisfy

\[
 \chi(G)=7,
 \qquad
 \text{every proper minor of `G` is six-colourable},
 \qquad
 \kappa(G)\ge7,
 \qquad
 K_7^-\npreccurlyeq G.                                  \tag{5}
\]

Let `S` be a vertex cut of order seven.  Let
`C_1,\ldots,C_r` be the components of `G-S`, and let `pi_S(G)` be the
maximum number of pairwise vertex-disjoint connected subgraphs of `G-S`
that are each full at `S`.  Then

\[
                         2\le r\le\pi_S(G)\le3.          \tag{6}
\]

For each `i`, let `mu_i` be the maximum number of pairwise vertex-disjoint
connected subgraphs of `G[C_i]` that are full at `S`.  Then:

1. if `r=3`, one has

   \[
                              \mu_1=\mu_2=\mu_3=1;       \tag{7}
   \]

   moreover,

   \[
                              \chi(G[S])=3,              \tag{8}
   \]

   and every proper three-colouring of `G[S]` has colour-class sizes
   `3,2,2`;

2. if `r=2`, then

   \[
                              \min\{\mu_1,\mu_2\}=1,
                              \qquad \mu_1+\mu_2\le3,   \tag{9}
   \]

   and `G[S]` has an edge.

In particular, deleting a seven-vertex cut from `G` never leaves four
components.

### Proof

Seven-connectivity gives

\[
                              N_G(C_i)=S                \tag{10}
\]

for every `i`: a proper subset of `S` containing `N_G(C_i)` would separate
`C_i` from another component.  Hence every component is itself full at
`S`, proving `2\le r\le\pi_S(G)` and `\mu_i\ge1`.

The audited connected-subgraph capacity theorem for a seven-vertex
boundary gives

\[
                              \pi_S(G)\le4.              \tag{11}
\]

Suppose equality holds.  The same theorem gives

\[
                              \Delta(G[S])\le1.          \tag{12}
\]

Every connected subgraph of `G-S` lies in one component, so

\[
                              \pi_S(G)=\sum_{i=1}^r\mu_i.\tag{13}
\]

Indeed, every global family restricts inside component `C_i` to at most
`\mu_i` members, while the union of maximum families chosen independently
inside the components is itself a global disjoint family.

The positive integers `\mu_i` therefore form a composition of four with
at least two parts.  The component set can be partitioned into two nonempty
classes so that the corresponding sums are either `2,2` or `1,3`:
the only compositions to consider are `2+2`, `3+1`, `2+1+1`, and
`1+1+1+1`.

Let `L` and `R` be the unions of the components in those two classes.
They are nonempty and anticomplete.  Their maximum families supply the
two-versus-two or one-versus-three configuration prohibited by Lemma 2,
using (12).  Thus equality in (11) is impossible, proving
`\pi_S(G)\le3` and hence (6).

If `r=3`, equations (13) and `\mu_i\ge1` force (7).  The general boundary
capacity theorem also gives

\[
                              |E(G[S])|\le9.             \tag{14}
\]

The boundary contains no `K_4`: four boundary singleton branch sets and
the three full components, each anchored at one of the other three
boundary vertices, would form an explicit `K_7` minor.

We claim that a `K_4`-free graph on seven vertices with at most nine edges
is three-colourable.  Otherwise take a four-critical subgraph `F`.  Then
`\delta(F)\ge3`.  If `|V(F)|=4`, then `F=K_4`.  If `|V(F)|=5`, parity
shows that some vertex is universal; deleting it leaves a three-chromatic
four-vertex graph because a universal vertex raises chromatic number by
exactly one.  Such a four-vertex graph contains a triangle, again giving a
`K_4` in `F`.
If `|V(F)|=6` and some vertex has degree at least four, then
`|E(F)|\ge10`; otherwise `F` is cubic.  In the latter case its complement
is either `C_6` or two disjoint triangles.  Pairing consecutive vertices
of the complementary `C_6` gives three independent pairs in `F`; if the
complement is two triangles, their vertex sets are two independent sets in
`F`.  Thus `F` is three-colourable in either case.  Finally, if
`|V(F)|=7`, minimum degree three gives `|E(F)|\ge11`.  Every case is
contradictory, proving the claim and hence `\chi(G[S])\le3`.

For the reverse inequality, suppose `G[S]` had a proper colouring into at
most two nonempty independent blocks.  For each component `C_i`, use the
other two full components in Lemma 1 to reflect that fixed boundary
partition onto `G[C_i\cup S]`.  Aligning colour names and gluing the three
component-side colourings would six-colour `G`.  Thus (8) holds.

Now fix any proper three-colouring of `G[S]`.  If one colour class were a
singleton, then for each `C_i` the other two full components could be
assigned to the other two colour classes in Lemma 1 while the singleton
was retained.  This would reproduce the same exact partition on every
component side and again six-colour `G`.  Therefore every colour class has
order at least two.  Their orders sum to seven, so they are `3,2,2`.

If `r=2`, equations (13) and `\mu_i\ge1` force (9).  If `G[S]` were
independent, apply Lemma 1 on each side to the one-block partition `{S}`,
using one full connected subgraph from the opposite component.  The two
returned colourings align and glue, a contradiction.  Hence `G[S]` has an
edge.  \(\square\)

## Consequences and scope

The general seven-boundary theorem now gives the following additional
information.  When `pi_S(G)=3`, the boundary has at most nine edges and
connectivity at most three.  When `pi_S(G)=2`, it has no `K_5` minor and
connectivity at most four.

Theorem 3 closes the four-component seven-cut case for the actual
minor-minimal non-six-colourable host.  It is stronger than a density-only
descent in that setting: the configuration itself cannot occur.  The proof
uses the proper-minor six-colouring hypothesis essentially, so it does not
exclude four-component cuts in arbitrary seven-connected graphs, prove the
bare `4n-4` extremal theorem, or settle the remaining two- and
three-component cases.

The colouring-reflection mechanism is a self-contained specialization of
the previously audited exact-seven connected-subgraph packing and
reflection results.  Those results already imply the bound
`\pi_S(G)\le3` and the exclusion of four-component cuts in the critical
host, so those conclusions are not claimed here as new to the repository.
The new consequence of the current `K_7^-` boundary theorem is the exact
three-component conclusion: its nine-edge bound and the explicit boundary
minor exclusion force `\chi(G[S])=3`, removing the formerly surviving
four-chromatic boundary case.

## Dependency

- [Capacity of connected subgraphs adjacent to a seven-vertex boundary](../results/hc7_k7minus_seven_boundary_component_descent.md),
  Theorem 1 and Corollary 2.

For overlap and provenance, compare the separately internally audited
[exact-seven connected-subgraph packing theorem](hc7_exact_seven_packet_packing.md)
and [adaptive one-versus-three reflection theorem](hc7_exact7_adaptive_packet_reflection.md).
