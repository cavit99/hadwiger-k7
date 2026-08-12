# The second triangle response is shore-inert at the dominated component

**Status:** written proof; separate internal audit adjacent; and recorded
route nonclosure.  This is a conditional reduction inside the
eight-coordinate campaign.  It does not prove the `K_7^-` six-colour
conjecture or `HC_7`.

The model-aligned dominated-singleton theorem puts two exclusive equality
responses on one common deletion graph.  It is tempting to use the second
response to force the response component into one branch set of the fixed
exact model.  The first theorem below shows why this does not work at the
component's original boundary: the old-coordinate response is improper on
both shores.  The only way for the two responses to interact is therefore
through a Kempe transition between them.  Such a transition has an exact
host-level alternative, but it need not meet the fixed model portals.

## 1. The dominated response component

Let `G` be a graph which is not six-colourable.  Let

\[
                         e=uv,\qquad f=ux
\]

be two edges for which `vx` is also an edge, and put

\[
                            H=G-\{e,f\}.              \tag{1.1}
\]

Suppose that `Q` is a subgraph of `G[N_G(u)-\{v\}]`, that `v` is adjacent
to every vertex of `Q`, and that `A` is a connected vertex set of `Q`
containing `x`.  In the dominated-singleton application, `A` is a component
of `Q-S` for a cut `S` of order at most two.

Assume that `H` has proper six-colourings of both exclusive signatures

\[
 \begin{array}{c|cc}
       &e&f\\ \hline
 c_e&=&\ne\\
 c_f&\ne&=
 \end{array}                                             \tag{1.2}
\]

and restore both selected edges when discussing a restriction to a subgraph
of `G`.  Put

\[
                              T=N_G(A).                 \tag{1.3}
\]

### Theorem 1.1 (exact shore localisation)

The following statements hold.

1. Both `u` and `v` belong to `T`.  The edge `e=uv` lies wholly in `G[T]`,
   while `f=ux` crosses from `A` to `T`.
2. The colouring `c_f` is proper on `G-A` and induces a rejected exterior
   boundary partition on `T`.  It is not proper on the intact closed
   `A`-side `G[A\cup T]`.
3. The colouring `c_e` is proper on neither `G-A` nor `G[A\cup T]`.
   Consequently it induces no proper shore colouring, and hence no
   boundary partition, on either side of the separation at `T`.

In particular, the exclusive pair (1.2) supplies exactly one of the two
shore languages needed for a colouring comparison at `T`.  The second
response cannot be used directly to synchronise the two shores or to
constrain the placement of `A` in a fixed minor model.

#### Proof

Every vertex of `A` is adjacent to `u` by the definition of `Q`, and to
`v` by the domination hypothesis.  Since `A` is nonempty and contains
neither `u` nor `v`, both vertices lie in `T`.  Thus `uv` is an edge of
`G[T]`.  The vertex `x` lies in `A` and `u` lies in `T`, so `ux` crosses
the displayed separation.  This proves item 1.

After restoring `e,f`, the sole monochromatic edge under `c_f` is `f=ux`.
Deleting `A` removes its end `x`, so `c_f|G-A` is proper.  If its boundary
partition extended through `G[A\cup T]`, a permutation of colour names and
gluing would give a proper six-colouring of `G`.  The partition is therefore
rejected.  The intact closed side contains both ends of the monochromatic
edge `ux`, so `c_f` itself is not proper there.  This proves item 2.

The sole monochromatic restored edge under `c_e` is `e=uv`.  Both `G-A`
and `G[A\cup T]` contain `u`, `v`, and their edge.  Hence the restriction
of `c_e` is improper on both subgraphs.  Item 3 and the final conclusion
follow. `\square`

The conclusion is unaffected by spanningness of a minor model: spanningness
assigns every vertex to a branch set, but it does not turn an improper
restriction into a shore colouring or identify a colour class with a branch
set.

## 2. The only available interaction between the responses

Assume now that `G` is minor-minimal subject to not being six-colourable.
Then every proper minor is six-colourable.  The triangle `uvx` makes the
signature language of `H` exactly the two rows in (1.2): the all-proper
signature would colour `G`, and equality on both selected edges would give
the same colour to the adjacent vertices `v,x`.

Let `mathcal C_e` and `mathcal C_f` denote the two families of proper
six-colourings of `H` having the respective signatures in (1.2).  Join two
colourings when one is obtained from the other by one Kempe interchange.

### Theorem 2.1 (transition alternative with the `K_7^-` target)

Suppose in addition that `G` is seven-connected and has no `K_7^-` minor.
At least one of the following alternatives holds.

1. No Kempe component of the colouring reconfiguration graph meets both
   `mathcal C_e` and `mathcal C_f`.
2. There are `phi in mathcal C_e` and `psi in mathcal C_f` which differ by
   one Kempe interchange on a connected bichromatic subgraph `D`, and
   `N_G(D)` is the boundary of an actual separation of order at least
   seven.  The two colourings agree literally on this boundary and both
   induce the same rejected exterior boundary partition on `D`.
