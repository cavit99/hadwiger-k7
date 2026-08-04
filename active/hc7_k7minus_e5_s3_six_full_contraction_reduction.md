# Contractions from a six-full component

**Status:** active computation-free written reduction; separately audited in
the [adjacent audit](hc7_k7minus_e5_s3_six_full_contraction_reduction_audit.md).
This note does not prove `(E5)`.

Write `K_7^-` for `K_7` with one edge deleted.  Use the endpoint of the
[high triangle-misser elimination](hc7_k7minus_e5_s3_high_misser_elimination.md).
Thus `G` is a minimum `E5` enemy in the exact `s=3` singleton-triangle
row,

```text
|E(G)|=4|V(G)|-7,                   kappa(G)=5,
Delta={p,t,q},                      L=Delta union R,
|R|=3.
```

Put `a=|A|`.  The original two-singleton five-cut has vertex partition
`A,S,{x},{y}`, so

```text
|V(G)|=a+7.
```

For any five-cut `Q` and component `X` of `G-Q`, put

```text
delta_Q(X)=|E(G[X])|+|E_G(X,Q)|-4|X|,
Phi(Q,X)=delta_Q(X)+|E(G[Q])|,
rho(Q,X)=number of components of G-Q other than X.
```

The global choice inherited from the high-misser theorem first minimises
`|A|`, then maximises `Phi(S,A)`, and then minimises `rho(S,A)`.  For the
selected two-singleton cut,

```text
Phi(S,A)=11,                         rho(S,A)=2.
```

The graph `G-L` has at least two components.  Every one is adjacent to
all three members of `R` and to at least two members of `Delta`.  No
high component misses a triangle vertex; every triangle-missing component
has order at most two.  Consequently some component is adjacent to every
vertex of `L`; call such a component **six-full**.

For a component `C` of `G-L`, write

```text
tau(C)=number of vertices of Delta adjacent to C.
```

Then `tau(C)` is two or three, and `C` is six-full precisely when
`tau(C)=3`.

## 1. Four complementary components are impossible

For `u in Delta`, let `c_u` be the number of components of `G-L` adjacent
to `u`, and put

```text
P_u=N_G(u)-Delta,                   |P_u|=3.
```

The exact contact-capacity inequality from the triangle-cut refinement is

\[
 c_u+|R\cap P_u|\le3.                                \tag{1}
\]

Summing it over the triangle gives

\[
 \sum_{C\in\mathcal C(G-L)}\tau(C)
   =c_p+c_t+c_q
   \le9-|E_G(\Delta,R)|.                             \tag{2}
\]

### Lemma 1

The graph `G-L` has at most three components.

### Proof

The triangle-cut refinement already bounds the number of components by
four.  Suppose that there were four.  Each has at least two triangle
contacts, and at least one is six-full.  Hence the left side of (2) is at
least

```text
3+2+2+2=9.
```

Equality must hold throughout (2).  In particular,

```text
E_G(Delta,R) is empty,              c_t=3.             (3)
```

The exact exterior neighbourhood of the selected leaf `t` is

```text
P_t={x,y,u_t}.
```

By (3), none of these vertices lies in `R`.  Equality `c_t=3` in (1)
therefore requires `x,y,u_t` to lie in three distinct components of
`G-L`.

On the other hand, at least one vertex

```text
s in S-({t} union R)
```

survives: `S-{t}` has four vertices and `R` has order three.  The original
singleton neighbourhoods satisfy `N_G(x)=N_G(y)=S`, so

```text
x-s-y
```

is a path in `G-L`.  Thus `x` and `y` lie in the same component, contrary
to the equality conclusion above.  \(\square\)

The same calculation records the remaining contact capacity exactly.
Let `m` be the number of components of `G-L`, let `f` be the number of
six-full components, and put `h=|E_G(Delta,R)|`.  Then

\[
                  2m+f+h\le9.                         \tag{4}
\]

Indeed, every non-six-full component has two triangle contacts and every
six-full component has three.  Here `m` is two or three and `f>=1`; in
particular,

```text
m=3 implies f+h<=3,
m=2 implies f+h<=5.                                  (5)
```

For later density accounting, if

```text
eta_L(C)=|E(G[C])|+|E_G(C,L)|-4|C|,
```

then the exact six-cut identity is

\[
 \sum_{C\in\mathcal C(G-L)}\eta_L(C)
   =17-|E(G[L])|
   =14-h-|E(G[R])|.                                  \tag{6}
\]

