# Internal self-audit: dominated degree-eight exterior connectivity

**Verdict:** **GREEN as a self-check.**  The 729-case quotient lemma, its
unbounded lift to exterior connectedness, and the complete four-coordinate
response family on the resulting order-seven/eight boundary are correct at
the pinned revisions.  The 46 surviving one-component quotients correctly
show that static near-complete attachment alone does not close the connected
case.

This audit was written by the same agent as the theorem and verifier.  It is
not a cold independent audit and is not external peer review.

## Exact revisions

The checked theorem is
[`hc7_k7minus_dominated_degree_eight_exterior_connectivity.md`](hc7_k7minus_dominated_degree_eight_exterior_connectivity.md),
with SHA-256

```text
c25bfc5f71d69bbddfb8d4880c017326c5f77dc32428071a99d244637bfeb26b
```

The finite materials are pinned as follows:

```text
6f3328ad431190ede28aea943073732d5d65f78623540ca276df098bb85dc5ec  active/experiments/dominated_singleton_two_exterior_completion/verify.py
b06f87e8072417fb3868c4b62fe665ba092f14f6b918105c95f9bda174a9622d  active/experiments/dominated_singleton_two_exterior_completion/README.md
81980e29daba936ace8e599a1147ffad233a227718247cce8872cadbbe9d4495  active/experiments/dominated_singleton_low_degree_completion/verify.py
```

The new verifier imports the exact graph and minor routines from the third
file.  Its direct mathematical dependencies were checked at these revisions:

```text
90c1a84a934ca2848c35152b3a0d0b089da55f308fa829f2add24addbcba8749  results/hc7_k7minus_singleton_coordinate_localisation.md
204365dd5d68e9b80d84b346fe0b796cd3bb817ac10f34c718de884b882b19d0  results/hc7_k7minus_dominated_singleton_twocut_response.md
fc1e88c28b1f4d0dc7a1cbdeefa19fecfd5e969b986c64e11eb1990615f5dfbd  results/hc7_k7minus_exceptional_neighbourhood_completion.md
7ebbc04ccdac9488088e3620ea949a5f08bdcc659fcffd5316e934cdc99c9292  active/hc7_k7minus_degree_eight_centre_cube_interface.md
```

The promoted dependencies have separate GREEN internal audits.  The final
active dependency has the adjacent GREEN self-audit pinned above.

## 1. Finite enumeration and minor test

The verifier asks `geng -q -t 7` for one representative of every unlabelled
triangle-free graph of order seven.  It independently computes the
independence number, rejects graphs containing a `K_5^-` minor, and retains
only graphs with a vertex cut of order zero, one, or two.  Exactly nine
graphs survive.

For each surviving graph, a contracted exterior component must see at least
seven of the eight vertices in `\{v\} union V(Q)`.  It therefore has exactly
nine possible profiles: miss none, or miss one named interface vertex.  Two
distinct exterior components are anticomplete and are both nonadjacent to
`u`, so their profiles vary independently.  The script consequently checks
exactly `9*9^2=729` quotients.

The imported `has_dense_minor` routine recursively enumerates vertex
deletions and edge contractions.  When the graph reaches the target order,
at least 20 edges on seven vertices is equivalent, after permitted edge
deletions, to containing `K_7^-`; at least nine edges on five vertices is
equivalent to containing `K_5^-`.  Thus the density terminal test does not
weaken either minor question.  Memoisation affects performance only.

The reproduction command was rerun at the pinned revisions and printed

```text
GREEN dominated degree-eight singleton two-exterior completion eligible_Q=9 profiles=729 one_component_survivors=46 survivor_graphs=6 live_profile_survivors=10 live_graphs=5
```

Assertions guard the eligible count, all 729 positive minor conclusions,
the 46 negative one-component conclusions, and their distribution over six
base graphs.  The search is exact but has no separately generated
certificate; its trust boundary is the short verifier, Python runtime and
nauty enumeration.

## 2. Unbounded host lift

