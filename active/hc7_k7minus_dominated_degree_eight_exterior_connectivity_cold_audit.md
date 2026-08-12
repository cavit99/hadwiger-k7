# Cold internal audit: dominated degree-eight exterior connectivity

**Verdict:** **GREEN.**  The finite two-component lemma, its unbounded host
lift, the exact two-full-shore response interface, and the reduction to five
common-neighbour graphs are correct at the pinned revisions.  The surviving
connected exterior remains unbounded; the theorem does not close the
eight-coordinate branch.

This audit was carried out by an agent other than the author of the theorem
and verifier.  It is an internal cold audit, not external peer review.

## Exact revisions and reproduction

```text
c25bfc5f71d69bbddfb8d4880c017326c5f77dc32428071a99d244637bfeb26b  active/hc7_k7minus_dominated_degree_eight_exterior_connectivity.md
6f3328ad431190ede28aea943073732d5d65f78623540ca276df098bb85dc5ec  active/experiments/dominated_singleton_two_exterior_completion/verify.py
b06f87e8072417fb3868c4b62fe665ba092f14f6b918105c95f9bda174a9622d  active/experiments/dominated_singleton_two_exterior_completion/README.md
81980e29daba936ace8e599a1147ffad233a227718247cce8872cadbbe9d4495  active/experiments/dominated_singleton_low_degree_completion/verify.py
```

The new verifier imports its graph and exact minor routines from the final
file above.  It was rerun at these revisions and printed

```text
GREEN dominated degree-eight singleton two-exterior completion eligible_Q=9 profiles=729 one_component_survivors=46 survivor_graphs=6 live_profile_survivors=10 live_graphs=5
```

## 1. Finite two-component lemma

The verifier enumerates every unlabelled triangle-free graph of order seven
with `geng -t`, computes its independence number directly, excludes a
`K_5^-` minor by exact vertex deletion and edge contraction, and checks all
vertex cuts of order at most two.  Exactly nine graphs satisfy the stated
hypotheses.

A contracted exterior component has at least seven neighbours in the
eight-vertex interface `\{v\}\cup V(Q)`, so it misses either no interface
vertex or one named interface vertex.  Two distinct exterior components are
anticomplete, and their nine choices are independent.  The search therefore
covers exactly

\[
                              9\cdot9^2=729
\]

quotients.  Every quotient passes the exact `K_7^-` minor test.

The imported minor routine is exhaustive: it recursively considers every
vertex deletion and edge contraction until the target order is reached.  On
seven vertices, at least twenty edges is equivalent, after harmless edge
deletion, to containing `K_7^-`; on five vertices the analogous nine-edge
test is exact for `K_5^-`.  Memoisation changes only runtime.

## 2. Unbounded host lift

For every component `C_i` of `G-N_G[u]`, its full neighbourhood lies in the
eight-set `N_G(u)` and separates `C_i` from `u`.  Seven-connectivity gives
`|N_G(C_i)|>=7`.  Contracting two components creates precisely the two
anticomplete, non-`u`-adjacent quotient vertices in the finite lemma; a
forbidden minor in the quotient lifts to `G`.  Thus a target-free host has
at most one exterior component.  The critical-host order bound makes the
exterior nonempty, so it is connected.

In the live dominated degree-eight case, `Q=N_G(u)-\{v\}` has order seven,
is triangle-free and `K_5^-`-minor-free, and has a cut of order at most two.
The exceptional-neighbourhood theorem gives `alpha(G[N(u)])=3`; since `v`
is complete to `Q`, an independent triple lies wholly in `Q`, and hence
`alpha(Q)=3`.  These are exactly the hypotheses used in the finite lemma.

## 3. Exact two-full-shore interface

Let `C=G-N_G[u]` be the now unique component and `T=N_G(C)`.  Its boundary
is contained in `N_G(u)`, and seven-connectivity gives `7<=|T|<=8`.
Everything outside `C\cup T` is

