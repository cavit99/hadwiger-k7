# All three--two terminal carriers do not force a rooted `K_5`

**Status:** barrier/counterexample to an intermediate claim; elementary
written proof; see the
[adjacent audit](hc7_three_two_carriers_do_not_force_rooted_k5_audit.md) for
independent verification.

## Refuted intermediate claim

> Let `F` be a graph with five prescribed vertices `S`.  Suppose that for
> every partition `S=R` disjoint union `B` with `|R|=3` and `|B|=2`, the
> graph `F` has vertex-disjoint connected subgraphs containing `R` and
> `B`, respectively.  Then `F` has an `S`-rooted `K_5`-minor model.

The claim remains false when `F` is required to be four-connected.

## Counterexample

Let

```text
F=K_{2,2,2}
```

with tripartition

```text
{a,a'},             {b,b'},             {c,z},
```

and prescribe the five terminals

```text
S={a,a',b,b',c}.
```

Thus `z` is the only nonterminal.

Every three--two partition has the required carriers.  Let `B` be its
two-set and put `R=S-B`.

- If `B` is neither `{a,a'}` nor `{b,b'}`, then `F[B]` is an edge.  The
  triple `R` meets at least two tripartition classes, so `F[R]` is
  connected.  Use `F[B]` and `F[R]`.
- If `B={a,a'}`, use the disjoint connected sets

  ```text
  {a,a',z},             {b,b',c}.
  ```

- If `B={b,b'}`, use the symmetric pair

  ```text
  {b,b',z},             {a,a',c}.
  ```

Nevertheless there is no `S`-rooted `K_5`-minor model.  Such a model
would have five disjoint bags containing the five terminals.  The only
missing edges among the terminals are the disjoint pairs `aa'` and
`bb'`.  Since `z` is the only nonterminal, repairing adjacency between
the bags rooted at `a,a'` requires `z` to belong to one of those two bags.
Repairing adjacency between the bags rooted at `b,b'` likewise requires
the same vertex `z` to belong to one of those two different bags.  The
bags are disjoint, so this is impossible.

The graph `F` is four-connected: it has minimum degree four, and after
deleting at most three vertices any surviving nonadjacent pair has every
vertex in the third tripartition class as a common neighbour.  Its order
and size are

```text
|V(F)|=6,             |E(F)|=12=4|V(F)|-12.
```

It is also minimum by order for the refuted claim.  On five vertices the
terminals exhaust the graph.  Feasibility for the partition with a given
pair `B={u,v}` forces its two-vertex carrier to be exactly `{u,v}`, so
`uv` is an edge.  Repeating this for every pair gives `K_5`.

## Exact scope

This construction shows that the three--two carrier conclusion obtained
from Du--Li--Xie--Yu, Theorem 1.2, cannot be converted directly into a
five-rooted clique model, even with four-connectivity.  It does not refute
the exact singleton-residue problem:

- its density is `4n-12`, three edges below the `4n-9` density of the
  closed shore `H`;
- its terminal graph is `K_5` minus a two-edge matching, not
  `P_3` disjoint union `K_2`; and
- it does not carry the minimum-enemy leaf cuts or high-excess descent
  structure.

Thus the carrier theorem is a valid additional constraint, but the live
anchored reduction still needs density-sensitive synchronization or
strict descent.
