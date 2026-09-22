# Conjecture 21: completed rooted-density construction

**Status, 21 September 2026:** written proof with two separate hash-pinned
internal audits. Every finite `K7^-`-minor-free graph is six-colourable.
The [research ledger](../RESEARCH_LEDGER.md) gives the current significance
assessment. HC7 remains open; internal audits are not external peer review.

## 1. Changed external input

Dvořák, Norin and Rahman, *Every graph with no K7= minor is 6-colorable*,
[arXiv:2609.17760v1](https://arxiv.org/html/2609.17760v1), submitted
15 September 2026, state:

- Theorem 1.1: every `Q=K7-2K2`-minor-free graph is six-colourable.
- Theorem 1.3: every five-connected graph of order `n>=6` with
  `e>=4n-7` contains Q.
- Theorem 1.6: a minor-minimal non-six-colourable `K7^-`-minor-free graph
  is seven-connected and has `e>=4n-2`.

Their first theorem resolves Conjecture 19. Their density theorem directly
excludes our former remaining host: seven-connectivity implies
five-connectivity, minimum degree eight gives `n>=9` and `e>=4n`.
No neighbourhood or exterior-colouring case remains for that application.
These are external preprint results. The statements and this implication
have been inspected; we have not independently reconstructed their whole
proof. They are not our own completion of the user's objective.

## 2. The completed theorem

The [global proof](../results/hc7_k7minus_bilight_extremal.md),
[first audit](../results/hc7_k7minus_bilight_extremal_audit.md) and
[second audit](../results/hc7_k7minus_bilight_extremal_second_audit.md)
establish that every 4-bilight graph on `n>=3` vertices with `e>=4n-2`
contains `K7^-`. In particular this proves Dvořák–Norin–Rahman Conjecture
1.5 for five-connected graphs. Their Theorem 1.6 then gives C21.

The new construction has two parts.

1. The [rooted helper theorem](../results/five_root_one_missing_contact.md)
   gives five prescribed-root bags and two root-free helpers with at least
   ten of eleven possible contacts involving a helper. It holds at rooted
   four-density two in every 4-light five-rooted graph, without an order
   bound. Its reductions preserve all roots and fixed disjoint preimages;
   padding is used only to select a fragment. This part is computation-free.
2. The global proof eliminates degree-five vertices and all five-cuts of
   a minimum density counterexample. A low-density fragment contains a
   low-triangle edge; consistent orientation makes an inclusion-minimal
   such fragment an unrestricted end. A new local end lemma gives the
   contradiction. The resulting six-connected graph has only high-triangle
   edges, and the degree-six and degree-seven terminal arguments finish.

The degree-seven step uses an
[elementary nine-vertex lemma](../results/hc7_k7minus_degree7_quotient_hand_proof.md),
with a [separate internal audit](../results/hc7_k7minus_degree7_quotient_hand_proof_audit.md),
together with a written reduction from arbitrary host order. Five maximal
complement types and explicit models replace the former 232-case
computational premise; its original proof and verifier remain preserved.
The [earlier helper probes](hc7_c21_helper_search_findings.md) are not proof
inputs. The [working draft](../archive/hc7_c21_global_composition_working_2026-09-21.md)
preserves the superseded routes; it is not the audited final proof.

## 3. Barriers remain valid

- A [boundary-star replacement](../barriers/five_root_star_replacement.md)
  can preserve density and destroy lightness. The final argument proves
  admissibility of its particular operations instead.
- [Density one](../barriers/five_root_helper_completion.md#1-the-density-one-extension-fails)
  does not force the ten-contact rooted model. The global end argument
  excludes those obstructions in a minimum counterexample.
- [Arbitrary density](../barriers/five_root_helper_completion.md#3-arbitrary-density-does-not-force-all-eleven-contacts)
  cannot force all eleven contacts. This blocks a direct strengthening
  of the rooted theorem to complete helpers.
- Independently selected helper models can yield `K_{2,2,2,2}`, without
  `K7^-`; the [working draft](../archive/hc7_c21_global_composition_working_2026-09-21.md)
  records that exact model-composition obstruction. The final proof does
  not rely on arbitrary such composition at six-cuts.

The [former six-cut frontier](hc7_k7minus_sixconnected_4n_sparse_threecut_frontier.md)
is now historical. Its global target follows from the new theorem; its
stronger local placement assertions are not automatically proved.

## 4. What remains towards HC7

C21 guarantees a seven-bag minor with at most one missing adjacency in
every non-six-colourable graph. HC7 requires all 21 adjacencies. Completing
that contact while preserving disjoint connected bags remains unproved.
A density-only version of the new theorem cannot supply the last step:
two universal vertices joined to a five-connected plane triangulation give
seven-connected `K7`-minor-free graphs with `5n-15` edges, as noted in
Dvořák–Norin–Rahman's introduction. Their chromatic structure must matter.

The complete [C21 manuscript](../paper/k7minus-six-colour/main.pdf) now
includes the supporting constructions and exact proof dependencies, with
a [separate internal audit](../paper/k7minus-six-colour/main_audit.md).
External review and historical priority remain outstanding. No author
contact has been authorised, and no particular HC7 construction follows
automatically from this theorem.

The next discovery focus is the actual minor-minimal non-six-colourable
`K7`-minor-free host: combine its proper-minor six-colourings with a changeable
`K7^-` model to obtain a `K7` model or a valid colouring lift. This is an
HC7-level construction obligation, not a proved reduction to a small local
case. The density-only and all-eleven-contact barriers above remain in force.
The old `K7^-`-minor-free critical-host degree, clique and defect restrictions
cannot be transferred to this larger class. The separate `3,2,2`
[seven-cut colouring theorem](../results/hc7_k7minus_three_component_seven_cut_exclusion.md)
can be reused only when its actual connectivity and boundary hypotheses hold.

**Selected checkpoint — conjectural:** every seven-connected graph `G`
with `chi(G)=7`, every proper minor six-colourable, and a degree-seven
vertex contains a `K7` minor. This would exclude an entire unbounded case;
it would not settle HC7. A hypothetical minimal counterexample has a
vertex of degree seven, eight or nine, by Mader's connectivity and edge
bounds; see [Rolek–Song, Theorems 1.8 and 2.1](https://sciences.ucf.edu/math/zxsong/wp-content/uploads/sites/13/2018/04/Coloring-graphs-with-forbidden-minors.pdf).

The [existing degree-seven programme](hc7_degree7_model_separator_frontier.md)
already supplies a connected exterior, proper-minor colourings realising
every single repeated neighbour pair, and rooted five-bag models. Its
global compatibility step is still open. For `S=N(u)`, the construction
must produce either a `K7` model or a six-colouring of `G-u` using at most
five colours on `S`; the latter extends to `u`. Choose the repeated pair,
colouring and rooted bags together. More fixed-model responses or a fresh
enumeration of neighbourhoods do not close this checkpoint.

Use the [actual boundary-aligned edge response](../results/hc7_low_degree_boundary_edge_alignment.md)
as a common-host witness, subject to its precise hypotheses. The
[selected-response barrier](../barriers/hc7_degree7_single_edge_response_alignment_barrier.md)
and [reversible rotations](../barriers/hc7_near_k7_rotation_involution_barrier.md)
exclude the old shortcuts. Keep the original critical host fixed; a
quotient supplies a colouring, not inherited criticality. Any recursive
construction needs a proved decreasing parameter and both colouring and
minor lifts. No such completion mechanism is presently established.

### Current construction and its limits

The [recolouring calculation](hc7_degree7_colour_repair_working.md), with
a separate internal audit, works with all six-colourings of one actual
edge-deletion graph. For an interior edge it identifies every endpoint
connection requiring `u` and gives a coupled interchange that can remove
all such exceptions. A single endpoint repair is precisely the reverse
of the earlier separating-edge move; it is not a decreasing reduction.
Even the strengthened singleton-root incidence does not suffice:
the [ten-vertex selected-layer counterexample](../barriers/hc7_degree7_selected_colour_layers.md)
has a written width-five certificate. It lacks criticality and seven-
connectivity, so the full construction remains possible.

**Working boundary-edge refinement.** For `h=sv`, with `s in S` and
`v in C`, the same interchange argument gives at most one exceptional
connection: the equality colour already occurs at `s`. An exception
forces a repeated pair `{s,t}` with `t in N_F(s)-N_G(v)`, where
`F=overline{G[S]}`. If `d_F(s)=2`, there are at most two companion roots.
Moreover `D=N_C(s)` contains an edge: otherwise `{u} union D` is an
independent subset of `N(s)` of size `|D|+1`, contrary to Dirac's bound
`alpha(G[N(s)])<=d(s)-5=|D|`. Thus the chosen boundary edge can belong
to an actual triangle through `s`. These restrictions do not synchronise
its different edge responses. The missing construction is one collection
of four disjoint connected core bags meeting both endpoint components and
retaining the boundary contacts to `u`. Separate colourful-set models
do not supply that collection; zero exceptional connections is not an exit.

**Concentrated attack:** the entire six-chromatic branch of the
`K_{3,3} dotunion K_1` complement case, detailed in the
[two-triangle construction](hc7_degree7_exceptional_construction_working.md).
Write `N(u)=P dotunion Q dotunion {r}`, with two triangles `P,Q` and
`r` adjacent to all six roots. A `K5` model in `G-{u,r}` whose bags all
meet `P union Q` finishes with singleton bags `{u},{r}`. This placement
is sufficient, not compulsory. The target is a complete construction
in the original critical graph; all seven bags may change.

The current case assumes `chi(J)=6`, where `J=G-{u,r}`. It retains
seven-connectivity and all proper-minor six-colourings of `G`, and places
no restriction on the order, root-ownership pattern or initial `K6` model.
Hadwiger's theorem for six supplies that model. The existing two-bag and
two-singleton constructions are terminal cases of the attack, not
extra assumptions. The missing step is a joint reassignment using the
actual colouring responses, or a direct `K7` construction. A theorem
about arbitrary five-connected graphs is not required. The branch
`chi(J)=5` remains open but is not receiving parallel discovery effort.

The [extremal prism reduction](../results/hc7_two_triangle_extremal_prism.md)
now supplies an exact representation if that rooted model is absent.
It applies already in four-connected graphs with an ordinary `K5`
minor and two anticomplete triangles. Maximising one connected helper
forces its complement to be an induced subdivision of the triangular
prism. Every original vertex is retained. In the actual critical graph,
each triangle vertex has at least two neighbours in the helper `E`,
and each path interior vertex has at least four. Moreover `G[E union {r}]`
requires at least four colours. Explicit exchanges confine every non-cut
vertex's prism contacts to one end triangle or a segment of at most two
edges of one path; its degree inside `E` is at least three.

The missing step is extending this exchange through vertices with no
path-interior contact and through separations of `E`, while retaining
the complementary helper's connectivity and all root contacts. A proposed
exclusion of three-connected `E` omitted these vertices and is withdrawn.
No induction or case closure follows from the representation. The
construction keeps the original colouring responses available; it does
not assume that a contracted helper or another extremal choice inherits
them.

The [contraction and colouring attack](hc7_degree7_exceptional_construction_working.md#8-what-the-contraction-attack-establishes)
now forces a triangle around a root with exactly two helper neighbours
and proves exact colouring lifts for a path owning a root. Contracting an induced
three-vertex path retains the prism theorem's premises, but can leave
the owned-root configuration inside the smaller helper. Mandatory Kempe
moves on both triangles, obtained using bipartite contractibility, are
also reversible. The unresolved construction must retain the complementary
connected set's contacts while rerouting or splitting it; neither fewer
quotient vertices nor a change of repeated pair establishes descent.

The subsequent [three-owner construction](hc7_degree7_exceptional_construction_working.md#9-a-construction-for-some-three-owner-patterns)
excludes a common root missing an independent pair of the four-vertex
path, and handles the minimal remaining contact sets when deleting the
root pair leaves a five-chromatic graph. The six-chromatic branch forces
an ordinary `K6` minor. The [two-bag construction](hc7_degree7_exceptional_construction_working.md#10-a-six-clique-model-using-two-remainder-bags)
turns any such model with exactly two bags entering `E` into the required
rooted `K5`, for arbitrary subdivision lengths. The stronger
[two-singleton construction](hc7_two_triangle_six_chromatic_working.md)
now finishes if just two vertices of either triangle are singleton in
the `K6` model. It uses the whole graph after deleting those two vertices,
allows arbitrary remaining bags, and covers every placement of the other
triangle. When all three of its roots lie in one bag, three choices of
helper pair give nested actual cutvertex shores; their incompatible
boundary restrictions force a linkage. It subsumes the previous
[singleton-triangle case](hc7_degree7_exceptional_construction_working.md#11-three-helpers-when-the-first-triangle-is-singleton).
Its four-colour deletion application also finishes if deleting a triangle
edge's ends leaves a four-colourable graph. These are working proofs,
without separate audits, and do not close the whole six-chromatic branch.

**First unresolved step in the extensions.** In a general `K6` model, a
part of a root bag can carry its only contacts to two helpers. Moving it
to one helper loses the other contact. Retaining only one singleton root
leaves routing cuts containing whole helper bags and up to two actual
vertices; the cutvertex nesting above no longer applies. Six disjoint
paths from `T` to chosen model representatives do not fix this: they can
enter other bags first. The stronger actual boundary condition has not
yielded a split preserving every required contact. These are route
nonclosures, not counterexamples to the desired construction.

The colouring attempts retain the same unresolved compatibility issue.
Minimising the size of the `r`-colour class gives five-colourings after
its deletion, with `T` using all five colours. Proper-minor colourings
can use fewer colours on `T`, but their restrictions need not agree with
those five-colourings. Contracting a triangle edge in `G` gives a
six-chromatic proper minor, yet does not make the relevant pair deletion
in `J` four-colourable. Across an actual
seven-cut, a colouring of a contracted shore likewise need not lift
through that shore. A valid joint recolouring or a simultaneous bag
reassignment remains possible; no decreasing transition has been proved.

The [intact-helper barrier](../barriers/hc7_prism_intact_helper_barrier.md)
rules out repairing root ownership solely after contracting two connected
pieces to single vertices. Its four-connected eleven-vertex graph has an
extremal helper and contacts from both pieces to all three paths, but no
`K5` model whose five bags all meet the triangles. It fails the stronger original-host
connectivity and contact bounds. A valid repair must retain those bounds
and the pieces' internal splitting choices.
The new two-bag construction has the additional premise of an explicit
`K6` model; the barrier does not refute this stronger statement.

Deleting the whole `r`-colour class from any six-colouring of `G-u`
gives a five-chromatic graph in which the six roots are colourful in
every five-colouring. The [new marked-minor reduction](../results/hc7_two_triangle_colourful_reduction.md),
with [separate internal reviews](../results/hc7_two_triangle_colourful_reduction_audit.md),
either finishes the model or reduces this pair to four-connectivity.
It covers all separators of order at most three, decreases vertex order,
and preserves the original marks in fixed disjoint preimages. Five
surviving marks finish by the existing rooted-certificate theorem; six
retain two literal triangles, with cross edges allowed.

The four-connected construction remains unproved and is an optional
stronger target, rather than the required next theorem. This reduction
handles both chromatic values of `G-{u,r}` but closes neither branch. Taking a
minimum `r`-colour class does not force a usable connector: the class may
be `{r}`. Paths from different Kempe colourings can reuse a vertex while
representing independent demands, so they do not automatically form a
bipartite scheme. The existing first-hit helper transfer can lose a
required triangle contact. The needed repair remains a simultaneous
choice of all five bags or a valid recolouring of the original host.

Two proposed reductions also remain invalid. Minimising arbitrary
seven-cut shores selects the original singleton `{u}`, without a terminal
construction. Contracting a connected fibre and using its quotient
colouring does not give a colouring lift. Closing an edge fibre under its
equality colour and the colour of `u` can reach another protected root;
if the endpoint connection closes inside the fibre, restoring the edge
creates an odd cycle and defeats the proposed two-colour lift.
A repair must preserve the required boundary partition and prove either
a colour extension or a strictly decreasing, liftable construction.