\[
 A=N_G[u]-T=
 \begin{cases}
  \{u\},&T=N_G(u),\\
  \{u,s\},&T=N_G(u)-\{s\}.
 \end{cases}
\]

In the second case `us` is an edge.  Neither `u` nor `s` has a neighbour
in `C`, by the definitions of the exterior and `T`; hence `A` is the only
other component of `G-T`.  Both components are `T`-full: this is the
definition of `T` for `C`, while `u` is adjacent to every vertex of `T`.

All four other independent centres lie in `C`.  The canonical
`u`-coordinate colouring is proper on `G[C\cup T]`, because its sole
monochromatic restored edge has endpoint `u` outside that shore.  For any
nonempty signature on the other four centre edges, deleting `C` removes
the centre endpoint of every monochromatic edge, so its restriction to
`G[A\cup T]=G-C` is proper.  If any displayed partition extended through
the opposite shore, a palette permutation would align the two restrictions
on `T` and six-colour `G`.  Thus all fifteen opposite responses and the
canonical response are correctly retained on one exact full separation.

## 4. The five surviving common-neighbour graphs

If `|T|=7`, write `N_G(u)-T=\{s\}`.  The vertex `s` has no neighbour in
`C`.  Minimum degree eight forces it to be adjacent to `u` and all seven
vertices of `T`.  If `s` lay in `Q`, it would be complete to the other six
vertices of the triangle-free graph `Q`, forcing those six vertices to be
independent, contrary to `alpha(Q)<=3`.  Hence `s=v`, so `T=Q`.

Consequently the contracted exterior component has only two live profiles:
it sees all of `\{v\}\cup Q` when `|T|=8`, or it sees all of `Q` and misses
only `v` when `|T|=7`.  The verifier checks both profiles for every one of
the nine eligible graphs.  Exactly ten profile instances survive, two for
each of the following five graph6 strings:

```text
FCQ`_
FCQb_
FCR`o
FCp`_
FCpb_
```

Their degree sequences, component sizes, and triangle-free structure verify
the descriptions in the theorem, respectively:

1. `C_5 dotunion K_2`;
2. `C_5` with a pendant path of length two;
3. the theta graph with path lengths `2,3,3`;
4. `C_7`; and
5. `C_7` with a chord forming cycles of orders four and five.

The sixth static one-component survivor, `FCpV?`, survives only a profile
which misses a vertex of `Q`; the host argument excludes that profile, so
its removal is valid.

## 5. Complete shore-language separation

The complete shore-language separation in Corollary 3.4 is correct.  When
`|T|=8`, the exterior closed shore is `G-u`.  Every one of its proper
six-colourings uses all six colours on `T=N_G(u)`, since a missing colour
would extend to `u`.  On the other closed shore, `u` is adjacent to every
boundary vertex, so its colour is absent from `T` and at most five boundary
blocks occur.

When `|T|=7`, the preceding host argument gives `T=Q` and the other open
component is the edge `uv`.  In a colouring of its closed shore
`G[\{u,v\}\cup Q]`, the adjacent vertices `u,v` use two distinct colours;
both colours are absent from `Q` because both vertices are complete to
`Q`.  Thus this shore induces at most four blocks on `Q`.  Conversely, if
a colouring of `G[C\cup Q]` induced at most four blocks, two of the six
palette colours would be unused on `Q`.  Assign those two colours
distinctly to `u,v`.  Neither vertex has a neighbour in `C`, and both are
complete to `Q`, so this extends to a proper six-colouring of `G`, a
contradiction.  Every exterior-shore partition therefore has at least five
blocks.  This verifies disjointness of the complete languages, not only of
the fifteen exhibited response partitions.

## 6. Scope

The five quotient graphs are not five complete host classifications.  The
unique exterior component may have arbitrary order, and its internal
geometry, the exact-model labels, and the fifteen operation-labelled
colourings are not encoded by the contracted quotient.  The theorem
therefore correctly stops before a rooted `K_5^-` model, a common boundary
partition, closure of the eight-coordinate branch, Conjecture 21, or
`HC_7`.  No gap was found in the stated conclusions.
