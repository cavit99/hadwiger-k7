# Internal audit: the cycle-and-triangle exterior

**Verdict: GREEN.** This separate internal mathematical audit covers all
three conclusions, minimum-degree corollary and cutvertex corollary of
[the source](hc7_degree8_cycle_exterior.md), at
whole-source SHA-256
`6c5196ea71f77a1426d8bc24ef040e7fe85805ac0cb784d2d62d152a67303eb3`.
It is not external peer review or a proof of Conjecture 19 or HC7.

The two invoked source hashes were checked against their adjacent GREEN
audits: connected-triple closure at `ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`,
and the rooted-wheel theorem at `f0fbab79d23d8079b91ff1a812b83db96059aa4fb0024c809b1037f3f533f62a`.
Their stated connectivity and degree hypotheses hold here; the wheel's
Corollary 4 applies to the spanning cycle, without assuming it induced.
No new literature application or finite census is used.

## Strongest inference and ownership checks

Contracting `{x,0,4}` retains four distinct neighbours of `v` with all
five diamond edges. This is one contraction of a connected original
triple, precisely within the input's scope. The corrected degree count
allows cycle chords: a cycle vertex has at most six neighbours in `N[v]`,
so its minimum degree forces an exterior neighbour.

If an exterior component misses `t`, its seven-root side retains every
nonroot neighbour. Every nonempty nonroot set therefore has boundary at
least seven, since `v` remains outside. The other component meeting `t`
exists by its degree and the single cycle-to-triangle edge bound. Its
four cycle contacts permit choosing the two contracted cycle edges so
that it meets all three resulting roots. These contractions lose at most
two neighbours per vertex or nonroot set, yielding the wheel's exact
degree-six and internal-five hypotheses. Their fixed preimages are
disjoint. The other component together with `t`, and singleton `v`, are
adjacent helpers full to the lifted wheel, giving `K_2 join W_4=Q`.

For three components, their cycle-neighbour sets have a common vertex.
The three arcs of orders `1,2,2`, with one assigned component each, are
connected, pairwise adjacent, and full to the literal four-clique.
For two components, the crucial omitted cycle vertex `a` has no contact
to the chosen component. Thus a boundary of order at most four in its
five-root side lifts by at most two actual vertices, contradicting
seven-connectivity. Individual nonroot degree loss is at most two by
the first conclusion. The opposite component plus an omitted neighbour
`d` is disjoint from this side and full to its five prescribed bags.
Together with `v` it completes `Q`. If both components contact all cycle
vertices, the displayed three apex bags and contracted cycle give
`K_3 join C_4=Q` directly.

The appended degree corollary uses the checked contraction input's
Corollary 3 with the literal clique `{v,r,s,t}`. A vertex of `B` has at
most two triangle contacts. If it has two, it cannot neighbour a cycle
vertex: that neighbour's clique contact `v` lies outside the pair, violating
the corollary's containment. Thus a vertex meeting the cycle loses at most
two cycle neighbours and one triangle neighbour; a vertex missing it loses
at most two neighbours. Original minimum degree eight yields `delta(G[B])>=5`.

For the cutvertex corollary, a component with at most one triangle
contact must meet exactly one triangle root and all five cycle vertices.
Its complement `K` in `B` is connected. The specified neighbourhood of
`L union M` contains every possible external neighbour, and another
triangle root survives outside it. Thus the seven-connectivity count
forces `|M|<=2`; equality supplies the stated extra cross-edge. The three
displayed bags are disjoint and connected, with their pairwise contacts
supplied by the literal four-clique. Two are full to the cycle, and the
third misses at most one cycle vertex. The prescribed edge contraction
retains four connected rim bags full to all three, giving `Q`.

## Remaining scope

No unresolved gap was found in these deductions. All required contacts
use literal roots or disjoint component preimages. No quotient is
assumed critical and no unproved induction is used. A single connected
exterior full to all eight neighbours remains; this result supplies no
partition into compatible helper bags and does not close the global target.
