# Boundary visibility of a spanning near-five model

**Status:** written proof; independently audited.  The theorem
is an unbounded composition result for a three-component order-six
separation.  It does not force the near-five model used in its hypothesis.

Let `G` be a six-connected graph with no `K_7^-` minor.  Let `S` be a
six-vertex cut such that `G-S` has three components `A,C,D`.  Each component
is adjacent to every vertex of `S`.

## Lemma 1 (five subsets of a six-set)

Let `H_1,...,H_5` be subsets of a six-set `S`, with

```text
union_i H_i=S.
```

If every `|H_i|>=2` and at most two of the sets have order two, then there is
a partition

```text
S=X disjoint union Y
```

such that both `X` and `Y` meet every `H_i`.

### Proof

Call a three-element set `X subseteq S` admissible if both `X` and `S-X`
meet every `H_i`.  There are twenty choices for `X`, with complementary
choices counted separately.  A set of order three is monochromatic for
exactly two choices, whilst a set of order at least four is never
monochromatic.

If none of the `H_i` has order two, at most ten of the twenty choices are
forbidden.  Suppose next that there is only one distinct two-set `P` among
the `H_i`.  There are twelve choices of `X` which split `P`.  Each remaining
set forbids at most two of them, so at most eight are forbidden.  This also
covers the case in which the same two-set occurs twice.

It remains to consider two distinct two-sets.  If they are disjoint, eight
choices of `X` split both of them.  Each of the other three sets forbids at
most two choices, leaving an admissible one.

Finally suppose the two-sets are `{a,b}` and `{a,c}`.  Put
`S={a,b,c,d,e,f}`.  Exactly six balanced choices split both two-sets.  A
remaining set can be monochromatic for one of these choices only if it is
one of the following complementary triples:

```text
{a,d,e} or {b,c,f},
{a,d,f} or {b,c,e},
{a,e,f} or {b,c,d}.                                  (1)
```

Unless the three remaining sets select one triple from each line of (1),
one of the six balanced choices is admissible.  In the exceptional case,
their union is all of `S` only when exactly one selected triple contains
`{b,c}`.  Relabel `d,e,f` so that it is `{b,c,f}`.  The other two selected
triples are then `{a,d,f}` and `{a,e,f}`.  The unbalanced partition

```text
X={b,c,d,e},             Y={a,f}
```

meets all five sets on both sides.  This proves the lemma. `\square`

## Theorem 2 (boundary-visibility alternative)

Suppose `G[C]` has a spanning `K_5^-` model with branch sets
`B_1,...,B_5`.  Then at least one of the following holds:

1. some `B_i` is adjacent to at most one vertex of `S`; or
2. at least three of the branch sets are each adjacent to at most two
   vertices of `S`.

The same conclusion holds for a spanning `K_5` model.

### Proof

Put

```text
H_i=N_G(B_i) intersect S.
```

Because the model spans `C` and `C` is adjacent to every vertex of `S`, the
five sets have union `S`.  Suppose that neither conclusion holds.  Every
`H_i` has order at least two and at most two have order two.  Lemma 1 gives
a partition `S=X disjoint union Y` meeting every `H_i` on both sides.

The seven sets

```text
B_1,...,B_5,          A union X,          D union Y
```

are pairwise disjoint and connected.  The last two are adjacent to every
`B_i` because `X` and `Y` meet every `H_i`.  They are adjacent to each
other because every vertex of `X` has a neighbour in the full component
`D`.  The first five sets have at most one missing adjacency.  The seven
sets therefore form a `K_7^-` model, contrary to the hypothesis on `G`.
`\square`

## Consequence and exact residue

Six-connectivity gives at least six vertices in the external neighbourhood
of every branch set.  Thus the first outcome has at least five such vertices
inside the other four model branch sets.  In the second outcome, each of
three branch sets has at least four external neighbours in the other model
branch sets.  The theorem does not distribute those vertices amongst
distinct branch sets and does not justify splitting a branch set.  That
simultaneous low-visibility normalisation is the remaining structural
problem for an ordinary `K_5^-`-minor approach to the sparse three-component
case.
