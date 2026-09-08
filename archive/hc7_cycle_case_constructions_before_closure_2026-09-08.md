# Cycle-case constructions before the complete closure

**Frozen historical record.** Extracted from Section 7.5 of Git `dbe474c`,
whole-frontier SHA-256
`826239ff6eb59b1c59c933bc69896f3f0c171a8455df4cb0674bb0fa0172ae05`.
Only relative navigation links are adjusted below. Statements that the
cycle case remains open describe that revision, not current status.
The [research ledger](../RESEARCH_LEDGER.md) is authoritative.

In the five-cycle-and-triangle case, the
[reserved-neighbour construction](../active/hc7_degree8_cycle_triangle_construction.md)
uses a proper-minor colouring and the bipartite theorem to obtain a rooted
`K_5` on five neighbours. Choose the omitted triangle vertex away from the
possible cross-edge; the two omitted cycle vertices and that vertex are
then independent. A connected set through the omitted triangle vertex,
disjoint from the underlying `K_{2,3}` model and touching two of its cycle
bags, would give `Q`. Its existence remains unproved. When it fails, the
component boundary lies in three model bags and `{v}`; this does not bound
the number of actual separator vertices by six. The other spanning
configuration and a decreasing global exchange remain open.

**Written proof; separate internal audit.** The
[five-root wheel theorem](../results/hc7_five_root_wheel.md) requires a
prescribed triangle, internal five-connectivity at all five roots, a
nonempty nonroot set, and degree at least six at every nonroot. A triangle
root with a unique outside neighbour absorbs it, preserving the rooted boundary condition
and every surviving nonroot degree; host order decreases. A connected-prefix
ordering then supplies the wheel, with all roots retained.
Across an actual seven-cut consisting of a four-clique and a three-set,
this closes the case where two vertices of the three-set neighbour the
same clique vertex. Consequently the entire four-clique exterior in the
five-cycle-and-triangle case is four-connected. A three-part allocation
there, or the earlier compatible helper, remains unproved. The theorem
does not assert that a second application survives deletion of its bags.

The [five-root almost-clique strengthening](../results/hc7_five_root_almost_clique.md),
with a separate internal audit, raises the nonroot degree hypothesis to
seven and gives nine contacts. For roots `b,c,r,s,t` with triangle `rst`,
the only possible missing pair is `rb` or `rc`, where `r` is designated
in advance. The same conclusion permits minimum degree six with at most
five degree-six nonroots. The reductions retain this choice and all five
roots. Neither version reserves a sixth helper.

The [cycle-and-triangle exterior proof](../results/hc7_degree8_cycle_exterior.md),
also separately audited, now makes `G-N[v]` connected, of minimum degree
at least five, and full to all eight neighbours. Every exterior vertex
has at most two cycle contacts, consecutive if there are two. Each exterior
component must meet all three triangle vertices: otherwise a contracted
cycle gives a five-root wheel, and another component and `v` complete `Q`.
Explicit combinations then exclude both the two-component and larger
cases. The remaining construction lies inside one connected exterior;
each component behind a cutvertex must meet at least two triangle roots.
These boundary contacts do not yet give three compatible helper bags.

Deleting `v` and a triangle vertex, then contracting two disjoint cycle
edges, passes the new degree test: at most two nonroots have degree six.
It can still shrink a root-free boundary from seven to four, so applying
the internal-five theorem without handling that cut is unsupported.
Even a valid five-root model would leave the deleted triangle vertex's
cycle-bag contacts unproved. A good cycle matching alone is not a terminal
construction; the cut and the additional contacts both need justification.

The [two-triangle exterior theorem](../results/hc7_degree8_two_triangle_exterior.md),
with a separate internal audit, now excludes multiple exterior components
in the other spanning configuration as well. Its wheel lemma removes the
separate degree hypothesis: internal five-connectivity at five roots containing
a triangle and at least two nonroots suffice. The terminal two-nonroot case
replaces further contraction.
For an actual seven-boundary fragment, disjoint paths replace every internal
port by a distinct missing neighbour of `v`, preserving every subset boundary.
An unused eighth neighbour joins the opposite component to form a full helper.
Thus in either spanning configuration `G-N[v]` is connected and full to all
eight neighbours. The one-component construction remains open: the port paths
need not leave a disjoint connected helper through that unused neighbour.

