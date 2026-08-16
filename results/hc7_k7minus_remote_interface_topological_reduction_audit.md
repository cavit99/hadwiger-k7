# Internal audit: remote-interface topological reduction

**Verdict:** **GREEN** for the exact promoted revision below.  This is a
separate internal mathematical audit, not external peer review.

## 1. Exact revision and promotion

The audited source is
[`hc7_k7minus_remote_interface_topological_reduction.md`](hc7_k7minus_remote_interface_topological_reduction.md),
with promoted SHA-256

```text
5bc54f3b7f4cbe68a7b3c35a35d16c693672cfbffa17686f65008938cdfc3865
```

The mathematical text was cold-audited before promotion at SHA-256

```text
a5f2a8521a05685c6a063d9fc5f1cc6a21a929984a011d4d708fcad511c406b8
```

Promotion changed only the status paragraph and relative links.  The one
mathematical wording correction made during the cold audit was already
present at the pre-promotion hash: the fresh crossing-edge deletion is not
claimed to preserve the fixed exact model.

## 2. Hypotheses and dependency closure

The critical-host hypotheses imply every assumption used downstream.
Exclusion of a `K_7^-` minor excludes a `K_7` minor, and the remote edge
guarantees that `G-N[z]` is nonempty.  The following exact dependency
revisions were checked against their adjacent GREEN audits:

```text
2f7c69fd57319f898d84c9884907ac70e3e1f2064b3a5753d19da8531406ecf9  remote removable-edge operation cube
4ee48c6d71c994b166b29dcd969d64c3526e6b6b75fa8a849fae834cf95eea29  low-degree exterior-component bounds
57d05838dfa92fa7ebd12ede1946f84b13e1a4839cd67a2359ae39b649e4f8c1  exact three-full-subgraph completion
1041988a33b749bef5802dd21d3cd9419b5afc754735a20174bf5a13c0a56c96  three-component seven-cut exclusion
8aa99a023ae2247dd24835a158c17677d1e3da218c9a431be36891e54119b758  both-full shore reduction
```

The operation-cube theorem supplies the named edge `f`, the four-edge
forest `T`, all fifteen nonempty equality signatures, all eighty mixed
operation patterns, and the fixed spanning exact `K_7^\vee` model.  The
low-degree theorem bounds the number of exterior components by two.  The
exact `(1,2)` consequence supplies `\chi(G[Q])\le3` in the only putative
connected order-seven case.  The critical seven-cut corollary supplies
exactly two complementary components at every order-seven cut; ordinary
seven-connectivity then makes both components full.  The both-full theorem
has precisely the hypotheses needed in outcome 4.

## 3. Exhaustive and mutually exclusive topology

For the component `C` containing `f`, its boundary `Q` is a subset of the
eight-set `N(z)` and separates `C` from `z`, so `|Q|` is seven or eight.
Together with the one-or-two-component bound, this gives the complete case
split.

- If `|Q|=7`, write `N(z)=Q\dot\cup\{w\}`.  The connected exterior case
  is excluded by the argument audited in Section 4 below.  With a second
  component `E`, deleting `Q` must leave one opposite component containing
  `z,w,E`; because `z` has no edge to `E`, this forces `wE` contact.
  Seven-connectivity gives `|N(E)|\ge7`, so `E` is full or misses exactly
  one vertex of `Q`.  These are outcomes 2 and 1 respectively.
- If `|Q|=8`, then `Q=N(z)`.  A connected exterior is outcome 3.  With a
  second component `E`, its boundary has order seven or eight, yielding
  outcome 1 or outcome 4.

The outcomes are mutually exclusive: outcome 3 is the sole one-component
row; in the two-component rows outcome 1 has the component distinct from
`C` nonfull, outcome 2 has `C` nonfull and the other component full, and
outcome 4 has both components full.  No exterior-component topology or
boundary order is omitted.

## 4. Connected order-seven contraction colouring

