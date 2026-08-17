# The order-seven `i=4` Hall return is terminal

**Status:** proved by a fourteen-row incidence lemma and independently
cold-audited.  No excess, relative-connectivity, or packet hypothesis is
needed after the Hall return.

## 1. Two general consequences of the Hall profile

Let a seven-vertex shore have a spanning ordinary `K_5^-` model, and let
`U` be an inclusion-minimal Hall-deficient family of `i>=2` singleton model
bags.  Put

```text
R=N_S(U),   W=C-U,   T=S-R.
```

The order-seven Hall profile gives `|R|=i-1`, `|W|=|T|=7-i`, a perfect
matching from `W` to `T`, and, for every `u in U`, a perfect matching from
`U-{u}` to `R`.

### Lemma 1.1 (overlapping minor-free deletions)

If there is no punctured `S`-rooted `K_5^-` model, then `C-u` is
ordinary-`K_5^-`-minor-free for every `u in U`.

### Proof

Combine the two matchings above.  They match all six vertices of `C-u` to
the six distinct roots.  If `C-u` had an ordinary `K_5^-` model, choose one
vertex from each of its five branch bags and attach the five distinct matched
roots.  This roots the old model and contradicts the hypothesis.  \(\square\)

### Lemma 1.2 (the order-six edge bound and its equality graph)

An ordinary-`K_5^-`-minor-free graph on six vertices has at most eleven
edges.  At equality it is uniquely

```text
K_2 join 2K_2,
```

with degree sequence `5,5,3,3,3,3`.

### Proof

With at least thirteen edges, deleting a minimum-degree vertex leaves at
least nine edges on five vertices, hence a literal `K_5^-`.  The same holds
at twelve edges unless the graph is four-regular.  The exceptional
four-regular graph is `K_{2,2,2}`; contracting an edge between two parts
gives a `K_5^-` model.  Thus eleven is the maximum.

At eleven edges, deletion of any vertex must leave at most eight edges, so
every degree is at least three.  The complement consequently has four edges
and maximum degree at most two.  Up to isomorphism it is one of

```text
C_4+2K_1,  C_3+K_2+K_1,  P_5+K_1,  P_4+K_2,  P_3+P_3.
```

In each of the last four cases, contract in the original graph respectively
an edge joining: an endpoint of the `K_2` to a triangle vertex; the second
and fourth path vertices; an internal `P_4` vertex to a `K_2` endpoint; or
the two path centres.  The four remaining singleton bags have at most one
missing contact.  These are `K_5^-` models.  The sole survivor has complement
`C_4+2K_1`, equivalently it is `K_2 join 2K_2`.  It has no five-vertex
near-clique.  Moreover, the only two-vertex bags available in a spanning
five-bag model either leave at least two edges of the complementary `C_4`,
or join opposite cycle vertices and then miss both remaining cycle vertices.
Thus it is indeed minor-free.  \(\square\)

### Corollary 1.3 (the `i=4` internal edge ceiling)

Under target exclusion and `i=4`, one has `e(C)<=15`.

### Proof

Lemma 1.1 and Lemma 1.2 give

```text
e(C)-d_C(u)<=11                    (u in U).
```

Thus `e(C)<=17`.  Equality would make all four vertices of `U` universal,
already giving the six edges in `U` and all twelve edges from `U` to `W`, a
contradiction.

Suppose `e(C)=16`.  Write `a=e(U)`, `b=e(U,W)` and `c=e(W)`.  The fifth
model bag `W` is connected, so `c>=2`.  Every `u in U` has degree at least
five, and hence

```text
20 <= sum_{u in U}d_C(u)=2a+b=a+16-c.
```

Since `a<=6`, equality is forced throughout: `a=6`, `c=2`, `b=8`, and every
vertex of `U` has degree five.  For distinct `u,v in U`, the degree of `v`
in `C-u` is therefore four.  But `C-u` has eleven edges and Lemma 1.2 says
that its degrees are only five and three.  This contradiction proves the
claim.  \(\square\)

## 2. The four-plus-three allocation lemma

### Lemma 2.1

Let `U={0,1,2,3}` and let `W={x_0,x_1,x_2}` induce the path
`x_0 x_1 x_2`.  Suppose

1. `U` induces `K_4` or `K_4-01`;
2. every `x_j` has a neighbour in `U`; and
3. the number of missing edges inside `U` plus the number of vertices of
   `U` with no neighbour in `W` is at most one.

