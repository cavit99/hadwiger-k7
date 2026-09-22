# The two exceptional degree-seven neighbourhoods

**Status:** preserved working deductions and earlier route nonclosures;
this note has no separate audit. The second exceptional case is now closed
by the [audited two-triangle theorem](../results/hc7_two_triangle_case_closure.md).
The `K3 dotunion K4` case remains open. This note belongs to the
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
`|K|<|W|`. Indeed equality would make the new helper maximum, so its
complement would again be an induced prism. But every vertex of `W`
is non-cut in `E`, has degree at least three in `E`, and has at most
one neighbour outside `W`. Thus `E[W]` contains a cycle, impossible
inside the three root-free path interiors of the new prism. The move
therefore loses helper vertices; it does not eliminate the end-block.
Adjoining the interval to `W` is
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

## 8. What the contraction attack establishes

**Written deductions; [separate internal audit](hc7_degree7_exceptional_contraction_audit.md).**
All statements below retain the original critical graph and the extremal
representation of Section 6. They do not establish a recursive reduction
or close the two-triangle case.

### Two owners force a triangle

If a triangle root `p` has exactly two `E`-neighbours `x,y`, and `v` is
its first vertical-path neighbour, then `{v,x,y}` induces a triangle.
Indeed `d_G(p)=7`. Any nonedge among these three vertices, together with
`u`, gives an independent triple in `N_G(p)`. Contract its star with
centre `p` and six-colour the proper minor. Give the triple the contracted
colour on expansion. The other four neighbours use at most four further
colours, leaving a colour for `p`, a contradiction. This argument also
applies to roots in `Q`, and needs no assumption that `x,y` are non-cut.

### A three-vertex contraction preserves the prism theorem's premises

Let `B={a,b,c}` induce `a-b-c` in `E`, put `H=J/B`, and call the
contracted vertex `z`. Then `H` is four-connected and `chi(H)>=5`.
A cut of size at most three avoiding `z` lifts unchanged to `J`.
A cut containing `z` lifts to `B` and at most two other vertices.
Every resulting component must meet `T`, by the six-neighbour condition
for root-free sets. Yet deleting any two vertices from the prism leaves
all surviving roots connected: each triangle's surviving roots are
connected, and at least one vertical path remains intact. This excludes
the cut. A four-colouring of `H` would expand with `a,c` in the colour
of `z`, `b,u` in a fresh fifth colour and `r` in a sixth, again impossible.

A `T`-meeting `K5` in `H` lifts through the fixed preimage `B`, so none
exists. The prism theorem therefore applies. Write `m=|E|` and let `M`
be any maximum helper in `H`, with `P` singleton and `Q` in its complement.
Then

    m-2 <= |M| <= m.

The old `E/B` proves the lower bound. If `z in M`, expanding it proves
`|M|=m-2`. Otherwise expansion in the complementary helper proves the
upper bound. In this latter case `z` is an internal vertex on a new
vertical path, between vertices `s,t`. Choose a shortest subpath `L` of
`B` joining a neighbour of `s` to a neighbour of `t`. All neighbours of
`B` outside `B` lie in `M union {s,t}`. Each unused vertex of `B` has
a neighbour in `M`, since its degree in `J` is at least six. Absorbing
these unused vertices into `M`, and replacing `s-z-t` by `s-L-t`, gives
an admissible original partition. Hence

    |M| + 3 - |L| <= m.

When `|M|=m`, this forces `L=B`, so the whole path becomes consecutive
vertices of another induced prism. It is an exchange between maxima,
not a decreasing operation. When one root is adjacent to all of `B`,
every maximum `M` instead has size exactly `m-2`: if `z` lies outside
`M`, that root is `s` or `t` and there is a one-vertex choice of `L`.
Thus even the three-owner path can remain inside the contracted helper.
The quotient has fewer vertices but is not known to be in the original
critical-host class; induction on its order would be unsupported.

### A colouring lift for a path owning a root

Let `X` induce a nonempty path in `E`, let `p=p_i`, and let `v` be the
first internal vertex of `R_i`. Suppose `N_E(p) subseteq X` and all
vertices of `N_X(v)` lie in one bipartition class of `X`. Then

    chi(G/(X union {p})) = 6.

The quotient is a proper minor. Suppose it
has a five-colouring, with fibre colour `gamma` and `u`-colour `delta`.
These colours differ. Recolour every outside `delta`-vertex except
`u` and, when applicable, `v` with a fresh colour six. Give `p` colour
six and alternate `gamma,delta` on `X`, assigning `gamma` to every
`X`-neighbour of `v`. No outside neighbour of `X` has colour `gamma`;
the remaining outside `delta`-vertices cause no conflict. The outside
neighbours of `p` are exactly `u,r,P-{p},v`. The vertices `r,P-{p}`
avoid `delta`, since they form a clique with `u`; neither `u` nor `v`
was recoloured. This gives a proper six-colouring of `G`, impossible.
The proper-minor upper bound now proves equality. This proof does not
assume that `E-X` is connected. The related lower bound
`chi(G-(X union {p}))>=5` supplies no additional information: that
deletion already contains the literal `K5` on `{u,r} union Q`.

