# Internal audit: contracted leaf-cut quotient nonclosure

**Verdict:** GREEN for the pinned source revision.  This is a separate
internal mathematical audit, not external peer review.

**Audited source:**
`active/hc7_k7minus_e5_leaf_cut_quotient_nonclosure.md`

**SHA-256:**
`cd86151b6526af8be0bfc82f92e1cfb998ca6184d8328f62a4a3829d02a2ef49`

No mathematical correction is required at this revision.

## 1. Number of complementary components

For the exact five-cut `Q=Q_{t,p}`, the audited singleton-contraction
theorem gives one high-excess component `D` of order `a` or `a+1`, with
all remaining components having total order at most two.  If there were
two low components, both would be singleton vertices adjacent to `t`.
The degree-five description leaves only `u_t,q_t` after excluding `x,y`
by their nonadjacency to `p`.

If `t` lies in the `P_3` component of the boundary, a singleton `u_t`
would have degree five while having boundary degree two, contrary to the
audited strict-descent theorem.  If `t` lies in the `K_2` component, the
identity `N_G(u_t)=Q` puts `x,y` in `Q`, so fullness of the other singleton
`q_t in A` would make it adjacent to `x,y`.  Both cases are impossible.
Thus there is exactly one low component `L`.

After contracting `D` and `L`, the two resulting vertices are nonadjacent
and each adjacent to all five vertices of `Q`.  The quotient therefore has
exactly

```text
10+|E(G[Q])|
```

edges.

## 2. Excess accounting and automatic target-freeness

A singleton low component has excess one.  A two-vertex low component is
an edge, and minimum degree five gives at least eight incidences with
`Q`, so it also has excess at least one.  Exact accounting at a five-cut
in a graph with `4n-7` edges gives

```text
delta_Q(D)+delta_Q(L)=13-|E(G[Q])|.
```

Since the two excesses are at least four and one, respectively,
`|E(G[Q])|<=8`.  Hence the seven-vertex quotient has at most eighteen
edges.  A minor model with seven nonempty bags in a seven-vertex graph
uses singleton bags, while `K_7^-` has twenty edges.  Its target-freeness
is therefore automatic, exactly as claimed.

## 3. Low-side classification

When `L` is a singleton, adjacency to `t` and fullness to `Q` leave the
two possibilities `u_t` and `q_t`.

- If `L={u_t}`, the path-centre case is excluded, so `t,u_t` are the
  `K_2` boundary component.  Then
  `Q=N_G(u_t)={x,y,t} union P_{u_t}`.  The high component must meet `t`;
  after locating `x,y,p` in `Q` and `u_t` in `L`, its only possible
  `t`-neighbour is `q_t`, so `q_t in D`.  The only optional cut edge is
  the edge within `P_{u_t}`, giving three or four boundary edges.
- If `L={q_t}`, then `Q=N_G(q_t)` excludes `x,y`.  The neighbours of `t`
  inside `Q` are `p` and possibly `u_t`, giving cut degree one or two.

If `|L|=2`, it is an edge.  Each endpoint has four or five neighbours in
`Q`, and fullness prevents both from missing the same cut vertex.  This
gives precisely the incidence counts `8,9,10` and excesses `1,2,3`.
There are `a+2` vertices outside `Q`, so `|D|=a`; the minimum high-excess
lobe reduction then gives `|E(G[Q])|<=6`.

## 4. Singleton orientation and exact potential

For `L={q_t}`, the order identities follow directly from
`Q=N_G(q_t)`, `x,y notin Q`, and `p in A intersect Q`.  In particular,

```text
|D|=a+1,
X=A intersect D=A-(B union {q_t}),
|X|=a+s-6<a.
```

The incident-edge excess identity

```text
epsilon(U intersect W)+epsilon(U union W)
 =epsilon(U)+epsilon(W)-|E_G(U-W,W-U)|
```

was recomputed edge by edge.  Here `epsilon(A)=8`,
`epsilon(D)=12-k`, and the complement of `A union D` is `R`, giving

```text
epsilon(A union D)=4s-7-|E(J[R])|.
```

Moreover, the cross-corner edges are exactly
`E_G(B,S-Q)`: vertices of `A` miss `x,y`, and `q_t` has no neighbour
outside `Q`.  Substitution yields equation (10) of the source.

When `s=4`, `B={p}` and

```text
epsilon(X)=11-d_S(p)>=6.
```

The connectedness of `A` forces `p` to meet `X`, since `p,q_t` are
adjacent and `q_t` has no neighbour in `X`.  The source correctly stops
here: a component of `X` need not have an order-five boundary while
retaining excess at least four.

The companion observation is also valid.  If its low side is `{p}`, then
`p,q_t` are adjacent degree-five vertices.  Four common neighbours would
form a four-cut isolating their edge, so they have at most three common
neighbours.  Contracting their edge consequently loses at most four edges,
retains the `E5` density, and the standard minimum-enemy argument supplies
another exact five-cut.  No descent is inferred from that cut.

## 5. Two-vertex orientation and contraction density

If `x` belonged to the two-vertex low edge, its mate would be the fifth
root outside `Q`, while the other four members of `Q` apart from
`p in A` would be roots.  The surviving vertex `y` would join the mate to
the other component, contradicting the component decomposition.  The same
holds for `y`.  Fullness to `t` then forces the low edge to contain
`u_t` or `q_t`.

Contracting `L union {z}` makes `z` adjacent to every other cut vertex and
adds the `mu_Q(z)` missing star edges.  With

```text
delta_Q(D)+delta_Q(L)=13-|E(G[Q])|,
```

the resulting minor has at least

```text
4|D|+13-delta_Q(L)+mu_Q(z)
```

edges on `|D|+5` vertices.  Thus `mu_Q(z)>=delta_Q(L)` is exactly the
condition for the `4v-7` threshold.  The source does not assert the
unproved five-connectivity of this minor.

## 6. Dependency, nonclosure and scope

The following source revisions were used:

```text
singleton-contraction theorem:
e4720b2641033396aabf333cc97d9f401df4577f8a6f337a44d7ca6aba0ac1c2

anchored four-root reduction:
b22556c8dc6fa22bbd950d53356c6dc46826e755173ca4a36b3fb5425c0995d8

E5 frontier consulted for the minimum-lobe endpoint:
588c6bdccacff21d8c95ff14375dc97d3eb289626467f4c4d79209b6ad5bbb28
```

The singleton theorem has an adjacent hash-pinned GREEN audit.  The
present note uses the anchored reduction only for notation and for the
statement of the desired endpoint; the anchored proof does not depend on
this quotient classification, so there is no circular inference.

The result is a recorded route nonclosure, not a counterexample to the
anchored target or `(E5)`.  It proves that target-freeness of the fully
contracted seven-vertex quotient supplies no extra restriction.  The two
proposed boundary-collapse and edge-completion statements remain open and
are correctly labelled as repairs rather than conclusions.
