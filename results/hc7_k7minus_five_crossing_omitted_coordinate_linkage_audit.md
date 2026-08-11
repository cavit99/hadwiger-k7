# Internal audit: omitted-coordinate linkages in the five-crossing row

**Verdict:** GREEN for Theorem 2.1, including the sixteen partial-transversal
cuts, the connectivity-six response, the common coordinate assignment, the
rooted join minor and the neighbourhood `K_5^-`-minor exclusion.  This is a
separate internal mathematical audit, not external peer review.

## 1. Exact revision and checked dependencies

The audited source is
[`hc7_k7minus_five_crossing_omitted_coordinate_linkage.md`](hc7_k7minus_five_crossing_omitted_coordinate_linkage.md),
with SHA-256

```text
43a42468dc9616936971300ca5869988bc7f1de4019b5956d5a23d105e286315
```

The promoted inputs were checked at these source revisions:

```text
d0d3aa3574d747a3164f29febff1fa8fd6f37b0899415cd97a515005c5de5f43  hc7_k7minus_five_centre_common_matching_reduction.md
1041988a33b749bef5802dd21d3cd9419b5afc754735a20174bf5a13c0a56c96  hc7_k7minus_three_component_seven_cut_exclusion.md
26bae59cab6b6023207dd5400c093e5a54e4e30b9abff91f3f5ab78bf039c41f  hc7_k7minus_four_crossing_signed_boolean_reduction.md
```

Each has an adjacent GREEN internal audit.  The common-host theorem supplies
the five-crossing no-descent row and the component-size bound.  The
seven-cut theorem is invoked in the connectivity-six branch.  The signed
Boolean theorem supplies the antecedent coordinate argument, but the
present proof correctly repeats it because its four-cubes lie in the five
different graphs `G-e_i`.  No finite computation is used.

## 2. All sixteen partial-transversal cuts

Fix `i`, put `J_i=G-e_i`, and choose one end of each of the other four
matching edges.  Covering those four edges, deleting `e_i`, and using that
`H-S` has components `A,D` prove that there is no edge between the two
displayed residual sets `A_X,D_X`.  Their orders remain positive because
each original component has order at least six and at most four vertices
are selected.

For a nonextreme choice, extending by `d_i` is mixed and proves that `A_X`
is connected; extending by `a_i` proves that `D_X` is connected.  The same
argument covers one side in each extreme:

- if all four selected ends lie in `D`, then `A_X=A` is connected by the
  definition of the original component, while extension by `a_i` is mixed
  and proves connectivity of `D_X`;
- if all four selected ends lie in `A`, the symmetric argument uses
  `D_X=D` and extension by `d_i`.

Thus neither unmixed five-edge transversal is being assumed full.

A mixed extension supplies both contacts for every vertex of `S`.  If a
selected endpoint lies in `A`, extension by `d_i` is mixed and supplies its
home-side contact, while its unselected matching mate supplies its
`D_X` contact.  The argument is symmetric for an endpoint selected in
`D`.  Hence every one of the sixteen sets `Q_X` is a literal order-seven
separator of `J_i` with exactly two full components.

## 3. Connectivity and the exact response

If at most five vertices separated `J_i`, restoring the single edge `e_i`
would have to connect all components because `G` is seven-connected.  A
single edge can do this only when there are exactly two components and its
ends lie in different ones.  At least one component is nonsingleton;
otherwise `|V(G)|` would be at most seven.  Adding the incident endpoint
from a nonsingleton component to the proposed cut removes the only restored
cross-edge and leaves vertices on both sides, producing a separator of `G`
of order at most six.  Therefore `\kappa(J_i)\geq6`.  The sets `Q_X` give
the upper bound seven.

When `\kappa(J_i)=6`, the same single-edge argument applied to a six-cut
`R` gives exactly two components of `J_i-R`, with the two ends of `e_i`
outside `R` and in different components.  Choose the end `p` whose
component is nonsingleton.  Then `T=R\cup\{p\}` is a proper seven-cut of
`G`: the other endpoint component remains, and deleting `p` leaves a
vertex on its original side.  The audited seven-cut theorem gives exactly
two full components.

Every six-colouring of `G-e_i` gives equal colours to the deleted-edge
ends, since otherwise it would colour `G`.  If `C` is the component of
`G-T` containing the other end, deletion of `C` removes the only possible
improper restored edge.  An extension of the exact boundary colouring
through `C` would glue to the exterior and six-colour `G`.  This proves all
four clauses of the defined `e_i`-anchored response.  Since `e_i=z_ix_i`,
the named centre is indeed in the boundary or in the response component.

## 4. Common coordinate assignment

In the seven-connected case, seven internally disjoint paths between the
ends of `e_i` must each meet every `Q_X`.  The paths have disjoint internal
vertices and `|Q_X|=7`, so each meets the cut exactly once and together they
exhaust it.

Start with the four `D`-ends.  Replacing `d_j` by `a_j` leaves six boundary
vertices fixed on six fixed paths.  The seventh path must therefore contain
both `d_j` and `a_j`.  Oriented from `A` to `D`, it meets `a_j` first.  Any
intermediate vertex would lie on the `A`-side of the first cut and the
`D`-side of the flipped cut, so the two endpoints are consecutive and the
path uses the literal edge `e_j`.  The four base boundary vertices lie on
different paths, so the four coordinates do also.

The remaining three paths meet the three different vertices of `S`.
For every other endpoint choice, each coordinate path already contains its
selected boundary endpoint; the once-only intersection forces the same
assignment, while the other paths retain their distinct `S` vertices.
Thus the proof establishes one path family for the entire sixteen-cut cube,
not sixteen unrelated Menger families.

Because the centre has degree eight in `G` and `e_i` is deleted, the seven
paths leave it through seven distinct vertices and therefore use all of
`N_G(z_i)-\{x_i\}`.  Restoring the direct edge gives the asserted eighth
internally disjoint path.

## 5. Rooted join and neighbourhood exclusion

Let `y` be one of the seven first neighbours.  No path can contain another
such neighbour `y'`: that vertex is an internal first vertex of its own
path, contrary to internal disjointness.  Delete `z_i` and the first vertex
`y` from every path and unite the remaining tails with `x_i`.  These tails
are pairwise disjoint away from `x_i`, so their union is a connected branch
set rooted at `x_i`, disjoint from the seven singleton branch sets `\{y\}`.
It is adjacent to each singleton.  The singleton `\{z_i\}` is adjacent to
all seven neighbours and to the `x_i` branch set through the restored edge
`e_i`.  Existing edges among the seven singleton roots retain precisely the
required copy of `G[N_G(z_i)-\{x_i\}]`.  This proves the rooted
`K_2\vee G[N_G(z_i)-\{x_i\}]` minor.

If the induced neighbourhood graph contained a `K_5^-` minor, its five
branch sets together with the two universal rooted branch sets would form
`K_2\vee K_5^-=K_7^-`.  Minor transitivity then contradicts the standing
target exclusion.  The displayed neighbourhood exclusion is therefore
valid.

## 6. Trust boundary

No proof gap or hidden finite assumption was found.  The conclusion is
coordinatewise.  In the all-linkage case it has the exact quantifier form

\[
                     \forall i\;\exists\mathcal P_i.
\]

The five families live in different one-edge-deleted graphs and need not
be mutually disjoint or compatible.  The theorem also supplies no common
boundary equality partition across the five cubes.  It consequently does
not justify simultaneous packet composition, a `K_7^-` model in the
all-linkage residue, a six-colouring of `G`, the `K_7^-` six-colour
conjecture, or `HC_7`.
