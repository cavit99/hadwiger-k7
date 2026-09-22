# Audit: exclusion of cutvertices in the prism remainder

Date: 22 September 2026.

**Verdict: GREEN for the stated cutvertex exclusion.** The reviewed
[source](hc7_prism_remainder_cutvertex_exclusion.md) has SHA-256
`dfe9546cf960a39eb6b87f1d18f70bc3ee8c4200e6b3e046a4bd81c2855ad42c`.
No unresolved gap was found in the planar projection, contact ordering
or actual separator counts. This is a separate internal reconstruction
by a reviewer who did not write the construction, not external peer
review. The scope strengthening in the final section was checked
independently before its incorporation into the promoted source.

## Revision and promotion provenance

The original reviewed source was
the pre-promotion draft, with SHA-256
`3572a0ce9056f13b9538a63afd18b76e203ae19254b675c5d101b691a56db351`.
That review separately established the replacement of `chi(J)=6`
by nonplanarity of every `J-z`, for `z in E`, as recorded below.
The only mathematical edit incorporated this already checked premise
and changed its two apex-planarity contradictions and the later reference
to the arbitrary-shore contradiction accordingly. The strengthened
active source had SHA-256
`fd4ace6380b3f0013d3786a41a7e9e2a851f6e9c2404dd2e7de62330ab2dd96b`.
Promotion to `results/` then changed only status/scope wording, relative
links and line wrapping. The reviewer inspected both diffs; the verdict
applies to the promoted hash above. No other construction was altered.

## Assumptions and the arbitrary-shore consequence

The argument retains the whole induced prism subdivision, its literal
end triangles, the connected nonempty remainder, five-connectivity of
`J`, the six-neighbour condition for every nonempty root-free set,
the two/four actual contact bounds and absence of a `T`-meeting `K5`.
The nonplanarity of every `J-z`, for `z in E`, excludes an apex-planar conclusion.
Every separator and linkage counted below concerns actual edges of `J`.

The claimed arbitrary-shore consequence follows from the already
audited [path-cell proof](hc7_two_triangle_web_path_cells.md).
Its ownership argument is stated and proved for any connected root-free
shore with at most three actual neighbours meeting a surviving rail.
The complementary shore uses precisely the resulting ownership
properties. Duplicate and mutual ownership then exclude path-containing
cells in the two other views; neither argument requires the original
shore to be a cell. Skeleton visibility and the final two-patch gluing
use those complementary shores and the two clean views. They therefore
give the same `J-z` planarity conclusion for this general shore.
No new containment or completion assertion is being assumed.

## The common-side projection and pocket

For a component `W` of `E-z` contacting only `R_i`, its actual boundary
is `z` together with its rail contacts. Hence it has at least five
distinct contacts. In either alternate view a nonempty intersection
of `W` with a whole cell has boundary in the cell's three actual gates
together with `z`; it has no contact to the deleted rail. The
six-neighbour condition excludes this intersection. Thus all of `W`
is visible. Cross-view cell disjointness also makes `z` visible in
at least one of these two views, which is the view subsequently used.

Projection of connected `E` onto its visible vertices is legitimate.
Every actual component inside a cell can reach a visible vertex through
an actual `E` gate. Projecting successive passages of an actual `E`
path uses only skeleton edges between visible `E` gates of a facial
triangle. The resulting auxiliary graph is connected and disjoint
from the actual two-rail cycle `D`; it therefore lies in one component
of the complement of that cycle. All its vertices and edges are on
the same side, rather than merely being individually drawable there.

The restricted projection of `A=E-W` uses only `A` gates. This follows
by taking an actual `A` path from the hidden component to visible `z`.
Its first gate still belongs to `A`. No hidden `A` vertex can contact
`W`, since the only external `E` neighbour of `W` is visible `z`.
Thus the connected projected `A` graph avoids every vertex of `W`.
For a hidden actual `A` neighbour of a rail vertex `t`, the same cell
has an `A` gate `h`, and its face edge `ht` represents that contact.
Here `h` is an `E` vertex and `t` is a rail vertex, so they are distinct.
The edge's interior lies on the established `E` side of `D`: it cannot
cross `D` and has its non-rail endpoint on that side. It also avoids
`W`. Multiple uses of auxiliary edges are harmless because this is
a planar drawing argument, not an extraction of disjoint actual paths.

