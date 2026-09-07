# Audit of two companion-induction counterexamples

**Verdict:** GREEN at source SHA-256
`f3761a2a22c7c13f56b39ce0e28ee226d6871be566b13ff176d27badf2a2ce81`
for [the counterexample source](hc7_companion_induction_shortcuts.md).
This is an internal mathematical audit, not external peer review.

**Provenance.** The density family originated with this audit agent and
was separately checked by the route-assessment agent, who also read and
confirmed Section 1 GREEN at the full final source hash above. Its
verification below is therefore a recheck, not a claim
of independent discovery or a cold independent audit. The Cartesian-product
construction and its complete source proof were audited independently here.
The final source differs from the examined `71fdb77f...` revision only
in its status wording; the mathematical claims and proofs are unchanged.

For the density family, the five-set edge bound is at most seven for
every possible number of vertices in the independent four-set. Every
connected branch set avoiding that four-set lies within one matching
edge. Among any three such disjoint bags at most one pair can contact,
whereas every triple of target vertices requires at least two contacts.
This establishes the minor exclusion for arbitrary bags. The edge count,
minimum degree five, and connectivity four hold throughout the stated
range `k>=16`. This does not refute either a minimum-degree-eight or a
seven-connected strengthening.

For the Cartesian product, each neighbourhood is exactly the disjoint
union `K_2 dot-union K_3 dot-union K_3`, so its independence number is
three and it contains no diamond. A universal vertex of any literal
`K_5^-` would contradict this neighbourhood description.

The connectivity argument uses actual deleted vertices. If a component
of a surviving `K_4 square K_4` layer has another surviving vertex outside
it, the latter uses neither a row nor a column met by the component.
Thus `1<=r,c<=3`, and all `r(4-c)+c(4-r)>=6` displayed boundary cells
are deleted. Five deletions therefore leave a layer connected. With at
most seven deletions overall, if all layers are good, their pairwise
matchings still contain an edge. If one layer has at least six deletions,
the other two layers are connected, remain linked, and contain at least
one of the two external neighbours of every surviving vertex of the
remaining layer. This proves eight-connectivity.

Every edge has a degree-eight common neighbour in a coordinate triangle,
which loses precisely one neighbour upon contraction. The seven displayed
bags in a single layer form a `K_7` model: the four singleton vertices of
one column contact each other and all three other whole-column bags,
which are connected and pairwise adjacent. Hence the construction does
not satisfy target exclusion. No unresolved mathematical gap was found
within the two explicitly limited refutations; neither supplies an
induction class or settles a global colouring conjecture.
