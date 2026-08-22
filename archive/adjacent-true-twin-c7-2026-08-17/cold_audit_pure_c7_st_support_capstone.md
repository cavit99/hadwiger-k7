# Cold audit of the proposed pure-`C_7` `st`-support capstone

**Status: RED for the proposed capstone; GREEN for the cycle-interval
lemma and the support-four/full repair below.**  This note concerns the
pure seven-cycle common neighbourhood of adjacent true twins.  It does not
claim that the pure-cycle seam itself is target-free or terminal.

## 1. Setting

Let `G` be seven-connected with minimum degree at least eight, let `a,b`
be adjacent degree-eight true twins, and put

\[
 T=N(a)-\{b\}=N(b)-\{a\}\cong C_7,
 \qquad D=G-(T\cup\{a,b\}).
\]

The separately proved portal/exterior reduction gives, in a
`K_7^-`-minor-free host:

1. `D` is three-connected;
2. every `t in T` has at least four neighbours in `D`;
3. every one-vertex portal set has order at most two or is a consecutive
   triple of `C_7`.

The proposed capstone took an `st`-ordering of `D`, obtained adjacent
connected prefix and suffix bags `X,Y` with supports `U,V` of order at
least three, partitioned `T` into three cyclic intervals having at most one
failed `U/V` incidence, and asserted that

\[
                 \{a\},\{b\},X,Y,I_1,I_2,I_3                 \tag{1}
\]

is a `K_7^-` model.

## 2. First invalid inference

The twins are anticomplete to `D`.  Hence, in (1), each of `a,b` misses
each of `X,Y`.  There are four absent twin--exterior contacts before any
interval incidence is considered.  The interval lemma does not repair
these contacts.

This is exactly the anchor defect already recorded for earlier pure-cycle
support sweeps.  It is not fixed by choosing the suffix support to be all
of `T`.

## 3. The `(3,3)` interval lemma is true

Let `C` be any cycle and let `U,V subseteq V(C)` have order at least three.
There is a partition of `C` into three nonempty cyclic intervals such that
all three meet `U` and at least two meet `V` (after possibly interchanging
the sets).

It is enough to shrink `U` to three vertices and `V` to two.  Regard the
three `U` vertices as cyclic markers and put one cut edge in each marker
gap.  This makes three intervals, one per marker.  Choose the cuts so that
the two selected `V` vertices lie in distinct intervals:

* if both are markers, this is automatic;
* if exactly one is a marker, assign the other vertex to the interval of
  the other endpoint marker of its gap;
* if neither is a marker and they lie in one gap, cut between them;
* if they lie in different gaps, choose distinct endpoint-marker intervals
  for them.  Two distinct two-subsets of a three-set have distinct
  representatives.

Thus at most one of the six support incidences is empty.  The finite lemma
is sound; only its use in (1) is invalid.

## 4. Fully flexible anchor falsification

The verifier `verify_c7_support3_full_sevenbag.c` tests a strictly more
general repair than (1).  For fixed adjacent connected exterior bags
`X,Y` with supports `U,V`, it assigns every cycle vertex independently to

* the bag containing `a`;
* the bag containing `b`;
* the bag containing `X` (only if supported by `U`);
* the bag containing `Y` (only if supported by `V`);
* one of three nonempty connected cycle-only bags; or
* the unused label.

It then computes all twenty-one contacts from the literal twin edges,
the exterior `X--Y` edge, support edges and cycle edges.  It exhausts all
ordered pairs with `|U|,|V|>=3` and `U union V=T`.

The exact output is

```text
union_full_support_pairs=1989 failures=140
```

The 140 failures form eight orbits under the dihedral group of `C_7` and
interchange of `U,V`:

| `U` | `V` | orbit size | maximum contacts |
|---|---|---:|---:|
| `012` | `3456` | 14 | 18 |
| `012` | `03456` | 28 | 18 |
| `012` | `13456` | 14 | 19 |
| `012` | `013456` | 28 | 19 |
| `012` | `023456` | 14 | 18 |
| `012` | `0123456` | 14 | 19 |
| `0123` | `0456` | 14 | 18 |
| `0123` | `03456` | 14 | 18 |

In particular, a consecutive triple against the full seven-cycle still
has optimum nineteen contacts, two short of `K_7^-`, within this fully
flexible fixed-bag construction.  This is a finite obstruction to the
proposed reconstruction, not a claim that a host realizing this support
pair has no other `K_7^-` model.

The additional verifier `verify_c7_three_shore_transition.c` also permits
the transition vertex of the `st` sweep to remain a third exterior bag,
uses two cycle-only bags, and includes the three guaranteed exterior
contacts.  The abstract first-support-four transition hypotheses still
have many failures.  Thus splitting out the transition vertex is not by
itself a repair.

## 5. A valid support-four/full repair

### Lemma

Let `X,Y subseteq D` be disjoint connected adjacent sets.  If

\[
                  |N_T(X)|\ge4,\qquad N_T(Y)=T,             \tag{2}
\]

then `G` contains a `K_7^-` minor.

### Proof

Write `U=N_T(X)`.  If `U` is a proper subset of `T`, choose a cycle edge
`uv` with `u in U` and `v notin U`.  If `U=T`, choose any cycle edge
`uv`.  Absorb `u` into `X` and `v` into `Y`.  The other five cycle vertices
form a path and contain at least three vertices of `U-\{u\}`.  Partition
that path into three nonempty consecutive intervals, each containing one
of three such vertices.

Use the seven bags

\[
 \{a\},\quad\{b\},\quad X\cup\{u\},\quad Y\cup\{v\},
 \quad I_1,I_2,I_3.
\]

The twins see every other bag.  The two exterior bags are adjacent; the
`Y` bag sees all three intervals; and the `X` bag sees all three through
the chosen `U` vertices.  Consecutive interval bags are adjacent, so only
the two outer intervals may be nonadjacent.  This is a `K_7^-` model.
`square`

The symmetric statement also holds.

## 6. Consequence: a sharper edge profile

For every edge `xy` of a target-free `D`,

\[
                    |N_T(x) union N_T(y)|\le3.              \tag{3}
\]

Indeed, `X=\{x,y\}` is connected.  Three-connectivity makes
`Y=D-\{x,y\}` connected and adjacent to `X`.  Every `t in T` has at least
four neighbours in `D`, so deleting `x,y` leaves a neighbour in `Y`, and
therefore `N_T(Y)=T`.  If the left side of (3) were at least four, the
lemma would apply.

This improves the previously recorded upper bound four.  It does not
finish the pure-cycle row: portal pairs and consecutive triples can still
change along paths while every edge-union has order at most three.

## 7. Correct stopping point

The `st` sweep supplies a support transition, but the eight finite
obstruction orbits show that support orders `3,3`, even `3,7`, do not
synchronize the two mandatory twin--exterior anchors with the residual
cycle quotient.  A completion must use additional internal structure of
the three-connected exterior, a different rooted model, or critical
colouring data.  Neither the interval lemma nor the support sweep alone
eliminates the pure `C_7` seam.
