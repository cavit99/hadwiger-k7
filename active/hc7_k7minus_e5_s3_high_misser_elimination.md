# Elimination of the high triangle-missing components

**Status:** active computation-free written reduction; separately audited in
the [adjacent audit](hc7_k7minus_e5_s3_high_misser_elimination_audit.md).
This note does not prove `(E5)`.

Write `K_7^-` for `K_7` with one edge deleted.  Let `G` be a minimum
`E5` enemy, so

```text
|E(G)|=4|V(G)|-7
```

and `G` is five-connected.  For a five-cut `Q` and a component `C` of
`G-Q`, put

```text
delta_Q(C)=|E(G[C])|+|E_G(C,Q)|-4|C|.
```

The purpose of this note is twofold.  First, it replaces the former
maximum-excess secondary choice by a boundary-sensitive choice which is
compatible with the companion-cut and edge-atom reductions.  Secondly,
it uses that choice, together with one further exact five-cut, to exclude
every high component which misses a vertex of the contracted singleton
triangle.

## 1. Boundary-complement selection

For a five-cut `Q` and a component `C` with `delta_Q(C)>=4`, define

```text
Phi(Q,C)=delta_Q(C)+|E(G[Q])|,
rho(Q,C)=number of components of G-Q other than C.
```

### Lemma 1 (complement-excess identity)

For every such pair,

\[
 \Phi(Q,C)=13-
   \sum_{D\in\mathcal C(G-Q),\ D\ne C}\delta_Q(D).       \tag{1}
\]

### Proof

Exact accounting at a five-cut gives

\[
 \sum_{D\in\mathcal C(G-Q)}\delta_Q(D)=13-|E(G[Q])|.
\]

Move the term indexed by `C` to the other side and use the definition of
`Phi`.  \(\square\)

Choose `(S,A)` globally among all five-cut--component pairs of excess at
least four by the following lexicographic rule:

1. minimise `|A|`;
2. subject to that, maximise `Phi(S,A)`;
3. subject to both, minimise `rho(S,A)`.

This is well-founded because `G` is finite.  Every reduction preceding the
`s=3` companion-cut argument uses only the first coordinate: no component
of excess at least four behind a five-cut has order below `|A|`.

In the exact two-singleton row, write

```text
G-S has components A,{x},{y},
N_G(x)=N_G(y)=S,                    xy is not an edge,
G[S]=P_3 disjoint union K_2.
```

Each singleton has excess one.  Since `|E(G[S])|=3`, the cut identity gives

```text
delta_S(A)=8,                       Phi(S,A)=11,
rho(S,A)=2.                                             (2)
```

The rest of this note assumes that the globally selected pair lies in
this exact row and then in its `s=3` singleton branch.

## 2. Compatibility with the route to the singleton triangle

The structural parts of the companion-cut and edge-atom arguments do not
use the former maximum-excess tie-break.  The next two lemmas record how
their terminal comparisons change under the selection above.

### Lemma 2 (the companion cut remains impossible)

The excess-two four-separator normal form in the atomic six-boundary
reduction does not occur.

### Proof

Lemmas 1--3 of the companion-cut reduction use the density-safe
contraction of `bq`, five-connectivity, and minimum component order.  They
produce the exact five-cut

```text
Sigma={b,c,q,x,y}
```

with two components: a component `L` of order `|A|` and a low edge.  The
exact data are

```text
|E(G[Sigma])|=2,
delta_Sigma(L)=9,
delta_Sigma(low edge)=2.
```

Consequently

```text
Phi(Sigma,L)=11=Phi(S,A),
rho(Sigma,L)=1<2=rho(S,A).
```

This contradicts the third coordinate of the global choice.  \(\square\)

### Lemma 3 (the edge atom still reduces to the singleton atom)

In the order-three edge atom `{p,b}`, let `k` be the number of adhesion
neighbours of `p`, as in the edge-atom reduction.  If `k=2`, the exact
neighbourhood of `p` is a five-cut with singleton component `{p}` and one
connected exterior.  If `k=3`, then `G` contains `K_7^-` or the revised
global choice is contradicted.  Hence the only surviving order-three atom
is the singleton `{p}`.

### Proof

The `k=2` argument is independent of every secondary tie-break and gives
the stated singleton cut directly.

For `k=3`, the density-safe contraction and placement argument from the
edge-atom reduction returns

```text
Sigma={b,p,q,x,y},                  |E(G[Sigma])|=3,
```

