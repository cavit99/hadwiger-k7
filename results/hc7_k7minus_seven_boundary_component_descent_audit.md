# Internal audit: connected subgraphs adjacent to a seven-vertex boundary and component-contraction criteria

Audited file:
`results/hc7_k7minus_seven_boundary_component_descent.md`.

Audited SHA-256:

```text
9e2f616c98dd17670f4d15e962f3b36e4fc1f4c4dc9aee4227eabeb51ca33913
```

**Verdict:** **GREEN** for the exact revision above.

This is a separate internal mathematical audit, not external peer review.
Two agents independently reconstructed the connected-subgraph minor models, the
four-component cutvertex argument, the simultaneous-contraction accounting,
and the exact connectivity criterion.  The mathematical revision was first
audited at SHA-256
`6494d25f2762752741f4401dd4e83acbdb343f70b5871c1978c331face74a2a6`;
the status-only GREEN revision was
`e071c63963e70b90ad6d2975aaf4cae1e686ec2635177c60fc6991d4094de2d4`.
The exact revision pinned above changes only the filename, title, and
terminology from “packet” to “connected subgraph adjacent to every boundary
vertex,” in
accordance with the repository's mathematical-language rule.  Two agents
confirmed that no hypothesis, formula, construction, or conclusion changed
and independently returned GREEN for the exact current source.

## 1. Capacity of connected subgraphs adjacent to every boundary vertex

After contracting pairwise disjoint connected subgraphs that are each
adjacent to every boundary vertex,
deleting unused vertices and any edges between their contracted images leaves
`I_p\vee G[S]`.  With five such subgraphs, the bags
`\{c_i,s_i\}`, `1\le i\le5`, `\{s_6\}`, and `\{s_7\}` have every
adjacency except possibly `s_6s_7`, so `p\le4`.

For `p\ge2`, the formula

\[
                 \kappa(I_p\vee R)=\min\{7,p+\kappa(R)\}
\]

is exact for a seven-vertex graph `R`.  The required `p=2,3,4`
seven-connected join constructions are supplied by the previously audited
[seven-cut theorem](hc7_k7minus_seven_cut_contraction.md), at SHA-256

```text
bbb9919b6d04c08836526d017607d318323fe457baa75d4c3364be85a4ad1ff5
```

The separate `K_5`, `K_4^-`/house/`K_{2,3}`, and three-vertex-path models
were checked bag by bag.  They prove the stated boundary restrictions.  A
maximum such family exists, contains at least the component family, and
therefore gives `2\le r\le\pi_S(G)\le4` with the stronger `p`-indexed
connectivity bound.

## 2. Four-component interiors

If a two-vertex component is split into its two ends, minimum degree seven
gives at least six boundary neighbours to each end.  If a larger component
has a cutvertex `v`, choose two distinct components `X,D` of its deletion
and put `Y=C-X`.  The external neighbourhood of each of `X,D` is exactly
`\{v\}` plus its boundary neighbours.  Each is a genuine cut, so
seven-connectivity gives at least six boundary neighbours to `X` and `D`,
and hence to `Y` because `D\subseteq Y`.

Thus `X,Y` have at least five common boundary neighbours.  The two interior
bags, three other component bags anchored at three common neighbours, and
the remaining two common-neighbour singletons are pairwise adjacent except
possibly for the last pair.  This is an explicit `K_7^-` model.  Hence every
four-component interior is a singleton or is two-connected.

## 3. Density and connectivity accounting

For each selected cut component, contraction removes `n_i-1` vertices and
replaces all `e_i` internal or boundary-incident edges by exactly seven
boundary edges.  Distinct components are anticomplete, so the changes add.
This verifies

\[
 q=e_S+\sum_i\delta_i-24,
 \qquad
 q(H_X)=q+\sum_{i\in X}(3-\delta_i).
\]

For a set `Y` of at most six vertices in `H_X`, let `D` index the contracted
vertices in `Y` and let `Z` be the remaining vertices.  If `D` is empty,
seven-connectivity of `G` applies directly.  Otherwise `H_X-Y` is obtained
from

\[
                  G-\bigcup_{i\in D}V(C_i)-Z
\]

by contracting the surviving selected components.  Each is an intact
connected subgraph inside one component, so contraction neither joins nor
splits components.  This proves both directions of the stated criterion.

The density inequality plus that criterion gives the exact sufficient
descent.  Requiring at least one selected component of order at least two is
exactly what makes the minor proper.  Its contrapositive gives Corollary 5,
including the `|Z|\le5` singleton-index certificate.

## 4. Residue and trust boundary

Every displayed arithmetic row satisfies the global identity and every
nonempty component subset fails the density inequality.  The rows are
correctly labelled arithmetic possibilities rather than graph examples.
They show that boundary counting alone does not close the descent.

No unresolved mathematical assumption remains in the audited revision.  It
is unbounded and computation-free.  It does not prove the full seven-cut
dichotomy, the bare `4n-4` extremal theorem, the `K_7^-` six-colour
conjecture, or `HC_7`.
