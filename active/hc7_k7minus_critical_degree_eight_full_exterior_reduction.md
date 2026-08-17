# A critical degree-eight centre has a full exterior

**Status:** written proof with an adjacent author-side audit.  The result
reduces the all-codegrees-at-least-three branch to one connected component
which is full to the entire neighbourhood; it does not eliminate that full
component.

## Theorem

Let `G` satisfy

```text
chi(G)=7,
every proper minor of G is six-colourable,
kappa(G)>=7,
delta(G)>=8,
K_7^- is not a minor of G.
```

Let `v` have degree eight, put `J=G[N_G(v)]`, and suppose

```text
delta(J)>=3,   K_4 is not a subgraph of J,   alpha(J)=3.
```

If `G-N_G[v]` is nonempty, then it is connected and its unique component
`C` satisfies

```text
N_G(C)=V(J).
```

## Proof

The exterior-connectedness theorem shows that `G-N_G[v]` has at most one
component.  Let `C` be its nonempty component.  Seven-connectivity gives
`|N_G(C)|>=7`, so `C` is full to `J` or misses exactly one vertex `r`.

Suppose it misses `r`.  Since `r` has no exterior neighbour,

```text
8 <= d_G(r)=1+d_J(r),
```

and hence `r` is complete to `S=V(J)-{r}`.  The connected one-miss
reduction leaves four labelled pairs.  Only `(GhCKN{,7)` has the missed
vertex of local degree seven; in that pair

```text
J = r join C_7,
```

with `S` inducing the displayed seven-cycle.  Label it cyclically as
`s_0,...,s_6` and put

```text
I_1={s_2,s_4,s_6},   I_2={s_3,s_5},   Q={s_0,s_1}.
```

The sets `I_1,I_2` are independent and `Q` is a clique.  The two
singletons `{v},{r}` are disjoint connected `S`-full subgraphs and are
adjacent.  Apply the exact boundary-colouring reflection lemma from the
`{v,r}` shore, assigning `I_1,I_2` to `{v},{r}` and retaining the two
singleton blocks indexed by the clique `Q`.  It gives a proper
six-colouring of `G[C union S]` whose equality partition on `S` is exactly

```text
I_1 | I_2 | {s_0} | {s_1}.
```

Exactly four colours occur on `S`.  Give `v,r` the two remaining colours,
one each.  They are adjacent to one another and to every vertex of `S`,
and neither has a neighbour in `C`.  This extends the colouring to all of
`G`, contrary to `chi(G)=7`.

Thus the one-miss case is impossible and `C` is full to `J`. `\square`

## Frozen inputs and scope

The proof uses the following frozen revisions:

```text
3654719b95d3a6b3446d5c15630ee474b07725568cf38a4ad426d0a3635a1fcf
  active/hc7_k7minus_sevenconnected_degree_eight_exterior_connectedness.md
bda284fabf9a414f73dee683474be3cf00d1bc973bc4d51c8f43b8d7771ad607
  active/hc7_k7minus_sevenconnected_degree_eight_one_miss_reduction.md
b27f6cacd4122e01efb65d4d714f28d2a7da7ff7552768cbec2281d9de8ef5c0
  active/experiments/sevenconnected_connected_exterior_profiles/verify.py
d4d650fee168fc2ff0e00a3b7b0faed6ff674ba8cd3c06c263f63c4170656f34
  results/hc7_k7minus_critical_seven_cut_capacity.md
```

Only Lemma 1, the exact boundary-colouring reflection, is used from the
last file.  The minimum-degree-eight hypothesis is essential to the short
reduction: minimum degree seven leaves all four one-miss residues.

The theorem does not treat an empty exterior and does not yet prove an
incident edge of codegree at most two.  It isolates the only remaining
nonempty case as a connected `J`-full exterior of arbitrary order.
