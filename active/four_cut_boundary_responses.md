# Chosen boundary responses at a missed-root four-cut

**Status:** written proof; a [separate exact-source internal audit](four_cut_boundary_responses_audit.md)
is recorded beside it. This reduces the possible minimum colouring
responses. It does not exclude all four-cuts,
close C19, or meet the HC7 / substantiated NT-comparable completion criterion.

All graphs are finite and simple; set neighbourhoods are external.
Put `Q=K7-2K2`. Assume G is seven-connected, has minimum degree at least
eight, has no Q minor, has chromatic number seven, and every proper minor
is six-colourable. Let `d(v)=8`, with `N(v)=A dotcup B dotcup {x,y}`
containing the two triangles A,B and edge xy. Put `R={v} union B` and
`F=G-R`. Let S be a four-cut of F, and let C,D be its two components.
Suppose C misses `r in R`. Write

`T=R-{r},  Z=T union S,  E=D union {r}`.

**Proposition.** Both `G[C union S]` and `G[E union S]` contain a
K4 rooted at S. Among all proper six-colourings of the two original
closed sides `G[C union Z]` and `G[E union Z]`, the minimum number of
colour classes meeting Z is either three or four. In particular, a
minimum response cannot have five or six boundary classes. If that
minimum is four, its block sizes are `3,2,1,1` or `2,2,2,1`, and Z
has no independent four-set.

## Pinned inputs and the actual sides

The [four-cut theorem](../results/hc7_four_cut_components.md), source
`2986fb1f55c2cbaa4572b7c88e287ed5aa4230f34ab3b63dabe4d840e247e03f`,
[audit](../results/hc7_four_cut_components_audit.md)
`7a9d05d3874f6a6da0fabda90493660ee893fb0fd7e29ab5afe8ef42ae3fa437`,
gives exactly two components, each full to S and meeting at least three
R vertices, and `|N(r) intersect S|<=1`.

We use [contraction closure, Theorem 1 and Corollary 3](hc7_companion_contraction_closure.md),
source `ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`,
[audit](hc7_companion_contraction_closure_audit.md)
`26b2f5ad7226c7bb3f194cac8523f043d7ae6ca955036249f04ddc9fb6d94394`.
Every outside-R vertex has at most two R-neighbours, and every edge
quotient has no literal K5-minus. Consequently any three vertices
spanning an edge have at most two common neighbours: for a triple
`{a,b,c}` with edge ab and three common neighbours p,q,s, contracting
cp gives a literal K5-minus on `{a,b,cp,q,s}`, whose only possible
missing edge is qs.

The [four-root exception theorem](../results/four_root_degree_five_exceptions.md),
source `a9bda26dcd8057cad14e2b52b33bec0700ecf8b2c64d60642afd1962e7d34067`,
[audit](../results/four_root_degree_five_exceptions_audit.md)
`194457425ddfe6a134d16ffdee477d8e29fd2790e28626012df89a44cb9fbbe9`,
supplies a prescribed-root K4 when there are at least three nonroots,
every nonroot subset has at least four neighbours, all nonroot degrees
are at least five, and at most five are exactly five.

Each of C,D has at least three vertices: otherwise an outside-R vertex
there has degree at most `1+4+2=7`. The vertex r has at least five
F-neighbours, misses C and sees at most one S vertex, so it contacts D.
Thus C and E are connected, nonempty, anticomplete open sides of Z.
Seven-connectivity makes each full to Z. For every nonempty subset X
of either open side, `|N_G(X)|>=7`, since the other open side survives
outside `X union N_G(X)`.

On C+S, deleting T leaves nonroot degree at least six and subset boundary
at least four. On E+S the same holds for D vertices; only r can have
degree five, since it loses its three T-neighbours. Both have at least
three nonroots. The four-root theorem gives the two asserted models.
Contracting one model and deleting unused vertices on its open side
gives a proper minor in which S is a clique. Expanding its six-colouring
only on the untouched closed side gives a response with S all distinct.
T is already a triangle. Such responses have only S--T pairs and
singletons, but subsequent response choices need not keep S distinct.

