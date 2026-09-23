# Hadwiger `K_7` research ledger

**Last updated:** 23 September 2026. This is the sole authority for current
research status. Internal audits are not external peer review.

**Standing:** `HC_7` and T44 are not proved. Norin–Totschnig Conjecture 21
now has a [written proof](results/hc7_k7minus_bilight_extremal.md) with two
separate hash-pinned internal audits: every finite `K7^-`-minor-free graph
is six-colourable. The proof includes an unbounded extremal theorem and an
elementary nine-vertex quotient lemma. This is not external peer review or a
historical priority determination. Conjecture 19 was resolved externally.

**Objective assessment:** the new C21 theorem, if correct, meets the requested
alternative in mathematical reach and significance. It strengthens NT's
colouring conclusion from excluding two adjacent deleted edges to excluding
one deleted edge, and supplies new rooted and global constructions. This
assessment concerns the completed implication chain, not the number of
lemmas or favourable audits. It relies on cited external results, notably
Dvořák–Norin–Rahman; their contribution is not claimed as ours. HC7 itself
remains open, and the proof still needs external mathematical scrutiny.
The fresh manuscript comparison confirms this assessment of mathematical
scope, conditional on correctness: the colouring conclusion strengthens
both NT and DNR. Their extremal theorems have different thresholds and
connectivity assumptions and are not uniformly subsumed by ours.

## Three-level frontier

1. **Global obligation:** prove `HC_7`, or obtain our own theorem of reach
   and significance comparable to Norin–Totschnig. The alternative now has
   a complete internally audited proof package; the original conjecture
   remains the sole open primary target.
2. **Completed refinement:** every finite `K7^-`-minor-free graph is
   six-colourable (C21). Its stronger extremal input forces `K7^-` in every
   4-bilight graph on `n>=3` vertices with `e>=4n-2`.
