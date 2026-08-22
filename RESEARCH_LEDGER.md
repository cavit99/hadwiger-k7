# Hadwiger `K_7` research ledger

**Last updated:** 22 August 2026
**Authoritative status:** `HC_7` is not proved here.  Neither is the
`K_7^-` six-colour conjecture.  Internal audits are not external peer
review.  Hadwiger's conjecture is known for `t<=6` and remains open for
every `t>=7`; `HC_7` is the first open case, not the only open case.

The previous live ledger is preserved at
[`archive/RESEARCH_LEDGER_2026-08-02.md`](archive/RESEARCH_LEDGER_2026-08-02.md).
This file is the sole authority for the present research frontier.

## Current frontier

**T44 campaign pivot, 22 August 2026.**  The sole active completion target is

> **T44.** Every seven-connected graph containing a `K_{4,4}` minor contains
> a `K_7^-` minor.

T44 is open.  It would prove Norin--Totschnig Conjecture 21: a
minor-minimal non-six-colourable target-free graph is seven-connected, and
Kawarabayashi--Toft prove that every seven-chromatic graph has a `K_7` or a
`K_{4,4}` minor.  The first alternative already contains the target and T44
would close the second.  T44 would not by itself prove `HC_7`.

The first falsification pass found no counterexample.  Exact certificate
searches cover every seven-connected graph through order eleven, including
all `9,940` order-eleven isomorphism types.  A separate monotone reduction
and exact search closes all `105` edge-minimal representatives of the
unbounded full-attachment non-clique seven-sum family.  These are bounded
and family results, respectively, and no global inference is made from
them.

The promoted local input is now substantial.  Four prescribed roots in a
three-connected graph have a rooted `K_4^-` model.  A double cone over a
five-connected graph forces `K_7^-`.  In a vertex-minimal nonliteral T44
counterexample, every internal branch-bag edge belongs to an exact
seven-cut.  A strengthened seven-vertex boundary theorem shows that every
such cut `Z` in a target-free host satisfies `delta(G[Z])<=3`.  For a
literal `K_{4,4}` core, the exterior is three-connected; a triangle of
four-portal bags is terminal; and a spanning `K_4` of three-portal bags is
terminal, with the sole tetrahedral local exception excluded by global
portal coverage.

Two obligations remain, and neither is a proved intermediate theorem.  In
the literal case one needs a core-sensitive labelled trichotomy producing
the terminal portal triangle, the terminal spanning `K_4`, or six
positive-portal exterior bags forming a `K_6^-` model.  The whole literal
core is the seventh bag in the last outcome.  The trichotomy is proved by
hand only through exterior order six and is supported, not proved, at order
seven by an exact Z3 census.  In the nonliteral case the exact cuts must be
converted into a well-founded labelled branch-model rotation.  Exact cuts
alone do not give a peel side, laminarity or preservation of branch
ownership.  The authoritative hypotheses, falsification data, trust
boundaries and stop rules are recorded in the [T44 technical
frontier](active/hc7_k44_closure_frontier.md).

The sound adjacent-true-twin induced-`C_7` chain, together with the RED
st-numbering audit and its 140 obstruction profiles, is preserved in
[`archive/adjacent-true-twin-c7-2026-08-17/`](archive/adjacent-true-twin-c7-2026-08-17/README.md).
It is not on the active spine.  The entries below retain promoted results
and the former campaign state as durable context; unless selected from
[`active/INDEX.md`](active/INDEX.md), the exceptional-centre and
six-connected-density threads are frozen rather than concurrent targets.

**Audited standalone theorem, 16 August 2026.**  Every complete bipartite
graph `K_{2,n}` is contractible in the sense of graph schemes.  The new
computation-free proof projects a coloured scheme onto two graphic matroids,
proves Edmonds' disjoint-base inequalities by a path--component count, and
lifts the resulting two spanning trees to a rooted `K_{2,n}` minor.  It
answers the `K_{2,4}` half of Kündgen--Pelsmajer--Ramamurthi Question 8.2
uniformly for all `n`; the [theorem](results/k2n_contractibility_via_matroid_packing.md)
and [hash-pinned internal audit](results/k2n_contractibility_via_matroid_packing_audit.md)
are promoted results.  It does not settle `K_{3,3}`, the `K_7^-` six-colour
conjecture, or `HC_7`.

**Five-root partial-routing theorem, 17 August 2026.**  The independently
twice-audited
[Kriesell--Mohr application](results/llru_question61_via_km_property_star.md)
proves that five roots spanning at least four literal edges have a rooted
`K_5` minor whenever every nonliteral root pair is joined inside its two
prescribed disjoint packets.  It answers Lafferty--Liu--Rolek--Yu Question
6.1 affirmatively and, by the consequence stated explicitly by those
authors, lowers their eight-connectivity threshold for
contraction-critical graphs from `k>=17` to `k>=11`.  This is a new
application of Kriesell--Mohr Theorem 7, not new property-`(*)` machinery.
Rolek--Song Lemma 1.7 gives the following exact local consequence in the
present campaign: at a degree-eight critical vertex `x`, every independent
neighbour triple `S` for which `R=N(x)-S` spans at least four edges yields
an `R`-rooted `K_5` minor in `G-(S\cup\{x\})`.  In the
adjacent-true-twin induced-`C_7` case this holds for every independent
triple, with the twin fixed as a singleton branch set.  The resulting
seven-bag construction still may miss the two contacts from one
independent-triple vertex to its two opposite rooted bags.  Neither that
connector problem, Conjecture 21, nor `HC_7` is solved; the
Norin--Totschnig benchmark remains unmet.

**Direct campaign advance, 17 August 2026.**  A new audited
[six-connected degree-eight theorem](results/hc7_k7minus_sixconnected_degree_eight_low_codegree.md)
shows that every degree-eight vertex of every six-connected target-free
graph has an incident edge contained in at most three triangles.  Its
coefficient-four contraction iterates with connectivity and gives the
global defect ladder `9n-2m>=20+kappa(G)`.  In the critical host this
improves the exceptional-vertex inequality from `n_8-tau>=25` to

\[
                              n_8-\tau\ge27.             \tag{A}
\]

Thus both former defect layers 25 and 26 are eliminated, not merely one
degree sequence.  The computation-free exceptional-neighbourhood
[precursor](results/hc7_k7minus_degree_eight_triangle_poor_edge_packing.md)
also gives a linear-size covering by such edges.  The associated audited
[critical-contraction reduction](active/hc7_k7minus_critical_to_sixconnected_4n_reduction.md)
shows that any hypothetical counterexample has a proper quotient `H` which
is six-connected, exactly six-chromatic, target-free and satisfies
`|E(H)|>=4|V(H)|`.  It also retains a specified contracted vertex and a
seven-vertex set which uses all other five colours in every six-colouring.
Consequently the universal six-connected `4n` extremal theorem would prove
Conjecture 21, although only quotients with this stronger colouring trace
need be excluded.  Neither that extremal theorem nor Conjecture 21 is proved
here; the Norin--Totschnig significance benchmark remains unmet.

**Critical-edge dichotomy, 17 August 2026.**  The independently audited
[codegree-three separator theorem](results/hc7_k7minus_critical_codegree_three_separator_or_surplus.md)
removes the former degree bound on the second endpoint.  At a selected
degree-eight vertex of every hypothetical critical host, either an incident
edge has codegree at most two, in which case its contraction is
six-connected, exactly six-chromatic, target-free and has at least
`4|V|+1` edges, with the retained seven-vertex five-colour trace; or the
edge has codegree three, in which case every spanning `K_6` model after
deleting its ends has a branch set whose every rooted split exposes an
actual separator.  One of the resulting separator boundaries can always be
chosen to contain the degree-eight endpoint; its order is at least seven
and it is full at order seven.  This replaces the former high-degree-surplus
incidence alternative by two exact structural outcomes.  Neither an upper
bound on the separator order nor elimination of the positive-surplus
six-connected quotient is proved, so the primary conjecture and the
Norin--Totschnig benchmark remain open.

The adjacent audited
[separator-order barrier](barriers/hc7_degree_eight_prescribed_separator_order_barrier.md)
shows why the second outcome cannot be finished by connectivity, a
degree-eight boundary vertex and separator-side minimisation alone:
`K_{8,n}` has connectivity eight and a prescribed degree-eight boundary
vertex, yet the least boundary order of such a connected separator side is
`n`.  The construction is target-rich, so it does not refute a
critical-host theorem; it proves that target exclusion or the full
proper-minor colouring system must enter any order bound.

**Returned-cut elimination, 17 August 2026.**  Two independently audited
theorems now eliminate every dense three-component cut returned by a
minimum enemy to the six-connected `4n` target.  The
[dense-boundary theorem](results/hc7_k7minus_returned_three_component_dense_boundary_elimination.md)
uses target-sensitive rooted `K_4` exclusions and sharp forms of the
Norin--Totschnig four-root bounds to eliminate all three eight-edge boundary
types and six of the seven seven-edge types, for components of arbitrary
order.  The companion
[type-VII theorem](results/hc7_k7minus_returned_type_vii_elimination.md)
eliminates the final seven-edge type: its rooted inequalities force doubled
attachments into one or two literal `K_2` components, and three independent
exact minor searches certify all 121 resulting quotient profiles.  Hence a
minimum target-free six-connected graph with at least `4n` edges can now
return only

\[
 \begin{array}{ll}
 r=2:& |E(G[S])|\le11,\\
 r=3:& |E(G[S])|\le6.
 \end{array}                                                   \tag{B}
\]

This is an unbounded direct elimination of a broad returned-cut class; it
does not eliminate either row in (B), prove the universal `4n` theorem, or
prove Conjecture 21.  The Norin--Totschnig significance benchmark therefore
remains unmet.

**Two-component and full-exterior checkpoint, 17 August 2026.**  The
independently audited
[order-two dense-lobe theorem](active/hc7_k7minus_returned_order_two_dense_lobe_elimination.md)
contracts the arbitrary opposite lobe and exhausts the resulting `122,941`
labelled nine-vertex quotients with two independent exact algorithms.  It
eliminates the order-two outcome in the dense returned two-component descent.
For `e(S)>=3`, only the one- or two-vertex boundary atom and the nested
near-model separator remain.  Independently, an audited census of all
`611,678` relevant six-connected
[adjacent exterior-pair quotients](active/hc7_k7minus_adjacent_exterior_pair_elimination.md)
proves that a connected full degree-eight exterior cannot contract to two
adjacent blocks while retaining six-connectivity.  Its computation-free
[terminal consequence](active/hc7_k7minus_full_exterior_contraction_terminal.md)
is unbounded: every maximal connectivity-preserving exterior contraction
ends in an exactly six-connected quotient with at least three exterior
images, and contracting any remaining exterior edge is exactly
five-connected and lifts to a full exact six-cut.  The cumulative
common-neighbour loss is not controlled and those cuts need not lift as
order-six cuts of the original graph.  Thus this is a new global normal
form, not a proof of the coefficient-four extremal theorem or Conjecture 21.

**Common-centre and sparse-six-cut machinery, 17 August 2026.**  The audited
[global edge--centre incidence theorem](active/hc7_k7minus_common_remote_edge_multicentre_cube.md)
uses the defect ladder `n_8-tau>=27` to show that every edge of a hypothetical
critical host is remote from at least fourteen degree-eight centres and
hence from three independent such centres.  Every five-edge matching also
has one exceptional centre remote from at least three of its edges.

On the sparse returned row, the consolidated
[technical frontier](active/hc7_k7minus_sixconnected_4n_sparse_threecut_frontier.md)
now records an unbounded exact-six descent.  Independent audits verify the
[rerooting theorem](active/hc7_k7minus_six_boundary_fragment_rerooting.md),
the [prescribed-boundary minimisation](active/hc7_k7minus_prescribed_vertex_separator_minimisation.md),
and the [cycle-rank bound](active/hc7_k7minus_sparse_sixcut_cyclic_residue.md)

\[
 |C|\le28+2\beta(C),\qquad |C|\le25+2\beta(C)
 \quad\hbox{if }\Delta(G[S])\ge2,
\]