with a high component `K` of order `|A|` and one low edge `L`.  If the
selected leaf `t` is not in `L`, the rooted six-bag construction in that
reduction gives an explicit `K_7^-` model; it uses no secondary lobe
choice.

It remains there to consider `L={t,u_t}`.  Put `epsilon=1` when `q u_t`
is an edge and `epsilon=0` otherwise.  Exact accounting gives

```text
delta_Sigma(L)=1+epsilon,
delta_Sigma(K)=9-epsilon.
```

If `epsilon=0`, then `Phi(Sigma,K)=12>11`.  If `epsilon=1`, then
`Phi(Sigma,K)=11` but `rho(Sigma,K)=1<2`.  Both alternatives contradict
the revised choice.  Thus `k=3` is impossible, and the `k=2` singleton is
the sole surviving atom.  \(\square\)

The singleton-triangle contraction therefore remains available with the
new selection.  Use its notation

```text
Delta={p,t,q},
L=Delta union R,                    |R|=3.
```

Every component of `G-L` is adjacent to all three vertices of `R` and to
at least two vertices of `Delta`.  A component missing a triangle vertex
is either a low component of order at most two or a high component of
order `a=|A|` accompanied by one singleton.  If no high missing component
exists, some component of `G-L` is adjacent to all six vertices of `L`.

## 3. High components missing `p` or `q`

### Lemma 4

No high component of `G-L` misses `p` or `q`.

### Proof

Suppose first that the order-`a` component `C` misses `p`, and let `{d}`
be the other component of `G-L`.  The connected-exterior swap in the
triangle-cut refinement gives an exact five-cut

```text
Q_p=R union {t,q}
```

whose components are `C` and the low edge `{p,d}`.  Moreover

```text
k=|N_G(d) intersect {t,q}| is 1 or 2,
delta_Q_p({p,d})=k.
```

The component `C` is high by hypothesis.  Lemma 1 therefore gives

```text
Phi(Q_p,C)=13-k.
```

If `k=1`, this is `12>11`.  If `k=2`, it equals eleven, while
`rho(Q_p,C)=1<2`.  Either case contradicts the global choice in (2).

For a high component missing `q`, the symmetric connected-exterior swap
gives the low edge `{q,d}` with excess one or two.  The same comparison
applies.  \(\square\)

## 4. A high component missing `t` and leaving a low edge

### Lemma 5

Suppose that a high component `C` of `G-L` misses `t`, the other component
is `{d}`, and `td` is an edge.  This is impossible.

### Proof

The exact normal form in the triangle-cut refinement says

```text
d=u_t,                              R={x,y,r},
beta=|N_G(u_t) intersect {p,q}| is 1 or 2.
```

Since `C` misses `t`, the set

```text
Q_t=L-{t}=R union {p,q}
```

is an exact five-cut.  Restoring `t` joins it to `u_t` but not to `C`, so
`G-Q_t` has precisely the two components `C` and `{t,u_t}`.  The low edge
has one internal edge; `t` has four incidences with `Q_t`, and `u_t` has
`3+beta` incidences.  Hence

```text
delta_Q_t({t,u_t})=1+4+(3+beta)-8=beta.
```

Lemma 1 gives `Phi(Q_t,C)=13-beta`.  For `beta=1` this is twelve.  For
`beta=2` it is eleven but `rho(Q_t,C)=1`.  Both alternatives contradict
(2).  \(\square\)

## 5. The apparent reorientation gives strict order descent

It remains to treat the normal form in which a high component misses `t`
and the opposite singleton `d` is nonadjacent to `t`.  This case was
previously recorded as a same-order reorientation.  The following cut
eliminates it without using either secondary coordinate.

### Lemma 6 (central five-cut)

The nonadjacent `t`-misser normal form contains a component of excess at
least four and order strictly below `a` behind another five-cut.

### Proof

Write the original boundary as

```text
G[S]=(t-u-d) disjoint union (r-s),
```

where `t-u-d` is the three-vertex path.  Put

```text
P={p,q},                            X={x,y},
B=A-P.
```

Here `p,q` are vertices of `A` and the imported order bound is `a>=8`,
so `B` is nonempty.

The nonadjacent normal form has the reoriented boundary

```text
Q=X union {u} union P,
G[Q]=(x-u-y) disjoint union (p-q),
N_G(t)=N_G(d)=Q.                                    (3)
```

Its high component is `B union {r,s}`.  Define the five-set

```text
W=P union {u,r,s}.                                   (4)
```

