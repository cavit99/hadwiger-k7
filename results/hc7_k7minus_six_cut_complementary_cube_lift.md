# Complementary response families at a six-cut

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_six_cut_complementary_cube_lift_audit.md).
This note treats the remaining crossing rows of the six-coordinate
induced-forest host.  It gives a common bounded separator and the exact first
unsupported colour-synchronisation step.  It does not prove the `K_7^-`
six-colour conjecture or `HC_7`.

## 1. Setting

Let `G` be a minor-minimal non-six-colourable graph and let `F` be the
six-edge componentwise-induced forest supplied by the audited
[six-coordinate reduction](hc7_k7minus_six_coordinate_forest_reduction.md).
Put

\[
                              X=G-F.                 \tag{1.1}
\]

Thus `X` is six-connected, every nonempty subset `J subseteq F` is realised as
the exact equality signature of a proper six-colouring `c_J` of `X`, and
an empty signature would six-colour `G`.

Suppose that `S` is a cut of order six in `X`.  The cited reduction gives
exactly two components `C,D` of `X-S`, both full to `S`.  Its two selected
edges `a,b` cross between `C,D`.

For a colouring `c` and a vertex set `T`, write `Pi_T(c)` for the partition
of `T` into the nonempty colour classes induced by `c`.  This notation
forgets the names of the colours.

Whenever `V(G)=A\mathbin{\dot\cup}T\mathbin{\dot\cup}B` with `A,B`
anticomplete, say that a partition of `T` **extends through `A`** if there
is a proper six-colouring of `G[A\cup T]` inducing that partition on `T`.
Otherwise the partition is **rejected by `A`**.  Define extension through
`B` symmetrically.

## 2. The matching rows

Suppose first that `F` is a matching.  Let

\[
                  E=\{uv\in F:u\in C, v\in D\},
                  \qquad q=|E|.                     \tag{2.1}
\]

Here `q>=2`; the present application is the previously untreated range
`q>=3`.

### Theorem 2.1 (complementary matching-cube lift)

For every partition

\[
                         E=E_C\mathbin{\dot\cup}E_D,
                         \qquad E_C,E_D\ne\varnothing,          \tag{2.2}
\]

there is a vertex set `T` of order `6+q` and a partition

\[
                         V(G)=C'\mathbin{\dot\cup}T
                                  \mathbin{\dot\cup}D'          \tag{2.3}
\]

such that:

1. `C',D'` are nonempty and anticomplete;
2. for every nonempty `J subseteq E_C`, the restriction of `c_J` to
   `G-C'` is a proper six-colouring whose boundary partition on `T` does
   not extend through `C'`;
3. for every nonempty `J subseteq E_D`, the restriction of `c_J` to
   `G-D'` is a proper six-colouring whose boundary partition on `T` does
   not extend through `D'`; and
4. no partition arising in item 2 equals a partition arising in item 3.

Consequently every matching row with `3<=q<=6` returns one common actual
two-sided separator of order between nine and twelve, carrying two
complementary nonempty response families.  One may choose (2.2) so that
their indexing cubes have dimensions `floor(q/2)` and `ceil(q/2)`.

#### Proof

For each edge `e in E_C`, put its end in `D` into `T`; for each edge
`e in E_D`, put its end in `C` into `T`.  Add all six vertices of `S` to
`T`, and let `C',D'` be the vertices left in `C,D`, respectively.  The
selected matching ends are distinct, so `|T|=6+q`.

Every edge from `C` to `D` in `G` belongs to `E`, because no such edge is
present in `X`.  The selection meets every edge of `E`, so `C'` and `D'`
are anticomplete.  A `C`-end of an edge in `E_C` remains in `C'`, while a
`D`-end of an edge in `E_D` remains in `D'`.  Since both parts of (2.2)
are nonempty, both open sets are nonempty.  This proves item 1.

Fix nonempty `J subseteq E_C`.  In `c_J`, precisely the edges of `J` have
equal-coloured ends.  Each such edge has its `C`-end in `C'`, so deleting
`C'` removes every monochromatic edge when all edges of `F` are restored.
Every edge of `F-J` is bichromatic.  Hence `c_J` restricts to a proper
six-colouring of `G-C'`.  If its partition on `T` extended through `C'`,
a permutation of the six colour names would make the extension and the
exterior colouring agree pointwise on `T`; gluing them would six-colour
`G`.  This proves item 2.  The proof of item 3 is symmetric.

Finally, suppose that colourings from items 2 and 3 induced the same
partition of `T`.  Permute the colour names in one colouring so that the
two colourings agree pointwise on `T`.  Use the colouring of `G-C'` on
`D' union T` and the colouring of `G-D'` on `C'`.  These assignments are
proper within both closed sides, agree on `T`, and there is no edge from
`C'` to `D'`.  They therefore give a proper six-colouring of `G`, a
contradiction.  This proves item 4. `\square`

