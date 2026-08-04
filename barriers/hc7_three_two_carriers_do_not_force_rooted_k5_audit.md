# Internal audit: three--two carriers do not force a rooted `K_5`

**Verdict:** GREEN for the pinned source revision.  This is a separate
internal mathematical audit, not external peer review.

**Audited source:**
`barriers/hc7_three_two_carriers_do_not_force_rooted_k5.md`

**SHA-256:**
`08e8925d9337700f55d58c738824044059f4f366b26c3e9c1fb0a33443487c78`

No mathematical correction is required at this revision.

## 1. All terminal partitions have carriers

Let the three parts of `K_{2,2,2}` be

```text
{a,a'},             {b,b'},             {c,z},
```

with terminals `S={a,a',b,b',c}`.  For a two-set `B` other than
`{a,a'}` or `{b,b'}`, its two terminals lie in different parts and hence
form an edge.  The complementary terminal triple meets at least two parts,
so its induced subgraph is connected.  These two induced subgraphs are
disjoint carriers.

For the two exceptional pairs, the displayed sets

```text
{a,a',z}, {b,b',c}
```

and their symmetric counterparts are disjoint and connected.  This
exhausts all ten partitions.  An independent exhaustive check over the
ten terminal pairs confirmed the same conclusion.

## 2. Absence of a rooted clique model

Five disjoint rooted bags must place the five terminals in distinct bags.
The sixth vertex `z` is the only possible additional vertex.  Since
`aa'` is absent, adjacency between its two rooted bags requires `z` to be
placed in the bag rooted at `a` or `a'`.  Since `bb'` is absent, the same
vertex would also have to be placed in the distinct bag rooted at `b` or
`b'`.  This is impossible for disjoint bags.  Leaving `z` unused or
placing it in the bag rooted at `c` repairs neither missing adjacency.
Thus no `S`-rooted `K_5` model exists.

## 3. Four-connectivity and minimum order

The graph has minimum degree four.  More directly, after deleting at most
three vertices, any two surviving vertices in different parts are
adjacent.  If two surviving vertices lie in the same part, four vertices
lie outside that part before deletion, so at least one surviving vertex in
another part is a common neighbour.  Hence every remaining graph with at
least two vertices is connected and `K_{2,2,2}` is four-connected.

Its edge count is

```text
|E(F)|=2*2+2*2+2*2=12=4|V(F)|-12.
```

On five vertices there is no nonterminal.  For the partition having
`B={u,v}`, disjointness forces the carrier containing `B` to be exactly
the two-vertex set `{u,v}`, so feasibility forces `uv` to be an edge.
Doing this for every pair forces `K_5`; hence no five-vertex counterexample
exists.  The claimed order minimality is correct.

## 4. Exact scope

The construction refutes precisely the implication from feasibility of
all three--two terminal partitions to a five-rooted clique model, even
under four-connectivity.  It does not satisfy the density or boundary
structure of the singleton residue: it has `4n-12` edges and terminal
graph `K_5` minus a matching of order two.  It therefore does not refute
the anchored four-root reduction, `(E5)`, or the primary theorem.  No
external theorem or unbounded computational inference is used.
