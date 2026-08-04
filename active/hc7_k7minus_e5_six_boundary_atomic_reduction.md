# Atomic separators in the six-boundary singleton row

**Status:** active computation-free written reduction; see the
[separate internal audit](hc7_k7minus_e5_six_boundary_atomic_reduction_audit.md).
The finite contact checks recorded in Section 7 are diagnostic only.  This
note does not prove `(E5)`.

Write `K_7^-` for `K_7` with one edge deleted.  Let `G` be a minimum
`E5` enemy, and use the exact two-singleton configuration and notation of
the [singleton-contraction theorem](hc7_k7minus_e5_singleton_contraction_uncrossing.md)
and the
[leaf-cut classification](hc7_k7minus_e5_leaf_cut_quotient_nonclosure.md).
Thus

```text
G-S has components A,{x},{y},
N_G(x)=N_G(y)=S,                    xy is not an edge,
G[S]=P_3 disjoint union K_2,
H=G[A union S],                    |E(H)|=4|V(H)|-9.
```

Fix a degree-five leaf `t` of `G[S]`, let

```text
P_t=N_G(t) intersect A={p,q},
```

and take the further exact five-cut `Q=Q_{t,p}` in the surviving
orientation whose low component is `{q}`.  This note treats the first open
intersection row

```text
R=S intersect Q,        |R|=3,        t in R.
```

The classification gives

```text
Q=N_G(q),               A intersect Q={p,b}.
```

Put

```text
Z=S-{t},
X=A-{p,b,q},
W=Z union {p,b},
E={x,y,t,q},
F=G[X union W]=H-{t,q}.
```

Thus `|W|=6` and `|X|=|A|-3>=5`.

## 1. Exact six-boundary accounting

### Lemma 1

The set `E` is a connected component of `G-W`, and

\[
 |E(G[E])|=3,\qquad |E_G(E,W)|=14,\qquad
 \delta_W(E)=1.                                      \tag{1}
\]

Moreover

\[
 |E(F)|=4|V(F)|-8,                                   \tag{2}
\]

and `(F,W)` is internally five-connected.

#### Proof

The only edges in `E` are `xt,yt,tq`.  There is no edge from `E` to `X`:
the vertices `x,y` have no neighbour in `A`, the only neighbours of `t`
in `A` are `p,q`, and `N_G(q)=Q` misses `X`.  The set is connected and
meets every vertex of `W`.  Its incidences with `W` number

```text
4 from x,       4 from y,       2 from t,       4 from q.
```

This proves (1).

In `H`, the vertices `t,q` have degrees three and five, respectively, and
they are adjacent.  Deleting both therefore removes seven edges.  Hence

\[
 |E(F)|=(4|V(H)|-9)-7=4|V(F)|-8.
\]

Finally, the open side of any rooted separation of `(F,W)` of order at
most four lies in `X`.  It has no neighbour in `E`, so the same separator
disconnects `G`, contrary to five-connectivity.  \(\square\)

### Lemma 2

Every component `C` of `G[X]` has

\[
                         |N_G(C)|\in\{5,6\},          \tag{3}
\]

with `N_G(C)` contained in `W`.  If the components are `C_1,...,C_m`,
then

\[
                 \sum_i\delta_W(C_i)=16-|E(F[W])|.   \tag{4}
\]

#### Proof

There are no edges from `X` to `E`, and different components of `G[X]`
are nonadjacent.  Thus `N_G(C)` is contained in the six-set `W`, while
five-connectivity gives the lower bound five.  Equation (4) follows by
subtracting the edges of `F[W]` from (2) and grouping the remaining edges
by their `X`-component.  \(\square\)

## 2. Five-contact components are atomic

For `w in W`, let `M_w` be the union of the components `C` of `G[X]`
with

\[
                           N_G(C)=W-\{w\}.             \tag{5}
\]

### Lemma 3

If `M_w` is nonempty, then `W-{w}` is an exact five-cut.  Each component
represented in `M_w` remains a component after the deletion, and there is
one connected exterior containing `E union {w}` and every other
`X`-component.  Moreover

\[
 |M_w|\le2,
 \qquad
 \delta_{W-\{w\}}(C)=\delta_W(C)\le3                 \tag{6}
\]

