# Internal audit: localisation at an order-six cut

**Verdict:** GREEN.

**Audited source:**
`results/hc7_k7minus_exact_six_cut_localisation.md`

**Source SHA-256:**
`f2a4480d27556996620117a68a8a7924dd61cf37bf5ec9e8cce4c953dfcc88af`

This is a separate internal mathematical audit, not external peer review.
The proof is computation-free.

## External inputs

The two quoted inputs have the forms used in the proof:

- Norin--Totschnig Lemma 9 bounds an internally four-connected pair
  `(F,Q)`, with four roots and no `Q`-rooted `K_4` model, by
  `|E(F)|<=3|V(F)|-7`.
- Norin--Totschnig Lemma 10, quoting Jorgensen, gives a `Q`-rooted
  `K_4^-` model when `(F,Q)` is internally four-connected and
  `|V(F)|>=6`.

These are the only external mathematical inputs.

## 1. Fullness and the number of components

For a component `C_i` of `H-S`, its neighbourhood is contained in the
six-set `S`.  If it were a proper subset of `S`, deleting that
neighbourhood would separate `C_i` from another component of `H-S` with
fewer than six vertices.  Six-connectivity therefore gives
`N_H(C_i)=S`.

For `k` selected full components, the proof absorbs `k-1` distinct
boundary vertices into distinct components, keeps one component bare, and
keeps the other `7-k` boundary vertices singleton.  This gives exactly
seven pairwise disjoint connected branch sets.  Every adjacency involving
a component-derived bag is supplied by fullness, so missing adjacencies
can occur only among the boundary singleton bags.  Consequently:

- five components immediately give a `K_7^-` model;
- four components force every boundary triple to span at most one edge,
  and hence force `H[S]` to be a matching;
- three components force every boundary four-set to span at most four
  edges; and
- two components force every boundary five-set to span at most eight
  edges.

The exclusion of four components is valid.  If a component `C` is
non-singleton and `Q` is a four-subset of `S`, a prohibited rooted
separation of `(H[C union Q],Q)` of order at most three, together with
`S-Q`, would give a cut of `H` of order at most five.  Another component
survives on the opposite side.  The rooted pair is therefore internally
four-connected and has at least six vertices, so Lemma 10 supplies a
rooted diamond.  Pairing the two unused boundary vertices with two of the
three other components and keeping the last component bare supplies the
remaining three mutually adjacent bags.  This is a valid `K_7^-` model.

Thus all four components would have to be singletons.  Every boundary
vertex would then have four exterior neighbours and, because the boundary
is a matching, at most one boundary neighbour.  This contradicts the
minimum degree at least six implied by six-connectivity.  Hence
`r` is two or three.

## 2. Initial boundary bounds

The boundary double counts are exact.  Each edge of a six-set lies in four
of its six five-subsets and in six of its fifteen four-subsets.  The
five-set and four-set bounds above therefore give respectively

```text
|E(H[S])| <= 12,             r=2,
|E(H[S])| <= 10,             r=3.
```

In the three-component case, if a component is non-singleton and a
boundary vertex `z` has four boundary neighbours `Q`, the same separator
lift and Lemma 10 give a `Q`-rooted diamond.  The other two components,
the remaining boundary vertex, and `{z}` form the three additional bags
displayed in the source.  Fullness supplies all component-bag adjacencies,
and the four literal `z-Q` edges supply all adjacencies from `{z}` to the
rooted bags.  Only the diamond's one possible missing adjacency remains.
Thus `Delta(H[S])<=3` under the stated non-singleton hypothesis.

## 3. Exact excess identity

The edge partition is

```text
|E(H)| = |E(H[S])|
         + sum_i (4|C_i| + delta_i),
|V(H)| = 6 + sum_i |C_i|.
```

Subtracting `4|V(H)|-2` gives exactly

```text
q_H = |E(H[S])| + sum_i delta_i - 22.
```

No minimum-degree estimate is used in this identity or in either
sharpening below.

## 4. Excluding twelve boundary edges with two components

If the boundary has twelve edges, every five-set has at most eight edges,
so `12-d_{H[S]}(s)<=8` for every `s`.  The boundary degree sum is exactly
twenty-four; hence every boundary degree is four and
`H[S]` is `K_6` minus a perfect matching.  This valid double-counting step
replaces the unsupported boundary-degree inference in the earlier draft.

For a matching nonedge `pq`, the other four boundary vertices induce a
four-cycle.  The rooted pair on any component `C` and those four vertices
is internally four-connected by the separator lift.  It has no rooted
`K_4` model: such a model, the other full component, and singleton bags
`{p}` and `{q}` would give a `K_7^-` model whose only possible missing
adjacency is `pq`.

Writing the component parameters as in the source, Lemma 9 gives

```text
p(p)+p(q) >= c+delta-1.
```

The three matching nonedges partition `S`, so their sum gives
`P>=3c+3delta-3`.  Connectedness gives `e_C>=c-1`, and therefore
`P=4c+delta-e_C<=3c+delta+1`.  Hence `delta<=2` for each component.
The resulting total at most four contradicts the exact requirement
`delta_1+delta_2=q_H+10>=10`.  Thus the sharpened bound
`|E(H[S])|<=11` is proved.

## 5. Excluding nine boundary edges with three components

If all three components were singletons, the graph would have nine
vertices and at most `18+10=28` edges, below `4(9)-2=34`.  Hence a
component is non-singleton, the preceding rooted-diamond argument gives
maximum boundary degree at most three, and a nine-edge boundary must be
cubic.

For every ordered boundary nonedge `(q,p)`, a rooted `K_4` model on a
component and `S-{q,p}` would combine with the other two full components,
`p`, and `q` as in the source.  Because `q` has three boundary neighbours
and `p` is one of its two boundary nonneighbours, `{q}` misses at most one
of the four rooted bags.  The proposed seven bags would therefore form a
`K_7^-` model.  The rooted model is absent, so Lemma 9 applies.

There are twelve ordered nonedges in a cubic graph on six vertices.  In
the sum of the rooted inequalities:

- `e_C` has coefficient twelve;
- every attachment count has coefficient eight, because its boundary
  vertex occurs in four ordered nonedges; and
- every boundary edge occurs in four complementary four-root sets.

The last coefficient is exact: after removing the ends of a fixed
boundary edge, the remaining four vertices induce four edges in any cubic
six-vertex graph, and hence contain four ordered nonedges.  The summed
inequality is therefore

```text
3e_C + 2P <= 9c+6.
```

Together with `e_C>=c-1`, this gives `2delta<=7`, and hence the integral
bound `delta<=3`.  All three components have total excess at most nine,
contradicting the exact requirement `sum_i delta_i=q_H+13>=13`.
Therefore the boundary has at most eight edges.

## Scope

The theorem proves only the stated localisation.  It does not eliminate
the residual two-component or three-component excess cases and does not
prove the seven-connected `4n-2` theorem.  The scope paragraph records
this limitation accurately.  No mathematical repair is required for the
pinned source revision.
