# Internal audit: boundary provenance lost under tri-separation reduction

Audited file:
`barriers/hc7_k7minus_tri_separation_boundary_trace_loss.md`.

Audited SHA-256:

```text
08f89cfcfdd097044a00c6b5969e90ea8a2e1337c7614020d0899affa9797f19
```

**Verdict:** **GREEN** for the exact revision above.

This is a separate internal mathematical audit, not external peer review.

## Construction and connectivity

The vertex sets have total order `3+4+4=11`.  The two four-vertex cliques
contribute twelve edges, and the displayed neighbourhoods of `a,b,c`
contribute twelve more, with no overlap.  Thus `|E(H)|=24`.  The degrees are
seven occurrences of four and four occurrences of five, so `delta(H)=4`.

The set `{a,b,c}` separates the two cliques, giving `kappa(H)<=3`.  Deleting
at most two vertices never disconnects the graph.  Both cliques retain
nonempty connected subgraphs.  If `b,c` survive, at least one retains a
neighbour in each clique: destroying one of the two-neighbour sets of `b`
and one of those of `c` requires at least three deletions.  If exactly one of
`b,c` survives, only one further vertex can be deleted, so the survivor still
meets both cliques.  If neither survives, then only `b,c` were deleted and
`a` joins the intact cliques.  Every other surviving vertex among `a,b,c`
still meets a surviving clique.  Hence `kappa(H)>=3`, and therefore
`kappa(H)=3`.

## The two separations and their common reduction

For the separation with boundary `{a,b,c}`, both closed sides contain a
`K_4`, so it is nontrivial.  The only deficient boundary incidence is that
`a` has the unique neighbour `c_1` on the `C`-side.  Its reduction is

```text
A = C union {b,c},    B = D union {a,b,c},
```

with mixed separator `{b,c} dotunion {ac_1}`.

For the separation with boundary `{b,c,c_1}`, the two open sides are
`{c_2,c_3,c_4}` and `{a,d_1,d_2,d_3,d_4}`.  Its closed sides again contain
the cliques `C` and `D`, respectively, so it too is nontrivial.  On the
second closed side, `c_1` has the unique neighbour `a`; reducing `c_1`
therefore gives the same ordered pair `(A,B)` and the same mixed separator.

In the common reduction, `b` has neighbours `c_2,c_3` on one side and
`d_2,d_3` on the other; `c` has neighbours `c_2,c_4` and `d_1,d_4`,
respectively.  Thus the common reduction is a tri-separation.  Both closed
sides contain cycles, and its vertex separator elements `b,c` have degree
four, so it is strong and nontrivial.

## Lost label and scope

The edge element `ac_1` represents original boundary vertex `a` in the first
separation and original boundary vertex `c_1` in the second.  Since `ac_1`
is an edge, every proper colouring assigns different colours to these two
vertices.  The undecorated reduction therefore determines neither the
original boundary endpoint nor its colour label.

The construction is not claimed to occur in a seven-connected
contraction-critical host.  It refutes only the intermediate assertion that
an undecorated Carmesin--Kurkofka reduction retains the boundary provenance
of an ordinary three-separation.  It does not challenge their reduction or
canonical-decomposition theorems, the repository's four-vertex exact-cut
theorem, or any claim about preserving Kempe components after torso
operations.
