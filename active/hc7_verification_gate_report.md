# Verification-gate report and research reassessment

**Status:** point-in-time internal verification report, 20 July 2026;
labelled-colour normalization corrected and re-audited 21 July 2026;
publication-scope and programme-mode wording refreshed 27 July 2026.  This
is not a status authority, a new theorem or external peer review.  Current
status remains governed by [`RESEARCH_LEDGER.md`](../RESEARCH_LEDGER.md), and
the reconstructed case graph is
[`hc7_live_case_dag.md`](hc7_live_case_dag.md).

**Current supersession:** this report predates the rooted-helper closure, the
9 August shift to Norin--Totschnig Conjecture 21, and the 22 August shift to
T44 as the sole active completion target.  It remains point-in-time
verification provenance for the frozen direct-`HC_7` programme; consult the
ledger for current conclusions.

## 1. Purpose

This gate asked three questions before another proof campaign:

1. Is there an exhaustive live case graph from a hypothetical
   counterexample to the stated open theorem?
2. Do the load-bearing promoted results survive a fresh audit at their
   present revisions?
3. Does the resulting programme justify further work on a host-level
   response-coupling theorem, and does it support a separate partial-results
   manuscript?

## 2. Exact revisions cold-audited

The following exact source revisions were checked.

| Result | SHA-256 | Cold verdict |
|---|---|---|
| [Low-degree adjacent-pair alignment](../results/hc7_low_degree_adjacent_pair_alignment.md) | `263611a40dc7829788967250e031a3f3170e1c7a6c8c9a3fbfbb358231b1f9ca` | GREEN |
| [Bounded-interface exact-block Kempe reduction](../results/hc7_bounded_interface_exact_block_kempe_reduction.md) | `19382ff7bc0065bc18a7caaeffd5c5fff46cf4ddc226d40036c751081a9853ff` | GREEN after the fixed-colour normalization correction, conditional on its promoted inputs |
| [Generic exact-seven response restart](../results/hc7_generic_exact7_response_restart.md) | `e689c96686a936c27e58c2cba22d699c62ad649092eebfcdfc9c5db95a8e7b5a` | GREEN, conditional on its promoted inputs |
| [Minimum positive-excess separator normal form](../results/hc7_minimum_positive_separator_normal_form.md) | `4b6a4d7a434cb255229fcf4fe12e1393d7b0dadad27985e8528b0535d4cf64ba` | GREEN, conditional on existence of the stated eligible set |
| [Cycle-boundary completion](../results/hc7_cycle_boundary_completion.md) | `f87ddcf7e4bd33b0fc107033033d9a8ebb2f6e32533b1b9c4538c0bf4bd137db` | GREEN |
| [Large-boundary singleton-response descent](../results/hc7_large_boundary_singleton_response_descent.md) | `bce97974e2d3d543aaf9ae2f07ff13b61684ddc9cb6bdf08bacdb750c2be2c97` | GREEN, with the fresh-response qualification below |

The existing adjacent audits already pin these revisions and accurately
state their trust boundaries.  Because the cold audit found no mathematical
change or new gap in the source theorems, their audit files were not rewritten
merely to record a second internal reading.

The exact-block correction is the one exception to the preceding historical
sentence.  Its former Corollary 2.2 was false for two labelled endpoints
giving the fixed block different colour names.  The corrected revision
requires a common fixed name, permits a global endpoint relabelling before
the Kempe sequence, and has a renewed adjacent audit.  Every promoted use
already aligned that name or used existential endpoints, so no downstream
theorem was retracted.

The finite degree-nine completion was rerun over all `4,608` recorded
instances with matching catalogue and witness hashes.  The order-eight/nine
boundary-absorption census was also rerun: there were no order-eight
survivors and the sole order-nine survivor was `K_2\vee C_7`.  The relevant
enumeration and minor-checking code was inspected for incomplete generation,
unsound caching and missing minor operations; none was found.

## 3. External-input check