for every component `C` contained in `M_w`.

#### Proof

The set `E union {w}` is connected.  Every `X`-component not represented
in `M_w` has a neighbour at `w`, and therefore belongs to the same
component after deleting `W-{w}`.  The components represented in `M_w`
miss `w` and are separated from it.  This proves the cut and component
description.

No component in `M_w` can have excess at least four: it is a proper subset
of `X`, hence has order below `|A|`, contradicting the minimum choice of
the high-excess lobe `A`.  The universal five-cut excess lemma therefore
places an excess-at-least-four component in the exterior.  Its order is at
least `|A|`.  There are exactly `|A|+2` vertices outside any five-cut, so
the total order of `M_w` is at most two.  A component in (5) has no edge
to `w`, making its two displayed excesses equal.  \(\square\)

### Lemma 4

At most one component of `G[X]` is adjacent to all six vertices of `W`.

#### Proof

Suppose that `C_1,C_2` are two such components.  If `t-u-v` is the
three-vertex path of `G[S]` and `rs` its disjoint edge, then

```text
{t,p}, {u}, {v}, {x,r}, {y,s}, C_1 union {b}, C_2
```

are seven disjoint connected branch sets.  Every pair is adjacent except
possibly `{t,p}` and `{v}`.

If instead `tu` is the disjoint edge and `r-s-v` is the path, use

```text
{t,p,x}, {u,y}, {r}, {s}, {v}, C_1 union {b}, C_2.
```

Only `{r}` and `{v}` are nonadjacent.  Either list is an explicit
`K_7^-` model, a contradiction.  \(\square\)

## 3. A helper containing `p` closes the row

Recall that a `Z`-rooted `K^*_{4,2}` model has four root bags and two
adjacent helper bags, each helper adjacent to every root bag.  The root
bags are not required to be mutually adjacent.

### Lemma 5

If `F` has a `Z`-rooted `K^*_{4,2}` model in which `p` belongs to a helper
bag, then `G` contains a `K_7^-` minor.

#### Proof

Write the helper containing `p` as `U` and the other helper as `V`.
Use a root letter also for its rooted bag.  Put `R_0=R-{t}`; this is the
two-set of root bags met by `q`.  The guaranteed additional adjacencies
are

```text
tU, qU, tq;
x and y to every root bag;
tx,ty;
q to the two bags in R_0.
```

For the two tables only, rename the fixed dense-side vertex `b` as
`\beta`; the letters `a,b,c,d` below are exclusively boundary-root labels.
The vertex `\beta` is not used in these constructions.

If `t-a-b` is the path and `c-d` the edge, the following table gives the
seven branch sets.  Concatenation denotes union.

| `R_0` | seven branch sets |
|---|---|
| `{a,b}` | `a`, `bq`, `cx`, `dy`, `U`, `V`, `t` |
| `{a,c}` | `a`, `bx`, `cq`, `dy`, `U`, `V`, `t` |
| `{a,d}` | `a`, `bx`, `cy`, `dq`, `U`, `V`, `t` |
| `{b,c}` | `a`, `b`, `cV`, `dU`, `x`, `y`, `tq` |
| `{b,d}` | `a`, `b`, `cU`, `dV`, `x`, `y`, `tq` |
| `{c,d}` | `aV`, `bU`, `c`, `d`, `x`, `y`, `tq` |

In the first row only `V`--`t` may be absent; in each of the last three
rows only `x`--`y` is absent.  The middle two rows of the first group are
complete or have the same harmless helper--`t` omission.

If `t-a` is the edge and `b-c-d` the path, the first three rows above work
for `R_0={a,b},{a,c},{a,d}`.  For the other rows use

| `R_0` | seven branch sets |
|---|---|
| `{b,c}` | `aV`, `b`, `c`, `dU`, `x`, `y`, `tq` |
| `{b,d}` | `aV`, `bq`, `c`, `d`, `Ut`, `x`, `y` |
| `{c,d}` | `aV`, `bU`, `c`, `d`, `x`, `y`, `tq` |

Every displayed union is connected through one of the guaranteed edges.
A direct pair check leaves at most the stated single nonadjacency.  Thus
every row gives `K_7^-`.  \(\square\)