For a component `C_i` of `G-N_G[u]`, its full neighbourhood lies in the
eight-set `N_G(u)` and separates `C_i` from `u`.  Seven-connectivity therefore
gives at least seven boundary neighbours.  Contracting two distinct
components produces nonadjacent vertices `c_1,c_2`; neither is adjacent to
`u`, and each has one of the enumerated profiles on `\{v\} union Q`.
Deleting the other exterior vertices cannot invalidate a minor found in the
quotient.  Lemma 1.1 therefore contradicts target exclusion whenever two
components exist.

The live dominated singleton has `|Q|=7`.  Its imported neighbourhood
structure makes `Q` triangle-free and `K_5^-`-minor-free.  The degree-eight
exceptional-neighbourhood theorem gives `alpha(G[N(u)])=3`; since the
dominating vertex `v` is complete to `Q`, every independent triple lies in
`Q`, giving `alpha(Q)=3`.  The audited Wood--Woodall application gives a cut
of order at most two.  Finally, `|V(G)|>=25` and `|N_G[u]|=9` make the
exterior nonempty.  These are exactly the hypotheses needed for Corollary
2.2.

## 3. Response-family consequence

All four other independent degree-eight centres lie outside `N_G[u]`.
Exterior connectedness puts all four in the unique component `C`.  Hence the
component-localisation theorem applies with all four of their matching edges,
not just a pair.  Its actual boundary `T=N_G(C)` has order seven or eight;
the canonical `u` response is proper on `G[C union T]`, and every one of the
15 nonempty signatures on the other four centre edges is proper on
`G-C=G[N_G[u]]`.  Section 3 imports no additional model or colouring
compatibility.

The two-full-shore strengthening is also exact.  If `T=N_G(u)`, deletion of
`T` leaves precisely `C` and `{u}`.  If one neighbour `s` is missed, it
leaves precisely `C` and the edge `{u,s}`; the definition of `T` makes `s`
anticomplete to `C`.  The component `C` has neighbourhood `T` by definition,
and `u` is adjacent to every vertex of `T`, so both components are full.
No claim about the internal order of `C` is introduced.

For an order-seven boundary, the missed neighbour `s` has no exterior
neighbour.  Minimum degree eight forces it to see `u` and every member of
the seven-set `T`.  If `s` belonged to `Q`, triangle-freeness would then
make the other six vertices of `Q` independent, contradicting
`alpha(Q)<=3`; hence `s=v`.  The contracted exterior therefore has only the
two profiles screened in Corollary 3.3: full interface attachment, or the
single miss at `v`.  The verifier leaves ten labelled profile instances,
two for each of five graph6 types.  Direct inspection of their edge lists
gives exactly the five standard descriptions displayed in the corollary.

The complete language separation in Corollary 3.4 spends only the exact
two-shore geometry.  At order eight, a colouring of `G-u` must use all six
colours on `N(u)`, whereas `u` excludes its own colour from the singleton
shore boundary.  At order seven, `T=Q`: the adjacent vertices `u,v`, each
complete to `Q`, consume two distinct colours outside `Q`, so the edge
shore has at most four boundary blocks.  An exterior-shore colouring with
at most four blocks would leave two palette colours for `u,v` and extend to
all of `G`, so that shore has at least five.  These arguments concern every
shore colouring, not only the displayed response colourings.

## 4. Negative one-component diagnostic and scope

The final 81-profile loop uses the same exact routine with one contracted
component.  It finds 46 target-free quotient profiles with distribution
`9+9+9+9+9+1`.  These are explicit finite obstructions to any inference
using only the displayed quotient and one near-complete attachment.

They are not counterexamples to the critical-host terminalisation target:
the quotients need not be seven-connected or seven-chromatic and do not
retain the spanning exact model or complete response cube.  The theorem
therefore correctly concludes only that the dominated exterior is connected
and carries the four-coordinate bounded response family.  It does not prove
the rooted `K_5^-` model, eliminate the connected residue, close the full
eight-coordinate branch, prove Conjecture 21, or prove `HC_7`.

No material gap was found in the stated host reduction.  Promotion of the
computer-assisted lemma would require a separate audit or independent
checker.
