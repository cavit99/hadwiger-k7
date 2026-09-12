# Audit: a six-vertex minor in four-connected five-chromatic graphs

**Source:** [the theorems and universal-vertex corollary](four_connected_five_chromatic_minor.md).

**Exact source SHA-256:**
`92627c08e88c8e067c34d6865afa939f349545f694f8691c1b4d2e682bc9cfd7`.

**Current verdict: GREEN.** The original review is preserved below; the
added prescribed-singleton theorem has the separate new review at the end.

## Preserved original-source review

**Original source SHA-256:**
`5ae447797bd217f620c193cb30ef3da92519381461bb743d7f0abd4e337be9c9`.

The following review, through “External inputs and limits”, concerns only
that original source. Its reviewer is not attributed the later addition.

**Verdict:** GREEN — separate internal whole-source audit. No unresolved
mathematical gap was found at this revision. This is not external peer
review or a novelty or comparative-significance assessment.

## Scope and provenance

The reviewer, `universal_proof`, independently checked the proposed
deduction and then read every line of the final source. The deduction
was proposed by `literature_repair` and assembled by the parent. The
reviewer previously contributed to the wheel-extension input; that
contribution and its separate review are disclosed in its adjacent audit.

The following input pins were checked against the actual files:

- [Wheel-extension source](hc7_rooted_wheel_extension.md):
  `f72e0b3d4254724a58f55b9445c0c173ea6c96e535416da47b1efc7fd5eb43b3`.
- [Wheel-extension audit](hc7_rooted_wheel_extension_audit.md):
  `c93612165de23798c63922425fbd8d9e74407d2eb1a85b365853bd1343969178`.

## Strongest checks

- A vertex-minimal induced non-four-colourable J is connected, has
  chromatic number exactly five, and every J-z is exactly four-chromatic.
  No connectivity of J or J-z beyond connectedness of J is imported.
- If J is K5, H has an exterior component because its order is at least
  six. A boundary of at most three leaves a surviving clique vertex and
  contradicts four-connectivity. The resulting six bags have at most one
  missing contact and therefore contain Q6.
- If J is not K5, Brooks gives a vertex with at least five neighbours
  in J. Every four-colouring of J-z uses all four colours on those
  neighbours, since otherwise it extends to J.
- Martinsson–Steiner supplies four distinct neighbour representatives.
  A fifth exists. The wheel theorem applies in the ambient H-z, which is
  three-connected; it explicitly allows the fifth root inside the initial
  K4 model. Thus no unused-root or induced-core connectivity assumption
  enters the proof.
- All five wheel bags retain actual neighbours of z and avoid z.
  Adding its singleton bag gives exactly K1 join W4 as a required
  subgraph of the contact graph, namely Q6. Extra contacts are harmless.
- In the corollary, universality gives chi(H-u)=5 and contacts from u to
  all six returned bags. The fixed seven bags therefore give Q7.

## External inputs and limits

The reviewer inspected Brooks' original statement on the rendered first
page, p. 194, of [the cited paper](https://doi.org/10.1017/S030500410002168X).
It allows parameter n>2, maximum degree at most n, and excludes a
K_(n+1) component. Setting n=4 gives precisely the statement used here.
The exact Martinsson–Steiner Theorem 1.3 statement and set-rooted
definition were checked through Section 7 and the primary-source review
recorded in the pinned wheel audit; no prescribed representatives are
assumed.

This is an unbounded, nonrecursive deduction, not an induction that must
retain four-connectivity after taking a critical subgraph. No finite
search is a dependency. The general five-connected six-chromatic target,
Conjecture 19, HC7 and an NT-comparable completion remain unproved here.
The result does not prescribe contacts of a Q6 model to a nonuniversal
outside vertex.

## Independent review of the prescribed-singleton addition

**Verdict: GREEN**, 12 September 2026, for source SHA-256
`92627c08e88c8e067c34d6865afa939f349545f694f8691c1b4d2e682bc9cfd7`.
The reviewer, `marked_state_falsification`, independently checked the
addition proposed by `exterior_joint_model`. Removing only the Lemma 3.1
input and the prescribed-singleton section recovers the original source
hash above. Its proof and universal-vertex corollary are unchanged.

The reviewer freshly inspected Martinsson–Steiner's
[primary Lemma 3.1 and definition of spread](https://arxiv.org/html/2209.00594v1#S3),
including their definition of a separation. The lemma requires a
three-connected graph, at least four marks, and a mark on each open side
of every separation of order three. Absence of a set-rooted K4 then
makes the graph with an added vertex adjacent to those marks planar.
No colouring hypothesis or prescribed choice of four marks is required.

Here H-z is three-connected and has at least five vertices. If its
three-separation (X,Y) had no S vertex in Y-X, then deleting X intersect Y
from H would leave that nonempty side without an edge to its complement,
which still contains z. This contradicts four-connectivity. The symmetric
argument supplies the other open side. Since S is the full neighbourhood
of z, the lemma's augmented graph is exactly H. Thus nonplanarity forces
the required S-rooted K4 for each specified z of degree at least five.

Choose one S representative in each of the four disjoint bags and a
fifth distinct S vertex. The pinned wheel source and audit hashes were
rechecked and match the preserved input pins. Its stated theorem expressly
allows this fifth root inside an initial bag, so no unused-root assumption
is made. All five returned bags lie in H-z and contain distinct neighbours
of z. Its singleton bag contacts every one; K1 join W4 is Q6. This even
makes the prescribed singleton universal in the resulting contact graph.

For the consequence, a nonplanar Q6-minor-free four-connected graph has
minimum degree four and, by this theorem, no degree above four. Hence it
is four-regular. This is a necessary alternative, not a claim that every
four-regular graph is Q6-minor-free. No unresolved gap, finite-check premise
or unproved lift was found. This is internal review, not external peer
review; novelty remains unassessed, and HC7 or NT-comparable completion
does not follow from this addition.