An actual path from the first to the last `W` contact with interior
in connected `W` is a simple arc in this disk. Its union with the
closed rail interval bounds a pocket whose interior side at every
open-interval rail vertex is the only available disk side there.
The projected connected `A` graph avoids the arc and reaches the other
rail, so it lies on the other side of the arc. A represented contact
to an open-interval vertex would have to enter the pocket or cross
the arc, both impossible. This excludes actual `A` contacts there,
because every such contact has just been represented in the same
drawing.

Consequently the actual boundary of `W` together with the open rail
interval is contained in `{z,a,b}`. The extreme contacts account for
all edges leaving `W`; inducedness of the prism accounts for all
rail edges. The set is nonempty and root-free, even when an extreme
contact is a rail endpoint. The six-neighbour contradiction is valid.
This rules out every component at a cutvertex with only one rail type;
zero rail types already give boundary `{z}`.

## Attachment order and the actual cuts

The forbidden opposed inequalities give two actual disjoint diagonals:
connected `W` and connected `A` supply disjoint interior portions,
and strict inequalities separate the two portions on each rail.
They contradict the four-root linkage obstruction in the appropriate
path-deleted graph. On every common rail at least one strict comparison
exists because the two contact sets cover that rail and it has at least
three vertices. Opposite directions on one common rail would prohibit
both directions on any other common rail. Hence, when there are at
least two common rails, every `W` contact precedes every `A` contact
on all of them, or the reverse holds throughout. Equality can occur
only at their common boundary vertex. The use of the whole complement
`A` is essential and is retained in this proof.

If `W` contacts two rails but `A` misses one of them, `W` together
with that rail's interior is a connected root-free three-gate shore
in the other rail's deleted view. Its actual boundary is contained
in the two endpoints and `z`, so the arbitrary-shore consequence
applies. Otherwise the two common rails have a consistent order.
For a prefix ending strictly before the last `W` contact, every
included rail vertex has all its `E` neighbours in `W`. All `W`
contacts are either included or are these last contact vertices.
Thus the boundary of `W` and the two prefixes is contained in
`{z,b_i,b_j,p_k}`. If one prefix is empty, its cap root equals its
boundary vertex `b_h`, so the cap edge is still accounted for.
No far-end cap root belongs to a strict prefix. The surviving vertex
`q_k` lies outside this set and its displayed boundary. The cut has
at most four vertices, contradicting five-connectivity. Suffixes
give the reverse-order case with the same checks.

Every component of `E-z` must consequently contact all three rails.
Another component exists because `z` is a cutvertex; thus the chosen
component and its whole complement both contact all three. The three
prefixes have boundary contained in `{z,b_1,b_2,b_3}`. Cap edges either
stay among included cap roots or end at a boundary root of an empty
prefix. A vertex of the other `E-z` component remains outside both
the selected set and the boundary. The resulting actual cut again
contradicts five-connectivity. No completion edge enters either cut.

## Independently checked strengthening to both chromatic branches

**Strengthened statement now incorporated.** The promoted theorem
replaces the originally reviewed hypothesis `chi(J)=6` by nonplanarity
of `J-z` for every `z in E`, retaining all other hypotheses.
Then `J[E]` still has no cutvertex.

The only uses of `chi(J)=6` in the original revision were to exclude a
path-containing cell and to exclude the arbitrary three-gate shore.
Both arguments first conclude that `J-z` is planar for some `z in E`.
The replacement hypothesis contradicts that conclusion directly.
Neither the projection nor the ordered-cut arguments use the chromatic
number. This proves the strengthened statement without any additional
connectivity or degree assumption.

In the original critical host, let `J=G-{u,r}` and let `z in E`.
The extremal prism remainder avoids the neighbourhood of `u`, so
`u` and `z` are nonadjacent. If `J-z` were planar, the Four Colour
Theorem would colour it with colours 1 through 4. Give `u,z` colour 5
and `r` colour 6. Every vertex of `G` is now coloured properly,
contrary to `chi(G)=7`. Thus the strengthened premise holds independently
of whether `chi(J)=5` or `chi(J)=6`. The normalisation's ordinary `K5`
input already follows from `chi(J)>=5` in that original-host setting;
the cutvertex proof requires no six-chromatic quotient or inherited
criticality. The two-separator and whole-cell insertion obligations
remain separate from this cutvertex exclusion.
