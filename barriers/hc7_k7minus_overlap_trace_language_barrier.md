# Independent-block responses need not synchronize on the common six-set

**Status:** hand-checkable barrier to an intermediate trace-language claim;
the finite assertions are also checked by
[`../results/hc7_k7minus_overlap_trace_synchronization_verify.py`](../results/hc7_k7minus_overlap_trace_synchronization_verify.py).
This is not a counterexample to the `K_7^-` six-colour conjecture.

## 1. Boundary and central vertices

Let

\[
 Z=\{a_1,b_1,a_2,b_2,a_3,b_3\},\qquad
 G[Z]=3K_2,
\]

with matching edges `a_i b_i`.  Add nonadjacent vertices `x,y`, each
complete to `Z`.  Then

\[
 \alpha(G[Z\cup\{x,y\}])=3,
 \qquad K_4\not\subseteq G[Z\cup\{x,y\}].              \tag{1}
\]

The graph `G[Z]` is `K_4`-minor-free and every vertex deletion is a forest,
so it satisfies the common-boundary minor exclusions.  If a further vertex
`u` is complete to `Z\cup\{x,y\}`, every proper equality partition of
`Z` with at most four blocks extends over `x,y,u` in six colours: give
`x,y` one new common colour and give `u` a second new colour.

## 2. Two disjoint complete response languages

Let `P_even` consist of the proper equality partitions of `Z` with at most
four blocks and an even number of blocks.  Define `P_odd` similarly.  The
two families are disjoint.

For every nonempty independent set `I subseteq Z`, each family contains a
partition having `I` as an exact block.  If `I` meets all three matching
edges, then `Z-I` is independent; keeping it as one block or splitting it
into two nonempty blocks gives two and three total blocks.  Otherwise
`Z-I` contains a matching edge.  Then `|I|<=2`, so `|Z-I|>=4`.  A proper
two-colouring of `G[Z-I]` gives three total blocks, while splitting one of
its colour classes gives four total blocks.

Consequently both `P_even` and `P_odd` satisfy every abstract obligation
obtained by contracting one connected `Z`-full subgraph together with an
arbitrarily selected independent block.  They also satisfy the exact
central extension constraint above, but they have no common trace.

## 3. Scope

This refutes the static implication

> if each of two common-boundary response languages contains a return with
> every prescribed independent block, then the languages intersect.

The construction specifies abstract trace languages, not two exterior
graphs realizing them.  It does not encode seven-chromaticity,
minor-criticality, `K_7^-`-minor exclusion, or compatibility between
colourings of related proper minors.  A positive completion may therefore
use an actual Kempe transition, a deletion/contraction relation, or a
structural theorem for an exterior component whose `Z`-full packing number
is one.  It
may not infer a common trace from independent-block coverage alone.