### Mandatory Kempe moves within one colouring

In every six-colouring of `G-u`, exactly one pair of vertices of `N(u)`
has the same colour; write it as `a in P`, `b in Q`, of colour `c`.
There is a Kempe interchange moving the repeated pair within `P`,
and another moving it within `Q`. These assertions concern the same
colouring, not the nine separately available star-contraction colourings.

For a move within `P`, take `x in P-{a}` of colour `t`. Its `c,t`
component contains `a`, by the edge `ax`. If it avoids `b`, swapping
the component changes the repeated pair to `x,b`. Suppose both choices
of `x` instead have components containing `b`. They give paths from
`b` to the two roots of `P-{a}`. The four cross-pairs between `P-{a}`
and `Q-{b}` are also connected in their two colours: otherwise a swap
would reduce the number of colours on `N(u)` to five and extend to `u`.
These six paths form a `K_{2,3}` scheme with shores `P-{a}` and `Q`.
The omitted root `a` may occur internally on the two paths incident
with `b`; this is permitted. At every common vertex, its colour is
the colour of a common target endpoint. No prescribed root is internal
to a nonincident path, and the whole `r`-colour class is avoided.
The [bipartite contractibility theorem](../results/bipartite_contractibility_via_matroid_reduction.md)
therefore supplies five disjoint rooted bags in `J`. The literal edges
within the two shores complete a `K5`, a contradiction. The move within
`Q` follows symmetrically.

These moves are reversible. Even the boundary pairs in one Kempe orbit
could occupy only a two-by-two rectangle of the three-by-three array:
that satisfies the forced-move rule and may include only one matched
prism pair. Thus the rule neither reaches all nine pairs nor proves
that a reserved path and the five-bag model can be chosen disjointly.

### Where the construction still fails

The attempted construction already leaves open a removable induced path
owning all three helper contacts of `p_i`:
its vertices `a,b,c` all meet `p_i`, with `a` also meeting `p_j`,
`b` having no other prism contact, and `c` meeting only the first
internal vertex of `R_i`. This describes a surviving configuration,
not a constructed critical graph or a counterexample. The two-owner
argument does not exclude it, and the contraction comparison gives
no improvement. Switching the fixed triangle does not repair it:
`(E-X) union {p_i}` is disconnected precisely because `X` owns `p_i`.

The colouring lift handles this path but does not finish the minor.
Even a suitably aligned model in its six-chromatic quotient can need
the same first rail vertex both to restore `p_i`'s contact and to route
the other part of `X` towards `Q`. Those uses cannot be allocated
independently. Rerouting to retain one owner may merely transfer the
lost contact to another root; no decreasing potential or simultaneous
allocation has been proved. More concretely, in this three-vertex
pattern put `Y=E-X`. An `a`--`c` path `Z` with interior in `Y` would
finish if `Y-int(Z)` were connected, Q-full and adjacent to `b`:
use the three singleton Q bags together with

    (Y-int(Z)) union {b,p_i},
    ((P union I_1 union I_2 union I_3)-{p_i}) union V(Z).

The first is connected through `b`, the second through `a`'s cap
contact and `c`'s rail contact; both are Q-full and the edge `ab`
joins them. Their roots are distinct. Existence of this path, with
all complementary contacts retained, remains unproved. This pattern
has not been shown to cover every failure of the global exchange.
The outstanding construction must split
the actual connected remainder while preserving the colouring data,
or repair the original colouring. Contracting that remainder first,
or repeating the separate Kempe responses, leaves this obligation open.

## 9. A construction for some three-owner patterns

**Working proof; not separately audited.** This section concerns only the
particular surviving pattern in Section 8, not every extremal remainder.
Write `p=p_i`, `s=p_j`, `t=p_k`, and let `v` be the first internal vertex
of `R_i`. Assume `E={a,b,c} dotunion Y`, with `Y` connected,
`N_E(p)={a,b,c}`, and

    E[{a,b,c}] = a-b-c,
    N_S(a)={p,s},  N_S(b)={p},  N_S(c)={p,v},

where `S=J-E`. Thus `a-b-c-v` is induced and
`N_G(p)={u,r,s,t,a,b,c,v}`. All arguments retain the original critical
graph; no quotient is asserted to remain critical.

### Five-root construction

