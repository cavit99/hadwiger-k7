# Internal audit: contractions from a six-full component

**Verdict:** GREEN for the pinned source revision.  This is a separate
internal mathematical audit, not external peer review.

**Audited source:**
`active/hc7_k7minus_e5_s3_six_full_contraction_reduction.md`

**SHA-256:**
`4ab5afe3d8e8cee4f41577ec5e571b033a792a61babfe5e8e795d0961904b991`

No mathematical correction is required at this revision.

Relative to the previously audited source revision
`a3ec3ad117148614879b096557b5696475016b69b50fd48b36bdf052df96c507`,
the source now adds the small companion cuts, the exact classification of
returned five-cuts, and Proposition 5.  Those additions are material and
are checked in Sections 7 and 8 below.

## 1. Imported setup

The imported singleton-triangle reductions provide an order-six cut

```text
L=Delta union R,          Delta={p,t,q},          |R|=3,
```

with at least two complementary components.  Each component is adjacent
to all of `R` and to two or three vertices of `Delta`.  The three triangle
vertices have degree five and exact exterior neighbourhoods

```text
P_u=N_G(u)-Delta,                    |P_u|=3.
```

The high-misser endpoint excludes a high component with only two triangle
contacts and guarantees at least one component with three contacts.  The
audited note uses no stronger conclusion from that dependency.

## 2. Excluding four complementary components

For `u in Delta`, each component counted by `c_u` requires a distinct
neighbour of `u` outside `L`, while every member of `R intersect P_u`
uses another member of the same three-set.  Hence

```text
c_u+|R intersect P_u|<=3.
```

Summing is legitimate because

```text
sum_u |R intersect P_u|=|E_G(Delta,R)|=h
```

and `sum_u c_u` counts the triangle contacts of all complementary
components.

Suppose there were four components.  At least one has three triangle
contacts and every other one has at least two, so the contact sum is at
least nine.  The summed capacity bound is at most `9-h`.  Equality is
therefore forced everywhere: `h=0`, the contact sum is nine, and each of
`c_p,c_t,c_q` equals three.  In particular, no member of

```text
P_t={x,y,u_t}
```

lies in `R`, and the equality `c_t=3` requires these three vertices to lie
in three distinct components of `G-L`.

This is incompatible with the original five-set `S`.  The vertices `p,q`
belong to the dense side in the imported singleton-triangle setup, while
`t in S`.  Since `|S-{t}|=4` and `|R|=3`, some

```text
s in S-({t} union R)
```

survives outside `L`.  The vertices `x,y` also survive, and their exact
neighbourhoods `N_G(x)=N_G(y)=S` give the path `x-s-y` in `G-L`.
Thus `x,y` lie in the same component, contradicting the forced distinct
placements.  Lemma 1 is correct.

## 3. Capacity and excess identities

If `m` is the component count and `f` is the number of components with
three triangle contacts, then the contact sum is exactly

```text
3f+2(m-f)=2m+f.
```

Combining this with the preceding capacity inequality gives

```text
2m+f+h<=9.
```

With `m in {2,3}` and `f>=1`, the two displayed consequences in equation
(5) follow directly.

There are no edges between distinct components of `G-L`.  Grouping all
edges outside `G[L]` by component therefore gives

```text
sum_C eta_L(C)
  =|E(G)|-|E(G[L])|-4(|V(G)|-6)
  =17-|E(G[L])|.
```

Since `Delta` induces a triangle,

```text
|E(G[L])|=3+h+|E(G[R])|,
```

which gives the second equality `14-h-|E(G[R])|`.  Thus all constants and
directions in equations (4)--(6) are correct.

## 4. Common-neighbour bound

Fix a six-full component `C`, another component `D`, and a triangle vertex
`u` met by `D`.  Choose neighbours `v in C` and `w in D` of `u`.  They are
distinct and nonadjacent because they lie in different components of
`G-L`.

