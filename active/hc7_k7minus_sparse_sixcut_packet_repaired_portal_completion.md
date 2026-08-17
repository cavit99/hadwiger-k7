# Packet repair of an essential rooted-`K_4` portal

**Status:** proved terminal strengthening of the clean portal-path decoder.
The second derived-boundary packet repairs every root-side component which
contains another portal.  Consequently a surviving essential portal is the
outermost portal on one duty arm of a minimal support-bag connector.

Use the `k=2` setup and notation of the
[clean portal-path completion](hc7_k7minus_sparse_sixcut_clean_portal_path_completion.md).
In particular,

```text
N_G(L)={z_1,z_2,p,q,r_1,r_2},
```

`M_1,M_2` are the support bags, `M_3,M_4` are the non-support bags, and
`P_1,P_2 subseteq L` are disjoint connected `N_G(L)`-full packets.

Fix an internal portal `r in M_2`.  Let `W` be a path from `r` to a vertex
`y in M_3` such that

```text
W subseteq G[(C-L) union {x_3,x_4}],
V(W) intersect L is empty,
V(W) intersect (M_1 union M_2 union M_3 union M_4)={r,y}.      (1)
```

Let `K` be the component of `G[M_2-r]` containing `z_2`.  Let
`H_1,...,H_m` be all components of `G[M_2-r]` other than `K` which contain
an internal portal from `N_G(L)-S` distinct from `r`, and put

```text
U=K union P_1 union H_1 union ... union H_m.          (2)
```

## Theorem 1 (packet-repaired clean-path completion)

If `U` is adjacent to `M_3`, then `G` contains a `K_7^-` minor.

### Proof

The set `U` is connected.  Indeed, `P_1` has a neighbour at
`z_2 in K`, and it has a neighbour at the internal portal contained in
each `H_i`.  The sets in (2) are otherwise pairwise disjoint.

We define a replacement `\widehat M_4`.  If `U` is adjacent to `M_4`, put
`\widehat M_4=M_4`.  Otherwise inspect an old `M_2`--`M_4` model edge.  Its
end in `M_2` cannot belong to `K` or to an `H_i`, by the present
nonadjacency assumption.  If that end is `r`, again put
`\widehat M_4=M_4`.  Otherwise it lies in a component `H` of `G[M_2-r]`
which is disjoint from `K,H_1,...,H_m`.  The connectedness of `M_2` gives
an edge from `r` to `H`; put

```text
\widehat M_4=M_4 union H.                             (3)
```

Now form the five disjoint connected bags

```text
B_1=M_1,
B_2=P_2 union (W-{y}),
B_3=U,
B_4=M_3,
B_5=\widehat M_4.                                    (4)
```

The ambient restriction in (1) keeps `B_2` disjoint from `D,E,p,q`, as
well as from the packets and the other four local bags.

The bag `B_1` is adjacent to `B_2,B_3` through the edges from `P_2,P_1`,
respectively, to `z_1`; it is adjacent to `B_4,B_5` through the old
`M_1` model contacts.  The bag `B_2` is adjacent to `B_3` through the edge
from `P_2` to `z_2`, and to `B_4` through the last edge of `W`.  The bags
`B_3,B_4` are adjacent by hypothesis, and `B_4,B_5` retain the old
`M_3`--`M_4` contact.

If `U` is adjacent to `M_4`, then `B_3,B_5` are adjacent and only
`B_2,B_5` may be nonadjacent.  Otherwise (3), or the direct edge from `r`
to `M_4`, makes `B_2,B_5` adjacent, and only `B_3,B_5` may be nonadjacent.
Thus the five bags in (4) have at most one missing pair.

As in the clean-path theorem, add

```text
B_6=D union {p},             B_7=E union {q}.
```

These are mutually adjacent universal bags for the five bags in (4): they
meet `B_2,B_3` through the `p,q` contacts of the two packets, and they meet
`B_1,B_4,B_5` through `z_1,x_3,x_4`.  The seven bags give a `K_7^-`
model.  \(\square\)

## Corollary 2 (outermost-duty orientation)

In a target-free host, suppose a saturated linkage path beginning at
`r in M_2` first re-enters the four-bag model in `M_j`, where
`j in {3,4}`.  Then every `M_j` contact of `M_2` lies either

1. at `r` itself; or
2. in a component of `G[M_2-r]` which contains neither `z_2` nor another
   internal portal.

### Proof

Trim the linkage path at its first model vertex.  It satisfies (1), with
`M_j` in place of `M_3`.  If the `z_2`-component or a component containing
another portal had an `M_j` contact, the repaired set `U` would be adjacent
to `M_j`, contrary to Theorem 1.  \(\square\)

Choose in `M_2` a minimal tree joining `z_2` to one selected contact with
each of `M_3,M_4`.  Corollary 2 says that a surviving portal assigned to
duty `M_j` separates the root from the selected `M_j` contact and has no
other portal beyond it on that arm.  Hence it is the outermost portal on
the root--`M_j` arm.  In particular, for each support bag and each of its
two non-support duties, at most one portal can survive with that duty.

## Exact remaining obstruction

The theorem removes portal chains and different-portal bypasses.  It does
not eliminate a portal which simultaneously dominates both non-support
duties, or two portals which are outermost on different duty arms.  Turning
those private terminal arms into a new exact separator requires control of
all graph edges leaving the arms, not merely the chosen minimal model tree.

The statement is deliberately restricted to the `k=2` orientation.  Its
connectivity argument uses `z_2 in N_G(L)` so that the packet `P_1` joins
the `z_2`-component `K` to every other portal component.  In the `k=4`
orientation no original rooted-model vertex lies in `N_G(L)`, so this
anchor is unavailable; the displayed bags do not prove a completion there.

## Dependency

The clean decoder used above is
[`hc7_k7minus_sparse_sixcut_clean_portal_path_completion.md`](hc7_k7minus_sparse_sixcut_clean_portal_path_completion.md),
source SHA-256
`15368619194a1beb244e3208f552889f29d604b55025b35ec9c489e03708e67d`;
independent GREEN audit SHA-256
`9d96cccba31258d2389127f75d8075158b2ddea83bcedb39362e119bb55448d5`.