Equations (4)--(6) do not by themselves localise excess in a proper
subcomponent.

## 2. Every cross-edge has safe contraction density

### Lemma 2 (three common neighbours)

Let `C` be a six-full component of `G-L`, let `D` be another component,
and let `u in Delta` be adjacent to `D`.  For every

```text
v in V(C) intersect N_G(u),
```

one has

\[
                         |N_G(u)\cap N_G(v)|\le3.      \tag{7}
\]

### Proof

The triangle vertex `u` has degree five: its two neighbours in `Delta`
and the three vertices of `P_u`.  Choose

```text
w in V(D) intersect N_G(u).
```

The vertices `v,w` lie in distinct components of `G-L`, so they are
nonadjacent.  Among the five neighbours of `u`, the vertex `v` itself is
not a common neighbour of `u,v`, and neither is `w`.  At most the other
three neighbours of `u` can be common neighbours.  This proves (7).
\(\square\)

### Theorem 3 (safe contraction and exact returned cut)

Under the hypotheses of Lemma 2, contract the edge `uv` to a vertex `z`
and call the resulting simple graph `H=G/uv`.  Then

1. `|E(H)|>=4|V(H)|-7`;
2. `H` is four-connected but not five-connected;
3. every four-cut of `H` contains `z`; and
4. every such four-cut lifts, by replacing `z` with `{u,v}`, to an exact
   five-cut of `G` containing `u,v`.

### Proof

Contracting `uv` loses exactly

\[
                  1+|N_G(u)\cap N_G(v)|\le4
\]

edges.  Since the order falls by one,

\[
 |E(H)|\ge4|V(G)|-11=4|V(H)|-7,                      \tag{8}
\]

proving the first assertion.  The graph `H` is a proper target-free minor
of `G`.

We next show that `H` is four-connected.  A cut of order at most three
which avoids `z` would lift unchanged to a cut of `G`: contracting the
connected edge `uv` cannot disconnect a graph which was connected.  A cut
of order at most three containing `z` would lift after replacing `z` by
`u,v`, giving a cut of `G` of order at most four.  Both alternatives
contradict five-connectivity of `G`.

If `H` were five-connected, (8) would make it a smaller `E5` enemy,
contrary to the minimum choice of `G`.  Thus `H` is not five-connected.
Its connectivity is therefore exactly four.

Let `X` be a four-cut of `H`.  If `z` were not in `X`, the same lifting
argument would make `X` a four-cut of `G`.  Hence `z in X`.  The set

\[
                    (X-\{z\})\cup\{u,v\}              \tag{9}
\]

has order five, and deleting it from `G` gives exactly the disconnected
graph obtained by deleting `X` from `H`.  It is therefore a five-cut of
`G`; five-connectivity makes its order exact.  This proves the final two
assertions.  \(\square\)

In particular, every other component `D` supplies such contractions for
each triangle vertex it meets and every neighbour of that vertex in a
chosen six-full component.  The returned five-cuts all contain one named
triangle vertex and one named vertex of the six-full component.

## 3. Companion cuts and the returned-cut classification

### Corollary 4

The following additional conclusions hold.

1. If a component `D` of `G-L` is not six-full, then it misses a unique
   vertex `w` of `Delta`, has order at most two, and

   ```text
   L_w=L-{w}
   ```

   is an exact five-cut of `G` with `D` as a component of `G-L_w`.
2. If `G-L` has three components, at least one of them is not six-full.
3. Every returned cut `Q_{u,v}` from Theorem 3 has two or three
   boundary-full complementary components, and
   `|E(G[Q_{u,v}])|<=8`.
4. If `G-Q_{u,v}` has three components and

   ```text
   k=|E(G[Q_{u,v}])|,
   ```

   then `G[Q_{u,v}]` is triangle-free and `k>=1`.  If `k=1`, the two low
   excesses are at most two and the high excess is at least eight.  If
   `k>=2`, the two low excesses are at most one and the high excess is at
   least `11-k`.

### Proof

Every component has two or three triangle contacts.  Thus a component
which is not six-full misses a unique `w in Delta`.  The triangle-misser
dichotomy and the subsequent high-misser elimination make its order at
most two.  All its neighbours outside the component lie in `L_w`, so
deleting `L_w` separates it from the rest of the graph.  The six-full
component has a neighbour of `w`, and hence the opposite side is nonempty.
Thus `L_w` is a cut of order five and `D` is one of its components.

