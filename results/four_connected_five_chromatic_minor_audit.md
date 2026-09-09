# Audit: a six-vertex minor in four-connected five-chromatic graphs

**Source:** [the theorem and universal-vertex corollary](four_connected_five_chromatic_minor.md).

**Exact source SHA-256:**
`5ae447797bd217f620c193cb30ef3da92519381461bb743d7f0abd4e337be9c9`.

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
