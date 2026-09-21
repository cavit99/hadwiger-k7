# Independent audit of the K7-minus density and six-colour theorem

## Current revision review

**21 September 2026: GREEN.** The current proof source has SHA-256
`4c48b60d4de77de2afc357ba81b47d8f2107656b5684005f743d247f894620d3`.
A separate auditor checked its complete diff from the original revision
below and independently reconstructed the replacement
[nine-vertex lemma](hc7_k7minus_degree7_quotient_hand_proof_audit.md).
Only the degree-seven input and its description changed: the lemma's
hypotheses and conclusion, the component contraction and its lift are
unchanged. The new proof classifies five maximal complements and supplies
all nine marked models explicitly. No executable premise remains in this
step; the external inputs and all other mathematical arguments are unchanged.

This is one focused replacement audit, recorded in both global audit files,
not two new whole-proof reconstructions. The original reconstruction below
applies to the unchanged arguments; its computational review is preserved
as provenance for the superseded proof of the nine-vertex lemma.

## Original reconstruction: superseded computational revision

**Date:** 21 September 2026.

**Verdict:** GREEN.

This is a separate internal audit.
No unresolved mathematical gap was found in the stated extremal theorem
or its C21 corollary, subject to the external results and finite verification
boundary identified below. This is not external peer review or a priority
assessment. HC7 remains open.

## Exact audited source and dependencies

The audited source is [the complete proof](hc7_k7minus_bilight_extremal.md),
with SHA-256

```text
4ffbe9fc80a47713173a5f260759959da9397379ff26c2b18754eba5e97a560f
```

The following local dependency revisions were inspected. The second through
fourth entries include the transitive inputs to the rooted helper theorem,
not merely the lemmas cited directly by the global proof.

| Source | SHA-256 |
| --- | --- |
| [Rooted helper theorem](five_root_one_missing_contact.md) | `078ba860d4cdde187cdc6e618a4e1842dd623523dbefbe3ead06544c7d8afa18` |
| [Rooted degree and connectivity reductions](hc7_c21_rooted_density_low_degree_reduction.md) | `431bd7d7d2b5bcb59e385781234c6d7ed6824f62ee50eb8ddf49e69da792cef2` |
| [Degree-six helper reduction and local contraction lemma](hc7_c21_helper_degree_six.md) | `85927a0f7d1af6229930fd67f7144eac35b934c54ad504539a34d39e209020ee` |
| [Degree-five rooted dart](rooted_dart_nonroot_degree_five.md) | `37dcf256f64fca7c49a1bd4ec66021371fba9a7863bf9523597ba4b898ecfad2` |
| [Degree-seven quotient lemma](../active/hc7_k7minus_degree7_common_neighbour_exclusion.md) | `663c1b7e0de9b0951de89801d52baf4aae12535d7807547d19d04fc10b00c4b0` |
| [Quotient verifier](../active/hc7_k7minus_degree7_quotient_verify.py) | `ac0c37438d802930a0aa80bfd1d6491101da3df9a55fac1e1cf3db5ae1b7e445` |

The auditor reconstructed the arguments before reading other audits. A
separate cold subaudit checked the rooted-dart lemma and its imported
terminal construction. The initial reconstruction covered the working
draft at SHA-256
`26aff1304f1acb7e101fdd6284fc5dc19b4b1ea22363ca991f1c90def4da2df5`.
The promoted source was then read in full: its reordered core retains the
hypotheses and conclusions used in that reconstruction. Its new Section 7
was audited independently, rather than accepted as an equivalent copy of
the older five-connected degree-six argument. The last terminology edit
distinguishes nonempty opposite sides from strict set containment.

The rooted degree-reduction dependency was repinned after two status
sentences were corrected. Reversing those two sentences reproduces its
previous hash `11d1897cbcf5ad2d7092affc1161c822fd2f537fdf533a3a8ef73d4f48851b79`;
no mathematical text changed.

## External inputs and their use

