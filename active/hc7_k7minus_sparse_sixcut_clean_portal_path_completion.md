# A clean portal path closes the two-exchanged-root packet return

**Status:** proved unbounded terminal composition; adjacent independent cold
audit GREEN.  In the two-root exchange of the rooted-`K_4` portal descent,
two packets behind the derived cut force `K_7^-` whenever one
portal-to-non-support-bag path is clean with respect to the four-bag model.
The unresolved residue has every such path model-essential or
model-entangled.

Let `G` be a six-connected graph with no `K_7^-` minor.  Let `S` be a
six-cut such that `G-S` has three `S`-full components `C,D,E`.  Fix

```text
S={z_1,z_2,x_3,x_4,p,q}.                              (1)
```

Suppose `G[C union {z_1,z_2,x_3,x_4}]` has a rooted `K_4` model

```text
M_1,M_2,M_3,M_4,                                     (2)
```

where the displayed roots occur in the correspondingly indexed bags.

Suppose further that `L subseteq C` is a connected exact fragment with

```text
N_G(L)={z_1,z_2,p,q,r_1,r_2},                        (3)
```

where `r_1,r_2` are internal vertices of `C`, both belong to
`M_1 union M_2`, and `L` is disjoint from all four model bags.  Thus this is
the `k=2` orientation of the rooted-`K_4` portal descent: `z_1,z_2` are the
two boundary portals and `x_3,x_4` are the two missing original roots.

An **`r`--`M_3` clean portal path through `M_2`** is a path `W` with ends
`r` and `y in M_3` such that

```text
r in {r_1,r_2} intersect M_2,
W subseteq G[(C-L) union {x_3,x_4}],
V(W) intersect L is empty,
V(W) intersect (M_1 union M_2 union M_3 union M_4)={r,y},     (4)
```

and the component `K` of `G[M_2-r]` containing `z_2` is adjacent to the
**target bag** `M_3`.  No retained `M_1` contact is required, and `K` need
not remain adjacent to the other non-support bag `M_4`.  The definitions
with the two support bags or the two missing roots interchanged are
symmetric.

## Theorem 1 (clean-path completion)

If `L` contains two disjoint connected subgraphs `P_1,P_2`, each adjacent
to every vertex of `N_G(L)`, and a clean portal path exists, then `G`
contains a `K_7^-` minor.

### Proof

By symmetry take a clean `r`--`M_3` path `W` through `M_2`, with other end
`y in M_3`, and let `K` be
the `z_2`-component of `G[M_2-r]`.  We first define a replacement
`\widehat M_4`.  If `K` is adjacent to `M_4`, put
`\widehat M_4=M_4`.  Otherwise the old bag `M_2` still has an edge to
`M_4`.  Either `r` itself has such an edge, in which case again put
`\widehat M_4=M_4`, or some component `H` of `G[M_2-r]` other than `K`
has an edge to `M_4`.  Every such component has a neighbour at `r`, since
`G[M_2]` is connected.  In the latter case put
`\widehat M_4=M_4 union H`.

The following five sets are pairwise disjoint and connected:

```text
B_1=P_1 union M_1,
B_2=P_2 union (W-{y}),
B_3=K,
B_4=M_3,
B_5=\widehat M_4.                                    (5)
```

For connectedness in (5), `P_1` is adjacent to `z_1 in M_1`, while
`P_2` is adjacent to `r` and `r belongs to W-{y}`.  Disjointness follows
from (2)--(4), from the disjointness of the two packets, and from
`L` being disjoint from the model and the path.  The ambient restriction
on `W` also keeps it disjoint from the opposite components `D,E` and from
the boundary anchors `p,q` used below.

We check every contact.  The bag `B_1` is adjacent to `B_4,B_5` through
the old `M_1` model contacts, and it is adjacent to `B_3` because `P_1`
has a neighbour at `z_2 in K`.  It is adjacent to `B_2` because `P_2`
has a neighbour at `z_1 in B_1`.  The bag `B_2` is
adjacent to `B_3` because `P_2` has a neighbour at `z_2 in K`; it is
adjacent to `B_4` through the last edge of `W` at `y`.  The three bags
`B_3,B_4,B_5` have the `B_3`--`B_4` contact by the clean-path definition
and the `B_4`--`B_5` contact through the old `M_3`--`M_4` model edge.

If `K` is adjacent to `M_4`, then `B_3,B_5` are adjacent and the only pair
in (5) which may be nonadjacent is `B_2,B_5`.  If `K` is not adjacent to
`M_4`, then the construction of `\widehat M_4` makes `B_2,B_5` adjacent:
either `r` has an edge to `M_4`, or it has an edge to the absorbed component
`H`.  In that case the only pair which may be nonadjacent is `B_3,B_5`.
Thus in both cases the five bags in (5) have at most one missing pair.

Use the two other full components to define

```text
B_6=D union {p},             B_7=E union {q}.         (6)
```

These bags are connected and disjoint.  They are adjacent to each other,
since `E` has a neighbour at `p`.  Each is adjacent to `B_1,B_2`: the
packets have neighbours at both `p,q`.  Each is adjacent to
`B_3,B_4,B_5` through the boundary roots `z_2,x_3,x_4`, respectively.
Consequently the seven bags in (5)--(6) have at most the one missing pair
identified above (`B_2,B_5` or `B_3,B_5`).  They form a `K_7^-` model, a
contradiction.
\(\square\)

## Corollary 2 (the exact surviving linkage obstruction)

In a target-free host, if the `k=2` exact fragment has
`mu_{N(L)}(L)>=2`, then every saturated

```text
{r_1,r_2}--{x_3,x_4}
```

linkage supplied by six-connectivity has the following property for each
of its two paths.  The first model vertex after its initial portal lies in
a support bag; or, if that first vertex lies in a non-support bag `M_j`,
deleting the initial portal separates the root of its support bag from
every contact with `M_j` inside that support bag.  Indeed, otherwise the
prefix ending at that first model vertex satisfies (4) and the residual-bag
condition, contrary to Theorem 1.

This is a genuine strengthening of the generic two-copy-linkage barrier:
only one clean path, not two disjoint saturated linkages, is needed for the
terminal composition.  What remains is a model-essential portal problem
inside one of the two support bags.

## Dependencies

- [rooted-`K_4` portal descent](hc7_k7minus_sparse_sixcut_rooted_k4_portal_descent.md),
  source SHA-256
  `6118da0fbbca965c241c8ff5259552744f96c2364d50f95ef0a8b87355be168c`;
- the saturated opposite-side linkage is Lemma 1 of
  [the exact-six rerooting theorem](hc7_k7minus_six_boundary_fragment_rerooting.md),
  source SHA-256
  `53c91cee74ae8b1f5251e13c14095f8abc65f05625eedb401d3d53173996da15`.
