# Contracted leaf-cut quotients do not retain the rooted obstruction

**Status:** active computation-free written proof and recorded route
nonclosure, not a counterexample; see the
[adjacent audit](hc7_k7minus_e5_leaf_cut_quotient_nonclosure_audit.md) for
independent verification.

This note works in the exact two-singleton residue and uses the notation of
the [anchored four-root reduction](hc7_k7minus_e5_anchored_four_root_reduction.md).
It classifies the bounded quotient of each further leaf-edge cut.  The
classification shows that target-freeness of that quotient is automatic
and therefore cannot by itself synchronize the required rooted model.

Fix `t in T` and `p in P_t`, let `q_t` be the other member of `P_t`, and
let

```text
Q=Q_{t,p}
```

be the exact five-cut supplied by the singleton-contraction theorem.  Let
`D` be the unique component of `G-Q` with excess at least four.  That
theorem gives

```text
|D| is |A| or |A|+1,
```

and all other components together have order at most two.

## Theorem 1 (there is exactly one low component)

The graph `G-Q` has exactly two components: the high component `D` and
one low component `L`.  Consequently, contracting `D` and `L` produces a
seven-vertex quotient, never an eight-vertex quotient.

### Proof

There is at least one low component because `Q` is a cut.  If there were
two, their total order bound would make both singleton components; call
their vertices `l_1,l_2`.  Every component behind a five-cut is adjacent
to all five cut vertices, so both `l_i` are adjacent to `t`.

By the degree-five leaf description,

```text
N_G(t)={x,y,u_t,p,q_t}.
```

The vertex `p` lies in `Q`.  Neither `x` nor `y` can be a singleton
component full to `Q`, because each is nonadjacent to `p in A`.  Hence

```text
{l_1,l_2}={u_t,q_t}.                                  (1)
```

Both vertices in (1) would have neighbourhood exactly `Q` and therefore
degree five.  If `t` is a leaf of the `P_3` component of `J`, then `u_t`
is the degree-two vertex of that path.  This is excluded in the surviving
branch by the strict-descent theorem for a degree-two boundary root.

If `t` is a vertex of the `K_2` component of `J`, then `u_t` is its other
end and `N_G(u_t)=Q` contains `x,y`.  But `q_t in A`, as the other
singleton component, would also be adjacent to every member of `Q`, and
in particular to `x,y`.  This contradicts the fact that `x,y` have no
neighbours in `A`.  Thus two low components are impossible.  \(\square\)

## Theorem 2 (the seven-vertex quotient is automatically target-free)

Contract `D` and `L` to vertices `d,l`, respectively.  The resulting
quotient consists of two nonadjacent vertices which are each universal to
`Q`, together with `G[Q]`; equivalently, it is

```text
G[Q] join two nonadjacent universal vertices d,l,
```

and has

```text
10+|E(G[Q])|                                             (2)
```

edges.  Moreover,

```text
|E(G[Q])|<=8.                                           (3)
```

Thus the quotient has at most 18 edges and is automatically
`K_7^-`-minor-free.

### Proof

Distinct components of `G-Q` are nonadjacent, and both `D,L` are adjacent
to every vertex of `Q`.  This proves the description and (2).

The low component has excess at least one.  This is immediate when it is
a singleton.  If it has two vertices, it contains their joining edge, and
minimum degree five gives each endpoint at least four neighbours in `Q`.
Its excess is then at least

```text
1+8-4(2)=1.
```

Exact accounting at the five-cut gives

```text
delta_Q(D)+delta_Q(L)=13-|E(G[Q])|.
```

Since `delta_Q(D)>=4` and `delta_Q(L)>=1`, inequality (3) follows.

A minor model with seven nonempty branch sets in a seven-vertex graph
uses every vertex as a singleton.  Such a graph contains `K_7^-` exactly
when it has at least 20 edges.  The quotient has at most 18, so its
target-freeness adds no further restriction.  \(\square\)