The inspected primary statements are Dvořák--Norin--Rahman,
[arXiv:2609.17760v1](https://arxiv.org/html/2609.17760v1), Theorems 1.6,
2.6 and 2.7, Lemma 3.3, Observation 4.1 and Corollary 4.2. The adaptation
of their Section 5 was checked against its actual proofs. H2 supplies
their permitted small-root configurations, while the global composition
retains H2's stronger contact count. No density-one version of H2 is used.
The terminal construction of their Lemma 3.1 is used under its explicitly
isolated hypotheses in the rooted-dart input.

The local quasi-five-connectivity assertion is proved within the local
dependency; the stronger global hypotheses of Kou--Qin--Yang--Zhang--Zhao
are not silently imported. Menger's theorem and elementary connectivity,
minor-model and planar edge-count facts are used in their ordinary forms.

For H2, the statement of Mader's atom theorem reproduced as Theorem 5 of
Kriesell--Schmidt, [arXiv:1610.09093v1, printed page 5](https://arxiv.org/pdf/1610.09093v1),
was inspected in the rendered PDF. In particular, its condition uses
`T` minus the opposite fragment, not `T` minus the atom.

For the new terminal argument, the primary
[Robertson--Seymour--Thomas Theorem (2.4)](https://thomas.math.gatech.edu/PAP/hadwiger.pdf)
was checked, as was its quotation in
[Norin--Totschnig, Theorem 13, arXiv:2507.03244v1](https://arxiv.org/html/2507.03244v1).
The audit treats these external theorems as inputs; it does not claim to
reprove their full external dependency chains.

## Reconstruction of the global argument

**Minimum class and orientations.** The density bound excludes orders
three through eight. Reducible-fragment replacement decreases order and
retains the minimum class. The identity for the two five-shore densities
gives sum at least `m+8`. Two heavy shores produce a rooted clique on one
side and an H2 model on the other, with disjoint interiors. This proves
the heavy threshold `m+7`. The linkage consistency argument preserves
all five distinct boundary roots and both helpers. In the edge-deletion
argument, the trimmed positive side is nonempty; if its original boundary
has order five, its remaining density is at least six. Thus the
density-one exception cannot obstruct the deletion step.

**Five-connectivity and degree six.** Deleting a vertex of degree at most
four can only create a positive five-boundary side of density at least
two. The consistency result excludes any resulting dense bifragment.
At a smaller minimum cut, the selected light component retains all its
degrees and has the required rooted connectivity. The clique, triangle
and dart constructions make it reducible, with at least three vertices
remaining outside it.

The localized unique-neighbour contraction lemma was checked by its
corner counts. The degree-five split-off preserves density and is an
actual minor. Its positive quotient sides lift with the stated density
correction. A two-vertex side forces the displayed adjacent degree-five
pair; repeating the contraction produces the four-cycle and its two
external triples. Each possible intersection size is covered. In the
disjoint-triple case, the selected quotient side cannot have one or two
vertices, so the localized contraction lemma applies with both required
shore-size bounds. Every successful contraction decreases order and has
a fixed connected preimage.

**Low sides and ends.** The weighted degree calculation on a low shore
produces a vertex with weight at most eight. If all incident edges had
four common neighbours, the rooted star and the five disjoint paths
would give ten helper contacts. The central helper avoids the boundary;
the trimmed fifth path remains nonempty. The opposite rooted clique then
gives the forbidden minor.

The end lemma was reconstructed for both internal and boundary-crossing
edges. A corner with containing boundary of size five has exactly that
boundary, including both endpoints of the designated edge; its opposite
side contains `C`, and it is a strict subset of the end. Smaller corner
boundaries always have a nonempty complementary side. The three patterns
of nonempty `A`-corners exhaust the possibilities and contradict
the four-vertex lower bound. Choosing an inclusion-minimal low eligible
fragment is valid: a smaller heavy eligible fragment would be disjoint
and nonadjacent to the heavy opposite side. Thus this is an unrestricted
end, with no assumed closure of positive-density fragments under crossing.

**Final degree cases and colouring.** The graph is now six-connected.
An edge in at most three triangles would contract to a five-connected,
4-bilight smaller graph of sufficient density. Hence every edge is in at
least four triangles, while average degree is below eight.

In Section 7 the two-path models fill two missing matching edges while
preserving all seven bags. Six-connectivity supplies the required
exterior attachments. After deleting the three specified vertices, the
separation outcome of RST (2.4) lifts to a proper separation of order at
most five: the deleted centre is on one open side and has no neighbour
in the other. The disc outcome and the deleted-edge count give
`e<=4v-9`. This proof does not use the old auxiliary five-separation or
prescribed five-linkage claim.

The degree-seven case contracts one whole exterior component and
retains precisely the required nine-vertex quotient. Its certified model
lifts by replacing that quotient vertex with the component. Finally,
DNR Theorem 1.6 directly supplies seven-connectivity and `e>=4v-2` for
the minor-minimal colouring counterexample. No stronger critical-host
lemma or inherited criticality of a proper minor is needed.

## Rooted input reconstruction

The H2 minimum-counterexample reductions preserve the five prescribed
roots and a genuinely decreasing lexicographic parameter. The proper-side
linkage preserves H2 itself when all five roots are linked; small-root
extraction is used only in the remaining reducible-fragment alternative.
The degree-five edge construction retains root-free helpers throughout
rerooting and the lift back to the original roots.

In the padded graph, an eligible atom meeting the padded clique would
contain more vertices than an already available root-free fragment.
Thus the minimum atom avoids the roots, and its closed side is proper
in the original graph. Its weighted degree supplies an eligible incident
edge whose two endpoints lie outside the complementary fragment. Both
local hypotheses of Mader's theorem hold. The resulting atom-size bound
contradicts its degree and density lower bound. Padding is solely an
auxiliary selection device, not a minor reduction.

The rooted-dart induction retains every interior neighbour and decreases
order by at least two. Its final linkage segments meet the selected side
only at distinct boundary roots and avoid the helper. The external
minimum-spine construction requires no unused density hypothesis.

## Finite verification boundary and limits

The quotient verifier was inspected and run with

```bash
UV_CACHE_DIR=/tmp/hadwiger-k7-uv-cache uv run python3 active/hc7_k7minus_degree7_quotient_verify.py
```

It returned

```text
complement types: 29
full-or-one-missed attachment cases: 232
model support orders: {7: 67, 8: 102, 9: 63}
certificate digest: b98ac56930aa7044c3a6a7c029b75cd85feb39f4dabd8476a0ba7f08ccdb7306
GREEN: every quotient contains a certified K_7^- minor
```

Every simple maximum-degree-two complement is a disjoint union of paths
and cycles, so the generated component multisets cover all types. The
eight attachment choices cover every set of size at least six. The
750 candidate partitions cover supports of orders seven through nine.
The returned models have seven nonempty, disjoint, connected bags and
at most one missing interbag adjacency. Known positive and negative
self-tests also passed.

The executable trust boundary is this finite generation, search and
certificate checking in standard Python. Search and certificate checking
share the basic connectivity and contact predicates; this audit does not
claim a separately implemented executable checker. Those predicates and
the enumeration were independently inspected. No finite host-order search
is an input to H2 or to the unbounded reductions.

The resulting conclusions are the stated 4-bilight extremal theorem,
its five-connected specialization, and C21. No remaining local gap was
identified. The audit does not establish HC7, external acceptance, or
historical priority, and does not by itself decide the user's comparative
significance criterion.
