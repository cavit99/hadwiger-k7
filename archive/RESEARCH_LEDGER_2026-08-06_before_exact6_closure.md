# Hadwiger `K_7` research ledger

**Last updated:** 6 August 2026
**Authoritative status:** `HC_7` is not proved here.  Neither is the
`K_7^-` six-colour conjecture.  Internal audits are not external peer
review.

The previous live ledger is preserved at
[`archive/RESEARCH_LEDGER_2026-08-02.md`](archive/RESEARCH_LEDGER_2026-08-02.md).
This file is the sole authority for the present research frontier.

## Current frontier

### 1. Exhaustive global obligation

The sole active research target is the following unconditional extremal
theorem.

> **`4n-2` extremal target.** Every seven-connected graph `G` with
> \[
> |E(G)|\ge4|V(G)|-2
> \]
> contains a `K_7^-` minor.

This statement is open.  It is exactly sufficient for Norin--Totschnig
Conjecture 21: the audited computation-free critical-host chain proves that
any minor-minimal non-six-colourable `K_7^-`-minor-free graph is
seven-connected and meets this density threshold.  Proving the target would
settle that conjecture, but would not prove `HC_7`.

The global six-edge difference from Norin and Totschnig's `4n-8` threshold
does not identify six edges near a chosen deficient branch set.  Surplus
localisation is therefore not being treated as a proved mechanism.

### 2. Principal conditional refinement: a smallest extremal enemy

Assume the target false, choose a counterexample `G` first with minimum
order and then with minimum size, and put

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

### 3. Immediate structural laboratory

The proposed canonical vertexwise `K_4`-reserve aggregation has now been
decisively assessed.  It is directly visible only at degree-seven vertices
inside the unique possible literal `K_5`, hence at no more than five
vertices; every strict-surplus enemy has at least eight degree-seven
vertices outside that stratum.  This closes that direct mechanism, not
every possible indirect use of the reserve inequality.

The immediate attack is now terminalisation of the strict labelled
separator shore.  There are three exact cases: a high shore which need not
inherit the canonical six-boundary hypotheses; a singleton `{y}` for which
`d_G(y)=7` is not known; and a non-singleton eligible shore whose
density-preserving contraction loses seven-connectivity.  In the last case
an exact local separator supplies one order-seven cut, but it may be nested
with the existing cuts; otherwise a label-preserving rooted linkage theorem
is still needed.  Pair deletion and two-root transfers remain secondary.

The E5 and direct attacks still meet at the same rooted obstruction, but
E5-specific boundary enumeration is frozen unless it proves an unbounded
theorem transferable to the primary target or finds a genuine E5
counterexample.

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

would imply the primary target.  A minimum auxiliary enemy is now proved
to have exact density `4n-7`, connectivity exactly five, and an actual
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

Outcome 1 is the immediate campaign.  Outcome 4 remains a valid auxiliary
route, but E5-specific case enumeration is frozen.

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

## Established context retained from the previous programme

The audited computation-free critical-host package remains valid:

\[
n_7\le4,
\qquad |E(G)|\ge4|V(G)|-2,
\qquad b\ge17+\sum_{i\ge10}(i-9)n_i,
\]

where `b` counts degree-eight vertices contained in no literal `K_5`.
If `n_7=4`, then `|V(G)|>=37` and the stronger exceptional-vertex bound is
`b>=32+tau`.  These are necessary conditions on a hypothetical
counterexample, not a colouring theorem.

Every order-seven cut in that critical host has exactly two complementary
components.  The earlier capacity theorem restricts a possible
three-component boundary to colour classes of sizes `3,2,2`, and the
audited
[three-shore planar-extension theorem](results/hc7_k7minus_three_component_seven_cut_exclusion.md)
six-colours that configuration.

The exceptional-centre and bounded-interface programmes remain available as
conditional refinements and sources of techniques.  They are frozen as
principal search directions while the unconditional `4n-2` target is
attacked.  Direct `HC_7` bridge composition is also frozen: Conjecture 21
is the cleaner setting in which to develop the same missing branch-set
transfer and separator-resolution machinery.

The concise computation-free manuscript in [`paper/k7minus-low-degree/`](paper/k7minus-low-degree/)
is preserved but is not the active task.  Its proofs still require normal
specialist validation before publication.

## Trust boundary

- The direct-extremal and auxiliary reductions are written results with
  adjacent hash-pinned GREEN internal audits.  The saturated degree-seven
  quotient, the four-distinct-miss path theorem and the six-boundary
  quotient barrier have explicit finite computational trust boundaries;
  the remaining new reductions are computation-free.
- External inputs include Mader, Halin, Jakobsen, Jørgensen, Yuan, Schmidt,
  Norin--Totschnig and Du--Li--Xie--Yu; exact statements and citations are
  recorded beside the results that use them.
- No robust `K_6`-model transversal theorem or two-root dominating-model
  augmentation theorem is claimed.  Both bounded attacks have been frozen
  as principal mechanisms.  The first loses common labels and connectivity
  after deleting its transversal; the second requires a rooted
  cycle-touching model whose failure is not known to give a six-cut.

## Navigation

- [`active/INDEX.md`](active/INDEX.md): concise live navigation.
- [`active/hc7_k7minus_density_frontier.md`](active/hc7_k7minus_density_frontier.md):
  exact technical frontier and recorded nonclosures.
- [`active/hc7_k7minus_e5_frontier.md`](active/hc7_k7minus_e5_frontier.md):
  auxiliary five-connected reduction and five-root reserve target.
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