## 4. Failure before the rooted model gives a three-separator atom

### Theorem 6

If `(F,Z)` is not internally four-connected, there is a three-set `T`
and a connected set `C` such that

\[
 N_F(C)=T,\qquad p\in C,\qquad |C|\le2,               \tag{7}
\]

and

\[
                         T\cup\{t,q\}                 \tag{8}
\]

is an exact five-cut of `G`.  This cut has exactly two complementary
components, `C` and one component of order `|A|+2-|C|`.  The small side is
exactly one of the following.

1. `C={p}`.  Then `N_G(p)=T union {t,q}` and
   `delta(C)=1`.
2. `C={p,b}`, where `pb` is an edge, `b` is adjacent to every member of
   `T`, and `p` is adjacent to two or three members of `T`.  Its excess is
   one or two, respectively.

In every case

\[
 |E(F-C)|=4|V(F-C)|-8+g-\delta(C)\ge4|V(F-C)|-7,      \tag{9}
\]

where `g=2` in case 1 and `g=3` in case 2.

#### Proof

Take a root-side separation of `(F,Z)` of order at most three and a
component `C` of its far side.  A component containing neither `p` nor
`b` has the same separator in `G`, contrary to five-connectivity.  A
component containing `b` but not `p` has open neighbourhood contained in
the separator together with `q`, again of order at most four.  Hence the
only far component contains `p`.

The only neighbours of `p` outside `F` are `t,q`, while `b` has only `q`
outside `F` and `X` has none.  Five-connectivity forces the separator to
have order three and makes (8) the whole neighbourhood of `C`.  Every
other component of `F-T` contains a surviving member of `Z`; otherwise
the preceding neighbourhood argument applies again.  The vertices `x,y`
join all those rooted components after (8) is deleted.  Hence the lifted
cut has exactly two complementary components.

The set `C` is contained in `X union {p,b}` and has order below `|A|`.
The universal five-cut excess lemma puts an excess-at-least-four component
on the other side, whose order is at least `|A|`.  Since there are
`|A|+2` vertices outside the cut, `|C|<=2` and `delta(C)<=3`.

If `C` is a singleton it is `{p}` and is full to the five-cut, proving
case 1.  If `C={p,c}`, then `c in X` would have only `p` and the three
vertices of `T` as possible neighbours, contrary to minimum degree five.
Thus `c=b`.  The edge `pb`, the edge `bq`, and the absence of `bt` force
`b` to be complete to `T`; minimum degree forces `p` to meet at least two
members of `T`.  Direct counting gives excess one or two.

Deleting `C` from `F` removes

\[
 4|C|+\delta(C)-g
\]

edges, where `g=|E_G(C,{t,q})|`.  This proves (9).  \(\square\)

## 5. Failure of fifth-root augmentation gives a four-separator atom

### Theorem 7

Suppose `(F,Z)` is internally four-connected.  Then `F` has a
`Z`-rooted `K^*_{4,2}` model.  Either `G` contains `K_7^-`, or there is a
four-set `T` and a connected set `C` such that

\[
 N_F(C)=T,\qquad b\in C,\qquad |C|\le2,               \tag{10}
\]

and `T union {q}` is an exact five-cut with exactly two complementary
components.  The small side is exactly one of the following.

1. `C={b}`.  Then `N_G(b)=T union {q}` and
   `delta(C)=1`.
2. `C={b,c}` for `c in X`.  The vertex `c` is complete to `T`; the vertex
   `b` is adjacent to three or four members of `T`; and the excess is one
   or two, respectively.

In both cases

\[
             |E(F-C)|\ge4|V(F-C)|-9.                 \tag{11}
\]

#### Proof

Equation (2) and Norin--Totschnig Lemma 12 give the rooted model.  If
`(F,Z union {p})` is internally five-connected, the audited fifth-root
augmentation lemma puts `p` in a helper, and Lemma 5 closes the row.

