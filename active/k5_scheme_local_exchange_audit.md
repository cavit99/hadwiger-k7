# Audit: the local foreign-colour exchange

**Verdict: GREEN.**

Audited source: [the local exchange](k5_scheme_local_exchange.md), SHA-256
`22a7d73f7c0235384baeb6855d5766678aae1a7b9a8fbee6974d4c4bd011624b`.
This is a separate exact-file internal review, 8 September 2026. The
auditor previously checked the author's triangle special case and the
ten-vertex barrier; this review additionally checks distinct same-coloured
other neighbours, the complete reduction and the host-class consequence.
It is not external peer review.

Each nonroot path membership needs a nonroot neighbour. Edge-disjointness
and nonroot degree two therefore force exactly two memberships at each
of x,y, with a prescribed root as the other neighbour in each membership.
Properness at xz and yw makes their common colour different from both
colours of x,y, even when z and w are distinct actual vertices. This
forces the displayed entire alpha--beta path and both gamma-root edges.

The two root preimages are connected, disjoint and contain no foreign
root. Their three actual contacts replace all demands using x or y.
Every other demand avoids both absorbed vertices, so its root images
and endpoint colours survive. Discarding unused edges is legitimate;
the conclusion does not require every quotient edge to be properly
coloured. Host order drops by two, and fixed connected preimages give
the stated root-preserving lift.

The consequence for graphs whose cyclic blocks are triangles is valid.
That host class, allowing isolated vertices and bridges, is minor-closed.
After any root-preserving normalization the graph outside the new roots
is a minor of the previous nonroot graph. Minimum nonroot degree two
then provides a leaf triangle with two degree-two vertices whenever
nonroots remain. Repeated normalization and exchange strictly decrease
host order. The normalization source and audit hashes printed in the
source were checked exactly: `07fa0fc5...` and `f3b8137a...` respectively.

The ten-vertex calibration gives the claimed five bags. The different-
colour obstruction in the last section correctly identifies contacts
lost by this particular exchange; it does not claim a counterexample
to another exchange. No gap was found in the stated lemma or its host-
restricted consequence. Full K5 contractibility and the global research
objective remain open. No finite computation is a proof premise.

The preceding review first covered source `0cadb6d6...`. The final
revision adds the different-colour terminal, updates its status, and
states the common-endpoint intersection condition in the opening raw-
scheme definition. The auditor caught that omitted clause on the second
read; the earlier properly coloured lemma inputs already implied it,
but the raw-scheme normalization consequence required it explicitly.

The added terminal is GREEN at the final hash above. It was first checked
with a literal beta--epsilon edge at revision `0058c209...`; the auditor
then proposed the epsilon-root expansion, which the author separately
checked before this exact-file review. The beta bag is connected and
literally full to alpha, gamma and delta. The first-contact repair is simple
and avoids that entire bag and every foreign root. Its borrowed suffix
avoids the three demands independent of beta--gamma and meets the other
two only in gamma, establishing the raw scheme condition for arbitrary
intersecting collections. Under the stated suffix-avoidance hypothesis,
the full repaired path misses E=P(beta,epsilon)-r_beta. E is a connected
root preimage, disjoint from the beta bag and all non-epsilon demands.
The epsilon demands enter it at old epsilon-coloured vertices; first-entry
truncation preserves the raw scheme condition and all four prescribed
roots. After lifting a rooted K4 model from this same quotient, the initial
beta--epsilon path edge gives the beta bag its fourth required contact.
This uses no independently chosen model or unowned path segment.
The K4 input follows from the recorded KM Theorem 7 applied to K4 plus
an isolated root after normalization. Its source and audit hashes were
checked exactly: `8cac1bbf...` and `92814588...`. The full-K5 theorem is
not used. A literal beta--epsilon demand satisfies the avoidance condition
automatically. Removing that avoidance hypothesis, or treating general
different-colour exchanges, remains expressly unproved here.
