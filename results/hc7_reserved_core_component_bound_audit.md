# Internal audit: connectedness behind the reserved-core ports

**Verdict: GREEN.**

**Audited source:** [the connectedness proof](hc7_reserved_core_component_bound.md).

**Whole-source SHA-256:**
`b02d2c88ebf4879b45e36031d9bf9b7ac0722d8c7302a26d7637d8ba3fcf0e3c`.

## Review and revision provenance

This is internal mathematical review, not external peer review. The
literature-repair reviewer contributed to the reserved-core input and an
invalid earlier connectedness argument, which was explicitly retracted.
Route-assessment wrote Proposition 1 and Corollary 2; literature-repair
independently reviewed their complete sources. Literature-repair wrote
Lemma 3 and Corollaries 4--5; route-assessment independently reviewed each
exact addition. The final Theorem 6 was developed by the parent and
route-assessment and written by route-assessment. Literature-repair checked
its proposed models, then read the complete changed source independently.
The parent also reported a complete review. Independence from the preceding
discussions is not claimed; authorship is separated from each scoped audit.

The previous audit is preserved at Git `0cd445f`. Its successive reviewed
source revisions were:

| Revision | Exact source SHA-256 |
| --- | --- |
| Original mathematical draft | `88f5f0804d28a09df192028839950f873c9f5d280eb7198c5572f8543355f791` |
| Historical-input clarification | `c363f4a2bbc1085fa8f4ba42393590e3f1ef2ba46eb584b19dce38c5a9949481` |
| Status/link-only promotion | `ac959b373ace3a6421d21a232f83d1caca5d408f7fbe42a3b5803e5c346874fb` |
| Corollary 2 append | `2434ad0bd10fa2805d134956c26e160524f63c851d18b6bf33139da9bb1f59e4` |
| Lemma 3 and Corollary 4 append | `953bed9c9bddc805c51819f1355e9deb535c6b5824186f6ab130ea877b9abec9` |
| Corollary 5 append; Git `0cd445f` | `2371cf108769929f459eff213047714762e4c05f2d183ebcfe00a4fec47296e2` |

The earlier exact reversals retain their recorded provenance: promotion
changed only status and two links; the preceding clarification added one
historical-revision line; later revisions appended their stated sections,
with the recorded b-omission scope sentence corrected alongside Corollary 4.
For the present revision, removing Theorem 6 and reversing only the title,
status, opening conclusion and Proposition 1 label byte-recovers Git
`0cd445f` exactly. All earlier proof bytes are unchanged.
The complete new draft was read at
`1ca57726076c1d0b9b85cdaad3fdb85956fb67e8af1af30681c9e0dd2930b212`.
Its final changes merely made the relabelling in the case split explicit
and replaced the pending-audit status. The final source was rechecked.

## Inputs

The frontier and scoped audit at historical Git `7bbcacb` were checked
against their source pins
`a7b7289d3e090414824b6d67b9abd5d456aadb765a2245bff3991c5783d6f5ea`
and `bd435dc374da1b58ba39ee77aa8f0414abf6245f51a2f287dbede3f8558148b8`.
They supply actual common ports, b's contact with U, nonempty D, and all
five H contacts and at least two B contacts for each component. They
supply neither connectedness of D nor a colouring of M.

The four direct source/audit pins also match: contraction closure
`ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4` /
`26b2f5ad7226c7bb3f194cac8523f043d7ae6ca955036249f04ddc9fb6d94394`,
and the four-root packet
`b3fe07ea52e0e553c61edb59cd5b7da3719ae834d8803f21afb9bde90fc410a8` /
`e9bc147d6c0e48bba395dc5fe590ef8a8cc778914804e3c1f5d33c48e2eec628`.
The invoked statements and packet proof were reread in the earlier scoped
reviews. No fresh primary-source inspection is claimed.

## Earlier deductions retained

**Proposition 1.** The two initial extra bags are disjoint, connected,
adjacent and full to the five core bags. In the first case the missing
contacts have distinct component and B ends. In the second case the
component absorbing Bi obtains its Bj contact from the literal B edge;
only a--Bj can be absent. In the last case the interior of the old
Bi--pi path is one connected set in a D component adjacent to Bi, and
therefore avoids all three selected Bi-missing components. Its endpoints
also avoid them, including for a single-edge path. The replacement extras
then yield seven disjoint clique bags. This explicitly repairs the old
path-reuse failure rather than assuming D connected.

**Corollary 2.** A Bi missed by both components also misses M, so its
eight listed possible neighbours are all forced by minimum degree eight.
The va contraction excludes a vertex seeing all of a,x,y. The fresh
four-root host loses at most two neighbours per vertex and at most three
boundary vertices per nonempty set; v remains outside to license the
original seven-neighbour bound. The extras M, C2+a, v+Bi are disjoint
and adjacent. The last uses the specifically forced Bi--p1,p2 edges;
M alone may miss the Bj core bag. No old path is retained.

**Lemma 3 and Corollary 4.** Thin-root and paired-root absorption preserve
surviving degrees and boundary cardinalities, with four separate root
preimages and strictly fewer nonroots. The one-exception condition excludes
orders one and two, including reduction endpoints. The same small-cut,
trisection and two-connectivity arguments apply; the cofacial degree-sum
gap remains at least five for every h. Two vertices seeing all a,x,y give
a literal K5-minus after va contraction, so there is at most one such
vertex. For a component missing b, the fresh packet consequently meets
the exact single-deficit hypotheses. Its port bags enlarge the same U,V
in the same deletion, preserve all four prescribed roots and add both
ports to M. Old B paths and any earlier colouring of M are discarded.

**Corollary 5.** Both fresh hosts have that same degree/boundary guarantee.
They meet only in b,p1,p2. Discarding both b bags leaves intersections
only between equally labelled port bags, whose unions are connected.
The four Bi--port contacts and the port--port contact survive; literal
B1B2 supplies the sixth. The same strict enlargement preserves the four
original roots. Thus, if there are two components, at least one is B-full.

## Final connectedness construction

**Theorem 6: separate exact-source verdict GREEN.** If either component
misses a B root, call it C1. Corollaries 4--5 identify the missed root
as Bi and make C2 B-full. The fresh core inside
`C1 union {b,Bj,p1,p2}` satisfies Lemma 3 because only a,x,y are removed.
The extras U, V+v+Bi, C2+a are disjoint and connected. Their triangle
uses U--V, a's U contact and av. U contacts b and both ports;
V+v+Bi contacts both ports through V and b,Bj through v;
C2+a contacts all four roots through C2. There is at most the single
U--Bj omission. In particular this proof does not assume Bi contacts
either port: V supplies those contacts.

If neither component misses B, the bags C1+p1, C2+p2, B1, B2 form
a rooted K4. The component--port edge C1--p2 gives their mutual contact;
the other five contacts use fullness and literal B1B2. Appending the two
port bags to U,V preserves disjointness, connectedness and the original
four roots, and strictly enlarges the defining maximum M. Neither case
retains an old B-root path. The two cases are exhaustive after the explicit
relabelling, and Proposition 1 plus the input's nonemptiness gives connected D.

## Scope

The nonroot-port residual set is now proved nonempty and connected.
Allocating that connected set and handling two root ports remain open;
the theorem does not prove the two-triangle case, C19 or HC7. No finite
computation or new external theorem is used as a mathematical premise.