Suppose that `G-L` had three components and all three were six-full.  Then
the triangle-contact sum in (2) would be nine.  Equality would hold in
(2), so `E_G(Delta,R)` would be empty and `c_t=3`.  Exactly as in the
proof of Lemma 1, the three vertices `x,y,u_t` would then lie in distinct
components of `G-L`, whereas a surviving vertex of
`S-({t} union R)` gives the path `x-s-y` in `G-L`.  This is impossible.

The remaining conclusions are the existing exact five-cut theorems
applied to `Q_{u,v}`.  Every five-cut in a minimum `E5` enemy has two or
three boundary-full components, and its boundary has at most eight edges.
In the three-component case the boundary is triangle-free.  The edge
`uv` lies in `G[Q_{u,v}]`, so `k>=1`; the exact three-component
concentration theorem then gives the asserted excess bounds.  \(\square\)

Thus every three-component lifted six-cut comes with a small-side
five-cut `L_w`, and the same is true in the two-component case unless both
components are six-full.  Moreover, any returned cut with three
components has a uniquely concentrated high-excess side.

### Proposition 5 (returned-cut order normal form)

Let `B` be a component of excess at least four behind a returned cut
`Q_{u,v}`.  Then

```text
|B|=a+1,
```

and `G-Q_{u,v}` has exactly one other component, a singleton `{d}` with

```text
N_G(d)=Q_{u,v},                    delta_Q_{u,v}({d})=1.
```

Consequently every returned cut satisfies

```text
Phi(Q_{u,v},B)=12,                 rho(Q_{u,v},B)=1.
```

### Proof

The global choice of `A` gives `|B|>=a`.  Since `Q_{u,v}` has order five
and `|V(G)|=a+7`, only `a+2` vertices lie outside the cut.  As the cut has
at least two components,

```text
|B| is a or a+1.                                     (10)
```

Suppose first that `|B|=a`.  The other two vertices form either two
singleton components or one edge component `K`.

In the edge case, write `K={alpha,beta}`.  The complement-excess identity
gives

```text
Phi(Q_{u,v},B)=13-delta_Q_{u,v}(K).
```

The component `K` is boundary-full, and hence

```text
delta_Q_{u,v}(K)=1+|E_G(K,Q_{u,v})|-8<=3.
```

If this excess is at most one, `Phi` is larger than the selected value
eleven.  If it is two, `Phi` is eleven and the number of opposite
components is one rather than two.  The global selection excludes both
possibilities.  Thus its excess is three, so both `alpha` and `beta` are
complete to `Q_{u,v}`.

Choose `w in D intersect N_G(u)` as in Lemma 2.  The six nominal
neighbours

```text
v, w, alpha, beta, and the two vertices of Delta-{u}
```

are distinct except that `alpha` or `beta` may be a triangle mate of `u`.
Indeed, `w` cannot be a low vertex: it lies in the original component
`D`, which is anticomplete to `v in C`, whereas both low vertices see
`v in Q_{u,v}`.  Since `d_G(u)=5`, at least one low vertex is a triangle
mate.  That vertex is adjacent to all five vertices of `Q_{u,v}` and also
to the other end of `K`, contrary to its degree five.  The edge case is
impossible.

It remains that the two other components are singletons `{alpha}` and
`{beta}`.  Boundary fullness gives

```text
N_G(alpha)=N_G(beta)=Q_{u,v}.
```

The same degree-five count shows that at least one singleton is a triangle
mate.  They cannot both be triangle mates, because the two mates are
adjacent whereas distinct components of `G-Q_{u,v}` are anticomplete.
Let `r` be the unique triangle-mate singleton.  If `r` is `p` or `q`,
then `N_G(r)=Q_{u,v}` contradicts the already proved fact that deleting
`N_G(r)` leaves `{r}` and one connected exterior: the other singleton
and `B` are distinct exterior components.  Hence `r=t`.

Let `d` be the other singleton.  Then

```text
N_G(d)=Q_{u,v}=N_G(t)={p,q,x,y,u_t}.                  (11)
```

Put

```text
R'=Q_{u,v}-{p,q},                   L'=Delta union R'.
```

Then `L'=Q_{u,v} union {t}` is another lifted triangle cut, and `G-L'`
has exactly the components `B` and `{d}`.  The component `B` has order
`a`, has excess at least four, and misses `t`; the vertices `t,d` are
nonadjacent because they were distinct components of `G-Q_{u,v}`.
The nonadjacent case of the triangle-misser classification therefore
reapplies the proved two-singleton boundary classification and gives

