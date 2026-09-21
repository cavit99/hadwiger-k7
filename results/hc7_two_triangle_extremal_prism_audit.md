# Audit: extremal prism normalisation

Date: 21 September 2026.

**Verdict: GREEN for the whole stated structural reduction and its
critical-host consequences.** The reviewed
[source](hc7_two_triangle_extremal_prism.md) has SHA-256
`8d617e35d5bc6fac0f25b5f418c6f35e976d282d883401199084e15c6d258222`.
No unresolved mathematical gap was found in those statements. This is a
separate internal reconstruction by a reviewer who did not write the
proof, not external peer review. The exceptional neighbourhood case,
the full degree-seven case and HC7 remain open.

## External input

The reviewer directly inspected Costalonga--Zhou, *Triangle-roundedness
in matroids*, [arXiv:1711.01618v3, Theorem 4](https://arxiv.org/html/1711.01618v3).
Its graph statement requires three-connectivity, a specified literal
triangle and an ordinary K5 minor, and retains the three original
triangle edges as a triangle in a K5 minor. All hypotheses hold here.
Retaining those edges forces the three original P vertices into distinct
connected branch-set preimages: identifying two would make their edge
a loop. This input is an external theorem; its proof was not independently
reproved in this audit. No existing local GREEN verdict was used as a
substitute for reconstructing the new argument.

## Strongest checks

- **Initial singleton bags.** A minimal tree joining the root and two
  distinct helper-contact vertices has a contact leaf other than the
  root. Moving that leaf preserves both helper contacts and every
  root-bag adjacency through the literal P edges. At a maximum, each
  root bag has one actual vertex neighbouring the helper union; unused
  components touching that union can also be absorbed. Those at most
  three actual vertices form a separator unless all remaining vertices
  are precisely the three roots. The initial spanning partition follows.

- **Four-connectivity and projections.** Claim 1 treats a contact at a
  Q vertex separately: its transfer gives a forbidden model rather than
  an admissible larger partition. Each shadow has one block projection.
  For the union Z of unselected projection regions, every external
  neighbour is either a selected gate or an unlocalised P vertex.
  The bound is therefore `|Gamma|+3-|L|<=3`, not a sum of unrelated
  contact counts. Nonempty E survives outside this cut. Consequently
  the Q block has exactly three vertices, and all three root-neighbour
  sets have distinct projections.

- **Components and induced paths.** A component at qi without a pi
  neighbour has no P contact and, by Claim 1, no E contact; its boundary
  is only qi. A component with no E contact has boundary contained in
  `{pi,qi}`. An E contact forces all D-neighbours of pi into its own
  component, proving uniqueness. In the resulting endpoint graph, every
  E-contact vertex separates pi from qi. An off-spine branch has boundary
  one, and the interior of a non-edge spine block has boundary at most
  two. Projection ownership excludes additional external neighbours in
  both arguments. Thus the conclusion concerns the entire induced graph,
  not merely a chosen prism subgraph.

- **Original-host application.** Deleting u,r leaves a five-connected
  graph of chromatic number at least five, so the established K5 case
  of Hadwiger supplies the ordinary minor. A T-meeting model lifts
  directly by adjoining the singleton bags u,r. A root-free set with
  at most five J-neighbours would have at most six G-neighbours and
  would be separated from u. This proves the actual contact bounds
  used later. For a root-free vertex x, the final reference to J-x is
  also justified: a four-colouring of J-x extends by giving u,x a fifth
  colour and r a sixth. Hence J-x still contains an ordinary K5 minor
  and is four-connected; its new normalisation need not match the old one.

- **Colouring consequences.** Three colours extend across each vertical
  path of length at least two after colouring the two triangles.
  Disjoint palettes on that prism and F, with u sharing an F colour
  different from r, prove `chi(F)>=4`. A bipartite E would make F
  three-colourable by giving r a new colour. The stated five-colouring
  of G/E is valid because u has no neighbour in E; no lift is inferred.

- **Non-cut exchange and locality.** Removing qi from D leaves exactly
  the two components asserted. The two contacts of x reconnect them;
  the surviving helper retains qi and all P contacts because each root
  has at least two actual E-neighbours. The symmetric exchange uses
  Q-fullness, not an unproved symmetric maximality. In the locality
  move, every transferred internal vertex keeps at least three
  neighbours in connected E-x. Replacing the path interval by y-x-z
  preserves the complementary connected P-full part, retains Q, and
  increases E strictly. No induced-path property is required of this
  comparison partition. The connected-set extension explicitly states
  the additional connectivity and contact hypotheses it needs.

- **Root-only exchange.** For the added five-bag construction, the first
  bag retains contacts through actual neighbours in E-x; among the
  other four bags, the six required contacts are the displayed P edge,
  the last edge of R1, three Q edges and xp1. All five bags are connected,
  disjoint and contain distinct original triangle roots. Hence a
  root-only contact set meeting both triangles can contain only a matched
  pair. The locality exchange also applies to that pair: its proof does
  not require an existing interior contact of x. The resulting bound of
  three prism neighbours combines with the root-free degree bound six
  to give degree at least three inside E. No conclusion about connected
  sets or rooted minors within E is inferred.

## Exact limit

The proof supplies an extremal induced prism and necessary restrictions
on its actual contacts. It supplies neither a final T-meeting K5 model
nor a recolouring of the critical host. In particular, it does not make
the connected-set exchange automatically admissible, compare different
normalisations, or establish a decreasing induction. The source makes
none of those stronger claims. No computation is a premise of this audit.
