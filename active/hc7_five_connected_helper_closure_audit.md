# Internal audit: five-connected rooted-helper closure

**Verdict: GREEN.** Lemma 1 and both conclusions of Theorem 2 hold at
the revision below. This is a separate internal mathematical audit, not
external peer review or a proof of the global six-colouring conjectures.

**Audited source:** [five-connected closure](hc7_five_connected_helper_closure.md).

**Whole-source SHA-256:**
`d68986c2c5228b322c8f1c93fff532d4c5f5b49009448a827ea7204fe5016513`.

The audit is deductive; no finite enumeration is used.

## Exact inherited input

The cited [rooted-helper source](../results/hc7_k7minus_degree7_rooted_helper_closure.md)
has the stated SHA-256
`6ffee04cf9ff66275f9674c24bc2b9c669b1e108b76e5b1d2a18ec7d0106fe67`.
Its [GREEN audit](../results/hc7_k7minus_degree7_rooted_helper_closure_audit.md)
has SHA-256
`360a121c2ca33bc81b6300551203956f9bca6c00866d3c524bfe3602c9744407`.
Both hashes were checked. That audit records the exact Norin--Totschnig
Lemma 12 input, including the adjacent helpers and prescribed root bags.
The primary text was not freshly inspected during this audit.

## Strongest inference: the actual four-vertex boundary

The finite optimization does not assume five-connectivity of `F`.
If a root bag has two distinct vertices contacting the helper union,
distinct contacts to the two different helpers can be chosen: otherwise
both contact sets would be the same singleton. Shrinking the bag to a
minimal tree through those contacts and its root preserves every required
model contact. Secondary minimality therefore makes that tree span the
bag. At least one contact is a leaf different from the prescribed root.

Moving that leaf to its contacted helper preserves both bags' connectivity.
The leaf's former tree edge supplies the retained root-bag contact, and
the other selected contact supplies the other helper contact. No root
moves; all old helper contacts persist because the helper only grows.
Thus maximality forces exactly one actual contact vertex per root bag.
No unused component can contact a helper, since it could be absorbed.

The entire helper union therefore has at most four actual external
neighbours in `F`. If `v` misses both helpers, these remain its entire
external neighbourhood in `G`. Deleting those vertices leaves `v` and
the nonempty helper union on different sides. This is an actual separator
of order four, not a separator of abstract model labels. Five-connectivity
of `G` contradicts it. There is no assumption that a returned arbitrary
model was already adjacent to `v`.

## Density and the seven-bag lift

Deleting `v` leaves a four-connected graph and transforms the density
bound exactly to `e(F)>=4|V(F)|-9`. Thus the inherited rooted input applies.
Each literal edge between members of `Z` survives all root-bag shrinking
because its endpoints remain in their prescribed bags. The singleton
`v` keeps its four root contacts and gains the helper contact supplied
by Lemma 1. All seven bags are connected and disjoint in the original
host. For `K_4^-` roots the two possible missing pairs have disjoint
ends; for `K_4` roots only the second helper contact can be missing.

## Remaining obligations

No gap was found. The optimization retains the required roots and has
strict finite improvements; it is not a quotient induction. The result
does not supply a suitable neighbourhood in every critical graph, ensure
connectivity of a later quotient, or establish either global conjecture.
