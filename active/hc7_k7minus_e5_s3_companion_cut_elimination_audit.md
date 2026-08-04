# Internal audit: companion-cut elimination of the four-separator atom

**Verdict:** **GREEN** for the pinned source revision.  This is a separate
internal mathematical audit, not external peer review.

**Audited source:**
`active/hc7_k7minus_e5_s3_companion_cut_elimination.md`

**SHA-256:**
`6acfe24187c99c5da3439e72ebdee4c72b32a38eeae0df08116689237d6bc22e`

No mathematical correction is required at this revision.  The argument is
computation-free.

Relative to the previously audited revision
`225268556f3ab70e628cab8511e290658030c796aa3c15b9a6787f096de54654`,
the source changes only its status text to link this adjacent audit.  Its
mathematical content is unchanged, so the GREEN verdict is retained.

## 1. Initial choice and exact excess

The source refines the existing global minimum-lobe choice
lexicographically: first minimise `|A|` over every component of excess at
least four behind every five-cut, and then maximise its excess.  This
refinement is legitimate.  There are finitely many cut--component pairs,
and every earlier dependency used only the first coordinate, namely that
no high-excess component has order below `|A|`.  None imposed an
incompatible secondary choice.  Thus all previously proved order
comparisons and strict-descents remain valid.

In the exact two-singleton branch, `G-S` has components `A,{x},{y}`.
Each singleton has excess one, while the cut identity and
`|E(G[S])|=3` give

```text
delta_S(A)+1+1=13-3.
```

Hence `delta_S(A)=8`, as asserted.  The later pair `(Sigma,L)` is compared
against the same global lexicographic choice, rather than against a choice
restricted to the present boundary type.

## 2. Density-safe contraction and lifted cut

In the excess-two normal form,

```text
N_G(b)={q,c} union T,
N_G(q)={t,p,b} union R_0,
|T|=4,                         |R_0|=2,
t notin T.
```

The vertex `c` is outside `N_G(q)`, so

```text
N_G(b) intersect N_G(q)=T intersect ({p} union R_0),
```

which has order at most three.  Contracting the edge `bq` therefore
removes the edge itself and at most three duplicate edges.  Since the
minimum enemy has exactly `4|V(G)|-7` edges, the contraction satisfies

```text
|E(G/bq)|>=4|V(G/bq)|-7.
```

It is a proper target-free minor.  Were it five-connected, it would be a
smaller `E5` enemy.  Thus it has a cut of order at most four.  Such a cut
must contain the contracted vertex; otherwise contraction of the adjacent
pair `b,q` does not change the component structure after deleting that
cut, and the same set would cut `G`.  Replacing the contracted vertex by
`b,q` lifts the cut to one of order at most five in `G`.  Five-connectivity
forces equality throughout, yielding the exact cut

```text
Q'={b,q} union D,                |D|=3.
```

Every component behind this minimum cut is full to all five cut vertices.

## 3. The two twin cases and the vertex `c`

If exactly one of `x,y` lies in `D`, fullness at that twin forces every
component of `G-Q'` to contain a surviving root.  The other twin survives
and is adjacent to every such root, joining all components.  This is
impossible.

If neither twin lies in `D`, the surviving twins and all surviving roots
form one component `K`.  Every other component must contain a neighbour
of the cut vertex `q`.  Outside `K` and `Q'`, its only possible neighbour
is `p`, so there is exactly one other component `P`, with `p in P` and
`P subseteq A`.  At least two roots survive, so `|K|>=4`.  The universal
five-cut excess lemma supplies a component of order at least `|A|`; since
there are `|A|+2` vertices outside the cut, `K` must be that component and
`|P|<=2`.

The edge `pt` forces `t in D`.  Intersecting the exact neighbourhood of
`P` with `F=G-{x,y,t,q}` then gives

```text
N_F(P)={b} union (D-{t}),         |N_F(P)|=3.
```

The component `P` contains `p` and no root in `Z`, so this is a forbidden
order-three rooted separation of the standing internally four-connected
pair `(F,Z)`.  Hence both twins lie in `D`, and `D={x,y,v}`.

