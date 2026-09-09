# Audit of the five-root two-exception theorem

**Verdict: GREEN — separate internal audit of the complete written proof.**
No mathematical gap or source correction was found. The theorem supplies
one admissible triangle endpoint, not the two endpoints available in
the unrestricted degree-six theorem.

## Exact source and provenance

The reviewed source is [the five-root proof](hc7_five_root_two_degree_five_exceptions.md),
SHA-256 `bc2e20127d1c614e4567bc50e49137bbe00087d2eee333f454ba8fa7902382c9`.
Route-assessment independently read the whole draft after its
construction and did not develop or edit this extension. This is
internal review, not external peer review. No finite search is a premise.

The inherited argument and its exact audit were read and hash-checked:

- [Degree-six source](../results/hc7_five_root_degree_six.md):
  `289c5ad015b6c392ea69e8e26e15eba54b4eba7cb155789edd76b3dbb5c9f9a4`.
- [Its audit](../results/hc7_five_root_degree_six_audit.md):
  `6f13ffd37126c78a697b5752574fe06b6fd13b68dabb0d63e4e39d76a8f1d065`.

The recorded Norin--Totschnig Theorem 8 statement and audit were also
read and checked at `de183e350c412739c05a744e811304454ba90856efee9e097813c70617bba9cd`
and `dc7db3d391ef2701516d64dd32e7546d40e2e4171406193f17d8feadcc4abb47`.
This uses their recorded primary inspection, not a fresh literature check.

## Strongest checks

1. **The bad two-nonroot endpoint is exact.** With no nonroot edge,
   both nonroots see all roots. With that edge, degrees at least five
   allow at most one missed root per nonroot, and the boundary condition
   forbids the same missed root. The displayed positive assignments
   cover a universal nonroot, a missed helper, and every possible
   helper--triangle edge. In the remaining configuration a singleton
   helper would need both nonroots in distinct triangle bags; both
   helpers would then miss the third triangle bag. Otherwise each
   helper owns one nonroot and the two holes have different triangle
   endpoints. Neither arrangement is admissible. Every root in this
   exceptional graph has degree at most four.
2. **Exceptional endpoints of contractions are handled.** Surviving
   nonroot degrees and boundaries are unchanged under both stated
   contractions. A bad endpoint after a single absorption uses both
   degree-five exceptions on the survivors; the absorbed vertex had
   degree at least six, leaving a merged root of degree at least five.
   For the simultaneous transfer with four original nonroots, a bad
   endpoint similarly forces both absorbed vertices to have degree at
   least six, but the absence of helper--triangle edges bounds them by
   five. With three original nonroots, the last vertex is full to the
   triangle and both others. It has degree five, so one absorbed vertex
   has degree at least six; the displayed two helper bags are connected
   and adjacent and miss at most one triangle contact. All labels,
   the root triangle, and disjoint lifting preimages are retained.
3. **The inherited port argument needs no degree-six assumption.**
   For an inadmissible root, a helper contact to it is already terminal.
   If another rooted bag has two helper ports, a minimal tree through
   its root and suitable distinct ports has a nonroot port leaf that
   can be transferred. The literal retained triangle edge preserves
   the other rooted-bag contact. Maximality then leaves at most two
   actual ports and no unused component meeting the helpers. Their
   nonroot interiors have boundary at most four in the original host,
   so are empty and force the excluded common-two-neighbour case.
   The trisection exclusion likewise uses only the internal-four bound,
   normalized roots and the literal edge between the retained triangle
   roots. Thus degree-four vertices after deleting a triangle root do
   not invalidate either exclusion.
4. **Three planar responses give the stated contradiction.** The root
   normalization and internal-four condition prove actual
   two-connectivity of each response. Facial subtraction gives
   `e_D+K-k_u<=3|D|+1`, including when `h>4`. Combined with
   `2e_D+K>=6|D|-d`, this gives `2k_u>=K-d-2`. Summing for all three
   inadmissible triangle roots yields
   `K_B+3(k_b+k_c)<=3d+6<=12`, while normalization makes the same
   expression at least eighteen. All inequalities refer to the same
   original graph; the drawings need not coincide.

## Scope

The class requires at least three nonroots, degree at least five with
at most two exceptions to degree six, and boundary at least five for
every nonempty nonroot subset. Only one admissible endpoint is proved.
The stated full-R four-cut application still lacks the required
boundary-five condition: three deletions guarantee only four. This
audit does not license that application, a second endpoint, an iterable
critical-host reduction, or completion of C19 or HC7.

Promotion to `results/` changed only the source status line and audit link;
its mathematical body is byte-identical to the reviewed draft at SHA-256
`a24d7910a3deb740bd23c9f5a9c097f50104b34a4820a4c2d96fcf3c431aeb20`. The current source hash above includes that editorial change.
