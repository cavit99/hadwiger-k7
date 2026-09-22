# Separate reconstruction audit: the split-clique three-contact branch

**Status:** separate internal mathematical audit, 22 September 2026.
This is an internal agent audit, not external peer review.

**Verdict: GREEN** for the exact statement below. No unresolved gap was
found. The argument closes one unbounded branch of the degree-seven
split-clique neighbourhood case; it does not close the four-contact
branch, the whole degree-seven case or `HC_7`.

## Exact revisions and input

- [Audited proof](hc7_split_clique_three_contact.md),
  whole-file SHA-256:
  `a72ad9a6e69497a4d064d826738f04ae0c19f49141fe124aaafd98d950f2f110`.
- [Universal bipartite contractibility theorem](bipartite_contractibility_via_matroid_reduction.md),
  whole-file SHA-256:
  `3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272`.
- Its [first internal audit](bipartite_contractibility_via_matroid_reduction_audit.md),
  whole-file SHA-256:
  `1c8ed74e98829690dc4c1fd6d44631454d330443dd33faea4435d35beb5cca06`.
- Its [second internal audit](bipartite_contractibility_via_matroid_reduction_second_audit.md),
  whole-file SHA-256:
  `83df07a306bef1a71b50bf5f36020a48b7240187c40d503819eb10baf5348297`.

The theorem's actual statement, scheme definition, root-preserving
reduction and both audits were inspected. Both audits identify the
current theorem source hash. The input supplies a fully rooted minor
for every scheme of every finite simple bipartite target, with no path
length, order or multiplicity restriction. It allows both root shores
to expand. Its external premise is Edmonds' finite matroid union theorem;
the present audit applies the written repository theorem, rather than
introducing another external graph-minor premise or re-auditing that
matroid theorem.

The final proof revision changes only the audited draft's status and
relative links for promotion. Its mathematical text is unchanged; the
final whole-file hash above was checked after those editorial changes.

## Exact audited statement

Let `G` be finite and simple, not six-colourable, with every proper
minor six-colourable. Suppose `N_G(u)=P dotunion D`, where `P` is a
triangle, `D` is a four-clique and there are no edges between them.
For any `p in P`, take any proper six-colouring of `G/up`, naming the
contracted vertex's colour six. Let `I` consist of the other vertices
of colour six, put `K=G-({u,p} union I)`, and let `X` be the component
of `K-D` containing `P-{p}`. If `X` has no neighbour at some vertex
of `D`, then `G` contains a `K7` minor.

This audit reconstructed the colouring implications and the nine-path
scheme from these hypotheses. In particular, it did not assume the
previously recorded five-bag extraction or a separate linkage from the
omitted `D` vertex.

## Original-host colourings and the missing boundary vertex

The contraction `G/up` is a proper minor, so the initial colouring exists.
Every vertex adjacent to either `u` or `p` is adjacent to its contracted
image. Therefore `I` lies outside `N_G[u]`, is anticomplete to `p`, and
is independent. Restricting the colouring gives a proper five-colouring
of `K`. Conversely, every proper five-colouring of `K` extends to
`G-u` by giving `p` and `I` colour six. This is a proper colouring of
the original graph, because `I union {p}` is independent.

Write `A=P-{p}`. If a five-colouring of `K` omitted a colour from
`A union D`, the preceding extension would permit that colour at `u`:
its remaining neighbour `p` has colour six, and `u` misses `I`.
Thus `A union D` uses all five colours in every such colouring.

In a colouring with the four `D` colours named one to four, the edge
`A` consequently uses five and exactly one colour `c` of `D`. Every
neighbour of `X` outside `X` in `K` belongs to `D`. If `X` missed two
vertices of `D`, one has colour `j!=c`. Swapping colours `j` and five
on all of `X` is proper, since neither colour occurs on its external
neighbourhood. It removes five from `A`, a contradiction. Under the
audited hypothesis, `X` therefore misses exactly one vertex `d` of
`D`, and it contacts all vertices of `Q=D-{d}`.

Name the colours of `Q` one, two, three and that of `d` four. If `A`
used five and one of one, two, three, swapping four and five throughout
`X` would again remove five from `A` without creating an improper edge.
Thus `A` has colours four and five in every five-colouring with these
fixed `D` colours. The identity of the vertex having colour four need
not stay fixed across all colourings; the argument only needs the pair
of colours. In the chosen original colouring call those vertices `a`
and `b`, respectively.

## The six paths inside the deleted colour-class graph