```text
d in S,                            G[Q_{u,v}]=(x-u_t-y) disjoint union (p-q),
delta_Q_{u,v}(B)=8.
```

This is exactly the nonadjacent `t`-misser reorientation eliminated by
the central five-cut in Lemma 6 of the high-misser theorem.  That lemma
produces a component of excess at least four and order below `a`, a
contradiction.

Therefore `|B|=a` is impossible.  By (10), `|B|=a+1`; the sole remaining
vertex outside the cut is a singleton `{d}`.  Boundary fullness gives
`N_G(d)=Q_{u,v}` and excess one.  The complement-excess identity now gives
`Phi(Q_{u,v},B)=13-1=12`, while there is one opposite component.  \(\square\)

The larger order in Proposition 5 is essential: although its `Phi` value
is better than eleven, the global selection minimises component order
before comparing `Phi`.

## 4. Exact remaining uncrossing obligation

For a choice `(C,D,u,v)` as in Theorem 3, fix a four-cut

```text
{z} union T_{u,v},                  |T_{u,v}|=3,
```

of `G/uv`.  Its lift is

```text
Q_{u,v}={u,v} union T_{u,v}.                         (12)
```

Proposition 5 says that `G-Q_{u,v}` consists exactly of a singleton and a
connected high-excess component of order `a+1`.  What is not proved is
that some permitted choice of `(C,D,u,v)` and quotient four-cut avoids
this larger connected-exterior form.  The cut may use vertices of `C`,
and its high side may contain vertices of `L` or several components of
`G-L`.

The remaining statement required from this contraction family is
therefore the following precise repair:

> For at least one permitted edge `uv`, some four-cut of `G/uv` lifts to
> a five-cut whose high-excess component has order `a`, not `a+1`.

Proposition 5 would then give an immediate contradiction.  Equivalently,
one may eliminate the order-`a+1` singleton connected-exterior form
directly or force from it a second density-safe contraction whose returned
high side has order `a`.

When a non-six-full component `D` is present, the most structured route
is to uncross the three exact cuts

```text
L,                                  L_w=L-{w},
Q_{u,v}={u,v} union T_{u,v},
```

using the order-at-most-two side `D` of `L_w` and the singleton side of
`Q_{u,v}`.  It must prove at least one of the following:

1. the cuts give an explicit `K_7^-` minor in `G`; or
2. one returned five-cut has a high component of order `a`, and hence is
   excluded by Proposition 5; or
3. another five-cut has a high component which is strictly better than
   the selected pair in the lexicographic order

   ```text
   minimum order, maximum Phi, minimum rho.
   ```

If `G-L` has exactly two six-full components, no cut `L_w` is available;
that branch instead requires a density-sensitive labelled split between
the two full components.  An arbitrary component properly contained in
`C` without a proved high-excess bound, an unrooted near-clique model in
`G/uv`, or the existence of the cuts (12) alone proves neither outcome.
Eliminating the order-`a+1` singleton exterior, together with the
two-six-full branch, is the first unsupported inference after
Proposition 5.

## Dependencies and scope

- The
  [singleton-triangle contraction](hc7_k7minus_e5_s3_triangle_contraction_reduction.md)
  supplies the exact triangle degrees and the lifted order-six cut.
- The
  [triangle-cut refinement](hc7_k7minus_e5_s3_triangle_cut_refinement.md)
  supplies the two-contact lemma and the component-capacity inequality.
- The audited
  [high triangle-misser elimination](hc7_k7minus_e5_s3_high_misser_elimination.md)
  excludes the high missing components and supplies a six-full component.
- The minimum-enemy facts and the universal high-excess component behind
  every five-cut are in the
  [singleton-contraction uncrossing](hc7_k7minus_e5_singleton_contraction_uncrossing.md).
- The
  [dense five-cut eliminations](hc7_k7minus_e5_k5minus_cut_elimination.md)
  give the boundary size bound, eliminate five components in Theorem 6,
  and give the triangle-free three-component boundary in Theorem 7.
- The
  [four-component elimination](hc7_k7minus_e5_independent_four_component_elimination.md)
  completes the two-or-three-component classification.
- The
  [three-component concentration theorem](hc7_k7minus_e5_three_component_concentration.md)
  gives the excess bounds for a returned cut with three components.

This note reduces the post-high-misser endpoint to overlapping exact
five-cuts obtained from density-safe contractions.  Outside the
two-six-full branch, the cuts include a small-side companion `L_w`.  It
proves no strict descent, no labelled `K_7^-` model, and neither `(E5)` nor
the primary seven-connected theorem.