The exact Mader bound used throughout is correctly sourced to W. Mader,
*Homomorphiesätze für Graphen*, Math. Ann. **178** (1968), 154--168,
[EuDML record and scan](https://eudml.org/doc/161741).  Its `p=7` case is

\[
 K_7\not\preccurlyeq G\quad\Longrightarrow\quad
 |E(G)|\le5|V(G)|-15.
\]

The equality classification quoted from L. K. Jørgensen,
*Extremal graphs for contractions to K7*, Ars Combin. **25C** (1988),
133--148, was checked against its
[publisher record](https://combinatorialpress.com/ars/vol25c/) and an
independent [modern extremal-minor treatment](https://users.monash.edu/~davidwo/files/Hendrey-PhD.pdf)
citing the original theorem.
It gives the five-clique sums of edge-maximal two-apex graphs together with
`K_{2,2,2,3}`.  The repository uses it correctly:

- `K_{2,2,2,3}` has connectivity six;
- a nontrivial five-clique sum has a separator of order five; and
- one two-apex summand is six-colourable by the Four Colour Theorem plus
  two fresh colours.

Thus equality is impossible in a seven-connected seven-chromatic graph,
and the strengthened bound `|E(G)|<=5|V(G)|-16` is valid.  For
publication-level source hygiene, a library scan of Jørgensen's original
article and its exact theorem number should still be obtained.  That is a
citation-verification task, not an identified proof gap.

Martinsson--Steiner Lemma 3.1 and the Las Vergnas--Meyniel Kempe-equivalence
theorem were also compared with their primary statements.  Their hypotheses
are used exactly in the cycle-boundary and exact-block arguments.

One proposed documentation correction was rejected after this comparison.
The opening positive-excess paragraph of the ledger correctly refers to a
Kempe-change graph: it invokes the unbounded exact-block Kempe theorem.
The later order-eight theorem genuinely uses a single-vertex recolouring
graph and is described separately.  Conflating the two would introduce,
rather than repair, a scope error.

## 4. What the audited chain does and does not prove

The audited entry and exact-block reduction yield one exhaustive coarse
chain for degrees seven, eight and nine:

```text
hypothetical counterexample
  -> bounded full separation of order 7, 8 or 9
  -> operation-specific pole-free paths
  -> open pole-free bridge composition theorem.
```

The last theorem has terminal `K_7` and colour-gluing outcomes and a proposed
strict recursive outcome measured by the literal component order.  Relative
to the entry reduction it is sufficient for `HC_7`; it therefore packages
essentially the entire remaining global difficulty.

The fine exact-seven chain has one proved strict arrow: a proper
list-critical core whose full neighbourhood again has order seven returns a
strictly smaller operated shore.  It is not globally well-founded.  The
remaining nonterminal arrows are:

- a singleton shore with a surviving nonbipartite two-connected exterior;
- a minimum positive-excess boundary returning two or three boundary-full
  components;
- a fresh exact-seven response from that boundary, with no proved decrease
  from the previous shore; and
- a shore-filling positive-excess list-critical core.

The developed order-eight and order-nine analyses are conditional
descendants of this positive-excess branch.  There is no proved reduction
from every original degree-eight or degree-nine entry to those detailed
normal forms.

The large-boundary theorem likewise needs its explicit qualification.  A
proper list-critical kernel gives a smaller connected response side, but
its boundary order, trace and inherited branch-set labels are uncontrolled.
It is genuine compression, not an allowed recursive arrow in the labelled
programme until a pullback theorem restores the required data.

## 5. Reassessment

### Full-proof campaign: FROZEN after the follow-up gates

The conditional campaign recommended on 20 July was subsequently carried
out and is now closed as a strategy.  The
[low-degree incident-source fork](../results/hc7_order8_low_degree_incident_source_fork.md),
[unified incident-pair response](../results/hc7_order8_unified_incident_pair_normal_form.md),
[height-six clean bypass](../results/hc7_height6_topological_clean_bypass.md)
and
[incident-bypass conflict theorem](../results/hc7_order8_incident_bypass_conflict_split.md)
are genuine audited gains.  They retain progressively stronger operation
provenance, but none returns an explicit `K_7` model, a common complete
boundary partition, or a strict same-host component descent.

The adjacent
[conflict-compression barrier](../barriers/hc7_incident_bypass_conflict_compression_barrier.md)
shows that the normalized conflict graph may have arbitrary bipartite
topology under the local response data.  It omits the full
contraction-critical host hypotheses and therefore does not refute the open
theorem.  It does show that another path- or conflict-topology campaign has
poor expected value.

Intensive autonomous proof search is consequently paused.  This is a
strategic decision, not a mathematical retraction: the pole-free
bridge-composition theorem remains the sole exhaustive all-degree target.
The current work is the
[external-review and manuscript blueprint](hc7_partial_results_external_review_blueprint.md).
Proof search should reopen only after a specialist supplies a concrete
matching mechanism, a new external theorem matches the required hypotheses,
or a future model closes an exhaustive branch with one of the three allowed
outputs and survives cold adversarial reconstruction.

### Partial-results paper: blueprint only until the external review gates pass

There is enough internally audited unbounded mathematics to prepare an
external-review blueprint for a possible partial-results paper.  The
current strongest coherent package is the low-degree bounded-interface
entry, component-uniform colouring responses, the proved one/two/three
exterior-component upper bounds, exact-seven full-connected-subgraph
packing, and the component-deletion Kempe exchange.  A boundary-labelled
degree-seven result is only an optional secondary application.  The public
benchmark already includes Norin and Totschnig's global unlabelled
[$K_7^\vee$-minor theorem](https://arxiv.org/abs/2507.03244); the possible
contribution here is instead the interface localization, uniform responses,
component bounds, packing restrictions, and retained colouring data.

No full manuscript should be drafted until the gate in the
[external-review blueprint](hc7_partial_results_external_review_blueprint.md)
passes.  A later manuscript must not present the detailed
order-eight/order-nine programme as exhaustive or lead with its live case
tree.  It must not claim novelty or submission readiness until a conventional
literature and priority review, independent human graph-minor and colouring
audits, and independent reproduction of the load-bearing finite
classifications are complete.

### No-go directions

- Do not present the global pole-free bridge theorem as a near-final local
  lemma; with the entry reduction it is `HC_7`-strength.
- Do not extend raw order-eight/order-nine case catalogues without an
  audited entry arrow and strict host-level rank.
- Do not identify palette colours with inherited branch-set labels without
  literal first-hit data.
- Do not count a smaller kernel, quotient or auxiliary path as induction
  unless the returned instance preserves the declared response data.

## 6. Bottom line

The verification gate is passed in the limited sense that the principal
promoted theorems remain sound and the programme has an honest map of its
exhaustive and nonexhaustive parts.  It fails any claim that the current
detailed reductions form a convergent proof.  Current investment should go
to external proof and priority review, independent computational
reproduction, and a blueprint for eventual publication.  Open-ended proof
search with the same architecture is frozen pending one of the explicit
restart triggers above.
