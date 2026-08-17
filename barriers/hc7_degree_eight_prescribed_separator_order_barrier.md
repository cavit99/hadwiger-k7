# A degree-eight barrier to bounding a prescribed separator

**Status:** barrier/counterexample to the intermediate assertion stated
below; computation-free written proof.  This note is not a counterexample to
any target-free or chromatic-critical statement.

## 1. The assertion refuted

For a graph `G` and a vertex `v`, let

```text
lambda_G(v) = min |N_G(R)|,
```

where the minimum is over all nonempty sets `R` such that

1. `G[R]` is connected;
2. `v` belongs to `N_G(R)`; and
3. `V(G) - (R union N_G(R))` is nonempty.

Thus `N_G(R)` is an actual separator whose boundary contains the prescribed
vertex `v`.  The construction below refutes each of the following possible
inferences from connectivity, degree and separator-side minimality alone:

- `lambda_G(v)=7` in every seven-connected graph with `d_G(v)=8`;
- `lambda_G(v)<=8` under those hypotheses; and
- more generally, `lambda_G(v)` is bounded by any absolute constant under
  those hypotheses.

It also shows that requiring every component behind the chosen boundary to
be full does not repair any of these assertions.

## 2. Construction and exact value

**Theorem 2.1 (written barrier).**  For every integer `n>=8`, let
`G_n=K_{8,n}` with bipartition `(A,B)`, where `|A|=8` and `|B|=n`, and fix
`v in B`.  Then

```text
kappa(G_n)=8,       d_G_n(v)=8,       lambda_G_n(v)=n.
```

Moreover, every component of `G_n-B` has neighbourhood exactly `B`.

**Proof.**  Deleting fewer than eight vertices leaves at least one vertex of
each bipartition class, and the remaining complete bipartite graph is
connected.  Deleting all eight vertices of `A` leaves the independent set
`B`, which has at least two vertices.  Hence `kappa(G_n)=8`.  The degree of
each vertex of `B`, in particular `v`, is eight.

Let `R` be any set admitted in the definition of `lambda_G_n(v)`.  Since
`v in B` has neighbours only in `A`, the set `R` contains a vertex `a in A`.
If `R` also contains a vertex `b in B`, then every vertex of `B-R` is
adjacent to `a` and every vertex of `A-R` is adjacent to `b`.  Consequently

```text
N_G_n(R)=V(G_n)-R,
```

contrary to the required nonempty far side.  Thus `R` is contained in `A`.
The set `A` is independent, so connectedness and nonemptiness force
`R={a}`.  It follows that `N_G_n(R)=B`, of order `n`.  Conversely, every
singleton `{a}` with `a in A` is admissible: its boundary is `B`, contains
`v`, and its far side is the nonempty set `A-{a}`.  Therefore
`lambda_G_n(v)=n`.

Finally, the components of `G_n-B` are the eight singleton vertices of
`A`, and every one is adjacent to every vertex of `B`.  They are all
`B`-full.  This proves the theorem.  `square`

## 3. Exact scope

The example leaves no route from seven-connectivity, `d(v)=8`, minimality of
a separator side containing `v` in its boundary, and boundary fullness to
an order-seven or even bounded-order separator containing `v`.  A positive
descent must use an additional critical-host input, such as exclusion of a
`K_7^-` minor or a colouring constraint, before it can bound the prescribed
boundary.

This construction deliberately does not satisfy those additional inputs.
For `n>=8`, choose distinct `a_1,...,a_7 in A` and distinct
`b_1,...,b_7 in B`.  The seven disjoint connected sets

```text
{a_i,b_i},  1<=i<=7,
```

are pairwise adjacent and hence form a `K_7`-minor model.  Thus `G_n`
contains a `K_7^-` minor, and it is bipartite rather than seven-chromatic.
The graph also has the unrooted order-eight separator `A`; the barrier is
specifically to bounding separators required to contain the nominated
degree-eight vertex `v`.
