# The six-connected `4n-6` entrance

**Status:** written reduction.  It does not prove the extremal statement
below.  The only new external input is Lo's 2026 `K_6^-` theorem, used in
Theorem 3 and Corollary 6.

Write `K_7^-` for `K_7` with one edge deleted.  Consider the candidate

> every six-connected graph `G` with
> `|E(G)|>=4|V(G)|-6` contains a `K_7^-` minor.                 (E6)

The reduction below puts any minimum enemy into the unresolved rows of the
existing degree-six cut programme and excludes the whole universal-vertex
family.

## Theorem 1 (first order and degree)

Suppose `(E6)` is false.  Choose an enemy `G` first with minimum order and,
subject to that, with minimum size.  Put

```text
n=|V(G)|,       m=|E(G)|,       q=m-(4n-6).
```

Then:

1. `n>=13`; if `n=13`, then `m=46`;
2. if `q>0`, then `G` has a vertex of degree six; and
3. if `q=0`, then `G` has a vertex of degree six or seven.

### Proof

For `n<=12`, one has

```text
4n-6 >= (9/2)n-12.
```

Jakobsen's theorem therefore gives a `K_7^-` minor or a
`(K_{2,2,2,2},K_6,4)`-cockade.  A nontrivial such cockade has a four-cut,
whereas `G` is six-connected.  The two base graphs do not meet the density
hypothesis: `K_6` has fifteen rather than eighteen edges, and
`K_{2,2,2,2}` has twenty-four rather than twenty-six.  Hence `n>=13`.
At `n=13`, Jakobsen's strict inequality for a target-free non-cockade gives
`m<93/2`, whilst `(E6)` gives `m>=46`; hence `m=46`.

Suppose `q>0`.  If `G-e` were six-connected for some edge `e`, then it
would still have at least `4n-6` edges and would be a smaller enemy.  Thus
`G` is minimally six-connected.  Halin's theorem gives a vertex of degree
six.  Finally, when `q=0`,

```text
2m/n=8-12/n<8.
```

Six-connectivity gives minimum degree at least six, so a minimum-degree
vertex has degree six or seven.  \(\square\)

## Theorem 2 (exact degree-six residue)

Let `x` be a degree-six vertex in an enemy, and put `T=N_G(x)`.  Write the
components of `G-T` other than `{x}` as `C_1,...,C_s`, and set

```text
delta_i = |E(G[C_i])|+|E_G(C_i,T)|-4|C_i|.
```

Then:

```text
s in {1,2},
N_G(C_i)=T for every i,
|E(G[T])| + sum_i delta_i = 16+q.                    (2.1)
```

If `s=2`, then either

```text
|E(G[T])|<=6,
```

or `|E(G[T])|=7` and `G[T]` is one of the four subcubic graphs with degree
sequence `3,3,2,2,2,2`.  If `s=1`, then

```text
|E(G[T])|<=12,
delta_1=16+q-|E(G[T])| >=4+q.                        (2.2)
```

### Proof

The existing degree-six cut-capacity theorem gives `s in {1,2}`, fullness
to `T`, and the boundary bounds.  Its exact excess identity is

```text
m=4n-22+|E(G[T])|+sum_i delta_i,
```

which is (2.1).

Suppose `s=2`.  Since `n>=13`, at least one of the two lobes is
nonsingleton, so the boundary is subcubic and has at most nine edges.  The
cubic nine-edge row and every eight-edge row force `m<=4n-7`.  The same is
true of a seven-edge boundary with three cubic vertices.  These conclusions
contradict the enemy density.  The only seven-edge degree sequence left by
subcubicity is `3,3,2,2,2,2`, with the four boundary graphs already isolated
in the degree-six cut programme.  This proves the first assertion.  The
one-lobe assertion is the two-component boundary bound together with
(2.1).  \(\square\)

## Theorem 3 (nonplanar deletion and root collision)

Retain the hypotheses and notation of Theorem 2, and put `P=G-x`.  Then:

1. `P` is five-connected, has minimum degree at least five, and is
   nonplanar;
2. `P` contains both a `K_6^-` minor and a `K_{3,4}` minor; and
3. in every `K_6^-` model in `P`, some branch bag is disjoint from `T`.
   In a spanning model, some other branch bag contains at least two
   vertices of `T`.  The rootless bag lies wholly in one component of
   `G-(T union {x})`.

### Proof

Deleting one vertex from a six-connected graph leaves a five-connected
graph and lowers every remaining degree by at most one.  Moreover, with
`p=|V(P)|=n-1`,

```text
|E(P)|=m-6 >=4n-12=4p-8>3p-6.
```

Thus `P` is nonplanar.  Lo's theorem says that every four-connected
nonplanar graph of minimum degree at least five contains `K_6^-` and,
unless it is `K_6`, also `K_{3,4}`.  Here `p>=12`, so both conclusions
apply.

If every bag of a `K_6^-` model met `T`, then the singleton `{x}` would be
adjacent to all six bags.  Together they would form a `K_7^-` model in
`G`, a contradiction.  Hence one bag misses `T`.  A model in a connected
graph may be made spanning.  The six vertices of `T` then occupy at most
five bags, so another bag contains at least two of them.  Finally, a
connected bag disjoint from `T` cannot meet two components of
`G-(T union {x})`.  \(\square\)

## Theorem 4 (low-codegree descent and an exact six-cut)

Retain the minimum-enemy hypotheses of Theorem 1.  Then some edge `uv` of
`G` satisfies

```text
|N_G(u) intersect N_G(v)|<=3.                         (4.1)
```

The contraction `G/uv` is five-connected and target-free, and

