# Palette surjectivity does not force edges in the terminal set

**Status:** scoped deterministic falsifier.  The verifier is
[`hc7_k7minus_palette_static_consequence_barrier_verify.py`](hc7_k7minus_palette_static_consequence_barrier_verify.py).

This note tests proposed edge or clique deductions from connectivity,
coefficient-four density, and the universal five-colour palette condition.
The examples contain a literal `K_7^-`.  They therefore do **not** refute
any argument that uses `K_7^-`-minor exclusion or another contraction-origin
constraint.

## Construction

Let `A_0,...,A_4` be five independent pairs, with every edge between
distinct pairs present.  Thus their union induces `K_{2,2,2,2,2}`.  Let
`T` be an independent seven-set and choose a surjection

```text
a:T->{0,1,2,3,4}.
```

A terminal `t` is adjacent to every core vertex outside `A_{a(t)}` and to
no vertex of `A_{a(t)}`.  Finally add a vertex `w` complete to every other
vertex.  Denote the resulting graph by `H_a`.

We use either of the assignment multiplicities

```text
(3,1,1,1,1)  or  (2,2,1,1,1).
```

In both cases

```text
|V(H_a)|=18,       |E(H_a)|=113>4|V(H_a)|,
kappa(H_a)=9,      chi(H_a)=6,
```

and `H_a[T]` is empty.  Indeed, deleting the nine neighbours of a terminal
isolates it.  Conversely, deletion of at most eight vertices leaves `w`,
or deletes `w` and at most seven further vertices.  In the latter case at
least three core vertices remain in at least two parts, so the remaining
core is connected, and every remaining terminal still has a core neighbour.
Thus the connectivity is exactly nine.

The vertex `w` together with one vertex from each core pair forms a `K_6`,
so six colours are necessary and sufficient.  In every proper six-colouring,
`w` has its own colour.  The five core pairs must use the other five colours,
one distinct colour per pair.  A terminal assigned to `A_i` is adjacent to
all four other core colours and to `w`, so it is forced to take the colour
of `A_i`.  Hence `T` uses every colour other than the colour of `w`, with
exactly the chosen multiplicity profile, despite spanning no edge.

Finally, take `w`, one representative of each core pair, and a terminal
assigned to the first pair.  These seven vertices induce `K_7^-`, whose
only missing edge joins that terminal to the representative of its assigned
pair.

## Consequence

Even nine-connectivity and density far above `4n` do not make the universal
five-colour palette condition force a single edge in `T`, and hence do not
force a nontrivial clique wholly inside `T`.  The palette condition does
retain dynamic Kempe content: if a colour occurs once on `T`, its singleton
terminal must share a bichromatic Kempe component with `T` in every other
non-`w` colour, since otherwise a swap would remove that colour from `T`.
A stronger conclusion must use additional information, such as this Kempe
dynamics, target exclusion, or a contraction-origin constraint.
