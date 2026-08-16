# Internal audit: reverse crossing five-cube and renewed exact model

**Verdict:** **GREEN** for the promoted source revision recorded below.  The two
terminology edits do not change any mathematical statement or proof step.
This is a separate internal mathematical audit, not external peer review.

## 1. Exact revision and scope

The promoted source is
[`hc7_k7minus_remote_crossing_five_cube_model_renewal.md`](hc7_k7minus_remote_crossing_five_cube_model_renewal.md),
with SHA-256

```text
10eb1918965ef8e8f3380bcf1a4154e1b49dbfe77ec0ce4e93335ee682098323
```

The complete mathematical text was audited before promotion at SHA-256
`8dc7a9e422787e2c3db2aa77cc2ecc4ab1fbb679c93669ac7b08e40c29a37ab7`.
Promotion changed only the status paragraph.

The audit covers the componentwise-induced five-edge expansion, all 242
labelled mixed operation patterns, all 31 nonempty equality signatures,
literal inheritance and orientation of the sixteen named shore responses,
connectivity and density of the common deletion host, renewal and exactness
of its spanning `K_7^\vee` model, the all-contraction `K_6` model, and every
case of the separator argument in Theorem 5.1.

## 2. The crossing edge and repair geometry

In outcome 1 of the remote-interface reduction, the full component `E` is
adjacent to every member of the seven-set `S`.  Since the independent
triple `I` has order three, `S-I` has at least four vertices.  Choosing
`s\in S-I` and an edge `h=es` with `e\in E` therefore is valid.

The new edge is vertex-disjoint from the old forest `T`: `s` is not a star
leaf, `e` belongs to the exterior component `E`, and both ends of the
remote edge `f` belong to the distinct exterior component `C`.  Thus the
five selected edges have eight distinct vertices and form

```text
K_{1,3} dot-union K_2 dot-union K_2.
```

The star is induced because its three leaves are independent; each
two-vertex component is automatically induced.  Cross-component edges do
not invalidate expansion because they remain represented in every
contraction quotient.  Finally, the repair vertices `z,u,e` are pairwise
nonadjacent: `u,e` both avoid `N[z]`, and an edge between them would merge
the distinct components `C,E` of `G-N[z]`.

## 3. All 242 mixed operation patterns

For disjoint `A,D\subseteq F` with `A\cup D` nonempty, `G/A-D` is a proper
minor and hence is at most six-colourable.  Expanding a hypothetical
five-colouring creates possible conflicts only on operated selected edges.
Recolouring `z` when a spoke is operated, `u` when `f` is operated, and
`e` when `h` is operated repairs all such conflicts with one fresh colour.
Those three vertices are independent, and every other vertex retains one
of the original five colours.

Within the star, contraction of some spokes cannot identify the leaf of a
kept spoke; componentwise inducedness excludes any hidden internal edge in
a contraction bag.  Across different selected components, every ordinary
edge is represented in the quotient and its endpoints already have
different old colours.  Kept selected edges likewise remain represented.
The expanded colouring is consequently a proper six-colouring of `G`, a
contradiction.  This proves the lower bound six for every pattern, while
minor-criticality supplies the upper bound.

Each of five labelled edges independently is kept, deleted, or contracted,
and the all-kept word is excluded.  The count `3^5-1=242` is therefore
exact.  No assertion that the resulting unlabelled minors are pairwise
nonisomorphic is made or needed.

## 4. The 31 signatures and the two response orientations

The all-delete pattern gives `\chi(K)=6`.  For every nonempty
`Q\subseteq F`, expand a six-colouring of `G/Q` onto `K=G-F`.  Contracted
edges have equal-coloured ends.  Every edge in `F-Q` survives as a genuine
edge between distinct quotient vertices, so its ends receive different
colours.  The equality signature is exactly `Q`.  An empty signature would
remain proper after all five edges were restored and would six-colour `G`.
Hence the signature language is exactly the 31 nonempty subsets of `F`.

Literal response inheritance is also correct.

- Each old `c_J` is a proper colouring of `H_0`, where `h` is still an
  edge.  Its restriction to `K` therefore has exact `F`-signature `J`,
  with `h` bichromatic in that same colouring.
- Every six-colouring of `G-h` makes the ends of `h` equal, since otherwise
  it would extend to `G`.  All four edges of `T` are present and proper, so
  restriction to `K` has exact signature `{h}`.
- No edge of `T` belongs to the closed `E`-shore, and `h` is proper in each
  old colouring.  Conversely, deleting `E` removes the sole `h` conflict
  of the fresh response.  The old responses and the fresh response are
  therefore legal in opposite orientations.