The colouring attempt must also include two-pair colourings. Contracting
`{v,0,2}` in the cycle case and expanding the independent pair gives a
six-colouring of `G-v` with neighbourhood multiplicities `2,2,1,1,1,1`:
the other six neighbours avoid the contracted colour and must use all five
others. This does not require a Kempe sequence from a reserved-triple colouring.
Changing the reserved colour class changes the available five-colour host;
an old model has no automatic lift. Contracting a failed helper component
also loses criticality, and expanding its single colour need not colour its
internal edges. The missing inference is still a joint choice of colouring,
paths and disjoint bags; neither of these operations supplies that choice.

**Written proofs; separate internal audits.** The
[colour-path completion](../results/hc7_cycle_colour_path_completion.md)
proves two terminal constructions: the six old paths plus **any two**
connections from `a0` to `1,3,4`; or the six old paths plus an
`a0--0` path using colours `a0,3` and an `a0--2` path using
colours `a0,4`. The latter needs no `a0--1` connection. Each uses
one proper endpoint-colouring. In the rank-one case, augmentation of
the other two forests moves the deficit to the `a0` projection; an
explicit tree transfer then gives seven disjoint bags. Identifying the
markers is only a rank test, never an asserted host contraction.
Separate one-marker inductions handle root hits and preserve connected
preimages. This resolves the earlier endpoint-loop and root-hit residues.

Consequently **every** reserved-triple colouring can be changed by one
Kempe swap to repeated pairs `{a0,3}` and `{0,2}`, after a dihedral
relabelling of the cycle. The host and critical hypotheses are unchanged.
The new paths must be chosen in the new colouring; the old model is not
asserted to survive the swap. The
[one-path example](../barriers/hc7_one_path_marked_scheme.md) still refutes
the unrestricted single-connection weakening, without the critical data.

**Immediate construction.** In this two-pair colouring take
`A={a0,a1,a2}` and `B={4,0,1}`. The four paths from `a1,a2` to
`1,4` exist because their neighbourhood colours are singleton. It would
suffice to obtain, in the same colouring, the four further connections
`a1--0,a2--0,a0--1,a0--4`. They give a genuine
`K_{3,3}-a0·0` scheme at six distinct-colour roots. The universal
bipartite theorem, literal `A` triangle and `B` path `4--0--1`
give six bags whose only possible missing pairs are `a0--0` and
`1--4`; these are independent. Adding `{v}` gives `Q`.

**A completed colouring state.** The
[flexible-root theorem](../results/bipartite_flexible_root_families.md),
with a separate GREEN internal audit, retains a separate connected bag
for every prescribed root of a bipartite target while permitting a demand
to change endpoints within its two root families. The reduction truncates
at the first actual root-containing piece; it never contracts a disconnected
preimage of an auxiliary identified root. Applied to cycle-colour families
`{0,2},{1,3},{4}`, it completes the state where the triangle uses the
three other colours: one of three cuts of `0--1--2--3` gives a cycle
triangle with at most two independent missing cross-contacts.

This exclusion forces a new connection in the retained two-pair colouring.
The component of `1` in colours `g(1),g(3)` must contain `3`.
Criticality forces it to meet `a0` or `3`; meeting only `a0` would
allow a swap producing the completed three-colour cycle state. Thus an
actual bichromatic `1--3` path exists, although it may pass through
`a0`. The theorem does not preserve a chosen member of a root family
as the endpoint of every contact, so it does not supply the four
connections in the preceding paragraph.

The [cycle-colouring theorem](../results/hc7_cycle_colour_cross.md), with
a separate GREEN internal audit, gives actual disjoint paths from a stronger
quantified restriction. In a five-colourable graph, if every five-colouring
uses at least four colours on a specified `C_5`, there are two disjoint
paths with alternating cycle endpoints and interiors outside the cycle.
Without such a cross, at most four Kempe swaps give three cycle colours.
In the critical host, contracting `va` supplies a colouring where the
triangle root `a` is uniquely coloured on `N(v)`. Delete its whole
colour class `I`. Every five-colouring of `G-v-I` must use at least four
cycle colours, by the completed state above, so a cross exists there.
Its four branch vertices are actual cycle roots. It may use the other
two triangle roots, and crosses from different colourings have no joint
ownership guarantee. The first unsupported assembly is retaining those
roots as additional disjoint bags after the paths have used them. A joint
construction must retain the every-colouring condition as well as the cross.

