# Internal audit: degree-seven density-preserving contraction and fragment residue

**Audited source:**
[`hc7_k7minus_degree7_safe_contraction.md`](hc7_k7minus_degree7_safe_contraction.md)

**Audited source SHA-256:**
`f69c7eefc74c6074173e5d4e0396e3c2a2a2635f0aba58c7b54f3559c2c16896`

**Verdict:** **GREEN.**  The three stated results are computation-free.
This is a separate internal mathematical audit, not external peer review.
The revision differs from the initially audited source only by replacing
the pending-audit status line with the completed GREEN status; no theorem,
proof, dependency or scope statement changed.

## Dependency revisions

- [`hc7_k7minus_seven_cut_three_component_bound.md`](hc7_k7minus_seven_cut_three_component_bound.md),
  SHA-256
  `cbd3ecb73bea0530797ad58080ae6db6052bfbf69f90af558283e3f250772ef8`;
- [`hc7_k7minus_seven_boundary_component_descent.md`](hc7_k7minus_seven_boundary_component_descent.md),
  SHA-256
  `9e2f616c98dd17670f4d15e962f3b36e4fc1f4c4dc9aee4227eabeb51ca33913`;
- [`hc7_seven_column_contact_structure.md`](hc7_seven_column_contact_structure.md),
  SHA-256
  `b48e19642347571a713f60d2b045be85907bfe6a07052465ba09d2446d516859`;
- R. Halin, *A theorem on n-connected graphs*, J. Combin. Theory **7**
  (1969), 150--154; and
- Yuan Xudong, *A note on fragments in a locally k-critical n-connected
  graph*, Ars Combin. **93** (2009), 25--31, Theorem 3.

The first three repository dependencies have adjacent GREEN audits at their
pinned revisions.  The two external statements were checked against their
published formulations.

## 1. Safe incident contraction

The density hypothesis excludes order eight, so a degree-seven vertex `v`
has a nonempty anti-neighbourhood and `S=N(v)` is an order-seven cut.
Seven-connectivity makes every component of `G-S` adjacent to every vertex
of `S`.  Since `{v}` is one component, the audited three-component theorem
leaves exactly two cases.

If `G-S` has three components, its boundary is subcubic.  The independent
capacity bound `|E(G[S])|<=9` also gives a boundary vertex of degree at most
two by averaging.  If `G-S` has two components, selecting those two full
components in the capacity theorem makes `G[S]` `K_5`-minor-free.  The
seven-vertex theorem then gives a vertex of degree at most three unless
`G[S]` is the pentagonal bipyramid.

The displayed model excludes that exceptional graph.  In
`I_2\vee B_5`, the seven bags

```text
{p0,r4}, {p1}, {r0,v}, {r1}, {r2}, {r3}, {c}
```

are connected and disjoint.  The pole and join edges supply every
adjacency involving the first, second, third or seventh bag; consecutive
rim edges supply the remaining required adjacencies.  Only the
`{r1}`--`{r3}` adjacency may be absent.  This is a valid `K_7^-` model.

Contracting `vs` deletes `vs` and exactly one duplicate edge for each
common neighbour of `v,s`.  Those common neighbours are precisely the
neighbours of `s` in `G[S]`.  Hence

\[
 |E(G/vs)|=|E(G)|-1-d_{G[S]}(s),
 \qquad
 q(G/vs)=q(G)+3-d_{G[S]}(s).
\]

This verifies Theorem 1, including the stronger two-exterior-component
conclusion.

## 2. Minimal-enemy cut pullback

At `q(G)=0`, the average degree is strictly below eight, while
seven-connectivity gives minimum degree at least seven, so a degree-seven
vertex exists.  At positive integral surplus, deletion of any edge retains
the density threshold.  Minimality in size therefore makes `G`
edge-minimal seven-connected, and Halin's theorem supplies a degree-seven
vertex.

For a density-preserving incident contraction, seven-connectivity of
`G/vs` would make it a smaller counterexample; target-minor exclusion is
inherited by minors.  Thus `G/vs` has a cut `X` of order at most six.  If
the contracted vertex `z` were not in `X`, the same set would cut `G`.
Replacing `z` by `v,s` consequently gives a cut of `G`, and
seven-connectivity forces `|X|=6`.  This proves the exact order-seven
pullback.

Every component behind the pulled-back cut contains a surviving neighbour
of `v`: otherwise its neighbourhood would lie in the other six cut
vertices.  The three-component theorem therefore applies exactly as
claimed.  In the two-exterior case every incident edge is
density-preserving.  If the returned cut missed either full exterior
component, that component would join every surviving neighbour of `v`,
and hence all components behind the cut, a contradiction.  The bounds on
`|T\cap N(v)|` and the subcubic three-component sharpening then follow by
direct counting.

## 3. Yuan fragment residue

In the two-exterior case every edge `vs`, `s\in S`, is
density-preserving, so minimality makes every such contraction fail
seven-connectivity.  Deleting `v` from its exact pullback cut gives a
five-cut of `H-s`.  Since deleting one or two vertices from a
seven-connected graph leaves a six- or five-connected graph, respectively,

\[
                    \kappa(H)=6,
              \qquad \kappa(H-s)=5\quad(s\in S).
\]

For a fragment `D` of `H` or `H-s` that missed the corresponding surviving
part of `S`, its neighbourhood in `G` would have order at most six.  The
local fragment condition is therefore correct.

Yuan defines a `W`-locally `k`-critical `n`-connected graph using all
`W'\subseteq W` with `|W'|<=k`.  Thus the established empty- and
singleton-deletion facts make `H` `S`-locally `(6,1)`-critical in the
published convention.  The graph is noncomplete because it has
connectivity six and contains the two nonempty exterior components.
Yuan's Theorem 3 with `k=1` consequently gives four fragments with
pairwise disjoint, nonempty `S`-traces.  Since `|S|=7`, at least one trace
is a singleton.

For such a fragment `F`, every component of `H-N_H(F)` contained in `F`
has the full six-vertex neighbourhood `N_H(F)` by six-connectivity.  It is
therefore itself a fragment and meets `S`; the singleton trace permits only
one such component.  This proves that `F` is connected.  The two displayed
seven-cuts and the degree-seven singleton alternative follow exactly as
stated.  If `F-t` is nonempty, each of its components has neighbourhood
contained in the seven-set `Q\cup\{t\}`; seven-connectivity forces equality.
The already audited three-component theorem then gives both the component
count and the subcubic boundary conclusion.

## 4. Scope

No unsupported closure is claimed.  The source correctly records that the
remaining inference -- forcing the root-only fragment to be a singleton or
finding a contractible edge in the nested root-swap configuration -- is not
proved by the cited fragment or seven-cut theorems.  No unresolved
assumption or mathematical gap remains in the three results at the pinned
revision.