For `i in {1,2,3}`, consider the subgraph on colours four and `i` in
`K[X union Q]`. If the component containing `a` omitted `q_i`, then
it would contain no vertex of `Q`: `q_i` is its only possible `Q`
vertex. Hence this component is a subset of `X`.

Swapping its two colours extends properly to all of `K`. An external
neighbour of either relevant colour in `X union Q` would belong to
the same two-colour component; outside `X union Q`, no vertex is
adjacent to `X`. In particular, the other vertex `d` of colour four
has no neighbour in `X`. The swap fixes `D` and `b`, and changes
`a` from four to `i`, contradicting the forced colour pair on `A`.
Thus `a` and `q_i` are connected in that two-colour subgraph.

The same reasoning on colours five and `i` gives a `b`--`q_i` path.
Choosing a simple path in each component gives six paths in
`K[X union Q]`. Each uses only its endpoint colours, and hence contains
no other vertex of `A union Q` internally. No vertex of `I`, `p`, `u`
or `d` belongs to this host.

## The three paths through colour six

Lift the same original quotient colouring to `G-u` with `p` and `I`
coloured six. No recolouring used to prove the preceding implications
is retained. This point ensures that all nine paths below use a common
proper colouring of one original graph.

For each `i in {1,2,3}`, the only neighbour of `u` with colour `i`
is `q_i`, and the only neighbour of `u` with colour six is `p`.
If their components in the subgraph of `G-u` on colours six and `i`
were distinct, swapping the component containing `p` would remove
colour six from `N_G(u)`. The only neighbour that could change from
`i` to six, namely `q_i`, is outside that component. Colouring `u`
six would then properly colour all of `G`, a contradiction.

There is therefore a simple `p`--`q_i` path on colours six and `i`.
It avoids `a`, `b` and `d`, whose colours are four, five and four,
respectively. It also avoids all other prescribed roots by colour.
It may use vertices of `I` and may intersect other chosen paths; the
scheme condition, checked next, handles precisely those intersections.

## Full collection axiom and all seven bags

All nine paths lie in `G-{u,d}`. Their prescribed roots are the six
distinct vertices of `P union Q`, coloured respectively six, four,
five, one, two and three. Every path uses only its two endpoint colours
and has no other prescribed root internally.

Consider any nonempty collection of these paths with a common vertex
`v`. Among the six prescribed roots exactly one has the colour of
`v`. Every path in the collection has that root as one of its two
endpoints, because every chosen path uses only its endpoint colours.
Their target edges therefore have a common endpoint. This verifies
the full collection axiom, including collections of three or more
paths; pairwise compatibility alone is not being substituted for it.

The repeated colour at `a` and `d` creates no ambiguity: `d` is not
a prescribed root and is absent from every chosen path. Other host
vertices with that colour also identify the unique prescribed root
`a` in the same argument. The nine paths consequently form a scheme
for the simple bipartite target `K3,3` with shores `P,Q`.

Apply the inspected theorem in the finite host `G-{u,d}`. It gives
six pairwise disjoint nonempty connected bags, one containing each
prescribed root, with all nine contacts between the two shores. The
three actual edges in the triangle `P` supply the three contacts
between the `P` bags; the three actual edges in the triangle `Q`
supply the three contacts between the `Q` bags. Root retention is
essential here and is part of the theorem's conclusion. These are
all fifteen contacts of a `K6` model.

Adjoin the singleton seventh bag `{u}`. It is disjoint from the six
bags, and its edge to the retained root in each bag supplies six
further contacts. Thus all twenty-one pairs of the seven connected
bags are adjacent in the original graph. This is an explicit `K7`
minor model, not merely a statement about a coloured quotient.

## Reduction discipline and unresolved scope

There is no induction in the new branch argument. The initial
contraction supplies a colouring only; neither `K` nor another minor
is asserted to inherit criticality. The sole inductive input is the
audited bipartite theorem, whose model lifts through disjoint connected
preimages and retains all six original roots. Its host excludes `u,d`,
so neither vertex can be absorbed during that lift. The actual triangle
edges are used after the lift in the original host.

No extra connectivity, maximality, path disjointness, degree bound on
other vertices, or finite-computation premise is required. This is an
unbounded branch closure. It proves that a hypothetical `K7`-minor-free
host with the stated criticality has `X` adjacent to every vertex of
`D`, for every chosen `p` and every allowed quotient colouring. It
does not produce two compatible `D`-full bags meeting `P`, nor exclude
that remaining four-contact branch. The global `HC_7` objective and
the entire degree-seven checkpoint remain unresolved by this proof.
