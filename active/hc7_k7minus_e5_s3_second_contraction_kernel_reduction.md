# Second contractions and labelled six-boundary kernels

**Status:** active written reduction, separately audited in the
[adjacent audit](hc7_k7minus_e5_s3_second_contraction_kernel_reduction_audit.md).
Sections 2--4 and Proposition 5.2 are computation-free.  Corollary 5.1 uses
the promoted computer-assisted
[six-boundary kernel screen](../results/hc7_k7minus_e5_six_boundary_kernel_screen.md).
The reduction closes the connected `P`-non-six-full kernel branch.  It does
not prove the proposed kernel-localisation lemma or `(E5)`.

Write `K_7^-` for `K_7` with one edge deleted.

## 1. Imported endpoint

Use Proposition 5 of the audited
[six-full contraction reduction](hc7_k7minus_e5_s3_six_full_contraction_reduction.md).
Thus `G` is the selected minimum `E5` enemy in the surviving `s=3` case,

```text
|V(G)|=a+7,                         |E(G)|=4|V(G)|-7,
```

and `a>=8`.  Let `uv` be a permitted density-safe edge from a degree-five
triangle vertex into a six-full component.  Put

```text
H=G/uv
```

and let `z` be the contracted vertex.  Then

```text
kappa(H)=4,                         |E(H)|>=4|V(H)|-7.
```

Every four-cut `X` of `H` contains `z` and has the exact form

```text
H-X={d} dot-union B,                N_H(d)=X,
d_H(d)=4,                           |B|=a+1,
```

where `B` is connected.  Lifting `X` through `z=uv` gives a five-cut of
`G`; boundary fullness makes the returned singleton `d` adjacent to both
`u,v` and hence gives `d_G(d)=5`.

For a cut `Q` and a component `C` of `G-Q`, write

```text
delta_Q(C)=|E(G[C])|+|E_G(C,Q)|-4|C|,
Phi(Q,C)=delta_Q(C)+|E(G[Q])|,
rho(Q,C)=number of components of G-Q other than C.
```

The selected original pair has

```text
(|A|,Phi(S,A),rho(S,A))=(a,11,2),
```

and the choice first minimises order, then maximises `Phi`, and then
minimises `rho`.

## 2. The anchored singleton switch

### Lemma 2.1

Fix a returned singleton `d`.

1. Contracting `dz` loses at most four edges.
2. If `H/dz` is not four-connected, there is another returned
   degree-four singleton `w` such that `d,w,z` are pairwise adjacent and

   ```text
   N_H(d) intersect N_H(w)={z}.
   ```

3. Contracting `dw` loses exactly two edges and `H/dw` is four-connected.

### Proof

Since `d_H(d)=4`, contracting `dz` loses

```text
1+|N_H(d) intersect N_H(z)|<=4.
```

Contracting an edge of a four-connected graph leaves a three-connected
graph: a cut of order at most two in the quotient would lift to a cut of
order at most three before contraction.  Hence, if `H/dz` is not
four-connected, it has a three-cut.  That cut contains the contracted
vertex, since otherwise it lifts unchanged to `H`.  Replacing the
contracted vertex by `{d,z}` gives a four-cut of `H`, which by the imported
normal form is `N_H(w)` for another degree-four singleton `w`.  In
particular `w` is adjacent to `d,z`.

If `d,w` had two common neighbours other than `z`, deleting those two
vertices and `z` would isolate the edge `dw`, contrary to
four-connectivity.  If they had exactly one, write

```text
N_H(d)={w,z,r,p},                   N_H(w)={d,z,r,q}.
```

Deleting `{z,r,p,q}` leaves the nonsingleton component `{d,w}`.  This
contradicts the assertion that every four-cut has one singleton component
and one connected remainder.  Thus their only common neighbour is `z`,
and contracting `dw` loses exactly two edges.

If `H/dw` were not four-connected, its three-cut would contain the
contracted vertex and would lift to a four-cut of `H` containing `d,w`.
The singleton belonging to that cut would be a common neighbour of `d,w`.
Every four-cut contains `z`, so the singleton is not `z`, contradicting
the preceding equality.  Therefore `H/dw` is four-connected.  \(\square\)

## 3. The adjacent-singleton `K_2` kernel

Suppose `H/dz` is not four-connected, and let `w` be supplied by Lemma
2.1.  Write

```text
N_H(d)={z,w,a_1,a_2},               N_H(w)={z,d,c_1,c_2}.
```

The two outside pairs are disjoint.  On expanding `z=uv`, both `d,w` are
adjacent to both `u,v`; otherwise one would retain degree four in the
five-connected graph `G`.  Hence

```text
N_G(d)={u,v,w,a_1,a_2},
N_G(w)={u,v,d,c_1,c_2}.
```

Put

```text
P={u,v,a_1,a_2,c_1,c_2},            T={d,w}.
```

Then `T` is a `K_2` component of `G-P`.  For a component `K` of `G-P`,
put

