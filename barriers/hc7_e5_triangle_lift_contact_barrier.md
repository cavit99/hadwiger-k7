# Two full components do not close the lifted triangle quotient

**Status:** barrier/counterexample to an intermediate contact-quotient
claim; computation-free written proof with a
[separate internal audit](hc7_e5_triangle_lift_contact_barrier_audit.md).
This is not a counterexample to `(E5)` or to the primary seven-connected
theorem.

## Refuted intermediate claim

The following local implication is false.

> Let `T` and `R` be disjoint three-sets in a graph, with both `T` and
> `R` inducing triangles.  Suppose that two nonadjacent component vertices
> are each complete to `T union R`, and that one member of `R` is complete
> to `T`.  Then these contacts force a `K_7^-` minor.

The counterexample below makes both component vertices adjacent to all
three vertices of `T`, rather than merely the two contacts available in
the motivating lifted six-separation.

## Counterexample

Put

```text
T={p,t,q},                         R={r_1,r_2,r_3},
```

and add two vertices `c_1,c_2`.  Define the graph `Q` by the following
complete edge list in structural form:

- `Q[T]` and `Q[R]` are triangles;
- `c_1,c_2` are nonadjacent and each is complete to `T union R`;
- `r_1` is complete to `T`; and
- there are no edges from `{r_2,r_3}` to `T`.

Thus

```text
|V(Q)|=8,                          |E(Q)|=3+3+12+3=21.
```

Each triangle vertex has exactly three neighbours outside `T`, namely
`c_1,c_2,r_1`.  The construction is therefore compatible with the
three-neighbour capacity inherited from the exact singleton
neighbourhoods after the triangle is contracted.

## Theorem

The graph `Q` has no `K_7^-` minor.

### Proof

A `K_7^-`-minor model has seven pairwise disjoint nonempty connected
branch sets.  Since `Q` has eight vertices, such a model uses either seven
or eight vertices.

If it uses seven vertices, every branch set is a singleton and one vertex
of `Q` is unused.  The minimum degree of `Q` is four, so the seven used
vertices induce at most

```text
21-4=17
```

edges.  This is fewer than the twenty adjacencies required by `K_7^-`.

If the model uses all eight vertices, exactly one branch set has order two
and the other six are singletons.  The two-vertex branch set is connected,
so its vertices are the ends of an edge `uv`.  Contracting `uv` turns the
putative model into a seven-vertex graph containing `K_7^-`.

Every edge of `Q` has at least two common neighbours.  This follows by
edge type:

- an edge in `T` has the third member of `T` and both `c_i` as common
  neighbours;
- an edge in `R` has the third member of `R` and both `c_i`;
- an edge from `c_i` to `T` has the other two members of `T`;
- an edge from `c_i` to `R` has the other two members of `R`; and
- an edge from `r_1` to `T` has both `c_i`.

Consequently contracting any edge loses that edge and at least two
duplicate incidences.  The resulting seven-vertex graph has at most

```text
21-3=18
```

edges, again fewer than the twenty edges of `K_7^-`.  Both possible model
orders are impossible.  \(\square\)

## Exact scope

This graph refutes only an inference from the contracted contact pattern.
The vertices `c_1,c_2` represent whole connected components as single
vertices; the construction retains none of their internal structure and
does not rule out splitting an actual component into several branch sets.

Moreover, `Q` is not a five-connected host: its minimum degree is four.
It also lies below the `E5` density threshold,

```text
21<4(8)-7=25.
```

It is not asserted to arise from a minimum `E5` enemy.  Thus it does not
refute the triangle-contraction reduction, `(E5)`, or the primary
seven-connected `4n-2` target.  It shows that two full complementary
components and the displayed boundary edges cannot by themselves upgrade
the lifted six-separation to a `K_7^-` model.