with respective nontrivial-tree bounds `22` and `19`.  A spanning rooted
`K_4` confines each omitted root to two branch sets; a four-portal return is
an exact order-six fragment and exchanges at least two roots, eliminating
the former one-root-exchange residue.  Punctured rooted-model exclusion and
the coefficient-four excess are hereditary across that fragment.  In the
two-root exchange, clean paths and a boundary-full connected-subgraph repair
give explicit `K_7^-` models unless the internal portals control separate
essential arms.

Independently, an ordinary `K_5^-` minor roots at component order at most
six, and a literal `K_5^-` subgraph roots at arbitrary component order; in a
larger minimum nonliteral obstruction every branch-set contraction returns
another exact order-six fragment.  The order-seven Hall row now records only
collective domination by a deficient singleton family: individual
universality is forced only when that family has order one.  Two
boundary-composition theorems force one branch set with at most one boundary
neighbour or three branch sets with at most two each.

The independently twice-audited
[exact-singleton theorem](active/hc7_k7minus_sparse_sixcut_threeconnected_minorfree_exact_singleton.md)
removes the no-exact-fragment subcase of the three-connected
ordinary-minor-free case.  By Wood--Woodall, the lobe is a wheel, the
triangular prism or `K_{3,3}`; an exact finite mask lemma and the
target-sensitive four-root packing bound force a total-degree-six vertex.
Its neighbourhood is an exact six-cut and the returned singleton has
coefficient-four excess exactly `2`.  This supersedes the former
order-`31`/excess-`62` bounded-core residue, but the exact fragment is a
descent output rather than a terminal contradiction.  Transfer across the
derived cut, ordinary-minor lobes and nested two-separation chains remain.
The exact open local theorem sufficient to close the whole case is still

\[
 \text{no punctured five-rooted }K_5^-\text{ model}
 \quad\Longrightarrow\quad
 \eta_U(X)\le5\mu_U(X).                              \tag{C}
\]

Equivalently, `eta_U(X)>=5 mu_U(X)+1` must force the rooted model.  The
sharp packet-one subcase `eta_U(X)>=6 =>` rooted model or `mu_U(X)>=2`
suffices when the boundary has maximum degree at least two, because then
every lobe has `mu=1`, but it leaves the possible `mu=2` lobe uncontrolled
in the matching-boundary row.  The audited orientation theorem shows that
the weighted form (C), not merely the packet-one subcase, would eliminate
the whole sparse three-component row.  Exact enumeration through every
connected internal graph of order four supports the packet-one subcase
only; it is not an unbounded proof.  Explicit barriers rule out
incidence-only, abstract three--two connectedness and automatic rooted-`K_4`
augmentation shortcuts.
Thus the universal `4n` theorem, Conjecture 21 and the Norin--Totschnig
benchmark remain open.

**New-literature check, 17 August 2026.**  Lo's arXiv:2603.27973v1 states
that every four-connected non-planar graph of minimum degree at least five
has a `K_6^-` minor.  The primary-source statement and the repository's
[elementary-minor deductions](active/hc7_k7minus_lo_elementary_minor_robustness.md)
have been checked, but the preprint is unrefereed and its finite terminal
figures have not all been independently reconstructed here.  More
importantly, it supplies an unrooted model where the current route already
has an unrooted `K_6`; it does not force the branch bags to meet the specified
degree-eight neighbourhood.  It therefore does not close the rooted
augmentation bottleneck.

**Campaign restart, 16 August 2026.**  The protected-centre fan-to-root
attack remains stopped at its recorded hard proof gate; no hidden branch-set
ownership is inferred from that fan.  Discovery has resumed through a suite
of separately audited mechanisms.  Chu's prescribed-set theorem gives a
seven-removable edge completely outside the closed neighbourhood of every
exceptional centre; an independent neighbour triple then produces an exact
`80`-pattern operation cube and an actual order-seven/eight separation with
oppositely oriented responses.  The topological reduction eliminates the
connected order-seven exterior and, in the nonfull return, puts all fifteen
operation signatures against one partition-disjoint reverse response on a
common exact-seven cut.  That return now grows to one five-edge forest with
all `3^5-1=242` nontrivial minor-operation patterns exactly six-chromatic,
all 31 nonempty equality signatures, and a renewed spanning exact
`K_7^\vee` model.  In the cross-miss/full order-seven and both-full
order-eight cases, the remote edge is nonseparating in its exterior
component and lies on four prescribed cycles; the proof includes an exact
252-case minor verification.  The connected-full order-eight case now has
one six-connected centre-deletion graph carrying the complete pointed
signature family and an exhaustive lift of every six-separation.  In
parallel, a general linear-forest threshold theorem closes the portal
two-cycle target, and minimum path-bag ownership eliminates the
nonrepeated order-nine allocation case.  The conjecture remains the sole
primary target and remains open; the active obstruction is operation-to-
model alignment on the bounded exceptional-centre interface, not the
frozen fan-to-root line.

### 1. Exhaustive global obligation

The sole active research target is T44.

> **T44.** Every seven-connected graph containing a `K_{4,4}` minor contains
> a `K_7^-` minor.

This statement is open.  By the contraction-critical reduction and the
Kawarabayashi--Toft `K_7`-or-`K_{4,4}` theorem, T44 would prove
Norin--Totschnig Conjecture 21.  Conjecture 21 is still weaker than `HC_7`:
forcing a `K_7^-` minor in every seven-chromatic graph does not force a
`K_7` minor.

The formerly primary density statement

\[
 \kappa(G)\ge7,\qquad |E(G)|\ge4|V(G)|-2
 \quad\Longrightarrow\quad K_7^-\preccurlyeq G
\]

remains a sufficient open theorem, but it quantifies over arbitrary dense
seven-connected graphs and discards the proper-minor colouring responses of
a hypothetical counterexample.  It is therefore retained as a conditional
extremal route rather than the active primary target.

### 2. Frozen conditional refinement: the critical host

Assume Conjecture 21 false and let `G` be minor-minimal subject to being
non-six-colourable and `K_7^-`-minor-free.  The audited computation-free
critical-host chain now gives

\[
 \kappa(G)\ge7,\qquad n_7=0,\qquad \delta(G)\ge8,
 \qquad |E(G)|\ge4|V(G)|,
\]

excludes every literal `K_5`, and gives

\[
 n_8\ge27+\sum_{i\ge10}(i-9)n_i.                     \tag{1}
\]

Every degree-eight vertex has a `K_4`-free neighbourhood.  Every order-seven
cut has exactly two complementary components.  Consequently the following
is a headline-equivalent finishing theorem, not a routine local lemma:

> **Exceptional-centre finishing target.** Every graph satisfying the
> critical-host hypotheses has at most 26 degree-eight vertices.

This would contradict (1) and prove Conjecture 21 directly.  The former
technical statement, proved inputs and exact surviving allocation problem
are recorded in the
[critical-host frontier](active/hc7_k7minus_seven_exceptional_frontier.md).

The [critical-contraction reduction](active/hc7_k7minus_critical_to_sixconnected_4n_reduction.md)
is a second, direct conditional refinement.  It preserves enough density to
reach `4|V(H)|` after one contraction while retaining the exact split and
five-colour-surjectivity data.  The immediate universal extremal target is

\[
 \kappa(H)\ge6,\qquad |E(H)|\ge4|V(H)|
 \quad\Longrightarrow\quad K_7^-\preccurlyeq H,       \tag{2}
\]

but proving (2) for arbitrary graphs is stronger than the critical-host
route requires.  Existing degree-six separation arithmetic does not close
this target by itself; explicit target-rich examples at exact density `4n`
defeat every orientation of the current numerical composition lemma.  Any
completion must use target exclusion or the retained colouring trace to
construct the rooted near-clique model.

The sharper
[critical-edge dichotomy](results/hc7_k7minus_critical_codegree_three_separator_or_surplus.md)
now makes this refinement exhaustive at a degree-eight vertex.  Codegree at
most two improves the quotient density to `4|V(H)|+1`.  Codegree three no
longer needs a bound on the other endpoint: the proved `t=6` case of
Hadwiger supplies a spanning `K_6` model after deleting the edge ends, and
target exclusion splits a mixed branch set into an actual separation whose
boundary contains the degree-eight endpoint.  The remaining obligations are
therefore a target-sensitive use of that prescribed boundary vertex, or a
strict-surplus version of the six-connected extremal theorem; neither is yet
proved.

The audited
[independence-four elimination](results/hc7_k7minus_alpha4_regular_ramsey_elimination.md)
now closes one exhaustive branch.  There is no 25-vertex 8-regular graph
with independence number four and clique number at most four; the finite
part is certified by 40 checked DRAT refutations.  Applied to the critical
host, this rules out independence number four in the graph induced by its
degree-eight vertices.  Since `R(4,5)=25` and the host has no literal
`K_5`, every hypothetical counterexample therefore contains five
independent degree-eight centres.

The new audited
[remote removable-edge and operation-cube theorem](results/hc7_k7minus_remote_removable_edge_operation_cube.md)
now applies at every one of those exceptional centres.  For an exceptional
degree-eight vertex `z`, it gives an edge

\[
                         f\in E(G-N[z])
\]

such that `G-f` is still seven-connected.  If
`I=\{x_1,x_2,x_3\}\subseteq N(z)` is independent, then

\[
              T=\{zx_1,zx_2,zx_3,f\}
                    \cong K_{1,3}\mathbin{\dot\cup}K_2          \tag{R0}
\]

supports all `3^4-1=80` nontrivial labelled keep/delete/contract patterns
as exactly six-chromatic proper minors.  The full deletion host is exactly
five-connected, has all fifteen nonempty signatures and has a spanning
exact `K_7^\vee` model.  More importantly, if `C` is the component of
`G-N[z]` containing `f`, then `Q=N(C)` has order seven or eight.  The seven
nonempty star signatures restrict properly to the closed `C`-shore, while
the `f`-only signature restricts properly to the opposite closed shore; the
remote partition differs from every star-labelled partition.  If all three
star leaves lie on the boundary, at least five distinct boundary partitions
survive; if exactly two lie there, at least three survive.  This is the
current direct bounded finishing interface.

The audited
[remote-interface topological reduction](results/hc7_k7minus_remote_interface_topological_reduction.md)
now removes the connected-exterior order-seven topology completely.  Every
interface lies in exactly one of four rows.  If the second exterior
component is nonfull, its exact order-seven shore carries all fifteen
nonempty `T`-signatures in one orientation and a fresh crossing-edge
partition in the other which differs from all fifteen; this feeds the
existing exact-seven machinery but is not itself a proof of the conjecture.
The three residual topologies are cross-miss/full at order seven, a
connected full exterior at order eight, or two full exteriors at order
eight.  The fixed exact model remains available on the original deletion
host; no persistence through the fresh crossing-edge deletion is asserted.

The audited
[five-edge operation-cube and model-renewal theorem](results/hc7_k7minus_remote_crossing_five_cube_model_renewal.md)
strengthens the full punctured-cube exact-seven return.  A reverse crossing
edge can be chosen disjoint from the three-spoke star and the remote edge,
so one componentwise-induced
`K_{1,3}\dot\cup K_2\dot\cup K_2` supports all `242` nontrivial labelled
keep/delete/contract patterns as exactly six-chromatic proper minors.  Its
common deletion graph realises all 31 nonempty signatures, retains the
fifteen original response colourings and the reverse response literally,
and has a renewed spanning exact `K_7^\vee` model.  The model-separator
dichotomy then exposes a named singleton response or returns a separator
containing all eight forest vertices.  That eight-endpoint allocation is
the exact surviving obstruction; the theorem does not identify operation
blocks with renewed model bags.