Otherwise take a far component `C` of a rooted separation of order at
most four.  It cannot avoid `b`: such a component lies in `X`, has the
same open neighbourhood in `G`, and contradicts five-connectivity.  Its
only possible neighbour outside `F` is `q`, through `b`.  Hence the
separator has order four and `T union {q}` is the exact neighbourhood of
`C`.  As in Theorem 6, every other component meets `Z union {p}` and the
fixed exterior joins them, so the lifted cut has exactly two components.
Minimum high-excess-lobe order now gives `|C|<=2`.

The singleton is `{b}` and is full to the cut.  In the edge case write
`C={b,c}`.  The vertex `c in X` has no neighbour outside `F`, so minimum
degree makes it complete to all four members of `T`.  The vertex `b` has
the two neighbours `c,q` and therefore meets three or four members of
`T`.  The excess is one or two by direct counting; in particular, the
formerly possible excess-three equality row does not exist.

Here `g=|E_G(C,{q})|=1`, so the deletion identity used in Theorem 6 gives

\[
 |E(F-C)|=4|V(F-C)|-7-\delta(C),
\]

which is (11).  \(\square\)

### Corollary 8 (the four-separator atom is the excess-two edge)

In a target-free instance, the alternative in Theorem 7 reduces further
to

```text
C={b,c},
b and c are adjacent to all four vertices of T,
delta_{T union {q}}(C)=2.
```

Moreover there is a `Z`-rooted `K^*_{4,2}` model whose helper bags are
the singletons `{b},{c}` and in which the four vertices of `T` occur one
in each root bag.

#### Proof

Among all `Z`-rooted `K^*_{4,2}` models in `F`, choose one whose helper
bags `U,V` have maximum total order and, subject to that, whose four root
bags have minimum total order.  The proof of the audited fifth-root
augmentation lemma applies verbatim to this optimisation.  In each root
bag there is exactly one vertex with a neighbour in `U union V`, and no
component outside the six model bags has a neighbour in `U union V`.
Consequently

\[
 |N_F(U\cup V)-(U\cup V)|=4,                          \tag{12}
\]

with the four boundary vertices lying one in each root bag.

If neither `p` nor `b` belonged to the helper union, (12) would give a
rooted separation of `(F,W)` of order four, contrary to Lemma 1.  If `p`
belongs to a helper, Lemma 5 gives the target.  We may therefore assume
that `b` belongs to the helper union and `p` does not.

The connected set `U union V` is then a component after deleting the
four-set in (12), and it is the far side of a separation of
`(F,Z union {p})`.  The proof of Theorem 7 applies to this particular
component, not merely to an existentially chosen witness.  Hence
`U union V` is `{b}` or `{b,c}` with one of the two incidence patterns
listed there.  Both helpers are nonempty and disjoint, so it is the edge
`{b,c}` and the helpers are its two singleton vertices.

In the excess-one pattern, `b` is adjacent in `F` only to `c` and three
vertices of `T`.  Those three vertices lie in three different root bags,
so the singleton helper `{b}` misses the fourth root bag, contradicting
the definition of the model.  The excess-two pattern is therefore forced.
Here Theorem 7 says that both `b` and `c` are complete to `T`, proving all
claims.  \(\square\)

### Corollary 9 (a synchronised rooted clique in the last normal form)

In the excess-two normal form of Corollary 8, `F` has a `Z`-rooted
`K_4` model obtained from the same six bags.  Enlarge its four bags to
include every vertex of `F`, and let `B_p` be the bag containing `p` and
`B_b` the bag containing `b`.  If

```text
B_p, B_b, and the two root bags indexed by R-{t}
```

are four distinct bags, then `G` contains `K_7^-`.

#### Proof

Let the four root bags be `R_1,...,R_4`, and let the corresponding four
vertices of `T` be `w_1,...,w_4`.  Choose any edge `z_kz_l` of `G[Z]`.
Absorb the singleton helpers `b,c` into the two root bags whose indices are
complementary to `k,l`, one helper into each bag.  The two enlarged bags
are adjacent through `bc` and are adjacent to both retained root bags
through the helper--portal edges.  The two retained bags are adjacent
through `z_kz_l`.  These are four pairwise adjacent bags rooted at `Z`.

