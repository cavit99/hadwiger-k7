# Second independent audit of the two-triangle complement

**Verdict: GREEN.**

Complete cold mathematical audit of the
[source](hc7_two_triangle_complement_four_connectivity.md), SHA-256
`0a75273d2270d5a675e3aa565610d47e375fa89e982b565fbd0ad4f4e5fd3b69`.
This is a separate internal audit, not external peer review.
Reversing only the promotion's status wording and input-link adjustment
recovers the cold-audited draft SHA-256
`5ab80c8c39c532f15f0a92d14b5a94319249776b9eb203bc76e4124049f21688`.

The packaged [separator input](hc7_two_triangle_separator_allocation.md)
matches SHA-256
`283444e901f18ec60f461eca91e158806a45e2b42394d6a87e5b54134c7b4b2b`;
its adjacent GREEN audit matches
`2ad4131413f9693ce8f233fafc6cc8f317c8185ebb3478ea08d59abf80ee8a29`.
The relevant side, minimal-torso and port arguments were reread. No fresh
literature inspection or finite enumeration is a proof premise.

## Strongest inference checks

Minimality concerns the order of the actual A-side, over all three-cuts
of `H`. The input therefore supplies the four-connected torso used here.
Choosing `t3` outside `A` retains all three A roots, including a possible
cut-root A vertex. The initial five-root model exists in the smaller side;
enlarging its ambient graph to `F*` and optimizing does not require the
deleted-root degree bound to hold for the newly available vertex `t3`.

Contact-leaf transfers preserve the allowed one-hole class and all literal
B-root edges. They leave the designated B bag singleton and each other
bag a root-to-port path with a unique common contact vertex. Unassigned
components miss the two-bag union. In the torso its external boundary is
contained in the two ports and `t3`; adding torso edges introduces only
the latter possible exit. Four-connectivity proves displayed (1), even
if `t3` already belongs to a bag. At most two A roots can be those ports,
so a T bag meets `v`.

The opposite bag is `O` itself: it avoids all of `F*`, meets `v`, and
contacts every retained B or T root. The full-core, two-contact and
unaligned-hole cases are therefore terminal. Any further A root outside
the T union must be a nonroot common B port. Its transfer to the deficient
T bag preserves the shortened root path, and the two possible lost edges
have different T and B ends. Thus all three A roots lie in `U`.

In `K-t3`, a flow cut of capacity at most two deletes at most two vertices
outside `V`, leaving an A source and the sink `t2` connected. Integral
flow consequently gives three paths, allowing shared V endpoints but
not shared ports. If an A root equals `t1`, its source capacity is still
one, and a virtual final edge may give the singleton prefix `{t1}`.
The only virtual edge is `t1t2`; it cannot be internal to a retained
prefix because `t2` is outside `U`. Growth uses actual edges of connected
`U`, including if it later assigns `t3`. Only the part containing `t1`
may lack an actual exit. The other two parts have distinct port exits
or actual V contacts.

For zero ports, the pigeonhole choice leaves at most one missing X-to-B
contact; if its B end is the designated root, the other merged bag
contacts that root. Otherwise the two possible holes are independent.
For one port, the shortened B path is nonempty, and its old last edge
retains its V contact. The two displayed alternatives exhaust the choices
of neighbours for the unaffected B bags; their respective possible holes
are exactly the two independent pairs stated in the source.
For two ports, one remains in its B bag. It simultaneously supplies the
X contact through its fan prefix and the Y contact through the old V edge.
The other port connects its A part to V and to its shortened B path.
The choice at the designated B root leaves only the displayed independent
holes. Every final bag retains its original root and has a fixed disjoint
connected preimage; no virtual edge supplies connectivity or a contact.

## Scope

No unresolved inference remains in the stated four-connectivity theorem
or its symmetric version. It uses the full structural hypotheses and
allows additional neighbourhood edges. It eliminates three-cuts of the
complement; it does not exclude the remaining neighbourhood configuration
or prove Conjecture 19 or the user's global objective.