**Audited barrier to discarding the original host.** The
[cycle-palette counterexamples](../barriers/hc7_cycle_palette_extension_barrier.md)
refute an unrestricted extension of that colouring argument. In the stronger
example, the seven roots induce exactly `C_5` disjoint-union `K_2`; every
five-colouring uses all five root colours and at least four cycle colours,
yet the graph excludes both `Q` and `P=K_7-3K_2` (three independent deleted
edges). Private colour-forcing gadgets and a two-clique-sum localization
proof establish this without finite minor testing. The first invalid
inference is that the quantified palette condition alone forces either
minor. Both examples contain a literal `K_5^-`, already excluded in the
actual host. A repair must therefore retain additional critical-host data,
such as the literal exclusions, connectivity and compatible restoration of
the deleted independent class. The cross theorem and the full cycle case
are unaffected; the latter remains open.

**A second exact cycle construction; its final partition is open.** Let
`e=xy` be any cycle edge, `n=|V(G)|`, `q=e(G)-4n>=0`, and
`c=|N_G(x) intersect N_G(y)|`. The total degree excess is `2q`, while
`d(x),d(y)>=c+1`; hence `c<=q+7`. In the simple quotient
`F=(G/e)-v`, there are `n-2` vertices and

```text
e(F)=e(G)-1-c-7=4|V(F)|+q-c >= 4|V(F)|-7.
```

The four images `Z` of the cycle span a `C_4`. The graph `F` is
five-connected: a cut of order at most four lifts, on restoring `v` and
both ends of the contracted edge, to a cut of order at most six in `G`.
[Norin--Totschnig, Lemma 12](https://arxiv.org/html/2507.03244v1#S2),
whose primary statement was inspected, and
[spanning-helper normalization, Lemma 3](../active/hc7_companion_helper_construction.md)
therefore give adjacent connected helpers `U,V` partitioning
`J=F-Z=G-v-C`, both contacting every singleton root in `Z`.

If **some** choice of cycle edge and helper partition places triangle
vertices on both sides, then `{v}`, `U,V` and the four lifted cycle bags
give `K_3 join C_4=Q`. The only nonsingleton cycle preimage is `{x,y}`;
the seven bags are disjoint, and each helper meets `N_G(v)` through its
triangle vertex. Equivalently, for `D_z=N_F(z) intersect J`, find a
connected bipartition of `J` splitting every `D_z` and the triangle `A`.
Splitting the four `D_z` is already guaranteed; splitting `A` is not.

The actual retained graph `J` has minimum degree at least six: an exterior
vertex loses at most two cycle neighbours, and a triangle
vertex loses `v` and at most one cycle neighbour. These contact bounds are
in the audited [exterior theorem](../results/hc7_degree8_cycle_exterior.md).
The [three-connectivity theorem](../results/hc7_cycle_triangle_complement_three_connectivity.md),
with two separate internal audits, excludes every two-cut of `J`.
On its triangle side, an integral flow preserves all prescribed cut
endpoints; a bridge reroutes one path when two have the same triangle
source, leaving two cycle contacts in a third disjoint piece. The opposite
side supplies a designated almost-clique, giving two independent possible
missing contacts and a valid `Q` model. No four-connectivity of `J` is
proved; the known four-connectivity is for the different graph `G-v-A`.
Moving a triangle-containing region to
the other helper may destroy a required `D_z` contact. No exchange that
preserves all four contacts and strictly decreases a well-founded parameter
has been proved. The contraction above is one fixed step with a valid
minor lift, not an induction preserving criticality or seven-connectivity.

**Recorded route nonclosure.** Criticality forces each singleton-colour
root to be bichromatically connected to at least one root of a repeated
colour, but these may be `2` instead of `0`, or `3` instead of `a0`.
The first unsupported inference is obtaining all four specified
connections in one colouring. Replacing alternative endpoints after
extracting a model can reuse vertices owned by other bags.
A joint choice using the full proper-minor colouring data, a different
terminal model, or a decreasing reduction with a valid lift is still
needed. The original colouring, its six actual paths and the swapped
component also remain available. Old paths may now use three colours;
they are not automatically paths of a scheme for the new target.
The four-colour attachment limitation in Section 7.7 remains
applicable; no colouring or connected preimage may be discarded without
its required replacement.