The set `N_G(u)` has exactly five vertices.  The vertex `v` is not a
common neighbour of `u,v` in a simple graph, and `w` is not a common
neighbour because `vw` is absent.  Only the other three members of
`N_G(u)` remain available.  Hence

```text
|N_G(u) intersect N_G(v)|<=3.
```

No possible common neighbour has been omitted from this count, and the
argument does not assume that `v` is the only neighbour of `u` in `C`.

## 5. Density, connectivity and minimality after contraction

Contracting `uv` in a simple graph loses its edge and one duplicate
incidence for every common neighbour.  The loss is therefore at most
four.  Since the order falls by one and `|E(G)|=4|V(G)|-7`, the quotient
`H=G/uv` satisfies

```text
|E(H)|>=4|V(H)|-7.
```

It is a proper target-free minor of `G`.

The quotient is four-connected.  A cut of order at most three avoiding
the contracted vertex `z` would also disconnect `G`; the edge `uv` lies
within one component before contraction.  A cut of order at most three
containing `z` becomes, after replacing `z` by `u,v`, a cut of `G` of
order at most four.  Both cases contradict five-connectivity.

If `H` were five-connected, its density and target-freeness would make it
a smaller `E5` enemy.  Minimum order of `G` excludes this.  Thus
`kappa(H)=4`, so four-cuts exist.

## 6. Exact lift

Every four-cut `X` of `H` contains `z`; otherwise it lifts unchanged to a
four-cut of `G`.  For `z in X`, deleting

```text
(X-{z}) union {u,v}
```

from `G` leaves exactly the same graph as deleting `X` from `H`.  The set
has order `4-1+2=5`, is a vertex cut, and contains both named vertices
`u,v`.  This verifies every assertion in Theorem 3, including the exact
order of the lifted cut.  The revised source then uses the full
minimum-enemy five-cut package rather than stopping at existence of the
cut.

## 7. Companion cuts and concentration

A non-six-full component `D` has exactly two triangle contacts and misses
a unique `w in Delta`.  The triangle-misser dichotomy makes such a
component either low or an order-`a` high misser, and the latter case has
already been eliminated.  Hence `|D|<=2`.  Every external neighbour of
`D` lies in `L-{w}`.  Deleting that five-set therefore separates `D`,
while the surviving vertex `w` has a neighbour in a six-full component.
Thus `L-{w}` is an exact five-cut with the asserted nonempty sides.

If three components of `G-L` were all six-full, their triangle-contact
sum would be nine.  Equality in the capacity inequality forces
`E_G(Delta,R)` empty and `c_t=3`.  The three members of
`P_t={x,y,u_t}` would lie in different components.  As in Lemma 1, a
vertex of `S-({t} union R)` survives and gives the path `x-s-y`, a
contradiction.  Corollary 4(1)--(2) is correct.

For a returned five-cut, the existing minimum-enemy results give two or
three boundary-full components and at most eight boundary edges.  In the
three-component case the boundary is triangle-free.  Since the literal
edge `uv` lies in the boundary, its size `k` is at least one.  The exact
concentration theorem gives precisely

```text
k=1:   low excesses <=2,   high excess >=8;
k>=2:  low excesses <=1,   high excess >=11-k.
```

These are the bounds stated in the pinned source.  In particular, because
a triangle-free five-vertex boundary has at most six edges, the designated
high side has excess at least five and is distinct from the two low sides.

## 8. Returned-cut order normal form

The original vertex partition has order `a+7`.  A high component `B`
behind a returned five-cut has order at least `a` by the first coordinate
of the global selection.  Only `a+2` vertices lie outside the cut, so
`|B|` is `a` or `a+1`.

Assume `|B|=a`.  If the other two vertices form an edge `K`, then

```text
Phi(Q,B)=13-delta_Q(K),             delta_Q(K)<=3.
```

Values at most one improve `Phi`; value two ties `Phi=11` and improves
`rho` from two to one.  Thus only excess three survives, forcing both ends
of `K` to be complete to `Q`.

