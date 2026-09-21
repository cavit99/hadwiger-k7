# The two exceptional degree-seven neighbourhoods

**Status:** working deduction and recorded route nonclosure; no separate
audit. Neither exceptional case is closed. This note belongs to the
[degree-seven construction laboratory](hc7_c21_rooted_density_construction.md#4-what-remains-towards-hc7),
not to the promoted proof inputs.

Let `G` be seven-connected, seven-chromatic, `K7`-minor-free, with every
proper minor six-colourable. Let `d(u)=7`, `S=N(u)`, and let the connected
exterior `C=G-N[u]` be full to `S`.

The exceptional complements are `K_{3,4}` and `K_{3,3} dotunion K_1`.
The [aligned-model theorem](../results/hc7_degree7_aligned_near_k7_model.md)
already handles their local models; repeating its finite classification
does not provide the missing contacts.

## 1. Exact common-pair reduction in the second exception

Write `S=P dotunion Q dotunion {r}`, where `P,Q` are anticomplete
triangles and `r` is complete to both. Put `J=G-{u,r}` and `T=P union Q`.
Then `J` is five-connected and `5<=chi(J)<=6`. A `K5` model in `J` all of
whose five bags meet `T` completes to `K7` with singleton bags `{u},{r}`.
All five bags avoid both added singletons; both singletons see each bag
at its actual `T` vertex, and `ur` is an edge.

Both chromatic branches now have one rigorous auxiliary reduction.
Choose any six-colouring of `G-u`, let `I` be the entire colour class of
`r`, and put `K=G-u-I`. Then `K` is five-chromatic and `T` is colourful
in every five-colouring of `K`: otherwise restore `I` in colour six and
give `u` a colour missing from `T`. The
[audited reduction](../results/hc7_two_triangle_colourful_reduction.md#7-application-to-the-exceptional-critical-host)
either finishes the `T`-meeting model or gives a four-connected marked
minor with the same colourful two-triangle invariant. Every cut of order
at most three is covered, including cuts meeting the marks and cuts with
all marks on one side. Vertex order strictly decreases and all marked
models lift through fixed disjoint connected preimages.

The resulting sufficient terminal is still **unproved**:

> Every four-connected, five-colourable graph with a colourful union of
> two disjoint literal triangles has a `K5` model meeting that union.

This stronger auxiliary statement is optional. The selected target is
closure of the original critical-host case, allowing the `u,r` bags and
all root assignments to change. The construction below retains the
stronger original-host conditions instead of replacing them by this
terminal statement.

Cross edges between the triangles are allowed in this auxiliary class.
Neither five-connectivity nor criticality of `G` is claimed for the
quotient. If `chi(J)=5`, one can choose `I={r}`; otherwise `I` contains
additional vertices. The reduction covers both branches without needing
the extra vertices as connectors. The original graph and all its
proper-minor colourings remain available to a direct construction.

The general colourful-set theorem cannot be substituted here:
Martinsson--Steiner [Theorem 1.3](https://arxiv.org/html/2209.00594v1#S1)
is for chromatic number four. Its primary statement was inspected.

One complete branch is elementary. If some five-set `T-{s}` is already
colourful in every five-colouring, all its roots are rainbow. Each
missing root pair is joined by its bichromatic component, since a failed
connection permits a Kempe swap omitting a colour from that five-set.
The missing-edge graph is a subgraph of `K_{3,2}`, hence has at most six
edges. Kriesell--Mohr [Theorem 7](https://arxiv.org/html/1911.09998)
packages these paths into a rooted certificate for the missing edges;
the literal root edges finish a `K5`. Thus any unresolved static instance
has no colourful five-subset of `T`.

## 2. A literal triangle can be kept singleton

This is the three-root adaptation of the existing port argument in
[the spanning-helper construction, Lemma 3](hc7_companion_helper_construction.md)
and [the companion separator proof, Lemma 1](hc7_companion_density_separators.md).
It is reused machinery, not a new construction mechanism.

**Working lemma.** Let `J` be four-connected and let `P={p1,p2,p3}` be a
literal triangle. Suppose `J` has a `K5` model with the three vertices of
`P` in three distinct bags. Then `J-P` has a partition into two nonempty
connected sets `D,E`, each adjacent to every vertex of `P`. The two sets
are adjacent.

**Proof.** Among those models, choose one maximizing the union `W=D union E`
of the other two bags. Call the three root bags `A_i`. If some `A_i` has
two distinct actual neighbours of `W`, choose distinct vertices `d,e` of
`A_i` adjacent to `D,E`, respectively. Such distinct representatives
exist whenever the union of the two contact sets has order at least two.
Replace `A_i` by a minimal tree connecting `p_i,d,e`. This tree has a
leaf in `{d,e}-{p_i}`; say it is `d`. Move that vertex into `D`.
The new `D` is connected, and the remaining tree is connected and retains
`p_i,e`. Its old tree edge to `d` supplies its `D` contact, while `e`
retains its `E` contact. The literal triangle `P` supplies every contact
between root bags. Thus `W` increases, a contradiction.

Consequently each `A_i` has exactly one actual `W` neighbour, say `v_i`.
Any unused component adjacent to `W` could be absorbed into the helper
bag that it meets, again increasing `W`. Therefore
`N_J(W) subseteq {v1,v2,v3}`. Four-connectivity implies that there is no
vertex outside `W union {v1,v2,v3}`: otherwise those at most three actual
vertices separate it from the nonempty set `W`. Each `p_i` consequently
equals `v_i`; every root bag is singleton and `W=V(J)-P`. The original
helper adjacency survives. This proves the assertion.

The existence hypothesis follows from an ordinary `K5` minor by
Costalonga--Zhou, [Theorem 4](https://arxiv.org/html/1711.01618): in a
three-connected graph a `K5` minor can retain the three literal edges of
any specified triangle. The primary theorem was inspected. In the static
five-chromatic setting, `HC5` supplies that ordinary minor. This deduction
does not keep the second triangle distributed among the two helpers.

## 3. The exact remaining helper exchange

Apply the lemma with `P`. If `Q` meets both `D,E`, the singleton `P`
bags and the two helpers give the desired `T`-meeting `K5`. Otherwise
assume `Q subseteq D`.

Take a path from `E` to `Q`, with interior in `D`, meeting `Q` for the
first time at `q`. Delete its `D` vertices from `D`, and let `D0` be the
component containing the edge on `Q-{q}`. Transfer the path and every
other component into `E`. The enlarged set is connected: each transferred
component meets the deleted path, since old `D` was connected. It remains
`P`-full. If `D0` is `P`-full, the two new helpers meet different vertices
of `Q` and finish the model.

Thus failure of this particular exchange says that for every such first-hit
path, `D0` loses at least one of the three literal `P` contacts. Five-
connectivity supplies two disjoint paths after deleting `P`; it does not
identify or synchronize their lost contacts. Keeping `P` singleton is only
an attempted construction constraint. A complete proof may absorb a
`P` vertex into a helper and use the second triangle to replace its root.
No valid uncrossing of the two triangle-based helper partitions has been
proved here, and no decreasing induction class is asserted.

## 4. Scope of the negative findings

For `G[S]=K3 dotunion K4`, all seven edges `ux` satisfy
`chi(G-{u,x})=6`: the alternative value five would force five common
neighbours, whereas `d_{G[S]}(x)` is two or three. For the second exception
this holds for all six triangle vertices; the edge `ur` is the sole
possible exception. These are restrictions, not case closures.

The common-neighbour inference uses only the selected edge `ux`. To verify
it, take a five-colouring of `G-{u,x}`. If a colour `i` misses
`N(u) intersect N(x)`, recolour the independent set of colour-`i`
neighbours of `u` with a fresh sixth colour. That set is anticomplete to
`x`. Give `u` colour `i` and `x` colour six. The resulting colouring is
proper, contradicting `chi(G)=7`. Thus all five colour classes meet the
common neighbourhood, which contains at least five vertices. This is also
the selected-edge argument in
[boundary-edge alignment, Section 2](../results/hc7_low_degree_boundary_edge_alignment.md#2-some-exterior-contacting-neighbour-is-non-double-critical).

Neither deleting clique edges nor retaining the two colour-forced exterior
paths solves the allocation problem. Clique-edge response paths may share
vertices of the repeated endpoint colour, so they do not automatically
form a bipartite scheme. The existing
[selected-response table](../barriers/hc7_degree7_single_edge_response_alignment_barrier.md)
and [reserved-connector barrier](../barriers/hc7_sole_exterior_reserved_connector_barrier.md)
remain applicable to those weaker inferences. They do not refute the
static terminal above or the full critical-host construction.

## 5. Direct prism construction: remaining gap

The original `J` retains more than the auxiliary minor. Every nonempty
`X subseteq J-T` has at least six neighbours in `J`, since `u` has no
neighbour in `X` and deleting `r` loses at most one boundary vertex.
Also `chi(J-x)>=5` for every vertex `x`. Suppose `J-x` had a
four-colouring. If `x` is outside `T`, give `x,u` colour five and
`r` colour six. If `x in P`, choose a colour absent from `P-{x}`,
recolour the neighbours of `x` having that colour with colour five,
and give `x` the chosen colour. The recoloured set is independent and avoids
`T`; again `u` can use five and `r` six. The `Q` case is symmetric.
In particular, the Four Colour Theorem excludes every apex decomposition
of `J`, including one whose apex is a root.

Three disjoint `P`--`Q` paths form a triangular prism with its two
triangles literal. If deleting one whole vertical path leaves a `K4`
model rooted at the other four endpoints, that path is the fifth bag;
the triangle edges give its four contacts. The first unsupported step
would be applying connectivity of `J` to this path-deleted graph: its
separator can have arbitrarily many neighbours along the deleted path.
Norin--Thomas [Lemma 4.2](https://arxiv.org/html/1402.1999v3) also leaves
a three-legged bridge to the prism; a cross-free conclusion alone does
not imply planarity. Deleting its centre and three feet does not preserve
ownership of paths through the surviving legs. No monotone rerouting or
actual root-free set with at most five neighbours has been obtained.
These are route nonclosures, not counterexamples to the critical-host
case. Its full colouring hypotheses remain available.

## 6. Exact extremal representation and the unresolved exchange

The [extremal prism theorem](../results/hc7_two_triangle_extremal_prism.md),
with a [separate internal audit](../results/hc7_two_triangle_extremal_prism_audit.md),
strengthens Sections 2--3. Maximising the connected helper `E` forces
`J-E` to be exactly an induced prism subdivision with literal end
triangles `P,Q` and three nontrivial paths `R_i=p_i...q_i`. Its proof
uses actual block-cut-tree boundaries and needs only four-connectivity
and an ordinary `K5` minor. No part of the graph is discarded.

In the original graph, roots have at least two `E`-neighbours, path
interiors at least four, and `F=G[E union {r}]` has chromatic number
at least four. Every non-cut vertex of `E` has its prism neighbours
within one end triangle or a segment of at most two edges of one path,
and has degree at least three inside `E`. The theorem gives the explicit
bags and cardinality comparison proving these restrictions.

The open step concerns connected sets in `E`, not another neighbourhood
census. A set meeting two relevant path portions can finish the model
when its complement remains connected and keeps the required root
contacts. These complementary conditions have not been established
through neutral vertices or two-vertex separations of `E`. In particular,
the attempted inference that three-connectivity of `E` suffices omitted
vertices with no path-interior contact, including vertices with no prism
contact at all. Its first unsupported step was assigning every edge
leaving one path's contact class an endpoint contacting another path.
The valid single-vertex exchange and the complete original-host target
remain unaffected. A repair must control the whole transferred set and
its complement simultaneously.

Allowing triangle roots to move still does not justify contracting both
pieces before that repair. The
[intact-helper counterexample](../barriers/hc7_prism_intact_helper_barrier.md)
has balanced root ownership and contacts from each piece to all three
paths, but permits no model even with all triangle roots movable.
It refutes only the weaker four-connected quotient claim. The actual
pieces' contact multiplicity and ability to split must remain available.

One comparison under deletion is valid. For `x in E`, let `E_x` be
any extremal helper supplied by the theorem in `J-x`. Then
`|E_x|<=|E|-1`, with equality if `E-x` is connected. Indeed, `J-x` is
four-connected and still has an ordinary `K5` minor by Section 5.
If `|E_x|>=|E|`, the vertex `x` cannot contact `E_x`, since absorbing it
would enlarge the original helper. Thus its at least six neighbours
all lie on the new prism. Two neighbours on one vertical path with
a nonempty interval between them allow that interval to move into
`E_x`, replacing it on the path by `x`; every moved vertex has an
`E_x` neighbour by four-connectivity. This again enlarges the helper.
Otherwise `x` has exactly two consecutive neighbours `y_i,z_i` on
each of the three paths, in order from `p_i`. A forbidden model has
the three `p_i`--`y_i` prefixes as bags, a fourth bag consisting of
`x` and the `z_1`--`q_1` suffix, and a fifth `E_x union {q_2}`.
The prefixes contact each other through `P`; the fourth contacts them
through `x`; the fifth through the original `P` roots; and the final
contact is `q_1q_2`. Each bag meets a distinct triangle root.
This proves the inequality. When `E-x` is connected it remains
`P`-full, since every root has at least two `E` neighbours, proving
equality by maximality in `J-x`.

This is a working comparison, not an induction: `J-x` need not retain
the original critical-host hypotheses, and equality does not identify
the two extremal choices. No recursive conclusion is imported from it.

One whole end-block exchange can retain the root contacts. Let `W=B-z`
be the interior of an end-block of `E`, attached at `z`, and suppose
all its prism contacts lie on `R_i`. It has at least five such contacts,
by the six-neighbour boundary condition. Let `s,t` be the extreme ones
and `K` the open interval between them. The set `(E-W) union K` is
connected: otherwise `K` has no neighbour in `E-W`, and `W union K`
has boundary contained in `{z,s,t}`, impossible. If `W` owns all
helper contacts of `p_i`, then `s=p_i` and the first internal path
vertex, now in `K`, restores that contact. Other P contacts survive.
The complementary helper replaces this interval by the connected `W`
and remains connected and P-full. Thus maximality proves only
`|K|<=|W|`. Strict gain has not been established, so this valid move
does not eliminate the end-block. Adjoining the interval to `W` is
also not a small-separator argument: its other neighbours in `E-W`
remain part of the actual boundary.

Alternatively, for each `i`, put `H_i=J-V(R_i)`. The cycle formed by
the other two paths fixes the four-root order. A rooted `K4` in `H_i`
would finish with `R_i`, so Fabila-Monroy--Wood
[Lemmas 2 and 7](https://arxiv.org/html/1102.3760v1)
give a separate ordered web completion of each `H_i`; their primary
statements were inspected. For a web cell behind three gates in `H_i`,
the theorem does not bound its additional contacts on `R_i`. The three completions
have not been shown to have compatible cells or gates. Thus neither
attempt gives a root-free set with at most five neighbours in `J`.

## 7. Proper-minor colourings retained for that construction

The following are working deductions, not additional case closures.
They must be used together with the exact representation and actual
attachments, rather than as an independent response table.

For any induced `P`--`Q` path `R=v_0...v_k` meeting the triangles only
at its ends, take a six-colouring of `G/R`. Write the distinct colours
of `u,r,R` as `alpha,beta,gamma`, and put `H=J-V(R)`. For every colour
`t` outside these three, a component of `H[gamma,t]` contacts both
parities of `R`. Otherwise alternate `gamma,t` on `R` and flip each
whole two-colour component so that its contact side is opposite the
parity it meets. No `gamma` vertex of `H` contacts `R`, by the quotient
colouring. Thus all contacts are repaired; other colours, including
`alpha,beta`, cause no conflict. This six-colours the original graph.
The four surviving triangle roots may change colour in these flips.

Each forced component supplies an even path outside `R` joining vertices
at odd distance on `R`. If `k` is even, a fourth such component exists
for `t=alpha`: the isolated vertex `u` in the off-path two-colour graph
contacts only the two same-parity ends, so cannot be the obstruction.
Different bridges may share `gamma` vertices and need not cross. Replacing
an odd path interval by an even bridge need not leave an induced path;
shortening chords can change parity. Thus this operation does not prove
the existence of an induced even path or a decreasing rerouting.

There is also a direct full-colour-class constraint on the extremal
remainder. In any four-colouring of `F=E+r`, let `I` be a colour class
not containing `r`, and let `S=J-E`. Then `chi(G[S union I])=4`.
It is at most four because `S` is three-colourable and `I` is independent.
If it were at most three, recolour `S union I` using its old `I` colour
and two fresh colours. Keep the other three `F` colours, and give `u`
one of those three different from `r`. This six-colours `G`: no vertex
of `T` retains one of those three colours, and `u` has no neighbour in
`E`. The conclusion is conditional on a four-colouring of `F`; the
case `chi(F)>=5` is not removed. Neither this constraint nor separate
colourful-set models supplies simultaneous branch-set ownership.