## Theorem 3 (exact low-side types)

The low component has one of the following forms.

1. `L={u_t}`.  Then `t` is a vertex of the `K_2` component of `J`,
   `u_t` is its other end, and

   ```text
   Q=N_G(u_t)={x,y,t} union P_{u_t},
   p in P_{u_t},                     q_t not in Q,
   |E(G[Q])| is 3 or 4.                              (4)
   ```

2. `L={q_t}`.  Then

   ```text
   Q=N_G(q_t),                     x,y not in Q,
   d_{G[Q]}(t) is 1 or 2.                            (5)
   ```

3. `|L|=2`.  Then `L` is an edge.  If

   ```text
   f=|E_G(L,Q)|,
   ```

   then

   ```text
   f is 8, 9 or 10,
   delta_Q(L)=f-7 is 1, 2 or 3,                      (6)
   |D|=|A|,                       |E(G[Q])|<=6.       (7)
   ```

   When `f=8`, the two ends of `L` miss two distinct vertices of `Q`,
   one each.  When `f=9`, exactly one endpoint--boundary incidence is
   absent.  When `f=10`, both endpoints are complete to `Q`.

### Proof

If `L` is a singleton, it is adjacent to `t` and full to `Q`.  The proof
of Theorem 1 shows that its vertex is `u_t` or `q_t`.

Suppose first that `L={u_t}`.  The degree-two path-centre case was excluded
in Theorem 1, so `t,u_t` form the `K_2` component of `J`.  Since the
singleton is full to `Q`,

```text
Q=N_G(u_t)={x,y,t} union P_{u_t}.
```

The vertex `p in A intersect Q` therefore belongs to `P_{u_t}`.  The high
component `D` is full to the cut vertex `t`.  Outside `Q`, the neighbours
of `t` are `u_t` and possibly `q_t`; the former lies in `L`.  Hence
`q_t in D`, proving that `q_t` is not in `Q`.  Inside `Q`, the fixed edges
are `xt,yt,tp`; the only other possible edge is the edge between the two
members of `P_{u_t}`.  This proves (4).

Suppose next that `L={q_t}`.  Fullness and singleton order give
`Q=N_G(q_t)`.  Since `q_t in A` is nonadjacent to `x,y`, neither belongs
to `Q`.  Among the cut vertices, `t` can therefore be adjacent only to
`p` and possibly `u_t`, which proves (5).

Finally suppose `|L|=2`.  Connectivity makes `L` an edge.  Each endpoint
has at least four neighbours in `Q`, because it has degree at least five
and its only neighbour outside `Q` is the other endpoint.  Fullness of
`L` to `Q` prevents the two endpoints from missing the same cut vertex.
This gives the three incidence patterns in (6), and direct counting gives

```text
delta_Q(L)=1+f-8=f-7.
```

There are `|A|+2` vertices outside `Q`; hence `|L|=2` gives `|D|=|A|`.
The component `D` is another minimum-order high-excess component behind a
five-cut.  The minimum-lobe reduction therefore gives
`|E(G[Q])|<=6`, proving (7).  \(\square\)

## Theorem 4 (the uncontracted singleton orientation)

Suppose `L={q_t}`.  Abbreviate `q=q_t`, put

```text
R=S intersect Q,              B=A intersect Q,
s=|R|,                        k=|E(G[Q])|,
X=A intersect D.
```

Then

```text
Q=N_G(q),                     1<=s<=4,
|B|=5-s,                      |D|=|A|+1,
delta_Q(D)=12-k,                                      (8)
X=A-(B union {q}),            |X|=|A|+s-6<|A|.       (9)
```

For an arbitrary vertex set `U`, define its incident-edge excess by

```text
epsilon(U)=|E(G[U])|+|E_G(U,V(G)-U)|-4|U|.
```

The strict intersection `X` satisfies the exact identity

```text
epsilon(X)=27-k-4s+|E(J[R])|-|E_G(B,S-Q)|.            (10)
```

