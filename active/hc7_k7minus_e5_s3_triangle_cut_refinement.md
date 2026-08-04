# Refining the lifted triangle cut

**Status:** active computation-free written reduction; separately audited in
the [adjacent audit](hc7_k7minus_e5_s3_triangle_cut_refinement_audit.md).
This note does not prove `(E5)`.

Use the notation and conclusions of the audited
[singleton-triangle contraction](hc7_k7minus_e5_s3_triangle_contraction_reduction.md).
Thus `G` is a minimum `E5` enemy in the exact `s=3` singleton row,
`a=|A|>=8`, and

```text
Delta={p,t,q}
```

is a triangle.  Contracting `Delta` to `z` gives a four-connected graph
`J`.  Fix a four-cut

```text
{z} union R,                         |R|=3,
```

of `J`, and put

```text
L=Delta union R.
```

The preceding theorem shows that `L` is an order-six cut of `G`.  Every
component of `G-L` is adjacent to every member of `R` and has a neighbour
in `Delta`.  There are exactly `a+1` vertices outside `L`.

For a component `C` of `G-L`, put

```text
eta_L(C)=|E(G[C])|+|E_G(C,L)|-4|C|.
```

The three triangle vertices have the exact exterior neighbourhoods

```text
P_p=N_G(p)-Delta,                    |P_p|=3,
P_t={x,y,u_t},                       |P_t|=3,
P_q={b} union R_0,                  |P_q|=3.
```

Here `P_p` is the three-vertex adhesion of the singleton atom and
`|R_0|=2`.

## Lemma 1 (two triangle contacts)

Every component `C` of `G-L` is adjacent to at least two vertices of
`Delta`.

### Proof

Suppose that `C` had only one neighbour in `Delta`, say `u`.  Since `C`
is a component after deleting `L`, all its external neighbours would lie
in

```text
R union {u}.
```

It is adjacent to all three members of `R`, so this four-set would be an
actual vertex cut of `G`.  This contradicts five-connectivity.  \(\square\)

In particular, if `C` misses `u in Delta`, then

```text
N_G(C)=R union (Delta-{u})                         (1)
```

is an exact five-cut.

## Lemma 2 (at most four components)

The graph `G-L` has at most four components.

### Proof

For `u in Delta`, let `c_u` be the number of components of `G-L` adjacent
to `u`.  Distinct components require distinct neighbours of `u` outside
`Delta`, and every such neighbour lies either in `R` or in one component.
Since `|P_u|=3`,

```text
c_u+|R intersect P_u|<=3.
```

If `m` is the number of components, Lemma 1 gives

```text
2m <= c_p+c_t+c_q <= 9-|E_G(Delta,R)|.                (2)
```

Hence `m<=4`.  \(\square\)

Exact accounting at the six-cut will also be used below.  Since
`|E(G)|=4|V(G)|-7`,

```text
sum_C eta_L(C)=17-|E(G[L])|
              =14-|E(G[R])|-|E_G(Delta,R)|.           (3)
```

## Theorem 3 (tiny misser, rigid high misser, or a six-full component)

Let `C` be a component of `G-L` which misses one vertex of `Delta`.
Exactly one of the following holds.

1. `|C|<=2` and its excess at the exact five-cut (1) is at most three.
2. `|C|=a`, its excess at (1) is at least four, `G-L` has exactly two
   components, and the other component is a singleton.

Consequently, if no component of the second type occurs, some component
of `G-L` is adjacent to all six vertices of `L`.

### Proof

Apply the universal five-cut high-excess lemma to (1).  If `C` itself has
excess at least four, the minimum choice of `a` gives `|C|>=a`.  There are
`a+1` vertices outside `L` and at least one other component, so necessarily
`|C|=a` and the remaining component is a singleton.

If `C` has excess at most three, the universal lemma gives a different
component of excess at least four behind (1).  That component has order at
least `a`.  Since a five-cut leaves `a+2` vertices, `|C|<=2`.

