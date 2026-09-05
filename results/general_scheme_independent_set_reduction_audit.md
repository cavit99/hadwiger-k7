# Audit: independent-set reduction and the pseudoforest host theorem

**Status:** separate internal audit, 5 September 2026.

**Audited source:** [written proof](general_scheme_independent_set_reduction.md).

**Exact SHA-256:**
`07fa0fc58284dba6f5ab180a64e92dd86f3829fd31494b8529f00fcaf7751e9f`.

**Verdict: GREEN.**

No mathematical gap was found in Lemma 1,
Corollary 2 or Theorem 3 under their stated hypotheses. The classification
claim is correctly left conjectural. No finite computation is used to
establish any unbounded conclusion.

This was a cold review of the newly written general reduction and
pseudoforest argument by a separate agent, not their author. The auditor
contributed to the preceding bipartite proof and authored the separate
odd-subdivision obstruction draft. This is internal review, not external
peer review or an independence claim about the entire research programme.

## Decisive reduction checks

1. **Quantifiers and projection ground sets.** `T` is an independent set
   of actual host nonroots, with no requirement that its colours be an
   independent target set. Every `T` vertex is excluded from every
   projection vertex set. Its two neighbours on any occurrence remain
   outside `T` and have the opposite endpoint colour. The simple target
   and simple scheme paths ensure that each label occurs at most once
   in each projection. Its neighbours are distinct, so every label is
   a nonloop in at least one projection.

2. **The neighbourhood rank bound.** For each colour, only its nonroot
   neighbours of `T` and its one root can be nonisolated in the
   projection. If their nonroot count is `k`, rank is at most `k`.
   Counting these vertices by colour proves equation (1), even when a
   projection is disconnected or its root is isolated.

3. **Both matroid cases.** If the maximum disjoint forest size is
   `q<|T|`, the minimizing-set equality forces `X` nonempty and each
   restricted forest to span all restricted components. If `q=|T|`,
   the hypothesis `sum r_v(T)<=|T|` forces equality in every rank bound,
   and `X=T` has the same spanning property. No strict inequality is
   silently required in the second case.

4. **Ownership and retained edges.** Every contracted set consists of
   base vertices outside `T` and labels allocated to it at most once.
   Consequently a label can never also survive as an independently
   owned base vertex. Removing an occurrence of `x in X` identifies its
   two neighbours through their own component's allocated tree. This
   does not require access to `x` when another component owns it.
   All remaining steps use images of actual edges with both endpoints
   outside `X`. Their two colours remain distinct.

5. **Root and scheme preservation.** Contracted components contain at
   most their own colour's prescribed root. Quotient walks retain both
   prescribed ends; erasing closed excursions produces simple paths.
   Every other root has a different colour and cannot be internal.
   At any intersection the quotient vertex's colour is a common target
   endpoint. The proof correctly imposes the scheme condition only
   after contraction, not on the precontraction rerouting walks.

6. **Strict descent and lift.** Nonempty `X` contains a nonloop label,
   hence the simultaneous spanning family has positive total rank.
   Some contracted set contains two distinct base vertices and its
   allocated label. Thus host order strictly decreases. Replacing each
   quotient vertex by its fixed connected preimage lifts every rooted
   minor model, preserving disjointness, all roots and every required
   contact. This justifies the minimum-order argument in Corollary 2.

## Terminal pseudoforest theorem checks

The condition concerns the graph after deleting all prescribed roots.
It is preserved by every root-preserving minor used here: nonroot
quotient vertices have connected preimages avoiding the original roots,
so the new nonroot graph is a minor of the original one. Deletion and
contraction preserve the pseudoforest condition.

The stronger normalization is correctly distinguished from mere proper
colouring. Its cited primary input was checked in KPR,
[Definition 3.1, Remark 3.2 and Lemma 3.3](https://arxiv.org/pdf/1207.6141).
It provides edge-disjoint scheme paths with at least two memberships
at every nonroot. Each membership supplies at least one nonroot
neighbour, and different memberships supply different neighbours.
Consequently a normalized nonroot pseudoforest has minimum degree two
and is a union of cycles. Equality forces exactly two path memberships,
each using one nonroot edge and one root edge.

On an oriented cycle, assigning `x_i` to the root of the preceding
colour produces disjoint connected stars. The contact proof was checked
with repeated colours allowed: the demand represented by
`x_i x_(i+1)` is supplied by the *next* cycle edge
`x_(i+1) x_(i+2)`, whose ends are assigned to its two required colours.
It does not assume a rainbow cycle or one cycle per colour. Literal
root edges remain valid contacts. The final model lifts through the
normalization by the same fixed-preimage argument.

## Scope and unresolved obligations

No unresolved assumption or gap was identified in the three stated
results. Their external inputs are the cited matroid union equality
from the audited bipartite proof and the exact KPR normalization.

Strict independent-neighbour expansion in a hypothetical counterexample
does not imply a shift automorphism, one nonroot per colour, or a bound
on host order. The pseudoforest theorem has an explicit host restriction.
Neither result proves the proposed hereditary M'-classification, full
rooted `K_5` or `K_6` contractibility, Hadwiger's conjecture for `t=7`,
or a comparative significance claim.

Verification was theorem-level inspection and exact source-hash checking;
no computational experiments were needed for this audit.
