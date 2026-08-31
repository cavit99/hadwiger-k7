# Hadwiger `K_7` research ledger

**Last updated:** 31 August 2026
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
3. **Immediate structural laboratory:** the T44 campaign must close both the
   literal-core portal-exchange obligation and the nonliteral labelled
   branch-model rotation obligation described below.

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
- the four-portal exterior-triangle completion theorem; and
- the three-portal exterior-`K_4` dichotomy, with its tetrahedral exception
  excluded in the spanning case by global portal coverage.

These promoted results have adjacent hash-pinned GREEN internal audits.
Their deterministic finite components are registered in the research
verifier whitelist. The audits cover their exact stated scopes and do not
prove T44, Conjecture 21 or `HC_7`.

### Two open obligations

1. **Literal portal exchange.** Prove the pure labelled trichotomy producing
   a triangle of three four-portal bags, a spanning `K_4` of four
   three-portal bags, or six positive-portal bags whose quotient contains
   `K_6^-`. The whole literal core joins the last outcome to the target.
2. **Nonliteral model-trace rotation.** Use the exact seven-cut through an
   internal branch edge to construct a strictly smaller labelled
   `K_{4,4}` model or the target. Exact cuts alone do not provide
   laminarity, a peel side or preserved branch ownership.

The literal trichotomy has a computation-free proof only through exterior
order six. The order-seven Z3 census is bounded written-unaudited evidence
without an independent UNSAT certificate. Neither obligation is a proved
intermediate theorem.

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
