# Hadwiger `K_7` research ledger

**Last updated:** 2 September 2026
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
   two exact residues.  A minimum nonsingleton crossing blocker is
   three-connected of minimum degree at least four, with sharply classified
   three-cuts.  Its seven-resource inequalities imply a five-support
   six-boundary system.  Either a closing bond already exists, or a minimum
   support-full bond side opposite the distinguished `a`-neighbour has one of
   three explicit block forms, and is a plain path if it sees `b`.
   Eliminating those forms is the exact nonsingleton leaf-block completion
   lemma.  For an adjacent singleton pair,
   every literal-shore split
   and every three-component contraction trace is now eliminated.  In the
   sole two-component core-concentrated profile, every rooted `K_5` has joint
   endpoint-contact rank at most three.  The one-defect two-helper split is
   target-producing; in the target-free profile its failure returns a marked
   proper connected side whose full neighbourhood is an actual separator.
   Eliminating that marked separator profile is the remaining singleton
   task.  The
   nonliteral labelled branch-model rotation obligation remains separate.

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
- the five-support bond reduction: minimum-blocker strictness gives the
  six-boundary inequality and, unless a closing bond already exists, a
  minimum support-full side opposite the distinguished `a`-neighbour has one
  of three explicit block forms; the `b`-meeting case is a path with exactly
  two split supports, and a rainbow four-support path reduces to the standard
  weakly-linkable parity obstruction;
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
   leaf-block completion lemma: eliminate the three minimum-side block forms
   using the complementary side, the full `a,b` incidence and the exact
   three-cut profiles.  The `b`-meeting form is already reduced to a plain
   path.  For a singleton blocker,
   eliminate the entire
   core-concentrated profile.  The current theorem only returns a marked
   separator certificate: even order seven is not yet proved sufficient for
   a target or safe contraction, and no well-founded descent through larger
   boundaries is known.  Closing both residues would give a safe contraction;
   induction would then prove the pure labelled trichotomy, and the whole
   literal core would join its six-bag outcome to the target.
2. **Nonliteral model-trace rotation.** Use the exact seven-cut through an
   internal branch edge to construct a strictly smaller labelled
   `K_{4,4}` model or the target. Exact cuts alone do not provide
   laminarity, a peel side or preserved branch ownership.

The literal route now has the following audited unbounded reductions.  A
minimum nonsingleton crossing blocker `X` is three-connected with
`delta(G[X])>=4`; every one of its five non-atom boundary resources has at
least two neighbours in `X`, deleting a specified atom-neighbour leaves all
six other resources represented, and every three-cut has one of two exact
resource-distribution profiles.  The missing nonsingleton statement is now
a single boundary-bisection lemma whose positive outcome feeds an explicit
two-helper `K_7^-` construction.

An audited spanning-normal-form corollary makes the numerical residue exact.
Any positive pair of disjoint adjacent connected helpers can absorb every
unused component without increasing its defect.  For an ordered spanning
partition, let `s` count the five non-atom resources represented on both
sides, and let `epsilon_b=1` exactly when the second side misses `b`.  The
minimum defect over the omitted resource is

`max(0,4-s+epsilon_b)`.

Thus the two-helper inequality holds exactly when `s>=3+epsilon_b`: three
split supports suffice when the second side sees `b`, while four are needed
when it misses `b`.  This is an exact reformulation of the sufficient
construction, not a proof that such a partition exists.

The new audited five-support reduction removes most of the arbitrary
partition geometry.  If `R_d=N_X(d)`, minimum-blocker strictness gives

`|N_X(W)|+|{k in K:R_k meets W}|>=6`

for every nonempty proper connected `W`.  Choose the distinguished
`p in R_a` and minimize a support-full bond side `U` subject to `p` lying on
the complementary side `V`.  If no closing bond exists, `X[U]` is either a
path with at most one edge replaced by a triangle, a triangle with a pendant
path, or a subdivided claw with its centre optionally replaced by a triangle.
Every vertex of `U` meets `V`, singleton leaf lobes have at least three
neighbours there, and the case in which `U` sees `b` is a plain path with
exactly two split supports.

The same reduction exposes the correct planar obstruction.  A rainbow path
through four distinct `K`-supports from an `a`-support vertex to a
`b`-support vertex gives a closing bond unless its parity instance is weakly
linkable in the sense of Chen--Ding--Yu--Zang.  Thus a four-connected
nonplanar blocker carrying such a rainbow path closes.  More generally, a
nonclosing four-connected nonplanar profile has no `K`-support containing
distinct vertices from both `R_a` and `R_b`.  In a four-connected facial
obstruction, Euler's formula
forces some `K`-support off the facial cycle.  Conversely, an
explicit icosahedral-minus-one-vertex profile shows that the stripped
four-support bond claim is false even when `X` is four-connected and the
five-root augmentation is six-connected.  That augmentation nevertheless
contains an unrooted target, and the fixed profile has no full `a,b` blocker
extension.  Thus this is a barrier to discarding the distinguished supports,
not to the exact blocker lemma.

Those three-cut profiles do not by themselves permit whole-component
bisection.  The technical frontier records an explicit profile
`K_3 join (3K_2)` which satisfies all preceding local consequences but leaves
two helper defects, hence only nineteen guaranteed contacts, whenever the
three components are kept intact.  Splitting one component closes that
profile, so this is a route nonclosure rather than a counterexample to the
full bisection lemma.

A second order-nine polarized incidence profile refutes the proposed
purely intra-component nonseparating-transversal repair while still having
231 spanning two-helper witnesses.  A third profile refutes the proposed
cross-component condition if its first side is unnecessarily required to
see `b`: it has no witness to either that mode or the component-local mode,
but has 54 witnesses after the redundant requirement is removed.  Neither
profile is known to occur in an ambient seven-connected blocker.

The exact `H`-full-complement subcase asks for a connected nonseparating
set which sees `a` and at least three of the five `K`-resources; the crossing
edge `ab` supplies `b` to the first helper for free.  The remaining hard
incidence phenomenon is support transfer when the complementary side is not
`H`-full.  The sharp theorem to prove is now the leaf-block completion lemma:
use the complementary side, full `a,b` incidence and exact three-cut profiles
to eliminate the three minimum-side forms above.  Equivalently phrased as a
proof goal, produce a closing bond in each form; a rainbow support path and
exclusion of its weakly-linkable planar outcome is one sufficient route.

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
neighbourhood-independence inequality.  This supplies only the first safe
edge: its contraction is six-colourable and need not remain seven-connected,
so the corollary neither iterates nor replaces universal T44 as the sole
active target.

## Durable recent results outside the active spine

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
  inequality.  It forces the first safe exterior edge but cannot be iterated
  after the resulting six-colourable contraction.

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
They may be reactivated only if T44 is independently falsified or a new
lemma directly removes one of their recorded barriers.

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
