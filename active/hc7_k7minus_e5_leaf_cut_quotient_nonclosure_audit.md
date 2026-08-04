# Internal audit: contracted leaf-cut quotient nonclosure

**Verdict:** GREEN for the pinned source revision.  This is a separate
internal mathematical audit, not external peer review.

**Audited source:**
`active/hc7_k7minus_e5_leaf_cut_quotient_nonclosure.md`

**SHA-256:**
`cd69a799e80385f0182b08eb6bed3d5e6954d3169ec8437378dfd1e490cb2edd`

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

## 5. Closure of the four-root singleton row

When `s=4`, the cut has the form

```text
Q=R union {p},                    |R|=4,
```

and `B={p}`.  Since `tq_t` is an edge and `Q=N_G(q_t)`, the root `t`
belongs to `R`.  The singleton-neighbour boundary-collapse theorem is
therefore applicable with

```text
Q^*=(S-{t}) union {p},
E={x,y,t,q_t},
X=A-{p,q_t}.
```

The absence of edges between `E` and `X` follows from the exact
neighbourhoods of `x,y,t,q_t`.  The set `E` is connected through
`xt,yt,tq_t`.  Its three internal edges and fourteen incidences with
`Q^*` give

```text
delta_{Q^*}(E)=3+14-16=1.
```

Every component of `G[X]` has neighbourhood contained in `Q^*`; by
five-connectivity it is full to that five-set.  The universal five-cut
excess lemma cannot select `E`, so it supplies a component of `X` with
excess at least four and order below `a`.  This contradicts the chosen
minimum high-excess lobe.  The revised source is therefore correct to
discard `s=4`.

For every survivor, `1<=s<=3`.  The only neighbours of `t` in `A` are
`p,q_t`, both outside `X`; hence `t` has no neighbour in `X`.  Equation
(11) consequently sharpens to

```text
N_G(X) subseteq (S-{t}) union B,
|(S-{t}) union B|=4+(5-s)=9-s.
```

The three container orders are six, seven and eight for `s=3,2,1`,
respectively.  This is an upper bound on the actual neighbourhood order,
not an assertion that every possible boundary vertex is used.

## 6. Two-vertex orientation and contraction density

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

## 7. Dependency order, nonclosure and first gap

The source revisions used were:

```text
singleton-contraction theorem:
e4720b2641033396aabf333cc97d9f401df4577f8a6f337a44d7ca6aba0ac1c2

anchored four-root reduction:
b22556c8dc6fa22bbd950d53356c6dc46826e755173ca4a36b3fb5425c0995d8

singleton-neighbour boundary collapse:
32091e0beb5cad0721f2a4ae826bac80b9a5f1c4bbc8e21247ef8b8820f90345

E5 frontier consulted for the minimum-lobe endpoint:
2b70e6d2a890b4145106ee42e21be5b8afde34d05373d8f108062c92d2c1c24a
```

The apparent file-level cycle with the boundary-collapse theorem is not a
mathematical cycle.  That theorem uses only Theorems 3 and 4 and equations
(8)--(11) of the earlier quotient revision

```text
cd86151b6526af8be0bfc82f92e1cfb998ca6184d8328f62a4a3829d02a2ef49,
```

all of which are unchanged in the present source.  The present revision
then invokes the collapse only after those proofs to eliminate `s=4`.
Thus the theorem-level dependency order is base classification, boundary
collapse, revised survivor statement.

The result remains a route nonclosure, not a counterexample to the
anchored target or `(E5)`.  The first exact unsupported inference is now
the multi-neighbour boundary reduction for `s<=3`.  At `s=3`, the set
`X` is contained behind six possible boundary vertices and `B` has two
members.  Removing either dense-side member to obtain a five-set leaves
the other outside that set, where it may join the low exterior to `X`.
No proved argument both removes this sixth boundary vertex and preserves
excess at least four.  The `u_t` singleton and two-vertex low-side
orientations also remain open exactly as stated.
