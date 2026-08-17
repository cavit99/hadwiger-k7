# Independent cold audit: common four-portal carrier completion

**Verdict:** **GREEN** at the frozen revisions below.  This audit was
conducted independently of the theorem and verifier author.  It is an
internal mathematical audit, not external peer review.

## Frozen artefacts

```text
49f2056d05c2c9550dbfdbc3429fc09ed55da0e5acbba2209ecc153b7b8a851f
  active/hc7_k7minus_returned_two_component_common_four_path_completion.md
55e0b6fd722d07738d3877ab9bc82e4a97e1a2c4163ca568522550e66265dbfb
  active/experiments/returned_two_component_common_four_path_verify.py
e7960a8c3738ac3cb3c1f621a221db21cf94c5e7f1fa0a1fe2cc7df9896a2c56
  active/experiments/returned_two_component_equality_witness_verify.py
```

## 1. The seven branch sets

Write the seven bags of Theorem 1 as

```text
W=A union {x,y,t_3}, X_1={t_1}, X_2={t_2},
X_4={t_4} union Q_0, Q_1,Q_2,Q_3.
```

They are disjoint: `A` and `B` are different components of `G-S`, all
four carriers lie disjointly in `B`, and the six displayed boundary
vertices are distinct.  The bag `W` is connected because each of
`x,y,t_3` has a neighbour in the connected full component `A`.  The bag
`X_4` is connected because `Q_0` has a neighbour at `t_4`; every other bag
is connected by definition.

Every required adjacency has an identified source.

- `W` sees `X_1,X_2,X_4` through fullness of `A`, and sees each of
  `Q_1,Q_2,Q_3` through `t_3`.
- `X_1X_2` is the literal edge `t_1t_2`.  The two edges from
  `X_4` to `X_1,X_2` are supplied by the contacts of `Q_0` at
  `t_1,t_2`.
- Each of `X_1,X_2,X_4` sees every `Q_i`, `1<=i<=3`, through the
  corresponding root `t_1,t_2,t_4` and the `T`-carrier property of
  `Q_i`.
- At least two of the three possible adjacencies among `Q_1,Q_2,Q_3`
  are hypotheses.

Thus twenty of the twenty-one bag pairs are guaranteed.  The construction
uses neither an edge between `A` and `B` nor an unproved edge of `G[S]`.
It is a valid `K_7^-` model for arbitrary carrier orders and attachment
distributions.

## 2. Connecting the carriers

In Lemma 2, “shortest” may be read globally over all paths whose endpoint
bags lie in different current contact components.  An internal vertex of
such a path cannot lie in another current bag.  If that bag is in the
first endpoint's contact component, the final subpath is a shorter path
between contact components; otherwise the initial subpath is one.  This
also covers a bag in a third contact component.

Absorbing the internal path vertices into the first endpoint bag preserves
connectivity and disjointness.  The last path edge creates a contact with
the other endpoint bag, so at least two former contact components merge.
The process therefore terminates with a connected contact graph.  Since
each enlarged bag contains its original carrier, it remains a
`T`-carrier.

## 3. Corollaries

A connected graph on four vertices has a vertex with at least two
neighbours.  Taking that carrier and two neighbours as
`Q_1,Q_2,Q_3` supplies the two contact edges required by Theorem 1, with
the fourth carrier used as `Q_0`.  Corollary 3 therefore proves the genuine
unbounded packing bound `nu_T(B)<=3`.

Singleton common neighbours are disjoint `T`-carriers, so
`|U_T(B)|<=3`.  Summing this inequality over edge-containing four-sets and
reversing the incidence count gives

```text
sum_T |U_T(B)|
 = sum_{v in B} |{T subseteq N(v) cap S: |T|=4 and E(G[T]) nonempty}|.
```

If `alpha(G[S])<=3`, all fifteen four-subsets contain an edge.  A vertex
with boundary degree at least four, five, or six contributes at least
`1`, `5`, or `15`, respectively, to the bound of `45`.  The resulting
limits `45,9,3` in Corollary 5 are exact deductions.

Finally, four vertices all adjacent to `T` are four singleton carriers;
hence any aligned path or other subgraph of order at least four is
terminal.  Connectivity of that subgraph is more than is needed for this
last implication, but causes no gap.

## 4. Equality witness and recession claim

The common roots in the aligned profile are `T={2,3,4,5}`, and the
displayed boundary has the literal edge `34`.  Therefore every member with
an aligned lobe of order at least four is eliminated.  This kills the
unbounded recession direction; the theorem does not claim to eliminate
the finite residual cases in which every such lobe has order at most
three.

For the order-seventeen witness, the displayed seven bags are disjoint.
The first bag is connected through the order-five path and its contacts at
`0,1,2`; `{5,11}` is connected by the edge `5--11`.  Direct checking gives
all bag adjacencies except `{14}--{16}`.  In particular, `14--15` and
`15--16` are path edges, whilst roots `2,3,4,5` supply every cross-contact
used in the construction.

Both retained standard-library verifiers were rerun.  They returned

```text
GREEN returned two-component equality witness n=17 m=68 kappa=6
  deletions_checked=9402 excesses=(6, 7) boundary_triangles=6
  compatible_supply_triples=0 target_status=not_asserted
GREEN common-four-path K7-minus model bags=7 adjacent_pairs=20
  missing_pair=(4,6) unused_vertices=(12,13)
```

## 5. Scope

The result is an unbounded, target-producing carrier theorem and a
constant portal-incidence bound.  It eliminates the aligned path
recession but does not force four common carriers in a general dense lobe,
couple arbitrary pole partitions across the two shores, or settle the
returned two-component row.  No branch-set, quantifier, arithmetic, or
scope gap remains at the frozen revision.
