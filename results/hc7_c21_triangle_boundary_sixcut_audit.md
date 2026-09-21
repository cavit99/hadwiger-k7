# Internal audit: triangle boundary in a three-component six-cut

**Verdict: GREEN.** This is a separate internal mathematical audit, not
external peer review. The proof applies to arbitrary component orders.

Audited [source](hc7_c21_triangle_boundary_sixcut.md), SHA-256:

```text
8a4454062fed34ae10de23a189c501af40f4a07cf5a04b1425fd5a0fa323766c
```

The final argument was independently reconstructed in this audit.
The following previously audited inputs were inspected, and their source
hashes still match the separate adjacent audits:

- [Five-root density application](hc7_five_root_density_sixcut.md):
  `4c31950cca633178dbcff0800a0ac1b55bc5a58cf9fe0127f165b1a24017a812`.
- [Four-root helper input](hc7_k7minus_degree7_rooted_helper_closure.md):
  `6ffee04cf9ff66275f9674c24bc2b9c669b1e108b76e5b1d2a18ec7d0106fe67`.
- [Fifth-root augmentation](../active/hc7_k7minus_e5_k5minus_cut_elimination.md):
  `81306114489449f1bd2d8521c4aefc216411f81bf6721c7763412d4a7a87c6c0`.

Dvořák--Norin--Rahman Theorem 2.6 is accepted in the exact labelled form
already inspected for the five-root application. Norin--Totschnig Lemma 12
is accepted as recorded in the four-root input. The present audit does
not reconstruct the external proofs or expand the earlier audits.

## Exact excess and the punctured model

Six-connectivity makes every component full to the six-set and gives
at least six external neighbours for every nonempty subset of a component.
The previously proved bound `eta<=7` and the three-component edge identity
force all three excesses to equal seven and global excess to equal zero.

Deleting an isolated boundary vertex removes at most one neighbour from
each nonempty component subset, so the remaining five-rooted shore is
internally five-connected. Its density is exactly `7-a_L(s)`. If the
deleted vertex has at most three neighbours in the component, the density
is at least four. Every invoked target then contains the chosen six
missing root pairs. The three literal triangle edges complete the rooted
model to `K5^-`.

The two added bags are `M union {s}` and `N`. Both are connected and
boundary-full; they are adjacent through `s`, which was excluded from
the rooted shore. They are disjoint from its five bags and from each
other. Only the designated root-pair contact may be absent. This proves
the neighbour lower bound for each isolated boundary vertex in each
component.

## Connectivity and the virtual-edge lift

All five added edges at the isolated vertex `r` are new. The exact
auxiliary edge count is `4|C|+7+3+5=4|V(H)|-9`, meeting the four-root
helper threshold.

The two connectivity tests are separate and valid. A nonempty component
subset in a root-free fragment of boundary at most three acquires at
most the two omitted vertices `x,y` when viewed in the original graph,
contradicting its six-neighbour bound. Fragments consisting only of those
omitted vertices have at least four component neighbours. With `x` also
prescribed, a fragment of boundary at most four similarly acquires at
most `y`; the remaining singleton case has four component neighbours
and the new neighbour `r`. Thus both exact rooted hypotheses hold.

The helper model can therefore retain `x` in one helper. Its four root
bags form a clique using the literal triangle and three added edges.
Every added edge has the same endpoint `r`, so all can be realised by
enlarging only the bag at `r` with the reserved component `A`. This
preserves both internal bag connectivity and contacts between bags:
the connected component meets `r` and every required opposite endpoint.
No other bag uses `A`, and a bag not containing `r` uses no added edge
internally. Thus the lift has fixed disjoint ownership.

The remaining component `D` supplies the seventh bag. It contacts the
four root bags and the helper containing `x`; only its contact with the
other helper may be absent. This is a `K7^-` model in the original graph.

No unresolved inference was found. This closes the stated triangle
boundary case only. Other sparse boundaries, the two-component case,
the global density theorem, C21 and HC7 are not certified.

The final source pin removes only a redundant blank line at end of file
from revision `93831dc54aec65e84bf0d3015c4f4a6f907027ac745afb65959ca9f923cb660e`. The mathematical text is unchanged.