## Reflection of a chosen minimum response

A boundary response is the equality partition of Z in a proper
six-colouring of one original closed side. Both languages are nonempty
because those sides are proper subgraphs of G. Choose a response pi
with the minimum number k of blocks over their union. The triangle T
gives `3<=k<=6`.

Call pi realisable on its coloured side if there are disjoint connected
sets, one for each block, whose intersections with Z are exactly those
blocks. Singleton blocks may use singleton sets; unused open-side
vertices may be deleted. Contract these sets and delete those unused
vertices. If at least one open-side vertex is consumed or deleted, this
is a proper minor. Its six-colouring expands on the untouched closed
side by giving all vertices of each old block the contracted colour.
This is proper: each block was independent in G, and every original
edge of that untouched side survives between the corresponding images.
The new response is a coarsening of pi. Minimality of k forces equality
of the partitions. Permuting colours then glues the two original
closed-side colourings into a six-colouring of G, a contradiction.

Every realisation used below consumes a nonempty open side, either by
deletion or contraction. No colouring is expanded through its consumed
interior. A partition with just one nonsingleton block I is always
realisable: unite I with the entire connected open side, which meets
every boundary vertex, and keep other roots singleton.

## Excluding five and six blocks

If k=6, the only nonsingleton block is a pair, so reflection applies.
If k=5, a triple and four singletons is likewise terminal. The other
possibility is two pairs and three singleton roots U.

If U spans an edge, delete U on the coloured side. The four remaining
boundary roots are the pair endpoints. Every nonroot subset still has
at least four neighbours and every nonroot has degree at least five.
A degree-five vertex must have had degree eight in G and must be
adjacent to all three deleted vertices. The common-neighbour bound
therefore leaves at most two exceptions. The four-root theorem gives
a rooted K4 on the four endpoints. Merge the bags within each prescribed
pair, using their actual K4 contact. The resulting two connected sets,
with the three U roots singleton, realise pi. Reflection contradicts
minimality.

If U is independent, contract U together with either whole open side.
The contracted vertex is adjacent to all other four boundary vertices,
since that open side is full to Z. Expanding only U on the untouched
side gives a response in which U is one block, distinct from the other
four roots, so there are at most five blocks. Minimality k=5 makes the
other four roots distinct. This is the already excluded one-triple
response. Hence `k<=4`.

For k=4 the sole-nonsingleton pattern `4,1,1,1` is excluded by reflection,
leaving precisely the two patterns in the proposition. If Z had an
independent four-set, its contraction with one whole open side would
produce at most four blocks and, by minimality, exactly the excluded
`4,1,1,1` pattern. This completes the proposition.

## Exact remaining construction

At k=4, the unresolved patterns are `3,2,1,1` and `2,2,2,1`.
At k=3 the one-nonsingleton pattern is excluded, leaving
`4,2,1`, `3,3,1` and `3,2,2`. A proof may change the chosen colouring
or use either open side; it need not realise every boundary partition.
For `3,2,1,1`, deleting the singleton roots gives the hypotheses of the
[relative five-root wheel theorem](../results/five_root_relative_degree_six_wheel.md),
source `46a2211c03938afb9fd5fc3e8e309f31ab7d102c3211a51f7a1c6e1adcb5ed6d`,
[audit](../results/five_root_relative_degree_six_wheel_audit.md)
`1c67692b6ce69ae068e9d1b14cc4b4f2884cc4d9c888373c76e5698c88f7163e`.
That wheel realises the partition
when its two pair roots are adjacent. Opposite rim ownership is not
resolved. No simultaneous three-pair realisation or valid improving
exchange is asserted. The full four-cut exclusion remains open.
