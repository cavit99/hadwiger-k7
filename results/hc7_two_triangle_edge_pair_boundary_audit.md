# Internal audit: an exterior four-boundary containing x and y

**Verdict: GREEN.** The complete theorem holds at the exact revision below.
This is a separate internal mathematical audit, not external peer review
or a conclusion that the two-triangle case is closed.

**Audited source:** [edge-pair boundary exclusion](hc7_two_triangle_edge_pair_boundary.md).

**Whole-source SHA-256:**
`7a6661db23b0364ea03a23cf1b9e5112fc024bb57930a6b4197e801b7e8ebfe3`.

Promotion changed only status and relative links; reversing those substitutions
recovers frozen source SHA-256
`64d15b39e1cfb6e3b6b31943c6a44cfc44cbea05a04ac1526b66e495aaae4a62` exactly, so the mathematics is unchanged.

## Inputs and provenance

The reviewer did not author this proof and cold-read the complete frozen
source. The following source and audit hashes were checked against disk;
the invoked statements and adjacent audits were read:

- [Complement four-connectivity](hc7_two_triangle_complement_four_connectivity.md):
  `0a75273d2270d5a675e3aa565610d47e375fa89e982b565fbd0ad4f4e5fd3b69`;
  [audit](hc7_two_triangle_complement_four_connectivity_audit.md):
  `d074cc7eb384222f1b68ed53728fd721c7a6e7edbf266c55cec313a5c73b2014`.
- [Degree-six five-root theorem](hc7_five_root_degree_six.md):
  `289c5ad015b6c392ea69e8e26e15eba54b4eba7cb155789edd76b3dbb5c9f9a4`;
  [audit](hc7_five_root_degree_six_audit.md):
  `6f13ffd37126c78a697b5752574fe06b6fd13b68dabb0d63e4e39d76a8f1d065`.

This reviewer also supplied the earlier degree-six input audit. The present
review checks its new application independently; no fresh literature
inspection or finite computation is a premise.

## Strongest checks

A component D0 of the proposed D has no neighbour in another D component,
so its H-boundary is contained in the same four-set C. A survives outside
D0 and C, licensing four-connectivity and equality of the boundary.
After this replacement, the actual component Z containing the literal A
triangle avoids D and C. Its H-boundary is contained in C, with D still
outside; hence it contacts every member of C. Its G-boundary is contained
in the eight actual vertices C, B and v. Seven-connectivity forces at
least seven of these contacts. Together with its four C contacts and
the v contact, this means at least two distinct B contacts.

For each nonempty X within D, v survives outside X and its G-boundary.
Thus that boundary has size at least seven. Every D neighbour is in
D, C or B, so forming the actual induced graph F deletes only p and q.
Both the degree-six and every-subset boundary-five hypotheses hold;
no minimum-degree or connectivity assertion about a contracted graph
is used. The five roots are distinct and the nonroot set is nonempty.

The set of admissible B centres and the set of B roots contacted by Z
each have size at least two, so they intersect. Choosing a centre in
that intersection ensures that Z's possible missed B bag differs from
the centre of the core's possible hole. The extra bags Z and {v} are
disjoint from the fresh F model. Literal root contacts supply every
claimed extra edge, including v-Z. The two possible missing pairs
therefore have four distinct bag ends; extra edges only help.

**Scope and gaps.** No gap was found. D need not initially be connected,
and no earlier minor model is reused. Chromatic criticality is unnecessary.
Other exterior boundaries and the global construction remain open.
