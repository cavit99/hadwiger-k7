# Internal audit: contraction of the singleton triangle

**Verdict:** GREEN for the pinned source revision.  This is a separate
internal mathematical audit, not external peer review.

**Audited source:**
`active/hc7_k7minus_e5_s3_triangle_contraction_reduction.md`

**SHA-256:**
`52e321c3c46a267663de3584d1a628f8a3c9044369071328f619df704129d242`

No mathematical correction is required at this revision.

Relative to the previously audited revision
`dc5de399b6f497af08c49eca461337ed65b150db7818e34b9359d45ef56247f1`,
the source changes only its status from pending audit to a link to this
audit.  Its theorem statement, proof, dependencies and scope are unchanged.

## 1. Exact singleton endpoint

Only the singleton endpoint of the preceding three-separator reduction is
used.  Its two singleton cuts give the exact neighbourhoods

```text
N_G(p)=T union {t,q},
N_G(q)={p,t,b} union R_0,
N_G(t)={p,q,x,y,u_t},
```

where `|T|=3`, `|R_0|=2`, and `p,t,q` are distinct and pairwise adjacent.
The adhesion `T` lies in `F=G-{x,y,t,q}`, so neither twin belongs to it.
No conclusion from the disputed excess-two edge-atom branch is used.

If `T={b} union R_0`, the connected edge `{p,q}` has open neighbourhood
exactly `{t} union T`, of order four.  The twins survive its deletion and
lie outside this edge, so this is a genuine cut contradicting
five-connectivity.  Lemma 1 is therefore valid.

## 2. Exact contraction loss

The triangle has exactly three internal edges.  Its exterior incidences
are exactly

```text
p--T:                  3,
t--{x,y,u_t}:          3,
q--({b} union R_0):    3.
```

Thus there are nine exterior incidences.  The two three-sets `T` and
`{b} union R_0` are unequal by Lemma 1, so their union has order at least
four.  The twins `x,y` are distinct from that union and from one another.
The exterior neighbourhood of the triangle consequently has order at
least six; the possible location of `u_t` can only increase this order,
not decrease the bound.

Contracting a triangle with nine exterior incidences and exterior
neighbourhood of order `d` removes exactly

```text
3+(9-d)
```

edges: the first term is the three internal edges and the second is the
number of duplicate exterior incidences suppressed.  Since `d>=6`, at
most six edges are lost.  No further edge is affected by the contraction.
With two vertices removed, this gives exactly the asserted lower bound

```text
|E(J)|>=4|V(G)|-13=4|V(J)|-5.
```

## 3. Exclusion of a three-cut

A cut of `J` of order at most two which avoids the contracted vertex `z`
lifts unchanged to `G`.  One containing `z` lifts by replacing it with
`p,t,q`, increasing its order by two and producing a cut of `G` of order
at most four.  Hence `J` is three-connected.

Suppose that `J` has a three-cut.  It must contain `z`; lifting it gives
the exact five-cut

```text
Q={p,t,q} union R',                  |R'|=2.
```

Every component behind `Q` is full to `t`.  The complete case split for
the possible surviving vertices of `{x,y,u_t}` is sound:

1. If both twins survive, at least two roots of `S` survive the cut, and
   either such root gives an `x`--`y` path.  All surviving members of
   `{x,y,u_t}` therefore lie in this component.
2. If exactly one twin survives, it is adjacent to every surviving root.
   In particular it joins `u_t` whenever `u_t` also survives.
3. If neither twin survives, then `R'={x,y}`.  The root `u_t` survives
   and is the sole possible neighbour of `t` outside the cut.

At least one of the three vertices survives in every case.  Hence all
neighbours of `t` outside `Q` lie in one component.  Fullness to `t`
would require every component behind `Q` to contain one of these
neighbours, so the cut could have only one component.  This contradiction
excludes every three-cut and proves that `J` is four-connected.

## 4. Four-cut and lifted six-separation

The quotient is a proper target-free minor and its density is above the
`E5` threshold.  If it were five-connected, it would be a smaller `E5`
enemy, contrary to the minimum order of `G`.  Thus it has a four-cut.
Every four-cut contains `z`, since an avoiding one would lift unchanged to
a four-cut of `G`.  Writing it as `{z} union R`, with `|R|=3`, and
uncontracting `z` gives the genuine order-six cut

```text
{p,t,q} union R
```

of `G`.  No assertion that this lifted cut is a minimum cut is made.

Because `J` is four-connected, every component behind its four-cut is
adjacent to all four cut vertices.  Under the lift this says exactly that
every component meets every vertex of `R` and has a neighbour in the
triangle in aggregate.  It does not imply adjacency to all three triangle
vertices, in agreement with the stated scope.

## 5. Published near-clique input and scope

Norin--Totschnig, Theorem 6, applies to a four-connected graph with at
least `4|V|-8` edges, apart from `K_{2,2,2,2}`.  Here the stronger bound
`4|V(J)|-5` applies.  The exceptional graph has exactly `4|V|-8` edges,
so it cannot be `J`.  The conclusion `K_7^vee` is a minor of `J` is
therefore valid.

The source correctly does not promote this unlabelled near-clique model
to `K_7^-`.  The theorem does not control whether `z` occurs in the
deficient bag or how a bag containing `z` splits over `p,t,q`.  Likewise,
the lifted six-separation records only aggregate triangle contact.  A
labelled model-or-separation theorem remains unresolved.

The local source revisions consulted were:

```text
singleton endpoint source:
63e9087752b66a0334d28ea555e40dbde9a7f4dad60d016c04329470e89e9a3a

atomic six-boundary reduction:
3f2084f172183f38b91aa5a9ef402d2c60095579dda915fa6fcadaabfe94edff

singleton-contraction theorem:
e4720b2641033396aabf333cc97d9f401df4577f8a6f337a44d7ca6aba0ac1c2
```

The audit uses only the exact singleton endpoint from the first source.
Relative to the revision originally consulted, that source changed only
its status to link its final audit; the singleton endpoint is unchanged.
The materially revised edge-atom elimination beyond that endpoint is not
assumed.  The result does not eliminate the singleton atom, prove `(E5)`,
or prove the primary seven-connected theorem.