Let `u` be the named degree-five triangle vertex, `v` its neighbour in
the six-full component, and `w` its neighbour in the comparison component.
The vertices `v,w`, the two low vertices and the two triangle mates are
six nominal neighbours of `u`.  The only possible identifications are
between a low vertex and a triangle mate: a low vertex sees `v`, whereas
`w` lies in a component anticomplete to `v`.  Hence one low vertex is a
triangle mate.  In the edge case it sees all five vertices of `Q` and its
low-edge mate, contradicting degree five.

If instead the two low vertices are singleton components, both have
neighbourhood exactly `Q`.  The same count forces exactly one of them to
be a triangle mate.  It cannot be `p` or `q`, because their exact
singleton cuts have connected exteriors.  It is therefore `t`, and the
other singleton `d` satisfies

```text
N_G(d)=Q=N_G(t)={p,q,x,y,u_t}.
```

Put `R'=Q-{p,q}` and `L'=Delta union R'`.  The set `L'` is a lifted
triangle cut, `G-L'` has components `B,{d}`, and `B` is an order-`a`
high component missing `t`; moreover `td` is absent.  The audited
triangle-misser classification now applies and, crucially, supplies the
previously nonautomatic boundary conclusion

```text
G[Q]=(x-u_t-y) disjoint union (p-q),  delta_Q(B)=8.
```

This is exactly the nonadjacent-`t` normal form eliminated by the central
five-cut of the high-misser theorem.  Thus `|B|=a` is impossible.

It follows that `|B|=a+1`, leaving one singleton component.  Fullness
gives its neighbourhood equal to `Q` and its excess equal to one, so the
complement-excess identity gives `Phi(Q,B)=12` and `rho(Q,B)=1`.
Proposition 5 is correct.

The source also states the exact residual limitation.  Order is the first
selection coordinate, so the improved value `Phi=12` does not exclude an
order-`a+1` high side.  No argument yet eliminates this singleton
connected-exterior form for one permitted contraction, and the
two-six-full case has no companion cut `L-{w}`.  Neither `(E5)` nor the
primary theorem follows.

## 9. Dependency revisions and audit boundary

The source revisions checked were:

```text
singleton-triangle contraction:
52e321c3c46a267663de3584d1a628f8a3c9044369071328f619df704129d242

triangle-cut refinement:
870e6d41c3d0f0e0e69c2a410ff6543bb2127ead3fd6cc371a1a1f148a123495

high triangle-misser elimination:
6c881f87026f3116fa01749a1dc665dd93642a482a90ba37d404b83e2976db8e

high triangle-misser elimination audit:
fcbedc7f3648794ec2e812106eef3dc2d3459e336409dd744b9342c219f37318

singleton-contraction uncrossing:
e4720b2641033396aabf333cc97d9f401df4577f8a6f337a44d7ca6aba0ac1c2

dense five-cut eliminations:
81306114489449f1bd2d8521c4aefc216411f81bf6721c7763412d4a7a87c6c0

dense five-cut eliminations audit:
924d89d2a7c7645b9834a125d5851a342640a5c8aeb68f0c6acc667d435af1b2

independent four-component elimination:
ed72324ab14b310522ac579b4207f1a0c3391b9061d9c1de09cf40b6ec0cfa5d

independent four-component elimination audit:
6f631b56c92ac9366190b060dd7b8142df83307bf8c7f54c0d5708d53dff4637

three-component concentration:
40391662ea90f75e36732776b67c9cac22c6ecaee1e056e0498b45d034620580

three-component concentration audit:
321cdd4193b52f034d925173319c27c934942bd3e821ea42ba3834bd681adb6b
```

The imported high triangle-misser elimination and the three additional
five-cut results are separately audited GREEN at the source and audit
hashes displayed above.  The present audit has checked that each endpoint
is imported with the correct scope.  The six-full contraction reduction
is therefore GREEN with no unresolved internal inference or unaudited live
dependency used in its proof.