Now suppose that no high misser occurs and no component is adjacent to all
of `Delta`.  Every component then has order at most two.  Lemma 2 bounds
their total order by eight, whereas `G-L` has order `a+1>=9`.  This is a
contradiction.  \(\square\)

## Theorem 4 (the high `p`- and `q`-misser swap)

Suppose that a component `C` of order `a` misses `p`.  Let `D={d}` be the
other component of `G-L`.  Then there is a vertex `r` in the connected
exterior of the singleton cut `N_G(p)` such that

```text
R=(P_p-{d}) union {r},               d in P_p.          (4)
```

The five-cut

```text
Q_p=R union {t,q}
```

has exactly the two components `C` and `{p,d}`.  Put

```text
k=|N_G(d) intersect {t,q}| in {1,2}.
```

Then

```text
delta_Q_p({p,d})=k,
delta_Q_p(C)=17-|E(G[L])|-k,
4<=delta_Q_p(C)<=8,
|E(G[L])|+k>=9.                                      (5)
```

The symmetric statement holds when `C` misses `q`, with `P_q` in place
of `P_p`, the low edge `{q,d}`, and
`k=|N_G(d) intersect {p,t}|`.

### Proof

The singleton cut `N_G(p)=P_p union {t,q}` has exactly two components:
`{p}` and its connected exterior `E_p=G-N_G[p]`.  The set `E_p` has order
`a+1`.  Since `C` misses `p`, it contains no member of `P_p`, and hence
`C subseteq E_p`.

Every vertex of `R` belongs to exactly one of `P_p,E_p`.  Counting the
`a+1` vertices of `E_p` and the three vertices of `P_p` across `R,C,{d}`
leaves two possibilities.  Either `R=P_p` and `d in E_p`, or `R` contains
two members of `P_p`, the omitted member is `d`, and its third member is a
vertex `r in E_p`.  The first possibility would say that

```text
G-N_G[p]=G-L=C disjoint union {d},
```

contrary to the connectedness of `E_p`.  This proves (4).

Fullness at the lifted cut makes `d` adjacent to all of `R` and to at
least two triangle vertices.  One of those vertices is `p`, because
`d in P_p`, so `k in {1,2}`.  Restoring `p` to `G-L` joins it to `d` but
not to `C`; hence `G-Q_p` has exactly the two stated components.

The low edge has one internal edge, four incidences from `p` to `Q_p`,
and `3+k` incidences from `d`.  Therefore

```text
delta_Q_p({p,d})=1+4+(3+k)-8=k.
```

The vertex `p` has exactly four neighbours in `L`, so

```text
|E(G[Q_p])|=|E(G[L])|-4.
```

The exact five-cut identity now gives the middle equality in (5).  The
lower bound is the present high-misser case.  Since `C` has the same order
as the globally selected lobe `A`, the maximum-excess tie-break and
`delta_S(A)=8` give the upper bound.  The final inequality follows.

For `q`, the original further leaf cut `N_G(q)` likewise has singleton
component `{q}` and one connected exterior.  The identical argument uses
`P_q`, and `q` again has four neighbours in the lifted six-set.  \(\square\)

## Theorem 5 (the high `t`-misser normal forms)

Suppose that a component `C` of order `a` misses `t`, and let `{d}` be the
other component of `G-L`.  Exactly one of the following holds.

1. The vertices `t,d` are nonadjacent,

   ```text
   R={x,y,u_t},
   N_G(t)=N_G(d)={x,y,u_t,p,q}.
   ```

   With `Q_t={x,y,u_t,p,q}`, one has

   ```text
   G[Q_t]=(x-u_t-y) disjoint union (p-q),
   delta_Q_t(C)=8.
   ```

   Thus this is an exact reorientation of the original two-singleton
   residue, not a strict descent.

