# Audit of the deficient near-clique bag reduction

**Date:** 7 September 2026.

**Status:** separate internal mathematical audit.

**Verdict: GREEN.** The audit covers the theorem as stated,
including retention of every original core bag
and the bridge and no-triangle conclusions when the minimum deficient
bag has order two.
This is not external peer review or completion of the research objective.

## Exact revision checked

The source is
[the deficient-bag reduction](hc7_near_clique_deficient_bag_normalization.md),
with SHA-256:

```text
537e885c1ef8930fadde8a8bf12423044e8d20a99b6c2f78a4b379e17870c4f2
```

The earlier draft was checked at
`1294a0150be1bcd1c2817d5967db680e00fa749613fd195cb6b7055dd9076977`.
Promotion changed its status and added the no-triangle conclusion and
proof. The complete promoted source was reread at
`1abf101d17d84b017735d670b802bf63521b88fe252acd329975aa91c2f399ef`.
The final revision clarifies that an outside component has a neighbour
on the path interior, rather than intersecting it. Reversing precisely
that wording change recovers the preceding hash; the actual-adjacency
argument checked below is unchanged. The earlier checks are retained.

The reviewer read the complete source at this hash and checked the
arguments below directly. The reviewer had previously discussed the
proposed reduction with its author; this is a separate full-source
internal check, not a claim of blind review. No online source,
computational result or unproved external theorem is a premise.

## Strongest inferences checked

1. **The minimization class is preserved.** The original model makes the
   class nonempty. It is finite because the host is finite. Replacing
   `D` by a connected subset preserves `D subseteq D_0`; absorbing a
   leaf or an unused component into one `T_i` preserves every inclusion
   `T_j^0 subseteq T_j`, fixes `B,C`, and keeps all bags disjoint. An
   absorbed component has an actual edge to its recipient bag, so that
   bag remains connected. Enlarging `D` by an unused component is used
   only to exhibit a forbidden `K_7^-` model, not as a minimization step.

2. **The path normalization uses selected witnesses correctly.** A tree
   minimal for the four chosen contact ends spans the minimum `D`.
   Every leaf of a nontrivial tree must carry at least two selected
   labels: an unlabelled leaf can be deleted, and a singly labelled leaf
   can be absorbed into that label's core bag. Its tree edge then supplies
   the required contact to the remaining `D`. Four labels force exactly
   two leaves, each with two distinct labels, hence the asserted path.
   Extra actual contacts need not be counted as selected labels.

3. **Reselecting a witness gives strict descent.** An internal contact to
   `T_i` permits moving label `i` off its original end. That end now has
   only its other selected label and can be absorbed into the corresponding
   core bag. The internal witness retains the first contact, and the path
   edge retains the second. The same argument applies to an opposite-pair
   contact at an end. Each contradiction therefore produces a model in
   the same class with strictly smaller `|D|`; no enlarged-core step is
   being used as an unsupported infinite iteration. A path chord would
   similarly give a smaller connected bag retaining all four end contacts.

4. **The two-vertex separator is an actual vertex separator.** Components
   outside the seven bags are components of the full remaining graph.
   If such a component touches a path interior and a core bag, absorbing
   it into a `T_i` permits the preceding shortening, or joining it to `D`
   creates a fifth core contact when it touches `B` or `C`. Thus none has
   a core contact. After removing the two ends, the nonempty path interior
   and every outside component attached to it have no route to the six
   core bags. This contradicts three-connectivity when `|D|>=3`.

5. **The order-two component analysis is exhaustive.** An outside
   component touching `x` cannot meet the opposite `T` pair or `B,C`;
   the symmetric restriction holds at `y`. A component touching both
   would therefore have its entire external neighbourhood in `{x,y}`,
   again contradicting three-connectivity. Distinct outside components
   have no edges between them by their definition. Consequently every
   path in `G-W` from the `x` side to the `y` side uses `xy`, proving
   the bridge assertion and both full-neighbourhood inclusions.

6. **There is no triangle through the deficient edge.** A common neighbour
   of `x,y` cannot lie in a core bag, by their disjoint permitted pairs
   and the exclusion of `B,C` contacts. Any other common neighbour belongs
   to an outside component meeting both ends, which item 5 excludes.
   This covers every possible third vertex; no connectivity claim about
   contracting `xy` follows from it.

7. **The final count concerns vertices.** The external neighbourhood of
   `Q_x` consists of `y` and vertices of `T_1 union T_2`. Removing it
   leaves the nonempty `Q_x` separated from the nonempty bags `B,C`,
   so seven-connectivity gives at least seven neighbours. Removing `y`
   leaves at least six distinct actual vertices. No conversion from
   these vertices to six distinct bag contacts is made. The argument
   for `Q_y` is identical.

## Corrections, assumptions and remaining work

No substantive correction to the checked source is required. The stated
hypotheses are used: three-connectivity excludes the displayed cuts;
absence of a `K_7^-` minor excludes additional foreign-core contacts;
finiteness supplies a minimum; and seven-connectivity is used only for
the final six-neighbour bounds. There is no preserved-root assertion for
vertices of the original deficient bag, and no quotient-connectivity or
colouring claim.

There is no identified gap in this reduction. The singleton case and
the simultaneous connected allocation through the two core bags on
each side of the order-two case remain unproved. The reduction provides
no terminating continuation through those cases and proves neither
Conjecture 19, Conjecture 21, T44 nor `HC_7`. Its significance is not
asserted to meet the user's alternative completion standard.