If `v!=c`, every neighbour of `b` outside `Q'` lies in

```text
{c} union (T-{v}).
```

This set is nonempty and connected because `c` is adjacent to every
member of `T`.  Fullness at `b` forces every component behind `Q'` to
contain a vertex of this one connected set, again making all components
coincide.  Thus `v=c`, and the lifted cut is exactly

```text
Sigma={b,c,q,x,y}.
```

The only edges inside `Sigma` are `bc` and `bq`.

## 4. Components behind the companion cut

Fullness at `x`, together with `N_G(x)=S`, makes every component of
`G-Sigma` contain a member of `S`.  A high-excess component has order at
least `|A|`, leaving at most two vertices outside it.  No other component
can be a singleton: its sole vertex would lie in `S`, while every vertex
of `P_3` disjoint union `K_2` has a neighbour in `S`, and no root was
deleted by `Sigma`.  Consequently `G-Sigma` has exactly two components,
of orders `|A|` and two.

Let `P` be the two-vertex component.  If only one of its vertices lay in
`S`, its other vertex would lie in `A` and have at most one neighbour in
`P` and at most the three possible neighbours `b,c,q` in `Sigma`; it has
no neighbour in `x,y`.  This contradicts minimum degree five.  Thus both
vertices lie in `S`.  They form an edge, and no edge of `G[S]` leaves
`P`, because no root belongs to `Sigma`.  Therefore `P` is exactly the
`K_2` component of `G[S]`.

The selected root `t` is not in `P`, since `p` survives the cut and `pt`
is an edge.  Thus `t` is an end of the `P_3`; writing that path as
`t-a-d` and the small component as `{u,v}`, Corollary 10 of the atomic
reduction leaves only `R_0={a,u}` or `R_0={a,v}`.  The renaming for which
`q` meets `u` and misses `v` is therefore valid.

## 5. Exact neighbourhoods and excess accounting

Because `{u,v}` is a component after deleting `Sigma`, the vertex `v`
has the known neighbours `u,x,y` and can have no further neighbours except
`b,c`; it misses `q`.  Minimum degree forces both `vb` and `vc`.  The
exact neighbourhoods of `b,c` then put `v in T`.

Similarly, `u` has the four known neighbours `v,q,x,y`.  It must meet at
least one of `b,c`; either edge places `u in T`, after which completeness
of both `b,c` to `T` supplies both edges.  Component separation excludes
all other neighbours.  Hence the displayed exact neighbourhoods are

```text
N_G(v)={u,b,c,x,y},
N_G(u)={v,b,c,q,x,y}.
```

The edge `{u,v}` has one internal edge and exactly nine incidences with
`Sigma`: four to `x,y`, four to `b,c`, and `uq`.  Therefore

```text
delta_Sigma({u,v})=1+9-4(2)=2.
```

For any five-cut in the exact `4n-7` graph, component excesses sum to
`13-|E(G[cut])|`.  Since `G[Sigma]` has two edges, the sum here is eleven.
The other component `L` consequently has

```text
|L|=|A|,                         delta_Sigma(L)=11-2=9.
```

This is a high-excess component of the same minimum order as `A` but with
excess `9>8`.  It contradicts the globally maximum-excess tie-breaker.
Thus the four-separator normal form is eliminated, and in the target-free
branch failure of internal four-connectivity leaves exactly the two
order-three atoms stated in Theorem 6 of the atomic reduction.

## 6. Dependencies and scope

The direct dependency revisions checked were:

```text
atomic six-boundary reduction:
eccb5d2e0181f0f7005bd7e86dce7f04b6bd9eb2f3eb5bd1e20a00a2f86afc34

singleton-contraction theorem:
e4720b2641033396aabf333cc97d9f401df4577f8a6f337a44d7ca6aba0ac1c2
```

Both have adjacent hash-pinned GREEN audits.  The companion-cut argument
does not prove `(E5)` and does not close the surviving order-three atoms.
