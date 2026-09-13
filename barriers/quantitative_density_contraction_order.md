# Density surplus can require a large coordinated contraction

**Status:** written proof with a
[separate GREEN internal audit](quantitative_density_contraction_order_audit.md).
This refutes an
`o(r)` order allowance per unit decrease of independence number, even
under arbitrarily large density surplus. It does not refute the
[density target](../active/quantitative_star_contraction_frontier.md).
All graphs are finite and simple; minor models have disjoint connected bags.

## Exact statement

For every even integer `k>=4`, there is a graph G with `r=k^2` such that

```text
|G|=k^3=r^(3/2),      alpha(G)=k,      |G|/alpha(G)=r,
e(G)/(r^2 alpha(G))=(k-1+1/k-1/k^2)/2.
```

For each integer `1<=s<=k-1`, every minor F with `alpha(F)<=k-s`
satisfies `|G|-|F|>=r s/2`. Equality is attainable, with
`alpha(F)=k-s` and `|F|/alpha(F)>r`. Thus any prescribed constant D
is exceeded by the density surplus for all sufficiently large even k,
while the exact minimum order loss for the first independence decrease
is `r/2`.

## Construction and lower bound

Take k parts. Each part is the disjoint union of k cliques of order k;
add every edge between different parts. An independent set lies in one
part and takes at most one vertex from each of its cliques. Hence
`alpha(G)=k`. Counting internal clique edges and edges between parts gives

`e(G)=k^2 binom(k,2)+binom(k,2)k^4`,

which proves the displayed parameters. The graph is connected and has
chromatic number `k^2=r`.

Consider any model of F, permitting deletions and arbitrary bag sizes.
If an original part has singleton bags surviving in `k-s+1` distinct
cliques, those singleton vertices are independent in F: operations
elsewhere cannot create edges between them. Thus at least s cliques in
each part contain no singleton bag. All their vertices are deleted or
belong to nontrivial bags. At least `k*s*k=r s` original vertices are
affected. A deleted vertex costs one unit of order; a bag of size `b>=2`
costs `b-1>=b/2`. Therefore `|G|-|F|>=r s/2`, regardless of the allocation.

## A batch attaining the bound

Pair the k parts. In each pair, choose s cliques on either side, pair
those cliques, and contract a perfect matching between each paired pair
of cliques. This gives `r s/2` disjoint connected two-vertex bags.
Each is adjacent to every other resulting vertex: an outside vertex is
in a different part from at least one endpoint. The new bags therefore
form a universal clique. Each old part retains `k-s` untouched cliques.
Consequently

```text
|F|=k^3-r s/2,      alpha(F)=k-s,
|F|/alpha(F)=r (k-s/2)/(k-s)>r.
```

All contacts are original edges between the stated bags, so the model
lifts directly. No induction or computation is used.

The first unsupported shortcut is demanding an independence decrease
after a small amount of order loss. A complete construction may instead
cross a long interval of contractions preserving independence. The
displayed batch succeeds on this family, but does not establish a rule
for all density-surplus graphs. Its chromatic number r also excludes
the `q>=Kr`, `K>=2` premise of critical reduction R.
