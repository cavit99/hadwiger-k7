# Audit: the double-contact wheel terminal and its weaker patterns

**Reviewed sources:**

- [Positive construction](hc7_sealed_wheel_terminal.md), SHA-256
  `3036409fbf1cb23b826185e56d8381962575370bf323d5efdac59092fb7c6c01`.
- [Counterexamples](../barriers/hc7_weak_wheel_terminal.md), SHA-256
  `6d99e559b22a93cc22dd2dc71b75c30d969913c33f18b8a56e54ac88b053625e`.

The original combined draft had SHA-256
`b3a85ae59a6aaaa2d587a383439fa609ce2d7b179bb538e011ddaf405524de5a`.
Promotion separated the positive and negative sections, updated their
status lines and added navigation. Reversing those changes and rejoining
the original sections reproduces that exact combined hash. The initial
split counterexample source had SHA-256
`40dd5b6e0dc0d82ef1fcacd8103f6f3766e1001d15b6ce7d4ce62f1aa7cbd675`.
Section 4 was subsequently added and separately checked at SHA-256
`0675b014a15e9cf4143d6709ba4bba260a0f48d73165de08f43ab0760de9204d`;
Removing only its pending-audit sentence gave SHA-256
`78945cb2d1861eb293611b80022507f805fd8ccba6337568b965155ea026c815`.
The current source additionally narrows the final application wording:
the exclusion concerns extra edges in the fixed six-bag core, while
constructions inside or splitting its preimages remain possible. This
scope correction changes none of the proofs and was separately checked.

**Verdict:** GREEN — separate internal whole-source audit. The positive
construction, both negative examples and their Section 4 strengthenings
are proved at these bytes.
No unresolved mathematical gap was found. This is not external peer
review or a completion claim for the actual critical-host problem.

## Provenance and scope

`literature_repair` wrote the source, including the conceptual positive
proof, six-orbit certificates and both written negative proofs. The parent
independently explored positive finite placements beforehand.
`route_assessment` independently read and checked this complete source,
including the exhaustive negative cases. The reviewer worked on the
separate ambient wheel-extraction problem, but did not develop this source
or its certificates. The verdict below uses the written arguments, not
an unreported search or a failed solver query.

`literature_repair` also wrote the Section 4 completion strengthening.
`route_assessment` independently checked its two explicit decompositions
and the whole-model clique projection before clearing its pending status.

The positive conclusion concerns nine disjoint connected sets with the
listed contacts. The counterexamples concern the exact weaker abstract
contact patterns; they do not satisfy the actual host's connectivity,
minimum-degree or critical-colouring assumptions.

## Positive construction

The two stated symmetries preserve every required contact. Their six
wheel orbits have sizes `1,2,2,4,2,4`, summing to all fifteen labelled
wheels. Each row's contracted edges is present, the two contractions
have disjoint endpoints, and the displayed seven preimages have only
the indicated two possible independent holes.

The uniform proof independently removes any reliance on the table.
After relabelling, `vq,qb,pc` are wheel edges: the hub and rim cases
give the required matching as stated. Minimum wheel degree three
then forces both v and q to contact `{p,c}`. For the seven bags
`d+b,p+c,v,q,r,s,t`, the d+b bag contacts q through bq and p+c through
dc; its other contacts use the listed d-edges. The p+c bag contacts
v,q through the forced wheel edges and r,s through p. The v bag is
full to r,s,t, q contacts r,t, and r,s,t form a triangle. Thus only
`(p+c)t` and `qs` can be missing, with distinct endpoints. All unions
are connected by actual edges and retain disjoint original preimages.
Additional contacts do not invalidate the construction.

## Nine-vertex negative example

The graph has exactly 23 edges. Its three degree-four vertices are
b,c,q; all other degrees are at least five. Any seven-bag minor uses
seven, eight or nine vertices. Omitting a vertex loses at least four
edges, and the additional required vertex reduction loses at least
one more; two omissions also satisfy this bound. Hence a minor with
the 19 edges required by Q must use all nine vertices. Edge deletions
cannot improve this upper bound.

A singleton degree-four vertex cannot acquire five distinct bag contacts
by contracting other bags. Therefore b,c,q must all lie in nonsingleton
bags. The only possible size distributions are one three-vertex bag
or two edge bags:

- The three-vertex bag must be `{b,c,q}`. Its two internal edges,
  two duplicate v-contacts and one duplicate contact each to p,d
  account for six lost edges, leaving 17.
- With two edge bags, one contains two of b,c,q. Since bc is absent,
  symmetry makes it `{b,q}`. The other is `{c,z}` with
  `z in {p,d,v}`. The bq contraction loses its edge and its one
  common-neighbour duplicate, namely v. In the resulting graph the
  c-p and c-d contractions each lose three edges, while c-v loses
  four. The final quotients have at most 18 edges.

These cases exhaust connected branch sets on nine vertices, including
arbitrary mergers of the named vertices. Thus the negative conclusion
is an exact proof, not merely a check of contractions preserving labels.
The additional edge vq is already present in this example.

## Eight-vertex negative example and limits

The vertices b,c are nonadjacent and both have exactly the neighbours
`{v,s,q,d}`. A seven-bag minor permits only one vertex deletion or one
edge contraction. A deletion leaves at least one of b,c singleton.
A contraction could absorb both only along the absent edge bc.
Consequently a degree-four singleton survives in every case, excluding
Q. The listed edges vs and vq are indeed present.

## Completing each six-vertex core

For the first completion, the intersection `{v,p,q,d}` is a literal K4.
The seven-vertex side has precisely the holes `pt,qr,qs`, hence 18 edges;
it cannot contain a seven-vertex Q minor, which requires 19 edges. The
other side is K6 and cannot supply seven bags. No edge joins the two
open sides. In the second completion the two stated sides are both K6,
their intersection `{v,s,q,d}` is a literal K4, and again the union is
exactly the specified completed graph.

The projection checks arbitrary branch sets. At most four Q bags meet
the four-clique. The other bags represent a connected graph, since Q
minus at most four vertices is a complete graph minus a matching on
at least three vertices. They therefore all lie in one open side.
Restrict each clique-meeting bag to that side and the clique. Every
retained piece reaches a clique vertex within its own bag, and the
bag's clique vertices reconnect it using actual clique edges. A lost
contact between two such bags is restored between their distinct clique
vertices. Contacts with a clique-avoiding bag already lie in the retained
side. Thus Q in the union would give Q in one of the two original sides,
contradicting the preceding order or edge counts. No general clique-sum
theorem, contraction search or virtual edge is assumed.

This proves failure even after every possible edge inside the indicated
six-vertex core is added. It consequently covers every partial completion
there with the same triangle contacts. It does not exclude using further
actual vertices, splitting previously chosen bags or changing which bags
own the triangle contacts.

The source therefore validates the two-double-contact terminal and
refutes the two weaker abstract terminals even with completed cores. It
does not show
that either counterexample occurs in an actual seven-connected,
minimum-degree-eight critical host. The new relative wheel theorem
supplies no missing contacts in these negative patterns. A global
construction or colouring argument is still required for those actual
states and for C19, HC7 or the stated NT-comparable objective.