The audited
[two-component cyclic-stability theorem](results/hc7_k7minus_remote_two_component_shore_stability.md)
removes every bridge realization of the remote edge in the cross-miss/full
order-seven case and the both-full order-eight case.  In the former, the
component carrying the edge has full-subgraph packing number one, so
seven-connectivity after deleting the edge forces its remainder to stay
connected.  In the latter, an exact 252-case quotient verification over
the seven promoted boundary types rules out every near-full bridge split.
The same theorem localises the complete three-shore response matrix,
forces boundary-partition demand at least three for the remote-only response
at order seven and for every one-coordinate response at order eight, and
puts the remote edge on one internal cycle and on three further cycles
containing each selected pair of star spokes.  Its remaining step is a
response-preserving split of that connected exterior shore, not another
boundary-only enumeration.

The audited
[connected-full centre-deletion theorem](results/hc7_k7minus_connected_full_remote_pole_core.md)
handles the last order-eight topology differently.  Deleting the centre and
the remote edge gives one six-connected, exactly six-chromatic graph of
density at least `4N-5` with a spanning exact `K_7^\vee` model and all
fifteen pointed signatures.  In every six-colouring, unequal remote-edge
ends force all six colours on the eight-vertex neighbourhood, while the
remote-only response uses at most five.  Every six-cut lifts exhaustively
to an operation-labelled exact-seven response, two overlapping order-eight
separations, or one boundary-contained endpoint configuration; otherwise
the centre-deletion graph is seven-connected.  Static boundary topology
does not eliminate the final bridge profile: the retained
[connected-full bridge quotient barrier](barriers/hc7_k7minus_connected_full_bridge_quotient_barrier.md)
is an explicit exceptional order-eight boundary with two adjacent
one-miss images whose full union still has no `K_7^-` minor.  The live
requirement is therefore a colouring- or model-sensitive argument.

### 3. Immediate structural laboratory

The audited
[removable-matching theorem](results/hc7_k7minus_seven_removable_matching_reduction.md)
and [replacement-abundance theorem](results/hc7_k7minus_removable_matching_rotation_abundance.md)
now force one common six-coordinate object.  The audited
[induced-forest reduction](results/hc7_k7minus_six_coordinate_forest_reduction.md)
gives a six-edge forest

\[
                 F\cong 6K_2\quad\hbox{or}\quad4K_2\mathbin{\dot\cup}P_3
\]

whose components are induced in `G`, such that, for `X=G-F`, both of two
distinguished one-edge restorations are seven-connected.  Consequently

\[
 \kappa(X)\ge6,qquad |E(X)|\ge4|V(X)|-6,qquad
 \{\Sigma_F(c):c\in\operatorname{Col}_6(X)\}
                       =2^F-\{\varnothing\}.         \tag{R1}
\]

The graph `X` has a spanning exact `K_7^vee` model, and one literal cycle
of `G` contains every edge of `F`.  The five-edge star which first appeared
in the replacement theorem is therefore not a separate obstruction: the
absence of a literal `K_5` supplies two nonadjacent leaves and turns it into
the induced `P_3` above.  The signature cube in (R1) is automatic from
minor-criticality and componentwise inducedness; the nonautomatic inputs
are the two seven-connected restorations, the common cycle and the exact
model.

The six-coordinate route remains a parallel capstone target:

> **Six-coordinate induced-forest terminalization.**  The critical host
> cannot contain the displayed forest `F` with both distinguished
> one-edge restorations seven-connected.

The target has two exhaustive connectivity rows.

1. If `kappa(X)=6`, every six-cut has exactly two full components and both
   distinguished edges cross them.  The audited
   [complementary-cube lift](results/hc7_k7minus_six_cut_complementary_cube_lift.md)
   first turns every nonsingleton crossing allocation into one actual
   separator of order eight through twelve.  The audited
   [coordinate-localisation theorem](results/hc7_k7minus_six_cut_coordinate_localisation.md)
   now sends each selected coordinate to a strict response-bearing
   separator or to a full component.  If all strict responses, including
   the fresh singleton response at boundary order at least ten, are
   excluded, the boundary has order eight or nine and exactly two or three
   full components.  The two forest types now have sharper, audited normal
   forms.

   * In the matching case, the sole row has boundary order nine.  Two
     opposite distinguished coordinates have one common double-deletion
     host whose six-colourings realise exactly the three signatures
     `(equal,proper)`, `(proper,equal)` and `(equal,equal)`.  One spanning
     `K_6` model co-bags both endpoint pairs; excluding responses of order
     at most eight makes this same host seven-connected and gives it an
     exact spanning `K_7^vee` model.  The audited
     [matching common-state theorem](results/hc7_k7minus_matching_square_common_state.md)
     then spends the absent all-proper signature: an unlocked palette gives
     a crossed response transition, while otherwise all five alternate
     palettes are locked.  The audited
     [selected-edge root-bag response theorem](results/hc7_k7minus_selected_edge_root_bag_response.md)
     splits the common model bag along the selected equality edge and gives
     either `K_7^-` or an actual separator retaining that edge and its
     rejected boundary partition.  Its direct boundary has order at least
     seven; reducing a large boundary numerically to order seven, eight or
     nine uses fresh singleton responses and can lose the original edge,
     model and shore labels.  The audited
     [boundary-reduction theorem](results/hc7_k7minus_matching_lock_boundary_reduction.md)
     sends every large actual response boundary numerically to order seven,
     eight or nine via fresh singleton responses; the matching and model
     labels need not survive that descent.  Its only sharp order-nine
     fallback is the existing full-component degree-nine pole.
     Independently, the audited
     [order-nine projection theorem](results/hc7_k7minus_order9_crossed_transition_projection.md)
     projects an unlocked transition onto at most four vertices of the
     original boundary.  It yields either one boundary colouring rejected
     by both shores or one boundary Kempe interchange supported by named
     opposite-shore components.  If no bounded response is available, each
     all-lock component is connected, dominating and three-chromatic, with
     a four- or five-chromatic `K_6`-minor-free complement.
     The separately audited
     [all-lock branch-set transfer gate](active/hc7_k7minus_all_lock_branch_transfer_gate.md)
     records a precise route nonclosure: a proper initial segment of one
     connected lock component is not a valid Kempe interchange, while
     switching the whole component leaves the selected equality edge
     monochromatic.  Thus blocked branch-set absorption in one fixed lock
     colouring does not produce an original-labelled response separator or
     a common shore partition.  Any continuation must compare different
     realised signatures, or spend target exclusion in a genuinely new way.

     That comparison has now passed a hard proof gate.  The written and
     separately audited
     [cross-signature pivot theorem](active/hc7_k7minus_cross_signature_pivot_gate.md)
     proves that the ordinary foreign-bag deficiency profile is independent
     of the colouring, so its `EP`, `PE`, and `EE` values repeat the same
     data.  If one `EE` colouring is adjacent by Kempe interchanges to both
     singleton signatures, however, the two components must interact
     literally: their palettes share exactly one colour, and the components
     either share a vertex of that colour or have an edge between their two
     other colour classes.  Otherwise the two switches combine to the
     forbidden `PP` signature.  What is not forced is one common `EE` pivot,
     or placement of its interaction on a deficient model label.

     The separately audited
     [static two-split profile barrier](barriers/hc7_k7minus_static_two_split_profile_barrier.md)
     makes the second issue exact.  The graph `K_{2,2,2,2}` has a common
     labelled `K_6` model with both selected splits blocked at three foreign
     double contacts, no literal `K_5`, and no `K_7^-` minor.  The exhaustive
     quotient diagnostic retains `30,652` target-free, `K_5`-free blocked
     profiles.  The example has the forbidden `PP` signature and is not a
     critical host, so it does not refute a cross-signature theorem; it
     proves that uncoloured deficiency profiles cannot perform the missing
     conversion.  The matching route is therefore frozen pending a
     Kempe-valid, model-monotone exchange, rather than another fixed-lock or
     static-profile argument.
   * In the induced-`P_3` case, the audited
     [common-model theorem](results/hc7_k7minus_p3_opposite_coordinate_common_model.md)
     puts each leaf response on a seven-connected two-edge host and puts
     the crossing matching edge and the whole induced path in one common
     co-bagged `K_6` model.  The order-nine host becomes seven-connected
     after bounded responses are excluded.  The order-eight row has the
     exact three-crossing normal form and two complete geometric linkages
     sharing one shore fan.

     The new audited
     [minimum path-bag owner-circuit theorem](results/hc7_k7minus_p3_owner_circuit_compression.md)
     now attacks the branch-set allocation directly.  Choose a spanning
     co-bagged `K_6` model with its path bag minimum.  Every component left
     after deleting the induced path owns at least two of the five foreign
     bag adjacencies; owner sets are disjoint, so there are at most two
     components.  Rado--Menger deficiency gives a minimal owner circuit of
     order two through four.  An all-five circuit would create a four-cut
     separating the retained path bag from the connected union of the five
     foreign bags, and is therefore impossible.  The exact output is a
     shared differently labelled contact, a repeated contact in one foreign
     bag, or a component boundary of order seven or eight.  In the
     nonrepeated case the boundary is exactly `2+5` at order seven or `3+5`
     at order eight, and it carries the original three path responses on the
     same literal shore.  Thus the nonrepeated order-nine branch and the old
     operation-provenance mismatch are eliminated; shared/repeated contact
     absorption remains open.

   Thus path existence, unrelated-model choice and an unbounded unlocked
   separator are no longer the first gaps.  The matching residue is to
   allocate one dominating lock or one projected transition to four
   foreign model bags, or preserve its labels through the order-nine
   response.  The induced-path residue is the corresponding triple split:
   four foreign bags must meet all three pieces of the co-bagged path, or a
   labelled order-seven response must be returned.
