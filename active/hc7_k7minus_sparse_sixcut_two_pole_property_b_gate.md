# Two-pole completion of a spanning near-five model

**Status:** proved unbounded composition gate.  A spanning `K_5^-` model
in one lobe of a three-component six-cut is terminal unless one of its
branch bags sees at most two boundary vertices.  This does not force such a
model, nor does it eliminate the resulting low-visibility bag.

Let `G` be a six-connected graph with no `K_7^-` minor.  Let `S` be a cut
of order six such that `G-S` has three components `A,C,D`.  Six-connectivity
gives

```text
N_G(A)=N_G(C)=N_G(D)=S.                              (1)
```

## Lemma 1 (five large subsets of a six-set have property B)

If `H_1,...,H_5` are subsets of a six-set `S` and `|H_i|>=3` for every
`i`, there is a partition

```text
S=X disjoint union Y,        |X|=|Y|=3,              (2)
```

such that both `X` and `Y` meet every `H_i`.

### Proof

Choose a labelled three--three partition uniformly from the twenty choices
of `X`.  A fixed three-set is monochromatic for exactly two choices, and a
set of order at least four is never monochromatic.  Hence the probability
that some `H_i` is monochromatic is at most

```text
5 * 2/20 = 1/2.
```

Some partition has no monochromatic `H_i`, which is exactly (2). `\square`

## Theorem 2 (two-pole completion)

Suppose `G[C]` has a spanning `K_5^-` model with branch bags

```text
B_1,...,B_5,        C=disjoint union_i B_i.          (3)
```

Put

```text
H_i=N_G(B_i) intersect S.                            (4)
```

If every `|H_i|>=3`, then `G` contains a `K_7^-` minor.  Consequently, in
a target-free host every spanning `K_5^-` model has a branch bag `B_i`
with

```text
|N_G(B_i) intersect S|<=2.                           (5)
```

### Proof

Apply Lemma 1 to obtain `S=X disjoint union Y` meeting every set in (4).
The seven sets

```text
B_1,...,B_5,        A union X,        D union Y       (6)
```

are pairwise disjoint and connected.  The first five have at most one
missing adjacency.  Each of the last two bags meets every `B_i`, using a
literal vertex of `X intersect H_i` or `Y intersect H_i`.  Finally,
`A union X` is adjacent to `D union Y`: for any `x in X`, fullness of `D`
gives an edge from `x` to `D`.  Thus the seven bags in (6) have at most the
one missing adjacency inherited from the near-five model.  They form a
`K_7^-` model, a contradiction. `\square`

The argument also works for a spanning `K_5` model.  It uses no boundary
edge and no virtual completion.

The same random partition gives a slightly sharper obstruction.  A fixed
two-set is monochromatic for eight of the twenty labelled balanced
partitions.  Hence one two-set and four sets of order at least three have
total bad probability at most

```text
8/20 + 4 * 2/20 = 4/5.
```

Consequently, every target-free spanning near-five model either has a bag
with at most one boundary neighbour, or has at least two bags with at most
two boundary neighbours.  This strengthening will be useful when the
low-visibility bags are normalised simultaneously.

## Lemma 3 (six distinct boundary representatives)

If `|C|>=6`, the bipartite incidence graph between `S` and `C`, with an
edge for each edge of `G` joining the two sets, has a matching saturating
`S`.

### Proof

Suppose Hall's condition fails for `X subseteq S`.  Then

```text
|N_C(X)|<|X|.
```

Delete

```text
N_C(X) union (S-X).                                  (7)
```

The set in (7) has order at most five.  The set `C-N_C(X)` is nonempty,
because `|C|>=6`, and it has no edge to `X` by definition.  Every edge from
it to another component of `G-S` would have to pass through `S-X`.
Therefore (7) separates `C-N_C(X)` from `X` and from the two other full
components, contrary to six-connectivity.  Hall's condition holds.
`\square`

## Corollary 4 (the literal five-vertex row)

If `|C|=5` and `G[C]` contains `K_5^-` as a spanning subgraph, then for
some `x in S` the closed shore `G[C union (S-{x})]` contains an
`(S-{x})`-rooted `K_5^-` model.  Hence this row is impossible in the
returned three-component cut.

### Proof

It is enough to find a matching from the five vertices of `C` into `S`.
For nonempty `U subseteq C`, relative six-connectivity gives

```text
|N_S(U)| >= 6-|N_C(U)-U|.                            (8)
```

Since `C` has five vertices,

```text
|N_C(U)-U|<=5-|U|,
```

so the right side of (8) is at least `|U|+1` for every nonempty `U`.
Hall's theorem therefore matches all five vertices of `C` to distinct roots.
Adjoin each matched root to its matched singleton branch bag and omit the
sixth root. `\square`

## Exact remaining gate

Theorem 2 reduces an ordinary-minor approach to a precise obstruction.  A
maximum-visibility spanning `K_5^-` model in a target-free lobe has a bag
with at most two boundary neighbours.  Six-connectivity still gives that
bag at least six **vertices** in its full external neighbourhood, so at
least four lie in the other model bags.  Those vertices need not lie one
per bag, and the low-visibility bag may have arbitrary order.  Turning this
boundary multiplicity into a safe split or an exact-six fragment is the
unproved next step; no such transfer is asserted here.