Its natural boundary obeys only

```text
N_G(X) subseteq S union B,              |S union B|=10-s.  (11)
```

### Proof

Theorem 3 gives `Q=N_G(q)` and excludes `x,y` from `Q`.  Hence `D`
contains `x,y`, while the singleton low side has excess one.  The cut
identity

```text
delta_Q(D)+1=13-k
```

gives (8).  The remaining order statements follow from `|Q|=5`,
`q in A-Q`, and the fact that `p in B`, so `s<=4`.

For two vertex sets `U,W`, direct edge counting gives

```text
epsilon(U intersect W)+epsilon(U union W)
 =epsilon(U)+epsilon(W)-|E_G(U-W,W-U)|.                (12)
```

Apply (12) to `U=A` and `W=D`.  Exact accounting at the original cut
gives `epsilon(A)=8`, while (8) gives `epsilon(D)=12-k`.  The complement
of `A union D` is `R`, so the equality `|E(G)|=4|V(G)|-7` gives

```text
epsilon(A union D)=4s-7-|E(J[R])|.                    (13)
```

Finally,

```text
A-D=B union {q},                  D-A={x,y} union (S-Q).
```

The vertex `q` has no neighbour outside `Q`, and no vertex of `A` is
adjacent to `x,y`.  Thus the cross term in (12) is exactly
`|E_G(B,S-Q)|`.  Substitution gives (10).  Every neighbour of
`X=A intersect D` outside `X` belongs to `S union Q`; the vertex `q` has
no neighbour in `X`, leaving only `S union B`.  This proves (11).
\(\square\)

When `s=4`, the set `B` is `{p}`, and (10) simplifies to

```text
epsilon(X)=11-d_S(p)>=6,                 N_G(X) subseteq S union {p}.  (14)
```

Moreover `p` has a neighbour in `X`: otherwise the connected graph `A`
would split into the nonempty set `X` and the adjacent pair `{p,q}`, since
`q` has no neighbour in `X`.  The subsequent
[singleton-neighbour boundary-collapse theorem](hc7_k7minus_e5_singleton_neighbour_boundary_collapse.md)
closes this row.  It deletes the five-set

```text
(S-{t}) union {p}
```

and finds the connected component `{x,y,t,q}` with excess one.  The
universal five-cut excess lemma then puts excess at least four in a strict
component of `X`, contradicting the choice of `A`.

Consequently every surviving `q_t`-singleton orientation has `1<=s<=3`.
Since `t` has no neighbour in `X`, equation (11) sharpens in these rows to

```text
N_G(X) subseteq (S-{t}) union B,        |(S-{t}) union B|=9-s,
```

whose boundary orders are six, seven or eight.

For these remaining orientations, the companion cut through `tq` does not
presently remove the obstruction.
If its low component is the singleton `{p}`, then `p,q` are adjacent
degree-five vertices.  They have at most three common neighbours: four
common neighbours would form a four-cut isolating the edge `pq`.  Thus
`pq` is itself density-safe to contract and supplies a third exact
five-cut, but no current uncrossing theorem collapses the boundary in
(11) to five vertices while preserving the excess in (10).

## Theorem 5 (the uncontracted two-vertex orientation)

Suppose `L={r_1,r_2}` has order two.  Then

```text
L intersect {x,y} is empty,
L intersect {u_t,q_t} is nonempty.                    (15)
```

Let `z in Q`, and contract the connected set `L union {z}` to `z`,
deleting no vertex of `D union Q`.  Write

```text
mu_Q(z)=4-d_{G[Q]}(z)
```

for the number of nonneighbours of `z` in `Q`.  The resulting proper
minor `M_z` has

```text
|E(M_z)|>=4|V(M_z)|-7
```

whenever

```text
mu_Q(z)>=delta_Q(L).                                  (16)
```

### Proof

