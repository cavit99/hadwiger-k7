# Internal audit: atomic separators in the six-boundary singleton row

**Verdict:** **GREEN** for the pinned source revision.  This is a separate
internal mathematical audit, not external peer review.

**Audited source:**
`active/hc7_k7minus_e5_six_boundary_atomic_reduction.md`

**SHA-256:**
`3f2084f172183f38b91aa5a9ef402d2c60095579dda915fa6fcadaabfe94edff`

No mathematical correction is required at this revision.

Relative to the previously audited revision
`eccb5d2e0181f0f7005bd7e86dce7f04b6bd9eb2f3eb5bd1e20a00a2f86afc34`,
the source changes only its status link and adds a final cross-reference to
the separately audited companion-cut theorem.  The theorem statements,
proofs, tables and diagnostic scope are unchanged.  The new cross-reference
accurately records that the companion theorem eliminates the
four-separator normal form only after the stated maximum-excess refinement,
while leaving the two order-three atoms open.

## 1. Setup and six-boundary accounting

In the `s=3`, singleton-`q` orientation, the identities

```text
Q=N_G(q),                 S intersect Q=R,
R={t,r_1,r_2},            A intersect Q={p,b}
```

give the disjoint partition

```text
W=(S-{t}) union {p,b},    X=A-{p,b,q},
E={x,y,t,q},              F=G[X union W]=H-{t,q}.
```

The only edges inside `E` are `xt,yt,tq`.  Its incidences with `W` are
eight from `x,y`, two from `t`, and four from `q`.  Thus its excess is

```text
3+14-4(4)=1.
```

In `H`, the degrees of `t,q` are three and five and their common edge is
counted twice in the degree sum.  Deleting them removes seven edges and
therefore gives

```text
|E(F)|=4|V(F)|-8.
```

Every far side of a rooted separation of `(F,W)` lies in `X`.  It has no
edge to `E`, so a separator of order at most four would also disconnect
`G`.  The asserted internal five-connectivity follows.  Grouping the
edges outside `F[W]` by the components of `G[X]` gives exactly

```text
sum_C delta_W(C)=16-|E(F[W])|.
```

Five-connectivity and the six-vertex boundary force every such component
to have five or six neighbours in `W`.

## 2. Five-contact components and full components

For a component with neighbourhood `W-{w}`, deleting that five-set leaves
the component separated from the connected set `E union {w}`.  Every
other `X`-component has a neighbour at `w` and therefore lies in the same
exterior component.  The component description in Lemma 3 is exact.

No five-contact component can have excess at least four, because its order
is below the selected minimum order `|A|`.  The universal five-cut lemma
therefore puts a high-excess component in the exterior.  There are
`|A|+2` vertices outside a five-cut, while that exterior has order at least
`|A|`; hence the union of all components missing the same `w` has order at
most two.  Their excess is unchanged when measured against `W-{w}` because
they have no edge to `w`.

The two branch-set lists in Lemma 4 were checked pair by pair.  In the
path-leaf case the only possible omission is between `{t,p}` and `{v}`.
In the edge-leaf case the only omission is between the two nonadjacent
ends `{r}` and `{v}` of the three-vertex path.  Connectivity of
`C_1 union {b}` and its adjacency to `C_2` both use fullness at `b`, so no
unstated component--component edge is used.

## 3. The helper-containing-`p` tables

Lemma 5 uses only the following edges beyond a rooted `K^*_{4,2}` model:

```text
tU, qU, tq, tx, ty;
x and y to every root bag;
q to the two root bags indexed by R-{t};
the three fixed edges of P_3 disjoint union K_2.
```

All twelve rows were independently checked.  Every displayed union is
connected and the branch sets are disjoint.  Their sole possible missing
pairs are as follows.

- In the first three rows for either boundary orientation, only `V` and
  `t` may fail to be adjacent.
