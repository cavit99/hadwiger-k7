# Internal audit: critical seven-cut capacity and three-component boundary

Audited file:
`results/hc7_k7minus_critical_seven_cut_capacity.md`.

Audited SHA-256:

```text
d4d650fee168fc2ff0e00a3b7b0faed6ff674ba8cd3c06c263f63c4170656f34
```

**Verdict:** **GREEN** for the exact revision above.

This is a separate internal mathematical audit, not independent human review
or external peer review.  Two cold agent audits reconstructed the proof;
one also checked the seven-vertex chromatic lemma against all graphs in the
NetworkX graph atlas.  That enumeration is corroboration only.  The written
proof is computation-free.

## 1. Exact boundary-colouring reflection

For every assigned boundary block `B_j`, the set

\[
                         V(P_j)\cup B_j
\]

is connected because `P_j` is connected and adjacent to every literal
vertex of `B_j`.  The sets belonging to different blocks are disjoint.
Contracting a spanning tree in each set is a proper minor operation: every
assigned nonempty block has an actual edge to its connected subgraph.

The contracted representatives and the retained singleton-block clique are
pairwise adjacent.  Fullness supplies every representative--representative
and representative--singleton adjacency, while the retained vertices are a
clique by hypothesis.  Hence a six-colouring gives different colours to
different partition blocks.

The pullback is only to the untouched opposite closed shore.  Each assigned
block is independent, and every edge from it to an untouched vertex was
represented at its contracted image.  No contracted connected subgraph is
expanded on its own shore.  The representative clique therefore makes the
pulled-back equality partition exact, not a coarsening.

## 2. Excluding four full connected subgraphs

When the boundary has maximum degree one, its vertices split as

\[
                         I_1\mathbin{\dot\cup}I_2
                         \mathbin{\dot\cup}\{q\},
                         \qquad |I_1|=|I_2|=3,
\]

with `I_1,I_2` independent.  Two full connected subgraphs on each shore
reflect this same three-block partition in both directions.  Palette
permutation aligns the block colours, and the shore colourings glue because
the open shores are anticomplete.

For a one-versus-three distribution, the thin shore contracts one full
connected subgraph with an independent boundary four-set.  That four-set is
an exact returned colour class.  The remaining three vertices form at most
three blocks, all of which the rich shore can reproduce using its three
full connected subgraphs, retaining one literal singleton only when all
three residual vertices are singleton blocks.  The resulting exact
partitions again align and glue.

For the maximum packing parameters, every connected subgraph of `G-S` lies
in one component.  Thus

\[
                              \pi_S(G)=\sum_i\mu_i
\]

in both directions: a global family restricts to at most `mu_i` members in
component `C_i`, while maximum componentwise families unite to a global
family.  Every positive composition of four with at least two parts admits
a component grouping of type `2+2` or `1+3`.  The audited general capacity
theorem supplies both `pi_S(G)<=4` and the maximum-degree-one boundary at
equality, so the two reflection arguments prove `pi_S(G)<=3`.

## 3. Three-component boundary

For three components, the packing identity forces

\[
                              \mu_1=\mu_2=\mu_3=1.
\]

The dependency theorem gives `|E(G[S])|<=9`.  A literal boundary `K_4`,
together with the three full components anchored at the other three
boundary vertices, is an explicit seven-bag `K_7` model.  Hence the boundary
is `K_4`-free.

The small critical-graph argument proving three-colourability is complete.
If a four-critical subgraph `F` existed, then `delta(F)>=3`.

- On four vertices it is `K_4`.
- On five vertices parity forces a universal vertex; deleting it leaves a
  three-chromatic four-vertex graph and hence a triangle, producing `K_4`.
- On six vertices either one degree is at least four, giving at least ten
  edges, or `F` is cubic.  The complement of a six-vertex cubic graph is
  `C_6` or two disjoint triangles, and either form gives an explicit
  three-colouring of `F`.
- On seven vertices minimum degree three gives at least eleven edges.

All cases contradict the nine-edge, `K_4`-free boundary.  Thus
`chi(G[S])<=3`.  Reflecting a fixed one- or two-block proper boundary
partition through the other two components would six-colour `G`, so the
reverse inequality holds.  Similarly, any three-colouring having a
singleton class can be reproduced componentwise using the other two full
components while retaining that singleton.  Therefore every proper
three-colouring has class sizes `3,2,2`.

## 4. Two-component case, provenance, and scope

For two components, the packing identity gives total packing at most three
and makes one component's boundary-full packing number equal to one.  An
independent boundary would admit
the one-block reflection in both directions, so the boundary has an edge.

The capacity-three conclusion and four-component exclusion overlap older
audited exact-seven packing and adaptive reflection results.  They are a
shorter self-contained specialization, not a new repository claim.  The new
deduction in this theorem is the combination of the `K_7^-` nine-edge
boundary bound with the critical-host colouring argument, which removes the
formerly surviving four-chromatic three-component boundary and forces the
exact three-chromatic conclusion.

The only theorem dependency is the separately audited seven-boundary
capacity theorem at source SHA-256

```text
9e2f616c98dd17670f4d15e962f3b36e4fc1f4c4dc9aee4227eabeb51ca33913
```

No unresolved mathematical assumption was found.  The result essentially
uses proper-minor six-colourability.  It does not exclude four-component
cuts in arbitrary seven-connected graphs, prove a density-preserving
component contraction, prove the bare `4n-4` extremal theorem, or settle the
`K_7^-` six-colour conjecture or `HC_7`.
