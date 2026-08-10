# Internal audit: local coordinate-synchronization barrier

**Verdict:** **GREEN** for the exact source revision below.

**Audited source:**
[`hc7_k7minus_local_coordinate_synchronization_barrier.md`](hc7_k7minus_local_coordinate_synchronization_barrier.md)

**Audited source SHA-256:**

```text
14477f337d656592c489efba2ceb0c45f42c16f56fd194c8952152df4bcf9c91
```

This is a separate internal mathematical audit, not external peer review.
The construction, all four shore partitions, both Kempe paths and the
three-path linkage were checked directly.  The example is correctly scoped
as a barrier to a local mechanism, not to the fixed-trace transfer theorem.

## Exact cuts

Deleting `e=v_0v_1` turns the rim into the path

```text
v_0-v_4-v_3-v_2-v_1.
```

After deleting `Q={v_3,h}`, its two edges `v_0v_4` and `v_1v_2` are the
only components.  Each component meets both boundary vertices.  Directly
deleting `S_x` or `S_u` gives the two decompositions displayed in (1.3).
Every singleton or edge component has a neighbour at each of the three
boundary vertices, verifying exactness.

The odd wheel is three-connected: deleting at most two vertices leaves the
rim path connected through the surviving hub, or leaves a connected path
after deleting the hub and at most one rim vertex.  It is four-chromatic
because the odd rim needs three colours and the universal hub needs a
fourth.

## Colouring table and locks

In `G-e`, the universal hub uses a colour absent from the rim.  The
five-vertex rim path must alternate in the other two colours, giving (2.1)
uniquely up to permutation.  Each closed shore consists of the hub joined
to a rim path.  Alternating that path gives exactly the four partitions in
(2.2): the two shores disagree at both `S_x` and `S_u`, while they agree on
the discrete partition of `Q`.

Recolouring `u` to `beta` on the intact left shore is proper: its only
neighbours there are `x`, coloured `alpha`, and `h`, coloured `gamma`.
The path `u-x-v_4-v_3` alternates `beta,alpha,beta,alpha`; the right path
`u-v_2-v_3` alternates `alpha,beta,alpha` under the edge-deletion
colouring.  Both are genuine two-colour locks with nonempty shore interior.

The three paths in (2.5) have common endpoints `v_4,v_2` and pairwise
disjoint internal sets `{x,u}`, `{v_3}`, `{h}`.  Their intersections with
`S_x` are respectively `x,v_3,h`, and their intersections with `S_u` are
respectively `u,v_3,h`.  Thus they exhaust both cuts and the changing path
contains the literal consecutive edge `xu`.

## Scope

Contracting `v_1v_2` and `v_3v_4` gives the proper `K_4` minor whose bags
are displayed in the source.  Hence the example is not a minor-minimal
four-chromatic host.  It has no Boolean replacement square, fixed
minimum-side trace, rooted-minor alternative or trace-descent conclusion.
The refuted inference therefore has exactly the restricted local data
listed in Section 3 of the source; no stronger project claim is refuted.