Five differently coloured roots containing a literal triangle give a
rooted `K5` if every missing pair is bichromatically connected.
Use the seven demands of `K5` minus that triangle, choosing literal edges
for present demands. Their paths form a scheme: any common vertex has
the colour of a common target endpoint, and the five distinct root colours
exclude other roots internally. Kündgen--Pelsmajer--Ramamurthi,
[Theorem 6.2](https://arxiv.org/pdf/1207.6141v1), proves fully rooted
contractibility of this demand graph, `K_{1,1,3}`. The literal triangle
edges finish the model. The primary definition and proof were inspected.

In particular, contract the star joining `p` to any independent triple
`I subseteq N_G(p)`, and six-colour the resulting proper minor. On
expansion, keep `I` monochromatic and omit `p`. The other five neighbours
must have all five remaining colours, or the colouring extends to `p`.
Every missing pair of those five neighbours is bichromatically connected:
otherwise a Kempe interchange again frees a colour for `p`. The core
constructed above avoids the entire colour class of `I`.

### An absent independent pair completes the minor

Suppose `r` misses both ends `x,y` of a nonedge of the induced path
`a-b-c-v`. Use `I={r,x,y}`. The other five neighbours are the literal
triangle `{u,s,t}` and the two remaining path vertices. The five-root
construction gives a core avoiding `p,r,x,y`.

Apply the singleton-triangle normalisation of Section 2 in
`G-{p,r,x}`, retaining those last two roots in the helpers. This graph
is four-connected. The normalisation proof still works with these
helper roots prescribed: it only adds vertices to their bags.
Both resulting helpers meet `Q`, since the only neighbours of `u`
outside the retained triangle in this graph are the vertices of `Q`.
Adjoin singleton bags `{p},{r}`. Both see every triangle root and both
helpers at their `Q` vertices; `pr` supplies the last contact. All seven
bags are disjoint, giving a `K7` minor.

Consequently, the surviving set of `r`-neighbours on `a-b-c-v` must contain
one of `{a,b}`, `{a,v}`, `{c,v}`. This is a restriction on this pattern,
not an exhaustive reduction of the two-triangle case.

### Two chromatic branches

Put `H=G-{p,r}`. Its chromatic number is five or six. In every
five-colouring of `H`, the common neighbourhood `N(p) intersect N(r)`
uses all five colours, by the selected-edge recolouring in Section 4.
If the `r`-neighbours on the path are exactly one of the three pairs
above, that common neighbourhood has exactly five vertices and contains
the triangle `{u,s,t}`. Its roots are rainbow, and a missing bichromatic
connection would contradict colourfulness by a Kempe interchange.
The five-root construction and singleton bags `{p},{r}` finish `K7`.
If `r` has three or four path neighbours, colourfulness alone does not
make the common neighbourhood rainbow; these five-chromatic instances
remain open.

If `chi(H)=6`, then `chi(J-p)=6`. Otherwise five-colour `J-p=H-u`.
The five neighbours `{s,t} union Q` of `u` in `H` must be rainbow and
have all missing bichromatic connections, since any missing colour
would extend the colouring to `H`. The bipartite contractibility theorem
packages the six demands between `{s,t}` and `Q`; their literal shore
edges give a `K5`. Singleton bags `{u},{r}` complete `K7`, a
contradiction. The proper-minor upper bound proves the claimed equality.
Hence this branch supplies an ordinary `K6` minor in `J-p`, by `HC6`.
Its bags are not yet allocated among the six triangle roots.

The next construction must handle the extra-contact five-chromatic
instances and turn the six-chromatic branch into a suitably rooted model.
There is no induction here and no closure of the three-owner pattern.
In particular, `K6` cannot simply replace `K5` in the triangle-retaining
theorem: Costalonga--Zhou explicitly exclude that unrestricted extension
after their Theorem 4. Nor does a small separator in a contracted model
lift to a separator of the same order in the original graph.

## 10. A six-clique model using two remainder bags

**Working proof; not separately audited.** Let a graph consist of an
induced triangular-prism subdivision `S`, with end triangles `P,Q`, and
a connected set `E` outside `S`. Assume that every vertex of `S` has an
`E`-neighbour. If the graph has a `K6` model with exactly two bags
meeting `E`, it has a `K5` model whose five bags meet `T=P union Q`.
The statement has no bound on the subdivision or the remainder.

The other four bags form a `K4` model entirely in `S`. They cover all
of `S`: deleting any vertex of a prism subdivision destroys all `K4`
minors. To see the latter assertion, prune the broken path's hanging
ends and suppress the two corresponding triangle vertices of degree
two. After removing parallel edges, the remainder is a cycle or its
subdivision. The same reduction works when the deleted vertex is a
triangle vertex. None of these operations hides a `K4` model.

The other two bags therefore lie entirely in `E`. Absorb each component
of their complement in `E` into a bag it meets; such a bag exists by
connectedness of `E`. This gives a connected partition `E=X dotunion Y`
retaining the `K6` model. Contract `X,Y` to adjacent vertices `x,y`.
Every prism vertex still sees at least one of them.

Each of the four prism bags meets `T`, since a connected root-free
subgraph of `S` is an interval with at most two external neighbours in
`S`. Along a vertical path, only its endpoint bags can occur: any other
bag there would have no route within its own vertices to `T`. Contract
the interiors of their prefix and suffix to the corresponding roots;
if both endpoints are in one bag, keep their two roots distinct and
contract the path to an edge. This retains the six distinct roots and
the `K6` model, giving the literal prism plus `x,y`. All contraction
preimages are fixed, connected and disjoint, so a rooted model in this
eight-vertex graph lifts to the original graph.

The four prism bags partition its six roots. There are three types, up
to permuting indices and interchanging the caps:

- one whole cap and the three opposite roots singleton;
- two vertical pairs and the remaining two roots singleton;
- one vertical pair, the other two roots of one cap paired, and the
  opposite two roots singleton.

Indeed, a bag of size three leaves a singleton triangle and is the
opposite cap. Otherwise there are two edge bags and two adjacent
singletons. Two cap edges fail one required contact; the remaining
possibilities are the last two types above.

Here is a common construction. Define

    A={i: yp_i and xq_i are edges},
    B={i: xp_i and yq_i are edges}.

Choose distinct `i in A`, `j in B`. Partition `Q` into `U,V`, placing
`q_i` in `U` and `q_j` in `V`. Force `q_k` into `U` when `p_k` misses
`x`, and into `V` when `p_k` misses `y`. These requirements do not
conflict, because each `p_k` sees `x` or `y`; neither contradicts the
two chosen placements. Assign the other vertices arbitrarily.
The sets `{x} union U` and `{y} union V` are connected through their
chosen `Q` neighbours, each is `P`-full, and `xy` joins them. With
singleton `P`, these are the required five bags.

Such distinct indices exist in all three partition types. In the first,
every `Q` root sees both apices and both apices meet `P`. Their
`P`-neighbour sets cover all three roots, so they have distinct
representatives. In the second, the singleton vertical index belongs
to both `A,B`. Each other vertical pair meets both apices and both of
its roots see an apex; hence it supplies an index in `A` or `B`.
In the third, the two singleton `Q` roots see both apices, and each
apex meets their paired `P` roots. Since both those roots see an apex,
the two apices have distinct representatives among them. This proves
the construction and its lift.

Applied to Section 9's six-chromatic branch, any remaining `K6` model
must therefore have at least three bags meeting `E`. This is a complete
conditional construction, not a proof that such a model can be rerouted
to use only two remainder bags. Moving a fan endpoint from a third bag
can still lose that bag's sole contact with another rooted bag.

## 11. Three helpers when the first triangle is singleton

**Working proof; not separately audited.** Let `J` be five-connected,
let `P,Q` be disjoint literal triangles, and suppose `J` has a `K6`
model with the three `P` vertices as singleton bags. Then `J` has a
`K5` model all of whose bags meet `P union Q`.

Absorb every unused component of `J-P` into one of the three helpers
it meets, so the helpers partition `J-P`. If two helpers meet `Q`,
retain them together with singleton `P`. Otherwise all of `Q` lies
in one helper `A`; call the other two `B,C`.

Set `R=J-P`, which is two-connected, and contract `B,C` to `b,c`.
There are two vertex-disjoint paths from `{b,c}` to `Q`, with distinct
starts and distinct ends. Indeed, a separating vertex outside `{b,c}`
would lift unchanged to a cutvertex of `R`: the contracted preimages
remain connected. Deleting `b` does not separate `c` from `Q`, since
`A` is connected, contains `Q`, and meets `C`; the case of `c` is
symmetric. Menger's theorem therefore supplies the paths.

Lift each path and add its vertices outside the starting bag to `B`
or `C`, respectively. The two enlargements remain disjoint, connected
and `P`-full; they meet distinct vertices of `Q` and retain their old
mutual edge. Singleton `P` completes the required model. There is no
recursive invocation and no lost prescribed root.

Keeping only `A union Q` when finding these paths would be an invalid
restriction: it can have a cutvertex bypassed by other vertices of
`R`, including the prism paths. Using the entire original `R` closes
that apparent separator case.

This does not normalise an arbitrary triangle-rooted `K6` model to
singleton `P`. A nonroot leaf of a root bag can carry its only contacts
to two helpers, so moving that leaf into one helper need not preserve
the other contact. The two-helper normalisation of Section 2 does not
establish this stronger three-helper premise.
