# Internal audit: common-six trace synchronization

**Verdict:** GREEN for the exact reduction stated in
[`hc7_k7minus_overlap_trace_synchronization.md`](hc7_k7minus_overlap_trace_synchronization.md).
It does not close the distinct nonadjacent-miss case.

## Audited revision

- theorem SHA-256:
  `4af8cd7ae468c989b38c7f22a400a49b75c5841d24605a69a128a92ee350b30e`;
- verifier SHA-256:
  `f491e0b6a2b16c7d796334005329c2830c047e281451e0fe1202c30961f3f2b1`;
- barrier SHA-256:
  `8d6f2fe124d4e1e2d041b377fe900862f94a0c4223f32d1a97a3173cb0a01e34`.

The audit checked the theorem text against the distinct-miss geometry in
the audited nonfull-attachment reduction and reran the retained verifier.

## 1. Common-trace gluing

The palette alignment is valid.  Equal equality partitions on `Z` give an
injective correspondence between the colours used on their blocks.  The
colour of `u` is distinct from all of them in each colouring, so this
correspondence plus the prescribed image of `u` extends to a permutation
of the six-colour palette.

After alignment, selecting `E,y` from the colouring of `G-F` and selecting
`F,x` from the colouring of `G-E` creates no unchecked edge.  The exact
facts used are

\[
 E\perp(F\cup\{u,x\}),\qquad
 F\perp(E\cup\{u,y\}),\qquad xy\notin E(G).
\]

All edges incident with `Z\cup\{u\}` were already proper in the selected
colouring.  Lemma 1 therefore proves a six-colouring, not merely compatible
boundary data.

## 2. Connected-subgraph reflection

For a partition `Pi`, choosing a maximum clique `U` among its singleton
blocks leaves exactly `d_Z(Pi)` blocks to contract.  For each such block
`B_i`, `P_i\cup B_i` is connected because `P_i` is connected and is
adjacent to every literal vertex of `Z`.  Distinct representatives are
adjacent through a literal vertex of the other block; they are also
adjacent to every retained singleton in `U`.  Thus the representatives
and `U` form the claimed clique.

The pullback expands only independent subsets of `Z` and discards the
whole operated exterior component.  It never expands a contracted
connected subgraph on its own side.  At least one boundary edge is
contracted because `G[Z]` is not complete under the displayed
`K_4`-minor exclusion, so the minor is proper.  Minor-criticality is used
exactly here to obtain its six-colouring.

The restriction to at most five trace blocks is harmless in the stated
application.  A `K_4`-minor-free graph is three-colourable, so a partition
attaining minimum reflection demand may be chosen with at most three
blocks when needed in (6).

## 3. Demand one and the triangle lift

The demand-one classification is computation-free.  A clique `U` and
independent complement `I` must each have order three.  Deleting a vertex
of `I` different from `i` preserves the four vertices `U\cup\{i\}`; two
`U`-neighbours of `i` give a `K_4^-` there, while three give a `K_4`.
Hence every `i` has at most one `U`-neighbour.  The independence bound
forces every `u in U` to have at least one `I`-neighbour, so the three
cross-edges form a perfect matching.  This is exactly the net.

For Lemma 4, the seven proposed branch sets were checked pairwise.  The
shortest-path enlargement supplies the adjacency between the two
same-component sets.  Their two distinct anchors outside the triangle
supply adjacency to both `F\cup\{x\}` and `{u}`.  The edge `ux` supplies
the remaining adjacency among those four sets, and `Z`-fullness supplies
all contacts with the three triangle singletons.  The result is a genuine
`K_7` minor and therefore contradicts the stronger `K_7^-` exclusion.

## 4. Finite verification

The command

```text
python3 results/hc7_k7minus_overlap_trace_synchronization_verify.py
```

completed with

```text
common_six_survivors=28 digest=9349e3f0c53068bdbdac7068c8fa347ac6658b5231c8abd3dc8e99804118bec9
reflection_demand_distribution=1:1,2:26,3:1
triangular=16 triangle_free=12
unique_demand_one=ECqg(net) unique_demand_three=EQhO(2K3)
matching_parity_languages=PASS
PASS overlap_trace_synchronization_finite_checks
```

The verifier enumerates all 156 unlabelled six-vertex graphs, tests `K_4`
and `K_4^-` minors by independent deletion/contraction recursion, and
computes reflection demand from the clique-deletion identity by direct
colourability search.  It also exhausts every set partition needed for the
three-matching parity-language barrier.

## 5. Scope and unresolved obligation

The result eliminates only the demand-one common boundary and imposes
the stated `Z`-full packing restrictions on the other 27 types.  It does
not prove that the two actual trace languages intersect there.  The
three-matching construction is correctly scoped as an abstract-language
barrier: it does not claim realization by exterior graphs and does not
satisfy the critical-host hypotheses.  A completion still needs a relation
between colourings of related proper minors or additional structure inside
an exterior component with `Z`-full packing number one.
