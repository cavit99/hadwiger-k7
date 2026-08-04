# Internal audit: anchored four-root reduction

**Verdict:** GREEN for the pinned source revision.  This is a separate
internal mathematical audit, not external peer review.

**Audited source:**
`active/hc7_k7minus_e5_anchored_four_root_reduction.md`

**SHA-256:**
`b22556c8dc6fa22bbd950d53356c6dc46826e755173ca4a36b3fb5425c0995d8`

No mathematical correction is required at this revision.

## 1. Four-root deletion and exact density

For a degree-five leaf root `t`, its neighbours in the closed shore are
exactly

```text
N_H(t)={u_t} union P_t,              |P_t|=2.
```

Thus `d_H(t)=3`, and deleting `t` from
`|E(H)|=4|V(H)|-9` gives

```text
|E(H-t)|=4|V(H-t)|-8.
```

The internal-connectivity argument was checked against the definition in
Norin--Totschnig.  If `(U,V)` is a separation of `(H-t,S-{t})` of order at
most three with `V-U` nonempty, then `V-U` lies in `A`.  It has no edge to
`x` or `y`, no edge to a root in `U-V`, and, after restoring `t`, no edge
outside through `t` once `t` is put in the separator.  Hence

```text
(U intersect V) union {t}
```

is a cut of `G` of order at most four.  A root of the four-set
`S-{t}` survives in `U-V`, so both sides are nonempty.  This contradicts
five-connectivity and proves that `(H-t,S-{t})` is internally
four-connected.

## 2. The two rooted-model supplies

Norin--Totschnig, arXiv:2507.03244v1, was checked directly:

- Lemma 9 says that an internally four-connected pair with four roots and
  no rooted `K_4` model has at most `3v-7` edges.
- Lemma 12 says that such a pair with no rooted `K^*_{4,2}` model has at
  most `4v-10` edges.

The strict inequalities in the source are therefore sufficient.  The
singleton-contraction theorem gives `|A|>=7`, hence `|V(H-t)|>=11`, and

```text
4|V(H-t)|-8 > 3|V(H-t)|-7,
4|V(H-t)|-8 > 4|V(H-t)|-10.
```

Both rooted models asserted in Corollary 2 follow.

The original cut `(V(G)-A,A union S)` has order five.  Five-connectivity
therefore makes `(H,S)` internally five-connected.  The audited
fifth-root augmentation lemma applies to the `Z`-rooted
`K^*_{4,2}` model viewed in `H`, and places `t` in a helper.  The helper
cannot be `{t}`, since `t` has only three neighbours in `H` and hence can
meet at most three disjoint root bags.  Its connectedness and disjointness
from the root bag containing `u_t` force it to contain a vertex of `P_t`.
No adjacency among the four root bags is inferred here.

## 3. Sufficiency of the anchored model

Given the five bags in Lemma 4, the seven displayed branch sets are
disjoint and connected.  Their adjacencies were checked individually:

- `{x,t}` meets `R` through `tp`, every `B_z` through `xz`, and `{y}`
  through `ty`;
- `{y}` meets each `B_z` through `yz`; and
- the five bags inside `H-t` are pairwise adjacent by hypothesis.

Thus `{y}`--`R` is the sole possibly missing adjacency.  This is an
explicit `K_7^-`-minor model, so the anchored conclusion is indeed
sufficient and is strictly weaker than demanding an `S`-rooted `K_5`
model in `H`.

## 4. Three--two carriers

Du--Li--Xie--Yu, *Journal of Combinatorial Theory, Series B* 169 (2024),
Theorem 1.2, DOI `10.1016/j.jctb.2024.06.006`, was checked against the
published theorem statement and arXiv:2303.12146v1.  For `m=3`, an
infeasible rooted graph admits a terminal collection whose members have
neighbourhood order at most four and whose completed quotient has at most

```text
4v-10
```

edges.  The completion adds every terminal edge except the nominated
`b_1b_2` edge.

In the source application, every nonempty collection member lies in `A`.
Since `x,y` have no neighbours in `A`, its neighbourhood in `G` equals its
neighbourhood in `H`; deleting at most four vertices would separate it
from `x,y`.  Five-connectivity therefore excludes every nonempty member.
An empty member, if permitted, has no effect, so the quotient is still
`H`.

If `epsilon` records whether `b_1b_2` is already an edge, the completed
terminal graph has `9+epsilon` edges.  As `G[S]` has three edges, the
completion adds `6+epsilon` edges and gives

```text
4|V(H)|-9+6+epsilon=4|V(H)|-3+epsilon,
```

contradicting the infeasible bound `4|V(H)|-10`.  Feasibility gives a
`b_1`--`b_2` path and a disjoint component containing the three other
roots, exactly the two connected carriers claimed.  The proof does not
iterate carriers chosen for different partitions.

## 5. Boundary-contact count

The use of the root-only low sides from the singleton-contraction theorem
was checked for each boundary component.

- At an end of the `P_3`, the low side contains its unique boundary
  neighbour.  If it omits the opposite end, the middle root has at most
  one neighbour in `A`; if it contains that end, both relevant roots have
  at most two neighbours in `A`.
- Applying this at both ends gives `d_1<=2`, and if `d_1=2` then
  `d_0,d_2<=2`.
- The two ends of the `K_2` each have at most two neighbours in `A`.
- The low side at the middle of the `P_3` contains an end, giving
  `min(d_0,d_2)<=2`.

These inequalities give

```text
sum d_i <= |A|+7.
```

The exact shore identity is

```text
|E(G[A])|+sum d_i=4|A|+8.
```

Together with the simple-graph bound on `E(G[A])`, it yields
`|A|^2-7|A|-2>=0`, whose positive integral solutions have `|A|>=8`.
The arithmetic and all equality directions are correct.

## 6. Dependency and scope check

The following local source revisions were used:

```text
singleton-contraction theorem:
e4720b2641033396aabf333cc97d9f401df4577f8a6f337a44d7ca6aba0ac1c2

fifth-root augmentation source:
81306114489449f1bd2d8521c4aefc216411f81bf6721c7763412d4a7a87c6c0
```

Both have adjacent hash-pinned GREEN audits.  The carrier barrier cited by
the source is independently audited beside that barrier.  There is no
circular use of the present reduction: the earlier singleton theorem and
augmentation lemma do not depend on it, while the carrier barrier is an
independent six-vertex construction.

The anchored `K_5`-or-descent statement remains explicitly conjectural.
Neither the separate rooted-model supplies nor the three--two carriers
synchronise the four root bags with a selected `p`-containing helper.  The
source therefore does not prove `(E5)` or the primary seven-connected
extremal theorem.