```text
eta_P(K)=|E(G[K])|+|E_G(K,P)|-4|K|.
```

The low kernel has `eta_P(T)=1`, the other components have total order
`a-1`, and exact edge accounting gives

\[
 \sum_{K\ne T}\eta_P(K)=16-|E(G[P])|.                \tag{3.1}
\]

## 4. A nontrivial four-separation

Assume instead that `J=H/dz` is four-connected, and write `x` for the
contracted vertex.  Lemma 2.1 and the density of `H` give

```text
|E(J)|>=4|V(J)|-7.
```

If `J` were five-connected, it would be a smaller target-free `E5` enemy,
contrary to the choice of `G`.  Thus `J` is exactly four-connected.  Let
`X` be any four-cut of `J` whose complementary
components can be partitioned into open sides `A_0,B_0` with

```text
|A_0|,|B_0|>=2.
```

The vertex `x` lies in `X`; otherwise `X` lifts to a four-cut of `H`
avoiding `z`.  Put

```text
U=X-{x},
Y=U union {d,z}.
```

The set `Y` is a five-cut of `H` with the same open sides.  Every vertex
of `Y` has a neighbour in both sides: if `s in Y` missed one side, then
`Y-{s}` would be either a four-cut avoiding `z` or a four-cut with a
nonsingleton side.  Both contradict the imported normal form.

The degree-four vertex `d` is adjacent to `z` and meets both sides, so

```text
d_{H[Y]}(d)<=2,                     |E(H[Y])|<=8.
```

Expanding `z=uv` gives

```text
R=U union {d,u,v},                  |R|=6.
```

The expansion adds `uv` and at most one edge for each of the at most three
common neighbours of `u,v`.  Therefore

\[
                         |E(G[R])|\le12.              \tag{4.1}
\]

Moreover `|V(G-R)|=a+1`, and each open side has order at most `a-1`.

### Theorem 4.1 (endpoint-missing equality cases)

Suppose one open side `F` is anticomplete to one of `u,v`, say `beta`.
Let `alpha` be the other endpoint and put

```text
Q=R-{beta}={d,alpha} union U.
```

Then `|F|=2`.  Exactly one of the following holds.

1. `F={f_1} dot-union {f_2}` consists of two singleton components with
   `N_G(f_1)=N_G(f_2)=Q`.
2. `F={f_1,f_2}` is an edge and both ends are complete to `Q`.

In the first case a six-cut exposes the labelled `P_3` kernel of Theorem
2.1 in the promoted finite screen; in the second it exposes the labelled
`K_3` kernel.

### Proof

The set `Q` is a five-cut and `F` is a union of components of `G-Q`.
The universal five-cut theorem supplies a component `C` of excess at least
four, and the minimum-order choice gives `|C|>=a`.  Since the open side
`F` has order at most `a-1`, this component is disjoint from `F`.  Only
`a+2` vertices lie outside `Q`, while `|F|>=2`.  Hence

```text
|F|=2,                              |C|=a,
```

with no other vertices outside `Q`.

If the vertices of `F` are distinct singleton components, boundary
fullness gives the first case.  Their excesses are one, so the high pair
has `(order,Phi,rho)=(a,11,2)`.

Otherwise `F` is an edge.  Put `delta=delta_Q(F)`.  The complement identity
gives

```text
Phi(Q,C)=13-delta.
```

The edge has at most ten contacts with the five-set `Q`, so `delta<=3`.
If `delta<=1`, this improves `Phi`; if `delta=2`, it ties `Phi=11` and
improves `rho`.  Both contradict the global selection.  Thus `delta=3`.
Since

```text
delta=1+|E_G(F,Q)|-8,
```

both ends of `F` are complete to all five vertices of `Q`.

In either case `d` sees `u,v,f_1,f_2`.  It must also meet the opposite open
side, and `d_G(d)=5`, so there is a unique `b in C` with

```text
N_G(d)={alpha,beta,f_1,f_2,b}.
```

In particular `d` misses all of `U`.  Put

```text
P={alpha,beta,b} union U,           T={d,f_1,f_2}.
```

Then

```text
N_P(d)={alpha,beta,b},
N_P(f_1)=N_P(f_2)={alpha} union U.
```

The first case makes `G[T]=P_3` and `eta_P(T)=1`; the second makes
`G[T]=K_3` and `eta_P(T)=2`.  There are no edges from `T` to the remaining
vertices.  This is exactly the labelled kernel assertion.  \(\square\)

Writing `W=V(G)-(P union T)`, the exact identities are

\[
 \sum_{K\in\mathcal C(G[W])}\eta_P(K)
 =\begin{cases}
 16-|E(G[P])|,&G[T]=P_3,\\
 15-|E(G[P])|,&G[T]=K_3.
 \end{cases}                                           \tag{4.2}
\]

## 5. Consequences of the finite screen

