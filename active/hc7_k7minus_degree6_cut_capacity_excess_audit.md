# Internal audit: degree-six cut capacity and exact excess

**Verdict:** GREEN.

**Audited source:**
`active/hc7_k7minus_degree6_cut_capacity_excess.md`

**Source SHA-256:**
`7f29b58fb1dcd40c1f6f22fc8b6811578deca56b60e07283197387dc2f762194`

This is a separate internal mathematical audit, not external peer review.
The proof is computation-free.

## 1. Fullness and the elementary branch-set construction

For every component `C` of `H-T`, its neighbourhood is a subset of the
six-set `T`.  Six-connectivity makes that neighbourhood all of `T`.

For `k` selected full components, absorbing `k-1` of them into distinct
boundary vertices, retaining the last component as a bare bag, and keeping
the remaining boundary vertices singleton gives exactly seven disjoint
connected bags.  All possible missing adjacencies lie among the `7-k`
unabsorbed boundary singletons.  The consequences are correct:

- five components give at most one missing adjacency;
- four components force every boundary triple to span at most one edge,
  so the boundary is a matching;
- three components force every boundary four-set to span at most four
  edges;
- two components force every boundary five-set to span at most eight
  edges.

The double counts are exact.  An edge of a six-set lies in six of its
fifteen four-subsets and four of its six five-subsets, giving respectively
`|E(H[T])|<=10` and `|E(H[T])|<=12`.

## 2. Exclusion of four components

If a component `C` is non-singleton and `Q` is a four-subset of `T`, then
`(H[C union Q],Q)` is internally four-connected.  A prohibited rooted
separation of order at most three lifts, after adding the two vertices of
`T-Q`, to a cut of `H` of order at most five.  Another component survives
on the opposite side.  Since the rooted graph has at least six vertices,
Jørgensen's rooted-diamond theorem applies.

The three remaining components and two unused boundary vertices give
three further bags: two components absorb one boundary vertex each and the
third remains bare.  Fullness supplies all adjacencies within these three
bags and from them to the four rooted bags.  Thus the rooted diamond gives
a `K_7^-` model.

Consequently all four components would be singletons.  A boundary vertex
then has four external neighbours and at most one boundary neighbour,
contradicting minimum degree six.  The strengthened conclusion `r<=3` is
valid.

The same construction in the three-component case proves the conditional
boundary bound `Delta(H[T])<=3`: a boundary vertex with four boundary
neighbours serves as the seventh singleton bag, while the two other
components supply one anchored and one bare bag.

## 3. Exact excess identity

Writing `C_1,...,C_s` for the components other than `{x}`, the edge
partition is

```text
|E(H)| = |E(H[T])| + 6
         + sum_i (4|C_i| + delta_i).
```

Since `|V(H)|=7+sum_i|C_i|`, this simplifies to

```text
|E(H)| = 4|V(H)|-22 + |E(H[T])| + sum_i delta_i.
```

The equivalence with the excess bound fifteen is therefore exact.  The
source correctly labels that bound as an open obligation outside the cubic
row.

## 4. Cubic three-component row

Let the components be `{x},A,B`, and suppose `H[T]` is cubic.  For every
ordered boundary nonedge `(q,p)`, put `Z=T-{q,p}`.  A `Z`-rooted `K_4`
model in `H[A union Z]`, together with

```text
B union {p}, {x}, {q},
```

would form a `K_7^-` model.  The only possible missing adjacency is from
`q` to the unique root in `Z` not adjacent to it.  Thus the rooted model is
absent, and the pair is internally four-connected by the same separator
lift used above.

Norin--Totschnig Lemma 9 gives the displayed inequality (8).  Its sum over
the twelve ordered nonedges is correct:

- each attachment count has coefficient `12-2-2=8`;
- each boundary edge avoids exactly two undirected boundary nonedges and
  therefore occurs in four ordered complements;
- a cubic graph on six vertices has nine edges.

This yields `3e_A+2P_A<=9|A|+6`.  Connectedness gives
`e_A>=|A|-1`, whence `2delta_A<=7` and the integral bound
`delta_A<=3`.  The symmetric bound for `B` proves total excess at most
fifteen.

## 5. Eight-edge three-component row

### Boundary classification

The degree-sequence argument is complete.  With eight edges and maximum
degree three, the only alternative to `3,3,3,3,2,2` is
`3,3,3,3,3,1`; deleting the degree-one vertex and its neighbour then
leaves five edges on four vertices, contrary to Theorem 1.

For the four degree-three vertices `D` and two degree-two vertices `L`,
degree summation gives

```text
|E(H[D])|-|E(H[L])|=4.
```

The four-set bound excludes an edge in `L`.  Thus `H[D]` has four edges
and minimum degree at least one, making it a four-cycle or a paw.  The
cross-degrees then give exactly the three labelled graphs I--III in the
source.

### Weighted certificates

Every omitted pair in the table is a boundary nonedge with a degree-three
end.  Hence the same seven-bag completion as in the cubic row proves the
absence of the corresponding rooted `K_4`, and Norin--Totschnig Lemma 9
applies.

For boundary I, the six pairs split into two triples and every boundary
vertex occurs twice.  One quarter of their six inequalities plus one half
of `c-e_C<=1` has left side exactly

```text
e_C+P_C-4c
```

and right side `14/4+1/2=4`.  For II and III the three pairs partition the
boundary; one half of those three inequalities plus the same connectedness
term has the identical left side and right side `7/2+1/2=4`.  Thus the two
lobe excesses are each at most four.

### Equality structure

Equality forces `e_C=c-1` and `P_C=3c+5`.  Minimum degree six gives
`6c<=5c+3`, so `c<=3`; fullness excludes `c=1`.  At `c=3`, equality in
the degree sum makes the lobe a path whose endpoints miss one boundary
vertex each and whose middle vertex misses two.

