# Independent audit of two-triangle complement four-connectivity

**Verdict: GREEN.** Separate cold mathematical audit of the complete
[source](hc7_two_triangle_complement_four_connectivity.md), at SHA-256
`0a75273d2270d5a675e3aa565610d47e375fa89e982b565fbd0ad4f4e5fd3b69`.
This is an internal audit, not external peer review or a global completion
claim. No finite enumeration is a premise of this verdict.

The original complete cold read pinned draft
`5ab80c8c39c532f15f0a92d14b5a94319249776b9eb203bc76e4124049f21688`.
Reversing only the promoted status wording and its one relative input link
exactly recovers those bytes. The GREEN verdict therefore applies to the
promoted source above; no mathematical change was made during promotion.

The packaged separator input was reread at its displayed source hash
`283444e901f18ec60f461eca91e158806a45e2b42394d6a87e5b54134c7b4b2b`;
its adjacent GREEN audit matches
`2ad4131413f9693ce8f233fafc6cc8f317c8185ebb3478ea08d59abf80ee8a29`.
The source uses its side structure, minimal-torso four-connectivity,
almost-clique existence and actual-port proof. It does not assume the
earlier source already excluded every three-cut.

The enlargement to `F*` preserves the original five prescribed roots.
Maximizing the two T bags and then minimizing the B bags is a valid
optimization in the allowed one-hole class. Distinct contact vertices
give a nonroot contact leaf whose transfer retains both B-to-T contacts
through the other port and old tree edge. The designated bag becomes
singleton; literal B-root edges retain every B-to-B contact. Absorbing
an unused component preserves all roots, including when it contains the
unprescribed vertex `t3`.

Every T-bag vertex lies in the actual torso vertex set. Its boundary in
that torso consists only of the two other B ports and possibly `t3`
from added T-clique edges. Four-connectivity therefore places every
outside vertex in this set. Choosing `t3` outside A forces an A vertex
into the two-bag union even if `t3` is `x` or `y`. The opposite component
alone is disjoint and full to the five prescribed roots and to `v`.
The full, unaligned and two-hit cases consequently are terminal. A
remaining A root outside the hit bag is a nonroot common B port; its
transfer to the unhit bag leaves only two independent core holes and
makes both bags meet `v`. This proves all A roots lie in the full bag
without imposing an extra constrained-optimization hypothesis.

For the fan in `K-t3`, a cut of capacity at most two deletes at most two
actual vertices or source roots. Some A source and the sink `t2` remain,
contradicting three-connectivity. V endpoints may be shared; non-V ports
may not. Source saturation and unit capacity keep the three A roots on
distinct prefixes. This also covers `t1` itself being an A source. After
first-exit truncation the only possible virtual edge is a final `t1t2`
edge, so no retained prefix uses a virtual edge. Growing a connected
partition of the actual bag preserves the prefixes. Naming the part
owning `t1` as `A0` retains its actual contact with the opposite component
and confines every possible virtual exit to that part.

All seven-bag contacts were checked in the three exit cases. With no
port exit, the at-most-once selection gives independent missing pairs;
if both candidate pairs involve `P0`, its selected contact fills one.
With one port, moving its nonroot leaf into V retains V's B contact
through the old path edge and can lose only that B bag's A contacts.
Both displayed subcases explicitly accommodate this loss. In particular,
the second uses the selected `Ai-P0` edge and retains all pairs except
possibly `X-P1'` and `v-V'`. With two ports, the untouched port stays in
its B bag, while only the other port enters `Y`. The old path edge
contacts the shortened bag; the retained port supplies both its required
contacts. The only possible holes are then `X-(Pj-pj)` and `Y-P0`.
Each shortened path is nonempty because a fan port lies in the torso
and hence is not its prescribed B root. No vertex or port is reused.

No unresolved mathematical gap was found in the stated four-connectivity
conclusion or its symmetric version. The hypotheses remain the stated
seven-connectivity, minimum degree eight, Q exclusion and spanning
two-triangle-plus-edge neighbourhood; extra edges are allowed and
proper-minor colourability is not required. The remaining global
two-triangle exclusion, Conjecture 19 and Hadwiger's conjecture for
`t=7` are not conclusions of this theorem.
