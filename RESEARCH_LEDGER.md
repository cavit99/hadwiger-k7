# Hadwiger `K_7` research ledger

**Last updated:** 4 September 2026
**Authoritative status:** `HC_7` is not proved here. Neither is the
`K_7^-` six-colour conjecture. Internal audits are not external peer
review. Hadwiger's conjecture is known for `t<=6` and remains open for every
`t>=7`; `HC_7` is the first open case, not the only open case.

Superseded ledgers are preserved at
[`archive/RESEARCH_LEDGER_2026-08-02.md`](archive/RESEARCH_LEDGER_2026-08-02.md),
[`archive/RESEARCH_LEDGER_2026-08-17.md`](archive/RESEARCH_LEDGER_2026-08-17.md),
and
[`archive/RESEARCH_LEDGER_2026-08-22.md`](archive/RESEARCH_LEDGER_2026-08-22.md).
This file is the sole authority for the present research frontier.

## Three-level frontier

1. **Exhaustive global obligation:** `HC_7` asks whether every
   seven-chromatic graph contains a `K_7` minor. It remains open.
2. **Principal conditional refinement:** Norin--Totschnig Conjecture 21 asks
   whether every `K_7^-`-minor-free graph is six-colourable. T44 is the sole
   active completion target because it would prove this refinement.