Suppose, by symmetry, that `x in L`.  Its mate lies in `S`, because `x`
has no neighbours in `A` and `xy` is absent.  The vertex `x` has at least
four neighbours in `Q`, while `p in Q intersect A` is not one of them.
Therefore the other four members of `Q` are roots.  The mate of `x` is
the fifth root outside `Q`.  The vertex `y` also lies outside `Q` and is
adjacent to that mate, joining `L` to the other component of `G-Q`, a
contradiction.  This proves the first part of (15).

The low component is full to the cut vertex `t`, so it contains a
neighbour of `t` outside `Q`.  The only possibilities after excluding
`x,y` are `u_t,q_t`, proving the second part.

Contracting `L` into `z` makes `z` adjacent to every other member of `Q`,
because `L` is full to `Q`.  It therefore adds all `mu_Q(z)` missing
star edges at `z`.  The minor has vertex set `D union Q`, and

```text
|E(M_z)|
 >=4|D|+delta_Q(D)+|E(G[Q])|+mu_Q(z)
 =4|D|+13-delta_Q(L)+mu_Q(z).
```

Since `|V(M_z)|=|D|+5`, condition (16) is exactly the displayed `E5`
density threshold.  \(\square\)

The unproved step is five-connectivity of `M_z`.  A cut of order at most
four may contain `z`; after deleting it, the remaining graph on `Q-{z}`
need not be connected.  Lifting that cut shows that every returned
component meets surviving roots, but does not isolate a strict smaller
component of `D` with excess at least four.

## Exact nonclosure and smallest repair

The classification refutes the following proposed mechanism, not the
anchored four-root target itself:

> target-freeness of the contracted seven- or eight-vertex quotient
> restricts the cut graph enough to align the selected leaf pair or force
> strict high-excess descent.

There is no eight-vertex quotient, and target-freeness of the
seven-vertex quotient follows already from excess accounting.  Contracting
`D` has erased precisely the information still needed: the traces of the
four old roots and a compatible rooted model inside the high side.

A smallest useful repair must retain that information.  One precise form
is the following.

> For some selected edge `tp`, the high component `D` contains a
> trace-compatible four-root `K_4`-minor model together with a disjoint
> `p`-anchored connected subgraph adjacent to all four bags, or the old
> shore `A` and `D` uncross to a component of order below `|A|` and excess
> at least four.

The two nontrivial orientations left by Theorem 3 are the
`q_t`-singleton cut `Q=N_G(q_t)` with at most three roots, which excludes
`x,y` and crosses the original cut, and the two-vertex low edge with its
explicit two-by-five incidence pattern.  The sparse `u_t`-singleton row
still requires the same trace-compatible rooted model; its quotient
supplies no such model.

More specifically, the two smallest missing statements are:

1. a **multi-neighbour boundary-reduction lemma** for `s<=3` which turns
   one component of the strict set `X` in Theorem 4, currently behind at
   most `9-s` vertices, into an order-five shore of excess at least four,
   unless an anchored four-root model already exists; and
2. a **near-universal edge-completion lemma** which says that a minor
   `M_z` satisfying (16) is five-connected, or that its first cut of
   order at most four lifts to a strict smaller high-excess component in
   `D`.

The first remains the sharper route.  At `s=3` the strict smaller set is
already behind only six possible boundary vertices; unlike the closed
`s=4` row, however, the second member of `B` survives outside every
five-set obtained by dropping one of them and may join the low exterior to
`X`.  Controlling that extra dense-side boundary vertex is the first exact
unsupported inference.

## Dependencies

- The [singleton-contraction uncrossing theorem](hc7_k7minus_e5_singleton_contraction_uncrossing.md),
  especially Theorems 6 and 7.
- The [singleton-neighbour boundary-collapse theorem](hc7_k7minus_e5_singleton_neighbour_boundary_collapse.md),
  which closes the `s=4` orientation described after Theorem 4.
- The minimum high-excess lobe reduction in the
  [auxiliary `E5` frontier](hc7_k7minus_e5_frontier.md).
