# Rooted-`K_4` transfer to the other lobes

**Status:** written unbounded proof, pending separate audit.  A
four-rooted `K_4` in one lobe lowers the common-four-neighbour capacity of
each other lobe from two to one.  This is a valid singleton-carrier
composition; it does not assert that two arbitrary four-root carriers can
be anchored at two omitted roots.

Let `G` be a six-connected graph with no `K_7^-` minor, let `S` be a
six-vertex cut, and suppose that `G-S` has exactly three components.  Every
component is `S`-full.  For a component `A` and a four-set `Z subseteq S`,
put

```text
n_A(Z)=|{v in A: Z subseteq N_G(v)}|.
```

## Theorem 1 (a rooted model transfers a capacity-one constraint)

Let `C,A,D` be the three components of `G-S`, let `Z subseteq S` have
order four, and write `S-Z={p,q}`.  If the closed shore
`G[C union Z]` contains a `Z`-rooted `K_4` model, then

```text
n_A(Z)<=1,   n_D(Z)<=1.                               (1)
```

### Proof

By symmetry it suffices to prove the first inequality.  Suppose that two
distinct vertices `x,y in A` are adjacent to every vertex of `Z`.

Consider

```text
H=G[A union {p,q}].
```

There are two vertex-disjoint paths in `H` joining the two-set `{p,q}`
to the two-set `{x,y}`.  Indeed, otherwise the set version of Menger's
theorem gives a vertex `w` such that `H-w` has no path from
`{p,q}-{w}` to `{x,y}-{w}`.  Both displayed differences are nonempty.
Let `K` be a component of `H-w` meeting `{x,y}-{w}`.  It does not meet
`{p,q}-{w}`, so `K subseteq A`.  Because distinct components of `G-S`
have no edge between them,

```text
N_G(K) subseteq Z union {w}.
```

The other two components of `G-S` lie outside `K union Z union {w}`.
Thus `Z union {w}` is a cut of order at most five, contrary to
six-connectivity.  The two paths exist.

Since both terminal sets have order two, the paths use distinct endpoints
in each.  Relabel them as a `p-x` path `P_x` and a `q-y` path `P_y`.
They are disjoint connected bags.  Take a shortest path in `G[A]` between
their nonempty intersections with `A`; its internal vertices avoid both
bags.  Absorb those internal vertices into `P_x`.  The two bags remain
disjoint and connected and are now adjacent.  They are both adjacent to
every root in `Z`, through `x` and `y`, respectively.

Let `R_z`, `z in Z`, be the four bags of the rooted `K_4` model in the
closed `C`-shore.  The seven bags

```text
(R_z:z in Z),   P_x,   P_y,   D
```

are pairwise adjacent.  The four rooted bags form a clique.  Each of
`P_x,P_y,D` meets every rooted bag through the literal root it contains.
The first two are adjacent by the connector just chosen.  Finally, `D`
is adjacent to `P_x` through its neighbour at `p` and to `P_y` through
its neighbour at `q`.  These bags form a `K_7` model, a contradiction.
This proves `n_A(Z)<=1`; the proof for `D` is identical.  \(\square\)

## Corollary 2 (joint rooted-status incidence bound)

For a component `X`, let `R_X` be the family of four-sets `Z subseteq S`
for which `G[X union Z]` contains a `Z`-rooted `K_4` model.  Fix a
component `A`, and let `C,D` be the other two.  Then

```text
sum_{v in A} binom(|N_G(v) cap S|,4)
    <= 30-|R_C union R_D|.                            (2)
```

If `U subseteq S` is a three-set spanning at least two boundary edges,
put

```text
Q(U)={U union {r}: r in S-U}.
```

Then the sharper joint bound

```text
sum_{v in A} binom(|N_G(v) cap S|,4)
    <= 30-|R_C union R_D union Q(U)|                 (3)
```

holds.

### Proof

For every four-set `Z`, the audited four-root carrier theorem gives
`n_A(Z)<=2`: three such vertices would be three disjoint singleton
`Z`-carriers.  Theorem 1 improves this to one whenever
`Z in R_C union R_D`.  If `Z in Q(U)`, Lemma 3 of the same carrier theorem
also gives `n_A(Z)=1`.  Sum these bounds over the fifteen four-sets and
reverse the order of counting.  Each vertex `v` is counted once for every
four-subset of `N_G(v) cap S`, namely
`binom(|N_G(v) cap S|,4)` times.  This proves (2) and (3).  \(\square\)

## Corollary 3 (root-rich lobes shrink opposite trees)

Let `M_A` denote the right side of (2), or the right side of (3) when a
two-edge boundary triple is fixed.  If `beta(A)` is the cyclomatic number
of `G[A]`, then

```text
|A| <= M_A+2 floor(M_A/5)+2 beta(A)-2               (4)
```

whenever `|A|>=2`.  In particular, if either other lobe is rooted for all
fifteen four-sets, then every tree lobe `A` has order at most nineteen.

### Proof

Put `a(v)=|N_G(v) cap S|`.  Internal degree one implies `a(v)>=5`, and
internal degree two implies `a(v)>=4`, because `delta(G)>=6`.  The
incidence sum bounded by `M_A` therefore gives at most
`floor(M_A/5)` internal leaves and at most `M_A` internal degree-two
vertices.  If `h` vertices have internal degree at least three, the
connected-graph degree identity gives

```text
h <= 2 beta(A)-2+n_1.
```

Adding the three degree classes yields (4).  When all fifteen four-sets
are rooted in another lobe, `M_A<=15`; substituting `beta(A)=0` gives
`|A|<=15+2*3-2=19`.  \(\square\)

## Scope

The theorem converts rooted-pair status in one or two lobes into a joint
quantitative restriction on the third.  Its Menger argument depends
essentially on the two carriers being single vertices.  For arbitrary
connected carriers a contracted carrier can itself be a multi-vertex
linkage obstruction, so no omitted-root assignment is claimed here.

## Dependency

The general capacity-two and boundary-triple capacity-one inputs are in
the [four-root carrier-packing theorem](hc7_k7minus_sparse_sixcut_four_root_carrier_packing.md),
source SHA-256
`adfcc70aca8543e15bcf7e94e1fb310492535f8155f02cb5a5430adba4ce8372`,
with adjacent GREEN cold-audit SHA-256
`4a185697d20ed73c358703eb7d433c3555bca6474497a011630d3805dc493e97`.
