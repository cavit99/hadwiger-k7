# Internal audit: lifted-triangle contact barrier

**Verdict:** **GREEN** for the pinned source revision.  This is a separate
internal mathematical audit, not external peer review.

**Audited source:**
`barriers/hc7_e5_triangle_lift_contact_barrier.md`

**SHA-256:**
`cf0fef6c5fb1824f08683bb7451745499dabce9fcd87702ce800d1046ad28d83`

No mathematical correction is required at this revision.  The proof is
computation-free.

Relative to the previously audited revision
`513e74d2c43f2bd94ef72589145149b88f3a67ac62537acb49383c5fcfa37dd9`,
the source changes only its status text to link this adjacent audit.  The
counterexample, proof and scope are unchanged.

## 1. Graph definition, size and capacity

The vertex partition is

```text
T={p,t,q},              R={r_1,r_2,r_3},              {c_1,c_2}.
```

The complete edge specification consists of:

- three edges in each of the two triangles;
- twelve edges from `c_1,c_2` to the six vertices of `T union R`;
- three edges from `r_1` to `T`; and
- no further edges.

These classes are disjoint, so the order and size are exactly

```text
|V(Q)|=8,                         |E(Q)|=3+3+12+3=21.
```

The degrees are

```text
d(p)=d(t)=d(q)=5,        d(r_1)=7,
d(r_2)=d(r_3)=4,         d(c_1)=d(c_2)=6.
```

In particular the minimum degree is four.  Each vertex of the designated
triangle `T` has exactly the three exterior neighbours `c_1,c_2,r_1`.
Thus the quotient respects the stated three-neighbour capacity.  The two
component vertices are nonadjacent and complete to `T union R`, while
`r_1` is complete to `T`; hence every hypothesis of the refuted local
claim is realised.

## 2. Exhaustion of possible seven-bag models

A `K_7^-` model has seven nonempty, pairwise disjoint branch sets.  Since
`Q` has only eight vertices, the union of those bags has order seven or
eight; no other order is possible.

If seven vertices are used, all seven bags are singletons.  Omitting a
vertex deletes at least its degree, which is at least four, from the
twenty-one-edge graph.  The seven used vertices therefore induce at most

```text
21-4=17
```

edges.  Singleton branch sets require one literal edge for every model
adjacency, whereas `K_7^-` has twenty edges.  This case is impossible.

If all eight vertices are used, the bag orders sum to eight.  Exactly one
bag consequently has order two and the other six are singletons.  The
two-vertex bag must be connected, so its two vertices are the ends of an
edge `uv`.  Contracting that edge turns the proposed seven bags into seven
singleton bags in `Q/uv`.  The contracted graph would therefore have to
contain at least the twenty edges of `K_7^-`.

This covers models using seven vertices, models using eight vertices, and
all possible placements of the unique non-singleton bag.

## 3. Common neighbours and contraction bound

Every possible edge type has at least two common neighbours.

- An edge of `T` has the third vertex of `T` and both `c_i`.
- An edge of `R` has the third vertex of `R` and both `c_i`.
- An edge from `c_i` to `T` has the other two vertices of `T`.
- An edge from `c_i` to `R` has the other two vertices of `R`.
- An edge from `r_1` to `T` has both `c_i`.

The structural edge list contains no other edge type.  In a simple graph,
contracting `uv` removes `uv` and one duplicate edge for every common
neighbour of `u,v`.  Hence

```text
|E(Q/uv)|<=21-1-2=18.
```

This contradicts the twenty-edge requirement from the all-eight-vertices
case.  Together with the preceding deletion bound, it proves that `Q` has
no `K_7^-` minor.

## 4. Exact scope

The construction is an explicit counterexample to the stated
contact-quotient implication, rather than merely a failed proof route.  It
does not extend to a host-level counterexample:

- `c_1,c_2` stand for whole connected components after contraction, so the
  quotient discards internal vertices that an actual host model might split
  among several branch sets;
- the minimum degree of `Q` is four, so `Q` is not five-connected; and
- `|E(Q)|=21<25=4|V(Q)|-7`, so it misses the `E5` density threshold.

Accordingly the barrier refutes neither the singleton-triangle contraction
reduction nor `(E5)` nor the primary seven-connected target.  Its exact
conclusion is only that the two full contracted component vertices, the
two boundary triangles, the complete `r_1`--`T` contact, and the stated
capacity do not alone force a `K_7^-` minor.
