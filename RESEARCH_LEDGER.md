# Hadwiger `K_7` research ledger

**Last updated:** 10 August 2026
**Authoritative status:** `HC_7` is not proved here.  Neither is the
`K_7^-` six-colour conjecture.  Internal audits are not external peer
review.  Hadwiger's conjecture is known for `t<=6` and remains open for
every `t>=7`; `HC_7` is the first open case, not the only open case.

The previous live ledger is preserved at
[`archive/RESEARCH_LEDGER_2026-08-02.md`](archive/RESEARCH_LEDGER_2026-08-02.md).
This file is the sole authority for the present research frontier.

## Current frontier

### 1. Exhaustive global obligation

The sole active research target is Norin--Totschnig Conjecture 21.

> **`K_7^-` six-colour conjecture.** Every graph with no `K_7^-` minor is
> six-colourable.

This statement is open.  It is weaker than `HC_7`: proving that every
seven-chromatic graph contains `K_7^-` does not prove that it contains
`K_7`.

The formerly primary density statement

\[
 \kappa(G)\ge7,\qquad |E(G)|\ge4|V(G)|-2
 \quad\Longrightarrow\quad K_7^-\preccurlyeq G
\]

remains a sufficient open theorem, but it quantifies over arbitrary dense
seven-connected graphs and discards the proper-minor colouring responses of
a hypothetical counterexample.  It is therefore retained as a conditional
extremal route rather than the active primary target.

### 2. Principal conditional refinement: the critical host

Assume Conjecture 21 false and let `G` be minor-minimal subject to being
non-six-colourable and `K_7^-`-minor-free.  The audited computation-free
critical-host chain now gives

\[
 \kappa(G)\ge7,\qquad n_7=0,\qquad \delta(G)\ge8,
 \qquad |E(G)|\ge4|V(G)|,
\]

excludes every literal `K_5`, and gives

\[
 n_8\ge25+\sum_{i\ge10}(i-9)n_i.                     \tag{1}
\]

Every degree-eight vertex has a `K_4`-free neighbourhood.  Every order-seven
cut has exactly two complementary components.  Consequently the following
is a headline-equivalent finishing theorem, not a routine local lemma:

> **Exceptional-centre finishing target.** Every graph satisfying the
> critical-host hypotheses has at most 24 degree-eight vertices.

This would contradict (1) and prove Conjecture 21 directly.  The active
technical statement, proved inputs and exact surviving allocation problem
are recorded in the
[critical-host frontier](active/hc7_k7minus_seven_exceptional_frontier.md).

The audited
[independence-four elimination](results/hc7_k7minus_alpha4_regular_ramsey_elimination.md)
now closes one exhaustive branch.  There is no 25-vertex 8-regular graph
with independence number four and clique number at most four; the finite
part is certified by 40 checked DRAT refutations.  Applied to the critical
host, this rules out independence number four in the graph induced by its
degree-eight vertices.  Since `R(4,5)=25` and the host has no literal
`K_5`, every hypothetical counterexample therefore contains five
independent degree-eight centres.

### 3. Immediate structural laboratory

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

This does not close the two-cut branch.  The returned separator can have
order greater than seven, can miss four of the five centres, and retains no
known boundary-colouring response.  The original `pq` critical completion
supplies a colouring constraint on `S=Z dotcup {p,q}`; it does not supply an
opposite-shore proper operation realizing the same labelled partition on
the new literal separator.  Thus the exact remaining theorem is a
response-preserving donor alternative: the quotient absorption must give
the forbidden minor, return an exact separator `Z dotcup {r,s}` carrying
the equal/distinct response needed for strict descent, or produce one
identical labelled partition of the returned boundary from proper
operations supported on its two open shores.  The last outcome glues
directly and does not require the new boundary to equal the old one.

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
branch is that `F` is
three-connected; there the five rooted-model/web outcomes must still be
composed across the five choices of omitted centre.  The four-centre
square-level fixed-trace kernel problem remains a conditional laboratory,
not the immediate global target.  The accepted conclusion is a
six-colouring of `G`, an explicit `K_7^-` model, or strict descent preserving
one common trace and minimum-side anchor.

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
\qquad b=n_8\ge25+\sum_{i\ge10}(i-9)n_i.
\]

Here the host contains no literal `K_5`, and `b` counts its exceptional
degree-eight vertices.  The new rooted-helper theorem eliminates every
degree-seven vertex; applying it at all five vertices of a hypothetical
literal `K_5` then contradicts the exact degree surplus.  Jakobsen's defect
inequality supplies the displayed lower bound on `n_8`.  These are necessary
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

The exceptional-centre programme is now the active proof route to Conjecture
21.  The universal `4n-2` theorem remains a sufficient conditional route,
and E5 remains a stronger frozen laboratory.  Direct `HC_7` bridge
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
- [`archive/`](archive/): superseded proof spines and the previous ledger.
