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

If `chi(J)=5`, `T` is colourful in every five-colouring of `J`. Otherwise
give `u` a colour missing from `T` and give `r` a new sixth colour. This
six-colours `G`. The two literal cliques `{u,r} union P` and
`{u,r} union Q` do not themselves supply the required rooted model.

The following static terminal is still **unproved**:

> If a five-connected, five-chromatic graph has two disjoint literal
> triangles whose union is colourful in every five-colouring, it has a
> `K5` model with every bag meeting that union.

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