The graph `F` is connected.  Indeed, every `X`-component meets at least
five vertices of `W`, so all such components and at least five vertices of
`W` lie in one component of `F`.  A possible sixth vertex of `W` has at
most four neighbours outside `F`, and minimum degree five gives it a
neighbour in that component.  The four bags may therefore be enlarged to
a spanning model without losing any adjacency.  The vertex `q` meets the
bag `B_b` through `qb`, the bag `B_p`
through `qp`, and the two root bags indexed by `R-{t}` through its two
root neighbours.  Under the displayed distinctness condition, it is
therefore adjacent to all four bags.  The seven bags

```text
the four enlarged rooted bags,       {x,t},       {y},       {q}
```

are pairwise adjacent except possibly `{y}`--`{q}`.  They give the claimed
minor.  \(\square\)

### Corollary 10 (only six root-contact rows survive)

In the excess-two normal form of Corollary 8, put `R_0=R-{t}`.  If `t` is
an end of the three-vertex path, label

```text
t-a-b,                 c-d.
```

Then target-freeness forces

\[
                         R_0\in\{\{a,c\},\{a,d\}\}.  \tag{13}
\]

If instead `t-a` is the two-vertex component and `b-c-d` is the path,
then target-freeness forces

\[
 R_0\in\{\{a,b\},\{a,c\},\{a,d\},\{b,d\}\}.         \tag{14}
\]

#### Proof

To avoid a collision with the root label `b`, write the dense-side helper
of Corollary 8 as `U={\beta}` and the other helper as `V`.  Thus `qU` is
an edge.  In the first boundary labelling, the four excluded rows have the
following seven branch sets:

| `R_0` | seven branch sets |
|---|---|
| `{a,b}` | `a`, `b`, `cx`, `dy`, `U`, `V`, `tq` |
| `{b,c}` | `a`, `b`, `cV`, `dU`, `x`, `y`, `tq` |
| `{b,d}` | `a`, `b`, `cU`, `dV`, `x`, `y`, `tq` |
| `{c,d}` | `aV`, `bU`, `c`, `d`, `x`, `y`, `tq` |

Only `V`--`tq` may be absent in the first row; only `x`--`y` is absent in
the other three.  In the second boundary labelling, the two additional
target rows are

| `R_0` | seven branch sets |
|---|---|
| `{b,c}` | `aV`, `b`, `c`, `dU`, `x`, `y`, `tq` |
| `{c,d}` | `aV`, `bU`, `c`, `d`, `x`, `y`, `tq` |

Again only `x`--`y` is absent.  Each displayed union is connected through
a guaranteed model or boundary edge.  This proves (13)--(14).  \(\square\)

### Corollary 11 (the final four-separator obstruction is one bag)

For each of the six pairs in (13)--(14), the rooted `K_4` construction of
Corollary 9 can be chosen so that `B_b` and the two bags indexed by `R_0`
are distinct.  Let `B_*` be the fourth bag.  Target-freeness implies that
no spanning enlargement of this chosen rooted model puts `p` in `B_*`.

#### Proof

Use the following choice of the actual root edge retained between the two
unabsorbed bags, and assign the helper `b` to the indicated complementary
root bag:

| boundary type | `R_0` | retained root edge | root of `B_b` | root of `B_*` |
|---|---|---|---|---|
| `t-a-b`, `c-d` | `{a,c}` | `ab` | `d` | `b` |
| `t-a-b`, `c-d` | `{a,d}` | `ab` | `c` | `b` |
| `t-a`, `b-c-d` | `{a,b}` | `bc` | `d` | `c` |
| `t-a`, `b-c-d` | `{a,c}` | `bc` | `d` | `b` |
| `t-a`, `b-c-d` | `{a,d}` | `cd` | `b` | `c` |
| `t-a`, `b-c-d` | `{b,d}` | `bc` | `a` | `c` |

The first assertion is immediate from the table and Corollary 9.  If a
spanning enlargement put `p` in `B_*`, then the edges from `q` to `b`,
`p`, and the two roots in `R_0` would meet four distinct bags.  Corollary 9
would give `K_7^-`, a contradiction.  \(\square\)

## 6. Published rooted `K_{3,3}` supply and its exact limit

There is a second, genuinely applicable published input.  The graph `H`
is three-connected: if a set of at most two vertices disconnected `H`,
then adjoining `x,y` to that set would give a cut of `G` of order at most
four.  Since `|E(H)|=4|V(H)|-9`, Corollary 5 of Jørgensen and
Kawarabayashi gives a `K_{3,3}` minor rooted at any prescribed three-set.