3. There is such a transition subgraph `D`, it is dominating in `G`, and

   \[
             \chi(G-D)=5,\qquad K_6^-\npreccurlyeq G-D.          \tag{2.1}
   \]

In outcomes 2 and 3 the transition has one of the two exact placements

\[
 u\in D,\ v,x\notin D,
 \qquad\hbox{or}\qquad
 v,x\in D,\ u\notin D.                                \tag{2.2}
\]

#### Proof

If no Kempe component meets both response families, outcome 1 holds.
Otherwise take a shortest Kempe-interchange sequence between them
and choose the first adjacent pair with different signatures.  The
critical-triangle transition theorem applies to `e=uv` and `f=ux`, with
outer edge `vx`.  It proves that the interchange uses the two colours on
the triangle and gives precisely the placements (2.2).

In either placement, `D` meets both possible monochromatic restored edges:
it contains `u` in the first placement and contains `v,x` in the second.
Thus both `phi|G-D` and `psi|G-D` are proper.  A Kempe interchange changes
no boundary vertex, so the two restrictions agree literally on `N_G(D)`.
If their common boundary partition extended through the intact closed
`D`-side, it would glue to either exterior restriction and six-colour `G`.
It is therefore rejected.

If `D` is not dominating, a vertex outside `N_G[D]` supplies a nonempty far
side.  Hence `N_G(D)` is an actual separator, and seven-connectivity gives
outcome 2.

It remains that `D` is dominating.  It is bipartite, being bichromatic.
If `G-D` were four-colourable, disjoint palettes of orders two and four
would six-colour `G`; hence `chi(G-D)>=5`.  If `G-D` contained a `K_6`
minor, the dominating connected set `D` would extend it to a `K_7` minor.
Hadwiger's conjecture for parameter six therefore gives
`chi(G-D)<=5`, so equality holds.  More sharply, a `K_6^-` model in
`G-D`, together with the dominating connected branch set `D`, would be a
`K_7^-` model in `G`.  This proves (2.1) and outcome 3. `\square`

The fixed spanning exact `K_7^vee` model in the aligned dominated-singleton
state remains the same family of branch sets throughout `H`; colour changes
do not alter it.  Theorem 2.1 does not, however, place `D` or `A` in one
branch set.  A bichromatic component can traverse several branch sets, and
the exact model gives no map from its six labels to the six palette colours.

## 3. Exact nonclosure of the portal argument

Let `J` be the fixed-model bag containing `x`, and for a foreign bag `D_i`
put

\[
                     \Pi_i=N_G(D_i)\cap J.
\]

The audited branch-bag criterion says that a captured subside exists
exactly when some component `W` of `G[J-x]` contains

\[
                         (J-A)\cup\Pi_i.               \tag{3.1}
\]

Condition (3.1) is uncoloured topology of the fixed branch sets.  Theorem
1.1 proves that the old-coordinate response supplies no shore colouring at
`N_G(A)`, so the two signatures do not compare boundary partitions there.
Theorem 2.1 exhausts the only generic way to relate the two response
families.  Its transition subgraph, when it exists, need not contain a full
portal set `Pi_i` or be contained in `J`; when it does not exist, the two
families have no Kempe transition at all.

Thus the inference

\[
 \begin{gathered}
  \text{one spanning exact model and the exclusive signatures }
  \{uv\},\{ux\}
 \end{gathered}
 \Longrightarrow
 \begin{gathered}
  \text{portal co-location (3.1), or a common partition at }N_G(A)
 \end{gathered}                                        \tag{3.2}
\]

is unsupported.  This is a route nonclosure, not a counterexample to
(3.2): a graph satisfying all critical-host hypotheses while refuting the
target conclusion would itself be a counterexample to the main conjecture.

The smallest repair must use one of the new objects in Theorem 2.1 rather
than the mere existence of the two signatures.  It must either align an
actual transition component with a full named portal set, eliminate the
dominating bipartite outcome in (2.1), or introduce an additional operation
whose colouring is proper on the intact `A`-side.  Further uncoloured
branch-set transfers cannot obtain this information.

## Dependencies and scope

- [dominated-singleton common-neighbour responses](../results/hc7_k7minus_dominated_singleton_twocut_response.md);
- [all-degree alignment with the fixed exact model](../results/hc7_k7minus_dominated_singleton_low_degree_terminal.md);
- [the exact branch-bag capture criterion](hc7_k7minus_component_to_bag_capture_gate.md); and
- [the critical-triangle transition theorem](../results/hc7_joint_persistent_incident_colour_fork.md).

Theorem 1.1 is elementary and Theorem 2.1 is a `K_7^-`-specific sharpening
of the cited critical-triangle alternative.  Neither theorem proves portal
co-location, bounds the transition separator above, eliminates the
five-chromatic complement in (2.1), or proves Conjecture 21 or `HC_7`.