Assume that, after any chosen `u in U` is left unmatched, `U-{u}` has three
distinct roots, while `x_0,x_1,x_2` have three further distinct roots.  Then
there is a punctured rooted `K_5^-` model.

### Proof

Delete `U`--`W` edges until the two incidence conditions are
inclusion-minimal.  Permutations of `U` (preserving the pair `01` in the
second case) and reversal of the path leave three minimal orbits for `K_4`
and eleven for `K_4-01`.

In the table, `12/0/0/-` records the four neighbourhoods in `W`: vertex `0`
sees `x_1,x_2`, vertices `1,2` see `x_0`, and vertex `3` sees none.  An entry
`x_1:x_0` is a bag rooted through the matched vertex `x_1` and additionally
containing `x_0`.  The column `u;o` gives the unmatched `U` vertex and the
matched vertex whose root is omitted.  The last column lists the sole
possible missing contact.

| `U` | neighbourhoods | `u;o` | five rooted internal parts | possible miss |
|---|---|---|---|---|
| `K_4` | `12/0/0/-` | `0;x_0` | `1 \| 2 \| 3 \| x_1:x_0 \| x_2:0` | `3,x_1` |
| `K_4` | `2/1/0/-` | `0;2` | `1 \| 3 \| x_0:2 \| x_1 \| x_2:0` | `3,x_1` |
| `K_4` | `02/1/1/-` | `0;x_0` | `1 \| 2 \| 3 \| x_1 \| x_2:0` | `3,x_1` |
| `K_4-01` | `12/0/0/0` | `0;x_0` | `1 \| 2 \| 3 \| x_1:x_0 \| x_2:0` | `1,x_2` |
| `K_4-01` | `2/1/0/0` | `0;1` | `2 \| 3 \| x_0 \| x_1:1 \| x_2:0` | `x_0,x_2` |
| `K_4-01` | `2/0/1/0` | `0;x_0` | `1 \| 2 \| 3 \| x_1:x_0 \| x_2:0` | `1,x_2` |
| `K_4-01` | `2/1/1/0` | `0;3` | `1 \| 2 \| x_0:3 \| x_1 \| x_2:0` | `1,x_2` |
| `K_4-01` | `2/2/1/0` | `0;3` | `1 \| 2 \| x_0:3 \| x_1 \| x_2:0` | `1,x_1` |
| `K_4-01` | `1/0/2/0` | `2;x_0` | `0 \| 1 \| 3 \| x_1:x_0 \| x_2:2` | `0,1` |
| `K_4-01` | `1/1/2/0` | `2;3` | `0 \| 1 \| x_0:3 \| x_1 \| x_2:2` | `0,1` |
| `K_4-01` | `0/0/12/0` | `2;x_0` | `0 \| 1 \| 3 \| x_1:x_0 \| x_2:2` | `0,1` |
| `K_4-01` | `2/0/1/1` | `0;1` | `2 \| 3 \| x_0:1 \| x_1 \| x_2:0` | `x_0,x_2` |
| `K_4-01` | `02/1/1/1` | `0;x_0` | `1 \| 2 \| 3 \| x_1 \| x_2:0` | `1,x_2` |
| `K_4-01` | `1/1/02/1` | `2;x_0` | `0 \| 1 \| 3 \| x_1 \| x_2:2` | `0,1` |

Every displayed part is connected, the five parts are disjoint, and all but
the listed pair contact.  The root convention is legal because the three
vertices of `U-{u}` can first be matched to their roots; if one of them is
`o`, its root is simply omitted.  The same applies to the three matched
vertices of `W`.  The fourteen incidence orbits are exhaustive, and adding
back deleted edges preserves the model.  \(\square\)

## 3. Terminal order-seven consequence

In the `i=4` Hall return, the four deficient model bags are the singleton
set `U` and the remaining three vertices form the connected fifth bag `W`.
The original five-bag quotient gives item 3 of Lemma 2.1, while
`N_C(U)=C-U` gives item 2.  Replace `W` by any spanning path and apply the
lemma with the Hall matchings from Section 1.  Thus the return always has a
punctured rooted `K_5^-` model.  The `i=4` row is terminal even without the
excess threshold.

## 4. Reproduction

Run

```text
python active/experiments/sparse_sixcut_order_seven_i4_completion/verify.py
```

The standard-library checker reconstructs the three and eleven orbit
partitions, verifies every displayed bag, and checks that every valid
incidence mask contains a displayed minimal mask.  Its terminal line is

```text
order-seven i=4 completion table: PASS
```
