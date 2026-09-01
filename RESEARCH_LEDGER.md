# Hadwiger `K_7` research ledger

**Last updated:** 1 September 2026
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
   three-cuts; an adjacent singleton pair has an exact contraction trace,
   and its two-component literal-shore split has explicit separator and
   endpoint-miss profiles.  The nonliteral labelled branch-model rotation
   obligation remains separate.

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
- the contraction-trace theorem for an adjacent singleton pair: the edge lies
  in an exact seven-cut with two or three complementary components; the
  three-component case puts one literal shore and one exterior vertex on a
  subcubic boundary, while the two-component case is either a whole-shore
  split or has a rooted `K_5` with universal endpoint-contact bounds; and
- the exact shore-split profile theorem: an unbalanced split has one connected
  tight small shore and reduces to an order-one or order-two attachment
  separator, while a balanced `2+2` split has the displayed exact endpoint
  miss types and, when both one-endpoint miss types occur, their forced
  cross-nonedges.

These promoted results have adjacent hash-pinned GREEN internal audits.
Their deterministic finite components are registered in the research
verifier whitelist. The audits cover their exact stated scopes and do not
prove T44, Conjecture 21 or `HC_7`.

### Two open obligations

1. **Literal exact-residue completion.** Close both audited outcomes of a
   minimum crossing blocker.  For a nonsingleton blocker, prove the precise
   minimum-degree-four boundary-bisection lemma.  For a singleton blocker,
   eliminate the exact contraction traces: the core-concentrated rooted-contact
   profile, the unbalanced and balanced literal-shore split profiles, and the
   three-component whole-shore trace.  This yields a safe contraction,
   induction gives the pure labelled trichotomy, and the whole literal core
   joins its six-bag outcome to the target.
2. **Nonliteral model-trace rotation.** Use the exact seven-cut through an
   internal branch edge to construct a strictly smaller labelled
   `K_{4,4}` model or the target. Exact cuts alone do not provide
   laminarity, a peel side or preserved branch ownership.

The literal route now has three further audited unbounded reductions.  A
minimum nonsingleton crossing blocker `X` is three-connected with
`delta(G[X])>=4`; every one of its five non-atom boundary resources has at
least two neighbours in `X`, deleting a specified atom-neighbour leaves all
six other resources represented, and every three-cut has one of two exact
resource-distribution profiles.  The missing nonsingleton statement is now
a single boundary-bisection lemma whose positive outcome feeds an explicit
two-helper `K_7^-` construction.

Those three-cut profiles do not by themselves permit whole-component
bisection.  The technical frontier records an explicit profile
`K_3 join (3K_2)` which satisfies all preceding local consequences but leaves
two helper defects, hence only nineteen guaranteed contacts, whenever the
three components are kept intact.  Splitting one component closes that
profile, so this is a route nonclosure rather than a counterexample.  The
precise repair is an intra-component nonseparating-transversal lemma.

For a singleton blocker `p`, the adjacent edge `ap` has an exact contraction
cut.  A three-component response has a subcubic boundary consisting of
`a,p`, one literal shore and one exterior vertex.  A two-component response
is either core-concentrated, giving a rooted `K_5` which each endpoint meets
in at most three bags, or splits the opposite literal shore.  In the latter
case the unbalanced split has a connected tight small shore, places the
unique common neighbour in the large component, and forces an order-one
attachment separator when the fifth boundary vertex is exterior (or the
specified order-two core separator when it is a core vertex).  The balanced
  `2+2` split is reduced to exact endpoint-miss types and, when both
  one-endpoint miss types occur, their forced cross-nonedges.

These results identify the remaining mechanisms; they do not eliminate
them.  The computation-free induction base remains exterior order at most
six, and all order-seven and newer finite screens are bounded evidence only.
The weighted splitter theorem, the literal T44 branch, T44, Conjecture 21,
and the nonliteral rotation obligation all remain open.

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