3. **Immediate laboratory:** close the entire degree-seven case of an
   HC7-minimal host, using its proper-minor six-colourings and jointly
   chosen rooted bags. The [technical frontier](active/hc7_c21_rooted_density_construction.md#4-what-remains-towards-hc7)
   specifies the colouring-or-minor construction and prior barriers.
   This is an old unresolved case, not a consequence of C21; degrees
   eight and nine remain beyond this checkpoint. Separately, the assembled
   [C21 manuscript](paper/k7minus-six-colour/main.pdf) needs expert review.

The entire degree-seven neighbourhood `K1 join (K3 dotunion K3)` now has
[a written case-closure proof](results/hc7_two_triangle_case_closure.md)
with a fresh separate whole-chain internal audit. This excludes both
`chi(G-{u,r})=5` and `6`, not merely the selected six-chromatic branch.
Its structural theorem gives a `K5` model meeting the two triangles in
every bag, or an apex planar graph. The original host either extends that
model to `K7` or admits a six-colouring. No proper-minor criticality is
transferred, and no finite computation is used. This is one complete
unbounded neighbourhood case, not the whole degree-seven case or HC7.

The [next concentrated attack](active/hc7_c21_rooted_density_construction.md#next-attack-the-split-clique-neighbourhood)
is the other exceptional neighbourhood, `K3 dotunion K4`. Its original
critical host has a common exterior for all four choices of a vertex in
the four-clique. A new working construction retains two disjoint bags
and an actual four-rooted remainder: a rooted `K4` there would give `K7`.
Its web description and decreasing bag exchanges preserve the original
contacts. The [seven-boundary cell theorem](results/hc7_split_clique_seven_boundary_cell.md),
with a separate internal audit, now excludes every triangle-free cell
of the selected type, and every cell whose vertices all have at least
five boundary neighbours. A second [audited construction](results/hc7_planar_seven_boundary_cell.md)
closes the planar case by a six-colouring of the whole original graph.
The remaining minimum exact cell has a nonplanar completed side and
internal triangles. A [new explicit barrier](barriers/hc7_both_nonplanar_cell.md)
rules out closing it from nonplanarity of both overlapping sides alone;
its finite hypotheses are checked, without a separate audit. The attempted
proper-minor colourings still lack an extension through the restored cell.
A separate five-colour reduction now has an
[audited three-contact closure](results/hc7_split_clique_three_contact.md).
After contracting any edge from the centre to its triangle, delete the
contracted root's other colour-class vertices. If the component containing
the remaining triangle edge misses any four-clique vertex, nine paths
from the same colouring form a fully rooted K3,3 scheme and yield K7.
Thus that component must contact all four clique vertices for every
choice of contracted edge and colouring. This closes one unbounded
branch; the remaining four-contact construction is open. The proposed
component exchanges can lose connecting vertices and do not yet give
a monotone reduction. The subsequent fixed-colour-class construction
retains that component across two edge-response repairs. An
[audited Ore-core exclusion](results/hc7_split_clique_ore_core.md)
now closes one resulting literal-five-clique configuration for arbitrary
host order. The [universal flexible-class reduction](results/hc7_split_clique_flexible_entry.md),
with a separate internal audit, removes the special edge-response premise:
every hypothetical split-clique host admits a fixed deleted colour class
and two five-colourings giving opposite endpoints of the remaining triangle
edge the fifth colour. Every minimal list obstruction contains that edge
and contacts all four clique vertices. A
[local counterexample](barriers/hc7_flexible_nucleus_root_edge.md) shows that
even these properties and K7 exclusion do not make deletion of the root
edge colourable; it does not satisfy the original critical-host hypotheses.
The general obstruction still needs a joint minor construction or an
original-host colouring lift. The whole split-clique case, other degree-seven
configurations, and degrees eight and nine remain. The C21 manuscript
is unchanged.

## Completed C21 construction

The [rooted helper theorem](results/five_root_one_missing_contact.md) gives
five prescribed-root bags and two root-free helpers with at most one missing
helper contact in every 4-light five-rooted graph of rooted four-density at
least two. Its computation-free proof uses a degree reduction, a rooted-star
construction and Mader's atom theorem in an auxiliary padded graph.

The [global proof](results/hc7_k7minus_bilight_extremal.md) handles the
obstruction that the rooted result alone did not settle. A minimum
4-bilight counterexample has a consistent high-density side at each five-cut.
The new degree-five construction and an inclusion-minimal-fragment lemma
exclude all five-cuts. Six-connectivity then permits every low-triangle
contraction; the remaining degree-six and degree-seven neighbourhoods
finish the contradiction. Every minor reduction decreases order or the
lexicographic pair `(order, size)` and lifts through disjoint connected
preimages. No quotient inherits chromatic criticality.

Dvořák–Norin–Rahman [Theorem 1.6](https://arxiv.org/html/2609.17760v1#S1)
puts a hypothetical minor-minimal non-six-colourable `K7^-`-minor-free graph
inside this extremal class. That critical-graph reduction was also obtained
independently in the repository by 1 August 2026; the
[dated proofs](paper/k7minus-six-colour/README.md#source-map-and-provenance)
give the same conclusion together with Mader's connectivity theorem.
Their Theorem 1.1 proves C19, not C21;
the new result also proves their stated Conjecture 1.5. Their small-root,
reducible-fragment and rooted-density machinery are explicit external
inputs. The final degree-seven reduction now uses an
[elementary quotient lemma](results/hc7_k7minus_degree7_quotient_hand_proof.md):
five maximal complement types and nine marked cases, with explicit models
and a [separate internal audit](results/hc7_k7minus_degree7_quotient_hand_proof_audit.md).
It replaces the computational premise without changing the theorem.
The original 232-case proof and verifier remain preserved cross-checks;
the current proof applies to hosts of arbitrary order without computation.

The earlier six-cut case analysis is superseded by the global theorem.
Its [proved cases](results/hc7_c21_triangle_boundary_sixcut.md) and
[audited barriers](barriers/five_root_helper_completion.md) remain valid.
In particular, density one still does not force the stronger rooted helper
model: the proof excludes the global obstruction without asserting that
false local extension.

The [frozen C19 plan](archive/hc7_c19_campaign_before_external_resolution_2026-09-21.md)
and [global working draft](archive/hc7_c21_global_composition_working_2026-09-21.md)
preserve the previous constructions and their nonclosures. Prior finite
helper searches are not inputs to the rooted theorem.

## Current frontier and completed campaign

**Written proof; two separate GREEN internal audits.** Every scheme of
every finite simple bipartite target `H` contains an `H`-minor rooted at
all prescribed vertices. There is no degree, order, path-length or
intersection-multiplicity bound. The
[proof](results/bipartite_contractibility_via_matroid_reduction.md),
[first audit](results/bipartite_contractibility_via_matroid_reduction_audit.md)
and [second audit](results/bipartite_contractibility_via_matroid_reduction_second_audit.md)
cover the full statement, including `K_{3,3}`, all `K_{m,n}` and bipartite
theta graphs. It answers Kündgen--Pelsmajer--Ramamurthi's bipartite scheme
questions in Section 8.

The proof uses matroid union to allocate disjoint trees spanning all
required projection components. Either they directly give the rooted
model, or their simultaneous contraction produces a smaller valid scheme.
Host order strictly decreases; fixed disjoint preimages preserve every
root and lift the final model. Both original shores may expand. The
[technical explanation](active/bipartite_contractibility_frontier.md#the-decisive-reduction)
records the ownership argument.

**Written quantitative refinement; separate GREEN internal audit.** For
[schemes with paths of length at most three](results/bipartite_short_scheme_radius.md),
every final bag has intrinsic radius at most two at its original root.
The bound is sharp. At length five the same reduction can create a
root-free component of unbounded intrinsic diameter; this defeats that
invariant, not bounded-radius existence. The refinement does not close
the HC7-related objective or substantiate comparable significance.

**Written corollary.** This independently proves the intended rooted
existence assertion of Biswal--Lee--Rao, Lemma 3.2, under the arXiv v2
independent-intersection convention. Their prefix construction's
intermediate Lemmas 3.5 and 3.6 remain
[refuted](barriers/bipartite_flow_prefix_construction.md). The published
definition's apparent reversal is a separate issue. The corollary makes
no new spectral, separator or bounded-depth claim.

**Assessment.** The [primary-source comparison](paper/bipartite-contractibility/citation_novelty_review.md)
substantiates a universal independent proof and its exact application to
Lee's later flow lemma, including fractional flows and initially
noninjective terminal maps. BLR already intended all roots to be retained;
private four-cycles remove its minimum-degree restriction. Flexible root
families also follow by augmentation. These are not new statement-level
advantages over that intended assertion. Property `(*)` is an equivalent
formulation. Later specialised constructions bypass the disputed
extraction step for some clique-flow applications without proving the
universal rooted theorem. The repair is assessed as a substantial
specialist contribution below NT's demonstrated advance, even granting
first-valid-proof credit; historical firstness remains unresolved.
This earlier bipartite result alone does not meet the benchmark. The C21
assessment above concerns the subsequent colouring theorem. The
[active index](active/INDEX.md) retains `HC_7` as the sole primary target;
C21 does not by itself imply it.

## Durable results and preserved proofs

**Unbounded counterexamples; written proofs and a separate GREEN audit.**
For every odd `ell>=5`, join `C_ell` to `K_{3,4}` at a vertex in its
three-vertex shore. The
[explicit scheme](barriers/triangle_free_bipartite_attachment_counterexample.md)
has `ell+8` nonroots, whereas any fully rooted model would require
`ell+9`. The target is triangle-free, has no skewed theta and has only
one odd cycle. Moreover, every subgraph passes the canonical two-copy
test. Thus both proposed sufficiency statements are false. The proof
allows arbitrary branch-set allocation; its exhaustive finite checker
only confirms the smallest example. The former
[classification campaign](archive/bipartite_contractibility_frontier_2026-09-05_before_attachment_obstruction.md)
is frozen.

The following audited inputs retain their exact statements:

- [Independent-set scheme reduction and pseudoforest host theorem](results/general_scheme_independent_set_reduction.md):
  valid for arbitrary targets under their stated host hypotheses.
- [Necessary odd-cycle-edge condition and series-class parity theorem](results/triangle_free_contractibility_odd_cycle_edge.md):
  the proposed converse is refuted; these necessary results are unchanged.
- [Even subdivisions](results/even_subdivision_contractibility.md),
  [degree three with one shore's roots preserved](results/degree_three_bipartite_weak_contractibility.md),
  [weak-to-rooted equivalence](results/bipartite_weak_to_rooted.md) and
  [`K_{2,n}` contractibility](results/k2n_contractibility_via_matroid_packing.md):
  preserved precursor proofs, now covered by the universal conclusion.

Earlier [odd-subdivision](barriers/triangle_free_odd_subdivision_contractibility.md),
[attachment](barriers/scheme_articulation_colour_fibre.md),
[singleton-shore](barriers/bipartite_scheme_singleton_shore_barrier.md) and
prefix-construction barriers retain their precise intermediate scopes.
They do not refute the universal bipartite theorem, `HC_7` or T44.

The [selected-results map](results/README.md) also preserves the five-root
partial-routing theorem, the four-root `K_4^-` theorem and audited
critical-host results. It is navigation, not a second status ledger.

## Manuscript status

**Primary draft, 21 September 2026:**
[Every graph with no K7-minus minor is six-colourable](paper/k7minus-six-colour/main.pdf),
by Cavit Erginsoy, with [source](paper/k7minus-six-colour/main.tex),
[separate internal manuscript audit](paper/k7minus-six-colour/main_audit.md)
and [build and verification instructions](paper/k7minus-six-colour/README.md).
The 16-page draft includes the supporting constructions, exact external
inputs and the elementary quotient lemma. It preserves the audited theorem
scopes and explicitly distinguishes C21 from HC7. External review and
historical priority remain outstanding.

**Fresh collection assessment, 21 September 2026:** retain three current
papers: C21 as the principal contribution, the seven-page
[bipartite proof/repair](paper/bipartite-contractibility/main.pdf), and the
six-page [paired-region theorem](paper/paired-clique-regions/main.pdf).
The latter two remain mathematically independent of C21. The bipartite
paper is a substantial specialist contribution, with a sharp radius-two
refinement; the paired-region criterion is a useful specialist theorem
for arbitrary terminal-set size. Neither has demonstrated NT-comparable
colouring reach. Their existing audits and qualified priority assessments
remain applicable to the exact revisions they identify.

The 17-page [structural draft](paper/k7minus-low-degree/main.pdf) is now
**a preserved precursor**. C21 excludes its hypothetical critical host.
The new five-connected `e>=4n-2` theorem also excludes its broader defect
theorem's `r>=6, e>=4n` class. Minimum-degree-eight, no-`K5`, degree counts
and the critical-host seven-cut conclusion are therefore not additional
current advances beyond C21. Its [independent supporting lemmas](paper/k7minus-low-degree/README.md#surviving-independent-content)
retain their exact scopes; some apply without a colouring or density
hypothesis. The audited manuscript and provenance remain unchanged.

The five-page [even-subdivision](paper/even-subdivision-contractibility/README.md)
and four-page [K2,n](paper/k2n-contractibility/README.md) papers also remain
preserved precursors. Do not create replacement manuscripts merely to
retain their number. The [collection map](paper/README.md) records this
organisation and version-specific length comparisons. The 21 September
editorial pass adds C21 proof motivation and precise NT/DNR attribution,
and names Cavit Erginsoy in both specialist papers and their PDF metadata.
All three current PDFs were rebuilt, visually checked and covered by
updated editorial-diff audits. The mathematical arguments and precursor
PDFs are unchanged; this is not a further theorem or external review.

The wheel/colouring and attachment-counterexample packages remain parked;
no new manuscript or significance claim follows from this reclassification.

## Preserved conditional routes and historical check

The [T44 frontier](active/hc7_k44_closure_frontier.md) retains three separate
obligations: singleton separator completion, nonsingleton connected
two-sided boundary allocation, and the nonliteral branch-model lift.
An induction must also preserve its full hypothesis class and decrease a
well-founded parameter. Closing only the literal residues would not prove
T44. The [root-expansion result and local barrier](barriers/hc7_k44_expanding_separator_roots.md)
close only the stated fixed-model subcase; global model reselection remains
possible. The critical-host refinement has two safe contractions, with no
closed unbounded induction. The latest independent audit confirms that
equal-endpoint colourings exist in both connectivity cases, while a cut
through an internal branch edge meets at most six model bags. The full
boundary-colouring families are now explicit; converting their
incompatibility into a terminal model remains unproved. The former
C19 construction had a short literal-core proof but lacked a decreasing
arbitrary-model exchange. Its external resolution does not repair that
exchange. C21 is now proved by the separate rooted-density chain above;
our former C19 construction remains incomplete.

The [exceptional-centre programme](active/hc7_k7minus_seven_exceptional_frontier.md)
and [six-connected density programme](active/hc7_k7minus_sixconnected_4n_sparse_threecut_frontier.md)
are superseded by the global theorem. Their local model and colouring
mechanisms remain historical nonclosures; a global conclusion does not
prove those stronger local assertions. Their old restrictions cannot be
imported into an HC7 counterexample, which may contain `K7^-`.

After scrutiny of the C21 proof, the next discovery focus is an actual
minor-minimal non-six-colourable `K7`-minor-free host, retaining its proper-minor
six-colourings alongside a changeable `K7^-` model. The required model
completion or colouring lift is unproved. The [technical frontier](active/hc7_c21_rooted_density_construction.md#4-what-remains-towards-hc7)
keeps the density-only barriers and valid surviving inputs beside that
obligation. This is no claim of a small residual gap or a success probability.

The [chronology review](archive/research_chronology_review_2026-09-04.md)
was checked against initial commit `a14eb38`, fortnightly snapshots
`df001e9`, `92b8722`, `f85e51c`, T44 checkpoint `2c17559` and intervening
retractions, including off-main `15f824c`. The
[previous ledger](archive/RESEARCH_LEDGER_2026-09-05_before_documentation_cleanup.md)
preserves the fuller account and earlier result inventory.

## Trust boundary and navigation

Promoted proofs and adjacent audits are tied to exact source hashes.
Finite computations establish only their stated finite or explicitly
reduced conclusions. Internal audits do not establish external acceptance,
priority or comparative significance.

- [Active index](active/INDEX.md): sole primary target and direct dependencies.
- [Technical frontier](active/bipartite_contractibility_frontier.md):
  global target, completed theorem, application limits and refuted routes.
- [Results](results/README.md) and [manuscripts](paper/README.md): navigation.
- [Archive](archive/): preserved history, retractions and frozen directions.
