# Independent cold audit: clean portal path completion

**Verdict:** **GREEN** for the hash-pinned revision below.  The seven
displayed branch sets are pairwise disjoint and connected and have at most
one missing contact.  This is an independent internal audit, not external
peer review.

## Audited revision

The audited theorem is
[`hc7_k7minus_sparse_sixcut_clean_portal_path_completion.md`](hc7_k7minus_sparse_sixcut_clean_portal_path_completion.md)
at SHA-256

```text
c46124dc905f970f76f42795a172ff61d80588bec29ae8f9f6815dd005931654
```

The current source SHA-256 is
`dacb0bab3c1811e5c5e8425a22595443ae7216d8a4378d1bcf93e23f5a2acd4a`
after an independently checked precision repair to Corollary 2 and a later
metadata-only repinning of the rooted-portal dependency.  The frozen source
accidentally said that
*no* saturated linkage has the stated pathwise support/model-essential
alternative.  Theorem 1 proves the opposite universal quantifier: in a
target-free host, *every* saturated linkage has that alternative on each
path, because any path violating it is the clean path decoded by Theorem 1.
The theorem statement and its seven-bag proof are unchanged by the dependency
repinning.

Its two stated dependencies match their recorded hashes:

```text
6118da0fbbca965c241c8ff5259552744f96c2364d50f95ef0a8b87355be168c
  active/hc7_k7minus_sparse_sixcut_rooted_k4_portal_descent.md
53c91cee74ae8b1f5251e13c14095f8abc65f05625eedb401d3d53173996da15
  active/hc7_k7minus_six_boundary_fragment_rerooting.md
```

The latter supplies the saturated linkage in

```text
G[(C-L) union {x_3,x_4}]-{z_1,z_2,p,q},
```

which is the ambient graph imposed directly in the clean-path definition.

## Ownership and connectivity of the five local bags

The clean path starts at

```text
r in {r_1,r_2} intersect M_2
```

and ends at `y in M_3`.  Its only vertices in the four old model bags are
`r,y`.  Therefore `W-{y}` is disjoint from `M_1,M_3,M_4` and from the
`z_2`-component `K` of `M_2-r`.  It is also disjoint from `L`.  The two
packets lie in `L`, are mutually disjoint, and `L` is disjoint from every
old model bag.  These facts verify pairwise disjointness of

```text
B_1=P_1 union M_1,       B_2=P_2 union (W-{y}),
B_3=K,                   B_4=M_3.
```

The ambient restriction on `W` keeps `B_2` out of `D,E,{p,q}`.  This is
needed for the later bags anchored at `p,q`.

The replacement `widehat M_4` is also valid.  If `K` is not adjacent to
`M_4`, an old `M_2`--`M_4` model edge either starts at `r` or starts in a
component `H` of `G[M_2-r]` distinct from `K`.  In the latter case
`M_4 union H` is connected through that model edge.  It is disjoint from
`K`, and it is disjoint from `W-{y}` because the clean path meets `M_2`
only at `r`.  Thus `B_5=widehat M_4` is connected and disjoint from the
first four bags.  Since `G[M_2]` is connected, every component of
`G[M_2-r]`, in particular the selected `H`, has a neighbour at `r`.

Connectedness of `B_1` uses the `P_1`--`z_1` edge, while connectedness of
`B_2` uses the `P_2`--`r` edge.  These contacts are legitimate precisely
because `z_1,r` belong to `N_G(L)` and each packet is adjacent to every
vertex of that six-set.  The other three bags are connected by definition
or by the preceding replacement argument.

## Complete contact check

Among `B_1,...,B_5`, the following contacts are forced:

| Pair or family | Contact source |
|---|---|
| `B_1B_2` | `P_2`--`z_1`, with `z_1 in M_1` |
| `B_1B_3` | `P_1`--`z_2`, with `z_2 in K` |
| `B_1B_4`, `B_1B_5` | old `M_1M_3`, `M_1M_4` contacts |
| `B_2B_3` | `P_2`--`z_2` |
| `B_2B_4` | last edge of `W` at `y in M_3` |
| `B_3B_4` | the residual clean-path condition `K`--`M_3` |
| `B_4B_5` | old `M_3M_4` contact |

If `K` is adjacent to `M_4`, this also gives `B_3B_5`, leaving only
`B_2B_5` possibly absent.  Otherwise `K` has no `M_4` contact.  If the old
`M_2M_4` edge starts at `r`, it gives `B_2B_5`; if it starts in the
absorbed component `H`, the `rH` edge gives `B_2B_5`.  In this second case
only `B_3B_5` may be absent.  Hence the five local bags have at most one
missing pair in either case.

## The two opposite-component bags

The sets

```text
B_6=D union {p},             B_7=E union {q}
```

are disjoint and connected because `D,E` are distinct `S`-full
components.  They contact one another through an `E`--`p` edge.  Their
contacts with the first five bags are:

| Target bags | Contact source for `B_6`; for `B_7` use `q,E` |
|---|---|
| `B_1,B_2` | the `p` contacts of packets `P_1,P_2` |
| `B_3` | a `D`--`z_2` edge, with `z_2 in K` |
| `B_4` | a `D`--`x_3` edge, with `x_3 in M_3` |
| `B_5` | a `D`--`x_4` edge, with `x_4 in M_4 subseteq B_5` |

All seven bags are therefore pairwise adjacent except for at most the one
local pair identified above.  This is an explicit `K_7^-` minor model.

## Corollary and scope

For a saturated `{r_1,r_2}`--`{x_3,x_4}` linkage, truncate a path at its
first model vertex after its initial portal.  The saturated-linkage ambient
condition remains valid, and the prefix meets the four model bags only at
its two ends.  If that first new model vertex lies in a non-support bag and
the root-component of the punctured support bag retains a contact with the
target bag, the prefix satisfies the clean-path theorem.  The stated
model-essential alternative is exactly its negation.

The proof uses both corrections present in the audited revision: the
initial vertex is explicitly one of `r_1,r_2`, and the path is explicitly
confined to the saturated-linkage ambient graph.  Without the first,
`B_2` need not be connected; without the second, it could intersect
`D,E,p`, or `q`.  No finite-order assumption or computational inference is
used.  The theorem closes only the clean-prefix case and does not establish
that such a prefix must exist.