If the exterior were the single component `C` with `|Q|=7`, the remaining
neighbour `w` has no neighbour in `C`.  Hence all of its neighbours lie in
`Q\cup\{z\}`; minimum degree eight makes `w` complete to `Q`.  Thus `C`,
`{z}`, and `{w}` are three disjoint connected subgraphs full at `Q`, with
the last two adjacent.  The exact `(1,2)` theorem correctly gives
`\chi(G[Q])\le3`.

Delete a smallest class `Z` from a three-colouring when all three colours
occur, or take `Z=\varnothing` when only two occur.  The boundary contains
an edge, so the two remaining independent classes `P,R` may be taken
nonempty, and `|Z|\le2`.  Contracting the two disjoint stars
`\{z\}\cup P` and `\{w\}\cup R` gives a proper minor.  In a six-colouring
of that minor, the two contraction images have distinct colours because
`zw` survives.  Expansion properly colours `G[C\cup Q]` and uses at most
`2+|Z|\le4` colours on `Q`.  Two distinct palette colours absent from `Q`
can then be assigned to `z,w`; neither has a neighbour in `C`, both are
complete to `Q`, and they are adjacent.  This is a valid six-colouring of
all of `G`, the required contradiction.

## 5. Exact-seven responses and model scope

In outcome 1 every edge of `T` lies outside the closed `E`-shore: the
three spoke edges use the absent centre `z`, and the remote edge lies in
the other exterior component `C`.  Therefore all fifteen signature
colourings restrict properly to `G[E\cup S]`.  If any induced boundary
partition extended through the intact opposite closed shore, colour-name
alignment would glue the two proper shore colourings and six-colour `G`.

For a crossing edge `h=es`, minor-criticality six-colours `G-h`; its ends
must receive one colour.  Removing `E` removes that sole conflict, so the
restriction to `G-E` is proper and its partition is rejected by the intact
`E`-shore.  Equality with any of the fifteen opposite partitions would
again glue to a six-colouring of `G`.  This proves the claimed
partition-disjoint opposite response.  The fifteen labelled responses are
not asserted to induce fifteen distinct boundary partitions.

The fixed exact model remains available in the original deletion host
`H=G-T`.  Since the fresh crossing edge is not in `T`, it belongs to `H`
and might be essential to a branch set or bag adjacency.  The corrected
source therefore explicitly makes no claim that the model survives in
`H-h`.  This is the exact safe persistence statement.

## 6. Order-eight both-full row

When both exterior components are full at `N(z)`, all hypotheses of the
audited both-full shore reduction hold: `z` is exceptional of degree eight
and the anti-neighbourhood has exactly the two full components `C,E`.
That result returns exactly its seven named boundary types and

```text
(mu_{N(z)}({z}), mu_{N(z)}(C), mu_{N(z)}(E)) = (1,1,1).
```

The present theorem correctly preserves the centre-star and remote-edge
response labels only as existing colourings.  It does not identify those
labels with the classified boundary demands, boundary partitions, or
fixed-model branch-set contacts.

## 7. Novelty, duplication, and trust boundary

The two-vertex-shore contraction used in Section 4 is essentially the
mechanism already recorded in the GREEN active
[`two-vertex-shore bipartite contraction`](../active/hc7_two_vertex_shore_bipartite_contraction.md).
It is re-proved in full here, so the active note is not a logical
dependency.  The new contribution is the remote-edge-centred exhaustive
topological synthesis, the elimination of its connected order-seven row,
and the common exact-seven shore carrying all fifteen operation-labelled
responses against a fresh partition-disjoint crossing response.

The theorem inherits the finite-computation trust boundaries of the
low-degree exterior-component theorem and the both-full seven-type
classification.  It does not terminalise outcomes 2--4, synchronize a
response partition with the fixed model, prove the `K_7^-` six-colour
conjecture, or prove `HC_7`.

All referenced local files and the exact-section anchor resolve.  The
promoted source and this audit pass Git whitespace checking.