The response families in Theorem 2.1 are indexed by all nonempty subsets
of the two displayed edge sets.  The theorem does **not** say that different
indices induce different partitions of `T`; several cube vertices may
collapse to the same boundary partition.

## 3. The induced-path row

Suppose now that

\[
                         F=M_0\cup\{rx,ry\},          \tag{3.1}
\]

where `M_0` is a matching of order four, disjoint from the induced path
`x-r-y`.  Orient the shores so that `r in C` and `x,y in D`.  Let

\[
              E_0=\{uv\in M_0:u\in C, v\in D\},
              \qquad k=|E_0|.                       \tag{3.2}
\]

The clean row `k=0` is Corollary 3.3 of the cited reduction.  Here we treat
`k>=1`.

### Theorem 3.1 (path-versus-matching response lift)

Assume `k>=1` and `C\ne\{r\}`.  There is a set `T` of order `7+k<=11` and
a partition

\[
                         V(G)=C'\mathbin{\dot\cup}T
                                  \mathbin{\dot\cup}D'          \tag{3.3}
\]

such that:

1. `C',D'` are nonempty and anticomplete;
2. for every nonempty `J subseteq E_0`, the restriction of `c_J` to
   `G-C'` is proper and gives a rejected boundary partition on `T` for
   `C'`;
3. for each nonempty `J subseteq {rx,ry}`, the restriction of `c_J` to
   `G-D'` is proper and gives a rejected boundary partition on `T` for
   `D'`; and
4. the two families of boundary partitions are disjoint.

The excluded case `C={r}` is exactly the degree-eight singleton of the
six-coordinate reduction: its neighbourhood has the multiplicity pattern
`2,2,1,1,1,1`, and deleting any one of the five original star leaves from
that neighbourhood leaves a graph with no `K_5^-` minor.

#### Proof

For each edge of `E_0`, put its end in `D` into `T`, and put

\[
                              T=S\cup\{r\}
                                \cup\{\text{the selected `D`-ends}\}.
                                                                  \tag{3.4}
\]

Set `C'=C-{r}` and remove the selected ends from `D` to form `D'`.  The
sets in (3.3) partition `V(G)` and `|T|=7+k`.  The set `C'` is nonempty by
hypothesis.  Both `x,y` remain in `D'`, so `D'` is nonempty.

Every edge of `G` from `C` to `D` belongs either to `E_0` or to
`{rx,ry}`.  The selected `D`-ends meet the former edges and `r` meets the
latter two, so `C',D'` are anticomplete.

If `J` is a nonempty subset of `E_0`, every monochromatic forest edge in
`c_J` has its `C`-end in `C'`; hence the restriction to `G-C'` is proper.
If instead `J` is a nonempty subset of `{rx,ry}`, every monochromatic edge
has its leaf end in `D'`; hence the restriction to `G-D'` is proper.  In
either case an extension of the induced boundary partition would glue to
six-colour `G`, so the partitions are rejected.

If one partition occurred in both families, align its colour names on `T`
and glue across the anticomplete open sets exactly as in Theorem 2.1.  This
would again six-colour `G`, proving item 4. `\square`

## 4. Exact remaining implication

Theorems 2.1 and 3.1 eliminate the geometric uncertainty in the remaining
six-cut rows.  They do not eliminate the rows themselves.  The first
unsupported implication is now the following bounded synchronisation
statement.

> **Complementary-cube synchronisation target.**  In the critical host, at
> a separator `T` produced above, the two complementary response families
> cannot induce disjoint sets of partitions of `T`.

This is not a counting statement.  The exact forest cube lives on `X`, but
after one endpoint of every crossing edge is moved into `T`, the equality
on that edge is no longer directly visible as an equality between two
vertices of `T`.  Thus different signatures may induce the same boundary
partition, and the cube cardinality cannot be compared with a Bell number
to force intersection.

Nor may one invoke the earlier order-eight machinery without additional
hypotheses.  The matching rows here have order `9` through `12`; the
induced-path rows have order `8` through `11`; their boundary vertices need
not be full to every component after selected endpoints are removed.  A
valid terminal theorem must exploit the common origin of the two families
in one componentwise-induced forest cube, or return a smaller exact
response-bearing separator.  Abstract partition enumeration alone does
not supply that conclusion.

## Dependencies and scope

The only substantive input is the audited
[six-coordinate induced-forest reduction](hc7_k7minus_six_coordinate_forest_reduction.md),
including its exact punctured forest cube and its six-cut classification.
The gluing argument is elementary and uses equality partitions rather than
fixed colour names.

The result is unbounded in the orders of `C,D`; the displayed separator
orders are bounded because the forest has six edges.  No finite
enumeration is used.