3. **Immediate structural laboratory:** the literal-core route is reduced to
   two exact residues.  In a target-free nonsingleton minimum blocker, a new
   literal-core construction shows that every bond splits at most two of the
   five non-atom supports.  Consequently the selected minimum support-full
   bond shore opposite the specified `p` is a plain path with two split
   endpoint supports and three sequential internal supports, without a
   `b`-incidence hypothesis.  A four-connected graph with
   the derived six-boundary system always has a three-support bond, so the
   entire four-connected nonsingleton case is eliminated.  Every survivor has
   connectivity exactly three, and every three-cut leaves exactly two
   components, each meeting the sequential minimum path.  At such a cut,
   every support meets the cut at most once and the five supports have one of
   two exact incidence types.  A smallest component meeting three supports
   has a four-connected triangle-boundary torso.  Its exact bisection lemma
   is the remaining nonsingleton task.  For an adjacent singleton pair,
   every literal-shore split
   and every three-component contraction trace is now eliminated.  In the
   sole two-component core-concentrated profile, every rooted `K_5` has joint
   endpoint-contact rank at most three.  The one-defect two-helper split is
   target-producing; in the target-free profile its failure returns a marked
   proper connected side whose full neighbourhood is an actual separator.
   Eliminating that marked separator profile is the remaining singleton
   task.  The
   nonliteral labelled branch-model rotation obligation remains separate.
   **Induction qualification, 4 September:** closing the two local literal
   residues must also preserve the ambient hypothesis class, or prove
   completion with purely labelled hypotheses. Safety alone has not supplied
   that unbounded step; see the
   [technical frontier](active/hc7_k44_closure_frontier.md#44-the-hypothesis-class-needed-for-induction).

## Current frontier

The sole active completion target is the following open statement.

> **T44.** Every seven-connected graph containing a `K_{4,4}` minor contains
> a `K_7^-` minor.

Here and below, *target-free* means `K_7^-`-minor-free. T44 would prove
Norin--Totschnig Conjecture 21: a minor-minimal non-six-colourable
target-free graph is seven-connected, and Kawarabayashi--Toft prove that
every seven-chromatic graph has a `K_7` or a `K_{4,4}` minor. The first
alternative already contains the target and T44 would close the second. T44
would not by itself prove `HC_7`.

### Falsification checkpoint

The first computer-assisted finite pass found no counterexample through
order eleven. At order eleven, complementation reduces the census to 10,946
unlabelled subcubic graphs; 9,940 complements are seven-connected and all
have independently checked seven-bag `K_7^-` certificates. This is a
computer-assisted finite result, not an unbounded theorem.

A separate hostile screen of the weighted literal-core splitter formula
found no survivor at exterior order eight after the cubic-vertex reduction:
all 1,619 eligible three-connected graphs were UNSAT. Targeted small-atom
probes were also UNSAT on all 16 connected four-regular graphs of order nine
and on the 57 three-connected graphs among the 59 connected four-regular
graphs of order ten. Z3
5.1.0 is the decisive trust boundary and no independently checkable UNSAT
certificate is retained. The exact encoding, checker, counts and digests are
preserved in the [weighted-splitter
experiment](active/experiments/k44_literal_weighted_splitter/README.md).

A more local hostile screen attacks the remaining minimum-blocker
bisection directly.  Its complete labelled encoding is UNSAT through
blocker order six, and a separate fixed-host encoding is UNSAT on all 157
three-connected graph-atlas hosts of orders four through seven.  The latter
already uses only spanning connected bisections.  Z3 remains the decisive
UNSAT trust boundary and no independently checkable certificate is retained;
the exact formulas, host digests, output and independent finite-encoding
audit are preserved in the [minimum-blocker bisection
experiment](active/experiments/k44_literal_minimum_blocker_bisection/README.md).

The next hostile screen imposes the complete minimum-blocker hypotheses and
tests both the exact spanning-partition negation and a stronger anchored
negation.  Both are UNSAT on all 422 eligible minimum-degree-four hosts of
order eight, all 16 connected four-regular hosts of order nine, ten
four-connected planar hosts of order nine, and six targeted sharp-three-cut
join perturbations.  This is independently audited bounded evidence with Z3
as the decisive trust boundary, not an unbounded theorem.  The asserted host
counts and graph6 digests, exact encodings and solver-free witness checks are
preserved in the [spanning-split hostile
screen](active/experiments/k44_literal_spanning_split_search/README.md).

A separate written-unaudited family reduction treats seven-connected
full-attachment seven-sums

`G = S join (L disjoint-union R)`, with `|S|=7` and nonempty connected
`L,R`.

For two outside vertices, seven-connectivity makes `S` five-connected and
the audited double-cone theorem applies. For three outside vertices, it
makes `S` four-connected, hence of minimum degree at least four, and the
audited seven-vertex double-cone theorem applies. For four through seven
outside vertices, an exact search checks 105 edge-minimal representatives.
For larger outside order, connected subgraphs of the two shores reduce to
seven outside vertices. This closes the seven-connected members of that
specified family only; it does not cover arbitrary non-full seven-sums or
imply T44.

### Direct audited inputs

The current direct inputs are:

- the double-cone theorem, two-near-full-model-bridges lemma and exact-cut
  normal form for a vertex-minimal nonliteral model;
- the theorem that every exact seven-cut boundary in a seven-connected
  target-free host has minimum degree at most three;
- the literal-core exterior theorem: the exterior is connected and no set
  of at most two vertices separates two nonempty exterior sets; when it has
  at least four vertices, it is three-connected;
- the four-portal exterior-triangle completion theorem;
- the three-portal exterior-`K_4` dichotomy, with its tetrahedral exception
  excluded in the spanning case by global portal coverage;
- the singleton-atom and exact one-resource blocker theorem, which is the
  direct entrance from failure of every safe contraction to the singleton
  atom and its crossing-boundary normal form;
- the tight-boundary and minimum-blocker theorem: every connected tight
  exterior shore has an actual bipartite `3`-by-`4` seven-boundary, while a
  minimum nonsingleton crossing blocker is three-connected of minimum degree
  at least four, has all five non-atom resources multiply attached, and has
  the stated exact three-cut profiles;
- the three-support bond and three-cut reduction: every bond splitting three
  non-atom supports has an explicit literal-core `K_7^-` model; an abstract
  four-connected graph satisfying the five-support six-boundary system has
  such a bond; hence every target-free nonsingleton blocker has connectivity
  exactly three, the selected minimum support-full bond shore opposite the
  specified `p` is a sequential path, and every three-cut leaves exactly two
  components, each meeting that path;
- the two-component three-cut support normal form: each support meets the
  cut at most once; either two supports meet both components and the other
  three lie wholly in the components with a `1+2` distribution, or one
  support meets both components and two further supports occur on each side,
  with the stated common cut-vertex restriction; every choice of a pair in
  a whole support on each side and a cross-component pair in a bridge
  support is weakly linkable, while any small torso separation behind one
  component meets at least three incident supports; a smallest component
  meeting exactly three supports has a four-connected triangle-boundary
  torso with one or two whole supports;
- the contraction-trace theorem for an adjacent singleton pair: the edge lies
  in an exact seven-cut with two or three complementary components; the
  three-component case puts one literal shore and one exterior vertex on a
  subcubic boundary, while the two-component case is either a whole-shore
  split or has a rooted `K_5` with universal endpoint-contact bounds;
- the two-component shore-split elimination theorem: every unbalanced or
  balanced literal-shore split yields an explicit triangle universal to a
  four-bag `K_4^-`, hence a `3+12+5=20` contact model;
- the three-component trace elimination theorem: every distribution of the
  opposite literal shore across the three full components yields the same
  `3+12+5=20` conclusion after a uniform two-root allocation; and
- the core-concentrated joint-contact theorem: every rooted `K_5` has joint
  endpoint-contact rank at most three, order-three contact on one side
  contains the other side's contacts, and failure of the exact two-helper
  split in the target-free profile returns a proper connected set with an
  actual separator as its full neighbourhood.

These promoted results have adjacent hash-pinned GREEN internal audits.
Their deterministic finite components are registered in the research
verifier whitelist. The audits cover their exact stated scopes and do not
prove T44, Conjecture 21 or `HC_7`.

### Two open obligations

1. **Literal exact-residue completion.** Close both audited outcomes of a
   minimum crossing blocker.  For a nonsingleton blocker, prove the precise
   triangle-boundary torso bisection lemma: inside the selected
   four-connected minimum three-support torso, find a connected
   nonseparating set which meets every external support and splits every
   whole support.  The former triangle and claw block forms, the
   four-connected case, and both three-component profiles are closed; the
   plain-path/two-component residue survives.  For a singleton blocker,
   eliminate the entire
   core-concentrated profile.  The current theorem only returns a marked
   separator certificate: even order seven is not yet proved sufficient for
   a target or safe contraction, and no well-founded descent through larger
   boundaries is known. Closing both local residues would give a safe
   contraction in the stated ambient class. A purely labelled completion
   theorem or preservation of the full ambient class is additionally needed
   to iterate that contraction and conclude the literal theorem.
2. **Nonliteral model-trace rotation.** Use the exact seven-cut through an
   internal branch edge to construct a strictly smaller labelled
   `K_{4,4}` model or the target. Exact cuts alone do not provide
   laminarity, a peel side or preserved branch ownership.

The literal route now has the following audited unbounded reduction.  A
minimum nonsingleton crossing blocker `X` is three-connected with
`delta(G[X])>=4`; every one of its five non-atom boundary resources has at
least two neighbours in `X`, and

`|N_X(W)|+|{k in K:R_k meets W}|>=6`

for every nonempty proper connected `W`.  The former split-count threshold
of four when one helper misses `b` is not the true ambient threshold.  A new
six-row literal-core construction reallocates all seven boundary-rooted bags,
the two connected bond shores and the unused core vertex.  It gives twenty
quotient contacts whenever any three `K`-supports split, independently of
the `a,b` distribution.  Therefore every bond of a target-free blocker
splits at most two supports.

Choose the distinguished `p in R_a` and minimize a support-full bond side
`U` opposite `p`.  The earlier three-form block theorem now has
`2<=|M|<=s(U,V)<=2`, so all triangle and claw forms disappear: `X[U]` is an
induced path, exactly two supports split at its endpoints, and the other
three lie wholly on the path with positive pairwise edge-disjoint hulls.
Every path vertex meets the complementary side; the endpoints have at least
three such neighbours and internal vertices at least two.  Every subpath is
a bond and splits at most two supports.  More globally, every bipolar order
has five support intervals of depth at most two, with interval-intersection
graph a forest.

These path hulls also close the full four-connected case.  Their three
extreme pairs form a nontrivial acyclic parity triple.  The
Chen--Ding--Yu--Zang bond theorem either supplies a three-support bond or a
facial obstruction.  In the latter case the audited Euler inequality gives
an off-face support; replacing one pair gives a second acyclic triple which
cannot lie on a facial cycle sharing three vertices with the first.  Thus a
four-connected graph satisfying the five-support system has a three-support
bond, contrary to target-freeness.

Every nonsingleton survivor consequently has connectivity exactly three,
and every component behind every three-cut meets the minimum path.  Both
formerly possible three-component profiles are impossible.  In the
exceptional profile, one component bond splits the three nonexclusive
supports.  In the equality profile, choose two vertices from each of the
three component-exclusive supports.  A two-linkage from each pair to two
vertices of the cut produces disjoint connected sets separating all three
pairs; extending them to a spanning bond splits the three supports.

At every remaining two-component three-cut, each support meets the cut in at
most one vertex.  Either two supports meet both components and the other
three are wholly component-contained in a `1+2` distribution, or one support
meets both components and two further supports occur on each side.  In the
latter type at most one side-support on each side meets the cut, and any two
such cross-side contacts use the same cut vertex.

More strongly, choose a whole support in each component and a support which
meets both.  Every choice of one two-element pair in each whole support and
one cross-component pair in the bridge support is a nontrivial acyclic
parity instance.  A feasible parity bond would split three supports, so all
members of this full Cartesian family must be weakly linkable in the sense
of Chen--Ding--Yu--Zang.  In the torso on either component and the cut, every
separation of order at most three isolating a nonempty component-side set
has order exactly three and that set meets at least three incident supports.
The next theorem must exclude this simultaneous weak-linkability system;
one inconvenient fixed triple is not enough.

There is also a canonical local place to do so.  Choose, over all three-cut
components meeting exactly three supports, one of minimum order, and replace
the other component by a triangle on the cut.  The resulting torso is
four-connected.  Exactly one or two of its three incident supports lie
wholly in the selected component, and connected component-side sets retain
the six-boundary inequality.  The exact open lemma asks for a nonempty
connected set inside that component whose torso complement is connected,
which meets every support extending outside the component and splits every
whole support.  Such a set is precisely one shore of a global bond splitting
the three incident supports, and would close the nonsingleton branch.
The [stripped-torso barrier](barriers/hc7_k44_three_support_torso_bisection_barrier.md)
shows that four-connectivity and the local inequality alone do not force
this set: a `K_5` example has all local scores equal to six but no valid
bisection.  It proves only that at least one retained global input must enter.
Available inputs include the global at-most-two-split bond restriction,
complementary-support provenance, the two supports outside the torso, the
minimum path, and the distinguished `a,b` incidence.

The exact nonsingleton target is therefore the triangle-boundary torso
bisection lemma under the full global blocker hypotheses.  The verified
minimum-path transversal counterexample shows that a fixed choice of the
three path-internal supports need not admit a prescribed rooted bond, even
in a four-connected local model; that graph has other three-support bonds.
It refutes only that local selection step, not the new theorem or the
remaining torso bisection lemma.

The exact two-component incidences also do not suffice after contracting
both components.  A thirteen-vertex literal-core quotient with two bridge
supports, a `1+2` distribution of the other supports and both distinguished
roots on the three-support side has exact `K_7^-` contact optimum nineteen.
It fails support multiplicity, `q>=6` and the minimum-path normal form, so it
is only a barrier to quotient-only completion.  The live proof must use the
uncontracted structure forced by those three hypotheses.

For a singleton blocker `p`, the adjacent edge `ap` has an exact contraction
cut.  A three-component response has a subcubic boundary consisting of
`a,p`, one literal shore and one exterior vertex.  A two-component response
is either core-concentrated, giving a rooted `K_5` which each endpoint meets
in at most three bags, or splits the opposite literal shore.

The latter alternative is now eliminated completely.  In the unbalanced
case, the unique common neighbour gives a third connected bag beside the two
endpoint-derived bags; these three form a triangle and are universal to four
`S_0`-rooted bags completed to `K_4^-`.  In the balanced case, the audited
one-sidedness theorem and a two-resource allocation eliminate both
`R-F nonempty` and the final two-core-vertex component `R=F`.  Every case
again has `3+12+5=20` contacts.

The three-component response is also eliminated.  Select two
opposite-shore components and remove one core vertex from each.  The selected
component pieces miss at most one cut vertex, so the removed core vertices
repair their possible missed literal roots and complete four core bags to
`K_4^-`.  Distinct representatives from `a,p,x` make the three
component-derived bags a triangle.  This uniform construction covers the
`3+1+0`, `2+2+0`, and `2+1+1` shore distributions.

In the sole two-component core-concentrated response, the two separate
three-bag endpoint bounds sharpen to the joint inequality

`|C_a union C_p|<=3`

for every spanning `T`-rooted `K_5` model.  If one contact set has order
three it contains the other.  The exact two-helper construction closes as
soon as two disjoint connected endpoint-anchored sets in the remote
component have total rooted-bag defect at most one.  If no such split is
obtained, a spanning-tree split of the remote component—or, in the unique
common-neighbour case, of one rooted branch bag—returns a proper nonempty
connected set `Y` for which `N_G(Y)` is an actual separator.  The construction
retains the relevant two-part tree or rooted-branch-bag split, its endpoint
anchors, and a named rooted bag anticomplete to `Y`.  Thus `|N_G(Y)|>=7`;
equality makes every complementary component full to that boundary.

The exact remaining singleton target is to prove that no target-free graph
satisfies this core-concentrated profile.  Two plausible mechanisms are open:
an exact-seven marked-certificate theorem producing the target or a safe
contraction, and a descent/rerouting theorem for larger returned boundaries
with an explicitly decreasing complexity.  Equality alone is not presently
known to be terminal, and no such descent measure has been proved.  A verified
order-three local incidence profile shows that relative boundary inequalities,
fullness, the degree-seven counts and the joint contact bound alone do not
force the one-defect split.  It already has five proper tight sides.  Therefore
the next argument must use the marked separator data or reconfigure the rooted
model; bare contact counting cannot close the case.

The computation-free induction base remains exterior order at most six, and
all order-seven and newer finite screens are bounded evidence only.
The weighted splitter theorem, the literal T44 branch, T44, Conjecture 21,
and the nonliteral rotation obligation all remain open.

There is also a new audited critical-host corollary.  In a strongly
seven-contraction-critical target-free graph with a specified literal
`K_{4,4}` and exterior order at least seven, the exterior has a safe
three-contractible edge.  Failure would produce the audited singleton atom,
whose degree-seven bipartite `3`-by-`4` neighbourhood contradicts Dirac's
neighbourhood-independence inequality. The new audited
[preservation theorem](results/hc7_k44_safe_contraction_preservation.md)
adds that the core is induced and each core vertex has degree at least nine.
The first safe contraction is seven-connected; if the exterior originally
has at least eight vertices, a second safe edge exists and its contraction
is seven-connected too. Both quotients remain target-free and retain the
literal core. The proof excludes a degree-seven bipartite neighbourhood
after one original contraction using Dirac's inequality. It proves neither
a third safe edge nor an unbounded closed reduction class. Six-colourability
of the proper quotients still prevents reapplying criticality itself.

The separate [induction-scope finding](active/hc7_k44_closure_frontier.md#44-the-hypothesis-class-needed-for-induction)
corrects the implication previously claimed after closing both literal
residues. The small-atom theorem has purely labelled hypotheses, while its
later ambient refinements use seven-connectivity and target exclusion.
Their conditional completion statements cannot yet be reapplied after an
arbitrary labelled safe contraction. No proved atom statement is retracted;
the missing inference is the closure of the proposed induction class.

## Durable recent results outside the active spine

- **Written proof with two separate internal audits, 4 September 2026:**
  every bipartite graph with degree at most two on one specified side is
  contractible. The [proof](results/even_subdivision_contractibility.md),
  [cold audit](results/even_subdivision_contractibility_audit.md), and
  [separate proof and literature audit](results/even_subdivision_contractibility_literature_audit.md)
  extend the two-projection `K_{2,n}` argument to arbitrarily many graphic
  matroids with partially shared labels. Every label belongs to at most two
  projections, which verifies the simultaneous matroid union inequality.
  Consequently every replacement of the edges of an arbitrary loopless
  multigraph by paths of positive even length is contractible. This gives a
  family of unbounded treewidth and covers the even-path portion of
  Kündgen--Pelsmajer--Ramamurthi's bipartite-theta question. It does not cover
  the three-odd-path case or `K_{3,3}`, and does not advance a specific
  `HC_7` subcase. Targeted literature checks found no matching theorem;
  priority and significance comparable to Norin--Totschnig remain
  unestablished. The earlier audited proof and manuscript are preserved.
- Every complete bipartite graph `K_{2,n}` is contractible in the sense of
  graph schemes. The [computation-free proof](results/k2n_contractibility_via_matroid_packing.md)
  has an adjacent [hash-pinned GREEN internal audit](results/k2n_contractibility_via_matroid_packing_audit.md)
  and a separate [four-page manuscript DRAFT](paper/k2n-contractibility/main.pdf)
  ready for specialist review.
- The [five-root partial-routing theorem](results/llru_question61_via_km_property_star.md),
  with a [GREEN audit](results/llru_question61_via_km_property_star_audit.md)
  and a [second GREEN cold audit](results/llru_question61_via_km_property_star_second_cold_audit.md),
  answers Lafferty--Liu--Rolek--Yu Question 6.1 when the five roots lie in
  pairwise disjoint vertex sets and every nonadjacent root pair is linked
  within the union of its two sets. It lowers their stated
  eight-connectivity threshold from `k>=17` to `k>=11`, but does not close
  the remaining degree-eight connector problem.
- Every three-connected graph has a `K_4^-` minor rooted at any four
  prescribed distinct vertices, with the missing quotient edge unspecified.
  The [elementary unbounded proof](results/rooted_k4minus_four_roots.md) has
  a [GREEN internal audit](results/rooted_k4minus_four_roots_audit.md).
- The [degree-eight low-codegree and defect theorem](results/hc7_k7minus_sixconnected_degree_eight_low_codegree.md),
  with [two GREEN internal audits](results/hc7_k7minus_sixconnected_degree_eight_low_codegree_audit.md),
  combines one deterministic finite local lemma with an unbounded host
  reduction. It proves the defect ladder `D(G)>=20+kappa(G)` and the current
  critical-host bound `n_8>=27+tau`.
- The computation-free [three-component order-seven-cut exclusion](results/hc7_k7minus_three_component_seven_cut_exclusion.md)
  and its [GREEN audit](results/hc7_k7minus_three_component_seven_cut_exclusion_audit.md),
  combined with the separately audited [critical seven-cut capacity theorem](results/hc7_k7minus_critical_seven_cut_capacity.md),
  show that every seven-vertex cut in the critical host leaves exactly two
  components.
- The [critical literal-core safe-contraction
  corollary](results/hc7_k44_critical_safe_contraction.md), with its adjacent
  audit, combines the singleton-atom theorem with Dirac's neighbourhood
  inequality. Its [audited preservation refinement](results/hc7_k44_safe_contraction_preservation.md)
  gives two safe contractions preserving seven-connectivity when the
  exterior has order at least eight, without an unbounded induction.

The [selected-results map](results/README.md) is a non-authoritative reader
guide to these proofs and the direct proved inputs to T44.

## Manuscript status

The four-page [`K_{2,n}` DRAFT](paper/k2n-contractibility/main.pdf) is the
primary circulation candidate. It is computation-free, has a
[GREEN internal audit](paper/k2n-contractibility/main_audit.md) and is
independent of the Hadwiger programme.

The compact eight-page [low-degree DRAFT](paper/k7minus-low-degree/main.pdf)
is a frozen, computation-free snapshot with a [GREEN internal audit](paper/k7minus-low-degree/main_audit.md).
It proves the baseline `n_8>=25+tau`, not the later `27+tau` strengthening.
The former rooted-web manuscript is retained only as a clearly marked
[historical DRAFT](archive/manuscripts/k7minus-rooted-web-2026-08-09/main.pdf).
Neither manuscript proves Conjecture 21 or `HC_7`.

## Preserved frozen routes

The former exceptional-centre campaign remains a frozen critical-host
refinement. Its sound chain, including the audited low-codegree theorem
linked above, gives

`n_8 >= 27 + tau`, where `tau=sum_{i>=10}(i-9)n_i`.

Thus an upper bound `n_8<=26` in the hypothetical critical host would prove
Conjecture 21. Its first unresolved inference is the operation-sensitive
alignment of colouring responses with a fixed exact minor model. The remote
interface, induced-forest and fan/static-profile programmes are not parallel
active targets under the T44 pivot.

The six-connected `4n` theorem, the stronger `4n-2` density programme, E5
and direct `HC_7` bridge composition remain conditional or frozen routes.
Their priority can be reconsidered when a new argument offers a stronger
justified prospect; T44 need not first be falsified.

The [historical review through the former HEAD](archive/research_chronology_review_2026-09-04.md)
records the initial commit, fortnightly snapshots and intervening
retractions, including the off-main August exact-six closure. Across those
changes the repeated failure was preservation of a complete colouring
partition or rooted model in a class closed under the proposed reduction.
The independent judgement is therefore to require a terminal theorem or a
proved decreasing reduction before counting additional counterexample
structure as progress. The even-subdivision theorem is a concrete outcome
of assessing the standalone packing route on that basis, while T44 remains
open.

## Trust boundary

- Promoted theorems have written proofs and adjacent internal audits at exact
  source hashes. Directory placement alone is not treated as promotion.
- Computer-assisted claims are restricted to their finite or explicitly
  reduced-family scopes. The order-eleven and Z3 generation environments are
  research-only; the claim-critical deterministic promoted-result checks are
  separately registered and hash-pinned.
- The shortcut profiles are barriers to local intermediate implications.
  They are not seven-connected and are not counterexamples to T44.
- External inputs are cited beside the results that use them. Recent
  preprints, including Chu's removable-matching theorem, are identified as
  preprints; checking the statement and its use is not an audit of the
  external proof.

## Navigation

- [`active/INDEX.md`](active/INDEX.md): concise live navigation.
- [`results/README.md`](results/README.md): selected completed and audited
  proofs, grouped by scope.
- [`paper/README.md`](paper/README.md): manuscript status and exact contents.
- [T44 technical frontier](active/hc7_k44_closure_frontier.md): exact
  hypotheses, two open obligations, barriers and stop rules.
- [T44 falsification checkpoint](active/experiments/k44_closure_falsification/README.md):
  bounded and reduced-family computational evidence.
- [Frozen exceptional-centre frontier](active/hc7_k7minus_seven_exceptional_frontier.md):
  preserved critical-host reduction and operation/model alignment barrier.
- [Frozen six-connected `4n` frontier](active/hc7_k7minus_sixconnected_4n_sparse_threecut_frontier.md):
  conditional sparse-cut programme.
- [`archive/`](archive/): superseded proof spines and historical ledgers.