- In the final three path-leaf rows, only `x` and `y` are nonadjacent.
- In the final three edge-leaf rows, only `x` and `y` are nonadjacent.

Thus every row is an explicit `K_7^-` model.  The local renaming of the
dense-side vertex as `\beta` removes the otherwise ambiguous collision
with the boundary-root label `b`.

## 4. The order-three atom

Take any far component `C` of a rooted separation of `(F,Z)` of order at
most three.  A component avoiding both `p,b` would have the same separator
in `G`; a component containing `b` but not `p` would have only the
separator and `q` as possible external neighbours.  Both contradict
five-connectivity.  Hence the unique far component contains `p`.

Its only neighbours outside `F` are `t,q`.  Five-connectivity therefore
forces

```text
|N_F(C)|=3,            N_G(C)=N_F(C) union {t,q}.
```

Every other component after deleting `N_F(C)` contains a surviving root
of `Z`; the vertices `x,y` join all of them after the lifted cut is
deleted.  The lift consequently has exactly two complementary components.

The opposite component has excess at least four and hence order at least
`|A|`.  Since there are `|A|+2` vertices outside the cut, `|C|<=2`.
The classification is exhaustive:

- a singleton is `{p}`, has five boundary neighbours, and has excess one;
- if `C={p,c}` with `c in X`, then `c` has at most four neighbours, which
  is impossible;
- hence the edge case is `{p,b}`.  Minimum degree makes `b` complete to
  the three adhesion vertices and makes `p` adjacent to two or three of
  them, giving excess one or two.

For either type, if `g=|E_G(C,{t,q})|`, then the number of edges removed
from `F` is

```text
4|C|+delta(C)-g.
```

Here `(g,delta)=(2,1)` for the singleton and `g=3`,
`delta in {1,2}` for the edge.  This verifies equation (9) and the stronger
residual bound `|E(F-C)|>=4|V(F-C)|-7`.

## 5. The order-four atom and maximal-helper normal form

When `(F,Z)` is internally four-connected, Norin--Totschnig Lemma 12
applies at `|E(F)|=4|V(F)|-8` and supplies the rooted six-bag model.  If
the five-root pair is internally five-connected, the already audited
fifth-root augmentation lemma puts `p` in a helper and Lemma 5 applies.

Otherwise, any far component of a separation of `(F,Z union {p})` of
order at most four must contain `b`; a component avoiding `b` lies in `X`
and would give a cut of `G` of order at most four.  Its only neighbour
outside `F` is `q`.  The separator therefore has order four and lifts to
the exact five-cut `T union {q}`.  The surviving exterior
`{x,y,t}` joins every other rooted component, so this cut again has
exactly two complementary components.  The same order comparison gives
`|C|<=2`.

The singleton `{b}` has excess one.  In an edge `{b,c}`, minimum degree
makes `c` complete to all four adhesion vertices and makes `b` adjacent
to three or four of them.  Direct counting gives excess one or two.  Since
the only deleted edge from the atom to outside `F` is `bq`,

```text
|E(F-C)|=4|V(F-C)|-7-delta(C),
```

which is at least `4|V(F-C)|-9`.

Corollary 8 correctly strengthens this classification.  In an optimal
rooted six-bag model, the proof of the fifth-root augmentation lemma gives
exactly one helper-contact vertex in each root bag and no helper contact
from any unused component.  The connected helper union therefore has an
external neighbourhood of exactly four vertices, one in each root bag.
Internal five-connectivity of `(F,W)` forces `p` or `b` into that union;
target-freeness and Lemma 5 exclude `p`.

The order-four atom argument applies to this particular helper union, so
its order is at most two.  Two nonempty disjoint helpers rule out the
singleton, leaving singleton helpers `{b},{c}`.  In the excess-one edge
pattern, `b` sees adhesion vertices in only three distinct root bags and
therefore cannot itself be a helper.  Thus only the excess-two edge
survives, and both helpers are complete to all four adhesion vertices.