```text
|E(G/uv)|>=4|V(G/uv)|-6+q.                            (4.2)
```

It is not six-connected.  If `w` is the contracted vertex, some five-cut
`X` of `G/uv` contains `w`, and

```text
(X-{w}) union {u,v}
```

is an exact six-cut of `G`.

### Proof

Choose the low-degree vertex supplied by Theorem 1, and suppose that every
edge of `G` has at least four common neighbours.  If the chosen vertex has
degree six, the established degree-six disk bound gives

```text
|E(G)|<=4|V(G)|-9,
```

contrary to the enemy density.  The only other possibility is a degree-seven
vertex in the exact row `q=0`.  The saturated degree-seven exclusion theorem
also rules this out.  Thus the supposition was false, and (4.1) holds.

Contracting `uv` removes its edge and one duplicate for each common
neighbour, which proves (4.2).  Edge contraction lowers vertex connectivity
by at most one, so the contraction is five-connected.  It remains
target-free because it is a minor of `G`.

If `G/uv` were six-connected, (4.2) would make it a smaller enemy.  Thus
its connectivity is exactly five.  Let `X` be a five-cut.  Necessarily
`w in X`: otherwise splitting `w` back into the adjacent vertices `u,v`
inside its component would show that `X` is a five-cut of `G`.  Replacing
`w` by `u,v` therefore lifts `X` to the displayed six-cut.  \(\square\)

## Corollary 5 (the returned six-cut)

Let `S` be the lifted six-cut from Theorem 4, and let `D_1,...,D_r` be the
components of `G-S`.  Put

```text
eta_i=|E(G[D_i])|+|E_G(D_i,S)|-4|D_i|.
```

Then every `D_i` is full to `S`, and

```text
r in {2,3},
|E(G[S])|+sum_i eta_i=18+q.                           (5.1)
```

If `r=2`, then `|E(G[S])|<=12`.  If `r=3`, then
`Delta(G[S])<=3` and `|E(G[S])|<=9`.

Suppose `r=2`, `S=Z dot_union {a,b}`, and `G[Z]=K_4`.  With
`epsilon=1` when `ab` is an edge and zero otherwise,

```text
d_G(a)+d_G(b)>=12+q+epsilon.                          (5.2)
```

In particular, if `{a,b}={u,v}` for the low-codegree edge in Theorem 4,
then its two ends cannot both have degree six.

### Proof

The exact six-cut localisation theorem gives fullness, the component count
and the boundary bounds.  In the three-component case at least one
component is nonsingleton, since `n>=13`; hence the boundary is subcubic.
Equation (5.1) is direct edge accounting.

For the last assertion, write `S=Z dot_union {a,b}` and put

```text
t=|E_G({a,b},Z)|.
```

The six-cut `K_4`-reserve inequality, summed over the two shores, gives

```text
eta_1+eta_2 <= |E_G(D_1 union D_2,{a,b})|.
```

Since `|E(G[S])|=6+t+epsilon`, (5.1) turns the left side into
`12+q-t-epsilon`.  The right side is
`d_G(a)+d_G(b)-t-2epsilon`, proving (5.2).  For the edge `uv`, one has
`epsilon=1`, so two degree-six ends would give `12>=13+q`, impossible.
\(\square\)

## Corollary 6 (universal vertices are impossible)

Every six-connected graph `H` with a universal vertex and
`|E(H)|>=4|V(H)|-6` contains a `K_7^-` minor.

### Proof

Let `u` be universal and put `R=H-u`, `r=|V(R)|`.  The graph `R` is
five-connected, has minimum degree at least five, and

```text
|E(R)|=|E(H)|-r >=3r-2.
```

It is therefore nonplanar.  Lo's theorem gives a `K_6^-` model in `R`;
adjoining the universal singleton `{u}` gives a `K_7^-` model in `H`.
\(\square\)

## Exact remaining gate

The broad candidate has survived the standard complete-multipartite,
extended-wheel, icosahedral-cone and sharp-cockade falsification screens;
Corollary 6 disposes of universal vertices altogether.  The proof
obligation exposed by the reduction is exact rather than a generic density
claim:

- close the one-lobe row (2.2);
- close the four seven-edge two-lobe boundaries and the boundaries with at
  most six edges; or
- turn the universal low-codegree contraction from Theorem 4 and its
  returned exact five-cut into a six-connected descent, or compose directly
  across the lifted six-cut.

Theorem 3 supplies an additional global object in every degree-six row: a
spanning near-clique model with a rootless lobe bag and a bag containing at
least two boundary roots.  What remains is a root-exchange theorem forcing
those six roots into distinct bags, or a direct composition from the forced
collision.

## External sources

- I. T. Jakobsen, *On a certain homomorphism properties of graphs II*,
  Math. Scand. **52** (1983), 229--261, Theorem 4.
- R. Halin, *A theorem on n-connected graphs*, J. Combin. Theory **7**
  (1969), 150--154.
- O.-H. S. Lo, *A characterization of graphs with no `K_{3,4}` minor*,
  arXiv:2603.27973 (2026), Theorem 1.3,
  <https://arxiv.org/abs/2603.27973>.
- [Degree-six cut capacity and exact excess](../active/hc7_k7minus_degree6_cut_capacity_excess.md).
- [Degree-six common-neighbour bound](../active/hc7_k7minus_degree6_common_neighbour_bound.md).
- [Saturated degree-seven exclusion](../active/hc7_k7minus_degree7_common_neighbour_exclusion.md).
- [`K_4`-reserve inequality at a six-cut](hc7_k7minus_six_cut_k4_reserve_inequality.md).
- [Exact six-cut localisation](hc7_k7minus_exact_six_cut_localisation.md).
