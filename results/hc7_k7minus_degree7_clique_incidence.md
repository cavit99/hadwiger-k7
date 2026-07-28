# Degree-seven clique incidence under `K_7^-` exclusion

**Status:** written proof; separate internal audit GREEN.  This is a theorem
about the proposed `K_7^-` intermediate conjecture.  It does not prove that
conjecture or `HC_7`.

Here `K_7^-` denotes `K_7` with one edge deleted.

## Theorem 1

Let `G` be a seven-connected graph with

\[
 \chi(G)=7,
 \qquad
 \text{every proper minor of `G` six-colourable},
 \qquad
 K_7^-\npreccurlyeq G.
\]

If `v` has degree seven, then `G[N(v)]` contains a literal `K_4`.
Consequently, `v` belongs to a literal `K_5` subgraph of `G`.

## Proof

Put `H=G[N(v)]`.  Dirac's contraction-critical neighbourhood inequality
gives

\[
                              \alpha(H)\le2.             \tag{1}
\]

Suppose that `H` is `K_4`-free.  We first show that `Delta(H)>=4`.
If instead `Delta(H)<=3`, then `F=\overline H` is triangle-free by (1) and
has minimum degree at least three.  A shortest odd cycle in `F` has order
five or seven.  A shortest seven-cycle is induced and uses every vertex,
contradicting the minimum-degree bound.  A shortest five-cycle is induced.
Each of the two vertices outside it has at most two neighbours on the cycle,
because its cycle-neighbourhood is independent.  The five cycle vertices
need at least five outside incidences to reach degree three, while the two
outside vertices supply at most four.  This is again impossible.

Thus `F` is bipartite.  Its parts have orders three and four, since
`delta(F)>=3`; the four-vertex part is a `K_4` in `H`, a contradiction.
Therefore

\[
                              \Delta(H)\ge4.             \tag{2}
\]

A universal vertex of `H` would also give a `K_4`: on the other six
vertices, `R(3,3)=6` gives either an independent triple, contradicting (1),
or a triangle, which the universal vertex completes to a `K_4`.  Choose a
nonuniversal maximum-degree vertex `a`, a nonneighbour `b` of `a`, and put

\[
                              U=N(v)-\{a,b\}.
\]

The set `U` has order five, and (2) says that `a` is adjacent to at least
four of its vertices.

The audited degree-seven anti-neighbourhood theorem makes `G-N[v]` nonempty
and connected.  Apply Theorem 3.5 of the audited exact matching-language
and rooted-model theorem to the boundary nonedge `ab`.  Since exclusion of
`K_7^-` also excludes `K_7`, its non-`K_7` outcome gives five pairwise
disjoint, connected, pairwise adjacent branch sets

\[
                              (B_x:x\in U)
\]

in `G-v-\{a,b\}`, with `x\in B_x` for every `x\in U`.

Now take

\[
                         \{v\},\quad \{a\},\quad (B_x:x\in U). \tag{3}
\]

These seven branch sets are disjoint and connected.  The five `B_x` form a
clique-minor model.  The singleton `\{v\}` is adjacent to `\{a\}` and to
every `B_x`.  Finally, `\{a\}` is adjacent through the literal roots to at
least four of the five `B_x`.  Hence at most one of the 21 required
branch-set adjacencies in (3) is absent.  If one is absent, (3) is a
`K_7^-`-minor model; if none is absent, it is a `K_7`-minor model and hence
also contains `K_7^-`.  Both contradict the hypothesis.

Therefore `H` contains a literal `K_4`, and adjoining `v` gives the claimed
literal `K_5`.  \(\square\)

## Dependencies and scope

The proof uses Dirac's contraction-critical neighbourhood inequality and
the following two separately audited repository results:

- [degree-seven anti-neighbourhood connectivity](hc7_degree7_anti_neighbourhood_connectivity.md);
- [exact matching languages and the uniform rooted `K_5` theorem](hc7_degree7_matching_bridge_bundle.md), specifically Theorem 3.5.

No finite census is a logical dependency.  A minor-minimal counterexample
to six-colourability under `K_7^-` exclusion satisfies the displayed
hypotheses because Mader's contraction-critical connectivity theorem makes
it seven-connected.