Let `K` be a component of `G[B]`.  Vertices of `B` have no neighbours in
`X`, because `N_G(x)=N_G(y)=S`, and no neighbours in `{t,d}`, by (3).
Every neighbour of `K` outside `B` therefore lies in `W`.  Since another
vertex survives the deletion of `N_G(K)`, five-connectivity gives

```text
N_G(K)=W.                                             (5)
```

In particular, every component of `G[B]` is adjacent to each of the five
vertices in `W`.

Let `c` be the number of components of `G[B]` and put

```text
m=|E_G(P,{r,s})|.
```

The vertices `p,q` both have degree five.  Each is adjacent to its mate
in `P` and to both `t,d`; it is adjacent to neither `x,y` nor `u`.
Consequently, for each `v in P`,

```text
d_B(v)+d_{ {r,s} }(v)=2.                             (6)
```

Equation (5) gives `d_B(p),d_B(q)>=c`.  It follows from (6) that

```text
c<=2,                       m<=4-2c.                  (7)
```

Deleting `W` leaves exactly the components of `G[B]` and the connected
four-vertex graph

```text
D=G[X union {t,d}]=K_{2,2}.
```

There are precisely `2+m` edges in `G[W]`: the edges `pq`, `rs`, and the
`m` edges between their endpoint pairs.  The vertex `u` has no edge to
`P` by (3) and no edge to `{r,s}` in the original boundary.  The component
`D` has four internal edges and twelve incidences with `W`: each member of
`X` meets `u,r,s`, while each of `t,d` meets `u,p,q`.  Thus

```text
delta_W(D)=4+12-4*4=0.                               (8)
```

Applying the exact five-cut identity at `W` and using (8) yields

```text
sum_{K in components of G[B]} delta_W(K)
    =13-(2+m)=11-m.                                  (9)
```

If `c=1`, then (7)--(9) give `delta_W(B)>=9`.  If `c=2`, then (7) gives
`m=0`, so one of the two components has integer excess at least six.
In both cases there is a component `K` behind `W` with

```text
delta_W(K)>=4,                    |K|<=|B|=a-2<a.
```

This contradicts the first coordinate of the global choice.  \(\square\)

## 6. Conclusion and scope

### Theorem 7 (high-misser elimination)

In the exact `s=3` singleton-triangle residue selected by minimum high
component order, then maximum `Phi`, then minimum `rho`, no order-`a`
component behind a lifted triangle cut can miss a vertex of `Delta`.
Consequently every such lifted cut has a component adjacent to all six of
its vertices.

### Proof

Lemmas 4--6 exclude respectively a miss at `p` or `q`, an adjacent miss
at `t`, and the nonadjacent miss at `t`.  The triangle-cut dichotomy then
supplies a component adjacent to all six cut vertices.  \(\square\)

This theorem does not turn a six-full component into a `K_7^-` model.
The contracted contact quotient is known not to suffice; the internal
structure or density of that component must be used.  Thus the sole
remaining class after the singleton-triangle contraction is the
six-full-component class, and `(E5)` remains open.

## Dependencies

The proof uses the following written reductions.

- The
  [singleton-contraction uncrossing](hc7_k7minus_e5_singleton_contraction_uncrossing.md)
  supplies a component of excess at least four behind every five-cut and
  justifies the minimum-order comparisons.
- The
  [atomic six-boundary reduction](hc7_k7minus_e5_six_boundary_atomic_reduction.md)
  supplies the three- and four-separator alternatives.
- The structural lemmas in the
  [companion-cut elimination](hc7_k7minus_e5_s3_companion_cut_elimination.md)
  give the exact companion cut used in Lemma 2.  Lemma 2 replaces its
  former maximum-excess comparison.
- The
  [edge-atom elimination](hc7_k7minus_e5_s3_edge_atom_elimination.md)
  supplies the exact `k=2` singleton reduction, the `k=3` returned cut,
  and the explicit rooted model used in Lemma 3.  Lemma 3 replaces its
  sole maximum-excess subcase.
- The
  [singleton-triangle contraction](hc7_k7minus_e5_s3_triangle_contraction_reduction.md)
  supplies the lifted order-six cut.
- The
  [triangle-cut refinement](hc7_k7minus_e5_s3_triangle_cut_refinement.md)
  supplies the missing-component dichotomy and the exact high-misser
  normal forms used in Lemmas 4--6.
- The contact-only limitation is recorded by the
  [lifted-triangle contact barrier](../barriers/hc7_e5_triangle_lift_contact_barrier.md).

All uses of the older maximum-excess tie-break have been replaced inside
the route invoked here.  No claim is made that unrelated branches of the
`E5` programme acquire the revised secondary choice without a separate
dependency check.