2. The vertices `t,d` are adjacent.  Then `d=u_t` and

   ```text
   R={x,y,r}
   ```

   for some vertex `r` adjacent to `u_t`.  Put

   ```text
   alpha=|N_G(r) intersect {p,q}|,
   beta =|N_G(u_t) intersect {p,q}| in {1,2},
   sigma=1 if r in S, and sigma=0 otherwise.
   ```

   Exact accounting gives

   ```text
   |E(G[L])|=5+alpha+2 sigma,
   eta_L({u_t})=beta,
   eta_L(C)=12-alpha-2 sigma-beta,
   alpha+2 sigma+beta>=4.                              (6)
   ```

### Proof

The only neighbours of `t` outside `Delta` are `x,y,u_t`.  If `td` is
absent, all three must lie in `R`, because `C` misses `t`.  Thus
`R={x,y,u_t}`.  The singleton `d` is adjacent to every member of `R` and,
by Lemma 1, to both `p,q`.  It cannot lie in `A`, since `x,y` have no
neighbours there; hence `d in S`.  The vertices `t,u_t,d` form the
three-vertex path component of `G[S]`, and

```text
N_G(t)=N_G(d)=Q_t.
```

Deleting `Q_t` leaves the high component `C` and the two singleton
components `{t},{d}`.  Reapply the proved two-singleton boundary
classification to the minimum-order high lobe `C`.  It gives exactly
`G[Q_t]=P_3` disjoint union `K_2` in the displayed orientation.  The
five-cut identity then gives `delta_Q_t(C)=8`.

Suppose instead that `td` is an edge.  Then `d` belongs to
`{x,y,u_t}`.  It cannot be `x` or `y`: the other twin belongs to `R`,
while fullness of the singleton component `{d}` would force the forbidden
edge `xy`.  Hence `d=u_t`, and the two remaining neighbours `x,y` of `t`
belong to `R`; write `R={x,y,r}`.  Fullness gives `u_t r`.

Inside `L`, there are the three edges of `Delta`, the edges `tx,ty`, the
`alpha` edges from `r` to `{p,q}`, and exactly two edges from `r` to
`{x,y}` when `r in S`.  If `r notin S`, it lies in `A` and has no edge to
either twin.  This proves the first identity in (6).  The singleton
`u_t` has the four neighbours `t,x,y,r` in `L` and its `beta` contacts
with `{p,q}`, proving `eta_L({u_t})=beta`.  Equation (3) gives the formula
for `eta_L(C)`.  Finally `C` is a high component of the same order as the
selected lobe, and it misses `t`, so
`eta_L(C)=delta_{L-{t}}(C)`.  The maximum-excess tie-break gives
`eta_L(C)<=8`, which is the last inequality in (6).  \(\square\)

## 6. Exact endpoint and nonclosures

Every four-cut returned by the triangle contraction therefore has at most
four complementary components and falls into one of two structural
classes:

1. a high component misses a triangle vertex, in which case there are
   exactly two components and the other is a singleton; for misses at
   `p` or `q`, Theorem 4 gives the exact one-vertex adhesion swap and the
   low-edge excess in (5), while Theorem 5 gives an exact reorientation or
   edge-low-side normal form for a miss at `t`; or
2. some component is adjacent to all six vertices of `L`, while every
   component missing a triangle vertex has order at most two.

Nor does the six-full component in outcome 2 close the minor by contacts
alone.  The audited
[lifted-triangle contact barrier](../barriers/hc7_e5_triangle_lift_contact_barrier.md)
has two nonadjacent component vertices complete to a triangle and another
three-set, yet excludes `K_7^-`.  It is only a contracted contact quotient,
not a five-connected host.  Thus internal component density may still
split a full component into the required branch sets, but that is an
additional theorem.

The smallest live repair is now a labelled model-or-descent theorem for
these two classes: turn the high-misser swaps and reorientation into strict
descent, or use the internal structure of a six-full component to split the
contracted `K_7^vee` bag or construct `K_7^-`.  Component contact alone is
insufficient.