## 6. Synchronised rooted `K_4` and the six surviving rows

In Corollary 9, retain any actual root edge `z_kz_l` of `G[Z]` and absorb
the two singleton helpers into the two complementary root bags.  The
absorbed bags meet through `bc`; each meets both retained bags through
the four distinct adhesion portals; and the retained bags meet through
`z_kz_l`.  This is a `Z`-rooted `K_4` using the same six-bag model.

The proof that it can be made spanning is valid.  Every `X`-component
meets at least five vertices of `W`, so all `X`-components and at least
five boundary vertices lie in one component of `F`.  Any sixth boundary
vertex has at most four neighbours outside `F`; minimum degree therefore
puts it in the same component.  A minor model in a connected graph can be
extended over the remaining components to a spanning branch-set model.

If the bags containing the dense-side `b`, the anchor `p`, and the two
root neighbours of `q` are all distinct, `q` meets all four clique bags.
Together with `{x,t}` and `{y}`, this gives seven bags whose only possible
missing pair is `{y}`--`{q}`.

The positive table in Corollary 10 was checked directly.  It eliminates
exactly four of the six choices when `t` is a path end and exactly two of
the six choices when `t` lies in the `K_2`.  The only choices not closed by
the guaranteed adjacencies are therefore

```text
path end:    {a,c}, {a,d};
K_2 end:     {a,b}, {a,c}, {a,d}, {b,d}.
```

For the four positive path-end rows, the first has only the possible
`V`--`tq` omission and the other three have only the `x`--`y` omission.
For the two positive `K_2`-end rows, only `x`--`y` is absent.

The choice table in Corollary 11 was also checked row by row.  In every
row the retained pair is an actual edge of `G[Z]`, the root assigned to
the dense-side helper is outside `R_0`, and the displayed `B_*` root is
the unique fourth root.  If a spanning enlargement placed `p` in `B_*`,
then the contacts through `b`, `p`, and the two members of `R_0` would
occupy four distinct clique bags, invoking Corollary 9.  The nominated
fourth-bag obstruction is therefore exact.

## 7. Published rooted `K_{3,3}` input

The cited primary source was checked directly:

> L. K. Jørgensen and K. Kawarabayashi, *Extremal results for rooted minor
> problems*, Journal of Graph Theory **55** (2007), 191--207, Corollary 5.

Corollary 5 states that a three-connected graph `G` with
`e(G)>=4|G|-9` has a `K_{3,3}(X)` minor for any prescribed three-set `X`.
The graph `H` is three-connected because a cut of order at most two in
`H`, together with `x,y`, would be a cut of `G` of order at most four.
Thus the application at the three vertices of the `P_3` is legitimate.

If the two `K_2` roots occupy distinct helper bags, merge the third helper
into an endpoint root bag.  The two path edges complete the three rooted
bags to a triangle, the `K_2` edge joins the two occupied helpers, and the
rooted `K_{3,3}` contacts give every cross-edge.  This is an `S`-rooted
`K_5` model.  The paper does not prescribe those two additional helper
placements, so the source correctly records this as an open augmentation,
not as a closure.

## 8. Diagnostic verifier and scope

The diagnostic verifier ran to completion at source SHA-256

```text
e6a57e3efd140d9e7c143fe87467142fc6609d6758b25758fb985e3cd8db9263
```

and returned minimum branch-set defect two for each of the four abstract
portal-concentration quotients.  Its partition totals and connected
partition totals agree with its embedded independent checks.  The two
incidence variants of each edge atom intentionally contract to the same
quotient.  This is finite evidence only and is not used in the unbounded
proof.

The reduction proves neither `(E5)` nor the principal seven-connected
extremal target.  Its exact output is the two order-three atomic forms or
the single excess-two order-four normal form with the six listed root-pair
orientations and the nominated fourth-bag obstruction.  No unrooted minor,
arbitrary small side, or residual density bound is promoted beyond that
scope.