If either oriented boundary partition extended through its intact opposite
shore, colour-name alignment would glue a six-colouring of `G`.  The same
argument shows that the fresh partition differs from every one of the
fifteen old partitions.  The theorem correctly does not claim that the
fifteen old partitions are mutually distinct.  A mixed signature
containing both `h` and an edge of `T` has a conflict on each original
closed shore, so Remark 3.2 states the exact orientation limit.

## 5. Connectivity, density, and model renewal

The audited four-edge operation theorem gives `\kappa(H_0)=5`.  Deleting
one edge lowers vertex connectivity by at most one, so `K=H_0-h` is at
least four-connected.  Exactly the three spokes incident with the
degree-eight vertex `z` have been removed there, giving `d_K(z)=5` and
the upper bound `\kappa(K)\le5`.

Deleting five distinct edges changes no vertices and gives

```text
|E(K)| = |E(G)|-5 >= 4|V(K)|-5.
```

Thus Norin--Totschnig, Theorem 6, applies well above its `4|V|-8`
threshold.  The exceptional graph `K_{2,2,2,2}` is excluded by the order
bound.  A returned `K_7^\vee` model may be made spanning.  If either of
its two nominal missing bag pairs acquired an edge during absorption or
from any edge restored in `G`, the same seven bags would be a `K_7^-`
model.  Target exclusion therefore makes both pairs anticomplete in the
full host `G`.  This is a renewed model in `K`, not an unsupported claim
that the old `H_0` model survives deletion of `h`.

The all-contraction quotient is connected and exactly six-chromatic.
The established `HC_6` case supplies a `K_6` model, and connectedness lets
unused vertices be absorbed.  Expansion puts each of the three contracted
forest components into a branch bag; the source correctly allows those
three bags to coincide.

## 6. Theorem 5.1 separator cases

The renewed model partitions `V(G)` into the seven bags required by the
audited exact-model separator dichotomy.  It remains exact in the
seven-connected graph `G`, and the dichotomy's target outcome is excluded.
It therefore returns the stated nonempty proper connected
`Y\subset U_i`, connected complement `U_i-Y`, and actual separator
`R=N_G(Y)` of order at least seven.

For each `q=ab\in F`, a singleton-signature colouring of `K` becomes a
proper colouring of `G-q` after the other four selected edges are restored.
The proof then exhausts the placement of the ends of `q`.

1. If `Y` contains an end, the edge `q` is absent from the opposite closed
   side `G-Y`, so the restriction there is proper.
2. If `Y` contains neither end and at most one end is in `R`, the edge is
   absent from the closed `Y`-side `G[Y\cup R]`, so that restriction is
   proper.
3. The only remaining placement has neither end in `Y` and both ends in
   `R`.

In either of the first two cases, extension of the displayed boundary
partition through the intact other side would glue a six-colouring of
`G`; rejection follows.  Therefore failure to expose a response for every
`q` forces `Y` to avoid every selected endpoint and forces both ends of
every selected edge into `R`.  Since the forest has eight distinct
vertices, `V(F)\subseteq R` and `|R|\ge8`.  In particular, an order-seven
separator cannot lie in this escape case and must expose one of the five
named singleton responses.  No separator placement is omitted.

## 7. Novelty, dependencies, and trust boundary

The broader six-coordinate forest theorem already supplies existential
common signature/model hosts.  The present result is not presented as a
larger coordinate-count theorem.  Its distinct contribution is the
literal reverse crossing edge at the same exact-seven interface, retention
of all fifteen old response colourings alongside the fresh opposite
response, exact six-chromaticity of every mixed operation pattern, and the
separator transfer tied to those five labelled singleton responses.

The logical dependencies were checked at these audited revisions:

```text
2f7c69fd57319f898d84c9884907ac70e3e1f2064b3a5753d19da8531406ecf9  remote removable-edge operation cube
5bc54f3b7f4cbe68a7b3c35a35d16c693672cfbffa17686f65008938cdfc3865  remote-interface topological reduction
4845f5375581971aca7397bbac0e3eb930dd2943c9dca71f6264a24e2fa31c6e  exact K_7^vee separator dichotomy
cc2b56362d52a3ef23559a4a0e5cbf5eded5abbe7d54b57e73f66f74f1dd3405  six-coordinate forest reduction, for novelty comparison only
```

Norin--Totschnig, Theorem 6, is the external density-to-model input, and
the established case `HC_6` is used only for Corollary 4.2.  The
three-split closure is cited solely to explain why a known matching-based
route does not apply to three spokes sharing a centre.

The theorem applies only to outcome 1 of the remote-interface reduction.
It does not preserve the old exact model through `h`-deletion, align the
renewed model with the quotient `K_6` model, resolve the eight-endpoint
separator, address the other three remote-interface outcomes, or prove the
`K_7^-` six-colour conjecture or `HC_7`.

All local links resolve, the source and audit pass Git whitespace checking,
and no finite computation is part of the proof.
