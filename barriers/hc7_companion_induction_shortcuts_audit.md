# Audit of companion-induction counterexamples

**Verdict:** GREEN at source SHA-256
`99661d13e82d84c940e3a7861bb7cfd048502399c1484c62c487da5a1ca0fec3`
for [the counterexample source](hc7_companion_induction_shortcuts.md).
This is an internal mathematical audit, not external peer review.

The 7 September 2026 addition independently checks new Sections 3–4.
Removing them and restoring the original title and "Neither construction"
wording exactly recovers Git `623110a`, at whole-source
SHA-256 `f3761a2a22c7c13f56b39ce0e28ee226d6871be566b13ff176d27badf2a2ce81`.
This byte equality was checked directly against Git. The original
Sections 1–2 audit and its authorship provenance below are preserved.

**Provenance.** The density family originated with this audit agent and
was separately checked by the route-assessment agent, who also read and
confirmed Section 1 GREEN at the preceding source hash `f3761a2a...`. Its
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

## Section 3: full boundary apex

**Verdict: GREEN**, independently checked by the route-assessment agent.
Any nonroot open side contains a triangle vertex adjacent to all five
roots, which must consequently lie in the separator. This proves the
stated internal five-connectivity directly. Completing edges between
roots cannot change this rooted separation condition. The side count is
`3+15=18`, exceeding `4*3+4=16`.

The apex graph lies in `K_4 join I_5`. Any six disjoint connected bags in
that supergraph include at least two avoiding the four-clique; they must
be distinct independent-set singletons and cannot contact. Thus arbitrary
`K_6` models, including models preserving the five roots, are excluded.
Contracting an edge between endpoints of different missing edges in
`K_7^=` gives `K_6`, so target exclusion follows. The spanning `K_{4,5}`
gives connectivity at least four, and deleting its four-vertex shore
separates the five roots, proving equality. Therefore the example retains
the specified one-apex exclusion while losing the required ambient
five-connectivity. No global five-connected density bound is refuted.
No gap was found in this exact additional refutation; preserving both
original sides' sufficient connectivity and ownership remains unproved.

## Section 4: complement of the eight-cycle

**Verdict: GREEN**, independently checked by the route-assessment agent.
A cut of at most four leaves at least four vertices; a disconnection would
require `K_{2,2}` in `C_8`, since all cross pairs are cycle edges and its
maximum degree is two. No such cycle exists. The degree-five upper bound
therefore gives connectivity exactly five. The six displayed bags are
connected and pairwise adjacent; the two odd pairs contact through `1–3`.
Every graph edge has three common neighbours at cycle distance two and
two at distance three or four. Seven disjoint nonempty bags use either
seven vertices (at most fifteen edges) or eight with exactly one edge bag
(at most seventeen quotient edges). These exhaust arbitrary models and
exclude the nineteen-edge target. The explicit `K_6` is a proper minor.
The example has insufficient density and degree for either global target;
only the asserted five-connected proper-minor augmentation is refuted.
