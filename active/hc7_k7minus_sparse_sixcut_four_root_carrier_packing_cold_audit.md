# Independent cold audit: four-root carrier packing

**Verdict:** **GREEN** at the frozen source revision

```text
adfcc70aca8543e15bcf7e94e1fb310492535f8155f02cb5a5430adba4ce8372
  active/hc7_k7minus_sparse_sixcut_four_root_carrier_packing.md
```

The current source SHA-256 is
`2d71dcc2110efe7aea44889e8671b0e9289d0ce3b25e95407f35574c37b12a42`.
The only post-audit change marks the source as independently audited; the
mathematical statement and proof are unchanged.

This is an independent internal mathematical audit, not external peer
review.  The source was not edited during the audit.

## 1. Fullness and carrier enlargement

Every component of `G-S` is `S`-full: a missed boundary vertex would make
its full neighbourhood a cut of order at most five, contrary to
six-connectivity.

In Lemma 1, take the path from the chosen neighbour `z` of the omitted root
to its first vertex in the union of the selected carriers.  Minimality
makes every earlier path vertex disjoint from every carrier.  Absorbing
those earlier vertices into the carrier containing the last vertex
therefore preserves pairwise disjointness, connectedness and all old root
contacts, while adding the contact at `x`.  The argument also covers the
zero-length case when `z` is already selected.

## 2. The five-bag models

For Lemma 2 the five sets

```text
{x} union Q_0, {t_1} union Q_1, {t_2} union Q_2,
{t_3}, {t_4}
```

are disjoint because the carriers lie in `C` and the five boundary roots
are distinct.  The first three are connected by the nominated root
contacts.  Every carrier-derived bag meets each untouched root singleton.
Two carrier-derived bags meet because a root placed in either bag has a
neighbour in the other bag's `T`-carrier; for example `t_1` meets `Q_0`.
Thus only `t_3t_4` may be absent, and the sets form the asserted rooted
`K_5^-` model.

The same check in Lemma 3 is exact.  The two carrier bags are adjacent
through the `r-Q_0` contact, both meet all three singleton roots in `U`,
and at least two of the three singleton pairs are literal boundary edges.
Again there is at most one missing bag adjacency.

## 3. Completion by the other components

Since `G-S` has at least three components, two distinct components `A,D`
remain after fixing `C`.  If `y` is the sole unused boundary root, then
`A union {y}` is connected and is adjacent to `D` through a `y-D` edge.
Both new bags meet every one of the five rooted bags through the literal
boundary root in that bag.  They are disjoint from one another and from
the closed `C`-shore.  Consequently the only possible nonedge among all
seven bags is the one already permitted in the rooted `K_5^-`; this is a
valid `K_7^-` model.  No adjacency between different open components is
assumed.

This completion agrees with the independently audited five-root terminal
at source SHA-256
`32c45ee41ee349e2499c82c49bd7a0af7cfd636620bbc7873edea4ca061e1100`
and audit SHA-256
`b89582b3c4c4dfe0c03980c45c93b7fcad250241e6ef356273fd9f3fa2db7a89`.

## 4. Incidence arithmetic

For each of the `binom(6,4)=15` four-sets `T`, three vertices containing
`T` in their boundary neighbourhoods would be three disjoint singleton
`T`-carriers.  Lemma 2 therefore bounds their number by two.  Reversing
the double count gives

```text
sum_v binom(a(v),4) <= 15*2 = 30.
```

If `U` spans two boundary edges, the three sets `U union {r}`, with
`r in S-U`, have bound one by Lemma 3.  The other twelve retain bound two,
so the exact total is

```text
3*1 + 12*2 = 27.
```

A vertex with boundary degree at least four, five or six contributes at
least `1`, `5` or `15`, respectively.  Hence the numbers of such vertices
are at most

```text
floor(27/1)=27, floor(27/5)=5, floor(27/15)=1.
```

These are simultaneous consequences of one nonnegative sum; no separate
incidence families are conflated.  Finally, `Delta(G[S])>=2` really does
supply the required `U`: a vertex of degree two and two of its neighbours
span the two incident edges.

## 5. Scope

The theorem gives an unbounded target-sensitive packing bound and a
constant boundary-incidence core.  Vertices with at most three boundary
neighbours remain uncontrolled, so the coefficient-four excess need not
be bounded by this argument.  The source accurately leaves the
excess-five dichotomy and the remaining sparse boundaries open.  No
disjointness, contact, completion or counting defect was found.
