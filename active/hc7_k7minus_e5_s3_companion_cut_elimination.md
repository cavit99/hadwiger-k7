# The companion cut eliminates the four-separator atom

**Status:** active computation-free written reduction; see the
[separate internal audit](hc7_k7minus_e5_s3_companion_cut_elimination_audit.md).
This note does not prove `(E5)`.

Write `K_7^-` for `K_7` with one edge deleted.  Use the notation and
hypotheses of the
[atomic six-boundary reduction](hc7_k7minus_e5_six_boundary_atomic_reduction.md).
Thus `G` is a minimum `E5` enemy,

```text
G-S has components A,{x},{y},
N_G(x)=N_G(y)=S,                    xy is not an edge,
G[S]=P_3 disjoint union K_2,
```

and the crossing singleton row has

```text
N_G(q)={t,p,b} union R_0,           |R_0|=2,
F=G-{x,y,t,q},                     Z=S-{t}.
```

As in the minimum-lobe reduction, choose `(S,A)` first with `|A|`
minimum among all pairs consisting of a five-cut and a component of
excess at least four.  Refine this harmlessly by choosing, subject to
minimum order, `delta_S(A)` maximum.  Since `G[S]` has three edges,

\[
                         \delta_S(A)=8.               \tag{1}
\]

Suppose the last four-separator normal form of Corollary 8 of the atomic
reduction occurs.  There are a vertex `c` and a four-set `T` such that

```text
C={b,c},                            N_G(C)=T union {q},
N_G(b)={q,c} union T,               N_G(c)={b} union T,
```

and `T union {q}` is an exact five-cut.  In particular, `b,c` are
adjacent to every member of `T`, and `t` is not in `T` because `T` is a
subset of `V(F)`.

The purpose of this note is to exclude this normal form.

## 1. A density-safe companion cut

### Lemma 1

There is a three-set `D` such that

\[
                         Q'={b,q}\mathbin\cup D       \tag{2}
\]

is an exact five-cut of `G`.

#### Proof

The exact neighbourhoods above and the singleton-row description give

```text
d_G(b)=6,                            d_G(q)=5,
N_G(b) intersect N_G(q)=T intersect ({p} union R_0).
```

The last set has order at most three.  Contracting `bq` therefore loses
at most

\[
             1+|N_G(b)\cap N_G(q)|\le4
\]

edges.  Consequently

\[
 |E(G/bq)|\ge4|V(G)|-11=4|V(G/bq)|-7.                \tag{3}
\]

The proper minor `G/bq` is target-free.  By the minimum choice of `G`, it
is not five-connected.  Every cut of order at most four in `G/bq`
contains the contracted vertex, since otherwise it would also be a cut
of `G`.  Replacing the contracted vertex by `b,q` lifts such a cut to a
cut of `G` of order at most five.  Five-connectivity makes its order
exactly five, proving (2).  \(\square\)

Every component behind `Q'` is adjacent to all five vertices of `Q'`, as
is standard for a component behind a minimum cut in a five-connected
graph.

## 2. The lift is forced onto the two singleton lobes

### Lemma 2

The three-set in (2) is

\[
                              D=\{x,y,c\}.             \tag{4}
\]

#### Proof

First suppose that `D` contains exactly one of `x,y`, say `x`.  Every
component of `G-Q'` must be adjacent to `x`, and hence must contain a
surviving member of `S`.  The surviving twin `y` joins all such boundary
vertices, so all components coincide, a contradiction.

Suppose next that `D` contains neither twin.  The vertices `x,y` and all
surviving members of `S` lie in one component `K` of `G-Q'`.  Any other
component must meet `q`.  Its only possible `q`-neighbour outside `K` is
`p`, because

```text
N_G(q)-{b,p}={t} union R_0 is contained in S.
```

Thus there is exactly one other component `P`, it contains `p`, and it
is contained in `A`.

There are `|A|+2` vertices outside a five-cut.  The universal five-cut
excess lemma supplies a component of excess at least four and hence of
order at least `|A|`.  The component `K` contains `x,y` and at least two
surviving roots, so it has order at least four and cannot be the side of
order at most two.  It follows that

\[
                              |P|\le2.                 \tag{5}
\]

Since `pt` is an edge while `P` and `K` are distinct components, `t`
must belong to `D`.  Fullness of `P` to `Q'` now gives

\[
                    N_F(P)=\{b\}\mathbin\cup(D-\{t\}),
                    \qquad |N_F(P)|=3.                \tag{6}
\]

The component `P` contains `p` and no member of `Z`.  Equation (6) is a
rooted separation of `(F,Z)` of order three, contrary to the standing
internal four-connectivity in the four-separator branch.  Therefore `D`
contains both twins, and we may write `D={x,y,v}`.

If `v` is not `c`, then all neighbours of `b` outside `Q'` lie in the
connected set

\[
                         \{c\}\mathbin\cup(T-\{v\}).  \tag{7}
\]