Apply it to the three vertices of the `P_3` component of `G[S]`.  If the
two vertices of the disjoint `K_2` can be put in two distinct helper bags,
then the third helper can be merged into an endpoint root bag.  The other
two path-root bags are adjacent by a path edge, while the two occupied
helper bags are adjacent through the `K_2` edge.  This is an `S`-rooted
`K_5` model.  Together with `{x},{y}` it gives `K_7^-`.

The cited corollary roots only the three bags on one side of `K_{3,3}`.  It
does not place two further prescribed vertices in distinct helper bags.
Thus it supplies a promising alternative formulation, but not the missing
augmentation theorem.

The external source is L. K. Jørgensen and K. Kawarabayashi,
*Extremal results for rooted minor problems*, Journal of Graph Theory
**55** (2007), 191--207, Corollary 5,
<https://doi.org/10.1002/jgt.20232>.

## 7. Exact endpoint and nonclosures

Combining Theorems 6 and 7 gives the following computation-free endpoint.

> **Atomic six-boundary reduction.** Every target-free instance of the
> `s=3`, singleton-`q` row has either a three-separator atom whose lifted
> low component is one of
> \[
>                         \{p\},\quad \{p,b\},
> \]
> or the unique four-separator normal form
> \[
> C=\{b,c\},\qquad \delta(C)=2,
> \]
> where `b,c` are the two singleton helpers and the four adhesion vertices
> occur one per root bag.  In that normal form the same bags contain a
> `Z`-rooted `K_4`, and target-freeness forces overlap among the four
> contacts supplied by `b`, `p`, and the two root neighbours of `q`.
> The two root neighbours must additionally lie in one of the six pairs
> listed in (13)--(14), and the remaining obstruction is that `p` cannot
> be assigned to one explicitly nominated fourth root bag in any spanning
> enlargement of the corresponding rooted `K_4` model.
> Every atom has excess one or two, and deleting it from `F` leaves at
> least `4|V|-9` edges.  Otherwise the instance has an explicit `K_7^-`
> minor.

The remaining inference is not merely density.  Deleting an atom can
expose another rooted separator, and an ordinary rooted
`K^*_{4,2}` model in the residual graph may put every adhesion portal in
one root bag.  It need not put `p` in a helper.

A diagnostic exhaustive check confirms that adhesion concentration is a
real obstruction for a generic residual six-bag model.  In the hardest
path-leaf row, contract all three or four adhesion vertices into the same
root bag of an otherwise valid model.  The four initial atomic side types,
including both edge-excess patterns, then have target-free contact
quotients of minimum defect two.  The dependency-free verifier is
[`hc7_k7minus_e5_s3_atomic_portal_concentration_verify.py`](hc7_k7minus_e5_s3_atomic_portal_concentration_verify.py).
This is finite evidence about abstract quotients, not a host counterexample
and not part of the proof above.  Corollary 8 shows in particular that the
surviving four-separator normal form itself has a stronger one-portal-per-
root-bag condition than this generic obstruction.

The smallest remaining repair is therefore any one of the following
host-level statements.

1. An atomic-side rerouting theorem puts `p` in a helper of a
   `Z`-rooted `K^*_{4,2}` model.
2. The adhesion must meet a helper or enough distinct root bags to trigger
   the explicit construction in Lemma 5.
3. In the excess-two four-separator normal form, reselect the spanning
   rooted `K_4` so that the `b`, `p`, and two `q`-root contacts occupy four
   distinct bags.
4. A further uncrossing localises excess at least four in a component of
   order below `|A|`.
5. In the published formulation, the two `K_2` roots can be put in
   distinct helpers of the `P_3`-rooted `K_{3,3}` model.

A smaller side, the residual `4|V|-9` density, or an unplaced rooted model
alone proves none of these conclusions.

The subsequent
[companion-cut theorem](hc7_k7minus_e5_s3_companion_cut_elimination.md)
eliminates the four-separator normal form after refining the minimum-lobe
choice by maximum excess.  The two order-three atoms remain open.