Call a component `K` of `G-P` **`P`-six-full** when `N_G(K)=P`; otherwise
it is `P`-non-six-full.  Five-connectivity gives `|N_G(K)|>=5`, so a
`P`-non-six-full component misses exactly one member of `P`.

### Corollary 5.1 (connected `P`-non-six-full shore)

In any of the `K_2`, `P_3`, or `K_3` kernel configurations above, suppose
the vertices opposite `T` form one connected component `K` and

```text
N_G(K)=P-{r}
```

for some `r in P`.  Then the configuration is impossible in the selected
minimum enemy.

### Proof

Contract `K` to the five-full representative `h`.  For the `K_2` and
`P_3` cases, the finite theorem gives a `K_7^-` minor when
`|E(G[P])|>=13`; otherwise (3.1) or (4.2) gives `eta_P(K)>=4`.  For the
`K_3` case, the finite theorem applies when `|E(G[P])|>=12`; otherwise
(4.2) again gives `eta_P(K)>=4`.

In the latter alternatives `P-{r}` is a five-cut and `K` has order
`a-1` in the `K_2` case or `a-2` in the other cases.  This is a strict
high-excess descent below the selected order `a`, a contradiction.
\(\square\)

If at least one opposite component is `P`-six-full, delete the other
opposite components and contract the chosen one.  The finite theorem then
leaves only

| low kernel | surviving boundary bound |
|---|---:|
| `K_2` | `|E(G[P])|<=12` |
| `P_3` | `|E(G[P])|<=10` |
| `K_3` | `|E(G[P])|<=9` |

There is then no five-cut obtained by deleting a missed root.

### Proposition 5.2 (`P`-non-six-full components in a split shore)

Suppose the vertices opposite `T` form several components, and let `K` be
one which misses a boundary root `r`.  Then `|K|<=2`.  If `|K|=1`, it is
a degree-five singleton complete to `P-{r}`.  If `|K|=2`, it is an edge
and both ends are complete to `P-{r}`.

### Proof

The set `P-{r}` is a five-cut.  The component `K` remains separate after
its deletion, while the at least three vertices of `T union {r}` lie
outside `K`.  Thus `K` cannot itself have order at least `a`.  The
universal high-excess theorem supplies a different component of order at
least `a`; since only `a+2` vertices lie outside the cut, `|K|<=2`.

A singleton component has exactly the five neighbours `P-{r}` by boundary
fullness.  If `|K|=2`, connectedness makes it an edge.  The high-excess
component then has order exactly `a`, and the complement identity and the
same `(a,Phi,rho)` comparison used in Theorem 4.1 force
`delta_{P-{r}}(K)=3`.  Hence both endpoints are complete to all five
vertices of `P-{r}`.  \(\square\)

Only the `P`-non-six-full components have thereby acquired bounded labelled
structure.  Their number and missed-root assignments are not bounded by
this proposition, and one or more `P`-six-full components may still be
arbitrarily large.

## 6. Exact residual alternatives

The results above do not make the three kernels exhaustive.  Starting from
the imported endpoint and the returned singleton `d`, the proved alternatives
are as follows.

1. If `H/dz` is not four-connected, Section 3 gives the `K_2` kernel.
2. If `H/dz` has an eligible nontrivial four-separation with a side missing
   `u` or `v`, Section 4 gives the `P_3` or `K_3` kernel.
3. If the opposite shore of a kernel is connected and misses one root,
   Corollary 5.1 eliminates it.  In a split shore, Proposition 5.2 bounds
   each `P`-non-six-full component but not their number or the
   `P`-six-full components.

Three branches remain open.

- **Self-similar quotient.** The graph `H/dz` may be exactly four-connected with
  every four-cut again having one singleton side and one connected
  remainder.  Iteration is not justified: enlarging the contracted anchor
  need not preserve the original `uv` labels, degree-five status,
  or the selected `(a,Phi,rho)` data.
- **Both-endpoints separations.** If no endpoint-missing kernel exists,
  every eligible nontrivial four-separation has both `u` and `v` meeting
  both open sides.  The endpoint-missing equality argument does not apply.
- **Remaining opposite shores.** A kernel may have a `P`-six-full component,
  or its opposite shore may split entirely into `P`-non-six-full
  components.  Proposition 5.2 bounds each `P`-non-six-full component but
  not their number or missed-root incidence pattern.  Any `P`-six-full
  component may remain arbitrarily large; the finite screen bounds the
  boundary but does not localise excess inside that component.

The proposed six-boundary kernel-localisation lemma remains a conjectural
target.  The density-free
[triangle-contact barrier](../barriers/hc7_e5_triangle_lift_contact_barrier.md),
the five-connected
[complement-of-`P_8` barrier](../barriers/hc7_e5_six_full_local_structure_barrier.md),
and the earlier
[six-boundary quotient barrier](../barriers/hc7_e5_six_boundary_quotient_barrier.md)
show why the remaining proof must retain exact host density rather than use
the contracted incidence pattern alone.