Indeed, `c` survives and is adjacent to every surviving member of `T`.
Every component behind `Q'` must contain a neighbour of `b`, so (7) would
put them all in one component.  This contradiction forces `v=c`, proving
(4).  \(\square\)

Put

\[
                            \Sigma=\{b,c,q,x,y\}.       \tag{8}
\]

The cut `Sigma` has only the two internal edges `bc,bq`.

## 3. Exact classification behind the companion cut

### Lemma 3

The graph `G-Sigma` has exactly two components.  One, say `L`, has

\[
                         |L|=|A|,\qquad \delta_\Sigma(L)=9.       \tag{9}
\]

The other is precisely the two vertices of the `K_2` component of
`G[S]`; call them `u,v`.  After interchanging their names if necessary,

```text
q is adjacent to u and not to v,
u and v both belong to T,
N_G(v)={u,b,c,x,y},
N_G(u)={v,b,c,q,x,y}.
```

In particular,

\[
                         \delta_\Sigma(\{u,v\})=2.     \tag{10}
\]

#### Proof

Every component behind `Sigma` contains a member of `S`, because it is
adjacent to `x`.  The universal five-cut excess lemma supplies a component
of order at least `|A|`; since exactly `|A|+2` vertices lie outside
`Sigma`, all remaining components have total order at most two.

No remaining component can be a singleton.  Such a component would be a
single member of `S`, but all five members of `S` survive `Sigma` and
every vertex of `G[S]=P_3` disjoint union `K_2` has a boundary neighbour.
That neighbour would lie in the same component.  Hence there are exactly
two components, of orders `|A|` and two.

Let `P` be the two-vertex component.  It contains a member of `S`.  If its
other vertex lay in `A`, that vertex would have at most one neighbour in
`P` and at most the three neighbours `b,c,q` in `Sigma`; vertices of `A`
are nonadjacent to `x,y`.  This would contradict minimum degree five.
Thus both vertices of `P` lie in `S`.  They form an edge of `G[S]`, and
no boundary edge may leave `P` because `Sigma` contains no member of `S`.
Therefore `P` is the whole `K_2` component of `G[S]`.

The vertex `t` is not in `P`, since `p` survives `Sigma` and `pt` is an
edge.  Thus `t` is an end of the `P_3`; write that path as `t-a-d`.  The
six-row restriction in Corollary 10 of the atomic reduction says that
`R_0` is `{a,u}` or `{a,v}`.  Rename the two vertices so that `R_0`
contains `u`.  Then `q` is adjacent to `u` and not to `v`.

The vertex `v` already has the three neighbours `u,x,y`, and its only
other possible neighbours are `b,c`; minimum degree forces both.  The
vertex `u` has the four neighbours `v,q,x,y`, so it meets at least one of
`b,c`.  The exact neighbourhoods of the atomic edge say that a vertex
other than `b,c,q` is adjacent to either `b` or `c` precisely here only
through membership in `T`; both `b` and `c` are complete to `T`.
Consequently `u,v` both belong to `T` and have the displayed exact
neighbourhoods.

The small edge has nine incidences with `Sigma`: four to `x,y`, four to
`b,c`, and the edge `uq`.  This proves (10).  Finally,

\[
 \sum_{K\in\mathcal C(G-\Sigma)}\delta_\Sigma(K)
      =13-|E(G[\Sigma])|=11.                           \tag{11}
\]

Equations (10)--(11) give (9).  \(\square\)

## 4. Elimination by the refined minimum choice

### Theorem 4

Under the refined minimum-lobe choice above, the excess-two
four-separator normal form of the atomic six-boundary reduction does not
occur.

#### Proof

The pair `(Sigma,L)` supplied by Lemma 3 is another five-cut and
high-excess component.  It has the same component order `|A|` as the
chosen pair `(S,A)`, but

\[
                         \delta_\Sigma(L)=9>8=\delta_S(A).
\]

This contradicts the maximum-excess tie-breaker.  \(\square\)

### Corollary 5

In a target-free `s=3`, singleton-`q` row chosen by minimum lobe order and
then maximum lobe excess, `(F,Z)` is not internally four-connected.  The
only remaining outcomes are therefore the two order-three atoms from
Theorem 6 of the atomic reduction:

\[
                              \{p\},\qquad \{p,b\}.     \tag{12}
\]

Their lifted separator is `T_3 union {t,q}`, their excess is one or two,
and deleting the atom from `F` leaves at least `4|V|-7` edges.  No rooted
minor conclusion for these two atoms is asserted here.

## 5. Exact endpoint

The former nominated-root-bag obstruction in the four-separator branch is
not a genuine terminal case: the density-safe edge `bq` exposes the
companion cut `Sigma`, and exact excess accounting contradicts the refined
choice of the dense lobe.

The smallest remaining repair in this crossing row is now confined to the
order-three atoms (12).  It must either synchronise the residual rooted
model across their three-vertex adhesion, or turn the residual
`4|V|-7` density into a proper five-connected target-free minor or a
strict lexicographic lobe descent.  Merely deleting the atom does not
verify either connectivity conclusion.
