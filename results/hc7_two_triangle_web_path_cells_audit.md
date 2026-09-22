# Audit: a path in a web cell forces an apex planar graph

Date: 22 September 2026.

**Verdict: GREEN for the stated path-cell theorem and the conditional
Euler contradiction.** The reviewed
[source](hc7_two_triangle_web_path_cells.md) has SHA-256
`21d22e189e0cb1e0f5a536aec3267577645bc8c37af94a888dbb3f3098ae4e50`.
No unresolved gap was found in the implication that a cell meeting a
surviving path forces `J-z` planar for some `z in E`. This is a separate
internal reconstruction by a reviewer who did not write the argument,
not external peer review. The all-clean branch, the selected whole
six-chromatic case, the degree-seven case and HC7 remain open.

**Promotion provenance:** the independent reconstruction originally
reviewed the pre-promotion draft at SHA-256
`33b424a138f891afcbf46a4907f4b0e2835841227a59021825df8e7dade6b7b8`.
On 22 September 2026 the source and this audit were moved to `results/`.
The reviewer compared the promotion against the frozen original:
only proof-status wording, a heading and relative links changed.
The mathematical statement and argument are unchanged; the verdict
applies to the promoted hash above.

## Scope and external input

The audit takes the displayed finite simple graph partition as a
hypothesis: the whole induced graph `J-E` is the prism subdivision,
each path has nonempty interior, and `E` is nonempty and connected.
It also retains all three stated actual-boundary and contact hypotheses,
and the absence of a `K5` model whose five bags all meet `T`.
The derivation of that partition is the separately audited
[extremal prism theorem](hc7_two_triangle_extremal_prism.md);
its proof is not silently replaced or strengthened here.

