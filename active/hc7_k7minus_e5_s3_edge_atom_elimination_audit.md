# Internal audit: elimination of the three-separator edge atom

**Verdict:** GREEN for the pinned source revision.  This is a separate
internal mathematical audit, not external peer review.

**Audited source:**
`active/hc7_k7minus_e5_s3_edge_atom_elimination.md`

**SHA-256:**
`63e9087752b66a0334d28ea555e40dbde9a7f4dad60d016c04329470e89e9a3a`

No mathematical correction is required at this revision.

## Revision history and repaired finding

The earlier source revision
`47a65bd011a0cebe8e8a224a3cb9c984753461096ff746dafbbc408d664263a3`,
was **RED**.  It did not exclude the selected root `t` from the exceptional
low `K_2`, but nevertheless inferred that both low roots belonged to `U`.
When `L={t,u_t}`, the guaranteed edge `pt` is exceptional to `U`, and the
old seven-bag list could have the two missing adjacencies `t B_b` and
`u_t B_q`.

The current revision repairs that exact gap.  It splits `t notin L` from
`L={t,u_t}`, computes the latter shore's excess using the optional edge
`q u_t`, invokes the already audited maximum-excess tie-break when that
edge is absent, and checks the corrected seven-bag model when it is
present.  The GREEN verdict applies only to the current hash pinned above.

Relative to the repaired GREEN revision
`c9bbcc1e8150d47c290dfb2ff685e1be1956c6160891cf766e0acb7becf93cb6`,
the final source changes only its status text to link this adjacent audit.
Its mathematical content is unchanged.

## 1. Edge-atom neighbourhoods and excess

The order-three atom supplied by Theorem 6 of the atomic reduction has

```text
C={p,b},                    N_F(C)=U,                    |U|=3,
N_G(C)=U union {t,q}.
```

The fixed singleton-row incidences give `pt,pq,bq,pb`, while `bt` is
absent.  Vertices of `A` have no neighbours in `{x,y}`.  Since `b` is
complete to `U` and `p` meets the subset `U_p`, the individual
neighbourhoods in the source are exact:

```text
N_G(b)={p,q} union U,
N_G(p)={b,t,q} union U_p.
```

For `k=|U_p|`, the atom has one internal edge and `k+6` incidences with
`U union {t,q}`.  Its excess is consequently

```text
1+(k+6)-4(2)=k-1.
```

## 2. The excess-one atom becomes a singleton atom

When `k=2`, the set

```text
U'={b} union U_p
```

has order three and is `N_F(p)`, while
`N_G(p)=U' union {t,q}` has order five.  Deleting this latter set isolates
`p`.

The connected-exterior argument is complete.  A component of `F-U'`
other than `{p}` which missed all four roots in `Z` would lie in the
dense side, avoid `p,b`, and have no neighbour in `{x,y,t,q}`.  Its
neighbourhood in `G` would therefore be contained in the three-set `U'`,
contrary to five-connectivity.  Since `b` is not a root, deleting `U'`
removes at most two vertices of `Z`; at least two roots survive.  The
undeleted twins `x,y` join all root-containing components.  Thus
`G-N_G(p)` has exactly the singleton `{p}` and one connected exterior.

The density identity is also exact: `d_F(p)=3`, so deleting `p` from
`|E(F)|=4|V(F)|-8` leaves

```text
|E(F-p)|=4|V(F-p)|-7.
```

## 3. Density-safe contraction and exact lifted cut

Assume `k=3`.  From the exact neighbourhoods,

```text
N_G(b) intersect N_G(q)={p} union (U intersect R_0),
```

which has order at most three.  Contracting `bq` therefore loses the
contracted edge and at most three duplicate edges.  The proper target-free
minor remains at or above `4|V|-7`.

Minimality makes `G/bq` non-five-connected.  The source's
four-connectivity argument is valid: a cut of order at most three either
lifts unchanged, if it avoids the contracted vertex, or lifts after that
vertex is replaced by `b,q`, producing a cut of `G` of order at most four.
Both alternatives contradict five-connectivity.  Hence a minimum cut of
`G/bq` has order four.  It contains the contracted vertex, since an
avoiding four-cut would lift unchanged.  Replacing it by `b,q` gives the
exact five-cut

```text
Q'={b,q} union D,                    |D|=3.
```

Every component behind `Q'` is full to it, as required later.

## 4. Placement of the twins

If exactly one twin lies in `D`, fullness at that twin puts a surviving
root in every complementary component, while the other twin joins all
such roots.  This contradicts that `Q'` is a cut.

If neither twin lies in `D`, the twins and all surviving roots form one
component `K`.  Every other component must contain a neighbour of `q`;
all surviving root-neighbours of `q` are in `K`, leaving only `p`.
Therefore there is exactly one other component `P`, containing `p`.
At least two roots survive the three-set `D`, so `|K|>=4`.  The universal
five-cut excess lemma and minimum choice of `|A|` then put the high
component on the `K` side and give `|P|<=2`.

The edge `pt` forces `t in D`.  Inside `F`, fullness and the component
decomposition give exactly

```text
N_F(P)={b} union (D-{t}).
```

If `P` had a second vertex, it would be in `X` and have at most its mate
and these three neighbours, contrary to minimum degree five.  Thus
`P={p}` and fullness gives `d_G(p)=5`, contradicting the six neighbours
in the `k=3` neighbourhood formula.

It follows that `D={x,y,v}`.  If `v` were not `p`, all neighbours of `b`
outside the cut would lie in

```text
{p} union (U-{v}),
```

