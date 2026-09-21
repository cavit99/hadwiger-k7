# Conjecture 21: completed rooted-density construction

**Status, 21 September 2026:** written proof with two separate hash-pinned
internal audits. Every finite `K7^-`-minor-free graph is six-colourable.
The [research ledger](../RESEARCH_LEDGER.md) gives the current significance
assessment. HC7 remains open; internal audits are not external peer review.

## 1. Changed external input

Dvořák, Norin and Rahman, *Every graph with no K7= minor is 6-colorable*,
[arXiv:2609.17760v1](https://arxiv.org/html/2609.17760v1), submitted
15 September 2026, state:

- Theorem 1.1: every `Q=K7-2K2`-minor-free graph is six-colourable.
- Theorem 1.3: every five-connected graph of order `n>=6` with
  `e>=4n-7` contains Q.
- Theorem 1.6: a minor-minimal non-six-colourable `K7^-`-minor-free graph
  is seven-connected and has `e>=4n-2`.

Their first theorem resolves Conjecture 19. Their density theorem directly
excludes our former remaining host: seven-connectivity implies
five-connectivity, minimum degree eight gives `n>=9` and `e>=4n`.
No neighbourhood or exterior-colouring case remains for that application.
These are external preprint results. The statements and this implication
have been inspected; we have not independently reconstructed their whole
proof. They are not our own completion of the user's objective.

## 2. The completed theorem

The [global proof](../results/hc7_k7minus_bilight_extremal.md),
[first audit](../results/hc7_k7minus_bilight_extremal_audit.md) and
[second audit](../results/hc7_k7minus_bilight_extremal_second_audit.md)
establish that every 4-bilight graph on `n>=3` vertices with `e>=4n-2`
contains `K7^-`. In particular this proves Dvořák–Norin–Rahman Conjecture
1.5 for five-connected graphs. Their Theorem 1.6 then gives C21.

The new construction has two parts.

1. The [rooted helper theorem](../results/five_root_one_missing_contact.md)
   gives five prescribed-root bags and two root-free helpers with at least
   ten of eleven possible contacts involving a helper. It holds at rooted
   four-density two in every 4-light five-rooted graph, without an order
   bound. Its reductions preserve all roots and fixed disjoint preimages;
   padding is used only to select a fragment. This part is computation-free.
2. The global proof eliminates degree-five vertices and all five-cuts of
   a minimum density counterexample. A low-density fragment contains a
   low-triangle edge; consistent orientation makes an inclusion-minimal
   such fragment an unrestricted end. A new local end lemma gives the
   contradiction. The resulting six-connected graph has only high-triangle
   edges, and the degree-six and degree-seven terminal arguments finish.

The degree-seven step uses an
[elementary nine-vertex lemma](../results/hc7_k7minus_degree7_quotient_hand_proof.md),
with a [separate internal audit](../results/hc7_k7minus_degree7_quotient_hand_proof_audit.md),
together with a written reduction from arbitrary host order. Five maximal
complement types and explicit models replace the former 232-case
computational premise; its original proof and verifier remain preserved.
The [earlier helper probes](hc7_c21_helper_search_findings.md) are not proof
inputs. The [working draft](../archive/hc7_c21_global_composition_working_2026-09-21.md)
preserves the superseded routes; it is not the audited final proof.

## 3. Barriers remain valid

- A [boundary-star replacement](../barriers/five_root_star_replacement.md)
  can preserve density and destroy lightness. The final argument proves
  admissibility of its particular operations instead.
- [Density one](../barriers/five_root_helper_completion.md#1-the-density-one-extension-fails)
  does not force the ten-contact rooted model. The global end argument
  excludes those obstructions in a minimum counterexample.
- [Arbitrary density](../barriers/five_root_helper_completion.md#3-arbitrary-density-does-not-force-all-eleven-contacts)
  cannot force all eleven contacts. This blocks a direct strengthening
  of the rooted theorem to complete helpers.
- Independently selected helper models can yield `K_{2,2,2,2}`, without
  `K7^-`; the [working draft](../archive/hc7_c21_global_composition_working_2026-09-21.md)
  records that exact model-composition obstruction. The final proof does
  not rely on arbitrary such composition at six-cuts.

The [former six-cut frontier](hc7_k7minus_sixconnected_4n_sparse_threecut_frontier.md)
is now historical. Its global target follows from the new theorem; its
stronger local placement assertions are not automatically proved.

## 4. What remains towards HC7

C21 guarantees a seven-bag minor with at most one missing adjacency in
every non-six-colourable graph. HC7 requires all 21 adjacencies. Completing
that contact while preserving disjoint connected bags remains unproved.
A density-only version of the new theorem cannot supply the last step:
two universal vertices joined to a five-connected plane triangulation give
seven-connected `K7`-minor-free graphs with `5n-15` edges, as noted in
Dvořák–Norin–Rahman's introduction. Their chromatic structure must matter.

The complete [C21 manuscript](../paper/k7minus-six-colour/main.pdf) now
includes the supporting constructions and exact proof dependencies, with
a [separate internal audit](../paper/k7minus-six-colour/main_audit.md).
External review and historical priority remain outstanding. No author
contact has been authorised, and no particular HC7 construction follows
automatically from this theorem.

The next discovery focus is the actual minor-minimal non-six-colourable
`K7`-minor-free host: combine its proper-minor six-colourings with a changeable
`K7^-` model to obtain a `K7` model or a valid colouring lift. This is an
HC7-level construction obligation, not a proved reduction to a small local
case. The density-only and all-eleven-contact barriers above remain in force.
The old `K7^-`-minor-free critical-host degree, clique and defect restrictions
cannot be transferred to this larger class. The separate `3,2,2`
[seven-cut colouring theorem](../results/hc7_k7minus_three_component_seven_cut_exclusion.md)
can be reused only when its actual connectivity and boundary hypotheses hold.

**Selected checkpoint — conjectural:** every seven-connected graph `G`
with `chi(G)=7`, every proper minor six-colourable, and a degree-seven
vertex contains a `K7` minor. This would exclude an entire unbounded case;
it would not settle HC7. A hypothetical minimal counterexample has a
vertex of degree seven, eight or nine, by Mader's connectivity and edge
bounds; see [Rolek–Song, Theorems 1.8 and 2.1](https://sciences.ucf.edu/math/zxsong/wp-content/uploads/sites/13/2018/04/Coloring-graphs-with-forbidden-minors.pdf).

The [existing degree-seven programme](hc7_degree7_model_separator_frontier.md)
already supplies a connected exterior, proper-minor colourings realising
every single repeated neighbour pair, and rooted five-bag models. Its
global compatibility step is still open. For `S=N(u)`, the construction
must produce either a `K7` model or a six-colouring of `G-u` using at most
five colours on `S`; the latter extends to `u`. Choose the repeated pair,
colouring and rooted bags together. More fixed-model responses or a fresh
enumeration of neighbourhoods do not close this checkpoint.

Use the [actual boundary-aligned edge response](../results/hc7_low_degree_boundary_edge_alignment.md)
as a common-host witness, subject to its precise hypotheses. The
[selected-response barrier](../barriers/hc7_degree7_single_edge_response_alignment_barrier.md)
and [reversible rotations](../barriers/hc7_near_k7_rotation_involution_barrier.md)
exclude the old shortcuts. Keep the original critical host fixed; a
quotient supplies a colouring, not inherited criticality. Any recursive
construction needs a proved decreasing parameter and both colouring and
minor lifts. No such completion mechanism is presently established.