The reviewer directly inspected Fabila-Monroy--Wood, *Rooted K4-Minors*,
[arXiv:1102.3760v1, Lemmas 2 and 7](https://arxiv.org/html/1102.3760v1).
Lemma 7 turns a linkage of opposite pairs on the specified actual cycle
into a rooted `K4`; Lemma 2 gives an ordered spanning web completion
when that linkage is absent. No connectivity premise is required for
these two lemmas. A rooted `K4` in `H_i` extends by the actual connected
fifth bag `R_i`: the two literal end triangles supply its contacts to
all four rooted bags. The nominated roots belong to the web skeleton,
and every actual component inside a cell has at most its three face
vertices as actual boundary. The external lemmas are used as inputs;
their proofs were not independently reproved in this audit.

## Reconstruction of the separator arguments

For a connected root-free shore with at most three neighbours in `H_i`,
meeting both surviving paths would require at least four distinct path
boundary vertices. Meeting one path forces a nonempty proper `E` part:
four `E` contacts rule out an empty part, while the four surviving roots
rule out containing all of `E`. Connectivity of `E` supplies an `E`
gate, leaving exactly two path gates and a single nonempty interval.
The `E` part is a union of components of `E-z`, so its complement is
connected through `z`. This applies to actual cell components and to
the later constructed complementary shore.

The full-ownership step retains actual disjointness. In the third view,
the first forbidden diagonal uses the prefix ending at the first
deleted-path contact, then the shore and the suffix of the owned path.
The other diagonal uses its opposite root, the connected complementary
`E` part and a suffix beginning strictly later on the deleted path.
Their rail segments and `E` parts are disjoint. The symmetric construction
uses the last contact. If either owned-path endpoint touched the
complementary `E` part, the open interval between the first and last
deleted-path contacts would have no such contact. Adding that interval
to the shore leaves at most the five displayed boundary vertices.
At least three distinct deleted-path contacts ensure this is a
nonempty root-free enlargement. The six-neighbour condition excludes
it, forcing both endpoint neighbour sets into the shore and its gates
to be the two end roots.

For overlapping `E`-only shores from different views, the intersection
has actual boundary in the union of the two boundary triples. Equality
is forced: the triples are disjoint and every member neighbours the
intersection. A gate outside the other shore and its deleted path would
belong to both triples. Consequently their union has no external `E`
neighbour and neither shore touches the third path, contradicting
connectedness and the contact hypotheses. This argument does not assume
that either `E`-only shore is connected.

Two shores owning the same path have an intersection containing its
interior with at most four boundary vertices. Each potentially deleted
path is forbidden as the third path by the other shore, so no contacts
are omitted from this count. For mutual ownership with intersecting
`E` parts, the union has at most one external `E` gate: the path inside
one shore plus its gate forces the other gate into that union whenever
necessary. The two path interiors then leave at most five neighbours.
For disjoint `E` parts, all deleted-path contacts are internal, because
the endpoints belong to the opposite ownership. These contacts force
each gate into the opposite `E` part; the union is then all of `E` and
misses the third path. Both cases give the stated contradiction.

The complementary component containing `I_k` has boundary in
`{p_k,q_k,z}`: there are no edges into `W`, and no contacts with `R_j`
outside `W` or `z`. The same shore theorem applies. Its `E` part is
disjoint from the first one and has the same gate. Thus any path-cell
shore in another view would give duplicate or mutual ownership.
The two other fixed views are therefore clean.

## Reconstruction of the planar gluing

In clean view `H_j`, a cell component intersecting `W_k union N` would
give a nonempty root-free intersection with boundary contained in its
three cell gates together with `z`. This count includes edges to the
rest of that cell: the only possible `E` edge leaving `W_k union N`
ends at `z`. There are no contacts to the deleted path. Hence all of
`W_k union N` lies in the skeleton; the symmetric assertion holds in
`H_k`. Cross-view disjointness of `E`-only cells puts `z` in at least
one of those skeletons. All surviving path vertices are in the
skeletons because those views are clean.

The strongest topological step is valid. In the skeleton disk of
`H_j`, the actual path `R_i` and the outer completion edge `p_iq_i`
bound a pocket. The other path `R_k` lies on the other side because
its endpoints are on the opposite outer arc and it avoids `R_i`.
The retained off-path graph `W_k union N union {z}` is connected:
every component of `E-z` has an edge to `z`. It has a contact with
`I_k`. It must therefore lie wholly on the `R_k` side of `R_i`.
The pocket contains no actual edge either. An edge with an endpoint
off `R_i` cannot enter it without crossing the boundary, and inducedness
of the prism excludes any additional edge with both endpoints on
`R_i`. In particular the outer edge `p_iq_i` is not actual.
Removing the unused pocket exposes the full actual path on the
boundary, while preserving the other two root positions. Delete `z`
after making this boundary argument.

The second patch is also valid even when `W_j` is disconnected: every
one of its components contacts `I_j`, so each lies on the nonpocket
side. Glue the two resulting disks along `R_i`, with opposite interiors.
Their outer boundary has cyclic root order

    p_i, p_k, q_k, q_i, q_j, p_j.

Thus the missing pairs `p_jp_k` and `q_jq_k` do not alternate. They can
be drawn in the exterior regions at the two endpoints of `R_i`.
The vertex sets otherwise are disjoint. Their actual edges cover all
of `J-z` except those two cap edges: `W_j`, `W_k` and `N` are unions
of different components of `E-z`; the forbidden contacts exclude all
omitted `E`-to-path edges; and the induced prism hypothesis excludes
extra edges among the paths. No gate edge or completion edge is used
as an actual edge in this construction. The Four Colour Theorem on
`J-z`, followed by a new colour for `z`, proves `chi(J)<=5`.

## Conditional Euler calculation and remaining obligation

Under the additional premise that every actual `H_i` is planar, its
connected off-cycle graph `E` lies on one side of the surviving-path
cycle. The induced prism supplies no cycle chords, so the other side
is empty and the whole cycle can bound the outer face. Its length is
`r_j+r_k`; disk Euler gives exactly the inequality in the source.
Summing it yields `3a+2d<=9e+2s-9`. The actual singleton degree bounds
give `2a+d>=6e`, and the stated root/internal contacts give
`d>=4s-12`. Their combination is
`3a+2d >= (3/2)(6e)+(1/2)(4s-12)=9e+2s-6`, a contradiction.
This verifies the implication with its planarity premise, not that
premise itself.

No proof is supplied for the remaining all-clean configuration.
In particular, disjointness of cells across views does not guarantee
cofacial gates or a compatible planar insertion of those cells.
There is no induction, quotient-criticality transfer or finite
computation in the audited path-cell argument. This audit establishes
only its unbounded conditional branch closure, not HC7 or the whole
selected critical-host case.