Writing `h_t=c-p_C(t)`, direct substitution in all six rooted inequalities
gives exactly the three rows in the source table.  The check is linear:

- for I, `01,02,12` give `(h_0,h_1,h_2)=(1,1,0)` and the other triple is
  symmetric;
- for II, the three weighted equalities and `03,12,45` give the same
  vector;
- for III, the weighted equalities and `04,12,35` give either
  `(1,1,1,0,0,1)` or `(0,2,0,1,1,0)` at order three, and the sole miss at
  root `1` at order two.

These equations also exclude order two in I and II.

### Equality decoder

For I and II, the six lobe vertices can be assigned one per boundary root.
Choose in the first path a vertex seeing both `0,1`, and in the second a
vertex seeing both `4,5`.  After removing them, at least two of the four
remaining vertices see `1` and at least two see `5`, so distinct
representatives exist.  The last two vertices see both degree-two roots.
The four-cycle supplies the remaining degree-three adjacencies, and the
lobe vertices repair every degree-two nonedge.  This is a rooted `K_6`.

For III with two order-two lobes, the displayed assignment repairs in turn
the seven boundary nonedges

```text
01, 04, 12, 23, 34, 35, 45.
```

For an order-three lobe, the six-row table was checked directly.  Each
assigned path vertex sees its root, and every pair among the five
non-universal rooted bags is joined either by a boundary edge, a path edge,
or a displayed attachment.  Reversal and the automorphism `(0 2)(3 4)`
generate every ordering compatible with the two deficiency vectors.  The
other full lobe absorbed at the image of root `0` supplies the universal
sixth bag.

Thus every equality case contains a boundary-rooted `K_6`; adjoining
`{x}` gives a `K_7`.  The eight-edge row is eliminated without a computer
classification.

## 6. One-terminal cross-lobe composition

For ordered distinct terminals `q,p`, put `Z=T-{p,q}`.  Removing `p`
from one closed lobe changes its excess by exactly `p_C(p)`.  The retained
five-terminal pair is internally five-connected: a separation of order at
most four lifts after adding `p` to a cut of `H` of order at most five.

The proof of the rooted six-bag assertion correctly separates the two
possible attachment rows.

- If `p_C(q)<=delta'-1`, omit `q`, complete the four roots, and obtain
  exactly the Lemma 12 threshold `4(c+4)-9`.
- Otherwise retain `q`.  The hypothesis
  `delta'+d_{T-p}(q)>=5` gives the exact threshold `4(c+5)-9`; it also
  makes the possible singleton open side at `q` have degree at least five.

The virtual edges join nominated roots and are irrelevant to the
root--helper and helper--helper adjacencies.  The existing fifth-root
augmentation lemma therefore legitimately places `q` in a helper.

For the opposite rooted `K_4`, the edge count is at least `3c+9`.  The
only possible failure of internal four-connectivity is the singleton
`{p}`.  If it occurs, its degree is at most three; deleting it leaves at
least `3c+6` edges on `c+4` vertices and an internally four-connected
rooted pair.  Thus Lemma 9 forces the rooted `K_4` in both cases.

The terminal composition is disjoint.  The first model omits `p`, the
second omits `q`, and the models overlap only in the four literal roots.
Merging corresponding root bags gives a clique through the rooted `K_4`.
The singleton `{x}` sees all four roots and the helper containing `q`, so
only its adjacency to the second helper may be absent.  This is exactly a
`K_7^-` model.

## 7. Seven-edge boundaries with three degree-three vertices

The boundary classification is complete.  Four degree-three vertices
would force at least five edges on their four-set.  With exactly three,
the remaining degrees are `2,2,1`; writing `h` and `ell` for the numbers
of edges inside the two degree classes gives `h-ell=2`.  The four-set
bound leaves precisely the three displayed graphs I--III.

For I and II, the three omitted pairs partition the boundary.  Half the
three rooted inequalities plus half of connectedness has left side
`delta_C` and right side `9/2`; integrality gives `delta_C<=4`.

For III, half the four rooted inequalities, half of the two attachment
upper bounds at roots `0,3`, and half of the minimum-degree inequality has
left side exactly

```text
e_C + sum_t p_C(t) - 4c = delta_C
```

and right side five.  Equality forces

```text
p_C(0)=p_C(3)=c,
p_C(1)=p_C(2)=3,
p_C(4)=p_C(5)=2.
```

If the total excess exceeded eight, one lobe would have excess five and
the other at least four.  For `(q,p)=(4,5)`, the equality lobe satisfies
the rooted six-bag threshold because root `4` has two neighbours after
deleting `5` and `p_C(5)=2`.  The opposite lobe satisfies the rooted
`K_4` threshold because deleting degree-two root `4` leaves five boundary
edges.  Lemma 5 then supplies the forbidden model.  The row is therefore
closed analytically, not by finite enumeration.

## 8. External trust boundary and scope

The only external rooted inputs are Lemmas 9 and 10 of Sergey Norin and
Agnès Totschnig, *Every graph with no `K_7^vee`-minor is 6-colorable*,
arXiv:2507.03244.  Lemma 9 gives `|E(F)|<=3|V(F)|-7` for an internally
four-connected rooted pair with no rooted `K_4` model.  Lemma 10 gives a
rooted `K_4^-` model in an internally four-connected rooted graph of order
at least six.  Their hypotheses are checked explicitly above; the external
theorems themselves are not reproved.

No claim is made for a three-component boundary with at most six edges,
for the four seven-edge boundaries of degree sequence `3,3,2,2,2,2`, or
for the two-component row.  In particular, the degree-six extremal theorem
has not been proved in those cases.