which is connected because `p` is adjacent to every surviving member of
`U`.  Fullness at `b` would put every complementary component into that
one component.  Hence `v=p` and

```text
Sigma={b,p,q,x,y}.
```

## 5. Components and excess behind `Sigma`

The induced graph on `Sigma` consists exactly of the triangle `bpq` and
the isolated vertices `x,y`.  Every component behind this cut contains a
root through fullness at `x`.  The universal high-excess lemma gives one
component of order at least `|A|`, leaving at most two vertices outside
it.  A singleton low component is impossible because its root-neighbour
in `G[S]` also survives `Sigma`.  Thus there are exactly two components:
a high component `K` and an edge `L` of order two.

Both vertices of `L` are roots.  An `A`-vertex there would have at most
its mate, the three possible neighbours `b,p,q`, and no neighbour in
`{x,y}`, giving degree at most four.  No root lies in `Sigma`, so the two
roots of `L` must be the whole `K_2` component of
`G[S]=P_3` disjoint union `K_2`.

If `t notin L`, both low roots belong to `U`.  For either root outside
`U`, the exact neighbourhoods would exclude its edges to both `b` and
`p`; together with its mate, `x,y`, and at most `q`, this would give degree
at most four.  Since `k=3`, one has `U_p=U`, so both low roots are adjacent
to `b,p,x,y`.  Fullness at `q` gives at least one low-root--`q` edge.  If
`r` is their number, then `r in {1,2}` and

```text
delta_Sigma(L)=1+8+r-8=1+r in {2,3}.
```

The exact cut identity, with three edges in `G[Sigma]`, now gives

```text
delta_Sigma(K)=9-r in {7,8}.
```

The former RED case is `L={t,u_t}`.  Here `t notin U`, and its exact
boundary neighbours in `Sigma` are `p,q,x,y`; in particular, `tb` is
absent.  The mate `u_t` must belong to `U`: otherwise it has only its
mate, `x,y`, and possibly `q`, again at most four neighbours.  Thus
`u_t` is adjacent to `b,p,x,y`.  Put

```text
epsilon=1 if q u_t is an edge, and epsilon=0 otherwise.
```

The two endpoints have respectively four and `4+epsilon` incidences with
`Sigma`, so exact accounting gives

```text
delta_Sigma(L)=1+epsilon,
delta_Sigma(K)=9-epsilon.
```

As established above, `|K|=|A|`.  If `epsilon=0`, the cut therefore has
a high-excess component of the same globally minimum order as `A` but
with excess nine, contradicting the imported maximum-excess choice
`delta_S(A)=8`.  Hence the only surviving `t in L` case has `epsilon=1`
and `delta_Sigma(K)=8`.

## 6. Rooted supply and branch-set verification

The closed `K`-shore is internally five-connected.  In the cut graph
`G[Sigma]`, the nominated vertex `y` has degree zero, while
`delta_Sigma(K)>=7`.  The rooted six-bag supply therefore applies with
roots `Sigma-{y}` and places `y` in one helper `U_y`.

Let the root bags be `B_b,B_p,B_q,B_x` and the other helper be `V`.
Absorbing `V` into `B_x` preserves connectivity and disjointness.  The
bags `B_b,B_p,B_q` are pairwise adjacent through the literal triangle
`bpq`, and `V` supplies all three adjacencies from `B_x union V`.  These
four bags therefore form a clique model.

For the seven displayed bags in the source, the common required
adjacencies are:

- six among the four clique bags;
- four from `U_y` to those bags;
- one between the two low roots;
- two from `U_y` to the low roots through `y`; and
- the root-bag contacts described in the following two cases.

When `t notin L`, each low root meets `B_b,B_p,B_x union V` through
`b,p,x`, respectively, and at least one meets `B_q`.  Thus only the other
low-root--`B_q` adjacency may be absent.

When `L={t,u_t}`, the preceding excess argument leaves only
`epsilon=1`.  The vertex `u_t` then meets all four root bags through
`b,p,q,x`.  The vertex `t` meets `B_p,B_q,B_x union V` through `p,q,x`,
and only `t B_b` may be absent.  In either case at least twenty of the
twenty-one branch-set pairs are adjacent.

All seven bags are connected and pairwise disjoint: the six-bag model
lies in `K union Sigma`, while the two singleton low bags lie in the
other component.  This is an explicit `K_7^-`-minor model in every branch
which survives the maximum-excess contradiction.

## 7. Dependencies and remaining scope

The dependency revisions checked were:

```text
atomic six-boundary reduction:
3f2084f172183f38b91aa5a9ef402d2c60095579dda915fa6fcadaabfe94edff

companion-cut elimination:
6acfe24187c99c5da3439e72ebdee4c72b32a38eeae0df08116689237d6bc22e

singleton-contraction theorem:
e4720b2641033396aabf333cc97d9f401df4577f8a6f337a44d7ca6aba0ac1c2

two-component rooted reduction:
e77dded1d9459f167f1f636832f9c4b46633172f8f8272b478cdf3f834fbc940
```

All four have adjacent hash-pinned GREEN audits.  The edge-atom theorem
uses the earlier universal five-cut excess lemma and rooted six-bag
supply without feeding its own conclusion into either source, so the
dependency chain is non-circular.

The theorem eliminates the excess-two edge atom and re-expresses the
excess-one edge atom as the singleton order-three atom with a different
adhesion.  The exact remaining obstruction in this `s=3` row is that
singleton atom; the separate `s<=2` singleton orientations also remain.
The theorem therefore does not prove `(E5)` or the primary seven-connected
theorem.