2. If `kappa(X)>=7`, the audited
   [growth-or-feedback theorem](results/hc7_k7minus_six_coordinate_growth_or_feedback.md)
   says that the coordinate forest either grows to an eight-edge
   componentwise-induced forest whose deletion is seven-connected and
   still has an exact spanning `K_7^vee` model, or `G` has a feedback
   vertex set `T` of order at most fourteen with `chi(G[T])>=5`.  The
   latter alternative is now impossible.  The separately audited
   [bounded-feedback degree elimination](results/hc7_k7minus_bounded_feedback_degree_elimination.md)
   combines the exact degree defect from (1), the forest identity for
   `G-T`, and a sharp edge bound for a `K_5`-free five-critical subgraph of
   `G[T]`.  It first forces `|T|=14` and `25<=|V(G)|<=27`, then uses the
   degree-eight vertices inside `T` to contradict the same defect
   inequality.  This argument is unbounded and computation-free.  Hence
   `kappa(X)>=7` now forces the eight-coordinate exact-model host.  The
   earlier full-shore, `7,6,7` and six-component feedback reductions remain
   proved infrastructure, but none is a live residue.

   The written and separately audited
   [eight-coordinate endpoint-visibility theorem](results/hc7_k7minus_eight_coordinate_endpoint_visibility.md)
   now spends the full response cube on that exact model.  Maximising the
   number of coordinate endpoints in the closed neighbourhood of the
   deficient branch set gives an exact branch-set transfer: moving a
   connected piece either constructs `K_7^-`, returns an actual separator
   retaining a singleton `F_8` response, or strictly increases that score.
   The third outcome cannot persist.  Pigeonhole over the fifteen or sixteen
   endpoints then forces two endpoint portals in one universal bag, where
   the exact-model dichotomy again gives the target or an original-coordinate
   response separator.

   Hence the eight-coordinate host is no longer an unlocalised model
   allocation problem.  It has the exhaustive conclusion

   \[
       K_7^-\preccurlyeq G
       \quad\text{or}\quad
       \text{an actual separator carrying a singleton }F_8\text{ response}.
   \]

   Generic density descent reduces the latter numerically to a response
   boundary of order seven, eight or nine, but may replace the forest edge
   by an unrelated singleton operation.  The audited
   [fixed-coordinate response-core reduction](results/hc7_k7minus_fixed_coordinate_response_core_reduction.md)
   instead preserves the edge and colouring while decreasing side order,
   but need not decrease the boundary.

   The new audited
   [model-anchored hull theorem](results/hc7_k7minus_model_anchored_response_hull.md)
   preserves the containing exact-model bag, a connected bag complement and
   a named anticomplete bag during that descent.  Minimising globally over
   the eight coordinate responses and all ordinary exact models then gives
   the audited
   [appendage-ownership normal form](results/hc7_k7minus_model_anchored_appendage_ownership.md):
   a terminal nonsingleton side consists of one boundary-list-critical core
   and at most two coordinate-free appendages.  Each appendage monopolises
   at least two foreign model adjacencies, and the monopoly sets are
   disjoint.  This is an unbounded use of the exact model rather than a
   boundary-size assumption.

   The appendages each carry a fresh attachment-edge response.  The audited
   [operation-provenance comparison](results/hc7_k7minus_operation_provenance_exchange.md)
   places that response and the retained forest response on one deletion
   host and determines its exact equality signatures.  It yields a
   six-colouring, both forest-edge ends on the appendage boundary, or two
   nonempty disjoint boundary-partition languages.  The equality-on-both-
   edges colouring does not transfer provenance: the critical core retains
   the forest coordinate but disconnects the branch-bag complement, while
   an appendage has connected complement but only the fresh operation.  The
   exhaustive
   [appendage quotient diagnostic](active/experiments/model_anchored_appendage_quotient_gate/README.md)
   leaves target-free profiles for every ownership allocation, including
   all `2+3` allocations.  Static ownership is therefore exhausted.

   At a singleton, the audited
   [coordinate-localisation theorem](results/hc7_k7minus_singleton_coordinate_localisation.md)
   proves the exact fork.  Either a fresh incident edge gives one induced
   path whose common deletion host realises all three nonempty signatures,
   or the mate of the forest coordinate dominates the remaining
   neighbourhood.  In the path case, the audited
   [common-deletion theorem](results/hc7_k7minus_singleton_induced_path_common_deletion.md)
   proves that the host is seven-connected or an actual order-seven or
   order-eight separation retains the whole response square.  The
   seven-connected outcome is precisely the deferred induced-path
   three-piece model-allocation problem; opening a second version of that
   campaign would add no new labels.

   The dominated case has now been terminally aligned.  The audited
   [common-neighbour two-cut theorem](results/hc7_k7minus_dominated_singleton_twocut_response.md)
   gives two actual response components and an exact exclusive switch
   between the forest edge and every fresh incident edge.  At most six such
   fresh edges are essential to the fixed exact model.  The new audited
   [low-degree completion](results/hc7_k7minus_dominated_singleton_low_degree_terminal.md)
   treats degrees eight and nine by an exact marked-neighbourhood
   classification: only three marked instances survive, and contracting an
   exterior component constructs `K_7^-` in every one.  Together with the
   high-degree count, every dominated singleton therefore supplies one
   common graph carrying the original exact model, the original forest
   colouring, a fresh exclusive response and an actual response component.

   Centre-preserving visibility now bypasses that unbounded component.  At
   an original degree-eight centre `u`, the exterior of `N[u]` is connected
   and the boundary is exactly `N(u)=Q\dot\cup\{v\}`, where `v` is complete
   to the seven vertices of `Q`.  Target exclusion and the complete rooted
   seven-terminal kernel reduce `Q` to

   \[
      C_5\dot\cup K_2,\qquad C_5\text{ with a pendant }P_2,
      \qquad C_7.
   \]

   Put `H=G-\{u,v\}`.  It is five-connected and contains the four other
   independent degree-eight centres.  Protect `Q` and two of those centres
   through one common terminal-legal contraction.  The resulting
   nine-terminal irreducible kernel has order at most eleven.  The written
   and audited
   [two-protected-centre theorem](active/hc7_k7minus_dominated_two_protected_centres_kernel.md)
   eliminates order eleven unconditionally, so the common kernel has order
   nine or ten and at most one nonterminal.

   The finite residue is exact.  At order ten, Wu's contractible-edge
   theorem gives 1,153 rooted occurrences; an independent implementation
   regenerates them and verifies that one usable coordinate contact from
   an adaptively selected protected centre to an adaptively selected
   `Q`-rooted bag makes every composition
   terminal.  At order nine, two usable contacts eliminate every static
   survivor.  A corrected computer-assisted replay shows that, in 1,901 of the
   2,252 placements, each named centre admits some closing contact; in the
   remaining 351 exactly one centre does.  The former figures
   2,177 and 75 came from a helper which inadvertently added a hidden second
   contact.  The order-eleven proof and independently checked order-ten
   statement are unaffected.

   Matching selection can prescribe a literal neighbour of a protected
   centre, but does not force its rooted-bag location.  The exact
   [rooted-suffix diagnostic](active/experiments/dominated_singleton_exact_eight_kernel_absorption/README.md#a-swallowed-matching-mate-exact-rooted-suffix-transfer)
   shows that this is not repaired by ordinary bag minimisation: faithful
   two-owner suffix transfer leaves `256`, `1022`, and `256` placements for
   the three graphs on `Q`.  The proposed
   **operation-labelled contact-or-split proof mechanism** has now failed
   a decisive test.  In `H-w`, failure of a six-arm fan from the
   selected mate to `Q` does produce an exact order-seven separation carrying
   the original operation and colouring.  When the fan exists, however, its
   paths and the independently contracted rooted model have incompatible
   quantifiers: distinct literal ends need not own distinct branch-set
   contacts or co-connected transferable suffixes.  An exact target-free
   quotient survives even when the mate has six direct `Q` contacts, and
   the explicit three-arm transfer screen has survivors.  Marked-edge
   terminal contraction also supplies only a contact already covered by the
   baseline rooted absorption.

   This is a recorded route nonclosure, not a counterexample to the desired
   host theorem.  It shows that the requested theorem cannot be obtained
   from five-connectivity, fan incidence and static rooted ownership alone.
   The protected-centre fan-to-root line is therefore frozen and is not
   being extended by more finite kernel cases.  The resumed campaign instead
   uses the remote-edge interface (R0).  The parallel nonsingleton
   obligation remains operation-sensitive transfer across at most two
   model-owning appendages.

   The separately audited
   [anchored-compression barrier](barriers/hc7_k7minus_anchored_coordinate_compression_barrier.md)
   remains the sharp warning against a generic local theorem.  Its
   singleton response has unbounded boundary even under stronger
   connectivity and degree assumptions, but the construction contains a
   literal `K_7`.  The new theorem must therefore spend the exact model,
   the second operation and `K_7^-`-minor exclusion, not merely the size of
   the response side.

In the seven-connected exact-model row, the new audited
[linear-forest cycle-or-separation theorem](results/hc7_k7minus_linear_forest_cycle_or_exact7_response.md)
supersedes the former two-cycle target.  A clean portal edge together with
the six original coordinates is a seven-edge componentwise-induced linear
forest.  If `G` is eight-connected, Haggkvist--Thomassen puts it on one
cycle.  Otherwise a seven-cut localises the complete `127`-signature cube:
one shore carries at least a two-coordinate punctured subcube, opposite
shore partition languages are disjoint, and the original fixed exact
`K_7^\vee` model survives.  Thus the exact alternative is now

\[
 \text{one portal-compatible cycle}
 \quad\hbox{or}\quad
 \text{an operation-labelled order-seven separation}.          \tag{R2}
\]

This does not assert the unresolved Lovasz--Woodall one-cycle conclusion;
it spends critical colourability at precisely the missing unit of
connectivity.  The returned exact-seven interface, rather than two-cycle
merging, is the remaining branch.

This is genuine progress inside both global cases: the entire
bounded-feedback alternative is impossible, and the eight-coordinate row
now has a model-anchored terminal normal form rather than an arbitrary
response separator.  Its hardest dominated singleton is reduced further to
a common kernel on seven boundary roots and two literal exceptional centres,
with at most one nonterminal.  It does not close Conjecture 21.  The exact
unresolved residues are a genuinely new operation-sensitive contact/model
exchange (not the frozen fan-to-root mechanism) or appendage transfer in the
eight-coordinate host, the induced-path triple split, the deferred matching
shared-pivot/model exchange, and the two-cycle exact-model composition.

#### Secondary centre-labelled route

Fix five independent degree-eight centres `Z`, and put `F=G-Z`.  The
audited
[five-centre two-cut reduction](results/hc7_k7minus_five_centre_two_cut_reduction.md)
now handles an arbitrary two-cut `{p,q}` of `F` without assuming a
support-five normal form.  The boundary `S=Z dotcup {p,q}` has exactly two
full complementary components, `pq` is absent, and a centre--pole boundary
edge is present.  The two closed shores have opposite singleton responses:
after orientation, `C` accepts only `p=q` and `D` only `p!=q`.  Moreover,

\[
 \chi(G[C])\ge4,\quad \chi(G[D])\ge5,\quad
 \mu_S(C)=1,\quad |C|\ge8,
 \quad e(C)+e(C,S)\le6|C|+1.
\]

The equality shore is rooted-`(2,5)`-infeasible and contains four
colour-distinguished `p`--`q` paths; the opposite shore contains a
bichromatic `p`--`q` path.  The order-five row is terminal: minimum degree
forces `G[C]=K_5^-`, and the separately audited
[order-seven component theorem](results/hc7_k7minus_order_seven_k5minus_component_elimination.md)
constructs an explicit `K_7^-` minor.  The order-six row is also terminal:
the separately audited
[finite incidence theorem](results/hc7_k7minus_order_six_equality_shore_elimination.md)
reduces the row to ten complement orbits and uses independently checked
DRAT refutations to construct the required explicit model.  The separately
audited
[order-seven allocation theorem](results/hc7_k7minus_order_seven_equality_shore_elimination.md)
closes the next row by an exact 149-orbit incidence search and a cold full
rerun, again reconstructing seven explicit branch sets.  Components of
order at least eight remain open, but their unbounded structure is now much
sharper.  In the singleton-contact case, the audited
[six-arm completion criterion](active/hc7_k7minus_five_centre_singleton_six_arm_completion.md)
is terminal whenever the arm-contact graph contains a `K_5^-` minor; the
available density inequalities do not yet force that contact minor.  In the
no-singleton case, the minimal bad-root row of order three is eliminated,
the order-four row has an exact three-outcome reduction, and the order-five
row is forced into one all-rainbow colouring.  In that last row the equality
shore has order at least fifteen.  The `b=2` common-hole orbit has further
rooted-model and Kempe-component structure, but remains nonterminal.

There is also a complete quotient-level reduction for a different
completion: contract `D union Z` and add the absent edge `pq`.  The audited
[completion-model lift](active/hc7_k7minus_five_centre_completion_model_lift.md)
reduces it to five branch sets with bijective centre ownership and one
owner--owner nonedge.  On the distinct-response shore, the promoted
[universal rooted-minor theorem](results/hc7_k7minus_five_centre_universal_boundary_rooted_k4.md)
gives a rooted `K_4` on every four boundary vertices.  Combining that model
with the exact pole-incidence classification proves the audited
[unique-owner separator reduction](active/hc7_k7minus_five_centre_owner_nonedge_connector.md):
every unique-owner configuration gives either an explicit `K_7^-` minor or
a nonempty proper connected donor piece, with connected complement in its
model bag, whose open neighbourhood is an actual separator of order at
least seven.

The proposed boundary-first
[minimal-donor gate](active/hc7_k7minus_five_centre_minimal_donor_gate.md)
has now been run and is decisively nonterminal.  A fixed proper-minor
colouring yields a vertex-minimal one-extra-colour core inside the donor.
Either that core is the whole donor, or the geometry exposes a smaller
donor-eligible set.  In a comparison class closed under that replacement,
the smaller set has strictly larger open neighbourhood and need not retain
the trace; if the class is not closed, no lexicographic comparison is
available.  Thus fixed-trace descent runs against, rather than with, the
primary boundary-order minimisation.

There is an exact quantifier fork.  Restricting the comparison to donors
which retain the near-clique labels and chosen operation gives no proved
upper bound on the new separator, and above order seven the output need not
have two full shores.  Enlarging the comparison to all geometric model
donors bounds the minimum by eight: the minimum is seven, or the second
coordinate selects a degree-eight singleton.  The latter exposes an
exceptional neighbourhood but need not retain the labelled model and
operation data; its two
unmodified shore languages are separated by using at most five versus
exactly six boundary blocks.  At order seven, split boundaries glue, so the
survivor is a nonsplit full boundary.  Its core either fills the donor or
leads to the same boundary-inflation/trace-loss fork.  Existing audited
parity and separator-excess barriers show why
ordinary boundary operations and model geometry do not eliminate these
endpoints.

This is a route nonclosure, not a counterexample and not a closure of the
two-cut branch.  Repeating an unlabelled one-donor minimisation is frozen.

The proposed single-edge
[paired-donor gate](active/hc7_k7minus_five_centre_paired_donor_gate.md)
has now also been run.  One colouring of `G-e` gives two genuine donor
traces only when the donors contain the two ends of `e`.  The resulting
cross-edge aligns the traces literally, yields one fixed-boundary joint
list-critical core containing both ends, and gives the exact boundary law

\[
 |N(Y_1\cup Y_2)|=|T_1|+|T_2|-|T_1\cap T_2|
                   -|T_1\cap Y_2|-|T_2\cap Y_1|.
\]

A supplied compatible pair would therefore give an explicit `K_7^-`
minor or one joint response-bearing separator.  The unique-owner theorem
does not supply such a pair: its only simultaneous canonical sets lie in
one bag, with no guaranteed joining edge, common far bag, jointly connected
complement, or colouring normalized to the original `pq` response.
Moreover, joint lexicographic minimisation forces either a shore-filling
core, loss of a prescribed duty, or a new boundary vertex private to the
same old bag; it does not force inflation into overlap.

The separately verified
[paired-overlap barrier](barriers/hc7_k7minus_paired_donor_overlap_barrier.md)
shows this is a genuine local obstruction.  It has two order-seven rejected
traces under one edge deletion, overlap of order five, the forced cross-edge,
five retained contacts per smaller donor, simultaneous trace-losing
inflation to order eight, and a rejected joint trace, while an explicit
width-four tree decomposition excludes a `K_7^-` minor.  The graph is only
three-connected and four-chromatic, so it does not refute a full host-level
supply theorem; it rules out overlap minimisation as that theorem's engine.

Thus the one-donor and single-edge two-donor minimisation mechanisms are
both frozen.  The bounded
[two-edge response reduction](active/hc7_k7minus_five_centre_two_edge_response_reduction.md)
has now tested the only natural next operation.  For one colouring of a
two-edge deletion, two disjoint traces exist exactly when every
monochromatic deleted edge crosses between the two sets; three disjoint
traces are impossible.  In the five-centre equality completion, the three
nonempty contraction choices form an exact Boolean alternative: a
single-edge pole-response flip, a genuinely joint double flip after both
single contractions remain seven-chromatic, or three seven-chromatic
stable completions carrying `K_7^-` models with the prescribed co-bagging.
This operation retains the literal block `Z` and the distinct `p,q`
response, but the current structure supplies neither the required pair of
cross-edges nor a lift of every stable completion model through the
artificial pole edge.  The bounded test is therefore complete and
nonterminal; it is not a reason to pass to three donors or larger edge
sets.

The exact-seven backup reaches the same label-placement failure: the new
boundary need not contain the five centres or inherit the original
equality-response orientation.  The two-cut branch remains open.

The three-connected branch was opened through the audited
[global rotation reduction](results/hc7_k7minus_five_centre_rotation_reduction.md).
The literal common core `F` is nonplanar and exactly six-chromatic.  Every
six-colouring of `F` saturates at least one centre, while the restriction of
a colouring of `G-z_i` saturates exactly `z_i`.  These five singleton sets
are colour-permutation-invariant response data.

For every ordered pair of distinct centres, the four-centre theorem applies
on `F+z_i`; there are twenty such applications, in five fixed-root packets.
A web outcome either returns a two-cut of `F` immediately or gives an
order-three separation of `F` crossed by exactly the four non-omitted
centres.  Two anchor-compatible labelled separations uncross to either an
order-two/order-four pair, with all five centres crossing the two-cut, or an
order-three/order-three pair in which the two omitted labels split.  Without
compatible anchors, an original exact-cut component has order three or
four.

Within one fixed-root packet, either two shores use the same literal
extension vertex and colour, or the four cuts have the rigid form

\[
 N_G(C_i)=(Z-\{z_i\})\mathbin{\dot\cup}(X-\{x_i\}).
\]

The maximal packet is now eliminated from the three-connected branch.
At least two omitted centres lie in their own selected components; meeting
those two exact separations gives the literal cut

\[
 Q=Z\mathbin{\dot\cup}(X-\{x_i,x_j\}).
\]

Thus `X-\{x_i,x_j\}` is a two-cut of `F`.  On one returned closed shore,
the same literal colouring extends over the fixed root with either of the
two distinct colours of `x_i,x_j`.  This is extra common-colouring data,
although it is not automatically the standard `Z`-monochromatic response.

The return also supplies two coupled proper-minor operations.  Restoring the
root with those colours gives colourings of `G-rx_i` and `G-rx_j` which
agree literally on `G-r` and have opposite singleton signatures on the
common two-edge deletion.  If `x_ix_j` is absent, contraction of the induced
path `x_i r x_j` supplies the double signature; if it is present, that
signature is impossible.  With `theta` the common colouring of `F` and

\[
 L_z=[6]\setminus\theta(N_G(z))\qquad(z\in Z-\{r\}),
\]

one operation has the standard distinct boundary response exactly when

\[
 \{\theta(x_i),\theta(x_j)\}\cap
                  \bigcap_{z\ne r}L_z\ne\varnothing.  \tag{2}
\]

Thus (2) is the exact normalization condition for this rotation route.  It
is not forced by the five local palettes.  The separately audited
[five-row palette barrier](barriers/hc7_k7minus_five_rotation_palette_intersection_barrier.md)
has singleton saturation at each root while the four other centres have
missing-colour sets `\{0\},\{1\},\{2\},\{3\}` and use those same four
colours.  Both (2) and the common-partition fallback then fail for every
singleton pair.  This refutes only a palette-level inference, not a theorem
under the full host hypotheses.

The audited
[common five-edge response theorem](results/hc7_k7minus_five_centre_common_matching_reduction.md)
now bypasses that false inference.  For each centre `z`, contract an
independent three-leaf star and expand a six-colouring.  The remaining five
neighbours of `z` have five distinct singleton colours.  Hall's theorem
chooses distinct representatives `x_z`, so

\[
 M=\{zx_z:z\in Z\}
\]

is a matching.  On the one literal graph `H=G-M`, the proper six-colourings
have exactly the signatures

\[
 \{\{e\in M:c(e^-)=c(e^+)\}:c\in\operatorname{Col}_6(H)\}
                         =2^M-\{\varnothing\}.        \tag{3}
\]

Equivalently, every one of the 31 nonempty endpoint-equality patterns is
realized, and the empty pattern would six-colour `G`.  More strongly, for
every nonempty `J subseteq M`,

\[
 \chi(G-J)=\chi(G/J)=6,
 \qquad
 \varnothing\ne\operatorname{Sat}(\theta_J)
                 \subseteq\{z:zx_z\in J\}.          \tag{4}
\]

There are spanning `K_6` models both in `G-J` and, after lifting `G/J`, in
`G` with the contracted pairs co-bagged.  Each of the five singleton
coordinates also gives an actual separator of order at least seven carrying
its literal rejected boundary precolouring.

The connectivity of `H` gives an exhaustive new structural reduction.

1. If `kappa(H)=2`, every two-cut has exactly two complementary components,
   all five matching edges cross, and all 32 endpoint transversals are exact
   order-seven cuts with two full sides.  The same two vertices cut
   `F=G-Z`; every centre has one opposite-open neighbour and its other seven
   neighbours in the home closed shore.  Thus all five centres have
   simultaneous singleton contacts, at least three on one shore.
2. If `kappa(H)=3`, every three-cut has exactly two complementary components
   crossed by four or five matching edges.  Four crossings give 16 exact
   order-seven cuts.  Five give 32 proper order-eight cuts; each of the 30
   mixed endpoint choices either exposes an exact order-seven cut or has
   exactly two full order-eight sides.  The cut with any centres removed is
   a cut of `F`; in the branch `kappa(F)>=3` it is a literal three-cut of
   `F`.
3. If `kappa(H)>=4`, Norin--Totschnig's theorem supplies a spanning exact
   `K_7^vee` model.  The audited near-clique dichotomy gives `K_7^-` or an
   actual nested separator.  If its returned connected set meets `r`
   matching edges, it carries all `2^r-1` nonempty exterior-realized,
   interior-rejected signature traces.  Those traces may induce the same
   boundary partition.

The audited
[two-shore rooted-minor theorem](results/hc7_k7minus_five_centre_two_shore_rooted_k4.md)
gives the two-cut row a symmetric refinement.  Orient its shores
as `C` (equal pole response) and `D` (distinct pole response), and let `U`
index the selected neighbours which lie in `C`.  The `D`-shore contains a
rooted `K_4` on every prescribed four boundary vertices.  If `U` is
nonempty, the singleton-shift density bound and the rooted `K_4`
obstruction theorem give the same universal conclusion on `C`.  Composing
the two models leaves an exact `3`-by-`3` cross-shore allocation problem:
eight of nine cross pairs are needed, while fullness alone need not place a
contact in any prescribed pair.  If `U` is empty, all five selected
neighbours are singleton contacts on `D`, and the equality-shore rooted
model remains the first missing step.

The audited
[signed four-crossing theorem](results/hc7_k7minus_four_crossing_signed_boolean_reduction.md)
gives a further unbounded reduction.  Its sixteen order-seven cuts are one
signed Boolean cube.  If
`R` is any nonempty subset of the four crossing matching edges, deleting
`R` leaves an exact separator of order `7-|R|` and

\[
 \kappa(G-R)=7-|R|,
 \qquad
 \Sigma_R(G-R)=2^R-\{\varnothing\}.                \tag{5}
\]

One family of seven disjoint paths identifies all four matching edges as
distinct literal linkage coordinates, independently of which shores
contain their centre ends.  For `1<=|R|<=3`, density and connectivity also
give a spanning `K_7^vee` model and hence either the target or an actual
nested model-bag separator carrying every signature trace whose deleted
edges it meets.  This closes the connectivity and linkage geometry of the
row, but the nested piece may miss every coordinate end, have boundary
larger than seven, or carry repeated rather than compatible boundary
partitions.

The audited
[omitted-coordinate theorem](results/hc7_k7minus_five_crossing_omitted_coordinate_linkage.md)
removes the per-coordinate linkage slack in the five-crossing row.  In the
no-descent case, fix a selected edge `e_i`.  Either `G-e_i`
has an exact order-seven response tied to `e_i`, or `G-e_i` is
seven-connected and has seven disjoint paths which simultaneously identify
the other four matching edges and the three vertices of the original
three-cut.  Restoring `e_i` gives eight disjoint paths between its ends and
a rooted minor

\[
             K_2\vee G[N(z_i)-\{x_i\}].             \tag{6}
\]

Consequently target exclusion forces `G[N(z_i)-{x_i}]` to have no
`K_5^-` minor.  If no selected edge gives the response outcome, all five
complete path systems exist.  They belong to the
five different graphs `G-e_i`; no theorem yet chooses them with compatible
intersections or a common boundary partition.  This simultaneous
composition, not local linkage, is the exact five-crossing residue.

The audited
[rotation-visibility theorem](results/hc7_k7minus_dense_branch_rotation_visibility.md)
makes the dense branch more visible than the selected matching alone
suggested.  For a centre `z`, let `K_z` be the intersection of all
independent triples in `N(z)`, and put

\[
 W=Z\cup\bigcup_{z\in Z}(N(z)-K_z).
\]

Every connected set meeting `W` carries a direct rejected trace from a
centre deletion or star contraction.  Two `P`-neighbours in `W` lying in
one universal bag of the exact `K_7^vee` model force the target or a nested
separator containing one of them.  Hence the only trace-invisible model
residue has at most one supported `P`-neighbour in each universal bag and
at least three `P`-neighbours outside `W`.  An exact order-seven returned
separator is already a labelled two-cut or four-centre three-separation of
`F`, according to how many centres its boundary contains, provided that the
selected piece itself avoids `Z`.

This centre-labelled common host remains a secondary laboratory.  It has
achieved the literal synchronization which the five-packet composition
sought, but it is not terminal.  Its exact remaining alternatives are:
eliminate the five
simultaneous singleton contacts through the `3`-by-`3` allocation, or handle
the all-five-on-`D` orientation; terminalize the signed four-coordinate
separator or compose the five omitted-coordinate path systems; or eliminate
the dense model whose four universal bags each contain at most one supported
portal.  Unbounded returned boundaries and repetition among their induced
partitions remain unsupported.  These rows may receive an exact labelled
separation from the seven-removable route.  The older rotation theorem
remains available for labelled three-cut geometry, while direct palette
intersection is frozen.

Any four-set `U subset Z` may also be used in the audited
[four-centre theorem](results/hc7_k7minus_four_centre_web_cut_lattice.md)
after putting `H=G-U`.  It shows that `H` is three-connected, nonplanar and
exactly six-chromatic.  For
every selected root in `U` and every fixed six-colouring after deleting that
root, it gives exactly one of the following outcomes:

1. a fixed-colouring-anchored `K_5` minor model avoiding the other three
   centres; or
2. an exact order-seven cut `U\dot\cup T`, with two full complementary
   components, a retained one-sided colouring trace, and nontriangular `T`.

If the host is eight-connected, only the rooted-model outcome occurs.  In the
seven-connected branch, fixed-anchor cuts returned by the second outcome form
an exact meet/join lattice.  If three cuts have all eight sign regions
nonempty, those regions already saturate all eight neighbours of every
centre; four cuts cannot have all sixteen sign regions nonempty.

Minimize the selected component `C` among cuts retaining the fixed trace.
The audited trace descent and generalized-wheel reduction then give three
facts: every vertex of `T` has at least two neighbours in `C`; no lower
tri-separation splits `C`; and `C` lies in one canonical leaf.  Moreover,
`H[T]` has an edge, while neither complementary component contains two
vertex-disjoint connected subgraphs that are each adjacent to every vertex
of `U\dot\cup T`.

The audited
[exact-boundary reduction](results/hc7_k7minus_four_centre_exact_u_bridge_reduction.md)
brings the critical colourings into this minimum side.  Each closed shore
has a six-colouring in which `U` is one exact colour class.  On `C`, either
a paired boundary trace forces three same-end bichromatic paths, or an
all-distinct trace forces one path for a paired trace accepted on the other
shore.  A connected support `Y` can be chosen so that every component `K`
of `C-Y` satisfies

\[
 |N_C(K)\cap Y|\ge
 \bigl(4-|N_G(K)\cap U|\bigr)
 +\bigl(3-|N_G(K)\cap T|\bigr),                       \tag{2}
\]

with a strict additional attachment when `K` sees all four centres.  No
component sees all of the centre block and the relevant singleton boundary
vertices, since that would reflect the accepted partition and six-colour
`G`.  All centre-free components can be absorbed into `Y`.  At most eight
components remain; at most two see all four centres, and at most two have
one attachment to `Y`.

In the paired case, the audited
[clean-fan theorem](results/hc7_k7minus_four_centre_paired_trace_fan.md)
replaces the arbitrary intersections of the three Kempe paths by one
`p`--`p'` path and two `p`--`q` paths with pairwise disjoint interiors.
Failure of this fan would itself give a smaller trace-admissible cut.

There is now also a global bound on the cuts returned by changing the
deleted centre.  The audited
[common-colouring and cut-family theorem](results/hc7_k7minus_common_colouring_centre_change.md)
constructs one six-colouring of `H` saturated at another centre.  Every
resulting exact four-centre cut is either the old cut or cuts off a proper
connected subset of `D`.  The inclusion-minimal such subsets form an
interaction graph `Gamma` with

\[
             \Delta(\Gamma)\le3,
             \qquad \alpha(\Gamma)\le2,
             \qquad |V(\Gamma)|\le4.                 \tag{3}
\]

The last inequality uses explicit `K_7^-` models, not enumeration.  If
equality holds, `Gamma` is one of `2K_2,P_4,C_4`.  Degree eight then forces
all simultaneous replacements of uniquely attached centres: the five exact
components yield at least eleven further exact order-seven cuts, all
distinct, and hence at least sixteen exact cuts in total.  For each exact
component, its simultaneous replacements form a Boolean sublattice of
minimum separations, and one six-colouring of the original closed side
induces one coherent boundary partition at each cut.  At least one such
sublattice contains a four-element square.

The audited
[Boolean replacement theorem](results/hc7_k7minus_boolean_replacement_edge_coupling.md)
identifies the graph structure behind that square.  All replacement edges
at one exact component lie on distinct paths of a common seven-path
linkage.  Proper-minor colourings realize every nonempty set of
endpoint-equalities and forbid the all-unequal set, with exact rules for
which closed shore each colouring fits.  Deleting one replacement edge
exposes an exact order-six separation in a six-connected, exactly
six-chromatic graph; its boundary has at most eleven edges and its two
component excesses sum to at least `sigma+12`, where
`sigma=|E(G)|-4|V(G)|`.  The endpoint edge is not
double-critical.  Deleting two coordinates exposes an exact order-five
separation in a five-connected, exactly six-chromatic graph with a spanning
`K_6` model.  If `Gamma` is `P_4` or `C_4`, the two replacement vertices in
any such square are nonadjacent; an edge between them would give an explicit
`K_7^-` model.

The audited
[cyclic four-region elimination](results/hc7_k7minus_cyclic_four_region_elimination.md)
now makes part of that interaction classification terminal.  A doubly
replaced component contains a rooted triangle on its two replacement
vertices and either remaining centre.  The other four exact components can
then be completed to a `K_4^-` model whenever `Gamma=C_4`, giving an
explicit `K_7^-` model.  Hence `C_4` is impossible.  If `Gamma=P_4`, the
same construction excludes every Boolean square based at `C` or at an
endpoint region.  The two internal regions therefore carry at least five
unique-centre incidences between them, so both carry an incidence and one
carries at least three.

The audited
[minimum-separator linkage theorem](results/hc7_k7minus_boolean_minimum_separator_linkage.md)
now removes the geometric anchoring ambiguity.  For every Boolean component
`P subset D`, one common seven-path family truncates to a centre-fixed
linkage between its replacement cut and the old minimum cut: each replaced
vertex is joined to its named centre by the literal replacement edge, each
unreplaced centre is fixed, and the remaining three paths biject the two
auxiliary boundaries.  Every coordinate path then continues from its named
centre wholly inside `C` and can be stopped on the clean-fan support.

The same theorem puts the one-coordinate colouring obstruction in normal
form.  On the six-boundary of `G-ux`, rejection at the cut containing `x`
already implies rejection at the cut containing `u`; the two rejections are
not independent.  Starting with any six-colouring of `G-ux`, recolouring
only `u` on the intact `P`-side aligns the two shores on the six-boundary
and forces one bichromatic lock in each shore.  The `P`-side lock begins
with the literal edge `ux`, so its reverse concatenates with the anchored
suffix to reach the clean fan through `u`.  The suffix in `C` remains
uncoloured.  Moreover, any one-missing-centre order-four separation which
actually enters and splits `C`, while retaining the fixed opposite anchor,
is terminal under exact uncrossing: it gives strict fixed-trace descent or
an exact transported one-missing-centre cut below the minimum separator.
The present opposite-region cuts are nested and do not split `C`.

The audited
[boundary-completion theorem](results/hc7_k7minus_four_centre_completed_side.md)
gives a complementary rooted-minor formulation.  The graph

\[
                         H[C\cup T]+\binom{T}{2}
\]

is four-connected.  For any two vertices `P subseteq T`, the actual graph
`G[C union U union P]` is internally six-connected; a
`(U union P)`-rooted `K_6^-` minor there, together with `D`, is an explicit
`K_7^-`-minor model.  In the generalized-wheel branch one may take `P` to
be the endpoints of the forced edge in `H[T]`.  The audited
[nine-vertex barrier](barriers/hc7_k7minus_internal_six_rooted_k6minus_barrier.md)
shows that internal six-connectivity, that edge and even a rooted `K_4` do
not suffice.

The square's linkage geometry and its local one-edge language are therefore
settled.  The unresolved step is fixed-trace colour synchronization.  The
normalization above uses an arbitrary colouring of `G-ux`; it need not
induce the exact-`U` trace used to choose `C` and construct the clean fan.
The scoped
[odd-wheel barrier](barriers/hc7_k7minus_local_coordinate_synchronization_barrier.md)
realizes the exact lower cut, adjacent lifted cuts, common lower partition,
endpoint lock and literal linkage coordinate without realizing a common
partition on either lifted cut.  It is not a critical host and does not
refute a fixed-trace theorem, but it excludes a proof from those local data
alone.

A direct fixed-trace audit also changes the proposed next lemma.  Fixing the
selected colouring on the old `C`-shore turns deletion of `ux` into a list
change at `x` on `D`.  If that fixed trace is rejected, a vertex-minimal
list obstruction can avoid `x` entirely.  The coordinate then disappears
from its own obstruction, and any separator exposed by that kernel is nested
inside `D`, not inside the minimum side `C`.  No current theorem excludes
this branch.  Consequently the proposed one-coordinate transfer trichotomy
does not follow from the existing package; this is a route nonclosure, not a
counterexample under the full critical-host hypotheses.

The fifth independent centre has now produced a genuine unbounded reduction
in the two-cut branch.  Its exact remaining case is a response-oriented
component `C` of order at least eight satisfying the displayed bounds,
rooted infeasibility, and the four colour-distinguished critical-edge paths,
coupled to the opposite shore's bichromatic pole path.  Eliminating that
larger-shore case would close every two-cut of `F`.  The other exhaustive
branch is that `F` is three-connected.  It is now reduced to the twenty
labelled rooted-model/web applications above.  Anchor-compatible web pairs
return a two-cut unless their omitted labels split across a `3+3` corner;
the maximal fixed-root packet itself now returns an exact five-centre
two-cut and is impossible in the three-connected branch.  Hence each of the
five fixed-root packets has a rooted-model outcome or two web outcomes with
one common literal extension vertex and colour.  In the returned two-cut
case those two colours already give coupled one-edge operations; their exact
missing normalization is (2).  The palette barrier shows that (2) cannot be
forced from the five local colour rows alone.  The common matching theorem
above replaces that proposed palette composition by one literal host
carrying the entire punctured signature cube.  The rotation theorem remains
useful for labelled three-cut geometry, but its palette-intersection route
is frozen.  The four-centre square-level fixed-trace kernel problem remains
a conditional laboratory rather than the immediate global target.

## Sufficient but non-primary extremal route

### A smallest `4n-2` enemy

Assume the `4n-2` theorem false, choose a counterexample `G` first with
minimum order and then with minimum size, and put

\[
q(G)=|E(G)|-(4|V(G)|-2).
\]

Jakobsen's audited extremal input rules out `|V(G)|<=20`: at those orders the
`4n-2` threshold reaches `9n/2-12`, while seven-connectivity excludes all
cockade exceptions.  Thus any enemy has at least 21 vertices; the only
possible first rows are `(n,m)=(21,82),(22,86)` and, at order 23,
`m\in\{90,91\}`.

A recorded, separately checked preliminary falsification screen found no
enemy among complete multipartite graphs, ordinary clique sums, the standard
cockades, or universal planar apex joins.  This is not an exhaustive or
separately promoted theorem.

The following computation-free reductions have written proofs and separate
GREEN internal audits.

- Every order-seven cut in a seven-connected `K_7^-`-minor-free graph has
  at most three complementary components.  With three components its
  boundary graph is subcubic.
- The minimum enemy has a degree-seven vertex `v`.  Some edge `vs` satisfies
  \[
  |N(v)\cap N(s)|\le3,
  \qquad q(G/vs)\ge q(G).
  \]
  The contraction cannot remain seven-connected.  Its failure pulls back
  to an exact order-seven cut containing `v,s`, with at most three
  complementary components.
- The contracted graph is nevertheless six-connected.  A new audited
  arbitrary-six-cut localisation shows that every order-six cut in it has
  exactly two or three boundary-full components.  At the `4n-2` threshold,
  the two-component boundary has at most eleven edges and total component
  excess at least `q+11`; the three-component boundary is subcubic with at
  most eight edges and total component excess at least `q+14`.
- If `G-N[v]` has two components, every incident contraction is
  density-preserving.  Yuan's fragment theorem then yields a connected
  fragment with a single surviving root and two nested exact seven-cuts.
  This is the precise root-swap residue; it is not a closure.
- If `q(G)>0`, then `G` is minimally seven-connected.  More than half its
  vertices have degree seven.  If `L` is the set of degree-seven vertices
  and `F=G-L`, then `F` is a forest and
  \[
  3(|L|-|F|)=c(F)+|E(G[L])|+q(G)-2,
  \qquad |L|\ge|F|+2.
  \]
  At least `ceil(|L|/2)` distinct density-preserving noncontractible edges
  cover `L`, each lying in an exact order-seven cut.  They include either
  a safe edge inside `L` or a safe two-edge star with two leaves in `L`.
- More generally, deleting any essential edge of an edge-minimal
  seven-connected target-free graph gives a six-connected graph with an
  exact six-separation into two boundary-full shores.  The deleted edge is
  the sole cross-edge.  The boundary is `K_5^-`-minor-free, every closed
  shore is internally rooted-connected, and the shore contraction surplus
  is known exactly.
- If such a six-boundary contains a literal `K_4` on `Z`, with remaining
  vertices `r,s`, then the new audited reserve inequality gives
  \[
  d_G(r)+d_G(s)\ge15+q(G)+\mathbf1_{rs\in E(G)}.
  \]
  In particular, in the `4n-2` range the two complementary boundary
  vertices cannot both have degree seven.
- In a strict-surplus minimum enemy there are at least thirteen
  degree-seven vertices and at most five lie in the unique possible literal
  `K_5`.  For each of the other at least eight vertices `x`, and every
  `y in N(x)`, the canonical set `T_y=N(x)-{y}` is a `K_4`-free
  six-boundary with at most ten edges.  Its connected high shore has excess
  at least `9+q(G)`, while `G-x` is internally six-connected at `T_y` and
  has exact density `4|V(G-x)|-5+q(G)`.  Norin--Totschnig already supplies
  a spanning `K_6` model there, but target exclusion forces every such
  model to meet `T_y` in at most four branch sets.
- The static model-splitting step is now proved.  For each fixed `x`, every
  spanning `K_6` model in `G-x` has a multiply rooted branch set containing
  a strict connected separator shore
  \[
  C\subsetneq B_y,\qquad C\cap N(x)=\{y\},
  \]
  whose complement in that branch set is connected and whose neighbourhood
  has order at least seven.  Writing `k=|N(C)|` and
  `eta=e(C)+e(C,N(C))-4|C|`, either `eta>q+k-4`, or a non-singleton `C`
  contracts to a proper minor still meeting the `4n-2` threshold.  Failure
  of seven-connectivity in that minor returns a labelled cut certificate
  through `C`.

These results replace the informal instruction to “place six surplus
edges”.  The positive-surplus obstruction now supplies at least fifty-six
canonical rooted six-boundary instances and converts every spanning-model
contact concentration at a fixed `x` into a strict same-host separator
shore with exact density accounting.

### Current density-route laboratory

The proposed canonical vertexwise `K_4`-reserve aggregation has now been
decisively assessed.  It is directly visible only at degree-seven vertices
inside the unique possible literal `K_5`, hence at no more than five
vertices; every strict-surplus enemy has at least eight degree-seven
vertices outside that stratum.  This closes that direct mechanism, not
every possible indirect use of the reserve inequality.

The safe-contraction quotient now supplies a second, potentially shorter
direct laboratory.  The full claim that every six-connected graph at the
`4n-2` threshold contains `K_7^-` is still open.  A proposed proof was
rejected because boundary fullness gives a lower bound on exterior degree,
not the upper bound needed to infer minimum degree inside the six-vertex
separator; its finite checker assumed those unsupported internal-degree
bounds.  This is a recorded route nonclosure, not a counterexample to the
six-connected statement.  What survives is the audited localisation above.
The efficient order is to close the subcubic three-component row first and
then attack the two-component high-excess row by a synchronised rooted-minor
or density-preserving shore argument.

The existing positive-surplus attack remains terminalisation of the strict
labelled separator shore.  There are three exact cases: a high shore which
need not inherit the canonical six-boundary hypotheses; a singleton `{y}`
for which
`d_G(y)=7` is not known; and a non-singleton eligible shore whose
density-preserving contraction loses seven-connectivity.  In the last case
an exact local separator supplies one order-seven cut, but it may be nested
with the existing cuts; otherwise a label-preserving rooted linkage theorem
is still needed.  Pair deletion and two-root transfers remain secondary.

The E5 and density attacks still meet at the same rooted obstruction, but
E5-specific boundary enumeration is frozen unless it proves an unbounded
theorem transferable to Conjecture 21 or finds a genuine E5 counterexample.

The direct positive-surplus attack uses Mader's generalised atoms.  It
reduces every nonsingleton atom to an edge, a three-vertex path, or a
triangle behind an exact seven-cut; one complete four-distinct-miss path
case is eliminated by a separately checked finite boundary lemma.  This
does not reach the exact-surplus layer.

The auxiliary five-connected statement

\[
 \kappa(G)\ge5,\qquad |E(G)|\ge4|V(G)|-7
 \quad\Longrightarrow\quad K_7^-\preccurlyeq G
\]

would imply the `4n-2` theorem and hence Conjecture 21.  A minimum auxiliary
enemy is now proved to have exact density `4n-7`, connectivity exactly five,
and an actual
five-cut with two or three boundary-full components.  Dense, four-component,
all seven-edge, sparse three-component, and several complete two-component
families are eliminated.  This is a substantial reduction, not a proof of
the auxiliary statement.

The common next theorem is a five-root reserve-or-descent lemma: a dense,
internally five-connected lobe with five prescribed boundary roots must
contain a `K_6` model with five distinct root bags and a root-free sixth
bag, or return a strictly smaller five-cut component which retains the
required high excess.  The full chain and exact surviving rows are in the
[auxiliary technical frontier](active/hc7_k7minus_e5_frontier.md).

The exact three-component branch with two singleton lobes is now much
sharper.  Contracting each singleton-to-boundary edge gives five rooted
three-cuts in the dense shore.  If no cut yields a strict high-excess
descent, their small sides contain only one or two roots.  Exact uncrossing
and Yuan's fragment theorem eliminate every boundary graph except
`P_3` disjoint union `K_2`; at least three of its four degree-one roots
then have degree five in the original graph.  Their two-vertex neighbour
sets in the dense component have distinct representatives, the component
has order at least eight, and each resulting leaf--neighbour edge lies in
another exact five-cut.  Deleting a degree-five leaf leaves an internally
four-connected four-root graph of exact size `4|V|-8`.  Published rooted
minor bounds supply separately a rooted `K_4` and a two-helper rooted model;
the helper containing the deleted leaf must also meet one of its two dense
neighbours.  A published linkage theorem also gives disjoint connected
carriers for every three--two split of the boundary roots.

Those supplies do not yet share one branch-set system.  The exact repair is
an anchored four-root `K_5`-or-descent theorem: for some leaf `t` and dense
neighbour `p`, the graph after deleting `t` must contain four pairwise
adjacent boundary-root bags and a disjoint `p`-bag adjacent to all four, or
uncross to a component of order below `|A|` retaining excess at least four.
The first outcome gives an explicit `K_7^-` model with the two singleton
lobes.  Further leaf-cut quotients do not close the gap: their fully
contracted seven-vertex form has at most eighteen edges, so target-freeness
is automatic.  One crossing orientation is now eliminated, however.  If
the low side is the singleton dense neighbour `q_t` and the further cut
contains four roots, replacing `t` by the other dense neighbour `p` gives
the five-cut

```text
(S-{t}) union {p}.
```

Its component `{x,y,t,q_t}` has excess one, so the universal five-cut
lemma forces excess at least four in a component strictly inside
`A-{p,q_t}`.  This contradicts the minimum choice of `A`.  The surviving
`q_t`-singleton rows therefore have at most three roots in the further cut
and natural boundary orders six, seven or eight.

The first of these rows, `s=3`, is now reduced exactly.  In the natural
six-boundary graph `F` one has `|E(F)|=4|V(F)|-8`.  An audited atomic
reduction shows that target-freeness leaves either a low component `{p}`
or `{p,b}` behind a rooted three-separation, or a unique excess-two helper
edge `{b,c}` behind a rooted four-separation.  Contracting the density-safe
edge `bq_t` in the latter case forces the companion five-cut

```text
{b,c,q_t,x,y}.
```

Its low side is exactly the `K_2` component of the original boundary and
has excess two.  The opposite side has the same order as the selected dense
lobe.  Under the current boundary-complement selection, this companion
pair ties the original value of `Phi` but has one other component rather
than two, eliminating the entire four-separator branch.  This replays the
earlier maximum-excess proof under the selection used below.

The two-vertex rooted three-separator atom is now eliminated as a distinct
outcome.  In its excess-one form, the degree-five vertex `p` defines a new
exact five-cut with singleton low side.  In its excess-two form, contracting
`bq_t` and applying the rooted six-bag supply in the returned high shore
gives an explicit `K_7^-` model.  Hence the sole obstruction in the `s=3`
singleton row is

```text
N_G(p)=T union {t,q_t},             |T|=3,
|E(F-p)|=4|V(F-p)|-7.
```

Contracting `pt` alone gives a four-connected graph with at least
`4|V|-6` edges, but its order-four cut is merely the image of the already
known cut `N(q_t)`.  Contracting the whole triangle `{p,t,q_t}` is stronger:
it loses at most six edges and gives a proper graph `J` with

```text
kappa(J)=4,                        |E(J)|>=4|V(J)|-5.
```

Every four-cut of `J` contains the contracted vertex and lifts to a new
order-six cut in `G`; every complementary component meets its three other
vertices and the triangle in aggregate.  Norin--Totschnig's density theorem
also supplies an unrooted `K_7^vee` model in `J`.  The exact remaining
cut structure is stronger: every component meets at least two triangle
vertices, and a triangle-missing component is either of order at most two
or has order `|A|` with one singleton opposite it.  A new global
boundary-complement potential preserves the companion- and edge-atom
reductions and eliminates every high triangle-missing component.  The
apparently neutral `t`-reorientation instead exposes a five-cut with a
strictly smaller high-excess component.

Consequently every lifted cut has at most three components and contains a
component adjacent to all six cut vertices.  For any other component, an
edge from a shared triangle vertex into this six-full component has at most
three common neighbours.  Contracting it is `E5`-density-safe, produces a
four-connected but not five-connected graph, and returns another exact
five-cut on lifting.  Exact order accounting and the global potential now
classify every returned cut: it has one singleton side with neighbourhood
exactly the cut and one high-excess side of order `|A|+1`.  All possible
order-`|A|` high sides are excluded by the degree-five triangle count and
the already eliminated nonadjacent-`t` reorientation.  Moreover every
non-six-full component has order at most two and supplies the companion
five-cut obtained by deleting its unique missed triangle vertex from the
six-cut; such a component necessarily exists in the three-component case.
The returned singleton now supports a second density-safe contraction.
If contracting it to the common anchor drops four-connectivity, an adjacent
returned singleton gives an exact labelled `K_2` kernel behind a six-set.
If four-connectivity survives and a nontrivial four-cut has a side missing
one original contraction endpoint, exact potential accounting instead gives
a labelled `P_3` or `K_3` kernel.  A promoted, independently checked finite
screen gives sharp boundary thresholds for all six five-full and six-full
kernel cases.  Together with the exact excess identities, it eliminates
every kernel configuration whose opposite shore is one connected component
missing a boundary root.  In a split shore, every non-six-full component is
now a full singleton or full edge of order at most two.

The subsequent six-boundary localisation sharpens, but does not close, this
kernel reduction.  Aggregate missed-root mass is at most two, every kernel
shore has a six-full component, and every multiple-six-full `P_3,K_3` shore
is eliminated.  The remaining kernel cases are one unbounded six-full
component, a self-similar singleton exterior, the `K_2`
one-six-full/full-edge equality, and the `K_2` two-six-full family with at
most seven boundary edges.  Before the kernel construction, the anchored
singleton quotient may repeat, or both original endpoints may meet both
sides of every eligible separation; the latter six-boundary has at most
eleven edges, with a `K_4` core only at equality.  Computation-free
eight-vertex barriers show that neither contracted contacts nor even the
five-connected local pattern suffices without density.  None of these
statements proves `(E5)`.

The decisive gate also gives an audited protected peel for an internally
four-connected rooted pair on the exact `4|V|-10` line with no rooted
`K^*_{4,2}` model.  The peel preserves any specified labels and strictly
decreases order while retaining equality.  It does not yet reduce an E5
host: reinserting the smaller pair need not preserve the host's
five-connectivity or external incidences.  The proposed four-root `K_6`
placement theorem and terminal equality classification remain conjectural.

An accepted result must prove at least one of:

1. terminalisation of the strict labelled separator shore, eliminating
   `q(G)>0`;
2. one density-preserving degree-seven edge is seven-contractible, or its
   exact seven-cut gives an explicit `K_7^-` model, in the equality layer;
3. one canonical or essential-edge shore contracts to a smaller
   seven-connected graph still at the `4n-2` threshold; or
4. the five-root reserve-or-descent target holds, or its anchored
   four-root specialisation closes the exact E5 two-singleton branch.

These remain valid exits for the conditional density route, but none is the
immediate campaign while the critical-host route is active.  E5-specific
case enumeration remains frozen.

The four exact nonclosures to overcome are:

- **root swap:** a trace-one fragment can support nested exact seven-cuts
  without being a singleton;
- **labelled-separator terminalisation:** the spanning-model split now
  returns a strict connected separator shore with exact density accounting.
  A high shore need not re-enter the canonical setting; a singleton shore
  need not have degree seven; and an eligible contraction failure returns a
  possibly nested exact cut or a still-unplaced rooted linkage.
- **safe-star uncrossing:** the positive-surplus count forces a safe edge
  inside the degree-seven set or a safe two-edge star, but their exact
  seven-cut certificates may coincide or nest without a smaller safe shore.
- **rooted reserve:** ordinary two--three linkage is sharp at lobe excess
  one, while an unrooted `K_6` model may consume every useful residual
  vertex.  Bare internal five-connectivity and excess four do not force the
  labelled reserve, and Wollan's small-neighbourhood theorem cannot be used
  at coefficient four because its `K_5` specialisation requires coefficient
  at least five.  In the exact two-singleton branch, fragment uncrossing
  and Hall's theorem give distinct leaf--neighbour pairs, and every
  three--two boundary split has disjoint carriers, but neither fact
  synchronises a rooted clique model.  Contracting both sides of the new
  leaf cuts erases the root traces and makes target-freeness vacuous.  The
  former five-boundary crossing row now descends strictly.  In the `s=3`
  row, a companion cut eliminates the internally four-connected atom and a
  second argument reduces the two-vertex three-separator atom to the
  singleton case.  Its safe `pt` contraction returns the old four-cut, but
  contracting the full singleton triangle gives a denser four-connected
  quotient and a genuinely new lifted six-separation.  Its components have
  two-of-three triangle contact.  A boundary-complement potential and one
  further exact five-cut eliminate all high-misser patterns; four
  complementary components are also impossible.  Thus a lifted cut has
  two or three components and one is six-full.  Density-safe contractions
  from the triangle into that component return a new family of exact
  five-cuts.  A second contraction from the returned singleton produces the
  labelled `K_2`, `P_3`, or `K_3` six-boundary kernels whenever connectivity
  drops or a nontrivial cut has an endpoint-missing side.  Exact missed-root
  mass is now at most two, so every kernel shore contains a six-full
  component.  A separately implemented exhaustive screen of 145,034 finite
  hosts, combined with a host-level portal-splitting argument, eliminates
  every multiple-six-full `P_3,K_3` shore.  The sole multi-six-full kernel
  survivor is `K_2` with two six-full components and at most seven boundary
  edges.  Another exact `K_2` family has one six-full component and one full
  edge missing the degree-five endpoint.  The both-endpoints branch now has
  boundary size at most eleven edges, with a literal `K_4` core only at
  equality.

  The live repair is therefore to control one unbounded six-full component,
  the self-similar anchored quotient, the two exact `K_2` residual families,
  or a both-endpoints separation with at most eleven boundary edges.  In
  particular, the one-six-full-only `K_2,P_3,K_3` rows remain open; they must
  not be omitted from the endpoint.  The alternative low-side cases still
  require a near-universal edge-completion lemma preserving
  five-connectivity.  A smaller arbitrary side is not enough unless it
  retains the high-excess inequality.

Kawarabayashi's contractible-edge theorem for odd connectivity and
`K_4^-`-free graphs supplies a relevant proof architecture, but its
triangle-free safe edge is what forces large shores in the uncrossing.
Here a density-safe edge may have three common neighbours, so a singleton
or root-only shore survives.  Replacing that lost shore-size bound is the
current uncrossing problem.  Another boundary census, isolated graph-code
elimination, or noncritical static barrier is not an accepted principal
outcome.

## Durable critical-host context

The strengthened audited computation-free critical-host package now gives:

\[
n_7=0,
\qquad \delta(G)\ge8,
\qquad |E(G)|\ge4|V(G)|,
\qquad b=n_8\ge27+\sum_{i\ge10}(i-9)n_i.
\]

Here the host contains no literal `K_5`, and `b` counts its exceptional
degree-eight vertices.  The rooted-helper theorem eliminates every
degree-seven vertex; applying it at all five vertices of a hypothetical
literal `K_5` then contradicts the exact degree surplus.  Jakobsen's defect
inequality, sharpened by the audited three-triangle-edge contraction, supplies
the displayed lower bound on `n_8`.  These are necessary
conditions on a hypothetical counterexample, not yet a colouring theorem,
and they do not apply to an arbitrary enemy to the unconditional `4n-2`
target.

Every order-seven cut in that critical host has exactly two complementary
components.  The earlier capacity theorem restricts a possible
three-component boundary to colour classes of sizes `3,2,2`, and the
audited
[three-shore planar-extension theorem](results/hc7_k7minus_three_component_seven_cut_exclusion.md)
six-colours that configuration.

The audited
[four-centre rooted-web theorem](results/hc7_k7minus_four_centre_web_cut_lattice.md)
is the current computation-free reduction: it returns either a labelled
rooted model or a nontriangular exact-cut lattice while preserving the
proper-minor colouring trace needed for the next operation.
Its audited
[operation-coupled continuation](results/hc7_k7minus_four_centre_operation_cut_reduction.md)
reduces the web branch to a response-carrying strict cut or a deficient
five-limb packing, and gives the exact independent-boundary normal form in
the case where one component contains two disjoint connected subgraphs
adjacent to the whole boundary.

The exceptional-centre programme and the split-colouring `4n` quotient are
the two active proof architectures for Conjecture 21.  The universal `4n-2`
theorem remains a sufficient conditional route, and E5 remains a stronger
frozen laboratory.  Direct `HC_7` bridge
composition is also frozen: Conjecture 21 is the cleaner setting in which to
develop the missing branch-set transfer and separator-resolution machinery.

The eight-page computation-free DRAFT in
[`paper/k7minus-low-degree/`](paper/k7minus-low-degree/) contains the
linked-cliques theorem, rooted-helper closure and the full low-degree and
density critical-host package.  Its exact source revision has an adjacent
internal mathematical audit and a separate internal citation and novelty
review.  The former rooted-web manuscript is retained as a labelled
[historical draft](archive/manuscripts/k7minus-rooted-web-2026-08-09/).
These checks are not external peer review or a priority certificate;
independent specialist validation is still required before publication.
Manuscript preparation is separate from the active proof target.

## Trust boundary

- The direct-extremal and auxiliary reductions are written results with
  adjacent hash-pinned GREEN internal audits.  The saturated degree-seven
  quotient, the four-distinct-miss path theorem and the six-boundary
  quotient barrier have explicit finite computational trust boundaries;
  the remaining new reductions are computation-free.
- The promoted both-full exceptional-boundary reduction has been rerun and
  independently rechecked at its pinned revision: `2,076` boundaries reduce
  to `15` and then `7`.  A separate Rolek--Song matching augmentation closes
  none of those seven and is recorded only as a finite route nonclosure.  A
  previously quoted list of `197` one-full boundaries has no retained
  predicate, digest, verifier or audit and is not part of the proof spine.
- External inputs include Mader, Halin, Jakobsen, Jørgensen, Yuan, Schmidt,
  McKay--Radziszowski, Fabila-Monroy--Wood, Norin--Totschnig and
  Du--Li--Xie--Yu; exact statements and citations are recorded beside the
  results that use them.
- No robust `K_6`-model transversal theorem or two-root dominating-model
  augmentation theorem is claimed.  Both bounded attacks have been frozen
  as principal mechanisms.  The first loses common labels and connectivity
  after deleting its transversal; the second requires a rooted
  cycle-touching model whose failure is not known to give a six-cut.

## Navigation

- [`active/INDEX.md`](active/INDEX.md): concise live navigation.
- [`active/hc7_k7minus_seven_exceptional_frontier.md`](active/hc7_k7minus_seven_exceptional_frontier.md):
  four-centre rooted-web dichotomy and nontriangular exact-cut residue.
- [`active/hc7_k7minus_density_frontier.md`](active/hc7_k7minus_density_frontier.md):
  stronger conditional `4n-2` frontier and recorded nonclosures.
- [`active/hc7_k7minus_e5_frontier.md`](active/hc7_k7minus_e5_frontier.md):
  frozen auxiliary five-connected reduction and five-root reserve target.
- [`results/hc7_k7minus_seven_cut_three_component_bound.md`](results/hc7_k7minus_seven_cut_three_component_bound.md):
  at most three components behind a seven-cut.
- [`results/hc7_k7minus_degree7_safe_contraction.md`](results/hc7_k7minus_degree7_safe_contraction.md):
  density-preserving degree-seven contraction and root-swap residue.
- [`results/hc7_k7minus_strict_surplus_minimal_enemy.md`](results/hc7_k7minus_strict_surplus_minimal_enemy.md):
  Mader--Schmidt structure at positive surplus.
- [`results/hc7_k7minus_essential_edge_six_separation.md`](results/hc7_k7minus_essential_edge_six_separation.md):
  essential-edge separation and shore accounting.
- [`results/hc7_k7minus_strict_surplus_canonical_six_boundary.md`](results/hc7_k7minus_strict_surplus_canonical_six_boundary.md):
  reserve blindness and the canonical sparse six-boundary obstruction.
- [`results/hc7_k7minus_remote_removable_edge_operation_cube.md`](results/hc7_k7minus_remote_removable_edge_operation_cube.md):
  a remote seven-removable edge and bounded opposite-shore operation
  interface at every exceptional centre.
- [`results/hc7_k7minus_remote_interface_topological_reduction.md`](results/hc7_k7minus_remote_interface_topological_reduction.md):
  the four-row interface normal form, excluding connected order seven and
  preserving all fifteen signatures on the nonfull return.
- [`results/hc7_k7minus_linear_forest_cycle_or_exact7_response.md`](results/hc7_k7minus_linear_forest_cycle_or_exact7_response.md):
  the portal-compatible one-cycle or labelled minimum-separation theorem.
- [`results/hc7_k7minus_p3_owner_circuit_compression.md`](results/hc7_k7minus_p3_owner_circuit_compression.md):
  minimum path-bag ownership compresses the nonrepeated allocation residue
  to boundary order seven or eight.
- [`archive/`](archive/): superseded proof spines and the previous ledger.
