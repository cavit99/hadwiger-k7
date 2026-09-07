# Internal audit: companion rooted-helper constructions

**Verdict: GREEN.** Theorem 1, Corollary 2, Lemma 3, Proposition 4 and
the stated supporting deductions are valid at the revision below. This is
a separate internal mathematical audit, not external peer review or a
proof of Conjecture 19, Conjecture 21 or `HC_7`.

**Audited source:** [rooted helpers](hc7_companion_helper_construction.md)

**Whole-source SHA-256:**
`0c1ac8052f7734d8d0267381c030e177bd70010eded63d15fdca8c0db6d1f375`.

The mathematical text was first checked at
`dd0d2086e9efb52618d241100e37698a0697dde95e206493f8e6f0a5a31a6c60`.
The final revision clarifies that helpers intersect `S`; adjacency alone
would not suffice. This audit is deductive, without finite enumeration.

## Input and missing-contact calculation

The cited [rooted-helper source](../results/hc7_k7minus_degree7_rooted_helper_closure.md)
matches its adjacent audit at SHA-256
`6ffee04cf9ff66275f9674c24bc2b9c669b1e108b76e5b1d2a18ec7d0106fe67`.
Its exact rooted bound, fifth-root lemma and critical minimum-degree bound
are the inputs used here. The primary literature was not freshly inspected
during this audit.

Deleting `v` from the six-connected host leaves a five-connected graph,
and the displayed density becomes `e(F)>=4|V(F)|-9`. There is a fifth
neighbour since `d(v)>=5`. Each literal edge joining two roots survives
between their prescribed bags. The only possible missing pairs
are one root-root pair and `v` with the helper lacking the fifth root;
they are independent. All seven bags are disjoint and connected.

Companion-minor exclusion implies `K_7^-`-minor exclusion, so the audited
critical corollary gives minimum degree eight. For a literal `K_5^-`,
its three vertices adjacent to the other four satisfy `d(w)>=q+14`
by the strict integer contrapositive of Theorem 1. Their nonnegative
degree-surplus contributions already exceed the total `2q`. This proves
the asserted subgraph exclusion, including neighbourhood diamonds.
For the independence bound, contracting `v` with four independent
neighbours allows those neighbours to share the contracted colour on
expansion. The other four neighbours use at most four colours, leaving
a sixth colour for `v`. This verifies the stated contradiction.

## Maximal helpers and actual separator ownership

In Lemma 3, maximizing helper order and then minimizing root-bag order
are finite choices. If a root bag has two distinct helper-contact
vertices, one can choose distinct contacts to the two different helpers.
A minimal tree through its root and these contacts spans the bag by
secondary minimality. A contact leaf different from the root can move
to its helper: the remaining tree stays connected, its old tree edge
retains that helper contact, and the other contact remains. Roots never
move. This contradicts maximal helper order.

An unused component touching a helper could likewise be absorbed. Thus
the helper union has at most four actual external neighbours, one in each
root bag. If any nonroot lay outside the helper union, its complement
would have more than four vertices. Deleting those at most four neighbours
would leave both the nonempty helper union and another vertex, separated
in `F`. Five-connectivity forbids this. The complement is exactly `Z`,
so the root bags are singleton roots and the helpers partition `F-Z`.
No nonliteral root-root contact is required to survive this optimization.

In Proposition 4, both helpers must contain neighbours of `v`. They then
form, with `v`, a triangle complete to the four cycle-root bags, giving
`K_3 join C_4`. For the edge alternative, `a,b` lie in the first helper,
and the second lies in one component `W` of `J-{a,b}`. Its four root
contacts remain in `W`. If `W` avoided `S`, it would have no edge to `v`;
deleting the six distinct vertices `Z union {a,b}` would separate `W`
from `v`. Seven-connectivity therefore forces `W` to intersect `S`.
Connectivity of `J` supplies an edge from `W` to `{a,b}`. The latter is
connected, disjoint from `W`, and contacts all four roots by hypothesis.
These are actual original-host bags, with every root retained.

## Remaining obligations

No gap was found in these statements. The final degree and connectivity
bounds follow by the stated vertex deletions. Existence of a suitable
four-cycle in every surviving neighbourhood, or a general redistribution
of the four remaining neighbours between the two helpers, is unproved.
The finite optimization in Lemma 3 is not an induction proving either
global conjecture; no such completion is claimed.
