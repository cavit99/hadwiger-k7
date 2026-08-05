# Missed-root mass and both-endpoints boundary bounds

**Status:** written computation-free proof; separate internal audit GREEN for
the pinned revision in the
[adjacent audit](hc7_k7minus_e5_six_boundary_mass_bounds_audit.md).  This
theorem is conditional on the selected minimum-`E5` setting imported below.
It does not prove `(E5)`.

Write `K_7^-` for `K_7` with one edge deleted.

## 1. Imported setting

Use the exact kernel configurations of the audited
[second-contraction reduction](../active/hc7_k7minus_e5_s3_second_contraction_kernel_reduction.md).
Thus `G` is the selected minimum `E5` enemy,

```text
|V(G)|=a+7,                    |E(G)|=4|V(G)|-7,
a>=8,
```

and a six-set `P` exposes one of the labelled low kernels `T=K_2,P_3,K_3`.
The opposite shore has order `a-1` in the `K_2` case and `a-2` in the
`P_3,K_3` cases.  A component is **`P`-six-full** when its neighbourhood is
all of `P`.  Every other opposite component misses exactly one root `r` of
`P`; Proposition 5.2 of the imported reduction says that it is either

1. a singleton complete to `P-{r}`; or
2. an edge whose two ends are each complete to `P-{r}`.

For `r in P`, let `M_r` be the family of opposite components missing `r`
and put

```text
sigma_r=sum_{K in M_r}|K|.
```

The degree-five endpoint is denoted by `u`.  In the `K_2` kernel it already
sees the other original endpoint and the two low vertices.  In the
`P_3,K_3` kernels it already sees four vertices in the favourable
orientation and two vertices in the other orientation.

## 2. Missed-root mass

### Theorem 2.1

For every `r in P`,

\[
                         \sigma_r\le2.                 \tag{2.1}
\]

### Proof

There is nothing to prove when `M_r` is empty.  Otherwise delete the
five-set `Q_r=P-{r}`.  Every member of `M_r` remains a separate component.
All remaining vertices outside `Q_r` lie in one connected central component:

- `r` has a neighbour in the connected low kernel;
- every `P`-six-full component meets `r`; and
- a component missing `s!=r` is complete to `P-{s}` and therefore meets
  `r`.

The central component contains `r` and the low kernel, so it has at least
three vertices.  Exactly `a+2` vertices lie outside `Q_r`.  Consequently no
member of `M_r` has order at least `a`.

The universal five-cut theorem supplies a component of excess at least four.
The minimum choice of the selected lobe makes its order at least `a`, so it
must be the central component.  At most two vertices remain outside it.
This proves (2.1).  \(\square\)

## 3. A six-full component is forced

### Theorem 3.1

Every kernel shore contains a `P`-six-full component.  Moreover the number
of such components is at most

| low kernel and orientation | maximum number |
|---|---:|
| `K_2` | 2 |
| favourable `P_3` or `K_3` | 1 |
| other `P_3` or `K_3` orientation | 3 |

### Proof

Suppose first that no opposite component is `P`-six-full.  Every vertex in
a component which does not miss `u` is adjacent to `u`, while Theorem 2.1
bounds the total order of components missing `u` by two.

In the `K_2` case, three neighbours of the degree-five vertex `u` are
already fixed, leaving at most two opposite vertices which do not miss `u`.
The opposite shore would therefore have order at most `2+2=4`, contrary to
`a-1>=7`.

In the favourable `P_3,K_3` orientation, four neighbours of `u` are fixed.
The shore would have order at most `1+2=3`, contrary to `a-2>=6`.  In the
other orientation two neighbours are fixed, giving the still impossible
bound `3+2=5<a-2`.

Finally, each `P`-six-full component contains a distinct neighbour of `u`.
The same three residual degree capacities are respectively two, one and
three, proving the displayed multiplicity bounds.  \(\square\)

## 4. Both-endpoints separations

Return to the nontrivial four-separation in Section 4 of the imported
reduction, but suppose both original contraction endpoints meet both open
sides.  Its lift has six-boundary

```text
R={u,d,v} union U,                 |U|=3,
```

where `u,d` have degree five, `ud,uv,dv` are edges, and both `u,d` meet both
open sides.

### Theorem 4.1

The boundary satisfies

\[
                         |E(G[R])|\le11.               \tag{4.1}
\]

If equality holds, then

```text
G[{v} union U]=K_4,
|E_G({u},U)|=|E_G({d},U)|=1,
```

and each of `u,d` has exactly one neighbour in each open side.  For the
components `K` of `G-R`, with

```text
eta_R(K)=|E(G[K])|+|E_G(K,R)|-4|K|,
```

one has the exact identity

\[
             \sum_K\eta_R(K)=17-|E(G[R])|.            \tag{4.2}
\]

### Proof

Each of `u,d` is adjacent to the other two vertices of `{u,d,v}` and has a
neighbour in each open side.  Its degree is five, so it has at most one
neighbour in `U`.  Therefore

\[
 |E(G[R])|
 \le {4\choose2}+3+1+1
 =11.
\]

Equality forces the four vertices `{v} union U` to induce `K_4` and forces
both remaining upper bounds to be equalities.  The degree-five condition
then leaves exactly two neighbours outside `R` for each of `u,d`; fullness
to both open sides puts one in each.

The components outside `R` have total order `a+1`.  Substituting
`|E(G)|=4a+21` into the definition of `eta_R` gives

\[
 4a+21=|E(G[R])|+4(a+1)+\sum_K\eta_R(K),
\]

which is (4.2).  \(\square\)

## 5. Scope

Theorems 2.1 and 3.1 eliminate the possibility that an opposite shore is an
unbounded collection of non-six-full components, and they bound the number
of six-full components.  They do not control the order or internal structure
of a six-full component.

Theorem 4.1 improves the earlier twelve-edge boundary estimate.  Only its
eleven-edge equality case has the displayed literal `K_4` core.  Every
both-endpoints case with at most ten boundary edges remains open; the larger
total excess in (4.2) does not by itself produce a high-excess component
behind a five-cut.
